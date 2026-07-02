---
title: "Peripheral Component Interconnect (part 2/2)"
source: https://en.wikipedia.org/wiki/Conventional_PCI
domain: pcie-interface
license: CC-BY-SA-4.0
tags: pci express, pcie root complex, message signaled interrupts, serial expansion bus
fetched: 2026-07-02
part: 2/2
---

## PCI bus signals

PCI bus transactions are controlled by five main control signals, two driven by the initiator of a transaction (FRAME# and IRDY#), and three driven by the target (DEVSEL#, TRDY#, and STOP#). There are two additional arbitration signals (REQ# and GNT#) that are used to obtain permission to initiate a transaction. All are active-low, meaning that the active or *asserted* state is a low voltage. Pull-up resistors on the motherboard ensure they will remain high (inactive or *deasserted*) if not driven by any device, but the PCI bus does not depend on the resistors to *change* the signal level; all devices drive the signals high for one cycle before ceasing to drive the signals.

### Signal timing

All PCI bus signals are sampled on the rising edge of the clock. Signals nominally change on the falling edge of the clock, giving each PCI device approximately one half a clock cycle to decide how to respond to the signals it observed on the rising edge, and one half a clock cycle to transmit its response to the other device.

The PCI bus requires that every time the device driving a PCI bus signal changes, one *turnaround cycle* must elapse between the time the one device stops driving the signal and the other device starts. Without this, there might be a period when both devices were driving the signal, which would interfere with bus operation.

The combination of this turnaround cycle and the requirement to drive a control line high for one cycle before ceasing to drive it means that each of the main control lines must be high for a minimum of two cycles when changing owners. The PCI bus protocol is designed so this is rarely a limitation; only in a few special cases (notably fast back-to-back transactions) is it necessary to insert additional delay to meet this requirement.

### Arbitration

Any device on a PCI bus that is capable of acting as a bus master may initiate a transaction with any other device. To ensure that only one transaction is initiated at a time, each master must first wait for a bus grant signal, GNT#, from an arbiter located on the motherboard. Each device has a separate request line REQ# that requests the bus, but the arbiter may "park" the bus grant signal at any device if there are no current requests.

The arbiter may remove GNT# at any time. A device that loses GNT# may complete its current transaction, but may not start one (by asserting FRAME#) unless it observes GNT# asserted the cycle before it begins.

The arbiter may also provide GNT# at any time, including during another master's transaction. During a transaction, either FRAME# or IRDY# or both are asserted; when both are deasserted, the bus is idle. A device may initiate a transaction at any time that GNT# is asserted and the bus is idle.

### Address phase

A PCI bus transaction begins with an *address phase*. The initiator (usually a chipset), seeing that it has GNT# and the bus is idle, drives the target address onto the AD[31:0] lines, the associated command (e.g. memory read, or I/O write) on the C/BE[3:0]# lines, and pulls FRAME# low.

Each other device examines the address and command and decides whether to respond as the target by asserting DEVSEL#. A device must respond by asserting DEVSEL# within 3 cycles. Devices that promise to respond within 1 or 2 cycles are said to have "fast DEVSEL" or "medium DEVSEL", respectively. (Actually, the time to respond is 2.5 cycles, since PCI devices must transmit all signals half a cycle early so that they can be received three cycles later.)

A device must latch the address on the first cycle; the initiator is required to remove the address and command from the bus on the following cycle, even before receiving a DEVSEL# response. The additional time is available only for interpreting the address and command after it is captured.

On the fifth cycle of the address phase (or earlier if all other devices have medium DEVSEL or faster), a catch-all "subtractive decoding" is allowed for some address ranges. This is commonly used by an ISA bus bridge for addresses within its range (24 bits for memory and 16 bits for I/O).

On the sixth cycle, if there has been no response, the initiator may abort the transaction by deasserting FRAME#. This is known as *master abort termination* and it is customary for PCI bus bridges to return all-ones data (0xFFFFFFFF) in this case. PCI devices, therefore, are generally designed to avoid using the all-ones value in important status registers, so that such an error can be easily detected by software.

#### Address phase timing

Notes:

- GNT# Irrelevant after cycle has started
- Address is only valid for one cycle.
- C/BE will provide the command following by first data phase byte enables

On the rising edge of clock 0, the initiator observes FRAME# and IRDY# both high, and GNT# low, so it drives the address, command, and asserts FRAME# in time for the rising edge of clock 1. Targets latch the address and begin decoding it. They may respond with DEVSEL# in time for clock 2 (fast DEVSEL), 3 (medium) or 4 (slow). Subtractive decode devices, seeing no other response by clock 4, may respond on clock 5. If the master does not see a response by clock 5, it will terminate the transaction and remove FRAME# on clock 6.

TRDY# and STOP# are deasserted (high) during the address phase. The initiator may assert IRDY# as soon as it is ready to transfer data, which could theoretically be as soon as clock 2.

#### Dual-cycle address

To allow 64-bit addressing, a master will present the address over two consecutive cycles. First, it sends the low-order address bits with a special "dual-cycle address" command on the C/BE[3:0]#. On the following cycle, it sends the high-order address bits and the actual command. Dual-address cycles are forbidden if the high-order address bits are zero, so devices that do not support 64-bit addressing can simply not respond to dual-cycle commands.

```
              _  0_  1_  2_  3_  4_  5_  6_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
            ___
       GNT#    \___/XXXXXXXXXXXXXXXXXXXXXXX
            _______
     FRAME#        \_______________________
                    ___ ___
   AD[31:0] -------<___X___>--------------- (Low, then high bits)
                    ___ ___ _______________
 C/BE[3:0]# -------<___X___X_______________ (DAC, then actual command)
            ___________________________
    DEVSEL#                \___\___\___\___
                         Fast Med Slow
              _   _   _   _   _   _   _   _
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
                 0   1   2   3   4   5   6
```

#### Configuration access

Addresses for PCI configuration space access use special decoding. For these, the low-order address lines specify the offset of the desired PCI configuration register, and the high-order address lines are ignored. Instead, an additional address signal, the IDSEL input, must be high before a device may assert DEVSEL#. Each slot connects a different high-order address line to the IDSEL pin and is selected using one-hot encoding on the upper address lines.

### Data phases

After the address phase (specifically, beginning with the cycle that DEVSEL# goes low) comes a burst of one or more *data phases*. In all cases, the initiator drives active-low byte select signals on the C/BE[3:0]# lines, but the data on the AD[31:0] may be driven by the initiator (in case of writes) or target (in case of reads).

During data phases, the C/BE[3:0]# lines are interpreted as active-low *byte enables*. In case of a write, the asserted signals indicate which of the four bytes on the AD bus are to be written to the addressed location. In the case of a read, they indicate which bytes the initiator is interested in. For reads, it is always legal to ignore the byte-enable signals and simply return all 32 bits; cacheable memory resources are required to always return 32 valid bits. The byte enables are mainly useful for I/O space accesses where reads have side effects.

A data phase with all four C/BE# lines deasserted is explicitly permitted by the PCI standard, and must have no effect on the target other than to advance the address in the burst access in progress.

The data phase continues until both parties are ready to complete the transfer and continue to the next data phase. The initiator asserts IRDY# (*initiator ready*) when it no longer needs to wait, while the target asserts TRDY# (*target ready*). Whichever side is providing the data must drive it on the AD bus before asserting its ready signal.

Once one of the participants asserts its ready signal, it may not become un-ready or otherwise alter its control signals until the end of the data phase. The data recipient must latch the AD bus each cycle until it sees both IRDY# and TRDY# asserted, which marks the end of the current data phase and indicates that the just-latched data is the word to be transferred.

To maintain full burst speed, the data sender then has half a clock cycle after seeing both IRDY# and TRDY# asserted to drive the next word onto the AD bus.

```
             0_  1_  2_  3_  4_  5_  6_  7_  8_  9_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
                ___         _______     ___ ___ ___
   AD[31:0] ---<___XXXXXXXXX_______XXXXX___X___X___ (If a write)
                ___             ___ _______ ___ ___
   AD[31:0] ---<___>~~~<XXXXXXXX___X_______X___X___ (If a read)
                ___ _______________ _______ ___ ___
 C/BE[3:0]# ---<___X_______________X_______X___X___ (Must always be valid)
            _______________      |  ___  |   |   |
      IRDY#              x \_______/ x \___________
            ___________________  |       |   |   |
      TRDY#              x   x \___________________
            ___________          |       |   |   |
    DEVSEL#            \___________________________
            ___                  |       |   |   |
     FRAME#    \___________________________________
              _   _   _   _   _  |_   _  |_  |_  |_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
             0   1   2   3   4   5   6   7   8   9
```

This continues the address cycle illustrated above, assuming a single address cycle with medium DEVSEL, so the target responds in time for clock 3. However, at that time, neither side is ready to transfer data. For clock 4, the initiator is ready, but the target is not. On clock 5, both are ready, and a data transfer takes place (as indicated by the vertical lines). For clock 6, the target is ready to transfer, but the initiator is not. On clock 7, the initiator becomes ready, and data is transferred. For clocks 8 and 9, both sides remain ready to transfer data, and data is transferred at the maximum possible rate (32 bits per clock cycle).

In case of a read, clock 2 is reserved for turning around the AD bus, so the target is not permitted to drive data on the bus even if it is capable of fast DEVSEL.

#### Fast DEVSEL# on reads

A target that supports fast DEVSEL could in theory begin responding to a read on the cycle after the address is presented. This cycle is, however, reserved for AD bus turnaround. Thus, a target may not drive the AD bus (and thus may not assert TRDY#) on the second cycle of a transaction. Most targets will not be this fast and will not need any special logic to enforce this condition.

### Ending transactions

Either side may request that a burst end after the current data phase. Simple PCI devices that do not support multi-word bursts will always request this immediately. Even devices that do support bursts will have some limit on the maximum length they can support, such as the end of their addressable memory.

#### Initiator burst termination

The initiator can mark any data phase as the final one in a transaction by deasserting FRAME# at the same time as it asserts IRDY#. The cycle after the target asserts TRDY#, the final data transfer is complete, both sides deassert their respective RDY# signals, and the bus is idle again. The master may not deassert FRAME# before asserting IRDY#, nor may it deassert FRAME# while waiting, with IRDY# asserted, for the target to assert TRDY#.

The only minor exception is a *master abort termination*, when no target responds with DEVSEL#. Obviously, it is pointless to wait for TRDY# in such a case. However, even in this case, the master must assert IRDY# for at least one cycle after deasserting FRAME#. (Commonly, a master will assert IRDY# before receiving DEVSEL#, so it must simply hold IRDY# asserted for one cycle longer.) This is to ensure that bus turnaround timing rules are obeyed on the FRAME# line.

#### Target burst termination

The target requests the initiator end a burst by asserting STOP#. The initiator will then end the transaction by deasserting FRAME# at the next legal opportunity; if it wishes to transfer more data, it will continue in a separate transaction. There are several ways for the target to do this:

**Disconnect with data**

If the target asserts STOP# and TRDY# at the same time, this indicates that the target wishes this to be the last data phase. For example, a target that does not support burst transfers will always do this to force single-word PCI transactions. This is the most efficient way for a target to end a burst.

**Disconnect without data**

If the target asserts STOP# without asserting TRDY#, this indicates that the target wishes to stop without transferring data. STOP# is considered equivalent to TRDY# for the purpose of ending a data phase, but no data is transferred.

**Retry**

A Disconnect without data before transferring any data is a

retry

, and unlike other PCI transactions, PCI initiators are required to pause slightly before continuing the operation. See the PCI specification for details.

**Target abort**

Normally, a target holds DEVSEL# asserted through the last data phase. However, if a target deasserts DEVSEL# before disconnecting without data (asserting STOP#), this indicates a

target abort

, which is a fatal error condition. The initiator may not retry, and typically treats it as a

bus error

. A target may not deassert DEVSEL# while waiting with TRDY# or STOP# low; it must do this at the beginning of a data phase.

It will always take at least one cycle for the initiator to notice a target-initiated disconnection request and respond by deasserting FRAME#. There are two sub-cases, which take the same amount of time, but one requires an additional data phase:

**Disconnect-A**

If the initiator observes STOP# before asserting its own IRDY#, then it can end the burst by deasserting FRAME# at the same time as it asserts IRDY#, ending the burst after the current data phase.

**Disconnect-B**

If the initiator has already asserted IRDY# (without deasserting FRAME#) by the time it observes the target's STOP#, it is committed to an additional data phase. The target must wait through an additional data phase without data, holding STOP# asserted without TRDY#, before the transaction can end.

If the initiator ends the burst at the same time as the target requests disconnection, there is no additional bus cycle.

### Burst addressing

For memory space accesses, the words in a burst may be accessed in several orders. The unnecessary low-order address bits AD[1:0] are used to convey the initiator's requested order. A target which does not support a particular order must terminate the burst after the first word. Some of these orders depend on the cache line size, which is configurable on all PCI devices.

| A[1] | A[0] | Burst order (with 16-byte cache line) |
|---|---|---|
| 0 | 0 | Linear incrementing (0x0C, 0x10, 0x14, 0x18, 0x1C, ...) |
| 0 | 1 | Cacheline toggle (0x0C, 0x08, 0x04, 0x00, 0x1C, 0x18, ...) |
| 1 | 0 | Cacheline wrap (0x0C, 0x00, 0x04, 0x08, 0x1C, 0x10, ...) |
| 1 | 1 | Reserved (disconnect after first transfer) |

If the starting offset within the cache line is zero, all of these modes reduce to the same order.

Cache line toggle and cache line wrap modes are two forms of critical-word-first cache line fetching. Toggle mode XORs the supplied address with an incrementing counter. This is the native order for Intel 486 and Pentium processors. It has the advantage that it is not necessary to know the cache line size to implement it.

PCI version 2.1 obsoleted toggle mode and added the cache line wrap mode, where fetching proceeds linearly, wrapping around at the end of each cache line. When one cache line is completely fetched, fetching jumps to the starting offset in the next cache line.

Most PCI devices only support a limited range of typical cache line sizes; if the cache line size is programmed to an unexpected value, they force single-word access.

PCI also supports burst access to I/O and configuration space, but only linear mode is supported. (This is rarely used, and may be buggy in some devices; they may not support it, but not properly force single-word access either.)

### Transaction examples

This is the highest-possible speed four-word write burst, terminated by the master:

```
             0_  1_  2_  3_  4_  5_  6_  7_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
                ___ ___ ___ ___ ___
   AD[31:0] ---<___X___X___X___X___>---<___>
                ___ ___ ___ ___ ___
 C/BE[3:0]# ---<___X___X___X___X___>---<___>
                     |   |   |   |  ___
      IRDY# ^^^^^^^^\______________/   ^^^^^
                     |   |   |   |  ___
      TRDY# ^^^^^^^^\______________/   ^^^^^
                     |   |   |   |  ___
    DEVSEL# ^^^^^^^^\______________/   ^^^^^
            ___      |   |   |  ___
     FRAME#    \_______________/ | ^^^^\____
              _   _  |_  |_  |_  |_   _   _
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
             0   1   2   3   4   5   6   7
```

On clock edge 1, the initiator starts a transaction by driving an address, command, and asserting FRAME# The other signals are idle (indicated by ^^^), pulled high by the motherboard's pull-up resistors. That might be their turnaround cycle. On cycle 2, the target asserts both DEVSEL# and TRDY#. As the initiator is also ready, a data transfer occurs. This repeats for three more cycles, but before the last one (clock edge 5), the master deasserts FRAME#, indicating that this is the end. On clock edge 6, the AD bus and FRAME# are undriven (turnaround cycle) and the other control lines are driven high for 1 cycle. On clock edge 7, another initiator can start a different transaction. This is also the turnaround cycle for the other control lines.

The equivalent read burst takes one more cycle, because the target must wait 1 cycle for the AD bus to turn around before it may assert TRDY#:

```
             0_  1_  2_  3_  4_  5_  6_  7_  8_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
                ___     ___ ___ ___ ___
   AD[31:0] ---<___>---<___X___X___X___>---<___>
                ___ _______ ___ ___ ___
 C/BE[3:0]# ---<___X_______X___X___X___>---<___>
            ___          |   |   |   |  ___
      IRDY#    ^^^^\___________________/   ^^^^^
            ___    _____ |   |   |   |  ___
      TRDY#    ^^^^     \______________/   ^^^^^
            ___          |   |   |   |  ___
    DEVSEL#    ^^^^\___________________/   ^^^^^
            ___          |   |   |  ___
     FRAME#    \___________________/ | ^^^^\____
              _   _   _  |_  |_  |_  |_   _   _
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
             0   1   2   3   4   5   6   7   8
```

A high-speed burst terminated by the target will have an extra cycle at the end:

```
             0_  1_  2_  3_  4_  5_  6_  7_  8_
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
                ___     ___ ___ ___ ___
   AD[31:0] ---<___>---<___X___X___X___XXXX>----
                ___ _______ ___ ___ ___ ___
 C/BE[3:0]# ---<___X_______X___X___X___X___>----
                         |   |   |   |      ___
      IRDY# ^^^^^^^\_______________________/
                   _____ |   |   |   |  _______
      TRDY# ^^^^^^^     \______________/
                   ________________  |      ___
      STOP# ^^^^^^^      |   |   | \_______/
                         |   |   |   |      ___
    DEVSEL# ^^^^^^^\_______________________/
            ___          |   |   |   |  ___
     FRAME#    \_______________________/   ^^^^
              _   _   _  |_  |_  |_  |_   _   _
        CLK _/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
             0   1   2   3   4   5   6   7   8
```

On clock edge 6, the target indicates that it wants to stop (with data), but the initiator is already holding IRDY# low, so there is a fifth data phase (clock edge 7), during which no data is transferred.

### Parity

The PCI bus detects parity errors, but does not attempt to correct them by retrying operations; it is purely a failure indication. Due to this, there is no need to detect the parity error before it has happened, and the PCI bus actually detects it a few cycles later. During a data phase, whichever device is driving the AD[31:0] lines computes even parity over them and the C/BE[3:0]# lines, and sends that out the PAR line one cycle later. All access rules and turnaround cycles for the AD bus apply to the PAR line, just one cycle later. The device listening on the AD bus checks the received parity and asserts the PERR# (parity error) line one cycle after that. This generally generates a processor interrupt, and the processor can search the PCI bus for the device which detected the error.

The PERR# line is only used during data phases, once a target has been selected. If a parity error is detected during an address phase (or the data phase of a Special Cycle), the devices which observe it assert the SERR# (System error) line.

Even when some bytes are masked by the C/BE# lines and not in use, they must still have *some* defined value, and this value must be used to compute the parity.

### Fast back-to-back transactions

Due to the need for a turnaround cycle between different devices driving PCI bus signals, in general it is necessary to have an idle cycle between PCI bus transactions. However, in some circumstances it is permitted to skip this idle cycle, going directly from the final cycle of one transfer (IRDY# asserted, FRAME# deasserted) to the first cycle of the next (FRAME# asserted, IRDY# deasserted).

An initiator may only perform back-to-back transactions when:

- they are by the same initiator (or there would be no time to turn around the C/BE# and FRAME# lines),
- the first transaction was a write (so there is no need to turn around the AD bus), and
- the initiator still has permission (from its GNT# input) to use the PCI bus.

Additional timing constraints may come from the need to turn around are the target control lines, particularly DEVSEL#. The target deasserts DEVSEL#, driving it high, in the cycle following the final data phase, which in the case of back-to-back transactions is the first cycle of the address phase. The second cycle of the address phase is then reserved for DEVSEL# turnaround, so if the target is different from the prior one, it must not assert DEVSEL# until the third cycle (medium DEVSEL speed).

One case where this problem cannot arise is if the initiator knows somehow (presumably because the addresses share sufficient high-order bits) that the second transfer is addressed to the same target as the prior one. In that case, it may perform back-to-back transactions. All PCI targets must support this.

It is also possible for the target to keep track of the requirements. If it never does fast DEVSEL, they are met trivially. If it does, it must wait until medium DEVSEL time unless:

- the current transaction was preceded by an idle cycle (is not back-to-back), or
- the prior transaction was to the same target, or
- the current transaction began with a double address cycle.

Targets that have this ability indicate it by a special bit in a PCI configuration register, and if all targets on a bus have it, all initiators may use back-to-back transfers freely.

A subtractive decoding bus bridge must know to expect this extra delay in the event of back-to-back cycles, to advertise back-to-back support.

### 64-bit PCI

Starting from revision 2.1, the PCI specification includes optional 64-bit support. This is provided via an extended connector which provides the 64-bit bus extensions AD[63:32], C/BE[7:4]#, and PAR64, and a number of additional power and ground pins. The 64-bit PCI connector can be distinguished from a 32-bit connector by the additional 64-bit segment.

Memory transactions between 64-bit devices may use all 64 bits to double the data transfer rate. Non-memory transactions (including configuration and I/O space accesses) may not use the 64-bit extension. During a 64-bit burst, burst addressing works just as in a 32-bit transfer, but the address is incremented twice per data phase. The starting address must be 64-bit aligned; i.e. AD2 must be 0. The data corresponding to the intervening addresses (with AD2 = 1) is carried on the upper half of the AD bus.

To initiate a 64-bit transaction, the initiator drives the starting address on the AD bus and asserts REQ64# at the same time as FRAME#. If the selected target can support a 64-bit transfer for this transaction, it replies by asserting ACK64# at the same time as DEVSEL#. A target may decide on a per-transaction basis whether to allow a 64-bit transfer.

If REQ64# is asserted during the address phase, the initiator also drives the high 32 bits of the address and a copy of the bus command on the high half of the bus. If the address requires 64 bits, a dual address cycle is still required, but the high half of the bus carries the upper half of the address and the final command code during both address phase cycles; this allows a 64-bit target to see the entire address and begin responding earlier.

If the initiator sees DEVSEL# asserted without ACK64#, it performs 32-bit data phases. The data which would have been transferred on the upper half of the bus during the first data phase is instead transferred during the second data phase. Typically, the initiator drives all 64 bits of data before seeing DEVSEL#. If ACK64# is missing, it may cease driving the upper half of the data bus.

The REQ64# and ACK64# lines are held asserted for the entire transaction save the last data phase and deasserted at the same time as FRAME# and DEVSEL#, respectively.

The PAR64 line operates just like the PAR line, but provides even parity over AD[63:32] and C/BE[7:4]#. It is only valid for address phases if REQ64# is asserted. PAR64 is only valid for data phases if both REQ64# and ACK64# are asserted.

### Cache snooping (obsolete)

PCI originally included optional support for write-back cache coherence. This required support by cacheable memory targets, which would listen to two pins from the cache on the bus, SDONE (snoop done) and SBO# (snoop backoff).

Because this was rarely implemented in practice, it was deleted from revision 2.2 of the PCI specification, and the pins re-used for SMBus access in revision 2.3.

The cache would watch all memory accesses, without asserting DEVSEL#. If it noticed an access that might be cached, it would drive SDONE low (snoop not done). A coherence-supporting target would avoid completing a data phase (asserting TRDY#) until it observed SDONE high.

In the case of a write to data that was clean in the cache, the cache would only have to invalidate its copy and would assert SDONE as soon as this was established. However, if the cache contained dirty data, the cache would have to write it back before the access could proceed. so it would assert SBO# when raising SDONE. This would signal the active target to assert STOP# rather than TRDY#, causing the initiator to disconnect and retry the operation later. In the meantime, the cache would arbitrate for the bus and write its data back to memory.

Targets supporting cache coherency are also required to terminate bursts before they cross cache lines.


## Development tools

When developing and/or troubleshooting the PCI bus, examination of hardware signals can be very important. Logic analyzers and bus analyzers are tools that collect, analyze, and decode signals for users to view in useful ways.

Companies such as Synopsys, Lattice Semiconductor and Rambus offer silicon IP cores to design semiconductor ASICs that use the PCI bus standard.

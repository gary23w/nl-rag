---
title: "Peripheral Component Interconnect (part 1/2)"
source: https://en.wikipedia.org/wiki/Conventional_PCI
domain: pcie-interface
license: CC-BY-SA-4.0
tags: pci express, pcie root complex, message signaled interrupts, serial expansion bus
fetched: 2026-07-02
part: 1/2
---

# Peripheral Component Interconnect

(Redirected from

Conventional PCI

)

**Peripheral Component Interconnect** (**PCI**) is a local computer bus for attaching hardware devices in a computer and is part of the **PCI Local Bus** standard. The PCI bus supports the functions found on a processor bus but in a standardized format that is independent of any given processor's native bus. Devices connected to the PCI bus appear to a bus master to be connected directly to its own bus and are assigned addresses in the processor's address space. It is a parallel bus, synchronous to a single bus clock.

Attached devices can take either the form of an integrated circuit fitted onto the motherboard (called a *planar device* in the PCI specification) or an expansion card that fits into a slot. The PCI Local Bus was first implemented in IBM PC compatibles, where it displaced the combination of several slow Industry Standard Architecture (ISA) slots and one fast VESA Local Bus (VLB) slot as the bus configuration. It has subsequently been adopted for other computer types. Typical PCI cards used in PCs include: network cards, sound cards, modems, extra ports such as Universal Serial Bus (USB) or serial, TV tuner cards and hard disk drive host adapters. PCI video cards replaced ISA and VLB cards until rising bandwidth needs outgrew the abilities of PCI. The preferred interface for video cards then became Accelerated Graphics Port (AGP), a superset of PCI, before giving way to PCI Express.

The first PCI specification was developed by Intel, but subsequent development of the standard became the responsibility of the *PCI Special Interest Group* (PCI-SIG). The first version of PCI found in retail desktop computers was a 32-bit bus using a 33 MHz bus clock and 5 V signaling, although the PCI 1.0 standard provided for a 64-bit variant as well. These have one locating notch in the card. Version 2.0 of the PCI standard introduced 3.3 V slots, physically distinguished by a flipped physical connector to prevent accidental insertion of 5 V cards. Universal cards, which can operate on either voltage, have two notches. Version 2.1 of the PCI standard introduced optional 66 MHz operation. A server-oriented variant of PCI, PCI Extended (PCI-X) operated at frequencies up to 133 MHz for PCI-X 1.0 and up to 533 MHz for PCI-X 2.0. An internal connector for laptop cards, called **Mini PCI**, was introduced in version 2.2 of the PCI specification. The PCI bus was also adopted as an external laptop connector standard – CardBus.

PCI and PCI-X are sometimes referred to as either **Parallel PCI** or **Conventional PCI** to distinguish them technologically from their more recent successor PCI Express, which adopted a serial, lane-based architecture. PCI's heyday in the desktop computer market was approximately 1995 to 2005. PCI and PCI-X have become obsolete for most purposes and have largely disappeared from many other modern motherboards since 2013; however they are still common on some modern desktops as of 2020 for the purposes of backward compatibility and the relative low cost to produce. Another common modern application of parallel PCI is in industrial PCs, where many specialized expansion cards, used here, never transitioned to PCI Express, just as some ISA cards never transitioned to PCI. Many kinds of devices formerly available on PCI expansion cards are now commonly integrated onto motherboards or available in USB and PCI Express versions.


## History

Work on PCI began at the Intel Architecture Labs (IAL, also Architecture Development Lab) c. 1990. A team of primarily IAL engineers defined the architecture and developed a proof of concept chipset and platform (Saturn) partnering with teams in the company's desktop PC systems and core logic product organizations.

PCI was immediately put to use in servers, replacing Micro Channel architecture (MCA) and Extended Industry Standard Architecture (EISA) as the server expansion bus of choice. In mainstream PCs, PCI was slower to replace VLB, and did not gain significant market penetration until late 1994 in second-generation Pentium PCs. By 1996, VLB was all but extinct, and manufacturers had adopted PCI even for Intel 80486 (486) computers. EISA continued to be used alongside PCI through 2000. Apple Computer adopted PCI for professional Power Macintosh computers (replacing NuBus) in mid-1995, and the consumer Performa product line (replacing LC Processor Direct Slot (PDS)) in mid-1996.

Outside the server market, the 64-bit version of plain PCI remained rare in practice though, although it was used for example by all (post-iMac) G3 and G4 Power Macintosh computers.

Later revisions of PCI added new features and performance improvements, including a 66 MHz 3.3 V standard and 133 MHz PCI-X, and the adaptation of PCI signaling to other form factors. Both PCI-X 1.0b and PCI-X 2.0 are backward compatible with some PCI standards. These revisions were used on server hardware but consumer PC hardware remained nearly all 32-bit, 33 MHz and 5 volt.

The PCI-SIG introduced the serial PCI Express in c. 2004. Since then, motherboard manufacturers gradually included fewer or zero PCI slots in favor of the new standard. Bridge adapters allow the use of legacy PCI cards with PCI Express motherboards.

| Spec | Year | Change summary |
|---|---|---|
| PCI 1.0 | 1992 | Original issue |
| PCI 2.0 | 1993 | Incorporated connector and add-in card specification |
| PCI 2.1 | 1995 | Incorporated clarifications and added 66 MHz chapter |
| PCI 2.2 | 1998 | Incorporated ECNs, and improved readability |
| PCI 2.3 | 2002 | Incorporated ECNs, errata, and deleted 5 volt only keyed add-in cards |
| PCI 3.0 | 2004 | Removed support for 5.0 volt keyed system board connector |


## Auto configuration

PCI provides separate memory and memory-mapped I/O port address spaces for the x86 processor family, 64 and 32 bits, respectively. Addresses in these address spaces are assigned by software. A third address space, called the PCI Configuration Space, which uses a fixed addressing scheme, allows software to determine the amount of memory and I/O address space needed by each device. Each device can request up to six areas of memory space or input/output (I/O) port space via its configuration space registers.

In a typical system, the firmware (or operating system) queries all PCI buses at startup time (via PCI Configuration Space) to find out what devices are present and what system resources (memory space, I/O space, interrupt lines, etc.) each needs. It then allocates the resources and tells each device what its allocation is.

The PCI configuration space also contains a small amount of device type information, which helps an operating system choose device drivers for it, or at least to have a dialogue with a user about the system configuration.

Devices may have an on-board read-only memory (ROM) containing executable code for x86 or PA-RISC processors, an Open Firmware driver, or an Option ROM. These are typically needed for devices used during system startup, before device drivers are loaded by the operating system.

In addition, there are *PCI Latency Timers* that are a mechanism for *PCI Bus-Mastering* devices to share the PCI bus fairly. "Fair" in this case means that devices will not use such a large portion of the available PCI bus bandwidth that other devices are not able to get needed work done. Note, this does not apply to PCI Express.

> How this works is that each PCI device that can operate in bus-master mode is required to implement a timer, called the Latency Timer, that limits the time that device can hold the PCI bus. The timer starts when the device gains bus ownership, and counts down at the rate of the PCI clock. When the counter reaches zero, the device is required to release the bus. If no other devices are waiting for bus ownership, it may simply grab the bus again and transfer more data.


## Interrupts

Devices are required to follow a protocol so that the interrupt-request (IRQ) lines can be shared. The PCI bus includes four interrupt lines, INTA# through INTD#, all of which are available to each device. Up to eight PCI devices share the same IRQ line (INTINA# through INTINH#) in APIC-enabled x86 systems. Interrupt lines are not wired in parallel as are the other PCI bus lines. The positions of the interrupt lines rotate between slots, so what appears to one device as the INTA# line is INTB# to the next and INTC# to the one after that. Single-function devices usually use their INTA# for interrupt signaling, so the device load is spread fairly evenly across the four available interrupt lines. This alleviates a common problem with sharing interrupts.

The mapping of PCI interrupt lines onto system interrupt lines, through the PCI host bridge, is implementation-dependent. Platform-specific firmware or operating system code is meant to know this, and set the "interrupt line" field in each device's configuration space indicating which IRQ it is connected to.

PCI interrupt lines are level-triggered. This was chosen over edge-triggering to gain an advantage when servicing a shared interrupt line, and for robustness: edge-triggered interrupts are easy to miss.

Later revisions of the PCI specification add support for message-signaled interrupts. In this system, a device signals its need for service by performing a memory write, rather than by asserting a dedicated line. This alleviates the problem of scarcity of interrupt lines. Even if interrupt vectors are still shared, it does not suffer the sharing problems of level-triggered interrupts. It also resolves the routing problem, because the memory write is not unpredictably modified between device and host. Finally, because the message signaling is in-band, it resolves some synchronization problems that can occur with posted writes and out-of-band interrupt lines.

PCI Express does not have physical interrupt lines at all. It uses message-signaled interrupts exclusively.


## Conventional hardware specifications

These specifications represent the most common version of PCI used in normal PCs:

- 33.33 MHz clock with synchronous transfers
- Peak transfer rate of 133 MB/s (133 megabytes per second) for 32-bit bus width (33.33 MHz × 32 bits ÷ 8 bits/byte = 133 MB/s)
- 32-bit bus width
- 32- or 64-bit memory address space (4 GiB or 16 EiB)
- 32-bit I/O port space
- 256-byte (per device) configuration space
- 5-volt signaling
- Reflected-wave switching

The PCI specification also provides options for 3.3 V signaling, 64-bit bus width, and 66 MHz clocking, but these are not commonly encountered outside of PCI-X support on server motherboards.

The PCI bus arbiter performs bus arbitration among multiple masters on the PCI bus. Any number of bus masters can reside on the PCI bus, as well as requests for the bus. One pair of request and grant signals is dedicated to each bus master.

### Card voltage and keying

Typical PCI cards have either one or two key notches, depending on their signaling voltage. Cards requiring 3.3 volts have a notch 56.21 mm from the card backplate in pin positions 12 and 13; those requiring 5 volts have a notch 104.41 mm from the backplate in pin positions 50 and 51. This allows cards to be fitted only into slots with a voltage they support. "Universal cards" accepting either voltage have both key notches.

### Connector pinout

The PCI connector is defined as having 62 contacts on each side of the edge connector, but two or four of them are replaced by key notches, so a card has 60 or 58 contacts on each side. Side A refers to the 'solder side' and side B refers to the 'component side': if the card is held with the connector pointing down, a view of side A will have the backplate on the right, whereas a view of side B will have the backplate on the left. The pinout of B and A sides are as follows, looking down into the motherboard connector (pins A1 and B1 are closest to backplate).

| Pin | Side B | Side A | Comments |   |
|---|---|---|---|---|
| 1 | −12 V | TRST# | JTAG port pins (optional) |   |
| 2 | TCK | +12 V |   |   |
| 3 | Ground | TMS |   |   |
| 4 | TDO | TDI |   |   |
| 5 | +5 V | +5 V |   |   |
| 6 | +5 V | INTA# | Interrupt pins (open-drain) |   |
| 7 | INTB# | INTC# |   |   |
| 8 | INTD# | +5 V |   |   |
| 9 | PRSNT1# | Reserved | Pulled low to indicate 7.5 or 25 W power required |   |
| 10 | Reserved | IOPWR | +5 V or +3.3 V |   |
| 11 | PRSNT2# | Reserved | Pulled low to indicate 7.5 or 15 W power required |   |
| 12 | Ground | Ground | Key notch for 3.3 V-capable cards |   |
| 13 | Ground | Ground |   |   |
| 14 | Reserved | 3.3 V aux | Standby power (optional) |   |
| 15 | Ground | RST# | Bus reset |   |
| 16 | CLK | IOPWR | 33/66 MHz clock |   |
| 17 | Ground | GNT# | Bus grant from motherboard to card |   |
| 18 | REQ# | Ground | Bus request from card to motherboard |   |
| 19 | IOPWR | PME# | Power management event (optional) 3.3 V, open drain, active low. |   |
| 20 | AD[31] | AD[30] | Address/data bus (upper half) |   |
| 21 | AD[29] | +3.3 V |   |   |
| 22 | Ground | AD[28] |   |   |
| 23 | AD[27] | AD[26] |   |   |
| 24 | AD[25] | Ground |   |   |
| 25 | +3.3 V | AD[24] |   |   |
| 26 | C/BE[3]# | IDSEL |   |   |
| 27 | AD[23] | +3.3 V |   |   |
| 28 | Ground | AD[22] |   |   |
| 29 | AD[21] | AD[20] |   |   |
| 30 | AD[19] | Ground |   |   |
| 31 | +3.3 V | AD[18] |   |   |
| 32 | AD[17] | AD[16] |   |   |
| 33 | C/BE[2]# | +3.3 V |   |   |
| 34 | Ground | FRAME# | Bus transfer in progress |   |
| 35 | IRDY# | Ground | Initiator ready |   |
| 36 | +3.3 V | TRDY# | Target ready |   |
| 37 | DEVSEL# | Ground | Target selected |   |
| 38 | PCIXCAP | Ground | STOP# | PCI-X capable; Target requests halt |
| 39 | LOCK# | +3.3 V | Locked transaction |   |
| 40 | PERR# | SMBCLK | *SDONE* | Parity error; SMBus clock or *Snoop done (obsolete)* |
| 41 | +3.3 V | SMBDAT | *SBO#* | SMBus data or *Snoop backoff (obsolete)* |
| 42 | SERR# | Ground | System error |   |
| 43 | +3.3 V | PAR | Even parity over AD[31:00] and C/BE[3:0]# |   |
| 44 | C/BE[1]# | AD[15] | Address/data bus (higher half) |   |
| 45 | AD[14] | +3.3 V |   |   |
| 46 | Ground | AD[13] |   |   |
| 47 | AD[12] | AD[11] |   |   |
| 48 | AD[10] | Ground |   |   |
| 49 | M66EN | Ground | AD[09] |   |
| 50 | Ground | Ground | Key notch for 5 V-capable cards |   |
| 51 | Ground | Ground |   |   |
| 52 | AD[08] | C/BE[0]# | Address/data bus (lower half) |   |
| 53 | AD[07] | +3.3 V |   |   |
| 54 | +3.3 V | AD[06] |   |   |
| 55 | AD[05] | AD[04] |   |   |
| 56 | AD[03] | Ground |   |   |
| 57 | Ground | AD[02] |   |   |
| 58 | AD[01] | AD[00] |   |   |
| 59 | IOPWR | IOPWR |   |   |
| 60 | ACK64# | REQ64# | For 64-bit extension; no connect for 32-bit devices. |   |
| 61 | +5 V | +5 V |   |   |
| 62 | +5 V | +5 V |   |   |

64-bit PCI extends this by an additional 32 contacts on each side which provide AD[63:32], C/BE[7:4]#, the PAR64 parity signal, and a number of power and ground pins.

| Ground pin | Zero volt reference |
|---|---|
| Power pin | Supplies power to the PCI card |
| Output pin | Driven by the PCI card, received by the motherboard |
| Initiator output | Driven by the master/initiator, received by the target |
| I/O signal | May be driven by initiator or target, depending on operation |
| Target output | Driven by the target, received by the initiator/master |
| Input | Driven by the motherboard, received by the PCI card |
| Open drain | May be pulled low and/or sensed by multiple cards |
| Reserved | Not presently used, do not connect |

Most lines are connected to each slot in parallel. The exceptions are:

- Each slot has its own REQ# output to, and GNT# input from the motherboard arbiter.
- Each slot has its own IDSEL line, usually connected to a specific AD line.
- TDO is daisy-chained to the following slot's TDI. Cards without JTAG support must connect TDI to TDO so as not to break the chain.
- PRSNT1# and PRSNT2# for each slot have their own pull-up resistors on the motherboard. The motherboard may (but does not have to) sense these pins to determine the presence of PCI cards and their power requirements.
- REQ64# and ACK64# are individually pulled up on 32-bit only slots.
- The interrupt pins INTA# through INTD# are connected to all slots in different orders. (INTA# on one slot is INTB# on the next and INTC# on the one after that.)

Notes:

- IOPWR is +3.3 V or +5 V, depending on the backplane. The slots also have a ridge in one of two places which prevents insertion of cards that do not have the corresponding key notch, indicating support for that voltage standard. Universal cards have both key notches and use IOPWR to determine their I/O signal levels.
- The PCI SIG strongly encourages 3.3 V PCI signaling, requiring support for it since standard revision 2.3, but most PC motherboards use the 5 V variant. Thus, while many currently available PCI cards support both, and have two key notches to indicate that, there are still a large number of 5 V-only cards on the market.
- The M66EN pin is an additional ground on 5 V PCI buses found in most PC motherboards. Cards and motherboards that do not support 66 MHz operation also ground this pin. If all participants support 66 MHz operation, a pull-up resistor on the motherboard raises this signal high and 66 MHz operation is enabled. The pin is still connected to ground via coupling capacitors on each card to preserve its AC shielding function.
- The PCIXCAP pin is an additional ground on PCI buses and cards. If all cards and the motherboard support the PCI-X protocol, a pull-up resistor on the motherboard raises this signal high and PCI-X operation is enabled. The pin is still connected to ground via coupling capacitors on each card to preserve its AC shielding function.
- At least one of PRSNT1# and PRSNT2# must be grounded by the card. The combination chosen indicates the total power requirements of the card (25 W, 15 W, or 7.5 W).
- SBO# and SDONE are signals from a cache controller to the current target. They are not initiator outputs, but are colored that way because they are target inputs.
- PME# (19 A) – Power management event (optional) which is supported in PCI version 2.2 and higher. It is a 3.3 V, open drain, active low signal. PCI cards may use this signal to send and receive PME via the PCI socket directly, which eliminates the need for a special Wake-on-LAN cable.

### Mixing of 32-bit and 64-bit PCI cards in different width slots

Most 32-bit PCI cards will function properly in 64-bit PCI-X slots, but the bus clock rate will be limited to the clock frequency of the slowest card, an inherent limitation of PCI's shared bus topology. For example, when a PCI 2.3, 66-MHz peripheral is installed into a PCI-X bus capable of 133 MHz, the entire bus backplane will be limited to 66 MHz. To get around this limitation, many motherboards have two or more PCI/PCI-X buses, with one bus intended for use with high-speed PCI-X peripherals, and the other bus intended for general-purpose peripherals.

Many 64-bit PCI-X cards are designed to work in 32-bit mode if inserted in shorter 32-bit connectors, with some loss of performance. An example of this is the Adaptec 29160 64-bit SCSI interface card. However, some 64-bit PCI-X cards do not work in standard 32-bit PCI slots.

Installing a 64-bit PCI-X card in a 32-bit slot will leave the 64-bit portion of the card edge connector not connected and overhanging. This requires that there be no motherboard components positioned so as to mechanically obstruct the overhanging portion of the card edge connector.


## Physical dimensions

PCI brackets heights:

- Standard: 120.02 mm;
- Low Profile: 79.20 mm.

PCI Card lengths (Standard Bracket & 3.3 V):

- Short Card: 169.52 mm;
- Long Card: 313.78 mm.

PCI Card lengths (Low Profile Bracket & 3.3 V):

- MD1: 121.79 mm;
- MD2: 169.52 mm;
- MD3: 243.18 mm.

- (A full-height bracket)A full-height bracket
- (A low-profile card with a full-height bracket)A low-profile card with a full-height bracket

### Mini PCI

**Mini PCI** was added to PCI version 2.2 for use in laptops and some routers; it uses a 32-bit, 33 MHz bus with powered connections (3.3 V only; 5 V is limited to 100 mA) and support for bus mastering and DMA. The standard size for Mini PCI cards is approximately a quarter of their full-sized counterparts. There is no access to the card from outside the case, unlike desktop PCI cards with brackets carrying connectors. This limits the kinds of functions a Mini PCI card can perform.

Many Mini PCI devices were developed such as Wi-Fi, Fast Ethernet, Bluetooth, modems (often Winmodems), sound cards, cryptographic accelerators, SCSI, IDE–ATA, SATA controllers and combination cards. Mini PCI cards can be used with regular PCI-equipped hardware, using Mini PCI-to-PCI *converters*. Mini PCI has been superseded by the much narrower PCI Express Mini Card.

#### Technical details of Mini PCI

Mini PCI cards have a 2 W maximum power consumption, which limits the functionality that can be implemented in this form factor. They also are required to support the CLKRUN# PCI signal used to start and stop the PCI clock for power management purposes.

There are three card form factors: Type I, Type II, and Type III cards. The card connector used for each type include: Type I and II use a 100-pin stacking connector, while Type III uses a 124-pin edge connector, i.e. the connector for Types I and II differs from that for Type III, where the connector is on the edge of a card, like with a SO-DIMM. The additional 24 pins provide the extra signals required to route I/O back through the system connector (audio, AC-Link, LAN, phone-line interface). Type II cards have RJ11 and RJ45 mounted connectors. These cards must be located at the edge of the computer or docking station so that the RJ11 and RJ45 ports can be mounted for external access.

| Type | Card on outer edge of host system | Connector | Size (mm × mm × mm) | comments |
|---|---|---|---|---|
| IA | No | 100-pin stacking | 07.50 × 70.0 × 45.00 | Large Z dimension (7.5 mm) |
| IB | 05.50 × 70.0 × 45.00 | Smaller Z dimension (5.5 mm) |   |   |
| IIA | Yes | 17.44 × 70.0 × 45.00 | Large Z dimension (17.44 mm) |   |
| IIB | 05.50 × 78.0 × 45.00 | Smaller Z dimension (5.5 mm) |   |   |
| IIIA | No | 124-pin card edge | 02.40 × 59.6 × 50.95 | Larger Y dimension (50.95 mm) |
| IIIB | 02.40 × 59.6 × 44.60 | Smaller Y dimension (44.6 mm) |   |   |

Mini PCI is distinct from 144-pin Micro PCI.


## PCI bus transactions

PCI bus traffic consists of a series of PCI bus transactions. Each transaction consists of an *address phase* followed by one or more *data phases*. The direction of the data phases may be from initiator to target (write transaction) or vice versa (read transaction), but all of the data phases must be in the same direction. Either party may pause or halt the data phases at any point. (One common example is a low-performance PCI device that does not support burst transactions, and always halts a transaction after the first data phase.)

Any PCI device may initiate a transaction. First, it must request permission from a PCI bus arbiter on the motherboard. The arbiter grants permission to one of the requesting devices. The initiator begins the address phase by broadcasting a 32-bit address plus a 4-bit command code, then waits for a target to respond. All other devices examine this address and one of them responds a few cycles later.

64-bit addressing is done using a two-stage address phase. The initiator broadcasts the low 32 address bits, accompanied by a special "dual address cycle" command code. Devices that do not support 64-bit addressing can simply not respond to that command code. The next cycle, the initiator transmits the high 32 address bits, plus the real command code. The transaction operates identically from that point on. To ensure compatibility with 32-bit PCI devices, it is forbidden to use a dual address cycle if not necessary, i.e. if the high-order address bits are all zero.

While the PCI bus transfers 32 bits per data phase, the initiator transmits 4 active-low byte enable signals indicating which 8-bit bytes are to be considered significant. In particular, a write must affect only the enabled bytes in the target PCI device. They are of little importance for memory reads, but I/O reads might have side effects. The PCI standard explicitly allows a data phase with no bytes enabled, which must behave as a no-op.

### PCI address spaces

PCI has three address spaces: memory, I/O address, and configuration.

Memory addresses are 32 bits (optionally 64 bits) in size, support caching and can be burst transactions.

I/O addresses are for compatibility with the Intel x86 architecture's I/O port address space. Although the PCI bus specification allows burst transactions in any address space, most devices only support it for memory addresses and not I/O.

Finally, PCI configuration space provides access to 256 bytes of special configuration registers per PCI device. Each PCI slot gets its own configuration space address range. The registers are used to configure devices memory and I/O address ranges they should respond to from transaction initiators. When a computer is first turned on, all PCI devices respond only to their configuration space accesses. The computer's BIOS scans for devices and assigns Memory and I/O address ranges to them.

If an address is not claimed by any device, the transaction initiator's address phase will time out causing the initiator to abort the operation. In case of reads, it is customary to supply all-ones for the read data value (0xFFFFFFFF) in this case. PCI devices therefore generally attempt to avoid using the all-ones value in important status registers, so that such an error can be easily detected by software.

### PCI command codes

There are 16 possible 4-bit command codes, and 12 of them are assigned. With the exception of the unique dual address cycle, the least significant bit of the command code indicates whether the following data phases are a read (data sent from target to initiator) or a write (data sent from an initiator to target). PCI targets must examine the command code as well as the address and not respond to address phases that specify an unsupported command code.

The commands that refer to cache lines depend on the PCI configuration space cache line size register being set up properly; they may not be used until that has been done.

**0000: Interrupt Acknowledge**

This is a special form of read cycle implicitly addressed to the interrupt controller, which returns an interrupt vector. The 32-bit address field is ignored. One possible implementation is to generate an interrupt acknowledge cycle on an ISA bus using a PCI/ISA bus bridge. This command is for

IBM PC compatibility

; if there is no

Intel 8259

style interrupt controller on the PCI bus, this cycle need never be used.

**0001: Special Cycle**

This cycle is a special broadcast write of system events that PCI card may be interested in. The address field of a special cycle is ignored, but it is followed by a data phase containing a payload message. The currently defined messages announce that the processor is stopping for some reason (e.g. to save power). No device ever responds to this cycle; it is always terminated with a master abort after leaving the data on the bus for at least 4 cycles.

**0010: I/O Read**

This performs a read from I/O space. All 32 bits of the read address are provided, so that a device may (for compatibility reasons) implement less than 4 bytes worth of I/O registers. If the byte enables request data not within the address range supported by the PCI device (e.g. a 4-byte read from a device which only supports 2 bytes of I/O address space), it must be terminated with a target abort. Multiple data cycles are permitted, using linear (simple incrementing) burst ordering.

The PCI standard is discouraging the use of I/O space in new devices, preferring that as much as possible be done through main memory mapping.

**0011: I/O Write**

This performs a write to I/O space.

**010*x*: Reserved**

A PCI device must not respond to an address cycle with these command codes.

**0110: Memory Read**

This performs a read cycle from memory space. Because the smallest memory space a PCI device is permitted to implement is 16 bytes,

the two least significant bits of the address are not needed during the address phase; equivalent information will arrive during the data phases in the form of byte select signals. They instead specify the order in which burst data must be returned.

If a device does not support the requested order, it must provide the first word and then disconnect.

If a memory space is marked as "prefetchable", then the target device must ignore the byte-select signals on a memory read and always return 32 valid bits.

**0111: Memory Write**

This operates similarly to a memory read. The byte select signals are more important in a write, as unselected bytes must not be written to memory.

Generally, PCI writes are faster than PCI reads, because a device may buffer the incoming write data and release the bus faster. For a read, it must delay the data phase until the data has been fetched.

**100*x*: Reserved**

A PCI device must not respond to an address cycle with these command codes.

**1010: Configuration Read**

This is similar to an I/O read, but reads from PCI configuration space. A device must respond only if the low 11 bits of the address specify a function and register that it implements, and if the special IDSEL signal is asserted. It must ignore the high 21 bits. Burst reads (using linear incrementing) are permitted in PCI configuration space.

Unlike I/O space, standard PCI configuration registers are defined so that reads never disturb the state of the device. It is possible for a device to have configuration space registers beyond the standard 64 bytes which have read side effects, but this is rare.

Configuration space accesses often have a few cycles of delay to allow the IDSEL lines to stabilize, which makes them slower than other forms of access. Also, a configuration space access requires a multi-step operation rather than a single machine instruction. Thus, it is best to avoid them during routine operation of a PCI device.

**1011: Configuration Write**

This operates analogously to a configuration read.

**1100: Memory Read Multiple**

This command is identical to a generic memory read, but includes the hint that a long read burst will continue beyond the end of the current cache line, and the target should internally

prefetch

a large amount of data. A target is always permitted to consider this a synonym for a generic memory read.

**1101: Dual Address Cycle**

When accessing a memory address that requires more than 32 bits to represent, the address phase begins with this command and the low 32 bits of the address, followed by a second cycle with the actual command and the high 32 bits of the address. PCI targets that do not support 64-bit addressing may simply treat this as another reserved command code and not respond to it. This command code may only be used with a non-zero high-order address word; it is forbidden to use this cycle if not necessary.

**1110: Memory Read Line**

This command is identical to a generic memory read, but includes the hint that the read will continue to the end of the cache line. A target is always permitted to consider this a synonym for a generic memory read.

**1111: Memory Write and Invalidate**

This command is identical to a generic memory write, but comes with the guarantee that one or more whole cache lines will be written, with all byte selects enabled. This is an optimization for write-back caches snooping the bus. Normally, a write-back cache holding dirty data must interrupt the write operation long enough to write its own dirty data first. If the write is performed using this command, the data to be written back is guaranteed to be irrelevant, and may simply be invalidated in the write-back cache.

This optimization only affects the snooping cache, and makes no difference to the target, which may treat this as a synonym for the memory write command.


## PCI bus latency

Soon after promulgation of the PCI specification, it was discovered that lengthy transactions by some devices, due to slow acknowledgments, long data bursts, or some combination, could cause buffer underrun or overrun in other devices. Recommendations on the timing of individual phases in Revision 2.0 were made mandatory in revision 2.1:

- A target must be able to complete the initial data phase (assert TRDY# and/or STOP#) within 16 cycles of the start of a transaction.
- An initiator must complete each data phase (assert IRDY#) within 8 cycles.

Additionally, as of revision 2.1, all initiators capable of bursting more than two data phases must implement a programmable latency timer. The timer starts counting clock cycles when a transaction starts (initiator asserts FRAME#). If the timer has expired *and* the arbiter has removed GNT#, then the initiator must terminate the transaction at the next legal opportunity. This is usually the next data phase, but Memory Write and Invalidate transactions must continue to the end of the cache line.

### Delayed transactions

Devices unable to meet those timing restrictions must use a combination of posted writes (for memory writes) and delayed transactions (for other writes and all reads). In a delayed transaction, the target records the transaction (including the write data) internally and aborts (asserts STOP# rather than TRDY#) the first data phase. The initiator *must* retry exactly the same transaction later. In the interim, the target internally performs the transaction, and waits for the retried transaction. When the retried transaction is seen, the buffered result is delivered.

A device may be the target of other transactions while completing one delayed transaction; it must remember the transaction type, address, byte selects and (if a write) data value, and only complete the correct transaction.

If the target has a limit on the number of delayed transactions that it can record internally (simple targets may impose a limit of 1), it will force those transactions to retry without recording them. They will be dealt with when the current delayed transaction is completed. If two initiators attempt the same transaction, a delayed transaction begun by one may have its result delivered to the other; this is harmless.

A target abandons a delayed transaction when a retry succeeds in delivering the buffered result, the bus is reset, or when 215=32768 clock cycles (approximately 1 ms) elapse without seeing a retry. The latter should never happen in normal operation, but it prevents a deadlock of the whole bus if one initiator is reset or malfunctions.


## PCI bus bridges

The PCI standard permits multiple independent PCI buses to be connected by bus bridges that will forward operations on one bus to another when required. Although PCI tends not to use many bus bridges, PCI Express systems use many PCI-to-PCI bridge usually called *PCI Express Root Port*; each PCI Express slot appears to be a separate bus, connected by a bridge to the others. The PCI host bridge (usually northbridge in x86 platforms) interconnect between CPU, main memory and PCI bus.

### Posted writes

Generally, when a bus bridge sees a transaction on one bus that must be forwarded to the other, the original transaction must wait until the forwarded transaction completes before a result is ready. One notable exception occurs in the case of memory writes. Here, the bridge may record the write data internally (if it has room) and signal completion of the write before the forwarded write has completed. Or, indeed, before it has begun. Such "sent but not yet arrived" writes are referred to as "posted writes", by analogy with a postal mail message. Although they offer great opportunity for performance gains, the rules governing what is permissible are somewhat intricate.

### Combining, merging, and collapsing

The PCI standard permits bus bridges to convert multiple bus transactions into one larger transaction under certain situations. This can improve the efficiency of the PCI bus.

#### Combining

Write transactions to consecutive addresses may be combined into a longer burst write, as long as the order of the accesses in the burst is the same as the order of the original writes. It is permissible to insert extra data phases with all byte enables turned off if the writes are almost consecutive.

#### Merging

Multiple writes to disjoint portions of the same word may be merged into a single write with multiple byte enables asserted. In this case, writes that were presented to the bus bridge in a particular order are merged so they occur at the same time when forwarded.

#### Collapsing

Multiple writes to the same byte or bytes may *not* be combined, for example, by performing only the second write and skipping the first write that was overwritten. This is because the PCI specification permits writes to have side effects.

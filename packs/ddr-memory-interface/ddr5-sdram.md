---
title: "DDR5 SDRAM"
source: https://en.wikipedia.org/wiki/DDR5_SDRAM
domain: ddr-memory-interface
license: CC-BY-SA-4.0
tags: ddr memory interface, double data rate, dram memory controller, ddr5 sdram
fetched: 2026-07-02
---

# DDR5 SDRAM

**Double Data Rate 5 Synchronous Dynamic Random-Access Memory** (**DDR5 SDRAM**) is a type of synchronous dynamic random-access memory. Compared to its predecessor DDR4 SDRAM, DDR5 was planned to reduce power consumption, while doubling bandwidth. The standard, originally targeted for 2018, was released on July 14, 2020.

A new feature called Decision Feedback Equalization (DFE) enables input/output (I/O) speed scalability for higher bandwidth and performance improvement. DDR5 has about the same 14 ns latency as DDR4 and DDR3. DDR5 octuples the maximum dual in-line memory module (DIMM) capacity from 64 GB to 512 GB. DDR5 also has higher frequencies than DDR4, up to 9.6 GT/s is currently possible, 8.2 GT/s translates into around 64 GB/s of bandwidth. Speeds of more than 13 GT/s have been achieved using liquid nitrogen cooling.

Rambus announced a working DDR5 DIMM in September 2017. On November 15, 2018, SK Hynix announced completion of its first DDR5 RAM chip; running at 5.2 GT/s at 1.1 V. In February 2019, SK Hynix announced a 6.4 GT/s chip, the highest speed specified by the preliminary DDR5 standard. The first production DDR5 DRAM chip was officially launched by SK Hynix on October 6, 2020.

The separate JEDEC standard Low Power Double Data Rate 5 (LPDDR5), intended for laptops and smartphones, was released in February 2019.

Compared to DDR4, DDR5 further reduces memory voltage to 1.1 V, a reduction from the 1.2 V required by DDR4. DDR5 modules incorporate on-board voltage regulators in order to reach higher speeds.

In 2024 the first CUDIMM (clocked unbuffered DIMM) and CSODIMM (clocked SODIMM) modules were introduced together with Intel Arrow Lake. These modules include a component to re-drive the clock signal to help reach higher speeds. AMD does not support CUDIMM, though Zen 5 will accept CUDIMMs in bypass mode.

In 2026 ASRock and Intel released the DDR5 HUDIMM (half unbuffered DIMM) modules, it populating one 32-bit subchannel per DIMM, designed for budget but reduced-performance computer markets. It requires the UEFI/BIOS to support HUDIMM.

## Features

### On-die ECC

Unlike DDR4, all DDR5 chips have on-die error-correction code, that detects and corrects storage errors before forwarding data to the CPU, to improve reliability and allow denser RAM chips with higher per-chip defect rate to be used.

On-die ECC happens at a lower level than true ECC memory. It does not have extra chips and data lines to the CPU and does not report any details about whether errors are detected, unlike externally-controlled ECC. Sophisticated algorithms have been built to infer the existence of corrected errors based on non-corrected errors.

### Subchannels

Each DDR5 DIMM has two independent subchannels. Earlier DIMM generations featured only a single channel and one CA (Command/Address) bus controlling the whole memory module with its 64 (for non-ECC) or 72 (for ECC) data lines. Both subchannels on a DDR5 DIMM each have their own CA bus, controlling 32 bits for non-ECC memory and either 36 or 40 data lines for ECC memory, resulting in a total number of either 64, 72 or 80 data lines. The reduced bus width is compensated by a doubled minimum burst length of 16, which preserves the minimum access size of 64 bytes, which matches the cache line size used by modern x86 microprocessors.

### Refreshing

DDR5 also decreased the refresh interval from 64 ms to 32 ms when operating up to 85°C. At 85°C to 95°C refresh times are 16 ms. The tRFC4 mechanism from DDR4 is retired. A tRFCsb timing is added.

It also provides two refresh commands: REFab and REFsb.

## Memory modules

Multiple DDR5 memory chips can be mounted on a circuit board to form memory modules. For use in personal computers and servers, DDR5 memory is usually supplied in 288-pin dual in-line memory modules, more commonly known as DIMMs. As with previous memory generations, there are multiple DIMM variants available for DDR5.

Unbuffered memory modules (UDIMMs) directly expose the memory chip interface to the module connector. Registered or load-reduced variants (RDIMMs/LRDIMMs) use additional active circuitry on the memory module in order to buffer the signals between the memory controller and the DRAM chips. This reduces the capacitive load on the DDR5 bus.

DDR5 UDIMMs use 5 V input, whereas RDIMMs and LRDIMMs use 12 V. In order to prevent damage by accidental insertion of the wrong memory type, DDR5 UDIMMs and (L)RDIMMs are not mechanically compatible. Additionally, DDR5 DIMMs are supplied with management interface power at 3.3 V, and use on-board circuitry (a power management integrated circuit and associated passive components) to convert to the lower voltage required by the memory chips. Final voltage regulation close to the point of use provides more stable power, and mirrors the development of voltage regulator modules for CPU power supplies.

## Operation

Standard DDR5 memory speeds range from 4,000 to 6,400 million transfers per second (PC5-32000 to PC5-51200). Higher speeds may be added later, as happened with previous generations. XMP profiles currently allow 8000 MT/s with 1.400 V/1.450 V, which is much higher than 1.1 V in the JEDEC standard.

Compared to DDR4 SDRAM, the minimum burst length was doubled to 16, with the option of "burst chop" after eight transfers. The addressing range is also slightly extended as follows:

- The number of chip ID bits remains at three bits, allowing up to eight stacked chips (3 → 3).
- A third bank group bit (BG2) was added, allowing up to eight bank groups (2 → 3).
- The maximum number of banks per bank group remains at four (2 → 2),
- The number of row address bits remains at 17, for a maximum of 128K rows (17 → 17).
- One more column address bit (C10) is added, allowing up to 8192 columns (1 KB pages) in ×4 chips (11 → 12).
- The least-significant three column-address bits (C0, C1, C2) are *removed*. All reads and writes must begin at a column address which is a multiple of 8 (3 → 0). This is necessary due to the internal ECC.
- One bit is reserved for addressing expansion as *either* a fourth chip ID bit (CID3) *or* an additional row address bit (R17) (0 → 1).

### Command encoding

DDR5 command encoding

Command

CS

Command/address (CA) bits

0

1

2

3

4

5

6

7

8

9

10

11

12

13

Activate

(Open a row)

L

L

L

Row R0–3

Bank

Bank group

Chip CID0–2

H

Row R4–16

R17/

CID3

reserved

L

L

H

Reserved

H

Reserved

reserved for future use

L

H

L

L

L

V

H

V

Write pattern

L

H

L

L

H

L

H

Bank

Bank group

Chip CID0–2

H

V

Column C3–10

V

AP

H

V

CID3

reserved for future use

L

H

L

L

H

H

V

H

V

Mode register write

L

H

L

H

L

L

Address MRA0–7

V

H

Data OP0-7

V

CW

V

Mode register read

L

H

L

H

L

H

Address MRA0–7

V

H

V

CW

V

Write

L

H

L

H

H

L

BL

Bank

Bank group

Chip CID0–2

H

V

Column C3–10

V

AP

WRP

V

CID3

Read

L

H

L

H

H

H

BL

Bank

Bank group

Chip CID0–2

H

V

Column C3–10

V

AP

V

CID3

Vref CA

L

H

H

L

L

L

Opcode OP0-6

L

V

Vref CS

L

H

H

L

L

L

Opcode OP0-6

H

V

Refresh all

L

H

H

L

L

H

CID3

V

H

L

Chip CID0–2

Refresh management all

L

H

H

L

L

H

CID3

V

L

Chip CID0–2

Refresh same bank

L

H

H

L

L

H

CID3

Bank

V

H

Chip CID0–2

Refresh management same bank

L

H

H

L

L

H

CID3

Bank

V

L

H

Chip CID0–2

Precharge all

L

H

H

L

H

L

CID3

V

L

Chip CID0–2

Precharge same bank

L

H

H

L

H

L

CID3

Bank

V

H

Chip CID0–2

Precharge

L

H

H

L

H

H

CID3

Bank

Bank group

Chip CID0–2

reserved for future use

L

H

H

H

L

L

V

Self-refresh entry

L

H

H

H

L

H

V

L

V

Power-down entry

L

H

H

H

L

H

V

H

ODT

V

Multi-purpose command

L

H

H

H

H

L

Opcode OP0–7

V

No operation; Power-down exit

L

H

H

H

H

H

V

Deselect (no operation)

H

X

- Signal level
  - H, high
  - L, low
  - V, valid, either low or high
  - X, irrelevant
- Logic level
  - Active
  - Inactive
  - Unused

- Control bits
  - AP, Auto-precharge
  - CW, Control word
  - BL, Burst length ≠ 16
  - WRP, Write partial
  - ODT, ODT remains enabled

The command encoding was significantly rearranged, eliminating the traditional RAS and CAS signals in favour of an system resembling LPDDR4: commands are sent using either one or two cycles with a 14-bit bus. Some simple commands (e.g. precharge) take one cycle, while any that include an address (activate, read, write) use two cycles to include 28 bits of information.

Also like LPDDR, there are now 256 8-bit mode registers, rather than eight 13-bit mode registers. Also, rather than one register (MR7) being reserved for use by the registered clock driver chip, a complete second bank of mode registers is defined (selected using the CW bit).

The new "Write pattern" command is similar to a normal write command, but instead of taking data from the bus, the range is filled in with copies of a one-byte mode register (which defaults to all-zero) instead of individual data. While this takes just as long to complete as a normal write, it frees up the data bus for operations on other banks.

The new "Precharge same bank" command precharges a given bank number in all bank groups.

The "Multi-purpose command" includes various sub-commands for training and calibration of the data bus.

The "Burst length" control bit normally requests "burst chop" mode, which transfers only 8 words (although the bank remains busy for 16 word times), but can instead be configured via a mode register to instead request a double-sized 32-word burst.

## Support

### Intel

The 12th generation Alder Lake, 13th generation Raptor Lake, as well as 14th generation Raptor Lake Refresh CPUs support both DDR5 and DDR4 but, usually, there are only DIMM sockets for either one or the other on a motherboard. Some mainboards with Intel's H610 chipset support both DDR4 and DDR5, but not simultaneously.

Sapphire Rapids server CPUs, Core Ultra Series 1 Meteor Lake mobile CPUs, and the latest Core Ultra Series 2 Arrow Lake desktop CPUs all exclusively support DDR5 and Arrow Lake also supports CUDIMM DDR5 memory standard that allows for higher default speed of 6400 MT/s.

### AMD

DDR5 and LPDDR5 are supported by the Ryzen 6000 series mobile APUs, powered by their Zen 3+ architecture. Ryzen 7000 and Ryzen 9000 series desktop processors also support DDR5 memory as standard.

Epyc fourth-generation *Genoa* and *Bergamo* server CPUs have support for 12-channel DDR5 on the SP5 socket.

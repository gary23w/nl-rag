---
title: "Random-access memory"
source: https://en.wikipedia.org/wiki/Memory_wall
domain: memory-hierarchy-design
license: CC-BY-SA-4.0
tags: memory hierarchy design, cpu cache levels, translation lookaside buffer, locality of reference
fetched: 2026-07-02
---

# Random-access memory

(Redirected from

Memory wall

)

**Random-access memory** (**RAM**; /ræm/) is a form of electronic computer memory that can be read and changed in any order, typically used to store working data and machine code. A random-access memory device allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory, in contrast with other direct-access data storage media (such as hard disks and magnetic tape), where the time required to read and write data items varies significantly depending on their physical locations on the recording medium, due to mechanical limitations such as media rotation speeds and arm movement.

In modern technology, random-access memory takes the form of integrated circuit (IC) chips with MOS (metal–oxide–semiconductor) memory cells. RAM is normally associated with volatile types of memory where stored information is lost if power is removed. The two main types of volatile random-access semiconductor memory are static random-access memory (SRAM) and dynamic random-access memory (DRAM).

Non-volatile RAM has also been developed and other types of non-volatile memories allow random access for read operations, but either do not allow write operations or have other kinds of limitations. These include most types of ROM and NOR flash memory.

The use of semiconductor RAM dates back to 1965 when IBM introduced the monolithic (single-chip) 16-bit SP95 SRAM chip for their System/360 Model 95 computer, and Toshiba used bipolar DRAM memory cells for its 180-bit Toscal BC-1411 electronic calculator, both based on bipolar transistors. While it offered higher speeds than magnetic-core memory, bipolar DRAM could not compete with the lower price of the then-dominant magnetic-core memory. In 1966, Dr. Robert Dennard invented modern DRAM architecture in which there's a single MOS transistor per capacitor. The first commercial DRAM IC chip, the 1K Intel 1103, was introduced in October 1970. Synchronous dynamic random-access memory (SDRAM) was reintroduced with the Samsung KM48SL2000 chip in 1992.

## History

Early computers used relays, mechanical counters or delay lines for main memory functions. Ultrasonic delay lines were serial devices which could only reproduce data in the order it was written. Drum memory could be expanded at relatively low cost but efficient retrieval of memory items requires knowledge of the physical layout of the drum to optimize speed. Latches built out of triode vacuum tubes, and later, out of discrete transistors, were used for smaller and faster memories such as registers. Such registers were relatively large and too costly to use for large amounts of data; generally, only a few dozen or few hundred bits of such memory could be provided.

The first practical form of random-access memory was the Williams tube. It stored data as electrically charged spots on the face of a cathode-ray tube. Since the electron beam of the CRT could read and write the spots on the tube in any order, memory was random access. The capacity of the Williams tube was a few hundred to around a thousand bits, but it was much smaller, faster, and more power-efficient than using individual vacuum tube latches. Developed at the University of Manchester in England, the Williams tube provided the medium on which the first electronically stored program was implemented in the Manchester Baby computer, which first successfully ran a program on 21 June, 1948. In fact, rather than the Williams tube memory being designed for the Baby, the Baby was a testbed to demonstrate the reliability of the memory.

Magnetic-core memory was invented in 1947 and developed up until the mid-1970s. It became a widespread form of random-access memory, relying on an array of magnetized rings. By changing the sense of each ring's magnetization, data could be stored with one bit stored per ring. Since every ring had a combination of address wires to select and read or write it, access to any memory location in any sequence was possible. Magnetic core memory was the standard form of computer memory until displaced by semiconductor memory in integrated circuits (ICs) during the early 1970s.

Prior to the development of integrated read-only memory (ROM) circuits, *permanent* (or *read-only*) random-access memory was often constructed using diode matrices driven by address decoders, or specially wound core rope memory planes.

Semiconductor memory appeared in the 1960s with bipolar memory, which used bipolar transistors. Although it was faster, it could not compete with the lower price of magnetic core memory.

### MOS RAM

In 1957, Frosch and Derick manufactured the first silicon dioxide field-effect transistors at Bell Labs, the first transistors in which drain and source were adjacent at the surface. Subsequently, in 1960, a team demonstrated a working MOSFET at Bell Labs. This led to the development of metal–oxide–semiconductor (MOS) memory by John Schmidt at Fairchild Semiconductor in 1964. In addition to higher speeds, MOS semiconductor memory was cheaper and consumed less power than magnetic core memory. The development of silicon-gate MOS integrated circuit (MOS IC) technology by Federico Faggin at Fairchild in 1968 enabled the production of MOS memory chips. MOS memory overtook magnetic core memory as the dominant memory technology in the early 1970s.

Integrated bipolar static random-access memory (SRAM) was invented by Robert H. Norman at Fairchild Semiconductor in 1963. It was followed by the development of MOS SRAM by John Schmidt at Fairchild in 1964. SRAM became an alternative to magnetic-core memory, but required six MOS transistors for each bit of data. Commercial use of SRAM began in 1965, when IBM introduced the SP95 memory chip for the System/360 Model 95.

Dynamic random-access memory (DRAM) allowed replacement of a 4- or 6-transistor latch circuit by a single transistor for each memory bit, greatly increasing memory density at the cost of volatility. Data was stored in the tiny capacitance of each transistor and had to be periodically refreshed every few milliseconds before the charge could leak away.

Toshiba's Toscal BC-1411 electronic calculator, which was introduced in 1965, used a form of capacitor bipolar DRAM, storing 180-bit data on discrete memory cells, consisting of germanium bipolar transistors and capacitors. Capacitors had also been used for earlier memory schemes, such as the drum of the Atanasoff–Berry Computer, the Williams tube and the Selectron tube. While it offered higher speeds than magnetic-core memory, bipolar DRAM could not compete with the lower price of the then-dominant magnetic-core memory.

In 1966, Robert Dennard, while examining the characteristics of MOS technology, found it was capable of building capacitors, and that storing a charge or no charge on the MOS capacitor could represent the 1 and 0 of a bit, and the MOS transistor could control writing the charge to the capacitor. This led to his development of modern DRAM architecture for which there is a single MOS transistor per capacitor. In 1967, Dennard filed a patent under IBM for a single-transistor DRAM memory cell, based on MOS technology. The first commercial DRAM IC chip was the Intel 1103, which was manufactured on an 8 μm MOS process with a capacity of 1 kbit, and was released in 1970.

The earliest DRAMs were often synchronized with the CPU clock and were used with early microprocessors. In the mid-1970s, DRAMs moved to the asynchronous design, but in the 1990s returned to synchronous operation. In 1992 Samsung released KM48SL2000, which had a capacity of 16 Mbit. The first commercial double data rate SDRAM was Samsung's 64 Mbit DDR SDRAM, released in June 1998. GDDR (graphics DDR) is a form of SGRAM (synchronous graphics RAM), which was first released by Samsung as a 16 Mbit memory chip in 1998.

## Types

In general, the term *RAM* refers solely to solid-state memory devices, and more specifically the main memory in most computers. The two widely used forms of modern RAM are static RAM (SRAM) and dynamic RAM (DRAM). In SRAM, a bit of data is stored using the state of a memory cell, typically using six MOSFETs. This form of RAM is more expensive to produce, but is generally faster and requires less static power than DRAM. In modern computers, SRAM is often used as cache memory for the CPU. DRAM stores a bit of data using a transistor and capacitor pair (typically a MOSFET and MOS capacitor, respectively), which together comprise a DRAM cell. The capacitor holds a high or low charge (1 or 0, respectively), and the transistor acts as a switch that lets the control circuitry on the chip read the capacitor's state of charge or change it. As this form of memory is less expensive to produce than static RAM, it is the predominant form of computer memory used in modern computers.

Both static and dynamic RAM are considered *volatile*, as their state is lost when power is removed from the system. By contrast, read-only memory (ROM) stores data by permanently enabling or disabling selected transistors, such that the memory cannot be altered. Writable variants of ROM (such as EEPROM and NOR flash) share properties of both ROM and RAM, enabling data to persist without power and to be updated without requiring special equipment.

ECC memory (which can be either SRAM or DRAM) includes special circuitry to detect and/or correct random faults (memory errors) in the stored data, using parity bits or error correction codes.

## Memory cell

The memory cell is the fundamental building block of computer memory. The memory cell is an electronic circuit that stores one bit of binary information. The cell can be set to store a logic 1 (high voltage level) and reset to store a logic 0 (low voltage level). Its value is maintained until it is changed by the set/reset process. The value in the memory cell can be accessed by reading it.

In SRAM, the memory cell is a type of flip-flop circuit, usually implemented using FETs. This means that SRAM requires very low power when not being accessed, but it is complex, expensive and has low storage density.

A second type, DRAM, is based around a capacitor. Charging and discharging this capacitor can store a 1 or a 0 in the cell. However, the charge in this capacitor slowly leaks away and must be refreshed periodically. Because of this refresh process, DRAM uses more power, but it can achieve greater storage densities and lower unit costs compared to SRAM.

|   |   |
|---|---|

## Addressing

To be useful, memory cells must be readable and writable. Within the RAM device, multiplexing and demultiplexing circuitry is used to select memory cells. Typically, a RAM device has a set of address lines $A_{0},A_{1},...A_{n}$ , and for each combination of bits that may be applied to these lines, a set of memory cells are selected. Due to this addressing, RAM devices virtually always have a memory capacity that is a power of two.

Usually, several memory cells share the same address. For example, a 4-bit-wide RAM chip has four memory cells for each address. Often the width of the memory and that of the microprocessor are different; for a 32-bit microprocessor, eight 4-bit RAM chips would be needed.

Often, more addresses are needed than can be provided by a single device. In that case, multiple devices are used, with external multiplexors used to select the device assigned to a specific address range. RAM is often byte addressable, although word-addressable RAM also exists.

## Memory hierarchy

Many computer systems have a memory hierarchy consisting of processor registers, on-die SRAM caches, external caches, DRAM, memory paging systems and virtual memory or swap space on a SSD or hard drive. This entire pool of memory may be referred to as RAM from a programming perspective. The overall goal of using a memory hierarchy is to obtain the fastest possible average access time while minimizing the total cost of the entire memory system.

## Other uses of RAM

In addition to serving as temporary storage and working space for the operating system and applications, RAM is used in numerous other ways.

### Virtual memory

Most modern operating systems employ a method, known as virtual memory, of extending RAM capacity. A portion of the computer's hard drive or SSD is set aside for a *paging file* or a *scratch partition*, and the combination of physical RAM and the paging file forms the system's total memory. For example, if a computer has 2 GB of RAM and a 1 GB page file, the operating system has 3 GB total memory available to it. When the system runs low on physical memory, it can swap portions of RAM to the paging file to make room for new data. When the previously swapped information is needed again, another swap is performed to read the information back into RAM. Excessive use of this mechanism results in thrashing and generally hampers overall system performance, mainly because hard drives are far slower than RAM.

### RAM disk

Software can *partition* a portion of a computer's RAM, allowing it to act as a much faster hard drive that is called a RAM drive. A RAM drive typically loses the stored data when the computer is shut down.

### Shadow RAM

Sometimes, the contents of a relatively slow ROM chip are copied to RAM to allow for shorter access times. The ROM chip is then disabled while the initialized memory locations are switched in on the same block of addresses (often write-protected). This process, sometimes called *shadowing*, is fairly common in both computers and embedded systems.

As a common example, the BIOS in typical personal computers often has an option called "use shadow BIOS" or similar. When enabled, functions that rely on data from the BIOS's ROM instead use DRAM locations (most can also toggle shadowing of video card ROM or other ROM sections). Free memory is reduced by the size of the shadowed ROMs. Depending on the system, this may not result in increased performance and may cause incompatibilities. For example, some hardware may be inaccessible to the operating system if shadow RAM is used. On some systems, the benefit may be hypothetical because the BIOS is not used after booting.

### Virtual private networks

Some virtual private network services utilize RAM servers to keep all runtime state, including session metadata and cryptographic material, in volatile memory. This is intended to improve security relative to disk-backed designs. In such a design, no data is written to hard drives; all information resides in volatile memory and is erased whenever the server is powered off or rebooted.

## Memory wall

The **memory wall** is the growing disparity of speed between CPU and the response time of memory (known as memory latency) outside the CPU chip. An important reason for this disparity is the limited communication bandwidth beyond chip boundaries. From 1986 to 2000, CPU speed improved at an annual rate of 55% while off-chip memory response time only improved at 10%. Given these trends, it was expected that memory latency would become an overwhelming bottleneck in computer performance.

Another reason for the disparity is the enormous increase in the size of memory since the start of the PC revolution in the 1980s. Originally, PCs contained less than 1 megabyte of RAM, which often had a response time of 1 CPU clock cycle, meaning that it required 0 wait states. Larger memory units are inherently slower than smaller ones of the same type, simply because it takes longer for signals to traverse a larger circuit. Constructing a memory unit of many gigabytes with a response time of one clock cycle is difficult or impossible. Modern CPUs often still have 0 wait state cache memory, but, due to the bandwidth limitations of chip-to-chip communication, it must reside on the same chip as the CPU cores. It must also be constructed from static RAM, which is far more expensive than the dynamic RAM used for larger memories.

CPU speed improvements slowed significantly, partly due to major physical barriers and partly because CPU designs have already hit the memory wall in some sense. Intel summarized these causes in a 2005 document.

> First of all, as chip geometries shrink and clock frequencies rise, the transistor leakage current increases, leading to excess power consumption and heat... Secondly, the advantages of higher clock speeds are in part negated by memory latency, since memory access times have not been able to keep pace with increasing clock frequencies. Third, for certain applications, traditional serial architectures are becoming less efficient as processors get faster (due to the so-called von Neumann bottleneck), further undercutting any gains that frequency increases might otherwise buy. In addition, partly due to limitations in the means of producing inductance within solid state devices, resistance-capacitance (RC) delays in signal transmission are growing as feature sizes shrink, imposing an additional bottleneck that frequency increases don't address.

The RC delays in signal transmission were also noted in "Clock Rate versus IPC: The End of the Road for Conventional Microarchitectures" which projected a maximum of 12.5% average annual CPU performance improvement between 2000 and 2014.

A different concept is the processor-memory performance gap, which can be addressed by 3D integrated circuits that reduce the distance between the control logic and memory cells that are further apart in a 2D chip. Memory subsystem design requires a focus on the gap, which is widening over time. The main method of bridging the gap is the use of caches; small amounts of high-speed memory that houses data associated with recent operations near the processor, speeding up access to this data in cases where they are called upon frequently. Multiple levels of caching have been developed to deal with the widening gap, and the performance of high-speed modern computers relies on evolving caching techniques. There can be up to a 53% difference between the growth in speed of processor and the lagging speed of main memory access.

Solid-state drives have continued to increase in speed, from ~400 Mbit/s via SATA3 in 2012 up to ~7 GB/s via NVMe/PCIe in 2024, closing the gap between RAM and hard disk speeds, although RAM continues to be an order of magnitude faster, with single-lane DDR5 8000 MHz capable of 128 GB/s, and modern GDDR even faster. Fast, cheap, non-volatile solid state drives have replaced some functions formerly performed by RAM, such as holding certain data for immediate availability in server farms – 1 terabyte of SSD storage can be had for $200, while 1 TB of RAM would cost thousands of dollars.

## Timeline

### SRAM

Static random-access memory

(SRAM)

Date of introduction

Chip name

Capacity (

bits

)

Access time

SRAM type

Manufacturer(s)

Process

MOSFET

Ref

March 1963

—

N/a

1

?

Bipolar

(

cell

)

Fairchild

—

N/a

—

N/a

1965

?

8

?

Bipolar

IBM

?

—

N/a

SP95

16

?

Bipolar

IBM

?

—

N/a

?

64

?

MOSFET

Fairchild

?

PMOS

1966

TMC3162

16

?

Bipolar (

TTL

)

Transitron

?

—

N/a

?

?

?

MOSFET

NEC

?

?

1968

?

64

?

MOSFET

Fairchild

?

PMOS

144

?

MOSFET

NEC

?

NMOS

512

?

MOSFET

IBM

?

NMOS

1969

?

128

?

Bipolar

IBM

?

—

N/a

1101

256

850

ns

MOSFET

Intel

12,000

nm

PMOS

1972

2102

1

kbit

?

MOSFET

Intel

?

NMOS

1974

5101

1 kbit

800 ns

MOSFET

Intel

?

CMOS

2102A

1 kbit

350 ns

MOSFET

Intel

?

NMOS (

depletion

)

1975

2114

4 kbit

450 ns

MOSFET

Intel

?

NMOS

1976

2115

1 kbit

70 ns

MOSFET

Intel

?

NMOS (

HMOS

)

2147

4 kbit

55 ns

MOSFET

Intel

?

NMOS (HMOS)

1977

?

4 kbit

?

MOSFET

Toshiba

?

CMOS

1978

HM6147

4 kbit

55 ns

MOSFET

Hitachi

3,000 nm

CMOS (

twin-well

)

TMS4016

16 kbit

?

MOSFET

Texas Instruments

?

NMOS

1980

?

16 kbit

?

MOSFET

Hitachi, Toshiba

?

CMOS

64 kbit

?

MOSFET

Matsushita

1981

?

16 kbit

?

MOSFET

Texas Instruments

2,500 nm

NMOS

October 1981

?

4 kbit

18 ns

MOSFET

Matsushita, Toshiba

2,000 nm

CMOS

1982

?

64 kbit

?

MOSFET

Intel

1,500 nm

NMOS (HMOS)

February 1983

?

64 kbit

50 ns

MOSFET

Mitsubishi

?

CMOS

1984

?

256 kbit

?

MOSFET

Toshiba

1,200 nm

CMOS

1987

?

1

Mbit

?

MOSFET

Sony

, Hitachi,

Mitsubishi

, Toshiba

?

CMOS

December 1987

?

256 kbit

10 ns

BiMOS

Texas Instruments

800 nm

BiCMOS

1990

?

4 Mbit

15–23 ns

MOSFET

NEC, Toshiba, Hitachi, Mitsubishi

?

CMOS

1992

?

16 Mbit

12–15 ns

MOSFET

Fujitsu

, NEC

400 nm

December 1994

?

512 kbit

2.5 ns

MOSFET

IBM

?

CMOS (

SOI

)

1995

?

4 Mbit

6 ns

Cache

(

SyncBurst

)

Hitachi

100 nm

CMOS

256 Mbit

?

MOSFET

Hyundai

?

CMOS

### DRAM

Dynamic random-access memory

(DRAM)

Date of introduction

Chip name

Capacity (

bits

)

DRAM type

Manufacturer(s)

Process

MOSFET

Area

Ref

1965

—

N/a

1 bit

DRAM (

cell

)

Toshiba

—

N/a

—

N/a

—

N/a

1967

—

N/a

1 bit

DRAM (cell)

IBM

—

N/a

MOS

—

N/a

1968

?

256 bit

DRAM (

IC

)

Fairchild

?

PMOS

?

1969

—

N/a

1 bit

DRAM (cell)

Intel

—

N/a

PMOS

—

N/a

1970

1102

1

kbit

DRAM (IC)

Intel,

Honeywell

?

PMOS

?

1103

1 kbit

DRAM

Intel

8,000

nm

PMOS

10 mm

2

1971

μPD403

1 kbit

DRAM

NEC

?

NMOS

?

?

2 kbit

DRAM

General Instrument

?

PMOS

13 mm

2

1972

2107

4 kbit

DRAM

Intel

?

NMOS

?

1973

?

8 kbit

DRAM

IBM

?

PMOS

19 mm

2

1975

2116

16 kbit

DRAM

Intel

?

NMOS

?

1977

?

64 kbit

DRAM

NTT

?

NMOS

35 mm

2

1979

MK4816

16 kbit

PSRAM

Mostek

?

NMOS

?

?

64 kbit

DRAM

Siemens

?

VMOS

25 mm

2

1980

?

256 kbit

DRAM

NEC, NTT

1,000–

1,500 nm

NMOS

34–42 mm

2

1981

?

288 kbit

DRAM

IBM

?

MOS

25 mm

2

1983

?

64 kbit

DRAM

Intel

1,500 nm

CMOS

20 mm

2

256 kbit

DRAM

NTT

?

CMOS

31 mm

2

January 5, 1984

?

8

Mbit

DRAM

Hitachi

?

MOS

?

February 1984

?

1 Mbit

DRAM

Hitachi, NEC

1,000 nm

NMOS

74–76 mm

2

NTT

800 nm

CMOS

53 mm

2

1984

TMS4161

64 kbit

DPRAM

(

VRAM

)

Texas Instruments

?

NMOS

?

January 1985

μPD41264

256 kbit

DPRAM (VRAM)

NEC

?

NMOS

?

June 1986

?

1 Mbit

PSRAM

Toshiba

?

CMOS

?

1986

?

4 Mbit

DRAM

NEC

800 nm

NMOS

99 mm

2

Texas Instruments, Toshiba

1,000 nm

CMOS

100–137 mm

2

1987

?

16 Mbit

DRAM

NTT

700 nm

CMOS

148 mm

2

October 1988

?

512 kbit

HSDRAM

IBM

1,000 nm

CMOS

78 mm

2

1991

?

64 Mbit

DRAM

Matsushita

,

Mitsubishi

,

Fujitsu

, Toshiba

400 nm

CMOS

?

1993

?

256 Mbit

DRAM

Hitachi, NEC

250 nm

CMOS

?

1995

?

4 Mbit

DPRAM (VRAM)

Hitachi

?

CMOS

?

January 9, 1995

?

1

Gbit

DRAM

NEC

250 nm

CMOS

?

Hitachi

160 nm

CMOS

?

1996

?

4 Mbit

FRAM

Samsung

?

NMOS

?

1997

?

4 Gbit

QLC

NEC

150 nm

CMOS

?

1998

?

4 Gbit

DRAM

Hyundai

?

CMOS

?

February 2001

?

4 Gbit

DRAM

Samsung

100 nm

CMOS

?

June 2001

TC51W3216XB

32 Mbit

PSRAM

Toshiba

?

CMOS

?

### SDRAM

Synchronous dynamic random-access memory (SDRAM)

Date of

intro-

duction

Chip

name

Capacity

(

bits

)

SDRAM

type

Manufac-

turer(s)

Pro-

cess

MOS-

FET

Area

(mm

2

)

Ref

1992

KM48SL2000

16

Mbit

SDR

Samsung

?

CMOS

?

1996

MSM5718C50

18 Mbit

RDRAM

Oki

?

CMOS

325

N64 RDRAM

36 Mbit

RDRAM

NEC

?

CMOS

?

?

1024 Mbit

SDR

Mitsubishi

150 nm

CMOS

?

1997

?

1024 Mbit

SDR

Hyundai

?

SOI

?

1998

MD5764802

64 Mbit

RDRAM

Oki

?

CMOS

325

Mar 1998

Direct RDRAM

72 Mbit

RDRAM

Rambus

?

CMOS

?

Jun 1998

?

64 Mbit

DDR

Samsung

?

CMOS

?

1998

?

64 Mbit

DDR

Hyundai

?

CMOS

?

128 Mbit

SDR

Samsung

?

CMOS

?

1999

?

128 Mbit

DDR

Samsung

?

CMOS

?

1024 Mbit

DDR

Samsung

140 nm

CMOS

?

2000

GS eDRAM

32 Mbit

eDRAM

Sony

,

Toshiba

180 nm

CMOS

279

2001

?

288 Mbit

RDRAM

Hynix

?

CMOS

?

?

DDR2

Samsung

100 nm

CMOS

?

2002

?

256 Mbit

SDR

Hynix

?

CMOS

?

2003

EE+GS eDRAM

32 Mbit

eDRAM

Sony, Toshiba

90 nm

CMOS

0

86

?

72 Mbit

DDR3

Samsung

90 nm

CMOS

?

512 Mbit

DDR2

Hynix

?

CMOS

?

Elpida

110 nm

CMOS

?

1024 Mbit

DDR2

Hynix

?

CMOS

?

2004

?

2048 Mbit

DDR2

Samsung

80 nm

CMOS

?

2005

EE+GS eDRAM

32 Mbit

eDRAM

Sony, Toshiba

65 nm

CMOS

0

86

Xenos eDRAM

80 Mbit

eDRAM

NEC

90 nm

CMOS

?

?

512 Mbit

DDR3

Samsung

80 nm

CMOS

?

2006

?

1024 Mbit

DDR2

Hynix

60 nm

CMOS

?

2008

?

?

LPDDR2

Hynix

?

Apr 2008

?

8192 Mbit

DDR3

Samsung

50 nm

CMOS

?

2008

?

16384 Mbit

DDR3

Samsung

50 nm

CMOS

?

2009

?

?

DDR3

Hynix

44 nm

CMOS

?

2048 Mbit

DDR3

Hynix

40 nm

2011

?

16384 Mbit

DDR3

Hynix

40 nm

CMOS

?

2048 Mbit

DDR4

Hynix

30 nm

CMOS

?

2013

?

?

LPDDR4

Samsung

20 nm

CMOS

?

2014

?

8192 Mbit

LPDDR4

Samsung

20 nm

CMOS

?

2015

?

12 Gbit

LPDDR4

Samsung

20 nm

CMOS

?

2018

?

8192 Mbit

LPDDR5

Samsung

10 nm

FinFET

?

128 Gbit

DDR4

Samsung

10 nm

FinFET

?

### SGRAM

Synchronous graphics random-access memory

(SGRAM)

Date of introduction

Chip name

Capacity (

bits

)

SDRAM type

Manufacturer(s)

Process

MOSFET

Area

Ref

November 1994

HM5283206

8 Mbit

SGRAM

(

SDR

)

Hitachi

350 nm

CMOS

58 mm

2

December 1994

μPD481850

8 Mbit

SGRAM (SDR)

NEC

?

CMOS

280 mm

2

1997

μPD4811650

16 Mbit

SGRAM (SDR)

NEC

350 nm

CMOS

280 mm

2

September 1998

?

16 Mbit

SGRAM (

GDDR

)

Samsung

?

CMOS

?

1999

KM4132G112

32 Mbit

SGRAM (SDR)

Samsung

?

CMOS

280 mm

2

2002

?

128 Mbit

SGRAM (

GDDR2

)

Samsung

?

CMOS

?

2003

?

256 Mbit

SGRAM (GDDR2)

Samsung

?

CMOS

?

SGRAM (

GDDR3

)

March 2005

K4D553238F

256 Mbit

SGRAM (GDDR)

Samsung

?

CMOS

77 mm

2

October 2005

?

256 Mbit

SGRAM (

GDDR4

)

Samsung

?

CMOS

?

2005

?

512 Mbit

SGRAM (GDDR4)

Hynix

?

CMOS

?

2007

?

1024 Mbit

SGRAM (

GDDR5

)

Hynix

60 nm

2009

?

2048 Mbit

SGRAM (GDDR5)

Hynix

40 nm

2010

K4W1G1646G

1024 Mbit

SGRAM (GDDR3)

Samsung

?

CMOS

100 mm

2

2012

?

4096 Mbit

SGRAM (GDDR3)

SK Hynix

?

CMOS

?

March 2016

MT58K256M32JA

8 Gbit

SGRAM (

GDDR5X

)

Micron

20 nm

CMOS

140 mm

2

January 2018

K4ZAF325BM

16 Gbit

SGRAM (

GDDR6

)

Samsung

10 nm

FinFET

225 mm

2

---
title: "Flash memory (part 2/2)"
source: https://en.wikipedia.org/wiki/Flash_memory
domain: embedded-systems
license: CC-BY-SA-4.0
tags: embedded system, microcontroller, firmware, bare metal, bootloader, mcu
fetched: 2026-07-02
part: 2/2
---

## Distinction between NOR and NAND flash

NOR and NAND flash differ in two important ways:

- The connections of the individual memory cells are different.
- The interface provided for reading and writing the memory is different; NOR allows random access as it can be either byte-addressable or word-addressable, with words being for example 32 bits long, while NAND allows only page access.

NOR and NAND flash get their names from the structure of the interconnections between memory cells. In NOR flash, cells are connected in parallel to the bit lines, allowing cells to be read and programmed individually. The parallel connection of cells resembles the parallel connection of transistors in a CMOS NOR gate. In NAND flash, cells are connected in series, resembling a CMOS NAND gate. The series connections consume less space than parallel ones, reducing the cost of NAND flash. It does not, by itself, prevent NAND cells from being read and programmed individually.

Each NOR flash cell is larger than a NAND flash cell – 10 F2 vs 4 F2 – even when using exactly the same semiconductor device fabrication and so each transistor, contact, etc. is exactly the same size – because NOR flash cells require a separate metal contact for each cell.

Because of the series connection and removal of wordline contacts, a large grid of NAND flash memory cells will occupy perhaps only 60% of the area of equivalent NOR cells (assuming the same CMOS process resolution, for example, 130 nm, 90 nm, or 65 nm). NAND flash's designers realized that the area of a NAND chip, and thus the cost, could be further reduced by removing the external address and data bus circuitry. Instead, external devices could communicate with NAND flash via sequential-accessed command and data registers, which would internally retrieve and output the necessary data. This design choice made random-access of NAND flash memory impossible, but the goal of NAND flash was to replace mechanical hard disks, not to replace ROMs.

The first GSM phones and many feature phones had NOR flash memory, from which processor instructions could be executed directly in an execute-in-place architecture and allowed for short boot times. With smartphones, NAND flash memory was adopted as it has larger storage capacities and lower costs, but causes longer boot times because instructions cannot be executed from it directly, and must be copied to RAM memory first before execution.

| Attribute | NAND | NOR |
|---|---|---|
| Main application | File storage | Code execution |
| Storage capacity | Higher | Lower |
| Cost per bit | Lower | Higher |
| Active power | Lower | Higher |
| Standby power | Higher | Lower |
| Write speed | Faster | Slower |
| Random read speed | Slower | Faster |
| Execute in place (XIP) | No | Yes |
| Reliability | Lower | Higher |
| Required flash memory controller | Usually Yes | No |

### Write endurance

The write endurance of SLC floating-gate NOR flash is typically equal to or greater than that of NAND flash, while MLC NOR and NAND flash have similar endurance capabilities. Examples of endurance cycle ratings listed in datasheets for NAND and NOR flash, as well as in storage devices using flash memory, are provided.

| Type of flash memory | Endurance rating (erases per block) | Example(s) of flash memory or storage device |
|---|---|---|
| SLC NAND | 50,000–100,000 | Samsung OneNAND KFW4G16Q2M, Toshiba SLC NAND flash chips, Transcend SD500, Fujitsu S26361-F3298 |
| MLC NAND | 5,000–10,000 for medium-capacity; 1,000 to 3,000 for high-capacity | Samsung K9G8G08U0M (example for medium-capacity applications), Memblaze PBlaze4, ADATA SU900, Mushkin Reactor |
| TLC NAND | 1,000 | Samsung SSD 840 |
| QLC NAND | Unknown | SanDisk X4 NAND flash SD cards |
| 3D SLC NAND | >100,000 | Samsung Z-NAND |
| 3D MLC NAND | 6,000–40,000 | Samsung SSD 850 PRO, Samsung SSD 845DC PRO, Samsung 860 PRO |
| 3D TLC NAND | 1,500–5,000 | Samsung SSD 850 EVO, Samsung SSD 845DC EVO, Crucial MX300，Memblaze PBlaze5 900, Memblaze PBlaze5 700, Memblaze PBlaze5 910/916, Memblaze PBlaze5 510/516, ADATA SX 8200 PRO (also being sold under "XPG Gammix" branding, model S11 PRO) |
| 3D QLC NAND | 100–1,500 | Samsung SSD 860 QVO SATA, Intel SSD 660p, Micron 5210 ION, Crucial P1, Samsung SSD BM991 NVMe |
| 3D PLC NAND | Unknown | In development by SK Hynix (formerly Intel) and Kioxia (formerly Toshiba Memory). |
| SLC (floating- gate) NOR | 100,000–1,000,000 | Numonyx M58BW (Endurance rating of 100,000 erases per block); Spansion S29CD016J (Endurance rating of 1,000,000 erases per block) |
| MLC (floating- gate) NOR | 100,000 | Numonyx J3 flash |
| 3D SLC NOR | >1,000,000 |   |
| 3D MLC NOR | 100,000-1,000,000 |   |

However, by applying certain algorithms and design paradigms, such as wear leveling, flash over-provisioning and high-quality flash memory (such as pSLC and eTLC), the endurance of a storage system can be tuned to serve specific requirements.

In order to compute the longevity of the NAND flash, one must account for the size of the memory chip, the type of memory (e.g. SLC/MLC/TLC), and use pattern. Industrial NAND and server NAND are in demand due to their capacity, longer endurance and reliability in sensitive environments.

As the number of bits per cell increases, performance and life of NAND flash may degrade, increasing random read times to 100μs for TLC NAND which is 4 times the time required in SLC NAND, and twice the time required in MLC NAND, for random reads.


## Flash file systems

Because of the particular characteristics of flash memory, it is best used with either a controller to perform wear leveling and error correction or specifically designed flash file systems, which spread writes over the media and deal with the long erase times of NOR flash blocks. The basic concept behind flash file systems is the following: when the flash store is to be updated, the file system will write a new copy of the changed data to a fresh block, remap the file pointers, then erase the old block later when it has time.

In practice, flash file systems are used only for memory technology devices (MTDs), which are embedded flash memories that do not have a controller. Removable flash memory cards, SSDs, eMMC/eUFS chips and USB flash drives have built-in controllers to perform wear leveling and error correction so use of a specific flash file system may not add benefit.


## Capacity

Multiple chips are often arrayed or die stacked to achieve higher capacities for use in consumer electronic devices such as multimedia players or GPSs. The capacity scaling (increase) of flash chips used to follow Moore's law because they are manufactured with many of the same integrated circuits techniques and equipment. Since the introduction of 3D NAND, scaling is no longer necessarily associated with Moore's law since ever smaller transistors (cells) are no longer used.

Consumer flash storage devices typically are advertised with usable sizes expressed as a small integer power of two (2, 4, 8, etc.) and a conventional designation of megabytes (MB) or gigabytes (GB); e.g., 512 MB, 8 GB. This includes SSDs marketed as hard drive replacements, in accordance with traditional hard drives, which use decimal prefixes. Thus, an SSD marked as "64 GB" is at least 64 × 10003 bytes (64 GB). Most users will have slightly less capacity than this available for their files, due to the space taken by file system metadata and because some operating systems report SSD capacity using binary prefixes which are somewhat larger than conventional prefixes .

The flash memory chips inside them are sized in strict binary multiples, but the actual total capacity of the chips is not usable at the drive interface. It is considerably larger than the advertised capacity in order to allow for distribution of writes (wear leveling), for sparing, for error correction codes, and for other metadata needed by the device's internal firmware.

In 2005, Toshiba and SanDisk developed a NAND flash chip capable of storing 1 GB of data using multi-level cell (MLC) technology, capable of storing two bits of data per cell. In September 2005, Samsung Electronics announced that it had developed the world's first 2 GB chip.

In March 2006, Samsung announced flash hard drives with capacity of 4 GB, essentially the same order of magnitude as smaller laptop hard drives, and in September 2006, Samsung announced an 8 GB chip produced using a 40 nm manufacturing process. In January 2008, SanDisk announced availability of their 16 GB MicroSDHC and 32 GB SDHC Plus cards.

More recent flash drives (as of 2012) have much greater capacities, holding 64, 128, and 256 GB.

A joint development at Intel and Micron will allow the production of 32-layer 3.5 terabyte (TB) NAND flash sticks and 10 TB standard-sized SSDs. The device includes 5 packages of 16 × 48 GB TLC dies, using a floating gate cell design.

Flash chips continue to be manufactured with capacities under or around 1 MB (e.g. for BIOS-ROMs and embedded applications).

In July 2016, Samsung announced the 4 TB Samsung 850 EVO which utilizes their 256 Gbit 48-layer TLC 3D V-NAND. In August 2016, Samsung announced a 32 TB 2.5-inch SAS SSD based on their 512 Gbit 64-layer TLC 3D V-NAND. Further, Samsung expects to unveil SSDs with up to 100 TB of storage by 2020.


## Transfer rates

Flash memory devices are typically much faster at reading than writing. Performance also depends on the quality of storage controllers, which become more critical when devices are partially full. Even when the only change to manufacturing is die-shrink, the absence of an appropriate controller can result in degraded speeds.


## Applications

### Serial flash

Serial flash is a small, low-power flash memory that provides only serial access to the data - rather than addressing individual bytes, the user reads or writes large contiguous groups of bytes in the address space serially. Serial Peripheral Interface Bus (SPI) is a typical protocol for accessing the device. When incorporated into an embedded system, serial flash requires fewer wires on the PCB than parallel flash memories, since it transmits and receives data one bit at a time. This may permit a reduction in board space, power consumption, and total system cost.

There are several reasons why a serial device, with fewer external pins than a parallel device, can significantly reduce overall cost:

- Many ASICs are pad-limited, meaning that the size of the die is constrained by the number of wire bond pads, rather than the complexity and number of gates used for the device logic. Eliminating bond pads thus permits a more compact integrated circuit, on a smaller die; this increases the number of dies that may be fabricated on a wafer, and thus reduces the cost per die.
- Reducing the number of external pins also reduces assembly and packaging costs. A serial device may be packaged in a smaller and simpler package than a parallel device.
- Smaller and lower pin-count packages occupy less PCB area.
- Lower pin-count devices simplify PCB routing.

There are two major SPI flash types. The first type is characterized by small blocks and one internal SRAM block buffer allowing a complete block to be read to the buffer, partially modified, and then written back (for example, the Atmel AT45 *DataFlash* or the Micron Technology Page Erase NOR Flash). The second type has larger sectors where the smallest sectors typically found in this type of SPI flash are 4 KB, but they can be as large as 64 KB. Since this type of SPI flash lacks an internal SRAM buffer, the complete block must be read out and modified before being written back, making it slow to manage. However, the second type is cheaper than the first and is therefore a good choice when the application is code shadowing.

The two types are not easily exchangeable, since they do not have the same pinout, and the command sets are incompatible.

Most FPGAs are based on SRAM configuration cells and require an external configuration device, often a serial flash chip, to reload the configuration bitstream every power cycle.

#### Firmware storage

With the increasing speed of modern CPUs, parallel flash devices are often much slower than the memory bus of the computer they are connected to. Conversely, modern SRAM offers access times below 10 ns, while DDR2 SDRAM offers access times below 20 ns. Because of this, it is often desirable to shadow code stored in flash into RAM; that is, the code is copied from flash into RAM before execution, so that the CPU may access it at full speed. Device firmware may be stored in a serial flash chip, and then copied into SDRAM or SRAM when the device is powered-up. Using an external serial flash device rather than on-chip flash removes the need for significant process compromise (a manufacturing process that is good for high-speed logic is generally not good for flash and vice versa). Once it is decided to read the firmware in as one big block it is common to add compression to allow a smaller flash chip to be used. Since 2005, many devices use serial NOR flash to deprecate parallel NOR flash for firmware storage. Typical applications for serial NOR flash include storing firmware for hard drives, BIOS, Option ROM of expansion cards, DSL modems, etc.

### Flash memory as a replacement for hard drives

One more recent application for flash memory is as a replacement for hard disks. Flash memory does not have the mechanical limitations and latencies of hard drives, so a solid-state drive (SSD) is attractive in terms of speed, noise, power consumption, and reliability. Flash drives are gaining traction as mobile device secondary storage devices; they are also used as substitutes for hard drives in high-performance desktop computers and some servers with RAID and SAN architectures.

There remain some aspects of flash-based SSDs that make them unattractive. The cost per gigabyte of flash memory remains significantly higher than that of hard disks. Also, flash memory has a finite number of P/E (*program/erase*) cycles, but this seems to be currently under control since warranties on flash-based SSDs are approaching those of current hard drives. In addition, deleted files on SSDs can remain for an indefinite period of time before being overwritten by fresh data; erasure or shred techniques or software that work well on magnetic hard disk drives have no effect on SSDs, compromising security and forensic examination. However, due to the so-called *TRIM* command employed by most solid state drives, which marks the logical block addresses occupied by the deleted file as unused to enable garbage collection, data recovery software is not able to restore files deleted from such.

For relational databases or other systems that require ACID transactions, even a modest amount of flash storage can offer vast speedups over arrays of disk drives.

In May 2006, Samsung Electronics announced two flash-memory based PCs, the Q1-SSD and Q30-SSD were expected to become available in June 2006, both of which used 32 GB SSDs, and were at least initially available only in South Korea. The Q1-SSD and Q30-SSD launch was delayed and finally was shipped in late August 2006.

The first flash-memory based PC to become available was the Sony Vaio UX90, announced for pre-order on 27 June 2006 and began to be shipped in Japan on 3 July 2006 with a 16 GB flash memory hard drive. In late September 2006 Sony upgraded the flash-memory in the Vaio UX90 to 32 GB.

A solid-state drive was offered as an option with the first MacBook Air introduced in 2008, and from 2010 onwards, all models were shipped with an SSD. Starting in late 2011, as part of Intel's Ultrabook initiative, an increasing number of ultra-thin laptops are being shipped with SSDs standard.

There are also hybrid techniques such as hybrid drive and ReadyBoost that attempt to combine the advantages of both technologies, using flash as a high-speed non-volatile cache for files on the disk that are often referenced, but rarely modified, such as application and operating system executable files.

On smartphones, the NAND flash products are used as file storage device, for example, eMMC and eUFS.

### Flash memory as RAM

As of 2012, there are attempts to use flash memory as the main computer memory, DRAM.

### Archival or long-term storage

Floating-gate transistors in the flash storage device hold charge which represents data. This charge gradually leaks over time, leading to an accumulation of logical errors, also known as "bit rot" or "bit fading".

#### Data retention

It is unclear how long data on flash memory will persist under archival conditions (i.e., benign temperature and humidity with infrequent access with or without prophylactic rewrite). Datasheets of Atmel's flash-based "ATmega" microcontrollers typically promise retention times of 20 years at 85 °C (185 °F) and 100 years at 25 °C (77 °F).

The retention span varies among types and models of flash storage. When supplied with power and idle, the charge of the transistors holding the data is routinely refreshed by the firmware of the flash storage. The ability to retain data varies among flash storage devices due to differences in firmware, data redundancy, and error correction algorithms.

An article from CMU in 2015 states "Today's flash devices, which do not require flash refresh, have a typical retention age of 1 year at room temperature." And that retention time decreases exponentially with increasing temperature. The phenomenon can be modeled by the Arrhenius equation.

While flash storage retains data for a longer time if stored at colder temperatures, a higher but not extreme temperature while writing reduces stress and wear on the drive, given that electrons are able to flow more easily, according to Tim Schulte, Pranav Kalavade, and Johnmichael Hands from Intel.

### FPGA configuration

Some FPGAs are based on flash configuration cells that are used directly as (programmable) switches to connect internal elements together, using the same kind of floating-gate transistor as the flash data storage cells in data storage devices.


## Industry

One source states that, in 2008, the flash memory industry includes about US$9.1 billion in production and sales. Other sources put the flash memory market at a size of more than US$20 billion in 2006, accounting for more than eight percent of the overall semiconductor market and more than 34 percent of the total semiconductor memory market. In 2012, the market was estimated at $26.8 billion. It can take up to 10 weeks to produce a flash memory chip.

### Manufacturers

The following were the largest NAND flash memory manufacturers, as of the third quarter of 2025.

1. Samsung Electronics – 30%
2. SK Hynix – 20%
3. Kioxia – 14%
4. Micron Technology – 13%
5. YMTC – 13%
6. Western Digital Corporation – 11%

Notes: Samsung remains the largest NAND flash memory manufacturer as of Q3 2025.

Kioxia spun out and got renamed of Toshiba in 2018/2019.

SK Hynix acquired Intel's NAND business at the end of 2021.

### Shipments

| Year(s) | Discrete flash memory chips | Flash memory data capacity (gigabytes) | Floating-gate MOSFET memory cells (billions) |
|---|---|---|---|
| 1992 | 26,000,000 | 3 | 24 |
| 1993 | 73,000,000 | 17 | 139 |
| 1994 | 112,000,000 | 25 | 203 |
| 1995 | 235,000,000 | 38 | 300 |
| 1996 | 359,000,000 | 140 | 1,121 |
| 1997 | 477,200,000+ | 317+ | 2,533+ |
| 1998 | 762,195,122 | 455+ | 3,642+ |
| 1999 | 12,800,000,000 | 635+ | 5,082+ |
| 2000–2004 | 134,217,728,000 (NAND) | 1,073,741,824,000 (NAND) |   |
| 2005–2007 | ***?*** |   |   |
| 2008 | 1,226,215,645 (mobile NAND) |   |   |
| 2009 | 1,226,215,645+ (mobile NAND) |   |   |
| 2010 | 7,280,000,000+ |   |   |
| 2011 | 8,700,000,000 |   |   |
| 2012 | 5,151,515,152 (serial) |   |   |
| 2013 | ***?*** |   |   |
| 2014 | ***?*** | 59,000,000,000 | 118,000,000,000+ |
| 2015 | 7,692,307,692 (NAND) | 85,000,000,000 | 170,000,000,000+ |
| 2016 | ***?*** | 100,000,000,000 | 200,000,000,000+ |
| 2017 | ***?*** | 148,200,000,000 | 296,400,000,000+ |
| 2018 | ***?*** | 231,640,000,000 | 463,280,000,000+ |
| 2019 | ***?*** | ***?*** | ***?*** |
| 2020 | ***?*** | ***?*** | ***?*** |
| 1992–2020 | 45,358,454,134+ memory chips | 758,057,729,630+ gigabytes | 2,321,421,837,044 billion+ cells |

In addition to individual flash memory chips, flash memory is also embedded in microcontroller (MCU) chips and system-on-chip (SoC) devices. Flash memory is embedded in ARM chips, which have sold 150 billion units worldwide as of 2019, and in programmable system-on-chip (PSoC) devices, which have sold 1.1 billion units as of 2012. This adds up to at least 151.1 billion MCU and SoC chips with embedded flash memory, in addition to the 45.4 billion known individual flash chip sales as of 2015, totalling at least 196.5 billion chips containing flash memory.


## Flash scalability

Due to its relatively simple structure and high demand for higher capacity, NAND flash memory is the most aggressively scaled technology among electronic devices. The heavy competition among the top few manufacturers only adds to the aggressiveness in shrinking the floating-gate MOSFET design rule or process technology node. While the expected shrink timeline is a factor of two every three years per the original version of Moore's law, this has recently been accelerated in the case of NAND flash to a factor of two every two years.

ITRS

or company

2010

2011

2012

2013

2014

2015

2016

2017

2018

ITRS Flash Roadmap 2011

32 nm

22 nm

20

nm

18

nm

16

nm

Updated ITRS Flash Roadmap

17

nm

15

nm

14 nm

Samsung

(Samsung 3D NAND)

35–

20 nm

27

nm

21

nm

(

MLC

,

TLC

)

19–16

nm

19–

10 nm

(MLC, TLC)

19–10

nm

V-NAND (24L)

16–10

nm

V-NAND (32L)

16–10

nm

12–10

nm

12–10

nm

Micron

,

Intel

34–25

nm

25

nm

20

nm

(MLC + HKMG)

20

nm

(TLC)

16

nm

16

nm

3D NAND

16

nm

3D NAND

12

nm

3D NAND

12

nm

3D NAND

Toshiba

,

WD

(

SanDisk

)

43–32

nm

24

nm (Toshiba)

24

nm

19

nm

(MLC, TLC)

15

nm

15

nm

3D NAND

15

nm

3D NAND

12

nm

3D

NAND

12

nm

3D

NAND

SK Hynix

46–35

nm

26

nm

20

nm (MLC)

16

nm

16

nm

16

nm

12

nm

12

nm

As the MOSFET feature size of flash memory cells reaches the 15–16 nm minimum limit, further flash density increases will be driven by TLC (3 bits/cell) combined with vertical stacking of NAND memory planes. The decrease in endurance and increase in uncorrectable bit error rates that accompany feature size shrinking can be compensated by improved error correction mechanisms. Even with these advances, it may be impossible to economically scale flash to smaller and smaller dimensions as the number of electron holding capacity reduces. Many promising new technologies (such as FeRAM, MRAM, PMC, PCM, ReRAM, and others) are under investigation and development as possible more scalable replacements for flash.

### Timeline

Date of introduction

Chip name

Memory package capacity

megabits (Mb), gigabits (Gb), terabits (Tb)

Flash type

Cell type

Layers or

stacks of layers

Manufacturer(s)

Process

Area

Ref

1984

?

?

NOR

SLC

1

Toshiba

?

?

1985

?

256 kb

NOR

SLC

1

Toshiba

2,000

nm

?

1987

?

?

NAND

SLC

1

Toshiba

?

?

1989

?

1 Mb

NOR

SLC

1

Seeq, Intel

?

?

4 Mb

NAND

SLC

1

Toshiba

1,000

nm

1991

?

16 Mb

NOR

SLC

1

Mitsubishi

600

nm

?

1993

DD28F032SA

32 Mb

NOR

SLC

1

Intel

?

280

mm²

1994

?

64 Mb

NOR

SLC

1

NEC

400

nm

?

1995

?

16 Mb

DINOR

SLC

1

Mitsubishi, Hitachi

?

?

NAND

SLC

1

Toshiba

?

?

32 Mb

NAND

SLC

1

Hitachi, Samsung, Toshiba

?

?

34 Mb

Serial

SLC

1

SanDisk

1996

?

64 Mb

NAND

SLC

1

Hitachi, Mitsubishi

400

nm

?

QLC

1

NEC

128 Mb

NAND

SLC

1

Samsung, Hitachi

?

1997

?

32 Mb

NOR

SLC

1

Intel, Sharp

400

nm

?

NAND

SLC

1

AMD, Fujitsu

350

nm

1999

?

256 Mb

NAND

SLC

1

Toshiba

250

nm

?

MLC

1

Hitachi

1

2000

?

32 Mb

NOR

SLC

1

Toshiba

250

nm

?

64 Mb

NOR

QLC

1

STMicroelectronics

180

nm

512 Mb

NAND

SLC

1

Toshiba

?

?

2001

?

512 Mb

NAND

MLC

1

Hitachi

?

?

1 Gibit

NAND

MLC

1

Samsung

1

Toshiba, SanDisk

160

nm

?

2002

?

512 Mb

NROM

MLC

1

Saifun

170

nm

?

2 GB

NAND

SLC

1

Samsung, Toshiba

?

?

2003

?

128 Mb

NOR

MLC

1

Intel

130

nm

?

1 GB

NAND

MLC

1

Hitachi

2004

?

8 GB

NAND

SLC

1

Samsung

60

nm

?

2005

?

16 GB

NAND

SLC

1

Samsung

50

nm

?

2006

?

32 GB

NAND

SLC

1

Samsung

40

nm

Apr-07

THGAM

128 GB

Stacked NAND

SLC

Toshiba

56

nm

252

mm²

Sep-07

?

128 GB

Stacked NAND

SLC

Hynix

?

?

2008

THGBM

256 GB

Stacked NAND

SLC

Toshiba

43

nm

353

mm²

2009

?

32 GB

NAND

TLC

Toshiba

32

nm

113

mm²

64 GB

NAND

QLC

Toshiba, SanDisk

43

nm

?

2010

?

64 GB

NAND

SLC

Hynix

20

nm

?

TLC

Samsung

20

nm

?

THGBM2

1 Tb

Stacked NAND

QLC

Toshiba

32

nm

374

mm²

2011

KLMCG8GE4A

512 GB

Stacked NAND

MLC

Samsung

?

192

mm²

2013

?

?

NAND

SLC

SK Hynix

16

nm

?

128 GB

V-NAND

TLC

Samsung

10

nm

?

2015

?

256 GB

V-NAND

TLC

Samsung

?

?

2017

eUFS 2.1

512 GB

V-NAND

TLC

8 of 64

Samsung

?

?

768 GB

V-NAND

QLC

Toshiba

?

?

KLUFG8R1EM

4 Tb

Stacked V-NAND

TLC

Samsung

?

150

mm²

2018

?

1 Tb

V-NAND

QLC

Samsung

?

?

1.33 Tb

V-NAND

QLC

Toshiba

?

158

mm²

2019

?

512 GB

V-NAND

QLC

Samsung

?

?

1 Tb

V-NAND

TLC

SK Hynix

?

?

eUFS 2.1

1 Tb

Stacked V-NAND

QLC

16 of 64

Samsung

?

150

mm²

2023

eUFS 4.0

8 Tb

3D NAND

QLC

232

Micron

?

?

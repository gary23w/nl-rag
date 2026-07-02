---
title: "DDR SDRAM"
source: https://en.wikipedia.org/wiki/DDR_SDRAM
domain: ddr-memory-interface
license: CC-BY-SA-4.0
tags: ddr memory interface, double data rate, dram memory controller, ddr5 sdram
fetched: 2026-07-02
---

# DDR SDRAM

**Double data rate synchronous dynamic random-access memory** (**DDR SDRAM**) is a type of synchronous dynamic random-access memory (SDRAM) widely used in computers and other electronic devices. It improves on earlier SDRAM technology by transferring data on both the rising and falling edges of the clock signal, effectively doubling the data rate without increasing the clock frequency. This technique, known as double data rate (DDR), allows for higher memory bandwidth while maintaining lower power consumption and reduced signal interference.

DDR SDRAM was first introduced in the late 1990s and is sometimes referred to as DDR1 to distinguish it from later generations. It has been succeeded by DDR2 SDRAM, DDR3 SDRAM, DDR4 SDRAM, and DDR5 SDRAM, each offering further improvements in speed, capacity, and efficiency. These generations are not backward or forward compatible, meaning memory modules from different DDR versions cannot be used interchangeably on the same motherboard.

DDR SDRAM typically transfers 64 bits of data at a time. Its effective transfer rate is calculated by multiplying the memory bus clock speed by two (for double data rate), then by the width of the data bus (64 bits), and dividing by eight to convert bits to bytes. For example, a DDR module with a 100 MHz bus clock has a peak transfer rate of 1600 megabytes per second (MB/s).

## History

In the late 1980s IBM had built DRAMs using a dual-edge clocking feature and presented their results at the International Solid-State Circuits Convention in 1990. However, it was standard DRAM, not SDRAM.

Samsung demonstrated the first DDR SDRAM memory prototype in 1997, and released the first commercial DDR SDRAM chip (64 Mbit) in June 1998, followed soon after by Hyundai Electronics (now SK Hynix) the same year. The development of DDR began in 1996, before its specification was finalized by JEDEC in June 2000 (JESD79). JEDEC has set standards for the data rates of DDR SDRAM, divided into two parts. The first specification is for memory chips, and the second is for memory modules. The first retail PC motherboard using DDR SDRAM was released in August 2000.

## Specification

### Modules

To increase memory capacity and bandwidth, chips are combined on a module. For instance, the 64-bit data bus for DIMM requires eight 8-bit chips, addressed in parallel. Multiple chips with common address lines are called a memory rank. The term was introduced to avoid confusion with chip internal **rows** and **banks**. A memory module may bear more than one rank. The term **sides** would also be confusing because it incorrectly suggests the physical placement of chips on the module. All ranks are connected to the same memory bus (address + data). The chip select signal is used to issue commands to specific rank.

Adding modules to the single memory bus creates additional electrical load on its drivers. To mitigate the resulting bus signaling rate drop and overcome the memory bottleneck, new chipsets employ the multi-channel architecture.

Comparison of DDR SDRAM standards

Name

Chip

Bus

Timings

- Voltage
- (V)

Standard

Type

Module

- Clock rate
- (MHz)

- Cycle time
- (ns)

- Clock rate
- (MHz)

- Transfer rate
- (MT/s)

- Bandwidth
- (MB/s)

CL-T

RCD

-T

RP

- CAS latency
- (ns)

DDR-200

PC-1600

100

10

100

200

1600

2-2-2

20

2.5

±

0.2

DDR-266

PC-2100

133.3

3

7.5

133.3

3

266.6

6

2133.3

3

2.5-3-3

18.75

DDR-333

PC-2700

166.6

6

6

166.6

6

133.3

3

2666.6

6

2.5-3-3

15

DDR-400

A

PC-3200

200

5

200

400

3200

2.5-3-3

12.5

2.6

±

0.1

B

3-3-3

15

C

3-4-4

15

1. **Note:** All items listed above are specified by JEDEC as JESD79F. All RAM data rates in-between or above these listed specifications are not standardized by JEDEC – often they are simply manufacturer optimizations using tighter tolerances or overvolted chips. The package sizes in which DDR SDRAM is manufactured are also standardized by JEDEC.
2. Cycle time is the inverse of the I/O bus clock frequency; e.g., ⁠1/(100 MHz)⁠ = 10 ns per clock cycle.

There is no architectural difference between DDR SDRAM modules. Modules are instead designed to run at different clock frequencies: for example, a PC-1600 module is designed to run at 100 MHz, and a PC-2100 is designed to run at 133 MHz. A module's clock speed designates the data rate at which it is guaranteed to perform, hence it is guaranteed to run at lower (underclocking) and can possibly run at higher (overclocking) clock rates than those for which it was made.

DDR SDRAM modules for desktop computers, dual in-line memory modules (DIMMs), have 184 pins (as opposed to 168 pins on SDRAM, or 240 pins on DDR2 SDRAM), and can be differentiated from SDRAM DIMMs by the number of notches (DDR SDRAM has one, SDRAM has two). DDR SDRAM for notebook computers, SO-DIMMs, have 200 pins, which is the same number of pins as DDR2 SO-DIMMs. These two specifications are notched very similarly and care must be taken during insertion if unsure of a correct match. Most DDR SDRAM operates at a voltage of 2.5 V, compared to 3.3 V for SDRAM. This can significantly reduce power consumption. Chips and modules with the DDR-400/PC-3200 standard have a nominal voltage of 2.6 V.

JEDEC Standard No. 21–C defines three possible operating voltages for 184 pin DDR, as identified by the key notch position relative to its centerline. Page 4.5.10-7 defines 2.5 V (left), 1.8 V (center), TBD (right), while page 4.20.5–40 nominates 3.3 V for the right notch position. The orientation of the module for determining the key notch position is with 52 contact positions to the left and 40 contact positions to the right.

Increasing the operating voltage slightly can increase maximum speed but at the cost of higher power dissipation and heating, and at the risk of malfunctioning or damage.

#### Capacity

- **Number of DRAM devices** The number of chips is a multiple of 8 for non-ECC modules and a multiple of 9 for ECC modules. Chips can occupy one side (*single sided*) or both sides (*dual sided*) of the module. The maximal number of chips per DDR module is 36 (9 × 4) for ECC and 32 (8 x 4) for non-ECC.
- **ECC vs non-ECC** Modules that have error-correcting code are labeled as ECC.
- **Timings** CAS latency (CL), clock cycle time (tCK), row cycle time (tRC), refresh row cycle time (tRFC), row active time (tRAS).
- **Buffering** Registered (or buffered) vs. unbuffered (RDIMM vs. UDIMM).
- **Packaging**: Typically DIMM or SO-DIMM.
- **Power consumption** A test with DDR and DDR2 RAM in 2005 found that average power consumption appeared to be about 1–3 W per 512 MB module; this increases with clock rate and when in use rather than idling. A manufacturer has produced calculators to estimate the power used by various types of RAM.

#### Chip Layout

Module and chip characteristics are inherently linked.

Total module capacity is a product of one chip's capacity and the number of chips. ECC modules multiply it by 8⁄9 because they use 1 bit per byte (8 bits) for error correction. A module of any particular size can therefore be assembled either from 32 small chips (36 for ECC memory), or 16(18) or 8(9) bigger ones.

DDR memory bus width per channel is 64 bits (72 for ECC memory). Total module bit width is a product of bits per chip and number of chips. It also equals number of ranks (rows) multiplied by DDR memory bus width. Consequently, a module with a greater number of chips or using ×8 chips instead of ×4 will have more ranks.

| Module size | Number of chips | Chip size | Chip organization | Number of ranks |
|---|---|---|---|---|
| 1 GB | 36 | 256 | 64M×4 MBit | 2 |
| 1 GB | 18 | 512 | 64M×8 MBit | 2 |
| 1 GB | 18 | 512 | 128M×4 MBit | 1 |

### Chip characteristics

**DRAM density**

Size of the chip is measured in

megabits

. Most motherboards recognize only 1

GB modules if they contain

64M×8

chips (

low density

). If

128M×4

(

high density

) 1

GB modules are used, they most likely will not work. The

JEDEC

standard allows

128M×4

only for registered modules designed specifically for servers, but some generic manufacturers do not comply.

**Organization**

The notation like

64M×4

means that the memory matrix has 64 million (the product of

banks

x

rows

x

columns

) 4-bit storage locations. There are

×4, ×8,

and

×16

DDR chips. The

×4

chips allow the use of advanced error correction features like

Chipkill

,

memory scrubbing

and Intel SDDC in server environments, while the

×8

and

×16

chips are somewhat less expensive.

x8

chips are mainly used in desktops/notebooks but are making an entry into the server market. There are normally 4 banks and only one row can be active in each bank.

#### Double data rate (DDR) SDRAM specification

From Ballot JCB-99-70, and modified by numerous other Board Ballots, formulated under the cognizance of Committee JC-42.3 on DRAM Parametrics.

Standard No. 79 Revision Log:

- Release 1, June 2000
- Release 2, May 2002
- Release C, March 2003 – JEDEC Standard No. 79C.

"This comprehensive standard defines all required aspects of 64Mb through 1Gb DDR SDRAMs with X4/X8/X16 data interfaces, including features, functionality, ac and dc parametrics, packages and pin assignments. This scope will subsequently be expanded to formally apply to x32 devices, and higher density devices as well."

### Organization

PC3200 is DDR SDRAM designed to operate at 200 MHz using DDR-400 chips with a bandwidth of 3,200 MB/s. Because PC3200 memory transfers data on both the rising and falling clock edges, its effective clock rate is 400 MHz.

1 GB PC3200 non-ECC modules are usually made with 16 512 Mbit chips, 8 on each side (512 Mbits × 16 chips) / (8 bits (per byte)) = 1,024 MB. The individual chips making up a 1 GB memory module are usually organized as 226 8-bit words, commonly expressed as 64M×8. Memory manufactured in this way is low-density RAM and is usually compatible with any motherboard specifying PC3200 DDR-400 memory.

## Generations

DDR (DDR1) was superseded by DDR2 SDRAM, which had modifications for a higher clock frequency and again doubled throughput, but operates on the same principle as DDR. Competing with DDR2 was Rambus XDR DRAM. DDR2 dominated due to cost and support factors. DDR2 was in turn superseded by DDR3 SDRAM, which offered higher performance for increased bus speeds and new features. DDR3 has been superseded by DDR4 SDRAM, which was first produced in 2011 and whose standards were still in flux (2012) with significant architectural changes.

DDR's prefetch buffer depth is 2 (bits), while DDR2 uses 4. Although the effective clock rates of DDR2 are higher than DDR, the overall performance was not greater in the early implementations, primarily due to the high latencies of the first DDR2 modules. DDR2 started to be effective by the end of 2004, as modules with lower latencies became available.

Memory manufacturers stated that it was impractical to mass produce DDR1 memory with effective transfer rates in excess of 400 MHz (i.e. 400 MT/s and 200 MHz external clock) due to internal speed limitations. DDR2 picks up where DDR1 leaves off, utilizing internal clock rates similar to DDR1, but is available at effective transfer rates of 400 MHz and higher. DDR3 advances extended the ability to preserve internal clock rates while providing higher effective transfer rates by again doubling the prefetch depth.

The DDR4 SDRAM is a high-speed dynamic random-access memory internally configured as 16 banks, 4 bank groups with 4 banks for each bank group for ×4/×8 and 8 banks, 2 bank groups with 4 banks for each bank group for ×16 DRAM. The DDR4 SDRAM uses an 8*n* prefetch architecture to achieve high-speed operation. The 8*n* prefetch architecture is combined with an interface designed to transfer two data words per clock cycle at the I/O pins. A single read or write operation for the DDR4 SDRAM consists of a single 8*n*-bit-wide 4-clock data transfer at the internal DRAM core and 8 corresponding *n*-bit-wide half-clock-cycle data transfers at the I/O pins.

RDRAM was a particularly expensive alternative to DDR SDRAM, and most manufacturers dropped its support from their chipsets. DDR1 memory's prices substantially increased from Q2 2008, while DDR2 prices declined. In January 2009, 1 GB DDR1 was 2–3 times more expensive than 1 GB DDR2.

Comparison of DDR SDRAM generations

Name

Release

year

Chip

Bus

Voltage

(V)

Pins

Gen

Standard

Clock rate

(MHz)

Cycle time

(ns)

Pre-

fetch

Clock rate

(MHz)

Transfer rate

(

MT/s

)

Bandwidth

(MB/s)

DIMM

SO-

DIMM

Micro-

DIMM

DDR

DDR-200

1998

100

10.0

2n

100

200

1600

2.5

184

200

172

DDR-266

133

7.50

133

266

2133

DDR-333

166

6.00

167

333

2667

DDR-400

200

5.00

200

400

3200

2.6

DDR2

DDR2-400

2003

100

10.0

4n

200

400

3200

1.8

240

200

214

DDR2-533

133

7.50

267

533

4267

DDR2-667

167

6.00

333

667

5333

DDR2-800

200

5.00

400

800

6400

DDR2-1066

267

3.75

533

1067

8533

DDR3

DDR3-800

2007

100

10.0

8n

400

800

6400

1.5/1.35

240

204

214

DDR3-1066

133

7.50

533

1067

8533

DDR3-1333

167

6.00

667

1333

10600

DDR3-1600

200

5.00

800

1600

12800

DDR3-1866

233

4.29

933

1867

14933

DDR3-2133

267

3.75

1067

2133

17067

DDR4

DDR4-1600

2014

200

5.00

8n

800

1600

12800

1.2/1.05

288

260

-

DDR4-1866

233

4.29

933

1867

14933

DDR4-2133

267

3.75

1067

2133

17067

DDR4-2400

300

3.33

1200

2400

19200

DDR4-2666

333

3.00

1333

2667

21333

DDR4-2933

367

2.73

1467

2933

23467

DDR4-3200

400

2.50

1600

3200

25600

DDR5

DDR5-3200

2020

200

5.00

16n

1600

3200

25600

1.1

288

262

DDR5-3600

225

4.44

1800

3600

28800

DDR5-4000

250

4.00

2000

4000

32000

DDR5-4800

300

3.33

2400

4800

38400

DDR5-5000

312

3.20

2500

5000

40000

DDR5-5120

320

3.13

2560

5120

40960

DDR5-5333

333

3.00

2667

5333

42667

DDR5-5600

350

2.86

2800

5600

44800

DDR5-6400

400

2.50

3200

6400

51200

DDR5-7200

450

2.22

3600

7200

57600

### LPDDR

LPDDR is an acronym that some enterprises use for LPDDR SDRAM, a type of memory used in some portable electronic devices, like mobile phones, handhelds, and digital audio players. Through techniques including reduced voltage supply and advanced refresh options, LPDDR can achieve greater power efficiency.

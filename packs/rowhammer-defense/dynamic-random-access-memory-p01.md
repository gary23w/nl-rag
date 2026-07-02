---
title: "Dynamic random-access memory (part 1/2)"
source: https://en.wikipedia.org/wiki/Dynamic_random-access_memory
domain: rowhammer-defense
license: CC-BY-SA-4.0
tags: rowhammer defense, dram disturbance mitigation, target row refresh, bit flip attack defense
fetched: 2026-07-02
part: 1/2
---

# Dynamic random-access memory

**Dynamic random-access memory** (**dynamic RAM** or **DRAM**) is a type of random-access semiconductor memory that stores each bit of data in a memory cell. A DRAM memory cell usually consists of a microscopic capacitor and a transistor, both typically based on metal–oxide–semiconductor (MOS) technology.

While most DRAM memory cell designs use a capacitor and transistor, some only use two transistors. In the designs where a capacitor is used, the capacitor can either be charged or discharged; these two states are taken to represent the two values of a bit, conventionally called 0 and 1. The electric charge on the capacitors gradually leaks away; without intervention, the data on the capacitor would soon be lost. To prevent this, DRAM requires an external memory refresh circuit which periodically rewrites the data in the capacitors, restoring them to their original charge. This refresh process is the defining characteristic of dynamic random-access memory, in contrast to static random-access memory (SRAM) which does not require data to be refreshed. Unlike flash memory, DRAM is volatile memory (as opposed to non-volatile memory), since it loses its data quickly when power is removed. However, DRAM does exhibit limited data remanence.

DRAM typically takes the form of an integrated circuit chip, which can consist of dozens to billions of DRAM memory cells. DRAM chips are widely used in digital electronics where low-cost, high-capacity computer memory is required. One of the largest applications for DRAM is the *main memory* (colloquially called the RAM) in modern computers and graphics cards (where the main memory is called the *graphics memory*). It is also used in many portable devices and video game consoles. In contrast, SRAM, which is faster and more expensive than DRAM, is typically used where speed is of greater concern than cost and size, such as the cache memories in processors.

The need to refresh DRAM demands more complicated circuitry and timing than SRAM. This complexity is offset by the structural simplicity of DRAM memory cells: only one transistor and a capacitor are required per bit, compared to four or six transistors in SRAM. This allows DRAM to reach very high densities with a simultaneous reduction in cost per bit. Refreshing the data consumes power, causing a variety of techniques to be used to manage the overall power consumption. For this reason, DRAM usually needs to operate with a memory controller; the memory controller needs to know DRAM parameters, especially memory timings, to initialize DRAMs, which may be different depending on different DRAM manufacturers and part numbers.

DRAM had a 47% increase in the price-per-bit in 2017, the largest jump in 30 years since the 45% jump in 1988. In 2018, a "key characteristic of the DRAM market is that there are currently only three major suppliers — Micron Technology, SK Hynix and Samsung Electronics" that are "keeping a pretty tight rein on their capacity". DRAM (DDR4, DDR, and flash memory/NAND) price has in early 2026 "experienced compounded increases, some exceeding 200%, since early 2025 .. [because of] unprecedented demand coming from the AI sector .. HBM is crowding out commodity DRAM capacity. Micron noted a 3-to-1 conversion ratio between HBM and DDR5 wafer capacity, meaning every HBM ramp directly compresses general-purpose memory supply."

Other manufacturers make and sell DIMMs but not the DRAM chips in them, such as Kingston Technology, and some manufacturers sell stacked DRAM (used e.g. in the fastest supercomputers on the exascale) separately such as Viking Technology. Others sell such integrated into other products, such as Fujitsu into its CPUs, AMD in GPUs, and Nvidia, with HBM2 in some of their GPU chips.


## History

### Precursors

The cryptanalytic machine code-named *Aquarius* used at Bletchley Park during World War II incorporated a hard-wired dynamic memory. Paper tape was read and the characters on it "were remembered in a dynamic store". The store used a large bank of capacitors, which were either charged or not, a charged capacitor representing cross (1) and an uncharged capacitor dot (0). Since the charge gradually leaked away, a periodic pulse was applied to top up those still charged (hence the term 'dynamic')".

In November 1965, Toshiba introduced a bipolar dynamic RAM for its electronic calculator Toscal BC-1411. In 1966, Tomohisa Yoshimaru and Hiroshi Komikawa from Toshiba applied for a Japanese patent of a memory circuit composed of several transistors and a capacitor, in 1967 they applied for a patent in the US.

The earliest forms of DRAM mentioned above used bipolar transistors. While it offered improved performance over magnetic-core memory, bipolar DRAM could not compete with the lower price of the then-dominant magnetic-core memory. Capacitors had also been used for earlier memory schemes, such as the drum of the Atanasoff–Berry Computer, the Williams tube and the Selectron tube.

### Single MOS DRAM

In 1966, Dr. Robert Dennard invented modern DRAM architecture in which there's a single MOS transistor per capacitor, at the IBM Thomas J. Watson Research Center, while he was working on MOS memory and was trying to create an alternative to SRAM which required six MOS transistors for each bit of data. While examining the characteristics of MOS technology, he found it was capable of building capacitors, and that storing a charge or no charge on the MOS capacitor could represent the 1 and 0 of a bit, while the MOS transistor could control writing the charge to the capacitor. This led to his development of the single-transistor MOS DRAM memory cell. He filed a patent in 1967, and was granted U.S. patent number 3,387,286 in 1968. MOS memory offered higher performance, was cheaper, and consumed less power, than magnetic-core memory. The patent describes the invention: "Each cell is formed, in one embodiment, using a single field-effect transistor and a single capacitor."

MOS DRAM chips were commercialized in 1969 by Advanced Memory Systems, Inc., of Sunnyvale, CA. This 1024 bit chip was sold to Honeywell, Raytheon, Wang Laboratories, and others. The same year, Honeywell asked Intel to make a DRAM using a three-transistor cell that they had developed. This became the Intel 1102 in early 1970. However, the 1102 had many problems, prompting Intel to begin work on their own improved design, in secrecy to avoid conflict with Honeywell. This became the first commercially available DRAM, the Intel 1103, in October 1970, despite initial problems with low yield until the fifth revision of the masks. The 1103 was designed by Joel Karp and laid out by Pat Earhart. The masks were cut by Barbara Maness and Judy Garcia. MOS memory overtook magnetic-core memory as the dominant memory technology in the early 1970s.

The first DRAM with multiplexed row and column address lines was the Mostek MK4096 4 Kbit DRAM designed by Robert Proebsting and introduced in 1973. This addressing scheme uses the same address pins to receive the low half and the high half of the address of the memory cell being referenced, switching between the two halves on alternating bus cycles. This was a radical advance, effectively halving the number of address lines required, which enabled it to fit into packages with fewer pins, a cost advantage that grew with every jump in memory size. The MK4096 proved to be a very robust design for customer applications. At the 16 Kbit density, the cost advantage increased; the 16 Kbit Mostek MK4116 DRAM, introduced in 1976, achieved greater than 75% worldwide DRAM market share. However, as density increased to 64 Kbit in the early 1980s, Mostek and other US manufacturers were overtaken by Japanese DRAM manufacturers, which dominated the US and worldwide markets during the 1980s and 1990s.

Early in 1985, Gordon Moore decided to withdraw Intel from producing DRAM. By 1986, many, but not all, United States chip makers had stopped making DRAMs. Micron Technology and Texas Instruments continued to produce them commercially, and IBM produced them for internal use.

In 1985, when 64K DRAM memory chips were the most common memory chips used in computers, and when more than 60 percent of those chips were produced by Japanese companies, semiconductor makers in the United States accused Japanese companies of export dumping for the purpose of driving makers in the United States out of the commodity memory chip business. Prices for the 64K product plummeted to as low as 35 cents apiece from $3.50 within 18 months, with disastrous financial consequences for some U.S. firms. On 4 December 1985 the US Commerce Department's International Trade Administration ruled in favor of the complaint.

Synchronous dynamic random-access memory (SDRAM) was developed by Samsung. The first commercial SDRAM chip was the Samsung KM48SL2000, which had a capacity of 16 Mbit, and was introduced in 1992. The first commercial DDR SDRAM (double data rate SDRAM) memory chip was Samsung's 64 Mbit DDR SDRAM chip, released in 1998.

Later, in 2001, Japanese DRAM makers accused Korean DRAM manufacturers of dumping.

In 2002, the United States Department of Justice began an investigation which ultimately found several computer manufacturers guilty of DRAM price fixing.


## Principles of operation

DRAM is usually arranged in a rectangular array of charge storage cells consisting of one capacitor and transistor per data bit. The figure to the right shows a simple example with a four-by-four cell matrix. Some DRAM matrices are many thousands of cells in height and width.

The long horizontal lines connecting each row are known as word-lines. Each column of cells is composed of two bit-lines, each connected to every other storage cell in the column (the illustration to the right does not include this important detail). They are generally known as the *+* and *−* bit lines.

A sense amplifier is essentially a pair of cross-connected inverters between the bit-lines. The first inverter is connected with input from the + bit-line and output to the − bit-line. The second inverter's input is from the − bit-line with output to the + bit-line. This results in positive feedback which stabilizes after one bit-line is fully at its highest voltage and the other bit-line is at the lowest possible voltage.

### Operations to read a data bit from a DRAM storage cell

1. The sense amplifiers are disconnected.
2. The bit-lines are precharged to exactly equal voltages that are in between high and low logic levels (e.g., 0.5 V if the two levels are 0 and 1 V). The bit-lines are physically symmetrical to keep the capacitance equal, and therefore at this time their voltages are equal.
3. The precharge circuit is switched off. Because the bit-lines are relatively long, they have enough capacitance to maintain the precharged voltage for a brief time. This is an example of dynamic logic.
4. The desired row's word-line is then driven high to connect a cell's storage capacitor to its bit-line. This causes the transistor to conduct, transferring charge from the storage cell to the connected bit-line (if the stored value is 1) or from the connected bit-line to the storage cell (if the stored value is 0). Since the capacitance of the bit-line is typically much higher than the capacitance of the storage cell, the voltage on the bit-line increases very slightly if the storage cell's capacitor is discharged and decreases very slightly if the storage cell is charged (e.g., 0.54 and 0.45 V in the two cases). As the other bit-line holds 0.50 V there is a small voltage difference between the two twisted bit-lines.
5. The sense amplifiers are now connected to the bit-lines pairs. Positive feedback then occurs from the cross-connected inverters, thereby amplifying the small voltage difference between the odd and even row bit-lines of a particular column until one bit line is fully at the lowest voltage and the other is at the maximum high voltage. Once this has happened, the row is *open* (the desired cell data is available).
6. All storage cells in the open row are sensed simultaneously, and the sense amplifier outputs latched. A column address then selects which latch bit to connect to the external data bus. Reads of different columns in the same row can be performed without a row opening delay because, for the open row, all data has already been sensed and latched.
7. While reading of columns in an open row is occurring, current is flowing back up the bit-lines from the output of the sense amplifiers and recharging the storage cells. This reinforces (i.e. refreshes) the charge in the storage cell by increasing the voltage in the storage capacitor if it was charged to begin with, or by keeping it discharged if it was empty. Note that due to the length of the bit-lines there is a fairly long propagation delay for the charge to be transferred back to the cell's capacitor. This takes significant time past the end of sense amplification, and thus overlaps with one or more column reads.
8. When done with reading all the columns in the current open row, the word-line is switched off to disconnect the storage cell capacitors (the row is closed) from the bit-lines. The sense amplifier is switched off, and the bit-lines are precharged again.

### To write to memory

To store data, a row is opened and a given column's sense amplifier is temporarily forced to the desired high or low-voltage state, thus causing the bit-line to charge or discharge the cell storage capacitor to the desired value. Due to the sense amplifier's positive feedback configuration, it will hold a bit-line at stable voltage even after the forcing voltage is removed. During a write to a particular cell, all the columns in a row are sensed simultaneously just as during reading, so although only a single column's storage-cell capacitor charge is changed, the entire row is refreshed (written back in), as illustrated in the figure to the right.

### Refresh rate

Typically, manufacturers specify that each row must be refreshed every 64 ms or less, as defined by the JEDEC standard.

Some systems refresh every row in a burst of activity involving all rows every 64 ms. Other systems refresh one row at a time staggered throughout the 64 ms interval. For example, a system with 213 = 8,192 rows would require a staggered refresh rate of one row every 7.8 μs which is 64 ms divided by 8,192 rows. A few real-time systems refresh a portion of memory at a time determined by an external timer function that governs the operation of the rest of a system, such as the vertical blanking interval that occurs every 10–20 ms in video equipment.

The row address of the row that will be refreshed next is maintained by external logic or a counter within the DRAM. A system that provides the row address (and the refresh command) does so to have greater control over when to refresh and which row to refresh. This is done to minimize conflicts with memory accesses, since such a system has both knowledge of the memory access patterns and the refresh requirements of the DRAM. When the row address is supplied by a counter within the DRAM, the system relinquishes control over which row is refreshed and only provides the refresh command. Some modern DRAMs are capable of self-refresh; no external logic is required to instruct the DRAM to refresh or to provide a row address.

Under some conditions, most of the data in DRAM can be recovered even if the DRAM has not been refreshed for several minutes.

### Memory timing

Many parameters are required to fully describe the timing of DRAM operation. Here are some examples for two timing grades of asynchronous DRAM, from a data sheet published in 1998:

|   | "50 ns" | "60 ns" | Description |
|---|---|---|---|
| *t*RC | 84 ns | 104 ns | Random read or write cycle time (from one full /RAS cycle to another) |
| *t*RAC | 50 ns | 60 ns | Access time: /RAS low to valid data out |
| *t*RCD | 11 ns | 14 ns | /RAS low to /CAS low time |
| *t*RAS | 50 ns | 60 ns | /RAS pulse width (minimum /RAS low time) |
| *t*RP | 30 ns | 40 ns | /RAS precharge time (minimum /RAS high time) |
| *t*PC | 20 ns | 25 ns | Page-mode read or write cycle time (/CAS to /CAS) |
| *t*AA | 25 ns | 30 ns | Access time: Column address valid to valid data out (includes address setup time before /CAS low) |
| *t*CAC | 13 ns | 15 ns | Access time: /CAS low to valid data out |
| *t*CAS | 8 ns | 10 ns | /CAS low pulse width minimum |

Thus, the generally quoted number is the /RAS low to valid data out time. This is the time to open a row, settle the sense amplifiers, and deliver the selected column data to the output. This is also the minimum /RAS low time, which includes the time for the amplified data to be delivered back to recharge the cells. The time to read additional bits from an open page is much less, defined by the /CAS to /CAS cycle time. The quoted number is the clearest way to compare between the performance of different DRAM memories, as it sets the slower limit regardless of the row length or page size. Bigger arrays forcibly result in larger bit line capacitance and longer propagation delays, which cause this time to increase as the sense amplifier settling time is dependent on both the capacitance as well as the propagation latency. This is countered in modern DRAM chips by instead integrating many more complete DRAM arrays within a single chip, to accommodate more capacity without becoming too slow.

When such a RAM is accessed by clocked logic, the times are generally rounded up to the nearest clock cycle. For example, when accessed by a 100 MHz state machine (i.e. a 10 ns clock), the 50 ns DRAM can perform the first read in five clock cycles, and additional reads within the same page every two clock cycles. This was generally described as "5-2-2-2" timing, as bursts of four reads within a page were common.

When describing synchronous memory, timing is described by clock cycle counts separated by hyphens. These numbers represent *t*CL-*t*RCD-*t*RP-*t*RAS in multiples of the DRAM clock cycle time. Note that this is half of the data transfer rate when double data rate signaling is used. JEDEC standard PC3200 timing is 3-4-4-8 with a 200 MHz clock, while premium-priced high performance PC3200 DDR DRAM DIMM might be operated at 2-2-2-5 timing.

Synchronous DRAM typical timing

PC-3200 (DDR-400)

PC2-6400 (DDR2-800)

PC3-12800 (DDR3-1600)

Description

cycles

time

cycles

time

cycles

time

t

CL

Typical

3

15

ns

5

12.5

ns

9

11.25

ns

/CAS low to valid data out (equivalent to

t

CAC

)

Fast

2

10

ns

4

10

ns

8

10

ns

t

RCD

Typical

4

20

ns

5

12.5

ns

9

11.25

ns

/RAS low to /CAS low time

Fast

2

10

ns

4

10

ns

8

10

ns

t

RP

Typical

4

20

ns

5

12.5

ns

9

11.25

ns

/RAS precharge time (minimum precharge to active time)

Fast

2

10

ns

4

10

ns

8

10

ns

t

RAS

Typical

8

40

ns

16

40

ns

27

33.75

ns

Row active time (minimum active to precharge time)

Fast

5

25

ns

12

30

ns

24

30

ns

Minimum random access time has improved from *t*RAC = 50 ns to *t*RCD + *t*CL = 22.5 ns, and even the premium 20 ns variety is only 2.5 times faster than the asynchronous DRAM. CAS latency has improved even less, from *t*CAC = 13 ns to 10 ns. However, the DDR3 memory does achieve 32 times higher bandwidth; due to internal pipelining and wide data paths, it can output two words every 1.25 ns (1600 Mword/s), while the EDO DRAM can output one word per *t*PC = 20 ns (50 Mword/s).

#### Timing abbreviations

| *t*CL – CAS latency *t*CR – Command rate *t*PTP – precharge to precharge delay *t*RAS – RAS active time *t*RCD – RAS to CAS delay *t*REF – Refresh period *t*RFC – Row refresh cycle time *t*RP – RAS precharge | *t*RRD – RAS to RAS delay *t*RTP – Read to precharge delay *t*RTR – Read to read delay *t*RTW – Read to write delay *t*WR – Write recovery time *t*WTP – Write to precharge delay *t*WTR – Write to read delay *t*WTW – Write to write delay |
|---|---|


## Memory cell design

Each bit of data in a DRAM is stored as a positive or negative electrical charge in a capacitive structure. The structure providing the capacitance, as well as the transistors that control access to it, is collectively referred to as a *DRAM cell*. They are the fundamental building block in DRAM arrays. Multiple DRAM memory cell variants exist, but the most commonly used variant in modern DRAMs is the one-transistor, one-capacitor (1T1C) cell. The transistor is used to admit current into the capacitor during writes, and to discharge the capacitor during reads. The access transistor is designed to maximize drive strength and minimize transistor-transistor leakage (Kenner, p. 34).

The capacitor has two terminals, one of which is connected to its access transistor, and the other to either ground or VCC/2. In modern DRAMs, the latter case is more common, since it allows faster operation. In modern DRAMs, a voltage of +VCC/2 across the capacitor is required to store a logic one; and a voltage of −VCC/2 across the capacitor is required to store a logic zero. The resultant charge is ${\textstyle Q=\pm {V_{CC} \over 2}\cdot C}$ , where *Q* is the charge in coulombs and *C* is the capacitance in farads.

Reading or writing a logic one requires the wordline be driven to a voltage greater than the sum of VCC and the access transistor's threshold voltage (VTH). This voltage is called *VCC pumped* (VCCP). The time required to discharge a capacitor thus depends on what logic value is stored in the capacitor. A capacitor containing logic one begins to discharge when the voltage at the access transistor's gate terminal is above VCCP. If the capacitor contains a logic zero, it begins to discharge when the gate terminal voltage is above VTH.

### Capacitor design

Up until the mid-1980s, the capacitors in DRAM cells were co-planar with the access transistor (they were constructed on the surface of the substrate), thus they were referred to as *planar* capacitors. The drive to increase both density and, to a lesser extent, performance, required denser designs. This was strongly motivated by economics, a major consideration for DRAM devices, especially commodity DRAMs. The minimization of DRAM cell area can produce a denser device and lower the cost per bit of storage. Starting in the mid-1980s, the capacitor was moved above or below the silicon substrate in order to meet these objectives. DRAM cells featuring capacitors above the substrate are referred to as *stacked* or *folded plate* capacitors. Those with capacitors buried beneath the substrate surface are referred to as *trench* capacitors. In the 2000s, manufacturers were sharply divided by the type of capacitor used in their DRAMs and the relative cost and long-term scalability of both designs have been the subject of extensive debate. The majority of DRAMs, from major manufacturers such as Hynix, Micron Technology, Samsung Electronics use the stacked capacitor structure, whereas smaller manufacturers such as Nanya Technology use the trench capacitor structure (Jacob, pp. 355–357).

The capacitor in the stacked capacitor scheme is constructed above the surface of the substrate. The capacitor is constructed from an oxide-nitride-oxide (ONO) dielectric sandwiched in between two layers of polysilicon plates (the top plate is shared by all DRAM cells in an IC), and its shape can be a rectangle, a cylinder, or some other more complex shape. There are two basic variations of the stacked capacitor, based on its location relative to the bitline—capacitor-under-bitline (CUB) and capacitor-over-bitline (COB). In the former, the capacitor is underneath the bitline, which is usually made of metal, and the bitline has a polysilicon contact that extends downwards to connect it to the access transistor's source terminal. In the latter, the capacitor is constructed above the bitline, which is almost always made of polysilicon, but is otherwise identical to the COB variation. The advantage the COB variant possesses is the ease of fabricating the contact between the bitline and the access transistor's source as it is physically close to the substrate surface. However, this requires the active area to be laid out at a 45-degree angle when viewed from above, which makes it difficult to ensure that the capacitor contact does not touch the bitline. CUB cells avoid this, but suffer from difficulties in inserting contacts in between bitlines, since the size of features this close to the surface are at or near the minimum feature size of the process technology (Kenner, pp. 33–42).

The trench capacitor is constructed by etching a deep hole into the silicon substrate. The substrate volume surrounding the hole is then heavily doped to produce a buried n+ plate with low resistance. A layer of oxide-nitride-oxide dielectric is grown or deposited, and finally the hole is filled by depositing doped polysilicon, which forms the top plate of the capacitor. The top of the capacitor is connected to the access transistor's drain terminal via a polysilicon strap (Kenner, pp. 42–44). A trench capacitor's depth-to-width ratio in DRAMs of the mid-2000s can exceed 50:1 (Jacob, p. 357).

Trench capacitors have numerous advantages. Since the capacitor is buried in the bulk of the substrate instead of lying on its surface, the area it occupies can be minimized to what is required to connect it to the access transistor's drain terminal without decreasing the capacitor's size, and thus capacitance (Jacob, pp. 356–357). Alternatively, the capacitance can be increased by etching a deeper hole without any increase to surface area (Kenner, p. 44). Another advantage of the trench capacitor is that its structure is under the layers of metal interconnect, allowing them to be more easily made planar, which enables it to be integrated in a logic-optimized process technology, which have many levels of interconnect above the substrate. The fact that the capacitor is under the logic means that it is constructed before the transistors are. This allows high-temperature processes to fabricate the capacitors, which would otherwise degrade the logic transistors and their performance. This makes trench capacitors suitable for constructing embedded DRAM (eDRAM) (Jacob, p. 357). Disadvantages of trench capacitors are difficulties in reliably constructing the capacitor's structures within deep holes and in connecting the capacitor to the access transistor's drain terminal (Kenner, p. 44).

### Historical cell designs

First-generation DRAM ICs (those with capacities of 1 Kbit), such as the archetypical Intel 1103, used a three-transistor, one-capacitor (3T1C) DRAM cell with separate read and write circuitry. The write wordline drove a write transistor which connected the capacitor to the write bitline just as in the 1T1C cell, but there was a separate read wordline and read transistor which connected an amplifier transistor to the read bitline. By the second generation, the drive to reduce cost by fitting the same amount of bits in a smaller area led to the almost universal adoption of the 1T1C DRAM cell, although a couple of devices with 4 and 16 Kbit capacities continued to use the 3T1C cell for performance reasons (Kenner, p. 6). These performance advantages included, most significantly, the ability to read the state stored by the capacitor without discharging it, avoiding the need to write back what was read out (non-destructive read). A second performance advantage relates to the 3T1C cell's separate transistors for reading and writing; the memory controller can exploit this feature to perform atomic read-modify-writes, where a value is read, modified, and then written back as a single, indivisible operation (Jacob, p. 459).

### Proposed cell designs

The one-transistor, zero-capacitor (1T, or 1T0C) DRAM cell has been a topic of research since the late-1990s. *1T DRAM* is a different way of constructing the basic DRAM memory cell, distinct from the classic one-transistor/one-capacitor (1T/1C) DRAM cell, which is also sometimes referred to as *1T DRAM*, particularly in comparison to the 3T and 4T DRAM which it replaced in the 1970s.

In 1T DRAM cells, the bit of data is still stored in a capacitive region controlled by a transistor, but this capacitance is no longer provided by a separate capacitor. 1T DRAM is a "capacitorless" bit cell design that stores data using the parasitic body capacitance that is inherent to silicon on insulator (SOI) transistors. Considered a nuisance in logic design, this floating body effect can be used for data storage. This gives 1T DRAM cells the greatest density as well as allowing easier integration with high-performance logic circuits since they are constructed with the same SOI process technologies.

Refreshing of cells remains necessary, but unlike with 1T1C DRAM, reads in 1T DRAM are non-destructive; the stored charge causes a detectable shift in the threshold voltage of the transistor. Performance-wise, access times are significantly better than capacitor-based DRAMs, but slightly worse than SRAM. There are several types of 1T DRAMs: the commercialized Z-RAM from Innovative Silicon, the TTRAM from Renesas and the A-RAM from the UGR/CNRS consortium.


## Array structures

DRAM cells are laid out in a regular rectangular, grid-like pattern to facilitate their control and access via wordlines and bitlines. The physical layout of the DRAM cells in an array is typically designed so that two adjacent DRAM cells in a column share a single bitline contact to reduce their area. DRAM cell area is given as *n*F2, where *n* is a number derived from the DRAM cell design, and *F* is the smallest feature size of a given process technology. This scheme permits comparison of DRAM size over different process technology generations, as DRAM cell area scales at linear or near-linear rates with respect to feature size. The typical area for modern DRAM cells varies between 6–8 F2.

The horizontal wire, the wordline, is connected to the gate terminal of every access transistor in its row. The vertical bitline is connected to the source terminal of the transistors in its column. The lengths of the wordlines and bitlines are limited. The wordline length is limited by the desired performance of the array, since propagation time of the signal that must traverse the wordline is determined by the RC time constant. The bitline length is limited by its capacitance (which increases with length), which must be kept within a range for proper sensing (as DRAMs operate by sensing the charge of the capacitor released onto the bitline). Bitline length is also limited by the amount of operating current the DRAM can draw and by how power can be dissipated, since these two characteristics are largely determined by the charging and discharging of the bitline.

### Bitline architecture

Sense amplifiers are required to read the state contained in the DRAM cells. When the access transistor is activated, the electrical charge in the capacitor is shared with the bitline. The bitline's capacitance is much greater than that of the capacitor (approximately ten times). Thus, the change in bitline voltage is minute. Sense amplifiers are required to resolve the voltage differential into the levels specified by the logic signaling system. Modern DRAMs use differential sense amplifiers, and are accompanied by requirements as to how the DRAM arrays are constructed. Differential sense amplifiers work by driving their outputs to opposing extremes based on the relative voltages on pairs of bitlines. The sense amplifiers function effectively and efficiently only if the capacitance and voltages of these bitline pairs are closely matched. Besides ensuring that the lengths of the bitlines and the number of DRAM cells attached to them are equal, two basic architectures to array design have emerged to provide for the requirements of the sense amplifiers: open and folded bitline arrays.

#### Open bitline arrays

The first generation (1 Kbit) DRAM ICs, up until the 64 Kbit generation (and some 256 Kbit generation devices) had open bitline array architectures. In these architectures, the bitlines are divided into multiple segments, and the differential sense amplifiers are placed in between bitline segments. Because the sense amplifiers are placed between bitline segments, to route their outputs outside the array, an additional layer of interconnect placed above those used to construct the wordlines and bitlines is required.

The DRAM cells that are on the edges of the array do not have adjacent segments. Since the differential sense amplifiers require identical capacitance and bitline lengths from both segments, dummy bitline segments are provided. The advantage of the open bitline array is a smaller array area, although this advantage is slightly diminished by the dummy bitline segments. The disadvantage that caused the near disappearance of this architecture is the inherent vulnerability to noise, which affects the effectiveness of the differential sense amplifiers. Since each bitline segment does not have any spatial relationship to the other, it is likely that noise would affect only one of the two bitline segments.

#### Folded bitline arrays

The folded bitline array architecture routes bitlines in pairs throughout the array. The close proximity of the paired bitlines provide superior common-mode noise rejection characteristics over open bitline arrays. The folded bitline array architecture began appearing in DRAM ICs during the mid-1980s, beginning with the 256 Kbit generation. This architecture is favored in modern DRAM ICs for its superior noise immunity.

This architecture is referred to as *folded* because it takes its basis from the open array architecture from the perspective of the circuit schematic. The folded array architecture appears to remove DRAM cells in alternate pairs (because two DRAM cells share a single bitline contact) from a column, then move the DRAM cells from an adjacent column into the voids.

The location where the bitline twists occupies additional area. To minimize area overhead, engineers select the simplest and most area-minimal twisting scheme that is able to reduce noise under the specified limit. As process technology improves to reduce minimum feature sizes, the signal to noise problem worsens, since coupling between adjacent metal wires is inversely proportional to their pitch. The array folding and bitline twisting schemes that are used must increase in complexity in order to maintain sufficient noise reduction. Schemes that have desirable noise immunity characteristics for a minimal impact in area is the topic of current research (Kenner, p. 37).

#### Future array architectures

Advances in process technology could result in open bitline array architectures being favored if it is able to offer better long-term area efficiencies; since folded array architectures require increasingly complex folding schemes to match any advance in process technology. The relationship between process technology, array architecture, and area efficiency is an active area of research.

### Row and column redundancy

The first DRAM integrated circuits did not have any redundancy. An integrated circuit with a defective DRAM cell would be discarded. Beginning with the 64 Kbit generation, DRAM arrays have included spare rows and columns to improve yields. Spare rows and columns provide tolerance of minor fabrication defects which have caused a small number of rows or columns to be inoperable. The defective rows and columns are physically disconnected from the rest of the array by triggering a programmable fuse or by cutting the wire by a laser. The spare rows or columns are substituted in by remapping logic in the row and column decoders (Jacob, pp. 358–361).


## Error detection and correction

Electrical or magnetic interference inside a computer system can cause a single bit of DRAM to spontaneously flip to the opposite state. The majority of one-off ("soft") errors in DRAM chips occur as a result of background radiation, chiefly neutrons from cosmic ray secondaries, which may change the contents of one or more memory cells or interfere with the circuitry used to read/write them.

The problem can be mitigated by using redundant memory bits and additional circuitry that use these bits to detect and correct soft errors. In most cases, the detection and correction are performed by the memory controller; sometimes, the required logic is transparently implemented within DRAM chips or modules, enabling the ECC memory functionality for otherwise ECC-incapable systems. The extra memory bits are used to record parity and to enable missing data to be reconstructed by error-correcting code (ECC). Parity allows the detection of all single-bit errors (actually, any odd number of wrong bits). The most common error-correcting code, a SECDED Hamming code, allows a single-bit error to be corrected and, in the usual configuration, with an extra parity bit, double-bit errors to be detected.

Recent studies give widely varying error rates with over seven orders of magnitude difference, ranging from 10−10−10−17 error/bit·h, roughly one bit error, per hour, per gigabyte of memory to one bit error, per century, per gigabyte of memory. The Schroeder et al. 2009 study reported a 32% chance that a given computer in their study would suffer from at least one correctable error per year, and provided evidence that most such errors are intermittent hard rather than soft errors and that trace amounts of radioactive material that had gotten into the chip packaging were emitting alpha particles and corrupting the data. A 2010 study at the University of Rochester also gave evidence that a substantial fraction of memory errors are intermittent hard errors. Large scale studies on non-ECC main memory in PCs and laptops suggest that undetected memory errors account for a substantial number of system failures: the 2011 study reported a 1-in-1700 chance per 1.5% of memory tested (extrapolating to an approximately 26% chance for total memory) that a computer would have a memory error every eight months.


## Security

### Data remanence

Although dynamic memory is only specified and *guaranteed* to retain its contents when supplied with power and refreshed every short period of time (often 64 ms), the memory cell capacitors often retain their values for significantly longer time, particularly at low temperatures. Under some conditions most of the data in DRAM can be recovered even if it has not been refreshed for several minutes.

This property can be used to circumvent security and recover data stored in the main memory that is assumed to be destroyed at power-down. The computer could be quickly rebooted, and the contents of the main memory read out; or by removing a computer's memory modules, cooling them to prolong data remanence, then transferring them to a different computer to be read out. Such an attack was demonstrated to circumvent popular disk encryption systems, such as the open source TrueCrypt, Microsoft's BitLocker Drive Encryption, and Apple's FileVault. This type of attack against a computer is often called a cold boot attack.

### Memory corruption

Dynamic memory, by definition, requires periodic refresh. Furthermore, reading dynamic memory is a destructive operation, requiring a recharge of the storage cells in the row that has been read. If these processes are imperfect, a read operation can cause soft errors. In particular, there is a risk that some charge can leak between nearby cells, causing the refresh or read of one row to cause a *disturbance error* in an adjacent or even nearby row. The awareness of disturbance errors dates back to the first commercially available DRAM in the early 1970s (the Intel 1103). Despite the mitigation techniques employed by manufacturers, commercial researchers proved in a 2014 analysis that commercially available DDR3 DRAM chips manufactured in 2012 and 2013 are susceptible to disturbance errors. The associated side effect that led to observed bit flips has been dubbed *row hammer*.


## Packaging

### Memory module

Dynamic RAM ICs can be packaged in molded epoxy cases, with an internal lead frame for interconnections between the silicon die and the package leads. The original IBM PC design used ICs, including those for DRAM, packaged in dual in-line packages (DIP), soldered directly to the main board or mounted in sockets. As memory density skyrocketed, the DIP package was no longer practical. For convenience in handling, several dynamic RAM integrated circuits may be mounted on a single memory module, allowing installation of 16-bit, 32-bit or 64-bit wide memory in a single unit, without the requirement for the installer to insert multiple individual integrated circuits. Memory modules may include additional devices for parity checking or error correction. Over the evolution of desktop computers, several standardized types of memory module have been developed. Laptop computers, game consoles, and specialized devices may have their own formats of memory modules not interchangeable with standard desktop parts for packaging or proprietary reasons.

### Embedded

DRAM that is integrated into an integrated circuit designed in a logic-optimized process (such as an application-specific integrated circuit, microprocessor, or an entire system on a chip) is called *embedded DRAM* (eDRAM). Embedded DRAM requires DRAM cell designs that can be fabricated without preventing the fabrication of fast-switching transistors used in high-performance logic, and modification of the basic logic-optimized process technology to accommodate the process steps required to build DRAM cell structures.

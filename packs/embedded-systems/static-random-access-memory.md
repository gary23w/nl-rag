---
title: "Static random-access memory"
source: https://en.wikipedia.org/wiki/Static_random-access_memory
domain: embedded-systems
license: CC-BY-SA-4.0
tags: embedded system, microcontroller, firmware, bare metal, bootloader, mcu
fetched: 2026-07-02
---

# Static random-access memory

**Static random-access memory** (**static RAM** or **SRAM**) is a type of random-access memory (RAM) that uses latching circuitry (flip-flop) to store each bit. SRAM is volatile memory; data is lost when power is removed.

The *static* qualifier differentiates SRAM from *dynamic* random-access memory (DRAM):

- SRAM will hold its data permanently in the presence of power, while data in DRAM decays in seconds and thus must be periodically refreshed.
- SRAM is faster than DRAM but it is more expensive in terms of silicon area and cost.
- Typically, SRAM is used for the cache and internal registers of a CPU while DRAM is used for a computer's main memory.

## History

Semiconductor bipolar SRAM was invented in 1963 by Robert Norman at Fairchild Semiconductor. Metal–oxide–semiconductor SRAM (MOS-SRAM) was invented in 1964 by John Schmidt at Fairchild Semiconductor. The first device was a 64-bit MOS p-channel SRAM.

SRAM was the main driver behind any new CMOS-based technology fabrication process since the 1960s, when CMOS was invented.

In 1964, Arnold Farber and Eugene Schlig, working for IBM, created a hard-wired memory cell, using a transistor gate and tunnel diode latch. They replaced the latch with two transistors and two resistors, a configuration that became known as the Farber-Schlig cell. That year they submitted an invention disclosure, but it was initially rejected. In 1965, Benjamin Agusta and his team at IBM created a 16-bit silicon memory chip based on the Farber-Schlig cell, with 84 transistors, 64 resistors, and 4 diodes.

In April 1969, Intel Inc. introduced its first product, Intel 3101, a SRAM memory chip intended to replace bulky magnetic-core memory modules; Its capacity was 64 bits and was based on bipolar junction transistors. It was designed by using rubylith.

## Characteristics

Though it can be characterized as volatile memory, SRAM exhibits data remanence.

SRAM offers a simple data access model and does not require a refresh circuit. Performance and reliability are good and power consumption is low when idle. Since SRAM requires more transistors per bit to implement, it is less dense and more expensive than DRAM and also has a higher power consumption during read or write access. The power consumption of SRAM varies widely depending on how frequently it is accessed.

## Applications

RAM cells on the

die

of a STM32F103VGT6

microcontroller

manufactured by

STMicroelectronics

using a 180-

nanometre

process

Imaged by

scanning electron microscope

; cell

topology

is clearly visible

Imaged by

optical microscope

### Embedded use

Many categories of industrial and scientific subsystems, automotive electronics, and similar embedded systems, contain SRAM which, in this context, may be referred to as *embedded SRAM* (ESRAM). Some amount is also embedded in practically all modern appliances, toys, etc. that implement an electronic user interface.

SRAM in its dual-ported form is sometimes used for real-time digital signal processing circuits.

### In computers

SRAM is used in personal computers, workstations and peripheral equipment: CPU register files, internal CPU caches and GPU caches, hard disk buffers, etc. LCD screens also may employ SRAM to hold the image displayed. SRAM was used for the main memory of many early personal computers such as the ZX80, TRS-80 Model 100, and VIC-20.

Some early memory cards in the late 1980s to early 1990s used SRAM as a storage medium, which required a lithium battery to retain the contents of the SRAM.

### Integrated on chip

SRAM may be integrated on chip for:

- the RAM in microcontrollers (usually from around 32 bytes to a megabyte),
- the on-chip caches in most modern processors, like CPUs and GPUs, from a few kilobytes and up to more than a hundred megabytes,
- the registers and parts of the state-machines used in CPUs, GPUs, chipsets and peripherals (see register file),
- scratchpad memory,
- application-specific integrated circuits (ASICs) (usually in the order of kilobytes),
- and in field-programmable gate arrays (FPGAs) and complex programmable logic devices (CPLDs).

### Hobbyists

Hobbyists, specifically home-built processor enthusiasts, often prefer SRAM due to the ease of interfacing. It is much easier to work with than DRAM as there are no refresh cycles and the address and data buses are often directly accessible. In addition to buses and power connections, SRAM usually requires only three controls: *chip enable* (CE), *write enable* (WE) and *output enable* (OE). In synchronous SRAM, *clock* line (CLK) is also included.

## Types of SRAM

### Non-volatile SRAM

Non-volatile SRAM (nvSRAM) has standard SRAM functionality, but retains data when power is lost. nvSRAMs are used in networking, aerospace, and medical, among other applications, where the preservation of data is critical and where batteries are impractical.

### Pseudostatic RAM

Pseudostatic RAM (PSRAM) is DRAM combined with a self-refresh circuit. It appears externally as slower SRAM, albeit with a density and cost advantage over true SRAM, and without the access complexity of DRAM.

### By transistor type

- Bipolar junction transistor (used in TTL and ECL) – very fast but with high power consumption
- MOSFET (used in CMOS) – low power

### By numeral system

- Binary
- Ternary

### By function

- Asynchronous – independent of clock frequency, data in and data out are controlled by address transition. Examples include the ubiquitous 28-pin 8K × 8 and 32K × 8 chips (often but not always named something along the lines of 6264 and 62C256, respectively), as well as similar products up to 16 Mbit per chip.
- Synchronous – all timings are initiated by the clock edges. Address, data in and other control signals are associated with the clock signals.

In the 1990s, asynchronous SRAM was employed for fast access time. Asynchronous SRAM was used as main memory for small cache-less embedded processors used in everything from industrial electronics and measurement systems to hard disks and networking equipment. Synchronous SRAM (e.g., DDR SRAM) is preferred similarly to how synchronous DRAM – DDR SDRAM memory is now preferred over asynchronous DRAM. The pipeline architecture employed by synchronous memory allows higher throughput. Furthermore, as DRAM is much cheaper than SRAM, SRAM is often replaced by DRAM, especially in cases where a large memory capacity is required. SRAM memory is, however, much faster for random access, as opposed to block or burst access. Therefore, SRAM memory is mainly used for CPU cache, small on-chip memory, FIFOs or other small buffers.

### By feature

- Zero bus turnaround (ZBT) – the turnaround is the number of clock cycles it takes to change access to SRAM from *write* to *read* and vice versa. The turnaround for ZBT SRAMs or the latency between read and write cycles is zero.
- syncBurst (syncBurst SRAM or synchronous-burst SRAM) – features synchronous burst write access to SRAM to increase write throughput to SRAM.
- DDR SRAM – synchronous, single read/write port, double data rate I/O.
- Quad Data Rate SRAM – synchronous, separate read and write ports, quadruple data rate I/O.

### By stacks

- Single-stack SRAM
- 2.5D SRAM – as of 2025, 3D SRAM technology is still expensive, so SRAM with 2.5D integrated circuit technology may be used.
- 3D SRAM – used on various performance-oriented models of AMD processors.

## Design

A typical SRAM cell is made up of six MOSFETs, and is often called a **6T SRAM cell**. Each bit in the cell is stored on four transistors (M1, M2, M3, M4) that form two cross-coupled inverters. This storage cell has two stable states, which are used to denote 0 and 1. Two additional *access* transistors serve to control the access to a storage cell during read and write operations. 6T SRAM is the most common kind of SRAM. In addition to 6T SRAM, other kinds of SRAM use 4, 5, 7, 8, 9, 10 (4T, 5T, 7T 8T, 9T, 10T SRAM), or more transistors per bit.

Additional transistors are sometimes used to implement more than one (read and/or write) port, which may be useful in certain types of video memory and register files implemented with multi-ported SRAM circuitry.

Generally, the fewer transistors needed per cell, the smaller each cell can be. Since the cost of processing a silicon wafer is relatively fixed, using smaller cells and so packing more bits on one wafer reduces the cost per bit of memory.

Four-transistor SRAM is common in stand-alone SRAM devices (as opposed to SRAM used for CPU caches), implemented in special processes with an extra layer of polysilicon, allowing for very high-resistance pull-up resistors. The principal drawback of using 4T SRAM is increased static power due to the constant current flow through one of the pull-down transistors (M1 or M2).

Memory cells that use fewer than four transistors are possible; however, such 3T or 1T cells are DRAM, not SRAM (even the so-called 1T-SRAM).

Access to the cell is enabled by the word line (WL in figure) which controls the two *access* transistors M5 and M6 in 6T SRAM figure (or M3 and M4 in 4T SRAM figure) which, in turn, control whether the cell should be connected to the bit lines: BL and BL. They are used to transfer data for both read and write operations.

During read accesses, the bit lines are actively driven high and low by the inverters in the SRAM cell. This improves SRAM bandwidth compared to DRAMs – in a DRAM, the bit line is connected to storage capacitors, and charge sharing causes the bit line to swing upwards or downwards. Although it is not strictly necessary to have two bit lines, both the signal and its inverse are typically provided in order to improve noise margins and speed. The symmetric structure of SRAMs also allows for differential signaling, which makes small voltage swings more easily detectable.

Another difference with DRAM that contributes to making SRAM faster is that commercial chips accept all address bits at a time. By comparison, commodity DRAMs have the address multiplexed in two halves, i.e., higher bits followed by lower bits, over the same package pins in order to keep their size and cost down. The size of an SRAM with m address lines and n data lines is 2*m* words, or 2*m* × *n* bits. The most common word size is 8 bits, meaning that a single byte can be read or written to each of 2*m* different words within the SRAM chip. Several common SRAM chips have 11 address lines (thus a capacity of 211 = 2,048 = 2 k words) and an 8-bit word, so they are referred to as *2k × 8 SRAM*.

The dimensions of an SRAM cell on an IC are determined by the minimum feature size of the process used to make the IC.

## SRAM operation

An SRAM cell has three states:

- **Standby:** The circuit is idle.
- **Reading:** The data has been requested.
- **Writing:** Updating the contents.

SRAM operating in read and write modes should have *readability* and *write stability*, respectively. The three different states work as follows:

### Standby

If the word line is not asserted, the *access* transistors M5 and M6 disconnect the cell from the bit lines. The two cross-coupled inverters formed by M1 – M4 will continue to reinforce each other as long as power is available.

### Reading

In theory, reading only requires activating a single access transistor and bit line, e.g. M6 on BL. However, in larger memories, bit lines are relatively long with many connections and thus have large capacitance. To speed up reading, a more complex process is used in practice. The read cycle is started by precharging both bit lines BL and BL, to high (logic 1) voltage. Then asserting the word line WL enables both the access transistors M5 and M6, which causes an initial slight drop on one bit line voltage creating a voltage difference between BL and BL. A differential sense amplifier will sense which line has the higher voltage and thus determine whether there was 1 or 0 stored. Because motion of the bit lines is slowed by capacitance, the higher the sensitivity of the sense amplifier, the faster the read operation.

### Writing

The write cycle begins by applying the value to be written to the bit lines. To write a 0, a 0 is applied to the bit lines, such as setting BL to 1 and BL to 0. This is similar to applying a reset pulse to an SR-latch, which causes the flip flop to change state. A **1** is written by inverting the values of the bit lines. WL is then asserted and the value that is to be stored is latched in. This works because the bit line input drivers are designed to be much stronger than the relatively weak transistors in the cell itself so they can easily override the previous state of the cross-coupled inverters. In practice, access NMOS transistors M5 and M6 have to be stronger than either bottom NMOS (M1, M3) or top PMOS (M2, M4) transistors. This is easily obtained as PMOS transistors are much weaker than NMOS when same sized. Consequently, when one transistor pair (e.g., M3 and M4) is only slightly overridden by the write process, the opposite transistor pair (M1 and M2) gate voltage is also changed. This means that the M1 and M2 transistors can be more easily overridden, and so on. Thus, cross-coupled inverters magnify the writing process.

### Bus behavior

RAM with an access time of 70 ns will output valid data within 70 ns from the time that the address lines are valid. Some SRAM cells have a *page mode*, where words of a page (256, 512, or 1024 words) can be read sequentially with a significantly shorter access time (typically approximately 30 ns). The page is selected by setting the upper address lines and then words are sequentially read by stepping through the lower address lines.

## Production challenges

Over 30 years (from 1987 to 2017), with a steadily decreasing transistor size (node size), the footprint-shrinking of the SRAM cell topology itself slowed down, making it harder to pack the cells more densely. One of the reasons is that scaling down transistor size leads to SRAM reliability issues. Careful cells designs are necessary to achieve SRAM cells that do not suffer from stability problems especially when they are being read. With the introduction of the FinFET transistor implementation of SRAM cells, they started to suffer from increasing inefficiencies in cell sizes.

Besides issues with size a significant challenge of modern SRAM cells is a static current leakage. The current, that flows from positive supply (Vdd), through the cell, and to the ground, increases exponentially when the cell's temperature rises. The cell power drain occurs in both active and idle states, thus wasting useful energy without any useful work done. Even though in the last 20 years the issue was partially addressed by the Data Retention Voltage technique (DRV) with reduction rates ranging from 5 to 10, the decrease in node size caused reduction rates to fall to about 2.

With these two issues it became more challenging to develop energy-efficient and dense SRAM memories, prompting semiconductor industry to look for alternatives such as STT-MRAM and F-RAM.

### Research

In 2019 a French institute reported on a research of an IoT-purposed 28nm fabricated IC. It was based on fully depleted silicon on insulator-transistors (FD-SOI), had two-ported SRAM memory rail for synchronous/asynchronous accesses, and selective virtual ground (SVGND). The study claimed reaching an ultra-low SVGND current in a *sleep* and read modes by finely tuning its voltage.

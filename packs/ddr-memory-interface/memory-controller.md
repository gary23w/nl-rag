---
title: "Memory controller"
source: https://en.wikipedia.org/wiki/Memory_controller
domain: ddr-memory-interface
license: CC-BY-SA-4.0
tags: ddr memory interface, double data rate, dram memory controller, ddr5 sdram
fetched: 2026-07-02
---

# Memory controller

A **memory controller**, also known as **memory chip controller** (**MCC**) or a **memory controller unit** (**MCU**), is a digital circuit that manages the flow of data going to and from a computer's main memory. When a memory controller is integrated into another chip, such as an integral part of a microprocessor, it is usually called an **integrated memory controller** (**IMC**).

Memory controllers contain the logic necessary to read and write to dynamic random-access memory (DRAM), and to provide the critical memory refresh and other functions. Reading and writing to DRAM is performed by selecting the row and column data addresses of the DRAM as the inputs to the multiplexer circuit, where the demultiplexer on the DRAM uses the converted inputs to select the correct memory location and return the data, which is then passed back through a multiplexer to consolidate the data in order to reduce the required bus width for the operation. Memory controllers' bus widths range from 8-bit in earlier systems, to 512-bit in more complicated systems, where they are typically implemented as four 64-bit simultaneous memory controllers operating in parallel, though some operate with two 64-bit memory controllers being used to access a 128-bit memory device.

Some memory controllers, such as the one integrated into PowerQUICC II processors, include error detection and correction hardware. Many modern processors are also integrated memory management unit (MMU), which in many operating systems implements virtual addressing. On early x86-32 processors, the MMU is integrated in the CPU, but the memory controller is usually part of northbridge.

## History

Older Intel and PowerPC-based computers have memory controller chips that are separate from the main processor. Often these are integrated into the northbridge of the computer, also sometimes called a memory controller hub.

Most modern desktop or workstation microprocessors use an **integrated memory controller** (**IMC**), including microprocessors from Intel, AMD, and those built around the ARM architecture. Prior to K8 (circa 2003), AMD microprocessors had a memory controller implemented on their motherboard's northbridge. In K8 and later, AMD employed an integrated memory controller. Likewise, until Nehalem (circa 2008), Intel microprocessors used memory controllers implemented on the motherboard's northbridge. Nehalem and later switched to an integrated memory controller. Other examples of microprocessor architectures that use *integrated memory controllers* include NVIDIA's Fermi, IBM's POWER5, and Sun Microsystems's UltraSPARC T1.

While an integrated memory controller has the potential to increase the system's performance, such as by reducing memory latency, it locks the microprocessor to a specific type (or types) of memory, forcing a redesign in order to support newer memory technologies. When DDR2 SDRAM was introduced, AMD released new Athlon 64 CPUs. These new models, with a DDR2 controller, use a different physical socket (known as Socket 754), so that they will only fit in motherboards designed for the new type of RAM. When the memory controller is not on-die, the same CPU may be installed on a new motherboard, with an updated northbridge to use newer memory.

Some microprocessors in the 1990s, such as the DEC Alpha 21066 and HP PA-7300LC, had integrated memory controllers; however, rather than for performance gains, this was implemented to reduce the cost of systems by eliminating the need for an external memory controller.

Some CPUs are designed to have their memory controllers as dedicated external components that are not part of the chipset. An example is IBM POWER8, which uses external Centaur chips that are mounted onto DIMM modules and act as memory buffers, L4 cache chips, and as the actual memory controllers. The first version of the Centaur chip used DDR3 memory but an updated version was later released which can use DDR4.

## Security

A few experimental memory controllers contain a second level of address translation, in addition to the first level of address translation performed by the CPU's memory management unit to improve cache and bus performance.

Memory controllers integrated into certain Intel Core processors provide **memory scrambling** as a feature that turns user data written to the main memory into pseudo-random patterns. Memory scrambling has the potential to prevent forensic and reverse-engineering analysis based on DRAM data remanence by effectively rendering various types of cold boot attacks ineffective. In current practice, this has not been achieved; memory scrambling has only been designed to address DRAM-related electrical problems. The late 2010s memory scrambling standards do address security issues and are not cryptographically secure or open to public revision or analysis.

ASUS and Intel have their separate memory scrambling standards. ASUS motherboards have allowed the user to choose which memory scrambling standard to use (ASUS or Intel) or whether to turn the feature off entirely.

## Variants

### Single data rate memory

Single data rate (SDR) memory controllers drive SDR SDRAM, where data is transferred once per clock. They are far simpler than double data rate memory controllers, but have been phased out due to their significantly reduced transfer speeds compared to DDR memory.

### Double data rate memory

Double data rate (DDR) memory controllers are used to drive DDR SDRAM, where data is transferred on both rising and falling edges of the system's memory clock. DDR memory controllers are significantly more complicated when compared to single data rate controllers, but they allow for twice the data to be transferred without increasing the memory's clock rate or bus width.

### Multichannel memory

Multichannel memory controllers are memory controllers where the DRAM devices are separated onto multiple buses to allow the memory controller(s) to access them in parallel. This increases the theoretical amount of bandwidth of the bus by a factor of the number of channels. While a channel for every DRAM would be the ideal solution, adding more channels increases complexity and cost.

### Fully buffered memory

Fully buffered memory systems place a memory buffer device on every memory module (called an FB-DIMM when fully buffered RAM is used), which unlike traditional memory controller devices, uses a serial data link to the memory controller instead of the parallel link used in previous RAM designs. This decreases the number of wires necessary to place the memory devices on a motherboard (allowing for a smaller number of layers to be used, meaning more memory devices can be placed on a single board), at the expense of increasing latency (the time necessary to access a memory location). This increase is due to the time required to convert the parallel information read from the DRAM cell to the serial format used by the FB-DIMM controller, and back to a parallel form in the memory controller on the motherboard.

### Error correction code

Error correction code (ECC) memory controllers drive ECC memory. ECC corrects common errors encountered by RAM and significantly reduces data loss and increases stability. It also slightly increases the RAM's bus width (typically from 64 to 72 bytes) to consolidate for this extra code. It is rarely needed in personal computing, but is commonly found in servers and workstations where increased stability and data integrity are important.

### Flash memory controller

Many flash memory devices, such as USB flash drives and solid-state drives, include a flash memory controller. Flash memory is inherently slower to access than RAM and often becomes unusable after a few million write cycles, which generally makes it unsuitable for RAM applications.

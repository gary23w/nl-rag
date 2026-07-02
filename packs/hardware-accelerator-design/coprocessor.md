---
title: "Coprocessor"
source: https://en.wikipedia.org/wiki/Coprocessor
domain: hardware-accelerator-design
license: CC-BY-SA-4.0
tags: hardware accelerator design, coprocessor architecture, fpga acceleration, digital signal processor
fetched: 2026-07-02
---

# Coprocessor

A **coprocessor** is a computer processor used to supplement the functions of the primary processor (the CPU). Operations performed by the coprocessor may be floating-point arithmetic, graphics, signal processing, string processing, cryptography or I/O interfacing with peripheral devices. By offloading processor-intensive tasks from the main processor, coprocessors can accelerate system performance. Coprocessors allow a line of computers to be customized, so that customers who do not need the extra performance do not need to pay for it.

## Functionality

Coprocessors vary in their degree of autonomy. Some (such as FPUs) rely on direct control via coprocessor instructions, embedded in the CPU's instruction stream. Others are independent processors in their own right, capable of working asynchronously; they are still not optimized for general-purpose code, or they are incapable of it due to a limited instruction set focused on accelerating specific tasks. It is common for these to be driven by direct memory access (DMA), with the host processor (a CPU) building a command list. The PlayStation 2's Emotion Engine contained an unusual DSP-like SIMD vector unit capable of both modes of operation.

## History

To make the best use of mainframe computer processor time, input/output tasks were delegated to separate systems called Channel I/O. The mainframe would not require any I/O processing at all, instead, it would set parameters for an input or output operation and then signal the channel processor to carry out the whole of the operation. By dedicating relatively simple sub-processors to handle time-consuming I/O formatting and processing, overall system performance was improved.

Coprocessors for floating-point arithmetic first appeared in desktop computers in the 1970s and became common throughout the 1980s and into the early 1990s. Early 8-bit and 16-bit processors used software to carry out floating-point arithmetic operations. Where a coprocessor was supported, floating-point calculations could be carried out many times faster. Math coprocessors were popular purchases for users of computer-aided design (CAD) software and scientific and engineering calculations. Some floating-point units, such as the AMD 9511, Intel 8231/8232 and Weitek FPUs were treated as peripheral devices, while others such as the Intel 8087, Motorola 68881 and National 32081 were more closely integrated with the CPU.

Another form of coprocessor was a video display coprocessor, as used in the Atari 8-bit computers, TI-99/4A, and MSX home computers, which were called "Video Display Controllers". The Amiga custom chipset includes such a unit known as the Copper, as well as a blitter for accelerating bitmap manipulation in memory.

As microprocessors developed, the cost of integrating the floating-point arithmetic functions into the processor declined. High processor speeds also made a closely integrated coprocessor difficult to implement. Separately packaged mathematics coprocessors are now uncommon in desktop computers. The demand for a dedicated graphics coprocessor has grown, however, particularly due to the increasing demand for realistic 3D graphics in computer games.

## Intel

The original IBM PC included a socket for the Intel 8087 floating-point coprocessor (aka FPU) which was a popular option for people using the PC for computer-aided design or mathematics-intensive calculations. In that architecture, the coprocessor speeds up floating-point arithmetic on the order of fiftyfold. Users that only used the PC for word processing, for example, saved the high cost of the coprocessor, which would not have accelerated performance of text manipulation operations.

The 8087 was tightly integrated with the 8086/8088 and responded to floating-point machine code operation codes inserted in the 8088 instruction stream. An 8088 processor without an 8087 could not interpret these instructions, requiring separate versions of programs for FPU and non-FPU systems, or at least a test at run time to detect the FPU and select appropriate mathematical library functions.

Another coprocessor for the 8086/8088 central processor was the 8089 input/output coprocessor. It used the same programming technique as 8087 for input/output operations, such as transfer of data from memory to a peripheral device, and so reducing the load on the CPU. But IBM did not use it in IBM PC design and Intel stopped development of this type of coprocessor.

The Intel 80386 microprocessor used an optional "math" coprocessor (the 80387) to perform floating-point operations directly in hardware. The Intel 80486DX processor included floating-point hardware on the chip. Intel released a cost-reduced processor, the 80486SX, that had no floating-point hardware, and also sold an 80487SX coprocessor that essentially disabled the main processor when installed, since the 80487SX was a complete 80486DX with a different set of pin connections.

Intel processors later than the 80486 integrated floating-point hardware on the main processor chip; the advances in integration eliminated the cost advantage of selling the floating-point processor as an optional element. It would be very difficult to adapt circuit-board techniques adequate at 75 MHz processor speed to meet the time-delay, power consumption, and radio-frequency interference standards required at gigahertz-range clock speeds. These on-chip floating-point processors are still referred to as coprocessors because they operate in parallel with the main CPU.

During the era of 8- and 16-bit desktop computers another common source of floating-point coprocessors was Weitek. These coprocessors had a different instruction set from the Intel coprocessors, and used a different socket, which not all motherboards supported. The Weitek processors did not provide transcendental mathematics functions (for example, trigonometric functions) like the Intel x87 family, and required specific software libraries to support their functions.

## Motorola

The Motorola 68000 family had the 68881/68882 coprocessors which provided similar floating-point speed acceleration as for the Intel processors. Computers using the 68000 family but not equipped with the hardware floating-point processor could trap and emulate the floating-point instructions in software, which, although slower, allowed one binary version of the program to be distributed for both cases. The 68451 memory-management coprocessor was designed to work with the 68020 processor.

## Modern coprocessors

As of 2001, dedicated Graphics Processing Units (GPUs) in the form of graphics cards are commonplace. Certain models of sound cards have been fitted with dedicated processors providing digital multichannel mixing and real-time DSP effects as early as 1990 to 1994 (the Gravis Ultrasound and Sound Blaster AWE32 being typical examples), while the Sound Blaster Audigy and the Sound Blaster X-Fi are more recent examples.

In 2006, AGEIA announced an add-in card for computers that it called the PhysX PPU. PhysX was designed to perform complex physics computations so that the CPU and GPU do not have to perform these time-consuming calculations. It was designed for video games, although other mathematical uses could theoretically be developed for it. In 2008, Nvidia purchased the company and phased out the PhysX card line; the functionality was added through software allowing their GPUs to render PhysX on cores normally used for graphics processing, using their Nvidia PhysX engine software.

In 2006, BigFoot Systems unveiled a PCI add-in card they christened the KillerNIC which ran its own special Linux kernel on a FreeScale PowerQUICC running at 400 MHz, calling the FreeScale chip a Network Processing Unit or NPU.

The SpursEngine is a media-oriented add-in card with a coprocessor based on the Cell microarchitecture. The SPUs are themselves vector coprocessors.

In 2008, Khronos Group released the OpenCL with the aim to support general-purpose CPUs, ATI/AMD and Nvidia GPUs (and other accelerators) with a single common language for compute kernels.

In 2010s, some mobile computation devices had implemented the sensor hub as a coprocessor. Examples of coprocessors used for handling sensor integration in mobile devices include the Apple M7 and M8 motion coprocessors, the Qualcomm Snapdragon Sensor Core and Qualcomm Hexagon, and the Holographic Processing Unit for the Microsoft HoloLens.

In 2012, Intel announced the Intel Xeon Phi coprocessor.

As of 2016, various companies are developing coprocessors aimed at accelerating artificial neural networks for vision and other cognitive tasks (e.g. vision processing units, TrueNorth, and Zeroth), and as of 2018, such AI chips are in smartphones such as from Apple, and several Android phone vendors.

## Other coprocessors

- The MIPS architecture supports up to four coprocessor units, used for memory management, floating-point arithmetic, and two undefined coprocessors for other tasks such as graphics accelerators.
- Using FPGA (field-programmable gate arrays), custom coprocessors can be created for acceleration of particular processing tasks such as digital signal processing (e.g. Zynq, combines ARM cores with FPGA on a single die).
- TLS/SSL accelerators, used on servers; such accelerators used to be cards, but in modern times are instructions for crypto in mainstream CPUs.
- Some multi-core chips can be programmed so that one of their processors is the primary processor, and the other processors are supporting coprocessors.
- China's Matrix 2000 128 core PCI-e coprocessor is a proprietary accelerator that requires a CPU to run it, and has been employed in an upgrade of the 17,792 node Tianhe-2 supercomputer (2 Intel Knights Bridge+ 2 Matrix 2000 each), now dubbed 2A, roughly doubling its speed at 95 petaflops, exceeding the world's fastest supercomputer.
- A range of coprocessors were available for various models from Acorn Computers, notably the BBC Micro and BBC Master series. Rather than special-purpose graphics or arithmetic devices, these were general-purpose CPUs (principally the 6502, Zilog Z80, National Semiconductor 32016, and ARM 1) described as second processors, typically interfaced to the host system using a message passing architecture known as the Tube, with Acorn's own products providing such processors in a BBC Micro expansion unit with accompanying memory and interfacing circuitry. Software could be executed independently on the second processor, and applications could be written to offload work from the host system, leaving it to perform input/output tasks, resulting in acceleration. Since a range of CPUs were available in a variety of products, a BBC Micro fitted with such a coprocessor was able to run operating systems for other processor architectures, such as CP/M, DOS and Unix, along with accompanying software.

## Trends

Over time CPUs have tended to grow to absorb the functionality of the most popular coprocessors. FPUs are now considered an integral part of a processors' main pipeline; SIMD units gave multimedia its acceleration, taking over the role of various DSP accelerator cards; and even GPUs have become integrated on CPU dies. Nonetheless, specialized units remain popular away from desktop machines, and for additional power, and allow continued evolution independently of the main processor product lines.

---
title: "32-bit computing"
source: https://en.wikipedia.org/wiki/32-bit
domain: h8-family
license: CC-BY-SA-4.0
tags: h8 family
fetched: 2026-07-03
---

# 32-bit computing

(Redirected from

32-bit

)

**32-bit computing** refers to computer architectures with a processor, memory, and other major components that operate on 32-bit units of data. Compared to smaller bit widths, 32-bit computers can perform large calculations more efficiently and process more data per clock cycle. From the 1980s to about 2006, typical 32-bit personal computers had a 32-bit address bus, permitting up to 4 GiB of RAM to be accessed.

32-bit designs have been used since the earliest days of electronic computing, in experimental systems and then in large mainframe and minicomputer systems. The first hybrid 16/32-bit microprocessor, the Motorola 68000, was introduced in the late 1970s and used in systems such as the original Macintosh. Fully 32-bit microprocessors such as the HP FOCUS, Motorola 68020 and Intel 80386 were launched in the early to mid 1980s and became dominant by the early 1990s. This generation of processors enabled the first mass-adoption of the World Wide Web. While 32-bit architectures are still widely used in specific applications, since the mid-2000s PCs, smartphones, and servers have moved on to 64 bits using architectures such as x86-64, with installed memory in entry-level computers often exceeding the 32-bit address limit of 4 GiB.

## Range for storing integers

A 32-bit register can store 232 different values. The range of integer values that can be stored in 32 bits depends on the representation used. With the two most common representations, the range is 0 through 4,294,967,295 (232 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−231) through 2,147,483,647 (231 − 1) for representation as two's complement.

This means a processor with 32-bit logical or virtual addresses can directly access at most 4 GiB of byte-addressable address space. A processor with 32-bit physical addresses can directly access at most 4 GiB of byte-addressable main memory; 32-bit processors don't necessarily always use 32-bit physical addresses, and implementations using more or fewer exist.

## Technical history

In 1948 the Manchester Baby, the first stored-program electronic computer, used a 32-bit architecture although it was only a proof of concept and had little practical capacity. It held only 32 32-bit words of RAM on a Williams tube, and had no addition operation, only subtraction.

Memory, other digital circuits, and wiring was expensive during the first decades of 32-bit architectures (the 1960s to the 1980s). Older 32-bit processor families often had many compromises and limitations to cut costs. This could include a 16-bit ALU, or buses narrower than 32 bits, which limited memory size or reduced the speed of operations.

These early processors are still *32-bit*, having 32-bit registers and instructions to manipulate 32-bit quantities. For example, the IBM System/360 Model 30 had an 8-bit ALU, 8-bit internal data paths, and an 8-bit path to memory, and the original Motorola 68000 had a 16-bit data ALU and a 16-bit external data bus, but had 32-bit registers and a 32-bit oriented instruction set. The 68000 design was sometimes referred to as *16/32-bit*.

However, the opposite is often true for newer 32-bit designs. For example, the Pentium Pro processor is a 32-bit machine, with 32-bit registers and instructions that manipulate 32-bit quantities, but has an 36 bit wide external address bus, giving a larger address space than 4 GB, and a 64 bit wide external data bus, allowing more efficient prefetch of instructions and data. Likewise, the PowerPC 604 is a 32-bit machine with a 64-bit external data bus.

## Architectures

Prominent 32-bit instruction set architectures used in general-purpose computing include the IBM System/360, IBM System/370 (which had 24-bit addressing), System/370-XA, ESA/370, and ESA/390 (which had 31-bit addressing), the DEC VAX, the NS320xx, the Motorola 68000 family (the first two models of which had 24-bit addressing), the Intel IA-32 32-bit version of the x86 architecture, and the 32-bit versions of the ARM, SPARC, MIPS, PowerPC and PA-RISC architectures. 32-bit instruction set architectures used for embedded computing include the 68000 family and ColdFire, x86, ARM, MIPS, PowerPC, and Infineon TriCore architectures.

## Applications

On the x86 architecture, 32-bit applications normally use the 32-bit linear address space possible with the 80386 and later chips. The term came about because MS-DOS, Windows and OS/2 were originally written for the 8088/8086 or 80286, 16-bit microprocessors with a segmented address space where programs had to switch between segments to reach more than 64 kilobytes of memory, causing performance to suffer. Programming with segments is complicated; requiring special keywords or *memory models* in assembly and high level languages.

The 80386 and successors support the 80286's 16-bit segments reuse the technique for 32-bit address offsets. If the base address of all 32-bit segments is set to 0, and segment registers are not used explicitly, the segmentation can be forgotten and the processor appears as having a simple linear 32-bit address space. Operating systems like Windows or OS/2 provide the possibility to run 16-bit (segmented) programs as well as 32-bit programs. The former possibility exists for backward compatibility and the latter is usually meant to be used for new software development.

## Images

32-bit digital images usually refers to RGBA color space, with every pixel using eight bits each for red, green, blue and transparency. Other image formats such as RGBE also use 32 bits per pixel.

In digital images, 32-bit sometimes refers to high-dynamic-range imaging (HDR) formats that use 32 bits per channel, a total of 96 bits per pixel. 32-bit-per-channel images are used to represent values more precisely than sRGB color space allows. This precision can be used to retain more detail when editing the image.

## File formats

A 32-bit file format is a binary file format for which each elementary information is defined on 32 bits (or 4 bytes). An example of such a format is the Enhanced Metafile Format.

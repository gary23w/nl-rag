---
title: "Endianness"
source: https://en.wikipedia.org/wiki/Endianness
domain: arm-riscv
license: CC-BY-SA-4.0
tags: arm architecture, aarch64, risc-v, riscv, cortex-m, instruction set
fetched: 2026-07-02
---

# Endianness

In computing, **endianness** is the order in which bytes within a *word* data type are transmitted over a data communication medium or addressed in computer memory, counting only byte significance compared to earliness. Endianness is primarily expressed as **big-endian** (**BE**) or **little-endian** (**LE**).

Computers store information in various-sized groups of binary bits. Each group is assigned a number, called its *address*, that the computer uses to access that data. On most modern computers, the smallest data group with an address is eight bits long, and is called a *byte*. Larger groups comprise two or more bytes; for example, a *word* often contains 32 bits or 64 bits.

There are two principal ways a computer could number the individual bytes in a larger group, starting at either end. A big-endian system stores the most significant byte of a word at the smallest memory address and the least significant byte at the largest. A little-endian system, in contrast, stores the least-significant byte at the smallest address. Of the two, big-endian is thus closer to the way the digits of numbers are written left-to-right in English, with the most significant digit first, comparing digits to bytes and assuming addresses increase from left to right.

Both types of endianness are in widespread use in digital electronic engineering. The initial choice of endianness of a new design is often arbitrary, but later technology revisions and updates perpetuate the existing endianness to maintain backward compatibility. Big-endianness is the dominant ordering in networking protocols, such as in the Internet protocol suite, where it is referred to as *network order*, transmitting the most significant byte first. Conversely, little-endianness is the dominant ordering for processor architectures (x86, most ARM implementations, base RISC-V implementations) and their associated memory. File formats can use either ordering; some formats use a mixture of both or contain an indicator of which ordering is used throughout the file.

*Bi-endianness* is a feature supported by numerous computer architectures that feature switchable endianness in data fetches and stores or for instruction fetches. Other orderings are generically called *middle-endian* or *mixed-endian*.

## Origin

Endianness is primarily expressed as **big-endian** (BE) or **little-endian** (LE), terms introduced by Danny Cohen in an Internet Experiment Note published in 1980. Cohen borrowed the terms from an absurd episode in the satirical novel *Gulliver's Travels* by Jonathan Swift. In the imaginary land of Lilliput, scholars are fiercely divided by a never-ending debate over how correctly to break the shell of a boiled egg. Those who insist on breaking the big end of the shell are Big-Endians, while their opponents who break the opposite end of the shell are Little-Endians.

## Characteristics

Computer memory consists of a sequence of storage cells (smallest addressable units); in machines that support byte addressing, those units are called *bytes*. Each byte is identified and accessed in hardware and software by its memory address. If the total number of bytes in memory is *n*, then addresses are enumerated from 0 to *n* − 1.

Computer programs often use data structures or fields that may consist of more data than can be stored in one byte. In the context of this article, where its type cannot be arbitrarily complicated, a *field* consists of a consecutive sequence of bytes and represents a *simple data value* which, at least potentially, can be manipulated by *one* single hardware instruction. On most systems, the address of a multi-byte simple data value is the address of its first byte (the byte with the lowest address). There are exceptions to this rule – for example, the Add instruction of the IBM 1401 addresses variable-length fields at their low-order (highest-addressed) position with their lengths being defined by a word mark set at their high-order (lowest-addressed) position. When an operation such as addition is performed, the processor begins at the low-order positions at the high addresses of the two fields and works its way down to the high-order.

Another important attribute of a byte being part of a *field* is its *significance*. These attributes of the parts of a field play an important role in the sequence the bytes are accessed by the computer hardware, more precisely: by the low-level algorithms contributing to the results of a computer instruction.

### Numbers

Positional number systems (mostly base 2, or less often base 10) are the predominant way of representing and particularly of manipulating integer data by computers. In pure form, this is valid for moderately sized non-negative integers, e.g., of C data type `unsigned`. In such a number system, the *value* of a digit that contributes to the whole number is determined not only by its value as a single digit, but also by the position it holds in the complete number, called its significance. These positions can be mapped to memory mainly in two ways:

- Decreasing numeric significance with increasing memory addresses, known as *big-endian* and
- Increasing numeric significance with increasing memory addresses, known as *little-endian*.

In *big-endian* and *little-endian*, the *end* is the extremity where the *big* or *little* significance is written in the location indexed by the lowest memory address.

### Text

When character (text) strings are to be compared with one another, e.g., in order to support some mechanism like sorting, this is very frequently done lexicographically where a single positional element (character) also has a positional value. Lexicographical comparison means almost everywhere: first character ranks highest, as in the telephone book. Almost all machines that can do this using a single instruction are big-endian or at least mixed-endian.

Integer numbers written as text are always represented most significant digit first in memory, which is similar to big-endian, independently of text direction.

### Byte addressing

When memory bytes are printed sequentially from left to right (e.g., in a hex dump), little-endian representation of integers has the significance decreasing from right to left. In other words, it appears backwards when visualized, which can be counterintuitive.

This behavior arises, for example, in FourCC or similar techniques that involve packing characters into an integer, so that it becomes a sequence of specific characters in memory. For example, take the string "JOHN", stored in hexadecimal ASCII. On big-endian machines, the value appears left-to-right, coinciding with the correct string order for reading the result ("J O H N"). But on a little-endian machine, one would see "N H O J". Middle-endian machines complicate this even further; for example, on the PDP-11, a 32-bit float is stored as two 16-bit words "JO" "HN" in big-endian, with the characters in the 16-bit words being stored in little-endian, resulting in "O J N H".

### Byte swapping

Byte-swapping consists of rearranging bytes to change endianness. Many compilers provide built-ins that are likely to be compiled into native processor instructions (`bswap`/`movbe`), such as `__builtin_bswap32`. Software interfaces for swapping include:

- Standard network endianness functions (from/to BE, up to 32-bit). Windows has a 64-bit extension in `winsock2.h`.
- BSD and Glibc `endian.h` functions (from/to BE and LE, up to 64-bit).
- macOS `OSByteOrder.h` macros (from/to BE and LE, up to 64-bit).
- The `std::byteswap` function in C++23.

Some CPU instruction sets provide native support for endian byte swapping, such as `bswap` (x86 — 486 and later, i960 — i960Jx and later), and `rev` (ARMv6 and later).

Some compilers have built-in facilities for byte swapping. For example, GNU Fortran and the Intel Fortran Compiler both support the non-standard `CONVERT` specifier when opening a file, e.g.: `OPEN(unit, CONVERT='BIG_ENDIAN',...)`. Other compilers have options for generating code that globally enables the conversion for all file IO operations. This permits the reuse of code on a system with the opposite endianness without code modification.

## Considerations

### Simplified access to part of a field

On most systems, the address of a multi-byte value is the address of its first byte (the byte with the lowest address); little-endian systems of that type have the property that, for sufficiently low data values, the same value can be read from memory at different lengths without using different addresses (even when alignment restrictions are imposed). For example, a 32-bit memory location with content `4A 00 00 00` can be read at the same address as either 8-bit (value = 4A), 16-bit (004A), 24-bit (00004A), or 32-bit (0000004A), all of which retain the same numeric value. Although this little-endian property is rarely used directly by high-level programmers, it is occasionally employed by code optimizers as well as by assembly language programmers. While not allowed by C++, such type punning code is allowed as "implementation-defined" by the C11 standard and commonly used in code interacting with hardware.

### Calculation order

Some operations in positional number systems have a natural or preferred order in which the elementary steps are to be executed. This order may affect their performance on small-scale byte-addressable processors and microcontrollers. However, high-performance processors usually fetch multi-byte operands from memory in the same amount of time they would have fetched a single byte, so the complexity of the hardware is not affected by the byte ordering.

Addition, subtraction, and multiplication start at the least significant digit position and propagate the carry to the subsequent more significant position. On most systems, the address of a multi-byte value is the address of its first byte (the byte with the lowest address). The implementation of these operations is marginally simpler using little-endian machines, where this first byte contains the least significant digit.

Comparison and division start at the most significant digit and propagate a possible carry to the subsequent less significant digits. For fixed-length numerical values (typically of length 1,2,4,8,16), the implementation of these operations is marginally simpler on big-endian machines.

Some big-endian processors (e.g., the IBM System/360 and its successors) contain hardware instructions for lexicographically comparing varying-length character strings.

The normal data transport by an assignment statement is, in principle, independent of the endianness of the processor.

## Hardware

Many historical and extant processors use a big-endian memory representation, either exclusively or as a design option. The IBM System/360 uses big-endian byte order, as do its successors System/370, ESA/390, and z/Architecture. The PDP-10 uses big-endian addressing for byte-oriented instructions. The IBM Series/1 minicomputer uses big-endian byte order. The Motorola 6800 / 6801, the 6809 and the 68000 series of processors use the big-endian format. Solely big-endian architectures include the IBM z/Architecture and OpenRISC. The PDP-11 minicomputer, however, uses little-endian byte order, as does its VAX successor.

The Datapoint 2200 used simple bit-serial logic with little-endian to facilitate carry propagation. When Intel developed the 8008 microprocessor for Datapoint, they used little-endian for compatibility. However, as Intel was unable to deliver the 8008 in time, Datapoint used a medium-scale integration equivalent, but the little-endianness was retained in most Intel designs, including the MCS-48 and the 8086 and its x86 successors, including IA-32 and x86-64 processors. The MOS Technology 6502 family (including Western Design Center 65802 and 65C816), the Zilog Z80 (including Z180 and eZ80), the Altera Nios II, the Atmel AVR, the Andes Technology NDS32, the Qualcomm Hexagon, and many other processors and processor families are also little-endian.

The Intel 8051, unlike other Intel processors, expects 16-bit addresses for LJMP and LCALL in big-endian format; however, xCALL instructions store the return address onto the stack in little-endian format.

### Bi-endianness

Some instruction set architectures feature a setting which allows for switchable endianness in data fetches and stores, instruction fetches, or both; those instruction set architectures are referred to as *bi-endian*. Architectures that support switchable endianness include PowerPC/Power ISA, SPARC V9, ARM versions 3 and above, DEC Alpha, MIPS, Intel i860, PA-RISC, SuperH SH-4, IA-64, C-Sky, and RISC-V. This feature can improve performance or simplify the logic of networking devices and software. The word *bi-endian*, when said of hardware, denotes the capability of the machine to compute or pass data in either endian format.

Many of these architectures can be switched via software to default to a specific endian format (usually done when the computer starts up); however, on some systems, the default endianness is selected by hardware on the motherboard and cannot be changed via software (e.g., Alpha, which runs only in big-endian mode on the Cray T3E).

IBM AIX and IBM i run in big-endian mode on bi-endian Power ISA; Linux originally ran in big-endian mode, but by 2019, IBM had transitioned to little-endian mode for Linux to ease the porting of Linux software from x86 to Power. SPARC has no relevant little-endian deployment, as both Oracle Solaris and Linux run in big-endian mode on bi-endian SPARC systems, and can be considered big-endian in practice. ARM, C-Sky, and RISC-V have no relevant big-endian deployments and can be considered little-endian in practice.

The term *bi-endian* refers primarily to how a processor treats data accesses. Instruction accesses (fetches of instruction words) on a given processor may still assume a fixed endianness, even if data accesses are fully bi-endian, though this is not always the case, such as on Intel's IA-64-based Itanium CPU, which allows both.

Some nominally bi-endian CPUs require motherboard help to fully switch endianness. For instance, the 32-bit desktop-oriented PowerPC processors in little-endian mode act as little-endian from the point of view of the executing programs, but they require the motherboard to perform a 64-bit swap across all 8 byte lanes to ensure that the little-endian view of things will apply to I/O devices. In the absence of this unusual motherboard hardware, device driver software must write to different addresses to undo the incomplete transformation and also must perform a normal byte swap.

Some CPUs, such as many PowerPC processors intended for embedded use and almost all SPARC processors, allow per-page choice of endianness.

SPARC processors since the late 1990s (SPARC v9 compliant processors) allow data endianness to be chosen with each individual instruction that loads from or stores to memory.

The ARM architecture supports two big-endian modes, called *BE-8* and *BE-32*. CPUs up to ARMv5 only support BE-32 or word-invariant mode. Here, any naturally aligned 32-bit access works like in little-endian mode, but access to a byte or 16-bit word is redirected to the corresponding address and unaligned access is not allowed. ARMv6 introduces BE-8 or byte-invariant mode, where access to a single byte works as in little-endian mode, but accessing a 16-bit, 32-bit or (starting with ARMv8) 64-bit word results in a byte swap of the data. This simplifies unaligned memory access as well as memory-mapped access to registers other than 32-bit.

Many processors have instructions to convert a word in a register to the opposite endianness, that is, they swap the order of the bytes in a 16-, 32- or 64-bit word.

Recent Intel x86 and x86-64 architecture CPUs have a MOVBE instruction (Intel Core since generation 4, after Atom), which fetches a big-endian format word from memory or writes a word into memory in big-endian format. These processors are otherwise thoroughly little-endian.

There are also devices that use different formats in different places. For instance, the BQ27421 Texas Instruments battery gauge uses the little-endian format for its registers and the big-endian format for its random-access memory.

SPARC historically used big-endian until version 9, which is bi-endian. Similarly, early IBM POWER processors were big-endian, but the PowerPC and Power ISA descendants are now bi-endian. The ARM architecture was little-endian before version 3, when it became bi-endian.

### Floating point

Although many processors use little-endian storage for all types of data (integer, floating point), there are a number of hardware architectures where floating-point numbers are represented in big-endian form while integers are represented in little-endian form. There are ARM processors that have mixed-endian floating-point representation for double-precision numbers: each of the two 32-bit words is stored as little-endian, but the most significant word is stored first. VAX floating point stores little-endian 16-bit words in big-endian order. Because there have been many floating-point formats with no network standard representation for them, the XDR standard uses big-endian IEEE 754 as its representation. It may therefore appear strange that the widespread IEEE 754 floating-point standard does not specify endianness. Theoretically, this means that even standard IEEE floating-point data written by one machine might not be readable by another. However, on modern standard computers (i.e., implementing IEEE 754), one may safely assume that the endianness is the same for floating-point numbers as for integers, making the conversion straightforward regardless of data type. Small embedded systems using special floating-point formats may be another matter, however.

### Variable-length data

Most instructions considered so far contain the size (lengths) of their operands within the operation code. Frequently available operand lengths are 1, 2, 4, 8, or 16 bytes. But there are also architectures where the length of an operand may be held in a separate field of the instruction or with the operand itself, e.g., by means of a word mark. Such an approach allows operand lengths up to 256 bytes or larger. The data types of such operands are character strings or BCD. Machines able to manipulate such data with one instruction (e.g. compare, add) include the IBM 1401, 1410, 1620, System/360, System/370, ESA/390, and z/Architecture, all of them of type big-endian.

### Middle-endian

Numerous other orderings, generically called *middle-endian* or *mixed-endian*, are possible.

The PDP-11 is primarily a 16-bit little-endian system. The instructions to convert between floating-point and integer values in the optional floating-point processor of the PDP-11/45, PDP-11/70, and in some later processors, stored 32-bit *double precision integer long* values with the 16-bit halves swapped from the expected little-endian order. The UNIX C compiler used the same format for 32-bit long integers. This ordering is known as *PDP-endian*.

UNIX was one of the first systems to allow the same code to be compiled for platforms with different internal representations. One of the first programs converted was supposed to print out `Unix`, but on the Series/1 it printed `nUxi` instead.

A way to interpret this endianness is that it stores a 32-bit integer as two little-endian 16-bit words, with a big-endian word ordering:

| byte offset | 8-bit value | 16-bit little-endian value |
|---|---|---|
| 0 | 0Bh | 0A0Bh |
| 1 | 0Ah |   |
| 2 | 0Dh | 0C0Dh |
| 3 | 0Ch |   |

Segment descriptors of IA-32 and compatible processors keep a 32-bit base address of the segment stored in little-endian order, but in four nonconsecutive bytes, at relative positions 2, 3, 4 and 7 of the descriptor start.

## Software

### Logic design

Hardware description languages (HDLs) used to express digital logic often support arbitrary endianness, with arbitrary granularity. For example, in SystemVerilog, a word can be defined as little-endian or big-endian.

### Files and filesystems

The recognition of endianness is important when reading a file or filesystem created on a computer with different endianness.

Fortran sequential unformatted files created with one endianness usually cannot be read on a system using the other endianness because Fortran usually implements a record (defined as the data written by a single Fortran statement) as data preceded and succeeded by count fields, which are integers equal to the number of bytes in the data. An attempt to read such a file using Fortran on a system of the other endianness results in a run-time error, because the count fields are incorrect.

Unicode text can optionally start with a byte order mark (BOM) to signal the endianness of the file or stream. Its code point is U+FEFF. In UTF-32 for example, a big-endian file should start with `00 00 FE FF`; a little-endian should start with `FF FE 00 00`.

Application binary data formats, such as MATLAB *.mat* files, or the *.bil* data format, used in topography, are usually endianness-independent. This is achieved by storing the data always in one fixed endianness or carrying with the data a switch to indicate the endianness. An example of the former is the binary XLS file format that is portable between Windows and Mac systems and always little-endian, requiring the Mac application to swap the bytes on load and save when running on a big-endian Motorola 68K or PowerPC processor.

TIFF image files are an example of the second strategy, whose header instructs the application about the endianness of their internal binary integers. If a file starts with the signature `MM` it means that integers are represented as big-endian, while `II` means little-endian. Those signatures need a single 16-bit word each, and they are palindromes, so they are endianness independent. `I` stands for Intel and `M` stands for Motorola. Intel CPUs are little-endian, while Motorola 680x0 CPUs are big-endian. This explicit signature allows a TIFF reader program to swap bytes if necessary when a given file was generated by a TIFF writer program running on a computer with a different endianness.

As a consequence of its original implementation on the Intel 8080 platform, the operating system-independent File Allocation Table (FAT) file system is defined with little-endian byte ordering, even on platforms using another endianness natively, necessitating byte-swap operations for maintaining the FAT on these platforms.

ZFS, which combines a filesystem and a logical volume manager, is known to provide adaptive endianness and to work with both big-endian and little-endian systems.

### Networking

Many IETF RFCs use the term *network order*, meaning the order of transmission for bytes *over the wire* in network protocols. Among others, the historic RFC 1700 defines the network order for protocols in the Internet protocol suite to be big-endian.

However, not all protocols use big-endian byte order as the network order. The Server Message Block (SMB) protocol uses little-endian byte order. In CANopen, multi-byte parameters are always sent least significant byte first (little-endian). The same is true for Ethernet Powerlink.

The Berkeley sockets API defines a set of functions to convert 16- and 32-bit integers to and from network byte order: the `htons` (host-to-network-short) and `htonl` (host-to-network-long) functions convert 16- and 32-bit values respectively from machine (*host*) to network order; the `ntohs` and `ntohl` functions convert from network to host order. These functions may be a no-op on a big-endian system.

While the high-level network protocols usually consider the byte (mostly meant as *octet*) as their atomic unit, the lowest layers of a network stack may deal with the ordering of bits within a byte. Bit ordering is sometimes referred to as little-endian or big-endian. Bit ordering does not need to be the same as byte ordering. For example, RS-232 transmits bits least significant first, I2C transmits bits most significant first, and SPI can be sent in either order. Ethernet transmits individual bits least significant first, but bytes are sent big-endian.

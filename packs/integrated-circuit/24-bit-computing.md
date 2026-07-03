---
title: "24-bit computing"
source: https://en.wikipedia.org/wiki/24-bit_computing
domain: integrated-circuit
license: CC-BY-SA-4.0
tags: integrated circuit
fetched: 2026-07-03
---

# 24-bit computing

In computer architecture, **24-bit** integers, memory addresses, or other data units are those that are 24 bits (3 octets) wide. Also, 24-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers, address buses, or data buses of that size.

Notable **24-bit** machines include the CDC 924 – a 24-bit version of the CDC 1604, CDC lower 3000 series, SDS 930 and SDS 940, the ICT 1900 series, the Elliott 4100 series, and the Datacraft minicomputers/Harris H series.

The term SWORD is sometimes used to describe a 24-bit data type with the S prefix referring to sesqui.

The range of unsigned integers that can be represented in 24 bits is 0 to 16,777,215 (FFFFFF16 in hexadecimal). The range of signed integers that can be represented in 24 bits is −8,388,608 to 8,388,607.

## Usage

The IV/70, was introduced by Four-Phase Systems in 1971. The IV/70 has an integer word size of 24 bits. Byte addressing is not supported directly but bytes are handled by instructions that pack three bytes per word. The IV/70 CPU is a 9-chip LSI microprocessor based on three AL4 8-bit slice register/ALUs.

The IBM System/360, announced in 1964, was a popular computer system with 24-bit addressing and 32-bit general registers and arithmetic. The early 1980s saw the first popular personal computers, including the IBM PC/AT with an Intel 80286 processor using 24-bit addressing and 16-bit general registers and arithmetic, and the Apple Macintosh 128K with a Motorola 68000 processor featuring 24-bit addressing and 32-bit registers. Some late-1980s Apple computers such as the Macintosh SE/30 and Macintosh IIx retained some 24-bit code in their ROMs despite being advertised as 32-bit computers. As a result, these computers require the installation of the MODE32 memory manager to address more than 8Mb of RAM.

The ARM1, supported 24-bit memory address, as it can access 16MiB memory.

The eZ80 is a microprocessor and microcontroller family, with 24-bit registers and 24-bit linear addressing. It is binary compatible with the 8/16-bit Z80. Although eZ80 supports 24-bit adds, subtracts, and moves, most ALU operations are limited to 8-bit.

The 65816 is a microprocessor and microcontroller family with 16-bit registers and 24-bit bank switched addressing. It is binary compatible with the 8-bit 6502.

Several fixed-point digital signal processors have a 24-bit data bus, selected as the basic word length because it gave the system a reasonable precision for the processing audio (sound). In particular, the Motorola 56000 series has three parallel 24-bit data buses, one connected to each memory space: program memory, data memory X, and data memory Y.

Engineering Research Associates (later merged into UNIVAC) designed a series of 24-bit drum memory machines including the Atlas, its commercial version the UNIVAC 1101, the ATHENA computer, the UNIVAC 1824 guidance computer, etc. Those designers selected a 24-bit word length because the Earth is roughly 40 million feet in diameter, and an intercontinental ballistic missile guidance computer needs to do the Earth-centered inertial navigation calculations to an accuracy of a few feet.

OpenCL has a built-in intrinsic for multiplication (`mul24()`) with two 24-bit integers, returning a 32-bit result. It is typically much faster than a 32-bit multiplication.

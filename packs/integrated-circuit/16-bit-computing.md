---
title: "16-bit computing"
source: https://en.wikipedia.org/wiki/16-bit_computing
domain: integrated-circuit
license: CC-BY-SA-4.0
tags: integrated circuit
fetched: 2026-07-03
---

# 16-bit computing

In computer architecture, **16-bit** integers, memory addresses, or other data units are those that are 16 bits (2 octets) wide. Also, 16-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers, address buses, or data buses of that size. 16-bit microcomputers are microcomputers that use 16-bit microprocessors.

A 16-bit register can store 216 different values. The range of integer values that can be stored in 16 bits depends on the integer representation used. With the two most common representations, the range is 0 through 65,535 (216 − 1) for representation as an (unsigned) binary number, and −32,768 (−1 × 215) through 32,767 (215 − 1) for representation as two's complement. Since 216 is 65,536, a processor with 16-bit memory addresses can directly access 64 KiB (65,536 bytes) of byte-addressable memory. If a system uses segmentation with 16-bit segment offsets, more can be accessed.

## 16-bit architecture

The MIT Whirlwind (c. 1951) was quite possibly the first-ever 16-bit computer. It had an unusual word size for the era; most systems used six-bit character code and used a word length of some multiple of 6-bits. This changed with the effort to introduce ASCII, which used a 7-bit code and naturally led to the use of an 8-bit multiple which could store a single ASCII character or two binary-coded decimal digits.

The 16-bit word length thus became more common in the 1960s, especially on minicomputer systems. Early 16-bit computers (c. 1965–70) include the IBM 1130, the HP 2100, the Data General Nova, and the DEC PDP-11. Early 16-bit microprocessors, often modeled on one of the mini platforms, began to appear in the 1970s. Examples (c. 1973–76) include the five-chip National Semiconductor IMP-16 (1973), the two-chip NEC μCOM-16 (1974), the three-chip Western Digital MCP-1600 (1975), and the five-chip Toshiba T-3412 (1976).

Early single-chip 16-bit microprocessors (c. 1975–76) include the Panafacom MN1610 (1975), National Semiconductor PACE (1975), General Instrument CP1600 (1975), Texas Instruments TMS9900 (1976), Ferranti F100-L, and the HP BPC. Other notable 16-bit processors include the Intel 8086, the Intel 80286, the WDC 65C816, and the Zilog Z8000. The Intel 8088 was binary compatible with the Intel 8086, and was 16-bit in that its registers were 16 bits wide, and arithmetic instructions could operate on 16-bit quantities, even though its external bus was 8 bits wide.

16-bit processors have been almost entirely supplanted in the personal computer industry, and are used less than 32-bit (or 8-bit) CPUs in embedded applications.

### 16/32-bit Motorola 68000 and Intel 386SX

The Motorola 68000 is sometimes called 16-bit because of the way it handles basic arithmetic. The instruction set was based on 32-bit numbers and the internal registers were 32 bits wide, so by common definitions, the 68000 is a 32-bit design. Internally, 32-bit arithmetic is performed using two 16-bit operations, and this leads to some descriptions of the system as 16-bit, or "16/32".

Such solutions have a long history in the computer field, with various designs performing math even one bit at a time, known as "serial arithmetic", while most designs by the 1970s processed at least a few bits at a time. A common example is the Data General Nova, which was a 16-bit design that performed 16-bit math as a series of four 4-bit operations. 4-bits was the word size of a widely available single-chip ALU and thus allowed for inexpensive implementation. Using the definition being applied to the 68000, the Nova would be a 4-bit computer, or 4/16. Not long after the introduction of the Nova, a second version was introduced, the SuperNova, which included four of the 4-bit ALUs running in parallel to perform math 16 bits at a time and therefore offer higher performance. This was invisible to the user and the programs, which always used 16-bit instructions and data. In a similar fashion, later 68000-family members, starting with the Motorola 68020, had 32-bit ALUs.

One may also see references to systems being, or not being, 16-bit based on some other measure. One common one is when the address space is not the same size of bits as the internal registers. Most 8-bit CPUs of the 1970s fall into this category; the MOS 6502, Intel 8080, Zilog Z80 and most others had 16-bit address space which provided 64 KiB of address space. This also meant address manipulation required two instruction cycles. For this reason, most processors had special 8-bit addressing modes, the zero page, improving speed. This sort of difference between internal register size and external address size remained in the 1980s, although often reversed, as memory costs of the era made a machine with 32-bit addressing, 2 or 4 GiB, a practical impossibility. For example, the 68000 exposed only 24 bits of addressing on the DIP, limiting it to a still huge (for the era) 16 MiB.

A similar analysis applies to Intel's 80286 CPU replacement, called the 386SX, which is a 32-bit processor with 32-bit ALU and internal 32-bit data paths with a 16-bit external bus and 24-bit addressing of the processor it replaced.

## 16-bit application

In the context of IBM PC compatible and Wintel platforms, a 16-bit application is any software written for MS-DOS, OS/2 1.x or early versions of Microsoft Windows which originally ran on the 16-bit Intel 8088 and Intel 80286 microprocessors. Such applications used a 20-bit or 24-bit segment or selector-offset address representation to extend the range of addressable memory locations beyond what was possible using only 16-bit addresses. Programs containing more than 216 bytes (65,536 bytes) of instructions and data therefore required special instructions to switch between their 64-kibibyte segments, increasing the complexity of programming 16-bit applications.

## 16-bit microcontrollers

Single chip 16-bit microcontrollers appeared around 1983 with the introduction of the Intel 8061. As of 2025, 16-bit microcontrollers cost well under a US dollar in 100 quantities, similar in price to legacy 8-bit. Even some 32-bit microcontrollers are priced under a US dollar.

## List of 16-bit CPUs

- Angstrem
  - 1801 series CPU
- Data General
  - Nova
  - Eclipse
- Digital Equipment Corporation
  - PDP-11 (for LSI-11, see Western Digital, below)
    - DEC J-11
    - DEC T-11
- EnSilica
  - eSi-1600
- Fairchild Semiconductor
  - 9440 MICROFLAME
- Ferranti
  - Ferranti F100-L
  - Ferranti F200-L
- General Instrument
  - CP1600
- Hewlett-Packard
  - HP 21xx/2000/1000/98xx/BPC
  - HP 3000
- Honeywell
  - Honeywell Level 6/DPS 6
- IBM
  - 1130/1800
  - System/7
  - Series/1
  - System/36
- Infineon
  - XE166 family
  - C166/C167 family
  - XC2000
- Intel
  - Intel 8086/Intel 8088
  - Intel 80186/Intel 80188
  - Intel 80286
  - Intel MCS-96
- Lockheed
  - MAC-16
- MIL-STD-1750A
- Motorola
  - Motorola 68HC12
  - Motorola 68HC16
- National Semiconductor
  - IMP-16
  - PACE/INS8900
- NEC
  - μCOM-16
  - NEC V20 and V30
- Panafacom
  - MN1610
- Renesas
  - Renesas M16C (16-bit registers, 24-bit address space)
- Ricoh
  - Ricoh 5A22 (WDC 65816 clone used in SNES)
- Texas Instruments
  - Texas Instruments TMS9900
  - TI MSP430
- Toshiba
  - T-3412
- Western Design Center
  - WDC 65816/65802
- Western Digital
  - MCP-1600
    - used in the DEC LSI-11
    - used in the Pascal MicroEngine
    - used in the WD16
- Xerox
  - Alto
- Zilog
  - Zilog Z8000
  - Zilog Z280

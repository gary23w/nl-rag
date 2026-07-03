---
title: "4-bit computing"
source: https://en.wikipedia.org/wiki/4-bit_computing
domain: h8-family
license: CC-BY-SA-4.0
tags: h8 family
fetched: 2026-07-03
---

# 4-bit computing

**4-bit computing** is the use of computer architectures in which integers and other data units are 4 bits wide. 4-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers or data buses of that size. A group of four bits is also called a nibble and has 24 = 16 possible values, with a range of 0 to 15.

4-bit computation is largely obsolete, i.e. CPUs supporting 4-bit as the maximum size, or 4-bit data bus are no longer available, but 4-bit microcontrollers, such as the EM Microelectronic EM6580, are still available as of 2026.

4-bit processors were widely used in electronic calculators and other roles where decimal math was used, like electronic cash registers, microwave oven timers, and so forth. This is because a 4-bit value holds a single binary-coded decimal (BCD) digit, making it a natural size for directly processing decimal values. As a 4-bit value is generally too small to hold a memory address for real-world programs or data, the address bus of these systems was generally larger. For instance, the canonical 4-bit microprocessor, the Intel 4004, had a 12-bit address format.

4-bit designs were used only for a short period when integrated circuits were still expensive, and were found primarily in cost-sensitive roles. While 4-bit computing is mostly obsolete, 4-bit values are still used in the same decimal-centric roles they were developed for, and modern implementations are generally much wider and process multiple 4-bit values in parallel. By the 1990s, most such uses had been replaced by general purpose binary designs.

## History

A 4-bit processor may seem limited, but it is a good match for calculators, where each decimal digit fits into four bits.

Some of the first microprocessors had a 4-bit word length and were developed around 1970. The first commercial microprocessor was the binary-coded decimal (BCD-based) Intel 4004, developed for calculator applications in 1971; it had a 4-bit word length, but had 8-bit instructions and 12-bit addresses. It was succeeded by the Intel 4040, which added interrupt support and a variety of other new features.

The first commercial single-chip computer was the 4-bit Texas Instruments TMS 1000 (1974). It contained a 4-bit CPU with a Harvard architecture and 8-bit-wide instructions, an on-chip instruction ROM, and an on-chip data RAM with 4-bit words.

The Rockwell PPS-4 was another early 4-bit processor, introduced in 1972, which had a long lifetime in handheld games and similar roles. It was steadily improved and by 1975 been combined with several support chips to make a one-chip computer.

The 4-bit processors were programmed in assembly language or Forth, e.g. "MARC4 Family of 4 bit Forth CPU" (which is now discontinued) because of the extreme size constraint on programs and because common programming languages (for microcontrollers, 8-bit and larger), such as the C programming language, do not support 4-bit data types (C, and C++, and more languages require that the size of the `char` data type be at least 8 bits, and that all data types other than bitfields have a size that is a multiple of the character size).

The 1970s saw the emergence of 4-bit software applications for mass markets like pocket calculators. During the 1980s, 4-bit microprocessors were used in handheld electronic games to keep costs low.

In the 1970s and 1980s, a number of research and commercial computers used bit slicing, in which the CPU's arithmetic logic unit (ALU) was built from multiple 4-bit-wide sections, each section including a chip such as an Am2901 or 74181.

The Zilog Z80 (discontinued in 2024), although it is an 8-bit microprocessor, has a 4-bit ALU.

Although the Data General Nova is a series of 16-bit minicomputers, the original Nova and the Nova 1200 internally processed numbers 4 bits at a time with a 4-bit ALU, sometimes called "nybble-serial".

The HP Saturn processors, used in many Hewlett-Packard calculators between 1984 and 2003 (including the HP 48 series of scientific calculators) are "4-bit" (or hybrid 64-/4-bit) machines. They string multiple 4-bit words together, e.g. to form a 20-bit memory address, and most of the registers are 64 bits wide, storing 16 4-bit digits. Operations were performed nybble-serial.

In addition, some early calculators – such as the 1967 Casio AL-1000, the 1972 Sinclair Executive, and the aforementioned 1984 HP Saturn – had 4-bit datapaths that accessed their registers 4 bits (one BCD digit) at a time.

## Uses

One bicycle computer specifies that it uses a "4 bit, 1-chip microcomputer". Other typical uses include coffee makers, infrared remote controls, and security alarms.

The processor in Barbie typewriters that can encrypt is a 4-bit microcontroller.

Several manufacturers used 4-bit microcontrollers in their early electronic games:

- Mattel's Funtronics Jacks, Red Light Green Light, Tag, Plus One and Dalla$.
- Milton Bradley Lightfight and Electronic Battleship 1982.
- Coleco Head to Head Basketball.
- National Semiconductor Quiz Kid Racer.
- Entex Space Invader.
- Texas Instruments My Little Computer.

Western Digital used a 4-bit microcontroller as the basis for their WD2412 time-of-day clock.

The Grundy Newbrain computer uses a 4-bit microcontroller to manage its keyboard, tape I/O, and its built-in 16 character VF alphanumeric display.

The Apple Lisa utilizes a 4-bit microcontroller to control the keyboard, mouse, RTC, and soft power switch.

## Details

With 4 bits, it is possible to create 16 different values. All single-digit hexadecimal numbers can be written with four bits.

Binary-coded decimal is a digital encoding method for numbers using decimal notation, with each decimal digit represented by four bits.

## List of 4-bit processors

- Intel 4004 (first 4-bit microprocessor and widely regarded as the first commercially available microprocessor from 1971, discontinued 1981)
- Intel 4040 (discontinued 1981)
- TMS 1000 (the first high-volume commercial microcontroller, from 1974, after Intel 4004; now discontinued)
- American Microsystems S2000
- Atmel MARC4 core (discontinued because of low demand. Last ship date: 7 March 2015)
- Essex SX 200
- Samsung S3C7 (KS57 Series) 4-bit microcontrollers (RAM: 512 to 5264 nibbles, 6 MHz clock)
- Toshiba TLCS-47 series
- HP Saturn
- NEC μPD75X
- NEC μCOM-4
- NEC (now Renesas) μPD612xA (discontinued), μPD613x, μPD6x and μPD1724x infrared remote control transmitter microcontrollers
- EM Microelectronic-Marin EM6600 family, EM6580, EM6682, etc.
- Epson S1C63 family
- National Semiconductor "COPS I" and "COPS II" ("COP400") 4-bit microcontroller families
- National Semiconductor MAPS MM570X
- Rockwell PPS-4
- Sharp SM590/SM591/SM595
- Sharp SM550/SM551/SM552
- Sharp SM578/SM579
- Sharp SM5E4
- Sharp LU5E4POP
- Sharp SM5J5/SM5J6
- Sharp SM530
- Sharp SM531
- Sharp SM500 (ROM 1197×8 bit, RAM 40×4 bit, a divider and 56-segment LCD driver circuit)
- Sharp SM5K1
- Sharp SM4A
- Sharp SM510 (ROM 2772×8 bit, RAM 128×4 bit, a divider and 132-segment LCD driver circuit)
- Sharp SM511/SM512 (ROM 4032×8 bit, RAM 128/142×4 bit, a divider and 136/200-segment LCD driver circuit)
- Sharp SM563

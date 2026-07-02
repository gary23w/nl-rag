---
title: "8-bit computing"
source: https://en.wikipedia.org/wiki/8-bit_computing
domain: gptq-quantization
license: CC-BY-SA-4.0
tags: post training quantization, weight only quantization, layer wise quantization, gptq method, low bit inference
fetched: 2026-07-02
---

# 8-bit computing

In computer architecture, **8-bit** integers or other data units are those that are 8 bits wide (1 octet). Also, 8-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers or data buses of that size. Memory addresses (and thus address buses) for 8-bit CPUs are generally larger than 8-bit, usually 16-bit. 8-bit microcomputers are microcomputers that use 8-bit microprocessors.

The term '8-bit' is also applied to the character sets that could be used on computers with 8-bit bytes, the best known being various forms of extended ASCII, including the ISO/IEC 8859 series of national character sets – especially Latin 1 for English and Western European languages.

The IBM System/360 introduced byte-addressable memory with 8-bit bytes, as opposed to bit-addressable or decimal digit-addressable or word-addressable memory, although its general-purpose registers were 32 bits wide, and addresses were contained in the lower 24 bits of those addresses. Different models of System/360 had different internal data path widths; the IBM System/360 Model 30 (1965) implemented the 32-bit System/360 architecture, but had an 8-bit native path width, and performed 32-bit arithmetic 8 bits at a time.

The first widely adopted 8-bit microprocessor was the Intel 8080, being used in many hobbyist computers of the late 1970s and early 1980s, often running the CP/M operating system; it had 8-bit data words and 16-bit addresses. The Zilog Z80 (compatible with the 8080) and the Motorola 6800 were also used in similar computers. The Z80 and the MOS Technology 6502 8-bit CPUs were widely used in home computers and second- and third-generation game consoles of the 1970s and 1980s. Many 8-bit CPUs or microcontrollers are the basis of today's ubiquitous embedded systems.

## Historical context

8-bit microprocessors were the first widely used microprocessors in the computing industry, marking a major shift from mainframes and minicomputers to smaller, more affordable systems. The introduction of 8-bit processors in the 1970s enabled the production of personal computers, leading to the popularization of computing and setting the foundation for the modern computing landscape.

The 1976 Zilog Z80, one of the most popular 8-bit CPUs (though with 4-bit ALU, at least in the original), was discontinued in 2024 (its product line Z84C00), with Last Time Buy (LTB) orders by 14 June 2024.

## Details

An 8-bit register can store 28 different values. The range of integer values that can be stored in 8 bits depends on the integer representation used. With the two most common representations, the range is 0 through 255 (28 − 1) for representation as an (unsigned) binary number, and −128 (−1 × 27) through 127 (27 − 1) for representation as two's complement.

8-bit CPUs use an 8-bit data bus and can therefore access 8 bits of data in a single machine instruction. The address bus is typically a double octet (16 bits) wide, due to practical and economical considerations. This implies a direct address space of 64 KB (65,536 bytes) on most 8-bit processors.

Most home computers from the 8-bit era fully exploited the address space, such as the BBC Micro (Model B) with 32 KB of RAM plus 32 KB of ROM. Others like the very popular Commodore 64 had full 64 KB RAM, plus 20 KB ROM, meaning with 16-bit addressing not all of the RAM could be used by default (e.g. from the included BASIC language interpreter in ROM); without exploiting bank switching, which allows for breaking the 64 KB (RAM) limit in some systems. Other computers would have as low as 1 KB (plus 4 KB ROM), such as the Sinclair ZX80 (while the later very popular ZX Spectrum had more memory), or even only 128 bytes of RAM (plus storage from a ROM cartridge), as in an early game console Atari 2600 and thus 8-bit addressing would have been enough for the RAM, if it would not have needed to cover ROM too). The Commodore 128, and other 8-bit systems, meaning still with 16-bit addressing, could use more than 64 KB, i.e. 128 KB RAM, also the BBC Master with it expandable to 512 KB of RAM.

While in general 8-bit CPUs have 16-bit addressing, in some architectures both are available, such as in the MOS Technology 6502 CPU, where the zero page is used extensively, saving one byte in the instructions accessing that page, and also having 16-bit addressing instructions that take 2 bytes for the address plus 1 for the opcode.

Some index registers, such as the two in the 6502, are 8-bit. This limits the size of the arrays addressed using indexed addressing instructions to objects of up to 256 bytes (28 bytes) without requiring more complicated code. Other 8-bit CPUs, such as the Motorola 6800 and Intel 8080, have 16-bit index registers.*"Interview with William Mensch, 1995 October 09". *Silicon Genesis: Oral Histories of Semiconductor Technology*. Stanford University Libraries. Retrieved 1 July 2026.*

## Notable 8-bit CPUs

The first commercial 8-bit processor was the Intel 8008 (1972) which was originally intended for the Datapoint 2200 intelligent terminal. Most competitors to Intel started off with such character oriented 8-bit microprocessors. Modernized variants of these 8-bit machines are still one of the most common types of processor in embedded systems.

The MOS Technology 6502, and variants of it, were used in personal computers, such as the Apple I, Apple II, Atari 8-bit computers, BBC Micro, PET, VIC-20, and in home video game consoles such as the Atari 2600 and the Nintendo Entertainment System.

| Manufacturer | Processor | Year | Comment |
|---|---|---|---|
| Intel | 8008 | 1972 | Datapoint 2200 compatible |
| Intel | 8080 | 1974 | 8008 source compatible |
| Motorola | 6800 | 1974 |   |
| Signetics | 2650 | 1975 |   |
| Fairchild | F8 | 1975 |   |
| MOS | 6502 | 1975 | Similar to 6800, but incompatible |
| Microchip | PIC | 1975 | Harvard architecture microcontroller |
| Electronic Arrays | EA9002 | 1976 | 8-bit data, 12-bit addressing |
| RCA | 1802 | 1976 |   |
| Zilog | Z80 | 1976 | 8080 binary compatible |
| Intel | 8048 | 1976 | Intel's first 8-bit microcontroller |
| Intel | 8085 | 1976 | 8080 binary compatible |
| Zilog | Z8 | 1978 | Harvard architecture microcontroller |
| Motorola | 6809 | 1978 | 6800 source compatible |
| Intel | 8051 | 1980 | Harvard architecture microcontroller |
| MOS | 6510 | 1982 | Enhanced 6502 custom-made for use in the Commodore 64 |
| Ricoh | 2A03 | 1982 | 6502 clone minus BCD instructions for the Nintendo Entertainment System |
| Zilog | Z180 | 1985 | Z80 binary compatible |
| Motorola | 68HC11 | 1985 |   |
| Hudson | HuC6280 | 1987 | 65C02 binary compatible |
| Atmel | AVR | 1996 |   |
| Zilog | eZ80 | 1999 | Backward Z80 binary compatible |
| Infineon | XC800 | 2005 |   |
| Freescale | 68HC08 | ? |   |
| Motorola | 6803 | ? |   |
| NEC | 78K0 | ? |   |

## Use for training, prototyping, and general hardware education

8-bit processors continue to be designed for general education about computer hardware, as well as for hobbyists' interests. One such CPU was designed and implemented using 7400-series integrated circuits on a breadboard. Designing 8-bit CPUs and their respective assemblers is a common training exercise for engineering students, engineers, and hobbyists. FPGAs are used for this purpose.

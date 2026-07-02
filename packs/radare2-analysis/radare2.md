---
title: "Radare2"
source: https://en.wikipedia.org/wiki/Radare2
domain: radare2-analysis
license: CC-BY-SA-4.0
tags: radare2 analysis framework, command line reverse engineering, binary debugger toolkit, hex editor inspection, disassembly workflow
fetched: 2026-07-02
---

# Radare2

**Radare2** (also known as **r2**) is a complete framework for reverse-engineering and analyzing binaries; composed of a set of small utilities that can be used together or independently from the command line. Built around a disassembler for computer software which generates assembly language source code from machine-executable code, it supports a variety of executable formats for different processor architectures and operating systems.

## History

Radare2 was created in February 2006, aiming to provide a free and simple command-line interface for a hexadecimal editor supporting 64 bit offsets to make searches and recovering data from hard-disks, for forensic purposes. Since then, the project has grown with the aim changed to provide a complete framework for analyzing binaries while adhering to several principles of the Unix philosophy.

In 2009, the decision was made to completely rewrite it, to get around limitations in the initial design. Since then, the project continued to grow, and attracted several resident developers.

In 2016, the first *r2con* took place in Barcelona, gathering more than 100 participants, featuring talks about various features and improvements of the framework.

Radare2 has been the focus of multiple presentations at several high-profile security conferences, like the recon, hack.lu, 33c3.

### Rizin fork

In 2020 Radare2 was forked as Rizin due to disagreements between the original author and a group of outside contributors.

## Features and usage

Radare2 itself has a steep learning curve since its main executable binaries are operated by a command line interface. Originally built around a hexadecimal editor, it now has a multitude of tools and features, and also bindings for several languages. Alongside the command line interface, it has a web user interface option and an official graphical user interface project called Iaito.

### Static analysis

Radare2 is able to assemble and disassemble a lot of software programs, mainly executables, but it can also perform binary diffing with graphs, extract information like relocations symbols, and various other types of data. Internally, it uses a NoSQL database named sdb to keep track of analysis information that can be inferred by Radare2 or manually added by the user. Since it is able to deal with malformed binaries, it has also been used by software security researchers for analysis purposes.

### Dynamic analysis

Radare2 has a built-in debugger that is lower-level than GDB. It can also interface with GDB and WineDBG to debug Windows binaries on other systems. In addition, it can also be used as a kernel debugger with VMWare.

### Software exploitation

Since it features a disassembler and a low-level debugger, Radare2 can be useful to developers of exploits. The software has features which assist in exploit development, such as a ROP gadget search engine and mitigation detection. Because of the software's flexibility and support for many file formats, it is often used by capture the flag teams and other security-oriented personnel. Radare2 can also assist in creating shellcodes with its 'ragg2' tool, similar to metasploit.

### Graphical user interface (GUI)

Project Iaito has been developed as the first dedicated graphical user interface (GUI) for Radare2; it's been forked by Cutter as secondly developed graphical user interface (GUI) for Radare2. When the Cutter project was separated from Radare2 project at the end of 2020, Iaito was re-developed to be the current official Radare2 graphical user interface (GUI) maintained by Radare2 project members.

## Supported architectures, formats

- Recognized file formats
  - COFF and derivatives, including Win32/64/generic PE
  - ELF and derivatives
  - Mach-O (Mach) and derivatives
  - Game Boy and Game Boy Advance cartridges
  - MZ (DOS)
  - Java class
  - Lua 5.1 and Python bytecode
  - dyld cache dump
  - Dex (Dalvik EXecutable)
  - Xbox xbe format
  - Plan9 binaries
  - WinRAR virtual machine
  - File system like the ext family, ReiserFS, HFS+, NTFS, FAT, ...
  - DWARF and PDB file formats for storing additional debug information
  - Amiga Hunk
  - Raw binary

- Instruction sets
  - Intel x86 family
  - ARM architecture
  - Atmel AVR series
  - Brainfuck
  - Motorola 68k and H8
  - Ricoh 5A22
  - MOS 6502
  - Smartcard PSOS Virtual Machine
  - Java virtual machine
  - MIPS: mipsb/mipsl/mipsr/mipsrl/r5900b/r5900l
  - PowerPC
  - SPARC Family
  - TMS320Cxxx series
  - Argonaut RISC Core
  - Intel 51 series: 8051/80251b/80251s/80930b/80930s
  - Zilog Z80
  - CR16
  - Cambridge Silicon Radio (CSR)
  - AndroidVM Dalvik
  - DCPU-16
  - EFI bytecode
  - Game Boy (z80-like)
  - Java Bytecode
  - Malbolge
  - MSIL/CIL
  - Nios II
  - SuperH
  - Spc700
  - Systemz
  - TMS320
  - V850
  - Whitespace
  - XCore

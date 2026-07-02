---
title: "Interactive Disassembler"
source: https://en.wikipedia.org/wiki/Interactive_Disassembler
domain: disassembly-analysis
license: CC-BY-SA-4.0
tags: disassembly analysis, interactive disassembler workflow, assembly instruction decoding, opcode instruction set, binary code inspection
fetched: 2026-07-02
---

# Interactive Disassembler

The **Interactive Disassembler** (**IDA**) is a disassembler for computer software which generates assembly language source code from machine-executable code. It supports a variety of executable formats for different processors and operating systems. It can also be used as a debugger for Windows PE, Mac OS X Mach-O, and Linux ELF executables. A decompiler plug-in, which generates a high level, C source code-like representation of the analysed program, is available at extra cost.

IDA is used widely in software reverse engineering, including for malware analysis and software vulnerability research. IDA's decompiler is one of the most popular and widely used decompilation frameworks, and IDA has been called the "de-facto industry standard" for program disassembly and static binary analysis.

## History

Ilfak Guilfanov began working on IDA in 1990, and initially distributed it as a shareware application. In 1996, the Belgian company DataRescue took over the development of IDA and began to sell it as a commercial product, under the name IDA Pro.

Initial versions of IDA did not have a graphical user interface (GUI), and ran as an extended DOS, OS/2, or Windows console application. In 1999, DataRescue released the first version of IDA Pro with a GUI, IDA Pro 4.0.

In 2005, Guilfanov founded Hex-Rays to pursue the development of the Hex-Rays Decompiler IDA extension. In January 2008, Hex-Rays assumed the development and support of DataRescue's IDA Pro.

In 2022, Hex-Rays was acquired by a group of investors led by Smartfin, a European venture capital and private equity investor. Co-investors in the acquisition included the Belgian public holding company The Federal Holding & Investment Company (SFPIM), and the Walloon public investment firm Regional Investment Company of Wallonia (SRIW).

## Features

IDA disassembles a compiled program back into an assembly language representation. In addition to performing basic disassembly, IDA also automatically annotates disassembled programs with information about:

- cross-references between code and data in the program
- function locations, function stack frames, and function calling conventions
- reconstructed data types

However, the nature of disassembly precludes total accuracy, and a great deal of human intervention is necessarily required; IDA has interactive functionality to aid in improving the disassembly. A typical IDA user will begin with an automatically generated disassembly listing and then convert sections from code to data and vice versa, rename, annotate, and otherwise add information to the listing, until its functionality becomes clear.

### Scripting

"IDC scripts" make it possible to extend the operation of the disassembler. Some helpful scripts are provided, which can serve as the basis for user written scripts. Most frequently scripts are used for extra modification of the generated code. For example, external symbol tables can be loaded, thereby using the function names of the original source code.

Users have created plugins that allow other common scripting languages to be used instead of, or in addition to, IDC. IdaRUB supports Ruby and IDAPython adds support for Python. As of version 5.4, IDAPython (dependent on Python 2.5) comes preinstalled with IDA Pro.

### Debugging

IDA Pro supports a number of debuggers, including:

- Remote Windows, Linux, and Mac applications (provided by Hex-Rays) allow running an executable in its native environment (presumably using a virtual machine for malware)
- GNU Debugger (gdb) is supported on Linux and OS X, as well as the native Windows debugger
- A Bochs plugin is provided for debugging simple applications (i.e., damaged UPX or mpress compacted executables)
- An Intel PIN-based debugger
- A trace replayer

## Versions

The latest full version of IDA Pro is available via paid annual subscription (version 9.0sp1 as of December 2024), while a less capable version (limited to x86), named IDA Free, is available for download free of cost.

## Supported systems/processors/compilers

- System hosts
  - Windows x86 and ARM
  - Linux x86
  - macOS x86 and Apple silicon
- Recognized executable file formats
  - COFF and derivatives, including Win32/64/generic PE
  - ELF and derivatives (generic)
  - Mach-O (Mach)
  - NLM (NetWare)
  - LC/LE/LX (OS/2 2.x+ and various DOS extenders)
  - NE (OS/2 1.x, Win16, and various DOS extenders)
  - MZ (MS-DOS)
  - OMF and derivatives (generic)
  - AIM (generic)
  - raw binary, such as a ROM image or a COM file
- Instruction sets
  - Intel 80x86 family
  - ARM architecture
  - Motorola 68k and H8
  - Zilog Z80
  - MOS 6502
  - Intel i860
  - DEC Alpha
  - Analog Devices ADSP218x
  - Angstrem KR1878
  - Atmel AVR series
  - DEC series PDP11
  - Fujitsu F2MC16L/F2MC16LX
  - Fujitsu FR 32-bit Family
  - Hitachi SH3/SH3B/SH4/SH4B
  - Hitachi H8: h8300/h8300a/h8s300/h8500
  - Intel 196 series: 80196/80196NP
  - Intel 51 series: 8051/80251b/80251s/80930b/80930s
  - Intel i960 series
  - Intel Itanium (ia64) series
  - Java virtual machine
  - MIPS: mipsb/mipsl/mipsr/mipsrl/r5900b/r5900l
  - Microchip PIC: PIC12Cxx/PIC16Cxx/PIC18Cxx
  - MSIL
  - Mitsubishi 7700 Family: m7700/m7750
  - Mitsubishi m32/m32rx
  - Mitsubishi m740
  - Mitsubishi m7900
  - Motorola DSP 5600x Family: dsp561xx/dsp5663xx/dsp566xx/dsp56k
  - Motorola ColdFire
  - Motorola HCS12
  - NEC 78K0/78K0S
  - PA-RISC
  - PowerPC
  - RISC-V
  - Xenon PowerPC family
  - SGS-Thomson ST20/ST20c4/ST7
  - SPARC family
  - Samsung SAM8
  - Siemens C166
  - TMS320Cxxx series
- Compiler/libraries (for automatic library function recognition)
  - Borland C++ 5.x for DOS/Windows
  - Borland C++ 3.1
  - Borland C Builder v4 for DOS/Windows
  - GNU C++ for Cygwin
  - Microsoft C
  - QuickC
  - Visual C++
  - Watcom C/C++ (16/32 bit) for DOS & OS/2
  - ARM C v1.2
  - GNU C++ for Unix/common

## Logo

IDA Pro's logo is a cropped image of Françoise d'Aubigné, Marquise de Maintenon. The logo image is similar to a miniature painting of Françoise d'Aubigné attested to a painter in the circle of Pierre Mignard.

The original greyscale version of the logo was introduced in September 1999, with the release of IDA 4.0. Ilfak Guilfanov has stated that the logo is not a depiction of Saint Ida of Louvain.

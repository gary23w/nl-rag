---
title: "Assembly language (part 2/2)"
source: https://en.wikipedia.org/wiki/Assembly_language
domain: retro-z80-assembly
license: CC-BY-SA-4.0
tags: z80 assembly, zilog z80, z80 opcode, intel 8080
fetched: 2026-07-02
part: 2/2
---

## Use of assembly language

When the stored-program computer was introduced, programs were written in machine code, and loaded into the computer from punched paper tape or toggled directly into memory from console switches. Kathleen Booth "is credited with inventing assembly language" based on theoretical work she began in 1947, while working on the ARC2 at Birkbeck, University of London, following consultation by Andrew Booth (later her husband) with mathematician John von Neumann and physicist Herman Goldstine at the Institute for Advanced Study.

In late 1948, the Electronic Delay Storage Automatic Calculator (EDSAC) had an assembler (named "initial orders") integrated into its bootstrap program. It used one-letter mnemonics developed by David Wheeler, who is credited by the IEEE Computer Society as the creator of the first "assembler". Reports on the EDSAC introduced the term "assembly" for the process of combining fields into an instruction word. SOAP (Symbolic Optimal Assembly Program) was an assembly language for the IBM 650 computer written by Stan Poley in 1955.

Assembly languages eliminated much of the error-prone, tedious, and time-consuming first-generation programming needed with the earliest computers, freeing programmers from tedium such as remembering numeric codes and calculating addresses. They were once widely used for all sorts of programming. By the late 1950s their use had largely been supplanted by higher-level languages in the search for improved programming productivity. Today, assembly language is still used for direct hardware manipulation, access to specialized processor instructions, or to address critical performance issues. Typical uses are device drivers, low-level embedded systems, and real-time systems (see § Current usage).

Numerous programs were written entirely in assembly language. The Burroughs MCP (1961) was the first computer for which an operating system was not developed entirely in assembly language; it was written in Executive Systems Problem Oriented Language (ESPOL), an Algol dialect. Many commercial applications were written in assembly language as well, including a large amount of the IBM mainframe software developed by large corporations. COBOL, FORTRAN and some PL/I eventually displaced assembly language, although a number of large organizations retained assembly-language application infrastructures well into the 1990s.

Assembly language was the primary development language for 8-bit home computers such as the Apple II, Atari 8-bit computers, ZX Spectrum, and Commodore 64. Interpreted BASIC on these systems did not offer maximum execution speed and full use of facilities to take full advantage of the available hardware. Assembly language was the default choice for programming 8-bit consoles such as the Atari 2600 and Nintendo Entertainment System.

Key software for IBM PC compatibles such as MS-DOS, Turbo Pascal, and the Lotus 1-2-3 spreadsheet was written in assembly language. As computer speed grew exponentially, assembly language became a tool for speeding up parts of programs, such as the rendering of *Doom*, rather than a dominant development language. In the 1990s, assembly language was used to maximise performance from systems such as the Sega Saturn, and as the primary language for arcade hardware using the TMS34010 integrated CPU/GPU such as *Mortal Kombat* and *NBA Jam*.

### Current usage

There has been debate over the usefulness and performance of assembly language relative to high-level languages.

Although assembly language has specific niche uses where it is important (see below), there are other tools for optimization.

As of July 2017, the TIOBE index of programming language popularity ranks assembly language at 11, ahead of Visual Basic, for example. Assembler can be used to optimize for speed or optimize for size. In the case of speed optimization, modern optimizing compilers are claimed to render high-level languages into code that can run as fast as hand-written assembly, despite some counter-examples. The complexity of modern processors and memory sub-systems makes effective optimization increasingly difficult for compilers and assembly programmers alike. Increasing processor performance has meant that most CPUs sit idle most of the time, with delays caused by predictable bottlenecks such as cache misses, I/O operations and paging, making raw code execution speed a non-issue for many programmers.

There are still certain computer programming domains in which the use of assembly programming is more common:

- Writing code for systems with older processors that have limited high-level language options such as the Atari 2600, Commodore 64, and graphing calculators. Programs for these computers of the 1970s and 1980s are often written in the context of demoscene or retrogaming subcultures.
- Code that must interact directly with the hardware, for example in device drivers and interrupt handlers.
- In an embedded processor or DSP, high-repetition interrupts require the shortest number of cycles per interrupt, such as an interrupt that occurs 1000 or 10000 times a second.
- Programs that need to use processor-specific instructions not implemented in a compiler. A common example is the bitwise rotation instruction at the core of many encryption algorithms, as well as querying the parity of a byte or the 4-bit carry of an addition.
- Stand-alone executables that are required to execute without recourse to the run-time components or libraries associated with a high-level language, such as the firmware for telephones, automobile fuel and ignition systems, air-conditioning control systems, and security systems.
- Programs with performance-sensitive inner loops, where assembly language provides optimization opportunities that are difficult to achieve in a high-level language. For example, linear algebra with BLAS or discrete cosine transformation (e.g. SIMD assembly version from x264).
- Programs that create vectorized functions for programs in higher-level languages such as C. In the higher-level language this is sometimes aided by compiler intrinsic functions which map directly to SIMD mnemonics, but nevertheless result in a one-to-one assembly conversion specific for the given vector processor.
- Real-time programs such as simulations, flight navigation systems, and medical equipment. For example, in a fly-by-wire system, telemetry must be interpreted and acted upon within strict time constraints. Such systems must eliminate sources of unpredictable delays, which may be created by interpreted languages, automatic garbage collection, paging operations, or preemptive multitasking. Choosing assembly or lower-level languages for such systems gives programmers greater visibility and control over processing details.
- Cryptographic algorithms that must always take strictly the same time to execute, preventing timing attacks.
- Video encoders and decoders such as rav1e (an encoder for AV1) and dav1d (the reference decoder for AV1) contain assembly to leverage AVX2 and ARM Neon instructions when available.
- Modify and extend legacy code written for IBM mainframe computers.
- Situations where complete control over the environment is required, in extremely high-security situations where nothing can be taken for granted.
- Computer viruses, bootloaders, certain device drivers, or other items very close to the hardware or low-level operating system.
- Instruction set simulators for monitoring, tracing and debugging where additional overhead is kept to a minimum.
- Situations where no high-level language exists, on a new or specialized processor for which no cross compiler is available.
- Reverse engineering and modifying program files such as:
  - existing binaries that may or may not have originally been written in a high-level language, for example when trying to recreate programs for which source code is not available or has been lost, or cracking copy protection of proprietary software.
  - Video games (also termed ROM hacking), which is possible via several methods. The most widely employed method is altering program code at the assembly language level.

Assembly language is still taught in most computer science and electronic engineering programs. Although few programmers today regularly work with assembly language as a tool, the underlying concepts remain important. Such fundamental topics as binary arithmetic, memory allocation, stack processing, character set encoding, interrupt processing, and compiler design would be hard to study in detail without a grasp of how a computer operates at the hardware level. Since a computer's behaviour is fundamentally defined by its instruction set, the logical way to learn such concepts is to study an assembly language. Most modern computers have similar instruction sets. Therefore, studying a single assembly language is sufficient to learn the basic concepts, recognize situations where the use of assembly language might be appropriate, and to see how efficient executable code can be created from high-level languages.

### Typical applications

- Assembly language is typically used in a system's boot code, the low-level code that initializes and tests the system hardware prior to booting the operating system and is often stored in ROM. (BIOS on IBM-compatible PC systems and CP/M is an example.)
- Assembly language is often used for low-level code, for instance for operating system kernels, which cannot rely on the availability of pre-existing system calls and must indeed implement them for the particular processor architecture on which the system will be running.
- Some compilers translate high-level languages into assembly first before fully compiling, allowing the assembly code to be viewed for debugging and optimization purposes.
- Some compilers for relatively low-level languages, such as Pascal or C, allow the programmer to embed assembly language directly in the source code (so called inline assembly). Programs using such facilities can then construct abstractions using different assembly language on each hardware platform. The system's portable code can then use these processor-specific components through a uniform interface.
- Assembly language is useful in reverse engineering. Many programs are distributed only in machine code form which is straightforward to translate into assembly language by a disassembler, but more difficult to translate into a higher-level language through a decompiler. Tools such as the Interactive Disassembler make extensive use of disassembly for such a purpose. This technique is used by hackers to crack commercial software, and competitors to produce software with similar results from competing companies.
- Assembly language is used to enhance speed of execution, especially in early personal computers with limited processing power and RAM.
- Assemblers can be used to generate blocks of data, with no high-level language overhead, from formatted and commented source code, to be used by other code.

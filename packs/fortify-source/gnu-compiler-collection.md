---
title: "GNU Compiler Collection"
source: https://en.wikipedia.org/wiki/GNU_Compiler_Collection
domain: fortify-source
license: CC-BY-SA-4.0
tags: fortify source hardening, compiler runtime buffer checks, glibc object size checking, hardened build flags
fetched: 2026-07-02
---

# GNU Compiler Collection

The **GNU Compiler Collection** (**GCC**; formerly **GNU C Compiler**) is a collection of compilers from the GNU Project that support various programming languages, hardware architectures, and operating systems. The Free Software Foundation (FSF) distributes GCC as free software under the GNU General Public License (GNU GPL). GCC is a key component of the GNU toolchain which is used for most projects related to GNU and the Linux kernel. With roughly 15 million lines of code in 2019, GCC is one of the largest free programs in existence. It has played an important role in the growth of free software, as both a tool and an example.

When it was first released in 1987 by Richard Stallman, GCC 1.0 was named the *GNU C Compiler* since it only handled the C programming language. It was extended to compile C++ in December of that year. Front ends were later developed for Objective-C, Objective-C++, Fortran, Ada, Go, D, Modula-2, Rust, COBOL, and ALGOL 68 among others. The OpenMP and OpenACC specifications are also supported in the C and C++ compilers.

As well as being the official compiler of the GNU operating system, GCC has been adopted as the standard compiler by many other modern Unix-like computer operating systems, including most Linux distributions. Most BSD family operating systems also switched to GCC shortly after its release, although since then, FreeBSD and Apple macOS have moved to the Clang compiler, largely due to licensing reasons. GCC can also compile code for Windows, Android, iOS, Solaris, HP-UX, AIX, and MS-DOS compatible operating systems.

GCC has been ported to more platforms and instruction set architectures than any other compiler, and is widely deployed as a tool in the development of both free and proprietary software. GCC is also available for many embedded systems, including ARM-based and Power ISA-based chips.

## History

In late 1983, in an effort to bootstrap the GNU operating system, Richard Stallman asked Andrew S. Tanenbaum, the author of the Amsterdam Compiler Kit (also known as the *Free University* *Compiler Kit*), for permission to use that software for GNU. When Tanenbaum advised him that the compiler itself was not free, but rather only the university, Stallman decided to work on a different compiler. His initial plan was to rewrite an existing compiler from Lawrence Livermore National Laboratory for the Pastel language, written in Pastel, with some help from Len Tower and others. Stallman wrote a new C front end for the Livermore compiler, but then realized that it required megabytes of stack space, an impossibility on a 68000 Unix system that didn't allow more than 64 KB of stack space, and concluded he would have to write a new compiler from scratch. None of the Pastel compiler code ended up in GCC, though Stallman did use the C front end he had written in Pastel.

GCC was first released March 22, 1987, available by FTP from MIT. Stallman was listed as the author but cited others for their contributions, including Tower for "parts of the parser, RTL generator, RTL definitions, and of the Vax machine description", Jack Davidson and Christopher W. Fraser for the idea of using RTL as an intermediate language, and Paul Rubin for writing most of the preprocessor. Described as the "first free software hit" by Peter H. Salus, the GNU compiler arrived just at the time when Sun Microsystems was unbundling its development tools from its operating system, selling them separately at a higher combined price than the previous bundle, which led many of Sun's users to buy or download GCC instead of the vendor's tools. While Stallman considered GNU Emacs as his main project, by 1990 GCC supported thirteen computer architectures, was outperforming several vendor compilers, and was used commercially by several companies.

### EGCS fork

As GCC was licensed under the GPL, programmers wanting to work in other directions—particularly those writing interfaces for languages other than C—were free to develop their own fork of the compiler, provided they meet the GPL's terms, including its requirements to distribute source code. Multiple forks proved inefficient and unwieldy, however, and the difficulty in getting work accepted by the official GCC project was greatly frustrating for many, as the project favored stability over new features. The FSF kept such close control on what was added to the official version of GCC 2.x (developed since 1992) that GCC was used as one example of the "cathedral" development model in Eric S. Raymond's essay *The Cathedral and the Bazaar*.

In 1997, a group of developers formed the *Experimental/Enhanced GNU Compiler System (EGCS)* to merge several experimental forks into a single project. The basis of the merger was a development snapshot of GCC (taken around the 2.7.2 and later followed up to 2.8.1 release). Mergers included g77 (Fortran), PGCC (P5 Pentium-optimized GCC), many C++ improvements, and many new architectures and operating system variants.

While both projects followed each other's changes closely, EGCS development proved considerably more vigorous, so much so that the FSF officially halted development on their GCC 2.x compiler, blessed EGCS as the official version of GCC, and appointed the EGCS project as the GCC maintainers in April 1999. With the release of GCC 2.95 in July 1999 the two projects were once again united. GCC has since been maintained by a varied group of programmers from around the world under the direction of a steering committee.

GCC 3 (2002) removed a front-end for CHILL due to a lack of maintenance.

Before version 4.0 the Fortran front end was `g77`, which only supported FORTRAN 77, but later was dropped in favor of the new GNU Fortran front end that supports Fortran 95 and large parts of Fortran 2003 and Fortran 2008 as well.

As of version 4.8, GCC is implemented in C++.

Support for Cilk Plus existed from GCC 5 to GCC 7.

GCC has been ported to a wide variety of instruction set architectures, and is widely deployed as a tool in the development of both free and proprietary software. GCC is also available for many embedded systems, including Symbian (called *gcce*), ARM-based, and Power ISA-based chips. The compiler can target a wide variety of platforms, including video game consoles such as the PlayStation 2, Cell SPE of PlayStation 3, and Dreamcast. It has been ported to "more than 60 platforms".

## Supported languages

As of the 16.1 release, GCC includes front ends for C (`gcc`), C++ (`g++`), Objective-C, Objective-C++, Fortran (`gfortran`), Ada (GNAT), Go (`gccgo`), D (`gdc`, since 9.1), Modula-2 (`gm2`, since 13.1), Rust (`gccrs`, since 15.1), COBOL (`gcobol`, since 15.1), and ALGOL 68 (`ga68`, since 16.1) programming languages, with the OpenMP and OpenACC parallel language extensions being supported since GCC 5.1. Versions prior to GCC 7 also supported Java (`gcj`), allowing compilation of Java to native machine code.

Third-party front ends exist for many languages, such as Pascal (`gpc`), Mercury, Modula-3, VHDL (`GHDL`) and PL/I. A few experimental branches exist to support additional languages, such as the GCC UPC compiler for Unified Parallel C.

The default target for C++ since GCC 15.1 is *gnu++20*, a superset of C++20, and the default target for C since GCC 15 is *gnu23*, a superset of C23, with strict standard support also available. GCC also provides experimental support for C2Y, C++23, and C++26. GCC 16.1 was released on 30 April 2026.

## Design

GCC's external interface follows Unix conventions. Users invoke a language-specific driver program (`gcc` for C, `g++` for C++, etc.), which interprets command arguments, calls the actual compiler, runs the assembler on the output, and then optionally runs the linker to produce a complete executable binary.

Each of the language compilers is a separate program that reads source code and outputs machine code. All have a common internal structure. A per-language front end parses the source code in that language and produces an abstract syntax tree ("tree" for short).

These are, if necessary, converted to the middle end's input representation, called *GENERIC* form; the middle end then gradually transforms the program towards its final form. Compiler optimizations and static code analysis techniques (such as FORTIFY_SOURCE, a compiler directive that attempts to discover some buffer overflows) are applied to the code. These work on multiple representations, mostly the architecture-independent GIMPLE representation and the architecture-dependent RTL representation. Finally, machine code is produced using architecture-specific pattern matching originally based on an algorithm of Jack Davidson and Chris Fraser.

GCC was written primarily in C except for parts of the Ada front end. The distribution includes the standard libraries for Ada and C++ whose code is mostly written in those languages. On some platforms, the distribution also includes a low-level runtime library, **libgcc**, written in a combination of machine-independent C and processor-specific machine code, designed primarily to handle arithmetic operations that the target processor cannot perform directly.

GCC uses many additional tools in its build, many of which are installed by default by many Unix and Linux distributions (but which, normally, aren't present in Windows installations), including Perl, Flex, Bison, and other common tools. In addition, it currently requires three additional libraries to be present in order to build: GMP, MPC, and MPFR.

In May 2010, the GCC steering committee decided to allow use of a C++ compiler to compile GCC. The compiler was intended to be written mostly in C plus a subset of features from C++. In particular, this was decided so that GCC's developers could use the destructors and generics features of C++.

In August 2012, the GCC steering committee announced that GCC now uses C++ as its implementation language. This means that to build GCC from sources, a C++ compiler is required that understands ISO/IEC C++03 standard.

On May 18, 2020, GCC moved away from ISO/IEC C++03 standard to ISO/IEC C++11 standard (i.e. needed to compile, bootstrap, the compiler itself; by default it however compiles later versions of C++).

### Front ends

Each front end uses a parser to produce the abstract syntax tree of a given source file. Due to the syntax tree abstraction, source files of any of the different supported languages can be processed by the same back end. GCC started out using LALR parsers generated with Bison, but gradually switched to hand-written recursive-descent parsers for C++ in 2004, and for C and Objective-C in 2006. As of 2021 all front ends use hand-written recursive-descent parsers.

Until GCC 4.0, the tree representation of the program was not fully independent of the processor being targeted. The meaning of a tree was somewhat different for different language front ends, and front ends could provide their own tree codes. This was simplified with the introduction of GENERIC and GIMPLE, two new forms of language-independent trees that were introduced with the advent of GCC 4.0. GENERIC is more complex, based on the GCC 3.x Java front end's intermediate representation. GIMPLE is a simplified GENERIC, in which various constructs are *lowered* to multiple GIMPLE instructions. The C, C++, and Java front ends produce GENERIC directly in the front end. Other front ends instead have different intermediate representations after parsing and convert these to GENERIC.

In either case, the so-called "gimplifier" then converts this more complex form into the simpler SSA-based GIMPLE form that is the common language for a large number of language- and architecture-independent global (function scope) optimizations.

### GENERIC and GIMPLE

*GENERIC* is an intermediate representation language used as a "middle end" while compiling source code into executable binaries. A subset, called *GIMPLE*, is targeted by all the front ends of GCC.

The middle stage of GCC does all of the code analysis and optimization, working independently of both the compiled language and the target architecture, starting from the GENERIC representation and expanding it to register transfer language (RTL). The GENERIC representation contains only the subset of the imperative programming constructs optimized by the middle end.

In transforming the source code to GIMPLE, complex expressions are split into a three-address code using temporary variables. This representation was inspired by the SIMPLE representation proposed in the McCAT compiler by Laurie J. Hendren for simplifying the analysis and optimization of imperative programs.

### Optimization

Optimization can occur during any phase of compilation; however, the bulk of optimizations are performed after the syntax and semantic analysis of the front end and before the code generation of the back end; thus a common, though somewhat self-contradictory, name for this part of the compiler is the "middle end."

The exact set of GCC optimizations varies from release to release as it develops, but includes the standard algorithms, such as loop optimization, jump threading, common subexpression elimination, instruction scheduling, and so forth. The RTL optimizations are of less importance with the addition of global SSA-based optimizations on GIMPLE trees, as RTL optimizations have a much more limited scope, and have less high-level information.

Some of these optimizations performed at this level include dead-code elimination, partial-redundancy elimination, global value numbering, sparse conditional constant propagation, and scalar replacement of aggregates. Array dependence based optimizations such as automatic vectorization and automatic parallelization are also performed. Profile-guided optimization is also possible.

### C++ Standard Library (libstdc++)

The GCC project includes an implementation of the C++ Standard Library called libstdc++, licensed under the GPLv3 License with an exception to link non-GPL-compatible applications when sources are built with GCC. Since GCC Version 3, the C++ ABI is based on the ABI published by Intel for the Itanium C++ ABI.

### Other features

Some features of GCC include:

**Link-time optimization**

Link-time optimization

optimizes across object file boundaries to directly improve the linked binary. Link-time optimization relies on an intermediate file containing the serialization of some

Gimple

representation included in the object file.

The file is generated alongside the object file during source compilation. Each source compilation generates a separate object file and link-time helper file. When the object files are linked, the compiler is executed again and uses the helper files to optimize code across the separately compiled object files.

**Plugins**

Plugins

extend the GCC compiler directly.

Plugins allow a stock compiler to be tailored to specific needs by external code loaded as plugins. For example, plugins can add, replace, or even remove middle-end passes operating on

Gimple

representations.

Several GCC plugins have already been published, notably:

- The Python plugin, which links against libpython, and allows one to invoke arbitrary Python scripts from inside the compiler. The aim is to allow GCC plugins to be written in Python.
- The MELT plugin provides a high-level Lisp-like language to extend GCC.

The support of plugins was once a contentious issue in 2007.

**C++ transactional memory**

The C++ language has an active proposal for transactional memory. It can be enabled in GCC 6 and newer when compiling with

-fgnu-tm

.

**Unicode identifiers**

Although the C++ language requires support for non-ASCII

Unicode characters

in

identifiers

, the feature has only been supported since GCC 10. As with the existing handling of string literals, the source file is assumed to be encoded in

UTF-8

. The feature is optional in C, but has been made available too since this change.

**C extensions**

GNU C extends the C programming language with several non-standard-features, including

nested functions

.

## Architectures

The primary supported (and best tested) processor families are 64- and 32-bit ARM, 64- and 32-bit x86 64 and x86 and 64-bit PowerPC and SPARC.

GCC target processor families as of version 11.1 include:

- AArch64
- Alpha
- ARM
- AVR
- Blackfin
- eBPF
- Epiphany (GCC 4.8)
- H8/300
- HC12
- IA-32 (32-bit x86)
- IA-64 (Intel Itanium)
- MIPS
- Motorola 68000 series
- MSP430
- Nvidia GPU
- Nvidia PTX
- PA-RISC
- PDP-11
- PowerPC
- R8C / M16C / M32C
- RISC-V
- SPARC
- SuperH
- System/390 / z/Architecture
- VAX
- x86-64

Lesser-known target processors supported in the standard release have included:

- 68HC11
- A29K
- C6x
- CR16
- D30V
- DSP16xx
- ETRAX CRIS
- FR-30
- FR-V
- IBM ROMP
- Intel i960
- IP2000
- M32R
- MCORE
- MIL-STD-1750A
- MMIX
- MN10200
- MN10300
- Motorola 88000
- NS32K
- RL78
- Stormy16
- V850
- Xtensa

Additional processors have been supported by GCC versions maintained separately from the FSF version:

- Cortus APS3
- ARC
- AVR32
- C166 and C167
- D10V
- EISC
- eSi-RISC
- Hexagon
- LatticeMico32
- LatticeMico8
- MeP
- MicroBlaze
- Motorola 6809
- MSP430
- NEC SX architecture
- Nios II and Nios
- OpenRISC
- PDP-10
- PIC24/dsPIC
- PIC32
- Propeller
- Saturn (HP48XGCC)
- System/370
- TIGCC (m68k variant)
- TMS9900
- TriCore
- Z8000
- ZPU

The GCJ Java compiler can target either a native machine language architecture or the Java virtual machine's Java bytecode. When retargeting GCC to a new platform, bootstrapping is often used. Motorola 68000, Zilog Z80, and other processors are also targeted in the GCC versions developed for various Texas Instruments, Hewlett Packard, Sharp, and Casio programmable graphing calculators.

## License

GCC is licensed under the GNU General Public License version 3. The *GCC runtime exception* permits compilation of proprietary programs (in addition to free software) with GCC headers and runtime libraries. This does not impact the license terms of GCC source code.

However this exception is limited. For example, when non-GPL-compatible software is used together with GCC within the Compile Process, following the GPLv3 for all of the propagated object code GCC generates, becomes mandatory as it is derived from the GPL-licensed libraries.

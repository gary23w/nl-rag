---
title: "Free Pascal"
source: https://en.wikipedia.org/wiki/Free_Pascal
domain: object-pascal
license: CC-BY-SA-4.0
tags: object pascal, delphi language, free pascal, lazarus ide
fetched: 2026-07-02
---

# Free Pascal

**Free Pascal Compiler** (**FPC**) is a compiler for the closely related programming-language dialects Pascal and Object Pascal. It is free software released under the GNU General Public License, with exception clauses that allow static linking against its runtime libraries and packages for any purpose in combination with any other software license.

It supports its own Object Pascal dialect, as well as the dialects of several other Pascal family compilers to a certain extent, including those of Borland Pascal (named "Turbo Pascal" until the 1990 version 6), Borland (later Embarcadero) Delphi, and some historical Macintosh compilers. The dialect is selected on a per-unit (module) basis, and more than one dialect can be used per program.

It follows a *write once, compile anywhere* philosophy and is available for many CPU architectures and operating systems (see Targets). It supports inline assembly language and includes an internal assembler capable of parsing several dialects such as AT&T and Intel style.

There are separate projects to facilitate developing cross-platform graphical user interface (GUI) applications, the most prominent one being the Lazarus integrated development environment (IDE).

## Supported dialects

Initially, Free Pascal adopted the *de facto* standard dialect of Pascal programmers, Borland Pascal, but later adopted Delphi's Object Pascal. From version 2.0 on, Delphi compatibility has been continuously implemented or improved.

The compiler can operate in different *modes*, for example the developers made it clear that they would incorporate working patches for the standardized dialects of the American National Standards Institute (ANSI) and International Organization for Standardization (ISO) to create a standards-compliant mode.

A small effort has been made to support some of the Apple Pascal syntax to ease interfacing to the Classic Mac OS and macOS. The Apple dialect implements some standard Pascal features that Turbo Pascal and Delphi omit.

The 2.2.*x* release series did not significantly change the dialect objectives beyond roughly Delphi 7 level syntax, instead aiming for closer compatibility. A notable exception to this was the addition of support for generics to Free Pascal in version 2.2.0, several years before they were supported in any capacity by Delphi.

In 2011 several Delphi 2006-specific features were added in the development branch, and some of the starting work for the features new in Delphi 2009 (most notably the addition of the `UnicodeString` type) was completed. The development branch also has an *Objective-Pascal* extension for Objective-C (Cocoa) interfacing.

Beginning with version 2.7.1, Free Pascal added support for ISO Pascal. As of version 3.0.0, it has been able to compile standardpascal.org's P5 ISO Pascal compiler with no changes.

## History

### Early years

Free Pascal was created when Borland clarified that Borland Pascal development for MS-DOS would stop with version 7. Student Florian Paul Klämpfl began developing his own compiler written in the Turbo Pascal dialect which produced 32-bit code for the GO32v1 DOS extender, (developed and used by the DJ's GNU Programming Platform project).

Originally, the compiler was a 16-bit executable compiled by Turbo Pascal. After two years, the compiler was able to compile itself into a 32-bit executable.

### Expansion

The initial 32-bit compiler was published on the Internet, and the first contributors joined the project. Later, a Linux port was created by Michael van Canneyt, five years before the Borland Kylix Pascal compiler for Linux became available.

The DOS port was adapted for use in OS/2 using the Eberhard Mattes eXtender (EMX) which made OS/2 the second supported compiling target. As well as Florian Klämpfl the original author, Daniël Mantione also contributed significantly to make this happen, providing the original port of the run-time library to OS/2 and EMX. The compiler improved gradually, and the DOS version migrated to the GO32v2 extender. This culminated in release 0.99.5, which was much more widely used than prior versions, and was the last release aiming only for Borland Pascal compliance; later releases added a Delphi compatibility mode. This release was also ported to systems using Motorola 68000 family (m68k) processors.

With release 0.99.8 the Win32 target was added, and a start was made with incorporating some Delphi features. Stabilizing for a non-beta release began, and version 1.0 was released in July 2000. The 1.0.*x* series was widely used, in business and education. For the 1.0.*x* releases, the port to 68k CPU was redone, and the compiler produced stable code for several 68k Unix-like and AmigaOS operating systems.

### Version 2

During the stabilization of what would become 1.0.*x*, and also when porting to the Motorola 68k systems, it was clear that the design of the code generator was far too limited in many aspects. The principal problems were that adding processors meant rewriting the code generator, and that the register allocation was based on the principle of always keeping three free registers between building blocks, which was inflexible and difficult to maintain.

For these reasons, the 1.1.*x* series branched off from the 1.0.*x* main branch in December 1999. At first, changes were mostly clean-ups and rewrite-redesigns to all parts of the compiler. The code generator and register allocator were also rewritten. Any remaining missing Delphi compatibility was added.

The work on 1.1.x continued slowly but steadily. In late 2003, a working PowerPC port became available, followed by an ARM port in summer 2004, a SPARC port in fall 2004, and an x86-64-AMD64 port in early 2004, which made the compiler available for a 64-bit platform.

In November 2003, a first beta release of the 1.1.*x* branch was packaged and numbered 1.9.0. These were quickly followed by versions 1.9.2 and 1.9.4; the latter introduced OS X support. The work continued with version 1.9.6 (January 2005), 1.9.8 (late February 2005), 2.0.0 (May 2005), 2.0.2 (December 2005), and 2.0.4 (August 2006).

### Version 2.2.x

In 2006, some of the major reworks planned for 2.2, such as the rewrite of the unit system, had still not begun, and it was decided to instead start stabilizing the already implemented features.

Some of the motives for this roadmap change were the needs of the Lazarus integrated development environment project, particularly the internal linker, support for Win64, Windows CE, and OS X on x86, and related features like DWARF. After betas 2.1.2 and 2.1.4, version 2.2.0 was released in September 2007, followed by version 2.2.2 in August 2008 and version 2.2.4 in March 2009.

The 2.2.*x* series vastly improved support for the ActiveX and Component Object Model (COM) interface, and Object Linking and Embedding (OLE), though bugs were still being found. The delegation to interface using the `implements` keyword was partly implemented, but was not complete as of March 2011. Library support for ActiveX was also improved.

Another major feature was the internal linker for Win32, Win64, and Windows CE, which greatly improved linking time and memory use, and make the compile-link-run cycle in Lazarus much faster. The efficiency for smart-linking, or dead code elimination, was also improved.

Minor new features included improved DWARF (2/3) debug format support, and optimizations such as tail recursion, omission of unneeded stack frames and register-based common subexpression elimination (CSE) optimization. A first implementation of generic programming (generics) support also became available, but only experimentally.

### Version 2.4.x

The 2.4.x release series had a less clear set of goals than earlier releases. The unit system rewrite was postponed again, and the branch that became 2.4 was created to keep risky commits from 2.2 to stabilize it. Mostly these risky commits were more involved improvements to the new platforms, Mac PowerPC 64, Mac x86-64, iPhone, and many fixes to the ARM and x86-64 architectures in general, as well as DWARF.

Other compiler improvements included whole program optimization (WPO) and devirtualization and ARM embedded-application binary interface (EABI) support.

Later, during the 2.2 cycle, a more Delphi-like resource support (based on special sections in the binary instead of Pascal constants) was added. This feature, direly needed by Lazarus, became the main highlight of the branch.

Other more minor additions were a memory manager that improved heap manager performance in threaded environments, small improvements in Delphi compatibility such as `OleVariant`, and improvements in interface delegation.

On January 1, 2010, Free Pascal 2.4.0 was released, followed on November 13, 2010, by bug fix release 2.4.2, with support for `for..in` loops, `sealed` and `abstract` classes, and other changes.

### Version 2.6.x

In January 2012, Free Pascal 2.6 was released. This first version from the 2.6 release series also supported Objective Pascal on OS X and iOS targets and implemented many small improvements and bug fixes. In February 2013, FPC 2.6.2 was released. It contained NetBSD and OpenBSD releases for the first time since 1.0.10, based on fresh ports. In March 2014, the last point release in the 2.6 series, 2.6.4, was launched, featuring mostly database (fcl-db) updates.

### Version 3.0.x

Version 3.0.0 was released on November 25, 2015, and was the first major release since January 1, 2012. It introduced many new language features.

Version 3.0.2 was released on February 15, 2017, and includes bug fixes and minor compiler updates. Version 3.0.4 was released on November 28, 2017. It includes many language improvements over previous versions, including an internal linker for Executable and Linkable Format (ELF), Arm AARCH64 for iOS and Linux, a revived i8086 platform, extended libraries and much more.

### Version 3.2.x

The next major release, version 3.2.0, was published on June 19, 2020. It introduced many new language features, including generic routines, standard namespaces, managed records and expanded functionality for dynamic arrays, in addition to the advent of new standard units and the support of additional platforms.

Version 3.2.2 was released on May 20, 2021, and supports macOS on AArch64 and naming of threads. Additionally it includes bug fixes and minor compiler updates.

A release candidate, FPC 3.2.4-rc1, was available for test in June 2025.

### Version 3.3.x

As of July 2025 development version 3.3.1 was available for download as file `fpc.zip`. The most recent member of the archive (excepting a file stating the date the members of `ftp.zip` were extracted) was dated 15 September 2023.

## Targets

Processor architecture

Operating system, device

Version 3.2.2 or 3.3.1 (Trunk)

Version 3.0.0 - 3.2.0

Version 2.6.2

Version 2.6.0

Version 2.4.4

Version 2.4.2

Version 2.4.0

Version 2.2.4

Version 2.0.

x

Version 1.0.

x

i386

DOS (

GO32v2

extender)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FreeBSD

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

OpenBSD

Yes

Yes

Yes

No

No

No

No

No

No

Yes

NetBSD

Yes

Yes

Yes

No

No

No

No

No

No

Yes

Linux

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

macOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

OS/2

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Windows

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Windows CE

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

BeOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Haiku

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

NetWare

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Solaris

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

Yes

iPhone Sim

Yes

Yes

Yes

Yes

No

No

No

No

No

No

QNX Neutrino

Yes

No

No

No

No

No

No

No

No

Yes

Android

Yes

Yes

Yes

No

No

No

No

No

No

No

AROS

Yes

Yes

No

No

No

No

No

No

No

No

x86-64

FreeBSD

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

OpenBSD

Yes

Yes

Yes

Unknown

Unknown

Unknown

Unknown

Unknown

Unknown

Unknown

NetBSD

Yes

Yes

Yes

Unknown

Unknown

Unknown

Unknown

Unknown

Unknown

Unknown

Linux

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unknown

No

macOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

Windows

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

iPhone Sim

Yes

Yes

Yes

Yes

No

No

No

No

No

No

AROS

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

DragonFly BSD

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

Solaris

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

Haiku

Yes

Yes

No

No

No

No

No

No

No

No

Android

Yes

Yes

No

No

No

No

No

No

No

No

ARM

iOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

Game Boy Advance

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

Nintendo DS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

Linux

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unknown

No

Windows CE

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unknown

No

Android

Yes

Yes

Yes

No

No

No

No

No

No

No

Embedded

Yes

Yes

Yes

No

No

No

No

No

No

No

Embedded Rasp-Pi

Yes

Yes

No

No

No

No

No

No

No

No

AROS

Yes

Yes

No

No

No

No

No

No

No

No

AArch64

Linux

Yes

Yes

Yes

No

No

No

No

No

No

No

iOS

Yes

Yes

Yes

No

No

No

No

No

No

No

Android

Yes

Yes

No

No

No

No

No

No

No

No

macOS

Yes

No

No

No

No

No

No

No

No

No

AVR

Embedded

Yes

Yes

No

No

No

No

No

No

No

No

PowerPC

Linux

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

macOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Classic Mac OS

Yes

Yes

Yes

Yes

Yes

No

No

Yes

Yes

No

AmigaOS 4

Yes

Yes

Yes

Yes

Yes

Unknown

Unknown

Unknown

Yes

No

MorphOS

Yes

Yes

Yes

Yes

Yes

Unknown

Unknown

Unknown

Yes

No

AIX

Yes

Yes

Yes

Yes

No

No

No

No

No

No

Wii

Yes

Yes

Yes

Yes

Yes

No

No

No

No

No

PowerPC 64-bit

Linux

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

macOS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

AIX

Yes

Yes

Yes

Yes

No

No

No

No

No

No

SPARC

Solaris

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

NetBSD

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

Embedded

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

Linux

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

SPARC64

Linux

Yes

Yes

Yes

Yes

No

No

No

No

No

No

RISC-V

Embedded

Yes

Yes

No

No

No

No

No

No

No

No

RISC-V64

Embedded

Yes

Yes

No

No

No

No

No

No

No

No

Java virtual machine

Java

Yes

Yes

No

No

No

No

No

No

No

No

Android

Yes

Yes

No

No

No

No

No

No

No

No

MIPS

(BE and LE)

Linux

Yes

Yes

No

No

No

No

No

No

No

No

Embedded

Yes

Yes

No

No

No

No

No

No

No

No

8086

(16-bit)

DOS

Yes

Yes

No

No

No

No

No

No

No

No

Win16

Yes

Yes

No

No

No

No

No

No

No

No

Embedded

Yes

Yes

No

No

No

No

No

No

No

No

m68k

Linux

Yes

Yes

No

No

No

No

No

No

No

Yes

NetBSD

Yes

Yes

No

No

No

No

No

No

No

Yes

AmigaOS

Yes

Yes

No

No

No

No

No

No

No

Yes

Atari TOS

Yes

Yes

No

No

No

No

No

No

No

Yes

limited cross-compiler only

Palm OS

Yes

Yes

No

No

No

No

No

No

No

Unknown

Z80

Embedded

Yes

No

No

No

No

No

No

No

No

No

ZX Spectrum

Yes

No

No

No

No

No

No

No

No

No

MSX-DOS

Yes

No

No

No

No

No

No

No

No

No

WebAssembly

Web browsers

Yes

No

No

No

No

No

No

No

No

No

Free Pascal also supports byte code generation for the Java Virtual Machine as of version 3.0.0 and targets both Oracle's Java and Google's Android JVM, although Object Pascal syntax is not fully supported. Free Pascal 3.0.0 also supports ARMHF platforms like the Raspberry Pi, including ARMV6-EABIHF running on Raspbian. Work on 64-bit ARM has resulted in support for iOS in 3.0.0 as well. A native ARM Android target has been added, ending the formerly hacked ARM Linux target to generate native ARM libraries for Android. This makes porting Lazarus applications to Android (using Custom Drawn Interface) easier. Since FPC 2.6.2, OpenBSD and NetBSD are supported on IA32 and X86_64 architectures. A new target *embedded* has been added for usage without OS (ARM Cortex M and MIPS mainly). With InstantFPC it is possible to run Pascal programs, which are translated just in time, as Unix scripts or CGI back-end.

Ultibo core is an embedded or bare metal development environment for Raspberry Pi. Ultibo is based on Free Pascal and developed under a modified version of Lazarus. The IDE is PC based but has been ported to Linux and Mac as well. Ultibo is an OS-less runtime and has support for most functions and allows the programmer full control over the hardware via the RTL units. The runtime implements multi-threaded, pre-emptive multitasking. The programmer can put threads on a specific CPU or let the runtime divide the load automatically or a mix of the two. Most Raspberry Pi models are supported including the A, B, A+ and B+ as well as the Raspberry Pi 2B, 3B, 4B/400/CM4 and Zero.

## Integrated development environments

Like most modern compilers, Free Pascal can be used with an integrated development environment (IDE). Besides independent IDEs there are also plugins to various existing IDEs

- Lazarus is the most popular IDE used by Free Pascal programmers. It looks and feels similar to the Delphi IDE, and can be used to create console and graphical applications, Windows services, daemons, and web applications. Lazarus provides a cross-platform user interface framework, called Lazarus Component Library (LCL). Graphical applications created with LCL can be ported to another platform via recompiling or cross compiling.

- MSEide+MSEgui is a visual programming environment using the Free Pascal compiler. It consists of the MSEgui visual component library and the MSEide form and source code editor. Unlike, for example, the Lazarus project, MSE does not focus on compatibility with the Delphi VCL, which in some cases simplifies development and reduces complexity. It features a built-in debugger, syntax highlighting, class field completion, code navigation, a report generator, and more.

- Free Pascal has its own text-mode IDE resembling Turbo Pascal's IDE. It is made using the Free Vision framework (also included with Free Pascal), a Turbo Vision clone. In addition to many features of the Turbo Pascal IDE, it has code completion and support for multiple help file formats (HTML, Microsoft Compiled HTML Help (CHM), Information Presentation Facility (IPF). Instead of using command line tools, the IDE uses its own embedded compiler, based on the same source as the command line compiler and debugger (using libgdb or GDBMI) to provide its functionality.

- Dev-Pascal is a free Windows-only IDE for Free Pascal and GNU Pascal, with no further development following the 2004 FPC version and the 2005 GPC version.

## Bundled libraries

Apart from a compiler and an IDE, Free Pascal provides the following libraries:

- Free Pascal Runtime Library (RTL): Basic low-level runtime library for general programming tasks
- Free Component Library (FCL): High-level software component library for general programming tasks

## Examples of software produced with Free Pascal

- Beyond Compare is a data comparison utility for Windows, OS X, and Linux. The Linux and OS X versions are compiled with Lazarus/FPC.
- Cartes du Ciel is a free planetarium program for Linux, OS X, and Windows. It maps and labels most constellations, planets, and objects visible by telescope. It was fully written in Lazarus/FPC, and released under GPL.
- Cheat Engine is a proprietary, source available, Freeware memory scanner, hex editor, and debugger. It can be used for cheating in computer games. Since version 6.0 it is compiled with Lazarus/FPC.
- Double Commander is an open-source multi-platform two-panel orthodox file manager inspired by the Microsoft Windows-only Total Commander.
- Free Pascal is written in Object Pascal and assembly language, and self-compiled.
- HNSKY, Hallo Northern Sky is a free planetarium program for Windows and Linux. Since version 3.4.0 written & compiled with Lazarus/FPC.
- Lazarus: Free Pascal's affiliated Delphi-like software package for rapid development of graphical applications.
- Morfik: Morfik WebOS AppBuilder uses Free Pascal to produce CGI binaries.
- MyNotex is a free software note-taking and notes manager for Linux.
- Early versions of the Nim compiler were developed in Free Pascal, before it became self-hosting in Nim.
- PeaZip is an open source archiver, made with Lazarus/FPC.
- TorChat, previously written in Python, is now being rewritten in Free Pascal and Lazarus.

---
title: "Modula-2"
source: https://en.wikipedia.org/wiki/Modula-2
domain: modula-2
license: CC-BY-SA-4.0
tags: modula language, niklaus wirth, modular programming, pascal language, structured programming
fetched: 2026-07-02
---

# Modula-2

**Modula-2** is a structured, procedural programming language developed between 1977 and 1985/8 by Niklaus Wirth at ETH Zurich. It was created as the language for the operating system and application software of the Lilith personal workstation. It was later used for programming outside the context of the Lilith.

Wirth viewed Modula-2 as a successor to his earlier programming languages Pascal and Modula. The main concepts are:

1. The module as a compiling unit for separate compiling
2. The coroutine as the basic building block for concurrent processes
3. Types and procedures that allow access to machine-specific data

The language design was influenced by the Mesa language and the Xerox Alto, both from Xerox PARC, that Wirth saw during his 1976 sabbatical year there. The computer magazine *Byte* devoted the August 1984 issue to the language and its surrounding environment.

Wirth created the Oberon series of languages as the successor to Modula-2, while others (particularly at Digital Equipment Corporation and Acorn Computers, later Olivetti) developed Modula-2 into Modula-2+ and later Modula-3.

## Description

Modula-2 is a general purpose procedural language suitable for both systems programming and applications programming. The syntax is based on Wirth's earlier language, Pascal, with some elements and syntactic ambiguities removed. The *module* concept, designed to support separate compilation and data abstraction; and direct language support for multiprogramming were added.

The language allows the use of one-pass compilers. Such a compiler by Gutknecht and Wirth was about four times faster than earlier multi-pass compilers.

Here is an example of the source code for the "Hello world" program:

```mw
MODULE Hello;
(* For GNU Modula-2 this would be
FROM StrIO IMPORT WriteString *)
FROM STextIO IMPORT WriteString;
BEGIN
  WriteString("Hello World!")
END Hello.
```

A Modula-2 *module* may be used to encapsulate a set of related subprograms and data structures, and restrict their visibility from other parts of the program. Modula-2 programs are composed of modules, each of which is made up of two parts: a *definition module*, the interface portion, which contains only those parts of the subsystem that are *exported* (visible to other modules), and an *implementation module*, which contains the working code that is internal to the module.

The language has strict scope control. Except for standard identifiers, no object from the outside is visible inside a module unless explicitly imported; no internal module object is visible from the outside unless explicitly exported.

Suppose module M1 exports objects a, b, c, and P by enumerating its identifiers in an explicit export list

```mw
  DEFINITION MODULE M1;
    EXPORT QUALIFIED a, b, c, P;
    ...
```

Then the objects a, b, c, and P from module M1 are known outside module M1 as M1.a, M1.b, M1.c, and M1.P. They are exported in a *qualified* manner to the outside (assuming module M1 is global). The exporting module's name, i.e. M1, is used as a qualifier followed by the object's name.

Suppose module M2 contains the following IMPORT declaration

```mw
  MODULE M2;
    IMPORT M1;
    ...
```

Then this means that the objects exported by module M1 to the outside of its enclosing program can now be used inside module M2. They are referenced in a *qualified* manner: M1.a, M1.b, M1.c, and M1.P. Example:

```mw
    ...
    M1.a := 0;
    M1.c := M1.P(M1.a + M1.b);
    ...
```

Qualified export avoids name clashes. For example, if another module M3 exports an object called P, then the two objects can be distinguished since M1.P differs from M3.P. It does not matter that both objects are called P inside their exporting modules M1 and M3.

An alternative method exists. Suppose module M4 is formulated as this:

```mw
  MODULE M4;
    FROM M1 IMPORT a, b, c, P;
```

This means that objects exported by module M1 to the outside can again be used inside module M4, but now by mere references to the exported identifiers in an *unqualified* manner as: a, b, c, and P. Example:

```mw
    ...
    a := 0;
    c := P(a + b);
    ...
```

This method of import is usable if there are no name clashes. It allows variables and other objects to be used outside their exporting module in the same *unqualified* manner as inside the exporting module.

The export and import rules not only safeguard objects against unwanted access, but also allow a cross-reference of the definition of every identifier in a program to be created. This property helps with the maintenance of large programs containing many modules.

The language provides for single-processor concurrency (monitors, coroutines and explicit transfer of control) and for hardware access (absolute addresses, bit manipulation, and interrupts). It uses a nominal type system.

## Dialects

There are two major dialects of Modula-2. The first is *PIM*, named for the book *Programming in Modula-2* by Niklaus Wirth. There were three major editions of PIM: the second, third (corrected), and fourth. Each describes slight variants of the language. The second major dialect is *ISO*, named for the standardization effort by the International Organization for Standardization. Here are a few of the differences among them.

- *PIM2* (1983)
  - Required explicit `EXPORT` clause in definition modules.
  - Function `SIZE` needs to be imported from module `SYSTEM`
- *PIM3* (1985)
  - Removed the `EXPORT` clause from definition modules following the observation that everything within a definition module defines the interface to that module, hence the `EXPORT` clause was redundant.
  - Function `SIZE` is pervasive (visible in any scope without import)
- *PIM4* (1988)
  - Specified the behaviour of the `MOD` operator when the operands are negative.
  - Required all `ARRAY OF CHAR` strings to be terminated by ASCII NUL, even if the string fits exactly into its array.
- *ISO* (1996, 1998)
  - ISO Modula-2 resolved most of the ambiguities in PIM Modula-2. It added the data types `COMPLEX` and `LONGCOMPLEX`, exceptions, module termination (`FINALLY` clause) and a complete standard input/output (I/O) library. There are many minor differences and clarifications.

## Supersets

There are several supersets of Modula-2 with language extensions for specific application domains:

- **PIM supersets**
  - Canterbury Modula-2, extended with Oberon-like extensible records [This has been withdrawn and is no longer available anywhere]
  - Modula-2+, extended with preemptive threads, exceptions, and garbage collection
  - Modula-2*, parallel extension
  - Modula-P, another parallel extension
  - Modula–Prolog, adds a Prolog layer
  - Modula/R, adds relational database extensions
  - Modula-GM, adds embedded system extensions
- **ISO supersets**
  - ISO10514-2, adds an object-oriented programming layer
  - ISO10514-3, adds a generic programming (generics) layer
- **IEC supersets**
  - Mod51, extended with IEC 1131 constructs for embedded development

## Derivatives

There are several derivative languages that resemble Modula-2 very closely but are new languages in their own right. Most are different languages with different purposes and with strengths and weaknesses of their own:

- Modula-3, developed by a team of ex-Xerox employees who had moved to DEC and Olivetti
- Oberon, developed at ETH Zurich Zürich for System Oberon available online.
- Oberon-2, Oberon with object-oriented (OO) extensions
- Active Oberon, another OO Oberon extension, developed at ETH Zurich with the main goal to support parallel computing programming on multiprocessing and multi-core processors
- Parallaxis, a language for machine-independent data-parallel programming
- Umbriel, developed by Pat Terry as a teaching language
- YAFL, a research language by Darius Blasband

Many other current programming languages have adopted features of Modula-2.

## Language elements

### Reserved words

PIM [2,3,4] defines 40 reserved words:

```
AND         ELSIF           LOOP       REPEAT
ARRAY       END             MOD        RETURN
BEGIN       EXIT            MODULE     SET
BY          EXPORT          NOT        THEN
CASE        FOR             OF         TO
CONST       FROM            OR         TYPE
DEFINITION  IF              POINTER    UNTIL
DIV         IMPLEMENTATION  PROCEDURE  VAR
DO          IMPORT          QUALIFIED  WHILE
ELSE        IN              RECORD     WITH
```

### Built-in identifiers

PIM [3,4] defines 29 built-in identifiers:

```
ABS         EXCL            LONGINT    REAL
BITSET      FALSE           LONGREAL   SIZE
BOOLEAN     FLOAT           MAX        TRUE
CAP         HALT            MIN        TRUNC
CARDINAL    HIGH            NIL        VAL
CHAR        INC             ODD
CHR         INCL            ORD
DEC         INTEGER         PROC
```

## Embedded system use

Modula-2 is used to program many embedded systems.

### Cambridge Modula-2

Cambridge Modula-2 by Cambridge Microprocessor Systems is based on a subset of PIM4 with language extensions for embedded development. The compiler runs on MS-DOS and it generates code for Motorola 68000 series (M68k) based embedded microcontrollers running a MINOS operating system.

### Mod51

Mod51 by Mandeno Granville Electronics is based on ISO Modula-2 with language extensions for embedded development following IEC 1131, an industry standard for programmable logic controllers (PLC) closely related to Modula-2. The Mod51 compiler generates standalone code for 80C51 based microcontrollers.

### Modula-GM

Delco Electronics, then a subsidiary of GM Hughes Electronics, developed a version of Modula-2 for embedded control systems starting in 1985. Delco named it Modula-GM. It was the first high-level programming language used to replace machine code (language) for embedded systems in Delco's *engine control units* (ECUs). This was significant because Delco was producing over 28,000 ECUs per day in 1988 for GM. This was then the world's largest producer of ECUs. The first experimental use of Modula-GM in an embedded controller was in the 1985 Antilock Braking System Controller which was based on the Motorola 68xxx microprocessor, and in 1993 Gen-4 ECU used by the Champ Car World Series Championship Auto Racing Teams (CART) and Indy Racing League (IRL) teams. The first production use of Modula-GM was its use in GM trucks starting with the 1990 model year *vehicle control module* (VCM) used to manage GM Powertrain's Vortec engines. Modula-GM was also used on all ECUs for GM's 90° Buick V6 engine family 3800 Series II used in the 1997-2005 model year Buick Park Avenue. The Modula-GM compilers and associated software management tools were sourced by Delco from Intermetrics.

Modula-2 was selected as the basis for Delco's high level language because of its many strengths over other alternative language choices in 1986. After Delco Electronics was spun off from GM (with other component divisions) to form Delphi Automotive Systems in 1995, global sourcing required that a non-proprietary high-level software language be used. ECU embedded software now developed at Delphi is compiled with commercial compilers for the language C.

### Russian radionavigation satellites

The satellites of the Russian radionavigation-satellite service framework GLONASS, similar to the United States Global Positioning System (GPS), are programmed in Modula-2.

## Compilers

- Amsterdam Compiler Kit (ACK) Modula-2 – for MINIX; freeware
- ADW Modula-2 – for Windows, ISO compliant, ISO/IEC 10514-1, ISO/IEC 10514-2 (OO extension), ISO/IEC 10514-3 (Generic extension); freeware
- Aglet Modula-2 – for AmigaOS 4.0 for PowerPC; freeware
- Fitted Software Tools (FST) Modula-2 – for DOS; freeware
- Gardens Point Modula-2 (GPM) – for BSD, Linux, OS/2, Solaris; ISO compliant; freeware, as of 30 July 2014
- Gardens Point Modula-2 (GPM/CLR) – for .NET Framework; freeware
- GNU Modula-2 – for GCC platforms (in 2023 with version 13 it was officially merged into the main GCC repository), version 1.0 released 11 December 2010; version 15.1 released on 25 April 2025; compliance: PIM2, PIM3, PIM4, ISO/IEC 10514-1; free software, GNU General Public License (GPL)
- Logitech - they also had a "Real Time Kernel" for embedded usage (1987)
- M2Amiga – for Amiga; free software
- M2M – by N. Wirth and collaborators from ETH Zurich, cross-platform, generates M-code for virtual machine; freeware
- M2RT11 – by N. Wirth and collaborators from ETH Zurich, originally created for bootstrapping the Lilith
- MacMETH – by N. Wirth and collaborators from ETH Zurich for Macintosh, Classic only; freeware
- Mod51 – for the Intel 80x51 microcontroller family, ISO compliant, IEC1132 extensions; proprietary software
- Megamax Modula-2 – for Atari ST with documentation; freeware
- Modula-2 R10 – reference compiler for this Modula; open-source, peer review
- ModulaWare – for OpenVMS (VAX and Alpha), ISO compliant; proprietary software
- ORCA/Modula-2 – for Apple IIGS by The Byte Works for the Apple Programmer's Workshop
- p1 Modula-2 – for Macintosh, Classic and macOS (PowerPC and Carbon (API) only), ISO compliant; proprietary software
- MOCKA – for various platforms, PIM compliant; commercial, freeware Linux/BSD versions
- TDI Modula-2 – for Atari ST, by TDI Software
- Terra M2VMS – for OpenVMS (VAX and Alpha), PIM compliant; proprietary software
- m2c, Ulm Modula-2 System – for Solaris (Sun SPARC and Motorola 68k); free software, GNU General Public License (GPL)
- XDS – ISO compliant, TopSpeed compatible library: *Native XDS-x86* for x86 (Windows and Linux); *XDS-C* for Windows and Linux (16- and 32-bit versions), targets C (K&R & ANSI); freeware

### Turbo Modula-2

Turbo Modula-2 was a compiler and an integrated development environment for MS-DOS developed, but not published, by Borland. Jensen and Partners, which included Borland cofounder Niels Jensen, bought the unreleased codebase and turned it into TopSpeed Modula-2. It was eventually sold to Clarion, now SoftVelocity, who then offered the Modula-2 compiler as part of its Clarion product line at that time.

A Zilog Z80 CP/M version of Turbo Modula-2 was briefly marketed by Echelon under license from Borland. A companion release for Hitachi HD64180 was sold by Micromint as a development tool for their SB-180 single-board computer.

### IBM Modula-2

IBM had a Modula-2 compiler for internal use which ran on both OS/2 and AIX, and had first class support in IBM's E2 editor. IBM Modula-2 was used for parts of the OS/400 *Vertical Licensed Internal Code* (effectively the kernel of OS/400). This code was mostly replaced with C++ when OS/400 was ported to the IBM RS64 processor family, although some remains in modern releases of the operating system. A Motorola 68000 backend also existed, which may have been used in embedded systems products.

## Operating systems

Modula-2 is used to program some operating systems (OSs). The Modula-2 module structure and support are used directly in two related OSs.

The OS named *Medos-2*, for the Lilith workstation, was developed at ETH Zurich, by Svend Erik Knudsen with advice from Wirth. It is a single user, object-oriented operating system built from Modula-2 modules.

The OS named *Excelsior*, for the Kronos workstation, was developed by the Academy of Sciences of the Soviet Union, Siberian branch, Novosibirsk Computing Center, Modular Asynchronous Developable Systems (MARS) project, Kronos Research Group (KRG). It is a single user system based on Modula-2 modules.

## Books

- *Gleaves, Richard (1984). *Modula-2 for Pascal Programmers*. Springer Books on Professional Computing (1st ed.). Switzerland: Springer Nature. doi:10.1007/978-1-4613-8531-8. ISBN 978-0-387-96051-7. S2CID 346624.*
- *King, K. N. (1 January 1988). *Modula-2: A Complete Guide*. Burlington, Massachusetts: Jones and Bartlett Publishers. ISBN 978-0669110913.*
- *Wirth, Niklaus (1988). *Programming in Modula-2* (4th ed.). Berlin Heidelberg: Springer-Verlag. doi:10.1007/978-3-642-83565-0. ISBN 978-0-387-96051-7. S2CID 41899609.*
- *Cooper, Doug (1 September 1990). *Oh My! Modula-2: An Introduction to Programming*. New York City, New York: W. W. Norton & Company. ISBN 978-0393960099.*
- *Helman, Paul (1 March 1998). *Walls and Mirrors: Intermediate Problem Solving and Data Structures: Modula, 2 (Benjamin/Cummings Series in Structured Programming)*. Benjamin-Cummings. ISBN 978-0805389456.*
- *Sutcliffe, Richard J. (2004–2005). *Modula-2: Abstractions for Data and Programming Structures*. Arjay Books. ISBN 978-0-669-11091-3.* Uses ISO-standard Modula-2.

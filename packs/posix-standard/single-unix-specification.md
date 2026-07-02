---
title: "Single UNIX Specification"
source: https://en.wikipedia.org/wiki/Single_UNIX_Specification
domain: posix-standard
license: CC-BY-SA-4.0
tags: posix, single unix specification, posix library, filesystem hierarchy standard
fetched: 2026-07-02
---

# Single UNIX Specification

The **Single UNIX Specification** (**SUS**) is a standard for computer operating systems, compliance with which is required to qualify for using the "UNIX" trademark. The standard specifies programming interfaces for the C language, a command-line shell, and user commands. The core specifications of the SUS known as *Base Specifications* are developed and maintained by the Austin Group, which is a joint working group of IEEE, ISO/IEC JTC 1/SC 22/WG 15 and The Open Group. If an operating system is submitted to The Open Group for certification and passes conformance tests, then it is deemed to be compliant with a UNIX standard such as UNIX 98 or UNIX 03.

Very few BSD and Linux-based operating systems are submitted for compliance with the Single UNIX Specification, although system developers generally aim for compliance with POSIX standards, which form the core of the Single UNIX Specification.

The latest SUS consists of two parts: the *base specifications* technically identical to POSIX, and the X/Open Curses specification.

Some parts of the SUS are optional.

## History

### 1980s: Motivation

The SUS emerged from multiple 1980s efforts to standardize operating system interfaces for software designed for variants of the Unix operating system. The need for standardization arose because enterprises using computers wanted to be able to develop programs that could be used on the computer systems of different manufacturers without reimplementing the programs. Unix was selected as the basis for a standard system interface partly because it was manufacturer-neutral.

In 1984, the UNIX user group called /usr/group published the results of their standardization effort for programming interfaces in their 1984 /usr/group standard, which became basis for what would become the POSIX.1-1988 standard.

In 1985, AT&T published System V Interface Definition (SVID), a specification of UNIX System V programming interfaces.

### 1988: POSIX

In 1988, standardization efforts resulted in **IEEE 1003** (also registered as **ISO/IEC 9945**), or **POSIX.1-1988**, which loosely stands for **Portable Operating System Interface**.

### 1980s and 1990s: X/Open Portability Guide

The X/Open Portability Guide (XPG) was a precursor to the SUS, published by the X/Open Company, a consortium of companies established in 1984. The guides were published in the following years.

- XPG1: X/Open Portability Guide Issue 1: 1985
- XPG2: X/Open Portability Guide Issue 2: 1987
- XPG3: X/Open Portability Guide Issue 3: 1989
- XPG4: X/Open Portability Guide Issue 4: 1992

XPG4 Base included the following documents:

- System Interface Definitions, Issue 4, ISBN 1-872630-46-4
- System Interfaces and Headers, Issue 4, ISBN 1-872630-47-2
- Commands and Utilities, Issue 4, ISBN 1-872630-48-0

### 1990s: Spec 1170

In the early 1990s, a separate effort known as the Common API Specification or Spec 1170 was initiated by several major vendors, who formed the COSE alliance in the wake of the Unix wars. In 1993, Spec 1170 was assigned by COSE to X/Open for fasttrack. In October 1993, a planned transfer of UNIX trademark from Novell to X/Open was announced; it was finalized in 2nd quarter of 1994. Spec 1170 would eventually become the Single Unix Specification.

### 1994: Single UNIX Specification

In 1994, the X/Open Company released the **Single UNIX Specification**. The SUS was made up of documents that were part of the X/Open Common Applications Environment (CAE):

- System Interface Definitions, Issue 4, Version 2
- System Interfaces and Headers, Issue 4, Version 2
- Commands and Utilities, Issue 4, Version 2
- Networking Services, Issue 4

This was a repackaging of the X/Open Portability Guide (XPG), Issue 4, Version 2.

Sources differ on whether X/Open Curses, Issue 4, Version 2 was part of this SUS; its copyright date is given as 1996. X/Open Curses, Issue 4 was published in 1995.

In October 1994, X/Open indicated they were going to refer to Spec 1170 as '"Single-Unix" specification'.

The SUS was at the core of the UNIX 95 brand.

This version had 1168 programming interfaces.

This version of SUS was drawn from the following sources:

- XPG4 Base by X/Open
- System V Interface Definition, (SVID) Edition 3, Level 1 calls by AT&T
- Application Environment Specification (AES) by the Open Software Foundation (OSF)
- Interfaces found in common use and not yet covered by a formal specification, drawn from a survey of major applications.

### 1997: Single UNIX Specification, version 2

In 1996, X/Open merged with Open Software Foundation (OSF) to form The Open Group.

In 1997, the Open Group released the **Single UNIX Specification, Version 2**.

This specification consisted of:

- System Interface Definitions, Issue 5,
- System Interfaces and Headers, Issue 5,
- Commands and Utilities, Issue 5,
- Networking Services, Issue 5,
- X/Open Curses, Issue 4, Version 2,

and was at the core of the UNIX 98 brand.

This version had 1434 programming interfaces.

### 2001: Single UNIX Specification, version 3, POSIX.1-2001

Beginning in 1998, a joint working group of IEEE, ISO JTC 1 SC22 and The Open Group known as the Austin Group began to develop the combined standard that would be known as the core of **Single UNIX Specification, Version 3** and as POSIX.1-2001. It was released on January 30, 2002.

This SUS consisted of:

- Base Specifications, Issue 6
  - Base Definitions, Issue 6
  - System Interfaces, Issue 6
  - Shell and Utilities, Issue 6
  - Rationale (Informative)
- X/Open Curses, Issue 4, Version 2

and is at the core of the UNIX 03 brand.

The Base Specifications are technically identical to **POSIX.1-2001**, which is IEEE Std 1003.1-2001.

This version had 1742 programming interfaces.

An authorized guide is available for the version.

#### 2004 Edition

In 2004, a new edition of the POSIX.1-2001 standard was released, incorporating two technical corrigenda. It is called IEEE Std 1003.1, 2004 Edition. Some informally call it POSIX.1-2004, but this is not an official identification.

### 2008: Single UNIX Specification, version 4, POSIX.1-2008

In December 2008, the Austin Group published a new major revision of SUS and POSIX. This is the Single UNIX Specification, Version 4 (SUSv4).

This SUS consists of:

- Base Specifications, Issue 7
  - Base Definitions, Issue 7
  - System Interfaces, Issue 7
  - Shell and Utilities, Issue 7
  - Rationale, Issue 7, (Informative)
- X/Open Curses, Issue 7

The Base Specifications are technically identical to **POSIX.1-2008**, which is IEEE Std 1003.1-2008.

This version had 1833 interfaces, of which 1191 were in the System Interfaces section.

#### 2013 Edition

Technical Corrigendum 1 mostly targeted internationalization, and also introduced a role-based access model. A trademark *UNIX V7* (not to be confused with V7 UNIX, the version of Research Unix from 1979) was created to mark compliance with SUS Version 4.

#### 2016 Edition

Technical Corrigendum 2 was published in September 2016, leading into *IEEE Std 1003.1-2008, 2016 Edition* and *Single UNIX Specification, Version 4, 2016 Edition*.

#### 2018 Edition, POSIX.1-2017

In January 2018, an "administrative rollup" edition was released. It incorporates Single UNIX Specification version 4 TC1 and TC2, and is technically identical to the 2016 edition.

The Base Specifications are technically identical to **POSIX.1-2017**, which is IEEE Std 1003.1-2017.

## Specification

SUSv3 totals some 3700 pages, which are divided into four main parts:

- **Base Definitions (XBD)** – a list of definitions and conventions used in the specifications and a list of C header files which must be provided by compliant systems. 84 header files in total are provided.
- **Shell and Utilities (XCU)** – a list of utilities and a description of the shell, sh. 160 utilities in total are specified.
- **System Interfaces (XSH)** – contains the specification of various functions which are implemented as system calls or library functions. 1123 system interfaces in total are specified.
- **Rationale (XRAT)** – the explanation behind the standard.

The standard user command line and scripting interface is the POSIX shell, an extension of the Bourne Shell based on an early version of the Korn Shell. Other user-level programs, services and utilities include awk, echo, ed, vi, and hundreds of others. Required program-level services include basic I/O (file, terminal, and network) services. A test suite accompanies the standard. It is called **PCTS** or the **POSIX Certification Test Suite**.

Additionally, SUS includes CURSES (XCURSES) specification, which specifies 372 functions and 3 header files. All in all, SUSv3 specifies 1742 interfaces.

Note that a system need not include source code derived in any way from AT&T Unix to meet the specification. For instance, IBM OS/390, now z/OS, qualifies as UNIX despite having no code in common.

## Marks for compliant systems

There are five official marks for conforming systems:

- UNIX 93
- UNIX 95 – the mark for systems conforming to version 1 of the SUS
- UNIX 98 – the mark for systems conforming to version 2 of the SUS
- UNIX 03 – the mark for systems conforming to version 3 of the SUS
- UNIX V7 – the mark for systems conforming to version 4 of the SUS (including Corrigenda)

## Compliance

Only AIX and macOS have UNIX 03 or later certifications. z/OS is mainly a non-UNIX OS, still current, but on old UNIX certification. Other products are discontinued, on pre-UNIX 03 certifications, or have let their certifications lapse.

### Currently registered UNIX systems

| Product | Vendor | Architecture | UNIX V7 | UNIX 03 | UNIX 98 | UNIX 95 | UNIX 93 |
|---|---|---|---|---|---|---|---|
| AIX | IBM Corporation | POWER processors | Yes | Yes | No | No | No |
| HP-UX | Hewlett Packard Enterprise | IA-64 | No | Yes | No | No | No |
| macOS | Apple | x86-64, ARM64 | No | Yes | No | No | No |
| OpenServer | Xinuos | IA-32 | No | No | No | No | Yes |
| UnixWare | Xinuos | IA-32 | No | No | No | Yes | No |
| z/OS | IBM Corporation | z/Architecture | No | No | No | Yes | No |

#### AIX

AIX version 7, at either 7.1 TL5 (or later) or 7.2 TL2 (or later) are registered as UNIX 03 compliant. AIX version 7, at 7.2 TL5 (or later) are registered as UNIX V7 compliant. Older versions were previously certified to the UNIX 95 and UNIX 98 marks.

#### HP-UX

HP-UX 11i V3 Release B.11.31 remains registered as UNIX 03 compliant on HPE Integrity Servers despite the end of support for HP-UX by HPE. Previous releases were registered as UNIX 95.

#### macOS

Apple macOS (formerly known as Mac OS X and OS X) is registered as UNIX 03 compliant. The first version registered was Mac OS X 10.5 Leopard, certified on October 26, 2007 (on x86 systems).

All versions of macOS from Mac OS X Leopard to macOS 10.15 Catalina, except for OS X Lion, have been registered on Intel-based systems, and all versions from macOS 11 Big Sur, the successor to macOS Catalina, up to macOS 26 Tahoe have been registered on both x86-64 and ARM64 systems.

#### UnixWare

UnixWare 7.1.3 and later is registered as UNIX 95 compliant.

#### OpenServer

OpenServer 5 and 6 are registered as UNIX 93 compliant.

#### z/OS

IBM z/OS 1.2 and higher is registered as UNIX 95 compliant. z/OS 1.9, released on September 28, 2007, and subsequent releases "better align" with UNIX 03.

### Previously registered UNIX systems

#### EulerOS

EulerOS 2.0 for the x86-64 architecture was registered as UNIX 03 compliant. The UNIX 03 conformance statement shows that the standard C compiler is from the GNU Compiler Collection (gcc), and that the system is a Linux distribution of the Red Hat Enterprise Linux family. The UNIX 03 certification expired in September 2022 and has not been renewed.

#### FTX

Stratus Technologies DNCP Series servers running FTX Release 3 were registered as UNIX 93 compliant.

#### Inspur K-UX

Inspur K-UX 2.0 and 3.0 for the x86-64 architecture were certified as UNIX 03 compliant. The UNIX 03 conformance statement for Inspur K-UX 2.0 and 3.0 shows that the standard C compiler is from the GNU Compiler Collection (gcc), and that the system is a Linux distribution of the Red Hat family.

#### IRIX

SGI IRIX 6.5 was registered as UNIX 95 compliant.

#### OS/390

IBM OS/390 was registered as UNIX 95 compliant beginning with the V2R4 release.

#### Reliant UNIX

The last Reliant UNIX versions were registered as UNIX 95 compliant (XPG4 hard branding).

#### Solaris

Solaris 11.4 was previously registered as UNIX v7 compliant in 2018. Solaris 11 and Solaris 10 were registered as UNIX 03 compliant on 32-bit and 64-bit x86 (X86-64) and SPARC systems. Solaris 8 and 9 were registered as UNIX 98 compliant on 32-bit x86 and SPARC systems; 64-bit x86 systems were not supported. Solaris 2.4 and 2.6, on both x86 and SPARC, were certified to the UNIX 93 and UNIX 95 marks respectively.

Solaris 2.5.1 was also registered as UNIX 95 compliant on the PReP PowerPC platform in 1996, but the product was withdrawn before more than a few dozen copies had been sold.

#### Tru64 UNIX

Tru64 UNIX V5.1A and later were registered as UNIX 98 compliant.

#### Other

Other operating systems previously registered as UNIX 95 or UNIX 93 compliant:

- NCR UNIX SVR4
- NEC UX/4800

### Non-registered Unix-like systems

Developers and vendors of Unix-like operating systems such as Linux, FreeBSD, and MINIX typically do not certify their distributions and do not install full POSIX utilities by default.

For Linux, the pax command is usually not installed; furthermore, the pax command packages available for Linux often lack the pax file format support required by POSIX. Sometimes, SUS compliance can be improved by installing additional packages, but very few Linux systems can be configured to be completely conformant. The Linux Standard Base was formed in 2001 as an attempt to standardize the internal structures of Linux-based systems for increased compatibility. It is based on the POSIX specifications, the Single UNIX Specification, and other open standards, and also extends them in several areas; but there are some conflicts between the LSB and the POSIX standards. Few Linux distributions actually go through certification as LSB compliant.

Darwin, the open source subset of macOS, has behavior that can be set to comply with UNIX 03. Darwin uses a 4.4BSD-derived pax command, which lacks multibyte support for filenames.

FreeBSD previously had a "C99 and POSIX Conformance Project" which aimed for compliance with a subset of the Single UNIX Specification, and documentation where there were differences. The FreeBSD pax command, derived from 4.4BSD, does not fully support the pax file format. pax and ustar in-archive format use the same with slightly different defaults (5120 block size vs 10240 block size); however, FreeBSD's pax lacks the extended PAX headers used for extended character set support. FreeBSD man pages sometimes indicate deviations from POSIX and thus SUS in their STANDARDS sections.

OpenBSD man pages sometimes indicate deviations from POSIX and thus SUS in their STANDARDS sections.

MINIX pax command does not support the pax file format and thereby fails POSIX.1-2001.

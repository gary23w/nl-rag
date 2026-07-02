---
title: "POSIX"
source: https://en.wikipedia.org/wiki/POSIX
domain: nuttx-rtos
license: CC-BY-SA-4.0
tags: nuttx rtos, apache nuttx, posix embedded, px4 flight stack
fetched: 2026-07-02
---

# POSIX

The **Portable Operating System Interface** (**POSIX**; IPA: /ˈpɒz.ɪks/) is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems. In order to define a level of compatibility, POSIX specifies many aspects of functionality that can be classified as application programming interface (API), command-line shell, and shell commands. Originally derived from commonly-found Unix APIs, shells, and commands (partly because Unix was considered manufacturer-neutral), today many systems conform to the standard – including branded Unix systems, Unix-like systems, and many systems that were historically unrelated to Unix.

The standardized user command line and scripting interface were based on the UNIX System V Bourne shell. Many user-level programs, services, and utilities (including awk, echo, ed) were also standardized, based on UNIX System V versions of them, along with required program-level services (including basic I/O: file, terminal, and network). POSIX also defines a standard threading library API which is supported by most modern operating systems.

The POSIX standard is developed by the Austin Group (a joint working group among the IEEE, The Open Group, and the ISO/IEC JTC 1/SC 22/WG 15).

POSIX is intended to be used by both application and system developers.

## Name

The standards emerged from a project that began in 1984 building on work from related activity in the */usr/group* association. Richard Stallman suggested the name *POSIX* to the IEEE instead of the former *IEEE-IX*. The committee found it more easily pronounceable and memorable, and thus adopted it.

Originally, POSIX referred to IEEE Std 1003.1-1988, released in 1988. The family of POSIX standards is formally designated as **IEEE 1003** and the ISO/IEC standard number is ISO/IEC 9945.

POSIX is a trademark of the IEEE.

## Versions

POSIX originally consisted of a single document for core services but over time additional documents were published to extend and revise the specification. Before 1997, POSIX comprised multiple documents that were published over the course of several years. After 1997, the Austin Group produces specifications titled Single UNIX Specification (SUS). Over time, the group publishes versions of this specification and later POSIX is amended per some or all of a SUS version. A SUS version consists of a collection of volumes – each for a grouping of required behavior – plus other information (outside of a volume). Each volume is assigned an issue number that is the same for each volume of a version, but is not the same value as the version. For example, SUS version 3 (SUSv3) includes volumes labeled issue 6.

As of 2014, POSIX documentation is divided into two parts:

- POSIX.1, 2013 Edition: POSIX Base Definitions, System Interfaces, and Commands and Utilities (which include POSIX.1, extensions for POSIX.1, Real-time Services, Threads Interface, Real-time Extensions, Security Interface, Network File Access and Network Process-to-Process Communications, User Portability Extensions, Corrections and Extensions, Protection and Control Utilities and Batch System Utilities. This is POSIX 1003.1-2008 with Technical Corrigendum 1.)
- POSIX Conformance Testing: A test suite for POSIX accompanies the standard: **VSX-PCTS** or the **VSX POSIX Conformance Test Suite**.

### Before 1997

#### POSIX.1

*Core Services* (IEEE Std 1003.1-1988) incorporates standard ANSI C and includes:

**Process Creation and Control**

**Signals**

**Floating Point Exceptions**

**Segmentation / Memory Violations**

**Illegal Instructions**

**Bus Errors**

**Timers**

**File and Directory Operations**

**Pipes**

**C Library (Standard C)**

**The POSIX terminal interface**

#### POSIX.1b

*Real-time extensions* (IEEE Std 1003.1b-1993, later appearing as librt—the Realtime Extensions library) includes:

**Priority Scheduling**

**Real-Time Signals**

**Clocks and Timers**

**Semaphores**

**Message Passing**

**Shared Memory**

**Asynchronous and Synchronous I/O**

**Memory Locking Interface**

#### POSIX.1c

*Threads extensions* (IEEE Std 1003.1c-1995) includes:

**Thread Creation, Control, and Cleanup**

**Thread Scheduling**

**Thread Synchronization**

**Signal Handling**

#### POSIX.2

*Shell and Utilities* (IEEE Std 1003.2-1992) includes:

**Command Interpreter**

**Utility Programs**

### POSIX.1-2001

*POSIX.1-2001* (IEEE Std 1003.1-2001) consists of most of SUSv3 which consists of volumes (issue 6): *Base Definitions*, *System Interfaces and Headers*, and *Commands and Utilities*. The POSIX specification specifically excludes the SUSv3 requirements for a curses API (often called *X/Open Curses*, even though there is no distinct grouping of this in SUSv3).

IEEE Std 1003.1-2004 modifies POSIX.1-2001 via two minor updates or errata referred to as technical corrigenda documents.

### POSIX.1-2008

Similar to its predecessor, POSIX.1-2008 (*IEEE Std 1003.1-2008*, 2016 Edition) consists of most of the normative material of SUSv4 (issue 7 of volumes *Base Definitions*, *System Interfaces and Headers*, *Commands and Utilities*). SUSv4 also includes rationale information that largely applies to POSIX although not included per se.

### POSIX.1-2017

POSIX.1-2017 (*IEEE Std 1003.1-2017*) revises the previous version (POSIX.1-2008) via two technical corrigenda.

### POSIX.1-2024

POSIX.1-2024 (*IEEE Std 1003.1-2024*) was published on 14 June 2024.

As of POSIX 2024, the standard is aligned with the C17 language standard.

## Controversies

### 512- vs 1024-byte blocks

POSIX mandates 512-byte default block sizes for the df and du utilities, reflecting the typical size of blocks on disks. When Richard Stallman and the GNU team were implementing POSIX for the GNU operating system, they objected to this on the grounds that most people think in terms of 1024 byte (or 1 KiB) blocks. The environment variable POSIX_ME_HARDER was introduced to allow the user to force the standards-compliant behaviour. The variable name was later changed to POSIXLY_CORRECT. As of 2025, this variable is also used for a number of other behaviour quirks.

## Conformance

An operating system can be classified depending upon the degree of conformance with a POSIX standard.

### Certified

Current versions of the following operating systems have been certified to conform to one or more of the various POSIX standards. This means that they passed the automated conformance tests and their certification has not expired and the operating system has not been discontinued.

- AIX
- INTEGRITY
- macOS (from Mac OS X Leopard to macOS Tahoe)
- OpenServer
- UnixWare
- VxWorks
- z/OS

### Formerly certified

Some versions of the following operating systems had been certified to conform to one or more of the various POSIX standards. This means that they passed the automated conformance tests. The certification has expired and some of the operating systems have been discontinued.

- EulerOS (exp. 2022)
- Inspur K-UX (exp. 2019)
- IRIX (defunct 2006)
- OS/390 (defunct 2004)
- QNX Neutrino
- Solaris (exp. 2019)
- Tru64 (defunct 2010)
- LiteOS (defunct 2020)
- HP-UX (defunct 2026)

### Partially conformant

The following are not certified as POSIX conforming yet are considered partially conforming which is sometimes called *compliant*:

- Android (Available through Android NDK)
- Darwin (core of macOS and iOS)
- DragonFly BSD
- FreeBSD
- Haiku
- illumos
- Linux (most distributions)
- LynxOS
- Minix (since 2005 Minix 3)
- MPE/iX
- NetBSD
- Nucleus RTOS
- NuttX
- OpenBSD
- OpenSolaris
- PikeOS RTOS for embedded systems with optional PSE51 and PSE52 partitions; see partition (mainframe)
- PX5 RTOS
- Redox
- RTEMS – POSIX API support designed to IEEE Std. 1003.13-2003 PSE52
- SerenityOS
- Stratus OpenVOS
- SkyOS (discontinued)
- Syllable (discontinued)
- ULTRIX
- VSTa
- VMware ESXi
- Xenix
- Zephyr

### Partially conformant via compatibility layer

The following operating systems are not certified as POSIX conformant, but they conform in large part to the standard by implementing POSIX support via a compatibility feature (usually translation libraries, or a layer atop the kernel).

- AmigaOS (through the ixemul library or vbcc_PosixLib)
- eCos – POSIX is part of the standard distribution, and used by many applications. 'external links' section below has more information.
- IBM i (through the PASE compatibility layer)
- MorphOS (through the built-in ixemul library)
- OpenVMS (through optional POSIX package)
- Plan 9 from Bell Labs APE - ANSI/POSIX Environment
- RIOT (through optional POSIX module)
- Symbian OS with PIPS (PIPS Is POSIX on Symbian)
- VAXELN (partial support of 1003.1 and 1003.4 through the VAXELN POSIX runtime library)
- Windows NT kernel when using Windows Services for UNIX 3.5 or Subsystem for UNIX-based Applications. To be POSIX compliant, one must activate optional features of Windows NT and Windows 2000 Server.

### Conformance via subsystem

Some technologies allow an operating system to enjoy a level of conformance to POSIX even though the operating system itself has little or no conformance.

#### For Windows

Although Windows does not conform to POSIX, the following technologies provide a level of compliance.

**Cygwin**

Provides a largely POSIX-compliant development and run-time environment for

Microsoft Windows

.

**MinGW**

A

fork

of Cygwin, provides a less POSIX-compliant development environment and supports compatible

C

-programmed applications via

Msvcrt

, Microsoft's old Visual C

runtime library

.

**libunistd**

A largely POSIX-compliant development library originally created to build the Linux-based C/

C++

source code of

CinePaint

as is in

Microsoft Visual Studio

. A lightweight implementation that has POSIX-compatible header files that map POSIX APIs to call their Windows API counterparts.

**Microsoft POSIX subsystem**

An optional Windows subsystem included in Windows NT-based operating systems up to Windows 2000. It supported POSIX.1 as it stood in the 1990 revision, without

threads

or

sockets

.

**Interix**

originally OpenNT by Softway Systems, Inc., is an upgrade and replacement for

Microsoft POSIX subsystem

that was purchased by

Microsoft

in 1999. It was initially marketed as a stand-alone add-on product and then later included as a component in

Windows Services for UNIX

(SFU) and finally incorporated as a component in

Windows Server 2003 R2

and later Windows OS releases under the name "Subsystem for UNIX-based Applications" (SUA), later made deprecated in 2012 (Windows 8)

and dropped in 2013 (2012 R2, 8.1). It enables full POSIX compliance for certain

Microsoft Windows

products.

**Windows Subsystem for Linux (WSL)**

A compatibility layer for running Linux binary executables natively on Windows 10 and 11 using a Linux image such as Ubuntu, Debian, or OpenSUSE among others, acting as an upgrade and replacement for Windows Services for UNIX. It was released in beta in April 2016. The first distribution available was Ubuntu.

**UWIN**

From AT&T Research implements a POSIX layer on top of the Win32 APIs.

**MKS Toolkit**

Originally created for MS-DOS, is a software package produced and maintained by

MKS Inc.

that provides a

Unix-like

environment for scripting, connectivity and porting

Unix

and

Linux

software to both 32- and 64-bit

Microsoft Windows

systems. A subset of it was included in the first release of

Windows Services for UNIX

(SFU) in 1998.

**Windows C Runtime Library and Windows Sockets API**

Implement commonly used POSIX API functions for file, time, environment, and socket access,

although the support remains largely incomplete and not fully interoperable with POSIX-compliant implementations.

#### For OS/2

POSIX environments for OS/2:

**emx+gcc**

Largely POSIX compliant.

#### For DOS

POSIX environments for DOS include:

**emx+gcc**

Largely POSIX compliant

**DJGPP**

Partially POSIX compliant

**DR-DOS**

Multitasking core via

EMM386

/MULTI

– a POSIX threads frontend API extension is available

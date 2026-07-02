---
title: "Core dump"
source: https://en.wikipedia.org/wiki/Core_dump
domain: memory-forensics-volatility
license: CC-BY-SA-4.0
tags: memory forensics volatility, volatile memory acquisition, process memory dump analysis, core dump inspection, digital evidence recovery
fetched: 2026-07-02
---

# Core dump

In computing, a **core dump**, **memory dump**, **crash dump**, **storage dump**, **system dump**, or **ABEND dump** consists of the recorded state of the working memory of a computer program at a specific time, generally when the program has crashed or otherwise terminated abnormally. In practice, other key pieces of program state are usually dumped at the same time, including the processor registers, which may include the program counter and stack pointer, memory management information, and other processor and operating system flags and information. A **snapshot dump** (or **snap dump**) is a memory dump requested by the computer operator or by the running program, after which the program is able to continue. Core dumps are often used to assist in diagnosing and debugging errors in computer programs.

On many operating systems, a fatal exception in a program automatically triggers a core dump. By extension, the phrase "to dump core" has come to mean in many cases, any fatal error, regardless of whether a record of the program memory exists. The term "core dump", "memory dump", or just "dump" has also become jargon to indicate any output of a large amount of raw data for further examination or other purposes.

## Background

The name comes from magnetic-core memory, the principal form of random-access memory from the 1950s to the 1970s. The name has remained long after magnetic-core technology became obsolete.

Earliest core dumps were paper printouts of the contents of memory, typically arranged in columns of octal or hexadecimal numbers (a "hex dump"), sometimes accompanied by their interpretations as machine language instructions, text strings, or decimal or floating-point numbers (*cf.* disassembler).

As memory sizes increased and post-mortem analysis utilities were developed, dumps were written to magnetic media like tape or disk.

Instead of only displaying the contents of the applicable memory, modern operating systems typically generate a file containing an image of the memory belonging to the crashed process, or the memory images of parts of the address space related to that process, along with other information such as the values of processor registers, program counter, system flags, and other information useful in determining the root cause of the crash. These files can be viewed as text, printed, or analysed with specialised tools such as elfdump on Unix and Unix-like systems, objdump and kdump on Linux, IPCS (Interactive Problem Control System) on IBM z/OS, DVF (Dump Viewing Facility) on IBM z/VM, WinDbg on Microsoft Windows, Valgrind, or other debuggers.

In some operating systems an application or operator may request a snapshot of selected storage blocks, rather than all of the storage used by the application or operating system.

## Uses

Core dumps can serve as useful debugging aids in several situations. On early standalone or batch-processing systems, core dumps allowed a user to debug a program without monopolizing the (very expensive) computing facility for debugging; a printout could also be more convenient than debugging using front panel switches and lights.

On shared computers, whether time-sharing, batch processing, or server systems, core dumps allow off-line debugging of the operating system, so that the system can go back into operation immediately.

Core dumps allow a user to save a crash for later or off-site analysis, or comparison with other crashes. For embedded computers, it may be impractical to support debugging on the computer itself, so analysis of a dump may take place on a different computer. Some operating systems such as early versions of Unix did not support attaching debuggers to running processes, so core dumps were necessary to run a debugger on a process's memory contents.

Core dumps can be used to capture data freed during dynamic memory allocation and may thus be used to retrieve information from a program that is no longer running. In the absence of an interactive debugger, the core dump may be used by an assiduous programmer to determine the error from direct examination.

Snap dumps are sometimes a convenient way for applications to record quick and dirty debugging output.

## Analysis

A core dump generally represents the complete contents of the dumped regions of the address space of the dumped process. Depending on the operating system, the dump may contain few or no data structures to aid interpretation of the memory regions. In these systems, successful interpretation requires that the program or user trying to interpret the dump understands the structure of the program's memory use.

A debugger can use a symbol table, if one exists, to help the programmer interpret dumps, identifying variables symbolically and displaying source code; if the symbol table is not available, less interpretation of the dump is possible, but there might still be enough possible to determine the cause of the problem. There are also special-purpose tools called dump analyzers to analyze dumps. One popular tool, available on many operating systems, is the GNU binutils' objdump.

On modern Unix-like operating systems, administrators and programmers can read core dump files using the GNU Binutils Binary File Descriptor library (BFD), and the GNU Debugger (gdb) and objdump that use this library. This library will supply the raw data for a given address in a memory region from a core dump; it does not know anything about variables or data structures in that memory region, so the application using the library to read the core dump will have to determine the addresses of variables and determine the layout of data structures itself, for example by using the symbol table for the program undergoing debugging.

Analysts of crash dumps from Linux systems can use kdump or the Linux Kernel Crash Dump (LKCD).

Core dumps can save the context (state) of a process at a given state for returning to it later. Systems can be made highly available by transferring core between processors, sometimes via core dump files themselves.

Core can also be dumped onto a remote host over a network (which is a security risk).

OS/360 introduced the service aid IMDPRDMP to print stand-alone and SVC dumps. This program formats several system control blocks in addition to printing storage areas in hexadecimal and EBCDIC. The OS/VS1 and OS/VS2 versions are called HMDPRDMP and AMDPRDMP.

Interactive Problem Control System (IPCS) is a full screen dump reader that IBM introduced for OS/VS2 (MVS), DOS/VSE and VM/370. The MVS version performs functions similar to AMDPRDMP, and uses compatible control block descriptions for formatting. IBM eventually dropped AMDPRDMP in favor of IPCS. IPCS on MVS supports scripts in CLIST and REXX.

Users of IBM mainframes running z/OS can browse both SVC and transaction dumps using IPCS, which supports user written scripts in REXX and supports point-and-shoot browsing of dumps.

## Core-dump files

### Format

In older and simpler operating systems, each process had a contiguous address-space, so a dump file was sometimes simply a file with the sequence of bytes, digits, characters or words. On other systems a dump file contained discrete records, each containing a storage address and the associated contents. On the earliest of these machines, the dump was often written by a stand-alone dump program rather than by the application or the operating system.

The IBSYS monitor for the IBM 7090 included a System Core-Storage Dump Program that supported post-mortem and snap dumps.

On the IBM System/360, the standard operating systems wrote formatted ABEND and SNAP dumps, with the addresses, registers, storage contents, etc., all converted into printable forms. Later releases added the ability to write unformatted dumps, called at that time core image dumps (also known as SVC dumps.)

In modern operating systems, a process address space may contain gaps, and it may share pages with other processes or files, so more elaborate representations are used; they may also include other information about the state of the program at the time of the dump.

In Unix-like systems, core dumps generally use the standard executable image-format:

- a.out in older versions of Unix,
- ELF in modern Linux, System V, Solaris, and BSD systems,
- Mach-O in macOS, *etc.*

### Naming

#### OS/360 and successors

In OS/360 and successors, a job may assign arbitrary data set names (dsnames) to the ddnames `SYSABEND` and `SYSUDUMP` for a formatted ABEND dump and to arbitrary ddnames for SNAP dumps, or define those ddnames as SYSOUT. The Damage Assessment and Repair (DAR) facility added an automatic unformatted storage dump to the dataset `SYS1.DUMP` at the time of failure as well as a console dump requested by the operator. A job may assign an arbitrary dsname to the ddname `SYSMDUMP` for an unformatted ABEND dump, or define that ddname as SYSOUT. The newer transaction dump is very similar to the older SVC dump. The *Interactive Problem Control System* (IPCS), added to OS/VS2 by *Selectable Unit* (SU) 57 and part of every subsequent MVS release, can be used to interactively analyze storage dumps on DASD. IPCS understands the format and relationships of system control blocks, and can produce a formatted display for analysis. The current versions of IPCS allow inspection of active address spaces without first taking a storage dump and of unformaated dumps on SPOOL.

#### Unix-like

Since Solaris 8, system utility `coreadm` allows the name and location of core files to be configured. Dumps of user processes are traditionally created as `core`. On Linux (since versions 2.4.21 and 2.6 of the Linux kernel mainline), a different name can be specified via procfs using the `/proc/sys/kernel/core_pattern` configuration file; the specified name can also be a template that contains tags substituted by, for example, the executable filename, the process ID, or the reason for the dump. System-wide dumps on modern Unix-like systems often appear as `vmcore` or `vmcore.incomplete`.

#### Others

Systems such as Microsoft Windows, which use filename extensions, may use extension `.dmp`; for example, core dumps may be named `memory.dmp` or `\Minidump\Mini051509-01.dmp`.

### Windows memory dumps

Microsoft Windows supports two memory dump formats, described below.

#### Kernel-mode dumps

There are five types of kernel-mode dumps:

- Complete memory dump – contains full physical memory for the target system.
- Kernel memory dump – contains all the memory in use by the kernel at the time of the crash.
- Small memory dump – contains various info such as the stop code, parameters, list of loaded device drivers, etc.
- Automatic memory dump (Windows 8 and later) – same as Kernel memory dump, but if the paging file is both System Managed and too small to capture the Kernel memory dump, it will automatically increase the paging file to at least the size of RAM for four weeks, then reduce it to the smaller size.
- Active memory dump (Windows 10 and later) – contains most of the memory in use by the kernel and user mode applications.

To analyze the Windows kernel-mode dumps Debugging Tools for Windows are used, a set that includes tools like WinDbg & DumpChk.

#### User-mode memory dumps

User-mode memory dump, also known as *minidump*, is a memory dump of a single process. It contains selected data records: full or partial (filtered) process memory; list of the threads with their call stacks and state (such as registers or TEB); information about handles to the kernel objects; list of loaded and unloaded libraries. Full list of options available in `MINIDUMP_TYPE` enum.

## Space missions

The NASA Voyager program was probably the first craft to routinely utilize the core dump feature in the Deep Space segment. The core dump feature is a mandatory telemetry feature for the Deep Space segment as it has been proven to minimize system diagnostic costs. The Voyager craft uses routine core dumps to spot memory damage from cosmic ray events.

Space Mission core dump systems are mostly based on existing toolkits for the target CPU or subsystem. However, over the duration of a mission the core dump subsystem may be substantially modified or enhanced for the specific needs of the mission.

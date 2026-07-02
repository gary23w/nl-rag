---
title: "Memory debugger"
source: https://en.wikipedia.org/wiki/Memory_debugger
domain: gdb-debugging
license: CC-BY-SA-4.0
tags: gdb, gdb debugging, gdb debugger, gdb breakpoint, core dump
fetched: 2026-07-02
---

# Memory debugger

A **memory debugger** is a debugger for finding software memory problems such as memory leaks and buffer overflows. These are due to bugs related to the allocation and deallocation of dynamic memory. Programs written in languages that have garbage collection, such as managed code, might also need memory debuggers, e.g. for memory leaks due to "living" references in collections.

## Overview

Memory debuggers work by monitoring memory access, allocations, and deallocation of memory. Many memory debuggers require applications to be recompiled with special dynamic memory allocation libraries, whose APIs are mostly compatible with conventional dynamic memory allocation libraries, or else use dynamic linking. Electric Fence is such a debugger which debugs memory allocation with malloc. Some memory debuggers (e.g. Valgrind) work by running the executable in a virtual machine-like environment, monitoring memory access, allocation and deallocation so that no recompilation with special memory allocation libraries is required.

Finding memory issues such as leaks can be extremely time-consuming as they may not manifest themselves except under certain conditions. Using a tool to detect memory misuse makes the process much faster and easier.

As abnormally high memory utilization can be a contributing factor in software aging, memory debuggers can help programmers to avoid software anomalies that would exhaust the computer system memory, thus ensuring high reliability of the software even for long runtimes.

## Comparison to static analyzer

Some static analysis tools can also help find memory errors. Memory debuggers operate as part of an application while its running while static code analysis is performed by analyzing the code without executing it. These different techniques will typically find different instances of problems, and using them both together yields the best result.

## List of memory debugging tools

This is a list of tools useful for memory debugging. A profiler can be used in conjunction with a memory debugger.

| Name | OS | License | Languages | Technique |
|---|---|---|---|---|
| AddressSanitizer | Linux, Mac OS | Free/open source (LLVM) | C, C++, Rust | Compile-time instrumentation (available in Clang and GCC) and specialized library |
| Allinea DDT | Linux, Blue Gene | Proprietary commercial | C, C++ and F90. Also for parallel programs on supercomputers | Runtime - through dynamic linking |
| AQtime | Windows (Visual Studio, Embarcadero IDEs) | Proprietary commercial | .NET, C++, Java, Silverlight, JScript, VBScript | Runtime |
| Bcheck | Solaris |   |   |   |
| BoundsChecker | Windows (Visual Studio) | Proprietary commercial | C++ | Runtime intercepts or compile-time |
| Daikon | Unix, Windows, Mac OS X | Free/open source | Java, C/C++, Perl, and Eiffel | Runtime dynamic invariant detection |
| Debug_new | (general technique) | (general technique) | C++ | Compile-time override |
| Deleaker | Windows (standalone, and plugins for Visual Studio, RAD Studio, Qt Creator, CLion) | Proprietary commercial | C++, .Net, Delphi | Runtime intercepts |
| dmalloc | Any | Free/open source (ISC License) | C | Compile-time override |
| DynamoRIO § Dr. Memory | Android, Linux, Windows | Free/open source (LGPL and BSD) | Any | Runtime intercepts |
| Electric Fence | Unix | GNU GPL | C, C++ | Compile-time override |
| FASTMM4 | Windows | GNU GPL | Delphi | Compile-time override |
| IBM Rational Purify | Unix, Windows | Proprietary commercial | C++, Java, .NET | Runtime |
| Insure++ | Windows (Visual Studio plugin), Unix | Proprietary commercial | C, C++ | source code instrumentation |
| Intel Inspector | Windows (Visual Studio), Linux | Proprietary commercial | C, C++, Fortran | Runtime |
| libcwd | Linux (gcc) | Free/open source | C, C++ | Compile-time override |
| libumem | Solaris | Bundled with Solaris |   | Link-time override |
| Memwatch | Any (programming library) | Free/open source | C | Compile-time override |
| mtrace | Various | GNU LGPL | GNU C library | Built-in, outputs accesses |
| MTuner | Various | Free | C, C++ | Runtime intercepts, Link-time override (MSVC, Clang and GCC), Leak detection |
| Oracle Solaris Studio (formerly Sun Studio Runtime Checking) | Linux, Solaris | Proprietary freeware | C, C++, Fortran |   |
| OLIVER (APT international) | MVS, MVS/EXA, DOS/VSE | Proprietary software | IBM Assembler | Runtime intercepts, Hypervisor - Type 2 |
| TotalView | Unix, Mac OS X | Proprietary commercial | C, C++, Fortran | Runtime |
| Valgrind § Memcheck | Linux, FreeBSD, Solaris/illumos, Mac OS, Android | GNU GPL | Any | Runtime intercepts |
| WinDbg | Windows | Proprietary freeware | C, C++, .NET, Python | Runtime |

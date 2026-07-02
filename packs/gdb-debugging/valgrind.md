---
title: "Valgrind"
source: https://en.wikipedia.org/wiki/Valgrind
domain: gdb-debugging
license: CC-BY-SA-4.0
tags: gdb, gdb debugging, gdb debugger, gdb breakpoint, core dump
fetched: 2026-07-02
---

# Valgrind

**Valgrind** (/ˈvælɡrɪnd/) is a programming tool for memory debugging, memory leak detection, and profiling.

Valgrind was originally designed to be a freely licensed memory debugging tool for Linux on x86, but has since evolved to become a generic framework for creating dynamic analysis tools such as checkers and profilers.

## Overview

Valgrind is in essence a virtual machine using just-in-time compilation techniques, including dynamic recompilation. Nothing from the original program ever gets run directly on the host processor. Instead, Valgrind first translates the program into a temporary, simpler form called intermediate representation (IR), which is a processor-neutral, static single assignment form-based form. After the conversion, a tool (see below) is free to do whatever transformations it would like on the IR, before Valgrind translates the IR back into machine code and lets the host processor run it. Valgrind recompiles binary code to run on host and target (or simulated) CPUs of the same architecture. It also includes a GDB stub to allow debugging of the target program as it runs in Valgrind, with "monitor commands" that allow querying the Valgrind tool for various information.

A considerable amount of performance is lost in these transformations (and usually, the code the tool inserts); usually, code run with Valgrind and the "none" tool (which does nothing to the IR) runs at 20% to 25% of the speed of the normal program.

## Tools

### Memcheck

There are multiple tools included with Valgrind (and several external ones). The default (and most used) tool is *Memcheck*. Memcheck inserts extra instrumentation code around almost all instructions, which keeps track of the *validity* (all unallocated memory starts as invalid or "undefined", until it is initialized into a deterministic state, possibly from other memory) and *addressability* (whether the memory address in question points to an allocated, non-freed memory block), stored in the so-called *V bits* and *A bits* respectively. As data is moved around or manipulated, the instrumentation code keeps track of the A and V bits, so they are always correct on a single-bit level.

In addition, Memcheck replaces the standard C++ allocators and C memory allocator with its own implementation, which also includes *memory guards* around all allocated blocks (with the A bits set to "invalid"). This feature enables Memcheck to detect off-by-one errors where a program reads or writes outside an allocated block by a small amount. The problems Memcheck can detect and warn about include the following:

- Reading uninitialized memory
- Reading/writing invalid memory which may be
  - memory that has been `free`'d
  - memory outside of `malloc`'d blocks
  - memory below the stack pointer
- Use of incorrect parameters for system calls
- Unsafe overlapping memory copies with `mem*` and `str*` functions
- Memory leaks
- Mismatched allocations and deallocations which may be
  - mixing C and C++ e.g., `malloc` and `delete`
  - mixing scalar and array e.g., `new` and `delete[]`
  - sized deallocation not the same size as allocation
  - aligned deallocation not the same alignment as allocation
- Use of incorrect alignment
- Use of `realloc` with a size of zero

The price of this is lost performance. Programs running under Memcheck usually run 20–30 times slower than running outside Valgrind and use more memory (there is a memory penalty per allocation). Thus, few developers run their code under Memcheck (or any other Valgrind tool) all the time. They most commonly use such tools either to trace down some specific bug, or to verify that there are no latent bugs (of the kind Memcheck can detect) in the code.

### Core errors

Part of the core of Valgrind always has to perform some checking on file descriptors (for instance to prevent the test executable from affecting Valgrind's log file or other output files). Checking can also be done for more general user errors affecting file descriptors. The kinds of errors that are detected are

- closing a file descriptor that is not open
- file descriptors that are not closed when the test executable exits
- use of a file descriptor that was never created or was closed already

Starting with Valgrind 3.24 these errors are handled by Valgrind in the same way as other errors. That means that you can generate and use suppressions with them.

Valgrind 3.25 added a feature where you can change the behaviour of functions that create file descriptors. The default behaviour is the same as POSIX, which will return the lowest available file descriptor, potentially recycling closed file descriptors. There is the risk that the test executable will accidentally and erroneously use such a recycled file descriptor. Valgrind's --modify-fds option changes the behaviour to no longer respect the POSIX standard. Instead it will try to create a new file descriptor for each request.

### Other tools

In addition to Memcheck, Valgrind has several other tools:

- *None*, runs the code in the virtual machine without performing any analysis and thus has the smallest possible CPU and memory overhead of all tools. Since Valgrind itself provides a trace back from a segmentation fault, the *none* tool provides this traceback at minimal overhead.
- *Addrcheck*, similar to Memcheck but with much smaller CPU and memory overhead, thus catching fewer types of bugs. Addrcheck has been removed as of version 3.2.0.
- *Massif*, a heap profiler. The separate GUI massif-visualizer visualizes output from Massif.
- *Helgrind* and *DRD*, detect race conditions in multithreaded code
- *Cachegrind*, a cache profiler. The separate GUI KCacheGrind visualizes output from Cachegrind.
- *Callgrind*, a call graph analyzer created by Josef Weidendorfer, added to Valgrind as of version 3.2.0. KCacheGrind can visualize output from Callgrind.
- *DHAT*, dynamic heap analysis tool which analyzes how much memory is allocated and for how long, as well as patterns of memory usage.
- *exp-bbv*, a performance simulator that extrapolates performance from a small sample set.

*exp-sgcheck* (named *exp-ptrcheck* prior to version 3.7), was removed in version 3.16.0. It was an experimental tool to find stack and global array overrun errors, which Memcheck cannot find.

There are also several externally developed tools available. One such tool is ThreadSanitizer, another detector of race conditions.

## Platforms supported

As of version 3.4.0, Valgrind supports Linux on x86, x86-64 and PowerPC. Support for Linux on ARMv7 (used for example in certain smartphones) was added in version 3.6.0. From version 3.7.0 the ARM/Android platform support was added. Support for Solaris was added in version 3.11.0. Support for OS X was added in version 3.5.0. Support for FreeBSD x86 and amd64 was added in version 3.18.0. Support for FreeBSD aarch64 was added in version 3.23.0.

Since version 3.9.0 there is support for Linux on MIPS64 little and big endian, for MIPS DSP ASE on MIPS32, for s390x Decimal Floating Point instructions, for POWER8 (Power ISA 2.07) instructions, for Intel AVX2 instructions, for Intel Transactional Synchronization Extensions, both RTM and HLE and initial support for Hardware Transactional Memory on POWER.

RISC-V 64bit since version 3.25.0.

Support for macOS 10.13 was improved and support for macOS 10.14, 10.15, 11, 12 and 13 were added in Valgrind 3.27.

There are unofficial ports to other Unix-like platforms (like OpenBSD, NetBSD, DragonFly BSD and QNX).

## History and development

The name Valgrind refers to the main entrance to Valhalla in Norse mythology. During development (before release) the project was named Heimdall; however, the name would have conflicted with a security package.

The original author of Valgrind is Julian Seward, who in 2006 won a Google-O'Reilly Open Source Award for his work on Valgrind.

Several others have also made significant contributions, including Nicholas Nethercote, Bart Van Assche, Florian Krohm, Tom Hughes, Philippe Waroquiers, Mark Wielaard, Paul Floyd, Petar Jovanovic, Carl Love, Petr Pavlu and Ivo Raisr.

It is used by a number of Linux-based projects.

## Limitations of Memcheck

In addition to the performance penalty, an important limitation of Memcheck is its inability to detect all cases of bounds errors in the use of static or stack-allocated data. The following code will pass the *Memcheck* tool in Valgrind without incident, despite containing the errors described in the comments:

```mw
int a[5]; // A global static array of length 5

int main() {
    int b[5]; // A stack array of length 5

    a[5] = 0; // Error - a[0] to a[4] exist, a[5] is out of bounds
    b[5] = 0; // Error - b[0] to b[4] exist, b[5] is out of bounds

    return 0;
}
```

The inability to detect all errors involving the access of stack allocated data is especially noteworthy since certain types of stack errors make software vulnerable to the classic stack smashing exploit.

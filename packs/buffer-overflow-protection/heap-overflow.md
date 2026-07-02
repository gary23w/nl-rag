---
title: "Heap overflow"
source: https://en.wikipedia.org/wiki/Heap_overflow
domain: buffer-overflow-protection
license: CC-BY-SA-4.0
tags: buffer overflow protection, bounds checking defense, out of bounds write mitigation, heap overflow hardening
fetched: 2026-07-02
---

# Heap overflow

A **heap overflow**, **heap overrun**, or **heap smashing** is a type of buffer overflow that occurs in the heap data area. Heap overflows are exploitable in a different manner to that of stack-based overflows. Memory on the heap is dynamically allocated at runtime and typically contains program data. Exploitation is performed by corrupting this data in specific ways to cause the application to overwrite internal structures such as linked list pointers. The canonical heap overflow technique overwrites dynamic memory allocation linkage (such as `malloc` metadata) and uses the resulting pointer exchange to overwrite a program function pointer.

For example, on older versions of Linux, two buffers allocated next to each other on the heap could result in the first buffer overwriting the second buffer's metadata. By setting the in-use bit to zero of the second buffer and setting the length to a small negative value which allows null bytes to be copied, when the program calls `free()` on the first buffer it will attempt to merge these two buffers into a single buffer. When this happens, the buffer that is assumed to be freed will be expected to hold two pointers FD and BK in the first 8 bytes of the formerly allocated buffer. BK gets written into FD and can be used to overwrite a pointer.

## Consequences

An accidental overflow may result in data corruption or unexpected behavior by any process that accesses the affected memory area. On operating systems without memory protection, this could be any process on the system.

For example, a Microsoft JPEG GDI+ buffer overflow vulnerability could allow remote execution of code on the affected machine.

iOS jailbreaking often uses heap overflows to gain arbitrary code execution.

## Detection and prevention

As with buffer overflows there are primarily three ways to protect against heap overflows. Several modern operating systems such as Windows and Linux provide some implementation of all three.

- Prevent execution of the payload by separating the code and data, typically with hardware features such as NX-bit
- Introduce randomization so the heap is not found at a fixed offset, typically with kernel features such as ASLR (Address Space Layout Randomization)
- Introduce sanity checks into the heap manager

Since version 2.3.6 the GNU libc includes protections that can detect heap overflows after the fact, for example by checking pointer consistency when calling `unlink`. However, those protections against prior exploits were almost immediately shown to also be exploitable. In addition, Linux has included support for ASLR since 2005, although PaX introduced a better implementation years before. Also Linux has included support for NX-bit since 2004.

Microsoft has included protections against heap resident buffer overflows since April 2003 in Windows Server 2003 and August 2004 in Windows XP with Service Pack 2. These mitigations were safe unlinking and heap entry header cookies. Later versions of Windows such as Vista, Server 2008 and Windows 7 include: Removal of commonly targeted data structures, heap entry metadata randomization, expanded role of heap header cookie, randomized heap base address, function pointer encoding, termination of heap corruption and algorithm variation. Normal Data Execution Prevention (DEP) and ASLR also help to mitigate this attack.

The most common detection method for heap overflows is online dynamic analysis. This method observes the runtime execution of programs to identify vulnerabilities through the detection of security breaches.

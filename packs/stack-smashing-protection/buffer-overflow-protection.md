---
title: "Buffer overflow protection"
source: https://en.wikipedia.org/wiki/Buffer_overflow_protection
domain: stack-smashing-protection
license: CC-BY-SA-4.0
tags: stack smashing protection, return address integrity, stack guard defense, prologue epilogue canary
fetched: 2026-07-02
---

# Buffer overflow protection

**Buffer overflow protection** is any of various techniques used during software development to enhance the security of executable programs by detecting buffer overflows on stack-allocated variables, and preventing them from causing program misbehavior or from becoming serious security vulnerabilities. A stack buffer overflow occurs when a program writes to a memory address on the program's call stack outside of the intended data structure, which is usually a fixed-length buffer. Stack buffer overflow bugs are caused when a program writes more data to a buffer located on the stack than what is actually allocated for that buffer. This almost always results in corruption of adjacent data on the stack, which could lead to program crashes, incorrect operation, or security issues.

Typically, buffer overflow protection modifies the organization of stack-allocated data so it includes a *canary* value that, when destroyed by a stack buffer overflow, shows that a buffer preceding it in memory has been overflowed. By verifying the canary value, execution of the affected program can be terminated, preventing it from misbehaving or from allowing an attacker to take control over it. Other buffer overflow protection techniques include *bounds checking*, which checks accesses to each allocated block of memory so they cannot go beyond the actually allocated space, and *tagging*, which ensures that memory allocated for storing data cannot contain executable code.

Overfilling a buffer allocated on the stack is more likely to influence program execution than overfilling a buffer on the heap because the stack contains the return addresses for all active function calls. However, similar implementation-specific protections also exist against heap-based overflows.

There are several implementations of buffer overflow protection, including those for the GNU Compiler Collection, LLVM, Microsoft Visual Studio, and other compilers.

## Overview

A stack buffer overflow occurs when a program writes to a memory address on the program's call stack outside of the intended data structure, which is usually a fixed-length buffer. Stack buffer overflow bugs are caused when a program writes more data to a buffer located on the stack than what is actually allocated for that buffer. This almost always results in corruption of adjacent data on the stack, and in cases where the overflow was triggered by mistake, will often cause the program to crash or operate incorrectly. Stack buffer overflow is a type of the more general programming malfunction known as buffer overflow (or buffer overrun). Overfilling a buffer on the stack is more likely to derail program execution than overfilling a buffer on the heap because the stack contains the return addresses for all active function calls.

Stack buffer overflow can be caused deliberately as part of an attack known as stack smashing. If the affected program is running with special privileges, or if it accepts data from untrusted network hosts (for example, a public webserver), then the bug is a potential security vulnerability that allows an attacker to inject executable code into the running program and take control of the process. This is one of the oldest and more reliable methods for attackers to gain unauthorized access to a computer.

Typically, buffer overflow protection modifies the organization of data in the stack frame of a function call to include a "canary" value that, when destroyed, shows that a buffer preceding it in memory has been overflowed. This provides the benefit of preventing an entire class of attacks. According to some researchers, the performance impact of these techniques is negligible.

Stack-smashing protection is unable to protect against certain forms of attack. For example, it cannot protect against buffer overflows in the heap. There is no sane way to alter the layout of data within a structure; structures are expected to be the same between modules, especially with shared libraries. Any data in a structure after a buffer is impossible to protect with canaries; thus, programmers must be very careful about how they organize their variables and use their structures.

## Canaries

*Canaries* or *canary words* or *stack cookies* are known values that are placed between a buffer and control data on the stack to monitor buffer overflows. When the buffer overflows, the first data to be corrupted will usually be the canary, and a failed verification of the canary data will therefore alert of an overflow, which can then be handled, for example, by invalidating the corrupted data. A canary value should not be confused with a sentinel value.

The terminology is a reference to the historic practice of using canaries in coal mines, since they would be affected by toxic gases earlier than the miners, thus providing a biological warning system. Canaries are alternately known as *stack cookies*, which is meant to evoke the image of a "broken cookie" when the value is corrupted.

There are three types of canaries in use: *terminator*, *random*, and *random XOR*. Current versions of StackGuard support all three, while ProPolice supports *terminator* and *random* canaries.

### Terminator canaries

*Terminator canaries* use the observation that most buffer overflow attacks are based on certain string operations which end at string terminators. The reaction to this observation is that the canaries are built of null terminators, CR, LF, and FF. As a result, the attacker must write a null character before writing the return address to avoid altering the canary. This prevents attacks using `strcpy()` and other methods that return upon copying a null character, while the undesirable result is that the canary is known. Even with the protection, an attacker could potentially overwrite the canary with its known value and control information with mismatched values, thus passing the canary check code, which is executed soon before the specific processor's return-from-call instruction.

### Random canaries

*Random canaries* are randomly generated, usually from an entropy-gathering daemon, in order to prevent an attacker from knowing their value. Usually, it is not logically possible or plausible to read the canary for exploiting; the canary is a secure value known only by those who need to know it—the buffer overflow protection code in this case.

Normally, a random canary is generated at program initialization, and stored in a global variable. This variable is usually padded by unmapped pages so that attempting to read it using any kinds of tricks that exploit bugs to read off RAM cause a segmentation fault, terminating the program. It may still be possible to read the canary if the attacker knows where it is or can get the program to read from the stack.

### Random XOR canaries

*Random XOR canaries* are random canaries that are XOR-scrambled using all or part of the control data. In this way, once the canary or the control data is clobbered, the canary value is wrong.

Random XOR canaries have the same vulnerabilities as random canaries, except that the "read from stack" method of getting the canary is a bit more complicated. The attacker must get the canary, the algorithm, and the control data in order to re-generate the original canary needed to spoof the protection.

In addition, random XOR canaries can protect against a certain type of attack involving overflowing a buffer in a structure into a pointer to change the pointer to point at a piece of control data. Because of the XOR encoding, the canary will be wrong if the control data or return value is changed. Because of the pointer, the control data or return value can be changed without overflowing over the canary.

Although these canaries protect the control data from being altered by clobbered pointers, they do not protect any other data or the pointers themselves. Function pointers especially are a problem here, as they can be overflowed into and can execute shellcode when called.

## Bounds checking

Bounds checking is a compiler-based technique that adds run-time bounds information for each allocated block of memory, and checks all pointers against those at run-time. For C and C++, bounds checking can be performed at pointer calculation time or at dereference time.

Implementations of this approach use either a central repository, which describes each allocated block of memory, or fat pointers, which contain both the pointer and additional data, describing the region that they point to.

## Tagging

Tagging is a compiler-based or hardware-based (requiring a tagged architecture) technique for tagging the type of a piece of data in memory, used mainly for type checking. By marking certain areas of memory as non-executable, it effectively prevents memory allocated to store data from containing executable code. Also, certain areas of memory can be marked as non-allocated, preventing buffer overflows.

Historically, tagging has been used for implementing high-level programming languages; with appropriate support from the operating system, tagging can also be used to detect buffer overflows. An example is the NX bit hardware feature, supported by Intel, AMD and ARM processors.

## Implementations

### GNU Compiler Collection (GCC)

Stack-smashing protection was first implemented by *StackGuard* in 1997, and published at the 1998 USENIX Security Symposium. StackGuard was introduced as a set of patches to the Intel x86 backend of GCC 2.7. StackGuard was maintained for the Immunix Linux distribution from 1998 to 2003, and was extended with implementations for terminator, random and random XOR canaries. StackGuard was suggested for inclusion in GCC 3.x at the GCC 2003 Summit Proceedings, but this was never achieved.

From 2001 to 2005, IBM developed GCC patches for stack-smashing protection, known as *ProPolice*. It improved on the idea of StackGuard by placing buffers after local pointers and function arguments in the stack frame. This helped avoid the corruption of pointers, preventing access to arbitrary memory locations.

Red Hat engineers identified problems with ProPolice though, and in 2005 re-implemented stack-smashing protection for inclusion in GCC 4.1. This work introduced the -fstack-protector flag, which protects only some vulnerable functions, and the -fstack-protector-all flag, which protects all functions whether they need it or not.

In 2012, Google engineers implemented the -fstack-protector-strong flag to strike a better balance between security and performance. This flag protects more kinds of vulnerable functions than -fstack-protector does, but not every function, providing better performance than -fstack-protector-all. It is available in GCC since its version 4.9.

All Fedora packages are compiled with -fstack-protector since Fedora Core 5, and -fstack-protector-strong since Fedora 20. Most packages in Ubuntu are compiled with -fstack-protector since 6.10. Every Arch Linux package is compiled with -fstack-protector since 2011. All Arch Linux packages built since 4 May 2014 use -fstack-protector-strong. Stack protection is only used for some packages in Debian, and only for the FreeBSD base system since 8.0. Stack protection is standard in certain operating systems, including OpenBSD, Hardened Gentoo and DragonFly BSD.

StackGuard and ProPolice cannot protect against overflows in automatically allocated structures that overflow into function pointers. ProPolice at least will rearrange the allocation order to get such structures allocated before function pointers. A separate mechanism for pointer protection was proposed in PointGuard and is available on Microsoft Windows.

### Microsoft Visual Studio

The compiler suite from Microsoft implements buffer overflow protection since version 2003 through the /GS command-line switch, which is enabled by default since version 2005. Using /GS- disables the protection.

### IBM Compiler

Stack-smashing protection can be turned on by the compiler flag `-qstackprotect`.

### Clang/LLVM

Clang supports the same -fstack-protector options as GCC and a stronger "safe stack" (-fsanitize=safe-stack) system with similarly low performance impact. Clang also has three buffer overflow detectors, namely AddressSanitizer (`-fsanitize=address`), UBSan (`-fsanitize=bounds`), and the unofficial SafeCode (last updated for LLVM 3.0).

These systems have different tradeoffs in terms of performance penalty, memory overhead, and classes of detected bugs. Stack protection is standard in certain operating systems, including OpenBSD.

### Intel Compiler

Intel's C and C++ compiler supports stack-smashing protection with options similar to those provided by GCC and Microsoft Visual Studio.

### Fail-Safe C

*Fail-Safe C* is an open-source memory-safe ANSI C compiler that performs bounds checking based on fat pointers and object-oriented memory access.

### StackGhost (hardware-based)

Invented by Mike Frantzen, StackGhost is a simple tweak to the register window spill–fill routines which makes buffer overflows much more difficult to exploit. It uses a unique hardware feature of the Sun Microsystems SPARC architecture—deferred, on-stack, in-frame register-window spill and fill—to transparently detect modifications of return pointers (a common way for an exploit to hijack execution paths), automatically protecting all applications without requiring their executable or source-code files to be modified for that. The performance impact is negligible: less than one percent. The resulting gdb issues were resolved by Mark Kettenis two years later, allowing enabling of the feature. Following this event, the StackGhost code was integrated (and optimized) into the SPARC version of the OpenBSD operating system.

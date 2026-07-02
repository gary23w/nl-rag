---
title: "W^X - Wikipedia"
source: https://en.wikipedia.org/wiki/W%5EX
domain: data-execution-prevention
license: CC-BY-SA-4.0
tags: data execution prevention, non executable memory, executable space protection, write xor execute policy, buffer overflow defense
fetched: 2026-07-02
---

# W^X

**W^X** (**write xor execute**, pronounced *W xor X*) is a security policy in operating systems and software frameworks. It implements executable-space protection by ensuring every memory page (a fixed-size block in a program’s virtual address space, the memory layout it uses) is either writable or executable, but not both. Without such protection, a program can write (as data "W") CPU instructions in an area of memory intended for data and then run (as executable "X"; or read-execute "RX") those instructions. This can be dangerous if the writer of the memory is malicious.

The terminology was first introduced in 2003 for Unix-like systems, but is today also used by some multi-platform systems (such as .NET). Other operating systems have adopted similar policies under different names (e.g., DEP in Windows).

On Unix-like operating system kernels, like the Linux kernel or XNU, or those used in as components in larger operating systems like FreeBSD, OpenBSD, Solaris, and the UNIX System Services of Z/OS, W^X is controlled via the mprotect system call. It is relatively simple on processor architectures supporting fine-grained page permissions, such as SPARC, x86-64, PA-RISC, Alpha, and ARM.

The term W^X has also been applied to file system write/execute permissions to mitigate file write vulnerabilities (as with in memory) and attacker persistence. Enforcing restrictions on file permissions can also close gaps in W^X enforcement caused by memory mapped files. Outright forbidding the usage of arbitrary native code can also mitigate kernel and CPU vulnerabilities not exposed via the existing code on the computer. A less intrusive approach is to lock a file for the duration of any mapping into executable memory, which suffices to prevent post-inspection bypasses.

## Compatibility

Some early Intel 64 processors lacked the NX bit required for W^X, but this appeared in later chips. On more limited processors such as the Intel i386, W^X requires using the CS code segment limit as a "line in the sand", a point in the address space above which execution is not permitted and data is located, and below which it is allowed and executable pages are placed. This scheme was used in Exec Shield.

Linker changes are generally required to separate data from code (such as trampolines that are needed for linker and library runtime functions). The switch allowing mixing is usually called `execstack` on Unix-like systems

W^X can also pose a minor problem for just-in-time compilation, which involves an interpreter generating machine code on the fly and then running it. The simple solution used by most, historically including Firefox, involves just making the page executable after the interpreter is done writing machine code, using `VirtualProtect` on Windows or `mprotect` on Unix-like operating systems. The other solution involves mapping the same region of memory to two pages, one with RW and the other with RX. There is no simple consensus on which solution is safer: supporters of the latter approach believe allowing a page that has ever been writable to be executed defeats the point of W^X (there exists an SELinux policy to control such operations called `allow_execmod`) and that address space layout randomization would make it safe to put both pages in the same process. Supporters of the former approach believe that the latter approach is only safe when the two pages are given to two separate processes, and inter-process communication would be costlier than calling `mprotect`.

## History

W^X was first implemented in OpenBSD 3.3, released May 2003. In 2004, Microsoft introduced a similar feature called DEP (Data Execution Prevention) in Windows XP. Similar features are available for other operating systems, including the PaX and Exec Shield patches for Linux, and NetBSD's implementation of PaX. In Red Hat Enterprise Linux (and automatically CentOS) version 5, or by Linux Kernel 2.6.18-8, SELinux received the `allow_execmem`, `allow_execheap`, and `allow_execmod` policies that provide W^X when disabled.

Although W^X (or DEP) has only protected userland programs for most of its existence, in 2012 Microsoft extended it to the Windows kernel on the x86 and ARM architectures. In late 2014 and early 2015, W^X was added in the OpenBSD kernel on the AMD64 architecture. In early 2016, W^X was fully implemented on NetBSD's AMD64 kernel and partially on the i386 kernel.

macOS computers running on Apple silicon processors enforce W^X for all programs. Intel-based Macs enforce the policy only for programs that use the OS's Hardened Runtime mode.

Starting with Firefox 46 in 2016 and ending with Firefox 116 in 2023, Firefox's virtual machine for JavaScript implemented the W^X policy. This was later rolled back on some platforms for performance reasons, though remained in others which enforce W^X for all programs.

.NET uses W^X starting with .NET 6.0 in 2021.

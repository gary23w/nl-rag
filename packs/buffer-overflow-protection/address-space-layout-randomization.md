---
title: "Address space layout randomization"
source: https://en.wikipedia.org/wiki/Address_space_layout_randomization
domain: buffer-overflow-protection
license: CC-BY-SA-4.0
tags: buffer overflow protection, bounds checking defense, out of bounds write mitigation, heap overflow hardening
fetched: 2026-07-02
---

# Address space layout randomization

**Address space layout randomization** (**ASLR**) is a computer security technique involved in preventing exploitation of memory corruption vulnerabilities. In order to prevent an attacker from reliably redirecting code execution to a particular exploited function in memory, ASLR randomly arranges the address space positions of key data areas of a process, including the base of the executable and the positions of the stack, heap and libraries. When applied to the kernel, this technique is called *kernel address space layout randomization* (*KASLR*).

## History

The Linux PaX project first coined the term "ASLR", and published the first design and implementation of ASLR in July 2001 as a patch for the Linux kernel. It is seen as a complete implementation, providing a patch for kernel stack randomization since October 2002.

The first mainstream operating system to support ASLR by default was OpenBSD version 3.4 in 2003, followed by Linux in 2005.

## Benefits

Address space randomization hinders some types of security attacks by making it more difficult for an attacker to predict target addresses. For example, attackers trying to execute return-to-libc attacks must locate the code to be executed, while other attackers trying to execute shellcode injected on the stack have to find the stack first. In both cases, the system makes related memory-addresses unpredictable from the attackers' point of view. These values have to be guessed, and a mistaken guess is not usually recoverable due to the application crashing.

### Effectiveness

Address space layout randomization is based upon the low chance of an attacker guessing the locations of randomly placed areas. Security is increased by increasing the search space. Thus, address space randomization is more effective when more entropy is present in the random offsets. Entropy is increased by either raising the amount of virtual memory area space over which the randomization occurs or reducing the period over which the randomization occurs. The period is typically implemented as small as possible, so most systems must increase VMA space randomization.

To defeat the randomization, attackers must successfully guess the positions of all areas they wish to attack. For data areas such as stack and heap, where custom code or useful data can be loaded, more than one state can be attacked by using NOP slides for code or repeated copies of data. This allows an attack to succeed if the area is randomized to one of a handful of values. In contrast, code areas such as library base and main executable need to be discovered exactly. Often these areas are mixed, for example stack frames are injected onto the stack and a library is returned into.

The following variables can be declared:

- $E_{s}$ (entropy bits of stack top)
- $E_{m}$ (entropy bits of `mmap()` base)
- $E_{x}$ (entropy bits of main executable base)
- $E_{h}$ (entropy bits of heap base)
- $A_{s}$ (attacked bits per attempt of stack entropy)
- $A_{m}$ (attacked bits per attempt of `mmap()` base entropy)
- $A_{x}$ (attacked bits per attempt of main executable entropy)
- $A_{h}$ (attacked bits per attempt of heap base entropy)
- $\alpha$ (attempts made)
- N (total amount of entropy: $N=(E_{s}-A_{s})+(E_{m}-A_{m})+(E_{x}-A_{x})+(E_{h}-A_{h})\,$ )

To calculate the probability of an attacker succeeding, a number of attempts α carried out without being interrupted by a signature-based IPS, law enforcement, or other factor must be assumed; in the case of brute forcing, the daemon cannot be restarted. The number of relevant bits and how many are being attacked in each attempt must also be calculated, leaving however many bits the attacker has to defeat.

The following formulas represent the probability of success for a given set of α attempts on N bits of entropy.

- $g\left(\alpha \,\right)=1-{\left(1-{2^{-N}}\right)^{\alpha }\,}\,{\text{ if }}0\leq \,\alpha \,$ (isolated guessing; address space is re-randomized after each attempt)
- $b\left(\alpha \,\right)={\frac {\alpha \,}{2^{N}}}\,{\text{ if }}0\leq \,\alpha \,\leq \,{2^{N}}$ (systematic brute forcing on copies of the program with the same address space)

In many systems, $2^{N}$ can be in the thousands or millions. On 32-bit systems, a typical amount of entropy *N* is 8 bits. For 2004 computer speeds, Shacham and co-workers state "... 16 bits of address randomization can be defeated by a brute force attack within minutes." (The authors' statement depends on the ability to attack the same application multiple times without any delay. Proper implementations of ASLR, like that included in grsecurity, provide several methods to make such brute force attacks infeasible. One method involves preventing an executable from executing for a configurable amount of time if it has crashed a certain number of times.) On modern 64-bit systems, these numbers typically reach the millions at least.

Android, and possibly other systems, implement *Library Load Order Randomization*, a form of ASLR which randomizes the order in which libraries are loaded. This supplies very little entropy. An approximation of the number of bits of entropy supplied per needed library appears below; this does not yet account for varied library sizes, so the actual entropy gained is really somewhat higher. Attackers usually need only one library; the math is more complex with multiple libraries, and shown below as well. The case of an attacker using only one library is a simplification of the more complex formula for $l=1$ .

- l (number of libraries loaded)
- β (number of libraries used by the attacker)
- $E_{m}={\begin{cases}\log _{2}\left(l\right)&{\text{ if }}\beta \,=1,l\geq \,1\\\sum _{i=l}^{l-\left(\beta \,-1\right)}\log _{2}\left(i\right)&{\text{ if }}\beta \,\geq \,1,l\geq \,1\end{cases}}$

These values tend to be low even for large values of l, most importantly since attackers typically can use only the C standard library and thus one can often assume that $\beta \,=1$ . However, even for a small number of libraries there are a few bits of entropy gained here; it is thus potentially interesting to combine library load order randomization with VMA address randomization to gain a few extra bits of entropy. These extra bits of entropy will not apply to other mmap() segments, only libraries.

#### Reducing entropy

Attackers may make use of several methods to reduce the entropy present in a randomized address space, ranging from simple information leaks to attacking multiple bits of entropy per attack (such as by heap spraying). There is little that can be done about this.

It is possible to leak information about memory layout using format string vulnerabilities. Format string functions such as printf use a variable argument list to do their job; format specifiers describe what the argument list looks like. Because of the way arguments are typically passed, each format specifier moves closer to the top of the stack frame. Eventually, the return pointer and stack frame pointer can be extracted, revealing the address of a vulnerable library and the address of a known stack frame; this can eliminate library and stack randomization as an obstacle to an attacker.

One can also decrease entropy in the stack or heap. The stack typically must be aligned to 16 bytes, and so this is the smallest possible randomization interval; while the heap must be page-aligned, typically 4096 bytes. When attempting an attack, it is possible to align duplicate attacks with these intervals; a NOP slide may be used with shellcode injection, and the string '`/bin/sh`' can be replaced with '`////////bin/sh`' for an arbitrary number of slashes when attempting to return to *system*. The number of bits removed is exactly $\log _{2}\!\left(n\right)$ for n intervals attacked.

Such decreases are limited due to the amount of data in the stack or heap. The stack, for example, is typically limited to 8 MB and grows to much less; this allows for at most 19 bits, although a more conservative estimate would be around 8–10 bits corresponding to 4–16 KB of stack stuffing. The heap on the other hand is limited by the behavior of the memory allocator; in the case of glibc, allocations above 128 KB are created using mmap, limiting attackers to 5 bits of reduction. This is also a limiting factor when brute forcing; although the number of attacks to perform can be reduced, the size of the attacks is increased enough that the behavior could in some circumstances become apparent to intrusion detection systems.

### Limitations

ASLR-protected addresses can be leaked by various side channels, removing mitigation utility. Recent attacks have used information leaked by the CPU branch target predictor buffer (BTB) or memory management unit (MMU) walking page tables. It is not clear if this class of ASLR attack can be mitigated. If they cannot, the benefit of ASLR is reduced or eliminated.

### Empirical analysis

In August 2024 a paper was published with an empirical analysis of major desktop platforms, including Linux, macOS, and Windows, by examining the variability in the placement of memory objects across various processes, threads, and system restarts. The results show that while some systems as of 2024, like Linux distributions, provide robust randomization, others, like Windows and macOS, often fail to adequately randomize key areas like executable code and libraries. Moreover, they found a significant reduction in the entropy of libraries after the Linux 5.18 version and identify correlation paths that an attacker could leverage to reduce exploitation complexity significantly.

## Implementations

Several mainstream, general-purpose operating systems implement ASLR.

### Android

Android 4.0 Ice Cream Sandwich provides address space layout randomization (ASLR) to help protect system and third-party applications from exploits due to memory-management issues. Position-independent executable support was added in Android 4.1. Android 5.0 dropped non-PIE support and requires all dynamically linked binaries to be position independent. Library load ordering randomization was accepted into the Android open-source project on 26 October 2015, and was included in the Android 7.0 release.

### DragonFly BSD

DragonFly BSD has an implementation of ASLR based upon OpenBSD's model, added in 2010. It is off by default, and can be enabled by setting the sysctl vm.randomize_mmap to 1.

### FreeBSD

Support for ASLR appeared in FreeBSD 13.0. It is enabled by default since 13.2.

### iOS (iPhone, iPod touch, iPad)

Apple introduced ASLR in iOS 4.3 (released March 2011).

KASLR was introduced in iOS 6. The randomized kernel base is `0x01000000 + ((1+0xRR) * 0x00200000)`, where `0xRR` is a random byte from SHA1 (random data) generated by iBoot (the 2nd-stage iOS Boot Loader).

### Linux

The Linux kernel enabled a weak form of ASLR by default since the kernel version 2.6.12, released in June 2005. The PaX and Exec Shield patchsets to the Linux kernel provide more complete implementations. The Exec Shield patch for Linux supplies 19 bits of stack entropy on a period of 16 bytes, and 8 bits of mmap base randomization on a period of 1 page of 4096 bytes. This places the stack base in an area 8 MB wide containing 524,288 possible positions, and the mmap base in an area 1 MB wide containing 256 possible positions.

ASLR can be disabled for a specific process by changing its execution domain, using `personality(2)`. A number of sysctl options control the behavior of mainline ASLR. For example, `kernel.randomize_va_space` controls *what* to randomize; the strongest option is 2. `vm.mmap_rnd_bits` controls how many bits to randomize for mmap.

Position-independent executable (PIE) implements a random base address for the main executable binary and has been in place since April 18, 2004. It provides the same address randomness to the main executable as being used for the shared libraries. The PIE feature cannot be used together with the prelink feature for the same executable. The prelink tool implements randomization at prelink time rather than runtime, because by design prelink aims to handle relocating libraries before the dynamic linker has to, which allows the relocation to occur once for many runs of the program. As a result, real address space randomization would defeat the purpose of prelinking.

In 2014, Marco-Gisbert and Ripoll disclosed *offset2lib* technique that weakens Linux ASLR for PIE executables. Linux kernels load PIE executables right after their libraries; as a result, there is a fixed offset between the executable and the library functions. If an attacker finds a way to find the address of a function in the executable, the library addresses are also known. They demonstrated an attack that finds the address in fewer than 400 tries. They proposed a new `randomize_va_space=3` option to randomize the placement of the executable relative to the library, but it is yet to be incorporated into the upstream as of 2024.

The Linux kernel 5.18 released May 2022 reduced the effectiveness of both 32-bit and 64-bit implementations. Linux filesystems call `thp_get_unmapped_area` to respond to a file-backed mmap. With a change in 5.18, files greater than 2 MiB are made to return 2 MiB-aligned addresses, so they can be potentially backed by huge pages. (Previously, the increased alignment only applied to Direct Access (DAX) mappings.) In the meantime, the C library (libc) has, over time, grown in size to exceed this 2 MiB threshold, so instead of being aligned to a (typically) 4 KiB page boundary as before, these libraries are now 2 MiB-aligned: a loss of 9 bits of entropy. For 32-bit Linux, many distributions show no randomization *at all* in the placement of the libc. For 64-bit Linux, the 28 bits of entropy is reduced to 19 bits. In response, Ubuntu has increased its `mmap_rnd_bits` setting. Martin Doucha added a Linux Test Project testcase to detect this issue.

#### Kernel address space layout randomization

Kernel address space layout randomization (KASLR) enables address space randomization for the Linux kernel image by randomizing where the kernel code is placed at boot time. KASLR was merged into the Linux kernel mainline in kernel version 3.14, released on 30 March 2014. When compiled in, it can be disabled at boot time by specifying nokaslr as one of the kernel's boot parameters.

There are several side-channel attacks in x86 processors that could leak kernel addresses. In late 2017, kernel page-table isolation (KPTI aka KAISER) was developed to defeat these attacks. However, this method cannot protect against side-channel attacks utilizing collisions in branch predictor structures.

As of 2021, finer grained kernel address space layout randomization (or function granular KASLR, FGKASLR) is a planned extension of KASLR to randomize down to the function level by placing functions in separate sections and reordering them at boot time.

### Microsoft Windows

Microsoft's Windows Vista (released *to manufacturing* November 2006, generally available January 2007) and later have ASLR enabled only for executables and dynamic link libraries that are specifically linked to be ASLR-enabled. For compatibility, it is not enabled by default for other applications. Typically, only older software is incompatible and ASLR can be fully enabled by editing a registry entry `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\MoveImages`, or by installing Microsoft's Enhanced Mitigation Experience Toolkit.

The locations of the heap, stack, Process Environment Block, and Thread Environment Block are also randomized. A security whitepaper from Symantec noted that ASLR in 32-bit Windows Vista may not be as robust as expected, and Microsoft has acknowledged a weakness in its implementation.

Host-based intrusion prevention systems such as *WehnTrust* and *Ozone* also offer ASLR for Windows XP and Windows Server 2003 operating systems. WehnTrust is open-source. Complete details of Ozone's implementation are not available.

It was noted in February 2012 that ASLR on 32-bit Windows systems prior to Windows 8 can have its effectiveness reduced in low memory situations. A similar effect also had been achieved on Linux in the same research. The test code caused the Mac OS X 10.7.3 system to kernel panic, so it was left unclear about its ASLR behavior in this scenario.

### NetBSD

Support for ASLR in userland appeared in NetBSD 5.0 (released April 2009), and was enabled by default in NetBSD-current in April 2016.

Kernel ASLR support on amd64 was added in NetBSD-current in October 2017, making NetBSD the first BSD system to support KASLR.

### OpenBSD

In 2003, OpenBSD became the first mainstream operating system to support a strong form of ASLR and to activate it by default. OpenBSD completed its ASLR support in 2008 when it added support for PIE binaries. OpenBSD 4.4's malloc(3) was designed to improve security by taking advantage of ASLR and gap page features implemented as part of OpenBSD's `mmap` system call, and to detect use-after-free bugs. Released in 2013, OpenBSD 5.3 was the first mainstream operating system to enable position-independent executables by default on multiple hardware platforms, and OpenBSD 5.7 activated position-independent static binaries (Static-PIE) by default.

### macOS

In Mac OS X Leopard 10.5 (released October 2007), Apple introduced randomization for system libraries.

In Mac OS X Lion 10.7 (released July 2011), Apple expanded their implementation to cover all applications, stating "address space layout randomization (ASLR) has been improved for all applications. It is now available for 32-bit apps (as are heap memory protections), making 64-bit and 32-bit applications more resistant to attack."

As of OS X Mountain Lion 10.8 (released July 2012) and later, the entire system including the kernel as well as kexts and zones are randomly relocated during system boot.

### Solaris

ASLR has been introduced in Solaris beginning with Solaris 11.1 (released October 2012). ASLR in Solaris 11.1 can be set system-wide, per zone, or on a per-binary basis.

## Exploitation

A side-channel attack utilizing branch target buffer was demonstrated to bypass ASLR protection. In 2017, an attack named "ASLR⊕Cache" was demonstrated which could defeat ASLR in a web browser using JavaScript.

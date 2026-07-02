---
title: "glibc"
source: https://en.wikipedia.org/wiki/GNU_C_Library
domain: fortify-source
license: CC-BY-SA-4.0
tags: fortify source hardening, compiler runtime buffer checks, glibc object size checking, hardened build flags
fetched: 2026-07-02
---

# glibc

(Redirected from

GNU C Library

)

The **GNU C Library**, commonly known as **glibc**, is the GNU Project implementation of the C standard library. It provides a wrapper around the system calls of the Linux kernel and other kernels for application use. Despite its name, it now also directly supports C++ (and, indirectly, other programming languages). It was started in the 1980s by the Free Software Foundation (FSF) for the GNU operating system.

glibc is free software released under the GNU Lesser General Public License. The GNU C Library project provides the core libraries for the GNU system, as well as many systems that use Linux as the kernel. These libraries provide critical APIs including ISO C11, POSIX.1-2008, BSD, OS-specific APIs and more. These APIs include such foundational facilities as open, read, write, malloc, printf, getaddrinfo, dlopen, pthread_create, crypt, login, exit and more.

## History

| Version | Date | Highlights |
|---|---|---|
| 0.1 – 0.6 | October 1991 – February 1992 |   |
| 1.0 | February 1992 |   |
| 1.01 – 1.09.3 | March 1992 – December 1994 |   |
| 1.90 – 1.102 | May 1996 – January 1997 |   |
| 2.0 | January 1997 |   |
| 2.0.1 | January 1997 |   |
| 2.0.2 | February 1997 |   |
| 2.0.91 | December 1997 |   |
| 2.0.95 | July 1998 |   |
| 2.1 | February 1999 |   |
| 2.1.1 | March 1999 |   |
| 2.2 | November 2000 |   |
| 2.2.1 | January 2001 |   |
| 2.2.2 | February 2001 |   |
| 2.2.3 | March 2001 |   |
| 2.2.4 | July 2001 |   |
| 2.3 | October 2002 |   |
| 2.3.1 | October 2002 |   |
| 2.3.2 | February 2003 |   |
| 2.3.3 | December 2003 |   |
| 2.3.4 | December 2004 | Minimum for Linux Standard Base (LSB) 3.0 |
| 2.3.5 | April 2005 |   |
| 2.3.6 | November 2005 |   |
| 2.4 | March 2006 | Minimum for LSB 4.0, initial inotify support |
| 2.5 | September 2006 | Full inotify support. RHEL5 end of support was November 30, 2020 (2020-11-30) |
| 2.6 | May 2007 |   |
| 2.7 | October 2007 |   |
| 2.8 | April 2008 |   |
| 2.9 | November 2008 |   |
| 2.10 | May 2009 | Minimum for LSB 5.0. Initial psiginfo Archived 19 September 2021 at the Wayback Machine support. |
| 2.11 | October 2009 | SLES11 reached end of long-term support in March 2022. |
| 2.12 | May 2010 |   |
| 2.13 | January 2011 |   |
| 2.14 | June 2011 |   |
| 2.15 | March 2012 |   |
| 2.16 | June 2012 | x32 ABI support, ISO C11 compliance, SystemTap |
| 2.17 | December 2012 | 64-bit ARM support |
| 2.18 | August 2013 | Improved C++11 support. Support for Intel TSX lock elision. Support for the Xilinx MicroBlaze and IBM POWER8 microarchitectures. |
| 2.19 | February 2014 | SystemTap probes for malloc. GNU Indirect Function (IFUNC) support for ppc32 and ppc64. New feature test macro _DEFAULT_SOURCE to replace _SVID_SOURCE and _BSD_SOURCE. Preliminary safety documentation for all functions in the manual. ABI change in ucontext and jmp_buf for s390/s390x. |
| 2.20 | September 2014 | Support for file description locks |
| 2.21 | February 2015 | New semaphore implementation |
| 2.22 | August 2015 | Support to enable Google Native Client (NaCl), that originally ran on x86, running on ARMv7-A, Unicode 7.0 |
| 2.23 | February 2016 | Unicode 8.0 |
| 2.24 | August 2016 | Some deprecated features have been removed |
| 2.25 | February 2017 | The `getentropy` and `getrandom` functions, and the `<sys/random.h>` header file have been added. |
| 2.26 | August 2017 | Improved performance (per-thread cache for malloc), Unicode 10 support |
| 2.27 | February 2018 | Performance optimizations. RISC-V support. |
| 2.28 | August 2018 | `statx`, `renameat2`, Unicode 11.0.0 |
| 2.29 | February 2019 | `getcpu` wrapper build and install all locales as directories with files optimized trigonomical functions Transactional Lock Elision for powercp64le ABI posix_spawn_file_actions_addchdir_np and posix_spawn_file_actions_addfchdir_np popen and system do not run atfork handlers anymore support for the C-SKY ABIV2 running on Linux strftime's default formatting of a locale's alternative year; the '_' and '-' flags can now be applied to its "%EY" |
| 2.30 | August 2019 | Unicode 12.1.0, the dynamic linker accepts the `--preload` argument to preload shared objects, the `gettid` function has been added on Linux, Minguo (Republic of China) calendar support, new Japanese era added to ja_JP locale, memory allocation functions fail with total object size larger than `PTRDIFF_MAX`; CVE-2019-7309 and CVE-2019-9169 fixed |
| 2.31 | February 2020 | Initial C23 standard support |
| 2.32 | August 2020 | Unicode 13.0, 'access' attribute for better warnings in GCC 10, i.e. to "help detect buffer overflows and other out-of-bounds accesses" |
| 2.33 | February 2021 | HWCAPS |
| 2.34 | August 2021 | libpthread, libdl, libutil, libanl has been integrated into libc. |
| 2.35 | February 2022 | Unicode 14.0, C.UTF-8 locale, restartable sequences. Removed Intel MPX support. |
| 2.36 | August 2022 |   |
| 2.37 | February 2023 | Unicode 15.0 |
| 2.38 | August 2023 | The strlcpy and strlcat functions added. libmvec support for ARM64. |
| 2.39 | January 2024 | The stdbit.h header has been added from ISO C2X. Support for shadow stacks on x86_64, new security features, and the removal of libcrypt. |
| 2.40 | July 2024 | Partial support for the ISO C23 standard, a new tunable for the testing of setuid programs, improved 64-bit ARM vector support. |
| 2.41 | January 2025 | Add sinpi, cospi, tanpi functions. Unicode 16.0 |
| 2.42 | July 2025 | New math functions, support for arbitrary baud rates in the termios.h interface, SFrame-based stack tracing. |
| 2.43 | January 2026 | Unicode 17.0, more C23 support, openat2 and mseal on Linux, experimental Clang support |

The glibc project was initially written mostly by Roland McGrath, working for the Free Software Foundation (FSF) in the summer of 1987 as a teenager. In February 1988, FSF described glibc as having nearly completed the functionality required by ANSI C. By 1992, it had the ANSI C-1989 and POSIX.1-1990 functions implemented and work was under way on POSIX.2. In September 1995 Ulrich Drepper made his first contribution to the glibc and by 1997 most commits were made by him. Drepper held the maintainership position for many years and until 2012 accumulated 63% of all commits to the project.

In May 2009, glibc was migrated to a Git repository.

In 2010, a licensing issue was resolved which was caused by the Sun RPC implementation in glibc that was not GPL compatible. It was fixed by re-licensing the Sun RPC components under the BSD license.

In 2014, glibc suffered from an ABI breakage bug on s390.

In July 2017, 30 years after he started glibc, Roland McGrath announced his departure, "declaring myself maintainer emeritus and withdrawing from direct involvement in the project. These past several months, if not the last few years, have proven that you don't need me anymore".

In 2018, maintainer Raymond Nicholson removed a joke about abortion from the glibc source code. It was restored later by Alexandre Oliva after Richard Stallman demanded to have it returned.

In 2021, the copyright assignment requirement to the Free Software Foundation was removed from the project.

### Fork and variant

In 1994, the developers of the Linux kernel forked glibc. Their fork, "Linux libc", was maintained separately until around 1998. Because the copyright attribution was insufficient, changes could not be merged back to the GNU Libc. When the FSF released glibc 2.0 in January 1997, the kernel developers discontinued Linux libc due to glibc 2.0's superior compliance with POSIX standards. glibc 2.0 also had better internationalization and more in-depth translation, IPv6 capability, 64-bit data access, facilities for multithreaded applications, future version compatibility, and the code was more portable. The last-used version of Linux libc used the internal name (soname) libc.so.5. Following on from this, glibc 2.x on Linux uses the soname libc.so.6

In 2009, Debian and a number of derivatives switched from glibc to the variant eglibc. Eglibc was supported by a consortium consisting of Freescale, MIPS, MontaVista and Wind River. It contained changes that made it more suitable for embedded usage and had added support for architectures that were not supported by glibc, such as the PowerPC e500. The code of eglibc was merged back into glibc at version 2.20. Since 2014, eglibc is discontinued. The Yocto Project and Debian also moved back to glibc since the release of Debian Jessie.

### Steering committee

Starting in 2001 the library's development had been overseen by a committee, with Ulrich Drepper kept as the lead contributor and maintainer. The steering committee installation was surrounded by a public controversy, as it was openly described by Ulrich Drepper as a failed hostile takeover maneuver by Richard Stallman.

In March 2012, the steering committee voted to disband itself and remove Drepper in favor of a community-driven development process, with Ryan Arnold, Maxim Kuvyrkov, Joseph Myers, Carlos O'Donell, and Alexandre Oliva holding the responsibility of GNU maintainership (but no extra decision-making power).

## Functionality

glibc provides the functionality required by the Single UNIX Specification, POSIX (1c, 1d, and 1j) and some of the functionality required by ISO C11, ISO C99, Berkeley Unix (BSD) interfaces, the System V Interface Definition (SVID) and the X/Open Portability Guide (XPG), Issue 4.2, with all extensions common to XSI (X/Open System Interface) compliant systems along with all X/Open UNIX extensions.

In addition, glibc also provides extensions that have been deemed useful or necessary while developing GNU.

### Supported hardware and kernels

glibc is used in systems that run many different kernels and different hardware architectures. Its most common use is in systems using the Linux kernel on x86 hardware, however, officially supported hardware includes: ARM, ARC, C-SKY, DEC Alpha, IA-64, Motorola m68k, MicroBlaze, MIPS, Nios II, PA-RISC, PowerPC, RISC-V, s390, SPARC, and x86 (old versions support TILE). It officially supports the Hurd and Linux kernels. Additionally, there are heavily patched versions that run on the kernels of FreeBSD and NetBSD (from which Debian GNU/kFreeBSD and Debian GNU/NetBSD systems are built, respectively), as well as a forked-version of OpenSolaris. It is also used (in an edited form) and named libroot.so in BeOS and Haiku.

### Use in small devices

glibc has been criticized as being "bloated" and slower than other libraries in the past, e.g. by Linus Torvalds and embedded Linux programmers. For this reason, several alternative C standard libraries have been created which emphasize a smaller footprint. However, many small-device projects use GNU libc over the smaller alternatives because of its application support, standards compliance, and completeness. Examples include Openmoko and Familiar Linux for iPaq handhelds (when using the GPE display software).

### Secure string functions

glibc does not implement bounds-checking interfaces defined in C11 and did not implement strlcpy and strlcat until 2023 on the grounds that "in practice these functions can cause trouble, as their intended use encourages silent data truncation, adds complexity and inefficiency, and does not prevent all buffer overruns in the destinations." The FAQ pointed out that the bounds-checking interfaces were optional in the ISO standard and that snprintf was available as an alternative.

## Compatibility layers

There are compatibility layers ("shims") to allow programs written for other ecosystems to run on glibc interface offering systems. These include libhybris, a compatibility layer for Android's Bionic, and Wine, which can be seen as a compatibility layer from Windows APIs to glibc and other native APIs available on Unix-like systems.

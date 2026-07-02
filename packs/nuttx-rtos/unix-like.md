---
title: "Unix-like"
source: https://en.wikipedia.org/wiki/Unix-like
domain: nuttx-rtos
license: CC-BY-SA-4.0
tags: nuttx rtos, apache nuttx, posix embedded, px4 flight stack
fetched: 2026-07-02
---

# Unix-like

A **Unix-like** operating system (sometimes referred to as a **UN*X,** ***nix** or ***NIX**) is one that behaves in a manner similar to a Unix system, although not necessarily conforming to or being certified to any version of the Single UNIX Specification. A Unix-like application is one that behaves like the corresponding Unix command or shell. Although there are general philosophies for Unix design, there is no technical standard defining the term, and opinions can differ about the degree to which a particular operating system or application is Unix-like. Some well-known examples of Unix-like operating systems include Linux, FreeBSD and OpenBSD. These systems are often used on servers as well as on personal computers and other devices. Many popular applications, such as the Apache web server and the Bash shell, are also designed to be used on Unix-like systems.

## Definition

The Open Group owns the UNIX trademark and administers the Single UNIX Specification, with the "UNIX" name being used as a certification mark. They do not approve of the construction "Unix-like" and consider it a misuse of their trademark. Their guidelines require "UNIX" to be presented in uppercase or otherwise distinguished from the surrounding text, strongly encourage using it as a branding adjective for a generic word such as "system", and discourage its use in hyphenated phrases.

Other parties frequently treat "Unix" as a genericized trademark. Some add a wildcard character to the name to make an abbreviation like "Un*x" or "*nix", since Unix-like systems often have Unix-like names such as AIX, A/UX, HP-UX, IRIX, Linux, Minix, Ultrix, Xenix, and XNU. These patterns do not literally match many system names, but are still generally recognized to refer to any UNIX system, descendant, or work-alike, even those with completely dissimilar names such as Darwin/macOS, illumos/Solaris or FreeBSD.

In 2007, Wayne R. Gray sued to dispute the status of UNIX as a trademark, claiming Novell did not lawfully own the trademark when they transferred it to X/Open (pointing to The SCO Group's statements which had, by then, already been deemed invalid by a court). He lost his case, and lost again on appeal, with the court upholding the trademark and its ownership.

## History

"Unix-like" systems started to appear in the late 1970s and early 1980s. Many proprietary versions, such as Idris (1978), UNOS (1982), Coherent (1983), and UniFlex (1985), aimed to provide businesses with the functionality available to academic users of UNIX.

When AT&T allowed relatively inexpensive commercial binary sublicensing of UNIX in 1979, a variety of proprietary systems were developed based on it, including AIX, HP-UX, IRIX, SunOS, Tru64, Ultrix, and Xenix. These largely displaced the proprietary clones. Growing incompatibility among these systems led to the creation of interoperability standards, including POSIX and the Single UNIX Specification.

Various free, low-cost, and unrestricted substitutes for UNIX emerged in the 1980s and 1990s, including 4.4BSD, Linux, and Minix. Some of these have in turn been the basis for commercial "Unix-like" systems, such as BSD/OS and macOS. Several versions of (Mac) OS X/macOS running on Intel-based and Apple silicon-based Mac computers have been certified under the Single UNIX Specification. The BSD variants are descendants of UNIX developed by the University of California at Berkeley, with UNIX source code from Bell Labs. However, the BSD code base has evolved since then, replacing all the AT&T code. Since the BSD variants are not certified as compliant with the Single UNIX Specification, they are referred to as "UNIX-like" rather than "UNIX".

## Categories

Eric S. Raymond and Rob Landley have suggested that there are three kinds of Unix-like systems: "genetic UNIX", derived from the original Bell Labs UNIX, "trademark UNIX" (or "branded UNIX"), for which the Open Group have licensed the UNIX trademark, and a third category of operating systems that are not in either of those categories but that are patterned after the original Bell Labs UNIX.

### Genetic UNIX

Those systems with a historical connection to the AT&T codebase. Most commercial UNIX systems fall into this category. So do the BSD systems, which are descendants of work done at the University of California, Berkeley in the late 1970s and early 1980s. Some of these systems have no original AT&T code but can still trace their ancestry to AT&T designs.

### Trademark UNIX

Trademark, or branded, UNIX systems‍—‌largely commercial in nature‍—‌have been determined by the Open Group to meet the Single UNIX Specification and are allowed to carry the UNIX name. Most such systems are commercial derivatives of the System V code base in one form or another, although Apple macOS 10.5 and later is a BSD variant that has been certified, and EulerOS and Inspur K-UX are Linux distributions that have been certified. A few other systems (such as IBM z/OS) earned the trademark through a POSIX compatibility layer and are not otherwise inherently Unix systems. Many ancient UNIX systems no longer meet this definition.

### Other UNIXes

Broadly, any Unix-like system that behaves in a manner roughly consistent with the UNIX specification, including having a "program which manages login and command line sessions"; more specifically, this can refer to systems, such as Linux or Minix, that behave similarly to a UNIX system but have no genetic or trademark connection to the AT&T code base. Most free/open-source implementations of the UNIX design, whether genetic UNIX or not, fall into the restricted definition of this third category due to the expense of obtaining Open Group certification, which costs thousands of dollars.

Dennis Ritchie, one of the original creators of Unix, mentioned Linux as one of the healthiest of the direct Unix derivatives due to its strong adherence to Unix principles.

Around 2001 Linux was given the opportunity to get a certification including free help from the POSIX chair Andrew Josey for the symbolic price of one dollar. There have been some activities to make Linux POSIX-compliant, with Josey having prepared a list of differences between the POSIX standard and the Linux Standard Base specification, but in August 2005 this project was shut down because of lack of interest at the LSB work group. As per § Trademark UNIX, some Linux distributions have been certified.

## Compatibility layers

Some non-Unix-like operating systems provide a Unix-like compatibility layer, with varying degrees of Unix-like functionality.

- IBM z/OS's UNIX System Services is sufficiently complete as to be certified as trademark UNIX.
- Cygwin, MSYS, and MSYS2 each provide a GNU environment on top of the Microsoft Windows user API, sufficient for most common open source software to be compiled and run.
- The MKS Toolkit and UWIN are comprehensive interoperability tools which allow the porting of Unix programs to Windows.
- Windows NT-type systems have a POSIX environmental subsystem (original implementation discontinued since Windows XP; Interix-based implementation discontinued since Windows 8.1).
- Subsystem for Unix-based Applications (previously Interix) provides Unix-like functionality as a Windows NT subsystem (discontinued).
- Windows Subsystem for Linux provides a Linux-compatible kernel interface developed by Microsoft and containing no Linux code, with Ubuntu user-mode binaries running on top of it.
  - Windows Subsystem for Linux version 2 (WSL2) provides a fully functional Linux environment running in a virtual machine.
- OpenHarmony employs the third-party musl libc library and native APIs ports, providing support on POSIX for Linux syscalls within the Linux kernel and LiteOS default kernels side of the system multi-kernel Kernel Abstract Layer subsystem for vendor and developers interoperability.
- HarmonyOS with HarmonyOS NEXT system has OpenHarmony user mode that contains musl libc library and native APIs ports, providing support with POSIX for Linux syscalls within the default kernels of the Linux kernel standard system and LiteOS small and lightweight system side of the system multi-kernel Kernel Abstract Layer subsystem for interoperability on legacy Unix-like functionalities.

Other means of Windows-Unix interoperability include:

- The above Windows packages can be used with various X servers for Windows
- Hummingbird Connectivity provides several ways for Windows machines to connect to Unix and Linux machines, from terminal emulators to X clients and servers, and others
- The Windows Resource Kits for versions of Windows NT include a Bourne Shell, some command-line tools, and a version of Perl
- Hamilton C shell is a version of csh written specifically for Windows.

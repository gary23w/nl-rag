---
title: "Cygwin"
source: https://en.wikipedia.org/wiki/Cygwin
domain: wsl-subsystem
license: CC-BY-SA-4.0
tags: windows subsystem for linux, wsl subsystem, subsystem for android, windows terminal
fetched: 2026-07-02
---

# Cygwin

**Cygwin** (/ˈsɪɡwɪn/ *SIG-win*) is a free and open-source Unix-like environment and command-line interface (CLI) for Microsoft Windows. The project also provides a software repository containing open-source packages. Cygwin allows source code for Unix-like operating systems to be compiled and run on Windows. Cygwin provides native integration of Windows-based applications.

The terminal emulator mintty is the default command-line interface provided to interact with the environment. The Cygwin installation directory layout mimics the root file system of Unix-like systems, with directories such as `/bin`, `/home`, `/etc`, `/usr`, and `/var`.

Cygwin is released under the GNU Lesser General Public License version 3. It was originally developed by Cygnus Solutions, which was later acquired by Red Hat (now part of IBM), to port the GNU toolchain to Win32, including the GNU Compiler Suite. Rather than rewrite the tools to use the Win32 runtime environment, Cygwin implemented a POSIX-compatible environment in the form of a DLL.

The brand motto is "*Get that Linux feeling – on Windows*", although Cygwin doesn't have Linux in it.

## History

Cygwin began in 1995 as a project of Steve Chamberlain, a Cygnus engineer who observed that Windows NT and 95 used COFF as their object file format, and that GNU already included support for x86 and COFF, and the C library newlib. He thought that it would be possible to retarget GCC and produce a cross compiler generating executables that could run on Windows. A prototype was later developed. Chamberlain bootstrapped the compiler on a Windows system, to emulate Unix to let the GNU configure shell script run.

Initially, Cygwin was called *Cygwin32*. When Microsoft registered the trademark Win32, the "32" was dropped to simply become *Cygwin*.

In 1999, Cygnus offered Cygwin 1.0 as a commercial product. Subsequent versions have not been released, instead relying on continued open source releases.

Geoffrey Noer was the project lead from 1996 to 1999. Christopher Faylor was lead from 1999 to 2004; he left Red Hat and became co-lead with Corinna Vinschen. Corinna Vinschen has been the project lead from mid-2014 to date (as of September, 2024).

From June 23, 2016, the Cygwin library version 2.5.2 was licensed under the GNU Lesser General Public License (LGPL) version 3.

## Description

Cygwin is provided in two versions: the full 64-bit version and a stripped-down 32-bit version, whose final version was released in 2022. Cygwin consists of a library that implements the POSIX system call API in terms of Windows system calls to enable the running of a large number of application programs equivalent to those on Unix systems, and a GNU development toolchain (including GCC and GDB). Programmers have ported the X Window System, K Desktop Environment 3, GNOME, Apache, and TeX. Cygwin permits installing inetd, syslogd, sshd, Apache, and other daemons as standard Windows services. Cygwin programs have full access to the Windows API and other Windows libraries.

Cygwin programs are installed by running Cygwin's "setup" program, which downloads them from repositories on the Internet.

The Cygwin API library is licensed under the GNU Lesser General Public License version 3 (or later), with an exception to allow linking to any free and open-source software whose license conforms to the Open Source Definition.

Cygwin consists of two parts:

1. A dynamic-link library in the form of a C standard library that acts as a compatibility layer for the POSIX API and
2. A collection of software tools and applications that provide a Unix-like look and feel.

Cygwin supports POSIX symbolic links, representing them as plain-text files with the system attribute set. Cygwin 1.5 represented them as Windows Explorer shortcuts, but this was changed for reasons of performance and POSIX correctness. Cygwin also recognises NTFS junction points and symbolic links and treats them as POSIX symbolic links, but it does not create them. The POSIX API for handling access control lists (ACLs) is supported.

### Technical details

A Cygwin-specific version of the Unix `mount` command allows mounting Windows paths as "filesystems" in the Unix file space. Initial mount points can be configured in `/etc/fstab`, which has a format very similar to Unix systems, except that Windows paths appear in place of devices. Filesystems can be mounted in binary mode (by default), or in text mode, which enables automatic conversion between LF and CRLF endings (which only affects programs that open files without explicitly specifying text or binary mode).

Cygwin 1.7 introduced comprehensive support for POSIX locales, and the UTF-8 Unicode encoding became the default.

The fork system call for duplicating a process is fully implemented, but the copy-on-write optimization strategy could not be used.

Cygwin's default user interface is the bash shell running in the mintty terminal emulator. The DLL also implements pseudo terminal (pty) devices, and Cygwin ships with a number of terminal emulators that are based on them, including rxvt/urxvt and xterm. The version of GCC that comes with Cygwin has various extensions for creating Windows DLLs, such as specifying whether a program is a windowing or console-mode program. Support for compiling programs that do not require the POSIX compatibility layer provided by the Cygwin DLL used to be included in the default GCC, but as of 2014, it is provided by cross-compilers contributed by the MinGW-w64 project.

## Software packages

Cygwin's base package selection is approximately 100MB, containing the bash (interactive user) and dash (installation) shells and the core file and text manipulation utilities. Additional packages are available as optional installs from within the Cygwin "setup" program and package manager ("setup-x86_64.exe" – 64 bit). The Cygwin Ports project provided additional packages that were not available in the Cygwin distribution itself. Examples included GNOME, K Desktop Environment 3, MySQL database, and the PHP scripting language. Most ports have been adopted by volunteer maintainers as Cygwin packages, and Cygwin Ports are no longer maintained. Cygwin ships with GTK+ and Qt.

The Cygwin/X project allows graphical Unix programs to display their user interfaces on the Windows desktop for both local and remote programs.

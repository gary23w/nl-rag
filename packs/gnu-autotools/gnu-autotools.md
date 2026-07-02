---
title: "GNU Autotools"
source: https://en.wikipedia.org/wiki/GNU_Autotools
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
---

# GNU Autotools

The **GNU Autotools**, also known as the **GNU Build System**, is a suite of build automation tools designed to support building source code and packaging the resulting binaries. It supports building a codebase for multiple target systems without customizing or modifying the code. It is available on many Linux distributions and Unix-like environments.

Autotools is part of the GNU toolchain and is widely used in many free software and open source packages. Its component tools are free software, licensed under the GNU General Public License with special license exceptions permitting its use with proprietary software.

## Motivation

It can be difficult to make a software program portable. Compilers differ from system to system. Certain library functions are missing on some systems. Compiler files (such as C headers) may have different names. Shared libraries may be compiled and installed in different ways. One way to handle platform differences is to write conditionally compiled code (i.e. via `#ifdef`), but because of the wide variety of build environments, this approach quickly becomes unmanageable. Autotools is designed to address this problem more manageably.

## Components

Autotools consists of the GNU utilities Autoconf, Automake, and Libtool. Other related tools include GNU make, GNU gettext, pkg-config, and the GNU Compiler Collection (GCC).

## Usage

Autotools assists with sharing cross-platform software with a relatively broad user community. It facilitates sharing the source code by providing relatively robust cross-platform build support so that consumers can build the software themselves. Generally, the source code is distributed with a script, named *configure*, that has no dependencies other than a Bourne-compatible shell. Autotools need not be available. The consumer runs `configure` which generates various files including a *Makefile* which the consumer uses by running `make`.

Autotools can be used both for building native programs on the build machine and also for cross-compiling to other architectures.

Cross-compiling software to run on a Windows host from a Linux or other Unix-like build system is also possible, using MinGW, however native compilation is often desirable on operating systems (such as the Microsoft Windows family of systems) that cannot run Bourne shell scripts on their own. This makes building such software on the Windows operating system a bit harder than on a Unix-like system which provides the Bourne shell as a standard component. One can install the Cygwin or MSYS system on top of Windows to provide a Unix-like compatibility layer, though, allowing configure scripts to run. Cygwin also provides the GNU Compiler Collection, GNU make, and other software that provides a nearly complete Unix-like system within Windows; MSYS also provides GNU make and other tools designed to work with the MinGW version of GCC.

A consumer can re-generate the configure script which might be necessary if they amend the source code. In this case, they need to have Autotools installed.

The autoconf-generated configure script can be slow because it executes programs such as a C compiler multiple times to test whether various libraries, header files, and language features are present. This particularly affects Cygwin, which, due to its lack of a native fork system call, may execute configure scripts considerably slower than on Linux.

## Criticism

In his column for *ACM Queue*, FreeBSD developer Poul-Henning Kamp criticized the GNU Build System:

> The idea is that the configure script performs approximately 200 automated tests, so that the user is not burdened with configuring libtool manually. This is a horribly bad idea, already much criticized back in the 1980s when it appeared, as it allows source code to pretend to be portable behind the veneer of the configure script, rather than actually having the quality of portability to begin with. It is a travesty that the configure idea survived.

Kamp sketches the history of the build system in the portability problems inherent in the multitude of 1980s Unix variants, and bemoans the need for such build systems to exist:

> the 31,085 lines of configure for libtool still check if <sys/stat.h> and <stdlib.h> exist, even though the Unixen, which lacked them, had neither sufficient memory to execute libtool nor disks big enough for its 16-MB source code.

Although critics of the Autotools frequently advocate for alternatives that provide greater simplicity to their users, some have argued that this is not necessarily a good thing. John Calcote, author of the *Autotools, 2nd Edition: A Practitioner's Guide to GNU Autoconf, Automake, and Libtool*, opined:

> The Autotools are actually more transparent than any other build tools out there. All these other tools' (cmake, maven, etc) - that purport to be so much simpler because they insulate the user from the underlying details of the build process - these tool's primary failure is that this very insulation keeps users from being able to make the changes they need to accomplish their unique project-specific build goals.
> 
> Anyone who has nothing but good things to say about this aspect of cmake, maven, gradle, or whatever, has simply not worked on a project that requires them to move far enough away from the defaults. I've used them all and I've spent hours in frustration trying to determine how to work around the shortcomings of some "do-all" (except what I want) tool function. This is simply not an issue with the Autotools. As someone mentioned earlier in this thread, you can drop shell script into a configure.ac file, and make script into a Makefile.am file. That is the very definition of transparency. No other tool in existence allows this level of flexibility.

---
title: "Gentoo Linux"
source: https://en.wikipedia.org/wiki/Gentoo_Linux
domain: gentoo-linux
license: CC-BY-SA-4.0
tags: gentoo linux, portage tree, source-based distribution, rolling release
fetched: 2026-07-02
---

# Gentoo Linux

**Gentoo Linux** (pronounced /ˈdʒɛntuː/ *JEN-too*) is a Linux distribution built using the Portage package management system. Unlike a binary software distribution, the source code is compiled locally according to the user's preferences and is often optimized for the specific type of computer. Precompiled binaries are available for some packages, but only for systems using Glibc; no precompiled binaries are available for Musl based systems. Gentoo runs on a wide variety of processor architectures.

Gentoo package management is designed to be modular, portable, easy to maintain, and flexible. Gentoo describes itself as a meta-distribution because of its adaptability, in that the majority of its users have configurations and sets of installed programs which are unique to the system and the applications they use.

Gentoo Linux is named after the gentoo penguin, the fastest swimming species of penguin. The name was chosen to reflect the potential speed improvements of machine-specific optimizing, which is a major feature of Gentoo.

## History

Gentoo Linux was initially created by Daniel Robbins as the *Enoch Linux* distribution. Its design philosophy was that of precompiled binaries which were tuned to the hardware and that only included required programs. At least one version of Enoch was distributed under that name: version 0.75, in December 1999. An older release labeled "Enoch 0.5" can be found on the CD accompanying the August 1999 edition of the Danish computer magazine *Alt om Data*.

Daniel Robbins and the other contributors experimented with a fork of GCC known as EGCS, developed by Cygnus Solutions. It was at this point that "Enoch" was renamed "Gentoo" Linux. The modifications to EGCS eventually became part of the official GCC (version 2.95); Gentoo and other Linux distros benefited from similar speed increases.

After problems with a bug on his own system, Robbins halted Gentoo development and switched to FreeBSD for several months, later saying, "I decided to add several FreeBSD features to make our autobuild system (now called Portage) a true next-generation ports system."

Gentoo Linux 1.0 was released on March 31, 2002. In 2004, Robbins set up the non-profit Gentoo Foundation, transferred all copyrights and trademarks to it, and stepped down as chief architect of the project.

The current board of trustees is composed of five members who were announced (following an election) on March 2, 2008. The seven-member Gentoo Council oversees related technical issues and policies. The Gentoo Council members are elected annually, for a period of one year, by the active Gentoo developers. When a member of the Council retires, the successor is voted into place by the existing Council members.

The Gentoo Foundation is a domestic non-profit corporation, registered in the State of New Mexico. In late 2007, the Foundation's charter was revoked, but by May 2008 the State of New Mexico declared that the Gentoo Foundation, Inc. had returned to good standing and was free to do business.

The creator of Gentoo, Daniel Robbins, left the project in both 2004 and 2007 due to conflicts with other developers.

## Features

Gentoo is aimed at Linux users who prefer a high degree of control over the software installed and running on their computer. Users who invest time in configuring and optimizing a Gentoo system can build efficient desktops and servers. Gentoo supports building a Linux kernel tailored to specific hardware. It provides detailed control over which services are installed and running, including the option to choose between systemd or OpenRC as the default init system, among other possibilities. Memory usage may also be reduced compared to some other distributions by omitting unnecessary kernel features and services.

Gentoo's package repositories provide a large collection of software. Each package contains details of any dependencies, so only the minimum set of packages need to be installed. Optional features of individual packages, such as whether they require LDAP or Qt support, can be selected by the user and any resulting package requirements are automatically included in the set of dependencies.

Gentoo itself does not have a default look and feel, hence installed packages usually appear as their authors intended.

### Portage

Portage is Gentoo's software distribution and package management system. The original design was based on the ports system used by the Berkeley Software Distribution (BSD) operating systems. The Gentoo repository contains over 19,000 packages.

A single invocation of portage's emerge command can update the local copy of the Gentoo repository, search for a package, or download, compile, and install one or more packages and their dependencies. The built-in features can be set for individual packages, or globally, with so-called "USE flags".

Pre-compiled binaries are provided for some applications with long build times, such as LibreOffice and Mozilla Firefox, but users lose the ability to customize optional features. There are configuration options to reduce compiling times, such as by enabling parallel compiling or using pipes instead of temporary files. Package compiling may also be distributed over multiple computers. Additionally, the user may be able to mount a large filesystem in memory to further speed up the process of building packages. Some approaches have drawbacks and are not enabled by default. When installing the same package on multiple computers with sufficiently similar hardware, the package may be compiled once and a binary package created for quick installation on the other computers.

On December 29, 2023, it was announced that Gentoo will offer binary packages for download and direct installation. For most architectures, this will be limited to the core system and weekly updates. For amd64 and arm64 however the availability of binary packages reaches over 20 GB.

### Portability

As Gentoo is a source-based distribution with a repository describing how to build the packages, adding instructions to build on different machine architectures is particularly easy.

Originally built on the IA-32 architecture, Gentoo has since been ported to many others. It is officially supported and considered stable on IA-32, x86-64, PA-RISC, 32-bit and 64-bit PowerPC, 64-bit SPARC, DEC Alpha, and 32- and 64-bit ARM architectures. It is also officially supported but considered in-development state on MIPS, PS3 Cell Processor, System Z/s390. Official support for 32-bit SPARC, SuperH and Itanium have been dropped.

Portability towards other operating systems, such as those derived from Berkeley Software Distribution (BSD), including macOS, is under active development by the Gentoo/Alt project. The Gentoo/FreeBSD project already has a working guide based on FreeSBIE, while Gentoo/NetBSD, Gentoo/OpenBSD and Gentoo/DragonFly are being developed. A project exists to get Portage working on OpenSolaris. An experimental port to GNU Hurd was released on April 1, 2026.

It is also possible to install a Gentoo Prefix (provided by a project that maintains alternative installation methods for Gentoo) in a Cygwin environment on Windows, but this configuration is experimental.

## Installation

Gentoo may be installed in several ways. The most common is to use the Gentoo minimal CD with a stage3 tarball (explained below). As with many Linux distributions, Gentoo may be installed from almost any Linux environment, such as another Linux distribution's Live CD, Live USB, or Network Booting using the "Gentoo Alternative Install Guide". A normal install requires a connection to the Internet, but a network-less install guide exists.

On April 3, 2022, it was announced that there would be a new official image with a GUI, called the LiveGUI image. This can be installed onto installation media such as a USB drive or a dual-layer DVD. It includes a large selection of software, including the KDE Plasma 6 desktop environment, image editors, office software, system administration, and installation tools.

Previously, Gentoo supported installation from stage1 and stage2 tarballs. The Gentoo Foundation no longer recommends this usage; stage1 and stage2 are now meant only for Gentoo developers.

Following the initial install steps, the Gentoo Linux install process in the Gentoo Handbook describes compiling a new Linux kernel. This process is generally not required by other Linux distributions. Although the installation requires significantly more configuration than most mainline distributions, Gentoo provides documentation and tools such as its stage3 tarball and distribution kernels to simplify the process. In addition, users may also use an existing kernel known to work on their system by simply copying it to the boot directory, or installing one of the provided pre-compiled kernel packages, and updating their bootloader. Support for installation is provided on the Gentoo forum, Reddit, and IRC.

A Live USB of Gentoo Linux can be created manually, by using various tools, or with dd as described in the handbook.

### Stages

Before October 2005, installation could be started from any of three base stages:

- *Stage1* begins with only what is necessary to build a toolchain (the various compilers, linkers, and language libraries necessary to compile other software) for the target system; compiling this target toolchain from another, pre-existing host system is known as bootstrapping the target system.
- *Stage2* begins with a self-hosting (bootstrapped) toolchain for the target system, which is then used to compile all other core userland software for the target.
- *Stage3* begins with a minimal set of compiled user software, with which the kernel and any other additional software are then configured and compiled.

Since October 2005, only the stage3 installations have been officially supported, due to the inherent complexities of bootstrapping from earlier stages (which requires resolving and then breaking numerous circular dependencies). Tarballs for stage1 and stage2 were distributed for some time after this, although the instructions for installing from these stages had been removed from the handbook and moved into the Gentoo FAQ. As of September 2015, only the supported stage3 tarballs are publicly available; stage1 and stage2 tarballs are only "officially" generated and used internally by Gentoo development teams. However, if so desired, a user may still rebuild the toolchain or reinstall the base system software during or after a normal stage3 installation, effectively simulating the old bootstrap process.

### Gentoo Reference Platform

From 2003 until 2008, the **Gentoo Reference Platform** (GRP) was a snapshot of prebuilt packages that users could quickly install during the Gentoo installation process, to give faster access to a fully functional Gentoo installation. These packages included KDE, X Window System, OpenOffice, GNOME, and Mozilla. Once the installation was complete, the packages installed as part of the GRP were intended to be replaced by the user with the same or newer versions built through Portage that would be built using the user's system configuration rather than the generic builds provided by the GRP. As of 2011, the GRP is discontinued, the final reference to it appearing in the 2008.0 handbook.

## Versions

Gentoo follows a rolling release model.

Like other Linux distributions, Gentoo systems have an `/etc/gentoo-release` file, but this contains the version of the installed `sys-apps/baselayout` package.

In 2004, Gentoo began to version its Live media by year rather than numerically. This continued until 2008, when it was announced that the 2008.1 Live CD release had been cancelled in favour of weekly automated builds of both Stages 3 and Minimal CDs. On December 20, 2008, the first weekly builds were published. In 2009, a special Live DVD was created to celebrate the Gentoo 10-year anniversary.

### Release media version history

| Name | Date |
|---|---|
| (Enoch Linux) 0.75 | December 1999 |
| pre-1.0 | July 26, 2000 |
| 1.0 | March 31, 2002 |
| 1.1a | April 8, 2002 |
| 1.2 | June 10, 2002 |
| 1.4 | August 5, 2003 (Gentoo Reference Platform introduced) |
| 1.4 maintenance release 1 | September 11, 2003 |
| 2004.0 | March 1, 2004 (versioning changed to four releases a year) |
| 2004.1 | April 28, 2004 |
| 2004.2 | July 26, 2004 |
| 2004.3 | November 15, 2004 |
| 2005.0 | March 27, 2005 (versioning changed to semi-annual releases) |
| 2005.1 | August 8, 2005 |
| 2005.1-r1 | November 21, 2005 (maintenance release 1) |
| 2006.0 | February 27, 2006 |
| 2006.1 | August 30, 2006 |
| 2007.0 | May 7, 2007 |
| 2008.0 | July 6, 2008 |
| Weekly Releases started | September 22, 2008 |

#### Special releases

In 2009, a special Live DVD was released to celebrate Gentoo's tenth anniversary. Initially planned as a one-off, the Live DVD was updated to the latest package versions in 2011 due to its popularity among new users.

| Name | Date/info |
|---|---|
| Unreal Tournament 2003 LiveCD | September 18, 2002 - Bootable NVIDIA GPU-accelerated Unreal Tournament 2003 LiveCD, demoed at LinuxWorld Conference and Expo 2003. |
| 10.0 | October 4, 2009 (special edition Live DVD for the 10th anniversary) |
| 10.1 | October 10, 2009 (Bugfix release of Special Live DVD) |
| 11.0 | April 8, 2011 (Anniversary Live DVD is updated to latest package versions) |
| 12.0 | January 2, 2012 |
| 12.1 | April 1, 2012 (With an April Fool's joke named "Install Wizard") |
| 20121221 | December 21, 2012 (Live DVD - End Of World Edition) |
| 20140826 | August 26, 2014 (Live DVD - Iron Penguin Edition) |
| 20160514 | May 14, 2016 (Live DVD - Choice Edition; UEFI, ZFSOnLinux, and writable file systems using AUFS) |
| 20160704 | July 4, 2016 (Live DVD - Choice Edition Part Dos) |

### Profiles

Although Gentoo does not have a concept of versioning the entire system, it does make use of "profiles", which define build configuration for all packages in the system. Major changes, such as changing the layout of how files are installed across the entire system, typically involve a profile upgrade and may require rebuilding all installed software. These profiles are versioned based on the year they were released, and include several variants for each release targeted towards different types of systems (such as servers and desktops). Profiles formerly tracked the versioning of install media, and switched to two-digit year naming after the discontinuation of versioned media. The following new profile versions have been released after 2008.0:

| Version | Date/info |
|---|---|
| 10.0 | August 6, 2009 (cosmetic name change from 2008.0 profiles) |
| 13.0 | February 10, 2013 |
| 17.0 | November 30, 2017 (C++14 and PIE by default) |
| 17.1 | December 26, 2017 (altered multilib layout for amd64 systems) |
| 23.0 | March 22, 2024 (merged /usr became the default) |

### Hardened Gentoo

Hardened Gentoo is a project designed to develop and designate a set of add-ons that are useful when a more security focused installation is required. Previously, the project included patches to produce a hardened kernel, but these were discontinued. Other parts of the hardened set, such as SELinux, and userspace hardening remain.

## Incidents

In June 2018 the Gentoo GitHub code repository mirror used mainly by developers was hacked after an attacker gained access to an organization administrator's account via deducing the password. Gentoo promptly responded by containing the attack and improving security practices. No Gentoo cryptography keys or signed packages were compromised, and the repository was restored after five days.

## Logo and mascots

The gentoo penguin is thought to be the fastest underwater-swimming penguin. The name Gentoo Linux is a reference both to the omnibus Linux mascot— a penguin called Tux— and the project's aim to produce a high-performance operating system. Unofficial mascots include *Larry The Cow* and *Znurt the Flying Saucer*.

## Derived distributions

Several independently developed Gentoo Linux variants exist, as do products built off of Gentoo such as ChromiumOS.

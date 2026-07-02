---
title: "RPM Package Manager"
source: https://en.wikipedia.org/wiki/RPM_Package_Manager
domain: red-hat-linux
license: CC-BY-SA-4.0
tags: red hat enterprise linux, yum package manager, dnf tool, centos rebuild
fetched: 2026-07-02
---

# RPM Package Manager

**RPM** (originally **Red Hat Package Manager**, now a recursive acronym for **RPM Package Manager**) is a free and open-source package management system. The name RPM refers to the `.rpm` file format and the package manager program itself. RPM was intended primarily for Linux distributions; the file format is the baseline package format of the Linux Standard Base.

Although it was created for use in Red Hat Linux, RPM is now used in many Linux distributions such as PCLinuxOS, Fedora Linux, AlmaLinux, CentOS, openSUSE, OpenMandriva and Oracle Linux. It has also been ported to some other operating systems, such as Novell NetWare (as of version 6.5 SP3), IBM's AIX (as of version 4), IBM i, and ArcaOS. An RPM package can contain an arbitrary set of files. Most RPM files are "binary RPMs" (or BRPMs) containing the compiled version of some software. There are also "source RPMs" (or SRPMs) containing the source code used to build a binary package. These have an appropriate tag in the file header that distinguishes them from normal (B)RPMs, causing them to be extracted to /usr/src on installation. SRPMs customarily carry the file extension ".src.rpm" (.spm on file systems limited to 3 extension characters, e.g. old DOS FAT).

## History

RPM was originally written in 1997 by Erik Troan and Marc Ewing, based on `pms`, `rpp`, and `pm` experiences.

`pm` was written by Rik Faith and Doug Hoffman in May 1995 for Red Hat Software, its design and implementations were influenced greatly by `pms`, a package management system by Faith and Kevin Martin in the fall of 1993 for the Bogus Linux Distribution. `pm` preserves the "Pristine Sources + patches" paradigm of `pms`, while adding features and eliminating arbitrary limitations present in the implementation. `pm` provides greatly enhanced database support for tracking and verifying installed packages.

## Features

For a system administrator performing software installation and maintenance, the use of package management rather than manual building has advantages such as simplicity, consistency and the ability for these processes to be automated and non-interactive. rpm uses Berkeley DB as the backend database although since 4.15 in 2019, it supports building rpm packages without Berkeley DB (`–disable-bdb`).

Features of RPM include:

- RPM packages can be cryptographically verified with GPG and MD5
- Original source archive(s) (e.g. `.tar.gz`, `.tar.bz2`) are included in SRPMs, making verification easier
- Delta update: PatchRPMs and DeltaRPMs, the RPM equivalent of a patch file, can incrementally update RPM-installed software
- Automatic build-time dependency evaluation.

## Local operations

Packages may come from within a particular distribution (for example Red Hat Enterprise Linux) or be built for it by other parties (for example RPM Fusion for Fedora Linux). Circular dependencies among mutually dependent RPMs (so-called "dependency hell") can be problematic; in such cases a single installation command needs to specify all the relevant packages.

### Repositories

RPMs are often collected centrally in one or more repositories on the internet. A site often has its own RPM repositories which may either act as local mirrors of such internet repositories or be locally maintained collections of useful RPMs.

### Front ends

Several front-ends to RPM ease the process of obtaining and installing RPMs from repositories and help in resolving their dependencies. These include:

- yum used in Fedora Linux, CentOS 5 and above, Red Hat Enterprise Linux 5 and above, Scientific Linux, Yellow Dog Linux and Oracle Linux
- DNF, introduced in Fedora Linux 18 (default since 22), Red Hat Enterprise Linux 8, AlmaLinux 8, and CentOS Linux 8.
- up2date used in Red Hat Enterprise Linux, CentOS 3 and 4, and Oracle Linux
- Zypper used in Mer (and thus Sailfish OS), MeeGo, openSUSE and SUSE Linux Enterprise
- urpmi used in Mandriva Linux, ROSA Linux and Mageia
- apt-rpm, a port of Debian's Advanced Packaging Tool (APT) used in Ark Linux, PCLinuxOS and ALT Linux
- Smart Package Manager, used in Unity Linux, available for many distributions including Fedora Linux.
- `rpmquery`, a command-line utility available in (for example) Red Hat Enterprise Linux
- `libzypp`, for Sailfish OS

### Local RPM installation database

Working behind the scenes of the package manager is the RPM database, stored in `/var/lib/rpm`. It uses Berkeley DB as its back-end. It consists of a single database (`Packages`) containing all of the meta information of the installed RPMs. Multiple databases are created for indexing purposes, replicating data to speed up queries. The database is used to keep track of all files that are changed and created when a user (using RPM) installs a package, thus enabling the user (via RPM) to reverse the changes and remove the package later. If the database gets corrupted (which is possible if the RPM client is killed), the index databases can be recreated with the `rpm --rebuilddb` command.

## Description

Whilst the RPM format is the same across different Linux distributions, the detailed conventions and guidelines may vary across them.

### Package filename and label

An RPM is delivered in a single file, normally with a filename in the format:

<name>-<version>-<release>.src.rpm

for source packages, or

<name>-<version>-<release>.<architecture>.rpm

for binaries.

For example, in the package filename `libgnomeuimm-2.0-2.0.0_3.i386.rpm`, the `<name>` is `libgnomeuimm`, the `<version>` is `2.0`, the `<release>` is `2.0.0_3`, and the `<architecture>` is `i386`. The associated source package would be named `libgnomeuimm-2.0-2.0.0_3.src.rpm`

RPMs with the `noarch.rpm` extension do not depend on a particular CPU architecture. For example, these RPMs may contain graphics and text for other programs to use. They may also contain shell scripts or programs written in other interpreted programming languages such as Python.

The RPM contents also include a *package label*, which contains the following pieces of information:

- software name
- software version (the version taken from original upstream source of the software)
- package release (the number of times the package has been rebuilt using the same version of the software). This field is also often used for indicating the specific distribution the package is intended for by appending strings like "mdv" (formerly, "mdk") (Mandriva Linux), "mga" (Mageia), "fc4" (Fedora Core 4), "rh9" (Red Hat Linux 9), "suse100" (SUSE Linux 10.0) etc.
- architecture for which the package was built (i386, i686, x86_64, ppc, etc.)

The package label fields do not need to match the filename.

### Library packaging

Libraries are distributed in two separate packages for each version. One contains the precompiled code for use at run-time, while the second one contains the related development files such as headers, etc. Those packages have "-devel" appended to their name field. The system administrator should ensure that the versions of the binary and development packages match.

### Binary format

The format is binary and consists of four sections:

- The lead, which identifies the file as an RPM file and contains some obsolete headers.
- The signature, which can be used to ensure integrity and/or authenticity.
- The header, which contains metadata including package name, version, architecture, file list, etc.
- A file archive (the payload), which usually is in cpio format, compressed with gzip. The `rpm2cpio` tool enables retrieval of the cpio file without needing to install the RPM package.
  - The Linux Standard Base requires the use of gzip, but Fedora 30 packages are xz-compressed and Fedora 31 packages might be zstd-compressed. Recent versions of RPM can also use bzip2, lzip, or lzma compression.
  - RPM 5.0 format supports using xar for archiving.

### SPEC file

The "Recipe" for creating an RPM package is a spec file. Spec files end in the ".spec" suffix and contain the package name, version, RPM revision number, steps to build, install, and clean a package, and a changelog. Multiple packages can be built from a single RPM spec file, if desired. RPM packages are created from RPM spec files using the rpmbuild tool.

Spec files are usually distributed within SRPM files, which contain the spec file packaged along with the source code.

### SRPM

A typical RPM is pre-compiled software ready for direct installation. The corresponding source code can also be distributed. This is done in an SRPM, which also includes the "SPEC" file describing the software and how it is built. The SRPM also allows the user to compile, and perhaps modify, the code itself.

A software package could contain only platform independent scripts. In such a case, the developer could provide only an SRPM, which is still an installable RPM.

### NOSRC

This is a special version of SRPM. It contains "SPEC" file and optionally patches, but does not include sources (usually because of license).

## Forks

As of June 2010, there are two versions of RPM in development: one led by the Fedora Project and Red Hat, and the other by a separate group led by a previous maintainer of RPM, a former employee of Red Hat.

### RPM.org

The *rpm.org* community's first major code revision was in July 2007; version 4.8 was released in January 2010, version 4.9 in March 2011, 4.10 in May 2012, 4.11 in January 2013, 4.12 in September 2014 and 4.13 in July 2015.

This version is used by distributions such as Fedora Linux, Red Hat Enterprise Linux and derivatives, openSUSE, SUSE Linux Enterprise, Unity Linux, Mageia, OpenEmbedded, Tizen and OpenMandriva Lx (formerly Mandriva).

### RPM v5 (Defunct)

Jeff Johnson, the RPM maintainer since 1999, continued development efforts together with participants from several other distributions. RPM version 5 was released in May 2007.

This version was used by distributions such as Wind River Linux (until Wind River Linux 10), Rosa Linux, and OpenMandriva Lx (former Mandriva Linux which switched to rpm5 in 2011) and also by the OpenPKG project which provides packages for other common UNIX-platforms.

OpenMandriva Lx has switched back to rpm.org for 4.0 release.

OpenEmbedded, the last major user of RPM5, switched back to rpm.org due to issues in RPM5.

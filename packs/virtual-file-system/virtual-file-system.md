---
title: "Virtual file system"
source: https://en.wikipedia.org/wiki/Virtual_file_system
domain: virtual-file-system
license: CC-BY-SA-4.0
tags: virtual file system, vfs layer, filesystem in userspace, mount
fetched: 2026-07-02
---

# Virtual file system

A **virtual file system** (**VFS**) or **virtual filesystem switch** is an abstract layer on top of a more concrete file system. The purpose of a VFS is to allow client applications to access different types of concrete file systems in a uniform way. A VFS can, for example, be used to access local and network storage devices transparently without the client application noticing the difference. It can be used to bridge the differences in Windows, classic Mac OS/macOS and Unix filesystems, so that applications can access files on local file systems of those types without having to know what type of file system they are accessing.

A VFS specifies an interface (or a "contract") between the kernel and a concrete file system. Therefore, it is easy to add support for new file system types to the kernel simply by fulfilling the contract. The terms of the contract might change incompatibly from release to release, which would require that concrete file system support be recompiled, and possibly modified before recompilation, to allow it to work with a new release of the operating system; or the supplier of the operating system might make only backward-compatible changes to the contract, so that concrete file system support built for a given release of the operating system would work with future versions of the operating system.

## Implementations

One of the first virtual file system mechanisms on Unix-like systems was introduced by Sun Microsystems in SunOS 2.0 in 1985. It allowed Unix system calls to access local UFS file systems and remote NFS file systems transparently. For this reason, Unix vendors who licensed the NFS code from Sun often copied the design of Sun's VFS. Other file systems could be plugged into it also: there was an implementation of the MS-DOS FAT file system developed at Sun that plugged into the SunOS VFS, although it was not shipped as a product until SunOS 4.1. The SunOS implementation was the basis of the VFS mechanism in System V Release 4.

John Heidemann developed a *stacking* VFS under SunOS 4.0 for the experimental Ficus file system. This design provided for code reuse among file system types with differing but similar semantics (*e.g.*, an encrypting file system could reuse all of the naming and storage-management code of a non-encrypting file system). Heidemann adapted this work for use in 4.4BSD as a part of his thesis research; descendants of this code underpin the file system implementations in modern BSD derivatives including macOS.

Other Unix virtual file systems include the File System Switch in System V Release 3, the Generic File System in Ultrix, and the VFS in Linux. In OS/2 and Microsoft Windows, the virtual file system mechanism is called the Installable File System.

The Filesystem in Userspace (FUSE) mechanism allows userland code to plug into the virtual file system mechanism in Linux, NetBSD, FreeBSD, OpenSolaris, and macOS.

In Microsoft Windows, virtual filesystems can also be implemented through userland Shell namespace extensions; however, they do not support the lowest-level file system access application programming interfaces in Windows, so not all applications will be able to access file systems that are implemented as namespace extensions. KIO and GVfs/GIO provide similar mechanisms in the KDE and GNOME desktop environments (respectively), with similar limitations, although they can be made to use FUSE techniques and therefore integrate smoothly into the system.

## Single-file virtual file systems

Sometimes Virtual File System refers to a file or a group of files (not necessarily inside a concrete file system) that acts as a manageable container which should provide the functionality of a concrete file system through the usage of software. Examples of such containers are CBFS Connect from Callback Technologies or a single-file virtual file system in an emulator like PCTask or so-called WinUAE, Oracle's VirtualBox, Microsoft's Virtual PC, VMware.

The primary benefit for this type of file system is that it is centralized and easy to remove. A single-file virtual file system may include all the basic features expected of any file system (virtual or otherwise), but access to the internal structure of these file systems is often limited to programs specifically written to make use of the single-file virtual file system (instead of implementation through a driver allowing universal access). Another major drawback is that performance is relatively low when compared to other virtual file systems. Low performance is mostly due to the cost of shuffling virtual files when data is written or deleted from the virtual file system.

### Implementation of single-file virtual filesystems

Direct examples of single-file virtual file systems include emulators, such as PCTask and WinUAE, which encapsulate not only the filesystem data but also emulated disk layout. This makes it easy to treat an OS installation like any other piece of software—transferring it with removable media or over the network.

#### PCTask

The Amiga emulator PCTask emulated an Intel PC 8088 based machine clocked at 4.77MHz (and later an 80486SX clocked at 25 MHz). Users of PCTask could create a file of large size on the Amiga filesystem, and this file would be virtually accessed from the emulator as if it were a real PC Hard Disk. The file could be formatted with the FAT16 filesystem to store normal MS-DOS or Windows files.[1][2]

#### WinUAE

The UAE for Windows, WinUAE, allows for large single files on Windows to be treated as Amiga file systems. In WinUAE this file is called a *hardfile*.[3]

UAE could also treat a directory on the host filesystem (Windows, Linux, macOS, AmigaOS) as an Amiga filesystem.[4]

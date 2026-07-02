---
title: "Filesystem Hierarchy Standard"
source: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
domain: posix-standard
license: CC-BY-SA-4.0
tags: posix, single unix specification, posix library, filesystem hierarchy standard
fetched: 2026-07-02
---

# Filesystem Hierarchy Standard

The **Filesystem Hierarchy Standard** (**FHS**) is a reference describing the conventions used for the layout of Unix-like systems. It has been made popular by its use in Linux distributions, but it is used by other Unix-like systems as well. The latest version of the standard, version 3.0, was originally released on 3 June 2015 by the Linux Foundation. It was republished on 6 November 2025 by FreeDesktop, which has since assumed maintenance of the specification.

## Directory structure

In the FHS, all files and directories appear under the root directory `/`, even if they are stored on different physical or virtual devices. Some of these directories only exist in a particular system if certain subsystems, such as the X Window System, are installed.

Most of these directories exist in all Unix-like operating systems and are generally used in much the same way; however, the descriptions here are those used specifically for the FHS and are not considered authoritative for platforms other than Linux.

| Directory | Description |
|---|---|
| `/` | *Primary hierarchy* root and root directory of the entire file system hierarchy. |
| `/bin` | Essential command binaries that need to be available in single-user mode, including to bring up the system or repair it, for all users (e.g., cat, ls, cp). |
| `/boot` | Boot loader files (e.g., kernels, initrd). |
| `/dev` | Device files (e.g., `/dev/null`, `/dev/disk0`, `/dev/sda1`, `/dev/tty`, `/dev/random`). |
| `/etc` | Host-specific system-wide configuration files. There has been controversy over the meaning of the name itself. In early versions of the UNIX Implementation Document from Bell Labs, `/etc` is referred to as the *etcetera directory*, as this directory historically held everything that did not belong elsewhere (however, the FHS restricts `/etc` to static configuration files and may not contain binaries). Since the publication of early documentation, the directory name has been re-explained in various ways. Later interpretations include backronyms such as "Editable Text Configuration" or "Extended Tool Chest". |
| `/etc/opt` | Configuration files for add-on packages stored in `/opt`. |
| `/etc/sgml` | Configuration files, such as catalogs, for software that processes SGML. |
| `/etc/X11` | Configuration files for the X Window System, version 11. |
| `/etc/xml` | Configuration files, such as catalogs, for software that processes XML. |
| `/home` | Users' home directories, containing saved files, personal settings, etc. |
| `/lib` | Libraries essential for the binaries in `/bin` and `/sbin`. |
| `/lib<qual>` | Alternate format essential libraries. These are typically used on systems that support more than one executable code format, such as systems supporting 32-bit and 64-bit versions of an instruction set. Such directories are optional, but if they exist, they have some requirements. |
| `/media` | Mount points for removable media such as CD-ROMs (appeared in FHS-2.3 in 2004). |
| `/mnt` | Temporarily mounted filesystems. |
| `/opt` | Add-on application software packages. |
| `/proc` | Virtual filesystem providing process and kernel information as files. In Linux, corresponds to a procfs mount. Generally, automatically generated and populated by the system, on the fly. |
| `/root` | Home directory for the root user. |
| `/run` | Run-time variable data: Information about the running system since last boot, e.g., currently logged-in users and running daemons. Files under this directory must be either removed or truncated at the beginning of the boot process, but this is not necessary on systems that provide this directory as a temporary filesystem (tmpfs) (appeared in FHS-3.0 in 2015). |
| `/sbin` | Essential system binaries (e.g., fsck, init, route). |
| `/srv` | Site-specific data served by this system, such as data and scripts for web servers, data offered by FTP servers, and repositories for version control systems (appeared in FHS-2.3 in 2004). |
| `/sys` | Contains information about devices, drivers, and some kernel features. |
| `/tmp` | Directory for temporary files (see also `/var/tmp`). Often not preserved between system reboots and may be severely size-restricted. |
| `/usr` | *Secondary hierarchy* for read-only user data; contains the majority of (multi-)user utilities and applications. Should be shareable and read-only. |
| `/usr/bin` | Non-essential command binaries (not needed in single-user mode); for all users. |
| `/usr/include` | Standard include files. |
| `/usr/lib` | Libraries for the binaries in `/usr/bin` and `/usr/sbin`. |
| `/usr/libexec` | Binaries run by other programs that are not intended to be executed directly by users or shell scripts (optional). |
| `/usr/lib<qual>` | Alternative-format libraries (e.g., `/usr/lib32` for 32-bit libraries on a 64-bit machine (optional)). |
| `/usr/local` | *Tertiary hierarchy* for local data, specific to this host. Typically has further subdirectories (e.g., `bin`, `lib`, `share`). |
| `/usr/sbin` | Non-essential system binaries (e.g., daemons for various network services). |
| `/usr/share` | Architecture-independent (shared) data. |
| `/usr/src` | Source code (e.g., the kernel source code with its header files). |
| `/usr/X11R6` | X Window System, Version 11, Release 6 (up to FHS-2.3, optional). |
| `/var` | Variable files: files whose content is expected to continually change during normal operation of the system, such as logs, spool files, and temporary e-mail files. |
| `/var/cache` | Application cache data. Such data are locally generated as a result of time-consuming I/O or calculation. The application must be able to regenerate or restore the data. The cached files can be deleted without loss of data. |
| `/var/lib` | State information. Persistent data modified by programs as they run (e.g., databases, packaging system metadata, etc.). |
| `/var/lock` | Lock files. Files keeping track of resources currently in use. |
| `/var/log` | Log files. Various logs. |
| `/var/mail` | Mailbox files. In some distributions, these files may be located in the deprecated `/var/spool/mail`. |
| `/var/opt` | Variable data from add-on packages that are stored in `/opt`. |
| `/var/run` | Run-time variable data. This directory contains system information data describing the system since it was booted. In FHS 3.0, `/var/run` is replaced by `/run`; a system should either continue to provide a `/var/run` directory or provide a symbolic link from `/var/run` to `/run` for backward compatibility. |
| `/var/spool` | Spool for tasks waiting to be processed (e.g., print queues and outgoing mail queue). Formerly also contained user mailbox files at `/var/spool/mail`. |
| `/var/tmp` | Temporary files to be preserved between reboots. |

## FHS compliance

Most Linux distributions follow the Filesystem Hierarchy Standard and declare it their own policy to maintain FHS compliance. GoboLinux and NixOS provide examples of intentionally non-compliant filesystem implementations.

Some distributions generally follow the standard but deviate from it in some areas. The FHS is a "trailing standard", and so documents common practices at a point in time. Of course, times change, and distribution goals and needs call for experimentation. Some common deviations include:

- Modern Linux distributions include a `/sys` directory as a virtual filesystem (sysfs, comparable to `/proc`, which is a procfs), which stores and allows modification of the devices connected to the system, whereas many traditional Unix-like operating systems use `/sys` as a symbolic link to the kernel source tree.
- Many modern Unix-like systems (such as FreeBSD and OpenBSD) via their ports systems install third-party packages into `/usr/local`, while keeping code considered part of the operating system in `/usr`.
- Some Linux distributions no longer differentiate between `/lib` and `/usr/lib` and have `/lib` symlinked to `/usr/lib`.
- Some Linux distributions no longer differentiate between `/bin` and `/usr/bin` and between `/sbin` and `/usr/sbin`. They may symlink `/bin` to `/usr/bin` and `/sbin` to `/usr/sbin`. Other distributions choose to consolidate all four, symlinking them to `/usr/bin`.

Modern Linux distributions include a `/run` directory as a temporary filesystem (tmpfs), which stores volatile runtime data, following the FHS version 3.0. According to the FHS version 2.3, such data were stored in `/var/run`, but this was a problem in some cases because this directory is not always available at early boot. As a result, these programs have had to resort to workarounds, such as using `/dev/.udev`, `/dev/.mdadm`, `/dev/.systemd` or `/dev/.mount` directories, even though the device directory is not intended for such data. Among other advantages, this makes the system easier to use normally with the root filesystem mounted read-only. For example, below are the changes Debian made in its 2013 Wheezy release:

- `/dev/.*` → `/run/*`
- `/dev/shm` → `/run/shm`
- `/dev/shm/*` → `/run/*`
- `/etc/*` (writeable files) → `/run/*`
- `/lib/init/rw` → `/run`
- `/var/lock` → `/run/lock`
- `/var/run` → `/run`
- `/tmp` → `/run/tmp`

## History

FHS was created as the FSSTND (short for "Filesystem Standard"), largely based on similar standards for other Unix-like operating systems, such as the Version 7 Unix hier(7) from 1979, the SunOS 4.x filesystem(7) and its successor, the Solaris filesystem(7), and the FreeBSD hier(7).

### Release history

| Version | Release date | Notes |
|---|---|---|
| Unsupported: 1.0 | 1994-02-14 | FSSTND |
| Unsupported: 1.1 | 1994-10-09 | FSSTND |
| Unsupported: 1.2 | 1995-03-28 | FSSTND |
| Unsupported: 2.0 | 1997-10-26 | FHS 2.0 is the direct successor for FSSTND 1.2. Name of the standard was changed to Filesystem Hierarchy Standard. |
| Unsupported: 2.1 | 2000-04-12 | FHS |
| Unsupported: 2.2 | 2001-05-23 | FHS |
| Unsupported: 2.3 | 2004-01-29 | FHS |
| Latest version: 3.0 | 2015-05-18 | FHS |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |

---
title: "init"
source: https://en.wikipedia.org/wiki/Init
domain: init-systems
license: CC-BY-SA-4.0
tags: init system, systemd manager, sysvinit scripts, process identifier
fetched: 2026-07-02
---

# init

In Unix-like computer operating systems, **init** (short for *initialization*) is the first user-space process started during booting of the operating system. Init is a daemon process that continues running until the system is shut down. It is the direct or indirect ancestor of all other processes and automatically adopts all orphaned processes. Init is started by the kernel during the booting process; in most Unix-like systems, a kernel panic will occur if the kernel is unable to start it or if it dies for any reason. Init is typically assigned process identifier 1.

In Unix systems such as System III and System V, the design of init diverged from the functionality provided by the init in Research Unix and its BSD derivatives. Up until the early 2010s, most Linux distributions employed a traditional init that was somewhat compatible with System V, while some distributions such as Slackware use BSD-style startup scripts, and other distributions such as Gentoo have their own customized versions.

Since then, most Linux distributions have employed a more modern init system, with most employing the init provided by the systemd project. Some distributions have elected to create their own System V-init compatible system, such as Gentoo Linux's OpenRC and Void Linux's runit. These projects typically include features originally not in System V's init, such as multi-threading or interactive init. Most modern init systems are also able to dynamically start, stop and enable services after boot with prompting by the user.

## Research Unix-style/BSD-style

Research Unix init runs the initialization shell script located at `/etc/rc`, then launches getty on terminals under the control of `/etc/ttys`. There are no runlevels; the `/etc/rc` file determines what programs are run by init. The advantage of this system is that it is simple and easy to edit manually. However, new software added to the system may require changes to existing files that risk producing an unbootable system.

BSD init was, prior to 4.3BSD, the same as Research UNIX's init; in 4.3BSD, it added support for running a windowing system such as X on graphical terminals under the control of `/etc/ttys`. To remove the requirement to edit `/etc/rc`, BSD variants have long supported a site-specific `/etc/rc.local` file that is run in a sub-shell near the end of the boot sequence.

A fully modular system was introduced with NetBSD 1.5 and ported to FreeBSD 5.0, OpenBSD 4.9 and successors. This system executes scripts in the `/etc/rc.d` directory. Unlike System V's script ordering, which is derived from the filename of each script, this system uses explicit dependency tags placed within each script. The order in which scripts are executed is determined by the *rcorder* utility based on the requirements stated in these tags.

## SysV-style

When compared to its predecessors, AT&T's UNIX System III introduced a new style of system startup configuration, which survived (with modifications) into UNIX System V and is therefore called the "SysV-style init".

At any moment, a running System V is in one of the predetermined number of states, called *runlevels*. At least one runlevel is the normal operating state of the system; typically, other runlevels represent single-user mode (used for repairing a faulty system), system shutdown, and various other states. Switching from one runlevel to another causes a per-runlevel set of scripts to be run, which typically mount filesystems, start or stop daemons, start or stop the X Window System, shutdown the machine, etc.

### Runlevels

The runlevels in System V describe certain states of a machine, characterized by the processes and daemons running in each of them. In general, there are seven runlevels, out of which three runlevels are considered "standard", as they are essential to the operation of a system:

1. Turn off
2. Single-user mode (also known as *S* or *s*)
3. Reboot

Aside from these standard ones, Unix and Unix-like systems treat runlevels somewhat differently. The common denominator, the `/etc/inittab` file, defines what each configured runlevel does in a given system.

### Default runlevels

| Operating system | Default runlevel |
|---|---|
| AIX | 2 |
| antiX | 5 |
| Gentoo Linux | 3 |
| HP-UX | 3 (console/server/multiuser) or 4 (graphical) |
| Slackware Linux | 3 |
| Solaris / illumos | 3 |
| UNIX System V Releases 3.x, 4.x | 2 |
| UnixWare 7.x | 3 |

On Linux distributions defaulting to runlevel 5 in the table on the right, runlevel 5 invokes a multiuser graphical environment running the X Window System, usually with a display manager like GDM or KDM. However, the Solaris and illumos operating systems typically reserve runlevel 5 to shut down and automatically power off the machine.

On most systems, all users can check the current runlevel with either the `runlevel` or `who -r` command. The root user typically changes the current runlevel by running the `telinit` or `init` commands. The `/etc/inittab` file sets the default runlevel with the `:initdefault:` entry.

On Unix systems, changing the runlevel is achieved by starting only the missing services (as each level defines only those that are started / stopped). For example, changing a system from runlevel 3 to 4 might only start the local X server. Going back to runlevel 3, it would be stopped again.

## Other implementations

Traditionally, one of the major drawbacks of init is that it starts tasks serially, waiting for each to finish loading before moving on to the next. When startup processes end up Input/output (I/O) blocked, this can result in long delays during boot. Speeding up I/O, e.g. by using SSDs, may shorten the delays but it does not address the root cause.

Various efforts have been made to replace the traditional init daemons to address this and other design problems, including:

### General

| Name | Developer | Latest release | License | Notes |   |
|---|---|---|---|---|---|
| Version | Date |   |   |   |   |
| BootScripts | GoboLinux Scripts Contributors | 016.02 | August 16, 2017; 8 years ago | GPL |   |
| busybox-init | Bruce Perens etc. | 1.36.1 (Edit this on Wikidata) | 19 May 2023; 3 years ago | GPL-2.0-only Since 1.3.0 GPL-2.0-or-later Until 1.2.2.1 |   |
| dinit | Davin McCall | 0.21.0 (Edit this on Wikidata) | 9 March 2026; 3 months ago | AL2 |   |
| Epoch | Epoch Contributors | 1.3.0 | June 24, 2015; 11 years ago | Unlicense |   |
| finit | Joachim Wiberg, etc. | 4.16 | February 27, 2026; 4 months ago | MIT |   |
| ginitd | S. M. Wood-Mattheusson |   |   |   |   |
| Initng | Initng Contributors | 0.6.10.2 | March 25, 2007; 19 years ago | GPL-3.0 |   |
| launchd | Apple Inc. | 10.4 | April 29, 2005; 21 years ago | Proprietary (was APSL then AL2) |   |
| OpenRC | OpenRC Developers | 0.63.2 (Edit this on Wikidata) | 13 June 2026; 14 days ago | BSD-2-Clause |   |
| procd | Daniel Golle, etc. |   | March 25, 2026; 3 months ago | GPL-2.0-only |   |
| runit | Gerrit Pape, runit Developers | 2.3.1 (Edit this on Wikidata) | 7 February 2026; 4 months ago | BSD-3-Clause |   |
| Service Management Facility (SMF) | Sun Microsystems | 5.10 | January 31, 2005; 21 years ago | CDDL |   |
| Shepherd | Ludovic Courtès (Edit this on Wikidata)etc. | 1.0.9 (Edit this on Wikidata) | 3 December 2025; 6 months ago | GPL-3.0-or-later |   |
| s6 | Laurent Bercot | 2.14.0.1 (Edit this on Wikidata) | 24 January 2026; 5 months ago | ISC |   |
| systemd | Red Hat345 in 20182,032 total | 261.1 (Edit this on Wikidata) | 26 June 2026; 24 hours ago | LGPL-2.1-or-later |   |
| SystemStarter | Wilfredo Sanchez | 10.4 | April 29, 2005; 21 years ago | BSD |   |
| Upstart | Canonical Ltd. | 1.13.2 | September 4, 2014; 11 years ago | GPL-2.0-only |   |
| Name | Developer | Latest release | License | Notes |   |
| Version | Date |   |   |   |   |

1. BootScripts in GoboLinux
2. busybox-init, suited to embedded operating systems, used by Alpine Linux (before being replaced with OpenRC), SliTaz 5 (Rolling), Tiny Core Linux, and VMware ESXi, and used by OpenWrt before it was replaced with procd
3. dinit, a service manager and init system.
4. Epoch, a single-threaded Linux init system focused on simplicity and service management
5. ginitd, a software package that consists of an init system and a service management system
6. Initng, a full replacement of init designed to start processes asynchronously
7. launchd, a replacement for init in Darwin and Darwin-based operating systems such as macOS and iOS starting with Mac OS X v10.4 (it launches SystemStarter to run old-style 'rc.local' and SystemStarter processes)
8. OpenRC, a process spawner that utilizes system-provided init, while providing process isolation, parallelized startup, and service dependency; used by Alpine Linux, Gentoo and its derivatives, and available as an option in Devuan and Artix Linux.
9. runit, a cross-platform full replacement for init with parallel starting of services, used by default in Void Linux
10. Service Management Facility (SMF), a complete replacement/redesign of init from the ground up in illumos/Solaris starting with Solaris 10, but launched as the only service by the original System V-style init
11. Shepherd, the GNU service and daemon manager which provides asynchronous, dependency-based initialisation; written in Guile Scheme and meant to be interactively hackable during normal system operation
12. s6, a software suite that includes an init system
13. systemd, a software suite, full replacement for init in Linux that includes an init daemon, with concurrent starting of services, service manager, and other features. Used by Debian (replaces SysV init) and Ubuntu, among other popular Linux distributions. As of February 2019, systemd has been adopted by most major Linux distributions.
14. SystemStarter, a process spawner started by the BSD-style init in Mac OS X prior to Mac OS X v10.4
15. Upstart, a full replacement of init designed to start processes asynchronously. Initiated by Ubuntu and used by them until 2014. It was also used in Fedora 9, Red Hat Enterprise Linux 6 and Google's ChromeOS.

### Operating system support

| Name | Linux | BSD | Darwin | Other |
|---|---|---|---|---|
| BootScripts | Yes | No | No | No |
| busybox-init | Yes | No | No | No |
| dinit | Yes | Yes | Yes | No |
| Epoch | Yes | No | No | No |
| finit | Yes | No | No | No |
| Initng | Yes | No | No | No |
| launchd | No | No | Yes | No |
| OpenRC | Yes | Yes | No | No |
| procd | Yes | No | No | No |
| runit | Yes | Yes | Yes | No |
| Service Management Facility (SMF) | No | No | No | Solaris |
| Shepherd | Yes | No | No | GNU Hurd |
| s6 | Yes | Yes | Yes | No |
| systemd | Yes | No | No | No |
| SystemStarter | No | No | Yes | No |
| Upstart | Yes | No | No | No |
| Name | Linux | BSD | Darwin | Other |

### Compatibility, interface and programming

Comparison of init systems

Name

musl

libc

compatible

dependency

free

script

/

service

format

Plain

log

format

Per-

service

config

Cross-

service

events

Parallel

service

startup

Process

supervision

Programming language

Codebase

size

(lines)

BootScripts

?

?

Shell

scripts

?

?

?

?

?

Shell 66.6%; C 19.0%; Python 12.7%; Other 1.7%

?

busybox-init

?

?

?

?

?

?

?

?

C 90.4%; shell script 4.6%; C++ 1.7%; HTML 1.4%; Assembly 0.8%; Make 0.5%; XML 0.2%; Perl 0.3%; Python 0.1%

319,897

dinit

Yes

Yes

Text

config

Yes

Yes

Yes

Yes

Native

C++ 96.1%; Starlark 1.0%; C 1.0%; Shell 0.9%; Makefile 0.7%; Zig 0.2%; Go 0.1%

~25,000

Epoch

Yes

libc,

/bin/sh

multiple

or single

.conf

Yes

Yes

(v1.1+)

(basic

support,

v1.3+)

No

Yes

C 98.2%; shell script 1.8%; Make 0.1%

10,546

finit

?

?

multiple

or single

.conf

Yes

?

?

Yes

Yes

C 86.7%; shell script 9.7%; Automake 1.8%; Autoconf 1.5%; Make 0.3%

33,034

Initng

?

?

?

?

?

?

?

?

C 67.5%; Assembly 12.8%; shell script 13.2%; Python 2.7%; CMake 1.5%; Jam 1.1%; HTML 0.6%; Make 0.5%; Vim Script 0.1%

59,471

launchd

?

Yes

plist

?

Yes

No

Yes

Yes

C 96.1%; shell script 2.2%; C++ 1.3%; Make 0.4%; XML 0.1%

28,128

OpenRC

Yes

init

(sysv or BSD)

Shell

scripts

Yes

Yes

(conf.d)

Yes

Disabled

by

default

Via

external

tool

C 87.6%; shell script 12.2%; Perl 0.2%

23,827

procd

?

?

Shell

scripts

?

Yes

?

?

Yes

C 98.8%; CMake 0.8%; shell script 0.4%

18,832

runit

Yes

Yes

Shell

scripts

Yes

No

Yes

Via

supervision

trees

Native

C 57.4%; HTML 32.1%; shell script 6.3%; Make 4.0%; XML 0.2%

11,616

Service Management Facility

(SMF)

?

init

(sysv?)

XML

(+ shell

scripts)

Yes

Yes

(service

instances)

Yes

Yes

Yes

C

Shepherd

?

?

?

?

?

?

?

?

Scheme 70.5%; shell script 28.3%; Automake 0.7%; Autoconf 0.4%

6,606

s6

Yes

execline

execline/

shell

Yes

No

Yes

Yes

Native

C 48.3%; HTML 46.1%; shell script 2.8%; Autoconf 2.0%; Make 0.7%; Emacs Lisp 0.1%

31,069

systemd

Limited

dbus

udev

dns

ntp

GNOME

NetworkManager

PipeWire

...

Unit files

No

(journald)

Yes

Yes

Yes

Built-in

but

opaque

C 77.9%; XML 12.5%; shell script 3.9%; Python 3.2%; C++ 2.4%; CSS 0.1%

1,310,214

Upstart

?

?

?

?

?

?

?

?

C 93.1%; Python 2.5%; Automake 1.1%; C++ 2.4%; shell script 0.3%; XML 0.3%; Autoconf 0.1%; Vim Script 0.1%

126,865

Name

musl

libc

compatible

dependency

free

script

/

service

format

Plain

log

format

Per-

service

config

Cross-

service

events

Parallel

service

startup

Process

supervision

Programming language

Codebase

size

(lines)

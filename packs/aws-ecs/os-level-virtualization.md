---
title: "OS-level virtualization"
source: https://en.wikipedia.org/wiki/OS-level_virtualization
domain: aws-ecs
license: CC-BY-SA-4.0
tags: aws ecs, elastic container service, container orchestration, cloud containers
fetched: 2026-07-02
---

# OS-level virtualization

**OS-level virtualization** is an operating system (OS) virtualization paradigm in which the kernel allows the existence of multiple isolated user space instances, including **containers** (LXC, Solaris Containers, AIX WPARs, HP-UX SRP Containers, Docker, Podman, Guix), **zones** (Solaris Containers), **virtual private servers** (OpenVZ), **partitions**, **virtual environments** (**VEs**), **virtual kernels** (DragonFly BSD), and **jails** (FreeBSD jail and chroot). Such instances may look like real computers from the point of view of programs running in them. A computer program running on an ordinary operating system can see all resources (connected devices, files and folders, network shares, CPU power, quantifiable hardware capabilities) of that computer. Programs running inside a container can only see the container's contents and devices assigned to the container.

On Unix-like operating systems, this feature can be seen as an advanced implementation of the standard chroot mechanism, which changes the apparent root folder for the current running process and its children. In addition to isolation mechanisms, the kernel often provides resource-management features to limit the impact of one container's activities on other containers. Linux containers are all based on the virtualization, isolation, and resource management mechanisms provided by the Linux kernel, notably Linux namespaces and cgroups.

Although the word *container* most commonly refers to OS-level virtualization, it is sometimes used to refer to fuller virtual machines operating in varying degrees of concert with the host OS, such as Microsoft's Hyper-V containers. For an overview of virtualization since 1960, see Timeline of virtualization technologies.

## Operation

On ordinary operating systems for personal computers, a computer program can see (even though it might not be able to access) all the system's resources. They include:

- Hardware capabilities that can be employed, such as the CPU and the network connection
- Data that can be read or written, such as files, folders and network shares
- Connected peripherals it can interact with, such as webcam, printer, scanner, or fax

The operating system may allow or deny access to such resources based on which program requests them and the user account in the context in which it runs. The operating system may also hide those resources, so that when the computer program enumerates them, they do not appear in the enumeration results. Nevertheless, from a programming point of view, the computer program has interacted with those resources and the operating system has managed an act of interaction.

With operating-system-virtualization, or containerization, it is possible to run programs within containers, to which only parts of these resources are allocated. A program expecting to see the whole computer, once run inside a container, can only see the allocated resources and believes them to be all that is available. Several containers can be created on each operating system, to each of which a subset of the computer's resources is allocated. Each container may contain any number of computer programs. These programs may run concurrently or separately, and may even interact with one another.

Containerization has similarities to application virtualization: In the latter, only one computer program is placed in an isolated container and the isolation applies to file system only.

## Uses

Operating-system level virtualization is commonly used in virtual hosting environments, where it is useful for securely allocating finite hardware resources among a large number of mutually-distrusting users. System administrators may also use it for consolidating server hardware by moving services on separate hosts into containers on the one server.

Operating-system level virtualization can also be used to run software created for a certain Linux distribution on another distribution, an example is Distrobox.

Other typical scenarios include separating several programs to separate containers for improved security, hardware independence, and added resource management features. The improved security provided by the use of a chroot mechanism, however, is not perfect. Operating-system-level virtualization implementations capable of live migration can also be used for dynamic load balancing of containers between nodes in a cluster.

### Overhead

Operating-system level virtualization usually imposes less overhead than full virtualization because programs in OS-level virtual partitions use the operating system's normal system call interface and do not need to be subjected to emulation or be run in an intermediate virtual machine, as is the case with full virtualization (such as VMware ESXi, QEMU, or Hyper-V) and paravirtualization (such as Xen or User-mode Linux). This form of virtualization also does not require hardware support for efficient performance.

### Flexibility

Operating-system level virtualization is not as flexible as other virtualization approaches since it cannot host a guest operating system different from the host one, or a different guest kernel. For example, with Linux, different distributions are fine, but other operating systems such as Windows cannot be hosted. Operating systems using variable input systematics are subject to limitations within the virtualized architecture. Adaptation methods including cloud-server relay analytics maintain the OS-level virtual environment within these applications.

Solaris partially overcomes the limitation described above with its branded zones feature, which provides the ability to run an environment within a container that emulates an older Solaris 8 or 9 version in a Solaris 10 host. Linux branded zones (referred to as "lx" branded zones) are also available on x86-based Solaris systems, providing a complete Linux user space and support for the execution of Linux applications; additionally, Solaris provides utilities needed to install Red Hat Enterprise Linux 3.x or CentOS 3.x Linux distributions inside "lx" zones. However, in 2010 Linux branded zones were removed from Solaris; in 2014 they were reintroduced in Illumos, which is the open source Solaris fork, supporting 32-bit Linux kernels.

### Storage

Some implementations provide file-level copy-on-write (CoW) mechanisms. (Most commonly, a standard file system is shared between partitions, and those partitions that change the files automatically create their own copies.) This is easier to back up, more space-efficient and simpler to cache than the block-level copy-on-write schemes common on whole-system virtualizers. Whole-system virtualizers, however, can work with non-native file systems and create and roll back snapshots of the entire system state.

## Implementations

### Actively Maintained / Developed Implementations

Mechanism

Operating system

License

Start of

development

Features

File system

isolation

Copy on write

Disk quotas

I/O rate

limiting

Memory limits

CPU quotas

Network

isolation

Nested

virtualization

Partition checkpointing and live migration

Root privilege isolation

chroot

Most

UNIX-like

operating systems

Varies by operating system

1982

Partial

No

No

No

No

No

No

Yes

No

No

Docker

Linux

,

Windows

x64

macOS

Apache License 2.0

2013

Yes

Yes

Partial

Yes

(since 1.10)

Yes

Yes

Yes

Yes

Only in experimental mode with

CRIU

Yes

(since 1.10)

Podman

Linux

,

Windows

,

macOS

,

FreeBSD

Apache License 2.0

2018

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

LXC

Linux

GNU GPLv2

2008

Yes

Yes

Partial

Partial

Yes

Yes

Yes

Yes

Yes

Yes

Apptainer

(fork of Singularity

)

Linux

BSD Licence

2015

Yes

Yes

Yes

No

No

No

No

No

No

Yes

OpenVZ

Linux

GNU GPLv2

2005

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Partial

Yes

Yes

Virtuozzo

Linux

,

Windows

Trialware

2000

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Partial

Yes

Yes

Solaris Containers

(Zones)

illumos

(

OpenSolaris

),

Solaris

CDDL

,

Proprietary

2004

Yes

Yes (ZFS)

Yes

Partial

Yes

Yes

Yes

Partial

Partial

Yes

FreeBSD jail

FreeBSD

,

DragonFly BSD

BSD License

2000

Yes

Yes (ZFS)

Yes

Yes

Yes

Yes

Yes

Yes

Partial

Yes

vkernel

DragonFly BSD

BSD Licence

2006

Yes

Yes

—

N/a

?

Yes

Yes

Yes

?

?

Yes

WPARs

AIX

Commercial

proprietary software

2007

Yes

No

Yes

Yes

Yes

Yes

Yes

No

Yes

?

iCore Virtual Accounts

Windows XP

Freeware

2008

Yes

No

Yes

No

No

No

No

?

No

?

Sandboxie

Windows

GNU GPLv3

2004

Yes

Yes

Partial

No

No

No

Partial

No

No

Yes

systemd-nspawn

Linux

GNU LGPLv2.1+

2010

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

?

Yes

Turbo

Windows

Freemium

2012

Yes

No

No

No

No

No

Yes

No

No

Yes

### Historical/Defunct Implementations

Mechanism

Operating system

License

Actively developed since or between

Features

File system isolation

Copy on write

Disk quotas

I/O rate limiting

Memory limits

CPU quotas

Network isolation

Nested virtualization

Partition checkpointing and live migration

Root privilege isolation

Linux-VServer

(security context)

Linux

,

Windows Server 2016

GNU GPLv2

2001-2018

Yes

Yes

Yes

Yes

Yes

Yes

Partial

?

No

Partial

lmctfy

Linux

Apache License 2.0

2013

–

2015

Yes

Yes

Yes

Yes

Yes

Yes

Partial

?

No

Partial

sysjail

OpenBSD

,

NetBSD

BSD License

2006

–

2009

Yes

No

No

No

No

No

Yes

No

No

?

rkt

(

rocket

)

Linux

Apache License 2.0

2014

–

2018

Yes

Yes

Yes

Yes

Yes

Yes

Yes

?

?

Yes

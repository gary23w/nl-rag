---
title: "Logical volume management"
source: https://en.wikipedia.org/wiki/Logical_volume_management
domain: btrfs-filesystem
license: CC-BY-SA-4.0
tags: btrfs, b-tree filesystem, filesystem snapshot, logical volume management
fetched: 2026-07-02
---

# Logical volume management

In computer storage, **logical volume management** (**LVM**) provides a method of allocating space on mass-storage devices that is more flexible than conventional partitioning schemes to store volumes. In particular, a volume manager can concatenate, stripe together or otherwise combine partitions (or block devices in general) into larger virtual partitions that administrators can re-size or move, potentially without interrupting system use.

Volume management represents just one of many forms of storage virtualization; its implementation takes place in a layer in the device-driver stack of an operating system (OS) (as opposed to within storage devices or in a network).

## Design

Most volume-manager implementations share the same basic design. They start with **physical volumes** (PVs), which can be either hard disks, hard disk partitions, or logical unit numbers (LUNs) of an external storage device. Volume management treats each PV as being composed of a sequence of chunks called **physical extents** (PEs). Some volume managers (such as that in HP-UX and Linux) have PEs of a uniform size; others (such as that in Veritas) have variably-sized PEs that can be split and merged at will.

Normally, PEs simply map one-to-one to **logical extents** (LEs). With mirroring, multiple PEs map to each LE. These PEs are drawn from a **physical volume group** (PVG), a set of same-sized PVs which act similarly to hard disks in a RAID 1 array. PVGs are usually laid out so that they reside on different disks or data buses for maximum redundancy.

The system pools LEs into a *volume group* (VG). The pooled LEs can then be concatenated together into virtual disk partitions called **logical volumes** or LVs. Systems can use LVs as raw block devices just like disk partitions: creating mountable file systems on them, or using them as swap storage.

Striped LVs allocate each successive LE from a different PV; depending on the size of the LE, this can improve performance on large sequential reads by bringing to bear the combined read-throughput of multiple PVs.

Administrators can grow LVs (by concatenating more LEs) or shrink them (by returning LEs to the pool). The concatenated LEs do not have to be contiguous. This allows LVs to grow without having to move already-allocated LEs. Some volume managers allow the re-sizing of LVs in either direction while online. Changing the size of the LV does not necessarily change the size of a file system on it; it merely changes the size of its containing space. A file system that can be resized online is recommended in that it allows the system to adjust its storage on-the-fly without interrupting applications.

PVs and LVs cannot be shared between or span different VGs (although some volume managers may allow moving them at will between VGs on the same host). This allows administrators conveniently to bring VGs online, to take them offline or to move them between host systems as a single administrative unit.

VGs can grow their storage pool by absorbing new PVs or shrink by retracting from PVs. This may involve moving already-allocated LEs out of the PV. Most volume managers can perform this movement online; if the underlying hardware is hot-pluggable this allows engineers to upgrade or replace storage without system downtime.

## Concepts

### Hybrid volume

A hybrid volume is any volume that intentionally and opaquely makes use of two separate physical volumes. For instance, a workload may consist of random seeks so an SSD may be used to permanently store frequently used or recently written data, while using higher-capacity rotational magnetic media for long-term storage of rarely needed data. On Linux, bcache or dm-cache may be used for this purpose, while Fusion Drive may be used on OS X. ZFS also implements this functionality at the file system level, by allowing administrators to configure multi-level read/write caching.

Hybrid volumes present a similar concept as hybrid drives, which also combine solid-state storage and rotational magnetic media.

### Snapshots

Some volume managers also implement snapshots by applying copy-on-write to each LE. In this scheme, the volume manager will copy the LE to a *copy-on-write table* just before it is written to. This preserves an old version of the LV, the snapshot, which may be later reconstructed by overlaying the copy-on-write table atop the current LV. Unless the volume management supports both thin provisioning and discard, once an LE in the origin volume is written to, it is permanently stored in the snapshot volume. If the snapshot volume was made smaller than its origin, which is a common practice, this may render the snapshot inoperable.

Snapshots can be useful for backing up self-consistent versions of volatile data such as table files from a busy database, or for rolling back large changes (such as an operating system upgrade) in a single operation. Snapshots have a similar effect as rendering storage quiescent, and are similar to the shadow copy (VSS) service in Microsoft Windows.

Some Linux-based Live CDs also use snapshots to simulate read-write access to a read-only optical disc.

## Implementations

Vendor

Introduced in

Volume manager

Allocate anywhere

Snapshots

RAID 0

RAID 1

RAID 5

RAID 10

Thin provisioning

Notes

IBM

AIX

3.0 (1989)

Logical Volume Manager

Yes

Yes

Yes

Yes

No

Yes

Refers to PEs as PPs (physical partitions), and to LEs as LPs (logical partitions). Does not have a copy-on-write snapshot mechanism; creates snapshots by freezing one volume of a mirror pair.

Hewlett-Packard

HP-UX

9.0

HP Logical Volume Manager

Yes

Yes

Yes

Yes

No

Yes

FreeBSD Foundation

FreeBSD

Vinum Volume Manager

Yes

Yes

Yes

Yes

Yes

Yes

The FreeBSD fast file system (UFS) supports snapshots.

FreeBSD Foundation

FreeBSD

ZFS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

A file system with integrated volume management

The NetBSD Foundation, Inc.

NetBSD

Logical Volume Manager

Yes

No

Yes

Yes

No

No

NetBSD from version 6.0 supports its own re-implementation of Linux LVM. Re-implementation is based on a BSD licensed device-mapper driver and uses a port of Linux lvm tools as the userspace part of LVM. There is no need to support RAID5 in LVM because of NetBSD superior RAIDFrame subsystem.

NetBSD

ZFS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

A file system with integrated volume management

NetBSD § 5.0

(2009)

bioctl

arcmsr

No

No

Yes

Yes

Yes

Yes

bioctl

on NetBSD can be used for both maintenance and initialisation of hardware RAID, although initialisation (through

BIOCVOLOPS

ioctl

) is only supported by a single driver as of 2019 —

arcmsr(4)

; software RAID is supported separately through

RAIDframe

and

ZFS

The OpenBSD Project

OpenBSD 4.2

(2007)

bioctl

softraid

Yes

No

Yes

Yes

Yes

Yes

bioctl

on OpenBSD can be used for maintenance of hardware RAID, as well as for both initialisation and maintenance of software RAID

Sistina

Linux

2.2

Logical Volume Manager version 1

Yes

Yes

Yes

Yes

No

No

IBM

Linux

2.4

Enterprise Volume Management System

Yes

Yes

Yes

Yes

Yes

No

Sistina

Linux

2.6 and above

Logical Volume Manager version 2

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Oracle

Linux

2.6 and above

Btrfs

Yes

Yes

Yes

Yes

Yes (not stable)

Yes

—

N/a

A file system with integrated volume management

Silicon Graphics

IRIX

or

Linux

XVM Volume Manager

Yes

Yes

Yes

Yes

Yes

Sun Microsystems

SunOS

Solaris Volume Manager

(was

Solstice DiskSuite

).

No

No

Yes

Yes

Yes

Yes

Refers to PVs as volumes (which can be combined with RAID0, RAID1 or RAID5 primitives into larger volumes), to LVs as soft partitions (which are contiguous extents placeable anywhere on volumes, but which cannot span multiple volumes), and to VGs as disk sets.

Solaris 10

ZFS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

A file system with integrated volume management

illumos

ZFS

Yes

Yes

Yes

Yes

Yes

Yes

Yes

A file system with integrated volume management

Veritas

Cross-OS

Veritas Volume Manager

(VxVM)

Yes

Yes

Yes

Yes

Yes

Yes

Refers to LVs as

volumes

, to VGs as

disk groups

; has variably-sized PEs called

subdisks

and LEs called

plexes

.

Microsoft

Windows 2000

and later NT-based operating systems

Logical Disk Manager

Yes

Yes

Yes

Yes

Yes

No

No

Does not have a concept of PEs or LEs; can only RAID0, RAID1, RAID5 or concatenate disk partitions into larger volumes; file systems must span whole volumes.

Windows 8

Storage Spaces

Yes

Yes

No

Yes

Yes

No

Yes

Higher-level logic than RAID1 and RAID5 - multiple storage spaces span multiple disks of different size, storage spaces are resilient from physical failure with either mirroring (at least 2 disks) or striped parity (at least 3 disks), disk management and data recovery is fully automatic

Windows 10

Storage Spaces

Yes

Yes

Yes

Yes

Yes

Yes

Yes

RAID 10 is called disk mirroring

Red Hat

Linux

4.14 and above

Stratis

Yes

Yes

No

No

No

No

Yes

RAID support planned in 2.0 version

Apple

Mac OS X Lion

Core Storage

Yes

No

No

No

No

No

No

Currently, it is used in Lion's implementation of

FileVault

, in order to allow for

full disk encryption

, as well as

Fusion Drive

, which is merely a multi-PV LVG.

Snapshots are handled by

Time Machine

; Software-based RAID is provided by AppleRAID. Both are separate from Core Storage.

## Disadvantages

Logical volumes can suffer from external fragmentation when the underlying storage devices do not allocate their PEs contiguously. This can reduce I/O performance on slow-seeking media such as magnetic disks and other rotational media. Volume managers that use fixed-size PEs, however, typically make PEs relatively large (for example, Linux LVM uses 4 MB by default) in order to amortize the cost of these seeks.

With implementations that are solely volume management, such as Core Storage and Linux LVM, separating and abstracting away volume management from the file system loses the ability to easily make storage decisions for particular files or directories. For example, if a certain directory (but not the entire file system) is to be permanently moved to faster storage, both the file system layout and the underlying volume management layer need to be traversed. For example, on Linux it would be needed to manually determine the offset of a file's contents within a file system and then manually *`pvmove`* the extents (along with data not related to that file) to the faster storage. Having volume and file management implemented within the same subsystem, instead of having them implemented as separate subsystems, makes the overall process theoretically simpler.

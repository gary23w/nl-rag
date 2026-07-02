---
title: "Device mapper"
source: https://en.wikipedia.org/wiki/Dm-verity
domain: dm-verity
license: CC-BY-SA-4.0
tags: device mapper verity, block device integrity verification, read only rootfs integrity, merkle tree block hashing
fetched: 2026-07-02
---

# Device mapper

(Redirected from

Dm-verity

)

The **device mapper** is a framework provided by the Linux kernel for mapping physical block devices onto higher-level *virtual block devices*. It forms the foundation of the logical volume manager (LVM), software RAIDs and dm-crypt disk encryption, and offers additional features such as file system snapshots.

Device mapper works by passing data from a virtual block device, which is provided by the device mapper itself, to another block device. Data can be also modified in transition, which is performed, for example, in the case of device mapper providing disk encryption or simulation of unreliable hardware behavior.

This article focuses on the device mapper implementation in the Linux kernel, but the device mapper functionality is also available in both NetBSD and DragonFly BSD.

## Usage

Applications (like LVM2 and Enterprise Volume Management System (EVMS)) that need to create new mapped devices talk to the device mapper via the `libdevmapper.so` shared library, which in turn issues ioctls to the `/dev/mapper/control` device node. Configuration of the device mapper can be also examined and configured interactively‍—‌or from shell scripts‍—‌by using the `dmsetup(8)` utility.

Both of these two userspace components have their source code maintained alongside the LVM2 source.

## Features

Functions provided by the device mapper include linear, striped and error *mappings,* as well as crypt and multipath *targets.* For example, two disks may be concatenated into one logical volume with a pair of *linear* mappings, one for each disk. As another example, *crypt* target encrypts the data passing through the specified device, by using the Linux kernel's Crypto API.

As of 2014, the following mapping targets are available:

- *cache* – allows creation of hybrid volumes, by using solid-state drives (SSDs) as caches for hard disk drives (HDDs)
- *clone* – will permit usage before a transfer is complete.
- *crypt* – provides data encryption, by using the Linux kernel's Crypto API
- *delay* – delays reads and/or writes to different devices (used for testing)
- *era* – behaves in a way similar to the linear target, while it keeps track of blocks that were written to within a user-defined period of time
- *error* – simulates I/O errors for all mapped blocks (used for testing)
- *flakey* – simulates periodic unreliable behaviour (used for testing)
- *linear* – maps a continuous range of blocks onto another block device
- *mirror* – maps a mirrored logical device, while providing data redundancy
- *multipath* – supports the mapping of multipathed devices, through usage of their path groups
- *raid* – offers an interface to the Linux kernel's software RAID driver (md)
- *snapshot* and *snapshot-origin* – used for creation of LVM snapshots, as part of the underlying copy-on-write scheme
- *striped* – stripes the data across physical devices, with the number of stripes and the striping chunk size as parameters
- *thin*  – allows creation of devices larger than the underlying physical device, physical space is allocated only when written to
- *zero* – an equivalent of `/dev/zero`, all reads return blocks of zeros, and writes are discarded

## Applications

Linux kernel features and projects built on top of the device mapper include the following:

- cryptsetup – utility used to conveniently setup disk encryption based on dm-crypt
- dm-crypt/LUKS – mapping target that provides volume encryption
- dm-cache – mapping target that allows creation of hybrid volumes
- dm-integrity – mapping target that provides data integrity, either using checksumming or cryptographic verification, also used with LUKS
- dm-log-writes – mapping target that uses two devices, passing through the first device and logging the write operations performed to it on the second device
- dm-verity – validates the data blocks contained in a file system against a list of cryptographic hash values, developed as part of the ChromiumOS project
- `dmraid(8)` – provides access to "fake" RAID configurations via the device mapper
- DM Multipath – provides I/O failover and load-balancing of block devices within the Linux kernel
- Docker – uses device mapper to create copy-on-write storage for software containers
- DRBD (Distributed Replicated Block Device)
- EVMS (deprecated)
- `kpartx(8)` – utility called from hotplug upon device maps creation and deletion
- LVM2 – logical volume manager for the Linux kernel
- VeraCrypt - Linux version of TrueCrypt
- VDO - Virtual Data Optimizer

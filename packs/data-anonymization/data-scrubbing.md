---
title: "Data scrubbing"
source: https://en.wikipedia.org/wiki/Data_scrubbing
domain: data-anonymization
license: CC-BY-SA-4.0
tags: data anonymization, de identification, data masking, synthetic data generation, data scrubbing
fetched: 2026-07-02
---

# Data scrubbing

**Data scrubbing** is an error correction technique that uses a background task to periodically inspect main memory or storage for errors, then corrects detected errors using redundant data in the form of different checksums or copies of data. Data scrubbing reduces the likelihood that single correctable errors will accumulate, leading to reduced risks of uncorrectable errors.

Data integrity is a high-priority concern in writing, reading, storage, transmission, or processing of data in computer operating systems and in computer storage and data transmission systems. However, only a few of the currently existing and used file systems provide sufficient protection against data corruption.

To address this issue, data scrubbing provides routine checks of all inconsistencies in data and, in general, prevention of hardware or software failure. This "scrubbing" feature occurs commonly in memory, disk arrays, file systems, or FPGAs as a mechanism of error detection and correction.

## RAID

With data scrubbing, a RAID controller may periodically read all hard disk drives in a RAID array and check for defective blocks before applications might actually access them. This reduces the probability of silent data corruption and data loss due to bit-level errors.

In Dell PowerEdge RAID environments, a feature called "patrol read" can perform data scrubbing and preventive maintenance.

In OpenBSD, the `bioctl(8)` utility allows the system administrator to control these patrol reads through the `BIOCPATROL` ioctl on the `/dev/bio` pseudo-device; as of 2019, this functionality is supported in some device drivers for LSI Logic and Dell controllers — this includes `mfi(4)` since OpenBSD 5.8 (2015) and `mfii(4)` since OpenBSD 6.4 (2018).

In FreeBSD and DragonFly BSD, patrol can be controlled through a RAID controller-specific utility `mfiutil(8)` since FreeBSD 8.0 (2009) and 7.3 (2010). The implementation from FreeBSD was used by the OpenBSD developers for adding patrol support to their generic bio(4) framework and the bioctl utility, without a need for a separate controller-specific utility.

In NetBSD in 2008, the bio(4) framework from OpenBSD was extended to feature support for consistency checks, which was implemented for `/dev/bio` pseudo-device under `BIOCSETSTATE` ioctl command, with the options being start and stop (`BIOC_SSCHECKSTART_VOL` and `BIOC_SSCHECKSTOP_VOL`, respectively); this is supported only by a single driver as of 2019 — `arcmsr(4)`.

Linux MD RAID, as a software RAID implementation, makes data consistency checks available and provides automated repairing of detected data inconsistencies. Such procedures are usually performed by setting up a weekly cron job. Maintenance is performed by issuing operations *check*, *repair*, or *idle* to each of the examined MD devices. Statuses of all performed operations, as well as general RAID statuses, are always available.

## File systems

### Btrfs

As a copy-on-write (CoW) file system for Linux, Btrfs provides fault isolation, corruption detection and correction, and file-system scrubbing. If the file system detects a checksum mismatch while reading a block, it first tries to obtain (or create) a good copy of this block from another device – if its internal mirroring or RAID techniques are in use.

Btrfs can initiate an online check of the entire file system by triggering a file system scrub job that is performed in the background. The scrub job scans the entire file system for integrity and automatically attempts to report and repair any bad blocks it finds along the way.

### ReFS

ReFS features automatic data scrubbing. Files that should not be scrubbed can be marked with the FILE_ATTRIBUTE_NO_SCRUB_DATA flag.

### ZFS

The features of ZFS, which is a combined file system and logical volume manager, include the verification against data corruption modes, continuous integrity checking, and automatic repair. Sun Microsystems designed ZFS from the ground up with a focus on data integrity and to protect the data on disks against issues such as disk firmware bugs and phantom writes (a write that never actually makes it to disk).

ZFS provides a repair utility called `scrub` that examines and repairs silent data corruption caused by data rot and other problems.

## Memory

Due to the high integration density of contemporary computer memory chips, the individual memory cell structures became small enough to be vulnerable to cosmic rays and/or alpha particle emission. The errors caused by these phenomena are called soft errors. This can be a problem for DRAM- and SRAM-based memories.

*Memory scrubbing* does error-detection and correction of bit errors in computer RAM by using ECC memory, other copies of the data, or other error-correction codes.

## FPGA

*Scrubbing* is a technique used to reprogram an FPGA. It can be used periodically to avoid the accumulation of errors without the need to find one in the configuration bitstream, thus simplifying the design.

Numerous approaches can be taken with respect to scrubbing, from simply reprogramming the FPGA to partial reconfiguration. The simplest method of scrubbing is to completely reprogram the FPGA at some periodic rate (typically 1/10 the calculated upset rate). However, the FPGA is not operational during that reprogram time, on the order of micro to milliseconds. For situations that cannot tolerate that type of interruption, partial reconfiguration is available. This technique allows the FPGA to be reprogrammed while still operational.

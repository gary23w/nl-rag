---
title: "ZFS - Wikipedia (part 2/2)"
source: https://en.wikipedia.org/wiki/ZFS
domain: zfs-filesystem
license: CC-BY-SA-4.0
tags: zfs, openzfs, raid-z, copy-on-write filesystem
fetched: 2026-07-02
part: 2/2
---

## OpenZFS and ZFS

Oracle Corporation ceased the public development of both ZFS and OpenSolaris after the acquisition of Sun in 2010. Some developers forked the last public release of OpenSolaris as the Illumos project. Because of the significant advantages present in ZFS, it has been ported to several different platforms with different features and commands. For coordinating the development efforts and to avoid fragmentation, OpenZFS was founded in 2013.

According to Matt Ahrens, one of the main architects of ZFS, over 50% of the original OpenSolaris ZFS code has been replaced in OpenZFS with community contributions as of 2019, making “Oracle ZFS” and “OpenZFS” politically and technologically incompatible.

### Commercial and open source products

- 2008: Sun shipped a line of ZFS-based 7000-series storage appliances.
- 2013: Oracle shipped ZS3 series of ZFS-based filers and seized first place in the SPC-2 benchmark with one of them.
- 2013: iXsystems ships ZFS-based NAS devices called FreeNAS, (now named TrueNAS CORE), for SOHO and TrueNAS for the enterprise.
- 2014: Netgear ships a line of ZFS-based NAS devices called ReadyDATA, designed to be used in the enterprise.
- 2015: rsync.net announces a cloud storage platform that allows customers to provision their own zpool and import and export data using zfs send and zfs receive.
- 2020: iXsystems Begins development of a ZFS-based hyperconverged software called TrueNAS SCALE, for SOHO and TrueNAS for the enterprise.

### Oracle Corporation, closed source, and forking (from 2010)

In January 2010, Oracle Corporation acquired Sun Microsystems, and quickly discontinued the OpenSolaris distribution and the open source development model. In August 2010, Oracle discontinued providing public updates to the source code of the Solaris OS/Networking repository, effectively turning Solaris 11 back into a closed source proprietary operating system.

In response to the changing landscape of Solaris and OpenSolaris, the illumos project was launched via webinar on Thursday, August 3, 2010, as a community effort of some core Solaris engineers to continue developing the open source version of Solaris, and complete the open sourcing of those parts not already open sourced by Sun. illumos was founded as a Foundation, the Illumos Foundation, incorporated in the State of California as a 501(c)6 trade association. The original plan explicitly stated that illumos would not be a distribution or a fork. However, after Oracle announced discontinuing OpenSolaris, plans were made to fork the final version of the Solaris ON, allowing illumos to evolve into an operating system of its own. As part of OpenSolaris, an open source version of ZFS was therefore integral within illumos.

ZFS was widely used within numerous platforms, as well as Solaris. Therefore, in 2013, the co-ordination of development work on the open source version of ZFS was passed to an umbrella project, *OpenZFS*. The OpenZFS framework allows any interested parties to collaboratively develop the core ZFS codebase in common, while individually maintaining any specific extra code which ZFS requires to function and integrate within their own systems.


## Version history

| Old release |
|---|
| Latest FOSS stable release |

| ZFS Filesystem Version Number | Release date | Significant changes |
|---|---|---|
| 1 | OpenSolaris Nevada build 36 | First release |
| 2 | OpenSolaris Nevada b69 | Enhanced directory entries. In particular, directory entries now store the object type. For example, file, directory, named pipe, and so on, in addition to the object number. |
| 3 | OpenSolaris Nevada b77 | Support for sharing ZFS file systems over SMB. Case insensitivity support. System attribute support. Integrated anti-virus support. |
| 4 | OpenSolaris Nevada b114 | Properties: userquota, groupquota, userused and groupused |
| 5 | OpenSolaris Nevada b137 | System attributes; symlinks are now their own object type |

| ZFS Pool Version Number | Release date | Significant changes |
|---|---|---|
| 1 | OpenSolaris Nevada b36 | First release |
| 2 | OpenSolaris Nevada b38 | Ditto Blocks |
| 3 | OpenSolaris Nevada b42 | Hot spares, double-parity RAID-Z (raidz2), improved RAID-Z accounting |
| 4 | OpenSolaris Nevada b62 | zpool history |
| 5 | OpenSolaris Nevada b62 | gzip compression for ZFS datasets |
| 6 | OpenSolaris Nevada b62 | "bootfs" pool property |
| 7 | OpenSolaris Nevada b68 | ZIL: adds the capability to specify a separate Intent Log device or devices |
| 8 | OpenSolaris Nevada b69 | ability to delegate zfs(1M) administrative tasks to ordinary users |
| 9 | OpenSolaris Nevada b77 | CIFS server support, dataset quotas |
| 10 | OpenSolaris Nevada b77 | Devices can be added to a storage pool as "cache devices" |
| 11 | OpenSolaris Nevada b94 | Improved zpool scrub / resilver performance |
| 12 | OpenSolaris Nevada b96 | Snapshot properties |
| 13 | OpenSolaris Nevada b98 | Properties: usedbysnapshots, usedbychildren, usedbyrefreservation, and usedbydataset |
| 14 | OpenSolaris Nevada b103 | passthrough-x aclinherit property support |
| 15 | OpenSolaris Nevada b114 | Properties: userquota, groupquota, usuerused and groupused; also required FS v4 |
| 16 | OpenSolaris Nevada b116 | STMF property support |
| 17 | OpenSolaris Nevada b120 | triple-parity RAID-Z |
| 18 | OpenSolaris Nevada b121 | ZFS snapshot holds |
| 19 | OpenSolaris Nevada b125 | ZFS log device removal |
| 20 | OpenSolaris Nevada b128 | zle compression algorithm that is needed to support the ZFS deduplication properties in ZFS pool version 21, which were released concurrently |
| 21 | OpenSolaris Nevada b128 | Deduplication |
| 22 | OpenSolaris Nevada b128 | zfs receive properties |
| 23 | OpenSolaris Nevada b135 | slim ZIL |
| 24 | OpenSolaris Nevada b137 | System attributes. Symlinks now their own object type. Also requires FS v5. |
| 25 | OpenSolaris Nevada b140 | Improved pool scrubbing and resilvering statistics |
| 26 | OpenSolaris Nevada b141 | Improved snapshot deletion performance |
| 27 | OpenSolaris Nevada b145 | Improved snapshot creation performance (particularly recursive snapshots) |
| 28 | OpenSolaris Nevada b147 | Multiple virtual device replacements |

*Note: The Solaris version under development by Sun since the release of Solaris 10 in 2005 was codenamed 'Nevada', and was derived from what was the OpenSolaris codebase. 'Solaris Nevada' is the codename for the next-generation Solaris OS to eventually succeed Solaris 10 and this new code was then pulled successively into new OpenSolaris 'Nevada' snapshot builds. OpenSolaris is now discontinued and OpenIndiana forked from it.* A final build (b134) of OpenSolaris was published by Oracle (2010-Nov-12) as an upgrade path to Solaris 11 Express.

### Operating system support

List of Operating Systems, distributions and add-ons that support ZFS, the zpool version it supports, and the Solaris build they are based on (if any):

| OS | Zpool version | Sun/Oracle Build # | Comments |
|---|---|---|---|
| Oracle Solaris 11.4 | 49 | 11.4.51 (11.4 SRU 51) |   |
| Oracle Solaris 11.3 | 37 | 0.5.11-0.175.3.1.0.5.0 |   |
| Oracle Solaris 10 1/13 (U11) | 32 |   |   |
| Oracle Solaris 11.2 | 35 | 0.5.11-0.175.2.0.0.42.0 |   |
| Oracle Solaris 11 2011.11 | 34 | b175 |   |
| Oracle Solaris Express 11 2010.11 | 31 | b151a | licensed for testing only |
| OpenSolaris 2009.06 | 14 | b111b |   |
| OpenSolaris (last dev) | 22 | b134 |   |
| OpenIndiana | 5000 | b147 | distribution based on illumos; creates a name clash naming their build code 'b151a' |
| Nexenta Core 3.0.1 | 26 | b134+ | GNU userland |
| NexentaStor Community 3.0.1 | 26 | b134+ | up to 18 TB, web admin |
| NexentaStor Community 3.1.0 | 28 | b134+ | GNU userland |
| NexentaStor Community 4.0 | 5000 | b134+ | up to 18 TB, web admin |
| NexentaStor Enterprise | 28 | b134 + | not free, web admin |
| GNU/kFreeBSD "Squeeze" (Unsupported) | 14 |   | Requires package "zfsutils" |
| GNU/kFreeBSD "Wheezy-9" (Unsupported) | 28 |   | Requires package "zfsutils" |
| FreeBSD | 5000 |   |   |
| zfs-fuse 0.7.2 | 23 |   | suffered from performance issues; defunct |
| ZFS on Linux 0.6.5.8 | 5000 |   | 0.6.0 release candidate has POSIX layer |
| KQ Infotech's ZFS on Linux | 28 |   | defunct; code integrated into LLNL-supported ZFS on Linux |
| BeleniX 0.8b1 | 14 | b111 | small-size live-CD distribution; once based on OpenSolaris |
| Schillix 0.7.2 | 28 | b147 | small-size live-CD distribution; as SchilliX-ON 0.8.0 based on OpenSolaris |
| StormOS "hail" |   |   | distribution once based on Nexenta Core 2.0+, Debian Linux; superseded by Dyson OS |
| Jaris |   |   | *Ja*panese Sola*ris* distribution; once based on OpenSolaris |
| MilaX 0.5 | 20 | b128a | small-size live-CD distribution; once based on OpenSolaris |
| FreeNAS 8.0.2 / 8.2 | 15 |   |   |
| FreeNAS 8.3.0 | 28 |   | based on FreeBSD 8.3 |
| FreeNAS 9.1.0+ | 5000 |   | based on FreeBSD 9.1+ |
| XigmaNAS 11.4.0.4/12.2.0.4 | 5000 |   | based on FreeBSD 11.4/12.2 |
| Korona 4.5.0 | 22 | b134 | KDE |
| EON NAS (v0.6) | 22 | b130 | embedded NAS |
| EON NAS (v1.0beta) | 28 | b151a | embedded NAS |
| napp-it | 28/5000 | Illumos/Solaris | Storage appliance; OpenIndiana (Hipster), OmniOS, Solaris 11, Linux (ZFS management) |
| OmniOS CE | 28/5000 | illumos-OmniOS branch | minimal stable/LTS storage server distribution based on Illumos, community driven |
| SmartOS | 28/5000 | Illumos b151+ | minimal live distribution based on Illumos (USB/CD boot); cloud and hypervisor use (KVM) |
| macOS 10.5, 10.6, 10.7, 10.8, 10.9 | 5000 |   | via MacZFS; superseded by OpenZFS on OS X |
| macOS 10.6, 10.7, 10.8 | 28 |   | via ZEVO; superseded by OpenZFS on OS X |
| NetBSD | 28 |   |   |
| MidnightBSD | 6 |   |   |
| Proxmox VE | 5000 |   | native support since 2014, pve.proxmox.com/wiki/ZFS_on_Linux |
| Ubuntu Linux 16.04 LTS+ | 5000 |   | native support via installable binary module, wiki.ubuntu.com/ZFS |
| ZFSGuru 10.1.100 | 5000 |   |   |

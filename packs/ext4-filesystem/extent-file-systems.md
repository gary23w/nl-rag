---
title: "Extent (file systems)"
source: https://en.wikipedia.org/wiki/Extent_(file_systems)
domain: ext4-filesystem
license: CC-BY-SA-4.0
tags: ext4, ext3 filesystem, journaling file system, inode
fetched: 2026-07-02
---

# Extent (file systems)

In computing, an **extent** is a contiguous area of storage reserved for a file in a file system, represented as a range of block numbers, or tracks on count key data devices. A file can consist of zero or more extents; one file fragment requires one extent. The direct benefit is in storing each range compactly as two numbers, instead of canonically storing every block number in the range. Also, extent allocation results in less file fragmentation.

Extent-based file systems can also eliminate most of the metadata overhead of large files that would traditionally be taken up by the block-allocation tree. But because the savings are small compared to the amount of stored data (for all file sizes in general) but make up a large portion of the metadata (for large files), the overall benefits in storage efficiency and performance are slight.

In order to resist fragmentation, several extent-based file systems do allocate-on-flush. Many modern fault-tolerant file systems also do copy-on-write, although that increases fragmentation. As a similar design, the CP/M file system uses extents as well, but those do not correspond to the definition given above. CP/M's extents appear contiguously as a single block in the combined directory/allocation table, and they do not necessarily correspond to a contiguous data area on disk.

IBM OS/360 and successors allocate files in multiples of disk tracks or cylinders. Files could originally have up to 16 extents, but this restriction has since been lifted. The initial allocation size, and the size of additional extents to be allocated if required, are specified by the user via Job Control Language. The system attempts to allocate the initial size as a contiguous area, although this may be split if contiguous space is not available.

## Adoption

The systems supporting file system extents include the following:

- APFS – Apple File System
- ASM – Automatic Storage Management – Oracle's database-oriented file system
- BFS – BeOS, Zeta and Haiku operating systems
- Btrfs – Extent-based copy-on-write (COW) file system for Linux
- EFS – Extent File System – SGI's first-generation file system for IRIX
- ext4 – Linux file system (when the configuration enables extents – the default in Linux since version 2.6.23)
- Files-11 – OpenVMS file system
- HFS and HFS Plus – Hierarchical File System – Apple Macintosh file systems
- High Performance File System (HPFS)  – on OS/2, eComStation and ArcaOS
- IceFS – IceFileSystem – optional file system for MorphOS
- JFS – Journaled File System – used by AIX, OS/2/eComStation/ArcaOS and Linux operating systems
- ISO 9660 – Extent-based file system for optical disc media
- MPE File System – the file system of the Multi-Programming Executive operating system.
- NTFS – used by Windows
- OCFS2 – Oracle Cluster File System – a shared-disk file system for Linux
- Reiser4 – Linux file system (in "extents" mode)
- SINTRAN III – file system used by early computer company Norsk Data
- UDF – Universal Disk Format – standard for optical media
- VERITAS File System – enabled via the pre-allocation API and CLI
- XFS – SGI's second-generation file system for IRIX and Linux

Adoption outside of file systems include the following:

- Microsoft SQL Server – versions support 64 KB extents consisting of eight 8 KB pages.
- Oracle Database groups blocks into extents and extents into segments.

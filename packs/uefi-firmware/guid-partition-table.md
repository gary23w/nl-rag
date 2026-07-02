---
title: "GUID Partition Table"
source: https://en.wikipedia.org/wiki/GUID_Partition_Table
domain: uefi-firmware
license: CC-BY-SA-4.0
tags: uefi firmware, bios firmware, guid partition table, system firmware
fetched: 2026-07-02
---

# GUID Partition Table

The **GUID Partition Table** (**GPT**) is a standard for the layout of partition tables of a physical computer storage device, such as a hard disk drive or solid-state drive. It is part of the Unified Extensible Firmware Interface (UEFI) standard.

It has several advantages over master boot record (MBR) partition tables, such as support for more than four primary partitions and 64-bit rather than 32-bit logical block addresses (LBA) for blocks on a storage device. The larger LBA size supports larger disks.

Some BIOSes support GPT partition tables as well as MBR partition tables, in order to support larger disks than MBR partition tables can support.

GPT uses universally unique identifiers (UUIDs), which are also known as globally unique identifiers (GUIDs), to identify partitions and partition types.

All modern personal computer operating systems support GPT. Some, including macOS and Microsoft Windows on the x86 architecture, support booting from GPT partitions only on systems with EFI firmware, but FreeBSD and most Linux distributions can boot from GPT partitions on systems with either the BIOS or the EFI firmware interface.

## History

The Master Boot Record (MBR) partitioning scheme, widely used since the early 1980s, had limitations when it came to modern hardware. The available size for block addresses and related information is limited to 32 bits. For hard disks with 512‑byte sectors, the MBR partition table entries allow a maximum size of 2 TiB (232 × 512‑bytes) or 2.20 TB (2.20 × 1012 bytes).

In the late 1990s, Intel developed a new partition table format as part of what eventually became the Unified Extensible Firmware Interface (UEFI). The GUID Partition Table is specified in chapter 5 of the UEFI 2.11 specification. GPT uses 64 bits for logical block addresses, allowing a maximum disk size of 264 sectors. For disks with 512‑byte sectors, the maximum size is 8 ZiB (264 × 512‑bytes) or 9.44 ZB (9.44 × 1021 bytes). For disks with 4,096‑byte sectors the maximum size is 64 ZiB (264 × 4,096‑bytes) or 75.6 ZB (75.6 × 1021 bytes).

In 2010, hard-disk manufacturers introduced drives with 4,096‑byte sectors (Advanced Format). For compatibility with legacy hardware and software, those drives include an emulation technology (512e) that presents 512‑byte sectors to the entity accessing the hard drive, despite their underlying 4,096‑byte physical sectors. Performance could be degraded on write operations, when the drive is forced to perform two read-modify-write operations to satisfy a single misaligned 4,096‑byte write operation. Since April 2014, enterprise-class drives without emulation technology (4K native) have been available on the market.

Readiness of the support for 4 KB logical sectors within operating systems differs among their types, vendors and versions. For example, Microsoft Windows supports 4K native drives since Windows 8 and Windows Server 2012 (both released in 2012) in UEFI.

## Features

Like MBR, GPT uses logical block addressing (LBA) in place of the historical cylinder-head-sector (CHS) addressing. The protective MBR is stored at LBA 0, and the GPT header is in LBA 1. The GPT header has a pointer to the partition table (*Partition Entry Array*), which is typically at LBA 2. Each entry in the partition table has the same size, which is 128 or 256 or 512, etc., bytes; typically this size is 128 bytes. The UEFI specification stipulates that a minimum of 16,384 bytes, regardless of sector size, are allocated for the Partition Entry Array. Thus, on a disk with 512-byte sectors, at least 32 sectors are used for the Partition Entry Array, and the first usable block is at LBA 34 or higher, while on a 4,096-byte sector disk, at least 4 sectors are used for the Partition Entry Array, and the first usable block is at LBA 6 or higher. In addition to the primary GPT header and Partition Entry Array, stored at the beginning of the disk, there is a backup GPT header and Partition Entry Array, stored at the end of the disk. The backup GPT header must be at the last block on the disk (LBA -1) and the backup Partition Entry Array is placed between the end of the last partition and the last block.

## MBR variants

### Protective MBR (LBA 0)

For limited backward compatibility, the space of the legacy Master Boot Record (MBR) is still reserved in the GPT specification, but it is now used in a way that prevents MBR-based disk utilities from misrecognizing and possibly overwriting GPT disks. This is referred to as a *protective MBR*.

A single partition of type EEh, encompassing the entire GPT drive (where "entire" actually means as much of the drive as can be represented in an MBR), is indicated and identifies it as GPT. Operating systems and tools which cannot read GPT disks will generally recognize the disk as containing one partition of unknown type and no empty space, and will typically refuse to modify the disk unless the user explicitly requests and confirms the deletion of this partition. This minimizes accidental erasures. Furthermore, GPT-aware OSes may check the protective MBR and if the enclosed partition type is not of type EEh or if there are multiple partitions defined on the target device, the OS may refuse to manipulate the partition table.

If the actual size of the disk exceeds the maximum partition size representable using the legacy 32-bit LBA entries in the MBR partition table, the recorded size of this partition is clipped at the maximum, thereby ignoring the rest of the disk. This amounts to a maximum reported size of 2 TiB, assuming a disk with 512 bytes per sector (see 512e). It would result in 16 TiB with 4 KiB sectors (4Kn), but since many older operating systems and tools are hard coded for a sector size of 512 bytes or are limited to 32-bit calculations, exceeding the 2 TiB limit could cause compatibility problems.

### Hybrid MBR (LBA 0 + GPT)

In operating systems that support GPT-based boot through BIOS services rather than EFI, the first sector may also still be used to store the first stage of the bootloader code, but modified to recognize GPT partitions. The bootloader in the MBR must not assume a sector size of 512 bytes.

## Partition table header (LBA 1)

| Offset | Length | Contents |
|---|---|---|
| 0 (0x00) | 8 bytes | Signature ("EFI PART", 45h 46h 49h 20h 50h 41h 52h 54h or 0x5452415020494645ULL on little-endian machines) |
| 8 (0x08) | 4 bytes | Revision number of header - 1.0 (00h 00h 01h 00h) for UEFI 2.10 |
| 12 (0x0C) | 4 bytes | Header size in little endian (in bytes, usually 5Ch 00h 00h 00h or 92 bytes) |
| 16 (0x10) | 4 bytes | CRC-32 of header (offset +0 to +0x5B) in little endian, with this field zeroed during calculation |
| 20 (0x14) | 4 bytes | Reserved; must be zero |
| 24 (0x18) | 8 bytes | Current LBA (location of this header copy) |
| 32 (0x20) | 8 bytes | Backup LBA (location of the other header copy) |
| 40 (0x28) | 8 bytes | First usable LBA for partitions (primary partition table last LBA + 1) |
| 48 (0x30) | 8 bytes | Last usable LBA for partitions (secondary partition table first LBA − 1) |
| 56 (0x38) | 16 bytes | Disk GUID in little endian |
| 72 (0x48) | 8 bytes | Starting LBA of array of partition entries (usually 2 for compatibility) |
| 80 (0x50) | 4 bytes | Number of partition entries in array |
| 84 (0x54) | 4 bytes | Size of a single partition entry (usually 80h or 128) |
| 88 (0x58) | 4 bytes | CRC-32 of partition entries array in little endian |
| 92 (0x5C) | * | Reserved; must be zeroes for the rest of the block (420 bytes for a sector size of 512 bytes; but can be more with larger sector sizes) |

The partition table header defines the usable blocks on the disk. It also defines the number and size of the partition entries that make up the partition table (offsets 80 and 84 in the table).

## Partition entries (LBA 2–33)

| Offset | Length | Contents |
|---|---|---|
| 0 (0x00) | 16 bytes | Partition type GUID (little endian) |
| 16 (0x10) | 16 bytes | Unique partition GUID (little endian) |
| 32 (0x20) | 8 bytes | First LBA (little endian) |
| 40 (0x28) | 8 bytes | Last LBA (inclusive, usually odd) |
| 48 (0x30) | 8 bytes | Attribute flags (e.g. bit 60 denotes read-only) |
| 56 (0x38) | 72 bytes | Partition name (36 UTF-16LE code units) |

After the primary header and before the backup header, the Partition Entry Array describes partitions, using a minimum size of 128 bytes for each entry block. The starting location of the array on disk, and the size of each entry, are given in the GPT header. The first 16 bytes of each entry designate the partition type's globally unique identifier (GUID). For example, the GUID for an EFI system partition is C12A7328-F81F-11D2-BA4B-00A0C93EC93B. The second 16 bytes are a GUID unique to the partition. Then follow the starting and ending 64 bit LBAs, partition attributes, and the 36 character (max.) Unicode partition name. As is the nature and purpose of GUIDs and as per RFC 4122, no central registry is needed to ensure the uniqueness of the GUID partition type designators.

The 64-bit partition table attributes are shared between 48-bit common attributes for all partition types, and 16-bit type-specific attributes:

| Bit | Content |
|---|---|
| 0 | Platform required (required by the computer to function properly, OEM partition for example, disk partitioning utilities must preserve the partition as is) |
| 1 | EFI firmware should ignore the content of the partition and not try to read from it |
| 2 | Legacy BIOS bootable (equivalent to *active flag* (typically bit 7 set) at offset +0h in partition entries of the MBR partition table) |
| 3–47 | Reserved for future use |
| 48–63 | Defined and used by the individual partition type |

Microsoft defines the type-specific attributes for basic data partition as:

| Bit | Content |
|---|---|
| 60 | Read-only |
| 61 | Shadow copy (of another partition) |
| 62 | Hidden |
| 63 | No drive letter (i.e. do not automount) |

Google defines the type-specific attributes for ChromeOS kernel as:

| Bit | Content |
|---|---|
| 56 | Successful boot flag |
| 55–52 | Tries remaining |
| 51–48 | Priority (15: highest, 1: lowest, 0: not bootable) |

## Operating-system support

### UNIX and Unix-like systems

| OS family | Version or edition | Platform | Read and write support | Boot support | Note |
|---|---|---|---|---|---|
| FreeBSD | Since 7.0 | IA-32, x86-64, ARM | Yes | Yes | In a hybrid configuration, both GPT and MBR partition identifiers may be used. |
| Linux | Most of the x86 Linux distributions Fedora 8+ and Ubuntu 8.04+ | IA-32, x86-64, ARM | Yes | Yes | Tools such as gdisk, GNU Parted, util-linux v2.23+ fdisk, SYSLINUX, GRUB 0.96 + patches and GRUB 2 have been GPT-enabled. Limited to 256 partitions per disk. |
| macOS | Since 10.4.0 (some features since 10.4.6) | IA-32, x86-64, PowerPC, Apple silicon | Yes | Yes | Only Intel and Apple silicon Macs can boot from GPT. |
| MidnightBSD | Since 0.4-CURRENT | IA-32, x86-64 | Yes | Yes | In a hybrid configuration, both GPT and MBR partition identifiers may be used. |
| NetBSD | Since 6.0 | IA-32, x86-64, ARM | Yes | Yes |   |
| OpenBSD | Since 5.9 | IA-32, x86-64, ARM | Yes | Yes |   |
| Solaris | Since Solaris 10 | IA-32, x86-64, SPARC | Yes | Yes |   |
| HP-UX | Since HP-UX 11.20 | IA-64 | Yes | Yes |   |

### Windows: 32-bit versions

Windows 7 and earlier do not support UEFI on 32-bit platforms, and therefore do not allow booting from GPT partitions.

| OS version | Release date | Platform | Read or write support | Boot support | Note |
|---|---|---|---|---|---|
| Windows 9x | 1995-08-24 | IA-32 | No | No |   |
| Windows XP | 2001-10-25 | IA-32 | No | No |   |
| Windows Server 2003 | 2003-04-24 | IA-32 | No | No |   |
| Windows Server 2003 SP1 | 2005-03-30 | IA-32 | Yes | No | MBR takes precedence in hybrid configuration. |
| Windows Vista | 2006-07-22 | IA-32 | Yes | No | MBR takes precedence in hybrid configuration. |
| Windows Server 2008 | 2008-02-27 | IA-32 | Yes | No | MBR takes precedence in hybrid configuration. |
| Windows 7 | 2009-10-22 | IA-32 | Yes | No | MBR takes precedence in hybrid configuration. |
| Windows 8 | 2012-08-01 | IA-32 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows 8.1 | 2013-08-27 | IA-32 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows 10 | 2015-07-29 | IA-32, ARM32 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |

### Windows: 64-bit versions

Limited to 128 partitions per disk.

| OS version | Release date | Platform | Read and write support | Boot support | Note |
|---|---|---|---|---|---|
| Windows XP 64-Bit Edition for Itanium systems, Version 2002 | 2001-10-25 | IA-64 | Yes | Yes | MBR takes precedence in hybrid configuration. |
| Windows XP 64-Bit Edition, Version 2003 | 2003-03-28 | IA-64 | Yes | Yes | MBR takes precedence in hybrid configuration. |
| Windows XP Professional x64 Edition Windows Server 2003 | 2005-04-25 | x64 | Yes | No | MBR takes precedence in hybrid configuration. |
| Windows Server 2003 | 2005-04-25 | IA-64 | Yes | Yes | MBR takes precedence in hybrid configuration. |
| Windows Vista | 2006-07-22 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2008 | 2008-02-27 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2008 | 2008-02-27 | IA-64 | Yes | Yes | MBR takes precedence in hybrid configuration. |
| Windows 7 | 2009-10-22 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2008 R2 | 2009-10-22 | IA-64 | Yes | Yes | MBR takes precedence in hybrid configuration. |
| Windows 8 Windows Server 2012 | 2012-08-01 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows 8.1 | 2013-08-27 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows 10 | 2015-07-29 | x64, ARM64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2016 | 2016-10-12 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2019 | 2018-10-02 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows Server 2022 | 2021-08-18 | x64 | Yes | Requires UEFI | MBR takes precedence in hybrid configuration. |
| Windows 11 | 2021-10-05 | x64, ARM64 | Yes | Yes | UEFI is a system requirement for Windows 11. |
| Windows Server 2025 | 2024-11-01 | x64 | Yes | Yes | UEFI is a system requirement for Windows Server 2025. |

## Partition type GUIDs

"Partition type GUID" means that each partition type is strictly identified by a GUID number unique to that type, and therefore partitions of the same type will all have the same "partition type GUID". Each partition also has a "partition unique GUID" as a separate entry, which as the name implies is a unique id for each partition.

Operating system

Partition type

Globally unique identifier (GUID)

OS-independent

Unused entry

00000000-0000-0000-0000-000000000000

MBR

partition scheme

024DEE41-33E7-11D3-9D69-0008C781F39F

EFI System partition

C12A7328-F81F-11D2-BA4B-00A0C93EC93B

BIOS boot partition

21686148-6449-6E6F-744E-656564454649

Intel Fast Flash (iFFS) partition (for Intel Rapid Start technology)

D3BFE2DE-3DAF-11DF-BA40-E3A556D89593

Sony boot partition

F4019732-066E-4E12-8273-346C5641494F

Lenovo boot partition

BFBFAFE7-A34F-448A-9A5B-6213EB736C22

Windows

Microsoft Reserved Partition

(MSR)

E3C9E316-0B5C-4DB8-817D-F92DF00215AE

Basic data partition

EBD0A0A2-B9E5-4433-87C0-68B6B72699C7

Logical Disk Manager

(LDM) metadata partition

5808C8AA-7E8F-42E0-85D2-E1E90434CFB3

Logical Disk Manager data partition

AF9B60A0-1431-4F62-BC68-3311714A69AD

Windows Recovery Environment

DE94BBA4-06D1-4D40-A16A-BFD50179D6AC

IBM General Parallel File System

(GPFS) partition

37AFFC90-EF7D-4E96-91C3-2D7AE055B174

Storage Spaces

partition

E75CAF8F-F680-4CEE-AFA3-B001E56EFC2D

Storage Replica partition

558D43C5-A1AC-43C0-AAC8-D1472B2923D1

S2D Cache

EEFF8352-DD2A-44DB-AE83-BEE1CF7481DC

S2D Cache Metadata

03AAA829-EBFC-4E7E-AAC9-C4D76C63B24B

HP-UX

Data partition

75894C1E-3AEB-11D3-B7C1-7B03A0000000

Service partition

E2A1E728-32E3-11D6-A682-7B03A0000000

Linux

Linux filesystem data

0FC63DAF-8483-4772-8E79-3D69D8477DE4

RAID partition

A19D880F-05FC-4D3B-A006-743F0F84911E

Root partition

Alpha

6523F8AE-3EB1-4E2A-A05A-18B695AE656F

ARC

D27F46ED-2919-4CB8-BD25-9531F3C16534

ARM

32‐bit

69DAD710-2CE4-4E3C-B16C-21A1D49ABED3

AArch64

B921B045-1DF0-41C3-AF44-4C6F280D3FAE

IA-64

993D8D3D-F80E-4225-855A-9DAF8ED7EA97

LoongArch

64‐bit

77055800-792C-4F94-B39A-98C91B762BB6

mips: 32‐bit

MIPS

big‐endian

E9434544-6E2C-47CC-BAE2-12D6DEAFB44C

mips64: 64‐bit

MIPS

big‐endian

D113AF76-80EF-41B4-BDB6-0CFF4D3D4A25

mipsel: 32‐bit

MIPS

little‐endian

37C58C8A-D913-4156-A25F-48B1B64E07F0

mips64el: 64‐bit

MIPS

little‐endian

700BDA43-7A34-4507-B179-EEB93D7A7CA3

PA-RISC

1AACDB3B-5444-4138-BD9E-E5C2239B2346

32‐bit

PowerPC

1DE3F1EF-FA98-47B5-8DCD-4A860A654D78

64‐bit PowerPC big‐endian

912ADE1D-A839-4913-8964-A10EEE08FBD2

64‐bit PowerPC little‐endian

C31C45E6-3F39-412E-80FB-4809C4980599

RISC-V

32‐bit

60D5A7FE-8E7D-435C-B714-3DD8162144E1

RISC-V 64‐bit

72EC70A6-CF74-40E6-BD49-4BDA08E8F224

s390

08A7ACEA-624C-4A20-91E8-6E0FA67D23F9

s390x

5EEAD9A9-FE09-4A1E-A1D7-520D00531306

TILE-Gx

C50CDD70-3862-4CC3-90E1-809A8C93EE2C

x86

44479540-F297-41B2-9AF7-D131D5F0458A

x86-64

4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709

/usr

partition

Alpha

E18CF08C-33EC-4C0D-8246-C6C6FB3DA024

ARC

7978A683-6316-4922-BBEE-38BFF5A2FECC

ARM 32‐bit

7D0359A3-02B3-4F0A-865C-654403E70625

AArch64

B0E01050-EE5F-4390-949A-9101B17104E9

IA-64

4301D2A6-4E3B-4B2A-BB94-9E0B2C4225EA

LoongArch 64‐bit

E611C702-575C-4CBE-9A46-434FA0BF7E3F

mips: 32‐bit MIPS big‐endian

773B2ABC-2A99-4398-8BF5-03BAAC40D02B

mips64: 64‐bit MIPS big‐endian

57E13958-7331-4365-8E6E-35EEEE17C61B

mipsel: 32‐bit MIPS little‐endian

0F4868E9-9952-4706-979F-3ED3A473E947

mips64el: 64‐bit MIPS little‐endian

C97C1F32-BA06-40B4-9F22-236061B08AA8

PA-RISC

DC4A4480-6917-4262-A4EC-DB9384949F25

32‐bit PowerPC

7D14FEC5-CC71-415D-9D6C-06BF0B3C3EAF

64‐bit PowerPC big‐endian

2C9739E2-F068-46B3-9FD0-01C5A9AFBCCA

64‐bit PowerPC little‐endian

15BB03AF-77E7-4D4A-B12B-C0D084F7491C

RISC-V 32‐bit

B933FB22-5C3F-4F91-AF90-E2BB0FA50702

RISC-V 64‐bit

BEAEC34B-8442-439B-A40B-984381ED097D

s390

CD0F869B-D0FB-4CA0-B141-9EA87CC78D66

s390x

8A4F5770-50AA-4ED3-874A-99B710DB6FEA

TILE-Gx

55497029-C7C1-44CC-AA39-815ED1558630

x86

75250D76-8CC6-458E-BD66-BD47CC81A812

x86-64

8484680C-9521-48C6-9C11-B0720656F69E

Root verity partition for

dm-verity

Alpha

FC56D9E9-E6E5-4C06-BE32-E74407CE09A5

ARC

24B2D975-0F97-4521-AFA1-CD531E421B8D

ARM 32‐bit

7386CDF2-203C-47A9-A498-F2ECCE45A2D6

AArch64

DF3300CE-D69F-4C92-978C-9BFB0F38D820

IA-64

86ED10D5-B607-45BB-8957-D350F23D0571

LoongArch 64‐bit

F3393B22-E9AF-4613-A948-9D3BFBD0C535

mips: 32‐bit MIPS big‐endian

7A430799-F711-4C7E-8E5B-1D685BD48607

mips64: 64‐bit MIPS big‐endian

579536F8-6A33-4055-A95A-DF2D5E2C42A8

mipsel: 32‐bit MIPS little‐endian

D7D150D2-2A04-4A33-8F12-16651205FF7B

mips64el: 64‐bit MIPS little‐endian

16B417F8-3E06-4F57-8DD2-9B5232F41AA6

PA-RISC

D212A430-FBC5-49F9-A983-A7FEEF2B8D0E

64‐bit PowerPC little‐endian

906BD944-4589-4AAE-A4E4-DD983917446A

64‐bit PowerPC big‐endian

9225A9A3-3C19-4D89-B4F6-EEFF88F17631

32‐bit PowerPC

98CFE649-1588-46DC-B2F0-ADD147424925

RISC-V 32‐bit

AE0253BE-1167-4007-AC68-43926C14C5DE

RISC-V 64‐bit

B6ED5582-440B-4209-B8DA-5FF7C419EA3D

s390

7AC63B47-B25C-463B-8DF8-B4A94E6C90E1

s390x

B325BFBE-C7BE-4AB8-8357-139E652D2F6B

TILE-Gx

966061EC-28E4-4B2E-B4A5-1F0A825A1D84

x86-64

2C7357ED-EBD2-46D9-AEC1-23D437EC2BF5

x86

D13C5D3B-B5D1-422A-B29F-9454FDC89D76

/usr

verity partition for dm-verity

Alpha

8CCE0D25-C0D0-4A44-BD87-46331BF1DF67

ARC

FCA0598C-D880-4591-8C16-4EDA05C7347C

ARM 32‐bit

C215D751-7BCD-4649-BE90-6627490A4C05

AArch64

6E11A4E7-FBCA-4DED-B9E9-E1A512BB664E

IA-64

6A491E03-3BE7-4545-8E38-83320E0EA880

LoongArch 64‐bit

F46B2C26-59AE-48F0-9106-C50ED47F673D

mips: 32‐bit MIPS big‐endian

6E5A1BC8-D223-49B7-BCA8-37A5FCCEB996

mips64: 64‐bit MIPS big‐endian

81CF9D90-7458-4DF4-8DCF-C8A3A404F09B

mipsel: 32‐bit MIPS little‐endian

46B98D8D-B55C-4E8F-AAB3-37FCA7F80752

mips64el: 64‐bit MIPS little‐endian

3C3D61FE-B5F3-414D-BB71-8739A694A4EF

PA-RISC

5843D618-EC37-48D7-9F12-CEA8E08768B2

64‐bit PowerPC little‐endian

EE2B9983-21E8-4153-86D9-B6901A54D1CE

64‐bit PowerPC big‐endian

BDB528A5-A259-475F-A87D-DA53FA736A07

32‐bit PowerPC

DF765D00-270E-49E5-BC75-F47BB2118B09

RISC-V 32‐bit

CB1EE4E3-8CD0-4136-A0A4-AA61A32E8730

RISC-V 64‐bit

8F1056BE-9B05-47C4-81D6-BE53128E5B54

s390

B663C618-E7BC-4D6D-90AA-11B756BB1797

s390x

31741CC4-1A2A-4111-A581-E00B447D2D06

TILE-Gx

2FB4BF56-07FA-42DA-8132-6B139F2026AE

x86-64

77FF5F63-E7B6-4633-ACF4-1565B864C0E6

x86

8F461B0D-14EE-4E81-9AA9-049B6FB97ABD

Root verity signature partition for dm-verity

Alpha

D46495B7-A053-414F-80F7-700C99921EF8

ARC

143A70BA-CBD3-4F06-919F-6C05683A78BC

ARM 32‐bit

42B0455F-EB11-491D-98D3-56145BA9D037

AArch64

6DB69DE6-29F4-4758-A7A5-962190F00CE3

IA-64

E98B36EE-32BA-4882-9B12-0CE14655F46A

LoongArch 64‐bit

5AFB67EB-ECC8-4F85-AE8E-AC1E7C50E7D0

mips: 32‐bit MIPS big‐endian

BBA210A2-9C5D-45EE-9E87-FF2CCBD002D0

mips64: 64‐bit MIPS big‐endian

43CE94D4-0F3D-4999-8250-B9DEAFD98E6E

mipsel: 32‐bit MIPS little‐endian

C919CC1F-4456-4EFF-918C-F75E94525CA5

mips64el: 64‐bit MIPS little‐endian

904E58EF-5C65-4A31-9C57-6AF5FC7C5DE7

PA-RISC

15DE6170-65D3-431C-916E-B0DCD8393F25

64‐bit PowerPC little‐endian

D4A236E7-E873-4C07-BF1D-BF6CF7F1C3C6

64‐bit PowerPC big‐endian

F5E2C20C-45B2-4FFA-BCE9-2A60737E1AAF

32‐bit PowerPC

1B31B5AA-ADD9-463A-B2ED-BD467FC857E7

RISC-V 32‐bit

3A112A75-8729-4380-B4CF-764D79934448

RISC-V 64‐bit

EFE0F087-EA8D-4469-821A-4C2A96A8386A

s390

3482388E-4254-435A-A241-766A065F9960

s390x

C80187A5-73A3-491A-901A-017C3FA953E9

TILE-Gx

B3671439-97B0-4A53-90F7-2D5A8F3AD47B

x86-64

41092B05-9FC8-4523-994F-2DEF0408B176

x86

5996FC05-109C-48DE-808B-23FA0830B676

/usr

verity signature partition for dm-verity

Alpha

5C6E1C76-076A-457A-A0FE-F3B4CD21CE6E

ARC

94F9A9A1-9971-427A-A400-50CB297F0F35

ARM 32‐bit

D7FF812F-37D1-4902-A810-D76BA57B975A

AArch64

C23CE4FF-44BD-4B00-B2D4-B41B3419E02A

IA-64

8DE58BC2-2A43-460D-B14E-A76E4A17B47F

LoongArch 64‐bit

B024F315-D330-444C-8461-44BBDE524E99

mips: 32‐bit MIPS big‐endian

97AE158D-F216-497B-8057-F7F905770F54

mips64: 64‐bit MIPS big‐endian

05816CE2-DD40-4AC6-A61D-37D32DC1BA7D

mipsel: 32‐bit MIPS little‐endian

3E23CA0B-A4BC-4B4E-8087-5AB6A26AA8A9

mips64el: 64‐bit MIPS little‐endian

F2C2C7EE-ADCC-4351-B5C6-EE9816B66E16

PA-RISC

450DD7D1-3224-45EC-9CF2-A43A346D71EE

64‐bit PowerPC little‐endian

C8BFBD1E-268E-4521-8BBA-BF314C399557

64‐bit PowerPC big‐endian

0B888863-D7F8-4D9E-9766-239FCE4D58AF

32‐bit PowerPC

7007891D-D371-4A80-86A4-5CB875B9302E

RISC-V 32‐bit

C3836A13-3137-45BA-B583-B16C50FE5EB4

RISC-V 64‐bit

D2F9000A-7A18-453F-B5CD-4D32F77A7B32

s390

17440E4F-A8D0-467F-A46E-3912AE6EF2C5

s390x

3F324816-667B-46AE-86EE-9B0C0C6C11B4

TILE-Gx

4EDE75E2-6CCC-4CC8-B9C7-70334B087510

x86-64

E7BB33FB-06CF-4E81-8273-E543B413E2E2

x86

974A71C0-DE41-43C3-BE5D-5C5CCD1AD2C0

/boot

, as an Extended Boot Loader (XBOOTLDR) partition

BC13C2FF-59E6-4262-A352-B275FD6F7172

Swap partition

0657FD6D-A4AB-43C4-84E5-0933C84B4F4F

Logical Volume Manager

(LVM) partition

E6D6D379-F507-44C2-A23C-238F2A3DF928

/home

partition

933AC7E1-2EB4-4F13-B844-0E14E2AEF915

/srv

(server data) partition

3B8F8425-20E0-4F3B-907F-1A25A76F98E8

Per‐user home partition

773F91EF-66D4-49B5-BD83-D683BF40AD16

Plain

dm-crypt

partition

7FFEC5C9-2D00-49B7-8941-3EA10A5586B7

LUKS

partition

CA7D7CCB-63ED-4C53-861C-1742536059CC

Reserved

8DA63339-0007-60C0-C436-083AC8230908

GNU/Hurd

Linux filesystem data

0FC63DAF-8483-4772-8E79-3D69D8477DE4

Linux Swap partition

0657FD6D-A4AB-43C4-84E5-0933C84B4F4F

FreeBSD

Boot partition

83BD6B9D-7F41-11DC-BE0B-001560B84F0F

BSD disklabel

partition

516E7CB4-6ECF-11D6-8FF8-00022D09712B

Swap partition

516E7CB5-6ECF-11D6-8FF8-00022D09712B

Unix File System

(UFS) partition

516E7CB6-6ECF-11D6-8FF8-00022D09712B

Vinum volume manager

partition

516E7CB8-6ECF-11D6-8FF8-00022D09712B

ZFS

partition

516E7CBA-6ECF-11D6-8FF8-00022D09712B

nandfs partition

74BA7DD9-A689-11E1-BD04-00E081286ACF

macOS

Darwin

Hierarchical File System Plus

(HFS+) partition

48465300-0000-11AA-AA11-00306543ECAC

Apple

APFS

container

APFS

FileVault

volume container

7C3457EF-0000-11AA-AA11-00306543ECAC

Apple

UFS

container

55465300-0000-11AA-AA11-00306543ECAC

ZFS

6A898CC3-1DD2-11B2-99A6-080020736631

Apple RAID partition

52414944-0000-11AA-AA11-00306543ECAC

Apple RAID partition, offline

52414944-5F4F-11AA-AA11-00306543ECAC

Apple Boot partition (Recovery HD)

426F6F74-0000-11AA-AA11-00306543ECAC

Apple Label

4C616265-6C00-11AA-AA11-00306543ECAC

Apple TV Recovery partition

5265636F-7665-11AA-AA11-00306543ECAC

Apple

Core Storage

Container

HFS+

FileVault

volume container

53746F72-6167-11AA-AA11-00306543ECAC

Apple APFS Preboot partition

69646961-6700-11AA-AA11-00306543ECAC

Apple APFS Recovery partition

52637672-7900-11AA-AA11-00306543ECAC

Solaris

illumos

Boot partition

6A82CB45-1DD2-11B2-99A6-080020736631

Root partition

6A85CF4D-1DD2-11B2-99A6-080020736631

Swap partition

6A87C46F-1DD2-11B2-99A6-080020736631

Backup partition

6A8B642B-1DD2-11B2-99A6-080020736631

/usr

partition

6A898CC3-1DD2-11B2-99A6-080020736631

/var

partition

6A8EF2E9-1DD2-11B2-99A6-080020736631

/home

partition

6A90BA39-1DD2-11B2-99A6-080020736631

Alternate sector

6A9283A5-1DD2-11B2-99A6-080020736631

Reserved partition

6A945A3B-1DD2-11B2-99A6-080020736631

6A9630D1-1DD2-11B2-99A6-080020736631

6A980767-1DD2-11B2-99A6-080020736631

6A96237F-1DD2-11B2-99A6-080020736631

6A8D2AC7-1DD2-11B2-99A6-080020736631

NetBSD

Swap partition

49F48D32-B10E-11DC-B99B-0019D1879648

FFS

partition

49F48D5A-B10E-11DC-B99B-0019D1879648

LFS

partition

49F48D82-B10E-11DC-B99B-0019D1879648

RAID partition

49F48DAA-B10E-11DC-B99B-0019D1879648

Concatenated partition

2DB519C4-B10F-11DC-B99B-0019D1879648

Encrypted partition

2DB519EC-B10F-11DC-B99B-0019D1879648

ChromeOS

ChromeOS kernel

FE3A2A5D-4F32-41A7-B725-ACCC3285A309

ChromeOS rootfs

3CB8E202-3B7E-47DD-8A3C-7FF2A13CFCEC

ChromeOS firmware

CAB6E88E-ABF3-4102-A07A-D4BB9BE3C1D3

ChromeOS future use

2E0A753D-9E48-43B0-8337-B15192CB1B5E

ChromeOS miniOS

09845860-705F-4BB5-B16C-8A8A099CAF52

ChromeOS hibernate

3F0F8318-F146-4E6B-8222-C28C8F02E0D5

Container Linux by CoreOS

/usr partition (coreos-usr)

5DFBF5F4-2848-4BAC-AA5E-0D9A20B745A6

Resizable rootfs (coreos-resize)

3884DD41-8582-4404-B9A8-E9B84F2DF50E

OEM customizations (coreos-reserved)

C95DC21A-DF0E-4340-8D7B-26CBFA9A03E0

Root filesystem on RAID (coreos-root-raid)

BE9067B9-EA49-4F15-B4F6-F36F8C9E1818

Haiku

Haiku BFS

42465331-3BA3-10F1-802A-4861696B7521

MidnightBSD

Boot partition

85D5E45E-237C-11E1-B4B3-E89A8F7FC3A7

Data partition

85D5E45A-237C-11E1-B4B3-E89A8F7FC3A7

Swap partition

85D5E45B-237C-11E1-B4B3-E89A8F7FC3A7

Unix File System

(UFS) partition

0394EF8B-237E-11E1-B4B3-E89A8F7FC3A7

Vinum volume manager

partition

85D5E45C-237C-11E1-B4B3-E89A8F7FC3A7

ZFS

partition

85D5E45D-237C-11E1-B4B3-E89A8F7FC3A7

Ceph

Journal

45B0969E-9B03-4F30-B4C6-B4B80CEFF106

dm-crypt

journal

45B0969E-9B03-4F30-B4C6-5EC00CEFF106

OSD

4FBD7E29-9D25-41B8-AFD0-062C0CEFF05D

dm-crypt

OSD

4FBD7E29-9D25-41B8-AFD0-5EC00CEFF05D

Disk in creation

89C57F98-2FE5-4DC0-89C1-F3AD0CEFF2BE

dm-crypt

disk in creation

89C57F98-2FE5-4DC0-89C1-5EC00CEFF2BE

Block

CAFECAFE-9B03-4F30-B4C6-B4B80CEFF106

Block DB

30CD0809-C2B2-499C-8879-2D6B78529876

Block write-ahead log

5CE17FCE-4087-4169-B7FF-056CC58473F9

Lockbox for

dm-crypt

keys

FB3AABF9-D25F-47CC-BF5E-721D1816496B

Multipath OSD

4FBD7E29-8AE0-4982-BF9D-5A8D867AF560

Multipath journal

45B0969E-8AE0-4982-BF9D-5A8D867AF560

Multipath block

CAFECAFE-8AE0-4982-BF9D-5A8D867AF560

Multipath block

7F4A666A-16F3-47A2-8445-152EF4D03F6C

Multipath block DB

EC6D6385-E346-45DC-BE91-DA2A7C8B3261

Multipath block write-ahead log

01B41E1B-002A-453C-9F17-88793989FF8F

dm-crypt

block

CAFECAFE-9B03-4F30-B4C6-5EC00CEFF106

dm-crypt

block DB

93B0052D-02D9-4D8A-A43B-33A3EE4DFBC3

dm-crypt

block write-ahead log

306E8683-4FE2-4330-B7C0-00A917C16966

dm-crypt

LUKS journal

45B0969E-9B03-4F30-B4C6-35865CEFF106

dm-crypt

LUKS block

CAFECAFE-9B03-4F30-B4C6-35865CEFF106

dm-crypt

LUKS block DB

166418DA-C469-4022-ADF4-B30AFD37F176

dm-crypt

LUKS block write-ahead log

86A32090-3647-40B9-BBBD-38D8C573AA86

dm-crypt

LUKS OSD

4FBD7E29-9D25-41B8-AFD0-35865CEFF05D

OpenBSD

Data partition

824CC7A0-36A8-11E3-890A-952519AD3F61

QNX

Power-safe (QNX6) file system

CEF5A9AD-73BC-4601-89F3-CDEEEEE321A1

Plan 9

Plan 9 partition

C91818F9-8025-47AF-89D2-F030D7000C2C

VMware ESX

vmkcore (

coredump

partition)

9D275380-40AD-11DB-BF97-000C2911D1B8

VMFS

filesystem partition

AA31E02A-400F-11DB-9590-000C2911D1B8

VMware Reserved

9198EFFC-31C0-11DB-8F78-000C2911D1B8

Android-IA

Bootloader

2568845D-2332-4675-BC39-8FA5A4748D15

Bootloader2

114EAFFE-1552-4022-B26E-9B053604CF84

Boot

49A4D17F-93A3-45C1-A0DE-F50B2EBE2599

Recovery

4177C722-9E92-4AAB-8644-43502BFD5506

Misc

EF32A33B-A409-486C-9141-9FFB711F6266

Metadata

20AC26BE-20B7-11E3-84C5-6CFDB94711E9

System

38F428E6-D326-425D-9140-6E0EA133647C

Cache

A893EF21-E428-470A-9E55-0668FD91A2D9

Data

DC76DDA9-5AC1-491C-AF42-A82591580C0D

Persistent

EBC597D0-2053-4B15-8B64-E0AAC75F4DB1

Vendor

C5A0AEEC-13EA-11E5-A1B1-001E67CA0C3C

Config

BD59408B-4514-490D-BF12-9878D963F378

Factory

8F68CC74-C5E5-48DA-BE91-A0C8C15E9C80

Factory (alt)

9FDAA6EF-4B3F-40D2-BA8D-BFF16BFB887B

Fastboot / Tertiary

767941D0-2085-11E3-AD3B-6CFDB94711E9

OEM

AC6D7924-EB71-4DF8-B48D-E267B27148FF

Android 6.0+ ARM

Android Meta

19A710A2-B3CA-11E4-B026-10604B889DCF

Android EXT

193D1EA4-B3CA-11E4-B075-10604B889DCF

Open Network Install Environment (

ONIE

)

Boot

7412F7D5-A156-4B13-81DC-867174929325

Config

D4E6E2CD-4469-46F3-B5CB-1BFF57AFC149

PowerPC

PReP boot

9E1A2D38-C612-4316-AA26-8B49521E5A8B

freedesktop.org

OSes (Linux, etc.)

Shared boot loader configuration

BC13C2FF-59E6-4262-A352-B275FD6F7172

Atari TOS

Basic data partition (GEM, BGM, F32)

734E5AFE-F61A-11E6-BC64-92361F002671

Raw data partition (RAW), XHDI

35540011-B055-499F-842D-C69AECA357B7

VeraCrypt

Encrypted data partition

8C8F8EFF-AC95-4770-814A-21994F2DBC8F

OS/2

ArcaOS

Type 1

90B6FF38-B98F-4358-A21F-48F35B4A8AD3

Storage Performance Development Kit (SPDK)

SPDK block device

7C5222BD-8F5D-4087-9C00-BF9843C7B58C

barebox

bootloader

barebox-state

4778ED65-BF42-45FA-9C5B-287A1DC4AAB1

U-Boot

bootloader

U-Boot environment

3DE21764-95BD-54BD-A5C3-4ABE786F38A8

Fuchsia

standard partitions

Bootloader (slot A/B/R)

FE8A2634-5E2E-46BA-99E3-3A192091A350

Durable mutable encrypted system data

D9FD4535-106C-4CEC-8D37-DFC020CA87CB

Durable mutable bootloader data (including A/B/R metadata)

A409E16B-78AA-4ACC-995C-302352621A41

Factory-provisioned read-only system data

F95D940E-CABA-4578-9B93-BB6C90F29D3E

Factory-provisioned read-only bootloader data

10B8DBAA-D2BF-42A9-98C6-A7C5DB3701E7

Fuchsia Volume Manager

49FD7CB8-DF15-4E73-B9D9-992070127F0F

Verified boot metadata (slot A/B/R)

421A8BFC-85D9-4D85-ACDA-B64EEC0133E9

Zircon boot image (slot A/B/R)

9B37FFF6-2E58-466A-983A-F7926D0B04E0

Fuchsia

legacy partitions

fuchsia-esp

C12A7328-F81F-11D2-BA4B-00A0C93EC93B

fuchsia-system

606B000B-B7C7-4653-A7D5-B737332C899D

fuchsia-data

08185F0C-892D-428A-A789-DBEEC8F55E6A

fuchsia-install

48435546-4953-2041-494E-5354414C4C52

fuchsia-blob

2967380E-134C-4CBB-B6DA-17E7CE1CA45D

fuchsia-fvm

41D0E340-57E3-954E-8C1E-17ECAC44CFF5

Zircon boot image (slot A)

DE30CC86-1F4A-4A31-93C4-66F147D33E05

Zircon boot image (slot B)

23CC04DF-C278-4CE7-8471-897D1A4BCDF7

Zircon boot image (slot R)

A0E5CF57-2DEF-46BE-A80C-A2067C37CD49

sys-config

4E5E989E-4C86-11E8-A15B-480FCF35F8E6

factory-config

5A3A90BE-4C86-11E8-A15B-480FCF35F8E6

bootloader

5ECE94FE-4C86-11E8-A15B-480FCF35F8E6

guid-test

8B94D043-30BE-4871-9DFA-D69556E8C1F3

Verified boot metadata (slot A)

A13B4D9A-EC5F-11E8-97D8-6C3BE52705BF

Verified boot metadata (slot B)

A288ABF2-EC5F-11E8-97D8-6C3BE52705BF

Verified boot metadata (slot R)

6A2460C3-CD11-4E8B-80A8-12CCE268ED0A

misc

1D75395D-F2C6-476B-A8B7-45CC1C97B476

emmc-boot1

900B0FC5-90CD-4D4F-84F9-9F8ED579DB88

emmc-boot2

B2B2E8D1-7C10-4EBC-A2D0-4614568260AD

Minix

Minix filesystem

481B2A38-0561-420B-B72A-F1C4988EFC16

Emu68/

AmigaOS

A partition that includes

Rigid Disk Block

3F82EEBC-87C9-4097-8165-89D6540557C0

Weka NeuralMesh (Storage System)

Weka Data Partition

993EC906-B4E2-11E7-A205-A0A8CD3EA1DE

## Example

Here is an example of GUID Partition Table for a 512 GB NVM Express solid state drive as used with multi-booting configuration, containing an EFI system partition, a Microsoft Reserved Partition, three Microsoft Basic Data Partitions (one is Windows standard partition and two are hidden Windows Recovery Environment partitions), and three Linux partitions (including a swap partition):

```mw
label: gpt
label-id: 96BB56B7-AE3C-4E94-986E-10E7F3CCA80B
device: /dev/nvme0n1
unit: sectors
first-lba: 34
last-lba: 1000215182
sector-size: 512

/dev/nvme0n1p1 : start=        2048, size=      532480, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, uuid=7885D52E-0F50-4E28-B058-8DCE7B7FF921, name="EFI system partition"
/dev/nvme0n1p2 : start=      534528, size=       32768, type=E3C9E316-0B5C-4DB8-817D-F92DF00215AE, uuid=5C34D099-E77A-4B46-9662-430D33E55AFF, name="Microsoft reserved partition"
/dev/nvme0n1p3 : start=      567296, size=   419196928, type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, uuid=109218B1-3097-4635-BE5F-044E28C2BCB0, name="Basic data partition"
/dev/nvme0n1p4 : start=   419764224, size=     1669120, type=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC, uuid=527B26E5-2768-444E-AB1F-ECB28201F3C8, attrs="RequiredPartition GUID:63"
/dev/nvme0n1p5 : start=   421435392, size=   329410560, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, uuid=5C52E480-AEE7-437B-A136-53F8C946D5ED, name="Linux Stuff"
/dev/nvme0n1p6 : start=   750845952, size=   243933184, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, uuid=023F3B88-D3D9-4E39-9F50-77F242410789, name="Linux Root"
/dev/nvme0n1p7 : start=   994779136, size=     4194304, type=0657FD6D-A4AB-43C4-84E5-0933C84B4F4F, uuid=18F44D65-B28D-4871-AF02-DDBD96771460, name="Swap"
/dev/nvme0n1p8 : start=   998973440, size=     1228800, type=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC, uuid=D4A41B1A-2F28-4AE5-AC67-A2D98FB91E22, name="Basic data partition", attrs="RequiredPartition GUID:63"
```

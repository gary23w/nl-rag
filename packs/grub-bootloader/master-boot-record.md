---
title: "Master boot record"
source: https://en.wikipedia.org/wiki/Master_boot_record
domain: grub-bootloader
license: CC-BY-SA-4.0
tags: grub bootloader, boot loader, master boot record, multi-boot menu
fetched: 2026-07-02
---

# Master boot record

A **master boot record** (**MBR**) is a type of boot sector in the first block of partitioned computer mass storage devices like fixed disks or removable drives intended for use with IBM PC-compatible systems and beyond. The concept of MBRs was publicly introduced in 1983 with PC DOS 2.0.

The MBR holds the information on how the disc's sectors (A.K.A. "blocks") are divided into partitions, each partition notionally containing a file system. The MBR also contains executable code to function as a loader for the installed operating system—usually by passing control over to the loader's second stage, or in conjunction with each partition's volume boot record (VBR). This MBR code is usually referred to as a boot loader.

The organization of the partition table in the MBR limits the maximum addressable storage space of a partitioned disk to 2 TiB (232 × 512 bytes). Approaches to slightly raise this limit utilizing 32-bit arithmetic or 4096-byte sectors are not officially supported, as they fatally break compatibility with existing boot loaders, most MBR-compliant operating systems and associated system tools, and may cause serious data corruption when used outside of narrowly controlled system environments. Therefore, the MBR-based partitioning scheme has been superseded by the GUID Partition Table (GPT) scheme in almost all new computers. A GPT can coexist with an MBR in order to provide some limited form of backward compatibility for older systems.

MBRs are not present on non-partitioned media such as floppies, superfloppies or other storage devices configured to behave as such, nor are they necessarily present on drives used in non-PC platforms.

## Overview

Support for partitioned media, and thereby the master boot record (MBR), was introduced with IBM PC DOS 2.0 in March 1983 in order to support the 10 MB hard disk of the then-new IBM Personal Computer XT, still using the FAT12 file system. The original version of the MBR was written by David Litton of IBM in June 1982. The partition table supported up to four *primary partitions*. This did not change when FAT16 was introduced as a new file system with DOS 3.0. Support for an *extended partition*, a special primary partition type used as a container to hold other partitions, was added with DOS 3.2, and nested *logical drives* inside an extended partition came with DOS 3.30. Since MS-DOS, PC DOS, OS/2 and Windows were never enabled to boot off them, the MBR format and boot code remained almost unchanged in functionality (except some third-party implementations) throughout the eras of DOS and OS/2 up to 1996.

In 1996, support for logical block addressing (LBA) was introduced in Windows 95B and MS-DOS 7.10 (Not to be confused with IBM PC-DOS 7.1) in order to support disks larger than 8 GB. *Disk timestamps* were also introduced. This also reflected the idea that the MBR is meant to be operating system and file system independent. However, this design rule was partially compromised in more recent Microsoft implementations of the MBR, which enforce CHS access for FAT16B and FAT32 partition types 0x06/0x0B, whereas LBA is used for 0x0E/0x0C.

Despite sometimes poor documentation of certain intrinsic details of the MBR format (which occasionally caused compatibility problems), it has been widely adopted as a de facto industry standard, due to the broad popularity of PC-compatible computers and its semi-static nature over decades. This was even to the extent of being supported by computer operating systems for other platforms. Sometimes this was in addition to other pre-existing or cross-platform standards for bootstrapping and partitioning.

MBR partition entries and the MBR boot code used in commercial operating systems, however, are limited to 32 bits. Therefore, the maximum disk size supported on disks using 512-byte sectors (whether real or emulated) by the MBR partitioning scheme (without 32-bit arithmetic) is limited to 2 TiB. Consequently, a different partitioning scheme must be used for larger disks, as they have become widely available since 2010. The MBR partitioning scheme is therefore in the process of being superseded by the GUID Partition Table (GPT). The official approach does little more than ensuring data integrity by employing a *protective MBR*. Specifically, it does not provide backward compatibility with operating systems that do not support the GPT scheme as well. Meanwhile, multiple forms of *hybrid MBRs* have been designed and implemented by third parties in order to maintain partitions located in the first physical 2 TiB of a disk in both partitioning schemes "in parallel" and/or to allow older operating systems to boot off GPT partitions as well. The present non-standard nature of these solutions causes various compatibility problems in certain scenarios.

The MBR consists of 512 or more bytes located in the first sector of the drive.

It may contain one or more of:

- A partition table describing the partitions of a storage device. In this context the boot sector may also be called a *partition sector*.
- Bootstrap code: Instructions to identify the configured bootable partition, then load and execute its volume boot record (VBR) as a chain loader.
- Optional 32-bit *disk timestamp*.
- Optional 32-bit *disk signature*.

## Disk partitioning

IBM PC DOS 2.0 introduced the `FDISK` utility to set up and maintain MBR partitions. When a storage device has been partitioned according to this scheme, its MBR contains a partition table describing the locations, sizes, and other attributes of linear regions referred to as partitions.

The partitions themselves may also contain data to describe more complex partitioning schemes, such as extended boot records (EBRs), BSD disklabels, or Logical Disk Manager metadata partitions.

The MBR is not located in a partition; it is located at a first sector of the device (physical offset 0), preceding the first partition. (The boot sector present on a non-partitioned device or within an individual partition is called a volume boot record instead.) In cases where the computer is running a DDO BIOS overlay or boot manager, the partition table may be moved to some other physical location on the device; e.g., Ontrack Disk Manager often placed a copy of the original MBR contents in the second sector, then hid itself from any subsequently booted OS or application, so the MBR copy was treated as if it were still residing in the first sector.

### Sector layout

By convention, there are exactly four primary partition table entries in the MBR partition table scheme, although some operating systems and system tools extended this to five (Advanced Active Partitions (AAP) with PTS-DOS 6.60 and DR-DOS 7.07), eight (AST and NEC MS-DOS 3.x as well as Storage Dimensions SpeedStor), or even sixteen entries (with Ontrack Disk Manager).

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | Bootstrap code area | 446 |   |
| `0x01BE` (446) | Partition entry №1 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №2 | 16 |   |
| `0x01DE` (478) | Partition entry №3 | 16 |   |
| `0x01EE` (494) | Partition entry №4 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 446 + 4×16 + 2 | 512 |   |   |

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | Bootstrap code area (part 1) | 218 |   |
| `0x00DA` (218) | `0x0000` | *Disk timestamp* (optional; Windows 95B/98/98SE/ME (MS-DOS 7.1–8.0). Alternatively, can serve as OEM loader signature with NEWLDR) | 2 |
| `0x00DC` (220) | Original physical drive (`0x80`–`0xFF`) | 1 |   |
| `0x00DD` (221) | Seconds (0–59) | 1 |   |
| `0x00DE` (222) | Minutes (0–59) | 1 |   |
| `0x00DF` (223) | Hours (0–23) | 1 |   |
| `0x00E0` (224) | Bootstrap code area (part 2, code entry at `0x0000`) | 216 (or 222) |   |
| `0x01B8` (440) | 32-bit disk signature | *Disk signature* (optional; UEFI, Linux, Windows NT family and other OSes) | 4 |
| `0x01BC` (444) | `0x0000` (`0x5A5A` if copy-protected) | 2 |   |
| `0x01BE` (446) | Partition entry №1 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №2 | 16 |   |
| `0x01DE` (478) | Partition entry №3 | 16 |   |
| `0x01EE` (494) | Partition entry №4 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 218 + 6 + 216 + 6 + 4×16 + 2 | 512 |   |   |

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | Bootstrap code area | 428 |   |
| `0x01AC` (428) | `0x78` | *AAP signature* (optional) | 2 |
| `0x01AD` (429) | `0x56` |   |   |
| `0x01AE` (430) | AAP physical drive (`0x80`–`0xFE`; `0x00`: not used; `0x01`–`0x7F`, `0xFF`: reserved) | *AAP record* (optional) (AAP partition entry #0 with special semantics) | 1 |
| `0x01AF` (431) | CHS (start) address of AAP partition/image file or VBR/EBR | 3 |   |
| `0x01B2` (434) | Reserved for AAP partition type (`0x00` if not used) (optional) | 1 |   |
| `0x01B3` (435) | Reserved for CHS end address in AAP (optional; byte at offset `0x01B5` is also used for MBR checksum (PTS DE, BootWizard); `0x000000` if not used) | 3 |   |
| `0x01B6` (438) | Start LBA of AAP image file or VBR/EBR or relative sectors of AAP partition (copied to offset `+01Chex` in the loaded sector over the "hidden sectors" entry of a DOS 3.31 BPB (or emulation thereof) to also support EBR booting) | 4 |   |
| `0x01BA` (442) | Reserved for sectors in AAP (optional; `0x00000000` if not used) | 4 |   |
| `0x01BE` (446) | Partition entry №1 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №2 | 16 |   |
| `0x01DE` (478) | Partition entry №3 | 16 |   |
| `0x01EE` (494) | Partition entry №4 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 428 + 2 + 16 + 4×16 + 2 | 512 |   |   |

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | JMPS (`EBhex`) / NEWLDR record size (often `0x0A`/`0x16`/`0x1C` for code start at `0x000C`/`0x0018`/`0x001E`) | *NEWLDR record* (optional) | 2 |
| `0x0002` (2) | "`NEWLDR`" signature | 6 |   |
| `0x0008` (8) | LOADER physical drive and boot flag (`0x80`–`0xFE`, `0x00`–`0x7E`, `0xFF`, `0x7F`) (if not used, this and following 3 bytes must be all 0) | 1 |   |
| `0x0009` (9) | CHS address of LOADER boot sector or image file (f.e. IBMBIO.LDR) (`0x000000` if not used) | 3 |   |
| `0x000C` (12) | Allowed DL minimum, else take from partition table (`0x80`: default; `0x00`: always use DL; `0xFF`: always use table entry) | 1 |   |
| `0x000D` (13) | Reserved (default: `0x000000`) | 3 |   |
| `0x0010` (16) | LBA of LOADER boot sector or image file (optional; `0x00000000` if not used) | 4 |   |
| `0x0014` (20) | Patch offset of VBR boot unit (default `0x0000` if not used, else `0024hex` or `01FDhex`) | 2 |   |
| `0x0016` (22) | Checksum (`0x0000` if not used) | 2 |   |
| `0x0018` (24) | OEM loader signature ("`MSWIN4`" for REAL/32, see also offset `+0DAhex`, corresponds with OEM label at offset `+003hex` in VBRs (optional) | 6 |   |
| *Varies* | Bootstrap code area (code entry at `0x0000`) | *Varies* |   |
| `0x01AC` (428) | `0x78` | *AAP signature* (optional) | 2 |
| `0x01AD` (429) | `0x56` |   |   |
| `0x01AE` (430) | AAP partition entry №0 with special semantics | *AAP record* (optional) | 16 |
| `0x01BE` (446) | Partition entry №1 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №2 | 16 |   |
| `0x01DE` (478) | Partition entry №3 | 16 |   |
| `0x01EE` (494) | Partition entry №4 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 30 + 398 + 2 + 16 + 4×16 + 2 | 512 |   |   |

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | Bootstrap code area | 380 |   |
| `0x017C` (380) | `0x5A` | *AST/NEC signature* (optional; not for SpeedStor) | 2 |
| `0x017D` (381) | `0xA5` |   |   |
| `0x017E` (382) | Partition entry №8 | *AST/NEC expanded partition table* (optional; also for SpeedStor) | 16 |
| `0x018E` (398) | Partition entry №7 | 16 |   |
| `0x019E` (414) | Partition entry №6 | 16 |   |
| `0x01AE` (430) | Partition entry №5 | 16 |   |
| `0x01BE` (446) | Partition entry №4 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №3 | 16 |   |
| `0x01DE` (478) | Partition entry №2 | 16 |   |
| `0x01EE` (494) | Partition entry №1 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 380 + 2 + 4×16 + 4×16 + 2 | 512 |   |   |

| Address | Description | Size (bytes) |   |
|---|---|---|---|
| `0x0000` (0) | Bootstrap code area | 252 |   |
| `0x00FC` (252) | `0xAA` | *DM signature* (optional) | 2 |
| `0x00FD` (253) | `0x55` |   |   |
| `0x00FE` (254) | Partition entry | *DM expanded partition table* (optional) | 16 |
| `0x010E` (270) | Partition entry | 16 |   |
| `0x011E` (286) | Partition entry | 16 |   |
| `0x012E` (302) | Partition entry | 16 |   |
| `0x013E` (318) | Partition entry | 16 |   |
| `0x014E` (334) | Partition entry | 16 |   |
| `0x015E` (350) | Partition entry | 16 |   |
| `0x016E` (366) | Partition entry | 16 |   |
| `0x017E` (382) | Partition entry | 16 |   |
| `0x018E` (398) | Partition entry | 16 |   |
| `0x019E` (414) | Partition entry | 16 |   |
| `0x01AE` (430) | Partition entry | 16 |   |
| `0x01BE` (446) | Partition entry №1 | *Partition table* (for primary partitions) | 16 |
| `0x01CE` (462) | Partition entry №2 | 16 |   |
| `0x01DE` (478) | Partition entry №3 | 16 |   |
| `0x01EE` (494) | Partition entry №4 | 16 |   |
| `0x01FE` (510) | `0x55` | *Boot signature* | 2 |
| `0x01FF` (511) | `0xAA` |   |   |
| Total size: 252 + 2 + 12×16 + 4×16 + 2 | 512 |   |   |

### Partition tables entries

| Offset (bytes) | Field length | Description |   |
|---|---|---|---|
| 0x00 |   | 1 byte | Status or physical drive (bit 7 set is for active or bootable, old MBRs only accept 0x80, 0x00 means inactive, and 0x01–0x7F stand for invalid) |
| 0x01 |   | 3 bytes | CHS address of first absolute sector in partition. The format is described by three bytes, see the next three rows. |
|   | 0x01 | 1 byte | h7–0 head x x x x x x x x |
|   | 0x02 | 1 byte | c9–8 s5–0 sector in bits 5–0; bits 7–6 are high bits of cylinder x x x x x x x x |
|   | 0x03 | 1 byte | c7–0 bits 7–0 of cylinder x x x x x x x x |
| 0x04 |   | 1 byte | Partition type |
| 0x05 |   | 3 bytes | CHS address of last absolute sector in partition. The format is described by 3 bytes, see the next 3 rows. |
|   | 0x05 | 1 byte | h7–0 head x x x x x x x x |
|   | 0x06 | 1 byte | c9–8 s5–0 sector in bits 5–0; bits 7–6 are high bits of cylinder x x x x x x x x |
|   | 0x07 | 1 byte | c7–0 bits 7–0 of cylinder x x x x x x x x |
| 0x08 |   | 4 bytes | LBA of first absolute sector in the partition |
| 0x0C |   | 4 bytes | Number of sectors in partition |

An artifact of hard disk technology from the era of the PC XT, the partition table subdivides a storage medium using units of cylinders, heads, and sectors (CHS addressing). These values no longer correspond to their namesakes in modern disk drives, as well as being irrelevant in other devices such as solid-state drives, which do not physically have cylinders or heads.

In the CHS scheme, sector indices have (almost) always begun with sector 1 rather than sector 0 by convention, and due to an error in all versions of MS-DOS/PC DOS up to including 7.10, the number of heads is generally limited to 255 instead of 256. When a CHS address is too large to fit into these fields, the tuple (1023, 254, 63) is typically used today, although on older systems, and with older disk tools, the cylinder value often wrapped around modulo the CHS barrier near 8 GB, causing ambiguity and risks of data corruption. (If the situation involves a "protective" MBR on a disk with a GPT, Intel's Extensible Firmware Interface specification requires that the tuple (1023, 255, 63) be used.) The 10-bit cylinder value is recorded within two bytes in order to facilitate making calls to the original/legacy INT 13h BIOS disk access routines, where 16 bits were divided into sector and cylinder parts, and not on byte boundaries.

Due to the limits of CHS addressing, a transition was made to using LBA, or logical block addressing. Both the partition length and partition start address are sector values stored in the partition table entries as 32-bit quantities. The sector size used to be considered fixed at 512 (29) bytes, and a broad range of important components including chipsets, boot sectors, operating systems, database engines, partitioning tools, backup and file system utilities and other software had this value hard-coded. Since the end of 2009, disk drives employing 4096-byte sectors (4Kn or Advanced Format) have been available, although the size of the sector for some of these drives was still reported as 512 bytes to the host system through conversion in the hard-drive firmware and referred to as 512 emulation drives (512e).

Since block addresses and sizes are stored in the partition table of an MBR using 32 bits, the maximum size, as well as the highest start address, of a partition using drives that have 512-byte sectors (actual or emulated) cannot exceed 2 TiB−512 bytes (2199023255040 bytes or 4294967295 (232−1) sectors × 512 (29) bytes per sector). Alleviating this capacity limitation was one of the prime motivations for the development of the GPT.

Since partitioning information is stored in the MBR partition table using a beginning block address and a length, it may in theory be possible to define partitions in such a way that the allocated space for a disk with 512-byte sectors gives a total size approaching 4 TiB, if all but one partition are located below the 2 TiB limit and the last one is assigned as starting at or close to block 232−1 and specify the size as up to 232−1, thereby defining a partition that requires 33 rather than 32 bits for the sector address to be accessed. However, in practice, only certain LBA-48-enabled operating systems, including Linux, FreeBSD and Windows 7 that use 64-bit sector addresses internally actually support this. Due to code space constraints and the nature of the MBR partition table to only support 32 bits, boot sectors, even if enabled to support LBA-48 rather than LBA-28, often use 32-bit calculations, unless they are specifically designed to support the full address range of LBA-48 or are intended to run on 64-bit platforms only. Any boot code or operating system using 32-bit sector addresses internally would cause addresses to wrap around accessing this partition and thereby result in serious data corruption over all partitions.

For disks that present a sector size other than 512 bytes, such as USB external drives, there are limitations as well. A sector size of 4096 results in an eight-fold increase in the size of a partition that can be defined using MBR, allowing partitions up to 16 TiB (232 × 4096 bytes) in size. Versions of Windows more recent than Windows XP support the larger sector sizes, as well as Mac OS X, and Linux has supported larger sector sizes since 2.6.31 or 2.6.32, but issues with boot loaders, partitioning tools and computer BIOS implementations present certain limitations, since they are often hard-wired to reserve only 512 bytes for sector buffers, causing memory to become overwritten for larger sector sizes. This may cause unpredictable behaviour as well, and therefore should be avoided when compatibility and standard conformity is an issue.

Where a data storage device has been partitioned with the GPT scheme, the master boot record will still contain a partition table, but its only purpose is to indicate the existence of the GPT and to prevent utility programs that understand only the MBR partition table scheme from creating any partitions in what they would otherwise see as free space on the disk, thereby accidentally erasing the GPT.

## System bootstrapping

On IBM PC-compatible computers, the bootstrapping firmware (contained within the ROM BIOS) loads and executes the master boot record. The PC/XT (type 5160) used an Intel 8088 microprocessor. In order to remain compatible, all x86 BIOS architecture systems start with the microprocessor in an operating mode referred to as real mode. The BIOS reads the MBR from the storage device into physical memory, and then it directs the microprocessor to the start of the boot code. The BIOS will switch the processor to real mode, then begin to execute the MBR program, and so the beginning of the MBR is expected to contain real-mode machine code.

Since the BIOS bootstrap routine loads and runs exactly one sector from the physical disk, having the partition table in the MBR with the boot code simplifies the design of the MBR program. It contains a small program that loads the Volume Boot Record (VBR) of the targeted partition. Control is then passed to this code, which is responsible for loading the actual operating system. This process is known as chain loading.

Popular MBR code programs were created for booting PC DOS and MS-DOS, and similar boot code remains in wide use. These boot sectors expect the `FDISK` partition table scheme to be in use and scans the list of partitions in the MBR's embedded partition table to find the only one that is marked with the *active flag*. It then loads and runs the volume boot record (VBR) of the active partition.

There are alternative boot code implementations, some of which are installed by boot managers, which operate in a variety of ways. Some MBR code loads additional code for a boot manager from the first track of the disk, which it assumes to be "free" space that is not allocated to any disk partition, and executes it. A MBR program may interact with the user to determine which partition on which drive should boot, and may transfer control to the MBR of a different drive. Other MBR code contains a list of disk locations (often corresponding to the contents of files in a filesystem) of the remainder of the boot manager code to load and to execute. (The first relies on behavior that is not universal across all disk partitioning utilities, most notably those that read and write GPTs. The last requires that the embedded list of disk locations be updated when changes are made that would relocate the remainder of the code.)

On machines that do not use x86 processors, or on x86 machines with non-BIOS firmware such as Open Firmware or Extensible Firmware Interface (EFI) firmware, this design is unsuitable, and the MBR is not used as part of the system bootstrap. EFI firmware is instead capable of directly understanding the GPT partitioning scheme and the FAT filesystem format, and loads and runs programs held as files in the EFI System partition. The MBR will be involved only insofar as it might contain a partition table for compatibility purposes if the GPT partition table scheme has been used.

There is some MBR replacement code that emulates EFI firmware's bootstrap, which makes non-EFI machines capable of booting from disks using the GPT partitioning scheme. It detects a GPT, places the processor in the correct operating mode, and loads the EFI compatible code from disk to complete this task.

## Disk identity

In addition to the bootstrap code and a partition table, master boot records may contain a disk signature. This is a 32-bit value that is intended to identify uniquely the disk medium (as opposed to the disk unit—the two not necessarily being the same for removable hard disks).

The disk signature was introduced by Windows NT version 3.5, but it is now used by several operating systems, including the Linux kernel version 2.6 and later. Linux tools can use the NT disk signature to determine which disk the machine booted from.

Windows NT (and later Microsoft operating systems) uses the disk signature as an index to all the partitions on any disk ever connected to the computer under that OS; these signatures are kept in Windows Registry keys, primarily for storing the persistent mappings between disk partitions and drive letters. It may also be used in Windows NT BOOT.INI files (though most do not), to describe the location of bootable Windows NT (or later) partitions. One key (among many), where NT disk signatures appear in a Windows 2000/XP registry, is:

```
HKEY_LOCAL_MACHINE\SYSTEM\MountedDevices\
```

If a disk's signature stored in the MBR was A8 E1 B9 D2 (in that order) and its first partition corresponded with logical drive C: under Windows, then the `REG_BINARY` data under the key value **`\DosDevices\C:`** would be:

```
A8 E1 B9 D2 00 7E 00 00 00 00 00 00
```

The first four bytes are said disk signature. (In other keys, these bytes may appear in reverse order from that found in the MBR sector.) These are followed by eight more bytes, forming a 64-bit integer, in little-endian notation, which are used to locate the byte offset of this partition. In this case, 00 7E corresponds to the hexadecimal value 0x7E00 (32,256). Under the assumption that the drive in question reports a sector size of 512 bytes, then dividing this byte offset by 512 results in 63, which is the physical sector number (or LBA) containing the first sector of the partition (unlike the *sector count* used in the sectors value of CHS tuples, which counts from **one**, the absolute or LBA sector value starts counting from *zero*).

If this disk had another partition with the values 00 F8 93 71 02 following the disk signature (under, e.g., the key value `\DosDevices\D:`), it would begin at byte offset 0x00027193F800 (10,495,457,280), which is also the first byte of physical sector 20,498,940.

Starting with Windows Vista, the disk signature is also stored in the Boot Configuration Data (BCD) store, and the boot process depends on it. If the disk signature changes, cannot be found or has a conflict, Windows is unable to boot. Unless Windows is forced to use the overlapping part of the LBA address of the Advanced Active Partition entry as pseudo-disk signature, Windows' usage is conflictive with the Advanced Active Partition feature of PTS-DOS 7 and DR-DOS 7.07, in particular if their boot code is located outside the first 8 GB of the disk, so that LBA addressing must be used.

## Programming considerations

The MBR originated in the PC XT. IBM PC-compatible computers are little-endian, which means the processor stores numeric values spanning two or more bytes in memory least significant byte first. The format of the MBR on media reflects this convention. Thus, the MBR signature will appear in a disk editor as the sequence `55 AA`.

The bootstrap sequence in the BIOS will load the first valid MBR that it finds into the computer's physical memory at address 0x7C00 to 0x7DFF. The last instruction executed in the BIOS code will be a "jump" to that address in order to direct execution to the beginning of the MBR copy. The primary validation for most BIOSes is the signature at offset 0x01FE, although a BIOS implementer may choose to include other checks, such as verifying that the MBR contains a valid partition table without entries referring to sectors beyond the reported capacity of the disk.

To the BIOS, removable (e.g. floppy) and fixed disks are essentially the same. For either, the BIOS reads the first physical sector of the media into RAM at absolute address 0x7C00, checks the signature in the last two bytes of the loaded sector, and then, if the correct signature is found, transfers control to the first byte of the sector with a jump (JMP) instruction. The only real distinction that the BIOS makes is that (by default, or if the boot order is not configurable) it attempts to boot from the first removable disk before trying to boot from the first fixed disk. From the perspective of the BIOS, the action of the MBR loading a volume boot record into RAM is exactly the same as the action of a floppy disk volume boot record loading the object code of an operating system loader into RAM. In either case, the program that the BIOS loaded is going about the work of chain loading an operating system.

While the MBR boot sector code expects to be loaded at physical address 0x0000:0x7C00, all the memory from physical address 0x0000:0x0501 (address 0x0000:0x0500 is the last one used by a Phoenix BIOS) to 0x0000:0x7FFF, later relaxed to 0x0000:0xFFFF (and sometimes up to 0x9000:0xFFFF)‍—‌the end of the first 640 KB‍—‌is available in real mode. The `INT 12h` BIOS interrupt call may help in determining how much memory can be allocated safely (by default, it simply reads the base memory size in KB from segment:offset location 0x0040:0x0013, but it may be hooked by other resident pre-boot software like BIOS overlays, RPL code or viruses to reduce the reported amount of available memory in order to keep other boot stage software like boot sectors from overwriting them).

The last 66 bytes of the 512-byte MBR are reserved for the partition table and other information, so the MBR boot sector program must be small enough to fit within 446 bytes of memory or less.

The MBR code examines the partition table, selects a suitable partition and loads the program that will perform the next stage of the boot process, usually by making use of INT 13h BIOS calls. The MBR bootstrap code loads and runs (a boot loader- or operating system-dependent) volume boot record code that is located at the beginning of the "active" partition. The volume boot record will fit within a 512-byte sector, but it is safe for the MBR code to load additional sectors to accommodate boot loaders longer than one sector, provided they do not make any assumptions on what the sector size is. In fact, at least 1 KB of RAM is available at address 0x7C00 in every IBM XT- and AT-class machine, so a 1 KB sector could be used with no problem. Like the MBR, a volume boot record normally expects to be loaded at address 0x0000:0x7C00. This derives from the fact that the volume boot record design originated on unpartitioned media, where a volume boot record would be directly loaded by the BIOS boot procedure; as mentioned above, the BIOS treats MBRs and volume boot records (VBRs) exactly alike. Since this is the same location where the MBR is loaded, one of the first tasks of an MBR is to relocate itself somewhere else in memory. The relocation address is determined by the MBR, but it is most often 0x0000:0x0600 (for MS-DOS/PC DOS, OS/2 and Windows MBR code) or 0x0060:0x0000 (most DR-DOS MBRs). (Even though both of these segmented addresses resolve to the same physical memory address in real mode, for Apple Darwin to boot, the MBR must be relocated to 0x0000:0x0600 instead of 0x0060:0x0000, since the code depends on the DS:SI pointer to the partition entry provided by the MBR, but it erroneously refers to it via 0x0000:SI only.) It is important not to relocate to other addresses in memory because many VBRs will assume a certain standard memory layout when loading their boot file.

The *Status* field in a partition table record is used to indicate an active partition. Standard-conformant MBRs will allow only one partition marked active and use this as part of a sanity-check to determine the existence of a valid partition table. They will display an error message, if more than one partition has been marked active. Some non-standard MBRs will not treat this as an error condition and just use the first marked partition in the row.

Traditionally, values other than 0x00 (not active) and 0x80 (active) were invalid and the bootstrap program would display an error message upon encountering them. However, the Plug and Play BIOS Specification and BIOS Boot Specification (BBS) allowed other devices to become bootable as well since 1994. Consequently, with the introduction of MS-DOS 7.10 (Windows 95B) and higher, the MBR started to treat a set bit 7 as active flag and showed an error message for values 0x01..0x7F only. It continued to treat the entry as physical drive unit to be used when loading the corresponding partition's VBR later on, thereby now also accepting other boot drives than 0x80 as valid, however, MS-DOS did not make use of this extension by itself. Storing the actual physical drive number in the partition table does not normally cause backward compatibility problems, since the value will differ from 0x80 *only* on drives other than the first one (which have not been bootable before, anyway). However, even with systems enabled to boot off other drives, the extension may still not work universally, for example, after the BIOS assignment of physical drives has changed when drives are removed, added or swapped. Therefore, per the BIOS Boot Specification (BBS), it is best practice for a modern MBR accepting bit 7 as active flag to pass on the DL value originally provided by the BIOS instead of using the entry in the partition table.

### BIOS to MBR interface

The MBR is loaded at memory location 0x0000:0x7C00 and with the following CPU registers set up when the prior bootstrap loader (normally the IPL in the BIOS) passes execution to it by jumping to 0x0000:0x7C00 in the CPU's real mode.

- CS:IP = 0x0000:0x7C00 (fixed)

Some Compaq BIOSes erroneously use

0x07C0

:

0x0000

instead. While this resolves to the same location in real mode memory, it is non-standard and should be avoided, since MBR code assuming certain register values or not written to be relocatable may not work otherwise.

- DL = boot drive unit (fixed disks / removable drives: 0x80 = first, 0x81 = second, ..., 0xFE; floppies / superfloppies: 0x00 = first, 0x01 = second, ..., 0x7E; values 0x7F and 0xFF are reserved for ROM / remote drives and must not be used on disk).

DL is supported by IBM BIOSes as well as most other BIOSes. The Toshiba T1000 BIOS is known not to support this properly, and some old Wyse 286 BIOSes use DL values greater or equal to 2 for fixed disks (thereby reflecting the logical drive numbers under DOS rather than the physical drive numbers of the BIOS). USB sticks configured as removable drives typically get an assignment of DL =

0x80

,

0x81

, etc. However, some rare BIOSes

erroneously presented them under DL =

0x01

, just as if they were configured as superfloppies.

A standard conformant BIOS assigns numbers greater or equal to

0x80

exclusively to fixed disk / removable drives, and traditionally only values

0x80

and

0x00

were passed on as physical drive units during boot. By convention, only fixed disks / removable drives are partitioned, therefore, the only DL value a MBR could see traditionally was

0x80

. Many MBRs were written to ignore the DL value and work with a hard-wired value (normally

0x80

), anyway.

The

Plug and Play BIOS Specification

and

BIOS Boot Specification

(BBS) allow other devices to become bootable as well since 1994.

The later recommends that MBR and VBR code should use DL rather than internally hardwired defaults.

This will also ensure compatibility with various non-standard assignments (see examples above), as far as the MBR code is concerned.

Bootable CD-ROMs following the

El Torito

specification may contain disk images mounted by the BIOS to occur as floppy or superfloppies on this interface. DL values of

0x00

and

0x01

may also be used by

Protected Area Run Time Interface Extension Services

(PARTIES) and

Trusted Computing Group

(TCG) BIOS extensions in Trusted mode to access otherwise invisible

PARTIES partitions, disk image files located via the

Boot Engineering Extension Record

(BEER) in the last physical sector of a hard disk's

Host Protected Area

(HPA). While designed to emulate floppies or superfloppies, MBR code accepting these non-standard DL values allows to use images of partitioned media at least in the boot stage of operating systems.

- DH bit 5 = 0: device supported through INT 13h; else: don't care (should be zero). DH is supported by some IBM BIOSes.
- Some of the other registers may typically also hold certain register values (DS, ES, SS = 0x0000; SP = 0x0400) with original IBM ROM BIOSes, but this is nothing to rely on, as other BIOSes may use other values. For this reason, MBR code by IBM, Microsoft, Digital Research, etc. never did take any advantage of it. Relying on these register values in boot sectors may also cause problems in chain-boot scenarios.

Systems with Plug-and-Play BIOS or BBS support will provide a pointer to PnP data in addition to DL:

- DL = boot drive unit (see above)
- ES:DI = points to "`$PnP`" installation check structure

This information allows the boot loader in the MBR (or VBR, if passed on) to actively interact with the BIOS or a resident PnP / BBS BIOS overlay in memory in order to configure the boot order, etc., however, this information is ignored by most standard MBRs and VBRs. Ideally, ES:DI is passed on to the VBR for later use by the loaded operating system, but PnP-enabled operating systems typically also have fallback methods to retrieve the PnP BIOS entry point later on

so that most operating systems do not rely on this.

### MBR to VBR interface

By convention, a standard conformant MBR passes execution to a successfully loaded VBR, loaded at memory location 0x0000:0x7C00, by jumping to 0x0000:0x7C00 in the CPU's real mode with the following registers maintained or specifically set up:

- CS:IP = 0x0000:0x7C00 (constant)
- DL = boot drive unit (see above)

MS-DOS 2.0–7.0 / PC

DOS 2.0–6.3

MBRs do not pass on the DL value received on entry, but they rather use the boot status entry in the partition table entry of the selected primary partition as physical boot drive unit. Since this is, by convention,

0x80

in most MBR partition tables, it won't change things unless the BIOS attempted to boot off a physical device other than the first fixed disk / removable drive in the row. This is also the reason why these operating systems cannot boot off a second hard disk, etc. Some FDISK tools allow to mark partitions on secondary disks as "active" as well. In this situation, knowing that these operating systems cannot boot off other drives anyway, some of them continue to use the traditionally fixed value of

0x80

as active marker, whereas others use values corresponding with the currently assigned physical drive unit (

0x81

,

0x82

), thereby allowing booting from other drives, at least in theory. In fact, this will work with many MBR codes, which take a set bit 7 of the boot status entry as active flag rather than insisting on

0x80

, however, MS-DOS/PC

DOS MBRs are hard-wired to accept the fixed value of

0x80

only. Storing the actual physical drive number in the partition table will also cause problems, when the BIOS assignment of physical drives changes, for example when drives are removed, added or swapped. Therefore, for a normal MBR accepting bit 7 as active flag and otherwise just using and passing on to the VBR the DL value originally provided by the BIOS allows for maximum flexibility. MS-DOS 7.1–8.0 MBRs have changed to treat bit 7 as active flag and any values

0x01

..

0x7F

as invalid, but they still take the physical drive unit from the partition table rather than using the DL value provided by the BIOS. DR-DOS 7.07 extended MBRs treat bit 7 as active flag and use and pass on the BIOS DL value by default (including non-standard values

0x00

..

0x01

used by some BIOSes also for partitioned media), but they also provide a special

NEWLDR

configuration block in order to support alternative boot methods in conjunction with LOADER and REAL/32 as well as to change the detail behaviour of the MBR, so that it can also work with drive values retrieved from the partition table (important in conjunction with LOADER and AAPs, see NEWLDR offset

0x000C

), translate Wyse non-standard drive units

0x02

..

0x7F

to

0x80

..

0xFD

, and optionally fix up the drive value (stored at offset

0x019

in the

Extended BIOS Parameter Block

(EBPB)

or at sector offset

0x01FD

) in loaded VBRs before passing execution to them (see NEWLDR offset

0x0014

)—this also allows other boot loaders to use NEWLDR as a chain-loader, configure its in-memory image on the fly and "tunnel" the loading of VBRs, EBRs, or AAPs through NEWLDR.

- The contents of DH and ES:DI should be preserved by the MBR for full Plug-and-Play support (see above), however, many MBRs, including those of MS-DOS 2.0–8.0 / PC DOS 2.0–6.3 and Windows NT/2000/XP, do not. (This is unsurprising, since those versions of DOS predate the Plug-and-Play BIOS standard, and previous standards and conventions indicated no requirements to preserve any register other than DL.) Some MBRs set DH to 0.

The MBR code passes additional information to the VBR in many implementations:

- DS:SI = points to the 16-byte MBR partition table entry (in the relocated MBR) corresponding with the activated VBR. PC-MOS 5.1 depends on this to boot if no partition in the partition table is flagged as bootable. In conjunction with LOADER, Multiuser DOS and REAL/32 boot sectors use this to locate the boot sector of the active partition (or another bootstrap loader like IBMBIO.LDR at a fixed position on disk) if the boot file (LOADER.SYS) could not be found. PTS-DOS 6.6 and S/DOS 1.0 use this in conjunction with their Advanced Active Partition (AAP) feature. In addition to support for LOADER and AAPs, DR-DOS 7.07 can use this to determine the necessary INT 13h access method when using its dual CHS/LBA VBR code and it will update the boot drive / status flag field in the partition entry according to the effectively used DL value. Darwin bootloaders (Apple's `boot1h`, `boot1u`, and David Elliott's `boot1fat32`) depend on this pointer as well, but additionally they don't use DS, but assume it to be set to 0x0000 instead. This will cause problems if this assumption is incorrect. The MBR code of OS/2, MS-DOS 2.0 to 8.0, PC DOS 2.0 to 7.10 and Windows NT/2000/XP provides this same interface as well, although these systems do not use it. The Windows Vista/7 MBRs no longer provide this DS:SI pointer. While some extensions only depend on the 16-byte partition table entry itself, other extensions may require the whole 4 (or 5 entry) partition table to be present as well.
- DS:BP = optionally points to the 16-byte MBR partition table entry (in the relocated MBR) corresponding with the activated VBR. This is identical to the pointer provided by DS:SI (see above) and is provided by MS-DOS 2.0–8.0, PC DOS 2.0–7.10, Windows NT/2000/XP/Vista/7 MBRs. It is, however, not supported by most third-party MBRs.

Under DR-DOS 7.07 an extended interface may be optionally provided by the extended MBR and in conjunction with LOADER:

- AX = magic signature indicating the presence of this NEWLDR extension (0x0EDC)
- DL = boot drive unit (see above)
- DS:SI = points to the 16-byte MBR partition table entry used (see above)
- ES:BX = start of boot sector or NEWLDR sector image (typically 0x7C00)
- CX = reserved

In conjunction with GPT, an *Enhanced Disk Drive Specification* (EDD) 4 Hybrid MBR proposal recommends another extension to the interface:

- EAX = 0x54504721 ("`!GPT`")
- DL = boot drive unit (see above)
- DS:SI = points to a Hybrid MBR handover structure, consisting of a 16-byte dummy MBR partition table entry (with all bits set except for the boot flag at offset 0x00 and the partition type at offset 0x04) followed by additional data. This is partially compatible with the older DS:SI extension discussed above, if only the 16-byte partition entry, not the whole partition table is required by these older extensions.

Since older operating systems (including their VBRs) do not support this extension nor are they able to address sectors beyond the 2

TiB barrier, a GPT-enabled hybrid boot loader should still emulate the 16-byte dummy MBR partition table entry if the boot partition is located within the first 2

TiB.

- ES:DI = points to "`$PnP`" installation check structure (see above)

Though it is possible to manipulate the bytes in the MBR sector directly using various disk editors, there are tools to write fixed sets of functioning code to the MBR. Since MS-DOS 5.0, the program `FDISK` has included the switch `/MBR`, which will rewrite the MBR code. Under Windows 2000 and Windows XP, the Recovery Console can be used to write new MBR code to a storage device using its `fixmbr` command. Under Windows Vista and Windows 7, the Recovery Environment can be used to write new MBR code using the `BOOTREC /FIXMBR` command. Some third-party utilities may also be used for directly editing the contents of partition tables (without requiring any knowledge of hexadecimal or disk/sector editors), such as MBRWizard.

`dd` is a POSIX command commonly used to read or write any location on a storage device, MBR included. In Linux, ms-sys may be used to install a Windows MBR. The GRUB and LILO projects have tools for writing code to the MBR sector, namely `grub-install` and `lilo -mbr`. The GRUB Legacy interactive console can write to the MBR, using the `setup` and `embed` commands, but GRUB2 currently requires `grub-install` to be run from within an operating system.

Various programs are able to create a "backup" of both the primary partition table and the logical partitions in the extended partition.

Linux `sfdisk` (on a SystemRescueCD) is able to save a backup of the primary and extended partition table. It creates a file that can be read in a text editor, or this file can be used by sfdisk to restore the primary/extended partition table. An example command to back up the partition table is `sfdisk -d /dev/hda > hda.out` and to restore is `sfdisk /dev/hda < hda.out`. It is possible to copy the partition table from one disk to another this way, useful for setting up mirroring, but sfdisk executes the command without prompting/warnings using `sfdisk -d /dev/sda | sfdisk /dev/sdb`.

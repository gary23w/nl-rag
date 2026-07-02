---
title: "NTFS (part 1/2)"
source: https://en.wikipedia.org/wiki/Alternate_Data_Streams
domain: ntfs-filesystem
license: CC-BY-SA-4.0
tags: ntfs, master file table, alternate data streams, fat filesystem
fetched: 2026-07-02
part: 1/2
---

# NTFS

(Redirected from

Alternate Data Streams

)

**NT File System** (**NTFS**) is a proprietary journaling file system developed by Microsoft in the 1990s.

It was developed to overcome scalability, security and other limitations with FAT. NTFS adds several features that FAT and HPFS lack, including: access control lists (ACLs); filesystem encryption; transparent compression; sparse files; file system journaling and volume shadow copy, a feature that allows backups of a system while in use.

Starting with Windows NT 3.1, it is the default file system of the Windows NT family superseding the File Allocation Table (FAT) file system. NTFS read/write support is available on Linux and BSD using NTFS3 in Linux and NTFS-3G in both Linux and BSD.

NTFS uses several files hidden from the user to store metadata about other files stored on the drive which can help improve speed and performance when reading data.


## History

In the mid-1980s, Microsoft and IBM formed a joint project to create the next generation of graphical operating system; the result was OS/2 and HPFS. Because Microsoft disagreed with IBM on many important issues, they eventually separated; OS/2 remained an IBM project and Microsoft worked to develop Windows NT and NTFS.

The HPFS file system for OS/2 contained several important new features. When Microsoft created their new operating system, they borrowed many of these concepts for NTFS. The original NTFS developers were Tom Miller, Gary Kimura, Brian Andrew, and David Goebel.

Probably as a result of this common ancestry, HPFS and NTFS use the same disk partition identification type code (07). Using the same Partition ID Record Number is highly unusual, since there were dozens of unused code numbers available, and other major file systems have their own codes. For example, FAT has more than nine (one each for FAT12, FAT16, FAT32, etc.). Algorithms identifying the file system in a partition type 07 must perform additional checks to distinguish between HPFS and NTFS.

### Versions

Microsoft has released five versions of NTFS:

| NTFS version number | First operating system | Release date | New features | Remarks |
|---|---|---|---|---|
| 1.0 | Windows NT 3.1 | 1993 | Initial version | NTFS 1.0 is incompatible with 1.1 and newer: volumes written by Windows NT 3.5x cannot be read by Windows NT 3.1 until an update (available on the NT 3.5x installation media) is installed. |
| 1.1 | Windows NT 3.5 | 1994 | Named streams and access control lists | NTFS compression support was added in Windows NT 3.51 |
| 1.2 | Windows NT 4.0 | 1996 | Security descriptors | Commonly called NTFS 4.0 after the OS release |
| 3.0 | Windows 2000 | 2000 | Disk quotas, file-level encryption in a form of Encrypting File System, sparse files, reparse points, update sequence number (USN) journaling, distributed link tracking, the `$Extend` folder and its files | Compatibility was also made available for Windows NT 4.0 with the Service Pack 4 update. Commonly called NTFS 5.0 after the OS release. |
| 3.1 | Windows XP | October 2001 | Expanded the Master File Table (MFT) entries with redundant MFT record number (useful for recovering damaged MFT files) | Commonly called NTFS 5.1 after the OS release. LFS version 1.1 was replaced by version 2.0 as of Windows 8 to improve performance. |

The `NTFS.sys` version number (e.g. v5.0 in Windows 2000) is based on the operating system version; it should not be confused with the NTFS version number (v3.1 since Windows XP).

Although subsequent versions of Windows added new file system-related features, they did not change NTFS itself. For example, Windows Vista implemented NTFS symbolic links, Transactional NTFS, partition shrinking, and self-healing. NTFS symbolic links are a new feature in the file system; all the others are new operating system features that make use of NTFS features already in place.


## Scalability

NTFS is optimized for 4 KB clusters, but supports a maximum cluster size of 2 MB. (Earlier implementations support up to 64 KB) The maximum NTFS volume size that the specification can support is 264 − 1 clusters, but not all implementations achieve this theoretical maximum, as discussed below.

The maximum NTFS volume size implemented in Windows XP Professional is 232 − 1 clusters, partly due to partition table limitations. For example, using 64 KB clusters, the maximum size Windows XP NTFS volume is 256 TB minus 64 KB. Using the default cluster size of 4 KB, the maximum NTFS volume size is 16 TB minus 4 KB. Both of these are vastly higher than the 128 GB limit in Windows XP SP1. The size of a partition in the Master Boot Record (MBR) is limited to 2 TiB with a hard drive with 512-byte physical sectors, although for a 4 KiB physical sector the MBR partition size limit is 16 TiB. An alternative is to use multiple GUID Partition Table (GPT or "dynamic") volumes for be combined to create a single NTFS volume larger than 2 TiB. Booting from a GPT volume to a Windows environment in a Microsoft supported way requires a system with Unified Extensible Firmware Interface (UEFI) and 64-bit support. GPT data disks are supported on systems with BIOS.

The NTFS maximum theoretical limit on the size of individual files is 16 EB (16 × 10246 or 264 bytes) minus 1 KB, which totals 18,446,744,073,709,550,592 bytes (18.4 EB). With Windows 10 version 1709 and Windows Server 2019, the maximum *implemented* file size is 8 PB minus 2 MB or 9,007,199,252,643,840 bytes (9 PB).


## Interoperability

### Windows

While the different NTFS versions are for the most part fully forward- and backward-compatible, there are technical considerations for mounting newer NTFS volumes in older versions of Microsoft Windows. This affects dual-booting, and external portable hard drives. For example, attempting to use an NTFS partition with Windows' feature "Previous Versions" (Volume Shadow Copy) on an operating system that does not support it will result in the contents of those previous versions being lost.

A Windows command-line utility called convert.exe can convert supporting file systems to NTFS, including HPFS (only on Windows NT 3.1, 3.5, and 3.51), FAT16 and FAT32 (on Windows 2000 and later). The conversion occurs in-place, meaning the existing files stay where they are and are not re-written during the process. The process is not reversible without formatting and writing the files again.

### FreeBSD

FreeBSD 3.2 released in May 1999 included read-only NTFS support written by Semen Ustimenko. This implementation was ported to NetBSD by Christos Zoulas and Jaromir Dolecek and released with NetBSD 1.5 in December 2000. The FreeBSD implementation of NTFS was also ported to OpenBSD by Julien Bordet and offers native read-only NTFS support by default on i386 and amd64 platforms as of version 4.9 released 1 May 2011.

### Linux

Linux kernel versions 2.1.74 and later include a driver written by Martin von Löwis which has the ability to read NTFS partitions; kernel versions 2.5.11 and later contain a new driver written by Anton Altaparmakov (University of Cambridge) and Richard Russon which supports file read. The ability to write to files was introduced with kernel version 2.6.15 in 2006 which allows users to write to existing files but does not allow the creation of new ones. Paragon's NTFS driver (see below) has been merged into kernel version 5.15, and it supports read/write on normal, compressed and sparse files, as well as journal replaying.

NTFS-3G is a free GPL-licensed FUSE implementation of NTFS that was initially developed as a Linux kernel driver by Szabolcs Szakacsits. It was re-written as a FUSE program to work on other systems that FUSE supports like macOS, FreeBSD, NetBSD, OpenBSD, Solaris, QNX, and Haiku and allows reading and writing to NTFS partitions. A performance enhanced commercial version of NTFS-3G, called "Tuxera NTFS for Mac", is also available from the NTFS-3G developers.

Captive NTFS, a 'wrapping' driver that uses Windows' own driver ntfs.sys, exists for Linux. It was built as a Filesystem in Userspace (FUSE) program and released under the GPL but work on Captive NTFS ceased in 2006.

Linux kernel versions 5.15 onwards carry NTFS3, a fully functional NTFS Read-Write driver which works on NTFS versions up to 3.1 and is maintained primarily by the Paragon Software Group.

### macOS

Mac OS X 10.3 included Ustimenko's read-only implementation of NTFS from FreeBSD. Then in 2006 Apple hired Anton Altaparmakov to write a new NTFS implementation for Mac OS X 10.6. Native NTFS write support is included in 10.6 and later, but is not activated by default, although workarounds do exist to enable the functionality. However, user reports indicate the functionality is unstable and tends to cause kernel panics.

Paragon Software Group sells a read-write driver named *NTFS for Mac*, which is also included on some models of Seagate hard drives.

### OS/2

The NetDrive package for OS/2 (and derivatives such as eComStation and ArcaOS) supports a plugin which allows read and write access to NTFS volumes.

### DOS

There is a free-for-personal-use read/write driver for MS-DOS by Avira called "NTFS4DOS".

Ahead Software developed a "NTFSREAD" driver (version 1.200) for DR-DOS 7.0x between 2002 and 2004. It was part of their Nero Burning ROM software.


## Security

NTFS uses access control lists and user-level encryption to help secure user data.

### Access control lists (ACLs)

In NTFS, each file or folder is assigned a security descriptor that defines its owner and contains two access control lists (ACLs). The first ACL, called discretionary access control list (DACL), defines exactly what type of interactions (e.g. reading, writing, executing or deleting) are allowed or forbidden by which user or groups of users. For example, files in the `C:\Program Files` folder may be read and executed by all users but modified only by a user holding administrative privileges. Windows Vista adds mandatory access control info to DACLs. DACLs are the primary focus of User Account Control in Windows Vista and later.

The second ACL, called system access control list (SACL), defines which interactions with the file or folder are to be audited and whether they should be logged when the activity is successful, failed or both. For example, auditing can be enabled on sensitive files of a company, so that its managers get to know when someone tries to delete them or make a copy of them, and whether they succeed.

### Encryption

Encrypting File System (EFS) provides user-transparent encryption of any file or folder on an NTFS volume. EFS works in conjunction with the EFS service, Microsoft's CryptoAPI and the EFS File System Run-Time Library (FSRTL). EFS works by encrypting a file with a bulk symmetric key (also known as the File Encryption Key, or FEK), which is used because it takes a relatively small amount of time to encrypt and decrypt large amounts of data than if an asymmetric key cipher is used. The symmetric key that is used to encrypt the file is then encrypted with a public key that is associated with the user who encrypted the file, and this encrypted data is stored in an alternate data stream of the encrypted file. To decrypt the file, the file system uses the private key of the user to decrypt the symmetric key that is stored in the data stream. It then uses the symmetric key to decrypt the file. Because this is done at the file system level, it is transparent to the user. Also, in case of a user losing access to their key, support for additional decryption keys has been built into the EFS system, so that a recovery agent can still access the files if needed. NTFS-provided encryption and NTFS-provided compression are mutually exclusive, meaning they can not be used for the same files at the same time; however, NTFS can be used for one and a third-party tool for the other.

The support of EFS is not available in Basic, Home, and MediaCenter versions of Windows, and must be activated after installation of Professional, Ultimate, and Server versions of Windows or by using enterprise deployment tools within Windows domains.


## Features

### Journaling

NTFS is a journaling file system and uses the NTFS Log ($LogFile) to record metadata changes to the volume. It is a feature that FAT does not provide and is critical for NTFS to ensure that its complex internal data structures will remain consistent in case of system crashes or data moves performed by the defragmentation API, and allow easy rollback of uncommitted changes to these critical data structures when the volume is remounted. Notably affected structures are the volume allocation bitmap, modifications to MFT records such as moves of some variable-length attributes stored in MFT records and attribute lists, and indices for directories and security descriptors.

The ($LogFile) format has evolved through several versions:

| Windows Version | $LogFile format version |
|---|---|
| Windows NT 4.0 | 1.1 |
| Windows 2000 |   |
| Windows XP |   |
| Windows Vista |   |
| Windows 7 |   |
| Windows 8 | 2.0 |
| Windows 8.1 |   |
| Windows 10 |   |
| Windows 11 |   |

The incompatibility of the $LogFile versions implemented by Windows 8, Windows 10, Windows 11 prevents Windows 7 (and earlier versions of Windows) from recognizing version 2.0 of the $LogFile. Backward compatibility is provided by downgrading the $LogFile to version 1.1 when an NTFS volume is cleanly dismounted. It is again upgraded to version 2.0 when mounting on a compatible version of Windows. However, when hibernating to disk in the logoff state (a.k.a. Hybrid Boot or Fast Boot, which is enabled by default), mounted file systems are not dismounted, and thus the $LogFiles of any active file systems are not downgraded to version 1.1. The inability to process version 2.0 of the $LogFile by versions of Windows older than 8.0 results in an unnecessary invocation of the CHKDSK disk repair utility. This is particularly a concern in a multi-boot scenario involving pre- and post-8.0 versions of Windows, or when frequently moving a storage device between older and newer versions. A Windows Registry setting exists to prevent the automatic upgrade of the $LogFile to the newer version. The problem can also be dealt with by disabling Hybrid Boot.

The USN Journal (Update Sequence Number Journal) is a system management feature that records (in $Extend\$UsnJrnl) changes to files, streams and directories on the volume, as well as their various attributes and security settings. The journal is made available for applications to track changes to the volume. This journal can be enabled or disabled on non-system volumes.

### Hard links

The hard link feature allows different file names to directly refer to the same file contents. Hard links may link only to files in the same volume, because each volume has its own MFT. Hard links were originally included to support the POSIX subsystem in Windows NT.

Although hard links use the same MFT record (inode) which records file metadata such as file size, modification date, and attributes, NTFS also caches this data in the directory entry as a performance enhancement. This means that when listing the contents of a directory using FindFirstFile/FindNextFile family of APIs, (equivalent to the POSIX opendir/readdir APIs) the software listing the directory will also receive this cached information, in addition to the name and inode. However, software may not see up-to-date information, as this information is only guaranteed to be updated when a file is closed, and then only for the directory from which the file was opened. This means where a file has multiple names via hard links, updating a file via one name does not update the cached data associated with the other name. Software can obtain up-to-date data using GetFileInformationByHandle (which is the equivalent of the POSIX fstat function). This can be done using a handle which has no access to the file itself (passing zero to CreateFile for dwDesiredAccess), and closing this handle has the incidental effect of updating the cached information.

Windows uses hard links to support short (8.3) filenames in NTFS. Operating system support is needed because there are legacy applications that can work only with 8.3 filenames, but support can be disabled. In this case, an additional filename record and directory entry is added, but both 8.3 and long file name are linked and updated together, unlike a regular hard link.

The NTFS file system has a limit of 1023 hard links on a file.

### Alternate data stream (ADS)

Alternate data streams allow more than one data stream to be associated with a filename (a fork), using the format "filename:streamname" (e.g., "text.txt:extrastream"). These streams are not shown to or made editable by users through any typical GUI application built into Windows by default, disguising their existence from most users. Although intended for helpful metadata, their arcane nature makes them a potential hiding place for malware, spyware, unseen browser history, and other potentially unwanted information.

Alternate streams are not listed in Windows Explorer, and their size is not included in the file's size. When the file is copied or moved to another file system without ADS support the user is warned that alternate data streams cannot be preserved. No such warning is typically provided if the file is attached to an e-mail, or uploaded to a website. Thus, using alternate streams for critical data may cause problems. Microsoft provides a downloadable tool called Streams to view streams on a selected volume. Starting with Windows PowerShell 3.0, it is possible to manage ADS natively with six cmdlets: Add-Content, Clear-Content, Get-Content, Get-Item, Remove-Item, Set-Content.

A small ADS named `Zone.Identifier` is added by Internet Explorer and by most browsers to mark files downloaded from external sites as possibly unsafe to run; the local shell would then require user confirmation before opening them. When the user indicates that they no longer want this confirmation dialog, this ADS is deleted. This functionality is also known as "Mark of the Web". All Chromium (e.g. Google Chrome) and Firefox-based web browsers also write the `Zone.Identifier` stream to downloaded files.

Malware has used alternate data streams to hide code. Since the late 2000s, some malware scanners and other special tools check for alternate data streams. Due to the risks associated with ADS, particularly involving privacy and the `Zone.Identifier` stream, there exists software specifically designed to strip streams from files (certain streams with perceived risk or all of them) in a user-friendly way.

NTFS Streams were introduced in Windows NT 3.1, to enable Services for Macintosh (SFM) to store resource forks. Although current versions of Windows Server no longer include SFM, third-party Apple Filing Protocol (AFP) products (such as GroupLogic's ExtremeZ-IP) still use this feature of the file system.

### File compression

Compression is enabled on a per-folder or per-file basis by setting the 'compressed' attribute. When compression is enabled on a folder, any files moved or saved to that folder will be automatically compressed using LZNT1 algorithm (a variant of LZ77). The compression algorithm is designed to support cluster sizes of up to 4 KB; when the cluster size is greater than 4 KB on an NTFS volume, NTFS compression is not available. Data is compressed in 16-cluster chunks (up to 64 KB in size); if the compression reduces 64 KB of data to 60 KB or less, NTFS treats the unneeded 4 KB pages like empty sparse file clusters—they are not written. This allows for reasonable random-access times as the OS merely has to follow the chain of fragments.

Compression works best with files that have repetitive content, are seldom written, are usually accessed sequentially, and are not themselves compressed. Single-user systems with limited hard disk space can benefit from NTFS compression for small files, from 4 KB to 64 KB or more, depending on compressibility. Files smaller than approximately 900 bytes are stored within the directory entry of the MFT.

For operating systems besides Windows, all versions of the NTFS-3G driver support reading compressed files according to its developers, but support for appending data to compressed files, which means adding new data resulting in increasing the size of a file, was added in November 2009. Overwriting existing compressed data is supported since August 2010. Various programs utilize NTFS file compression, such as CompactGUI.

#### Advantages

Users of fast multi-core processors will find improvements in application speed by compressing their applications and data as well as a reduction in space used. Even when SSD controllers already compress data, there is still a reduction in I/Os since less data is transferred.

According to research by Microsoft's NTFS Development team, 50–60 GB is a reasonable maximum size for a compressed file on an NTFS volume with a 4 KB (default) cluster (block) size. This reasonable maximum size decreases sharply for volumes with smaller cluster sizes.

#### Disadvantages

Large compressible files become highly fragmented since every chunk smaller than 64 KB becomes a fragment. Flash memory, such as SSD drives do not have the head movement delays and high access time of mechanical hard disk drives, so fragmentation has only a smaller penalty.

Windows 2000 cannot start if NTLDR is compressed because decompression filters are not yet loaded. Later versions of Windows do not allow important system files to be compressed.

### System compression

Since Windows 10, Microsoft has introduced new file compression scheme based on the XPRESS algorithm with 4K/8K/16K block size and the LZX algorithm; both are variants of LZ77 updated with Huffman entropy coding and range coding, which LZNT1 lacked. These compression algorithms were taken from Windows Imaging Format (WIM file).

The new compression scheme is used by CompactOS feature, which reduces disk usage by compressing Windows system files. CompactOS is not an extension of NTFS file compression and does not use the 'compressed' attribute; instead, it sets a reparse point on each compressed file with a WOF (Windows Overlay Filter) tag, but the actual data is stored in an alternate data stream named "WofCompressedData", which is decompressed on-the-fly by a WOF filesystem filter driver, and the main file is an empty sparse file. This design is meant purely for read-only access, so any writes to compressed files result in an automatic decompression.

CompactOS compression is intended for OEMs who prepare OS images with the `/compact` flag of the `DISM` tool in Windows ADK, but it can also be manually turned on per file with the `/exe` flag of the `compact` command. CompactOS algorithm avoids file fragmentation by writing compressed data in contiguously allocated chunks, unlike core NTFS compression.

CompactOS file compression is an improved version of WIMBoot feature introduced in Windows 8.1. WIMBoot reduces Windows disk usage by keeping system files in a compressed WIM image on a separate hidden disk partition. Similarly to CompactOS, Windows system directories only contain sparse files marked by a reparse point with a WOF tag, and Windows Overlay Filter driver decompresses file contents on-the-fly from the WIM image. WIMBoot is less effective than CompactOS though, as new updated versions of system files need to be written to the system partition, consuming disk space.

### Sparse files

Sparse files are files interspersed with empty segments for which no actual storage space is used. To the applications, the file looks like an ordinary file with empty regions seen as regions filled with zeros; the file system maintains an internal list of such regions for each sparse file. A sparse file does not necessarily include sparse zeros areas; the "sparse file" attribute just means that the file is allowed to have them.

Database applications, for instance, may use sparse files. As with compressed files, the actual sizes of sparse files are not taken into account when determining quota limits.

### Volume Shadow Copy

The Volume Shadow Copy Service (VSS) keeps historical versions of files and folders on NTFS volumes by copying old, newly overwritten data to shadow copy via copy-on-write technique. The user may later request an earlier version to be recovered. This also allows data backup programs to archive files currently in use by the file system.

Windows Vista also introduced persistent shadow copies for use with System Restore and Previous Versions features. Persistent shadow copies, however, are deleted when an older operating system mounts that NTFS volume. This happens because the older operating system does not understand the newer format of persistent shadow copies.

### Transactions

As of Windows Vista, applications can use Transactional NTFS (TxF) to group multiple changes to files together into a single transaction. The transaction will guarantee that either all of the changes happen, or none of them do, and that no application outside the transaction will see the changes until they are committed.

It uses similar techniques as those used for Volume Shadow Copies (i.e. copy-on-write) to ensure that overwritten data can be safely rolled back, and a CLFS log to mark the transactions that have still not been committed, or those that have been committed but still not fully applied (in case of system crash during a commit by one of the participants).

Transactional NTFS does not restrict transactions to just the local NTFS volume, but also includes other transactional data or operations in other locations such as data stored in separate volumes, the local registry, or SQL databases, or the current states of system services or remote services. These transactions are coordinated network-wide with all participants using a specific service, the DTC, to ensure that all participants will receive same commit state, and to transport the changes that have been validated by any participant (so that the others can invalidate their local caches for old data or rollback their ongoing uncommitted changes). Transactional NTFS allows, for example, the creation of network-wide consistent distributed file systems, including with their local live or offline caches.

Microsoft now advises against using TxF: "Microsoft strongly recommends developers utilize alternative means" since "TxF may not be available in future versions of Microsoft Windows".

### Quotas

Disk quotas were introduced in NTFS v3. They allow the administrator of a computer that runs a version of Windows that supports NTFS to set a threshold of disk space that users may use. It also allows administrators to keep track of how much disk space each user is using. An administrator may specify a certain level of disk space that a user may use before they receive a warning, and then deny access to the user once they hit their upper limit of space. Disk quotas do not take into account NTFS's transparent file-compression, should this be enabled. Applications that query the amount of free space will also see the amount of free space left to the user who has a quota applied to them.

### Reparse points

Introduced in NTFS v3, NTFS reparse points are used by associating a reparse tag in the user space attribute of a file or directory. Microsoft includes several default tags including symbolic links, directory junction points and volume mount points. When the Object Manager parses a file system name lookup and encounters a reparse attribute, it will *reparse* the name lookup, passing the user controlled reparse data to every file system filter driver that is loaded into Windows. Each filter driver examines the reparse data to see whether it is associated with that reparse point, and if that filter driver determines a match, then it intercepts the file system request and performs its special functionality.

### Date and time

NTFS stores date and time attributes as a 64-bit integer that counts the 100-nanosecond intervals from the beginning of the year 1601, following the Windows NT epoch. The year 1601 was chosen to align the beginning of the date range with the gregorian calendar in order to simplify calculations, given that the gregorian calendar operates on a 400-year cycle, and the 1601-2000 cycle was the active cycle at the time Windows NT was conceived.

NTFS records four types of time stamps: A file creation time (interpreted as "birth time" on Linux), a last modification time, a last modification of the MFT record (interpreted as "change time" on Linux) and a last access time. Each of those times has the same granularity of 100 nanoseconds.


## Limitations

### Resizing

Starting with Windows Vista, Microsoft added the built-in ability to shrink or expand a partition. However, this ability does not relocate page file fragments or files that have been marked as unmovable, so shrinking a volume will often require relocating or disabling any page file, the index of Windows Search, and any Shadow Copy used by System Restore. Various third-party tools are capable of resizing NTFS partitions.

### OneDrive

Since 2017, Microsoft requires the OneDrive file structure to reside on an NTFS disk. This is because OneDrive Files On-Demand feature uses NTFS reparse points to link files and folders that are stored in OneDrive to the local filesystem, making the file or folder unusable with any previous version of Windows, with any other NTFS file system driver, or any file system and backup utilities not updated to support it.

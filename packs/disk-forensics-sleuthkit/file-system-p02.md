---
title: "File system (part 2/2)"
source: https://en.wikipedia.org/wiki/File_system
domain: disk-forensics-sleuthkit
license: CC-BY-SA-4.0
tags: disk forensics sleuth kit, file system forensic analysis, forensic disk imaging, file carving recovery, write blocker acquisition
fetched: 2026-07-02
part: 2/2
---

## Implementations

An operating system (OS) typically supports one or more file systems. Sometimes an OS and its file system are so tightly interwoven that it is difficult to describe them independently.

An OS typically provides file system access to the user. Often an OS provides a command line interface, such as a Unix shell, Windows Command Prompt and PowerShell, or OpenVMS DCL. An OS often also provides a file browser in a graphical user interface such as Finder on macOS, File Explorer on Windows, GNOME Files in GNOME, or Dolphin in KDE Plasma.

### Unix and Unix-like operating systems

Unix-like operating systems create a virtual file system, which makes all files on all connected storage devices appear to exist in a single hierarchy. This means, in those systems, there is one root directory, and every file existing on the system is located under it somewhere. Unix-like systems can use a RAM disk or network shared resource as its root directory.

Unix-like systems assign a device name to each device, but this is not how the files on that device are accessed. Instead, to gain access to files on another device, the operating system must first be informed where in the directory tree those files should appear. This process is called mounting a file system. For example, to access the files on a CD-ROM, one must tell the operating system "Take the file system from this CD-ROM and make it appear under such-and-such directory." The directory given to the operating system is called the *mount point* – it might, for example, be /media. The /media directory exists on many Unix systems (as specified in the Filesystem Hierarchy Standard) and is intended specifically for use as a mount point for removable media such as CDs, DVDs, USB drives or floppy disks. It may be empty, or it may contain subdirectories for mounting individual devices. Generally, only the administrator (i.e. root user) may authorize the mounting of file systems.

Unix-like operating systems often include software and tools that assist in the mounting process and provide it new functionality. Some of these strategies have been coined "auto-mounting" as a reflection of their purpose.

- In many situations, file systems other than the root need to be available as soon as the operating system has booted. All Unix-like systems therefore provide a facility for mounting file systems at boot time. System administrators define these file systems in the configuration file fstab (*vfstab* in Solaris), which also indicates options and mount points.
- In some situations, there is no need to mount certain file systems at boot time, although their use may be desired thereafter. There are some utilities for Unix-like systems that allow the mounting of predefined file systems upon demand.
- Removable media allow programs and data to be transferred between machines without a physical connection. Common examples include USB flash drives, CD-ROMs, and DVDs. Utilities have therefore been developed to detect the presence and availability of a medium and then mount that medium without any user intervention.
- Progressive Unix-like systems have also introduced a concept called **supermounting**; see, for example, the Linux supermount-ng project. For example, a floppy disk that has been supermounted can be physically removed from the system. Under normal circumstances, the disk should have been synchronized and then unmounted before its removal. Provided synchronization has occurred, a different disk can be inserted into the drive. The system automatically notices that the disk has changed and updates the mount point contents to reflect the new medium.
- An automounter will automatically mount a file system when a reference is made to the directory atop which it should be mounted. This is usually used for file systems on network servers, rather than relying on events such as the insertion of media, as would be appropriate for removable media.

#### Linux

Linux supports numerous file systems, but common choices for the system disk on a block device include the ext* family (ext2, ext3 and ext4), XFS, JFS, and btrfs. For raw flash without a flash translation layer (FTL) or Memory Technology Device (MTD), there are UBIFS, JFFS2 and YAFFS, among others. SquashFS is a common compressed read-only file system.

#### Solaris

Solaris in earlier releases defaulted to (non-journaled or non-logging) UFS for bootable and supplementary file systems. Solaris defaulted to, supported, and extended UFS.

Support for other file systems and significant enhancements were added over time, including Veritas Software Corp. (journaling) VxFS, Sun Microsystems (clustering) QFS, Sun Microsystems (journaling) UFS, and Sun Microsystems (open source, poolable, 128 bit compressible, and error-correcting) ZFS.

Kernel extensions were added to Solaris to allow for bootable Veritas VxFS operation. Logging or journaling was added to UFS in Sun's Solaris 7. Releases of Solaris 10, Solaris Express, OpenSolaris, and other open source variants of the Solaris operating system later supported bootable ZFS.

Logical Volume Management allows for spanning a file system across multiple devices for the purpose of adding redundancy, capacity, and/or throughput. Legacy environments in Solaris may use Solaris Volume Manager (formerly known as Solstice DiskSuite). Multiple operating systems (including Solaris) may use Veritas Volume Manager. Modern Solaris based operating systems eclipse the need for volume management through leveraging virtual storage pools in ZFS.

#### macOS

macOS (formerly Mac OS X) uses the Apple File System (APFS), which in 2017 replaced a file system inherited from classic Mac OS called HFS Plus (HFS+). Apple also uses the term "Mac OS Extended" for HFS+. HFS Plus is a metadata-rich and case-preserving but (usually) case-insensitive file system. Due to the Unix roots of macOS, Unix permissions were added to HFS Plus. Later versions of HFS Plus added journaling to prevent corruption of the file system structure and introduced a number of optimizations to the allocation algorithms in an attempt to defragment files automatically without requiring an external defragmenter.

File names can be up to 255 characters. HFS Plus uses Unicode to store file names. On macOS, the filetype can come from the type code, stored in file's metadata, or the filename extension.

HFS Plus has three kinds of links: Unix-style hard links, Unix-style symbolic links, and aliases. Aliases are designed to maintain a link to their original file even if they are moved or renamed; they are not interpreted by the file system itself, but by the File Manager code in userland.

macOS 10.13 High Sierra, which was announced on June 5, 2017, at Apple's WWDC event, uses the Apple File System on solid-state drives.

macOS also supported the UFS file system, derived from the BSD Unix Fast File System via NeXTSTEP. However, as of Mac OS X Leopard, macOS could no longer be installed on a UFS volume, nor can a pre-Leopard system installed on a UFS volume be upgraded to Leopard. As of Mac OS X Lion UFS support was completely dropped.

Newer versions of macOS are capable of reading and writing to the legacy FAT file systems (16 and 32) common on Windows. They are also capable of *reading* the newer NTFS file systems for Windows. In order to *write* to NTFS file systems on macOS versions prior to Mac OS X Snow Leopard third-party software is necessary. Mac OS X 10.6 (Snow Leopard) and later allow writing to NTFS file systems, but only after a non-trivial system setting change (third-party software exists that automates this).

Finally, macOS supports reading and writing of the exFAT file system since Mac OS X Snow Leopard, starting from version 10.6.5.

### OS/2

OS/2 1.2 introduced the High Performance File System (HPFS). HPFS supports mixed case file names in different code pages, long file names (255 characters), more efficient use of disk space, an architecture that keeps related items close to each other on the disk volume, less fragmentation of data, extent-based space allocation, a B+ tree structure for directories, and the root directory located at the midpoint of the disk, for faster average access. A journaled filesystem (JFS) was shipped in 1999.

### PC-BSD

PC-BSD is a desktop version of FreeBSD, which inherits FreeBSD's ZFS support, similarly to FreeNAS. The new graphical installer of PC-BSD can handle */ (root) on ZFS* and RAID-Z pool installs and disk encryption using Geli right from the start in an easy convenient (GUI) way. The current PC-BSD 9.0+ 'Isotope Edition' has ZFS filesystem version 5 and ZFS storage pool version 28.

### Plan 9

Plan 9 from Bell Labs treats everything as a file and accesses all objects as a file would be accessed (i.e., there is no ioctl or mmap): networking, graphics, debugging, authentication, capabilities, encryption, and other services are accessed via I/O operations on file descriptors. The 9P protocol removes the difference between local and remote files. File systems in Plan 9 are organized with the help of private, per-process namespaces, allowing each process to have a different view of the many file systems that provide resources in a distributed system.

The Inferno operating system shares these concepts with Plan 9.

### Microsoft Windows

Windows makes use of the FAT, NTFS, exFAT, Live File System and ReFS file systems (the last of these is only supported and usable in Windows Server 2012, Windows Server 2016, Windows 8, Windows 8.1, and Windows 10; Windows cannot boot from it).

Windows uses a *drive letter* abstraction at the user level to distinguish one disk or partition from another. For example, the path C:\WINDOWS represents a directory WINDOWS on the partition represented by the letter C. Drive C: is most commonly used for the primary hard disk drive partition, on which Windows is usually installed and from which it boots. This "tradition" has become so firmly ingrained that bugs exist in many applications which make assumptions that the drive that the operating system is installed on is C. The use of drive letters, and the tradition of using "C" as the drive letter for the primary hard disk drive partition, can be traced to MS-DOS, where the letters A and B were reserved for up to two floppy disk drives. This in turn derived from CP/M in the 1970s, and ultimately from IBM's CP/CMS of 1967.

#### FAT

The family of FAT file systems is supported by almost all operating systems for personal computers, including all versions of Windows and MS-DOS/PC DOS, OS/2, and DR-DOS. (PC DOS is an OEM version of MS-DOS, MS-DOS was originally based on SCP's 86-DOS. DR-DOS was based on Digital Research's Concurrent DOS, a successor of CP/M-86.) The FAT file systems are therefore well-suited as a universal exchange format between computers and devices of most any type and age.

The FAT file system traces its roots back to an (incompatible) 8-bit FAT precursor in Standalone Disk BASIC and the short-lived MDOS/MIDAS project.

Over the years, the file system has been expanded from FAT12 to FAT16 and FAT32. Various features have been added to the file system including subdirectories, codepage support, extended attributes, and long filenames. Third parties such as Digital Research have incorporated optional support for deletion tracking, and volume/directory/file-based multi-user security schemes to support file and directory passwords and permissions such as read/write/execute/delete access rights. Most of these extensions are not supported by Windows.

The FAT12 and FAT16 file systems had a limit on the number of entries in the root directory of the file system and had restrictions on the maximum size of FAT-formatted disks or partitions.

FAT32 addresses the limitations in FAT12 and FAT16, except for the file size limit of close to 4 GB, but it remains limited compared to NTFS.

FAT12, FAT16 and FAT32 also have a limit of eight characters for the file name, and three characters for the extension (such as .exe). This is commonly referred to as the 8.3 filename limit. VFAT, an optional extension to FAT12, FAT16 and FAT32, introduced in Windows 95 and Windows NT 3.5, allowed long file names (LFN) to be stored in the FAT file system in a backwards compatible fashion.

#### NTFS

NTFS, introduced with the Windows NT operating system in 1993, allowed ACL-based permission control. Other features also supported by NTFS include hard links, multiple file streams, attribute indexing, quota tracking, sparse files, encryption, compression, and reparse points (directories working as mount-points for other file systems, symlinks, junctions, remote storage links).

#### exFAT

exFAT has certain advantages over NTFS with regard to file system overhead.

exFAT is not backward compatible with FAT file systems such as FAT12, FAT16 or FAT32. The file system is supported with newer Windows systems, such as Windows XP, Windows Server 2003, Windows Vista, Windows 2008, Windows 7, Windows 8, Windows 8.1, Windows 10 and Windows 11.

exFAT is supported in macOS starting with version 10.6.5 (Snow Leopard). Support in other operating systems is sparse since implementing support for exFAT requires a license. exFAT is the only file system that is fully supported on both macOS and Windows that can hold files larger than 4 GB.

### OpenVMS

Files-11 is the file system used in the RSX-11, IAS, and OpenVMS operating systems from Digital Equipment Corporation. It supports record-oriented I/O, remote network access, and file versioning. The original ODS-1 layer is a flat file system; the ODS-2 version is a hierarchical file system, with support for access control lists.

Files-11 is similar to, but significantly more advanced than, the file systems used in previous Digital Equipment Corporation operating systems such as TOPS-20 and RSTS/E.

### MVS

Prior to the introduction of VSAM, OS/360 systems implemented a hybrid file system. The system was designed to easily support removable disk packs, so the information relating to all files on one disk (*volume* in IBM terminology) is stored on that disk in a flat system file called the *Volume Table of Contents* (VTOC). The VTOC stores all metadata for the file. Later a hierarchical directory structure was imposed with the introduction of the *System Catalog*, which can optionally catalog files (datasets) on resident and removable volumes. The catalog only contains information to relate a dataset to a specific volume. If the user requests access to a dataset on an offline volume, and they have suitable privileges, the system will attempt to mount the required volume. Cataloged and non-cataloged datasets can still be accessed using information in the VTOC, bypassing the catalog, if the required volume id is provided to the OPEN request. Still later the VTOC was indexed to speed up access.

### Conversational Monitor System

The IBM Conversational Monitor System (CMS) component of VM/370 uses a separate flat file system for each virtual disk (*minidisk*). File data and control information are scattered and intermixed. The anchor is a record called the *Master File Directory* (MFD), always located in the fourth block on the disk. Originally CMS used fixed-length 800-byte blocks, but later versions used larger size blocks up to 4K. Access to a data record requires two levels of indirection, where the file's directory entry (called a *File Status Table* (FST) entry) points to blocks containing a list of addresses of the individual records.

### AS/400 file system

Data on the AS/400 and its successors consists of system objects mapped into the system virtual address space in a single-level store. Many types of objects are defined including the directories and files found in other file systems. File objects, along with other types of objects, form the basis of the AS/400's support for an integrated relational database.

### Other file systems

- RSRE FLEX file system - written in ALGOL 68
- The file system of the Michigan Terminal System (MTS) is interesting because: (i) it provides "line files" where record lengths and line numbers are associated as metadata with each record in the file, lines can be added, replaced, updated with the same or different length records, and deleted anywhere in the file without the need to read and rewrite the entire file; (ii) using program keys files may be shared or permitted to commands and programs in addition to users and groups; and (iii) there is a comprehensive file locking mechanism that protects both the file's data and its metadata.
- TempleOS uses RedSea, a file system made by Terry A. Davis.


## Limitations

### Design limitations

File systems limit storable data capacity – generally driven by the typical size of storage devices at the time the file system is designed and anticipated into the foreseeable future.

Since storage sizes have increased at near exponential rate (see Moore's law), newer storage devices often exceed existing file system limits within only a few years after introduction. This requires new file systems with ever increasing capacity.

With higher capacity, the need for capabilities and therefore complexity increases as well. File system complexity typically varies proportionally with available storage capacity. Capacity issues aside, the file systems of early 1980s home computers with 50 KB to 512 KB of storage would not be a reasonable choice for modern storage systems with hundreds of gigabytes of capacity. Likewise, modern file systems would not be a reasonable choice for these early systems, since the complexity of modern file system structures would quickly consume the limited capacity of early storage systems.

### Converting the type of a file system

It may be advantageous or necessary to have files in a different file system than they currently exist. Reasons include the need for an increase in the space requirements beyond the limits of the current file system. The depth of path may need to be increased beyond the restrictions of the file system. There may be performance or reliability considerations. Providing access to another operating system which does not support the existing file system is another reason.

#### In-place conversion

In some cases conversion can be done in-place, although migrating the file system is more conservative, as it involves a creating a copy of the data and is recommended. On Windows, FAT and FAT32 file systems can be converted to NTFS via the convert.exe utility, but not the reverse. On Linux, ext2 can be converted to ext3 (and converted back), and ext3 can be converted to ext4 (but not back), and both ext3 and ext4 can be converted to btrfs, and converted back until the undo information is deleted. These conversions are possible due to using the same format for the file data itself, and relocating the metadata into empty space, in some cases using sparse file support.

#### Migrating to a different file system

Migration has the disadvantage of requiring additional space although it may be faster. The best case is if there is unused space on media which will contain the final file system.

For example, to migrate a FAT32 file system to an ext2 file system, a new ext2 file system is created. Then the data from the FAT32 file system is copied to the ext2 one, and the old file system is deleted.

An alternative, when there is not sufficient space to retain the original file system until the new one is created, is to use a work area (such as a removable media). This takes longer but has the benefit of producing a backup.

### Long file paths and long file names

In hierarchical file systems, files are accessed by means of a *path* that is a branching list of directories containing the file. Different file systems have different limits on the depth of the path. File systems also have a limit on the length of an individual file name.

Copying files with long names or located in paths of significant depth from one file system to another may cause undesirable results. This depends on how the utility doing the copying handles the discrepancy.

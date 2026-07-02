---
title: "File system (part 1/2)"
source: https://en.wikipedia.org/wiki/File_system
domain: operating-systems
license: CC-BY-SA-4.0
tags: operating system, os kernel, virtual memory, process scheduling, os theory
fetched: 2026-07-02
part: 1/2
---

# File system

In computing, a **file system** or **filesystem** (often abbreviated to **FS** or **fs**) governs file organization and access. A *local* file system is a capability of an operating system that services the applications running on the same computer. A *distributed* file system is a protocol that provides file access between networked computers.

A file system provides a data storage service that allows applications to share mass storage. Without a file system, applications could access the storage in incompatible ways that lead to resource contention, data corruption, and data loss.

There are many file system designs and implementations – with various structures and features and various resulting characteristics such as speed, flexibility, security, size, and more.

File systems have been developed for many types of storage devices, including hard disk drives (HDDs), solid-state drives (SSDs), magnetic tapes and optical discs.

A portion of the computer main memory can be set up as a RAM disk that serves as a storage device for a file system. File systems such as tmpfs can store files in virtual memory.

A *virtual* file system provides access to files that are either computed on request, called *virtual files* (for example those provided by procfs and sysfs), or are mapping into another, backing storage.


## Etymology

From c. 1900 and before the advent of computers, the terms *file system*, *filing system* and *system for filing* were used to describe methods of organizing, storing and retrieving paper documents. By 1961, the term *file system* was being applied to computerized filing alongside the original meaning. By 1964, it was in general use.


## Architecture

A local file system's architecture can be described as layers of abstraction even though a particular file system design may not actually separate the concepts.

The *logical file system* layer provides relatively high-level access via an application programming interface (API) for file operations including open, close, read and write – delegating operations to lower layers. This layer manages open file table entries and per-process file descriptors. It provides file access, directory operations, security, and protection.

The *virtual file system*, an optional layer, supports multiple concurrent instances of physical file systems, each of which is called a file system implementation.

The *physical file system* layer provides relatively low-level access to a storage device (e.g. disk). It reads and writes data blocks, provides buffering and other memory management, and controls placement of blocks in specific locations on the storage medium. This layer uses device drivers or channel I/O to drive the storage device.


## Attributes

### File names

A *file name*, or *filename*, identifies a file to consuming applications and in some cases users.

A file name is unique so that an application can refer to exactly one file for a particular name. If the file system supports directories, then generally file name uniqueness is enforced within the context of each directory. In other words, a storage can contain multiple files with the same name, but not in the same directory.

Most file systems restrict the length of a file name.

Some file systems match file names as case sensitive and others as case insensitive. For example, the names `MYFILE` and `myfile` match the same file for case-insensitive, but different files for case-sensitive.

Most modern file systems allow a file name to contain a wide range of characters from the Unicode character set. Some restrict characters such as those used to indicate special attributes such as a device, device type, directory prefix, file path separator, or file type.

### Directories

File systems typically support organizing files into *directories*, also called *folders*, which segregate files into groups.

This may be implemented by associating the file name with an index in a table of contents or an inode in a Unix-like file system.

Directory structures may be flat (i.e. linear), or allow hierarchies by allowing a directory to contain directories, called subdirectories.

The first file system to support arbitrary hierarchies of directories was used in the Multics operating system. The native file systems of Unix-like systems also support arbitrary directory hierarchies, as do, Apple's Hierarchical File System and its successor HFS+ in classic Mac OS, the FAT file system in MS-DOS 2.0 and later versions of MS-DOS and in Microsoft Windows, the NTFS file system in the Windows NT family of operating systems, and the ODS-2 (On-Disk Structure-2) and higher levels of the Files-11 file system in OpenVMS.

In addition to data, the file content, a file system also manages associated metadata which may include but is not limited to:

- name
- size which may be stored as the number of blocks allocated or as a byte count
- when created, last accessed, last modified
- owner user and group
- access permissions
- file attributes such as whether the file is read-only, executable, etc.
- device type (e.g. block, character, socket, subdirectory, etc.)

A file system stores associated metadata separate from the content of the file.

Most file systems store the names of all the files in one directory in one place—the directory table for that directory—which is often stored like any other file. Many file systems put only some of the metadata for a file in the directory table, and the rest of the metadata for that file in a completely separate structure, such as the inode.

Most file systems also store metadata not associated with any one particular file. Such metadata includes information about unused regions—free space bitmap, block availability map—and information about bad sectors. Often such information about an allocation group is stored inside the allocation group itself.

Additional attributes can be associated on file systems, such as NTFS, XFS, ext2, ext3, some versions of UFS, and HFS+, using extended file attributes. Some file systems provide for user defined attributes such as the author of the document, the character encoding of a document or the size of an image.

Some file systems allow for different data collections to be associated with one file name. These separate collections may be referred to as *streams* or *forks*. Apple has long used a forked file system on the Macintosh, and Microsoft supports streams in NTFS. Some file systems maintain multiple past revisions of a file under a single file name; the file name by itself retrieves the most recent version, while prior saved versions can be accessed using a special naming convention such as "filename;4" or "filename(-4)" to access the version four saves ago.

### Storage space organization

A local file system tracks which areas of storage belong to which file and which are not being used.

When a file system creates a file, it allocates space for data. Some file systems permit or require specifying an initial space allocation and subsequent incremental allocations as the file grows.

To delete a file, the file system records that the file's space is free (available to use for another file).

A local file system manages storage space to provide a level of reliability and efficiency. Generally, it allocates storage device space in a granular manner, usually multiple physical units (i.e. bytes). For example, in Apple DOS of the early 1980s, 256-byte sectors on 140 kilobyte floppy disk used a *track/sector map*.

The granular nature results in unused space, sometimes called slack space, for each file except for those that have the rare size that is a multiple of the granular allocation. For a 512-byte allocation, the average unused space is 256 bytes. For 64 KB clusters, the average unused space is 32 KB.

Generally, the allocation unit size is set when the storage is configured. Choosing a relatively small size compared to the files stored results in excessive access overhead. Choosing a relatively large size results in excessive unused space. Choosing an allocation size based on the average size of files expected to be in the storage tends to minimize unusable space.

### Fragmentation

As a file system creates, modifies, and deletes files, the underlying storage representation may become fragmented. Files and the unused space between files will occupy allocation blocks that are not contiguous.

A file becomes fragmented if space needed to store its content cannot be allocated in contiguous blocks. Free space becomes fragmented when files are deleted.

Fragmentation is invisible to the end user and the system still works correctly. However, this can degrade performance on some storage hardware that works better with contiguous blocks such as hard disk drives. Other hardware such as solid-state drives are not affected by fragmentation.

### Access control

A file system often supports access control of data that it manages.

The intent of access control is often to prevent certain users from reading or modifying certain files.

Access control can also restrict access by program to ensure that data is modified in a controlled way. Examples include passwords stored in the metadata of the file or elsewhere and file permissions in the form of permission bits, access control lists, or capabilities. The need for file system utilities to be able to access the data at the media level to reorganize the structures and provide efficient backup usually means that these are only effective for polite users, but are not effective against intruders.

Methods for encrypting file data are sometimes included in the file system. This is very effective since there is no need for file system utilities to know the encryption seed to effectively manage the data. The risks of relying on encryption include the fact that an attacker can copy the data and use brute force to decrypt the data. Additionally, losing the seed means losing the data.

### Storage quota

Some operating systems allow a system administrator to enable disk quotas to limit a user's use of storage space.

### Data integrity

A file system typically ensures that stored data remains consistent in both normal operations as well as exceptional situations like:

- accessing program neglects to inform the file system that it has completed file access (to close a file)
- accessing program terminates abnormally (crashes)
- media failure
- loss of connection to remote systems
- operating system failure
- system reset (soft reboot)
- power failure (hard reboot)

Recovery from exceptional situations may include updating metadata, directory entries, and handling data that was buffered but not written to storage media.

### Recording

A file system might record events to allow analysis of issues such as:

- file or systemic problems and performance
- nefarious access

### Data access

#### Byte stream access

Many file systems access data as a stream of bytes. Typically, to read file data, a program provides a memory buffer and the file system retrieves data from the medium and then writes the data to the buffer. A write involves the program providing a buffer of bytes that the file system reads and then stores to the medium.

#### Record access

Some file systems, or layers on top of a file system, allow a program to define a record so that a program can read and write data as a structure, not an unorganized sequence of bytes.

If a *fixed length* record definition is used, then locating the nth record can be calculated mathematically, which is relatively fast compared to parsing the data for record separators.

An identification for each record, also known as a key, allows a program to read, write, and update records without regard to their location in storage. Such storage requires managing blocks of media, usually separating key blocks and data blocks. Efficient algorithms can be developed with pyramid structures for locating records.

### Utilities

Typically, a file system can be managed by the user via various utility programs.

Some utilities allow the user to create, configure and remove an instance of a file system. It may allow extending or truncating the space allocated to the file system.

Directory utilities may be used to create, rename, and delete *directory entries*, which are also known as *dentries* (singular: *dentry*), and to alter metadata associated with a directory. Directory utilities may also include capabilities to create additional links to a directory (hard links in Unix), to rename parent links (".." in Unix-like operating systems), and to create bidirectional links to files.

File utilities create, list, copy, move, and delete files, and alter metadata. They may be able to truncate data, truncate or extend space allocation, append to, move, and modify files in-place. Depending on the underlying structure of the file system, they may provide a mechanism to prepend to or truncate from the beginning of a file, insert entries into the middle of a file, or delete entries from a file. Utilities to free space for deleted files, if the file system provides an undelete function, also belong to this category.

Some file systems defer operations such as reorganization of free space, secure erasing of free space, and rebuilding of hierarchical structures by providing utilities to perform these functions at times of minimal activity. An example is the file system defragmentation utilities.

Some of the most important features of file system utilities are supervisory activities, which may involve bypassing ownership or direct access to the underlying device. These include high-performance backup and recovery, data replication, and reorganization of various data structures and allocation tables within the file system.

### File system API

Utilities, libraries, and programs use file system APIs to make requests of the file system. These include data transfer, positioning, updating metadata, managing directories, managing access specifications, and removal.

### Multiple file systems within a single system

Frequently, retail systems are configured with a single file system occupying the entire storage device.

Another approach is to partition the disk so that several file systems with different attributes can be used. One file system, for use as browser cache or email storage, might be configured with a small allocation size. This keeps the activity of creating and deleting files typical of browser activity in a narrow area of the disk where it will not interfere with other file allocations. Another partition might be created for the storage of audio or video files with a relatively large block size. Yet another may normally be set *read-only* and only periodically be set writable. Some file systems, such as ZFS and APFS, support multiple file systems sharing a common pool of free blocks, supporting several file systems with different attributes without having to reserve a fixed amount of space for each file system.

A third approach, which is mostly used in cloud systems, is to use "disk images" to house additional file systems, with the same attributes or not, within another (host) file system as a file. A common example is virtualization: one user can run an experimental Linux distribution (using the ext4 file system) in a virtual machine under their production Windows environment (using NTFS). The ext4 file system resides in a disk image, which is treated as a file (or multiple files, depending on the hypervisor and settings) in the NTFS host file system.

Having multiple file systems on a single system has the additional benefit that in the event of a corruption of a single file system, the remaining file systems will frequently still be intact. This includes virus destruction of the *system* file system or even a system that will not boot. File system utilities that require dedicated access can be effectively completed piecemeal. In addition, defragmentation may be more effective. Several system maintenance utilities, such as virus scans and backups, can also be processed in segments. For example, it is not necessary to backup the file system containing videos along with all the other files if none have been added since the last backup. As for the image files, one can easily "spin off" differential images that contain only "new" data written to the master (original) image. Differential images can be used for both safety concerns (as a "disposable" system - can be quickly restored if destroyed or contaminated by a virus, as the old image can be removed and a new image can be created in matter of seconds, even without automated procedures) and quick virtual machine deployment (since the differential images can be quickly spawned using a script in batches).


## Types

### Storage media

#### Disk file systems

A *disk file system* takes advantage of the ability of disk storage media to randomly address data in a short amount of time. Additional considerations include the speed of accessing data following that initially requested and the anticipation that the following data may also be requested. This permits multiple users (or processes) access to various data on the disk without regard to the sequential location of the data. Examples include FAT (FAT12, FAT16, FAT32), exFAT, NTFS, ReFS, HFS and HFS+, HPFS, APFS, UFS, ext2, ext3, ext4, XFS, btrfs, Files-11, Veritas File System, VMFS, ZFS, ReiserFS, NSS and ScoutFS. Some disk file systems are journaling file systems or versioning file systems.

##### Optical discs

ISO 9660 and Universal Disk Format (UDF) are two common formats that target Compact Discs, DVDs and Blu-ray discs. Mount Rainier is an extension to UDF supported since 2.6 series of the Linux kernel and since Windows Vista that facilitates rewriting to DVDs.

#### Flash file systems

A *flash file system* considers the special abilities, performance and restrictions of flash memory devices. Frequently a disk file system can use a flash memory device as the underlying storage media, but it is much better to use a file system specifically designed for a flash device.

#### Tape file systems

A *tape file system* is a file system and tape format designed to store files on tape. Magnetic tapes are sequential storage media with significantly longer random data access times than disks, posing challenges to the creation and efficient management of a general-purpose file system.

In a disk file system there is typically a master file directory, and a map of used and free data regions. Any file additions, changes, or removals require updating the directory and the used/free maps. Random access to data regions is measured in milliseconds so this system works well for disks.

Tape requires linear motion to wind and unwind potentially very long reels of media. This tape motion may take several seconds to several minutes to move the read/write head from one end of the tape to the other.

Consequently, a master file directory and usage map can be extremely slow and inefficient with tape. Writing typically involves reading the block usage map to find free blocks for writing, updating the usage map and directory to add the data, and then advancing the tape to write the data in the correct spot. Each additional file write requires updating the map and directory and writing the data, which may take several seconds to occur for each file.

Tape file systems instead typically allow for the file directory to be spread across the tape intermixed with the data, referred to as *streaming*, so that time-consuming and repeated tape motions are not required to write new data.

However, a side effect of this design is that reading the file directory of a tape usually requires scanning the entire tape to read all the scattered directory entries. Most data archiving software that works with tape storage will store a local copy of the tape catalog on a disk file system, so that adding files to a tape can be done quickly without having to rescan the tape media. The local tape catalog copy is usually discarded if not used for a specified period of time, at which point the tape must be re-scanned if it is to be used in the future.

IBM has developed a file system for tape called the Linear Tape File System. The IBM implementation of this file system has been released as the open-source IBM Linear Tape File System — Single Drive Edition (LTFS-SDE) product. The Linear Tape File System uses a separate partition on the tape to record the index meta-data, thereby avoiding the problems associated with scattering directory entries across the entire tape.

##### Tape formatting

Writing data to a tape, erasing, or formatting a tape is often a significantly time-consuming process and can take several hours on large tapes. With many data tape technologies it is not necessary to format the tape before over-writing new data to the tape. This is due to the inherently destructive nature of overwriting data on sequential media.

Because of the time it can take to format a tape, typically tapes are pre-formatted so that the tape user does not need to spend time preparing each new tape for use. All that is usually necessary is to write an identifying media label to the tape before use, and even this can be automatically written by software when a new tape is used for the first time.

#### Minimal file system / audio-cassette storage

In the 1970s disk and digital tape devices were too expensive for some early microcomputer users. An inexpensive basic data storage system was devised that used common audio cassette tape.

When the system needed to write data, the user was notified to press "RECORD" on the cassette recorder, then press "RETURN" on the keyboard to notify the system that the cassette recorder was recording. The system wrote a sound to provide time synchronization, then modulated sounds that encoded a prefix, the data, a checksum and a suffix. When the system needed to read data, the user was instructed to press "PLAY" on the cassette recorder. The system would *listen* to the sounds on the tape waiting until a burst of sound could be recognized as the synchronization. The system would then interpret subsequent sounds as data. When the data read was complete, the system would notify the user to press "STOP" on the cassette recorder. It was primitive, but it (mostly) worked. Data was stored sequentially, usually in an unnamed format, although some systems (such as the Commodore PET series of computers) did allow the files to be named. Multiple sets of data could be written and located by fast-forwarding the tape and observing at the tape counter to find the approximate start of the next data region on the tape. The user might have to listen to the sounds to find the right spot to begin playing the next data region. Some implementations even included audible sounds interspersed with the data.

### Database file systems

Another concept for file management is the idea of a database-based file system. Instead of, or in addition to, hierarchical structured management, files are identified by their characteristics, like type of file, topic, author, or similar rich metadata.

IBM DB2 for i (formerly known as DB2/400 and DB2 for i5/OS) is a database file system as part of the object based IBM i operating system (formerly known as OS/400 and i5/OS), incorporating a single level store and running on IBM Power Systems (formerly known as AS/400 and iSeries), designed by Frank G. Soltis IBM's former chief scientist for IBM i. Around 1978 to 1988 Frank G. Soltis and his team at IBM Rochester had successfully designed and applied technologies like the database file system where others like Microsoft later failed to accomplish. These technologies are informally known as 'Fortress Rochester' and were in few basic aspects extended from early Mainframe technologies but in many ways more advanced from a technological perspective.

Some other projects that are not "pure" database file systems but that use some aspects of a database file system:

- Many Web content management systems use a relational DBMS to store and retrieve files. For example, XHTML files are stored as XML or text fields, while image files are stored as blob fields; SQL SELECT (with optional XPath) statements retrieve the files, and allow the use of a sophisticated logic and more rich information associations than "usual file systems." Many CMSs also have the option of storing only metadata within the database, with the standard filesystem used to store the content of files.
- Very large file systems, embodied by applications like Apache Hadoop and Google File System, use some *database file system* concepts.

### Transactional file systems

Some programs need to either make multiple file system changes, or, if one or more of the changes fail for any reason, make none of the changes. For example, a program which is installing or updating software may write executables, libraries, and/or configuration files. If some of the writing fails and the software is left partially installed or updated, the software may be broken or unusable. An incomplete update of a key system utility, such as the command shell, may leave the entire system in an unusable state.

Transaction processing introduces the atomicity guarantee, ensuring that operations inside of a transaction are either all committed or the transaction can be aborted and the system discards all of its partial results. This means that if there is a crash or power failure, after recovery, the stored state will be consistent. Either the software will be completely installed or the failed installation will be completely rolled back, but an unusable partial install will not be left on the system. Transactions also provide the isolation guarantee, meaning that operations within a transaction are hidden from other threads on the system until the transaction commits, and that interfering operations on the system will be properly serialized with the transaction.

Windows, beginning with Vista, added transaction support to NTFS, in a feature called Transactional NTFS, but its use is now discouraged. There are a number of research prototypes of transactional file systems for UNIX systems, including the Valor file system, Amino, LFS, and a transactional ext3 file system on the TxOS kernel, as well as transactional file systems targeting embedded systems, such as TFFS.

Ensuring consistency across multiple file system operations is difficult, if not impossible, without file system transactions. File locking can be used as a concurrency control mechanism for individual files, but it typically does not protect the directory structure or file metadata. For instance, file locking cannot prevent TOCTTOU race conditions on symbolic links. File locking also cannot automatically roll back a failed operation, such as a software upgrade; this requires atomicity.

Journaling file systems is one technique used to introduce transaction-level consistency to file system structures. Journal transactions are not exposed to programs as part of the OS API; they are only used internally to ensure consistency at the granularity of a single system call.

Data backup systems typically do not provide support for direct backup of data stored in a transactional manner, which makes the recovery of reliable and consistent data sets difficult. Most backup software simply notes what files have changed since a certain time, regardless of the transactional state shared across multiple files in the overall dataset. As a workaround, some database systems simply produce an archived state file containing all data up to that point, and the backup software only backs that up and does not interact directly with the active transactional databases at all. Recovery requires separate recreation of the database from the state file after the file has been restored by the backup software.

### Network file systems

A *network file system* is a file system that acts as a client for a remote file access protocol, providing access to files on a server. Programs using local interfaces can transparently create, manage and access hierarchical directories and files in remote network-connected computers. Examples of network file systems include clients for the NFS, AFS, SMB protocols, and file-system-like clients for FTP and WebDAV.

### Shared disk file systems

A *shared disk file system* is one in which a number of machines (usually servers) all have access to the same external disk subsystem (usually a storage area network). The file system arbitrates access to that subsystem, preventing write collisions. Examples include GFS2 from Red Hat, GPFS, now known as Spectrum Scale, from IBM, SFS from DataPlow, CXFS from SGI, StorNext from Quantum Corporation and ScoutFS from Versity.

### Special file systems

Some file systems expose elements of the operating system as files so they can be acted on via the file system API. This is common in Unix-like operating systems, and to a lesser extent in other operating systems. Examples include:

- devfs, udev, TOPS-10 expose I/O devices or pseudo-devices as special files
- configfs and sysfs expose special files that can be used to query and configure Linux kernel information
- procfs exposes process information as special files

### Directory hierarchy support

#### Flat file systems

In a flat file system, there are no subdirectories; files are stored on a disk without hierarchy. While simple, this become awkward as the number of files grows and makes it difficult to organize files into related groups.

The mainframe DOS/360 and OS/360 store entries for all files on a disk pack (*volume*) in a directory on the pack called a *Volume Table of Contents* (VTOC).

Some minicomputer operating systems, such as RT-11, had a flat file system with only one top-level directory. Others, such as RSX-11, supported a top-level directory and subdirectories for user accounts, but did not support subdirectories of the user-account directories.

Most 8-bit microcomputer operating systems originally used flat file systems (e.g., Apple DOS, Atari DOS). CP/M machines use a flat file system, where files can be assigned to one of 16 *user areas* and generic file operations narrowed to work on one instead of defaulting to work on all of them. These user areas are no more than special attributes associated with the files; it is not necessary to define specific quota for each of these areas and files can be added to groups for as long as there is free storage space on the disk.

The FAT file system in IBM PC DOS/MS-DOS was a flat file system until DOS version 2.0, when support for subdirectories was added.

The classic Mac OS for the Macintosh supported only the flat Macintosh File System until the Hierarchical File System was introduced in version 2.1. The file management program, the Finder, created the illusion of a partially hierarchical filing system. This structure required every file to have a unique name, even if it appeared to be in a separate folder.

A 21st century addition to the flat file system family is Amazon's S3, a remote storage service, which is intentionally simplistic to allow users the ability to customize how their data is stored. The only constructs are buckets (imagine a disk drive of unlimited size) and objects (similar, but not identical to the standard concept of a file). Advanced file management is allowed by being able to use nearly any character (including '/') in the object's name, and the ability to select subsets of the bucket's content based on identical prefixes.

#### Hierarchical file systems

In computing, a hierarchical file system is a file system that uses directories to organize files into a tree structure.

In a hierarchical file system, *directories* contain information about both files and other directories, called *subdirectories* which, in turn, can point to other subdirectories, and so on. This is organized as a tree structure, or *hierarchy*, generally portrayed with the root at the top. The *root directory* is the base of the hierarchy, and is usually stored at some fixed location on disk.

A hierarchical file system contrasts with a *flat file system*, where information about all files is stored in a single directory, and there are no subdirectories.

Almost all file systems today are hierarchical. What is referred to as a file system is a specific instance of a hierarchical system. For example, NTFS, HPFS, and ext4, all implement a hierarchical system with different features for buffering, file allocation, and file recovery.

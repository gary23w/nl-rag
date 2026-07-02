---
title: "NTFS (part 2/2)"
source: https://en.wikipedia.org/wiki/Master_File_Table
domain: ntfs-filesystem
license: CC-BY-SA-4.0
tags: ntfs, master file table, alternate data streams, fat filesystem
fetched: 2026-07-02
part: 2/2
---

## Structure

NTFS is made up of several components including: a partition boot sector (PBS) that holds boot information; the master file table that stores a record of all files and folders in the filesystem; a series of meta files that help structure meta data more efficiently; data streams and locking mechanisms.

Internally, NTFS uses B-trees to index file system data. A file system journal is used to guarantee the integrity of the file system metadata but not individual files' content. Systems using NTFS are known to have improved reliability compared to FAT file systems.

NTFS allows any sequence of 16-bit values for name encoding (e.g. file names, stream names or index names) except 0x0000. This means UTF-16 code units are supported, but the file system does not check whether a sequence is valid UTF-16 (it allows any sequence of short values, not restricted to those in the Unicode standard). In Win32 namespace, any UTF-16 code units are case insensitive whereas in POSIX namespace they are case sensitive. File names are limited to 255 UTF-16 code units. Certain names are reserved in the volume root directory and cannot be used for files. These are `$MFT`, `$MFTMirr`, `$LogFile`, `$Volume`, `$AttrDef`, `.` (dot), `$Bitmap`, `$Boot`, `$BadClus`, `$Secure`, `$UpCase`, and `$Extend`. `.` (dot) and `$Extend` are both directories; the others are files. The NT kernel limits full paths to 32,767 UTF-16 code units. There are some additional restrictions on code points and file names.

### Partition Boot Sector (PBS)

| Byte offset | Field length | Typical value | Field name | Purpose |   |
|---|---|---|---|---|---|
| 0x00 | 3 bytes | 0xEB5290 | x86 JMP and NOP instructions | Causes execution to continue after the data structures in this boot sector. |   |
| 0x03 | 8 bytes | "`NTFS`" Word "NTFS" followed by four trailing spaces (0x20) | OEM ID | This is the magic number that indicates this is an NTFS file system. |   |
| 0x0B | 2 bytes | 0x0200 | BPB | Bytes per sector | The number of bytes in a disk sector. |
| 0x0D | 1 byte | 0x08 | Sectors Per Cluster | The number of sectors in a cluster. If the value is greater than 0x80, the amount of sectors is 2 to the power of the absolute value of considering this field to be negative. |   |
| 0x0E | 2 bytes | 0x0000 | Reserved Sectors, unused |   |   |
| 0x10 | 3 bytes | 0x000000 | Unused | This field is always 0 |   |
| 0x13 | 2 bytes | 0x0000 | Unused by NTFS | This field is always 0 |   |
| 0x15 | 1 byte | 0xF8 | Media Descriptor | The type of drive. 0xF8 is used to denote a hard drive (in contrast to the several sizes of floppy). |   |
| 0x16 | 2 bytes | 0x0000 | Unused | This field is always 0 |   |
| 0x18 | 2 bytes | 0x003F | Sectors Per Track | The number of disk sectors in a drive track. |   |
| 0x1A | 2 bytes | 0x00FF | Number Of Heads | The number of heads on the drive. |   |
| 0x1C | 4 bytes | 0x0000003F | Hidden Sectors | The number of sectors preceding the partition. |   |
| 0x20 | 4 bytes | 0x00000000 | Unused | Not used by NTFS |   |
| 0x24 | 4 bytes | 0x00800080 | EBPB | Unused | Not used by NTFS |
| 0x28 | 8 bytes | 0x00000000007FF54A | Total sectors | The partition size in sectors. |   |
| 0x30 | 8 bytes | 0x0000000000000004 | $MFT cluster number | The cluster that contains the Master File Table |   |
| 0x38 | 8 bytes | 0x000000000007FF54 | $MFTMirr cluster number | The cluster that contains a backup of the Master File Table |   |
| 0x40 | 1 byte | 0xF6 | Bytes or Clusters Per File Record Segment | A positive value denotes the number of clusters in a File Record Segment. A negative value denotes the amount of bytes in a File Record Segment, in which case the size is 2 to the power of the absolute value. (0xF6 = -10 → 210 = 1024). |   |
| 0x41 | 3 bytes | 0x000000 | Unused | This field is not used by NTFS |   |
| 0x44 | 1 byte | 0x01 | Bytes or Clusters Per Index Buffer | A positive value denotes the number of clusters in an Index Buffer. A negative value denotes the amount of bytes and it uses the same algorithm for negative numbers as the "Bytes or Clusters Per File Record Segment." |   |
| 0x45 | 3 bytes | 0x000000 | Unused | This field is not used by NTFS |   |
| 0x48 | 8 bytes | 0x1C741BC9741BA514 | Volume Serial Number | A unique random number assigned to this partition, to keep things organized. |   |
| 0x50 | 4 bytes | 0x00000000 | Checksum, unused | Supposedly a checksum. |   |
| 0x54 | 426 bytes |   | Bootstrap Code | The code that loads the rest of the operating system. This is pointed to by the first 3 bytes of this sector. |   |
| 0x01FE | 2 bytes | 0xAA55 | End-of-sector Marker | This flag indicates that this is a valid boot sector. |   |

This boot partition format is roughly based upon the earlier FAT filesystem, but the fields are in different locations. Some of these fields, especially the "sectors per track", "number of heads" and "hidden sectors" fields may contain dummy values on drives where they either do not make sense or are not determinable.

The OS first looks at the 8 bytes at 0x30 to find the cluster number of the $MFT, then multiplies that number by the number of sectors per cluster (1 byte found at 0x0D). This value is the sector offset (LBA) to the $MFT, which is described below.

### Master File Table

In NTFS, all file, directory and metafile data—file name, creation date, access permissions (by the use of access control lists), and size—are stored as metadata in the **Master File Table** (**MFT**). This abstract approach allowed easy addition of file system features during Windows NT's development—an example is the addition of fields for indexing used by the Active Directory and the Windows Search. This also enables fast file search software to locate named local files and folders included in the MFT very quickly, without requiring any other index.

The MFT structure supports algorithms which minimize disk fragmentation. A directory entry consists of a filename and a "file ID" (analogous to the inode number), which is the record number representing the file in the Master File Table. The file ID also contains a reuse count to detect stale references. While this strongly resembles the W_FID of Files-11, other NTFS structures radically differ.

A partial copy of the MFT, called the MFT mirror, is stored to be used in case of corruption. If the first record of the MFT is corrupted, NTFS reads the second record to find the MFT mirror file. Locations for both files are stored in the boot sector.

### Metafiles

NTFS contains several files that define and organize the file system. In all respects, most of these files are structured like any other user file ($Volume being the most peculiar), but are not of direct interest to file system clients. These metafiles define files, back up critical file system data, buffer file system changes, manage free space allocation, satisfy BIOS expectations, track bad allocation units, and store security and disk space usage information. All content is in an unnamed data stream, unless otherwise indicated.

| Segment number | File name | Purpose |
|---|---|---|
| 0 | `$MFT` | Describes all files on the volume, including file names, timestamps, stream names, and lists of cluster numbers where data streams reside, indexes, security identifiers, and file attributes like "read only", "compressed", "encrypted", etc. |
| 1 | `$MFTMirr` | Duplicate of the first vital entries of $MFT, usually 4 entries (4 kilobytes). |
| 2 | `$LogFile` | Contains transaction log of file system metadata changes. |
| 3 | `$Volume` | Contains information about the volume, namely the volume object identifier, volume label, file system version, and volume flags (mounted, chkdsk requested, requested $LogFile resize, mounted on NT 4, volume serial number updating, structure upgrade request). This data is not stored in a data stream, but in special MFT attributes: If present, a volume object ID is stored in an $OBJECT_ID record; the volume label is stored in a $VOLUME_NAME record, and the remaining volume data is in a $VOLUME_INFORMATION record. Note: volume serial number is stored in file $Boot (below). |
| 4 | `$AttrDef` | A table of MFT attributes that associates numeric identifiers with names. |
| 5 | `.` | Root directory. Directory data is stored in $INDEX_ROOT and $INDEX_ALLOCATION attributes both named $I30. |
| 6 | `$Bitmap` | An array of bit entries: each bit indicates whether its corresponding cluster is used (allocated) or free (available for allocation). |
| 7 | `$Boot` | Volume boot record (VBR). This file is always located at the first clusters on the volume. It contains bootstrap code (see NTLDR/BOOTMGR) and a BIOS parameter block including a volume serial number and cluster numbers of $MFT and $MFTMirr. |
| 8 | `$BadClus` | A file that contains all the clusters marked as having bad sectors. This file simplifies cluster management by the chkdsk utility, both as a place to put newly discovered bad sectors, and for identifying unreferenced clusters. This file contains two data streams, even on volumes with no bad sectors: an unnamed stream contains bad sectors—it is zero length for perfect volumes; the second stream is named $Bad and contains all clusters on the volume not in the first stream. |
| 9 | `$Secure` | Access control list database that reduces overhead having many identical ACLs stored with each file, by uniquely storing these ACLs only in this database (contains two indices: $SII *(Standard_Information ID)* and $SDH *(Security Descriptor Hash)*, which index the stream named $SDS containing actual ACL table). |
| 10 | `$UpCase` | A table of unicode uppercase characters for ensuring case-insensitivity in Win32 and DOS namespaces. |
| 11 | `$Extend` | A file system directory containing various optional extensions, such as $Quota, $ObjId, $Reparse or $UsnJrnl. |
| 12–23 | Reserved for $MFT extension entries. Extension entries are additional MFT records that contain additional attributes that do not fit in the primary record. This could occur if the file is sufficiently fragmented, has many streams, long filenames, complex security, or other rare situations. |   |
| 24 | `$Extend\$Quota` | Holds disk quota information. Contains two index roots, named $O and $Q. |
| 25 | `$Extend\$ObjId` | Holds link tracking information. Contains an index root and allocation named $O. |
| 26 | `$Extend\$Reparse` | Holds reparse point data (such as symbolic links). Contains an index root and allocation named $R. |
| 27– | Beginning of regular file entries. |   |

These metafiles are treated specially by Windows, handled directly by the `NTFS.SYS` driver and are difficult to directly view: special purpose-built tools are needed. As of Windows 7, the NTFS driver completely prohibits user access, resulting in a BSoD whenever an attempt to execute a metadata file is made. One such tool is the nfi.exe ("NTFS File Sector Information Utility") that is freely distributed as part of the Microsoft "OEM Support Tools". For example, to obtain information on the "$MFT"-Master File Table Segment the following command is used: `nfi.exe c:\$MFT` Another way to bypass the restriction is to use 7-Zip's file manager and go to the low-level NTFS path `\\.\X:\` (where `X:\` resembles any drive/partition). Here, 3 new folders will appear: `$EXTEND`, `[DELETED]` (a pseudo-folder that 7-Zip uses to attach files deleted from the file system to view), and `[SYSTEM]` (another pseudo-folder that contains all the NTFS metadata files). This trick can be used from removable devices (USB flash drives, external hard drives, SD cards, etc.) inside Windows, but doing this on the active partition requires offline access (namely WinRE).

### Attribute lists, attributes, and streams

For each file (or directory) described in the MFT record, there is a linear repository of stream descriptors (also named *attributes*), packed together in one or more MFT records (containing the so-called *attributes list*), with extra padding to fill the fixed 1 KB size of every MFT record, and that fully describes the effective streams associated with that file.

Each attribute has an attribute type (a fixed-size integer mapping to an attribute definition in file $AttrDef), an optional attribute name (for example, used as the name for an alternate data stream), and a value, represented in a sequence of bytes. For NTFS, the standard data of files, the alternate data streams, or the index data for directories are stored as attributes.

According to $AttrDef, some attributes can be either resident or non-resident. The $DATA attribute, which contains file data, is such an example. When the attribute is resident (which is represented by a flag), its value is stored directly in the MFT record. Otherwise, clusters are allocated for the data, and the cluster location information is stored as data runs in the attribute.

- For each file in the MFT, the attributes identified by *attribute type, attribute name* must be unique. Additionally, NTFS has some ordering constraints for these attributes.
- There is a predefined null attribute type, used to indicate the end of the list of attributes in one MFT record. It must be present as the last attribute in the record (all other storage space available after it will be ignored and just consists of padding bytes to match the record size in the MFT).
- Some attribute types are required and must be present in each MFT record, except unused records that are just indicated by null attribute types.
  - This is the case for the $STANDARD_INFORMATION attribute that is stored as a fixed-size record and contains the timestamps and other basic single-bit attributes (compatible with those managed by FAT in DOS or Windows 9x).
- Some attribute types cannot have a name and must remain anonymous.
  - This is the case for the standard attributes, or for the preferred NTFS "filename" attribute type, or the "short filename" attribute type, when it is also present (for compatibility with DOS-like applications, see below). It is also possible for a file to contain only a short filename, in which case it will be the preferred one, as listed in the Windows Explorer.
  - The filename attributes stored in the attribute list do not make the file immediately accessible through the hierarchical file system. In fact, all the filenames must be indexed separately in at least one other directory on the same volume. There it must have its own MFT record and its own security descriptors and attributes that reference the MFT record number for this file. This allows the same file or directory to be "hardlinked" several times from several containers on the same volume, possibly with distinct filenames.
- The default data stream of a regular file is a stream of type $DATA but with an anonymous name, and the ADSs are similar but must be named.
- On the other hand, the default data stream of directories has a distinct type, but are not anonymous: they have an attribute name ("$I30" in NTFS 3+) that reflects its indexing format.

All attributes of a given file may be displayed by using the nfi.exe ("NTFS File Sector Information Utility") that is freely distributed as part of the Microsoft "OEM Support Tools".

Windows system calls may handle alternate data streams. Depending on the operating system, utility and remote file system, a file transfer might silently strip data streams. A safe way of copying or moving files is to use the BackupRead and BackupWrite system calls, which allow programs to enumerate streams, to verify whether each stream should be written to the destination volume and to knowingly skip unwanted streams.

### Resident vs. non-resident attributes

To optimize the storage and reduce the I/O overhead for the very common case of attributes with very small associated value, NTFS prefers to place the value within the attribute itself (if the size of the attribute does not then exceed the maximum size of an MFT record), instead of using the MFT record space to list clusters containing the data; in that case, the attribute will not store the data directly but will just store an allocation map (in the form of *data runs*) pointing to the actual data stored elsewhere on the volume. When the value can be accessed directly from within the attribute, it is called "resident data" (by computer forensics workers). The amount of data that fits is highly dependent on the file's characteristics, but 700 to 800 bytes is common in single-stream files with non-lengthy filenames and no ACLs.

- Some attributes (such as the preferred filename, the basic file attributes) cannot be made non-resident. For non-resident attributes, their allocation map must fit within MFT records.
- Encrypted-by-NTFS, sparse data streams, or compressed data streams cannot be made resident.
- The format of the allocation map for non-resident attributes depends on its capability of supporting sparse data storage. In the current implementation of NTFS, once a non-resident data stream has been marked and converted as sparse, it cannot be changed back to non-sparse data, so it cannot become resident again, unless this data is fully truncated, discarding the sparse allocation map completely.
- When a non-resident attribute is so fragmented that its effective allocation map cannot fit entirely within one MFT record, NTFS stores the attribute in multiple records. The first one among them is called the base record, while the others are called extension records. NTFS creates a special attribute $ATTRIBUTE_LIST to store information mapping different parts of the long attribute to the MFT records, which means the allocation map may be split into multiple records. The $ATTRIBUTE_LIST itself can also be non-resident, but its own allocation map must fit within one MFT record.
- When there are too many attributes for a file (including ADS's, extended attributes, or security descriptors), so that they cannot fit all within the MFT record, extension records may also be used to store the other attributes, using the same format as the one used in the base MFT record, but without the space constraints of one MFT record.

The allocation map is stored in a form of *data runs* with compressed encoding. Each data run represents a contiguous group of clusters that store the attribute value. For files on a multi-GB volume, each entry can be encoded as 5 to 7 bytes, which means a 1 KB MFT record can store about 100 such data runs. However, as the $ATTRIBUTE_LIST also has a size limit, it is dangerous to have more than 1 million fragments of a single file on an NTFS volume, which also implies that it is in general not a good idea to use NTFS compression on a file larger than 10 GB.

The NTFS file system driver will sometimes attempt to relocate the data of some of the attributes that can be made non-resident into the clusters, and will also attempt to relocate the data stored in clusters back to the attribute inside the MFT record, based on priority and preferred ordering rules, and size constraints.

Since resident files do not directly occupy clusters ("allocation units"), it is possible for an NTFS volume to contain more files on a volume than there are clusters. For example, a 74.5 GB partition NTFS formats with 19,543,064 clusters of 4 KB. Subtracting system files (a 64 MB log file, a 2,442,888-byte Bitmap file, and about 25 clusters of fixed overhead) leaves 19,526,158 clusters free for files and indices. Since there are four MFT records per cluster, this volume theoretically could hold almost 4 × 19,526,158 = 78,104,632 resident files.

### Opportunistic locks

Opportunistic file locks (oplocks) allow clients to alter their buffering strategy for a given file or stream in order to increase performance and reduce network use. Oplocks apply to the given open stream of a file and do not affect oplocks on a different stream.

Oplocks can be used to transparently access files in the background. A network client may avoid writing information into a file on a remote server if no other process is accessing the data, or it may buffer read-ahead data if no other process is writing data.

Windows supports four different types of oplocks:

- Level 2 (or shared) oplock: multiple readers, no writers (i.e. read caching).
- Level 1 (or exclusive) oplock: exclusive access with arbitrary buffering (i.e. read and write caching).
- Batch oplock (also exclusive): a stream is opened on the server, but closed on the client machine (i.e. read, write and handle caching).
- Filter oplock (also exclusive): applications and file system filters can "back out" when others try to access the same stream (i.e. read and write caching) (since Windows 2000)

Opportunistic locks have been enhanced in Windows 7 and Windows Server 2008 R2 with per-client oplock keys.

### Time

Windows NT and its descendants keep internal timestamps as UTC and make the appropriate conversions for display purposes; all NTFS timestamps are in UTC.

For historical reasons, the versions of Windows that do not support NTFS all keep time internally as local zone time, and therefore so does the FAT file system. This means that when files are copied or moved between NTFS and FAT partitions, the OS needs to convert timestamps on the fly. But if some files are moved when daylight saving time (DST) is in effect, and other files are moved when standard time is in effect, there can be some ambiguities in the conversions. As a result, especially shortly after one of the days on which local zone time changes, users may observe that some files have timestamps that are incorrect by one hour. Due to the differences in implementation of DST in different jurisdictions, this can result in a potential timestamp error of up to 4 hours in any given 12 months.

This problem is further exacerbated for any computers for which local time zone changes sometimes (e.g. due to moving the computer from one time zone to another, as often happens with laptops and other portable devices).

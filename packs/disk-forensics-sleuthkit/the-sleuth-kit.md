---
title: "The Sleuth Kit"
source: https://en.wikipedia.org/wiki/The_Sleuth_Kit
domain: disk-forensics-sleuthkit
license: CC-BY-SA-4.0
tags: disk forensics sleuth kit, file system forensic analysis, forensic disk imaging, file carving recovery, write blocker acquisition
fetched: 2026-07-02
---

# The Sleuth Kit

**The Sleuth Kit** (**TSK**) is an open-source library and collection of utilities for Unix-like operating systems and Windows that is used for extracting and parsing data from disk drives and other computer data storage devices so as to facilitate the forensic analysis of computer systems. It forms the foundation for Autopsy, a better known tool that is essentially a graphical user interface to the command line utilities bundled with The Sleuth Kit.

The software is under active development and it is supported by a team of developers. The initial development was done by Brian Carrier who based it on The Coroner's Toolkit. It is the official successor platform.

The Sleuth Kit is capable of parsing NTFS, FAT, ExFAT, UFS versions 1 and 2, Ext2, Ext3, Ext4, HFS, ISO 9660 and YAFFS2 file systems either on disk or within whole disk or disk partition images stored in raw form (as can be obtained with dd), or Expert Witness or AFF formats. The Sleuth Kit can be used to examine the contents of most computers that run Microsoft Windows, macOS, or Linux and some other computers which run derivatives of Unix such as the BSDs or Solaris.

The Sleuth Kit can be used via the included command line tools, or as a library embedded within a separate digital forensic tool such as Autopsy or log2timeline/plaso.

## Tools

Some of the tools included in The Sleuth Kit include:

- **ils** lists filesystem metadata entries, such as Inodes.
- **blkls** displays data blocks within a file system (formerly called dls).
- **fls** lists file names (including names corresponding to hidden or deleted files that have not yet been overwritten) within a file system.
- **fsstat** displays statistical information about a file system.
- **ffind** searches for file names that point to a specified metadata entry.
- **mactime** creates a timeline of all files based upon their MAC times.
- **disk_stat** (currently Linux-only) discovers the existence of a Host Protected Area.

## Applications

The Sleuth Kit can be used

- for use in forensics, its main purpose
- for understanding what data is stored on a disk drive, even if the operating system has removed all metadata.
- for recovering deleted image files
- summarizing all deleted files
- search for files by name or included keyword
- for use by future historians dealing with computer storage devices

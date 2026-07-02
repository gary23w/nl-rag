---
title: "Directory (computing)"
source: https://en.wikipedia.org/wiki/Directory_(computing)
domain: gitignore-patterns
license: CC-BY-SA-4.0
tags: gitignore patterns, git ignore rules, glob ignore patterns, version control exclusion
fetched: 2026-07-02
---

# Directory (computing)

In computing, a **directory** is a file system cataloging structure that contains references to other computer files, and possibly other directories. On many computers, directories are known as **folders** or **drawers**, analogous to a workbench or the traditional office filing cabinet. The name derives from books like a telephone directory that lists the phone numbers of all the people living in a certain area.

Files are organized by storing related files in the same directory. In a hierarchical file system (that is, one in which files and directories are organized in a manner that resembles a tree), a directory contained inside another directory is called a **subdirectory**. The terms **parent** and **child** are often used to describe the relationship between a subdirectory and the directory in which it is cataloged, the latter being the parent. The top-most directory in such a filesystem, which does not have a parent of its own, is called the **root** directory.

The freedesktop.org media type for directories within many Unix-like systems – including but not limited to systems using GNOME, KDE Plasma 5, or ROX Desktop as the desktop environment – is "inode/directory". This is not an IANA registered media type.

## Overview

Historically, and even on some modern embedded systems, the file systems either had no support for directories at all or had only a "flat" directory structure, meaning subdirectories were not supported; there was only a group of top-level directories, each containing files. In modern systems, a directory can contain a mix of files and subdirectories.

A reference to a location in a directory system is called a path.

In many operating systems, programs have an associated working directory in which they execute. Typically, file names accessed by the program are assumed to reside within this directory if the file names are not specified with an explicit directory name.

Some operating systems restrict a user's access only to their home directory or project directory, thus isolating their activities from all other users. In early versions of Unix, the root directory was the home directory of the root user, but modern Unix usually uses another directory such as /root for this purpose.

In keeping with Unix philosophy, Unix systems treat directories as a type of file. Caveats include not being able to write to a directory file except indirectly by creating, renaming, and removing file system objects in the directory and only being able to read from a directory file using directory-specific library routines and system calls that return records, not a byte-stream.

### Folder metaphor

The name *folder*, presenting an analogy to the file folder used in offices, and used in a hierarchical file system design for the Electronic Recording Machine, Accounting (ERMA) Mark 1 published in 1958 as well as by Xerox Star, is used in almost all modern operating systems' desktop environments. Folders are often depicted with icons that visually resemble physical file folders.

There is a difference between a *directory*, which is a file system concept, and the graphical user interface metaphor that is used to represent it (a *folder*). For example, Microsoft Windows uses the concept of special folders to help present the contents of the computer to the user in a fairly consistent way that frees the user from having to deal with absolute directory paths, which can vary between versions of Windows, and between individual installations. Many operating systems also have the concept of "smart folders" or virtual folders that reflect the results of a file system search or other operation. These folders do not represent a directory in the file hierarchy. Many email clients allow the creation of folders to organize email. These folders have no corresponding representation in the filesystem structure.

If one is referring to a *container of documents*, the term *folder* is more appropriate. The term *directory* refers to the way a structured list of document files and folders are stored on the computer. The distinction can be due to the way a directory is accessed; on Unix systems, /usr/bin/ is usually referred to as a directory when viewed in a command line console, but if accessed through a graphical file manager, users may sometimes call it a folder.

## Lookup cache

Operating systems that support hierarchical file systems implement a form of caching in RAM to speed up file path resolution. This mechanism reduces the overhead associated with repeatedly traversing file system hierarchies to resolve pathnames into inode references.

In Unix-like systems, this may be called the **directory name lookup cache** (DNLC), **directory entry cache**, or **dcache**.

### Overview

Directory lookup caches store mappings between absolute or relative path components (such as `/usr/bin`) and their corresponding inode or directory entry objects. This allows the system to bypass full path traversal for frequently accessed files or directories, dramatically improving performance for workloads with heavy metadata operations.

The cache is typically implemented using fast lookup structures such as hash tables or radix trees, and may utilize aging algorithms such as LRU for cache eviction.

### Historical background

SunOS introduced a lookup cache as part of the implementation of NFS; however, it was not only used by NFS. It has since been adapted and extended in systems such as Linux, BSD, Solaris, and macOS.

### Implementations

#### Windows

Windows uses internal path caching mechanisms as part of its NTFS and kernel object manager layers, though these are not always exposed directly.

#### BSD variants

BSD variants, including FreeBSD, NetBSD, OpenBSD, and DragonFly BSD implement directory lookup caches.

#### macOS

macOS integrates lookup caching into its VFS layer.

#### Linux

The Linux kernel's Virtual File System (VFS) layer uses a structure called the **dcache** to cache directory entry objects (delete). Each dentry links to an inode and can represent a file or subdirectory. These dentries are organized in a tree structure that mirrors the directory hierarchy and are stored in memory as long as there is no memory pressure.

In delete to speeding up file lookups, the dcache also plays a role in maintaining consistency across mounted file systems, including complex setups with overlays or bind mounts.

### Cache coherence in distributed file systems

For distributed file systems such as NFS or AFS, the cache must remain coherent across multiple clients. In such systems, a change made on one client must be reflected in other clients' lookup caches. To achieve this, network file systems use a variety of mechanisms:

- Attribute timeouts
- Lease-based locking (e.g., NFSv4 delegations)
- Callback invalidations (e.g., AFS)

Failure to ensure coherence may result in stale file metadata or incorrect path resolution, leading to application errors or data loss.

### Performance impact

Optimized directory lookup caches can significantly reduce system call latency for file operations such as `open()`, `stat()`, and `execve()`. In benchmark tests, systems with aggressive dentry caching have shown orders-of-magnitude improvements in access times for large codebases and system boot times.

---
title: "File-system permissions"
source: https://en.wikipedia.org/wiki/File-system_permissions
domain: landlock-lsm
license: CC-BY-SA-4.0
tags: landlock unprivileged sandbox, filesystem access restriction, self restricting process sandbox, linux security module ruleset
fetched: 2026-07-02
---

# File-system permissions

Typically, a file system maintains **permission** settings for each stored item – commonly files and directories – that either grant or deny the ability to manipulate file system items. Often the settings allow controlling access based on function such as read, change, navigate, and execute and to different users and groups of users.

One well-established technology was developed for Unix, later codified by POSIX and is used in Linux. Another common technology is an access-control list (ACL) with multiple variants implemented in file systems and one codified by POSIX. Since POSIX defines both the older Unix-based technology as well as ACLs, the former is called *traditional POSIX permissions* for clarity even though it is not a well-known term.

A permission-driven user interface tailors the functionality available to the user based on file system item permissions. For example, the interface might hide menu options that are not allowed based on the permissions stored for an item.

## History

### CTSS

An early time-sharing system, the Compatible Time-Sharing System (CTSS), supported multiple users; each user's account had a "problem number" and "programmer number".

The first version of the CTSS file system supported only two "read-only" file modes, one of which can be unset by the user and the other of which can only be unset with edit cards submitted to the computer center. Files can be shared between users in the same project; shared files are assigned to programmer number zero. There is no protection other than that provided by the read-only bits.

The second version of the file system has separate permission bits for "read-only" and "write-only"; the latter allows only appending to the file. It also has a "private" bit, allowing only the author of the file to access it, and a "protected" bit, allowing only the author of the file to change the file's permissions.

### Multics

Users on the Multics time-sharing system have a "Person_id", and projects have a "Project_id"; a user logs on to the system with their Person_id and a Project_id. A file has an access control list (ACL), with entries containing a Person_id or a "*", a Project_id or a "*", and an "instance tag" or a "*". An instance tag represents a type of process; an "a", for example, represents a process from a regular interactive session. The entries in an ACL are matched against the process's Person_id, Project_id, and instance tag; an "*" is a wildcard that matches all Person_ids, Project_Ids, or instance tags. The ACL entry that matches with the fewest wildcards is the one that is used.

An ACL for a file has access permissions of "read", "write", and "execute"; an ACL for a directory has access permissions of "status" (allows reading attributes of files and directories in the directory), "modify" (allows modification of attributes of files and directories in the directory and removing items from the directory), and "append" (allows adding new items to the directory).

### TENEX

A user in TENEX belongs to a set of groups.

A file or directory has a set of permission bits, with six bits for permissions for the file or directory's owner, six bits for permissions for other users in the file's or directory's group, and six bits for other users. For a file, the permission bits are "read", "write", "execute", "append", and "each page of the file has its own permissions", with the sixth bit not being used. For a directory, the permission bits are "access allowed" (if not set, no access to the directory is allowed), "files in the directory may be opened" (subject to the file's permission bits), "owner-like functions may be performed without the file's password", and "files may be added to the directory", with the fifth and sixth bits not being used.

### TOPS-10

A user account in TOPS-10 has a programmer number and a project number.

A file has a set of permission bits, with three bits for permissions for the file's owner, three bits for permissions for other users with the same project number as the owner, and three bits for all other users. The operating system may be configured to treat any account with a programmer number that is the same as the programmer number of the containing directory as the owner or to treat only an account with the same programmer number and project number as those of the containing directory as the owner. The values for the permission bits are:

- 7 - no access privileges, except that the owner may look up the file in order to change its permissions;
- 6 - execute-only;
- 5 - read and execute;
- 4 - append, read, and execute;
- 3 - update, append, read, and execute;
- 2 - write, update, append, read, and execute;
- 1 - rename, write, update, append, read, and execute;
- 0 - change permissions, rename, write, update, append, read, and execute.

The owner is always allowed to change the permissions.

### UNIX and Unix-like systems

Files in the first edition of Unix (v1) had five bits of permission:

- write, non-owner;
- read, non-owner;
- write, owner;
- read, owner;
- executable;

and a set-UID bit. It had no notion of groups. This continued until the third edition (v3); the fourth edition (v4) introduced groups, and files in v4 had nine bits of permission:

- read, owner;
- write, owner;
- execute, owner;
- read, group;
- write, group;
- execute, group;
- read, other;
- write, other;
- execute, other;

as well as a set-UID and set-GID bit; This is the same set of permissions that are specified in POSIX and that are provided by current Unix and Unix-like systems.

## Examples

File system permissions have been implemented many ways. Some notable examples are described here.

NTFS which is in many versions of Windows including the current, uses ACLs to provide permission-based access control; NTFS ACLs are considered powerful yet complex.

Linux file systems such as ext2, ext3, ext4, Btrfs support both POSIX permissions and POSIX.1e ACLs. There is experimental support for NFSv4 ACLs for ext3 and ext4 filesystems.

FreeBSD supports POSIX.1e ACLs on UFS, and NFSv4 ACLs on UFS and ZFS.

HFS, and its successor HFS+, as implemented in the Classic Mac OS operating systems, do not support permissions.

macOS supports POSIX-compliant permissions, and supports them in both HFS+ and APFS. Beginning with version 10.4 ("Tiger"), it also supports the use of NFSv4 ACLs in addition to POSIX-compliant permissions. The *Apple Mac OS X Server version 10.4+ File Services Administration Manual* recommends using only traditional Unix permissions if possible. macOS also still supports the Classic Mac OS's "Protected"/"Locked" attribute as the "user immutable" flag in the 4.4BSD flags field.

File Allocation Table (original version) has a per-file read-only attribute that applies to all users.

OpenVMS defines four access functions: read, write, execute and delete and user selections: system, owner, group, and world where world includes group which in turn includes owner and system selects system users. This design is similar to that of Unix with notable extensions: additional function: delete and additional user selection: system. ACLs are supported in VMS 4.0 and later.

Solaris ACL support depends on the filesystem being used; the older UFS filesystem supports POSIX.1e ACLs, while ZFS supports only NFSv4 ACLs.

IBM z/OS implements file security using RACF (Resource Access Control Facility)

The AmigaOS Filesystem, AmigaDOS supports a permissions system relatively advanced for a single-user OS. In AmigaOS 1.x, files had Archive, Read, Write, Execute and Delete (collectively known as ARWED) permissions/flags. In AmigaOS 2.x and higher, additional Hold, Script, and Pure permissions/flags were added.

OpenHarmony operating system alongside its client side ecosystem in Oniro OS and HarmonyOS with HarmonyOS NEXT versions and also Linux-based openEuler server OS natively uses its Harmony Distributed File System (HMDFS) that supports access token manager (role-based access control) and Core File Kit API capability-based with granular permission management with exception to openEuler that is fine grained.

## Traditional POSIX permissions

Traditionally, file permissions on a Unix-based file system are defined by POSIX.1. It specifies three classes (user, group and others) that allow for mapping permissions to users and three operations (read, write, execute) that can be granted or denied for each class. When a file is created, its permissions default to that as accessible via the `umask` command.

In a Unix-based file system, everything is a file, even directories and other special files.

### Classes

The classes determine how permissions map to a user. The *user class* permissions apply to the user who owns the file. The *group class* permissions apply to users of the file's owning group. The *others class* applies to other users.

The *effective permissions* are the permissions of the class in which the user falls *first* given the order: user, group then others. For example, the owning user has effective permissions of the user class even if they are in the owning group.

### Permissions

The following permissions grant the corresponding operations on files and directories:

#### Read (r)

- For files: grants the ability to read the file’s contents (not its name or metadata, which are determined by the permissions of its parent directory).
- For directories: grants the ability to read the directory entry names of its contained files and directories, but not to access their metadata (inode) and therefore their content, which is determined by the directory *execute* permission.

#### Write (w)

- For files: grants the ability to modify the file contents.
- For directories: grants the ability to modify entries in the directory, which allows creating, deleting, and renaming its files or directories.
  - Doing so also requires the *execute* permission in order to access the metadata (inode) of all its containing files and directories. Therefore, without *execute* permission the *write* permission is effectively meaningless.

#### Execute (x)

- For files: grants the ability to execute a file. This permission must be set for executable programs to allow running them.
  - Doing so also requires the *read* permission.
- For directories: grants the ability to read the metadata of its containing files and directories if their names are known, but not to read their names. A directory without *execute* permission effectively blocks reading and writing the content of its contained files and directories.
  - A directory with *execute* permission but without *read* permission effectively makes it a name guessing game to access the contents of its files and directories.

#### General access requirement inside directories

Accessing the content of file or directory inside a directory requires:

1. Knowing its name which is discoverable if the parent directory *read* permission is set (or by guessing its name).
2. The parent directory *execute* permission to access the file or directory inode.
3. Its corresponding *read*, *write* or *execute* permissions.

#### Permission requirement summary for file operations

To read from a file you need:

- The file *read* permission.
- *Execute* permission on its parent directory .

To write to a file you need:

- The file *write* permission.
- *Execute* permission on its parent directory .

To execute a file you need:

- The file *read* and *execute* permission.
- *Execute* permission on its parent directory .

To know the name of the file you need:

- *Read* permission of its parent directory .

To add, remove, or rename a file you need:

- *write, and execute* permission on its parent directory.

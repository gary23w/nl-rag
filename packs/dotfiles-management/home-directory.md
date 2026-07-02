---
title: "Home directory"
source: https://en.wikipedia.org/wiki/Home_directory
domain: dotfiles-management
license: CC-BY-SA-4.0
tags: dotfiles management, unix dotfiles, hidden config files, shell config files
fetched: 2026-07-02
---

# Home directory

A **home directory** is a file system directory on a multi-user operating system containing files for a given user of the system. The specifics of the home directory (such as its name and location) are defined by the operating system involved; for example, Linux / BSD (FHS) systems use `/home/⟨username⟩` or `/usr/home/⟨username⟩`, macOS uses `/Users/⟨username⟩`, and Windows systems since Windows Vista use `\Users\⟨username⟩`.

## Description

A user's home directory is intended to contain that user's files; including text documents, music, pictures, videos, etc. It may also include their configuration files of preferred settings for any software they have used there and might have tailored to their liking: web browser bookmarks, favorite desktop wallpaper and themes, stored passwords to any external services accessed via a given software, etc. The user can install executable software in this directory, but it will only be available to users with permission to execute files in this directory. The home directory can be organized further with the use of sub-directories.

The content of a user's home directory is protected by file-system permissions, and by default is accessible to all authenticated users and administrators. Any other user that has been granted administrator privileges has authority to access any protected location on the file system including other users' home directories.

## Benefits

Separating user data from system-wide data avoids redundancy (the same system files can be used by between different users) and makes backups of files that are important for a specific user simpler.

Furthermore, Trojan horses, viruses, and worms running under the user's name and with their privileges will in most cases only be able to alter the files in the user's home directory, and perhaps some files belonging to workgroups the user is a part of, but not actual system files, reducing the chances of harming the functioning of the operating system.

## Location

| Operating system | Path | Environment variable |
|---|---|---|
| AT&T Unix (original version) | `/usr/⟨username⟩` | `$HOME` |
| Unix-derived | `/var/users/⟨username⟩` `/u01/⟨username⟩` `/usr/⟨username⟩` `/user/⟨username⟩` `/users/⟨username⟩` |   |
| Unix-based | `/home/⟨username⟩` |   |
| BSD / Linux (FHS) | `/home/⟨username⟩` or `/usr/home/⟨username⟩` |   |
| SunOS / Solaris | `/export/home/⟨username⟩` |   |
| macOS | `/Users/⟨username⟩` |   |
| Android | `/data/media/⟨userid⟩` |   |
| Windows NT 4.0 | `(windows-directory)\Profiles\⟨username⟩` | `%USERPROFILE%` `%HOMEDRIVE%%HOMEPATH%` |
| Windows 2000, XP, and Server 2003 | `\Documents and Settings\⟨username⟩` |   |
| Windows Vista and later | `\Users\⟨username⟩` |   |

### Super-user's home directory

In most operating systems, the superuser usually have a different location for the home directory than regular users. The superuser is usually *root* in Unix-like systems, and *SYSTEM* in Windows NT.

| Operating system | Path |
|---|---|
| Solaris 10 or earlier | `/` |
| Solaris 11 | `/root` |
| macOS | `/var/root` |
| Other Unix-like system | `/` `/root` |
| Windows NT | `(windows-directory)\system32\config\systemprofile` |

### Subdirectories

The file `/etc/xdg/user-dirs.defaults` on many Linux systems defines the subdirectories created for users by default. Creation is normally done with the first login by Xdg-user-dirs, a tool to help manage "well known" user directories like *desktop*, *downloads*, *documents*, *pictures*, *videos*, or *music*. The tool is also capable of localization (i.e. translation) of the folders' names.

1. (windows-directory) is *WINNT* by default in Windows NT 4.0.

## Other features

### Unix

In Unix, the working directory is automatically set to a user's home directory when they log in. In many built-in commands, typing the `~` (tilde) character is equivalent to specifying the current user's home directory.

The Unix superuser has access to all directories on the file system, and hence can access home directories of all users. The superuser's home directory on older systems was /, but on many newer systems it is located at /root (Linux, BSD), or /var/root (macOS).

### VMS

In the OpenVMS operating system, a user's home directory is called the *root directory*, and the equivalent of a Unix/DOS/Windows/AmigaOS *root directory* is referred to as the *Master File Directory*.

## Single-user operating systems

Single-user operating systems simply have a single directory or partition for all user files, there is no individual directory setup per user (though users can still setup and maintain directories inside this main working directory manually).

- AmigaOS versions 2 and up have "System" and "Work" partitions on hard disks by default.
- BeOS (and its successors) have a /home directory which contains the files belonging to the single user of the system.
- Versions of Windows prior Windows 95 OEM Service Release 2 did not have a user folder but, since that release, C:\My Documents became in-effect the single user's home directory.
- NeXTSTEP and OPENSTEP in a single-user, non-networked setup, `/me` is used, as well as `/root` when logged in as superuser.

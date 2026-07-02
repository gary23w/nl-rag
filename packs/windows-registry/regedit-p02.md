---
title: "Windows Registry (part 2/2)"
source: https://en.wikipedia.org/wiki/Regedit
domain: windows-registry
license: CC-BY-SA-4.0
tags: windows registry, registry editor, registry hive, group policy
fetched: 2026-07-02
part: 2/2
---

## Equivalents and alternatives

In Windows, use of the registry for storing program data is a matter of developer's discretion. Microsoft provides programming interfaces for storing data in XML files (via MSXML) or database files (via SQL Server Compact) which developers can use instead. Developers are also free to use non-Microsoft alternatives or develop their own proprietary data stores.

In contrast to Windows Registry's binary-based database model, some other operating systems use separate plain-text files for daemon and application configuration, but group these configurations together for ease of management.

- In Unix-like operating systems (including Linux) that follow the Filesystem Hierarchy Standard, system-wide configuration files (information similar to what would appear in HKEY_LOCAL_MACHINE on Windows) are traditionally stored in files in /etc/ and its subdirectories, or sometimes in /usr/local/etc/. Per-user information (information that would be roughly equivalent to that in HKEY_CURRENT_USER) is stored in hidden directories and files (that start with a period/full stop) within the user's home directory. However XDG-compliant applications should refer to the environment variables defined in the Base Directory specification.
- In macOS, system-wide configuration files are typically stored in the /Library/ folder, whereas per-user configuration files are stored in the corresponding ~/Library/ folder in the user's home directory, and configuration files set by the system are in /System/Library/. Within these respective directories, an application typically stores a property list file in the Preferences/ sub-directory.
- RISC OS (not to be confused with *MIPS RISC/os*) uses directories for configuration data, which allows applications to be copied into application directories, as opposed to the separate installation process that typifies Windows applications; this approach is also used on the ROX Desktop for Linux. This directory-based configuration also makes it possible to use different versions of the same application, since the configuration is done "on the fly". If one wishes to remove the application, it is possible to simply delete the folder belonging to the application. This will often not remove configuration settings which are stored independently from the application, usually within the computer's !Boot structure, in !Boot Choices or potentially anywhere on a network fileserver. It is possible to copy installed programs between computers running RISC OS by copying the application directories belonging to the programs, however some programs may require re-installing, e.g. when shared files are placed outside an application directory.
- IBM AIX (a Unix variant) uses a registry component called Object Data Manager (ODM). The ODM is used to store information about system and device configuration. An extensive set of tools and utilities provides users with means of extending, checking, correcting the ODM database. The ODM stores its information in several files, default location is /etc/objrepos.
- The GNOME desktop environment uses a registry-like interface called dconf for storing configuration settings for the desktop and applications.
- The Elektra Initiative provides alternative back-ends for various different text configuration files.
- While not an operating system, the Wine compatibility layer, which allows Windows software to run on a Unix-like system, also employs a Windows-like registry as text files in the WINEPREFIX folder: system.reg (HKEY_LOCAL_MACHINE), user.reg (HKEY_CURRENT_USER) and userdef.reg. The format is virtually the same as those of Windows .REG files, except that the header line is changed to "WINE REGISTRY Version 2" and paths (keys) do not start with the name of the hive.

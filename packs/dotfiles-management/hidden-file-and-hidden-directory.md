---
title: "Hidden file and hidden directory"
source: https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory
domain: dotfiles-management
license: CC-BY-SA-4.0
tags: dotfiles management, unix dotfiles, hidden config files, shell config files
fetched: 2026-07-02
---

# Hidden file and hidden directory

In computing, a **hidden file** or **hidden directory** is a file system object (such as a file or directory) that is excluded from a directory content report unless explicitly requested. The value of hiding files is generally to avoid showing the user files that are not likely to be of interest to them. The feature is not a security mechanism because access is not restricted; the user can request that normally-hidden files be displayed. Hiding is a feature of the programs that display file system objects, not a feature of file systems or of the operating system as a whole.

## Unix and Unix-like environments

The Unix-based `ls` shell command hides any file that starts with a dot (commonly called a **dot file** or **dotfile**) unless the option `-a` or `-A` is specified. Even with wildcard matching, the command does not match a dotfile unless the expression starts with `.` For example, `*f*` does not match `.foo`, but `.f*` does.

According to Rob Pike, dotfiles were an unintended consequence of the implementation of the hierarchical file system during the Unix 2nd Edition re-write, which introduced `.` as a name in a directory that refers to the directory itself and `..` as a name in a directory that refers to its parent directory. In order to exclude those two entries from `ls` output, all entries prefixed with `.` were omitted. This meant that any file or directory could be excluded from the output of `ls` by giving it a file name with `.` as the first character.

Commonly, user-specific application configuration information is stored in the user's home directory as a dotfile. Notable dotfiles include startup shell scripts such as `.profile`, `.login`, and `.cshrc` as well as `.plan` and `.project` which are used by the `finger` and `name` commands. Many applications, from bash to desktop environments such as GNOME, store user-specific configuration this way, but the *XDG Base Directory Specification* aims to migrate such config files to be non-hidden (not starting with `.`) but stored in a hidden directory `$HOME/.config`.

### Android

The Android operating system provides empty .nomedia files as a hint to apps to exclude the content of the folder. This convention prevents photo and music files from appearing in picture galleries or played in MP3 player apps. This is useful to prevent downloaded voicemail files from playing between the songs in a playlist and to keep personal photos private while still allowing those in other folders to be shared freely.

This convention is not enforced by the file or operating systems. Each app is responsible for following the convention.

### GNOME

In the GNOME desktop environment (as well as programs using GLib), filenames listed in a file named .hidden are excluded from the directory containing the file. In the file manager, keyboard shortcut Ctrl+H includes both dotfiles and files listed in .hidden.

### macOS

In addition to the dotfile behaviour, files with the invisible attribute are excluded by Finder although not by `ls`.

The invisible attribute can be set or cleared via the `SetFile` command. For example, command line `SetFile -a V jimbo` hides the file jimbo. Starting in Snow Leopard, the `chflags` command can also be used. For example, `chflags hidden jimbo` is equivalent.

## Windows and DOS

The FAT, NTFS, and ReFS file systems, which have originated from DOS and Windows, maintain two file attributes called "hidden" and "system" for each item. Items with these attributes are hidden.

### Command Prompt

In Windows Command Prompt, the `dir` command excludes items that have either the "hidden" or "system" attributes. If invoked with the `/a` command-line switch, the command shows all items, even the hidden ones. Its variations `/as` and `/ah` respectively display files with the "system" and "hidden" attributes.

The `attrib.exe` command-line utility, included will all versions of MS-DOS and Windows, can set or clear attributes.

### File Explorer

File Explorer controls visibility based on user settings that are accessible from its toolbar (or via the Control Panel). By Default, File Explorer excludes items with the "hidden" attribute, but can reveal them if the "Show hidden files, folders, or drives" is set. Items with the "System" attribute remain hidden unless another setting, called "Hide protected operating system files (Recommended)," is cleared. File Explorer renders the icons of hidden items semi-transparently.

A Windows Shell hack allows one to hide the content of a folder by suffixing a pre-defined CLSID to its name. The folder is still visible in File Explorer, but its content becomes one of the Windows special folders. This hack is restricted to File Explorer and Windows Shell API. Any app that doesn't use the Shell API (including the bundled Windows Command Prompt and PowerShell) can see the folder, its name, and its content.

## PowerShell (cross-platform)

PowerShell started out as the successor Windows Command Prompt for Microsoft Windows, but is now a cross-platform, free, and open-source shell.

The `Get-ChildItem` cmdlet, by default, doesn't display hidden items, unless configured to do so via parameters. With the `-Force` parameter, the cmdlet displays all items, including hidden ones. With the `-Hidden` parameter, the cmdlet displays only hidden items, excluding ordinary items. The cmdlet also features a `-Attributes` parameters that allows granular filtering by specific attributes.

The `Get-ItemProperty` and `Set-ItemProperty` cmdlets can query or modify the `Attributes` property of each file or directory.

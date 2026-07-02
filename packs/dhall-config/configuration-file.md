---
title: "Configuration file"
source: https://en.wikipedia.org/wiki/Configuration_file
domain: dhall-config
license: CC-BY-SA-4.0
tags: dhall config, dhall language, total functional configuration, typed config language
fetched: 2026-07-02
---

# Configuration file

A **configuration file**, also known as **config file**, is a file that stores data used to configure a software system such as an application, a server or an operating system.

Some applications provide a tool to create, modify, and verify the syntax of their configuration files – sometimes via graphical user interface (GUI). For context, system administrators may be expected to create and modify text config files via a text editor. For server processes and operating-system settings, there is often no standard tool, but operating systems may provide graphical interfaces such as YaST or debconf.

Some computer programs only read their configuration files at startup. Others periodically check the configuration files for changes. Users can instruct some programs to re-read the configuration files and apply the changes to the current process, or indeed to read arbitrary files as a configuration file. There are no definitive standards or strong conventions.

## File format

In general, a config file can have any format. The format that applies to a particular system is determined by the design of that system. Often, a standardized format is used since it allows for using tools designed for the format even if not designed for the consuming system. In particular, general-purpose serialization formats, such as JSON, XML, and YAML, are often used in open-source and platform-neutral software. The specifications for these formats are generally publicly available to support wide-spread use.

The following table compares notable formats used for configuration data.

| Format | Formal spec | Allows comments | Syntax typing |
|---|---|---|---|
| INI | No | Yes | No |
| JSON | Yes | No | Yes |
| TOML | Yes | Yes | Yes |
| UCL | No | Yes | Yes |
| YAML | Yes | Yes | Yes |
| XML | Yes | Yes | No |

The *syntax typing* column indicates whether the syntax supports data types. A format has syntax-typing if a value's type is specified by syntax – e.g. `true` is a Boolean while `"true"` is a string. A format does not have syntax-typing if a value's type is based on semantics – e.g. `true` and `"true"` are both Boolean if the parser expects a Boolean. Opinions on the value of syntax-typing vary.

## Examples

The following are examples of config files organized by the operating systems on which they are commonly used.

### Unix and Unix-like

Many different file formats are used on Unix and Unix-like operating systems. Even so, there is a strong tradition of using human-editable, plain text formats including simple key–value pair. Filename extensions of `.cnf`, `.conf`, `.cfg`, `.cf` or `.ini` are often used.

Many formats allow comments, in which case, individual settings can be disabled by prepending with the comment character. Often the default configuration files contain extensive internal documentation in the form of comments and man files are also typically used to document the format and options available.

System-wide software often uses configuration files stored in `/etc`, while user applications often use a "dotfile" – a file or directory in the home directory prefixed with a period, which in Unix hides the file or directory from casual listing. Since this causes pollution, newer user applications generally make their own folder in the `.config` directory, a standardized subdirectory of the home directory.

Similar to config files, a run command (rc) shell script can configure a shell session. Often, such scripts are named with an `rc` suffix after the consuming program's name such as `.xinitrc`, `.vimrc`, `.bashrc`, `xsane.rc`.

By contrast, IBM's AIX uses an Object Data Manager (ODM) database to store much of its system settings.

### MS-DOS

MS-DOS primarily relied on the `CONFIG.SYS` config file, a plain text file with simple key–value pairs (e.g. `DEVICEHIGH=C:\DOS\ANSI.SYS`). MS-DOS 6 introduced the INI-file format. Similar to an rc file, the batch file named `AUTOEXEC.BAT` ran commands on startup. Both these files were retained up to Windows 98SE, which still ran on top of MS-DOS.

An example CONFIG.SYS:

```mw
DOS=HIGH,UMB
DEVICE=C:\DOS\HIMEM.SYS
DEVICE=C:\DOS\EMM386.EXE RAM
DEVICEHIGH=C:\DOS\ANSI.SYS
FILES=30
SHELL=C:\DOS\COMMAND.COM C:\DOS /E:512 /P
```

DOS applications used a wide variety of individual configuration files, most of them binary, proprietary and undocumented - and there were no common conventions or formats.

### Windows

Early Windows operating systems heavily utilized plain-text INI files which served as the primary mechanism to configure the operating system and applications. The APIs to read and write from these still exist in Windows, but after 1993, Microsoft began to steer developers away from using INI files and toward storing settings in the registry, a hierarchical database to store configuration settings, which was introduced with Windows NT. Later systems use XML and other formats instead of the registry.

### macOS

The Property List is the standard configuration file format in macOS (as well as in iOS, NeXTSTEP, GNUstep and Cocoa applications). It uses the filename extension `.plist`.

### IBM OS/2

IBM's OS/2 uses a binary format, also with a .INI suffix, but this differs from the Windows versions. It contains a list of lists of untyped key–value pairs. Two files control system-wide settings: OS2.INI and OS2SYS.INI. Application developers can choose whether to use them or to create a specific file for their applications.

### HarmonyOS and OpenHarmony operating systems

HarmonyOS and OpenHarmony-based operating systems use JSON config files, named `config.json`. The platform IDE, DevEco Studio, provides methods for editing `config.json`.

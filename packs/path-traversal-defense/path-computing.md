---
title: "Path (computing)"
source: https://en.wikipedia.org/wiki/Path_(computing)
domain: path-traversal-defense
license: CC-BY-SA-4.0
tags: directory traversal, path traversal defense, canonical path resolution, file access control
fetched: 2026-07-02
---

# Path (computing)

A **path** (or **filepath**, **file path**, **pathname**, or similar) is a string that uniquely identifies an item in a hierarchical file system. Generally, a path is composed of directory names, special format specifiers, and optionally a filename, all separated by delimiters. This delimiter can vary by operating system, but popular, modern systems use the slash `/`, backslash `\`, or colon `:`.

The case-sensitivity of individual path components will vary based on operating system, or based on options specified at the time of a file system's creation or first use. In practice, this means that for a **case-sensitive** system, path components named `component1` and `Component1` can coexist at the same level in the hierarchy, whereas for a **case-*in*sensitive** file system, they cannot (an error will occur). macOS and Windows' native file systems are case-insensitive by default, whereas typical Linux file systems are case-sensitive.

A path can be either **relative** or **absolute**. A relative path is a path in relation to another, most often the working directory. An absolute path indicates a location regardless of the current directory; that is, it specifies all path components starting from the file system's root, and does not depend on context like a relative path does.

Paths are also essential for locating hierarchically-organized network resources, as seen in URLs and UNC paths.

## History

Multics first introduced a hierarchical file system with directories (separated by ">") in the mid-1960s.

Around 1970, Unix introduced the slash `/` as its directory separator.

Originally, MS-DOS did not support directories. When adding the feature, using the Unix standard of a slash was not a good option since many existing commands used a slash as the switch prefix (i.e., `dir /w`). In contrast, Unix uses the dash `-` as the switch prefix. The backslash `\` was ultimately chosen instead for its similarity to the slash and not conflicting with existing commands. This convention continued into Windows. However, some areas of Windows do accept or understand Unix-style slashes also, such as PowerShell.

## Summary of systems

The following table describes the syntax of paths in notable operating systems:

| System | Root dir. | Path delim. | Working dir. | Parent dir. | Home dir. | Examples |
|---|---|---|---|---|---|---|
| Unix and Unix-like systems, including macOS | / | / | . | .. | ~ | /home/user/docs/Letter.txt ./child ../../greatgrandparent ~/.rcinfo |
| Windows, Command Prompt | \ (relative to current working directory root) or [drive letter]:\ or \\.\ or \\?\ or \\[Host name]\[Root name] (UNC) | / or \ | . | .. |   | C:\user\docs\Letter.txt /user/docs/Letter.txtC:\user\docs\somefile.ext:alternate stream name C:picture.jpg \\?\UNC\Server01\user\docs\Letter.txt \\.\COM1 |
| PowerShell | [drive letter]:/ or [drive name]:\ or [PSSnapIn name]\[PSProvider name]::[PSDrive root] or UNC | / or \ | . | .. | ~ | C:\user\docs\Letter.txt ~\DesktopUserDocs:/Letter.txt Variable:PSVersionTable Registry::HKEY_LOCAL_MACHINE\SOFTWARE\ Microsoft.PowerShell.Security\Certificate::CurrentUser\ |
| UNC | \\[server]\[sharename]\ | / |   |   |   | \\Server01\user\docs\Letter.txt |
| DOS, COMMAND.COM | [drive letter]:\ or \\[server name]\[volume]\ | \ | . | .. |   | C:\USER\DOCS\LETTER.TXT A:PICTURE.JPG \\SERVER01\USER\DOCS\LETTER.TXT |
| OS/2 | [drive letter]:\ or \\[server name]\[volume]\ | / or \ | . | .. |   | C:\user\docs\Letter.txt A:Picture.jpg \\SERVER01\USER\docs\Letter.txt |
| RSX-11 MCR | [device name]: |   |   |   |   | DR0:[30,12]LETTER.TXT;4 |
| TOPS-20 DCL | [device name]: | . |   |   |   | PS:<USER.DOCS>LETTER.TXT,4 |
| OpenVMS DCL | [device name]:[000000] or [NODE["accountname password"]]::[device name][000000]: | . | [] | [-] | SYS$LOGIN: | NODE$DISK:[USER.DOCS]PHOTO.JPGUSER:[000000]000000.DIR[]IN_THIS_DIR.COM; [-.-]GreatGrandParent.TXT SYS$SYSDEVICE:[.DRAFTS]LETTER.TXT;4 GEIN::[000000]LETTER.TXT;4 SYS$LOGIN:LOGIN.COM |
| ProDOS AppleSoft BASIC | /[volume or drive name]/ | / |   |   |   | /SCHOOL.DISK/APPLEWORKS/MY.REPORTFLIGHT.SIMULATOR,D2 |
| AmigaOS Amiga CLI / AmigaShell | [drive, volume, device, or assign name]: | / | *empty string* | / |   | Workbench:Utilities/MultiView DF0:S/Startup-Sequence S:Startup-Sequence TCP:en.wikipedia.com/80 |
| RISC OS ShellCLI | [fs type[#option]:][:drive number or disc name.]$ | . | @ | ^ | & | ADFS::MyDrive.$.Documents.Letter Net#MainServer::DataDrive.$.Main.sy10823 LanMan::WindowsC.$.Pictures.Japan/gif NFS:&.!Choices ADFS:%.IfThere @.inthisdir ^.^.greatgrandparent |
| Symbian OS File manager | \ | \ |   |   |   | \user\docs\Letter.txt |
| Domain/OS Shell | // (root of domain) or / (root of current node) | / | . | \ | ~ | //node/home/user/docs/Letter.txt ./inthisdir \\greatgrandparent ~rcinfo |
| MenuetOS CMD | / | / |   |   |   | /file |
| Stratus VOS CLI | %[system_name]#[module_name]> | > |   | < |   | %sysname#module1>SubDir>AnotherDir |
| NonStop Kernel TACL |   | . |   |   |   | \NODE.$DISK.SUBVOL.FILE \NODE.$DEVICE \NODE.$DEVICE.#SUBDEV.QUALIFIER |
| CP/M CCP | [drive letter:] | *no subdirectories, only user areas 0–F* | A:LETTER.TXT |   |   |   |
| GS/OS | :[volume name]: or.[device name]: or [prefix]: | : or / |   |   | @ | :Apps:Platinum.Paint:Platinum.Paint *:System:Finder .APPLEDISK3.5B/file |
| OpenHarmony exec, Oniro, including HarmonyOS | hb set -root [ROOT_PATH] or hb set -p --product [PRODUCT_NAME] | > or / | ./ | ../ |   | LOCAL/MEDIA_TYPE_/Download/Letter.txt |

## In programming languages

Most programming languages use the path representation of the underlying system, but some may also be system-independent.

For instance, this C code is system-*dependent* and may fail on opposing systems:

```mw
uxFile = fopen("project/readme.txt", "r") // Fails on Windows
winFile = fopen("C:\\Program Files\\bin\\config.bat", "r") // Fails on Unix
```

- In Java, the *File.separator* field stores the system-dependent separator. Some functions preclude the need for the separator entirely.

```mw
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;
// ...
File file = new File("path" + File.separator + "file.txt");
Path path = Paths.get("path", "file.txt");
```

- In Python, the `pathlib` module offers system-independent path operations.

```mw
from pathlib import Path

with (Path("path") / "to" / "file.txt").open() as open_file:
    ...
```

## In Unix

Most Unix-like systems use a similar syntax. POSIX allows treating a path beginning with two slashes in an implementation-defined manner, though in other cases systems must treat consecutive slashes as one.

Many applications on Unix-like systems (for example, scp, rcp, and rsync) use resource definitions such as `hostname:/directorypath/resource`, or URI schemes with the service name (here 'smb'), like `smb://hostname/directorypath/resource`.

### In macOS

When macOS was being developed, it inherited some pathname choices from Classic Mac OS and the Unix-like NeXTSTEP. The classic Mac OS uses a `:` while Unix and Unix-like systems use a `/` as the path delimiter. As a solution, to preserve compatibility for software and familiarity for users, and to allow disk file systems to be used both by the classic Mac OS and macOS, some portions of macOS convert between colons and slashes in pathnames; for example, the HFS+ file system, from the classic Mac OS, converts colons in file names to slashes and, when reading a directory, converts slashes in filenames to colons, and the Carbon toolkit converts colons in pathnames to slashes and slashes in path names to colons, and converts them back when providing filenames and pathnames to the caller.

## In DOS and Windows

DOS and Windows have no single root directory; a root exists for each storage drive, indicated with a drive letter or through UNC.

Directory and file name comparisons are case-insensitive: "test.TXT" would match "Test.txt".

Windows understands the following kinds of paths:

- Local paths, such as `C:\File`.
- Universal naming convention (UNC).
- DOS device paths, such as `\\.\C:\File` or `\\?\UNC\Server\Volume\File`. The first, `\\?\` skips path normalization. The second, `\\.\` uses the raw device namespace.

In the Windows API, file I/O functions automatically convert `/` into `\` (except when using the `\\?\` prefix). Paths using standard Windows APIs (dating back to DOS and Win9x), were limited to 260 characters, or less, as defined by the environment variable *MAX_PATH*. For backwards compatibility with legacy applications this limitation was not removed until Windows 10, build 1607, when it could be expanded to 32,767. Windows NT always supported the 32,767 path length internally but only if using Unicode APIs or forcing UNC paths by the `\\?\` prefix.

PowerShell allows slash-interoperability for backwards-compatibility:

```mw
PS C:\>Get-Content -Path "C:/path/to/file.txt"

Here is some text within a file
```

### Yen/won character error

Japanese and Korean versions of Windows often displayed the '¥' character or the '₩' character instead of the directory separator. This is because, while in ANSI codepages the character at 0x5C was the backslash, in Japanese and Korean codepages 0x5C was the yen and won signs, respectively. Therefore, when the character for a backslash was used, other glyphs appeared.

### Universal Naming Convention

The Microsoft **Universal Naming Convention** (**UNC**, **uniform naming convention**, or **network path**), is a syntax to describe the location of a network resource, such as a shared file, directory, or printer. A UNC path has the general form:

\\ComputerName\SharedFolder\Resource

Some Windows interfaces allow or require UNC syntax for WebDAV share access, rather than a URL. The UNC syntax is extended with optional components to denote use of SSL and TCP/IP port number. Thus, the WebDAV URL of `https://hostname:443/SharedFolder/Resource` becomes `\\hostname@SSL@443\SharedFolder\Resource`.

When viewed remotely, the "SharedFolder" may have a name different from what a program on the server sees when opening "\SharedFolder". Instead, the SharedFolder name consists of an arbitrary name assigned during creation of the share.

Since UNCs start with two backslashes, and the backslash is also used for escape sequences and in regular expressions, cases of leaning toothpick syndrome may arise. An escaped string for a regular expression matching a UNC begins with 8 backslashes `\\\\\\\\` because the string and regular expression both require escaping. This can be simplified by using raw strings, such as `@"\\\\"` in C#, `r'\\\\'` in Python, or `qr{\\\\}` in Perl.

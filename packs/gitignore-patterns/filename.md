---
title: "Filename"
source: https://en.wikipedia.org/wiki/Filename
domain: gitignore-patterns
license: CC-BY-SA-4.0
tags: gitignore patterns, git ignore rules, glob ignore patterns, version control exclusion
fetched: 2026-07-02
---

# Filename

A **filename** is used to uniquely identify a computer file in a file system. Different file systems impose different restrictions on filename lengths.

A filename may (depending on the file system) include:

- **name** – base name of the file
- **extension** – may indicate the format of the file (e.g. `.txt` for plain text, `.pdf` for Portable Document Format, `.dat` for unspecified binary data, etc.)

The components required to identify a file by utilities and applications varies across operating systems, as does the syntax and format for a valid filename.

The characters allowed in filenames depend on the file system. The letters A–Z and digits 0–9 are allowed by most file systems; many file systems support additional characters, such as the letters a–z, special characters, and other printable characters such as accented letters, symbols in non-Roman alphabets, and symbols in non-alphabetic scripts. Some file systems allow even unprintable characters, including Bell, Null, Return and Linefeed, to be part of a filename, although most utilities do not handle them well.

Filenames may include things like a revision or generation number of the file, a numerical sequence number (widely used by digital cameras through the *DCF* standard), a date and time (widely used by smartphone camera software and for screenshots), or a comment such as the name of a subject or a location or any other text to help identify the file.

Some people use the term filename when referring to a complete specification of device, subdirectories and filename such as the Windows *C:\Program Files\Microsoft Games\Chess\Chess.exe*. The filename in this case is *Chess.exe*. Some utilities have settings to suppress the extension as with MS Windows Explorer.

## History

During the 1970s, some mainframe and minicomputers had operating systems where files on the system were identified by a user name, or account number.

For example, on the TOPS-10 and RSTS/E operating systems from Digital Equipment Corporation, files were identified by

- optional device name (one or two characters) followed by an optional unit number, and a colon ":". If not present, it was presumed to be SY:
- the account number, consisting of a bracket "[", a pair of numbers separated by a comma, and followed by a close bracket "]". If omitted, it was presumed to be yours.
- mandatory file name, consisting of 1 to 6 characters (upper-case letters or digits)
- optional 3-character extension.

On the OS/360 and successor operating systems from IBM, a file name can be up to 44 characters, consisting of upper case letters, digits, and the period; a file name had to start with a letter or number, a period must occur at least once each 8 characters, two consecutive periods can not appear in the name, and the name must end with a letter or digit. By convention, when using TSO, the letters and numbers before the first period is the account number of the owner or the project it belongs to, but there is no requirement to use this convention.

On the McGill University MUSIC/SP system, file names consisted of

- Optional account number, which was one to four characters followed by a colon.If the account number was missing, it was presumed to be in your account, but if it was not, it was presumed to be in the *COM: pseudo-account, which is where all files marked as public were catalogued.
- 1–17 character file name, which could be upper case letters or digits, and the period, with the requirement it not begin or end with a period, or have two consecutive periods.

The Univac VS/9 operating system had file names consisting of

- Account name, consisting of a dollar sign "$", a 1-7 character (letter or digit) username, and a period ("."). If not present it was presumed to be in your account, but if it was not, the operating system would look in the system manager's account $TSOS. If you typed in a dollar sign only as the account, this would indicate the file was in the $TSOS account *unless* the first 1–7 character of the file name before the first period matched an actual account name, then that account was used, e.g. ABLE.BAKER is a file in your account, but if not there the system would search for $TSOS.ABLE.BAKER, but if $ABLE.BAKER was specified, the file $TSOS.ABLE.BAKER would be used *unless* $ABLE was a valid account, then it would look for a file named BAKER in that account.
- File name, 1–56 characters (letters and digits) separated by periods. File names cannot start or end with a period, nor can two consecutive periods appear.

In 1985, RFC 959 officially defined a *pathname* to be the character string that must be entered into a file system by a user in order to identify a file.

On early personal computers using the CP/M operating system, filenames were always 11 characters. This was referred to as the 8.3 filename with a maximum of an 8 byte name and a maximum of a 3 byte extension. Utilities and applications allowed users to specify filenames without trailing spaces and include a dot before the extension. The dot was not actually stored in the directory. Using only 7 bit characters allowed several file attributes to be included in the actual filename by using the high-order-bit; these attributes included Readonly, Archive, and System. Eventually this was too restrictive and the number of characters allowed increased. The attribute bits were moved to a special block of the file including additional information.

The original File Allocation Table (FAT) file system, used by Standalone Disk BASIC-80, had a 6.3 file name, with a maximum of 6 bytes in the name and a maximum of 3 bytes in the extension. The FAT12 and FAT16 file systems in IBM PC DOS/MS-DOS and Microsoft Windows prior to Windows 95 used the same 8.3 convention as the CP/M file system. The FAT file systems supported 8-bit characters, allowing them to support non-ASCII characters in file names, and stored the attributes separately from the file name.

Around 1995, VFAT, an extension to the MS-DOS FAT filesystem, was introduced in Windows 95 and Windows NT. It allowed mixed-case long filenames (LFNs), using Unicode characters, in addition to classic "8.3" names.

## File naming schemes

Programs and devices may automatically assign names to files such as a numerical counter (for example `IMG_0001.JPG`) or a time stamp with the current date and time.

The benefit of a time stamped file name is that it facilitates searching files by date, given that file managers usually feature file searching by name. In addition, files from different devices can be merged in one directory without file naming conflicts.

Numbered file names, on the other hand, do not require that the device has a correctly set internal clock. For example, some digital camera users might not bother setting the clock of their camera. Internet-connected devices such as smartphones may synchronize their clock from a NTP server.

Perhaps the most common file naming convention is to limit directory names and file names to the 65 characters in the POSIX portable filename character set. One common approach is to store the full "title" of a document inside the file itself as arbitrary UTF-8 characters, and then automatically generating a "slug" from that title to use as the filename.

## References: absolute vs relative

An absolute reference includes all directory levels. In some systems, a filename reference that does not include the complete directory path defaults to the current working directory. This is a relative reference. One advantage of using a relative reference in program configuration files or scripts is that different instances of the script or program can use different files.

This makes an absolute or relative path composed of a sequence of filenames.

## Number of names per file

Unix-like file systems allow a file to have more than one name; in traditional Unix-style file systems, the names are hard links to the file's inode or equivalent. Windows supports hard links on NTFS file systems, and provides the command `fsutil` in Windows XP, and `mklink` in later versions, for creating them. Hard links are different from Windows shortcuts, classic Mac OS/macOS aliases, or symbolic links. The introduction of LFNs with VFAT allowed filename aliases. For example, `longfi~1.???` with a maximum of eight plus three characters was a filename alias of "`long file name.???`" as a way to conform to 8.3 limitations for older programs.

This property was used by the move command algorithm that first creates a second filename and then only removes the first filename.

Other filesystems, by design, provide only one filename per file, which guarantees that alteration of one filename's file does not alter the other filename's file.

## Length restrictions

Some filesystems restrict the length of filenames. In some cases, these lengths apply to the entire file name, as in 44 characters in IBM z/OS. In other cases, the length limits may apply to particular portions of the filename, such as the name of a file in a directory, or a directory name. For example, 9 (e.g., 8-bit FAT in Standalone Disk BASIC), 11 (e.g. FAT12, FAT16, FAT32 in DOS), 14 (e.g. early Unix), 21 (Human68K), 31, 30 (e.g. Apple DOS 3.2 and 3.3), 15 (e.g. Apple ProDOS), 44 (e.g. IBM S/370), or 255 (e.g. early Berkeley Unix) characters or bytes. Length limits often result from assigning fixed space in a filesystem to storing components of names, so increasing limits often requires an incompatible change, as well as reserving more space.

A particular issue with filesystems that store information in nested directories is that it may be possible to create a file with a complete pathname that exceeds implementation limits, since length checking may apply only to individual parts of the name rather than the entire name. Many Windows applications are limited to a `MAX_PATH` value of 260, but Windows file names can easily exceed this limit. From Windows 10, version 1607, MAX_PATH limitations have been removed.

## Filename extensions

Filenames in some file systems, such as FAT and the ODS-1 and ODS-2 levels of Files-11, are composed of two parts: a *base name* or *stem* and an *extension* or *suffix* used by some applications to indicate the file type. Some other file systems, such as Unix file systems, VFAT, and NTFS, treat a filename as a single string; a convention often used on those file systems is to treat the characters following the last period in the filename, in a filename containing periods, as the extension part of the filename.

Multiple output files created by an application may use the same basename and various extensions. For example, a Fortran compiler might use the extension `FOR` for source input file, `OBJ` for the object output and `LST` for the listing. Although there are some common extensions, they are arbitrary and a different application might use `REL` and `RPT`. Extensions have been restricted, at least historically on some systems, to a length of 3 characters, but in general can have any length, e.g., `html`.

## Encoding interoperability

There is no general encoding standard for filenames.

File names have to be exchanged between software environments for network file transfer, file system storage, backup and file synchronization software, configuration management, data compression and archiving, etc. It is thus very important not to lose file name information between applications. This led to wide adoption of Unicode as a standard for encoding file names, although legacy software might not be Unicode-aware.

### Encoding indication interoperability

Traditionally, filenames allowed any character in their filenames as long as they were file system safe. Although this permitted the use of any encoding, and thus allowed the representation of any local text on any local system, it caused many interoperability issues.

A filename could be stored using different byte strings in distinct systems within a single country, such as if one used Japanese Shift JIS encoding and another Japanese EUC encoding. Conversion was not possible as most systems did not expose a description of the encoding used for a filename as part of the extended file information. This forced costly filename encoding guessing with each file access.

A solution was to adopt Unicode as the encoding for filenames.

In the classic Mac OS, however, encoding of the filename was stored with the filename attributes.

### Unicode interoperability

The Unicode standard solves the encoding determination issue.

Nonetheless, some limited interoperability issues remain, such as normalization (equivalence), or the Unicode version in use. For instance, UDF is limited to Unicode 2.0; macOS's HFS+ file system applies NFD Unicode normalization and is optionally case-sensitive (case-insensitive by default.) Filename maximum length is not standard and might depend on the code unit size. Although it is a serious issue, in most cases this is a limited one.

On Linux, this means the filename is not enough to open a file: additionally, the exact byte representation of the filename on the storage device is needed. This can be solved at the application level, with some tricky normalization calls.

The issue of Unicode equivalence is known as "normalized-name collision". A solution is the *Non-normalizing Unicode Composition Awareness* used in the Subversion and Apache technical communities. This solution does not normalize paths in the repository. Paths are only normalized for the purpose of comparisons. Nonetheless, some communities have patented this strategy, forbidding its use by other communities.

### Perspectives

To limit interoperability issues, some ideas described by Sun are to:

- use one Unicode encoding (such as UTF-8)
- do transparent code conversions on filenames
- store no normalized filenames
- check for canonical equivalence among filenames, to avoid two canonically equivalent filenames in the same directory.

Those considerations create a limitation not allowing a switch to a future encoding different from UTF-8.

### Unicode migration

One issue was migration to Unicode. For this purpose, several software companies provided software for migrating filenames to the new Unicode encoding.

- Microsoft provided migration transparent for the user throughout the VFAT technology
- Apple provided "File Name Encoding Repair Utility v1.0".
- The Linux community provided "convmv".

Mac OS X 10.3 marked Apple's adoption of Unicode 3.2 character decomposition, superseding the Unicode 2.1 decomposition used previously. This change caused problems for developers writing software for Mac OS X.

## Uniqueness

Within a single directory, filenames must be unique. Since the filename syntax also applies for directories, it is not possible to create a file and directory entries with the same name in a single directory. Multiple files in different directories may have the same name.

Uniqueness approach may differ both on the case sensitivity and on the Unicode normalization form such as NFC, NFD. This means two separate files might be created with the same text filename and a different byte implementation of the filename, such as L"\x00C0.txt" (UTF-16, NFC) (Latin capital A with grave) and L"\x0041\x0300.txt" (UTF-16, NFD) (Latin capital A, grave combining).

## Letter case preservation

Some filesystems, such as FAT prior to the introduction of VFAT, store filenames as upper-case regardless of the letter case used to create them. For example, a file created with the name "MyName.Txt" or "myname.txt" would be stored with the filename "MYNAME.TXT" (VFAT preserves the letter case). Any variation of upper and lower case can be used to refer to the same file. These kinds of file systems are called **case-insensitive** and are not **case-preserving**. Some filesystems prohibit the use of lower case letters in filenames altogether.

Some file systems store filenames in the form that they were originally created; these are referred to as **case-retentive** or **case-preserving**. Such a file system can be **case-sensitive** or **case-insensitive**. If case-sensitive, then "MyName.Txt" and "myname.txt" may refer to two different files in the same directory, and each file must be referenced by the exact capitalization by which it is named. On a case-insensitive, case-preserving file system, on the other hand, only one of "MyName.Txt", "myname.txt" and "Myname.TXT" can be the name of a file in a given directory at a given time, and a file with one of these names can be referenced by any capitalization of the name.

From its original inception, the file systems on Unix and its derivative systems were case-sensitive and case-preserving. However, not all file systems on those systems are case-sensitive; by default, HFS+ and APFS in macOS are case-insensitive but case-preserving, and SMB servers usually provide case-insensitive behavior (even when the underlying file system is case-sensitive, e.g. Samba on most Unix-like systems), and SMB client file systems provide case-insensitive behavior. File system case sensitivity is a considerable challenge for software such as Samba and Wine, which must interoperate efficiently with both systems that treat uppercase and lowercase files as different and with systems that treat them the same.

## Reserved characters and words

File systems have not always provided the same character set for composing a filename. Before Unicode became a de facto standard, file systems mostly used a locale-dependent character set. By contrast, some new systems permit a filename to be composed of almost any character of the Unicode repertoire, and even some non-Unicode byte sequences. Limitations may be imposed by the file system, operating system, application, or requirements for interoperability with other systems.

Many file system utilities prohibit control characters from appearing in filenames. In Unix-like file systems, the null character and the path separator `/` are prohibited.

### Problematic characters

File system utilities and naming conventions on various systems prohibit particular characters from appearing in filenames or make them problematic: Except as otherwise stated, the symbols in the **Character** column, " and < for example, cannot be used in Windows filenames.

| Character | Name | Reason for prohibition |
|---|---|---|
| `/` | slash | Used as a path name component separator in Unix-like, Windows, and Amiga systems. (For as long as the SwitChar setting is set to /, the DOS COMMAND.COM shell would consume it as a switch character, but DOS and Windows themselves always accept it as a separator on API level.) The big solidus ⧸ (Unicode code point U+29F8) is permitted in Unix and Windows filenames. |
| `\` | backslash | Used as the default path name component separator in DOS, OS/2 and Windows (even if the SwitChar is set to '-'; allowed in Unix filenames, see Note 1). The big reverse solidus ⧹ (U+29F9) is permitted in Windows filenames. |
| `?` | question mark | Used as a wildcard in Unix, Windows and AmigaOS; marks a single character. Allowed in Unix filenames, see Note 1. The glottal stop ʔ (U+0294), the interrobang ‽ (U+203D), the inverted question mark ¿ (U+00BF), the double question mark ⁇ (U+2047), and the black question mark ornament❓(U+2753) are allowed in all filenames. |
| `%` | percent | Used as a wildcard in RT-11; marks a single character. Not special on Windows. |
| `*` | asterisk *or* star | Used as a wildcard in Unix, DOS, RT-11, VMS and Windows. Marks any sequence of characters (Unix, Windows, DOS) or any sequence of characters in either the basename or extension (thus `*.*` in DOS means "all files"). Allowed in Unix filenames, see Note 1. See Star (grapheme) for many asterisk-like characters allowed in filenames. |
| `:` | colon | Used to determine the mount point / drive on Windows; used to determine the virtual device or physical device such as a drive on AmigaOS, RT-11 and VMS; used as a pathname separator in classic Mac OS. Doubled after a name on VMS, indicates the DECnet nodename (equivalent to a NetBIOS [Windows networking] hostname preceded by `\\`.) Colon is also used in Windows to separate an alternative data stream from the main file. The letter colon ꞉ (U+A789) and the ratio symbol ∶ (U+2236) are permitted in Windows filenames. In the Segoe UI font, used in Windows Explorer, the glyphs for the colon and the letter colon are identical. |
| `\|` | vertical bar *or* pipe | Designates software pipelining in Unix, DOS and Windows; allowed in Unix filenames, see Note 1. The mathematical operator divides ∣ (U+2223) is permitted in Windows filenames. |
| `"` | straight double quote | A legacy restriction carried over from DOS. The single quotes ' (U+0027), ‘ (U+2018), and ’ (U+2019) and the curved double quotes left double quotation mark “ (U+201C) and right double quotation mark ” (U+201D) are permitted anywhere in filenames. See Note 1. |
| `<` | less than | Used to redirect input, allowed in Unix filenames, see Note 1. The spacing modifier letter left arrowhead ˂ (U+02C2) is permitted in Windows filenames. |
| `>` | greater than | Used to redirect output, allowed in Unix filenames, see Note 1. The spacing modifier letter right arrowhead ˃ (U+02C3) is permitted in Windows filenames. |
| `.` | period *or* dot | Directory names cannot end with a period in Windows, though the name can end with a period followed by a whitespace character such as a non-breaking space. Elsewhere, the period is allowed, but the last occurrence will be interpreted to be the extension separator in VMS, DOS, and Windows. In other OSes, usually considered as part of the filename, and more than one period (full stop) may be allowed. In Unix, a leading period means the file or directory is normally hidden. |
| `,` | comma | Allowed, but treated as separator by the command line interpreters COMMAND.COM and CMD.EXE on DOS and Windows. |
| `;` | semicolon | Allowed, but treated as separator by the command line interpreters Bourne shell (and compatibles) and C shell (and compatibles) on Unix-like systems, and COMMAND.COM and CMD.EXE on DOS and Windows. See Note 1. |
| `=` | equals sign | Allowed, but treated as separator by the command line interpreters COMMAND.COM and CMD.EXE on DOS and Windows. |
|   | space | Allowed, but the space is also used as a parameter separator in command line applications; see Note 1. |

Note 1: While they are allowed in Unix file and directory names, most Unix shells require specific characters such as spaces, <, >, |, \, and sometimes :, (, ), &, ;, #, as well as wildcards such as ? and *, to be quoted or escaped:

> `five\ and\ six\<seven` (example of escaping) `'five and six<seven'` or `"five and six<seven"` (examples of quoting)

The character å (U+00E5) was not allowed as the first letter in a filename under 86-DOS and MS-DOS/PC DOS 1.x-2.x, but can be used in later versions.

In Windows utilities, the space and the period are not allowed as the final character of a filename. The period is allowed as the first character, but some Windows applications, such as Windows Explorer, forbid creating or renaming such files (despite this convention being used in Unix-like systems to describe hidden files and directories). Workarounds include appending a dot when renaming the file (that is then automatically removed afterwards), using alternative file managers, creating the file using the command line, or saving a file with the desired filename from within an application.

Some file systems on a given operating system (especially file systems originally implemented on other operating systems), and particular applications on that operating system, may apply further restrictions and interpretations. See comparison of file systems for more details on restrictions.

In Unix-like systems, DOS, and Windows, the filenames "." and ".." have special meanings (current and parent directory respectively). Windows 95/98/ME also uses names like "...", "...." and so on to denote grandparent or great-grandparent directories. All Windows versions forbid creation of filenames that consist of only dots, although names consisting of three dots ("...") or more are legal in Unix.

In addition, in Windows and DOS utilities, some words are also reserved and cannot be used as filenames. For example, DOS device files:

```
CON, CONIN$, CONOUT$, PRN, AUX, CLOCK$, NUL
COM0, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9
LPT0, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9
LST (only in 86-DOS and DOS 1.xx)
KEYBD$, SCREEN$ (only in multitasking MS-DOS 4.0)
$IDLE$ (only in Concurrent DOS 386, Multiuser DOS and DR DOS 5.0 and higher)
CONFIG$ (only in MS-DOS 7.0-8.0)
```

Systems that have these restrictions cause incompatibilities with some other filesystems. For example, Windows will fail to handle, or raise error reports for, these legal UNIX filenames: aux.c, q"uote"s.txt, or NUL.txt.

NTFS filenames that are used internally include:

```
$Mft, $MftMirr, $LogFile, $Volume, $AttrDef, $Bitmap, $Boot, $BadClus, $Secure,
$Upcase, $Extend, $Quota, $ObjId and $Reparse
```

## Comparison of filename limitations

The following table describes common attributes of filenames as implemented on various notable file systems.

| System | Case sensitive | Case preserving | Allowed characters | Content restrictions | Length restrictions |
|---|---|---|---|---|---|
| 8-bit FAT | ? | ? | 7-bit ASCII (stored as 8-bit bytes) | Name cannot start with code 0 or 255 | Up to 9 characters for a sequential file name (without extension); 6, plus 3 for extension for a binary file |
| FAT12, FAT16, FAT32 | No | No | Any SBCS/DBCS OEM codepage | Forbids codes 0–31 and 255, `"`, `*`, `/`, `:`, `<`, `>`, `?`, `\`, `\|`, `+`, `,`, `.`, `;`, `=`, `[`, `]`; in some environments also: `!` `@`; DOS 1/2 forbid code 0xE5 as the first character Forbids device names including: `$IDLE$`, `AUX`, `COM1`...`COM4`, `CON`, `CONFIG$`, `CLOCK$`, `KEYBD$`, `LPT1`...`LPT4`, `LST`, `NUL`, `PRN`, `SCREEN$`; depending on `AVAILDEV` status everywhere or only in virtual `\DEV\` directory | Up to 8 characters for base name and 3 for extension |
| VFAT | No | Yes | UCS-2 | Forbids codes 0–31, `"`, `*`, `/`, `:`, `<`, `>`, `?`, `\`, `\|` | Up to 255 characters |
| exFAT | No | Yes | UTF-16 | Forbids codes 0–31, `"`, `*`, `/`, `:`, `<`, `>`, `?`, `\`, `\|` | Up to 255 characters |
| NTFS (on Windows) | Optional | Yes | UTF-16 | Forbids codes 0–31, `"`, `*`, `/`, `:`, `<`, `>`, `?`, `\`, `\|` Forbids MS-DOS device names. The Win32 API strips trailing dots, and leading and trailing spaces, except for a UNC path. | Up to 255 characters |
| NTFS (POSIX namespace) | Optional | Yes | UTF-16 | Forbids `/` and code 0 | Up to 255 characters |
| HPFS | No | Yes | Any 8-bit set | Forbids `\|`, `\`, `?`, `*`, `<`, `"`, `:`, `>`, `/` | Up to 254 characters |
| HFS | No | Yes | Any 8-bit set | Forbids `:` | Up to 255 characters; old versions of Finder limited to 31 |
| HFS+ | Optional | Yes | UTF-16 | Forbids `:` on disk and the classic Mac OS; maps between `:` in file names and `/` on disk in macOS | Up to 255 characters |
| APFS | Optional | Yes | UTF-8 | Forbids `/`, code 0 | Up to 255 characters |
| UNIX (typical) | Yes | Yes | Any 8-bit set | Forbids `/`, code 0 | Up to 255 characters |
| UNIX (V7/S3/S5 file systems) | Yes | Yes | Any 8-bit set | Forbids `/`, code 0 | Up to 14 characters |
| POSIX (fully portable filename) | Yes | Yes | `A`–`Z`, `a`–`z`, `0`–`9`, `.`, `_`, `-` | Forbids `/`, code 0; first character cannot be `-` | Up to 14 characters |
| z/OS classic MVS filesystem (datasets) | No | No | EBCDIC code pages | Forbids `$`, `#`, `@`, `-`, code C0 hex; first character must be alphabetic or national (`$`, `#`, `@`) | Up to 44 characters |
| CMS file system | No | No | EBCDIC code pages |   | Up to 8 characters for base name plus 8 for file type |
| ISO 9660 | No | ? | `A`–`Z`, `0`–`9`, `_`, `.` |   | Level 2: up to 180 (approx.); Level 3: up to 200 |
| Amiga OFS | No | Yes | Any 8-bit set | Forbids `:`, `/`, code 0 | Up to 30 characters |
| Amiga FFS | No | Yes | Any 8-bit set | Forbids `:`, `/`, code 0 | Up to 30 characters |
| Amiga PFS | No | Yes | Any 8-bit set | Forbids `:`, `/`, code 0 | Up to 107 characters |
| Amiga SFS | No | Yes | Any 8-bit set | Forbids `:`, `/`, code 0 | Up to 107 characters |
| Amiga FFS2 | No | Yes | Any 8-bit set | Forbids `:`, `/`, code 0 | Up to 107 characters |
| BFS | Yes | Yes | UTF-8 | Forbids `/` | Up to 255 characters |
| PDP-11 RT-11 | No | No | RADIX-50 |   | Up to 6 characters for base name plus up to 3 for extension |
| Files-11 ODS-1 (RSX-11/IAS) | No | No | RADIX-50 |   | Up to 6 characters for base name plus up to 3 for extension |
| Files-11 ODS-2 ((Open)VMS) | No | No | `A`–`Z`, `0`–`9`, `$`, `-`, `_` |   | Up to 32 characters per component; earlier 9 per component; latterly, 255 for a filename and 32 for an extension. |
| Files-11 ODS-5 (OpenVMS) | No | from v7.2 | `A`–`Z`, `0`–`9`, `$`, `-`, `_` |   | Up to 32 characters per component; earlier 9 per component; latterly, 255 for a filename and 32 for an extension. |
| Commodore DOS | Yes | Yes | Any 8-bit set | Forbids characters `:`, `=` and name `$` | Usually, up to 16 characters; depends on the drive |
| HP 250 | Yes | Yes | Any 8-bit set | Forbids space, `"`, `,`, `:`, codes 0 and 255 | Up to 6 characters |

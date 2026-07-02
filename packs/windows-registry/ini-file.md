---
title: "INI file"
source: https://en.wikipedia.org/wiki/INI_file
domain: windows-registry
license: CC-BY-SA-4.0
tags: windows registry, registry editor, registry hive, group policy
fetched: 2026-07-02
---

# INI file

An **INI file** is a configuration file for computer software that consists of plain text with a structure and syntax comprising key–value pairs organized in sections. The name of these configuration files comes from the filename extension *INI*, short for initialization, used in the MS-DOS operating system, which popularized this method of software configuration. The format has become an informal standard in many contexts of configuration, but many applications on other operating systems use different filename extensions, such as *conf* and *cfg*.

## History

The primary mechanism of software configuration in Windows was originally a text file format that comprised text lines with one key–value pair per line, organized into sections. This format was used for operating system components, such as device drivers, fonts, and startup launchers. INI files were also generally used by applications to store individual settings.

The format was maintained in 16-bit Microsoft Windows platforms up through Windows 3.1x. Starting with Windows 95 Microsoft favored the use of the Windows Registry and began to steer developers away from using INI files for configuration. All subsequent versions of Windows have used the Windows Registry for system configuration, but applications built on the .NET Framework use special XML *.config* files. The initialization-file functions are still available in Windows and developers may still use them.

Besides Windows software, platform-agnostic software may use this file format for configuration. Some Unix-like config files also use a similar format. INI is human-readable and simple to parse, so it is a usable format for configuration files that do not require much greater complexity.

## Prevalence

What follows is a non-exhaustive list of places in which INI files appear.

- `Desktop.ini` files are still used in Windows to configure properties of directories, e.g. specifying the icon for a folder.
- PHP's `php.ini` file employs the INI format.
- Git's `.git/config` file is written in an INI flavour.
- freedesktop.org `*.desktop` entries are written in an INI flavour.
- systemd `*.service` unit configuration files are written in INI.
- Netatalk's `afp.conf` file is written in an INI-style configuration language.
- Pacman's `pacman.conf` file is written in INI.
- Forgejo's `app.ini` configuration file is written in INI.
- EditorConfig's `.editorconfig` configuration file is written in INI.

## Example

The following example file has two sections: one for the owner of the software, and one for a payroll database connection. Comments record the last person who modified the file and the reason for modification.

```mw
; last modified 1 April 2001 by John Doe
[owner]
name = John Doe
organization = Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server = 192.0.2.62     
port = 143
file = "payroll.dat"
```

## Format

In its broader sense, INI is an informal format which lends itself well to ad-hoc implementation while remaining human-configurable. Consequently, many varying specifications (where sometimes a parser implementation is the only specification ever written) exist, called *INI dialects*.

INI interpretations depend a lot on personal taste and the needs of the computing environment, such as whitespace preservation, field type information, case sensitivity, or preferred comment delimiters. This makes INI prone to proliferation. Nonetheless, *INI-flavoured* implementations typically share common design features: a text file consisting of a key–value pair on each line, delimited by an equals sign, organized into sections denoted by square brackets.

In its most complicated interpretation, the INI format is able to express arbitrary S-expressions, making it equivalent to standardized formats like XML or JSON, albeit with a syntax which is not set in stone and to some may feel more comfortable.

As the INI file format is not rigidly defined, many parsers support features beyond those that form the common core. Implemented support is highly volatile. Attempts have been made to create parsers able to support as many dialects as possible.

### Key–value pairs

Data in INI is held in key–value pairs called *key* or *property*. *Key* may thus either refer to the entire key–value pair or only its key. A value is also called *property name*. In its textual representation, the key–value pair is represented by either a line or a multiline where the start of the value is indicated by a delimiter, most often an equals sign (`=`, ASCII 0x3D) but sometimes also a colon (`:`, ASCII 0x3A) or whitespace (occasionally used in the GNU world). The key's key appears to the left of the delimiter, is often non-empty and should not contain the delimiter. Some flavours allow escape sequences in the value.

In the Windows implementation, the equals sign and the semicolon are reserved characters and cannot appear in the key. Any whitespace surrounding the key is stripped by the parser. The value can contain any character (in Windows-style, no whitespace surrounds the delimiter: e.g. `IconFile=Folder.ico`).

Key–value pairs may textually look like:

```mw
key=key=v
  name =value
sem=;
semver=v5822.433.2
```

### Sections

Key–value pairs may be grouped under a *section*. Some INI dialects require every key–value pair to be in a section, some allow so-called *global properties*. When key–value pairs are grouped, the section name appears on a line by itself, enclosed in square brackets (`[`, ASCII 0x5B, and `]`, ASCII 0x5D), and applies to all key–value pairs on subsequent lines until another section is declared. There is no explicit "end of section" delimiter (such as e.g. XML's `</tag>`). Thus, sections syntactically cannot be arbitrarily nested. When required, nesting can be implemented through flattening one's hierarchy and concatenating with a custom delimiter character inside the section name (often `.`, ASCII 0x2E). One level of nesting is often supported, called *subsections*.

Example INI document employing nested sections:

```mw
[project]
name = orchard rental service (with app)
target region = "Bay Area"
; TODO: advertise vacant positions
legal team = (vacant)

[fruit "Apple"]
trademark issues = foreseeable
taste = known

[fruit.Date]
taste = novel
Trademark Issues="truly unlikely"

[fruit "Raspberry"]
anticipated problems  ="logistics (fragile fruit)"
Trademark Issues=\
 possible

[fruit.raspberry.proponents.fred]
date = 2021-11-23, 08:54 +0900
comment = "I like red fruit."
[fruit "Date/proponents/alfred"]
comment: Why,  \
 \
 \
 I would buy dates.
# folding: Is "\\\\\nn" interpreted as "\\n" or "\n"?
#   Or does "\\\\" prevent folding?
editor  =My name may contain a \\
newline.
```

#### Hierarchy (section nesting)

Some parsers allow section nesting, using dots as path delimiters:

```mw
[section]
domain = example.com

[section.subsection]
foo = bar
```

In some cases relative nesting is supported too, where a leading dot expresses nesting to the previous section:

```mw
[section]
domain = example.com

[.subsection]
foo = bar
```

Historically, ways for expressing nesting alternative to the dot have existed too (for example, IBM's driver file for Microsoft Windows `devlist.ini`, in which the backslash was used as nesting delimiter in the form of `[A\B\C]`; or Microsoft Visual Studio's `AEMANAGR.INI` file, which used a completely different syntax in the form of `[A]` and `B,C,P = V`). Some parsers did not offer nesting support at all and were hierarchy-blind, but nesting could still be partially emulated by exploiting the fact that `[A.B.C]` constitutes a unique identifier.

### Case sensitivity

Section and property names in Windows are case insensitive. Most Unix-style INI interpretations forbid case folding altogether, although case folding for the section name or key is sometimes allowed.

A line with contiguous trailing whitespace followed by a semicolon (`;`, ASCII 0x3E) indicates a comment. Some INI dialects furthermore allow use of the number sign (`#`, ASCII 0x23) to denote a comment, mirroring Unix shell comments. Some INI dialects but not all allow a comment on a key–value pair line or section line (called *in-line comment*), where some require whitespace separating the value or section closing bracket from the comment. The number sign might be nonetheless included in the key name in some dialects and ignored as such. Comment lines are designed to be ignored by a parser.

```mw
#! /bin/convert-ini-to-perl | perl | ssh wikipedia.org upload --sanitise=no
; Ambiguous without further knowledge of the INI dialect:
; is the value "live" or "live # dangerously"?
I like to = live # dangerously

#var = a

var = a       ; This is an inline comment
foo = bar     # This is another inline comment
```

Under the WinAPI's *GetPrivateProfileString*'s dialect, comments must occur on lines by themselves.

### Order of sections and properties

The order of properties in a section and the order of sections in a file is irrelevant.

### Duplicate names

Most implementations only support having one property with a given name in a section. The second occurrence of a property name may cause an abort, it may be ignored (and the value discarded), or it may override the first occurrence (with the first value discarded). Some programs use duplicate property names to implement multi-valued properties.

Interpretation of multiple section declarations with the same name also varies. In some implementations, duplicate sections simply merge their properties, as if they occurred contiguously. Others may abort or ignore some aspect of the INI file.

### Quoted values

Some implementations allow values to be quoted, typically using double quotes and/or apostrophes. This allows for explicit declaration of whitespace, and/or for quoting of special characters (equals, semicolon, etc.). The standard Windows function GetPrivateProfileString supports this, and will remove quotation marks that surround the values.

### Line continuation

Emulating C syntax, some dialects allow line folding by a backslash (`\`, ASCII 0x5C) as the last character on a line. In such *line continuation*, backslashes followed immediately by EOL (end-of-line) cause the backslash and line break to be dropped, transforming the document's lines into *logical lines*.

### Escape characters

Some dialects offer varying support for character escaping, typically with the backslash character (`\`, ASCII 0x5C) as a metacharacter and emulating C syntax.

It is not wise to blindly interpret escape sequences as some specifications explicitly mute their metacharacter for common escape sequences.

| Sequence | Meaning |
|---|---|
| `\\` | \ (a single backslash, escaping the escape character) |
| `\'` | Apostrophe |
| `\"` | Double quotes |
| `\0` | Null character |
| `\a` | Bell/Alert/Audible |
| `\b` | Backspace, Bell character for some applications |
| `\t` | Tab character |
| `\r` | Carriage return |
| `\n` | Line feed |
| `\;` | Semicolon |
| `\#` | Number sign |
| `\=` | Equals sign |
| `\:` | Colon |
| `\x*hhhh*` | Unicode character with code point 0xhhhh, encoded either in UTF-8 or local encoding |

## Accessing INI files

Under Windows, the *Profile API* is the programming interface used to read and write settings from classic Windows `.ini` files. For example, the GetPrivateProfileString function retrieves a string from the specified section in an initialization file. (The "private" profile is contrasted with `GetProfileString`, which fetches from WIN.INI.)

The following sample C program demonstrates reading property values from the above sample INI file (let the name of configuration file be `dbsettings.ini`):

```mw
#include <windows.h>

int main(int argc, TCHAR *argv[])
{
  TCHAR dbserver[1000];
  int dbport;
  GetPrivateProfileString(TEXT("database"), TEXT("server"), TEXT("127.0.0.1"), dbserver, sizeof(dbserver) / sizeof(dbserver[0]), TEXT(".\\dbsettings.ini"));
  dbport = GetPrivateProfileInt(TEXT("database"), TEXT("port"), 143, TEXT(".\\dbsettings.ini"));
  // N.B. WritePrivateProfileInt() does not exist, only WritePrivateProfileString()
  return 0;
}
```

The third parameter of the `GetPrivateProfileString` function is the default value, which are `"127.0.0.1"` and `143` respectively in the two function calls above. If the argument supplied for this parameter is `NULL`, the default is an empty string, `""`.

Under Unix, many different configuration libraries exist to access INI files. They are often already included in frameworks and toolkits. Examples of INI parsers for Unix include GLib, iniparser and libconfini.

### Comparison of INI parsers

Name

Sections support

Section nesting support

Disabled entry recognition

Multi-line support

Value types

Read/Write support

Platform

License

Programming language

Latest release version

Python ConfigParser

Yes

Yes

No

Non-standard

Boolean

,

Number

,

String

Read + Write

*BSD

,

Linux

,

macOS

,

Windows

PSFL

C

(implementation),

Python

(usage)

3.9.7

GLib

Yes

Yes

No

No

Boolean

,

Number

,

String

,

Array

Read + Write

*BSD

,

Linux

,

macOS

,

Windows

LGPL

C

2.66.7 (February 11, 2021

(

2021-02-11

)

)

[±]

inifile

Yes

No

No

No

Boolean

,

Number

,

String

Read + Write

*BSD

,

Linux

,

macOS

,

Windows

Apache

Go

1.2.0

inih

Yes

No

No

Non-standard

Boolean

,

Number

,

String

Read

*BSD

,

Linux

,

macOS

,

Windows

BSD

C

60

iniparser

Yes

No

No

Yes

Boolean

,

Number

,

String

Read + Write

*BSD

,

Linux

,

macOS

,

Windows

MIT

C

4.2.4

Java

(via

java.util.Properties

)

No

No

No

Yes

String

Read + Write

Platform-agnostic

Dual-license:

GPL

version 2 with classpath exception,

and a

proprietary

license.

C

(implementation),

Java

(usage)

26.0.1 (April 21, 2026 (2026-04-21)) [±] 25.0.3 LTS (April 21, 2026 (2026-04-21)) [±] 21.0.11 LTS (April 21, 2026 (2026-04-21)) [±] 17.0.19 LTS (April 21, 2026 (2026-04-21)) [±] 11.0.31 LTS (April 21, 2026 (2026-04-21)) [±] 8u491 LTS (April 21, 2026 (2026-04-21)) [±]

libconfini

Yes

Yes

Yes

Yes

Boolean

,

Number

,

String

,

Array

Read

*BSD

,

Linux

,

macOS

,

Windows

GPL

C

1.16.2

PHP

(via

parse_ini_file()

)

Yes

Yes

Yes

No

Boolean

,

Number

,

String

,

Null

Read

Linux

,

macOS

,

Windows

PHP License

v3.01

C

(implementation),

PHP

(usage)

8.5.7

(4 June 2026

(

4 June 2026

)

)

PyINI

Yes

Yes (up to two sections)

Yes

Yes

Boolean

,

Number

,

String

,

Array

Read + Write

Platform-agnostic

GPLv3

Python

2.1

python-ini

Yes

No

No

Yes

Boolean

,

Number

,

String

,

Null

Read + Write

Platform-agnostic

BSD

Python

1.1.0

RudeConfig

Yes

No

No

No

Boolean

,

Number

,

String

Read + Write

Linux

,

Windows

GPL

C++

Discontinued – last version is 5.0.5, from November 2009

Windows API

Yes

No

No

No

Number

,

String

,

Struct

Read + Write (non-destructive)

Windows

Proprietary

C

26H1 (10.0.28000.2340) (June 23, 2026

(

2026-06-23

)

)

[±]

25H2 (10.0.26200.8737) (June 23, 2026 (2026-06-23)) [±]

Wine

(implementation of

Windows API

)

Yes

No

No

No

Number

,

String

,

Struct

Read + Write (non-destructive)

Linux

,

macOS

,

Windows

LGPL

C

11.0

13 January 2026

(

13 January 2026

)

Rust configparser

Yes

No

No

No

Boolean

,

Number

,

String

Read + Write

*BSD

,

Linux

,

macOS

,

Windows

MIT

or

LGPL

v3.0+

Rust

3.0.2

(11 September 2022)

java-ini-parser

Yes

No

Yes

Yes

Boolean

,

Number

,

String

Read + Write

Platform-agnostic

Apache

Java

1.4

(29 December 2022)

Name

Sections support

Section nesting support

Disabled entry recognition

Multi-line support

Value types

Read/Write support

Platform

License

Programming language

Latest release version

## File mapping

Initialization file mapping creates a mapping between an INI file and the Windows registry. It was introduced with Windows NT and Windows 95 as a way to migrate from storing settings in classic .ini files to the new registry. File mapping traps the Profile API calls and, using settings from the IniFileMapping Registry section, directs reads and writes to appropriate places in the Registry.

Using the example below, a string call could be made to fetch the *name* key from the *owner* section from a settings file called, say, dbsettings.ini. The returned value should be the string "John Doe":

```mw
GetPrivateProfileString("owner", "name", ... , "c:\\programs\\oldprogram\\dbsettings.ini");
```

INI mapping takes this Profile API call, ignores any path in the given filename and checks to see if there is a Registry key matching the filename under the directory:

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\

CurrentVersion\IniFileMapping

If this exists, it looks for an entry name matching the requested section. If an entry is found, INI mapping uses its value as a pointer to another part of the Registry. It then looks up the requested INI setting in that part of the Registry.

If no matching entry name is found and there is an entry under the *(Default)* entry name, INI mapping uses that instead. Thus each section name does not need its own entry.

| *(Default)* | @USR:Software\oldprogs\inisettings\all |
|---|---|
| *database* | USR:Software\oldprogs\inisettings\db |

So, in this case the profile call for the `[owner]` section is mapped through to:

| *name* | John Doe |
|---|---|
| *organization* | Acme Products |

where the "*name*" Registry entry name is found to match the requested INI key. The value of "John Doe" is then returned to the Profile call. In this case, the @ prefix on the default prevents any reads from going to the dbsettings.ini file on disk. The result is that any settings not found in the Registry are not looked for in the INI file.

The "*database*" Registry entry does not have the @ prefix on the value; thus, for the `[database]` section *only*, settings in the Registry are taken first followed by settings in the dbsettings.ini file on disk.

## Alternatives

Starting with Windows 95, Microsoft began strongly promoting the use of the Windows Registry over INI files. INI files are typically limited to two levels (sections and properties) and do not handle binary data well. This decision, however, has not been immune to critiques, due to the fact that the registry is monolithic, opaque, and binary, must be in sync with the filesystem, and represents a single point of failure for the operating system.

Later, XML-based configuration files became a popular choice for encoding configuration in text files. XML allows arbitrarily complex levels and nesting and has standard mechanisms for encoding binary data.

More recently, data serialization formats, such as JSON, TOML, and YAML, can serve as configuration formats. These three alternative formats can nest arbitrarily but have a syntax different from INI. Among them, TOML most closely resembles INI, but the idea to make TOML deliberately compatible with a large subset of INI was rejected.

The newest INI parsers, however, also allow arbitrarily deep nesting like XML, JSON, TOML, and YAML, offer equivalent support of typed values and Unicode, although they keep the informal status of INI files by allowing multiple syntaxes for expressing the same thing.

---
title: "Property list"
source: https://en.wikipedia.org/wiki/Property_list
domain: launchd
license: CC-BY-SA-4.0
tags: launchd daemon, macos init, service management, property list config
fetched: 2026-07-02
---

# Property list

In the macOS, iOS, NeXTSTEP, and GNUstep programming frameworks, **property list** files are files that store serialized objects. Property list files use the filename extension `.plist`, and thus are often referred to as **p-list** files.

Property list files are often used to store a user's settings. They are also used to store information about bundles and applications, a task served by the resource fork in the old Mac OS.

Property lists are also used for localization strings for development. These files use the `.strings` or `.stringsdict` extensions. The former is a "reduced" old-style plist containing only one dictionary without the braces (see propertyListFromStringsFileFormat), while the latter is a fully fledged plist. Xcode also uses a `.pbxproj` extension for old-style plists used as project files.

## Representations

Since the data represented by property lists is somewhat abstract, the underlying file format can be implemented in many ways. Namely, NeXTSTEP used one format to represent a property list, and the subsequent GNUstep and macOS frameworks introduced differing formats.

### NeXTSTEP

Under NeXTSTEP, property lists were designed to be human-readable and edited by hand, serialized to ASCII in a syntax somewhat like a programming language. This same format was used by OPENSTEP.

- Strings are represented in C literal style: `"This is a plist string\n"`; simpler, unquoted strings are allowed as long as they consist of alphanumericals and one of _$/:.-.
- Binary data are represented as: `< *[hexadecimal codes in ASCII]* >`. Spaces and comments between paired hex-codes are ignored.
- Arrays are represented as: `( "1", "2", "3" )`. Trailing commas are tolerated.
- Dictionaries are represented as: `{ "key" = "value"; ... }`. The left-hand side must be a string, but it can be unquoted.
- Comments are allowed as: `/* This is a comment */` and `// This is a line comment`.
- As in C, whitespace are generally insignificant to syntax. Value statements terminate by a semicolon.

One limitation of the original NeXT property list format is that it could not represent an NSValue (number, Boolean, etc.) object. As a result, these values would have to be converted to string, and "fuzzily" recovered by the application. Another limitation is that there is no official 8-bit encoding defined.

The defaults utility, introduced in OPENSTEP (1996), can be used to manipulate plist files used for storage of preferences (known as *defaults* in NeXTSTEP, hence the name) on the command line via their preferences domain, and this utility can be used to edit arbitrary plist files. This utility superseded three older commands (dread, dwrite, and dremove).

### GNUstep

GNUstep adopts the NeXTSTEP format, with additions for representing NSValue and NSDate data types. The new typed entries have the form <**T*...>, where *T* is a one-letter type code. For example, an NSValue of Boolean YES is represented as <*BY> and NSDate objects are represented as `<*DYYYY-MM-DD HH:MM:SS +ZZZZ>`. Binary data can also use the more efficient base64 format as <[ b64... ]>. The 8-bit problem is implicitly solved as well, as most deployments use UTF-8.

GNUstep also has its own binary format, NSPropertyListGNUstepBinaryFormat, implemented in NSSerialization. This format is defined recursively like the textual formats, with a single-byte type marker preceding some data. A form of string interning is supported via a GS-extension shouldBeCompact switch.

Two relative independent plist handlers are found in GNUstep: the CFPropertyList in libs-core-base (CoreFoundation), and the NSPropertyList in libs-base (Foundation Kit). Both support the binary and XML forms used by macOS to some degree, but the latter is a lot more complete. For example, the two GNUstep-specific formats are only handled in the latter.

GNUstep provides a set of plist command-line tools based on NSPropertyList, including a version of pl and defaults.

### macOS

While macOS can also read the NeXTSTEP format, Apple sets it aside in favor of two new formats of its own, one XML-based and the other binary. Apple also has a partially-compatible JSON format (NSJSONSerialization).

#### History

In Mac OS X 10.0, the NeXTSTEP format was deprecated, and a new XML format was introduced, with a public DTD defined by Apple. The XML format supports non-ASCII characters and storing NSValue objects (which, unlike GNUstep's ASCII property list format, Apple's ASCII property list format does not support).

Since XML files, however, are not the most space-efficient means of storage, Mac OS X 10.2 introduced a new format where property list files are stored as binary files. Starting with Mac OS X 10.4, this is the default format for preference files. In Mac OS X 10.7, support for reading and writing files in JSON format was introduced. JSON and property lists are not fully compatible with each other, though. For example, property lists have native date and data types, which the JSON format does not support. Conversely, JSON permits `null` values while property lists do not support explicit nulls.

#### Tooling

The old defaults tool from NeXTSTEP remains available. The /usr/libexec/PlistBuddy command provides an interactive plist editor. It can also be scripted.

The plutil utility (introduced in Mac OS X 10.2) can be used to check the syntax of property lists, or convert a property list file from one format to another. It also supports converting plists to Objective-C or Swift object literals. Like the Cocoa NSPropertyListSerialization it is built on, it takes "old-style" inputs, but does not convert to this type. (The Cocoa NSSerializer from before Mac OS X 10.2 emits old-styled output.)

The pl utility is introduced in Mac OS X v10.5. It takes any input and tries to generate "old-style" plists. Like the GNUstep version, it appears to use the description property of Foundation types found in plists, which Apple has specified to produce valid old-style plists.

In terms of the internals, Apple provides an open source parser for old style, XML, and binary formats in their C Core Foundation code as CFPropertyList. However, all the utilities and most parts of the system use the closed-source NSPropertyList parser from the Obj-C Foundation Kit. The Swift reimplementation is open source, but is not guaranteed to be identical.

#### Format

XML and JSON property lists are hand-editable in any text editor. Additionally, Apple provides support in Xcode for editing property lists in a hierarchical viewer/editor that can handle plists formatted in binary or XML, but not JSON. As of Mac OS X 10.4, Apple provides an AppleScript interface for reading property list files through the System Events application. As of Mac OS X 10.5, Apple provides an AppleScript interface for editing, creating and writing property list files as well.

For the XML format, the tags, related Foundation classes and CoreFoundation types, and data storage formats are as follows:

| Foundation class | CoreFoundation type | XML Tag | Storage format |
|---|---|---|---|
| NSString | CFString | <string> | UTF-8 encoded string |
| NSNumber | CFNumber | <real> | Floating-point value. Supports exponential notation and the special values NaN (nan) and Infinity (inf, +inf, -inf, alternatively written infinity). All of these forms are case-insensitive. |
| <integer> | Integer value in decimal (255) or hexadecimal (0xFF). The latter notation is case-insensitive. |   |   |
| NSNumber | CFBoolean | <true/>, <false/> | No data (tag only) |
| NSDate | CFDate | <date> | ISO 8601 formatted string |
| NSData | CFData | <data> | Base64 encoded data |
| NSArray | CFArray | <array> | Can contain any number of child elements. Can be empty. |
| NSDictionary | CFDictionary | <dict> | Alternating <key> tags and plist element tags. Can be empty. |

The binary file format is documented in a comment block in the Core Foundation C code source file (CF/CFBinaryPList.c) for Apple's open sourced implementation of binary plists in its Foundation library. Apple describes the implementation as opaque in its plist(5) manual page documentation, which means that reliance on the format is discouraged. In the binary file format the magic number (the first few bytes of the file which indicate that it's a valid plist file) is the text **bplist**, followed by two bytes indicating the version of the format.

The binary file can store some information that cannot be captured in the XML or JSON file formats. The array, set and dictionary binary types are made up of **pointers** - the objref and keyref entries - that index into an object table in the file. This means that binary plists can capture the fact that - for example - a separate array and dictionary serialized into a file both have the same data element stored in them. This cannot be captured in an XML file. Converting such a binary file will result in a copy of the data element being placed into the XML file. Additionally the binary file has a UID type that is used to identify data items when serialized. The complete list of data that can be stored taken from the C code source file is as follows:

| Foundation class | CoreFoundation type | Object type | Marker byte | Encoded data |
|---|---|---|---|---|
| nil | nil | null (v"1?"+) | 0000 0000 | —N/a |
| NSNumber | CFBoolean | bool | 0000 1000 (false) 0000 1001 (true) | —N/a |
| NSURL | CFURL | url (v"1?"+) | 0000 1100 (base string) 0000 1101 (string) | string: URL string in recursive encoding (as in "string object format?"); base string: the same, but with a base URL encoded first. |
| NSUUID | CFUUID | uuid (v"1?"+) | 0000 1110 | 16 bytes of UUID |
|   |   | fill | 0000 1111 | nothing - just a padding |
| NSNumber | CFNumber | int | 0001 nnnn | # of bytes is 2^nnnn, big-endian bytes (1, 2, 4, or 8) |
| NSNumber | CFNumber | real | 0010 nnnn | # of bytes is 2^nnnn, big-endian bytes (4 or 8) |
| NSDate | CFDate | date | 0011 0011 | 8 byte float follows, big-endian bytes; seconds from 1/1/2001 (Core Data epoch) |
| NSData | CFData | data | 0100 nnnn [int] | nnnn is number of bytes unless 1111 then int count follows, followed by bytes |
| NSString | CFString | string | 0101 nnnn [int] | ASCII string, nnnn is # of chars, else 1111 then int count, then bytes |
| NSString | CFString | string | 0110 nnnn [int] | Unicode string, nnnn is # of chars, else 1111 then int count, then big-endian 2-byte uint16_t |
| NSString | CFString | string (v"1?"+) | 0111 nnnn [int] | UTF-8 string, nnnn is # of chars, else 1111 then int count, then bytes |
|   |   | UID | 1000 nnnn | nnnn+1 is # of big-endian bytes (1, 2, 4, or 8). Unsigned int, only produced by NSKeyedArchiver (see below). |
| NSArray | CFArray | array | 1010 nnnn [int] | objref* nnnn is count, unless '1111', then int count follows |
| NSOrderedSet |   | ordset (v"1?"+) | 1011 nnnn [int] | objref* nnnn is count, unless '1111', then int count follows |
| NSSet | CFSet | set (v"1?"+) | 1100 nnnn [int] | objref* nnnn is count, unless '1111', then int count follows |
| NSDictionary | CFDictionary | dict | 1101 nnnn [int] | keyref* objref* nnnn is count, unless '1111', then int count follo |

Note the v"1?"+ note in many types. This means that the marker byte is only found in files with a format version no lower than the "1?" magic number. The precise way to parse them is more nebulous than the way to parse legacy types, since the CFBinaryPlist implementation only handles version "0?". In practice, these types are never encountered, since NSKeyedArchiver is already capable of capturing these information.

A table of offsets follow the object table, which is then followed by a trailer containing information on the size and location of the two tables.

## Serializing to plist

Since property lists do not capture all the information and data types required to describe an arbitrary object, an extra layer of encoding and decoding is often done. The OpenStep specification abstracts the operation of serializing any NSObject under the NSCoding protocol. Any class implementing this protocol can have its instances serialized by a NSCoder subclass to some other format. Two main coders exist for the purpose of serializing objects to plists:

- NSArchiver, which converts an object into a block of binary data somewhat like a tagged struct. This class is part of OpenStep, although no concrete format has been defined. In practice, one can use it to serialize an object to a file (skipping the plist), or to embed the data in a plist. It must be read and written in the same order as written. The introduction of NSKeyedArchiver deprecates its use.
- NSKeyedArchiver, introduced in Mac OS X 10.2, transforms the object into an NSDictionary. The main improvement of this format for programmers is that it accesses members not by a fixed order, but by string keys. Internally, it somewhat recapitulates the binary plist format by storing an object table array called $objects in the dictionary. Everything else, including class information, is referenced by a UID pointer. A $top entry under the dict points to the top-level object the programmer was meaning to encode.

Among other things, using an archiver allows for new datatypes to be encoded without changing the plist format itself and it is the preferred way for Apple to encode things like NSSets and null values. Parsing the formats do prove a bit harder, since one more layer must be followed even for some classes plists were supposed to support. Like the binary format which also has an object table, it is possible to create circular references in NSKeyedArchiver. Since there is not a UID data type in XML, the integers are stored in a dictionary under the key "CF$UID".

Apple publishes an open-source NSKeyedArchiver in Swift Corelibs Foundation; like the closed-source Apple Foundation, it restricts output formats to binary and XML only. It also has some test cases showing the results of serialization. GNUstep also has a compatible implementation, which does not limit output formats.

## Path language

There is not a single, standardized path language for property lists like XPath does for XML, but informal conventions used by various programs exist.

- A dot syntax version is found in the *keypath* argument of Apple's plutil. It appears to derive from `(id) -[NSObject(NSKeyValueCoding) valueForKeyPath:]`.
- A different format is used by PlistBuddy, with a colon syntax for indexing.

Neither format is able to express a key with the separator character in it.

## Other platforms

### Windows

Although best known on Apple or Darwin systems, including iOS and macOS, plist files are also present on Windows computers when Apple software, such as iTunes or Safari are installed. On Windows, the files are typically binary files, although some applications may generate PLIST files in the other formats.

On Windows the Apple plist files are stored in the user's home directory under %USERPROFILE%\AppData\Roaming\Apple Computer. These plist files on Windows typically store preferences and other information, rather than using the Windows registry.

Options for editing PLIST files on Windows are not as extensive as on macOS. If the file is in the XML or JSON format with care a text editor such as Notepad++ can be used. Apple ships a plutil.exe within its "Apple Application Support" package (which is part of iTunes), and it is identical to its macOS counterpart.

### NetBSD

Introduced in 2006 and first released with NetBSD#4.0 (2007) is a proplib library, which can be used for serialising data between the kernel and userland. It implements part of the XML plist language.

One of the sample users of proplib is the second revision of the sysmon envsys framework for system monitoring.

NetBSD's proplib library has also been ported to DragonFly in 2010, and is available since DragonFly BSD#2.8.

### Cross-platform

- Facebook's open-source reimplementation of the Xcode build tool, xcbuild, contains a plist library as well as plutil and PlistBuddy. These cross-platform utilities are written in C++.
- Python has a builtin `plistlib` module to read and write plist files, in Apple's XML or in binary (since Python 3.4). ProperTree is a cross-platform editor that makes use of this library.
  - A third-party library called ccl-bplist has the additional ability to handle NSKeyedArchiver UIDs.
- Go has a `plist` package that supports four types of plists: OpenStep text, GNUStep text, Apple XML, and Apple Binary. It also handles UIDs in XML and binary formats.
- Dart has a third-party library called propertylistserialization which also handles NSKeyedArchiver UIDs.

---
title: "Terminfo"
source: https://en.wikipedia.org/wiki/Terminfo
domain: terminfo-termcap
license: CC-BY-SA-4.0
tags: terminfo database, termcap capabilities, terminal capability database, terminal control codes
fetched: 2026-07-02
---

# Terminfo

**Terminfo** is a library and database that enables programs to use display terminals in a device-independent manner. Mary Ann Horton implemented the first terminfo library in 1981–1982 as an improvement over termcap. The improvements include

- faster access to stored terminal descriptions,
- longer, more understandable names for terminal capabilities and
- general expression evaluation for strings sent to the terminal.

Terminfo was included with UNIX System V Release 2 and soon became the preferred form of terminal descriptions in System V, rather than termcap (which BSD continued to use). This was imitated in pcurses in 1982–1984 by Pavel Curtis, and was available on other UNIX implementations, adapting or incorporating fixes from Mary Horton. For more information, refer to the posting on the `comp.sources.unix` newsgroup from December 1986.

A terminfo database can describe the capabilities of hundreds of different display terminals. This allows external programs to be able to have character-based display output, independent of the type of terminal.

Some configurations are:

- Number of lines on the screen
- Mono mode; suppress color
- Use visible bell instead of beep

## Data model

Terminfo databases consist of one or more descriptions of terminals.

### Indices

Each description must contain the canonical name of the terminal. It may also contain one or more aliases for the name of the terminal. The canonical name or aliases are the keys by which the library searches the terminfo database.

### Data values

The description contains one or more capabilities, which have conventional names. The capabilities are typed: *boolean*, *numeric* and *string*. The terminfo library has predetermined types for each capability name. It checks the types of each capability by the syntax:

- *string* capabilities have an "=" between the capability name and its value,
- *numeric* capabilities have a "#" between the capability name and its value, and
- *boolean* capabilities have no associated value (they are always *true* if specified).

Applications which use terminfo know the types for the respective capabilities, and obtain the values of capabilities from the terminfo database using library calls that return successfully only when the capability name corresponds to one of the predefined typed capabilities.

Like termcap, some of the *string* capabilities represent escape sequences which may be sent to the host by pressing special keys on the keyboard. Other capabilities represent strings that may be sent by an application to the terminal. In the latter case, the terminfo library functions (as does a termcap library) for substituting application parameters into the string which is sent. These functions provide a stack-based expression parser, which is primarily used to help minimize the number of characters sent for control sequences which have optional parameters such as SGR (Select Graphic Rendition). In contrast, termcap libraries provide a limited set of operations which are useful for most terminals.

### Hierarchy

Terminfo descriptions can be constructed by including the contents of one description in another, suppressing capabilities from the included description or overriding or adding capabilities. No matter what storage model is used, the terminfo library returns the terminal description from the requested description, using data which is compiled using a standalone tool (e.g., **tic**).

## Storage model

Terminfo data is stored as a binary file, making it less simple to modify than termcap. The data can be retrieved by the terminfo library from the files where it is stored. The data itself is organized as tables for the Boolean, numeric and string capabilities, respectively. This is the scheme devised by Mary Horton, and except for some differences regarding the available names is used in most terminfo implementations. X/Open does not specify the format of the compiled terminal description. In fact, it does not even mention the common **tic** or **infocmp** utilities. Because the compiled terminfo entries do not contain metadata identifying the indices within the tables to which each capability is assigned, they are not necessarily compatible between implementations. However, since most implementations use the same overall table structure (including sizes of header and data items), it is possible to automatically construct customized terminfo libraries which can read data for a given implementation. For example, ncurses can be built to match the terminfo data for several other implementations.

### Directory tree

The original (and most common) implementation of the terminfo library retrieves data from a directory hierarchy. By using the first character of the name of the terminal description as one component of the pathname, and the name of the terminal description as the name of the file to retrieve, the terminfo library usually outperforms searching a large termcap file.

### Hashed database

Some implementations of terminfo store the terminal description in a hashed database (e.g., something like Berkeley DB version 1.85). These store two types of records: aliases which point to the canonical entry, and the canonical entry itself, which contains the data for the terminal capabilities.

## Limitations and extensions

The Open Group documents the limits for terminfo (minimum guaranteed values), which apply only to the source file. Two of these are of special interest:

- 14 character maximum for terminal aliases
- 32,767 maximum for numeric quantities

The 14-character limit addresses very old filesystems which could represent filenames no longer than that. While those filesystems are generally obsolete, these limits were as documented from the late 1980s, and unreviewed since then.

The 32,767 limit is for positive values in a signed two's complement 16-bit value. A terminfo entry may use negative numbers to represent cancelled or absent values.

Unlike termcap, terminfo has both a source and compiled representation. The limits for the compiled representation are unspecified. However, most implementations note in their documentation for **tic** (terminal information compiler) that compiled entries cannot exceed 4,096 bytes in size.

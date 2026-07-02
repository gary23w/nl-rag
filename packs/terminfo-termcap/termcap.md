---
title: "Termcap"
source: https://en.wikipedia.org/wiki/Termcap
domain: terminfo-termcap
license: CC-BY-SA-4.0
tags: terminfo database, termcap capabilities, terminal capability database, terminal control codes
fetched: 2026-07-02
---

# Termcap

**Termcap** (*terminal capability*) is a legacy software library and database used on Unix-like computers that enables programs to use display computer terminals in a terminal-independent manner, which greatly simplifies the process of writing portable text mode applications. It was superseded by the terminfo database used by ncurses, tput, and other programs.

A termcap database can describe the capabilities of hundreds of different display terminals. This allows programs to have character-based display output, independent of the type of terminal. On-screen text editors such as vi and Emacs are examples of programs that may use termcap. Other programs are listed in the Termcap category. Access to the termcap database was usually provided by separate libraries, e.g. GNU Termcap.

Examples of what the database describes:

- how many columns wide the display is
- what string to send to move the cursor to an arbitrary position (including how to encode the row and column numbers)
- how to scroll the screen up one or several lines
- how much padding is needed for such a scrolling operation.

## History

Bill Joy wrote the first termcap library in 1978 for the Berkeley Unix operating system; it has since been ported to most Unix and Unix-like environments, even OS-9. Joy's design was reportedly influenced by the design of the terminal data store in the earlier Incompatible Timesharing System.

## Data model

Termcap databases consist of one or more descriptions of terminals.

### Indices

Each description must contain the canonical name of the terminal. It may also contain one or more aliases for the name of the terminal. The canonical name or aliases are the keys by which the library searches the termcap database.

### Data values

The description contains one or more capabilities, which have conventional names. The capabilities are typed: *boolean*, *numeric* and *string*. The termcap library has no predetermined type for each capability name. It determines the types of each capability by the syntax:

- *string* capabilities have an "=" between the capability name and its value,
- *numeric* capabilities have a "#" between the capability name and its value, and
- *boolean* capabilities have no associated value (they are always *true* if specified).

Applications which use termcap do expect specific types for the commonly used capabilities, and obtain the values of capabilities from the termcap database using library calls that return successfully only when the database contents matches the assumed type.

### Hierarchy

Termcap descriptions can be constructed by including the contents of one description in another, suppressing capabilities from the included description or overriding or adding capabilities. No matter what storage model is used, the termcap library constructs the terminal description from the requested description, including, suppressing or overriding at the time of the request.

## Storage model

Termcap data is stored as text, making it simple to modify. The text can be retrieved by the termcap library from files or environment variables.

### Environment variables

The **TERM** environment variable contains the terminal type name.

The **TERMCAP** environment variable may contain a termcap database. It is most often used to store a single termcap description, set by a terminal emulator to provide the terminal's characteristics to the shell and dependent programs.

The **TERMPATH** environment variable is supported by newer termcap implementations and defines a search path for termcap files.

### Flat file

The original (and most common) implementation of the termcap library retrieves data from a flat text file. Searching a large termcap file, e.g., 500 kB, can be slow. To aid performance, a utility such as **reorder** is used to put the most frequently used entries near the beginning of the file.

### Hashed database

4.4BSD based implementations of termcap store the terminal description in a hashed database (e.g., something like Berkeley DB version 1.85). These store two types of records: aliases which point to the canonical entry, and the canonical entry itself. The text of the termcap entry is stored literally.

## Limitations and extensions

The original termcap implementation was designed to use little memory:

- the first name is two characters, to fit in 16 bits
- capability names are two characters
- descriptions are limited to 1023 characters.
- only one termcap entry with its definitions can be included, and must be at the end.

Newer implementations of the termcap interface generally do not require the two-character name at the beginning of the entry.

Capability names are still two characters in all implementations.

The **tgetent** function used to read the terminal description uses a buffer whose size must be large enough for the data, and is assumed to be 1024 characters. Newer implementations of the termcap interface may relax this constraint by allowing a null pointer in place of the fixed buffer, or by hiding the data which would not fit, e.g., via the **ZZ** capability in NetBSD termcap. The terminfo library interface also emulates the termcap interface, and does not actually use the fixed-size buffer.

The terminfo library's emulation of termcap allows multiple other entries to be included without restricting the position. A few other newer implementations of the termcap library may also provide this ability, though it is not well documented.

## Obsolete features

A special capability, the "hz" capability, was defined specifically to support the Hazeltine 1500 terminal, which had the unfortunate characteristic of using the ASCII tilde character ('~') as a control sequence introducer. In order to support that terminal, not only did code that used the database have to know about using the tilde to introduce certain control sequences, but it also had to know to substitute another printable character for any tildes in the displayed text, since a tilde in the text would be interpreted by the terminal as the start of a control sequence, resulting in missing text and screen garbling. Additionally, attribute markers (such as start and end of underlining) themselves took up space on the screen. Comments in the database source code often referred to this as "Hazeltine braindamage". Since the Hazeltine 1500 was a widely used terminal in the late 1970s, it was important for applications to be able to deal with its limitations.

---
title: "glob (programming)"
source: https://en.wikipedia.org/wiki/Glob_(programming)
domain: gitignore-patterns
license: CC-BY-SA-4.0
tags: gitignore patterns, git ignore rules, glob ignore patterns, version control exclusion
fetched: 2026-07-02
---

# glob (programming)

**glob()** (/ɡlɒb/) is a POSIX C function for ***globbing***, which is the archetypal use of pattern matching against the names in a filesystem directory such that a name pattern is expanded into a list of names matching that pattern. Although *globbing* may now refer to `glob()`-style pattern matching of any string, not just expansion into a list of filesystem names, the original meaning of the term is still widespread.

The `glob()` function and the underlying `gmatch()` function originated at Bell Labs in the early 1970s alongside the original AT&T UNIX itself and had a formative influence on the syntax of UNIX command line utilities and therefore also on the present-day reimplementations thereof.

In their original form, `glob()` and `gmatch()` derived from code used in Bell Labs in-house utilities that developed alongside the original Unix in the early 1970s. Among those utilities were also two command line tools called `glob` and `find`; each could be used to pass a list of matching filenames to other command line tools, and they shared the backend code subsequently formalized as `glob()` and `gmatch()`. Shell-statement-level globbing by default became commonplace following the "builtin"-integration of globbing-functionality into the 7th edition of the Unix shell in 1978. The Unix shell's -f option to disable globbing — i.e. revert to literal "file" mode — appeared in the same version.

The glob *pattern quantifiers* now standardized by POSIX.2 (IEEE Std 1003.2) fall into two groups, and can be applied to any character sequence ("string"), not just to directory entries.

- "Metacharacters" (also called "Wildcards"):
  - `?` (not in brackets) matches any character exactly once.
  - `*` (not in brackets) matches a string of zero or more characters.
- "Ranges/sets":
  - `[...]`, where the first character within the brackets is not '!', matches any single character among the characters specified in the brackets. If the first character within brackets is '!', then the `[!...]` matches any single character that is *not* among the characters specified in the brackets.

The characters in the brackets may be a list (

[abc]

) or a range (

[a-c]

) or denote a character class (like

[[:space:]]

where the inner brackets are part of the classname). POSIX does not mandate multi-range (

[a-c0-3]

) support, which derive originally from

regular expressions

.

As reimplementations of Bell Labs' UNIX proliferated, so did reimplementations of its Bell Labs' libc and shell, and with them `glob()` and *globbing*. Today, `glob()` and *globbing* are standardized by the POSIX.2 specification and are integral part of every Unix-like libc ecosystem and shell, including AT&T Bourne shell-compatible Korn shell (ksh), Z shell (zsh), Almquist shell (ash) and its derivatives and reimplementations such as busybox, toybox, GNU bash, Debian dash.

## Origin

The glob command, short for *global*, originates in the earliest versions of Bell Labs' Unix. The command interpreters of the early versions of Unix (1st through 6th Editions, 1969–1975) relied on a separate program to expand wildcard characters in unquoted arguments to a command: `/etc/glob`. That program performed the expansion and supplied the expanded list of file paths to the command for execution.

Glob was originally written in the B programming language. It was the first piece of mainline Unix software to be developed in a high-level programming language. Later, this functionality was provided as a C library function, `glob()`, used by programs such as the shell. It is usually defined based on a function named `fnmatch()`, which tests for whether a string matches a given pattern - the program using this function can then iterate through a series of strings (usually filenames) to determine which ones match. Both functions are a part of POSIX: the functions defined in POSIX.1 since 2001, and the syntax defined in POSIX.2. The idea of defining a separate match function started with wildmat (wildcard match), a simple library to match strings against Bourne Shell globs.

Traditionally, globs do not match hidden files in the form of Unix dotfiles; to match them the pattern must explicitly start with `.`. For example, `*` matches all visible files while `.*` matches all hidden files.

## Syntax

The most common wildcards are `*`, `?`, and `[…]`.

| Wildcard | Description | Example | Matches | Does not match |
|---|---|---|---|---|
| `*` | matches any number of any characters including none | `Law*` | `Law`, `Laws`, or `Lawyer` | `GrokLaw`, `La`, or `aw` |
| `*Law*` | `Law`, `GrokLaw`, or `Lawyer`. | `La`, or `aw` |   |   |
| `?` | matches any single character | `?at` | `Cat`, `cat`, `Bat` or `bat` | `at` |
| `[abc]` | matches one character given in the bracket | `[CB]at` | `Cat` or `Bat` | `cat`, `bat` or `CBat` |
| `[a-z]` | matches one character from the (locale-dependent) range given in the bracket | `Letter[0-9]` | `Letter0`, `Letter1`, `Letter2` up to `Letter9` | `Letters`, `Letter` or `Letter10` |

Normally, the path separator character (`/` on Linux/Unix, MacOS, etc. or `\` on Windows) will never be matched. Some shells, such as Unix shell have functionality allowing users to circumvent this.

### Unix-like

On Unix-like systems `*`, `?` is defined as above while `[…]` has two additional meanings:

| Wildcard | Description | Example | Matches | Does not match |
|---|---|---|---|---|
| `[!abc]` | matches one character that is not given in the bracket | `[!C]at` | `Bat`, `bat`, or `cat` | `Cat` |
| `[!a-z]` | matches one character that is not from the range given in the bracket | `Letter[!3-5]` | `Letter1`, `Letter2`, `Letter6` up to `Letter9` and `Letterx` etc. | `Letter3`, `Letter4`, `Letter5` or `Letterxx` |

The ranges are also allowed to include pre-defined character classes, equivalence classes for accented characters, and collation symbols for hard-to-type characters. They are defined to match up with the brackets in POSIX regular expressions.

Unix globbing is handled by the shell per POSIX tradition. Globbing is provided on filenames at the command line and in shell scripts. The POSIX-mandated `case` statement in shells provides pattern-matching using glob patterns.

Some shells (such as the C shell and Bash) support additional syntax known as alternation or brace expansion. Because it is not part of the glob syntax, it is not provided in `case`. It is only expanded on the command line before globbing.

The Bash shell also supports the following extensions:

- Extended globbing (extglob): allows other pattern matching operators to be used to match multiple occurrences of a pattern enclosed in parentheses, essentially providing the missing kleene star and alternation for describing regular languages. It can be enabled by setting the `extglob` shell option. This option came from ksh93. The GNU fnmatch and glob has an identical extension.
- globstar: allows `**` on its own as a name component to recursively match any number of layers of non-hidden directories. Also supported by the JavaScript libraries and Python's glob.

### Windows and DOS

The original DOS was a clone of CP/M designed to work on Intel's 8088 and 8086 processors. Windows shells, following DOS, do not traditionally perform any glob expansion in arguments passed to external programs. Shells may use an expansion for their own builtin commands:

- Windows PowerShell has all the common syntax defined as stated above without any additions.
- COMMAND.COM and cmd.exe have most of the common syntax with some limitations: There is no `[…]` and for COMMAND.COM the `*` may only appear at the end of the pattern. It can not appear in the middle of a pattern, except immediately preceding the filename extension separator dot.

Windows and DOS programs receive a long command-line string instead of argv-style parameters, and it is their responsibility to perform any splitting, quoting, or glob expansion. There is technically no fixed way of describing wildcards in programs since they are free to do what they wish. Two common glob expanders include:

- The Microsoft C Runtime (msvcrt) command-line expander, which only supports `?` and `*`. Both ReactOS (`crt/misc/getargs.c`) and Wine (`msvcrt/data.c`) contain a compatible open-source implementation of `__getmainargs`, the function operating under-the-hood, in their core CRT.
- The Cygwin and MSYS `dcrt0.cc` command-line expander, which uses the unix-style `glob()` routine under-the-hood, after splitting the arguments.

Most other parts of Windows, including the Indexing Service, use the MS-DOS style of wildcards found in CMD. A relic of the 8.3 filename age, this syntax pays special attention to dots in the pattern and the text (filename). Internally this is done using three extra wildcard characters, `<>"`. On the Windows API end, the `glob()` equivalent is `FindFirstFile()`, and `fnmatch()` corresponds to its underlying `RtlIsNameInExpression()`. (Another `fnmatch()` analogue is `PathMatchSpec()`.) Both open-source msvcrt expanders use `FindFirstFile()`, so 8.3 filename quirks will also apply in them.

### SQL

The SQL `LIKE` operator has an equivalent to `?` and `*` but not `[…]`.

| Common wildcard | SQL wildcard | Description |
|---|---|---|
| `?` | `_` | matches any single character |
| `*` | `%` | matches any number of any characters including none |

Standard SQL uses a glob-like syntax for simple string matching in its `LIKE` operator, although the term "glob" is not generally used in the SQL community. The percent sign (`%`) matches zero or more characters and the underscore (`_`) matches exactly one.

Many implementations of SQL have extended the `LIKE` operator to allow a richer pattern-matching language, incorporating character ranges (`[…]`), their negation, and elements of regular expressions.

## Compared to regular expressions

Globs do not include syntax for the Kleene star which allows multiple repetitions of the preceding part of the expression; thus they are not considered regular expressions, which can describe the full set of regular languages over any given finite alphabet.

| Common wildcard | Equivalent regular expression |
|---|---|
| `?` | `.` |
| `*` | `.*` |

Globs attempt to match the entire string (for example, `S*.DOC` matches S.DOC and SA.DOC, but not POST.DOC or SURREY.DOCKS), whereas, depending on implementation details, regular expressions may match a substring.

### Implementing as regular expressions

The original Mozilla proxy auto-config implementation, which provides a glob-matching function on strings, uses a replace-as-RegExp implementation as above. The bracket syntax happens to be covered by regex in such an example.

Python's fnmatch uses a more elaborate procedure to transform the pattern into a regular expression.

## Other implementations

Beyond their uses in shells, globs patterns also find use in a variety of programming languages, mainly to process human input. A glob-style interface for returning files or an fnmatch-style interface for matching strings are found in the following programming languages:

- C and C++ do not have built-in support for glob patterns in the ISO-defined standard libraries, however on Unix-like systems C and C++ may include `<glob.h>` from the C POSIX library to use `::glob()`.
  - C++ itself does not have direct support for glob patterns, however they may be approximated using `std::filesystem::directory_iterator` and `std::regex_match()`.
  - C++ has external libraries, such as POCO C++ Libraries, which includes a `Poco::Glob` class which can act on glob patterns.
- C# provides an official extension library `Microsoft.Extensions.FileSystemGlobbing`, which contains class `Microsoft.Extensions.FileSystemGlobbing.Matcher`.
  - C# also has multiple external libraries available through NuGet such as `Glob` or `DotNet.Glob`.
- D has a `std.path.globMatch()` function.
- Go has a `filepath.Glob()` function.
- Java provides a class `java.nio.file.Files`, which has methods such as `Files.newDirectoryStream(Path dir, String glob)` for operating over glob patterns and returns `DirectoryStream<Path>`. The classes `java.nio.file.FileSystems` and `java.nio.file.PathMatcher` are also used for matching glob patterns.
- Haskell has a `Glob` package with the main module `System.FilePath.Glob`. The pattern syntax is based on a subset of Zsh's. It tries to optimize the given pattern and should be noticeably faster than a naïve character-by-character matcher.
- Node.js has a `glob` function in the `node:fs` module.
- Perl has both a `glob` function (as discussed in Larry Wall's book *Programming Perl*) and a *Glob* extension which mimics the BSD glob routine. Perl's angle brackets can be used to glob as well: `<*.log>`.
- PHP has a `glob` function.
- Python has a `glob` module in the standard library which performs wildcard pattern matching on filenames, and an `fnmatch` module with functions for matching strings or filtering lists based on these same wildcard patterns. Guido van Rossum, author of the Python programming language, wrote and contributed a `glob` routine to BSD Unix in 1986. There were previous implementations of `glob`, e.g., in the ex and ftp programs in previous releases of BSD.
- Ruby has a `glob` method for the `Dir` class which performs wildcard pattern matching on filenames. Several libraries such as Rant and Rake provide a `FileList` class which has a glob method or use the method `FileList.[]` identically.
- Rust itself does not have built-in support for globbing, but it has multiple third-party libraries that can match glob patterns, the most popular of these being the `glob` crate which itself has a `glob()` function.
- SQLite has a `GLOB` function.
- Tcl contains a globbing facility.

---
title: "grep"
source: https://en.wikipedia.org/wiki/Grep
domain: ripgrep
license: CC-BY-SA-4.0
tags: ripgrep search, string searching, recursive grep, command-line search
fetched: 2026-07-02
---

# grep

**grep** is a command-line utility for searching text for lines that match a regular expression. Its name comes from the ed command `g/*re*/p` (**g**lobal, **r**egular **e**xpression, **p**rint), which has the same effect. grep was originally developed for the Unix operating system, and is commonly available on Unix-like and some other systems such as OS-9. The shell command that runs the utility has the same name: `grep`.

## History

Before it was named, grep was a private utility written by Ken Thompson to search files for certain patterns. Doug McIlroy, unaware of its existence, asked Thompson to write such a program. Responding that he would think about such a utility overnight, Thompson actually corrected bugs and made improvements for about an hour on his own program called `s` (short for "search"). The next day he presented the program to McIlroy, who said it was exactly what he wanted. Thompson's account may explain the belief that grep was written overnight.

Thompson wrote the first version in PDP-11 assembly language to help Lee E. McMahon analyze the text of *The Federalist Papers* to determine authorship of the individual papers. The ed text editor (also authored by Thompson) had regular expression support but could not be used to search through such a large amount of text, as it loaded the entire file into memory to enable random access editing, so Thompson excerpted that regexp code into a standalone tool which would instead process arbitrarily long files sequentially without buffering too much into memory. He chose the name because in ed, the command `g/*re*/p`, where the *`re`* is the **r**egular **e**xpression to match, would print all lines featuring a specified pattern match. grep was first included in Version 4 Unix. Stating that it is "generally cited as *the* prototypical software tool", McIlroy credited grep with "irrevocably ingraining" Thompson's tools philosophy in Unix.

## Implementations

A variety of grep implementations are available in many operating systems and software development environments. Early variants included `egrep` and `fgrep`, introduced in Version 7 Unix. The `egrep` variant supports an extended regular expression syntax added by Alfred Aho after Ken Thompson's original regular expression implementation. The `fgrep` variant searches for any of a list of *fixed* strings using the Aho–Corasick string matching algorithm. Binaries of these variants exist in modern systems, usually linking to grep or calling grep as a shell script with the appropriate flag added, e.g. `exec grep -E "$@"`. Commands `egrep` and `fgrep`, while commonly deployed on POSIX systems, to the point the POSIX specification mentions their widespread existence, are actually not part of POSIX.

Other commands contain the word "grep" to indicate they are search tools, typically ones that rely on regular expression matches. The `pgrep` utility, for instance, displays the processes whose names match a given regular expression.

In the Perl programming language, `grep` is a built-in function that finds elements in a list that satisfy a certain property. This higher-order function is typically named `filter` or `where` in other languages.

The `pcregrep` command is an implementation of grep that uses Perl regular expression syntax. Similar functionality can be invoked in the GNU version of grep with the `-P` flag.

Ports of grep (within Cygwin and GnuWin32, for example) also run under Microsoft Windows. Some versions of Windows feature the similar `qgrep` or `findstr` command.

A grep command is also part of ASCII's *MSX-DOS2 Tools* for MSX-DOS version 2.

The `grep`, `egrep`, and `fgrep` commands have also been ported to the IBM i operating system.

The software Adobe InDesign has functions GREP (since CS3 version (2007)), in the *find/change* dialog box "GREP" tab, and introduced with InDesign CS4 in *paragraph styles* "GREP styles".

### agrep

**`agrep`** (approximate grep) is an open-source approximate string matching program, developed by Udi Manber and Sun Wu between 1988 and 1991, for use with the Unix operating system. It was later ported to OS/2, DOS, and Windows.

*a*grep matches even when the text only *approximately* fits the search pattern.

This following invocation finds `netmasks` in file `myfile`, but also any other word that can be derived from it, given no more than two substitutions.

```
agrep -2 netmasks myfile
```

This example generates a list of matches with the closest, that is those with the fewest, substitutions listed first. The command flag `-B` means "best":

```
agrep -B netmasks myfile
```

## Usage as a verb

In December 2003, the *Oxford English Dictionary Online* added "grep" as both a noun and a verb.

A common verb usage is the phrase "You can't grep dead trees"—meaning one can more easily search through digital media, using tools such as grep, than one could with a hard copy (i.e. one made from "dead trees", which in this context is a dysphemism for paper).

---
title: "The GNU Awk User’s Guide (part 1/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 1/38
---

# General Introduction

This file documents `awk`, a program that you can use to select particular records in a file and perform operations upon them.

Copyright © 1989, 1991, 1992, 1993, 1996–2005, 2007, 2009–2026 Free Software Foundation, Inc.

This is Edition 5.4 of *GAWK: Effective AWK Programming: A User’s Guide for GNU Awk*, for the 5.4.0 (or later) version of the GNU implementation of AWK.

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being “GNU General Public License”, with the Front-Cover Texts being “A GNU Manual”, and with the Back-Cover Texts as in (a) below. A copy of the license is included in the section entitled “GNU Free Documentation License”.

1. The FSF’s Back-Cover Text is: “You have the freedom to copy and modify this GNU manual.”


## Short Table of Contents


## Foreword to the Third Edition

Arnold Robbins and I are good friends. We were introduced in 1990 by circumstances—and our favorite programming language, AWK. The circumstances started a couple of years earlier. I was working at a new job and noticed an unplugged Unix computer sitting in the corner. No one knew how to use it, and neither did I. However, a couple of days later, it was running, and I was `root` and the one-and-only user. That day, I began the transition from statistician to Unix programmer.

On one of many trips to the library or bookstore in search of books on Unix, I found the gray AWK book, a.k.a. Alfred V. Aho, Brian W. Kernighan, and Peter J. Weinberger’s *The AWK Programming Language* (Addison-Wesley, 1988). `awk`’s simple programming paradigm—find a pattern in the input and then perform an action—often reduced complex or tedious data manipulations to a few lines of code. I was excited to try my hand at programming in AWK.

Alas, the `awk` on my computer was a limited version of the language described in the gray book. I discovered that my computer had “old `awk`” and the book described “new `awk`.” I learned that this was typical; the old version refused to step aside or relinquish its name. If a system had a new `awk`, it was invariably called `nawk`, and few systems had it. The best way to get a new `awk` was to `ftp` the source code for `gawk` from `prep.ai.mit.edu`. `gawk` was a version of new `awk` written by David Trueman and Arnold, and available under the GNU General Public License.

(Incidentally, it’s no longer difficult to find a new `awk`. `gawk` ships with GNU/Linux, and you can download binaries or source code for almost any system; my wife uses `gawk` on her VMS box.)

My Unix system started out unplugged from the wall; it certainly was not plugged into a network. So, oblivious to the existence of `gawk` and the Unix community in general, and desiring a new `awk`, I wrote my own, called `mawk`. Before I was finished, I knew about `gawk`, but it was too late to stop, so I eventually posted to a `comp.sources` newsgroup.

A few days after my posting, I got a friendly email from Arnold introducing himself. He suggested we share design and algorithms and attached a draft of the POSIX standard so that I could update `mawk` to support language extensions added after publication of *The AWK Programming Language*.

Frankly, if our roles had been reversed, I would not have been so open and we probably would have never met. I’m glad we did meet. He is an AWK expert’s AWK expert and a genuinely nice person. Arnold contributes significant amounts of his expertise and time to the Free Software Foundation.

This book is the `gawk` reference manual, but at its core it is a book about AWK programming that will appeal to a wide audience. It is a definitive reference to the AWK language as defined by the 1987 Bell Laboratories release and codified in the 1992 POSIX Utilities standard.

On the other hand, the novice AWK programmer can study a wealth of practical programs that emphasize the power of AWK’s basic idioms: data-driven control flow, pattern matching with regular expressions, and associative arrays. Those looking for something new can try out `gawk`’s interface to network protocols via special /inet files.

The programs in this book make clear that an AWK program is typically much smaller and faster to develop than a counterpart written in C. Consequently, there is often a payoff to prototyping an algorithm or design in AWK to get it running quickly and expose problems early. Often, the interpreted performance is adequate and the AWK prototype becomes the product.

The new `pgawk` (profiling `gawk`), produces program execution counts. I recently experimented with an algorithm that for *n* lines of input, exhibited ~ C n^2 performance, while theory predicted ~ C n log n behavior. A few minutes poring over the awkprof.out profile pinpointed the problem to a single line of code. `pgawk` is a welcome addition to my programmer’s toolbox.

Arnold has distilled over a decade of experience writing and using AWK programs, and developing `gawk`, into this book. If you use AWK or want to learn how, then read this book.

```
Michael Brennan
Author of mawk
March 2001
```


## Foreword to the Fourth Edition

Some things don’t change. Thirteen years ago I wrote: “If you use AWK or want to learn how, then read this book.” True then, and still true today.

Learning to use a programming language is about more than mastering the syntax. One needs to acquire an understanding of how to use the features of the language to solve practical programming problems. A focus of this book is many examples that show how to use AWK.

Some things do change. Our computers are much faster and have more memory. Consequently, speed and storage inefficiencies of a high-level language matter less. Prototyping in AWK and then rewriting in C for performance reasons happens less, because more often the prototype is fast enough.

Of course, there are computing operations that are best done in C or C++. With `gawk` 4.1 and later, you do not have to choose between writing your program in AWK or in C/C++. You can write most of your program in AWK and the aspects that require C/C++ capabilities can be written in C/C++, and then the pieces glued together when the `gawk` module loads the C/C++ module as a dynamic plug-in. Writing Extensions for `gawk`, has all the details, and, as expected, many examples to help you learn the ins and outs.

I enjoy programming in AWK and had fun (re)reading this book. I think you will too.

```
Michael Brennan
Author of mawk
October 2014
```


## Preface

Several kinds of tasks occur repeatedly when working with text files. You might want to extract certain lines and discard the rest. Or you may need to make changes wherever certain patterns appear, but leave the rest of the file alone. Such jobs are often easy with `awk`. The `awk` utility interprets a special-purpose programming language that makes it easy to handle simple data-reformatting jobs.

The GNU implementation of `awk` is called `gawk`; if you invoke it with the proper options or environment variables, it is fully compatible with the POSIX1 specification of the `awk` language and with the Unix version of `awk` maintained by Brian Kernighan. This means that all properly written `awk` programs should work with `gawk`. So most of the time, we don’t distinguish between `gawk` and other `awk` implementations.

Using `awk` you can:

- Manage small, personal databases
- Generate reports
- Validate data
- Produce indexes and perform other document-preparation tasks
- Experiment with algorithms that you can adapt later to other computer languages

In addition, `gawk` provides facilities that make it easy to:

- Extract bits and pieces of data for processing
- Sort data
- Perform simple network communications
- Profile and debug `awk` programs
- Extend the language with functions written in C or C++

This Web page teaches you about the `awk` language and how you can use it effectively. You should already be familiar with basic system commands, such as `cat` and `ls`,2 as well as basic shell facilities, such as input/output (I/O) redirection and pipes.

Implementations of the `awk` language are available for many different computing environments. This Web page, while describing the `awk` language in general, also describes the particular implementation of `awk` called `gawk` (which stands for “GNU `awk`”). `gawk` runs on a broad range of Unix systems, ranging from Intel-architecture PC-based computers up through large-scale systems. `gawk` has also been ported to macOS, z/OS, Microsoft Windows (all versions), and OpenVMS.3

### History of `awk` and `gawk`

| Recipe for a Programming Language |
|---|
| 1 part `egrep`1 part `snobol` 2 parts `ed`3 parts C Blend all parts well using `lex` and `yacc`. Document minimally and release. After eight years, add another part `egrep` and two more parts C. Document very well and release. After 35 more years, add Unicode and CSV support, sprinkle lightly with a few choice features from `gawk`, document very well again, and release. |

The name `awk` comes from the initials of its designers: Alfred V. Aho, Peter J. Weinberger, and Brian W. Kernighan. The original version of `awk` was written in 1977 at AT&T Bell Laboratories. In 1985, a new version made the programming language more powerful, introducing user-defined functions, multiple input streams, and computed regular expressions. This new version became widely available with Unix System V Release 3.1 (1987). The version in System V Release 4 (1989) added some new features and cleaned up the behavior in some of the “dark corners” of the language. The specification for `awk` in the POSIX Command Language and Utilities standard further clarified the language. Both the `gawk` designers and the original `awk` designers at Bell Laboratories provided feedback for the POSIX specification.

Paul Rubin wrote `gawk` in 1986. Jay Fenlason completed it, with advice from Richard Stallman. John Woods contributed parts of the code as well. In 1988 and 1989, David Trueman, with help from me, thoroughly reworked `gawk` for compatibility with the newer `awk`. Circa 1994, I became the primary maintainer. Current development focuses on bug fixes, performance improvements, standards compliance, and, occasionally, new features.

In May 1997, Jürgen Kahrs felt the need for network access from `awk`, and with a little help from me, set about adding features to do this for `gawk`. At that time, he also wrote the bulk of *TCP/IP Internetworking with `gawk`* (a separate document, available as part of the `gawk` distribution). His code finally became part of the main `gawk` distribution with `gawk` version 3.1.

John Haque rewrote the `gawk` internals, in the process providing an `awk`-level debugger. This version became available as `gawk` version 4.0 in 2011.

See Major Contributors to `gawk` for a full list of those who have made important contributions to `gawk`.

### A Rose by Any Other Name

The `awk` language has evolved over the years. Full details are provided in The Evolution of the `awk` Language. The language described in this Web page is often referred to as “new `awk`.” By analogy, the original version of `awk` is referred to as “old `awk`.”

On most current systems, when you run the `awk` utility you get some version of new `awk`.4 If your system’s standard `awk` is the old one, you will see something like this if you try the following test program:

```
$ awk 1 /dev/null
error→ awk: syntax error near line 1
error→ awk: bailing out near line 1
```

In this case, you should find a version of new `awk`, or just install `gawk`!

Throughout this Web page, whenever we refer to a language feature that should be available in any complete implementation of POSIX `awk`, we simply use the term `awk`. When referring to a feature that is specific to the GNU implementation, we use the term `gawk`.

### Using This Book

The term `awk` refers to a particular program as well as to the language you use to tell this program what to do. When we need to be careful, we call the language “the `awk` language,” and the program “the `awk` utility.” This Web page explains both how to write programs in the `awk` language and how to run the `awk` utility. The term “`awk` program” refers to a program written by you in the `awk` programming language.

Primarily, this Web page explains the features of `awk` as defined in the POSIX standard. It does so in the context of the `gawk` implementation. While doing so, it also attempts to describe important differences between `gawk` and other `awk` implementations.5 Finally, it notes any `gawk` features that are not in the POSIX standard for `awk`.

This Web page has the difficult task of being both a tutorial and a reference. If you are a novice, feel free to skip over details that seem too complex. You should also ignore the many cross-references; they are for the expert user and for the Info and HTML versions of the Web page.

There are sidebars scattered throughout the Web page. They add a more complete explanation of points that are relevant, but not likely to be of interest on first reading. All appear in the index, under the heading “sidebar.”

Most of the time, the examples use complete `awk` programs. Some of the more advanced sections show only the part of the `awk` program that illustrates the concept being described.

Although this Web page is aimed principally at people who have not been exposed to `awk`, there is a lot of information here that even the `awk` expert should find useful. In particular, the description of POSIX `awk` and the example programs in A Library of `awk` Functions, and in Practical `awk` Programs, should be of interest.

This Web page is split into several parts, as follows:

- Part I describes the `awk` language and the `gawk` program in detail. It starts with the basics, and continues through all of the features of `awk`. It contains the following chapters:
  - Getting Started with `awk`, provides the essentials you need to know to begin using `awk`.
  - Running `awk` and `gawk`, describes how to run `gawk`, the meaning of its command-line options, and how it finds `awk` program source files.
  - Regular Expressions, introduces regular expressions in general, and in particular the flavors supported by POSIX `awk` and `gawk`.
  - Reading Input Files, describes how `awk` reads your data. It introduces the concepts of records and fields, as well as the `getline` function. I/O redirection is first described here. Network I/O is also briefly introduced here.
  - Printing Output, describes how `awk` programs can produce output with `print` and `printf`.
  - Expressions, describes expressions, which are the basic building blocks for getting most things done in a program.
  - Patterns, Actions, and Variables, describes how to write patterns for matching records, actions for doing something when a record is matched, and the predefined variables `awk` and `gawk` use.
  - Arrays in `awk`, covers `awk`’s one-and-only data structure: the associative array. Deleting array elements and whole arrays is described, as well as sorting arrays in `gawk`. The chapter also describes how `gawk` provides arrays of arrays.
  - Functions, describes the built-in functions `awk` and `gawk` provide, as well as how to define your own functions. It also discusses how `gawk` lets you call functions indirectly.
- Part II shows how to use `awk` and `gawk` for problem solving. There is lots of code here for you to read and learn from. This part contains the following chapters: Reading these two chapters allows you to see `awk` solving real problems.
  - A Library of `awk` Functions, provides a number of functions meant to be used from main `awk` programs.
  - Practical `awk` Programs, provides many sample `awk` programs.
- Part III focuses on features specific to `gawk`. It contains the following chapters:
  - Advanced Features of `gawk`, describes a number of advanced features. Of particular note are the abilities to control the order of array traversal, have two-way communications with another process, perform TCP/IP networking, and profile your `awk` programs.
  - Internationalization with `gawk`, describes special features for translating program messages into different languages at runtime.
  - Debugging `awk` Programs, describes the `gawk` debugger.
  - Namespaces in `gawk`, describes how `gawk` allows variables and/or functions of the same name to be in different namespaces.
  - Arithmetic and Arbitrary-Precision Arithmetic with `gawk`, describes advanced arithmetic facilities.
  - Writing Extensions for `gawk`, describes how to add new variables and functions to `gawk` by writing extensions in C or C++.
- Part IV provides the appendices, the Glossary, and two licenses that cover the `gawk` source code and this Web page, respectively. It contains the following appendices:
  - The Evolution of the `awk` Language, describes how the `awk` language has evolved since its first release to the present. It also describes how `gawk` has acquired features over time.
  - Installing `gawk`, describes how to get `gawk`, how to compile it on POSIX-compatible systems, and how to compile and use it on different non-POSIX systems. It also describes how to report bugs in `gawk` and where to get other freely available `awk` implementations.
  - Implementation Notes, describes how to disable `gawk`’s extensions, as well as how to contribute new code to `gawk`, and some possible future directions for `gawk` development.
  - Basic Programming Concepts, provides some very cursory background material for those who are completely unfamiliar with computer programming.
  - The Glossary, defines most, if not all, of the significant terms used throughout the Web page. If you find terms that you aren’t familiar with, try looking them up here.
  - GNU General Public License, and GNU Free Documentation License, present the licenses that cover the `gawk` source code and this Web page, respectively.

### Typographical Conventions

This Web page is written in Texinfo, the GNU documentation formatting language. A single Texinfo source file is used to produce both the printed and online versions of the documentation. Because of this, the typographical conventions are slightly different than in other books you may have read.

Examples you would type at the command line are preceded by the common shell primary and secondary prompts, ‘$’ and ‘>’, respectively. Input that you type is shown like this. Output from the command is preceded by the glyph “-|”. This typically represents the command’s standard output. Error messages and other output on the command’s standard error are preceded by the glyph “error→”. For example:

```
$ echo hi on stdout
-| hi on stdout
$ echo hello on stderr 1>&2
error→ hello on stderr
```

In the text, almost anything related to programming, such as command names, variable and function names, and string, numeric and regexp constants appear in `this font`. Code fragments appear in the same font and quoted, ‘like this’. Things that are replaced by the user or programmer appear in *this font*. Options look like this: -f. File names are indicated like this: /path/to/ourfile. Some things are emphasized *like this*, and if a point needs to be made strongly, it is done **like this**. The first occurrence of a new term is usually its *definition* and appears in the same font as the previous occurrence of “definition” in this sentence.

Characters that you type at the keyboard look like this. In particular, there are special characters called “control characters.” These are characters that you type by holding down both the CONTROL key and another key, at the same time. For example, a Ctrl-d is typed by first pressing and holding the CONTROL key, next pressing the d key, and finally releasing both keys.

For the sake of brevity, throughout this Web page, we refer to Brian Kernighan’s version of `awk` as “BWK `awk`.” (See Other Freely Available `awk` Implementations for information on his and other versions.)

#### Dark Corners

> *Dark corners are basically fractal—no matter how much you illuminate, there’s always a smaller but darker one.*

—

Brian Kernighan

Until the POSIX standard (and *GAWK: Effective AWK Programming*), many features of `awk` were either poorly documented or not documented at all. Descriptions of such features (often called “dark corners”) are noted in this Web page with “(d.c.).” They also appear in the index under the heading “dark corner.”

But, as noted by the opening quote, any coverage of dark corners is by definition incomplete.

Extensions to the standard `awk` language that are supported by more than one `awk` implementation are marked “(c.e.),” and listed in the index under “common extensions” and “extensions, common.”

### The GNU Project and This Book

The Free Software Foundation (FSF) is a nonprofit organization dedicated to the production and distribution of freely distributable software. It was founded by Richard M. Stallman, the author of the original Emacs editor. GNU Emacs is the most widely used version of Emacs today.

The GNU6 Project is an ongoing effort on the part of the Free Software Foundation to create a complete, freely distributable, POSIX-compliant computing environment. The FSF uses the GNU General Public License (GPL) to ensure that its software’s source code is always available to the end user. A copy of the GPL is included in this Web page for your reference (see GNU General Public License). The GPL applies to the C language source code for `gawk`. To find out more about the FSF and the GNU Project online, see the GNU Project’s home page. This Web page may also be read from GNU’s website.

A shell, an editor (Emacs), highly portable optimizing C, C++, and Objective-C compilers, a symbolic debugger and dozens of large and small utilities (such as `gawk`), have all been completed and are freely available. The GNU operating system kernel (the HURD), has been released but remains in an early stage of development.

Until the GNU operating system is more fully developed, you should consider using GNU/Linux, a freely distributable, Unix-like operating system for Intel, Power Architecture, Sun SPARC, IBM S/390, and other systems.7 Many GNU/Linux distributions are available for download from the Internet.

The Web page you are reading is actually free—at least, the information in it is free to anyone. The machine-readable source code for the Web page comes with `gawk`. (Take a moment to check the Free Documentation License in GNU Free Documentation License.)

The Web page itself has gone through multiple previous editions. Paul Rubin wrote the very first draft of *The GAWK Manual*; it was around 40 pages long. Diane Close and Richard Stallman improved it, yielding a version that was around 90 pages and barely described the original, “old” version of `awk`.

I started working with that version in the fall of 1988. As work on it progressed, the FSF published several preliminary versions (numbered 0.*x*). In 1996, edition 1.0 was released with `gawk` 3.0.0. The FSF published the first two editions under the title *The GNU Awk User’s Guide*.

This edition maintains the basic structure of the previous editions. For FSF edition 4.0, the content was thoroughly reviewed and updated. All references to `gawk` versions prior to 4.0 were removed. Of significant note for that edition was the addition of Debugging `awk` Programs.

For FSF edition 5.0, the content has been reorganized into parts, and the major new additions are Arithmetic and Arbitrary-Precision Arithmetic with `gawk`, and Writing Extensions for `gawk`.

This Web page will undoubtedly continue to evolve. If you find an error in the Web page, please report it! See Reporting Problems and Bugs for information on submitting problem reports electronically.

### How to Contribute

As the maintainer of GNU `awk`, I once thought that I would be able to manage a collection of publicly available `awk` programs and I even solicited contributions. Making things available on the Internet helps keep the `gawk` distribution down to manageable size.

The initial collection of material, such as it is, is still available at ftp://ftp.freefriends.org/arnold/Awkstuff.

In the hopes of doing something broader, I acquired the `awklang.org` domain. Late in 2017, a volunteer took on the task of managing it.

If you have written an interesting `awk` program that you would like to share with the rest of the world, please see http://www.awklang.org and use the “Contact” link.

If you have written a `gawk` extension, please see The `gawkextlib` Project.

### Acknowledgments

The initial draft of *The GAWK Manual* had the following acknowledgments:

> Many people need to be thanked for their assistance in producing this manual. Jay Fenlason contributed many ideas and sample programs. Richard Mlynarik and Robert Chassell gave helpful comments on drafts of this manual. The paper *A Supplemental Document for AWK* by John W. Pierce of the Chemistry Department at UC San Diego, pinpointed several issues relevant both to `awk` implementation and to this manual, that would otherwise have escaped us.

I would like to acknowledge Richard M. Stallman, for his vision of a better world and for his courage in founding the FSF and starting the GNU Project.

Earlier editions of this Web page had the following acknowledgements:

> The following people (in alphabetical order) provided helpful comments on various versions of this book: Rick Adams, Dr. Nelson H.F. Beebe, Karl Berry, Dr. Michael Brennan, Rich Burridge, Claire Cloutier, Diane Close, Scott Deifik, Christopher (“Topher”) Eliot, Jeffrey Friedl, Dr. Darrel Hankerson, Michal Jaegermann, Dr. Richard J. LeBlanc, Michael Lijewski, Pat Rankin, Miriam Robbins, Mary Sheehan, and Chuck Toporek.
> 
> Robert J. Chassell provided much valuable advice on the use of Texinfo. He also deserves special thanks for convincing me *not* to title this Web page *How to Gawk Politely*. Karl Berry helped significantly with the TeX part of Texinfo.
> 
> I would like to thank Marshall and Elaine Hartholz of Seattle and Dr. Bert and Rita Schreiber of Detroit for large amounts of quiet vacation time in their homes, which allowed me to make significant progress on this Web page and on `gawk` itself.
> 
> Phil Hughes of SSC contributed in a very important way by loaning me his laptop GNU/Linux system, not once, but twice, which allowed me to do a lot of work while away from home.
> 
> David Trueman deserves special credit; he has done a yeoman job of evolving `gawk` so that it performs well and without bugs. Although he is no longer involved with `gawk`, working with him on this project was a significant pleasure.
> 
> The intrepid members of the GNITS mailing list, and most notably Ulrich Drepper, provided invaluable help and feedback for the design of the internationalization features.
> 
> Chuck Toporek, Mary Sheehan, and Claire Cloutier of O’Reilly & Associates contributed significant editorial help for this Web page for the 3.1 release of `gawk`.

Dr. Nelson Beebe, Andreas Buening, Dr. Manuel Collado, Antonio Colombo, Stephen Davies, Scott Deifik, Akim Demaille, Daniel Richard G., Juan Manuel Guerrero, Darrel Hankerson, Michal Jaegermann, Jürgen Kahrs, Stepan Kasal, John Malmberg, Chet Ramey, Pat Rankin, Andrew Schorr, Corinna Vinschen, and Eli Zaretskii (in alphabetical order) make up the current `gawk` “crack portability team.” Without their hard work and help, `gawk` would not be nearly the robust, portable program it is today. It has been and continues to be a pleasure working with this team of fine people.

Notable code and documentation contributions were made by a number of people. See Major Contributors to `gawk` for the full list.

Thanks to Michael Brennan for the Forewords.

Thanks to Patrice Dumas for the new `makeinfo` program. Thanks to Karl Berry for his past work on Texinfo, and to Gavin Smith, who continues to work to improve the Texinfo markup language.

Robert P.J. Day, Michael Brennan, and Brian Kernighan kindly acted as reviewers for the 2015 edition of this Web page. Their feedback helped improve the final work.

I would also like to thank Brian Kernighan for his invaluable assistance during the testing and debugging of `gawk`, and for his ongoing help and advice in clarifying numerous points about the language. We could not have done nearly as good a job on either `gawk` or its documentation without his help.

Brian is in a class by himself as a programmer and technical author. I have to thank him (yet again) for his ongoing friendship and for being a role model to me for over 30 years! Having him as a reviewer is an exciting privilege. It has also been extremely humbling...

I must thank my wonderful wife, Miriam, for her patience through the many versions of this project, for her proofreading, and for sharing me with the computer. I would like to thank my parents for their love, and for the grace with which they raised and educated me. Finally, I also must acknowledge my gratitude to G-d, for the many opportunities He has sent my way, as well as for the gifts He has given me with which to take advantage of those opportunities.

Arnold Robbins Nof Ayalon Israel March, 2020

# Part I: The `awk` Language

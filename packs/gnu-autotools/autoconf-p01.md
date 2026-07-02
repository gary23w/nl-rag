---
title: "Autoconf (part 1/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 1/26
---

# Autoconf

This manual (17 March 2026) is for GNU Autoconf (version 2.73), a package for creating scripts to configure source code packages using templates and an M4 macro package.

Copyright © 1992–1996, 1998–2017, 2020–2026 Free Software Foundation, Inc.

> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover texts, and no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License.”


## 1 Introduction

A physicist, an engineer, and a computer scientist were discussing the nature of God. “Surely a Physicist,” said the physicist, “because early in the Creation, God made Light; and you know, Maxwell’s equations, the dual nature of electromagnetic waves, the relativistic consequences...” “An Engineer!,” said the engineer, “because before making Light, God split the Chaos into Land and Water; it takes a hell of an engineer to handle that big amount of mud, and orderly separation of solids from liquids...” The computer scientist shouted: “And the Chaos, where do you think it was coming from, hmm?”

—Anonymous

Autoconf is a tool for producing shell scripts that automatically configure software source code packages to adapt to many kinds of POSIX-like systems. The configuration scripts produced by Autoconf are independent of Autoconf when they are run, so their users do not need to have Autoconf.

The configuration scripts produced by Autoconf require no manual user intervention when run; they do not normally even need an argument specifying the system type. Instead, they individually test for the presence of each feature that the software package they are for might need. (Before each check, they print a one-line message stating what they are checking for, so the user doesn’t get too bored while waiting for the script to finish.) As a result, they deal well with systems that are hybrids or customized from the more common POSIX variants. There is no need to maintain files that list the features supported by each release of each variant of POSIX.

For each software package that Autoconf is used with, it creates a configuration script from a template file that lists the system features that the package needs or can use. After the shell code to recognize and respond to a system feature has been written, Autoconf allows it to be shared by many software packages that can use (or need) that feature. If it later turns out that the shell code needs adjustment for some reason, it needs to be changed in only one place; all of the configuration scripts can be regenerated automatically to take advantage of the updated code.

Those who do not understand Autoconf are condemned to reinvent it, poorly. The primary goal of Autoconf is making the *user’s* life easier; making the *maintainer’s* life easier is only a secondary goal. Put another way, the primary goal is not to make the generation of configure automatic for package maintainers (although patches along that front are welcome, since package maintainers form the user base of Autoconf); rather, the goal is to make configure painless, portable, and predictable for the end user of each *autoconfiscated* package. And to this degree, Autoconf is highly successful at its goal—most complaints to the Autoconf list are about difficulties in writing Autoconf input, and not in the behavior of the resulting configure. Even packages that don’t use Autoconf will generally provide a configure script, and the most common complaint about these alternative home-grown scripts is that they fail to meet one or more of the GNU Coding Standards (see Configuration in *The GNU Coding Standards*) that users have come to expect from Autoconf-generated configure scripts.

The Metaconfig package is similar in purpose to Autoconf, but the scripts it produces require manual user intervention, which is quite inconvenient when configuring large source trees. Unlike Metaconfig scripts, Autoconf scripts can support cross-compiling, if some care is taken in writing them.

Autoconf does not solve all problems related to making portable software packages—for a more complete solution, it should be used in concert with other GNU build tools like Automake and Libtool. These other tools take on jobs like the creation of a portable, recursive makefile with all of the standard targets, linking of shared libraries, and so on. See The GNU Build System, for more information.

Autoconf imposes some restrictions on the names of macros used with `#if` in C programs (see Preprocessor Symbol Index).

Autoconf requires GNU M4 version 1.4.8 or later in order to generate the scripts. It uses features that some versions of M4, including GNU M4 1.3, do not have. Autoconf works better with GNU M4 version 1.4.16 or later, though this is not required.

See Upgrading From Version 1, for information about upgrading from version 1. See History of Autoconf, for the story of Autoconf’s development. See Frequent Autoconf Questions, with answers, for answers to some common questions about Autoconf.

See the Autoconf web page for up-to-date information, details on the mailing lists, pointers to a list of known bugs, etc.

Mail suggestions to the Autoconf mailing list. Past suggestions are archived.

Mail bug reports to the Autoconf Bugs mailing list. Past bug reports are archived.

If possible, first check that your bug is not already solved in current development versions, and that it has not been reported yet. Be sure to include all the needed information and a short configure.ac that demonstrates the problem.

Autoconf’s development tree is accessible via `git`; see the Autoconf Summary for details, or view the actual repository. Patches relative to the current `git` version can be sent for review to the Autoconf Patches mailing list, with discussion on prior patches archived; and all commits are posted in the read-only Autoconf Commit mailing list, which is also archived.

Because of its mission, the Autoconf package itself includes only a set of often-used macros that have already demonstrated their usefulness. Nevertheless, if you wish to share your macros, or find existing ones, see the Autoconf Macro Archive, which is kindly run by Peter Simons.


## 2 The GNU Build System

Autoconf solves an important problem—reliable discovery of system-specific build and runtime information—but this is only one piece of the puzzle for the development of portable software. To this end, the GNU project has developed a suite of integrated utilities to finish the job Autoconf started: the GNU build system, whose most important components are Autoconf, Automake, and Libtool. In this chapter, we introduce you to those tools, point you to sources of more information, and try to convince you to use the entire GNU build system for your software.

### 2.1 Automake

The ubiquity of `make` means that a makefile is almost the only viable way to distribute automatic build rules for software, but one quickly runs into its numerous limitations. Its lack of support for automatic dependency tracking, recursive builds in subdirectories, reliable timestamps (e.g., for network file systems), and so on, mean that developers must painfully (and often incorrectly) reinvent the wheel for each project. Portability is non-trivial, thanks to the quirks of `make` on many systems. On top of all this is the manual labor required to implement the many standard targets that users have come to expect (`make install`, `make distclean`, `make uninstall`, etc.). Since you are, of course, using Autoconf, you also have to insert repetitive code in your Makefile.in to recognize `@CC@`, `@CFLAGS@`, and other substitutions provided by `configure`. Into this mess steps *Automake*.

Automake allows you to specify your build needs in a Makefile.am file with a vastly simpler and more powerful syntax than that of a plain makefile, and then generates a portable Makefile.in for use with Autoconf. For example, the Makefile.am to build and install a simple “Hello world” program might look like:

```
bin_PROGRAMS = hello
hello_SOURCES = hello.c
```

The resulting Makefile.in (~400 lines) automatically supports all the standard targets, the substitutions provided by Autoconf, automatic dependency tracking, `VPATH` building, and so on. `make` builds the `hello` program, and `make install` installs it in /usr/local/bin (or whatever prefix was given to `configure`, if not /usr/local).

The benefits of Automake increase for larger packages (especially ones with subdirectories), but even for small programs the added convenience and portability can be substantial. And that’s not all...

### 2.2 Gnulib

GNU software has a well-deserved reputation for running on many different types of systems. While our primary goal is to write software for the GNU system, many users and developers have been introduced to us through the systems that they were already using.

Gnulib is a central location for common GNU code, intended to be shared among free software packages. Its components are typically shared at the source level, rather than being a library that gets built, installed, and linked against. The idea is to copy files from Gnulib into your own source tree. There is no distribution tarball; developers should just grab source modules from the repository. The source files are available online, under various licenses, mostly GNU GPL or GNU LGPL.

Gnulib modules typically contain C source code along with Autoconf macros used to configure the source code. For example, the Gnulib `stdckdint` module implements a stdckdint.h header that nearly conforms to C23, even on older hosts that lack stdckdint.h. This module contains a source file for the replacement header, along with an Autoconf macro that arranges to use the replacement header on older systems.

For more information, consult the Gnulib website, https://www.gnu.org/software/gnulib/.

### 2.3 Libtool

Often, one wants to build not only programs, but libraries, so that other programs can benefit from the fruits of your labor. Ideally, one would like to produce *shared* (dynamically linked) libraries, which can be used by multiple programs without duplication on disk or in memory and can be updated independently of the linked programs. Producing shared libraries portably, however, is the stuff of nightmares—each system has its own incompatible tools, compiler flags, and magic incantations. Fortunately, GNU provides a solution: *Libtool*.

Libtool handles all the requirements of building shared libraries for you, and at this time seems to be the *only* way to do so with any portability. It also handles many other headaches, such as: the interaction of Make rules with the variable suffixes of shared libraries, linking reliably with shared libraries before they are installed by the superuser, and supplying a consistent versioning system (so that different versions of a library can be installed or upgraded without breaking binary compatibility). Although Libtool, like Autoconf, can be used without Automake, it is most simply utilized in conjunction with Automake—there, Libtool is used automatically whenever shared libraries are needed, and you need not know its syntax.

### 2.4 Pointers

Developers who are used to the simplicity of `make` for small projects on a single system might be daunted at the prospect of learning to use Automake and Autoconf. As your software is distributed to more and more users, however, you otherwise quickly find yourself putting lots of effort into reinventing the services that the GNU build tools provide, and making the same mistakes that they once made and overcame. (Besides, since you’re already learning Autoconf, Automake is a piece of cake.)

There are a number of places that you can go to for more information on the GNU build tools.

- Web The project home pages for Autoconf, Automake, Gnulib, and Libtool.
- Automake Manual See Automake in *GNU Automake*, for more information on Automake.
- Books The book *GNU Autoconf, Automake and Libtool*1 describes the complete GNU build environment. You can also find the entire book on-line.


## 3 Making `configure` Scripts

The configuration scripts that Autoconf produces are by convention called `configure`. When run, `configure` creates several files, replacing configuration parameters in them with appropriate values. The files that `configure` creates are:

- one or more Makefile files, usually one in each subdirectory of the package (see Substitutions in Makefiles);
- optionally, a C header file, the name of which is configurable, containing `#define` directives (see Configuration Header Files);
- a shell script called config.status that, when run, recreates the files listed above (see config.status Invocation);
- an optional shell script normally called config.cache (created when using ‘configure --config-cache’) that saves the results of running many of the tests (see Cache Files);
- a file called config.log containing any messages produced by compilers, to help debugging if `configure` makes a mistake.

To create a `configure` script with Autoconf, you need to write an Autoconf input file configure.ac and run `autoconf` on it. If you write your own feature tests to supplement those that come with Autoconf, you might also write files called aclocal.m4 and acsite.m4. If you use a C header file to contain `#define` directives, you might also run `autoheader`, and you can distribute the generated file config.h.in with the package.

Here is a diagram showing how the files that can be used in configuration are produced. Programs that are executed are suffixed by ‘*’. Optional files are enclosed in square brackets (‘[]’). `autoconf` and `autoheader` also read the installed Autoconf macro files (by reading autoconf.m4).

Files used in preparing a software package for distribution, when using just Autoconf:

```
your source files --> [autoscan*] --> [configure.scan] --> configure.ac
```

```
configure.ac --.
               |   .------> autoconf* -----> configure
[aclocal.m4] --+---+
               |   `-----> [autoheader*] --> [config.h.in]
[acsite.m4] ---'
```

```
Makefile.in
```

Additionally, if you use Automake, the following additional productions come into play:

```
[acinclude.m4] --.
                 |
[local macros] --+--> aclocal* --> aclocal.m4
                 |
configure.ac ----'
```

```
configure.ac --.
               +--> automake* --> Makefile.in
Makefile.am ---'
```

Files used in configuring a software package:

```
                       .-------------> [config.cache]
configure* ------------+-------------> config.log
                       |
[config.h.in] -.       v            .-> [config.h] -.
               +--> config.status* -+               +--> make*
Makefile.in ---'                    `-> Makefile ---'
```

### 3.1 Writing configure.ac

To produce a `configure` script for a software package, create a file called configure.ac that contains invocations of the Autoconf macros that test the system features your package needs or can use. Autoconf macros already exist to check for many features; see Existing Tests, for their descriptions. For most other features, you can use Autoconf template macros to produce custom checks; see Writing Tests, for information about them. For especially tricky or specialized features, configure.ac might need to contain some hand-crafted shell commands; see Portable Shell Programming. The `autoscan` program can give you a good start in writing configure.ac (see Using `autoscan` to Create configure.ac, for more information).

Previous versions of Autoconf promoted the name configure.in, which is somewhat ambiguous (the tool needed to process this file is not described by its extension), and introduces a slight confusion with config.h.in and so on (for which ‘.in’ means “to be processed by `configure`”). Using configure.ac is now preferred, while the use of configure.in will cause warnings from `autoconf`.

#### 3.1.1 A Shell Script Compiler

Just as for any other computer language, in order to properly program configure.ac in Autoconf you must understand *what* problem the language tries to address and *how* it does so.

The problem Autoconf addresses is that the world is a mess. After all, you are using Autoconf in order to have your package compile easily on all sorts of different systems, some of them being extremely hostile. Autoconf itself bears the price for these differences: `configure` must run on all those systems, and thus `configure` must limit itself to their lowest common denominator of features.

Naturally, you might then think of shell scripts; who needs `autoconf`? A set of properly written shell functions is enough to make it easy to write `configure` scripts by hand. Sigh! Unfortunately, even in 2008, where shells without any function support are far and few between, there are pitfalls to avoid when making use of them. Also, finding a Bourne shell that accepts shell functions is not trivial, even though there is almost always one on interesting porting targets.

So, what is really needed is some kind of compiler, `autoconf`, that takes an Autoconf program, configure.ac, and transforms it into a portable shell script, `configure`.

How does `autoconf` perform this task?

There are two obvious possibilities: creating a brand new language or extending an existing one. The former option is attractive: all sorts of optimizations could easily be implemented in the compiler and many rigorous checks could be performed on the Autoconf program (e.g., rejecting any non-portable construct). Alternatively, you can extend an existing language, such as the `sh` (Bourne shell) language.

Autoconf does the latter: it is a layer on top of `sh`. It was therefore most convenient to implement `autoconf` as a macro expander: a program that repeatedly performs *macro expansions* on text input, replacing macro calls with macro bodies and producing a pure `sh` script in the end. Instead of implementing a dedicated Autoconf macro expander, it is natural to use an existing general-purpose macro language, such as M4, and implement the extensions as a set of M4 macros.

#### 3.1.2 The Autoconf Language

The Autoconf language differs from many other computer languages because it treats actual code the same as plain text. Whereas in C, for instance, data and instructions have different syntactic status, in Autoconf their status is rigorously the same. Therefore, we need a means to distinguish literal strings from text to be expanded: quotation.

When calling macros that take arguments, there must not be any white space between the macro name and the open parenthesis.

```
AC_INIT ([oops], [1.0]) # incorrect
AC_INIT([hello], [1.0]) # good
```

Arguments should be enclosed within the quote characters ‘[’ and ‘]’, and be separated by commas. Any leading blanks or newlines in arguments are ignored, unless they are quoted. You should always quote an argument that might contain a macro name, comma, parenthesis, or a leading blank or newline. This rule applies recursively for every macro call, including macros called from other macros. For more details on quoting rules, see Programming in M4.

For instance:

```
AC_CHECK_HEADER([stdio.h],
                [AC_DEFINE([HAVE_STDIO_H], [1],
                   [Define to 1 if you have <stdio.h>.])],
                [AC_MSG_ERROR([sorry, can't do anything for you])])
```

is quoted properly. You may safely simplify its quotation to:

```
AC_CHECK_HEADER([stdio.h],
                [AC_DEFINE([HAVE_STDIO_H], 1,
                   [Define to 1 if you have <stdio.h>.])],
                [AC_MSG_ERROR([sorry, can't do anything for you])])
```

because ‘1’ cannot contain a macro call. Here, the argument of `AC_MSG_ERROR` must be quoted; otherwise, its comma would be interpreted as an argument separator. Also, the second and third arguments of ‘AC_CHECK_HEADER’ must be quoted, since they contain macro calls. The three arguments ‘HAVE_STDIO_H’, ‘stdio.h’, and ‘Define to 1 if you have <stdio.h>.’ do not need quoting, but if you unwisely defined a macro with a name like ‘Define’ or ‘stdio’ then they would need quoting. Cautious Autoconf users would keep the quotes, but many Autoconf users find such precautions annoying, and would rewrite the example as follows:

```
AC_CHECK_HEADER(stdio.h,
                [AC_DEFINE(HAVE_STDIO_H, 1,
                   [Define to 1 if you have <stdio.h>.])],
                [AC_MSG_ERROR([sorry, can't do anything for you])])
```

This is safe, so long as you adopt good naming conventions and do not define macros with names like ‘HAVE_STDIO_H’, ‘stdio’, or ‘h’. Though it is also safe here to omit the quotes around ‘Define to 1 if you have <stdio.h>.’ this is not recommended, as message strings are more likely to inadvertently contain commas.

The following example is wrong and dangerous, as it is underquoted:

```
AC_CHECK_HEADER(stdio.h,
                AC_DEFINE(HAVE_STDIO_H, 1,
                   Define to 1 if you have <stdio.h>.),
                AC_MSG_ERROR([sorry, can't do anything for you]))
```

In other cases, you may want to use text that also resembles a macro call. You must quote that text (whether just the potential problem, or the entire line) even when it is not passed as a macro argument; and you may also have to use `m4_pattern_allow` (see Forbidden Patterns), to declare your intention that the resulting configure file will have a literal that resembles what would otherwise be reserved for a macro name. For example:

```
dnl Simulate a possible future autoconf macro
m4_define([AC_DC], [oops])
dnl Underquoted:
echo "Hard rock was here!  --AC_DC"
dnl Correctly quoted:
m4_pattern_allow([AC_DC])
echo "Hard rock was here!  --[AC_DC]"
[echo "Hard rock was here!  --AC_DC"]
```

which results in this text in configure:

```
echo "Hard rock was here!  --oops"
echo "Hard rock was here!  --AC_DC"
echo "Hard rock was here!  --AC_DC"
```

When you use the same text in a macro argument, you must therefore have an extra quotation level (since one is stripped away by the macro substitution). In general, then, it is a good idea to *use double quoting for all literal string arguments*, either around just the problematic portions, or over the entire argument:

```
m4_pattern_allow([AC_DC])
AC_MSG_WARN([[AC_DC] stinks  --Iron Maiden])
AC_MSG_WARN([[AC_DC stinks  --Iron Maiden]])
```

It is also possible to avoid the problematic patterns in the first place, by the use of additional escaping (either a quadrigraph, or creative shell constructs), in which case it is no longer necessary to use `m4_pattern_allow`:

```
echo "Hard rock was here!  --AC""_DC"
AC_MSG_WARN([[AC@&t@_DC stinks  --Iron Maiden]])
```

You are now able to understand one of the constructs of Autoconf that has been continually misunderstood... The rule of thumb is that *whenever you expect macro expansion, expect quote expansion*; i.e., expect one level of quotes to be lost. For instance:

```
AC_COMPILE_IFELSE(AC_LANG_SOURCE([char b[10];]), [],
 [AC_MSG_ERROR([you lose])])
```

is incorrect: here, the first argument of `AC_LANG_SOURCE` is ‘char b[10];’ and is expanded once, which results in ‘char b10;’; and the `AC_LANG_SOURCE` is also expanded prior to being passed to `AC_COMPILE_IFELSE`. (There was an idiom common in Autoconf’s past to address this issue via the M4 `changequote` primitive, but do not use it!) Let’s take a closer look: the author meant the first argument to be understood as a literal, and therefore it must be quoted twice; likewise, the intermediate `AC_LANG_SOURCE` macro should be quoted once so that it is only expanded after the rest of the body of `AC_COMPILE_IFELSE` is in place:

```
AC_COMPILE_IFELSE([AC_LANG_SOURCE([[char b[10];]])], [],
  [AC_MSG_ERROR([you lose])])
```

Voilà, you actually produce ‘char b[10];’ this time!

On the other hand, descriptions (e.g., the last parameter of `AC_DEFINE` or `AS_HELP_STRING`) are not literals—they are subject to line breaking, for example—and should not be double quoted. Even if these descriptions are short and are not actually broken, double quoting them yields weird results.

Some macros take optional arguments, which this documentation represents as [*arg*] (not to be confused with the quote characters). You may just leave them empty, or use ‘[]’ to make the emptiness of the argument explicit, or you may simply omit the trailing commas. The three lines below are equivalent:

```
AC_CHECK_HEADERS([stdio.h], [], [], [])
AC_CHECK_HEADERS([stdio.h],,,)
AC_CHECK_HEADERS([stdio.h])
```

It is best to put each macro call on its own line in configure.ac. Most of the macros don’t add extra newlines; they rely on the newline after the macro call to terminate the commands. This approach makes the generated `configure` script a little easier to read by not inserting lots of blank lines. It is generally safe to set shell variables on the same line as a macro call, because the shell allows assignments without intervening newlines.

You can include comments in configure.ac files by starting them with the ‘#’. For example, it is helpful to begin configure.ac files with a line like this:

```
# Process this file with autoconf to produce a configure script.
```

#### 3.1.3 Standard configure.ac Layout

The order in which configure.ac calls the Autoconf macros is not important, with a few exceptions. Every configure.ac must contain a call to `AC_INIT` before the checks, and a call to `AC_OUTPUT` at the end (see Outputting Files). Additionally, some macros rely on other macros having been called first, because they check previously set values of some variables to decide what to do. These macros are noted in the individual descriptions (see Existing Tests), and they also warn you when `configure` is created if they are called out of order.

To encourage consistency, here is a suggested order for calling the Autoconf macros. Generally speaking, the things near the end of this list are those that could depend on things earlier in it. For example, library functions could be affected by types and libraries.

```
Autoconf requirements
AC_INIT(package, version, bug-report-address)
information on the package
checks for programs
checks for libraries
checks for header files
checks for types
checks for structures
checks for compiler characteristics
checks for library functions
checks for system services
AC_CONFIG_FILES([file...])
AC_OUTPUT
```

### 3.2 Using `autoscan` to Create configure.ac

The `autoscan` program can help you create and/or maintain a configure.ac file for a software package. `autoscan` examines source files in the directory tree rooted at a directory given as a command line argument, or the current directory if none is given. It searches the source files for common portability problems and creates a file configure.scan which is a preliminary configure.ac for that package, and checks a possibly existing configure.ac for completeness.

When using `autoscan` to create a configure.ac, you should manually examine configure.scan before renaming it to configure.ac; it probably needs some adjustments. Occasionally, `autoscan` outputs a macro in the wrong order relative to another macro, so that `autoconf` produces a warning; you need to move such macros manually. Also, if you want the package to use a configuration header file, you must add a call to `AC_CONFIG_HEADERS` (see Configuration Header Files). You might also have to change or add some `#if` directives to your program in order to make it work with Autoconf (see Using `ifnames` to List Conditionals, for information about a program that can help with that job).

When using `autoscan` to maintain a configure.ac, simply consider adding its suggestions. The file autoscan.log contains detailed information on why a macro is requested.

`autoscan` uses several data files (installed along with Autoconf) to determine which macros to output when it finds particular symbols in a package’s source files. These data files all have the same format: each line consists of a symbol, one or more blanks, and the Autoconf macro to output if that symbol is encountered. Lines starting with ‘#’ are comments.

`autoscan` accepts the following options:

**--help**

**-h**

Print a summary of the command line options and exit.

**--version**

**-V**

Print the version number of Autoconf and exit.

**--verbose**

**-v**

Print the names of the files it examines and the potentially interesting symbols it finds in them. This output can be voluminous.

**--debug**

**-d**

Don’t remove temporary files.

**--include=*dir***

**-I *dir***

Append *dir* to the include path. Multiple invocations accumulate.

**--prepend-include=*dir***

**-B *dir***

Prepend *dir* to the include path. Multiple invocations accumulate.

### 3.3 Using `ifnames` to List Conditionals

`ifnames` can help you write configure.ac for a software package. It prints the identifiers that the package already uses in C preprocessor conditionals. If a package has already been set up to have some portability, `ifnames` can thus help you figure out what its `configure` needs to check for. It may help fill in some gaps in a configure.ac generated by `autoscan` (see Using `autoscan` to Create configure.ac).

`ifnames` scans all of the C source files named on the command line (or the standard input, if none are given) and writes to the standard output a sorted list of all the identifiers that appear in those files in `#if`, `#ifdef`, `#ifndef`, `#elif`, `#elifdef`, or `#elifndef` directives. It prints each identifier on a line, followed by a space-separated list of the files in which that identifier occurs.

`ifnames` accepts the following options:

**--help**

**-h**

Print a summary of the command line options and exit.

**--version**

**-V**

Print the version number of Autoconf and exit.

### 3.4 Using `autoconf` to Create `configure`

To create `configure` from configure.ac, run the `autoconf` program with no arguments. `autoconf` processes configure.ac with the M4 macro processor, using the Autoconf macros. If you give `autoconf` an argument, it reads that file instead of configure.ac and writes the configuration script to the standard output instead of to `configure`. If you give `autoconf` the argument -, it reads from the standard input instead of configure.ac and writes the configuration script to the standard output.

The Autoconf macros are defined in several files. Some of the files are distributed with Autoconf; `autoconf` reads them first. Then it looks for the optional file acsite.m4 in the directory that contains the distributed Autoconf macro files, and for the optional file aclocal.m4 in the current directory. Those files can contain your site’s or the package’s own Autoconf macro definitions (see Writing Autoconf Macros, for more information). If a macro is defined in more than one of the files that `autoconf` reads, the last definition it reads overrides the earlier ones.

`autoconf` accepts the following options:

**--help**

**-h**

Print a summary of the command line options and exit.

**--version**

**-V**

Print the version number of Autoconf and exit.

**--verbose**

**-v**

Report processing steps.

**--debug**

**-d**

Don’t remove the temporary files.

**--force**

**-f**

Remake configure even if newer than its input files.

**--include=*dir***

**-I *dir***

Append *dir* to the include path. Multiple invocations accumulate.

**--prepend-include=*dir***

**-B *dir***

Prepend *dir* to the include path. Multiple invocations accumulate.

**--output=*file***

**-o *file***

Save output (script or trace) to *file*. The file - stands for the standard output.

**--warnings=*category*[,*category*...] ¶**

**-W*category*[,*category*...]**

Enable or disable warnings related to each *category*. See m4_warn, for a comprehensive list of categories. Special values include:

**‘all’**

Enable all categories of warnings.

**‘none’**

Disable all categories of warnings.

**‘error’**

Treat all warnings as errors.

**‘no-*category*’**

Disable warnings falling into *category*.

The environment variable `WARNINGS` may also be set to a comma-separated list of warning categories to enable or disable. It is interpreted exactly the same way as the argument of --warnings, but unknown categories are silently ignored. The command line takes precedence; for instance, if `WARNINGS` is set to `obsolete`, but -Wnone is given on the command line, no warnings will be issued.

Some categories of warnings are on by default. Again, for details see m4_warn.

**--trace=*macro*[:*format*]**

**-t *macro*[:*format*]**

Do not create the `configure` script, but list the calls to *macro* according to the *format*. Multiple --trace arguments can be used to list several macros. Multiple --trace arguments for a single macro are not cumulative; instead, you should just make *format* as long as needed.

The *format* is a regular string, with newlines if desired, and several special escape codes. It defaults to ‘$f:$l:$n:$%’; see Invoking `autom4te`, for details on the *format*.

**--initialization**

**-i**

By default, --trace does not trace the initialization of the Autoconf macros (typically the `AC_DEFUN` definitions). This results in a noticeable speedup, but can be disabled by this option.

It is often necessary to check the content of a configure.ac file, but parsing it yourself is extremely fragile and error-prone. It is suggested that you rely upon --trace to scan configure.ac. For instance, to find the list of variables that are substituted, use:

```
$ autoconf -t AC_SUBST
configure.ac:28:AC_SUBST:SHELL
configure.ac:28:AC_SUBST:PATH_SEPARATOR
More traces deleted
```

The example below highlights the difference between ‘$@’, ‘$*’, and ‘$%’.

```
$ cat configure.ac
AC_DEFINE(This, is, [an
[example]])
$ autoconf -t 'AC_DEFINE:@: $@
*: $*
%: $%'
@: [This],[is],[an
[example]]
*: This,is,an
[example]
%: This:is:an [example]
```

The *format* gives you a lot of freedom:

```
$ autoconf -t 'AC_SUBST:$$ac_subst{"$1"} = "$f:$l";'
$ac_subst{"SHELL"} = "configure.ac:28";
$ac_subst{"PATH_SEPARATOR"} = "configure.ac:28";
More traces deleted
```

A long *separator* can be used to improve the readability of complex structures, and to ease their parsing (for instance when no single character is suitable as a separator):

```
$ autoconf -t 'AM_MISSING_PROG:${|:::::|}*'
ACLOCAL|:::::|aclocal|:::::|$missing_dir
AUTOCONF|:::::|autoconf|:::::|$missing_dir
AUTOMAKE|:::::|automake|:::::|$missing_dir
More traces deleted
```

### 3.5 Using `autoreconf` to Update `configure` Scripts

Installing the various components of the GNU Build System can be tedious: running `autopoint` for Gettext, `automake` for Makefile.in etc. in each directory. It may be needed either because some tools such as `automake` have been updated on your system, or because some of the sources such as configure.ac have been updated, or finally, simply in order to install the GNU Build System in a fresh tree.

`autoreconf` runs `autoconf`, `autoheader`, `aclocal`, `automake`, `libtoolize`, `intltoolize`, `gtkdocize`, and `autopoint` (when appropriate) repeatedly to update the GNU Build System in the specified directories and their subdirectories (see Configuring Other Packages in Subdirectories). By default, it only remakes those files that are older than their sources.

If you install a new version of some tool, you can make `autoreconf` remake *all* of the files by giving it the --force option.

The environment variables `AUTOM4TE`, `AUTOCONF`, `AUTOHEADER`, `AUTOMAKE`, `ACLOCAL`, `AUTOPOINT`, `LIBTOOLIZE`, `INTLTOOLIZE`, `GTKDOCIZE`, `M4`, and `MAKE` may be used to override the invocation of the respective tools.

Except for `AUTOM4TE` and `M4`, setting any of these enviroment variables to ‘true’, ‘false’, ‘:’, or the empty string has the same effect as passing ‘--exclude=*cmd*’ on the command line, where *cmd* is the lowercased version of the command’s name; see the description of the --exclude option, below.

See Automatic Remaking, for Make rules to automatically rebuild `configure` scripts when their source files change. That method handles the timestamps of configuration header templates properly, but does not pass --autoconf-dir=*dir* or --localdir=*dir*.

Gettext supplies the `autopoint` command to add translation infrastructure to a source package. If you use `autopoint`, your configure.ac should invoke `AM_GNU_GETTEXT` and one of `AM_GNU_GETTEXT_VERSION(*gettext-version*)` or `AM_GNU_GETTEXT_REQUIRE_VERSION(*min-gettext-version*)`. See Invoking the `autopoint` Program in *GNU `gettext` utilities*, for further details.

`autoreconf` accepts the following options:

**--help**

**-h**

Print a summary of the command line options and exit.

**--version**

**-V**

Print the version number of Autoconf and exit.

**--verbose**

**-v**

Print the name of each directory `autoreconf` examines and the commands it runs. If given two or more times, pass --verbose to subordinate tools that support it.

**--debug**

**-d**

Don’t remove the temporary files.

**--force**

**-f**

Consider all generated and standard auxiliary files to be obsolete. This remakes even configure scripts and configuration headers that are newer than their input files (configure.ac and, if present, aclocal.m4).

If deemed appropriate, this option triggers calls to ‘automake --force-missing’. Passing both --force and --install to `autoreconf` will in turn undo any customizations to standard files. Note that the macro `AM_INIT_AUTOMAKE` has some options which change the set of files considered to be standard.

**--replace-handwritten**

**-R**

Replace files that *could* be generated but appear to have been written by hand. Currently this only affects the treatment of the primary configuration header template (usually config.h.in; see Configuration Header Templates). In the future it may also affect aclocal.m4 and others.

**--install**

**-i**

Install any missing standard auxiliary files in the package. By default, files are copied; this can be changed with --symlink.

If deemed appropriate, this option triggers calls to ‘automake --add-missing’, ‘libtoolize’, ‘autopoint’, etc.

**--no-recursive**

Do not rebuild files in subdirectories to configure (see Configuring Other Packages in Subdirectories, macro `AC_CONFIG_SUBDIRS`).

**--symlink**

**-s**

When used with --install, install symbolic links to the missing auxiliary files instead of copying them.

**--make**

**-m**

When the directories were configured, update the configuration by running ‘./config.status --recheck && ./config.status’, and then run ‘make’.

**--exclude=*cmd*[,*cmd*...]**

**-x *cmd*[,*cmd*...]**

Do not run any *cmd* in the list, even if it seems to be needed. *cmd* can be ‘autoconf’, ‘autoheader’, ‘automake’, ‘aclocal’, ‘autopoint’, ‘libtoolize’, ‘intltoolize’, ‘gtkdocize’, or ‘make’.

‘--exclude make’ has priority over ‘--make’.

**--include=*dir***

**-I *dir***

Append *dir* to the include path. Multiple invocations accumulate. Passed on to `aclocal`, `autoconf` and `autoheader` internally.

**--prepend-include=*dir***

**-B *dir***

Prepend *dir* to the include path. Multiple invocations accumulate. Passed on to `autoconf` and `autoheader` internally.

**--warnings=*category*[,*category*...] ¶**

**-W*category*[,*category*...]**

Enable or disable warnings related to each *category*. See m4_warn, for a comprehensive list of categories. Special values include:

**‘all’**

Enable all categories of warnings.

**‘none’**

Disable all categories of warnings.

**‘error’**

Treat all warnings as errors.

**‘no-*category*’**

Disable warnings falling into *category*.

The environment variable `WARNINGS` may also be set to a comma-separated list of warning categories to enable or disable. It is interpreted exactly the same way as the argument of --warnings, but unknown categories are silently ignored. The command line takes precedence; for instance, if `WARNINGS` is set to `obsolete`, but -Wnone is given on the command line, no warnings will be issued.

Some categories of warnings are on by default. Again, for details see m4_warn.

If you want `autoreconf` to pass flags that are not listed here on to `aclocal`, set `ACLOCAL_AMFLAGS` in your Makefile.am. Due to a limitation in the Autoconf implementation these flags currently must be set on a single line in Makefile.am, without any backslash-newlines or makefile comments. Also, be aware that future Automake releases might start flagging `ACLOCAL_AMFLAGS` as obsolescent, or even remove support for it.

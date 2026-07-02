---
title: "The GNU Awk User’s Guide (part 31/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 31/38
---

# The GNU Awk User’s Guide

(You may want to substitute a site-specific help library rather than the standard OpenVMS library ‘HELPLIB’.) After loading the help text, the command:

```
$ HELP GAWK
```

provides information about both the `gawk` implementation and the `awk` programming language.

The logical name ‘AWK_LIBRARY’ can designate a default location for `awk` program files. For the -f option, if the specified file name has no device or directory path information in it, `gawk` looks in the current directory first, then in the directory specified by the translation of ‘AWK_LIBRARY’ if the file is not found. If, after searching in both directories, the file still is not found, `gawk` appends the suffix ‘.awk’ to the file name and retries the file search. If ‘AWK_LIBRARY’ has no definition, a default value of ‘SYS$LIBRARY:’ is used for it.

#### B.3.2.4 Running `gawk` on OpenVMS

Command-line parsing and quoting conventions are significantly different on OpenVMS, so examples in this Web page or from other sources often need minor changes. They *are* minor though, and all `awk` programs should run correctly.

Here are a couple of trivial tests:

```
$ gawk -- "BEGIN {print ""Hello, World!""}"
$ gawk -"W" version
! could also be -"W version" or "-W version"
```

Note that uppercase and mixed-case text must be quoted.

The OpenVMS port of `gawk` includes a `DCL`-style interface in addition to the original shell-style interface (see the help entry for details). One side effect of dual command-line parsing is that if there is only a single parameter (as in the quoted program string), the command becomes ambiguous. To work around this, the normally optional -- flag is required to force Unix-style parsing rather than `DCL` parsing. If any other dash-type options (or multiple parameters such as data files to process) are present, there is no ambiguity and -- can be omitted.

The `exit` value is a Unix-style value and is encoded into an OpenVMS exit status value when the program exits.

The OpenVMS severity bits will be set based on the `exit` value. A failure is indicated by 1, and OpenVMS sets the `ERROR` status. A fatal error is indicated by 2, and OpenVMS sets the `FATAL` status. All other values will have the `SUCCESS` status. The exit value is encoded to comply with OpenVMS coding standards and will have the `C_FACILITY_NO` of `0x350000` with the constant `0xA000` added to the number shifted over by 3 bits to make room for the severity codes.

To extract the actual `gawk` exit code from the OpenVMS status, use:

```
unix_status = (vms_status .and. %x7f8) / 8
```

A C program that uses `exec()` to call `gawk` will get the original Unix-style exit value.

OpenVMS reports time values in GMT unless one of the `SYS$TIMEZONE_RULE` or `TZ` logical names is set.

The default search path, when looking for `awk` program files specified by the -f option, is `"SYS$DISK:[],AWK_LIBRARY:"`. The logical name `AWKPATH` can be used to override this default. The format of `AWKPATH` is a comma-separated list of directory specifications. When defining it, the value should be quoted so that it retains a single translation and not a multitranslation `RMS` searchlist.

This restriction also applies to running `gawk` under GNV, as redirection is always to a DCL command.

If you are redirecting data to an OpenVMS command or utility, the current implementation requires setting up an OpenVMS foreign command that runs a command file before invoking `gawk`. (This restriction may be removed in a future release of `gawk` on OpenVMS.)

Without this command file, the input data will also appear prepended to the output data.

This also allows simulating POSIX commands that are not found on OpenVMS or the use of GNV utilities.

The example below is for `gawk` redirecting data to the OpenVMS `sort` command.

```
$ sort = "@device:[dir]vms_gawk_sort.com"
```

The command file needs to be of the format in the example below.

The first line inhibits the passed input data from also showing up in the output. It must be in the format in the example.

The next line creates a foreign command that overrides the outer foreign command which prevents an infinite recursion of command files.

The next to the last command redirects `sys$input` to be `sys$command`, in order to pick up the data that is being redirected to the command.

The last line runs the actual command. It must be the last command as the data redirected from `gawk` will be read when the command file ends.

```
$!'f$verify(0,0)'
$ sort := sort
$ define/user sys$input sys$command:
$ sort sys$input: sys$output:
```

#### B.3.2.5 The OpenVMS GNV Project

The OpenVMS GNV package provides a build environment similar to POSIX with ports of a collection of open source tools. The `gawk` found in the GNV base kit is an older port. Currently, the GNV project is being reorganized to supply individual PCSI packages for each component. See https://sourceforge.net/p/gnv/wiki/InstallingGNVPackages/.

The normal build procedure for `gawk` produces a program that is suitable for use with GNV.

To be compatible and share common code with GNV projects, all OpenVMS-specific defines and prototypes for `gawk` are in the process of being moved to vms/config_vms.h. The vms directory will have missing or updated system header files and any replacement routines that will hide most of the differences between OpenVMS and Linux. This is intended to make `gawk` easier to maintain.

The file vms/gawk_build_steps.txt in the distribution documents the procedure for building an OpenVMS PCSI kit that is compatible with GNV.

### B.4 Reporting Problems and Bugs

> *There is nothing more dangerous than a bored archaeologist.*

—

Douglas Adams,

The Hitchhiker’s Guide to the Galaxy

If you have problems with `gawk` or think that you have found a bug, report it to the developers; we cannot promise to do anything, but we might well want to fix it.

#### B.4.1 Defining What Is and What Is Not A Bug

Before talking about reporting bugs, let’s define what is a bug, and what is not.

A bug is:

- When `gawk` behaves differently from what’s described in the POSIX standard, and that difference is not mentioned in this Web page as being done on purpose.
- When `gawk` behaves differently from what’s described in this Web page.
- When `gawk` behaves differently from other `awk` implementations in particular circumstances, and that behavior cannot be attributed to an additional feature in `gawk`.
- Something that is obviously wrong, such as a core dump.
- When this Web page is unclear or ambiguous about a particular feature’s behavior.

The following things are *not* bugs, and should not be reported to the bug mailing list. You can ask about them on the “help” mailing list (see Where To Send Non-bug Questions), but don’t be surprised if you get an answer of the form “that’s how `gawk` behaves and it isn’t going to change.” Here’s the list:

- Missing features, for any definition of *feature*. For example, additional built-in arithmetic functions, or additional ways to split fields or records, or anything else. The number of features that `gawk` does *not* have is by definition infinite. It cannot be all things to all people. In short, just because `gawk` doesn’t do what *you* think it should, it’s not necessarily a bug.
- Behaviors that are defined by the POSIX standard and/or for historical compatibility with Unix `awk`. Even if you happen to dislike those behaviors, they’re not going to change: changing them would break millions of existing `awk` programs.
- Behaviors that differ from how it’s done in other languages. `awk` and `gawk` stand on their own and do not have to follow the crowd. This is particularly true when the requested behavior change would break backwards compatibility. This applies also to differences in behavior between `gawk` and other language compilers and interpreters, such as wishes for more detailed descriptions of what the problem is when a syntax error is encountered.
- Documentation issues of the form “the manual doesn’t tell me how to do XYZ.” The manual is not a cookbook to solve every little problem you may have. Its purpose is to teach you how to solve your problems on your own.
- General questions and discussion about `awk` programming or why `gawk` behaves the way it does. For that use the “help” mailing list: see Where To Send Non-bug Questions.

For more information, see *Fork My Code, Please!—An Open Letter To Those of You Who Are Unhappy*, by Arnold Robbins and Chet Ramey.

| A Note About Fuzzers |
|---|
| In recent years, people have been running “fuzzers” to generate invalid `awk` programs in order to find and report (so-called) bugs in `gawk`. In general, such reports are not of much practical use. The programs they create are not realistic and the bugs found are generally from some kind of memory corruption that is fatal anyway. So, if you want to run a fuzzer against `gawk` and report the results, you may do so, but be aware that such reports don’t carry the same weight as reports of real bugs do. |

#### B.4.2 Submitting Bug Reports

Before reporting a bug, make sure you have really found a genuine bug.

Here are the steps for submitting a bug report. Following them will make both your life and the lives of the maintainers much easier.

1. Make sure that what you want to report is appropriate. See Defining What Is and What Is Not A Bug. If it’s not, you are wasting your time and ours.
2. Verify that you have the latest version of `gawk`. Many bugs (usually subtle ones) are fixed at each release, and if yours is out-of-date, the problem may already have been solved.
3. Please see if setting the environment variable `LC_ALL` to `LC_ALL=C` causes things to behave as you expect. If so, it’s a locale issue, and may or may not really be a bug.
4. Carefully reread the documentation and see if it says you can do what you’re trying to do. If it’s not clear whether you should be able to do something or not, report that too; it’s a bug in the documentation!
5. Before reporting a bug or trying to fix it yourself, try to isolate it to the smallest possible `awk` program and input data file that reproduce the problem.
6. Use the `gawkbug` program to submit the bug report. This program sets up a bug report template and opens it in your editor. You then need to edit it appropriately to include:
  - The program and data file.
  - The exact results `gawk` gave you. Also say what you expected to occur; this helps us decide whether the problem is really in the documentation.
  - A fix if you have one.
7. Do *not* send screenshots. Instead, use copy/paste to send text, or send files.
8. Please be sure to send all mail in *plain text*, not (or not exclusively) in HTML.
9. *All email must be in English. This is the only language understood in common by all the maintainers.*

The `gawkbug` program sends email to “bug dash gawk at gnu dot org”.

The `gawk` maintainers subscribe to this address, and thus they will receive your bug report. Do *not* send mail to the maintainers directly; the bug reporting address is preferred because the email list is archived at the GNU Project.

If you are using OpenVMS or the MinGW build of `gawk`, the `gawkbug` script won’t be available. Please send the previously listed information directly in an email to the bug list. Please send any test program or data files as attachments, instead of inline in the email, to avoid their being mangled by various mail systems.

> **NOTE:** Many distributions of GNU/Linux and the various BSD-based operating systems have their own bug reporting systems. If you report a bug using your distribution’s bug reporting system, you should also send a copy to “bug dash gawk at gnu dot org”.
> 
> This is for two reasons. First, although some distributions forward bug reports “upstream” to the GNU mailing list, many don’t, so there is a good chance that the `gawk` maintainers won’t even see the bug report! Second, mail to the GNU list is archived, and having everything at the GNU Project keeps things self-contained and not dependent on other organizations.

Please note: We ask that you follow the GNU Kind Communication Guidelines in your correspondence on the list (as well as off of it).

Additionally, just to be clear, on the list:

- Personal attacks (so called *ad hominem attacks*) are always inappropriate. If you make such attacks, you will be banned from the list.
- Discussion of proprietary software is strongly discouraged on GNU mailing lists. If you continue to discuss such software after being asked not to, you will also be banned.

#### B.4.3 Please Don’t Post Bug Reports to USENET

> I gave up on Usenet a couple of years ago and haven’t really looked back. It’s like sports talk radio—you feel smarter for not having read it.

—

Chet Ramey

Please do *not* try to report bugs in `gawk` by posting to the Usenet/Internet newsgroup `comp.lang.awk`. Although some of the `gawk` developers occasionally read this news group, the primary `gawk` maintainer no longer does. Thus it’s virtually guaranteed that he will *not* see your posting.

If you really don’t care about the previous paragraph and continue to post bug reports in `comp.lang.awk`, then understand that you’re not reporting bugs, you’re just whining.

Similarly, posting bug reports or questions in web forums (such as Stack Overflow) may get you an answer, but it won’t be from the `gawk` maintainers, who do not spend their time in web forums. The steps described here are the only officially recognized way for reporting bugs. Really.

#### B.4.4 What To Do If You Think There Is A Performance Issue

If you think that `gawk` is too slow at doing a particular task, you should investigate before sending in a bug report. Here are the steps to follow:

1. Run `gawk` with the --profile option (see Command-Line Options) to see what your program is doing. It may be that you have written it in an inefficient manner. For example, you may be doing something for every record that could be done just once, for every file. (Use a `BEGINFILE` rule; see The `BEGINFILE` and `ENDFILE` Special Patterns.) Or you may be doing something for every file that only needs to be done once per run of the program. (Use a `BEGIN` rule; see The `BEGIN` and `END` Special Patterns.)
2. If profiling at the `awk` level doesn’t help, then you will need to compile `gawk` itself for profiling at the C language level. To do that, start with the latest released version of `gawk`. Unpack the source code in a new directory, and configure it: $ tar -xpzvf gawk-X.Y.Z.tar.gz ... *Output omitted* $ cd gawk-X.Y.Z $ ./configure ... *Output omitted*
3. Edit the files Makefile and support/Makefile. Change every instance of -O2 or -O to -pg. This causes `gawk` to be compiled for profiling.
4. Compile the program by running the `make` command: $ make ... *Output omitted*
5. Run the freshly compiled `gawk` on a *real* program, using *real* data. Using an artificial program to try to time one particular feature of `gawk` is useless; real `awk` programs generally spend most of their time doing I/O, not computing. If you want to prove that something is slow, it *must* be done using a real program and real data. Use a data file that is large enough for the statistical profiling to measure where `gawk` spends its time. It should be at least 100 megabytes in size. $ ./gawk -f realprogram.awk realdata > /dev/null
6. When done, you should have a file in the current directory named gmon.out. Run the command ‘gprof gawk gmon.out > gprof.out’.
7. Submit a bug report explaining what you think is slow. Include the gprof.out file with it. Preferably, you should also submit the program and the data, or else indicate where to get the data if the file is large.
8. If you have not submitted your program and data, be prepared to apply patches and rerun the profiling in order to see if the patches were effective.

If you are incapable or unwilling to do the steps listed above, then you will just have to live with `gawk` as it is.

#### B.4.5 Where To Send Non-bug Questions

If you have questions related to `awk` programming, or why `gawk` behaves a certain way, or any other `awk`- or `gawk`-related issue, please *do not* send it to the bug reporting address.

As of July, 2021, there is a separate mailing list for this purpose: “help dash gawk at gnu dot org”. Anything that is not a bug report should be sent to that list.

> **NOTE:** If you disregard these directions and send non-bug mails to the bug list, you will be told to use the help list. After two such requests you will be silently *blacklisted* from the bug list.

Please note: As with the bug list, we ask that you follow the GNU Kind Communication Guidelines in your correspondence on the help list (as well as off of it).

If you wish to the subscribe to the list, in order to help out others, or to learn from others, here are instructions, courtesy of Bob Proulx:

***Subscribe by email***

Send an email message to “help dash gawk dash request at gnu dot org” with “subscribe” in the body of the message. The subject does not matter and is not used.

***Subscribe by web form***

To use the web interface visit the list information page. Use the subscribe form to fill out your email address and submit using the `Subscribe` button.

***Reply to the confirmation message***

In both cases then reply to the confirmation message that is sent to your address in reply.

Bob mentions that you may also use email for subscribing and unsubscribing. For example:

```
$ echo help | mailx -s request help-gawk-request@gnu.org
$ echo subscribe | mailx -s request help-gawk-request@gnu.org
$ echo unsubscribe | mailx -s request help-gawk-request@gnu.org
```

#### B.4.6 Reporting Problems with Non-Unix Ports

If you find bugs in one of the non-Unix ports of `gawk`, send an email to the bug list, with a copy to the person who maintains that port. The maintainers are named in the following list, as well as in the README file in the `gawk` distribution. Information in the README file should be considered authoritative if it conflicts with this Web page.

The people maintaining the various `gawk` ports are:

| Unix and POSIX systems | Arnold Robbins, “arnold at skeeve dot com” |
|---|---|
| MS-Windows with MinGW | Eli Zaretskii, “eliz at gnu dot org” |
| OpenVMS | John Malmberg, “wb8tyw at qsl dot net” |
| z/OS (OS/390) | Daniel Richard G. “skunk at iSKUNK dot ORG” |

If your bug is also reproducible under Unix, send a copy of your report to the “bug dash gawk at gnu dot org” email list as well.

### B.5 Other Freely Available `awk` Implementations

> *Implementation is the sincerest form of flattery.*

—

L. Peter Deutsch

> *It’s kind of fun to put comments like this in your awk code:*       `// Do C++ comments work? answer: yes! of course`

—

Michael Brennan

There are a number of other freely available `awk` implementations. This section briefly describes where to get them.

The following programs are all written in C:

**Unix `awk`**

Brian Kernighan, one of the original designers of Unix `awk`, has made his implementation of `awk` freely available. You can retrieve it from GitHub:

```
git clone https://github.com/onetrueawk/awk bwkawk
```

This command creates a copy of the Git repository in a directory named bwkawk. If you omit the last argument from the `git` command line, the repository copy is created in a directory named awk.

To build it, review the settings in the makefile, and then just run `make`. Note that the result of compilation is named `a.out`; you will have to rename it to something reasonable.

See Common Extensions Summary for a list of extensions in this `awk` that are not in POSIX `awk`.

In 2023, Brian Kernighan, along with Al Aho and Peter Weinberger, published a second edition of their book on `awk`. Professor Kernighan also maintains a companion web site for the book. A copy of all the book’s programs are available there for download.

As a side note, Dan Bornstein has created a Git repository tracking all the versions of BWK `awk` that he could find. It’s available at https://github.com/danfuzz/one-true-awk.

**`mawk`**

Michael Brennan wrote an independent implementation of `awk`, called `mawk`. It is available under the GPL (see GNU General Public License), just as `gawk` is.

The original distribution site for the `mawk` source code no longer has it. A copy is available at https://www.skeeve.com/gawk/mawk1.3.3.tar.gz.

In 2009, Thomas Dickey took on `mawk` maintenance. Basic information is available on the project’s web page. The download URL is https://invisible-island.net/datafiles/release/mawk.tar.gz.

Once you have it, `gunzip` may be used to decompress this file. Installation is similar to `gawk`’s (see Compiling and Installing `gawk` on Unix-Like Systems).

See Common Extensions Summary for a list of extensions in `mawk` that are not in POSIX `awk`.

**`mawk` 2.0**

In 2016, Michael Brennan resumed `mawk` development. His development snapshots are available via Git from the project’s GitHub page.

**`awka`**

Written by Andrew Sumner, `awka` translates `awk` programs into C, compiles them, and links them with a library of functions that provide the core `awk` functionality. It also has a number of extensions.

Both the `awk` translator and the library are released under the GPL.

To get `awka`, go to https://sourceforge.net/projects/awka.

The project is frozen; no new code changes have been made since approximately 2001.

**Revive Awka**

This project, available at https://github.com/noyesno/awka, intends to fix bugs in `awka` and add more features.

This project also seems to be frozen; no new code changes have been made since approximately 2021.

**`pawk`**

Nelson H.F. Beebe at the University of Utah has modified BWK `awk` to provide timing and profiling information. It is different from `gawk` with the --profile option (see Profiling Your `awk` Programs) in that it uses CPU-based profiling, not line-count profiling. You may find it at either ftp://ftp.math.utah.edu/pub/pawk/pawk-20030606.tar.gz or https://www.math.utah.edu/pub/pawk/pawk-20030606.tar.gz.

**BusyBox `awk` ¶**

BusyBox is a GPL-licensed program providing small versions of many applications within a single executable. It is aimed at embedded systems. It includes a full implementation of POSIX `awk`. When building it, be careful not to do ‘make install’ as it will overwrite copies of other applications in your /usr/local/bin. For more information, see the project’s home page.

**The OpenSolaris POSIX `awk`**

The versions of `awk` in /usr/xpg4/bin and /usr/xpg6/bin on Solaris are more or less POSIX-compliant. They are based on the `awk` from Mortice Kern Systems for PCs. We were able to make this code compile and work under GNU/Linux with 1–2 hours of work. Making it more generally portable (using GNU Autoconf and/or Automake) would take more work, and this has not been done, at least to our knowledge.

The source code used to be available from the OpenSolaris website. However, that project was ended and the website shut down. Fortunately, the Illumos project makes this implementation available. You can view the files one at a time from https://github.com/joyent/illumos-joyent/blob/master/usr/src/cmd/awk_xpg4.

**Libmawk ¶**

This is an embeddable `awk` interpreter derived from `mawk`. For more information, see http://repo.hu/projects/libmawk/.

**Mircea Neacsu’s Embeddable `awk` ¶**

Mircea Neacsu has created an embeddable `awk` interpreter, based on BWK awk. It’s available at https://github.com/neacsum/awk. A short overview of how to use it may be found at https://www.codeproject.com/Articles/5264205/Embedding-AWK-in-a-C-program.

**`awkcc` ¶**

This is an early adaptation of Unix `awk` that translates `awk` into C code. It was done by J. Christopher Ramming at Bell Labs, circa 1988. It’s available at https://github.com/nokia/awkcc. Bringing this up to date would be an interesting software engineering exercise.

**QSE `awk` ¶**

This is an embeddable `awk` interpreter. For more information, see https://code.google.com/p/qse/. The source can be found at https://code.google.com/archive/p/qse/source/default/source.

**`wak` ¶**

`wak` (a permutation of the letters in `awk`) is a small, mostly POSIX compatible version of `awk` written in C by Ray Gardner. The source code is available from its Github repository. Some nice articles about its development may be found in the author’s weblog.

The following implementations are written in Go:

**`goawk`**

This is an `awk` interpreter written in the Go programming language. It implements POSIX `awk`, with a few minor extensions. Source code is available from https://github.com/benhoyt/goawk. The author wrote a nice article describing the implementation.

**`AWKgo`**

This is an `awk` to Go translator. It was written by the author of `goawk`. (See the previous entry in this list.) Source code is available from https://github.com/benhoyt/goawk/tree/master/awkgo. The author’s article about it is at https://benhoyt.com/writings/awkgo/.

The following implementations are written in Java:

**`jawk`**

This is an interpreter for `awk` written in Java. It claims to be a full interpreter, although because it uses Java facilities for I/O and for regexp matching, the language it supports is different from POSIX `awk`. More information is available on the project’s home page.

**Hoijui’s `jawk`**

This project, available at https://github.com/hoijui/Jawk, is another `awk` interpreter written in Java. It uses modern Java build tools.

This version is written in Python:

**`pawk` ¶**

This is a Python module that claims to bring `awk`-like features to Python. See https://github.com/alecthomas/pawk for more information. (This is not related to Nelson Beebe’s modified version of BWK `awk`, described earlier.)

There are several versions written in Rust:

**`rust-awk`**

This program implements a small subset of `awk` in Rust. Many features are missing. The code is available at https://github.com/wenley/rust-awk.

**`frawk`**

This is a language for writing short programs. “To a first approximation, it is an implementation of the AWK language; many common `awk` programs produce equivalent output when passed to `frawk`.” However, it has a number of important additional features. The code is available at https://github.com/ezrosent/frawk.

**`zawk`**

This program is based off of `frawk`. The code is available at https://crates.io/crates/zawk.

**`awk-rs`**

This program simply claims to be “`awk` written in rust.” It seems to be frozen, with no updates since 2020. The code is available at https://github.com/conradludgate/awk-rs.

**`awk-rs`**

This program seems to be the most complete and actively maintained of the versions written in Rust. It used to be named `rawk` but is now called `awk-rs`. It seems to be different from the other version with the same name. The code is available at https://github.com/pegasusheavy/rawk.

This version is written in Zig:

**`dawk` ¶**

An implementation of `awk` in the Zig programming language. See https://codeberg.org/triallax/dawk.

And finally, this tool is written in shell:

**`cppawk` ¶**

Quoting from the web page, “`cppawk` is a tiny shell script that is used like `awk`. It invokes the C preprocessor (GNU `cpp`) on the Awk code and calls Awk on the result.” This program may be of use if the way `gawk`’s `@include` facility works doesn’t suit your needs. For more information, see https://www.kylheku.com/cgit/cppawk/.

See also the “Versions and implementations” section of the Wikipedia article on `awk` for information on additional versions.

An interesting collection of library functions is available at https://github.com/e36freak/awk-libs.

An interesting collection of `gawk` extensions is available https://github.com/su8/gawk-extensions.

### B.6 Summary

- The `gawk` distribution is available from the GNU Project’s main distribution site, `ftp.gnu.org`. The canonical build recipe is: wget https://ftp.gnu.org/gnu/gawk/gawk-5.4.0.tar.gz tar -xvpzf gawk-5.4.0.tar.gz cd gawk-5.4.0 ./configure && make && make check **NOTE:** Because of the ‘https://’ URL, you may have to supply the --no-check-certificate option to `wget` to download the file.
- `gawk` may be built on non-POSIX systems as well. The currently supported systems are MS-Windows using MSYS, MSYS2, MinGW, and Cygwin, and OpenVMS. Instructions for each system are included in this appendix.
- Bug reports should be sent via email to “bug dash gawk at gnu dot org”. Bug reports should be in English and should include the version of `gawk`, how it was compiled, and a short program and data file that demonstrate the problem.
- Non-bug emails should be sent to “help dash gawk at gnu dot org”. Repeatedly sending non-bug emails to the bug list will get you blacklisted from it.
- There are a number of other freely available `awk` implementations. Many are POSIX-compliant; others are less so.

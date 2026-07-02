---
title: "GNU make (part 15/17)"
source: https://www.gnu.org/software/make/manual/make.html
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
part: 15/17
---

## Appendix A Quick Reference

This appendix summarizes the directives, text manipulation functions, and special variables which GNU `make` understands. See Special Built-in Target Names, Catalogue of Built-In Rules, and Summary of Options, for other summaries.

Here is a summary of the directives GNU `make` recognizes:

**`define *variable*`**

**`define *variable* =`**

**`define *variable* :=`**

**`define *variable* ::=`**

**`define *variable* :::=`**

**`define *variable* +=`**

**`define *variable* ?=`**

**`endef`**

Define multi-line variables. See Defining Multi-Line Variables.

**`undefine *variable*`**

Undefining variables. See Undefining Variables.

**`ifdef *variable*`**

**`ifndef *variable*`**

**`ifeq (*a*,*b*)`**

**`ifeq "*a*" "*b*"`**

**`ifeq '*a*' '*b*'`**

**`ifneq (*a*,*b*)`**

**`ifneq "*a*" "*b*"`**

**`ifneq '*a*' '*b*'`**

**`else`**

**`endif`**

Conditionally evaluate part of the makefile. See Conditional Parts of Makefiles.

**`include *file*`**

**`-include *file*`**

**`sinclude *file*`**

Include another makefile. See Including Other Makefiles.

**`override *variable-assignment*`**

Define a variable, overriding any previous definition, even one from the command line. See The `override` Directive.

**`export`**

Tell `make` to export all variables to child processes by default. See Communicating Variables to a Sub-`make`.

**`export *variable*`**

**`export *variable-assignment*`**

**`unexport *variable*`**

Tell `make` whether or not to export a particular variable to child processes. See Communicating Variables to a Sub-`make`.

**`private *variable-assignment*`**

Do not allow this variable assignment to be inherited by prerequisites. See Suppressing Inheritance.

**`vpath *pattern* *path*`**

Specify a search path for files matching a ‘%’ pattern. See The `vpath` Directive.

**`vpath *pattern*`**

Remove all search paths previously specified for *pattern*.

**`vpath`**

Remove all search paths previously specified in any `vpath` directive.

Here is a summary of the built-in functions (see Functions for Transforming Text):

**`$(subst *from*,*to*,*text*)`**

Replace *from* with *to* in *text*. See Functions for String Substitution and Analysis.

**`$(patsubst *pattern*,*replacement*,*text*)`**

Replace words matching *pattern* with *replacement* in *text*. See Functions for String Substitution and Analysis.

**`$(strip *string*)`**

Remove excess whitespace characters from *string*. See Functions for String Substitution and Analysis.

**`$(findstring *find*,*text*)`**

Locate *find* in *text*. See Functions for String Substitution and Analysis.

**`$(filter *pattern*…,*text*)`**

Select words in *text* that match one of the *pattern* words. See Functions for String Substitution and Analysis.

**`$(filter-out *pattern*…,*text*)`**

Select words in *text* that *do not* match any of the *pattern* words. See Functions for String Substitution and Analysis.

**`$(sort *list*)`**

Sort the words in *list* lexicographically, removing duplicates. See Functions for String Substitution and Analysis.

**`$(word *n*,*text*)`**

Extract the *n*th word (one-origin) of *text*. See Functions for String Substitution and Analysis.

**`$(words *text*)`**

Count the number of words in *text*. See Functions for String Substitution and Analysis.

**`$(wordlist *s*,*e*,*text*)`**

Returns the list of words in *text* from *s* to *e*. See Functions for String Substitution and Analysis.

**`$(firstword *names*…)`**

Extract the first word of *names*. See Functions for String Substitution and Analysis.

**`$(lastword *names*…)`**

Extract the last word of *names*. See Functions for String Substitution and Analysis.

**`$(dir *names*…)`**

Extract the directory part of each file name. See Functions for File Names.

**`$(notdir *names*…)`**

Extract the non-directory part of each file name. See Functions for File Names.

**`$(suffix *names*…)`**

Extract the suffix (the last ‘.’ and following characters) of each file name. See Functions for File Names.

**`$(basename *names*…)`**

Extract the base name (name without suffix) of each file name. See Functions for File Names.

**`$(addsuffix *suffix*,*names*…)`**

Append *suffix* to each word in *names*. See Functions for File Names.

**`$(addprefix *prefix*,*names*…)`**

Prepend *prefix* to each word in *names*. See Functions for File Names.

**`$(join *list1*,*list2*)`**

Join two parallel lists of words. See Functions for File Names.

**`$(wildcard *pattern*…)`**

Find file names matching a shell file name pattern (*not* a ‘%’ pattern). See The Function `wildcard`.

**`$(realpath *names*…)`**

For each file name in *names*, expand to an absolute name that does not contain any `.`, `..`, nor symlinks. See Functions for File Names.

**`$(abspath *names*…)`**

For each file name in *names*, expand to an absolute name that does not contain any `.` or `..` components, but preserves symlinks. See Functions for File Names.

**`$(error *text*…)`**

When this function is evaluated, `make` generates a fatal error with the message *text*. See Functions That Control Make.

**`$(warning *text*…)`**

When this function is evaluated, `make` generates a warning with the message *text*. See Functions That Control Make.

**`$(shell *command*)`**

Execute a shell command and return its output. See The `shell` Function.

**`$(origin *variable*)`**

Return a string describing how the `make` variable *variable* was defined. See The `origin` Function.

**`$(flavor *variable*)`**

Return a string describing the flavor of the `make` variable *variable*. See The `flavor` Function.

**`$(let *var* [*var* ...],*words*,*text*)`**

Evaluate *text* with the *var*s bound to the words in *words*. See The `let` Function.

**`$(foreach *var*,*words*,*text*)`**

Evaluate *text* with *var* bound to each word in *words*, and concatenate the results. See The `foreach` Function.

**`$(if *condition*,*then-part*[,*else-part*])`**

Evaluate the condition *condition*; if it’s non-empty substitute the expansion of the *then-part* otherwise substitute the expansion of the *else-part*. See Functions for Conditionals.

**`$(or *condition1*[,*condition2*[,*condition3*…]])`**

Evaluate each condition *conditionN* one at a time; substitute the first non-empty expansion. If all expansions are empty, substitute the empty string. See Functions for Conditionals.

**`$(and *condition1*[,*condition2*[,*condition3*…]])`**

Evaluate each condition *conditionN* one at a time; if any expansion results in the empty string substitute the empty string. If all expansions result in a non-empty string, substitute the expansion of the last *condition*. See Functions for Conditionals.

**`$(intcmp *lhs*,*rhs*[,*lt-part*[,*eq-part*[,*gt-part*]]])`**

Compare *lhs* and *rhs* numerically; substitute the expansion of *lt-part*, *eq-part*, or *gt-part* depending on whether the left-hand side is less-than, equal-to, or greater-than the right-hand side, respectively. See Functions for Conditionals.

**`$(call *var*,*param*,…)`**

Evaluate the variable *var* replacing any references to `$(1)`, `$(2)` with the first, second, etc. *param* values. See The `call` Function.

**`$(eval *text*)`**

Evaluate *text* then read the results as makefile commands. Expands to the empty string. See The `eval` Function.

**`$(file *op* *filename*,*text*)`**

Expand the arguments, then open the file *filename* using mode *op* and write *text* to that file. See The `file` Function.

**`$(value *var*)`**

Evaluates to the contents of the variable *var*, with no expansion performed on it. See The `value` Function.

Here is a summary of the automatic variables. See Automatic Variables, for full information.

**`$@`**

The file name of the target.

**`$%`**

The target member name, when the target is an archive member.

**`$<`**

The name of the first prerequisite.

**`$?`**

The names of all the prerequisites that are newer than the target, with spaces between them. For prerequisites which are archive members, only the named member is used (see Using `make` to Update Archive Files).

**`$^`**

**`$+`**

The names of all the prerequisites, with spaces between them. For prerequisites which are archive members, only the named member is used (see Using `make` to Update Archive Files). The value of `$^` omits duplicate prerequisites, while `$+` retains them and preserves their order.

**`$*`**

The stem with which an implicit rule matches (see How Patterns Match).

**`$(@D)`**

**`$(@F)`**

The directory part and the file-within-directory part of `$@`.

**`$(*D)`**

**`$(*F)`**

The directory part and the file-within-directory part of `$*`.

**`$(%D)`**

**`$(%F)`**

The directory part and the file-within-directory part of `$%`.

**`$(<D)`**

**`$(<F)`**

The directory part and the file-within-directory part of `$<`.

**`$(^D)`**

**`$(^F)`**

The directory part and the file-within-directory part of `$^`.

**`$(+D)`**

**`$(+F)`**

The directory part and the file-within-directory part of `$+`.

**`$(?D)`**

**`$(?F)`**

The directory part and the file-within-directory part of `$?`.

These variables are used specially by GNU `make`:

**`MAKEFILES`**

Makefiles to be read on every invocation of `make`. See The Variable `MAKEFILES`.

**`VPATH`**

Directory search path for files not found in the current directory. See `VPATH` Search Path for All Prerequisites.

**`SHELL`**

The name of the system default command interpreter, usually /bin/sh. You can set `SHELL` in the makefile to change the shell used to run recipes. See Recipe Execution. The `SHELL` variable is handled specially when importing from and exporting to the environment. See Choosing the Shell.

**`MAKESHELL`**

On MS-DOS only, the name of the command interpreter that is to be used by `make`. This value takes precedence over the value of `SHELL`. See MAKESHELL variable.

**`MAKE`**

The name with which `make` was invoked. Using this variable in recipes has special meaning. See How the `MAKE` Variable Works.

**`MAKE_VERSION`**

The built-in variable ‘MAKE_VERSION’ expands to the version number of the GNU `make` program.

**`MAKE_HOST`**

The built-in variable ‘MAKE_HOST’ expands to a string representing the host that GNU `make` was built to run on.

**`MAKELEVEL`**

The number of levels of recursion (sub-`make`s). See Communicating Variables to a Sub-`make`.

**`MAKEFLAGS`**

The flags given to `make`. You can set this in the environment or a makefile to set flags. See Communicating Options to a Sub-`make`.

It is *never* appropriate to use `MAKEFLAGS` directly in a recipe line: its contents may not be quoted correctly for use in the shell. Always allow recursive `make`’s to obtain these values through the environment from its parent.

**`GNUMAKEFLAGS`**

Other flags parsed by `make`. You can set this in the environment or a makefile to set `make` command-line flags. GNU `make` never sets this variable itself. This variable is only needed if you’d like to set GNU `make`-specific flags in a POSIX-compliant makefile. This variable will be seen by GNU `make` and ignored by other `make` implementations. It’s not needed if you only use GNU `make`; just use `MAKEFLAGS` directly. See Communicating Options to a Sub-`make`.

**`MAKECMDGOALS`**

The targets given to `make` on the command line. Setting this variable has no effect on the operation of `make`. See Arguments to Specify the Goals.

**`CURDIR`**

Set to the absolute pathname of the current working directory (after all `-C` options are processed, if any). Setting this variable has no effect on the operation of `make`. See Recursive Use of `make`.

**`SUFFIXES`**

The default list of suffixes before `make` reads any makefiles.

**`.LIBPATTERNS`**

Defines the naming of the libraries `make` searches for, and their order. See Directory Search for Link Libraries.

Next: Complex Makefile Example, Previous: Quick Reference, Up: GNU `make`   [Contents][Index]


## Appendix B Errors Generated by Make

Here is a list of the more common errors you might see generated by `make`, and some information about what they mean and how to fix them.

Sometimes `make` errors are not fatal, especially in the presence of a `-` prefix on a recipe line, or the `-k` command line option. Errors that are fatal are prefixed with the string `***`.

Error messages are all either prefixed with the name of the program (usually ‘make’), or, if the error is found in a makefile, the name of the file and line number containing the problem.

In the table below, these common prefixes are left off.

**‘[*foo*] Error *NN*’**

**‘[*foo*] *signal description*’**

These errors are not really `make` errors at all. They mean that a program that `make` invoked as part of a recipe returned a non-0 error code (‘Error *NN*’), which `make` interprets as failure, or it exited in some other abnormal fashion (with a signal of some type). See Errors in Recipes.

If no `***` is attached to the message, then the sub-process failed but the rule in the makefile was prefixed with the `-` special character, so `make` ignored the error.

**‘missing separator. Stop.’**

**‘missing separator (did you mean TAB instead of 8 spaces?). Stop.’**

This means that `make` could not understand much of anything about the makefile line it just read. GNU `make` looks for various separators (`:`, `=`, recipe prefix characters, etc.) to indicate what kind of line it’s parsing. This message means it couldn’t find a valid one.

One of the most common reasons for this message is that you (or perhaps your oh-so-helpful editor, as is the case with many MS-Windows editors) have attempted to indent your recipe lines with spaces instead of a tab character. In this case, `make` will use the second form of the error above. Remember that every line in the recipe must begin with a tab character (unless you set `.RECIPEPREFIX`; see Other Special Variables). Eight spaces do not count. See Rule Syntax.

**‘recipe commences before first target. Stop.’**

**‘missing rule before recipe. Stop.’**

This means the first thing in the makefile seems to be part of a recipe: it begins with a recipe prefix character and doesn’t appear to be a legal `make` directive (such as a variable assignment). Recipes must always be associated with a target.

The second form is generated if the line has a semicolon as the first non-whitespace character; `make` interprets this to mean you left out the "target: prerequisite" section of a rule. See Rule Syntax.

**‘No rule to make target `*xxx*'.’**

**‘No rule to make target `*xxx*', needed by `*yyy*'.’**

This means that `make` decided it needed to build a target, but then couldn’t find any instructions in the makefile on how to do that, either explicit or implicit (including in the default rules database).

If you want that file to be built, you will need to add a rule to your makefile describing how that target can be built. Other possible sources of this problem are typos in the makefile (if that file name is wrong) or a corrupted source tree (if that file is not supposed to be built, but rather only a prerequisite).

**‘No targets specified and no makefile found. Stop.’**

**‘No targets. Stop.’**

The former means that you didn’t provide any targets to be built on the command line, and `make` couldn’t find any makefiles to read in. The latter means that some makefile was found, but it didn’t contain any default goal and none was given on the command line. GNU `make` has nothing to do in these situations. See Arguments to Specify the Makefile.

**‘Makefile `*xxx*' was not found.’**

**‘Included makefile `*xxx*' was not found.’**

A makefile specified on the command line (first form) or included (second form) was not found.

**‘warning: overriding recipe for target `*xxx*'’**

**‘warning: ignoring old recipe for target `*xxx*'’**

GNU `make` allows only one recipe to be specified per target (except for double-colon rules). If you give a recipe for a target which already has been defined to have one, this warning is issued and the second recipe will overwrite the first. See Multiple Rules for One Target.

**‘Circular *xxx* <- *yyy* dependency dropped.’**

This means that `make` detected a loop in the dependency graph: after tracing the prerequisite *yyy* of target *xxx*, and its prerequisites, etc., one of them depended on *xxx* again.

**‘Recursive variable `*xxx*' references itself (eventually). Stop.’**

This means you’ve defined a normal (recursive) `make` variable *xxx* that, when it’s expanded, will refer to itself (*xxx*). This is not allowed; either use simply-expanded variables (‘:=’ or ‘::=’) or use the append operator (‘+=’). See How to Use Variables.

**‘Unterminated variable reference. Stop.’**

This means you forgot to provide the proper closing parenthesis or brace in your variable or function reference.

**‘insufficient arguments to function `*xxx*'. Stop.’**

This means you haven’t provided the requisite number of arguments for this function. See the documentation of the function for a description of its arguments. See Functions for Transforming Text.

**‘missing target pattern. Stop.’**

**‘multiple target patterns. Stop.’**

**‘target pattern contains no `%'. Stop.’**

**‘mixed implicit and static pattern rules. Stop.’**

These errors are generated for malformed static pattern rules (see Syntax of Static Pattern Rules). The first means the target-pattern part of the rule is empty; the second means there are multiple pattern characters (`%`) in the target-pattern part; the third means there are no pattern characters in the target-pattern part; and the fourth means that all three parts of the static pattern rule contain pattern characters (`%`)–the first part should not contain pattern characters.

If you see these errors and you aren’t trying to create a static pattern rule, check the value of any variables in your target and prerequisite lists to be sure they do not contain colons.

**‘warning: -jN forced in submake: disabling jobserver mode.’**

This warning and the next are generated if `make` detects error conditions related to parallel processing on systems where sub-`make`s can communicate (see Communicating Options to a Sub-`make`). This warning is generated if a recursive invocation of a `make` process is forced to have ‘-j*N*’ in its argument list (where *N* is greater than one). This could happen, for example, if you set the `MAKE` environment variable to ‘make -j2’. In this case, the sub-`make` doesn’t communicate with other `make` processes and will simply pretend it has two jobs of its own.

**‘warning: jobserver unavailable: using -j1. Add `+' to parent make rule.’**

In order for `make` processes to communicate, the parent will pass information to the child. Since this could result in problems if the child process isn’t actually a `make`, the parent will only do this if it thinks the child is a `make`. The parent uses the normal algorithms to determine this (see How the `MAKE` Variable Works). If the makefile is constructed such that the parent doesn’t know the child is a `make` process, then the child will receive only part of the information necessary. In this case, the child will generate this warning message and proceed with its build in a sequential manner.

**‘warning: ignoring prerequisites on suffix rule definition’**

According to POSIX, a suffix rule cannot contain prerequisites. If a rule that could be a suffix rule has prerequisites it is interpreted as a simple explicit rule, with an odd target name. This requirement is obeyed when POSIX-conforming mode is enabled (the `.POSIX` target is defined). In versions of GNU `make` prior to 4.3, no warning was emitted and a suffix rule was created, however all prerequisites were ignored and were not part of the suffix rule. Starting with GNU `make` 4.3 the behavior is the same, and in addition this warning is generated. In a future version the POSIX-conforming behavior will be the only behavior: no rule with a prerequisite can be suffix rule and this warning will be removed.

Next: GNU Free Documentation License, Previous: Errors Generated by Make, Up: GNU `make`   [Contents][Index]


## Appendix C Complex Makefile Example

Here is the makefile for the GNU `tar` program. This is a moderately complex makefile. The first line uses a `#!` setting to allow the makefile to be executed directly.

Because it is the first target, the default goal is ‘all’. An interesting feature of this makefile is that testpad.h is a source file automatically created by the `testpad` program, itself compiled from testpad.c.

If you type ‘make’ or ‘make all’, then `make` creates the tar executable, the rmt daemon that provides remote tape access, and the tar.info Info file.

If you type ‘make install’, then `make` not only creates tar, rmt, and tar.info, but also installs them.

If you type ‘make clean’, then `make` removes the ‘.o’ files, and the tar, rmt, testpad, testpad.h, and core files.

If you type ‘make distclean’, then `make` not only removes the same files as does ‘make clean’ but also the TAGS, Makefile, and config.status files. (Although it is not evident, this makefile (and config.status) is generated by the user with the `configure` program, which is provided in the `tar` distribution, but is not shown here.)

If you type ‘make realclean’, then `make` removes the same files as does ‘make distclean’ and also removes the Info files generated from tar.texinfo.

In addition, there are targets `shar` and `dist` that create distribution kits.

```
#!/usr/bin/make -f
# Generated automatically from Makefile.in by configure.
# Un*x Makefile for GNU tar program.
# Copyright (C) 1991 Free Software Foundation, Inc.
```

```
# This program is free software; you can redistribute
# it and/or modify it under the terms of the GNU
# General Public License …
…
…
```

```
SHELL = /bin/sh

#### Start of system configuration section. ####

srcdir = .
```

```
# If you use gcc, you should either run the
# fixincludes script that comes with it or else use
# gcc with the -traditional option.  Otherwise ioctl
# calls will be compiled incorrectly on some systems.
CC = gcc -O
YACC = bison -y
INSTALL = /usr/local/bin/install -c
INSTALLDATA = /usr/local/bin/install -c -m 644
```

```
# Things you might add to DEFS:
# -DSTDC_HEADERS        If you have ANSI C headers and
#                       libraries.
# -DPOSIX               If you have POSIX.1 headers and
#                       libraries.
# -DBSD42               If you have sys/dir.h (unless
#                       you use -DPOSIX), sys/file.h,
#                       and st_blocks in `struct stat'.
# -DUSG                 If you have System V/ANSI C
#                       string and memory functions
#                       and headers, sys/sysmacros.h,
#                       fcntl.h, getcwd, no valloc,
#                       and ndir.h (unless
#                       you use -DDIRENT).
# -DNO_MEMORY_H         If USG or STDC_HEADERS but do not
#                       include memory.h.
# -DDIRENT              If USG and you have dirent.h
#                       instead of ndir.h.
# -DSIGTYPE=int         If your signal handlers
#                       return int, not void.
# -DNO_MTIO             If you lack sys/mtio.h
#                       (magtape ioctls).
# -DNO_REMOTE           If you do not have a remote shell
#                       or rexec.
# -DUSE_REXEC           To use rexec for remote tape
#                       operations instead of
#                       forking rsh or remsh.
# -DVPRINTF_MISSING     If you lack vprintf function
#                       (but have _doprnt).
# -DDOPRNT_MISSING      If you lack _doprnt function.
#                       Also need to define
#                       -DVPRINTF_MISSING.
# -DFTIME_MISSING       If you lack ftime system call.
# -DSTRSTR_MISSING      If you lack strstr function.
# -DVALLOC_MISSING      If you lack valloc function.
# -DMKDIR_MISSING       If you lack mkdir and
#                       rmdir system calls.
# -DRENAME_MISSING      If you lack rename system call.
# -DFTRUNCATE_MISSING   If you lack ftruncate
#                       system call.
# -DV7                  On Version 7 Unix (not
#                       tested in a long time).
# -DEMUL_OPEN3          If you lack a 3-argument version
#                       of open, and want to emulate it
#                       with system calls you do have.
# -DNO_OPEN3            If you lack the 3-argument open
#                       and want to disable the tar -k
#                       option instead of emulating open.
# -DXENIX               If you have sys/inode.h
#                       and need it 94 to be included.

DEFS =  -DSIGTYPE=int -DDIRENT -DSTRSTR_MISSING \
        -DVPRINTF_MISSING -DBSD42
# Set this to rtapelib.o unless you defined NO_REMOTE,
# in which case make it empty.
RTAPELIB = rtapelib.o
LIBS =
DEF_AR_FILE = /dev/rmt8
DEFBLOCKING = 20
```

```
CDEBUG = -g
CFLAGS = $(CDEBUG) -I. -I$(srcdir) $(DEFS) \
        -DDEF_AR_FILE=\"$(DEF_AR_FILE)\" \
        -DDEFBLOCKING=$(DEFBLOCKING)
LDFLAGS = -g
```

```
prefix = /usr/local
# Prefix for each installed program,
# normally empty or `g'.
binprefix =

# The directory to install tar in.
bindir = $(prefix)/bin

# The directory to install the info files in.
infodir = $(prefix)/info
```

```
#### End of system configuration section. ####
```

```
SRCS_C  = tar.c create.c extract.c buffer.c   \
          getoldopt.c update.c gnu.c mangle.c \
          version.c list.c names.c diffarch.c \
          port.c wildmat.c getopt.c getopt1.c \
          regex.c
SRCS_Y  = getdate.y
SRCS    = $(SRCS_C) $(SRCS_Y)
OBJS    = $(SRCS_C:.c=.o) $(SRCS_Y:.y=.o) $(RTAPELIB)
```

```
AUX =   README COPYING ChangeLog Makefile.in  \
        makefile.pc configure configure.in \
        tar.texinfo tar.info* texinfo.tex \
        tar.h port.h open3.h getopt.h regex.h \
        rmt.h rmt.c rtapelib.c alloca.c \
        msd_dir.h msd_dir.c tcexparg.c \
        level-0 level-1 backup-specs testpad.c
```

```
.PHONY: all
all:    tar rmt tar.info
```

```
tar:    $(OBJS)
        $(CC) $(LDFLAGS) -o $@ $(OBJS) $(LIBS)
```

```
rmt:    rmt.c
        $(CC) $(CFLAGS) $(LDFLAGS) -o $@ rmt.c
```

```
tar.info: tar.texinfo
        makeinfo tar.texinfo
```

```
.PHONY: install
install: all
        $(INSTALL) tar $(bindir)/$(binprefix)tar
        -test ! -f rmt || $(INSTALL) rmt /etc/rmt
        $(INSTALLDATA) $(srcdir)/tar.info* $(infodir)
```

```
$(OBJS): tar.h port.h testpad.h
regex.o buffer.o tar.o: regex.h
# getdate.y has 8 shift/reduce conflicts.
```

```
testpad.h: testpad
        ./testpad
```

```
testpad: testpad.o
        $(CC) -o $@ testpad.o
```

```
TAGS:   $(SRCS)
        etags $(SRCS)
```

```
.PHONY: clean
clean:
        rm -f *.o tar rmt testpad testpad.h core
```

```
.PHONY: distclean
distclean: clean
        rm -f TAGS Makefile config.status
```

```
.PHONY: realclean
realclean: distclean
        rm -f tar.info*
```

```
.PHONY: shar
shar: $(SRCS) $(AUX)
        shar $(SRCS) $(AUX) | compress \
          > tar-`sed -e '/version_string/!d' \
                     -e 's/[^0-9.]*\([0-9.]*\).*/\1/' \
                     -e q
                     version.c`.shar.Z
```

```
.PHONY: dist
dist: $(SRCS) $(AUX)
        echo tar-`sed \
             -e '/version_string/!d' \
             -e 's/[^0-9.]*\([0-9.]*\).*/\1/' \
             -e q
             version.c` > .fname
        -rm -rf `cat .fname`
        mkdir `cat .fname`
        ln $(SRCS) $(AUX) `cat .fname`
        tar chZf `cat .fname`.tar.Z `cat .fname`
        -rm -rf `cat .fname` .fname
```

```
tar.zoo: $(SRCS) $(AUX)
        -rm -rf tmp.dir
        -mkdir tmp.dir
        -rm tar.zoo
        for X in $(SRCS) $(AUX) ; do \
            echo $$X ; \
            sed 's/$$/^M/' $$X \
            > tmp.dir/$$X ; done
        cd tmp.dir ; zoo aM ../tar.zoo *
        -rm -rf tmp.dir
```

Next: Index of Concepts, Previous: Complex Makefile Example, Up: GNU `make`   [Contents][Index]

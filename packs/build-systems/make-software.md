---
title: "Make (software)"
source: https://en.wikipedia.org/wiki/Make_(software)
domain: build-systems
license: GFDL-1.3 / CC-BY-SA-4.0
tags: makefile, cmake, build system, compiler toolchain
fetched: 2026-07-02
---

# Make (software)

In software development, **Make** is a command-line interface software tool that performs actions ordered by configured dependencies as defined in a configuration file called a *makefile*. It is commonly used for build automation to build executable code (such as a program or library) from source code. Make is also not limited to building and can perform any operation available via the operating system shell.

Make is widely used, especially in Unix and Unix-like operating systems, even though many competing technologies and tools are available, including similar tools that perform actions based on dependencies, some compilers and interactively via an integrated development environment.

In addition to referring to the original Unix tool, Make is also a technology since multiple tools have been implemented with roughly the same functionality – including similar makefile syntax and semantics.

## Origin

Stuart Feldman created Make while at Bell Labs. An early version was completed in April 1976. Feldman received the 2003 ACM Software System Award for authoring Make.

Feldman describes the inspiration to write Make as arising from a coworker's frustration with the available tooling of the time:

> Make originated with a visit from Steve Johnson (author of yacc, etc.), storming into my office, cursing the Fates that had caused him to waste a morning debugging a correct program (bug had been fixed, file hadn't been compiled, `cc *.o` was therefore unaffected). As I had spent a part of the previous evening coping with the same disaster on a project I was working on, the idea of a tool to solve it came up. It began with an elaborate idea of a dependency analyzer, boiled down to something much simpler, and turned into Make that weekend. Use of tools that were still wet was part of the culture. Makefiles were text files, not magically encoded binaries, because that was the Unix ethos: printable, debuggable, understandable stuff.

— Stuart Feldman, *The Art of Unix Programming*, Eric S. Raymond 2003

Before Make, building on Unix mostly consisted of shell scripts written for each program's codebase. Make's dependency ordering and out-of-date checking makes the build process more robust and more efficient. The makefile allowed for better organization of build logic and often fewer build files.

Make is widely used in part due to its early inclusion in Unix, starting with PWB/UNIX 1.0, which featured a variety of software development tools.

## Variants

Make has been implemented numerous times, generally using the same makefile format and providing the same features, but some providing enhancements from the original. Examples:

- Sun DevPro Make appeared in 1986 with SunOS-3.2. With SunOS-3.2. It was delivered as an optional program; with SunOS-4.0, SunPro Make was made the default Make program. In December 2006, Sun DevPro Make was made open source as part of the efforts to open-source Solaris.
- dmake or Distributed Make that came with Sun Solaris Studio as its default Make, but not the default one on the Solaris Operating System (SunOS). It was originally required to build OpenOffice, but in 2009 the build system was rewritten to use GNU Make. While Apache OpenOffice still contains a mixture of both build systems, the much more actively developed LibreOffice only uses the modernized "gbuild" now.
- BSD Make (*pmake*, *bmake* or *fmake*), which is derived from Adam de Boor's work on a version of Make capable of building targets in parallel, and survives with varying degrees of modification in FreeBSD, NetBSD and OpenBSD. Distinctively, it has conditionals and iterative loops which are applied at the parsing stage and may be used to conditionally and programmatically construct the makefile, including generation of targets at runtime.
- GNU Make (short *gmake*) is the standard implementation of Make for Linux and macOS. It provides several extensions over the original Make, such as conditionals. It also provides many built-in functions which can be used to eliminate the need for shell-scripting in the makefile rules as well as to manipulate the variables set and used in the makefile. For example, the *foreach* function can be used to iterate over a list of values, such as the names of files in a given directory. GNU Make is required for building many software systems, including GNU Compiler Collection (GCC) (since version 3.4), the Linux kernel, Apache OpenOffice, LibreOffice, and Mozilla Firefox.
- Rocky Bernstein's Remake is a fork of GNU Make and provides several extensions over GNU Make, such as better location and error-location reporting, execution tracing, execution profiling, and it contains a debugger.
- Glenn Fowler's *nmake* (unrelated to the same-named Microsoft variant) is incompatible with the UNIX variant, but provides features which, according to some, reduce the size of makefiles by a factor of 10.
- Microsoft *nmake* is normally installed with Visual Studio. It supports preprocessor directives such as includes and conditional expressions which use variables set on the command-line or within the makefiles. Inference rules differ from Make; for example they can include search paths.
- Embarcadero make has a command-line option that "Causes MAKE to mimic Microsoft's NMAKE.".
- Qt Project's *Jom* tool is a clone of nmake.
- *Mk* replaced Make in Research Unix, starting from version 9. A redesign of the original tool by Bell Labs programmer Andrew G. Hume, it features a different syntax. Mk became the standard build tool in Plan 9, Bell Labs' intended successor to Unix.
- *Kati* is Google's replacement of GNU Make, as of 2020 used in Android OS builds. It translates the makefile into ninja for faster incremental builds (similar to the cmake metatool).
- Snakemake is a Python-driven implementation for compiling and running bioinformatics workflows.

POSIX includes standardization of the basic features and operation of the Make utility, and is implemented with varying degrees of compatibility with Unix-based versions of Make. In general, simple makefiles may be used between various versions of Make with reasonable success. GNU Make, Makepp and some versions of BSD Make default to looking first for files named "GNUmakefile", "Makeppfile" and "BSDmakefile" respectively, which allows one to put makefiles which use implementation-defined behavior in separate locations.

## Use

In general, based on a makefile, Make updates target files from source files if any source file has a newer timestamp than the target file or the target file does not exist. For example, this could include compiling C files (`*.c`) into object files, then linking the object files into an executable program. Or this could include compiling TypeScript files (`*.ts`) to JavaScript for use in a browser. Other examples include: convert a source image file to another format, copy a file to a content management system, and send e-mail about build status.

A makefile defines targets where each is either a file to generate or is a user-defined concept, called a *phony* target.

Make updates the targets passed as arguments:

```mw
make [-f makefile] [options] [targets]
```

If no target is specified, Make updates the first target in the makefile which is often a phony target to perform the most commonly used action.

Make skips build actions if the target file timestamp is after that of the source files. Doing so optimizes the build process by skipping actions when the target file is up-to-date, but sometimes updates are skipped erroneously due to file timestamp issues including restoring an older version of a source file, or when a network filesystem is a source of files and its clock or time zone is not synchronized with the machine running Make. Also, if a source file's timestamp is in the future, make repeatedly triggers unnecessary actions, causing longer build time.

When Make starts, it uses the makefile specified on the command-line or if not specified, then uses the one found by via specific search rules. Generally, Make defaults to using the file in the working directory named Makefile. GNU Make searches for the first file matching: GNUmakefile, makefile, or Makefile.

Make processes the options of the command-line based on the loaded makefile.

## Makefile

The **makefile** language is partially declarative programming where end conditions are described but the order in which actions are to be taken is not.

Makefiles can contain the following constructs:

- *Explicit rule*: defines when and how to update a target, listing *prerequisites* (dependent targets) and commands that define the update action, called the *recipe*
- *Implicit rule*: defines when and how to remake a class of files based on their names, including how a target depends on a file with a name similar to the target and an update recipe
- *Variable definition*: associates a text value with a name that can be substituted into later text
- *Directive*: instruction to do something special such as include another makefile
- *Comment*: line starting with `#`

### Rules

Each rule begins with a *dependency line* which consists of the rule's target name followed by a colon (:), and optionally a list of targets (also known as prerequisites) on which the rule's target depends.

```
target [target ...]: [component ...]
Tab ↹[command 1]
	   .
	   .
	   .
Tab ↹[command n]
```

Usually a rule has a single target, rather than multiple.

A dependency line may be followed by a recipe: a series of TAB indented command lines that define how to generate the target from the components (i.e. source files). If any prerequisite has a more recent timestamp than the target file or the target does not exist as a file, the recipe is performed.

The first command may appear on the same line after the prerequisites, separated by a semicolon,

```mw
targets: prerequisites ; command
```

for example,

```mw
hello: ; @echo "hello"
```

Each command line must begin with a tab character. Even though a space is also whitespace, Make requires tab. Since this often leads to confusion and mistakes, this aspect of makefile syntax is subject to criticism. Eric S. Raymond describes it as "one of the worst design botches in the history of Unix" and *The Unix-Haters Handbook* said "using tabs as part of the syntax is like one of those pungee [sic] stick traps in *The Green Berets*". Feldman explains the choice as caused by a workaround for an early implementation difficulty, and preserved by a desire for backward compatibility with the very first users:

> Why the tab in column 1? Yacc was new, Lex was brand new. I hadn't tried either, so I figured this would be a good excuse to learn. After getting myself snarled up with my first stab at Lex, I just did something simple with the pattern newline-tab. It worked, it stayed. And then a few weeks later I had a user population of about a dozen, most of them friends, and I didn't want to screw up my embedded base. The rest, sadly, is history.

— Stuart Feldman

GNU Make since version 3.82 allows the choice of any symbol (one character) as the recipe prefix using the .RECIPEPREFIX special variable:

```mw
.RECIPEPREFIX := :
all:
:@echo "recipe prefix symbol is set to '$(.RECIPEPREFIX)'"
```

Each command is executed in a separate shell. Since operating systems use different shells, this can lead to unportable makefiles. For example, GNU Make (all POSIX Makes) executes commands with /bin/sh by default, where Unix commands like cp are normally used. In contrast, Microsoft's *nmake* executes commands with cmd.exe where batch commands like copy are available but not necessarily cp.

Since a recipe is optional, the dependency line can consist solely of components that refer to other targets:

```mw
realclean: clean distclean
```

The following example rule is evaluated when Make updates target file.txt via `make file.txt`. If file.html is newer than file.txt or file.txt does not exist, then the command is run to generate file.txt from file.html.

```mw
file.txt: file.html
	lynx -dump file.html > file.txt
```

A command can have one or more of the following prefixes (after the tab):

- minus (-) specifies to ignore an error from the command
- at (@) specifies to *not* output the command before it is executed
- plus (+) specifies to execute the command even if Make is invoked in "do not execute" mode

Ignoring errors and silencing echo can alternatively be obtained via the special targets `.IGNORE` and `.SILENT`.

Microsoft's NMAKE has predefined rules that can be omitted from these makefiles, e.g. `c.obj $(CC)$(CFLAGS)`.

### Macros

A makefile can define and use macros. Macros are usually referred to as *variables* when they hold simple string definitions, like `CC=clang`. Macros in makefiles may be overridden in the command-line arguments passed to the Make utility. Environment variables are also available as macros.

For example, the macro `CC` is frequently used in makefiles to refer to the location of a C compiler. If used consistently throughout the makefile, then the compiler used can be changed by changing the value of the macro rather than changing each rule command that invokes the compiler.

Macros are commonly named in all-caps:

```mw
MACRO = definition
```

A macro value can consist of other macro values. The value of macro is expanded on each use lazily.

A macro is used by expanding either via $*NAME* or $(*NAME*). The latter is safer since omitting the parentheses leads to Make interpreting the next letter after the `$` as the entire variable name. An equivalent form uses curly braces rather than parentheses, i.e. `${}`, which is the style used in BSD.

```mw
NEW_MACRO = $(MACRO)-$(MACRO2)
```

Macros can be composed of shell commands by using the command substitution operator `!=`.

```mw
YYYYMMDD != date
```

The command-line syntax for overriding a macro is:

```mw
make MACRO="value" [MACRO="value" ...] TARGET [TARGET ...]
```

Makefiles can access predefined *internal macros*, with `?` and `@` being common.

```mw
target: component1 component2
	# echo components YOUNGER than TARGET
	echo $? 
	# echo TARGET name
	echo $@
```

A common syntax when defining macros, which works on BSD and GNU Make, is to use +=, ?=, and != instead of the equal sign (=).

### Suffix rules

Suffix rules have "targets" with names in the form `.FROM.TO` and are used to launch actions based on file extension. In the command lines of suffix rules, POSIX specifies that the internal macro `$<` refers to the first prerequisite and `$@` refers to the target. In this example, which converts any HTML file into text, the shell redirection token `>` is part of the command line, whereas `$<` is a macro referring to the HTML file:

```mw
.SUFFIXES: .txt .html

# From .html to .txt
.html.txt:
	lynx -dump $<   >   $@
```

When called from the command line, the example above expands:

```mw
$ make -n file.txt
lynx -dump file.html > file.txt
```

### Pattern rules

Suffix rules cannot have any prerequisites of their own. If they have any, they are treated as normal files with unusual names, not as suffix rules. GNU Make supports suffix rules for compatibility with old makefiles but otherwise encourages usage of *pattern rules*.

A pattern rule looks like an ordinary rule, except that its target contains exactly one `%` character within the string. The target is considered a pattern for matching file names: the `%` can match any substring of zero or more characters, while other characters match only themselves. The prerequisites likewise use `%` to show how their names relate to the target name.

The example above of a suffix rule would look like the following pattern rule:

```mw
# From %.html to %.txt
%.txt : %.html 
	lynx -dump $< > $@
```

Single-line comments are started with the hash symbol (#).

### Directive

A directive specifies special behavior such as including another makefile.

### Line continuation

Line continuation is indicated with a backslash `\` character at the end of a line.

```
   target: component \
           component
   Tab ↹command ; \
   another-command | \
   piped-command
```

## Examples

The following commands are in the context of the makefile that follows.

```mw
make            # updates first target, 'all'
make help       # updates target 'help' to list targets
make dist       # updates target 'dist' to build for distribution
```

```mw
PACKAGE	 = package
VERSION	 = ` date "+%Y.%m%d%" `
RELEASE_DIR  = ..
RELEASE_FILE = $(PACKAGE)-$(VERSION)

# Default target
# note: variable LOGNAME comes from the environment
all:
	echo "Hello $(LOGNAME), nothing to do by default"
	echo "Try 'make help'"

# Display targets by searching this file
help:
	egrep "^# target:" [Mm]akefile

# Make a release
dist:
	tar -cf  $(RELEASE_DIR)/$(RELEASE_FILE) && \
	gzip -9  $(RELEASE_DIR)/$(RELEASE_FILE).tar
```

Below is a simple makefile that by default (the "all" rule is listed first) compiles a source file called "helloworld.c" using the system's C compiler and also provides a "clean" target to remove the generated files if the user desires to start over. The `$@` and `$<` are two of the so-called internal macros (also known as automatic variables) and stand for the target name and "implicit" source, respectively. In the example below, `$^` expands to a space delimited list of the prerequisites. There are a number of other internal macros.

```mw
CFLAGS ?= -g
LDLIBS += -lm

all: Out.txt

Out.txt: helloworld
	./$< > $@

helloworld: helloworld.o
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

helloworld.o: helloworld.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	$(RM) Out.txt helloworld helloworld.o
```

Many systems come with predefined Make rules and macros to specify common tasks such as compilation based on file suffix. This lets users omit the actual (often unportable) instructions of how to generate the target from the source(s). On such a system the makefile above could be modified as follows:

```mw
all: helloworld

helloworld: helloworld.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

clean:
	$(RM) helloworld helloworld.o

# suffix rule
.c.o:
	$(CC) $(CFLAGS) -c $<

.SUFFIXES: .c
```

That "helloworld.o" depends on "helloworld.c" is now automatically handled by Make. In such a simple example as the one illustrated here this hardly matters, but the real power of suffix rules becomes evident when the number of source files in a software project starts to grow. One only has to write a rule for the linking step and declare the object files as prerequisites. Make will then implicitly determine how to make all the object files and look for changes in all the source files.

Simple suffix rules work well as long as the source files do not depend on each other and on other files such as header files. Another route to simplify the build process is to use so-called pattern matching rules that can be combined with compiler-assisted dependency generation. As a final example requiring the gcc compiler and GNU Make, here is a generic makefile that compiles all C files in a folder to the corresponding object files and then links them to the final executable. Before compilation takes place, dependencies are gathered in makefile-friendly format into a hidden file ".depend" that is then included to the makefile. Portable programs ought to avoid constructs used below.

```mw
# Generic GNUMakefile

# snippet to fail if not GNU
ifneq (,)
This makefile requires GNU Make.
endif

PROGRAM = foo
C_FILES := $(wildcard *.c)
OBJS := $(patsubst %.c, %.o, $(C_FILES))
CC = cc
CFLAGS = -Wall -pedantic
LDFLAGS =
LDLIBS = -lm

all: $(PROGRAM)

$(PROGRAM): .depend $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LDFLAGS) -o $(PROGRAM) $(LDLIBS)

depend: .depend

.depend: cmd = gcc -MM -MF depend $(var); cat depend >> .depend;
.depend:
	@echo "Generating dependencies..."
	@$(foreach var, $(C_FILES), $(cmd))
	@rm -f depend

-include .depend

# These are the pattern matching rules. In addition to the automatic
# variables used here, the variable $* that matches whatever % stands for
# can be useful in special cases.
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%: %.o
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f .depend $(OBJS)

.PHONY: clean depend
```

## Dependency tracking

Makefile consist of dependencies and a forgotten or an extra one may not be immediately obvious to the user and may result in subtle bugs in the generated software that are hard to catch. Various approaches may be used to avoid this problem and keep dependencies in source and makefiles in sync. One approach is using the compiler to keep track of dependencies changes. GCC can statically analyze the source code and produce rules for the given file automatically by using the `-MM` switch. The other approach would be makefiles or third-party tools that would generate makefiles with dependencies (e.g. Automake toolchain by the GNU Project, can do so automatically).

Another approach is to use meta-build tools like CMake, Meson etc.

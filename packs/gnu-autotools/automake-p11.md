---
title: "automake (part 11/14)"
source: https://www.gnu.org/software/automake/manual/automake.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 11/14
---

## 26 Frequently Asked Questions about Automake

This chapter covers some questions that often come up on the mailing lists.

### 26.1 Version control and generated files

#### Background: distributed generated Files

Packages made with Autoconf and Automake ship with some generated files like configure or Makefile.in. These files were generated on the developer’s machine and are distributed so that end-users do not have to install the maintainer tools required to rebuild them. Other generated files like Lex scanners, Yacc parsers, or Info documentation are usually distributed on similar grounds.

Automake output generates rules in Makefiles to rebuild these files. For instance, `make` will run `autoconf` to rebuild configure whenever configure.ac is changed. This makes development safer by ensuring a configure is never out-of-date with respect to configure.ac.

As generated files shipped in packages are up-to-date, and because `tar` preserves timestamps, these rebuild rules are not triggered when a user unpacks and builds a package.

#### Background: Version Control and Timestamps

Typically when you update files with version control commands, working files will have the timestamp of your update, not the original timestamp of the commit. This is meant to make sure that `make` notices that source files have been updated.

This timestamp shift is troublesome when both sources and generated files are kept under version control. Because version control commands often process files in lexical order, configure.ac will appear newer than configure after a version control command that updates both files, even if configure was newer than configure.ac when it was committed. Calling `make` will then trigger a spurious rebuild of configure.

#### Living with Version Control in Autoconfiscated Projects

There are basically two clans among maintainers: those who keep all distributed files under version control, including generated files, and those who keep generated files *out* of version control.

#### All Files under Version Control

- The repository contains all distributed files so you know exactly what is distributed, and you can check out any prior version entirely.
- Maintainers can see how generated files evolve (for instance, you can see what happens to your Makefile.ins when you upgrade Automake and make sure they look OK).
- Users do not need Autotools to build a check-out of the project; it works just like a released tarball.
- If users use version control to update their copy, timestamps will likely be inaccurate. Some rebuild rules will be triggered and attempt to run developer tools such as `autoconf` or `automake`. Calls to such tools are all wrapped into a call to the `missing` script discussed later (see `missing` and `AM_MAINTAINER_MODE`), so that the user will see more descriptive warnings about missing or out-of-date tools, and possible suggestions about how to obtain them, rather than just some “command not found” error, or (worse) some obscure message from some older version of the required tool they happen to have installed. Maintainers interested in keeping their package buildable from a checkout even for those users that lack maintainer-specific tools might want to provide a helper script (or to enhance their existing bootstrap script) to fix the timestamps after a checkout, to prevent spurious rebuilds. In case of a project committing the Autotools-generated files, as well as the generated .info files, such a script might look something like this: #!/bin/sh # fix-timestamp.sh: Prevent useless rebuilds after "git pull". sleep 1 # aclocal-generated aclocal.m4 depends on locally-installed # '.m4' macro files, as well as on 'configure.ac'. touch aclocal.m4 sleep 1 # autoconf-generated 'configure' and autoheader-generated # config.h.in both depend on aclocal.m4 and on configure.ac. touch configure config.h.in # Automake-generated Makefile.in files depend on Makefile.am, # and makeinfo-generated '.info' files depend on the # corresponding '.texi' files. touch $(git ls-files '*/Makefile.in' '*.info')
- In distributed development, developers are likely to have different versions of the maintainer tools installed. In this case rebuilds triggered by clock skew can lead to spurious changes to generated files. There are several solutions to this:
  - All developers should use the same versions, so that the rebuilt files are identical to files in the repository. (This becomes difficult when different projects on which you are working use different versions.)
  - Or people use a script to fix the timestamp after a checkout (the GCC folks have such a script).
  - Or configure.ac uses `AM_MAINTAINER_MODE`, which disables all of these rebuild rules by default. This is further discussed in `missing` and `AM_MAINTAINER_MODE`.
- Although we focused on spurious rebuilds, the converse can also happen. Version control timestamp handling can also let you think an out-of-date file is up-to-date. For instance, suppose a developer has modified Makefile.am and has rebuilt Makefile.in, and then decides to do a last-minute change to Makefile.am right before checking in both files (without rebuilding Makefile.in to account for the change). This last change to Makefile.am makes the copy of Makefile.in out-of-date. Assuming version control processes files alphabetically, when another developer updates their tree, Makefile.in will happen to be newer than Makefile.am. This other developer will not see that Makefile.in is out-of-date.

#### Generated Files out of Version Control

One way to get version control and `make` working peacefully is to never store generated files in version control, i.e., do not version-control files that are Makefile targets (also called *derived* files).

This way developers are not annoyed by changes to generated files. It does not matter if they all have different versions (assuming they are compatible, of course). And finally, timestamps are not lost; changes to source files can’t be missed as in the Makefile.am/Makefile.in example discussed earlier.

The drawback is that the repository does not contain some files that are is distributed, so builders now need to install various development tools (maybe even specific versions) before they can build a checkout. But, after all, the job of version control is versioning, not distribution.

Allowing developers to use different versions of their tools can also hide bugs during distributed development. Indeed, developers will be using (hence testing) their own generated files, instead of the generated files that will be released. The developer who prepares the tarball might be using a version of the tool that produces bogus output (for instance a non-portable C file), something other developers could have noticed if they weren’t using their own versions of this tool.

#### Third-party Files

Another class of files not discussed here (because they do not cause timestamp issues) are files that are shipped with a package, but maintained elsewhere. For instance, tools like `gettextize` and `autopoint` (from Gettext) or `libtoolize` (from Libtool), will install or update files in your package.

These files, whether they are kept under version control or not, raise similar concerns about version mismatch between developers’ tools. The Gettext manual has a section about this; see Integrating with Version Control Systems in *GNU gettext tools*.

### 26.2 `missing` and `AM_MAINTAINER_MODE`

#### `missing`

The `missing` script is a wrapper around several maintainer tools, designed to warn users if a maintainer tool is required but missing. Typical maintainer tools are `autoconf`, `automake`, `bison`, etc. Because files generated by these tools are shipped with the other sources of a package, these tools shouldn’t be required during a user build and they are not checked for in configure.

However, if for some reason a rebuild rule is triggered and involves a missing tool, `missing` will notice it and warn the user, even suggesting how to obtain such a tool (at least in case it is a well-known one, like `makeinfo` or `bison`). This is more helpful and user-friendly than just having the rebuild rules spewing out a terse error message like ‘sh: *tool*: command not found’. Similarly, `missing` will warn the user if it detects that a maintainer tool it attempted to use seems too old (be warned that diagnosing this correctly is typically more difficult than detecting missing tools, and requires cooperation from the tool itself, so it won’t always work).

If the required tool is installed, `missing` will run it and won’t attempt to continue after failures. This is correct behavior during development: developers love fixing failures. However, users with missing or too old maintainer tools may get an error when the rebuild rule is spuriously triggered, halting the build. This failure to let the build continue is one of the arguments of the `AM_MAINTAINER_MODE` advocates.

#### `AM_MAINTAINER_MODE`

`AM_MAINTAINER_MODE` allows you to choose whether the so called "rebuild rules" should be enabled or disabled. With `AM_MAINTAINER_MODE([enable])`, they are enabled by default; otherwise they are disabled by default. In the latter case, if you have `AM_MAINTAINER_MODE` in configure.ac, and run ‘./configure && make’, then `make` will *never* attempt to rebuild configure, Makefile.ins, Lex or Yacc outputs, etc. That is, this disables build rules for files that are usually distributed and that users should normally not have to update.

The user can override the default setting by passing either ‘--enable-maintainer-mode’ or ‘--disable-maintainer-mode’ to `configure`.

People use `AM_MAINTAINER_MODE` either because they do not want their users (or themselves) annoyed by clock skew (see Version control and generated files), or because they simply can’t stand the rebuild rules and prefer running maintainer tools explicitly.

`AM_MAINTAINER_MODE` also allows you to disable some custom build rules conditionally. Some developers use this feature to disable rules that need exotic tools that users may not have available.

Several years ago François Pinard pointed out several arguments against this `AM_MAINTAINER_MODE` macro. Most of them relate to insecurity. By removing dependencies you get non-dependable builds: changes to source files can have no effect on generated files and this can be very confusing when unnoticed. He adds that security shouldn’t be reserved to maintainers (what --enable-maintainer-mode suggests), on the contrary. If one user has to modify a Makefile.am, then either Makefile.in should be updated or a warning should be output (this is what Automake uses `missing` for) but the last thing you want is that nothing happens and the user doesn’t notice it (this is what happens when rebuild rules are disabled by `AM_MAINTAINER_MODE`).

Jim Meyering, the inventor of the `AM_MAINTAINER_MODE` macro, was swayed by François’ arguments, and got rid of `AM_MAINTAINER_MODE` in all of his packages.

Still many people continue to use `AM_MAINTAINER_MODE`, because it helps them working on projects where all files are kept under version control, and because `missing` isn’t enough if you have the wrong version of the tools.

### 26.3 Why doesn’t Automake support wildcards?

Developers are lazy. They would often like to use wildcards in Makefile.ams, so that they would not need to remember to update Makefile.ams every time they add, delete, or rename a file.

There are several objections to this:

- When using version control, developers need to remember they have to add or remove files from version control anyway. Updating Makefile.am accordingly quickly becomes a reflex. Conversely, if your application doesn’t compile because you forgot to add a file in Makefile.am, it will help you remember to add the file to version control.
- Using wildcards makes it easy to distribute files by mistake. For instance, some code a developer is experimenting with (a test case, say) that should not be part of the distribution.
- Using wildcards it’s easy to omit some files by mistake. For instance, one developer creates a new file, uses it in many places, but forgets to commit it. Another developer then checks out the incomplete project and is able to run ‘make dist’ successfully, even though a file is missing. By listing files, ‘make dist’ *will* complain.
- Wildcards are not portable to some non-GNU `make` implementations, e.g., NetBSD `make` will not expand globs such as ‘*’ in prerequisites of a target.
- Finally, it’s quite hard to *forget* to add a file to Makefile.am: files that are not listed in Makefile.am are not compiled or installed, so you can’t even test them.

Still, these are philosophical objections, and as such you may disagree, or find enough value in wildcards to dismiss all of them. Before you start writing a patch against Automake to teach it about wildcards, let’s see the main technical issue: portability.

Although ‘$(wildcard ...)’ works with GNU `make`, it is not portable to other `make` implementations.

The only way Automake could support `$(wildcard ...)` is by expanding `$(wildcard ...)` when `automake` is run. The resulting Makefile.ins would be portable since they would list all files and not use ‘$(wildcard ...)’. However that means developers would need to remember to run `automake` each time they add, delete, or rename files.

Compared to editing Makefile.am, this is a very small gain. Sure, it’s easier and faster to type ‘automake; make’ than to type ‘emacs Makefile.am; make’. But nobody bothered enough to write a patch to add support for this syntax. Some people use scripts to generate file lists in Makefile.am or in separate Makefile fragments.

Even if you don’t care about portability, and are tempted to use ‘$(wildcard ...)’ anyway because you target only GNU Make, you should know there are many places where Automake needs to know exactly which files should be processed. As Automake doesn’t know how to expand ‘$(wildcard ...)’, you cannot use it in these places. ‘$(wildcard ...)’ is a black box comparable to `AC_SUBST`ed variables as far Automake is concerned.

You can get warnings about ‘$(wildcard ...’) constructs using the -Wportability flag.

### 26.4 Limitations on File Names

Automake attempts to support all kinds of file names, even those that contain unusual characters or are unusually long. However, some limitations are imposed by the underlying operating system and tools.

Most operating systems prohibit the use of the null byte in file names, and reserve ‘/’ as a directory separator. Also, they require that file names are properly encoded for the user’s locale. Automake is subject to these limits.

Portable packages should limit themselves to POSIX file names. These can contain ASCII letters and digits, ‘_’, ‘.’, and ‘-’. File names consist of components separated by ‘/’. File name components cannot begin with ‘-’.

Portable POSIX file names cannot contain components that exceed a 14-byte limit, but nowadays it’s normally safe to assume the more-generous XOPEN limit of 255 bytes. POSIX limits file names to 255 bytes (XOPEN allows 1023 bytes), but you may want to limit a source tarball to file names of 99 bytes to avoid interoperability problems with old versions of `tar`.

If you depart from these rules (e.g., by using non-ASCII characters in file names, or by using lengthy file names), your installers may have problems for reasons unrelated to Automake. However, if this does not concern you, you should know about the limitations imposed by Automake itself. These limitations are undesirable, but some of them seem to be inherent to underlying tools like Autoconf, Make, M4, and the shell. They fall into three categories: install directories, build directories, and file names.

The following characters:

```
newline " # $ ' `
```

should not appear in the names of install directories. For example, the operand of `configure`’s --prefix option should not contain these characters.

Build directories suffer the same limitations as install directories, and in addition should not contain the following characters:

```
& @ \
```

For example, the full name of the directory containing the source files should not contain these characters.

Source and installation file names like main.c are limited even further: they should conform to the POSIX/XOPEN rules described above. In addition, if you plan to port to non-POSIX environments, you should avoid file names that differ only in case (e.g., makefile and Makefile). Nowadays it is no longer worth worrying about the 8.3 limits of DOS file systems.

### 26.5 Flag Variables Ordering

```
What is the difference between AM_CFLAGS, CFLAGS, and
mumble_CFLAGS?
```

```
Why does automake output CPPFLAGS after
AM_CPPFLAGS on compile lines?  Shouldn’t it be the converse?
```

```
My configure adds some warning flags into CXXFLAGS.  In
one Makefile.am I would like to append a new flag, however if I
put the flag into AM_CXXFLAGS it is prepended to the other
flags, not appended.
```

#### Compile Flag Variables

This section attempts to answer all the above questions. We will mostly discuss `CPPFLAGS` in our examples, but the answer holds for all the compile flags used in Automake: `CCASFLAGS`, `CFLAGS`, `CPPFLAGS`, `CXXFLAGS`, `FCFLAGS`, `FFLAGS`, `GCJFLAGS`, `LDFLAGS`, `LFLAGS`, `LIBTOOLFLAGS`, `OBJCFLAGS`, `OBJCXXFLAGS`, `RFLAGS`, `UPCFLAGS`, and `YFLAGS`.

`CPPFLAGS`, `AM_CPPFLAGS`, and `mumble_CPPFLAGS` are three variables that can be used to pass flags to the C preprocessor ( these variables are also used for other languages like C++ or preprocessed Fortran). `CPPFLAGS` is the user variable (see Variables reserved for the user), `AM_CPPFLAGS` is the Automake variable, and `mumble_CPPFLAGS` is the variable specific to the `mumble` target (we call this a per-target variable, see Program and Library Variables).

Automake always uses two of these variables when compiling C sources files. When compiling an object file for the `mumble` target, the first variable will be `mumble_CPPFLAGS` if it is defined, or `AM_CPPFLAGS` otherwise. The second variable is always `CPPFLAGS`.

In the following example,

```
bin_PROGRAMS = foo bar
foo_SOURCES = xyz.c
bar_SOURCES = main.c
foo_CPPFLAGS = -DFOO
AM_CPPFLAGS = -DBAZ
```

xyz.o will be compiled with ‘$(foo_CPPFLAGS) $(CPPFLAGS)’, (because xyz.o is part of the `foo` target), while main.o will be compiled with ‘$(AM_CPPFLAGS) $(CPPFLAGS)’ (because there is no per-target variable for target `bar`).

The difference between `mumble_CPPFLAGS` and `AM_CPPFLAGS` being clear enough, let’s focus on `CPPFLAGS`. `CPPFLAGS` is a user variable, i.e., a variable that users are entitled to modify in order to compile the package. This variable, like many others, is documented at the end of the output of ‘configure --help’.

For instance, someone who needs to add /home/my/usr/include to the C compiler’s search path would configure a package with

```
./configure CPPFLAGS='-I /home/my/usr/include'
```

and this flag would be propagated to the compile rules of all Makefiles.

It is also not uncommon to override a user variable at `make`-time. Many installers do this with `prefix`, but this can be useful with compiler flags too. For instance, while debugging a C++ project, if you need to disable optimization in one specific object file, you can run something like

```
rm file.o
make CXXFLAGS=-O0 file.o
make
```

The reason ‘$(CPPFLAGS)’ appears after ‘$(AM_CPPFLAGS)’ or ‘$(mumble_CPPFLAGS)’ in the compile command is that users should have the last say. In the example above, the desire is for the ‘CXXFLAGS=-O0’ to supersede any other switch from `AM_CXXFLAGS` or `mumble_CXXFLAGS`.

It’s true that not all options to all programs can be overridden. So in general, users could conceivably want to place options at arbitrary places in the command line, but Automake does not support this. It would be difficult to make such generality comprehensible. Being able to specify the final options commonly suffices.

Thus, you should never redefine a user variable such as `CPPFLAGS` in Makefile.am. Use ‘automake -Woverride’ to diagnose such mistakes. Even something like

```
CPPFLAGS = -DDATADIR=\"$(datadir)\" @CPPFLAGS@
```

is erroneous. Although this preserves configure’s value of `CPPFLAGS`, the definition of `DATADIR` will disappear if a user attempts to override `CPPFLAGS` from the `make` command line.

```
AM_CPPFLAGS = -DDATADIR=\"$(datadir)\"
```

is all that is needed here if no per-target flags are used.

You should not add options to these user variables within configure either, for the same reason. Occasionally you need to modify these variables to perform a test, but you should reset their values afterwards. In contrast, it is OK to modify the ‘AM_’ variables within configure if you `AC_SUBST` them, but it is rather rare that you need to do this, unless you want to change the default definitions of the ‘AM_’ variables in all Makefiles.

What we recommend is that you define extra flags in separate variables. For instance, you may write an Autoconf macro that computes a set of warning options for the C compiler, and `AC_SUBST` them in `WARNINGCFLAGS`; you may also have an Autoconf macro that determines which compiler and which linker flags should be used to link with library libfoo, and `AC_SUBST` these in `LIBFOOCFLAGS` and `LIBFOOLDFLAGS`. Then, a Makefile.am could use these variables as follows:

```
AM_CFLAGS = $(WARNINGCFLAGS)
bin_PROGRAMS = prog1 prog2
prog1_SOURCES = ...
prog2_SOURCES = ...
prog2_CFLAGS = $(LIBFOOCFLAGS) $(AM_CFLAGS)
prog2_LDFLAGS = $(LIBFOOLDFLAGS)
```

In this example both programs will be compiled with the flags substituted into ‘$(WARNINGCFLAGS)’, and `prog2` will additionally be compiled with the flags required to link with libfoo.

Note that listing `AM_CFLAGS` in a per-target `CFLAGS` variable is a common idiom to ensure that `AM_CFLAGS` applies to every target in a Makefile.in.

Using variables like this gives you full control over the ordering of the flags. For instance, if there is a flag in $(WARNINGCFLAGS) that you want to negate for a particular target, you can use something like ‘prog1_CFLAGS = $(AM_CFLAGS) -no-flag’. If all of these flags had been forcefully appended to `CFLAGS`, there would be no way to disable one flag. Yet another reason to leave user variables to users.

Finally, we have avoided naming the variable of the example `LIBFOO_LDFLAGS` (with an underscore) because that would cause Automake to think that this is a per-target variable (like `mumble_LDFLAGS`) for some non-declared `LIBFOO` target.

#### Other Variables

There are other variables in Automake that follow similar principles to allow user options. For instance, Texinfo rules (see Texinfo) use `MAKEINFOFLAGS` and `AM_MAKEINFOFLAGS`. Similarly, DejaGnu tests (see DejaGnu Tests) use `RUNTESTFLAGS` and `AM_RUNTESTFLAGS`. The tags and ctags rules (see Interfacing to `etags`) use `ETAGSFLAGS`, `AM_ETAGSFLAGS`, `CTAGSFLAGS`, and `AM_CTAGSFLAGS`. Java rules (see Java bytecode compilation (deprecated)) use `JAVACFLAGS` and `AM_JAVACFLAGS`. None of these rules support per-target flags (yet).

To some extent, even `AM_MAKEFLAGS` (see Recursing subdirectories) obeys this naming scheme. The slight difference is that `MAKEFLAGS` is passed to sub-`make`s implicitly by `make` itself.

`ARFLAGS` (see Building a library) is usually defined by Automake and has neither an `AM_` nor a per-target cousin.

Finally you should not think that the existence of a per-target variable implies the existence of an `AM_` variable or of a user variable. For instance, the `mumble_LDADD` per-target variable overrides the makefile-wide `LDADD` variable (which is not a user variable), and `mumble_LIBADD` exists only as a per-target variable. See Program and Library Variables.

### 26.6 Why are object files sometimes renamed?

This happens when per-target compilation flags are used. Object files need to be renamed just in case they would clash with object files compiled from the same sources, but with different flags. Consider the following example.

```
bin_PROGRAMS = true false
true_SOURCES = generic.c
true_CPPFLAGS = -DEXIT_CODE=0
false_SOURCES = generic.c
false_CPPFLAGS = -DEXIT_CODE=1
```

Obviously the two programs are built from the same source, but it would be bad if they shared the same object, because generic.o cannot be built with both ‘-DEXIT_CODE=0’ *and* ‘-DEXIT_CODE=1’. Therefore `automake` outputs rules to build two different objects: true-generic.o and false-generic.o.

Automake doesn’t actually determine whether source files are shared to decide if it must rename objects. It just renames all objects of a target as soon as it sees that per-target compilation flags are used.

It’s OK to share object files when per-target compilation flags are not used. For instance, true and false will both use version.o in the following example.

```
AM_CPPFLAGS = -DVERSION=1.0
bin_PROGRAMS = true false
true_SOURCES = true.c version.c
false_SOURCES = false.c version.c
```

Note that the renaming of objects is also affected by the `_SHORTNAME` variable (see Program and Library Variables).

### 26.7 Per-Object Flags Emulation

```
One of my source files needs to be compiled with different flags.  How
do I do that?
```

Automake supports per-program and per-library compilation flags (see Program and Library Variables and Flag Variables Ordering). With this you can define compilation flags that apply to all files compiled for a target. For instance, in

```
bin_PROGRAMS = foo
foo_SOURCES = foo.c foo.h bar.c bar.h main.c
foo_CFLAGS = -some -flags
```

foo-foo.o, foo-bar.o, and foo-main.o will all be compiled with ‘-some -flags’. (If you wonder about the names of these object files, see Why are object files sometimes renamed?.) Note that `foo_CFLAGS` gives the flags to use when compiling all the C sources of the *program* `foo`; it has nothing to do with foo.c or foo-foo.o specifically.

What if foo.c needs to be compiled into foo.o using some specific flags, that none of the other files requires? Obviously per-program flags are not directly applicable here. Something like per-object flags are expected, i.e., flags that would be used only when creating foo-foo.o. Automake does not support that; however this is easy to simulate using a library that contains only that object, and compiling this library with per-library flags.

```
bin_PROGRAMS = foo
foo_SOURCES = bar.c bar.h main.c
foo_CFLAGS = -some -flags
foo_LDADD = libfoo.a
noinst_LIBRARIES = libfoo.a
libfoo_a_SOURCES = foo.c foo.h
libfoo_a_CFLAGS = -some -other -flags
```

Here foo-bar.o and foo-main.o will all be compiled with ‘-some -flags’, while libfoo_a-foo.o will be compiled using ‘-some -other -flags’. Eventually, all three objects will be linked to form foo.

This trick can also be achieved using Libtool convenience libraries, for instance ‘noinst_LTLIBRARIES = libfoo.la’ (see Libtool Convenience Libraries).

Another tempting idea to implement per-object flags is to override the compile rules `automake` would output for these files. Automake will not define a rule for a target you have defined, so you could think about defining the ‘foo-foo.o: foo.c’ rule yourself. We recommend against this, because this is error prone. For instance, if you add such a rule to the first example, it will break the day you decide to remove `foo_CFLAGS` (because foo.c will then be compiled as foo.o instead of foo-foo.o, see Why are object files sometimes renamed?). Also in order to support dependency tracking, the two .o/.obj extensions, and all the other flags variables involved in a compilation, you will end up modifying a copy of the rule previously output by `automake` for this file. If a new release of Automake generates a different rule, your copy will need to be updated by hand.

### 26.8 Handling Tools that Produce Many Outputs

This section describes a `make` idiom that can be used when a tool produces multiple output files. It is not specific to Automake and can be used in ordinary Makefiles.

First, however: GNU `make` is able to express rules with multiple output files using pattern rules (see Pattern Rule Examples in *The GNU Make Manual*). We do not discuss pattern rules here because they are not portable, but if you’re able to assume GNU `make`, they are typically more convenient than any of the below approaches.

Suppose we have a program called `foo` that will read one file called data.foo and produce two files named data.c and data.h. We want to write a Makefile rule that captures this one-to-two dependency.

The naive rule is incorrect:

```
# This is incorrect.
data.c data.h: data.foo
        foo data.foo
```

What the above rule says is that data.c and data.h each depend on data.foo, and can each be built by running ‘foo data.foo’. In other words it is equivalent to:

```
# We do not want this.
data.c: data.foo
        foo data.foo
data.h: data.foo
        foo data.foo
```

which means that `foo` can be run twice. Usually it will not be run twice, because `make` implementations are smart enough to check for the existence of the second file after the first one has been built; they will therefore detect that it already exists. However there are a few situations where it can run twice anyway:

- The most worrying case is when running a parallel `make`. If data.c and data.h are built in parallel, two ‘foo data.foo’ commands will run concurrently. This is harmful.
- Another case is when the dependency (here data.foo) is (or depends upon) a phony target.

Ideally, we want a scheme that will support any number of output files, and that works with parallel `make` invocations, and that does nothing when ‘make -n’ is run. It is apparently not possible to achieve a perfect solution. Even an acceptable solution for the majority of cases gets complicated, so we will take it step by step.

One idea is to write the following:

```
# There is still a problem with this one.
data.c: data.foo
        foo data.foo
data.h: data.c
```

The idea is that ‘foo data.foo’ is run only when data.c needs to be updated, but we further state that data.h depends upon data.c. That way, if data.h is required and data.foo is out of date, the dependency on data.c will trigger the build.

This is almost perfect, but suppose we have built data.h and data.c, and then we erase data.h. Then, running ‘make data.h’ will not rebuild data.h. The above rules just state that data.c must be up-to-date with respect to data.foo, and this is already the case.

What we need is a rule that forces a rebuild when data.h is missing. Here it is:

```
# More or less works, but not easy to generalize.
data.c: data.foo
        foo data.foo
data.h: data.c

## Recover from the removal of $@
        @test -f $@ || rm -f data.c
        @test -f $@ || $(MAKE) $(AM_MAKEFLAGS) data.c
```

It is tempting to use a single test as follows:

```
# This breaks make -n.
data.h: data.c

## Recover from the removal of $@
        @if test -f $@; then :; else \
          rm -f data.c; \
          $(MAKE) $(AM_MAKEFLAGS) data.c; \
        fi
```

but that would break ‘make -n’: at least GNU `make` and Solaris `make` execute recipes containing the ‘$(MAKE)’ string even when they are running in dry mode. So if we didn’t break the recipe above in two invocations, the file data.c would be removed even upon ‘make -n’. Not nice.

The above scheme can be extended to handle more outputs and more inputs. One of the outputs is selected to serve as a witness to the successful completion of the command, it depends upon all inputs, and all other outputs depend upon it. For instance, if `foo` should additionally read data.bar and also produce data.w and data.x, we would write:

```
data.c: data.foo data.bar
        foo data.foo data.bar
data.h data.w data.x: data.c

## Recover from the removal of $@
        @test -f $@ || rm -f data.c
        @test -f $@ || $(MAKE) $(AM_MAKEFLAGS) data.c
```

However there are now three problems in this setup. One is related to the timestamp ordering of data.h, data.w, data.x, and data.c. A second is a race condition if a parallel `make` attempts to run multiple instances of the recover block at once. Finally, the recursive rule breaks ‘make -n’ when run with GNU `make` (as well as some other `make` implementations), as it may remove data.h even when it should not (see How the `MAKE` Variable Works in *The GNU Make Manual*).

Let us deal with the first problem. `foo` outputs four files, but we do not know in which order these files are created. Suppose that data.h is created before data.c. Then we have a weird situation. The next time `make` is run, data.h will appear older than data.c, the second rule will be triggered, a shell will be started to execute the ‘if…fi’ command, but it will just execute the `then` branch, that is: nothing. In other words, because the witness we selected is not the first file created by `foo`, `make` will start a shell to do nothing each time it is run.

A simple riposte is to fix the timestamps when this happens.

```
data.c: data.foo data.bar
        foo data.foo data.bar
data.h data.w data.x: data.c
        @test ! -f $@ || touch $@

## Recover from the removal of $@
        @test -f $@ || rm -f data.c
        @test -f $@ || $(MAKE) $(AM_MAKEFLAGS) data.c
```

Another solution is to use a different and dedicated file as witness, rather than using any of `foo`’s outputs.

```
data.stamp: data.foo data.bar
        @rm -f data.tmp
        @touch data.tmp
        foo data.foo data.bar
        @mv -f data.tmp $@
data.c data.h data.w data.x: data.stamp

## Recover from the removal of $@
        @test -f $@ || rm -f data.stamp
        @test -f $@ || $(MAKE) $(AM_MAKEFLAGS) data.stamp
```

data.tmp is created before `foo` is run, so it has a timestamp older than output files output by `foo`. It is then renamed to data.stamp after `foo` has run, because we do not want to update data.stamp if `foo` fails.

This solution still suffers from the second problem: the race condition in the recover rule. If, after a successful build, a user erases data.c and data.h, and runs ‘make -j’, then `make` may start both recover rules in parallel. If the two instances of the rule execute ‘$(MAKE) $(AM_MAKEFLAGS) data.stamp’ concurrently the build is likely to fail (for instance, the two rules will create data.tmp, but only one can rename it).

Admittedly, such a weird situation does not arise during ordinary builds. It occurs only when the build tree is mutilated. Here data.c and data.h have been explicitly removed without also removing data.stamp and the other output files. `make clean; make` will always recover from these situations even with parallel makes, so you may decide that the recover rule is solely to help non-parallel make users and leave things as-is. Fixing this requires some locking mechanism to ensure only one instance of the recover rule rebuilds data.stamp. One could imagine something along the following lines.

```
data.c data.h data.w data.x: data.stamp

## Recover from the removal of $@
        @if test -f $@; then :; else \
          trap 'rm -rf data.lock data.stamp' 1 2 13 15; \

## mkdir is a portable test-and-set
          if mkdir data.lock 2>/dev/null; then \

## This code is being executed by the first process.
            rm -f data.stamp; \
            $(MAKE) $(AM_MAKEFLAGS) data.stamp; \
            result=$$?; rm -rf data.lock; exit $$result; \
          else \

## This code is being executed by the follower processes.

## Wait until the first process is done.
            while test -d data.lock; do sleep 1; done; \

## Succeed if and only if the first process succeeded.
            test -f data.stamp; \
          fi; \
        fi
```

Using a dedicated witness, like data.stamp, is very handy when the list of output files is not known beforehand. As an illustration, consider the following rules to compile many *.el files into *.elc files in a single command. It does not matter how `ELFILES` is defined (as long as it is not empty: empty targets are not accepted by POSIX).

```
ELFILES = one.el two.el three.el ...
ELCFILES = $(ELFILES:=c)

elc-stamp: $(ELFILES)
        @rm -f elc-temp
        @touch elc-temp
        $(elisp_comp) $(ELFILES)
        @mv -f elc-temp $@

$(ELCFILES): elc-stamp
        @if test -f $@; then :; else \

## Recover from the removal of $@
          trap 'rm -rf elc-lock elc-stamp' 1 2 13 15; \
          if mkdir elc-lock 2>/dev/null; then \

## This code is being executed by the first process.
            rm -f elc-stamp; \
            $(MAKE) $(AM_MAKEFLAGS) elc-stamp; \
            rmdir elc-lock; \
          else \

## This code is being executed by the follower processes.

## Wait until the first process is done.
            while test -d elc-lock; do sleep 1; done; \

## Succeed if and only if the first process succeeded.
            test -f elc-stamp; exit $$?; \
          fi; \
        fi
```

These solutions all still suffer from the third problem, namely that they break the promise that ‘make -n’ should not cause any actual changes to the tree. For those solutions that do not create lock files, it is possible to split the recover rules into two separate recipe commands, one of which does all work but the recursion, and the other invokes the recursive ‘$(MAKE)’. The solutions involving locking could act upon the contents of the ‘MAKEFLAGS’ variable, but parsing that portably is not easy (see The Make Macro MAKEFLAGS in *The Autoconf Manual*). Here is an example:

```
ELFILES = one.el two.el three.el ...
ELCFILES = $(ELFILES:=c)

elc-stamp: $(ELFILES)
        @rm -f elc-temp
        @touch elc-temp
        $(elisp_comp) $(ELFILES)
        @mv -f elc-temp $@

$(ELCFILES): elc-stamp

## Recover from the removal of $@
        @dry=; for f in x $$MAKEFLAGS; do \
          case $$f in \
            *=*|--*);; \
            *n*) dry=:;; \
          esac; \
        done; \
        if test -f $@; then :; else \
          $$dry trap 'rm -rf elc-lock elc-stamp' 1 2 13 15; \
          if $$dry mkdir elc-lock 2>/dev/null; then \

## This code is being executed by the first process.
            $$dry rm -f elc-stamp; \
            $(MAKE) $(AM_MAKEFLAGS) elc-stamp; \
            $$dry rmdir elc-lock; \
          else \

## This code is being executed by the follower processes.

## Wait until the first process is done.
            while test -d elc-lock && test -z "$$dry"; do \
              sleep 1; \
            done; \

## Succeed if and only if the first process succeeded.
            $$dry test -f elc-stamp; exit $$?; \
          fi; \
        fi
```

### 26.9 Installing to Hard-Coded Locations

```
My package needs to install some configuration file.  I tried to use
the following rule, but ‘make distcheck’ fails.  Why?
```

```
# Do not do this.
install-data-local:
        $(INSTALL_DATA) $(srcdir)/afile $(DESTDIR)/etc/afile
```

```
My package needs to populate the installation directory of another
package at install-time.  I can easily compute that installation
directory in configure, but if I install files therein,
‘make distcheck’ fails.  How else should I do it?
```

These two setups share their symptoms: ‘make distcheck’ fails because they are installing files to hard-coded paths. In the latter case the path is not hard-coded in the package, but we can consider it to be hard-coded in the system (or in whichever tool that supplies the path). As long as the path does not use any of the standard directory variables (‘$(prefix)’, ‘$(bindir)’, ‘$(datadir)’, etc.), the effect will be the same: user-installations are impossible.

As a (non-root) user who wants to install a package, you usually have no right to install anything in /usr or /usr/local. So you do something like ‘./configure --prefix ~/usr’ to install a package in your own ~/usr tree.

If a package attempts to install something to some hard-coded path (e.g., /etc/afile), regardless of this --prefix setting, then the installation will fail. ‘make distcheck’ performs such a --prefix installation, hence it will fail too.

Now, there are some easy solutions.

The above `install-data-local` example for installing /etc/afile would be better replaced by

```
sysconf_DATA = afile
```

By default `sysconfdir` will be ‘$(prefix)/etc’, because this is what the GNU Standards require. When such a package is installed on an FHS compliant system, the installer will have to set ‘--sysconfdir=/etc’. As the maintainer of the package you should not be concerned by such site policies: use the appropriate standard directory variable to install your files so that the installer can easily redefine these variables to match their site conventions.

Installing files that should be used by another package is slightly more involved. Let’s take an example and assume you want to install a shared library that is a Python extension module. If you ask Python where to install the library, it will answer something like this:

```
% python -c 'from distutils import sysconfig;
             print sysconfig.get_python_lib(1,0)'
/usr/lib/python2.5/site-packages
```

If you indeed use this absolute path to install your shared library, non-root users will not be able to install the package; hence distcheck fails.

Let’s do better. The ‘sysconfig.get_python_lib()’ function accepts a third argument that will replace Python’s installation prefix.

```
% python -c 'from distutils import sysconfig;
             print sysconfig.get_python_lib(1,0,"${exec_prefix}")'
${exec_prefix}/lib/python2.5/site-packages
```

You can also use this new path. If you do

- root users can install your package with the same --prefix as Python (you get the behavior of the previous attempt)
- non-root users can install your package too; they will have the extension module in a place that is not searched by Python but they can work around this using environment variables (and if you installed scripts that use this shared library, it’s easy to tell Python where to look in the beginning of your script, so the script works in both cases).

The `AM_PATH_PYTHON` macro uses similar commands to define ‘$(pythondir)’ and ‘$(pyexecdir)’ (see Python).

Of course not all tools are as advanced as Python regarding that substitution of *prefix*. So another strategy is to figure out the part of the installation directory that must be preserved. For instance, here is how `AM_PATH_LISPDIR` (see Emacs Lisp) computes ‘$(lispdir)’:

```
$EMACS -batch -no-site-file -eval '(while load-path
  (princ (concat (car load-path) "\n"))
  (setq load-path (cdr load-path)))' >conftest.out
lispdir=`sed -n
  -e 's,/$,,'
  -e '/.*\/lib\/x*emacs\/site-lisp$/{
        s,.*/lib/\(x*emacs/site-lisp\)$,${libdir}/\1,;p;q;
      }'
  -e '/.*\/share\/x*emacs\/site-lisp$/{
        s,.*/share/\(x*emacs/site-lisp\),${datarootdir}/\1,;p;q;
      }'
  conftest.out`
```

That is, it just picks the first directory that looks like */lib/*emacs/site-lisp or */share/*emacs/site-lisp in the search path of emacs, and then substitutes ‘${libdir}’ or ‘${datadir}’ appropriately.

The emacs case looks complicated because it processes a list and expects two possible layouts; otherwise it’s easy, and the benefits for non-root users are worth the extra `sed` invocation.

### 26.10 Debugging Make Rules

The rules and dependency trees generated by `automake` can get rather complex, and leave the developer head-scratching when things don’t work as expected. Besides the debug options provided by the `make` command (see Options Summary in *The GNU Make Manual*), here’s a couple of further hints for debugging makefiles generated by `automake` effectively:

- If less verbose output has been enabled in the package with the use of silent rules (see How Automake can help in silencing Make), you’ll probably want undo that and see the actual commands being run: see Unsilencing Automake.
- `make -n` can help show what would be done without actually doing it. However, this *still executes* commands prefixed with ‘+’, and, when using GNU `make`, commands that contain the strings ‘$(MAKE)’ or ‘${MAKE}’ (see Instead of Execution in *The GNU Make Manual*). Typically, this is helpful to show what recursive rules would do, but it means that, in your own rules, you should not mix such recursion with actions that change any files.6 Furthermore, GNU `make` will update prerequisites for the Makefile file itself even with -n (see Remaking Makefiles in *The GNU Make Manual*).
- `make SHELL="/bin/bash -vx"` can help debug complex rules. See The Make Macro SHELL in *The Autoconf Manual*, for some portability quirks associated with this construct.
- `echo 'print: ; @echo "$(VAR)"' | make -f Makefile -f - print` can be handy to examine the expanded value of variables. You may need to use a target other than ‘print’ if that is already used or a file with that name exists.
- http://bashdb.sourceforge.net/remake/ provides a modified GNU `make` command called `remake` that copes with complex GNU `make`-specific Makefiles and allows tracing execution, examining variables, and calling rules interactively, much like a debugger.

### 26.11 Reporting Bugs

Most nontrivial software has bugs. Automake is no exception. We cannot promise we can or will fix a bug, and we might not even agree that it is a bug, but we want to hear about problems you encounter. Often we agree they are bugs and want to fix them.

So, to make it possible for us to fix a bug, please report it. If you can, though, it is helpful if you check if it is already known. You can look at the GNU Bug Tracker and the bug-automake mailing list archives for previous bug reports. (We previously used a Gnats database for bug tracking, but it is no longer online.)

If the bug is not already known, it should be reported. To report bugs in a way that is useful and efficient, please read How to Report Bugs Effectively and How to Ask Questions the Smart Way. Good bug reports save time for everyone.

For a bug report, a feature request or other suggestions, please send email to bug-automake@gnu.org. This will then open a new bug in the bug tracker. Be sure to include the versions of Autoconf and Automake that you use and the kind of system you’re on. Ideally, post a minimal Makefile.am and configure.ac that reproduces the problem you encounter. If you have encountered test suite failures, please attach the test-suite.log file.

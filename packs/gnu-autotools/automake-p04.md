---
title: "automake (part 4/14)"
source: https://www.gnu.org/software/automake/manual/automake.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 4/14
---

## 7 Directories

For simple projects that distribute all files in the same directory it is enough to have a single Makefile.am that builds everything in place.

In larger projects, it is common to organize files in different directories, in a tree. For example, there could be a directory for the program’s source, one for the testsuite, and one for the documentation; or, for very large projects, there could be one directory per program, per library or per module.

The traditional approach is to build these subdirectories recursively, employing *make recursion*: each directory contains its own Makefile, and when `make` is run from the top-level directory, it enters each subdirectory in turn, and invokes there a new `make` instance to build the directory’s contents.

Because this approach is very widespread, Automake offers built-in support for it. However, it is worth noting that the use of make recursion has its own serious issues and drawbacks, and that it’s well possible to have packages with a multi directory layout that make little or no use of such recursion (examples of such packages are GNU Bison and GNU Automake itself); see also the An Alternative Approach to Subdirectories section below.

### 7.1 Recursing subdirectories

In packages using make recursion, the top level Makefile.am must tell Automake which subdirectories are to be built. This is done via the `SUBDIRS` variable.

The `SUBDIRS` variable holds a list of subdirectories in which building of various sorts can occur. The rules for many targets (e.g., `all`) in the generated Makefile will run commands both locally and in all specified subdirectories. Note that the directories listed in `SUBDIRS` are not required to contain Makefile.ams; only Makefiles (after configuration). This allows inclusion of libraries from packages that do not use Automake (such as `gettext`; see also Third-Party Makefiles).

In packages that use subdirectories, the top-level Makefile.am is often very short. For instance, here is the Makefile.am from the GNU Hello distribution:

```
EXTRA_DIST = BUGS ChangeLog.O README-alpha
SUBDIRS = doc intl po src tests
```

When Automake invokes `make` in a subdirectory, it uses the value of the `MAKE` variable. It passes the value of the variable `AM_MAKEFLAGS` to the `make` invocation; this can be set in Makefile.am if there are flags you must always pass to `make`.

The directories mentioned in `SUBDIRS` are usually direct children of the current directory, each subdirectory containing its own Makefile.am with a `SUBDIRS` pointing to deeper subdirectories. Automake can be used to construct packages of arbitrary depth this way.

By default, Automake generates Makefiles that work depth-first in postfix order: the subdirectories are built before the current directory. However, it is possible to change this ordering. You can do this by putting ‘.’ into `SUBDIRS`. For instance, putting ‘.’ first will cause a prefix ordering of directories.

Using

```
SUBDIRS = lib src . test
```

will cause lib/ to be built before src/, then the current directory will be built, finally the test/ directory will be built. It is customary to arrange test directories to be built after everything else since they are meant to test what has been constructed.

In addition to the built-in recursive targets defined by Automake (`all`, `check`, etc.), the developer can also define his own recursive targets. That is done by passing the names of such targets as arguments to the M4 macro `AM_EXTRA_RECURSIVE_TARGETS` in configure.ac. Automake generates rules to handle the recursion for such targets; and the developer can define real actions for them by defining corresponding `-local` targets.

```
% cat configure.ac
AC_INIT([pkg-name], [1.0])
AM_INIT_AUTOMAKE
AM_EXTRA_RECURSIVE_TARGETS([foo])
AC_CONFIG_FILES([Makefile sub/Makefile sub/src/Makefile])
AC_OUTPUT
% cat Makefile.am
SUBDIRS = sub
foo-local:
        @echo This will be run by "make foo".
% cat sub/Makefile.am
SUBDIRS = src
% cat sub/src/Makefile.am
foo-local:
        @echo This too will be run by a "make foo" issued either in
        @echo the 'sub/src/' directory, the 'sub/' directory, or the
        @echo top-level directory.
```

### 7.2 Conditional Subdirectories

It is possible to define the `SUBDIRS` variable conditionally if, like in the case of GNU Inetutils, you want to only build a subset of the entire package.

To illustrate how this works, let’s assume we have two directories, src/ and opt/. src/ should always be built, but we want to decide in `configure` whether opt/ will be built or not. (For this example we will assume that opt/ should be built when the variable ‘$want_opt’ was set to ‘yes’.)

Running `make` should thus recurse into src/ always, and then maybe in opt/.

However ‘make dist’ should always recurse into both src/ and opt/, because opt/ should be distributed even if it is not needed in the current configuration. This means opt/Makefile should be created *unconditionally*.

There are two ways to set up a project like this. You can use Automake conditionals (see Conditionals) or use Autoconf `AC_SUBST` variables (see Setting Output Variables in *The Autoconf Manual*). Using Automake conditionals is the preferred solution. Before we illustrate these two possibilities, let’s introduce `DIST_SUBDIRS`.

#### 7.2.1 `SUBDIRS` vs. `DIST_SUBDIRS`

Automake considers two sets of directories, defined by the variables `SUBDIRS` and `DIST_SUBDIRS`.

`SUBDIRS` contains the subdirectories of the current directory that must be built (see Recursing subdirectories). It must be defined manually; Automake will never guess a directory is to be built. As we will see in the next two sections, it is possible to define it conditionally so that some directory will be omitted from the build.

`DIST_SUBDIRS` is used in rules that need to recurse in all directories, even those that have been conditionally left out of the build. Recall our example where we may not want to build subdirectory opt/, but yet we want to distribute it? This is where `DIST_SUBDIRS` comes into play: ‘opt’ may not appear in `SUBDIRS`, but it must appear in `DIST_SUBDIRS`.

Precisely, `DIST_SUBDIRS` is used by ‘make maintainer-clean’, ‘make distclean’ and ‘make dist’. All other recursive rules use `SUBDIRS`.

If `SUBDIRS` is defined conditionally using Automake conditionals, Automake will define `DIST_SUBDIRS` automatically from the possible values of `SUBDIRS` in all conditions.

If `SUBDIRS` contains `AC_SUBST` variables, `DIST_SUBDIRS` will not be defined correctly because Automake does not know the possible values of these variables. In this case `DIST_SUBDIRS` needs to be defined manually.

#### 7.2.2 Subdirectories with `AM_CONDITIONAL`

configure should output the Makefile for each directory and define a condition into which opt/ should be built.

```
...
AM_CONDITIONAL([COND_OPT], [test "$want_opt" = yes])
AC_CONFIG_FILES([Makefile src/Makefile opt/Makefile])
...
```

Then `SUBDIRS` can be defined in the top-level Makefile.am as follows.

```
if COND_OPT
  MAYBE_OPT = opt
endif
SUBDIRS = src $(MAYBE_OPT)
```

As you can see, running `make` will rightly recurse into src/ and maybe opt/.

As you can’t see, running ‘make dist’ will recurse into both src/ and opt/ directories because ‘make dist’, unlike ‘make all’, doesn’t use the `SUBDIRS` variable. It uses the `DIST_SUBDIRS` variable.

In this case Automake will define ‘DIST_SUBDIRS = src opt’ automatically because it knows that `MAYBE_OPT` can contain ‘opt’ in some condition.

#### 7.2.3 Subdirectories with `AC_SUBST`

Another possibility is to define `MAYBE_OPT` from ./configure using `AC_SUBST`:

```
...
if test "$want_opt" = yes; then
  MAYBE_OPT=opt
else
  MAYBE_OPT=
fi
AC_SUBST([MAYBE_OPT])
AC_CONFIG_FILES([Makefile src/Makefile opt/Makefile])
...
```

In this case the top-level Makefile.am should look as follows.

```
SUBDIRS = src $(MAYBE_OPT)
DIST_SUBDIRS = src opt
```

The drawback is that since Automake cannot guess what the possible values of `MAYBE_OPT` are, it is necessary to define `DIST_SUBDIRS`.

#### 7.2.4 Unconfigured Subdirectories

The semantics of `DIST_SUBDIRS` are often misunderstood by some users that try to *configure and build* subdirectories conditionally. Here by configuring we mean creating the Makefile (it might also involve running a nested `configure` script: this is a costly operation that explains why people want to do it conditionally, but only the Makefile is relevant to the discussion).

The above examples all assume that every Makefile is created, even in directories that are not going to be built. The simple reason is that we want ‘make dist’ to distribute even the directories that are not being built (e.g., platform-dependent code), hence make dist must recurse into the subdirectory, hence this directory must be configured and appear in `DIST_SUBDIRS`.

Building packages that do not configure every subdirectory is a tricky business, and we do not recommend it to the novice as it is easy to produce an incomplete tarball by mistake. We will not discuss this topic in depth here, yet for the adventurous here are a few rules to remember.

| `SUBDIRS` should always be a subset of `DIST_SUBDIRS`. It makes little sense to have a directory in `SUBDIRS` that is not in `DIST_SUBDIRS`. Think of the former as a way to tell which directories listed in the latter should be built. Any directory listed in `DIST_SUBDIRS` and `SUBDIRS` must be configured. That is, the Makefile must exist or the recursive `make` rules will not be able to process the directory. Any configured directory must be listed in `DIST_SUBDIRS`. This is so the cleaning rules remove the generated Makefiles. It would be correct to see `DIST_SUBDIRS` as a variable that lists all the directories that have been configured. |
|---|

In order to prevent recursion in some unconfigured directory you must therefore ensure that this directory does not appear in `DIST_SUBDIRS` (and `SUBDIRS`). For instance, if you define `SUBDIRS` conditionally using `AC_SUBST` and do not define `DIST_SUBDIRS` explicitly, it will be default to ‘$(SUBDIRS)’; another possibility is to force `DIST_SUBDIRS = $(SUBDIRS)`.

Of course, directories that are omitted from `DIST_SUBDIRS` will not be distributed unless you make other arrangements for this to happen (for instance, always running ‘make dist’ in a configuration where all directories are known to appear in `DIST_SUBDIRS`; or writing a `dist-hook` target to distribute these directories).

In a few packages, unconfigured directories are not even expected to be distributed. Although these packages do not require the aforementioned extra arrangements, there is another pitfall. If the name of a directory appears in `SUBDIRS` or `DIST_SUBDIRS`, `automake` will make sure the directory exists. Consequently `automake` cannot be run on such a distribution when one directory has been omitted. One way to avoid this check is to use the `AC_SUBST` method to declare conditional directories; since `automake` does not know the values of `AC_SUBST` variables it cannot ensure the corresponding directory exists.

### 7.3 An Alternative Approach to Subdirectories

If you’ve ever read Peter Miller’s excellent paper, *Recursive Make Considered Harmful*, the preceding sections on the use of make recursion will probably come as unwelcome advice. For those who haven’t read the paper, Miller’s main thesis is that recursive `make` invocations are both slow and error-prone.

Automake is intended to have sufficient cross-directory support to enable you to write a single Makefile.am for a complex multi-directory package. (If it seems to be lacking, please report the issue as usual.)

By default an installable file specified in a subdirectory will have its directory name stripped before installation. For instance, in this example, the header file will be installed as $(includedir)/stdio.h:

```
include_HEADERS = inc/stdio.h
```

However, the ‘nobase_’ prefix can be used to circumvent this path stripping. In this example, the header file will be installed as $(includedir)/sys/types.h:

```
nobase_include_HEADERS = sys/types.h
```

‘nobase_’ should be specified first when used in conjunction with either ‘dist_’ or ‘nodist_’ (see Fine-grained Distribution Control). For instance:

```
nobase_dist_pkgdata_DATA = images/vortex.pgm sounds/whirl.ogg
```

Finally, note that a variable using the ‘nobase_’ prefix can often be replaced by several variables, one for each destination directory (see The Uniform Naming Scheme). For instance, the last example could be rewritten as follows:

```
imagesdir = $(pkgdatadir)/images
soundsdir = $(pkgdatadir)/sounds
dist_images_DATA = images/vortex.pgm
dist_sounds_DATA = sounds/whirl.ogg
```

This latter syntax makes it possible to change one destination directory without changing the layout of the source tree.

Currently, ‘nobase_*_LTLIBRARIES’ are the only exception to this rule, in that there is no particular installation order guarantee for an otherwise equivalent set of variables without ‘nobase_’ prefix.

### 7.4 Nesting Packages

In the GNU Build System, packages can be nested to arbitrary depth. This means that a package can embed other packages with their own configure, Makefiles, etc.

These other packages should just appear as subdirectories of their parent package. They must be listed in `SUBDIRS` like other ordinary directories. However the subpackage’s Makefiles should be output by its own configure script, not by the parent’s configure. This is achieved using the `AC_CONFIG_SUBDIRS` Autoconf macro (see Configuring Other Packages in Subdirectories in *The Autoconf Manual*).

Here is an example package for an `arm` program that links with a `hand` library that is a nested package in subdirectory hand/.

`arm`’s configure.ac:

```
AC_INIT([arm], [1.0])
AC_CONFIG_AUX_DIR([.])
AM_INIT_AUTOMAKE
AC_PROG_CC
AC_CONFIG_FILES([Makefile])
# Call hand's ./configure script recursively.
AC_CONFIG_SUBDIRS([hand])
AC_OUTPUT
```

`arm`’s Makefile.am:

```
# Build the library in the hand subdirectory first.
SUBDIRS = hand

# Include hand's header when compiling this directory.
AM_CPPFLAGS = -I$(srcdir)/hand

bin_PROGRAMS = arm
arm_SOURCES = arm.c
# link with the hand library.
arm_LDADD = hand/libhand.a
```

Now here is `hand`’s hand/configure.ac:

```
AC_INIT([hand], [1.2])
AC_CONFIG_AUX_DIR([.])
AM_INIT_AUTOMAKE
AC_PROG_CC
AM_PROG_AR
AC_PROG_RANLIB
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
```

and its hand/Makefile.am:

```
lib_LIBRARIES = libhand.a
libhand_a_SOURCES = hand.c
```

When ‘make dist’ is run from the top-level directory it will create an archive arm-1.0.tar.gz that contains the `arm` code as well as the hand subdirectory. This package can be built and installed like any ordinary package, with the usual ‘./configure && make && make install’ sequence (the `hand` subpackage will be built and installed by the process).

When ‘make dist’ is run from the hand directory, it will create a self-contained hand-1.2.tar.gz archive. So although it appears to be embedded in another package, it can still be used separately.

The purpose of the ‘AC_CONFIG_AUX_DIR([.])’ instruction is to force Automake and Autoconf to search for auxiliary scripts in the current directory. For instance, this means that there will be two copies of install-sh: one in the top-level of the `arm` package, and another one in the hand/ subdirectory for the `hand` package.

The historical default is to search for these auxiliary scripts in the parent directory and the grandparent directory. So if the ‘AC_CONFIG_AUX_DIR([.])’ line was removed from hand/configure.ac, that subpackage would share the auxiliary script of the `arm` package. This may look like a gain in size (a few kilobytes), but more importantly, it is a loss of modularity as the `hand` subpackage is no longer self-contained (‘make dist’ in the subdirectory will not work anymore).

Packages that do not use Automake need more work to be integrated this way. See Third-Party Makefiles.

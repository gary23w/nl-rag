---
title: "Autoconf (part 21/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 21/26
---

# Autoconf

Aside from the fact that `AC_CONFIG_COMMANDS` requires an additional key, an important difference is that `AC_OUTPUT_COMMANDS` is quoting its arguments twice, unlike `AC_CONFIG_COMMANDS`. This means that `AC_CONFIG_COMMANDS` can safely be given macro calls as arguments:

```
AC_CONFIG_COMMANDS(foo, [my_FOO()])
```

Conversely, where one level of quoting was enough for literal strings with `AC_OUTPUT_COMMANDS`, you need two with `AC_CONFIG_COMMANDS`. The following lines are equivalent:

```
AC_OUTPUT_COMMANDS([echo "Square brackets: []"])
AC_CONFIG_COMMANDS([default], [[echo "Square brackets: []"]])
```

**Macro: **AC_PID_T** ¶**

Replaced by `AC_TYPE_PID_T` (see AC_TYPE_PID_T).

**Macro: **AC_PREFIX** ¶**

Replaced by `AC_PREFIX_PROGRAM` (see AC_PREFIX_PROGRAM).

**Macro: **AC_PROG_CC_C89** ¶**

Now done by `AC_PROG_CC` (see AC_PROG_CC).

**Macro: **AC_PROG_CC_C99** ¶**

Now done by `AC_PROG_CC` (see AC_PROG_CC).

**Macro: **AC_PROG_CC_STDC** ¶**

Now done by `AC_PROG_CC` (see AC_PROG_CC).

**Macro: **AC_PROG_GCC_TRADITIONAL** ¶**

Used to put GCC into “traditional” (pre-ISO C) compilation mode, on systems with headers that did not work correctly with a standard-compliant compiler. GCC has not supported traditional compilation in many years, and all of the systems that required this are long obsolete themselves. This macro is now a compatibility synonym for `AC_PROG_CC` (see AC_PROG_CC).

**Macro: **AC_PROGRAMS_CHECK** ¶**

Replaced by `AC_CHECK_PROGS` (see AC_CHECK_PROGS).

**Macro: **AC_PROGRAMS_PATH** ¶**

Replaced by `AC_PATH_PROGS` (see AC_PATH_PROGS).

**Macro: **AC_PROGRAM_CHECK** ¶**

Replaced by `AC_CHECK_PROG` (see AC_CHECK_PROG).

**Macro: **AC_PROGRAM_EGREP** ¶**

Replaced by `AC_EGREP_CPP` (see AC_EGREP_CPP).

**Macro: **AC_PROGRAM_PATH** ¶**

Replaced by `AC_PATH_PROG` (see AC_PATH_PROG).

**Macro: **AC_REMOTE_TAPE** ¶**

Removed because of limited usefulness.

**Macro: **AC_RESTARTABLE_SYSCALLS** ¶**

This macro was renamed `AC_SYS_RESTARTABLE_SYSCALLS`. However, these days portable programs should use `sigaction` with `SA_RESTART` if they want restartable system calls. They should not rely on `HAVE_RESTARTABLE_SYSCALLS`, since nowadays whether a system call is restartable is a dynamic issue, not a configuration-time issue.

**Macro: **AC_RETSIGTYPE** ¶**

Replaced by `AC_TYPE_SIGNAL` (see AC_TYPE_SIGNAL), which itself is obsolete.

**Macro: **AC_RSH** ¶**

Removed because of limited usefulness.

**Macro: **AC_SCO_INTL** ¶**

Equivalent to the obsolescent macro `AC_FUNC_STRFTIME`. See AC_FUNC_STRFTIME.

**Macro: **AC_SETVBUF_REVERSED** ¶**

Replaced by

```
AC_FUNC_SETVBUF_REVERSED
```

See AC_FUNC_SETVBUF_REVERSED.

**Macro: **AC_SET_MAKE** ¶**

Replaced by `AC_PROG_MAKE_SET` (see AC_PROG_MAKE_SET).

**Macro: **AC_SIZEOF_TYPE** ¶**

Replaced by `AC_CHECK_SIZEOF` (see AC_CHECK_SIZEOF).

**Macro: **AC_SIZE_T** ¶**

Replaced by `AC_TYPE_SIZE_T` (see AC_TYPE_SIZE_T).

**Macro: **AC_STAT_MACROS_BROKEN** ¶**

Replaced by `AC_HEADER_STAT` (see AC_HEADER_STAT).

**Macro: **AC_STDC_HEADERS** ¶**

Replaced by `AC_HEADER_STDC` (see AC_HEADER_STDC), which is itself obsolete. Nowadays it is safe to assume the facilities of C89 exist.

**Macro: **AC_STRCOLL** ¶**

Replaced by `AC_FUNC_STRCOLL` (see AC_FUNC_STRCOLL).

**Macro: **AC_STRUCT_ST_BLKSIZE** ¶**

If `struct stat` contains an `st_blksize` member, define `HAVE_STRUCT_STAT_ST_BLKSIZE`. The former name, `HAVE_ST_BLKSIZE` is to be avoided, as its support will cease in the future. This macro is obsoleted, and should be replaced by

```
AC_CHECK_MEMBERS([struct stat.st_blksize])
```

See AC_CHECK_MEMBERS.

**Macro: **AC_STRUCT_ST_RDEV** ¶**

If `struct stat` contains an `st_rdev` member, define `HAVE_STRUCT_STAT_ST_RDEV`. The former name for this macro, `HAVE_ST_RDEV`, is to be avoided as it will cease to be supported in the future. Actually, even the new macro is obsolete and should be replaced by:

```
AC_CHECK_MEMBERS([struct stat.st_rdev])
```

See AC_CHECK_MEMBERS.

**Macro: **AC_ST_BLKSIZE** ¶**

Replaced by `AC_CHECK_MEMBERS` (see AC_CHECK_MEMBERS).

**Macro: **AC_ST_BLOCKS** ¶**

Replaced by `AC_STRUCT_ST_BLOCKS` (see AC_STRUCT_ST_BLOCKS).

**Macro: **AC_ST_RDEV** ¶**

Replaced by `AC_CHECK_MEMBERS` (see AC_CHECK_MEMBERS).

**Macro: **AC_SYS_RESTARTABLE_SYSCALLS** ¶**

If the system automatically restarts a system call that is interrupted by a signal, define `HAVE_RESTARTABLE_SYSCALLS`. This macro does not check whether system calls are restarted in general—it checks whether a signal handler installed with `signal` (but not `sigaction`) causes system calls to be restarted. It does not check whether system calls can be restarted when interrupted by signals that have no handler.

These days portable programs should use `sigaction` with `SA_RESTART` if they want restartable system calls. They should not rely on `HAVE_RESTARTABLE_SYSCALLS`, since nowadays whether a system call is restartable is a dynamic issue, not a configuration-time issue.

**Macro: **AC_SYS_SIGLIST_DECLARED** ¶**

This macro was renamed `AC_DECL_SYS_SIGLIST`. However, even that name is obsolete, as the same functionality is now achieved via `AC_CHECK_DECLS` (see AC_CHECK_DECLS).

**Macro: **AC_TEST_CPP** ¶**

This macro was renamed `AC_TRY_CPP`, which in turn was replaced by `AC_PREPROC_IFELSE` (see AC_PREPROC_IFELSE).

**Macro: **AC_TEST_PROGRAM** ¶**

This macro was renamed `AC_TRY_RUN`, which in turn was replaced by `AC_RUN_IFELSE` (see AC_RUN_IFELSE).

**Macro: **AC_TIMEZONE** ¶**

Replaced by `AC_STRUCT_TIMEZONE` (see AC_STRUCT_TIMEZONE).

**Macro: **AC_TIME_WITH_SYS_TIME** ¶**

Replaced by `AC_HEADER_TIME` (see AC_HEADER_TIME), which is itself obsolete; nowadays one need only do ‘AC_CHECK_HEADERS([sys/time.h])’.

**Macro: **AC_TRY_COMPILE***(*includes*, *function-body*, [*action-if-true*], [*action-if-false*])* ¶**

Same as:

```
AC_COMPILE_IFELSE(
  [AC_LANG_PROGRAM([[includes]],
     [[function-body]])],
  [action-if-true],
  [action-if-false])
```

See Running the Compiler.

This macro double quotes both *includes* and *function-body*.

For C and C++, *includes* is any `#include` statements needed by the code in *function-body* (*includes* is ignored if the currently selected language is Fortran or Fortran 77). The compiler and compilation flags are determined by the current language (see Language Choice).

**Macro: **AC_TRY_CPP***(*input*, [*action-if-true*], [*action-if-false*])* ¶**

Same as:

```
AC_PREPROC_IFELSE(
  [AC_LANG_SOURCE([[input]])],
  [action-if-true],
  [action-if-false])
```

See Running the Preprocessor.

This macro double quotes the *input*.

**Macro: **AC_TRY_LINK***(*includes*, *function-body*, [*action-if-true*], [*action-if-false*])* ¶**

Same as:

```
AC_LINK_IFELSE(
  [AC_LANG_PROGRAM([[includes]],
     [[function-body]])],
  [action-if-true],
  [action-if-false])
```

See Running the Linker.

This macro double quotes both *includes* and *function-body*.

Depending on the current language (see Language Choice), create a test program to see whether a function whose body consists of *function-body* can be compiled and linked. If the file compiles and links successfully, run shell commands *action-if-found*, otherwise run *action-if-not-found*.

This macro double quotes both *includes* and *function-body*.

For C and C++, *includes* is any `#include` statements needed by the code in *function-body* (*includes* is ignored if the currently selected language is Fortran or Fortran 77). The compiler and compilation flags are determined by the current language (see Language Choice), and in addition `LDFLAGS` and `LIBS` are used for linking.

**Macro: **AC_TRY_LINK_FUNC***(*function*, [*action-if-found*], [*action-if-not-found*])* ¶**

This macro is equivalent to

```
AC_LINK_IFELSE([AC_LANG_CALL([], [function])],
  [action-if-found], [action-if-not-found])
```

See Running the Linker.

**Macro: **AC_TRY_RUN***(*program*, [*action-if-true*], [*action-if-false*], [*action-if-cross-compiling* = ‘AC_MSG_FAILURE’])* ¶**

Same as:

```
AC_RUN_IFELSE(
  [AC_LANG_SOURCE([[program]])],
  [action-if-true],
  [action-if-false],
  [action-if-cross-compiling])
```

See Checking Runtime Behavior.

**Macro: **AC_TYPE_SIGNAL** ¶**

If signal.h declares `signal` as returning a pointer to a function returning `void`, define `RETSIGTYPE` to be `void`; otherwise, define it to be `int`. These days, it is portable to assume C89, and that signal handlers return `void`, without needing to use this macro or `RETSIGTYPE`.

**Macro: **AC_UID_T** ¶**

Replaced by `AC_TYPE_UID_T` (see AC_TYPE_UID_T).

**Macro: **AC_UNISTD_H** ¶**

Same as ‘AC_CHECK_HEADERS([unistd.h])’ (see AC_CHECK_HEADERS), which is one of the tests done as a side effect by `AC_INCLUDES_DEFAULT` (see Default Includes), so usually unnecessary to write explicitly.

**Macro: **AC_USG** ¶**

Define `USG` if the BSD string functions (`bcopy`, `bzero`, `index`, `rindex`, etc) are *not* defined in strings.h. Modern code should assume string.h exists and should use the standard C string functions (`memmove`, `memset`, `strchr`, `strrchr`, etc) unconditionally.

strings.h may be the only header that declares `strcasecmp`, `strncasecmp`, and `ffs`. `AC_INCLUDES_DEFAULT` checks for it (see Default Includes); test `HAVE_STRINGS_H`.

**Macro: **AC_UTIME_NULL** ¶**

Replaced by `AC_FUNC_UTIME_NULL` (see AC_FUNC_UTIME_NULL).

**Macro: **AC_VALIDATE_CACHED_SYSTEM_TUPLE***([*cmd*])* ¶**

If the cache file is inconsistent with the current host, target and build system types, it used to execute *cmd* or print a default error message. This is now handled by default.

**Macro: **AC_VERBOSE***(*result-description*)* ¶**

Replaced by `AC_MSG_RESULT` (see AC_MSG_RESULT).

**Macro: **AC_VFORK** ¶**

Replaced by `AC_FUNC_FORK` (see AC_FUNC_FORK).

**Macro: **AC_VPRINTF** ¶**

Replaced by `AC_FUNC_VPRINTF` (see AC_FUNC_VPRINTF).

**Macro: **AC_WAIT3** ¶**

This macro was renamed `AC_FUNC_WAIT3`. However, these days portable programs should use `waitpid`, not `wait3`, as `wait3` has been removed from POSIX.

**Macro: **AC_WARN** ¶**

Replaced by `AC_MSG_WARN` (see AC_MSG_WARN).

**Macro: **AC_WARNING***(*message*)* ¶**

Replaced by `m4_warn` (see m4_warn).

**Macro: **AC_WITH***(*package*, *action-if-given*, [*action-if-not-given*])* ¶**

This is an obsolete version of `AC_ARG_WITH` that does not support providing a help string (see AC_ARG_WITH).

**Macro: **AC_WORDS_BIGENDIAN** ¶**

Replaced by `AC_C_BIGENDIAN` (see AC_C_BIGENDIAN).

**Macro: **AC_XENIX_DIR** ¶**

This macro is equivalent to the obsolescent `AC_HEADER_DIRENT` macro, plus it also sets the shell variable `XENIX`. Don’t use this macro, the dignified means to check the nature of the host is using `AC_CANONICAL_HOST` (see Getting the Canonical System Type).

**Macro: **AC_YYTEXT_POINTER** ¶**

This macro was renamed `AC_DECL_YYTEXT`, which in turn was integrated into `AC_PROG_LEX` (see AC_PROG_LEX).

### 18.5 Upgrading From Version 1

Autoconf version 2 is mostly backward compatible with version 1. However, it introduces better ways to do some things, and doesn’t support some of the ugly things in version 1. So, depending on how sophisticated your configure.ac files are, you might have to do some manual work in order to upgrade to version 2. This chapter points out some problems to watch for when upgrading. Also, perhaps your `configure` scripts could benefit from some of the new features in version 2; the changes are summarized in the file NEWS in the Autoconf distribution.

#### 18.5.1 Changed File Names

If you have an aclocal.m4 installed with Autoconf (as opposed to in a particular package’s source directory), you must rename it to acsite.m4. See Using `autoconf` to Create `configure`.

If you distribute install.sh with your package, rename it to install-sh so `make` builtin rules don’t inadvertently create a file called install from it. `AC_PROG_INSTALL` looks for the script under both names, but it is best to use the new name.

If you were using config.h.top, config.h.bot, or acconfig.h, you still can, but you have less clutter if you use the `AH_` macros. See Autoheader Macros.

#### 18.5.2 Changed Makefiles

Add ‘@CFLAGS@’, ‘@CPPFLAGS@’, and ‘@LDFLAGS@’ in your Makefile.in files, so they can take advantage of the values of those variables in the environment when `configure` is run. Doing this isn’t necessary, but it’s a convenience for users.

Also add ‘@configure_input@’ in a comment to each input file for `AC_OUTPUT`, so that the output files contain a comment saying they were produced by `configure`. Automatically selecting the right comment syntax for all the kinds of files that people call `AC_OUTPUT` on became too much work.

Add config.log and config.cache to the list of files you remove in `distclean` targets.

If you have the following in Makefile.in:

```
prefix = /usr/local
exec_prefix = $(prefix)
```

you must change it to:

```
prefix = @prefix@
exec_prefix = @exec_prefix@
```

The old behavior of replacing those variables without ‘@’ characters around them has been removed.

#### 18.5.3 Changed Macros

Many of the macros were renamed in Autoconf version 2. You can still use the old names, but the new ones are clearer, and it’s easier to find the documentation for them. See Obsolete Macros, for a table showing the new names for the old macros. Use the `autoupdate` program to convert your configure.ac to using the new macro names. See Using `autoupdate` to Modernize configure.ac.

Some macros have been superseded by similar ones that do the job better, but are not call-compatible. If you get warnings about calling obsolete macros while running `autoconf`, you may safely ignore them, but your `configure` script generally works better if you follow the advice that is printed about what to replace the obsolete macros with. In particular, the mechanism for reporting the results of tests has changed. If you were using `echo` or `AC_VERBOSE` (perhaps via `AC_COMPILE_CHECK`), your `configure` script’s output looks better if you switch to `AC_MSG_CHECKING` and `AC_MSG_RESULT`. See Printing Messages. Those macros work best in conjunction with cache variables. See Caching Results.

#### 18.5.4 Changed Results

If you were checking the results of previous tests by examining the shell variable `DEFS`, you need to switch to checking the values of the cache variables for those tests. `DEFS` no longer exists while `configure` is running; it is only created when generating output files. This difference from version 1 is because properly quoting the contents of that variable turned out to be too cumbersome and inefficient to do every time `AC_DEFINE` is called. See Cache Variable Names.

For example, here is a configure.ac fragment written for Autoconf version 1:

```
AC_HAVE_FUNCS(syslog)
case "$DEFS" in
*-DHAVE_SYSLOG*) ;;
*) # syslog is not in the default libraries.  See if it's in some other.
  saved_LIBS="$LIBS"
  for lib in bsd socket inet; do
    AC_CHECKING(for syslog in -l$lib)
    LIBS="-l$lib $saved_LIBS"
    AC_HAVE_FUNCS(syslog)
    case "$DEFS" in
    *-DHAVE_SYSLOG*) break ;;
    *) ;;
    esac
    LIBS="$saved_LIBS"
  done ;;
esac
```

Here is a way to write it for version 2:

```
AC_CHECK_FUNCS([syslog])
AS_IF([test "x$ac_cv_func_syslog" = xno],
  [# syslog is not in the default libraries.  See if it's in some other.
   for lib in bsd socket inet; do
     AC_CHECK_LIB([$lib], [syslog],
       [AC_DEFINE([HAVE_SYSLOG])
        LIBS="-l$lib $LIBS"; break])
   done])
```

If you were working around bugs in `AC_DEFINE_UNQUOTED` by adding backslashes before quotes, you need to remove them. It now works predictably, and does not treat quotes (except back quotes) specially. See Setting Output Variables.

All of the Boolean shell variables set by Autoconf macros now use ‘yes’ for the true value. Most of them use ‘no’ for false, though for backward compatibility some use the empty string instead. If you were relying on a shell variable being set to something like 1 or ‘t’ for true, you need to change your tests.

#### 18.5.5 Changed Macro Writing

When defining your own macros, you should now use `AC_DEFUN` instead of `define`. `AC_DEFUN` automatically calls `AC_PROVIDE` and ensures that macros called via `AC_REQUIRE` do not interrupt other macros, to prevent nested ‘checking…’ messages on the screen. There’s no actual harm in continuing to use the older way, but it’s less convenient and attractive. See Macro Definitions.

You probably looked at the macros that came with Autoconf as a guide for how to do things. It would be a good idea to take a look at the new versions of them, as the style is somewhat improved and they take advantage of some new features.

If you were doing tricky things with undocumented Autoconf internals (macros, variables, diversions), check whether you need to change anything to account for changes that have been made. Perhaps you can even use an officially supported technique in version 2 instead of kludging. Or perhaps not.

To speed up your locally written feature tests, add caching to them. See whether any of your tests are of general enough usefulness to encapsulate them into macros that you can share.

### 18.6 Upgrading From Version 2.13

The introduction of the previous section (see Upgrading From Version 1) perfectly suits this section...

> Autoconf version 2.50 is mostly backward compatible with version 2.13. However, it introduces better ways to do some things, and doesn’t support some of the ugly things in version 2.13. So, depending on how sophisticated your configure.ac files are, you might have to do some manual work in order to upgrade to version 2.50. This chapter points out some problems to watch for when upgrading. Also, perhaps your `configure` scripts could benefit from some of the new features in version 2.50; the changes are summarized in the file NEWS in the Autoconf distribution.

#### 18.6.1 Changed Quotation

The most important changes are invisible to you: the implementation of most macros have completely changed. This allowed more factorization of the code, better error messages, a higher uniformity of the user’s interface etc. Unfortunately, as a side effect, some construct which used to (miraculously) work might break starting with Autoconf 2.50. The most common culprit is bad quotation.

For instance, in the following example, the message is not properly quoted:

```
AC_INIT
AC_CHECK_HEADERS(foo.h, ,
  AC_MSG_ERROR(cannot find foo.h, bailing out))
AC_OUTPUT
```

Autoconf 2.13 simply ignores it:

```
$ autoconf-2.13; ./configure --silent
creating cache ./config.cache
configure: error: cannot find foo.h
$
```

while Autoconf 2.50 produces a broken configure:

```
$ autoconf-2.50; ./configure --silent
configure: error: cannot find foo.h
./configure: exit: bad non-numeric arg `bailing'
./configure: exit: bad non-numeric arg `bailing'
$
```

The message needs to be quoted, and the `AC_MSG_ERROR` invocation too!

```
AC_INIT([Example], [1.0], [bug-example@example.org])
AC_CHECK_HEADERS([foo.h], [],
  [AC_MSG_ERROR([cannot find foo.h, bailing out])])
AC_OUTPUT
```

Many many (and many more) Autoconf macros were lacking proper quotation, including no less than… `AC_DEFUN` itself!

```
$ cat configure.in
AC_DEFUN([AC_PROG_INSTALL],
[# My own much better version
])
AC_INIT
AC_PROG_INSTALL
AC_OUTPUT
$ autoconf-2.13
autoconf: Undefined macros:
***BUG in Autoconf--please report*** AC_FD_MSG
***BUG in Autoconf--please report*** AC_EPI
configure.in:1:AC_DEFUN([AC_PROG_INSTALL],
configure.in:5:AC_PROG_INSTALL
$ autoconf-2.50
$
```

#### 18.6.2 New Macros

While Autoconf was relatively dormant in the late 1990s, Automake provided Autoconf-like macros for a while. Starting with Autoconf 2.50 in 2001, Autoconf provided versions of these macros, integrated in the `AC_` namespace, instead of `AM_`. But in order to ease the upgrading via `autoupdate`, bindings to such `AM_` macros are provided.

Unfortunately older versions of Automake (e.g., Automake 1.4) did not quote the names of these macros. Therefore, when `m4` finds something like ‘AC_DEFUN(AM_TYPE_PTRDIFF_T, …)’ in aclocal.m4, `AM_TYPE_PTRDIFF_T` is expanded, replaced with its Autoconf definition.

Fortunately Autoconf catches pre-`AC_INIT` expansions, and complains, in its own words:

```
$ cat configure.ac
AC_INIT([Example], [1.0], [bug-example@example.org])
AM_TYPE_PTRDIFF_T
$ aclocal-1.4
$ autoconf
aclocal.m4:17: error: m4_defn: undefined macro: _m4_divert_diversion
aclocal.m4:17: the top level
autom4te: m4 failed with exit status: 1
$
```

Modern versions of Automake no longer define most of these macros, and properly quote the names of the remaining macros. If you must use an old Automake, do not depend upon macros from Automake as it is simply not its job to provide macros (but the one it requires itself):

```
$ cat configure.ac
AC_INIT([Example], [1.0], [bug-example@example.org])
AM_TYPE_PTRDIFF_T
$ rm aclocal.m4
$ autoupdate
autoupdate: 'configure.ac' is updated
$ cat configure.ac
AC_INIT([Example], [1.0], [bug-example@example.org])
AC_CHECK_TYPES([ptrdiff_t])
$ aclocal-1.4
$ autoconf
$
```

#### 18.6.3 Hosts and Cross-Compilation

Based on the experience of compiler writers, and after long public debates, many aspects of the cross-compilation chain have changed:

- the relationship between the build, host, and target architecture types,
- the command line interface for specifying them to `configure`,
- the variables defined in `configure`,
- the enabling of cross-compilation mode.

The relationship between build, host, and target have been cleaned up: the chain of default is now simply: target defaults to host, host to build, and build to the result of `config.guess`. Nevertheless, in order to ease the transition from 2.13 to 2.50, the following transition scheme is implemented. *Do not rely on it*, as it will be completely disabled in a couple of releases (we cannot keep it, as it proves to cause more problems than it cures).

They all default to the result of running `config.guess`, unless you specify either --build or --host. In this case, the default becomes the system type you specified. If you specify both, and they’re different, `configure` enters cross compilation mode, so it doesn’t run any tests that require execution.

Hint: if you mean to override the result of `config.guess`, prefer --build over --host.

For backward compatibility, `configure` accepts a system type as an option by itself. Such an option overrides the defaults for build, host, and target system types. The following configure statement configures a cross toolchain that runs on NetBSD/aarch64 but generates code for GNU Hurd/riscv64, which is also the build platform.

```
./configure --host=aarch64-netbsd riscv64-gnu
```

In Autoconf 2.13 and before, the variables `build`, `host`, and `target` had a different semantics before and after the invocation of `AC_CANONICAL_BUILD` etc. Now, the argument of --build is strictly copied into `build_alias`, and is left empty otherwise. After the `AC_CANONICAL_BUILD`, `build` is set to the canonicalized build type. To ease the transition, before, its contents is the same as that of `build_alias`. Do *not* rely on this broken feature.

For consistency with the backward compatibility scheme exposed above, when --host is specified but --build isn’t, the build system is assumed to be the same as --host, and ‘build_alias’ is set to that value. Eventually, this historically incorrect behavior will go away.

The former scheme to enable cross-compilation proved to cause more harm than good, in particular, it used to be triggered too easily, leaving regular end users puzzled in front of cryptic error messages. `configure` could even enter cross-compilation mode only because the compiler was not functional. This is mainly because `configure` used to try to detect cross-compilation, instead of waiting for an explicit flag from the user.

Now, `configure` enters cross-compilation mode if and only if --host is passed.

That’s the short documentation. To ease the transition between 2.13 and its successors, a more complicated scheme is implemented. *Do not rely on the following*, as it will be removed in the near future.

If you specify --host, but not --build, when `configure` performs the first compiler test it tries to run an executable produced by the compiler. If the execution fails, it enters cross-compilation mode. This is fragile. Moreover, by the time the compiler test is performed, it may be too late to modify the build-system type: other tests may have already been performed. Therefore, whenever you specify --host, be sure to specify --build too.

```
./configure --build=x86_64-pc-linux-gnu --host=x86_64-w64-mingw64
```

enters cross-compilation mode. The former interface, which consisted in setting the compiler to a cross-compiler without informing `configure` is obsolete. For instance, `configure` fails if it can’t run the code generated by the specified compiler if you configure as follows:

```
./configure CC=x86_64-w64-mingw64-gcc
```

#### 18.6.4 `AC_LIBOBJ` vs. `LIBOBJS`

Up to Autoconf 2.13, the replacement of functions was triggered via the variable `LIBOBJS`. Since Autoconf 2.50, the macro `AC_LIBOBJ` should be used instead (see Generic Function Checks). Starting at Autoconf 2.53, the use of `LIBOBJS` is an error.

This change is mandated by the unification of the GNU Build System components. In particular, the various fragile techniques used to parse a configure.ac are all replaced with the use of traces. As a consequence, any action must be traceable, which obsoletes critical variable assignments. Fortunately, `LIBOBJS` was the only problem, and it can even be handled gracefully (read, “without your having to change something”).

There were two typical uses of `LIBOBJS`: asking for a replacement function, and adjusting `LIBOBJS` for Automake and/or Libtool.

As for function replacement, the fix is immediate: use `AC_LIBOBJ`. For instance:

```
LIBOBJS="$LIBOBJS fnmatch.o"
LIBOBJS="$LIBOBJS malloc.$ac_objext"
```

should be replaced with:

```
AC_LIBOBJ([fnmatch])
AC_LIBOBJ([malloc])
```

When used with Automake 1.10 or newer, a suitable value for `LIBOBJDIR` is set so that the `LIBOBJS` and `LTLIBOBJS` can be referenced from any Makefile.am. Even without Automake, arranging for `LIBOBJDIR` to be set correctly enables referencing `LIBOBJS` and `LTLIBOBJS` in another directory. The `LIBOBJDIR` feature is experimental.

#### 18.6.5 `AC_*ACT*_IFELSE` vs. `AC_TRY_*ACT*`

Since Autoconf 2.50, internal codes uses `AC_PREPROC_IFELSE`, `AC_COMPILE_IFELSE`, `AC_LINK_IFELSE`, and `AC_RUN_IFELSE` on one hand and `AC_LANG_SOURCE`, and `AC_LANG_PROGRAM` on the other hand instead of the deprecated `AC_TRY_CPP`, `AC_TRY_COMPILE`, `AC_TRY_LINK`, and `AC_TRY_RUN`. The motivations where:

- a more consistent interface: `AC_TRY_COMPILE` etc. were double quoting their arguments;
- the combinatorial explosion is solved by decomposing on the one hand the generation of sources, and on the other hand executing the program;
- this scheme helps supporting more languages than plain C and C++.

In addition to the change of syntax, the philosophy has changed too: while emphasis was put on speed at the expense of accuracy, today’s Autoconf promotes accuracy of the testing framework at, ahem…, the expense of speed.

As a perfect example of what is *not* to be done, here is how to find out whether a header file contains a particular declaration, such as a typedef, a structure, a structure member, or a function. Use `AC_EGREP_HEADER` instead of running `grep` directly on the header file; on some systems the symbol might be defined in another header file that the file you are checking includes.

As a (bad) example, here is how you should not check for C preprocessor symbols, either defined by header files or predefined by the C preprocessor: using `AC_EGREP_CPP`:

```
AC_EGREP_CPP(yes,
[#ifdef _AIX
  yes
#endif
], is_aix=yes, is_aix=no)
```

The above example, properly written would (i) use `AC_LANG_PROGRAM`, and (ii) run the compiler:

```
AC_COMPILE_IFELSE([AC_LANG_PROGRAM(
[[#ifndef _AIX
 error: This isn't AIX!
#endif
]])],
                   [is_aix=yes],
                   [is_aix=no])
```

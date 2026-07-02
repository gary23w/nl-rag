---
title: "Autoconf (part 4/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 4/26
---

## 5 Existing Tests

These macros test for particular system features that packages might need or want to use. If you need to test for a kind of feature that none of these macros check for, you can probably do it by calling primitive test macros with appropriate arguments (see Writing Tests).

These tests print messages telling the user which feature they’re checking for, and what they find. They cache their results for future `configure` runs (see Caching Results).

Some of these macros set output variables. See Substitutions in Makefiles, for how to get their values. The phrase “define *name*” is used below as a shorthand to mean “define the C preprocessor symbol *name* to the value 1”. See Defining C Preprocessor Symbols, for how to get those symbol definitions into your program.

### 5.1 Common Behavior

Much effort has been expended to make Autoconf easy to learn. The most obvious way to reach this goal is simply to enforce standard interfaces and behaviors, avoiding exceptions as much as possible. Because of history and inertia, unfortunately, there are still too many exceptions in Autoconf; nevertheless, this section describes some of the common rules.

#### 5.1.1 Standard Symbols

All the generic macros that `AC_DEFINE` a symbol as a result of their test transform their *argument* values to a standard alphabet. First, *argument* is converted to upper case and any asterisks (‘*’) are each converted to ‘P’. Any remaining characters that are not alphanumeric are converted to underscores.

For instance,

```
AC_CHECK_TYPES([struct $Expensive*])
```

defines the symbol ‘HAVE_STRUCT__EXPENSIVEP’ if the check succeeds.

#### 5.1.2 Default Includes

Test programs frequently need to include headers that may or may not be available on the system whose features are being tested. Each test can use all the preprocessor macros that have been `AC_DEFINE`d by previous tests, so for example one may write

```
#include <time.h>
#ifdef HAVE_SYS_TIME_H
# include <sys/time.h>
#endif
```

if sys/time.h has already been tested for.

All hosted environments that are still of interest for portable code provide all of the headers specified in C89 (as amended in 1995): assert.h, ctype.h, errno.h, float.h, iso646.h, limits.h, locale.h, math.h, setjmp.h, signal.h, stdarg.h, stddef.h, stdio.h, stdlib.h, string.h, time.h, wchar.h, and wctype.h. Most programs can safely include these headers unconditionally. A program not intended to be portable to C89 can also safely include the C99-specified header stdbool.h. Other headers, including headers from C99 and later revisions of the C standard, might need to be tested for (see Header Files) or their bugs may need to be worked around (see Gnulib).

If your program needs to be portable to a *freestanding* environment, such as an embedded OS that doesn’t provide all of the facilities of the C89 standard library, you may need to test for some of the above headers as well. Note that many Autoconf macros internally assume that the complete set of C89 headers are available.

Most generic macros use the following macro to provide a default set of includes:

**Macro: **AC_INCLUDES_DEFAULT***([*include-directives*])* ¶**

Expand to *include-directives* if present and nonempty, otherwise to:

```
#include <stddef.h>
#ifdef HAVE_STDIO_H
# include <stdio.h>
#endif
#ifdef HAVE_STDLIB_H
# include <stdlib.h>
#endif
#ifdef HAVE_STRING_H
# include <string.h>
#endif
#ifdef HAVE_INTTYPES_H
# include <inttypes.h>
#endif
#ifdef HAVE_STDINT_H
# include <stdint.h>
#endif
#ifdef HAVE_STRINGS_H
# include <strings.h>
#endif
#ifdef HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#ifdef HAVE_SYS_STAT_H
# include <sys/stat.h>
#endif
#ifdef HAVE_UNISTD_H
# include <unistd.h>
#endif
```

Using this macro without *include-directives* has the side effect of checking for stdio.h, stdlib.h, string.h, inttypes.h, stdint.h, strings.h, sys/types.h, sys/stat.h, and unistd.h, as if by `AC_CHECK_HEADERS_ONCE`. For backward compatibility, the macro `STDC_HEADERS` will be defined when both stdlib.h and string.h are available.

**Portability Note:** It is safe for most programs to assume the presence of all of the headers required by the original 1990 C standard. `AC_INCLUDES_DEFAULT` checks for stdio.h, stdlib.h, and string.h, even though they are in that list, because they might not be available when compiling for a “freestanding environment” (in which most of the features of the C library are optional). You probably do not need to write ‘#ifdef HAVE_STDIO_H’ in your own code.

inttypes.h and stdint.h were added to C in the 1999 revision of the standard, and strings.h, sys/types.h, sys/stat.h, and unistd.h are POSIX extensions. You *should* guard uses of these headers with appropriate conditionals.

**Macro: **AC_CHECK_INCLUDES_DEFAULT** ¶**

Check for all the headers that `AC_INCLUDES_DEFAULT` would check for as a side-effect, if this has not already happened.

This macro mainly exists so that `autoupdate` can replace certain obsolete constructs with it. You should not need to use it yourself; in fact, it is likely to be safe to delete it from any script in which it appears. (`autoupdate` does not know whether preprocessor macros such as `HAVE_STDINT_H` are used in the program, nor whether they would get defined as a side-effect of other checks.)

### 5.2 Alternative Programs

These macros check for the presence or behavior of particular programs. They are used to choose between several alternative programs and to decide what to do once one has been chosen. If there is no macro specifically defined to check for a program you need, and you don’t need to check for any special properties of it, then you can use one of the general program-check macros.

#### 5.2.1 Particular Program Checks

These macros check for particular programs—whether they exist, and in some cases whether they support certain features.

**Macro: **AC_PROG_AR** ¶**

Set output variable `AR` to ‘ar’ if `ar` is found, and otherwise to ‘:’ (do nothing).

**Macro: **AC_PROG_AWK** ¶**

Check for the commands `gawk`, `mawk`, `nawk`, `awk`, and `busybox awk`, in that order, and set output variable `AWK` to the first one that is found. Try `gawk` first because that is reported to be the best implementation. The result can be overridden by setting the variable `AWK` or the cache variable `ac_cv_prog_AWK`.

Using this macro avoids some pitfalls of older systems that have both traditional `awk` (see Limitations of Usual Tools) and better alternatives like `gawk`. It also can help port to stripped-down systems that have only `busybox awk`, although these systems could well have problems with other build components that use plain `awk`.

**Macro: **AC_PROG_GREP** ¶**

Look for the best available `grep` or `ggrep` that accepts the longest input lines possible, and that supports multiple -e options. Set the output variable `GREP` to whatever is chosen. See Limitations of Usual Tools, for more information about portability problems with the `grep` command family. The result can be overridden by setting the `GREP` variable and is cached in the `ac_cv_path_GREP` variable.

**Macro: **AC_PROG_EGREP** ¶**

Check whether `$GREP -E` works, or else look for the best available `egrep` or `gegrep` that accepts the longest input lines possible. Set the output variable `EGREP` to whatever is chosen. The result can be overridden by setting the `EGREP` variable and is cached in the `ac_cv_path_EGREP` variable.

**Macro: **AC_PROG_FGREP** ¶**

Check whether `$GREP -F` works, or else look for the best available `fgrep` or `gfgrep` that accepts the longest input lines possible. Set the output variable `FGREP` to whatever is chosen. The result can be overridden by setting the `FGREP` variable and is cached in the `ac_cv_path_FGREP` variable.

**Macro: **AC_PROG_INSTALL** ¶**

Set output variable `INSTALL` to the name of a BSD-compatible `install` program, if one is found in the current `PATH`. Otherwise, set `INSTALL` to ‘*dir*/install-sh -c’, checking the directories specified to `AC_CONFIG_AUX_DIR` (or its default directories) to determine *dir* (see Outputting Files). Also set the variables `INSTALL_PROGRAM` and `INSTALL_SCRIPT` to ‘${INSTALL}’ and `INSTALL_DATA` to ‘${INSTALL} -m 644’.

‘@INSTALL@’ is special, as its value may vary for different configuration files.

This macro screens out various instances of `install` known not to work. It prefers to find a C program rather than a shell script, for speed. Instead of install-sh, it can also use install.sh, but that name is obsolete because some `make` programs have a rule that creates install from it if there is no makefile. Further, this macro requires `install` to be able to install multiple files into a target directory in a single invocation.

Autoconf comes with a copy of install-sh that you can use. If you use `AC_PROG_INSTALL`, you must include install-sh in your distribution; otherwise `autoreconf` and `configure` will produce an error message saying they can’t find it—even if the system you’re on has a good `install` program. This check is a safety measure to prevent you from accidentally leaving that file out, which would prevent your package from installing on systems that don’t have a BSD-compatible `install` program.

If you need to use your own installation program because it has features not found in standard `install` programs, there is no reason to use `AC_PROG_INSTALL`; just put the file name of your program into your Makefile.in files.

The result of the test can be overridden by setting the variable `INSTALL` or the cache variable `ac_cv_path_install`.

**Macro: **AC_PROG_MKDIR_P** ¶**

Set output variable `MKDIR_P` to a program that ensures that for each argument, a directory named by this argument exists, creating it and its parent directories if needed, and without race conditions when two instances of the program attempt to make the same directory at nearly the same time.

This macro uses the equivalent of the ‘mkdir -p’ command. Ancient versions of `mkdir` are vulnerable to race conditions, so if you want to support parallel installs from different packages into the same directory you should use a non-ancient `mkdir`.

This macro is related to the `AS_MKDIR_P` macro (see Programming in M4sh), but it sets an output variable intended for use in other files, whereas `AS_MKDIR_P` is intended for use in scripts like `configure`. Also, `AS_MKDIR_P` does not accept options, but `MKDIR_P` supports the -m option, e.g., a makefile might invoke `$(MKDIR_P) -m 0 dir` to create an inaccessible directory, and conversely a makefile should use `$(MKDIR_P) -- $(FOO)` if *FOO* might yield a value that begins with ‘-’.

The result of the test can be overridden by setting the variable `MKDIR_P` or the cache variable `ac_cv_path_mkdir`.

**Macro: **AC_PROG_LEX***(*options*)* ¶**

Search for a lexical analyzer generator, preferring `flex` to plain `lex`. Output variable `LEX` is set to whichever program is available. If neither program is available, `LEX` is set to ‘:’; for packages that ship the generated file.yy.c alongside the source file.l, this default allows users without a lexer generator to still build the package even if the timestamp for file.l is inadvertently changed.

The name of the program to use can be overridden by setting the output variable `LEX` or the cache variable `ac_cv_prog_LEX` when running `configure`.

If a lexical analyzer generator is found, this macro performs additional checks for common portability pitfalls. If these additional checks fail, `LEX` is reset to ‘:’; otherwise the following additional macros and variables are provided.

Preprocessor macro `YYTEXT_POINTER` is defined if the lexer skeleton, by default, declares `yytext` as a ‘char *’ rather than a ‘char []’.

Output variable `LEX_OUTPUT_ROOT` is set to the base of the file name that the lexer generates; this is usually either lex.yy or lexyy.

If generated lexers need a library to work, output variable `LEXLIB` is set to a link option for that library (e.g., -ll), otherwise it is set to empty.

The *options* argument modifies the behavior of `AC_PROG_LEX`. It should be a whitespace-separated list of options. Currently there are only two options, and they are mutually exclusive:

**`yywrap`**

Indicate that the library in `LEXLIB` needs to define the function `yywrap`. If a library that defines this function cannot be found, `LEX` will be reset to ‘:’.

**`noyywrap`**

Indicate that the library in `LEXLIB` does not need to define the function `yywrap`. `configure` will not search for it at all.

Prior to Autoconf 2.70, `AC_PROG_LEX` did not take any arguments, and its behavior was different from either of the above possibilities: it would search for a library that defines `yywrap`, and would set `LEXLIB` to that library if it finds one. However, if a library that defines this function could not be found, `LEXLIB` would be left empty and `LEX` would *not* be reset. This behavior was due to a bug, but several packages came to depend on it, so `AC_PROG_LEX` still does this if neither the `yywrap` nor the `noyywrap` option is given.

Usage of `AC_PROG_LEX` without choosing one of the `yywrap` or `noyywrap` options is deprecated. It is usually better to use `noyywrap` and define the `yywrap` function yourself, as this almost always renders the `LEXLIB` unnecessary.

**Caution:** As a side-effect of the test, this macro may delete any file in the configure script’s current working directory named lex.yy.c or lexyy.c.

**Caution:** Packages that ship a generated lex.yy.c cannot assume that the definition of `YYTEXT_POINTER` matches the code in that file. They also cannot assume that `LEXLIB` provides the library routines required by the code in that file.

If you use Flex to generate lex.yy.c, you can work around these limitations by defining `yywrap` and `main` yourself (rendering `-lfl` unnecessary), and by using either the --array or --pointer options to control how `yytext` is declared. The code generated by Flex is also more portable than the code generated by historical versions of Lex.

If you have used Flex to generate lex.yy.c, and especially if your scanner depends on Flex features, we recommend you use this Autoconf snippet to prevent the scanner being regenerated with historical Lex:

```
AC_PROG_LEX
AS_IF([test "x$LEX" != xflex],
  [LEX="$SHELL $missing_dir/missing flex"
   AC_SUBST([LEX_OUTPUT_ROOT], [lex.yy])
   AC_SUBST([LEXLIB], [''])])
```

The shell script `missing` can be found in the Automake distribution.

Remember that the user may have supplied an alternate location in `LEX`, so if Flex is required, it is better to check that the user provided something sufficient by parsing the output of ‘$LEX --version’ than by simply relying on `test "x$LEX" = xflex`.

**Macro: **AC_PROG_LN_S** ¶**

If ‘ln -s’ works on the current file system (the operating system and file system support symbolic links), set the output variable `LN_S` to ‘ln -s’; otherwise, if ‘ln’ works, set `LN_S` to ‘ln’, and otherwise set it to ‘cp -pR’.

If you make a link in a directory other than the current directory, its meaning depends on whether ‘ln’ or ‘ln -s’ is used. To safely create links using ‘$(LN_S)’, either find out which form is used and adjust the arguments, or always invoke `ln` in the directory where the link is to be created.

In other words, it does not work to do:

```
$(LN_S) foo /x/bar
```

Instead, do:

```
(cd /x && $(LN_S) foo bar)
```

**Macro: **AC_PROG_RANLIB** ¶**

Set output variable `RANLIB` to ‘ranlib’ if `ranlib` is found, and otherwise to ‘:’ (do nothing).

**Macro: **AC_PROG_SED** ¶**

Set output variable `SED` to a Sed implementation that conforms to POSIX and does not have arbitrary length limits. Report an error if no acceptable Sed is found. See Limitations of Usual Tools.

The result of this test can be overridden by setting the `SED` variable and is cached in the `ac_cv_path_SED` variable.

**Macro: **AC_PROG_YACC** ¶**

If `bison` is found, set output variable `YACC` to ‘bison -y’. Otherwise, if `byacc` is found, set `YACC` to ‘byacc’. Otherwise set `YACC` to ‘yacc’. The result of this test can be influenced by setting the variable `YACC` or the cache variable `ac_cv_prog_YACC`.

#### 5.2.2 Generic Program and File Checks

These macros are used to find programs not covered by the “particular” test macros. If you need to check the behavior of a program as well as find out whether it is present, you have to write your own test for it (see Writing Tests). By default, these macros use the environment variable `PATH`. If you need to check for a program that might not be in the user’s `PATH`, you can pass a modified path to use instead, like this:

```
AC_PATH_PROG([INETD], [inetd], [/usr/libexec/inetd],
             [$PATH$PATH_SEPARATOR/usr/libexec$PATH_SEPARATOR]dnl
[/usr/sbin$PATH_SEPARATOR/usr/etc$PATH_SEPARATOR/etc])
```

You are strongly encouraged to declare the *variable* passed to `AC_CHECK_PROG` etc. as precious. See Setting Output Variables, `AC_ARG_VAR`, for more details.

**Macro: **AC_CHECK_PROG***(*variable*, *prog-to-check-for*, *value-if-found*, [*value-if-not-found*], [*path* = ‘$PATH’], [*reject*])* ¶**

Check whether program *prog-to-check-for* exists in *path*. If it is found, set *variable* to *value-if-found*, otherwise to *value-if-not-found*, if given. Always pass over *reject* (an absolute file name) even if it is the first found in the search path; in that case, set *variable* using the absolute file name of the *prog-to-check-for* found that is not *reject*. If *variable* was already set, do nothing. Calls `AC_SUBST` for *variable*. The result of this test can be overridden by setting the *variable* variable or the cache variable `ac_cv_prog_*variable*`.

**Macro: **AC_CHECK_PROGS***(*variable*, *progs-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Check for each program in the blank-separated list *progs-to-check-for* existing in the *path*. If one is found, set *variable* to the name of that program. Otherwise, continue checking the next program in the list. If none of the programs in the list are found, set *variable* to *value-if-not-found*; if *value-if-not-found* is not specified, the value of *variable* is not changed. Calls `AC_SUBST` for *variable*. The result of this test can be overridden by setting the *variable* variable or the cache variable `ac_cv_prog_*variable*`.

**Macro: **AC_CHECK_TARGET_TOOL***(*variable*, *prog-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_PROG`, but first looks for *prog-to-check-for* with a prefix of the target type as determined by `AC_CANONICAL_TARGET`, followed by a dash (see Getting the Canonical System Type). If the tool cannot be found with a prefix, and if the build and target types are equal, then it is also searched for without a prefix.

As noted in Specifying target triplets, the target is rarely specified, because most of the time it is the same as the host: it is the type of system for which any compiler tool in the package produces code. What this macro looks for is, for example, *a tool (assembler, linker, etc.) that the compiler driver (`gcc` for the GNU C Compiler) uses to produce objects, archives or executables*.

**Macro: **AC_CHECK_TOOL***(*variable*, *prog-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_PROG`, but first looks for *prog-to-check-for* with a prefix of the host type as specified by --host, followed by a dash. For example, if the user runs ‘configure --build=x86_64-gnu --host=aarch64-linux-gnu’, then this call:

```
AC_CHECK_TOOL([RANLIB], [ranlib], [:])
```

sets `RANLIB` to aarch64-linux-gnu-ranlib if that program exists in *path*, or otherwise to ‘ranlib’ if that program exists in *path*, or to ‘:’ if neither program exists.

When cross-compiling, this macro will issue a warning if no program prefixed with the host type could be found. For more information, see Specifying target triplets.

**Macro: **AC_CHECK_TARGET_TOOLS***(*variable*, *progs-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_TARGET_TOOL`, each of the tools in the list *progs-to-check-for* are checked with a prefix of the target type as determined by `AC_CANONICAL_TARGET`, followed by a dash (see Getting the Canonical System Type). If none of the tools can be found with a prefix, and if the build and target types are equal, then the first one without a prefix is used. If a tool is found, set *variable* to the name of that program. If none of the tools in the list are found, set *variable* to *value-if-not-found*; if *value-if-not-found* is not specified, the value of *variable* is not changed. Calls `AC_SUBST` for *variable*.

**Macro: **AC_CHECK_TOOLS***(*variable*, *progs-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_TOOL`, each of the tools in the list *progs-to-check-for* are checked with a prefix of the host type as determined by `AC_CANONICAL_HOST`, followed by a dash (see Getting the Canonical System Type). If none of the tools can be found with a prefix, then the first one without a prefix is used. If a tool is found, set *variable* to the name of that program. If none of the tools in the list are found, set *variable* to *value-if-not-found*; if *value-if-not-found* is not specified, the value of *variable* is not changed. Calls `AC_SUBST` for *variable*.

When cross-compiling, this macro will issue a warning if no program prefixed with the host type could be found. For more information, see Specifying target triplets.

**Macro: **AC_PATH_PROG***(*variable*, *prog-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_PROG`, but set *variable* to the absolute name of *prog-to-check-for* if found. The result of this test can be overridden by setting the *variable* variable. A positive result of this test is cached in the `ac_cv_path_*variable*` variable.

**Macro: **AC_PATH_PROGS***(*variable*, *progs-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_PROGS`, but if any of *progs-to-check-for* are found, set *variable* to the absolute name of the program found. The result of this test can be overridden by setting the *variable* variable. A positive result of this test is cached in the `ac_cv_path_*variable*` variable.

**Macro: **AC_PATH_PROGS_FEATURE_CHECK***(*variable*, *progs-to-check-for*, *feature-test*, [*action-if-not-found*], [*path* = ‘$PATH’])* ¶**

This macro was introduced in Autoconf 2.62. If *variable* is not empty, then set the cache variable `ac_cv_path_*variable*` to its value. Otherwise, check for each program in the blank-separated list *progs-to-check-for* existing in *path*. For each program found, execute *feature-test* with `ac_path_*variable*` set to the absolute name of the candidate program. If no invocation of *feature-test* sets the shell variable `ac_cv_path_*variable*`, then *action-if-not-found* is executed. *feature-test* will be run even when `ac_cv_path_*variable*` is set, to provide the ability to choose a better candidate found later in *path*; to accept the current setting and bypass all further checks, *feature-test* can execute `ac_path_*variable*_found=:`.

Note that this macro has some subtle differences from `AC_CHECK_PROGS`. It is designed to be run inside `AC_CACHE_VAL`, therefore, it should have no side effects. In particular, *variable* is not set to the final value of `ac_cv_path_*variable*`, nor is `AC_SUBST` automatically run. Also, on failure, any action can be performed, whereas `AC_CHECK_PROGS` only performs `*variable*=*value-if-not-found*`.

Here is an example that searches for an implementation of `m4` that supports the `indir` builtin, even if it goes by the name `gm4` or is not the first implementation on `PATH`.

```
AC_CACHE_CHECK([for m4 that supports indir], [ac_cv_path_M4],
  [AC_PATH_PROGS_FEATURE_CHECK([M4], [m4 gm4],
    [[m4out=`echo 'changequote([,])indir([divnum])' | $ac_path_M4`
      test "x$m4out" = x0 \
      && ac_cv_path_M4=$ac_path_M4 ac_path_M4_found=:]],
    [AC_MSG_ERROR([could not find m4 that supports indir])])])
AC_SUBST([M4], [$ac_cv_path_M4])
```

**Macro: **AC_PATH_TARGET_TOOL***(*variable*, *prog-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_TARGET_TOOL`, but set *variable* to the absolute name of the program if it is found.

**Macro: **AC_PATH_TOOL***(*variable*, *prog-to-check-for*, [*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Like `AC_CHECK_TOOL`, but set *variable* to the absolute name of the program if it is found.

When cross-compiling, this macro will issue a warning if no program prefixed with the host type could be found. For more information, see Specifying target triplets.

### 5.3 Files

You might also need to check for the existence of files. Before using these macros, ask yourself whether a runtime test might not be a better solution. Be aware that, like most Autoconf macros, they test a feature of the host machine, and therefore, they die when cross-compiling.

**Macro: **AC_CHECK_FILE***(*file*, [*action-if-found*], [*action-if-not-found*])* ¶**

Check whether file *file* exists on the native system. If it is found, execute *action-if-found*, otherwise do *action-if-not-found*, if given. Cache the result of this test in the `ac_cv_file_*file*` variable, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_FILES***(*files*, [*action-if-found*], [*action-if-not-found*])* ¶**

For each file listed in *files*, execute `AC_CHECK_FILE` and perform either *action-if-found* or *action-if-not-found*. Like `AC_CHECK_FILE`, this defines ‘HAVE_*file*’ (see Standard Symbols) for each file found and caches the results of each test in the `ac_cv_file_*file*` variable, with characters not suitable for a variable name mapped to underscores.

### 5.4 Library Files

The following macros check for the presence of certain C, C++, Fortran, or Go library archive files.

**Macro: **AC_CHECK_LIB***(*library*, *function*, [*action-if-found*], [*action-if-not-found*], [*other-libraries*])* ¶**

Test whether the library *library* is available by trying to link a test program that calls function *function* with the library. *function* should be a function provided by the library. Use the base name of the library; e.g., to check for -lmp, use ‘mp’ as the *library* argument.

*action-if-found* is a list of shell commands to run if the link with the library succeeds; *action-if-not-found* is a list of shell commands to run if the link fails. If *action-if-found* is not specified, the default action prepends -l*library* to `LIBS` and defines ‘HAVE_LIB*library*’ (in all capitals). This macro is intended to support building `LIBS` in a right-to-left (least-dependent to most-dependent) fashion such that library dependencies are satisfied as a natural side effect of consecutive tests. Linkers are sensitive to library ordering so the order in which `LIBS` is generated is important to reliable detection of libraries.

If linking with *library* results in unresolved symbols that would be resolved by linking with additional libraries, give those libraries as the *other-libraries* argument, separated by spaces: e.g., -lXt -lX11. Otherwise, this macro may fail to detect that *library* is present, because linking the test program can fail with unresolved symbols. The *other-libraries* argument should be limited to cases where it is desirable to test for one library in the presence of another that is not already in `LIBS`.

`AC_CHECK_LIB` requires some care in usage, and should be avoided in some common cases. Many standard functions like `gethostbyname` appear in the standard C library on some hosts, and in special libraries like `nsl` on other hosts. On some hosts the special libraries contain variant implementations that you may not want to use. These days it is normally better to use `AC_SEARCH_LIBS([gethostbyname], [nsl])` instead of `AC_CHECK_LIB([nsl], [gethostbyname])`.

The result of this test is cached in the `ac_cv_lib_*library*_*function*` variable.

**Macro: **AC_SEARCH_LIBS***(*function*, *search-libs*, [*action-if-found*], [*action-if-not-found*], [*other-libraries*])* ¶**

Search for a library defining *function* if it’s not already available. This equates to calling ‘AC_LINK_IFELSE([AC_LANG_CALL([], [*function*])])’ first with no libraries, then for each library listed in *search-libs*.

Prepend -l*library* to `LIBS` for the first library found to contain *function*, and run *action-if-found*. If the function is not found, run *action-if-not-found*.

If linking with *library* results in unresolved symbols that would be resolved by linking with additional libraries, give those libraries as the *other-libraries* argument, separated by spaces: e.g., -lXt -lX11. Otherwise, this macro fails to detect that *function* is present, because linking the test program always fails with unresolved symbols.

The result of this test is cached in the `ac_cv_search_*function*` variable as ‘none required’ if *function* is already available, as ‘no’ if no library containing *function* was found, otherwise as the -l*library* option that needs to be prepended to `LIBS`.

### 5.5 Library Functions

The following macros check for particular C library functions. If there is no macro specifically defined to check for a function you need, and you don’t need to check for any special properties of it, then you can use one of the general function-check macros.

#### 5.5.1 Portability of C Functions

Most usual functions can either be missing, or be buggy, or be limited on some architectures. This section tries to make an inventory of these portability issues. By definition, this list always requires additions. A much more complete list is maintained by the Gnulib project (see Gnulib), covering Current POSIX Functions in *Gnulib*, Legacy Functions in *Gnulib*, and Glibc Functions in *Gnulib*. Please help us keep the Gnulib list as complete as possible.

**`exit`**

On ancient hosts, `exit` returned `int`. This is because `exit` predates `void`, and there was a long tradition of it returning `int`.

On current hosts, the problem more likely is that `exit` is not declared, due to C++ problems of some sort or another. For this reason we suggest that test programs not invoke `exit`, but return from `main` instead.

**`malloc`**

The C standard says a successful call `malloc (0)` is implementation dependent. It can return either `NULL` or a new non-null pointer. The latter is more common (e.g., the GNU C Library) but is by no means universal. `AC_FUNC_MALLOC` can be used to insist on non-`NULL` (see Particular Function Checks).

**`putenv`**

POSIX prefers `setenv` to `putenv`; among other things, `putenv` is not required of all POSIX implementations, but `setenv` is.

POSIX specifies that `putenv` puts the given string directly in `environ`, but some systems make a copy of it instead (e.g., glibc 2.0, or BSD). And when a copy is made, `unsetenv` might not free it, causing a memory leak (e.g., FreeBSD 4).

On some systems `putenv ("FOO")` removes ‘FOO’ from the environment, but this is not standard usage and it dumps core on some systems (e.g., AIX).

On MinGW, a call `putenv ("FOO=")` removes ‘FOO’ from the environment, rather than inserting it with an empty value.

**`realloc`**

It is problematic to call `realloc` with a zero size. The C standard says `realloc (NULL, 0)` is equivalent to `malloc (0)`, which means one cannot portably tell whether the call has succeeded if it returns a null pointer. If `ptr` is non-null, the C standard says `realloc (ptr, 0)` has undefined behavior.

The `AC_FUNC_REALLOC` macro avoids some of these portability issues. See Particular Function Checks.

**`signal` handler**

In most cases, it is more robust to use `sigaction` when it is available, rather than `signal`.

**`snprintf`**

In C99 and later, if the output array isn’t big enough and if no other errors occur, `snprintf` and `vsnprintf` truncate the output and return the number of bytes that ought to have been produced. Some older systems, notably Microsoft Windows before Visual Studio 2015 and Windows 10, do not null-terminate the output and return −1 instead.

Portable code can check the return value of `snprintf (buf, sizeof buf, ...)`: if the value is negative or is not less than `sizeof buf`, an error occurred and the contents of `buf` can be ignored. Alternatively, one of the Gnulib modules related to `snprintf` can be used. See Gnulib.

**`strerror_r`**

POSIX specifies that `strerror_r` returns an `int`, but many systems (e.g., the GNU C Library) provide a different version returning a `char *`. `AC_FUNC_STRERROR_R` can detect which is in use (see Particular Function Checks).

**`strnlen`**

Android 5.0’s strnlen was broken, because it assumed the addressed array always had at least the specified number of bytes. For example, `strnlen ("", SIZE_MAX)` should return 0 but on Android 5.0 it crashed.

AIX 4.3 provided a broken version which produces the following results:

```
strnlen ("foobar", 0) = 0
strnlen ("foobar", 1) = 3
strnlen ("foobar", 2) = 2
strnlen ("foobar", 3) = 1
strnlen ("foobar", 4) = 0
strnlen ("foobar", 5) = 6
strnlen ("foobar", 6) = 6
strnlen ("foobar", 7) = 6
strnlen ("foobar", 8) = 6
strnlen ("foobar", 9) = 6
```

**`sysconf`**

`_SC_PAGESIZE` is standard, but some older systems (e.g., HP-UX 9) have `_SC_PAGE_SIZE` instead. This can be tested with `#ifdef`.

**`unlink`**

The POSIX spec says that `unlink` causes the given file to be removed only after there are no more open file handles for it. Some non-POSIX hosts have trouble with this requirement, though, and some DOS variants even corrupt the file system.

**`unsetenv`**

On MinGW, `unsetenv` is not available, but a variable ‘FOO’ can be removed with a call `putenv ("FOO=")`, as described under `putenv` above.

**`va_copy`**

C99 and later provide `va_copy` for copying `va_list` variables. It may be available in older environments too, though possibly as `__va_copy` (e.g., `gcc` in strict pre-C99 mode). These can be tested with `#ifdef`. A fallback to `memcpy (&dst, &src, sizeof (va_list))` gives maximum portability.

**`va_list`**

`va_list` is not necessarily just a pointer. It can be a `struct`, which means `NULL` is not portable. Or it can be an array, which means as a function parameter it can be effectively call-by-reference and library routines might modify the value back in the caller.

**Signed `>>`**

Normally the C `>>` right shift of a signed type replicates the high bit, giving a so-called “arithmetic” shift. But care should be taken since Standard C doesn’t require that behavior. On a few platforms (e.g., Cray C by default) zero bits are shifted in, the same as a shift of an unsigned type.

**Integer `/`**

C divides signed integers by truncating their quotient toward zero, yielding the same result as Fortran. However, before C99 the standard allowed C implementations to take the floor or ceiling of the quotient in some cases. Hardly any implementations took advantage of this freedom, though, and it’s probably not worth worrying about this issue nowadays.

#### 5.5.2 Particular Function Checks

These macros check for particular C functions—whether they exist, and in some cases how they respond when given certain arguments.

**Macro: **AC_FUNC_ALLOCA** ¶**

Check for the `alloca` function. Define `HAVE_ALLOCA_H` if alloca.h defines a working `alloca`. If not, look for a builtin alternative. If either method succeeds, define `HAVE_ALLOCA`. Otherwise, set the output variable `ALLOCA` to ‘${LIBOBJDIR}alloca.o’ and define `C_ALLOCA` (so programs can periodically call ‘alloca (0)’ to garbage collect). This variable is separate from `LIBOBJS` so multiple programs can share the value of `ALLOCA` without needing to create an actual library, in case only some of them use the code in `LIBOBJS`. The ‘${LIBOBJDIR}’ prefix serves the same purpose as in `LIBOBJS` (see `AC_LIBOBJ` vs. `LIBOBJS`).

Source files that use `alloca` should start with a piece of code like the following, to declare it properly.

```
#include <stdlib.h>
#include <stddef.h>
#ifdef HAVE_ALLOCA_H
# include <alloca.h>
#elif !defined alloca
# ifdef __GNUC__
#  define alloca __builtin_alloca
# elif defined _MSC_VER
#  include <malloc.h>
#  define alloca _alloca
# elif !defined HAVE_ALLOCA
#  ifdef  __cplusplus
extern "C"
#  endif
void *alloca (size_t);
# endif
#endif
```

If you don’t want to maintain this piece of code in your package manually, you can instead use the Gnulib module `alloca-opt` or `alloca`. See Gnulib.

**Macro: **AC_FUNC_CHOWN** ¶**

If the `chown` function is available and works (in particular, it should accept -1 for `uid` and `gid`), define `HAVE_CHOWN`. The result of this macro is cached in the `ac_cv_func_chown_works` variable.

If you want a workaround, that is, a `chown` function that is available and works, you can use the Gnulib module `chown`. See Gnulib.

**Macro: **AC_FUNC_CLOSEDIR_VOID** ¶**

If the `closedir` function does not return a meaningful value, define `CLOSEDIR_VOID`. Otherwise, callers ought to check its return value for an error indicator.

Currently this test is implemented by running a test program. When cross compiling the pessimistic assumption that `closedir` does not return a meaningful value is made.

The result of this macro is cached in the `ac_cv_func_closedir_void` variable.

This macro is obsolescent, as `closedir` returns a meaningful value on current systems. New programs need not use this macro.

**Macro: **AC_FUNC_ERROR_AT_LINE** ¶**

If the `error_at_line` function is not found, require an `AC_LIBOBJ` replacement of ‘error’.

The result of this macro is cached in the `ac_cv_lib_error_at_line` variable.

The `AC_FUNC_ERROR_AT_LINE` macro is obsolescent. New programs should use Gnulib’s `error` module. See Gnulib.

**Macro: **AC_FUNC_FNMATCH** ¶**

If the `fnmatch` function conforms to POSIX, define `HAVE_FNMATCH`.

Unlike the other specific `AC_FUNC` macros, `AC_FUNC_FNMATCH` does not replace a broken/missing `fnmatch`. This is for historical reasons. See `AC_REPLACE_FNMATCH` below.

The result of this macro is cached in the `ac_cv_func_fnmatch_works` variable.

This macro is obsolescent. New programs should use Gnulib’s `fnmatch-posix` module. See Gnulib.

**Macro: **AC_FUNC_FNMATCH_GNU** ¶**

Behave like `AC_REPLACE_FNMATCH` (*replace*) but also test whether `fnmatch` supports GNU extensions. Detect common implementation bugs, for example, the bugs in the GNU C Library 2.1.

The result of this macro is cached in the `ac_cv_func_fnmatch_gnu` variable.

This macro is obsolescent. New programs should use Gnulib’s `fnmatch-gnu` module. See Gnulib.

**Macro: **AC_FUNC_FORK** ¶**

This macro checks for the `fork` and `vfork` functions. If a working `fork` is found, define `HAVE_WORKING_FORK`. This macro checks whether `fork` is just a stub by trying to run it.

If vfork.h is found, define `HAVE_VFORK_H`. If a working `vfork` is found, define `HAVE_WORKING_VFORK`. Otherwise, define `vfork` to be `fork` for backward compatibility with previous versions of `autoconf`. This macro checks for several known errors in implementations of `vfork` and considers the system to not have a working `vfork` if it detects any of them.

Since this macro defines `vfork` only for backward compatibility with previous versions of `autoconf` you’re encouraged to define it yourself in new code:

```
#ifndef HAVE_WORKING_VFORK
# define vfork fork
#endif
```

The results of this macro are cached in the `ac_cv_func_fork_works` and `ac_cv_func_vfork_works` variables. In order to override the test, you also need to set the `ac_cv_func_fork` and `ac_cv_func_vfork` variables.

**Macro: **AC_FUNC_FSEEKO** ¶**

If the `fseeko` and `ftello` functions are available, define `HAVE_FSEEKO`. Define `_LARGEFILE_SOURCE` if necessary to make the prototype visible.

Configure scripts that use `AC_FUNC_FSEEKO` should normally also use `AC_SYS_LARGEFILE` to ensure that `off_t` can represent all supported file sizes. See AC_SYS_LARGEFILE.

The Gnulib module `fseeko` invokes `AC_FUNC_FSEEKO` and also contains workarounds for other portability problems of `fseeko`. See Gnulib.

**Macro: **AC_FUNC_GETGROUPS** ¶**

Perform all the checks performed by `AC_TYPE_GETGROUPS` (see AC_TYPE_GETGROUPS). Then, if the `getgroups` function is available and known to work correctly, define `HAVE_GETGROUPS`. Set the output variable `GETGROUPS_LIB` to any libraries needed to get that function.

This macro relies on a list of systems with known, serious bugs in `getgroups`. If this list mis-identifies your system’s `getgroups` as buggy, or as not buggy, you can override it by setting the cache variable `ac_cv_func_getgroups_works` in a config.site file (see Setting Site Defaults). Please also report the error to the Autoconf Bugs mailing list.

The Gnulib module `getgroups` provides workarounds for additional, less severe portability problems with this function.

**Macro: **AC_FUNC_GETLOADAVG** ¶**

Check how to get the system load averages. To perform its tests properly, this macro needs the file getloadavg.c; therefore, be sure to set the `AC_LIBOBJ` replacement directory properly (see Generic Function Checks, `AC_CONFIG_LIBOBJ_DIR`).

If the system has the `getloadavg` function, define `HAVE_GETLOADAVG`, and set `GETLOADAVG_LIBS` to any libraries necessary to get that function. Also add `GETLOADAVG_LIBS` to `LIBS`. Otherwise, require an `AC_LIBOBJ` replacement for ‘getloadavg’ and possibly define several other C preprocessor macros and output variables:

1. Define `C_GETLOADAVG`.
2. Define `SVR4`, `DGUX`, `UMAX`, or `UMAX4_3` if on those systems.
3. If nlist.h is found, define `HAVE_NLIST_H`.
4. If ‘struct nlist’ has an ‘n_un.n_name’ member, define `HAVE_STRUCT_NLIST_N_UN_N_NAME`. The obsolete symbol `NLIST_NAME_UNION` is still defined, but do not depend upon it.
5. Programs may need to be installed set-group-ID (or set-user-ID) for `getloadavg` to work. In this case, define `GETLOADAVG_PRIVILEGED`, set the output variable `NEED_SETGID` to ‘true’ (and otherwise to ‘false’), and set `KMEM_GROUP` to the name of the group that should own the installed program.

The `AC_FUNC_GETLOADAVG` macro is obsolescent. New programs should use Gnulib’s `getloadavg` module. See Gnulib.

**Macro: **AC_FUNC_GETMNTENT** ¶**

Check for `getmntent` in the standard C library, and then in the sun, seq, and gen libraries. Then, if `getmntent` is available, define `HAVE_GETMNTENT` and set `ac_cv_func_getmntent` to `yes`. Otherwise set `ac_cv_func_getmntent` to `no`.

The result of this macro can be overridden by setting the cache variable `ac_cv_search_getmntent`.

The `AC_FUNC_GETMNTENT` macro is obsolescent. New programs should use Gnulib’s `mountlist` module. See Gnulib.

**Macro: **AC_FUNC_GETPGRP** ¶**

Define `GETPGRP_VOID` if it is an error to pass 0 to `getpgrp`; this is the POSIX behavior. On older BSD systems, you must pass 0 to `getpgrp`, as it takes an argument and behaves like POSIX’s `getpgid`.

```
#ifdef GETPGRP_VOID
  pid = getpgrp ();
#else
  pid = getpgrp (0);
#endif
```

This macro does not check whether `getpgrp` exists at all; if you need to work in that situation, first call `AC_CHECK_FUNC` for `getpgrp`.

The result of this macro is cached in the `ac_cv_func_getpgrp_void` variable.

This macro is obsolescent, as current systems have a `getpgrp` whose signature conforms to POSIX. New programs need not use this macro.

**Macro: **AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK** ¶**

If link is a symbolic link, then `lstat` should treat link/ the same as link/.. However, many older `lstat` implementations incorrectly ignore trailing slashes.

It is safe to assume that if `lstat` incorrectly ignores trailing slashes, then other symbolic-link-aware functions like `unlink` also incorrectly ignore trailing slashes.

If `lstat` behaves properly, define `LSTAT_FOLLOWS_SLASHED_SYMLINK`, otherwise require an `AC_LIBOBJ` replacement of `lstat`.

The result of this macro is cached in the `ac_cv_func_lstat_dereferences_slashed_symlink` variable.

The `AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK` macro is obsolescent. New programs should use Gnulib’s `lstat` module. See Gnulib.

**Macro: **AC_FUNC_MALLOC** ¶**

If the `malloc` function is compatible with the GNU C library `malloc` (i.e., ‘malloc (0)’ returns a valid pointer), define `HAVE_MALLOC` to 1. Otherwise define `HAVE_MALLOC` to 0, ask for an `AC_LIBOBJ` replacement for ‘malloc’, and define `malloc` to `rpl_malloc` so that the native `malloc` is not used in the main project.

Typically, the replacement file malloc.c should look like (note the ‘#undef malloc’):

```
#include <config.h>
#undef malloc

#include <stdlib.h>

/* Allocate an N-byte block of memory from the heap.
   If N is zero, allocate a 1-byte block.  */

void *
rpl_malloc (size_t n)
{
  if (n == 0)
    n = 1;
  return malloc (n);
}
```

The result of this macro is cached in the `ac_cv_func_malloc_0_nonnull` variable. The result might contain spaces, e.g., `guessing yes`.

If you don’t want to maintain a `malloc.c` file in your package manually, you can instead use the Gnulib module `malloc-gnu`.

**Macro: **AC_FUNC_MBRTOWC** ¶**

Define `HAVE_MBRTOWC` to 1 if the function `mbrtowc` and the type `mbstate_t` are properly declared.

The result of this macro is cached in the `ac_cv_func_mbrtowc` variable.

The Gnulib module `mbrtowc` not only ensures that the function is declared, but also works around other portability problems of this function.

**Macro: **AC_FUNC_MEMCMP** ¶**

If the `memcmp` function is not available or does not work, require an `AC_LIBOBJ` replacement for ‘memcmp’.

The result of this macro is cached in the `ac_cv_func_memcmp_working` variable.

This macro is obsolescent, as current systems have a working `memcmp`. New programs need not use this macro.

**Macro: **AC_FUNC_MKTIME** ¶**

If the `mktime` function is not available, or does not work correctly, require an `AC_LIBOBJ` replacement for ‘mktime’. For the purposes of this test, `mktime` should conform to the POSIX standard and should be the inverse of `localtime`.

The result of this macro is cached in the `ac_cv_func_working_mktime` variable.

The `AC_FUNC_MKTIME` macro is obsolescent. New programs should use Gnulib’s `mktime` module. See Gnulib.

**Macro: **AC_FUNC_MMAP** ¶**

If the `mmap` function exists and works correctly, define `HAVE_MMAP`. This checks only private fixed mapping of already-mapped memory.

The result of this macro is cached in the `ac_cv_func_mmap_fixed_mapped` variable.

Note: This macro asks for more than what an average program needs from `mmap`. In particular, the use of `MAP_FIXED` fails on HP-UX 11, whereas `mmap` otherwise works fine on this platform.

**Macro: **AC_FUNC_OBSTACK** ¶**

If the obstacks are found, define `HAVE_OBSTACK`, else require an `AC_LIBOBJ` replacement for ‘obstack’.

The result of this macro is cached in the `ac_cv_func_obstack` variable.

The `AC_FUNC_OBSTACK` macro is obsolescent. New programs should use Gnulib’s `obstack` module. See Gnulib.

**Macro: **AC_FUNC_REALLOC** ¶**

If a successful call to ‘realloc (NULL, 0)’ returns a non-null pointer, define `HAVE_REALLOC` to 1. Otherwise define `HAVE_REALLOC` to 0, ask for an `AC_LIBOBJ` replacement for ‘realloc’, and define `realloc` to `rpl_realloc` so that the native `realloc` is not used in the main project. See `AC_FUNC_MALLOC` for details.

The result of this macro is cached in the `ac_cv_func_realloc_0_nonnull` variable. The result might contain spaces, e.g., `guessing yes`.

This macro does not check compatibility with glibc `realloc (*p*, 0)` when *p* is non-null, as glibc 1–2.1 behaves differently from glibc 2.1.1–2.40 (at least), and the C standard says behavior is undefined.

**Macro: **AC_FUNC_SELECT_ARGTYPES** ¶**

Determines the correct type to be passed for each of the `select` function’s arguments, and defines those types in `SELECT_TYPE_ARG1`, `SELECT_TYPE_ARG234`, and `SELECT_TYPE_ARG5` respectively. `SELECT_TYPE_ARG1` defaults to ‘int’, `SELECT_TYPE_ARG234` defaults to ‘int *’, and `SELECT_TYPE_ARG5` defaults to ‘struct timeval *’.

This macro is obsolescent, as current systems have a `select` whose signature conforms to POSIX. New programs need not use this macro.

**Macro: **AC_FUNC_SETPGRP** ¶**

If `setpgrp` takes no argument (the POSIX version), define `SETPGRP_VOID`. Otherwise, it is the BSD version, which takes two process IDs as arguments. This macro does not check whether `setpgrp` exists at all; if you need to work in that situation, first call `AC_CHECK_FUNC` for `setpgrp`. This macro also does not check for the Solaris variant of `setpgrp`, which returns a `pid_t` instead of an `int`; portable code should only use the return value by comparing it against `-1` to check for errors.

The result of this macro is cached in the `ac_cv_func_setpgrp_void` variable.

This macro is obsolescent, as all forms of `setpgrp` are also obsolescent. New programs should use the POSIX function `setpgid`, which takes two process IDs as arguments (like the BSD `setpgrp`).

**Macro: **AC_FUNC_STAT** ¶**

**Macro: **AC_FUNC_LSTAT** ¶**

Determine whether `stat` or `lstat` have the bug that it succeeds when given the zero-length file name as argument.

If it does, then define `HAVE_STAT_EMPTY_STRING_BUG` (or `HAVE_LSTAT_EMPTY_STRING_BUG`) and ask for an `AC_LIBOBJ` replacement of it.

The results of these macros are cached in the `ac_cv_func_stat_empty_string_bug` and the `ac_cv_func_lstat_empty_string_bug` variables, respectively.

These macros are obsolescent, as no current systems have the bug. New programs need not use these macros.

**Macro: **AC_FUNC_STRCOLL** ¶**

If the `strcoll` function exists and works correctly, define `HAVE_STRCOLL`. This does a bit more than ‘AC_CHECK_FUNCS(strcoll)’, because some systems have incorrect definitions of `strcoll` that should not be used. But it does not check against a known bug of this function on Solaris 10.

The result of this macro is cached in the `ac_cv_func_strcoll_works` variable.

**Macro: **AC_FUNC_STRERROR_R** ¶**

If `strerror_r` is available, define `HAVE_STRERROR_R`, and if it is declared, define `HAVE_DECL_STRERROR_R`. If it returns a `char *` message, define `STRERROR_R_CHAR_P`; otherwise it returns an `int` error number. The Thread-Safe Functions option of POSIX requires `strerror_r` to return `int`, but many systems (including, for example, the GNU C Library) return a `char *` value that is not necessarily equal to the buffer argument.

The result of this macro is cached in the `ac_cv_func_strerror_r_char_p` variable.

The Gnulib module `strerror_r` not only ensures that the function has the return type specified by POSIX, but also works around other portability problems of this function.

**Macro: **AC_FUNC_STRFTIME** ¶**

Check for `strftime` in the intl library. Then, if `strftime` is available, define `HAVE_STRFTIME`.

This macro is obsolescent, as no current systems require the intl library for `strftime`. New programs need not use this macro.

**Macro: **AC_FUNC_STRTOD** ¶**

If the `strtod` function does not exist or doesn’t work correctly, ask for an `AC_LIBOBJ` replacement of ‘strtod’. In this case, because strtod.c is likely to need ‘pow’, set the output variable `POW_LIB` to the extra library needed.

This macro caches its result in the `ac_cv_func_strtod` variable and depends upon the result in the `ac_cv_func_pow` variable.

The `AC_FUNC_STRTOD` macro is obsolescent. New programs should use Gnulib’s `strtod` module. See Gnulib.

**Macro: **AC_FUNC_STRTOLD** ¶**

If the `strtold` function exists and conforms to C99 or later, define `HAVE_STRTOLD`.

This macro caches its result in the `ac_cv_func_strtold` variable.

The Gnulib module `strtold` not only ensures that the function exists, but also works around other portability problems of this function.

**Macro: **AC_FUNC_STRNLEN** ¶**

If the `strnlen` function is not available, or is buggy (like the one from Android 5.0 or AIX 4.3), require an `AC_LIBOBJ` replacement for it.

This macro caches its result in the `ac_cv_func_strnlen_working` variable.

The `AC_FUNC_STRNLEN` macro is obsolescent. New programs should use Gnulib’s `strnlen` module. See Gnulib.

**Macro: **AC_FUNC_UTIME_NULL** ¶**

If ‘utime (*file*, NULL)’ sets *file*’s timestamp to the present, define `HAVE_UTIME_NULL`.

This macro caches its result in the `ac_cv_func_utime_null` variable.

This macro is obsolescent, as all current systems have a `utime` that behaves this way. New programs need not use this macro.

**Macro: **AC_FUNC_VPRINTF** ¶**

If `vprintf` is found, define `HAVE_VPRINTF`. Otherwise, if `_doprnt` is found, define `HAVE_DOPRNT`. (If `vprintf` is available, you may assume that `vfprintf` and `vsprintf` are also available.)

This macro is obsolescent, as all current systems have `vprintf`. New programs need not use this macro.

**Macro: **AC_REPLACE_FNMATCH** ¶**

If the `fnmatch` function does not conform to POSIX (see `AC_FUNC_FNMATCH`), ask for its `AC_LIBOBJ` replacement.

The files fnmatch.c, fnmatch_loop.c, and fnmatch_.h in the `AC_LIBOBJ` replacement directory are assumed to contain a copy of the source code of GNU `fnmatch`. If necessary, this source code is compiled as an `AC_LIBOBJ` replacement, and the fnmatch_.h file is linked to fnmatch.h so that it can be included in place of the system `<fnmatch.h>`.

This macro caches its result in the `ac_cv_func_fnmatch_works` variable.

This macro is obsolescent, as it assumes the use of particular source files. New programs should use Gnulib’s `fnmatch-posix` module, which provides this macro along with the source files. See Gnulib.

#### 5.5.3 Generic Function Checks

These macros are used to find functions not covered by the “particular” test macros. If the functions might be in libraries other than the default C library, first call `AC_CHECK_LIB` for those libraries. If you need to check the behavior of a function as well as find out whether it is present, you have to write your own test for it (see Writing Tests).

**Macro: **AC_CHECK_FUNC***(*function*, [*action-if-found*], [*action-if-not-found*])* ¶**

If C function *function* is available, run shell commands *action-if-found*, otherwise *action-if-not-found*. If you just want to define a symbol if the function is available, consider using `AC_CHECK_FUNCS` instead. This macro checks for functions with C linkage even when `AC_LANG(C++)` has been called, since C is more standardized than C++. (see Language Choice, for more information about selecting the language for checks.)

This macro caches its result in the `ac_cv_func_*function*` variable.

**Macro: **AC_CHECK_FUNCS***(*function*…, [*action-if-found*], [*action-if-not-found*])* ¶**

For each *function* enumerated in the blank-or-newline-separated argument list, define `HAVE_*function*` (in all capitals) if it is available. If *action-if-found* is given, it is additional shell code to execute when one of the functions is found. You can give it a value of ‘break’ to break out of the loop on the first match. If *action-if-not-found* is given, it is executed when one of the functions is not found.

Results are cached for each *function* as in `AC_CHECK_FUNC`.

**Macro: **AC_CHECK_FUNCS_ONCE***(*function*…)* ¶**

For each *function* enumerated in the blank-or-newline-separated argument list, define `HAVE_*function*` (in all capitals) if it is available. This is a once-only variant of `AC_CHECK_FUNCS`. It generates the checking code at most once, so that `configure` is smaller and faster; but the checks cannot be conditionalized and are always done once, early during the `configure` run.

Autoconf follows a philosophy that was formed over the years by those who have struggled for portability: isolate the portability issues in specific files, and then program as if you were in a POSIX environment. Some functions may be missing or unfixable, and your package must be ready to replace them.

Suitable replacements for many such problem functions are available from Gnulib (see Gnulib).

**Macro: **AC_LIBOBJ***(*function*)* ¶**

Specify that ‘*function*.c’ must be included in the executables to replace a missing or broken implementation of *function*.

Technically, it adds ‘*function*.$ac_objext’ to the output variable `LIBOBJS` if it is not already in, and calls `AC_LIBSOURCE` for ‘*function*.c’. You should not directly change `LIBOBJS`, since this is not traceable.

**Macro: **AC_LIBSOURCE***(*file*)* ¶**

Specify that *file* might be needed to compile the project. If you need to know what files might be needed by a configure.ac, you should trace `AC_LIBSOURCE`. *file* must be a literal.

This macro is called automatically from `AC_LIBOBJ`, but you must call it explicitly if you pass a shell variable to `AC_LIBOBJ`. In that case, since shell variables cannot be traced statically, you must pass to `AC_LIBSOURCE` any possible files that the shell variable might cause `AC_LIBOBJ` to need. For example, if you want to pass a variable `$foo_or_bar` to `AC_LIBOBJ` that holds either `"foo"` or `"bar"`, you should do:

```
AC_LIBSOURCE([foo.c])
AC_LIBSOURCE([bar.c])
AC_LIBOBJ([$foo_or_bar])
```

There is usually a way to avoid this, however, and you are encouraged to simply call `AC_LIBOBJ` with literal arguments.

Note that this macro replaces the obsolete `AC_LIBOBJ_DECL`, with slightly different semantics: the old macro took the function name, e.g., `foo`, as its argument rather than the file name.

**Macro: **AC_LIBSOURCES***(*files*)* ¶**

Like `AC_LIBSOURCE`, but accepts one or more *files* in a comma-separated M4 list. Thus, the above example might be rewritten:

```
AC_LIBSOURCES([foo.c, bar.c])
AC_LIBOBJ([$foo_or_bar])
```

**Macro: **AC_CONFIG_LIBOBJ_DIR***(*directory*)* ¶**

Specify that `AC_LIBOBJ` replacement files are to be found in *directory*, a name relative to the top level of the source tree. The replacement directory defaults to ., the top level directory, and the most typical value is lib, corresponding to ‘AC_CONFIG_LIBOBJ_DIR([lib])’.

`configure` might need to know the replacement directory for the following reasons: (i) some checks use the replacement files, (ii) some macros bypass broken system headers by installing links to the replacement headers (iii) when used in conjunction with Automake, within each makefile, *directory* is used as a relative path from `$(top_srcdir)` to each object named in `LIBOBJS` and `LTLIBOBJS`, etc.

It is common to merely check for the existence of a function, and ask for its `AC_LIBOBJ` replacement if missing. The following macro is a convenient shorthand.

**Macro: **AC_REPLACE_FUNCS***(*function*…)* ¶**

Like `AC_CHECK_FUNCS`, but uses ‘AC_LIBOBJ(*function*)’ as *action-if-not-found*. You can declare your replacement function by enclosing the prototype in ‘#ifndef HAVE_*function*’. If the system has the function, it probably declares it in a header file you should be including, so you shouldn’t redeclare it lest your declaration conflict.

### 5.6 Header Files

The following macros check for the presence of certain C header files. If there is no macro specifically defined to check for a header file you need, and you don’t need to check for any special properties of it, then you can use one of the general header-file check macros.

#### 5.6.1 Portability of Headers

This section documents some collected knowledge about common headers, and the problems they cause. By definition, this list always requires additions. A much more complete list is maintained by the Gnulib project (see Gnulib), covering POSIX Headers in *Gnulib* and Glibc Headers in *Gnulib*. Please help us keep the Gnulib list as complete as possible.

When we say that a header “may require” some set of other headers, we mean that it may be necessary for you to manually include those other headers first, or the contents of the header under test will fail to compile. When checking for these headers, you must provide the potentially-required headers in the *includes* argument to `AC_CHECK_HEADER` or `AC_CHECK_HEADERS`, or the check will fail spuriously. `AC_INCLUDES_DEFAULT` (see Default Includes) arranges to include a number of common requirements and should normally come first in your *includes*. For example, net/if.h may require sys/types.h, sys/socket.h, or both, and `AC_INCLUDES_DEFAULT` handles sys/types.h but not sys/socket.h, so you should check for it like this:

```
AC_CHECK_HEADERS([sys/socket.h])
AC_CHECK_HEADERS([net/if.h], [], [],
[AC_INCLUDES_DEFAULT[
#ifdef HAVE_SYS_SOCKET_H
# include <sys/socket.h>
#endif
]])
```

Note that the example mixes single quoting (for`AC_INCLUDES_DEFAULT`, so that it gets expanded) and double quoting (to ensure that each preprocessor `#` gets treated as a literal string rather than a comment).

**limits.h**

In C99 and later, limits.h defines `LLONG_MIN`, `LLONG_MAX`, and `ULLONG_MAX`, but many almost-C99 environments (e.g., default GCC 4.0.2 + glibc 2.4) do not define them.

**memory.h ¶**

This header file is obsolete; use string.h instead.

**strings.h ¶**

On some systems, this is the only header that declares `strcasecmp`, `strncasecmp`, and `ffs`.

This header may or may not include string.h for you. However, on all recent systems it is safe to include both string.h and strings.h, in either order, in the same source file.

**inttypes.h vs. stdint.h ¶**

C99 specifies that inttypes.h includes stdint.h, so there’s no need to include stdint.h separately in a standard environment. However, some implementations have stdint.h but not inttypes.h (e.g. MSVC 2012). Therefore, it is necessary to check for each and include each only if available.

**linux/irda.h ¶**

This header may require linux/types.h and/or sys/socket.h.

**linux/random.h ¶**

This header may require linux/types.h.

**net/if.h ¶**

This header may require sys/types.h and/or sys/socket.h.

**netinet/if_ether.h ¶**

This header may require some combination of sys/types.h, sys/socket.h, netinet/in.h, and net/if.h.

**sys/mount.h ¶**

This header may require sys/params.h.

**sys/ptem.h ¶**

This header may require sys/stream.h.

**sys/socket.h ¶**

This header may require sys/types.h.

**sys/ucred.h ¶**

This header may require sys/types.h.

**X11/extensions/scrnsaver.h ¶**

Using XFree86, this header requires X11/Xlib.h, which is probably so required that you might not even consider looking for it.

#### 5.6.2 Particular Header Checks

These macros check for particular system header files—whether they exist, and in some cases whether they declare certain symbols.

**Macro: **AC_CHECK_HEADER_STDBOOL** ¶**

Check whether stdbool.h exists and conforms to C99 or later, and cache the result in the `ac_cv_header_stdbool_h` variable. If the type `_Bool` is defined, define `HAVE__BOOL` to 1.

This macro is obsolescent, as all current C compilers have stdbool.h, a header that is itself obsolescent as of C23.

This macro is intended for use by Gnulib (see Gnulib) and other packages that supply a substitute stdbool.h on platforms lacking a conforming one. The `AC_HEADER_STDBOOL` macro is better for code that explicitly checks for stdbool.h.

**Macro: **AC_HEADER_ASSERT** ¶**

Check whether to enable assertions in the style of assert.h. Assertions are enabled by default, but the user can override this by invoking `configure` with the --disable-assert option.

**Macro: **AC_HEADER_DIRENT** ¶**

Check for the following header files. For the first one that is found and defines ‘DIR’, define the listed C preprocessor macro:

| dirent.h | `HAVE_DIRENT_H` |
|---|---|
| sys/ndir.h | `HAVE_SYS_NDIR_H` |
| sys/dir.h | `HAVE_SYS_DIR_H` |
| ndir.h | `HAVE_NDIR_H` |

The directory-library declarations in your source code should look something like the following:

```
#include <sys/types.h>
#ifdef HAVE_DIRENT_H
# include <dirent.h>
# define NAMLEN(dirent) strlen ((dirent)->d_name)
#else
# define dirent direct
# define NAMLEN(dirent) ((dirent)->d_namlen)
# ifdef HAVE_SYS_NDIR_H
#  include <sys/ndir.h>
# endif
# ifdef HAVE_SYS_DIR_H
#  include <sys/dir.h>
# endif
# ifdef HAVE_NDIR_H
#  include <ndir.h>
# endif
#endif
```

Using the above declarations, the program would declare variables to be of type `struct dirent`, not `struct direct`, and would access the length of a directory entry name by passing a pointer to a `struct dirent` to the `NAMLEN` macro.

This macro also checks for the obsolete dir and x libraries.

This macro is obsolescent, as all current systems with directory libraries have `<dirent.h>`. New programs need not use this macro.

Also see `AC_STRUCT_DIRENT_D_INO` and `AC_STRUCT_DIRENT_D_TYPE` (see Particular Structure Checks).

**Macro: **AC_HEADER_MAJOR** ¶**

Detect the headers required to use `makedev`, `major`, and `minor`. These functions may be defined by sys/mkdev.h, `sys/sysmacros.h`, or sys/types.h.

`AC_HEADER_MAJOR` defines `MAJOR_IN_MKDEV` if they are in sys/mkdev.h, or `MAJOR_IN_SYSMACROS` if they are in sys/sysmacros.h. If neither macro is defined, they are either in sys/types.h or unavailable.

To properly use these functions, your code should contain something like:

```
#include <sys/types.h>
#ifdef MAJOR_IN_MKDEV
# include <sys/mkdev.h>
#elif defined MAJOR_IN_SYSMACROS
# include <sys/sysmacros.h>
#endif
```

Note: Configure scripts built with Autoconf 2.69 or earlier will not detect a problem if sys/types.h contains definitions of `major`, `minor`, and/or `makedev` that trigger compiler warnings upon use. This is known to occur with GNU libc 2.25, where those definitions are being deprecated to reduce namespace pollution. If it is not practical to use Autoconf 2.70 to regenerate the configure script of affected software, you can work around the problem by setting ‘ac_cv_header_sys_types_h_makedev=no’, as an argument to `configure` or as part of a config.site site default file (see Setting Site Defaults).

**Macro: **AC_HEADER_RESOLV** ¶**

Checks for header resolv.h, checking for prerequisites first. To properly use resolv.h, your code should contain something like the following:

```
#ifdef HAVE_SYS_TYPES_H
#  include <sys/types.h>
#endif
#ifdef HAVE_NETINET_IN_H
#  include <netinet/in.h>   /* inet_ functions / structs */
#endif
#ifdef HAVE_ARPA_NAMESER_H
#  include <arpa/nameser.h> /* DNS HEADER struct */
#endif
#ifdef HAVE_NETDB_H
#  include <netdb.h>
#endif
#include <resolv.h>
```

**Macro: **AC_HEADER_STAT** ¶**

If the macros `S_ISDIR`, `S_ISREG`, etc. defined in sys/stat.h do not work properly (returning false positives), define `STAT_MACROS_BROKEN`. This is the case on Tektronix UTekV, Amdahl UTS and Motorola System V/88.

This macro is obsolescent, as no current systems have the bug. New programs need not use this macro.

**Macro: **AC_HEADER_STDBOOL** ¶**

If stdbool.h exists and conforms to C99 or later, define `HAVE_STDBOOL_H` to 1; if the type `_Bool` is defined, define `HAVE__BOOL` to 1.

This macro is obsolescent, as all current C compilers have stdbool.h, a header that is itself obsolescent as of C23. Nowadays programs that need `bool`, `true` and `false` can include stdbool.h unconditionally, without using `AC_HEADER_STDBOOL`, and if such a program needs to be portable only to C23 or later it need not even include stdbool.h.

This macro caches its result in the `ac_cv_header_stdbool_h` variable.

This macro differs from `AC_CHECK_HEADER_STDBOOL` only in that it defines `HAVE_STDBOOL_H` whereas `AC_CHECK_HEADER_STDBOOL` does not.

**Macro: **AC_HEADER_STDC** ¶**

This macro is obsolescent. Its sole effect is to make sure that all the headers that are included by `AC_INCLUDES_DEFAULT` (see Default Includes), but not part of C89, have been checked for.

All hosted environments that are still of interest for portable code provide all of the headers specified in C89 (as amended in 1995).

**Macro: **AC_HEADER_SYS_WAIT** ¶**

If sys/wait.h exists and is compatible with POSIX, define `HAVE_SYS_WAIT_H`. Incompatibility can occur if sys/wait.h does not exist, or if it uses the old BSD `union wait` instead of `int` to store a status value. If sys/wait.h is not POSIX compatible, then instead of including it, define the POSIX macros with their usual interpretations. Here is an example:

```
#include <sys/types.h>
#ifdef HAVE_SYS_WAIT_H
# include <sys/wait.h>
#endif
#ifndef WEXITSTATUS
# define WEXITSTATUS(stat_val) ((unsigned int) (stat_val) >> 8)
#endif
#ifndef WIFEXITED
# define WIFEXITED(stat_val) (((stat_val) & 255) == 0)
#endif
```

This macro caches its result in the `ac_cv_header_sys_wait_h` variable.

This macro is obsolescent, as current systems are compatible with POSIX. New programs need not use this macro.

`_POSIX_VERSION` is defined when unistd.h is included on POSIX systems. If there is no unistd.h, it is definitely not a POSIX system. However, some non-POSIX systems do have unistd.h.

The way to check whether the system says it supports POSIX is:

```
#ifdef HAVE_UNISTD_H
# include <sys/types.h>
# include <unistd.h>
#endif

#ifdef _POSIX_VERSION
/* Code for POSIX systems.  */
#endif
```

**Macro: **AC_HEADER_TIOCGWINSZ** ¶**

If the use of `TIOCGWINSZ` requires <sys/ioctl.h>, then define `GWINSZ_IN_SYS_IOCTL`. Otherwise `TIOCGWINSZ` can be found in <termios.h>.

Use:

```
#ifdef HAVE_TERMIOS_H
# include <termios.h>
#endif

#ifdef GWINSZ_IN_SYS_IOCTL
# include <sys/ioctl.h>
#endif
```

#### 5.6.3 Generic Header Checks

These macros are used to find system header files not covered by the “particular” test macros. If you need to check the contents of a header as well as find out whether it is present, you have to write your own test for it (see Writing Tests).

**Macro: **AC_CHECK_HEADER***(*header-file*, [*action-if-found*], [*action-if-not-found*], [*includes*])* ¶**

If the system header file *header-file* is compilable, execute shell commands *action-if-found*, otherwise execute *action-if-not-found*. If you just want to define a symbol if the header file is available, consider using `AC_CHECK_HEADERS` instead.

*includes* should be the appropriate *prerequisite* code, i.e. whatever might be required to appear above ‘#include <*header-file*>’ for it to compile without error. This can be anything, but will normally be additional ‘#include’ directives. If *includes* is omitted or empty, configure will use the contents of the macro `AC_INCLUDES_DEFAULT`. See Default Includes.

This macro used to check only for the *presence* of a header, not whether its contents were acceptable to the compiler. Some older `configure` scripts rely on this behavior, so it is still available by specifying ‘-’ as *includes*. This mechanism is deprecated as of Autoconf 2.70; situations where a preprocessor-only check is required should use `AC_PREPROC_IFELSE`. See Running the Preprocessor.

This macro caches its result in the `ac_cv_header_*header-file*` variable, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_HEADERS***(*header-file*…, [*action-if-found*], [*action-if-not-found*], [*includes*])* ¶**

For each given system header file *header-file* in the blank-separated argument list that exists, define `HAVE_*header-file*` (in all capitals). If *action-if-found* is given, it is additional shell code to execute when one of the header files is found. You can give it a value of ‘break’ to break out of the loop on the first match. If *action-if-not-found* is given, it is executed when one of the header files is not found.

*includes* is interpreted as in `AC_CHECK_HEADER`, in order to choose the set of preprocessor directives supplied before the header under test.

This macro caches its result in the `ac_cv_header_*header-file*` variable, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_HEADERS_ONCE***(*header-file*…)* ¶**

For each given system header file *header-file* in the blank-separated argument list that exists, define `HAVE_*header-file*` (in all capitals).

If you do not need the full power of `AC_CHECK_HEADERS`, this variant generates smaller, faster `configure` files. All headers passed to `AC_CHECK_HEADERS_ONCE` are checked for in one pass, early during the `configure` run. The checks cannot be conditionalized, you cannot specify an *action-if-found* or *action-if-not-found*, and `AC_INCLUDES_DEFAULT` is always used for the prerequisites.

In previous versions of Autoconf, these macros merely checked whether the header was accepted by the preprocessor. This was changed because the old test was inappropriate for typical uses. Headers are typically used to compile, not merely to preprocess, and the old behavior sometimes accepted headers that clashed at compile-time (see Header Present But Cannot Be Compiled). If for some reason it is inappropriate to check whether a header is compilable, you should use `AC_PREPROC_IFELSE` (see Running the Preprocessor) instead of these macros.

Requiring each header to compile improves the robustness of the test, but it also requires you to make sure that the *includes* are correct. Most system headers nowadays make sure to `#include` whatever they require, or else have their dependencies satisfied by `AC_INCLUDES_DEFAULT` (see Default Includes), but see Portability of Headers, for known exceptions. In general, if you are looking for bar.h, which requires that foo.h be included first if it exists, you should do something like this:

```
AC_CHECK_HEADERS([foo.h])
AC_CHECK_HEADERS([bar.h], [], [],
[#ifdef HAVE_FOO_H
# include <foo.h>
#endif
])
```

### 5.7 Declarations

The following macros check for the declaration of variables and functions. If there is no macro specifically defined to check for a symbol you need, then you can use the general macros (see Generic Declaration Checks) or, for more complex tests, you may use `AC_COMPILE_IFELSE` (see Running the Compiler).

#### 5.7.1 Particular Declaration Checks

There are no specific macros for declarations.

#### 5.7.2 Generic Declaration Checks

These macros are used to find declarations not covered by the “particular” test macros.

**Macro: **AC_CHECK_DECL***(*symbol*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

If *symbol* (a function, variable, or constant) is not declared in *includes* and a declaration is needed, run the shell commands *action-if-not-found*, otherwise *action-if-found*. *includes* is a series of include directives, defaulting to `AC_INCLUDES_DEFAULT` (see Default Includes), which are used prior to the declaration under test.

This macro actually tests whether *symbol* is defined as a macro or can be used as an r-value, not whether it is really declared, because it is much safer to avoid introducing extra declarations when they are not needed. In order to facilitate use of C++ and overloaded function declarations, it is possible to specify function argument types in parentheses for types which can be zero-initialized:

```
AC_CHECK_DECL([basename(char *)])
```

This macro caches its result in the `ac_cv_have_decl_*symbol*` variable, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_DECLS***(*symbols*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

For each of the *symbols* (*comma*-separated list with optional function argument types for C++ overloads), define `HAVE_DECL_*symbol*` (in all capitals) to ‘1’ if *symbol* is declared, otherwise to ‘0’. If *action-if-not-found* is given, it is additional shell code to execute when one of the function declarations is needed, otherwise *action-if-found* is executed.

*includes* is a series of include directives, defaulting to `AC_INCLUDES_DEFAULT` (see Default Includes), which are used prior to the declarations under test.

This macro uses an M4 list as first argument:

```
AC_CHECK_DECLS([strdup])
AC_CHECK_DECLS([strlen])
AC_CHECK_DECLS([malloc, realloc, calloc, free])
AC_CHECK_DECLS([j0], [], [], [[#include <math.h>]])
AC_CHECK_DECLS([[basename(char *)], [dirname(char *)]])
```

Unlike the other ‘AC_CHECK_*S’ macros, when a *symbol* is not declared, `HAVE_DECL_*symbol*` is defined to ‘0’ instead of leaving `HAVE_DECL_*symbol*` undeclared. When you are *sure* that the check was performed, use `HAVE_DECL_*symbol*` in `#if`:

```
#if !HAVE_DECL_SYMBOL
extern char *symbol;
#endif
```

If the test may have not been performed, however, because it is safer *not* to declare a symbol than to use a declaration that conflicts with the system’s one, you should use:

```
#if defined HAVE_DECL_MALLOC && !HAVE_DECL_MALLOC
void *malloc (size_t *s);
#endif
```

You fall into the second category only in extreme situations: either your files may be used without being configured, or they are used during the configuration. In most cases the traditional approach is enough.

This macro caches its results in `ac_cv_have_decl_*symbol*` variables, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_DECLS_ONCE***(*symbols*)* ¶**

For each of the *symbols* (*comma*-separated list), define `HAVE_DECL_*symbol*` (in all capitals) to ‘1’ if *symbol* is declared in the default include files, otherwise to ‘0’. This is a once-only variant of `AC_CHECK_DECLS`. It generates the checking code at most once, so that `configure` is smaller and faster; but the checks cannot be conditionalized and are always done once, early during the `configure` run.

### 5.8 Structures

The following macros check for the presence of certain members in C structures. If there is no macro specifically defined to check for a member you need, then you can use the general structure-member macros (see Generic Structure Checks) or, for more complex tests, you may use `AC_COMPILE_IFELSE` (see Running the Compiler).

#### 5.8.1 Particular Structure Checks

The following macros check for certain structures or structure members.

**Macro: **AC_STRUCT_DIRENT_D_INO** ¶**

Perform all the actions of `AC_HEADER_DIRENT` (see Particular Header Checks). Then, if `struct dirent` contains a `d_ino` member, define `HAVE_STRUCT_DIRENT_D_INO`.

`HAVE_STRUCT_DIRENT_D_INO` indicates only the presence of `d_ino`, not whether its contents are always reliable. Traditionally, a zero `d_ino` indicated a deleted directory entry, though current systems hide this detail from the user and never return zero `d_ino` values. Many current systems report an incorrect `d_ino` for a directory entry that is a mount point.

**Macro: **AC_STRUCT_DIRENT_D_TYPE** ¶**

Perform all the actions of `AC_HEADER_DIRENT` (see Particular Header Checks). Then, if `struct dirent` contains a `d_type` member, define `HAVE_STRUCT_DIRENT_D_TYPE`.

**Macro: **AC_STRUCT_ST_BLOCKS** ¶**

If `struct stat` contains an `st_blocks` member, define `HAVE_STRUCT_STAT_ST_BLOCKS`. Otherwise, require an `AC_LIBOBJ` replacement of ‘fileblocks’. The former name, `HAVE_ST_BLOCKS` is to be avoided, as its support will cease in the future.

This macro caches its result in the `ac_cv_member_struct_stat_st_blocks` variable.

**Macro: **AC_STRUCT_TM** ¶**

If time.h does not define `struct tm`, define `TM_IN_SYS_TIME`, which means that including sys/time.h had better define `struct tm`.

---
title: "Autoconf (part 8/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 8/26
---

## 7 Results of Tests

Once `configure` has determined whether a feature exists, what can it do to record that information? There are four sorts of things it can do: define a C preprocessor symbol, set a variable in the output files, save the result in a cache file for future `configure` runs, and print a message letting the user know the result of the test.

### 7.1 Defining C Preprocessor Symbols

A common action to take in response to a feature test is to define a C preprocessor symbol indicating the results of the test. That is done by calling `AC_DEFINE` or `AC_DEFINE_UNQUOTED`.

By default, `AC_OUTPUT` places the symbols defined by these macros into the output variable `DEFS`, which contains an option -D*symbol*=*value* for each symbol defined. Unlike in Autoconf version 1, there is no variable `DEFS` defined while `configure` is running. To check whether Autoconf macros have already defined a certain C preprocessor symbol, test the value of the appropriate cache variable, as in this example:

```
AC_CHECK_FUNC([vprintf],
  [AC_DEFINE([HAVE_VPRINTF], [1],
     [Define if vprintf exists.])])
AS_IF([test "x$ac_cv_func_vprintf" != xyes],
  [AC_CHECK_FUNC([_doprnt],
     [AC_DEFINE([HAVE_DOPRNT], [1],
        [Define if _doprnt exists.])])])
```

If `AC_CONFIG_HEADERS` has been called, then instead of creating `DEFS`, `AC_OUTPUT` creates a header file by substituting the correct values into `#define` statements in a template file. See Configuration Header Files, for more information about this kind of output.

**Macro: **AC_DEFINE***(*variable*, *value*, [*description*])* ¶**

**Macro: **AC_DEFINE***(*variable*)* ¶**

Define *variable* to *value* (verbatim), by defining a C preprocessor macro for *variable*. *variable* should be a C identifier, optionally suffixed by a parenthesized argument list to define a C preprocessor macro with arguments. The macro argument list, if present, should be a comma-separated list of C identifiers, possibly terminated by an ellipsis ‘...’ if C99-or-later syntax is employed. *variable* should not contain comments, white space, trigraphs, backslash-newlines, universal character names, or non-ASCII characters.

*value* may contain backslash-escaped newlines, which will be preserved if you use `AC_CONFIG_HEADERS` but flattened if passed via `@DEFS@` (with no effect on the compilation, since the preprocessor sees only one line in the first place). *value* should not contain raw newlines. If you are not using `AC_CONFIG_HEADERS`, *value* should not contain any ‘#’ characters, as `make` tends to eat them. To use a shell variable, use `AC_DEFINE_UNQUOTED` instead.

*description* is only useful if you are using `AC_CONFIG_HEADERS`. In this case, *description* is put into the generated config.h.in as the comment before the macro define. The following example defines the C preprocessor variable `EQUATION` to be the string constant ‘"$a > $b"’:

```
AC_DEFINE([EQUATION], ["$a > $b"],
  [Equation string.])
```

If neither *value* nor *description* are given, then *value* defaults to 1 instead of to the empty string. This is for backwards compatibility with older versions of Autoconf, but this usage is obsolescent and may be withdrawn in future versions of Autoconf.

If the *variable* is a literal string, it is passed to `m4_pattern_allow` (see Forbidden Patterns).

If multiple `AC_DEFINE` statements are executed for the same *variable* name (not counting any parenthesized argument list), the last one wins.

**Macro: **AC_DEFINE_UNQUOTED***(*variable*, *value*, [*description*])* ¶**

**Macro: **AC_DEFINE_UNQUOTED***(*variable*)* ¶**

Like `AC_DEFINE`, but three shell expansions are performed—once—on *variable* and *value*: variable expansion (‘$’), command substitution (‘`’), and backslash escaping (‘\’), as if in an unquoted here-document. Single and double quote characters in the value have no special meaning. Use this macro instead of `AC_DEFINE` when *variable* or *value* is a shell variable. Examples:

```
AC_DEFINE_UNQUOTED([config_machfile], ["$machfile"],
  [Configuration machine file.])
AC_DEFINE_UNQUOTED([GETGROUPS_T], [$ac_cv_type_getgroups],
  [getgroups return type.])
AC_DEFINE_UNQUOTED([$ac_tr_hdr], [1],
  [Translated header name.])
```

Due to a syntactical oddity of the Bourne shell, do not use semicolons to separate `AC_DEFINE` or `AC_DEFINE_UNQUOTED` calls from other macro calls or shell code; that can cause syntax errors in the resulting `configure` script. Use either blanks or newlines. That is, do this:

```
AC_CHECK_HEADER([elf.h],
  [AC_DEFINE([SVR4], [1], [System V Release 4]) LIBS="-lelf $LIBS"])
```

or this:

```
AC_CHECK_HEADER([elf.h],
  [AC_DEFINE([SVR4], [1], [System V Release 4])
   LIBS="-lelf $LIBS"])
```

instead of this:

```
AC_CHECK_HEADER([elf.h],
  [AC_DEFINE([SVR4], [1], [System V Release 4]); LIBS="-lelf $LIBS"])
```

### 7.2 Setting Output Variables

Another way to record the results of tests is to set *output variables*, which are shell variables whose values are substituted into files that `configure` outputs. The two macros below create new output variables. See Preset Output Variables, for a list of output variables that are always available.

**Macro: **AC_SUBST***(*variable*, [*value*])* ¶**

Create an output variable from a shell variable. Make `AC_OUTPUT` substitute the variable *variable* into output files (typically one or more makefiles). This means that `AC_OUTPUT` replaces instances of ‘@*variable*@’ in input files with the value that the shell variable *variable* has when `AC_OUTPUT` is called. The value can contain any non-`NUL` character, including newline. If you are using Automake 1.11 or newer, for newlines in values you might want to consider using `AM_SUBST_NOTMAKE` to prevent `automake` from adding a line `*variable* = @*variable*@` to the Makefile.in files (see Automake in *Other things Automake recognizes*).

Variable occurrences should not overlap: e.g., an input file should not contain ‘@*var1*@*var2*@’ if *var1* and *var2* are variable names. The substituted value is not rescanned for more output variables; occurrences of ‘@*variable*@’ in the value are inserted literally into the output file. (The algorithm uses the special marker `|#_!!_#|` internally, so neither the substituted value nor the output file may contain `|#_!!_#|`.)

If *value* is given, in addition assign it to *variable*.

The string *variable* is passed to `m4_pattern_allow` (see Forbidden Patterns). *variable* is not further expanded, even if there is another macro by the same name.

**Macro: **AC_SUBST_FILE***(*variable*)* ¶**

Another way to create an output variable from a shell variable. Make `AC_OUTPUT` insert (without substitutions) the contents of the file named by shell variable *variable* into output files. This means that `AC_OUTPUT` replaces instances of ‘@*variable*@’ in output files (such as Makefile.in) with the contents of the file that the shell variable *variable* names when `AC_OUTPUT` is called. Set the variable to /dev/null for cases that do not have a file to insert. This substitution occurs only when the ‘@*variable*@’ is on a line by itself, optionally surrounded by spaces and tabs. The substitution replaces the whole line, including the spaces, tabs, and the terminating newline.

This macro is useful for inserting makefile fragments containing special dependencies or other `make` directives for particular host or target types into makefiles. For example, configure.ac could contain:

```
AC_SUBST_FILE([host_frag])
host_frag=$srcdir/conf/sun4.mh
```

and then a Makefile.in could contain:

```
@host_frag@
```

The string *variable* is passed to `m4_pattern_allow` (see Forbidden Patterns).

Running `configure` in varying environments can be extremely dangerous. If for instance the user runs ‘CC=bizarre-cc ./configure’, then the cache, config.h, and many other output files depend upon `bizarre-cc` being the C compiler. If for some reason the user runs `./configure` again, or if it is run via ‘./config.status --recheck’, (See Automatic Remaking, and see config.status Invocation), then the configuration can be inconsistent, composed of results depending upon two different compilers.

Environment variables that affect this situation, such as ‘CC’ above, are called *precious variables*, and can be declared as such by `AC_ARG_VAR`.

**Macro: **AC_ARG_VAR***(*variable*, *description*)* ¶**

Declare *variable* is a precious variable, and include its *description* in the variable section of ‘./configure --help’.

Being precious means that

- *variable* is substituted via `AC_SUBST`.
- The value of *variable* when `configure` was launched is saved in the cache, including if it was not specified on the command line but via the environment. Indeed, while `configure` can notice the definition of `CC` in ‘./configure CC=bizarre-cc’, it is impossible to notice it in ‘CC=bizarre-cc ./configure’, which, unfortunately, is what most users do. We emphasize that it is the *initial* value of *variable* which is saved, not that found during the execution of `configure`. Indeed, specifying ‘./configure FOO=foo’ and letting ‘./configure’ guess that `FOO` is `foo` can be two different things.
- *variable* is checked for consistency between two `configure` runs. For instance: $ ./configure --silent --config-cache $ CC=cc ./configure --silent --config-cache configure: error: 'CC' was not set in the previous run configure: error: changes in the environment can compromise \ the build configure: error: run 'make distclean' and/or \ 'rm config.cache' and start over and similarly if the variable is unset, or if its content is changed. If the content has white space changes only, then the error is degraded to a warning only, but the old value is reused.
- *variable* is kept during automatic reconfiguration (see config.status Invocation) as if it had been passed as a command line argument, including when no cache is used: $ CC=/usr/bin/cc ./configure var=raboof --silent $ ./config.status --recheck running CONFIG_SHELL=/bin/sh /bin/sh ./configure var=raboof \ CC=/usr/bin/cc --no-create --no-recursion

### 7.3 Special Characters in Output Variables

Many output variables are intended to be evaluated both by `make` and by the shell. Some characters are expanded differently in these two contexts, so to avoid confusion these variables’ values should not contain any of the following characters:

```
" # $ & ' ( ) * ; < > ? [ \ ^ ` |
```

Also, these variables’ values should neither contain newlines, nor start with ‘~’, nor contain white space or ‘:’ immediately followed by ‘~’. The values can contain nonempty sequences of white space characters like tabs and spaces, but each such sequence might arbitrarily be replaced by a single space during substitution.

These restrictions apply both to the values that `configure` computes, and to the values set directly by the user. For example, the following invocations of `configure` are problematic, since they attempt to use special characters within `CPPFLAGS` and white space within `$(srcdir)`:

```
CPPFLAGS='-DOUCH="&\"#$*?"' '../My Source/ouch-1.0/configure'

'../My Source/ouch-1.0/configure' CPPFLAGS='-DOUCH="&\"#$*?"'
```

### 7.4 Caching Results

To avoid checking for the same features repeatedly in various `configure` scripts (or in repeated runs of one script), `configure` can optionally save the results of many checks in a *cache file* (see Cache Files). If a `configure` script runs with caching enabled and finds a cache file, it reads the results of previous runs from the cache and avoids rerunning those checks. As a result, `configure` can then run much faster than if it had to perform all of the checks every time.

**Macro: **AC_CACHE_VAL***(*cache-id*, *commands-to-set-it*)* ¶**

Ensure that the results of the check identified by *cache-id* are available. If the results of the check were in the cache file that was read, and `configure` was not given the --quiet or --silent option, print a message saying that the result was cached; otherwise, run the shell commands *commands-to-set-it*. If the shell commands are run to determine the value, the value is saved in the cache file just before `configure` creates its output files. See Cache Variable Names, for how to choose the name of the *cache-id* variable.

The *commands-to-set-it* *must have no side effects* except for setting the variable *cache-id*, see below.

**Macro: **AC_CACHE_CHECK***(*message*, *cache-id*, *commands-to-set-it*)* ¶**

A wrapper for `AC_CACHE_VAL` that takes care of printing the messages. This macro provides a convenient shorthand for the most common way to use these macros. It calls `AC_MSG_CHECKING` for *message*, then `AC_CACHE_VAL` with the *cache-id* and *commands* arguments, and `AC_MSG_RESULT` with *cache-id*.

The *commands-to-set-it* *must have no side effects* except for setting the variable *cache-id*, see below.

It is common to find buggy macros using `AC_CACHE_VAL` or `AC_CACHE_CHECK`, because people are tempted to call `AC_DEFINE` in the *commands-to-set-it*. Instead, the code that *follows* the call to `AC_CACHE_VAL` should call `AC_DEFINE`, by examining the value of the cache variable. For instance, the following macro is broken:

```
AC_DEFUN([AC_SHELL_TRUE],
[AC_CACHE_CHECK([whether true(1) works], [my_cv_shell_true_works],
                [my_cv_shell_true_works=no
                 (true) 2>/dev/null && my_cv_shell_true_works=yes
                 if test "x$my_cv_shell_true_works" = xyes; then
                   AC_DEFINE([TRUE_WORKS], [1],
                             [Define if 'true(1)' works properly.])
                 fi])
])
```

This fails if the cache is enabled: the second time this macro is run, `TRUE_WORKS` *will not be defined*. The proper implementation is:

```
AC_DEFUN([AC_SHELL_TRUE],
[AC_CACHE_CHECK([whether true(1) works], [my_cv_shell_true_works],
                [my_cv_shell_true_works=no
                 (true) 2>/dev/null && my_cv_shell_true_works=yes])
 if test "x$my_cv_shell_true_works" = xyes; then
   AC_DEFINE([TRUE_WORKS], [1],
             [Define if 'true(1)' works properly.])
 fi
])
```

Also, *commands-to-set-it* should not print any messages, for example with `AC_MSG_CHECKING`; do that before calling `AC_CACHE_VAL`, so the messages are printed regardless of whether the results of the check are retrieved from the cache or determined by running the shell commands.

#### 7.4.1 Cache Variable Names

The names of cache variables should have the following format:

```
package-prefix_cv_value-type_specific-value_[additional-options]
```

for example, ‘ac_cv_header_stat_broken’ or ‘ac_cv_prog_gcc_traditional’. The parts of the variable name are:

***package-prefix***

An abbreviation for your package or organization; the same prefix you begin local Autoconf macros with, except lowercase by convention. For cache values used by the distributed Autoconf macros, this value is ‘ac’.

**`_cv_`**

Indicates that this shell variable is a cache value. This string *must* be present in the variable name, including the leading underscore.

***value-type***

A convention for classifying cache values, to produce a rational naming system. The values used in Autoconf are listed in Macro Names.

***specific-value***

Which member of the class of cache values this test applies to. For example, which function (‘alloca’), program (‘gcc’), or output variable (‘INSTALL’).

***additional-options***

Any particular behavior of the specific member that this test applies to. For example, ‘broken’ or ‘set’. This part of the name may be omitted if it does not apply.

The values assigned to cache variables may not contain newlines. Usually, their values are Boolean (‘yes’ or ‘no’) or the names of files or functions; so this is not an important restriction. Cache Variable Index for an index of cache variables with documented semantics.

#### 7.4.2 Cache Files

A cache file is a shell script that caches the results of configure tests run on one system so they can be shared between configure scripts and configure runs. It is not useful on other systems. If its contents are invalid for some reason, the user may delete or edit it, or override documented cache variables on the `configure` command line.

By default, `configure` uses no cache file, to avoid problems caused by accidental use of stale cache files.

To enable caching, `configure` accepts --config-cache (or -C) to cache results in the file config.cache. Alternatively, --cache-file=*file* specifies that *file* be the cache file. The cache file is created if it does not exist already. When `configure` calls `configure` scripts in subdirectories, it uses the --cache-file argument so that they share the same cache. See Configuring Other Packages in Subdirectories, for information on configuring subdirectories with the `AC_CONFIG_SUBDIRS` macro.

config.status only pays attention to the cache file if it is given the --recheck option, which makes it rerun `configure`.

It is wrong to try to distribute cache files for particular system types. There is too much room for error in doing that, and too much administrative overhead in maintaining them. For any features that can’t be guessed automatically, use the standard method of the canonical system type and linking files (see Manual Configuration).

The site initialization script can specify a site-wide cache file to use, instead of the usual per-program cache. In this case, the cache file gradually accumulates information whenever someone runs a new `configure` script. (Running `configure` merges the new cache results with the existing cache file.) This may cause problems, however, if the system configuration (e.g., the installed libraries or compilers) changes and the stale cache file is not deleted.

If `configure` is interrupted at the right time when it updates a cache file outside of the build directory where the `configure` script is run, it may leave behind a temporary file named after the cache file with digits following it. You may safely delete such a file.

#### 7.4.3 Cache Checkpointing

If your configure script, or a macro called from configure.ac, happens to abort the configure process, it may be useful to checkpoint the cache a few times at key points using `AC_CACHE_SAVE`. Doing so reduces the amount of time it takes to rerun the configure script with (hopefully) the error that caused the previous abort corrected.

**Macro: **AC_CACHE_LOAD** ¶**

Loads values from existing cache file, or creates a new cache file if a cache file is not found. Called automatically from `AC_INIT`.

**Macro: **AC_CACHE_SAVE** ¶**

Flushes all cached values to the cache file. Called automatically from `AC_OUTPUT`, but it can be quite useful to call `AC_CACHE_SAVE` at key points in configure.ac.

For instance:

```
 ... AC_INIT, etc. ...
```

```
# Checks for programs.
AC_PROG_CC
AC_PROG_AWK
 ... more program checks ...
AC_CACHE_SAVE
```

```
# Checks for libraries.
AC_CHECK_LIB([nsl], [gethostbyname])
AC_CHECK_LIB([socket], [connect])
 ... more lib checks ...
AC_CACHE_SAVE
```

```
# Might abort...
AM_PATH_GTK([1.0.2], [], [AC_MSG_ERROR([GTK not in path])])
AM_PATH_GTKMM([0.9.5], [], [AC_MSG_ERROR([GTK not in path])])
```

```
 ... AC_OUTPUT, etc. ...
```

### 7.5 Printing Messages

`configure` scripts need to give users running them several kinds of information. The following macros print messages in ways appropriate for each kind. The arguments to all of them get enclosed in shell double quotes, so the shell performs variable and back-quote substitution on them.

These macros are all wrappers around the `printf` shell command. They direct output to the appropriate file descriptor (see File Descriptor Macros). `configure` scripts should rarely need to run `printf` directly to print messages for the user. Using these macros makes it easy to change how and when each kind of message is printed; such changes need only be made to the macro definitions and all the callers change automatically.

To diagnose static issues, i.e., when `autoconf` is run, see Diagnostic messages from M4sugar.

**Macro: **AC_MSG_CHECKING***(*feature-description*)* ¶**

Notify the user that `configure` is checking for a particular feature. This macro prints a message that starts with ‘checking ’ and ends with ‘...’ and no newline. It must be followed by a call to `AC_MSG_RESULT` to print the result of the check and the newline. The *feature-description* should be something like ‘whether the Fortran compiler accepts C++ comments’ or ‘for _Alignof’.

This macro prints nothing if `configure` is run with the --quiet or --silent option.

**Macro: **AC_MSG_RESULT***(*result-description*)* ¶**

Notify the user of the results of a check. *result-description* is almost always the value of the cache variable for the check, typically ‘yes’, ‘no’, or a file name. This macro should follow a call to `AC_MSG_CHECKING`, and the *result-description* should be the completion of the message printed by the call to `AC_MSG_CHECKING`.

This macro prints nothing if `configure` is run with the --quiet or --silent option.

**Macro: **AC_MSG_NOTICE***(*message*)* ¶**

Deliver the *message* to the user. It is useful mainly to print a general description of the overall purpose of a group of feature checks, e.g.,

```
AC_MSG_NOTICE([checking if stack overflow is detectable])
```

This macro prints nothing if `configure` is run with the --quiet or --silent option.

**Macro: **AC_MSG_ERROR***(*error-description*, [*exit-status* = ‘$?/1’])* ¶**

Notify the user of an error that prevents `configure` from completing. This macro prints an error message to the standard error output and exits `configure` with *exit-status* (‘$?’ by default, except that ‘0’ is converted to ‘1’). *error-description* should be something like ‘invalid value $HOME for \$HOME’.

The *error-description* should start with a lower-case letter, and “cannot” is preferred to “can’t”.

**Macro: **AC_MSG_FAILURE***(*error-description*, [*exit-status*])* ¶**

This `AC_MSG_ERROR` wrapper notifies the user of an error that prevents `configure` from completing *and* that additional details are provided in config.log. This is typically used when abnormal results are found during a compilation.

**Macro: **AC_MSG_WARN***(*problem-description*)* ¶**

Notify the `configure` user of a possible problem. This macro prints the message to the standard error output; `configure` continues running afterward, so macros that call `AC_MSG_WARN` should provide a default (back-up) behavior for the situations they warn about. *problem-description* should be something like ‘ln -s seems to make hard links’.

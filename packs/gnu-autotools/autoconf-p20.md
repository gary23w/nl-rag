---
title: "Autoconf (part 20/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 20/26
---

## 18 Obsolete Constructs

Autoconf changes, and throughout the years some constructs have been obsoleted. Most of the changes involve the macros, but in some cases the tools themselves, or even some concepts, are now considered obsolete.

You may completely skip this chapter if you are new to Autoconf. Its intention is mainly to help maintainers updating their packages by understanding how to move to more modern constructs.

### 18.1 Obsolete config.status Invocation

config.status now supports arguments to specify the files to instantiate; see config.status Invocation, for more details. Before, environment variables had to be used.

**Variable: **CONFIG_COMMANDS** ¶**

The tags of the commands to execute. The default is the arguments given to `AC_OUTPUT` and `AC_CONFIG_COMMANDS` in configure.ac.

**Variable: **CONFIG_FILES** ¶**

The files in which to perform ‘@*variable*@’ substitutions. The default is the arguments given to `AC_OUTPUT` and `AC_CONFIG_FILES` in configure.ac.

**Variable: **CONFIG_HEADERS** ¶**

The files in which to substitute C `#define` statements. The default is the arguments given to `AC_CONFIG_HEADERS`; if that macro was not called, config.status ignores this variable.

**Variable: **CONFIG_LINKS** ¶**

The symbolic links to establish. The default is the arguments given to `AC_CONFIG_LINKS`; if that macro was not called, config.status ignores this variable.

In config.status Invocation, using this old interface, the example would be:

```
config.h: stamp-h
stamp-h: config.h.in config.status
        CONFIG_COMMANDS= CONFIG_LINKS= CONFIG_FILES= \
          CONFIG_HEADERS=config.h ./config.status
        echo > stamp-h

Makefile: Makefile.in config.status
        CONFIG_COMMANDS= CONFIG_LINKS= CONFIG_HEADERS= \
          CONFIG_FILES=Makefile ./config.status
```

(If configure.ac does not call `AC_CONFIG_HEADERS`, there is no need to set `CONFIG_HEADERS` in the `make` rules. Equally for `CONFIG_COMMANDS`, etc.)

### 18.2 acconfig.h

In order to produce config.h.in, `autoheader` needs to build or to find templates for each symbol. Modern releases of Autoconf use `AH_VERBATIM` and `AH_TEMPLATE` (see Autoheader Macros), but in older releases a file, acconfig.h, contained the list of needed templates. `autoheader` copied comments and `#define` and `#undef` statements from acconfig.h in the current directory, if present. This file used to be mandatory if you `AC_DEFINE` any additional symbols.

Modern releases of Autoconf also provide `AH_TOP` and `AH_BOTTOM` if you need to prepend/append some information to config.h.in. Ancient versions of Autoconf had a similar feature: if ./acconfig.h contains the string ‘@TOP@’, `autoheader` copies the lines before the line containing ‘@TOP@’ into the top of the file that it generates. Similarly, if ./acconfig.h contains the string ‘@BOTTOM@’, `autoheader` copies the lines after that line to the end of the file it generates. Either or both of those strings may be omitted. An even older alternate way to produce the same effect in ancient versions of Autoconf is to create the files *file*.top (typically config.h.top) and/or *file*.bot in the current directory. If they exist, `autoheader` copies them to the beginning and end, respectively, of its output.

In former versions of Autoconf, the files used in preparing a software package for distribution were:

```
configure.ac --.   .------> autoconf* -----> configure
               +---+
[aclocal.m4] --+   `---.
[acsite.m4] ---'       |
                       +--> [autoheader*] -> [config.h.in]
[acconfig.h] ----.     |
                 +-----'
[config.h.top] --+
[config.h.bot] --'
```

Using only the `AH_` macros, configure.ac should be self-contained, and should not depend upon acconfig.h etc.

### 18.3 Using `autoupdate` to Modernize configure.ac

The `autoupdate` program updates a configure.ac file that calls Autoconf macros by their old names to use the current macro names. In version 2 of Autoconf, most of the macros were renamed to use a more uniform and descriptive naming scheme. See Macro Names, for a description of the new scheme. Although the old names still work (see Obsolete Macros, for a list of the old macros and the corresponding new names), you can make your configure.ac files more readable and make it easier to use the current Autoconf documentation if you update them to use the new macro names.

If given no arguments, `autoupdate` updates configure.ac, backing up the original version with the suffix ~ (or the value of the environment variable `SIMPLE_BACKUP_SUFFIX`, if that is set). If you give `autoupdate` an argument, it reads that file instead of configure.ac and writes the updated file to the standard output.

`autoupdate` accepts the following options:

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

Force the update even if the file has not changed. Disregard the cache.

**--include=*dir***

**-I *dir***

Also look for input files in *dir*. Multiple invocations accumulate. Directories are browsed from last to first.

**--prepend-include=*dir***

**-B *dir***

Prepend directory *dir* to the search path. This is used to include the language-specific files before any third-party macros.

### 18.4 Obsolete Macros

Several macros are obsoleted in Autoconf, for various reasons (typically they failed to quote properly, couldn’t be extended for more recent issues, etc.). They are still supported, but deprecated: their use should be avoided.

During the jump from Autoconf version 1 to version 2, most of the macros were renamed to use a more uniform and descriptive naming scheme, but their signature did not change. See Macro Names, for a description of the new naming scheme. Below, if there is just the mapping from old names to new names for these macros, the reader is invited to refer to the definition of the new macro for the signature and the description.

**Macro: **AC_AIX** ¶**

This macro is a platform-specific subset of `AC_USE_SYSTEM_EXTENSIONS` (see AC_USE_SYSTEM_EXTENSIONS).

**Macro: **AC_ALLOCA** ¶**

Replaced by `AC_FUNC_ALLOCA` (see AC_FUNC_ALLOCA).

**Macro: **AC_ARG_ARRAY** ¶**

Removed because of limited usefulness.

**Macro: **AC_C_CROSS** ¶**

This macro is obsolete; it does nothing.

**Macro: **AC_C_LONG_DOUBLE** ¶**

If the C compiler supports a working `long double` type with more range or precision than the `double` type, define `HAVE_LONG_DOUBLE`.

You should use `AC_TYPE_LONG_DOUBLE` or `AC_TYPE_LONG_DOUBLE_WIDER` instead. See Particular Type Checks.

**Macro: **AC_CANONICAL_SYSTEM** ¶**

Determine the system type and set output variables to the names of the canonical system types. See Getting the Canonical System Type, for details about the variables this macro sets.

The user is encouraged to use either `AC_CANONICAL_BUILD`, or `AC_CANONICAL_HOST`, or `AC_CANONICAL_TARGET`, depending on the needs. Using `AC_CANONICAL_TARGET` is enough to run the two other macros (see Getting the Canonical System Type).

**Macro: **AC_CHAR_UNSIGNED** ¶**

Replaced by `AC_C_CHAR_UNSIGNED` (see AC_C_CHAR_UNSIGNED).

**Macro: **AC_CHECK_TYPE***(*type*, *default*)* ¶**

Autoconf, up to 2.13, used to provide this version of `AC_CHECK_TYPE`, deprecated because of its flaws. First, although it is a member of the `CHECK` clan, it does more than just checking. Secondly, missing types are defined using `#define`, not `typedef`, and this can lead to problems in the case of pointer types.

This use of `AC_CHECK_TYPE` is obsolete and discouraged; see Generic Type Checks, for the description of the current macro.

If the type *type* is not defined, define it to be the C (or C++) builtin type *default*, e.g., ‘short int’ or ‘unsigned int’.

This macro is equivalent to:

```
AC_CHECK_TYPE([type], [],
  [AC_DEFINE_UNQUOTED([type], [default],
     [Define to 'default'
      if <sys/types.h> does not define.])])
```

In order to keep backward compatibility, the two versions of `AC_CHECK_TYPE` are implemented, selected using these heuristics:

1. If there are three or four arguments, the modern version is used.
2. If the second argument appears to be a C or C++ type, then the obsolete version is used. This happens if the argument is a C or C++ *builtin* type or a C identifier ending in ‘_t’, optionally followed by one of ‘[(* ’ and then by a string of zero or more characters taken from the set ‘[]()* _a-zA-Z0-9’.
3. If the second argument is spelled with the alphabet of valid C and C++ types, the user is warned and the modern version is used.
4. Otherwise, the modern version is used.

You are encouraged either to use a valid builtin type, or to use the equivalent modern code (see above), or better yet, to use `AC_CHECK_TYPES` together with

```
#ifndef HAVE_LOFF_T
typedef loff_t off_t;
#endif
```

**Macro: **AC_CHECKING***(*feature-description*)* ¶**

Same as

```
AC_MSG_NOTICE([checking feature-description...]
```

See AC_MSG_NOTICE.

**Macro: **AC_COMPILE_CHECK***(*echo-text*, *includes*, *function-body*, *action-if-true*, [*action-if-false*])* ¶**

This is an obsolete version of `AC_TRY_COMPILE` itself replaced by `AC_COMPILE_IFELSE` (see Running the Compiler), with the addition that it prints ‘checking for *echo-text*’ to the standard output first, if *echo-text* is non-empty. Use `AC_MSG_CHECKING` and `AC_MSG_RESULT` instead to print messages (see Printing Messages).

**Macro: **AC_CONST** ¶**

Replaced by `AC_C_CONST` (see AC_C_CONST).

**Macro: **AC_CROSS_CHECK** ¶**

Same as `AC_C_CROSS`, which is obsolete too, and does nothing `:-)`.

**Macro: **AC_CYGWIN** ¶**

Check for the Cygwin environment in which case the shell variable `CYGWIN` is set to ‘yes’. Don’t use this macro, the dignified means to check the nature of the host is using `AC_CANONICAL_HOST` (see Getting the Canonical System Type). As a matter of fact this macro is defined as:

```
AC_REQUIRE([AC_CANONICAL_HOST])[]dnl
case $host_os in
  *cygwin* ) CYGWIN=yes;;
         * ) CYGWIN=no;;
esac
```

Beware that the variable `CYGWIN` has a special meaning when running Cygwin, and should not be changed. That’s yet another reason not to use this macro.

**Macro: **AC_DECL_SYS_SIGLIST** ¶**

Same as:

```
AC_CHECK_DECLS([sys_siglist], [], [],
[#include <signal.h>
/* NetBSD declares sys_siglist in unistd.h.  */
#ifdef HAVE_UNISTD_H
# include <unistd.h>
#endif
])
```

See AC_CHECK_DECLS.

**Macro: **AC_DECL_YYTEXT** ¶**

Does nothing, now integrated in `AC_PROG_LEX` (see AC_PROG_LEX).

**Macro: **AC_DIAGNOSE***(*category*, *message*)* ¶**

Replaced by `m4_warn` (see m4_warn).

**Macro: **AC_DIR_HEADER** ¶**

Like calling `AC_FUNC_CLOSEDIR_VOID` (see AC_FUNC_CLOSEDIR_VOID) and `AC_HEADER_DIRENT` (see AC_HEADER_DIRENT), but defines a different set of C preprocessor macros to indicate which header file is found:

| Header | Old Symbol | New Symbol |
|---|---|---|
| dirent.h | `DIRENT` | `HAVE_DIRENT_H` |
| sys/ndir.h | `SYSNDIR` | `HAVE_SYS_NDIR_H` |
| sys/dir.h | `SYSDIR` | `HAVE_SYS_DIR_H` |
| ndir.h | `NDIR` | `HAVE_NDIR_H` |

**Macro: **AC_DYNIX_SEQ** ¶**

If on DYNIX/ptx, add -lseq to output variable `LIBS`. This macro used to be defined as

```
AC_CHECK_LIB([seq], [getmntent], [LIBS="-lseq $LIBS"])
```

now it is just `AC_FUNC_GETMNTENT` (see AC_FUNC_GETMNTENT).

**Macro: **AC_EXEEXT** ¶**

Defined the output variable `EXEEXT` based on the output of the compiler, which is now done automatically. Typically set to empty string if POSIX and ‘.exe’ if a DOS variant.

**Macro: **AC_EMXOS2** ¶**

Similar to `AC_CYGWIN` but checks for the EMX environment on OS/2 and sets `EMXOS2`. Don’t use this macro, the dignified means to check the nature of the host is using `AC_CANONICAL_HOST` (see Getting the Canonical System Type).

**Macro: **AC_ENABLE***(*feature*, *action-if-given*, [*action-if-not-given*])* ¶**

This is an obsolete version of `AC_ARG_ENABLE` that does not support providing a help string (see AC_ARG_ENABLE).

**Macro: **AC_ERROR** ¶**

Replaced by `AC_MSG_ERROR` (see AC_MSG_ERROR).

**Macro: **AC_FATAL***(*message*)* ¶**

Replaced by `m4_fatal` (see m4_fatal).

**Macro: **AC_FIND_X** ¶**

Replaced by `AC_PATH_X` (see AC_PATH_X).

**Macro: **AC_FIND_XTRA** ¶**

Replaced by `AC_PATH_XTRA` (see AC_PATH_XTRA).

**Macro: **AC_FOREACH** ¶**

Replaced by `m4_foreach_w` (see m4_foreach_w).

**Macro: **AC_FUNC_CHECK** ¶**

Replaced by `AC_CHECK_FUNC` (see AC_CHECK_FUNC).

**Macro: **AC_FUNC_SETVBUF_REVERSED** ¶**

Do nothing. Formerly, this macro checked whether `setvbuf` takes the buffering type as its second argument and the buffer pointer as the third, instead of the other way around, and defined `SETVBUF_REVERSED`. However, the last systems to have the problem were those based on SVR2, which became obsolete in 1987, and the macro is no longer needed.

**Macro: **AC_FUNC_WAIT3** ¶**

If `wait3` is found and fills in the contents of its third argument (a ‘struct rusage *’), which HP-UX does not do, define `HAVE_WAIT3`.

These days portable programs should use `waitpid`, not `wait3`, as `wait3` has been removed from POSIX.

**Macro: **AC_GCC_TRADITIONAL** ¶**

Replaced by `AC_PROG_GCC_TRADITIONAL` (see AC_PROG_GCC_TRADITIONAL), which is itself obsolete.

**Macro: **AC_GETGROUPS_T** ¶**

Replaced by `AC_TYPE_GETGROUPS` (see AC_TYPE_GETGROUPS).

**Macro: **AC_GETLOADAVG** ¶**

Replaced by `AC_FUNC_GETLOADAVG` (see AC_FUNC_GETLOADAVG).

**Macro: **AC_GNU_SOURCE** ¶**

This macro is a platform-specific subset of `AC_USE_SYSTEM_EXTENSIONS` (see AC_USE_SYSTEM_EXTENSIONS).

**Macro: **AC_HAVE_FUNCS** ¶**

Replaced by `AC_CHECK_FUNCS` (see AC_CHECK_FUNCS).

**Macro: **AC_HAVE_HEADERS** ¶**

Replaced by `AC_CHECK_HEADERS` (see AC_CHECK_HEADERS).

**Macro: **AC_HAVE_LIBRARY***(*library*, [*action-if-found*], [*action-if-not-found*], [*other-libraries*])* ¶**

This macro is equivalent to calling `AC_CHECK_LIB` with a *function* argument of `main`. In addition, *library* can be written as any of ‘foo’, -lfoo, or ‘libfoo.a’. In all of those cases, the compiler is passed -lfoo. However, *library* cannot be a shell variable; it must be a literal name. See AC_CHECK_LIB.

**Macro: **AC_HAVE_POUNDBANG** ¶**

Replaced by `AC_SYS_INTERPRETER` (see AC_SYS_INTERPRETER).

**Macro: **AC_HEADER_CHECK** ¶**

Replaced by `AC_CHECK_HEADER` (see AC_CHECK_HEADER).

**Macro: **AC_HEADER_EGREP** ¶**

Replaced by `AC_EGREP_HEADER` (see AC_EGREP_HEADER).

**Macro: **AC_HEADER_TIME** ¶**

This macro used to check whether it was possible to include time.h and sys/time.h in the same source file, defining `TIME_WITH_SYS_TIME` if so.

Nowadays, it is equivalent to ‘AC_CHECK_HEADERS([sys/time.h])’, although it does still define `TIME_WITH_SYS_TIME` for compatibility’s sake. time.h is universally present, and the systems on which sys/time.h conflicted with time.h are obsolete.

**Macro: **AC_HELP_STRING** ¶**

Replaced by `AS_HELP_STRING` (see AS_HELP_STRING).

**Macro: **AC_INIT***(*unique-file-in-source-dir*)* ¶**

Formerly `AC_INIT` used to have a single argument, and was equivalent to:

```
AC_INIT
AC_CONFIG_SRCDIR(unique-file-in-source-dir)
```

See AC_INIT and AC_CONFIG_SRCDIR.

**Macro: **AC_INLINE** ¶**

Replaced by `AC_C_INLINE` (see AC_C_INLINE).

**Macro: **AC_INT_16_BITS** ¶**

If the C type `int` is 16 bits wide, define `INT_16_BITS`. Use ‘AC_CHECK_SIZEOF(int)’ instead (see AC_CHECK_SIZEOF).

**Macro: **AC_IRIX_SUN** ¶**

If on IRIX (Silicon Graphics Unix), add -lsun to output `LIBS`. If you were using it to get `getmntent`, use `AC_FUNC_GETMNTENT` instead. If you used it for the NIS versions of the password and group functions, use ‘AC_CHECK_LIB(sun, getpwnam)’. Up to Autoconf 2.13, it used to be

```
AC_CHECK_LIB([sun], [getmntent], [LIBS="-lsun $LIBS"])
```

now it is defined as

```
AC_FUNC_GETMNTENT
AC_CHECK_LIB([sun], [getpwnam])
```

See AC_FUNC_GETMNTENT and AC_CHECK_LIB.

**Macro: **AC_ISC_POSIX** ¶**

This macro adds -lcposix to output variable `LIBS` if necessary for POSIX facilities. Sun dropped support for the obsolete INTERACTIVE Systems Corporation Unix on 2006-07-23. New programs need not use this macro. It is implemented as `AC_SEARCH_LIBS([strerror], [cposix])` (see AC_SEARCH_LIBS).

**Macro: **AC_LANG_C** ¶**

Same as ‘AC_LANG([C])’ (see AC_LANG).

**Macro: **AC_LANG_CPLUSPLUS** ¶**

Same as ‘AC_LANG([C++])’ (see AC_LANG).

**Macro: **AC_LANG_FORTRAN77** ¶**

Same as ‘AC_LANG([Fortran 77])’ (see AC_LANG).

**Macro: **AC_LANG_RESTORE** ¶**

Select the *language* that is saved on the top of the stack, as set by `AC_LANG_SAVE`, remove it from the stack, and call `AC_LANG(*language*)`. See Language Choice, for the preferred way to change languages.

**Macro: **AC_LANG_SAVE** ¶**

Remember the current language (as set by `AC_LANG`) on a stack. The current language does not change. `AC_LANG_PUSH` is preferred (see AC_LANG_PUSH).

**Macro: **AC_LINK_FILES***(*source*…, *dest*…)* ¶**

This is an obsolete version of `AC_CONFIG_LINKS` (see AC_CONFIG_LINKS. An updated version of:

```
AC_LINK_FILES(config/$machine.h config/$obj_format.h,
              host.h            object.h)
```

is:

```
AC_CONFIG_LINKS([host.h:config/$machine.h
                object.h:config/$obj_format.h])
```

**Macro: **AC_LN_S** ¶**

Replaced by `AC_PROG_LN_S` (see AC_PROG_LN_S).

**Macro: **AC_LONG_64_BITS** ¶**

Define `LONG_64_BITS` if the C type `long int` is 64 bits wide. Use the generic macro ‘AC_CHECK_SIZEOF([long int])’ instead (see AC_CHECK_SIZEOF).

**Macro: **AC_LONG_DOUBLE** ¶**

If the C compiler supports a working `long double` type with more range or precision than the `double` type, define `HAVE_LONG_DOUBLE`.

You should use `AC_TYPE_LONG_DOUBLE` or `AC_TYPE_LONG_DOUBLE_WIDER` instead. See Particular Type Checks.

**Macro: **AC_LONG_FILE_NAMES** ¶**

Replaced by

```
AC_SYS_LONG_FILE_NAMES
```

See AC_SYS_LONG_FILE_NAMES.

**Macro: **AC_MAJOR_HEADER** ¶**

Replaced by `AC_HEADER_MAJOR` (see AC_HEADER_MAJOR).

**Macro: **AC_MEMORY_H** ¶**

Used to define `NEED_MEMORY_H` if the `mem` functions were defined in memory.h. Today it is equivalent to ‘AC_CHECK_HEADERS([memory.h])’ (see AC_CHECK_HEADERS). Adjust your code to get the `mem` functions from string.h instead.

**Macro: **AC_MINGW32** ¶**

Similar to `AC_CYGWIN` but checks for the MinGW compiler environment and sets `MINGW32`. Don’t use this macro, the dignified means to check the nature of the host is using `AC_CANONICAL_HOST` (see Getting the Canonical System Type).

**Macro: **AC_MINIX** ¶**

This macro is a platform-specific subset of `AC_USE_SYSTEM_EXTENSIONS` (see AC_USE_SYSTEM_EXTENSIONS).

**Macro: **AC_MINUS_C_MINUS_O** ¶**

Replaced by `AC_PROG_CC_C_O` (see AC_PROG_CC_C_O).

**Macro: **AC_MMAP** ¶**

Replaced by `AC_FUNC_MMAP` (see AC_FUNC_MMAP).

**Macro: **AC_MODE_T** ¶**

Replaced by `AC_TYPE_MODE_T` (see AC_TYPE_MODE_T).

**Macro: **AC_OBJEXT** ¶**

Defined the output variable `OBJEXT` based on the output of the compiler, after .c files have been excluded. Typically set to ‘o’ if POSIX, ‘obj’ if a DOS variant. Now the compiler checking macros handle this automatically.

**Macro: **AC_OBSOLETE***(*this-macro-name*, [*suggestion*])* ¶**

Make M4 print a message to the standard error output warning that *this-macro-name* is obsolete, and giving the file and line number where it was called. *this-macro-name* should be the name of the macro that is calling `AC_OBSOLETE`. If *suggestion* is given, it is printed at the end of the warning message; for example, it can be a suggestion for what to use instead of *this-macro-name*.

For instance

```
AC_OBSOLETE([$0], [; use AC_CHECK_HEADERS(unistd.h) instead])dnl
```

You are encouraged to use `AU_DEFUN` instead, since it gives better services to the user (see AU_DEFUN).

**Macro: **AC_OFF_T** ¶**

Replaced by `AC_TYPE_OFF_T` (see AC_TYPE_OFF_T).

**Macro: **AC_OUTPUT***([*file*]…, [*extra-cmds*], [*init-cmds*])* ¶**

The use of `AC_OUTPUT` with arguments is deprecated. This obsoleted interface is equivalent to:

```
AC_CONFIG_FILES(file...)
AC_CONFIG_COMMANDS([default],
                   extra-cmds, init-cmds)
AC_OUTPUT
```

See AC_CONFIG_FILES, AC_CONFIG_COMMANDS, and AC_OUTPUT.

**Macro: **AC_OUTPUT_COMMANDS***(*extra-cmds*, [*init-cmds*])* ¶**

Specify additional shell commands to run at the end of config.status, and shell commands to initialize any variables from `configure`. This macro may be called multiple times. It is obsolete, replaced by `AC_CONFIG_COMMANDS` (see AC_CONFIG_COMMANDS).

Here is an unrealistic example:

```
fubar=27
AC_OUTPUT_COMMANDS(
  [AS_ECHO(["this is extra $fubar, and so on."])],
  [fubar=$fubar])
AC_OUTPUT_COMMANDS(
  [AS_ECHO(["this is another, extra, bit"])],
  [AS_ECHO(["init bit"])])
```

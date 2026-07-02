---
title: "Autoconf (part 2/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 2/26
---

## 4 Initialization and Output Files

Autoconf-generated `configure` scripts need some information about how to initialize, such as how to find the package’s source files and about the output files to produce. The following sections describe the initialization and the creation of output files.

### 4.1 Initializing `configure`

Every `configure` script must call `AC_INIT` before doing anything else that produces output. Calls to silent macros, such as `AC_DEFUN`, may also occur prior to `AC_INIT`, although these are generally used via aclocal.m4, since that is implicitly included before the start of configure.ac. The only other required macro is `AC_OUTPUT` (see Outputting Files).

**Macro: **AC_INIT***(*package*, *version*, [*bug-report*], [*tarname*], [*url*])* ¶**

Process any command-line arguments and perform initialization and verification.

Set the name of the *package* and its *version*. These are typically used in --version support, including that of `configure`. The optional argument *bug-report* should be the email to which users should send bug reports. The package *tarname* differs from *package*: the latter designates the full package name (e.g., ‘GNU Autoconf’), while the former is meant for distribution tar ball names (e.g., ‘autoconf’). It defaults to *package* with ‘GNU ’ stripped, lower-cased, and all characters other than alphanumerics and underscores are changed to ‘-’. If provided, *url* should be the home page for the package.

Leading and trailing whitespace is stripped from all the arguments to `AC_INIT`, and interior whitespace is collapsed to a single space. This means that, for instance, if you want to put several email addresses in *bug-report*, you can put each one on its own line:

```
# We keep having problems with the mail hosting for
# gnomovision.example, so give people an alternative.
AC_INIT([Gnomovision], [17.0.1], [
    bugs@gnomovision.example
    or gnomo-bugs@reliable-email.example
])
```

The arguments to `AC_INIT` may be computed by M4, when `autoconf` is run. For instance, if you want to include the package’s version number in the *tarname*, but you don’t want to repeat it, you can use a helper macro:

```
m4_define([gnomo_VERSION], [17.0.1])
AC_INIT([Gnomovision],
        m4_defn([gnomo_VERSION]),
        [bugs@gnomovision.example],
        [gnomo-]m4_defn([gnomo_VERSION]))
```

This uses `m4_defn` to produce the expansion of `gnomo_VERSION` *as a quoted string*, so that if there happen to be any more M4 macro names in `gnomo_VERSION`, they will not be expanded. See Renaming Macros in *GNU m4 macro processor*.

Continuing this example, if you don’t want to embed the version number in configure.ac at all, you can use `m4_esyscmd` to look it up somewhere else when `autoconf` is run:

```
m4_define([gnomo_VERSION],
  m4_esyscmd([build-aux/git-version-gen .tarball-version]))
AC_INIT([Gnomovision],
        m4_defn([gnomo_VERSION]),
        [bugs@gnomovision.example],
        [gnomo-]m4_defn([gnomo_VERSION]))
```

This uses the utility script `git-version-gen` to look up the package’s version in its version control metadata. This script is part of Gnulib (see Gnulib).

The arguments to `AC_INIT` are written into configure in several different places. Therefore, we strongly recommend that you write any M4 logic in `AC_INIT` arguments to be evaluated *before* `AC_INIT` itself is evaluated. For instance, in the above example, the second argument to `m4_define` is *not* quoted, so the `m4_esyscmd` is evaluated only once, and `gnomo_VERSION` is defined to the output of the command. If the second argument to `m4_define` were quoted, `m4_esyscmd` would be evaluated each time the *version* or *tarname* arguments were written to configure, and the command would be run repeatedly.

In some of the places where the arguments to `AC_INIT` are used, within configure, shell evaluation cannot happen. Therefore, the arguments to `AC_INIT` may *not* be computed when `configure` is run. If they contain any construct that isn’t always treated as literal by the shell (e.g. variable expansions), `autoconf` will issue an error.

The *tarname* argument is used to construct filenames. It should not contain wildcard characters, white space, or anything else that could be troublesome as part of a file or directory name.

Some of M4’s active characters (notably parentheses, square brackets, ‘,’ and ‘#’) commonly appear in URLs and lists of email addresses. If any of these characters appear in an argument to AC_INIT, that argument will probably need to be double-quoted to avoid errors and mistranscriptions. See M4 Quotation.

The following M4 macros (e.g., `AC_PACKAGE_NAME`), output variables (e.g., `PACKAGE_NAME`), and preprocessor symbols (e.g., `PACKAGE_NAME`), are defined by `AC_INIT`:

**`AC_PACKAGE_NAME`, `PACKAGE_NAME` ¶**

Exactly *package*.

**`AC_PACKAGE_TARNAME`, `PACKAGE_TARNAME` ¶**

Exactly *tarname*, possibly generated from *package*.

**`AC_PACKAGE_VERSION`, `PACKAGE_VERSION` ¶**

Exactly *version*.

**`AC_PACKAGE_STRING`, `PACKAGE_STRING` ¶**

Exactly ‘*package* *version*’.

**`AC_PACKAGE_BUGREPORT`, `PACKAGE_BUGREPORT` ¶**

Exactly *bug-report*, if one was provided. Typically an email address, or URL to a bug management web page.

**`AC_PACKAGE_URL`, `PACKAGE_URL` ¶**

Exactly *url*, if one was provided. If *url* was empty, but *package* begins with ‘GNU ’, then this defaults to ‘https://www.gnu.org/software/*tarname*/’, otherwise, no URL is assumed.

If your `configure` script does its own option processing, it should inspect ‘$@’ or ‘$*’ immediately after calling `AC_INIT`, because other Autoconf macros liberally use the `set` command to process strings, and this has the side effect of updating ‘$@’ and ‘$*’. However, we suggest that you use standard macros like `AC_ARG_ENABLE` instead of attempting to implement your own option processing. See Site Configuration.

### 4.2 Dealing with Autoconf versions

The following optional macros can be used to help choose the minimum version of Autoconf that can successfully compile a given configure.ac.

**Macro: **AC_PREREQ***(*version*)* ¶**

Ensure that a recent enough version of Autoconf is being used. If the version of Autoconf being used to create `configure` is earlier than *version*, print an error message to the standard error output and exit with failure (exit status is 63). For example:

```
AC_PREREQ([2.73])
```

This macro may be used before `AC_INIT`.

**Macro: **AC_AUTOCONF_VERSION** ¶**

This macro was introduced in Autoconf 2.62. It identifies the version of Autoconf that is currently parsing the input file, in a format suitable for `m4_version_compare` (see m4_version_compare); in other words, for this release of Autoconf, its value is ‘2.73’. One potential use of this macro is for writing conditional fallbacks based on when a feature was added to Autoconf, rather than using `AC_PREREQ` to require the newer version of Autoconf. However, remember that the Autoconf philosophy favors feature checks over version checks.

You should not expand this macro directly; use ‘m4_defn([AC_AUTOCONF_VERSION])’ instead. This is because some users might have a beta version of Autoconf installed, with arbitrary letters included in its version string. This means it is possible for the version string to contain the name of a defined macro, such that expanding `AC_AUTOCONF_VERSION` would trigger the expansion of that macro during rescanning, and change the version string to be different than what you intended to check.

### 4.3 Notices in `configure`

The following macros manage version numbers for `configure` scripts. Using them is optional.

**Macro: **AC_COPYRIGHT***(*copyright-notice*)* ¶**

State that, in addition to the Free Software Foundation’s copyright on the Autoconf macros, parts of your `configure` are covered by the *copyright-notice*.

The *copyright-notice* shows up in both the head of `configure` and in ‘configure --version’.

**Macro: **AC_REVISION***(*revision-info*)* ¶**

Copy revision stamp *revision-info* into the `configure` script, with any dollar signs or double-quotes removed. This macro lets you put a revision stamp from configure.ac into `configure` that the traditional version control systems RCS and CVS can update, without these systems changing it again when you check in the resulting `configure`. That way, you can determine easily which revision of configure.ac a particular `configure` corresponds to.

For example, this line in configure.ac:

```
AC_REVISION([$Revision: 1.1 $])
```

produces this in `configure`:

```
#!/bin/sh
# From configure.ac Revision: 1.30
```

### 4.4 Configure Input: Source Code, Macros, and Auxiliary Files

The following macros help you manage the contents of your source tree.

**Macro: **AC_CONFIG_SRCDIR***(*unique-file-in-source-dir*)* ¶**

Distinguish this package’s source directory from other source directories that might happen to exist in the file system. *unique-file-in-source-dir* should name a file that is unique to this package. `configure` will verify that this file exists in *srcdir*, before it runs any other checks.

Use of this macro is strongly recommended. It protects against people accidentally specifying the wrong directory with --srcdir. See `configure` Invocation, for more information.

Packages that use `aclocal` to generate aclocal.m4 should declare where local macros can be found using `AC_CONFIG_MACRO_DIRS`.

**Macro: **AC_CONFIG_MACRO_DIRS***(*dir1* [*dir2* ... *dirN*])* ¶**

**Macro: **AC_CONFIG_MACRO_DIR***(*dir*)* ¶**

Specify the given directories as the location of additional local Autoconf macros. These macros are intended for use by commands like `autoreconf` or `aclocal` that trace macro calls; they should be called directly from configure.ac so that tools that install macros for `aclocal` can find the macros’ declarations. Tools that want to learn which directories have been selected should trace `AC_CONFIG_MACRO_DIR_TRACE`, which will be called once per directory.

AC_CONFIG_MACRO_DIRS is the preferred form, and can be called multiple times and with multiple arguments; in such cases, directories in earlier calls are expected to be searched before directories in later calls, and directories appearing in the same call are expected to be searched in the order in which they appear in the call. For historical reasons, the macro AC_CONFIG_MACRO_DIR can also be used once, if it appears first, for tools such as older `libtool` that weren’t prepared to handle multiple directories. For example, a usage like

```
AC_CONFIG_MACRO_DIR([dir1])
AC_CONFIG_MACRO_DIRS([dir2])
AC_CONFIG_MACRO_DIRS([dir3 dir4])
```

will cause the trace of AC_CONFIG_MACRO_DIR_TRACE to appear four times, and should cause the directories to be searched in this order: ‘dir1 dir2 dir3 dir4’.

Note that if you use `aclocal` from an Automake release prior to 1.13 to generate aclocal.m4, you must also set `ACLOCAL_AMFLAGS = -I *dir1* [-I *dir2* ... -I *dirN*]` in your top-level Makefile.am. Due to a limitation in the Autoconf implementation of `autoreconf`, these include directives currently must be set on a single line in Makefile.am, without any backslash-newlines or makefile comments.

Some Autoconf macros require auxiliary scripts. `AC_PROG_INSTALL` (see Particular Program Checks) requires a fallback implementation of `install` called install-sh, and the `AC_CANONICAL` macros (see Manual Configuration) require the system-identification scripts config.sub and config.guess. Third-party tools, such as Automake and Libtool, may require additional auxiliary scripts.

By default, `configure` looks for these scripts next to itself, in *srcdir*. For convenience when working with subdirectories with their own configure scripts (see Configuring Other Packages in Subdirectories), if the scripts are not in *srcdir* it will also look in *srcdir*/.. and *srcdir*/../... All of the scripts must be found in the same directory.

If these default locations are not adequate, or simply to reduce clutter at the top level of the source tree, packages can use `AC_CONFIG_AUX_DIR` to declare where to look for auxiliary scripts.

**Macro: **AC_CONFIG_AUX_DIR***(*dir*)* ¶**

Look for auxiliary scripts in *dir*. Normally, *dir* should be a relative path, which is taken as relative to *srcdir*. If *dir* is an absolute path or contains shell variables, however, it is used as-is.

When the goal of using `AC_CONFIG_AUX_DIR` is to reduce clutter at the top level of the source tree, the conventional name for *dir* is build-aux. If you need portability to DOS variants, do not name the auxiliary directory aux. See File System Conventions.

**Macro: **AC_REQUIRE_AUX_FILE***(*file*)* ¶**

Declare that *file* is an auxiliary script needed by this configure script, and set the shell variable `ac_aux_dir` to the directory where it can be found. The value of `ac_aux_dir` is guaranteed to end with a ‘/’.

Macros that need auxiliary scripts must use this macro to register each script they need.

`configure` checks for all the auxiliary scripts it needs on startup, and exits with an error if any are missing.

`autoreconf` also detects missing auxiliary scripts. When used with the --install option, `autoreconf` will try to add missing scripts to the directory specified by `AC_CONFIG_AUX_DIR`, or to the top level of the source tree if `AC_CONFIG_AUX_DIR` was not used. It can always do this for the scripts needed by Autoconf core macros: install-sh, config.sub, and config.guess. Many other commonly-needed scripts are installed by the third-party tools that `autoreconf` knows how to run, such as missing for Automake and ltmain.sh for Libtool.

If you are using Automake, auxiliary scripts will automatically be included in the tarball created by `make dist`. If you are not using Automake you will need to arrange for auxiliary scripts to be included in tarballs yourself. Auxiliary scripts should normally *not* be checked into a version control system, for the same reasons that `configure` shouldn’t be.

The scripts needed by Autoconf core macros can be found in $(datadir)/autoconf/build-aux of the Autoconf installation (see Installation Directory Variables). install-sh can be downloaded from https://git.savannah.gnu.org/cgit/automake.git/plain/lib/install-sh. config.sub and config.guess can be downloaded from https://git.savannah.gnu.org/cgit/config.git/tree/.

### 4.5 Outputting Files

Every Autoconf script, e.g., configure.ac, should finish by calling `AC_OUTPUT`. That is the macro that generates and runs config.status, which in turn creates the makefiles and any other files resulting from configuration. This is the only required macro besides `AC_INIT` (see Configure Input: Source Code, Macros, and Auxiliary Files).

**Macro: **AC_OUTPUT** ¶**

Generate config.status and launch it. Call this macro once, at the end of configure.ac.

config.status performs all the configuration actions: all the output files (see Creating Configuration Files, macro `AC_CONFIG_FILES`), header files (see Configuration Header Files, macro `AC_CONFIG_HEADERS`), commands (see Running Arbitrary Configuration Commands, macro `AC_CONFIG_COMMANDS`), links (see Creating Configuration Links, macro `AC_CONFIG_LINKS`), subdirectories to configure (see Configuring Other Packages in Subdirectories, macro `AC_CONFIG_SUBDIRS`) are honored.

The location of your `AC_OUTPUT` invocation is the exact point where configuration actions are taken: any code afterwards is executed by `configure` once `config.status` was run. If you want to bind actions to `config.status` itself (independently of whether `configure` is being run), see Running Arbitrary Configuration Commands.

Historically, the usage of `AC_OUTPUT` was somewhat different. See Obsolete Macros, for a description of the arguments that `AC_OUTPUT` used to support.

If you run `make` in subdirectories, you should run it using the `make` variable `MAKE`. Most versions of `make` set `MAKE` to the name of the `make` program plus any options it was given. (But many do not include in it the values of any variables set on the command line, so those are not passed on automatically.) Some old versions of `make` do not set this variable. The following macro allows you to use it even with those versions.

**Macro: **AC_PROG_MAKE_SET** ¶**

If the Make command, `$MAKE` if set or else ‘make’, predefines `$(MAKE)`, define output variable `SET_MAKE` to be empty. Otherwise, define `SET_MAKE` to a macro definition that sets `$(MAKE)`, such as ‘MAKE=make’. Calls `AC_SUBST` for `SET_MAKE`.

If you use this macro, place a line like this in each Makefile.in that runs `MAKE` on other directories:

```
@SET_MAKE@
```

### 4.6 Performing Configuration Actions

configure is designed so that it appears to do everything itself, but there is actually a hidden slave: config.status. configure is in charge of examining your system, but it is config.status that actually takes the proper actions based on the results of configure. The most typical task of config.status is to *instantiate* files.

This section describes the common behavior of the four standard instantiating macros: `AC_CONFIG_FILES`, `AC_CONFIG_HEADERS`, `AC_CONFIG_COMMANDS` and `AC_CONFIG_LINKS`. They all have this prototype:

```
AC_CONFIG_ITEMS(tag..., [commands], [init-cmds])
```

where the arguments are:

***tag…***

A blank-or-newline-separated list of tags, which are typically the names of the files to instantiate.

You are encouraged to use literals as *tags*. In particular, you should avoid

```
AS_IF([...], [my_foos="$my_foos fooo"])
AS_IF([...], [my_foos="$my_foos foooo"])
AC_CONFIG_ITEMS([$my_foos])
```

and use this instead:

```
AS_IF([...], [AC_CONFIG_ITEMS([fooo])])
AS_IF([...], [AC_CONFIG_ITEMS([foooo])])
```

The macros `AC_CONFIG_FILES` and `AC_CONFIG_HEADERS` use special *tag* values: they may have the form ‘*output*’ or ‘*output*:*inputs*’. The file *output* is instantiated from its templates, *inputs* (defaulting to ‘*output*.in’).

‘AC_CONFIG_FILES([Makefile:boiler/top.mk:boiler/bot.mk])’, for example, asks for the creation of the file Makefile that contains the expansion of the output variables in the concatenation of boiler/top.mk and boiler/bot.mk.

The special value ‘-’ might be used to denote the standard output when used in *output*, or the standard input when used in the *inputs*. You most probably don’t need to use this in configure.ac, but it is convenient when using the command line interface of ./config.status, see config.status Invocation, for more details.

The *inputs* may be absolute or relative file names. In the latter case they are first looked for in the build tree, and then in the source tree. Input files should be text files, and a line length below 2000 bytes should be safe.

***commands***

Shell commands output literally into config.status, and associated with a tag that the user can use to tell config.status which commands to run. The commands are run each time a *tag* request is given to config.status, typically each time the file *tag* is created.

The variables set during the execution of `configure` are *not* available here: you first need to set them via the *init-cmds*. Nonetheless the following variables are pre-computed:

**`srcdir` ¶**

The name of the top source directory, assuming that the working directory is the top build directory. This is what `configure`’s --srcdir option sets.

**`ac_top_srcdir` ¶**

The name of the top source directory, assuming that the working directory is the current build directory.

**`ac_top_build_prefix` ¶**

The name of the top build directory, assuming that the working directory is the current build directory. It can be empty, or else ends with a slash, so that you may concatenate it.

**`ac_srcdir` ¶**

The name of the corresponding source directory, assuming that the working directory is the current build directory.

**`tmp` ¶**

The name of a temporary directory within the build tree, which you can use if you need to create additional temporary files. The directory is cleaned up when `config.status` is done or interrupted. Please use package-specific file name prefixes to avoid clashing with files that `config.status` may use internally.

The *current* directory refers to the directory (or pseudo-directory) containing the input part of *tags*. For instance, running

```
AC_CONFIG_COMMANDS([deep/dir/out:in/in.in], [...], [...])
```

with --srcdir=../package produces the following values:

```
# Argument of --srcdir
srcdir='../package'
# Reversing deep/dir
ac_top_build_prefix='../../'
# Concatenation of $ac_top_build_prefix and srcdir
ac_top_srcdir='../../../package'
# Concatenation of $ac_top_srcdir and deep/dir
ac_srcdir='../../../package/deep/dir'
```

independently of ‘in/in.in’.

***init-cmds***

Shell commands output *unquoted* near the beginning of config.status, and executed each time config.status runs (regardless of the tag). Because they are unquoted, for example, ‘$var’ is output as the value of `var`. *init-cmds* is typically used by configure to give config.status some variables it needs to run the *commands*.

You should be extremely cautious in your variable names: all the *init-cmds* share the same name space and may overwrite each other in unpredictable ways. Sorry...

All these macros can be called multiple times, with different *tag* values, of course!

### 4.7 Creating Configuration Files

Be sure to read the previous section, Performing Configuration Actions.

**Macro: **AC_CONFIG_FILES***(*file*…, [*cmds*], [*init-cmds*])* ¶**

Make `AC_OUTPUT` create each *file* by copying an input file (by default *file*.in), substituting the output variable values. This macro is one of the instantiating macros; see Performing Configuration Actions. See Substitutions in Makefiles, for more information on using output variables. See Setting Output Variables, for more information on creating them. This macro creates the directory that the file is in if it doesn’t exist. Usually, makefiles are created this way, but other files, such as .gdbinit, can be specified as well.

Typical calls to `AC_CONFIG_FILES` look like this:

```
AC_CONFIG_FILES([Makefile src/Makefile man/Makefile X/Imakefile])
AC_CONFIG_FILES([autoconf], [chmod +x autoconf])
```

You can override an input file name by appending to *file* a colon-separated list of input files. Examples:

```
AC_CONFIG_FILES([Makefile:boiler/top.mk:boiler/bot.mk]
                [lib/Makefile:boiler/lib.mk])
```

Doing this allows you to keep your file names acceptable to DOS variants, or to prepend and/or append boilerplate to the file.

The *file* names should not contain shell metacharacters. See Special Characters in Output Variables.

### 4.8 Substitutions in Makefiles

Each subdirectory in a distribution that contains something to be compiled or installed should come with a file Makefile.in, from which `configure` creates a file Makefile in that directory. To create Makefile, `configure` performs a simple variable substitution, replacing occurrences of ‘@*variable*@’ in Makefile.in with the value that `configure` has determined for that variable. Variables that are substituted into output files in this way are called *output variables*. They are ordinary shell variables that are set in `configure`. To make `configure` substitute a particular variable into the output files, the macro `AC_SUBST` must be called with that variable name as an argument. Any occurrences of ‘@*variable*@’ for other variables are left unchanged. See Setting Output Variables, for more information on creating output variables with `AC_SUBST`.

A software package that uses a `configure` script should be distributed with a file Makefile.in, but no makefile; that way, the user has to properly configure the package for the local system before compiling it.

See Makefile Conventions in *The GNU Coding Standards*, for more information on what to put in makefiles.

#### 4.8.1 Preset Output Variables

Some output variables are preset by the Autoconf macros. Some of the Autoconf macros set additional output variables, which are mentioned in the descriptions for those macros. See Output Variable Index, for a complete list of output variables. See Installation Directory Variables, for the list of the preset ones related to installation directories. Below are listed the other preset ones, many of which are precious variables (see Setting Output Variables, `AC_ARG_VAR`).

The preset variables which are available during config.status (see Performing Configuration Actions) may also be used during `configure` tests. For example, it is permissible to reference ‘$srcdir’ when constructing a list of directories to pass via the -I option during a compiler feature check. When used in this manner, coupled with the fact that `configure` is always run from the top build directory, it is sufficient to use just ‘$srcdir’ instead of ‘$top_srcdir’.

**Variable: **CFLAGS** ¶**

Debugging and optimization options for the C compiler. If it is not set in the environment when `configure` runs, the default value is set when you call `AC_PROG_CC` (or empty if you don’t). `configure` uses this variable when compiling or linking programs to test for C features.

If a compiler option affects only the behavior of the preprocessor (e.g., -D*name*), it should be put into `CPPFLAGS` instead. If it affects only the linker (e.g., -L*directory*), it should be put into `LDFLAGS` instead. If it affects only the compiler proper, `CFLAGS` is the natural home for it. If an option affects multiple phases of the compiler, though, matters get tricky:

- If an option selects a 32-bit or 64-bit build on a bi-arch system, it must be put direcly into `CC`, e.g., `CC='gcc -m64'`. This is necessary for `config.guess` to work right.
- Otherwise one approach is to put the option into `CC`. Another is to put it into both `CPPFLAGS` and `LDFLAGS`, but not into `CFLAGS`.

However, remember that some Makefile variables are reserved by the GNU Coding Standards for the use of the “user”—the person building the package. For instance, `CFLAGS` is one such variable.

Sometimes package developers are tempted to set user variables such as `CFLAGS` because it appears to make their job easier. However, the package itself should never set a user variable, particularly not to include switches that are required for proper compilation of the package. Since these variables are documented as being for the package builder, that person rightfully expects to be able to override any of these variables at build time. If the package developer needs to add switches without interfering with the user, the proper way to do that is to introduce an additional variable. Automake makes this easy by introducing `AM_CFLAGS` (see Flag Variables Ordering in *GNU Automake*), but the concept is the same even if Automake is not used.

**Variable: **configure_input** ¶**

A comment saying that the file was generated automatically by `configure` and giving the name of the input file. `AC_OUTPUT` adds a comment line containing this variable to the top of every makefile it creates. For other files, you should reference this variable in a comment at the top of each input file. For example, an input shell script should begin like this:

```
#!/bin/sh
# @configure_input@
```

The presence of that line also reminds people editing the file that it needs to be processed by `configure` in order to be used.

**Variable: **CPPFLAGS** ¶**

Preprocessor options for the C, C++, Objective C, and Objective C++ preprocessors and compilers. If it is not set in the environment when `configure` runs, the default value is empty. `configure` uses this variable when preprocessing or compiling programs to test for C, C++, Objective C, and Objective C++ features.

This variable’s contents should contain options like -I, -D, and -U that affect only the behavior of the preprocessor. Please see the explanation of `CFLAGS` for what you can do if an option affects other phases of the compiler as well.

Currently, `configure` always links as part of a single invocation of the compiler that also preprocesses and compiles, so it uses this variable also when linking programs. However, it is unwise to depend on this behavior because the GNU Coding Standards do not require it and many packages do not use `CPPFLAGS` when linking programs.

See Special Characters in Output Variables, for limitations that `CPPFLAGS` might run into.

**Variable: **CXXFLAGS** ¶**

Debugging and optimization options for the C++ compiler. It acts like `CFLAGS`, but for C++ instead of C.

**Variable: **DEFS** ¶**

-D options to pass to the C compiler. If `AC_CONFIG_HEADERS` is called, `configure` replaces ‘@DEFS@’ with -DHAVE_CONFIG_H instead (see Configuration Header Files). This variable is not defined while `configure` is performing its tests, only when creating the output files. See Setting Output Variables, for how to check the results of previous tests.

**Variable: **ECHO_C** ¶**

**Variable: **ECHO_N** ¶**

**Variable: **ECHO_T** ¶**

These obsolescent variables let you suppress the trailing newline from `echo` for question-answer message pairs. Nowadays it is better to use `AS_ECHO_N`.

**Variable: **ERLCFLAGS** ¶**

Debugging and optimization options for the Erlang compiler. If it is not set in the environment when `configure` runs, the default value is empty. `configure` uses this variable when compiling programs to test for Erlang features.

**Variable: **FCFLAGS** ¶**

Debugging and optimization options for the Fortran compiler. If it is not set in the environment when `configure` runs, the default value is set when you call `AC_PROG_FC` (or empty if you don’t). `configure` uses this variable when compiling or linking programs to test for Fortran features.

**Variable: **FFLAGS** ¶**

Debugging and optimization options for the Fortran 77 compiler. If it is not set in the environment when `configure` runs, the default value is set when you call `AC_PROG_F77` (or empty if you don’t). `configure` uses this variable when compiling or linking programs to test for Fortran 77 features.

**Variable: **LDFLAGS** ¶**

Options for the linker. If it is not set in the environment when `configure` runs, the default value is empty. `configure` uses this variable when linking programs to test for features in C, C++, Objective C, Objective C++, Fortran, Go, and Algol 68.

This variable’s contents should contain options like -s and -L that affect only the behavior of the linker. Please see the explanation of `CFLAGS` for what you can do if an option also affects other phases of the compiler.

Don’t use this variable to pass library names (-l) to the linker; use `LIBS` instead.

**Variable: **LIBS** ¶**

-l options to pass to the linker. The default value is empty, but some Autoconf macros may prepend extra libraries to this variable if those libraries are found and provide necessary functions, see Library Files. `configure` uses this variable when linking programs to test for C, C++, Objective C, Objective C++, Fortran, and Go features.

**Variable: **OBJCFLAGS** ¶**

Debugging and optimization options for the Objective C compiler. It acts like `CFLAGS`, but for Objective C instead of C.

**Variable: **OBJCXXFLAGS** ¶**

Debugging and optimization options for the Objective C++ compiler. It acts like `CXXFLAGS`, but for Objective C++ instead of C++.

**Variable: **GOFLAGS** ¶**

Debugging and optimization options for the Go compiler. It acts like `CFLAGS`, but for Go instead of C.

**Variable: **A68FLAGS** ¶**

Debugging and optimization options for the Algol 68 compiler. It acts like `CFLAGS`, but for Algol 68 instead of C.

**Variable: **builddir** ¶**

Rigorously equal to ‘.’. Added for symmetry only.

**Variable: **abs_builddir** ¶**

Absolute name of `builddir`.

**Variable: **top_builddir** ¶**

The relative name of the top level of the current build tree. In the top-level directory, this is the same as `builddir`.

**Variable: **top_build_prefix** ¶**

The relative name of the top level of the current build tree with final slash if nonempty. This is the same as `top_builddir`, except that it contains zero or more runs of `../`, so it should not be appended with a slash for concatenation. This helps for `make` implementations that otherwise do not treat ./file and file as equal in the top-level build directory.

**Variable: **abs_top_builddir** ¶**

Absolute name of `top_builddir`.

**Variable: **srcdir** ¶**

The name of the directory that contains the source code for that makefile.

**Variable: **abs_srcdir** ¶**

Absolute name of `srcdir`.

**Variable: **top_srcdir** ¶**

The name of the top-level source code directory for the package. In the top-level directory, this is the same as `srcdir`.

**Variable: **abs_top_srcdir** ¶**

Absolute name of `top_srcdir`.

#### 4.8.2 Installation Directory Variables

The following variables specify the directories for package installation, see Variables for Installation Directories in *The GNU Coding Standards*, for more information. Each variable corresponds to an argument of `configure`; trailing slashes are stripped so that expressions such as ‘${prefix}/lib’ expand with only one slash between directory names. See the end of this section for details on when and how to use these variables.

**Variable: **bindir** ¶**

The directory for installing executables that users run.

**Variable: **datadir** ¶**

The directory for installing idiosyncratic read-only architecture-independent data.

**Variable: **datarootdir** ¶**

The root of the directory tree for read-only architecture-independent data files.

**Variable: **docdir** ¶**

The directory for installing documentation files (other than Info and man).

**Variable: **dvidir** ¶**

The directory for installing documentation files in DVI format.

**Variable: **exec_prefix** ¶**

The installation prefix for architecture-dependent files. By default it’s the same as `prefix`. You should avoid installing anything directly to `exec_prefix`. However, the default value for directories containing architecture-dependent files should be relative to `exec_prefix`.

**Variable: **htmldir** ¶**

The directory for installing HTML documentation.

**Variable: **includedir** ¶**

The directory for installing C header files.

**Variable: **infodir** ¶**

The directory for installing documentation in Info format.

**Variable: **libdir** ¶**

The directory for installing object code libraries.

**Variable: **libexecdir** ¶**

The directory for installing executables that other programs run.

**Variable: **localedir** ¶**

The directory for installing locale-dependent but architecture-independent data, such as message catalogs. This directory usually has a subdirectory per locale.

**Variable: **localstatedir** ¶**

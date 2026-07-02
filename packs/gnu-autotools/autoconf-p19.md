---
title: "Autoconf (part 19/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 19/26
---

## 15 Site Configuration

`configure` scripts support several kinds of local configuration decisions. There are ways for users to specify where external software packages are, include or exclude optional features, install programs under modified names, and set default values for `configure` options.

### 15.1 Controlling Help Output

Users consult ‘configure --help’ to learn of configuration decisions specific to your package. By default, `configure` breaks this output into sections for each type of option; within each section, help strings appear in the order configure.ac defines them:

```
Optional Features:
  ...
  --enable-bar            include bar

Optional Packages:
  ...
  --with-foo              use foo
```

**Macro: **AC_PRESERVE_HELP_ORDER** ¶**

Request an alternate --help format, in which options of all types appear together, in the order defined. Call this macro before any `AC_ARG_ENABLE` or `AC_ARG_WITH`.

```
Optional Features and Packages:
  ...
  --enable-bar            include bar
  --with-foo              use foo
```

### 15.2 Working With External Software

Some packages require, or can optionally use, other software packages that are already installed. The user can give `configure` command line options to specify which such external software to use. The options have one of these forms:

```
--with-package[=arg]
--without-package
```

For example, --with-gnu-ld means work with the GNU linker instead of some other linker. --with-x means work with The X Window System.

The user can give an argument by following the package name with ‘=’ and the argument. Giving an argument of ‘no’ is for packages that are used by default; it says to *not* use the package. An argument that is neither ‘yes’ nor ‘no’ could include a name or number of a version of the other package, to specify more precisely which other package this program is supposed to work with. If no argument is given, it defaults to ‘yes’. --without-*package* is equivalent to --with-*package*=no.

Normally `configure` scripts complain about --with-*package* options that they do not support. See Controlling Checking of `configure` Options, for details, and for how to override the defaults.

For each external software package that may be used, configure.ac should call `AC_ARG_WITH` to detect whether the `configure` user asked to use it. Whether each package is used or not by default, and which arguments are valid, is up to you.

**Macro: **AC_ARG_WITH***(*package*, *help-string*, [*action-if-given*], [*action-if-not-given*])* ¶**

If the user gave `configure` the option --with-*package* or --without-*package*, run shell commands *action-if-given*. If neither option was given, run shell commands *action-if-not-given*. The name *package* indicates another software package that this program should work with. It should consist only of alphanumeric characters, dashes, plus signs, and dots.

The option’s argument is available to the shell commands *action-if-given* in the shell variable `withval`, which is actually just the value of the shell variable named `with_*package*`, with any non-alphanumeric characters in *package* changed into ‘_’. You may use that variable instead, if you wish.

Note that *action-if-not-given* is not expanded until the point that `AC_ARG_WITH` was expanded. If you need the value of `with_*package*` set to a default value by the time argument parsing is completed, use `m4_divert_text` to the `DEFAULTS` diversion (see m4_divert_text) (if done as an argument to `AC_ARG_WITH`, also provide non-diverted text to avoid a shell syntax error).

The argument *help-string* is a description of the option that looks like this:

```
  --with-readline         support fancy command line editing
```

*help-string* may be more than one line long, if more detail is needed. Just make sure the columns line up in ‘configure --help’. Avoid tabs in the help string. The easiest way to provide the proper leading whitespace is to format your *help-string* with the macro `AS_HELP_STRING` (see Making Your Help Strings Look Pretty).

The following example shows how to use the `AC_ARG_WITH` macro in a common situation. You want to let the user decide whether to enable support for an external library (e.g., the readline library); if the user specified neither --with-readline nor --without-readline, you want to enable support for readline only if the library is available on the system.

```
AC_ARG_WITH([readline],
  [AS_HELP_STRING([--with-readline],
    [support fancy command line editing @<:@default=check@:>@])],
  [],
  [: m4_divert_text([DEFAULTS], [with_readline=check])])

LIBREADLINE=
AS_IF([test "x$with_readline" != xno],
  [AC_CHECK_LIB([readline], [main],
    [AC_SUBST([LIBREADLINE], ["-lreadline -lncurses"])
     AC_DEFINE([HAVE_LIBREADLINE], [1],
               [Define if you have libreadline])
    ],
    [if test "x$with_readline" != xcheck; then
       AC_MSG_FAILURE(
         [--with-readline was given, but test for readline failed])
     fi
    ], -lncurses)])
```

The next example shows how to use `AC_ARG_WITH` to give the user the possibility to enable support for the readline library, in case it is still experimental and not well tested, and is therefore disabled by default.

```
AC_ARG_WITH([readline],
  [AS_HELP_STRING([--with-readline],
    [enable experimental support for readline])],
  [],
  [with_readline=no])

LIBREADLINE=
AS_IF([test "x$with_readline" != xno],
  [AC_CHECK_LIB([readline], [main],
    [AC_SUBST([LIBREADLINE], ["-lreadline -lncurses"])
     AC_DEFINE([HAVE_LIBREADLINE], [1],
               [Define if you have libreadline])
    ],
    [AC_MSG_FAILURE(
       [--with-readline was given, but test for readline failed])],
    [-lncurses])])
```

The last example shows how to use `AC_ARG_WITH` to give the user the possibility to disable support for the readline library, given that it is an important feature and that it should be enabled by default.

```
AC_ARG_WITH([readline],
  [AS_HELP_STRING([--without-readline],
    [disable support for readline])],
  [],
  [with_readline=yes])

LIBREADLINE=
AS_IF([test "x$with_readline" != xno],
  [AC_CHECK_LIB([readline], [main],
    [AC_SUBST([LIBREADLINE], ["-lreadline -lncurses"])
     AC_DEFINE([HAVE_LIBREADLINE], [1],
               [Define if you have libreadline])
    ],
    [AC_MSG_FAILURE(
       [readline test failed (--without-readline to disable)])],
    [-lncurses])])
```

These three examples can be easily adapted to the case where `AC_ARG_ENABLE` should be preferred to `AC_ARG_WITH` (see Choosing Package Options).

### 15.3 Choosing Package Options

If a software package has optional compile-time features, the user can give `configure` command line options to specify whether to compile them. The options have one of these forms:

```
--enable-feature[=arg]
--disable-feature
```

These options allow users to choose which optional features to build and install. --enable-*feature* options should never make a feature behave differently or cause one feature to replace another. They should only cause parts of the program to be built rather than left out.

The user can give an argument by following the feature name with ‘=’ and the argument. Giving an argument of ‘no’ requests that the feature *not* be made available. A feature with an argument looks like --enable-debug=stabs. If no argument is given, it defaults to ‘yes’. --disable-*feature* is equivalent to --enable-*feature*=no.

Normally `configure` scripts complain about --enable-*package* options that they do not support. See Controlling Checking of `configure` Options, for details, and for how to override the defaults.

For each optional feature, configure.ac should call `AC_ARG_ENABLE` to detect whether the `configure` user asked to include it. Whether each feature is included or not by default, and which arguments are valid, is up to you.

**Macro: **AC_ARG_ENABLE***(*feature*, *help-string*, [*action-if-given*], [*action-if-not-given*])* ¶**

If the user gave `configure` the option --enable-*feature* or --disable-*feature*, run shell commands *action-if-given*. If neither option was given, run shell commands *action-if-not-given*. The name *feature* indicates an optional user-level facility. It should consist only of alphanumeric characters, dashes, plus signs, and dots.

The option’s argument is available to the shell commands *action-if-given* in the shell variable `enableval`, which is actually just the value of the shell variable named `enable_*feature*`, with any non-alphanumeric characters in *feature* changed into ‘_’. You may use that variable instead, if you wish. The *help-string* argument is like that of `AC_ARG_WITH` (see Working With External Software).

Note that *action-if-not-given* is not expanded until the point that `AC_ARG_ENABLE` was expanded. If you need the value of `enable_*feature*` set to a default value by the time argument parsing is completed, use `m4_divert_text` to the `DEFAULTS` diversion (see m4_divert_text) (if done as an argument to `AC_ARG_ENABLE`, also provide non-diverted text to avoid a shell syntax error).

You should format your *help-string* with the macro `AS_HELP_STRING` (see Making Your Help Strings Look Pretty).

See the examples suggested with the definition of `AC_ARG_WITH` (see Working With External Software) to get an idea of possible applications of `AC_ARG_ENABLE`.

### 15.4 Making Your Help Strings Look Pretty

Properly formatting the ‘help strings’ which are used in `AC_ARG_WITH` (see Working With External Software) and `AC_ARG_ENABLE` (see Choosing Package Options) can be challenging. Specifically, you want your own ‘help strings’ to line up in the appropriate columns of ‘configure --help’ just like the standard Autoconf ‘help strings’ do. This is the purpose of the `AS_HELP_STRING` macro.

**Macro: **AS_HELP_STRING***(*left-hand-side*, *right-hand-side* [*indent-column* = ‘26’], [*wrap-column* = ‘79’])* ¶**

Expands into a help string that looks pretty when the user executes ‘configure --help’. It is typically used in `AC_ARG_WITH` (see Working With External Software) or `AC_ARG_ENABLE` (see Choosing Package Options). The following example makes this clearer.

```
AC_ARG_WITH([foo],
  [AS_HELP_STRING([--with-foo],
     [use foo (default is no)])],
  [use_foo=$withval],
  [use_foo=no])
```

Then the last few lines of ‘configure --help’ appear like this:

```
--enable and --with options recognized:
  --with-foo              use foo (default is no)
```

Macro expansion is performed on the first argument. However, the second argument of `AS_HELP_STRING` is treated as a whitespace separated list of text to be reformatted, and is not subject to macro expansion. Since it is not expanded, it should not be double quoted. See The Autoconf Language, for a more detailed explanation.

The `AS_HELP_STRING` macro is particularly helpful when the *left-hand-side* and/or *right-hand-side* are composed of macro arguments, as shown in the following example. Be aware that *left-hand-side* may not expand to unbalanced quotes, although quadrigraphs can be used.

```
AC_DEFUN([MY_ARG_WITH],
  [AC_ARG_WITH(m4_translit([[$1]], [_], [-]),
     [AS_HELP_STRING([--with-m4_translit([$1], [_], [-])],
                     [use $1 (default is $2)])],
     [use_[]$1=$withval],
     [use_[]$1=$2])])
MY_ARG_WITH([a_b], [no])
```

Here, the last few lines of ‘configure --help’ will include:

```
--enable and --with options recognized:
  --with-a-b              use a_b (default is no)
```

The parameters *indent-column* and *wrap-column* were introduced in Autoconf 2.62. Generally, they should not be specified; they exist for fine-tuning of the wrapping.

```
AS_HELP_STRING([--option], [description of option])
⇒  --option                description of option
AS_HELP_STRING([--option], [description of option], [15], [30])
⇒  --option     description of
⇒               option
```

### 15.5 Controlling Checking of `configure` Options

The `configure` script checks its command-line options against a list of known options, like --help or --config-cache. An unknown option ordinarily indicates a mistake by the user and `configure` halts with an error. However, by default unknown --with-*package* and --enable-*feature* options elicit only a warning, to support configuring entire source trees.

Source trees often contain multiple packages with a top-level `configure` script that uses the `AC_CONFIG_SUBDIRS` macro (see Configuring Other Packages in Subdirectories). Because the packages generally support different --with-*package* and --enable-*feature* options, the GNU Coding Standards say they must accept unrecognized options without halting. Even a warning message is undesirable here, so `AC_CONFIG_SUBDIRS` automatically disables the warnings.

This default behavior may be modified in two ways. First, the installer can invoke `configure --disable-option-checking` to disable these warnings, or invoke `configure --enable-option-checking=fatal` options to turn them into fatal errors, respectively. Second, the maintainer can use `AC_DISABLE_OPTION_CHECKING`.

**Macro: **AC_DISABLE_OPTION_CHECKING** ¶**

By default, disable warnings related to any unrecognized --with-*package* or --enable-*feature* options. This is implied by `AC_CONFIG_SUBDIRS`.

The installer can override this behavior by passing --enable-option-checking (enable warnings) or --enable-option-checking=fatal (enable errors) to `configure`.

### 15.6 Configuring Site Details

Some software packages require complex site-specific information. Some examples are host names to use for certain services, company names, and email addresses to contact. Since some configuration scripts generated by Metaconfig ask for such information interactively, people sometimes wonder how to get that information in Autoconf-generated configuration scripts, which aren’t interactive.

Such site configuration information should be put in a file that is edited *only by users*, not by programs. The location of the file can either be based on the `prefix` variable, or be a standard location such as the user’s home directory. It could even be specified by an environment variable. The programs should examine that file at runtime, rather than at compile time. Runtime configuration is more convenient for users and makes the configuration process simpler than getting the information while configuring. See Variables for Installation Directories in *The GNU Coding Standards*, for more information on where to put data files.

### 15.7 Transforming Program Names When Installing

Autoconf supports changing the names of programs when installing them. In order to use these transformations, configure.ac must call the macro `AC_ARG_PROGRAM`.

**Macro: **AC_ARG_PROGRAM** ¶**

Place in output variable `program_transform_name` a sequence of `sed` commands for changing the names of installed programs.

If any of the options described below are given to `configure`, program names are transformed accordingly. Otherwise, if `AC_CANONICAL_TARGET` has been called and a --target value is given, the target type followed by a dash is used as a prefix. Otherwise, no program name transformation is done.

#### 15.7.1 Transformation Options

You can specify name transformations by giving `configure` these command line options:

**--program-prefix=*prefix***

prepend *prefix* to the names;

**--program-suffix=*suffix***

append *suffix* to the names;

**--program-transform-name=*expression***

perform `sed` substitution *expression* on the names.

#### 15.7.2 Transformation Examples

These transformations are useful with programs that can be part of a cross-compilation development environment. For example, a cross-assembler running on x86-64 configured with --target=aarch64-linux-gnu is normally installed as aarch64-linux-gnu-as, rather than as, which could be confused with a native x86-64 assembler.

You can force a program name to begin with g, if you don’t want GNU programs installed on your system to shadow other programs with the same name. For example, if you configure GNU `diff` with --program-prefix=g, then when you run ‘make install’ it is installed as /usr/local/bin/gdiff.

As a more sophisticated example, you could use

```
--program-transform-name='s/^/g/; s/^gg/g/; s/^gless/less/'
```

to prepend ‘g’ to most of the program names in a source tree, excepting those like `gdb` that already have one and those like `less` and `lesskey` that aren’t GNU programs. (That is assuming that you have a source tree containing those programs that is set up to use this feature.)

One way to install multiple versions of some programs simultaneously is to append a version number to the name of one or both. For example, if you want to keep Autoconf version 1 around for awhile, you can configure Autoconf version 2 using --program-suffix=2 to install the programs as /usr/local/bin/autoconf2, /usr/local/bin/autoheader2, etc. Nevertheless, pay attention that only the binaries are renamed, therefore you’d have problems with the library files which might overlap.

#### 15.7.3 Transformation Rules

Here is how to use the variable `program_transform_name` in a Makefile.in:

```
PROGRAMS = cp ls rm
transform = @program_transform_name@
install:
        for p in $(PROGRAMS); do \
          $(INSTALL_PROGRAM) $$p $(DESTDIR)$(bindir)/`echo $$p | \
                                              sed '$(transform)'`; \
        done

uninstall:
        for p in $(PROGRAMS); do \
          rm -f $(DESTDIR)$(bindir)/`echo $$p | sed '$(transform)'`; \
        done
```

It is guaranteed that `program_transform_name` is never empty, and that there are no useless separators. Therefore you may safely embed `program_transform_name` within a sed program using ‘;’:

```
transform = @program_transform_name@
transform_exe = s/$(EXEEXT)$$//;$(transform);s/$$/$(EXEEXT)/
```

Whether to do the transformations on documentation files (Texinfo or `man`) is a tricky question; there seems to be no perfect answer, due to the several reasons for name transforming. Documentation is not usually particular to a specific architecture, and Texinfo files do not conflict with system documentation. But they might conflict with earlier versions of the same files, and `man` pages sometimes do conflict with system documentation. As a compromise, it is probably best to do name transformations on `man` pages but not on Texinfo manuals.

### 15.8 Setting Site Defaults

Autoconf-generated `configure` scripts allow your site to provide default values for some configuration values. You do this by creating site- and system-wide initialization files.

If the environment variable `CONFIG_SITE` is set, `configure` uses its value as a space-separated list of shell scripts to read; it is recommended that these be absolute file names. Otherwise, it reads the shell script *prefix*/share/config.site if it exists, then *prefix*/etc/config.site if it exists. Thus, settings in machine-specific files override those in machine-independent ones in case of conflict.

Site files can be arbitrary shell scripts, but only certain kinds of code are really appropriate to be in them. Because `configure` reads any cache file after it has read any site files, a site file can define a default cache file to be shared between all Autoconf-generated `configure` scripts run on that system (see Cache Files). If you set a default cache file in a site file, it is a good idea to also set the output variable `CC` in that site file, because the cache file is only valid for a particular compiler, but many systems have several available.

You can examine or override the value set by a command line option to `configure` in a site file; options set shell variables that have the same names as the options, with any dashes turned into underscores. The exceptions are that --without- and --disable- options are like giving the corresponding --with- or --enable- option and the value ‘no’. Thus, --cache-file=localcache sets the variable `cache_file` to the value ‘localcache’; --enable-warnings=no or --disable-warnings sets the variable `enable_warnings` to the value ‘no’; --prefix=/usr sets the variable `prefix` to the value ‘/usr’; etc.

Site files are also good places to set default values for other output variables, such as `CFLAGS`, if you need to give them non-default values: anything you would normally do, repetitively, on the command line. If you use non-default values for *prefix* or *exec_prefix* (wherever you locate the site file), you can set them in the site file if you specify it with the `CONFIG_SITE` environment variable.

You can set some cache values in the site file itself. Doing this is useful if you are cross-compiling, where it is impossible to check features that require running a test program. You could “prime the cache” by setting those values correctly for that system in *prefix*/etc/config.site. To find out the names of the cache variables you need to set, see the documentation of the respective Autoconf macro. If the variables or their semantics are undocumented, you may need to look for shell variables with ‘_cv_’ in their names in the affected `configure` scripts, or in the Autoconf M4 source code for those macros; but in that case, their name or semantics may change in a future Autoconf version.

The cache file is careful to not override any variables set in the site files. Similarly, you should not override command-line options in the site files. Your code should check that variables such as `prefix` and `cache_file` have their default values (as set near the top of `configure`) before changing them.

Here is a sample file /usr/share/local/gnu/share/config.site. The command ‘configure --prefix=/usr/share/local/gnu’ would read this file (if `CONFIG_SITE` is not set to a different file).

```
# /usr/share/local/gnu/share/config.site for configure
#
# Change some defaults.
test "$prefix" = NONE && prefix=/usr/share/local/gnu
test "$exec_prefix" = NONE && exec_prefix=/usr/local/gnu
test "$sharedstatedir" = '${prefix}/com' && sharedstatedir=/var
test "$localstatedir" = '${prefix}/var' && localstatedir=/var
test "$runstatedir" = '${localstatedir}/run' && runstatedir=/run

# Give Autoconf 2.x generated configure scripts a shared default
# cache file for feature test results, architecture-specific.
if test "$cache_file" = /dev/null; then
  cache_file="$prefix/var/config.cache"
  # A cache file is only valid for one C compiler.
  CC=gcc
fi
```

Another use of config.site is for priming the directory variables in a manner consistent with the Filesystem Hierarchy Standard (FHS). Once the following file is installed at /usr/share/config.site, a user can execute simply `./configure --prefix=/usr` to get all the directories chosen in the locations recommended by FHS.

```
# /usr/share/config.site for FHS defaults when installing below /usr,
# and the respective settings were not changed on the command line.
if test "$prefix" = /usr; then
  test "$sysconfdir" = '${prefix}/etc' && sysconfdir=/etc
  test "$sharedstatedir" = '${prefix}/com' && sharedstatedir=/var
  test "$localstatedir" = '${prefix}/var' && localstatedir=/var
fi
```

Likewise, on platforms where 64-bit libraries are built by default, then installed in /usr/local/lib64 instead of /usr/local/lib, it is appropriate to install /usr/local/share/config.site:

```
# /usr/local/share/config.site for platforms that prefer
# the directory /usr/local/lib64 over /usr/local/lib.
test "$libdir" = '${exec_prefix}/lib' && libdir='${exec_prefix}/lib64'
```


## 16 Running `configure` Scripts

Below are instructions on how to configure a package that uses a `configure` script, suitable for inclusion as an INSTALL file in the package. A plain-text version of INSTALL which you may use comes with Autoconf.

### 16.1 Basic Installation

The following shell commands:

```
test -f configure || ./bootstrap
./configure
make
make install
```

should configure, build, and install this package. The first line, which bootstraps, is intended for developers; when building from distribution tarballs it does nothing and can be skipped. A package might name the bootstrapping script differently; if the name is autogen.sh, for example, the first line should say `./autogen.sh` instead of `./bootstrap`.

The following more-detailed instructions are generic; see the README file for instructions specific to this package. More recommendations for GNU packages can be found in Makefile Conventions in *GNU Coding Standards*.

Many packages have scripts meant for developers instead of ordinary builders, as they may use developer tools that are less commonly installed, or they may access the network, which has privacy implications. These scripts attempt to bootstrap by building the `configure` script and related files, possibly using developer tools or the network. Because the output of bootstrapping is system-independent, it is normally run by a package developer so that its output can be put into the distribution tarball and ordinary builders and users need not bootstrap. Some packages have commands like `./autopull.sh` and `./autogen.sh` that you can run instead of `./bootstrap`, for more fine-grained control over bootstrapping.

The `configure` script attempts to guess correct values for various system-dependent variables used during compilation. It uses those values to create a Makefile in each directory of the package. It may also create one or more .h files containing system-dependent definitions. Finally, it creates a script config.status that you can run in the future to recreate the current configuration, and a file config.log containing output useful for debugging `configure`.

It can also use an optional file (typically called config.cache and enabled with --cache-file=config.cache or simply -C) that saves the results of its tests to speed up reconfiguring. Caching is disabled by default to prevent problems with accidental use of stale cache files.

If you need to do unusual things to compile the package, please try to figure out how `configure` could check whether to do them, and mail diffs or instructions to the address given in the README so they can be considered for the next release. If you are using the cache, and at some point config.cache contains results you don’t want to keep, you may remove or edit it.

The `autoconf` program generates configure from the file configure.ac. Normally you should edit configure.ac instead of editing configure directly.

The simplest way to compile this package is:

1. `cd` to the directory containing the package’s source code.
2. If this is a developer checkout and file configure does not yet exist, run the bootstrapping script (typically `./bootstrap` or `./autogen.sh`) to bootstrap and create the file. You may need special developer tools and network access to bootstrap, and the network access may have privacy implications.
3. Type ‘./configure’ to configure the package for your system. This might take a while. While running, `configure` prints messages telling which features it is checking for.
4. Type ‘make’ to compile the package.
5. Optionally, type ‘make check’ to run any self-tests that come with the package, generally using the just-built uninstalled binaries.
6. Type ‘make install’ to install the programs and any data files and documentation. When installing into a prefix owned by root, it is recommended that the package be configured and built as a regular user, and only the ‘make install’ phase executed with root privileges.
7. Optionally, type ‘make installcheck’ to repeat any self-tests, but this time using the binaries in their final installed location. This target does not install anything. Running this target as a regular user, particularly if the prior ‘make install’ required root privileges, verifies that the installation completed correctly.
8. You can remove the program binaries and object files from the source code directory by typing ‘make clean’. To also remove the files that `configure` created (so you can compile the package for a different kind of computer), type ‘make distclean’. There is also a ‘make maintainer-clean’ target, but that is intended mainly for the package’s developers. If you use it, you may have to bootstrap again.
9. If the package follows the GNU Coding Standards, you can type ‘make uninstall’ to remove the installed files.

### 16.2 Installation Prerequisites

Installation requires a POSIX-like environment with a shell and at least the following standard utilities:

> `awk cat cp diff echo expr false ls mkdir mv printf pwd rm rmdir sed sort test tr`

This package’s installation may need other standard utilities such as `grep`, `make`, `sleep` and `touch`, along with compilers like `gcc`.

### 16.3 Compilers and Options

Some systems require unusual options for compilation or linking that the `configure` script does not know about. Run ‘./configure --help’ for details on some of the pertinent environment variables.

You can give `configure` initial values for configuration parameters by setting variables in the command line or in the environment. Here is an example:

```
./configure CC=gcc CFLAGS=-g LIBS=-lposix
```

Defining Variables and Preset Output Variables for more details.

### 16.4 Compiling For Multiple Architectures

You can compile the package for more than one kind of computer at the same time, by placing the object files for each system in their own directory. To do this, you can use GNU `make`. `cd` to the directory where you want the object files and executables to go and run the `configure` script. `configure` automatically checks for the source code in the directory that `configure` is in and in ... This is known as a *VPATH* build.

With a non-GNU `make`, it is safer to compile the package for one system at a time in the source code directory. After you have installed the package for one system, use ‘make distclean’ before reconfiguring for another system.

Some platforms, notably macOS, support “fat” or “universal” binaries, where a single binary can execute on different architectures. On these platforms you can configure and compile just once, with options specific to that platform.

### 16.5 Installation Names

By default, ‘make install’ installs the package’s commands under /usr/local/bin, include files under /usr/local/include, etc. You can specify an installation prefix other than /usr/local by giving `configure` the option --prefix=*prefix*, where *prefix* must be an absolute file name.

You can specify separate installation prefixes for architecture-specific files and architecture-independent files. If you pass the option --exec-prefix=*prefix* to `configure`, the package uses *prefix* as the prefix for installing programs and libraries. Documentation and other data files still use the regular prefix.

In addition, if you use an unusual directory layout you can give options like --bindir=*dir* to specify different values for particular kinds of files. Run ‘configure --help’ for a list of the directories you can set and what kinds of files go in them. In general, the default for these options is expressed in terms of ‘${prefix}’, so that specifying just --prefix will affect all of the other directory specifications that were not explicitly provided.

The most portable way to affect installation locations is to pass the correct locations to `configure`; however, many packages provide one or both of the following shortcuts of passing variable assignments to the ‘make install’ command line to change installation locations without having to reconfigure or recompile.

The first method involves providing an override variable for each affected directory. For example, ‘make install prefix=/alternate/directory’ will choose an alternate location for all directory configuration variables that were expressed in terms of ‘${prefix}’. Any directories that were specified during `configure`, but not in terms of ‘${prefix}’, must each be overridden at install time for the entire installation to be relocated. The approach of makefile variable overrides for each directory variable is required by the GNU Coding Standards, and ideally causes no recompilation. However, some platforms have known limitations with the semantics of shared libraries that end up requiring recompilation when using this method, particularly noticeable in packages that use GNU Libtool.

The second method involves providing the ‘DESTDIR’ variable. For example, ‘make install DESTDIR=/alternate/directory’ will prepend ‘/alternate/directory’ before all installation names. The approach of ‘DESTDIR’ overrides is not required by the GNU Coding Standards, and does not work on platforms that have drive letters. On the other hand, it does better at avoiding recompilation issues, and works well even when some directory options were not specified in terms of ‘${prefix}’ at `configure` time.

### 16.6 Optional Features

If the package supports it, you can cause programs to be installed with an extra prefix or suffix on their names by giving `configure` the option --program-prefix=*PREFIX* or --program-suffix=*SUFFIX*.

Some packages pay attention to --enable-*feature* and --disable-*feature* options to `configure`, where *feature* indicates an optional part of the package. They may also pay attention to --with-*package* and --without-*package* options, where *package* is something like ‘gnu-ld’. ‘./configure --help’ should mention the --enable-... and --with-... options that the package recognizes.

Some packages offer the ability to configure how verbose the execution of `make` will be. For these packages, running ‘./configure --enable-silent-rules’ sets the default to minimal output, which can be overridden with `make V=1`; while running ‘./configure --disable-silent-rules’ sets the default to verbose, which can be overridden with `make V=0`.

### 16.7 Specifying a System Type

By default `configure` builds for the current system. To create binaries that can run on a different system type, specify a --host=*type* option along with compiler variables that specify how to generate object code for *type*. For example, to create binaries intended to run on a 64-bit ARM processor:

```
./configure --host=aarch64-linux-gnu \
   CC=aarch64-linux-gnu-gcc \
   CXX=aarch64-linux-gnu-g++
```

If done on a machine that can execute these binaries (e.g., via `qemu-aarch64`, `$QEMU_LD_PREFIX`, and Linux’s `binfmt_misc` capability), the build behaves like a native build. Otherwise it is a cross-build: `configure` will make cross-compilation guesses instead of running test programs, and `make check` will not work.

A system type can either be a short name like ‘mingw64’, or a canonical name like ‘x86_64-pc-linux-gnu’. Canonical names have the form *cpu*-*company*-*system* where *system* is either *os* or *kernel*-*os*. To canonicalize and validate a system type, you can run the command config.sub, which is often squirreled away in a subdirectory like build-aux. For example:

```
$ build-aux/config.sub arm64-linux
aarch64-unknown-linux-gnu
$ build-aux/config.sub riscv-lnx
Invalid configuration 'riscv-lnx': OS 'lnx' not recognized
```

You can look at the config.sub file to see which types are recognized. If the file is absent, this package does not need the system type.

If `configure` fails with the diagnostic “cannot guess build type”. config.sub did not recognize your system’s type. In this case, first fetch the newest versions of these files from the GNU config package. If that fixes things, please report it to the maintainers of the package containing `configure`. Otherwise, you can try the configure option --build=*type* where *type* comes close to your system type; also, please report the problem to config-patches@gnu.org.

For more details about configuring system types, see Manual Configuration.

### 16.8 Sharing Defaults

If you want to set default values for `configure` scripts to share, you can create a site shell script called config.site that gives default values for variables like `CC`, `cache_file`, and `prefix`. `configure` looks for *prefix*/share/config.site if it exists, then *prefix*/etc/config.site if it exists. Or, you can set the `CONFIG_SITE` environment variable to the location of the site script. A warning: not all `configure` scripts look for a site script.

### 16.9 Defining Variables

Variables not defined in a site shell script can be set in the environment passed to `configure`. However, some packages may run configure again during the build, and the customized values of these variables may be lost. In order to avoid this problem, you should set them in the `configure` command line, using ‘VAR=value’. For example:

```
./configure CC=/usr/local2/bin/gcc
```

causes the specified `gcc` to be used as the C compiler (unless it is overridden in the site shell script).

Unfortunately, this technique does not work for `CONFIG_SHELL` due to an Autoconf limitation. Until the limitation is lifted, you can use this workaround:

```
CONFIG_SHELL=/bin/bash ./configure CONFIG_SHELL=/bin/bash
```

### 16.10 `configure` Invocation

`configure` recognizes the following options to control how it operates.

**--help**

**-h**

Print a summary of all of the options to `configure`, and exit.

**--help=short**

**--help=recursive**

Print a summary of the options unique to this package’s `configure`, and exit. The `short` variant lists options used only in the top level, while the `recursive` variant lists options also present in any nested packages.

**--version**

**-V**

Print the version of Autoconf used to generate the `configure` script, and exit.

**--cache-file=*file* ¶**

Enable the cache: use and save the results of the tests in *file*, traditionally config.cache. *file* defaults to /dev/null to disable caching.

**--config-cache**

**-C**

Alias for --cache-file=config.cache.

**--srcdir=*dir***

Look for the package’s source code in directory *dir*. Usually `configure` can determine that directory automatically.

**--prefix=*dir***

Use *dir* as the installation prefix. Installation Names for more details, including other options available for fine-tuning the installation locations.

**--host=*type***

Build binaries for system *type*. See Specifying a System Type.

**--enable-*feature***

**--disable-*feature***

Enable or disable the optional *feature*. See Optional Features.

**--with-*package***

**--without-*package***

Use or omit *package* when building. See Optional Features.

**--quiet**

**--silent**

**-q**

Do not print messages saying which checks are being made. To suppress all normal output, redirect it to /dev/null (any error messages will still be shown).

**--no-create**

**-n**

Run the configure checks, but stop before creating any output files.

`configure` also recognizes several environment variables, and accepts some other, less widely useful, options. Run ‘configure --help’ for more details.


## 17 config.status Invocation

The `configure` script creates a file named config.status, which actually configures, *instantiates*, the template files. It also records the configuration options that were specified when the package was last configured in case reconfiguring is needed.

Synopsis:

```
./config.status [option]... [tag]...
```

It configures each *tag*; if none are specified, all the templates are instantiated. A *tag* refers to a file or other tag associated with a configuration action, as specified by an `AC_CONFIG_*ITEMS*` macro (see Performing Configuration Actions). The files must be specified without their dependencies, as in

```
./config.status foobar
```

not

```
./config.status foobar:foo.in:bar.in
```

The supported options are:

**--help**

**-h**

Print a summary of the command line options, the list of the template files, and exit.

**--version**

**-V**

Print the version number of Autoconf and the configuration settings, and exit.

**--config**

Print the configuration settings in reusable way, quoted for the shell, and exit. For example, for a debugging build that otherwise reuses the configuration from a different build directory *build-dir* of a package in *src-dir*, you could use the following:

```
args=`build-dir/config.status --config`
eval src-dir/configure "$args" CFLAGS=-g --srcdir=src-dir
```

Note that it may be necessary to override a --srcdir setting that was saved in the configuration, if the arguments are used in a different build directory.

**--silent**

**--quiet**

**-q**

Do not print progress messages.

**--debug**

**-d**

Don’t remove the temporary files.

**--file=*file*[:*template*]**

Require that *file* be instantiated as if ‘AC_CONFIG_FILES(*file*:*template*)’ was used. Both *file* and *template* may be ‘-’ in which case the standard output and/or standard input, respectively, is used. If a *template* file name is relative, it is first looked for in the build tree, and then in the source tree. See Performing Configuration Actions, for more details.

This option and the following ones provide one way for separately distributed packages to share the values computed by `configure`. Doing so can be useful if some of the packages need a superset of the features that one of them, perhaps a common library, does. These options allow a config.status file to create files other than the ones that its configure.ac specifies, so it can be used for a different package, or for extracting a subset of values. For example,

```
echo '@CC@' | ./config.status --file=-
```

provides the value of `@CC@` on standard output.

**--header=*file*[:*template*]**

Same as --file above, but with ‘AC_CONFIG_HEADERS’.

**--recheck**

Ask config.status to update itself and exit (no instantiation). This option is useful if you change `configure`, so that the results of some tests might be different from the previous run. The --recheck option reruns `configure` with the same arguments you used before, plus the --no-create option, which prevents `configure` from running config.status and creating Makefile and other files, and the --no-recursion option, which prevents `configure` from running other `configure` scripts in subdirectories. (This is so other Make rules can run config.status when it changes; see Automatic Remaking, for an example).

config.status checks several optional environment variables that can alter its behavior:

**Variable: **CONFIG_SHELL** ¶**

The shell with which to run `configure`. It must be Bourne-compatible, and the absolute name of the shell should be passed. The default is a shell that supports `LINENO` if available, and /bin/sh otherwise.

**Variable: **CONFIG_STATUS** ¶**

The file name to use for the shell script that records the configuration. The default is ./config.status. This variable is useful when one package uses parts of another and the `configure` scripts shouldn’t be merged because they are maintained separately.

You can use ./config.status in your makefiles. For example, in the dependencies given above (see Automatic Remaking), config.status is run twice when configure.ac has changed. If that bothers you, you can make each run only regenerate the files for that rule:

```
config.h: stamp-h
stamp-h: config.h.in config.status
        ./config.status config.h
        echo > stamp-h

Makefile: Makefile.in config.status
        ./config.status Makefile
```

The calling convention of config.status has changed; see Obsolete config.status Invocation, for details.

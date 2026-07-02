---
title: "Autoconf (part 3/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 3/26
---

# Autoconf

The directory for installing modifiable single-machine data. Content in this directory typically survives a reboot.

**Variable: **runstatedir** ¶**

The directory for installing temporary modifiable single-machine data. Content in this directory survives as long as the process is running (such as pid files), as contrasted with /tmp that may be periodically cleaned. Conversely, this directory is typically cleaned on a reboot. By default, this is a subdirectory of `localstatedir`.

**Variable: **mandir** ¶**

The top-level directory for installing documentation in man format.

**Variable: **oldincludedir** ¶**

The directory for installing C header files for non-GCC compilers.

**Variable: **pdfdir** ¶**

The directory for installing PDF documentation.

**Variable: **prefix** ¶**

The common installation prefix for all files. If `exec_prefix` is defined to a different value, `prefix` is used only for architecture-independent files.

**Variable: **psdir** ¶**

The directory for installing PostScript documentation.

**Variable: **sbindir** ¶**

The directory for installing executables that system administrators run.

**Variable: **sharedstatedir** ¶**

The directory for installing modifiable architecture-independent data.

**Variable: **sysconfdir** ¶**

The directory for installing read-only single-machine data.

Most of these variables have values that rely on `prefix` or `exec_prefix`. It is deliberate that the directory output variables keep them unexpanded: typically ‘@datarootdir@’ is replaced by ‘${prefix}/share’, not ‘/usr/local/share’, and ‘@datadir@’ is replaced by ‘${datarootdir}’.

This behavior is mandated by the GNU Coding Standards, so that when the user runs:

**‘make’**

she can still specify a different prefix from the one specified to `configure`, in which case, if needed, the package should hard code dependencies corresponding to the make-specified prefix.

**‘make install’**

she can specify a different installation location, in which case the package *must* still depend on the location which was compiled in (i.e., never recompile when ‘make install’ is run). This is an extremely important feature, as many people may decide to install all the files of a package grouped together, and then install links from the final locations to there.

In order to support these features, it is essential that `datarootdir` remains defined as ‘${prefix}/share’, so that its value can be expanded based on the current value of `prefix`.

A corollary is that you should not use these variables except in makefiles. For instance, instead of trying to evaluate `datadir` in configure and hard-coding it in makefiles using e.g., ‘AC_DEFINE_UNQUOTED([DATADIR], ["$datadir"], [Data directory.])’, you should add -DDATADIR='$(datadir)' to your makefile’s definition of `CPPFLAGS` (`AM_CPPFLAGS` if you are also using Automake).

Similarly, you should not rely on `AC_CONFIG_FILES` to replace `bindir` and friends in your shell scripts and other files; instead, let `make` manage their replacement. For instance Autoconf ships templates of its shell scripts ending with ‘.in’, and uses a makefile snippet similar to the following to build scripts like `autoheader` and `autom4te`:

```
edit = sed \
        -e 's|@bindir[@]|$(bindir)|g' \
        -e 's|@pkgdatadir[@]|$(pkgdatadir)|g' \
        -e 's|@prefix[@]|$(prefix)|g'
```

```
autoheader autom4te: Makefile
        rm -f $@ $@.tmp
        srcdir=''; \
          test -f ./$@.in || srcdir=$(srcdir)/; \
          $(edit) $${srcdir}$@.in >$@.tmp
        chmod +x $@.tmp
        chmod a-w $@.tmp
        mv $@.tmp $@
```

```
autoheader: $(srcdir)/autoheader.in
autom4te: $(srcdir)/autom4te.in
```

Some details are noteworthy:

**‘@bindir[@]’**

The brackets prevent `configure` from replacing ‘@bindir@’ in the Sed expression itself. Brackets are preferable to a backslash here, since POSIX says ‘\@’ is not portable.

**‘$(bindir)’**

Don’t use ‘@bindir@’! Use the matching makefile variable instead.

**‘$(pkgdatadir)’**

The example takes advantage of the variable ‘$(pkgdatadir)’ provided by Automake; it is equivalent to ‘$(datadir)/$(PACKAGE)’.

**‘/’**

Don’t use ‘/’ in the Sed expressions that replace file names since most likely the variables you use, such as ‘$(bindir)’, contain ‘/’. Use a shell metacharacter instead, such as ‘|’.

**special characters**

File names, file name components, and the value of `VPATH` should not contain shell metacharacters or white space. See Special Characters in Output Variables.

**dependency on Makefile**

Since `edit` uses values that depend on the configuration specific values (`prefix`, etc.) and not only on `VERSION` and so forth, the output depends on Makefile, not configure.ac.

**‘$@’**

The main rule is generic, and uses ‘$@’ extensively to avoid the need for multiple copies of the rule.

**Separated dependencies and single suffix rules**

You can’t use them! The above snippet cannot be (portably) rewritten as:

```
autoconf autoheader: Makefile
```

```
.in:
        rm -f $@ $@.tmp
        $(edit) $< >$@.tmp
        chmod +x $@.tmp
        mv $@.tmp $@
```

See Single Suffix Rules and Separated Dependencies, for details.

**‘$(srcdir)’**

Be sure to specify the name of the source directory, otherwise the package won’t support separated builds.

For the more specific installation of Erlang libraries, the following variables are defined:

**Variable: **ERLANG_INSTALL_LIB_DIR** ¶**

The common parent directory of Erlang library installation directories. This variable is set by calling the `AC_ERLANG_SUBST_INSTALL_LIB_DIR` macro in configure.ac.

**Variable: **ERLANG_INSTALL_LIB_DIR_*library*** ¶**

The installation directory for Erlang library *library*. This variable is set by using the ‘AC_ERLANG_SUBST_INSTALL_LIB_SUBDIR’ macro in configure.ac.

See Erlang Libraries, for details.

#### 4.8.3 Changed Directory Variables

In Autoconf 2.60, the set of directory variables has changed, and the defaults of some variables have been adjusted (see Installation Directory Variables) to changes in the GNU Coding Standards. Notably, datadir, infodir, and mandir are now expressed in terms of datarootdir. If you are upgrading from an earlier Autoconf version, you may need to adjust your files to ensure that the directory variables are substituted correctly (see How Do I `#define` Installation Directories?), and that a definition of datarootdir is in place. For example, in a Makefile.in, adding

```
datarootdir = @datarootdir@
```

is usually sufficient. If you use Automake to create Makefile.in, it will add this for you.

To help with the transition, Autoconf warns about files that seem to use `datarootdir` without defining it. In some cases, it then expands the value of `$datarootdir` in substitutions of the directory variables. The following example shows such a warning:

```
$ cat configure.ac
AC_INIT
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
$ cat Makefile.in
prefix = @prefix@
datadir = @datadir@
$ autoconf
$ configure
configure: creating ./config.status
config.status: creating Makefile
config.status: WARNING:
               Makefile.in seems to ignore the --datarootdir setting
$ cat Makefile
prefix = /usr/local
datadir = ${prefix}/share
```

Usually one can easily change the file to accommodate both older and newer Autoconf releases:

```
$ cat Makefile.in
prefix = @prefix@
datarootdir = @datarootdir@
datadir = @datadir@
$ configure
configure: creating ./config.status
config.status: creating Makefile
$ cat Makefile
prefix = /usr/local
datarootdir = ${prefix}/share
datadir = ${datarootdir}
```

In some cases, however, the checks may not be able to detect that a suitable initialization of `datarootdir` is in place, or they may fail to detect that such an initialization is necessary in the output file. If, after auditing your package, there are still spurious configure warnings about `datarootdir`, you may add the line

```
AC_DEFUN([AC_DATAROOTDIR_CHECKED])
```

to your configure.ac to disable the warnings. This is an exception to the usual rule that you should not define a macro whose name begins with `AC_` (see Macro Names).

#### 4.8.4 Build Directories

You can support compiling a software package for several architectures simultaneously from the same copy of the source code. The object files for each architecture are kept in their own directory.

To support doing this, `make` uses the `VPATH` variable to find the files that are in the source directory. GNU Make can do this. Most other recent `make` programs can do this as well, though they may have difficulties and it is often simpler to recommend GNU `make` (see `VPATH` and Make). Older `make` programs do not support `VPATH`; when using them, the source code must be in the same directory as the object files.

If you are using GNU Automake, the remaining details in this section are already covered for you, based on the contents of your Makefile.am. But if you are using Autoconf in isolation, then supporting `VPATH` requires the following in your Makefile.in:

```
srcdir = @srcdir@
VPATH = @srcdir@
```

Do not set `VPATH` to the value of another variable (see Variables listed in `VPATH`.

`configure` substitutes the correct value for `srcdir` when it produces Makefile.

Do not use the `make` variable `$<`, which expands to the file name of the file in the source directory (found with `VPATH`), except in implicit rules. (An implicit rule is one such as ‘.c.o’, which tells how to create a .o file from a .c file.) Some versions of `make` do not set `$<` in explicit rules; they expand it to an empty value.

Instead, Make command lines should always refer to source files by prefixing them with ‘$(srcdir)/’. It’s safer to quote the source directory name, in case it contains characters that are special to the shell. Because ‘$(srcdir)’ is expanded by Make, single-quoting works and is safer than double-quoting. For example:

```
time.info: time.texinfo
        $(MAKEINFO) '$(srcdir)/time.texinfo'
```

#### 4.8.5 Automatic Remaking

You can put rules like the following in the top-level Makefile.in for a package to automatically update the configuration information when you change the configuration files. This example includes all of the optional files, such as aclocal.m4 and those related to configuration header files. Omit from the Makefile.in rules for any of these files that your package does not use.

The ‘$(srcdir)/’ prefix is included because of limitations in the `VPATH` mechanism.

The stamp- files are necessary because the timestamps of config.h.in and config.h are not changed if remaking them does not change their contents. This feature avoids unnecessary recompilation. You should include the file stamp-h.in in your package’s distribution, so that `make` considers config.h.in up to date. Don’t use `touch` (see Limitations of Usual Tools); instead, use `echo` (using `date` would cause needless output differences).

```
$(srcdir)/configure: configure.ac aclocal.m4
        cd '$(srcdir)' && autoconf

# autoheader might not change config.h.in, so touch a stamp file.
$(srcdir)/config.h.in: stamp-h.in ;
$(srcdir)/stamp-h.in: configure.ac aclocal.m4
        cd '$(srcdir)' && autoheader
        echo timestamp > '$(srcdir)/stamp-h.in'

config.h: stamp-h ;
stamp-h: config.h.in config.status
        ./config.status

Makefile: Makefile.in config.status
        ./config.status

config.status: configure
        ./config.status --recheck
```

(Be careful if you copy these lines directly into your makefile, as you need to convert the indented lines to start with the tab character.)

In addition, you should use

```
AC_CONFIG_FILES([stamp-h], [echo timestamp > stamp-h])
```

so config.status ensures that config.h is considered up to date. See Outputting Files, for more information about `AC_OUTPUT`.

See config.status Invocation, for more examples of handling configuration-related dependencies.

### 4.9 Configuration Header Files

When a package contains more than a few tests that define C preprocessor symbols, the command lines to pass -D options to the compiler can get quite long. This causes two problems. One is that the `make` output is hard to visually scan for errors. More seriously, the command lines can exceed the length limits of some operating systems. As an alternative to passing -D options to the compiler, `configure` scripts can create a C header file containing ‘#define’ directives. The `AC_CONFIG_HEADERS` macro selects this kind of output. Though it can be called anywhere between `AC_INIT` and `AC_OUTPUT`, it is customary to call it right after `AC_INIT`.

The package should ‘#include’ the configuration header file before any other header files, to prevent inconsistencies in declarations (for example, if it redefines `const`, or if it defines a macro like `_FILE_OFFSET_BITS` that affects the behavior of system headers). Note that it is okay to only include config.h from .c files; the project’s .h files can rely on config.h already being included first by the corresponding .c file.

To provide for VPATH builds, remember to pass the C compiler a -I. option (or -I..; whichever directory contains config.h). Even if you use ‘#include "config.h"’, the preprocessor searches only the directory of the currently read file, i.e., the source directory, not the build directory.

With the appropriate -I option, you can use ‘#include <config.h>’. Actually, it’s a good habit to use it, because in the rare case when the source directory contains another config.h, the build directory should be searched first.

**Macro: **AC_CONFIG_HEADERS***(*header* …, [*cmds*], [*init-cmds*])* ¶**

This macro is one of the instantiating macros; see Performing Configuration Actions. Make `AC_OUTPUT` create the file(s) in the blank-or-newline-separated list *header* containing C preprocessor `#define` statements, and replace ‘@DEFS@’ in generated files with -DHAVE_CONFIG_H instead of the value of `DEFS`. The usual name for *header* is config.h; *header* should not contain shell metacharacters. See Special Characters in Output Variables.

If *header* already exists and its contents are identical to what `AC_OUTPUT` would put in it, it is left alone. Doing this allows making some changes in the configuration without needlessly causing object files that depend on the header file to be recompiled.

Usually the input file is named *header*.in; however, you can override the input file name by appending to *header* a colon-separated list of input files. For example, you might need to make the input file name acceptable to DOS variants:

```
AC_CONFIG_HEADERS([config.h:config.hin])
```

**Macro: **AH_HEADER** ¶**

This macro is defined as the name of the first declared config header and undefined if no config headers have been declared up to this point. A third-party macro may, for example, require use of a config header without invoking AC_CONFIG_HEADERS twice, like this:

```
AC_CONFIG_COMMANDS_PRE(
        [m4_ifndef([AH_HEADER], [AC_CONFIG_HEADERS([config.h])])])
```

See Performing Configuration Actions, for more details on *header*.

#### 4.9.1 Configuration Header Templates

Your distribution should contain a template file that looks as you want the final header file to look, including comments, with `#undef` statements which are used as hooks. For example, suppose your configure.ac makes these calls:

```
AC_CONFIG_HEADERS([conf.h])
AC_CHECK_HEADERS([unistd.h])
```

Then you could have code like the following in conf.h.in. The conf.h created by `configure` defines ‘HAVE_UNISTD_H’ to 1, if and only if the system has unistd.h.

```
/* Define as 1 if you have unistd.h.  */
#undef HAVE_UNISTD_H
```

The format of the template file is stricter than what the C preprocessor is required to accept. A directive line should contain only whitespace, ‘#undef’, and ‘HAVE_UNISTD_H’. The use of ‘#define’ instead of ‘#undef’, or of comments on the same line as ‘#undef’, is strongly discouraged. Each hook should only be listed once. Other preprocessor lines, such as ‘#ifdef’ or ‘#include’, are copied verbatim from the template into the generated header.

Since it is a tedious task to keep a template header up to date, you may use `autoheader` to generate it, see Using `autoheader` to Create config.h.in.

During the instantiation of the header, each ‘#undef’ line in the template file for each symbol defined by ‘AC_DEFINE’ is changed to an appropriate ‘#define’. If the corresponding ‘AC_DEFINE’ has not been executed during the `configure` run, the ‘#undef’ line is commented out. (This is important, e.g., for ‘_POSIX_SOURCE’: on many systems, it can be implicitly defined by the compiler, and undefining it in the header would then break compilation of subsequent headers.)

Currently, *all* remaining ‘#undef’ lines in the header template are commented out, whether or not there was a corresponding ‘AC_DEFINE’ for the macro name; but this behavior is not guaranteed for future releases of Autoconf.

Generally speaking, since you should not use ‘#define’, and you cannot guarantee whether a ‘#undef’ directive in the header template will be converted to a ‘#define’ or commented out in the generated header file, the template file cannot be used for conditional definition effects. Consequently, if you need to use the construct

```
#ifdef THIS
# define THAT
#endif
```

you must place it outside of the template. If you absolutely need to hook it to the config header itself, please put the directives to a separate file, and ‘#include’ that file from the config header template. If you are using `autoheader`, you would probably use ‘AH_BOTTOM’ to append the ‘#include’ directive.

#### 4.9.2 Using `autoheader` to Create config.h.in

The `autoheader` program can create a template file of C ‘#define’ statements for `configure` to use. It searches for the first invocation of `AC_CONFIG_HEADERS` in configure sources to determine the name of the template. (If the first call of `AC_CONFIG_HEADERS` specifies more than one input file name, `autoheader` uses the first one.)

It is recommended that only one input file is used. If you want to append a boilerplate code, it is preferable to use ‘AH_BOTTOM([#include <conf_post.h>])’. File conf_post.h is not processed during the configuration then, which make things clearer. Analogically, `AH_TOP` can be used to prepend a boilerplate code.

In order to do its job, `autoheader` needs you to document all of the symbols that you might use. Typically this is done via an `AC_DEFINE` or `AC_DEFINE_UNQUOTED` call whose first argument is a literal symbol and whose third argument describes the symbol (see Defining C Preprocessor Symbols). Alternatively, you can use `AH_TEMPLATE` (see Autoheader Macros), or you can supply a suitable input file for a subsequent configuration header file. Symbols defined by Autoconf’s builtin tests are already documented properly; you need to document only those that you define yourself.

You might wonder why `autoheader` is needed: after all, why would `configure` need to “patch” a config.h.in to produce a config.h instead of just creating config.h from scratch? Well, when everything rocks, the answer is just that we are wasting our time maintaining `autoheader`: generating config.h directly is all that is needed. When things go wrong, however, you’ll be thankful for the existence of `autoheader`.

The fact that the symbols are documented is important in order to *check* that config.h makes sense. The fact that there is a well-defined list of symbols that should be defined (or not) is also important for people who are porting packages to environments where `configure` cannot be run: they just have to *fill in the blanks*.

But let’s come back to the point: the invocation of `autoheader`…

If you give `autoheader` an argument, it uses that file instead of configure.ac and writes the header file to the standard output instead of to config.h.in. If you give `autoheader` an argument of -, it reads the standard input instead of configure.ac and writes the header file to the standard output.

`autoheader` accepts the following options:

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

Remake the template file even if newer than its input files.

**--replace-handwritten**

**-R**

Remake the template file even if it appears not to have been generated by `autoheader`.

**--include=*dir***

**-I *dir***

Append *dir* to the include path. Multiple invocations accumulate.

**--prepend-include=*dir***

**-B *dir***

Prepend *dir* to the include path. Multiple invocations accumulate.

**--warnings=*category*[,*category*...] ¶**

**-W*category*[,*category*...]**

Enable or disable warnings related to each *category*. See m4_warn, for a comprehensive list of categories. Special values include:

**‘all’**

Enable all categories of warnings.

**‘none’**

Disable all categories of warnings.

**‘error’**

Treat all warnings as errors.

**‘no-*category*’**

Disable warnings falling into *category*.

The environment variable `WARNINGS` may also be set to a comma-separated list of warning categories to enable or disable. It is interpreted exactly the same way as the argument of --warnings, but unknown categories are silently ignored. The command line takes precedence; for instance, if `WARNINGS` is set to `obsolete`, but -Wnone is given on the command line, no warnings will be issued.

Some categories of warnings are on by default. Again, for details see m4_warn.

#### 4.9.3 Autoheader Macros

`autoheader` scans configure.ac and figures out which C preprocessor symbols it might define. It knows how to generate templates for symbols defined by `AC_CHECK_HEADERS`, `AC_CHECK_FUNCS` etc., but if you `AC_DEFINE` any additional symbol, you must define a template for it. If there are missing templates, `autoheader` fails with an error message.

The template for a *symbol* is created by `autoheader` from the *description* argument to an `AC_DEFINE`; see Defining C Preprocessor Symbols.

For special needs, you can use the following macros.

**Macro: **AH_TEMPLATE***(*key*, *description*)* ¶**

Tell `autoheader` to generate a template for *key*. This macro generates standard templates just like `AC_DEFINE` when a *description* is given.

For example:

```
AH_TEMPLATE([NULL_DEVICE],
  [Name of the file to open to get
   a null file, or a data sink.])
```

generates the following template, with the description properly justified.

```
/* Name of the file to open to get a null file, or a data sink. */
#undef NULL_DEVICE
```

**Macro: **AH_VERBATIM***(*key*, *template*)* ¶**

Tell `autoheader` to include the *template* as-is in the header template file. This *template* is associated with the *key*, which is used to sort all the different templates and guarantee their uniqueness. It should be a symbol that can be defined via `AC_DEFINE`.

**Macro: **AH_TOP***(*text*)* ¶**

Include *text* at the top of the header template file.

**Macro: **AH_BOTTOM***(*text*)* ¶**

Include *text* at the bottom of the header template file.

Please note that *text* gets included “verbatim” to the template file, not to the resulting config header, so it can easily get mangled when the template is processed. There is rarely a need for something other than

```
AH_BOTTOM([#include <custom.h>])
```

### 4.10 Running Arbitrary Configuration Commands

You can execute arbitrary commands before, during, and after config.status is run. The three following macros accumulate the commands to run when they are called multiple times. `AC_CONFIG_COMMANDS` replaces the obsolete macro `AC_OUTPUT_COMMANDS`; see Obsolete Macros, for details.

**Macro: **AC_CONFIG_COMMANDS***(*tag*…, [*cmds*], [*init-cmds*])* ¶**

Specify additional shell commands to run at the end of config.status, and shell commands to initialize any variables from `configure`. Associate the commands with *tag*. Since typically the *cmds* create a file, *tag* should naturally be the name of that file. If needed, the directory hosting *tag* is created. The *tag* should not contain shell metacharacters. See Special Characters in Output Variables. This macro is one of the instantiating macros; see Performing Configuration Actions.

Here is an unrealistic example:

```
fubar=42
AC_CONFIG_COMMANDS([fubar],
  [AS_ECHO(["this is extra $fubar, and so on."])],
  [fubar=$fubar])
```

Here is a better one:

```
AC_CONFIG_COMMANDS([timestamp], [echo >timestamp])
```

The following two macros look similar, but in fact they are not of the same breed: they are executed directly by configure, so you cannot use config.status to rerun them.

**Macro: **AC_CONFIG_COMMANDS_PRE***(*cmds*)* ¶**

Execute the *cmds* right before creating config.status.

This macro presents the last opportunity to call `AC_SUBST`, `AC_DEFINE`, or `AC_CONFIG_*ITEMS*` macros.

**Macro: **AC_CONFIG_COMMANDS_POST***(*cmds*)* ¶**

Execute the *cmds* right after creating config.status.

### 4.11 Creating Configuration Links

You may find it convenient to create links whose destinations depend upon results of tests. One can use `AC_CONFIG_COMMANDS` but the creation of relative symbolic links can be delicate when the package is built in a directory different from the source directory.

**Macro: **AC_CONFIG_LINKS***(*dest*:*source*…, [*cmds*], [*init-cmds*])* ¶**

Make `AC_OUTPUT` link each of the existing files *source* to the corresponding link name *dest*. Makes a symbolic link if possible, otherwise a hard link if possible, otherwise a copy. The *dest* and *source* names should be relative to the top level source or build directory, and should not contain shell metacharacters. See Special Characters in Output Variables.

This macro is one of the instantiating macros; see Performing Configuration Actions.

For example, this call:

```
AC_CONFIG_LINKS([host.h:config/$machine.h
                object.h:config/$obj_format.h])
```

creates in the current directory host.h as a link to *srcdir*/config/$machine.h, and object.h as a link to *srcdir*/config/$obj_format.h.

The tempting value ‘.’ for *dest* is invalid: it makes it impossible for ‘config.status’ to guess the links to establish.

One can then run:

```
./config.status host.h object.h
```

to create the links.

### 4.12 Configuring Other Packages in Subdirectories

In most situations, calling `AC_OUTPUT` is sufficient to produce makefiles in subdirectories. However, `configure` scripts that control more than one independent package can use `AC_CONFIG_SUBDIRS` to run `configure` scripts for other packages in subdirectories.

**Macro: **AC_CONFIG_SUBDIRS***(*dir* …)* ¶**

Make `AC_OUTPUT` run `configure` in each subdirectory *dir* in the given blank-or-newline-separated list. Each *dir* should be a literal, i.e., please do not use:

```
if test "x$package_foo_enabled" = xyes; then
  my_subdirs="$my_subdirs foo"
fi
AC_CONFIG_SUBDIRS([$my_subdirs])
```

because this prevents ‘./configure --help=recursive’ from displaying the options of the package `foo`. Instead, you should write:

```
AS_IF([test "x$package_foo_enabled" = xyes],
  [AC_CONFIG_SUBDIRS([foo])])
```

If a given *dir* is not found at `configure` run time, a warning is reported; if the subdirectory is optional, write:

```
AS_IF([test -d "$srcdir/foo"],
  [AC_CONFIG_SUBDIRS([foo])])
```

These examples use `AS_IF` instead of ordinary shell `if` to avoid problems that Autoconf has with macro calls in shell conditionals outside macro definitions. See Common Shell Constructs.

If a given *dir* contains `configure.gnu`, it is run instead of `configure`. This is for packages that might use a non-Autoconf script `Configure`, which can’t be called through a wrapper `configure` since it would be the same file on case-insensitive file systems.

The subdirectory `configure` scripts are given the same command line options that were given to this `configure` script, with minor changes if needed, which include:

- adjusting a relative name for the cache file;
- adjusting a relative name for the source directory;
- propagating the current value of `$prefix`, including if it was defaulted, and if the default values of the top level and of the subdirectory configure differ.

This macro also sets the output variable `subdirs` to the list of directories ‘*dir* …’. Make rules can use this variable to determine which subdirectories to recurse into.

This macro may be called multiple times.

### 4.13 Default Prefix

By default, `configure` sets the prefix for files it installs to /usr/local. The user of `configure` can select a different prefix using the --prefix and --exec-prefix options. There are two ways to change the default: when creating `configure`, and when running it.

Some software packages might want to install in a directory other than /usr/local by default. To accomplish that, use the `AC_PREFIX_DEFAULT` macro.

**Macro: **AC_PREFIX_DEFAULT***(*prefix*)* ¶**

Set the default installation prefix to *prefix* instead of /usr/local.

It may be convenient for users to have `configure` guess the installation prefix from the location of a related program that they have already installed. If you wish to do that, you can call `AC_PREFIX_PROGRAM`.

**Macro: **AC_PREFIX_PROGRAM***(*program*)* ¶**

If the user did not specify an installation prefix (using the --prefix option), guess a value for it by looking for *program* in `PATH`, the way the shell does. If *program* is found, set the prefix to the parent of the directory containing *program*, else default the prefix as described above (/usr/local or `AC_PREFIX_DEFAULT`). For example, if *program* is `gcc` and the `PATH` contains /usr/local/gnu/bin/gcc, set the prefix to /usr/local/gnu.

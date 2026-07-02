---
title: "automake (part 7/14)"
source: https://www.gnu.org/software/automake/manual/automake.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 7/14
---

## 10 Other GNU Tools

Since Automake is primarily intended to generate Makefile.ins for use in GNU programs, it tries hard to interoperate with other GNU tools.

### 10.1 Emacs Lisp

Automake provides some support for Emacs Lisp. The `LISP` primary is used to hold a list of .el files. Possible prefixes for this primary are `lisp_` and `noinst_`. Note that if `lisp_LISP` is defined, then configure.ac must run `AM_PATH_LISPDIR` (see Autoconf macros supplied with Automake).

Lisp sources are not distributed by default. You can prefix the `LISP` primary with `dist_`, as in `dist_lisp_LISP` or `dist_noinst_LISP`, to indicate that these files should be distributed.

Automake will byte-compile all Emacs Lisp source files using the Emacs found by `AM_PATH_LISPDIR`, if any was found. When performing such byte-compilation, the flags specified in the (developer-reserved) `AM_ELCFLAGS` and (user-reserved) `ELCFLAGS` make variables will be passed to the Emacs invocation.

Byte-compiled Emacs Lisp files are not portable among all versions of Emacs, so it makes sense to turn this off if you expect sites to have more than one version of Emacs installed. Furthermore, many packages do not actually benefit from byte-compilation. Still, we recommend that you byte-compile your Emacs Lisp sources. It is probably better for sites with strange setups to cope for themselves than to make the installation less nice for everybody else.

There are two ways to avoid byte-compiling. Historically, we have recommended the following construct.

```
lisp_LISP = file1.el file2.el
ELCFILES =
```

`ELCFILES` is an internal Automake variable that normally lists all .elc files that must be byte-compiled. Automake defines `ELCFILES` automatically from `lisp_LISP`. Emptying this variable explicitly prevents byte-compilation.

Since Automake 1.8, we now recommend using `lisp_DATA` instead:

```
lisp_DATA = file1.el file2.el
```

Note that these two constructs are not equivalent. `_LISP` will not install a file if Emacs is not installed, while `_DATA` will always install its files.

### 10.2 Gettext

If `AM_GNU_GETTEXT` is seen in configure.ac, then Automake turns on support for GNU gettext, a message catalog system for internationalization (see Introduction in *GNU gettext utilities*).

The `gettext` support in Automake requires the addition of one or two subdirectories to the package: po and possibly also intl. The latter is needed if `AM_GNU_GETTEXT` is not invoked with the ‘external’ argument, or if `AM_GNU_GETTEXT_INTL_SUBDIR` is used. Automake ensures that these directories exist and are mentioned in `SUBDIRS`.

### 10.3 Libtool

Automake provides support for GNU Libtool (see Introduction in *The Libtool Manual*) with the `LTLIBRARIES` primary. See Building a Shared Library.

### 10.4 Java bytecode compilation (deprecated)

Automake provides some minimal support for Java bytecode compilation with the `JAVA` primary (in addition to the support for compiling Java to native machine code; see Compiling Java sources using gcj). Note however that *the interface and most features described here are deprecated*. Future Automake releases will strive to provide a better and cleaner interface, which however *won’t be backward-compatible*; the present interface will probably be removed altogether some time after the introduction of the new interface (if that ever materializes). In any case, the current `JAVA` primary features are frozen and will no longer be developed, not even to take bug fixes.

Any .java files listed in a `_JAVA` variable will be compiled with `JAVAC` at build time. By default, .java files are not included in the distribution; you should use the `dist_` prefix to distribute them.

Here is a typical setup for distributing .java files and installing the .class files resulting from their compilation.

```
javadir = $(datadir)/java
dist_java_JAVA = a.java b.java ...
```

Currently Automake enforces the restriction that only one `_JAVA` primary can be used in a given Makefile.am. The reason for this restriction is that, in general, it isn’t possible to know which .class files were generated from which .java files, so it would be impossible to know which files to install where. For instance, a .java file can define multiple classes; the resulting .class file names cannot be predicted without parsing the .java file.

There are a few variables that are used when compiling Java sources:

**`JAVAC` ¶**

The name of the Java compiler. This defaults to ‘javac’.

**`JAVACFLAGS` ¶**

The flags to pass to the compiler. This is considered to be a user variable (see Variables reserved for the user).

**`AM_JAVACFLAGS` ¶**

More flags to pass to the Java compiler. This, and not `JAVACFLAGS`, should be used when it is necessary to put Java compiler flags into Makefile.am.

**`JAVAROOT` ¶**

The value of this variable is passed to the -d option to `javac`. It defaults to ‘$(top_builddir)’.

**`CLASSPATH_ENV` ¶**

This variable is a shell expression that is used to set the `CLASSPATH` environment variable on the `javac` command line. (In the future we will probably handle class path setting differently.)

### 10.5 Python

Automake provides support for Python compilation with the `PYTHON` primary. A typical setup is to call `AM_PATH_PYTHON` in configure.ac and use a line like this in Makefile.am:

```
python_PYTHON = tree.py leave.py
```

Python source files are included in the distribution by default; prepend `nodist_` (as in `nodist_python_PYTHON`) to omit them.

At install time, any files listed in a `_PYTHON` variable will be byte-compiled with `py-compile`. `py-compile` creates both standard (.pyc) and optimized (.pyo) byte-compiled versions of the source files. Because byte-compilation occurs at install time, files listed in `noinst_PYTHON` will not be compiled.

Automake ships with an Autoconf macro named `AM_PATH_PYTHON` that determines some Python-related directory variables (see below). If you have called `AM_PATH_PYTHON` from configure.ac, then you may use the variables `python_PYTHON` and `pkgpython_PYTHON` to list Python source files in your Makefile.am, depending on whether you want your files installed in `pythondir` or `pkgpythondir`, respectively.

**Macro: **AM_PATH_PYTHON** *([*version*], [*action-if-found*],* ¶**

[*action-if-not-found*])

Search for a Python interpreter on the system. This macro takes three optional arguments. The first argument, if present, is the minimum version of Python required for this package: `AM_PATH_PYTHON` will skip any Python interpreter that is older than *version*. If an interpreter is found and satisfies *version*, then *action-if-found* is run. Otherwise, *action-if-not-found* is run.

If *action-if-not-found* is not specified, as in the following example, the default is to abort `configure`:

```
AM_PATH_PYTHON([2.5])
```

This is fine when Python is an absolute requirement for the package. If Python ≥ 2.5 was only *optional* for the package, `AM_PATH_PYTHON` could be called as follows.

```
AM_PATH_PYTHON([2.5],, [:])
```

If the `PYTHON` variable is set when `AM_PATH_PYTHON` is called, then that will be the only Python interpreter that is tried.

`AM_PATH_PYTHON` creates the following output variables based on the Python installation found during configuration:

**`PYTHON` ¶**

The name of the Python executable, or ‘:’ if no suitable interpreter could be found.

Assuming *action-if-not-found* is used (otherwise ./configure will abort if Python is absent), the value of `PYTHON` can be used to set up a conditional in order to disable the relevant part of a build as follows.

```
AM_PATH_PYTHON(,, [:])
AM_CONDITIONAL([HAVE_PYTHON], [test "$PYTHON" != :])
```

**`PYTHON_VERSION` ¶**

The Python version number, in the form *major*.*minor* (e.g., ‘2.5’). This is set to be the value of ‘'%u.%u' % sys.version_info[:2]’.

**`PYTHON_PREFIX` ¶**

**`PYTHON_EXEC_PREFIX` ¶**

With no special options given, these have values ‘${prefix}’ and ‘${exec_prefix}’, respectively (unexpanded; see below).

The configure options --with-python_prefix and --with-python_exec_prefix set them to an explicit value.

The configure option --with-python-sys-prefix set them to the values of Python’s ‘sys.prefix’ and ‘sys.exec_prefix’ variables. These often differ from ‘${prefix}’ and ‘${exec_prefix}’, e.g., on platforms such as Mac OS x (where Python is usually installed as a Framework).

**`PYTHON_PLATFORM` ¶**

The canonical name used by Python to describe the operating system, as given by ‘sys.platform’. This value is sometimes needed when building Python extensions.

**`pythondir` ¶**

The subdirectory of the Python install tree in which to install Python scripts. By default this is, on all systems, $PYTHON_PREFIX/lib/python*version*/site-packages, where `$PYTHON_PREFIX` is described above, and *version* is the Python version. (For those knowledgeable about Python installation details: systems generally have their own Python installation scheme, such as `posix_local` on Debian and related (as of Python 3.10), which ends up using a directory named dist-packages; Automake uses the `posix_prefix` scheme and site-packages.)

**`pkgpythondir` ¶**

This is the directory under `pythondir` that is named after the package. That is, it is ‘$(pythondir)/$(PACKAGE)’. It is provided as a convenience.

**`pyexecdir` ¶**

This is the directory where Python extension modules (shared libraries) should be installed. An extension module written in C could be declared as follows to Automake:

```
pyexec_LTLIBRARIES = quaternion.la
quaternion_la_SOURCES = quaternion.c support.c support.h
quaternion_la_LDFLAGS = -avoid-version -module
```

**`pkgpyexecdir` ¶**

This is a convenience variable that is defined as ‘$(pyexecdir)/$(PACKAGE)’.

All of these directory variables have values that can start with either ‘${prefix}’ or ‘${exec_prefix}’, unexpanded. This works fine in Makefiles, but it makes these variables hard to use in configure. This is mandated by the GNU coding standards, so that the user can run ‘make prefix=/foo install’. The Autoconf manual has a section with more details on this topic (see Installation Directory Variables in *The Autoconf Manual*). See also Installing to Hard-Coded Locations.

#### 10.5.1 Supported versions

Automake guarantees releases will support all Python versions that are still supported by the Python project at the time of the Automake release. Support for EOL versions of Python are not guaranteed, but will be considered as long as it is not onerous to do so, and there are large supported distros including them. If you need to support older Python versions, please use a previous Automake release.

Here are the current support plans.

| Version | Status |
|---|---|
| 0.x | Not supported |
| 1.x | Not supported |
| 2.0–2.6 | Untested, but should work |
| 2.7 | Supported (until Apr 2026) |
| 3.0–3.3 | Untested, but should work |
| 3.4 | Supported (until Apr 2022) |
| 3.5 | Supported (until Apr 2024) |
| 3.6 | Supported (until Apr 2028) |
| 3.7 | Supported (until Apr 2028) |
| 3.8 | Supported (until Apr 2030) |
| 3.9 | Supported (until Apr 2030) |
| 3.10 | Supported (until Apr 2030) |


## 11 Building documentation

Currently Automake provides support for Texinfo and man pages.

### 11.1 Texinfo

If the current directory contains Texinfo source, you must declare it with the `TEXINFOS` primary. Generally Texinfo files are converted into info, and thus the `info_TEXINFOS` variable is most commonly used here. Any Texinfo source file should have the .texi extension. Automake also accepts .txi or .texinfo extensions, but their use is discouraged now, and will elicit runtime warnings.

Automake generates rules to build .info, .dvi, .ps, .pdf and .html files from your Texinfo sources. Following the GNU Coding Standards, only the .info files are built by ‘make all’ and installed by ‘make install’ (unless you use no-installinfo, see below). Furthermore, .info files are automatically distributed so that Texinfo is not a prerequisite for installing your package.

It is worth noting that, contrary to what happens with the other formats, the generated .info files are by default placed in `srcdir` rather than in the `builddir`. This can be changed with the info-in-builddir option.

If the Texinfo sources are in a subdirectory relative to the Makefile, then `-I` flags for the subdirectory, both in the source directory and in the build directory, will automatically be added. There is no need to specify these in ‘$(MAKEINFO)’, ‘$(MAKEINFOFLAGS)’, etc.

If a Texinfo source file contains an ‘@setfilename’ directive, and its argument has extension ‘.info’ (or no extension, but this is discouraged), that argument should be the same as the basename of the Texinfo file, extended with ‘.info’. The Make rules generated by Automake assume this, and will not work if the ‘@setfilename’ is for some other name.

If a Texinfo source ‘foo.texi’ is not present, but foo.texi.in exists, Texinfo will read that .texi.in file for `@setfilename` and `@include version.texi` (described below).

Texinfo source files need not be present at all, and if present, need not contain `@setfilename`. Then the file name given in the Makefile.am will be used.

Other documentation formats can be built on request by ‘make dvi’, ‘make ps’, ‘make pdf’ and ‘make html’, and they can be installed with ‘make install-dvi’, ‘make install-ps’, ‘make install-pdf’ and ‘make install-html’ explicitly. ‘make uninstall’ will remove everything: the Texinfo documentation installed by default as well as all the above optional formats.

All of these targets can be extended using ‘-local’ rules (see Extending Automake Rules).

If a .texi file `@include`s version.texi (actually any file named vers...texi, then that file will be automatically generated. The file version.texi defines four Texinfo flags you can reference using `@value{EDITION}`, `@value{VERSION}`, `@value{UPDATED}`, and `@value{UPDATED-MONTH}`.

**`EDITION`**

**`VERSION`**

Both of these flags hold the version number of your program. They are kept separate for historical reasons.

**`UPDATED`**

This holds the date the primary .texi file was last modified.

**`UPDATED-MONTH`**

This holds the name of the month in which the primary .texi file was last modified.

The version.texi support requires the `mdate-sh` script; this script is supplied with Automake and automatically included when `automake` is invoked with the --add-missing option.

If you have multiple Texinfo files, and you want to use the version.texi feature, then you have to have a separate version file for each Texinfo file. Automake will treat any include in a Texinfo file that matches vers*.texi just like an automatically generated version file.

Often an Info file depends on more than one .texi file. For instance, in GNU Hello, hello.texi includes the file fdl.texi. You can tell Automake about these dependencies using the `*texi*_TEXINFOS` variable. Here is how GNU Hello does it:

```
info_TEXINFOS = hello.texi
hello_TEXINFOS = fdl.texi
```

By default, Automake requires the file texinfo.tex to appear in the same directory as the Makefile.am file that lists the .texi files. If you used `AC_CONFIG_AUX_DIR` in configure.ac (see Finding ‘configure’ Input in *The Autoconf Manual*), then texinfo.tex is looked for there. In both cases, `automake` then supplies texinfo.tex if --add-missing is given, and takes care of its distribution. However, if you set the `TEXINFO_TEX` variable (see below), it overrides the location of the file and turns off its installation into the source as well as its distribution.

The option no-texinfo.tex can be used to eliminate the requirement for the file texinfo.tex. Use of the variable `TEXINFO_TEX` is preferable, however, because that allows the `dvi`, `ps`, and `pdf` targets to still work.

Automake generates an `install-info` rule; some people apparently use this. By default, info pages are installed by ‘make install’, so running `make install-info` is pointless. This can be prevented via the `no-installinfo` option. In this case, .info files are not installed by default, and user must request this explicitly using ‘make install-info’.

By default, `make install-info` and `make uninstall-info` will try to run the `install-info` program (if available) to update (or create/remove) the `${infodir}`/dir index. If this is undesired, it can be prevented by exporting the `AM_UPDATE_INFO_DIR` variable to "`no`".

The following variables are used by the Texinfo build rules.

**`MAKEINFO` ¶**

The name of the program invoked to build .info files. This variable is defined by Automake. If the `makeinfo` program is found on the system then it will be used by default; otherwise `missing` will be used instead.

**`MAKEINFOHTML` ¶**

The command invoked to build .html files. Automake defines this to ‘$(MAKEINFO) --html’.

**`MAKEINFOFLAGS` ¶**

User flags passed to each invocation of ‘$(MAKEINFO)’ and ‘$(MAKEINFOHTML)’. This user variable (see Variables reserved for the user) is not expected to be defined in any Makefile; it can be used by users to pass extra flags to suit their needs.

**`AM_MAKEINFOFLAGS` ¶**

**`AM_MAKEINFOHTMLFLAGS` ¶**

**`AM_TEXI2FLAGS` ¶**

Maintainer flags passed to each `makeinfo` invocation. Unlike `MAKEINFOFLAGS`, these variables are meant to be defined by maintainers in Makefile.am. ‘$(AM_MAKEINFOFLAGS)’ is passed to `makeinfo` when building .info files; ‘$(AM_MAKEINFOHTMLFLAGS)’ is used when building .html files; and ‘$(AM_TEXI2FLAGS)’ is used when building .dvi and .pdf files.

For instance, the following setting can be used to obtain one single .html file per manual, without node separators.

```
AM_MAKEINFOHTMLFLAGS = --no-headers --no-split
```

`AM_MAKEINFOHTMLFLAGS` defaults to ‘$(AM_MAKEINFOFLAGS)’. This means that defining `AM_MAKEINFOFLAGS` without defining `AM_MAKEINFOHTMLFLAGS` will impact builds of both .info and .html files.

**`TEXI2DVI` ¶**

The name of the command that converts a .texi file into a .dvi file. This defaults to ‘texi2dvi’, a script that ships with the Texinfo package.

**`TEXI2PDF` ¶**

The name of the command that translates a .texi file into a .pdf file. This defaults to ‘$(TEXI2DVI) --pdf --batch’.

**`DVIPS` ¶**

The name of the command that builds a .ps file out of a .dvi file. This defaults to ‘dvips’.

**`TEXINFO_TEX` ¶**

If your package has Texinfo files in many directories, you can use the variable `TEXINFO_TEX` to tell Automake where to find the canonical texinfo.tex for your package. The value of this variable should be the relative path from the current Makefile.am to texinfo.tex:

```
TEXINFO_TEX = ../doc/texinfo.tex
```

### 11.2 Man Pages

A package can also include man pages (but see the GNU standards on this matter, Man Pages in *The GNU Coding Standards*.) Man pages are declared using the `MANS` primary. Generally the `man_MANS` variable is used. Man pages are automatically installed in the correct subdirectory of `mandir`, based on the file extension.

File extensions such as .1c are handled by looking for the valid part of the extension and using that to determine the correct subdirectory of `mandir`. Valid section names are the digits ‘0’ through ‘9’, and the letters ‘l’ and ‘n’.

Sometimes developers prefer to name a man page something like foo.man in the source, and then rename it to have the correct suffix, for example foo.1, when installing the file. Automake also supports this mode. For a valid section named *section*, there is a corresponding directory named ‘man*section*dir’, and a corresponding `_MANS` variable. Files listed in such a variable are installed in the indicated section. If the file already has a valid suffix, then it is installed as-is; otherwise the file suffix is changed to match the section.

For instance, consider this example:

```
man1_MANS = rename.man thesame.1 alsothesame.1c
```

In this case, rename.man will be renamed to rename.1 when installed, but the other files will keep their names.

By default, man pages are installed by ‘make install’. However, since the GNU project does not require man pages, many maintainers do not expend effort to keep the man pages up to date. In these cases, the no-installman option will prevent the man pages from being installed by default. The user can still explicitly install them via ‘make install-man’.

For fast installation, with many files it is preferable to use ‘man*section*_MANS’ over ‘man_MANS’ as well as files that do not need to be renamed.

Man pages are not currently considered to be source, because it is not uncommon for man pages to be automatically generated. Therefore they are not automatically included in the distribution. However, this can be changed by use of the `dist_` prefix. For instance here is how to distribute and install the two man pages of GNU `cpio` (which includes both Texinfo documentation and man pages):

```
dist_man_MANS = cpio.1 mt.1
```

The `nobase_` prefix is meaningless for man pages and is disallowed.

Executables and manpages may be renamed upon installation (see Renaming Programs at Install Time). For manpages this can be avoided by use of the `notrans_` prefix. For instance, suppose an executable ‘foo’ allowing to access a library function ‘foo’ from the command line. The way to avoid renaming of the foo.3 manpage is:

```
man_MANS = foo.1
notrans_man_MANS = foo.3
```

‘notrans_’ must be specified first when used in conjunction with either ‘dist_’ or ‘nodist_’ (see Fine-grained Distribution Control). For instance:

```
notrans_dist_man3_MANS = bar.3
```


## 12 What Gets Installed

Naturally, Automake handles the details of installing your program once it has been built. All files named by the various primaries are automatically installed in the appropriate places when the user runs ‘make install’.

### 12.1 Basics of Installation

A file named in a primary is installed by copying the built file into the appropriate directory. The base name of the file is used when installing.

```
bin_PROGRAMS = hello subdir/goodbye
```

In this example, both ‘hello’ and ‘goodbye’ will be installed in ‘$(bindir)’.

Sometimes it is useful to avoid the basename step at install time. For instance, you might have a number of header files in subdirectories of the source tree that are laid out precisely how you want to install them. In this situation you can use the `nobase_` prefix to suppress the base name step. For example:

```
nobase_include_HEADERS = stdio.h sys/types.h
```

will install stdio.h in ‘$(includedir)’ and types.h in ‘$(includedir)/sys’.

For most file types, Automake will install multiple files at once, while avoiding command line length issues (see Staying below the command line length limit). Since some `install` programs will not install the same file twice in one invocation, you may need to ensure that file lists are unique within one variable such as ‘nobase_include_HEADERS’ above.

You should not rely on the order in which files listed in one variable are installed. Likewise, to cater for parallel make, you should not rely on any particular file installation order even among different file types (library dependencies are an exception here).

### 12.2 The Two Parts of Install

Automake generates separate `install-data` and `install-exec` rules, in case the installer is installing on multiple machines that share directory structure—these targets allow the machine-independent parts to be installed only once. `install-exec` installs platform-dependent files, and `install-data` installs platform-independent files. The `install` target depends on both of these targets. While Automake tries to automatically segregate objects into the correct category, the Makefile.am author is, in the end, responsible for making sure this is done correctly.

Variables using the standard directory prefixes ‘data’, ‘info’, ‘man’, ‘include’, ‘oldinclude’, ‘pkgdata’, or ‘pkginclude’ are installed by `install-data`.

Variables using the standard directory prefixes ‘bin’, ‘sbin’, ‘libexec’, ‘sysconf’, ‘localstate’, ‘lib’, or ‘pkglib’ are installed by `install-exec`.

For instance, `data_DATA` files are installed by `install-data`, while `bin_PROGRAMS` files are installed by `install-exec`.

Any variable using a user-defined directory prefix with ‘exec’ in the name (e.g., `myexecbin_PROGRAMS`) is installed by `install-exec`. All other user-defined prefixes are installed by `install-data`.

### 12.3 Extending Installation

It is possible to extend this mechanism by defining an `install-exec-local` or `install-data-local` rule. If these rules exist, they will be run at ‘make install’ time. These rules can do almost anything; care is required.

Automake also supports two install hooks, `install-exec-hook` and `install-data-hook`. These hooks are run after all other install rules of the appropriate type, exec or data, have completed. So, for instance, it is possible to perform post-installation modifications using an install hook. See Extending Automake Rules, for some examples.

### 12.4 Staged Installs

Automake generates support for the `DESTDIR` variable in all install rules. `DESTDIR` is used during the ‘make install’ step to relocate install objects into a staging area. Each object and path is prefixed with the value of `DESTDIR` before being copied into the install area. Here is an example of typical DESTDIR usage:

```
mkdir /tmp/staging &&
make DESTDIR=/tmp/staging install
```

The `mkdir` command avoids a security problem if the attacker creates a symbolic link from /tmp/staging to a victim area; then `make` places install objects in a directory tree built under /tmp/staging. If /gnu/bin/foo and /gnu/share/aclocal/foo.m4 are to be installed, the above command would install /tmp/staging/gnu/bin/foo and /tmp/staging/gnu/share/aclocal/foo.m4.

This feature is commonly used to build install images and packages (see Building Binary Packages Using DESTDIR).

Support for `DESTDIR` is implemented by coding it directly into the install rules. If your Makefile.am uses a local install rule (e.g., `install-exec-local`) or an install hook, then you must write that code to respect `DESTDIR`.

See Makefile Conventions in *The GNU Coding Standards*, for another usage example.

### 12.5 Install Rules for the User

Automake also generates rules for targets `uninstall`, `installdirs`, and `install-strip`.

Automake supports `uninstall-local` and `uninstall-hook`. There is no notion of separate uninstalls for “exec” and “data”, as these features would not provide additional functionality.

Note that `uninstall` is not meant as a replacement for a real packaging tool.


## 13 What Gets Cleaned

The GNU Makefile Standards specify a number of different clean rules. See Standard Targets for Users in *The GNU Coding Standards*.

Generally the files that can be cleaned are determined automatically by Automake. Of course, Automake also recognizes some variables that can be defined to specify additional files to clean. These variables are `MOSTLYCLEANFILES`, `CLEANFILES`, `DISTCLEANFILES`, and `MAINTAINERCLEANFILES`.

When cleaning involves more than deleting some hard-coded list of files, it is also possible to supplement the cleaning rules with your own commands. Simply define a rule for any of the `mostlyclean-local`, `clean-local`, `distclean-local`, or `maintainer-clean-local` targets (see Extending Automake Rules). A common case is deleting a directory, for instance, a directory created by the test suite:

```
clean-local:
        -rm -rf testSubDir
```

Since `make` allows only one set of rules for a given target, a more extensible way of writing this is to use a separate target listed as a dependency:

```
clean-local: clean-local-check
.PHONY: clean-local-check
clean-local-check:
        -rm -rf testSubDir
```

As the GNU Standards aren’t always explicit as to which files should be removed by which rule, we’ve adopted a heuristic that we believe was first formulated by François Pinard:

- If `make` built it, and it is commonly something that one would want to rebuild (for instance, a .o file), then `mostlyclean` should delete it.
- Otherwise, if `make` built it, then `clean` should delete it.
- If `configure` built it, then `distclean` should delete it.
- If the maintainer built it (for instance, a .info file), then `maintainer-clean` should delete it. However `maintainer-clean` should not delete anything that needs to exist in order to run ‘./configure && make’.

We recommend that you follow this same set of heuristics in your Makefile.am.

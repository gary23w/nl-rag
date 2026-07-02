---
title: "Libtool (part 3/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 3/8
---

## 5 Integrating libtool with your package

This chapter describes how to integrate libtool with your packages so that your users can install hassle-free shared libraries.

There are several ways that Libtool may be integrated in your package, described in the following sections. Typically, the Libtool macro files as well as ltmain.sh are copied into your package using `libtoolize` and `aclocal` after setting up the configure.ac and toplevel Makefile.am, then `autoconf` adds the needed tests to the configure script. These individual steps are often automated with `autoreconf`.

Here is a diagram showing how such a typical Libtool configuration works when preparing a package for distribution, assuming that m4 has been chosen as the location for additional Autoconf macros, and build-aux as the location for auxiliary build tools (see The Autoconf Manual in *The Autoconf Manual*):

```
libtool.m4 -----.                .--> aclocal.m4 -----.
ltoptions.m4 ---+  .-> aclocal* -+                    +--> autoconf*
ltversion.m4 ---+--+             `--> [copy in m4/] --+       |
ltsugar.m4 -----+  |                    ^             |       \/
lt~obsolete.m4 -+  +-> libtoolize* -----'             |    configure
[ltdl.m4] ------+  |                                  |
                   `----------------------------------'

ltmain.sh -----------> libtoolize* -> [copy in build-aux/]
```

During configuration, the libtool script is generated either through `config.status` or `config.lt`:

```
             .--> config.status* --.
configure* --+                     +--> libtool
             `--> [config.lt*] ----'      ^
                                          |
ltmain.sh --------------------------------'
```

At `make` run time, `libtool` is then invoked as needed as a wrapper around compilers, linkers, install and cleanup programs.

There are alternatives choices to several parts of the setup; for example, the Libtool macro files can either be copied or symlinked into the package, or copied into aclocal.m4. As another example, an external, pre-configured `libtool` script may be used, by-passing most of the tests and package-specific setup for Libtool.

### 5.1 Autoconf macros exported by libtool

Libtool uses a number of macros to interrogate the host system when it is being built, and you can use some of them yourself too. Although there are a great many other macros in the libtool installed m4 files, these do not form part of the published interface, and are subject to change between releases.

Macros in the ‘LT_CMD_’ namespace check for various shell commands:

**Macro: **LT_CMD_MAX_LEN** ¶**

Finds the longest command line that can be safely passed to ‘$SHELL’ without being truncated, and store in the shell variable ‘$max_cmd_len’. It is only an approximate value, but command lines of this length or shorter are guaranteed not to be truncated.

Macros in the ‘LT_FUNC_’ namespace check characteristics of library functions:

**Macro: **LT_FUNC_DLSYM_USCORE** ¶**

‘AC_DEFINE’ the preprocessor symbol ‘DLSYM_USCORE’ if we have to add an underscore to symbol-names passed in to ‘dlsym’.

Macros in the ‘LT_LIB_’ namespace check characteristics of system libraries:

**Macro: **LT_LIB_M** ¶**

Set ‘LIBM’ to the math library or libraries required on this machine, if any.

**Macro: **LT_LIB_DLLOAD** ¶**

This is the macro used by ‘libltdl’ to determine what dlloaders to use on this machine, if any. Several shell variables are set (and ‘AC_SUBST’ed) depending on the dlload interfaces are available on this machine. ‘LT_DLLOADERS’ contains a list of libtool libraries that can be used, and if necessary also sets ‘LIBADD_DLOPEN’ if additional system libraries are required by the ‘dlopen’ loader, and ‘LIBADD_SHL_LOAD’ if additional system libraries are required by the ‘shl_load’ loader, respectively. Finally some symbols are set in config.h depending on the loaders that are found to work: ‘HAVE_LIBDL’, ‘HAVE_SHL_LOAD’, ‘HAVE_DYLD’, ‘HAVE_DLD’.

Macros in the ‘LT_PATH_’ namespace search the system for the full path to particular system commands:

**Macro: **LT_PATH_LD** ¶**

Add a --with-gnu-ld option to configure. Try to find the path to the linker used by ‘$CC’, and whether it is the GNU linker. The result is stored in the shell variable ‘$LD’, which is `AC_SUBST`ed.

**Macro: **LT_PATH_NM** ¶**

Try to find a BSD-compatible `nm` or a MS-compatible `dumpbin` command on this machine. The result is stored in the shell variable ‘$NM’, which is `AC_SUBST`ed.

Macros in the ‘LT_SYS_’ namespace probe for system characteristics:

**Macro: **LT_SYS_DLOPEN_SELF** ¶**

Tests whether a program can dlopen itself, and then also whether the same program can still dlopen itself when statically linked. Results are stored in the shell variables ‘$enable_dlopen_self’ and ‘enable_dlopen_self_static’ respectively.

**Macro: **LT_SYS_DLOPEN_DEPLIBS** ¶**

Define the preprocessor symbol ‘LTDL_DLOPEN_DEPLIBS’ if the OS needs help to load dependent libraries for ‘dlopen’ (or equivalent).

**Macro: **LT_SYS_DLSEARCH_PATH** ¶**

Define the preprocessor symbol ‘LT_DLSEARCH_PATH’ to the system default library search path.

**Macro: **LT_SYS_MODULE_EXT** ¶**

Define the preprocessor symbol ‘LT_MODULE_EXT’ to the extension used for runtime loadable modules. If you use libltdl to open modules, then you can simply use the libtool library extension, .la.

**Macro: **LT_SYS_MODULE_PATH** ¶**

Define the preprocessor symbol ‘LT_MODULE_PATH_VAR’ to the name of the shell environment variable that determines the run-time module search path.

**Macro: **LT_SYS_SYMBOL_USCORE** ¶**

Set the shell variable ‘sys_symbol_underscore’ to ‘no’ unless the compiler prefixes global symbols with an underscore.

### 5.2 Writing Makefile rules for libtool

Libtool is fully integrated with Automake (see Introduction in *The Automake Manual*), starting with Automake version 1.2.

If you want to use libtool in a regular Makefile (or Makefile.in), you are on your own. If you’re not using Automake, and you don’t know how to incorporate libtool into your package you need to do one of the following:

1. Download the latest Automake distribution from your nearest GNU mirror, install it, and start using it.
2. Learn how to write Makefile rules by hand. They’re sometimes complex, but if you’re clever enough to write rules for compiling your old libraries, then you should be able to figure out new rules for libtool libraries (hint: examine the Makefile.in in the tests/testsuite.dir/027 subdirectory, generated from the Autotest labeled ’link against a preloaded static library’ in tests/demo.at, of the libtool distribution; note especially that it was automatically generated from the Makefile.am by Automake).

### 5.3 Using Automake with libtool

Libtool library support is implemented under the ‘LTLIBRARIES’ primary.

Here are some samples from the Automake Makefile.am in the libtool distribution’s tests/demo.at.

First, to link a program against a libtool library, just use the ‘program_LDADD’6 variable:

```
bin_PROGRAMS = hell hell_static

# Build hell from main.c and libhello.la
hell_SOURCES = main.c
hell_LDADD = libhello.la

# Create a statically linked version of hell.
hell_static_SOURCES = main.c
hell_static_LDADD = libhello.la
hell_static_LDFLAGS = -static
```

You may use the ‘program_LDFLAGS’ variable to stuff in any flags you want to pass to libtool while linking program (such as -static to avoid linking uninstalled shared libtool libraries).

Building a libtool library is almost as trivial… note the use of ‘libhello_la_LDFLAGS’ to pass the -version-info (see Library interface versions) option to libtool:

```
# Build a libtool library, libhello.la for installation in libdir.
lib_LTLIBRARIES = libhello.la
libhello_la_SOURCES = hello.c foo.c
libhello_la_LDFLAGS = -version-info 3:12:1
```

The -rpath option is passed automatically by Automake (except for libraries listed as `noinst_LTLIBRARIES`), so you should not specify it.

See The Automake Manual in *The Automake Manual*, for more information.

When building libtool archives which depend on built sources (for example a generated header file), you may find it necessary to manually record these dependencies. Because libtool archives generate object file names manually recording these dependencies is not as straightforward as the examples in Automake’s manual describe. This affects header files in particular, because simply listing them as ‘nodist_libfoo_la_SOURCES’ will not cause Automake to establish a dependent relationship for the object files of libfoo.la. A useful trick (although somewhat imprecise) is to manually record built sources used by a libtool archive as dependencies of all the objects for that library as shown below (as opposed to a particular object file):

```
# Build a libtool library, libhello.la which depends on a generated header.
hello.h:
	echo '#define HELLO_MESSAGE  "Hello, World!"' > $@
BUILT_SOURCES = hello.h
CLEANFILES = hello.h
nodist_libhello_la_SOURCES = hello.h
libhello_la_SOURCES = hello.c foo.h foo.c bar.h bar.c
# Manually record hello.h as a prerequisite for all objects in libhello.la
$(libhello_la_OBJECTS): hello.h
```

See The Automake Manual in *The Automake Manual*, for more information.

### 5.4 Configuring libtool

Libtool requires intimate knowledge of your compiler suite and operating system to be able to create shared libraries and link against them properly. When you install the libtool distribution, a system-specific libtool script is installed into your binary directory.

However, when you distribute libtool with your own packages (see Including libtool in your package), you do not always know the compiler suite and operating system that are used to compile your package.

For this reason, libtool must be *configured* before it can be used. This idea should be familiar to anybody who has used a GNU `configure` script. `configure` runs a number of tests for system features, then generates the Makefiles (and possibly a config.h header file), after which you can run `make` and build the package.

Libtool adds its own tests to your `configure` script to generate a libtool script for the installer’s host machine.

#### 5.4.1 The `LT_INIT` macro

If you are using GNU Autoconf (or Automake), you should add a call to `LT_INIT` to your configure.ac file. This macro adds many new tests to the `configure` script so that the generated libtool script will understand the characteristics of the host. It’s the most important of a number of macros defined by Libtool:

**Macro: **LT_PREREQ** *(*version*)* ¶**

Ensure that a recent enough version of Libtool is being used. If the version of Libtool used for `LT_INIT` is earlier than *version*, print an error message to the standard error output and exit with failure (exit status is 63). For example:

```
LT_PREREQ([2.5.4])
```

**Macro: **LT_INIT** *(*options*)* ¶**

**Macro: **AC_PROG_LIBTOOL** ¶**

**Macro: **AM_PROG_LIBTOOL** ¶**

Add support for the --enable-shared, --disable-shared, --enable-static, --disable-static, --enable-pic, and --disable-pic `configure` flags.7 `AC_PROG_LIBTOOL` and `AM_PROG_LIBTOOL` are deprecated names for older versions of this macro; `autoupdate` will upgrade your configure.ac files.

By default, this macro turns on shared libraries if they are available, and also enables static libraries if they don’t conflict with the shared libraries. You can modify these defaults by passing either `disable-shared` or `disable-static` in the option list to `LT_INIT`, or using `AC_DISABLE_SHARED` or `AC_DISABLE_STATIC`.

```
# Turn off shared libraries during beta-testing, since they
# make the build process take too long.
LT_INIT([disable-shared])
```

The user may specify modified forms of the configure flags --enable-shared and --enable-static to choose whether shared or static libraries are built based on the name of the package. For example, to have shared ‘bfd’ and ‘gdb’ libraries built, but not shared ‘libg++’, you can run all three `configure` scripts as follows:

```
trick$ ./configure --enable-shared=bfd,gdb
```

In general, specifying --enable-shared=*pkgs* is the same as configuring with --enable-shared every package named in the comma-separated *pkgs* list, and every other package with --disable-shared. The --enable-static=*pkgs* flag behaves similarly, but it uses --enable-static and --disable-static. The same applies to the --enable-fast-install=*pkgs* flag, which uses --enable-fast-install and --disable-fast-install.

The package name ‘default’ matches any packages that have not set their name in the `PACKAGE` environment variable.

The --enable-pic and --disable-pic configure flags can be used to specify whether or not `libtool` uses PIC objects. By default, `libtool` uses PIC objects for shared libraries and non-PIC objects for static libraries. The --enable-pic option also accepts a comma-separated list of package names. Specifying --enable-pic=*pkgs* is the same as configuring every package in *pkgs* with --enable-pic and every other package with the default configuration. The package name ‘default’ is treated the same as for --enable-shared and --enable-static.

This macro also sets the shell variable `LIBTOOL_DEPS`, that you can use to automatically update the libtool script if it becomes out-of-date. In order to do that, add to your configure.ac:

```
LT_INIT
AC_SUBST([LIBTOOL_DEPS])
```

and, to Makefile.in or Makefile.am:

```
LIBTOOL_DEPS = @LIBTOOL_DEPS@
libtool: $(LIBTOOL_DEPS)
        $(SHELL) ./config.status libtool
```

If you are using GNU Automake, you can omit the assignment, as Automake will take care of it. You’ll obviously have to create some dependency on libtool.

Aside from `disable-static` and `disable-shared`, there are other options that you can pass to `LT_INIT` to modify its behaviour. Here is a full list:

**‘dlopen’**

Enable checking for dlopen support. This option should be used if the package makes use of the -dlopen and -dlpreopen libtool flags, otherwise libtool will assume that the system does not support dlopening.

**‘win32-dll’**

This option should be used if the package has been ported to build clean dlls on win32 platforms. Usually this means that any library data items are exported with `__declspec(dllexport)` and imported with `__declspec(dllimport)`. If this option is not used, libtool will assume that the package libraries are not dll clean and will build only static libraries on win32 hosts.

Provision must be made to pass -no-undefined to `libtool` in link mode from the package `Makefile`. Naturally, if you pass -no-undefined, you must ensure that all the library symbols **really are** defined at link time!

**‘aix-soname=aix’**

**‘aix-soname=svr4’**

**‘aix-soname=both’**

Enable the --enable-aix-soname to `configure`, which the user can pass to override the given default.

By default (and **always** in releases prior to 2.4.4), Libtool always behaves as if `aix-soname=aix` is given, with no `configure` option for the user to override. Specifically, when the -brtl linker flag is seen in `LDFLAGS` at build-time, static archives are built from static objects only, otherwise, traditional AIX shared library archives of shared objects using in-archive versioning are built (with the `.a` file extension!). Similarly, with -brtl in `LDFLAGS`, libtool shared archives are built from shared objects, without any filename-based versioning; and without -brtl no shared archives are built at all.

When `aix-soname=svr4` option is given, or the --enable-aix-soname=svr4 `configure` option is passed, static archives are always created from static objects, even without -brtl in `LDFLAGS`. Shared archives are made from shared objects, and filename based versioning is enabled.

When `aix-soname=both` option is given, or the --enable-aix-soname=svr4 `configure` option is passed, static archives are built traditionally (as aix-soname=aix), and both kinds of shared archives are built. The `.la` pseudo-archive specifies one or the other depending on whether -brtl is specified in `LDFLAGS` when the library is built.

**‘disable-fast-install’**

Change the default behaviour for `LT_INIT` to disable optimization for fast installation. The user may still override this default, depending on platform support, by specifying --enable-fast-install to `configure`.

**‘shared’**

Change the default behaviour for `LT_INIT` to enable shared libraries. This is the default on all systems where Libtool knows how to create shared libraries. The user may still override this default by specifying --disable-shared to `configure`.

**‘disable-shared’**

Change the default behaviour for `LT_INIT` to disable shared libraries. The user may still override this default by specifying --enable-shared to `configure`.

**‘static’**

Change the default behaviour for `LT_INIT` to enable static libraries. This is the default on all systems where shared libraries have been disabled for some reason, and on most systems where shared libraries have been enabled. If shared libraries are enabled, the user may still override this default by specifying --disable-static to `configure`.

**‘disable-static’**

Change the default behaviour for `LT_INIT` to disable static libraries. The user may still override this default by specifying --enable-static to `configure`.

**‘pic-only’**

Change the default behaviour for `libtool` to try to use only PIC objects. The user may still override this default by specifying --disable-pic to `configure`.

**‘no-pic’**

Change the default behaviour of `libtool` to try to use only non-PIC objects. The user may still override this default by specifying --enable-pic to `configure`.

**Macro: **LT_LANG** *(*language*)* ¶**

Enable `libtool` support for the language given if it has not yet already been enabled. Languages accepted are “C++”, “Fortran 77”, “Java”, “Go”, and “Windows Resource”.

If Autoconf language support macros such as `AC_PROG_CXX` are used in your configure.ac, Libtool language support will automatically be enabled.

Conversely using `LT_LANG` to enable language support for Libtool will automatically enable Autoconf language support as well.

Both of the following examples are therefore valid ways of adding C++ language support to Libtool.

```
LT_INIT
LT_LANG([C++])
```

```
LT_INIT
AC_PROG_CXX
```

**Macro: **AC_LIBTOOL_DLOPEN** ¶**

This macro is deprecated, the ‘dlopen’ option to `LT_INIT` should be used instead.

**Macro: **AC_LIBTOOL_WIN32_DLL** ¶**

This macro is deprecated, the ‘win32-dll’ option to `LT_INIT` should be used instead.

**Macro: **AC_DISABLE_FAST_INSTALL** ¶**

This macro is deprecated, the ‘disable-fast-install’ option to `LT_INIT` should be used instead.

**Macro: **AC_DISABLE_SHARED** ¶**

**Macro: **AM_DISABLE_SHARED** ¶**

Change the default behaviour for `LT_INIT` to disable shared libraries. The user may still override this default by specifying ‘--enable-shared’. The option ‘disable-shared’ to `LT_INIT` is a shorthand for this. `AM_DISABLE_SHARED` is a deprecated alias for `AC_DISABLE_SHARED`.

**Macro: **AC_ENABLE_SHARED** ¶**

**Macro: **AM_ENABLE_SHARED** ¶**

Change the default behaviour for `LT_INIT` to enable shared libraries. This is the default on all systems where Libtool knows how to create shared libraries. The user may still override this default by specifying ‘--disable-shared’. The option ‘shared’ to `LT_INIT` is a shorthand for this. `AM_ENABLE_SHARED` is a deprecated alias for `AC_ENABLE_SHARED`.

**Macro: **AC_DISABLE_STATIC** ¶**

**Macro: **AM_DISABLE_STATIC** ¶**

Change the default behaviour for `LT_INIT` to disable static libraries. The user may still override this default by specifying ‘--enable-static’. The option ‘disable-static’ to `LT_INIT` is a shorthand for this. `AM_DISABLE_STATIC` is a deprecated alias for `AC_DISABLE_STATIC`.

**Macro: **AC_ENABLE_STATIC** ¶**

**Macro: **AM_ENABLE_STATIC** ¶**

Change the default behaviour for `LT_INIT` to enable static libraries. This is the default on all systems where shared libraries have been disabled for some reason, and on most systems where shared libraries have been enabled. If shared libraries are enabled, the user may still override this default by specifying ‘--disable-static’. The option ‘static’ to `LT_INIT` is a shorthand for this. `AM_ENABLE_STATIC` is a deprecated alias for `AC_ENABLE_STATIC`.

The tests in `LT_INIT` also recognize the following environment variables:

**Variable: **CC** ¶**

The C compiler that will be used by the generated `libtool`. If this is not set, `LT_INIT` will look for `gcc` or `cc`.

**Variable: **CFLAGS** ¶**

Compiler flags used to generate standard object files. If this is not set, `LT_INIT` will not use any such flags. It affects only the way `LT_INIT` runs tests, not the produced `libtool`.

**Variable: **CPPFLAGS** ¶**

C preprocessor flags. If this is not set, `LT_INIT` will not use any such flags. It affects only the way `LT_INIT` runs tests, not the produced `libtool`.

**Variable: **LD** ¶**

The system linker to use (if the generated `libtool` requires one). If this is not set, `LT_INIT` will try to find out what is the linker used by `CC`.

**Variable: **LDFLAGS** ¶**

The flags to be used by `libtool` when it links a program. If this is not set, `LT_INIT` will not use any such flags. It affects only the way `LT_INIT` runs tests, not the produced `libtool`.

**Variable: **LIBS** ¶**

The libraries to be used by `LT_INIT` when it links a program. If this is not set, `LT_INIT` will not use any such flags. It affects only the way `LT_INIT` runs tests, not the produced `libtool`.

**Variable: **NM** ¶**

Program to use rather than checking for `nm`.

**Variable: **RANLIB** ¶**

Program to use rather than checking for `ranlib`.

**Variable: **LN_S** ¶**

A command that creates a link of a program, a soft-link if possible, a hard-link otherwise. `LT_INIT` will check for a suitable program if this variable is not set.

**Variable: **DLLTOOL** ¶**

Program to use rather than checking for `dlltool`. Only meaningful for Cygwin/MS-Windows.

**Variable: **OBJDUMP** ¶**

Program to use rather than checking for `objdump`. Only meaningful for Cygwin/MS-Windows.

**Variable: **AS** ¶**

Program to use rather than checking for `as`. Only used on Cygwin/MS-Windows at the moment.

**Variable: **MANIFEST_TOOL** ¶**

Program to use rather than checking for `mt`, the Manifest Tool. Only used on Cygwin/MS-Windows at the moment.

**Variable: **LT_SYS_LIBRARY_PATH** ¶**

Libtool has heuristics for the system search path for runtime-loaded libraries. If the guessed default does not match the setup of the host system, this variable can be used to modify that path list, as follows (`LT_SYS_LIBRARY_PATH` is a colon-delimited list like `PATH`):

- `path:` The heuristically determined paths will be appended after the trailing colon;
- `:path` The heuristically determined paths will be prepended before the leading colon;
- `path::path` The heuristically determined paths will be inserted between the double colons;
- `path` With no dangling colons, the heuristically determined paths will be ignored entirely.

With 1.3 era libtool, if you wanted to know any details of what libtool had discovered about your architecture and environment, you had to run the script with --config and grep through the results. This idiom was supported up to and including 1.5.x era libtool, where it was possible to call the generated libtool script from configure.ac as soon as `LT_INIT` had completed. However, one of the features of libtool 1.4 was that the libtool configuration was migrated out of a separate ltconfig file, and added to the `LT_INIT` macro (nee `AC_PROG_LIBTOOL`), so the results of the configuration tests were available directly to code in configure.ac, rendering the call out to the generated libtool script obsolete.

Starting with libtool 2.0, the multipass generation of the libtool script has been consolidated into a single config.status pass, which happens after all the code in configure.ac has completed. The implication of this is that the libtool script does not exist during execution of code from configure.ac, and so obviously it cannot be called for --config details anymore. If you are upgrading projects that used this idiom to libtool 2.0 or newer, you should replace those calls with direct references to the equivalent Autoconf shell variables that are set by the configure time tests before being passed to config.status for inclusion in the generated libtool script.

**Macro: **LT_OUTPUT** ¶**

By default, the configured libtool script is generated by the call to `AC_OUTPUT` command, and there is rarely any need to use libtool from configure. However, sometimes it is necessary to run configure time compile and link tests using libtool. You can add `LT_OUTPUT` to your configure.ac any time after `LT_INIT` and any `LT_LANG` calls; that done, libtool will be created by a specially generated config.lt file, and available for use in later tests.

Also, when `LT_OUTPUT` is used, for backwards compatibility with Automake regeneration rules, config.status will call config.lt to regenerate libtool, rather than generating the file itself.

When you invoke the `libtoolize` program (see Invoking `libtoolize`), it will tell you where to find a definition of `LT_INIT`. If you use Automake, the `aclocal` program will automatically add `LT_INIT` support to your configure script when it sees the invocation of `LT_INIT` in configure.ac.

Because of these changes, and the runtime version compatibility checks Libtool now executes, we now advise **against** including a copy of libtool.m4 (and brethren) in acinclude.m4. Instead, you should set your project macro directory with `AC_CONFIG_MACRO_DIRS`. When you `libtoolize` your project, a copy of the relevant macro definitions will be placed in your `AC_CONFIG_MACRO_DIRS`, where `aclocal` can reference them directly from aclocal.m4.

#### 5.4.2 Platform-specific configuration notes

While Libtool tries to hide as many platform-specific features as possible, some have to be taken into account when configuring either the Libtool package or a libtoolized package.

- You currently need GNU make to build the Libtool package itself.
- On AIX there are two different styles of shared linking, one where symbols are bound at link-time and one where symbols are bound at runtime only, similar to ELF. In case of doubt use `LDFLAGS=-Wl,-brtl` for the latter style.
- On AIX, native tools are to be preferred over binutils; especially for C++ code, if using the AIX Toolbox GCC 4.0 and binutils, configure with `AR=/usr/bin/ar LD=/usr/bin/ld NM='/usr/bin/nm -B'`.
- On AIX, the `/bin/sh` is very slow due to its inefficient handling of here-documents. A modern shell is preferable: CONFIG_SHELL=/bin/bash; export $CONFIG_SHELL $CONFIG_SHELL ./configure [...]
- For C++ code with templates, it may be necessary to specify the way the compiler will generate the instantiations. For Portland pgCC version5, use `CXX='pgCC --one_instantiation_per_object'` and avoid parallel `make`.
- For C++ code, it may be necessary to specify a library if it is a dependency of a link/compile flag. For example in GNU G++, if you want to use `-fsanitize=address` you need to specify the `-lasan` library, like so: `g++ -o libx.la -fsanitize=address -lasan -rpath [...]`.
- On Darwin, for C++ code with templates you need two level shared libraries. Libtool builds these by default if `MACOSX_DEPLOYMENT_TARGET` is set to 10.3 or later at `configure` time. See rdar://problem/4135857 for more information on this issue.
- The default shell on UNICOS 9, a ksh 88e variant, is too buggy to correctly execute the libtool script. Users are advised to install a modern shell such as GNU bash.
- Some HP-UX `sed` programs are horribly broken, and cannot handle libtool’s requirements, so users may report unusual problems. There is no workaround except to install a working `sed` (such as GNU sed) on these systems.
- The vendor-distributed NCR MP-RAS `cc` programs emits copyright on standard error that confuse tests on size of conftest.err. The workaround is to specify `CC` when run configure with `CC='cc -Hnocopyr'`.
- Any earlier DG/UX system with ELF executables, such as R3.10 or R4.10, is also likely to work, but hasn’t been explicitly tested.
- On Reliant Unix libtool has only been tested with the Siemens C-compiler and an old version of `gcc` provided by Marco Walther.
- libtool.m4, ltdl.m4 and the configure.ac files are marked to use autoconf-mode, which is distributed with GNU Emacs 21, Autoconf itself, and all recent releases of XEmacs.
- When building on some GNU/Linux systems for multilib targets `libtool` sometimes guesses the wrong paths that the linker and dynamic linker search by default. If this occurs for the dynamic library path, you may use the `LT_SYS_LIBRARY_PATH` environment variable to adjust. Otherwise, at `configure` time you may override libtool’s guesses by setting the `autoconf` cache variables `lt_cv_sys_lib_search_path_spec` and `lt_cv_sys_lib_dlsearch_path_spec` respectively.

### 5.5 Including libtool in your package

In order to use libtool, you need to include the following files with your package:

**config.guess ¶**

Attempt to guess a canonical system name.

**config.sub ¶**

Canonical system name validation subroutine script.

**install-sh ¶**

BSD-compatible `install` replacement script.

**ltmain.sh ¶**

A generic script implementing basic libtool functionality.

Note that the libtool script itself should *not* be included with your package. See Configuring libtool.

You should use the `libtoolize` program, rather than manually copying these files into your package.

#### 5.5.1 Invoking `libtoolize`

The `libtoolize` program provides a standard way to add libtool support to your package. In the future, it may implement better usage checking, or other features to make libtool even easier to use.

The `libtoolize` program has the following synopsis:

```
libtoolize [option]...
```

and accepts the following options:

**--copy**

**-c**

Copy files from the libtool data directory rather than creating symlinks.

**--debug**

Dump a trace of shell script execution to standard output. This produces a lot of output, so you may wish to pipe it to `less` (or `more`) or redirect to a file.

**--dry-run**

**-n**

Don’t run any commands that modify the file system, just print them out.

**--force**

**-f**

Replace existing libtool files. By default, `libtoolize` won’t overwrite existing files.

**--help**

Display a help message and exit.

**--ltdl [*target-directory-name*]**

Install libltdl in the *target-directory-name* subdirectory of your package. Normally, the directory is extracted from the argument to `LT_CONFIG_LTDL_DIR` in configure.ac, though you can also specify a subdirectory name here if you are not using Autoconf for example. If `libtoolize` can’t determine the target directory, ‘libltdl’ is used as the default.

**--no-warn**

Normally, Libtoolize tries to diagnose use of deprecated libtool macros and other stylistic issues. If you are deliberately using outdated calling conventions, this option prevents Libtoolize from explaining how to update your project’s Libtool conventions.

**--nonrecursive**

If passed in conjunction with --ltdl, this option will cause the `libltdl` installed by ‘libtoolize’ to be set up for use with a non-recursive `automake` build. To make use of it, you will need to add the following to the Makefile.am of the parent project:

```

## libltdl/ltdl.mk appends to the following variables

## so we set them here before including it:
BUILT_SOURCES   =

AM_CPPFLAGS        =
AM_LDFLAGS         =

include_HEADERS    =
noinst_LTLIBRARIES =
lib_LTLIBRARIES   =
EXTRA_LTLIBRARIES  =

EXTRA_DIST   =

CLEANFILES   =
MOSTLYCLEANFILES   =

include libltdl/ltdl.mk
```

**--quiet**

**-q**

Work silently. ‘libtoolize --quiet’ is used by GNU Automake to add libtool files to your package if necessary.

**--recursive**

If passed in conjunction with --ltdl, this option will cause the `libtoolize` installed ‘libltdl’ to be set up for use with a recursive `automake` build. To make use of it, you will need to adjust the parent project’s configure.ac:

```
AC_CONFIG_FILES([libltdl/Makefile])
```

and Makefile.am:

```
SUBDIRS += libltdl
```

**--subproject**

If passed in conjunction with --ltdl, this option will cause the `libtoolize` installed ‘libltdl’ to be set up for independent configuration and compilation as a self-contained subproject. To make use of it, you should arrange for your build to call `libltdl/configure`, and then run `make` in the libltdl directory (or the subdirectory you put libltdl into). If your project uses Autoconf, you can use the supplied ‘LT_WITH_LTDL’ macro, or else call ‘AC_CONFIG_SUBDIRS’ directly.

Previous releases of ‘libltdl’ built exclusively in this mode, but now it is the default mode both for backwards compatibility and because, for example, it is suitable for use in projects that wish to use ‘libltdl’, but not use the Autotools for their own build process.

**--verbose**

**-v**

Work noisily! Give a blow by blow account of what `libtoolize` is doing.

**--version**

Print `libtoolize` version information and exit.

Sometimes it can be useful to pass options to `libtoolize` even though it is called by another program, such as `autoreconf`. A limited number of options are parsed from the environment variable `LIBTOOLIZE_OPTIONS`: currently --debug, --no-warn, --quiet and --verbose. Multiple options passed in `LIBTOOLIZE_OPTIONS` must be separated with a space, comma or a colon.

By default, a warning is issued for unknown options found in `LIBTOOLIZE_OPTIONS` unless the first such option is --no-warn. Where `libtoolize` has always quit on receipt of an unknown option at the command line, this and all previous releases of `libtoolize` will continue unabated whatever the content of `LIBTOOLIZE_OPTIONS` (modulo some possible warning messages).

```
trick$ LIBTOOLIZE_OPTIONS=--no-warn,--quiet autoreconf --install
```

If `libtoolize` detects an explicit call to `AC_CONFIG_MACRO_DIRS` (see The Autoconf Manual in *The Autoconf Manual*) in your configure.ac, it will put the Libtool macros in the specified directory.

In the future other Autotools will automatically check the contents of `AC_CONFIG_MACRO_DIRS`, but at the moment it is more portable to add the macro directory to `ACLOCAL_AMFLAGS` in Makefile.am, which is where the tools currently look. If `libtoolize` doesn’t see `AC_CONFIG_MACRO_DIRS`, it too will honour the first ‘-I’ argument in `ACLOCAL_AMFLAGS` when choosing a directory to store libtool configuration macros in. It is perfectly sensible to use both `AC_CONFIG_MACRO_DIRS` and `ACLOCAL_AMFLAGS`, as long as they are kept in synchronisation.

```
ACLOCAL_AMFLAGS = -I m4
```

When you bootstrap your project with `aclocal`, then you will need to explicitly pass the same macro directory with `aclocal`’s ‘-I’ flag:

```
trick$ aclocal -I m4
```

If `libtoolize` detects an explicit call to `AC_CONFIG_AUX_DIR` (see The Autoconf Manual in *The Autoconf Manual*) in your configure.ac, it will put the other support files in the specified directory. Otherwise they too end up in the project root directory.

Unless --no-warn is passed, `libtoolize` displays hints for adding libtool support to your package, as well.

#### 5.5.2 Autoconf and `LTLIBOBJS`

People used to add code like the following to their configure.ac:

```
LTLIBOBJS=`echo "$LIBOBJS" | sed 's/\.[^.]* /.lo /g;s/\.[^.]*$/.lo/'`
AC_SUBST([LTLIBOBJS])
```

This is no longer required (since Autoconf 2.54), and doesn’t take Automake’s deansification support into account either, so doesn’t work correctly even with ancient Autoconfs!

Provided you are using a recent (2.54 or better) incarnation of Autoconf, the call to `AC_OUTPUT` takes care of setting `LTLIBOBJS` up correctly, so you can simply delete such snippets from your configure.ac if you had them.

### 5.6 Static-only libraries

When you are developing a package, it is often worthwhile to configure your package with the --disable-shared flag, or to override the defaults for `LT_INIT` by using the `disable-shared` option (see The `LT_INIT` macro). This prevents libtool from building shared libraries, which has several advantages:

- compilation is twice as fast, which can speed up your development cycle,
- debugging is easier because you don’t need to deal with any complexities added by shared libraries, and
- you can see how libtool behaves on static-only platforms.

You may want to put a small note in your package README to let other developers know that --disable-shared can save them time. The following example note is taken from the GIMP8 distribution README:

```
The GIMP uses GNU Libtool to build shared libraries on a
variety of systems.  While this is very nice for making usable
binaries, it can be a pain when trying to debug a program.  For that
reason, compilation of shared libraries can be turned off by
specifying the --disable-shared option to configure.
```


## 6 Using libtool with other languages

Libtool was first implemented to add support for writing shared libraries in the C language. However, over time, libtool is being integrated with other languages, so that programmers are free to reap the benefits of shared libraries in their favorite programming language.

This chapter describes how libtool interacts with other languages, and what special considerations you need to make if you do not use C.

### 6.1 Writing libraries for C`++`

Creating libraries of C++ code should be a fairly straightforward process, because its object files differ from C ones in only three ways:

1. Because of name mangling, C++ libraries are only usable by the C++ compiler that created them. This decision was made by the designers of C++ to protect users from conflicting implementations of features such as constructors, exception handling, and RTTI.
2. On some systems, the C++ compiler must take special actions for the dynamic linker to run dynamic (i.e., run-time) initializers. This means that we should not call `ld` directly to link such libraries, and we should use the C++ compiler instead.
3. C++ compilers will link some Standard C++ library in by default, but libtool does not know what these libraries are, so it cannot even run the inter-library dependence analyzer to check how to link it in. Therefore, running `ld` to link a C++ program or library is deemed to fail.

Because of these three issues, Libtool has been designed to always use the C++ compiler to compile and link C++ programs and libraries. In some instances the `main()` function of a program must also be compiled with the C++ compiler for static C++ objects to be properly initialized.

### 6.2 Tags

Libtool supports multiple languages through the use of tags. Technically a tag corresponds to a set of configuration variables associated with a language. These variables tell `libtool` how it should create objects and libraries for each language.

Tags are defined at `configure`-time for each language activated in the package (see `LT_LANG` in The `LT_INIT` macro). Here is the correspondence between language names and tags names.

| Language name | Tag name |
|---|---|
| C | CC |
| C++ | CXX |
| Java | GCJ |
| Fortran 77 | F77 |
| Fortran | FC |
| Go | GO |
| Windows Resource | RC |

`libtool` tries to automatically infer what tag to use from the compiler command being used to compile or link. If it can’t infer a tag, then it defaults to the configuration for the `C` language.

The tag can also be specified using `libtool`’s --tag=*tag* option (see Invoking `libtool`). It is a good idea to do so in Makefile rules, because that will allow users to substitute the compiler without relying on `libtool` inference heuristics. When no tag is specified, `libtool` will default to `CC`; this tag always exists.

Finally, the set of tags available in a particular project can be retrieved by tracing for the `LT_SUPPORTED_TAG` macro (see Libtool’s trace interface).

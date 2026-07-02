---
title: "Libtool (part 6/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 6/8
---

## 14 Troubleshooting

Libtool is under constant development, changing to remain up-to-date with modern operating systems. If libtool doesn’t work the way you think it should on your platform, you should read this chapter to help determine what the problem is, and how to resolve it.

### 14.1 The libtool test suite

Libtool comes with an integrated set of tests to check that your build is sane, that test its capabilities, and report obvious bugs in the libtool program. The test suite is based on Autotest from Autoconf (see Generating Test Suites with Autotest in *The Autoconf Manual*). These tests, too, are constantly evolving, based on past problems with libtool, and known deficiencies in other operating systems.

As described in the README file, you may run make -k check after you have built libtool (possibly before you install it) to make sure that it meets basic functional requirements.

#### 14.1.1 Description of test suite

The test suite uses keywords to classify certain test groups:

**‘CXX’**

**‘F77’**

**‘FC’**

**‘GCJ’**

The test group exercises one of these `libtool` language tags.

**‘autoconf’**

**‘automake’**

These keywords denote that the respective external program is needed by the test group. The tests are typically skipped if the program is not installed. The ‘automake’ keyword may also denote use of the `aclocal` program.

**‘interactive’**

This test group may require user interaction on some systems. Typically, this means closing a popup window about a DLL load error on Windows.

**‘libltdl’**

Denote that the libltdl library is exercised by the test group.

**‘libtool’**

**‘libtoolize’**

Denote that the `libtool` or `libtoolize` scripts are exercised by the test group, respectively.

**‘recursive’**

Denote that this test group may recursively re-invoke the test suite itself, with changed settings and maybe a changed `libtool` script. You may use the `INNER_TESTSUITEFLAGS` variable to pass additional settings to this recursive invocation. Typically, recursive invocations delimit the set of tests with another keyword, for example by passing `-k libtool` right before the expansion of the `INNER_TESTSUITEFLAGS` variable (without an intervening space, so you get the chance for further delimitation).

Test groups with the keyword ‘recursive’ should not be denoted with keywords, in order to avoid infinite recursion. As a consequence, recursive test groups themselves should never require user interaction, while the test groups they invoke may do so.

There is a convenience target ‘check-noninteractive’ that runs all tests from both test suites that do not cause user interaction on Windows. Conversely, the target ‘check-interactive’ runs the complement of tests and might require closing popup windows about DLL load errors on Windows.

Here is a list of the some of the current files in the test suite, and what they test for:

**tests/am-subdirs.at**

Tests that a binary can be built and ran from outside of the sub-directory that it is built and ran in.

**tests/archive-in-archive.at**

Tests convenience archive within another convenience archive. Compiles `foo()` in libfoo, then compiles libfoo (and `bar()` function) into libbar.

**tests/bindir.at**

Tests include a demonstration of various scenarios related to using the -bindir option with `libtool`, verifying that installed files are correctly linked and executed, and demonstrating flexibility in handling different installation paths and adapting to changing directory structures.

**tests/bug_42313.at**

Tests that there are no conflicting warnings about AC_PROG_RANLIB by verifying no autoscan AC_PROG_RANLIB warning and checking that AC_PROG_RANLIB declaration has a warning.

**tests/bug_62343.at**

Tests that the -no-canonical-prefixes flag is not removed from the linking command, but it is instead passed through to the linker.

**tests/bug_71489.at**

Tests that the local version of an installed program is used both with and without an external library.

**tests/cdemo.at**

Tests include a demonstration of `libtool` convenience libraries, a mechanism that allows build-time static libraries to be created, in a way that their components can be later linked into programs or other libraries, even shared ones.

**tests/cmdline_wrap.at**

Tests include a verification that `libtool` operates properly when the maximum command line length is very small.

**tests/configure-funcs.at**

Tests creation of shell functions shared with `configure` and `libtool`.

**tests/configure-iface.at**

Tests that exercise the configure interface to libltdl.

**tests/convenience.at**

Tests demonstrate `libtool`’s convenience archive capabilities for C, C++, Fortran, and Java languages.

**tests/ctor.at**

Test that `libtool` can handle code with C++ constructors.

**tests/cwrapper.at**

Test cwrapper compliance with standards for uninstalled executables, string length, and installed shared libraries.

**tests/darwin.at**

Tests for macOS X including compilation, concurrent library extraction, `GDB` debug information, `ld` warnings, and verifying .dylib and .so files can be used with `lt_dlopen`.

**tests/demo.at**

Tests include a demonstration of a trivial package that uses `libtool`. The tests include scenarios to build both static and shared libraries, only static libraries, only shared libraries, disabling fast-install mode, building PIC code, and building non-PIC code.

**tests/depdemo.at**

Tests include a demonstration of inter-library dependencies with `libtool`. The test programs link some interdependent libraries under different scenarios.

**tests/deplib-in-subdir.at**

Tests building and linking various libraries within various directories and sub-directories while changing directories as well. It should be possible to use a nontrivial relative path to the output file name when creating libraries and programs. The `deplibs` of these might have relative paths as well. When executing uninstalled programs, the paths relative to $PWD at build time needs to be translated to a path valid at execution time. Also test installing these libraries and programs; however, use consistent relative paths between `libtool` --mode=link and `libtool` --mode=install in this test.

**tests/deplibs-ident.at**

Tests the correct detection and handling of identical dependency libraries when using `libtool`.

**tests/deplibs-mingw.at**

Tests include various scenarios related to detecting deplibs correctly, including cases where there is no `file` command installed as well as the host OS being MinGW.

**tests/destdir.at**

Installs some libs in $DESTDIR, moves them to a different dir, then installs some false libraries in $DESTDIR that should not be linked against. If the program refers to these false libraries, there is a bug.

**tests/dlloader-api.at**

Tests that `lt_dlopen` can open a shared library and call a function from the library, verifies that `lt_dlsym` can find a symbol in the opened library, and make sure that `lt_dlclose` can properly close the library.

**tests/dumpbin-symbols.at**

Tests whether on Windows a convenience symbol in a section of a .lib file is present even if that section is hidden in the .obj file.

**tests/duplicate_conv.at**

Tests two convenience archives with the same name, and also containing an object with the same name.

**tests/duplicate_deps.at**

Tests circular call of dependencies between two libraries, liba and libb. Function `a1()` from liba calls `b1()` from libb and function `b1()` from libb calls `a2()` from liba.

**tests/duplicate_members.at**

Tests a library with multiple files of the same name (from different directories), such as 1/a.c, 2/a.c, 3/a.c, etc.

**tests/early-libtool.at**

Tests building binaries using `libtool` using two configure approaches.

**tests/exceptions.at**

Tests C++ exception handling with `libtool`.

**tests/execute-mode.at**

Tests the --mode=execute feature of `libtool`.

**tests/exeext.at**

Tests ensure that `$EXEEXT` handling works by linking and installing an executable.

**tests/export.at**

Tests symbol exports if shared libraries are enabled.

**tests/export-def.at**

Test exporting from a DLL with module definition (.def files). This test only runs if shared libraries are enabled and building a DLL is supported.

**tests/f77demo.at**

Tests test Fortran 77 support in `libtool` by creating libraries from Fortran 77 sources, and mixed Fortran and C sources, and a Fortran 77 program to use the former library, and a C program to use the latter library.

**tests/fail.at**

Tests to ensure that `libtool` really fails when it should, including after compile failure, program creation failure, and shared library creation failure.

**tests/fcdemo.at**

Tests are similar to the tests/f77demo.at tests, except that Fortran 90 is used in combination with the ‘FC’ interface provided by Autoconf and Automake.

**tests/flags.at**

Tests include checks that compile and linker flags get passed through `libtool`. Tests flags for C, C++, Fortran 77, and Fortran 90.

**tests/help.at**

Tests a variety of mode commands, including mode short-hands, to ensure basic command line functionality. Also verify that the --debug flag is handled correctly in each mode.

**tests/indirect_deps.at**

Tests indirect dependencies (or nested dependencies). libd depends on libconv, which depends on libb, which depends on liba.

**tests/infer-tag.at**

Tests that `func_infer_tag` works by compiling various code snippets in various languages (C, C++, Fortran, Java) without a --tag flag.

**tests/inherited_flags.at**

Tests the functionality of the `inherited_linker_flags` variable in `libtool` library files.

**tests/install.at**

Tests install mode and ensures that `install_override_mode` overrides the mode of the shared library (and only the shared library).

**tests/lalib-syntax.at**

Tests parsing of .la files including both correctly formed .la files and malformed or bogus .la files.

**tests/libtool.at**

Tests basic `libtool` functionality including shell meta-character removal, lack of supplied mode option, file extension handling, simple linking, objectlist flag usage, and `LT_SUPPORTED_TAG` usage.

**tests/libtoolize.at**

Tests that errors and warnings are reported for invalid and unknown `LIBTOOLIZE_OPTIONS` as well as checking the --no-warn flag suppresses `libtoolize` warnings.

**tests/link-order2.at**

Tests to make sure that `depdepls` are added right after the libraries that pull them in which is necessary at least for static linking and on systems where libraries do not link against other libraries.

**tests/link-order.at**

Tests for problems with linking libraries in different order.

**tests/loadlibrary.at**

Tests libltdl (a libdl API for `dlopen`) support of `LoadLibrary` for dynamically linking DLLs in Windows environments.

**tests/localization.at**

Tests to verify that invoking C compiler language localization options do not cause problems with `libtool`.

**tests/lt_dladvise.at**

Tests libltdl (a libdl API for `dlopen`) module loading advisor functions.

**tests/lt_dlexit.at**

Tests libltdl (a libdl API for `dlopen`) for a memory use after free bug in `lt_dlexit`.

**tests/lt_dlopen_a.at**

Tests `lt_dlopen` with an archive file. Verifies that `lt_dlopen` can load an archive file and successfully return a handle to it.

**tests/lt_dlopen.at**

Tests libltdl (a libdl API for `dlopen`) with a basic C example.

**tests/lt_dlopenext.at**

Tests libltdl (a libdl API for `dlopen`) with an extern C++ function.

**tests/ltdl-api.at**

Tests that `libtool` doesn’t mangle gnulib `argv` names.

**tests/ltdl-libdir.at**

Tests if ltdl can find an installed module using the `libdir` variable in the .la file. Tests also include a MinGW test which uses a Windows-style `libdir` name.

**tests/mdemo.at**

Tests include a demonstration of a package that uses `libtool` and the system independent `dlopen` wrapper libltdl to load modules. The library libltdl provides a `dlopen` wrapper for various platforms (POSIX) including support for `dlpreopened` modules (see Dlpreopening).

**tests/need_lib_prefix.at**

Tests to check for failures on systems that require libraries to be prefixed with lib.

**tests/nocase.at**

Tests the `want_nocaseglob` configuration option to search for libraries regardless of case.

**tests/no-executables.at**

Tests `AC_NO_EXECUTABLES` macro with `gcc`.

**tests/nonrecursive.at**

Tests non-recursive DLL libraries with nonrecursive Automake libltdl (a libdl API for `dlopen`) build.

**tests/old-m4-iface.at**

Tests various aspects of `libtool`’s old `m4` interface.

**tests/pic_flag.at**

Tests the -fpic flag with `gcc` and `g++`.

**tests/recursive.at**

Tests recursive DLL libraries with recursive Automake libltdl (a libdl API for `dlopen`) build.

**tests/resident.at**

Tests that resident modules are not unloaded at program exit, as they need to be able to invoke `atexit` handlers. A module being a resident module means it is prevented from being `lt_dlclosed`.

**tests/runpath-in-lalib.at**

Tests the runpath configuration options in `libtool` (-R and -rpath) and that the resulting .la files are installed in the directory appended to their respective library’s `dependency_libs` by -R.

**tests/search-path.at**

Tests `sys_lib_search_path_spec`, which is an expression to get the compile-time system library search path. Tests include determining if it is possible to link an executable to system libraries and if `sys_lib_search_path_spec` also works on MSVC (Microsoft Visual C++).

**tests/shlibpath.at**

Tests include verifying proper behaviour of the `shlibpath_var`, which is the variable responsible for telling the linker where to find shared libraries. Additionally, this tests the behaviour of the `shlibpath_overrides_runpath` variable, which determines if it possible to override an executable’s hardcoded library search path with an environment variable.

**tests/slist.at**

Tests the functionality of the SList datastructure, which is an implementation of singly linked lists. Tests include verifying the usual linked list functions such as finding, removing, deleting, reversing, and sorting the element(s) in SLists.

**tests/standalone.at**

Tests libltdl functionality as a standalone tool. Tests include compiling a symlinked version of libltdl and a copied version of libltdl. Next libltdl is installed locally and linked in a project without the use of Autoconf or Automake.

**tests/static.at**

Tests various flags related to static and dynamic linking including -Bstatic and -Bdynamic.

**tests/stresstest.at**

Tests various `libtool` flag and option combinations, tests linking various types of objects in different sections, and tests regular expressions to cover edge cases and unusual configurations over multiple iterations.

**tests/subproject.at**

Tests the libltdl flag for building subprojects in individual directories. Tests cover soft-linked libltdl trees, copied libltdl trees, and linking libltdl without Autotools.

**tests/sysroot.at**

Tests that `libtool` runs properly in sandboxed sysroot directories.

**tests/tagdemo.at**

Tests include a demonstration of a package that uses `libtool`’s multi-language support through configuration tags. It generates a library from C++ sources, which is then linked to a C++ program.

**tests/template.at**

Tests that `libtool` can handle C++ code utilizing templates.

**tests/testsuite.at**

Main testsuite framework file processed by `autom4te` processes enable running the `libtool` test cases.

**tests/versioning.at**

Tests `libtool`’s versioning system. Tests begin with verifying the behaviour of `libtool` versioning flags -version-info and -version-number. Next, this tests installing a library, then updating the library with a new revision, a compatible update, and an incompatible update. In each case, the tests verify that the original library will link and install as expected.

**tests/with_pic.at**

Tests the function of the --enable-pic flag. The --enable-pic flag is used to specify whether or not `libtool` uses PIC objects. This includes tests for setting --enable-pic to no, yes, or a comma delimited list of package names.

#### 14.1.2 When tests fail

The Autotest-based test suite produces as output a file tests/testsuite.log that contains information about failed tests.

You can pass options to the test suite through the `make` variable `TESTSUITEFLAGS` (see Making testsuite Scripts in *The Autoconf Manual*).

### 14.2 Reporting bugs

If you think you have discovered a bug in libtool, you should think twice: the libtool maintainer is notorious for passing the buck (or maybe that should be “passing the bug”). Libtool was invented to fix known deficiencies in shared library implementations, so, in a way, most of the bugs in libtool are actually bugs in other operating systems. However, the libtool maintainer would definitely be happy to add support for somebody else’s buggy operating system. [I wish there was a good way to do winking smiley-faces in Texinfo.]

Genuine bugs in libtool include problems with shell script portability, documentation errors, and failures in the test suite (see The libtool test suite).

First, check the documentation and help screens to make sure that the behaviour you think is a problem is not already mentioned as a feature.

Then, you should read the Emacs guide to reporting bugs (see Reporting Bugs in *The Emacs Manual*). Some of the details listed there are specific to Emacs, but the principle behind them is a general one.

Finally, send a bug report to the Libtool bug reporting address bug-libtool@gnu.org with any appropriate *facts*, such as test suite output (see When tests fail), all the details needed to reproduce the bug, and a brief description of why you think the behaviour is a bug. Be sure to include the word “libtool” in the subject line, as well as the version number you are using (which can be found by typing libtool --version).

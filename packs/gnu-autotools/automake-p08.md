---
title: "automake (part 8/14)"
source: https://www.gnu.org/software/automake/manual/automake.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 8/14
---

## 14 What Goes in a Distribution

### 14.1 Basics of Distribution

The `dist` rule in the generated Makefile.in can be used to generate a gzipped `tar` file and/or other flavors of archives for distribution. The file is named based on the `PACKAGE` and `VERSION` variables automatically defined by either the `AC_INIT` invocation or by a *deprecated* two-arguments invocation of the `AM_INIT_AUTOMAKE` macro (see Public Macros for how these variables get their values, from either defaults or explicit values—it’s slightly trickier than one would expect). More precisely, the gzipped `tar` file is named ‘${PACKAGE}-${VERSION}.tar.gz’.

You can set the environment (or `Makefile.am`) variable `TAR` to override the tar program used; it defaults to `tar`. See The Types of Distributions, for how to generate other kinds of archives.

With GNU tar, you can also set the environment (or `Makefile.am`) variable `TAR_OPTIONS` to pass options to `tar`. One common case for using this is to avoid having the local user’s uid and gid in the tar file, or the uid being larger than is supported by the tar format. This can be done with, for example:

```
TAR_OPTIONS = --owner=0 --group=0
export TAR_OPTIONS
```

The `export` (a GNU make feature) is necessary to pass the variable in the environment to the `tar` invocation. Another possible fix is to use the `tar-pax` option (see tar-formats), though this reduces portability. (For more discussion, see https://bugs.gnu.org/19615 and https://bugs.gnu.org/73316.)

For the most part, the files to distribute are automatically found by Automake:

- All source files are automatically included in a distribution, as are all Makefile.am and Makefile.in files.
- Files that are read by `configure` are automatically distributed. These are the source files as specified in various Autoconf macros such as `AC_CONFIG_FILES` and siblings.
- Files included in a Makefile.am (using `include`) or in configure.ac (using `m4_include`).
- Automake has a built-in list of commonly used files automatically included in the distribution if they are found in the current directory (either physically, or as the target of a Makefile.am rule). Some common examples: ABOUT-GNU, COPYING, TODO. This list also includes helper scripts installed with ‘automake --add-missing’. Some common examples: compile, config.guess, config.rpath, config.sub, texinfo.tex.
- Automake has another built-in list of files automatically distributed if they are found either with the plain name, or with extension .md (presumably MarkDown, though this not checked). They are checked for in that order, so the plain name is preferred. These are: AUTHORS ChangeLog INSTALL NEWS README README-alpha THANKS.
- A final built-in list of files are those distributed only if other certain conditions hold. For example, the files config.h.top and config.h.bot are automatically distributed only if, e.g., ‘AC_CONFIG_HEADERS([config.h])’ is used in configure.ac). README-alpha is another such file, with README-alpha.md distributed if that is what is available; see Strictness, for its conditions for distribution.

These three lists of files are given in their entirety in the output from `automake --help`.

Despite all this automatic inclusion, it is still common to have files to be distributed which are not found by the automatic rules. You should listed these files in the `EXTRA_DIST` variable. You can mention files in subdirectories in `EXTRA_DIST`.

You can also mention a directory in `EXTRA_DIST`; in this case the entire directory will be recursively copied into the distribution. To emphasize, this copies *everything* in the directory, including temporary editor files, intermediate build files, version control files, etc.; thus we recommend against using this feature as-is. However, you can use the `dist-hook` feature to ameliorate the problem; see The dist Hook.

If you define `SUBDIRS`, Automake will recursively include the subdirectories in the distribution. If `SUBDIRS` is defined conditionally (see Conditionals), Automake will normally include all directories that could possibly appear in `SUBDIRS` in the distribution. If you need to specify the set of directories conditionally, you can set the variable `DIST_SUBDIRS` to the exact list of subdirectories to include in the distribution (see Conditional Subdirectories).

### 14.2 Fine-grained Distribution Control

Sometimes you need tighter control over what does *not* go into the distribution; for instance, you might have source files that are generated and that you do not want to distribute. In this case Automake gives fine-grained control using the `dist` and `nodist` prefixes. Any primary or `_SOURCES` variable can be prefixed with `dist_` to add the listed files to the distribution. Similarly, `nodist_` can be used to omit the files from the distribution.

As an example, here is how you would cause some data to be distributed while leaving some source code out of the distribution:

```
dist_data_DATA = distribute-this
bin_PROGRAMS = foo
nodist_foo_SOURCES = do-not-distribute.c
```

### 14.3 The dist Hook

Occasionally it is useful to be able to change the distribution before it is packaged up. If the `dist-hook` rule exists, it is run after the distribution directory is filled, but before the actual distribution archives are created. One way to use this is for removing unnecessary files that get recursively included by specifying a directory in `EXTRA_DIST`:

```
EXTRA_DIST = doc
dist-hook:
        chmod -R u+w $(distdir)/doc
        rm -rf `find $(distdir)/doc -type d -name RCS`
```

The `dist-hook` recipe should not assume that the regular files in the distribution directory are writable; this might not be the case if one is packaging from a read-only source tree, or when a `make distcheck` is being done. Similarly, the recipe should not assume that the subdirectories put into the distribution directory as a result of being listed in `EXTRA_DIST` are writable. So, if the `dist-hook` recipe wants to modify the content of an existing file (or `EXTRA_DIST` subdirectory) in the distribution directory, it should explicitly to make it writable first:

```
EXTRA_DIST = README doc
dist-hook:
        chmod u+w $(distdir)/README $(distdir)/doc
        echo "Distribution date: `date`" >> $(distdir)/README
        rm -f $(distdir)/doc/HACKING
```

Two variables that come handy when writing `dist-hook` rules are ‘$(distdir)’ and ‘$(top_distdir)’.

‘$(distdir)’ points to the directory where the `dist` rule will copy files from the current directory before creating the tarball. If you are at the top-level directory, then ‘distdir = $(PACKAGE)-$(VERSION)’. When used from subdirectory named foo/, then ‘distdir = ../$(PACKAGE)-$(VERSION)/foo’. ‘$(distdir)’ can be either a relative or absolute path; do not assume a particular form.

‘$(top_distdir)’ always points to the root directory of the distributed tree. At the top level it’s equal to ‘$(distdir)’. In the foo/ subdirectory ‘top_distdir = ../$(PACKAGE)-$(VERSION)’. ‘$(top_distdir)’ can also be either a relative or absolute path.

When packages are nested using `AC_CONFIG_SUBDIRS` (see Nesting Packages), then ‘$(distdir)’ and ‘$(top_distdir)’ are relative to the package where ‘make dist’ was run, not to any sub-packages involved.

### 14.4 Checking the Distribution

Automake also generates a `distcheck` rule that can be of help to ensure that a given distribution will actually work. Simplifying a bit, we can say this rule first makes a distribution, and then, *operating from it*, takes the following steps (in this order):

- does a `VPATH` build (see Parallel Build Trees (a.k.a. VPATH Builds)), with the `srcdir` and all its content made *read-only*;
- makes the printable documentation (with `make dvi`), if any,
- runs the test suite (with `make check`) on this fresh build;
- installs the package in a temporary directory (with `make install`), and runs the test suite on the resulting installation (with `make installcheck`);
- checks that the package can be correctly uninstalled (by `make uninstall`) and cleaned (by `make distclean`);
- finally, makes another tarball to ensure the distribution is self-contained.

All of these actions are performed in a temporary directory. The exact location and the exact structure of such a directory (where the read-only sources are placed, how the temporary build and install directories are named and how deeply they are nested, etc.) is to be considered an implementation detail, which can change at any time, so please do not rely on it.

#### 14.4.1 `DISTCHECK_CONFIGURE_FLAGS`

Building the package involves running ‘./configure’. If you need to supply additional flags to `configure`, define them in the `AM_DISTCHECK_CONFIGURE_FLAGS` variable in your top-level Makefile.am. The user can still extend or override the flags provided there by defining the `DISTCHECK_CONFIGURE_FLAGS` variable, on the command line when invoking `make`. It’s worth noting that `make distcheck` needs complete control over the `configure` options --srcdir and --prefix, so those options cannot be overridden by `AM_DISTCHECK_CONFIGURE_FLAGS` nor by `DISTCHECK_CONFIGURE_FLAGS`.

Developers are encouraged to strive to make their code buildable without requiring any special configure option; thus, in general, you shouldn’t define `AM_DISTCHECK_CONFIGURE_FLAGS`. GNU `m4` offers an example of when its use is justified, however. GNU `m4` configures by default with its experimental and seldom used ‘changeword’ feature disabled; so in this case it is useful to have `make distcheck` run configure with the --with-changeword option, to ensure that the code for changeword support still compiles correctly. GNU `m4` also employs the `AM_DISTCHECK_CONFIGURE_FLAGS` variable to stress-test the use of --program-prefix=g, since at one point the `m4` build system had a bug where `make installcheck` was wrongly assuming it could blindly test ‘m4’, rather than the just-installed ‘gm4’.

#### 14.4.2 `distcheck-hook`

If the `distcheck-hook` rule is defined in your top-level Makefile.am, then it will be invoked by `distcheck` after the new distribution has been unpacked, but before the unpacked copy is configured and built. Your `distcheck-hook` can do almost anything, though as always caution is advised. Generally this hook is used to check for potential distribution errors not caught by the standard mechanism.

`distcheck-hook`, as well as `AM_DISTCHECK_CONFIGURE_FLAGS` and `DISTCHECK_CONFIGURE_FLAGS`, are not honored in a subpackage Makefile.am, but the flags from `AM_DISTCHECK_CONFIGURE_FLAGS` and `DISTCHECK_CONFIGURE_FLAGS` are passed down to the `configure` script of the subpackage.

#### 14.4.3 `dvi` and `distcheck`

Ordinarily, `make distcheck` runs `make dvi`. It does nothing if the distribution contains no Texinfo sources. If the distribution does contain a Texinfo manual, by default the `dvi` target will run TeX to make sure it can be successfully processed (see Texinfo).

However, you may wish to test the manual by producing `pdf` (e.g., if your manual uses images in formats other than `eps`), `html` (if you don’t have TeX at all), some other format, or just skip the test entirely (not recommended). You can change the target that is run by setting the variable `AM_DISTCHECK_DVI_TARGET` in your `Makefile.am`; for example,

```
AM_DISTCHECK_DVI_TARGET = pdf
```

To make `dvi` into a do-nothing target, see the example for `EMPTY_AUTOMAKE_TARGETS` in Third-Party Makefiles.

#### 14.4.4 `distcleancheck`

`distcheck` ensures that the `distclean` rule actually removes all built files. This is done by running ‘make distcleancheck’ at the end of the `VPATH` build. By default, `distcleancheck` will run `distclean` and then make sure the build tree has been emptied by running the value of the variable ‘$(distcleancheck_listfiles)’. Often this check will find generated files that you forgot to add to the `DISTCLEANFILES` variable (see What Gets Cleaned).

The `distcleancheck` behavior should be OK for most packages, otherwise you have the possibility to override the definition of either the `distcleancheck` rule, or the ‘$(distcleancheck_listfiles)’ variable. For instance, to disable `distcleancheck` completely (not recommended), add the following rule to your top-level Makefile.am:

```
distcleancheck:
        @:
```

If you want `distcleancheck` to ignore built files that have not been cleaned because they are also part of the distribution, make the following definition:

```
distcleancheck_listfiles = \
  find . -type f -exec sh -c 'test -f $(srcdir)/$$1 || echo $$1' \
       sh '{}' ';'
```

The above definition is not the default because it’s usually an error if your Makefiles cause some distributed files to be rebuilt when the user builds the package: consider the user missing the tool required to build the file; or if the required tool is built by your package, consider the cross-compilation case where it can’t be run.

Please see the (following) section Errors with `distclean` before playing with `distcleancheck_listfiles`.

#### 14.4.5 `distuninstallcheck`

`distcheck` also checks that the `uninstall` rule works properly, both for ordinary and `DESTDIR` builds. It does this by invoking ‘make uninstall’, and then it checks the install tree to see if any files are left over. This check will make sure that you correctly coded your `uninstall`-related rules.

By default, the checking is done by the `distuninstallcheck` rule, and the list of files in the install tree is generated by ‘$(distuninstallcheck_listfiles)’. The value of the latter variable is taken to be a shell command to run that prints the list of files to stdout.

Either of these can be overridden to modify the behavior of `distcheck`. For instance, to disable this check completely (not recommended), you would write:

```
distuninstallcheck:
        @:
```

#### 14.4.6 Errors with `distclean`

As explained in the section above (see Checking the Distribution), ‘make distcheck’ attempts to build and check your package for errors. One such error you might see is:

```
ERROR: files left in build directory after distclean:
```

The file(s) left in the build directory after ‘make distclean’ has run are listed after this error message. This can happen in two ways:

- files that were forgotten to be distclean-ed;
- distributed files that are erroneously rebuilt.

In the first case of simple left-over files not intended to be distributed, the fix is to include them for cleaning (see What Gets Cleaned); this is straightforward and doesn’t need more explanation.

The second case, however, is not always easy to understand and fix, so let’s proceed with an example. Suppose our package contains a program for which we want to build a man page using `help2man`. GNU `help2man` produces simple manual pages from the --help and --version output of other commands (see *The Help2man Manual*). Because we don’t want to force our users to install `help2man`, we distribute the generated man page using the following setup.

```
# This Makefile.am is bogus.
bin_PROGRAMS = foo
foo_SOURCES = foo.c
dist_man_MANS = foo.1

foo.1: foo$(EXEEXT)
        help2man --output=foo.1 ./foo$(EXEEXT)
```

This will effectively distribute the man page. However, ‘make distcheck’ will fail with:

```
ERROR: files left in build directory after distclean:
./foo.1
```

Why was foo.1 rebuilt? Because although distributed, foo.1 depends on a non-distributed built file: foo$(EXEEXT). foo$(EXEEXT) is built by the user, so it will always appear to be newer than the distributed foo.1.

In other words, ‘make distcheck’ caught an inconsistency in our package. Our intent was to distribute foo.1 so users do not need to install `help2man`, but since this rule causes this file to be always rebuilt, users *do* need `help2man`. Either we should ensure that foo.1 is not rebuilt by users, or there is no point in distributing foo.1.

More generally, the rule is that distributed files should never depend on non-distributed built files. If you distribute something generated, distribute all its sources.

One way to fix the above example, while still distributing foo.1, is to not depend on foo$(EXEEXT), but instead on relevant source files. For instance, assuming `foo --version` and `foo --help` do not change unless foo.c or configure.ac change, we could write the following Makefile.am:

```
bin_PROGRAMS = foo
foo_SOURCES = foo.c
dist_man_MANS = foo.1

foo.1: foo.c $(top_srcdir)/configure.ac
        $(MAKE) $(AM_MAKEFLAGS) foo$(EXEEXT)
        help2man --output=foo.1 ./foo$(EXEEXT)
```

This way, foo.1 will not get rebuilt every time foo$(EXEEXT) changes. The `make` call makes sure foo$(EXEEXT) is up-to-date before `help2man`.

Another step towards ensuring this would be to use separate directories for binaries and man pages, and set `SUBDIRS` so that binaries are built before man pages. Unfortunately, this alone is, in general, not sufficient. In order to avoid to avoid concurrency bugs, it may be necessary to include wrappers; this is done by GNU Autoconf, as mentioned below.

We could also decide not to distribute foo.1. In this case it’s fine to have foo.1 dependent upon foo$(EXEEXT), since both will have to be rebuilt. However, it might be impossible to build the package in a cross-compilation, because building foo.1 involves an *execution* of foo$(EXEEXT). The exception would be if foo is a platform-independent script, such as `help2man`.

Another context where such errors are common is when distributed files are built by tools that are built by the package. The pattern is similar:

```
distributed-file: built-tools distributed-sources
        build-command
```

should be changed to

```
distributed-file: distributed-sources
        $(MAKE) $(AM_MAKEFLAGS) built-tools
        build-command
```

or you could choose not to distribute distributed-file, if cross-compilation does not matter.

The points made through these examples are worth summarizing:

| Distributed files should never depend upon non-distributed built files. Distributed files should be distributed with all their dependencies. If a file is *intended* to be rebuilt by users, then there is no point in distributing it. |
|---|

Real-world examples for `help2man`:

- Autoconf takes the approach described above, including man pages in its releases. A wrapper for each script is needed to avoid concurrency problems. See its source file `autoconf/man/local.mk`, which has a good discussion of the necessary additional details.
- Automake itself takes another approach: it does *not* include man pages in distributions; thus, every user generates them when building from the release tarballs. This is ok (only) because Automake also includes a copy of the `help2man` script, which is plausible because `help2man` is small, self-contained, and platform-independent. See the source file `automake/doc/local.mk`.

If you’re desperate, it’s possible to disable this check completely by setting `distcleancheck_listfiles` (see `distcleancheck`). Make sure you understand the reason why ‘make distcheck’ complains first. `distcleancheck_listfiles` is a way to *hide* errors, not to fix them. You can always do better.

### 14.5 The Types of Distributions

Automake generates rules to provide archives of the project for distributions in various formats. Their targets are:

**`dist-gzip` ¶**

Generate a ‘gzip’ tar archive of the distribution. This is the only format enabled by default. By default, this rule makes `gzip` use a compression option of -9 (more widely supported than --best). To make it use a different one, set the `GZIP_ENV` environment variable. For example, ‘make dist-gzip GZIP_ENV=-7’. `GZIP_ENV` is not used when decompressing.

**`dist-bzip2` ¶**

Generate a ‘bzip2’ tar archive of the distribution. bzip2 archives are usually smaller than gzipped archives. By default, this rule makes ‘bzip2’ use a compression option of -9. To make it use a different one, set the `BZIP2` environment variable.

**`dist-bzip3` ¶**

Generate a ‘bzip3’ tar archive of the distribution. Unlike the other compression programs here, `bzip3` does not read any environment variables.

**`dist-lzip` ¶**

Generate an ‘lzip’ tar archive of the distribution. `lzip` archives are usually smaller than `bzip2`-compressed archives. By default, this rule makes ‘lzip’ use a compression option of -9. To make it use a different one, set the `LZIP_OPT` environment variable.

**`dist-xz` ¶**

Generate an ‘xz’ tar archive of the distribution. `xz` archives are usually smaller than `bzip2`-compressed archives. By default, this rule makes ‘xz’ use a compression option of -e. To make it use a different one, set the `XZ_OPT` environment variable. For example, run this command to use the default compression ratio, but with a progress indicator: ‘make dist-xz XZ_OPT=-ve’.

**`dist-zip` ¶**

Generate a ‘zip’ archive of the distribution.

**`dist-zstd` ¶**

Generate a `zstd` tar archive of the distribution. By default, this rule makes `zstd` use a compression option of -19. To use a different setting, set the `ZSTD_OPT` environment variable. For example, run this command to use the default compression ratio, but with a progress indicator: ‘make dist-zstd ZSTD_OPT=-19v’. However, note that for compatibility with `zstd` itself, you may instead set the `ZSTD_CLEVEL` environment variable, in which case, any `ZSTD_OPT` setting is ignored.

**`dist-shar` ¶**

Generate a ‘shar’ archive of the distribution. This format archive is obsolescent, and use of this option is deprecated. It and the corresponding functionality will be removed altogether in Automake 2.0.

**`dist-tarZ` ¶**

Generate a tar archive of the distribution, compressed with the historical (and obsolescent) program `compress`. This option is deprecated, and it and the corresponding functionality will be removed altogether in Automake 2.0.

The rule `dist` (and its historical synonym `dist-all`) will create archives in all the enabled formats (see List of Automake options for how to change this list). By default, only the `dist-gzip` target is enabled by `dist`.


## 15 Support for test suites

Automake can generate code to handle two kinds of test suites. One is based on integration with the `dejagnu` framework. The other (and most used) form is based on the use of generic test scripts, and its activation is triggered by the definition of the special `TESTS` variable. This second form allows for various degrees of sophistication and customization; in particular, it allows for concurrent execution of test scripts, use of established test protocols such as TAP, and definition of custom test drivers and test runners.

In either case, the testsuite is invoked via ‘make check’.

### 15.1 Generalities about Testing

The purpose of testing is to determine whether a program or system behaves as expected (e.g., known inputs produce the expected outputs, error conditions are correctly handled or reported, and older bugs do not resurface).

The minimal unit of testing is usually called *test case*, or simply *test*. How a test case is defined or delimited, and even what exactly *constitutes* a test case, depends heavily on the testing paradigm and/or framework in use, so we won’t attempt any more precise definition. The set of the test cases for a given program or system constitutes its *testsuite*.

A *test harness* (also *testsuite harness*) is a program or software component that executes all (or part of) the defined test cases, analyzes their outcomes, and reports or registers these outcomes appropriately. Again, the details of how this is accomplished (and how the developer and user can influence it or interface with it) varies wildly, and we’ll attempt no precise definition.

A test is said to *pass* when it can determine that the condition or behavior it means to verify holds, and is said to *fail* when it can determine that such condition of behavior does *not* hold.

Sometimes, tests can rely on non-portable tools or prerequisites, or simply make no sense on a given system (for example, a test checking a Windows-specific feature makes no sense on a GNU/Linux system). In this case, accordingly to the definition above, the tests can neither be considered passed nor failed; instead, they are *skipped*, that is, they are not run, or their result is in any case ignored for what concerns the count of failures and successes. Skips are usually explicitly reported though, so that the user will be aware that not all of the testsuite has been run.

It’s not uncommon, especially during early development stages, that some tests fail for known reasons, and that the developer doesn’t want to tackle these failures immediately (this is especially true when the failing tests deal with corner cases). In this situation, the better policy is to declare that each of those failures is an *expected failure* (or *xfail*). In case a test that is expected to fail ends up passing instead, many testing environments will flag the result as a special kind of failure called *unexpected pass* (or *xpass*).

Many testing environments and frameworks distinguish between test failures and hard errors. As we’ve seen, a test failure happens when some invariant or expected behavior of the software under test is not met. A *hard error* happens when e.g., the set-up of a test case scenario fails, or when some other unexpected or highly undesirable condition is encountered (for example, the program under test experiences a segmentation fault).

### 15.2 Simple Tests

#### 15.2.1 Scripts-based Testsuites

If the special variable `TESTS` is defined, its value is taken to be a list of programs or scripts to run in order to do the testing. Under the appropriate circumstances, it’s possible for `TESTS` to list also data files to be passed to one or more test scripts defined by different means (the so-called “log compilers”, see Parallel Test Harness).

Test scripts can be executed serially or concurrently. Automake supports both these kinds of test execution, with the parallel test harness being the default. The concurrent test harness relies on the concurrence capabilities (if any) offered by the underlying `make` implementation, and can thus only be as good as those are.

By default, only the exit statuses of the test scripts are considered when determining the testsuite outcome. But Automake allows also the use of more complex test protocols, either standard (see Using the TAP test protocol) or custom (see Custom Test Drivers). You can’t enable such protocols when the serial harness is used, though. In the rest of this section we are going to concentrate mostly on protocol-less tests, since we cover test protocols in a later section (again, see Custom Test Drivers).

When no test protocol is in use, an exit status of 0 from a test script will denote a success, an exit status of 77 a skipped test, an exit status of 99 a hard error, and any other exit status will denote a failure.

You may define the variable `XFAIL_TESTS` to a list of tests (usually a subset of `TESTS`) that are expected to fail; this will effectively reverse the result of those tests (with the provision that skips and hard errors remain untouched). You may also instruct the testsuite harness to treat hard errors like simple failures, by defining the `DISABLE_HARD_ERRORS` make variable to a nonempty value.

Note however that, for tests based on more complex test protocols, the exact effects of `XFAIL_TESTS` and `DISABLE_HARD_ERRORS` might change, or they might even have no effect at all (for example, in tests using TAP, there is no way to disable hard errors, and the `DISABLE_HARD_ERRORS` variable has no effect on them).

The result of each test case run by the scripts in `TESTS` will be printed on standard output, along with the test name. For test protocols that allow more test cases per test script (such as TAP), a number, identifier and/or brief description specific for the single test case is expected to be printed in addition to the name of the test script. The possible results (whose meanings should be clear from the previous Generalities about Testing) are `PASS`, `FAIL`, `SKIP`, `XFAIL`, `XPASS` and `ERROR`. Here is an example of output from a hypothetical testsuite that uses both plain and TAP tests:

```
PASS: foo.sh
PASS: zardoz.tap 1 - Daemon started
PASS: zardoz.tap 2 - Daemon responding
SKIP: zardoz.tap 3 - Daemon uses /proc # SKIP /proc is not mounted
PASS: zardoz.tap 4 - Daemon stopped
SKIP: bar.sh
PASS: mu.tap 1
XFAIL: mu.tap 2 # TODO frobnication not yet implemented
```

A testsuite summary (expected to report at least the number of run, skipped and failed tests) will be printed at the end of the testsuite run. By default, the first line of the summary has the form:

```
Testsuite summary for package-string
```

where *package-string* is the name and version of the package. If you have several independent test suites for different parts of the package, though, it can be misleading for each suite to imply it is for the whole package. Or, in complex projects, you may wish to add the current directory or other information to the testsuite header line. So you can override the ‘ for *package-string*’ suffix on that line by setting the `AM_TESTSUITE_SUMMARY_HEADER` variable. The value of this variable is used unquoted in a shell echo command, so you must include any necessary quotes. For example, the default value is

```
AM_TESTSUITE_SUMMARY_HEADER = ' for $(PACKAGE_STRING)'
```

including the double quotes (interpreted by the shell) and the leading space (since the value is output directly after the ‘Testsuite summary’). The `$(PACKAGE_STRING)` is substituted by `make`.

If the standard output is connected to a capable terminal, then the test results and the summary are colored appropriately. The developer and the user can disable colored output by setting the `make` variable ‘AM_COLOR_TESTS=no’; the user can in addition force colored output even without a connecting terminal with ‘AM_COLOR_TESTS=always’. It’s also worth noting that some `make` implementations, when used in parallel mode, have slightly different semantics (see Parallel make in *The Autoconf Manual*), which can break the automatic detection of a connection to a capable terminal. If this is the case, the user will have to resort to the use of ‘AM_COLOR_TESTS=always’ in order to have the testsuite output colorized.

Test programs that need data files should look for them in `srcdir` (which is both a make variable and an environment variable made available to the tests), so that they work when building in a separate directory (see Build Directories in *The Autoconf Manual*), and in particular for the `distcheck` rule (see Checking the Distribution).

Automake ensures that each file listed in `TESTS` is built before it is run; you can list both source and derived programs (or scripts) in `TESTS`; the generated rule will look both in `srcdir` and ‘..’. For instance, you might want to run a C program as a test. To do this you would list its name in `TESTS` and also in `check_PROGRAMS`, and then specify it as you would any other program.

Programs listed in `check_PROGRAMS` (and `check_LIBRARIES`, `check_LTLIBRARIES`, ...) are only built during `make check`, not during `make all`. You should list there any program needed by your tests that does not need to be built by `make all`. The programs in `check_PROGRAMS` are *not* automatically added to `TESTS` because `check_PROGRAMS` usually lists programs used by the tests, not the tests themselves. If all your programs are in fact test cases, you can set `TESTS = $(check_PROGRAMS)`.

#### 15.2.1.1 Testsuite Environment Overrides

The `AM_TESTS_ENVIRONMENT` and `TESTS_ENVIRONMENT` variables can be used to run initialization code and set environment variables for the test scripts. The former variable is developer-reserved, and can be defined in the Makefile.am, while the latter is reserved for the user, which can employ it to extend or override the settings in the former; for this to work portably, however, the contents of a non-empty `AM_TESTS_ENVIRONMENT` *must* be terminated by a semicolon.

The `AM_TESTS_FD_REDIRECT` variable can be used to define file descriptor redirections for the test scripts. One might think that `AM_TESTS_ENVIRONMENT` could be used for this purpose, but experience has shown that doing so portably is practically impossible. The main hurdle is constituted by Korn shells, which usually set the close-on-exec flag on file descriptors opened with the `exec` builtin, thus rendering an idiom like `AM_TESTS_ENVIRONMENT = exec 9>&2;` ineffectual. This issue also affects some Bourne shells, such as the HP-UX’s `/bin/sh`.

```
AM_TESTS_ENVIRONMENT = \

## Some environment initializations are kept in a separate shell

## file 'tests-env.sh', which can make it easier to also run tests

## from the command line.
  . $(srcdir)/tests-env.sh; \

## On Solaris, prefer more POSIX-compliant versions of the standard

## tools by default.
  if test -d /usr/xpg4/bin; then \
    PATH=/usr/xpg4/bin:$$PATH; export PATH; \
  fi;


## With this, the test scripts will be able to print diagnostic

## messages to the original standard error stream, even if the test

## driver redirects the stderr of the test scripts to a log file

## before executing them.
AM_TESTS_FD_REDIRECT = 9>&2
```

As another example, a notice that a test is starting can be emitted using `AM_TESTS_ENVIRONMENT` (for package maintainers) or `TESTS_ENVIRONMENT` by users:

```
make -j12 ... TESTS_ENVIRONMENT='echo RUNNING: "$$f";' check
```

The shell variable `$f` contains the test name. (Although technically this is not guaranteed, in practice it is extremely unlikely to ever change.) This can be helpful to see when trying to debug test failures.

Notwithstanding these benefits, `AM_TESTS_ENVIRONMENT` is, for historical and implementation reasons, *not* supported by the serial harness (see Older (and discouraged) Serial Test Harness).

#### 15.2.2 Older (and discouraged) Serial Test Harness

First, note that today the use of this harness is strongly discouraged in favor of the parallel test harness (see Parallel Test Harness). Still, there are a *few* situations when the advantages offered by the parallel harness are irrelevant, and when test concurrency can even cause tricky problems. In those cases, it might make sense to still use the serial harness, for simplicity and reliability (we still suggest trying to give the parallel harness a shot though).

The serial test harness is enabled by the Automake option serial-tests. It operates by simply running the tests serially, one at the time, without any I/O redirection. It’s up to the user to implement logging of tests’ output, if that’s required or desired.

For historical and implementation reasons, the `AM_TESTS_ENVIRONMENT` variable is *not* supported by this harness (it will be silently ignored if defined); only `TESTS_ENVIRONMENT` is, and it is to be considered a developer-reserved variable. This is done so that, when using the serial harness, `TESTS_ENVIRONMENT` can be defined to an invocation of an interpreter through which the tests are to be run. For instance, the following setup may be used to run tests with Perl:

```
TESTS_ENVIRONMENT = $(PERL) -Mstrict -w
TESTS = foo.pl bar.pl baz.pl
```

It’s important to note that the use of `TESTS_ENVIRONMENT` endorsed here would be *invalid* with the parallel harness. That harness provides a more elegant way to achieve the same effect, with the further benefit of freeing the `TESTS_ENVIRONMENT` variable for the user (see Parallel Test Harness).

Another, less serious limitation of the serial harness is that it doesn’t distinguish between simple failures and hard errors; this is for historical reasons, and might be fixed in future Automake versions.

#### 15.2.3 Parallel Test Harness

By default, Automake generates a parallel (concurrent) test harness. It features automatic collection of the test scripts output in .log files, concurrent execution of tests with `make -j`, specification of inter-test dependencies, lazy reruns of tests that have not completed in a prior run, and hard errors for exceptional failures.

The parallel test harness operates by defining a set of `make` rules that run the test scripts listed in `TESTS`, and, for each such script, save its output in a corresponding .log file and its results (and other “metadata”, see API for Custom Test Drivers) in a corresponding .trs (as in **T**est **R**e**S**ults) file. The .log file will contain all the output emitted by the test on its standard output and its standard error. The .trs file will contain, among the other things, the results of the test cases run by the script.

The parallel test harness will also create a summary log file, `TEST_SUITE_LOG`, which defaults to test-suite.log and requires a .log suffix. This file depends upon all the .log and .trs files created for the test scripts listed in `TESTS`. It contains the output of all tests that failed, encountered a hard error, succeeded unexpectedly, or—unless the variable `IGNORE_SKIPPED_LOGS` is set to a non-empty value—were skipped.

As with the serial harness above, by default one status line is printed per completed test, and a short summary after the suite has completed. However, standard output and standard error of the test are redirected to a per-test log file, so that parallel execution does not produce intermingled output. The output from failed tests is collected in the test-suite.log file. If the variable ‘VERBOSE’ is set, this file is output after the summary.

Each couple of .log and .trs files is created when the corresponding test has completed. The set of log files is listed in the read-only variable `TEST_LOGS`, and defaults to `TESTS`, with the executable extension if any (see Support for executable extensions), as well as any suffix listed in `TEST_EXTENSIONS` removed, and .log appended. Results are undefined if a test file name ends in several concatenated suffixes. `TEST_EXTENSIONS` defaults to .test; it can be overridden by the user, in which case any extension listed in it must be constituted by a dot, followed by a non-digit alphabetic character, followed by any number of alphabetic characters. For example, ‘.sh’, ‘.T’ and ‘.t1’ are valid extensions, while ‘.x-y’, ‘.6c’ and ‘.t.1’ are not.

It is important to note that, due to current limitations (unlikely to be lifted), configure substitutions in the definition of `TESTS` can only work if they will expand to a list of tests that have a suffix listed in `TEST_EXTENSIONS`.

For tests that match an extension `.*ext*` listed in `TEST_EXTENSIONS`, you can provide a custom “test runner” using the variable `*ext*_LOG_COMPILER` (note the upper-case extension) and pass options in `AM_*ext*_LOG_FLAGS` and allow the user to pass options in `*ext*_LOG_FLAGS`. It will cause all tests with this extension to be called with this runner. For all tests without a registered extension, the variables `LOG_COMPILER`, `AM_LOG_FLAGS`, and `LOG_FLAGS` may be used. For example,

```
TESTS = foo.pl bar.py baz
TEST_EXTENSIONS = .pl .py
PL_LOG_COMPILER = $(PERL)
AM_PL_LOG_FLAGS = -w
PY_LOG_COMPILER = $(PYTHON)
AM_PY_LOG_FLAGS = -v
LOG_COMPILER = ./wrapper-script
AM_LOG_FLAGS = -d
```

will invoke ‘$(PERL) -w foo.pl’, ‘$(PYTHON) -v bar.py’, and ‘./wrapper-script -d baz’ to produce foo.log, bar.log, and baz.log, respectively. The foo.trs, bar.trs and baz.trs files will be automatically produced as a side-effect.

It’s important to note that, differently from what we’ve seen for the serial test harness (see Older (and discouraged) Serial Test Harness), the `AM_TESTS_ENVIRONMENT` and `TESTS_ENVIRONMENT` variables *cannot* be used to define a custom test runner; the `LOG_COMPILER` and `LOG_FLAGS` (or their extension-specific counterparts) should be used instead:

```

## This is WRONG!
AM_TESTS_ENVIRONMENT = PERL5LIB='$(srcdir)/lib' $(PERL) -Mstrict -w
```

```

---
title: "Autoconf (part 22/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 22/26
---

## 19 Generating Test Suites with Autotest

```
N.B.: This section describes a feature which is still
stabilizing.  Although we believe that Autotest is useful as-is, this
documentation describes an interface which might change in the future:
do not depend upon Autotest without subscribing to the Autoconf mailing
lists.
```

It is paradoxical that portable projects depend on nonportable tools to run their test suite. Autoconf by itself is the paragon of this problem: although it aims at perfectly portability, up to 2.13 its test suite was using DejaGNU, a rich and complex testing framework, but which is far from being standard on POSIX systems. Worse yet, it was likely to be missing on the most fragile platforms, the very platforms that are most likely to torture Autoconf and exhibit deficiencies.

To circumvent this problem, many package maintainers have developed their own testing framework, based on simple shell scripts whose sole outputs are exit status values describing whether the test succeeded. Most of these tests share common patterns, and this can result in lots of duplicated code and tedious maintenance.

Following exactly the same reasoning that yielded to the inception of Autoconf, Autotest provides a test suite generation framework, based on M4 macros building a portable shell script. The suite itself is equipped with automatic logging and tracing facilities which greatly diminish the interaction with bug reporters, and simple timing reports.

Autoconf itself has been using Autotest for years, and we do attest that it has considerably improved the strength of the test suite and the quality of bug reports. Other projects are known to use some generation of Autotest, such as Bison, GNU Wdiff, GNU Tar, each of them with different needs, and this usage has validated Autotest as a general testing framework.

Nonetheless, compared to DejaGNU, Autotest is inadequate for interactive tool testing, which is probably its main limitation.

### 19.1 Using an Autotest Test Suite

#### 19.1.1 `testsuite` Scripts

Generating testing or validation suites using Autotest is rather easy. The whole validation suite is held in a file to be processed through `autom4te`, itself using GNU M4 under the hood, to produce a stand-alone Bourne shell script which then gets distributed. Neither `autom4te` nor GNU M4 are needed at the installer’s end.

Each test of the validation suite should be part of some test group. A *test group* is a sequence of interwoven tests that ought to be executed together, usually because one test in the group creates data files that a later test in the same group needs to read. Complex test groups make later debugging more tedious. It is much better to keep only a few tests per test group. Ideally there is only one test per test group.

For all but the simplest packages, some file such as testsuite.at does not fully hold all test sources, as these are often easier to maintain in separate files. Each of these separate files holds a single test group, or a sequence of test groups all addressing some common functionality in the package. In such cases, testsuite.at merely initializes the validation suite, and sometimes does elementary health checking, before listing include statements for all other test files. The special file package.m4, containing the identification of the package, is automatically included if found.

A convenient alternative consists in moving all the global issues (local Autotest macros, elementary health checking, and `AT_INIT` invocation) into the file `local.at`, and making testsuite.at be a simple list of `m4_include`s of sub test suites. In such case, generating the whole test suite or pieces of it is only a matter of choosing the `autom4te` command line arguments.

The validation scripts that Autotest produces are by convention called `testsuite`. When run, `testsuite` executes each test group in turn, producing only one summary line per test to say if that particular test succeeded or failed. At end of all tests, summarizing counters get printed. One debugging directory is left for each test group which failed, if any: such directories are named testsuite.dir/*nn*, where *nn* is the sequence number of the test group, and they include:

- a debugging script named run which reruns the test in *debug mode* (see Running `testsuite` Scripts). The automatic generation of debugging scripts has the purpose of easing the chase for bugs.
- all the files created with `AT_DATA`
- all the Erlang source code files created with `AT_CHECK_EUNIT`
- a log of the run, named testsuite.log

In the ideal situation, none of the tests fail, and consequently no debugging directory is left behind for validation.

It often happens in practice that individual tests in the validation suite need to get information coming out of the configuration process. Some of this information, common for all validation suites, is provided through the file atconfig, automatically created by `AC_CONFIG_TESTDIR`. For configuration information which your testing environment specifically needs, you might prepare an optional file named atlocal.in, instantiated by `AC_CONFIG_FILES`. The configuration process produces atconfig and atlocal out of these two input files, and these two produced files are automatically read by the testsuite script.

Here is a diagram showing the relationship between files.

Files used in preparing a software package for distribution:

```
                [package.m4] -->.
                                 \
subfile-1.at ->.  [local.at] ---->+
    ...         \                  \
subfile-i.at ---->-- testsuite.at -->-- autom4te* -->testsuite
    ...         /
subfile-n.at ->'
```

Files used in configuring a software package:

```
                                     .--> atconfig
                                    /
[atlocal.in] -->  config.status* --<
                                    \
                                     `--> [atlocal]
```

Files created during test suite execution:

```
atconfig -->.                    .--> testsuite.log
             \                  /
              >-- testsuite* --<
             /                  \
[atlocal] ->'                    `--> [testsuite.dir]
```

#### 19.1.2 Autotest Logs

When run, the test suite creates a log file named after itself, e.g., a test suite named `testsuite` creates testsuite.log. It contains a lot of information, usually more than maintainers actually need, but therefore most of the time it contains all that is needed:

**command line arguments**

A bad but unfortunately widespread habit consists of setting environment variables before the command, such as in ‘CC=my-home-grown-cc ./testsuite’. The test suite does not know this change, hence (i) it cannot report it to you, and (ii) it cannot preserve the value of `CC` for subsequent runs. Autoconf faced exactly the same problem, and solved it by asking users to pass the variable definitions as command line arguments. Autotest requires this rule, too, but has no means to enforce it; the log then contains a trace of the variables that were changed by the user.

**ChangeLog excerpts**

The topmost lines of all the ChangeLog files found in the source hierarchy. This is especially useful when bugs are reported against development versions of the package, since the version string does not provide sufficient information to know the exact state of the sources the user compiled. Of course, this relies on the use of a ChangeLog.

**build machine**

Running a test suite in a cross-compile environment is not an easy task, since it would mean having the test suite run on a machine *build*, while running programs on a machine *host*. It is much simpler to run both the test suite and the programs on *host*, but then, from the point of view of the test suite, there remains a single environment, *host* = *build*. The log contains relevant information on the state of the *build* machine, including some important environment variables.

**tested programs**

The absolute file name and answers to --version of the tested programs (see Writing testsuite.at, `AT_TESTED`).

**configuration log**

The contents of config.log, as created by `configure`, are appended. It contains the configuration flags and a detailed report on the configuration itself.

### 19.2 Writing testsuite.at

The testsuite.at is a Bourne shell script making use of special Autotest M4 macros. It often contains a call to `AT_INIT` near its beginning followed by one call to `m4_include` per source file for tests. Each such included file, or the remainder of testsuite.at if include files are not used, contain a sequence of test groups. Each test group begins with a call to `AT_SETUP`, then an arbitrary number of shell commands or calls to `AT_CHECK`, and then completes with a call to `AT_CLEANUP`. Multiple test groups can be categorized by a call to `AT_BANNER`.

All of the public Autotest macros have all-uppercase names in the namespace ‘^AT_’ to prevent them from accidentally conflicting with other text; Autoconf also reserves the namespace ‘^_AT_’ for internal macros. All shell variables used in the testsuite for internal purposes have mostly-lowercase names starting with ‘at_’. Autotest also uses here-document delimiters in the namespace ‘^_AT[A-Z]’, and makes use of the file system namespace ‘^at-’.

Since Autoconf is built on top of M4sugar (see Programming in M4sugar) and M4sh (see Programming in M4sh), you must also be aware of those namespaces (‘^_?\(m4\|AS\)_’). In general, you *should not use* the namespace of a package that does not own the macro or shell code you are writing.

**Macro: **AT_INIT***([*name*])* ¶**

Initialize Autotest. Giving a *name* to the test suite is encouraged if your package includes several test suites. Before this macro is called, `AT_PACKAGE_STRING` and `AT_PACKAGE_BUGREPORT` must be defined, which are used to display information about the testsuite to the user. Typically, these macros are provided by a file package.m4 built by `make` (see Making `testsuite` Scripts), in order to inherit the package name, version, and bug reporting address from configure.ac.

**Macro: **AT_COPYRIGHT***(*copyright-notice*)* ¶**

State that, in addition to the Free Software Foundation’s copyright on the Autotest macros, parts of your test suite are covered by *copyright-notice*.

The *copyright-notice* shows up in both the head of `testsuite` and in ‘testsuite --version’.

**Macro: **AT_ARG_OPTION***(*options*, *help-text*, [*action-if-given*], [*action-if-not-given*])* ¶**

Accept options from the space-separated list *options*, a list that has leading dashes removed from the options. Long options will be prefixed with ‘--’, single-character options with ‘-’. The first word in this list is the primary *option*, any others are assumed to be short-hand aliases. The variable associated with it is `at_arg_*option*`, with any dashes in *option* replaced with underscores.

If the user passes --*option* to the `testsuite`, the variable will be set to ‘:’. If the user does not pass the option, or passes --no-*option*, then the variable will be set to ‘false’.

*action-if-given* is run each time the option is encountered; here, the variable `at_optarg` will be set to ‘:’ or ‘false’ as appropriate. `at_optarg` is actually just a copy of `at_arg_*option*`.

*action-if-not-given* will be run once after option parsing is complete and if no option from *options* was used.

*help-text* is added to the end of the list of options shown in `testsuite --help` (see AS_HELP_STRING).

It is recommended that you use a package-specific prefix to *options* names in order to avoid clashes with future Autotest built-in options.

**Macro: **AT_ARG_OPTION_ARG***(*options*, *help-text*, [*action-if-given*], [*action-if-not-given*])* ¶**

Accept options with arguments from the space-separated list *options*, a list that has leading dashes removed from the options. Long options will be prefixed with ‘--’, single-character options with ‘-’. The first word in this list is the primary *option*, any others are assumed to be short-hand aliases. The variable associated with it is `at_arg_*option*`, with any dashes in *option* replaced with underscores.

If the user passes --*option*=*arg* or --*option* *arg* to the `testsuite`, the variable will be set to ‘*arg*’.

*action-if-given* is run each time the option is encountered; here, the variable `at_optarg` will be set to ‘*arg*’. `at_optarg` is actually just a copy of `at_arg_*option*`.

*action-if-not-given* will be run once after option parsing is complete and if no option from *options* was used.

*help-text* is added to the end of the list of options shown in `testsuite --help` (see AS_HELP_STRING).

It is recommended that you use a package-specific prefix to *options* names in order to avoid clashes with future Autotest built-in options.

**Macro: **AT_COLOR_TESTS** ¶**

Enable colored test results by default when the output is connected to a terminal.

**Macro: **AT_TESTED***(*executables*)* ¶**

Log the file name and answer to --version of each program in space-separated list *executables*. Several invocations register new executables, in other words, don’t fear registering one program several times.

Autotest test suites rely on `PATH` to find the tested program. This avoids the need to generate absolute names of the various tools, and makes it possible to test installed programs. Therefore, knowing which programs are being exercised is crucial to understanding problems in the test suite itself, or its occasional misuses. It is a good idea to also subscribe foreign programs you depend upon, to avoid incompatible diagnostics.

*executables* is implicitly wrapped in shell double quotes, but it will still use shell variable expansion (‘$’), command substitution (‘`’), and backslash escaping (‘\’). In particular, the `EXEEXT` variable is available if it is passed to the testsuite via atlocal or atconfig.

**Macro: **AT_PREPARE_TESTS***(*shell-code*)* ¶**

Execute *shell-code* in the main testsuite process, after initializing the test suite and processing command-line options, but before running any tests. If this macro is used several times, all of the *shell-code*s will be executed, in the order they appeared in testsuite.at.

One reason to use `AT_PREPARE_TESTS` is when the programs under test are sensitive to environment variables: you can unset all these variables or reset them to safe values in *shell-code*.

*shell-code* is only executed if at least one test is going to be run. In particular, it will not be executed if any of the --help, --version, --list, or --clean options are given to `testsuite` (see Running `testsuite` Scripts).

**Macro: **AT_PREPARE_EACH_TEST***(*shell-code*)* ¶**

Execute *shell-code* in each test group’s subshell, at the point of the `AT_SETUP` that starts the test group.

**Macro: **AT_TEST_HELPER_FN***(*name*, *args*, *description*, *code*)* ¶**

Define a shell function that will be available to the code for each test group. Its name will be `ath_fn_*name*`, and its body will be *code*. (The prefix prevents name conflicts with shell functions defined by M4sh and Autotest.)

*args* should describe the function’s arguments and *description* what it does; these are used only for documentation comments in the generated testsuite script.

**Macro: **AT_BANNER***(*test-category-name*)* ¶**

This macro identifies the start of a category of related test groups. When the resulting testsuite is invoked with more than one test group to run, its output will include a banner containing *test-category-name* prior to any tests run from that category. The banner should be no more than about 40 or 50 characters. A blank banner indicates uncategorized tests; an empty line will be inserted after tests from an earlier category, effectively ending that category.

**Macro: **AT_SETUP***(*test-group-name*)* ¶**

This macro starts a group of related tests, all to be executed in the same subshell. It accepts a single argument, which holds a few words (no more than about 30 or 40 characters) quickly describing the purpose of the test group being started. *test-group-name* must not expand to unbalanced quotes, although quadrigraphs can be used.

**Macro: **AT_KEYWORDS***(*keywords*)* ¶**

Associate the space-separated list of *keywords* to the enclosing test group. This makes it possible to run “slices” of the test suite. For instance, if some of your test groups exercise some ‘foo’ feature, then using ‘AT_KEYWORDS(foo)’ lets you run ‘./testsuite -k foo’ to run exclusively these test groups. The *test-group-name* of the test group is automatically recorded to `AT_KEYWORDS`.

Several invocations within a test group accumulate new keywords. In other words, don’t fear registering the same keyword several times in a test group.

**Macro: **AT_CAPTURE_FILE***(*file*)* ¶**

If the current test group fails, log the contents of *file*. Several identical calls within one test group have no additional effect.

**Macro: **AT_FAIL_IF***(*shell-condition*)* ¶**

Make the test group fail and skip the rest of its execution, if *shell-condition* is true. *shell-condition* is a shell expression such as a `test` command. Tests before `AT_FAIL_IF` will be executed and may still cause the test group to be skipped. You can instantiate this macro many times from within the same test group.

You should use this macro only for very simple failure conditions. If the *shell-condition* could emit any kind of output you should instead use `AT_CHECK` like

```
AT_CHECK([if shell-condition; then exit 99; fi])
```

so that such output is properly recorded in the testsuite.log file.

**Macro: **AT_SKIP_IF***(*shell-condition*)* ¶**

Determine whether the test should be skipped because it requires features that are unsupported on the machine under test. *shell-condition* is a shell expression such as a `test` command. Tests before `AT_SKIP_IF` will be executed and may still cause the test group to fail. You can instantiate this macro many times from within the same test group.

You should use this macro only for very simple skip conditions. If the *shell-condition* could emit any kind of output you should instead use `AT_CHECK` like

```
AT_CHECK([if shell-condition; then exit 77; fi])
```

so that such output is properly recorded in the testsuite.log file.

**Macro: **AT_XFAIL_IF***(*shell-condition*)* ¶**

Determine whether the test is expected to fail because it is a known bug (for unsupported features, you should skip the test). *shell-condition* is a shell expression such as a `test` command; you can instantiate this macro many times from within the same test group, and one of the conditions is enough to turn the test into an expected failure.

**Macro: **AT_CLEANUP** ¶**

End the current test group.

**Macro: **AT_DATA***(*file*, *contents*)* ¶**

**Macro: **AT_DATA_UNQUOTED***(*file*, *contents*)* ¶**

Initialize an input data *file* with given *contents*. Of course, the *contents* have to be properly quoted between square brackets to protect against included commas or spurious M4 expansion. *contents* must be empty or end with a newline. *file* must be a single shell word that expands into a single file name.

The difference between `AT_DATA` and `AT_DATA_UNQUOTED` is that only the latter performs shell variable expansion (‘$’), command substitution (‘`’), and backslash escaping (‘\’) on *contents*.

**Macro: **AT_CHECK***(*commands*, [*status* = ‘0’], [*stdout*], [*stderr*], [*run-if-fail*], [*run-if-pass*])* ¶**

**Macro: **AT_CHECK_UNQUOTED***(*commands*, [*status* = ‘0’], [*stdout*], [*stderr*], [*run-if-fail*], [*run-if-pass*])* ¶**

Perform a test, by running the shell *commands* in a subshell. *commands* is output as-is, so shell expansions are honored. These commands are expected to have a final exit status of *status*, and to produce output as described by *stdout* and *stderr* (see below).

This macro must be invoked in between `AT_SETUP` and `AT_CLEANUP`.

If *commands* exit with unexpected status 77, then the rest of the test group is skipped. If *commands* exit with unexpected status 99, then the test group is immediately failed; this is called a *hard failure*. Otherwise, the test is considered to have succeeded if all of the status, stdout, and stderr expectations were met.

If *run-if-fail* is nonempty, it provides extra shell commands to run when the test fails; if *run-if-pass* is nonempty, it provides extra shell commands to run when the test succeeds. These commands are *not* run in a subshell, and they are not run when the test group is skipped (exit code 77) or hard-failed (exit code 99). They may change whether the test group is considered to have succeeded, by modifying the shell variable `at_failed`; set it to `:` to indicate that the test group has failed, or `false` to indicate that it has succeeded.

The exit status of *commands* is available to *run-if-fail* and *run-if-pass* commands in the `at_status` shell variable. The output from *commands* is also available, in the files named by the `at_stdout` and `at_stderr` variables.

If *status* is the literal ‘ignore’, then the exit status of *commands* is not checked, except for the special cases of 77 (skip) and 99 (hard failure). The existence of hard failures allows one to mark a test as an expected failure with `AT_XFAIL_IF` because a feature has not yet been implemented, but to still distinguish between gracefully handling the missing feature and dumping core.

If the value of the *stdout* or *stderr* parameter is one of the literals in the following table, then the test treats the output according to the rules of that literal.

**‘ignore’**

The content of the output is ignored, but still captured in the test group log (if the testsuite is run with the -v option, the test group log is displayed as the test is run; if the test group later fails, the test group log is also copied into the overall testsuite log). This action is valid for both *stdout* and *stderr*.

**‘ignore-nolog’**

The content of the output is ignored, and nothing is captured in the log files. If *commands* are likely to produce binary output (including long lines) or large amounts of output, then logging the output can make it harder to locate details related to subsequent tests within the group, and could potentially corrupt terminal display of a user running `testsuite -v`. This action is valid for both *stdout* and *stderr*.

**‘stdout’**

Only valid as the *stdout* parameter. Capture the content of standard output in both a file named stdout and the test group log. Subsequent commands in the test group can then post-process the file. This action is often used when it is desired to use `grep` to look for a substring in the output, or when the output must be post-processed to normalize error messages into a common form.

**‘stderr’**

Only valid as the *stderr* parameter. Capture the content of standard error in both a file named stderr and the test group log.

**‘stdout-nolog’**

**‘stderr-nolog’**

Like ‘stdout’ or ‘stderr’, except that the captured output is not duplicated into the test group log. This action is particularly useful for an intermediate check that produces large amounts of data, which will be followed by another check that filters down to the relevant data, as it makes it easier to locate details in the log.

**‘expout’**

Only valid as the *stdout* parameter. Compare standard output with the previously created file expout, and list any differences in the testsuite log.

**‘experr’**

Only valid as the *stderr* parameter. Compare standard error with the previously created file experr, and list any differences in the testsuite log.

Otherwise, the values of the *stdout* and *stderr* parameters are treated as text that must exactly match the output given by *commands* on standard output and standard error (including an empty parameter for no output); any differences are captured in the testsuite log and the test is failed (unless an unexpected exit status of 77 skipped the test instead).

`AT_CHECK_UNQUOTED` performs shell variable expansion (‘$’), command substitution (‘`’), and backslash escaping (‘\’) on comparison text given in the *stdout* and *stderr* parameters; `AT_CHECK` does not. There is no difference in the interpretation of *commands*.

**Macro: **AT_CHECK_EUNIT***(*module*, *test-spec*, [*erlflags*], [*run-if-fail*], [*run-if-pass*])* ¶**

Initialize and execute an Erlang module named *module* that performs tests following the *test-spec* EUnit test specification. *test-spec* must be a valid EUnit test specification, as defined in the EUnit Reference Manual. *erlflags* are optional command-line options passed to the Erlang interpreter to execute the test Erlang module. Typically, *erlflags* defines at least the paths to directories containing the compiled Erlang modules under test, as ‘-pa path1 path2 ...’.

For example, the unit tests associated with Erlang module ‘testme’, which compiled code is in subdirectory src, can be performed with:

```
AT_CHECK_EUNIT([testme_testsuite], [{module, testme}],
               [-pa "${abs_top_builddir}/src"])
```

This macro must be invoked in between `AT_SETUP` and `AT_CLEANUP`.

Variables `ERL`, `ERLC`, and (optionally) `ERLCFLAGS` must be defined as the path of the Erlang interpreter, the path of the Erlang compiler, and the command-line flags to pass to the compiler, respectively. Those variables should be configured in configure.ac using the `AC_ERLANG_PATH_ERL` and `AC_ERLANG_PATH_ERLC` macros, and the configured values of those variables are automatically defined in the testsuite. If `ERL` or `ERLC` is not defined, the test group is skipped.

If the EUnit library cannot be found, i.e. if module `eunit` cannot be loaded, the test group is skipped. Otherwise, if *test-spec* is an invalid EUnit test specification, the test group fails. Otherwise, if the EUnit test passes, shell commands *run-if-pass* are executed or, if the EUnit test fails, shell commands *run-if-fail* are executed and the test group fails.

Only the generated test Erlang module is automatically compiled and executed. If *test-spec* involves testing other Erlang modules, e.g. module ‘testme’ in the example above, those modules must be already compiled.

If the testsuite is run in verbose mode and with the --verbose option, EUnit is also run in verbose mode to output more details about individual unit tests.

### 19.3 Running `testsuite` Scripts

Autotest test suites support the following options:

**--help**

**-h**

Display the list of options and exit successfully.

**--version**

**-V**

Display the version of the test suite and exit successfully.

**--directory=*dir***

**-C *dir***

Change the current directory to *dir* before creating any files. Useful for running the testsuite in a subdirectory from a top-level Makefile.

**--jobs[=*n*]**

**-j[*n*]**

Run *n* tests in parallel, if possible. If *n* is not given, run all given tests in parallel. Note that there should be no space before the argument to -j, as -j *number* denotes the separate arguments -j and *number*, see below.

In parallel mode, the standard input device of the testsuite script is not available to commands inside a test group. Furthermore, banner lines are not printed, and the summary line for each test group is output after the test group completes. Summary lines may appear unordered. If verbose and trace output are enabled (see below), they may appear intermixed from concurrently running tests.

Parallel mode requires the `mkfifo` command to work, and will be silently disabled otherwise.

**--clean**

**-c**

Remove all the files the test suite might have created and exit. Meant for `clean` Make targets.

**--list**

**-l**

List all the tests (or only the selection), including their possible keywords.

By default all tests are performed (or described with --list) silently in the default environment, but the environment, set of tests, and verbosity level can be tuned:

**‘*variable*=*value*’**

Set the environment *variable* to *value*. Use this rather than ‘FOO=foo ./testsuite’ as debugging scripts would then run in a different environment.

The variable `AUTOTEST_PATH` specifies the testing path to prepend to `PATH`. Relative directory names (not starting with ‘/’) are considered to be relative to the top level of the package being built. All directories are made absolute, first starting from the top level *build* tree, then from the *source* tree. For instance ‘./testsuite AUTOTEST_PATH=tests:bin’ for a /src/foo-1.0 source package built in /tmp/foo results in ‘/tmp/foo/tests:/tmp/foo/bin’ and then ‘/src/foo-1.0/tests:/src/foo-1.0/bin’ being prepended to `PATH`.

**‘*number*’**

**‘*number*-*number*’**

**‘*number*-’**

**‘-*number*’**

Add the corresponding test groups, with obvious semantics, to the selection.

**‘--keywords=*keywords*’**

**‘-k *keywords*’**

Add to the selection the test groups with title or keywords (arguments to `AT_SETUP` or `AT_KEYWORDS`) that match *all* keywords of the comma separated list *keywords*, case-insensitively. Use ‘!’ immediately before the keyword to invert the selection for this keyword. By default, the keywords match whole words; enclose them in ‘.*’ to also match parts of words.

For example, running

```
./testsuite -k 'autoupdate,.*FUNC.*'
```

selects all tests tagged ‘autoupdate’ *and* with tags containing ‘FUNC’ (as in ‘AC_CHECK_FUNC’, ‘AC_FUNC_ALLOCA’, etc.), while

```
./testsuite -k '!autoupdate' -k '.*FUNC.*'
```

selects all tests not tagged ‘autoupdate’ *or* with tags containing ‘FUNC’.

**‘--errexit’**

**‘-e’**

If any test fails, immediately abort testing. This implies --debug: post test group clean up, and top-level logging are inhibited. This option is meant for the full test suite, it is not really useful for generated debugging scripts. If the testsuite is run in parallel mode using --jobs, then concurrently running tests will finish before exiting.

**‘--verbose’**

**‘-v’**

Force more verbosity in the detailed output of what is being done. This is the default for debugging scripts.

**‘--color’**

**‘--color[=never|auto|always]’**

Enable colored test results. Without an argument, or with ‘always’, test results will be colored. With ‘never’, color mode is turned off. Otherwise, if either the macro `AT_COLOR_TESTS` is used by the testsuite author, or the argument ‘auto’ is given, then test results are colored if standard output is connected to a terminal.

**‘--debug’**

**‘-d’**

Do not remove the files after a test group was performed—but they are still removed *before*, therefore using this option is sane when running several test groups. Create debugging scripts. Do not overwrite the top-level log (in order to preserve a supposedly existing full log file). This is the default for debugging scripts, but it can also be useful to debug the testsuite itself.

**‘--recheck’**

Add to the selection all test groups that failed or passed unexpectedly during the last non-debugging test run.

**‘--trace’**

**‘-x’**

Trigger shell tracing of the test groups.

Besides these options accepted by every Autotest testsuite, the testsuite author might have added package-specific options via the `AT_ARG_OPTION` and `AT_ARG_OPTION_ARG` macros (see Writing testsuite.at); refer to `testsuite --help` and the package documentation for details.

### 19.4 Making `testsuite` Scripts

For putting Autotest into movement, you need some configuration and makefile machinery. We recommend, at least if your package uses deep or shallow hierarchies, that you use tests/ as the name of the directory holding all your tests and their makefile. Here is a check list of things to do, followed by an example, taking into consideration whether you are also using Automake.

- Make sure to create the file package.m4, which defines the identity of the package. It must define `AT_PACKAGE_STRING`, the full signature of the package, and `AT_PACKAGE_BUGREPORT`, the address to which bug reports should be sent. For sake of completeness, we suggest that you also define `AT_PACKAGE_NAME`, `AT_PACKAGE_TARNAME`, `AT_PACKAGE_VERSION`, and `AT_PACKAGE_URL`. See Initializing `configure`, for a description of these variables. Be sure to distribute package.m4 and to put it into the source hierarchy: the test suite ought to be shipped! See below for an example.
- Invoke `AC_CONFIG_TESTDIR` in your configure.ac. Macro: **AC_CONFIG_TESTDIR***(*directory*, [*test-path* = *directory*])* ¶ An Autotest test suite is to be configured in *directory*. This macro causes *directory*/atconfig to be created by `config.status` and sets the default `AUTOTEST_PATH` to *test-path* (see Running `testsuite` Scripts).
- Still within configure.ac, as appropriate, ensure that some `AC_CONFIG_FILES` command includes substitution for tests/atlocal.
- Also within your configure.ac, arrange for the `AUTOM4TE` variable to be set.
- The appropriate Makefile should be modified so the validation in your package is triggered by ‘make check’.

The following example demonstrates the above checklist, first by assuming that you are using Automake (see below for tweaks to make to get the same results without Automake). Begin by adding the following lines to your configure.ac:

```
# Initialize the test suite.
AC_CONFIG_TESTDIR([tests])
AC_CONFIG_FILES([tests/Makefile tests/atlocal])
AM_MISSING_PROG([AUTOM4TE], [autom4te])
```

Next, add the following lines to your tests/Makefile.am, in order to link ‘make check’ with a validation suite.

```
$(srcdir)/package.m4: $(top_srcdir)/configure.ac
        printf >'$@' '%s\n' \
          '# Signature of the current package.' \
          'm4_define([AT_PACKAGE_NAME], [$(PACKAGE_NAME)])' \
          'm4_define([AT_PACKAGE_TARNAME], [$(PACKAGE_TARNAME)])' \
          'm4_define([AT_PACKAGE_VERSION], [$(PACKAGE_VERSION)])' \
          'm4_define([AT_PACKAGE_STRING], [$(PACKAGE_STRING)])' \
          'm4_define([AT_PACKAGE_URL], [$(PACKAGE_URL)])' \
          'm4_define([AT_PACKAGE_BUGREPORT], [$(PACKAGE_BUGREPORT)])'

EXTRA_DIST = testsuite.at $(srcdir)/package.m4 $(TESTSUITE) atlocal.in
TESTSUITE = $(srcdir)/testsuite

check-local: atconfig atlocal $(TESTSUITE)
        $(SHELL) '$(TESTSUITE)' $(TESTSUITEFLAGS)

installcheck-local: atconfig atlocal $(TESTSUITE)
        $(SHELL) '$(TESTSUITE)' AUTOTEST_PATH='$(bindir)' \
          $(TESTSUITEFLAGS)

clean-local:
        test ! -f '$(TESTSUITE)' || \
         $(SHELL) '$(TESTSUITE)' --clean

AUTOTEST = $(AUTOM4TE) --language=autotest
$(TESTSUITE): $(srcdir)/testsuite.at $(srcdir)/package.m4
        $(AUTOTEST) -I '$(srcdir)' -o $@.tmp $@.at
        mv $@.tmp $@
```

Note that the built testsuite is distributed; this is necessary because users might not have Autoconf installed, and thus would not be able to rebuild it. Likewise, the use of Automake’s `AM_MISSING_PROG` will arrange for the definition of `$AUTOM4TE` within the Makefile to provide the user with a nicer error message if they modify a source file to the testsuite, and accidentally trigger the rebuild rules.

You might want to list explicitly the dependencies, i.e., the list of the files testsuite.at includes.

If you don’t use Automake, you should make the following tweaks. In your configure.ac, replace the `AM_MISSING_PROG` line above with `AC_PATH_PROG([AUTOM4TE], [autom4te], [false])`. You are welcome to also try using the `missing` script from the Automake project instead of `false`, to try to get a nicer error message when the user modifies prerequisites but did not have Autoconf installed, but at that point you may be better off using Automake. Then, take the code suggested above for tests/Makefile.am and place it in your tests/Makefile.in instead. Add code to your tests/Makefile.in to ensure that `$(EXTRA_DIST)` files are distributed, as well as adding the following additional lines to prepare the set of needed Makefile variables:

```
subdir = tests
PACKAGE_NAME = @PACKAGE_NAME@
PACKAGE_TARNAME = @PACKAGE_TARNAME@
PACKAGE_VERSION = @PACKAGE_VERSION@
PACKAGE_STRING = @PACKAGE_STRING@
PACKAGE_BUGREPORT = @PACKAGE_BUGREPORT@
PACKAGE_URL = @PACKAGE_URL@
AUTOM4TE = @AUTOM4TE@

atconfig: $(top_builddir)/config.status
        cd $(top_builddir) && \
           $(SHELL) ./config.status $(subdir)/$@

atlocal: $(srcdir)/atlocal.in $(top_builddir)/config.status
        cd $(top_builddir) && \
           $(SHELL) ./config.status $(subdir)/$@
```

Using the above example (with or without Automake), and assuming you were careful to not initialize ‘TESTSUITEFLAGS’ within your makefile, you can now fine-tune test suite execution at runtime by altering this variable, for example:

```
make check TESTSUITEFLAGS='-v -d -x 75 -k AC_PROG_CC CFLAGS=-g'
```

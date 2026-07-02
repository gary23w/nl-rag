---
title: "Autoconf (part 7/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 7/26
---

## 6 Writing Tests

If the existing feature tests don’t do something you need, you have to write new ones. These macros are the building blocks. They provide ways for other macros to check whether various kinds of features are available and report the results.

This chapter contains some suggestions and some of the reasons why the existing tests are written the way they are. You can also learn a lot about how to write Autoconf tests by looking at the existing ones. If something goes wrong in one or more of the Autoconf tests, this information can help you understand the assumptions behind them, which might help you figure out how to best solve the problem.

These macros check the output of the compiler system of the current language (see Language Choice). They do not cache the results of their tests for future use (see Caching Results), because they don’t know enough about the information they are checking for to generate a cache variable name. They also do not print any messages, for the same reason. The checks for particular kinds of features call these macros and do cache their results and print messages about what they’re checking for.

When you write a feature test that could be applicable to more than one software package, the best thing to do is encapsulate it in a new macro. See Writing Autoconf Macros, for how to do that.

### 6.1 Language Choice

Autoconf-generated `configure` scripts check for the C compiler and its features by default. Packages that use other programming languages (maybe more than one, e.g., C and C++) need to test features of the compilers for the respective languages. The following macros determine which programming language is used in the subsequent tests in configure.ac.

**Macro: **AC_LANG***(*language*)* ¶**

Do compilation tests using the compiler, preprocessor, and file extensions for the specified *language*.

Supported languages are:

**‘C’**

Do compilation tests using `CC` and `CPP` and use extension .c for test programs. Use compilation flags: `CPPFLAGS` with `CPP`, and both `CPPFLAGS` and `CFLAGS` with `CC`.

**‘C++’**

Do compilation tests using `CXX` and `CXXCPP` and use extension .C for test programs. Use compilation flags: `CPPFLAGS` with `CXXCPP`, and both `CPPFLAGS` and `CXXFLAGS` with `CXX`.

**‘Fortran 77’**

Do compilation tests using `F77` and use extension .f for test programs. Use compilation flags: `FFLAGS`.

**‘Fortran’**

Do compilation tests using `FC` and use extension .f (or whatever has been set by `AC_FC_SRCEXT`) for test programs. Use compilation flags: `FCFLAGS`.

**‘Erlang’ ¶**

Compile and execute tests using `ERLC` and `ERL` and use extension .erl for test Erlang modules. Use compilation flags: `ERLCFLAGS`.

**‘Objective C’**

Do compilation tests using `OBJC` and `OBJCPP` and use extension .m for test programs. Use compilation flags: `CPPFLAGS` with `OBJCPP`, and both `CPPFLAGS` and `OBJCFLAGS` with `OBJC`.

**‘Objective C++’**

Do compilation tests using `OBJCXX` and `OBJCXXCPP` and use extension .mm for test programs. Use compilation flags: `CPPFLAGS` with `OBJCXXCPP`, and both `CPPFLAGS` and `OBJCXXFLAGS` with `OBJCXX`.

**‘Go’**

Do compilation tests using `GOC` and use extension .go for test programs. Use compilation flags `GOFLAGS`.

**‘Algol 68’**

Do compilation tests using `A68` and use extension .a68 for test programs. Use compilation flags `A68FLAGS`.

**Macro: **AC_LANG_PUSH***(*language*)* ¶**

Remember the current language (as set by `AC_LANG`) on a stack, and then select the *language*. Use this macro and `AC_LANG_POP` in macros that need to temporarily switch to a particular language.

**Macro: **AC_LANG_POP***([*language*])* ¶**

Select the language that is saved on the top of the stack, as set by `AC_LANG_PUSH`, and remove it from the stack.

If given, *language* specifies the language we just *quit*. It is a good idea to specify it when it’s known (which should be the case…), since Autoconf detects inconsistencies.

```
AC_LANG_PUSH([Fortran 77])
# Perform some tests on Fortran 77.
# ...
AC_LANG_POP([Fortran 77])
```

**Macro: **AC_LANG_ASSERT***(*language*)* ¶**

Check statically that the current language is *language*. You should use this in your language specific macros to avoid that they be called with an inappropriate language.

This macro runs only at `autoconf` time, and incurs no cost at `configure` time. Sadly enough and because Autoconf is a two layer language 2, the macros `AC_LANG_PUSH` and `AC_LANG_POP` cannot be “optimizing”, therefore as much as possible you ought to avoid using them to wrap your code, rather, require from the user to run the macro with a correct current language, and check it with `AC_LANG_ASSERT`. And anyway, that may help the user understand she is running a Fortran macro while expecting a result about her Fortran 77 compiler...

**Macro: **AC_REQUIRE_CPP** ¶**

Ensure that whichever preprocessor would currently be used for tests has been found. Calls `AC_REQUIRE` (see Prerequisite Macros) with an argument of either `AC_PROG_CPP` or `AC_PROG_CXXCPP`, depending on which language is current.

### 6.2 Writing Test Programs

Autoconf tests follow a common scheme: feed some program with some input, and most of the time, feed a compiler with some source file. This section is dedicated to these source samples.

#### 6.2.1 Guidelines for Test Programs

The most important rule to follow when writing testing samples is:

Look for realism.

This motto means that testing samples must be written with the same strictness as real programs are written. In particular, you should avoid “shortcuts” and simplifications.

Don’t just play with the preprocessor if you want to prepare a compilation. For instance, using `cpp` to check whether a header is functional might let your `configure` accept a header which causes some *compiler* error. Do not hesitate to check a header with other headers included before, especially required headers.

Make sure the symbols you use are properly defined, i.e., refrain from simply declaring a function yourself instead of including the proper header.

Test programs should not write to standard output. They should exit with status 0 if the test succeeds, and with status 1 otherwise, so that success can be distinguished easily from a core dump or other failure; segmentation violations and other failures produce a nonzero exit status. Unless you arrange for `exit` to be declared, test programs should `return`, not `exit`, from `main`, because on many systems `exit` is not declared by default.

Test programs can use `#if` or `#ifdef` to check the values of preprocessor macros defined by tests that have already run. For example, if you call `AC_HEADER_STDBOOL`, then later on in configure.ac you can have a test program that includes stdbool.h conditionally:

```
#ifdef HAVE_STDBOOL_H
# include <stdbool.h>
#endif
```

Both `#if HAVE_STDBOOL_H` and `#ifdef HAVE_STDBOOL_H` will work with any standard C compiler. Some developers prefer `#if` because it is easier to read, while others prefer `#ifdef` because it avoids diagnostics with picky compilers like GCC with the -Wundef option.

If a test program needs to use or create a data file, give it a name that starts with conftest, such as conftest.data. The `configure` script cleans up by running ‘rm -f -r conftest*’ after running test programs and if the script is interrupted.

#### 6.2.2 Test Functions

Functions in test code should use function prototypes, introduced in C89 and required in C23.

Functions that test programs declare should also be conditionalized for C++, which requires ‘extern "C"’ prototypes. Make sure to not include any header files containing clashing prototypes.

```
#ifdef __cplusplus
extern "C"
#endif
void *valloc (size_t);
```

If a test program calls a function with invalid parameters (just to see whether it exists), organize the program to ensure that it never invokes that function. You can do this by calling it in another function that is never invoked. You can’t do it by putting it after a call to `exit`, because GCC version 2 knows that `exit` never returns and optimizes out any code that follows it in the same block.

If you include any header files, be sure to call the functions relevant to them with the correct number of arguments, even if they are just 0, to avoid compilation errors due to prototypes. GCC version 2 has internal prototypes for several functions that it automatically inlines; for example, `memcpy`. To avoid errors when checking for them, either pass them the correct number of arguments or redeclare them with a different return type (such as `char`).

#### 6.2.3 Generating Sources

Autoconf provides a set of macros that can be used to generate test source files. They are written to be language generic, i.e., they actually depend on the current language (see Language Choice) to “format” the output properly.

**Macro: **AC_LANG_CONFTEST***(*source*)* ¶**

Save the *source* text in the current test source file: conftest.*extension* where the *extension* depends on the current language. As of Autoconf 2.63b, the source file also contains the results of all of the `AC_DEFINE` performed so far.

Note that the *source* is evaluated exactly once, like regular Autoconf macro arguments, and therefore (i) you may pass a macro invocation, (ii) if not, be sure to double quote if needed.

The *source* text is expanded as an unquoted here-document, so ‘$’, ‘`’ and some ‘\’s should be backslash-escaped. See Here-Documents.

This macro issues a warning during `autoconf` processing if *source* does not include an expansion of the macro `AC_LANG_DEFINES_PROVIDED` (note that both `AC_LANG_SOURCE` and `AC_LANG_PROGRAM` call this macro, and thus avoid the warning).

This macro is seldom called directly, but is used under the hood by more common macros such as `AC_COMPILE_IFELSE` and `AC_RUN_IFELSE`.

**Macro: **AC_LANG_DEFINES_PROVIDED** ¶**

This macro is called as a witness that the file conftest.*extension* appropriate for the current language is complete, including all previously determined results from `AC_DEFINE`. This macro is seldom called directly, but exists if you have a compelling reason to write a conftest file without using `AC_LANG_SOURCE`, yet still want to avoid a syntax warning from `AC_LANG_CONFTEST`.

**Macro: **AC_LANG_SOURCE***(*source*)* ¶**

Expands into the *source*, with the definition of all the `AC_DEFINE` performed so far. This macro includes an expansion of `AC_LANG_DEFINES_PROVIDED`.

In many cases, you may find it more convenient to use the wrapper `AC_LANG_PROGRAM`.

For instance, executing (observe the double quotation!):

```
AC_INIT([Hello], [1.0], [bug-hello@example.org], [],
        [https://www.example.org/])
AC_DEFINE([HELLO_WORLD], ["Hello, World\n"],
  [Greetings string.])
AC_LANG([C])
AC_LANG_CONFTEST(
   [AC_LANG_SOURCE([[const char hw[] = "Hello, World\n";]])])
gcc -E -dD conftest.c
```

on a system with `gcc` installed, results in:

```
...
# 1 "conftest.c"

#define PACKAGE_NAME "Hello"
#define PACKAGE_TARNAME "hello"
#define PACKAGE_VERSION "1.0"
#define PACKAGE_STRING "Hello 1.0"
#define PACKAGE_BUGREPORT "bug-hello@example.org"
#define PACKAGE_URL "https://www.example.org/"
#define HELLO_WORLD "Hello, World\n"

const char hw[] = "Hello, World\n";
```

When the test language is Fortran, Erlang, Go, or Algol 68, the `AC_DEFINE` definitions are not automatically translated into constants in the source code by this macro.

**Macro: **AC_LANG_PROGRAM***([*prologue*], [*body*])* ¶**

Expands into a source file which consists of the *prologue*, and then *body* as body of the main function (e.g., `main` in C). Since it uses `AC_LANG_SOURCE`, the features of the latter are available.

For instance:

```
AC_INIT([Hello], [1.0], [bug-hello@example.org], [],
        [https://www.example.org/])
AC_DEFINE([HELLO_WORLD], ["Hello, World\n"],
  [Greetings string.])
AC_LANG_CONFTEST(
[AC_LANG_PROGRAM([[const char hw[] = "Hello, World\n";]],
                 [[fputs (hw, stdout);]])])
gcc -E -dD conftest.c
```

on a system with `gcc` installed, results in:

```
...
# 1 "conftest.c"

#define PACKAGE_NAME "Hello"
#define PACKAGE_TARNAME "hello"
#define PACKAGE_VERSION "1.0"
#define PACKAGE_STRING "Hello 1.0"
#define PACKAGE_BUGREPORT "bug-hello@example.org"
#define PACKAGE_URL "https://www.example.org/"
#define HELLO_WORLD "Hello, World\n"

const char hw[] = "Hello, World\n";
int
main (void)
{
fputs (hw, stdout);
  ;
  return 0;
}
```

In Erlang tests, the created source file is that of an Erlang module called `conftest` (conftest.erl). This module defines and exports at least one `start/0` function, which is called to perform the test. The *prologue* is optional code that is inserted between the module header and the `start/0` function definition. *body* is the body of the `start/0` function without the final period (see Checking Runtime Behavior, about constraints on this function’s behavior).

For instance:

```
AC_INIT([Hello], [1.0], [bug-hello@example.org])
AC_LANG(Erlang)
AC_LANG_CONFTEST(
[AC_LANG_PROGRAM([[-define(HELLO_WORLD, "Hello, world!").]],
                 [[io:format("~s~n", [?HELLO_WORLD])]])])
cat conftest.erl
```

results in:

```
-module(conftest).
-export([start/0]).
-define(HELLO_WORLD, "Hello, world!").
start() ->
io:format("~s~n", [?HELLO_WORLD])
.
```

**Macro: **AC_LANG_CALL***(*prologue*, *function*)* ¶**

Expands into a source file which consists of the *prologue*, and then a call to the *function* as body of the main function (e.g., `main` in C). Since it uses `AC_LANG_PROGRAM`, the feature of the latter are available.

This function will probably be replaced in the future by a version which would enable specifying the arguments. The use of this macro is not encouraged, as it violates strongly the typing system.

This macro cannot be used for Erlang tests.

**Macro: **AC_LANG_FUNC_LINK_TRY***(*function*)* ¶**

Expands into a source file which uses the *function* in the body of the main function (e.g., `main` in C). Since it uses `AC_LANG_PROGRAM`, the features of the latter are available.

As `AC_LANG_CALL`, this macro is documented only for completeness. It is considered to be severely broken, and in the future will be removed in favor of actual function calls (with properly typed arguments).

This macro cannot be used for Erlang tests.

### 6.3 Running the Preprocessor

Sometimes one might need to run the preprocessor on some source file. *Usually it is a bad idea*, as you typically need to *compile* your project, not merely run the preprocessor on it; therefore you certainly want to run the compiler, not the preprocessor. Resist the temptation of following the easiest path.

Nevertheless, if you need to run the preprocessor, then use `AC_PREPROC_IFELSE`.

The macros described in this section cannot be used for tests in Erlang, Fortran, Go, or Algol 68 since those languages require no preprocessor.

**Macro: **AC_PREPROC_IFELSE***(*input*, [*action-if-true*], [*action-if-false*])* ¶**

Run the preprocessor of the current language (see Language Choice) on the *input*, run the shell commands *action-if-true* on success, *action-if-false* otherwise.

If *input* is nonempty use the equivalent of `AC_LANG_CONFTEST(*input*)` to generate the current test source file; otherwise reuse the already-existing test source file. The *input* can be made by `AC_LANG_PROGRAM` and friends. The *input* text is expanded as an unquoted here-document, so ‘$’, ‘`’ and some ‘\’s should be backslash-escaped. See Here-Documents.

This macro uses `CPPFLAGS`, but not `CFLAGS`, because -g, -O, etc. are not valid options to many C preprocessors.

It is customary to report unexpected failures with `AC_MSG_FAILURE`. If needed, *action-if-true* can further access the preprocessed output in the file conftest.i.

For instance:

```
AC_INIT([Hello], [1.0], [bug-hello@example.org])
AC_DEFINE([HELLO_WORLD], ["Hello, World\n"],
  [Greetings string.])
AC_PREPROC_IFELSE(
   [AC_LANG_PROGRAM([[const char hw[] = "Hello, World\n";]],
                    [[fputs (hw, stdout);]])],
   [AC_MSG_RESULT([OK])],
   [AC_MSG_FAILURE([unexpected preprocessor failure])])
```

might result in:

```
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C23 features... -std=gnu23
checking how to run the C preprocessor... gcc -std=gnu23 -E
OK
```

The macro `AC_TRY_CPP` (see Obsolete Macros) used to play the role of `AC_PREPROC_IFELSE`, but double quotes its argument, making it impossible to use it to elaborate sources. You are encouraged to get rid of your old use of the macro `AC_TRY_CPP` in favor of `AC_PREPROC_IFELSE`, but, in the first place, are you sure you need to run the *preprocessor* and not the compiler?

**Macro: **AC_EGREP_HEADER***(*pattern*, *header-file*, *action-if-found*, [*action-if-not-found*])* ¶**

*pattern*, after being expanded as if in a double-quoted shell string, is an extended regular expression. If the output of running the preprocessor on the system header file *header-file* contains a line matching *pattern*, execute shell commands *action-if-found*, otherwise execute *action-if-not-found*.

See below for some problems involving this macro.

**Macro: **AC_EGREP_CPP***(*pattern*, *program*, [*action-if-found*], [*action-if-not-found*])* ¶**

*pattern*, after being expanded as if in a double-quoted shell string, is an extended regular expression. *program* is the text of a C or C++ program, which is expanded as an unquoted here-document (see Here-Documents). If the output of running the preprocessor on *program* contains a line matching *pattern*, execute shell commands *action-if-found*, otherwise execute *action-if-not-found*.

See below for some problems involving this macro.

`AC_EGREP_CPP` and `AC_EGREP_HEADER` should be used with care, as preprocessors can insert line breaks between output tokens. For example, the preprocessor might transform this:

```
#define MAJOR 2
#define MINOR 23
Version MAJOR . MINOR
```

into this:

```
Version
       2
                 .
                   23
```

Because preprocessors are allowed to insert white space, change escapes in string constants, insert backlash-newline pairs, or do any of a number of things that do not change the meaning of the preprocessed program, it is better to rely on `AC_PREPROC_IFELSE` than to resort to `AC_EGREP_CPP` or `AC_EGREP_HEADER`.

For more information about what can appear in portable extended regular expressions, see Problematic Expressions in *GNU Grep*.

### 6.4 Running the Compiler

To check for a syntax feature of the current language’s (see Language Choice) compiler, such as whether it recognizes a certain keyword, or simply to try some library feature, use `AC_COMPILE_IFELSE` to try to compile a small program that uses that feature.

**Macro: **AC_COMPILE_IFELSE***(*input*, [*action-if-true*], [*action-if-false*])* ¶**

Run the compiler and compilation flags of the current language (see Language Choice) on the *input*, run the shell commands *action-if-true* on success, *action-if-false* otherwise.

If *input* is nonempty use the equivalent of `AC_LANG_CONFTEST(*input*)` to generate the current test source file; otherwise reuse the already-existing test source file. The *input* can be made by `AC_LANG_PROGRAM` and friends. The *input* text is expanded as an unquoted here-document, so ‘$’, ‘`’ and some ‘\’s should be backslash-escaped. See Here-Documents.

It is customary to report unexpected failures with `AC_MSG_FAILURE`. This macro does not try to link; use `AC_LINK_IFELSE` if you need to do that (see Running the Linker). If needed, *action-if-true* can further access the just-compiled object file conftest.$OBJEXT.

This macro uses `AC_REQUIRE` for the compiler associated with the current language, which means that if the compiler has not yet been determined, the compiler determination will be made prior to the body of the outermost `AC_DEFUN` macro that triggered this macro to expand (see Expanded Before Required).

For tests in Erlang, the *input* must be the source code of a module named `conftest`. `AC_COMPILE_IFELSE` generates a conftest.beam file that can be interpreted by the Erlang virtual machine (`ERL`). It is recommended to use `AC_LANG_PROGRAM` to specify the test program, to ensure that the Erlang module has the right name.

### 6.5 Running the Linker

To check for a library, a function, or a global variable, Autoconf `configure` scripts try to compile and link a small program that uses it. This is unlike Metaconfig, which by default uses `nm` or `ar` on the C library to try to figure out which functions are available. Trying to link with the function is usually a more reliable approach because it avoids dealing with the variations in the options and output formats of `nm` and `ar` and in the location of the standard libraries. It also allows configuring for cross-compilation or checking a function’s runtime behavior if needed. On the other hand, it can be slower than scanning the libraries once, but accuracy is more important than speed.

`AC_LINK_IFELSE` is used to compile test programs to test for functions and global variables. It is also used by `AC_CHECK_LIB` to check for libraries (see Library Files), by adding the library being checked for to `LIBS` temporarily and trying to link a small program.

**Macro: **AC_LINK_IFELSE***(*input*, [*action-if-true*], [*action-if-false*])* ¶**

Run the compiler (and compilation flags) and the linker of the current language (see Language Choice) on the *input*, run the shell commands *action-if-true* on success, *action-if-false* otherwise. If needed, *action-if-true* can further access the just-linked program file conftest$EXEEXT.

If *input* is nonempty use the equivalent of `AC_LANG_CONFTEST(*input*)` to generate the current test source file; otherwise reuse the already-existing test source file. The *input* can be made by `AC_LANG_PROGRAM` and friends. The *input* text is expanded as an unquoted here-document, so ‘$’, ‘`’ and some ‘\’s should be backslash-escaped. See Here-Documents.

`LDFLAGS` and `LIBS` are used for linking, in addition to the current compilation flags.

It is customary to report unexpected failures with `AC_MSG_FAILURE`. This macro does not try to execute the program; use `AC_RUN_IFELSE` if you need to do that (see Checking Runtime Behavior).

The `AC_LINK_IFELSE` macro cannot be used for Erlang tests, since Erlang programs are interpreted and do not require linking.

### 6.6 Checking Runtime Behavior

Sometimes you need to find out how a system performs at runtime, such as whether a given function has a certain capability or bug. If you can, make such checks when your program runs instead of when it is configured. You can check for things like the machine’s endianness when your program initializes itself.

If you really need to test for a runtime behavior while configuring, you can write a test program to determine the result, and compile and run it using `AC_RUN_IFELSE`. Avoid running test programs if possible, because this prevents people from configuring your package for cross-compiling.

**Macro: **AC_RUN_IFELSE***(*input*, [*action-if-true*], [*action-if-false*], [*action-if-cross-compiling* = ‘AC_MSG_FAILURE’])* ¶**

Run the compiler (and compilation flags) and the linker of the current language (see Language Choice) on the *input*, then execute the resulting program. If the program returns an exit status of 0 when executed, run shell commands *action-if-true*. Otherwise, run shell commands *action-if-false*.

If *input* is nonempty use the equivalent of `AC_LANG_CONFTEST(*input*)` to generate the current test source file; otherwise reuse the already-existing test source file. The *input* can be made by `AC_LANG_PROGRAM` and friends. The *input* text is expanded as an unquoted here-document, so ‘$’, ‘`’ and some ‘\’s should be backslash-escaped. See Here-Documents.

`LDFLAGS` and `LIBS` are used for linking, in addition to the compilation flags of the current language (see Language Choice). Additionally, *action-if-true* can run `./conftest$EXEEXT` for further testing.

In the *action-if-false* section, the failing exit status is available in the shell variable ‘$?’. This exit status might be that of a failed compilation, or it might be that of a failed program execution.

If cross-compilation mode is enabled (this is the case if either the compiler being used does not produce executables that run on the system where `configure` is being run, or if the options `--build` and `--host` were both specified and their values are different), then the test program is not run. If the optional shell commands *action-if-cross-compiling* are given, those commands are run instead; typically these commands provide pessimistic defaults that allow cross-compilation to work even if the guess was wrong. If the fourth argument is empty or omitted, but cross-compilation is detected, then `configure` prints an error message and exits. If you want your package to be useful in a cross-compilation scenario, you *should* provide a non-empty *action-if-cross-compiling* clause, as well as wrap the `AC_RUN_IFELSE` compilation inside an `AC_CACHE_CHECK` (see Caching Results) which allows the user to override the pessimistic default if needed.

It is customary to report unexpected failures with `AC_MSG_FAILURE`.

`autoconf` prints a warning message when creating `configure` each time it encounters a call to `AC_RUN_IFELSE` with no *action-if-cross-compiling* argument given. If you are not concerned about users configuring your package for cross-compilation, you may ignore the warning. A few of the macros distributed with Autoconf produce this warning message; but if this is a problem for you, please report it as a bug, along with an appropriate pessimistic guess to use instead.

To configure for cross-compiling you can also choose a value for those parameters based on the canonical system name (see Manual Configuration). Alternatively, set up a test results cache file with the correct values for the host system (see Caching Results).

To provide a default for calls of `AC_RUN_IFELSE` that are embedded in other macros, including a few of the ones that come with Autoconf, you can test whether the shell variable `cross_compiling` is set to ‘yes’, and then use an alternate method to get the results instead of calling the macros.

It is also permissible to temporarily assign to `cross_compiling` in order to force tests to behave as though they are in a cross-compilation environment, particularly since this provides a way to test your *action-if-cross-compiling* even when you are not using a cross-compiler.

```
# We temporarily set cross-compile mode to force AC_COMPUTE_INT
# to use the slow link-only method
save_cross_compiling=$cross_compiling
cross_compiling=yes
AC_COMPUTE_INT([...])
cross_compiling=$save_cross_compiling
```

A C or C++ runtime test should be portable. See Portable C and C++ Programming.

Erlang tests must exit themselves the Erlang VM by calling the `halt/1` function: the given status code is used to determine the success of the test (status is `0`) or its failure (status is different than `0`), as explained above. It must be noted that data output through the standard output (e.g., using `io:format/2`) may be truncated when halting the VM. Therefore, if a test must output configuration information, it is recommended to create and to output data into the temporary file named conftest.out, using the functions of module `file`. The `conftest.out` file is automatically deleted by the `AC_RUN_IFELSE` macro. For instance, a simplified implementation of Autoconf’s `AC_ERLANG_SUBST_LIB_DIR` macro is:

```
AC_INIT([LibdirTest], [1.0], [bug-libdirtest@example.org])
AC_ERLANG_NEED_ERL
AC_LANG(Erlang)
AC_RUN_IFELSE(
  [AC_LANG_PROGRAM([], [dnl
    file:write_file("conftest.out", code:lib_dir()),
    halt(0)])],
  [AS_ECHO(["code:lib_dir() returned: `cat conftest.out`"])],
  [AC_MSG_FAILURE([test Erlang program execution failed])])
```

### 6.7 Multiple Cases

Some operations are accomplished in several possible ways, depending on the OS variant. Checking for them essentially requires a “case statement”. Autoconf does not directly provide one; however, it is easy to simulate by using a shell variable to keep track of whether a way to perform the operation has been found yet.

Here is an example that uses the shell variable `fstype` to keep track of whether the remaining cases need to be checked. Note that since the value of `fstype` is under our control, we don’t have to use the longer ‘test "x$fstype" = xno’.

```
AC_MSG_CHECKING([how to get file system type])
fstype=no
# The order of these tests is important.
AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <sys/statvfs.h>
                                     #include <sys/fstyp.h>
                                   ]])],
  [AC_DEFINE([FSTYPE_STATVFS], [1],
     [Define if statvfs exists.])
   fstype=SVR4])
AS_IF([test $fstype = no],
  [AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <sys/statfs.h>
                                        #include <sys/fstyp.h>
                                      ]])],
     [AC_DEFINE([FSTYPE_USG_STATFS], [1],
        [Define if USG statfs.])
      fstype=SVR3])])
AS_IF([test $fstype = no],
  [AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <sys/statfs.h>
                                        #include <sys/vmount.h>
                                      ]])],
     [AC_DEFINE([FSTYPE_AIX_STATFS], [1],
        [Define if AIX statfs.])
      fstype=AIX])])
# (more cases omitted here)
AC_MSG_RESULT([$fstype])
```

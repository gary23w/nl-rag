---
title: "Autoconf (part 6/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 6/26
---

# Autoconf

**Macro: **AC_ERLANG_PATH_ERLC***([*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Determine an Erlang compiler to use. If `ERLC` is not already set in the environment, check for `erlc`. Set output variable `ERLC` to the complete path of the compiler command found. In addition, if `ERLCFLAGS` is not set in the environment, set it to an empty value.

The two optional arguments have the same meaning as the two last arguments of macro `AC_PATH_PROG` for looking for the `erlc` program. For example, to look for `erlc` only in the /usr/lib/erlang/bin directory:

```
AC_ERLANG_PATH_ERLC([not found], [/usr/lib/erlang/bin])
```

**Macro: **AC_ERLANG_NEED_ERLC***([*path* = ‘$PATH’])* ¶**

A simplified variant of the `AC_ERLANG_PATH_ERLC` macro, that prints an error message and exits the `configure` script if the `erlc` program is not found.

**Macro: **AC_ERLANG_PATH_ERL***([*value-if-not-found*], [*path* = ‘$PATH’])* ¶**

Determine an Erlang interpreter to use. If `ERL` is not already set in the environment, check for `erl`. Set output variable `ERL` to the complete path of the interpreter command found.

The two optional arguments have the same meaning as the two last arguments of macro `AC_PATH_PROG` for looking for the `erl` program. For example, to look for `erl` only in the /usr/lib/erlang/bin directory:

```
AC_ERLANG_PATH_ERL([not found], [/usr/lib/erlang/bin])
```

**Macro: **AC_ERLANG_NEED_ERL***([*path* = ‘$PATH’])* ¶**

A simplified variant of the `AC_ERLANG_PATH_ERL` macro, that prints an error message and exits the `configure` script if the `erl` program is not found.

#### 5.10.8 Fortran Compiler Characteristics

The Autoconf Fortran support is divided into two categories: legacy Fortran 77 macros (`F77`), and modern Fortran macros (`FC`). The former are intended for traditional Fortran 77 code, and have output variables like `F77`, `FFLAGS`, and `FLIBS`. The latter are for newer programs that can (or must) compile under the newer Fortran standards, and have output variables like `FC`, `FCFLAGS`, and `FCLIBS`.

Except for the macros `AC_FC_SRCEXT`, `AC_FC_FREEFORM`, `AC_FC_FIXEDFORM`, and `AC_FC_LINE_LENGTH` (see below), the `FC` and `F77` macros behave almost identically, and so they are documented together in this section.

**Macro: **AC_PROG_F77***([*compiler-search-list*])* ¶**

Determine a Fortran 77 compiler to use. If `F77` is not already set in the environment, then check for `g77` and `f77`, and then some other names. Set the output variable `F77` to the name of the compiler found.

This macro may, however, be invoked with an optional first argument which, if specified, must be a blank-separated list of Fortran 77 compilers to search for. This just gives the user an opportunity to specify an alternative search list for the Fortran 77 compiler. For example, if you didn’t like the default order, then you could invoke `AC_PROG_F77` like this:

```
AC_PROG_F77([fl32 f77 fort77 xlf g77 f90 xlf90])
```

If using a compiler that supports GNU Fortran 77, set the shell variable `G77` to ‘yes’. If the output variable `FFLAGS` was not already set in the environment, set it to -g -02 for `g77` (or -O2 where the GNU Fortran 77 compiler does not accept -g), or -g for other compilers.

The result of the GNU test is cached in the `ac_cv_f77_compiler_gnu` variable, acceptance of -g in the `ac_cv_prog_f77_g` variable.

**Macro: **AC_PROG_FC***([*compiler-search-list*], [*dialect*])* ¶**

Determine a Fortran compiler to use. If `FC` is not already set in the environment, then `dialect` is a hint to indicate what Fortran dialect to search for; the default is to search for the newest available dialect. Set the output variable `FC` to the name of the compiler found.

By default, newer dialects are preferred over older dialects, but if `dialect` is specified then older dialects are preferred starting with the specified dialect. `dialect` can currently be one of Fortran 77, Fortran 90, or Fortran 95. However, this is only a hint of which compiler *name* to prefer (e.g., `f90` or `f95`), and no attempt is made to guarantee that a particular language standard is actually supported. Thus, it is preferable that you avoid the `dialect` option, and use AC_PROG_FC only for code compatible with the latest Fortran standard.

This macro may, alternatively, be invoked with an optional first argument which, if specified, must be a blank-separated list of Fortran compilers to search for, just as in `AC_PROG_F77`.

If using a compiler that supports GNU Fortran, set the shell variable `GFC` to ‘yes’. If the output variable `FCFLAGS` was not already set in the environment, then set it to -g -02 for a GNU Fortran compiler (or -O2 where the compiler does not accept -g), or -g for other compilers.

The result of the GNU test is cached in the `ac_cv_fc_compiler_gnu` variable, acceptance of -g in the `ac_cv_prog_fc_g` variable.

**Macro: **AC_PROG_F77_C_O** ¶**

**Macro: **AC_PROG_FC_C_O** ¶**

Test whether the Fortran compiler accepts the options -c and -o simultaneously, and define `F77_NO_MINUS_C_MINUS_O` or `FC_NO_MINUS_C_MINUS_O`, respectively, if it does not.

The result of the test is cached in the `ac_cv_prog_f77_c_o` or `ac_cv_prog_fc_c_o` variable, respectively.

The following macros check for Fortran compiler characteristics. To check for characteristics not listed here, use `AC_COMPILE_IFELSE` (see Running the Compiler) or `AC_RUN_IFELSE` (see Checking Runtime Behavior), making sure to first set the current language to Fortran 77 or Fortran via `AC_LANG([Fortran 77])` or `AC_LANG(Fortran)` (see Language Choice).

**Macro: **AC_F77_LIBRARY_LDFLAGS** ¶**

**Macro: **AC_FC_LIBRARY_LDFLAGS** ¶**

Determine the linker flags (e.g., -L and -l) for the *Fortran intrinsic and runtime libraries* that are required to successfully link a Fortran program or shared library. The output variable `FLIBS` or `FCLIBS` is set to these flags (which should be included after `LIBS` when linking).

This macro is intended to be used in those situations when it is necessary to mix, e.g., C++ and Fortran source code in a single program or shared library (see Mixing Fortran 77 With C and C++ in *GNU Automake*).

For example, if object files from a C++ and Fortran compiler must be linked together, then the C++ compiler/linker must be used for linking (since special C++-ish things need to happen at link time like calling global constructors, instantiating templates, enabling exception support, etc.).

However, the Fortran intrinsic and runtime libraries must be linked in as well, but the C++ compiler/linker doesn’t know by default how to add these Fortran 77 libraries. Hence, this macro was created to determine these Fortran libraries.

The macros `AC_F77_DUMMY_MAIN` and `AC_FC_DUMMY_MAIN` or `AC_F77_MAIN` and `AC_FC_MAIN` are probably also necessary to link C/C++ with Fortran; see below. Further, it is highly recommended that you use `AC_CONFIG_HEADERS` (see Configuration Header Files) because the complex defines that the function wrapper macros create may not work with C/C++ compiler drivers.

These macros internally compute the flag needed to verbose linking output and cache it in `ac_cv_prog_f77_v` or `ac_cv_prog_fc_v` variables, respectively. The computed linker flags are cached in `ac_cv_f77_libs` or `ac_cv_fc_libs`, respectively.

**Macro: **AC_F77_DUMMY_MAIN***([*action-if-found*], [*action-if-not-found* = ‘AC_MSG_FAILURE’])* ¶**

**Macro: **AC_FC_DUMMY_MAIN***([*action-if-found*], [*action-if-not-found* = ‘AC_MSG_FAILURE’])* ¶**

With many compilers, the Fortran libraries detected by `AC_F77_LIBRARY_LDFLAGS` or `AC_FC_LIBRARY_LDFLAGS` provide their own `main` entry function that initializes things like Fortran I/O, and which then calls a user-provided entry function named (say) `MAIN__` to run the user’s program. The `AC_F77_DUMMY_MAIN` and `AC_FC_DUMMY_MAIN` or `AC_F77_MAIN` and `AC_FC_MAIN` macros figure out how to deal with this interaction.

When using Fortran for purely numerical functions (no I/O, etc.) often one prefers to provide one’s own `main` and skip the Fortran library initializations. In this case, however, one may still need to provide a dummy `MAIN__` routine in order to prevent linking errors on some systems. `AC_F77_DUMMY_MAIN` or `AC_FC_DUMMY_MAIN` detects whether any such routine is *required* for linking, and what its name is; the shell variable `F77_DUMMY_MAIN` or `FC_DUMMY_MAIN` holds this name, `unknown` when no solution was found, and `none` when no such dummy main is needed.

By default, *action-if-found* defines `F77_DUMMY_MAIN` or `FC_DUMMY_MAIN` to the name of this routine (e.g., `MAIN__`) *if* it is required. *action-if-not-found* defaults to exiting with an error.

In order to link with Fortran routines, the user’s C/C++ program should then include the following code to define the dummy main if it is needed:

```
#ifdef F77_DUMMY_MAIN
#  ifdef __cplusplus
     extern "C"
#  endif
   int F77_DUMMY_MAIN (void) { return 1; }
#endif
```

(Replace `F77` with `FC` for Fortran instead of Fortran 77.)

Note that this macro is called automatically from `AC_F77_WRAPPERS` or `AC_FC_WRAPPERS`; there is generally no need to call it explicitly unless one wants to change the default actions.

The result of this macro is cached in the `ac_cv_f77_dummy_main` or `ac_cv_fc_dummy_main` variable, respectively.

**Macro: **AC_F77_MAIN** ¶**

**Macro: **AC_FC_MAIN** ¶**

As discussed above, many Fortran libraries allow you to provide an entry point called (say) `MAIN__` instead of the usual `main`, which is then called by a `main` function in the Fortran libraries that initializes things like Fortran I/O. The `AC_F77_MAIN` and `AC_FC_MAIN` macros detect whether it is *possible* to utilize such an alternate main function, and defines `F77_MAIN` and `FC_MAIN` to the name of the function. (If no alternate main function name is found, `F77_MAIN` and `FC_MAIN` are simply defined to `main`.)

Thus, when calling Fortran routines from C that perform things like I/O, one should use this macro and declare the "main" function like so:

```
#ifdef __cplusplus
  extern "C"
#endif
int F77_MAIN (int argc, char *argv[]);
```

(Again, replace `F77` with `FC` for Fortran instead of Fortran 77.)

The result of this macro is cached in the `ac_cv_f77_main` or `ac_cv_fc_main` variable, respectively.

**Macro: **AC_F77_WRAPPERS** ¶**

**Macro: **AC_FC_WRAPPERS** ¶**

Defines C macros `F77_FUNC (name, NAME)`, `FC_FUNC (name, NAME)`, `F77_FUNC_(name, NAME)`, and `FC_FUNC_(name, NAME)` to properly mangle the names of C/C++ identifiers, and identifiers with underscores, respectively, so that they match the name-mangling scheme used by the Fortran compiler.

Fortran is case-insensitive, and in order to achieve this the Fortran compiler converts all identifiers into a canonical case and format. To call a Fortran subroutine from C or to write a C function that is callable from Fortran, the C program must explicitly use identifiers in the format expected by the Fortran compiler. In order to do this, one simply wraps all C identifiers in one of the macros provided by `AC_F77_WRAPPERS` or `AC_FC_WRAPPERS`. For example, suppose you have the following Fortran 77 subroutine:

```
      subroutine foobar (x, y)
      double precision x, y
      y = 3.14159 * x
      return
      end
```

You would then declare its prototype in C or C++ as:

```
#define FOOBAR_F77 F77_FUNC (foobar, FOOBAR)
#ifdef __cplusplus
extern "C"  /* prevent C++ name mangling */
#endif
void FOOBAR_F77 (double *x, double *y);
```

Note that we pass both the lowercase and uppercase versions of the function name to `F77_FUNC` so that it can select the right one. Note also that all parameters to Fortran 77 routines are passed as pointers (see Mixing Fortran 77 With C and C++ in *GNU Automake*).

(Replace `F77` with `FC` for Fortran instead of Fortran 77.)

Although Autoconf tries to be intelligent about detecting the name-mangling scheme of the Fortran compiler, there may be Fortran compilers that it doesn’t support yet. In this case, the above code generates a compile-time error, but some other behavior (e.g., disabling Fortran-related features) can be induced by checking whether `F77_FUNC` or `FC_FUNC` is defined.

Now, to call that routine from a C program, we would do something like:

```
{
    double x = 2.7183, y;
    FOOBAR_F77 (&x, &y);
}
```

If the Fortran identifier contains an underscore (e.g., `foo_bar`), you should use `F77_FUNC_` or `FC_FUNC_` instead of `F77_FUNC` or `FC_FUNC` (with the same arguments). This is because some Fortran compilers mangle names differently if they contain an underscore.

The name mangling scheme is encoded in the `ac_cv_f77_mangling` or `ac_cv_fc_mangling` cache variable, respectively, and also used for the `AC_F77_FUNC` and `AC_FC_FUNC` macros described below.

**Macro: **AC_F77_FUNC***(*name*, [*shellvar*])* ¶**

**Macro: **AC_FC_FUNC***(*name*, [*shellvar*])* ¶**

Given an identifier *name*, set the shell variable *shellvar* to hold the mangled version *name* according to the rules of the Fortran linker (see also `AC_F77_WRAPPERS` or `AC_FC_WRAPPERS`). *shellvar* is optional; if it is not supplied, the shell variable is simply *name*. The purpose of this macro is to give the caller a way to access the name-mangling information other than through the C preprocessor as above, for example, to call Fortran routines from some language other than C/C++.

**Macro: **AC_FC_SRCEXT***(*ext*, [*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

**Macro: **AC_FC_PP_SRCEXT***(*ext*, [*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

By default, the `FC` macros perform their tests using a .f extension for source-code files. Some compilers, however, only enable newer language features for appropriately named files, e.g., Fortran 90 features only for .f90 files, or preprocessing only with .F files or maybe other upper-case extensions. On the other hand, some other compilers expect all source files to end in .f and require special flags to support other file name extensions. The `AC_FC_SRCEXT` and `AC_FC_PP_SRCEXT` macros deal with these issues.

The `AC_FC_SRCEXT` macro tries to get the `FC` compiler to accept files ending with the extension .*ext* (i.e., *ext* does *not* contain the dot). If any special compiler flags are needed for this, it stores them in the output variable `FCFLAGS_*ext*`. This extension and these flags are then used for all subsequent `FC` tests (until `AC_FC_SRCEXT` or `AC_FC_PP_SRCEXT` is called another time).

For example, you would use `AC_FC_SRCEXT(f90)` to employ the .f90 extension in future tests, and it would set the `FCFLAGS_f90` output variable with any extra flags that are needed to compile such files.

Similarly, the `AC_FC_PP_SRCEXT` macro tries to get the `FC` compiler to preprocess and compile files with the extension .*ext*. When both `fpp` and `cpp` style preprocessing are provided, the former is preferred, as the latter may treat continuation lines, `//` tokens, and white space differently from what some Fortran dialects expect. Conversely, if you do not want files to be preprocessed, use only lower-case characters in the file name extension. Like with `AC_FC_SRCEXT(f90)`, any needed flags are stored in the `FCFLAGS_*ext*` variable.

The `FCFLAGS_*ext*` flags can *not* be simply absorbed into `FCFLAGS`, for two reasons based on the limitations of some compilers. First, only one `FCFLAGS_*ext*` can be used at a time, so files with different extensions must be compiled separately. Second, `FCFLAGS_*ext*` must appear *immediately* before the source-code file name when compiling. So, continuing the example above, you might compile a foo.f90 file in your makefile with the command:

```
foo.o: foo.f90
       $(FC) -c $(FCFLAGS) $(FCFLAGS_f90) '$(srcdir)/foo.f90'
```

If `AC_FC_SRCEXT` or `AC_FC_PP_SRCEXT` succeeds in compiling files with the *ext* extension, it calls *action-if-success* (defaults to nothing). If it fails, and cannot find a way to make the `FC` compiler accept such files, it calls *action-if-failure* (defaults to exiting with an error message).

The `AC_FC_SRCEXT` and `AC_FC_PP_SRCEXT` macros cache their results in `ac_cv_fc_srcext_*ext*` and `ac_cv_fc_pp_srcext_*ext*` variables, respectively.

**Macro: **AC_FC_PP_DEFINE***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Find a flag to specify defines for preprocessed Fortran. Not all Fortran compilers use -D. Substitute `FC_DEFINE` with the result and call *action-if-success* (defaults to nothing) if successful, and *action-if-failure* (defaults to failing with an error message) if not.

This macro calls `AC_FC_PP_SRCEXT([F])` in order to learn how to preprocess a conftest.F file, but restores a previously used Fortran source file extension afterwards again.

The result of this test is cached in the `ac_cv_fc_pp_define` variable.

**Macro: **AC_FC_FREEFORM***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Try to ensure that the Fortran compiler (`$FC`) allows free-format source code (as opposed to the older fixed-format style from Fortran 77). If necessary, it may add some additional flags to `FCFLAGS`.

This macro is most important if you are using the default .f extension, since many compilers interpret this extension as indicating fixed-format source unless an additional flag is supplied. If you specify a different extension with `AC_FC_SRCEXT`, such as .f90, then `AC_FC_FREEFORM` ordinarily succeeds without modifying `FCFLAGS`. For extensions which the compiler does not know about, the flag set by the `AC_FC_SRCEXT` macro might let the compiler assume Fortran 77 by default, however.

If `AC_FC_FREEFORM` succeeds in compiling free-form source, it calls *action-if-success* (defaults to nothing). If it fails, it calls *action-if-failure* (defaults to exiting with an error message).

The result of this test, or ‘none’ or ‘unknown’, is cached in the `ac_cv_fc_freeform` variable.

**Macro: **AC_FC_FIXEDFORM***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Try to ensure that the Fortran compiler (`$FC`) allows the old fixed-format source code (as opposed to free-format style). If necessary, it may add some additional flags to `FCFLAGS`.

This macro is needed for some compilers alias names like `xlf95` which assume free-form source code by default, and in case you want to use fixed-form source with an extension like .f90 which many compilers interpret as free-form by default. If you specify a different extension with `AC_FC_SRCEXT`, such as .f, then `AC_FC_FIXEDFORM` ordinarily succeeds without modifying `FCFLAGS`.

If `AC_FC_FIXEDFORM` succeeds in compiling fixed-form source, it calls *action-if-success* (defaults to nothing). If it fails, it calls *action-if-failure* (defaults to exiting with an error message).

The result of this test, or ‘none’ or ‘unknown’, is cached in the `ac_cv_fc_fixedform` variable.

**Macro: **AC_FC_LINE_LENGTH***([*length*], [*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Try to ensure that the Fortran compiler (`$FC`) accepts long source code lines. The *length* argument may be given as 80, 132, or unlimited, and defaults to 132. Note that line lengths above 250 columns are not portable, and some compilers do not accept more than 132 columns at least for fixed format source. If necessary, it may add some additional flags to `FCFLAGS`.

If `AC_FC_LINE_LENGTH` succeeds in compiling fixed-form source, it calls *action-if-success* (defaults to nothing). If it fails, it calls *action-if-failure* (defaults to exiting with an error message).

The result of this test, or ‘none’ or ‘unknown’, is cached in the `ac_cv_fc_line_length` variable.

**Macro: **AC_FC_CHECK_BOUNDS***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

The `AC_FC_CHECK_BOUNDS` macro tries to enable array bounds checking in the Fortran compiler. If successful, the *action-if-success* is called and any needed flags are added to `FCFLAGS`. Otherwise, *action-if-failure* is called, which defaults to failing with an error message. The macro currently requires Fortran 90 or a newer dialect.

The result of the macro is cached in the `ac_cv_fc_check_bounds` variable.

**Macro: **AC_F77_IMPLICIT_NONE***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

**Macro: **AC_FC_IMPLICIT_NONE***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Try to disallow implicit declarations in the Fortran compiler. If successful, *action-if-success* is called and any needed flags are added to `FFLAGS` or `FCFLAGS`, respectively. Otherwise, *action-if-failure* is called, which defaults to failing with an error message.

The result of these macros are cached in the `ac_cv_f77_implicit_none` and `ac_cv_fc_implicit_none` variables, respectively.

**Macro: **AC_FC_MODULE_EXTENSION** ¶**

Find the Fortran 90 module file name extension. Most Fortran 90 compilers store module information in files separate from the object files. The module files are usually named after the name of the module rather than the source file name, with characters possibly turned to upper case, plus an extension, often .mod.

Not all compilers use module files at all, or by default. The Cray Fortran compiler requires -e m in order to store and search module information in .mod files rather than in object files. Likewise, the Fujitsu Fortran compilers uses the -Am option to indicate how module information is stored.

The `AC_FC_MODULE_EXTENSION` macro computes the module extension without the leading dot, and stores that in the `FC_MODEXT` variable. If the compiler does not produce module files, or the extension cannot be determined, `FC_MODEXT` is empty. Typically, the result of this macro may be used in cleanup `make` rules as follows:

```
clean-modules:
        -test -z "$(FC_MODEXT)" || rm -f *.$(FC_MODEXT)
```

The extension, or ‘unknown’, is cached in the `ac_cv_fc_module_ext` variable.

**Macro: **AC_FC_MODULE_FLAG***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Find the compiler flag to include Fortran 90 module information from another directory, and store that in the `FC_MODINC` variable. Call *action-if-success* (defaults to nothing) if successful, and set `FC_MODINC` to empty and call *action-if-failure* (defaults to exiting with an error message) if not.

Most Fortran 90 compilers provide a way to specify module directories. Some have separate flags for the directory to write module files to, and directories to search them in, whereas others only allow writing to the current directory or to the first directory specified in the include path. Further, with some compilers, the module search path and the preprocessor search path can only be modified with the same flag. Thus, for portability, write module files to the current directory only and list that as first directory in the search path.

There may be no whitespace between `FC_MODINC` and the following directory name, but `FC_MODINC` may contain trailing white space. For example, if you use Automake and would like to search ../lib for module files, you can use the following:

```
AM_FCFLAGS = $(FC_MODINC). $(FC_MODINC)../lib
```

Inside `configure` tests, you can use:

```
if test -n "$FC_MODINC"; then
  FCFLAGS="$FCFLAGS $FC_MODINC. $FC_MODINC../lib"
fi
```

The flag is cached in the `ac_cv_fc_module_flag` variable. The substituted value of `FC_MODINC` may refer to the `ac_empty` dummy placeholder empty variable, to avoid losing the significant trailing whitespace in a Makefile.

**Macro: **AC_FC_MODULE_OUTPUT_FLAG***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Find the compiler flag to write Fortran 90 module information to another directory, and store that in the `FC_MODOUT` variable. Call *action-if-success* (defaults to nothing) if successful, and set `FC_MODOUT` to empty and call *action-if-failure* (defaults to exiting with an error message) if not.

Not all Fortran 90 compilers write module files, and of those that do, not all allow writing to a directory other than the current one, nor do all have separate flags for writing and reading; see the description of `AC_FC_MODULE_FLAG` above. If you need to be able to write to another directory, for maximum portability use `FC_MODOUT` before any `FC_MODINC` and include both the current directory and the one you write to in the search path:

```
AM_FCFLAGS = $(FC_MODOUT)../mod $(FC_MODINC)../mod $(FC_MODINC). ...
```

The flag is cached in the `ac_cv_fc_module_output_flag` variable. The substituted value of `FC_MODOUT` may refer to the `ac_empty` dummy placeholder empty variable, to avoid losing the significant trailing whitespace in a Makefile.

**Macro: **AC_F77_CRAY_POINTERS***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

**Macro: **AC_FC_CRAY_POINTERS***([*action-if-success*], [*action-if-failure* = ‘AC_MSG_FAILURE’])* ¶**

Try to ensure that the Fortran compiler (`$F77` or `$FC`) accepts Cray pointers. If successful, the *action-if-success* is called and any needed flags are added to `FFLAGS` or `FCFLAGS`. Otherwise, *action-if-failure* is called, which defaults to failing with an error message.

Cray pointers are a non-standard extension supported by many Fortran compilers which allow an integer to be declared as C-like pointer to a target variable.

The result of this test, or ‘none’ or ‘unknown’, is cached in the `ac_cv_f77_cray_ptr` or `ac_cv_fc_cray_ptr` variable.

#### 5.10.9 Go Compiler Characteristics

Autoconf provides basic support for the Go programming language when using the `gccgo` compiler (there is currently no support for the `6g` and `8g` compilers).

**Macro: **AC_PROG_GO***([*compiler-search-list*])* ¶**

Find the Go compiler to use. Check whether the environment variable `GOC` is set; if so, then set output variable `GOC` to its value.

Otherwise, if the macro is invoked without an argument, then search for a Go compiler named `gccgo`. If it is not found, then as a last resort set `GOC` to `gccgo`.

This macro may be invoked with an optional first argument which, if specified, must be a blank-separated list of Go compilers to search for.

If output variable `GOFLAGS` was not already set, set it to -g -O2. If your package does not like this default, `GOFLAGS` may be set before `AC_PROG_GO`.

#### 5.10.10 Algol 68 Compiler

Autoconf provides basic support for the Algol 68 programming language when using the `ga68` compiler.

Note that the GCC Algol 68 front-end is not yet integrated in the main compiler, so it is developed and distributed off-tree. See https://gcc.gnu.org/wiki/Algol68FrontEnd. Additional information about the Algol 68 programming language, and how it is being evolved by the GNU Algol 68 Working Group can be found at https://algol68-lang.org.

**Macro: **AC_PROG_A68***([*compiler-search-list*])* ¶**

Find the Algol 68 compiler to use. Check whether the environment variable `A68` is set; if so, then set output variable `A68` to its value.

Otherwise, if the macro is invoked without an argument, then search for an Algol 68 compiler named `ga68`. If it is not found, then as a last resort set `A68` to `ga68`.

This macro may be invoked with an optional first argument which, if specified, must be a blank-separated list of Algol 68 compilers to search for.

If output variable `A68FLAGS` was not already set, set it to -g -O2. If your package does not like this default, `A68FLAGS` may be set before `AC_PROG_A68`.

### 5.11 System Services

The following macros check for operating system services or capabilities.

**Macro: **AC_PATH_X** ¶**

Try to locate the X Window System include files and libraries. If the user gave the command line options --x-includes=*dir* and --x-libraries=*dir*, use those directories.

If either or both were not given, get the missing values by running `xmkmf` (or an executable pointed to by the `XMKMF` environment variable) on a trivial Imakefile and examining the makefile that it produces. Setting `XMKMF` to ‘false’ disables this method.

If this method fails to find the X Window System, `configure` looks for the files in several directories where they often reside. If either method is successful, set the shell variables `x_includes` and `x_libraries` to their locations, unless they are in directories the compiler searches by default.

If both methods fail, or the user gave the command line option --without-x, set the shell variable `no_x` to ‘yes’; otherwise set it to the empty string.

**Macro: **AC_PATH_XTRA** ¶**

An enhanced version of `AC_PATH_X`. It adds the C compiler flags that X needs to output variable `X_CFLAGS`, and the X linker flags to `X_LIBS`. Define `X_DISPLAY_MISSING` if X is not available.

This macro also checks for special libraries that some systems need in order to compile X programs. It adds any that the system needs to output variable `X_EXTRA_LIBS`. And it checks for special X11R6 libraries that need to be linked with before -lX11, and adds any found to the output variable `X_PRE_LIBS`.

**Macro: **AC_SYS_INTERPRETER** ¶**

Check whether the system supports starting scripts with a line of the form ‘#!/bin/sh’ to select the interpreter to use for the script. After running this macro, shell code in configure.ac can check the shell variable `interpval`; it is set to ‘yes’ if the system supports ‘#!’, ‘no’ if not.

**Macro: **AC_SYS_LARGEFILE** ¶**

If the default `off_t` type is a 32-bit integer, and therefore cannot be used with files 2 GiB or larger, make a wider `off_t` available if the system supports it. Similarly, widen other types related to sizes of files and file systems if possible. These types may include `blkcnt_t`, `dev_t`, `ino_t`, `fsblkcnt_t`, `fsfilcnt_t`, and `rlim_t`.

Also, arrange for a `configure` option `--enable-year2038` to request widening the type `time_t` as needed to represent file wand other timestamps after mid-January 2038. This widening is possible only on 32-bit GNU/Linux x86 and ARM systems with glibc 2.34 or later. If year-2038 support is requested but `configure` fails to find a way to widen `time_t` and inspection of the system suggests that this feature is available somehow, `configure` will error out. If you want the default to be `--enable-year2038`, you can use `AC_SYS_YEAR2038` or `AC_SYS_YEAR2038_RECOMMENDED` instead of `AC_SYS_LARGEFILE`. In other words, older packages that have long used `AC_SYS_LARGEFILE` can have year-2038 support on 32-bit GNU/Linux x86 and ARM systems either by regenerating configure with current Autoconf and configuring with --enable-year2038, or by using `AC_SYS_YEAR2038` or `AC_SYS_YEAR2038_RECOMMENDED` and configuring without --disable-year2038. A future version of Autoconf might change the `AC_SYS_LARGEFILE` default to `--enable-year2038`; if and when that happens, `AC_SYS_LARGEFILE` and `AC_SYS_YEAR2038` will become equivalent. See AC_SYS_YEAR2038.

Set the shell variable `ac_have_largefile` to ‘yes’ or `no` depending on whether a wide `off_t` is available, regardless of whether arrangements were necessary. Similarly, set the shell variable `ac_have_year2038` to `yes` or `no` depending on whether a wide-enough `time_t` is available.

Define preprocessor macros if necessary to make types wider; for example, on GNU/Linux systems the macros `_FILE_OFFSET_BITS` and `_TIME_BITS` can be defined. Some of these macros work only if defined before the first system header is included; therefore, when using this macro in concert with `AC_CONFIG_HEADERS`, make sure that config.h is included before any system headers.

Large-file support can be disabled by configuring with the --disable-largefile option, and year-2038 support can be enabled and disabled via the --enable-year2038 and --disable-year2038 options. These options have no effect on systems where types are wide enough by default. Large-file support is required for year-2038 support: if you configure with --disable-largefile on a platform with 32-bit `time_t`, then year-2038 support is not available.

Disabling large-file or year-2038 support can have surprising effects, such as causing functions like `readdir` and `stat` to fail even on a small file because its inode number or timestamp is out of range.

Regardless of whether you use this macro, portable programs should not assume that any of the types listed above fit into a `long int`. For example, it is not portable to print an arbitrary `off_t` or `time_t` value `X` with `printf ("%ld", (long int) X)`.

The standard C library functions `fseek` and `ftell` do not use `off_t`. If you need to use either of these functions, you should use `AC_FUNC_FSEEKO` as well as `AC_SYS_LARGEFILE`, and then use their POSIX replacements `fseeko` and `ftello`. See AC_FUNC_FSEEKO.

When using `AC_SYS_LARGEFILE` in different packages that are linked together and that have interfaces that depend on the width of `off_t`, `time_t` or related types, the simplest thing is to configure all components the same way. For example, if an application uses `AC_SYS_LARGEFILE` and is configured with --enable-year2038, libraries it links to with an `off_t`- or `time_t`-dependent interface should be configured equivalently. Alternatively, you can modify libraries to support both 32- and 64-bit interfaces though this is more work and few libraries other than the C library itself are modified in this way.

Applications and libraries should be configured compatibly. If `off_t`, `time_t` or related types appear in a library’s public interface, enabling or disabling the library’s large-file or year-2038 support may break binary compatibility with applications or with other libraries. Similarly, if an application links to a such a library, enabling or disabling the application’s large-file support may break binary compatibility with that library.

**Macro: **AC_SYS_LONG_FILE_NAMES** ¶**

If the system supports file names longer than 14 characters, define `HAVE_LONG_FILE_NAMES`.

**Macro: **AC_SYS_POSIX_TERMIOS** ¶**

Check to see if the POSIX termios headers and functions are available on the system. If so, set the shell variable `ac_cv_sys_posix_termios` to ‘yes’. If not, set the variable to ‘no’.

**Macro: **AC_SYS_YEAR2038** ¶**

This is like `AC_SYS_LARGEFILE` except it defaults to enabling instead of disabling year-2038 support. Year-2038 support for applications and libraries should be configured compatibly. See AC_SYS_LARGEFILE.

**Macro: **AC_SYS_YEAR2038_RECOMMENDED** ¶**

This macro has the same effect as `AC_SYS_YEAR2038`, but also declares that the program being configured should support timestamps after mid-January 2038. If a large `time_t` is unavailable, `configure` will error out unless the --disable-year2038 option is specified.

Year-2038 support for applications and libraries should be configured compatibly. See AC_SYS_YEAR2038.

### 5.12 C and POSIX Variants

The following macro makes it possible to use C language and library extensions defined by the C standards committee, features of POSIX that are extensions to C, and platform extensions not defined by POSIX.

**Macro: **AC_USE_SYSTEM_EXTENSIONS** ¶**

If possible, enable extensions to C or POSIX on hosts that normally disable the extensions, typically due to standards-conformance namespace issues. This should be called before any macros that run the C compiler. Also, when using this macro in concert with `AC_CONFIG_HEADERS`, be sure that config.h is included before any system header.

Define the following preprocessor macros unconditionally:

**`_ALL_SOURCE` ¶**

Enable extensions on AIX and z/OS.

**`_COSMO_SOURCE` ¶**

Enable extensions on Cosmopolitan Libc.

**`_DARWIN_C_SOURCE` ¶**

Enable extensions on macOS.

**`_GNU_SOURCE` ¶**

Enable extensions on GNU systems.

**`_NETBSD_SOURCE` ¶**

Enable general extensions on NetBSD. Enable NetBSD compatibility extensions on Minix.

**`_OPENBSD_SOURCE` ¶**

Enable OpenBSD compatibility extensions on NetBSD. Oddly enough, this does nothing on OpenBSD.

**`_POSIX_PTHREAD_SEMANTICS` ¶**

Enable POSIX-compatible threading on Solaris.

**`__STDC_WANT_IEC_60559_ATTRIBS_EXT__` ¶**

Enable extensions specified by ISO/IEC TS 18661-5:2014.

**`__STDC_WANT_IEC_60559_BFP_EXT__` ¶**

Enable extensions specified by ISO/IEC TS 18661-1:2014.

**`__STDC_WANT_IEC_60559_DFP_EXT__` ¶**

Enable extensions specified by ISO/IEC TS 18661-2:2015.

**`__STDC_WANT_IEC_60559_EXT__` ¶**

Enable extensions specified by C23 Annex F.

**`__STDC_WANT_IEC_60559_FUNCS_EXT__` ¶**

Enable extensions specified by ISO/IEC TS 18661-4:2015.

**`__STDC_WANT_IEC_60559_TYPES_EXT__` ¶**

Enable extensions specified by C23 Annex H and by ISO/IEC TS 18661-3:2015.

**`__STDC_WANT_LIB_EXT2__` ¶**

Enable extensions specified by ISO/IEC TR 24731-2:2010.

**`__STDC_WANT_MATH_SPEC_FUNCS__` ¶**

Enable extensions specified by ISO/IEC 24747:2009.

**`_TANDEM_SOURCE` ¶**

Enable extensions on HP NonStop systems.

The following preprocessor macros are defined only when necessary; they enable access to extensions on some operating systems but *disable* extensions on other operating systems.

**`__EXTENSIONS__` ¶**

Enable general extensions on Solaris. This macro is defined only if the headers included by `AC_INCLUDES_DEFAULT` (see Default Includes) work correctly with it defined.

**`_MINIX` ¶**

**`_POSIX_SOURCE`**

**`_POSIX_1_SOURCE`**

Defined only on MINIX. `_POSIX_SOURCE` and `_POSIX_1_SOURCE` are needed to enable a number of POSIX features on this OS. `_MINIX` does not affect the system headers’ behavior; future versions of Autoconf may stop defining it. Programs that need to recognize Minix should use `AC_CANONICAL_HOST`.

**`_XOPEN_SOURCE` ¶**

Defined (with value 500) only if needed to make wchar.h declare `mbstate_t`. This is known to be necessary on some versions of HP-UX.

The C preprocessor macro `__STDC_WANT_DEC_FP__` is not defined. ISO/IEC TR 24732:2009 was superseded by ISO/IEC TS 18661-2:2015.

The C preprocessor macro `__STDC_WANT_LIB_EXT1__` is not defined, as the C standard’s Annex K is problematic. See: O’Donell C, Sebor M. Field Experience With Annex K—Bounds Checking Interfaces.

The Autoconf macro `AC_USE_SYSTEM_EXTENSIONS` was introduced in Autoconf 2.60.

### 5.13 Erlang Libraries

The following macros check for an installation of Erlang/OTP, and for the presence of certain Erlang libraries. All those macros require the configuration of an Erlang interpreter and an Erlang compiler (see Erlang Compiler and Interpreter Characteristics).

**Macro: **AC_ERLANG_SUBST_ERTS_VER** ¶**

Set the output variable `ERLANG_ERTS_VER` to the version of the Erlang runtime system (as returned by Erlang’s `erlang:system_info(version)` function). The result of this test is cached if caching is enabled when running `configure`. The `ERLANG_ERTS_VER` variable is not intended to be used for testing for features of specific ERTS versions, but to be used for substituting the ERTS version in Erlang/OTP release resource files (`.rel` files), as shown below.

**Macro: **AC_ERLANG_SUBST_ROOT_DIR** ¶**

Set the output variable `ERLANG_ROOT_DIR` to the path to the base directory in which Erlang/OTP is installed (as returned by Erlang’s `code:root_dir/0` function). The result of this test is cached if caching is enabled when running `configure`.

**Macro: **AC_ERLANG_SUBST_LIB_DIR** ¶**

Set the output variable `ERLANG_LIB_DIR` to the path of the library directory of Erlang/OTP (as returned by Erlang’s `code:lib_dir/0` function), which subdirectories each contain an installed Erlang/OTP library. The result of this test is cached if caching is enabled when running `configure`.

**Macro: **AC_ERLANG_CHECK_LIB***(*library*, [*action-if-found*], [*action-if-not-found*])* ¶**

Test whether the Erlang/OTP library *library* is installed by calling Erlang’s `code:lib_dir/1` function. The result of this test is cached if caching is enabled when running `configure`. *action-if-found* is a list of shell commands to run if the library is installed; *action-if-not-found* is a list of shell commands to run if it is not. Additionally, if the library is installed, the output variable ‘ERLANG_LIB_DIR_*library*’ is set to the path to the library installation directory, and the output variable ‘ERLANG_LIB_VER_*library*’ is set to the version number that is part of the subdirectory name, if it is in the standard form (`*library*-*version*`). If the directory name does not have a version part, ‘ERLANG_LIB_VER_*library*’ is set to the empty string. If the library is not installed, ‘ERLANG_LIB_DIR_*library*’ and ‘ERLANG_LIB_VER_*library*’ are set to `"not found"`. For example, to check if library `stdlib` is installed:

```
AC_ERLANG_CHECK_LIB([stdlib],
  [AS_ECHO(["stdlib version \"$ERLANG_LIB_VER_stdlib\""])
   AS_ECHO(["is installed in \"$ERLANG_LIB_DIR_stdlib\""])],
  [AC_MSG_ERROR([stdlib was not found!])])
```

The ‘ERLANG_LIB_VER_*library*’ variables (set by `AC_ERLANG_CHECK_LIB`) and the `ERLANG_ERTS_VER` variable (set by `AC_ERLANG_SUBST_ERTS_VER`) are not intended to be used for testing for features of specific versions of libraries or of the Erlang runtime system. Those variables are intended to be substituted in Erlang release resource files (`.rel` files). For instance, to generate a example.rel file for an application depending on the `stdlib` library, configure.ac could contain:

```
AC_ERLANG_SUBST_ERTS_VER
AC_ERLANG_CHECK_LIB([stdlib],
  [],
  [AC_MSG_ERROR([stdlib was not found!])])
AC_CONFIG_FILES([example.rel])
```

The example.rel.in file used to generate example.rel should contain:

```
{release,
    {"@PACKAGE@", "@VERSION@"},
    {erts, "@ERLANG_ERTS_VER@"},
    [{stdlib, "@ERLANG_LIB_VER_stdlib@"},
     {@PACKAGE@, "@VERSION@"}]}.
```

In addition to the above macros, which test installed Erlang libraries, the following macros determine the paths to the directories into which newly built Erlang libraries are to be installed:

**Macro: **AC_ERLANG_SUBST_INSTALL_LIB_DIR** ¶**

Set the `ERLANG_INSTALL_LIB_DIR` output variable to the directory into which every built Erlang library should be installed in a separate subdirectory. If this variable is not set in the environment when `configure` runs, its default value is `${libdir}/erlang/lib`.

**Macro: **AC_ERLANG_SUBST_INSTALL_LIB_SUBDIR***(*library*, *version*)* ¶**

Set the ‘ERLANG_INSTALL_LIB_DIR_*library*’ output variable to the directory into which the built Erlang library *library* version *version* should be installed. If this variable is not set in the environment when `configure` runs, its default value is ‘$ERLANG_INSTALL_LIB_DIR/*library*-*version*’, the value of the `ERLANG_INSTALL_LIB_DIR` variable being set by the `AC_ERLANG_SUBST_INSTALL_LIB_DIR` macro.

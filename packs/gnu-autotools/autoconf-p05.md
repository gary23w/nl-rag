---
title: "Autoconf (part 5/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 5/26
---

# Autoconf

This macro is obsolescent, as time.h defines `struct tm` in current systems. New programs need not use this macro.

**Macro: **AC_STRUCT_TIMEZONE** ¶**

Figure out how to get the current timezone. If `struct tm` has a `tm_zone` member, define `HAVE_STRUCT_TM_TM_ZONE` (and the obsoleted `HAVE_TM_ZONE`). Otherwise, if the external array `tzname` is found, define `HAVE_TZNAME`; if it is declared, define `HAVE_DECL_TZNAME`.

#### 5.8.2 Generic Structure Checks

These macros are used to find structure members not covered by the “particular” test macros.

**Macro: **AC_CHECK_MEMBER***(*aggregate*.*member*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

Check whether *member* is a member of the aggregate *aggregate*. If no *includes* are specified, the default includes are used (see Default Includes).

```
AC_CHECK_MEMBER([struct passwd.pw_gecos], [],
                [AC_MSG_ERROR([we need 'passwd.pw_gecos'])],
                [[#include <pwd.h>]])
```

You can use this macro for submembers:

```
AC_CHECK_MEMBER(struct top.middle.bot)
```

This macro caches its result in the `ac_cv_member_*aggregate*_*member*` variable, with characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_MEMBERS***(*members*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

Check for the existence of each ‘*aggregate*.*member*’ of *members* using the previous macro. When *member* belongs to *aggregate*, define `HAVE_*aggregate*_*member*` (in all capitals, with spaces and dots replaced by underscores). If *action-if-found* is given, it is executed for each of the found members. If *action-if-not-found* is given, it is executed for each of the members that could not be found.

*includes* is a series of include directives, defaulting to `AC_INCLUDES_DEFAULT` (see Default Includes), which are used prior to the members under test.

This macro uses M4 lists:

```
AC_CHECK_MEMBERS([struct stat.st_rdev, struct stat.st_blksize])
```

### 5.9 Types

The following macros check for C types, either builtin or typedefs. If there is no macro specifically defined to check for a type you need, and you don’t need to check for any special properties of it, then you can use a general type-check macro.

#### 5.9.1 Particular Type Checks

These macros check for particular C types in sys/types.h, stdlib.h, stdint.h, inttypes.h and others, if they exist.

The Gnulib `stdint` module is an alternate way to define many of these symbols; it is useful if you prefer your code to assume a C99-or-better environment. See Gnulib.

**Macro: **AC_TYPE_GETGROUPS** ¶**

Define `GETGROUPS_T` to be whichever of `gid_t` or `int` is the base type of the array argument to `getgroups`.

This macro caches the base type in the `ac_cv_type_getgroups` variable.

**Macro: **AC_TYPE_INT8_T** ¶**

If stdint.h or inttypes.h does not define the type `int8_t`, define `int8_t` to a signed integer type that is exactly 8 bits wide and that uses two’s complement representation, if such a type exists. If you are worried about porting to hosts that lack such a type, you can use the results of this macro as follows:

```
#if HAVE_STDINT_H
# include <stdint.h>
#endif
#if defined INT8_MAX || defined int8_t
 code using int8_t
#else
 complicated alternative using >8-bit 'signed char'
#endif
```

This macro caches the type in the `ac_cv_c_int8_t` variable.

**Macro: **AC_TYPE_INT16_T** ¶**

This is like `AC_TYPE_INT8_T`, except for 16-bit integers.

**Macro: **AC_TYPE_INT32_T** ¶**

This is like `AC_TYPE_INT8_T`, except for 32-bit integers.

**Macro: **AC_TYPE_INT64_T** ¶**

This is like `AC_TYPE_INT8_T`, except for 64-bit integers.

**Macro: **AC_TYPE_INTMAX_T** ¶**

If stdint.h or inttypes.h defines the type `intmax_t`, define `HAVE_INTMAX_T`. Otherwise, define `intmax_t` to the widest signed integer type.

**Macro: **AC_TYPE_INTPTR_T** ¶**

If stdint.h or inttypes.h defines the type `intptr_t`, define `HAVE_INTPTR_T`. Otherwise, define `intptr_t` to a signed integer type wide enough to hold a pointer, if such a type exists.

**Macro: **AC_TYPE_LONG_DOUBLE** ¶**

If the C compiler supports a working `long double` type, define `HAVE_LONG_DOUBLE`. The `long double` type might have the same range and precision as `double`.

This macro caches its result in the `ac_cv_type_long_double` variable.

This macro is obsolescent, as current C compilers support `long double`. New programs need not use this macro.

**Macro: **AC_TYPE_LONG_DOUBLE_WIDER** ¶**

If the C compiler supports a working `long double` type with more range or precision than the `double` type, define `HAVE_LONG_DOUBLE_WIDER`.

This macro caches its result in the `ac_cv_type_long_double_wider` variable.

**Macro: **AC_TYPE_LONG_LONG_INT** ¶**

If the C compiler supports a working `long long int` type, define `HAVE_LONG_LONG_INT`. However, this test does not test `long long int` values in preprocessor `#if` expressions, because too many compilers mishandle such expressions. See Preprocessor Arithmetic.

This macro caches its result in the `ac_cv_type_long_long_int` variable.

**Macro: **AC_TYPE_MBSTATE_T** ¶**

Define `HAVE_MBSTATE_T` if `<wchar.h>` declares the `mbstate_t` type. Also, define `mbstate_t` to be a type if `<wchar.h>` does not declare it.

This macro caches its result in the `ac_cv_type_mbstate_t` variable.

**Macro: **AC_TYPE_MODE_T** ¶**

Define `mode_t` to a suitable type, if standard headers do not define it.

This macro caches its result in the `ac_cv_type_mode_t` variable.

**Macro: **AC_TYPE_OFF_T** ¶**

Define `off_t` to a suitable type, if standard headers do not define it.

This macro caches its result in the `ac_cv_type_off_t` variable.

**Macro: **AC_TYPE_PID_T** ¶**

Define `pid_t` to a suitable type, if standard headers do not define it.

This macro caches its result in the `ac_cv_type_pid_t` variable.

**Macro: **AC_TYPE_SIZE_T** ¶**

Define `size_t` to a suitable type, if standard headers do not define it.

This macro caches its result in the `ac_cv_type_size_t` variable.

**Macro: **AC_TYPE_SSIZE_T** ¶**

Define `ssize_t` to a suitable type, if standard headers do not define it.

This macro caches its result in the `ac_cv_type_ssize_t` variable.

**Macro: **AC_TYPE_UID_T** ¶**

Define `uid_t` and `gid_t` to suitable types, if standard headers do not define them.

This macro caches its result in the `ac_cv_type_uid_t` variable.

**Macro: **AC_TYPE_UINT8_T** ¶**

If stdint.h or inttypes.h does not define the type `uint8_t`, define `uint8_t` to an unsigned integer type that is exactly 8 bits wide, if such a type exists. This is like `AC_TYPE_INT8_T`, except for unsigned integers.

**Macro: **AC_TYPE_UINT16_T** ¶**

This is like `AC_TYPE_UINT8_T`, except for 16-bit integers.

**Macro: **AC_TYPE_UINT32_T** ¶**

This is like `AC_TYPE_UINT8_T`, except for 32-bit integers.

**Macro: **AC_TYPE_UINT64_T** ¶**

This is like `AC_TYPE_UINT8_T`, except for 64-bit integers.

**Macro: **AC_TYPE_UINTMAX_T** ¶**

If stdint.h or inttypes.h defines the type `uintmax_t`, define `HAVE_UINTMAX_T`. Otherwise, define `uintmax_t` to the widest unsigned integer type.

**Macro: **AC_TYPE_UINTPTR_T** ¶**

If stdint.h or inttypes.h defines the type `uintptr_t`, define `HAVE_UINTPTR_T`. Otherwise, define `uintptr_t` to an unsigned integer type wide enough to hold a pointer, if such a type exists.

**Macro: **AC_TYPE_UNSIGNED_LONG_LONG_INT** ¶**

If the C compiler supports a working `unsigned long long int` type, define `HAVE_UNSIGNED_LONG_LONG_INT`. However, this test does not test `unsigned long long int` values in preprocessor `#if` expressions, because too many compilers mishandle such expressions. See Preprocessor Arithmetic.

This macro caches its result in the `ac_cv_type_unsigned_long_long_int` variable.

#### 5.9.2 Generic Type Checks

These macros are used to check for types not covered by the “particular” test macros.

**Macro: **AC_CHECK_TYPE***(*type*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

Check whether *type* is defined. It may be a compiler builtin type or defined by the *includes*. *includes* is a series of include directives, defaulting to `AC_INCLUDES_DEFAULT` (see Default Includes), which are used prior to the type under test.

In C, *type* must be a type-name, so that the expression ‘sizeof (*type*)’ is valid (but ‘sizeof ((*type*))’ is not). The same test is applied when compiling for C++, which means that in C++ *type* should be a type-id and should not be an anonymous ‘struct’ or ‘union’.

This macro caches its result in the `ac_cv_type_*type*` variable, with ‘*’ mapped to ‘p’ and other characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_TYPES***(*types*, [*action-if-found*], [*action-if-not-found*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

For each *type* of the *types* that is defined, define `HAVE_*type*` (in all capitals). Each *type* must follow the rules of `AC_CHECK_TYPE`. If no *includes* are specified, the default includes are used (see Default Includes). If *action-if-found* is given, it is additional shell code to execute when one of the types is found. If *action-if-not-found* is given, it is executed when one of the types is not found.

This macro uses M4 lists:

```
AC_CHECK_TYPES([ptrdiff_t])
AC_CHECK_TYPES([unsigned long long int, uintmax_t])
AC_CHECK_TYPES([float_t], [], [], [[#include <math.h>]])
```

Autoconf, up to 2.13, used to provide to another version of `AC_CHECK_TYPE`, broken by design. In order to keep backward compatibility, a simple heuristic, quite safe but not totally, is implemented. In case of doubt, read the documentation of the former `AC_CHECK_TYPE`, see Obsolete Macros.

### 5.10 Compilers and Preprocessors

All the tests for compilers (`AC_PROG_CC`, `AC_PROG_CXX`, `AC_PROG_F77`) define the output variable `EXEEXT` based on the output of the compiler, typically to the empty string if POSIX and ‘.exe’ if a DOS variant.

They also define the output variable `OBJEXT` based on the output of the compiler, after .c files have been excluded, typically to ‘o’ if POSIX, ‘obj’ if a DOS variant.

If the compiler being used does not produce executables, the tests fail. If the executables can’t be run, and cross-compilation is not enabled, they fail too. See Manual Configuration, for more on support for cross compiling.

#### 5.10.1 Specific Compiler Characteristics

Some compilers exhibit different behaviors.

**Static/Dynamic Expressions**

Autoconf relies on a trick to extract one bit of information from the C compiler: using negative array sizes. For instance the following excerpt of a C source demonstrates how to test whether ‘int’ objects are 4 bytes wide:

```
static int test_array[sizeof (int) == 4 ? 1 : -1];
```

To our knowledge, there is a single compiler that does not support this trick: the HP C compilers (the real ones, not only the “bundled”) on HP-UX 11.00. They incorrectly reject the above program with the diagnostic “Variable-length arrays cannot have static storage.” This bug comes from HP compilers’ mishandling of `sizeof (int)`, not from the `? 1 : -1`, and Autoconf works around this problem by casting `sizeof (int)` to `long int` before comparing it.

#### 5.10.2 Generic Compiler Characteristics

**Macro: **AC_CHECK_SIZEOF***(*type-or-expr*, [*unused*], [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

Define `SIZEOF_*type-or-expr*` (see Standard Symbols) to be the size in bytes of *type-or-expr*, which may be either a type or an expression returning a value that has a size. If the expression ‘sizeof (*type-or-expr*)’ is invalid, the result is 0. *includes* is a series of include directives, defaulting to `AC_INCLUDES_DEFAULT` (see Default Includes), which are used prior to the expression under test.

This macro now works even when cross-compiling. The *unused* argument was used when cross-compiling.

For example, the call

```
AC_CHECK_SIZEOF([int *])
```

defines `SIZEOF_INT_P` to be 8 on x86-64 systems.

This macro caches its result in the `ac_cv_sizeof_*type-or-expr*` variable, with ‘*’ mapped to ‘p’ and other characters not suitable for a variable name mapped to underscores.

**Macro: **AC_CHECK_ALIGNOF***(*type*, [*includes* = ‘AC_INCLUDES_DEFAULT’])* ¶**

Define `ALIGNOF_*type*` (see Standard Symbols) to be the alignment in bytes of *type*. ‘*type* y;’ must be valid as a structure member declaration. If ‘type’ is unknown, the result is 0. If no *includes* are specified, the default includes are used (see Default Includes).

This macro caches its result in the `ac_cv_alignof_*type-or-expr*` variable, with ‘*’ mapped to ‘p’ and other characters not suitable for a variable name mapped to underscores.

**Macro: **AC_COMPUTE_INT***(*var*, *expression*, [*includes* = ‘AC_INCLUDES_DEFAULT’], [*action-if-fails*])* ¶**

Store into the shell variable *var* the value of the integer *expression*. The value should fit in an initializer in a C variable of type `signed long`. To support cross compilation, it should be possible to evaluate the expression at compile-time. If no *includes* are specified, the default includes are used (see Default Includes).

Execute *action-if-fails* if the value cannot be determined correctly.

**Macro: **AC_LANG_WERROR** ¶**

Normally Autoconf ignores warnings generated by the compiler, linker, and preprocessor. If this macro is used, warnings count as fatal errors for the current language. This macro is useful when the results of configuration are used where warnings are unacceptable; for instance, if parts of a program are built with the GCC -Werror option. If the whole program is built using -Werror it is often simpler to put -Werror in the compiler flags (`CFLAGS`, etc.).

**Macro: **AC_OPENMP** ¶**

OpenMP specifies extensions of C, C++, and Fortran that simplify optimization of shared memory parallelism, which is a common problem on multi-core CPUs.

If the current language is C, the macro `AC_OPENMP` sets the variable `OPENMP_CFLAGS` to the C compiler flags needed for supporting OpenMP. `OPENMP_CFLAGS` is set to empty if the compiler already supports OpenMP, if it has no way to activate OpenMP support, or if the user rejects OpenMP support by invoking ‘configure’ with the ‘--disable-openmp’ option.

`OPENMP_CFLAGS` needs to be used when compiling programs, when preprocessing program source, and when linking programs. Therefore you need to add `$(OPENMP_CFLAGS)` to the `CFLAGS` of C programs that use OpenMP. If you preprocess OpenMP-specific C code, you also need to add `$(OPENMP_CFLAGS)` to `CPPFLAGS`. The presence of OpenMP support is revealed at compile time by the preprocessor macro `_OPENMP`.

Linking a program with `OPENMP_CFLAGS` typically adds one more shared library to the program’s dependencies, so its use is recommended only on programs that actually require OpenMP.

If the current language is C++, `AC_OPENMP` sets the variable `OPENMP_CXXFLAGS`, suitably for the C++ compiler. The same remarks hold as for C.

If the current language is Fortran 77 or Fortran, `AC_OPENMP` sets the variable `OPENMP_FFLAGS` or `OPENMP_FCFLAGS`, respectively. Similar remarks as for C hold, except that `CPPFLAGS` is not used for Fortran, and no preprocessor macro signals OpenMP support.

For portability, it is best to avoid spaces between ‘#’ and ‘pragma omp’. That is, write ‘#pragma omp’, not ‘# pragma omp’. The Sun WorkShop 6.2 C compiler chokes on the latter.

This macro caches its result in the `ac_cv_prog_c_openmp`, `ac_cv_prog_cxx_openmp`, `ac_cv_prog_f77_openmp`, or `ac_cv_prog_fc_openmp` variable, depending on the current language.

**Caution:** Some of the compiler options that `AC_OPENMP` tests, mean “enable OpenMP” to one compiler, but “write output to a file named mp or penmp” to other compilers. We cannot guarantee that the implementation of `AC_OPENMP` will not overwrite an existing file with either of these names.

Therefore, as a defensive measure, a `configure` script that uses `AC_OPENMP` will issue an error and stop (before doing any of the operations that might overwrite these files) upon encountering either of these files in its working directory. `autoconf` will also issue an error if it finds either of these files in the same directory as a configure.ac that uses `AC_OPENMP`.

If you have files with either of these names at the top level of your source tree, and you need to use `AC_OPENMP`, we recommend you either change their names or move them into a subdirectory.

#### 5.10.3 C Compiler Characteristics

The following macros provide ways to find and exercise a C Compiler. There are a few constructs that ought to be avoided, but do not deserve being checked for, since they can easily be worked around.

**Don’t use lines containing solitary backslashes**

They tickle a bug in the HP-UX C compiler (checked on HP-UX 10.20, 11.00, and 11i). When given the following source:

```
#ifdef __STDC__
/\
* A comment with backslash-newlines in it.  %{ %} *\
\
/
char str[] = "\\
" A string with backslash-newlines in it %{ %} \\
"";
char apostrophe = '\\
\
'\
';
#endif
```

the compiler incorrectly fails with the diagnostics “Non-terminating comment at end of file” and “Missing ‘#endif’ at end of file.” Removing the lines with solitary backslashes solves the problem.

**Don’t compile several files at once if output matters to you**

Some compilers, such as HP’s, report names of files being compiled when given more than one file operand. For instance:

```
$ cc a.c b.c
a.c:
b.c:
```

This can cause problems if you observe the output of the compiler to detect failures. Invoking ‘cc -c a.c && cc -c b.c && cc -o c a.o b.o’ solves the issue.

**Don’t rely on correct `#line` support**

On Solaris, `c89` (at least through Oracle Developer Studio 12.6) diagnoses `#line` directives whose line numbers are greater than 32767. Nothing in POSIX makes this invalid. That is why Autoconf stopped issuing `#line` directives.

**Macro: **AC_PROG_CC***([*compiler-search-list*])* ¶**

Determine a C compiler to use.

If the environment variable `CC` is set, its value will be taken as the name of the C compiler to use. Otherwise, search for a C compiler under a series of likely names, trying `gcc` and `cc` first. Regardless, the output variable `CC` is set to the chosen compiler.

If the optional first argument to the macro is used, it must be a whitespace-separated list of potential names for a C compiler, which overrides the built-in list.

If no C compiler can be found, `configure` will error out.

If the selected C compiler is found to be GNU C (regardless of its name), the shell variable `GCC` will be set to ‘yes’. If the shell variable `CFLAGS` was not already set, it is set to -g -O2 for the GNU C compiler (-O2 on systems where GCC does not accept -g), or -g for other compilers. `CFLAGS` is then made an output variable. You can override the default for `CFLAGS` by inserting a shell default assignment between `AC_INIT` and `AC_PROG_CC`:

```
: ${CFLAGS="options"}
```

where *options* are the appropriate set of options to use by default. (It is important to use this construct rather than a normal assignment, so that `CFLAGS` can still be overridden by the person building the package. See Preset Output Variables.)

If necessary, options are added to `CC` to enable support for ISO Standard C features with extensions, preferring the newest edition of the C standard for which detection is supported. Currently the newest edition Autoconf knows how to detect support for is C23. After calling this macro you can check whether the C compiler has been set to accept standard C by inspecting the shell variable `ac_prog_cc_stdc`. Its value is ‘c23’, ‘c11’, ‘c99’, or ‘c89’, respectively, if the C compiler has been set to use the 2023, 2011, 1999, or 1990 edition of the C standard, and ‘no’ if the compiler does not support compiling standard C at all. (There is no special value for the 2017 edition of the C standard, as it is a minor revision that does not introduce new language features.)

The tests for standard conformance are not comprehensive. They test the value of `__STDC_VERSION__`, and a representative sample of the language features added in each version of the C standard. They do not examine `__STDC__` because some compilers by default leave it undefined. They do not test for variable-length arrays, a C99 feature that was made optional in C11; if you need to use this feature when available, use `AC_C_VARARRAYS`. They do not test the C standard library, because the C compiler might be generating code for a “freestanding environment” (in which most of the standard library is optional). If you need to know whether a particular C standard header exists, use `AC_CHECK_HEADER`.

None of the options that may be added to `CC` by this macro enable *strict* conformance to the C standard. In particular, system-specific extensions are not disabled. (For example, for GNU C, the -std=gnu*nn* options may be used, but not the -std=c*nn* options.)

Many Autoconf macros use a compiler, and thus call ‘AC_REQUIRE([AC_PROG_CC])’ to ensure that the compiler has been determined before the body of the outermost `AC_DEFUN` macro. Although `AC_PROG_CC` is safe to directly expand multiple times, it performs certain checks (such as the proper value of `EXEEXT`) only on the first invocation. Therefore, care must be used when invoking this macro from within another macro rather than at the top level (see Expanded Before Required).

**Macro: **AC_PROG_CC_C_O** ¶**

If the C compiler does not accept the -c and -o options simultaneously, define `NO_MINUS_C_MINUS_O`. This macro actually tests both the compiler found by `AC_PROG_CC`, and, if different, the first `cc` in the path. The test fails if one fails. This macro was created for GNU Make to choose the default C compilation rule.

For the compiler *compiler*, this macro caches its result in the `ac_cv_prog_cc_*compiler*_c_o` variable.

**Macro: **AC_PROG_CPP** ¶**

Set output variable `CPP` to a command that runs the C preprocessor. If ‘$CC -E’ doesn’t work, tries `cpp` and /lib/cpp, in that order.

It is only portable to run `CPP` on files with a .c extension.

Some preprocessors don’t indicate missing include files by the error status. For such preprocessors an internal variable is set that causes other macros to check the standard error from the preprocessor and consider the test failed if any warnings have been reported. For most preprocessors, though, warnings do not cause include-file tests to fail unless `AC_PROG_CPP_WERROR` is also specified.

**Macro: **AC_PROG_CPP_WERROR** ¶**

This acts like `AC_PROG_CPP`, except it treats warnings from the preprocessor as errors even if the preprocessor exit status indicates success. This is useful for avoiding headers that generate mandatory warnings, such as deprecation notices.

The following macros check for C compiler or machine architecture features. To check for characteristics not listed here, use `AC_COMPILE_IFELSE` (see Running the Compiler) or `AC_RUN_IFELSE` (see Checking Runtime Behavior).

**Macro: **AC_C_BACKSLASH_A** ¶**

Define ‘HAVE_C_BACKSLASH_A’ to 1 if the C compiler understands ‘\a’.

This macro is obsolescent, as current C compilers understand ‘\a’. New programs need not use this macro.

**Macro: **AC_C_BIGENDIAN***([*action-if-true*], [*action-if-false*], [*action-if-unknown*], [*action-if-universal*])* ¶**

If words are stored with the most significant byte first (like Motorola and SPARC CPUs), execute *action-if-true*. If words are stored with the least significant byte first (like Intel and VAX CPUs), execute *action-if-false*.

This macro runs a test-case if endianness cannot be determined from the system header files. When cross-compiling, the test-case is not run but grep’ed for some magic values. *action-if-unknown* is executed if the latter case fails to determine the byte sex of the host system.

In some cases a single run of a compiler can generate code for multiple architectures. This can happen, for example, when generating Mac OS X universal binary files, which work on both PowerPC and Intel architectures. In this case, the different variants might be for architectures with differing endianness. If `configure` detects this, it executes *action-if-universal* instead of *action-if-unknown*.

The default for *action-if-true* is to define ‘WORDS_BIGENDIAN’. The default for *action-if-false* is to do nothing. The default for *action-if-unknown* is to abort configure and tell the installer how to bypass this test. And finally, the default for *action-if-universal* is to ensure that ‘WORDS_BIGENDIAN’ is defined if and only if a universal build is detected and the current code is big-endian; this default works only if `autoheader` is used (see Using `autoheader` to Create config.h.in).

If you use this macro without specifying *action-if-universal*, you should also use `AC_CONFIG_HEADERS`; otherwise ‘WORDS_BIGENDIAN’ may be set incorrectly for Mac OS X universal binary files.

**Macro: **AC_C_CONST** ¶**

If the C compiler does not fully support the `const` keyword, define `const` to be empty. Some C compilers that do not define `__STDC__` do support `const`; some compilers that define `__STDC__` do not completely support `const`. Programs can simply use `const` as if every C compiler supported it; for those that don’t, the makefile or configuration header file defines it as empty.

Occasionally installers use a C++ compiler to compile C code, typically because they lack a C compiler. This causes problems with `const`, because C and C++ treat `const` differently. For example:

```
const int foo;
```

is valid in C but not in C++. These differences unfortunately cannot be papered over by defining `const` to be empty.

If `autoconf` detects this situation, it leaves `const` alone, as this generally yields better results in practice. However, using a C++ compiler to compile C code is not recommended or supported, and installers who run into trouble in this area should get a C compiler like GCC to compile their C code.

This macro caches its result in the `ac_cv_c_const` variable.

This macro is obsolescent, as current C compilers support `const`. New programs need not use this macro.

**Macro: **AC_C__GENERIC** ¶**

If the C compiler supports C11-style generic selection using the `_Generic` keyword, define `HAVE_C__GENERIC`.

**Macro: **AC_C_RESTRICT** ¶**

If the C compiler recognizes a variant spelling for the `restrict` keyword (`__restrict`, `__restrict__`, or `_Restrict`), then define `restrict` to that; this is more likely to do the right thing with compilers that support language variants where plain `restrict` is not a keyword. Otherwise, if the C compiler recognizes the `restrict` keyword, don’t do anything. Otherwise, define `restrict` to be empty. Thus, programs may simply use `restrict` as if every C compiler supported it; for those that do not, the makefile or configuration header defines it away.

Although support in C++ for the `restrict` keyword is not required, several C++ compilers do accept the keyword. This macro works for them, too.

This macro caches ‘no’ in the `ac_cv_c_restrict` variable if `restrict` is not supported, and a supported spelling otherwise.

**Macro: **AC_C_VOLATILE** ¶**

If the C compiler does not understand the keyword `volatile`, define `volatile` to be empty. Programs can simply use `volatile` as if every C compiler supported it; for those that do not, the makefile or configuration header defines it as empty.

If the correctness of your program depends on the semantics of `volatile`, simply defining it to be empty does, in a sense, break your code. However, given that the compiler does not support `volatile`, you are at its mercy anyway. At least your program compiles, when it wouldn’t before. See Volatile Objects, for more about `volatile`.

This macro is obsolescent, as current C compilers support `volatile`. New programs need not use this macro.

**Macro: **AC_C_INLINE** ¶**

If the C compiler supports the keyword `inline`, do nothing. Otherwise define `inline` to `__inline__` or `__inline` if it accepts one of those, otherwise define `inline` to be empty.

**Macro: **AC_C_CHAR_UNSIGNED** ¶**

If the C type `char` is unsigned, define `__CHAR_UNSIGNED__`, unless the C compiler predefines it.

These days, using this macro is not necessary. The same information can be determined by this portable alternative, thus avoiding the use of preprocessor macros in the namespace reserved for the implementation.

```
#include <limits.h>
#if CHAR_MIN == 0
# define CHAR_UNSIGNED 1
#endif
```

**Macro: **AC_C_STRINGIZE** ¶**

If the C preprocessor supports the stringizing operator, define `HAVE_STRINGIZE`. The stringizing operator is ‘#’ and is found in macros such as this:

```
#define x(y) #y
```

This macro is obsolescent, as current C compilers support the stringizing operator. New programs need not use this macro.

**Macro: **AC_C_FLEXIBLE_ARRAY_MEMBER** ¶**

If the C compiler supports flexible array members, define `FLEXIBLE_ARRAY_MEMBER` to nothing; otherwise define it to 1. That way, a declaration like this:

```
struct s
  {
    size_t n_vals;
    double val[FLEXIBLE_ARRAY_MEMBER];
  };
```

will let applications use the “struct hack” even with compilers that do not support flexible array members. To allocate and use such an object, you can use code like this:

```
size_t i;
size_t n = compute_value_count ();
struct s *p =
   malloc (offsetof (struct s, val)
           + n * sizeof (double));
p->n_vals = n;
for (i = 0; i < n; i++)
  p->val[i] = compute_value (i);
```

**Macro: **AC_C_VARARRAYS** ¶**

If the C compiler does not support variable-length arrays, define the macro `__STDC_NO_VLA__` to be 1 if it is not already defined. A variable-length array is an array of automatic storage duration whose length is determined at run time, when the array is declared. For backward compatibility this macro also defines `HAVE_C_VARARRAYS` if the C compiler supports variable-length arrays, but this usage is obsolescent and new programs should use `__STDC_NO_VLA__`.

**Macro: **AC_C_TYPEOF** ¶**

If the C compiler supports GNU C’s `typeof` syntax either directly or through a different spelling of the keyword (e.g., `__typeof__`), define `HAVE_TYPEOF`. If the support is available only through a different spelling, define `typeof` to that spelling.

**Macro: **AC_C_PROTOTYPES** ¶**

If function prototypes are understood by the compiler (as determined by `AC_PROG_CC`), define `PROTOTYPES` and `__PROTOTYPES`. Defining `__PROTOTYPES` is for the benefit of header files that cannot use macros that infringe on user name space.

This macro is obsolescent, as current C compilers support prototypes. New programs need not use this macro.

#### 5.10.4 C++ Compiler Characteristics

**Macro: **AC_PROG_CXX***([*compiler-search-list*])* ¶**

Determine a C++ compiler to use.

If either the environment variable `CXX` or the environment variable `CCC` is set, its value will be taken as the name of a C++ compiler. If both are set, `CXX` is preferred. If neither are set, search for a C++ compiler under a series of likely names, trying `g++` and `c++` first. Regardless, the output variable `CXX` is set to the chosen compiler.

If the optional first argument to the macro is used, it must be a whitespace-separated list of potential names for a C++ compiler, which overrides the built-in list.

If no C++ compiler can be found, as a last resort `CXX` is set to `g++` (and subsequent tests will probably fail).

If the selected C++ compiler is found to be GNU C++ (regardless of its name), the shell variable `GXX` will be set to ‘yes’. If the shell variable `CXXFLAGS` was not already set, it is set to -g -O2 for the GNU C++ compiler (-O2 on systems where G++ does not accept -g), or -g for other compilers. `CXXFLAGS` is then made an output variable. You can override the default for `CXXFLAGS` by inserting a shell default assignment between `AC_INIT` and `AC_PROG_CXX`:

```
: ${CXXFLAGS="options"}
```

where *options* are the appropriate set of options to use by default. (It is important to use this construct rather than a normal assignment, so that `CXXFLAGS` can still be overridden by the person building the package. See Preset Output Variables.)

**Macro: **AC_PROG_CXXCPP** ¶**

Set output variable `CXXCPP` to a command that runs the C++ preprocessor. If ‘$CXX -E’ doesn’t work, tries `cpp` and /lib/cpp, in that order. Because of this fallback, `CXXCPP` may or may not set C++-specific predefined macros (such as `__cplusplus`).

It is portable to run `CXXCPP` only on files with a .c, .C, .cc, or .cpp extension.

Some preprocessors don’t indicate missing include files by the error status. For such preprocessors an internal variable is set that causes other macros to check the standard error from the preprocessor and consider the test failed if any warnings have been reported. However, it is not known whether such broken preprocessors exist for C++.

**Macro: **AC_PROG_CXX_C_O** ¶**

Test whether the C++ compiler accepts the options -c and -o simultaneously, and define `CXX_NO_MINUS_C_MINUS_O`, if it does not.

#### 5.10.5 Objective C Compiler Characteristics

**Macro: **AC_PROG_OBJC***([*compiler-search-list*])* ¶**

Determine an Objective C compiler to use. If `OBJC` is not already set in the environment, check for Objective C compilers. Set output variable `OBJC` to the name of the compiler found.

This macro may, however, be invoked with an optional first argument which, if specified, must be a blank-separated list of Objective C compilers to search for. This just gives the user an opportunity to specify an alternative search list for the Objective C compiler. For example, if you didn’t like the default order, then you could invoke `AC_PROG_OBJC` like this:

```
AC_PROG_OBJC([gcc objcc objc])
```

If using a compiler that supports GNU Objective C, set shell variable `GOBJC` to ‘yes’. If output variable `OBJCFLAGS` was not already set, set it to -g -O2 for a GNU Objective C compiler (-O2 on systems where the compiler does not accept -g), or -g for other compilers.

**Macro: **AC_PROG_OBJCPP** ¶**

Set output variable `OBJCPP` to a command that runs the Objective C preprocessor. If ‘$OBJC -E’ doesn’t work, tries `cpp` and /lib/cpp, in that order. Because of this fallback, `CXXCPP` may or may not set Objective-C-specific predefined macros (such as `__OBJC__`).

#### 5.10.6 Objective C++ Compiler Characteristics

**Macro: **AC_PROG_OBJCXX***([*compiler-search-list*])* ¶**

Determine an Objective C++ compiler to use. If `OBJCXX` is not already set in the environment, check for Objective C++ compilers. Set output variable `OBJCXX` to the name of the compiler found.

This macro may, however, be invoked with an optional first argument which, if specified, must be a blank-separated list of Objective C++ compilers to search for. This just gives the user an opportunity to specify an alternative search list for the Objective C++ compiler. For example, if you didn’t like the default order, then you could invoke `AC_PROG_OBJCXX` like this:

```
AC_PROG_OBJCXX([gcc g++ objcc++ objcxx])
```

If using a compiler that supports GNU Objective C++, set shell variable `GOBJCXX` to ‘yes’. If output variable `OBJCXXFLAGS` was not already set, set it to -g -O2 for a GNU Objective C++ compiler (-O2 on systems where the compiler does not accept -g), or -g for other compilers.

**Macro: **AC_PROG_OBJCXXCPP** ¶**

Set output variable `OBJCXXCPP` to a command that runs the Objective C++ preprocessor. If ‘$OBJCXX -E’ doesn’t work, tries `cpp` and /lib/cpp, in that order. Because of this fallback, `CXXCPP` may or may not set Objective-C++-specific predefined macros (such as `__cplusplus` and `__OBJC__`).

#### 5.10.7 Erlang Compiler and Interpreter Characteristics

Autoconf defines the following macros for determining paths to the essential Erlang/OTP programs:

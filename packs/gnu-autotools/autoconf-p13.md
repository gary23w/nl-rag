---
title: "Autoconf (part 13/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 13/26
---

## 10 Writing Autoconf Macros

When you write a feature test that could be applicable to more than one software package, the best thing to do is encapsulate it in a new macro. Here are some instructions and guidelines for writing Autoconf macros. You should also familiarize yourself with M4sugar (see Programming in M4) and M4sh (see Programming in M4sh).

### 10.1 Macro Definitions

**Macro: **AC_DEFUN***(*name*, [*body*])* ¶**

Autoconf macros are defined using the `AC_DEFUN` macro, which is similar to the M4 builtin `m4_define` macro; this creates a macro named *name* and with *body* as its expansion. In addition to defining a macro, `AC_DEFUN` adds to it some code that is used to constrain the order in which macros are called, while avoiding redundant output (see Prerequisite Macros).

An Autoconf macro definition looks like this:

```
AC_DEFUN(macro-name, macro-body)
```

You can refer to any arguments passed to the macro as ‘$1’, ‘$2’, etc. See How to define new macros in *GNU M4*, for more complete information on writing M4 macros.

Most macros fall in one of two general categories. The first category includes macros which take arguments, in order to generate output parameterized by those arguments. Macros in this category are designed to be directly expanded, often multiple times, and should not be used as the argument to `AC_REQUIRE`. The other category includes macros which are shorthand for a fixed block of text, and therefore do not take arguments. For this category of macros, directly expanding the macro multiple times results in redundant output, so it is more common to use the macro as the argument to `AC_REQUIRE`, or to declare the macro with `AC_DEFUN_ONCE` (see One-Shot Macros).

Be sure to properly quote both the *macro-body* *and* the *macro-name* to avoid any problems if the macro happens to have been previously defined.

Each macro should have a header comment that gives its prototype, and a brief description. When arguments have default values, display them in the prototype. For example:

```
# AC_MSG_ERROR(ERROR, [EXIT-STATUS = 1])
# --------------------------------------
m4_define([AC_MSG_ERROR],
  [{ AS_MESSAGE([error: $1], [2])
     exit m4_default([$2], [1]); }])
```

Comments about the macro should be left in the header comment. Most other comments make their way into configure, so just keep using ‘#’ to introduce comments.

If you have some special comments about pure M4 code, comments that make no sense in configure and in the header comment, then use the builtin `dnl`: it causes M4 to discard the text through the next newline.

Keep in mind that `dnl` is rarely needed to introduce comments; `dnl` is more useful to get rid of the newlines following macros that produce no output, such as `AC_REQUIRE`.

Public third-party macros need to use `AC_DEFUN`, and not `m4_define`, in order to be found by `aclocal` (see Extending aclocal in *GNU Automake*). Additionally, if it is ever determined that a macro should be made obsolete, it is easy to convert from `AC_DEFUN` to `AU_DEFUN` in order to have `autoupdate` assist the user in choosing a better alternative, but there is no corresponding way to make `m4_define` issue an upgrade notice (see AU_DEFUN).

There is another subtle, but important, difference between using `m4_define` and `AC_DEFUN`: only the former is unaffected by `AC_REQUIRE`. When writing a file, it is always safe to replace a block of text with a `m4_define` macro that will expand to the same text. But replacing a block of text with an `AC_DEFUN` macro with the same content does not necessarily give the same results, because it changes the location where any embedded but unsatisfied `AC_REQUIRE` invocations within the block will be expanded. For an example of this, see Expanded Before Required.

### 10.2 Macro Names

All of the public Autoconf macros have all-uppercase names in the namespace ‘^AC_’ to prevent them from accidentally conflicting with other text; Autoconf also reserves the namespace ‘^_AC_’ for internal macros. All shell variables that they use for internal purposes have mostly-lowercase names starting with ‘ac_’. Autoconf also uses here-document delimiters in the namespace ‘^_AC[A-Z]’. During `configure`, files produced by Autoconf make heavy use of the file system namespace ‘^conf’.

Since Autoconf is built on top of M4sugar (see Programming in M4sugar) and M4sh (see Programming in M4sh), you must also be aware of those namespaces (‘^_?\(m4\|AS\)_’). And since configure.ac is also designed to be scanned by Autoheader, Autoscan, Autoupdate, and Automake, you should be aware of the ‘^_?A[HNUM]_’ namespaces. In general, you *should not use* the namespace of a package that does not own the macro or shell code you are writing.

To ensure that your macros don’t conflict with present or future Autoconf macros, you should prefix your own macro names and any shell variables they use with some other sequence. Possibilities include your initials, or an abbreviation for the name of your organization or software package. Historically, people have not always followed the rule of using a namespace appropriate for their package, and this has made it difficult for determining the origin of a macro (and where to report bugs about that macro), as well as difficult for the true namespace owner to add new macros without interference from pre-existing uses of third-party macros. Perhaps the best example of this confusion is the `AM_GNU_GETTEXT` macro, which belongs, not to Automake, but to Gettext.

Most of the Autoconf macros’ names follow a structured naming convention that indicates the kind of feature check by the name. The macro names consist of several words, separated by underscores, going from most general to most specific. The names of their cache variables use the same convention (see Cache Variable Names, for more information on them).

The first word of the name after the namespace initials (such as ‘AC_’) usually tells the category of the feature being tested. Here are the categories used in Autoconf for specific test macros, the kind of macro that you are more likely to write. They are also used for cache variables, in all-lowercase. Use them where applicable; where they’re not, invent your own categories.

**`C`**

C language builtin features.

**`DECL`**

Declarations of C variables in header files.

**`FUNC`**

Functions in libraries.

**`GROUP`**

POSIX group owners of files.

**`HEADER`**

Header files.

**`LIB`**

C libraries.

**`PROG`**

The base names of programs.

**`MEMBER`**

Members of aggregates.

**`SYS`**

Operating system features.

**`TYPE`**

C builtin or declared types.

**`VAR`**

C variables in libraries.

After the category comes the name of the particular feature being tested. Any further words in the macro name indicate particular aspects of the feature. For example, `AC_PROG_MAKE_SET` checks whether `make` sets a variable to its own name.

An internal macro should have a name that starts with an underscore; Autoconf internals should therefore start with ‘_AC_’. Additionally, a macro that is an internal subroutine of another macro should have a name that starts with an underscore and the name of that other macro, followed by one or more words saying what the internal macro does. For example, `AC_PATH_X` has internal macros `_AC_PATH_X_XMKMF` and `_AC_PATH_X_DIRECT`.

### 10.3 Dependencies Between Macros

Some Autoconf macros depend on other macros having been called first in order to work correctly. Autoconf provides a way to ensure that certain macros are called if needed and a way to warn the user if macros are called in an order that might cause incorrect operation.

#### 10.3.1 Prerequisite Macros

A macro that you write might need to use values that have previously been computed by other macros. For example, `AC_DECL_YYTEXT` examines the output of `flex` or `lex`, so it depends on `AC_PROG_LEX` having been called first to set the shell variable `LEX`.

Rather than forcing the user of the macros to keep track of the dependencies between them, you can use the `AC_REQUIRE` macro to do it automatically. `AC_REQUIRE` can ensure that a macro is only called if it is needed, and only called once.

**Macro: **AC_REQUIRE***(*macro-name*)* ¶**

If the M4 macro *macro-name* has not already been called, call it (without any arguments). Make sure to quote *macro-name* with square brackets. *macro-name* must have been defined using `AC_DEFUN` or else contain a call to `AC_PROVIDE` to indicate that it has been called.

`AC_REQUIRE` must be used inside a macro defined by `AC_DEFUN`; it must not be called from the top level. Also, it does not make sense to require a macro that takes parameters.

`AC_REQUIRE` is often misunderstood. It really implements dependencies between macros in the sense that if one macro depends upon another, the latter is expanded *before* the body of the former. To be more precise, the required macro is expanded before the outermost defined macro in the current expansion stack. In particular, ‘AC_REQUIRE([FOO])’ is not replaced with the body of `FOO`. For instance, this definition of macros:

```
AC_DEFUN([TRAVOLTA],
[test "$body_temperature_in_Celsius" -gt 38 &&
  dance_floor=occupied])
AC_DEFUN([NEWTON_JOHN],
[test "x$hair_style" = xcurly &&
  dance_floor=occupied])
```

```
AC_DEFUN([RESERVE_DANCE_FLOOR],
[if test "x`date +%A`" = xSaturday; then
  AC_REQUIRE([TRAVOLTA])
  AC_REQUIRE([NEWTON_JOHN])
fi])
```

with this configure.ac

```
AC_INIT([Dance Manager], [1.0], [bug-dance@example.org])
RESERVE_DANCE_FLOOR
if test "x$dance_floor" = xoccupied; then
  AC_MSG_ERROR([cannot pick up here, let's move])
fi
```

does not leave you with a better chance to meet a kindred soul on days other than Saturday, since the call to `RESERVE_DANCE_FLOOR` expands to:

```
test "$body_temperature_in_Celsius" -gt 38 &&
  dance_floor=occupied
test "x$hair_style" = xcurly &&
  dance_floor=occupied
if test "x`date +%A`" = xSaturday; then

fi
```

This behavior was chosen on purpose: (i) it prevents messages in required macros from interrupting the messages in the requiring macros; (ii) it avoids bad surprises when shell conditionals are used, as in:

```
if ...; then
  AC_REQUIRE([SOME_CHECK])
fi
...
SOME_CHECK
```

However, this implementation can lead to another class of problems. Consider the case where an outer macro first expands, then indirectly requires, an inner macro:

```
AC_DEFUN([TESTA], [[echo in A
if test -n "$SEEN_A" ; then echo duplicate ; fi
SEEN_A=:]])
AC_DEFUN([TESTB], [AC_REQUIRE([TESTA])[echo in B
if test -z "$SEEN_A" ; then echo bug ; fi]])
AC_DEFUN([TESTC], [AC_REQUIRE([TESTB])[echo in C]])
AC_DEFUN([OUTER], [[echo in OUTER]
TESTA
TESTC])
OUTER
```

Prior to Autoconf 2.64, the implementation of `AC_REQUIRE` recognized that `TESTB` needed to be hoisted prior to the expansion of `OUTER`, but because `TESTA` had already been directly expanded, it failed to hoist `TESTA`. Therefore, the expansion of `TESTB` occurs prior to its prerequisites, leading to the following output:

```
in B
bug
in OUTER
in A
in C
```

Newer Autoconf is smart enough to recognize this situation, and hoists `TESTA` even though it has already been expanded, but issues a syntax warning in the process. This is because the hoisted expansion of `TESTA` defeats the purpose of using `AC_REQUIRE` to avoid redundant code, and causes its own set of problems if the hoisted macro is not idempotent:

```
in A
in B
in OUTER
in A
duplicate
in C
```

The bug is not in Autoconf, but in the macro definitions. If you ever pass a particular macro name to `AC_REQUIRE`, then you are implying that the macro only needs to be expanded once. But to enforce this, either the macro must be declared with `AC_DEFUN_ONCE` (although this only helps in Autoconf 2.64 or newer), or all uses of that macro should be through `AC_REQUIRE`; directly expanding the macro defeats the point of using `AC_REQUIRE` to eliminate redundant expansion. In the example, this rule of thumb was violated because `TESTB` requires `TESTA` while `OUTER` directly expands it. One way of fixing the bug is to factor `TESTA` into two macros, the portion designed for direct and repeated use (here, named `TESTA`), and the portion designed for one-shot output and used only inside `AC_REQUIRE` (here, named `TESTA_PREREQ`). Then, by fixing all clients to use the correct calling convention according to their needs:

```
AC_DEFUN([TESTA], [AC_REQUIRE([TESTA_PREREQ])[echo in A]])
AC_DEFUN([TESTA_PREREQ], [[echo in A_PREREQ
if test -n "$SEEN_A" ; then echo duplicate ; fi
SEEN_A=:]])
AC_DEFUN([TESTB], [AC_REQUIRE([TESTA_PREREQ])[echo in B
if test -z "$SEEN_A" ; then echo bug ; fi]])
AC_DEFUN([TESTC], [AC_REQUIRE([TESTB])[echo in C]])
AC_DEFUN([OUTER], [[echo in OUTER]
TESTA
TESTC])
OUTER
```

the resulting output will then obey all dependency rules and avoid any syntax warnings, whether the script is built with old or new Autoconf versions:

```
in A_PREREQ
in B
in OUTER
in A
in C
```

You can use the helper macros `AS_IF` and `AS_CASE` in top-level code to enforce expansion of required macros outside of shell conditional constructs; these helpers are not needed in the bodies of macros defined by `AC_DEFUN`. You are furthermore encouraged, although not required, to put all `AC_REQUIRE` calls at the beginning of a macro. You can use `dnl` to avoid the empty lines they leave.

Autoconf will normally warn if an `AC_REQUIRE` call refers to a macro that has not been defined. However, the `aclocal` tool relies on parsing an incomplete set of input files to trace which macros have been required, in order to then pull in additional files that provide those macros; for this particular use case, pre-defining the macro `m4_require_silent_probe` will avoid the warnings.

#### 10.3.2 Suggested Ordering

Some macros should be run before another macro if both are called, but neither *requires* that the other be called. For example, a macro that changes the behavior of the C compiler should be called before any macros that run the C compiler. Many of these dependencies are noted in the documentation.

Autoconf provides the `AC_BEFORE` macro to warn users when macros with this kind of dependency appear out of order in a configure.ac file. The warning occurs when creating `configure` from configure.ac, not when running `configure`.

For example, `AC_PROG_CPP` checks whether the C compiler can run the C preprocessor when given the -E option. It should therefore be called after any macros that change which C compiler is being used, such as `AC_PROG_CC`. So `AC_PROG_CC` contains:

```
AC_BEFORE([$0], [AC_PROG_CPP])dnl
```

This warns the user if a call to `AC_PROG_CPP` has already occurred when `AC_PROG_CC` is called.

**Macro: **AC_BEFORE***(*this-macro-name*, *called-macro-name*)* ¶**

Make M4 print a warning message to the standard error output if *called-macro-name* has already been called. *this-macro-name* should be the name of the macro that is calling `AC_BEFORE`. The macro *called-macro-name* must have been defined using `AC_DEFUN` or else contain a call to `AC_PROVIDE` to indicate that it has been called.

#### 10.3.3 One-Shot Macros

Some macros should be called only once, either because calling them multiple time is unsafe, or because it is bad style. For instance Autoconf ensures that `AC_CANONICAL_BUILD` and cousins (see Getting the Canonical System Type) are evaluated only once, because it makes no sense to run these expensive checks more than once. Such one-shot macros can be defined using `AC_DEFUN_ONCE`.

**Macro: **AC_DEFUN_ONCE***(*macro-name*, *macro-body*)* ¶**

Declare macro *macro-name* like `AC_DEFUN` would (see Macro Definitions), but add additional logic that guarantees that only the first use of the macro (whether by direct expansion or `AC_REQUIRE`) causes an expansion of *macro-body*; the expansion will occur before the start of any enclosing macro defined by `AC_DEFUN`. Subsequent expansions are silently ignored. Generally, it does not make sense for *macro-body* to use parameters such as `$1`.

Prior to Autoconf 2.64, a macro defined by `AC_DEFUN_ONCE` would emit a warning if it was directly expanded a second time, so for portability, it is better to use `AC_REQUIRE` than direct invocation of *macro-name* inside a macro defined by `AC_DEFUN` (see Prerequisite Macros).

### 10.4 Obsoleting Macros

Configuration and portability technology has evolved over the years. Often better ways of solving a particular problem are developed, or ad-hoc approaches are systematized. This process has occurred in many parts of Autoconf. One result is that some of the macros are now considered *obsolete*; they still work, but are no longer considered the best thing to do, hence they should be replaced with more modern macros. Ideally, `autoupdate` should replace the old macro calls with their modern implementation.

Autoconf provides a simple means to obsolete a macro.

**Macro: **AU_DEFUN***(*old-macro*, *implementation*, [*message*], [*silent*])* ¶**

Define *old-macro* as *implementation*, just like `AC_DEFUN`, but also declare *old-macro* to be obsolete. When `autoupdate` is run, occurrences of *old-macro* will be replaced by the text of *implementation* in the updated configure.ac file.

If a simple textual replacement is not enough to finish the job of updating a configure.ac to modern style, provide instructions for whatever additional manual work is required as *message*. These instructions will be printed by `autoupdate`, and embedded in the updated configure.ac file, next to the text of *implementation*.

Normally, `autoconf` will also issue a warning (in the “obsolete” category) when it expands *old-macro*. This warning does not include *message*; it only advises the maintainer to run `autoupdate`. If it is inappropriate to issue this warning, set the *silent* argument to the word `silent`. One might want to use a silent `AU_DEFUN` when *old-macro* is used in a widely-distributed third-party macro. If that macro’s maintainers are aware of the need to update their code, it’s unnecessary to nag all of the transitive users of *old-macro* as well. This capability was added to `AU_DEFUN` in Autoconf 2.70; older versions of autoconf will ignore the *silent* argument and issue the warning anyway.

**Caution:** If *implementation* contains M4 or M4sugar macros, they will be evaluated when `autoupdate` is run, not emitted verbatim like the rest of *implementation*. This cannot be avoided with extra quotation, because then *old-macro* will not work when it is called normally. See the definition of `AC_FOREACH` in general.m4 for a workaround.

**Macro: **AU_ALIAS***(*old-name*, *new-name*, [*silent*])* ¶**

A shorthand version of `AU_DEFUN`, to be used when a macro has simply been renamed. `autoupdate` will replace calls to *old-name* with calls to *new-name*, keeping any arguments intact. No instructions for additional manual work will be printed.

The *silent* argument works the same as the *silent* argument to `AU_DEFUN`. It was added to `AU_ALIAS` in Autoconf 2.70.

**Caution:** `AU_ALIAS` cannot be used when *new-name* is an M4 or M4sugar macro. See above.

### 10.5 Coding Style

The Autoconf macros follow a strict coding style. You are encouraged to follow this style, especially if you intend to distribute your macro, either by contributing it to Autoconf itself or the Autoconf Macro Archive, or by other means.

The first requirement is to pay great attention to the quotation. For more details, see The Autoconf Language, and M4 Quotation.

Do not try to invent new interfaces. It is likely that there is a macro in Autoconf that resembles the macro you are defining: try to stick to this existing interface (order of arguments, default values, etc.). We *are* conscious that some of these interfaces are not perfect; nevertheless, when harmless, homogeneity should be preferred over creativity.

Be careful about clashes both between M4 symbols and between shell variables.

If you stick to the suggested M4 naming scheme (see Macro Names), you are unlikely to generate conflicts. Nevertheless, when you need to set a special value, *avoid using a regular macro name*; rather, use an “impossible” name. For instance, up to version 2.13, the macro `AC_SUBST` used to remember what *symbol* macros were already defined by setting `AC_SUBST_*symbol*`, which is a regular macro name. But since there is a macro named `AC_SUBST_FILE`, it was just impossible to ‘AC_SUBST(FILE)’! In this case, `AC_SUBST(*symbol*)` or `_AC_SUBST(*symbol*)` should have been used (yes, with the parentheses).

No Autoconf macro should ever enter the user-variable name space; i.e., except for the variables that are the actual result of running the macro, all shell variables should start with `ac_`. In addition, small macros or any macro that is likely to be embedded in other macros should be careful not to use obvious names.

Do not use `dnl` to introduce comments: most of the comments you are likely to write are either header comments which are not output anyway, or comments that should make their way into configure. There are exceptional cases where you do want to comment special M4 constructs, in which case `dnl` is right, but keep in mind that it is unlikely.

M4 ignores the leading blanks and newlines before each argument. Use this feature to indent in such a way that arguments are (more or less) aligned with the opening parenthesis of the macro being called. For instance, instead of

```
AC_CACHE_CHECK(for EMX OS/2 environment,
ac_cv_emxos2,
[AC_COMPILE_IFELSE([AC_LANG_PROGRAM(, [return __EMX__;])],
[ac_cv_emxos2=yes], [ac_cv_emxos2=no])])
```

write

```
AC_CACHE_CHECK([for EMX OS/2 environment], [ac_cv_emxos2],
[AC_COMPILE_IFELSE([AC_LANG_PROGRAM([], [return __EMX__;])],
                   [ac_cv_emxos2=yes],
                   [ac_cv_emxos2=no])])
```

or even

```
AC_CACHE_CHECK([for EMX OS/2 environment],
               [ac_cv_emxos2],
               [AC_COMPILE_IFELSE([AC_LANG_PROGRAM([],
                                                   [return __EMX__;])],
                                  [ac_cv_emxos2=yes],
                                  [ac_cv_emxos2=no])])
```

When using `AC_RUN_IFELSE` or any macro that cannot work when cross-compiling, provide a pessimistic value (typically ‘no’).

Feel free to use various tricks to prevent auxiliary tools, such as syntax-highlighting editors, from behaving improperly. For instance, instead of:

```
m4_bpatsubst([$1], [$"])
```

use

```
m4_bpatsubst([$1], [$""])
```

so that Emacsen do not open an endless “string” at the first quote. For the same reasons, avoid:

```
test $[#] != 0
```

and use:

```
test $[@%:@] != 0
```

Otherwise, the closing bracket would be hidden inside a ‘#’-comment, breaking the bracket-matching highlighting from Emacsen. Note the preferred style to escape from M4: ‘$[1]’, ‘$[@]’, etc. Do not escape when it is unnecessary. Common examples of useless quotation are ‘[$]$1’ (write ‘$$1’), ‘[$]var’ (use ‘$var’), etc.

When using `sed`, don’t use -e except for indenting purposes. With the `s` and `y` commands, the preferred separator is ‘/’ unless ‘/’ itself might appear in the pattern or replacement, in which case you should use ‘|’, or optionally ‘,’ if you know the pattern and replacement cannot contain a file name. If none of these characters will do, choose a printable character that cannot appear in the pattern or replacement. Characters from the set ‘"#$&'()*;<=>?`|~’ are good choices if the pattern or replacement might contain a file name, since they have special meaning to the shell and are less likely to occur in file names.

See Macro Definitions, for details on how to define a macro. If a macro doesn’t use `AC_REQUIRE`, is expected to never be the object of an `AC_REQUIRE` directive, and macros required by other macros inside arguments do not need to be expanded before this macro, then use `m4_define`. In case of doubt, use `AC_DEFUN`. Also take into account that public third-party macros need to use `AC_DEFUN` in order to be found by `aclocal` (see Extending aclocal in *GNU Automake*). All the `AC_REQUIRE` statements should be at the beginning of the macro, and each statement should be followed by `dnl`.

You should not rely on the number of arguments: instead of checking whether an argument is missing, test that it is not empty. It provides both a simpler and a more predictable interface to the user, and saves room for further arguments.

Unless the macro is short, try to leave the closing ‘])’ at the beginning of a line, followed by a comment that repeats the name of the macro being defined. This introduces an additional newline in `configure`; normally, that is not a problem, but if you want to remove it you can use ‘[]dnl’ on the last line. You can similarly use ‘[]dnl’ after a macro call to remove its newline. ‘[]dnl’ is recommended instead of ‘dnl’ to ensure that M4 does not interpret the ‘dnl’ as being attached to the preceding text or macro output. For example, instead of:

```
AC_DEFUN([AC_PATH_X],
[AC_MSG_CHECKING([for X])
AC_REQUIRE_CPP()
# ...omitted...
  AC_MSG_RESULT([libraries $x_libraries, headers $x_includes])
fi])
```

you would write:

```
AC_DEFUN([AC_PATH_X],
[AC_REQUIRE_CPP()[]dnl
AC_MSG_CHECKING([for X])
# ...omitted...
  AC_MSG_RESULT([libraries $x_libraries, headers $x_includes])
fi[]dnl
])# AC_PATH_X
```

If the macro is long, try to split it into logical chunks. Typically, macros that check for a bug in a function and prepare its `AC_LIBOBJ` replacement should have an auxiliary macro to perform this setup. Do not hesitate to introduce auxiliary macros to factor your code.

In order to highlight the recommended coding style, here is a macro written the old way:

```
dnl Check for EMX on OS/2.
dnl _AC_EMXOS2
AC_DEFUN(_AC_EMXOS2,
[AC_CACHE_CHECK(for EMX OS/2 environment, ac_cv_emxos2,
[AC_COMPILE_IFELSE([AC_LANG_PROGRAM(, return __EMX__;)],
ac_cv_emxos2=yes, ac_cv_emxos2=no)])
test "x$ac_cv_emxos2" = xyes && EMXOS2=yes])
```

and the new way:

```
# _AC_EMXOS2
# ----------
# Check for EMX on OS/2.
m4_define([_AC_EMXOS2],
[AC_CACHE_CHECK([for EMX OS/2 environment], [ac_cv_emxos2],
[AC_COMPILE_IFELSE([AC_LANG_PROGRAM([], [return __EMX__;])],
                   [ac_cv_emxos2=yes],
                   [ac_cv_emxos2=no])])
test "x$ac_cv_emxos2" = xyes && EMXOS2=yes[]dnl
])# _AC_EMXOS2
```

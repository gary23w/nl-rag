---
title: "Autoconf (part 10/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 10/26
---

## ------------------ ##

begin-language: "Autoconf-without-aclocal-m4"
args: --no-cache
end-language: "Autoconf-without-aclocal-m4"
```

### 8.3 Programming in M4sugar

M4 by itself provides only a small, but sufficient, set of all-purpose macros. M4sugar introduces additional generic macros. Its name was coined by Lars J. Aas: “Readability And Greater Understanding Stands 4 M4sugar”.

M4sugar reserves the macro namespace ‘^_m4_’ for internal use, and the macro namespace ‘^m4_’ for M4sugar macros. You should not define your own macros into these namespaces.

#### 8.3.1 Redefined M4 Macros

With a few exceptions, all the M4 native macros are moved in the ‘m4_’ pseudo-namespace, e.g., M4sugar renames `define` as `m4_define` etc.

The list of macros unchanged from M4, except for their name, is:

- m4_builtin
- m4_changecom
- m4_changequote
- m4_debugfile
- m4_debugmode
- m4_decr
- m4_define
- m4_divnum
- m4_errprint
- m4_esyscmd
- m4_eval
- m4_format
- m4_ifdef
- m4_incr
- m4_index
- m4_indir
- m4_len
- m4_pushdef
- m4_shift
- m4_substr
- m4_syscmd
- m4_sysval
- m4_traceoff
- m4_traceon
- m4_translit

Some M4 macros are redefined, and are slightly incompatible with their native equivalent.

**Macro: **__file__** ¶**

**Macro: **__line__** ¶**

All M4 macros starting with ‘__’ retain their original name: for example, no `m4__file__` is defined.

**Macro: **__oline__** ¶**

This is not technically a macro, but a feature of Autom4te. The sequence `__oline__` can be used similarly to the other m4sugar location macros, but rather than expanding to the location of the input file, it is translated to the line number where it appears in the output file after all other M4 expansions.

**Macro: **dnl** ¶**

This macro kept its original name: no `m4_dnl` is defined.

**Macro: **m4_bpatsubst***(*string*, *regexp*, [*replacement*])* ¶**

This is the M4sugar name for the M4 native macro `patsubst`.

It uses the same regular expression syntax as `m4_bregexp`; see m4_bregexp. Also see Substituting text by regular expression in *GNU m4 macro processor*, for details of how the *replacement* is processed.

The name `m4_patsubst` is reserved for use by a future version of M4sugar, when there is a version of GNU M4 that supports POSIX extended regular expression syntax.

**Macro: **m4_bregexp***(*string*, *regexp*, [*replacement*])* ¶**

This is the M4sugar name for the M4 native macro `regexp`.

The only regular expression syntax understood by GNU M4 is similar to, but not the same as, POSIX basic regular expression syntax. See Searching for regular expressions in *GNU m4 macro processor*, for the precise syntax.

The name `m4_regexp` is reserved for use by a future version of M4sugar, when there is a version of GNU M4 that supports POSIX extended regular expression syntax.

**Macro: **m4_copy***(*source*, *dest*)* ¶**

**Macro: **m4_copy_force***(*source*, *dest*)* ¶**

**Macro: **m4_rename***(*source*, *dest*)* ¶**

**Macro: **m4_rename_force***(*source*, *dest*)* ¶**

These macros aren’t directly builtins, but are closely related to `m4_pushdef` and `m4_defn`. `m4_copy` and `m4_rename` ensure that *dest* is undefined, while `m4_copy_force` and `m4_rename_force` overwrite any existing definition. All four macros then proceed to copy the entire pushdef stack of definitions of *source* over to *dest*. `m4_copy` and `m4_copy_force` preserve the source (including in the special case where *source* is undefined), while `m4_rename` and `m4_rename_force` undefine the original macro name (making it an error to rename an undefined *source*).

Note that attempting to invoke a renamed macro might not work, since the macro may have a dependence on helper macros accessed via composition of ‘$0’ but that were not also renamed; likewise, other macros may have a hard-coded dependence on *source* and could break if *source* has been deleted. On the other hand, it is always safe to rename a macro to temporarily move it out of the way, then rename it back later to restore original semantics.

**Macro: **m4_defn***(*macro*…)* ¶**

This macro fails if *macro* is not defined, even when using older versions of M4 that did not warn. See `m4_undefine`. Unfortunately, in order to support these older versions of M4, there are some situations involving unbalanced quotes where concatenating multiple macros together will work in newer M4 but not in m4sugar; use quadrigraphs to work around this.

**Macro: **m4_divert***(*diversion*)* ¶**

M4sugar relies heavily on diversions, so rather than behaving as a primitive, `m4_divert` behaves like:

```
m4_divert_pop()m4_divert_push([diversion])
```

See Diversion support, for more details about the use of the diversion stack. In particular, this implies that *diversion* should be a named diversion rather than a raw number. But be aware that it is seldom necessary to explicitly change the diversion stack, and that when done incorrectly, it can lead to syntactically invalid scripts.

**Macro: **m4_dumpdef***(*name*…)* ¶**

**Macro: **m4_dumpdefs***(*name*…)* ¶**

`m4_dumpdef` is like the M4 builtin, except that this version requires at least one argument, output always goes to standard error rather than the current debug file, no sorting is done on multiple arguments, and an error is issued if any *name* is undefined. `m4_dumpdefs` is a convenience macro that calls `m4_dumpdef` for all of the `m4_pushdef` stack of definitions, starting with the current, and silently does nothing if *name* is undefined.

Unfortunately, due to a limitation in M4 1.4.x, any macro defined as a builtin is output as the empty string. This behavior is rectified by using M4 1.6 or newer. However, this behavior difference means that `m4_dumpdef` should only be used while developing m4sugar macros, and never in the final published form of a macro.

**Macro: **m4_esyscmd_s***(*command*)* ¶**

Like `m4_esyscmd`, this macro expands to the result of running *command* in a shell. The difference is that any trailing newlines are removed, so that the output behaves more like shell command substitution.

**Macro: **m4_exit***(*exit-status*)* ¶**

This macro corresponds to `m4exit`.

**Macro: **m4_if***(*comment*)* ¶**

**Macro: **m4_if***(*string-1*, *string-2*, *equal*, [*not-equal*])* ¶**

**Macro: **m4_if***(*string-1*, *string-2*, *equal-1*, *string-3*, *string-4*, *equal-2*, …, [*not-equal*])* ¶**

This macro corresponds to `ifelse`. *string-1* and *string-2* are compared literally, so usually one of the two arguments is passed unquoted. See Conditional constructs, for more conditional idioms.

**Macro: **m4_include***(*file*)* ¶**

**Macro: **m4_sinclude***(*file*)* ¶**

Like the M4 builtins, but warn against multiple inclusions of *file*.

**Macro: **m4_mkstemp***(*template*)* ¶**

**Macro: **m4_maketemp***(*template*)* ¶**

Older versions of POSIX specified a macro `maketemp`, which replaced the trailing ‘X’ characters in *template* with the process id, without regards to the existence of a file by that name. This was a security hole, so current POSIX instead specifies a macro `mkstemp` that always creates a uniquely named file. In M4sugar, `m4_maketemp` and `m4_mkstemp` are synonyms for each other, and both have the secure semantics regardless of which macro the underlying M4 provides.

**Macro: **m4_popdef***(*macro*…)* ¶**

This macro fails if *macro* is not defined, even when using older versions of M4 that did not warn. See `m4_undefine`.

**Macro: **m4_undefine***(*macro*…)* ¶**

This macro fails if *macro* is not defined, even when using older versions of M4 that did not warn. Use

```
m4_ifdef([macro], [m4_undefine([macro])])
```

if you are not sure whether *macro* is defined.

**Macro: **m4_undivert***(*diversion*…)* ¶**

Unlike the M4 builtin, at least one *diversion* must be specified. Also, since the M4sugar diversion stack prefers named diversions, the use of `m4_undivert` to include files is risky. See Diversion support, for more details about the use of the diversion stack. But be aware that it is seldom necessary to explicitly change the diversion stack, and that when done incorrectly, it can lead to syntactically invalid scripts.

**Macro: **m4_wrap***(*text*)* ¶**

**Macro: **m4_wrap_lifo***(*text*)* ¶**

These macros correspond to `m4wrap`. POSIX requires arguments of multiple wrap calls to be reprocessed at EOF in the same order as the original calls (first-in, first-out). GNU M4 versions through 1.4.10, however, reprocess them in reverse order (last-in, first-out). Both orders are useful, therefore, you can rely on `m4_wrap` to provide FIFO semantics and `m4_wrap_lifo` for LIFO semantics, regardless of the underlying GNU M4 version.

Unlike the GNU M4 builtin, these macros only recognize one argument, and avoid token pasting between consecutive invocations. On the other hand, nested calls to `m4_wrap` from within wrapped text work just as in the builtin.

#### 8.3.2 Diagnostic messages from M4sugar

When macros statically diagnose abnormal situations, benign or fatal, they should report them using these macros. For issuing dynamic issues, i.e., when `configure` is run, see Printing Messages.

**Macro: **m4_assert***(*expression*, [*exit-status* = ‘1’])* ¶**

Assert that the arithmetic *expression* evaluates to non-zero. Otherwise, issue a fatal error, and exit `autom4te` with *exit-status*.

**Macro: **m4_errprintn***(*message*)* ¶**

Similar to the builtin `m4_errprint`, except that a newline is guaranteed after *message*.

**Macro: **m4_fatal***(*message*)* ¶**

Report a severe error *message* prefixed with the current location, and have `autom4te` die.

**Macro: **m4_location** ¶**

Useful as a prefix in a message line. Short for:

```
__file__:__line__
```

**Macro: **m4_warn***(*category*, *message*)* ¶**

Report *message* as a warning (or as an error if requested by the user) if warnings of the *category* are turned on. If the message is emitted, it is prefixed with the current location, and followed by a call trace of all macros defined via `AC_DEFUN` used to get to the current expansion.

The *category* must be one of:

**‘cross’**

Warnings about constructs that may interfere with cross-compilation, such as using `AC_RUN_IFELSE` without a default.

**‘gnu’**

Warnings related to the GNU Coding Standards (see *The GNU Coding Standards*). On by default.

**‘obsolete’**

Warnings about obsolete features. On by default.

**‘override’**

Warnings about redefinitions of Autoconf internals.

**‘portability’**

Warnings about non-portable constructs.

**‘portability-recursive’**

Warnings about recursive Make variable expansions (`$(foo$(x))`).

**‘extra-portability’**

Extra warnings about non-portable constructs, covering rarely-used tools.

**‘syntax’**

Warnings about questionable syntactic constructs, incorrectly ordered macro calls, typos, etc. On by default.

**‘unsupported’**

Warnings about unsupported features. On by default.

**Hacking Note:** The set of categories is defined by code in `autom4te`, not by M4sugar itself. Additions should be coordinated with Automake, so that both sets of tools accept the same options.

#### 8.3.3 Diversion support

M4sugar makes heavy use of diversions under the hood, because it is often the case that text that must appear early in the output is not discovered until late in the input. Additionally, some of the topological sorting algorithms used in resolving macro dependencies use diversions. However, most macros should not need to change diversions directly, but rather rely on higher-level M4sugar macros to manage diversions transparently. If you change diversions improperly, you risk generating a syntactically invalid script, because an incorrect diversion will violate assumptions made by many macros about whether prerequisite text has been previously output. In short, if you manually change the diversion, you should not expect any macros provided by the Autoconf package to work until you have restored the diversion stack back to its original state.

In the rare case that it is necessary to write a macro that explicitly outputs text to a different diversion, it is important to be aware of an M4 limitation regarding diversions: text only goes to a diversion if it is not part of argument collection. Therefore, any macro that changes the current diversion cannot be used as an unquoted argument to another macro, but must be expanded at the top level. The macro `m4_expand` will diagnose any attempt to change diversions, since it is generally useful only as an argument to another macro. The following example shows what happens when diversion manipulation is attempted within macro arguments:

```
m4_do([normal text]
m4_divert_push([KILL])unwanted[]m4_divert_pop([KILL])
[m4_divert_push([KILL])discarded[]m4_divert_pop([KILL])])dnl
⇒normal text
⇒unwanted
```

Notice that the unquoted text `unwanted` is output, even though it was processed while the current diversion was `KILL`, because it was collected as part of the argument to `m4_do`. However, the text `discarded` disappeared as desired, because the diversion changes were single-quoted, and were not expanded until the top-level rescan of the output of `m4_do`.

To make diversion management easier, M4sugar uses the concept of named diversions. Rather than using diversion numbers directly, it is nicer to associate a name with each diversion. The diversion number associated with a particular diversion name is an implementation detail, and a syntax warning is issued if a diversion number is used instead of a name. In general, you should not output text to a named diversion until after calling the appropriate initialization routine for your language (`m4_init`, `AS_INIT`, `AT_INIT`, …), although there are some exceptions documented below.

M4sugar defines two named diversions.

**`KILL`**

Text written to this diversion is discarded. This is the default diversion once M4sugar is initialized.

**`GROW`**

This diversion is used behind the scenes by topological sorting macros, such as `AC_REQUIRE`.

M4sh adds several more named diversions.

**`BINSH`**

This diversion is reserved for the ‘#!’ interpreter line.

**`HEADER-REVISION`**

This diversion holds text from `AC_REVISION`.

**`HEADER-COMMENT`**

This diversion holds comments about the purpose of a file.

**`HEADER-COPYRIGHT`**

This diversion is managed by `AC_COPYRIGHT`.

**`M4SH-SANITIZE`**

This diversion contains M4sh sanitization code, used to ensure M4sh is executing in a reasonable shell environment.

**`M4SH-INIT`**

This diversion contains M4sh initialization code, initializing variables that are required by other M4sh macros.

**`BODY`**

This diversion contains the body of the shell code, and is the default diversion once M4sh is initialized.

Autotest inherits diversions from M4sh, and changes the default diversion from `BODY` back to `KILL`. It also adds several more named diversions, with the following subset designed for developer use.

**`PREPARE_TESTS`**

This diversion contains initialization sequences which are executed after atconfig and atlocal, and after all command line arguments have been parsed, but prior to running any tests. It can be used to set up state that is required across all tests. This diversion will work even before `AT_INIT`.

Autoconf inherits diversions from M4sh, and adds the following named diversions which developers can utilize.

**`DEFAULTS`**

This diversion contains shell variable assignments to set defaults that must be in place before arguments are parsed. This diversion is placed early enough in configure that it is unsafe to expand any autoconf macros into this diversion.

**`HELP_ENABLE`**

If `AC_PRESERVE_HELP_ORDER` was used, then text placed in this diversion will be included as part of a quoted here-doc providing all of the --help output of configure related to options created by `AC_ARG_WITH` and `AC_ARG_ENABLE`.

**`INIT_PREPARE`**

This diversion occurs after all command line options have been parsed, but prior to the main body of the configure script. This diversion is the last chance to insert shell code such as variable assignments or shell function declarations that will used by the expansion of other macros.

For now, the remaining named diversions of Autoconf, Autoheader, and Autotest are not documented. In other words, intentionally outputting text into an undocumented diversion is subject to breakage in a future release of Autoconf.

**Macro: **m4_cleardivert***(*diversion*…)* ¶**

Permanently discard any text that has been diverted into *diversion*.

**Macro: **m4_divert_once***(*diversion*, [*content*])* ¶**

Similar to `m4_divert_text`, except that *content* is only output to *diversion* if this is the first time that `m4_divert_once` has been called with its particular arguments.

**Macro: **m4_divert_pop***([*diversion*])* ¶**

If provided, check that the current diversion is indeed *diversion*. Then change to the diversion located earlier on the stack, giving an error if an attempt is made to pop beyond the initial m4sugar diversion of `KILL`.

**Macro: **m4_divert_push***(*diversion*)* ¶**

Remember the former diversion on the diversion stack, and output subsequent text into *diversion*. M4sugar maintains a diversion stack, and issues an error if there is not a matching pop for every push.

**Macro: **m4_divert_text***(*diversion*, [*content*])* ¶**

Output *content* and a newline into *diversion*, without affecting the current diversion. Shorthand for:

```
m4_divert_push([diversion])content
m4_divert_pop([diversion])dnl
```

One use of `m4_divert_text` is to develop two related macros, where macro ‘MY_A’ does the work, but adjusts what work is performed based on whether the optional macro ‘MY_B’ has also been expanded. Of course, it is possible to use `AC_BEFORE` within `MY_A` to require that ‘MY_B’ occurs first, if it occurs at all. But this imposes an ordering restriction on the user; it would be nicer if macros ‘MY_A’ and ‘MY_B’ can be invoked in either order. The trick is to let ‘MY_B’ leave a breadcrumb in an early diversion, which ‘MY_A’ can then use to determine whether ‘MY_B’ has been expanded.

```
AC_DEFUN([MY_A],
[# various actions
if test -n "$b_was_used"; then
  # extra action
fi])
AC_DEFUN([MY_B],
[AC_REQUIRE([MY_A])dnl
m4_divert_text([INIT_PREPARE], [b_was_used=true])])
```

**Macro: **m4_init** ¶**

Initialize the M4sugar environment, setting up the default named diversion to be `KILL`.

#### 8.3.4 Conditional constructs

The following macros provide additional conditional constructs as convenience wrappers around `m4_if`.

**Macro: **m4_bmatch***(*string*, *regex-1*, *value-1*, [*regex-2*], [*value-2*], …, [*default*])* ¶**

The string *string* is repeatedly compared against a series of *regex* arguments; if a match is found, the expansion is the corresponding *value*, otherwise, the macro moves on to the next *regex*. If no *regex* match, then the result is the optional *default*, or nothing.

The regular expression syntax understood by `m4_bmatch` is the same as that understood by `m4_bregexp`; see m4_bregexp. The name `m4_match` is reserved for use by a future version of M4sugar, when there is a version of GNU M4 that supports POSIX extended regular expression syntax.

**Macro: **m4_bpatsubsts***(*string*, *regex-1*, *subst-1*, [*regex-2*], [*subst-2*], …)* ¶**

The string *string* is altered by *regex-1* and *subst-1*, as if by:

```
m4_bpatsubst([[string]], [regex], [subst])
```

The result of the substitution is then passed through the next set of *regex* and *subst*, and so forth. An empty *subst* implies deletion of any matched portions in the current string. Note that this macro over-quotes *string*; this behavior is intentional, so that the result of each step of the recursion remains as a quoted string. However, it means that anchors (‘^’ and ‘$’ in the *regex* will line up with the extra quotations, and not the characters of the original string. The overquoting is removed after the final substitution.

The regular expression and replacement syntax understood by `m4_bpatsubsts` is the same as that understood by `m4_bpatsubst`; see m4_bpatsubst. The name `m4_patsubsts` is reserved for use by future version of M4sugar, when there is a version of GNU M4 that supports POSIX extended regular expression syntax.

**Macro: **m4_case***(*string*, *value-1*, *if-value-1*, [*value-2*], [*if-value-2*], …, [*default*])* ¶**

Test *string* against multiple *value* possibilities, resulting in the first *if-value* for a match, or in the optional *default*. This is shorthand for:

```
m4_if([string], [value-1], [if-value-1],
      [string], [value-2], [if-value-2], ...,
      [default])
```

**Macro: **m4_cond***(*test-1*, *value-1*, *if-value-1*, [*test-2*], [*value-2*], [*if-value-2*], …, [*default*])* ¶**

This macro was introduced in Autoconf 2.62. Similar to `m4_if`, except that each *test* is expanded only when it is encountered. This is useful for short-circuiting expensive tests; while `m4_if` requires all its strings to be expanded up front before doing comparisons, `m4_cond` only expands a *test* when all earlier tests have failed.

For an example, these two sequences give the same result, but in the case where ‘$1’ does not contain a backslash, the `m4_cond` version only expands `m4_index` once, instead of five times, for faster computation if this is a common case for ‘$1’. Notice that every third argument is unquoted for `m4_if`, and quoted for `m4_cond`:

```
m4_if(m4_index([$1], [\]), [-1], [$2],
      m4_eval(m4_index([$1], [\\]) >= 0), [1], [$2],
      m4_eval(m4_index([$1], [\$]) >= 0), [1], [$2],
      m4_eval(m4_index([$1], [\`]) >= 0), [1], [$3],
      m4_eval(m4_index([$1], [\"]) >= 0), [1], [$3],
      [$2])
m4_cond([m4_index([$1], [\])], [-1], [$2],
        [m4_eval(m4_index([$1], [\\]) >= 0)], [1], [$2],
        [m4_eval(m4_index([$1], [\$]) >= 0)], [1], [$2],
        [m4_eval(m4_index([$1], [\`]) >= 0)], [1], [$3],
        [m4_eval(m4_index([$1], [\"]) >= 0)], [1], [$3],
        [$2])
```

**Macro: **m4_default***(*expr-1*, *expr-2*)* ¶**

**Macro: **m4_default_quoted***(*expr-1*, *expr-2*)* ¶**

**Macro: **m4_default_nblank***(*expr-1*, [*expr-2*])* ¶**

**Macro: **m4_default_nblank_quoted***(*expr-1*, [*expr-2*])* ¶**

If *expr-1* contains text, use it. Otherwise, select *expr-2*. `m4_default` expands the result, while `m4_default_quoted` does not. Useful for providing a fixed default if the expression that results in *expr-1* would otherwise be empty. The difference between `m4_default` and `m4_default_nblank` is whether an argument consisting of just blanks (space, tab, newline) is significant. When using the expanding versions, note that an argument may contain text but still expand to an empty string.

```
m4_define([active], [ACTIVE])dnl
m4_define([empty], [])dnl
m4_define([demo1], [m4_default([$1], [$2])])dnl
m4_define([demo2], [m4_default_quoted([$1], [$2])])dnl
m4_define([demo3], [m4_default_nblank([$1], [$2])])dnl
m4_define([demo4], [m4_default_nblank_quoted([$1], [$2])])dnl
demo1([active], [default])
⇒ACTIVE
demo1([], [active])
⇒ACTIVE
demo1([empty], [text])
⇒
-demo1([ ], [active])-
⇒- -
demo2([active], [default])
⇒active
demo2([], [active])
⇒active
demo2([empty], [text])
⇒empty
-demo2([ ], [active])-
⇒- -
demo3([active], [default])
⇒ACTIVE
demo3([], [active])
⇒ACTIVE
demo3([empty], [text])
⇒
-demo3([ ], [active])-
⇒-ACTIVE-
demo4([active], [default])
⇒active
demo4([], [active])
⇒active
demo4([empty], [text])
⇒empty
-demo4([ ], [active])-
⇒-active-
```

**Macro: **m4_define_default***(*macro*, [*default-definition*])* ¶**

If *macro* does not already have a definition, then define it to *default-definition*.

**Macro: **m4_ifblank***(*cond*, [*if-blank*], [*if-text*])* ¶**

**Macro: **m4_ifnblank***(*cond*, [*if-text*], [*if-blank*])* ¶**

If *cond* is empty or consists only of blanks (space, tab, newline), then expand *if-blank*; otherwise, expand *if-text*. Two variants exist, in order to make it easier to select the correct logical sense when using only two parameters. Note that this is more efficient than the equivalent behavior of:

```
m4_ifval(m4_normalize([cond]), if-text, if-blank)
```

**Macro: **m4_ifndef***(*macro*, *if-not-defined*, [*if-defined*])* ¶**

This is shorthand for:

```
m4_ifdef([macro], [if-defined], [if-not-defined])
```

**Macro: **m4_ifset***(*macro*, [*if-true*], [*if-false*])* ¶**

If *macro* is undefined, or is defined as the empty string, expand to *if-false*. Otherwise, expands to *if-true*. Similar to:

```
m4_ifval(m4_defn([macro]), [if-true], [if-false])
```

except that it is not an error if *macro* is undefined.

**Macro: **m4_ifval***(*cond*, [*if-true*], [*if-false*])* ¶**

Expands to *if-true* if *cond* is not empty, otherwise to *if-false*. This is shorthand for:

```
m4_if([cond], [], [if-false], [if-true])
```

**Macro: **m4_ifvaln***(*cond*, [*if-true*], [*if-false*])* ¶**

Similar to `m4_ifval`, except guarantee that a newline is present after any non-empty expansion. Often followed by `dnl`.

**Macro: **m4_n***(*text*)* ¶**

Expand to *text*, and add a newline if *text* is not empty. Often followed by `dnl`.

#### 8.3.5 Looping constructs

The following macros are useful in implementing recursive algorithms in M4, including loop operations. An M4 list is formed by quoting a list of quoted elements; generally the lists are comma-separated, although `m4_foreach_w` is whitespace-separated. For example, the list ‘[[a], [b,c]]’ contains two elements: ‘[a]’ and ‘[b,c]’. It is common to see lists with unquoted elements when those elements are not likely to be macro names, as in ‘[fputc_unlocked, fgetc_unlocked]’.

Although not generally recommended, it is possible for quoted lists to have side effects; all side effects are expanded only once, and prior to visiting any list element. On the other hand, the fact that unquoted macros are expanded exactly once means that macros without side effects can be used to generate lists. For example,

```
m4_foreach([i], [[1], [2], [3]m4_errprintn([hi])], [i])
error→hi
⇒123
m4_define([list], [[1], [2], [3]])
⇒
m4_foreach([i], [list], [i])
⇒123
```

**Macro: **m4_argn***(*n*, [*arg*]…)* ¶**

Extracts argument *n* (larger than 0) from the remaining arguments. If there are too few arguments, the empty string is used. For any *n* besides 1, this is more efficient than the similar ‘m4_car(m4_shiftn([*n*], [], [*arg*…]))’.

**Macro: **m4_car***(*arg*…)* ¶**

Expands to the quoted first *arg*. Can be used with `m4_cdr` to recursively iterate through a list. Generally, when using quoted lists of quoted elements, `m4_car` should be called without any extra quotes.

**Macro: **m4_cdr***(*arg*…)* ¶**

Expands to a quoted list of all but the first *arg*, or the empty string if there was only one argument. Generally, when using quoted lists of quoted elements, `m4_cdr` should be called without any extra quotes.

For example, this is a simple implementation of `m4_map`; note how each iteration checks for the end of recursion, then merely applies the first argument to the first element of the list, then repeats with the rest of the list. (The actual implementation in M4sugar is a bit more involved, to gain some speed and share code with `m4_map_sep`, and also to avoid expanding side effects in ‘$2’ twice).

```
m4_define([m4_map], [m4_ifval([$2],
  [m4_apply([$1], m4_car($2))[]$0([$1], m4_cdr($2))])])dnl
m4_map([ m4_eval], [[[1]], [[1+1]], [[10],[16]]])
⇒ 1 2 a
```

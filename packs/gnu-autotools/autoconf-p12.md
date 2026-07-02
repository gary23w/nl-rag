---
title: "Autoconf (part 12/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 12/26
---

## 9 Programming in M4sh

M4sh, pronounced “mash”, is aiming at producing portable Bourne shell scripts. This name was coined by Lars J. Aas, who notes that, according to the Webster’s Revised Unabridged Dictionary (1913):

> Mash \Mash\, n. [Akin to G. meisch, maisch, meische, maische, mash, wash, and prob. to AS. miscian to mix. See “Mix”.]
> 
> 1. A mass of mixed ingredients reduced to a soft pulpy state by beating or pressure...
> 2. A mixture of meal or bran and water fed to animals.
> 3. A mess; trouble. [Obs.] –Beau. & Fl.

M4sh reserves the M4 macro namespace ‘^_AS_’ for internal use, and the namespace ‘^AS_’ for M4sh macros. It also reserves the shell and environment variable namespace ‘^as_’, and the here-document delimiter namespace ‘^_AS[A-Z]’ in the output file. You should not define your own macros or output shell code that conflicts with these namespaces.

### 9.1 Common Shell Constructs

M4sh provides portable alternatives for some common shell constructs that unfortunately are not portable in practice.

**Macro: **AS_BOX***(*text*, [*char* = ‘-’])* ¶**

Expand into shell code that will output *text* surrounded by a box with *char* in the top and bottom border. *text* should not contain a newline, but may contain shell expansions valid for unquoted here-documents. *char* defaults to ‘-’, but can be any character except ‘/’, ‘'’, ‘"’, ‘\’, ‘&’, or ‘`’. This is useful for outputting a comment box into log files to separate distinct phases of script operation.

**Macro: **AS_CASE***(*word*, [*pattern1*], [*if-matched1*], …, [*default*])* ¶**

Expand into a shell ‘case’ statement, where *word* is matched against one or more patterns. *if-matched* is run if the corresponding pattern matched *word*, else *default* is run. See Prerequisite Macros for why this macro should be used instead of plain ‘case’ in code outside of an `AC_DEFUN` macro, when the contents of the ‘case’ use `AC_REQUIRE` directly or indirectly. See Limitations of Shell Builtins, for how this macro avoids some portability issues. See Dealing with unbalanced parentheses for how this macro lets you write code with balanced parentheses even if your code must run on obsolescent shells.

**Macro: **AS_DIRNAME***(*file-name*)* ¶**

Output the directory portion of *file-name*. For example, if `$file` is ‘/one/two/three’, the command dir=`AS_DIRNAME(["$file"])` sets `dir` to ‘/one/two’.

`AS_DIRNAME` was designed long ago when the `dirname` command was not universally supported. Nowadays one can safely use dir=`dirname -- "$file"` instead. This interface may be improved in the future to avoid forks and losing trailing newlines.

**Macro: **AS_ECHO***(*word*)* ¶**

Emit *word* to the standard output, followed by a newline. The *word* must be a single shell word (typically a quoted string). Output the shell expansion of *word* as-is, even if it starts with ‘-’ or contains ‘\’. Redirections can be placed outside the macro invocation.

If the shell variable *foo* could contain ‘\’ or leading ‘-’. `AS_ECHO(["$foo"])` is more portable than `echo "$foo"`. See Limitations of Shell Builtins.

Also, `AS_ECHO(["$foo"])` is often easier to read than the ‘printf '%s\n' "$foo"’ that it stands for. However, because it employs ‘'’ characters, in contexts where ‘'’ is not allowed it is better to use `printf` directly. For example, ‘`eval 'foo=${'AS_ESCAPE([[$1]], [`\])'};printf "%s\\n" "$foo")'`’ would not work if `printf` were replaced with `AS_ECHO`.

**Macro: **AS_ECHO_N***(*word*)* ¶**

Act like `AS_ECHO(*word*)`, except do not output a following newline.

**Macro: **AS_ESCAPE***(*string*, [*chars* = ‘`\"$’])* ¶**

Expands to *string*, with any characters in *chars* escaped with a backslash (‘\’). *chars* should be at most four bytes long, and only contain characters from the set ‘`\"$’; however, characters may be safely listed more than once in *chars* for the sake of syntax highlighting editors. The current implementation expands *string* after adding escapes; if *string* contains macro calls that in turn expand to text needing shell quoting, you can use `AS_ESCAPE(m4_dquote(m4_expand([string])))`.

The default for *chars* (‘\"$`’) is the set of characters needing escapes when *string* will be used literally within double quotes. One common variant is the set of characters to protect when *string* will be used literally within back-ticks or an unquoted here-document (‘\$`’). Another common variant is ‘""’, which can be used to form a double-quoted string containing the same expansions that would have occurred if *string* were expanded in an unquoted here-document; however, when using this variant, care must be taken that *string* does not use double quotes within complex variable expansions (such as ‘${foo-`echo "hi"`}’) that would be broken with improper escapes.

This macro is often used with `AS_ECHO`. For an example, observe the output generated by the shell code generated from this snippet:

```
foo=bar
AS_ECHO(["AS_ESCAPE(["$foo" = ])AS_ESCAPE(["$foo"], [""])"])
⇒"$foo" = "bar"
m4_define([macro], [a, [\b]])
AS_ECHO(["AS_ESCAPE([[macro]])"])
⇒macro
AS_ECHO(["AS_ESCAPE([macro])"])
⇒a, b
AS_ECHO(["AS_ESCAPE(m4_dquote(m4_expand([macro])))"])
⇒a, \b
```

To escape a string that will be placed within single quotes, use:

```
m4_bpatsubst([[string]], ['], ['\\''])
```

**Macro: **AS_EXECUTABLE_P***(*file*)* ¶**

Emit code to probe whether *file* is a regular file with executable permissions (and not a directory with search permissions). The caller is responsible for quoting *file*.

**Macro: **AS_EXIT***([*status* = ‘$?’])* ¶**

Emit code to exit the shell with *status*, defaulting to ‘$?’. This macro works around shells that see the exit status of the command prior to `exit` inside a ‘trap 0’ handler (see Limitations of Shell Builtins).

**Macro: **AS_IF***(*test1*, [*run-if-true1*], …, [*run-if-false*])* ¶**

Run shell code *test1*. If *test1* exits with a zero status then run shell code *run-if-true1*, else examine further tests. If no test exits with a zero status, run shell code *run-if-false*, with simplifications if either *run-if-true1* or *run-if-false* is empty. For example,

```
AS_IF([test "x$foo" = xyes], [HANDLE_FOO([yes])],
      [test "x$foo" != xno], [HANDLE_FOO([maybe])],
      [echo foo not specified])
```

ensures any required macros of `HANDLE_FOO` are expanded before the first test.

This macro should be used instead of plain ‘if’ in code outside of an `AC_DEFUN` macro, when the contents of the ‘if’ use `AC_REQUIRE` directly or indirectly (see Prerequisite Macros).

**Macro: **AS_MKDIR_P***(*file-name*)* ¶**

Make the directory *file-name*, including intervening directories as necessary. This is equivalent to ‘mkdir -p -- *file-name*’. If creation of *file-name* fails, exit the script.

Also see the `AC_PROG_MKDIR_P` macro (see Particular Program Checks).

**Macro: **AS_SET_STATUS***(*status*)* ¶**

Emit shell code to set the value of ‘$?’ to *status*, as efficiently as possible. However, this is not guaranteed to abort a shell running with `set -e` (see Limitations of Shell Builtins). This should also be used at the end of a complex shell function instead of ‘return’ (see Shell Functions) to avoid a DJGPP shell bug.

**Macro: **AS_TR_CPP***(*expression*)* ¶**

Transform *expression* into a valid right-hand side for a C `#define`. For example:

```
# This outputs "#define HAVE_CHAR_P 1".
# Notice the m4 quoting around #, to prevent an m4 comment
type="char *"
echo "[#]define AS_TR_CPP([HAVE_$type]) 1"
```

**Macro: **AS_TR_SH***(*expression*)* ¶**

Transform *expression* into shell code that generates a valid shell variable name. The result is literal when possible at m4 time, but must be used with `eval` if *expression* causes shell indirections. For example:

```
# This outputs "Have it!".
header="sys/some file.h"
eval AS_TR_SH([HAVE_$header])=yes
if test "x$HAVE_sys_some_file_h" = xyes; then echo "Have it!"; fi
```

**Macro: **AS_SET_CATFILE***(*var*, *dir*, *file*)* ¶**

Set the polymorphic shell variable *var* to *dir*/*file*, but optimizing the common cases (*dir* or *file* is ‘.’, *file* is absolute, etc.).

**Macro: **AS_UNSET***(*var*)* ¶**

Unsets the shell variable *var*, working around bugs in older shells (see Limitations of Shell Builtins). *var* can be a literal or indirect variable name.

**Macro: **AS_VERSION_COMPARE***(*version-1*, *version-2*, [*action-if-less*], [*action-if-equal*], [*action-if-greater*])* ¶**

Compare two strings *version-1* and *version-2*, possibly containing shell variables, as version strings, and expand *action-if-less*, *action-if-equal*, or *action-if-greater* depending upon the result. The algorithm to compare is similar to the one used by strverscmp in glibc (see String/Array Comparison in *The GNU C Library*).

### 9.2 Support for indirect variable names

Often, it is convenient to write a macro that will emit shell code operating on a shell variable. The simplest case is when the variable name is known. But a more powerful idiom is writing shell code that can work through an indirection, where another variable or command substitution produces the name of the variable to actually manipulate. M4sh supports the notion of polymorphic shell variables, making it easy to write a macro that can deal with either literal or indirect variable names and output shell code appropriate for both use cases. Behavior is undefined if expansion of an indirect variable does not result in a literal variable name.

**Macro: **AS_LITERAL_IF***(*expression*, [*if-literal*], [*if-not*], [*if-simple-ref* = *if-not*])* ¶**

**Macro: **AS_LITERAL_WORD_IF***(*expression*, [*if-literal*], [*if-not*], [*if-simple-ref* = *if-not*])* ¶**

If the expansion of *expression* is definitely a shell literal, expand *if-literal*. If the expansion of *expression* looks like it might contain shell indirections (such as `$var` or `expr`), then *if-not* is expanded. Sometimes, it is possible to output optimized code if *expression* consists only of shell variable expansions (such as `${var}`), in which case *if-simple-ref* can be provided; but defaulting to *if-not* should always be safe. `AS_LITERAL_WORD_IF` only expands *if-literal* if *expression* looks like a single shell word, containing no whitespace; while `AS_LITERAL_IF` allows whitespace in *expression*.

In order to reduce the time spent recognizing whether an *expression* qualifies as a literal or a simple indirection, the implementation is somewhat conservative: *expression* must be a single shell word (possibly after stripping whitespace), consisting only of bytes that would have the same meaning whether unquoted or enclosed in double quotes (for example, ‘a.b’ results in *if-literal*, even though it is not a valid shell variable name; while both ‘'a'’ and ‘[$]’ result in *if-not*, because they behave differently than ‘"'a'"’ and ‘"[$]"’). This macro can be used in contexts for recognizing portable file names (such as in the implementation of `AC_LIBSOURCE`), or coupled with some transliterations for forming valid variable names (such as in the implementation of `AS_TR_SH`, which uses an additional `m4_translit` to convert ‘.’ to ‘_’).

This example shows how to read the contents of the shell variable `bar`, exercising all three arguments to `AS_LITERAL_IF`. It results in a script that will output the line ‘hello’ three times.

```
AC_DEFUN([MY_ACTION],
[AS_LITERAL_IF([$1],
  [AS_ECHO(["$$1"])],
  [AS_VAR_COPY([var], [$1])
   AS_ECHO(["$var"])],
  [AS_ECHO(["$'"$1"\"])])])
foo=bar bar=hello
MY_ACTION([bar])
MY_ACTION([`echo bar`])
MY_ACTION([$foo])
```

**Macro: **AS_VAR_APPEND***(*var*, *text*)* ¶**

Emit shell code to append the shell expansion of *text* to the end of the current contents of the polymorphic shell variable *var*, taking advantage of shells that provide the ‘+=’ extension for more efficient scaling.

For situations where the final contents of *var* are relatively short (less than 256 bytes), it is more efficient to use the simpler code sequence of `*var*=${*var*}*text*` (or its polymorphic equivalent of `AS_VAR_COPY([t], [*var*])` and `AS_VAR_SET([*var*], ["$t"*text*])`). But in the case when the script will be repeatedly appending text into `var`, issues of scaling start to become apparent. A naive implementation requires execution time linear to the length of the current contents of *var* as well as the length of *text* for a single append, for an overall quadratic scaling with multiple appends. This macro takes advantage of shells which provide the extension `*var*+=*text*`, which can provide amortized constant time for a single append, for an overall linear scaling with multiple appends. Note that unlike `AS_VAR_SET`, this macro requires that *text* be quoted properly to avoid field splitting and file name expansion.

**Macro: **AS_VAR_ARITH***(*var*, *expression*)* ¶**

Emit shell code to compute the arithmetic expansion of *expression*, assigning the result as the contents of the polymorphic shell variable *var*. The code takes advantage of shells that provide ‘$(())’ for fewer forks, but uses `expr` as a fallback. Therefore, the syntax for a valid *expression* is rather limited: all operators must occur as separate shell arguments and with proper quoting; the only operators supported are ‘*’, ‘/’, ‘%’, binary ‘+’, binary ‘-’, ‘>’, ‘>=’, ‘<’, ‘<=’, ‘!=’, ‘&’, and ‘|’; all variables containing numbers must be expanded prior to the computation; the first shell argument must not start with ‘-’; and each number must be an optional ‘-’ followed by one or more decimal digits, where the first digit is nonzero if there is more than one digit. In the following example, this snippet will print ‘(2+3)*4 == 20’.

```
bar=3
AS_VAR_ARITH([foo], [\( 2 + $bar \) \* 4])
echo "(2+$bar)*4 == $foo"
```

**Macro: **AS_VAR_COPY***(*dest*, *source*)* ¶**

Emit shell code to assign the contents of the polymorphic shell variable *source* to the polymorphic shell variable *dest*. For example, executing this M4sh snippet will output ‘bar hi’:

```
foo=bar bar=hi
AS_VAR_COPY([a], [foo])
AS_VAR_COPY([b], [$foo])
echo "$a $b"
```

When it is necessary to access the contents of an indirect variable inside a shell double-quoted context, the recommended idiom is to first copy the contents into a temporary literal shell variable.

```
for header in stdint_h inttypes_h ; do
  AS_VAR_COPY([var], [ac_cv_header_$header])
  AS_ECHO(["$header detected: $var"])
done
```

**Macro: **AS_VAR_IF***(*var*, [*word*], [*if-equal*], [*if-not-equal*])* ¶**

Output a shell conditional statement. If the contents of the polymorphic shell variable *var* match the string *word*, execute *if-equal*; otherwise execute *if-not-equal*. *word* must be a single shell word (typically a quoted string). Avoids shell bugs if an interrupt signal arrives while a command substitution in *var* is being expanded.

**Macro: **AS_VAR_PUSHDEF***(*m4-name*, *value*)* ¶**

**Macro: **AS_VAR_POPDEF***(*m4-name*)* ¶**

A common M4sh idiom involves composing shell variable names from an m4 argument (for example, writing a macro that uses a cache variable). *value* can be an arbitrary string, which will be transliterated into a valid shell name by `AS_TR_SH`. In order to access the composed variable name based on *value*, it is easier to declare a temporary m4 macro *m4-name* with `AS_VAR_PUSHDEF`, then use that macro as the argument to subsequent `AS_VAR` macros as a polymorphic variable name, and finally free the temporary macro with `AS_VAR_POPDEF`. These macros are often followed with `dnl`, to avoid excess newlines in the output.

Here is an involved example, that shows the power of writing macros that can handle composed shell variable names:

```
m4_define([MY_CHECK_HEADER],
[AS_VAR_PUSHDEF([my_Header], [ac_cv_header_$1])dnl
AS_VAR_IF([my_Header], [yes], [echo "header $1 detected"])dnl
AS_VAR_POPDEF([my_Header])dnl
])
MY_CHECK_HEADER([stdint.h])
for header in inttypes.h stdlib.h ; do
  MY_CHECK_HEADER([$header])
done
```

In the above example, `MY_CHECK_HEADER` can operate on polymorphic variable names. In the first invocation, the m4 argument is `stdint.h`, which transliterates into a literal `stdint_h`. As a result, the temporary macro `my_Header` expands to the literal shell name ‘ac_cv_header_stdint_h’. In the second invocation, the m4 argument to `MY_CHECK_HEADER` is `$header`, and the temporary macro `my_Header` expands to the indirect shell name ‘$as_my_Header’. During the shell execution of the for loop, when ‘$header’ contains ‘inttypes.h’, then ‘$as_my_Header’ contains ‘ac_cv_header_inttypes_h’. If this script is then run on a platform where all three headers have been previously detected, the output of the script will include:

```
header stdint.h detected
header inttypes.h detected
header stdlib.h detected
```

**Macro: **AS_VAR_SET***(*var*, [*value*])* ¶**

Emit shell code to assign the contents of the polymorphic shell variable *var* to the shell expansion of *value*. *value* is not subject to field splitting or file name expansion, so if command substitution is used, it may be done with ‘`""`’ rather than using an intermediate variable (see Shell Substitutions). However, *value* does undergo rescanning for additional macro names; behavior is unspecified if late expansion results in any shell meta-characters.

**Macro: **AS_VAR_SET_IF***(*var*, [*if-set*], [*if-undef*])* ¶**

Emit a shell conditional statement, which executes *if-set* if the polymorphic shell variable `var` is set to any value, and *if-undef* otherwise.

**Macro: **AS_VAR_TEST_SET***(*var*)* ¶**

Emit a shell statement that results in a successful exit status only if the polymorphic shell variable `var` is set.

### 9.3 Initialization Macros

**Macro: **AS_BOURNE_COMPATIBLE** ¶**

Set up the shell to be more compatible with the Bourne shell as standardized by POSIX, if possible. This may involve setting environment variables, or setting options, or similar implementation-specific actions. This macro is deprecated, since `AS_INIT` already invokes it.

**Macro: **AS_INIT** ¶**

Initialize the M4sh environment. This macro calls `m4_init`, then outputs the `#! /bin/sh` line, a notice about where the output was generated from, and code to sanitize the environment for the rest of the script. Among other initializations, this sets `SHELL` to the shell chosen to run the script (see CONFIG_SHELL), and `LC_ALL` to ensure the C locale. Finally, it changes the current diversion to `BODY`. `AS_INIT` is called automatically by `AC_INIT` and `AT_INIT`, so shell code in configure, config.status, and testsuite all benefit from a sanitized shell environment.

**Macro: **AS_INIT_GENERATED***(*file*, [*comment*])* ¶**

Emit shell code to start the creation of a subsidiary shell script in *file*, including changing *file* to be executable. This macro populates the child script with information learned from the parent (thus, the emitted code is equivalent in effect, but more efficient, than the code output by `AS_INIT`, `AS_BOURNE_COMPATIBLE`, and `AS_SHELL_SANITIZE`). If present, *comment* is output near the beginning of the child, prior to the shell initialization code, and is subject to parameter expansion, command substitution, and backslash quote removal. The parent script should check the exit status after this macro, in case *file* could not be properly created (for example, if the disk was full). If successfully created, the parent script can then proceed to append additional M4sh constructs into the child script.

Note that the child script starts life without a log file open, so if the parent script uses logging (see AS_MESSAGE_LOG_FD), you must temporarily disable any attempts to use the log file until after emitting code to open a log within the child. On the other hand, if the parent script has `AS_MESSAGE_FD` redirected somewhere besides ‘1’, then the child script already has code that copies stdout to that descriptor. Currently, the suggested idiom for writing a M4sh shell script from within another script is:

```
AS_INIT_GENERATED([file], [[# My child script.
]]) || { AS_ECHO(["Failed to create child script"]); AS_EXIT; }
m4_pushdef([AS_MESSAGE_LOG_FD])dnl
cat >> "file" <<\__EOF__
# Code to initialize AS_MESSAGE_LOG_FD
m4_popdef([AS_MESSAGE_LOG_FD])dnl
# Additional code
__EOF__
```

This, however, may change in the future as the M4sh interface is stabilized further.

Also, be aware that use of `LINENO` within the child script may report line numbers relative to their location in the parent script, even when using `AS_LINENO_PREPARE`, if the parent script was unable to locate a shell with working `LINENO` support.

**Macro: **AS_LINENO_PREPARE** ¶**

Find a shell that supports the special variable `LINENO`, which contains the number of the currently executing line. This macro is automatically invoked by `AC_INIT` in configure scripts.

**Macro: **AS_ME_PREPARE** ¶**

Set up variable `as_me` to be the basename of the currently executing script. This macro is automatically invoked by `AC_INIT` in configure scripts.

**Macro: **AS_TMPDIR***(*prefix*, [*dir* = ‘${TMPDIR:=/tmp}’])* ¶**

Create, as safely as possible, a temporary sub-directory within *dir* with a name starting with *prefix*. *prefix* should be 2–4 characters, to make it slightly easier to identify the owner of the directory. If *dir* is omitted, then the value of `TMPDIR` will be used (defaulting to ‘/tmp’). On success, the name of the newly created directory is stored in the shell variable `tmp`. On error, the script is aborted.

Typically, this macro is coupled with some exit traps to delete the created directory and its contents on exit or interrupt. However, there is a slight window between when the directory is created and when the name is actually known to the shell, so an interrupt at the right moment might leave the temporary directory behind. Hence it is important to use a *prefix* that makes it easier to determine if a leftover temporary directory from an interrupted script is safe to delete.

If you set `TMPDIR=$tmp` after invoking this macro, you should reset `TMPDIR` before deleting the created directory, to avoid breaking commands that rely on `$TMPDIR`.

The use of the output variable ‘$tmp’ rather than something in the ‘as_’ namespace is historical; it has the unfortunate consequence that reusing this otherwise common name for any other purpose inside your script has the potential to break any cleanup traps designed to remove the temporary directory.

**Macro: **AS_SHELL_SANITIZE** ¶**

Initialize the shell suitably for `configure` scripts. This has the effect of `AS_BOURNE_COMPATIBLE`, and sets some other environment variables for predictable results from configuration tests. For example, it sets `LC_ALL` to change to the default C locale. See Special Shell Variables. This macro is deprecated, since `AS_INIT` already invokes it.

### 9.4 File Descriptor Macros

The following macros define file descriptors used to output messages (or input values) from configure scripts. For example:

```
AS_ECHO(["$wombats found"]) >&AS_MESSAGE_LOG_FD
AS_ECHO_N(['Enter desired kangaroo count: ']) >&AS_MESSAGE_FD
read kangaroos <&AS_ORIGINAL_STDIN_FD
```

However doing so is seldom needed, because Autoconf provides higher level macros as described below.

**Macro: **AS_MESSAGE_FD** ¶**

The file descriptor for ‘checking for...’ messages and results. By default, `AS_INIT` sets this to ‘1’ for standalone M4sh clients. However, `AC_INIT` shuffles things around to another file descriptor, in order to allow the -q option of `configure` to choose whether messages should go to the script’s standard output or be discarded.

If you want to display some messages, consider using one of the printing macros (see Printing Messages) instead. Copies of messages output via these macros are also recorded in config.log.

**Macro: **AS_MESSAGE_LOG_FD** ¶**

This must either be empty, or expand to a file descriptor for log messages. By default, `AS_INIT` sets this macro to the empty string for standalone M4sh clients, thus disabling logging. However, `AC_INIT` shuffles things around so that both `configure` and `config.status` use config.log for log messages. Macros that run tools, like `AC_COMPILE_IFELSE` (see Running the Compiler), redirect all output to this descriptor. You may want to do so if you develop such a low-level macro.

**Macro: **AS_ORIGINAL_STDIN_FD** ¶**

This must expand to a file descriptor for the original standard input. By default, `AS_INIT` sets this macro to ‘0’ for standalone M4sh clients. However, `AC_INIT` shuffles things around for safety.

When `configure` runs, it may accidentally execute an interactive command that has the same name as the non-interactive meant to be used or checked. If the standard input was the terminal, such interactive programs would cause `configure` to stop, pending some user input. Therefore `configure` redirects its standard input from /dev/null during its initialization. This is not normally a problem, since `configure` normally does not need user input.

In the extreme case where your configure script really needs to obtain some values from the original standard input, you can read them explicitly from `AS_ORIGINAL_STDIN_FD`.

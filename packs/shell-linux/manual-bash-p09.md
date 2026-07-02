---
title: "Bash Reference Manual (part 9/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 9/15
---

# Bash Reference Manual

conditional operator

**`= *= /= %= += -= <<= >>= &= ^= |=`**

assignment

**`expr1 , expr2`**

comma

Shell variables are allowed as operands; parameter expansion is performed before the expression is evaluated. Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax. This means you can use *x*, where *x* is a shell variable name, in an arithmetic expression, and the shell will evaluate its value as an expression and use the result. A shell variable that is null or unset evaluates to 0 when referenced by name in an expression.

The value of a variable is evaluated as an arithmetic expression when it is referenced, or when a variable which has been given the `integer` attribute using ‘declare -i’ is assigned a value. A null value evaluates to 0. A shell variable need not have its `integer` attribute turned on to be used in an expression.

Integer constants follow the C language definition, without suffixes or character constants. Constants with a leading 0 are interpreted as octal numbers. A leading ‘0x’ or ‘0X’ denotes hexadecimal. Otherwise, numbers take the form [*base*`#`]*n*, where the optional *base* is a decimal number between 2 and 64 representing the arithmetic base, and *n* is a number in that base. If *base*`#` is omitted, then base 10 is used. When specifying *n*, if a non-digit is required, the digits greater than 9 are represented by the lowercase letters, the uppercase letters, ‘@’, and ‘_’, in that order. If *base* is less than or equal to 36, lowercase and uppercase letters may be used interchangeably to represent numbers between 10 and 35.

Operators are evaluated in precedence order. Sub-expressions in parentheses are evaluated first and may override the precedence rules above.

### 6.6 Aliases

*Aliases* allow a string to be substituted for a word that is in a position in the input where it can be the first word of a simple command. Aliases have names and corresponding values that are set and unset using the `alias` and `unalias` builtin commands (see Shell Builtin Commands).

If the shell reads an unquoted word in the right position, it checks the word to see if it matches an alias name. If it matches, the shell replaces the word with the alias value, and reads that value as if it had been read instead of the word. The shell doesn’t look at any characters following the word before attempting alias substitution.

The characters ‘/’, ‘$’, ‘`’, ‘=’ and any of the shell metacharacters or quoting characters listed above may not appear in an alias name. The replacement text may contain any valid shell input, including shell metacharacters. The first word of the replacement text is tested for aliases, but a word that is identical to an alias being expanded is not expanded a second time. This means that one may alias `ls` to `"ls -F"`, for instance, and Bash does not try to recursively expand the replacement text.

If the last character of the alias value is a `blank`, then the shell checks the next command word following the alias for alias expansion.

Aliases are created and listed with the `alias` command, and removed with the `unalias` command.

There is no mechanism for using arguments in the replacement text, as in `csh`. If arguments are needed, use a shell function (see Shell Functions) instead.

Aliases are not expanded when the shell is not interactive, unless the `expand_aliases` shell option is set using `shopt` (see The Shopt Builtin).

The rules concerning the definition and use of aliases are somewhat confusing. Bash always reads at least one complete line of input, and all lines that make up a compound command, before executing any of the commands on that line or the compound command. Aliases are expanded when a command is read, not when it is executed. Therefore, an alias definition appearing on the same line as another command does not take effect until the shell reads the next line of input, and an alias definition in a compound command does not take effect until the shell parses and executes the entire compound command. The commands following the alias definition on that line, or in the rest of a compound command, are not affected by the new alias. This behavior is also an issue when functions are executed. Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a command. As a consequence, aliases defined in a function are not available until after that function is executed. To be safe, always put alias definitions on a separate line, and do not use `alias` in compound commands.

For almost every purpose, shell functions are preferable to aliases.

### 6.7 Arrays

Bash provides one-dimensional indexed and associative array variables. Any variable may be used as an indexed array; the `declare` builtin explicitly declares an array. There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously. Indexed arrays are referenced using arithmetic expressions that must expand to an integer (see Shell Arithmetic)) and are zero-based; associative arrays use arbitrary strings. Unless otherwise noted, indexed array indices must be non-negative integers.

The shell performs parameter and variable expansion, arithmetic expansion, command substitution, and quote removal on indexed array subscripts. Since this can potentially result in empty strings, subscript indexing treats those as expressions that evaluate to 0.

The shell performs tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, and quote removal on associative array subscripts. Empty strings cannot be used as associative array keys.

Bash automatically creates an indexed array if any variable is assigned to using the syntax

```
name[subscript]=value
```

The *subscript* is treated as an arithmetic expression that must evaluate to a number greater than or equal to zero. To explicitly declare an indexed array, use

```
declare -a name
```

(see Bash Builtin Commands). The syntax

```
declare -a name[subscript]
```

is also accepted; the *subscript* is ignored.

Associative arrays are created using

```
declare -A name
```

Attributes may be specified for an array variable using the `declare` and `readonly` builtins. Each attribute applies to all members of an array.

Arrays are assigned using compound assignments of the form

```
name=(value1 value2 ... )
```

where each *value* may be of the form `[*subscript*]=`*string*. Indexed array assignments do not require anything but *string*.

Each *value* in the list undergoes the shell expansions described above (see Shell Expansions), but *value*s that are valid variable assignments including the brackets and subscript do not undergo brace expansion and word splitting, as with individual variable assignments.

When assigning to indexed arrays, if the optional subscript is supplied, that index is assigned to; otherwise the index of the element assigned is the last index assigned to by the statement plus one. Indexing starts at zero.

When assigning to an associative array, the words in a compound assignment may be either assignment statements, for which the subscript is required, or a list of words that is interpreted as a sequence of alternating keys and values: *name*=(*key1* *value1* *key2* *value2* … ). These are treated identically to *name*=( [*key1*]=*value1* [*key2*]=*value2* … ). The first word in the list determines how the remaining words are interpreted; all assignments in a list must be of the same type. When using key/value pairs, the keys may not be missing or empty; a final missing value is treated like the empty string.

This syntax is also accepted by the `declare` builtin. Individual array elements may be assigned to using the `*name*[*subscript*]=*value*` syntax introduced above.

When assigning to an indexed array, if *name* is subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of *name*, so negative indices count back from the end of the array, and an index of -1 references the last element.

The ‘+=’ operator appends to an array variable when assigning using the compound assignment syntax; see Shell Parameters above.

An array element is referenced using `${*name*[*subscript*]}`. The braces are required to avoid conflicts with the shell’s filename expansion operators. If the *subscript* is ‘@’ or ‘*’, the word expands to all members of the array *name*, unless otherwise noted in the description of a builtin or word expansion. These subscripts differ only when the word appears within double quotes. If the word is double-quoted, `${*name*[*]}` expands to a single word with the value of each array member separated by the first character of the `IFS` variable, and `${*name*[@]}` expands each element of *name* to a separate word. When there are no array members, `${*name*[@]}` expands to nothing. If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the expansion of the original word, and the expansion of the last parameter is joined with the last part of the expansion of the original word. This is analogous to the expansion of the special parameters ‘@’ and ‘*’.

`${#*name*[*subscript*]}` expands to the length of `${*name*[*subscript*]}`. If *subscript* is ‘@’ or ‘*’, the expansion is the number of elements in the array.

If the *subscript* used to reference an element of an indexed array evaluates to a number less than zero, it is interpreted as relative to one greater than the maximum index of the array, so negative indices count back from the end of the array, and an index of -1 refers to the last element.

Referencing an array variable without a subscript is equivalent to referencing with a subscript of 0. Any reference to a variable using a valid subscript is valid; Bash creates an array if necessary.

An array variable is considered set if a subscript has been assigned a value. The null string is a valid value.

It is possible to obtain the keys (indices) of an array as well as the values. ${!*name*[@]} and ${!*name*[*]} expand to the indices assigned in array variable *name*. The treatment when in double quotes is similar to the expansion of the special parameters ‘@’ and ‘*’ within double quotes.

The `unset` builtin is used to destroy arrays. `unset *name*[*subscript*]` unsets the array element at index *subscript*. Negative subscripts to indexed arrays are interpreted as described above. Unsetting the last element of an array variable does not unset the variable. `unset *name*`, where *name* is an array, removes the entire array. `unset *name*[*subscript*]` behaves differently depending on the array type when *subscript* is ‘*’ or ‘@’. When *name* is an associative array, it removes the element with key ‘*’ or ‘@’. If *name* is an indexed array, `unset` removes all of the elements, but does not remove the array itself.

When using a variable name with a subscript as an argument to a command, such as with `unset`, without using the word expansion syntax described above (e.g., unset a[4]), the argument is subject to the shell’s filename expansion. Quote the argument if pathname expansion is not desired (e.g., unset ’a[4]’).

The `declare`, `local`, and `readonly` builtins each accept a -a option to specify an indexed array and a -A option to specify an associative array. If both options are supplied, -A takes precedence. The `read` builtin accepts a -a option to assign a list of words read from the standard input to an array, and can read values from the standard input into individual array elements. The `set` and `declare` builtins display array values in a way that allows them to be reused as input. Other builtins accept array name arguments as well (e.g., `mapfile`); see the descriptions of individual builtins for details. The shell provides a number of builtin array variables.

### 6.8 The Directory Stack

The directory stack is a list of recently-visited directories. The `pushd` builtin adds directories to the stack as it changes the current directory, and the `popd` builtin removes specified directories from the stack and changes the current directory to the directory removed. The `dirs` builtin displays the contents of the directory stack. The current directory is always the "top" of the directory stack.

The contents of the directory stack are also visible as the value of the `DIRSTACK` shell variable.

#### 6.8.1 Directory Stack Builtins

**`dirs` ¶**

```
dirs [-clpv] [+N | -N]
```

Without options, display the list of currently remembered directories. Directories are added to the list with the `pushd` command; the `popd` command removes directories from the list. The current directory is always the first directory in the stack.

Options, if supplied, have the following meanings:

**`-c`**

Clears the directory stack by deleting all of the elements.

**`-l`**

Produces a listing using full pathnames; the default listing format uses a tilde to denote the home directory.

**`-p`**

Causes `dirs` to print the directory stack with one entry per line.

**`-v`**

Causes `dirs` to print the directory stack with one entry per line, prefixing each entry with its index in the stack.

**`+*N*`**

Displays the *N*th directory (counting from the left of the list printed by `dirs` when invoked without options), starting with zero.

**`-*N*`**

Displays the *N*th directory (counting from the right of the list printed by `dirs` when invoked without options), starting with zero.

**`popd` ¶**

```
popd [-n] [+N | -N]
```

Remove elements from the directory stack. The elements are numbered from 0 starting at the first directory listed by `dirs`; that is, `popd` is equivalent to `popd +0`.

When no arguments are given, `popd` removes the top directory from the stack and changes to the new top directory.

Arguments, if supplied, have the following meanings:

**`-n`**

Suppress the normal change of directory when removing directories from the stack, only manipulate the stack.

**`+*N*`**

Remove the *N*th directory (counting from the left of the list printed by `dirs`), starting with zero, from the stack.

**`-*N*`**

Remove the *N*th directory (counting from the right of the list printed by `dirs`), starting with zero, from the stack.

If the top element of the directory stack is modified, and the -n option was not supplied, `popd` uses the `cd` builtin to change to the directory at the top of the stack. If the `cd` fails, `popd` returns a non-zero value.

Otherwise, `popd` returns an unsuccessful status if an invalid option is specified, the directory stack is empty, or *N* specifies a non-existent directory stack entry.

If the `popd` command is successful, Bash runs `dirs` to show the final contents of the directory stack, and the return status is 0.

**`pushd` ¶**

```
pushd [-n] [+N | -N | dir]
```

Add a directory to the top of the directory stack, or rotate the stack, making the new top of the stack the current working directory. With no arguments, `pushd` exchanges the top two elements of the directory stack.

Arguments, if supplied, have the following meanings:

**`-n`**

Suppress the normal change of directory when rotating or adding directories to the stack, only manipulate the stack.

**`+*N*`**

Rotate the stack so that the *N*th directory (counting from the left of the list printed by `dirs`, starting with zero) is at the top.

**`-*N*`**

Rotate the stack so that the *N*th directory (counting from the right of the list printed by `dirs`, starting with zero) is at the top.

**`*dir*`**

Make *dir* be the top of the stack.

After the stack has been modified, if the -n option was not supplied, `pushd` uses the `cd` builtin to change to the directory at the top of the stack. If the `cd` fails, `pushd` returns a non-zero value.

Otherwise, if no arguments are supplied, `pushd` returns zero unless the directory stack is empty. When rotating the directory stack, `pushd` returns zero unless the directory stack is empty or *N* specifies a non-existent directory stack element.

If the `pushd` command is successful, Bash runs `dirs` to show the final contents of the directory stack.

### 6.9 Controlling the Prompt

In addition, the following table describes the special characters which can appear in the prompt variables `PS0`, `PS1`, `PS2`, and `PS4`:

**`\a`**

A bell character.

**`\d`**

The date, in "Weekday Month Date" format (e.g., "Tue May 26").

**`\D{*format*}`**

The *format* is passed to `strftime`(3) and the result is inserted into the prompt string; an empty *format* results in a locale-specific time representation. The braces are required.

**`\e`**

An escape character.

**`\h`**

The hostname, up to the first ‘.’.

**`\H`**

The hostname.

**`\j`**

The number of jobs currently managed by the shell.

**`\l`**

The basename of the shell’s terminal device name (e.g., "ttys0").

**`\n`**

A newline.

**`\r`**

A carriage return.

**`\s`**

The name of the shell: the basename of `$0` (the portion following the final slash).

**`\t`**

The time, in 24-hour HH:MM:SS format.

**`\T`**

The time, in 12-hour HH:MM:SS format.

**`\@`**

The time, in 12-hour am/pm format.

**`\A`**

The time, in 24-hour HH:MM format.

**`\u`**

The username of the current user.

**`\v`**

The Bash version (e.g., 2.00).

**`\V`**

The Bash release, version + patchlevel (e.g., 2.00.0).

**`\w`**

The value of the `PWD` shell variable (`$PWD`), with `$HOME` abbreviated with a tilde (uses the `$PROMPT_DIRTRIM` variable).

**`\W`**

The basename of `$PWD`, with `$HOME` abbreviated with a tilde.

**`\!`**

The history number of this command.

**`\#`**

The command number of this command.

**`\$`**

If the effective uid is 0, `#`, otherwise `$`.

**`\*nnn*`**

The character whose ASCII code is the octal value *nnn*.

**`\\`**

A backslash.

**`\[`**

Begin a sequence of non-printing characters. Thiss could be used to embed a terminal control sequence into the prompt.

**`\]`**

End a sequence of non-printing characters.

The command number and the history number are usually different: the history number of a command is its position in the history list, which may include commands restored from the history file (see Bash History Facilities), while the command number is the position in the sequence of commands executed during the current shell session.

After the string is decoded, it is expanded via parameter expansion, command substitution, arithmetic expansion, and quote removal, subject to the value of the `promptvars` shell option (see The Shopt Builtin). This can have unwanted side effects if escaped portions of the string appear within command substitution or contain characters special to word expansion.

### 6.10 The Restricted Shell

If Bash is started with the name `rbash`, or the --restricted or -r option is supplied at invocation, the shell becomes *restricted*. A restricted shell is used to set up an environment more controlled than the standard shell. A restricted shell behaves identically to `bash` with the exception that the following are disallowed or not performed:

- Changing directories with the `cd` builtin.
- Setting or unsetting the values of the `SHELL`, `PATH`, `HISTFILE`, `ENV`, or `BASH_ENV` variables.
- Specifying command names containing slashes.
- Specifying a filename containing a slash as an argument to the `.` builtin command.
- Using the -p option to the `.` builtin command to specify a search path.
- Specifying a filename containing a slash as an argument to the `history` builtin command.
- Specifying a filename containing a slash as an argument to the -p option to the `hash` builtin command.
- Importing function definitions from the shell environment at startup.
- Parsing the value of `SHELLOPTS` from the shell environment at startup.
- Redirecting output using the ‘>’, ‘>|’, ‘<>’, ‘>&’, ‘&>’, and ‘>>’ redirection operators.
- Using the `exec` builtin to replace the shell with another command.
- Adding or deleting builtin commands with the -f and -d options to the `enable` builtin.
- Using the `enable` builtin command to enable disabled shell builtins.
- Specifying the -p option to the `command` builtin.
- Turning off restricted mode with ‘set +r’ or ‘shopt -u restricted_shell’.

These restrictions are enforced after any startup files are read.

When a command that is found to be a shell script is executed (see Shell Scripts), `rbash` turns off any restrictions in the shell spawned to execute the script.

The restricted shell mode is only one component of a useful restricted environment. It should be accompanied by setting `PATH` to a value that allows execution of only a few verified commands (commands that allow shell escapes are particularly vulnerable), changing the current directory to a non-writable directory other than `$HOME` after login, not allowing the restricted shell to execute shell scripts, and cleaning the environment of variables that cause some commands to modify their behavior (e.g., `VISUAL` or `PAGER`).

Modern systems provide more secure ways to implement a restricted environment, such as `jails`, `zones`, or `containers`.

### 6.11 Bash and POSIX

#### 6.11.1 What is POSIX?

POSIX is the name for a family of standards based on Unix. A number of Unix services, tools, and functions are part of the standard, ranging from the basic system calls and C library functions to common applications and tools to system administration and management.

The POSIX Shell and Utilities standard was originally developed by IEEE Working Group 1003.2 (POSIX.2). The first edition of the 1003.2 standard was published in 1992. It was merged with the original IEEE 1003.1 Working Group and is currently maintained by the Austin Group (a joint working group of the IEEE, The Open Group and ISO/IEC SC22/WG15). Today the Shell and Utilities are a volume within the set of documents that make up IEEE Std 1003.1-2024, and thus the former POSIX.2 (from 1992) is now part of the current unified POSIX standard.

The Shell and Utilities volume concentrates on the command interpreter interface and utility programs commonly executed from the command line or by other programs. The standard is freely available on the web at https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html.

Bash is concerned with the aspects of the shell’s behavior defined by the POSIX Shell and Utilities volume. The shell command language has of course been standardized, including the basic flow control and program execution constructs, I/O redirection and pipelines, argument handling, variable expansion, and quoting.

The *special* builtins, which must be implemented as part of the shell to provide the desired functionality, are specified as being part of the shell; examples of these are `eval` and `export`. Other utilities appear in the sections of POSIX not devoted to the shell which are commonly (and in some cases must be) implemented as builtin commands, such as `read` and `test`. POSIX also specifies aspects of the shell’s interactive behavior, including job control and command line editing. Only vi-style line editing commands have been standardized; emacs editing commands were left out due to objections.

#### 6.11.2 Bash POSIX Mode

Although Bash is an implementation of the POSIX shell specification, there are areas where the Bash default behavior differs from the specification. The Bash *posix mode* changes the Bash behavior in these areas so that it conforms more strictly to the standard.

Starting Bash with the --posix command-line option or executing ‘set -o posix’ while Bash is running will cause Bash to conform more closely to the POSIX standard by changing the behavior to match that specified by POSIX in areas where the Bash default differs.

When invoked as `sh`, Bash enters POSIX mode after reading the startup files.

The following list is what’s changed when POSIX mode is in effect:

1. Bash ensures that the `POSIXLY_CORRECT` variable is set.
2. Bash reads and executes the POSIX startup files (`$ENV`) rather than the normal Bash files (see Bash Startup Files.
3. Alias expansion is always enabled, even in non-interactive shells.
4. Reserved words appearing in a context where reserved words are recognized do not undergo alias expansion.
5. Alias expansion is performed when initially parsing a command substitution. The default (non-posix) mode generally defers it, when enabled, until the command substitution is executed. This means that command substitution will not expand aliases that are defined after the command substitution is initially parsed (e.g., as part of a function definition).
6. The `time` reserved word may be used by itself as a simple command. When used in this way, it displays timing statistics for the shell and its completed children. The `TIMEFORMAT` variable controls the format of the timing information.
7. The parser does not recognize `time` as a reserved word if the next token begins with a ‘-’.
8. When parsing and expanding a ${…} expansion that appears within double quotes, single quotes are no longer special and cannot be used to quote a closing brace or other special character, unless the operator is one of those defined to perform pattern removal. In this case, they do not have to appear as matched pairs.
9. Redirection operators do not perform filename expansion on the word in a redirection unless the shell is interactive.
10. Redirection operators do not perform word splitting on the word in a redirection.
11. Function names may not be the same as one of the POSIX special builtins.
12. Tilde expansion is only performed on assignments preceding a command name, rather than on all assignment statements on the line.
13. While variable indirection is available, it may not be applied to the ‘#’ and ‘?’ special parameters.
14. Expanding the ‘*’ special parameter in a pattern context where the expansion is double-quoted does not treat the `$*` as if it were double-quoted.
15. A double quote character (‘"’) is treated specially when it appears in a backquoted command substitution in the body of a here-document that undergoes expansion. That means, for example, that a backslash preceding a double quote character will escape it and the backslash will be removed.
16. Command substitutions don’t set the ‘?’ special parameter. The exit status of a simple command without a command word is still the exit status of the last command substitution that occurred while evaluating the variable assignments and redirections in that command, but that does not happen until after all of the assignments and redirections.
17. Literal tildes that appear as the first character in elements of the `PATH` variable are not expanded as described above under Tilde Expansion.
18. Command lookup finds POSIX special builtins before shell functions, including output printed by the `type` and `command` builtins.
19. Even if a shell function whose name contains a slash was defined before entering POSIX mode, the shell will not execute a function whose name contains one or more slashes.
20. When a command in the hash table no longer exists, Bash will re-search `$PATH` to find the new location. This is also available with ‘shopt -s checkhash’.
21. Bash will not insert a command without the execute bit set into the command hash table, even if it returns it as a (last-ditch) result from a `$PATH` search.
22. The message printed by the job control code and builtins when a job exits with a non-zero status is ‘Done(status)’.
23. The message printed by the job control code and builtins when a job is stopped is ‘Stopped(*signame*)’, where *signame* is, for example, `SIGTSTP`.
24. If the shell is interactive, Bash does not perform job notifications between executing commands in lists separated by ‘;’ or newline. Non-interactive shells print status messages after a foreground job in a list completes.
25. If the shell is interactive, Bash waits until the next prompt before printing the status of a background job that changes status or a foreground job that terminates due to a signal. Non-interactive shells print status messages after a foreground job completes.
26. Bash permanently removes jobs from the jobs table after notifying the user of their termination via the `wait` or `jobs` builtins. It removes the job from the jobs list after notifying the user of its termination, but the status is still available via `wait`, as long as `wait` is supplied a PID argument.
27. The `vi` editing mode will invoke the `vi` editor directly when the ‘v’ command is run, instead of checking `$VISUAL` and `$EDITOR`.
28. Prompt expansion enables the POSIX `PS1` and `PS2` expansions of ‘!’ to the history number and ‘!!’ to ‘!’, and Bash performs parameter expansion on the values of `PS1` and `PS2` regardless of the setting of the `promptvars` option.
29. The default history file is ~/.sh_history (this is the default value the shell assigns to `$HISTFILE`).
30. The ‘!’ character does not introduce history expansion within a double-quoted string, even if the `histexpand` option is enabled.
31. When printing shell function definitions (e.g., by `type`), Bash does not print the `function` reserved word unless necessary.
32. Non-interactive shells exit if a syntax error in an arithmetic expansion results in an invalid expression.
33. Non-interactive shells exit if a parameter expansion error occurs.
34. If a POSIX special builtin returns an error status, a non-interactive shell exits. The fatal errors are those listed in the POSIX standard, and include things like passing incorrect options, redirection errors, variable assignment errors for assignments preceding the command name, and so on.
35. A non-interactive shell exits with an error status if a variable assignment error occurs when no command name follows the assignment statements. A variable assignment error occurs, for example, when trying to assign a value to a readonly variable.
36. A non-interactive shell exits with an error status if a variable assignment error occurs in an assignment statement preceding a special builtin, but not with any other simple command. For any other simple command, the shell aborts execution of that command, and execution continues at the top level ("the shell shall not perform any further processing of the command in which the error occurred").
37. A non-interactive shell exits with an error status if the iteration variable in a `for` statement or the selection variable in a `select` statement is a readonly variable or has an invalid name.
38. Non-interactive shells exit if *filename* in `.` *filename* is not found.
39. Non-interactive shells exit if there is a syntax error in a script read with the `.` or `source` builtins, or in a string processed by the `eval` builtin.
40. Non-interactive shells exit if the `export`, `readonly` or `unset` builtin commands get an argument that is not a valid identifier, and they are not operating on shell functions. These errors force an exit because these are special builtins.
41. Assignment statements preceding POSIX special builtins persist in the shell environment after the builtin completes.
42. The `command` builtin does not prevent builtins that take assignment statements as arguments from expanding them as assignment statements; when not in POSIX mode, declaration commands lose their assignment statement expansion properties when preceded by `command`.
43. Enabling POSIX mode has the effect of setting the `inherit_errexit` option, so subshells spawned to execute command substitutions inherit the value of the -e option from the parent shell. When the `inherit_errexit` option is not enabled, Bash clears the -e option in such subshells.
44. Enabling POSIX mode has the effect of setting the `shift_verbose` option, so numeric arguments to `shift` that exceed the number of positional parameters will result in an error message.
45. Enabling POSIX mode has the effect of setting the `interactive_comments` option (see Comments).
46. The `.` and `source` builtins do not search the current directory for the filename argument if it is not found by searching `PATH`.
47. When the `alias` builtin displays alias definitions, it does not display them with a leading ‘alias ’ unless the -p option is supplied.
48. The `bg` builtin uses the required format to describe each job placed in the background, which does not include an indication of whether the job is the current or previous job.
49. When the `cd` builtin is invoked in logical mode, and the pathname constructed from `$PWD` and the directory name supplied as an argument does not refer to an existing directory, `cd` will fail instead of falling back to physical mode.
50. When the `cd` builtin cannot change a directory because the length of the pathname constructed from `$PWD` and the directory name supplied as an argument exceeds `PATH_MAX` when canonicalized, `cd` will attempt to use the supplied directory name.
51. When the `xpg_echo` option is enabled, Bash does not attempt to interpret any arguments to `echo` as options. `echo` displays each argument after converting escape sequences.
52. The `export` and `readonly` builtin commands display their output in the format required by POSIX.
53. When listing the history, the `fc` builtin does not include an indication of whether or not a history entry has been modified.
54. The default editor used by `fc` is `ed`.
55. `fc` treats extra arguments as an error instead of ignoring them.
56. If there are too many arguments supplied to `fc -s`, `fc` prints an error message and returns failure.
57. The output of ‘kill -l’ prints all the signal names on a single line, separated by spaces, without the ‘SIG’ prefix.
58. The `kill` builtin does not accept signal names with a ‘SIG’ prefix.
59. The `kill` builtin returns a failure status if any of the pid or job arguments are invalid or if sending the specified signal to any of them fails. In default mode, `kill` returns success if the signal was successfully sent to any of the specified processes.
60. The `printf` builtin uses `double` (via `strtod`) to convert arguments corresponding to floating point conversion specifiers, instead of `long double` if it’s available. The ‘L’ length modifier forces `printf` to use `long double` if it’s available.
61. The `pwd` builtin verifies that the value it prints is the same as the current directory, even if it is not asked to check the file system with the -P option.
62. The `read` builtin may be interrupted by a signal for which a trap has been set. If Bash receives a trapped signal while executing `read`, the trap handler executes and `read` returns an exit status greater than 128.
63. When the `set` builtin is invoked without options, it does not display shell function names and definitions.
64. When the `set` builtin is invoked without options, it displays variable values without quotes, unless they contain shell metacharacters, even if the result contains nonprinting characters.
65. The `test` builtin compares strings using the current locale when evaluating the ‘<’ and ‘>’ binary operators.
66. The `test` builtin’s -t unary primary requires an argument. Historical versions of `test` made the argument optional in certain cases, and Bash attempts to accommodate those for backwards compatibility.
67. The `trap` builtin displays signal names without the leading `SIG`.
68. The `trap` builtin doesn’t check the first argument for a possible signal specification and revert the signal handling to the original disposition if it is, unless that argument consists solely of digits and is a valid signal number. If users want to reset the handler for a given signal to the original disposition, they should use ‘-’ as the first argument.
69. `trap -p` without arguments displays signals whose dispositions are set to SIG_DFL and those that were ignored when the shell started, not just trapped signals.
70. The `type` and `command` builtins will not report a non-executable file as having been found, though the shell will attempt to execute such a file if it is the only so-named file found in `$PATH`.
71. The `ulimit` builtin uses a block size of 512 bytes for the -c and -f options.
72. The `unset` builtin with the -v option specified returns a fatal error if it attempts to unset a `readonly` or `non-unsettable` variable, which causes a non-interactive shell to exit.
73. When asked to unset a variable that appears in an assignment statement preceding the command, the `unset` builtin attempts to unset a variable of the same name in the current or previous scope as well. This implements the required "if an assigned variable is further modified by the utility, the modifications made by the utility shall persist" behavior.
74. The arrival of `SIGCHLD` when a trap is set on `SIGCHLD` does not interrupt the `wait` builtin and cause it to return immediately. The trap command is run once for each child that exits.
75. Bash removes an exited background process’s status from the list of such statuses after the `wait` builtin returns it.

There is additional POSIX behavior that Bash does not implement by default even when in POSIX mode. Specifically:

1. POSIX requires that word splitting be byte-oriented. That is, each *byte* in the value of `IFS` potentially splits a word, even if that byte is part of a multibyte character in `IFS` or part of multibyte character in the word. Bash allows multibyte characters in the value of `IFS`, treating a valid multibyte character as a single delimiter, and will not split a valid multibyte character even if one of the bytes composing that character appears in `IFS`. This is POSIX interpretation 1560, further modified by issue 1924.
2. The `fc` builtin checks `$EDITOR` as a program to edit history entries if `FCEDIT` is unset, rather than defaulting directly to `ed`. `fc` uses `ed` if `EDITOR` is unset.
3. As noted above, Bash requires the `xpg_echo` option to be enabled for the `echo` builtin to be fully conformant.

Bash can be configured to be POSIX-conformant by default, by specifying the --enable-strict-posix-default to `configure` when building (see Optional Features).

### 6.12 Shell Compatibility Mode

Bash-4.0 introduced the concept of a *shell compatibility level*, specified as a set of options to the shopt builtin (`compat31`, `compat32`, `compat40`, `compat41`, and so on). There is only one current compatibility level – each option is mutually exclusive. The compatibility level is intended to allow users to select behavior from previous versions that is incompatible with newer versions while they migrate scripts to use current features and behavior. It’s intended to be a temporary solution.

This section does not mention behavior that is standard for a particular version (e.g., setting `compat32` means that quoting the right hand side of the regexp matching operator quotes special regexp characters in the word, which is default behavior in bash-3.2 and subsequent versions).

If a user enables, say, `compat32`, it may affect the behavior of other compatibility levels up to and including the current compatibility level. The idea is that each compatibility level controls behavior that changed in that version of Bash, but that behavior may have been present in earlier versions. For instance, the change to use locale-based comparisons with the `[[` command came in bash-4.1, and earlier versions used ASCII-based comparisons, so enabling `compat32` will enable ASCII-based comparisons as well. That granularity may not be sufficient for all uses, and as a result users should employ compatibility levels carefully. Read the documentation for a particular feature to find out the current behavior.

Bash-4.3 introduced a new shell variable: `BASH_COMPAT`. The value assigned to this variable (a decimal version number like 4.2, or an integer corresponding to the `compat`*NN* option, like 42) determines the compatibility level.

Starting with bash-4.4, Bash began deprecating older compatibility levels. Eventually, the options will be removed in favor of `BASH_COMPAT`.

Bash-5.0 was the final version for which there was an individual shopt option for the previous version. `BASH_COMPAT` is the only mechanism to control the compatibility level in versions newer than bash-5.0.

The following table describes the behavior changes controlled by each compatibility level setting. The `compat`*NN* tag is used as shorthand for setting the compatibility level to *NN* using one of the following mechanisms. For versions prior to bash-5.0, the compatibility level may be set using the corresponding `compat`*NN* shopt option. For bash-4.3 and later versions, the `BASH_COMPAT` variable is preferred, and it is required for bash-5.1 and later versions.

**`compat31`**

- Quoting the rhs of the `[[` command’s regexp matching operator (=~) has no special effect

**`compat40`**

- The ‘<’ and ‘>’ operators to the `[[` command do not consider the current locale when comparing strings; they use ASCII ordering. Bash versions prior to bash-4.1 use ASCII collation and strcmp(3); bash-4.1 and later use the current locale’s collation sequence and strcoll(3).

**`compat41`**

- In POSIX mode, `time` may be followed by options and still be recognized as a reserved word (this is POSIX interpretation 267).
- In POSIX mode, the parser requires that an even number of single quotes occur in the *word* portion of a double-quoted ${…} parameter expansion and treats them specially, so that characters within the single quotes are considered quoted (this is POSIX interpretation 221).

**`compat42`**

- The replacement string in double-quoted pattern substitution does not undergo quote removal, as it does in versions after bash-4.2.
- In POSIX mode, single quotes are considered special when expanding the *word* portion of a double-quoted ${…} parameter expansion and can be used to quote a closing brace or other special character (this is part of POSIX interpretation 221); in later versions, single quotes are not special within double-quoted word expansions.

**`compat43`**

- Word expansion errors are considered non-fatal errors that cause the current command to fail, even in POSIX mode (the default behavior is to make them fatal errors that cause the shell to exit).
- When executing a shell function, the loop state (while/until/etc.) is not reset, so `break` or `continue` in that function will break or continue loops in the calling context. Bash-4.4 and later reset the loop state to prevent this.

**`compat44`**

- The shell sets up the values used by `BASH_ARGV` and `BASH_ARGC` so they can expand to the shell’s positional parameters even if extended debugging mode is not enabled.
- A subshell inherits loops from its parent context, so `break` or `continue` will cause the subshell to exit. Bash-5.0 and later reset the loop state to prevent the exit.
- Variable assignments preceding builtins like `export` and `readonly` that set attributes continue to affect variables with the same name in the calling environment even if the shell is not in POSIX mode.

**`compat50 (set using BASH_COMPAT)`**

- Bash-5.1 changed the way `$RANDOM` is generated to introduce slightly more randomness. If the shell compatibility level is set to 50 or lower, it reverts to the method from bash-5.0 and previous versions, so seeding the random number generator by assigning a value to `RANDOM` will produce the same sequence as in bash-5.0.
- If the command hash table is empty, Bash versions prior to bash-5.1 printed an informational message to that effect, even when producing output that can be reused as input. Bash-5.1 suppresses that message when the -l option is supplied.

**`compat51 (set using BASH_COMPAT)`**

- The `unset` builtin will unset the array `a` given an argument like ‘a[@]’. Bash-5.2 will unset an element with key ‘@’ (associative arrays) or remove all the elements without unsetting the array (indexed arrays).
- Arithmetic commands ( ((…)) ) and the expressions in an arithmetic for statement can be expanded more than once.
- Expressions used as arguments to arithmetic operators in the `[[` conditional command can be expanded more than once.
- The expressions in substring parameter brace expansion can be expanded more than once.
- The expressions in the $(( … )) word expansion can be expanded more than once.
- Arithmetic expressions used as indexed array subscripts can be expanded more than once.
- `test -v`, when given an argument of ‘A[@]’, where *A* is an existing associative array, will return true if the array has any set elements. Bash-5.2 will look for and report on a key named ‘@’.
- the ${*parameter*[:]=*value*} word expansion will return *value*, before any variable-specific transformations have been performed (e.g., converting to lowercase). Bash-5.2 will return the final value assigned to the variable.
- Parsing command substitutions will behave as if extended globbing (see The Shopt Builtin) is enabled, so that parsing a command substitution containing an extglob pattern (say, as part of a shell function) will not fail. This assumes the intent is to enable extglob before the command is executed and word expansions are performed. It will fail at word expansion time if extglob hasn’t been enabled by the time the command is executed.

**`compat52 (set using BASH_COMPAT)`**

- The `test` builtin uses its historical algorithm to parse parenthesized subexpressions when given five or more arguments.
- If the -p or -P option is supplied to the `bind` builtin, `bind` treats any arguments remaining after option processing as bindable command names, and displays any key sequences bound to those commands, instead of treating the arguments as key sequences to bind.
- Interactive shells will notify the user of completed jobs while sourcing a script. Newer versions defer notification until script execution completes.

---
title: "Bash Reference Manual (part 5/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 5/15
---

## 4 Shell Builtin Commands

Builtin commands are contained within the shell itself. When the name of a builtin command is used as the first word of a simple command (see Simple Commands), the shell executes the command directly, without invoking another program. Builtin commands are necessary to implement functionality impossible or inconvenient to obtain with separate utilities.

This section briefly describes the builtins which Bash inherits from the Bourne Shell, as well as the builtin commands which are unique to or have been extended in Bash.

Several builtin commands are described in other chapters: builtin commands which provide the Bash interface to the job control facilities (see Job Control Builtins), the directory stack (see Directory Stack Builtins), the command history (see Bash History Builtins), and the programmable completion facilities (see Programmable Completion Builtins).

Many of the builtins have been extended by POSIX or Bash.

Unless otherwise noted, each builtin command documented as accepting options preceded by ‘-’ accepts ‘--’ to signify the end of the options. The `:`, `true`, `false`, and `test`/`[` builtins do not accept options and do not treat ‘--’ specially. The `exit`, `logout`, `return`, `break`, `continue`, `let`, and `shift` builtins accept and process arguments beginning with ‘-’ without requiring ‘--’. Other builtins that accept arguments but are not specified as accepting options interpret arguments beginning with ‘-’ as invalid options and require ‘--’ to prevent this interpretation.

### 4.1 Bourne Shell Builtins

The following shell builtin commands are inherited from the Bourne Shell. These commands are implemented as specified by the POSIX standard.

**`: (a colon)` ¶**

```
: [arguments]
```

Do nothing beyond expanding *arguments* and performing redirections. The return status is zero.

**`. (a period)` ¶**

```
. [-p path] filename [arguments]
```

The `.` command reads and execute commands from the *filename* argument in the current shell context.

If *filename* does not contain a slash, `.` searches for it. If -p is supplied, `.` treats *path* as a colon-separated list of directories in which to find *filename*; otherwise, `.` uses the directories in `PATH` to find *filename*. *filename* does not need to be executable. When Bash is not in POSIX mode, it searches the current directory if *filename* is not found in `$PATH`, but does not search the current directory if -p is supplied. If the `sourcepath` option (see The Shopt Builtin) is turned off, `.` does not search `PATH`.

If any *arguments* are supplied, they become the positional parameters when *filename* is executed. Otherwise the positional parameters are unchanged.

If the -T option is enabled, `.` inherits any trap on `DEBUG`; if it is not, any `DEBUG` trap string is saved and restored around the call to `.`, and `.` unsets the `DEBUG` trap while it executes. If -T is not set, and the sourced file changes the `DEBUG` trap, the new value persists after `.` completes. The return status is the exit status of the last command executed from *filename*, or zero if no commands are executed. If *filename* is not found, or cannot be read, the return status is non-zero. This builtin is equivalent to `source`.

**`break` ¶**

```
break [n]
```

Exit from a `for`, `while`, `until`, or `select` loop. If *n* is supplied, `break` exits the *n*th enclosing loop. *n* must be greater than or equal to 1. The return status is zero unless *n* is not greater than or equal to 1.

**`cd` ¶**

```
cd [-L] [-@] [directory]
cd -P [-e] [-@] [directory]
```

Change the current working directory to *directory*. If *directory* is not supplied, the value of the `HOME` shell variable is used as *directory*. If the shell variable `CDPATH` exists, and *directory* does not begin with a slash, `cd` uses it as a search path: `cd` searches each directory name in `CDPATH` for *directory*, with alternative directory names in `CDPATH` separated by a colon (‘:’). A null directory name in `CDPATH` means the same thing as the current directory.

The -P option means not to follow symbolic links: symbolic links are resolved while `cd` is traversing *directory* and before processing an instance of .. in *directory*.

By default, or when the -L option is supplied, symbolic links in *directory* are resolved after `cd` processes an instance of .. in *directory*.

If .. appears in *directory*, `cd` processes it by removing the immediately preceding pathname component, back to a slash or the beginning of *directory*, and verifying that the portion of *directory* it has processed to that point is still a valid directory name after removing the pathname component. If it is not a valid directory name, `cd` returns a non-zero status.

If the -e option is supplied with -P and `cd` cannot successfully determine the current working directory after a successful directory change, it returns a non-zero status.

On systems that support it, the -@ option presents the extended attributes associated with a file as a directory.

If *directory* is ‘-’, it is converted to `$OLDPWD` before attempting the directory change.

If `cd` uses a non-empty directory name from `CDPATH`, or if ‘-’ is the first argument, and the directory change is successful, `cd` writes the absolute pathname of the new working directory to the standard output.

If the directory change is successful, `cd` sets the value of the `PWD` environment variable to the new directory name, and sets the `OLDPWD` environment variable to the value of the current working directory before the change.

The return status is zero if the directory is successfully changed, non-zero otherwise.

**`continue` ¶**

```
continue [n]
```

`continue` resumes the next iteration of an enclosing `for`, `while`, `until`, or `select` loop. If *n* is supplied, Bash resumes the execution of the *n*th enclosing loop. *n* must be greater than or equal to 1. The return status is zero unless *n* is not greater than or equal to 1.

**`eval` ¶**

```
eval [arguments]
```

The *arguments* are concatenated together into a single command, separated by spaces. Bash then reads and executes this command and returns its exit status as the exit status of `eval`. If there are no arguments or only empty arguments, the return status is zero.

**`exec` ¶**

```
exec [-cl] [-a name] [command [arguments]]
```

If *command* is supplied, it replaces the shell without creating a new process. *command* cannot be a shell builtin or function. The *arguments* become the arguments to *command* If the -l option is supplied, the shell places a dash at the beginning of the zeroth argument passed to *command*. This is what the `login` program does. The -c option causes *command* to be executed with an empty environment. If -a is supplied, the shell passes *name* as the zeroth argument to *command*.

If *command* cannot be executed for some reason, a non-interactive shell exits, unless the `execfail` shell option is enabled. In that case, it returns a non-zero status. An interactive shell returns a non-zero status if the file cannot be executed. A subshell exits unconditionally if `exec` fails.

If *command* is not specified, redirections may be used to affect the current shell environment. If there are no redirection errors, the return status is zero; otherwise the return status is non-zero.

**`exit` ¶**

```
exit [n]
```

Exit the shell, returning a status of *n* to the shell’s parent. If *n* is omitted, the exit status is that of the last command executed. Any trap on `EXIT` is executed before the shell terminates.

**`export` ¶**

```
export [-fn] [-p] [name[=value]]
```

Mark each *name* to be passed to subsequently executed commands in the environment. If the -f option is supplied, the *name*s refer to shell functions; otherwise the names refer to shell variables.

The -n option means to unexport each name: no longer mark it for export. If no *name*s are supplied, or if only the -p option is given, `export` displays a list of names of all exported variables on the standard output. Using -p and -f together displays exported functions. The -p option displays output in a form that may be reused as input.

`export` allows the value of a variable to be set at the same time it is exported or unexported by following the variable name with =*value*. This sets the value of the variable is to *value* while modifying the export attribute.

The return status is zero unless an invalid option is supplied, one of the names is not a valid shell variable name, or -f is supplied with a name that is not a shell function.

**`false` ¶**

```
false
```

Does nothing; returns a non-zero status.

**`getopts` ¶**

```
getopts optstring name [arg ...]
```

`getopts` is used by shell scripts or functions to parse positional parameters and obtain options and their arguments. *optstring* contains the option characters to be recognized; if a character is followed by a colon, the option is expected to have an argument, which should be separated from it by whitespace. The colon (‘:’) and question mark (‘?’) may not be used as option characters.

Each time it is invoked, `getopts` places the next option in the shell variable *name*, initializing *name* if it does not exist, and the index of the next argument to be processed into the variable `OPTIND`. `OPTIND` is initialized to 1 each time the shell or a shell script is invoked. When an option requires an argument, `getopts` places that argument into the variable `OPTARG`.

The shell does not reset `OPTIND` automatically; it must be manually reset between multiple calls to `getopts` within the same shell invocation to use a new set of parameters.

When it reaches the end of options, `getopts` exits with a return value greater than zero. `OPTIND` is set to the index of the first non-option argument, and *name* is set to ‘?’.

`getopts` normally parses the positional parameters, but if more arguments are supplied as *arg* values, `getopts` parses those instead.

`getopts` can report errors in two ways. If the first character of *optstring* is a colon, `getopts` uses *silent* error reporting. In normal operation, `getopts` prints diagnostic messages when it encounters invalid options or missing option arguments. If the variable `OPTERR` is set to 0, `getopts` does not display any error messages, even if the first character of `optstring` is not a colon.

If `getopts` detects an invalid option, it places ‘?’ into *name* and, if not silent, prints an error message and unsets `OPTARG`. If `getopts` is silent, it assigns the option character found to `OPTARG` and does not print a diagnostic message.

If a required argument is not found, and `getopts` is not silent, it sets the value of *name* to a question mark (‘?’), unsets `OPTARG`, and prints a diagnostic message. If `getopts` is silent, it sets the value of *name* to a colon (‘:’), and sets `OPTARG` to the option character found.

`getopts` returns true if an option, specified or unspecified, is found. It returns false when it encounters the end of options or if an error occurs.

**`hash` ¶**

```
hash [-r] [-p filename] [-dt] [name]
```

Each time `hash` is invoked, it remembers the full filenames of the commands specified as *name* arguments, so they need not be searched for on subsequent invocations. The commands are found by searching through the directories listed in `$PATH`. Any previously-remembered filename associated with *name* is discarded. The -p option inhibits the path search, and `hash` uses *filename* as the location of *name*.

The -r option causes the shell to forget all remembered locations. Assigning to the `PATH` variable also clears all hashed filenames. The -d option causes the shell to forget the remembered location of each *name*.

If the -t option is supplied, `hash` prints the full pathname corresponding to each *name*. If multiple *name* arguments are supplied with -t, `hash` prints each *name* before the corresponding hashed full path. The -l option displays output in a format that may be reused as input.

If no arguments are given, or if only -l is supplied, `hash` prints information about remembered commands. The -t, -d, and -p options (the options that act on the *name* arguments) are mutually exclusive. Only one will be active. If more than one is supplied, -t has higher priority than -p, and both have higher priority than -d.

The return status is zero unless a *name* is not found or an invalid option is supplied.

**`pwd` ¶**

```
pwd [-LP]
```

Print the absolute pathname of the current working directory. If the -P option is supplied, or the -o physical option to the `set` builtin (see The Set Builtin) is enabled, the pathname printed will not contain symbolic links. If the -L option is supplied, the pathname printed may contain symbolic links. The return status is zero unless an error is encountered while determining the name of the current directory or an invalid option is supplied.

**`readonly` ¶**

```
readonly [-aAf] [-p] [name[=value]] ...
```

Mark each *name* as readonly. The values of these names may not be changed by subsequent assignment or unset. If the -f option is supplied, each *name* refers to a shell function. The -a option means each *name* refers to an indexed array variable; the -A option means each *name* refers to an associative array variable. If both options are supplied, -A takes precedence. If no *name* arguments are supplied, or if the -p option is supplied, print a list of all readonly names. The other options may be used to restrict the output to a subset of the set of readonly names. The -p option displays output in a format that may be reused as input.

`readonly` allows the value of a variable to be set at the same time the readonly attribute is changed by following the variable name with =*value*. This sets the value of the variable is to *value* while modifying the readonly attribute.

The return status is zero unless an invalid option is supplied, one of the *name* arguments is not a valid shell variable or function name, or the -f option is supplied with a name that is not a shell function.

**`return` ¶**

```
return [n]
```

Stop executing a shell function or sourced file and return the value *n* to its caller. If *n* is not supplied, the return value is the exit status of the last command executed. If `return` is executed by a trap handler, the last command used to determine the status is the last command executed before the trap handler. If `return` is executed during a `DEBUG` trap, the last command used to determine the status is the last command executed by the trap handler before `return` was invoked.

When `return` is used to terminate execution of a script being executed with the `.` (`source`) builtin, it returns either *n* or the exit status of the last command executed within the script as the exit status of the script. If *n* is supplied, the return value is its least significant 8 bits.

Any command associated with the `RETURN` trap is executed before execution resumes after the function or script.

The return status is non-zero if `return` is supplied a non-numeric argument or is used outside a function and not during the execution of a script by `.` or `source`.

**`shift` ¶**

```
shift [n]
```

Shift the positional parameters to the left by *n*: the positional parameters from *n*+1 … `$#` are renamed to `$1` … `$#`-*n*. Parameters represented by the numbers `$#` down to `$#`-*n*+1 are unset. *n* must be a non-negative number less than or equal to `$#`. If *n* is not supplied, it is assumed to be 1. If *n* is zero or greater than `$#`, the positional parameters are not changed. The return status is zero unless *n* is greater than `$#` or less than zero, non-zero otherwise.

**`test` ¶**

**`[`**

```
test expr
```

Evaluate a conditional expression *expr* and return a status of 0 (true) or 1 (false). Each operator and operand must be a separate argument. Expressions are composed of the primaries described below in Bash Conditional Expressions. `test` does not accept any options, nor does it accept and ignore an argument of -- as signifying the end of options. When using the `[` form, the last argument to the command must be a `]`.

Expressions may be combined using the following operators, listed in decreasing order of precedence. The evaluation depends on the number of arguments; see below. `test` uses operator precedence when there are five or more arguments.

**`! *expr*`**

True if *expr* is false.

**`( *expr* )`**

Returns the value of *expr*. This may be used to override normal operator precedence.

**`*expr1* -a *expr2*`**

True if both *expr1* and *expr2* are true.

**`*expr1* -o *expr2*`**

True if either *expr1* or *expr2* is true.

The `test` and `[` builtins evaluate conditional expressions using a set of rules based on the number of arguments.

**0 arguments**

The expression is false.

**1 argument**

The expression is true if, and only if, the argument is not null.

**2 arguments**

If the first argument is ‘!’, the expression is true if and only if the second argument is null. If the first argument is one of the unary conditional operators (see Bash Conditional Expressions), the expression is true if the unary test is true. If the first argument is not a valid unary operator, the expression is false.

**3 arguments**

The following conditions are applied in the order listed.

1. If the second argument is one of the binary conditional operators (see Bash Conditional Expressions), the result of the expression is the result of the binary test using the first and third arguments as operands. The ‘-a’ and ‘-o’ operators are considered binary operators when there are three arguments.
2. If the first argument is ‘!’, the value is the negation of the two-argument test using the second and third arguments.
3. If the first argument is exactly ‘(’ and the third argument is exactly ‘)’, the result is the one-argument test of the second argument.
4. Otherwise, the expression is false.

**4 arguments**

The following conditions are applied in the order listed.

1. If the first argument is ‘!’, the result is the negation of the three-argument expression composed of the remaining arguments.
2. If the first argument is exactly ‘(’ and the fourth argument is exactly ‘)’, the result is the two-argument test of the second and third arguments.
3. Otherwise, the expression is parsed and evaluated according to precedence using the rules listed above.

**5 or more arguments**

The expression is parsed and evaluated according to precedence using the rules listed above.

If the shell is in POSIX mode, or if the expression is part of the `[[` command, the ‘<’ and ‘>’ operators sort using the current locale. If the shell is not in POSIX mode, the `test` and ‘[’ commands sort lexicographically using ASCII ordering.

The historical operator-precedence parsing with 4 or more arguments can lead to ambiguities when it encounters strings that look like primaries. The POSIX standard has deprecated the -a and -o primaries and enclosing expressions within parentheses. Scripts should no longer use them. It’s much more reliable to restrict test invocations to a single primary, and to replace uses of -a and -o with the shell’s `&&` and `||` list operators. For example, use

```
test -n string1 && test -n string2
```

instead of

```
test -n string1 -a -n string2
```

**`times` ¶**

```
times
```

Print out the user and system times used by the shell and its children. The return status is zero.

**`trap` ¶**

```
trap [-lpP] [action] [sigspec ...]
```

The *action* is a command that is read and executed when the shell receives any of the signals *sigspec*. If *action* is absent (and there is a single *sigspec*) or equal to ‘-’, each specified *sigspec*’s disposition is reset to the value it had when the shell was started. If *action* is the null string, then the signal specified by each *sigspec* is ignored by the shell and commands it invokes.

If no arguments are supplied, `trap` prints the actions associated with each trapped signal as a set of `trap` commands that can be reused as shell input to restore the current signal dispositions.

If *action* is not present and -p has been supplied, `trap` displays the trap commands associated with each *sigspec*, or, if no *sigspec*s are supplied, for all trapped signals, as a set of `trap` commands that can be reused as shell input to restore the current signal dispositions. The -P option behaves similarly, but displays only the actions associated with each *sigspec* argument. -P requires at least one *sigspec* argument. The -P or -p options may be used in a subshell environment (e.g., command substitution) and, as long as they are used before `trap` is used to change a signal’s handling, will display the state of its parent’s traps.

The -l option prints a list of signal names and their corresponding numbers. Each *sigspec* is either a signal name or a signal number. Signal names are case insensitive and the `SIG` prefix is optional. If -l is supplied with no *sigspec* arguments, it prints a list of valid signal names.

If a *sigspec* is `0` or `EXIT`, *action* is executed when the shell exits. If a *sigspec* is `DEBUG`, *action* is executed before every simple command, `for` command, `case` command, `select` command, (( arithmetic command, [[ conditional command, arithmetic `for` command, and before the first command executes in a shell function. Refer to the description of the `extdebug` shell option (see The Shopt Builtin) for details of its effect on the `DEBUG` trap. If a *sigspec* is `RETURN`, *action* is executed each time a shell function or a script executed with the `.` or `source` builtins finishes executing.

If a *sigspec* is `ERR`, *action* is executed whenever a pipeline (which may consist of a single simple command), a list, or a compound command returns a non-zero exit status, subject to the following conditions. The `ERR` trap is not executed if the failed command is part of the command list immediately following an `until` or `while` reserved word, part of the test following the `if` or `elif` reserved words, part of a command executed in a `&&` or `||` list except the command following the final `&&` or `||`, any command in a pipeline but the last, (subject to the state of the `pipefail` shell option), or if the command’s return status is being inverted using `!`. These are the same conditions obeyed by the `errexit` (-e) option.

When the shell is not interactive, signals ignored upon entry to a non-interactive shell cannot be trapped or reset. Interactive shells permit trapping signals ignored on entry. Trapped signals that are not being ignored are reset to their original values in a subshell or subshell environment when one is created.

The return status is zero unless a *sigspec* does not specify a valid signal; non-zero otherwise.

**`true` ¶**

```
true
```

Does nothing, returns a 0 status.

**`umask` ¶**

```
umask [-p] [-S] [mode]
```

Set the shell process’s file creation mask to *mode*. If *mode* begins with a digit, it is interpreted as an octal number; if not, it is interpreted as a symbolic mode mask similar to that accepted by the `chmod` command. If *mode* is omitted, `umask` prints the current value of the mask. If the -S option is supplied without a *mode* argument, `umask` prints the mask in a symbolic format; the default output is an octal number. If the -p option is supplied, and *mode* is omitted, the output is in a form that may be reused as input. The return status is zero if the mode is successfully changed or if no *mode* argument is supplied, and non-zero otherwise.

Note that when the mode is interpreted as an octal number, each number of the umask is subtracted from `7`. Thus, a umask of `022` results in permissions of `755`.

**`unset` ¶**

```
unset [-fnv] [name]
```

Remove each variable or function *name*. If the -v option is given, each *name* refers to a shell variable and that variable is removed. If the -f option is given, the *name*s refer to shell functions, and the function definition is removed. If the -n option is supplied, and *name* is a variable with the `nameref` attribute, *name* will be unset rather than the variable it references. -n has no effect if the -f option is supplied. If no options are supplied, each *name* refers to a variable; if there is no variable by that name, a function with that name, if any, is unset. Readonly variables and functions may not be unset. When variables or functions are removed, they are also removed from the environment passed to subsequent commands. Some shell variables may not be unset. Some shell variables lose their special behavior if they are unset; such behavior is noted in the description of the individual variables. The return status is zero unless a *name* is readonly or may not be unset.

### 4.2 Bash Builtin Commands

This section describes builtin commands which are unique to or have been extended in Bash. Some of these commands are specified in the POSIX standard.

**`alias` ¶**

```
alias [-p] [name[=value] ...]
```

Without arguments or with the -p option, `alias` prints the list of aliases on the standard output in a form that allows them to be reused as input. If arguments are supplied, define an alias for each *name* whose *value* is given. If no *value* is given, print the name and value of the alias *name*. A trailing space in *value* causes the next word to be checked for alias substitution when the alias is expanded during command parsing. `alias` returns true unless a *name* is given (without a corresponding =*value*) for which no alias has been defined. Aliases are described in Aliases.

**`bind` ¶**

```
bind [-m keymap] [-lsvSVX]
bind [-m keymap] [-q function] [-u function] [-r keyseq]
bind [-m keymap] -f filename
bind [-m keymap] -x keyseq[: ]shell-command
bind [-m keymap] keyseq:function-name
bind [-m keymap] keyseq:readline-command
bind [-m keymap] -p|-P [readline-command]
bind readline-command-line
```

Display current Readline (see Command Line Editing) key and function bindings, bind a key sequence to a Readline function or macro or to a shell command, or set a Readline variable. Each non-option argument is a key binding or command as it would appear in a Readline initialization file (see Readline Init File), but each binding or command must be passed as a separate argument; e.g., ‘"\C-x\C-r":re-read-init-file’.

In the following descriptions, options that display output in a form available to be re-read format their output as commands that would appear in a Readline initialization file or that would be supplied as individual arguments to a `bind` command.

Options, if supplied, have the following meanings:

**`-m *keymap*`**

Use *keymap* as the keymap to be affected by the subsequent bindings. Acceptable *keymap* names are `emacs`, `emacs-standard`, `emacs-meta`, `emacs-ctlx`, `vi`, `vi-move`, `vi-command`, and `vi-insert`. `vi` is equivalent to `vi-command` (`vi-move` is also a synonym); `emacs` is equivalent to `emacs-standard`.

**`-l`**

List the names of all Readline functions.

**`-p`**

Display Readline function names and bindings in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file. If arguments remain after option processing, `bind` treats them as readline command names and restricts output to those names.

**`-P`**

List current Readline function names and bindings. If arguments remain after option processing, `bind` treats them as readline command names and restricts output to those names.

**`-s`**

Display Readline key sequences bound to macros and the strings they output in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file.

**`-S`**

Display Readline key sequences bound to macros and the strings they output.

**`-v`**

Display Readline variable names and values in such a way that they can be used as an argument to a subsequent `bind` command or in a Readline initialization file.

**`-V`**

List current Readline variable names and values.

**`-f *filename*`**

Read key bindings from *filename*.

**`-q *function*`**

Display key sequences that invoke the named Readline *function*.

**`-u *function*`**

Unbind all key sequences bound to the named Readline *function*.

**`-r *keyseq*`**

Remove any current binding for *keyseq*.

**`-x *keyseq:shell-command*`**

Cause *shell-command* to be executed whenever *keyseq* is entered. The separator between *keyseq* and *shell-command* is either whitespace or a colon optionally followed by whitespace. If the separator is whitespace, *shell-command* must be enclosed in double quotes and Readline expands any of its special backslash-escapes in *shell-command* before saving it. If the separator is a colon, any enclosing double quotes are optional, and Readline does not expand the command string before saving it. Since the entire key binding expression must be a single argument, it should be enclosed in single quotes. When *shell-command* is executed, the shell sets the `READLINE_LINE` variable to the contents of the Readline line buffer and the `READLINE_POINT` and `READLINE_MARK` variables to the current location of the insertion point and the saved insertion point (the *mark*), respectively. The shell assigns any numeric argument the user supplied to the `READLINE_ARGUMENT` variable. If there was no argument, that variable is not set. If the executed command changes the value of any of `READLINE_LINE`, `READLINE_POINT`, or `READLINE_MARK`, those new values will be reflected in the editing state.

**`-X`**

List all key sequences bound to shell commands and the associated commands in a format that can be reused as an argument to a subsequent `bind` command.

The return status is zero unless an invalid option is supplied or an error occurs.

**`builtin` ¶**

```
builtin [shell-builtin [args]]
```

Execute the specified shell builtin *shell-builtin*, passing it *args*, and return its exit status. This is useful when defining a shell function with the same name as a shell builtin, retaining the functionality of the builtin within the function. The return status is non-zero if *shell-builtin* is not a shell builtin command.

**`caller` ¶**

```
caller [expr]
```

Returns the context of any active subroutine call (a shell function or a script executed with the `.` or `source` builtins).

Without *expr*, `caller` displays the line number and source filename of the current subroutine call. If a non-negative integer is supplied as *expr*, `caller` displays the line number, subroutine name, and source file corresponding to that position in the current execution call stack. This extra information may be used, for example, to print a stack trace. The current frame is frame 0.

The return value is 0 unless the shell is not executing a subroutine call or *expr* does not correspond to a valid position in the call stack.

**`command` ¶**

```
command [-pVv] command [arguments ...]
```

The `command` builtin runs *command* with *arguments* ignoring any shell function named *command*. Only shell builtin commands or commands found by searching the `PATH` are executed. If there is a shell function named `ls`, running ‘command ls’ within the function will execute the external command `ls` instead of calling the function recursively. The -p option means to use a default value for `PATH` that is guaranteed to find all of the standard utilities. The return status in this case is 127 if *command* cannot be found or an error occurred, and the exit status of *command* otherwise.

If either the -V or -v option is supplied, `command` prints a description of *command*. The -v option displays a single word indicating the command or file name used to invoke *command*; the -V option produces a more verbose description. In this case, the return status is zero if *command* is found, and non-zero if not.

**`declare` ¶**

```
declare [-aAfFgiIlnrtux] [-p] [name[=value] ...]
```

Declare variables and give them attributes. If no *name*s are given, then display the values of variables or shell functions instead.

The -p option will display the attributes and values of each *name*. When -p is used with *name* arguments, additional options, other than -f and -F, are ignored.

When -p is supplied without *name* arguments, `declare` will display the attributes and values of all variables having the attributes specified by the additional options. If no other options are supplied with -p, `declare` will display the attributes and values of all shell variables. The -f option restricts the display to shell functions.

The -F option inhibits the display of function definitions; only the function name and attributes are printed. If the `extdebug` shell option is enabled using `shopt` (see The Shopt Builtin), the source file name and line number where each *name* is defined are displayed as well. -F implies -f.

The -g option forces variables to be created or modified at the global scope, even when `declare` is executed in a shell function. It is ignored in when `declare` is not executed in a shell function.

The -I option causes local variables to inherit the attributes (except the `nameref` attribute) and value of any existing variable with the same *name* at a surrounding scope. If there is no existing variable, the local variable is initially unset.

The following options can be used to restrict output to variables with the specified attributes or to give variables attributes:

**`-a`**

Each *name* is an indexed array variable (see Arrays).

**`-A`**

Each *name* is an associative array variable (see Arrays).

**`-f`**

Each *name* refers to a shell function.

**`-i`**

The variable is to be treated as an integer; arithmetic evaluation (see Shell Arithmetic) is performed when the variable is assigned a value.

**`-l`**

When the variable is assigned a value, all upper-case characters are converted to lower-case. The upper-case attribute is disabled.

**`-n`**

Give each *name* the `nameref` attribute, making it a name reference to another variable. That other variable is defined by the value of *name*. All references, assignments, and attribute modifications to *name*, except for those using or changing the -n attribute itself, are performed on the variable referenced by *name*’s value. The nameref attribute cannot be applied to array variables.

**`-r`**

Make *name*s readonly. These names cannot then be assigned values by subsequent assignment statements or unset.

**`-t`**

Give each *name* the `trace` attribute. Traced functions inherit the `DEBUG` and `RETURN` traps from the calling shell. The trace attribute has no special meaning for variables.

**`-u`**

When the variable is assigned a value, all lower-case characters are converted to upper-case. The lower-case attribute is disabled.

**`-x`**

Mark each *name* for export to subsequent commands via the environment.

Using ‘+’ instead of ‘-’ turns off the specified attribute instead, with the exceptions that ‘+a’ and ‘+A’ may not be used to destroy array variables and ‘+r’ will not remove the readonly attribute.

When used in a function, `declare` makes each *name* local, as with the `local` command, unless the -g option is supplied. If a variable name is followed by =*value*, the value of the variable is set to *value*.

When using -a or -A and the compound assignment syntax to create array variables, additional attributes do not take effect until subsequent assignments.

The return status is zero unless an invalid option is encountered, an attempt is made to define a function using ‘-f foo=bar’, an attempt is made to assign a value to a readonly variable, an attempt is made to assign a value to an array variable without using the compound assignment syntax (see Arrays), one of the *name*s is not a valid shell variable name, an attempt is made to turn off readonly status for a readonly variable, an attempt is made to turn off array status for an array variable, or an attempt is made to display a non-existent function with -f.

**`echo` ¶**

```
echo [-neE] [arg ...]
```

Output the *arg*s, separated by spaces, terminated with a newline. The return status is 0 unless a write error occurs. If -n is specified, the trailing newline is not printed.

If the -e option is given, `echo` interprets the following backslash-escaped characters. The -E option disables interpretation of these escape characters, even on systems where they are interpreted by default. The `xpg_echo` shell option determines whether or not `echo` interprets any options and expands these escape characters. `echo` does not interpret -- to mean the end of options.

`echo` interprets the following escape sequences:

**`\a`**

alert (bell)

**`\b`**

backspace

**`\c`**

suppress further output

**`\e`**

**`\E`**

escape

**`\f`**

form feed

**`\n`**

new line

**`\r`**

carriage return

**`\t`**

horizontal tab

**`\v`**

vertical tab

**`\\`**

backslash

**`\0*nnn*`**

The eight-bit character whose value is the octal value *nnn* (zero to three octal digits).

**`\x*HH*`**

The eight-bit character whose value is the hexadecimal value *HH* (one or two hex digits).

**`\u*HHHH*`**

The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHH* (one to four hex digits).

**`\U*HHHHHHHH*`**

The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHHHHHH* (one to eight hex digits).

`echo` writes any unrecognized backslash-escaped characters unchanged.

**`enable` ¶**

```
enable [-a] [-dnps] [-f filename] [name ...]
```

Enable and disable builtin shell commands. Disabling a builtin allows an executable file which has the same name as a shell builtin to be executed without specifying a full pathname, even though the shell normally searches for builtins before files.

If -n is supplied, the *name*s are disabled. Otherwise *name*s are enabled. For example, to use the `test` binary found using `$PATH` instead of the shell builtin version, type ‘enable -n test’.

If the -p option is supplied, or no *name* arguments are supplied, print a list of shell builtins. With no other arguments, the list consists of all enabled shell builtins. The -n option means to print only disabled builtins. The -a option means to list each builtin with an indication of whether or not it is enabled. The -s option means to restrict `enable` to the POSIX special builtins.

The -f option means to load the new builtin command *name* from shared object *filename*, on systems that support dynamic loading. If *filename* does not contain a slash. Bash will use the value of the `BASH_LOADABLES_PATH` variable as a colon-separated list of directories in which to search for *filename*. The default for `BASH_LOADABLES_PATH` is system-dependent, and may include "." to force a search of the current directory. The -d option will delete a builtin loaded with -f. If -s is used with -f, the new builtin becomes a POSIX special builtin (see Special Builtins).

If no options are supplied and a *name* is not a shell builtin, `enable` will attempt to load *name* from a shared object named *name*, as if the command were ‘enable -f *name* *name*’.

The return status is zero unless a *name* is not a shell builtin or there is an error loading a new builtin from a shared object.

**`help` ¶**

```
help [-dms] [pattern]
```

Display helpful information about builtin commands. If *pattern* is specified, `help` gives detailed help on all commands matching *pattern* as described below; otherwise it displays a list of all builtins and shell compound commands.

Options, if supplied, have the following meanings:

**`-d`**

Display a short description of each *pattern*

**`-m`**

Display the description of each *pattern* in a manpage-like format

**`-s`**

Display only a short usage synopsis for each *pattern*

If *pattern* contains pattern matching characters (see Pattern Matching) it’s treated as a shell pattern and `help` prints the description of each help topic matching *pattern*.

If not, and *pattern* exactly matches the name of a help topic, `help` prints the description associated with that topic. Otherwise, `help` performs prefix matching and prints the descriptions of all matching help topics.

The return status is zero unless no command matches *pattern*.

**`let` ¶**

```
let expression [expression ...]
```

The `let` builtin allows arithmetic to be performed on shell variables. Each *expression* is evaluated as an arithmetic expression according to the rules given below in Shell Arithmetic. If the last *expression* evaluates to 0, `let` returns 1; otherwise `let` returns 0.

**`local` ¶**

```
local [option] name[=value] ...
```

For each argument, create a local variable named *name*, and assign it *value*. The *option* can be any of the options accepted by `declare`. `local` can only be used within a function; it makes the variable *name* have a visible scope restricted to that function and its children. It is an error to use `local` when not within a function.

If *name* is ‘-’, it makes the set of shell options local to the function in which `local` is invoked: any shell options changed using the `set` builtin inside the function after the call to `local` are restored to their original values when the function returns. The restore is performed as if a series of `set` commands were executed to restore the values that were in place before the function.

With no operands, `local` writes a list of local variables to the standard output.

The return status is zero unless `local` is used outside a function, an invalid *name* is supplied, or *name* is a readonly variable.

**`logout` ¶**

```
logout [n]
```

Exit a login shell, returning a status of *n* to the shell’s parent.

**`mapfile` ¶**

```
mapfile [-d delim] [-n count] [-O origin] [-s count]
    [-t] [-u fd] [-C callback] [-c quantum] [array]
```

Read lines from the standard input, or from file descriptor *fd* if the -u option is supplied, into the indexed array variable *array*. The variable `MAPFILE` is the default *array*. Options, if supplied, have the following meanings:

**`-d`**

Use the first character of *delim* to terminate each input line, rather than newline. If *delim* is the empty string, `mapfile` will terminate a line when it reads a NUL character.

**`-n`**

Copy at most *count* lines. If *count* is 0, copy all lines.

**`-O`**

Begin assigning to *array* at index *origin*. The default index is 0.

**`-s`**

Discard the first *count* lines read.

**`-t`**

Remove a trailing *delim* (default newline) from each line read.

**`-u`**

Read lines from file descriptor *fd* instead of the standard input.

**`-C`**

Evaluate *callback* each time *quantum* lines are read. The -c option specifies *quantum*.

**`-c`**

Specify the number of lines read between each call to *callback*.

If -C is specified without -c, the default quantum is 5000. When *callback* is evaluated, it is supplied the index of the next array element to be assigned and the line to be assigned to that element as additional arguments. *callback* is evaluated after the line is read but before the array element is assigned.

If not supplied with an explicit origin, `mapfile` will clear *array* before assigning to it.

`mapfile` returns zero unless an invalid option or option argument is supplied, *array* is invalid or unassignable, or if *array* is not an indexed array.

**`printf` ¶**

```
printf [-v var] format [arguments]
```

Write the formatted *arguments* to the standard output under the control of the *format*. The -v option assigns the output to the variable *var* rather than printing it to the standard output.

The *format* is a character string which contains three types of objects: plain characters, which are simply copied to standard output, character escape sequences, which are converted and copied to the standard output, and format specifications, each of which causes printing of the next successive *argument*. In addition to the standard `printf(3)` format characters `cCsSndiouxXeEfFgGaA`, `printf` interprets the following additional format specifiers:

**`%b`**

Causes `printf` to expand backslash escape sequences in the corresponding *argument* in the same way as `echo -e` (see Bash Builtin Commands).

**`%q`**

Causes `printf` to output the corresponding *argument* in a format that can be reused as shell input. `%q` and `%Q`P use the ANSI-C quoting style (see ANSI-C Quoting) if any characters in the argument string require it, and backslash quoting otherwise. If the format string uses the `printf` *alternate form*, these two formats quote the argument string using single quotes.

**`%Q`**

like `%q`, but applies any supplied precision to the *argument* before quoting it.

**`%(*datefmt*)T`**

Causes `printf` to output the date-time string resulting from using *datefmt* as a format string for `strftime`(3). The corresponding *argument* is an integer representing the number of seconds since the epoch. This format specifier recognizes Two special argument values: -1 represents the current time, and -2 represents the time the shell was invoked. If no argument is specified, conversion behaves as if -1 had been supplied. This is an exception to the usual `printf` behavior.

The %b, %q, and %T format specifiers all use the field width and precision arguments from the format specification and write that many bytes from (or use that wide a field for) the expanded argument, which usually contains more characters than the original.

The %n format specifier accepts a corresponding argument that is treated as a shell variable name.

The %s and %c format specifiers accept an l (long) modifier, which forces them to convert the argument string to a wide-character string and apply any supplied field width and precision in terms of characters, not bytes. The %S and %C format specifiers are equivalent to %ls and %lc, respectively.

Arguments to non-string format specifiers are treated as C language constants, except that a leading plus or minus sign is allowed, and if the leading character is a single or double quote, the value is the numeric value of the following character, using the current locale.

The *format* is reused as necessary to consume all of the *arguments*. If the *format* requires more *arguments* than are supplied, the extra format specifications behave as if a zero value or null string, as appropriate, had been supplied. The return value is zero on success, non-zero if an invalid option is supplied or a write or assignment error occurs.

**`read` ¶**

```
read [-Eers] [-a aname] [-d delim] [-i text] [-n nchars]
    [-N nchars] [-p prompt] [-t timeout] [-u fd] [name ...]
```

Read one line from the standard input, or from the file descriptor *fd* supplied as an argument to the -u option, split it into words as described above in Word Splitting, and assign the first word to the first *name*, the second word to the second *name*, and so on. If there are more words than names, the remaining words and their intervening delimiters are assigned to the last *name*. If there are fewer words read from the input stream than names, the remaining names are assigned empty values. The characters in the value of the `IFS` variable are used to split the line into words using the same rules the shell uses for expansion (described above in Word Splitting). The backslash character ‘\’ removes any special meaning for the next character read and is used for line continuation.

Options, if supplied, have the following meanings:

**`-a *aname*`**

The words are assigned to sequential indices of the array variable *aname*, starting at 0. All elements are removed from *aname* before the assignment. Other *name* arguments are ignored.

**`-d *delim*`**

The first character of *delim* terminates the input line, rather than newline. If *delim* is the empty string, `read` will terminate a line when it reads a NUL character.

**`-e`**

If the standard input is coming from a terminal, `read` uses Readline (see Command Line Editing) to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings, but uses Readline’s default filename completion.

**`-E`**

If the standard input is coming from a terminal, `read` uses Readline (see Command Line Editing) to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings, but uses Bash’s default completion, including programmable completion.

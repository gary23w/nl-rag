---
title: "Bash Reference Manual (part 4/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 4/15
---

# Bash Reference Manual

**`*`**

Matches any string, including the null string. When the `globstar` shell option is enabled, and ‘*’ is used in a filename expansion context, two adjacent ‘*’s used as a single pattern match all files and zero or more directories and subdirectories. If followed by a ‘/’, two adjacent ‘*’s match only directories and subdirectories.

**`?`**

Matches any single character.

**`[…]`**

Matches any one of the characters enclosed between the brackets. This is known as a *bracket expression* and matches a single character. A pair of characters separated by a hyphen denotes a *range expression*; any character that falls between those two characters, inclusive, using the current locale’s collating sequence and character set, matches. If the first character following the ‘[’ is a ‘!’ or a ‘^’ then any character not within the range matches. To match a ‘−’, include it as the first or last character in the set. To match a ‘]’, include it as the first character in the set.

The sorting order of characters in range expressions, and the characters included in the range, are determined by the current locale and the values of the `LC_COLLATE` and `LC_ALL` shell variables, if set.

For example, in the default C locale, ‘[a-dx-z]’ is equivalent to ‘[abcdxyz]’. Many locales sort characters in dictionary order, and in these locales ‘[a-dx-z]’ is typically not equivalent to ‘[abcdxyz]’; it might be equivalent to ‘[aBbCcDdxYyZz]’, for example. To obtain the traditional interpretation of ranges in bracket expressions, you can force the use of the C locale by setting the `LC_COLLATE` or `LC_ALL` environment variable to the value ‘C’, or enable the `globasciiranges` shell option.

Within a bracket expression, *character classes* can be specified using the syntax `[:`*class*`:]`, where *class* is one of the following classes defined in the POSIX standard:

```
alnum   alpha   ascii   blank   cntrl   digit   graph   lower
print   punct   space   upper   word    xdigit
```

A character class matches any character belonging to that class. The `word` character class matches letters, digits, and the character ‘_’.

For instance, the following pattern will match any character belonging to the `space` character class in the current locale, then any upper case letter or ‘!’, a dot, and finally any lower case letter or a hyphen.

```
[[:space:]][[:upper:]!].[-[:lower:]]
```

Within a bracket expression, an *equivalence class* can be specified using the syntax `[=`*c*`=]`, which matches all characters with the same collation weight (as defined by the current locale) as the character *c*.

Within a bracket expression, the syntax `[.`*symbol*`.]` matches the collating symbol *symbol*.

If the `extglob` shell option is enabled using the `shopt` builtin, the shell recognizes several extended pattern matching operators. In the following description, a *pattern-list* is a list of one or more patterns separated by a ‘|’. When matching filenames, the `dotglob` shell option determines the set of filenames that are tested, as described above. Composite patterns may be formed using one or more of the following sub-patterns:

**`?(*pattern-list*)`**

Matches zero or one occurrence of the given patterns.

**`*(*pattern-list*)`**

Matches zero or more occurrences of the given patterns.

**`+(*pattern-list*)`**

Matches one or more occurrences of the given patterns.

**`@(*pattern-list*)`**

Matches one of the given patterns.

**`!(*pattern-list*)`**

Matches anything except one of the given patterns.

The `extglob` option changes the behavior of the parser, since the parentheses are normally treated as operators with syntactic meaning. To ensure that extended matching patterns are parsed correctly, make sure that `extglob` is enabled before parsing constructs containing the patterns, including shell functions and command substitutions.

When matching filenames, the `dotglob` shell option determines the set of filenames that are tested: when `dotglob` is enabled, the set of filenames includes all files beginning with ‘.’, but the filenames . and .. must be matched by a pattern or sub-pattern that begins with a dot; when it is disabled, the set does not include any filenames beginning with ‘.’ unless the pattern or sub-pattern begins with a ‘.’. If the `globskipdots` shell option is enabled, the filenames . and .. never appear in the set. As above, ‘.’ only has a special meaning when matching filenames.

Complicated extended pattern matching against long strings is slow, especially when the patterns contain alternations and the strings contain multiple matches. Using separate matches against shorter strings, or using arrays of strings instead of a single long string, may be faster.

#### 3.5.9 Quote Removal

After the preceding expansions, all unquoted occurrences of the characters ‘\’, ‘'’, and ‘"’ that did not result from one of the above expansions are removed.

### 3.6 Redirections

Before a command is executed, its input and output may be *redirected* using a special notation interpreted by the shell. *Redirection* allows commands’ file handles to be duplicated, opened, closed, made to refer to different files, and can change the files the command reads from and writes to. When used with the `exec` builtin, redirections modify file handles in the current shell execution environment. The following redirection operators may precede or appear anywhere within a simple command or may follow a command. Redirections are processed in the order they appear, from left to right.

Each redirection that may be preceded by a file descriptor number may instead be preceded by a word of the form {*varname*}. In this case, for each redirection operator except `>&-` and `<&-`, the shell allocates a file descriptor greater than or equal to 10 and assigns it to {*varname*}. If {*varname*} precedes `>&-` or `<&-`, the value of *varname* defines the file descriptor to close. If {*varname*} is supplied, the redirection persists beyond the scope of the command, which allows the shell programmer to manage the file descriptor’s lifetime manually without using the `exec` builtin. The `varredir_close` shell option manages this behavior (see The Shopt Builtin).

In the following descriptions, if the file descriptor number is omitted, and the first character of the redirection operator is ‘<’, the redirection refers to the standard input (file descriptor 0). If the first character of the redirection operator is ‘>’, the redirection refers to the standard output (file descriptor 1).

The *word* following the redirection operator in the following descriptions, unless otherwise noted, is subjected to brace expansion, tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, quote removal, filename expansion, and word splitting. If it expands to more than one word, Bash reports an error.

The order of redirections is significant. For example, the command

```
ls > dirlist 2>&1
```

directs both standard output (file descriptor 1) and standard error (file descriptor 2) to the file *dirlist*, while the command

```
ls 2>&1 > dirlist
```

directs only the standard output to file *dirlist*, because the standard error was made a copy of the standard output before the standard output was redirected to *dirlist*.

Bash handles several filenames specially when they are used in redirections, as described in the following table. If the operating system on which Bash is running provides these special files, Bash uses them; otherwise it emulates them internally with the behavior described below.

**`/dev/fd/*fd*`**

If *fd* is a valid integer, duplicate file descriptor *fd*.

**`/dev/stdin`**

File descriptor 0 is duplicated.

**`/dev/stdout`**

File descriptor 1 is duplicated.

**`/dev/stderr`**

File descriptor 2 is duplicated.

**`/dev/tcp/*host*/*port*`**

If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding TCP socket.

**`/dev/udp/*host*/*port*`**

If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding UDP socket.

A failure to open or create a file causes the redirection to fail.

Redirections using file descriptors greater than 9 should be used with care, as they may conflict with file descriptors the shell uses internally.

#### 3.6.1 Redirecting Input

Redirecting input opens the file whose name results from the expansion of *word* for reading on file descriptor `n`, or the standard input (file descriptor 0) if `n` is not specified.

The general format for redirecting input is:

```
[n]<word
```

#### 3.6.2 Redirecting Output

Redirecting output opens the file whose name results from the expansion of *word* for writing on file descriptor *n*, or the standard output (file descriptor 1) if *n* is not specified. If the file does not exist it is created; if it does exist it is truncated to zero size.

The general format for redirecting output is:

```
[n]>[|]word
```

If the redirection operator is ‘>’, and the `noclobber` option to the `set` builtin command has been enabled, the redirection fails if the file whose name results from the expansion of *word* exists and is a regular file. If the redirection operator is ‘>|’, or the redirection operator is ‘>’ and the `noclobber` option to the `set` builtin is not enabled, Bash attempts the redirection even if the file named by *word* exists.

#### 3.6.3 Appending Redirected Output

Redirecting output in this fashion opens the file whose name results from the expansion of *word* for appending on file descriptor *n*, or the standard output (file descriptor 1) if *n* is not specified. If the file does not exist it is created.

The general format for appending output is:

```
[n]>>word
```

#### 3.6.4 Redirecting Standard Output and Standard Error

This construct redirects both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to the file whose name is the expansion of *word*.

There are two formats for redirecting standard output and standard error:

```
&>word
```

and

```
>&word
```

Of the two forms, the first is preferred. This is semantically equivalent to

```
>word 2>&1
```

When using the second form, *word* may not expand to a number or ‘-’. If it does, other redirection operators apply (see Duplicating File Descriptors below) for compatibility reasons.

#### 3.6.5 Appending Standard Output and Standard Error

This construct appends both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to the file whose name is the expansion of *word*.

The format for appending standard output and standard error is:

```
&>>word
```

This is semantically equivalent to

```
>>word 2>&1
```

(see Duplicating File Descriptors below).

#### 3.6.6 Here Documents

This type of redirection instructs the shell to read input from the current source until it reads a line containing only *delimiter* (with no trailing blanks). All of the lines read up to that point then become the standard input (or file descriptor *n* if *n* is specified) for a command.

The format of here-documents is:

```
[n]<<[−]word
        here-document
delimiter
```

The shell does not perform parameter and variable expansion, command substitution, arithmetic expansion, or filename expansion on *word*.

If any part of *word* is quoted, the *delimiter* is the result of quote removal on *word*, and the lines in the here-document are not expanded. If *word* is unquoted, *delimiter* is *word* itself, and the here-document text is treated similarly to a double-quoted string: all lines of the here-document are subjected to parameter expansion, command substitution, and arithmetic expansion, the character sequence `\newline` is treated literally, and ‘\’ must be used to quote the characters ‘\’, ‘$’, and ‘`’; however, double quote characters have no special meaning.

If the redirection operator is ‘<<-’, the shell strips leading tab characters are stripped from input lines and the line containing *delimiter*. This allows here-documents within shell scripts to be indented in a natural fashion.

If the delimiter is not quoted, the `\<newline>` sequence is treated as a line continuation: the two lines are joined and the backslash-newline is removed. This happens while reading the here-document, before the check for the ending delimiter, so joined lines can form the end delimiter.

#### 3.6.7 Here Strings

A variant of here documents, the format is:

```
[n]<<< word
```

The *word* undergoes tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal. Filename expansion and word splitting are not performed. The result is supplied as a single string, with a newline appended, to the command on its standard input (or file descriptor *n* if *n* is specified).

#### 3.6.8 Duplicating File Descriptors

The redirection operator

```
[n]<&word
```

is used to duplicate input file descriptors. If *word* expands to one or more digits, file descriptor *n* is made to be a copy of that file descriptor. It is a redirection error if the digits in *word* do not specify a file descriptor open for input. If *word* evaluates to ‘-’, file descriptor *n* is closed. If *n* is not specified, this uses the standard input (file descriptor 0).

The operator

```
[n]>&word
```

is used similarly to duplicate output file descriptors. If *n* is not specified, this uses the standard output (file descriptor 1). It is a redirection error if the digits in *word* do not specify a file descriptor open for output. If *word* evaluates to ‘-’, file descriptor *n* is closed. As a special case, if *n* is omitted, and *word* does not expand to one or more digits or ‘-’, this redirects the standard output and standard error as described previously.

#### 3.6.9 Moving File Descriptors

The redirection operator

```
[n]<&digit-
```

moves the file descriptor *digit* to file descriptor *n*, or the standard input (file descriptor 0) if *n* is not specified. *digit* is closed after being duplicated to *n*.

Similarly, the redirection operator

```
[n]>&digit-
```

moves the file descriptor *digit* to file descriptor *n*, or the standard output (file descriptor 1) if *n* is not specified.

#### 3.6.10 Opening File Descriptors for Reading and Writing

The redirection operator

```
[n]<>word
```

opens the file whose name is the expansion of *word* for both reading and writing on file descriptor *n*, or on file descriptor 0 if *n* is not specified. If the file does not exist, it is created.

### 3.7 Executing Commands

#### 3.7.1 Simple Command Expansion

When the shell executes a simple command, it performs the following expansions, assignments, and redirections, from left to right, in the following order.

1. The words that the parser has marked as variable assignments (those preceding the command name) and redirections are saved for later processing.
2. The words that are not variable assignments or redirections are expanded (see Shell Expansions). If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments.
3. Redirections are performed as described above (see Redirections).
4. The text after the ‘=’ in each variable assignment undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before being assigned to the variable.

If no command name results, the variable assignments affect the current shell environment. In the case of such a command (one that consists only of assignment statements and redirections), assignment statements are performed before redirections. Otherwise, the variables are added to the environment of the executed command and do not affect the current shell environment. If any of the assignments attempts to assign a value to a readonly variable, an error occurs, and the command exits with a non-zero status.

If no command name results, redirections are performed, but do not affect the current shell environment. A redirection error causes the command to exit with a non-zero status.

If there is a command name left after expansion, execution proceeds as described below. Otherwise, the command exits. If one of the expansions contained a command substitution, the exit status of the command is the exit status of the last command substitution performed. If there were no command substitutions, the command exits with a zero status.

#### 3.7.3 Command Execution Environment

The shell has an *execution environment*, which consists of the following:

- Open files inherited by the shell at invocation, as modified by redirections supplied to the `exec` builtin.
- The current working directory as set by `cd`, `pushd`, or `popd`, or inherited by the shell at invocation.
- The file creation mode mask as set by `umask` or inherited from the shell’s parent.
- Current traps set by `trap`.
- Shell parameters that are set by variable assignment or with `set` or inherited from the shell’s parent in the environment.
- Shell functions defined during execution or inherited from the shell’s parent in the environment.
- Options enabled at invocation (either by default or with command-line arguments) or by `set`.
- Options enabled by `shopt` (see The Shopt Builtin).
- Shell aliases defined with `alias` (see Aliases).
- Various process IDs, including those of background jobs (see Lists of Commands), the value of `$$`, and the value of `$PPID`.

When a simple command other than a builtin or shell function is to be executed, it is invoked in a separate execution environment that consists of the following. Unless otherwise noted, the values are inherited from the shell.

- The shell’s open files, plus any modifications and additions specified by redirections to the command.
- The current working directory.
- The file creation mode mask.
- Shell variables and functions marked for export, along with variables exported for the command, passed in the environment (see Environment).
- Traps caught by the shell are reset to the values inherited from the shell’s parent, and traps ignored by the shell are ignored.

A command invoked in this separate environment cannot affect the shell’s execution environment.

A *subshell* is a copy of the shell process.

Command substitution, commands grouped with parentheses, and asynchronous commands are invoked in a subshell environment that is a duplicate of the shell environment, except that traps caught by the shell are reset to the values that the shell inherited from its parent at invocation. Builtin commands that are invoked as part of a pipeline, except possibly in the last element depending on the value of the `lastpipe` shell option (see The Shopt Builtin), are also executed in a subshell environment. Changes made to the subshell environment cannot affect the shell’s execution environment.

When the shell is in POSIX mode, subshells spawned to execute command substitutions inherit the value of the -e option from the parent shell. When not in POSIX mode, Bash clears the -e option in such subshells See the description of the `inherit_errexit` shell option (see Bash Builtin Commands) for how to control this behavior when not in POSIX mode.

If a command is followed by a ‘&’ and job control is not active, the default standard input for the command is the empty file /dev/null. Otherwise, the invoked command inherits the file descriptors of the calling shell as modified by redirections.

#### 3.7.4 Environment

When a program is invoked it is given an array of strings called the *environment*. This is a list of name-value pairs, of the form `name=value`.

Bash provides several ways to manipulate the environment. On invocation, the shell scans its own environment and creates a parameter for each name found, automatically marking it for `export` to child processes. Executed commands inherit the environment. The `export`, ‘declare -x’, and `unset` commands modify the environment by adding and deleting parameters and functions. If the value of a parameter in the environment is modified, the new value automatically becomes part of the environment, replacing the old. The environment inherited by any executed command consists of the shell’s initial environment, whose values may be modified in the shell, less any pairs removed by the `unset` and ‘export -n’ commands, plus any additions via the `export` and ‘declare -x’ commands.

If any parameter assignment statements, as described in Shell Parameters, appear before a simple command, the variable assignments are part of that command’s environment for as long as it executes. These assignment statements affect only the environment seen by that command. If these assignments precede a call to a shell function, the variables are local to the function and exported to that function’s children.

If the -k option is set (see The Set Builtin), then all parameter assignments are placed in the environment for a command, not just those that precede the command name.

When Bash invokes an external command, the variable ‘$_’ is set to the full pathname of the command and passed to that command in its environment.

#### 3.7.5 Exit Status

The exit status of an executed command is the value returned by the `waitpid` system call or equivalent function. Exit statuses fall between 0 and 255, though, as explained below, the shell may use values above 125 specially. Exit statuses from shell builtins and compound commands are also limited to this range. Under certain circumstances, the shell will use special values to indicate specific failure modes.

For the shell’s purposes, a command which exits with a zero exit status has succeeded. So while an exit status of zero indicates success, a non-zero exit status indicates failure. This seemingly counter-intuitive scheme is used so there is one well-defined way to indicate success and a variety of ways to indicate various failure modes.

When a command terminates on a fatal signal whose number is *N*, Bash uses the value 128+*N* as the exit status.

If a command is not found, the child process created to execute it returns a status of 127. If a command is found but is not executable, the return status is 126.

If a command fails because of an error during expansion or redirection, the exit status is greater than zero.

The exit status is used by the Bash conditional commands (see Conditional Constructs) and some of the list constructs (see Lists of Commands).

All of the Bash builtins return an exit status of zero if they succeed and a non-zero status on failure, so they may be used by the conditional and list constructs. All builtins return an exit status of 2 to indicate incorrect usage, generally invalid options or missing arguments.

The exit status of the last command is available in the special parameter $? (see Special Parameters).

Bash itself returns the exit status of the last command executed, unless a syntax error occurs, in which case it exits with a non-zero value. See also the `exit` builtin command (see Bourne Shell Builtins.

#### 3.7.6 Signals

When Bash is interactive, in the absence of any traps, it ignores `SIGTERM` (so that ‘kill 0’ does not kill an interactive shell), and catches and handles `SIGINT` (so that the `wait` builtin is interruptible). When Bash receives a `SIGINT`, it breaks out of any executing loops. In all cases, Bash ignores `SIGQUIT`. If job control is in effect (see Job Control), Bash ignores `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.

The `trap` builtin modifies the shell’s signal handling, as described below (see Bourne Shell Builtins.

Non-builtin commands Bash executes have signal handlers set to the values inherited by the shell from its parent, unless `trap` sets them to be ignored, in which case the child process will ignore them as well. When job control is not in effect, asynchronous commands ignore `SIGINT` and `SIGQUIT` in addition to these inherited handlers. Commands run as a result of command substitution ignore the keyboard-generated job control signals `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.

The shell exits by default upon receipt of a `SIGHUP`. Before exiting, an interactive shell resends the `SIGHUP` to all jobs, running or stopped. The shell sends `SIGCONT` to stopped jobs to ensure that they receive the `SIGHUP` (See Job Control, for more information about running and stopped jobs). To prevent the shell from sending the `SIGHUP` signal to a particular job, remove it from the jobs table with the `disown` builtin (see Job Control Builtins) or mark it not to receive `SIGHUP` using `disown -h`.

If the `huponexit` shell option has been set using `shopt` (see The Shopt Builtin), Bash sends a `SIGHUP` to all jobs when an interactive login shell exits.

If Bash is waiting for a command to complete and receives a signal for which a trap has been set, it will not execute the trap until the command completes. If Bash is waiting for an asynchronous command via the `wait` builtin, and it receives a signal for which a trap has been set, the `wait` builtin will return immediately with an exit status greater than 128, immediately after which the shell executes the trap.

When job control is not enabled, and Bash is waiting for a foreground command to complete, the shell receives keyboard-generated signals such as `SIGINT` (usually generated by ‘^C’) that users commonly intend to send to that command. This happens because the shell and the command are in the same process group as the terminal, and ‘^C’ sends `SIGINT` to all processes in that process group. Since Bash does not enable job control by default when the shell is not interactive, this scenario is most common in non-interactive shells.

When job control is enabled, and Bash is waiting for a foreground command to complete, the shell does not receive keyboard-generated signals, because it is not in the same process group as the terminal. This scenario is most common in interactive shells, where Bash attempts to enable job control by default. See Job Control, for a more in-depth discussion of process groups.

When job control is not enabled, and Bash receives `SIGINT` while waiting for a foreground command, it waits until that foreground command terminates and then decides what to do about the `SIGINT`:

1. If the command terminates due to the `SIGINT`, Bash concludes that the user meant to send the `SIGINT` to the shell as well, and acts on the `SIGINT` (e.g., by running a `SIGINT` trap, exiting a non-interactive shell, or returning to the top level to read a new command).
2. If the command does not terminate due to `SIGINT`, the program handled the `SIGINT` itself and did not treat it as a fatal signal. In that case, Bash does not treat `SIGINT` as a fatal signal, either, instead assuming that the `SIGINT` was used as part of the program’s normal operation (e.g., `emacs` uses it to abort editing commands) or deliberately discarded. However, Bash will run any trap set on `SIGINT`, as it does with any other trapped signal it receives while it is waiting for the foreground command to complete, for compatibility.

When job control is enabled, Bash does not receive keyboard-generated signals such as `SIGINT` while it is waiting for a foreground command. An interactive shell does not pay attention to the `SIGINT`, even if the foreground command terminates as a result, other than noting its exit status. If the shell is not interactive, and the foreground command terminates due to the `SIGINT`, Bash pretends it received the `SIGINT` itself (scenario 1 above), for compatibility.

### 3.8 Shell Scripts

A shell script is a text file containing shell commands. When such a file is used as the first non-option argument when invoking Bash, and neither the -c nor -s option is supplied (see Invoking Bash), Bash reads and executes commands from the file, then exits. This mode of operation creates a non-interactive shell. If the filename does not contain any slashes, the shell first searches for the file in the current directory, and looks in the directories in `$PATH` if not found there.

Bash tries to determine whether the file is a text file or a binary, and will not execute files it determines to be binaries.

When Bash runs a shell script, it sets the special parameter `0` to the name of the file, rather than the name of the shell, and the positional parameters are set to the remaining arguments, if any are given. If no additional arguments are supplied, the positional parameters are unset.

A shell script may be made executable by using the `chmod` command to turn on the execute bit. When Bash finds such a file while searching the `$PATH` for a command, it creates a new instance of itself to execute it. In other words, executing

```
filename arguments
```

is equivalent to executing

```
bash filename arguments
```

if `filename` is an executable shell script. This subshell reinitializes itself, so that the effect is as if a new shell had been invoked to interpret the script, with the exception that the locations of commands remembered by the parent (see the description of `hash` in Bourne Shell Builtins) are retained by the child.

The GNU operating system, and most versions of Unix, make this a part of the operating system’s command execution mechanism. If the first line of a script begins with the two characters ‘#!’, the remainder of the line specifies an interpreter for the program and, depending on the operating system, one or more optional arguments for that interpreter. Thus, you can specify Bash, `awk`, Perl, or some other interpreter and write the rest of the script file in that language.

The arguments to the interpreter consist of one or more optional arguments following the interpreter name on the first line of the script file, followed by the name of the script file, followed by the rest of the arguments supplied to the script. The details of how the interpreter line is split into an interpreter name and a set of arguments vary across systems. Bash will perform this action on operating systems that do not handle it themselves. Note that some older versions of Unix limit the interpreter name and a single argument to a maximum of 32 characters, so it’s not portable to assume that using more than one argument will work.

Bash scripts often begin with `#! /bin/bash` (assuming that Bash has been installed in /bin), since this ensures that Bash will be used to interpret the script, even if it is executed under another shell. It’s a common idiom to use `env` to find `bash` even if it’s been installed in another directory: `#!/usr/bin/env bash` will find the first occurrence of `bash` in `$PATH`.

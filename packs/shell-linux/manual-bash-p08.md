---
title: "Bash Reference Manual (part 8/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 8/15
---

## 6 Bash Features

This chapter describes features unique to Bash.

### 6.1 Invoking Bash

```
bash [long-opt] [-ir] [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] [argument ...]
bash [long-opt] [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] -c string [argument ...]
bash [long-opt] -s [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] [argument ...]
```

All of the single-character options used with the `set` builtin (see The Set Builtin) can be used as options when the shell is invoked. In addition, there are several multi-character options that you can use. These options must appear on the command line before the single-character options to be recognized.

**`--debugger`**

Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see The Shopt Builtin for a description of the `extdebug` option to the `shopt` builtin).

**`--dump-po-strings`**

Print a list of all double-quoted strings preceded by ‘$’ on the standard output in the GNU `gettext` PO (portable object) file format. Equivalent to -D except for the output format.

**`--dump-strings`**

Equivalent to -D.

**`--help`**

Display a usage message on standard output and exit successfully.

**`--init-file *filename*`**

**`--rcfile *filename*`**

Execute commands from *filename* (instead of ~/.bashrc) in an interactive shell.

**`--login`**

Equivalent to -l.

**`--noediting`**

Do not use the GNU Readline library (see Command Line Editing) to read command lines when the shell is interactive.

**`--noprofile`**

Don’t load the system-wide startup file /etc/profile or any of the personal initialization files ~/.bash_profile, ~/.bash_login, or ~/.profile when Bash is invoked as a login shell.

**`--norc`**

Don’t read the ~/.bashrc initialization file in an interactive shell. This is on by default if the shell is invoked as `sh`.

**`--posix`**

Enable POSIX mode; change the behavior of Bash where the default operation differs from the POSIX standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. See Bash and POSIX, for a description of the Bash POSIX mode.

**`--restricted`**

Equivalent to -r. Make the shell a restricted shell (see The Restricted Shell).

**`--verbose`**

Equivalent to -v. Print shell input lines as they’re read.

**`--version`**

Show version information for this instance of Bash on the standard output and exit successfully.

There are several single-character options that may be supplied at invocation which are not available with the `set` builtin.

**`-c`**

Read and execute commands from the first non-option argument *command_string*, then exit. If there are arguments after the *command_string*, the first argument is assigned to `$0` and any remaining arguments are assigned to the positional parameters. The assignment to `$0` sets the name of the shell, which is used in warning and error messages.

**`-i`**

Force the shell to run interactively. Interactive shells are described in Interactive Shells.

**`-l`**

Make this shell act as if it had been directly invoked by login. When the shell is interactive, this is equivalent to starting a login shell with ‘exec -l bash’. When the shell is not interactive, it will read and execute the login shell startup files. ‘exec bash -l’ or ‘exec bash --login’ will replace the current shell with a Bash login shell. See Bash Startup Files, for a description of the special behavior of a login shell.

**`-r`**

Make the shell a restricted shell (see The Restricted Shell).

**`-s`**

If this option is present, or if no arguments remain after option processing, then Bash reads commands from the standard input. This option allows the positional parameters to be set when invoking an interactive shell or when reading input through a pipe.

**`-D`**

Print a list of all double-quoted strings preceded by ‘$’ on the standard output. These are the strings that are subject to language translation when the current locale is not `C` or `POSIX` (see Locale-Specific Translation). This implies the -n option; no commands will be executed.

**`[-+]O [*shopt_option*]`**

*shopt_option* is one of the shell options accepted by the `shopt` builtin (see The Shopt Builtin). If *shopt_option* is present, -O sets the value of that option; +O unsets it. If *shopt_option* is not supplied, Bash prints the names and values of the shell options accepted by `shopt` on the standard output. If the invocation option is +O, the output is displayed in a format that may be reused as input.

**`--`**

A `--` signals the end of options and disables further option processing. Any arguments after the `--` are treated as a shell script filename (see Shell Scripts) and arguments passed to that script.

**`-`**

Equivalent to `--`.

A *login shell* is one whose first character of argument zero is ‘-’, or one invoked with the --login option.

An *interactive shell* is one started without non-option arguments, unless -s is specified, without specifying the -c option, and whose standard input and standard error are both connected to terminals (as determined by *isatty(3)*), or one started with the -i option. See Interactive Shells, for more information.

If arguments remain after option processing, and neither the -c nor the -s option has been supplied, the first argument is treated as the name of a file containing shell commands (see Shell Scripts). When Bash is invoked in this fashion, `$0` is set to the name of the file, and the positional parameters are set to the remaining arguments. Bash reads and executes commands from this file, then exits. Bash’s exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0. Bash first attempts to open the file in the current directory, and, if no file is found, searches the directories in `PATH` for the script.

### 6.2 Bash Startup Files

This section describes how Bash executes its startup files. If any of the files exist but cannot be read, Bash reports an error. Tildes are expanded in filenames as described above under Tilde Expansion (see Tilde Expansion).

Interactive shells are described in Interactive Shells.

#### Invoked as an interactive login shell, or with --login

When Bash is invoked as an interactive login shell, or as a non-interactive shell with the --login option, it first reads and executes commands from the file /etc/profile, if that file exists. After reading that file, it looks for ~/.bash_profile, ~/.bash_login, and ~/.profile, in that order, and reads and executes commands from the first one that exists and is readable. The --noprofile option inhibits this behavior.

When an interactive login shell exits, or a non-interactive login shell executes the `exit` builtin command, Bash reads and executes commands from the file ~/.bash_logout, if it exists.

#### Invoked as an interactive non-login shell

When Bash runs as an interactive shell that is not a login shell, it reads and executes commands from ~/.bashrc, if that file exists. The --norc option inhibits this behavior. The --rcfile *file* option causes Bash to use *file* instead of ~/.bashrc.

So, typically, your ~/.bash_profile contains the line

```
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
```

after (or before) any login-specific initializations.

#### Invoked non-interactively

When Bash is started non-interactively, to run a shell script, for example, it looks for the variable `BASH_ENV` in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. Bash behaves as if the following command were executed:

```
if [ -n "$BASH_ENV" ]; then . "$BASH_ENV"; fi
```

but does not the value of the `PATH` variable to search for the filename.

As noted above, if a non-interactive shell is invoked with the --login option, Bash attempts to read and execute commands from the login shell startup files.

#### Invoked with name `sh`

If Bash is invoked with the name `sh`, it tries to mimic the startup behavior of historical versions of `sh` as closely as possible, while conforming to the POSIX standard as well.

When invoked as an interactive login shell, or as a non-interactive shell with the --login option, it first attempts to read and execute commands from /etc/profile and ~/.profile, in that order. The --noprofile option inhibits this behavior.

When invoked as an interactive shell with the name `sh`, Bash looks for the variable `ENV`, expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. Since a shell invoked as `sh` does not attempt to read and execute commands from any other startup files, the --rcfile option has no effect.

A non-interactive shell invoked with the name `sh` does not attempt to read any other startup files.

When invoked as `sh`, Bash enters POSIX mode after reading the startup files.

#### Invoked in POSIX mode

When Bash is started in POSIX mode, as with the --posix command line option, it follows the POSIX standard for startup files. In this mode, interactive shells expand the `ENV` variable and read and execute commands from the file whose name is the expanded value. No other startup files are read.

#### Invoked by remote shell daemon

Bash attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the historical and rarely-seen remote shell daemon, usually `rshd`, or the secure shell daemon `sshd`. If Bash determines it is being run non-interactively in this fashion, it reads and executes commands from ~/.bashrc, if that file exists and is readable. Bash does not read this file if invoked as `sh`. The --norc option inhibits this behavior, and the --rcfile option makes Bash use a different file instead of ~/.bashrc, but neither `rshd` nor `sshd` generally invoke the shell with those options or allow them to be specified.

#### Invoked with unequal effective and real UID/GIDs

If Bash is started with the effective user (group) id not equal to the real user (group) id, and the -p option is not supplied, no startup files are read, shell functions are not inherited from the environment, the `SHELLOPTS`, `BASHOPTS`, `CDPATH`, and `GLOBIGNORE` variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the -p option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.

### 6.3 Interactive Shells

#### 6.3.1 What is an Interactive Shell?

An interactive shell is one started without non-option arguments (unless -s is specified) and without specifying the -c option, whose input and error output are both connected to terminals (as determined by `isatty(3)`), or one started with the -i option.

An interactive shell generally reads from and writes to a user’s terminal.

The -s invocation option may be used to set the positional parameters when an interactive shell starts.

#### 6.3.2 Is this Shell Interactive?

To determine within a startup script whether or not Bash is running interactively, test the value of the ‘-’ special parameter. It contains `i` when the shell is interactive. For example:

```
case "$-" in
*i*)	echo This shell is interactive ;;
*)	echo This shell is not interactive ;;
esac
```

Alternatively, startup scripts may examine the variable `PS1`; it is unset in non-interactive shells, and set in interactive shells. Thus:

```
if [ -z "$PS1" ]; then
        echo This shell is not interactive
else
        echo This shell is interactive
fi
```

#### 6.3.3 Interactive Shell Behavior

When the shell is running interactively, it changes its behavior in several ways.

1. Bash reads and executes startup files as described in Bash Startup Files.
2. Job Control (see Job Control) is enabled by default. When job control is in effect, Bash ignores the keyboard-generated job control signals `SIGTTIN`, `SIGTTOU`, and `SIGTSTP`.
3. Bash executes the values of the set elements of the `PROMPT_COMMAND` array variable as commands before printing the primary prompt, `$PS1` (see Bash Variables).
4. Bash expands and displays `PS1` before reading the first line of a command, and expands and displays `PS2` before reading the second and subsequent lines of a multi-line command. Bash expands and displays `PS0` after it reads a command but before executing it. See Controlling the Prompt, for a complete list of prompt string escape sequences.
5. Bash uses Readline (see Command Line Editing) to read commands from the user’s terminal.
6. Bash inspects the value of the `ignoreeof` option to `set -o` instead of exiting immediately when it receives an `EOF` on its standard input when reading a command (see The Set Builtin).
7. Bash enables Command history (see Bash History Facilities) and history expansion (see History Expansion) by default. When a shell with history enabled exits, Bash saves the command history to the file named by `$HISTFILE`.
8. Alias expansion (see Aliases) is performed by default.
9. In the absence of any traps, Bash ignores `SIGTERM` (see Signals).
10. In the absence of any traps, `SIGINT` is caught and handled (see Signals). `SIGINT` will interrupt some shell builtins.
11. An interactive login shell sends a `SIGHUP` to all jobs on exit if the `huponexit` shell option has been enabled (see Signals).
12. The -n option has no effect, whether at invocation or when using ‘set -n’ (see The Set Builtin).
13. Bash will check for mail periodically, depending on the values of the `MAIL`, `MAILPATH`, and `MAILCHECK` shell variables (see Bash Variables).
14. The shell will not exit on expansion errors due to references to unbound shell variables after ‘set -u’ has been enabled (see The Set Builtin).
15. The shell will not exit on expansion errors caused by *var* being unset or null in `${*var*:?*word*}` expansions (see Shell Parameter Expansion).
16. Redirection errors encountered by shell builtins will not cause the shell to exit.
17. When running in POSIX mode, a special builtin returning an error status will not cause the shell to exit (see Bash and POSIX).
18. A failed `exec` will not cause the shell to exit (see Bourne Shell Builtins).
19. Parser syntax errors will not cause the shell to exit.
20. If the `cdspell` shell option is enabled, the shell will attempt simple spelling correction for directory arguments to the `cd` builtin (see the description of the `cdspell` option to the `shopt` builtin in The Shopt Builtin). The `cdspell` option is only effective in interactive shells.
21. The shell will check the value of the `TMOUT` variable and exit if a command is not read within the specified number of seconds after printing `$PS1` (see Bash Variables).

### 6.4 Bash Conditional Expressions

Conditional expressions are used by the `[[` compound command (see Conditional Constructs) and the `test` and `[` builtin commands (see Bourne Shell Builtins). The `test` and `[` commands determine their behavior based on the number of arguments; see the descriptions of those commands for any other command-specific actions.

Expressions may be unary or binary, and are formed from the primaries listed below. Unary expressions are often used to examine the status of a file or shell variable. Binary operators are used for string, numeric, and file attribute comparisons.

Bash handles several filenames specially when they are used in expressions. If the operating system on which Bash is running provides these special files, Bash uses them; otherwise it emulates them internally with this behavior: If the *file* argument to one of the primaries is of the form /dev/fd/*N*, then Bash checks file descriptor *N*. If the *file* argument to one of the primaries is one of /dev/stdin, /dev/stdout, or /dev/stderr, Bash checks file descriptor 0, 1, or 2, respectively.

When used with `[[`, the ‘<’ and ‘>’ operators sort lexicographically using the current locale. The `test` command uses ASCII ordering.

Unless otherwise specified, primaries that operate on files follow symbolic links and operate on the target of the link, rather than the link itself.

**`-a *file*`**

True if *file* exists.

**`-b *file*`**

True if *file* exists and is a block special file.

**`-c *file*`**

True if *file* exists and is a character special file.

**`-d *file*`**

True if *file* exists and is a directory.

**`-e *file*`**

True if *file* exists.

**`-f *file*`**

True if *file* exists and is a regular file.

**`-g *file*`**

True if *file* exists and its set-group-id bit is set.

**`-h *file*`**

True if *file* exists and is a symbolic link.

**`-k *file*`**

True if *file* exists and its "sticky" bit is set.

**`-p *file*`**

True if *file* exists and is a named pipe (FIFO).

**`-r *file*`**

True if *file* exists and is readable.

**`-s *file*`**

True if *file* exists and has a size greater than zero.

**`-t *fd*`**

True if file descriptor *fd* is open and refers to a terminal.

**`-u *file*`**

True if *file* exists and its set-user-id bit is set.

**`-w *file*`**

True if *file* exists and is writable.

**`-x *file*`**

True if *file* exists and is executable.

**`-G *file*`**

True if *file* exists and is owned by the effective group id.

**`-L *file*`**

True if *file* exists and is a symbolic link.

**`-N *file*`**

True if *file* exists and has been modified since it was last accessed.

**`-O *file*`**

True if *file* exists and is owned by the effective user id.

**`-S *file*`**

True if *file* exists and is a socket.

**`*file1* -ef *file2*`**

True if *file1* and *file2* refer to the same device and inode numbers.

**`*file1* -nt *file2*`**

True if *file1* is newer (according to modification date) than *file2*, or if *file1* exists and *file2* does not.

**`*file1* -ot *file2*`**

True if *file1* is older than *file2*, or if *file2* exists and *file1* does not.

**`-o *optname*`**

True if the shell option *optname* is enabled. The list of options appears in the description of the -o option to the `set` builtin (see The Set Builtin).

**`-v *varname*`**

True if the shell variable *varname* is set (has been assigned a value). If *varname* is an indexed array variable name subscripted by ‘@’ or ‘*’, this returns true if the array has any set elements. If *varname* is an associative array variable name subscripted by ‘@’ or ‘*’, this returns true if an element with that key is set.

**`-R *varname*`**

True if the shell variable *varname* is set and is a name reference.

**`-z *string*`**

True if the length of *string* is zero.

**`-n *string*`**

**`*string*`**

True if the length of *string* is non-zero.

**`*string1* == *string2*`**

**`*string1* = *string2*`**

True if the strings are equal. When used with the `[[` command, this performs pattern matching as described above (see Conditional Constructs).

‘=’ should be used with the `test` command for POSIX conformance.

**`*string1* != *string2*`**

True if the strings are not equal.

**`*string1* < *string2*`**

True if *string1* sorts before *string2* lexicographically.

**`*string1* > *string2*`**

True if *string1* sorts after *string2* lexicographically.

**`*arg1* OP *arg2*`**

`OP` is one of ‘-eq’, ‘-ne’, ‘-lt’, ‘-le’, ‘-gt’, or ‘-ge’. These arithmetic binary operators return true if *arg1* is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to *arg2*, respectively. *Arg1* and *arg2* may be positive or negative integers. When used with the `[[` command, *arg1* and *arg2* are evaluated as arithmetic expressions (see Shell Arithmetic). Since the expansions the `[[` command performs on *arg1* and *arg2* can potentially result in empty strings, arithmetic expression evaluation treats those as expressions that evaluate to 0.

### 6.5 Shell Arithmetic

The shell allows arithmetic expressions to be evaluated, as one of the shell expansions or by using the `((` compound command, the `let` and `declare` builtins, the arithmetic `for` command, the `[[` conditional command, or the -i option to the `declare` builtin.

Evaluation is done in the largest fixed-width integers available, with no check for overflow, though division by 0 is trapped and flagged as an error. The operators and their precedence, associativity, and values are the same as in the C language. The following list of operators is grouped into levels of equal-precedence operators. The levels are listed in order of decreasing precedence.

**`*id*++ *id*--`**

variable post-increment and post-decrement

**`++*id* --*id*`**

variable pre-increment and pre-decrement

**`- +`**

unary minus and plus

**`! ~`**

logical and bitwise negation

**`**`**

exponentiation

**`* / %`**

multiplication, division, remainder

**`+ -`**

addition, subtraction

**`<< >>`**

left and right bitwise shifts

**`<= >= < >`**

comparison

**`== !=`**

equality and inequality

**`&`**

bitwise AND

**`^`**

bitwise exclusive OR

**`|`**

bitwise OR

**`&&`**

logical AND

**`||`**

logical OR

**`expr ? if-true-expr : if-false-expr`**

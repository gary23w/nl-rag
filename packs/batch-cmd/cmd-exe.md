---
title: "cmd.exe"
source: https://en.wikipedia.org/wiki/Cmd.exe
domain: batch-cmd
license: CC-BY-SA-4.0
tags: batch file, windows batch, cmd.exe, bat script
fetched: 2026-07-02
---

# cmd.exe

**cmd.exe**, also known as **Command Prompt** or **Windows Command Processor**, is a shell program on later versions of Windows (NT and CE families), OS/2, eComStation, ArcaOS, and ReactOS. In some versions of Windows (CE .NET 4.2, CE 5.0 and Embedded CE 6.0) it is referred to as the **Command Processor Shell**. Implementation differs between operating systems, but with significant consistency of behavior and available commands.

Older, related operating systems, DOS and Windows 9x, provided COMMAND.COM as the shell. cmd.exe replaced COMMAND.COM in the Windows product line with the introduction of NT. Current versions of Windows include PowerShell as an alternative shell that runs side-by-side with cmd.exe.

The initial version of cmd.exe for Windows NT was developed by Therese Stowell. Windows CE 2.11 was the first embedded Windows release to support a console and a Windows CE version of cmd.exe. The ReactOS implementation of cmd.exe is derived from FreeCOM, the FreeDOS command line interpreter.

## Use

### Desktop integration

In Windows, the shell is presented in the desktop via Windows Terminal or on older versions via Windows Console.

### Concurrent piping

In OS/2 and Windows, the shell supports pipes to allow both sides of a pipeline to run concurrently. As a result, it is possible to redirect the standard error stream. In contrast, COMMAND.COM uses temporary files, and runs the two sides serially, one after the other.

### Command separator

Multiple commands can be included in a single line using the command separators `&`, `&&` or `||`.

With the `&` separator, a subsequent command is executed even if the previous command indicates an error. In the following example, each of the three commands is executed, one after the other, and regardless of their exit code.

```mw
>CommandA & CommandB & CommandC
```

With the `&&` separator, a command must succeed, i.e. yield the exit code 0, for the subsequent command to execute. In the following example, `CommandB` only executes if `CommandA` completes successfully, and `CommandC` only executes if `CommandB` also completes successfully.

```mw
>CommandA && CommandB && CommandC
```

With the `||` separator, a command must fail, i.e. yield an exit code not equal 0, for the subsequent command to execute. In the following example, `CommandB` executes if `CommandA` fails, and `CommandC` executes if `CommandB` succeeds.

```mw
>CommandA || CommandB && CommandC
```

### Command line limit

The shell limits the length of a command line which includes entered text, individual environment variables that are inherited by other processes, and all environment variable expansions On Windows XP and later, the maximum length is 8191 (213-1) characters. On earlier versions, such as Windows 2000 or Windows NT 4.0, the maximum length is 2047 (211-1) characters.

### Escaping special characters

The shell reserves the following characters as special: &<>[]{}^=;!'+,`~ and whitespace. In some cases, an argument that contains such characters must be enclosed in double quotes to escape from the special character handling. For example:

```mw
>echo me & you
me
'you' is not recognized as an internal or external command,
operable program or batch file.

>echo "me & you"
"me & you"
```

## Internal commands

The following sections list internal commands for implementations of the shell on various operating systems.

### OS/2

Internal commands in OS/2:

- break
- chcp
- cd
- chdir
- cls
- copy
- date
- del
- detach
- dir
- dpath
- echo
- erase
- exit
- for
- goto
- if
- md
- mkdir
- path
- pause
- prompt
- rd
- rem
- ren
- rename
- rmdir
- set
- shift
- start
- time
- type
- ver
- verify
- vol

### Windows NT family

Internal commands in Windows NT and later:

- assoc
- break
- call
- cd
- chdir
- cls
- color
- copy
- date
- del
- dir
- dpath
- echo
- endlocal
- erase
- exit
- for
- ftype
- goto
- if
- keys
- md
- mkdir
- mklink
- move
- path
- pause
- popd
- prompt
- pushd
- rd
- rem
- ren
- rename
- rmdir
- set
- setlocal
- shift
- start
- time
- title
- type
- ver
- verify
- vol

### Windows CE

Internal commands in Windows CE .NET 4.2, Windows CE 5.0 and Windows Embedded CE 6.0:

- attrib
- call
- cd
- chdir
- cls
- copy
- date
- del
- dir
- echo
- erase
- exit
- goto
- help
- if
- md
- mkdir
- move
- path
- pause
- prompt
- pwd
- rd
- rem
- ren
- rename
- rmdir
- set
- shift
- start
- time
- title
- type

The net command is available as an external command.

### ReactOS

Internal commands in ReactOS:

- ?
- alias
- assoc
- beep
- call
- cd
- chdir
- choice
- cls
- color
- copy
- ctty
- date
- del
- delete
- delay
- dir
- dirs
- echo
- echos
- echoerr
- echoserr
- endlocal
- erase
- exit
- for
- free
- goto
- history
- if
- memory
- md
- mkdir
- mklink
- move
- path
- pause
- popd
- prompt
- pushd
- rd
- rmdir
- rem
- ren
- rename
- replace
- screen
- set
- setlocal
- shift
- start
- time
- timer
- title
- type
- ver
- verify
- vol

## Comparison with COMMAND.COM

On Windows, cmd.exe provides various user experience enhancements as compared to COMMAND.COM, including:

- More detailed error reporting for malformed commands than the generic COMMAND.COM "Bad command or file name". In OS/2, errors are reported in the chosen language of the system, their text being taken from the system message files. The `HELP` command can then be issued with the error message number to obtain further information.
- Supports using of arrow keys to scroll through command history. With COMMAND.COM, this functionality was only available in DR DOS (via HISTORY) and later via an external component called DOSKEY.
- Adds rotating command-line completion for file and folder paths, where the user can cycle through results for the prefix using the Tab ↹, and ⇧ Shift+Tab ↹ for reverse direction.
- Treats the caret character (^) as the escape character; the character following it is to be taken literally. There are special characters in cmd.exe and COMMAND.COM that are meant to alter the behavior of the command line processor. The caret character forces the command line processor to interpret them literally.
- Supports delayed variable expansion with `SETLOCAL EnableDelayedExpansion`, allowing values of variables to be calculated at runtime instead of during parsing of script before execution (Windows 2000 and later), fixing DOS idioms that made using control structures hard and complex. The extensions can be disabled, providing a stricter compatibility mode.
- The COMMAND.COM `DELTREE` command was merged into the `rd` command via the `/S` switch.
- `SetLocal` and `EndLocal` commands limit the scope of changes to the environment. Changes made to the command line environment after `SetLocal` are local to the batch file. `EndLocal` restores the previous settings.
- The `call` command allows subroutines within batch file. The COMMAND.COM `CALL` command only supports calling external batch files.
- File name parser extensions to the `set` command are comparable with C shell.
- The `set` command can perform expression evaluation.
- An expansion of the `for` command supports parsing files and arbitrary sets in addition to file names.
- The new `pushd` and `popd` commands provide access past navigated paths similar to forward and back buttons in a web browser or File Explorer.
- The conditional `if` command can perform case-insensitive comparisons and numeric equality and inequality comparisons in addition to case-sensitive string comparisons. This was available in DR-DOS, but not in PC DOS or MS-DOS.

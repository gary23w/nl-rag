---
title: "Comparison of command shells"
source: https://en.wikipedia.org/wiki/Comparison_of_command_shells
domain: shell-completion
license: CC-BY-SA-4.0
tags: shell completion, command-line completion, tab completion shells, bash completion scripts
fetched: 2026-07-02
---

# Comparison of command shells

This article catalogs comparable aspects of notable operating system shells.

## General characteristics

Shell

Usual environment

Usually invoked

Introduced

Platform-independent

Default login shell in

Default script shell in

License

Source code

availability

User interface

Mouse support

Unicode

support

ISO 8601

support

Console redirection

Stream

redirection

Configurability

Startup/shutdown

scripts

Batch scripts

Logging

Available as

statically linked,

independent

single file executable

Thompson shell

UNIX

sh

1971

—

N/a

UNIX

UNIX

—

N/a

Yes

Text-based

CLI

No

No

—

N/a

Yes

—

N/a

—

N/a

—

N/a

—

N/a

—

N/a

—

N/a

Bourne shell

1977 version

7th Ed. UNIX

sh

1977

Yes

7th Ed. UNIX

7th Ed. UNIX

,

Proprietary

Yes

Text-based

CLI

No

No

—

N/a

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Yes

(

.profile

)

Yes

(Unix feature)

No

Yes

Bourne shell

current version

Various

UNIX

sh

1977

Yes

SunOS-5.x, FreeBSD

SunOS-5.x

CDDL

Yes

Text-based

CLI

No

Yes

—

N/a

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Yes

(

.profile

)

Yes

(Unix feature)

Yes

Yes

POSIX

shell

POSIX

sh

1992

—

N/a

—

N/a

POSIX

—

N/a

—

N/a

Text-based CLI

No

Yes

if used by configured locale

—

N/a

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Unspecified

(

.profile

given as an example)

Yes

(Unix feature)

Yes

—

N/a

bash

(v4)

POSIX

bash, sh

1989

Yes

GNU

,

Linux

(default for root),

macOS

10.3–10.14

GNU

,

Linux

,

Haiku

,

macOS

10.3–10.14

GPL

Yes

Text-based CLI

No

Yes

Yes

(

printf

builtin)

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Yes

(

/etc/profile

,

.bash_profile

,

.bash_login

,

.profile

,

.bashrc

)

Yes

(Unix feature)

Yes

Yes

csh

POSIX

csh

1978

Yes

SunOS

?

BSD

Yes

Text-based CLI

No

No

?

Yes

Yes

(

stdin

,

stdout

,

stdout+stderr

)

Yes

(via variables and options)

Yes

(

~/.cshrc

,

~/.login

,

~/.logout

)

Yes

(Unix feature)

Yes

Yes

tcsh

POSIX

tcsh, csh

1983

Yes

FreeBSD

(former default for root),

formerly

Mac OS X

?

BSD

Yes

Text-based CLI

No

Yes

?

Yes

Yes

(

stdin

,

stdout

,

stdout+stderr

)

Yes

(via variables and options)

Yes

(

/etc/csh.cshrc

,

/etc/csh.login

,

~/.tcshrc

,

~/.cshrc

,

~/.history

,

~/.login

,

~/.cshdirs

)

Yes

(Unix feature)

Yes

Yes

Hamilton C shell

Win32

, OS/2

csh

1988

Yes

(OS/2 version no longer maintained)

Optional

Optional

Proprietary

No

Text-based CLI

No

No

Yes

(-t timestamp operator)

Yes

Yes

(

stdin

,

stdout

,

stdout+stderr

)

Yes

(via variables and options)

Yes

(via login.csh, startup.csh and logout.csh)

Yes

(command line option)

Yes

Yes

Scsh

POSIX

scsh

1994

Yes

?

?

BSD

-style

Yes

?

?

?

?

?

Yes

?

?

?

?

Yes

ksh

(ksh93t+)

POSIX

ksh

1983

Yes

AIX

,

HP-UX

OpenSolaris

Common Public License

Yes

Text-based CLI

No

Yes

Yes

(

printf

builtin with

%(%F)T

)

Yes

Yes

(

fds

up to 9)

Yes

(via variables and options)

Yes

(system and user's

profile

and

kshrc

)

Yes

(Unix feature)

Yes

Yes

pdksh

POSIX

ksh, sh

1989?

Yes

OpenBSD

OpenBSD

Public domain

Yes

Text-based CLI

No

No

—

N/a

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Yes

(

/etc/profile

,

.profile

)

Yes

(Unix feature)

Yes

Yes

zsh

POSIX

zsh

1990

Yes

Deepin

,

GoboLinux

,

Grml

,

macOS

10.15+,

Kali

2020.4+,

GhostBSD

26.1-R15.0p2+

Grml

,

macOS

10.15+

MIT

-style

Yes

Text-based CLI

Yes

via additional code

Yes

Yes

(various internal features involving the date, by using the

%F

strftime

format

and the

-i

option for the

fc

builtin

)

Yes

Yes

(

fds

up to 9)

Yes

(via variables, options, functions, styles, etc.)

Yes

(system and user's

zshenv

,

zprofile

,

zshrc

,

zlogin

,

zlogout

)

Yes

(Unix feature)

Yes

Yes

ash

POSIX

sh

1989

Yes

Minix

,

BusyBox

based systems

NetBSD

,

Minix

,

BusyBox

based systems

BSD

-style

Yes

Text-based CLI

No

Partial

(for BusyBox, supported in command-line editing, but not in string handling

)

—

N/a

Yes

Yes

(

arbitrary

fds

)

Yes

(via variables and options)

Yes

(

/etc/profile

,

.profile

)

Yes

(Unix feature)

Yes

Yes

CCP

CP/M

,

MP/M

(CCP)

1976 (1974)

No

CP/M

(no login),

MP/M

CP/M

,

MP/M

Freeware (originally proprietary)

Yes (originally closed-source)

Text-based

CLI

No

No

No

No

No

No

Yes (automatic via

$$$.SUB

)

Partial

(only via external

SUBMIT

command to update

$$$.SUB

)

No

Yes

COMMAND.COM

DOS

COMMAND

1980

No

(3rd party implementations, not bound to a specific DOS vendor or version, available)

DOS

,

Windows 95

,

98

,

SE

,

ME

DOS

,

Windows 95

,

98

,

SE

,

ME

vendor specific, f.e.

MS

-

EULA

,

or

BSD

/

GPL

(free clones)

No (except for OpenDOS, DR-DOS, PTS/DOS and FreeDOS)

Text-based CLI

No

No

No (except for DR-DOS)

Yes (via

COMMAND con:

or

CTTY con:

)

Yes

(

stdin

,

stdout

)

Yes (via startup parameters and environment variables, DR-DOS also supports

DIR /C /R

user-default switch command)

Yes (automatic

\AUTOEXEC.BAT

for primary shell, or explicitly via

/P

,

/P:filename.bat

or

/K

startup options)

Yes (via

CALL

command or

/C

and

/K

startup options)

No

Yes

OS/2

CMD.EXE

OS/2

,

eComStation

,

ArcaOS

CMD

1987

No

OS/2

,

eComStation

,

ArcaOS

OS/2

,

eComStation

,

ArcaOS

IBM

-

EULA

No

Text-based CLI

No

No

No

No

Yes

(

stdin

,

stdout

,

stderr

)

?

Partial (only via

/K

startup option)

Yes (via

CALL

command or

/C

and

/K

startup options)

No

Yes

Windows

CMD.EXE

Win32

CMD

1993

No

Windows

NT, 2000, XP, Server 2003, Vista

Windows

NT, 2000, XP, Server 2003, Vista

MS

-

EULA

No

Text-based CLI

No

Partial (

CHCP

65001

for

UTF-8

, but program arguments are still encoded in local codepage)

No

No

Yes

Yes (via registry, startup parameters, and environment variables)

Yes (automatic via registry, or explicitly via

/K

startup option)

Yes (via

CALL

command or

/C

and

/K

startup options)

No

Yes

4DOS

,

NDOS

DOS

,

Windows 95

,

98

,

SE

,

ME

4DOS

,

NDOS

1989 (1986)

No

(not bound to a specific OS vendor or version)

Optional

Optional

MIT License

, with restrictions

Yes

Text-based CLI with

TUI

extensions

Yes (popups, help system,

%_MOUSE

internal variable,

INKEY /M

command)

No

Yes

Yes (via

CTTY con:

, except for

DRAWBOX

,

DRAWLINE

,

DRAWVLINE

,

LIST

,

SCREEN

,

SCRPUT

,

SELECT

,

VSCRPUT

commands and file / directory coloring)

Yes

(

stdin

,

stdout

,

stderr

,

stdout+stderr

)

Yes (via

4DOS.INI

/

NDOS.INI

file, startup parameters, environment variables,

SETDOS

command)

Yes (automatic

\AUTOEXEC.BAT

for primary shell and

4START.BTM

/

4START.BAT

as well as

4EXIT.BTM

/

4EXIT.BAT

for any shell, or explicitly via

/P

,

/P:dir\filename.ext

or

/K

startup options)

Yes (via

CALL

command or

/C

and

/K

startup options)

Yes

Yes

4OS2

OS/2

,

eComStation

,

ArcaOS

4OS2

1992

No

(not bound to specific OS/2 versions)

Optional (but bundled with ArcaOS)

Optional

Freeware

Yes

Text-based CLI

No

No

No

No

Yes

(

stdin

,

stdout

,

stderr

,

stdout+stderr

)

Yes (via

4OS2.INI

file, startup parameters, environment variables,

SETDOS

command)

Yes (automatic via

4START.CMD

/

4START.BTM

as well as

4EXIT.CMD

/

4EXIT.BTM

files, or explicitly via

/K startup.cmd

option)

Yes (via

CALL

command or

/C

and

/K

startup options)

Yes

?

TCC

(formerly 4NT)

Win32

TCC

1993

No

(not bound to specific NT versions)

optional

optional

Shareware

No

Text-based CLI (

Take Command

:

GUI

)

Yes

(console mouse, popups, help system,

%_XMOUSE

,

%_YMOUSE

internal variables,

INKEY /M

command)

Yes

Yes

No

Yes

(

stdin

,

stdout

,

stderr

,

stdout+stderr

)

Yes

(via registry,

TCMD.INI

/

4NT.INI

file, startup parameters, environment variables,

SETDOS

command)

Yes

(automatic via registry and

TCSTART

/

4START

as well as

TCEXIT

/

4EXIT

, or explicitly via

/K

startup option)

Yes

(via

CALL

command or

/C

and

/K

startup options)

Yes

No

VMS DCL

OpenVMS

Automatically for login/interactive process

1977

Yes

VMS

VMS

Proprietary, bundled in VMS

by special license only

Text-based CLI

with DECwindows/Motif

Yes

Yes, at least to 1988 standard

Yes

Yes

(

sys$input

,

sys$output

assignment)

Yes

(via symbols, logical names, and options)

Yes

(SYS$MANAGER:SYLOGIN.COM and user defined LOGIN.COM)

Yes

Yes

No

PowerShell

.NET

,

.NET Framework

PowerShell

2006

Yes

Windows

10, 8, Server 2008, 7

Windows

10, 8, Server 2008, 7

MIT

-style

Yes

Graphical CLI

Yes

Yes

Yes

Yes

Yes

Yes

(via variables and options)

Yes

(%USERPROFILE%\Documents \WindowsPowerShell\Microsoft.PowerShell_profile.ps1)

Yes

(PowerShell feature)

Yes

No

rc

Plan 9

,

POSIX

rc

1989

Yes

Plan 9

,

Version 10 Unix

Plan 9

,

Version 10 Unix

MIT License

Yes

Text-based CLI

?

Yes

Yes

?

Yes

Yes

(via options)

Yes

(

$HOME/.rcrc

)

Yes

?

Yes

BeanShell

Java

?

2005

Yes

?

?

LGPL

?

?

?

Yes

?

?

Yes

?

?

?

?

No

fish

POSIX

fish

2005

Yes

GhostBSD

?

GPL

Yes

Text-based CLI

?

Yes

?

?

Yes

(

arbitrary

fds

)

Yes

(through environment variables and via web interface through

fish_config

)

Yes

(

/etc/fish/config.fish

and

~/.config/fish/config.fish

)

Yes

(Unix feature)

Yes

(

~/.config/fish/fish_history*

)

?

Ion

Redox

,

Linux

ion

2015

Yes

Redox

Redox

MIT

Yes

Text-based CLI

?

Yes

Yes

?

Yes

(

arbitrary

fds

)

Yes

(follows the XDG Base Directory spec)

Yes

(

~/.config/ion/initrc

)

Yes

Yes

(

~/.local/share/ion/history

)

Partial (not distributed as a standalone executable, but it can be built as one)

## Interactive features

Shell

Command

name

completion

Path

completion

Command

argument

completion

Wildcard

completion

Command

history

Mandatory

argument

prompt

Automatic

suggestions

Colored

directory

listings

Text

highlighting

Syntax

highlighting

Directory history,

stack or similar

features

Implicit

directory

change

Auto­correction

Integrated

environment

Snippets

Value

prompt

Menu/options

prompt

Progress

indicator

Context

sensitive

help

Thompson shell

No

No

No

No

No

No

No

?

?

No

No

No

No

No

No

No

No

No

No

Bourne shell

1977 version

No

No

No

No

No

No

No

?

?

No

No

No

No

No

No

Yes

No

External

No

Bourne shell

current version

No

Yes

No

No

Yes

No

No

Yes

Yes

No

Yes (CDPATH, pushd, popd, dirs), CDPATH since SVr4

No

No

No

No

Yes

No

External

No

POSIX

shell

No

No

No

No

Yes

No

No

Yes

Yes

No

Yes

(

CDPATH

)

No

No

No

No

Yes

No

External

No

bash

(v4.0)

Yes

Yes

Yes

Yes

Yes

No

No

Yes

Yes

No

Yes

(

CDPATH

,

pushd

,

popd

)

optional

No

No

No

Yes

Yes

External

No

csh

Yes

Yes

No

No

Yes

No

No

Yes

Yes

No

Yes

(

cdpath

,

pushd

,

popd

)

optional

No

No

No

Yes

No

External

No

tcsh

Yes

Yes

when defined

No

Yes

No

No

Yes

Yes

No

Yes

(

cdpath

,

pushd

,

popd

)

optional

Yes

No

No

Yes

No

External

No

Hamilton C shell

Yes

Yes

No

Yes

Yes

No

No

Yes

Yes

No

Yes

(

cdpath

,

pushd

,

popd

)

No

No

No

No

Yes

No

External

No

Scsh

No

No

No

No

No

No

No

?

?

No

No

No

No

No

No

Yes

No

External

No

ksh

(ksh93t+)

Yes

(extendable)

Yes

(extendable)

No

No

Yes

No

No

Yes

Yes

No

Yes

(

cdpath

builtin,

pushd

,

popd

implemented as functions)

No

No

No

No

Yes

Yes

External

No

pdksh

Yes

Yes

No

No

Yes

No

No

Yes

Yes

No

No

No

No

No

No

Yes

Yes

External

No

zsh

Yes

Yes

Yes

Yes

Yes

Yes

Yes

(via

predict-on

or user-defined

)

Yes

Yes

Third-party extension

Yes

optional

Yes

No

when defined (as ZLE widgets)

Yes

Yes

External

Yes

ash

No

No

No

No

Yes

No

No

Yes

Yes

No

No

No

No

No

No

Yes

Yes

External

No

CCP

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

COMMAND.COM

No

No

No

No

No

No

No

No

No (only in DR-DOS through

%$ON%

,

%$OFF%

,

%$HEADER%

,

%$FOOTER%

)

No

No

No

No

No (only single-stepping with COMMAND /Y

)

No

No

No (only via external

CHOICE

command, in DR-DOS also via

SWITCH

/

DRSWITCH

internal commands)

No

No

OS/2

CMD.EXE

Yes

Yes

No

No

Yes

No

No

No

No

No

No

No

No

No

No

No

No

No

No

Windows

CMD.EXE

partial

partial

No

No

Yes

(

F8

)

No

No

No

No

No

Yes

(

PUSHD

,

POPD

)

No

No

No

No

Yes (via

SET /P

command)

No

No

No

4DOS

Yes

Yes

Yes

Yes

Yes

No

No

Yes

No

No

(via popup, extended directory searches,

CDPATH

,

PUSHD

,

POPD

,

DIRHISTORY

,

DIRS

,

CDD

,

CD -

commands and

%@DIRSTACK[]

function)

Yes

No

Yes

No

Yes (via

INPUT

,

INKEY

and

ESET

commands)

Yes (via

@SELECT[]

function, and indirectly via a combination of

INKEY

,

INPUT

,

SWITCH

commands)

No

Yes

4OS2

?

?

?

?

Yes

No

No

Yes

No

No

Yes

Yes

No

?

No

?

?

No

Yes

TCC

(formerly 4NT)

Yes

Yes

Yes

Yes

Yes

No

No

Yes

No

Yes

(via popup, extended directory searches,

CDPATH

,

PUSHD

,

POPD

,

DIRHISTORY

,

DIRS

,

CDD

,

CD -

commands and

%@DIRSTACK[]

function)

Yes

No

Yes

No

Yes (via

INPUT

,

INKEY

,

ESET

and

SET /P

commands)

Yes (via

@SELECT[]

function, and indirectly via a combination of

INKEY

,

INPUT

,

SWITCH

commands)

No

Yes

PowerShell

Yes

Yes

Yes

Yes

Yes

(

F8

)

Yes

Yes; via PSReadLine

module (bundled in v5.0

) or in ISE

Third-party extension

Yes

Yes; via PSReadLine

module (bundled in v5.0) or in ISE

Yes

(multiple stacks; multiple location types;

Push-Location

,

Pop-Location

)

Yes, in PSReadLine

module

Yes, in ISE

Yes, in ISE

Yes

Yes

Yes

Yes, in ISE

popup window

rc

Yes

Yes

No

No

Yes

No

No

No

?

No

No

No

No

No

No

?

No

No

No

BeanShell

Yes

Yes

No

No

No

No

No

?

?

No

No

No

No

No

No

No

No

No

No

VMS DCL

Minimum uniqueness scheme

No

No

No

Yes

Yes

No

?

?

No

No

No

No

No

No

Yes

No

No

No

fish

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Yes

(built-in helper available

)

Yes

Yes

Yes

Yes

Yes

Yes, using

abbr

command

Yes

(via

fish_config

command

)

No

No

### Background execution

Background execution allows a shell to run a command without user interaction in the terminal, freeing the command line for additional work with the shell. POSIX shells and other Unix shells allow background execution by using the *&* character at the end of command.

### Completions

Completion features assist the user in typing commands at the command line, by looking for and suggesting matching words for incomplete ones. Completion is generally requested by pressing the completion key (often the Tab ↹ key).

*Command name completion* is the completion of the name of a command. In most shells, a command can be a program in the command path (usually `$PATH`), a builtin command, a function or alias.

*Path completion* is the completion of the path to a file, relative or absolute.

*Wildcard completion* is a generalization of path completion, where an expression matches any number of files, using any supported syntax for file matching.

*Variable completion* is the completion of the name of a variable name (environment variable or shell variable). Bash, zsh, and fish have completion for all variable names. PowerShell has completions for environment variable names, shell variable names and — from within user-defined functions — parameter names.

*Command argument completion* is the completion of a specific command's arguments. There are two types of arguments, named and positional: Named arguments, often called *options*, are identified by their name or letter preceding a value, whereas positional arguments consist only of the value. Some shells allow completion of argument names, but few support completing values.

Bash, zsh and fish offer parameter name completion through a definition external to the command, distributed in a separate completion definition file. For command parameter name/value completions, these shells assume path/filename completion if no completion is defined for the command. Completion can be set up to dynamically suggest completions by calling a shell function. The fish shell additionally supports parsing of man pages to extract parameter information that can be used to improve completions/suggestions. In PowerShell, all types of commands (cmdlets, functions, script files) inherently expose data about the names, types and valid value ranges/lists for each argument. This metadata is used by PowerShell to automatically support argument name and value completion for built-in commands/functions, user-defined commands/functions as well as for script files. Individual cmdlets can also define dynamic completion of argument values where the completion values are computed dynamically on the running system.

### Command history

Users of a shell may find themselves typing something similar to what they have typed before. Support for *command history* means that a user can recall a previous command into the command-line editor and edit it before issuing the potentially modified command.

Shells that support completion may also be able to directly complete the command from the command history given a partial/initial part of the previous command.

Most modern shells support command history. Shells which support command history in general also support completion from history rather than just recalling commands from the history. In addition to the plain command text, PowerShell also records execution start- and end time and execution status in the command history.

### Mandatory argument prompt

Mandatory arguments/parameters are arguments/parameters which must be assigned a value upon invocation of the command, function or script file. A shell that can determine ahead of invocation that there are missing mandatory values, can assist the interactive user by prompting for those values instead of letting the command fail. Having the shell prompt for missing values will allow the author of a script, command or function to mark a parameter as mandatory instead of creating script code to either prompt for the missing values (after determining that it is being run interactively) or fail with a message.

### Automatic suggestions

Shells featuring automatic suggestions display optional command-line completions as the user types. The PowerShell and fish shells natively support this feature; pressing the Tab ↹ key inserts the completion.

Implementations of this feature can differ between shells; for example, PowerShell and zsh use an external module to provide completions, and fish derives its completions from the user's command history.

### Directory history, stack or similar features

Shells may record a history of directories the user has been in and allow for fast switching to any recorded location. This is referred to as a "directory stack". The concept had been realized as early as 1978 in the release of the C shell (csh).

Command line interpreters 4DOS and its graphical successor Take Command Console also feature a directory stack.

### Implicit directory change

A directory name can be used directly as a command which implicitly changes the current location to the directory.

This must be distinguished from an unrelated load drive feature supported by Concurrent DOS, Multiuser DOS, System Manager and REAL/32, where the drive letter L: will be implicitly updated to point to the load path of a loaded application, thereby allowing applications to refer to files residing in their load directory under a standardized drive letter instead of under an absolute path.

### Autocorrection

When a command line does not match a command or arguments directly, spell checking can automatically correct common typing mistakes (such as case sensitivity, missing letters). There are two approaches to this; the shell can either suggest probable corrections upon command invocation, or this can happen earlier as part of a completion or autosuggestion.

The tcsh and zsh shells feature optional spell checking/correction, upon command invocation.

Fish does the autocorrection upon completion and autosuggestion. The feature is therefore not in the way when typing out the whole command and pressing enter, whereas extensive use of the tab and right-arrow keys makes the shell mostly case insensitive.

The PSReadLine PowerShell module (which is shipped with version 5.0) provides the option to specify a CommandValidationHandler ScriptBlock which runs before submitting the command. This allows for custom correcting of commonly mistyped commands, and verification before actually running the command.

### Progress indicator

A shell script (or job) can report progress of long running tasks to the interactive user.

Unix/Linux systems may offer other tools support using progress indicators from scripts or as standalone-commands, such as the program "pv". These are not integrated features of the shells, however.

### Colored directory listings

JP Software command-line processors provide user-configurable colorization of file and directory names in directory listings based on their file extension and/or attributes through an optionally defined `%COLORDIR%` environment variable.

For the Unix/Linux shells, this is a feature of the ls command and the terminal.

### Text highlighting

The command line processors in DOS Plus, Multiuser DOS, REAL/32 and in all versions of DR-DOS support a number of optional environment variables to define escape sequences allowing to control text highlighting, reversion or colorization for display or print purposes in commands like TYPE. All mentioned command line processors support `%$ON%` and `%$OFF%`. If defined, these sequences will be emitted before and after filenames. A typical sequence for `%$ON%` would be `\033[1m` in conjunction with ANSI.SYS, `\033p` for an ASCII terminal or `\016` for an IBM or ESC/P printer. Likewise, typical sequences for `%$OFF%` would be `\033[0m`, `\033q`, `\024`, respectively. The variables `%$HEADER%` and `%$FOOTER%` are only supported by COMMAND.COM in DR-DOS 7.02 and higher to define sequences emitted before and after text blocks in order to control text highlighting, pagination or other formatting options.

For the Unix/Linux shells, this is a feature of the terminal.

### Syntax highlighting

A defining feature of the fish shell is built-in syntax highlighting, As the user types, text is colored to represent whether the input is a valid command or not (the executable exists and the user has permissions to run it), and valid file paths are underlined.

An independent project offers syntax highlighting as an add-on to the Z Shell (zsh). This is not part of the shell, however.

PowerShell provides customizable syntax highlighting on the command line through the PSReadLine module. This module can be used with PowerShell v3.0+, and is bundled with v5.0 onwards. It is loaded by default in the command line host "powershell.exe" since v5.0.

Take Command Console (TCC) offers syntax highlighting in the integrated environment.

### Context sensitive help

4DOS, 4OS2, 4NT / Take Command Console and PowerShell (in PowerShell ISE) looks up context-sensitive help information when F1 is pressed.

Zsh provides various forms of configurable context-sensitive help as part of its run-help widget, _complete_help command, or in the completion of options for some commands.

The fish shell provides brief descriptions of a command's flags during tab completion.

## Programming features

Shell

Functions

Exception handling

Search & replace

on variable substi­tutions

Arithmetic

Floating point

Math function library

Linear arrays

or

lists

Assoc­iative

arrays

Lambda

functions

eval

function

Pseudo­random number generation

Bytecode

Bourne shell

1977 version

No

Yes (via

trap

)

No

No

No

No

No

No

No

Yes

No

No

Bourne shell

current version

Yes since SVR2

Yes (via

trap

)

No

Yes

No

No

No

No

No

Yes

No

No

POSIX

shell

Yes

Yes (via

trap

)

No

Yes

No

No

No

No

No

Yes

No

No

bash

(v4.0)

Yes

Yes (via

trap

)

Yes

(via

${//

} syntax)

Yes

No

No

Yes

Yes

No

Yes

Yes

(

$RANDOM

)

No

csh

No

No

Yes

(via

$var:s///

syntax)

Yes

No

No

Yes

No

No

Yes

No

No

tcsh

No

No

Yes

(via

$var:s///

syntax)

Yes

No

No

Yes

No

No

Yes

No

No

Hamilton C shell

Yes

No

Yes

(via

$var:s///

syntax)

Yes

Yes

Yes

Yes

No

No

Yes

Yes (random utility)

No

Scsh

Yes

?

Yes

(via string functions and regular expressions)

?

?

?

Yes

?

Yes

Yes

Yes

(random-integer, random-real)

Yes

(compiler is Scheme48 virtual machine, via

scshvm

)

ksh

(ksh93t+)

Yes

Yes (via

trap

)

Yes

(via

${//

} syntax and builtin commands)

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

(

$RANDOM

)

Yes

(compiler is called

shcomp

)

pdksh

Yes

Yes (via

trap

)

No

Yes

No

No

Yes

No

No

Yes

Yes

(

$RANDOM

)

No

zsh

Yes

Yes

Yes

(via

${:s//

} and

${//

} syntax)

Yes

Yes

Yes

(

zsh/mathfunc

module)

Yes

Yes

No

Yes

Yes

(

$RANDOM

)

Yes

(built-in

zcompile

command)

ash

Yes

Yes (via

trap

)

No

Yes

(since 1992)

No

No

No

No

No

Yes

No

No

CCP

No

?

No

No

?

?

No

No

No

No

No

No

COMMAND.COM

No

Partial (only Auto-fail (via

COMMAND /F

(or

/N

in some versions of DR-DOS))

No

No

No

No

No

No

No

No

No

No

OS/2

CMD.EXE

No

No

No

?

No

No

?

No

No

No

No

No

Windows

CMD.EXE

Yes

(via

CALL :label

)

No

Yes

(via

SET %

varname

:

expression

syntax)

Yes

(via

SET /A

)

No

No

Yes

(via

SET

)

No

No

No

Yes

(

%random%

)

No

4DOS

Yes

Yes

(via

ON

command, optional Auto-fail via

4DOS /F

)

Yes

(via

%@Replace[...]

function)

Yes

(via

SET /A

)

?

?

Yes

(via ranges, include lists,

@

file lists and

FOR

command)

No

No

Yes

Yes

(

%@Random[...]

function)

Yes

(via

BATCOMP

command)

4OS2

?

?

?

?

?

?

?

?

No

Yes

Yes (

%@Random[...]

function)

?

TCC

(formerly 4NT)

Yes

Yes

(via

ON

and various

...MONITOR

commands)

Yes

(via

%@Replace[...]

function)

Yes

(via

SET /A

)

?

?

Yes

(via ranges, include lists,

@

file lists and

FOR

command)

?

No

Yes

Yes (

%@Random[...]

function)

Yes (via

BATCOMP

command)

PowerShell

Yes

Yes (Try-Catch-Finally)

Yes

(

-replace

operator)

Yes

Yes

[Math] class

Yes

Yes

Yes

Yes

Yes

Yes, automatic

rc

Yes

Yes

No

Yes

?

?

Yes

?

No

Yes

No

No

BeanShell

Yes

Yes

?

Yes

?

?

Yes

Yes

No

Yes

Yes

Yes

VMS DCL

Yes

Yes

No

Yes

No

yes, for compiled programs

Yes

No

No

No

No

No

fish

Yes

Yes (via

trap

)

Yes, via

string

builtin command

Yes

Yes

Yes

Yes

No

No

Yes

Yes

(

random

)

No

## String processing and filename matching

| Shell | String processing | Alternation (Brace expansion) | Pattern matching (regular expressions built-in) | Pattern matching (filename globbing) | Globbing qualifiers (filename generation based on file attributes) | Recursive globbing (generating files from any level of subdirectories) |
|---|---|---|---|---|---|---|
| Bourne shell 1977 version | ? | No | No | Yes (*, ?, [...]) | No | No |
| Bourne shell recent version | Partial (prefix and suffix stripping in variable expansion) | No | No | Yes (*, ?, [...]) | No | No |
| POSIX shell | Partial (prefix and suffix stripping in variable expansion) | No | No | Yes (*, ?, [...]) | No | No |
| bash (v4.0) | Partial (prefix and suffix stripping in variable expansion) | Yes | Yes | Yes (*, ?, [...], {...}) | No | Yes (**/...) |
| csh | Yes (:s and other editing operators) | Yes | No | Yes | No | No |
| tcsh | Yes (:s and other editing operators) | Yes | Yes | Yes | No | No |
| Hamilton C shell | Yes (:s and other editing operators + substr, strlen, strindex, printf, reverse, upper, lower, concat and other builtin functions) | Yes | No | Yes | No | Yes (via indefinite directory "..." wildcard) |
| Scsh | ? | ? | Yes | Yes | No | No |
| ksh (ksh93t+) | Partial (prefix, suffix stripping and string replacement in variable expansion) | Yes | Yes | Yes (*, ?, [...]) | No | Yes (with set -G, no following of symlinks) |
| pdksh | ? | Yes | No | Yes | No | No |
| zsh | Yes (through variable processing: e.g. substring extraction, various transformations via parameter expansion) | Yes | Yes | Yes (*, ?, [...], extended globbing) | Yes | Yes (**/... or ***/... to follow symlinks) |
| ash | ? | ? | No | Yes | No | No |
| CCP | No | No | No | No | No | No |
| COMMAND.COM | No | No | No | Yes (*, ?) | No | No |
| OS/2 CMD.EXE | No | No | No | Yes (*, ?) | Partial (only in DIR /A:... command) | No |
| Windows CMD.EXE | Partial (only through FOR /F and SET /A) | No | No | Yes (*, ?) | Partial (only in DIR /A:... command) | Yes (via FOR /R command, or, where available, indirectly via /S subdir option) |
| 4DOS | Yes (through variable functions %@...[], extended environment variable processing, various string commands and FOR /F and SET /A) | No | No | Yes (*, ?, [...], extended wildcards, SELECT popup command) | Yes (via /A:... attribute and /I"..." description options and /[S...] size, /[T...] time, /[D...] date, and /[!...] file exclusion ranges) | Yes (via FOR /R command, or indirectly via GLOBAL command or, where available, /S subdir option) |
| 4OS2 | ? | No | No | ? | ? | ? |
| TCC (formerly 4NT) | Yes (through variable functions %@...[], extended environment variable processing, various string commands and FOR /F and SET /A) | No | Yes | Yes (*, ?, [...], extended wildcards, SELECT popup command) | Yes (via /A:... attribute and /I"..." description options and /[S...] size, /[T...] time, /[D...] date, /[O...] owner, and /[!...] file exclusion ranges) | Yes (via FOR /R command, or indirectly via GLOBAL command or, where available, /S subdir option) |
| PowerShell | Yes (Concat/Substring/Insert/Remove/Replace, ToLower/ToUpper, Trim/TrimStart/TrimEnd, Compare, Contains/StartsWith/EndWith, Format, IndexOf/LastIndexOf, Pad/PadLeft/PadRight, Split/Join, regular expression functions and other .NET string functions) | Range operator for numbers | Yes (full regex support) | Yes (*, ?, [...]) | ? | ? |
| rc | ? | ? | Yes (~ operator) | Yes | No | No |
| BeanShell | ? | ? | Yes | ? | ? | ? |
| VMS DCL | Yes | No | No | Yes | No | Yes (via [SUBDIR...]) |
| fish | Yes (builtin string function) | Yes | Yes (via builtin string match and string replace functions) | Yes (*, ?, {...}) | No | Yes (**/...) |

## Inter-process communication

| Shell | Pipes | Command substitution | Process substitution | Subshells | TCP/UDP connections as streams | Keystroke stacking |
|---|---|---|---|---|---|---|
| Bourne shell | bytes concurrent | Yes | No | Yes | No | N/A |
| POSIX shell | bytes concurrent | Yes | No | Yes | No | N/A |
| bash (v4.0) | bytes concurrent | Yes | Yes (if system supports /dev/fd/*⟨n⟩* or named pipes) | Yes | Yes (client only) | N/A |
| csh | bytes concurrent | Yes | No | Yes | No | N/A |
| tcsh | bytes concurrent | Yes | No | Yes | No | N/A |
| Hamilton C shell | bytes concurrent | Yes | No | Yes | No | ? |
| Scsh | text | ? | ? | ? | Yes | N/A |
| ksh (ksh93t+) | bytes (may contain serialized objects if print -C is used) concurrent | Yes ($(...) and ${<space>...;}) | Yes (if system supports /dev/fd/*⟨n⟩*) | Yes | Yes (and SCTP support, client only) | N/A |
| pdksh | bytes concurrent | Yes | No | Yes | No | N/A |
| zsh | bytes concurrent | Yes | Yes | Yes | Yes (client and server, but only TCP) | N/A |
| ash | bytes concurrent | Yes | No | Yes | No | N/A |
| CCP | No | No | No | No | No | No |
| COMMAND.COM | text sequential temporary files | No | No | Partial (only under DR-DOS multitasker via COMMAND.COM /T) | No | No |
| OS/2 CMD.EXE | text concurrent | No | No | ? | No | No |
| Windows CMD.EXE | text concurrent | Yes (via FOR /F command) | No | Yes (Backtick: ` in FOR /F usebackq) | No | No |
| 4DOS | text sequential temporary files | Yes (via FOR /F command) | ? | Partial (via %@EXECSTR[] and %@EXEC[], or via SET /M, ESET /M and UNSET /M and %@MASTER[...]) | No | Yes (via KEYSTACK and KSTACK) |
| 4OS2 | text concurrent | ? | ? | ? | No | Yes (via KEYSTACK) |
| TCC (formerly 4NT) | text concurrent | Yes (via FOR /F command) | ? | Partial (via %@EXECSTR[] and %@EXEC[]) | Yes (via FTP, TFTP, FTPS, SFTP, HTTP, HTTPS and IFTP, client only) | Yes (via KEYSTACK) |
| PowerShell | objects concurrent | Yes | No | Yes | Yes | ? |
| rc | text concurrent | Yes | Yes (via: <{cmd} if system supports /dev/fd/*⟨n⟩*) | Yes | No | ? |
| BeanShell | not supported | ? | ? | ? | Yes | ? |
| VMS DCL | text (via PIPE command) | Yes | No | Yes (spawn) | Yes (server TCP only) | No |
| fish | bytes concurrent | Yes (...) | No (broken) | No | No | N/A |

### Keystroke stacking

In anticipation of what a given running application may accept as keyboard input, the user of the shell instructs the shell to generate a sequence of *simulated* keystrokes, which the application will interpret as a keyboard input from an interactive user. By sending keystroke sequences the user may be able to direct the application to perform actions that would be impossible to achieve through input redirection or would otherwise require an interactive user. For example, if an application acts on keystrokes, which cannot be redirected, distinguishes between normal and extended keys, flushes the queue before accepting new input on startup or under certain conditions, or because it does not read through standard input at all. Keystroke stacking typically also provides means to control the timing of simulated keys being sent or to delay new keys until the queue was flushed etc. It also allows to simulate keys which are not present on a keyboard (because the corresponding keys do not physically exist or because a different keyboard layout is being used) and therefore would be impossible to type by a user.

## Security features

| Shell | Secure (password) prompt | File/directory passwords | Execute permission | Restricted shell subset | Safe data subset |
|---|---|---|---|---|---|
| Bourne shell | via stty | ? | N/A | Yes | No |
| POSIX shell | via stty | ? | N/A | No | No |
| bash (v4.0) | `read -s` | ? | N/A | Yes | No |
| csh | via stty | ? | N/A | Yes | No |
| tcsh | via stty | ? | N/A | Yes | No |
| Hamilton C shell | No | No | No | No | No |
| Scsh | via stty | ? | N/A | No | No |
| ksh (ksh93t+) | via stty | ? | N/A | Yes | No |
| pdksh | via stty | ? | N/A | Yes | No |
| zsh | `read -s` | ? | N/A | Yes | No |
| ash | via stty | ? | N/A | No | No |
| CCP | No | No | No | No | No |
| COMMAND.COM | Partial (only under DR-DOS, prompts for password if file/directory is protected) | Partial (only under DR-DOS via `\dirname;dirpwd\filename;filepwd` syntax) | Partial (only under DR-DOS, if files are password-protected for read and/or execute permission) | No | No |
| OS/2 CMD.EXE | No | No | No | No | No |
| Windows CMD.EXE | No | No | No | No | No |
| 4DOS | Yes (via `INPUT /P` or `INKEY /P`) | Partial (only under DR-DOS via `\dirname;;dirpwd\filename;;filepwd` syntax) | Partial (only under DR-DOS, if files are password-protected for read and/or execute permission) | No | No |
| 4OS2 | ? | No | No | No | No |
| TCC (formerly 4NT) | Yes (via `INPUT /P`, `INKEY /P` or `QUERYBOX /P`) | No | No | No | No |
| PowerShell | Yes | No | No | Yes | Yes |
| rc | via stty | ? | N/A | No | No |
| BeanShell | ? | ? | ? | ? | ? |
| VMS DCL | Yes | No | Yes | Yes | No |
| fish | `read -s` | ? | N/A | No | ? |

### Secure prompt

Some shell scripts need to query the user for sensitive information such as passwords, private digital keys, PIN codes or other confidential information. Sensitive input should not be echoed back to the screen/input device where it could be gleaned by unauthorized persons. Plaintext memory representation of sensitive information should also be avoided as it could allow the information to be compromised, e.g., through swap files, core dumps etc.

The shells bash, zsh and PowerShell offer this as a specific feature. Shells which do not offer this as a specific feature may still be able to turn off echoing through some other means. Shells executing on a Unix/Linux operating system can use the stty external command to switch off/on echoing of input characters. In addition to not echoing back the characters, PowerShell's `-AsSecureString` option also encrypts the input character-by-character during the input process, ensuring that the string is never represented unencrypted in memory where it could be compromised through memory dumps, scanning, transcription etc.

### Execute permission

Some operating systems define an *execute* permission which can be granted to users/groups for a file when the file system itself supports it.

On Unix systems, the execute permission controls access to invoking the file as a program, and applies both to executables and scripts. As the permission is enforced in the program loader, no obligation is needed from the invoking program, nor the invoked program, in enforcing the execute permission – this also goes for shells and other interpreter programs. The behaviour is mandated by the POSIX C library that is used for interfacing with the kernel. POSIX specifies that the `exec` family of functions shall fail with EACCESS (permission denied) if the file denies execution permission (see `execve` – System Interfaces Reference, The Single UNIX Specification, Version 5 from The Open Group).

The *execute* permission only applies when the script is run directly. If a script is invoked as an argument to the interpreting shell, it will be executed regardless of whether the user holds the *execute* permission for that script.

Although Windows also specifies an *execute* permission, none of the Windows-specific shells block script execution if the permission has not been granted.

### Restricted shell subset

Several shells can be started or be configured to start in a mode where only a limited set of commands and actions is available to the user. While not a security *boundary* (the command accessing a resource is blocked rather than the resource) this is nevertheless typically used to restrict users' actions before logging in.

A restricted mode was evaluated for the POSIX specification for shells, but not included. However, most of the Linux/Unix shells support such a mode where several of the built-in commands are disabled and only external commands from a certain directory can be invoked.

PowerShell supports restricted modes through *session configuration files* or session configurations. A session configuration file can define visible (available) cmdlets, aliases, functions, path providers and more.

### Safe data subset

Scripts that invoke other scripts can be a security risk as they can potentially execute foreign code in the context of the user who launched the initial script. Scripts will usually be designed to exclusively include scripts from known safe locations; but in some instances, e.g. when offering the user a way to configure the environment or loading localized messages, the script may need to include other scripts/files. One way to address this risk is for the shell to offer a safe subset of commands which can be executed by an included script.

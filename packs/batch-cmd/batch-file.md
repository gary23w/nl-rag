---
title: "Batch file"
source: https://en.wikipedia.org/wiki/Batch_file
domain: batch-cmd
license: CC-BY-SA-4.0
tags: batch file, windows batch, cmd.exe, bat script
fetched: 2026-07-02
---

# Batch file

A **batch file** is a script file in DOS, OS/2 and Microsoft Windows. It consists of a series of commands to be executed by the command-line interpreter, stored in a plain text file. A batch file may contain any command the interpreter accepts interactively and use constructs that enable conditional branching and looping within the batch file, such as `IF`, `FOR`, and `GOTO` labels. The term "batch" is from batch processing, meaning "non-interactive execution", though a batch file might not process a *batch* of multiple data.

Similar to Job Control Language (JCL), DCL and other systems on mainframe and minicomputer systems, batch files were added to ease the work required for certain regular tasks by allowing the user to set up a script to automate them. When a batch file is run, the shell program (usually COMMAND.COM or cmd.exe) reads the file and executes its commands, normally line-by-line. Unix-like operating systems, such as Linux, have a similar, but more flexible, type of file called a shell script.

The filename extension **.bat** is used in DOS and Windows. Windows NT and OS/2 also added **.cmd**. Batch files for other environments may have different extensions, e.g., **.btm** in 4DOS, 4OS2 and 4NT related shells.

The detailed handling of batch files has changed significantly between versions. Some of the detail in this article applies to all batch files, while other details apply only to certain versions.

## Variants

### DOS

In MS-DOS, a batch file can be started from the command-line interface by typing its name, followed by any required parameters and pressing the ↵ Enter key. When DOS loads, the file AUTOEXEC.BAT, when present, is automatically executed, so any commands that need to be run to set up the DOS environment may be placed in this file. Computer users would have the AUTOEXEC.BAT file set up the system date and time, initialize the DOS environment, load any resident programs or device drivers, or initialize network connections and assignments.

A .bat file name extension identifies a file containing commands that are executed by the command interpreter COMMAND.COM line by line, as if it were a list of commands entered manually, with some extra batch-file-specific commands for basic programming functionality, including a `GOTO` command for changing flow of line execution.

### Early Windows

Microsoft Windows was introduced in 1985 as a graphical user interface-based (GUI) overlay on text-based operating systems and was designed to run on DOS. In order to start it, the `WIN` command was used, which could be added to the end of the AUTOEXEC.BAT file to allow automatic loading of Windows. In the earlier versions, one could run a .bat type file from Windows in the MS-DOS Prompt. Windows 3.1x and earlier, as well as Windows 9x invoked COMMAND.COM to run batch files.

### OS/2

The IBM OS/2 operating system supported DOS-style batch files. It also included a version of REXX, a more advanced batch-file scripting language. IBM and Microsoft started developing this system, but during the construction of it broke up after a dispute; as a result of this, IBM referred to their DOS-like console shell without mention of Microsoft, naming it just DOS, although this seemingly made no difference with regard to the way batch files worked from COMMAND.COM.

OS/2's batch file interpreter also supports an EXTPROC command. This passes the batch file to the program named on the EXTPROC file as a data file. The named program can be a script file; this is similar to the #! mechanism used by Unix-like operating systems.

### Windows NT

Unlike Windows 98 and earlier, the Windows NT family of operating systems does not depend on MS-DOS. Windows NT introduced an enhanced 32-bit command interpreter (cmd.exe) that could execute scripts with either the .CMD or .BAT extension. Cmd.exe added additional commands, and implemented existing ones in a slightly different way, so that the same batch file (with different extension) might work differently with cmd.exe and COMMAND.COM. In most cases, operation is identical if the few unsupported commands are not used. Cmd.exe's extensions to COMMAND.COM can be disabled for compatibility.

Microsoft released a version of cmd.exe for Windows 9x and ME called WIN95CMD to allow users of older versions of Windows to use certain cmd.exe-style batch files.

As of Windows 8, cmd.exe is the normal command interpreter for batch files; the older COMMAND.COM can be run as well in 32-bit versions of Windows able to run 16-bit programs.

## Filename extensions

**.bat**

The first filename extension used by

Microsoft

for batch files. This extension runs with DOS and all versions of Windows, under COMMAND.COM or cmd.exe, despite the different ways the two command interpreters execute batch files.

**.cmd**

Used for batch files in

Windows NT

family and sent to cmd.exe for interpretation. COMMAND.COM does not recognize this file name extension, so cmd.exe scripts are not executed in the wrong Windows environment by mistake. In addition,

append

,

dpath

,

ftype

,

set

,

path

,

assoc

and

prompt

commands, when executed from a .bat file, alter the value of the

errorlevel

variable only upon an error, whereas from within a .cmd file, they would affect errorlevel even when returning without an error.

It is also used by IBM's OS/2 for batch files.

**.btm**

The extension used by

4DOS

,

4OS2

,

4NT

and

Take Command

. These scripts are faster, especially with longer ones, as the script is loaded entirely ready for execution, rather than line-by-line.

COMMAND.COM and cmd.exe can run a batch file even if its filename is typed without an extension. For instance, if `DoThis` is entered, the interpreter tries the following extensions in the order given: `COM`, `.EXE`, `.BAT`, `.CMD`, and seven other extension unrelated to this topic. The PATHEXT environment variable can change the aforesaid default.

## Batch file parameters

COMMAND.COM and cmd.exe support special variables (`%0`, `%1` through `%9`) in order to refer to the path and name of the batch job and the first nine calling parameters from within the batch job, see also SHIFT. Non-existent parameters are replaced by a zero-length string. They can be used similar to environment variables, but are not stored in the environment. Microsoft and IBM refer to these variables as *replacement parameters* or *replaceable parameters*, whereas Digital Research, Novell and Caldera established the term *replacement variables* for them. JP Software calls them *batch file parameters*.

## Examples

This example batch file displays `Hello World!`, prompts and waits for the user to press a key, and then terminates. (Commands may be lowercase or uppercase, but variable names are case-sensitive)

```mw
@ECHO OFF
ECHO Hello World!
PAUSE
```

To execute the file, it must be saved with the filename extension suffix .bat (or .cmd for Windows NT-type operating systems) in plain text format, typically created by using a text editor such as Microsoft Notepad or a word processor working in plain text mode.

When executed, the following is displayed:

```
Hello World!
Press any key to continue . . .
```

### Explanation

The interpreter executes each line in turn, starting with the first. The `@` symbol at the start of any line prevents the prompt from displaying that command as it is executed. The command `ECHO OFF` turns off the prompt permanently, or until it is turned on again. The combined `@ECHO OFF` is often as here the first line of a batch file, preventing any commands from displaying, itself included. Then the next line is executed and the `ECHO Hello World!` command outputs `Hello World!`. The next line is executed and the `PAUSE` command displays `Press any key to continue . . .` and pauses the script's execution. After a key is pressed, the script terminates, as there are no more commands. In Windows, if the script is executed from an already running command prompt window, the window remains open at the prompt as in MS-DOS; otherwise, the window closes on termination.

## Limitations and exceptions

### Null values in variables

Variable expansions are substituted textually into the command, and thus variables which contain nothing simply disappear from the syntax, and variables which contain spaces turn into multiple tokens. This can lead to syntax errors or bugs.

For example, if %foo% is empty, this statement:

```mw
IF %foo%==bar ECHO Equal
```

parses as the erroneous construct:

```mw
IF ==bar ECHO Equal
```

Similarly, if `%foo%` contains `abc def`, then a different syntax error results:

```mw
IF abc def==bar ECHO Equal
```

The usual way to prevent this problem is to surround variable expansions in quotes so that an empty variable expands into the valid expression `IF ""=="bar"` instead of the invalid `IF ==bar`. The text that is being compared to the variable must also be enclosed in quotes, because the quotes are not special delimiting syntax; these characters represent themselves.

```mw
IF "%foo%"=="bar" ECHO Equal
```

The delayed !VARIABLE! expansion available in Windows 2000 and later may be used to avoid these syntactical errors. In this case, null or multi-word variables do not fail syntactically because the value is expanded after the IF command is parsed:

```mw
IF !foo!==bar ECHO Equal
```

Another difference in Windows 2000 or higher is that an empty variable (undefined) is not substituted. As described in previous examples, previous batch interpreter behaviour would have resulted in an empty string. Example:

```mw
C:\>set MyVar=
C:\>echo %MyVar%
%MyVar%

C:\>if "%MyVar%"=="" (echo MyVar is not defined) else (echo MyVar is %MyVar%)
MyVar is %MyVar%
```

Batch interpreters prior to Windows 2000 would have displayed result `MyVar is not defined`.

### Quotation marks and spaces in passed strings

Unlike Unix/POSIX processes, which receive their command-line arguments already split up by the shell into an array of strings, a Windows process receives the entire command-line as a single string, via the GetCommandLine API function. As a result, each Windows application can implement its own parser to split the entire command line into arguments. Many applications and command-line tools have evolved their own syntax for doing that, and so there is no single convention for quoting or escaping metacharacters on Windows command lines.

- For some commands, spaces are treated as delimiters that separate arguments, unless those spaces are enclosed by quotation marks. Various conventions exist of how quotation marks can be passed on to the application:
  - A widely used convention is implemented by the command-line parser built into the Microsoft Visual C++ runtime library] or in the CommandLineToArgvW function. It uses the convention that 2*n* backslashes followed by a quotation mark (") produce *n* backslashes followed by a begin/end quote, whereas (2*n*)+1 backslashes followed by a quotation mark again produce n backslashes followed by a quotation mark literal. The same convention is part of the .NET Framework specification.
    - An undocumented aspect is that "" occurring in the middle of a quoted string produces a single quotation mark. (A CRT change in 2008 [msvcr90] modified this undocumented handling of quotes.) This is helpful for inserting a quotation mark in an argument without re-enabling interpretation of cmd metacharacters like |, & and >. (cmd does not recognize the usual \" as escaping the quote. It re-enables these special meanings on seeing the quote, thinking the quotation has ended.)
  - Another convention is that a single quotation mark (") is not included as part of the string. However, an escaped quotation mark (""") can be part of the string.
  - Yet another common convention comes from the use of Cygwin-derived ported programs. It does not differentiate between backslashes occurring before or not before quotes. See glob (programming) § Windows and DOS for information on these alternative command-line parsers.
  - Some important Windows commands, like `cmd.exe` and `wscript.exe`, use their own rules.
- For other commands, spaces are not treated as delimiters and therefore do not need quotation marks. If quotes are included they become part of the string. This applies to some built-in commands like echo.

Where a string contains quotation marks, and is to be inserted into another line of text that must also be enclosed in quotation marks, particular attention to the quoting mechanism is required:

```mw
C:\>set foo="this string is enclosed in quotation marks"

C:\>echo "test 1 %foo%"
"test 1 "this string is enclosed in quotation marks""

C:\>eventcreate /T Warning /ID 1 /L System /SO "Source" /D "Example: %foo%"
ERROR: Invalid Argument/Option - 'string'.
Type "EVENTCREATE /?" for usage.
```

On Windows 2000 and later, the solution is to replace each occurrence of a quote character within a value by a series of three quote characters:

```mw
C:\>set foo="this string is enclosed in quotes"

C:\>set foo=%foo:"="""%

C:\>echo "test 1 %foo%"
"test 1 """this string is enclosed in quotes""""

C:\>eventcreate /T Warning /ID 1 /L System /SO "Source" /D "Example: %foo%"
SUCCESS: A 'Warning' type event is created in the 'Source' log/source.
```

### Escaped characters in strings

Some characters, such as pipe (`|`) characters, have special meaning to the command line. They cannot be printed as text using the ECHO command unless escaped using the caret ^ symbol:

```mw
C:\>echo foo | bar
'bar' is not recognized as an internal or external command,
operable program or batch file.

C:\>echo foo ^| bar
foo | bar
```

However, escaping does not work as expected when inserting the escaped character into an environment variable. The variable ends up containing a live pipe command when merely echoed. It is necessary to escape both the caret itself and the escaped character for the character display as text in the variable:

```mw
C:\>set foo=bar | baz
'baz' is not recognized as an internal or external command,
operable program or batch file.

C:\>set foo=bar ^| baz
C:\>echo %foo%
'baz' is not recognized as an internal or external command,
operable program or batch file.

C:\>set foo=bar ^^^| baz
C:\>echo %foo%
bar | baz
```

The delayed expansion available with or with in Windows 2000 and later may be used to show special characters stored in environment variables because the variable value is expanded after the command was parsed:

```mw
C:\>cmd /V:ON
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation. All rights reserved.

C:\>set foo=bar ^| baz
C:\>echo !foo!
bar | baz
```

### Sleep or scripted delay

Until the TIMEOUT command was introduced with Windows Vista, there was no easy way to implement a timed pause, as the PAUSE command halts script activity indefinitely until any key is pressed.

Many workarounds were possible, but generally only worked in some environments: The `CHOICE` command was not available in older DOS versions, `PING` was only available if TCP/IP was installed, and so on. No solution was available from Microsoft, but a number of small utility programs, could be installed from other sources. A commercial example would be the 1988 Norton Utilities Batch Enhancer (BE) command, where `BE DELAY 18` would wait for 1 second, or the free 94-byte WAIT.COM where `WAIT 5` would wait for 5 seconds, then return control to the script. Most such programs are 16-bit .COM files, so are incompatible with 64-bit Windows.

### Text output with stripped CR/LF

Normally, all printed text automatically has the control characters for carriage return (CR) and line feed (LF) appended to the end of each line.

- batchtest.bat @echo foo @echo bar C:\>batchtest.bat foo bar

It does not matter if the two echo commands share the same command line; the CR/LF codes are inserted to break the output onto separate lines:

```mw
C:\>@echo Message 1&@echo Message 2
Message 1
Message 2
```

A trick discovered with Windows 2000 and later is to use the special prompt for input to output text without CR/LF trailing the text. In this example, the CR/LF does not follow Message 1, but does follow Line 2 and Line 3:

- batchtest2.bat @echo off set /p ="Message 1"<nul echo Message 2 echo Message 3 C:\>batchtest2.bat Message 1Message 2 Message 3

This can be used to output data to a text file without CR/LF appended to the end:

```mw
C:\>set /p ="Message 1"<nul >data.txt
C:\>set /p ="Message 2"<nul >>data.txt
C:\>set /p ="Message 3"<nul >>data.txt
C:\>type data.txt
Message 1Message 2Message 3
```

However, there is no way to inject this stripped CR/LF prompt output directly into an environment variable.

### Setting a Uniform Naming Convention (UNC) working directory from a shortcut

It is not possible to have a command prompt that uses a UNC path as the current working directory; e.g. `\\server\share\directory\`

The command prompt requires the use of drive letters to assign a working directory, which makes running complex batch files stored on a server UNC share more difficult. While a batch file can be run from a UNC file path, the working directory default is `C:\Windows\System32\`.

In Windows 2000 and later, a workaround is to use the **`PUSHD`** and **`POPD`** command with command extensions.

If not enabled by default, command extensions can be temporarily enabled using the `/E:ON` switch for the command interpreter.

So to run a batch file on a UNC share, assign a temporary drive letter to the UNC share, and use the UNC share as the working directory of the batch file, a Windows shortcut can be constructed that looks like this:

- Target:

The working directory attribute of this shortcut is ignored.

This also solves a problem related to User Account Control (UAC) on Windows Vista and newer. When an administrator is logged on and UAC is enabled, and they try to run a batch file as administrator from a network drive letter, using the right-click file context menu, the operation will unexpectedly fail. This is because the elevated UAC privileged account context does not have network drive letter assignments, and it is not possible to assign drive letters for the elevated context via the Explorer shell or logon scripts. However, by creating a shortcut to the batch file using the above `PUSHD` / `POPD` construct, and using the shortcut to run the batch file as administrator, the temporary drive letter will be created and removed in the elevated account context, and the batch file will function correctly.

The following syntax does correctly expand to the path of the current batch script.

```
%~dp0
```

UNC default paths are turned off by default as they used to crash older programs.

The Dword registry value `DisableUNCCheck` at `HKEY_CURRENT_USER\Software\Microsoft\Command Processor` allows the default directory to be UNC. `CD` command will refuse to change but placing a UNC path in Default Directory in a shortcut to Cmd or by using the Start command. (`C$` share is for administrators).

### Character set

Batch files use an OEM character set, as defined by the computer, e.g. Code page 437. The non-ASCII parts of these are incompatible with the Unicode or Windows character sets otherwise used in Windows so care needs to be taken. Non-English file names work only if entered through a DOS character set compatible editor. File names with characters outside this set do not work in batch files.

To get a command prompt with Unicode instead of Code page 437 or similar, one can use the `cmd /U` command. In such a command prompt, a batch file with Unicode filenames will work. Also one can use `cmd /U` to directly execute commands with Unicode as character set. For example, `cmd /U /C dir > files.txt` creates a file containing a directory listing with correct Windows characters, in the UTF-16LE encoding.

## Batch viruses and malware

As with any other programming language, batch files can be used maliciously. Simple trojans and fork bombs are easily created, and batch files can do a form of DNS poisoning by modifying the hosts file. Batch viruses are possible, and can also spread themselves via USB flash drives by using Windows' Autorun capability.

The following command in a batch file will delete all the data in the current directory (folder) - without first asking for confirmation:

```mw
del /Q *.*
```

These three commands are a simple fork bomb that will continually replicate itself to deplete available system resources, slowing down or crashing the system:

```mw
:TOP
 start "" %0
 goto TOP
```

## Other Windows scripting languages

The cmd.exe command processor that interprets both `.bat` and `.cmd` files is supported in all versions of the Windows NT family, Windows CE, and ReactOS. The older COMMAND.COM, which only interprets `.bat` files, is available in Windows 9x and 32-bit editions of Windows NT; hence, it is not available in Windows 11, which is strictly 64-bit.

Microsoft Windows, however, comes with more advanced scripting environments:

- Windows Script Host (deprecated) — released in 1998 with Windows 98, it consists of `cscript.exe` and `wscript.exe`, runs scripts written in VBScript or JScript (bearing **.vbs**, **.js** and **.wsf** extensions). It can run them in windowed mode (with the `wscript.exe` host) or in console-based mode (with the `cscript.exe` host). It has been deprecated in Windows 11.
- MSHTA (deprecated) — introduced to Microsoft Windows in 1999, along with the release of Microsoft Internet Explorer 5, `mshta.exe` is means of creating graphically rich scripts whose source code is made of HTML, CSS and JScript.
- PowerShell — a free, open-source, cross-platform, object-oriented shell that can harness the .NET APIs. PowerShell was originally released in 2006 as a closed-source add-on for Windows XP and Windows Vista. It has since been bundled with all subsequent versions of Windows. 10 years later, PowerShell went open-source and cross-platform. It can operate both interactively (from a command-line interface) and also via saved scripts (**.ps1** files). The scripting syntax can further expand PowerShell via script modules (**.psm** files) and binary modules (**.dll** files). PowerShell's commands use a "Verb-Noun" format to facilitate quick discovery.

There are other scripting languages available for Windows. However, these require the scripting language interpreter to be installed before they can be used:

- Extended Batch Language (EBL) (**.bat**) — developed by Frank Canova as an 'own-time' project while working at IBM in 1982. It was subsequently sold by Seaware Corp as an interpreter and compiler primarily for DOS, but later for Windows.
- KiXtart (**.kix**) — developed by a Microsoft employee in 1991, specifically to meet the need for commands useful in a network logon script while retaining the simple 'feel' of a .cmd file.
- Unix-style shell scripting languages can be used if a Unix compatibility tool such as Cygwin is installed, or Windows Subsystem for Linux (WSL) is used.
- Cross-platform scripting tools including Perl, Python, Ruby, Rexx, Node.js and PHP are available for Windows.

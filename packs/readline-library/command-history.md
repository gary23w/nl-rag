---
title: "Command history"
source: https://en.wikipedia.org/wiki/Command_history
domain: readline-library
license: CC-BY-SA-4.0
tags: gnu readline, readline line editing, command-line editing library, interactive line editor
fetched: 2026-07-02
---

# Command history

**Command history** is a feature in many operating system shells, computer algebra programs, and other software that allows the user to recall, edit and rerun previous commands.

Command line history was added to Unix in Bill Joy's C shell of 1978; Joy took inspiration from an earlier implementation in Interlisp. It quickly became popular because it made the C shell fast and easy to use. History has since become a standard feature in other shells, including ksh, Bash and Microsoft's cmd.exe. History addressed two important scenarios:

1. Executing the same command or a short sequence of commands over and over. An example might be a developer frequently compiling and running a program.
2. Correcting mistakes or rerunning a command with only a small modification.

In Joy's original C shell, the user could refer to a previous command by typing an exclamation, `!`, followed by additional characters to specify a particular command, only certain words, or to edit it in some way before pasting it back into the command line. For example:

!!

meant the entire previous command.

!$

meant just the last word of the previous command.

!

abc

meant the command that started with

abc

.

The usual implementation today is to combine history with command-line editing. The cursor keys are used to navigate up and down through the history list and left or right to anyplace on the line, where the user can simply type a desired change. But some implementations are menu-based: The user presses a certain function key which displays a menu of recent commands, which the user can select one by typing a number.

Some implementation such as Bash support recording command history to a file (`history` command).

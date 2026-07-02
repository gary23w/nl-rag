---
title: "AutoHotkey"
source: https://en.wikipedia.org/wiki/AutoHotkey
domain: autohotkey
license: CC-BY-SA-4.0
tags: autohotkey, auto hotkey, ahk script, hotkey macro
fetched: 2026-07-02
---

# AutoHotkey

**AutoHotkey** (**AHK**) is a free and open-source custom scripting language for Microsoft Windows, primarily designed to provide easy keyboard shortcuts (or 'hotkeys'), fast macro-creation, and software automation, to allow users of most computer skill levels to automate repetitive tasks in any Windows application. It can easily extend or modify user interfaces (for example, overriding the default Windows control key commands with their Emacs equivalents).

AutoHotkey was initially released by its creator, Chris Mallet, in 2003; it has subsequently become one of the most commonly used and commonly recommended pieces of software available for simple macro implementation. The installation package includes an extensive help file; web-based documentation is also available.

## Features and uses

AutoHotkey scripts can be used to launch programs, open documents, and emulate keystrokes or mouse clicks and movements. They can also assign, retrieve, and manipulate variables, run loops, and manipulate windows, files, and folders. They can be triggered by a hotkey, such as a script that opens an internet browser when the user presses the relevant hotkey (key combination) Ctrl+Alt+I on the keyboard.

AutoHotkey also allows "hotstrings" that automatically replace certain text as it is typed, such as assigning the string "btw" to produce the text "by the way", or the text "%o" to produce "percentage of". Keyboard keys can also be remapped and disabled—for example, so that pressing Ctrl+M produces an em dash in the active window. Scripts can also be set to run automatically at computer startup, with no keyboard action required—for example, for performing file management at a set interval.

More complex tasks can be achieved with custom data entry forms (GUI windows), working with the system registry, or using the Windows API by calling functions from DLLs. The scripts can be compiled into standalone executable files that can be run on other computers without AutoHotkey installed. The C++ source code can be compiled with Visual Studio Express.

AutoHotkey allows memory access through pointers, as in C.

### Some sample uses for AutoHotkey

- Remapping the keyboard, such as from QWERTY to Dvorak and other alternative keyboard layouts
- Opening programs, documents, and websites with simple keystrokes
- Using shortcuts to type frequently-used filenames and other phrases
- Typing punctuation not available on the keyboard, such as a curved quotemark (**“**…**”**)
- Typing other non-keyboard characters, such as the sign × used for dimensional measurement (e.g. 10′×12′)
- Simulating mouse cursor input via a script or keystrokes
- Pasting blocks of predefined text on command (e.g. to add signatures to e-mails, message boards posts, etc.)
- Monitoring a system and automatically closing unwanted programs
- Scheduling an automatic reminder, system scan, or backup
- Filling out forms automatically
- Prototyping applications before implementing them in other, more time-consuming programming languages

## History

The first public beta of AutoHotkey was released on November 10, 2003, after author Chris Mallett's proposal to integrate hotkey support into AutoIt v2 failed to generate response from the AutoIt community. Mallett built a new program from scratch basing the syntax on AutoIt v2 and using AutoIt v3 for some commands and the compiler. Later, AutoIt v3 switched from GPL to closed source because of "other projects repeatedly taking AutoIt code" and "setting themselves up as competitors".

In 2010, AutoHotkey v1.1 (originally called AutoHotkey_L) became the platform for ongoing development of AutoHotkey. In late 2012, it became the official branch. Another port of the program is AutoHotkey.dll. A well known fork of the program is AutoHotkey_H, which has its own subforum on the main site.

### Version 2

In July 2021, the first AutoHotkey v2 beta was released. The first release candidate was released on November 20, 2022, with the full release of v2.0.0 planned later in the year. On December 20, 2022, version 2.0.0 was officially released. On January 22, 2023, AutoHotkey v2 became the official primary version. AutoHotkey v1.1 became legacy and no new features were implemented, but this version was still supported by the site. On March 16, 2024, the final update of AutoHotkey v1.1 was released. AutoHotkey v1.1 has now reached its end of life (this version has been "deprecated").

## Examples

The following script searches for a particular word or phrase using Google. After the user copies text from any application to the clipboard, pressing the configurable hotkey ⊞ Win+G opens the user's default web browser and performs the search.

```mw
#g::Run "https://www.google.com/search?q=" . A_Clipboard
```

The following script defines a hotstring that enables the user to type *afaik* in any program and, when followed by an ending character, automatically replace it with "as far as I know":

```mw
::afaik::as far as I know
```

## User-contributed features

AutoHotKey extensions, interops and inline script libraries are available for use with and from other programming languages, including:

- VB/C# (.NET)
- Lua
- Lisp
- ECL
- Embedded machine code
- VBScript/JScript (Windows Scripting Host)

Other major plugins enable support for:

- Aspect-oriented programming
  - Function hooks
- COM wrappers
- Console interaction
- Dynamic code generation
- HIDs
- Internet Explorer automation
- GUI creation
- Synthetic programming
- Web services
- Windows event hooks

## Malware

When AutoHotkey is used to make standalone software for distribution, that software must include the part of AutoHotkey itself that understands and executes AutoHotkey scripts, as it is an interpreted language. Inevitably, some malware has been written using AutoHotkey. When anti-malware products attempt to earmark items of malware that have been programmed using AutoHotkey, they sometimes falsely identify AutoHotkey as the culprit rather than the actual malware.

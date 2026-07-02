---
title: "Vim (text editor)"
source: https://en.wikipedia.org/wiki/Vim_(text_editor)
domain: vim-editor
license: CC-BY-SA-4.0
tags: vim editor, text editor, modal editing, terminal editor
fetched: 2026-07-02
---

# Vim (text editor)

**Vim** (/vɪm/ ⓘ; short for **v**i **im**proved) is a free and open-source text editor. Vim provides both a terminal screen user interface as well as a graphical user interface (called gvim).

Vim's documentation describes it as an improved form of the older vi text editor (though it is built from a distinct codebase). In release information, the author originally implied that Vim was an abbreviation for "Vi IMitation", but later, the expansion was changed to "Vi IMproved" because, as described by the author, the functionality had increased beyond that of a clone of vi. Some sources indicate the change happened with v2.0, but conflicting information (including from author) suggests the change happened as early as v2.0 and as late as v3.0.

Since its original release for the Amiga, Vim has been ported to many environments including Atari MiNT, BeOS, MS-DOS, Windows starting from Windows NT 3.1, OS/2, OS/390, MorphOS, OpenVMS, QNX, RISC OS, Linux, BSD, and Classic Mac OS. Vim is also shipped with Apple macOS. Independent ports of Vim are available for Android and iOS.

Vim has been and continues to be popular for software development. In 2018, it was voted the most popular editor amongst *Linux Journal* readers. In 2015, the Stack Overflow developer survey found it to be the third most popular text editor, and, in 2019, the fifth most popular development environment.

## History

In 1988, Bram Moolenaar began work on what would become Vim. He used the codebase for the Stevie editor ported to Amiga (by Tony Andrews et al.) as a starting point. Version 1.14 (completed 2 November 1991) became the first public release. It was distributed via Fish Disk #591 in January 1992.

## License

Vim is released under the Vim license, which includes some charityware clauses that encourage users who enjoy the software to consider donating to children in Uganda. The Vim license is compatible with the GNU General Public License through a special clause allowing distribution of modified copies under the GNU GPL version 2.0 or later.

## User experience

### Text user interface

Building upon the core vi functionality, Vim provides a user experience that integrates keyboard-entered command input with a full-screen editing experience. Vim allows a user with a typical keyboard to keep their fingers on the home row, which can be an advantage for touch typing.

### Graphical user interface

Via its GUI mode (called gVim), it presents an interface with a more modern experience including aspects such as menus, toolbars and icons. The full functionality is still expressed through its command line mode.

### Help

Vim has a built-in help facility accessible via the `:help` command.

The Vim tutorial for beginners, called vimtutor, is usually installed alongside Vim, but is a separate executable and can be run separately.

The Vim Users' Manual details Vim's features and can be read from within Vim, or found online.

### Registers

Vim features various special memory entries called registers (not to be confused with hardware or processor registers). When cutting, deleting, copying, or pasting text the user can choose to store the manipulated text in a register. There are 36 general-purpose registers associated with letters and numbers ([a-z0-9]) and a range of special ones that either contain special values (current filename, last command, etc.) or serve a special purpose.

### Modes

Like vi, Vim supports multiple editing modes. Depending on the mode, entered characters are either processed as command input or inserted as text. Vim has 14 modes (7 basic modes and 7 variants):

- **Normal**: For editor commands. Generally, this is the default mode and ESC enters this mode.
- **Insert**: For editing content like in a modern editor.
- **Visual**: For selecting areas of text. Commands can be run on the selected area – moving, editing, filtering via built-in or external command, etc.
  - **Visual linewise**: Selects one or more whole lines.
  - **Visual blockwise**: Selects a rectangular block of text across one or more lines.
- **Select**: Similar to visual, but commands are not interpreted. Instead, highlighted text is directly replaced by input from the keyboard. This behavior mimics the selection mode in editors on Windows platforms.
- **Command-line (Cmdline)**: Provides a single line input at the bottom of the terminal. Commands (beginning with :) and some other keys for specific actions (including pattern search and the filter command) activate this mode. On completion of the command, Vim reverts to the previous mode.
- **Ex**: Accepts a sequence of commands.
- **Terminal-Job**: Interacting with a job in a terminal window.

## Customization

Vim is customizable and extensible, making it attractive to those who want control and flexibility in a text editing environment. Users can execute complex commands with *key bindings*, which can be customized and extended. The *recording* feature allows for the creation of macros to automate sequences of keystrokes and call internal or user-defined functions and mappings. Abbreviations, similar to macros and key mappings, facilitate the expansion of short strings of text into longer ones and can also be used to correct mistakes. Vim also features an *easy* mode for users wanting a simpler user experience.

There are many plugins available that extend or add new functionality to Vim. These plugins are usually written in Vim's internal scripting language, vimscript (also known as VimL), but can be written in other languages as well.

There are projects bundling together complex scripts and customizations and aimed at turning Vim into a tool for a specific task or adding a major flavour to its behaviour. Examples include Cream, which makes Vim behave like a click-and-type editor, or VimOutliner, which provides a comfortable outliner for users of Unix-like systems.

## Improvements

Vim provides many features beyond what vi provides. Some of Vim's enhancements include completion functions, comparison and merging of files (known as vimdiff), a comprehensive integrated help system, extended regular expressions, scripting languages (both native and through alternative scripting interpreters such as Perl, Python, Ruby, Tcl, etc.) including support for plugins, a graphical user interface (gvim), limited integrated development environment-like features, mouse interaction (both with and without the GUI), folding, editing of compressed or archived files in gzip, bzip2, bzip3, zip, and tar format and files over network protocols such as SSH, FTP, and HTTP, session state preservation, spell checking, split (horizontal and vertical) and tabbed windows, Unicode and other multi-language support, syntax highlighting, trans-session command, search and cursor position histories, multiple level and branching undo/redo history which can persist across editing sessions, and visual mode.

Vim continually saves information to a file that allows for recovering from a crash. Generally, the file extension is ".swp", but if the user tries to open a file when the recovery file already exists, then Vim notifies the user of the condition. If the user confirms to proceed, Vim uses a different extension to form a name for a file that does not exist. The extensions are along the progression: ".swo", ".swn", ".swm", etc. The feature can be disabled.

## Compatibility

Vim provides a vi-compatibility mode that limits its functionality to be similar to that of vi. However, even in compatibility mode, Vim is not entirely compatible with vi as specified by POSIX. For example, Vim does not support vi's open mode. Vim's developers state that it is "very much compatible with Vi".

## Vim script

**Vim script** (also called **Vimscript** or **VimL**) is the scripting language built into Vim. Based on the ex editor language of the original vi editor, early versions of Vim added commands for control flow and function definitions. Since version 7, Vim script also supports more advanced data types such as lists and dictionaries and a simple form of object-oriented programming. Built-in functions such as `map()` and `filter()` allow a basic form of functional programming, and Vim script has lambda since version 8.0. Vim script is mostly written in an imperative programming style.

Version 9.0 added **Vim9 script**, a new script language closer to commonly used languages.

Vim macros can contain a sequence of *normal-mode* commands, but can also invoke ex commands or functions written in Vim script for more complex tasks. Almost all extensions (called plugins or more commonly scripts) of the core Vim functionality are written in Vim script, but plugins can also utilize other languages like Perl, Python, Lua, Ruby, Tcl, or Racket. These plugins can be installed manually, or through a plugin manager such as Vundle, Pathogen, or Vim-Plug.

Vim script files are stored as plain text, similarly to other code, and the filename extension is usually `.vim`. One notable exception to that is Vim's config file, `.vimrc`.

### Examples

```mw
" This is the Hello World program in Vim script.
echo "Hello, world!"

" This is a simple while loop in Vim script.
let i = 1
while i < 5
  echo "count is" i
  let i += 1
endwhile
unlet i
```

## Versions

| When | Version | Changes |
|---|---|---|
| 1988 | 1.0 | Bram Moolenaar starts development; never publicly released |
| 2 Nov 1991 | 1.14 | The date Moolenaar ascribed to Vim's public release, based on the build date of version 1.14 |
| Jan 1992 | 1.14 | First public distribution; on Fish Disk #591 |
| 1992 | 1.22 | Port to Unix; never publicly released |
| 14 Dec 1993 | 2.0 | First release using the abbreviation expansion "Vi IMproved" |
| 12 Aug 1994 | 3.0 | Support for multiple windows |
| 29 May 1996 | 4.0 | Graphical user interface |
| 19 Feb 1998 | 5.0 | Syntax highlighting, basic scripting (user defined functions, commands, etc.) |
| 6 Apr 1998 | 5.1 | Bug fixes, various improvements |
| 27 Apr 1998 | 5.2 | Long line support, file browser, dialogs, popup menu, select mode, session files, user defined functions and commands, Tcl interface, etc. |
| 31 Aug 1998 | 5.3 | Bug fixes, etc. |
| 25 Jul 1999 | 5.4 | Basic file encryption, various improvements |
| 19 Sep 1999 | 5.5 | Bug fixes, various improvements |
| 16 Jan 2000 | 5.6 | New syntax files, bug fixes, etc. |
| 24 Jun 2000 | 5.7 | New syntax files, bug fixes, etc. |
| 31 May 2001 | 5.8 | New syntax files, bug fixes, etc. |
| 26 Sep 2001 | 6.0 | Folding, plugins, multi-language, etc. |
| 24 Mar 2002 | 6.1 | Bug fixes |
| 1 Jun 2003 | 6.2 | GTK2 and libgnome2 support, Arabic language support, :try command, minor features, bug fixes |
| 7 Jun 2004 | 6.3 | Bug fixes, translation updates, mark improvements |
| 15 Oct 2005 | 6.4 | Bug fixes, updates to Perl, Python, and Ruby support |
| 7 May 2006 | 7.0 | Spell checking, code completion, tab pages (multiple viewports/window layouts), current line and column highlighting, undo branches, and more |
| 12 May 2007 | 7.1 | Bug fixes, new syntax and runtime files, etc. |
| 9 Aug 2008 | 7.2 | Floating point support in scripts, refactored screen drawing code, bug fixes, new syntax files, etc. |
| 15 Aug 2010 | 7.3 | Lua support, Python3 support, Blowfish encryption, persistent undo/redo |
| 10 Aug 2013 | 7.4 | A new, faster regular expression engine. |
| 12 Sep 2016 | 8.0 | Asynchronous I/O support, jobs, lambdas, etc. |
| 18 May 2018 | 8.1 | Terminal window support and terminal gdb plugin. |
| 13 Dec 2019 | 8.2 | Popup windows, text properties. |
| 28 Jun 2022 | 9.0 | Vim9 script |
| 2 Jan 2024 | 9.1 | Classes and objects support for Vim9 script, smooth scrolling, virtual text |
| 14 Feb 2026 | 9.2 | Enums, Generic functions, and Tuples support for Vim9 script, improved diff mode, new completion features |

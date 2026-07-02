---
title: "GNU Emacs"
source: https://en.wikipedia.org/wiki/GNU_Emacs
domain: emacs-lisp
license: CC-BY-SA-4.0
tags: emacs lisp, elisp, gnu emacs, emacs config
fetched: 2026-07-02
---

# GNU Emacs

**GNU Emacs** is a text editor and suite of free software tools. Its development began in 1984 by GNU Project founder Richard Stallman, based on the Emacs editor developed for Unix operating systems. GNU Emacs has been a central component of the GNU project and a flagship project of the free software movement.

The program's tagline is "the extensible self-documenting text editor." Most functionality in GNU Emacs is implemented in user-accessible Emacs Lisp, allowing deep extensibility directly by users and through community-contributed packages. Its built-in features include a file browser and editor (Dired), an advanced calculator (Calc), an email client and news reader (Gnus), a Language Server Protocol integration, and the productivity system Org-mode. A large community of users have contributed extensions such as the Git interface Magit, the Vim emulation layer Evil, several search frameworks, the window manager EXWM, and tools for working with a wide range of programming languages.

## History

The original EMACS was written in 1976 by David A. Moon and Guy L. Steele Jr. as a set of macros for the TECO editor, and in 1984, Richard Stallman began work on GNU Emacs, to produce a free software replacement to the proprietary Gosling Emacs. GNU Emacs was initially based on Gosling Emacs, but Stallman's replacement of its Mocklisp interpreter with a true Lisp interpreter required that nearly all of its code be rewritten. This became the first program released by the then-nascent GNU Project. GNU Emacs is written in C and provides Emacs Lisp, also implemented in C, as an extension language. Version 13, the first public release, was made on March 20, 1985. The first widely distributed version of GNU Emacs was version 15.34, released later in 1985. Early versions of GNU Emacs were numbered as "1.x.x," with the initial digit denoting the version of the C core. The "1" was dropped after version 1.12 as it was thought that the major number would never change, and thus the major version skipped from "1" to "13". A new third version number was added to represent changes made by user sites. In the current numbering scheme, a number with two components signifies a release version, with development versions having three components.

GNU Emacs was later ported to the Unix operating system. It offered more features than Gosling Emacs, in particular a full-featured Lisp as its extension language, and soon replaced Gosling Emacs as the *de facto* Unix Emacs editor. Markus Hess exploited a security flaw in GNU Emacs's email subsystem in his 1986 cracking spree, in which he gained superuser access to Unix computers.

Although users commonly submitted patches and Elisp code to the net.emacs newsgroup, participation in GNU Emacs development was relatively restricted until 1999, and was used as an example of the "Cathedral" development style in *The Cathedral and the Bazaar*. The project has since adopted a public development mailing list and anonymous CVS access. Development took place in a single CVS trunk until 2008, and today uses the Git DVCS.

Richard Stallman has remained the principal maintainer of GNU Emacs, but he has stepped back from the role at times. Stefan Monnier and Chong Yidong oversaw maintenance from 2008. On September 21, 2015, Monnier announced that he would be stepping down as maintainer effective with the feature freeze of Emacs 25. Longtime contributor John Wiegley was announced as the new maintainer on November 5, 2015. Wiegley was joined by Eli Zaretskii in July, 2016, and Lars Ingebrigtsen in September, 2020. Wiegley stepped down in 2018, and Ingebrigtsen concluded his term with the release of Emacs 29.1, leaving Zaretskii as lead maintainer. Stefan Kangas was appointed as co-maintainer in 2023, and Andrea Corallo joined Zaretskii and Kangas in 2024.

## Licensing

The terms of the GNU General Public License (GPL) state that the Emacs source code, including both the C and Emacs Lisp components, are freely available for examination, modification, and redistribution.

Older versions of the GNU Emacs documentation appeared under an ad-hoc license that required the inclusion of certain text in any modified copy. In the GNU Emacs user's manual, for example, this included instructions for obtaining GNU Emacs and Richard Stallman's essay *The GNU Manifesto*. The XEmacs manuals, which were inherited from older GNU Emacs manuals when the fork occurred, have the same license. Newer versions of the documentation use the GNU Free Documentation License with "invariant sections" that require the inclusion of the same documents and that the manuals proclaim themselves as *GNU Manuals*.

For GNU Emacs, like many other GNU packages, it remains policy to accept significant code contributions only if the copyright holder executes a suitable disclaimer or assignment of their copyright interest to the Free Software Foundation (FSF.) Small contributions of fewer than 10 lines of code are exempt. This policy is in place so that the FSF can defend the software in court if its copyleft license is violated.

In 2011, it was noticed that GNU Emacs had been accidentally releasing some binaries without corresponding source code for two years, in opposition to the intended spirit of the GPL. Richard Stallman described this incident as "a very bad mistake," which was promptly fixed. The FSF did not sue any downstream redistributors who unknowingly violated the GPL by distributing these binaries.

## Using GNU Emacs

### Commands

In its normal editing mode, GNU Emacs behaves like common text editors by allowing the user to type text with the keyboard and move the editing point with arrow keys. Escape key sequences or pressing the control key and/or the meta key, alt key or super keys in conjunction with a regular key produces modified keystrokes that invoke functions from the Emacs Lisp environment. Commands such as `save-buffer` and `save-buffers-kill-emacs` combine multiple modified keystrokes.

Some GNU Emacs commands work by invoking external programs, such as ispell for spell-checking and the GNU Compiler Collection (GCC) for program compilation. Emacs also supports "inferior processes," long-lived child processes that interact with the editor. This is used to implement shell-mode, running a Unix shell as inferior process, as well as read–eval–print loop (REPL) modes for various programming languages. Emacs' support for external processes makes it suitable for interactive programming along the lines of Interlisp or Smalltalk.

Users who prefer the widely used IBM Common User Access keyboard shortcut layout can use cua-mode, a package that originally was a third-party add-on but has been included in GNU Emacs since version 22.

### Minibuffer

Emacs uses the "minibuffer," normally the bottommost line, to display messages and request information, functions that are often performed by dialog boxes in GUI editors. The minibuffer holds information such as text to target in a search or the name of a file to read or save. When applicable, command-line completion is available using the tab and space keys.

### File management and display

Emacs keeps text in data structures known as buffers. Buffers may or may not be displayed onscreen, and all buffer features are accessible by both Emacs Lisp programs and the user interface. The user can create new buffers and dismiss unwanted ones, and many buffers can exist at the same time, limited only by available memory. Emacs can be configured to save the list of open buffers on exit, and reopen this list when it is restarted.

Some buffers contain text loaded from text files, which the user can edit and save back to permanent storage. These buffers are said to be "visiting" files. Buffers also serve to display other data, such as the output of Emacs commands, dired directory listings, documentation strings displayed by the "help" library and notification messages that in other editors would be displayed in a dialog box. Some of these notifications are displayed briefly in the minibuffer, and GNU Emacs provides a *Messages* buffer that keeps a history of the most recent notifications of this type. When the minibuffer is used for output from Emacs, it is called the "echo area". Longer notifications are displayed in buffers of their own. The maximum length of messages that will be displayed in the minibuffer is, of course, configurable.

Buffers can also serve as input and output areas for an external process such as a shell or REPL. Buffers which Emacs creates on its own are typically named with asterisks on each end, to distinguish from user buffers. The list of open buffers is itself displayed in this type of buffer.

Most Emacs key sequences remain functional in any buffer. For example, the standard Ctrl-s `isearch` function can be used to search filenames in dired buffers, and the file list can be saved to a text file just as any other buffer. Dired buffers can be switched to a writable mode, in which filenames and attributes can be edited textually; when the buffer is saved, the changes are written to the filesystem. This allows multiple files to be renamed using the search and replace features of Emacs. When so equipped, Emacs displays image files in buffers. Emacs is binary safe and 8-bit clean.

Emacs can split the editing area into separate non-overlapping sections called "windows," a feature that has been available since 1975, predating the graphical user interface in common use. In Emacs terminology, "windows" are similar to what other systems call "frames" or "panes" – a rectangular portion of the program's display that can be updated and interacted with independently. Each Emacs window has a status bar called the "mode line" displayed by default at the bottom edge of the window. Emacs windows are available both in text-terminal and graphical modes and allow more than one buffer, or several parts of a buffer, to be displayed at once. Common applications are to display a dired buffer along with the contents of files in the current directory (there are special modes to make the file buffer follow the file highlighted in dired), to display the source code of a program in one window while another displays a shell buffer with the results of compiling the program, to run a debugger along with a shell buffer running the program, to work on code while displaying a man page or other documentation (possibly loaded over the World Wide Web using one of Emacs' built-in web browsers) or simply to display multiple files for editing at once such as a header along with its implementation file for C-based languages. In addition, there is follow-mode, a minor mode that chains windows to display non-overlapping portions of a buffer. Using follow-mode, a single file can be displayed in multiple side-by-side windows that update appropriately when scrolled. In addition, Emacs supports "narrowing" a buffer to display only a portion of a file, with top/bottom of buffer navigation functionality and buffer size calculations reflecting only the selected range.

Emacs windows are tiled and cannot appear "above" or "below" their companions. Emacs can launch multiple "frames", which are displayed as individual windows in a graphical environment. On a text terminal, multiple frames are displayed stacked filling the entire terminal, and can be switched using the standard Emacs commands.

### Major modes

GNU Emacs can display or edit a variety of different types of text and adapts its behavior by entering add-on modes called "major modes". There are major modes for many different purposes including editing ordinary text files, the source code of many markup and programming languages, as well as displaying web pages, directory listings and other system info. Each major mode involves an Emacs Lisp program that extends the editor to behave more conveniently for the specified type of text. Major modes typically provide some or all of the following common features:

- Syntax highlighting ("font lock"): combinations of fonts and colors, termed "faces," that differentiate between document elements such as keywords and comments.
- Automatic indentation to maintain consistent formatting within a file.
- The automatic insertion of elements required by the structure of the document, such as spaces, newlines, and parentheses.
- Special editing commands, such as commands to jump to the beginning or the end of a function while editing a programming file or commands to validate documents or insert closing tags while working with markup languages such as XML.

### Minor modes

The use of "minor modes" enables further customization. A GNU Emacs editing buffer can use only one major mode at a time, but multiple minor modes can operate simultaneously. These may operate directly on documents, as in the way the major mode for the C programming language defines a separate minor mode for each of its popular indent styles, or they may alter the editing environment. Examples of the latter include a mode that adds the ability to undo changes to the window configuration and one that performs on-the-fly syntax checking. There is also a minor mode that allows multiple major modes to be used in a single file, for convenience when editing a document in which multiple programming languages are embedded.

### "Batch mode"

GNU Emacs supports the capability to use it as an interpreter for the Emacs Lisp language without displaying the text editor user interface. In batch mode, user configuration is not loaded and the terminal interrupt characters C-c and C-z will have their usual effect of exiting the program or suspending execution instead of invoking Emacs keybindings. GNU Emacs has command line options to specify either a file to load and execute, or an Emacs Lisp function may be passed in from the command line. Emacs will start up, execute the passed-in file or function, print the results, then exit. The shebang line `#!/usr/bin/emacs --script` allows the creation of standalone scripts in Emacs Lisp.

## Manuals

The *GNU Emacs Manual*, written by Richard Stallman, is bundled with GNU Emacs and can be viewed with the built-in info browser. Two additional manuals, the *Emacs Lisp Reference Manual* by Bil Lewis, Richard Stallman, and Dan Laliberte and *An Introduction to Programming in Emacs Lisp* by Robert Chassell, are included. All three manuals are also published in book form by the Free Software Foundation.

## Internationalization

GNU Emacs has support for many alphabets, scripts, writing systems, and cultural conventions and provides spell-checking for many languages by calling external programs such as ispell. Version 24 added support for bidirectional text and left-to-right and right-to-left writing direction for languages such as Arabic, Persian and Hebrew.

Many character encoding systems, including UTF-8, are supported. GNU Emacs uses UTF-8 for its encoding as of version 23, while prior versions used their own encoding internally and performed conversion upon load and save. The internal encoding used by XEmacs is similar to that of GNU Emacs but differs in details.

The GNU Emacs user interface originated in English and, with the exception of the beginners' tutorial, has not been translated into any other language.

A subsystem called *Emacspeak* enables visually impaired and blind users to control the editor through audio feedback.

## Extensibility

The behavior of GNU Emacs can be modified and extended almost without limit by incorporating Emacs Lisp programs that define new commands, new buffer modes, new keymaps, add command-line options, and so on. Many extensions providing user-facing functionality define a major mode (either for a new file type or to build a non-text-editing user interface); others define only commands or minor modes, or provide functions that enhance another extension.

Since version 24 GNU Emacs includes a built-in package manager accessible with the `list-packages` command that allows users to search for and install packages. Historically, packages were downloaded manually, often distributed through the Usenet newsgroup gnu.emacs.sources. Now, packages can be retrieved from various ELPA (Emacs Lisp Package Archive) repositories, including one run by the GNU Project. Over time many popular packages have been included in Emacs by default; for example version 21 began bundling Org-mode, Calc, TRAMP, and many others.

Notable packages include:

- AUCTeX, tools to edit and process TeX and LaTeX documents
- Dired, a file manager
- Dissociated press, a Racter-like text generator
- Dunnet, a text adventure
- Emacs Web Wowser (eww), a web browser.
- Emacs Speaks Statistics (ESS) modes for editing statistical languages like R and SAS
- ERC, an IRC client
- Eshell, a command line shell written in Emacs Lisp. This allows closer integration with the Emacs environment than standard shells such as bash or PowerShell, which are also available from within Emacs. For example, in Eshell, Elisp functions are available as shell commands and output from Unix commands can be redirected to an Emacs buffer.
- Exwm, an X window manager allowing X11 apps to be run in an Emacs window.
- Gnus, a full-featured news client (newsreader) and email client and early evidence for Zawinski's Law
- Magit, for working with the version control system Git
- MULtilingual Enhancement to Emacs (MULE) allows editing of text in multiple languages in a manner somewhat analogous to Unicode
- Org-mode for keeping notes, maintaining various types of lists, planning and measuring projects, and composing documents in many formats (such as PDF, HTML, or OpenDocument formats). There are static site generators using org mode, as well as an extension, Babel, allowing it to be used for literate programming.
- Rcirc, an IRC client
- Superior Lisp Interaction Mode for Emacs (SLIME) extends GNU Emacs into a development environment for Common Lisp. With SLIME (written in Emacs Lisp) the GNU Emacs editor communicates with a Common Lisp system (using the SWANK backend) over a special communication protocol and provides such tools as a read–eval–print loop, a data inspector and a debugger.
- Texinfo (Info), an online help-browser

## Performance

In its early history, GNU Emacs often ran noticeably slower than rival text editors because the loading and interpreting of its Lisp-based code incurs a performance overhead. Modern computers are powerful enough to run GNU Emacs with ease, but versions prior to 19.29 (released in 1995) couldn't edit files larger than 8 MB. The file size limit was raised in successive versions, and 32 bit versions after GNU Emacs 23.2 can edit files up to 512 MB in size. Emacs compiled on a 64-bit machine can handle much larger buffers.

While GNU Emacs is largely written in Emacs Lisp, it makes extensive use of natively compiled C code to improve performance. In addition to its own C code, it uses external libraries such as libxml2 for parsing XML. Packages installed by the user can load dynamic modules.

Since version 28.1, Emacs can natively compile Emacs Lisp files via `libgccjit`, as opposed to just byte compiling them, resulting in a significant boost in performance.

## Platforms

GNU Emacs runs on a wide variety of operating systems, including DOS, Windows, and most Unix-like operating systems, such as Linux, the various BSDs, Solaris, AIX, HP-UX and macOS. Many Unix-like systems include Emacs by default. In 2023 an official port for Android was released. Version 23.1 removed support for some platforms deemed obsolete.

GNU Emacs runs both on text terminals and in graphical user interface (GUI) environments. On Unix-like operating systems, GNU Emacs can use the X Window System to produce its GUI either directly using Athena widgets or by using a "widget toolkit" such as Motif, LessTif, or GTK+. GNU Emacs can also use the graphics systems native to macOS and Windows to provide menubars, toolbars, scrollbars and context menus conforming more closely to each platform's look and feel.

## Spelling of name

The correct spelling is "GNU Emacs", not "GNU/Emacs", following the rules of English, in the construction "GNU Emacs" the word "GNU" modifies "Emacs." That is the right way to describe a program called Emacs which is a GNU package.

## Forks

### XEmacs

Lucid Emacs, based on an early version of GNU Emacs 19, was developed beginning in 1991 by Jamie Zawinski and others at Lucid Inc. One of the best-known forks in free software development occurred when the codebases of the two Emacs versions diverged and the separate development teams ceased efforts to merge them back into a single program. After Lucid filed for bankruptcy, Lucid Emacs was renamed XEmacs. XEmacs development has slowed, with the most recent stable version 21.4.22 released in January 2009, while GNU Emacs has implemented many formerly XEmacs-only features. This has led some users to proclaim XEmacs' obsolescence.

### Other forks of GNU Emacs

Other forks, less known than XEmacs, include:

- Meadow – a Japanese version for Microsoft Windows
- SXEmacs – Steve Youngs' fork of XEmacs
- Aquamacs – a version which focuses on integrating with the Apple Macintosh user interface
- Remacs – an incremental port of GNU Emacs to the Rust programming language, incomplete and no longer maintained as of 2023.
- emacs-ng  – is an attempt to bring modern JavaScript tooling into emacs while remaining backwards compatible.

## Release history

Changes in each Emacs release are listed in a NEWS file distributed with Emacs. Changes brought about by *downgrading* to the previous release are listed in an "Antinews" file, often with some snarky commentary on why this might be desirable.

| Version | Release date | Significant changes |
|---|---|---|
| 30.2 | August 14, 2025 | Bugfix release |
| 30.1 | February 23, 2025 | Native compilation of Lisp files is enabled by default. Native JSON is now always available. Includes built-in support for EditorConfig files. Bundles the popular which-key package. Native support for using Emacs on Android and touchscreens. Numerous performance improvements. |
| 29.4 | June 22, 2024 | Security release. |
| 29.3 | March 24, 2024 | Security release. |
| 29.2 | January 18, 2024 | Bugfix release. |
| 29.1 | July 30, 2023 | Adds Tree-sitter parser integration and a pure GTK frontend enabling Wayland support. Bundles popular packages including language server protocol package Eglot, package manager use-package, and csharp-mode for C# programming. |
| 28.2 | September 12, 2022 | A bug-fix release with no new features. |
| 28.1 | April 4, 2022 | Native compilation of Lisp files. Text shaping with HarfBuzz and drawing with Cairo. Support for loading Secure Computing filters. Much improved display of Emoji and Emoji sequences. Mode-specific commands. Emacs shows matching parentheses by default. |
| 27.2 | March 25, 2021 | Mainly a bugfix release. |
| 27.1 | August 10, 2020 | Built-in support for arbitrary-size integers. Text shaping with HarfBuzz. Native support for JSON parsing. Better support for Cairo drawing. Portable dumping used instead of unexec. Support for XDG conventions for init files. Additional early-init initialization file. Lexical-binding is used by default. Built-in support for tab bar and tab-line. Support for resizing and rotating of images without ImageMagick. |
| 26.3 | August 28, 2019 | New GPG key for GNU Emacs Lisp Package Archive (ELPA) package signature checking. |
| 26.2 | April 12, 2019 | Emacs modules can now be built outside of the Emacs tree source. Compliance with Unicode version 11.0. |
| 26.1 | May 28, 2018 | Limited form of concurrency with Lisp threads. Support for optional display of line numbers in the buffer. Emacs now uses double buffering to reduce flicker on the X Window System. Flymake has been completely redesigned. TRAMP has a new connection method for Google Drive. New single-line horizontal scrolling mode. A systemd user unit file is provided. Support for 24-bit colors on capable text terminals. |
| 25.3 | September 11, 2017 | Emergency release to fix a security vulnerability in Emacs. |
| 25.2 | April 21, 2017 | Mainly a bugfix release. |
| 25.1 | September 17, 2016 | Support for loading shared/dynamic libraries (modules). Validation of TLS/SSL certificates. New minor mode 'electric-quote-mode' for using curved quotes. Character folding support in isearch.el. Support for embedding native widgets inside Emacs buffers. New and improved facilities for inserting Unicode characters. |
| 24.5 | April 10, 2015 | Mainly a bugfix release. |
| 24.4 | October 20, 2014 | Support for ACLs (access control lists) and digital signatures of Emacs Lisp packages. Improved fullscreen and multi-monitor support. Support for saving and restoring the state of frames and windows. Improved menu support on text terminals. Another built-in web browser (`M-x eww`). A new rectangular mark mode (`C-x SPC`). File notification support. |
| 24.3 | March 10, 2013 | Generalized variables are now in core Emacs Lisp, an update for the Common Lisp emulation library, and a new major mode for Python. |
| 24.2 | August 27, 2012 | Bugfix release |
| 24.1 | June 10, 2012 | ELPA, support for native color themes, optional GTK+3, support for bi-directional input, support for lexical scoping in Emacs Lisp |
| 23.4 | January 29, 2012 | Fixes a security flaw. |
| 23.3 | March 10, 2011 | Improved functionality for using Emacs with version control systems. |
| 23.2 | May 8, 2010 | New tools for using Emacs as an IDE, including navigation across a project and automatic Makefile generation. New major mode for editing JavaScript source. In GUIs, the cursor is hidden while the user types. |
| 23.1 | July 29, 2009 | Support for anti-aliased fonts on X through Xft, better Unicode support, Doc-view mode and new packages for viewing PDF and PostScript files, connection to processes through D-Bus (dbus), connection to the GNU Privacy Guard (EasyPG), nXML mode for editing XML documents, Ruby mode for editing Ruby programs, and more. Use of the Carbon GUI libraries on Mac OS X was replaced by use of the more modern Cocoa GUI libraries. |
| 22.3 | September 5, 2008 | GTK+ toolkit support, enhanced mouse support, a new keyboard macro system, improved Unicode support, and drag-and-drop operation on X. Many new modes and packages including a graphical user interface to GDB, Python mode, the mathematical tool Calc, and the remote file editing system Tramp ("Transparent Remote (file) Access, Multiple Protocol"). |
| 22.2 | March 26, 2008 | New support for the Bazaar, Mercurial, Monotone, and Git version control systems. New major modes for editing CSS, Vera, Verilog, and BibTeX style files. Improved scrolling support in Image mode. |
| 22.1 | June 2, 2007 | Support for the GTK+ graphical toolkit, support for drag-and-drop on X, support for the Mac OS X Carbon UI, org-mode version 4.67d included |
| 21.1 | October 20, 2001 | Support for displaying colors and some other attributes on terminals, built-in horizontal scrolling, sound support, wheel mouse support, improved menu-bar layout, support for images, toolbar, and tooltips, Unicode support |
| 20.1 | September 17, 1997 | Multi-lingual support |
| 19.34 | August 22, 1996 | Bug fix release with no user-visible changes |
| 19.31 | May 25, 1996 | Emacs opens X11 frames by default, scroll bars on Windows 95 and NT, subprocesses on Windows 95, `recover-session` to recover multiple files after a crash, some `[[doctor.el]]` features removed to comply with the US Communications Decency Act |
| 19.30 | November 24, 1995 | Multiple frame support on MS Windows, menu bar available on text terminals, `pc-select` package to emulate common Windows and Macintosh keybindings. |
| 19.29 | June 19, 1995 | Significant improvements to performance, font support, and image handling. It offered faster performance, expanded font options, including scalable fonts, and enhanced image format support. Additionally, it improved internationalization features and introduced more customization options, further enhancing the user experience. |
| 19.28 | November 1, 1994 | First official v19 release. Support for multiple frames using the X Windowing System; VC, a new interface for version control systems, font-lock mode, hexl mode for hexadecimal editing. |
| 18.59 | October 31, 1992 | Emacs 18.59 included enhancements and bug fixes compared to previous versions of Emacs 18.x. |
| 18.53 | February 23, 1989 | Emacs 18.53 introduced support for font-locking, which allowed syntax highlighting in different programming modes. This feature greatly enhanced the readability of code by highlighting different language elements with distinct colors or styles. It also included various bug fixes and improvements over previous versions. |
| 18.52 | August 17, 1988 | Introduced `spook.el`, a library for adding some "distract the NSA" keywords to every message you send. |
| 18.24 | October 2, 1986 | Server mode, `M-x disassemble`, Emacs can open TCP connections, `emacs -nw` to open Emacs in console mode on xterms. |
| 17.36 | December 20, 1985 | Backup file version numbers |
| 16.56 | July 15, 1985 | First Emacs 16 release. Emacs-lisp-mode distinct from lisp-mode, remove all code from Gosling Emacs due to copyright issues |
| 13.8? | March 20, 1985 | First release. However, the VAXSIG VAX85b DECUS tape has version 13.8 with file dates of June 19, 1985 with RCS files dated March 31, 1985. It's a badly damaged copy. Version 13.9 is referenced in the news file, so 13.8 may have been the first release since there are no other 13.x releases named. |

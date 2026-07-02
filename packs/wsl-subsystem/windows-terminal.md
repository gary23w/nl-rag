---
title: "Windows Terminal"
source: https://en.wikipedia.org/wiki/Windows_Terminal
domain: wsl-subsystem
license: CC-BY-SA-4.0
tags: windows subsystem for linux, wsl subsystem, subsystem for android, windows terminal
fetched: 2026-07-02
---

# Windows Terminal

**Windows Terminal** is a multi-tabbed terminal emulator developed by Microsoft for Windows 10 and later as a replacement for Windows Console. It can run any command-line app in a separate tab. It is preconfigured to run Command Prompt, PowerShell, Windows Subsystem for Linux and Azure Cloud Shell Connector, and can also connect to SSH by manually configuring a profile. Windows Terminal comes with its own rendering back-end; starting with version 1.11 on Windows 11, command-line apps can run using this newer back-end instead of the old Windows Console.

Since Windows 11 22H2 and Windows Terminal 1.15, Windows Terminal replaces Windows Console as the default.

## History

Windows Terminal was announced at Microsoft's Build 2019 developer conference in May 2019 as a modern alternative for Windows Console, and Windows Terminal's source code first appeared on GitHub on May 3, 2019. The first preview release was version 0.2, which appeared on July 10, 2019. The first stable version of the project (version 1.0) was on May 19, 2020, at which point, Microsoft started releasing preview versions as the Windows Terminal Preview app, which could be installed side-by-side with the stable version.

## Features

Terminal is a command-line front-end. It can run multiple command-line apps, including text-based shells in a multi-tabbed window. It has out-of-the-box support for Command Prompt, PowerShell, and Bash on Windows Subsystem for Linux (WSL). It can natively connect to Azure Cloud Shell.

Terminal augments the text-based command experience by providing support for:

- Notebook tabs, to hold multiple instances in a single window
- ANSI VT sequence support
- UTF-8 and UTF-16 (including CJK ideograms and emojis)
- Hardware-accelerated text rendering via DirectWrite
- Modern font and font feature support (see below)
- 24-bit color
- Window transparency effects
- Themes, background images and tab color settings
- Different window modes (e.g. fullscreen mode, focus mode, always on top mode)
- Split panes
- Command palette
- Jump list support
- Microsoft Narrator compatibility via a User Interface Automation (UIA) tree
- Support for embedded hyperlinks
- Copying text to clipboard in HTML and RTF format
- Mouse input
- Customizable key bindings
- Incremental search
- Terminal shortcut
- Sixel support

### Cascadia Code

Cascadia Code is a purpose-built monospaced font by Aaron Bell of Saja Typeworks for the new command-line interface. It includes programming ligatures and was designed to enhance the look and feel of Windows Terminal, terminal applications and text editors such as Visual Studio and Visual Studio Code. The font is open-source under the SIL Open Font License and available on GitHub. It is bundled with Windows Terminal since version 0.5.2762.0.

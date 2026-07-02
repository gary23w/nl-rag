---
title: "Terminal multiplexer"
source: https://en.wikipedia.org/wiki/Terminal_multiplexer
domain: tmux
license: CC-BY-SA-4.0
tags: tmux multiplexer, terminal multiplexer, terminal sessions, pane splitting
fetched: 2026-07-02
---

# Terminal multiplexer

A **terminal multiplexer** is a software application that can be used to multiplex several separate pseudoterminal-based login sessions inside a single terminal display, terminal emulator window, PC/workstation system console, or remote login session, or to detach and reattach sessions from a terminal. It is useful for dealing with multiple programs from a command line interface, and for separating programs from the session of the Unix shell that started the program, particularly so a remote process continues running even when the user is disconnected.

## Features

A terminal multiplexer can be thought of as a text version of graphical window managers, or as a way of attaching virtual terminals to any login session. It is a wrapper that allows multiple text programs to run at the same time, and provides features that allow the user to use the programs within a single interface productively.

**Persistence**

Similar to

Virtual Network Computing

, many terminal multiplexers allow the user to start applications from one computer, and then reconnect from a different computer and continue using the same application without having to restart it. This makes accessing the same session between different locations like work and home simple. These multiplexers generally provide terminal-agnostic functionality so that users can disconnect and reconnect using different terminal types, allowing applications to continue running without being aware of the change in terminals.

Concretely, the multiplexer starts a session (with associated processes), and then either does not attach a terminal to it, or attaches a terminal but can subsequently detach it (for example if the network connection is dropped). Since the session does not end, the processes are not sent a "hangup" signal (

SIGHUP

) and are not terminated, so they continue running, and one can subsequently (re)attach a terminal to the session and continue interacting, or simply leave the session unattached.

**Multiple windows**

Multiple terminal sessions can be created, each of which usually runs a single application. The windows are numbered, and the user can use the keyboard to switch between them. Some

GUI

terminal emulators provide tabs or otherwise similar functionality to this. Each window has its own scroll-back buffer, so that output is captured even when the window isn't actively displayed, and that history can be saved even when migrating to another computer. Windows can be split-screened. While some text applications have this functionality built in, a terminal multiplexer allows any application to be split-screened alongside any number of other applications.

**Session Sharing**

Terminal multiplexers allow multiple computers to connect to the same session at once, enabling collaboration between multiple users. The same computer can also be used to make multiple simultaneous connections, providing alternative functionality to screen-splitting, particularly for computers with multiple monitors.

## Implementations

- **Byobu**: A profile and configuration utility for GNU Screen and tmux.
- **dvtm**: Tiling window management for the console.
- **GNU Screen**: the prototypical terminal multiplexer, first released in 1987.
- **mtm**: billed as "perhaps the smallest useful terminal multiplexer in the world"
- **neercs**: ("screen" spelled backwards) is a GNU screen workalike. It supports window thumbnailing and graphical animated screensavers. It also supports 3D console switching (switching between consoles mapped to the faces of a cube) via the libcaca ASCII art library.
- **splitvt**: split terminal utility.
- **TD/SMP**: introduced by DEC on their VT330/340 terminals, TD/SMP was proprietary and only widely supported by their own terminal servers.
- **tmux**: A modern GNU Screen workalike, released in 2007; it is BSD-licensed, allows multiple panes (with optional Xterm mouse support), and has a scriptable command interface. tmux aimed to allow the sharing of a single window between multiple terminals, while keeping the other windows in the same session entirely separate. tmux has been part of the OpenBSD base system since 2009's version 4.6.
- **Twin** ("Text mode WINdow environment"): a full-fledged window manager for text windows. Initially started as an MS-DOS project, it was later ported to Linux.
- **Zellij**: A terminal workspace with batteries included.

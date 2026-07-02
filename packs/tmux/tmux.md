---
title: "tmux"
source: https://en.wikipedia.org/wiki/Tmux
domain: tmux
license: CC-BY-SA-4.0
tags: tmux multiplexer, terminal multiplexer, terminal sessions, pane splitting
fetched: 2026-07-02
---

# tmux

**tmux** is an open-source terminal multiplexer for Unix-like operating systems. It allows multiple terminal sessions to be accessed simultaneously in a single window. It is useful for running more than one command-line program at the same time. It can also be used to detach processes from their controlling terminals, allowing remote sessions to remain active without being visible.

## Features

tmux includes most features of GNU Screen. It allows users to start a terminal session with clients that are not bound to a specific physical or virtual console; multiple terminal sessions can be created within a single terminal session and then freely rebound from one virtual console to another, and each session can have several connected clients.

Some notable tmux features are:

- Menus for interactive selection of running sessions, windows or clients
- Window can be linked to an arbitrary number of sessions
- vi-like or Emacs command mode (with auto completion) for managing tmux
- Vertical and horizontal window split support

tmux lacks built-in serial port and telnet support. It uses different command keys from the ones used by screen, so it is not a drop-in replacement for screen, but it can be configured to use compatible keybindings.

## Availability

tmux is included in the OpenBSD base system, and is available as a package for many other Unix-like operating systems.

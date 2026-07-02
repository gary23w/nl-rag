---
title: "GNU Screen"
source: https://en.wikipedia.org/wiki/GNU_Screen
domain: tmux
license: CC-BY-SA-4.0
tags: tmux multiplexer, terminal multiplexer, terminal sessions, pane splitting
fetched: 2026-07-02
---

# GNU Screen

**GNU Screen** is a terminal multiplexer: a software application that can be used to multiplex several virtual consoles, allowing a user to access multiple separate login sessions inside a single terminal window, or detach and reattach sessions from a terminal. It is useful for dealing with multiple programs from a command line interface, and for separating programs from the session of the Unix shell that started the program, particularly so a remote process continues running even when the user is disconnected.

Released under the terms of version 3 or later of the GNU General Public License, GNU Screen is free software.

## Features

GNU Screen can be thought of as a text version of graphical window managers, or as a way of putting virtual terminals into any login session. It is a wrapper that allows multiple text programs to run at the same time, and provides features that allow the user to use the programs within a single interface productively. This enables the following features: persistence, multiple windows, and session sharing.

Screen is often used when a network connection to the terminal is unreliable, as a dropped network connection typically terminates all programs the user was running (child processes of the login session), due to the session ending and sending a "hangup" signal (SIGHUP) to all the child processes. Running the applications under screen means that the session does not terminate – only the now-defunct terminal gets detached – so applications don't even know the terminal has detached, and allows the user to reattach the session later and continue working from where they left off.

## History

Screen was originally designed by Oliver Laumann and Carsten Bormann at Technische Universität Berlin and published in 1987.

Design criteria included VT100 emulation (including ANSI X3.64 (ISO 6429) and ISO 2022) and reasonable performance for heavy daily use when character-based terminals were still common. Later, the at-the-time novel feature of disconnection/reattachment was added.

Around 1990, Laumann handed over maintenance of the code to Jürgen Weigert and Michael Schroeder at the University of Erlangen–Nuremberg, who later moved the project to the GNU Project and added features such as scrollback, split-screen, copy-and-paste, and screen sharing.

By 2014, development had slowed to a crawl. Wanting to change this, Amadeusz Sławiński volunteered to help. In response, Laumann granted him maintainership. Sławiński proceeded to put out the first new Screen release in half a decade. Because there were some unofficial "Screen 4.1" releases floating around the Internet, he called this new release "Screen 4.2.0".

In May 2015, on openSUSE Conference, Jürgen Weigert invited Alexander Naumov to help to develop and maintain GNU screen. Two months later with Alex's help *GNU screen 4.3.0* was released.

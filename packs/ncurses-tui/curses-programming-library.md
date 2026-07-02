---
title: "curses (programming library)"
source: https://en.wikipedia.org/wiki/Curses_(programming_library)
domain: ncurses-tui
license: CC-BY-SA-4.0
tags: ncurses library, curses tui programming, text-based user interface, terminal ui library
fetched: 2026-07-02
---

# curses (programming library)

**curses** is a terminal control library for Unix-like systems, enabling the construction of text user interface (TUI) applications.

The name is a pun on the term "cursor optimization". It is a library of functions that manage an application's display on character-cell terminals (e.g., VT100).

ncurses is the approved replacement for 4.4BSD classic curses.

## Overview

Using curses, programmers are able to write text-based applications without writing directly for any specific terminal type. The curses library on the executing system sends the correct control characters based on the terminal type. It provides an abstraction of one or more windows that maps onto the terminal screen. Each window is represented by a character matrix. The programmer sets up the desired appearance of each window, then tells the curses package to update the screen. The library determines a minimal set of changes that are needed to update the display and then executes these using the terminal's specific capabilities and control sequences.

In short, this means that the programmer creates a character matrix of how the screen should look and lets curses handle the work.

The curses API is described in several places. Most implementations of curses use a database that can describe the capabilities of thousands of different terminals. There are a few implementations, such as PDCurses, which use specialized device drivers rather than a terminal database. Most implementations use terminfo; some use termcap. Curses has the advantage of back-portability to character-cell terminals and simplicity. For an application that does not require bit-mapped graphics or multiple fonts, an interface implementation using curses will usually be much simpler and faster than one using an X toolkit.

## History

The first curses library was written by Ken Arnold and originally released with BSD UNIX, where it was used for several games, most notably *Rogue*. Some improvements were made to the BSD library in the 1990s as "4.4BSD" curses, e.g., to provide more than one type of video highlighting. However, those are not widely used.

The name "curses" is a pun on *cursor optimization*. Sometimes it is incorrectly stated that curses was used by the vi editor; in actuality, the code in curses that optimizes moving the cursor was borrowed from vi, which predated curses.

According to Goodheart, Ken Arnold's original implementation of curses started by reusing functions from the termcap library, and adding to that. A few years later, Mary Ann Horton, who had maintained the vi and termcap sources at Berkeley, went to AT&T Corporation and made a different version using terminfo, which became part of UNIX System III and UNIX System V. Due to licensing restrictions on the latter, the BSD and AT&T versions of the library were developed independently. In addition to the termcap/terminfo improvement, other improvements were made in the AT&T version:

**video highlighting (bold, underline)**

The BSD version supported only

standout

.

**line-drawing**

The BSD version gave little support here.

**colors**

This was not supported in the BSD version.

AT&T curses development appears to have halted in the mid-1990s when X/Open Curses was defined. In 1995, BSD maintainer, Keith Bostic, officially deprecated the curses library in favor of ncurses. Development of ncurses and PDCurses continues. A version of BSD curses continues to be maintained in the NetBSD operating system (wide character support, termcap to terminfo migration, etc.).

### pcurses and PDCurses

Different lines of development started by imitating the AT&T curses, from at least three implementations: **pcurses** by Pavel Curtis (started in 1982), **PDCurses** (Public Domain curses) by Mark Hessling to support his editor THE (started in 1987) as well as Rexx/Curses, and **PC curses** (version 1.4 and earlier by Björn Larsson-based inspired by Pavel Curtis' library before 1990).

### ncurses

**ncurses** (new curses) "originated as **pcurses** ... and was re-issued as ncurses 1.8.1 in late 1993". ncurses is the most widely known implementation of curses, and has motivated further development of other variations, such as BSD curses in the NetBSD project.

## Portability

Although the ncurses library was initially developed under Linux, OpenBSD, FreeBSD, and NetBSD, it has been ported to many other ANSI/POSIX UNIX systems, mainly by Thomas Dickey. PDCurses, while not identical to ncurses, uses the same function calls and operates the same way as ncurses does except that PDCurses targets different devices, e.g., console windows for DOS, Win32, OS/2, as well as X11. Porting between the two is not difficult. For example, the roguelike game *ADOM* was written for Linux and ncurses, later ported to DOS and PDCurses.

## Screenshots

- (Color newsreader interface for tin) Color newsreader interface for tin
- (Curses used in JACK) Curses used in JACK

## Applications

Curses is designed to facilitate GUI-like functionality on a text-only device, such as a PC running in console mode, a hardware ANSI terminal, a Telnet or SSH client, or similar. Curses-based software is software whose user interface is implemented through the curses library, or a compatible library (such as ncurses).

Curses-based programs often have a user interface that resembles a traditional graphical user interface, including 'widgets' such as text boxes and scrollable lists, rather than the command line interface (CLI) most commonly found on text-only devices. This can make them more user-friendly than a CLI-based program, while still being able to run on text-only devices. Curses-based software can also have a lighter resource footprint and operate on a wider range of systems (both in terms of hardware and software) than their GUI-based counterparts. This includes old pre-1990 machines along with modern embedded systems using text-only displays.

Curses is most commonly associated with Unix-like operating systems, although implementations for Microsoft Windows also exist.

---
title: "GLib"
source: https://en.wikipedia.org/wiki/GLib
domain: gtk-toolkit
license: CC-BY-SA-4.0
tags: gtk toolkit, gobject type system, glib library, gnome widgets
fetched: 2026-07-02
---

# GLib

**GLib** is a bundle of three (formerly five) low-level system libraries written in C and developed mainly by GNOME. GLib's code was separated from GTK, so it can be used by software other than GNOME and has been developed in parallel ever since.

The name "GLib" originates from the project's start as a GTK C utility library.

## Features

GLib provides advanced data structures, such as memory chunks, doubly and singly linked lists, hash tables, dynamic strings and string utilities, such as a lexical scanner, string chunks (groups of strings), dynamic arrays, balanced binary trees, N-ary trees, quarks (a two-way association of a string and a unique integer identifier), keyed data lists, relations, and tuples. Caches provide memory management.

GLib implements functions that provide threads, thread programming and related facilities such as primitive variable access, mutexes, asynchronous queues, secure memory pools, message passing and logging, hook functions (callback registering) and timers. GLib also includes message passing facilities such as byte order conversion and I/O channels.

Some other features of GLib include:

- standard macros
- warnings and assertions
- dynamic loading of modules

### Components

The GLib package consisted of five libraries, but they were all merged into one library, since then named simply *GLib*, and are no longer sustained as standalone libraries. The original libraries were:

- GObject, an object system including the type system GType
- GLib
- GModule
- GThread
- GIO

Of these, three continue to reside in distinct subdirectories of the source tree, and so can be thought of as discrete components: GLib, GObject, and GIO. These can be thought of as a software stack: GObject relies on GLib, and GIO provides higher-level functionality that uses both.

### Programs for the GLib library

Command-line utilities associated with GLib, are usually packaged separately into libglib2.0-bin:

- `gapplication(1)` – for starting applications via D-Bus activation
- `gdbus(1)` – for working with D-Bus objects and monitoring the bus
- `gio(1)` – a file management utility that can work with GIO virtual filesystems
- `gresource(1)` – for extracting files from binary format (*.gresource)-files and executables
- `gsettings(1)` – for inspecting and editing application configuration
- `gio-query-modules(1)` – for updating caches used internally by GLib
- `glib-compile-schemas(1)` – for updating caches used internally by GLib

## History

GLib began as part of the GTK+ project, now named GTK. However, before releasing GTK+ version 2, the project's developers decided to separate code from GTK+ that was not for graphical user interfaces (GUIs), thus creating GLib as a separate software bundle. GLib was released as a separate library so other developers, those not using the GUI-related parts of GTK+, could use the non-GUI parts of the library without the overhead of depending on the full GUI library.

Since GLib is a cross-platform library, applications using it to interface with the operating system are usually portable across different operating systems without major changes.

### Releases

Glib is undergoing active development. For a current overview see https://gitlab.gnome.org/GNOME/glib/-/blob/main/NEWS. The table below documents major patch notes from 1998 to 2025.

| Release series | Initial release date | Major enhancements |
|---|---|---|
| GLib 1.x |   |   |
| 1.1 | 1998-09-12 |   |
| 1.2 | 1999-02-27 |   |
| 1.3 | 2001-09-25 |   |
| GLib 2.x |   |   |
| 2.0 | 2002-03-08 |   |
| 2.24 | 2010-03-26 | GVariant, GConverted |
| 2.26 | 2010-09-27 | GSettings, GDbus, GObject property bindings (GAtomic for refcounting) |
| 2.30 | 2011-09-26 | Non-unique GApplications, use `eventfd()` for mainloop wakeup, GHashTable set optimization, GObject data scalability |
| 2.32 | 2012-03-24 | Plans for GLib 2.32 |
| 2.34 | 2012-09-23 | What's New for Developers in GLib 2.34 |
| 2.36 | 2013-03-25 |   |
| 2.38 | 2013-09-23 | applications launched using D-Bus activation GSubprocess, Unicode 6.3 (released September 2013) |
| 2.40 | 2014-03-24 | GNotification, System notification API |
| 2.42 | 2014-09-22 |   |
| 2.43 | 2014-10-27 |   |
| 2.44 | 2015-03-23 |   |
| 2.45 | 2015-04-30 |   |
| 2.46 | 2015-09-21 |   |
| 2.47 | 2015-10-26 |   |
| 2.48 | 2016-03-22 |   |
| 2.50 | 2016-09-19 |   |
| 2.52 | 2017-03-19 |   |
| 2.53 | 2017-04-25 |   |
| 2.54 | 2018-01-08 |   |
| 2.55 | 2018-02-06 |   |
| 2.56 | 2018-03-12 |   |
| 2.57 | 2018-05-05 |   |
| 2.58 | 2018-08-30 |   |
| 2.59 | 2018-12-23 |   |
| 2.60 | 2019-03-04 |   |
| 2.61 | 2019-04-15 |   |
| 2.62 | 2019-09-05 |   |
| 2.63 | 2019-10-04 |   |
| 2.64 | 2020-02-27 |   |
| 2.65 | 2020-06-18 |   |
| 2.66 | 2020-09-10 |   |
| 2.67 | 2020-10-23 |   |
| 2.68 | 2021-03-18 |   |
| 2.69 | 2021-07-06 |   |
| 2.70 | 2021-09-17 |   |
| 2.71 | 2021-12-16 |   |
| 2.72 | 2022-03-17 |   |
| 2.73 | 2022-05-27 |   |
| 2.74 | 2022-09-17 |   |
| 2.75 | 2022-11-10 |   |
| 2.76 | 2023-03-10 |   |
| 2.77 | 2023-07-06 |   |
| 2.78 | 2023-09-08 |   |
| 2.79 | 2023-12-22 |   |
| 2.80 | 2024-03-07 |   |
| 2.81 | 2024-06-28 |   |
| 2.82 | 2024-08-26 |   |
| 2.83 | 2024-11-06 |   |
| 2.84 | 2025-03-06 |   |
| 2.85 | 2025-05-20 |   |
| 2.86 | 2025-09-05 |   |
| 2.87 | 2025-11-03 |   |
| 2.88 | 2026-03-16 |   |

## Similar projects

Other libraries provide low-level functions and implementations of data structures, including:

- Microsoft Foundation Class Library (MFC) – An object-oriented C++ wrapper library to the C-based Windows API which also includes some data structures and other convenience functionality
- Standard Template Library (STL) – C++ library for data structures and algorithms
- Boost – provides some functions for C++, such as threading primitives, similar to what GLib does for C
- QtCore – core API of the Qt Framework
- wxBase – non-GUI functions of the wxWidgets library
- The Apache Portable Runtime and Apple Core Foundation have a large functional overlap with GLib, and provide many similar OS-portable threading, network and data structure implementations in C.
- Gnulib - The GNU portability library

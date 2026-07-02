---
title: "FLTK"
source: https://en.wikipedia.org/wiki/FLTK
domain: fltk-toolkit
license: CC-BY-SA-4.0
tags: fltk toolkit, lightweight gui library, cross-platform widgets, opengl windowing
fetched: 2026-07-02
---

# FLTK

**Fast Light Toolkit** (**FLTK**) is a cross-platform widget (graphical control element) library for graphical user interfaces (GUIs), developed by Bill Spitzak and others. Made to accommodate 3D graphics programming, it has an interface to OpenGL, but it is also suitable for general GUI programming.

Using its own widget, drawing and event systems abstracted from the underlying system-dependent code, it allows for writing programs which look the same on all supported operating systems.

FLTK is free and open-source software, licensed under GNU Lesser General Public License (LGPL) with an added clause permitting static linking from applications with incompatible licenses.

In contrast to user interface libraries like GTK, Qt, and wxWidgets, FLTK uses a more lightweight design and restricts itself to GUI functionality. Because of this, the library is very small (the FLTK "Hello World" program is around 100 KiB), and is usually statically linked. It also avoids complex macros, separate code preprocessors, and use of some advanced C++ features: templates, exceptions, and run-time type information (RTTI) or, for FLTK 1.x, namespaces. Combined with the modest size of the package, this makes it relatively easy to learn for new users.

These advantages come with corresponding disadvantages. FLTK offers fewer widgets than most GUI toolkits and, because of its use of non-native widgets, does not have native look-and-feel on any platform.

## Meaning of the name

FLTK was originally designed to be compatible with the Forms Library written for Silicon Graphics (SGI) machines (a derivative of this library called *XForms* is still used quite often). In that library, all functions and structures start with `fl_`. This naming was extended to all new methods and widgets in the C++ library, and this prefix `FL` was taken as the name of the library. After FL was released as open source, it was discovered that searching "FL" on the Internet was a problem, because it is also the abbreviation for Florida. After much debating and searching for a new name for the toolkit, which was already in use by several people, Bill Spitzak came up with *Fast Light Tool Kit* (FLTK).

## Architecture

FLTK is an object-oriented widget toolkit written in the programming language C++. While GTK is mainly optimized for the X Window System, FLTK works on other platforms, including Microsoft Windows (interfaced with the Windows API), and OS X (interfaced with Quartz). A Wayland back-end has been implemented and is available since release 1.4.0. FLTK2 has gained experimental support for optionally using the cairo graphics library.

### Language bindings

A library written in one programming language may be used in another language if language bindings are written. FLTK has a range of bindings for various languages.

FLTK was mainly designed for, and is written in, the programming language C++. However, bindings exist for other languages, for example Lua, Perl, Python, Ruby, Rust and Tcl.

For FLTK 1.x, this example creates a window with an *Okay* button:

```mw
# include <FL/Fl.H>
# include <FL/Fl_Window.H>
# include <FL/Fl_Button.H>

int main(int argc, char *argv[]) {
   Fl_Window* w = new Fl_Window(330, 190);
   new Fl_Button(110, 130, 100, 35, "Okay");
   w->end();
   w->show(argc, argv);
   return Fl::run();
}
```

### GUI designers

FLTK includes *Fast Light User Interface Designer* (FLUID), a graphical GUI designer that generates C++ source and header files.

## Use

Many programs and projects use FLTK, including:

- Nanolinux, 14 MB Linux distribution
- XFDOS, a FreeDOS-based distribution with a GUI, porting Nano-X and FLTK
- Agenda VR3, a Linux-based personal digital assistant with software based on FLTK.
  - third-party **Agenda VR3** software
- Amnesia: The Dark Descent, by Frictional Games uses FLTK in its launcher application
- MwendanoWD, Logic puzzle for personal computer by YPH.
- Audio:
  - Fldigi, amateur radio software, allows data transmission and text chat via digital modes such as PSK31
  - Giada, looper, micro-sequencer, sample player software, open-source
  - Prodatum, synthesizer preset editor, uses a lifelike interface design
  - ZynAddSubFX, an open-source software synthesizer
- DiSTI GL Studio, human-machine interface development tool
- Engineering:
  - ForcePAD, an intuitive tool to visualise the behavior of structures subject to loading and boundary conditions
  - Gmsh, an open-source finite element mesh generator
  - RoboCIM, software to simulate and control operation of a servo robot system and external devices
- Equinox Desktop Environment (EDE)
- FlBurn optical disc burning software for Linux
- Graphics:
  - CinePaint, deep-paint software, migrating from GTK to FLTK, open-source
  - ITK-SNAP, software application for medical image segmentation, open-source
  - Nuke, a digital compositing program. Until version 5, now replaced by Qt
  - Open Movie Editor
  - OpenVSP, an open-source NASA parametric 3D CAD for aircraft design and analysing
  - PosteRazor, open-source poster printing software for Windows, OS X, Linux
  - Tilemap Studio, An open-source tilemap editor for Game Boy, Color, Advance, DS, and SNES projects
- SmallBASIC, Windows port
- Web browsers:
  - Dillo, Dillo-2 was based on FLTK-2, abandoning this FLTK branch, with no official release, was a major cause of Dillo-3 being started, using FLTK1.3
  - Fifth, replicates functioning of early Opera
  - NetRider
- Brain Visualizer: An open-source interactive visualizer for large-scale 3D brain models. Part of the Brain Organization Simulation System (BOSS) developed at Stony Brook University
- X window managers:
  - FLWM
  - miwm

## Versions

This version history is an example of the sometimes tumultuous nature of open-source development.

### 1.0.x

This is a prior stable version, now unmaintained.

### 1.1.x

This is a prior stable version, now unmaintained.

### 2.0 branch

This was a development branch, long thought to be the next step in FLTK's evolution, with many new features and a cleaner programming style. It never achieved stability, and development has largely ceased. The branch is inactive now.

### 1.2.x

This was an attempt to take some of the best features of 2.0 and merge them back into the more popular 1.1 branch. It is no longer developed. All of its features have been incorporated in branch 1.3.

### 1.3.x

Previous stable release. Provides UTF-8 support.

### 1.4.x

Current stable branch. Adds more features to 1.3. This branch is in maintenance mode since release 1.4.2 (Feb. 23, 2025).

### 1.5.x

Current development branch. This branch is in early development stage. Since FLTK 1.5 CMake is required to build FLTK (configure/Makefile support has been dropped).

### 3.0 branch

This branch resulted from a vision to "unfork" branches 1.x and 2.0, but it was never completed. All efforts to develop this branch have been abandoned. Now inactive.

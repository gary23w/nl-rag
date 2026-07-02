---
title: "freedesktop.org"
source: https://en.wikipedia.org/wiki/Freedesktop.org
domain: wayland-protocol
license: CC-BY-SA-4.0
tags: wayland protocol, wayland compositor, weston reference, display server
fetched: 2026-07-02
---

# freedesktop.org

**freedesktop.org** (**fd.o**), formerly **X Desktop Group** (**XDG**), is a project to work on interoperability and shared base technology for free-software desktop environments for the X Window System (X11) and Wayland on Linux and other Unix-like operating systems. Although freedesktop.org produces specifications for interoperability, it is not a formal standards body.

The project was founded by Havoc Pennington, a GNOME developer working for Red Hat in March 2000. Widely used open-source Desktop projects, such as GNOME, KDE's Plasma Desktop, and Xfce, are collaborating with the freedesktop.org project. In 2006, the project released Portland 1.0 (xdg-utils), a set of common interfaces for desktop environments. freedesktop.org joined the X.Org Foundation in 2019. Some of the project's servers are hosted by Portland State University.

## Hosted projects

freedesktop.org provides hosting for a number of relevant projects. These include:

### Windowing system and graphics

Software related to windowing systems and graphics in general

- Cairo, a vector graphics library with cross-device output support
- Direct Rendering Infrastructure (DRI), a Linux API to access the graphics hardware, used by X11, Wayland compositors, Mesa 3D, etc.
- Glamor, a 2D graphics common driver for X server on graphics chipsets which have support for OpenGL/EGL/GBM APIs
- Mesa 3D, an implementation of several graphics APIs such as Vulkan and OpenGL
- Pixman, a low-level software library for pixel manipulation, providing features such as image compositing and trapezoid rasterization; users include the cairo graphics library and the X.Org Server
- Poppler, a PDF rendering library
- Video Acceleration API
- Wayland, a protocol to replace X11; features: no tearing, lag, redrawing or flicker
- X.Org Server, the official reference implementation of the X11 protocol
- XCB, an Xlib replacement
- Xephyr, a display server
- wlroots, a modular Wayland compositor library

### Other

- D-Bus, a message bus akin to DCOP (KDE 3) and Bonobo (GNOME 2)
- Elektra, a library for reading and writing configuration
- FreeType, a text rendering library
- fontconfig, a library for font discovery, name substitution, etc.
- fprint, a library for consumer fingerprint reader devices
- Geoclue, a geoinformation service
- GNU GRUB, a boot loader package from the GNU Project
- GStreamer, a cross-platform multimedia framework
- GTK-Qt engine, a GTK+ 2 engine which uses Qt to draw the graphical control elements, providing the look and feel of KDE applications to GTK+2 applications
- HAL (Hardware Abstraction Layer), a consistent cross-operating system layer; deprecated and replaced by udev
- kmscon, a userspace virtual console to replace the Linux console; uses the KMS driver and supports Unicode
- luit, a tool used by terminal emulators
- libinput, a library to handle input devices in Wayland compositors and to provide a generic X.Org input driver. It provides device detection, device handling, input device event processing and abstraction to minimize the amount of custom input code compositors need to provide the common set of functionality that users expect.
- PulseAudio, a sound server frontend providing software mixing, network audio, and per application volume control
- PipeWire, a low-latency server for handling sandbox-friendly audio and video streams on Linux, which provides an implementation of PulseAudio, JACK, and ALSA as well as secure methods for screenshotting and screencasting on Wayland compositors
- Xft, anti-aliased fonts using the FreeType library, rather than the old X core fonts
- pkg-config, a helper program used to generate flags for compiler and linker to include necessary libraries

Also, Avahi (a free Zeroconf implementation) started as a fd.o project but has since become a separate project.

### Base Directory Specification

*XDG Base Directory Specification* (XDG BDS) introduces a range of variables where user-specific files used by programs should be found. Many tools and applications utilize these variables by default.

#### User directories

Besides the variables mentioned below, XDG BDS also specifies that users' local binary files may be installed into `$HOME/.local/bin`. Systems compliant with the spec are expected to make this directory available in their CLI's `PATH` environment variable.

**`XDG_DATA_HOME`**

For user application's own data files

Default to

$HOME/.local/share

**`XDG_CONFIG_HOME`**

For user's app configuration files

Default to

$HOME/.config

**`XDG_STATE_HOME`**

For user-specific app session data, which should be stored for future reuse

Default to

$HOME/.local/state

May include logs, recently used files, application-specific information (e.g. window layout, views, opened files, undo history, etc.), akin to session data that should be stored by app by request of system session manager, like

X session manager

**`XDG_CACHE_HOME`**

For user-specific app cache files

Default to

$HOME/.cache

**`XDG_RUNTIME_DIR`**

For user-specific app runtime files, like sockets, which must not survive reboot and full logout/login cycles

#### System directories

**`XDG_DATA_DIRS`**

Colon-separated list of preference-ordered paths to search for data files in

Default to

/usr/local/share/:/usr/share/

**`XDG_CONFIG_DIRS`**

The same as above but for config files

Default to

/etc/xdg/

## Stated aims

The project aims to catch interoperability issues much earlier in the process. It is not for legislating formal standards. Stated goals include:

- Collect existing specifications, standards, and documents related to X desktop interoperability and make them available in a central location.
- Promote the development of new specifications and standards to be shared among multiple X desktops.
- Integrate desktop-specific standards into broader standards efforts, such as Linux Standard Base and the ICCCM.
- Work on the implementation of these standards in specific X desktops.
- Serve as a neutral forum for sharing ideas about X desktop technology.
- Implement technologies that further X desktop interoperability and free X desktops in general.
- Promote X desktops and X desktop standards to application authors, both commercial and volunteer.
- Communicate with the developers of free operating system kernels, the X Window System itself, free OS distributions, and so on to address desktop-related problems.
- Provide source repositories (git and CVS), web hosting, Bugzilla, mailing lists, and other resources to free software projects that work toward the above goals.

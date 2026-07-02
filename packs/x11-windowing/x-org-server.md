---
title: "X.Org Server"
source: https://en.wikipedia.org/wiki/X.Org_Server
domain: x11-windowing
license: CC-BY-SA-4.0
tags: x window system, x.org server, window manager, display server
fetched: 2026-07-02
---

# X.Org Server

**X.Org Server** is the free and open-source implementation of the X Window System (X11) display server stewarded by the X.Org Foundation.

Implementations of the client-side X Window System protocol exist in the form of *X11 libraries*, which serve as helpful APIs for communicating with the X server. Two such major X libraries exist for X11. The first of these libraries was Xlib, the original C language X11 API, but another C language X library, XCB, was created later in 2001. Other smaller X libraries exist, both as interfaces for Xlib and XCB in other languages, and as smaller standalone X libraries.

The services with which the X.Org Foundation supports X Server include the packaging of the releases; certification (for a fee); evaluation of improvements to the code; developing the web site, and handling the distribution of monetary donations. The releases are coded, documented, and packaged by global developers.

## Software architecture

The X.Org Server implements the server side of the X Window System core protocol version 11 (X11) and extensions to it, e.g. RandR.

Version 1.16.0 integrates support for systemd-based launching and management which improved boot performance and reliability.

### Device Independent X (DIX)

The Device Independent X (DIX) is the part of the X.Org Server that interacts with clients and implements software rendering. The main loop and the event delivery are part of the DIX.

An X server has a tremendous amount of functionality that must be implemented to support the X core protocol. This includes code tables, glyph rasterization and caching, XLFDs, and the core rendering API which draws graphics primitives.

### Device Dependent X (DDX)

The Device Dependent X (DDX) is the part of the x-server that interacts with the hardware. In the X.Org Server source code, each directory under "hw" corresponds to one DDX. Hardware comprises graphics cards as well as mouse and keyboards. Each driver is hardware specific and implemented as a separate loadable module.

#### 2D graphics driver

For historical reasons the X.Org Server still contains graphics device drivers supporting some form of 2D rendering acceleration. In the past, mode-setting was done by an X-server graphics device driver specific to some video controller hardware (*e.g.*, a GPU). To this mode-setting functionality, additional support for 2D acceleration was added when such became available with various GPUs. The mode-setting functionality was moved into the DRM and is being exposed through a DRM mode-setting interface, the new approach being called "kernel mode-setting" (KMS). But the 2D rendering acceleration remained.

In Debian the 2D graphics drivers for the X.Org Server are packaged individually and called *xserver-xorg-video-**. After installation the 2D graphics driver-file is found under `/usr/lib/xorg/modules/drivers/`. The package xserver-xorg-video-nouveau installs `nouveau_drv.so` with a size of 215 KiB, the proprietary Nvidia GeForce driver installs an 8 MiB-sized file called `nvidia_drv.so` and Radeon Software installs `fglrx_drv.so` with a size of about 25MiB.

The available free and open-source graphics device drivers are being developed inside of the Mesa 3D-project. While these can be recompiled as required, the development of the proprietary DDX 2D graphics drivers is greatly eased when the X.Org Server keeps a stable API/ABI across multiple of its versions.

With version 1.17 a generic method for mode-setting was mainlined. The `xf86-video-modesetting` package, the Debian-package being called `xserver-xorg-video-modesetting`, was retired, and the generic modesetting DDX it contained was moved into the server package to become the KMS-enabled default DDX, supporting the vast majority of AMD, Intel and NVidia GPUs.

On April 7, 2016, AMD employee Michel Dänzer released `xf86-video-ati` version 7.7.0 and `xf86-video-amdgpu` version 1.1.0, the latter including support for their Polaris microarchitecture.

##### Acceleration architectures

There are (at least) XAA (XFree86 Acceleration Architecture), EXA, UXA and SNA.

XAA

is an API between the Device-Independent-X (DIX) and the Device-Dependent-X (DDX), a 2D graphics driver, here e.g. with the

Linux kernel

.

In the X Window System, **XFree86 Acceleration Architecture** (**XAA**) is a driver architecture to make a video card's 2D hardware acceleration available to the X server. It was written by Harm Hanemaayer in 1996 and first released in XFree86 version 3.3. It was completely rewritten for XFree86 4.0. It was removed again from X.Org Server 1.13.

Most drivers implement acceleration using the XAA module. XAA is on by default, though acceleration of individual functions can be switched off as needed in the server configuration file (`XF86Config` or `xorg.conf`).

The driver for the ARK chipset was the original development platform for XAA.

In X.Org Server release 6.9/7.0, EXA was released as a replacement for XAA, as XAA supplies almost no speed advantage for current video cards. EXA is regarded as an intermediate step to converting the entire X server to using OpenGL.

##### Glamor

Glamor is a generic, hardware independent, 2D acceleration driver for the X server that translates the X render primitives into OpenGL operations, taking advantage of any existing 3D OpenGL drivers. In this way, it is functionally similar to Quartz Extreme and QuartzGL (2D performance acceleration) for Apple Quartz Compositor.

The ultimate goal of GLAMOR is to obsolete and replace all the DDX 2D graphics device drivers and acceleration architectures, thereby avoiding the need to write X 2D specific drivers for every supported graphic chipset. Glamor requires a 3D driver with support for shaders.

Glamor performance tuning was accepted for Google Summer of Code 2014. Glamor supports Xephyr and DRI3, and can boost some operations by 700–800%. Since its mainlining into version 1.16 of the X.Org Server, development on Glamor was continued and patches for the 1.17 release were published.

##### Virtualization

There is a distinct and special DDX for instances of the X.Org Server which run on a guest system inside of a virtualized environment: xf86-video-qxl, a driver for the "QXL video device". SPICE makes use of this driver though it works without it as well.

In the Debian repositories it is called xserver-xorg-video-qxl.

#### Input stack

Under Debian, drivers related to input are found under `/usr/lib/xorg/modules/input/`. Such drivers are named e.g. `evdev_drv.so`, `mouse_drv.so`, `synaptics_drv.so` or `wacom_drv.so`.

With version 1.16, the X.Org Server obtained support for the libinput library in form of a wrapper called `xf86-input-libinput`. At the XDC 2015 in Toronto, libratbag was introduced as a generic library to support configurable mice. `xserver-xorg-input-joystick` is the input module for the X.Org server to handle classic joysticks and gamepads, which is not meant for playing games under X, but to control the cursor with a joystick or gamepad.

#### Other DDX components

**XWayland**

XWayland is a series of patches over the X.Org server codebase that implement an X server running upon the

Wayland

protocol. The patches are developed and maintained by the Wayland developers for compatibility with X11 applications during the transition to Wayland,

and were mainlined in version 1.16 of the X.Org Server in 2014.

When a user runs an X application from within

Weston

, it calls upon XWayland to service the request.

**XQuartz**

XQuartz is a series of patches from

Apple Inc.

to integrate support for the X11 protocol into their

Quartz Compositor

, in a similar way to how XWayland integrates X11 into

Wayland compositors

.

**Xspice**

Xspice is a device driver for the X.Org Server. It supports the QXL framebuffer device and includes a wrapper script

which makes it possible to launch an X.Org Server whose display is exported via the

SPICE

protocol. This enables use of SPICE in a remote desktop environment, without requiring

KVM

virtualization.

**Xephyr**

Xephyr

is an X-on-X implementation. Since version 1.16.0, Xephyr serves as the primary development environment for the new 2D acceleration subsystem (Glamor), permitting rapid development and testing on a single machine.

**RandR**

RandR

(

resize and rotate

) is a

communications protocol

written as an extension to the

X11

protocol. XRandR provides the ability to resize, rotate and reflect the

root window

of a screen. RandR is responsible for setting the screen refresh rate.

It allows for the control of multiple monitors.

### IPC

The X.Org Server, and any x-client, each run as distinct processes. On Unix/Linux, a process knows nothing about any other processes. For it to communicate with another process, it is completely and utterly reliant on the kernel to moderate the communication via available inter-process communication (IPC) mechanisms. Unix domain sockets are used to communicate with processes running on the same machine. Special socket function calls are part of the System Call Interface. Although Internet domain sockets can be used locally, Unix domain sockets are more efficient, since they do not have the protocol overhead (checksums, byte orders, etc.).

X.Org Server does not use D-Bus.

Sockets are the most common interprocess communication (IPC) method between the processes of the X server and its various X clients. It provides the Application Programming Interface (API) for communication in the TCP/IP domain and also locally only in the UNIX domain. There are several other APIs described in the X Transport Interface, for instance TLI (Transport Layer Interface). Other options for IPC between for the X client-server, require X Window system extensions, for instance the MIT Shared Memory Extension (MIT-SHM).

### Multiseat configuration

Multi-seat refers to an assembly of a single computer with multiple "seats", allowing multiple users to sit down at the computer, log in, and use the computer at the same time independently. The computer has multiple keyboards, mice, and monitors attached to it, each "seat" having one keyboard, one mouse and one monitor assigned to it. A "seat" consists of all hardware devices assigned to a specific workplace. It consists of at least one graphics device (graphics card or just an output and the attached monitor) and a keyboard and a mouse. It can also include video cameras, sound cards and more.

Due to limitation of the VT system in the Linux kernel and of the X core protocol (in particular, how X defines the relation between the root window and an output of the graphics card), multi-seat does not work out-of-the-box for the usual Linux distribution but necessitates a special configuration.

There are these methods to configure a multi-seat assembly:

- multiple Xephyr servers over a host xorg-server
- multiple instances of an xorg-server
  - one graphics card per seat
  - a single graphics card for all seats

The utilized command-line options of the xorg-server are:

- `-isolateDevice bus-id` Restrict device resets (output) to the device at bus-id. The bus-id string has the form bustype:bus:device:function (e.g., 'PCI:1:0:0'). At present, only isolation of PCI devices is supported; i.e., this option is ignored if bustype is anything other than 'PCI'.
- `vtXX` the default for e.g. Debian 9 Stretch is 7, i.e. by pressing Ctrl+Alt+F7 the user can switch to the VT running the xorg-server.

Only the user on the first monitor has the use of vt consoles and can use Ctrl+Alt+Fx to select them. The other users have a GDM login screen and can use xorg-server normally, but have no vt's.

Even though a single user can utilize multiple monitors connected to the different ports of a single graphics card (cf. RandR), the method which is based on multiple instances of the xorg-server seems to require multiple PCI graphics cards.

It is possible to configure multi-seat employing only one graphics card, but due to limitations of the X protocol this necessitates the usage of X Display Manager Control Protocol XDMCP.

There is also Xdmx (Distributed Multihead X).

## Adoption

**Unix and Linux**

The X.Org Server runs on many free-software

Unix-like

operating systems, including being adopted for use by most

Linux distributions

and

BSD

variants. It is also the X server for the

Solaris

operating system. X.Org is also available in the repositories of

Minix 3

.

**Windows**

Cygwin/X

,

Cygwin

's implementation of the X server for

Microsoft Windows

, uses the X.Org Server, as do VcXsrv

(

Visual C++

X-server

) and

Xming

. SSH clients such as

PuTTY

allow launching of X applications through X11 forwarding on the condition that it is enabled on both the server and client.

**OS X / macOS**

OS X

versions prior to

Mac OS X Leopard

(10.5) shipped with an XFree86-based server, but 10.5's X server adopted the X.Org codebase.

Starting with

OS X Mountain Lion

, (10.8) X11 is not bundled in OS X; instead, it has to be installed from, for example, the open source

XQuartz

project.

As of version 2.7.4, X11.app/XQuartz does not expose support for high-resolution

Retina displays

to X11 apps, which run in pixel-doubled mode on high-resolution displays.

**OpenVMS**

Current versions of the DECwindows X11 server for

OpenVMS

are based on X.org Server.

## History

A display server, such as X.Org Server, implements the

windowing system

and serves its clients.

The modern X.Org Foundation came into being in 2004 when the body that oversaw X standards and published the official reference implementation joined forces with former XFree86 developers. X11R6.7.0, the first version of the X.Org Server, was forked from XFree86 4.4 RC2. The immediate reason for the fork was a disagreement with the new license for the final release version of XFree86 4.4, but several disagreements among the contributors surfaced prior to the split. Many of the previous XFree86 developers have joined the X.Org Server project.

In 2005, a great effort was put in the modularization of the X.Org server source code, resulting in a dual release by the end of the year. The X11R7.0.0 release added a new modular build system based on the GNU Autotools, while X11R6.9.0 kept the old imake build system, both releases sharing the same codebase. Since then the X11R6.9 branch is maintained frozen and all the ongoing development is done to the modular branch. The new build system also brought the use of dlloader standard dynamic linker to load plugins and drivers, deprecating the old own method. As a consequence of the modularization, the X11 binaries were moving out of their own `/usr/X11R6` subdirectory tree and into the global `/usr` tree on many Unix systems.

In June 2006, another effort was done to move the X.Org server source codebase from CVS to git. Both efforts had the long-term goal of bringing new developers to the project. In the words of Alan Coopersmith:

> Some of our efforts here have been technological – one of the driving efforts of the conversions from Imake to automake and from CVS to git was to make use of tools developers would already be familiar and productive with from other projects. The Modularization project, which broke up X.Org from one giant tree into over 200 small ones, had the goal of making it possible to fix a bug in a single library or driver without having to download and build many megabytes of software & fonts that were not being changed.

In the 7.1 release, the KDrive framework (a small implementation of X written by Keith Packard, which was not based on XFree86 that X.Org developers used as a testing ground for new ideas, such as EXA) was integrated into the main codebase of X.Org server.

In 2008, the new DRI2, based on the kernel mode-setting (KMS) driver, replaced DRI. This change also set a major milestone in the X.Org server architecture, as the drivers were moved out from the server and user space (UMS) to the kernel space.

In 2013, the initial versions of DRI3 and Present extensions were written and coded by Keith Packard to provide a faster and tearing-free 2D rendering. By the end of the year the implementation of GLX was rewritten by Adam Jackson at Red Hat.

In June 2025, a fork of X.Org Server called XLibre was released.

### Releases

| Version | Date | X11 Release | Main features |
|---|---|---|---|
| Unsupported: 1.0 | 21 December 2005 | X11R7.0 (1.0.1) | Initial modularized X server, EXA architecture |
| Unsupported: 1.1 | 22 May 2006 | X11R7.1 (1.1.0) | KDrive integration, AIGLX support |
| Unsupported: 1.2 | 22 January 2007 | X11R7.2 (1.2.0) | Autoconfiguration, enhanced support for GL-based compositing managers |
| Unsupported: 1.3 | 19 April 2007 |   | RandR 1.2 |
| Unsupported: 1.4 | 6 September 2007 | X11R7.3 (1.4.0) | Input hotplugging support |
| Unsupported: 1.5 | 3 September 2008 | X11R7.4 (1.5.1) | MPX |
| Unsupported: 1.6 | 25 February 2009 |   | RandR 1.3, DRI2, XInput 1.5 |
| Unsupported: 1.7 | 1 October 2009 | X11R7.5 (1.7.1) | XInput 2.0, multi-pointer X |
| Unsupported: 1.8 | 2 April 2010 |   | xorg.conf.d, udev input handling |
| Unsupported: 1.9 | 20 August 2010 | X11R7.6 (1.9.3) |   |
| Unsupported: 1.10 | 25 February 2011 |   | X Synchronization Fences |
| Unsupported: 1.11 | 26 August 2011 |   |   |
| Unsupported: 1.12 | 4 March 2012 | X11R7.7 (1.12.2) | XInput 2.2 (including multi-touch support) |
| Unsupported: 1.13 | 5 September 2012 |   | New DDX driver API, DRI2 offload, RandR 1.4, OpenGL 3.x+ contexts, removing XAA |
| Unsupported: 1.14 | 5 March 2013 |   | XInput 2.3 |
| Unsupported: 1.15 | 27 December 2013 |   | DRI3 and Present extensions |
| Unsupported: 1.16 | 17 July 2014 |   | XWayland DDX, GLAMOR acceleration, non-PCI devices support, systemd-logind support (rootless X), obtained support for the libinput library in form of a wrapper called `xf86-input-libinput` |
| Unsupported: 1.17 | 4 February 2015 |   | Integration of the former `xf86-video-modesetting` generic DRM/KMS driver, added support for DRI2 with GLAMOR |
| Unsupported: 1.18 | 9 November 2015 |   | RandR 1.5 |
| Unsupported: 1.19 | 15 November 2016 |   | Threaded Input, PRIME synchronization, XWayland pointer confinement and warping, Windows DRI extension support |
| Unsupported: 1.20 | 10 May 2018 |   | Meson build system improvements, GLXVND allows for distinct OpenGL drivers for different X screens, RandR leasing improves Steam VR support |
| Latest version: 21.1 | 27 October 2021 |   | Meson build system now on par with Autotools, Variable refresh rate support, touchpad gestures via XInput 2.4 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

---
title: "Wayland (protocol)"
source: https://en.wikipedia.org/wiki/Wayland_(protocol)
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
---

# Wayland (protocol)

**Wayland** is a communication protocol that specifies the communication between a display server and its clients, as well as a C library implementation of that protocol. A display server using the Wayland protocol is called a *Wayland compositor*, because it additionally performs the task of a compositing window manager.

Wayland is developed by a group of volunteers initially led by Kristian Høgsberg as a free and open-source community-driven project with the aim of replacing the X Window System with a secure and simpler windowing system for Linux and other Unix-like operating systems. The project's source code is published under the terms of the MIT License, a permissive free software license. The Wayland project also develops an implementation of a Wayland compositor called *Weston*.

## Overview

1. The evdev module of the Linux kernel gets an event and sends it to the Wayland compositor.
2. The Wayland compositor looks through its scenegraph to determine which window should receive the event. The scenegraph corresponds to what is on screen and the Wayland compositor understands the transformations that it may have applied to the elements in the scenegraph. Thus, the Wayland compositor can pick the right window and transform the screen coordinates to window local coordinates, by applying the inverse transformations. The types of transformation that can be applied to a window are only restricted to what the compositor can do, as long as it can compute the inverse transformation for the input events.
3. As in the X case, when the client receives the event, it updates the UI in response. But in the Wayland case, the rendering happens by the client via EGL, and the client just sends a request to the compositor to indicate the region that was updated.
4. The Wayland compositor collects damage requests from its clients and then re-composites the screen. The compositor can then directly issue an ioctl to schedule a pageflip with KMS.

The Wayland Display Server project was created by Red Hat developer Kristian Høgsberg in 2008.

Beginning around 2010, Linux desktop graphics have moved from having "a pile of rendering interfaces... all talking to the X server, which is at the center of the universe" towards putting the Linux kernel and its components (i.e. Direct Rendering Infrastructure (DRI), Direct Rendering Manager (DRM)) "in the middle", with "window systems like X and Wayland ... off in the corner". This will be "a much-simplified graphics system offering more flexibility and better performance".

Høgsberg could have added an extension to X as many recent projects have done, but preferred to "[push] X out of the hotpath between clients and the hardware" for reasons explained in the project's FAQ:

> What's different now is that a lot of infrastructure has moved from the X server into the kernel (memory management, command scheduling, mode setting) or libraries (cairo, pixman, freetype, fontconfig, pango, etc.), and there is very little left that has to happen in a central server process. ... [An X server has] a tremendous amount of functionality that you must support to claim to speak the X protocol, yet nobody will ever use this. ... This includes code tables, glyph rasterization and caching, XLFDs (seriously, XLFDs!), and the entire core rendering API that lets you draw stippled lines, polygons, wide arcs and many more state-of-the-1980s style graphics primitives. For many things we've been able to keep the X.org server modern by adding extension such as XRandR, XRender and COMPOSITE ... With Wayland we can move the X server and all its legacy technology to an optional code path. Getting to a point where the X server is a compatibility option instead of the core rendering system will take a while, but we'll never get there if [we] don't plan for it.

The Wayland protocol is represented through a .xml file which comes with the Wayland compiler, which can compile the wayland.xml file into relevant C libraries for applications and compositor implementations to use. The official reference implementation for a Wayland compositor is named Weston. The project is also developing versions of GTK and Qt that render to Wayland instead of to X. Most applications are expected to gain support for Wayland through one of these libraries without modification to the application.

Initial versions of Wayland have not provided network transparency, though Høgsberg noted in 2010 that network transparency is possible. It was attempted as a Google Summer of Code project in 2011, but was not successful. Adam Jackson has envisioned providing remote access to a Wayland application by either "pixel-scraping" (like VNC) or getting it to send a "rendering command stream" across the network (as in RDP, SPICE or X11). As of early 2013, Høgsberg was experimenting with network transparency using a proxy Wayland server which sends compressed images to the real compositor. In August 2017, GNOME saw the first such pixel-scraping VNC server implementation under Wayland. In modern Wayland compositors, network transparency is handled in an xdg-desktop-portal implementation that implements the RemoteDesktop portal.

Many Wayland compositors also include an xdg-desktop-portal implementation for common tasks such as a native file picker for native applications and sandboxes such as Flatpak (xdg-desktop-portal-gtk is commonly used as a fallback filepicker), screen recording, network transparency, screenshots, color picking, and other tasks that could be seen as needing user intervention and being security risks otherwise. Note that xdg-desktop-portal is not Flatpak or Wayland-specific, and can be used with alternative packaging systems and windowing systems.

## Software architecture

### Protocol architecture

In the Wayland protocol architecture, a client and a compositor communicate through the Wayland protocol using the reference implementation libraries.

The Wayland protocol follows a client–server model in which clients are the graphical applications requesting the display of pixel buffers on the screen, and the server (compositor) is the service provider controlling the display of these buffers.

The Wayland reference implementation has been designed as a two-layer protocol:

- A low-level layer or *wire protocol* that handles the inter-process communication between the two involved processes‍—‌client and compositor‍—‌and the marshalling of the data that they interchange. This layer is message-based and usually implemented using the kernel IPC services, specifically Unix domain sockets in the case of Linux and other Unix-like operating systems.
- A high-level layer built upon it, that handles the information that client and compositor need to exchange to implement the basic features of a window system. This layer is implemented as "an asynchronous object-oriented protocol".

While the low-level layer was written manually in C, the high-level layer is automatically generated from a description of the elements of the protocol stored in XML format. Every time the protocol description in this XML file changes, the C source code that implements the protocol can be regenerated to include the new changes, allowing a very flexible, extensible and error-proof protocol.

The reference implementation of Wayland protocol is split in two libraries: a library to be used by Wayland clients called `libwayland-client` and a library to be used by Wayland compositors called `libwayland-server`.

### Protocol overview

The Wayland protocol is described as an "asynchronous object-oriented protocol". *Object-oriented* means that the services offered by the compositor are presented as a series of *objects* living on the same compositor. Each object implements an *interface* which has a name, a number of methods (called *requests*) as well as several associated *events*. Every request and event has zero or more arguments, each one with a name and a data type. The protocol is *asynchronous* in the sense that requests do not have to wait for synchronized replies or ACKs, avoiding round-trip delay time and achieving improved performance.

The Wayland clients can make a request (a method invocation) on some object if the object's interface supports that request. The client must also supply the required data for the arguments of such request. This is the way the clients request services from the compositor. The compositor in turn sends information back to the client by causing the object to emit events (probably with arguments too). These events can be emitted by the compositor as a response to a certain request, or asynchronously, subject to the occurrence of internal events (such as one from an input device) or state changes. The error conditions are also signaled as events by the compositor.

For a client to be able to make a request to an object, it first needs to tell the server the ID number it will use to identify that object. There are two types of objects in the compositor: global objects and non-global objects. Global objects are advertised by the compositor to the clients when they are created (and also when they are destroyed), while non-global objects are usually created by other objects that already exist as part of their functionality.

The interfaces and their requests and events are the core elements that define the Wayland protocol. Each version of the protocol includes a set of interfaces, along with their requests and events, which are expected to be in any Wayland compositor. Optionally, a Wayland compositor may define and implement its own interfaces that support new requests and events, thereby extending functionality beyond the core protocol. To facilitate changes to the protocol, each interface contains a "version number" attribute in addition to its name; this attribute allows for distinguishing variants of the same interface. Each Wayland compositor exposes not only what interfaces are available, but also the supported versions of those interfaces.

#### Wayland core interfaces

The interfaces of the current version of Wayland protocol are defined in the file protocol/wayland.xml of the Wayland source code. This is an XML file that lists the existing interfaces in the current version, along with their requests, events and other attributes. This set of interfaces is the minimum required to be implemented by any Wayland compositor.

Some of the most basic interfaces of the Wayland protocol are:

**wl_display**

the core global object, a special object to encapsulate the Wayland protocol itself

**wl_registry**

the global registry object, in which the compositor registers all the global objects that it wants to be available to all clients

**wl_compositor**

an object that represents the compositor, and is in charge of combining the different surfaces into one output

**wl_surface**

an object representing a rectangular area on the screen, defined by a location, size and pixel content

**wl_buffer**

an object that, when attached to a

wl_surface

object, provides its displayable content

**wl_output**

an object representing the displayable area of a screen

**wl_pointer, wl_keyboard, wl_touch**

objects representing different input devices like

pointers

or

keyboards

**wl_seat**

an object representing a seat (a set of input/output devices) in

multiseat configurations

A typical Wayland client session starts by opening a connection to the compositor using the wl_display object. This is a special local object that represents the connection and does not live within the server. By using its interface the client can request the wl_registry global object from the compositor, where all the global object names live, and bind those that the client is interested in. Usually the client binds at least a wl_compositor object from where it will request one or more wl_surface objects to show the application output on the display.

#### Wayland extension interfaces

A Wayland compositor can define and export its own additional interfaces. This feature is used to extend the protocol beyond the basic functionality provided by the core interfaces, and has become the standard way to implement Wayland protocol extensions. Certain compositors can choose to add custom interfaces to provide specialized or unique features. The Wayland reference compositor, Weston, used them to implement new experimental interfaces as a testbed for new concepts and ideas, some of which later became part of the core protocol (such as wl_subsurface interface added in Wayland 1.4).

### Extension protocols to the core protocol

#### XDG-Shell protocol

XDG-Shell protocol (see freedesktop.org for XDG) is an extended way to manage surfaces under Wayland compositors (not only Weston). The traditional way to manipulate (maximize, minimize, fullscreen, etc.) surfaces is to use the `wl_shell_*()` functions, which are part of the core Wayland protocol and live in libwayland-client, however are now deprecated. An implementation of the xdg-shell protocol, on the contrary, is supposed to be provided by the Wayland compositor. So you will find the <xdg-shell-client-protocol.h> header in the Weston source tree.

xdg_shell is a protocol aimed to substitute wl_shell in the long term, but will not be part of the Wayland core protocol. It starts as a non-stable API, aimed to be used as a development place at first, and once features are defined as required by several desktop shells, it can be finally made stable. It provides mainly two new interfaces: xdg_surface and xdg_popup. The xdg_surface interface implements a desktop-style window that can be moved, resized, maximized, etc.; it provides a request for creating child/parent relationship. The xdg_popup interface implements a desktop-style popup/menu; an xdg_popup is always transient for another surface, and also has implicit grab.

#### IVI-Shell protocol

IVI-Shell is an extension to the Wayland core protocol, targeting in-vehicle infotainment (IVI) devices.

### Rendering model

Wayland compositor

and its clients use

EGL

to draw directly into the

framebuffer

;

X.Org Server

with

XWayland

and

Glamor

.

The Wayland protocol does not include a rendering API. Instead, Wayland follows a *direct rendering* model, in which the client must render the window contents to a buffer shareable with the compositor. For that purpose, the client can choose to do all the rendering by itself, use a rendering library like Cairo or OpenGL, or rely on the rendering engine of high-level widget libraries with Wayland support, such as Qt or GTK. The client can also optionally use other specialized libraries to perform specific tasks, such as Freetype for font rendering.

The resulting buffer with the rendered window contents are stored in a wl_buffer object. The internal type of this object is implementation dependent. The only requirement is that the content data must be shareable between the client and the compositor. If the client uses a software (CPU) renderer and the result is stored in the system memory, then client and compositor can use shared memory to implement the buffer communication without extra copies. The Wayland protocol already natively provides this kind of shared memory buffer through the wl_shm and wl_shm_pool interfaces. The drawback of this method is that the compositor may need to do additional work (usually to copy the shared data to the GPU) to display it, which leads to slower graphics performance.

The most typical case is for the client to render directly into a video memory buffer using a hardware (GPU) accelerated API such as OpenGL, OpenGL ES or Vulkan. Client and compositor can share this GPU-space buffer using a special handler to reference it. This method allows the compositor to avoid the extra data copy through itself of the main memory buffer client-to-compositor-to-GPU method, resulting in faster graphics performance, and is therefore the preferred one. The compositor can further optimize the composition of the final scene to be shown on the display by using the same hardware acceleration API as an API client.

When rendering is completed in a shared buffer, the Wayland client should instruct the compositor to present the rendered contents of the buffer on the display. For this purpose, the client binds the buffer object that stores the rendered contents to the surface object, and sends a "commit" request to the surface, transferring the effective control of the buffer to the compositor. Then the client waits for the compositor to release the buffer (signaled by an event) if it wants to reuse the buffer to render another frame, or it can use another buffer to render the new frame, and, when the rendering is finished, bind this new buffer to the surface and commit its contents. The procedure used for rendering, including the number of buffers involved and their management, is entirely under the client control.

## Comparison with other window systems

### Differences between Wayland and X

There are several differences between Wayland and X with regard to performance, code maintainability, and security:

**Architecture**

The

composition manager

is a separate, additional feature in X, while Wayland merges display server and compositor as a single function.

Also, it incorporates some of the tasks of the

window manager

, which in X is a separate client-side process.

**Compositing**

Compositing is optional in X, but mandatory in Wayland. Compositing in X is "active"; that is, the compositor must fetch all pixel data, which introduces latency. In Wayland, compositing is "passive", which means the compositor receives pixel data directly from clients.

**Rendering**

The X server itself is able to perform rendering, although it can also be instructed to display a rendered window sent by a client. In contrast, Wayland does not expose any API for rendering, but delegates to clients such tasks (including the rendering of fonts, widgets, etc.).

Window decorations are to be rendered on the client side (e.g., by a graphics toolkit), or on the server side (by the compositor) with the opt-in

xdg-decoration

protocol, if the compositor chooses to implement such functionality.

**Security**

Wayland isolates the input and output of every window, achieving

confidentiality, integrity and availability

for both. The original X design lacked these important security features,

although some extensions have been developed trying to mitigate it.

Also, with the vast majority of the code running in the client, less code needs to run with

root

privileges, improving security,

although multiple popular Linux distributions now allow the X server to be run without root privileges.

**Networking**

The X Window System is an

architecture

that was designed at its core to run over a network. Wayland does not offer network transparency by itself;

however, a compositor can implement any

remote desktop protocol

to achieve remote display. In addition, there is research into Wayland image streaming and compression that would provide remote frame buffer access similar to that of

VNC

.

### Compatibility with X

XWayland is an X Server running as a Wayland client, and thus is capable of displaying native X11 client applications in a Wayland compositor environment. This is similar to the way XQuartz runs X applications in macOS's native windowing system. The goal of XWayland is to facilitate the transition from X Window System to Wayland environments, providing a way to run unported applications in the meantime. XWayland was mainlined into X.Org Server version 1.16.

Widget toolkits such as Qt 5 and GTK 3 can switch their graphical back-end at run time, allowing users to choose at load time whether they want to run the application over X or over Wayland. Qt 5 provides the `-platform` command-line option to that effect, whereas GTK 3 lets users select the desired GDK back-end by setting the `GDK_BACKEND` Unix environment variable.

## Wayland compositors

Display servers that implement the Wayland display server protocol are also called *Wayland compositors* because they additionally perform the task of a compositing window manager.

A library called **wlroots** is a modular Wayland implementation that functions as a base for several compositors.

Some notable Wayland compositors are:

- Weston – an implementation from the Wayland development team. For details about Weston see below.
- Enlightenment had Wayland support since version 0.20
- KWin - the default Wayland compositor of KDE Plasma has defaulted to Wayland since KDE Plasma 6.0. In Plasma 6.4, KWin's X11 session support was split off into a separate code base. In Plasma 6.8, KWin-X11 will no longer be supported by KDE.
- Mutter, the default Wayland compositor of GNOME disabled the X11 session at compile time in GNOME 49. Mutter's X11 session code was removed in GNOME 50.
- labwc is a wlroots-based stacking Wayland compositor inspired by Openbox. It is meant as a simple compositor without animations for systems that may not be powerful enough to run compositors with desktop animations and effects. It is used as the default compositor of Raspberry Pi OS.
- Sway – a tiling Wayland compositor, based on wlroots; it is a drop-in replacement for the i3 X11 window manager.
- Hyprland – a tiling Wayland compositor written in C++. Noteworthy features of Hyprland include dynamic tiling, tabbed windows, and a custom renderer that provides window animations, rounded corners, and Dual-Kawase Blur on transparent windows.
- Woodland – wlroots-based window-stacking compositor for Wayland written in C, inspired by TinyWL and focused on simplicity and stability.
- niri – a scrollable-tiling Wayland compositor written in Rust.
- Wayfire is a wlroots-based stacking Wayland compositor with desktop animations and effects inspired by Compiz.
- Phoc, a Wayland compositor for mobile devices like the PinePhone using the wlroots library. It is often used with the Phosh mobile shell.
- River – a wlroots-based compositor written in Zig. It provides its own protocol for window management; it does not do window management on its own.
- xfwl4 - a planned drop in replacement for Xfce's xfwm, written in Rust.

### Weston

Weston is a Wayland compositor previously developed as the reference implementation of the protocol by the Wayland project. It is written in C and released under the MIT License.

Weston officially supports only Linux due to dependencies on kernel-specific features such as kernel mode-setting (KMS), the Graphics Execution Manager (GEM), and udev. On Linux, it handles input via evdev and buffer management via Generic Buffer Management (GBM). A prototype port for FreeBSD was announced in 2013.

The compositor supports High-bandwidth Digital Content Protection (HDCP) and uses GEM to share buffers between applications and the compositor. It features a plug-in architecture with "shells" that provide elements like docks and panels. Applications are responsible for rendering their own window decorations.

Weston supports rendering via OpenGL ES or the pixman library for software rendering. The full OpenGL stack is avoided to prevent pulling in GLX and other X Window System dependencies.

A remote desktop interface for Weston was proposed in 2013 by a developer from RealVNC.

#### Maynard

***Maynard*** is a graphical shell and has been written as a plug-in for Weston, just as the GNOME Shell has been written as a plug-in to Mutter.

Raspberry Pi Holdings in collaboration with Collabora released Maynard.

### libinput

The Weston code for handling input devices (keyboards, pointers, touch screens, etc.) was split into its own separate library, called *libinput*, for which support was first merged in Weston 1.5.

Libinput handles input devices for multiple Wayland compositors and also provides a generic X.Org Server input driver. It aims to provide one implementation for multiple Wayland compositors with a common way to handle input events while minimizing the amount of custom input code compositors need to include. libinput provides device detection (via udev), device handling, input device event processing and abstraction.

Version 1.0 of libinput followed version 0.21, and included support for tablets, button sets and touchpad gestures. This version will maintain stable API/ABI.

As GNOME/GTK and KDE Frameworks 5 have mainlined the required changes, Fedora 22 will replace X.Org's evdev and Synaptics drivers with libinput.

With version 1.16, the X.Org Server obtained support for the libinput library in form of a wrapper called xf86-input-libinput.

### Wayland Security Module

Wayland Security Module is a proposition that resembles the Linux Security Module interface found in the Linux kernel.

Some applications (especially the ones related to accessibility) require privileged capabilities that should work across different Wayland compositors. Currently, applications under Wayland are generally unable to perform any sensitive tasks such as taking screenshots or injecting input events without going through xdg-desktop-portal or obtaining privileged access to the system. The security model forced by Wayland also creates mouse position problems when attempting to type text in many games.

Wayland Security Module is a way to delegate security decisions within the compositor to a centralized security decision engine.

## Adoption

The Wayland protocol is designed to be simple so that additional protocols and interfaces need to be defined and implemented to achieve a holistic windowing system. While many graphical toolkits already fully support Wayland, the developers of the graphical shells are cooperating with the Wayland developers to create the necessary additional interfaces.

### Desktop Linux distributions

Most major Linux distributions default to using Wayland. Some notable examples are:

- Debian ships Wayland as the default session for GNOME since version 10 (Buster), released 6 July 2019.
- Fedora starting with version 25 (released 22 November 2016) uses Wayland for the GNOME Workstation Edition desktop session, with X.Org as a fallback if the graphics driver cannot support Wayland. Fedora uses Wayland as the default for the KDE Plasma Edition session starting with version 34 (released 27 April 2021). Both of these Fedora Editions dropped their X.Org Sessions by default in Fedora 41 (released 29 October 2024).
- Manjaro ships Wayland as default in the GNOME edition of Manjaro 20.2 (Nibia) (released 22 November 2020).
- Raspberry Pi OS, a port of Debian, has offered the option to use Wayland since version 11 (Bullseye), which was released on 3 December 2021. Wayland became the default in version 12 (Bookworm), released on 10 October 2023.
- Red Hat Enterprise Linux ships Wayland as the default session in version 8, released 7 May 2019.
- Steam OS 3.7's desktop mode moved to KDE Plasma 6.2 from Plasma 5.27, however, at the time, Valve still defaulted to the X.Org session. Steam OS 3.8's desktop mode moved to KDE Plasma 6.4, and with this release of Steam OS, Valve switched the desktop mode to the Wayland session by default.
- Ubuntu shipped with Wayland by default in Ubuntu 17.10 (Artful Aardvark). However, Ubuntu 18.04 LTS reverted to X.Org by default due to several issues. Since Ubuntu 21.04's release in 2021, Wayland is the default again. As of Ubuntu 25.10, because GNOME 49, the version of GNOME used in that version, the X.Org session was disabled at compile time. As the next version of GNOME, GNOME 50, would see the X.Org session fully removed, and because Ubuntu 26.04 is an LTS release of Ubuntu, Ubuntu did not renable the X.Org session to allow for testing 25.10 with only the Wayland session in preparation for Ubuntu 26.04.
- Slackware Linux included Wayland on 20 February 2020 for the development version, -current, which became version 15.0 in 2022. However, Wayland is still not the default.

### Toolkit support

Toolkits supporting Wayland include the following:

- EFL has complete Wayland support, except for selection.
- GTK 3.20 has complete Wayland support.
- Qt 5 has complete Wayland support, and can be used to write both Wayland compositors and Wayland clients.
- SDL support for Wayland debuted with the 2.0.2 release and was enabled by default since version 2.0.4.
- GLFW 3.2 has Wayland support.
- FreeGLUT has initial Wayland support.
- FLTK supports Wayland since version 1.4.0 (Nov. 2024).

### Desktop environments

Desktop environments that have been ported from X11 to Wayland include GNOME, KDE Plasma and Enlightenment. Currently, Xfce is also developing a Wayland compositor.

- **GNOME** 3.20 was the first version to have a full Wayland session. GNOME 3.22 included much improved Wayland support across GTK, Mutter, and GNOME Shell. GNOME 3.24 shipped support for the proprietary Nvidia drivers under Wayland. In GNOME 49, the X.Org session was disabled by default and in GNOME 50, the X.Org session support was removed from the source code. This does *not* remove the ability to run X11 apps on the Wayland session of GNOME via XWayland.
- **KDE Plasma** started supporting Wayland in version 5. Version 5.4 of Plasma was the first with a full Wayland session. In KDE Plasma 6.0, Wayland became the default session, with X.Org available as a fallback session. In KDE Plasma 6.4, KWin saw the X.Org session In KDE Plasma 6.8, which is scheduled to release in early 2027, KDE Plasma will drop support for the X11 session. This does *not* remove the ability to run X11 apps on the Wayland session of KDE Plasma via XWayland.
- In November 2015, **Enlightenment** e20 was announced with full Wayland support.
- In January 2026, **Xfce** announced xfwl4, the Wayland equivalent of xfwm. xfwl4 will be written in Rust using smithay, the same toolkit used by System76's COSMIC, used in Pop!_OS as of 24.04. Unlike GNOME & KDE Plasma, as of April 2026, the Xfce developers announced that the X11 session would not be deprecated and/or removed as long as there were developers willing to maintain xfwm.

### Other software

Other software supporting Wayland includes the following:

- Intelligent Input Bus is working on Wayland support, it could be ready for Fedora 22.
- RealVNC published a Wayland developer preview in July 2014.
- wayvnc is a VNC server for wlroots-based Wayland compositors.
- Maliit and KDE's Plasma Keyboard are two virtual keyboards used as an input method framework that run under Wayland.
- kmscon supports Wayland with wlterm.
- Mesa has Wayland support integrated.
- Eclipse was made to run on Wayland during a GSoC-Project in 2014.
- The Vulkan WSI (Window System Interface) is a set of API calls that serve a similar purpose as EGL does for OpenGL & OpenGL ES or GLX for OpenGL on X11. Vulkan WSI includes support for Wayland from day one: VK_USE_PLATFORM_WAYLAND_KHR. Vulkan clients can run on unmodified Wayland servers, including Weston, GENIVI LayerManager, Mutter / GNOME Shell, Enlightenment, and more. The WSI allows applications to discover the different GPUs on the system, and display the results of GPU rendering to a window system.
- Waydroid (formerly called Anbox-Halium), a container for Android applications to run on Linux distributions using Wayland.

### Mobile and embedded hardware

Mobile and embedded hardware supporting Wayland includes the following:

- postmarketOS
- GENIVI Alliance: The GENIVI Aliance, now COVESA, for in-vehicle infotainment (IVI) supports Wayland.
- Jolla: Smartphones from Jolla use Wayland. It is also used as standard when Linux Sailfish OS is used with hardware from other vendors or when it is installed into Android devices by users.
- Tizen: Starting in version 2.x, Tizen supports Wayland in in-vehicle infotainment (IVI) setups. From 3.0 onward, Tizen defaults to Wayland.

## History

Wayland

uses

direct rendering

over

EGL

.

Kristian Høgsberg, a Linux graphics and X.Org developer who previously worked on AIGLX and DRI2, started Wayland as a spare-time project in 2008 while working for Red Hat. His stated goal was a system in which "every frame is perfect, by which I mean that applications will be able to control the rendering enough that we'll never see tearing, lag, redrawing or flicker." Høgsberg was driving through the town of Wayland, Massachusetts when the underlying concepts "crystallized", hence the name (Weston and Maynard are also nearby towns in the same area, continuing the reference). Other early prominent developers for Wayland include Daniel Stone, Peter Hutterer, and Pekka Paalanen.

In October 2010, Wayland became a freedesktop.org project. The developer mailing list was migrated at that time to *wayland-devel*, which as of 2026 is hosted via GNU Mailman.

The Wayland client and server libraries were initially released under the MIT License, while the reference compositor Weston and some example clients used the GNU General Public License version 2. Later, all the GPL code was relicensed under the MIT license "to make it easier to move code between the reference implementation and the actual libraries". In 2015 it was discovered that the license text used by Wayland was a slightly different and older version of the MIT license, and the license text was updated to the current version used by the X.Org project (known as MIT Expat License).

Wayland works with all Mesa-compatible drivers with DRI2 support as well as Android drivers via the Hybris project.

### Releases

| Version | Date | Main features |   |   |
|---|---|---|---|---|
| Wayland | Weston | Wayland Protocols |   |   |
| Unsupported: 0.85 | 9 February 2012 | First release. |   |   |
| Unsupported: 0.95 | 24 July 2012 | Began API stabilization. |   |   |
| Unsupported: 1.0 | 22 October 2012 | Stable wayland-client API. |   |   |
| Unsupported: 1.1 | 15 April 2013 |   | Software rendering. FBDEV, RDP backends. |   |
| Unsupported: 1.2 | 12 July 2013 | Stable wayland-server API. | Color management. Subsurfaces. Raspberry Pi backend. |   |
| Unsupported: 1.3 | 11 October 2013 | More pixel formats. Support for language bindings. | Android driver support via libhybris. |   |
| Unsupported: 1.4 | 23 January 2014 | New wl_subcompositor and wl_subsurface interfaces. | Multiple framebuffer formats. logind support for rootless Weston. |   |
| Unsupported: 1.5 | 20 May 2014 |   | libinput. Fullscreen shell. |   |
| Unsupported: 1.6 | 19 September 2014 |   | libinput by default. |   |
| Unsupported: 1.7 | 14 February 2015 |   | Support for the Wayland presentation extension and for surface roles. IVI shell protocol. |   |
| Unsupported: 1.8 | 2 June 2015 | Separated headers for core and generated protocol. | Repaint scheduling. Named outputs. Output transformations. Surface-shooting API. |   |
| Unsupported: 1.9 | 21 September 2015 | Updated license. | Updated license. New test framework. Triple-head DRM compositor. linux_dmabuf extension. | 1.0 (24 November 2015) |
| Unsupported: 1.10 | 17 February 2016 | Drag-and-drop functionality, grouped pointer events. | Video 4 Linux 2, touch input, debugging improvements. | 1.1 (16 February 2016) 1.4 (23 May 2016) |
| Unsupported: 1.11 | 1 June 2016 | New backup loading routine, new setup logic. | Proxy wrappers, shared memory changes, Doxygen-generated HTML docs. | 1.5 (22 July 2016) 1.7 (15 August 2016) |
| Unsupported: 1.12 | 21 September 2016 | Debugging support improved. | libweston and libweston-desktop. Pointer locking and confinement. Relative pointer support. |   |
| Unsupported: 1.13 | 24 February 2017 |   | The ABI of Weston has been changed, thus the new version was named 2.0.0 rather than 1.13.0. | 1.8 (12 June 2017) 1.10 (31 July 2017) |
| Unsupported: 1.14 | 8 August 2017 |   | Weston 3.0.0 was released at the same time. | 1.11 (11 October 2017) 1.13 (14 February 2018) |
| Unsupported: 1.15 | 9 April 2018 |   | Weston 4.0.0 was released at the same time. | 1.14 (7 May 2018) 1.16 (30 July 2018) |
| Unsupported: 1.16 | 24 August 2018 |   | Weston 5.0.0 was released at the same time. | 1.17 (12 November 2018) |
| Unsupported: 1.17 | 20 March 2019 |   | Weston 6.0.0 was released at the same time. | 1.18 (25 July 2019) |
| Unsupported: 1.18 | 11 February 2020 |   | Weston 7.0.0 was released on 23 August 2019. Weston 8.0.0 was released on 24 January 2020. Weston 9.0.0 was released on 4 September 2020. | 1.19 (29 February 2020) 1.20 (29 February 2020) |
| Unsupported: 1.19 | 27 January 2021 |   |   | 1.21 (30 April 2021) 1.24 (23 November 2021) |
| Unsupported: 1.20 | 9 December 2021 |   | Weston 10.0.0 was released on 1 February 2022. Weston 10.0.5 was released on 2 August 2023. | 1.25 (28 January 2022) |
| Unsupported: 1.21 | 30 June 2022 |   | Weston 11.0.0 was released on 22 September 2022. Weston 11.0.3 was released on 2 August 2023. | 1.26 (7 July 2022) 1.31 (29 November 2022) |
| Supported: 1.22 | 4 April 2023 |   | Weston 12.0.0 was released on 17 May 2023. Weston 12.0.5 was released on 29 April 2025. Weston 13.0.0 was released on 27 November 2023. Weston 13.0.4 was released on 25 April 2025. | 1.32 (3 July 2023) 1.36 (26 April 2024) |
| Supported: 1.23 | 30 May 2024 |   | Weston 14.0.0 was released on 4 September 2024. Weston 14.0.2 was released on 25 April 2025. | 1.37 (31 August 2024) 1.45 (13 June 2025) |
| Supported: 1.24 | 7 July 2025 |   | Weston 15.0.0 was released on 19 February 2026. | 1.46 (23 November 2025) 1.47 (15 December 2025) |
| Latest version: 1.25 | 19 March 2026 |   |   | 1.48 (1 April 2026) 1.49 (7 June 2026) |
| Future version: 1.26 |   |   |   |   |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |

---
title: "KDE Plasma"
source: https://en.wikipedia.org/wiki/KDE_Plasma
domain: kde-frameworks
license: CC-BY-SA-4.0
tags: kde frameworks, plasma desktop libraries, kirigami convergent ui, qt kde modules
fetched: 2026-07-02
---

# KDE Plasma

**KDE Plasma** is a graphical shell developed by the KDE community for Unix-like operating systems. It serves as the interface layer between the user and the operating system, providing a graphical user interface (GUI) and workspace environment for launching applications, managing windows, and interacting with files and system settings. Plasma is designed to be modular and adaptable, with different variants tailored for specific device types, such as **Plasma Desktop** for personal computers, and Plasma Mobile for smartphones.

Plasma was first introduced in 2008 as part of KDE Software Compilation 4, as a major technical overhaul, combining traditional desktop functionality with a widget-based system designed for flexibility and visual consistency. With the KDE brand repositioning in 2009, the KDE software compilation was split into three distinct projects: KDE Plasma, KDE Frameworks and KDE Gear, allowing each to develop and release on independent schedules. As of the Plasma 6 series, feature updates are released every four months, with interim bugfix releases.

## Releases

### Version history

### Plasma 4

Plasma 4 was released as part of KDE Software Compilation 4 and replacing the KDesktop shell, Kicker taskbar, and SuperKaramba widget engine, which formed the Desktop in earlier KDE releases. They are bundled as the default environment with a number of free software operating systems, such as Chakra, Kubuntu, Mageia (DVD version), openSUSE, or TrueOS.

From KDE SC 4.0 to KDE SC 4.2, the default theme, "Oxygen", was characterized by dark tones. In KDE SC 4.3, it was replaced by the new "Air" theme, which predominates in transparency and white as the base color. New themes for Plasma can be chosen and installed through software like Discover or online at store.kde.org.

With the release of KDE SC 4.11 on 14 August 2013, Plasma 4 was placed into a feature freeze and turned into a long-term stable package until August 2015. On 15 July 2014, Plasma 4's successor, Plasma 5, was released.

#### Features

Plasma features *containments*, which are essentially applets that contain other applets. Two examples of containments are the desktop background and the taskbar. A containment can be anything the developer wants: an image (either raster graphics or an SVG image), animation, or even OpenGL. Images are most commonly used, but with Plasma the user could set any applet as the desktop background without losing functionality of the applet. This also allows for applets to be dragged between the desktop and the taskbar (two separate containments), and have a separate visualization for the more confined taskbar.

Plasma separates components into "data engine" and their visualization counterparts. This is intended to reduce the total programming effort when there are multiple possible visualizations of given data, and to make it easier for the data engine and the workspaces to be written independently.

The scalable nature of the Plasma widgets allows for them to be resized and rotated to any size, with only a brief pause to redraw themselves. The Kross scripting framework allows developers to write widgets in a variety of programming languages in addition to C++.

*KRunner* is a versatile tool for several functions. It replaces the dialog box "Run Command" from K Desktop Environment 3, and also inherits from the application launcher feature, expanding the possibilities through a modular plug. KRunner stores previously entered commands and searches, accessible via an auto-complete feature. *KRunner* can be shown on the desktop via the keyboard combination Alt+F2 or by selecting "Run Command ..." in the desktop menu.

These functions are handled by the plugin:

- Application launcher: Type at least three letters of the desired name or description. KRunner shows applications associated with the terms of the search and allows the selection of the desired one.
- Calculator: Simply enter the desired operation to show the result. It also supports sophisticated expressions.
- Contacts can search for entries in KDE's address book, allowing users to directly open, for example, KMail to write an e-mail. The address of the recipient of your choice is automatically added to the message.
- Unit Converter converts values between different units of measure.
- Web history: Search history of recently visited sites in Konqueror.
- Recent documents: Search for recently opened files.

#### Widgets

This is a list of widgets that the current release version of Plasma supports. Not all widgets are supported by default in all Linux distributions; some may require different packages or even a recompilation of Plasma.

- First-generation native widgets (in C++, JavaScript, Ruby, or Python. In many distributions, the Ruby and Python bindings must be downloaded separately as packages.)
- Second-generation native widgets written in QML
- Apple Dashboard widgets
- SuperKaramba widgets – used in KDE 3
- Web widgets (supports HTML and JavaScript)

Previous Plasma Workspaces releases also supported Edje gadgets and E17 modules. Support for those was developed in 2008 but removed later, in 2010.

Google Gadgets were also supported. After Google announced the discontinuation of its two services that utilize Gadgets – Google Desktop and iGoogle – KDE removed support for this widget engine in March 2013.

### Plasma 5

Plasma 5 is the fifth generation of the graphical workspaces environment created by KDE primarily for Linux systems. Plasma 5 is the successor of Plasma 4 and was first released on 15 July 2014. It includes a new default theme, known as "Breeze", as well as increased convergence across different devices. The graphical interface was fully migrated to QML, which uses OpenGL for hardware acceleration, resulting in better performance and reduced power consumption.

Plasma Mobile is a Plasma 5 variant for Linux-based smartphones.

#### Architecture

KDE Plasma 5 is built using Qt 5 and KDE Frameworks 5, predominantly plasma-framework.

It improves support for HiDPI displays and ships a convergable graphical shell, which can adjust itself according to the device in use. 5.0 also includes a new default theme, dubbed Breeze. Qt 5's QtQuick 2 uses a hardware-accelerated OpenGL(ES) scene graph (canvas) to compose and render graphics on the screen, which allows for the offloading of computationally expensive graphics rendering tasks onto the GPU, freeing up resources on the system's main CPU.

#### Windowing systems

KDE Plasma 5 uses the X Window System and Wayland. Support for Wayland was prepared in the compositor and planned for a later release. It was made initially available in the 5.4 release. Stable support for a basic Wayland session was provided in the 5.5 release (December 2015).

Support for NVIDIA proprietary driver for Plasma on Wayland was added in the 5.16 release (June 2019).

#### Features

- KRunner, a search feature with many available plugins. In addition to launching apps, it can find files and folders, open websites, convert from one currency or unit to another, calculate simple mathematical expressions, and perform numerous other useful tasks.
- Flexible desktop and panel layouts composed of individual widgets (also known as "Plasmoids") can be individually configured, moved around, replaced with alternatives, or deleted. Each screen's layout can be individually configured. New widgets created by others can be downloaded within Plasma.
- Powerful clipboard with a memory of previously copied pieces of text that can be called up at will.
- Systemwide notification system supporting quick reply and drag-and-drop straight from notifications, history view, and a Do Not Disturb mode.
- Central location to control playback of media in open apps, the phone (with KDE Connect installed), or the web browser (with Plasma Browser Integration installed)
- Activities, which allow users to separate methods of using the system into distinct workspaces. Each activity can have its own set of favorite and recently used applications, wallpapers, "virtual desktops", panels, window styles, and layout configurations. It also couples with `ksmserver` (X Session Manager implementation) which keeps track of apps that can be run or shutdown along with given activity via subSessions functionality that keep track of state of applications (not all applications support this feature as they do not implement XSMP protocol).
- Encrypted vaults for storing sensitive data.
- Night Color, which can automatically warm the screen colors at night, or user-specified times, or manually.
- Styling for icons, cursors, application colors, user interface elements, splash screens and more can be changed, with new styles created by others being downloadable from within the System Settings application. Global Themes allow the entire look and feel of the system to be changed in one click.
- Session Management allows apps that were running when the system shut down to be automatically restarted in the same state they were in before.

### Plasma 6

KDE Plasma 6 is the sixth and current generation of the graphical workspaces environment made by KDE. It is the successor to Plasma 5 and was initially released on 28 February 2024.

Plasma 6 changes the default display server from X11 to Wayland, though the former is still available.

As of version 6.4, the X11 version is no longer installed by default and the KWin (the KDE window manager) codebase is split into *kwin* and *kwin_x11*. *Kwin* is the default Wayland version and will see active development. New fixes are developed for *kwin* first and backported later to *kwin_x11*. Version *kwin_x11* is maintained until Plasma 6.8 and no new features are expected to be backported.

## Variants

### Plasma Desktop

*Plasma Desktop* is the default and primary variant of KDE Plasma, designed for desktop PCs and laptops. It offers full support for widgets, desktop effects, multiple monitors, and extensive customization options.

With the release of Plasma 6 as part of the KDE MegaRelease 6 (28 February 2024), Wayland became the default display protocol, although X11 remains available as an alternative. Plasma 6.8, scheduled for release on October 2026, is planned to drop the X11 session entirely, with only XWayland remaining to support X11 applications.

Notable improvements in Plasma 6 include:

- Merging of the "Overview" and "Desktop Grid" effects, with improved touch gesture support.
- Support for HDR and ICC color profiles under Wayland.
- Accessibility improvements including color blindness correction filters.
- Default use of a "floating panel", with smarter auto-hide behavior ("Dodge Windows").
- Progress toward persistent session restoration, restoring app states and window locations across restarts.

### Plasma Netbook

*Plasma Netbook* was a variant optimized for netbooks and small tablet PCs. It debuted with KDE Software Compilation 4.4 in 2010. Development was discontinued with Plasma 5, and its features were merged into the main Plasma shell.

### Plasma Active

*Plasma Active* was a variant designed for touchscreen devices such as tablets. It featured applications like Kontact Touch and a document viewer from the Calligra Suite. It also introduced the "Contour" user interface, developed in 2011 by basysKom. Plasma Active was succeeded by Plasma Mobile with the transition to KDE Frameworks 5.

### Plasma Mobile

*Plasma Mobile* is aimed at smartphones and small tablets operated via touch input. A version based on Qt 6 and KDE Frameworks 6 was released alongside Plasma 6.

Key changes in recent Plasma Mobile versions include:

- A redesigned home screen supporting grids, folders, paging, and app drawer with KRunner integration.
- Dropping support for Halium-based devices, focusing instead on mainline Linux-supported smartphones.
- Active development across distributions such as postmarketOS, with various ports to older devices in progress.

### Plasma Bigscreen

*Plasma Bigscreen* is a shell variant for smart TVs, large displays, and set-top boxes, optimized for remote control or controller-based navigation. It was first introduced with Plasma 5.26.

Current status:

- Initially dropped from the Plasma 6 release due to delayed Qt 6 porting, but re-added in Plasma 6.7.
- Actively revived by developers such as Devin Lin with UI rewrites, home screen redesign, TV control apps, and Raspberry Pi 5 testing.
- Packages are available in some distributions, including Fedora 42 (`plasma-bigscreen-5.27.80`).
- Currently, Flatpak is unsuitable for packaging Bigscreen as a system shell. Snap or image-based deployment may be explored. Nightly builds and testing images are being used in development.

### Plasma Nano

*Plasma Nano* is a minimal shell designed for embedded, automotive, IoT, and other touchscreen-based low-resource devices. It provides only essential UI elements for building custom lightweight interfaces.

Status:

- Available in distributions like Alpine Linux (`plasma-nano 6.4.5` in the edge repository).
- Also packaged in openMamba and other independent distributions.
- Documentation remains limited. Community discussions point to a need for clearer guidance on customization and deployment scenarios.

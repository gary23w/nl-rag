---
title: "GNOME (part 1/2)"
source: https://en.wikipedia.org/wiki/GNOME
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 1/2
---

# GNOME

**GNOME** (/ɡəˈnoʊm, ˈnoʊm/) is a free and open-source desktop environment for Linux and other Unix-like operating systems. It is distributed as the default desktop environment of many major Linux distributions, including Debian, Fedora Linux, Ubuntu, Red Hat Enterprise Linux, and SUSE Linux Enterprise, and is the default in Oracle Solaris, a Unix operating system.

GNOME is developed by the GNOME Project, which is composed of both volunteers and paid contributors, the largest corporate contributor being Red Hat. It is an international project that aims to develop frameworks for software development, to program end-user applications based on these frameworks, and to coordinate efforts for the internationalization, localization, and accessibility of that software.

In 2023 and 2024, GNOME received €1,000,000 from Germany's Sovereign Tech Fund.


## Interface design

Since GNOME 2, productivity has been a key focus for GNOME. To meet this end, the GNOME Human Interface Guidelines (HIG) were created. All GNOME programs share a coherent style of interfaces but are not limited to the employment of the same GUI widgets. Rather, the design of the GNOME's interface is guided by concepts described in the HIG, itself relying on insights from cognitive ergonomics. Following the HIG, developers can create high-quality, consistent, and usable GUI programs, as it addresses everything from interface design to the recommended pixel-based layout of widgets. However, critics have complained about GNOME ignoring traditional user interface conventions, and the wasting of screen real estate.

During the GNOME 2 rewrite, many settings deemed of little value to the majority of users were removed. The guiding principle was outlined by Havoc Pennington – a software developer involved in the project – who emphasized the idea that it is better to make software behave correctly by default than to add a UI preference to get the desired behavior:

> A traditional free software application is configurable so that it has the union of all features anyone's ever seen in any equivalent application on any other historical platform. Or even configurable to be the union of all applications that anyone's ever seen on any historical platform (Emacs *cough*).
> 
> Does this hurt anything? Yes it does. It turns out that preferences have a cost. [...] [E]ach one has a price, and you have to carefully consider its value. Many users and developers don't understand this, and end up with a lot of cost and little value for their preferences dollar.

— Havoc Pennington, *Free software UI*


## Features

### Accessibility

GNOME aims to make and keep the desktop environment physically and cognitively ergonomic for people with disabilities. The GNOME Human Interface Guidelines try to take this into account as far as possible but specific issues are solved by special software.

GNOME addresses computer accessibility issues by using the Accessibility Toolkit (ATK) application programming interface, which allows enhancing user experience by using special input methods and speech synthesis and speech recognition software. Particular utilities are registered with ATK using Assistive Technology Service Provider Interface (AT-SPI), and become globally used throughout the desktop. Several assistive technology providers, including Orca screen reader and Dasher input method, were developed specifically for use with GNOME.

### Internationalization and localization

The internationalization and localization of GNOME software relies on locale, and supports 197 languages with varying levels of completion, with some not being translated at all.


## Session types

### GNOME Shell

GNOME Shell is the main graphical shell of GNOME. It features a top bar holding (from left to right) an Overview button, a clock and an integrated system status menu. The application menu displays the name of the application in focus and provides access to functions such as accessing the application's preferences, closing the application, or creating a new application window. The status menu holds various system status indicators, shortcuts to system settings, and session actions including logging out, switching users, locking the screen, and suspending the computer.

Clicking on the Activities button, moving the mouse to the top-left hot corner or pressing the Super key brings up the Overview. The Overview gives users an overview of current activities and provides a way to switch between windows and workspaces and to launch applications. The Dash on the bottom houses shortcuts to favorite applications, currently open windows, and an application picker button to show a list of all installed applications. A search bar appears at the top and a workspace list for viewing and switching between workspaces is directly above it. Notifications appear from the top of the shell.

### GNOME Classic

Beginning with GNOME 3.8, GNOME provides a suite of officially supported GNOME Shell extensions that provide an Applications menu (a basic start menu) and a "Places menu" on the top bar and a panel with a windows list at the bottom of the screen that lets users quickly minimize and restore open windows, a "Show Desktop" button in the bottom left corner, and virtual desktops in the bottom right corner. GNOME Classic also adds the minimize and maximize buttons to window headers.

GNOME Classic 3.36 (March 2020)

GNOME Classic 3.12 with GNOME Files (March 2014)

### GNOME Flashback

*GNOME Flashback* is an official session for GNOME 3. Based on GNOME Panel and Metacity, it has lower hardware requirements and uses fewer system resources than GNOME Shell. It provides a traditional and highly customizable taskbar (panel) with many plug-ins bundled in one package (gnome-applets), including a customizable start menu. It provides a similar user experience to the GNOME 2.x series and has customization capacities built in.

GNOME Flashback consists of the following components:

- Metacity (window manager)
- GNOME Panel – a highly configurable taskbar
- gnome-applets – a collection of useful applets for the GNOME Panel

### GNOME Mobile

*GNOME Mobile* is a set of patches on top of the GNOME stack, that make GNOME suitable for mobile phones and touch devices. A core component enabling this adaptability is libadwaita, a GTK-based library that provides consistent, adaptive UI components and widgets for GNOME applications, which ensures a cohesive design language across platforms. GNOME Mobile is available as a desktop environment in PostmarketOS.


## Applications

### Core Applications

There are a large number of GTK-based programs written by various authors. Since the release of GNOME 3.0, GNOME Project concentrates on developing a set of programs that accounts for the GNOME Core Applications. The commonalities of the GNOME Core Applications are the adherence to the current GNOME Human Interface Guidelines (HIG) as well as the tight integration with underlying GNOME layers like e.g. GVfs (GNOME virtual filesystem) and also with one another e.g. GOA (gnome-online-accounts) settings and GNOME Files with Google Drive and GNOME Photos with Google Photos. Some programs are simply existing programs with a new name and revamped user interface, while others have been written from scratch.

### Development tools

The GNOME project provides a suite of software development tools to facilitate the creation of GNOME software. These tools are designed to streamline the development process for the GNOME ecosystem.

1. Integrated Development Environments (IDEs):
  - GNOME Builder: The official IDE developed by the GNOME project, replacing the older Anjuta IDE.
2. User interface design:
  - Cambalache Interface Designer: A Rapid Application Development (RAD) IDE for GTK 3 and GTK 4, serving as the successor to the Glade Interface Designer.
3. Debugging and Documentation Tools:
  - GTK Inspector: Shipped with GTK, this tool allows developers to inspect the widget tree of an application for debugging purposes.
  - Devhelp: A GNOME utility for browsing and searching API documentation.
4. Libraries and Frameworks:
  - libsoup: A library that enables GNOME applications to access HTTP servers, using GObjects.
  - BuildStream: A flexible, extensible framework written in Python for modeling build and CI pipelines using a declarative YAML format.
5. Third-Party Integration:
  - The GNOME ecosystem supports integration options for third-party development tools, expanding the possibilities for developers.

These tools collectively provide a comprehensive development environment for creating software that aligns with the GNOME desktop and its design principles.

### GNOME Circle

GNOME Circle is a collection of applications which have been built to extend the GNOME platform, utilize GNOME technologies, and follow the GNOME human interface guidelines.


## History

### GNOME 1

GNOME was started on 15 August 1997 by Miguel de Icaza and Federico Mena as a free software project to develop a desktop environment and applications for it. It was founded in part because the K Desktop Environment, which was growing in popularity, relied on the Qt widget toolkit which used a proprietary software license until version 2.0 (June 1999). In place of Qt, GTK (formerly called GIMP Toolkit) was chosen as the base of GNOME. GTK is licensed under the GNU Lesser General Public License (LGPL), a free software license that allows software linking to it to use a much wider set of licenses, including proprietary software licenses. GNOME itself is licensed under the LGPL for its libraries and the GNU General Public License (GPL) for its applications.

GNOME was formerly a part of the GNU Project, but that is no longer the case. In 2021, GNOME Executive Director Neil McGovern publicly tweeted that GNOME was not a GNU project and that he had been asking GNU to remove GNOME from their list of packages since 2019. In 2021, GNOME was removed from the list. GNOME proceeded to remove mentions of any link to GNU from their code and documentation. The name "GNOME" was initially an acronym for *GNU Network Object Model Environment*, referring to the original intention of creating a distributed object framework similar to Microsoft's OLE, but the acronym was eventually dropped because it no longer reflected the vision of the GNOME project.

The California startup Eazel developed the Nautilus file manager from 1999 to 2001. De Icaza and Nat Friedman founded Helix Code (later Ximian) in 1999 in Massachusetts; this company developed GNOME's infrastructure and applications and was purchased by Novell in 2003.

During the transition to GNOME 2 and shortly thereafter, there were brief talks about creating a *GNOME Office* suite. On 15 September 2003 GNOME-Office 1.0, consisting of AbiWord 2.0, GNOME-DB 1.0, and Gnumeric 1.2.0, was released. Although some release planning for GNOME Office 1.2 was happening on the gnome-office mailing list, and Gnumeric 1.4 was announced as a part of it, the 1.2 release of the suite itself never materialized. As of 4 May 2014, the GNOME wiki only mentions "GNOME/GTK applications that are useful in an office environment".

### GNOME 2

GNOME 2 was released in June 2002 and was very similar to a conventional desktop interface, featuring a simple desktop in which users could interact with virtual objects such as windows, icons, and files. GNOME 2 started out with Sawfish as its default window manager, but later switched to Metacity in GNOME 2.2. The handling of windows, applications, and files in GNOME 2 is similar to that of contemporary desktop operating systems. In the default configuration of GNOME 2, the desktop has a launcher menu for quick access to installed programs and file locations; open windows may be accessed by a taskbar along the bottom of the screen; and the top-right corner features a notification area for programs to display notices while running in the background. However, these features can be moved to almost any position or orientation the user desires, replaced with other functions, or removed altogether.

As of 2009, GNOME 2 was the default desktop for OpenSolaris. The MATE desktop environment is a fork of the GNOME 2 codebase (see Criticism, below.)

### GNOME 3

In 2008, an increasing discontent among the community and developers about the lack of project direction and technical progress prompted the announcement of GNOME 3.0. Originally, the plan was to make only incremental changes and avoid disruption for users. This changed when efforts led to the creation of the GNOME Shell.

GNOME 3 was released in 2011. While GNOME 1 and 2 interfaces followed the traditional desktop metaphor, the GNOME Shell adopted a more abstract metaphor with a minimalistic window management workflow, where switching between different tasks and virtual desktops occurs in a separate area called *the* *overview.* The *Minimize* and *maximize* buttons were hidden by default, leaving only the close button and application name in the window decoration.

GNOME 3 brought many enhancements to core software. Many GNOME Core Applications also went through redesigns to provide a better user experience. Mutter replaced Metacity as the default window manager, and Adwaita replaced Clearlooks as the default theme.

#### Criticism

The release of GNOME 3 caused considerable controversy in the GNU and Linux communities. Aiming to provide an easy-to-use and uncluttered user experience has led to some criticized design decisions, like the removal of *minimize* and *maximize* buttons, the simplification of configuration options, and visual cues that could lead to confusion.

Several projects have been initiated to either continue development of GNOME 2.x, modify GNOME 3.x to be more like the 2.x releases, or create a desktop environment with a traditional design metaphor entirely from scratch due to the negative reception of GNOME 3:

- The MATE desktop environment was forked in August 2011 from the GNOME 2 code-base with the intent of preserving the traditional desktop metaphor associated with GNOME 2 while keeping compatibility with modern Linux-related technologies, such as Wayland, Systemd, PipeWire, and GTK3.
- The Linux Mint team addressed the issue by developing "Mint GNOME Shell Extensions" that ran on top of GNOME Shell and allowed it to be used via the traditional desktop metaphor. This eventually led to the creation of the Cinnamon desktop environment in 2011, which was forked from the GNOME 3 codebase. Cinnamon became a completely independent desktop environment from GNOME Shell with Cinnamon 2.0 on October 9, 2013.
- The LXDE Project, which was experimenting with a Qt port at the time, merged with the Razor-qt project to form LXQt in 2013. The main developer of LXDE, Hong Jen Lee, cited that the reason he wanted to port LXDE to Qt was due to dissatification with the memory and CPU consumption of GTK3 and GNOME libraries when testing a GTK3 version of LXDE. Hong eventually posted a blog post about how an early build of LXQt used less memory than GTK3-based XFCE.
- Canonical, the company developing Ubuntu, ceased working with the GNOME Shell developers during the GNOME 3 planning phases and released their own desktop environment, Unity, replacing GNOME as the default desktop shell in Ubuntu 11.04 "Natty Narwhal" released in April 2011. Previously, Unity had only been intended for use with the Ubuntu Netbook Edition starting with version 10.10 and a now-canceled edition of Ubuntu called Ubuntu Light. However, Ubuntu has since switched to a modified version of GNOME as of Ubuntu 17.10.
- The Solus Project developed the Budgie desktop environment in response to GNOME 3 in 2014, aiming to provide a simpler and more modern interface. Budgie is built using GTK and GNOME technologies, but offers a different user experience, focusing on providing a lightweight, simple, and elegant user experience.
- The elementaryOS team created the Pantheon desktop environment as a new GTK-based desktop environment distinct from GNOME. Built from scratch, Pantheon aims to provide a user-friendly and visually appealing aesthetic, focusing on a cohesive and minimal design, and integrating tightly with the elementaryOS ecosystem.
- System76, an American computer manufacturer selling computer hardware with Linux preinstalled and the creators of a set of GNOME extensions for their own Linux distribution Pop!_OS known collectively as COSMIC, built a new desktop environment of the same name in Rust. The reasons cited by System76 for building a new desktop environment from scratch included limitations with GNOME extensions as well as disagreements with GNOME developers on the desktop experience, such as with supporting server-side decorations in addition to client-side decorations on Wayland. COSMIC will support both client-side and server-side window decorations, unlike GNOME, which only supports the former.

Among those critical of the early releases of GNOME 3 is Linus Torvalds, the creator of the Linux kernel. Torvalds abandoned GNOME for a while after the release of GNOME 3.0, saying, "The developers have apparently decided that it's 'too complicated' to actually do real work on your desktop, and have decided to make it really annoying to do". He subsequently switched to Xfce.

Over time, critical reception has grown more positive. In 2013, Torvalds resumed using GNOME, noting that "they have extensions now that are still much too hard to find; but with extensions you can make your desktop look almost as good as it used to look two years ago". Debian, a Linux distribution that had historically used GNOME 2, switched to Xfce when GNOME 3 was released, but re-adopted GNOME 3 in time for the release of Debian 8 "Jessie". Ubuntu switched from Unity to GNOME 3 with several extensions to resemble Unity, such as a persistent left application panel instead of a hidden dock and re-enabling desktop icons, with Ubuntu 17.10 Artful Aardvark in 2017. This release also saw the Ubuntu GNOME edition merge with the mainline release. However, Ubuntu Unity was then released, keeping the Unity desktop and continuing to update it.

### GNOME 40 and higher

GNOME 40 was released on 24 March 2021. It immediately follows version 3, but adopts a new versioning scheme and a schedule of future major releases on a fixed six-month cycle (see Release Cycle). With this quicker release cadence, major releases became somewhat leaner, because full rewrites of major packages were not occurring as often as they were in the jumps between GNOME 1.0, 2.0, and 3.0 versions.

GNOME 40 organizes the activities overview in a horizontal fashion, instead of using a vertical design like its predecessors. The release also brings new touchpad gestures.

GNOME 40

GNOME 41

GNOME 41 was released on 22 September 2021 and introduced a rewritten and redesigned GNOME Software application manager, a multitasking panel and a mobile network (for WWAN) panel in settings, a new remote desktop app called Connections, updates to GNOME Music app, and improvements to the power mode settings.

GNOME 42 was released on 23 March 2022 and introduced the option to screen record and switch light/dark themes using a new GTK API called Libadwaita. Several default apps were replaced with more modern versions such as Text Editor instead of Gedit and Console instead of Terminal.

GNOME 43 (Guadalajara) was released on 21 September 2022 and introduced a new quick settings menu, a GNOME Files update to GTK4, and a new 'Device Security' panel in settings, among many other changes. GNOME Web was updated, bringing in support for web apps and experimental Firefox and Chrome extension support.

GNOME 44 (Kuala Lumpur) was released on 22 March 2023. Named after Kuala Lumpur in recognition of work done by the GNOME.Asia community, GNOME 44 introduced a new file chooser grid view, updated settings panels, and redesigned accessibility settings. The new quick settings menu introduced in GNOME 43 was updated, alongside the addition of several new apps and improvements to existing apps.

GNOME 45 (Rīga) was released on 20 September 2023. It introduced redesigned app styles alongside a new activities button, which replaced both the previous "Activities" label and the app menu with a graphical workspace indicator. Other updates to the system bar included a new camera usage indicator and a keyboard shortcut to open and close the quick settings menu. GNOME 45 also introduced two new image viewer and camera apps, keyboard backlight controls, and numerous enhancements to existing apps.

GNOME 46 (Kathmandu) was released on 20 March 2024 and featured an enhanced files app with global search, support for headless remote login via GDM, and a refreshed settings app, amongst many other app changes. Other system changes included accessibility improvements and experimental support for variable refresh rates.

GNOME 47 (Denver) was released on 18 September 2024 and introduced support for user-selected accent colors in Libadwaita applications, allowing greater interface customization. It also brought improvements for low-resolution displays through automatic icon scaling, optimizations in screen recording with GPU hardware encoding, and various enhancements to performance, file navigation, and online accounts.

GNOME 48 (Bengaluru) was released on 19 March 2025 and is included in Fedora 42 and Ubuntu 25.04. This version introduced notification grouping by application (notification stacking), significant performance improvements such as dynamic triple buffering for smoother animations, and optimizations in CPU and memory usage across key system components. It also included improvements in file indexing and graphical stability on systems with dedicated GPUs.

GNOME 49 (Brescia) was released in September 2025 and is included in Fedora 43 and Ubuntu 25.10. It deprecated X11 support, disabling it by default. It also replaced the video player Totem and the document viewer Evince with Showtime and Papers, respectively, and introduced shutting down and restarting the computer when logged out.

GNOME 50 (Tokyo) was released on 18 March 2026. GNOME 50 removed X11 support from the source code. It introduced new parental control features, accessibility improvements such as global options and reduced animations, and optimizations in core applications such as Files (Nautilus) and Calendar. It also added improvements to remote desktop with hardware acceleration, expanded graphics support (including enhancements for NVIDIA and variable refresh rates), and new options in system settings.

### GNOME Panel

**GNOME Panel** was a highly configurable taskbar for GNOME. It formed a core part of the desktop in GNOME 1 and GNOME 2. It has been replaced in GNOME 3 by default with GNOME Shell, which only works with the Mutter window manager. GNOME Panel served as *Fallback Mode* until GNOME 3.8 when Mutter could not be executed, then it was replaced with a suite of officially supported GNOME Shell extensions named *GNOME Classic*. Now it is part of *GNOME Flashback*, an official session for GNOME 3 which provides a user experience similar to GNOME 2. In GNOME 3, customizing GNOME Panel is done by pressing the Alt key while right-clicking on the panel.

By default, GNOME Flashback contains two panels (one on the top, and one to its opposite on the bottom) spanning the width of the screen. The top panel usually contains navigation menus labeled "Applications" and "Places" in that order, as the "System" menu from GNOME 2.x has been replaced by a control panel in GNOME 3.x. These menus hold links to common applications and areas of the file system, respectively. A user menu placed on the opposite side of the screen, which has been available since GNOME 2.14 but has become more prominent in GNOME 3.x, holds access to account and system settings as well as options to log out, switch user, and shut down the computer. The top panel usually contains a clock/calendar and a notification area, which can double as a sort of dock, as well. The bottom panel is commonly empty by default (other than a set of buttons to navigate between desktops) due to its use in the navigation between windows (windows minimize to the bottom panel by default).

Users can populate these panels with other completely customizable menus and buttons, including new menus, search boxes, and icons, with the icons in particular (called *launchers*) performing functions similar to the *quick-launch* feature found in the Microsoft Windows 98–Vista taskbar. Other applications can also be attached to the panels, and the panels are highly reconfigurable: anything on these panels can be moved, removed, or configured in other ways. For example, a migrating Microsoft Windows user might move the menus usually positioned in the top panel into a 'start' menu on the bottom panel as well as moving the notification area into the place normally positioned by the Windows notification area, then remove the top panel altogether, to interact with GNOME Panel similarly to the Windows taskbar. The version of GNOME Panel available in the repository for Ubuntu 12.04 offers a modified version of Fallback Mode with the addition of a custom theme and ports of Ubuntu's own Indicators from their old GNOME 2.x desktop. Trisquel uses Fallback Mode (Flashback) for its main desktop, because GNOME Shell requires 3D acceleration as it relies on graphics composition, while some free software drivers do not support 3D acceleration, among other reasons like more usability and more stability.


## Releases

### Release cycle

Each of the component software products in the GNOME project has its own version number and release schedule. However, individual module maintainers coordinate their efforts to create a full GNOME stable release on an approximately six-month schedule, alongside its underlying libraries such as GTK and GLib. Some experimental projects are excluded from these releases.

Before GNOME 40, GNOME version numbers followed the scheme *v.xx.yy*. Here, *v* is a major version, which can include large changes such as ABI breakage; these have no regular schedule and occur in response to requirements for large-scale changes. *xx* is a minor version, released on the above schedule of approximately every 6 months, in which the 1- or 2-digit number's parity indicates the type of release: if *xx* is even (e.g. 3.20) the release is considered stable, whereas if *xx* is odd, it represents a current development snapshot (e.g. 3.21) that will eventually evolve into the next stable release. *yy* indicates a point release, e.g. 3.20.6; these are made on a frequency of weeks in order to fix issues, add non-breaking enhancements, etc.

GNOME 40 started a new versioning scheme in which a single number is incremented with each semi-annual release. The number is followed by a dot and then "alpha", "beta", or "rc" for a development release, or a decimal for a minor stable release (much like the *yy* mentioned previously).

GNOME releases are made to the main FTP server in the form of source code with configure scripts, which are compiled by operating system vendors and integrated with the rest of their systems before distribution. Most vendors only use stable and tested versions of GNOME and provide it in the form of easily installed, pre-compiled packages. The source code of every stable and development version of GNOME is stored in the GNOME git source code repository.

A number of build scripts (such as JHBuild or formerly GARNOME) are available to help automate the process of compiling the source code.

### Release history

| Version | Date | Information |
|---|---|---|
|   | August 1997 | GNOME development announced |
| 1.0 | March 1999 | First major GNOME release |
| 1.2 | May 2000 | Codename "Bongo" |
| 1.4 | April 2001 | Codename "Tranquility" Nautilus became the default file manager in GNOME, replacing GNU Midnight Commander, the previous default file manager used since GNOME 1.0. |
| 2.0 | June 2002 | Major upgrade based on GTK2. Introduction of the Human Interface Guidelines. |
| 2.2 | February 2003 | Multimedia and file manager improvements. |
| 2.4 | September 2003 | Codename "Temujin": Epiphany, accessibility support. |
| 2.6 | March 2004 | Nautilus changes to a spatial file manager from a navigational file manager by default, and a new GTK file dialog is introduced. A short-lived fork of GNOME, GoneME, is created as a response to the changes in this version. |
| 2.8 | September 2004 | Improved removable device support, adds Evolution. |
| 2.10 | March 2005 | Lower memory requirements and performance improvements. Adds: new panel applets (modem control, drive mounter and trashcan); and the Totem and Sound Juicer applications. |
| 2.12 | September 2005 | Nautilus improvements; improvements in cut/paste between applications and freedesktop.org integration. Adds: Evince PDF viewer; New default theme: Clearlooks; Alacarte menu editor; keyring manager and admin tools. Based on GTK 2.8 with cairo support. |
| 2.14 | March 2006 | Performance improvements (over 100% in some cases); usability improvements in user preferences; GStreamer 0.10 multimedia framework. Adds: Ekiga video conferencing application; Deskbar search tool; Pessulus lockdown editor; Fast user switching; Sabayon system administration tool. |
| 2.16 | September 2006 | Performance improvements. Adds: Tomboy notetaking application; Baobab disk usage analyser; Orca screen reader; GNOME Power Manager (improving laptop battery life); improvements to Totem, Nautilus; compositing support for Metacity; new icon theme. Based on GTK 2.10 with new print dialog. |
| 2.18 | March 2007 | Performance improvements. Adds: Seahorse GPG security application, allowing encryption of emails and local files; Baobab disk usage analyser improved to support ring chart view; Orca screen reader; improvements to Evince, Epiphany and GNOME Power Manager, Volume control; two new games, GNOME Sudoku and glChess. MP3 and AAC audio encoding. |
| 2.20 | September 2007 | Tenth anniversary release. Evolution backup functionality; improvements in Epiphany, EOG, GNOME Power Manager; password keyring management in Seahorse. Adds: PDF forms editing in Evince; integrated search in the file manager dialogs; automatic multimedia codec installer. |
| 2.22 | March 2008 | Addition of Cheese, a tool for taking photos from webcams and Remote Desktop Viewer; basic window compositing support in Metacity; introduction of GVfs; improved playback support for DVDs and YouTube, MythTV support in Totem; internationalised clock applet; Google Calendar support and message tagging in Evolution; improvements in Evince, Tomboy, Sound Juicer and Calculator. Deprecate GnomeVFS in favor of GVfs and GIO. |
| 2.24 | September 2008 | Addition of the Empathy instant messenger client, Ekiga 3.0, tabbed browsing in Nautilus, better multiple screens support and improved digital TV support. |
| 2.26 | March 2009 | New optical disc recording application Brasero, simpler file sharing, media player improvements, support for multiple monitors and fingerprint reader support. |
| 2.28 | September 2009 | Addition of GNOME Bluetooth module. Improvements to Epiphany web browser, Empathy instant messenger client, Time Tracker, and accessibility. Upgrade to GTK version 2.18. |
| 2.30 | March 2010 | Improvements to Nautilus file manager, including the reversion from a spatial file manager back to a navigational file manager, Empathy instant messenger client, Tomboy, Evince, Time Tracker, Epiphany, and Vinagre. iPod and iPod Touch devices are now partially supported via GVfs through libimobiledevice. Uses GTK 2.20. |
| 2.32 | September 2010 | Addition of Rygel and GNOME Color Manager. Improvements to Empathy instant messenger client, Evince, Nautilus file manager and others. 3.0 was intended to be released in September 2010, so a large part of the development effort since 2.30 went towards 3.0. This version of GNOME and many of its applications were forked as part of the MATE desktop environment. |
| 3.0 | April 2011 | Introduction of GNOME Shell. A redesigned settings framework with fewer, more focused options. Topic-oriented help based on the Mallard markup language. Side-by-side window tiling. A new visual theme and default font. Adoption of GTK 3.0 with its improved language bindings, themes, touch, and multiplatform support. Removal of long-deprecated development APIs. |
| 3.2 | September 2011 | Online accounts support; Web applications support; contacts manager; documents and files manager; quick preview of files in the File Manager; greater integration; better documentation; enhanced looks and various performance improvements. |
| 3.4 | March 2012 | New Look for GNOME 3 Applications: Documents, Epiphany (now called Web), and GNOME Contacts. Search for documents from the Activities overview. Application menus support. Refreshed interface components: New color picker, redesigned scrollbars, easier to use spin buttons, and hideable title bars. Smooth scrolling support. New animated backgrounds. Improved system settings with new Wacom panel. Easier extensions management. Better hardware support. Topic-oriented documentation. Video calling and Live Messenger support in Empathy. Better accessibility: Improved Orca integration, better high contrast mode, and new zoom settings. Plus many other application enhancements and smaller details. |
| 3.6 | September 2012 | Refreshed Core components: New applications button and improved layout in the Activities Overview. A new login and lock screen. Redesigned Message Tray. Notifications are now smarter, more noticeable, easier to dismiss. Improved interface and settings for System Settings. The user menu now shows Power Off by default. Integrated Input Methods. Accessibility is always on. New applications: Boxes, that was introduced as a preview version in GNOME 3.4, and Clocks, an application to handle world times. Updated looks for Disk Usage Analyzer, Empathy and Font Viewer. Improved braille support in Orca. In Web, the previously blank start page was replaced by a grid that holds your most visited pages, plus better full screen mode and a beta of WebKit2. Evolution renders email using WebKit. Major improvements to Disks. Revamped Files application (also known as Nautilus), with new features like Recent files and search. |
| 3.8 | March 2013 | Refreshed Core components: A new applications view with frequently used and all apps. An overhauled window layout. New input methods OSD switcher. The Notifications & Messaging tray now react to the force with which the pointer is pressed against the screen edge. Added Classic mode for those who prefer a more traditional desktop experience. The GNOME Settings application features an updated toolbar design. New Initial Setup assistant. GNOME Online Accounts integrates with more services. Web has been upgraded to use the WebKit2 engine. Web has a new private browsing mode. Documents has gained a new dual page mode & Google Documents integration. Improved user interface of Contacts. GNOME Files, GNOME Boxes and GNOME Disks have received a number of improvements. Integration of ownCloud. New GNOME Core Applications: GNOME Clocks and GNOME Weather. |
| 3.10 | September 2013 | A reworked system status area, which gives a more focused overview of the system. A collection of new applications, including GNOME Maps, GNOME Notes, GNOME Music and GNOME Photos. New geolocation features, such as automatic time zones and world clocks. HiDPI support and smart card support. D-Bus activation made possible with GLib 2.38 |
| 3.12 | March 2014 | Improved keyboard navigation and window selection in the Overview. Revamped first set-up utility based on usability tests. Wired networking re-added to the system status area. Customizable application folders in the Applications view. Introduction of new GTK widgets such as popovers in many applications. New tab style in GTK. GNOME Videos, GNOME Terminal and gedit were given a fresh look, more consistent with the HIG. A search provider for the terminal emulator is included in GNOME Shell. Improvements to GNOME Software and high-density display support. A new sound recorder application. New desktop notifications API. Progress in the Wayland port has reached a usable state that can be optionally previewed. |
| 3.14 | September 2014 | Improved desktop environment animations. Improved touchscreen support. GNOME Software supports managing installed add-ons. GNOME Photos adds support for Google. Redesigned UI for Evince, Sudoku, Mines and Weather. Hitori is added as part of GNOME Games. |
| 3.16 | March 2015 | Major changes include UI color scheme goes from black to charcoal. Overlay scroll bars added. Improvements to notifications including integration with Calendar applet. Tweaks to various apps including Files, Image Viewer, and Maps. New Preview applications: Calendar, Characters, Books. Continued porting from X11 to Wayland. |
| 3.18 | September 2015 | Major changes include Google Drive integration in Files. Firmware updates through Software. Automatic screen brightness. Touchpad gestures. Several new applications: GNOME Calendar and GNOME Character Map. Significant improvements to Files, Boxes and Polari. Smaller changes and bug fixes. |
| 3.20 | March 2016 | Significant improvements to many core applications, such as system upgrades and reviews in Software, simple photo editing in Photos and improved search in Files. Platform improvements include shortcut help windows which are available in many applications, a refined font, and better control of location services. |
| 3.22 | September 2016 | GNOME 3.22 applications are based on GTK 3.22, the last gtk-3.x release Wayland is now default. Comprehensive Flatpak support. GNOME Software can install and update Flatpaks, GNOME Builder can create them, and the desktop provides portal implementations to enable sandboxed applications. Improvements to core GNOME applications include support for batch renaming in Files, sharing support in GNOME Photos, an updated look for GNOME Software, a redesigned keyboard settings panel, and much more. |
| 3.24 | March 2017 | Night Light is a new feature and reduces eye strain at night by coloring the screen a little red. The date/time drop down now shows Weather information. A refined look to notifications. Gnome Calendar got a week view. Gnome Web got improvements to the experience of adding and managing bookmarks, and ships with Easy Privacy as default. The online accounts, user and printer settings panel was redesigned. |
| 3.26 | September 2017 | New look for the Settings application, which has a new navigation sidebar and improved network and display settings, and browser synchronization thanks to the Firefox Sync service. Color emoji are now supported throughout GNOME and will be visible wherever they appear. |
| 3.28 | 12 March 2018 | wiki.gnome.org/ReleasePlanning/FeaturePlans wiki.gnome.org/ThreePointTwentyseven/ReleaseNotes new application GNOME Usage new On-screen-keyboard |
| 3.30 | 5 September 2018 | release notes for GNOME 3.30.0 release announcement for GNOME 3.30.0 list of updated modules and changes for 3.30.1 release announcement for 3.30.1 release announcement for 3.30.2 list of updated modules and changes for 3.30.2 |
| 3.32 | 13 March 2019 | release notes for GNOME 3.32 release announcement for GNOME 3.32 |
| 3.34 | 12 September 2019 | release notes for GNOME 3.34 release announcement for GNOME 3.34 |
| 3.36 | 11 March 2020 | release notes for GNOME 3.36 release announcement for GNOME 3.36 |
| 3.38 | 16 September 2020 | release notes for GNOME 3.38 release announcement for GNOME 3.38 |
| 40 | 24 March 2021 | release notes for GNOME 40 website for GNOME 40 |
| 41 | 22 September 2021 | release notes for GNOME 41 Archived 22 December 2021 at the Wayback Machine release announcement for GNOME 41 Archived 21 June 2023 at the Wayback Machine |
| 42 | 23 March 2022 | Introduction of the LibAdwaita GTK libraries. Many GNOME Core Applications were ported to LibAdwaita. GNOME Text Editor replaced Gedit as the default text editor. release notes for GNOME 42 release announcement for GNOME 42 Archived 21 June 2022 at the Wayback Machine |
| 43 | 21 September 2022 | GNOME Files (Nautilus) was ported to LibAdwaita. release notes for GNOME 43 release announcement for GNOME 43 Archived 30 May 2023 at the Wayback Machine |
| 44 | 22 March 2023 | release notes for GNOME 44 release announcement for GNOME 44 Archived 24 June 2023 at the Wayback Machine |
| 45 | 20 September 2023 | Loupe replaced Eye of GNOME as the default image viewer and Snapshot replaced Cheese as the default webcam application. release notes for GNOME 45 release announcement for GNOME 45 |
| 46 | 20 March 2024 | release notes for GNOME 46 release announcement for GNOME 46 |
| 47 | 18 September 2024 | release notes for GNOME 47 release announcement for GNOME 47 |
| 48 | 19 March 2025 | Introduction of Decibels as the default audio player. release notes for GNOME 48 release announcement for GNOME 48 |
| 49 | 17 September 2025 | Papers replaced Evince as the default document viewer and Showtime replaced Totem as the default Video Player. The GNOME X.Org session support for Mutter was disabled as of this release (this can be reverted at build time for GNOME 49) with plans to start removing the X.Org/X11 session in GNOME 50. (XWayland support remains unaffected for running X11 apps in GNOME Shell on Wayland.) *"Introducing GNOME 49, "Brescia"". *release.gnome.org*. 17 September 2025. Retrieved 18 September 2025.* |
| 50 | 18 March 2026 | Parents can now monitor and set time limits for child accounts. There are several new accessibility enhancements, including global settings, and an option to reduce motion. The Document App has added a brand new annotation feature. GNOME Files (Nautilus) has several new additions, such as optimized memory usage, multiple filters, and improved batch rename. The Calendar app has received a lot of improvements, including ICS file export, region customization, and improved navigation. Settings has received numerous additions, such as a new first day of week option, color management bug fixes, and sound options have distinguished input and output. GNOME's Remote desktop has received a lot of optimizations, including hardware acceleration support, and improved support for NVIDIA drivers. Improved support for variable refresh rates, fractional scaling, improved NVIDIA support, and HDR screen sharing. release notes for GNOME 50 |


## Development

GNOME is developed by GNOME Project. GNOME development is loosely managed. Since the introduction of Discourse forum in 2019, the discussion moved from mailing lists and in October 2022, the project announced the plan to close all its public mailing lists.

GNOME developers and users gather at an annual GUADEC meeting to discuss the current state and the future direction of GNOME. GNOME incorporates standards and programs from freedesktop.org to better support interoperability with other desktops.

GNOME is mainly written in C, XML, C++, C#, HTML, Vala, Python, JavaScript, CSS, and more. A number of language bindings are available.

### Development platform

The GLib data structures and utilities library, GObject object and type system and GTK widget toolkit along with the Adwaita design language implemented by libadwaita, comprise the central part of the GNOME development platform. This foundation is further extended with D-Bus IPC framework, Cairo 2D vector-based drawing library, Cogl accelerated graphics library, Pango international text rendering library, PulseAudio and PipeWire low-level audio APIs, GStreamer multimedia framework, and several specialized libraries including NetworkManager, PackageKit, Telepathy (instant messaging), and WebKit.

- GNOME Display Manager (GDM), which manages user sessions, X and Wayland alike.
- Tracker automatically searches the specified directories for files and keeps an index of them to provide fast search; heavily integrated into GNOME Shell and GNOME Files
- GVfs, an abstraction layer framework for file systems augmenting GIO; well integrated into GNOME Files and GNOME Disks
- dconf a backend for GSettings
- Mutter, the Wayland compositor and X Window Manager
- Linux color management, udev, etc.
- Evolution Data Server, responsible for managing mail, calendar, address book, tasks and memo information
- Meson is replacing GNU Build System (autotools) as build automation tools of choice
- BuildStream, a distribution agnostic build and integration tool

### Dependencies

The GNOME desktop environment does not consist solely of the graphical control element library GTK and the core applications that make use of it. There are quite a few additional software packages that make up the GNOME desktop environment, such as the above.

#### Windowing system

GNOME runs on Wayland. Wayland support was introduced in GNOME 3.10 and deemed "for the majority of users […] a usable day to day experience" by 3.20, at which point Wayland became the default user session. With GNOME 3.24, Wayland compatibility was extended to Nvidia drivers. In GNOME 3.30 or later, it was possible to run GNOME without X11 running at startup, using only Wayland. In GNOME 50, using the X11 session in Mutter is no longer possible, and GNOME became one of the first desktop environments to only support Wayland. X11 applications can still be run though XWayland.

#### systemd

In May 2011 Lennart Poettering proposed systemd as a GNOME dependency. As systemd is available only on Linux, the proposal led to a discussion of possibly dropping support for other platforms in future GNOME releases. Since GNOME 3.2, multiseat support has only been available on systems using systemd. In November 2012 the GNOME release team concluded there will be no compile time dependency on systemd for basic functionality, like session tracking. For non-basic functionality, like power management, compile time dependency is possible. For example, there is no concept of systemd inhibitors in alternatives like consolekit. A package manager may want to ensure that the system is not turned off while the upgrade is taking place.

Since GNOME 49 systemd became a stronger dependency. Adrian Vovk had announced two major changes: GDM is gaining a dependency on systemd’s userdb infrastructure and the builtin service manager of gnome-session is being removed. "GNOME is about to gain a few strong dependencies on systemd, and this will make running GNOME harder in environments that don’t have systemd available. [...] you’ll need to implement replacements for more systemd components, similarly to what you have done with elogind and eudev."

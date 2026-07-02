---
title: "KDE Frameworks"
source: https://en.wikipedia.org/wiki/KDE_Frameworks
domain: kde-frameworks
license: CC-BY-SA-4.0
tags: kde frameworks, plasma desktop libraries, kirigami convergent ui, qt kde modules
fetched: 2026-07-02
---

# KDE Frameworks

**KDE Frameworks** is a collection of libraries and software frameworks readily available to any Qt-based software stacks or applications on multiple operating systems. Featuring frequently needed functionality solutions like hardware integration, file format support, additional graphical control elements, plotting functions, and spell checking, the collection serves as the technological foundation for KDE Plasma and KDE Gear. It is distributed under the GNU Lesser General Public License (LGPL). As of September 2025, the latest stable release is KDE Frameworks 6 (KF6).

## Overview

KDE Frameworks is based on Qt, which enables a more widespread use of QML, a simpler JavaScript-based declarative programming language, for the design of user interfaces. The graphics rendering engine used by QML allows for more fluid user interfaces across different devices.

Since the split of the KDE Software Compilation into KDE Frameworks 5, KDE Plasma 5 and KDE Applications, each sub-project can pick its own development pace. KDE Frameworks are released on a monthly basis and use Git.

It should be possible to install KDE Frameworks alongside the KDE Platform 4 so apps can use either one.

### API and ABI stability

Platform releases are those which begin a series (version number X.0). Only these major releases are allowed to break binary compatibility with the predecessor. Releases in the minor series (X.1, X.2, ...) will guarantee binary portability (API & ABI). This means, for instance, that software that was developed for KDE 3.0 will work on all (future) KDE 3 releases; however, an application developed for KDE 2 is not guaranteed to be able to make use of the KDE 3 libraries. KDE major version numbers mainly follow the Qt release cycle, meaning that KDE SC 4 is based on Qt 4, while KDE 3 was based on Qt 3.

### Supported operating systems

The repository of each framework should contain a file named *metainfo.yaml*. This file documents the maintainer of the framework, the type, the supported operating system and other information. The currently supported platforms are Linux, Microsoft Windows, macOS and Android.

## Software architecture

### Structure

The Frameworks have a clear dependency structure, divided into "categories" and "tiers". The "categories" refer to runtime dependencies:

- Functional elements have no runtime dependencies.
- Integration designates code that may require runtime dependencies for integration depending on what the OS or platform offers.
- Solutions have mandatory runtime dependencies.

### Components

The KDE Frameworks bundle consists of over 70 packages. These existed as a single large package, called kdelibs, in KDE SC 4. Kdelibs was split into several individual frameworks, some of which are no longer part of KDE but were integrated into Qt 5.2.

KDE Frameworks are grouped in four different tiers according to dependency on other libraries.

**Tiers of Frameworks**

Tier 1

–

Mostly depend only on

Qt

, highly portable

Tier 2

–

Depends on Tier 1, but dependencies are still manageable.

Tier 3

–

Complex dependencies, including Tiers 1

–

2 etc.

Tier 4

–

Can be mostly ignored by application programmers. Mostly plugins that provide additional features like platform support.

| Name | Tier | Git repository | Description |
|---|---|---|---|
| Frameworkintegration | 4 | frameworkintegration.git | Framework Integration is a set of plugins responsible for better integration of Qt applications when running on a KDE Plasma workspace. Applications do not need to link to this directly. The library KF5Style provides integration with KDE Plasma Workspace settings for Qt styles. Derive your Qt style from KStyle to automatically inherit various settings from the KDE Plasma Workspace, providing a consistent user experience. For example, this will ensure a consistent single-click or double-click activation setting, and the use of standard themed icons. |
| KActivities | 3 | kactivities.git | Core components for KDE Activities' Activity Manager. |
| KApiDox | 1 | kapidox.git | Scripts and data for building API documentation in a standard format and style. This framework contains scripts and data for building API documentation (dox) in a standard format and style. The Doxygen tool is used to do the actual documentation extraction and formatting, but this framework provides a wrapper script to make generating the documentation more convenient (including reading settings from the target framework or other module) and a standard template for the generated documentation. |
| KArchive | 1 | karchive.git | Classes for easy reading, creation and manipulation of "archive" formats including zip and tar. |
| KAuth | 2 | kauth.git | Provides a convenient, system-integrated way to offload actions that need to be performed as a privileged user to small helper utilities. |
| KBookmarks | 3 | kbookmarks.git | KBookmarks lets you access and manipulate bookmarks stored using the "XBEL format". The most common use for bookmarks is web browsers, but this can also be useful in any application where local files or URLs can be saved as bookmarks. |
| KCMUtils | 3 | kcmutils.git | Utilities, i.a. KSettings, for KDE System Settings modules. KCMUtils provides various classes to work with KCModules. KCModules can be created with the KConfigWidgets framework. |
| KCodecs | 1 | kcodecs.git | KCodecs is a string encoding library, it provides a collection of methods to manipulate strings using various encodings. It can automatically determine the charset of a string, translate XML entities, validate email addresses, and find encodings by name in a more tolerant way than QTextCodec (useful e.g. for data coming from the Internet). |
| KCompletion | 2 | kcompletion.git | String completion framework, including completion-enabled lineedit and combobox. When typing filenames, email addresses and other text where the user often wants to select from existing data (including what they previously typed) rather than enter anything wholly original, users often find it helpful if they only need to type the first few characters, and then have the application offer them a set of choices or attempt to finish off what they were typing. Email clients, shells and "open file" dialogs often provide this functionality. This framework helps implement this in Qt-based applications. You can use one of the completion-ready widgets provided by this framework, or integrate it into your application's other widgets directly. The easiest way to get started is to use a KComboBox, KHistoryComboBox or KLineEdit. If you want to integrate completion into other parts of the user interface, you can use KCompletion to manage and select the possible completions. |
| KConfig | 1 | kconfig.git | Persistent platform-independent application settings made of two parts: KConfigCore and KConfigGui. KConfigCore provides access to the configuration files themselves, meaning it also generates the configuration in XML. KConfigGui provides a way to hook graphical control elements (widgets) to the configuration so that they are automatically initialized from the configuration and automatically propagate their changes to their respective configuration files. |
| KConfigWidgets | 3 | kconfigwidgets.git | Graphical control elements (widgets) for configuration dialogs. Widgets for configuration dialogs. KConfigWidgets provides easy-to-use classes to create configuration dialogs, as well as a set of widgets which uses KConfig to store their settings. |
| KCoreAddons | 1 | kcoreaddons.git | Utilities for core application functionality and accessing the OS. Qt addon library with a collection of non-GUI utilities. KCoreAddons provides classes built on top of QtCore to perform various tasks such as manipulating mime types, autosaving files, creating backup files, generating random sequences, performing text manipulations such as macro replacement, accessing user information and many more. |
| KCrash | 2 | kcrash.git | Provides support for intercepting and handling application crashes. |
| KDBusAddons | 1 | kdbusaddons.git | KDBusAddons provides convenience DBus classes on top of QtDBus, as well as an API to create KDED modules. |
| KDeclarative | 3 | kdeclarative.git | Addon for Qt declarative |
| KDED | 3 | kded.git | KDED stands for KDE Daemon, the central daemon of KDE work spaces. KDED runs in the background and performs a number of small tasks. Some of these tasks are built in, others are started on demand. |
| KDesignerPlugin | 3 | kdesignerplugin.git | This framework provides plugins for Qt Designer that allow it to display the widgets provided by various KDE frameworks, as well as a utility (kgendesignerplugin) that can be used to generate other such plugins from ini-style description files. |
| KDESu | 3 | kdesu.git | KDESU (KDE super user) provides a user interface for running shell commands with root privileges. It provides functionality for building GUI front ends for (password asking) console mode programs. For example, kdesu and kdessh use it to interface with su and ssh respectively. |
| KDEWebkit | 3 | kdewebkit.git | Integration of the HTML rendering engine WebKit. The KDEWebkit library provides KDE integration of the QtWebKit library. If you are using QtWebKit in your KDE application, you are encouraged to use this layer instead of using the QtWebKit classes directly. In particular, you should use KWebView in place of QWebView, KGraphicsWebView in place of QGraphicsWebView and KWebPage in place of QWebPage. |
| KDNSSDFramework | 2 | kdnssd.git | KDNSSD is a library for handling the DNS-based Service Discovery Protocol (DNS-SD), the layer of [Zeroconf] (www.zeroconf.org) that allows network services, such as printers, to be discovered without any user intervention or centralized infrastructure. |
| KDocTools | 2 | kdoctools.git | Provides tools to generate documentation in various format from DocBook files. |
| KEmoticons | 3 | kemoticons.git | Provides emoticons themes as well as helper classes to automatically convert text emoticons to graphical emoticons. |
| KGlobalAccel | 1 | kglobalaccel.git | KGlobalAccel allows you to have global keyboard shortcuts (accelerators) that are independent of the focused window. Unlike regular shortcuts, the application's window does not need focus for them to be activated. |
| KGuiAddons | 1 | kguiaddons.git | KDE GUI Addons; Utilities for graphical user interfaces; The KDE GUI addons provide utilities for graphical user interfaces in the areas of colors, fonts, text, images, keyboard input. |
| KHTML | 4 | khtml.git | KHTML is the HTML rendering engine from which WebKit was forked. It is based on the KParts technology and uses KJS for JavaScript support. |
| Ki18n | 1 | ki18n.git | KDE gettext-based UI text internationalization. KI18n provides functionality for internationalizing user interface text in applications, based on the GNU Gettext translation system. It wraps the standard Gettext functionality, so that the programmers and translators can use the familiar Gettext tools and workflows. KI18n provides additional functionality as well, for both programmers and translators, which can help to achieve a higher overall quality of source and translated text. This includes argument capturing, customizable markup, and translation scripting. |
| KIconThemes | 3 | kiconthemes.git | This library contains classes to improve the handling of icons in applications using the KDE Frameworks. |
| KIdleTime | 1 | kidletime.git | Integration module for idle time detection. |
| KImageFormats | 1 | kimageformats.git | Plugins to allow QImage to support extra file formats. This framework provides additional image format plugins for QtGui. As such it is not required for the compilation of any other software, but may be a runtime requirement for Qt-based software to support certain image formats. The following image formats have read-only support: GIMP (xcf) OpenEXR (exr) Adobe Photoshop documents (psd) Sun Raster (ras) The following image formats have read and write support: Encapsulated PostScript (eps) Personal Computer Exchange (pcx) SGI images (rgb, rgba, sgi, bw) Autodesk Softimage (pic) Targa (tga): supports more formats than Qt's version XView (xv) <--! Khoros Visualization Image file? --> |
| KInit | 3 | kinit.git | kdeinit is a process launcher, that launches processes by forking and then loading a dynamic library which should contain a 'kdemain(...)' function. kdeinit speeds up start of applications on KDE workspaces; kdeinit is linked against all libraries a standard KDE application needs. With this technique starting an application becomes much faster because now only the application itself needs to be linked whereas otherwise both the application as well as all the libraries it uses need to be linked. |
| KIO | 3 | kio.git | Network transparent access to files and data. This framework implements almost all the file management functions you will ever need. Dolphin and the KDE file dialog also uses this to provide its network-enabled file management. |
| Kirigami | 1 | kirigami.git | A set of QtQuick plugins to build user interfaces based on the KDE UX guidelines |
| KItemModels | 1 | kitemmodels.git | Set of item models extending the Qt model-view framework. KItemModels provides the following models: KBreadcrumbSelectionModel - Selects the parents of selected items to create breadcrumbs KCheckableProxyModel - Adds a checkable capability to a source model KConcatenateRowsProxyModel - Concatenates rows from multiple source models KDescendantsProxyModel - Proxy Model for restructuring a Tree into a list KExtraColumnsProxyModel - Adds columns after existing columns KLinkItemSelectionModel - Share a selection in multiple views which do not have the same source model KModelIndexProxyMapper - Mapping of indexes and selections through proxy models KRearrangeColumnsProxyModel - Can reorder and hide columns from the source model KRecursiveFilterProxyModel - Recursive filtering of models KSelectionProxyModel - A Proxy Model which presents a subset of its source model to observers |
| KItemViews | 1 | kitemviews.git | Set of item views extending the Qt model-view framework. KItemViews includes a set of views, which can be used with item models. It includes views for categorizing lists and to add search filters to flat and hierarchical lists. |
| KJobWidgets | 2 | kjobwidgets.git | KJobWIdgets provides widgets for showing progress of asynchronous jobs. |
| KJS | 1 | kjs.git | KJS provides an ECMAScript compatible interpreter. The ECMA standard is based on well known scripting languages such as Netscape's JavaScript and Microsoft's JScript. |
| KJSEmbed | 3 | kjsembed.git | KSJEmbed provides a method of binding JavaScript objects to QObjects, so you can script your applications. |
| KMediaPlayer | 3 | kmediaplayer.git | *Deprecated*: Interface for media player KParts. KMediaPlayer builds on the KParts framework to provide a common interface for KParts that can play media files. This framework is a porting aid. It is not recommended for new projects, and existing projects that use it are advised to port away from it, and use plain KParts instead. |
| KNewStuff | 3 | knewstuff.git | Framework for downloading and sharing additional application data. The KNewStuff library implements collaborative data sharing for applications. It uses libattica to support the Open Collaboration Services specification. Attica is a Qt library that implements the Open Collaboration Services API version 1.6. It grants easy access to the services such as querying information about persons and contents. |
| KNotifications | 3 | knotifications.git | Solution with abstraction for system notifications. |
| KNotifyConfig | 3 | knotifyconfig.git | Module for KNotify configuration. |
| KParts | 3 | kparts.git | The KParts library implements the framework for KDE parts. One individual user interface component is called a *KPart* and is some elaborate widget with a user-interface defined in terms of actions (menu items, toolbar icons). KParts are analogous to Bonobo components in GNOME and ActiveX controls in Microsoft's Component Object Model. Konsole is available as a KPart and is used in applications like Konqueror and Kate. Example uses of KParts: Konqueror uses the Okular part to display documents Konqueror uses the Dragon Player part to play multimedia Kontact embeds kdepim applications Kate and other editors use the katepart editor component Several applications use the Konsole KPart to embed a terminal Further documentation: Creating and Using Components (KParts) (from KDE) Writing Plugins For KDE Applications (from KDE) |
| KPlotting | 1 | kplotting.git | KPlotWidget is a QWidget-derived class that provides a virtual base class for easy data-plotting. The idea behind KPlotWidget is that you only have to specify information in "data units"; i.e., the natural units of the data being plotted. KPlotWidget automatically converts everything to screen pixel units. KPlotWidget draws X and Y axes with tick marks and tick labels. It automatically determines how many tick marks to use and where they should be, based on the data limits specified for the plot. You change the limits by calling `setLimits(double x1, double x2, double y1, double y2)`. Data to be plotted are stored using the KPlotObject class. KPlotObject consists of a QList of QPointF's, each specifying the X,Y coordinates of a data point. KPlotObject also specifies the "type" of data to be plotted (POINTS or CURVE or POLYGON or LABEL). |
| KPty | 2 | kpty.git | Interfacing with pseudo terminal devices. This library provides primitives to interface with pseudo terminal devices as well as a KProcess derived class for running child processes and communicating with them using a pty. |
| Kross | 3 | kross.git | Embedding of scripting into applications. Kross is a scripting bridge to embed scripting functionality into an application. It supports QtScript as a scripting interpreter back-end. The core of Kross provides the framework to deal transparently with interpreter-back-ends and offers abstract functionality to deal with scripts. |
| KRunner | 3 | krunner.git | Framework for providing different actions given a string query. Framework for Plasma runners. The Plasma workspace provides an application called KRunner which, among other things, allows one to type into a text area which causes various actions and information that match the text appear as the text is being typed. One application for this is the universal runner you can launch with ALT+F2. |
| KService | 3 | kservice.git | KService provides a plugin framework for handling desktop services. Services can be applications or libraries. They can be bound to MIME types or handled by application specific code. |
| KSyntaxHighlighting | 1 | syntax-highlighting.git | This is a stand-alone implementation of the Kate syntax highlighting engine. It's meant as a building block for text editors as well as for simple highlighted text rendering (e.g. as HTML), supporting both integration with a custom editor as well as a ready-to-use QSyntaxHighlighter sub-class. |
| KTextEditor | 3 | ktexteditor.git | KTextEditor provides a powerful text editor component that you can embed in your application, either as a KPart or using the KF5::TextEditor library (if you need more control). The text editor component contains many useful features, from syntax highlighting and automatic indentation to advanced scripting support, making it suitable for everything from a simple embedded text-file editor to an advanced IDE. |
| KTextWidgets | 3 | ktextwidgets.git | KTextWidgets provides widgets for displaying and editing text. It supports rich text as well as plain text. |
| KUnitConversion | 2 | kunitconversion.git | KUnitConversion provides functions to convert values in different physical units. It supports converting different prefixes (e.g. kilo, mega, giga) as well as converting between different unit systems (e.g. liters, gallons). The following areas are supported: Acceleration Angle Area Currency Density Electrical Current Electrical Resistance Energy Force Frequency Fuel efficiency Length Mass Power Pressure Temperature Thermal Conductivity Thermal Flux Thermal Generation Time Velocity Volume Voltage |
| KWalletFramework | 3 | kwallet.git | Safe desktop-wide storage for passwords. This framework contains two main components: Interface to KWallet, the safe desktop-wide storage for passwords on KDE work spaces. The kwalletd used to safely store the passwords on KDE work spaces. |
| KWayland | 1 | kwayland.git | KWayland is the KDE library for implementing Wayland support in KDE applications, it fulfills needs beyond what QtWayland provides. All the KDE applications in a plasma-wayland-session use this library and LXQt maybe as well. KWayland has been part of KDE Frameworks since 5.22 (May 2016); it was formerly distributed as part of KDE Plasma 5. |
| KWidgetsAddons | 1 | kwidgetsaddons.git | Addon with various classes on top of QtWidgets. If you are porting applications from KDE Platform 4 "kdeui" library, you will find many of its classes here. Provided are action classes that can be added to toolbars or menus, a wide range of widgets for selecting characters, fonts, colors, actions, dates and times, or MIME types, as well as platform-aware dialogs for configuration pages, message boxes, and password requests. Further widgets and classes can be found in other KDE frameworks. |
| KWindowSystem | 1 | kwindowsystem.git | Allows to interact with the windowing system. It provides a NETRootInfo for accessing the global state (all that's set on the root window) and NETWinInfo for all information about a specific window. The classes have a window manager and client perspective. This is the foundation which powers KWin and various parts of the graphical shell such as the taskmanager. On top of those X11-specific classes we have a convenient API KWindowInfo and KWindowSystem which provides a windowing system independent API for our applications. |
| KXMLGUI | 3 | kxmlgui.git | KXMLGUI provides a framework for managing menu and toolbar actions in an abstract way. The actions are configured through a XML description and hooks in the application code. The framework supports merging of multiple description for example for integrating actions from plugins. KXMLGui makes use of the Kiosk authorization functionality of KConfig (see the KAuthorized namespace in that framework). Notably, QAction instances added to a KActionCollection are disabled if KAuthorized::authorizeAction() reports that they are not authorized. The items on the standard help menu (KHelpMenu) can likewise be disabled based on Kiosk settings, and toolbar editing can be restricted. See KActionCollection, KHelpMenu and KToolBar documentation for more information. |
| Plasma-framework | 3 | plasma-framework.git | Foundational libraries, runtime components and tools of the KDE Plasma workspaces based upon KF5 and Qt5. The plasma framework provides the following: QML components org.kde.plasma.core: bindings for libplasma functionality, such as DataEngine and FrameSvg org.kde.plasma.components: graphical components for common items such as buttons, lineedits, tabbars and so on. Compatible subset of the MeeGo components used on the N9 org.kde.plasma.extras: Extra graphical components that extend org.kde.plasma.components but are not in the standard API org.kde.plasma.plasmoid: Attached properties for manipulating the current applet or containment libplasma: a C++ library that provides: rendering of SVG themes loading of files from a certain filesystem structure: packages data access through data engines loading of the plugin structure of the workspace: containments and applets Script engines: Provides support to create applets or containments in various scripting languages |
| Prison | 1 | prison.git | Prison is a Qt-based barcode abstraction layer/library and provides uniform access to generation of barcodes with data. |
| Solid | 1 | solid.git | Solid provides a way of querying and interacting with hardware independently of the underlying operating system. It provides the following features for application developers: Hardware Discovery Power Management Network Management Screen Management makes use of KScreen a new KDE Plasma 5 component |
| Sonnet | 1 | sonnet.git | Sonnet is a plugin-based spell checking library for Qt-based applications. It supports several different plugins, including HSpell, Enchant, ASpell and HUNSPELL. It also supports automated language detection, based on a combination of different algorithms. The simplest way to use Sonnet in your application is to use the SpellCheckDecorator class on your QTextEdit. |
| Syndication | 2 | syndication.git | Syndication is an RSS/Atom parser library. |
| ThreadWeaver | 1 | threadweaver.git | ThreadWeaver is a Job queue. It executes jobs in threads it internally manages. |

#### Kirigami

Kirigami is a QML application framework developed by Marco Martin that enables developers to write applications that run natively on Android, iOS, Windows, Plasma Mobile and any classic Linux desktop environment without code adjustments.

It is used by various applications, for example Linus Torvalds and Dirk Hohndels' scuba diving application Subsurface, the messenger client Banji, the Kaidan messenger, Vvave music player and the KDE software center Discover.

#### Software packages

Linux distribution use some package management system to package the software they distribute. Debian for example distributes *KGlobalAccel* under the package name *libkf5globalaccel*, while Fedora Linux distributes it under the name *kf5-kglobalaccel*.

### Bindings

While being mainly written in C++, there are bindings for other programming languages available:

- Python invent.kde.org/teams/goals/streamlined-application-development-experience/-/issues/9

These and other bindings use the following technologies:

- Qt for Python: doc.qt.io/qtforpython-6

## History

The 5.0 release was preceded by a technology preview, two alpha releases, and three beta releases.

The source code of KDE Frameworks has been around since KDElibs 1. The first release as *KDE Frameworks* was with version 5, to account for the fact that the code base was that of KDE Platform version 4 (the only major version of KDE Platform).

The transition from KDE Platform to KDE Frameworks began in August 2013, guided by top KDE technical contributors.

After the initial release of KDE Frameworks 5.0, the developers focused on adding new features to the components in KDE Frameworks 5, an example being better integration of Firefox into KDE.

The major improvement of Frameworks 5 is its modularization. In earlier KDE versions, the libraries were bundled as a single large package. In Frameworks, the libraries were split into individual smaller packages. This facilitates utilization of the libraries by other Qt-based software, since dependencies can be kept at a minimum.

While KDE 4 was based on version 4 of the Qt widget toolkit, Frameworks 5 is based on version 5.

As part of the KDE project's 'MegaRelease 6', on February 28, 2024, KDE Frameworks 6 was released, upgrading it to a Qt 6 base.

### KDE4 transformation

During KDE SC 4, the then so called KDE Platform consisted of all libraries and services needed for KDE Plasma and the applications. Starting with Qt 5, this platform was transformed into a set of modules that is now referred to as KDE Frameworks. These modules include: Solid, Nepomuk, Phonon, etc. and are licensed either under the LGPL, BSD license, MIT License or X11 license.

## Adoption

Besides the KDE Software Compilation, there are other adopters such as the desktop environments LXQt, MoonLightDE or Hawaii.

Version 3.0 of Krita, the raster graphics editor of the Calligra Suite, which was released on May 31, 2016, depends on KDE Frameworks 5 and Qt 5.2.

With Kirigami, there is also increased usage by applications such as Amarok, Avogadro, Trojitá or Subsurface.

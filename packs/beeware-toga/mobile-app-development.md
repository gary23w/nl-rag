---
title: "Mobile app development"
source: https://en.wikipedia.org/wiki/Mobile_app_development
domain: beeware-toga
license: CC-BY-SA-4.0
tags: beeware toga, native python widgets, toga cross-platform, python native app
fetched: 2026-07-02
---

# Mobile app development

**Mobile app development** is the act or process by which a mobile app is developed for one or more mobile devices, which can include personal digital assistants (PDA), enterprise digital assistants (EDA), or mobile phones. Such software applications are specifically designed to run on mobile devices, after considering many hardware constraints. Common constraints include central processing unit (CPU) architecture and speeds, available random-access memory (RAM), limited data storage capacities, and considerable variation in displays (technology, size, dimensions, resolution) and input methods (buttons, keyboards, touch screens with or without styluses). These applications (or 'apps') can be pre-installed on phones during manufacturing or delivered as web applications, using server-side or client-side processing (e.g., JavaScript) to provide an "application-like" experience within a web browser.

The mobile app development sector has experienced significant growth in Europe. A 2017 report from the Progressive Policy Institute estimated there were *1.89 million jobs* in the *app economy* across the European Union (EU) by January 2017, marking a 15% increase from the previous year. These jobs include roles such as mobile app developers and other positions supporting the app economy.

## Overview

To facilitate developing applications for mobile devices, and the consistency thereof, various approaches have been taken.

Most companies that ship a product (e.g., Apple, iPod/iPhone/iPad) provide an official software development kit (SDK). They may also opt to provide some form of software testing and/or quality assurance (QA). In exchange for being provided the SDK or other tools, it may be necessary for a prospective developer to sign some form of non-disclosure agreement (NDA), which restricts the sharing of privileged information.

As part of the development process, mobile user interface (UI) design is an essential step in the creation of mobile apps. Mobile UI designers consider constraints, contexts, screen space, input methods, and mobility as outlines for design. Constraints in mobile UI design, which include the limited attention span of the user and form factors such as a mobile device's screen size for a user's hand(s). Mobile UI context includes signal cues from user activity, such as the location where or the time when the device is in use, that can be observed from user interactions within a mobile app. Such context clues can be used to provide automatic suggestions when scheduling an appointment or activity or to filter a list of various services for the user.

The user is often the focus of interaction with their device, and the interface entails components of both hardware and software. User input allows for the users to manipulate a system, and the device's output allows the system to indicate the effects of the users' manipulation.

Overall, mobile UI design's goal is mainly for an understandable, user-friendly interface. Functionality is supported by mobile enterprise application platforms or integrated development environments (IDEs).

Developers of mobile applications must also consider a large array of devices with different screen sizes, hardware specifications, and configurations because of intense competition in mobile hardware and changes within each of the platforms.

Today, mobile apps are usually distributed via an official online outlet or marketplace (e.g., Apple: The App Store – Google: Google Play) and there is a formalized process by which developers submit their apps for approval and inclusion in those marketplaces. Historically, however, that was not always the case.

Mobile UIs, or front-ends, rely on mobile back-ends to support access to enterprise systems. The mobile back-end facilitates data routing, security, authentication, authorization, working off-line, and service orchestration. This functionality is supported by a mix of middleware components, including mobile app servers, mobile backend as a service (MBaaS), and service-oriented architecture (SOA) infrastructure.

## Platform

The software development packages needed to develop, deploy, and manage mobile apps are made from many components and tools which allow a developer to write, test, and deploy applications for one or more target platforms.

### Front-end development tools

Front-end development tools are focused on the user interface and user experience (UI-UX) and provide the following abilities:

- UI design tools
- SDKs to access device features
- Cross-platform accommodations/support

Notable tools are listed below.

#### First party

First party tools include official SDKs published by, or on behalf of, the company responsible for the design of a given hardware platform (e.g., Apple, Google, etc.), and any third-party software that is officially supported for the purpose of developing mobile apps for that hardware.

| Platform | Programming language | Debuggers available | Emulator available | Integrated development environment available | Cross-platform deployment | Installer packaging options | Development tool cost |
|---|---|---|---|---|---|---|---|
| Android | Java but portions of code can be in C, C++, Kotlin | Debugger integrated in Eclipse, standalone debugging monitor available | Yes | Eclipse, IntelliJ IDEA, Android Studio, Project Kenai Android plugin for NetBeans | Android only, because of Dalvik VM, March 2009 | apk | Free, IntelliJ IDEA Community Edition - Free |
| BlackBerry | Java | Debugger integrated in IDE | Yes | Eclipse, BlackBerry JDE | BlackBerry only, because of RIM API | alx, cod | Free |
| iOS SDK | Objective-C, Swift | LLDB debugger integrated in Xcode IDE | Bundled with iPhone SDK, integrated with Xcode IDE | Xcode | iPhone, iPad, iPod Touch | Only via App Store, needs review and approval by Apple Inc. | Apple tools are available for free for development on Mac. Applications can be run in a simulator or on a device. Some advanced abilities need a paid developer account. |
| iOS SDK | Object Pascal | Debugger integrated in Xcode IDE | Included in Delphi XE2 professional or higher | Embarcadero Delphi XE2 | iPhone, iPad, iPod Touch | Only via App Store, needs review and approval by Apple Inc. | Development requires Intel-based Mac besides the IDE on Windows. Design is on Windows. Compiling and deploying is on Mac. Simulator testing is free, but installing on a device needs a fee for a developer signing key |

#### Second party

| Platform | Programming language | Debuggers available | Emulator available | Integrated development environment available | Cross-platform deployment | Installer packaging options | Development tool cost |
|---|---|---|---|---|---|---|---|
| Java ME | Java | Yes | Free emulator, Sun Java Wireless Toolkit, mpowerplayer | Eclipse, LMA NetBeans Mobility Pack | Yes although many VM implementations have device specific bugs necessitating separate builds | Jad/Jar packaging; PRC files under Palm OS | Free |

#### Third party

| Platform | Programming language | Debuggers available | Emulator available | Integrated development environment available | Cross-platform deployment | Installer packaging options | Development tool cost |
|---|---|---|---|---|---|---|---|
| MobileTogether | XPath/XQuery, Action Trees visual programming language | Yes | Yes | Proprietary IDE on Windows only | Android, iOS, Windows, browser | The native distribution for each format | Free |
| App Inventor for Android | Visual blocks-based programming language, with Interface designer | Limited debugging tools built into IDE | Yes | Web-based interface designer, with connection to Java web-start program for blocks programming | Android devices | apk | Free |
| Appcelerator | JavaScript | Yes, in Titanium Studio. | Emulator is available using native emulators | Titanium Studio based on Eclipse | Android, iPhone; BlackBerry, Tizen, mobile web | The native distribution format of each platform | Free, open-sourced Apache 2.0 licensed, commercial and enterprise licenses available |
| Basic4android | Visual Basic similar syntax | Yes | Emulator is available using native emulators | Proprietary IDE | Android | The native distribution format of each platform | Commercial licenses available |
| Codename One | Java | Yes | Yes | Eclipse, Netbeans | Android, iPhone, BlackBerry, Windows Mobile, J2ME | The native distribution format of each platform | Open Source GPLv2 and subscription-based build server |
| Solar2D | Lua | Yes | Yes | Xcode | Android, iOS, Nook Color | Native deployment for each platform | Free using MIT license |
| DragonRAD | Visual drag & drop tiles | Yes | Uses third-party emulators | Proprietary IDE | Android, BlackBerry, Windows Mobile | OTA deployment | Free & commercial licenses available |
| GeneXus for Mobile and Smart Devices | Knowledge representation and declarative programming-modeling for easy development, then code is automatically generated for each platform | GeneXus utilizes pre-tested code libraries and user debugging of code not necessary after code generation. | Publish in the cloud, test native in the device, no emulator needed | Proprietary IDE | Android, iOS (iPhone, iPad), BlackBerry OS, and even HTML5 if needed | The native distribution format of each platform and also cloud-browser-based | Free to try, commercial and enterprise licenses available |
| IBM MobileFirst Studio | HTML5, CSS3, JavaScript, and native SDK languages w/ Native Worklight API | Yes, Mobile Browser Simulator or integration with Native SDK Debugger | Emulator is available using native emulators or Browser Simulator w/ Cordova Plugin | Eclipse plugin, Eclipse-based stand-alone | Android, iOS, BlackBerry 6,7, & 10, Windows Phone 7.5 & 8, Windows 8 (desktop, tablets), Adobe AIR, Mobile Web App, desktop browser web page | The native distribution format of each platform | Developer edition free via Eclipse Marketplace, commercial license for deployment |
| Lazarus | Object Pascal | Yes, can debug in IDE via ActiveSync for Windows CE | Uses the emulators of the platforms | Lazarus IDE, including integrated GUI designer and debugger | Compiled language available for Windows CE, Linux-based devices, Symbian port in development | The native distribution format of each platform | Free |
| LambdaNative | Scheme | No | No but can build and test on the localhost | Eclipse (software) (optional) | All native binaries: Android, iOS, BlackBerry 10, Windows, OS X, Linux, OpenBSD, OpenWrt | The native distribution format of each platform | Free (BSD license) |
| LiveCode | LiveCode | Yes (integrated into IDE) | Yes (iOS and Android emulators may be used) | Yes | iOS, Android, macOS, Windows, Linux, server, HTML5. Installer packaging | The native distribution format of each platform | free open-source edition, commercial and enterprise editions available |
| Macromedia Flash Lite | ActionScript | Yes | Bundled with IDE | Macromedia Flash MX2004/8, Eclipse | Yes | SIS-CAB deployment or OTA-IR-Bluetooth SWF files | Varies, free but limited with MTASC |
| Marmalade | C, C++ | Yes | Yes | Visual Studio, Xcode | All native: Android, BlackBerry, BREW, iOS (iPhone), Maemo, Palm-webOS, Samsung bada, Symbian, Windows Mobile 6.x and desktop, OS X | The native distribution format of each platform | Commercial licenses available |
| Monaca | HTML5, CSS, JavaScript | Yes | Preview is available on cloud IDE and local tool | Cloud-based IDE, Visual Studio, third-party IDE/editors | Android, iOS, windows8.1, 10 | The native distribution format of each platform | Free, up to 3 projects. Commercial and enterprise license available |
| Mono for Android | C# | Yes | Yes | Visual Studio 2005 and MonoDevelop | Android | The native distribution format of the platform |   |
| MonoTouch | C# | Yes | Yes | Visual Studio 2005 and MonoDevelop | iOS | The native distribution format of the platform |   |
| MoSync | C, C++, Lua, HTML5, CSS, JavaScript | Yes | Yes | Eclipse, Visual Studio 2005 and later, MoBuild w/ text editors | Android, iOS (iPhone), Java ME, Moblin, Smartphone 2003, Symbian, Windows Mobile (Pocket PC), Blackberry (experimental) | SIS, CAB, JAD, JAR, APK, OTA deployment | Free, GPL 2.0, Free Indie Subscription; commercial subscription available |
| NetBeans | C++, Java | Yes | Yes | Java development tools | Android (Mobile and Tablet), Nokia (Symbian, Seria 60 – 40 – 80), etc... |   | Free |
| OpenPlug | ActionScript, XML | Yes | Yes | OpenPlug ELIPS plugin for Adobe Flash Builder | Android, iOS (iPad, iPhone, iPod Touch), Symbian, Windows Mobile | The native distribution format of each platform | Free & commercial licenses available |
| OutSystems | OutSystems, CSS, JavaScript | Yes | Test directly in browser | OutSystems Service Studio | Android, iOS, Windows Phone 7 | NA | Free community edition for personal use, or subscription licensing for commercial use |
| PhoneGap and Apache Cordova | HTML, CSS, JavaScript | Yes | Yes A lot of functionality can be tested directly in browser. Running native emulators on iOS and Android is also possible. | Yes Many IDEs exist for Cordova-based tools like Ionic Studio or Appery.io | iPhone, Android, Tizen, Windows Phone, BlackBerry, Symbian, Palm, Bada | The native distribution format of each platform | Apache 2 |
| Qt SDK | C++, QML | Yes | Yes | Qt Creator | Android (technology preview), iOS (technology preview), Symbian, Maemo, MeeGo, Linux, Windows, OS X | The native distribution format of each platform | Free and commercial licenses available |
| Rhomobile | Ruby with HTML interface features compiled through an interpreter into native applications | Yes | N/A, applications can run in Win32 runner, or in device emulators for supported platforms. | Xcode or Eclipse, on-demand RhoHub version includes full IDE | Yes, supports Android 1.6+, iOS 3.0+ (iPhone, iPad), Windows Mobile 6.1 Professional, Windows Mobile 6.0 Standard, BlackBerry 4.6, 4.7, 5.0, 6.0 (4.2 and 4.5 supported but database access is very slow on these devices), Symbian | OTA deployment, iOS through App store, .SIS, .CAB, .APK, .COD | Rhodes is free and open source under the MIT License, RhoSync is under GPL or commercial, Commercial support available. Subscription for RhoHub |
| RubyMotion | Ruby | Yes | Yes | Any text editor. As an IDE, RubyMine. | Android, iOS | The native distribution format of the platform | RubyMotion is a commercial product. |
| Sencha Touch | HTML, CSS, JavaScript | Yes | Yes | Sencha Architect 2 | Android, iOS (iPhone, iPad, iPod touch), Kindle, BlackBerry, Bada | Web delivered, or hybrid via native shells for each platform | GPLv3, free for commercial, paid for OEM and embedded systems |
| Smartface | WYSIWYG design editor with JavaScript code editor | Yes | Yes | Smartface IDE and SDK | Yes Android, iOS (iPhone, iPad, iPod touch), Kindle, Gear, Google Glass | The native distribution format of each platform | Community license and commercial licenses available |
| Stencyl | Drag-and-drop editor based on Scratch, Objective-C | Yes | Yes | Xcode | iOS (iPad, iPhone, iPod Touch) | The native distribution format of each platform | Free and commercial development licenses |
| Telerik Platform, and AppBuilder | HTML5, CSS and Javascript | Yes | Test right in browser or device | In-browser client, desktop client, Visual Studio, Sublime Text or command-line interface (CLI) | Android, iOS, Windows phone | The native distribution format of each platform | Free to try, commercial and enterprise licenses available |
| Unity | C#, JavaScript, Boo, other .NET-based languages | Yes | Remote used to simulate device interaction before app is uploaded to the device. | Unity Editor, also works with Visual Studios and MonoDevelop. | Android, iOS (iPhone, iPad), PC, Mac, desktop browser, Xbox 360, PS3, Wii. BlackBerry Playbook, Nokia Symbian, Roku 2 and others available through company's Union program. | Native distribution format of each platform | Free and commercial development licenses. |
| Verivo AppStudio | WYSIWYG, graphical drag and drop, JavaScript, .NET-based languages; replaced by Appery.io | Yes | Test right in browser or device | Proprietary design studio | Android, iOS, Blackberry | Native distribution format of each platform | Free development licenses; per-CPU deployment licenses |
| ViziApps | WYSIWYG, graphical drag and drop | Yes | Test right in browser or device | Online design studio | Android, iOS, Windows Phone planned | The native distribution format of each platform | Free to design, test, demo, update, app; fee to publish |
| V-Play Engine | Objective-C, C++, JavaScript, QML, Java | Yes | Yes | Qt Creator | All Platforms | The native distribution format of each platform | Free, Indie and Enterprise licenses are available |
| Xamarin | C# | Yes | Yes | Xamarin Studio (Mac only; deprecated), Visual Studio (Windows only), Visual Studio for Mac (Mac only; replaced Xamarin Studio) | Android, iOS, Windows Phone, Windows Store apps | The native distribution of each platform | Free community edition, pro edition included in Microsoft MSDN licensing |
| Xojo | Xojo (similar to VB) | Yes | Yes | Xojo IDE | iOS, mobile web apps | iOS apps are native iPad | Free trial with no time limit; commercial licenses available |

### Back-end servers

Back-end tools pick up where the front-end tools leave off, and provide a set of reusable services that are centrally managed and controlled and provide the following abilities:

- Integration with back-end systems
- User authentication-authorization
- Data services
- Reusable business logic

Available tools include:

| Platform | Programming language | Integrated development environment available | Cross-platform deployment | Deployment options | Development tool cost |
|---|---|---|---|---|---|
| Altova MobileTogether Server | Browser-based interface | Proprietary IDE | Server available for Windows, Linux, macOS. Supports mobile devices running Android, iOS, Windows 8, Windows 10 Windows Phone, HTML5 browser-based client | On-prem, cloud, or hybrid | Development tools are free, commercial license needed for deployment |
| Metismo | Java | Eclipse | Android, iOS (iPhone, iPad), Java ME, BREW, BlackBerry, Nintendo DS, Palm/webOS, Sony PSP, Samsung bada, Symbian, Windows Mobile, Windows Phone 7, Windows Desktop, OS X | On-prem | Commercial licenses available |
| Verivo Akula | Java | Use any front-end IDE | Android, iOS (iPhone, iPad), Windows Phone7 | On-prem, cloud, or hybrid | Free development licenses; per-CPU deployment licenses. Replaced by Appery.io |

### Security add-on layers

With bring your own device (BYOD) becoming the norm within more enterprises, IT departments often need stop-gap, tactical solutions that layer atop existing apps, phones, and platform component. Features include

- App wrapping for security
- Data encryption
- Client actions
- Reporting and statistics

### System software

Many system-level components are needed to have a functioning platform for developing mobile apps.

| Platform | Programming language | Debuggers available | Emulator available | Integrated development environment available | Cross-platform deployment | Installer packaging options | Development tool cost |
|---|---|---|---|---|---|---|---|
| Adobe AIR | ActionScript, HTML, CSS, JavaScript | Yes | Yes | Flash Builder, Flash Professional, IntelliJ IDEA | Android, iOS (iPhone, iPad, iPod touch), BlackBerry | The native distribution format of each platform | Flash Builder, Flash Professional, IntelliJ IDEA - commercial licenses available Adobe AIR SDK (command line tool) - Free |
| BREW | C; the APIs are provided in C with a C++ style interface | Debugger support for the native ARM target code. Can use Visual Studio to debug the x86 testing code | No Emulator for the target ARM code, has a simulator for the x86 testing code | Visual Studio 6.0, Visual Studio 2003 .NET, Visual Studio 2005 | Compile for the specific BREW version available on the handset | OTA | Related dev fees typically needed for Brew App Certification - VeriSign annual fee for becoming a certified developer. Realview ARM compiler for BREW (the free GNU C/C++ is available, but with limited function and support). TRUE BREW testing fee for distributing the application. |
| Firefox OS | HTML5, CSS, JavaScript | Yes | No, but simulator available. | Firefox browser, Firebug | Web browser on other platform | Firefox Marketplace, Web URL | Development requires Mozilla Firefox and the simulator add-on |
| .NET Compact Framework | C#, VB.NET, Basic4ppc | Yes | Free emulator, source code available, also bundled with IDE | Visual Studio 2008, 2005, 2003, Basic4ppc IDE | Windows Mobile, Windows CE, Symbian-based devices via third-party tools | OTA deployment, CAB files, ActiveSync | Most tools free, but commercial editions of Visual Studio needed for visual designers |
| OpenFL | Haxe (similar to Actionscript and Java) | Yes | Yes | IntelliJ IDEA, FlashDevelop | Android, iOS (iPhone, iPad, iPod touch), BlackBerry Playbook, WebOS, HTML5, Flash, Windows (exe), Linux | The native distribution format of each platform | Free |
| Palm OS | C, C++, Pascal | Yes | OS 1.0–4.1: free emulator provided by PalmSource (Access); OS 5.0: - 5.4 device-specific simulators provided by Palm (palmOne) | Palm OS Development System (Eclipse), CodeWarrior, PocketStudio, HB++, Satellite Forms | Palm OS handhelds, or Windows Mobile with StyleTap emulator | PRC files, PalmSource Installer (.psi) | Free (POSE or GCC for Palm OS), or commercial (CodeWarrior), or various commercial rapid-development frameworks |
| Python | Python | Yes | Add-on to Nokia Emulator | Several, including plugins for Eclipse | Interpreted language available natively only on Nokia Series60 (and desktops) though ports exist to other mobile platforms, including Palm OS | Sis deployment with py2sis or can use Python Runtime | Free |
| Symbian | C++ | Yes | Free emulator | Many choices | Compile per target | SIS deployment | Commercial and free tools available |
| Tizen | *Web-based*: HTML5, CSS, JavaScript *Native*: C, C++ | Yes | Free emulator | Tizen SDK | Web-based app to be available on web browser | Tizen through App store, Web URL | Development needs Windows, OS X, or Ubuntu Desktop |
| Ubuntu Touch | *Web-based*: HTML5, CSS, JavaScript *Native*: QML, C, C++ | Yes | Yes | Ubuntu SDK | HTML5 app to be available web browser. | Ubuntu Touch through App store, Web URL | Development requires Ubuntu Desktop 12.04 or higher, Free |
| webOS | JavaScript, CSS, HTML, C and C++ through the PDK | Yes | Free emulator | Eclipse | webOS, Palm only | OTA deployment, webOS through App store, Web URL, Precentral, .ipk | Free |
| Windows Mobile | C, C++ | Yes | Free emulator (source code available), also bundled with IDE | Visual Studio 2010, 2008, 2005, eMbedded VC++ (free), Satellite Forms | Windows Mobile, Windows CE | OTA deployment, CAB files, ActiveSync | Free command-line tools or eMbedded VC++, or Visual Studio (Standard edition or better) |
| Windows Phone | C#, Visual Basic, C, C++ | Yes | Free emulator, also bundled with IDE | Visual Studio 2012, Visual Studio 2010 | Windows Phone | OTA deployment, XAP files |   |

Criteria for selecting a development platform usually include the target mobile platforms, existing infrastructure, and development skills. When targeting more than one platform with cross-platform development, it is also important to consider the impact of the tool on the user experience. Performance is another important criterion, as research on mobile apps indicates a strong correlation between application performance and user satisfaction. Along with performance and other criteria, the availability of the technology and the project's requirements may drive the development between native and cross-platform environments. To aid the choice between native and cross-platform environments, some guidelines and benchmarks have been published. Typically, cross-platform environments are reusable across multiple platforms, leveraging a native container while using HTML, CSS, and JavaScript for the user interface. In contrast, native environments are targeted at one platform for each of those environments. For example, Android development occurs in the Eclipse IDE using Android Developer Tools (ADT) plugins, Apple iOS development occurs using the Xcode IDE with Objective-C and/or Swift, Windows and BlackBerry each have their own development environments.

### Mobile app testing

Mobile applications are first tested within the development environment using emulators and later subjected to field testing. Emulators provide an inexpensive way to test applications on mobile phones to which developers may not have physical access. The following are examples of tools used for testing applications across the most popular mobile operating systems.

- *Google Android Emulator* – an Android emulator that is patched to run on a Windows PC as a standalone app, without having to download and install the complete and complex Android SDK. It can be installed and Android compatible apps can be tested on it.
- *The official Android SDK Emulator* – a mobile device emulator which mimics all of the hardware and software features of a typical mobile device (without the calls).
- *TestiPhone* – a web browser-based simulator for quickly testing iPhone web applications. This tool has been tested and works using Internet Explorer 7, Firefox 2 and Safari 3.
- *iPhoney* – gives a pixel-accurate web browsing environment and it is powered by Safari. It can be used while developing web sites for the iPhone. It is not an iPhone simulator but instead is designed for web developers who want to create 320 by 480 (or 480 by 320) websites for use with iPhones. iPhoney will only run on OS X 10.4.7 or later.
- *BlackBerry Simulator* – There are a variety of official BlackBerry simulators available to emulate the functionality of actual BlackBerry products and test how the device software, screen, keyboard and trackwheel will work with the application.
- *Windows UI Automation* – To test applications that use the Microsoft UI Automation technology, it requires Windows Automation API 3.0. It is pre-installed on Windows 7, Windows Server 2008 R2 and later versions of Windows. On other operating systems, you can install it using Windows Update or download it from the Microsoft Web site.
- *MobiOne Developer* – a mobile Web integrated development environment (IDE) for Windows that helps developers to code, test, debug, package and deploy mobile Web applications to devices such as iPhone, BlackBerry, Android, and the Palm Pre. MobiOne Developer was officially declared End of Life by the end of 2014.

Tools include

- Eggplant Functional – GUI-based automated test tool for mobile apps across all operating systems and devices
- Ranorex – Test automation tools for mobile, web and desktop apps
- Testdroid – Real mobile devices and test automation tools for testing mobile and web apps

## Design principles

According to a 2020 Industry Report on Applications, 46% of mobile app users have stated that they have stopped using or uninstalled an app due to poor performance. Design experts advocate for the following design principles to create successful and effective mobile apps:

*Clutter-free screens* – Keeps interactions quick and simple, allowing users to focus on one specific task rather than being overwhelmed with multiple features and tasks. Design experts strongly advocate for one task per screen and recommend breaking down long forms into pages and progressively revealing new tasks or fields to minimize clutter.

*Reduce cognitive load* – Makes the use of the app as seamless as possible, and preserves natural flow through the app. Design experts suggest incorporating autocomplete, spell-check, predictive text assistance, and dropdown menus to reduce cognitive load. Design experts also recommend the state of the app be preserved when users temporarily leave the app and re-enter so that users can continue their use from where they left off.

*Simple navigation* – Around 11% of people have uninstalled apps due to their complicated interface. Design experts state it is paramount to present the navigation bar visibly in your app to help users navigate to frequently used and high-priority screens instantly. They suggest the use of recognizable icons specific to the device operating system to help users easily take actions such as opening a menu, changing settings, going back a screen, and searching within a page. According to them, a user should not be confused while navigating the app, so an orderly, clear, and logical navigation flow drives engagement and discovery in the app.

*Notifications* – It's reported that around 19% of users uninstall an app due to frequent push notifications. Notifications should be sent with careful planning according to design experts. Experts state notifications should be sent at a time most convenient to users in their time zone and the messages should be personalized to bring great value to them.

*Speed appearance* – About 19% of people uninstall apps due to hang up issues. Design experts state it's important to make sure the app is fast and responsive so that users don't have to wait for content. They state developers should deliver content faster or give the perception of progress. Some approaches suggested by the experts are the use of skeleton screens which show the layout of the app with content grayed out, progress bars or loading spinners, tasks being carried out in the background and delivering the content quickly when the user requests for it, or giving users some tasks or content while they are waiting for a page to load.

*Usability* – Approximately 85% of mobile users use their phone with one hand, thus design experts state it is important that the top-level menu, frequently used controls, and common action items are within the reach of the user's thumb. They also stress the importance of readability and it's recommended that the text size is at least 11 point font so that users can read it at the typical reading distance without zooming in. It is recommended that headers and titles on the app screens be San Francisco 17pt and Roboto 16sp for operating systems iOS and Android respectively. The experts also state there should be 4.5:1 minimum contrast ratio between text and the background color. Design experts strongly encourage developers to make apps accessible for all users including people with disabilities, so they suggest features such as voice navigation, screen reader compatibility, and user interface adaptability in mobile apps.

## Patents

Many patent applications are pending for new mobile phone apps. Most of these are in the technological fields of business methods, database management, data transfer, and operator interface.

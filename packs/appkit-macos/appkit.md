---
title: "AppKit"
source: https://en.wikipedia.org/wiki/AppKit
domain: appkit-macos
license: CC-BY-SA-4.0
tags: appkit framework, macos gui, aqua interface, quartz compositor
fetched: 2026-07-02
---

# AppKit

**AppKit** (formally **Application Kit**) is a graphical user interface toolkit. It initially served as the UI framework for NeXTSTEP. Along with Foundation and Display PostScript, it became one of the core parts of the OpenStep specification of APIs. Later, AppKit and Foundation became part of Cocoa, the Objective-C API framework of macOS. GNUstep, GNU's implementation of the OpenStep/Cocoa API, also contains an implementation of the AppKit API.

AppKit comprises a collection of Objective-C classes and protocols that can be used to build an application in OpenStep/Cocoa. These classes can also be used in Swift through its Objective-C bridge. Xcode has built-in functionality for developing a Cocoa application using AppKit, including the ability to visually design user interfaces with Interface Builder. It relies heavily on patterns like reference types, delegation, notifications, target–action, and model–view–controller. A sign of the NeXTSTEP heritage, AppKit's classes and protocols still use the "NS" prefix.

Most of the applications bundled with macOS—for example, the Finder, TextEdit, Calendar, and Preview—use AppKit to provide their user interface.

macOS, iOS, iPadOS, and tvOS also support other UI frameworks, including UIKit, which is derived from AppKit and uses many similar structures, and SwiftUI, a Swift-only declarative UI framework.

Prior to macOS Catalina, macOS also supported Carbon, a UI framework derived from the Macintosh Toolbox.

## Classes

Of the more than 170 classes included in the Application Kit, the following classes form the core:

- `NSApplication`: a singleton object that represents the application as a whole and tracks its windows and other global state
- `NSWindow`: an object representing a window on screen, it holds a hierarchy of views
- `NSView`: an object representing a rectangular region; it may draw UI content of its own (using drawing engines like Quartz, Core Animation, and Metal), and it may also hold a subtree of other views
- `NSResponder`: an object that can respond to events during the application's lifetime; `NSApplication`, `NSWindow`, and `NSView` are all subclasses of `NSResponder`
- `NSDocument`: an object representing a document saved on disk that manages its display in a window
- `NSController`: an abstract class implementing some functionality for a controller, mediating between views and model objects

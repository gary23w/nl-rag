---
title: "Interface Builder"
source: https://en.wikipedia.org/wiki/Interface_Builder
domain: cocoa-appkit-deep
license: CC-BY-SA-4.0
tags: cocoa appkit, objective-c runtime, interface builder, macos native ui
fetched: 2026-07-02
---

# Interface Builder

**Interface Builder** is a software development application for Apple's macOS operating system. It is part of Xcode (formerly Project Builder), the Apple Developer developer's toolset. Interface Builder allows Cocoa and Carbon developers to create interfaces for applications using a graphical user interface. The resulting interface is stored as a **.nib** file, short for *NeXT Interface Builder,* or more recently, as an XML-based **.xib** file.

Interface Builder is descended from the NeXTSTEP development software of the same name. A version of Interface Builder is also used in the development of OpenStep software, and a very similar tool called Gorm exists for GNUstep. On March 27, 2008, a specialized iPhone version of Interface Builder allowing interface construction for iPhone applications was released with the iPhone SDK Beta 2.

Interface Builder was intentionally developed as a separate application, to allow interaction designers to design interfaces without having to use a code-oriented IDE, but as of Xcode 4, Apple has integrated its functionality directly into Xcode.

## History

Originally the software was called *SOS Interface*, and was created by Jean-Marie Hullot whilst he was a researcher at Inria at Rocquencourt near Paris. He was allowed to retain ownership of the software upon resigning from Inria, and spent a year working it into a fully-featured product, now named *Interface Builder* and distributed for Macintosh by ExperTelligence in the USA in 1986. It was written in Lisp (for the *ExperLisp* product by *ExperTelligence*) and deeply integrated with the Macintosh Toolbox. *Interface Builder* was presented at MacWorld Expo in San Francisco in January 1987.

Denison Bollay took Jean-Marie Hullot to NeXT after MacWorld Expo to demonstrate it to Steve Jobs. Jobs recognized its value, and started incorporating it into NeXTSTEP, and by 1988 it was part of NeXTSTEP 0.8. It was the first commercial application that allowed interface objects, such as buttons, menus, and windows, to be placed in an interface using a mouse.

One notable early use of *Interface Builder* was the development of the first web browser, WorldWideWeb by Tim Berners-Lee at CERN, made using a NeXT workstation.

## Design

Interface Builder provides *palettes*, or collections, of user interface objects to an Objective-C or Swift developer. These user interface objects contain items like text fields, data tables, sliders, and pop-up menus. Interface Builder's palettes are completely extensible, meaning any developer can develop new objects and add palettes to Interface Builder.

To build an interface, a developer simply drags interface objects from the palette onto a window or menu. *Actions* (messages) which the objects can emit are connected to *targets* in the application's code and *outlets* (pointers) declared in the application's code are connected to specific objects. In this way all initialization is done before runtime, both improving performance and streamlining the development process. When Interface Builder was a standalone application, interface designers could ship nib files to developers, who would then drop them into their projects.

Interface Builder saves an application's interface as a bundle that contains the interface objects and relationships used in the application. These objects are archived (a process also known as serialization or marshalling in other contexts) into either an XML file or a NeXT-style property list file with a .nib extension. Upon running an application, the proper NIB objects are unarchived, connected into the binary of their owning application, and awakened. Unlike almost all other GUI designer systems which generate code to construct the UI (notable exceptions being Glade, Embarcadero Technologies's Delphi and C++Builder, which stream UI objects similarly), NIBs are often referred to as *freeze dried* because they contain the archived objects themselves, ready to run. As of Interface Builder version 3, a new file format (with extension .xib) has been added, which is functionally identical to .nib, except it is stored in a flat file, making it more suitable for storage in revision control systems and processing by tools such as diff.

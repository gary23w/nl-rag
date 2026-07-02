---
title: "UIKit"
source: https://en.wikipedia.org/wiki/UIKit
domain: catalyst-mac
license: CC-BY-SA-4.0
tags: mac catalyst, uikit on mac, ipad app port, apple platform bridge
fetched: 2026-07-02
---

# UIKit

**UIKit** is an application development environment and graphical user interface toolkit from Apple Inc. used to build apps for the iOS, iPadOS, watchOS, tvOS, and visionOS operating systems.

UIKit provides an abstraction layer of iOS, the operating system for the iPhone, iPod Touch, and iPad. UIKit is similar to AppKit from the macOS Cocoa API toolset, and it too is primarily written in the Objective-C language. UIKit allows the use of hardware and features that are not found in macOS computers and are thus unique to the iOS range of devices. Like AppKit, UIKit follows a Model–View–Controller (MVC) software architecture.

UIKit contains a different set of graphical control elements from AppKit. Tools for developing applications based on UIKit are included in the iOS SDK.

## UIKit in relation to other layers

iOS, watchOS, and tvOS technologies can be seen as a set of layers, with UIKit at the highest level and the core operating system / kernel at the bottom.

A hierarchical view of the iOS, watchOS, and tvOS technologies can be shown as follows:

1. UIKit
2. Media / Application Services
3. Core Services
4. Core OS / iOS kernel

## Main features

Some of the main features and technologies of UIKit are:

- App Extension
- Data Management
- Handoff
- Document Picker
- AirDrop
- TextKit
- UIKit Dynamics
- Multitasking
- Auto Layout
- Storyboards
- UI State Preservation
- Apple Push Notification Service
- Local Notifications
- Gesture Recognisers
- Standard System View Controllers

## Main frameworks

UIKit provides the key frameworks for developing applications on devices running iOS, and is based atop Foundation Kit. Other frameworks built by Apple that complement AppKit are:

- GameKit
- MapKit
- Address Book UI
- EventKit UI
- Message UI
- Notification Center
- PushKit

## Ports

Microsoft's WinObjC, the GNUstep-based iOS bridge for the Universal Windows Platform, contains working implementations of frameworks such as Foundation, UIKit, and MapKit released under the MIT License. One of the UIKit implementations is based on XAML.

Various efforts have tried to bring UIKit to macOS:

- Chameleon is a port of UIKit to macOS from 2014.
- ZeeZide's UXKit is a more recent port of UIKit to macOS. It exists a layer above AppKit and UIKit.
- Apple used a "UXKit" private framework for a 2015 version of Photos.app.
- Apple made the bridge more official with the "iosMac" or "Marzipan" project in 2018, which put an "iOSSupport" directory full of iOS frameworks in macOS Mojave. They were originally restricted from developer use and was finally made official with the release of Mac Catalyst in 2019.

---
title: "NativeScript"
source: https://en.wikipedia.org/wiki/NativeScript
domain: nativescript
license: CC-BY-SA-4.0
tags: nativescript framework, javascript native access, direct native api, cross-platform mobile js
fetched: 2026-07-02
---

# NativeScript

**NativeScript** is an open-source native app development framework that brings JavaScript and TypeScript to native platform development for iOS, visionOS, and Android. It provides platform APIs directly to the JavaScript runtime, allowing developers to use Web development approaches such as CSS, view templating, and popular JavaScript frameworks while interoperating with platform languages including Swift, Kotlin, Objective-C, and Java.

It was originally conceived and developed by Bulgarian company Telerik, later acquired by Progress Software. At the end of 2019 stewardship of the NativeScript project transitioned to long-time Progress partner nStudio. In December 2020, NativeScript joined the OpenJS Foundation as an Incubating Project. NativeScript apps are built using JavaScript, or by using any programming language that transpiles to JavaScript, such as TypeScript. NativeScript supports the Angular, Vue, React, Solid, and Svelte frameworks. Mobile applications built with NativeScript result in fully native apps, which use the same APIs as if they were developed in Xcode or Android Studio. Additionally, software developers can re-purpose third-party libraries from CocoaPods, Maven, and npm.js in their mobile applications without the need for wrappers.

## Development

NativeScript was publicly released first in March 2015. Version 1.0.0 followed two months later. The framework quickly gained popularity reaching 3000 github-stars and over 1500 followers on Twitter soon after the public release. In the meantime, over 700 plugins are available, which are either officially supported by Progress or stem from the open source community. The use of Angular is an optional development approach allowing for application source code to be shared between the web platform and mobile platform.

## Structure

NativeScript and related packages are installed using the package manager npm. Projects are created, configured, and compiled primarily through the NativeScript command-line interface and associated JavaScript tooling. Historically, NativeScript also provided a graphical tool called NativeScript Sidekick.

Platform-independent user interfaces are defined using XML files. NativeScript then uses the abstractions described in the XML files to call native UI elements of each platform. Application logic developed in Angular and TypeScript can be developed independent of the target platform as well. A NativeScript mobile application is built using the node.js runtime and tooling. Progress aims for a ratio of 90% common code between the iOS and Android platforms.

## Direct access to native platform APIs and controls

Platform-independent user interfaces are defined using XML files. NativeScript uses the XML data structures representing the cross platform abstraction to trigger platform-specific code that directly interacts with the native elements of the target operating system. This means a call to the NativeScript Button API provides a UI abstraction for Button, which directly calls UIButton on iOS or com.android.widget.Button on Android.

While application source code is written in JavaScript, TypeScript, Angular, or Vue.js, the source code is not compiled or otherwise mutated. The source code as-is runs directly on the device. This architectural choice eliminates the need for cross-compiling or transpiling. Additionally, while the application source code is written in languages commonly encountered in a browser (or in a WebView-contained mobile application) NativeScript applications run directly on the native device. There is no DOM manipulation or any mandatory browser interaction.

## Notable features

### Native API reflection

Another notable feature is the use of reflection to handle native API endpoints. Rather than requiring separate binding layers between NativeScript and each mobile platform API, NativeScript uses reflection to gain information and metadata about the native platform APIs. New features added to any native platform API are available immediately.

Another way the reflection feature is used is in working with third party libraries. As JavaScript (or TypeScript/Angular) can talk directly to native code, there is no need to write binding layers in Objective-C, Swift, Java or Kotlin.

### Angular integration

With the launch of NativeScript 2.0, it is possible to use Angular to build cross-platform mobile applications. Additionally, when using Angular with NativeScript you have the ability to share large chunks of code between your web and mobile apps.

### Vue.js integration

The Vue.js framework is supported in NativeScript via the nativescript-vue plugin.

## Supporting tools and services

- The NativeScript command-line interface is used to create, configure, build, and run NativeScript applications.
- NativeScript Preview allows you to run apps in the browser from StackBlitz.
- Norrix allows you to build, update and submit NativeScript apps to the App Store and Google Play.
- NativeScript Marketplace lists community and ecosystem plugins for NativeScript applications.
- NativeScript Sidekick and NativeScript Playground were historical tools associated with the ecosystem.

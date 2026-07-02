---
title: "Ionic (mobile app framework)"
source: https://en.wikipedia.org/wiki/Ionic_(mobile_app_framework)
domain: ionic-framework
license: CC-BY-SA-4.0
tags: ionic framework, hybrid mobile toolkit, web component controls, cordova capacitor shell
fetched: 2026-07-02
---

# Ionic (mobile app framework)

**Ionic** is an open-source UI toolkit for building cross-platform mobile, web, and desktop applications using web technologies such as HTML, CSS, and JavaScript/TypeScript. It provides a set of pre-designed UI components and tools for building high-quality, interactive applications. Ionic was originally built as a complete open-source SDK for hybrid mobile app development created by Max Lynch, Ben Sperry, and Adam Bradley of Drifty Co. in 2013. The original version was released in 2013 and built on top of AngularJS and Apache Cordova. However, the latest release was re-built as a set of Web Components using StencilJS, allowing the user to choose any user interface framework, such as Angular, React or Vue.js. It also allows the use of Ionic components with no user interface framework at all. Ionic provides tools and services for developing hybrid mobile, desktop, and progressive web apps based on modern web development technologies and practices, using Web technologies like CSS, HTML5, and Sass. In particular, mobile apps can be built with these Web technologies and then distributed through native app stores to be installed on devices by utilizing Cordova or Capacitor.

## History

Ionic was created by Drifty Co. in 2013. After releasing an alpha version of the framework in November 2013, a 1.0 beta was released in March 2014, a 1.0 final in May 2015, and several 2.0 releases in 2016.

Since January 2019, Ionic 4 allows developers to choose other frameworks apart from Angular like React, Vue.js, and web components. Ionic 4 was built using StencilJS. Ionic was acquired by OutSystems in November 2022.

## Services and features

Ionic uses Cordova and, more recently, Capacitor plugins to gain access to host operating systems features such as Camera, GPS, Flashlight, etc. Users can build their apps, and they can then be customized for Android, iOS, Windows, Desktop (with Electron), or modern browsers. Ionic allows app building and deployment by wrapping around the build tool Cordova or Capacitor with a simplified 'ionic' command line tool.

Ionic includes mobile components, typography, interactive paradigms, and an extensible base theme.

Using Web Components, Ionic provides custom components and methods for interacting with them. One such component, virtual scroll, allows users to scroll through a list of thousands of items without any performance hits. Another component, tabs, creates a tabbed interface with support for native-style navigation and history state management.

Besides the SDK, Ionic also provides services that developers can use to enable features, such as code deploys, automated builds. Ionic also provides its own IDE known as Ionic Studio, but it was discontinued in 2020.

Ionic also provides a command-line interface (CLI) to create projects. The CLI also allows developers to add Cordova plugins and additional front-end packages, enable push notifications, generate app Icons and Splash screens, and build native binaries.

## Supported platforms

For Android, Ionic supports Android 4.4 and up. For iOS, Ionic supports iOS 10 and up. Ionic 2 supports the Universal Windows Platform for building Windows 10 apps. Ionic Framework, based on *Angular.js*, supports BlackBerry 10 apps.

## Performance

Ionic apps run with a mixture of native code and web code, providing full access to native functionality if necessary, with the bulk of the UI of the app built with standard web technology. Ionic utilizes native hardware acceleration features available in the browser (such as CSS animations) and optimizes rendering (avoiding expensive DOM manipulation). Ionic leverages CSS transitions and transforms for animation as a way to leverage the GPU and maximize available processor time.

## Installation

Ionic is an npm module and requires Node.js.

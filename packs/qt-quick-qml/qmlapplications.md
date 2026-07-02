---
title: "Getting started with Qt Quick applications"
source: https://doc.qt.io/qt-6/qmlapplications.html
domain: qt-quick-qml
license: CC-BY-SA-4.0
tags: qt quick, qml declarative ui, scene graph rendering, fluid animation
fetched: 2026-07-02
---

# Getting started with Qt Quick applications

First Steps with QML

# Getting started with Qt Quick applications

QML is a declarative language that allows user interfaces to be described in terms of their visual components and how they interact and relate with one another. It is a highly readable language that was designed to enable components to be interconnected in a dynamic manner, and it allows components to be easily reused and customized within a user interface. Using the `QtQuick` module, designers and developers can easily build fluid animated user interfaces in QML, and have the option of connecting these user interfaces to any back-end C++ libraries.

## Qt Academy Courses

The following Qt Academy courses are recommended for getting started with QML and Qt Quick.

### Basic courses

- QML for Beginners
- Introduction to QML
- Introduction to Qt Quick
- Introduction to Qt Quick Controls
- Creating a Simple Qt Quick Application

### Intermediate courses

- QML Dashboard: Main UI
- QML Dashboard: Inbox
- QML Dashboard: Calendar
- QML Dashboard: Courses

## What is QML?

QML is a user interface specification and programming language. It allows developers and designers alike to create highly performant, fluidly animated and visually appealing applications. QML offers a highly readable, declarative, JSON-like syntax with support for imperative JavaScript expressions combined with dynamic property bindings.

```
import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 400
    height: 400
    visible: true

    Button {
        id: button
        text: "A Special Button"
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            border.width: 1
            radius: 4
        }
    }
}
```

The QML language and engine infrastructure is provided by the Qt Qml module. For in-depth information about the QML language, see the Qt Qml module documentation.

The following pages contain more information about QML:

- Qt Creator: Create Qt Quick Applications
- First Steps with QML - begin using QML with these examples
- Glossary of QML Terms
- The QML Reference - reference about the QML constructs and features
- QML Coding Conventions
- All QML APIs by Module

## What is Qt Quick?

Qt Quick is the standard library of QML types and functionality for QML. It includes visual types, interactive types, animations, models and views, particle effects and shader effects. A QML application developer can get access to all of that functionality with a single import statement.

The `QtQuick` QML library is provided by the Qt Quick module. For in-depth information about the various QML types and other functionality provided by Qt Quick, please see the Qt Quick module documentation. Qt Quick adds visual types, animation types, and other QML types in addition to the standard QML types from Qt Qml.

- Visual types
- Positioners and layouts
- Handling user input
- Displaying text
- Animations
- Integrating JavaScript in QML

### Buttons, Menus, and other Controls

For a set of UI controls, the Qt Quick Controls module implements several controls such as buttons, menus, and views. These controls come with several built-in styles that can be used, and also support the creation of custom styles.

## Qt Quick Application Development

Qt Creator has built-in support for creating Qt Quick applications. Qt VS Tools and Qt Extension for VS Code also allow you to create Qt Quick applications with Visual Studio and Visual Studio Code. The QML Language Server can be used from any IDE supporting the language server protocol.

For a design centric workflow, use Qt Design Studio.

For more information about creating Qt Quick applications, visit the following pages:

- Qt Creator: Create Qt Quick Applications
- Qt Design Studio: Getting Started

## Code Samples and Demos

To learn more about uses of QML code, there are several code samples which show how QML types are used. In addition, there are several demos which show how QML code is used in applications.

- Getting Started programming with Qt Quick: An Alarm Application - a tutorial showing the creation of a simple alarm application.
- Qt Quick Examples and Tutorials

## Advanced Application Development Topics

- Overview - QML and C++ Integration
- Deploying QML Applications
- Qt Quick Compiler
- Best Practices for QML and Qt Quick
- Performance considerations and suggestions
- Internationalization and Localization
- Testing and Debugging
  - Prototyping with the QML Runtime Tool
  - Debugging QML Applications
  - Qt Quick Test: QML Unit Testing Framework

- All QML Types
- All QML APIs by Module
- Obsolete QML Types

First Steps with QML

© 2026 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the GNU Free Documentation License version 1.3 as published by the Free Software Foundation. Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners.

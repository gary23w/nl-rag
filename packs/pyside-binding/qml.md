---
title: "QML - Wikipedia"
source: https://en.wikipedia.org/wiki/QML
domain: pyside-binding
license: CC-BY-SA-4.0
tags: pyside binding, qt for python, shiboken generator, official qt python
fetched: 2026-07-02
---

# QML

**QML** (**Qt Meta-object Language**) is a user interface markup language. It is a declarative language (similar to CSS and JSON) for designing user interface–centric applications. Imperative aspects are handled by inline JavaScript code. It is associated with Qt Quick, the UI creation kit originally developed by Nokia within the Qt framework. Qt Quick is used for mobile applications where touch input, fluid animations and user experience are crucial. QML is also used with Qt3D to describe a 3D scene and a "frame graph" rendering methodology. A QML document describes a hierarchical object tree. QML modules shipped with Qt include primitive graphical building blocks (e.g., Rectangle, Image), modeling components (e.g., FolderListModel, XmlListModel), behavioral components (e.g., TapHandler, DragHandler, State, Transition, Animation), and more complex controls (e.g., Button, Slider, Drawer, Menu). These elements can be combined to build components ranging in complexity from simple buttons and sliders, to complete internet-enabled programs.

QML elements can be augmented by standard JavaScript both inline and via included .js files. Elements can also be seamlessly integrated and extended by C++ components using the Qt framework.

QML is the language; its JavaScript runtime is the custom V4 engine, since Qt 5.2; and Qt Quick is the 2D scene graph and the UI framework based on it. These are all part of the Qt Declarative module, while the technology is no longer called Qt Declarative.

QML and JavaScript code can be compiled into native C++ binaries with the Qt Quick Compiler. Alternatively there is a QML cache file format which stores a compiled version of QML dynamically for faster startup the next time it is run.

## Adoption

- KDE Plasma 4, KDE Plasma 5 and KDE Plasma 6 through Plasma-framework
- Liri OS
- Simple Desktop Display Manager
- reMarkable tablet device
- Unity2D
- Sailfish OS
- BlackBerry 10
- MeeGo
- Maemo
- Tizen
- Mer
- Ubuntu Phone
- Lumina (desktop environment)
- Many open-source applications

## Syntax, semantics

Some syntax examples follow:

### Basic syntax

```mw
import QtQuick

Rectangle {
    id: canvas
    width: 250
    height: 200
    color: "blue"

    Image {
        id: logo
        source: "pics/logo.png"
        anchors.centerIn: parent
        x: canvas.height / 5
    }
}
```

Objects are specified by their type, followed by a pair of braces. Object types always begin with a capital letter. In the example above, there are two objects, a Rectangle; and its child, an Image. Between the braces, one can specify information about the object, such as its properties. Properties are specified as property: value. In the example above, the Image has a property named `source`, which has been assigned the value `pics/logo.png`. The property and its value are separated by a colon.

**The id property**

Each object can be given a special unique property called an id. Assigning an id enables the object to be referred to by other objects and scripts. The first Rectangle element below has an id, `myRect`. The second Rectangle element defines its own width by referring to `myRect.width`, which means it will have the same width value as the first Rectangle element.

```mw
Item {
    Rectangle {
        id: myRect
        width: 120
        height: 100
    }
    Rectangle {
        width: myRect.width
        height: 200
    }
}
```

An id must begin with a lower-case letter or an underscore, and can contain no characters other than letters, digits, and underscores.

### Property bindings

A property binding specifies the value of a property in a declarative way. The property value is automatically updated if the other properties or data values change, following the reactive programming paradigm.

Property bindings are created implicitly in QML whenever a property is assigned a JavaScript expression. The following QML uses two property bindings to connect the size of the rectangle to that of otherItem.

```mw
Rectangle {
    width: otherItem.width
    height: otherItem.height
}
```

QML extends a standards-compliant JavaScript engine, so any valid JavaScript expression can be used as a property binding. Bindings can access object properties, make function calls, and even use built-in JavaScript objects like Date and Math.

```mw
Rectangle {
    function calculateMyHeight() {
        return Math.max(otherItem.height, thirdItem.height);
    }
    anchors.centerIn: parent
    width: Math.min(otherItem.width, 10)
    height: calculateMyHeight()
    color: width > 10 ? "blue" : "red"
}
```

### States

States are a mechanism to combine changes to properties in a semantic unit. A button for example has a pressed and a non-pressed state, an address book application could have a read-only and an edit state for contacts. Every element has an "implicit" base state. Every other state is described by listing the properties and values of those elements which differ from the base state.

Example: In the default state, myRect is positioned at 0,0. In the "moved" state, it is positioned at 50,50. Clicking within the mouse area changes the state from the default state to the "moved" state, thus moving the rectangle.

```mw
import QtQuick

Item {
    id: myItem
    width: 200; height: 200

    Rectangle {
        id: myRect
        width: 100; height: 100
        color: "red"
    }
    states: [
        State {
            name: "moved"
            PropertyChanges {
                target: myRect
                x: 50
                y: 50
            }
        }
    ]
    MouseArea {
        anchors.fill: parent
        onClicked: myItem.state = 'moved'
    }
}
```

State changes can be animated using Transitions.

For example, adding this code to the above Item element animates the transition to the "moved" state:

```mw
transitions: [
    Transition {
        from: "*"
        to: "moved"
        NumberAnimation { properties: "x,y"; duration: 500 }
    }
]
```

### Animation

Animations in QML are done by animating properties of objects. Properties of type real, int, color, rect, point, size, and vector3d can all be animated.

QML supports three main forms of animation: basic property animation, transitions, and property behaviors.

The simplest form of animation is a PropertyAnimation, which can animate all of the property types listed above. A property animation can be specified as a value source using the Animation on property syntax. This is especially useful for repeating animations.

The following example creates a bouncing effect:

```mw
Rectangle {
    id: rect
    width: 120; height: 200

    Image {
        id: img
        source: "pics/qt.png"
        x: 60 - img.width/2
        y: 0

        SequentialAnimation on y {
            loops: Animation.Infinite
            NumberAnimation { to: 200 - img.height; easing.type: Easing.OutBounce; duration: 2000 }
            PauseAnimation { duration: 1000 }
            NumberAnimation { to: 0; easing.type: Easing.OutQuad; duration: 1000 }
        }
    }
}
```

## Qt/C++ integration

Usage of QML does not require Qt/C++ knowledge to use, but it can be easily extended via Qt. Any C++ class derived from QObject can be easily registered as a type which can then be instantiated in QML.

### Familiar concepts

QML provides direct access to the following concepts from Qt:

- QObject signals – can trigger callbacks in JavaScript
- QObject slots – available as functions to call in JavaScript
- QObject properties – available as variables in JavaScript, and for bindings
- QWindow – Window creates a QML scene in a window
- Q*Model – used directly in data binding (e.g., QAbstractItemModel)

### Signal handlers

Signal handlers are JavaScript callbacks which allow imperative actions to be taken in response to an event. For instance, the MouseArea element has signal handlers to handle mouse press, release and click:

```mw
MouseArea {
    onPressed: console.log("mouse button pressed")
}
```

All signal handler names begin with "on".

## Development tools

Because QML and JavaScript are very similar, almost all code editors supporting JavaScript will work. Full support for syntax highlighting, code completion, integrated help, and a WYSIWYG editor are available in the free cross-platform integrated development environment (IDE) Qt Creator since version 2.1 and many other IDEs.

The qml executable can be used to run a QML file as a script. If the QML file begins with a shebang it can be made directly executable. However packaging an application for deployment (especially on mobile platforms) generally involves writing a simple C++ launcher and packaging the needed QML files as resources.

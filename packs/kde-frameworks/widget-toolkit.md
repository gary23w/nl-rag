---
title: "Widget toolkit"
source: https://en.wikipedia.org/wiki/Widget_toolkit
domain: kde-frameworks
license: CC-BY-SA-4.0
tags: kde frameworks, plasma desktop libraries, kirigami convergent ui, qt kde modules
fetched: 2026-07-02
---

# Widget toolkit

A **widget toolkit**, **widget library**, **GUI toolkit**, **GUI framework**, **UI framework**, or **UX library** is a library or a collection of libraries containing a set of graphical control elements (called *widgets*) used to construct the graphical user interface (GUI) of programs.

Most widget toolkits additionally include their own rendering engine. This engine can be specific to a certain operating system or windowing system or contain back-ends to interface with multiple ones and also with rendering APIs such as OpenGL, OpenVG, or EGL. The look and feel of the graphical control elements can be hard-coded or decoupled, allowing the graphical control elements to be themed/skinned.

## Overview

Some toolkits may be used from other languages by employing language bindings. Graphical user interface builders such as e.g. Glade Interface Designer facilitate the authoring of GUIs in a WYSIWYG manner employing a user interface markup language such as in this case GtkBuilder.

The GUI of a program is commonly constructed in a cascading manner, with graphical control elements being added directly to on top of one another.

Most widget toolkits use event-driven programming as a model for interaction. The toolkit handles user events, for example when the user clicks on a button. When an event is detected, it is passed on to the application where it is dealt with. The design of those toolkits has been criticized for promoting an oversimplified model of event-action, leading programmers to create error-prone, difficult to extend and excessively complex application code. Finite-state machines and hierarchical state machines have been proposed as high-level models to represent the interactive state changes for reactive programs.

## Windowing systems

A window is considered to be a graphical control element. In some windowing systems, windows are added directly to the scene graph (canvas) by the window manager, and can be stacked and layered on top of each other through various means. Each window is associated with a particular application which controls the widgets added to its canvas, which can be watched and modified by their associated applications.

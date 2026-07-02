---
title: "Viewport"
source: https://en.wikipedia.org/wiki/Viewport
domain: viewport-meta
license: CC-BY-SA-4.0
tags: viewport meta tag, mobile viewport scaling, css viewport concepts, device width layout, media query breakpoints
fetched: 2026-07-02
---

# Viewport

A **viewport** is a polygon viewing region in computer graphics.

In computer graphics theory, there are two region-like notions of relevance when rendering some objects to an image. In textbook terminology, the *world coordinate window* is the area of interest (meaning what the user wants to visualize) in some application-specific coordinates, e.g. miles, centimeters etc.

The word *window* as used here should not be confused with the GUI window, i.e. the notion used in window managers. Rather it is an analogy with how a window limits what one can see outside a room.

In contrast, the *viewport* is an area (typically rectangular) expressed in rendering-device-specific coordinates, e.g. pixels for screen coordinates, in which the objects of interest are going to be rendered. Clipping to the world-coordinates window is usually applied to the objects before they are passed through the window-to-viewport transformation. For a 2D object, the latter transformation is simply a combination of translation and scaling, the latter not necessarily uniform. An analogy of this transformation process based on traditional photography notions is to equate the world-clipping window with the camera settings and the variously sized prints that can be obtained from the resulting film image as possible viewports.

Because the physical-device-based coordinates may not be portable from one device to another, a software abstraction layer known as normalized device coordinates is typically introduced for expressing viewports; it appears for example in the Graphical Kernel System (GKS) and later systems inspired from it.

In 3D computer graphics, the viewport refers to the 2D rectangle used to project the 3D scene to the position of a virtual camera. A viewport is a region of the screen used to display a portion of the total image to be shown.

In virtual desktops, the viewport is the visible portion of a 2D area which is larger than the visualization device.

When viewing a document in a web browser, the viewport is the region of the browser window which contains the visible portion of the document. If the size of the viewport changes, for example as a result of the user resizing the browser window, then the browser may reflow the document (recalculate the locations and sizes of elements of the document). If the document is larger than the viewport, the user can control the portion of the document which is visible by scrolling in the viewport.

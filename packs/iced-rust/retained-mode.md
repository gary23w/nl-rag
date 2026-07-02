---
title: "Retained mode"
source: https://en.wikipedia.org/wiki/Retained_mode
domain: iced-rust
license: CC-BY-SA-4.0
tags: iced toolkit, elm architecture, rust reactive gui, cross-platform rendering
fetched: 2026-07-02
---

# Retained mode

**Retained mode** in computer graphics is a major pattern of API design in graphics libraries, in which

- the graphics library, instead of the client, retains the scene (complete object model of the rendering primitives) to be rendered and
- the client calls into the graphics library do not directly cause actual rendering, but make use of extensive indirection to resources, managed – thus ***retained*** – by the graphics library. It does not preclude the use of double-buffering.

Immediate mode is an alternative approach. Historically, retained mode has been the dominant style in GUI libraries; however, both can coexist in the same library and are not necessarily exclusionary in practice.

## Overview

In retained mode the client calls do not directly cause actual rendering, but instead update an abstract internal model (typically a list of objects) which is maintained within the library's data space. This allows the library to optimize when actual rendering takes place along with the processing of related objects.

Some techniques to optimize rendering include:

- managing double buffering
- treatment of hidden surfaces by backface culling/occlusion culling (Z-buffering)
- only transferring data that has changed from one frame to the next from the application to the library

Example of coexistence with immediate mode in the same library is OpenGL. OpenGL has immediate mode functions that can use previously defined server side objects (textures, vertex buffers and index buffers, shaders, etc.) without resending unchanged data.

Examples of retained mode rendering systems include Windows Presentation Foundation, SceneKit on macOS, and PHIGS.

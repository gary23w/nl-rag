---
title: "Immediate mode (computer graphics)"
source: https://en.wikipedia.org/wiki/Immediate_mode_GUI
domain: dear-imgui
license: CC-BY-SA-4.0
tags: dear imgui, immediate mode gui, bloat-free interface, debug tooling overlay
fetched: 2026-07-02
---

# Immediate mode (computer graphics)

(Redirected from

Immediate mode GUI

)

**Immediate mode** is an API design pattern in computer graphics libraries, in which

- the client calls directly cause rendering of graphics objects to the display, or in which
- the data to describe rendering primitives is inserted frame by frame directly from the client into a command list (in the case of *immediate mode primitive rendering*),

without the use of extensive indirection – thus***immediate***– to retained resources. It does not preclude the use of double-buffering.

Retained mode is an alternative approach. Historically, retained mode has been the dominant style in GUI libraries; however, both can coexist in the same library and are not necessarily exclusive in practice.

## Overview

In immediate mode, the scene (complete object model of the rendering primitives) is retained in the memory space of the client, instead of the graphics library. This implies that in an immediate mode application, the lists of graphical objects to be rendered are kept by the client and are not saved by the graphics library API. The application must re-issue all drawing commands required to describe the entire scene each time a new frame is required, regardless of actual changes. This method provides on the one hand a maximum of control and flexibility to the application program, but on the other hand it also generates continuous work load on the CPU.

Examples of immediate mode rendering systems include Direct2D, OpenGL and Quartz. There are some immediate mode GUIs that are particularly suitable when used in conjunction with immediate mode rendering systems.

## Immediate mode primitive rendering

Primitive vertex attribute data may be inserted frame by frame into a command buffer by a rendering API. This involves significant bandwidth and processor time (especially if the graphics processing unit is on a separate bus), but may be advantageous for data generated dynamically by the CPU. It is less common since the advent of increasingly versatile shaders, with which a graphics processing unit may generate increasingly complex effects without the need for CPU intervention.

## Immediate mode rendering with vertex buffers

Although drawing commands have to be re-issued for each new frame, modern systems using this method are generally able to avoid the unnecessary duplication of more memory-intensive display data by referring to that unchanging data (via indirection) (e.g. textures and vertex buffers) in the drawing commands.

## Immediate mode GUI

Graphical user interfaces traditionally use retained mode-style API design, but immediate mode GUIs instead use an immediate mode-style API design, in which user code directly specifies the GUI elements to draw in the user input loop. For example, rather than having a CreateButton() function that a user would call once to instantiate a button, an immediate-mode GUI API may have a DoButton() function which should be called whenever the button should be on screen. The technique was developed by Casey Muratori in 2002. Prominent implementations include Omar Cornut's Dear ImGui in C++, Nic Barker's Clay in C and Micha Mettke's Nuklear in C.

---
title: "raylib"
source: https://en.wikipedia.org/wiki/Raylib
domain: raylib
license: CC-BY-SA-4.0
tags: raylib library, raylib game, c game library, immediate mode graphics
fetched: 2026-07-02
---

# raylib

**raylib** is a cross-platform open-source software development library. The library was made to create graphical applications and games.

The library is designed to be suited for prototyping, tooling, graphical applications, embedded systems, and education. The source code is written in the C programming language (specifically using C99), which is distributed under a zlib/libpng OSI certified open-source license. It supports compilation to several target platforms, including Windows, Linux, macOS, FreeBSD, Android, Raspberry Pi and HTML5.

raylib has been ported to more than 70 programming languages in the form of bindings, but many of these ports are not stable.

## History

raylib development began in August 2013 when Ramon Santamaria created the library to support a game development course aimed at students with artistic backgrounds and no prior coding experience. Student feedback throughout the course shaped its early development, and by mid-2014 the library was being showcased at game development events in Barcelona.

raylib 1.0 was released in November 2013, offering basic functionality for window management, 2D/3D rendering, texture and font loading, and audio playback. Eight minor releases over the following five years added Android, WebAssembly, and Raspberry Pi support, multiple OpenGL backends, VR support, shaders, a physics module, and an expanding examples library.

raylib 2.0 was released in July 2018, coinciding with Santamaria leaving his professorship to focus on raylib full-time. All external dependencies were removed, OpenAL was replaced by the miniaudio library, and continuous integration support was introduced. A subsequent minor release, raylib 2.5, added Unicode text rendering, skeletal animation with glTF support, and a redesigned gamepad system.

raylib 3.0 was released in April 2020, refactoring the codebase to improve portability and language binding support. Global state was consolidated into context structures, and all file I/O was centralized to allow custom virtual filesystem integration. Bindings for over 40 programming languages were available by this point. A minor update, raylib 3.5, followed in December 2020, adding Raspberry Pi 4 native mode and improved software rendering aimed at embedded devices.

raylib 4.0 was released in November 2021, focusing on API consistency through broad renaming and documentation improvements. It introduced an experimental input recording and replay system, optional user-controlled game-loop timing, and OpenGL 4.3 support, with rlgl and raymath promoted to usable standalone libraries. Two minor releases followed: raylib 4.2 in August 2022, which moved secondary libraries such as raygui and physac to separate repositories and introduced the rres resource packaging format; and raylib 4.5 in March 2023, which added ANGLE support on desktop to enable Vulkan, Direct3D 11, and Metal backends, extended animation support to M3D and glTF formats, and added the QOA audio format.

raylib 5.0 was released in November 2023 to mark the library's 10th anniversary. Its most significant change was splitting the core platform module into separate, swappable backends, making new platform support far more approachable, with SDL2 added as an alternative desktop backend alongside an unofficial Nintendo Switch backend. Spline drawing, a new pseudo-random number generator, and a redesigned automation events system were also introduced. A minor release, raylib 5.5, followed in November 2024, adding RGFW and SDL3 as additional platform backends, GPU skinning support for 3D model animations.

raylib 6.0 was released in April 2026. A software renderer backend was introduced, allowing raylib to run entirely on CPU without a GPU. New platform backends were added for Win32 and Emscripten without third-party library dependencies, alongside a headless memory framebuffer mode. Fullscreen and High-DPI scaling were completely redesigned, and the skeletal animation system was rebuilt to support blending between animations. The examples collection grew past 215 entries, and a dedicated examples management tool was introduced to streamline contributions.

## Features

raylib offers the following features:

- Support for multiple platforms, including Windows, Linux, macOS, Raspberry Pi Android and HTML5
- Support for OpenGL 1.1, 2.1, 3.3, 4.3 and OpenGL ES 2.0, 3.0 as graphic API
- Image, textures and fonts loading and drawing from several formats
- Audio loading and playing from several formats and streaming support
- Math operations for vectors, matrices, and quaternions
- 2D rendering with a camera, including automatic sprites batching
- 3D models rendering including custom shaders and postprocessing shaders
- Support for VR simulations with configurable HMD device parameters
- Support for animated as well as non-animated 3D and 2D models

## Example

This is a simple example that creates a window with text, given on the GitHub page of Raylib.

```mw
#include "raylib.h"

int main(void) {
    InitWindow(800, 450, "raylib [core] example - basic window");

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY);
        EndDrawing();
    }

    CloseWindow();

    return 0;
}
```

## Reception and adoption

As of April 2026, GitHub lists around 2500 projects matching the `raylib` topic.

## Software architecture

### Modules

raylib consists of several modules that are exposed to the programmer through the API.

- core – Handles the window creation and OpenGL context initialization as well as inputs management (keyboard, mouse, gamepad and touch input)
- rlgl – Handles OpenGL backend, abstracting multiple versions to a common API. This module can be used standalone.
- shapes – Handles basic 2D shape rendering (line, rectangle, circle...) and basic collision detection
- textures – Handles image and texture loading (CPU and GPU) and management, including image manipulation functionality (crop, scale, tint, etc.)
- text – Handles fonts loading as spritesheet and text rendering. Also includes some text processing functionality (join, split, replace, etc.)
- models – Handles 3D model loading and rendering, including support for animated models
- raudio – Handles audio device management and audio file loading and playback, including streaming support. This module can be used standalone.
- raymath – Provides a set of math functions for vectors, matrices and quaternions

### Bindings

raylib has bindings for more than 70 different programming languages, created by various language communities. Computer programming languages that are updated to the latest version include: C#, Crystal, D (Dlang), Fortran, Go, Jai, Java, Lua, Nim, Python, Rust, V (Vlang), and Zig. There is also a C++ wrapper for users of C++ who prefer a less C-like, more C++-idiomatic usage, and also can be imported as a C++ module. A list of bindings is available in the BINDINGS.md file in the raylib GitHub repository.

#### Example using raylib-cpp

The following is the same as the earlier example, using the C++ bindings from raylib-cpp.

```mw
import raylib;

using raylib::Texture;
using raylib::Window;
using namespace raylib::Colors;

int main(int argc, char* argv[]) {
    constexpr int SCREEN_WIDTH = 800;
    constexpr int SCREEN_HEIGHT = 450;

    Window window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - basic window");
    Texture logo("raylib_logo.png");

    window.SetTargetFPS(60);

    while (!window.ShouldClose()) {
        window.BeginDrawing();
        window.ClearBackground(RAYWHITE);
        raylib::DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY);

        logo.Draw(
            SCREEN_WIDTH / 2 - logo.GetWidth() / 2,
            SCREEN_HEIGHT / 2 - logo.GetHeight() / 2
        );

        window.EndDrawing();
    }

    return 0;
}
```

### Add-ons

The raylib community has contributed several add-ons to extend the features and connection of raylib with other libraries. Some of the modules are:

- raygui – Immediate mode GUI module for raylib
- physac – physics module intended to be used with raylib
- libpartikel – particle system module for raylib
- spine-raylib – Spine animations integration module for raylib
- cimgui-raylib – Dear Imgui integration module for raylib

## Awards

- In April 2019, Santamaria was awarded with the Google Open Source Peer Bonus award for contributing to the open-source ecosystem with raylib.
- In August 2020, raylib was awarded with an Epic MegaGrant by Epic Games to support its development.
- In April 2021, Santamaria was awarded with another Google Open Source Peer Bonus award for the same reasons.
- In March 2022, raylib was nominated for the Best Game Engine category on Mobile Games Awards 2022.

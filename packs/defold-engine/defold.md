---
title: "Defold"
source: https://en.wikipedia.org/wiki/Defold
domain: defold-engine
license: CC-BY-SA-4.0
tags: defold engine, defold game engine, lua game engine, defold editor
fetched: 2026-07-02
---

# Defold

**Defold** is a cross-platform, free, and source-available game engine developed by King, and later the Defold Foundation. It is used to create mostly two-dimensional (2D) games, but is fully capable of three-dimensional (3D) as well.

Defold is a downloadable desktop app, and ships with its own embedded IDE. Defold targets desktop, mobile, web, and console platforms. Defold is free-to-use and is source-available. Defold has over 30,000 users, and has been used to publish over 100 games. Exported games with Defold typically use less than 100kB RAM and very small bundle sizes, less than 2 MB, due to the Engine's modularization and efficient core.

## Features

Defold uses Lua for scripting, but also allows native extensions, written in C, C++, and target-specific native languages. Defold projects are organized as collections, which consist of a hierarchy of game objects containing in-game entities. Scripting between game objects is handled using the message-passing paradigm, which allows scripts to intercommunicate in call-response and event-based models. Defold's IDE natively supports in-editor Git tracking.

### Supported platforms

The Defold editor can be run on three platforms and natively supports targeting eight platforms. Defold supports exports for:

- Windows (32-bit and 64-bit)
- macOS (x86_64 and Apple Silicon)
- Linux
- HTML (HTML5 and WebAssembly)
- Android (32-bit and 64-bit)
- iOS
- Nintendo Switch (requires approval from Nintendo)
- PlayStation 4 (requires approval from Sony)
- PlayStation 5 (requires approval from Sony)

The editor is currently supported on:

- Windows (Vista or newer; 64-bit)
- macOS (11 Big Sur or newer)
- Ubuntu (18.04 or newer; 64-bit)

### Scripting and editor

Users communicate with the engine via a Lua API. LuaJIT is used on all platforms except HTML and just-in-time compilation is enabled on permitted platforms. Users can extend the engine using C, C++, Java, Objective-C, and JavaScript for platform-specific or more performant code. In addition, the community maintains TypeScript and Haxe bindings. Scripts are platform-agnostic.

The editor includes a visual scene editor, debugger, asset management, tilemap editor, and all templates required for bundling the game. Newer versions support hot-reloading, to make changes to assets and scripts without rebuilding the project.

### Rendering

The render pipeline can be customized via a render script API, which can be translated into OpenGL, OpenGL ES, Vulkan, or Metal (via MoltenVK) depending on the user's needs. Shaders can be written in GLSL for various post-processing effects.

### Engine extensions

Defold has support for extensions, which are plugins that extend the engine, where users can integrate auxiliary solutions into their projects. There are libraries for simplifying game systems, interacting with hardware, and integration with third-party software. Both the Defold Foundation and the community host their extensions on the Defold Asset Portal.

## History

Defold was created in 2008 by Christian Murray and Ragnar Svensson As a side-project while they were working at Avalanche Studios, and later as a full time business before being acquired by King in 2014. Defold was developed and used internally at King for a few years before the decision was made to make Defold available to developers outside of King. The announcement and release of Defold as a free to use game engine was made at the Game Developers Conference in San Francisco in March 2016. Some mobile developers expressed concern about King's long term intentions for the engine, as well as the lack of a clear business goal. Development has continued with bi-weekly incremental releases of the engine and editor, with a major milestone being the release of the new editor in 2017. Defold was nominated for best engine in the 2018 Develop Awards, the 2018 and 2019 Mobile Games Awards.

In 2020, the Defold Foundation was established to oversee the development and stewardship of the engine, ensuring its independence from any single entity. In the process, the source code for the engine was made public. King released the source on GitHub as open source game engine, but community of developers questioned the choice of license, as it was initially unclear. Many assumed it was released under an Apache 2.0 - popular open source license. However, King had used a custom license that prevented commercialization of the Defold editor, so that Defold would always remain free for developers to use, calling into question whether it could be considered open source as defined by the Free Software Foundation and the Open Source Initiative. Shortly after, Defold added support for Nintendo Switch target platform exports.

## Licensing

Defold is released under the "Defold License" which is derived from the permissive Apache License, Version 2.0. The engine is "source available" and developers can access the engine's source code on GitHub.

The "Defold License" license permits any use of the code except for the sale of the Defold engine itself. However, games made with the Defold Engine are unaffected and can be distributed freely without restriction or royalties.

## Funding

The Defold Foundation is funded entirely by community donations and corporate partnerships. The Defold engine is maintained by both the Defold foundation and open source developers.

---
title: "Löve (game framework)"
source: https://en.wikipedia.org/wiki/L%C3%96VE_(game_framework)
domain: love2d
license: CC-BY-SA-4.0
tags: love2d framework, love game framework, lua game framework, luajit game
fetched: 2026-07-02
---

# Löve (game framework)

(Redirected from

LÖVE (game framework)

)

**Löve** (stylized in all caps) is a free, open-source, cross-platform framework released under the zlib license for developing video games. The framework is written in C++ and uses Lua as its scripting language and is still maintained by its original developers. The framework is cross-platform supporting the platforms Microsoft Windows, macOS, Linux, Android, and iOS.

The API provided by the framework gives access to the video and sound functions of the host machine through the libraries SDL and OpenGL, or since version 0.10 also OpenGL ES 2 and 3. Fonts can be rendered by the FreeType engine. A version of the framework called piLöve has been specifically ported to Raspberry Pi.

The framework is frequently found in the compositions of video game development competitions, such as the game development competition Ludum Dare. In July 2018, it was the 10th most popular game development software used by independent game developers on the site Itch.io, holding a 1.97% share.

## Version history

| Version | Code name | Added | Release date |
|---|---|---|---|
| 0.1.1 | Santa-Power | Reading and displaying images. Reading and playing sounds. Loading and rendering fonts. Keyboard and mouse support. | January 13, 2008 |
| 0.2.0 | Mini-Moose | Added a screen that displays if no game is loaded. Adding an animation system. Added text formatting functions. | February 6, 2008 |
| 0.2.1 | Impending Doom | Added many filesystem functions. Added dedicated save folders for games. | March 29, 2008 |
| 0.3.0 | Mutant Vermin | Addition of the particle system. | June 17, 2008 |
| 0.3.1 | Meat Space | Bug fixes. | June 21, 2008 |
| 0.3.2 | Lemony Fresh | Added several graphical functions. | July 4, 2008 |
| 0.4.0 | Taco Beam | Added physics engine Box2D. | August 29, 2008 |
| 0.5.0 | Salted Nuts | Added joystick support. Support of protocols TCP/UDP using luasocket. | January 2, 2009 |
| 0.6.0 | Jiggly Juice | Removed the animation system. Added support for managing events like key presses. | December 24, 2009 |
| 0.6.1 | Jiggly Juice | Added function to set and get a Box2D body's fixed rotation. Added function to set the inertia of a Box2D body. | February 7, 2010 |
| 0.6.2 | Jiggly Juice | Bug fixes. | March 6, 2010 |
| 0.7.0 | Game Slave | Added support for working with fonts. | December 5, 2010 |
| 0.7.1 | Game Slave | Bug fixes. | February 14, 2011 |
| 0.7.2 | Game Slave | Updated libraries for Windows version. | May 4, 2011 |
| 0.8.0 | Rubber Piggy | Added UTF-8 support for fonts. Added PNG and JPEG encoding. | April 2, 2012 |
| 0.9.0 | Baby Inspector | Added better multiplayer networking support. | December 13, 2013 |
| 0.9.1 | Baby Inspector | Added support for opening a URL with a web or file browser. | April 1, 2014 |
| 0.9.2 | Baby Inspector | Added UTF-8 encoding support. | February 14, 2015 |
| 0.10.0 | Super Toast | Supports Android and iOS. Added touch screen support. Added video support. | December 22, 2015 |
| 0.10.1 | Super Toast | Added configuration option for saving files in internal or external storage on Android devices. | February 14, 2016 |
| 0.10.2 | Super Toast | Added the ability to restart the application. | October 31, 2016 |
| 11.0 | Mysterious Mysteries | Support for meshes. Various additions to shaders (such as the `effect` method). Ability to record from a microphone. Consolidation of many object methods into new methods. Added many new formats to stencil/depth buffers. Audio effects such as reverberation and echoing. Added support for Base64 encoding, MD5 hashing, and more. | April 1, 2018 |
| 11.1 | Mysterious Mysteries | Bug fixes. | April 15, 2018 |
| 11.2 | Mysterious Mysteries | Added functions to set and get a Box2D body's transform. | November 25, 2018 |
| 11.3 | Mysterious Mysteries | Added support for loading FLAC audio files. Added support for recording audio from the microphone on Android devices. Added support for uncompressed DirectDraw Surface files. | October 27, 2019 |
| 11.4 | Mysterious Mysteries | Added native Apple Silicon support on macOS. | January 22, 2022 |
| 11.5 | Mysterious Mysteries | Added new game launcher on Android for easier loading of games. | December 3, 2023 |
| 12.0 | Bestest Friend |   | In development |

## Features

The framework provides these features:

- OpenGL pixel shaders GLSL.
- Touchscreen for mobile devices.
- Joysticks by providing interface for connected joysticks.
- UTF-8.
- Image formats: PNG, JPEG, GIF, TGA and BMP.
- Audio formats: WAV, OGG, and MP3.
- Video formats: OGV.
- The physics engine Box2D, which can be disabled to lighten the library.
- LuaSocket library for network communications TCP/UDP.
- Lua-enet library, another network library implementing Enet, a reliable protocol based on UDP.

## Notable games

Some of the games that have been made with LÖVE:

- *Kingdom Rush* (2011)
- *Mari0* (2012)
- *Oh My Giraffe* (2014)
- *Blue Revolver* (2016)
- *Move or Die* (2016)
- *Warlock's Tower* (2017)
- *Aeon of Sands - The Trail* (2018)
- *BYTEPATH* (2018)
- *Metanet Hunter G4* (2020)
- *Intravenous* series (2021-2024)
- *Gravity Circuit* (2023)
- *Moonring* (2023)
- *Balatro* (2024)
- *Arco* (2024)

## Libraries and implementations

There are various libraries and forks of LÖVE to improve basic functions, such as OOP with inheritance and overloading, interpolations, cameras, gamestates, etc. This is a small list of some:

- The Simple Tiled Implementation library allows users to load levels as tiles, edit using Tiled and display them in games. It works in conjunction with Box2D for collision management with this decor.
- The anim8 library allows users to load animations, for characters for example, from an image grid into a bitmap file (PNG or JPEG).
- LIKO-12 is a free platform inspired by the PICO-8 *fantasy console* and uses LÖVE. It allows users to develop applications in a limited resolution, backup/restore in the modified PNG format, in the same way as video game cartridges or some of the first microcomputers, and export them to HTML5 or to systems supported by LÖVE.
- Lutro is a Lua game framework for libretro, a partial port of the LÖVE API. ChaiLove follows a similar path by offering an implementation in ChaiScript, an embedded and cross-platform scripting language for C++ (C++14).
- love.js is a port of LÖVE that aims to make it possible to run LÖVE games on the web via HTML5, WebGL, and Emscripten.
- g3d is a 3D engine that simplifies 3D capabilities in LÖVE. It allows for 3D model rendering, .obj file loading, first person movement and camera controls, perspective and orthographic projections, 3D collisions and more.

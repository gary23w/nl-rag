---
title: "Graphics library"
source: https://en.wikipedia.org/wiki/Graphics_library
domain: fltk-toolkit
license: CC-BY-SA-4.0
tags: fltk toolkit, lightweight gui library, cross-platform widgets, opengl windowing
fetched: 2026-07-02
---

# Graphics library

A **graphics library** or **graphics API** is a program library designed to aid in rendering computer graphics to a monitor. This typically involves providing optimized versions of functions that handle common rendering tasks. This can be done purely in software and running on the CPU, common in embedded systems, or being hardware accelerated by a GPU, more common in PCs. By employing these functions, a program can assemble an image to be output to a monitor. This relieves the programmer of the task of creating and optimizing these functions, and allows them to focus on building the graphics program. Graphics libraries are mainly used in video games and simulations.

The use of graphics libraries in connection with video production systems, such as Pixar RenderMan, is not covered here.

| OS | Vulkan | Direct X | GNMX | Metal |
|---|---|---|---|---|
| Windows 10 | Free, Nvidia and AMD | Free, MS | no | no |
| Mac | Free, MoltenVK | no | no | Free, Apple |
| Linux | Free | no | no | no |
| Android | Free | no | no | no |
| iOS | Free, MoltenVK | no | no | Free, Apple |
| Tizen | in Development | no | no | no |
| Sailfish | in Development | no | no | no |
| Xbox One | no | Free | no | no |
| Orbis OS (PS4) | no | no | Free | no |
| Nintendo Switch | Free | no | no | no |
| HarmonyOS | Free | no | no | no |
| OpenHarmony | Free | no | no | no |

Some APIs use Graphics Library (GL) in their name, notably OpenGL and WebGL.

## Hardware

### Dedicated Graphics Processor (Graphics Card)

Dedicated graphics processors use RAM allocated directly to the graphics processor rather than the computer’s main system memory. This RAM is usually specifically selected with the expected sequential load of the graphics card in mind (see GDDR). Sometimes systems with dedicated discrete graphics processors were called “DIS” systems in contrast to “UMA” systems. Technologies such as 3dfx's Scan-Line Interleave, Nvidia's SLI and NVLink, and AMD's CrossFire allow multiple graphics processors to simultaneously display images on one screen, increasing the computational power available for graphics processing. However, these technologies are becoming increasingly rare; most games do not utilize all the capabilities of multiple graphics processors since most users cannot afford them.

### Integrated Graphics Processor

Today, laptops and mini-PCs require powerful integrated graphics. In many cases, quality integrated graphics can replace a discrete graphics card, enhancing laptop portability and mini-PC compactness while maintaining performance. Integrated graphics processors (IGPU), integrated graphics, shared graphics solutions, integrated graphics processors (IGP), or unified memory architectures (UMA) use part of the computer’s RAM rather than dedicated graphics memory. IGP may be integrated into the motherboard as part of its northbridge chipset or on a single chip (integrated circuit) with the central processor (e.g., AMD APU or Intel HD Graphics). On some motherboards, AMD’s IGP may use sideport dedicated memory: a separate fixed block of high-performance memory allocated for use by the graphics processor. As of early 2007, computers with integrated graphics accounted for about 90% of all PC shipments. They are less expensive to implement than dedicated graphics processing but generally less powerful. Historically, integrated processing was considered unsuitable for 3D games or graphics-intensive applications but could run less resource-demanding programs like Adobe Flash. Examples of such IGPs include offerings from SiS and VIA around 2004. However, modern integrated graphics processors such as AMD Accelerated Processing Unit and Intel Graphics Technology (HD, UHD, Iris, Iris Pro, Iris Plus, and Xe-LP) can handle 2D graphics or undemanding 3D graphics. In systems with a “unified memory architecture” (UMA), including modern AMD processors with integrated graphics, modern Intel processors with integrated graphics, Apple processors, PS5, and Xbox Series (among others), the CPU cores and GPU unit share the same pool of RAM and memory address space.

## Examples

- Allegro
- ANGLE
- Cairo (graphics)
- DFPSR https://dawoodoz.com/dfpsr.html — GUI toolkit and software renderer
- DirectX — a library created by Microsoft, to run under Windows operating systems and 'Direct' Xbox
- Display PostScript
- emWin — an Embedded Graphics Library
- FLTK — GUI Toolkit and Graphics Library
- GTK — a GUI toolkit
- Mesa 3D — a library that implements OpenGL and Vulkan
- Mobile 3D Graphics API
- Qt — cross-platform application framework
- Quartz (graphics layer)
- SFML
- SIGIL — Sound, Input, and Graphics Integration Library
- Simple DirectMedia Layer (SDL)
- Skia Graphics Library
- X Window System

---
title: "Direct3D (part 2/2)"
source: https://en.wikipedia.org/wiki/Direct3D
domain: wine-compatibility-layer
license: CC-BY-SA-4.0
tags: wine compatibility layer, windows api reimplementation, dxvk translation, compatibility layer
fetched: 2026-07-02
part: 2/2
---

## Multithreading

WDDM driver model in Windows Vista and higher supports arbitrarily large number of execution contexts (or threads) in hardware or in software. Windows XP only supported multitasked access to Direct3D, where separate applications could execute in different windows and be hardware accelerated, and the OS had limited control about what the GPU could do and the driver could switch execution threads arbitrarily.

The ability to execute the runtime in a multi-threaded mode has been introduced with Direct3D 11 runtime. Each execution context is presented with a resource view of the GPU. Execution contexts are protected from each other, however a rogue or badly written app can take control of the execution in the user-mode driver and could potentially access data from another process within GPU memory by sending modified commands. Though protected from access by another app, a well-written app still needs to protect itself against failures and device loss caused by other applications.

The OS manages the threads all by itself, allowing the hardware to switch from one thread to the other when appropriate, and also handles memory management and paging (to system memory and to disk) via integrated OS-kernel memory management.

Finer-grained context switching, i.e. being able to switch two execution threads at the shader-instruction level instead of the single-command level or even batch of commands, was introduced in WDDM/DXGI 1.2 which shipped with Windows 8. This overcomes a potential scheduling problem when application would have very long execution of a single command/batch of commands and will have to be terminated by the OS watchdog timer.

WDDM 2.0 and DirectX 12 have been reengineered to allow fully multithreaded draw calls. This was achieved by making all resources immutable (i.e. read-only), serializing the rendering states and using draw call bundles. This avoids complex resource management in the kernel-mode driver, making possible multiple reentrant calls to the user-mode driver via concurrent executions contexts supplied by separate rendering threads in the same application.


## Direct3D Mobile

Direct3D Mobile is derived from Direct3D but has a smaller memory footprint. Windows CE provides Direct3D Mobile support.


## Alternative implementations

The following alternative implementations of Direct3D API exist. They are useful for non-Windows platforms and for hardware without some versions of DX support:

- **DXVK** – An open source Vulkan-based translation layer for Direct3D 8/9/10/11 which allows running 3D applications on Linux using Wine. It is used by Proton/Steam for Linux. DXVK is able to run a large number of modern Windows games under Linux.
  - **D7VK** – A DXVK fork exclusively for Direct3D 3, 5, 6, and 7.
  - **D8VK** – An obsolete fork of DXVK for adding Direct3D 8 support on Linux. It was merged with DXVK version 2.4 which was released on July 10, 2024.
  - **D9VK** – An obsolete fork of DXVK for adding Direct3D 9 support, included with Steam/Proton on Linux. On December 16, 2019 D9VK was merged into DXVK.
- **Gallium Nine** – Gallium Nine makes it possible to run Direct3D 9 applications on Linux natively, i.e. without any calls translation which allows for a near native speed. It depends on Wine and Mesa.
- **vkd3d** – vkd3d is an open source 3D graphics library built on top of Vulkan which allows to run Direct3D 12 applications on top of Vulkan. It's primarily used by the Wine project, and is now included with Valve's Proton project bundled with Steam on Linux.
- **WineD3D** – The Wine open source project has working implementations of the Direct3D APIs via translation to OpenGL. Wine's implementation can also be run on Windows under certain conditions.

### D3DX

Direct3D comes with D3DX, a library of tools designed to perform common mathematical calculations on vectors, matrices and colors, calculating look-at and projection matrices, spline interpolations, and several more complicated tasks, such as compiling or assembling shaders used for 3D graphic programming, compressed skeletal animation storage and matrix stacks. There are several functions that provide complex operations over 3D meshes like tangent-space computation, mesh simplification, precomputed radiance transfer, optimizing for vertex cache friendliness and stripification, and generators for 3D text meshes. 2D features include classes for drawing screen-space lines, text and sprite based particle systems. Spatial functions include various intersection routines, conversion from/to barycentric coordinates and bounding box/sphere generators. D3DX is provided as a dynamic link library (DLL). D3DX is deprecated from Windows 8 onward and can't be used in Windows Store apps.

Some features present in previous versions of D3DX were removed in Direct3D 11 and now provided as separate sources:

- Windows SDK and Visual Studio
- A large part of the math library has been removed. Microsoft recommends use of the DirectX Math library instead.
- Spherical harmonics math has been removed and is now distributed as source.
- The Effect framework has been removed and is now distributed as source via CodePlex.
- The Mesh interface and geometry functions have been removed and are now distributed as source via CodePlex under DirectXMesh geometry processing library.
- Texture functions have been removed and are now distributed as source via CodePlex under DirectXTex texture processing library.
- General helpers have been removed and are now distributed as source via CodePlex under DirectX Tool Kit (DirectXTK) project.
- The isochart texture atlas has been removed and is now distributed as source via CodePlex under UVAtlas project.

### DXUT

DXUT (also called the sample framework) is a layer built on top of the Direct3D API. The framework is designed to help the programmer spend less time with mundane tasks, such as creating a window, creating a device, processing Windows messages and handling device events. DXUT have been removed with the Windows SDK 8.0 and now distributed as source via CodePlex.

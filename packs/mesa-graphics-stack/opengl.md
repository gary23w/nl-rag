---
title: "OpenGL"
source: https://en.wikipedia.org/wiki/OpenGL
domain: mesa-graphics-stack
license: CC-BY-SA-4.0
tags: mesa graphics library, opengl implementation, direct rendering manager, gallium driver
fetched: 2026-07-02
---

# OpenGL

**OpenGL** (**Open Graphics Library**) is a cross-language, cross-platform application programming interface (API) for rendering 2D and 3D vector graphics. The API is typically used to interact with a graphics processing unit (GPU), to achieve hardware-accelerated rendering.

Silicon Graphics, Inc. (SGI) began developing OpenGL in 1991 and released it on June 30, 1992. It is used for a variety of applications, including computer-aided design (CAD), video games, scientific visualization, virtual reality, and flight simulation. Since 2006, OpenGL has been managed by the non-profit technology consortium Khronos Group.

## Design

The OpenGL specification describes an abstract application programming interface (API) for drawing 2D and 3D graphics. It is designed to be implemented mostly or entirely using hardware acceleration such as a GPU, although it is possible for the API to be implemented entirely in software running on a CPU.

The API is defined as a set of functions which may be called by the client program, alongside a set of named integer constants (for example, the constant GL_TEXTURE_2D, which corresponds to the decimal number 3553). Although the function definitions are superficially similar to those of the programming language C, they are language-independent. As such, OpenGL has many language bindings, some of the most noteworthy being the JavaScript binding WebGL (API, based on OpenGL ES 2.0, for 3D rendering from within a web browser); the C bindings WGL, GLX and CGL; the C binding provided by iOS; and the Java and C bindings provided by Android.

In addition to being language-independent, OpenGL is also cross-platform. The specification says nothing on the subject of obtaining and managing an OpenGL context, leaving this as a detail of the underlying windowing system. For the same reason, OpenGL is purely concerned with rendering, providing no APIs related to input, audio, or windowing.

### Development

New versions of the OpenGL specifications are released by the Khronos Group, each of which extends the API to support various new features. The details of each version are decided by consensus between the Group's members, including graphics card manufacturers, operating system designers, and general technology companies such as Mozilla and Google.

In addition to the features required by the core API, graphics processing unit (GPU) vendors may provide additional functionality in the form of *extensions*. Extensions may introduce new functions and new constants, and may relax or remove restrictions on existing OpenGL functions. Vendors can use extensions to expose custom APIs without needing support from other vendors or the Khronos Group as a whole, which greatly increases the flexibility of OpenGL. All extensions are collected in, and defined by, the OpenGL Registry.

The features introduced by each new version of OpenGL are typically formed from the combined features of several widely implemented extensions, especially extensions of type ARB or EXT.

OpenGL is no longer in active development; whereas between 2001 and 2014, OpenGL specification was updated mostly on a yearly basis, with two releases (3.1 and 3.2) taking place in 2009 and three (3.3, 4.0 and 4.1) in 2010. The latest OpenGL specification 4.6 was released in 2017 after a three-year break, and was limited to inclusion of eleven existing ARB and EXT extensions into the core profile.

Active development of OpenGL was dropped in favor of the Vulkan API, released in 2016, and codenamed glNext during initial development. In 2017, Khronos Group announced that OpenGL ES would not have new versions and has since concentrated on development of Vulkan and other technologies. As a result, certain capabilities offered by modern GPUs, e.g. ray tracing, are not supported by the OpenGL standard. However, support for newer features might be provided through the vendor-specific OpenGL extensions.

## Documentation

The OpenGL Architecture Review Board released a series of manuals along with the specification which have been updated to track changes in the API. These are commonly referred to by the colors of their covers:

**The Red Book**

OpenGL Programming Guide, 9th Edition.

ISBN

978-0-134-49549-1

The Official Guide to Learning OpenGL, Version 4.5 with SPIR-V

**The Orange Book**

OpenGL Shading Language, 3rd edition.

ISBN

0-321-63763-1

A tutorial and reference book for

GLSL

.

Historic books (pre-OpenGL 2.0):

**The Green Book**

OpenGL Programming for the X Window System.

ISBN

978-0-201-48359-8

A book about X11 interfacing and

OpenGL Utility Toolkit

(GLUT).

**The Blue Book**

OpenGL Reference manual, 4th edition.

ISBN

0-321-17383-X

Essentially a hard-copy printout of the

Unix manual

(man) pages for OpenGL.

Includes a poster-sized fold-out diagram showing the structure of an idealised OpenGL implementation.

**The Alpha Book (white cover)**

OpenGL Programming for Windows 95 and Windows NT.

ISBN

0-201-40709-4

A book about interfacing OpenGL with Microsoft Windows.

OpenGL's documentation is also accessible via its official webpage.

## Associated libraries

The earliest versions of OpenGL were released with a companion library called the OpenGL Utility Library (GLU). It provided simple, useful features which were unlikely to be supported in contemporary hardware, such as tessellating, and generating mipmaps and primitive shapes. The GLU specification was last updated in 1998 and depends on OpenGL features which are now deprecated.

### Context and window toolkits

Given that creating an OpenGL context is quite a complex process, and given that it varies between operating systems, automatic OpenGL context creation has become a common feature of several game-development and user-interface libraries, including SDL, Allegro, SFML, FLTK, and Qt. A few libraries have been designed solely to produce an OpenGL-capable window. The first such library was OpenGL Utility Toolkit (GLUT), later superseded by freeglut. GLFW is a newer alternative.

- These toolkits are designed to create and manage OpenGL windows, and manage input, but little beyond that.
  - GLFW – A cross-platform windowing and keyboard-mouse-joystick handler; is more game-oriented
  - freeglut – A cross-platform windowing and keyboard-mouse handler; its API is a superset of the GLUT API, and it is more stable and up to date than GLUT
  - OpenGL Utility Toolkit (GLUT) – An old windowing handler, no longer maintained.
- Several "multimedia libraries" can create OpenGL windows, in addition to input, sound and other tasks useful for game-like applications
  - Allegro 5 – A cross-platform multimedia library with a C API focused on game development
  - Simple DirectMedia Layer (SDL) – A cross-platform multimedia library with a C API
  - SFML – A cross-platform multimedia library with a C++ API and multiple other bindings to languages such as C#, Java, Haskell, and Go
- Widget toolkits
  - FLTK – A small cross-platform C++ widget library
  - Qt – A cross-platform C++ widget toolkit. It provides many OpenGL helper objects, which even abstract away the difference between desktop GL and OpenGL ES
  - wxWidgets – A cross-platform C++ widget toolkit

### Extension loading libraries

Given the high workload involved in identifying and loading OpenGL extensions, a few libraries have been designed which load all available extensions and functions automatically. Examples include OpenGL Easy Extension library (GLEE), OpenGL Extension Wrangler Library (GLEW) and glbinding. Extensions are also loaded automatically by most language bindings, such as Java OpenGL, PyOpenGL and WebGL.

### Implementations

Mesa 3D is an open-source implementation of OpenGL. It can do pure software rendering, and it may also use hardware acceleration on BSD, Linux, and other platforms by taking advantage of the Direct Rendering Infrastructure. As of version 20.0, it implements version 4.6 of the OpenGL standard.

## History

In the 1980s, developing software that could function with a wide range of graphics hardware was a challenge without a cross-platform library. Software developers wrote custom interfaces and drivers for each piece of hardware. This was expensive and resulted in multiplication of effort.

By the early 1990s, Silicon Graphics (SGI) was a leader in 3D graphics for workstations. Their IRIS GL API became the industry standard, as IRIS GL was considered easier to use, and it supported immediate mode rendering, therefore being faster than competitors like PHIGS.

SGI's competitors (including Sun Microsystems, Hewlett-Packard and IBM) were also able to bring to market 3D hardware supported by extensions made to the PHIGS standard, which pressured SGI to open source a version of IRIS GL as a public standard called **OpenGL**.

However, SGI had many customers for whom the change from IRIS GL to OpenGL would demand significant investment. Moreover, IRIS GL had API functions that were irrelevant to 3D graphics. For example, it included a windowing, keyboard and mouse API, in part because it was developed before the X Window System and Sun's NeWS. IRIS GL libraries were heavily tied into SGI's proprietary graphics hardware and could not be open sourced as-is due to hardware patents and trade secrets. These factors required SGI to continue to support the advanced and proprietary Iris Inventor and Iris Performer programming APIs while market support for OpenGL matured.

One of the restrictions of IRIS GL was that it only provided access to features supported by the underlying hardware. If the graphics hardware did not support a feature natively, then the application could not use it. OpenGL overcame this problem by providing software implementations of features unsupported by hardware, allowing applications to use advanced graphics on relatively low-powered systems. OpenGL standardized access to hardware, pushed the development responsibility of hardware interface programs (device drivers) to hardware manufacturers, and delegated windowing functions to the underlying operating system. With so many different kinds of graphics hardware, getting them all to speak the same language in this way had a remarkable impact by giving software developers a higher-level platform for 3D-software development.

In 1992, SGI led the creation of the OpenGL Architecture Review Board (OpenGL ARB), the group of companies that would maintain and expand the OpenGL specification in the future. Two years later, they also played with the idea of releasing something called "OpenGL++" which included elements such as a scene-graph API (presumably based on their Performer technology). The specification was circulated among a few interested parties – but never turned into a product.

Released in 1996, Microsoft's Direct3D eventually became the main competitor of OpenGL. Over 50 game developers signed an open letter to Microsoft, released on June 12, 1997, calling on the company to actively support OpenGL. On December 17, 1997, Microsoft and SGI initiated the Fahrenheit project, which was a joint effort with the goal of unifying the OpenGL and Direct3D interfaces (and adding a scene-graph API too). In 1998, Hewlett-Packard joined the project. It initially showed some promise of bringing order to the world of interactive 3D computer graphics APIs, but on account of financial constraints at SGI, strategic reasons at Microsoft, and a general lack of industry support, it was abandoned in 1999.

In July 2006, the OpenGL Architecture Review Board voted to transfer control of the OpenGL API standard to the Khronos Group.

### Industry support

OpenGL was the standard for many CAD software (such as Blender) and games in the 1990s and 2000s, and faces wide support across virtually all hardware vendors. Despite the emergence of newer graphics APIs like its successor Vulkan or Metal, OpenGL continues to be a widely used standard. This continued relevance is supported by several factors: ongoing development with new extensions and driver optimizations, its cross-platform compatibility, and the availability of compatibility layers like ANGLE and Zink. These layers allow OpenGL to run efficiently on top of Vulkan and Metal, offering a pathway for continued use or gradual transitions for developers.

However, the graphics API landscape has been shifting, where some companies are moving away from OpenGL. In June 2018, Apple deprecated OpenGL APIs on all of their platforms (iOS, macOS and tvOS), encouraging developers to use their proprietary Metal API, which was introduced in 2014.

Game developers have also begun to adopt newer APIs. id Software, who has been using OpenGL in their games since the late 1990s in games such as GLQuake or some games of the Doom franchise, transitioned away to its successor Vulkan in its id Tech 7 engine in 2016. They first supported Vulkan in an update for their id Tech 6 engine. The company's first licensed use of OpenGL was in its Quake II engine, also known as id Tech 2. In March 2023, Valve removed OpenGL support from Dota 2 in favor of Vulkan. Atypical Games, with support from Samsung, updated their game engine to use Vulkan, rather than OpenGL, across all non-Apple platforms.

The Khronos Group, the consortium responsible for OpenGL's development, has stopped updating OpenGL, with the last release made in 2017. It has not received a number of modern graphics technologies, such as hardware accelerated Ray Tracing, on-GPU video decoding, and advanced anti-aliasing algorithms like Nvidia DLSS and AMD FSR. Another modern feature, Mesh Shaders, was initially only supported through an Nvidia exclusive extension, however in 2025, a cross-vendor OpenGL Mesh Shader extension was released.

Google's Fuchsia OS, while using Vulkan natively and requiring a Vulkan-conformant GPU, still intends to support OpenGL on top of Vulkan via the ANGLE translation layer.

## Version history

The first version of OpenGL, version 1.0, was released on June 30, 1992, by Mark Segal and Kurt Akeley. Since then, OpenGL has occasionally been extended by releasing a new version of the specification. Such releases define a baseline set of features which all conforming graphics cards must support, and against which new extensions can more easily be written. Each new version of OpenGL tends to incorporate several extensions which have widespread support among graphics-card vendors, although the details of those extensions may be changed.

| Version | Release Date | Features |
|---|---|---|
| 1.0 | June 30, 1992 | Initial release. |
| 1.1 | March 4, 1997 | Texture objects, Vertex Arrays |
| 1.2 | March 16, 1998 | 3D textures, BGRA and packed pixel formats, introduction of the *imaging subset* useful to image-processing applications |
| 1.2.1 | October 14, 1998 | A concept of ARB extensions |
| 1.3 | August 14, 2001 | Multitexturing, multisampling, texture compression |
| 1.4 | July 24, 2002 | Depth textures, GLSlang |
| 1.5 | July 29, 2003 | Vertex Buffer Object (VBO), Occlusion Queries |
| 2.0 | September 7, 2004 | GLSL 1.1, MRT, Non Power of Two textures, Point Sprites, Two-sided stencil |
| 2.1 | July 2, 2006 | GLSL 1.2, Pixel Buffer Object (PBO), sRGB Textures |
| 3.0 | August 11, 2008 | GLSL 1.3, Texture Arrays, Conditional rendering, Frame Buffer Object (FBO) |
| 3.1 | March 24, 2009 | GLSL 1.4, Instancing, Texture Buffer Object, Uniform Buffer Object, Primitive restart |
| 3.2 | August 3, 2009 | GLSL 1.5, Geometry Shader, Multi-sampled textures |
| 3.3 | March 11, 2010 | GLSL 3.30, Retain as much OpenGL 4.0 functionality as possible, New blending functions, Sampler Objects, new texture and vertex formats |
| 4.0 | March 11, 2010 | GLSL 4.00, Tessellation on GPU, shaders with 64-bit precision |
| 4.1 | July 26, 2010 | GLSL 4.10, Developer-friendly debug outputs, compatibility with OpenGL ES 2.0 |
| 4.2 | August 8, 2011 | GLSL 4.20, Shaders with atomic counters, draw transform feedback instanced, shader packing, performance improvements |
| 4.3 | August 6, 2012 | GLSL 4.30, Compute shaders leveraging GPU parallelism, shader storage buffer objects, high-quality ETC2/EAC texture compression, increased memory security, a multi-application robustness extension, compatibility with OpenGL ES 3.0 |
| 4.4 | July 22, 2013 | GLSL 4.40, Buffer Placement Control, Efficient Asynchronous Queries, Shader Variable Layout, Efficient Multiple Object Binding, Streamlined Porting of Direct3D applications, Bindless Texture Extension, Sparse Texture Extension |
| 4.5 | August 11, 2014 | GLSL 4.50, Direct State Access (DSA), Flush Control, Robustness, OpenGL ES 3.1 API and shader compatibility, DX11 emulation features |
| 4.6 | July 31, 2017 | GLSL 4.60, More efficient geometry processing and shader execution, more information, no error context, polygon offset clamp, SPIR-V, anisotropic filtering |

### OpenGL 2.0

*Release date*: September 7, 2004

OpenGL 2.0 was originally conceived by 3Dlabs to address concerns that OpenGL was stagnating and lacked a strong direction. 3Dlabs proposed a number of major additions to the standard. Most of these were, at the time, rejected by the ARB or otherwise never came to fruition in the form that 3Dlabs proposed. However, their proposal for a C-style shading language was eventually completed, resulting in the current formulation of the OpenGL Shading Language (GLSL or GLslang). Like the assembly-like shading languages it was replacing, it allowed replacing the fixed-function vertex and fragment pipe with shaders, though this time written in a C-like high-level language.

The design of GLSL was notable for making relatively few concessions to the limits of the hardware then available. This harked back to the earlier tradition of OpenGL setting an ambitious, forward-looking target for 3D accelerators rather than merely tracking the state of currently available hardware. The final OpenGL 2.0 specification includes support for GLSL 1.10.

### OpenGL 2.1

*Release date*: July 2, 2006

OpenGL 2.1 adds support for Pixel Buffer Objects, sRGB textures and GLSL 1.20.

### Longs Peak and OpenGL 3.0

Before the release of OpenGL 3.0, the new revision had the codename Longs Peak. At the time of its original announcement, Longs Peak was presented as the first major API revision in OpenGL's lifetime. It consisted of an overhaul to the way that OpenGL works, calling for fundamental changes to the API.

The draft introduced a change to object management. The GL 2.1 object model was built upon the state-based design of OpenGL. That is, to modify an object or to use it, one needs to bind the object to the state system, then make modifications to the state or perform function calls that use the bound object.

Because of OpenGL's use of a state system, objects must be mutable. That is, the basic structure of an object can change at any time, even if the rendering pipeline is asynchronously using that object. A texture object can be redefined from 2D to 3D. This requires any OpenGL implementations to add a degree of complexity to internal object management.

Under the Longs Peak API, object creation would become atomic, using templates to define the properties of an object which would be created with one function call. The object could then be used immediately across multiple threads. Objects would also be immutable; however, they could have their contents changed and updated. For example, a texture could change its image, but its size and format could not be changed.

To support backwards compatibility, the old state based API would still be available, but no new functionality would be exposed via the old API in later versions of OpenGL. This would have allowed legacy code bases, such as the majority of CAD products, to continue to run while other software could be written against or ported to the new API.

Longs Peak was initially due to be finalized in September 2007 under the name OpenGL 3.0, but the Khronos Group announced on October 30 that it had run into several issues that it wished to address before releasing the specification. As a result, the spec was delayed, and the Khronos Group went into a media blackout until the release of the final OpenGL 3.0 spec.

The final specification proved far less revolutionary than the Longs Peak proposal. Instead of removing all immediate mode and fixed functionality (non-shader mode), the spec included them as deprecated features. The proposed object model was not included, and no plans have been announced to include it in any future revisions. As a result, the API remained largely the same with a few existing extensions being promoted to core functionality. Among some developer groups this decision caused something of an uproar, with many developers professing that they would switch to DirectX in protest. Most complaints revolved around the lack of communication by Khronos to the development community and multiple features being discarded that were viewed favorably by many. Other frustrations included the requirement of DirectX 10 level hardware to use OpenGL 3.0 and the absence of geometry shaders and instanced rendering as core features.

Other sources reported that the community reaction was not quite as severe as originally presented, with many vendors showing support for the update.

### OpenGL 3.0

*Release date*: August 11, 2008

OpenGL 3.0 introduced a deprecation mechanism to simplify future revisions of the API. Certain features, marked as deprecated, could be completely disabled by requesting a *forward-compatible context* from the windowing system. OpenGL 3.0 features could still be accessed alongside these deprecated features, however, by requesting a *full context*.

Deprecated features include:

- All fixed-function vertex and fragment processing
- Direct-mode rendering, using glBegin and glEnd
- Display lists
- Indexed-color rendering targets
- OpenGL Shading Language version 1.30

Hardware support: Nvidia GeForce 8 Series and newer, ATI Radeon HD 2000 series and newer, Intel HD Graphics in Intel Sandy Bridge processors and newer.

### OpenGL 3.1

*Release date*: March 24, 2009

OpenGL 3.1 fully removed all of the features which were deprecated in version 3.0, with the exception of wide lines. From this version onwards, it's not possible to access new features using a *full context*, or to access deprecated features using a *forward-compatible context*. An exception to the former rule is made if the implementation supports the ARB_compatibility extension, but this is not guaranteed. Includes support for GLSL 1.40.

Hardware support: Mesa supports ARM Panfrost with Version 21.0.

### OpenGL 3.2

*Release date*: August 3, 2009

OpenGL 3.2 further built on the deprecation mechanisms introduced by OpenGL 3.0, by dividing the specification into a *core profile* and *compatibility profile*. Compatibility contexts include the previously removed fixed-function APIs, equivalent to the ARB_compatibility extension released alongside OpenGL 3.1, while core contexts do not. OpenGL 3.2 also included an upgrade to GLSL version 1.50.

### OpenGL 3.3

*Release date:* March 11, 2010

OpenGL 3.3 includes minor additions, with the goal of retaining as much functionality as possible from OpenGL 4.0, while keeping support for older hardware. Additions include new blending functions, Sampler Objects and new texture and vertex formats. Support is also added for GLSL version 3.30, major and minor versions now match with OpenGL.

### OpenGL 4.0

*Release date*: March 11, 2010

OpenGL 4.0 was released alongside version 3.3. It was designed for hardware able to support Direct3D 11.

As in OpenGL 3.0, this version of OpenGL contains a high number of fairly inconsequential extensions, designed to thoroughly expose the abilities of Direct3D 11-class hardware, such as tessellation.

Hardware support: Nvidia GeForce 400 series and newer, AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel HD Graphics in Intel Ivy Bridge processors and newer.

### OpenGL 4.1

*Release date*: July 26, 2010

- Minimum "maximum texture size" is 16,384 × 16,384 for GPUs implementing this specification.
- Improved compatibility for OpenGL ES 2.0
- Multiple Viewports for the same rendering surface, or one per surface.

Hardware support: Nvidia GeForce 400 series and newer, AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel HD Graphics in Intel Haswell processors and newer (Linux Mesa: Ivy Bridge and newer). Additionally, this is the last core profile supported by Apple macOS.

### OpenGL 4.2

*Release date:* August 8, 2011

- Support for shaders with atomic counters and load-store-atomic read-modify-write operations to one level of a texture
- Drawing multiple instances of data captured from GPU vertex processing (including tessellation), to enable complex objects to be efficiently repositioned and replicated
- Support for modifying an arbitrary subset of a compressed texture, without having to re-download the whole texture to the GPU for significant performance improvements

Hardware support: Nvidia GeForce 400 series and newer, AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), and Intel HD Graphics in Intel Haswell processors and newer. (Linux Mesa: Ivy Bridge and newer)

### OpenGL 4.3

*Release date:* August 6, 2012

- Compute shaders leveraging GPU parallelism within the context of the graphics pipeline
- Shader storage buffer objects, allowing shaders to read and write buffer objects like image load/store from 4.2, but through the language rather than function calls.
- Image format parameter queries
- ETC2/EAC texture compression as a standard feature
- Full compatibility with OpenGL ES 3.0 APIs
- Debug abilities to receive debugging messages during application development
- Texture views to interpret textures in different ways without data replication
- Increased memory security and multi-application robustness

Hardware support: AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel HD Graphics in Intel Haswell processors and newer. (Linux Mesa: Ivy Bridge without stencil texturing, Haswell and newer), Nvidia GeForce 400 series and newer. VIRGL Emulation for virtual machines supports 4.3+ with Mesa 20.

### OpenGL 4.4

*Release date:* July 22, 2013

- Enforced buffer object usage controls
- Asynchronous queries into buffer objects
- Expression of more layout controls of interface variables in shaders
- Efficient binding of multiple objects simultaneously

Hardware support: AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel HD Graphics in Intel Broadwell processors and newer (Linux Mesa: Haswell and newer), Nvidia GeForce 400 series and newer, Tegra K1.

### OpenGL 4.5

*Release date:* August 11, 2014

- Direct State Access (DSA) – object accessors enable state to be queried and modified without binding objects to contexts, for increased application and middleware efficiency and flexibility.
- Flush Control – applications can control flushing of pending commands before context switching – enabling high-performance multithreaded applications;
- Robustness – providing a secure platform for applications such as WebGL browsers, including preventing a GPU reset affecting any other running applications;
- OpenGL ES 3.1 API and shader compatibility – to enable the easy development and execution of the latest OpenGL ES applications on desktop systems.

Hardware support: AMD Radeon HD 5000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel HD Graphics in Intel Broadwell processors and newer (Linux Mesa: Haswell and newer), Nvidia GeForce 400 series and newer, Tegra K1, and Tegra X1.

### OpenGL 4.6

*Release date:* July 31, 2017

- More efficient, GPU-sided, geometry processing
- More efficient shader execution (AZDO)
- More information through statistics, overflow query and counters
- Higher performance through no error handling contexts
- Clamping of polygon offset function, solves a shadow rendering problem
- SPIR-V shaders
- Improved anisotropic filtering

Hardware support: AMD Radeon HD 7000 series and newer (FP64 shaders implemented by emulation on some TeraScale GPUs), Intel Skylake and newer, Nvidia GeForce 400 series and newer.

Driver support:

- Mesa 19.2 on Linux supports OpenGL 4.6 for Intel Broadwell and newer. Mesa 20.0 supports AMD Radeon GPUs, while support for Nvidia Kepler+ arrived later. Zink as Emulation Driver with 21.1 and software driver LLVMpipe also support with Mesa 21.0.
- AMD Adrenalin 18.4.1 Graphics Driver on Windows 7 and 10 version 1803 (April 2018 update) for AMD Radeon HD 7700+, HD 8500+ and newer. Both 64-bit and 32-bit are supported. Released April 2018.
- Intel 26.20.100.6861 graphics driver on Windows 10, 64-bit only. Released May 2019.
- NVIDIA GeForce 387.92 graphics driver on Windows 7, 8, 8.1 and 10, both 64-bit and 32-bit are supported. Released October 2017.

## Alternative implementations

Apple deprecated OpenGL in iOS 12 and macOS 10.14 Mojave in favor of Metal, but it is still available as of macOS 15 Sequoia (including on Apple silicon devices). The latest version supported for OpenGL is 4.1 from 2011. A proprietary library from Molten – authors of MoltenVK – called MoltenGL, can translate OpenGL calls to Metal.

There are several projects that attempt to implement OpenGL on top of Vulkan. The Vulkan backend for Google's ANGLE achieved OpenGL ES 3.1 conformance in July 2020. The Mesa3D project also includes such a driver, called *Zink*.

Microsoft's Windows 11 on Arm added support for OpenGL 3.3 via GLon12, an open source OpenGL implementation on top DirectX 12 via Mesa Gallium.

## Vulkan

Vulkan, formerly named the "Next Generation OpenGL Initiative" (glNext), is a ground-up redesign effort to unify OpenGL and OpenGL ES into one common API that will not be backwards compatible with existing OpenGL versions.

The initial version of Vulkan API was released on February 16, 2016.

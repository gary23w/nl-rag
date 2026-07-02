---
title: "Mesa (computer graphics)"
source: https://en.wikipedia.org/wiki/Mesa_(computer_graphics)
domain: mesa-graphics-stack
license: CC-BY-SA-4.0
tags: mesa graphics library, opengl implementation, direct rendering manager, gallium driver
fetched: 2026-07-02
---

# Mesa (computer graphics)

**Mesa**, also called **Mesa3D** and **The Mesa 3D Graphics Library**, is an open source implementation of OpenGL, OpenGL ES, Vulkan, and other graphics API specifications, as well as OpenCL for GPU compute. Mesa implements these specifications with vendor-specific graphics hardware drivers, software rendering drivers, layered (translation) drivers, and more.

On Linux systems, GPU acceleration is provided primarily through Mesa. AMD supports the RadeonSI and RADV drivers in Mesa as their official GPU drivers on Linux. Intel has only ever supported the Mesa drivers on Linux systems. Google uses the Freedreno driver in Mesa in some Chromebooks with Qualcomm processors. Systems with Nvidia cards usually use the proprietary Nvidia GeForce driver, but there are ongoing efforts to write Mesa Nvidia drivers called Nouveau and NVK. As of 2026, NVK is still usually slower than the proprietary driver, but the performance gap is continually decreasing as it is developed further.

Besides 3D applications such as games, modern display servers (X.org's Glamor or Wayland's Weston) use OpenGL/EGL; therefore all graphics typically go through Mesa.

Mesa is hosted by freedesktop.org and was initiated in August 1993 by Brian Paul, who is still active in the project. Mesa was subsequently widely adopted and now contains numerous contributions from various individuals and corporations worldwide, including from most graphics hardware manufacturers, and other interested parties, such as Valve Corporation.

## Overview

### Implementations of rendering APIs

Mesa is known as housing implementations of graphic APIs. Historically the main API that Mesa has implemented is OpenGL, along with other Khronos Group related specifications (like OpenVG, OpenGL ES or recently EGL). But Mesa can implement other APIs and indeed it did with Glide (deprecated) and Direct3D 9 since July 2013. Mesa is also not specific to Unix-like operating systems: on Windows for example, Mesa provides an OpenGL API over DirectX.

Mesa implements a translation layer between a graphics API such as OpenGL and the graphics hardware drivers in the operating system kernel. The supported version of the different graphic APIs depends on the driver, because each hardware driver has its own implementation (and therefore status). This is especially true for the "classic" drivers, while the Gallium3D drivers share common code that tend to homogenize the supported extensions and versions.

Mesa maintains a support matrix with the status of the current OpenGL conformance visualized at mesamatrix.net.

#### Table of Rendering APIs

Mesa Version

First Release Date

Last update

Vulkan

OpenCL

OpenGL

OpenGL ES

OpenVG

EGL

GLX

Direct3D

1.4

2024-12-03

3.0

2020-11-30

4.6

2017-07-31

3.2.6

2019-07-10

1.1

2008-12-03

1.5

2014-03-19

1.4

2005-12-16

12

2015-07-29

Unsupported:

23.1

2023-05-10

23.1.8

1.3.244: 1.3+ (Intel Gen8+ to XE, AMD GCN Gen2+ to RDNA3, Lavapipe, Google Venus), 1.1+ (Qualcomm Turnip), 1.0+ (AMD GCN1, Broadcom v3dv, ARM Mali PanVK)

1.0, 1.1, 1.2 (full support), 3.0 (wip, some functions in 21.1),

OpenCL 1.2+ and 3.0 with new RustiCL for AMD GCN and Intel Xe (Mesa 22.3+), AMD R600, Nvidia Fermi+ (Mesa 23.1+)

4.6 (19.3: Intel Gen 8+, 20.0: AMD GCN, 21.1: Zink, llvmpipe, 21.2: Intel Gen 7.5)

3.2 (20.3: Intel i965, AMD radeonsi, llvmpipe, VirGL, freedreno, Zink (21.3); 3.1: AMD r600, Nvidia nvC0, softpipe, Broadcom v3d, ARM Panfrost (21.3), d3d12 (22.0)

N/A

1.5

1.4

9.0c

Unsupported:

23.0

2023-02-23

23.0.4

1.3.232: mostly equal to 23.1

Unsupported:

22.3

2022-11-30

22.3.7

22.3: 1.3.225: 1.3+ (Intel Gen8+, AMD GCN Gen2+, Lavapipe), 1.2+ (Google Venus), 1.1+ (Qualcomm Turnip, Lavapipe (22.2)), 1.0+ (AMD GCN1, Broadcom v3dv, ARM Mali PanVK)

Unsupported:

22.2

2022-09-21

22.2.5

Unsupported:

22.1

2022-05-20

22.1.7

Unsupported:

22.0

2022-03-09

22.0.5

Unsupported:

21.3

2021-11-17

21.3.9

21.3: 1.2.190 (Intel Gen8+, AMD GCN Gen2+, Google Venus (21.3), Lavapipe), 1.0+ (AMD GCN1, Broadcom v3dv), 1.1+ (Qualcomm Turnip, Lavapipe (21.1))

Unsupported:

21.2

2021-08-04

21.2.6

Unsupported:

21.1

2021-05-05

21.1.8

Unsupported:

21.0

2021-03-11

21.0.3

Unsupported:

20.3

2020-12-03

20.3.5

20.3: 1.2.158 (Intel Gen8+, AMD GCN Gen2+), 1.0+ (AMD GCN1, Broadcom v3dv (20.3))

Unsupported:

20.2

2020-09-28

20.2.6

1.0, 1.1, 1.2 (WIP) some failed conformance tests

Unsupported:

20.1

2020-05-27

20.1.10

Unsupported:

20.0

2020-02-19

20.0.8

1.2+ (Intel Gen8+, AMD GCN Gen2+)

Unsupported:

19.3

2019-12-11

19.3.5

1.1+ (Intel Gen8+, AMD GCN Gen2+) (19.1: 1.1.104 19.0: 1.1.102, 18.3: 1.1.90, 18.2: 1.1.84)

Unsupported:

19.2

2019-09-25

19.2.8

4.5

Unsupported:

19.1

2019-06-11

19.1.8

Unsupported:

19.0

2019-03-13

19.0.8

Unsupported:

18.3

2018-12-07

18.3.6

Unsupported:

18.2

2018-09-07

18.2.8

Unsupported:

18.1

2018-05-18

18.1.9

1.1 (Intel Gen8+, AMD GCN Gen2+)(1.1.73)

Unsupported:

18.0

2018-03-27

18.0.5

1.0+ (1.0.66)

Unsupported:

17.3

2017-12-08

17.3.9

1.0 (PC: ANV Intel Gen7+ Ivy Bridge, RADV AMD GCN only) (header: 17.3: 1.0.63, 17.2: 1.0.54, 17.1: 1.0.42, 17.0: 1.0.38, 13.0: 1.0.6, 12.0: 1.0.3)

in dev. by Gallium

Compute (Clover):

some CTS-Tests fail

in 1.0 and 1.1,

1.2 (WIP),

so 1.0, 1.1, 1.2

incomplete

Unsupported:

17.2

2017-09-04

17.2.8

Unsupported:

17.1

2017-05-10

17.1.10

Unsupported:

17.0

2017-02-13

17.0.7

Unsupported:

13.0

2016-11-01

13.0.6

4.4

(4.5 No Test Label)

Unsupported:

12.0

2016-07-08

12.0.6

4.3

3.1

Unsupported:

11.2

2016-04-04

11.2.2

N/A

4.1 (Intel 3.3+)

Unsupported:

11.1

2015-12-15

11.1.4

3.0

Unsupported:

11.0

2015-09-12

11.0.9

Unsupported:

10.6

2015-06-15

10.6.9

3.3

1.4

Unsupported:

10.5

2015-03-06

10.5.9

1.1

Unsupported:

10.4

2014-12-14

10.4.7

Unsupported:

10.3

2014-09-19

10.3.7

N/A

Unsupported:

10.2

2014-06-06

10.2.9

Unsupported:

10.1

2014-03-04

10.1.6

Unsupported:

10.0

2013-11-30

10.0.5

Unsupported:

9.0

2012-10-08

9.0.3, 9.1.7, 9.2.5

N/A

3.1

2.0

Unsupported:

8.0

2012-02-08

8.0.5

3.0

Unsupported:

7.0

2007-06-22

7.0.4, ..., 7.11.2

2.1

N/A

N/A

N/A

Unsupported:

6.0

2004-01-06

6.0.1

1.5

1.3

Unsupported:

5.0

2002-11-13

5.0.2

1.4

Unsupported:

4.0

2001-10-22

4.0.4

1.3

Unsupported:

3.0

1998-09

3.1, 3.2.1, 3.4.2.1

1.2

Unsupported:

2.0

1996-10

2.6

1.1

Unsupported:

1.0

1995-02

1.2.8

1.0

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

#### Vulkan

The Khronos Group officially announced Vulkan API in March 2015, and officially released Vulkan 1.0 on 16 February 2016. Vulkan breaks compatibility with OpenGL and completely abandons its monolithic state machine concept. The developers of Gallium3D called Vulkan to be something along the lines of Gallium3D 2.0 – Gallium3D separates the code that implements the OpenGL state machine from the code that is specific to the hardware.

Version 1.3 is immediately available with Mesa 22.0. Hardware with support of OpenGL ES 3.1 should run at Vulkan Level 1.3 and before.

As Gallium3D ingests TGSI, Vulkan ingests SPIR-V (Standard Portable Intermediate Representation version "V" as in "Vulkan").

Intel released their implementation of a Vulkan driver for their hardware the day the specification was officially released, but it was only mainlined in April and so became part of Mesa 12.0, released in July 2016. While already the i965 driver wasn't written according to the Gallium3D specifications, for the Vulkan driver it makes even less sense to flange it on top of Gallium3D. Similarly there is no technical reason to flange it with NIR, but yet Intel's employees implemented their Vulkan driver that way.

It is to be expected that AMD's own proprietary Vulkan driver, which was released in March, and was announced to be released as free and open-source software in the future and be mainlined into Mesa, also abandons Gallium3D.

RADV is a free project for AMD and is available since version 13. Conformance with Khronos-Test came in version 17.3. Actual is Full support of Vulkan 1.0 and 1.1 since Mesa 18.1.

Nvidia released their proprietary GeForce driver with Vulkan support at launch day and Imagination Technologies (PowerVR), Qualcomm (Adreno) and ARM (Mali) have done the same or at least announced proprietary Vulkan drivers for Android and other operating systems. But when and whether additional free and open-source Vulkan implementations for these GPUs will show up, remains to be seen.

Mesa Software Driver VIRGL starts Vulkan Development in 2018 with GSOC projects for support of Virtual machines.

Lavapipe is a CPU-based Software Vulkan driver and the brother of LLVMpipe. Mesa Version 21.1 supports Vulkan 1.1+.

Google introduces Venus Vulkan Driver for virtual machines in Mesa 21.1 with full support for Vulkan 1.2+.

Qualcomm Turnip and Broadcom v3dv are new drivers for Qualcomm Adreno and Broadcom Raspberry 4 Hardware. Turnip is the Vulkan brother of freedreno for OpenGL. V3dv supports Vulkan 1.0+ since Mesa 20.3. In Version 21.1 Turnip supports Vulkan 1.1+.

Panfrost PanVK for ARM Mali is at way to Vulkan 1.1, but only 1.0 is stable available with Mesa 22.0.

Project Dozen is connecting direct 3D 12 (d3d12) with Vulkan for Linux Emulation WSL2 in Windows 10 and 11. In Mesa 23.2 Vulkan 1.0 is full conformant supported and 80% of 1.1 and 1.2 (mesamatrix).

#### Explicit fencing

A kind of memory barrier that separates one buffer from the rest of the memory is called a fence. Fences are there to ensure that a buffer is not being overwritten before rendering and display operations have completed on it. Implicit fencing is used for synchronization between graphics drivers and the GPU hardware. The fence signals when a buffer is no longer being used by one component so it can be operated on or reused by another. In the past the Linux kernel had an implicit fencing mechanism, where a fence is directly attached to a buffer (cf. GEM handles and FDs), but userspace is unaware of this. Explicit fencing exposes fences to userspace, where userspace gets fences from both the Direct Rendering Manager (DRM) subsystem and from the GPU. Explicit fencing is required by Vulkan and offers advantages for tracing and debugging.

Linux kernel 4.9 added Android's synchronization framework to mainline.

#### Generic Buffer Management

Generic Buffer Management (GBM) is an API that provides a mechanism for allocating buffers for graphics rendering tied to Mesa. GBM is intended to be used as a native platform for EGL on DRM or openwfd. The handle it creates can be used to initialize EGL and to create render target buffers.

Mesa GBM is an abstraction of the graphics driver specific buffer management APIs (for instance the various libdrm_* libraries), implemented internally by calling into the Mesa GPU drivers.

For example, the Wayland compositor Weston does its rendering using OpenGL ES 2, which it initializes by calling EGL. Since the server runs on the "bare KMS driver", it uses the EGL DRM platform, which could really be called the GBM platform, since it relies on the Mesa GBM interface.

At XDC2014, Nvidia employee Andy Ritger proposed to enhance EGL in order to replace GBM. This was not taken positively by the community, and Nvidia eventually changed their mind, and took another approach.

### Implementations of video acceleration APIs

There are three possible ways to do the calculations necessary for the encoding and decoding of video streams:

1. use a software implementation of a video compression or decompression algorithm (commonly called a CODEC) and execute this software on the *C*PU
2. use a software implementation of a video compression or decompression algorithm (commonly called a CODEC) and execute this software on the *G*PU (the 3D rendering engine)
3. use a complete (or partial) hardware implementation of a video compression or decompression algorithm; it has become very common to integrate such ASICs into the chip of the GPU/CPU/SoC and therefore abundantly available; for marketing reasons companies have established brands for their ASICs, such as PureVideo (Nvidia), Unified Video Decoder (AMD), Video Coding Engine (AMD), Quick Sync Video (Intel), DaVinci (Texas Instruments), CedarX (Allwinner), Crystal HD (Broadcom); some ASICs are available for licensing as semiconductor intellectual property core; usually different versions implement different video compression and/or video decompression algorithms; support for such ASICs usually belong into the kernel driver, to initialize the hardware and do low-level stuff. Mesa, which runs in user-space, houses the implementations of several APIs for software, e.g. VLC media player, GStreamer, HandBrake, etc., to conveniently access such ASICs:

- Video Acceleration API (VAAPI) – the most common API for Linux, used by AMD and Intel
- Video Decode and Presentation API for Unix (VDPAU) – used by Nvidia
- DirectX Video Acceleration (DXVA) – Microsoft Windows-only
- OpenMAX IL – designed by Khronos Group for video compression
- Distributed Codec Engine (DCE) – designed by Texas Instruments
- X-Video Bitstream Acceleration (XvBA) – extension to Xv - succeeded by VAAPI
- X-Video Motion Compensation (XvMC) – extension to Xv - succeeded by VAAPI

For example, Nouveau, which has been developed as part of Mesa, but also includes a Linux kernel component, which is being developed as part of the Linux kernel, supports the PureVideo-branded ASICs and provides access to them through VDPAU and partly through XvMC.

The free radeon driver supports Unified Video Decoder and Video Coding Engine through VDPAU and OpenMAX.

V4L2 is a kernel-to-user-space interface for video bit streams delivered by webcams or TV tuners.

Due to patent concerns regarding the H.264, H.265 and VC-1 video codecs, Fedora Linux disabled support for VAAPI acceleration for those in its build of Mesa in September 2022.

### Device drivers

The available free and open-source device drivers for graphic chipsets are "stewarded" by Mesa (because the existing free and open-source implementation of APIs are developed inside of Mesa). Currently there are two frameworks to write graphics drivers: "classic" and Gallium3D. An overview over some (but not all) of the drivers available in Mesa is given at mesamatrix.net.

There are device drivers for AMD/ATI R100 to R800, Intel, and Nvidia cards with 3D acceleration. Previously drivers existed for the IBM/Toshiba/Sony Cell processor of the PlayStation 3, S3 Virge & Savage chipsets, VIA chipsets, Matrox G200 & G400, and more.

The free and open-source drivers compete with proprietary closed-source drivers. Depending on the availability of hardware documentation and man-power, the free and open-source driver lag behind more or less in supporting 3D acceleration of new hardware. Also, 3D rendering performance was usually significantly slower with some notable exceptions. Today this is still true for Nouveau for most NVIDIA GPUs while on AMDs Radeon GPUs the open driver now mostly matches or exceeds the proprietary driver's performance.

### Direct Rendering Infrastructure (DRI)

At the time 3D graphics cards became more mainstream for PCs, individuals partly supported by some companies began working on adding more support for hardware-accelerated 3D rendering to Mesa. The Direct Rendering Infrastructure (DRI) was one of these approaches to interface Mesa, OpenGL and other 3D rendering API libraries with the device drivers and hardware. After reaching a basic level of usability, DRI support was officially added to Mesa. This significantly broadened the available range of hardware support achievable when using the Mesa library.

With adapting to DRI, the Mesa library finally took over the role of the front end component of a full scale OpenGL framework with varying backend components that could offer different degrees of 3D hardware support while not dropping the full software rendering capability. The total system used many different software components.

While the design requires all these components to interact carefully, the interfaces between them are relatively fixed. Nonetheless, as most components interacting with the Mesa stack are open source, experimental work is often done through altering several components at once as well as the interfaces between them. If such experiments prove successful, they can be incorporated into the next major or minor release. That applies e.g. to the update of the DRI specification developed in the 2007-2008 timeframe. The result of this experimentation, DRI2, operates without locks and with improved back buffer support. For this, a special git branch of Mesa was created.

DRI3 is supported by the Intel driver since 2013 and is default in some Linux distributions since 2016 to enable Vulkan support and more. It is also default on AMD hardware since late 2016 (X.Org Server 1.18.3 and newer).

### Software renderers

Mesa also contains multiple implementations of software rendering, *softpipe*, *llvmpipe*, and *lavapipe*, that allow OpenGL, Vulkan, and more to run on the CPU as a fallback when no graphics hardware accelerators are present.

VirGL is a Rasterizer for Virtual machines implemented in Mesa 11.1 since 2015 with OpenGL 3.3 support and showed in Mesamatrix since Mesa 18. In actual new Mesa 18.2 it supports more than the others with OpenGL 4.3 and OpenGL ES 3.2. About 80% of OpenGL 4.4 and 4.5 features are also now ready. Vulkan Development starts with GSOC 2018 projects.

Actual virGL state in Mesamatrix is full support of OpenGL 4.6+ and OpenGL ES 3.2+ with some necessary Linux software.

D3d12 is a project of Microsoft for WSL2 emulation of OpenGL 3.3+ and OpenCL 1.2+ with Direct3D 12. D3D12 is merged in 21.0. Actual state in Mesa 23.1 is OpenGL 4.2+ with nearly 4.4+ and OpenGL ES 3.1+.

Venus is a new Vulkan VirtIO GPU Driver for GPU in virtual machines by Google. Venus is merged in 21.1 and for public in 21.2 introduced. Venus supports Vulkan 1.3+ in Mesa 23.1. Hardware minimum is Vulkan 1.1 with some extensions.

### Mega drivers

The idea of bundling multiple drivers into a single "mega" driver was proposed by Emma Anholt. It allows for a single copy of the shared Mesa code to be used among multiple drivers (instead of it existing in each driver separately) and offering better performance than a separate shared library due to the removal of the internal library interface. The state trackers for VDPAU and XvMC have become separate libraries.

### shader-db

shader-db is a collection of about 20,000 shaders gathered from various computer games and benchmarks as well as some scripts to compile these and collect some statistics. Shader-db is intended to help validate an optimization.

It was noticed that an unexpected number of shaders are not hand-written but generated. This means these shaders were originally written in HLSL and then translated into GLSL by some translator program, such as e.g. HLSL2GLSL. The problem is, that the generated code is often far from being optimal. Matt Turner said it was much easier to fix this in the translator program than having to make Mesa's compiler carry the burden of dealing with such bloated shaders.

shader-db cannot be considered free and open-source software. To use it legally, one must have a license for all the computer games that the shaders are part of.

## Software architecture

The so-called "user-mode graphics device drivers" (UMD) in Mesa have very few commonalities with what is generally called a device driver. There are a couple of differences:

- they are meant to work on top of additionally existent kernel mode graphics device drivers, that are e.g. available as part of the Linux kernel found in the source code under `/drivers/gpu/drm/` Each UMD communicates with its kernel mode counterpart with the help of a specific library, name *libdrm_specific* and a generic one, named *libdrm*. This section shall look solely on the user-mode part above libdrm
- there is some implementation of the finite-state machine as specified by e.g. OpenGL; this implementation of the OpenGL state machine may be shared among multiple UMDs or not
- they consist to a great part of some sort of compiler, that ingests e.g. GLSL and eventually outputs machine code. Parsers may be shared among multiple UMD or be specific

### Mesa's Intermediate Representations

One goal of Mesa is the optimization of code that is to be executed by the respective GPU. Another is the sharing of code. Instead of documenting the pieces of software, this article shall instead look at the Intermediate Representations used in the process of compiling and optimizing. See Abstract syntax tree (AST) and Static single assignment form (SSA form).

#### SPIR-V

SPIR-V is a certain version of the Standard Portable Intermediate Representation. The idea is, that graphics applications output SPIR-V instead of GLSL. In contrast to the latter, SPIR-V is binary to avoid implementation differences between GLSL compiler frontends of different driver implementations, as this has been a major source of application incompatibilities and bugs. Also SPIR-V binary usually also passed through some general optimizations. SPIR-V's binary representation also offers some degree of obfuscation, which might appeal to some software vendors as a form of intellectual property protection; however, SPIR-V contains ample information for reflection and tools exist that translate SPIR-V back into high quality, human readable high level code. A UMD needs only apply optimizations, that are specific to the supported hardware.

#### GLSL IR

#### Mesa IR

#### NIR

NIR (New Internal Representation) was introduced to overcome TGSI limitations. NIR was extended in last and actual releases as base of Spir-V support and is since 2016 main development area. LLVMpipe, i965, RadeonSI, Nouveau, freedreno, vc4 are changed to NIR from TGSI. RADV, Zink and other new drivers starts with NIR. All drivers with full OpenGL 4.6 support are related to NIR by SPIR-V support. Also AMD r600 has a fork with NIR for better support of HD5000 and HD6000 series. This option for r600 is default since Mesa 21.0.

#### TGSI

The Tungsten Graphics Shader Infrastructure (TGSI) was introduced in 2008 by Tungsten Graphics. All Gallium3D-style UMDs ingest TGSI. NIR is now Main development area, so TGSI is only for older driver like r300g default infrastructure and will be deprecated in some years.

GLSL-To-TGSI code will be deleted in Mesa 22.2. Default is newer NIR-to-TGSI with GLSL-to-NIR for all native NIR drivers. Some older TGSI drivers are supported with this NIR Code path. Later NIR-To-TGSI will be deprecated for native NIR drivers only.

#### LLVM IR

`llvmpipe` does not output machine code, but instead LLVM IR. From here on, LLVM does optimizations and the compilation to machine code. This does mean, that a certain minimum version of LLVM has to be installed as well.

### Mesa's GLSL compiler

Mesa's GLSL compiler generates its own IR. Because each driver has very different requirements from a LIR, it differentiates between HIR (high-level IR) and LIR (low-level IR).

## Gallium3D

**Gallium3D** is a set of interfaces and a collection of supporting libraries intended to ease the programming of device drivers for 3D graphics chipsets for multiple operating systems, rendering or video acceleration APIs. It is free and open-source graphics device driver software.

A feature matrix is being provided at mesamatrix.net.

The development of Gallium3D started in 2008 at Tungsten Graphics, and the implementation is available as free and open-source software as part of Mesa 3D hosted by freedesktop.org. The primary goal of making driver development easier, bundling otherwise duplicated code of several different drivers at a single point, and to support modern hardware architectures. This is done by providing a better division of labor, for example, leaving memory management to the kernel DRI driver.

Gallium3D has been a part of Mesa since 2009 and is used by all non-Vulkan drivers as of version 22.0. As of 2026, there are at least 20 Gallium3D drivers, including hardware drivers, software implementations, virtualization passthrough, and translation layers implementing Gallium3D on top of APIs such as Vulkan, Apple's Metal API, and Microsoft's Direct3D 12.

### Software architecture

Gallium3D eases programming of device drivers by splitting the graphics device driver into three parts. This is accomplished by the introduction of two interfaces: *Gallium3D State Tracker Interface* and the *Gallium3D WinSys Interface*. The three components are called:

**Gallium3D State Tracker**

Each graphical

API

by which a device driver is being addressed has its own State Tracker, e.g. there is a Gallium3D State Tracker for

OpenGL

, and a different one (Rusticl) for

OpenCL

. Each State Tracker contains an implementation of the Gallium3D State Tracker Interface, and is used by all existent Gallium3D hardware device drivers.

**Gallium3D hardware device driver**

This is the actual code that is specific to the underlying 3D graphic accelerator, but only as far as the Gallium3D WinSys Interface allows. There is a unique Gallium3D hardware device driver for each available graphics chip and each implements the Gallium3D State Tracker Interface as well as the Gallium3D WinSys Interface. The Gallium3D hardware device driver understands NIR (NIR Intermediate Representation, a recursive acronym), an intermediate language for describing shaders. This code translated NIR shaders from the state tracker into the

instruction set

implemented by the GPU.

**Gallium3D WinSys**

This is specific to the underlying

kernel

of the

operating system

and each one implements the Gallium3D WinSys Interface to interface with all available Gallium3D hardware device drivers.

#### Differences from classic graphics drivers

Gallium3D provides a unified API exposing standard hardware functions, such as shader units found on modern hardware. Thus, 3D APIs such as OpenGL 1.x/2.x, OpenGL 3.x, OpenVG, GPGPU infrastructure or even Direct3D (as found in the Wine compatibility layer) will need only a single back-end, called a state tracker, targeting the Gallium3D API. By contrast, legacy DRI device drivers required a different back-end for each hardware platform, and several other APIs needed translation to OpenGL, at the expense of code duplication. All vendor device drivers, due to their proprietary and closed-source nature, are written that way meaning that, e.g. the AMD Catalyst implements both OpenGL and Direct3D, and the vendor drivers for the GeForce have their implementations.

Under Gallium3D, Direct Rendering Manager (DRM) kernel drivers will manage the memory and Direct Rendering Interface (DRI2) drivers will be more GPU processing oriented.

#### Tungsten Graphics Shader Infrastructure

Tungsten Graphics Shader Infrastructure (TGSI) is an Intermediate representation used within some parts of Mesa. Shaders written in OpenGL Shading Language are to be translated/compiled into TGSI, then optimizations are made, and then the TGSI shaders are being compiled into shaders for the instruction set of the used GPU.

As of 2026, most drivers have moved away from TGSI, in favor of NIR.

#### NIR Intermediate Representation

NIR is the primary Intermediate Representation in Mesa. Development of NIR started in 2014 inside Intel, and over time NIR has replaced TGSI in most parts of Mesa.

### History

Original authors of Gallium3D were Keith Whitwell and Brian Paul at Tungsten Graphics (acquired by VMware in 2008).

#### Milestones

**2008-07-13 (2008-07-13)**

Nouveau development is done exclusively for the Gallium framework. The old DRI driver was removed from the master branch of the Mesa repository on Freedesktop.org.

**2009-02-11 (2009-02-11)**

The gallium-0.2 branch was merged into mainline Master branch of Mesa.

Development is done in Mesa mainline.

**2009-02-25 (2009-02-25)**

Gallium3D can run on Linux as well as FreeBSD kernels.

**2009-05-01 (2009-05-01)**

Zack Rusin from Tungsten Graphics added the

OpenVG

state tracker to Mesa 3D,

which enables

Scalable Vector Graphics

to be hardware-accelerated by any Gallium3D-based driver.

**2009-07-17 (2009-07-17)**

Mesa3D 7.5 is released, the first version to include Gallium3D.

**2010-09-10 (2010-09-10)**

Initial support for the Evergreen GPUs was added to the r600g driver.

**2010-09-21 (2010-09-21)**

There are two Gallium3D drivers for ATI hardware known as r300g and r600g for R300-R500 and R600-Evergreen GPUs respectively.

**2010-09-21 (2010-09-21)**

Major commits were made to the code to support Direct3D 10 and 11.

In time, this might offer the ability to use recent Direct3D implementations on Linux systems.

**2011-11-30 (2011-11-30)**

Intel 965g and Cell Gallium drivers were removed from the master branch of Mesa as unmaintained and broken.

**2013-11-30 (2013-11-30)**

Mesa 10 with OpenGL 3.2, 3.3 and OpenCL 1.0+

**2014-11-18 (2014-11-18)**

Major commits were made to the code to support Direct3D 9.

**2015-09-15 (2015-09-15)**

Mesa 11 with OpenGL 4.0, 4.1 and OpenCL 1.2 (incomplete)

**2015-12-15 (2015-12-15)**

Mesa 11.1 Driver VIRGL for virtual machines with OpenGL 3.3

**2016-07-08 (2016-07-08)**

Mesa 12 with OpenGL 4.2, 4.3 and Vulkan 1.0 (Intel ANV and AMD RADV)

**2016-11-01 (2016-11-01)**

Mesa 13 with OpenGL 4.4 and OpenGL ES 3.2

**2017-02-13 (2017-02-13)**

Mesa 17.0 with OpenGL 4.5 and freedreno driver with OpenGL 3.0 and 3.1

**2017-05-10 (2017-05-10)**

Mesa 17.1 OpenGL 4.2+ for Intel Ivy Bridge (more than Intel driver for Windows, OpenGL 3.3+ for Intel Open SWR Rasterizer (important for cluster Computer for huge simulations)

**2017-12-08 (2017-12-08)**

Mesa 17.3 AMD Vulkan Driver RADV full compliant in Khronos Test of Vulkan 1.0

**2018-05-18 (2018-05-18)**

Mesa 18.1 with Vulkan 1.1 (Intel ANV and AMD RADV)

**2018-09-07 (2018-09-07)**

Mesa 18.2 with OpenGL 4.3 for Soft Driver VIRGL (important for virtual machines in cloud Cluster Computer), OpenGL ES 3.1 for Freedreno with Adreno A5xx

**2019-06-11 (2019-06-11)**

Mesa 19.1 released with Intel's next generation 'iris' graphics driver for generation 8+ iGPUs, built using Gallium3D

**2019-12-11 (2019-12-11)**

Mesa 19.3 released OpenGL 4.6 with Intel i965 with gen 7+ and optional Iris Gen 8+

**2020-03-18 (2020-03-18)**

Mesa 20.0 released OpenGL 4.6 with AMD GCN and Vulkan 1.2 for Intel

**2020-05-27 (2020-05-27)**

Mesa 20.1 released NIR vectorisation support and shared virtual memory support for OpenCL in Clover

**2020-11-30 (2020-11-30)**

Mesa 20.3 full support of OpenCL 1.2 in Clover

**2021-03-11 (2021-03-11)**

Mesa 21.0 initial support of "D3D12“: Direct 3D 12 for WSL2 in Windows 10 with OpenGL 3.3+, ARM Freedreno: OpenGL 3.3+

**2021-05-05 (2021-05-05)**

Mesa 21.1 initial support of Google VirtIO GPU Driver "Venus“ with Vulkan 1.2+; Zink: OpenGL 4.6+, OpenGL ES 3.1+; Qualcomm Turnip, Lavapipe: Vulkan 1.1+

**2021-08-04 (2021-08-04)**

Mesa 21.2 released with new Intel Crocus driver, based on Gallium3D, supporting Intel Sandy Bridge through Haswell iGPUs, replacing the need for the old non-Gallium3D i965 driver. Also added was the PanVK Vulkan Driver for ARM Mali GPUs.

**2022-03-09 (2022-03-09)**

Mesa 22.0 removed all legacy non-Gallium3D drivers

. It also has full support of Vulkan 1.3 by Intel Anvil and AMD RADV

**2023-05-10 (2023-05-10)**

Mesa 23.1 OpenCL with Rust: RustiCL for AMD GCN Hardware available (more hardware wip)

**2023-09-30 (2023-09-30)**

Mesa 23.2 with Apple Asahi OpenGL 3.1 and OpenGL ES 3.0, RADV supports Ray Tracing in AMD RDNA 2 and 3, Intel Anvil Vulkan H.265 decoding support

## Performance

Mature drivers in Mesa can often out-perform the proprietary drivers for that same hardware. Particularly on handheld gaming devices that are significantly constrained in both power and thermals, running Linux with Mesa drivers has been shown to consistently and significantly out-perform Windows with the manufacturer's proprietary drivers on the same hardware, sometimes by as much as 75%. Microsoft allegedly set an internal goal of being able to match the performance of SteamOS on handheld gaming devices.

## History

Project initiator Brian Paul was a graphics hobbyist. He thought it would be fun to implement a simple 3D graphics library using the OpenGL API, which he might then use instead of VOGL (very ordinary GL Like Library). Beginning in 1993, he spent eighteen months of part-time development before he released the software on the Internet in February 1995. The software was well received, and people began contributing to its development. Mesa started off by rendering all 3D computer graphics on the CPU. Despite this, the internal architecture of Mesa was designed to be open for attaching to graphics processor-accelerated 3D rendering. In this first phase, rendering was done indirectly in the display server, leaving some overhead and noticeable speed lagging behind the theoretical maximum. The Diamond Monster 3D, using the Voodoo Graphics chipset, was one of the first 3D hardware devices supported by Mesa.

The first true graphics hardware support was added to Mesa in 1997, based upon the Glide API for the then new 3dfx Voodoo I/II graphics cards and their successors. A major problem of using Glide as the acceleration layer was the habit of Glide to run full screen, which was only suitable for computer games. Further, Glide took the lock of the screen memory, and thus the display server was blocked from doing any other GUI tasks.

Mesa 10 complies with OpenGL 3.3 for Intel, AMD/ATI, and Nvidia GPU hardware. Mesa 11 was announced with some drivers being OpenGL 4.1 compliant.

Mesa 12 contains OpenGL 4.2 and 4.3 and Intel Vulkan 1.0 support.

Mesa 13 brought Intel support for OpenGL 4.4 and 4.5 (all Features supported for Intel Gen 8+, Radeon GCN, Nvidia (Fermi, Kepler), but no Khronos-Test for 4.5-Label) and experimental AMD Vulkan 1.0 support through the community driver RADV. OpenGL ES 3.2 is possible with Intel Skylake (Gen9).

1st stable version of 2017 is 17.0 (new year Counting). Ready features are certified OpenGL 4.5, OpenGL 4.5 for Intel Haswell, OpenGL 4.3 for Nvidia Maxwell and Pascal (GM107+). Huge performance gain was measured with Maxwell 1 (GeForce GTX 750 Ti and more with GM1xx). Maxwell-2-Cards (GeForce GTX 980 and more with GM2xx) are underclocked without Nvidia information.

The Khronos CTS test suite for OpenGL 4.4, 4.5 and OpenGL ES 3.0+ is in now (2017-01-24) Open Source and all tests for Mesa 13 and 17 are now possible without costs.

2nd stable version of 2017, 17.1.0, came out on 10 May 2017 with some interesting improvements. OpenGL 4.2+ for Intel Ivy Bridge and OpenGL 3.3+ for Intel Open SWR Rasterizer are 2 of the highlights.

Due to the modularized nature of OpenGL, Mesa can support extensions from newer versions of OpenGL without claiming full support for such versions. For example, in July 2016, Mesa supported OpenGL ES 3.1 but also all OpenGL ES 3.2 extensions except for five, as well as a number of extensions not part of any OpenGL or OpenGL ES version.

3rd Version 17.2 is available since September 2017 with some new OpenGL 4.6 features and velocity improvements in 3D for Intel and AMD. Only 1.4% of Tests fail for OpenGL 4.5 in Nouveau for Kepler.

4th Version 17.3 is ready since December 2017. Many improvements in many drivers are available. OpenGL 4.6 is nearly fully available (Spir-V is not ready). AMD Vulkan Driver RADV is now fully conformant in Khronos-Test.

1st version of 2018 is 18.0 and available since March 2018 by same scheme in 2017. Full OpenGL 4.6 support is not ready, but many features and improvements were successfully tested in RC3. 10-bit support for Intel i965 in Colors is also a Highlight. New is support for Intel Cannon Lake and AMD Vega with actual Linux Version. AMD Evergreen Chips (RV800 or R900) are near OpenGL 4.5 support. Old AMD R600 or RV700 Chips can only support OpenGL 3.3 with some features of OpenGL 4.x. Freedreno is the Driver for Adreno Hardware and near OpenGL 3.3 support.

2nd version of 2018 is 18.1 and available since May. Target is Vulkan 1.1.72 in Intel ANV and AMD RADV driver. OpenGL 4.6 with spir-V is also main target. Permanent work is possible completion of Features and Optimization of drivers for older hardware like AMD R600/Evergreen, Nvidia Tesla and before, Fermi, Kepler or Intel Sandybridge, Ivybridge, Haswell or Broadwell. ARM Architecture made also great improvements in Adreno 3xx/4xx/5xx and Broadwell VC4/VC5 for Raspi with main target OpenGL ES.

3rd version of 2018 is 18.2 and available in calendar stable in September. OpenGL 4.6 with spir-V and Vulkan 1.1.80 are in WIP. The soft Driver for virtual machines VIRGL is ready for OpenGL 4.3 and OpenGL ES 3.2. RadeonSI is also ready for OpenGL ES 3.2. ASTC Texture Compression Support and Compatibility Modus Support for OpenGL 4.4 (3.1 in 18.1) are other highlights in RadeonSI for AMD GCN Cards. New Vulkan 1.1 and more features for Intel and AMD are available. See more Details for Vulkan in Mesamatrix.

4th version of 2018 is 18.3 and released as stable Version 18.3.1 in December 2018. Many features in Detail and support of newer hardware are main parts. Full support of OpenGL 4.6 is not ready.

1st Version of 2019 is 19.0 and was now released at March. Full support of OpenGL 4.6 is not ready, but many improvements on this way are in all drivers.

The second 2019 version is 19.1. A key feature is the transition of TGSI to NIR, marking a step toward OpenGL 4.6 with SPIR-V support and broader OpenCL compatibility. RadeonSI performs well with NIR in the development version.

3rd Version of 2019 is 19.2. OpenGL 4.6 is Beta ready for new Intel Iris Driver.

4th Version of 2019 is 19.3. OpenGL 4.6 is ready for Intel i965 and optional for new Iris Driver.

First Version of 2020 is 20.0. Vulkan 1.2 is ready for AMD RADV and Intel ANV. Intel Iris is default for Intel Broadwell Gen 8+. RadeonSI driver switched to using NIR by default, instead of TGSI.

2nd Version of 2020 is 20.1. Many improvements are ready in many drivers. Zink is a new virtual driver for OpenGL over Vulkan.

3rd Version of 2020 is 20.2. OpenGL 3.0 for Zink is one new feature. LLVMpipe will support OpenGL 4.3+ (4.5+ in 20.3). ARM Panfrost is mostly improved with many modules. Shared virtual memory is possible for OpenCL in Nouveau with Pascal and higher.

4th Version of 2020 is 20.3. v3d and v3dv are new drivers for OpenGL and Vulkan 1.0 with Broadcom hardware like Raspberry Pi 4. OpenCL 1.2 is full supported in clover module. Zink support OpenGL 3.3+. LLVMpipe virtual driver support now OpenGL 4.5+ with 4.6 in view. Lavapipe (originally called Vallium) as Vulkan Tree of LLVMpipe is merged.

In Mesa 21.0 d3d12 will be merged with OpenGL 3.0 to 3.3. Microsoft and Collabora develops new emulation d3d12 in WSL2 to Windows 10 with Direct 3D 12. OpenCL 1.2 is also target in d3d12. An acceleration of factor 2 to 5 is done in Benchmark SPECviewperf with improved OpenGL Code. Many Mesa 21.0 features improves performance. New Release 21.0.0 is public since 11 March 2021.

Mesa 21.1 is second release of year 2021. OpenGL 4.6+ and OpenGL ES 3.1+ is available for Zink. AMD Driver 600g can change to NIR with more possibilities for old Radeon HD 5000 and 6000 cards. Qualcomm Turnip reaches Vulkan 1.1+ and software emulation Lavapipe Vulkan 1.1+. Google VirtIO GPU Driver Venus with Vulkan 1.2+ is merged in experimental state with low performance in mesa main tree.

Mesa 21.2 is third release of year 2021. Google Virtual Vulkan IO Driver Venus will be official introduced with full Vulkan 1.2+ support (more mesamatrix). ARM Panfrost: OpenGL ES 3.1+ Support is available and panVK is the new Vulkan Driver. Initial support started for ARM Apple M1 with new driver Asahi. 21.2 is available since 4 August 2021.

Proposed architectural changes involve migrating legacy drivers to a standalone "classic" tree to streamline maintenance and bug fixing for the modern **Gallium3D** framework. A significant complication remains the **Intel i965** driver, which provides critical support for popular legacy hardware—including the **Intel Haswell** microarchitecture—and maintains compatibility with **Windows 10**. A new Gallium3D driver Crocus for Intel Gen 4 Graphics to Haswell is here in development to complete here the gallium3D area with possible split in the next time of year 2021. Crocus is optional available in 21.2. Amber branch is for old drivers without Gallium 3D Functions like Radeon R200, intel i915 and 965 with actual version 21.3.9.

In Version 22.0 Classic drivers are retired. Vulkan 1.3 is available for Intel Anvil and AMD RADV.

Microsoft introduces new driver „Dozen“ for WSL 2 in early development stage as Vulkan over d3d12 in Mesa 22.1.

RustiCL is available at 22.3 with official OpenCL 3.0 Conformance for Intel XE Graphics. Performance is equal and better to AMD ROCm with AMD 6700 XT Card.

A main development target of Mesa 23.0 was ray tracing for Vulkan.

Microsoft develops the Dozen driver for Vulkan in WSL. Vulkan 1.0+ with 80% 1.1 and 1.2 will be available in Mesa 23.2 after delay to 23.1 (See mesamatrix). RustiCL for AMD hardware is available in 23.1.

VirGL for virtual machines jumps in Mesa 23.2 to OpenGL 4.6. Apple Asahi for Apple Arm Machines jumps from OpenGL 2.1 to 3.1 with 90% features of OpenGL 3.2 and 3.3 and OpenGL ES 2.0 to 3.0.

Microsoft Supports in WSL OpenGL 4.6+ in Mesa 24.0 (in Mesa 23.3: 4.3+) with DirectX 12 translation driver dozen.

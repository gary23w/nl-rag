---
title: "High-Level Shader Language"
source: https://en.wikipedia.org/wiki/High-Level_Shader_Language
domain: directx-graphics
license: CC-BY-SA-4.0
tags: directx api, direct3d, hlsl shader, directx raytracing
fetched: 2026-07-02
---

# High-Level Shader Language

The **High-Level Shader Language** or **High-Level Shading Language** (**HLSL**) is a proprietary shading language developed by Microsoft for the Direct3D 9 API to augment the shader assembly language, and went on to become the required shading language for the unified shader model of Direct3D 10 and higher. It was developed alongside the **Cg** (short for *C for Graphics*) shading language from Nvidia. Early versions of the two languages were considered identical, only marketed differently.

Although Cg and HLSL share the same core syntax, some features of C were modified and new data types were added to make Cg/HLSL more suitable for programming graphics processing units.

Two main branches of the Cg/HLSL language exist: the Nvidia Cg compiler (cgc) which outputs DirectX or OpenGL and the Microsoft HLSL which outputs DirectX shaders in bytecode format. Nvidia's cgc was deprecated in 2012, with no additional development or support available.

HLSL shaders can enable many special effects in both 2D and 3D computer graphics.

- The Cg/HLSL language originally only included support for vertex shaders and pixel shaders ("fragment" in GLSL). A vertex shader is executed for each vertex that is submitted by the application, and is primarily responsible for transforming the vertex from object space to view space, generating texture coordinates, and calculating lighting coefficients such as the vertex's normal, tangent, and bitangent vectors. When a group of vertices (normally 3, to form a triangle) come through the vertex shader, their output position is interpolated to form pixels within its area; this process is known as rasterization.
- DirectX 10 (Shader Model 4) and Cg 2.0 introduced geometry shaders. This shader takes as its input some vertices of a primitive (triangle/line/point) and uses this data to generate/degenerate (or tessellate) additional primitives or to change the type of primitives, which are each then sent to the rasterizer.
- DirectX 11 (Shader Model 5) introduced compute shaders (GPGPU) and tessellation shaders (hull and domain). The latter is present in Cg 3.1.
- DirectX 12 (Shader Model 6.3) introduced ray tracing shaders (ray generation, intersection, any hit / closest hit / miss).

D3D11.3 and D3D12 introduced Shader Model 5.1 and later 6.0.

## Background

Due to technical advances in graphics hardware, some areas of 3D graphics programming have become quite complex. To simplify the process, new features were added to graphics cards, including the ability to modify their rendering pipelines using vertex and pixel shaders.

In the beginning, vertex and pixel shaders were programmed at a very low level with only the assembly language of the graphics processing unit. Although using the assembly language gave the programmer complete control over code and flexibility, it was fairly hard to use. A portable, higher level language for programming the GPU was needed, so Cg was created to overcome these problems and make shader development easier.

Some of the benefits of using Cg/HLSL over assembly are:

- High level code is easier to learn, program, read, and maintain than assembly code.
- Cg/HLSL code is portable to a wide range of hardware and platforms, unlike assembly code, which usually depends on hardware and the platforms it's written for.
- The Cg/HLSL compiler can optimize code and do lower level tasks automatically, which are hard to do and error-prone in assembly.

## Language

### Data types

Cg/HLSL has six basic data types. Some of them are the same as in C, while others are especially added for GPU programming. These types are:

- float - a 32bit floating point number
- half - a 16bit floating point number
- int - a 32bit integer
- fixed - a 12bit fixed point number
- bool - a Boolean variable
- sampler* - represents a texture object

Cg also features vector and matrix data types that are based on the basic data types, such as float3 and float4x4. Such data types are quite common when dealing with 3D graphics programming. Cg also has struct and array data types, which work in a similar way to their C equivalents.

### Operators

Cg supports a wide range of operators, including the common arithmetic operators from C, the equivalent arithmetic operators for vector and matrix data types, and the common logical operators.

### Functions and control structures

Cg shares the basic control structures with C, like if/else, while, and for. It also has a similar way of defining functions.

### Semantics

### Preprocessor

Cg implements many C preprocessor directives and its macro expansion system. It implements `#include`.

### HLSL features

- Namespace
- Annotation

## Environment

Cg programs are built for different *shader profiles* that stand for GPUs with different capabilities. These profiles decide, among others, how many instructions can be in each shader, how many registers are available, and what kind of resources a shader can use. Even if a program is correct, it might be too complex to work on a profile.

As the number of profile and shader types cropped up, Microsoft has switched to use the term "Shader Model" to group a set of profiles found in a generation of GPUs. Cg supports some of the newer profiles up to Shader Model 5.0 as well as translation to glsl or hlsl.

GPUs listed are the hardware that first supported the given specifications. Manufacturers generally support all lower shader models through drivers. Note that games may claim to require a certain DirectX version, but don't necessarily require a GPU conforming to the full specification of that version, as developers can use a higher DirectX API version to target lower-Direct3D-spec hardware; for instance DirectX 9 exposes features of DirectX7-level hardware that DirectX7 did not, targeting their fixed-function T&L pipeline.

### Pixel shader comparison

Pixel shader version

1.0

1.1

1.2

1.3

1.4

2.0

2.0a

2.0b

3.0

4.0

4.1

5.0

Dependent texture limit

4

4

4

6

8

Unlimited

8

Unlimited

Unlimited

Texture instruction limit

4

4

4

6 * 2

32

Unlimited

Unlimited

Unlimited

Unlimited

Arithmetic instruction limit

8

8

8

8 * 2

64

Unlimited

Unlimited

Unlimited

Unlimited

Position register

No

No

No

No

No

No

No

Yes

Yes

Instruction slots

8

8 + 4

8 + 4

(8 + 6) * 2

64 + 32

512

512

≥ 512

≥ 65536

Executed instructions

8

8 + 4

8 + 4

(8 + 6) * 2

64 + 32

512

512

65536

Unlimited

Texture indirections

4

4

4

4

4

Unlimited

4

Unlimited

Unlimited

Interpolated registers

2 + 4

2 + 4

2 + 4

2 + 6

2 + 8

2 + 8

2 + 8

10

32

Instruction predication

No

No

No

No

No

Yes

No

Yes

No

Index input registers

No

No

No

No

No

No

No

Yes

Yes

Temp registers

2

2 + 4

3 + 4

6

12 to 32

22

32

32

4096

Constant registers

8

8

8

8

32

32

32

224

16×4096

Arbitrary

swizzling

No

No

No

No

No

Yes

No

Yes

Yes

Gradient instructions

No

No

No

No

No

Yes

No

Yes

Yes

Loop count register

No

No

No

No

No

No

No

Yes

Yes

Face register (2-sided lighting)

No

No

No

No

No

No

Yes

Yes

Yes

Dynamic flow control

No

No

No

No

No

No

No

Yes (24)

Yes (64)

Bitwise Operators

No

No

No

No

No

No

No

No

Yes

Native Integers

No

No

No

No

No

No

No

No

Yes

- **PS 1.0** — Unreleased 3dfx Rampage, DirectX 8
- **PS 1.1** — GeForce 3, DirectX 8
- **PS 1.2** — 3Dlabs Wildcat VP, DirectX 8.1
- **PS 1.3** — GeForce 4 Ti, DirectX 8.1
- **PS 1.4** — Radeon 8500–9250, Matrox Parhelia, DirectX 8.1
- **Shader Model 2.0** — Radeon 9500–9800/X300–X600, DirectX 9
- **Shader Model 2.0a** — GeForce FX/PCX-optimized model, DirectX 9.0a
- **Shader Model 2.0b** — Radeon X700–X850 shader model, DirectX 9.0b
- **Shader Model 3.0** — Radeon X1000 and GeForce 6, DirectX 9.0c
- **Shader Model 4.0** — Radeon HD 2000 and GeForce 8, DirectX 10
- **Shader Model 4.1** — Radeon HD 3000 and GeForce 200, DirectX 10.1
- **Shader Model 5.0** — Radeon HD 5000 and GeForce 400, DirectX 11
- **Shader Model 5.1** — GCN 1+, Fermi+, DirectX 12 (11_0+) with WDDM 2.0
- **Shader Model 6.0** — GCN 1+, Kepler+, DirectX 12 (11_0+) with WDDM 2.1
- **Shader Model 6.1** — GCN 1+, Kepler+, DirectX 12 (11_0+) with WDDM 2.3
- **Shader Model 6.2** — GCN 1+, Kepler+, DirectX 12 (11_0+) with WDDM 2.4
- **Shader Model 6.3** — GCN 1+, Kepler+, DirectX 12 (11_0+) with WDDM 2.5
- **Shader Model 6.4** — GCN 1+, Kepler+, Skylake+, DirectX 12 (11_0+) with WDDM 2.6
- **Shader Model 6.5** — GCN 1+, Kepler+, Skylake+, DirectX 12 (11_0+) with WDDM 2.7
- **Shader Model 6.6** — GCN 4+, Maxwell+, DirectX 12 (11_0+) with WDDM 3.0
- **Shader Model 6.7** — GCN 4+, Maxwell+, DirectX 12 (12_0+) with WDDM 3.1
- **Shader Model 6.8** — RDNA 1+, Maxwell 2+, DirectX 12 (12_0+) with WDDM 3.1 / 3.2 with Agility SDK

"32 + 64" for *Executed Instructions* means "32 texture instructions and 64 arithmetic instructions."

### Vertex shader comparison

| Vertex shader version | 1.0 | 1.1 | 2.0 | 2.0a | 3.0 | 4.0 4.1 5.0 |
|---|---|---|---|---|---|---|
| # of instruction slots | 128 | 128 | 256 | 256 | ≥ 512 | ≥ 65536 |
| Max # of instructions executed | 128 | 128 | 1024 | 65536 | 65536 | Unlimited |
| Instruction predication | No | No | No | Yes | Yes | Yes |
| Temp registers | 12 | 12 | 12 | 16 | 32 | 4096 |
| # constant registers | ≥ 96 | ≥ 96 | ≥ 256 | 256 | ≥ 256 | 16×4096 |
| Address register | No | Yes | Yes | Yes | Yes | Yes |
| Static flow control | No | No | Yes | Yes | Yes | Yes |
| Dynamic flow control | No | No | No | Yes | Yes | Yes |
| Dynamic flow control depth | —N/a | —N/a | —N/a | 24 | 24 | 64 |
| Vertex texture fetch | No | No | No | No | Yes | Yes |
| # of texture samplers | —N/a | —N/a | —N/a | —N/a | 4 | 128 |
| Geometry instancing support | No | No | No | No | Yes | Yes |
| Bitwise operators | No | No | No | No | No | Yes |
| Native integers | No | No | No | No | No | Yes |

### The standard library

As in C, Cg/HLSL features a set of functions for common tasks in GPU programming. Some of the functions have equivalents in C, like the mathematical functions abs and sin, while others are specialized in GPU programming tasks, like the texture mapping functions tex1D and tex2D.

### The Cg/HLSL runtime library

Cg/HLSL programs are merely vertex and pixel shaders, and they need supporting programs that handle the rest of the rendering process. Cg can be used with two graphics APIs: OpenGL or DirectX. Each has its own set of Cg functions to communicate with the Cg program, like setting the current Cg shader, passing parameters, and such tasks. (HLSL only targets DirectX.)

In addition to being able to compile Cg source to assembly code, the Cg runtime also has the ability to compile shaders during execution of the supporting program. This allows the runtime to compile the shader using the latest optimizations available for hardware that the program is currently executing on. However, this technique requires that the source code for the shader be available in plain text to the compiler, allowing the user of the program to access the source-code for the shader. Some developers view this as a major drawback of this technique.

To avoid exposing the source code of the shader, and still maintain some of the hardware specific optimizations, the concept of profiles was developed. Shaders can be compiled to suit different graphics hardware platforms (according to profiles). When executing the supporting program, the best/most optimized shader is loaded according to its profile. For instance there might be a profile for a graphics card that supports complex pixel shaders, and another profile for one that supports only minimal pixel shaders. By creating a pixel shader for each of these profiles a supporting program enlarges the number of supported hardware platforms without sacrificing picture quality on powerful systems.'

## Compilers and dialects

The Cg dialect has only ever had one compiler, in the form of Nvidia's Cg toolkit.

Microsoft has released two compilers for HLSL. The original compiler was the closed-source FXC (Effect Compiler), supported until 2015. It was deprecated in favor of the open-source LLVM-based DXC (DirectXShaderCompiler) with support for newer HLSL features. Both compilers generate bytecode: while the older FXC used DXBC, DXC now uses DXIL. DXC can also emit SPIR-V bytecode.

The Khronos Group has also written a LLVM-based HLSL compiler, in the form of a frontend for *glslang*, their GLSL-to-SPIR_V compiler. Support for SPIR-V means that the shaders can be cross-platform, no longer limiting them to a DirectX stack. This task was previously performed by source-level converters like HLSL2GLSL, but the resulting code is often bloated.

### Derived languages

The PlayStation Shader Language (PSSL) is based on Cg/HLSL.

The ReshadeFX shading language is also based on Cg/HLSL. Shaders written in ReshadeFX are compiled to OpenGL, DX, or Vulkan and injected into games to act as post-processing filters.

Khronos has since evolved *glslang* into *slang*, a shading language and compiler that is mostly source-code-compatible with HLSL. Slang can compile to textual shading languages (GLSL, MSL, CUDA, WGSL), bytecodes (D3D11, D3D12, Vulkan SPIR-V) as well as the CPU. It also has a GLSL-compatibility mode.

## Applications and games that use Cg or HLSL

- *3DVIA Virtools*
- Adobe Photoshop
- Maya
- *Battlefield 2*
- *Crystal Space*
- *Dolphinity Racer*
- *Earth's Special Forces* - A Half-Life Mod
- *Enemy Territory: Quake Wars*
- *Doom 3 BFG Edition*
- *EON Professional™/Ultra™* of EON Reality
- *eyeon Fusion*
- *Far Cry*
- *Garshasp: The Monster Slayer*
- *GLScene*
- *Gun Metal*
- *Hitman: Blood Money*
- *Irrlicht Engine*
- *League of Legends*
- *Lightfeather 3D Engine*
- LightWave 11.6
- *muvee Reveal*
- *OGRE*
- *OpenEmu*
- *Panda3D*
- PCSX2
- PlayStation 3
- *RetroArch*
- *R.U.S.E.*
- *Snes9x*
- *Unity game engine*
- *Unreal Engine*

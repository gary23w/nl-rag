---
title: "Shading language"
source: https://en.wikipedia.org/wiki/Shading_language
domain: hlsl-shading
license: CC-BY-SA-4.0
tags: hlsl shader, direct3d shader, hlsl compute, pixel shader hlsl
fetched: 2026-07-02
---

# Shading language

A **shading language** is a graphics programming language made for programming shader effects on the graphics processing unit (unlike other programming languages, which send instructions to the central processing unit instead). Because of this, shading languages are usually more 'low level' languages and usually consist of special data types like "vector", "matrix", "color" and "normal".

## Offline rendering

Shading languages used in offline rendering tend to be close to natural language, so that no special knowledge of programming is required. Offline rendering aims to produce maximum-quality images, at the cost of greater time and compute than real-time rendering.

### RenderMan Shading Language

The RenderMan Shading Language (RSL or SL, for short), defined in the *RenderMan Interface Specification*, is a common shading language for production-quality rendering. It is also one of the first shading languages ever implemented.

It defines six major shader types:

- *Light source shaders* compute the color of light emitted from a point on a light source to a point on a target surface.
- *Surface shaders* model the color and position of points on an object's surface, based on incoming light and the object's physical properties.
- *Displacement shaders* manipulate surface geometry independent of color.
- *Deformation shaders* transform the entire space. Only one RenderMan implementation, the AIR renderer by SiTex Graphics, implemented this shader type, supporting only a single linear transformation applied to the space.
- *Volume shaders* manipulate the color of light as it passes through a volume. They create effects such as fog.
- *Imager shaders* describe a color transformation to final pixel values. This is like an image filter, except the imager shader operates on data prior to quantization. Such data have more dynamic range and color resolution than can be displayed on a typical output device.

### Houdini VEX Shading Language

Houdini VEX (Vector Expressions) shading language (often abbreviated to "VEX") is closely modeled after RenderMan. However, its integration into a complete 3D package means that the shader writer can access the information inside the shader, a feature that is not usually available in a rendering context. The language differences between RSL and VEX are mainly syntactic, in addition to differences regarding the names of several shadeop names.

### Gelato Shading Language

Gelato's shading language, like Houdini's VEX, is closely modeled after RenderMan. The differences between Gelato Shading Language and RSL are mainly syntactical — Gelato uses semicolons instead of commas to separate arguments in function definitions and a few shadeops have different names and parameters.

### Open Shading Language

Open Shading Language (OSL) was developed by Sony Pictures Imageworks for use in its Autodesk Arnold Renderer. It is also used by Blender's Cycles render engine. OSL's surface and volume shaders define how surfaces or volumes scatter light in a way that allows for importance sampling; thus, it is well suited for physically-based renderers that support ray tracing and global illumination.

## Real-time rendering

Shading languages for real-time rendering are now widespread. They provide both higher hardware abstraction and a more flexible programming model than previous paradigms, which hardcoded transformation and shading equations. They deliver more control and richer content with less overhead.

Shaders that are designed to be executed directly on the GPU became useful for high-throughput general processing because of their stream programming model; this led to the development of compute shaders running on similar hardware (see also: GPGPU).

Historically, a few such languages dominated the market; they are described below.

### ARB assembly language

The OpenGL Architecture Review Board established the ARB assembly language in 2002 as a standard low-level instruction set for programmable graphics processors.

High-level OpenGL shading languages often compile to ARB assembly for loading and execution. Unlike high-level shading languages, ARB assembly does not support control flow or branching. However, it continues to be used when cross-GPU portability is required.

### OpenGL shading language

Also known as GLSL or *glslang*, this standardized shading language is meant to be used with OpenGL.

The language unifies vertex and fragment processing in a single instruction set, allowing conditional loops and branches. GLSL was preceded by the ARB assembly language.

### Cg programming language

The Cg language, developed by Nvidia, was designed for easy and efficient production pipeline integration. It features API independence and comes with many free tools to improve asset management. Development of Cg was stopped in 2012, and the language is now deprecated.

### DirectX Shader Assembly Language

The shader assembly language in Direct3D 8 and 9 is the main programming language for vertex and pixel shaders in Shader Model 1.0/1.1, 2.0, and 3.0. It is a direct representation of the intermediate shader bytecode which is passed to the graphics driver for execution.

The shader assembly language cannot be directly used to program unified Shader Model 4.0, 4.1, 5.0, and 5.1, although it retains its function as a representation of the intermediate bytecode for debug purposes.

### DirectX High-Level Shader Language

The High-Level Shading Language (HLSL) is a C-style shader language for DirectX 9 and higher and Xbox game consoles. It is related to Nvidia's Cg, but is only supported by DirectX and Xbox. HLSL programs are compiled into bytecode equivalent of DirectX shader assembly language.

HLSL was introduced as an optional alternative to the shader assembly language in Direct3D 9, but became a requirement in Direct3d 10 and higher, where the shader assembly language is deprecated.

### Adobe Pixel Bender and Adobe Graphics Assembly Language

Adobe Systems added Pixel Bender as part of the Adobe Flash 10 API. Pixel Bender could only process pixel but not 3D-vertex data. Flash 11 introduced an entirely new 3D API called Stage3D, which uses its own shading language called Adobe Graphics Assembly Language (AGAL), which offers full 3D acceleration support. GPU acceleration for Pixel Bender was removed in Flash 11.8.

AGAL is a low-level but platform-independent shading language, which can be compiled, for example, to the ARB assembly language or GLSL.

### PlayStation Shader Language

Sony announced PlayStation Shader Language (PSSL) as a shading language similar to Cg/HLSL, but specific to the PlayStation 4. PSSL is said to be largely compatible with the HLSL shader language from DirectX 12, but with additional features for the PS4 and PS5 platforms.

### Metal Shading Language

Apple has created a low-level graphics API, called Metal, which runs on most Macs made since 2012, iPhones since the 5S, and iPads since the iPad Air. Metal has its own shading language called Metal Shading Language (MSL), which is based on C++14 and implemented using clang and LLVM. MSL unifies vertex, fragment and compute processing.

### WebGPU Shading Language

WebGPU Shading Language (WGSL) is the shader language for WebGPU. That is, an application using the WebGPU API uses WGSL to express the programs, known as shaders, that run on the GPU.

## Translation

To port shaders from one shading language to another, a few approaches are used:

- Define a common interface. For example, Cg/HLSL, GLSL, and MSL all implement C preprocessor macros, so it is possible to wrap all the different operations into a common interface. Valve's Source 2 and NVIDIA's FXAA 3.11 do this.
- Translate one language to the other. For example, DirectX bytecode can be partially converted to GLSL via HLSLcc, and several tools for converting GLSL to HLSL such as ANGLE and HLSL2GLSL exist.
- Define an intermediate language. SPIR-V is designed partially for this purpose. It can be generated from HLSL or GLSL, and be decompiled into HLSL, GLSL, or MSL.

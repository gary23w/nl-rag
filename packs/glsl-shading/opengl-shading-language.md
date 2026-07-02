---
title: "OpenGL Shading Language"
source: https://en.wikipedia.org/wiki/OpenGL_Shading_Language
domain: glsl-shading
license: CC-BY-SA-4.0
tags: glsl shader, opengl shading language, fragment shader, vertex shader glsl
fetched: 2026-07-02
---

# OpenGL Shading Language

**OpenGL Shading Language** (**GLSL**) is a high-level shading language with a syntax based on the C programming language. It was created by the OpenGL ARB (OpenGL Architecture Review Board) to give developers more direct control of the graphics pipeline without having to use ARB assembly language or hardware-specific languages.

## Background

With advances in graphics cards, new features have been added to allow for increased flexibility in the rendering pipeline at the vertex and fragment level. Programmability at this level is achieved with the use of fragment and vertex shaders.

Originally, this functionality was achieved by writing shaders in ARB assembly language – a complex and unintuitive task. The OpenGL ARB created the OpenGL Shading Language to provide a more intuitive method for programming the graphics processing unit while maintaining the open standards advantage that has driven OpenGL throughout its history.

Originally introduced as an extension to OpenGL 1.4, GLSL was formally included into the OpenGL 2.0 core in 2004 by the OpenGL ARB. It was the first major revision to OpenGL since the creation of OpenGL 1.0 in 1992.

Some benefits of using GLSL are:

- Cross-platform compatibility on multiple operating systems, including Linux, macOS and Windows.
- The ability to write shaders that can be used on any hardware vendor's graphics card that supports the OpenGL Shading Language.
- Each hardware vendor includes the GLSL compiler in their driver, thus allowing each vendor to create code optimized for their particular graphics card’s architecture.

## Versions

GLSL versions have evolved alongside specific versions of the OpenGL API. It is only with OpenGL versions 3.3 and above that the GLSL and OpenGL major and minor version numbers match. These versions for GLSL and OpenGL are related in the following table:

| GLSL Version | OpenGL Version | Date | Shader Preprocessor |
|---|---|---|---|
| 1.10.59 | 2.0 | 30 April 2004 | #version 110 |
| 1.20.8 | 2.1 | 07 September 2006 | #version 120 |
| 1.30.10 | 3.0 | 22 November 2009 | #version 130 |
| 1.40.08 | 3.1 | 22 November 2009 | #version 140 |
| 1.50.11 | 3.2 | 04 December 2009 | #version 150 |
| 3.30.6 | 3.3 | 11 March 2010 | #version 330 |
| 4.00.9 | 4.0 | 24 July 2010 | #version 400 |
| 4.10.6 | 4.1 | 24 July 2010 | #version 410 |
| 4.20.11 | 4.2 | 12 December 2011 | #version 420 |
| 4.30.8 | 4.3 | 7 February 2013 | #version 430 |
| 4.40.9 | 4.4 | 16 June 2014 | #version 440 |
| 4.50.7 | 4.5 | 09 May 2017 | #version 450 |
| 4.60.8 | 4.6 | 14 August 2023 | #version 460 |

OpenGL ES and WebGL use **OpenGL ES Shading Language** (abbreviated: **GLSL ES** or **ESSL**).

| GLSL ES version | OpenGL ES version | WebGL version | Based on GLSL version | Date | Shader Preprocessor |
|---|---|---|---|---|---|
| 1.00.17 | 2.0 | 1.0 | 1.20 | 12 May 2009 | #version 100 |
| 3.00.6 | 3.0 | 2.0 | 3.30 | 29 January 2016 | #version 300 es |
| 3.10.5 | 3.1 |   | GLSL ES 3.00 | 29 January 2016 | #version 310 es |
| 3.20.8 | 3.2 |   | GLSL ES 3.10 | 14 August 2023 | #version 320 es |

The two languages are related but not directly compatible. They can be interconverted through SPIRV-Cross.

## Language

### Operators

GLSL contains the same operators as the operators in C and C++, with the exception of pointers. Bitwise operators were added in version 1.30.

### Functions and control structures

Similar to the C programming language, GLSL supports loops and branching, for instance: if-else, for, switch, etc. Recursion is forbidden and checked for during compilation.

User-defined functions are supported and built-in functions are provided. The graphics card manufacturer may optimize built-in functions at the hardware level. Many of these functions are similar to those in the math library of the C programming language while others are specific to graphics programming. Most of the built-in functions and operators, can operate both on scalars and vectors (up to 4 elements), for one or both operands. Common built-in functions that are provided and are commonly used for graphics purposes are: `mix`, `smoothstep`, `normalize`, `inversesqrt`, `clamp`, `length`, `distance`, `dot`, `cross`, `reflect`, `refract` and vector `min` and `max`. Other functions like `abs`, `sin`, `pow`, etc, are provided but they can also all operate on vector quantities, i.e. `pow(vec3(1.5, 2.0, 2.5))`, `abs(vec3(0.1, -0.2, 0.3)))`. GLSL supports function overloading (for both built-in functions and operators, and user-defined functions), so there might be multiple function definitions with the same name, having different number of parameters or parameter types. Each of them can have own independent return type.

### Preprocessor

GLSL defines a subset of the C preprocessor (CPP), combined with its own special directives for specifying versions and OpenGL extensions. The parts removed from CPP are those relating to file names such as `#include` and `__FILE__`.

The `GL_ARB_shading_language_include` extension (implemented for example in Nvidia drivers on Windows and Linux, and all Mesa 20.0.0 drivers on Linux, FreeBSD and Android) implements ability to use `#include` in source code, allowing easier sharing of code and definitions between many shaders without extra manual pre-processing. Similar extension `GL_GOOGLE_include_directive` and `GL_GOOGLE_cpp_style_line_directive` exist for using GLSL with Vulkan, and are supported in reference SPIR-V compiler (`glslang` aka glslangValidator).

## Compilation and execution

GLSL shaders are not stand-alone applications; they require an application that utilizes the OpenGL API, which is available on many different platforms (e.g., Linux, macOS, Windows). There are language bindings for C, C++, C#, JavaScript, Delphi, Java, and many more.

GLSL shaders themselves are simply a set of strings that are passed to the hardware vendor's driver for compilation from within an application using the OpenGL API's entry points. Shaders can be created on the fly from within an application, or read-in as text files, but must be sent to the driver in the form of a string.

The set of APIs used to compile, link, and pass parameters to GLSL programs are specified in three OpenGL extensions, and became part of core OpenGL as of OpenGL Version 2.0. The API was expanded with geometry shaders in OpenGL 3.2, tessellation shaders in OpenGL 4.0 and compute shaders in OpenGL 4.3. These OpenGL APIs are found in the extensions:

- ARB vertex shader
- ARB fragment shader
- ARB shader objects
- ARB geometry shader 4
- ARB tessellation shader
- ARB compute shader

GLSL shaders can also be used with Vulkan, and are a common way of using shaders in Vulkan. GLSL shaders are precompiled before use, or at runtime, into a binary bytecode format called SPIR-V, usually using offline compiler.

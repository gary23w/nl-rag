---
title: "Shader"
source: https://en.wikipedia.org/wiki/Shader
domain: gpu-driven-rendering
license: CC-BY-SA-4.0
tags: gpu driven rendering, indirect draw call, gpu culling pipeline, compute shader culling
fetched: 2026-07-02
---

# Shader

In computer graphics, a **shader** is a programmable operation which is applied to data as it moves through the rendering pipeline. Shaders act on data such as vertices and primitives, generate or morph geometries and fragments, and calculate the colors in a rendered image.

Shaders can execute a wide variety of operations. In modern real-time computer graphics, shaders are run on graphics processing units (GPUs) - dedicated hardware which provide parallel execution of programs. Because image rendering is an embarrassingly parallel problem (having an Amdahl's index of one), shaders benefit greatly from parallel computing, such as SIMD hardware. The drive for faster rendering has produced highly parallel processors, like GPUs, which are now used for general-purpose computing. Shaders used for general purposes are commonly called *compute shaders*.

## History

The term "shader" was first introduced to the public by Pixar with version 3.0 of their RenderMan Interface Specification, originally published in May 1988.

As graphics processing units evolved, major graphics software libraries such as OpenGL and Direct3D began to support shaders. The first shader-capable GPUs only supported pixel shading, but vertex shaders were quickly introduced once developers realized the power of shaders. The first video card with a programmable pixel shader was the Nvidia GeForce 3 (NV20), released in 2001. Geometry shaders were introduced with Direct3D 10 and OpenGL 3.2. Graphics hardware evolved toward a unified shader model, making all shaders equal.

## Graphics shaders

The traditional use of shaders is to operate on data in the graphics pipeline to control the rendering of an image. Graphics shaders are classified according to their position in the pipeline, the data being manipulated, and the graphics API being used.

### Vertex shaders

Vertex shaders are run once for each 3D vertex given to the graphics processor. The purpose is to transform each vertex's 3D position in virtual space to the 2D coordinate at which it appears on the screen (as well as a depth value for the Z-buffer). Vertex shaders can manipulate properties such as position, color and texture coordinates, but cannot create new vertices. The output of the vertex shader goes to the next stage in the pipeline, which is either a geometry shader if present, or the rasterizer. Vertex shaders can enable powerful control over the details of position, movement, lighting, and color in any scene involving 3D models.

### Geometry shaders

Geometry shaders were introduced in Direct3D 10 and OpenGL 3.2; formerly available in OpenGL 2.0+ with the use of extensions. This type of shader can generate new graphics primitives, such as points, lines, and triangles, from those primitives that were sent to the beginning of the graphics pipeline.

Geometry shader programs are executed after vertex shaders. They take as input a whole primitive, possibly with adjacency information. For example, when operating on triangles, the three vertices are the geometry shader's input. The shader can then emit zero or more primitives, which are rasterized and their fragments ultimately passed to a pixel shader.

Typical uses of a geometry shader include point sprite generation, geometry tessellation, shadow volume extrusion, and single pass rendering to a cube map. A typical real-world example of the benefits of geometry shaders would be automatic mesh complexity modification. A series of line strips representing control points for a curve are passed to the geometry shader and depending on the complexity required the shader can automatically generate extra lines each of which provides a better approximation of a curve.

### Fragment shaders

The

Stanford dragon

model rendered using fragment shaders with different outputs: solid white, applied texture, physically based shading.

Fragment shaders, also known as **pixel shaders**, compute color and other attributes of each "fragment": a unit of rendering work affecting at most a single output pixel. The simplest kinds of pixel shaders output one screen pixel as a color value; more complex shaders with multiple inputs/outputs are also possible. Pixel shaders range from simply always outputting the same color, to applying a lighting value, to doing bump mapping, shadows, specular highlights, translucency and other phenomena. They can alter the depth of the fragment (for Z-buffering), or output more than one color if multiple render targets are active. In 3D graphics, a pixel shader alone cannot produce some kinds of complex effects because it operates only on a single fragment, without knowledge of a scene's geometry (i.e. vertex data). However, pixel shaders do have knowledge of the screen coordinate being drawn, and can sample the screen and nearby pixels if the contents of the entire screen are passed as a texture to the shader. This technique can enable a wide variety of two-dimensional postprocessing effects such as blur, or edge detection/enhancement for cartoon/cel shaders. Pixel shaders may also be applied in *intermediate* stages to any two-dimensional images—sprites or textures—in the pipeline, whereas vertex shaders always require a 3D scene. For instance, a pixel shader is the only kind of shader that can act as a postprocessor or filter for a video stream after it has been rasterized.

### Tessellation shaders

OpenGL 4.0 and Direct3D 11 introduced a new shader class called a tessellation shader. It added two new shader stages to the traditional model: tessellation control shaders (also known as hull shaders) and tessellation evaluation shaders (also known as *domain shaders*), which together allow for simpler meshes to be subdivided into finer meshes at run-time according to a mathematical function. The function can be related to a variety of variables, most notably the distance from the viewing camera to allow active level-of-detail scaling. This allows objects close to the camera to have fine detail, while further away ones can have more coarse meshes, yet seem comparable in quality. It also can drastically reduce required mesh bandwidth by allowing meshes to be refined once inside the shader units instead of down-sampling very complex ones from memory. Some algorithms can up-sample any arbitrary mesh, while others allow for "hinting" in meshes to dictate the most characteristic vertices and edges.

### Primitive and Mesh shaders

Circa 2017, the AMD Vega microarchitecture added support for a new shader stage—primitive shaders—somewhat akin to compute shaders with access to the data necessary to process geometry.

Nvidia introduced mesh and task shaders with its Turing microarchitecture in 2018 which are also modelled after compute shaders. Nvidia Turing is the world's first GPU microarchitecture that supports mesh shading through DirectX 12 Ultimate API, several months before Ampere RTX 30 series was released.

In 2020, AMD and Nvidia released RDNA 2 and Ampere microarchitectures which both support mesh shading through DirectX 12 Ultimate. These mesh shaders allow the GPU to handle more complex algorithms, offloading more work from the CPU to the GPU, and in algorithm intense rendering, increasing the frame rate of or number of triangles in a scene by an order of magnitude. Intel announced that Intel Arc Alchemist GPUs shipping in Q1 2022 will support mesh shaders.

### Ray-tracing shaders

Ray tracing shaders are supported by Microsoft via DirectX Raytracing, by Khronos Group via Vulkan, GLSL, and SPIR-V, by Apple via Metal. Nvidia and AMD called the parts of the hardware responsible for executing these shaders "ray tracing cores".

## Compute kernels

Compute kernels are routines compiled for high throughput accelerators (such as graphics processing units (GPUs), digital signal processors (DSPs), or field-programmable gate arrays (FPGAs)), separate from but used by a main program (typically running on a central processing unit). They may be specified by a separate programming language such as "OpenCL C", as "compute shaders" written in a shading language, or embedded directly in application code written in a high level language. Compute kernels roughly correspond to inner loops when implementing algorithms in traditional languages (except there is no implied sequential operation), or to code passed to internal iterators. Microsoft support this as DirectCompute.

This single program, multiple data programming paradigm maps well to vector processors: there is an assumption that each invocation of a kernel within a batch is independent, allowing for data parallel execution. However, atomic operations may sometimes be used for synchronization between elements (for interdependent work), in some scenarios. Individual invocations are given indices (in 1 or more dimensions) from which arbitrary addressing of buffer data may be performed (including scatter gather operations), so long as the non-overlapping assumption is respected.

The Vulkan API provides the intermediate SPIR-V representation to describe *both* graphical shaders, and compute kernels in a language independent and machine independent manner. The intention is to facilitate language evolution and provide a more natural ability to leverage GPU compute capabilities, in line with hardware developments such as Unified Memory Architecture and Heterogeneous System Architecture. This allows closer cooperation between a CPU and GPU.

Much work has been done in the field of Kernel generation through LLMs as a means of optimizing code. KernelBench, created by the Scaling Intelligence Lab at Stanford, provides a framework to evaluate the ability of LLMs to generate efficient GPU kernels. Cognition has created Kevin 32-B to create efficient CUDA kernels which is currently the highest performing model on KernelBench.

### Compute shaders

*Computer shaders* refer to compute kernels written in a shading language. These shaders share execution units with vertex shaders and pixel shaders on GPUs, an example of GPGPU operation. They may be used in graphics pipelines for purposes such as additional stages in animation or lighting algorithms (e.g. tiled forward rendering) or be used for a non-graphics purpose. Some rendering APIs allow compute shaders to easily share data resources with the graphics pipeline, which eases the integration of graphics and compute.

### Tensor shaders

Tensor shaders are accelerator programs that deal with matrix operations on large arrays, a type of operation commonly used in neural network-based AI. They may be run on NPUs or GPUs. Tensor shaders are supported by Microsoft via DirectML, by Khronos Group via OpenVX, by Apple via Core ML, by Google via TensorFlow, by Linux Foundation via ONNX. Nvidia and AMD called the parts of the hardware responsible for executing these shaders "tensor cores".

## Programming

Several programming languages exist specifically for writing shaders, and which is used can depend on the target environment. The shading language for OpenGL is GLSL, and Direct3D uses HLSL. The Metal framework, used by Apple devices, has its own shading language called Metal Shading Language.

Increasingly in modern graphics APIs, shaders are compiled into SPIR-V, an intermediate language, before they are distributed to the end user. This standard allows more flexible choice of shading language, regardless of target platform. First supported by Vulkan and OpenGL, SPIR-V is also being adopted by Direct3D.

### GUI shader editors

Modern video game development platforms such as Unity, Unreal Engine and Godot increasingly include node-based editors that can create shaders without the need for written code; the user is instead presented with a directed graph of connected nodes that allow users to direct various textures, maps, and mathematical functions into output values like the diffuse color, the specular color and intensity, roughness/metalness, height, normal, and so on. The graph is then compiled into a shader.

In web development contexts, visual and component-based shader tools have also emerged. Platforms such as shaders.com provide component-driven composition of shaders for integration into frontend frameworks including Vue, React, and Svelte, while tools such as Shadertoy and FragCoord.xyz focus on lower-level shader authoring and debugging.

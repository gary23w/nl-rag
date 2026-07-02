---
title: "Fixed-function (computer graphics)"
source: https://en.wikipedia.org/wiki/Fixed-function
domain: forward-plus-rendering
license: CC-BY-SA-4.0
tags: forward plus rendering, tiled forward rendering, light culling forward, depth prepass rendering
fetched: 2026-07-02
---

# Fixed-function (computer graphics)

(Redirected from

Fixed-function

)

In computer graphics, **fixed-function** is a term primarily used to describe 3D graphics APIs and GPUs designed prior to the advent of programmable shaders. The term is also used to describe APIs and graphics pipelines that do not allow users to change its underlying processing techniques, hence the word 'fixed'. Fixed-function can also refer to graphics processing techniques that employ non-programmable dedicated hardware, like the use of ROPs to rasterize an image.

## History

Although the exact origin of the term 'fixed-function' is unclear, the first known graphics hardware that is considered to be fixed-function is the IBM 8514/A graphics add-in-board from 1987. When compared to other graphics hardware of its time, particularly hardware that made use of the RISC-based TMS34010, the 8514/A has similar processing speeds while also launching at a significantly less expensive price point. However, those benefits came at a cost of programming flexibility, as the 8514/A was designed more like an ASIC than its competition that were similar to general-purpose CPUs.

Following the 8514/A, the most powerful dedicated graphics hardware of the 1990s have pipelines that are not programmable, only configurable to a limited degree. This means that host CPUs have no direct influence on how its GPUs will process vertex and rasterization operations, beyond issuing indirect commands and transferring data bidirectionally from CPU-sided RAM to GPU-sided VRAM. As more hardware with this fixed-function design released, 3D graphics API developers of the 90s mimicked the nature of available hardware in their own software design by creating logical graphics pipelines that are only configurable and non-programmable. Graphics APIs of this time, notably OpenGL and early versions DirectX (Direct3D), are themselves retroactively referred to as fixed-function as they ultimately share many design characteristics with the fixed-function hardware they targeted.

Historically fixed-function APIs consisted of a set of function entry points that would approximately or directly map to dedicated logic for their named purpose in GPUs designed to support them. As shader based GPUs and APIs evolved, fixed-function APIs were implemented by graphics driver engineers using the more general purpose shading architecture. This approach served as a segue that would continue providing the fixed-function API abstraction most developers were experienced with while allowing further development and enhancements of the newer shader-based architectures.

OpenGL, OpenGL ES and DirectX are all 3D graphics APIs that went through the transition from the fixed-function programming model to the shader-based programming model. Below is a table of when the transition from fixed-function to shaders was made:

| 3D API | Last Fixed-function Version | First Shader Version |
|---|---|---|
| OpenGL | v1.5 | v2.0 |
| OpenGL ES | v1.1 | v2.0 |
| DirectX | v7.0 | v8.0 |

Even after the popularization of programmable shaders and graphics pipelines, certain GPU features would remain non-programmable to optimize for speed over flexibility. For example, the NVIDIA GeForce 6 series GPUs delegated early culling, rasterization, MSAA, depth queries, texture mapping and more to fixed-function implementations. The CPU does not direct the GPU how to specifically process these operations; these features can only be configured to a limited degree.

## Fixed function vs shaders

In a fixed-function pipeline, the stages of the graphics pipeline are pre-defined and can be configured by the programmer. A shader-based pipeline allows programmers to replace some of these stages with custom programs called shaders, which allows for more sophisticated rendering techniques and greater flexibility. However, even modern shader-based pipelines are not wholly programmable; APIs such as OpenGL and Direct3D 12 define graphics pipelines that combine programmable shader stages with fixed-function operations.

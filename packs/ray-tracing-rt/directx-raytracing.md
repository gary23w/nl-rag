---
title: "DirectX Raytracing"
source: https://en.wikipedia.org/wiki/DirectX_Raytracing
domain: ray-tracing-rt
license: CC-BY-SA-4.0
tags: ray tracing, ray tracing hardware, rtx gpu, bvh acceleration
fetched: 2026-07-02
---

# DirectX Raytracing

**DirectX Raytracing** (**DXR**) is a feature introduced in Microsoft's DirectX 12 that implements ray tracing, for video graphic rendering. DXR was released with the Windows 10 October update (version 1809) on October 10, 2018. It requires an AMD Radeon RX 6000, 7000, or 9000 series, Intel Arc A or B series, or Nvidia GeForce RTX 20, 30, 40, or 50 series video card, which is designed to handle the high computing load used for ray tracing.

## Additions to DirectX 12

With the introduction of DXR in October, four new features were added to DirectX 12:

1. *Acceleration structure* is a representation of the 3D environment that is efficiently formatted for the GPU. This environment is the plane that is used to create the starting points. The structure allows for modifications to be made and has optimized ray traversal.
2. The command list *DispatchRays,* is the start of the rays that are used to generate the reflection graphics. These are used by the GPU to begin the raytracing process.
3. New HLSL shaders, *ray-generation, closest-hit, any hit,* and *miss*, that are used describe computationally what DXR is doing when rendering raytracing. These shaders utilize the *TraceRay* function in HLSL to trace rays in the environment. When the ray interacts with the generated plane it can call on one of many selected hit or miss shaders. The variation of hit and miss shaders creates different textures.
4. *Raytracing pipeline state*, a counterpart to the current Graphics and Compute pipeline state objects. Pipeline state objects are hardware settings that determine how the GPU interprets and renders information.

## Technical details

DXR starts by sending out a ray from each pixel on a given plane and calculates which objects on the plane are hit by the ray first. Next, the DXR algorithm estimates the amount of light where the ray intersects the object and attaches that calculation to the object. Objects can have different properties that will absorb or reflect light at different rates. To stop infinite bounces of a ray from happening, DXR will stop calculations after a certain amount of intersections. Rays that never interact with an object are tracked for how far they have gone. This is so the algorithm understands when rays have gone too far.

## Updates

DXR was released to the public on October 10, 2018 with the Windows 10 October update (version 1809).

The first major update was made to DXR on May 27, 2020 with the Windows 10 May update (version 2004). The May update implemented DXR Tier 1.1, which allows game engines to make real time calculations which makes the raytracing graphics faster and more efficient.

During GDC 2025, Microsoft announced the next update to DXR (1.2) that will include standardized support for Opacity Micro-maps (OMM) and Shader Execution Reordering (SER). Major hardware vendors had announced official statements that they will implement the updated API spec into their products.

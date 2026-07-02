---
title: "Order-independent transparency"
source: https://en.wikipedia.org/wiki/Order-independent_transparency
domain: order-independent-transparency
license: CC-BY-SA-4.0
tags: order independent transparency, depth peeling transparency, alpha blending order, per-pixel linked list transparency
fetched: 2026-07-02
---

# Order-independent transparency

**Order-independent transparency** (OIT) is a class of techniques in rasterisational computer graphics for rendering transparency in a 3D scene, which do not require rendering geometry in sorted order for alpha compositing.

## Description

Commonly, 3D geometry with transparency is rendered by blending (using alpha compositing) all surfaces into a single buffer (think of this as a canvas). Each surface occludes existing color and adds some of its own color depending on its *alpha* value, a ratio of light *transmittance*. The order in which surfaces are blended affects the total occlusion or *visibility* of each surface. For a correct result, surfaces must be blended from farthest to nearest or nearest to farthest, depending on the alpha compositing operation, *over* or *under*. Ordering may be achieved by rendering the geometry in sorted order, for example sorting triangles by depth, but can take a significant amount of time, not always produce a solution (in the case of intersecting or circularly overlapping geometry) and the implementation is complex. Instead, order-independent transparency sorts geometry per-pixel, after rasterisation. For exact results this requires storing all fragments before sorting and compositing.

## History

The A-buffer is a computer graphics technique introduced in 1984 which stores per-pixel lists of fragment data (including micro-polygon information) in a software rasteriser, REYES, originally designed for anti-aliasing but also supporting transparency.

More recently, depth peeling in 2001 described a hardware accelerated OIT technique. With limitations in graphics hardware the scene's geometry had to be rendered many times. A number of techniques have followed, to improve on the performance of depth peeling, still with the many-pass rendering limitation. For example, Dual Depth Peeling (2008).

In 2009, two significant features were introduced in GPU hardware/drivers/Graphics APIs that allowed capturing and storing fragment data in a single rendering pass of the scene, something not previously possible. These are, the ability to write to arbitrary GPU memory from shaders and atomic operations. With these features a new class of OIT techniques became possible that do not require many rendering passes of the scene's geometry.

- The first was storing the fragment data in a 3D array, where fragments are stored along the *z* dimension for each pixel *x/y*. In practice, most of the 3D array is unused or overflows, as a scene's depth complexity is typically uneven. To avoid overflow the 3D array requires large amounts of memory, which in many cases is impractical.
- Two approaches to reducing this memory overhead exist.
  1. Packing the 3D array with a prefix sum scan, or *linearizing*, removed the unused memory issue but requires an additional depth complexity computation rendering pass of the geometry. The *"Sparsity-aware"* S-Buffer, Dynamic Fragment Buffer, *"deque"* D-Buffer, Linearized Layered Fragment Buffer all pack fragment data with a prefix sum scan and are demonstrated with OIT.
  2. Storing fragments in per-pixel linked lists provides tight packing of this data and in late 2011, driver improvements reduced the atomic operation contention overhead making the technique very competitive.

## Exact OIT

Exact, as opposed to approximate, OIT accurately computes the final color, for which all fragments must be sorted. For high depth complexity scenes, sorting becomes the bottleneck.

One issue with the sorting stage is local memory limited *occupancy*, in this case a SIMT attribute relating to the throughput and operation latency hiding of GPUs. *Backwards memory allocation* (BMA) groups pixels by their depth complexity and sorts them in batches to improve the occupancy and hence performance of low depth complexity pixels in the context of a potentially high depth complexity scene. Up to a 3× overall OIT performance increase is reported.

Sorting is typically performed in a local array, however performance can be improved further by making use of the GPU's memory hierarchy and sorting in registers, similarly to an external merge sort, especially in conjunction with BMA.

## Approximate OIT

Approximate OIT techniques relax the constraint of exact rendering to provide faster results. Higher performance can be gained from not having to store all fragments or only partially sorting the geometry. A number of techniques also compress, or *reduce*, the fragment data. These include:

- Stochastic Transparency: draw in a higher resolution in full opacity but discard some fragments. Downsampling will then yield transparency.
- Adaptive Transparency, a two-pass technique where the first constructs a visibility function which compresses on the fly (this compression avoids having to fully sort the fragments) and the second uses this data to composite unordered fragments. Intel's *pixel synchronization* avoids the need to store all fragments, removing the unbounded memory requirement of many other OIT techniques.
- Weighted Blended Order-Independent Transparency replaced the **over** operator with a commutative approximation. Feeding depth information into the weight produces visually-acceptable occlusion.
- Moment-based OIT stores moments of a per-pixel transmittance function and reconstructs an approximation during compositing, providing a compact approximate OIT method.

## OIT in Hardware

- The Sega Dreamcast games console included hardware support for automatic OIT.

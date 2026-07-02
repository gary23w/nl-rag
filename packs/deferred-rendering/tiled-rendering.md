---
title: "Tiled rendering"
source: https://en.wikipedia.org/wiki/Tiled_rendering
domain: deferred-rendering
license: CC-BY-SA-4.0
tags: deferred shading, g-buffer, deferred rendering, tiled rendering
fetched: 2026-07-02
---

# Tiled rendering

**Tiled rendering** is the process of subdividing a computer graphics image by a regular grid in optical space and rendering each section of the grid, or *tile*, separately. The advantage to this design is that the amount of memory and bandwidth is reduced compared to *immediate mode* rendering systems that draw the entire frame at once. This has made tile rendering systems particularly common for low-power handheld device use. Tiled rendering is sometimes known as a "sort middle" architecture, because it performs the sorting of the geometry in the middle of the graphics pipeline instead of near the end.

## Basic concept

Creating a 3D image for display consists of a series of steps. First, the objects to be displayed are loaded into memory from individual *models*. The system then applies mathematical functions to transform the models into a common coordinate system, the *world view*. From this world view, a series of polygons (typically triangles) is created that approximates the original models as seen from a particular viewpoint, the *camera*. Next, a compositing system produces an image by rendering the triangles and applying *textures* to the outside. Textures are small images that are painted onto the triangles to produce realism. The resulting image is then combined with various special effects, and moved into a frame buffer, which video hardware then scans to produce the displayed image. This basic conceptual layout is known as the *display pipeline*.

Each of these steps increases the amount of memory needed to hold the resulting image. By the time it reaches the end of the pipeline the images are so large that typical graphics card designs often use specialized high-speed memory and a very fast computer bus to provide the required bandwidth to move the image in and out of the various sub-components of the pipeline. This sort of support is possible on dedicated graphics cards, but as power and size budgets become more limited, providing enough bandwidth becomes expensive in design terms.

Tiled renderers address this concern by breaking down the image into sections known as tiles, and rendering each one separately. This reduces the amount of memory needed during the intermediate steps, and the amount of data being moved about at any given time. To do this, the system sorts the triangles making up the geometry by location, allowing to quickly find which triangles overlap the tile boundaries. It then loads just those triangles into the rendering pipeline, performs the various rendering operations in the GPU, and sends the result to the frame buffer. Very small tiles can be used, 16×16 and 32×32 pixels are popular tile sizes, which makes the amount of memory and bandwidth required in the internal stages small as well. And because each tile is independent, it naturally lends itself to simple parallelization.

In a typical tiled renderer, geometry must first be transformed into screen space and assigned to screen-space tiles. This requires some storage for the lists of geometry for each tile. In early tiled systems, this was performed by the CPU, but all modern hardware contains hardware to accelerate this step. The list of geometry can also be sorted front to back, allowing the GPU to use hidden surface removal to avoid processing pixels that are hidden behind others, saving on memory bandwidth for unnecessary texture lookups.

There are two main disadvantages of the tiled approach. One is that some triangles may be drawn several times if they overlap several tiles. This means the total rendering time would be higher than an immediate-mode rendering system. There are also possible issues when the tiles have to be stitched together to make a complete image, but this problem was solved long ago. More difficult to solve is that some image techniques are applied to the frame as a whole, and these are difficult to implement in a tiled render where the idea is to not have to work with the entire frame. These tradeoffs are well known, and of minor consequence for systems where the advantages are useful; tiled rendering systems are widely found in handheld computing devices.

Tiled rendering should not be confused with tiled/nonlinear framebuffer addressing schemes, which make adjacent pixels also adjacent in memory. These addressing schemes are used by a wide variety of architectures, not just tiled renderers.

## Early work

Much of the early work on tiled rendering was done as part of the Pixel Planes 5 architecture (1989).

The Pixel Planes 5 project validated the tiled approach and invented a lot of the techniques now viewed as standard for tiled renderers. It is the work most widely cited by other papers in the field.

The tiled approach was also known early in the history of software rendering. Implementations of Reyes rendering often divide the image into "tile buckets".

## Commercial products – Desktop and console

Early in the development of desktop GPUs, several companies developed tiled architectures. Over time, these were largely supplanted by immediate-mode GPUs with fast custom external memory systems.

Major examples of this are:

- PowerVR rendering architecture (1996): The rasterizer consisted of a 32×32 tile into which polygons were rasterized across the image across multiple pixels in parallel. On early PC versions, tiling was performed in the display driver running on the CPU. In the application of the Dreamcast console, tiling was performed by a piece of hardware. This facilitated deferred rendering—only the visible pixels were texture-mapped, saving shading calculations and texture-bandwidth.
- Oak Technology (1997) Warp 5. The Oak chip is the first in the market to combine tiling with other high-performance rendering algorithms such as antialiasing and trilinear mip-mapped textures, per Jon Peddie, president of Jon Peddie Associates.
- Microsoft Talisman (1996)
- Dreamcast (powered by PowerVR chipset) (1998)
- Gigapixel GP-1 (1999)
- Intel Larrabee GPU (2009) (canceled)
- PS Vita (powered by PowerVR chipset) (2011)
- Nvidia GPUs based on the Maxwell architecture and later architectures (2014)
- AMD GPUs based on the Vega (GCN5) architecture and later architectures (2017)
- Intel Gen11 GPU and later architectures (2019)

Examples of non-tiled architectures that use large on-chip buffers are:

- Xbox 360 (2005): the GPU contains an embedded 10 MB eDRAM; this is not sufficient to hold the raster for an entire 1280×720 image with 4× multisample anti-aliasing, so a tiling solution is superimposed when running in HD resolutions and 4× MSAA is enabled.
- Xbox One (2013): the GPU contains an embedded 32 MB eSRAM, which can be used to hold all or part of an image. It is not a tiled architecture, but is flexible enough that software developers can emulate tiled rendering.

## Commercial products – Embedded

Due to the relatively low external memory bandwidth, and the modest amount of on-chip memory required, tiled rendering is a popular technology for embedded GPUs. Current examples include:

Tile-based immediate mode rendering (TBIM):

- ARM Mali series.
- Qualcomm Adreno (series 300 and newer can also dynamically switch to immediate/direct mode rendering via FlexRender).

Tile-based deferred rendering (TBDR):

- Arm Mali series.
- Imagination Technologies PowerVR 5/6/7 series.
- Broadcom VideoCore IV series.
- Apple silicon GPUs.

Vivante produces mobile GPUs which have tightly coupled frame buffer memory (similar to the Xbox 360 GPU described above). Although this can be used to render parts of the screen, the large size of the rendered regions means that they are not usually described as using a tile-based architecture.

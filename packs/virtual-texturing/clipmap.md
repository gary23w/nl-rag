---
title: "Clipmap"
source: https://en.wikipedia.org/wiki/Clipmap
domain: virtual-texturing
license: CC-BY-SA-4.0
tags: virtual texturing, megatexture streaming, sparse texture residency, texture streaming pipeline
fetched: 2026-07-02
---

# Clipmap

In computer graphics, **clipmapping** is a method of clipping a mipmap to a subset of data pertinent to the geometry being displayed. The technique was introduced by Christopher C. Tanner, Christopher J. Migdal, and Michael T. Jones as a "virtual mipmap" for caching arbitrarily large textures in finite physical memory for real-time rendering. This is useful for loading as little data as possible when memory is limited, such as on a graphics processing unit. For terrain rendering, the idea was adapted into geometry clipmaps, which use nested regular grids centered on the viewer and update them incrementally as the viewpoint moves. The technique is used for LODing in NVIDIA’s implementation of voxel cone tracing. The high-resolution levels of the mipmapped scene representation are clipped to a region near the camera, while lower resolution levels are clipped further away.

## MegaTexture

MegaTexture is a clipmap implementation developed by id Software. It was introduced in their id Tech 4 engine and also appeared in id Tech 5 and id Tech 6 before being removed in id Tech 7. MegaTexture is a texture allocation technique that uses a single, extremely large texture rather than repeating multiple smaller textures. It is also featured in Splash Damage's game *Enemy Territory: Quake Wars*, and was developed by id Software former technical director John Carmack.

MegaTexture employs a single large texture space for static terrain. The texture is stored on removable media or a computer's hard drive and streamed as needed, allowing large amounts of detail and variation over a large area with comparatively little RAM usage. Depending on the pixel resolution per square meter, covering a large area could require several gigabytes of memory. However, RAM is also filled by the rest of the game and the underlying operating system, limiting the amount available for texturing. As the player moves around the game, different sections of the MegaTexture are loaded into memory. They are then scaled to the correct size and applied to the 3D models of the terrain.

Id has presented a more advanced technique that builds upon the MegaTexture idea and virtualizes both the geometry and the textures to obtain unique geometry down to the equivalent of the texel: the sparse voxel octree (SVO). It works by raycasting the geometry represented by voxels (instead of triangles) stored in an octree. The goal is to stream parts of the octree into video memory, going further down along the tree for nearby objects to give them more details, and to use higher level, larger voxels for farther objects, which give an automatic level of detail (LOD) system for both geometry and textures at the same time. The geometric detail that can be obtained using this method is nearly infinite, which removes the need for faking 3-dimensional details with techniques such as normal mapping. Despite that most voxel rendering tests use very large amounts of memory (up to several GB), Jon Olick of id Software claimed the technology is able to compress such SVO to 1.15 bits per voxel of position data.

## Virtual texturing

Unlike clipmaps, which clip each mip level around a viewpoint-dependent clipcenter and therefore work best for terrain, virtual texturing preprocesses texture data into equally sized tiles that can be streamed for arbitrary textured geometry. *Rage*, powered by the id Tech 5 engine, uses a more advanced technique called virtual texturing. Textures can measure up to 128000×128000 pixels and are also used for in-game models and sprites, etc. and not just the terrain.

*Wolfenstein: The New Order* and the 2016 version of *Doom* also use these. *Carmageddon: Reincarnation* also uses virtual texturing, though unlike id's virtual texturing system, which is designed for unique texture-mapping everywhere, their system is designed to use storage space sparingly while still offering good blend of texture variation and resolution.

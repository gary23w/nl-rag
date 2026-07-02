---
title: "Hidden-surface determination"
source: https://en.wikipedia.org/wiki/Frustum_culling
domain: forward-plus-rendering
license: CC-BY-SA-4.0
tags: forward plus rendering, tiled forward rendering, light culling forward, depth prepass rendering
fetched: 2026-07-02
---

# Hidden-surface determination

(Redirected from

Frustum culling

)

In 3D computer graphics, **hidden-surface determination** (also known as **shown-surface determination**, **hidden-surface removal** (**HSR**), **occlusion culling** (**OC**) or **visible-surface determination** (**VSD**)) is the process of identifying what surfaces and parts of surfaces can be seen from a particular viewing angle. A hidden-surface determination algorithm is a solution to the visibility problem, which was one of the first major problems in the field of 3D computer graphics. The process of hidden-surface determination is sometimes called **hiding**, and such an algorithm is sometimes called a **hider**. When referring to line rendering it is known as hidden-line removal. Hidden-surface determination is necessary to render a scene correctly, so that one may not view features hidden behind the model itself, allowing only the naturally viewable portion of the graphic to be visible.

## Background

Hidden-surface determination is a process that identifies which surfaces are not visible to the user (for example, because they lie behind opaque objects such as walls). Despite advances in hardware capability, rendering algorithms require substantial computational resources. By deciding that certain surfaces do not need to be rendered because they are not visible, rendering engines can improve efficiency, allowing the rendering of large world spaces.

There are many techniques for hidden-surface determination, but they generally rely on sorting the surfaces based on their distance from the viewer. Sorting large quantities of graphics primitives can be computationally-expensive and is usually done by divide and conquer. The different hidden-surface determination techniques differ, in part, through the way in which the space is partitioned prior to sorting.

## Algorithms

A rendering pipeline typically entails the following steps: projection, clipping, and rasterization.

Some algorithms used in rendering include:

**Z-buffering**

During rasterization, the depth (Z value) of each pixel (or

sample

in the case of anti-aliasing, but without loss of generality the term

pixel

is used) is checked against an existing depth value. If the current pixel is behind the pixel in the Z-buffer, the pixel is rejected, otherwise, it is shaded and its depth value replaces the one in the Z-buffer. Z-buffering supports dynamic scenes easily and is currently implemented efficiently in graphics hardware. This approach is the current standard. Z-buffering requires up to 4 bytes per pixel, and can have a substantial computational cost since the rasterization algorithm needs to check each rasterized sample against the Z-buffer. The Z-buffer algorithm can suffer from artifacts due to precision errors (also known as

Z-fighting

).

**Coverage buffers (C-buffer) and surface buffer (S-buffer)**

Faster than Z-buffering and commonly used in games such as

Quake I

, these approaches store information about already displayed segments for each line of the screen (in contrast of storing each pixel as is the case for Z-buffering). New polygons are then cut against already displayed segments that would hide them. An S-buffer can display unsorted polygons, while a C-buffer requires polygons to be displayed from the nearest to the furthest. Because the C-buffer technique does not require a pixel to be drawn more than once, the process is slightly faster. This approach was commonly used with

binary space partitioning

(BSP) trees.

**Sorted active edge list**

Used in

Quake I

, this technique stores a list of the edges of already displayed polygons (see

scanline rendering

). Polygons are displayed from the nearest to the furthest. New polygons are clipped against already displayed polygons' edges, creating new polygons to display, then storing the additional edges. Such an approach is harder to implement than S/C/Z-buffers, but it scales much better with increased image resolution.

**Painter's algorithm**

This algorithm sorts polygons by their

barycenter

and draws them back to front. This approach produces few artifacts when applied to scenes with polygons of similar size forming smooth meshes and

back-face culling

turned on. The drawbacks are the computational cost of the sorting step and the fact that visual artifacts can occur. This algorithm can fail for general scenes, as it cannot handle polygons in various common configurations, such as surfaces that intersect each other.

**Binary space partitioning (BSP)**

This technique divides a scene along planes corresponding to polygon boundaries. The subdivision is constructed in such a way as to provide an unambiguous depth ordering from any point in the scene when the BSP tree is traversed. The main disadvantage of the technique is the high computational cost of the construction of the BSP tree. As a result, this approach is less suitable for scenes consisting of dynamic geometry. The advantage of BSP is that the data is pre-sorted and error-free, and can be used as input for the previously mentioned algorithms. Note that the BSP is not a solution to hidden-surface removal, only an aid.

**Ray tracing**

Ray tracing attempts to model the path of light rays to a viewpoint by tracing rays from the viewpoint into the scene. Although not a hidden-surface removal algorithm as such, it implicitly solves the hidden-surface removal problem by finding the nearest surface along each view-ray. Effectively this approach is equivalent to sorting all the geometry on a per-pixel basis.

**The Warnock algorithm**

This algorithm divides the screen into smaller areas and sorts triangles within these. If there is ambiguity (i.e., polygons overlap in-depth extent within these areas), then further subdivision occurs. At the limit, the subdivision may occur down to the pixel level.

## Culling and visible-surface determination

A related area to visible-surface determination is *culling*, which usually happens before visible-surface determination in a rendering pipeline. Primitives or batches of primitives can be rejected in their entirety, which *usually* reduces the computational load in a rendering system. Types of culling algorithms include:

### Viewing-frustum culling

The viewing frustum is a geometric representation of the volume visible to the virtual camera. Naturally, objects outside this volume will not be visible in the final image, so they are discarded. Often, objects lie on the boundary of the viewing frustum. These objects are cut into pieces along this boundary in a process called clipping, and the pieces that lie outside the frustum are discarded as there is no place to draw them.

### Back-face culling

With 3D objects, some of the object's surface is facing the camera, and the rest is facing away from the camera, i.e. is on the backside of the object, hindered by the front side. If the object is completely opaque, those surfaces never need to be drawn. These surfaces are determined by the vertex winding order: if the triangle drawn has its vertices in clockwise order on the projection plane when facing the camera, they switch into counter-clockwise order when the surface turns away from the camera.

Incidentally, this approach also makes the objects completely transparent when the viewpoint camera is located inside them, because then all the surfaces of the object are facing away from the camera and are culled by the renderer. To prevent this artifact, the object must be set as double-sided (i.e. no back-face culling is done) or have separate inside surfaces.

### Contribution culling

Often, objects are so far away that they do not contribute significantly to the final image. These objects are thrown away if their screen projection is too small. See Clipping.

### Occlusion culling

Objects that are entirely behind other opaque objects may be culled. This is a very popular mechanism to speed up the rendering of large scenes that have a moderate to high depth complexity. There are several types of occlusion culling approaches:

- Potentially visible set (*PVS*) rendering divides a scene into regions and pre-computes visibility for them. These visibility sets are then indexed at run-time to obtain high-quality visibility sets (accounting for complex occluder interactions) quickly.
- Portal rendering divides a scene into cells/sectors (rooms) and portals (doors), and computes which sectors are visible by clipping them against portals.
- Hierarchical occlusion maps (HOM) represent the cumulative projection of occluders at multiple resolutions and perform overlap tests hierarchically through that pyramid; the method was designed for current graphics hardware, stores opacity separately from depth, and can support approximate visibility culling.

## Divide and conquer

A popular theme in the visible surface determination literature is divide and conquer. The Warnock algorithm pioneered dividing the screen. Beam tracing is a ray-tracing approach that divides the visible volumes into beams. Various screen-space subdivision approaches reduce the number of primitives considered per region, e.g. tiling, or screen-space BSP clipping. Tiling may be used as a preprocess to other techniques. Z-buffer hardware may typically include a coarse "hi-Z", against which primitives can be rejected early without rasterization. Such an approach is a form of occlusion culling.

Bounding volume hierarchies (BVHs) are often used to subdivide the scene's space (examples are the BSP tree, the octree and the kd-tree). This approach allows visibility determination to be performed hierarchically: if a node in the tree is considered to be *invisible*, then all of its child nodes are also invisible, and no further processing is necessary (they can all be rejected by the renderer). If a node is considered *visible*, then each of its children needs to be evaluated. This traversal is effectively a tree walk, where invisibility/occlusion or reaching a leaf node determines whether to stop or whether to recurse, respectively.

---
title: "Texture mapping"
source: https://en.wikipedia.org/wiki/Texture_mapping
domain: decal-rendering
license: CC-BY-SA-4.0
tags: decal rendering, deferred decal projection, texture splatting decal, screen space decal
fetched: 2026-07-02
---

# Texture mapping

**Texture mapping** is a term used in computer graphics to describe how 2D images are projected onto 3D models. The most common variant is the UV unwrap, which can be described as an inverse paper cutout, where the surfaces of a 3D model are cut apart so that it can be unfolded into a 2D coordinate space (UV space).

## Semantic

*Texture mapping* can multiply refer to (1) the task of unwrapping a 3D model (converting the surface of a 3D model into a 2D texture map), (2) applying a 2D texture map onto the surface of a 3D model, and (3) the 3D software algorithm that performs both tasks.

A *texture map* refers to a 2D image ("texture") that adds visual detail to a 3D model. The image can be stored as a raster graphic. Textures can also store properties beyond color and are then correspondingly referred to by other names, such as *normal map*, *roughness map*, or *emission map*

The coordinate space that converts from a 3D model's 3D space into a 2D space for sampling from the texture map is variously called *UV space*, *UV coordinates*, or *texture space*.

## Algorithm

The following is a simplified explanation of how an algorithm could work to render an image:

1. For each pixel, trace the coordinates of the screen into the 3D scene.
2. If a 3D model is hit or, more precisely, the polygon of a 3D model hits the 2D UV coordinates, then
3. The UV Coordinates are used to read the color from the texture and apply it to the pixel.

## History

The original technique was pioneered by Edwin Catmull in 1974 as part of his doctoral thesis.

Texture mapping originally referred to *diffuse mapping*, a method that simply mapped pixels from a texture to a 3D surface ("wrapping" the image around the object). In recent decades, the advent of multi-pass rendering, multitexturing, mipmaps, and more complex mappings such as height mapping, bump mapping, normal mapping, displacement mapping, reflection mapping, specular mapping, occlusion mapping, and many other variations on the technique (controlled by a materials system) have made it possible to simulate near-photorealism in real time by vastly reducing the number of polygons and lighting calculations needed to construct a realistic and functional 3D scene.

## Texture maps

A **texture map** is an image applied ("mapped") to the surface of a shape or polygon. This may be a bitmap image or a procedural texture. They may be stored in common image file formats, referenced by 3D model formats or material definitions, and assembled into resource bundles.

They may have one to three dimensions, although two dimensions are most common for visible surfaces. For use with modern hardware, texture map data may be stored in swizzled or tiled orderings to improve cache coherency. Rendering APIs typically manage texture map resources (which may be located in device memory) as buffers or surfaces, and may allow 'render to texture' for additional effects such as post processing or environment mapping.

Texture maps usually contain RGB color data (either stored as direct color, compressed formats, or indexed color), and sometimes an additional channel for alpha blending (RGBA) especially for billboards and decal overlay textures. It is possible to use the alpha channel (which may be convenient to store in formats parsed by hardware) for other uses such as specularity.

Multiple texture maps (or channels) may be combined for control over specularity, normals, displacement, or subsurface scattering, e.g. for skin rendering.

Multiple texture images may be combined in texture atlases or array textures to reduce state changes for modern hardware. (They may be considered a modern evolution of tile map graphics). Modern hardware often supports cube map textures with multiple faces for environment mapping.

### Creation

Texture maps may be acquired by scanning or digital photography, designed in image manipulation software such as GIMP or Photoshop, or painted onto 3D surfaces directly in a 3D paint tool such as Mudbox or ZBrush.

### Texture application

This process is akin to applying patterned paper to a plain white box. Every vertex in a polygon is assigned a texture coordinate (which in the 2D case is also known as UV coordinates). This may be done through explicit assignment of vertex attributes, manually edited in a 3D modelling package through UV unwrapping tools. It is also possible to associate a procedural transformation from 3D space to texture space with the material. This might be accomplished via planar projection or, alternatively, cylindrical or spherical mapping. More complex mappings may consider the distance along a surface to minimize distortion. These coordinates are interpolated across the faces of polygons to sample the texture map during rendering. Textures may be repeated or mirrored to extend a finite rectangular bitmap over a larger area, or they may have a one-to-one unique "injective" mapping from every piece of a surface (which is important for render mapping and light mapping, also known as baking).

#### Texture space

Texture mapping maps the model surface (or screen space during rasterization) into *texture space*; in this space, the texture map is visible in its undistorted form. UV unwrapping tools typically provide a view in texture space for manual editing of texture coordinates. Some rendering techniques such as subsurface scattering may be performed approximately by texture-space operations.

### Multitexturing

Multitexturing is the use of more than one texture at a time on a polygon. For instance, a light map texture may be used to light a surface as an alternative to recalculating that lighting every time the surface is rendered. *Microtextures* or *detail textures* are used to add higher frequency details, and *dirt maps* add weathering and variation; this can greatly reduce the apparent periodicity of repeating textures. Modern graphics may use more than 10 layers, which are combined using shaders, for greater fidelity. Another multitexture technique is bump mapping, which allows a texture to directly control the facing direction of a surface for the purposes of its lighting calculations; it can give a very good appearance of a complex surface (such as tree bark or rough concrete) that takes on lighting detail in addition to the usual detailed coloring. Bump mapping has become popular in video games, as graphics hardware has become powerful enough to accommodate it in real-time.

### Texture filtering

The way that samples (e.g. when viewed as pixels on the screen) are calculated from the texels (texture pixels) is governed by texture filtering. The cheapest method is to use the nearest-neighbour interpolation, but bilinear interpolation or trilinear interpolation between mipmaps are two commonly used alternatives which reduce aliasing or jaggies. In the event of a texture coordinate being outside the texture, it is either clamped or wrapped. Anisotropic filtering better eliminates directional artefacts when viewing textures from oblique viewing angles.

### Texture streaming

Texture streaming is a means of using data streams for textures, where each texture is available in two or more different resolutions, as to determine which texture should be loaded into memory and used based on draw distance from the viewer and how much memory is available for textures. Texture streaming allows a rendering engine to use low resolution textures for objects far away from the viewer's camera, and resolve those into more detailed textures, read from a data source, as the point of view nears the objects.

### Baking

As an optimization, it is possible to render detail from a complex, high-resolution model or expensive process (such as global illumination) into a surface texture (possibly on a low-resolution model). This technique is called *baking* (or *render mapping*) and is most commonly used for light maps, but may also be used to generate normal maps and displacement maps. Some computer games (e.g. *Messiah*) have used this technique. The original *Quake* software engine used on-the-fly baking to combine light maps and colour maps in a process called *surface caching*.

Baking can be used as a form of level of detail generation, where a complex scene with many different elements and materials may be approximated by a single element with a single texture, which is then algorithmically reduced for lower rendering cost and fewer drawcalls. It is also used to take high-detail models from 3D sculpting software and point cloud scanning and approximate them with meshes more suitable for realtime rendering.

## Rasterisation algorithms

Various techniques have evolved in software and hardware implementations. Each offers different trade-offs in precision, versatility, and performance.

### Affine texture mapping

**Affine texture mapping** linearly interpolates texture coordinates across a surface, making it the fastest form of texture mapping. Some software and hardware (such as the original PlayStation) project vertices in 3D space onto the screen during rendering and linearly interpolate the texture coordinates *in screen space* between them. This may be done by incrementing fixed-point UV coordinates or by an incremental error algorithm akin to Bresenham's line algorithm.

In contrast to perpendicular polygons, this leads to noticeable distortion with perspective transformations (as shown in the figure: the checker box texture appears bent), especially as primitives near the camera. This distortion can be reduced by subdividing polygons into smaller polygons.

Using quad primitives for rectangular objects can look less incorrect than if those rectangles were split into triangles. However, since interpolating four points adds complexity to the rasterization, most early implementations preferred triangles only. Some hardware, such as the forward texture mapping used by the Nvidia NV1, offered efficient quad primitives. With perspective correction, triangles become equivalent to quad primitives and this advantage disappears.

For rectangular objects that are at right angles to the viewer (like floors and walls), the perspective only needs to be corrected in one direction across the screen rather than both. The correct perspective mapping can be calculated at the left and right edges of the floor. Affine linear interpolation across that horizontal span will look correct because every pixel along that line is the same distance from the viewer.

### Perspective correctness

**Perspective correct texturing** accounts for the vertices' positions in 3D space rather than simply interpolating coordinates in 2D screen space. While achieving the correct visual effect, perspective correct texturing is more expensive to calculate.

To perform perspective correction of the texture coordinates u and v , with z being the depth component from the viewer's point of view, it is possible to take advantage of the fact that the values ${\frac {1}{z}}$ , ${\frac {u}{z}}$ , and ${\frac {v}{z}}$ are linear in screen space across the surface being textured. In contrast, the original z , u , and v , before the division, are not linear across the surface in screen space. It is therefore possible to linearly interpolate these reciprocals across the surface, computing corrected values at each pixel, to produce a perspective correct texture mapping.

To do this, the reciprocals at each vertex of the geometry (three points for a triangle) are calculated. Vertex n has reciprocals ${\frac {u_{n}}{z_{n}}}$ , ${\frac {v_{n}}{z_{n}}}$ , and ${\frac {1}{z_{n}}}$ . Then, linear interpolation can be done on these reciprocals between the n vertices (e.g., using barycentric coordinates), resulting in interpolated values across the surface. At a given point, this yields the interpolated $u_{i},v_{i}$ and ${\frac {1}{z_{i}}}$ (reciprocal $z_{i}$ ). However, as our division by z altered their coordinate system, this $u_{i},v_{i}$ cannot be used as texture coordinates. To correct back to the $u,v$ space, the corrected z is calculated by taking the reciprocal once again: $z_{correct}={\frac {1}{\frac {1}{z_{i}}}}$ . This is then used to correct the $u_{i},v_{i}$ coordinates: $u_{correct}=u_{i}\cdot z_{i}$ and $v_{correct}=v_{i}\cdot z_{i}$ .

This correction makes it so that the difference from pixel to pixel between texture coordinates is smaller in parts of the polygon that are closer to the viewer (stretching the texture wider) and is larger in parts that are farther away (compressing the texture).

Affine texture mapping directly interpolates a texture coordinate $u_{\alpha }$ between two endpoints $u_{0}$ and $u_{1}$ : $u_{\alpha }=(1-\alpha )u_{0}+\alpha u_{1}$ where $0\leq \alpha \leq 1$ .

Perspective correct mapping interpolates after dividing by depth z , then uses its interpolated reciprocal to recover the correct coordinate: $u_{\alpha }={\frac {(1-\alpha ){\frac {u_{0}}{z_{0}}}+\alpha {\frac {u_{1}}{z_{1}}}}{(1-\alpha ){\frac {1}{z_{0}}}+\alpha {\frac {1}{z_{1}}}}}$ 3D graphics hardware typically supports perspective correct texturing.

Various techniques have evolved for rendering texture mapped geometry into images with different quality and precision trade-offs, which can be applied to both software and hardware.

Classic software texture mappers generally only performed simple texture mapping with one lighting effect at most (typically applied through a lookup table), and the perspective correctness was about 16 times more expensive.

### Restricted camera rotation

The *Doom* engine restricted the world to vertical walls and horizontal floors and ceilings, with a camera that could only rotate about the vertical axis. This meant the walls would be a constant depth coordinate along a vertical line and the floors and ceilings would have a constant depth along a horizontal line. After performing one perspective correction calculation for the depth, the rest of the line could use fast affine mapping. Some later renderers of this era simulated a small amount of camera pitch with shearing which allowed the appearance of greater freedom while using the same rendering technique.

Some engines were able to render texture mapped heightmaps (e.g. Nova Logic's Voxel Space, and the engine for *Outcast*) via Bresenham-like incremental algorithms, producing the appearance of a texture mapped landscape without the use of traditional geometric primitives.

### Subdivision for perspective correction

Every triangle can be further subdivided into groups of about 16 pixels in order to achieve two goals: keeping the arithmetic mill busy at all times and producing faster arithmetic results.

#### World space subdivision

For perspective texture mapping without hardware support, a triangle is broken down into smaller triangles for rendering and affine mapping is used on them. The reason this technique works is that the distortion of affine mapping becomes much less noticeable on smaller polygons. The Sony PlayStation made extensive use of this because it only supported affine mapping in hardware and had a relatively high triangle throughput compared to its peers.

#### Screen space subdivision

Software renderers generally prefer screen subdivision because it has less overhead. Additionally, they try to do linear interpolation along a line of pixels to simplify the set-up (compared to 2D affine interpolation), thus lessening the overhead further. Another reason is that affine texture mapping does not fit into the low number of CPU registers of the x86 CPU; the 68000 and RISC processors are much more suited for that approach.

A different approach was taken for *Quake*, which would calculate perspective correct coordinates only once every 16 pixels of a scanline and linearly interpolate between them, effectively running at the speed of linear interpolation because the perspective correct calculation runs in parallel on the co-processor. As the polygons are rendered independently, it may be possible to switch between spans and columns or diagonal directions depending on the orientation of the polygon normal to achieve a more constant z, but the effort seems not to be worth it.

#### Other techniques

One other technique is to approximate the perspective with a faster calculation, such as a polynomial. A second uses the ${\textstyle {\frac {1}{z_{i}}}}$ value of the last two drawn pixels to linearly extrapolate the next value. For the latter, the division is then done starting from those values so that all that has to be divided is a small remainder. However, the amount of bookkeeping needed makes this technique too slow on most systems.

A third technique, used by the Build Engine (used, most notably, in *Duke Nukem 3D*), builds on the constant distance trick used by the *Doom* engine by finding and rendering along the line of constant distance for arbitrary polygons.

### Hardware implementations

Texture mapping hardware was originally developed for simulation (e.g. as implemented in the Evans and Sutherland ESIG and Singer-Link Digital Image Generators DIG) and professional graphics workstations (such as Silicon Graphics) and broadcast digital video effects machines such as the Ampex ADO. Texture mapping hardware later appeared in arcade cabinets, consumer video game consoles, and PC video cards in the mid-1990s.

In flight simulations, texture mapping provided important motion and altitude cues necessary for pilot training not available on untextured surfaces. Additionally, texture mapping was implemented so that real-time processing of prefiltered texture patterns stored in memory could be accessed by the video processor in real-time.

Modern graphics processing units (GPUs) provide specialised fixed function units called *texture samplers*, or *texture mapping units*, to perform texture mapping, usually with trilinear filtering or better multi-tap anisotropic filtering and hardware for decoding specific formats such as DXTn. As of 2016, texture mapping hardware is ubiquitous as most SOCs contain a suitable GPU.

Some hardware implementations combine texture mapping with hidden-surface determination in tile-based deferred rendering or scanline rendering; such systems only fetch the visible texels at the expense of using greater workspace for transformed vertices. Most systems have settled on the z-buffering approach, which can still reduce the texture mapping workload with front-to-back sorting.

On earlier graphics hardware, there were two competing paradigms of how to deliver a texture to the screen:

1. Forward texture mapping iterates through each texel on the texture and decides where to place it on the screen.
2. Inverse texture mapping instead iterates through pixels on the screen and decides what texel to use for each.

Of these methods, inverse texture mapping has become standard in modern hardware.

#### Inverse texture mapping

With this method, a pixel on the screen is mapped to a point on the texture. Each vertex of a rendering primitive is projected to a point on the screen, and each of these points is mapped to a u,v texel coordinate on the texture. A rasterizer will interpolate between these points to fill in each pixel covered by the primitive.

The primary advantage of this method is that each pixel covered by a primitive will be traversed exactly once. Once a primitive's vertices are transformed, the amount of remaining work scales directly with how many pixels it covers on the screen.

The main disadvantage is that the memory access pattern in the texture space will not be linear if the texture is at an angle to the screen. This disadvantage is often addressed by texture caching techniques, such as the swizzled texture memory arrangement.

The linear interpolation can be used directly for simple and efficient affine texture mapping, but can also be adapted for perspective correctness.

#### Forward texture mapping

Forward texture mapping maps each texel of the texture to a pixel on the screen. After transforming a rectangular primitive to a place on the screen, a forward texture mapping renderer iterates through each texel on the texture, splatting each one onto a pixel of the frame buffer. This was used by some hardware, such as the 3DO, the Sega Saturn and the NV1.

The primary advantage is that the texture will be accessed in a simple linear order, allowing very efficient caching of the texture data. However, this benefit is also its disadvantage: as a primitive gets smaller on screen, it still has to iterate over every texel in the texture, causing many pixels to be overdrawn redundantly.

This method is also well suited for rendering quad primitives rather than reducing them to triangles, which provided an advantage when perspective correct texturing was not available in hardware. This is because the affine distortion of a quad looks less incorrect than the same quad split into two triangles . The NV1 hardware also allowed a quadratic interpolation mode to provide an even better approximation of perspective correctness.

UV mapping became an important technique for 3D modelling and assisted in clipping the texture correctly when the primitive went past the edge of the screen, but existing hardware did not provide effective implementations of this. These shortcomings could have been addressed with further development, but GPU design has mostly shifted toward using the inverse mapping technique.

## Applications

Beyond 3D rendering, the availability of texture mapping hardware has inspired its use for accelerating other tasks:

### Tomography

It is possible to use texture mapping hardware to accelerate both the reconstruction of voxel data sets from tomographic scans, and to visualize the results.

### User interfaces

Many user interfaces use texture mapping to accelerate animated transitions of screen elements, e.g. Exposé in Mac OS X.

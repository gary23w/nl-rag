---
title: "Z-buffering"
source: https://en.wikipedia.org/wiki/Z-buffering
domain: graphics
license: CC-BY-SA-4.0
tags: computer graphics, rasterization, ray tracing, shader, graphics pipeline, texture mapping
fetched: 2026-07-02
---

# Z-buffering

A **z-buffer**, also known as a **depth buffer**, is a type of data buffer used in computer graphics to store the depth information of fragments. The values stored represent the distance to the camera, with 0 being the closest. The encoding scheme may be flipped with the highest number being the value closest to camera.

In a 3D-rendering pipeline, when an object is projected on the screen, the depth (z-value) of a generated fragment in the projected screen image is compared to the value already stored in the buffer (**depth test**), and replaces it if the new value is closer. It works in tandem with the rasterizer, which computes the colored values. The fragment output by the rasterizer is saved if it is not overlapped by another fragment.

Z-buffering is a technique used in almost all contemporary computers, laptops, and mobile phones for generating 3D computer graphics. The primary use now is for video games, which require fast and accurate processing of 3D scenes.

## Usage

### Occlusion

Determining what should be displayed on the screen and what should be omitted is a multi-step process utilising various techniques. Using a z-buffer is the final step in this process.

Each time an object is rendered into the framebuffer the z-buffer is used to compare the z-values of the fragments with the z-value already in the z-buffer (i.e., check what is closer), if the new z-value is closer than the old value, the fragment is written into the framebuffer and this new closer value is written into the z-buffer. If the z-value is further away than the value in the z-buffer, the fragment is discarded. This is repeated for all objects and surfaces in the scene (often in parallel). In the end, the z-buffer will allow correct reproduction of the usual depth perception: a close object hides one further away. This is called **z-culling**.

The granularity of a z-buffer has a great influence on the scene quality: the traditional 16-bit z-buffer can result in artifacts (called "z-fighting" or **stitching**) when two objects are very close to each other. A more modern 24-bit or 32-bit z-buffer behaves much better, although the problem cannot be eliminated without additional algorithms. An 8-bit z-buffer is almost never used since it has too little precision.

### Shadow mapping

Z-buffer data obtained from rendering a surface from a light's point-of-view permits the creation of shadows by the shadow mapping technique.

## History

Z-buffering was first described in 1974 by Wolfgang Straßer in his PhD thesis on fast algorithms for rendering occluded objects. A similar solution to determining overlapping polygons is the painter's algorithm, which is capable of handling non-opaque scene elements, though at the cost of efficiency and incorrect results.

Z-buffers are often implemented in hardware within consumer graphics cards. Z-buffering is also used (implemented as software as opposed to hardware) for producing computer-generated special effects for films.

## Developments

Even with small enough granularity, quality problems may arise when precision in the z-buffer's distance values are not spread evenly over distance. Nearer values are much more precise (and hence can display closer objects better) than values that are farther away. Generally, this is desirable, but sometimes it will cause artifacts to appear as objects become more distant. A variation on z-buffering which results in more evenly distributed precision is called **w-buffering** (see below).

At the start of a new scene, the z-buffer must be cleared to a defined value, usually 1.0, because this value is the upper limit (on a scale of 0 to 1) of depth, meaning that no object is present at this point through the viewing frustum.

The invention of the z-buffer concept is most often attributed to Edwin Catmull, although Wolfgang Straßer described this idea in his 1974 Ph.D. thesis months before Catmull's invention.

On more recent PC graphics cards (1999–2005), z-buffer management uses a significant chunk of the available memory bandwidth. Various methods have been employed to reduce the performance cost of z-buffering, such as lossless compression (computer resources to compress/decompress are cheaper than bandwidth) and ultra-fast hardware z-clear that makes obsolete the "one frame positive, one frame negative" trick (skipping inter-frame clear altogether using signed numbers to cleverly check depths).

Some games, notably several games later in the Nintendo 64's life cycle, decided to either minimize z-buffering (for example, rendering the background first without z-buffering and only using z-buffering for the foreground objects) or to omit it entirely, to reduce memory bandwidth requirements and memory requirements respectively. Super Smash Bros. and F-Zero X are two Nintendo 64 games that minimized z-buffering to increase framerates. Several Factor 5 games also minimized or omitted z-buffering. On the Nintendo 64 z-Buffering can consume up to 4x as much bandwidth as opposed to not using z-buffering.

Mechwarrior 2 on PC supported resolutions up to 800 × 600 on the original 4 MB 3dfx Voodoo due to not using z-buffering.

## Z-culling

In rendering, z-culling is early pixel elimination based on depth, a method that provides an increase in performance when rendering of hidden surfaces is costly. It is a direct consequence of z-buffering, where the depth of each pixel candidate is compared to the depth of the existing geometry behind which it might be hidden.

When using a z-buffer, a pixel can be culled (discarded) as soon as its depth is known, which makes it possible to skip the entire process of lighting and texturing a pixel that would not be visible anyway. Also, time-consuming pixel shaders will generally not be executed for the culled pixels. This makes z-culling a good optimization candidate in situations where fillrate, lighting, texturing, or pixel shaders are the main bottlenecks.

While z-buffering allows the geometry to be unsorted, sorting polygons by increasing depth (thus using a reverse painter's algorithm) allows each screen pixel to be rendered fewer times. This can increase performance in fillrate-limited scenes with large amounts of overdraw, but if not combined with z-buffering it suffers from severe problems such as:

- polygons occluding one another in a cycle (e.g. triangle A occludes B, B occludes C, C occludes A)
- the lack of any canonical "closest" point on a triangle (i.e. no matter whether one sorts triangles by their centroid or closest point or furthest point, one can always find two triangles A and B such that A is "closer" but in reality B should be drawn first).

As such, a reverse painter's algorithm cannot be used as an alternative to z-culling (without strenuous re-engineering), except as an optimization to z-culling. For example, an optimization might be to keep polygons sorted according to x/y-location and z-depth to provide bounds, in an effort to quickly determine if two polygons might possibly have an occlusion interaction.

## Mathematics

The range of depth values in camera space to be rendered is often defined between a ${\textit {near}}$ and ${\textit {far}}$ value of z .

After a perspective transformation, the new value of z , or $z'$ , is defined by:

$z'={\frac {{\textit {far}}+{\textit {near}}}{{\textit {far}}-{\textit {near}}}}+{\frac {1}{z}}\left({\frac {-2\cdot {\textit {far}}\cdot {\textit {near}}}{{\textit {far}}-{\textit {near}}}}\right)$

After an orthographic projection, the new value of z , or $z'$ , is defined by:

$z'=2\cdot {\frac {{z}-{\textit {near}}}{{\textit {far}}-{\textit {near}}}}-1$

where z is the old value of z in camera space, and is sometimes called w or $w'$ .

The resulting values of $z'$ are normalized between the values of –1 and 1, where the ${\textit {near}}$ plane is at –1 and the ${\mathit {far}}$ plane is at 1. Values outside of this range correspond to points which are not in the viewing frustum, and shouldn't be rendered.

### Fixed-point representation

Typically, these values are stored in the z-buffer of the hardware graphics accelerator in fixed point format. First they are normalized to a more common range which is [0, 1] by substituting the appropriate conversion $z'_{2}={\frac {1}{2}}\left(z'_{1}+1\right)$ into the previous formula:

$z'={\frac {{\textit {far}}+{\textit {near}}}{2\cdot \left({\textit {far}}-{\textit {near}}\right)}}+{\frac {1}{2}}+{\frac {1}{z}}\left({\frac {-{\textit {far}}\cdot {\textit {near}}}{{\textit {far}}-{\textit {near}}}}\right)$

Simplifying:

$z'={\frac {\textit {far}}{\left({\textit {far}}-{\textit {near}}\right)}}+{\frac {1}{z}}\left({\frac {-{\textit {far}}\cdot {\textit {near}}}{{\textit {far}}-{\textit {near}}}}\right)$

Second, the above formula is multiplied by $S=2^{d}-1$ where d is the depth of the z-buffer (usually 16, 24, or 32 bits) and rounding the result to an integer:

$z'=f(z)=\left\lfloor \left(2^{d}-1\right)\cdot \left({\frac {\textit {far}}{\left({\textit {far}}-{\textit {near}}\right)}}+{\frac {1}{z}}\left({\frac {-{\textit {far}}\cdot {\textit {near}}}{{\textit {far}}-{\textit {near}}}}\right)\right)\right\rfloor$

This formula can be inverted and derived in order to calculate the z-buffer resolution (the "granularity" mentioned earlier). The inverse of the above $f(z)\,$ :

$z={\frac {-{\textit {far}}\cdot {\textit {near}}}{{\frac {z'}{S}}\left({\textit {far}}-{\textit {near}}\right)-{\textit {far}}}}={\frac {-S\cdot {\textit {far}}\cdot {\textit {near}}}{z'\left({\textit {far}}-{\textit {near}}\right)-{\textit {far}}\cdot S}}$

where $S=2^{d}-1$

The z-buffer resolution in terms of camera space would be the incremental value resulted from the smallest change in the integer stored in the z-buffer, which is +1 or –1. Therefore, this resolution can be calculated from the derivative of z as a function of $z'$ :

${\frac {dz}{dz'}}={\frac {-1\cdot -1\cdot S\cdot {\textit {far}}\cdot {\textit {near}}}{\left(z'\left({\textit {far}}-{\textit {near}}\right)-{\textit {far}}\cdot S\right)^{2}}}\cdot \left({\textit {far}}-{\textit {near}}\right)$

Expressing it back in camera space terms, by substituting $z'$ by the above $f(z)\,$ :

${\begin{aligned}{\frac {dz}{dz'}}&={\frac {-1\cdot -1\cdot S\cdot {\textit {far}}\cdot {\textit {near}}\cdot \left({\textit {far}}-{\textit {near}}\right)}{\left(S\cdot \left({\frac {-{\textit {far}}\cdot {\textit {near}}}{z}}+{\textit {far}}\right)-{\textit {far}}\cdot S\right)^{2}}}\\&={\frac {\left({\textit {far}}-{\textit {near}}\right)\cdot z^{2}}{S\cdot {\textit {far}}\cdot {\textit {near}}}}\\&={\frac {z^{2}}{S\cdot {\textit {near}}}}-{\frac {z^{2}}{S\cdot {\textit {far}}}}\approx {\frac {z^{2}}{S\cdot {\textit {near}}}}\end{aligned}}$

This shows that the values of $z'$ are grouped much more densely near the ${\textit {near}}$ plane, and much more sparsely farther away, resulting in better precision closer to the camera. The smaller $near$ is, the less precision there is far away—having the $near$ plane set too closely is a common cause of undesirable rendering artifacts in more distant objects.

To implement a z-buffer, the values of $z'$ are linearly interpolated across screen space between the vertices of the current polygon, and these intermediate values are generally stored in the z-buffer in fixed point format.

### W-buffer

To implement a w-buffer, the old values of z in camera space, or w , are stored in the buffer, generally in floating point format. However, these values cannot be linearly interpolated across screen space from the vertices—they usually have to be inverted, interpolated, and then inverted again. The resulting values of w , as opposed to $z'$ , are spaced evenly between ${\textit {near}}$ and ${\textit {far}}$ . There are implementations of the w-buffer that avoid the inversions altogether.

Whether a z-buffer or w-buffer results in a better image depends on the application.

## Algorithmics

The following pseudocode demonstrates the process of z-buffering:

```
// First of all, initialize the depth of each pixel.
d(i, j) = infinite // Max length

// Initialize the color value for each pixel to the background color
c(i, j) = background color

// For each polygon, do the following steps :
for (each pixel in polygon's projection)
{
    // Find depth i.e, z of polygon
    //   at (x, y) corresponding to pixel (i, j)   
    if (z < d(i, j))
    {
        d(i, j) = z;
        c(i, j) = color;
    }
}
```

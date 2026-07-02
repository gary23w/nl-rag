---
title: "Radiance (software)"
source: https://en.wikipedia.org/wiki/Radiance_(software)
domain: tone-mapping
license: CC-BY-SA-4.0
tags: tone mapping, hdr tone mapping, dynamic range compression image, exposure imaging
fetched: 2026-07-02
---

# Radiance (software)

**Radiance** is a suite of tools for performing *lighting simulation* originally written by Greg Ward. It includes a renderer as well as many other tools for measuring the simulated light levels. It uses ray tracing to perform all lighting calculations, accelerated by the use of an octree data structure. It pioneered the concept of high-dynamic-range imaging, where light levels are (theoretically) open-ended values instead of a decimal proportion of a maximum (e.g. 0.0 to 1.0) or integer fraction of a maximum (0 to 255 / 255). It also implements global illumination using the Monte Carlo method to sample light falling on a point.

Greg Ward started developing Radiance in 1985 while at Lawrence Berkeley National Laboratory. The source code was distributed under a license forbidding further redistribution. In January 2002 Radiance 3.4 was relicensed under a less restrictive license.

One study found Radiance to be the most generally useful software package for architectural lighting simulation. The study also noted that Radiance often serves as the underlying simulation engine for many other packages.

## HDR image format

Radiance defined an image format for storing HDR images, now described as *RGBE image format*. Since it was the first (and for a long time the only) HDR image format, this format is supported by many other software packages.

The file starts with the signature '#?RADIANCE' and then several lines listing the commands used to generate the image. This information allows the renderer **rpict** to continue a partially completed render (either manually, or using the **rad** front-end). There are also *key*=*value* declarations, including the line 'FORMAT=32-bit_rle_rgbe'.

After this is a blank line signifying the end of the header. A single line describes the resolution and pixel order. As produced by the Radiance tools this always takes the form of '-Y *height* +X *width'*. After this line follows the binary pixel data.

Radiance calculates light values as floating point triplets, one each for red, green and blue. But storing a full double precision float for each channel (8 bytes × 3 = 24 bytes) is a burden even for modern systems. Two stages are used to compress the image data. The first scales the three floating point values to share a common 8-bit *exponent*, taken from the brightest of the three. Each value is then truncated to an 8-bit mantissa (fractional part). The result is four bytes, 32 bits, for each pixel. This results in a 6:1 compression, at the expense of reduced colour fidelity.

The second stage performs run-length encoding on the 32-bit pixel values. This has a limited impact on the size of most rendered images, but it is fast and simple.

## Scene description format

A radiance scene is made from one or more object files. The *.rad* format is a simple text file. It can specify individual geometric objects, as well as call programs by starting a line with an exclamation point '!'.

When specifying geometry the first line is

```
modifier type name
```

The following three lines contain parameters starting with an integer specifying the number of parameters. The parameters need not be on the same line, they can be continued on multiple lines to aid in readability.

Modifiers create materials and can be chained together, one *modifying* the next.

For example:

**myball.rad**

```
chrome sphere ball
0
0
4       0       0       10
       10
```

This can then be *arrayed* in another file using the **xform** program (described later):

**scene.rad**

```
void metal chrome
0
0
5       0.8     0.8     0.8
        0.9     0.0

!xform -a 5 -t 20 0 0 myball.rad
```

This creates a chrome material and five chrome spheres spaced 20 units apart along the X-axis.

Before a scene can be used, it must be compiled into an octree file ('.oct') using the **oconv** tool. Most of the rendering tools (see below) use an octree file as input.

## Tools

The Radiance suite includes over 50 tools. They were designed for use on Unix and Unix-like systems. Many of the tools act as filters, taking input on standard input and sending the processed result to standard output. These can be used on the Unix command line and piped to a new file, or included in Radiance scene files ('.rad') themselves, as shown above.

### Geometry manipulation

Several radiance programs manipulate Radiance scene data by reading from either a specified file or their standard input, and writing to standard output.

- **xform** allows an arbitrary number of transformations to be performed on a '.rad' file. The transformations include translation, rotation (around any of the three axes), and scaling. It also can perform multi-dimensional arraying.
- **replmarks** replaces certain triangles in a scene with objects from another file. Used for simplifying a scene when modelling in a 3D modeller.

### Generators

Generators simplify the task of modelling a scene, they create certain types of geometry from supplied parameters.

- **genbox** creates a box.
- **genrprism** extrudes a given 2D polygon along the Z-axis.
- **genrev** creates a surface of revolution from a given function.
- **genworm** creates a *worm* given four functions - the (x, y, z) coordinates of the path, and the radius of the worm.
- **gensurf** creates a tesselated surface from a given function.
- **gensky** creates a description for a CIE standard sky distribution.

### Geometry converters

Radiance includes a number of programs for converting scene geometry from other formats. These include:

- **nff2rad** converts *NFF* objects to Radiance geometry.
- **obj2rad** convert Wavefront *.obj* files to Radiance geometry.
- **obj2mesh** convert Wavefront *.obj* files to a Radiance *compiled mesh*. This can then be included in a scene using the recently added *mesh* primitive. More efficient than using **obj2rad** and includes texture coordinates.

### Rendering

- **rpict** is the renderer, producing a Radiance image on its standard output.
- **rvu** is an interactive renderer, opening an X11 window to show the render in progress, and allowing the view to be altered.
- **rtrace** is a tool for tracing specific rays into a scene. It reads the parameters for these rays on its standard input and returns the light value on standard output. **rtrace** is used by other tools, and can even be used to render images on its own by using the **vwray** program to generate view rays to be piped to it.
- **dayfact** is an interactive script to compute luminance values and daylight factors on a grid.
- **findglare** takes an image or scene and finds bright sources that would cause discomforting glare in human eyes.
- **mkillum** takes a surface (e.g. a window or lamp shade) and computes the lighting contribution going through it. This data is then used by the *illum* material modifier to make lighting from these secondary sources more accurate and efficient to compute.

### Image manipulation and analysis

- **pfilt** filters an image. The common technique to achieve anti-aliased images is to render several times larger than the desired size, and then filter the image down using **pfilt**.
- **pcompos** composites images, either with anchor coordinates or by adding several images on top of another.
- **pcond** conditions images. Can simulate a number of effects of the human visual response e.g. defocusing dark areas, veiling due to glare, and colour loss due to mesopic or scotopic vision in low light.
- **pinterp** interpolates between two images provided they both have z buffers. Uses **rtrace** to fill in gaps. Is used to speed up the rendering speed of simple animations.
- **ximage** is an image viewer for viewing HDR Radiance images. It can adjust the simulated exposure and apply some of the human visual effects of **pcond**.

### Integration

- **rad** is a front-end which reads a '.rif' file describing a scene and multiple camera views. Previously, make and a *makefile* were used in a similar role. **rad** coordinates **oconv**, **mkillum**, **rpict**/**rview** and other programs to render an image (or preview) from the source scene file(s).
- **trad** is a GUI front-end to **rad** using Tcl/Tk.
- **ranimate** is a front-end which coordinates many programs to generate *virtual walk-through* animations i.e. the camera moves but the scene is static.

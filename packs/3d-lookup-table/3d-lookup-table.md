---
title: "3D lookup table"
source: https://en.wikipedia.org/wiki/3D_lookup_table
domain: 3d-lookup-table
license: CC-BY-SA-4.0
tags: 3d lookup table
fetched: 2026-07-03
---

# 3D lookup table

In the film and graphics industries, **3D lookup tables** (**3D LUT**s) are used for color grading and for mapping one color space to another. They are commonly used to calculate preview colors for a monitor or digital projector of how an image will be reproduced on another display device, typically the final digitally projected image or release print of a movie. A 3D LUT is a 3D lattice of output RGB color values that can be indexed by sets of input RGB colour values. Each axis of the lattice represents one of the three input color components; the input color thus defines a point inside the lattice. Since the point may not be on a lattice point, the lattice values must be interpolated; most products use trilinear interpolation.

3D LUTs are used extensively in the movie production chain, as part of the digital intermediate process.

Cubes may be of various sizes and bit depths. Often 33×33×33 cubes are used as 3D LUTs. The most common practice is to use RGB 10-bit/component log images as the input to the 3D LUT. Output is usually RGB values that are to be placed unchanged into a display device's buffer.

Modern GPU of graphics cards have direct support for 3D LUTs, allowing entire HD images to be processed at 60 fps or faster. Also, modern display controller of monitors have support for 3D LUTs.

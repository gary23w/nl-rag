---
title: "OpenEXR"
source: https://en.wikipedia.org/wiki/OpenEXR
domain: hdr-imaging
license: CC-BY-SA-4.0
tags: high dynamic range imaging, hdr rendering, perceptual quantizer, openexr format
fetched: 2026-07-02
---

# OpenEXR

**OpenEXR** is a high-dynamic range, multi-channel raster file format, released as an open standard along with a set of software tools created by Industrial Light & Magic (ILM), under a free software license similar to the BSD license.

It is notable for supporting multiple channels of potentially different pixel sizes, including 32-bit unsigned integer, 32-bit and 16-bit floating point values, as well as various compression techniques which include lossless and lossy compression algorithms. It also has arbitrary channels and encodes multiple points of view such as left- and right-camera images.

## Overview

A full technical introduction of the format is available on the OpenEXR website.

OpenEXR, or EXR for short, is a deep raster format developed by ILM and broadly used in the computer-graphics industry, both visual effects and animation.

OpenEXR's multi-resolution and arbitrary channel format makes it appealing for compositing, as it alleviates several painful elements of the process. Since it can store arbitrary channels—specular, diffuse, alpha, RGB, normals, and various other types—in one file, it takes away the need to store this information in separate files. The multi-channel concept also reduces the necessity to "bake" in the aforementioned data to the final image. If a compositor is not happy with the current level of specularity, they can adjust that specific channel.

OpenEXR's API makes tools development a relative ease for developers. Since there are almost never two identical production pipelines, custom tools always need to be developed to address problems (e.g. image-manipulation issue). OpenEXR's library allows quick and easy access to the image's attributes such as tiles and channels.

The OpenEXR library is developed in C++ and is available in source format as well as compiled format for Microsoft Windows, macOS and Linux. Python bindings for the library are also available for version 2.x.

### History

OpenEXR was created by ILM in 1999 and released to the public in 2003 along with an open source software library. It soon received wide adoption by software used in computer graphics, particularly for film and television production. The format has been updated several times, adding support for tiles, mipmaps, new compression methods, and other features. In 2007, OpenEXR was honored with an Academy Award for Technical Achievement.

OpenEXR 2.0 was released in April 2013, extending the format with support for deep image buffers and multiple images embedded in a single file. Version 2.2, released August 2014, added the lossy DWA compression format.

## Distribution

The OpenEXR software distribution includes:

- libraries
- Half, a C++ class for manipulating half values as if they were a built-in C++ data type
- exrdisplay, a sample application for viewing OpenEXR images on a display at various exposure settings

### Libraries

- IlmImf = library made by Industrial Light & Magic (Ilm) for low-level operations on the files with OpenEXR image format (Imf)
  - libIlmImf on linux
  - IlmImf.dll on windows
- IlmImfUtil
- Imath

## Color depth

OpenEXR has support for color depth using:

- 16-bit floating-point (half)
- 32-bit floating-point
- 32-bit unsigned integer

## Compression methods

There are three general types of lossless compression built into OpenEXR, with two different methods of Zip compressing. For most images without a lot of grain, the two Zip compression methods seem to work best, while the PIZ compression algorithm is better suited to grainy images. The following options are available:

**None**

Disables all compression.

**Run Length Encoding (RLE)**

This is a basic form of compression that is comparable to that used by standard

Targa

files.

**Zip (per scanline)**

deflate

compression with

zlib wrapper

applied to individual

scanlines

(not based on the

ZIP file format

despite its name).

**Zip (16 scanline blocks)**

deflate compression applied to blocks of 16 scanlines at time. This tends to be the most effective style of compression to use with rendered images that do not have film grain applied.

**PIZ (wavelet compression)**

This lossless method uses a new combined wavelet /

Huffman

compression. This form of compression is quite effective when dealing with grainy images, and will often surpass any of the other options under grainy conditions.

**PXR24 (24-bit data conversion then deflate compression)**

This form of compression from

Pixar Animation Studios

converts 32-bit floats to 24 bits then uses deflate compression. It is lossless for half and 32-bit integer data and slightly lossy for 32-bit float data.

**B44**

This form of compression is lossy for half data and stores 32-bit data uncompressed. It maintains a fixed compression size of either 2.28:1 or 4.57:1 and is designed for realtime playback. B44 compresses uniformly regardless of image content.

**B44A**

An extension to B44 where areas of flat color are further compressed, such as alpha channels.

**DWAA**

JPEG-like lossy compression format contributed by

DreamWorks Animation

. Compresses 32 scanlines together.

**DWAB**

Same as DWAA, but compresses blocks of 256 scanlines.

## Credits

From OpenEXR.org's Technical Introduction:

> The ILM OpenEXR file format was designed and implemented by Florian Kainz, Wojciech Jarosz, and Rod Bogart. The PIZ compression scheme is based on an algorithm by Christian Rouet. Josh Pines helped extend the PIZ algorithm for 16-bit and found optimizations for the float-to-half conversions. Drew Hess packaged and adapted ILM's internal source code for public release and maintains the OpenEXR software distribution. The PXR24 compression method is based on an algorithm written by Loren Carpenter at Pixar Animation Studios.

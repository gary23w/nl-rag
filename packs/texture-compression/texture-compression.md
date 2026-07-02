---
title: "Texture compression"
source: https://en.wikipedia.org/wiki/Texture_compression
domain: texture-compression
license: CC-BY-SA-4.0
tags: texture compression, s3tc block compression, astc format, etc texture
fetched: 2026-07-02
---

# Texture compression

**Texture compression** is a specialized form of image compression designed for storing texture maps in 3D computer graphics rendering systems. Unlike conventional image compression algorithms, texture compression algorithms are optimized for random access.

Texture compression can be applied to reduce memory usage at runtime. Texture data is often the largest source of memory usage in a mobile application.

## Tradeoffs

In their seminal paper on texture compression, Beers, Agrawala and Chaddha list four features that tend to differentiate texture compression from other image compression techniques. These features are:

**Decoding Speed**

It is highly desirable to be able to render directly from the compressed texture data and so, in order not to impact rendering performance, decompression must be fast.

**Random Access**

Since predicting the order that a renderer accesses

texels

would be difficult, any texture compression scheme must allow fast random access to decompressed texture data. This tends to rule out many better-known image compression schemes such as

JPEG

or

run-length encoding

.

**Compression Rate and Visual Quality**

In a rendering system, lossy compression can be more tolerable than for other use cases. Some texture compression libraries, such as crunch,

allow the developer to flexibly trade off compression rate vs. visual quality, using methods such as

rate–distortion optimization

(RDO).

**Encoding Speed**

Texture compression is more tolerant of asymmetric encoding/decoding rates as the encoding process is often done only once during the application authoring process.

Given the above, most texture compression algorithms involve some form of fixed-rate lossy vector quantization of small fixed-size blocks of pixels into small fixed-size blocks of coding bits, sometimes with additional extra pre-processing and post-processing steps. Block Truncation Coding is a very simple example of this family of algorithms.

Because their data access patterns are well-defined, texture decompression may be executed on-the-fly during rendering as part of the overall graphics pipeline, reducing overall bandwidth and storage needs throughout the graphics system. As well as texture maps, texture compression may also be used to encode other kinds of rendering map, including bump maps and surface normal maps. Texture compression may also be used together with other forms of map processing such as mipmaps and anisotropic filtering.

## Availability

Some examples of practical texture compression systems are S3 Texture Compression (S3TC), PVRTC, Ericsson Texture Compression (ETC) and Adaptive Scalable Texture Compression (ASTC); these may be supported by special function units in modern graphics processing units (GPUs).

OpenGL and OpenGL ES, as implemented on many video accelerator cards and mobile GPUs, can support multiple common kinds of texture compression - generally through the use of vendor extensions.

## Supercompression

A compressed-texture can be further compressed in what is called "supercompression". Fixed-rate texture compression formats are optimized for random access and are much less efficient compared to image formats such as PNG. By adding further compression, a programmer can reduce the efficiency gap. The extra layer can be decompressed by the CPU so that the GPU receives a normal compressed texture, or in newer methods, decompressed by the GPU itself. Supercompression saves the same amount of VRAM as regular texture compression, but saves more disk space and download size.

## Neural Texture Compression

Random-Access Neural Compression of Material Textures (Neural Texture Compression) is a Nvidia's technology which enables two additional levels of detail (16× more texels, so four times higher resolution) while maintaining similar storage requirements as traditional texture compression methods.

The key idea is compressing multiple material textures and their mipmap chains together, and using a small neural network, that is optimized for each material, to decompress them.

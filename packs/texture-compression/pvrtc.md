---
title: "PVRTC"
source: https://en.wikipedia.org/wiki/PVRTC
domain: texture-compression
license: CC-BY-SA-4.0
tags: texture compression, s3tc block compression, astc format, etc texture
fetched: 2026-07-02
---

# PVRTC

**PVRTC** (PowerVR Texture Compression) and PVRTC2 are a family of lossy, fixed-rate texture compression formats used in PowerVR's MBX (PVRTC only), SGX and Rogue technologies. The PVRTC algorithm is documented in Simon Fenney's paper "Texture Compression using Low-Frequency Signal Modulation" that was presented (slides) at Graphics Hardware 2003.

These differ from strictly block-based texture formats such as S3TC and Ericsson Texture Compression (ETC) in that the compressed image is represented by two lower resolution images which are bilinearly upscaled and then blended according to low precision, per-pixel weights. They also differ in that they support ARGB data in both 4-bpp and 2-bpp modes.

PVRTC is the compressed texture format used in the Nokia N9 and all generations of the iPhone, iPod Touch, and iPad. It is also supported in certain Android devices, that use PowerVR GPUs.

## Data structure

In both PVRTC and PVRTC2, texture data is stored in blocks (but note that the decoding of any 2x2 set of texels requires access to 4 of these blocks.) A data block always occupies 64 bits (8 bytes) of storage/memory space and thus, in 4-bit mode (4bpp), there will be one block for each 4×4 pixels. In 2-bit mode (2-bpp), there will be one block for every 8×4 pixels.

For example, a 1024×1024 4-bpp PVRTC texture would have 65,536 blocks and take 524,288 bytes of storage/memory space. In some hardware implementations, the blocks are arranged in a variant of Morton order.

With PVRTC there are six different variables stored in each block: Modulation data (32 bits), punch-through alpha flag (1 bit), color A (15 bits), color A opaque flag (1 bit), color B (14 bits) and color B opaque flag (1 bit).

With PVRTC2 there are six different variables stored to one block: Modulation data (32 bits), modulation flag (1 bit), color B (14 bits), hard transition flag (1 bit), color A (15 bits) and opacity flag (1 bit).

Although in PVRTC the opacity flags can be set independently for the A & B colours, in PVRTC2, Color A and Color B must both be in same format (i.e. either both RGB or both RGBA).

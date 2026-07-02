---
title: "Ericsson Texture Compression"
source: https://en.wikipedia.org/wiki/Ericsson_Texture_Compression
domain: texture-compression
license: CC-BY-SA-4.0
tags: texture compression, s3tc block compression, astc format, etc texture
fetched: 2026-07-02
---

# Ericsson Texture Compression

**Ericsson Texture Compression** (**ETC**) is a lossy texture compression technique developed in collaboration with Ericsson Research in early 2005. It was originally developed under the name **iPACKMAN** and based on an earlier compression scheme called **PACKMAN**.

## ETC1

The original 'ETC1' compression scheme provides 6x compression of 24-bit RGB data. It does not port the compression of images with Alpha components, although there are work-arounds for this.

ETC1 takes 4x4 groups of pixel data and compresses each into a single 64-bit word. The 4×4 pixel group is first divided into two 4×2 chunks - either horizontally or vertically. Each half is given a base color - either using 4/4/4 RGB or by giving one of them a 5/5/5 RGB and having the other be a 3/3/3 bit offset from that base. Each 4×2 region also has a 3-bit brightness range selection. Each pixel is then offset from the base color by adding one of four signed values to the base color for its half of the 4×4 group.

This format is a part of the OpenGL ES graphics standard extensions for embedded devices such as mobile phones and has been approved by the Khronos Group for use in the WebGL graphics standard for browser-side World Wide Web graphics.

Android version 2.2 (Froyo) includes support for ETC1.

## ETC2

The 'ETC2' scheme expands ETC1 in a backwards-compatible way to provide higher quality RGB compression, as well as compression of RGBA (RGB plus alpha).

The following ETC2 codecs are mandatory in OpenGL ES 3.0 and OpenGL 4.3:

- `GL_COMPRESSED_RGB8_ETC2` — Compresses RGB888 data, the followup of ETC1.
- `GL_COMPRESSED_RGBA8_ETC2_EAC` — Compresses RGBA8888 data with full alpha support.
- `GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2` — Compresses RGBA data where pixels are either fully transparent or fully opaque.

sRGB variants of the above codecs are also available.

## EAC

EAC is built on the same principles as ETC1/ETC2 but is used for one- or two-channel data. The following four EAC codecs are included as mandatory in OpenGL ES 3.0 and OpenGL 4.3:

- `GL_COMPRESSED_R11_EAC` — one channel unsigned data
- `GL_COMPRESSED_SIGNED_R11_EAC` — one channel signed data
- `GL_COMPRESSED_RG11_EAC` — two channel unsigned data
- `GL_COMPRESSED_SIGNED_RG11_EAC` — two channel signed data

## Encoding

The RGBA and RG11 formats are encoded in 128 bits per 4x4 block, while the rest are encoded in 64 bits per block. For RGBA, the RGB channels are encoded in a regular 64-bit block, while the A channel gets its own 64-bit block. RG11 formats are encoded similarly, with one 64-bit block per component.

## Software

A software utility called **ETCPACK** for compression and decompression of ETC1/ETC2 textures is available for free download in code form from Ericsson on GitHub.

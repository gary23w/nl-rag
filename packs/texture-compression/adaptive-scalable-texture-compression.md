---
title: "Adaptive scalable texture compression"
source: https://en.wikipedia.org/wiki/Adaptive_scalable_texture_compression
domain: texture-compression
license: CC-BY-SA-4.0
tags: texture compression, s3tc block compression, astc format, etc texture
fetched: 2026-07-02
---

# Adaptive scalable texture compression

**Adaptive scalable texture compression** (**ASTC**) is a lossy block-based texture compression algorithm developed by Jørn Nystad et al. of ARM Ltd. and AMD.

Full details of ASTC were first presented publicly at the High Performance Graphics 2012 conference, in a paper by Olson et al. entitled "Adaptive Scalable Texture Compression".

ASTC was adopted as an official extension for both OpenGL and OpenGL ES by the Khronos Group on 6 August 2012.

## Hardware support

| Vendor/product | Profile | Generation |
|---|---|---|
| AMD Radeon |   | ? |
| Apple GPUs | LDR only | A8 through A12 |
| Full | Since A13 |   |
| Arm Mali | Full | Since Mali-T620/T720/T820 |
| Imagination PowerVR | Full | Since Series6XT |
| Intel GPUs | Full | From Skylake ; Removed in Arc / Gen12.5 |
| Nvidia Tegra | ? | Since Kepler |
| Qualcomm Adreno | Full | LDR since 4xx series, at least 7xx series support GL_KHR_texture_compression_astc_hdr extension on Android 13 |

On Linux, all Gallium 3D drivers have a software fallback since 2018, so ASTC can be used on any AMD Radeon GPU.

## Overview

The method of compression is an evolution of Color Cell Compression with features including numerous closely spaced fractional bit rates, multiple color formats, support for high-dynamic-range (HDR) textures, and real 3D texture support.

The stated primary design goal for ASTC is to enable content developers to have better control over the space/quality tradeoff inherent in any lossy compression scheme. With ASTC, the ratio between adjacent bit rates is of the order of 25%, making it less expensive to increase quality for a given texture.

Encoding different assets often requires different color formats. ASTC allows a wide choice of input formats, including luminance-only, luminance-alpha, RGB, RGBA, and modes optimized for surface normals. The designer can thus choose the optimal format without having to support multiple different compression schemes.

The choices of bit rate and color format do not constrain each other, so that it's possible to choose from a large number of combinations.

Despite this flexibility, ASTC achieves better peak signal-to-noise ratios than PVRTC, S3TC, and ETC2 when measured at 2 and 3.56 bits per texel. For HDR textures, it produces results comparable to BC6H at 8 bits per texel.

## Technical features

The algorithm decouples the resolution of the weight grid from the texels, allowing each block to have a grid of up to 64 weights. These weights are then interpolated to determine the values for each texel using bilinear or trilinear interpolation.

In dual-plane mode, two separate weight values are specified for each texel. One color channel can be designated as the second plane and interpolated using an independent weight grid, selected via a 2-bit component selector. This is particularly useful for uncorrelated channels like alpha. Void-extent blocks are also available to efficiently encode constant color areas.

A fundamental component of ASTC is Bounded Integer Sequence Encoding (BISE), a low-level coding scheme that allows sequences of data values to be represented using a fractional number of bits per value. This is used for efficient non-power-of-two quantization of both color endpoints and weights.

ASTC also supports multi-partitioning, allowing a block to be divided into up to four spatial subsets, each with its own color endpoints. For high-dynamic-range (HDR) textures, it uses a pseudo-logarithmic representation to maintain consistent precision across a wide range of values.

## Supported color formats

ASTC supports anywhere from 1 to 4 channels. In modes with 2–4 channels, one of the channels can be treated as "uncorrelated" and be given a separate gradient for prediction. In any case, the data is decoded as RGBA.

| Channel count | RGBA interpretation | Description |
|---|---|---|
| 1 | L | Luminance-only: RGB set to same value in decoded buffer, alpha set to 1 |
| 2 | LA | Luminance with transparency |
| 2 | L+A | Luminance with uncorrelated transparency |
| 3 | RGB | Full color, alpha set to 1 |
| 3 | RG+B | Full color with uncorrelated blue (not actually used for color purposes) |
| 4 | RGBA | Full color with transparency |
| 4 | RGB+A | Full color with uncorrelated transparency |

Each of these may be encoded as low or high dynamic range. The encoder selects color formats independently for each block in the image.

In practice, ASTC may be used to represent data other than color. For example, the L+A format may be used to represent "X+Y", a normal map with uncorrelated components; the "RG+B" format can be used to represent XY+Z. The `astc-encoder` software supplied by ARM supports "X+Y" generation with the `-normal` option. The shader is expected to treat the decoded output as a swizzled texture.

## 2D block footprints and bit rates

ASTC textures are compressed using a fixed block size of 128 bits, but with a variable block footprint ranging from 4×4 texels up to 12×12 texels. The available bit rates thus range from 8 bits per texel down to 0.89 bits per texel, with fine steps in between.

| Block footprint | Bit rate | Increment |
|---|---|---|
| 4×4 | 8.00 | 25% |
| 5×4 | 6.40 | 25% |
| 5×5 | 5.12 | 20% |
| 6×5 | 4.27 | 20% |
| 6×6 | 3.56 | 14% |
| 8×5 | 3.20 | 20% |
| 8×6 | 2.67 | 5% |
| 10×5 | 2.56 | 20% |
| 10×6 | 2.13 | 7% |
| 8×8 | 2.00 | 25% |
| 10×8 | 1.60 | 25% |
| 10×10 | 1.28 | 20% |
| 12×10 | 1.07 | 20% |
| 12×12 | 0.89 |   |

In the above table, the "Increment" column shows the additional storage required to store a texture using this bit rate, as compared to the next smallest. Block footprints are presented as width × height.

## 3D block footprints and bit rates

ASTC 3D textures are compressed using a fixed block size of 128 bits, as for 2D but with a variable block footprint ranging from 3×3×3 texels up to 6×6×6 texels. The available bit rates thus range from 4.74 bits per texel down to 0.59 bits per texel, with fine steps in between.

| Block footprint | Bit rate | Increment |
|---|---|---|
| 3×3×3 | 4.74 | 33% |
| 4×3×3 | 3.56 | 33% |
| 4×4×3 | 2.67 | 33% |
| 4×4×4 | 2.00 | 25% |
| 5×4×4 | 1.60 | 25% |
| 5×5×4 | 1.28 | 25% |
| 5×5×5 | 1.02 | 20% |
| 6×5×5 | 0.85 | 20% |
| 6×6×5 | 0.71 | 20% |
| 6×6×6 | 0.59 |   |

Block footprints are presented as width × height × depth.

## Universal ASTC

UASTC (Universal ASTC) is a subset of ASTC specified by Binomial. The format is used in their Basis Universal "supercompressed" GPU texture format, which adds extra compression over compressed texture formats such as UASTC and ETC1S and allows for efficient conversion from UASTC/ETC1S to compressed texture formats directly usable by GPUs. UASTC, as part of Basis Universal, is part of the KTX (Khronos Texture) file format.

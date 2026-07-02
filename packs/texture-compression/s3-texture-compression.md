---
title: "S3 Texture Compression"
source: https://en.wikipedia.org/wiki/S3_Texture_Compression
domain: texture-compression
license: CC-BY-SA-4.0
tags: texture compression, s3tc block compression, astc format, etc texture
fetched: 2026-07-02
---

# S3 Texture Compression

**S3 Texture Compression** (**S3TC**) (sometimes also called **DXTn**, **DXTC**, or **BCn**) is a group of related lossy texture compression algorithms originally developed by Iourcha et al. of S3 Graphics, Ltd. for use in their Savage 3D computer graphics accelerator. The method of compression is strikingly similar to the previously published Color Cell Compression, which is in turn an adaptation of Block Truncation Coding published in the late 1970s. Unlike some image compression algorithms (e.g. JPEG), S3TC's fixed-rate data compression coupled with the single memory access (cf. Color Cell Compression and some VQ-based schemes) made it well-suited for use in compressing textures in hardware-accelerated 3D computer graphics. Its subsequent inclusion in Microsoft's DirectX 6.0 and OpenGL 1.3 (via the GL_EXT_texture_compression_s3tc extension) led to widespread adoption of the technology among hardware and software makers. While S3 Graphics is no longer a competitor in the graphics accelerator market, license fees have been levied and collected for the use of S3TC technology until October 2017, for example in game consoles and graphics cards. The wide use of S3TC has led to a de facto requirement for OpenGL drivers to support it, but the patent-encumbered status of S3TC presented a major obstacle to open source implementations, while implementation approaches which tried to avoid the patented parts existed.

## Patent

Some (e.g. US 5956431 A) of the multiple USPTO patents on S3 Texture Compression expired on October 2, 2017. At least one continuation patent, US6,775,417, however had a 165-day extension. This continuation patent expired on March 16, 2018.

## Codecs

There are five variations of the S3TC algorithm (named **DXT1** through **DXT5**, referring to the FourCC code assigned by Microsoft to each format), each designed for specific types of image data. All convert a 4×4 block of pixels to a 64-bit or 128-bit quantity, resulting in compression ratios of 6:1 with 24-bit RGB input data or 4:1 with 32-bit RGBA input data. S3TC is a lossy compression algorithm, resulting in image quality degradation, an effect which is minimized by the ability to increase texture resolutions while maintaining the same memory requirements. Hand-drawn cartoon-like images do not compress well, nor do normal map data, both of which usually generate artifacts. ATI's 3Dc compression algorithm is a modification of DXT5 designed to overcome S3TC's shortcomings with regard to normal maps. id Software worked around the normalmap compression issues in *Doom 3* by moving the red component into the alpha channel before compression and moving it back during rendering in the pixel shader.

Like many modern image compression algorithms, S3TC only specifies the method used to decompress images, allowing implementers to design the compression algorithm to suit their specific needs, although the patent still covers compression algorithms. The Nvidia GeForce 256 through to GeForce 4 cards also used 16-bit interpolation to render DXT1 textures, which resulted in banding when unpacking textures with color gradients. Again, this created an unfavorable impression of texture compression, not related to the fundamentals of the codec itself.

## DXT1

DXT1 (also known as Block Compression 1 or BC1) is the smallest variation of S3TC, storing 16 input pixels in 64 bits of output, consisting of two 16-bit RGB 5:6:5 color values $c_{0}$ and $c_{1}$ , and a 4×4 two-bit lookup table.

If $c_{0}>c_{1}$ (compare these colors by interpreting them as two 16-bit unsigned numbers), then two other colors are calculated, such that for each component, ${\textstyle c_{2}={2 \over 3}c_{0}+{1 \over 3}c_{1}}$ and ${\textstyle c_{3}={1 \over 3}c_{0}+{2 \over 3}c_{1}}$ . This mode operates similarly to mode 0xC0 of the original Apple Video codec.

Otherwise, if $c_{0}\leq c_{1}$ , then ${\textstyle c_{2}={1 \over 2}c_{0}+{1 \over 2}c_{1}}$ and $c_{3}$ is transparent black corresponding to a premultiplied alpha format. This color sometimes causes a black border surrounding the transparent area when linear texture filtering and alpha test is used, due to colors being interpolated between the color of opaque texel and neighbouring black transparent texel.

The lookup table is then consulted to determine the color value for each pixel, with a value of 0 corresponding to $c_{0}$ and a value of 3 corresponding to $c_{3}$ .

## DXT2 and DXT3

DXT2 and DXT3 (collectively also known as Block Compression 2 or BC2) converts 16 input pixels (corresponding to a 4x4 pixel block) into 128 bits of output, consisting of 64 bits of alpha channel data (4 bits for each pixel) followed by 64 bits of color data, encoded the same way as DXT1 (with the exception that the 4-color version of the DXT1 algorithm is always used instead of deciding which version to use based on the relative values of $c_{0}$ and $c_{1}$ ).

In DXT2, the color data is interpreted as being premultiplied by alpha, in DXT3 it is interpreted as not having been premultiplied by alpha. Typically DXT2/3 are well suited to images with sharp alpha transitions, between translucent and opaque areas.

## DXT4 and DXT5

DXT4 and DXT5 (collectively also known as Block Compression 3 or BC3) converts 16 input pixels into 128 bits of output, consisting of 64 bits of alpha channel data (two 8-bit alpha values and a 4×4 3-bit lookup table) followed by 64 bits of color data (encoded the same way as DXT1).

If $\alpha _{0}>\alpha _{1}$ , then six other alpha values are calculated, such that ${\textstyle \alpha _{2}={{6\alpha _{0}+1\alpha _{1}} \over 7}}$ , ${\textstyle \alpha _{3}={{5\alpha _{0}+2\alpha _{1}} \over 7}}$ , ${\textstyle \alpha _{4}={{4\alpha _{0}+3\alpha _{1}} \over 7}}$ , ${\textstyle \alpha _{5}={{3\alpha _{0}+4\alpha _{1}} \over 7}}$ , ${\textstyle \alpha _{6}={{2\alpha _{0}+5\alpha _{1}} \over 7}}$ , and ${\textstyle \alpha _{7}={{1\alpha _{0}+6\alpha _{1}} \over 7}}$ .

Otherwise, if ${\textstyle \alpha _{0}\leq \alpha _{1}}$ , four other alpha values are calculated such that ${\textstyle \alpha _{2}={{4\alpha _{0}+1\alpha _{1}} \over 5}}$ , ${\textstyle \alpha _{3}={{3\alpha _{0}+2\alpha _{1}} \over 5}}$ , ${\textstyle \alpha _{4}={{2\alpha _{0}+3\alpha _{1}} \over 5}}$ , and ${\textstyle \alpha _{5}={{1\alpha _{0}+4\alpha _{1}} \over 5}}$ with $\alpha _{6}=0$ and $\alpha _{7}=255$ .

The lookup table is then consulted to determine the alpha value for each pixel, with a value of 0 corresponding to $\alpha _{0}$ and a value of 7 corresponding to $\alpha _{7}$ . DXT4's color data is premultiplied by alpha, whereas DXT5's is not. Because DXT4/5 use an interpolated alpha scheme, they generally produce superior results for alpha (transparency) gradients than DXT2/3.

## Further variants

### BC4 and BC5

BC4 and BC5 (Block Compression 4 and 5) are added in Direct3D 10. They reuse the alpha channel encoding found in DXT4/5 (BC3).

- BC4 stores 16 input single-channel (e.g. greyscale) pixels into 64 bits of output, encoded in nearly the same way as BC3 alphas. The expanded palette provides higher quality.
- BC5 stores 16 input double-channel (e.g. tangent space normal map) pixels into 128 bits of output, consisting of two halves each encoded like BC4.

### BC6H and BC7

BC6H (sometimes BC6) and BC7 (Block Compression 6H and 7) are added in Direct3D 11.

- BC6H encodes 16 input RGB HDR (float16) pixels into 128 bits of output. It essentially treats float16 as 16 sign-magnitude integer value and interpolates such integers linearly. It works well for blocks without sign changes. A total of 14 modes are defined, though most differ minimally: only two prediction modes are really used.
- BC7 encodes 16 input RGB8/RGBA8 pixels into 128 bits of output. It can be understood as a much-enhanced BC3.

BC6H and BC7 have a much more complex algorithm with a selection of encoding modes. The quality is much better as a result. These two modes are also specified much more exactly, with ranges of accepted deviation. Earlier BCn modes decode slightly differently among GPU vendors.

## S3TC format comparison

| FOURCC | DX 10/11 name | Description | Alpha premultiplied? | Compression ratio | Texture type |
|---|---|---|---|---|---|
| DXT1 | BC1 | 1-bit alpha / opaque | Yes | 6:1 (for 24-bit source image) | Simple non-alpha |
| DXT2 | BC2 | Explicit alpha | Yes | 4:1 | Sharp alpha |
| DXT3 | BC2 | Explicit alpha | No | 4:1 | Sharp alpha |
| DXT4 | BC3 | Interpolated alpha | Yes | 4:1 | Gradient alpha |
| DXT5 | BC3 | Interpolated alpha | No | 4:1 | Gradient alpha |
| —N/a | BC4 | Interpolated greyscale | —N/a | 2:1 | Gradient |
| —N/a | BC5 | Interpolated two-channel | —N/a | 2:1 | Gradient |
| —N/a | BC6H | Interpolated HDR (no alpha) | —N/a | 6:1 | Gradient |
| —N/a | BC7 | Interpolated alpha | ? | 4:1 | Gradient |

## Data preconditioning

BCn textures can be further compressed for on-disk storage and distribution (texture supercompression). An application would decompress this extra layer and send the BCn data to the GPU as usual.

BCn can be combined with Oodle Texture, a lossy preprocessor that modifies the input texture so that the BCn output is more easily compressed by a LZ77 compressor (rate–distortion optimization). BC7 specifically can also use "bc7prep", a lossless pass to re-encode the texture in a more compressible form (requiring its inverse at decompression).

crunch is another tool that performs RDO and optionally further re-encoding.

In 2021, Microsoft produced a "BCPack" compression algorithm specifically for BCn-compressed textures. Xbox series X and S have hardware support for decompressing BCPack streams.

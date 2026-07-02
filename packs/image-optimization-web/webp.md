---
title: "WebP"
source: https://en.wikipedia.org/wiki/WebP
domain: image-optimization-web
license: CC-BY-SA-4.0
tags: image optimization, responsive picture element, webp image format, avif image format
fetched: 2026-07-02
---

# WebP

**WebP** (/ˈwɛpi/ *WEP-ee*) is a raster graphics file format developed by Google and intended as a replacement for the JPEG, PNG, and GIF file formats on the web. It supports image compression (both lossy and lossless), as well as animation and alpha compositing. The sister project for video is called WebM.

Google announced the WebP format in September 2010; the company released the first stable version of its supporting library in April 2018. WebP has seen widespread adoption across the Internet in order to reduce image size, with all major browsers currently supporting the format.

## History

WebP was first announced by Google on 30 September 2010 as a new open format for lossy compressed true-color graphics on the web, producing files that were smaller than JPEG files for comparable image quality. It was based on technology which Google had acquired with the purchase of On2 Technologies. As a derivative of the VP8 video format, it is a sister project to the WebM multimedia container format. WebP-related software is released under a BSD free software license.

On 3 October 2011, Google added an "Extended File Format" allowing WebP support for animation, ICC profile, XMP and Exif metadata, and tiling (compositing very large images from maximum 16384 × 16384 tiles). Tiling support was never finalized and was removed from the spec again.

On 18 November 2011, Google announced a new lossless compression mode, and support for transparency (alpha channel) in both lossless and lossy modes; support was enabled by default in libwebp 0.2.0 (16 August 2012). According to Google's measurements in November 2011, a conversion from PNG to WebP resulted in a 45% reduction in file size when starting with PNGs found on the web, and a 28% reduction compared to PNGs that are recompressed with pngcrush and PNGOUT.

In July 2016, Apple added WebP support to early beta versions of macOS Sierra and iOS 10, but support was later removed in the GM seed versions of iOS 10 and macOS Sierra released in September 2016. In September 2020, WebP support was added in Safari version 14.

The supporting libwebp library reached version 1.0 in April 2018.

In November 2024, WebP was formally specified in and published as RFC 9649.

## Technology

| Bytes | Content |   |   |   |
|---|---|---|---|---|
| 0–3 | R | I | F | F |
| 4–7 | *length* + 12 |   |   |   |
| 8–11 | W | E | B | P |
| 12–15 | V | P | 8 | (space) |
| 16–19 | *length* (padded) |   |   |   |
| 20–… | *VP8 key frame* |   |   |   |
| *pad* | ? (even length) |   |   |   |

WebP's lossy compression algorithm is based on the intra-frame coding of the VP8 video format and the Resource Interchange File Format (RIFF) as a container format. As such, it is a block-based transformation scheme with eight bits of color depth and a luminance–chrominance model with chroma subsampling by a ratio of 1:2 (YCbCr 4:2:0). Without further content, the mandatory RIFF container has an overhead of only twenty bytes, though it can also hold additional metadata. The side length of WebP images is limited to 16383 pixels.

WebP is based on block prediction. Each block is predicted on the values from the three blocks above it and from one block to the left of it (block decoding is done in raster-scan order: left to right and top to bottom). There are four basic modes of block prediction: horizontal, vertical, DC (one color), and TrueMotion. Mispredicted data and non-predicted blocks are compressed in a 4×4 pixel sub-block with a discrete cosine transform or a Walsh–Hadamard transform. Both transforms are done with fixed-point arithmetic to avoid rounding errors. The output is compressed with entropy encoding. WebP also has explicit support for parallel decoding.

The reference implementation consists of converter software in the form of a command-line program for Linux (cwebp) and a programming library for the decoding, the same as for WebM. The open-source community ported the converter to other platforms, such as Windows.

The WebP container (i.e., RIFF container for WebP) allows feature support over and above the basic use case of WebP (i.e., a file containing a single image encoded as a VP8 key frame). The WebP container provides additional support for:

**Metadata**

An image may have metadata stored in Exif or XMP formats.

**Transparency**

An image may have transparency, i.e., an alpha channel.

**Color profile**

An image may have an embedded ICC profile as described by the International Color Consortium.

### Lossless compression

WebP's lossless compression, a newer algorithm unrelated to VP8, was designed by Google software engineer Jyrki Alakuijala. It uses advanced techniques such as dedicated entropy codes for different color channels, exploiting 2D locality of backward reference distances and a color cache of recently used colors. This complements basic techniques such as dictionary coding, Huffman coding and color indexing transform. This format uses a recursive definition: all of the control images, such as the local entropy code selection, are encoded the same way as the whole image itself.

### Animation

Google has proposed using WebP for animated images as an alternative to the popular GIF format, citing the advantages of 24-bit color with transparency, combining frames with lossy and lossless compression in the same animation, and support for seeking to specific frames. Google reports a 64% reduction in file size for images converted from animated GIFs to lossy WebP, and a 19% reduction for lossless WebP.

## Support

### Web browsers

As of 2024, web browsers that support WebP had 97% market share.

Google actively promotes WebP. The proprietary PageSpeed Insights tool suggests that webmasters switch from JPEG and PNG to WebP in order to improve their website speed score.

Google Chrome and all Chromium-based browsers support WebP. Lossy WebP support was added to Chrome for desktop in version 17 (released February 2012) and lossless WebP support was added in version 23 (released November 2012); lossy and lossless support was added in Google Chrome for Android in version 25 (released March 2013).

Microsoft Edge versions released after January 2020 are based on the Chromium browser, and have native WebP support. EdgeHTML-based versions of Microsoft Edge support WebP through a platform extension (installed by default) (unless running in the security-hardened "Application Guard" mode, which does not support platform extensions).

Safari added support for WebP in September 2020 with iOS 14 and macOS Big Sur.

Mozilla Firefox officially supports WebP since January 2019. It was initially considered for implementation in 2013.

Pale Moon implemented initial support for WebP in January 2016 with its version 26 milestone.

SeaMonkey began supporting WebP with its version 2.53.5 released in November 2020.

GNOME Web, Midori, and Falkon natively support WebP.

WebP can also be displayed in all major browsers using the WebPJS JavaScript library, although support in Internet Explorer 6 and above is achieved using Flash.

Support for WebP was added to Links in version 2.26.

### Graphics software

After WebP was announced in September 2010, software gradually began to support it. By 2011, there were plugins for several popular graphics software programs to support WebP, and some programs such as Acorn and Pixelmator had added native support. Over time, support for the WebP format has grown.

| Software | First version with native support | Release date of native support | Notes | Reference |
|---|---|---|---|---|
| Pixelmator Classic | 1.6.2 | 6 October 2010 |   |   |
| Acorn | 2.6 | 21 October 2010 | Export of lossless WebP added in 2022 |   |
| ImageMagick | 6.6.8-5 | 14 March 2011 |   |   |
| GraphicConverter | 7.2 | 8 April 2011 |   |   |
| XnView | 1.98 | 9 May 2011 |   |   |
| PaintShop Pro | X4 (14.0) | 7 September 2011 |   |   |
| Picasa | 3.9 | 8 December 2011 |   |   |
| IrfanView | 4.32 | 15 December 2011 |   |   |
| GDAL | 1.9.0 | 9 January 2012 |   |   |
| gThumb | 3.1.1 | 23 September 2012 |   |   |
| PhotoLine | 18 | 4 October 2013 |   |   |
| Canvas X | 15 | 20 November 2013 |   |   |
| Krita | 2.9.5 | 10 June 2015 | Basic support |   |
| 5.1.0 | 18 August 2022 | Full support |   |   |
| Aseprite | 1.1.1 | 6 November 2015 |   |   |
| Sketch | 41 | 8 November 2016 |   |   |
| GIMP | 2.10 | 27 April 2018 |   |   |
| FastStone Image Viewer | 7.1 | 28 May 2019 | Writing WebP files supported in Version 8.1 (released July 31, 2025) |   |
| Paint.NET | 4.2.5 | 1 October 2019 |   |   |
| Pixelmator Pro | 1.6.4 | 4 June 2020 |   |   |
| Inkscape | 1.1 | 24 May 2021 | Export only |   |
| kdenlive | 21.04.3 | 8 July 2021 |   |   |
| Xara Designer Pro+ | 18.5 | 24 August 2021 |   |   |
| Adobe Illustrator | 26.0 | 16 October 2021 |   |   |
| Adobe Photoshop | 23.2 | 17 February 2022 |   |   |
| Blender | 3.2 | 8 June 2022 |   |   |
| LibreOffice Draw | 7.4 | 18 August 2022 |   |   |
| Affinity Designer | 2.0 | 9 November 2022 |   |   |
| Shotwell | 0.32.0 | 23 April 2023 |   |   |
| Windows Photos | 2023.11050.2013.0 | 3 May 2023 |   |   |
| CorelDRAW | 24.5 | 18 September 2023 |   |   |
| Clip Studio Paint | 3.0.0 | 14 March 2024 |   |   |
| PhotoMill | 2.8.0 | 11 November 2024 |   |   |
| DaVinci Resolve | 20.1 | 7 August 2025 |   |   |

In 2019, Google released a free plug-in that enables WebP support in earlier versions of Adobe Photoshop. Free Photoshop plug-ins had been released by Telegraphics and fnordware before that. GIMP up to version 2.8 also supported WebP via a plugin; later, this plugin was shipped in GIMP 2.9 branch, and received multiple improvements. Google has also released a plug-in for Microsoft Windows that enables WebP support in Windows Photo Viewer, Microsoft Office 2010, FastPictureViewer, and any other application that uses Windows Imaging Component.

### Other programs

FFmpeg linked with the VP8/VP9 reference codec library *libvpx* can extract VP8 key frames from WebM media and a script can then add the WebP RIFF header and the NUL pad byte for odd frame lengths. Meanwhile, FFmpeg supports *libwebp* directly.

Gmail and Google Photos both support WebP. Support for WebP is also planned for Google App Engine. The *Instant Previews* feature of Google Search uses WebP internally to reduce disk space used by previews. Android 4.0 supports encoding and decoding WebP images (via bitmap and Skia). SDL_image supports the format since 1.2.11.

Sumatra PDF supports WebP images for both standalone files and comic books since version 2.4.

Telegram Messenger uses WebP for its Stickers, claiming they are displayed five times faster compared to the other formats usually used in messaging apps.

Signal uses WebP for its non-animated stickers.

LibreOffice supports the import of WebP images since version 7.4, so does the LibreOffice technology based online office Collabora Online.

Godot Engine as of version 4.0 supports importing and exporting WebP images and uses WebP as its internal format for storing imported compressed textures.

Content management systems (CMS) usually do not support WebP natively or by default. However, for most popular CMS, extensions are available for automated conversion from other image formats to WebP and delivering WebP images to compatible browsers. Since June 2021, WordPress supports WebP natively.

Social media services known to natively support WebP in messages include Facebook, Slack, Discord and Element; however, some of these services only support static WebP, and not animated WebP.

## Disadvantages and criticism

Like VP8 on which it is based, lossy WebP supports only 8-bit YUV 4:2:0 format, which may cause color loss on images with thin contrast elements (such as in pixel art and computer graphics) and ghosting in anaglyph. Lossless WebP supports VP8L encoding that works exclusively with 8-bit RGBA (red, green, blue, alpha) color space. It has no support for 10-bit color depth, while the successors HEIC and AVIF added 10-bit color depth support.

Due to the complexity of their compression method, WebP files take significantly more time to create than other web image formats. It is therefore not always advisable to process WebP images on demand, for example in the context of Web Map Services.

In October 2013, Josh Aas from Mozilla Research published a comprehensive study of current lossy encoding techniques and was not able to conclude that WebP outperformed JPEG by any significant margin.

## Vulnerability

In September 2023, two critical vulnerabilities relating to WebP images were discovered by Apple Security Engineering and Architecture (SEAR) and the Citizen Lab, potentially affecting libwebp itself, Google Chrome and other Chromium-based browsers, as well as any other application using the library.

CVE-2023-4863 was the more actively exploited vulnerability of the two, with a high risk-rating of CVSS 8.8, which means it could lead to a buffer overflow, in applications using the affected library, upon exploitation of a maliciously crafted .webp lossless file, resulting in a denial of service (DoS), or worse, enabling malicious remote code execution (RCE).

The extensive use of libwebp packages across hundreds of applications, from web browsers to mobile apps, posed a major patching challenge to mitigate the vulnerability, due to the demanding pre-release testing requirements, which highlights the wide-scale implications of this vulnerability.

Several web browsers—including Google Chrome, Firefox, Microsoft Edge, and Brave—issued security patches following the discovery of the vulnerability. The vulnerability was ultimately patched in libwebp version 1.3.2.

## WebP 2

Google began developing a second version of WebP, plainly named WebP 2, in June 2021, the goal of which was to reach similar compression ratios as AVIF's while remaining faster to encode and decode; its reference implementation is `libwebp2`.

On 12 October 2022, Google changed the README file in WebP 2's development repository to state "WebP 2 will not be released as an image format" and described the version as a "playground for image compression experiments".

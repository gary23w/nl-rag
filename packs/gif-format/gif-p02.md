---
title: "GIF - Wikipedia (part 2/2)"
source: https://en.wikipedia.org/wiki/GIF
domain: gif-format
license: CC-BY-SA-4.0
tags: gif image, lzw compression, animated gif, indexed color
fetched: 2026-07-02
part: 2/2
---

## Alternatives

### PNG

Portable Network Graphics (PNG) was designed as a replacement for GIF to avoid infringement of Unisys' patent on the LZW compression technique. PNG offers better compression and more features than GIF, animation being the only significant exception. PNG is more suitable than GIF in instances where true-color imaging and alpha transparency are required.

Although support for PNG format came slowly, new web browsers support PNG. Older versions of Internet Explorer do not support all features of PNG. Versions 6 and earlier do not support alpha channel transparency without using Microsoft-specific HTML extensions. Gamma correction of PNG images was not supported before version 8, and the display of these images in earlier versions may have the wrong tint.

For identical 8-bit (or lower) image data, PNG files are typically smaller than the equivalent GIFs, due to the more efficient compression techniques used in PNG encoding. Complete support for GIF is complicated chiefly by the complex canvas structure it allows, though this is what enables the compact animation features.

### Animation formats

Videos resolve many issues that GIFs present through common usage on the web. They include drastically smaller file sizes, the ability to surpass the 8-bit color restriction, and better frame-handling and compression through inter-frame coding. Virtually universal support for the GIF format in web browsers, and a lack of official support for video in the HTML standard, caused GIF to rise to prominence for the purpose of displaying short video-like files on the web.

- MNG ("Multiple-image Network Graphics") was originally developed as a PNG-based solution for animations. MNG reached version 1.0 in 2001, but few applications support it.
- APNG ("Animated Portable Network Graphics") was proposed by Mozilla in 2006. APNG is an extension to the PNG format as an alternative to the MNG format. APNG is supported by most browsers as of 2019. APNG provides the ability to animate PNG files, while retaining backwards compatibility in decoders that cannot understand the animation chunk (unlike MNG). Older decoders will simply render the first frame of the animation.

The PNG group officially rejected APNG as an official extension on 20 April 2007.

There have been several subsequent proposals for a simple animated graphics format based on PNG using several different approaches.

Nevertheless, APNG is still under development by Mozilla and is supported in

Firefox 3.0

while MNG support was dropped.

APNG is currently supported by all major web browsers including Chrome (since version 59.0), Opera, Firefox and Edge.

- Embedded Adobe Flash objects and MPEG files were used on some websites to display simple video, but required the use of an additional browser plugin.
- WebM and WebP are in development and are supported by some web browsers.
- Other options for web animation include serving individual frames using AJAX, or animating SVG ("Scalable vector graphics") images using JavaScript or SMIL ("Synchronized Multimedia Integration Language").
- With the introduction of widespread support of the HTML video (`<video>`) tag in most web browsers, some websites use a looped version of the video tag generated. This gives the appearance of a GIF, but with the size and speed advantages of compressed video.

Notable examples are

Gfycat

and

Imgur

and their GIFV metaformat, which is really a video tag playing a looped

MP4

or

WebM

compressed video.

- HEIF ("High Efficiency Image File Format") is an image file format, finalized in 2015, which uses a discrete cosine transform (DCT) lossy compression algorithm based on the HEVC video format, and related to the JPEG image format. In contrast to JPEG, HEIF supports animation.

Compared to the GIF format, which lacks DCT compression, HEIF allows significantly more efficient compression. HEIF stores more information and produces higher-quality animated images at a small fraction of an equivalent GIF's size.

- VP9 only supports alpha compositing with 4:2:0 chroma subsampling, which may be unsuitable for GIFs that combine transparency with rasterised vector graphics with fine color details.
- AV1 video codec or AVIF can also be used either as a video or a sequenced image.

#### Uses

In April 2014, 4chan added support for silent WebM videos that are under 3 MB in size and 2 min in length, and in October 2014, Imgur started converting any GIF files uploaded to the site to H.264 video and giving the link to the HTML player the appearance of an actual file with a `.gifv` extension.

In January 2016, Telegram started re-encoding all GIFs to MPEG-4 videos that "require up to 95% less disk space for the same image quality."

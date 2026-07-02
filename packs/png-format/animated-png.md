---
title: "APNG"
source: https://en.wikipedia.org/wiki/Animated_PNG
domain: png-format
license: CC-BY-SA-4.0
tags: png image, deflate compression, lossless png, alpha compositing
fetched: 2026-07-02
---

# APNG

(Redirected from

Animated PNG

)

**Animated Portable Network Graphics** (**APNG**) is a file format which extends the Portable Network Graphics (PNG) specification to permit animated images that work similarly to animated GIF files, while supporting images with a higher color depth and full alpha transparency not available for GIFs. It also retains backward compatibility with non-animated PNG files. It was developed by the Mozilla Foundation in 2004.

The first frame of an APNG file is stored as a normal PNG stream, so most standard PNG decoders are able to display the first frame of an APNG file. The frame speed data and all of the subsequent frames are stored in extra chunks (as provided for by the original PNG specification).

APNG competed with Multiple-image Network Graphics (MNG), a comprehensive format for bitmapped animations which was created in 2001 by the same team as PNG, which is now obsolete. APNG's advantages over MNG are its smaller library size and its compatibility with older PNG implementations.

## History and development

The APNG specification was created in 2004 by Stuart Parmenter and Vladimir Vukićević of the Mozilla Corporation to allow for storing the animations needed for interfaces such as throbbers. In May 2003, Mozilla had scrapped support for MNG animations, which provides a superset of APNG functionality, citing concerns about the large file size required for the expansive MNG decoder library (300 KB); the APNG decoder, built on the back of the PNG decoder, was a much smaller component.

Among users and maintainers of the PNG and MNG formats, APNG had a lukewarm reception. In particular, PNG was conceived to be a single-image format. APNG hides the subsequent frames in PNG ancillary chunks in such a way that APNG-unaware applications would ignore them, but there are otherwise no changes to the format to allow software to distinguish between animated and non-animated images. Some of the main concerns arising from this were the inability of applications to negotiate for PNG and APNG, or distinguish between PNG and APNG once received, or for legacy software to even inform users that there are additional frames. Glenn Randers-Pehrson spearheaded efforts to reconcile the PNG purists' position with that of APNG proponents by recommending changes to APNG's format and proposing the use of a unique MIME type (e.g., video/png), but the APNG proponents only added the different MIME type (image/apng) while insisting on the use of the *.png* extension instead of *.apng*, leading to the format not being approved by the PNG Development Group.

The PNG Development Group rejected APNG as an official extension on 20 April 2007, and there have been several subsequent proposals for a simple animated graphics format based on PNG using several different approaches. However, since 14 September 2021, the PNG Working Group has been chartered by the World Wide Web Consortium (W3C) to maintain and develop for the PNG specification, and the first public working draft of PNG Specification (Third Edition) was published on 25 October 2022, adding APNG extensions to the core PNG specification. The Candidate Recommendation was published on 21 September 2023.

On 24 June 2025 it was finally elevated to the Recommendation final status by the W3C.

## File format

The APNG specification follows the PNG File format introducing three new ancillary chunks:

- The animation control chunk (acTL) precedes the IDAT(s) of the default image and is a kind of "marker" that this is an animated PNG file. It also contains the number of frames and the number of times to loop the animation (0 meaning infinite).
- The frame control chunk (fcTL) precedes each frame and contains its metadata : dimensions; position (relative to the default image); duration; if once over it is cleared to black, replaced by the previous frame or drawn over by the next frame; and if its transparency applies.
- The frame data chunk (fdAT) storing frame's content. It starts with a sequence number, then has the same structure as the default image's IDAT chunk(s).

Sequence numbers apply to both frame control and frame data chunks, which together follow a common sequence, thus enabling the order and timing of frames to be recovered should an APNG-unaware PNG editor re-order them as allowed by PNG chunk ordering rules.

Frames utilize the same bit depth, color type, compression method, filter method, interlace method, and palette (if any) as the default image.

An application reading a PNG file is meant to ignore any chunks which it does not understand, making APNG backwards compatible. Applications without support for the APNG extension show only the first frame, disregarding the rest of the frames.

### Compression and optimization

A number of optimization techniques make APNG files as small as possible: Inter-frame optimization utilizing alpha-blend and alpha dispose operations, smaller than the full-size subframes, dirty transparency, color type and color palette optimizations, and various compression options: zlib, 7-Zip, Zopfli.

### Derived formats

Animated stickers for Signal are APNG with some restrictions (the size of the file is limited to 300kb, the length of the animation is limited to 3 seconds and, visibly (this last point is unclear), the resolution must be 512x512px).

## Support

Mozilla Firefox added support for APNG in version 3 trunk builds on 23 March 2007. However, because libpng is the PNG Group's reference implementation of the official specification, APNG support was not added prior to version 1.8 of the main libpng distribution since it was unratified by the Group before. Iceweasel 3 supports APNG by using Mozilla's unofficial variant of libpng.

In 2008 WorldDMB adopted APNG as a backward compatible extension to enable animation as part of the MOT SlideShow user application for Digital Radio. "APNG 1.0 Specification - Animated Portable Network Graphics" is included as normative Annex A in the ETSI standard TS 101 499 V2.2.1. In 2016, Apple adopted the APNG format as the preferred format for animated stickers in iOS 10 iMessage apps. On 15 March 2017, APNG support was added to Chromium.

| Field | Software | Supports? | Since |
|---|---|---|---|
| Image processing | APNG Assembler | Yes | v. 2.91 |
| cphktool APNG Anime Maker | Yes | v. 1 (9 June 2009) |   |
| APNG Disassembler | Yes | v. 1 |   |
| APNG Optimizer | Yes | v. 1.0 (28 March 2011) |   |
| Chasys Draw IES | Yes | v. 5.17.05 |   |
| Clip Studio Paint | Yes | v. 1.6.7 (7 September 2017) |   |
| FFmpeg | Yes | v. 2.7 |   |
| FireAlpaca | Yes | v. 2.3.13 |   |
| Gamani GIF Movie Gear | Yes | v. 4.2 (March 2008) |   |
| GID | Read-only | v. 11 (December 2023) |   |
| GIMP | Read-only | v. 3.1.2 (23 June 2025) |   |
| Honeycam | Yes | v. 3.48 (29 November 2021) |   |
| Honeyview | Yes | v. 5.10 (17 February 2015) |   |
| ImageJ | Yes | v. 1.41g (3 July 2008) |   |
| ImageMagick | Yes | v. 7.0.10-31 (20 September 2020) |   |
| Imagine | Yes | v. 1.0.2 (4 May 2008) |   |
| IrfanView | Read-only | v. 4.40 (31 July 2015) |   |
| Konvertor | Yes | v. 4.02 (May 2010) |   |
| KSquirrel (later SAIL) | Read-only | v. 0.7.2 (3 October 2007) |   |
| Paint.NET | Needs plugin | —N/a |   |
| PhotoLine | Yes | v19.5 (11 March 2016) |   |
| RealWorld Paint | Yes | v. 2011.1 (December 2011) |   |
| VirtualDub | Needs plugin | —N/a |   |
| XnView | Read-only | v. 1.97.4 (30 April 2010) |   |
| Sciter and HTMLayout UI engines | Read-only | since 2008 |   |
| Krita | Yes | Krita Nightly 5.0.0 pre-alpha (since 22 February 2021) |   |
| qView | Read-only | v. 4.0 (31 October 2020) |   |
| Browser engines | WebKit | Yes | (17 March 2015) |
| Blink | Yes | June 2017 |   |
| Web browsers | Mozilla Firefox (Gecko layout engine) | Yes | v. 3 (17 June 2008) |
| SeaMonkey (Gecko layout engine) | Yes | v. 2 |   |
| Iceweasel and other Debian rebrandings (Gecko layout engine) | Yes | v. 4.0~b12 |   |
| Safari (WebKit layout engine) | Yes | v. 8.0 |   |
| Google Chrome and Chromium (Blink layout engine) | Yes | v. 59 (5 June 2017) |   |
| Internet Explorer (Trident layout engine) | No | —N/a |   |
| Microsoft Edge [Legacy] (EdgeHTML layout engine) | No | —N/a |   |
| Microsoft Edge (Blink layout engine) | Yes | v. 79 |   |
| Opera v12 and earlier (Presto layout engine) | Yes | v. 9.5 (12 June 2008) |   |
| Opera 15 and later (Blink layout engine) | Yes | v. 46.0 (22 June 2017) |   |
| Pale Moon (Goanna layout engine) | Yes | v. 27 |   |
| Mobile browsers | iOS Safari | Yes | v. 8.0 |
| Firefox for Android | Yes | ? |   |
| Samsung Internet for Android | Yes | v. 7.0 |   |
| Opera Mobile | Yes | v. 12 (27 February 2012) |   |
| Productivity software | LibreOffice | No | ? |

1. After loading a video, an APNG file can be created via the "File|Export|Animated PNG" menu item.

A server-side library exists that allows web browsers that support the canvas tag, but do not support APNG, to display APNGs. Examples of such browsers include Microsoft Edge Legacy and Internet Explorer 9.

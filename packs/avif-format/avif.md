---
title: "AVIF"
source: https://en.wikipedia.org/wiki/AVIF
domain: avif-format
license: CC-BY-SA-4.0
tags: avif image, av1 image, avif codec, next-gen image
fetched: 2026-07-02
---

# AVIF

**AV1 Image File Format** (**AVIF** extension/container) is an open, royalty-free file format specification for storing images or image sequences compressed with AV1.

An AVIF file is designed to be a conformant HEIF file for both image items and image sequences. Specifically, this specification follows the recommendations given in "Annex I: Guidelines On Defining New Image Formats and Brands" of HEIF.

This specification reuses syntax and semantics used in the specification for the AV1 Codec ISO Media File Format Binding.

In tests by Netflix in 2020, AVIF showed better compression efficiency than JPEG, as well as better detail preservation, fewer blocking artifacts and less color bleeding around hard edges in composites of natural images, text, and graphics.

AVIF has been supported by all major web browsers since 2024, with over 93% of users worldwide on compatible browsers.

## Features

The AV1 Image File Format supports:

- Multiple color spaces, including:
  - HDR (with PQ or HLG transfer functions and BT.2020 color primaries, as part of BT.2100)
    - Supports HDR gain map approach, backwards compatible with SDR displays, but no encoder is currently available.
  - SDR (with sRGB / BT.709 / BT.601 or with wide color gamut)
  - Color space signaling via CICP (ITU-T H.273 and ISO/IEC 23091-2) or ICC profiles
- Both lossless and lossy compression
- 8-, 10-, and 12-bit color depths
- Monochrome (alpha/depth) or multi-components
- 4:2:0, 4:2:2, 4:4:4 chroma subsampling and RGB
- Film grain synthesis
- Image sequences and animation
- Alpha transparency

## Profiles

AVIF specification defines two image profiles:

- AVIF Baseline Profile
  - Uses AV1 Main Profile
  - AV1 level is 5.1 or lower
    - *Level 5.1 is chosen for the Baseline profile to ensure that no single coded image exceeds 8K resolution, as some decoders may not be able to handle larger images. More precisely, coded image items compliant to the AVIF Baseline profile may not have a total number of pixels greater than 8,912,896, a width greater than 8,192, or a height greater than 4,352. It is still possible to use the Baseline profile to create larger images using grid derivation.*
- AVIF Advanced Profile
  - Uses AV1 High Profile
  - AV1 level is 6.0 or lower
    - *Coded image items compliant to the AVIF Advanced profile may not have a total number of pixels greater than 35,651,584, a width greater than 16,384, or a height greater than 8,704. It is still possible to use the Advanced profile to create larger images using grid derivation.*

## Support

On 14 December 2018, Netflix published the first .avif sample images. In November 2020, HDR sample images with PQ transfer function and BT.2020 color primaries were published.

### Web browsers

- In August 2020, Google Chrome version 85 was released with full AVIF support. Google Chrome 89 for Android adds AVIF support.
- In October 2021, Mozilla Firefox 93 was released with default AVIF support.
- WebKit added AVIF support on 5 March 2021. Safari for iOS 16 and macOS Ventura added support for AVIF; iOS 16 was released on 12 September 2022 and macOS Ventura on 24 October 2022. Safari 16.4 retroactively added AVIF support for macOS Monterey and macOS Big Sur.
- Microsoft Edge added AVIF support in version 121 released in January 2024.

### Image viewers

- FastStone Image Viewer (Version 7.8 onwards)
- XnView
- gThumb
- Eye of GNOME
- Gnome's Loupe
- ImageMagick
- IrfanView (read only)
- Gwenview
- digiKam 7.7.0
- Preview and Photos apps on iOS 16, iPadOS 16 and macOS 13.
- ImageGlass (read+write)

### Media players

- mpv supports AVIF format both as viewer and as encoder, since it is able to export screenshots in such format.
- VLC will read AVIF files starting with version 4, which is still in development.

### Image editors

- Paint.NET added support for opening AVIF files in September 2019, and the ability to save AVIF format images in an August 2020 update.
- GraphicConverter has AVIF support from version 12 and MacOS 10.13 onwards.
- The Colorist format conversion and Darktable RAW image data have each released support for and provide reference implementations of libavif.
- GIMP added native AVIF import and export in October 2020.
- IrfanView 4.57, released on 13 January 2021, added read-only AVIF support via its plugins.
- Krita 5.0, released on 23 December 2021, added AVIF support. The support also includes Rec.2100 HDR AVIF images.
- Adobe Illustrator (May 2022 release) added AVIF support.
- Adobe Photoshop (June 2025 release) added AVIF support (open, edit, save).
- Pixelmator Pro 3.1, released on 2 November 2022, added initial AVIF support.
- Adobe Lightroom 7.0 (October 2023 release) and Lightroom Classic 13 (October 2023 release) added HDR capabilities, including opening and saving photos in AVIF format.
- PhotoLine 24, released 30 June 2023, added AVIF support.
- ACDSee Photo Studio 2025, released September 2024
- Zoner Studio – photo and video editing software
- ezgif.com – allows creating, editing and converting animated AVIF files

### Image libraries

- libavif – portable library for encoding and decoding AVIF files.
- libheif – ISO/IEC 23008-12:2017 HEIF and AVIF decoder and encoder.
- SAIL – format-agnostic library with support of AVIF implemented on top of libavif.
- FFmpeg
- AVIF and HEIC unit – Delphi/Lazarus wrapper for libavif
- JDeli – Java Image library for encoding and decoding AVIF

### Operating systems

- Windows – Microsoft announced support with the Windows 10, version 1903 preview release, including support in File Explorer, Paint, and multiple APIs, together with sample images. Since Windows 11, version 22H2, the AVIF Image Extension is built-in by default installation.
- Android – Android 12, released on 4 October 2021, added native support for AVIF.
- Linux – AVIF is widely supported in Linux distributions. With the release of libavif 0.8.0 in July 2020, which added a GdkPixbuf plugin, AVIF support is present in most GNOME/GTK applications. The KDE Frameworks added support for AVIF to the "KImageFormats" library in January 2021, enabling most KDE/Qt applications to support viewing and saving AVIF images. Nomacs 3.16 adds support for AVIF viewing and conversion. Nomacs appimage is also for older Linux.
- Apple platforms – iOS 16, iPadOS 16 and macOS Ventura natively support AVIF. AVIF images can be directly viewed in the Finder, with QuickLook, in the iOS Files app, etc.

### Websites

- Cloudflare announced AVIF support in a blog post on 3 October 2020.
- Vimeo announced AVIF support in a blog post on 3 June 2021.
- Joomla 5 includes AVIF support.
- WordPress 6.5 added AVIF support.
- Wikimedia Commons does not support in 2024, see the ticket.
- Wikipedia does not support AVIF
- GitHub: no support, see related page
- Gitea 1.23 added AVIF support.

### Programming languages

- Python supports AVIF via Pillow.
- PHP has had AVIF support in its GD extension since PHP version 8.1.
- Perl has support via the Imager library suite

### Others

- ExifTool has supported AVIF format for reading and writing Exif since version 11.79 (released 12 December 2019).
- scrot supports through Imlib2
- Discord has officially supported AVIF since 12 March 2025
- Gamescope, a Wayland compositor, uses AVIF for its screenshots.
- The IIPImage image server has AVIF output support since version 1.3

---
title: "Container format"
source: https://en.wikipedia.org/wiki/Digital_container_format
domain: heif-format
license: CC-BY-SA-4.0
tags: heif container, heic image, hevc still image, apple heif
fetched: 2026-07-02
---

# Container format

(Redirected from

Digital container format

)

A **container format** (informally, sometimes called a **wrapper**) or **metafile** is a file format that allows multiple data streams to be embedded into a single file, usually along with metadata for identifying and further detailing those streams. Notable examples of container formats include archive files (such as the ZIP format) and formats used for multimedia playback (such as Matroska, MP4, and AVI). Among the earliest cross-platform container formats were Distinguished Encoding Rules and the 1985 Interchange File Format.

## Design

Although containers may identify how data or metadata is encoded, they do not actually provide instructions about how to decode that data. A program that can open a container must also use an appropriate codec to decode its contents. If the program doesn't have the required algorithm, it can't use the contained data. In these cases, programs usually emit an error message that complains of a missing codec, which users may be able to acquire.

Container formats can be made to wrap any kind of data. Though there are some examples of such file formats (e.g. Microsoft Windows's DLL files), most container formats are specialized for specific data requirements. For example, since audio and video streams can be coded and decoded with many different algorithms, a container format may be used to provide the appearance of a single file format to users of multimedia playback software.

### Considerations

The differences between various container formats arise from five main issues:

1. Popularity; how widely supported a container is.
2. Overhead. This is the difference in file-size between two files with the same content in a different container.
3. Support for advanced codec functionality. Older formats such as AVI do not support new codec features like B-frames, VBR audio or VFR video natively. The format may be "hacked" to add support, but this creates compatibility problems.
4. Support for advanced content, such as chapters, subtitles, meta-tags, user-data.
5. Support of streaming media.

### Single coding formats

In addition to pure container formats, which specify *only* the wrapper but not the coding, a number of file formats specify *both* a storage layer and the coding, as part of modular design and forward compatibility.

Examples include the JPEG File Interchange Format (JFIF), for containing JPEG data, and Portable Network Graphics (PNG) formats.

In principle, coding can be changed while the storage layer is retained; for example, Multiple-image Network Graphics (MNG) uses the PNG container format but provides animation, while JPEG Network Graphics (JNG) puts JPEG encoded data in a PNG container; in both cases however, the different formats have different magic numbers – the format specifies the coding, though a MNG can contain both PNG-encoded images and JPEG-encoded images.

## Multimedia container formats

The container file is used to identify and interleave different data types. Simpler container formats can contain different types of audio formats, while more advanced container formats can support multiple audio and video streams, subtitles, chapter-information, and meta-data (tags) — along with the synchronization information needed to play back the various streams together. In most cases, the file header, most of the metadata and the synchro chunks are specified by the container format. For example, container formats exist for optimized, low-quality, internet video streaming which differs from high-quality Blu-ray streaming requirements.

Container format parts have various names: "chunks" as in RIFF and PNG, "atoms" in QuickTime/MP4, "packets" in MPEG-TS (from the communications term), and "segments" in JPEG. The main content of a chunk is called the "data" or "payload". Most container formats have chunks in sequence, each with a header, while TIFF instead stores offsets. Modular chunks make it easy to recover other chunks in case of file corruption or dropped frames or bit slip, while offsets result in framing errors in cases of bit slip.

Some containers are exclusive to audio:

- AIFF (IFF file format, widely used on the macOS platform)
- WAV (RIFF file format, widely used on Windows platform)
- XMF (Extensible Music Format)

Other containers are exclusive to still images:

- FITS (Flexible Image Transport System) still images, raw data, and associated metadata.
- TIFF (Tag Image File Format) still images and associated metadata.
- Macintosh PICT resource (PICT), superseded by PDF in Mac OS X
- Windows Metafile (WMF) = (EMF) Enhanced Metafile
- Encapsulated PostScript (EPS)
- Computer Graphics Metafile (CGM)
- Portable Document Format (PDF)
- Corel Draw File (CDR)
- Scalable Vector Graphics (SVG)
- Rich Text Format file (RTF)

Other flexible containers can hold many types of audio and video, as well as other media. The most popular multi-media containers are:

- 3GP (used by many mobile phones; based on the ISO base media file format)
- ASF (container for Microsoft WMA and WMV, which today usually do not use a container)
- AVI (the standard Microsoft Windows container, also based on RIFF)
- DVR-MS ("Microsoft Digital Video Recording", proprietary video container format developed by Microsoft based on ASF)
- Flash Video (FLV, F4V) (container for video and audio from Adobe Systems)
- IFF (first platform-independent container format)
- Matroska (MKV) (not limited to any coding format, as it can hold virtually anything; it is an open standard container format)
- MJ2 - Motion JPEG 2000 file format, based on the ISO base media file format which is defined in MPEG-4 Part 12 and JPEG 2000 Part 12
- QuickTime File Format (standard QuickTime video container from Apple Inc.)
- MPEG program stream (standard container for MPEG-1 and MPEG-2 elementary streams on reasonably reliable media such as disks; used also on DVD-Video discs)
- MPEG-2 transport stream (a.k.a. MPEG-TS) (standard container for digital broadcasting and for transportation over unreliable media; used also on Blu-ray Disc video; typically contains multiple video and audio streams, and an electronic program guide)
- MP4 (standard audio and video container for the MPEG-4 multimedia portfolio, based on the ISO base media file format defined in MPEG-4 Part 12 and JPEG 2000 Part 12) which in turn was based on the QuickTime file format.
- Ogg (standard container for Xiph.org audio formats Vorbis and Opus and video format Theora)
- RM (RealMedia; standard container for RealVideo and RealAudio)
- WebM (subset of Matroska, used for web-based media distribution on online platforms; container for royalty-free audio formats Vorbis/Opus and video formats VP8/VP9/AV1)

There are many other container formats, such as NUT, MXF, GXF, ratDVD, SVI, VOB and DivX Media Format

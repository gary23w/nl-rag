---
title: "3GP and 3G2"
source: https://en.wikipedia.org/wiki/3GP_and_3G2
domain: apple-prores
license: CC-BY-SA-4.0
tags: apple prores
fetched: 2026-07-03
---

# 3GP and 3G2

**3GP** (3GPP file format) is a digital multimedia container format defined by the Third Generation Partnership Project (3GPP) for 3G UMTS multimedia services, largely based on MPEG-4 Part 12. A 3GP container may consist of H.263 or H.264 video codecs or AMR or AAC-LC audio codecs.

**3G2** (3GPP2 file format) is a multimedia container format defined by the 3GPP2 for 3G CDMA2000 multimedia services. It is very similar to the 3GP file format but consumes less space and bandwidth, and has some extensions and limitations in comparison to 3GP.

## Specifications

3GP is defined in the ETSI 3GPP technical specification. 3GP is a required file format for video and associated speech/audio media types and timed text in ETSI 3GPP technical specifications for IP Multimedia Subsystem (IMS), Multimedia Messaging Service (MMS), Multimedia Broadcast/Multicast Service (MBMS) and Transparent end-to-end Packet-switched Streaming Service (PSS).

3G2 is defined in the 3GPP2 technical specification.

## Technical details

The 3GP and 3G2 file formats are both structurally based on the ISO base media file format defined in ISO/IEC 14496-12 – MPEG-4 Part 12, but older versions of the 3GP file format did not use some of its features. 3GP and 3G2 are container formats similar to MPEG-4 Part 14 (MP4), which is also based on MPEG-4 Part 12. The 3GP and 3G2 file format were designed to decrease storage and bandwidth requirements to accommodate mobile phones. They are good for lower end smartphones for faster streaming & download.

3GP and 3G2 are similar standards, but with some differences:

- 3GPP file format was designed for GSM-based phones and may have the filename extension `.3gp`
- 3GPP2 file format was designed for CDMA-based phones and may have the filename extension `.3g2`

Some cell phones use the `.mp4` extension for 3GP video.

### 3GP

The 3GP file format stores video streams as MPEG-4 Part 2, H.263, or MPEG-4 Part 10 (AVC/H.264), and audio streams as AMR-NB, AMR-WB, AMR-WB+, AAC-LC, HE-AAC v1 or Enhanced aacPlus (HE-AAC v2). 3GPP allowed use of AMR and H.263 codecs in the ISO base media file format (MPEG-4 Part 12), because 3GPP specified the usage of the Sample Entry and template fields in the ISO base media file format as well as defining new boxes to which codecs refer. These extensions were registered by the registration authority for code-points in ISO base media file format ("MP4 Family" files).

For the storage of MPEG-4 media specific information in 3GP files, the 3GP specification refers to MP4 and the AVC file format, which are also based on the ISO base media file format. The MP4 and the AVC file format specifications described usage of MPEG-4 content in the ISO base media file format.

A 3GP file is always big-endian, storing and transferring the most significant bytes first.

### 3G2

The 3G2 file format can store the same video streams and most of the audio streams used in the 2007 3GP file format. In addition, 3G2 stores audio streams as EVRC, EVRC-B, EVRC-WB, 13K (QCELP), SMV or VMR-WB, which was specified by 3GPP2 for use in ISO base media file format. The 3G2 specification also defined some enhancements to 3GPP Timed Text. 3G2 file format does not store Enhanced aacPlus (HE-AAC v2) and AMR-WB+ audio streams. For the storage of MPEG-4 media (AAC audio, MPEG-4 Part 2 video, MPEG-4 Part 10 – H.264/AVC) in 3G2 files, the 3G2 specification refers to the MP4 file format and the AVC file format specification, which described usage of this content in the ISO base media file format. For the storage of H.263 and AMR content 3G2 specification refers to the 3GP file format specification.

## Device support

- Most 3G capable mobile phones support the playback and recording of video in 3GP format (memory, maximum filesize for playback and recording, and resolution limits exist and vary).
- Some newer/higher-end phones without 3G capabilities may also playback and record in this format (again, with said limitations).
- Audio imported from CD onto a PlayStation 3 when it is set to encode to the MPEG-4 AAC format copies onto USB devices in the 3GP format.
- The Nintendo 3DS used 3GP technology to play YouTube videos.
- Apple iDevices used to support files for playback only as passthrough files, hence no editing ability, but since iOS 9 this has been deprecated meaning files of this format have to be manually converted to H.264.

## Software support

When transferred to a computer, 3GP movies can be viewed on Microsoft Windows, Apple macOS, and the various Linux-based operating systems; on the former two with Windows Media Player and Apple QuickTime respectively (their built-in media players), and on all three with VLC media player. Programs such as Media Player Classic, K-Multimedia Player, Totem, RealPlayer, MPlayer, and GOM Player can also be used.

3GP and 3G2 files can be encoded and decoded with open source software FFmpeg. Media tags can be read and written on Linux, macOS and Windows using the open source AtomicParsley command-line utility.

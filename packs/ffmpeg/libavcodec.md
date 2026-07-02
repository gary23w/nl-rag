---
title: "libavcodec"
source: https://en.wikipedia.org/wiki/Libavcodec
domain: ffmpeg
license: CC-BY-SA-4.0
tags: ffmpeg tool, libavcodec, video transcoding, media conversion
fetched: 2026-07-02
---

# libavcodec

**libavcodec** is a free and open-source library of codecs for encoding and decoding video and audio data.

libavcodec is an integral part of many open-source multimedia applications and frameworks. The popular MPV, xine and VLC media players use it as their main, built-in decoding engine that enables playback of many audio and video formats on all supported platforms. It is also used by the ffdshow tryouts decoder as its primary decoding library. libavcodec is also used in video editing and transcoding applications like Avidemux, MEncoder or Kdenlive for both decoding and encoding.

libavcodec contains decoder and sometimes encoder implementations of several proprietary formats, including ones for which no public specification has been released. As such, a significant reverse engineering effort is part of libavcodec development. Having such codecs available within the standard libavcodec framework gives a number of benefits over using the original codecs, most notably increased portability, and in some cases also better performance, since libavcodec contains a standard library of highly optimized implementations of common building blocks, such as DCT and color space conversion. However, while libavcodec does strive to achieve decoding that is bit-exact to their official format implementations, occasional bugs and missing features in such re-implementations can sometimes introduce playback compatibility problems for certain files.

## Implemented video codecs

libavcodec includes video decoders and/or encoders for the following formats, this list is not exhaustive:

- Animated GIF
- Asus video format v1 and v2
- AVS (decoding only, encoding through libxavs)
- AV1
- Bink Video/Audio (decoding only, version 2 not supported)
- CamStudio format (decoding only)
- CineForm (decoding only)
- Cinepak
- Creative YUV (CYUV, decoding only)
- Dirac
- DNxHD
- Duck Corporation Truemotion 1, 2, and RT codecs (decoding only)
- FFV1
- Flash Screen Video v1 and v2
- H.261
- H.262/MPEG-2 Part 2
- H.263
- H.264/MPEG-4 AVC (native decoder, encoding through x264 and hardware encoding)
- H.265 HEVC (native decoder, encoding through x265 and hardware encoding)
- Huffyuv
- id Software RoQ Video
- Indeo (decoding only)
- Lagarith (decoding only)
- MJPEG
- MPEG-1
- MPEG-4 Part 2 (the format used for example by the popular DivX and Xvid codecs)
- Apple ProRes
- QuickDraw (decoding only)
- QuickTime: Graphics (decoding only), Video (decoding only) and Animation (RLE)
- RealVideo RV10 and RV20
- RealVideo RV30 and RV40 (decoding only)
- SheerVideo (decoding only)
- Smacker video (decoding only)
- Snow
- Sorenson Spark under the name FLV1
- SVQ1
- SVQ3 (decoding only)
- Theora (native decoder, encoding through libtheora)
- TrueMotion v1 and v2 (decoding only)
- VC-1 (decoding only)
- Sierra VMD Video (decoding only)
- VMware VMnc (decoding only)
- VP3 (decoding only)
- VP5 (decoding only)
- VP6 (decoding only)
- VP7 (decoding only)
- VP8 (native decoder, encoding through libvpx)
- VP9 (native decoder, encoding through libvpx)
- VQA (decoding only)
- VVC (native decoder)
- WMV version 7 and 8
- WMV version 9 (decoding only)
- Windows Media Video Image (decoding only)
- Windows Media Video Screen 1 and 2 (decoding only)
- Wing Commander/Xan Video (decoding only)

## Implemented audio codecs

libavcodec includes decoders and encoders for the following formats:

- 8SVX (decoding only)
- AAC
- AC-3
- AMR (decoding only)
- AMR-WB (decoding only)
- Apple Lossless
- ATRAC1, ATRAC3, ATRAC3plus and ATRAC9 (decoding only)
- Codec 2
- Cook Codec (decoding only)
- DTS (encoder is highly experimental)
- EA ADPCM (decoding only)
- E-AC-3
- EVRC (decoding only)
- FLAC
- G.711 (μ-law and A-law)
- G.722
- G.723.1
- G.726
- G.729 (decoding only)
- GSM 06.10 (native decoder, encoding through libgsm)
- Intel Music Coder and Indeo Audio Coder (decoding only)
- Meridian Lossless Packing / Dolby TrueHD
- Monkey's Audio (decoding only)
- MP1 (decoding only)
- MP2
- MP3 (native decoder, encoding through LAME)
- Nellymoser Asao Codec in Flash
- Opus (native encoder and decoder, encoding through libopus)
- QCELP (decoding only)
- QDM2 (decoding only)
- RealAudio 1.0
- RealAudio 2.0 (decoding only)
- Shorten (decoding only)
- Truespeech (decoding only)
- TTA
- TwinVQ (decoding only)
- Vorbis
- WAV
- WavPack
- Windows Media Audio 1 and 2
- Windows Media Audio 9 Lossless (decoding only)
- Windows Media Audio 9 Professional (decoding only)
- Windows Media Audio Voice (decoding only)

## Legal aspects

Libavcodec contains more than 100 codecs, most of which do not just store uncompressed data. Most codecs that compress information could be claimed by patent holders. Such claims may be enforceable in countries like the United States which have implemented software patents, but are considered unenforceable or void in countries that have not implemented software patents.

Furthermore, many of these codecs are only released under terms that forbid reverse engineering, even for purposes of interoperability. These terms of use are forbidden in certain countries. For example, some European Union nations have not implemented software patents and have laws expressly allowing reverse engineering for purposes of interoperability.

## Libraries that depend on libavcodec

- libavformat (part of FFmpeg)
- libgegl (optional part of GEGL)
  - libgimp (part of GIMP)
- libmpcodecs (part of MPlayer)
  - libmpdemux (part of MPlayer)

## Applications using libavcodec

### Video players

- FFplay
- MPlayer
- mpv
- MPC-HC and MPC-BE
- VLC
- xine

### Audio players

- Audacious (Uses in audacious-plugins's ffaudio)
- Rockbox (Includes only FLAC code)
- XMMS2

### Multimedia players

- Gnash
- Moonlight
- swfdec

### Video editors

- Avidemux
- Cinelerra
- Kdenlive
- Kino

### Audio editors

- Audacity (since 1.3.6)
- SoX (optional)

### Video converters

- FFmpeg
- HandBrake
- MEncoder
- SUPER

### Video libraries

- GPAC
- Media Lovin' Toolkit

### Optical disc authoring

- K3b

### Graphics libraries

- GEGL
- ImageMagick

### 3D graphics editors

- Blender

### VoIP

- Ekiga
- QuteCom
- Linphone

### Multimedia streaming server

- FFserver
- VLC media player

### Multimedia frameworks

- ffdshow (wraps libavcodec as a DirectShow filter and adds postprocessing to improve image quality; once installed, it is automatically used by all Windows DirectShow video players, such as Windows Media Player, Media Player Classic, Winamp etc. It also wraps libavcodec as a Video for Windows filter; the framework used by most video editing software.)
- LAV Filters
- GStreamer via the GStreamer FFmpeg plugin
- Perian
- Bellagio OpenMAX Integration Layer – open-source OpenMAX IL API implementation

### Computer vision libraries

- OpenCV

### Browser

- Google Chrome
- Mozilla Firefox

### Media center

- MythTV
- Plex
- Kodi (formerly XBMC)

### Screen capture

- xvidcap

### Device utilities

- BitPim – utilities for CDMA phones

### CCTV

- ZoneMinder – video camera security suite
- Motion – video camera security/monitoring program

### Games

- Performous – music game including singing, band and dance.
- StepMania
- Ultrastar
- osu!

### Others

- CorePlayer
- FreeJ
- Ingex Studio – used by BBC
- PulseAudio – includes only resamplers code
- Steam digital distribution service

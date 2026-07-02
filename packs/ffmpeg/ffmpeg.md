---
title: "FFmpeg"
source: https://en.wikipedia.org/wiki/FFmpeg
domain: ffmpeg
license: CC-BY-SA-4.0
tags: ffmpeg tool, libavcodec, video transcoding, media conversion
fetched: 2026-07-02
---

# FFmpeg

**FFmpeg** is a free and open-source software project consisting of a suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the command-line `ffmpeg` tool itself, designed for processing video and audio files. It is widely used for format transcoding, basic editing (trimming and concatenation), video scaling, video post-production effects, and standards compliance (SMPTE, ITU).

FFmpeg also includes other tools: `ffplay`, a simple media player, and `ffprobe`, a command-line tool to display media information. Among included libraries are libavcodec, an audio/video codec library used by many commercial and free software products, **libavformat** (Lavf), an audio/video container mux and demux library, and libavfilter, a library for enhancing and editing filters through a GStreamer-like filtergraph.

FFmpeg is part of the workflow of many other software projects, and its libraries are a core part of software media players such as VLC, and has been included in core processing for YouTube and Bilibili. Encoders and decoders for many audio and video file formats are included, making it highly useful for the transcoding of common and uncommon media files.

FFmpeg is published under the LGPL-2.1-or-later or GPL-2.0-or-later, depending on which options are enabled.

## Project history

The project was started by Fabrice Bellard (using the pseudonym "Gérard Lantau") in 2000, and was led by Michael Niedermayer from 2004 until 2015. Some FFmpeg developers were also part of the MPlayer project.

The "FF" in FFmpeg stands for "fast forward." The logo represents a zigzag scan pattern that shows how MPEG video codecs handle entropy encoding.

On March 13, 2011, a group of FFmpeg developers decided to fork the project under the name Libav. The group decided to fork the project due to a disagreement with the leadership of FFmpeg. Libav was declared abandoned in 2020.

On January 10, 2014, two Google employees announced that over 1000 bugs had been fixed in FFmpeg during the previous two years by means of fuzz testing.

In January 2018, the *ffserver* command-line program – a long-time component of FFmpeg – was removed. The developers had previously deprecated the program citing high maintenance efforts due to its use of internal application programming interfaces.

In April 2026, Anthropic's Claude Mythos Preview found a 16-year-old critical vulnerability in FFmpeg codec H.264.

The project publishes a new release every three months on average. While release versions are available from the website for download, FFmpeg developers recommend that users compile the software from source using the latest build from their source code, using the Git version control system.

## Codec development

Two video coding formats with corresponding codecs and one container format have been created within the FFmpeg project so far. The two video codecs are the lossless FFV1, and the lossless and lossy Snow codec. Development of Snow has stalled, while its bit-stream format has not been finalized yet, making it experimental since 2011. The multimedia container format called NUT is no longer being actively developed, but still maintained.

In summer 2010, FFmpeg developers Fiona Glaser, Ronald Bultje, and David Conrad, announced the ffvp8 decoder. Through testing, they determined that ffvp8 was faster than Google's own libvpx decoder. Starting with version 0.6, FFmpeg also supported WebM and VP8.

In October 2013, a native VP9 decoder and OpenHEVC, an open source High Efficiency Video Coding (HEVC) decoder, were added to FFmpeg. In 2016 the native AAC encoder was considered stable, removing support for the two external AAC encoders from VisualOn and FAAC. FFmpeg 3.0 (nicknamed *"Einstein"*) retained build support for the Fraunhofer FDK AAC encoder. Since version 3.4 *"Cantor"* FFmpeg supported the FITS image format. Since November 2018 in version 4.1 *"al-Khwarizmi"* AV1 can be muxed in MP4 and Matroska, including WebM.

## Components

### Command-line tools

- *ffmpeg* is a command-line tool that converts audio or video formats. It can also capture and encode in real-time from various hardware and software sources such as a TV capture card.
- *ffplay* is a simple media player utilizing SDL and the FFmpeg libraries.
- *ffprobe* is a command-line tool to display media information (text, CSV, XML, JSON), see also MediaInfo.

### Libraries

- *libswresample* is a library containing audio resampling routines.
- *libavcodec* is a library containing all of the native FFmpeg audio/video encoders and decoders. Most codecs were developed from scratch to ensure best performance and high code reusability.
- *libavformat* (Lavf) is a library containing demuxers and muxers for audio/video container formats.
- *libavutil* is a helper library containing routines common to different parts of FFmpeg. This library includes hash functions, ciphers, LZO decompressor and Base64 encoder/decoder.
- *libswscale* is a library containing video image scaling and colorspace/pixelformat conversion routines.
- *libavfilter* is the substitute for vhook which allows the video/audio to be modified or examined (for debugging) between the decoder and the encoder. Filters have been ported from many projects including MPlayer and avisynth.
- *libavdevice* is a library containing audio/video io through internal and external devices.

## Supported hardware

### CPUs

FFmpeg encompasses software implementations of video and audio compressing and decompressing algorithms. These can be compiled and run on many different instruction sets, including x86 (IA-32 and x86-64), PPC (PowerPC), ARM, DEC Alpha, SPARC, and MIPS.

### Special purpose hardware

There are a variety of application-specific integrated circuits (ASICs) for audio/video compression and decompression. These ASICs can partially or completely offload the computation from the host CPU. Instead of a complete implementation of an algorithm, only the API is required to use such an ASIC.

| Firm | ASIC | purpose | supported by FFmpeg | Details |
|---|---|---|---|---|
| AMD | UVD | decoding | (Yes) | via VDPAU API and VAAPI |
| VCE | encoding | (Yes) | via VAAPI, considered experimental |   |
| Amlogic | Amlogic Video Engine | decoding | ? |   |
| BlackMagic | DeckLink | encoding/decoding | (Yes) | real-time ingest and playout |
| Broadcom | Crystal HD | decoding | (Yes) |   |
| Samsung | Exynos MFC | decoding | (Yes) |   |
| Qualcomm | Hexagon | encoding/decoding | (Yes) | hwaccel |
| Intel | Intel Clear Video | decoding | (Yes) | (libmfx, VAAPI) |
| Intel Quick Sync Video | encoding/decoding | (Yes) | (libmfx, VAAPI) |   |
| Nvidia | PureVideo / NVDEC | decoding | (Yes) | via the VDPAU API as of FFmpeg v1.2 (deprecated) via CUVID API as of FFmpeg v3.1 |
| NVENC | encoding | (Yes) | as of FFmpeg v2.6 |   |

The following APIs are also supported: DirectX Video Acceleration (DXVA2, Windows), Direct3D 11 (D3D11VA, Windows), Media Foundation (Windows), Vulkan (VKVA), VideoToolbox (iOS, iPadOS, macOS), RockChip MPP, OpenCL, OpenMAX, MMAL (Raspberry Pi), MediaCodec (Android OS), V4L2 (Linux). Depending on the environment, these APIs may lead to specific ASICs, to GPGPU routines, or to SIMD CPU code.

## Supported codecs and formats

### Image formats

FFmpeg supports many common and some uncommon image formats.

The **PGMYUV** image format is a homebrew variant of the binary (P5) PGM Netpbm format. FFmpeg also supports 16-bit depths of the PGM and PPM formats, and the binary (P7) PAM format with or without alpha channel, depth 8 bit or 16 bit for `pix_fmts` *monob, gray, gray16be, rgb24, rgb48be, ya8, rgba, rgb64be*.

### Supported formats

In addition to FFV1 and Snow formats, which were created and developed from within FFmpeg, the project also supports the following formats:

| Group | Format type | Format name |
|---|---|---|
| ISO/IEC/ITU-T | Video | MPEG-1 Part 2, H.261 (Px64), H.262/MPEG-2 Part 2, H.263, MPEG-4 Part 2, H.264/MPEG-4 AVC, HEVC/H.265 (MPEG-H Part 2), MPEG-4 VCB (a.k.a. VP8), Motion JPEG, IEC DV video and CD+G |
| Audio | MP1, MP2, MP3, AAC, HE-AAC, MPEG-4 ALS, G.711 μ-law, G.711 A-law, G.721 (a.k.a. G.726 32k), G.722, G.722.2 (a.k.a. AMR-WB), G.723 (a.k.a. G.726 24k and 40k), G.723.1, G.726, G.729, G.729D, IEC DV audio and Direct Stream Transfer |   |
| Subtitle | MPEG-4 Timed Text (a.k.a. 3GPP Timed Text) |   |
| Image | JPEG, Lossless JPEG, JPEG-LS, JPEG 2000, JPEG XL, PNG, CCITT G3 and CCITT G4 |   |
| Alliance for Open Media | Video | AV1 |
| Image | AVIF |   |
| EIA | Subtitle | EIA-608 |
| CEA | Subtitle | CEA-708 |
| SMPTE | Video | SMPTE 314M (a.k.a. DVCAM and DVCPRO), SMPTE 370M (a.k.a. DVCPRO HD), VC-1 (a.k.a. WMV3), VC-2 (a.k.a. Dirac Pro), VC-3 (a.k.a. AVID DNxHD) |
| Audio | SMPTE 302M |   |
| Image | DPX |   |
| ATSC/ETSI/DVB | Audio | Full Rate (GSM 06.10), AC-3 (Dolby Digital), Enhanced AC-3 (Dolby Digital Plus) and DTS Coherent Acoustics (a.k.a. DTS or DCA) |
| Subtitle | DVB Subtitling (ETSI 300 743) |   |
| DVD Forum/Dolby | Audio | MLP / Dolby TrueHD |
| Subtitle | DVD-Video subtitles |   |
| Xperi/DTS, Inc/QDesign | Audio | DTS Coherent Acoustics (a.k.a. DTS or DCA), DTS Extended Surround (a.k.a. DTS-ES), DTS 96/24, DTS-HD High Resolution Audio, DTS Express (a.k.a. DTS-HD LBR), DTS-HD Master Audio, QDesign Music Codec 1 and 2 |
| Blu-ray Disc Association | Subtitle | PGS (Presentation Graphics Stream) |
| 3GPP | Audio | AMR-NB, AMR-WB (a.k.a. G.722.2) |
| 3GPP2 | Audio | QCELP-8 (a.k.a. SmartRate or IS-96C), QCELP-13 (a.k.a. PureVoice or IS-733) and Enhanced Variable Rate Codec (EVRC. a.k.a. IS-127) |
| World Wide Web Consortium | Video | Animated GIF |
| Subtitle | WebVTT |   |
| Image | GIF, and SVG (via librsvg) |   |
| IETF | Video | FFV1 |
| Audio | iLBC (via libilbc), Opus and Comfort noise |   |
| International Voice Association | Audio | DSS-SP |
| SAC | Video | AVS video, AVS2 video (via libdavs2), and AVS3 video (via libuavs3d) |
| Microsoft | Video | Microsoft RLE, Microsoft Video 1, Cinepak, Microsoft MPEG-4 v1, v2 and v3, Windows Media Video (WMV1, WMV2, WMV3/VC-1), WMV Screen and Mimic codec |
| Audio | Windows Media Audio (WMA1, WMA2, WMA Pro and WMA Lossless), XMA (XMA1 and XMA2), MSN Siren, MS-GSM and MS-ADPCM |   |
| Subtitle | SAMI |   |
| Image | Windows Bitmap, WMV Image (WMV9 Image and WMV9 Image v2), DirectDraw Surface, and MSP |   |
| Interactive Multimedia Association | Audio | IMA ADPCM |
| Intel / Digital Video Interactive | Video | RTV 2.1 (Indeo 2), Indeo 3, 4 and 5, and Intel H.263 |
| Audio | DVI4 (a.k.a. IMA DVI ADPCM), Intel Music Coder, and Indeo Audio Coder |   |
| RealNetworks | Video | RealVideo Fractal Codec (a.k.a. Iterated Systems ClearVideo), 1, 2, 3 and 4 |
| Audio | RealAudio v1 – v10, and RealAudio Lossless |   |
| Subtitle | RealText |   |
| Apple / Spruce Technologies | Video | Cinepak (Apple Compact Video), ProRes, Sorenson 3 Codec, QuickTime Animation (Apple Animation), QuickTime Graphics (Apple Graphics), Apple Video, Apple Intermediate Codec and Pixlet |
| Audio | ALAC |   |
| Image | QuickDraw PICT |   |
| Subtitle | Spruce subtitle (STL) |   |
| Adobe Flash Player (SWF) | Video | Screen video, Screen video 2, Sorenson Spark and VP6 |
| Audio | Adobe SWF ADPCM and Nellymoser Asao |   |
| Adobe / Aldus | Image | TIFF, PSD, and DNG |
| Xiph.Org | Video | Theora |
| Audio | Speex, Vorbis, Opus and FLAC |   |
| Subtitle | Ogg Writ |   |
| Sony | Audio | Adaptive Transform Acoustic Coding (ATRAC1, ATRAC3, ATRAC3Plus, and ATRAC9) and PSX ADPCM |
| NTT | Audio | TwinVQ |
| Google / On2 / GIPS | Video | Duck TrueMotion 1, Duck TrueMotion 2, Duck TrueMotion 2.0 Real Time, VP3, VP4, VP5, VP6, VP7, VP8, VP9 and animated WebP |
| Audio | DK ADPCM Audio 3/4, On2 AVC and iLBC (via libilbc) |   |
| Image | WebP |   |
| Epic Games / RAD Game Tools | Video | Smacker video and Bink video |
| Audio | Bink audio |   |
| CRI Middleware | Audio | ADX ADPCM, and HCA |
| Nintendo / NERD | Video | Mobiclip video |
| Audio | GCADPCM (a.k.a. ADPCM THP), FastAudio, and ADPCM IMA MOFLEX |   |
| Synaptics / DSP Group | Audio | Truespeech |
| Electronic Arts / Criterion Games / Black Box Games / Westwood Studios | Video | RenderWare TXD, Madcow, CMV, TGV, TGQ, TQI, Midivid VQ (MVDV), MidiVid 3.0 (MV30), Midivid Archival (MVHA), and Vector Quantized Animation (VQA) |
| Audio | Electronic Arts ADPCM variants |   |
| Netpbm | Image | PBM, PGM, PPM, PNM, PAM, PFM and PHM |
| MIT/X Consortium/The Open Group | Image | XBM, XPM and xwd |
| HPE / SGI / Silicon Graphics | Video | Silicon Graphics RLE 8-bit video, Silicon Graphics MVC1/2 |
| Image | Silicon Graphics Image |   |
| Oracle/Sun Microsystems | Image | Sun Raster |
| IBM | Video | IBM UltiMotion |
| Avid Technology / Truevision | Video | Avid 1:1x, Avid Meridien, Avid DNxHD, Avid DNx444, and DNxHR |
| Image | Targa |   |
| Autodesk / Alias | Video | Autodesk Animator Studio Codec and FLIC |
| Image | Alias PIX |   |
| Activision Blizzard / Activision / Infocom | Audio | ADPCM Zork |
| Konami / Hudson Soft | Video | HVQM4 Video |
| Audio | Konami MTAF, and ADPCM IMA HVQM4 |   |
| Grass Valley / Canopus | Video | HQ, HQA, HQX and Lossless |
| Vizrt / NewTek | Video | SpeedHQ |
| Image | Vizrt Binary Image |   |
| Academy Software Foundation / ILM | Image | OpenEXR |
| Mozilla Corporation | Video | APNG |
| Matrox | Video | Matrox Uncompressed SD (M101) / HD (M102) |
| AMD/ATI | Video | ATI VCR1/VCR2 |
| Asus | Video | ASUS V1/V2 codec |
| Commodore | Video | CDXL codec |
| Kodak | Image | Photo CD |
| Blackmagic Design / Cintel | Image | Cintel RAW |
| Houghton Mifflin Harcourt / The Learning Company / ZSoft Corporation | Image | PCX |
| Australian National University | Image | X-Face |
| Bluetooth Special Interest Group | Audio | SBC, and mSBC |
| Qualcomm / CSR | Audio | QCELP, aptX, and aptX HD |
| Open Mobile Alliance / WAP Forum | Image | Wireless Bitmap |

### Muxers

Output formats (container formats and other ways of creating output streams) in FFmpeg are called "muxers". FFmpeg supports, among others, the following:

- AIFF
- ASF
- AVI and also input from AviSynth
- BFI
- CAF
- FLV
- GIF
- GXF, General eXchange Format, SMPTE 360M
- HLS, HTTP Live Streaming
- IFF
- ISO base media file format (including QuickTime, 3GP and MP4)
- Matroska (including WebM)
- Maxis XA
- MPEG-DASH
- MPEG program stream
- MPEG transport stream (including AVCHD)
- MXF, Material eXchange Format, SMPTE 377M
- MSN Webcam stream
- NUT
- Ogg
- OMA
- RL2
- Segment, for creating segmented video streams
- Smooth Streaming
- TXD
- WTV

### Pixel formats

| Type | Color | Packed | Planar | Palette |   |   |   |
|---|---|---|---|---|---|---|---|
| Without alpha | With alpha | Without alpha | With alpha | Chroma-interleaved | With alpha |   |   |
| Monochrome | Binary (1-bit monochrome) | monoblack, monowhite | — | — | — | — | — |
| Grayscale | 8/9/10/12/14/16bpp | — | — | 16/32bpp | — | — |   |
| RGB | RGB 1:2:1 (4-bit color) | 4bpp | — | — | — | — | — |
| RGB 3:3:2 (8-bit color) | 8bpp | — | — | — | — | — |   |
| RGB 5:5:5 (High color) | 16bpp | — | — | — | — | — |   |
| RGB 5:6:5 (High color) | 16bpp | — | — | — | — | — |   |
| RGB/BGR | 24/30/48bpp | 32/64bpp | — | — | — | 8bit->32bpp |   |
| GBR | — | — | 8/9/10/12/14/16bpc | 8/10/12/16bpc | — | — |   |
| RGB Float | RGB | 32bpc | 16/32bpc | — | — | — | — |
| GBR | — | — | 32bpc | 32bpc | — | — |   |
| YUV | YVU 4:1:0 | — | — | (9bpp (YVU9)) | — | — | — |
| YUV 4:1:0 | — | — | 9bpp | — | — | — |   |
| YUV 4:1:1 | 8bpc (UYYVYY) | — | 8bpc | — | (8bpc (NV11)) | — |   |
| YVU 4:2:0 | — | — | (8bpc (YV12)) | — | 8 (NV21) | — |   |
| YUV 4:2:0 | — | — | 8/9/10/12/14/16bpc | 8/9/10/16bpc | 8 (NV12)/10 (P010)/12 (P012)/16bpc (P016) | — |   |
| YVU 4:2:2 | — | — | (8bpc (YV16)) | — | (8bpc (NV61)) | — |   |
| YUV 4:2:2 | 8 (YUYV and UYVY)/10 (Y210)/12bpc (Y212) | — | 8/9/10/12/14/16bpc | 8/9/10/12/16bpc | 8 (NV16)/10 (NV20 and P210)/16bpc (P216) | — |   |
| YUV 4:4:0 | — | — | 8/10/12bpc | — | — | — |   |
| YVU 4:4:4 | — | — | (8bpc (YV24)) | — | 8bpc (NV42) | — |   |
| YUV 4:4:4 | 8 (VUYX)/10/12bpc | 8 / 16bpc (AYUV64) | 8/9/10/12/14/16bpc | 8/9/10/12/16bpc | 8 (NV24)/10 (P410)/ 16bpc (P416) | — |   |
| XYZ | XYZ 4:4:4 | 12bpc | — | — | — | — | — |
| Bayer | BGGR/RGGB/GBRG/GRBG | 8/16bpp | — | — | — | — | — |

1. 10-bit color components with 2-bit padding (X2RGB10)
2. RGBx (rgb0) and xBGR (0bgr) are also supported
3. used in YUV-centric codecs such like H.264
4. YVU9, YV12, YV16, and YV24 are supported as *rawvideo* codec in FFmpeg.
5. I420 a.k.a. YUV420P
6. aka YUY2 in Windows
7. UYVY 10bpc without a padding is supported as *bitpacked* codec in FFmpeg. UYVY 10bpc with 2-bits padding is supported as *v210* codec in FFmpeg. 16bpc (Y216) is supported as *targa_y216* codec in FFmpeg.
8. I422 a.k.a. YUV422P
9. XV30 a.k.a. XVYU2101010
10. XV36
11. VUYA a.k.a. AYUV
12. 10bpc (Y410), 12bpc (Y412), and Y416 (16bpc) are not supported.
13. I444 a.k.a. YUV444P
14. used in JPEG2000

FFmpeg does not support IMC1-IMC4, AI44, CYMK, RGBE, Log RGB and other formats. It also does not yet support ARGB 1:5:5:5, 2:10:10:10, or other BMP bitfield formats that are not commonly used.

## Supported protocols

### Open standards

- IETF RFCs:
  - FTP
  - Gopher
  - HLS
  - HTTP
  - HTTPS
  - RTP
  - RTSP
  - SCTP
  - SDP
  - SRTP
  - TCP
  - TLS
  - UDP
  - UDP-Lite
- IETF I-Ds:
  - SFTP (via libssh)
- Microsoft OSP:
  - CIFS/SMB (via libsmbclient)
  - MMS over TCP (MS-MMSP)
  - MMS over HTTP (MS-WMSP)
- CENELEC
  - SAT>IP
- OASIS standards:
  - AMQP 0-9-1 (via librabbitmq)
- SRT Alliance standard:
  - SRT (via libsrt)

### De facto standards

- RTSP over TLS
- Icecast protocol
- Adobe RTMP, RTMPT, RTMPE, RTMPTE and RTMPS
- RealMedia RTSP/RDT
- ZeroMQ (via libzmq)
- RIST (librist)

## Supported filters

FFmpeg supports, among others, the following filters.

### Audio

- Resampling (aresample)
- Pass/Stop filters
  - Low-pass filter (lowpass)
  - High-pass filter (highpass)
  - All-pass filter (allpass)
  - Butterworth Band-pass filter (bandpass)
  - Butterworth Band-stop filter (bandreject)
- Arbitrary Finite Impulse Response Filter (afir)
- Arbitrary Infinite Impulse Response Filter (aiir)
- Equalizer
  - Peak Equalizer (equalizer)
  - Butterworth/Chebyshev Type I/Type II Multiband Equalizer (anequalizer)
  - Low Shelving filter (bass)
  - High Shelving filter (treble)
  - Xbox 360 equalizer
  - FIR equalizer (firequalizer)
  - Biquad filter (biquad)
- Remove/Add DC offset (dcshift)
- Expression evaluation
  - Time domain expression evaluation (aeval)
  - Frequency domain expression evaluation (afftfilt)
- Dynamics
  - Limiter (alimiter)
  - Compressor (acompressor)
  - Dynamic range expander (crystalizer)
  - Side-chain Compressor (sidechaincompress)
  - Compander (compand)
  - Noise gate (agate)
  - Side-chain Noise gate(sidechaingate)
- Distortion
  - Bitcrusher (acrusher)
- Emphasis (aemphasis)
- Amplify/Normalizer
  - Volume (volume)
  - Dynamic Audio Normalizer (dynaudnorm)
  - EBU R 128 loudness normalizer (loudnorm)
- Modulation
  - Sinusoidal Amplitude Modulation (tremolo)
  - Sinusoidal Phase Modulation (vibrato)
  - Phaser (aphaser)
  - Chorus (chorus)
  - Flanger (flanger)
  - Pulsator (apulsator)
- Echo/Reverb
  - Echo (aecho)
- Routing/Panning
  - Stereo widening (stereowiden)
  - Increase channel differences (extrastereo)
  - M/S to L/R (stereotools)
  - Channel mapping (channelmap)
  - Channel splitting (channelsplit)
  - Channel panning (pan)
  - Channel merging (amerge)
  - Channel joining (join)
  - for Headphones
    - Stereo to Binaural (earwax, ported from SoX)
    - Bauer Stereo to Binaural (bs2b, via libbs2b)
    - Crossfeed (crossfeed)
    - Multi-channel to Binaural (sofalizer, requires libnetcdf)
  - Delay
    - Delay (adelay)
    - Delay by distance (compensationdelay)
- Fade
  - Fader (afade)
  - Crossfader (acrossfade)
- Audio time stretching and pitch scaling
  - Time stretching (atempo)
  - Time-stretching and Pitch-shifting (rubberband, via librubberband)
- Editing
  - Trim (atrim)
  - Silence-padding (apad)
  - Silence remover (silenceremove)
- Show frame/channel information
  - Show frame information (ashowinfo)
  - Show channel information (astats)
  - Show silence ranges (silencedetect)
  - Show audio volumes (volumedetect)
  - ReplayGain scanner (replaygain)
- Modify frame/channel information
  - Set output format (aformat)
  - Set number of sample (asetnsamples)
  - Set sampling rate (asetrate)
- Mixer (amix)
- Synchronization (asyncts)
- HDCD data decoder (hdcd)
- Plugins
  - LADSPA (ladspa)
  - LV2 (lv2)
- Do nothing (anull)

### Video

- Transformations
  - Cropping (crop, cropdetect)
  - Fading (fade)
  - Scaling (scale)
  - Padding (pad)
  - Rotation (rotate)
  - Transposition (transpose)
  - Others:
    - Lens correction (lenscorrection)
    - OpenCV filtering (ocv)
    - Perspective correction (perspective)
- Temporal editing
  - Framerate (fps, framerate)
  - Looping (loop)
  - Trimming (trim)
- Deinterlacing (bwdif, idet, kerndeint, nnedi, yadif, w3fdif)
- Inverse Telecine
- Filtering
  - Blurring (boxblur, gblur, avgblur, sab, smartblur)
  - Convolution filters
    - Convolution (convolution)
    - Edge detection (edgedetect)
    - Sobel Filter (sobel)
    - Prewitt Filter (prewitt)
    - Unsharp masking (unsharp)
- Denoising (atadenoise, bitplanenoise, dctdnoiz, owdenoise, removegrain)
- Logo removal (delogo, removelogo)
- Subtitles (ASS, subtitles)
- Alpha channel editing (alphaextract, alphamerge)
- Keying (chromakey, colorkey, lumakey)
- Frame detection
  - Black frame detection (blackdetect, blackframe)
  - Thumbnail selection (thumbnail)
- Frame Blending (blend, tblend, overlay)
- Video stabilization (vidstabdetect, vidstabtransform)
- Color and Level adjustments
  - Balance and levels (colorbalance, colorlevels)
  - Channel mixing (colorchannelmixer)
  - Color space (colorspace)
  - Parametric adjustments (curves, eq)
- Histograms and visualization
  - CIE Scope (ciescope)
  - Vectorscope (vectorscope)
  - Waveform monitor (waveform)
  - Color histogram (histogram)
- Drawing
- OCR
- Quality measures
  - SSIM (ssim)
  - PSNR (psnr)
- Lookup Tables
  - lut, lutrgb, lutyuv, lut2, lut3d, haldclut

#### Supported test patterns

- SMPTE color bars (smptebars and smptehdbars)
- EBU color bars (pal75bars and pal100bars)

#### Supported LUT formats

- cineSpace LUT format
- Iridas Cube
- Adobe After Effects 3dl
- DaVinci Resolve dat
- Pandora m3d

## Supported media and interfaces

FFmpeg supports the following devices via external libraries.

### Media

- Compact disc (via libcdio; input only)

### Physical interfaces

- IEEE 1394 (a.k.a. FireWire; via libdc1394 and libraw1394; input only)
- IEC 61883 (via libiec61883; input only)
- DeckLink
- Brooktree video capture chip (via bktr driver; input only)

### Audio IO

- Advanced Linux Sound Architecture (ALSA)
- Open Sound System (OSS)
- PulseAudio
- JACK Audio Connection Kit (JACK; input only)
- OpenAL (input only)
- sndio
- Core Audio (for macOS)
  - AVFoundation (input only)
  - AudioToolbox (output only)

### Video IO

- Video4Linux2
- Video for Windows (input only)
- Windows DirectShow
- Android Camera (input only)

### Screen capture and output

- Simple DirectMedia Layer 2 (output only)
- OpenGL (output only)
- Linux framebuffer (fbdev)
- Graphics Device Interface (GDI; input only)
- X Window System (X11; via XCB; input only)
- X video extension (XV; via Xlib; output only)
- Kernel Mode Setting (via libdrm; input only)

### Others

- ASCII art (via libcaca; output only)

## Applications

### Legal aspects

FFmpeg contains more than 100 codecs, most of which use compression techniques of one kind or another. Many such compression techniques may be subject to legal claims relating to software patents. Such claims may be enforceable in countries like the United States which have implemented software patents, but are considered unenforceable or void in member countries of the European Union, for example. Patents for many older codecs, including AC3 and all MPEG-1 and MPEG-2 codecs, have expired.

FFmpeg is licensed under the LGPL license, but if a particular build of FFmpeg is linked against any GPL libraries (notably x264), then the entire binary is licensed under the GPL.

### Projects using FFmpeg

FFmpeg is used by software such as Blender, Cinelerra-GG Infinity, HandBrake, Kodi, MPC-HC, Plex, Shotcut, VirtualDub2 (a VirtualDub fork), VLC media player, xine and YouTube. It handles video and audio playback in Chromium (and deliveries such as Google Chrome and Microsoft Edge) and the Linux version of Firefox. GUI front-ends for FFmpeg have been developed, including Multimedia Xpert, XMedia Recode and ShutterEncoder.

FFmpeg is used by ffdshow, FFmpegInterop, the GStreamer FFmpeg plug-in, LAV Filters and OpenMAX IL to expand the encoding and decoding capabilities of their respective multimedia platforms.

As part of NASA's Mars 2020 mission, FFmpeg is used by the Perseverance rover on Mars for image and video compression before footage is sent to Earth.

### Embedded applications

FFmpeg is also being used in embedded applications, where it can be used with custom hardware to simplify version and dependency management and also to provide operating system abstraction across multiple different OS and processor manufacturers.

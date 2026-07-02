---
title: "Apple ProRes"
source: https://en.wikipedia.org/wiki/Apple_ProRes
domain: camera-monitor
license: CC-BY-SA-4.0
tags: camera monitor, embedded systems
fetched: 2026-07-02
---

# Apple ProRes

**Apple ProRes** is a lossy compression format developed by Apple for use in post-production that supports video resolution up to 8K. Although it uses lossy compression, it is considered a perceptually lossless compression format. It is the successor of the Apple Intermediate Codec and was introduced in 2007 with Final Cut Studio 2. Much like the H.26x and MPEG standards, the ProRes family of codecs use compression algorithms based on the discrete cosine transform (DCT). ProRes is widely used as a final format delivery method for HD broadcast files in commercials, features, Blu-ray and streaming.

## Overview

ProRes is a line of intermediate codecs, which means they are intended for use during video editing, and not for practical end-user viewing. This is achieved by only using intra-frame compression, where each frame is stored independently and can be decoded with no dependencies on other frames. The benefit of an intermediate codec is that it offers excellent random access performance in post-production applications, and retains higher quality than end-user codecs while still requiring much less expensive disk systems compared to uncompressed video. It is comparable to Avid's DNxHD codec or CineForm which offer similar bitrates and are also intended to be used as intermediate codecs. ProRes is a DCT scalar based intra-frame-only codec and is therefore simpler to decode than distribution-oriented formats like H.264. In 2018 Apple added a new "ProRes RAW" (compressed Bayer filter) to Final Cut Pro X, after Blackmagic Design implemented compressed Bayer as "CinemaDNG 3:1" and "CinemaDNG 4:1" in their cameras and DaVinci Resolve.

## Data rates

ProRes supports different data rates and different resolutions. All ProRes422-variants use chroma subsampling of 4:2:2 at 10-bit color depth. ProRes 4444 and 4444 XQ samples color in the 4:4:4 schema with a color depth of 10 or 12 bits, and can optionally include an alpha channel.

| Resolution | FPS | ProRes 422 Proxy | ProRes 422 LT | ProRes 422 | ProRes 422 HQ | ProRes 4444 (without Alpha) | ProRes 4444 XQ (without Alpha) |
|---|---|---|---|---|---|---|---|
| (points) | (Hz) | (Mbit/s) | (Mbit/s) | (Mbit/s) | (Mbit/s) | (Mbit/s) | (Mbit/s) |
| 720 × 0576 | 50i, 25p | 12 | 28 | 41 | 61 | 92 | 138 |
| 1280 × 0720 | 25p | 19 | 42 | 61 | 92 | 138 | 206 |
| 1440 × 1080 | 50i, 25p | 32 | 73 | 105 | 157 | 236 | 354 |
| 1920 × 1080 | 50i, 25p | 38 | 85 | 122 | 184 | 275 | 415 |
| 50p | 76 | 170 | 245 | 367 | 551 | 826 |   |
| 60p | 91 | 204 | 293 | 440 | 990 | 990 |   |
| 2048 × 1536 | 25p | 58 | 131 | 189 | 283 | 425 | 637 |
| 50p | 117 | 262 | 377 | 567 | 850 | 1275 |   |
| 3840 × 2160 | 25p | 151 | 342 | 492 | 737 | 1106 | 1659 |
| 50p | 303 | 684 | 983 | 1475 | 2212 | 3318 |   |
| 60p | 363 | 821 | 1178 | 1768 | 2652 | 3977 |   |
| 4096 × 2160 | 25p | 162 | 365 | 524 | 786 | 1180 | 1769 |
| 50p | 323 | 730 | 1049 | 1573 | 2359 | 3539 |   |
| 5120 × 2880 | 25p | 202 | 456 | 655 | 983 | 1475 | 2212 |
| 50p | 405 | 912 | 1311 | 1966 | 2949 | 4424 |   |

## ProRes 422

### Key features

- 8K, 5K, 4K, UHD, 2K, HD (up to 1920×1080), & SD resolutions
- 4:2:2 chroma subsampling
- Up to 12-bit sample depth
- I-frame-only encoding
- Variable bitrate (VBR) encoding
- Normal 147 Mbit/s and High-Quality 220 Mbit/s and ProRes (LT) 100 Mbit/s as well as ProRes Proxy for HD 45 Mbit/s for HD resolution at 60i
- Normal 42 Mbit/s and High-Quality 63 Mbit/s for SD resolution at 29.97
- Fast encoding and decoding (both at full size and half size)

## ProRes 4444 and ProRes 4444 XQ

**ProRes 4444** and **ProRes 4444 XQ** are lossy video compression formats developed by Apple Inc. for use in post-production and include support for an alpha channel.

ProRes 4444 was introduced with Final Cut Studio (2009) as another in the company's line of intermediate codecs for editing material but not for final delivery. It shares many features with other, 422, codecs of Apple's ProRes family but provides better quality than 422 HQ in color detail. It has a target data rate of approximately 330 Mbit/s for 4:4:4 sources at 1920x1080 and 29.97 fps.

ProRes 4444 XQ was introduced with Final Cut Pro X version 10.1.2 in June 2014. It has a target data rate of approximately 500 Mbit/s for 4:4:4 sources at 1920x1080 and 29.97 fps, and requires OS X v10.8 (Mountain Lion) or later.

### Key features

- 8K, 5K, 4K, 2K, HD (up to 1920×1080), & SD resolutions
- 4:4:4 chroma subsampling
- Up to 12-bit sample depth for video
- Variable bitrate (VBR) encoding
- Alpha channel support at up to 16-bit sample depth

## ProRes RAW

In April 2018 Apple released ProRes RAW. It is built upon the same technology as other ProRes codecs, but is directly applied to the raw data coming from the sensor, thus delaying the debayering process to the post-production stage. ProRes RAW therefore aims at quality and better color reproduction, rather than performance.

Apple ProRes RAW is available in LUMIX cameras, Nikon cameras (Z9, Z8, Z6iii), Sony Alpha FX3 via Atomos Ninja V, and as of September 2025, in the Apple iPhone 17 Pro and ProMax.

ProRes RAW is a 16 bit uncompressed video format in .mov.

In the Sony FX3 and the Atomos Ninja V, ProRes Raw records in 16 bit and compresses in 12 bit for color data.

ProRes RAW codec is natively available in Adobe Premiere Pro, Adobe After Effects, Assimilate Scratch, Apple Final Cut Pro and Davinci Resolve.

## Playback

On 28 August 2008, Apple introduced a free ProRes QuickTime Decoder for both Mac and Windows that allows playback of ProRes files through QuickTime.

## Open source projects

On 15 September 2011, FFmpeg introduced a free decoder for ProRes 422 for libavcodec.

FFmbc, a fork of FFmpeg customized for broadcast and professional usage, supports ProRes 422 and 4444 files.

On 1 October 2011, JCodec introduced an open source (FreeBSD License) pure Java decoder for ProRes 422, a translation of the FFmpeg version.

FFmpeg as of 2024, now supports encoding generally compatible (for current hardware and broadcasting software suites) Proxy-HQ and 4444/4444XQ modes, but still only supports 10-bit or 16-bit modes and not the 12-bit standard for the 4444 codec versions (4:4:4 chroma subsampling) compared to hardware and native Apple licensed software encoders.

## Encoding

Installing Final Cut Pro will install the ProRes codecs for encoding files on macOS. Without Final Cut Pro installed, QuickTime Player can also be used to capture ProRes 422 video from any compatible attached camera, using the "Maximum" quality setting when producing a Movie Recording.

Apple released ProRes bundled with other pro codecs as a download for users with "qualifying copies of Final Cut Pro, Motion, or Compressor" installed, for OS X with QuickTime 7.6 and newer.

At the April 2010 NAB Show, Digital Video Systems launched the first Windows 7 platform with the ability to encode to all the varieties of Apple ProRes at speeds far faster than real time on their Clipster product.

On March 31, 2011, Telestream added support for ProRes encoding on Windows systems with Episode Engine, Vantage, and FlipFactory as a free upgrade to the current versions of these products. The system must be running on Windows Server 2008 and be able to support this feature. ProRes video capturing and output to tape is available in Telestream's Pipeline network encoder.

On 29 October 2011, FFmpeg introduced a free encoder, enabling ProRes 422 encoding on all FFmpeg supported platforms.

On 1 November 2011, JCodec introduced an open source (BSD License) pure Java encoder for ProRes 422.

At the April 2012 NAB Show, Brevity introduced a customized algorithm for the accelerated transport and encoding of ProRes files.

## Frame layout

A typical ProRes 422 frame has the following layout:

- Frame container atom
- Frame header
- Picture 1
- Picture 2 (interlaced frames only)

## ProRes hardware

The Arri Alexa has a built-in ProRes recording unit for its 1080p and 2K video streams, supporting ProRes 4444 and all ProRes 422 versions.

As of June 2011, several hardware-based ProRes encoders exist, from AJA Video Systems (HD FireWire 800 interface; Ki Pro and Ki Pro Mini portable recorders, Ki Pro Rack and Ki Pro Ultra for 4K/UltraHD workflows), Atomos (Ninja and Samurai recorders), Sound Devices (PIX series recorders), Convergent Designs (Odyssey7, 7Q, 7Q+), and Fast Forward Video (Sidekick recorder).

At NAB 2012, Blackmagic announced ProRes recording support for their HyperDeck SSD recorders as well as onboard recording on the Blackmagic Cinema Camera, and Brevity announced a GPU-based ProRes transcoder with simultaneous accelerated file transport.

In 2013 Blackmagic Design released the Blackmagic Cinema Camera that record in RAW and ProRes files directly in camera 4:2:2 10-bit.

In 2013 Convergent Design introduced their Odyssey7 and Odyssey7Q monitor/recorders that can record in Apple ProRes 422 (HQ) and are certified by Apple.

In 2014 Atomos introduced their latest advanced recorder Shogun that can record 4K in Apple ProRes.

In 2015 AJA introduced the CION production camera that can capture 4K/UltraHD/2K/HD to all Apple ProRes 422 formats as well as Apple ProRes 4444 in 12-bit.

In 2016 Blackmagic Design released UrsaMini 4.6k that can capture from 4.6k to HD in all Apple ProRes flavor from Proxy to 4444 in 12-bit.

In 2018/2019 Blackmagic Design released Pocket Cinema Camera 4K that can capture 4k/UltraHD/1080p in all Apple ProRes 422 formats.

In 2019 Mac Pro introduced a new "Apple Afterburner" card as an optional component to accelerate ProRes and ProRes RAW decoding.

In 2021, Apple announced the iPhone 13 Pro, with ProRes encoding/decoding using its built-in camera app alongside its recent addition of DNG raw photos (DNG v5.1) on the 12 Pro Models. ProRes encoding can be performed at up to 3840 × 2160 30p ProRes HQ with Dolby Vision HDR color profiles on models with at least 256 GB of storage, while the 128 GB model will be limited to 1080p 30p with its built-in camera application. Other applications such as Filmic Pro (a third-party application, notably used by Apple for their demo reels in recent years) bypasses this limitation on lower end models and allows full industry compliant ProRes 10bit 4:2:2 profiles LT, 422, and HQ using the less supported Dolby Vision HDR standard. In 2023, Apple announced the iPhone 15 Pro, which added the ability to shoot ProRes in the Apple Log format, as well as the ability to shoot ProRes footage at up to 3840 x 2160 60p to an external drive via the USB-C port from the built-in camera application.

In 2021, Apple announced the Apple M1 Pro and M1 Max, variants of the Apple M1 system on a chip containing, among other new features, hardware ProRes encoding and decoding acceleration.

In February 2022, Panasonic released the Lumix GH6 mirrorless camera which has the ability to record 5.7K video in ProRes 422 HQ.

On June 6, 2022, Apple announced the Apple M2 with 8K ProRes hardware decoding and encoding acceleration.

On January 17, 2023, Apple announced the Apple M2 Pro and M2 Max with 8K ProRes hardware decoding and encoding acceleration.

On October 30, 2023, Apple announced the Apple M3 series of chips with 8K ProRes hardware decoding and encoding acceleration.

Lasergraphics motion picture film scanning systems include support for output to ProRes 4444 HQ/XQ, ProRes 422, and others.

## Awards

The ProRes codec was awarded an Engineering Emmy Award in 2020 for "Outstanding Achievement in Technology".

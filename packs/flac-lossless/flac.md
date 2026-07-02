---
title: "FLAC"
source: https://en.wikipedia.org/wiki/FLAC
domain: flac-lossless
license: CC-BY-SA-4.0
tags: flac lossless, linear predictive coding audio, rice coding, lossless audio
fetched: 2026-07-02
---

# FLAC

**FLAC** (/flæk/; **Free Lossless Audio Codec**) is an audio coding format for lossless compression of digital audio, developed by the Xiph.Org Foundation, and is also the name of the free software project producing the FLAC tools, the reference software package that includes a codec implementation. Digital audio compressed by FLAC's algorithm can typically be reduced to between 50 and 70 percent of its original size and decompresses to an identical copy of the original audio data.

FLAC is an open format with royalty-free licensing and a reference implementation which is free software. FLAC supports metadata tagging, album cover art, and fast seeking.

## History

Development was started in 2000 by Josh Coalson. The bitstream format was frozen with the release of version 0.9 of the reference implementation on 31 March 2001. Version 1.0 was released on 20 July 2001.

On 29 January 2003, the Xiph.Org Foundation and the FLAC project announced the incorporation of FLAC under the Xiph.org banner. Xiph.org is home to other free compression formats such as Vorbis, Theora, Speex and Opus.

Version 1.3.0 was released on 26 May 2013, at which point development was moved to the Xiph.org git repository.

In 2019, FLAC was proposed as an IETF standard.

In December 2024, FLAC was formally specified in and published as RFC 9639.

## Design

FLAC is a lossless encoding of linear pulse-code modulation data.

### File structure

A FLAC file consists of the magic number `fLaC`, metadata, and encoded audio.

The encoded audio is divided into frames, each of which consists of a header, a data block, and a CRC16 checksum. Each frame is encoded independently of the others. A frame header begins with a sync word, used to identify the beginning of a valid frame. The rest of the header contains the number of samples, position of the frame, channel assignment, and optionally the sample rate and bit depth. The data block contains the audio information.

Metadata in FLAC precedes the audio. Properties like the sample rate and the number of channels are always contained in the metadata. It may also contain other information, the album cover, for example. FLAC uses Vorbis comments for textual metadata like track title and artist name.

### Encoding and decoding

The FLAC encoding algorithm consists of multiple stages. In the first stage, the input audio is split into blocks. If the audio contains multiple channels, each channel is encoded separately as a subblock. The encoder then tries to find a good mathematical approximation of the block, either by fitting a simple polynomial, or through general linear predictive coding. A description of the approximation, which is only a few bytes in length, is then written. Finally, the difference between the approximation and the input, called residual, is encoded using Rice coding. In many cases, a description of the approximation and the encoded residual takes up less space than using pulse-code modulation.

The decoding process is the reverse of encoding. The compressed residual is first decoded. The description of the mathematical approximation is then used to calculate a waveform. The result is formed by adding the residual and the calculated waveform. As FLAC compresses losslessly, the decoded waveform is identical to the waveform before encoding.

For two-channel stereo, the encoder may choose to joint-encode the audio. The channels are transformed into a side channel, which is the difference between the two input channels, and a mid channel, the sum of the two input channels. In place of a mid channel, the left channel or the right channel may be encoded instead, which is sometimes more space-efficient.

Even though the reference encoder uses a single block size for the whole stream, FLAC allows the block size in samples to vary per block.

### Compression

The amount of compression is determined by various parameters, including the order of the linear prediction model and the block size. Regardless of the amount of compression, the original data can always be reconstructed perfectly.

For the user's convenience, the reference implementation defines 9 compression levels, which are presets of the more technical parameters to the encoding algorithm. The levels are labeled from 0 to 8, with higher numbers resulting in a higher compression ratio, at the cost of compression speed. The meaning of each compression level varies by implementation.

FLAC is optimized for decoding speed at the expense of encoding speed. A benchmark has shown that, while there is little variation in decoding speed as compression level increases, beyond the default compression level 5, the encoding process takes up considerably more time with little space saved compared to level 5.

### Implementation

Alongside the format, the FLAC project also contains a free and open-source reference implementation of FLAC called libFLAC. libFLAC contains facilities to encode and decode FLAC data and to manipulate the metadata of FLAC files. libFLAC++, an object-oriented wrapper around libFLAC for C++, and the command-line programs `flac` and `metaflac`, are also part of the reference implementation.

The FLAC format, along with libFLAC, is not known to be covered by any patents, and anyone is free to write their own implementations of FLAC.

## Comparison to other formats

FLAC is specifically designed for efficient packing of audio data, unlike general-purpose lossless algorithms such as DEFLATE, which are used in ZIP and gzip. While ZIP may reduce the size of a CD-quality audio file by 10–20%, FLAC is able to reduce the size of audio data by 40–50% by taking advantage of the characteristics of audio.

The technical strengths of FLAC compared to other lossless formats lie in its ability to be streamed and decoded quickly, independent of compression level.

Since FLAC is a lossless scheme, it is suitable as an archive format for owners of CDs and other media who wish to preserve their audio collections. If the original media are lost, damaged, or worn out, a FLAC copy of the audio tracks ensures that an exact duplicate of the original data can be recovered at any time. An exact restoration from a lossy copy (e.g., MP3) of the same data is impossible. FLAC's being lossless means it is highly suitable for transcoding, e.g., to MP3, without the normally associated transcoding quality loss between one lossy format and another. A CUE file can optionally be created when ripping a CD. If a CD is read and ripped perfectly to FLAC files, the CUE file allows later burning of an audio CD that is identical in audio data to the original CD, including track order and pregap, but excluding additional data such as lyrics and CD+G graphics. But depending on the burning program used, CD-Text may be recovered from the metadata stored in the CUE sheet and burned back to a new copy on blank CD-R media.

## Adoption and implementations

### Reference implementation

The reference implementation of FLAC is implemented as the *libFLAC* core encoder & decoder library, with the main distributable program `flac` being the reference implementation of the libFLAC API. This codec API is also available in C++ as libFLAC++. The reference implementation of FLAC compiles on many platforms, including most Unix (such as Solaris, BSD) and Unix-like (including Linux), Windows, BeOS, and OS/2 operating systems. There are build systems for autotools and CMake. There is currently no multicore support in libFLAC, but utilities such as GNU parallel and various graphical frontends can be used to spin up multiple instances of the encoder.

### Hardware and software

FLAC playback support in portable audio devices and dedicated audio systems is limited compared to formats such as MP3 or uncompressed PCM. FLAC support is included by default in Windows 10, Android, macOS and iOS.

|   | Microsoft Windows | macOS | Android | iOS |
|---|---|---|---|---|
| Codec support | Yes | Yes | Yes | Yes |
| Container support | FLAC (.flac) Matroska (.mka, .mkv) Ogg (.oga) | FLAC (.flac) Core Audio Format (.caf) | FLAC (.flac) | FLAC (.flac) Core Audio Format (.caf) |
| Notes | Support introduced in Windows 10. Windows Media Player (2022) also supports FLAC in an Ogg container for live streams (e.g. Icecast internet radio). | Support introduced in macOS 10.13 High Sierra. | Support introduced in Android 3.1. Android natively supports regular FLAC (.flac), but not Ogg FLAC (.oga). However, support for both regular FLAC and Ogg FLAC were later added to the Files (Google) file manager. | Support introduced in iOS 11 (but depends on hardware). |

Various other containers are supported, independently of the operating system used, depending on the playback software used.

### Use in archives

The standardization process of the FLAC format into RFC 9639 was driven by the specific use case of archival and preservation in mind. The National Archives and Records Administration of the United States has FLAC listed as a preferred format for digital audio.

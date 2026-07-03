---
title: ".m2ts"
source: https://en.wikipedia.org/wiki/.m2ts
domain: apple-prores
license: CC-BY-SA-4.0
tags: apple prores
fetched: 2026-07-03
---

# .m2ts

**.m2ts** is a filename extension used for the **Blu-ray disc Audio-Video (BDAV) MPEG-2 Transport Stream (M2TS)** container file format. It is used for multiplexing audio, video and other streams, such as subtitles. It is based on the MPEG-2 transport stream container. This container format is commonly used for high-definition video on Blu-ray Disc and AVCHD.

## Overview

The BDAV container format is a modification of the MPEG-2 transport stream (ITU-T H.222.0 | ISO/IEC 13818-1) specification for random-access media, such as Blu-ray discs, DVDs, hard drives or solid-state memory cards. The format is informally called *M2TS*.

In order to optimize the storage size, the format uses variable rate Transport Streams instead of the constant rates found in MPEG-2 TS broadcast. To be able to reconstruct a T-STD compliant constant rate Transport Stream for playback, the arrival timestamp of each packet needs to be recorded.

The standard MPEG-2 TS 188-byte packet is prefixed with a 4-byte extra header to a total size of 192 bytes. The header consists of a 2-bit copy permission indicator and the 30-bit arrival timestamp with a resolution of 27 MHz.

The BDAV container format (`.m2ts`) is a standard used on Blu-ray discs. Blu-ray disc titles authored with menu support are in the BDMV (Blu-ray disc Movie) format and contain audio, video, and other streams in a BDAV container (`.m2ts`), which is based on the MPEG transport stream format. The BDAV container is also used in the BDAV (Blu-ray disc Audio/Visual) disc format, the consumer-oriented alternative to the BDMV discs. The BDAV disc format is used on BD-RE and BD-R discs for audio/video recording.

The BDAV container with filename extension .MTS or .m2ts is also used in AVCHD format, which is a high-definition digital video camera recorder format. AVCHD is a simpler form of the Blu-ray disc standard with just one video encoding algorithm and two audio encodings. Compared to Blu-ray disc format, AVCHD can use various storage media, such as DVD media, memory cards or hard disk drives. The BDAV container contains videos recorded using AVCHD camcorders, such as Sony's HDR-SR(xx) series models. Panasonic, Canon and other brands of AVCHD camcorders also store recorded video in the BDAV container format.

## Formats

The BDAV container format used on Blu-ray discs can contain one of the three mandatory supported video compression formats–H.262/MPEG-2 Part 2, H.264/MPEG-4 AVC or SMPTE VC-1–and audio compression formats, such as Dolby Digital, DTS or uncompressed Linear PCM. Optionally supported audio formats are Dolby Digital Plus, DTS-HD High Resolution Audio, DTS-HD Master Audio and Dolby TrueHD.

The BDAV container format used on AVCHD equipment is more restricted and can contain only H.264/MPEG-4 AVC video compression and Dolby Digital (AC-3) audio compression or uncompressed LPCM audio.

## File and directory structure

The names of M2TS files are in the form zzzzz.m2ts, where *zzzzz* is a five-digit number corresponding to the audiovisual clip. This number is also used in the filename of an associated clip information file "*zzzzz*.clpi". (This number can be a date and time stamp of when the video clip was recorded.) Each stream has its own file.

Files in the AVCHD format use the legacy 8.3 filename convention, whereas Blu-ray discs use long filenames. This is why the filename extension of video files is "`.MTS`" instead of Blu-ray disc's "`.m2ts`". Also, other files use different extensions: `.CPI` – `.clpi`, `.MPL` – `.mpls`, `.BDM` – `.bdmv`.

The M2TS files on a Blu-ray disc are placed in the subdirectory "STREAM" of the "BDMV" (or "BDAV") directory, which is at the root level. (e.g. \BDMV\STREAM\00001.m2ts or \BDAV\STREAM\00001.m2ts) On some AVCHD equipment, the "BDMV" directory is located in the "AVCHD" directory, which is placed at the root level (e.g. \AVCHD\BDMV\STREAM\00001.MTS).

## Software support

Almost all commercially produced Blu-ray disc titles use a copy protection method called the Advanced Access Content System, which encrypts the content of the disc, including M2TS files. Software that supports M2TS files usually works only with decrypted or unencrypted files. Blu-ray disc software players can usually play back encrypted content from the original disc. Video content created using AVCHD equipment is commonly unencrypted.

Most M2TS files can be played with ALLPlayer, MPlayer, VLC, PotPlayer and other media players, depending on the compression formats used in the M2TS file. Some players will need an appropriate codec, component or plugin installed.

Current versions of Nero Vision, FormatFactory, MediaCoder, HandBrake and Picture Motion Browser are capable of converting M2TS files into MPEG-4 files, which can also be viewed using the aforementioned media players.

M2TS files can also be played on Sony PlayStation 3s, Sony Bravia TVs, Western Digital WDTVs, Xtreamer media player, Amkette FlashTV HD Media Player and Panasonic Viera TVs supporting playback of AVCHD.

Apple's Final Cut Pro can read .MTS files (as stored in Sony HDR camcorders) by using the AVCHD plugin in the Log and Transfer window.

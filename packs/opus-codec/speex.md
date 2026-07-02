---
title: "Speex"
source: https://en.wikipedia.org/wiki/Speex
domain: opus-codec
license: CC-BY-SA-4.0
tags: opus audio, celt codec, silk speech, voip audio codec
fetched: 2026-07-02
---

# Speex

The **Speex** project is an attempt to create a free software speech codec, unencumbered by patent restrictions. Speex is licensed under the BSD License and is used with the Xiph.org Foundation's Ogg container format.

The Speex coder uses the Ogg bitstream format, and the Speex designers see their project as complementary to the Vorbis general-purpose audio compression project.

Since 2012, the developers of Speex have considered it to be obsoleted by Opus.

## Description

Unlike many other speech codecs, Speex is not targeted at cell phones but rather at voice over IP (VoIP) and file-based compression. The design goals have been to make a codec that would allow both very good quality speech and low bit rate, which led to the development of a codec with multiple bit rates. Very good quality also meant the support of wideband (16 kHz sampling rate) in addition to narrowband (telephone quality, 8 kHz sampling rate). Designing for VoIP instead of cell phone use means that Speex must be robust to lost packets, but not to corrupted ones since UDP ensures that packets either arrive unaltered or don't arrive. All this led to the choice of Code Excited Linear Prediction (CELP) as the encoding technique to use for Speex. One of the main reasons is that CELP has long proved that it could do the job and scale well to both low bit rates (as evidenced by DoD CELP @ 4.8 kbit/s) and high bit rates (as with G.728 @ 16 kbit/s). The main characteristics can be summarized as follows:

- Free software/open-source, patent and royalty-free
- Integration of narrowband and wideband in the same bit-stream
- Wide range of bit rates available (from 2 to 44 kbit/s)
- Dynamic bit rate switching and Variable bit-rate (VBR)
- Voice Activity Detection (VAD, integrated with VBR)
- Variable complexity
- Ultra-wideband mode at 32 kHz (up to 48 kHz)
- Intensity stereo encoding option

### Feature description

#### Sampling rate

Speex is mainly designed for 3 different sampling rates: 8 kHz (narrowband), 16 kHz (wideband) and 32 kHz (ultra-wideband).

#### Quality

Speex encoding is controlled most of the time by a quality parameter that ranges from 0 to 10. In constant bit-rate (CBR) operation, the quality parameter is an integer, while for variable bit-rate (VBR), the parameter is a float.

#### Complexity (variable)

With Speex, it is possible to vary the complexity allowed for the encoder. This is done by controlling how the search is performed with an integer ranging from 1 to 10 in a way that's similar to the -1 to -9 options to gzip and bzip2 compression utilities. For normal use, the noise level at complexity 1 is between 1 and 2 dB higher than at complexity 10, but the CPU requirements for complexity 10 is about 5 times higher than for complexity 1. In practice, the best trade-off is between complexity 2 and 4, though higher settings are often useful when encoding non-speech sounds like DTMF tones.

#### Variable Bit-Rate (VBR)

Variable bit-rate (VBR) allows a codec to change its bit rate dynamically to adapt to the "difficulty" of the audio being encoded. In the example of Speex, sounds like vowels and high-energy transients require a higher bit rate to achieve good quality, while fricatives (e.g. s and f sounds) can be coded adequately with fewer bits. For this reason, VBR can achieve lower bit rate for the same quality, or a better quality for a certain bit rate. Despite its advantages, VBR has two main drawbacks: first, by only specifying quality, there's no guarantee about the final average bit-rate. Second, for some real-time applications like voice over IP (VoIP), what counts is the maximum bit-rate, which must be low enough for the communication channel.

#### Average Bit-Rate (ABR)

Average bit-rate solves one of the problems of VBR, as it dynamically adjusts VBR quality in order to meet a specific target bit-rate. Because the quality/bit-rate is adjusted in real-time (open-loop), the global quality will be slightly lower than that obtained by encoding in VBR with exactly the right quality setting to meet the target average bitrate.

#### Voice Activity Detection (VAD)

When enabled, voice activity detection detects whether the audio being encoded is speech or silence/background noise. VAD is always implicitly activated when encoding in VBR, so the option is only useful in non-VBR operation. In this case, Speex detects non-speech periods and encode them with just enough bits to reproduce the background noise. This is called "comfort noise generation" (CNG).

#### Discontinuous Transmission (DTX)

Discontinuous transmission is an addition to VAD/VBR operation, that allows to stop transmitting completely when the background noise is stationary. In file-based operation, only 5 bits are used for such frames (corresponding to 250 kbit/s) since the process that is writing to the file cannot be stopped.

#### Perceptual enhancement

Perceptual enhancement is a part of the decoder which, when turned on, tries to reduce (the perception of) the noise produced by the coding/decoding process. In most cases, perceptual enhancement makes the sound further from the original objectively (signal-to-noise ratio), but in the end it still sounds better (subjective improvement).

#### Algorithmic delay

Every speech codec introduces a delay in the transmission. For Speex, this delay is equal to the frame size, plus some amount of "look-ahead" required to process each frame. In narrowband operation (8 kHz), the delay is 30 ms, while for wideband (16 kHz), the delay is 34 ms. These values don't account for the CPU time it takes to encode or decode the frames.

## Large application base

There is already a large base of applications supporting the speex codec, from teleconference software to streaming, P2P, and audio processing applications. Most of these are based on the DirectDS filter, OpenACM codec -- Netmeeting on Microsoft Windows, or OpenH323 on Linux (GnomeMeeting), for example. There are also plugins for the Winamp and XMMS players.

The MIME type for Speex is audio/x-speex, although the type audio/speex is proposed.

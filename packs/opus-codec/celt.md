---
title: "CELT"
source: https://en.wikipedia.org/wiki/CELT
domain: opus-codec
license: CC-BY-SA-4.0
tags: opus audio, celt codec, silk speech, voip audio codec
fetched: 2026-07-02
---

# CELT

**Constrained Energy Lapped Transform** (**CELT**) is an open, royalty-free lossy audio compression format and a free software codec with especially low algorithmic delay for use in low-latency audio communication. The algorithms are openly documented and may be used free of software patent restrictions. Development of the format was maintained by the Xiph.Org Foundation (as part of the Ogg codec family) and later coordinated by the Opus working group of the Internet Engineering Task Force (IETF).

CELT was meant to bridge the gap between Vorbis and Speex for applications where both high quality audio and low delay are desired. It is suitable for both speech and music. It borrows ideas from the CELP algorithm, but avoids some of its limitations by operating in the frequency domain exclusively.

The original stand-alone CELT has been merged into Opus. Therefore, CELT as stand-alone format is now abandoned and obsolete. Development is going on only for its hybridised form as a layer of Opus, integrated with SILK. This article covers the historic, stand-alone format; for the integrated form and its evolution since the integration into Opus see the article on Opus.

## Properties

CELT's central feature is low algorithmic delay. It allows for latencies of typically 3 to 9 ms but is configurable to below 2 ms at the price of more bitrate to reach a similar audio quality. CELT supports mono and stereo audio and is applicable to both speech and music. It can use a sampling rate from 32 kHz to 48 kHz and above and an adaptive bitrate from 24 kbit/s to 128 kbit/s per channel and above.

There are no known intellectual property issues pertaining to the CELT algorithm, and its reference implementation is published under a permissive open-source license (the 2-clause BSD).

Like Vorbis, CELT is a fullband (entire human hearing range) general-purpose codec, i.e. not specialized for special types of audio signals and therefore different from its sibling project Speex. The format enables for transparent results at high bitrates, as well as very decent quality at lower bitrates. All in all, the compression capabilities are said to be significantly superior to those of MP3, and as another useful feature for realtime applications like telephony, CELT's audio quality at lower bitrates are even on par with HE-AACv1, thanks to the band folding. In comparative double-blind listening tests it proved to be noticeably superior to HE-AACv1 at ~64 kbit/s.

It has a comparably low computational complexity that resembles that of the low-delay variant of AAC (AAC-LD) and stays significantly below the complexity of Vorbis.

It enables for constant and variable bitrate. If the signal disappears into the noise floor in speech pauses and similar cases, the transmission can be limited to signal the output of comfort noise to the decoder. Most settings of the naturally streaming-enabled format can be changed on the fly without interrupting transmission.

The format is robust to transmission errors. Loss of whole packets as well as bit errors can be masked with a steady degradation of audio quality (packet loss concealment, PLC).

## Technology

CELT is a transform codec based on the modified discrete cosine transform (MDCT) and concepts from CELP (with a code book for excitation, but in the frequency domain).

The initial PCM-coded signal is handled in relatively small, overlapping blocks for the MDCT (window function) and transformed to frequency coefficients. Choosing an especially short block size on the one hand enables for a low latency, but also leads to poor frequency resolution that has to be compensated. For a further reduction of the algorithmic delay to the expense of a minor sacrifice in audio quality, the by nature 50% of overlap between the blocks is practically cut down to half by silencing the signal during one eight at both ends of a block, respectively.

The coefficients are grouped to resemble the critical bands of the human auditory system. The entire amount of energy of each group is analysed and the values quantised for data reduction and compressed through prediction by only transmitting the difference to the predicted values (delta encoding).

The (unquantised) band energy values are removed from the raw DCT coefficients (normalisation). The coefficients of the resulting residual signal (so-called “band shape”) are coded by Pyramid Vector Quantisation (PVQ, a spherical vector quantisation). This encoding leads to code words of fixed (predictable) length, which in turn enables for robustness against bit errors and leaves no need for entropy encoding. Finally, all output of the encoder are coded to one bitstream by a range encoder. In connection with the PVQ, CELT uses a technique known as band folding, which delivers a similar effect to spectral band replication (SBR) by reusing coefficients of lower bands for higher ones, but has much less impact on the algorithmic delay and computational complexity than the SBR. This works against “birdie” artifacts by preserving more richness in the appropriate frequency bands.

The decoder unpacks the individual components from the range coded bitstream, multiplies the band energy to the band shape coefficients and transforms them back (via iMDCT) to PCM data. The individual blocks are rejoined using weighted overlap-add (WOLA). Many parameters are not explicitly coded, but instead reconstructed by using the same functions as the encoder.

For the channel coupling CELT may use M/S stereo or intensity stereo. Blocks can be described independent from adjacent frames (Intra-frame); for example to enable a decoder to jump into a running stream. With transform codecs so-called pre-echo artifacts can get audible, because the quantisation error of sharp, energy-heavy sounds (transients) can spread over the entire DCT block and the transient doesn't mask them backward in time as well as forward. With CELT each block can be further divided to thwart such artifacts.

## History

First work on plans and drafts for a Vorbis successor was done in 2005 at Xiph.org as part of the Ghost project (initially talked about as “Vorbis II”). This discussion together with Vorbis creator Christopher Montgomery led to Jean-Marc Valin′s interest in a particularly low-latency codec. Valin has worked on CELT since 2007. In December 2007, the first draft version of libcelt was published as version 0.0.1, initially named “Code-Excited Lapped Transform”. CELT was established as an IETF technology in July 2009 under the "ietfcodec" working group. In May 2009, a draft of *RTP payload format for the CELT Codec* was published.

In version 0.9, the pitch prediction operating in the frequency domain used until then was replaced by a less complex solution with a pre- and postfilter pair in time domain, which was contributed by Raymond Chen of Broadcom.

With CELT 0.11 from February 4, 2011 the format was tentatively frozen (“soft freeze”) – reserving the possibility of unexpectedly necessary last changes.

Shortly after the advent of the CELT/SILK hybrid codec Opus (formerly known as Harmony), the development of CELT as a separate project was halted, instead living on the basis of Opus, which aims to treat the lower part of the spectral range in the time domain with linear prediction (SILK) and the higher part in the frequency domain with the MDCT. The draft for Opus has been registered at the IETF since September 2010.

## Software

The software library **libcelt** serves as the reference implementation for CELT, written in C and published as free software under Xiph's own 3-clause BSD-ish license.

Despite the format not being finally frozen, it was being used in many VoIP applications such as Ekiga and FreeSWITCH, which switched to CELT upon entering soft-freeze in January 2009, as well as Mumble, TeamSpeak and other software. In April 2011, support for CELT was included in FFmpeg.

CELT is also supported or used by:

- GStreamer
- jack-audio-connection-kit (netjack)
- Mumble (starting with version 1.2)
- SFLphone
- TeamSpeak 3
- SPICE
- Dota 2
- Counter Strike: Global Offensive
- Team Fortress 2

---
title: "Advanced Audio Coding"
source: https://en.wikipedia.org/wiki/Advanced_Audio_Coding
domain: audio-codec-aac
license: CC-BY-SA-4.0
tags: aac codec, advanced audio coding, perceptual audio, aac encoding
fetched: 2026-07-02
---

# Advanced Audio Coding

**Advanced Audio Coding** (**AAC**) is an audio coding standard for lossy digital audio compression. It was developed by Dolby, AT&T, Fraunhofer and Sony, originally as part of the MPEG-2 specification but later improved under MPEG-4. AAC was designed to be the successor of the MP3 format (MPEG-2 Audio Layer III) and generally achieves higher sound quality than MP3 at the same bit rate. AAC encoded audio files are typically packaged in an MP4 container most commonly using the filename extension `.m4a`.

The basic profile of AAC (both MPEG-4 and MPEG-2) is called **AAC-LC** (*Low Complexity*). It is widely supported in the industry and has been adopted as the default or standard audio format on products including Apple's iTunes Store, Nintendo's Wii, DSi and 3DS and Sony's PlayStation 3. It is also further supported on various other devices and software such as iPhone, iPod, PlayStation Portable and Vita, PlayStation 5, Android and older cell phones, digital audio players like Sony Walkman and SanDisk Clip, media players such as VLC, Winamp and Windows Media Player, various in-dash car audio systems, and streaming services such as Spotify, Apple Music, YouTube and YouTube Music. AAC has been further extended into HE-AAC (*High Efficiency*, or AAC+), which improves efficiency over AAC-LC. Another variant is AAC-LD (*Low Delay*).

AAC supports inclusion of 48 full-bandwidth (up to 96 kHz) audio channels in one stream plus 16 low frequency effects (LFE, limited to 120 Hz) channels, up to 16 "coupling" or dialog channels, and up to 16 data streams. The quality for stereo is satisfactory to modest requirements at 96 kbit/s in joint stereo mode; however, hi-fi transparency demands data rates of at least 128 kbit/s (VBR). Tests of MPEG-4 audio have shown that AAC meets the requirements referred to as "transparent" for the ITU at 128 kbit/s for stereo, and 384 kbit/s for 5.1 audio. AAC uses only a modified discrete cosine transform (MDCT) algorithm, giving it higher compression efficiency than MP3, which uses a hybrid coding algorithm that is part MDCT and part FFT.

## History

### Background

The discrete cosine transform (DCT), a type of transform coding for lossy compression, was proposed by Nasir Ahmed in 1972, and developed by Ahmed with T. Natarajan and K. R. Rao in 1973, publishing their results in 1974. This led to the development of the modified discrete cosine transform (MDCT), proposed by J. P. Princen, A. W. Johnson and A. B. Bradley in 1987, following earlier work by Princen and Bradley in 1986. The MP3 audio coding standard introduced in 1992 used a hybrid coding algorithm that is part MDCT and part FFT. AAC uses a purely MDCT algorithm, giving it higher compression efficiency than MP3. Development further advanced when Lars Liljeryd introduced a method that radically shrank the amount of information needed to store the digitized form of a song or speech.

AAC was developed with cooperation between AT&T Labs, Dolby, Fraunhofer IIS (who developed MP3) and Sony Corporation. AAC was officially declared an international standard by the Moving Picture Experts Group in April 1997. It is specified both as *Part 7 of the MPEG-2 standard*, and *Subpart 4 in Part 3 of the MPEG-4 standard*. Further companies have contributed to development in later years including Bell Labs, LG Electronics, NEC, Nokia, Panasonic, ETRI, JVC Kenwood, Philips, Microsoft, and NTT.

### Standardization

In 1997, AAC was first introduced as *MPEG-2 Part 7*, formally known as *ISO/IEC 13818-7:1997*. This part of MPEG-2 was a new part, since MPEG-2 already included *MPEG-2 Part 3*, formally known as *ISO/IEC 13818-3: MPEG-2 BC* (Backwards Compatible). Therefore, MPEG-2 Part 7 is also known as *MPEG-2 NBC* (Non-Backward Compatible), because it is not compatible with the MPEG-1 audio formats (MP1, MP2 and MP3).

MPEG-2 Part 7 defined three profiles: *Low-Complexity* profile (AAC-LC / LC-AAC), *Main* profile (AAC Main) and *Scalable Sampling Rate* profile (AAC-SSR). AAC-LC profile consists of a base format very much like AT&T's Perceptual Audio Coding (PAC) coding format, with the addition of temporal noise shaping (TNS), the Kaiser window (described below), a nonuniform quantizer, and a reworking of the bitstream format to handle up to 16 stereo channels, 16 mono channels, 16 low-frequency effect (LFE) channels and 16 commentary channels in one bitstream. The Main profile adds a set of recursive predictors that are calculated on each tap of the filterbank. The SSR uses a 4-band PQMF filterbank, with four shorter filterbanks following, in order to allow for scalable sampling rates.

In 1999, MPEG-2 Part 7 was updated and included in the MPEG-4 family of standards and became known as *MPEG-4 Part 3*, *MPEG-4 Audio* or *ISO/IEC 14496-3:1999*. This update included several improvements. One of these improvements was the addition of *Audio Object Types* which are used to allow interoperability with a diverse range of other audio formats such as TwinVQ, CELP, HVXC, speech synthesis and MPEG-4 Structured Audio. Another notable addition in this version of the AAC standard is *Perceptual Noise Substitution* (PNS). In that regard, the AAC profiles (AAC-LC, AAC Main and AAC-SSR profiles) are combined with perceptual noise substitution and are defined in the MPEG-4 audio standard as Audio Object Types. MPEG-4 Audio Object Types are combined in four MPEG-4 Audio profiles: Main (which includes most of the MPEG-4 Audio Object Types), Scalable (AAC LC, AAC LTP, CELP, HVXC, TwinVQ, Wavetable Synthesis, TTSI), Speech (CELP, HVXC, TTSI) and Low Rate Synthesis (Wavetable Synthesis, TTSI).

The reference software for MPEG-4 Part 3 is specified in MPEG-4 Part 5 and the conformance bit-streams are specified in MPEG-4 Part 4. MPEG-4 Audio remains backward-compatible with MPEG-2 Part 7.

The MPEG-4 Audio Version 2 (ISO/IEC 14496-3:1999/Amd 1:2000) defined new audio object types: the low delay AAC (AAC-LD) object type, bit-sliced arithmetic coding (BSAC) object type, parametric audio coding using harmonic and individual line plus noise and error resilient (ER) versions of object types. It also defined four new audio profiles: High Quality Audio Profile, Low Delay Audio Profile, Natural Audio Profile and Mobile Audio Internetworking Profile.

The HE-AAC Profile (AAC LC with SBR) and AAC Profile (AAC LC) were first standardized in ISO/IEC 14496-3:2001/Amd 1:2003. The HE-AAC v2 Profile (AAC LC with SBR and Parametric Stereo) was first specified in ISO/IEC 14496-3:2005/Amd 2:2006. The Parametric Stereo audio object type used in HE-AAC v2 was first defined in ISO/IEC 14496-3:2001/Amd 2:2004.

The current version of the AAC standard is defined in ISO/IEC 14496-3:2019.

AAC+ v2 is also standardized by ETSI (European Telecommunications Standards Institute) as TS 102005.

The MPEG-4 Part 3 standard also contains other ways of compressing sound. These include lossless compression formats, synthetic audio and low bit-rate compression formats generally used for speech.

### AAC's improvements over MP3

Advanced Audio Coding is designed to be the successor of the *MPEG-1 Audio Layer 3*, known as MP3 format, which was specified by ISO/IEC in 11172-3 (MPEG-1 Audio) and 13818-3 (MPEG-2 Audio).

Improvements include:

- more sample rates (from 8 to 96 kHz) than MP3 (16 to 48 kHz);
- up to 48 channels (MP3 supports up to two channels in MPEG-1 mode and up to 5.1 channels in MPEG-2 mode);
- up to 24 audio bit depth;
- arbitrary bit rates and variable frame length. Standardized constant bit rate with bit reservoir;
- higher bit rate (up to 512 Kbps in two channels);
- higher efficiency and simpler filter bank. AAC uses a pure MDCT (modified discrete cosine transform), rather than MP3's hybrid coding (which was part MDCT and part FFT);
- higher coding efficiency for stationary signals (AAC uses a blocksize of 1024 or 960 samples, allowing more efficient coding than MP3's 576 sample blocks);
- higher coding accuracy for transient signals (AAC uses a blocksize of 128 or 120 samples, allowing more accurate coding than MP3's 192 sample blocks);
- possibility to use Kaiser-Bessel derived window function to eliminate spectral leakage at the expense of widening the main lobe;
- much better handling of audio frequencies above 16 kHz;
- more flexible joint stereo (different methods can be used in different frequency ranges);
- additional modules (tools) added to increase compression efficiency: TNS, backwards prediction, perceptual noise substitution (PNS), etc. These modules can be combined to constitute different encoding profiles.

Overall, the AAC format allows developers more flexibility to design codecs than MP3 does, and corrects many of the design choices made in the original MPEG-1 audio specification. This increased flexibility often leads to more concurrent encoding strategies and, as a result, to more efficient compression. This is especially true at very low bit rates where the superior stereo coding, pure MDCT, and better transform window sizes leave MP3 unable to compete.

### Adoption

While the MP3 format has near-universal hardware and software support, primarily because MP3 was the format of choice during the crucial first few years of widespread music file-sharing/distribution over the internet, AAC remained a strong contender due to some unwavering industry support. Due to MP3's dominance, adoption of AAC was initially slow. The first commercialization was in 1997 when AT&T Labs (a co-owner of AAC patents) launched a digital music store with songs encoded in MPEG-2 AAC. HomeBoy for Windows was one of the earliest available AAC encoders and decoders.

Dolby Laboratories came in charge of AAC licensing in 2000. A new licensing model was launched by Dolby in 2002, while Nokia became a fifth co-licenser of the format. Dolby itself also marketed its own coding format, Dolby AC-3.

Nokia started supporting AAC playback on devices as early as 2001, but it was the exclusive use of AAC by Apple Computer for their iTunes Store which accelerated attention to AAC. Soon the format was also supported by Sony for their PlayStation Portable (albeit Sony continued promoting its proprietary ATRAC), and music-oriented cell phones from Sony Ericsson, beginning with the Sony Ericsson W800. The Windows Media Audio (WMA) format, from Microsoft, was considered to be AAC's main competitor.

By 2017, AAC was considered to have become a *de facto* industry standard for lossy audio.

## Functionality

AAC is a wideband audio coding algorithm that exploits two primary coding strategies to dramatically reduce the amount of data needed to represent high-quality digital audio: signal components that are perceptually irrelevant are discarded, and redundancies in the coded audio signal are eliminated.

The encoding process begins by converting the signal from the time domain to the frequency domain using forward modified discrete cosine transform (MDCT), accomplished via filter banks that take an appropriate number of time samples and convert them to frequency samples. The frequency-domain signal is then quantized based on a psychoacoustic model and encoded. Internal error correction codes are subsequently added before the signal is stored or transmitted. To prevent corrupt samples, a modern implementation of the Luhn mod N algorithm is applied to each frame.

The MPEG-4 audio standard does not define a single or small set of highly efficient compression schemes but rather a complex toolbox to perform a wide range of operations from low bit rate speech coding to high-quality audio coding and music synthesis.

- The MPEG-4 audio coding algorithm family spans the range from low bit rate speech encoding (down to 2 kbit/s) to high-quality audio coding (at 64 kbit/s per channel and higher).
- AAC offers sampling frequencies between 8 kHz and 96 kHz and any number of channels between 1 and 48.
- In contrast to MP3's hybrid filter bank, AAC uses the modified discrete cosine transform (MDCT) together with the increased window lengths of 1024 or 960 points.

AAC encoders can switch dynamically between a single MDCT block of length 1024 points or 8 blocks of 128 points (or between 960 points and 120 points, respectively).

- If a signal change or a transient occurs, 8 shorter windows of 128/120 points each are chosen for their better temporal resolution.
- By default, the longer 1024-point/960-point window is otherwise used because the increased frequency resolution allows for a more sophisticated psychoacoustic model, resulting in improved coding efficiency.

### Modular encoding

AAC takes a modular approach to encoding. Depending on the complexity of the bitstream to be encoded, the desired performance and the acceptable output, implementers may create profiles to define which of a specific set of tools they want to use for a particular application.

The MPEG-2 Part 7 standard (Advanced Audio Coding) was first published in 1997 and offers three default profiles:

- **Low Complexity (LC)** – the simplest and most widely used and supported
- **Main Profile (Main)** – like the LC profile, with the addition of backwards prediction
- **Scalable Sample Rate (SSR)** a.k.a. Sample-Rate Scalable (SRS)

The MPEG-4 Part 3 standard (MPEG-4 Audio) defined various new compression tools (a.k.a. Audio Object Types) and their usage in brand new profiles. AAC is not used in some of the MPEG-4 Audio profiles. The MPEG-2 Part 7 AAC LC profile, AAC Main profile and AAC SSR profile are combined with Perceptual Noise Substitution and defined in the MPEG-4 Audio standard as Audio Object Types (under the name AAC LC, AAC Main and AAC SSR). These are combined with other Object Types in MPEG-4 Audio profiles. Here is a list of some audio profiles defined in the MPEG-4 standard:

- **Main Audio Profile** – defined in 1999, uses most of the MPEG-4 Audio Object Types (AAC Main, AAC-LC, AAC-SSR, AAC-LTP, AAC Scalable, TwinVQ, CELP, HVXC, TTSI, Main synthesis)
- **Scalable Audio Profile** – defined in 1999, uses AAC-LC, AAC-LTP, AAC Scalable, TwinVQ, CELP, HVXC, TTSI
- **Speech Audio Profile** – defined in 1999, uses CELP, HVXC, TTSI
- **Synthetic Audio Profile** – defined in 1999, TTSI, Main synthesis
- **High Quality Audio Profile** – defined in 2000, uses AAC-LC, AAC-LTP, AAC Scalable, CELP, ER-AAC-LC, ER-AAC-LTP, ER-AAC Scalable, ER-CELP
- **Low Delay Audio Profile** – defined in 2000, uses CELP, HVXC, TTSI, ER-AAC-LD, ER-CELP, ER-HVXC
- **Low Delay AAC v2** – defined in 2012, uses AAC-LD, AAC-ELD and AAC-ELDv2
- **Mobile Audio Internetworking Profile** – defined in 2000, uses ER-AAC-LC, ER-AAC-Scalable, ER-TwinVQ, ER-BSAC, ER-AAC-LD
- **AAC Profile** – defined in 2003, uses AAC-LC
- **High Efficiency AAC Profile** – defined in 2003, uses AAC-LC, SBR
- **High Efficiency AAC v2 Profile** – defined in 2006, uses AAC-LC, SBR, PS
- **Extended High Efficiency AAC xHE-AAC** – defined in 2012, uses USAC

One of many improvements in MPEG-4 Audio is an Object Type called Long Term Prediction (LTP), which is an improvement of the Main profile using a forward predictor with lower computational complexity.

### AAC error protection toolkit

Applying error protection enables error correction up to a certain extent. Error correcting codes are usually applied equally to the whole payload. However, since different parts of an AAC payload show different sensitivity to transmission errors, this would not be a very efficient approach.

The AAC payload can be subdivided into parts with different error sensitivities.

- Independent error correcting codes can be applied to any of these parts using the Error Protection (EP) tool defined in MPEG-4 Audio standard.
- This toolkit provides the error correcting capability to the most sensitive parts of the payload in order to keep the additional overhead low.
- The toolkit is backwardly compatible with simpler and pre-existing AAC decoders. A great deal of the toolkit's error correction functions are based around spreading information about the audio signal more evenly in the datastream.

### Error Resilient (ER) AAC

Error Resilience (ER) techniques can be used to make the coding scheme itself more robust against errors.

For AAC, three custom-tailored methods were developed and defined in MPEG-4 Audio

- **Huffman Codeword Reordering (HCR)** to avoid error propagation within spectral data
- **Virtual Codebooks (VCB11)** to detect serious errors within spectral data
- **Reversible Variable Length Code (RVLC)** to reduce error propagation within scale factor data

### AAC Low Delay

The audio coding standards **MPEG-4 Low Delay** (AAC-LD), **Enhanced Low Delay** (AAC-ELD), and **Enhanced Low Delay v2** (AAC-ELDv2) as defined in ISO/IEC 14496-3:2009 and ISO/IEC 14496-3:2009/Amd 3 are designed to combine the advantages of perceptual audio coding with the low delay necessary for two-way communication. They are closely derived from the MPEG-2 Advanced Audio Coding (AAC) format. AAC-ELD is recommended by GSMA as super-wideband voice codec in the IMS Profile for High Definition Video Conference (HDVC) Service.

## Licensing and patents

No licenses or payments are required for a user to stream or distribute audio in AAC format. This reason alone might have made AAC a more attractive format to distribute audio than its predecessor MP3, particularly for streaming audio (such as Internet radio) depending on the use case.

However, a patent license is required for all manufacturers or developers of AAC "end-user" codecs. The terms (as disclosed to SEC) use per-unit pricing. In the case of software, each computer running the software is to be considered a separate "unit".

It used to be common for free and open source software implementations such as FFmpeg and FAAC to only be distributed in source code form so as to not "otherwise supply" an AAC codec. However, FFmpeg has since become more lenient on patent matters: the "gyan.dev" builds recommended by the official site now contain its AAC codec, with the FFmpeg legal page stating that patent law conformance is the user's responsibility. (See below under Products that support AAC, Software.) The Fedora Project, a community backed by Red Hat, imported the "Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android" to its repositories on September 25, 2018, and has enabled FFmpeg's native AAC encoder and decoder for its ffmpeg-free package on January 31, 2023.

The AAC patent holders include Bell Labs, Dolby, ETRI, Fraunhofer, JVC Kenwood, LG Electronics, Microsoft, NEC, NTT (and its subsidiary NTT Docomo), Panasonic, Philips and Sony. Based on the list of patents from the SEC terms, the last baseline AAC patent expires in 2028, and the last patent for all AAC extensions mentioned expires in 2031.

## Extensions and improvements

Some extensions have been added to the first AAC standard (defined in MPEG-2 Part 7 in 1997):

- **Perceptual Noise Substitution (PNS)**, added in MPEG-4 in 1999. It allows the coding of noise as pseudorandom data.
- **Long Term Predictor (LTP)**, added in MPEG-4 in 1999. It is a forward predictor with lower computational complexity.
- **Error Resilience (ER)**, added in MPEG-4 Audio version 2 in 2000, used for transport over error prone channels
- **AAC-LD** (Low Delay), defined in 2000, used for real-time conversation applications
- **High Efficiency AAC (HE-AAC)**, a.k.a. aacPlus v1 or AAC+, the combination of SBR (Spectral Band Replication) and AAC LC. Used for low bitrates. Defined in 2003.
- **HE-AAC v2**, a.k.a. aacPlus v2, eAAC+ or Enhanced aacPlus, the combination of Parametric Stereo (PS) and HE-AAC; used for even lower bitrates. Defined in 2004 and 2006.
- **xHE-AAC**, extends the operating range of the codec from 12 to 300 kbit/s.
- **MPEG-4 Scalable to Lossless (SLS)**, Not yet published, can supplement an AAC stream to provide a lossless decoding option, such as in Fraunhofer IIS's "HD-AAC" product
- **MPEG-4 Audio Lossless Coding (ALC)**

## Container formats

In addition to the MP4, 3GP and other container formats based on ISO base media file format for file storage, AAC audio data was first packaged in a file for the MPEG-2 standard using Audio Data Interchange Format (ADIF), consisting of a single header followed by the raw AAC audio data blocks. However, if the data is to be streamed within an MPEG-2 transport stream, a self-synchronizing format called an **Audio Data Transport Stream** (**ADTS**) is used, consisting of a series of frames, each frame having a header followed by the AAC audio data. This file and streaming-based format are defined in MPEG-2 Part 7, but are only considered informative by MPEG-4, so an MPEG-4 decoder does not need to support either format. These containers, as well as a raw AAC stream, may bear the .aac file extension. MPEG-4 Part 3 also defines its own self-synchronizing format called a Low Overhead Audio Stream (LOAS) that encapsulates not only AAC, but any MPEG-4 audio compression scheme such as TwinVQ and ALS. This format is what was defined for use in DVB transport streams when encoders use either SBR or parametric stereo AAC extensions. However, it is restricted to only a single non-multiplexed AAC stream. This format is also referred to as a Low Overhead Audio Transport Multiplex (LATM), which is just an interleaved multiple stream version of a LOAS.

## Encoders and decoders

### Tools

#### Apple AAC

Apple's AAC encoder was first part of the QuickTime media framework but is now part of Audio Toolbox.

#### FAAC and FAAD2

FAAC and FAAD2 stand for Freeware Advanced Audio Coder and Decoder 2 respectively. FAAC supports audio object types LC, Main and LTP. FAAD2 supports audio object types LC, Main, LTP, SBR and PS. Although FAAD2 is free software, FAAC is not free software.

#### Fraunhofer FDK AAC

A Fraunhofer-authored open-source encoder/decoder included in Android has been ported to other platforms. FFmpeg's native AAC encoder does not support HE-AAC and HE-AACv2, but GPL 2.0+ of ffmpeg is not compatible with FDK AAC, hence ffmpeg with libfdk-aac is not redistributable. The QAAC encoder that is using Apple's Core Media Audio is still higher quality than FDK.

#### FFmpeg and Libav

The native AAC encoder created in FFmpeg's libavcodec, and forked with Libav, was considered experimental and poor. A significant amount of work was done for the 3.0 release of FFmpeg (February 2016) to make its version usable and competitive with the rest of the AAC encoders. Libav has not merged this work and continues to use the older version of the AAC encoder. These encoders are LGPL-licensed open-source and can be built for any platform that the FFmpeg or Libav frameworks can be built.

Both FFmpeg and Libav can use the Fraunhofer FDK AAC library via libfdk-aac, and while the FFmpeg native encoder has become stable and good enough for common use, FDK is still considered the highest quality encoder available for use with FFmpeg. Libav also recommends using FDK AAC if it is available. FFmpeg 4.4 and above can also use the Apple audiotoolbox encoder.

Although the native AAC encoder only produces AAC-LC, ffmpeg's native decoder is able to deal with a wide range of input formats.

#### Nero Digital Audio

In May 2006, Nero AG released an AAC encoding tool free of charge, *Nero Digital Audio* (the AAC codec portion has become Nero AAC Codec), which is capable of encoding LC-AAC, HE-AAC and HE-AAC v2 streams. The tool is a command-line interface tool only. A separate utility is also included to decode to PCM WAV.

Various tools including the foobar2000 audio player and MediaCoder can provide a GUI for this encoder.

### Media players

Almost all current computer media players include built-in decoders for AAC, or can utilize a library to decode it. On Microsoft Windows, DirectShow can be used this way with the corresponding filters to enable AAC playback in any DirectShow based player. Mac OS X supports AAC via the QuickTime libraries. Adobe Flash Player, since version 9 update 3, can also play back AAC streams. Since Flash Player is also a browser plugin, it can play AAC files through a browser as well.

The Rockbox open source firmware (available for multiple portable players) also offers support for AAC to varying degrees, depending on the model of player and the AAC profile.

Optional iPod support (playback of unprotected AAC files) for the Xbox 360 is available as a free download from Xbox Live.

The following is a non-comprehensive list of other software player applications:

- 3ivx MPEG-4: a suite of DirectShow and QuickTime plugins which support AAC encoding or AAC/ HE-AAC decoding in any DirectShow application
- CorePlayer: also supports LC and HE AAC
- ffdshow: a free open source DirectShow filter for Microsoft Windows that uses FAAD2 to support AAC decoding
- foobar2000: a freeware audio player for Windows that supports LC and HE AAC
- KMPlayer
- MediaMonkey
- AIMP
- Media Player Classic Home Cinema
- mp3tag
- MPlayer or xine: often used as AAC decoders on Linux or Macintosh
- MusicBee: an advanced music manager and player that also supports encoding and ripping through a plugin
- RealPlayer: includes RealNetworks' RealAudio 10 AAC encoder
- Songbird: supports AAC on Windows, Linux and Mac OS X, including the DRM rights management encoding used for purchased music from the iTunes Store, with a plug-in
- Sony SonicStage
- VLC media player: supports playback and encoding of MP4 and raw AAC files
- Winamp for Windows: includes an AAC encoder that supports LC and HE AAC
- Windows Media Player 12: released with Windows 7, supports playback of AAC files natively
- Another Real: Rhapsody supports the RealAudio AAC codec, in addition to offering subscription tracks encoded with AAC
- XBMC: supports AAC (both LC and HE).
- XMMS: supports MP4 playback using a plugin provided by the faad2 library

Some of these players (e.g., foobar2000, Winamp, and VLC) also support the decoding of ADTS (Audio Data Transport Stream) using the SHOUTcast protocol. Plug-ins for Winamp and foobar2000 enable the creation of such streams.

### Use in HDTV broadcasting

#### Japanese ISDB-T

In December 2003, Japan started broadcasting terrestrial DTV ISDB-T standard that implements MPEG-2 video and MPEG-2 AAC audio. In April 2006 Japan started broadcasting the ISDB-T mobile sub-program, called 1seg, that was the first implementation of video H.264/AVC with audio HE-AAC in Terrestrial HDTV broadcasting service on the planet.

#### International ISDB-Tb

In December 2007, Brazil started broadcasting terrestrial DTV standard called International ISDB-Tb that implements video coding H.264/AVC with audio AAC-LC on main program (single or multi) and video H.264/AVC with audio HE-AACv2 in the 1seg mobile sub-program.

#### DVB

The ETSI, the standards governing body for the DVB suite, supports AAC, HE-AAC and HE-AAC v2 audio coding in DVB applications since at least 2004. DVB broadcasts which use the H.264 compression for video normally use HE-AAC for audio.

### Hardware

#### iTunes and iPod

In April 2003, Apple brought mainstream attention to AAC by announcing that its iTunes and iPod products would support songs in MPEG-4 AAC format (via a firmware update for older iPods). Customers could download music in a closed-source digital rights management (DRM)-restricted form of 128 kbit/s AAC (see FairPlay) via the iTunes Store or create files without DRM from their own CDs using iTunes. In later years, Apple began offering music videos and movies, which also use AAC for audio encoding.

On May 29, 2007, Apple began selling songs and music videos from participating record labels at higher bitrate (256 kbit/s cVBR) and free of DRM, a format dubbed "iTunes Plus" . These files mostly adhere to the AAC standard and are playable on many non-Apple products but they do include custom iTunes information such as album artwork and a purchase receipt, so as to identify the customer in case the file is leaked out onto peer-to-peer networks. It is possible, however, to remove these custom tags to restore interoperability with players that conform strictly to the AAC specification. As of January 6, 2009, nearly all music on the USA regioned iTunes Store became DRM-free, with the remainder becoming DRM-free by the end of March 2009.

iTunes offers a "Variable Bit Rate" encoding option which encodes AAC tracks in the Constrained Variable Bitrate scheme (a less strict variant of ABR encoding); the underlying QuickTime API does offer a true VBR encoding profile however.

As of September 2009, Apple has added support for HE-AAC (which is fully part of the MP4 standard) only for radio streams, not file playback, and iTunes still lacks support for true VBR encoding.

#### Other portable players

- Archos
- Cowon (unofficially supported on some models)
- Creative Zen Portable
- Fiio (all current models)
- Nintendo 3DS
- Nintendo DSi
- Philips GoGear Muse
- PlayStation Portable (PSP) with firmware 2.0 or greater
- Samsung YEPP
- SanDisk Sansa (some models)
- Walkman
- Zune
- Any portable player that fully supports the Rockbox third party firmware

#### Mobile phones

For a number of years, many mobile phones from manufacturers such as Nokia, Motorola, Samsung, Sony Ericsson, BenQ-Siemens and Philips have supported AAC playback. The first such phone was the Nokia 5510 released in 2002 which also plays MP3s. However, this phone was a commercial failure and such phones with integrated music players did not gain mainstream popularity until 2005 when the trend of having AAC as well as MP3 support continued. Most new smartphones and music-themed phones support playback of these formats.

- **Sony Ericsson** phones support various AAC formats in MP4 container. AAC-LC is supported in all phones beginning with K700, phones beginning with W550 have support of HE-AAC. The latest devices such as the P990, K610, W890i and later support HE-AAC v2.
- **Nokia XpressMusic** and other new generation Nokia multimedia phones like N- and E-Series also support AAC format in LC, HE, M4A and HEv2 profiles. These also supports playing LTP-encoded AAC audio.
- **BlackBerry** phones running the BlackBerry 10 operating system support AAC playback natively. Select previous generation BlackBerry OS devices also support AAC.
- **bada OS**
- **Apple's iPhone** supports AAC and FairPlay protected AAC files formerly used as the default encoding format in the iTunes Store until the removal of DRM restrictions in March 2009.
- **Android** 2.3 and later supports AAC-LC, HE-AAC and HE-AAC v2 in MP4 or M4A containers along with several other audio formats. Android 3.1 and later supports raw ADTS files. Android 4.1 can encode AAC.
- **WebOS** by HP/Palm supports AAC, AAC+, eAAC+, and .m4a containers in its native music player as well as several third-party players. However, it does not support Apple's FairPlay DRM files downloaded from iTunes.
- **Windows Phone**'s Silverlight runtime supports AAC-LC, HE-AAC and HE-AAC v2 decoding.

#### Other devices

- **Apple's iPad**: Supports AAC and FairPlay protected AAC files used as the default encoding format in the iTunes Store
- **Palm OS PDAs**: Many Palm OS based PDAs and smartphones can play AAC and HE-AAC with the 3rd party software Pocket Tunes. Version 4.0, released in December 2006, added support for native AAC and HE-AAC files. The AAC codec for TCPMP, a popular video player, was withdrawn after version 0.66 due to patent issues, but can still be downloaded from sites other than corecodec.org. CorePlayer, the commercial follow-on to TCPMP, includes AAC support. Other Palm OS programs supporting AAC include Kinoma Player and AeroPlayer.
- **Windows Mobile**: Supports AAC either by the native Windows Media Player or by third-party products (TCPMP, CorePlayer)
- **Epson**: Supports AAC playback in the P-2000 and P-4000 Multimedia/Photo Storage Viewers
- **Sony Reader**: plays M4A files containing AAC, and displays metadata created by iTunes. Other Sony products, including the A and E series Network Walkmans, support AAC with firmware updates (released May 2006) while the S series supports it out of the box.
- **Sonos Digital Media Player**: supports playback of AAC files
- **Barnes & Noble Nook Color**: supports playback of AAC encoded files
- **Roku SoundBridge**: a network audio player, supports playback of AAC encoded files
- **Squeezebox**: network audio player (made by Slim Devices, a Logitech company) that supports playback of AAC files
- **PlayStation 3**: supports encoding and decoding of AAC files
- **Xbox 360**: supports streaming of AAC through the Zune software, and of supported iPods connected through the USB port
- **Wii**: supports AAC files through version 1.1 of the Photo Channel as of December 11, 2007. All AAC profiles and bitrates are supported as long as it is in the .m4a file extension. The 1.1 update removed MP3 compatibility, but according to Nintendo, users who have installed this may freely downgrade to the old version if they wish.
- **Livescribe Pulse and Echo Smartpens**: record and store audio in AAC format. The audio files can be replayed using the pen's integrated speaker, attached headphones, or on a computer using the Livescribe Desktop software. The AAC files are stored in the user's "My Documents" folder of the Windows OS and can be distributed and played without specialized hardware or software from Livescribe.
- **Google Chromecast**: supports playback of LC-AAC and HE-AAC audio

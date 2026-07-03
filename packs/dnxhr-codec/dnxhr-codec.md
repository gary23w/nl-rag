---
title: "DNxHR codec"
source: https://en.wikipedia.org/wiki/DNxHR_codec
domain: dnxhr-codec
license: CC-BY-SA-4.0
tags: dnxhr codec
fetched: 2026-07-03
---

# DNxHR codec

**Avid DNxHR**, which stands for "**D**igital **N**onlinear E**x**tensible **H**igh **R**esolution", is a lossy mezzanine (post-production) codec engineered for multi-generation compositing with reduced storage and bandwidth requirements. It is not intended as a distribution codec like H.264 or AV1. Avid DNxHR supersedes (completely contains) the older Avid DNxHD codec and was rebranded in 2025 under the unified term "Avid DNx".

## History

Avid DNx was originally introduced as Avid DNxHD in 2004 as a proprietary Constant Bitrate (CBR) codec, supported in Avid products like Avid MediaComposer. It was standardized by SMPTE (Society of Motion Picture and Television Engineers) in 2008 as SMPTE ST 2019-1 (VC-3), covering HD resolutions in YCbCr color encoding and wrapping the codec in MXF and MOV (QuickTime File Format) containers.

The 2014 revision of SMPTE ST 2019-1 (VC-3) added encoding directly in the RGB color model, allowing the codec to store graphic content without the need to convert to YCbCr representation, either externally or internally, as typically required by other codecs such as Apple ProRes.

On September 12, 2014, Avid Technology, Inc. announced the DNxHR (**H**igh **R**esolution) codec as part of a broader "Avid Resolution Independence" announcement at their Fall 2014 Avid Connect event, which was held during the IBC 2014 conference in Amsterdam, Netherlands.

DNxHR was formally standardized with the publication of the 2016 revision of SMPTE ST 2019-1 (VC-3), where DNxHR corresponded to the newly introduced **R**esolution **I**ndependent (RI) profile. It extended the resolution coverage from HD to support any resolution between 2x2 and 16384x16384 pixels, most importantly including support for the emerging 2K, 4K and 8K resolutions, as well as adding support for an optional alpha channel (lossy or lossless) and Variable Bitrate (VBR) encoding.

In 2021 Avid DNxHR was added as production codec to the SMPTE ST 2067 suite of standard documents covering the IMF (Interoperable Master Format), allowing the codec to be used in modern post-production cycles.

In 2022 SMPTE published an to SMPTE ST 2019-1 (VC-3), which extended the support for the alpha channel into the HD profile.

At the IBC 2025 conference in Amsterdam Avid announced a rebranding of DNxHD and DNxHR to "Avid DNx", to eliminate the confusion around supported resolutions and bit depths arising from the continued and often misleading use of the HD and HR acronyms .

The pending publication of the 2026 revision of SMPTE ST 2019-1 (VC-3) adds 2 new RGB compression levels (HQ and SQ), which were previously released by Avid under the acronym "Avid DNx GX". This revision also renamed the "RI" profile to "HR", bringing this in line with industry practice based primarily on use of Avid DNx. It also generalizes the custom bitrate support to CBR mode (previously only supported in VBR mode, to stay compliant with 2016 revision of SMPTE ST 2019-1).

## Specifications

Avid DNx is a fully compliant implementation of SMPTE ST 2019-1 (VC-3). It supports 5 primary compression levels, corresponding to different bitrate ranges and compression quality levels, as found in SMPTE ST 2019-1 (VC-3).

Avid DNx can carry any color coding and supports all bit depths between 8 and 16 bits for filler and lossy alpha.

- **444**: 4:4:4 and RGB, highest quality and bitrate, lossless alpha support (VFX work and Cinema delivery).
- **HQX** (**H**igh **Q**uality e**X**tended): 4:2:2 and 4:2:0, less aggressive quantization than HQ if needed for multi-generation workflows (High-end broadcast production and delivery)
- **HQ** (**H**igh **Q**uality): RGB, 4:4:4, 4:2:2, 4:2:0, high end format for standard broadcast usage (none or few multi-generation work, specifically sports and advertising)
- **SQ** (**S**tandard **Q**uality): RGB, 4:4:4, 4:2:2, 4:2.0 , standard broadcast production usage (everyday broadcast production)
- **LB** (**L**ow **B**andwidth): 4:2:2 and 4:2:0, Proxy format for post-production work, replaced during finishing with a higher quality content representation (rough cuts and non-VFX work)

| Level | Bit Depth | Color Coding | Resolution | Sub-sampling | Bitrate Range (Mbps @ 30 FPS) |
|---|---|---|---|---|---|
| 444 | 8 through 16 | Any | up to 16384 x 16384 | 4:4:4(:4), RGB(A) | 116-440 |
| HQX | 4:2:2(:4), 4:2:0(:4) | 72-220 |   |   |   |
| HQ | 4:4:4(:4), 4:2:2(:4), 4:2:0(:4), RGB(A) | 36-220 |   |   |   |
| SQ | 4:4:4(:4), 4:2:2(:4), 4:2:0(:4), RGB(A) | 36-145 |   |   |   |
| LB | 4:2:2(:4), 4:2:0(:4) | 36-45 |   |   |   |

*Table showing format support in Avid DNx as shown in*.

Users first select a *Level* based on the high-level quality aspects (aggressiveness of the quantization matrix). Within this Level they can then select any target bitrate within the specified *Bitrate Range.*

Up to the 2026 revision of SMPTE ST 2019-1 this adjustable bitrate feature required the use of the VBR flag. It has now been generalized this to also cover CBR bitstreams.

## Trademarks

"Avid DNx", "Avid DNxHD", "Avid DNxHR", "DNxHD" and "DNxHR" are trademarks owned by Avid Technology.

## Support

Avid DNx is primarily supported through the Avid DNx SDK, published and licensed by Avid Technology. The SDK is the only complete implementation of the standard. Reference decoder software (un-optimized) is also available through SMPTE . The SDK supports all major platforms (Windows Intel, Windows ARM (Neon), Windows ARM EC, Linux Intel, MacOS Intel, MacOS ARM (Neon)).

In software VC-3 is also supported by FFmpeg. However this implementation is known to be incomplete, supporting primarily the HD resolutions of the original 2008 version of the VC-3 standard, frequently refusing operations for options introduced later (including most of the DNxHR options).

Hardware implementations of Avid DNx are available from several vendors, like for example Atomos.

Avid DNx is supported by all major editing applications, including Avid Media Composer, Adobe Premiere Pro, Blackmagic Design Resolve and Apple Final Cut Pro. Avid DNx is licensed to a wide range of application providers.

## Uses

Avid DNx is widely used in the cinematic and high-end broadcast productions, which have specific post production requirements.

The I-frame format used by the codec encodes each frame independently. Unlike distribution codecs like like H.264 or AV1, which rely on inter-frame (GOP codecs) compression technologies and which very efficiently reduce the bandwidth required to transmit high quality content to end users in streaming applications the codec requires significantly more storage space to achieve the same encoding quality. This is an explicit tradeoff accepted in production, because it allows to maintain quality in specific operations found frequently in post production:

- Each frame can be individually and instantly accessed. Only a single frame needs to be retrieved and decoded, allowing the fastest possible reaction to random access user actions as found in editing applications, when searching for a specific frame where to introduce a cut or position an effect (scrubbing). GOP codecs require considerably more overhead and introduce decoding latency, because to access a single frame multiple frames need to be decoded, although a lot of these negative impacts can be countered by ample caching.
- In the default CBR mode SMPTE ST 2019-1 (VC-3) has exact frame size requirements: Each frame must be exactly the same compressed size within the bitstream. This enables features not possible with other production codecs like e.g. Apple ProRes, which only offers VBR operations:
  - All frames in the bitstream can be accessed without the need to use and maintain an expensive frame index, further improving random access speed.
  - Frames can be modified and/or replaced in an existing bitstream without the need to re-encode parts or the entire bitstream. In file-based broadcast workflows frames can still be changed in the file shortly (seconds) before they go "on air", if e.g. a face needs to be made unrecognizable through barring or blurring. For GOP-based or VBR codecs either the entire file or at least the part following the modification needs to be recreated because of the change of compressed size of the frames. In GOP-based codecs an additional constraint becomes a major inhibitor: Frames can only be modified as part of a group (entire GOP), and Open-GOP structures may even require entire segments, spanning multiple GOPs, to be re-encoded.
  - Bitstreams can be rendered in parallel: Because the final position within the bitstream is fully predictable before the frames have been encoded, the bitstream does not have to be encoded sequentially. Different areas of the bitstream can be encoded in parallel without having to resort to intermediate storage solutions with a subsequent stream-merge operation.
- The absence of an encoding latency allows frames being accessed for decoding/playback immediately after encoding. Paired with the CBR characteristic this allows instant, random access and variable speed replay, as frequently found in live sports productions.
- If the number of production formats is limited, the final edited sequences can be finished without going through a decode/encode cycle, merging the final bitstream in compressed form, frequently eliminating all of the expensive image processing requirements, avoiding a digital generation loss (quality) and reducing the overhead to a binary copy workflow.
- Even if the production formats are not exactly matching, Avid DNx allows either maintaining a binary copy or a minimal re-encode, which can be achieved within the codec itself without having to go through the (much longer) editor pipeline.

The low complexity of the codec when compared to GOP codecs, allows using a SW-based decoder, even had 4K and 8K resolutions, without the mandatory need to resort to HW-assisted decoding support. HW decoders are frequently only optimized for sustained linear real-time playback of a single stream, limiting their use in non-linear editing applications: Editing requires stable, concurrent playback of at least 2 streams (single-track dissolve), more streams if multi-layered compositing is being used and many concurrent streams for multi-camera editing scenarios (alternate shot angles), as frequently used in professional cinematic productions, where time directly translates into operating expenses:

For low budget or personal productions time and limited storage space are usually the most effective cost-reduction factors, while in professional productions time-to-market frequently outweighs all other concerns. For professional applications being able to edit on virtually any computing platform without the need for expensive, dedicated studio equipment with virtually no wait limitations is usually deemed vastly more cost effective, as personnel waiting for hardware (recurring) is usually more expensive than re-usable hardware investments.

In cinematic productions, specifically if VFX heavy, a single finished shot frequently goes through many processing generations, with content frequently getting exchanged multiple times between specialized finishing applications. The exchange usually happens in file form, requiring multiple encodings of the content and preservations of associated production metadata. Reliance on the professional market focused MXF file format, which stresses the importance of the latter in professional productions, complements the encoder design, which was specifically designed to provide high multi-generation resistance.

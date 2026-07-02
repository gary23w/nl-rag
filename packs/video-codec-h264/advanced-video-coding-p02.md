---
title: "Advanced Video Coding (part 2/2)"
source: https://en.wikipedia.org/wiki/Advanced_Video_Coding
domain: video-codec-h264
license: CC-BY-SA-4.0
tags: h.264 codec, advanced video coding, cabac entropy, motion compensation
fetched: 2026-07-02
part: 2/2
---

## Implementations

In 2009, the HTML5 working group was split between supporters of Ogg Theora, a free video format which is thought to be unencumbered by patents, and H.264, which contains patented technology. As late as July 2009, Google and Apple were said to support H.264, while Mozilla and Opera support Ogg Theora (eventually Google, Mozilla and Opera all supported Theora and WebM with VP8, although Theora support was removed in 2023–2024). Microsoft, with the release of Internet Explorer 9, has added support for HTML 5 video encoded using H.264. At the Gartner Symposium/ITXpo in November 2010, Microsoft CEO Steve Ballmer answered the question "HTML 5 or Silverlight?" by saying "If you want to do something that is universal, there is no question the world is going HTML5." In January 2011, Google announced that they were pulling support for H.264 from their Chrome browser and supporting both Theora and WebM/VP8 to use only open formats.

On March 18, 2012, Mozilla announced support for H.264 in Firefox on mobile devices, due to prevalence of H.264-encoded video and the increased power-efficiency of using dedicated H.264 decoder hardware common on such devices. On February 20, 2013, Mozilla implemented support in Firefox for decoding H.264 on Windows 7 and above. This feature relies on Windows' built in decoding libraries. Firefox 35.0, released on January 13, 2015, supports H.264 on OS X 10.6 and higher.

On October 30, 2013, Rowan Trollope from Cisco Systems announced that Cisco would release both binaries and source code of an H.264 video codec called OpenH264 under the Simplified BSD license, and pay all royalties for its use to MPEG LA for any software projects that use Cisco's precompiled binaries, thus making Cisco's OpenH264 *binaries* free to use. However, any software projects that use Cisco's source code instead of its binaries would be legally responsible for paying all royalties to MPEG LA. Target CPU architectures include x86 and ARM, and target operating systems include Linux, Windows XP and later, Mac OS X, and Android; iOS was notably absent from this list, because it does not allow applications to fetch and install binary modules from the Internet. Also on October 30, 2013, Brendan Eich from Mozilla wrote that it would use Cisco's binaries in future versions of Firefox to add support for H.264 to Firefox where platform codecs are not available. Cisco published the source code to OpenH264 on December 9, 2013.

Although iOS was not supported by the 2013 Cisco software release, Apple updated its Video Toolbox Framework with iOS 8 (released in September 2014) to provide direct access to hardware-based H.264/AVC video encoding and decoding.

### Software encoders

AVC software implementations

Feature

QuickTime

Nero

OpenH264

x264

Main-

Concept

Elecard

TSE

Pro-

Coder

Avivo

Elemental

IPP

B slices

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Multiple reference frames

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Interlaced coding (PicAFF, MBAFF)

No

MBAFF

MBAFF

MBAFF

Yes

Yes

No

Yes

MBAFF

Yes

No

CABAC entropy coding

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

8×8 vs. 4×4 transform adaptivity

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Quantization scaling matrices

No

No

Yes

Yes

Yes

No

No

No

No

No

No

Separate C

B

and C

R

QP control

No

No

Yes

Yes

Yes

Yes

No

No

No

No

No

Extended chroma formats

No

No

No

4:0:0

4:2:0

4:2:2

4:4:4

4:2:2

4:2:2

4:2:2

No

No

4:2:0

4:2:2

No

Largest sample depth (bit)

8

8

8

10

10

8

8

8

8

10

12

Predictive lossless coding

No

No

No

Yes

No

No

No

No

No

No

No

### Hardware

Because H.264 encoding and decoding require significant computational power for specific arithmetic operations, software implementations running on general-purpose CPUs are typically less power-efficient. However, consumer-grade CPUs with 6 or 8 cores since around 2016, and quad-core general-purpose x86 CPUs as of January 2020 have sufficient computation power to perform real-time SD and HD encoding. Compression efficiency depends on video algorithmic implementations, not on whether hardware or software implementation is used. Therefore, the difference between hardware and software based implementation is more on power-efficiency, flexibility and cost. To improve the power efficiency and reduce hardware form-factor, special-purpose hardware may be employed, either for the complete encoding or decoding process, or for acceleration assistance within a CPU-controlled environment.

CPU based solutions are known to be much more flexible, particularly when encoding must be done concurrently in multiple formats, multiple bit rates and resolutions (multi-screen video), and possibly with additional features on container format support, advanced integrated advertising features, etc. CPU based software solution generally makes it much easier to load balance multiple concurrent encoding sessions within the same CPU.

The 2nd generation Intel "Sandy Bridge" Core i3/i5/i7 processors introduced at the January 2011 CES (Consumer Electronics Show) offer an on-chip hardware full HD H.264 encoder, known as Intel Quick Sync Video.

A hardware H.264 encoder can be an ASIC or an FPGA.

ASIC encoders with H.264 encoder functionality are available from many different semiconductor companies, but the core design used in the ASIC is typically licensed from one of a few companies such as Chips&Media, Allegro DVT, On2 (formerly Hantro, acquired by Google), Imagination Technologies, NGCodec. Some companies have both FPGA and ASIC product offerings.

Texas Instruments manufactures a line of ARM + DSP cores that perform DSP H.264 BP encoding 1080p at 30 fps. This permits flexibility with respect to codecs (which are implemented as highly optimized DSP code) while being more efficient than software on a generic CPU.


## Licensing

In countries where patents on software algorithms are upheld, vendors and commercial users of products that use H.264/AVC are expected to pay patent licensing royalties for the patented technology that their products use. This applies to the Baseline Profile as well.

A private organization known as Via-LA administers the licenses for patents applying to this standard, as well as other patent pools, such as for MPEG-4 Part 2 Video, HEVC and MPEG-DASH. The patent holders include Fujitsu, Panasonic, Sony, Mitsubishi, Apple, Columbia University, KAIST, Dolby, Google, JVC Kenwood, LG Electronics, Microsoft, NTT Docomo, Philips, Samsung, Sharp, Toshiba and ZTE, although the majority of patents in the pool are held by Panasonic (1,197 patents), Godo Kaisha IP Bridge (1,130 patents) and LG Electronics (990 patents).

On August 26, 2010, MPEG-LA announced that royalties would not be charged for H.264 encoded Internet video that is free to end users. All other royalties remain in place, such as royalties for products that decode and encode H.264 video as well as to operators of free television and subscription channels. The license terms are updated in 5-year blocks.

Since the first version of the standard was completed in May 2003 (23 years ago) and the most commonly used profile (the High profile) was completed in June 2004 (21–22 years ago), some of the relevant patents are expired by now, while others are still in force in jurisdictions around the world and one of the US patents in the MPEG LA H.264 pool (granted in 2016) lasts at least until November 2030.

In 2005, Qualcomm sued Broadcom in US District Court, alleging that Broadcom infringed on two of its patents by making products that were compliant with the H.264 video compression standard. In 2007, the District Court found that the patents were unenforceable because Qualcomm had failed to disclose them to the JVT prior to the release of the H.264 standard in May 2003. In December 2008, the US Court of Appeals for the Federal Circuit affirmed the District Court's order that the patents be unenforceable but remanded to the District Court with instructions to limit the scope of unenforceability to H.264 compliant products.

In October 2023 Nokia sued HP and Amazon for H.264/H.265 patent infringement in USA, UK and other locations.

In February 2026, the VIA Licensing Authority announced a new licensing scheme targeting video streaming that applies to version 4 of the h264 specification and later. This changes the terms for new licensees after January 2026.

---
title: "AV1 - Wikipedia"
source: https://en.wikipedia.org/wiki/AV1
domain: av2-codec
license: CC-BY-SA-4.0
tags: aomedia av2, av2 codec, av1 successor codec, royalty-free video coding
fetched: 2026-07-02
---

# AV1

**AOMedia Video 1** (**AV1**) is an open, royalty-free video coding format initially designed for video transmissions over the Internet. It was developed as a successor to VP9 by the Alliance for Open Media (AOMedia), a consortium founded in 2015 that includes semiconductor firms, video on demand providers, video content producers, software development companies and web browser vendors. The AV1 bitstream specification includes a reference video codec. In 2018, Facebook re-encoded 400 compressed Facebook videos with AV1, VP9, and x264 and found AV1 delivered around 34% lower bitrates than VP9 and about 50% lower than x264 at similar visual quality, though encoding was much slower.

Like VP9, but unlike H.264 (AVC) and H.265 (HEVC), AV1 has a royalty-free licensing model that does not hinder adoption in open-source projects.

AVIF is an image file format that uses AV1 compression algorithms.

## History

The Alliance's motivations for creating AV1 included the high cost and uncertainty involved with the patent licensing of HEVC (also known as H.265), the MPEG-designed codec expected to succeed AVC. Additionally, the Alliance's seven founding members – Amazon, Cisco, Google, Intel, Microsoft, Mozilla, and Netflix – announced that the initial focus of the video format would be delivery of high-quality web video. The official announcement of AV1 came with the press release on the formation of the Alliance for Open Media on 1 September 2015. Only 42 days before, on 21 July 2015, HEVC Advance's initial licensing offer was announced to be an increase over the royalty fees of its predecessor, AVC. In addition to the increased cost, the complexity of the licensing process increased with HEVC. Unlike previous MPEG standards where the technology in the standard could be licensed from a single entity, MPEG LA, when the HEVC standard was finished, two patent pools had been formed with a third pool on the horizon. In addition, various patent holders were refusing to license patents via either pool, increasing uncertainty about HEVC's licensing. According to Microsoft's Ian LeGrow, an open-source, royalty-free technology was seen as the easiest way to eliminate this uncertainty around licensing.

The negative effect of patent licensing on free and open-source software has also been cited as a reason for the creation of AV1. For example, building an H.264 implementation into Firefox would prevent it from being distributed free of charge since licensing fees would have to be paid to MPEG-LA. Free Software Foundation Europe has argued that FRAND patent licensing practices make the free software implementation of standards impossible due to various incompatibilities with free-software licenses.

Many of the components of the AV1 project were sourced from previous research efforts by Alliance members. Individual contributors had started experimental technology platforms years before: Xiph's/Mozilla's Daala published code in 2010, Google's experimental VP9 evolution project VP10 was announced on 12 September 2014, and Cisco's Thor was published on 11 August 2015. Building on the code base of VP9, AV1 incorporates additional techniques, several of which were developed in these experimental formats.

Many companies are part of Alliance for Open Media, including Samsung, Vimeo, Microsoft, Netflix, Mozilla, AMD, Nvidia, Intel, ARM, Google, Facebook, Cisco, Amazon, Hulu, VideoLAN, Adobe, and Apple. Apple is an AOMedia governing member, although it joined after the formation. The management of the AV1 streams has been officially included among the typological videos manageable by Coremedia.

The first version 0.1.0 of the AV1 reference codec was published on April 7, 2016. Although a soft feature freeze came into effect at the end of October 2017, development continued on several significant features. The bitstream format, was projected to be frozen in January 2018 but was delayed due to unresolved critical bugs as well as further changes to transformations, syntax, the prediction of motion vectors, and the completion of legal analysis. The Alliance announced the release of the AV1 bitstream specification on March 28, 2018, along with a reference, software-based encoder and decoder. On 25 June 2018, a validated version 1.0.0 of the specification was released. On January 8, 2019, a validated *version 1.0.0 with Errata 1* of the specification was released. Martin Smole from AOM member Bitmovin said that the computational efficiency was the greatest remaining challenge after the bitstream format freeze had been completed. While working on the format, the encoder was not targeted for production use and speed optimizations were not prioritized. Consequently, the early version of AV1 was orders of magnitude slower than existing HEVC encoders. Much of the development effort was consequently shifted towards improving the reference encoder. In March 2019, it was reported that the speed of the reference encoder had improved greatly and was within the same order of magnitude as encoders for other common formats.

On January 21, 2021, the MIME type of AV1 was defined as `video/AV1`. The usage of AV1 using this MIME type is restricted to Real-time Transport Protocol purposes only.

### AV2

For AOM's 10th birthday, the Alliance announced the successor to AV1 called AV2. It is designed to deliver better compression performance, enhanced support for AR, VR and split-screen usage and support for a wider visual quality range.

## Purpose

AV1 aims to be a video format for the web that is both state-of-the-art and royalty free. According to Matt Frost, head of strategy and partnerships in Google's Chrome Media team, "The mission of the Alliance for Open Media remains the same as the WebM project." A recurring concern in standards development, not least of royalty-free multimedia formats, is the danger of accidentally infringing on patents that their creators and users did not know about. This concern has been raised regarding AV1, and previously VP8, VP9, Theora and IVC. The problem is not unique to royalty-free formats, but it uniquely threatens their *status* as royalty-free.

| Patent licensing | AV1, VP9, Theora, MPEG-5 Base profile | VVC, HEVC, AVC, MPEG-5 Main profile | GIF, MP3, MPEG-1, MPEG-2, MPEG-4 Part 2 |
|---|---|---|---|
| By known patent holders | Royalty-free | Royalty bearing | Patents expired |
| By unknown patent holders | Impossible to ascertain until the format is old enough that any patents would have expired (up to 20 years in WTO countries) |   |   |

To fulfill the goal of being royalty free, the development process requires that no feature can be adopted before it has been confirmed independently by two separate parties to not infringe on patents of competing companies. In cases where an alternative to a patent-protected technique is not available, owners of relevant patents have been invited to join the Alliance (even if they were already members of another patent pool). For example, Alliance members Apple, Cisco, Google, and Microsoft are also licensors in MPEG-LA's patent pool for H.264. As an additional protection for the royalty-free status of AV1, the Alliance has a legal defense fund to aid smaller Alliance members or AV1 licensees in the event they are sued for alleged patent infringement.

Under patent rules adopted from the World Wide Web Consortium (W3C), technology contributors license their AV1-connected patents to anyone, anywhere, anytime based on reciprocity (i.e. as long as the user does not engage in patent litigation). As a defensive condition, anyone engaging in patent litigation loses the right to the patents of *all* patent holders.

This treatment of intellectual property rights (IPR), and its absolute priority during development, is contrary to extant MPEG formats like AVC and HEVC. These were developed under an IPR uninvolvement policy by their standardization organisations, as stipulated in the ITU-T's definition of an open standard. However, MPEG's chairman has argued this practice has to change, which it is: EVC is also set to have a royalty-free subset, and will have switchable features in its bitstream to defend against future IPR threats.

The creation of royalty-free web standards has been a long-stated pursuit for the industry. In 2007, the proposal for HTML video specified Theora as mandatory to implement. The reason was that public content should be encoded in freely implementable formats, if only as a "baseline format", and that changing such a baseline format later would be hard because of network effects.

The Alliance for Open Media is a continuation of Google's efforts with the WebM project, which renewed the royalty-free competition after Theora had been surpassed by AVC. For companies such as Mozilla that distribute free software, AVC can be difficult to support as a per-copy royalty is unsustainable given the lack of revenue stream to support these payments in free software (see FRAND § Excluding costless distribution). Similarly, HEVC has not successfully convinced all licensors to allow an exception for freely distributed software (see HEVC § Provision for costless software).

The performance goals include "a step up from VP9 and HEVC" in efficiency for a low increase in complexity. NETVC's efficiency goal is 25% improvement over HEVC. The primary complexity concern is for software decoding, since hardware support will take time to reach users. However, for WebRTC, live encoding performance is also relevant, which is Cisco's agenda: Cisco is a manufacturer of videoconferencing equipment, and their Thor contributions aim at "reasonable compression at only moderate complexity".

Feature-wise, AV1 is specifically designed for real-time applications (especially WebRTC) and higher resolutions (wider color gamuts, higher frame rates, UHD) than typical usage scenarios of the current generation (H.264) of video formats, where it is expected to achieve its biggest efficiency gains. It is therefore planned to support the color space from ITU-R Recommendation BT.2020 and up to 12 bits of precision per color component. AV1 is primarily intended for lossy encoding, although lossless compression is supported as well.

## Technology

AV1 is a traditional block-based frequency transform format featuring new techniques. Based on Google's VP9, AV1 incorporates additional techniques that mainly give encoders more coding options to enable better adaptation to different types of input.

The Alliance published a reference implementation written in C and assembly language (`aomenc`, `aomdec`) as free software under the terms of the BSD 2-Clause License. Development happens in public and is open for contributions, regardless of AOM membership. The development process was such that coding tools were added to the reference code base as *experiments*, controlled by flags that enable or disable them at build time, for review by other group members as well as specialized teams that helped with and ensured hardware friendliness and compliance with intellectual property rights (TAPAS). When the feature gained some support in the community, the experiment was enabled by default, and ultimately had its flag removed when all of the reviews were passed. Experiment names were lowercased in the *configure* script and uppercased in conditional compilation flags. To better and more reliably support HDR and color spaces, corresponding metadata can now be integrated into the video bitstream instead of being signaled in the container.

### Partitioning

Frame content is separated into adjacent same-sized blocks referred to as superblocks. Similar to the concept of a macroblock, superblocks are square-shaped and can either be of size 128×128 or 64×64 pixels. Superblocks can be divided in smaller blocks according to different partitioning patterns. The four-way split pattern is the only pattern whose partitions can be recursively subdivided. This allows superblocks to be divided into partitions as small as 4×4 pixels.

"T-shaped" partitioning patterns are introduced, a feature developed for VP10, as well as horizontal or vertical splits into four stripes of 4:1 and 1:4 aspect ratio. The available partitioning patterns vary according to the block size, both 128×128 and 8×8 blocks can't use 4:1 and 1:4 splits. Moreover, 8×8 blocks can't use T-shaped splits.

Two separate predictions can now be used on spatially different parts of a block using a smooth, oblique transition line (*wedge-partitioned prediction*). This enables more accurate separation of objects without the traditional staircase lines along the boundaries of square blocks.

More encoder parallelism is possible thanks to configurable prediction dependency between tile rows (`ext_tile`).

### Prediction

AV1 performs internal processing in higher precision (10 or 12 bits per sample), which leads to quality improvement by reducing rounding errors.

Predictions can be combined in more advanced ways (than a uniform average) in a block (*compound prediction*), including smooth and sharp transition gradients in different directions (*wedge-partitioned prediction*) as well as implicit masks that are based on the difference between the two predictors. This allows the combination of either two inter predictions or an inter and an intra prediction to be used in the same block.

A frame can reference 6 instead of 3 of the 8 available frame buffers for temporal (inter) prediction while providing more flexibility on bi-prediction (`ext_refs`).

The *Warped Motion* (`warped_motion`) and *Global Motion* (`global_motion`) tools in AV1 aim to reduce redundant information in motion vectors by recognizing patterns arising from camera motion. They implement ideas that were attempted in preceding formats like e.g. MPEG-4 ASP, albeit with a novel approach that works in three dimensions. There can be a set of warping parameters for a whole frame offered in the bitstream, or blocks can use a set of implicit local parameters that get computed based on surrounding blocks.

*Switch frames* (S-frame) are a new inter-frame type that can be predicted using already-decoded reference frames from a higher-resolution version of the same video to allow switching to a lower resolution without the need for a full keyframe at the beginning of a video segment in the adaptive bitrate streaming use case.

#### Intra prediction

Intra prediction consists of predicting the pixels of given blocks only using information available in the current frame. Most often, intra predictions are built from the neighboring pixels above and to the left of the predicted block. The DC predictor builds a prediction by averaging the pixels above and to the left of block.

Directional predictors extrapolate these neighboring pixels according to a specified angle. In AV1, 8 main directional modes can be chosen. These modes start at an angle of 45 degrees and increase by a step size of 22.5 degrees up until 203 degrees. Furthermore, for each directional mode, six offsets of 3 degrees can be signaled for bigger blocks, three above the main angle and three below it, resulting in a total of 56 angles (`ext_intra`).

The "TrueMotion" predictor was replaced with a Paeth predictor which looks at the difference from the known pixel in the above-left corner to the pixel directly above and directly left of the new one and then chooses the one that lies in direction of the smaller gradient as predictor. A palette predictor is available for blocks with up to 8 dominant colors, such as some computer screen content. Correlations between the luminosity and the color information can now be exploited with a predictor for chroma blocks that is based on samples from the luma plane (`cfl`), a technique borrowed from Daala. In order to reduce visible boundaries along borders of inter-predicted blocks, a technique called overlapped block motion compensation (OBMC) can be used. This involves extending a block's size so that it overlaps with neighboring blocks by 2 to 32 pixels, and blending the overlapping parts together.

### Data transformation

To transform the error remaining after prediction to the frequency domain, AV1 encoders can use square, 2:1/1:2, and 4:1/1:4 rectangular DCTs (`rect_tx`), as well as an asymmetric DST for blocks where the top and/or left edge is expected to have lower error thanks to prediction from nearby pixels, or choose to do no transform (identity transform).

It can combine two one-dimensional transforms in order to use different transforms for the horizontal and the vertical dimension (`ext_tx`).

### Quantization

AV1 has new optimized quantization matrices (`aom_qm`). The eight sets of quantization parameters that can be selected and signaled for each frame now have individual parameters for the two chroma planes and can use spatial prediction. On every new superblock, the quantization parameters can be adjusted by signaling an offset.

### Filters

In-loop filtering combines Thor's constrained low-pass filter and Daala's directional deringing filter into the *Constrained Directional Enhancement Filter*, `cdef`. This is an edge-directed conditional replacement filter that smooths blocks roughly along the direction of the dominant edge to eliminate ringing artifacts.

There is also the *loop restoration filter* (`loop_restoration`) based on the Wiener filter and self-guided restoration filters to remove blur artifacts due to block processing.

*Film grain synthesis* (`film_grain`) improves coding of noisy signals using a parametric video coding approach. Due to the randomness, inherent to film grain noise, this signal component is traditionally either very expensive to code or prone to get damaged or lost, possibly leaving serious coding artifacts as residue. This tool circumvents these problems using analysis and synthesis, replacing parts of the signal with a visually similar synthetic texture based solely on subjective visual impression instead of objective similarity. It removes the grain component from the signal, analyzes its non-random characteristics, and instead transmits only descriptive parameters to the decoder, which adds back a synthetic, pseudorandom noise signal that's shaped after the original component. It is the visual equivalent of the Perceptual Noise Substitution technique used in AC3, AAC, Vorbis, and Opus audio codecs.

### Entropy coding

Daala's entropy coder (`daala_ec`), a non-binary arithmetic coder, was selected for replacing VP9's binary entropy coder. The use of *non-binary* arithmetic coding helps evade patents but also adds bit-level parallelism to an otherwise serial process, reducing clock rate demands on hardware implementations. This is to say that the effectiveness of modern binary arithmetic coding like CABAC is being approached using a greater alphabet than binary, hence greater speed, as in Huffman code (but not as simple and fast as Huffman code). AV1 also gained the ability to adapt the symbol probabilities in the arithmetic coder per coded symbol instead of per frame (`ec_adapt`).

AV1 has provisions for temporal and spatial scalability.

## Quality and efficiency

A first comparison from the beginning of June 2016 found AV1 roughly on par with HEVC, as did one using code from late January 2017.

In April 2017, using the 8 enabled experimental features at the time (of 77 total), Bitmovin was able to demonstrate favorable objective metrics, as well as visual results, compared to HEVC on the *Sintel* and *Tears of Steel* short films. A follow-up comparison by Jan Ozer of *Streaming Media Magazine* confirmed this, and concluded that "AV1 is at least as good as HEVC now". Ozer noted that his and Bitmovin's results contradicted a comparison by Fraunhofer Institute for Telecommunications from late 2016 that had found AV1 65.7% less efficient than HEVC, underperforming even H.264/AVC which they concluded as being 10.5% more efficient. Ozer justified this discrepancy by having used encoding parameters endorsed by each encoder vendor, as well as having more features in the newer AV1 encoder. Decoding performance was at about half the speed of VP9 according to internal measurements from 2017.

Tests from Netflix in 2017, based on measurements with PSNR and VMAF at 720p, showed that AV1 was about 25% more efficient than VP9 (libvpx). Tests from Facebook conducted in 2018, based on PSNR, showed that the AV1 reference encoder was able to achieve 34%, 46.2% and 50.3% higher data compression than libvpx-vp9, x264 High profile, and x264 Main profile respectively.

Tests from Moscow State University in 2017 found that VP9 required 31% and HEVC 22% more bitrate than AV1 in order to achieve similar levels of quality. The AV1 encoder was operating at speed "2500–3500 times lower than competitors" due to the lack of optimization (which was not available at that time). Tests from University of Waterloo in 2020 found that when using a mean opinion score (MOS) for 2160p (4K) video AV1 had the bitrate saving of 9.5% compared to HEVC and 16.4% compared to VP9. They also concluded that at the time of the study at 2160p the AV1 video encodes on average took 590× longer compared to encoding with AVC; while HEVC took on average 4.2× longer and VP9 took on average 5.2× longer than AVC respectively.

The latest encoder comparison by Streaming Media Magazine as of September 2020, which used moderate encoding speeds, VMAF, and a diverse set of short clips, indicated that the open-source libaom and SVT-AV1 encoders took about twice as long time to encode as x265 in its "veryslow" preset while using 15-20% less bitrate, or about 45% less bitrate than *x264 veryslow*. The best-in-test AV1 encoder, Visionular's Aurora1, in its "slower" preset, was as fast as *x265 veryslow* while saving 50% bitrate over *x264 veryslow*.

CapFrameX tested the GPUs performance with AV1 decoding. On 5 October 2022, Cloudflare announced that it has a beta player.

## Profiles and levels

### Profiles

AV1 defines three profiles for decoders which are Main, High, and Professional. The Main profile allows for a bit depth of 8 or 10 bits per sample with 4:0:0 (greyscale) and 4:2:0 (quarter) chroma sampling. The High profile further adds support for 4:4:4 chroma sampling (no subsampling). The Professional profile extends capabilities to full support for 4:0:0, 4:2:0, 4:2:2 (half) and 4:4:4 chroma sub-sampling with 8, 10 and 12 bit color depths.

|   | Main (0) | High (1) | Professional (2) |   |
|---|---|---|---|---|
| Bit depth | 8 or 10 | 8 or 10 | 8, 10 & 12 |   |
| Chroma subsampling | 4:0:0 | Yes | Yes | Yes |
| 4:2:0 | Yes | Yes | Yes |   |
| 4:2:2 | No | No | Yes |   |
| 4:4:4 | No | Yes | Yes |   |

### Levels

AV1 defines levels for decoders with maximum variables for levels ranging from 2.0 to 6.3. The levels that can be implemented depend on the hardware capability.

Example resolutions would be 426×240@30 fps for level 2.0, 854×480@30 fps for level 3.0, 1920×1080@30 fps for level 4.0, 3840×2160@60 fps for level 5.1, 3840×2160@120 fps for level 5.2, and 7680×4320@120 fps for level 6.2. A "Level 7" is mentioned but is not defined.

seq_level_idx

Level

MaxPicSize

(Samples)

MaxHSize

(Samples)

MaxVSize

(Samples)

MaxDisplayRate

(Hz)

MaxDecodeRate

(Hz)

MaxHeader

Rate (Hz)

MainMbps

(Mbit/s)

HighMbps

(Mbit/s)

Min Comp Basis

Max Tiles

Max Tile Cols

Example

0

2.0

147,456

2,048

1,152

4,423,680

5,529,600

150

1.5

—

2

8

4

426×240@30fps

1

2.1

278,784

2,816

1,584

8,363,520

10,454,400

150

3.0

—

2

8

4

640×360@30fps

4

3.0

665,856

4,352

2,448

19,975,680

24,969,600

150

6.0

—

2

16

6

854×480@30fps

5

3.1

1,065,024

5,504

3,096

31,950,720

39,938,400

150

10.0

—

2

16

6

1280×720@30fps

8

4.0

2,359,296

6,144

3,456

70,778,880

77,856,768

300

12.0

30.0

4

32

8

1920×1080@30fps

9

4.1

2,359,296

6,144

3,456

141,557,760

155,713,536

300

20.0

50.0

4

32

8

1920×1080@60fps

12

5.0

8,912,896

8,192

4,352

267,386,880

273,715,200

300

30.0

100.0

6

64

8

3840×2160@30fps

13

5.1

8,912,896

8,192

4,352

534,773,760

547,430,400

300

40.0

160.0

8

64

8

3840×2160@60fps

14

5.2

8,912,896

8,192

4,352

1,069,547,520

1,094,860,800

300

60.0

240.0

8

64

8

3840×2160@120fps

15

5.3

8,912,896

8,192

4,352

1,069,547,520

1,176,502,272

300

60.0

240.0

8

64

8

3840×2160@120fps

16

6.0

35,651,584

16,384

8,704

1,069,547,520

1,176,502,272

300

60.0

240.0

8

128

16

7680×4320@30fps

17

6.1

35,651,584

16,384

8,704

2,139,095,040

2,189,721,600

300

100.0

480.0

8

128

16

7680×4320@60fps

18

6.2

35,651,584

16,384

8,704

4,278,190,080

4,379,443,200

300

160.0

800.0

8

128

16

7680×4320@120fps

19

6.3

35,651,584

16,384

8,704

4,278,190,080

4,706,009,088

300

160.0

800.0

8

128

16

7680×4320@120fps

## Supported container formats

Standardized:

- ISO base media file format: the ISOBMFF containerization spec by AOMedia was the first to be finalized and the first to gain adoption. This is the format used by YouTube.
- Matroska: version 1 of the Matroska containerization spec was published in late 2018.
- Real-time Transport Protocol: a RTP packetization spec by AOMedia defines the transmission of AV1 OBUs (*Open Bitstream Units*) directly as the RTP payload. It defines an RTP header extension that carries information about video frames and their dependencies, which is of general usefulness to § scalable video coding. The carriage of raw video data also differs from for example MPEG TS over RTP in that other streams, such as audio, must be carried externally.

Unfinished standards:

- MPEG Transport Stream (MPEG TS)

Not standardized:

- WebM: AV1 has not been formally sanctioned into the subset of Matroska known as WebM as of October 2023. However, support has been present in libwebm since May 2018.
- On2 IVF: this format was inherited from the first public release of VP8, where it served as a simple development container. rav1e also supports this format.
- Pre-standard WebM: Libaom featured early support for WebM before Matroska containerization was specified; this has since been changed to conform to the Matroska spec.

## Adoption

### Content providers

AV1 video is usually accompanied with AAC or Opus audio in an ISO base media file format (MP4) container.

In October 2016, Netflix stated they expected to be an early adopter of AV1. On 5 February 2020, Netflix began using AV1 to stream select titles on Android, providing 20% improved compression efficiency over their VP9 streams. On 9 November 2021, Netflix announced it had begun streaming AV1 content to a number of TVs with AV1 decoders as well as the PlayStation 4 Pro. In December 2025 they reported that 30% of their streams use AV1.

In 2018, YouTube began deploying AV1, starting with its AV1 Beta Launch Playlist. According to the description, the videos are (to begin with) encoded at high bitrate to test decoding performance, and YouTube has "ambitious goals" for rolling out AV1. YouTube for Android TV supports playback of videos encoded in AV1 on capable platforms as of version 2.10.13, released in early 2020. In 2020, YouTube started serving videos at 8K resolution in AV1.

In February 2019, Facebook followed its own positive test results, by saying it would gradually roll out the AV1 codec as soon as browser support emerges, starting with its most popular videos. Also in 2022, its parent company Meta expressed interest in SVT-AV1 as in the meantime Google engineer Matt Frost spoke at the ending on YouTube's Intel channel that an intention was to carry out a first test in 2023, when hardware acceleration will be introduced and widespread, but on the latest May video by Streaming Media the status was unknown and no statements from the AOMedia were expressed. MSVP (Meta Scalable Video Processor) was announced and the symposis was published in a popular scientific research website on 15 October 2022.

On 4 November 2022, the AV1 codec was announced with the article of Meta technology blog and with Mark Zuckerberg on Instagram Reels which shows AV1 codec compared with H.264/MPEG-4 AVC. Citing "Our Instagram engineering team developed a way to dramatically improve video quality. We made basic video processing 94% faster." Android has preliminary native AV1 playback.

In June 2019, Vimeo's videos in the "Staff picks" channel were available in AV1 and Opus. Vimeo is using and contributing to Mozilla's Rav1e encoder and expects, with further encoder improvements, to eventually provide AV1 support for all videos uploaded to Vimeo as well as the company's "Live" offering.

On 30 April 2020, iQIYI announced support for AV1 for users on PC web browsers and Android devices, according to the announcement, as the first Chinese video streaming site to adopt the codec.

Twitch deployed AV1 for its most popular content in 2022 or 2023, with universal support projected to arrive in 2024 or 2025.

In April 2021, Roku removed the YouTube TV app from the Roku streaming platform after a contract expired. It was later reported that Roku streaming devices do not use processors that support the AV1 codec. In December 2021, YouTube and Roku agreed to a multiyear deal to keep both the YouTube TV app and the YouTube app on the Roku streaming platform. Roku had argued that using processors in their streaming devices that support the royalty-free AV1 codec would increase costs to consumers.

In January 2022, Bilibili rolled out H.265 HEVC and AV1 encoding to videos with high view-count, while videos with lower view-count are only available in H.264 AVC.

In July 2024, DMM.com deployed AV1 on its DMM.TV service, becoming the first Japanese company to do so.

### Software implementations

- Libaom is the reference implementation. It includes an encoder (aomenc) and a decoder (aomdec). As the former research codec, it has the advantage of being made to justifiably demonstrate efficient use of every feature, but at the general cost of encoding speed. At feature freeze, the encoder had become problematically slow, but dramatic speed optimizations with negligible efficiency impact have subsequently been made.
- SVT-AV1 includes an open-source encoder and decoder developed primarily by Intel in collaboration with Netflix with a special focus on threading performance. They implemented in Cidana Corporation (Cidana Developers) and Software Implementation Working Group (SIWG). In August 2020, the Alliance for Open Media Software Implementation Working Group adopted SVT-AV1 as their production encoder. SVT-AV1 1.0.0 was released on 22 April 2022. SVT-AV1 2.0.0 was released on 13 March 2024. SVT-AV1 3.0.0 was released on 20 February 2025. SVT-AV1 4.0.0 was released on 23 January 2026.
- rav1e is an encoder written in Rust and assembly language from the Xiph.Org Foundation. rav1e takes the opposite developmental approach to aomenc: start out as the simplest (therefore fastest) conforming encoder, and then improve efficiency over time while remaining fast.
- dav1d is a decoder written in assembly and C99 focused on speed and portability, associated with VideoLAN. The first official version (0.1) was released in December 2018. Version 0.3 was announced in May 2019 with further optimizations demonstrating performance 2 to 5 times faster than aomdec. Version 0.5 was released in October 2019. Firefox 67 switched from Libaom to dav1d as a default decoder in May 2019. In 2019, dav1d v0.5 was rated the best decoder in comparison to libgav1 and libaom.
- Cisco AV1 is a proprietary live encoder that Cisco developed for its Webex teleconference products. The encoder is optimized for latency and the constraint of having a usable CPU footprint as with a "commodity laptop". Cisco stressed that at their operating point – high speed, low latency – the large toolset of AV1 does not preclude a low encoding complexity. Rather, the availability of tools for screen content and scalability in all profiles enabled them to find good compression-to-speed tradeoffs, better even than with HEVC; Compared to their previously deployed H.264 encoder, a particular area of improvement was in high resolution screen sharing.
- libgav1 is a decoder written in C++11 released by Google.
- rav1d is an AV1 cross-platform decoder, open-source, and focused on speed and correctness. It is a Rust port of dav1d.

Other vendors had announced encoders, including EVE for AV1, NGCodec, Socionext, Aurora and MilliCast.

### Operating system support

|   | Microsoft Windows | macOS | BSD / Linux | ChromeOS | Android | iOS |
|---|---|---|---|---|---|---|
| Codec support | Yes | Yes | Yes | Yes | Yes | Yes |
| Container support | ISO base media file format (.mp4) WebM (.webm) Matroska (.mkv) | ISO base media file format (.mp4) WebM (.webm) | ISO base media file format (.mp4) WebM (.webm) Matroska (.mkv) |   | ISO base media file format (.mp4) WebM (.webm) Matroska (.mkv) | ISO base media file format (.mp4) WebM (.webm) |
| Notes | Support introduced in Windows 10 October 2018 Update (1809) with AV1 Video Extension add-on for free download Support for hardware acceleration added in Windows 10 November 2019 Update (1909) Supported in Universal Windows Platform apps like Films & TV Since Windows 11 version 22H2, the AV1 Video Extension is built-in by default installation. | Built-in playback support on devices with M3 Apple silicon and higher, which have AV1 hardware decoders. On older devices (which use M1 and M2 chips, for example) VLC supports AV1 playback (including 4K) via software decoder. Firefox 67 and higher and Chrome 70 and higher support playback on all devices. |   | Supports decoding, from ChromeOS 70 onward | Supported since Android 10 | Playback support on devices with A17 Apple Silicon and higher, which have AV1 hardware decoders. |

### Hardware encoding and decoding support

There are several hardware accelerators for AV1, typically as part of a GPU or system on a chip. For example, later-generation NVidia GPUs have dedicated hardware and the NVENC and NVDEC APIs for encoding and decoding AV1 and other codecs.

Devices that support hardware-based decoding include: Samsung Galaxy S21 and newer, Google Pixel 6 and newer, iPhone 15 Pro & 15 Pro Max (A17 Pro), all iPhone 16 (A18) models and newer, iPad Mini (7th generation) (A17 Pro) and newer, iPad Air (7th generation) (M3) and newer, iPad Pro (7th generation) (M4) and newer.

| Company | Product | Decode | Encode |
|---|---|---|---|
| AMD | RDNA 2 (excluding Navi 24) | (Yes) | (No) |
| RDNA 3 and onwards | (Yes) | (Yes) |   |
| Alveo MA35D | (Yes) | (Yes) |   |
| Amlogic | S905X4 | (Yes) | (No) |
| S908X | (Yes) | (No) |   |
| S805X2 | (Yes) | (No) |   |
| Apple | A17 Pro | (Yes) | (No) |
| A18 / A18 Pro and onwards | (Yes) | (No) |   |
| M3 series and onwards | (Yes) | (No) |   |
| Broadcom | BCM7218X | (Yes) | (No) |
| Chips&Media | WAVE510A WAVE627 | (Yes) | (Yes) |
| Google | Tensor Original/G2 | (Yes) | (No) |
| Tensor G3 and onwards | (Yes) | (Yes) |   |
| Intel | Xe | (Yes) | (No) |
| Xe 2 and onwards | (Yes) | (Yes) |   |
| Arc | (Yes) | (Yes) |   |
| Data Center GPU Flex | (Yes) | (Yes) |   |
| MediaTek | Dimensity 1000, 8000, 9000 | (Yes) | (No) |
| MT96XX | (Yes) | (No) |   |
| MT9950 | (Yes) | (No) |   |
| Pentonic | (Yes) | (No) |   |
| NETINT | Quadra T1 (1x Codensity G5 ASIC) | (Yes) | (Yes) |
| Quadra T2 (2x Codensity G5 ASICs) | (Yes) | (Yes) |   |
| Quadra T4 (4x Codensity G5 ASICs) | (Yes) | (Yes) |   |
| Nvidia | GeForce RTX 30 | (Yes) | (No) |
| GeForce RTX 40 and onwards | (Yes) | (Yes) |   |
| Qualcomm | Snapdragon 8 Gen 2 | (Yes) | (No) |
| Snapdragon 8/8s Gen 3/4/5 | (Yes) | (No) |   |
| Snapdragon X Plus/Elite | (Yes) | (Yes) |   |
| Snapdragon X2 Plus | (Yes) | (Yes) |   |
| Snapdragon X2 Elite/X2 Extreme | (Yes) | (Yes) |   |
| Snapdragon 7 Gen 4 | (Yes) | (No) |   |
| Realtek | RTD1311 | (Yes) | (No) |
| RTD2893 | (Yes) | (No) |   |
| Rockchip | RK3588 | (Yes) | (No) |
| Samsung | Exynos 2000 series | (Yes) | (No) |
| Axis Communications | ARTPEC-9 | (No) | (Yes) |

## Patent claims

In early 2019, Sisvel, a Luxembourg-based company, claimed to be forming a patent pool of patents essential to AV1. This development has not caused Google to reevaluate its planned AV1 usage and the Alliance for Open Media has stated they remain confident that AV1 still overcomes the environment of "high patent royalty requirements and licensing uncertainty". Sisvel began selling licenses to the pool, which contains patents from Philips, GE, NTT, Ericsson, Dolby, and Toshiba in 2020. Unified Patents has been tracking challenges to various patents in the pool.

On 7 July 2022, it was revealed that the European Union's antitrust regulators had opened an investigation into AOM and its licensing policy. It said this action may be restricting the innovators' ability to compete with the AV1 technical specification, and may eliminate incentives for them to innovate.

> The Commission has information that AOM and its members may be imposing licensing terms (mandatory royalty-free cross licensing) on innovators that were not a part of AOM at the time of the creation of the AV1 technical, but whose patents are deemed essential to (its) technical specifications

On 23 May 2023, the European Commission decided to close the investigation while taking no further action. But in an email they reiterated that the closure does not constitute a finding of compliance or non-compliance with EU antitrust laws.

In October 2023, patent pool operator Avanci announced the start of a new licensing program targeting video streaming operators that use AV1 in addition to H.265, H.266, VP9, etc.

In March 2026, Dolby sued Snapchat for Video patent infringement in the United States District Court for the District of Delaware (D. Del., case no. 1:26-cv-00317 (Dolby Video Compression LLC v. Snap Inc.)) and in the Rio de Janeiro State Court in Brazil (Case no. 3043830-49.2026.8.19.0001 (Dolby Video Compression, LLC v. Snap Inc.).

In May 2026, the 5th Business Court of Rio de Janeiro granted Dolby IP Bridge preliminary injunction against Skyworth. The judge baned implementation of patented technologies in current and upcomming products sold in Brazil. Also in the same month Malikie Innovations sued TCL Technology over AV1 patents in United States District Court for the Eastern District of Texas.

## AV1 Image File Format (AVIF)

AV1 Image File Format (AVIF) is an image file format specification for storing still images or image sequences compressed with AV1 in the HEIF file format. It competes with HEIC which uses the same container format, built upon ISOBMFF, but HEVC for compression.

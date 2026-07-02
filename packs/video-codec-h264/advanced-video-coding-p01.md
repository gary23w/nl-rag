---
title: "Advanced Video Coding (part 1/2)"
source: https://en.wikipedia.org/wiki/Advanced_Video_Coding
domain: video-codec-h264
license: CC-BY-SA-4.0
tags: h.264 codec, advanced video coding, cabac entropy, motion compensation
fetched: 2026-07-02
part: 1/2
---

# Advanced Video Coding

**Advanced Video Coding** (**AVC**), also referred to as **H.264** or **MPEG-4 Part 10**, is a video compression standard based on block-oriented, motion-compensated coding. It is by far the most commonly used format for the recording, compression, and distribution of video content, used by 79% of video industry developers as of December 2024. It supports a maximum resolution of 8K UHD.

H.264 was standardized by the ITU-T Video Coding Experts Group (VCEG) of Study Group 16 together with the ISO/IEC JTC 1 Moving Picture Experts Group (MPEG). The project partnership effort is known as the Joint Video Team (JVT). The ITU-T H.264 standard and the ISO/IEC MPEG-4 AVC standard (formally, ISO/IEC 14496-10 – MPEG-4 Part 10, Advanced Video Coding) are jointly maintained so that they have identical technical content. The final drafting work on the first version of the standard was completed in May 2003, and various extensions of its capabilities have been added in subsequent editions. High Efficiency Video Coding (HEVC), a.k.a. H.265 and MPEG-H Part 2 is a successor to H.264/MPEG-4 AVC developed by the same organizations, while earlier standards are still in common use.

H.264 is perhaps best known as being the most commonly used video encoding format on Blu-ray Discs. It has also been widely used by streaming Internet sources, such as videos from Netflix, Hulu, Amazon Prime Video, Vimeo, YouTube (more recently transitioning to VP9 and AV1), and the iTunes Store, Web software such as the Adobe Flash Player and Microsoft Silverlight, and also various HDTV broadcasts over terrestrial (ATSC, ISDB-T, DVB-T or DVB-T2), cable (DVB-C), and satellite (DVB-S and DVB-S2) systems.

H.264 is restricted by patents owned by various parties. A license covering most (but not all) patents essential to H.264 is administered by a patent pool formerly administered by MPEG LA. Via Licensing Corp acquired MPEG LA in April 2023 and formed a new patent pool administration company called Via Licensing Alliance. The commercial use of patented H.264 technologies requires the payment of royalties to Via and other patent owners. MPEG LA has allowed the free use of H.264 technologies for streaming Internet video that is free to end users, and Cisco paid royalties to MPEG LA on behalf of the users of binaries for its open source H.264 encoder openH264.


## Naming

The H.264 name follows the ITU-T naming convention, where Recommendations are given a letter corresponding to their series and a recommendation number within the series. H.264 is part of "H-Series Recommendations: Audiovisual and multimedia systems". H.264 is further categorized into "H.200-H.499: Infrastructure of audiovisual services" and "H.260-H.279: Coding of moving video". The MPEG-4 AVC name relates to the naming convention in ISO/IEC MPEG, where the standard is part 10 of ISO/IEC 14496, which is the suite of standards known as MPEG-4. The standard was developed jointly in a partnership of VCEG and MPEG, after earlier development work in the ITU-T as a VCEG project called H.26L. It is thus common to refer to the standard with names such as H.264/AVC, AVC/H.264, H.264/MPEG-4 AVC, or MPEG-4/H.264 AVC, to emphasize the common heritage. Occasionally, it is also referred to as "the JVT codec", in reference to the Joint Video Team (JVT) organization that developed it. (Such partnership and multiple naming is not uncommon. For example, the video compression standard known as MPEG-2 also arose from the partnership between MPEG and the ITU-T, where MPEG-2 video is known to the ITU-T community as H.262.) Some software programs (such as VLC media player) internally identify this standard as AVC1.


## History

### Overall history

In early 1998, the Video Coding Experts Group (VCEG – ITU-T SG16 Q.6) issued a call for proposals on a project called H.26L, with the target to double the coding efficiency (which means halving the bit rate necessary for a given level of fidelity) in comparison to any other existing video coding standards for a broad variety of applications. VCEG was chaired by Gary Sullivan (Microsoft, formerly PictureTel, U.S.). The first draft design for that new standard was adopted in August 1999. In 2000, Thomas Wiegand (Heinrich Hertz Institute, Germany) became VCEG co-chair.

In December 2001, VCEG and the Moving Picture Experts Group (MPEG – ISO/IEC JTC 1/SC 29/WG 11) formed a Joint Video Team (JVT), with the charter to finalize the video coding standard. Formal approval of the specification came in March 2003. The JVT was (is) chaired by Gary Sullivan, Thomas Wiegand, and Ajay Luthra (Motorola, U.S.: later Arris, U.S.). In July 2004, the Fidelity Range Extensions (FRExt) project was finalized. From January 2005 to November 2007, the JVT was working on an extension of H.264/AVC towards scalability by an Annex (G) called Scalable Video Coding (SVC). The JVT management team was extended by Jens-Rainer Ohm (RWTH Aachen University, Germany). From July 2006 to November 2009, the JVT worked on Multiview Video Coding (MVC), an extension of H.264/AVC towards 3D television and limited-range free-viewpoint television. That work included the development of two new profiles of the standard: the Multiview High Profile and the Stereo High Profile.

Throughout the development of the standard, additional messages for containing supplemental enhancement information (SEI) have been developed. SEI messages can contain various types of data that indicate the timing of the video pictures or describe various properties of the coded video or how it can be used or enhanced. SEI messages are also defined that can contain arbitrary user-defined data. SEI messages do not affect the core decoding process, but can indicate how the video is recommended to be post-processed or displayed. Some other high-level properties of the video content are conveyed in video usability information (VUI), such as the indication of the color space for interpretation of the video content. As new color spaces have been developed, such as for high dynamic range and wide color gamut video, additional VUI identifiers have been added to indicate them.

### Fidelity range extensions and professional profiles

The standardization of the first version of H.264/AVC was completed in May 2003. In the first project to extend the original standard, the JVT then developed what was called the Fidelity Range Extensions (FRExt). These extensions enabled higher quality video coding by supporting increased sample bit depth precision and higher-resolution color information, including the sampling structures known as Y′CBCR 4:2:2 (a.k.a. YUV 4:2:2) and 4:4:4. Several other features were also included in the FRExt project, such as adding an 8×8 integer discrete cosine transform (integer DCT) with adaptive switching between the 4×4 and 8×8 transforms, encoder-specified perceptual-based quantization weighting matrices, efficient inter-picture lossless coding, and support of additional color spaces. The design work on the FRExt project was completed in July 2004, and the drafting work on them was completed in September 2004.

Five other new profiles (see version 7 below) intended primarily for professional applications were then developed, adding extended-gamut color space support, defining additional aspect ratio indicators, defining two additional types of "supplemental enhancement information" (post-filter hint and tone mapping), and deprecating one of the prior FRExt profiles (the High 4:4:4 profile) that industry feedback indicated should have been designed differently.

### Scalable video coding

The next major feature added to the standard was Scalable Video Coding (SVC). Specified in Annex G of H.264/AVC, SVC allows the construction of bitstreams that contain *layers* of sub-bitstreams that also conform to the standard, including one such bitstream known as the "base layer" that can be decoded by a H.264/AVC codec that does not support SVC. For temporal bitstream scalability (i.e., the presence of a sub-bitstream with a smaller temporal sampling rate than the main bitstream), complete access units are removed from the bitstream when deriving the sub-bitstream. In this case, high-level syntax and inter-prediction reference pictures in the bitstream are constructed accordingly. On the other hand, for spatial and quality bitstream scalability (i.e. the presence of a sub-bitstream with lower spatial resolution/quality than the main bitstream), the NAL (Network Abstraction Layer) is removed from the bitstream when deriving the sub-bitstream. In this case, inter-layer prediction (i.e., the prediction of the higher spatial resolution/quality signal from the data of the lower spatial resolution/quality signal) is typically used for efficient coding. The Scalable Video Coding extensions were completed in November 2007.

### Multiview video coding

The next major feature added to the standard was Multiview Video Coding (MVC). Specified in Annex H of H.264/AVC, MVC enables the construction of bitstreams that represent more than one view of a video scene. An important example of this functionality is stereoscopic 3D video coding. Two profiles were developed in the MVC work: Multiview High profile supports an arbitrary number of views, and Stereo High profile is designed specifically for two-view stereoscopic video. The Multiview Video Coding extensions were completed in November 2009.

### 3D-AVC and MFC stereoscopic coding

Additional extensions were later developed that included 3D video coding with joint coding of depth maps and texture (termed 3D-AVC), multi-resolution frame-compatible (MFC) stereoscopic and 3D-MFC coding, various additional combinations of features, and higher frame sizes and frame rates.

### Versions

Versions of the H.264/AVC standard include the following completed revisions, corrigenda, and amendments (dates are final approval dates in ITU-T, while final "International Standard" approval dates in ISO/IEC are somewhat different and slightly later in most cases). Each version represents changes relative to the next lower version that is integrated into the text.

- Version 1 (Edition 1): (May 30, 2003) First approved version of H.264/AVC containing Baseline, Main, and Extended profiles.
- Version 2 (Edition 1.1): (May 7, 2004) Corrigendum containing various minor corrections.
- Version 3 (Edition 2): (March 1, 2005) Major addition containing the first amendment, establishing the Fidelity Range Extensions (FRExt). This version added the High, High 10, High 4:2:2, and High 4:4:4 profiles. After a few years, the High profile became the most commonly used profile of the standard.
- Version 4 (Edition 2.1): (September 13, 2005) Corrigendum containing various minor corrections and adding three aspect ratio indicators.
- Version 5 (Edition 2.2): (June 13, 2006) Amendment consisting of removal of prior High 4:4:4 profile (processed as a corrigendum in ISO/IEC).
- Version 6 (Edition 2.2): (June 13, 2006) Amendment consisting of minor extensions like extended-gamut color space support (bundled with above-mentioned aspect ratio indicators in ISO/IEC).
- Version 7 (Edition 2.3): (April 6, 2007) Amendment containing the addition of the High 4:4:4 Predictive profile and four Intra-only profiles (High 10 Intra, High 4:2:2 Intra, High 4:4:4 Intra, and CAVLC 4:4:4 Intra).
- Version 8 (Edition 3): (November 22, 2007) Major addition to H.264/AVC containing the amendment for Scalable Video Coding (SVC) containing Scalable Baseline, Scalable High, and Scalable High Intra profiles.
- Version 9 (Edition 3.1): (January 13, 2009) Corrigendum containing minor corrections.
- Version 10 (Edition 4): (March 16, 2009) Amendment containing definition of a new profile (the Constrained Baseline profile) with only the common subset of capabilities supported in various previously specified profiles.
- Version 11 (Edition 4): (March 16, 2009) Major addition to H.264/AVC containing the amendment for Multiview Video Coding (MVC) extension, including the Multiview High profile.
- Version 12 (Edition 5): (March 9, 2010) Amendment containing definition of a new MVC profile (the Stereo High profile) for two-view video coding with support of interlaced coding tools and specifying an additional supplemental enhancement information (SEI) message termed the frame packing arrangement SEI message.
- Version 13 (Edition 5): (March 9, 2010) Corrigendum containing minor corrections.
- Version 14 (Edition 6): (June 29, 2011) Amendment specifying a new level (Level 5.2) supporting higher processing rates in terms of maximum macroblocks per second, and a new profile (the Progressive High profile) supporting only the frame coding tools of the previously specified High profile.
- Version 15 (Edition 6): (June 29, 2011) Corrigendum containing minor corrections.
- Version 16 (Edition 7): (January 13, 2012) Amendment containing definition of three new profiles intended primarily for real-time communication applications: the Constrained High, Scalable Constrained Baseline, and Scalable Constrained High profiles.
- Version 17 (Edition 8): (April 13, 2013) Amendment with additional SEI message indicators.
- Version 18 (Edition 8): (April 13, 2013) Amendment to specify the coding of depth map data for 3D stereoscopic video, including a Multiview Depth High profile.
- Version 19 (Edition 8): (April 13, 2013) Corrigendum to correct an error in the sub-bitstream extraction process for multiview video.
- Version 20 (Edition 8): (April 13, 2013) Amendment to specify additional color space identifiers (including support of ITU-R Recommendation BT.2020 for UHDTV) and an additional model type in the tone mapping information SEI message.
- Version 21 (Edition 9): (February 13, 2014) Amendment to specify the Enhanced Multiview Depth High profile.
- Version 22 (Edition 9): (February 13, 2014) Amendment to specify the multi-resolution frame compatible (MFC) enhancement for 3D stereoscopic video, the MFC High profile, and minor corrections.
- Version 23 (Edition 10): (February 13, 2016) Amendment to specify MFC stereoscopic video with depth maps, the MFC Depth High profile, the mastering display color volume SEI message, and additional color-related VUI codepoint identifiers.
- Version 24 (Edition 11): (October 14, 2016) Amendment to specify additional levels of decoder capability supporting larger picture sizes (Levels 6, 6.1, and 6.2), the green metadata SEI message, the alternative depth information SEI message, and additional color-related VUI codepoint identifiers.
- Version 25 (Edition 12): (April 13, 2017) Amendment to specify the Progressive High 10 profile, hybrid log–gamma (HLG), and additional color-related VUI code points and SEI messages.
- Version 26 (Edition 13): (June 13, 2019) Amendment to specify additional SEI messages for ambient viewing environment, content light level information, content color volume, equirectangular projection, cubemap projection, sphere rotation, region-wise packing, omnidirectional viewport, SEI manifest, and SEI prefix.
- Version 27 (Edition 14): (August 22, 2021) Amendment to specify additional SEI messages for annotated regions and shutter interval information, and miscellaneous minor corrections and clarifications.
- Version 28 (Edition 15): (August 13, 2024) Amendment to specify additional SEI messages for neural-network postfilter characteristics, neural-network post-filter activation, and phase indication, additional colour type identifiers, and miscellaneous minor corrections and clarifications.


## Applications

The H.264 video format has a very broad application range that covers all forms of digital compressed video from low bit-rate Internet streaming applications to HDTV broadcast and Digital Cinema applications with nearly lossless coding. With the use of H.264, bit rate savings of 50% or more compared to MPEG-2 Part 2 are reported. For example, H.264 has been reported to give the same Digital Satellite TV quality as current MPEG-2 implementations with less than half the bitrate, with current MPEG-2 implementations working at around 3.5 Mbit/s and H.264 at only 1.5 Mbit/s. Sony claims that 9 Mbit/s AVC recording mode is equivalent to the image quality of the HDV format, which uses approximately 18–25 Mbit/s.

To ensure compatibility and problem-free adoption of H.264/AVC, many standards bodies have amended or added to their video-related standards so that users of these standards can employ H.264/AVC. Both the Blu-ray Disc format and the now-discontinued HD DVD format include the H.264/AVC High Profile as one of three mandatory video compression formats. The Digital Video Broadcast project (DVB) approved the use of H.264/AVC for broadcast television in late 2004.

The Advanced Television Systems Committee (ATSC) standards body in the United States approved the use of H.264/AVC for broadcast television in July 2008. It has also been approved for use with the more recent ATSC-M/H (Mobile/Handheld) standard, using the AVC and SVC portions of H.264.

The closed-circuit-television and video-surveillance markets have included the technology in many products.

Many common DSLRs use H.264 video wrapped in QuickTime MOV containers as the native recording format.

### Derived formats

AVCHD is a high-definition recording format designed by Sony and Panasonic that uses H.264 (conforming to H.264 while adding additional application-specific features and constraints).

AVC-Intra is an intraframe-only compression format, developed by Panasonic.

XAVC is a recording format designed by Sony that uses level 5.2 of H.264/MPEG-4 AVC, which is the highest level supported by that video standard. XAVC can support 4K resolution (4096 × 2160 and 3840 × 2160) at up to 60 frames per second (fps). Sony has announced that cameras that support XAVC include two CineAlta cameras—the Sony PMW-F55 and Sony PMW-F5. The Sony PMW-F55 can record XAVC with 4K resolution at 30 fps at 300 Mbit/s and 2K resolution at 30 fps at 100 Mbit/s. XAVC can record 4K resolution at 60 fps with 4:2:2 chroma sampling at 600 Mbit/s.


## Design

### Features

H.264/AVC/MPEG-4 Part 10 contains a number of new features that allow it to compress video much more efficiently than older standards and to provide more flexibility for application to a wide variety of network environments. In particular, some such key features include:

- Multi-picture inter-picture prediction including the following features:
  - Using previously encoded pictures as references in a much more flexible way than in past standards, allowing up to 16 reference frames (or 32 reference fields, in the case of interlaced encoding) to be used in some cases. In profiles that support non-IDR frames, most levels specify that sufficient buffering should be available to allow for at least 4 or 5 reference frames at maximum resolution. This is in contrast to prior standards, where the limit was typically one; or, in the case of conventional "B pictures" (B-frames), two.
  - Variable block-size motion compensation (VBSMC) with block sizes as large as 16×16 and as small as 4×4, enabling precise segmentation of moving regions. The supported luma prediction block sizes include 16×16, 16×8, 8×16, 8×8, 8×4, 4×8, and 4×4, many of which can be used together in a single macroblock. Chroma prediction block sizes are correspondingly smaller when chroma subsampling is used.
  - The ability to use multiple motion vectors per macroblock (one or two per partition) with a maximum of 32 in the case of a B macroblock constructed of 16 4×4 partitions. The motion vectors for each 8×8 or larger partition region can point to different reference pictures.
  - The ability to use any macroblock type in B-frames, including I-macroblocks, resulting in much more efficient encoding when using B-frames. This feature was notably left out from MPEG-4 ASP.
  - Six-tap filtering for derivation of half-pel luma sample predictions, for sharper subpixel motion-compensation. Quarter-pixel motion is derived by linear interpolation of the halfpixel values, to save processing power.
  - Quarter-pixel precision for motion compensation, enabling precise description of the displacements of moving areas. For chroma the resolution is typically halved both vertically and horizontally (see 4:2:0) therefore the motion compensation of chroma uses one-eighth chroma pixel grid units.
  - Weighted prediction, allowing an encoder to specify the use of a scaling and offset when performing motion compensation, and providing a significant benefit in performance in special cases—such as fade-to-black, fade-in, and cross-fade transitions. This includes implicit weighted prediction for B-frames, and explicit weighted prediction for P-frames.
- Spatial prediction from the edges of neighboring blocks for "intra" coding, rather than the "DC"-only prediction found in MPEG-2 Part 2 and the transform coefficient prediction found in H.263v2 and MPEG-4 Part 2. This includes luma prediction block sizes of 16×16, 8×8, and 4×4 (of which only one type can be used within each macroblock).
- Integer discrete cosine transform (integer DCT), a type of discrete cosine transform (DCT) where the transform is an integer approximation of the standard DCT. It has selectable block sizes and exact-match integer computation to reduce complexity, including:
  - An exact-match integer 4×4 spatial block transform, allowing precise placement of residual signals with little of the "ringing" often found with prior codec designs. It is similar to the standard DCT used in previous standards, but uses a smaller block size and simple integer processing. Unlike the cosine-based formulas and tolerances expressed in earlier standards (such as H.261 and MPEG-2), integer processing provides an exactly specified decoded result.
  - An exact-match integer 8×8 spatial block transform, allowing highly correlated regions to be compressed more efficiently than with the 4×4 transform. This design is based on the standard DCT, but simplified and made to provide exactly specified decoding.
  - Adaptive encoder selection between the 4×4 and 8×8 transform block sizes for the integer transform operation.
  - A secondary Hadamard transform performed on "DC" coefficients of the primary spatial transform applied to chroma DC coefficients (and also luma in one special case) to obtain even more compression in smooth regions.
- Lossless macroblock coding features including:
  - A lossless "PCM macroblock" representation mode in which video data samples are represented directly, allowing perfect representation of specific regions and allowing a strict limit to be placed on the quantity of coded data for each macroblock.
  - An enhanced lossless macroblock representation mode allowing perfect representation of specific regions while ordinarily using substantially fewer bits than the PCM mode.
- Flexible interlaced-scan video coding features, including:
  - Macroblock-adaptive frame-field (MBAFF) coding, using a macroblock pair structure for pictures coded as frames, allowing 16×16 macroblocks in field mode (compared with MPEG-2, where field mode processing in a picture that is coded as a frame results in the processing of 16×8 half-macroblocks).
  - Picture-adaptive frame-field coding (PAFF or PicAFF) allowing a freely selected mixture of pictures coded either as complete frames where both fields are combined for encoding or as individual single fields.
- A quantization design including:
  - Logarithmic step size control for easier bit rate management by encoders and simplified inverse-quantization scaling
  - Frequency-customized quantization scaling matrices selected by the encoder for perceptual-based quantization optimization
- An in-loop deblocking filter that helps prevent the blocking artifacts common to other DCT-based image compression techniques, resulting in better visual appearance and compression efficiency
- An entropy coding design including:
  - Context-adaptive binary arithmetic coding (CABAC), an algorithm to losslessly compress syntax elements in the video stream knowing the probabilities of syntax elements in a given context. CABAC compresses data more efficiently than CAVLC but requires considerably more processing to decode.
  - Context-adaptive variable-length coding (CAVLC), which is a lower-complexity alternative to CABAC for the coding of quantized transform coefficient values. Although lower complexity than CABAC, CAVLC is more elaborate and more efficient than the methods typically used to code coefficients in other prior designs.
  - A common simple and highly structured variable length coding (VLC) technique for many of the syntax elements not coded by CABAC or CAVLC, referred to as Exponential-Golomb coding (or Exp-Golomb).
- Loss resilience features including:
  - A Network Abstraction Layer (NAL) definition allowing the same video syntax to be used in many network environments. One very fundamental design concept of H.264 is to generate self-contained packets, to remove the header duplication as in MPEG-4's Header Extension Code (HEC). This was achieved by decoupling information relevant to more than one slice from the media stream. The combination of the higher-level parameters is called a parameter set. The H.264 specification includes two types of parameter sets: Sequence Parameter Set (SPS) and Picture Parameter Set (PPS). An active sequence parameter set remains unchanged throughout a coded video sequence, and an active picture parameter set remains unchanged within a coded picture. The sequence and picture parameter set structures contain information such as picture size, optional coding modes employed, and macroblock to slice group map.
  - Flexible macroblock ordering (FMO), also known as slice groups, and arbitrary slice ordering (ASO), which are techniques for restructuring the ordering of the representation of the fundamental regions (*macroblocks*) in pictures. Typically considered an error/loss robustness feature, FMO and ASO can also be used for other purposes.
  - Data partitioning (DP), a feature providing the ability to separate more important and less important syntax elements into different packets of data, enabling the application of unequal error protection (UEP) and other types of improvement of error/loss robustness.
  - Redundant slices (RS), an error/loss robustness feature that lets an encoder send an extra representation of a picture region (typically at lower fidelity) that can be used if the primary representation is corrupted or lost.
  - Frame numbering, a feature that allows the creation of "sub-sequences", enabling temporal scalability by optional inclusion of extra pictures between other pictures, and the detection and concealment of losses of entire pictures, which can occur due to network packet losses or channel errors.
- Switching slices, called SP and SI slices, allowing an encoder to direct a decoder to jump into an ongoing video stream for such purposes as video streaming bit rate switching and "trick mode" operation. When a decoder jumps into the middle of a video stream using the SP/SI feature, it can get an exact match to the decoded pictures at that location in the video stream despite using different pictures, or no pictures at all, as references prior to the switch.
- A simple automatic process for preventing the accidental emulation of start codes, which are special sequences of bits in the coded data that allow random access into the bitstream and recovery of byte alignment in systems that can lose byte synchronization.
- Supplemental enhancement information (SEI) and video usability information (VUI), which are extra information that can be inserted into the bitstream for various purposes such as indicating the color space used the video content or various constraints that apply to the encoding. SEI messages can contain arbitrary user-defined metadata payloads or other messages with syntax and semantics defined in the standard.
- Auxiliary pictures, which can be used for such purposes as alpha compositing.
- Support of monochrome (4:0:0), 4:2:0, 4:2:2, and 4:4:4 chroma sampling (depending on the selected profile).
- Support of sample bit depth precision ranging from 8 to 14 bits per sample (depending on the selected profile).
- The ability to encode individual color planes as distinct pictures with their own slice structures, macroblock modes, motion vectors, etc., allowing encoders to be designed with a simple parallelization structure (supported only in the three 4:4:4-capable profiles).
- Picture order count, a feature that serves to keep the ordering of the pictures and the values of samples in the decoded pictures isolated from timing information, allowing timing information to be carried and controlled/changed separately by a system without affecting decoded picture content.

These techniques, along with several others, help H.264 to perform significantly better than any prior standard under a wide variety of circumstances in a wide variety of application environments. H.264 can often perform radically better than MPEG-2 video—typically obtaining the same quality at half of the bit rate or less, especially on high bit rate and high resolution video content.

Like other ISO/IEC MPEG video standards, H.264/AVC has a reference software implementation that can be freely downloaded. Its main purpose is to give examples of H.264/AVC features, rather than being a useful application *per se*. Some reference hardware design work has also been conducted in the Moving Picture Experts Group. The above-mentioned aspects include features in all profiles of H.264. A profile for a codec is a set of features of that codec identified to meet a certain set of specifications of intended applications. This means that many of the features listed are not supported in some profiles. Various profiles of H.264/AVC are discussed in next section.

### Profiles

The standard defines several sets of capabilities, which are referred to as *profiles*, targeting specific classes of applications. These are declared using a profile code (profile_idc) and sometimes a set of additional constraints applied in the encoder. The profile code and indicated constraints allow a decoder to recognize the requirements for decoding that specific bitstream. (And in many system environments, only one or two profiles are allowed to be used, so decoders in those environments do not need to be concerned with recognizing the less commonly used profiles.) By far the most commonly used profile is the High Profile.

Profiles for non-scalable 2D video applications include the following:

**Constrained Baseline Profile (CBP, 66 with constraint set 1)**

Primarily for low-cost applications, this profile is most typically used in videoconferencing and mobile applications. It corresponds to the subset of features that are in common between the Baseline, Main, and High Profiles.

**Baseline Profile (BP, 66)**

Primarily for low-cost applications that require additional data loss robustness, this profile is used in some videoconferencing and mobile applications. This profile includes all features that are supported in the Constrained Baseline Profile, plus three additional features that can be used for loss robustness (or for other purposes such as low-delay multi-point video stream compositing). The importance of this profile has faded somewhat since the definition of the Constrained Baseline Profile in 2009. All Constrained Baseline Profile bitstreams are also considered to be Baseline Profile bitstreams, as these two profiles share the same profile identifier code value.

**Extended Profile (XP, 88)**

Intended as the streaming video profile, this profile has relatively high compression capability and some extra tricks for robustness to data losses and server stream switching.

**Main Profile (MP, 77)**

This profile is used for standard-definition digital TV broadcasts that use the MPEG-4 format as defined in the DVB standard.

It is not, however, used for high-definition television broadcasts, as the importance of this profile faded when the High Profile was developed in 2004 for that application.

**High Profile (HiP, 100)**

The primary profile for broadcast and disc storage applications, particularly for high-definition television applications (for example, this is the profile adopted by the

Blu-ray Disc

storage format and the

DVB

HDTV broadcast service).

**Progressive High Profile (PHiP, 100 with constraint set 4)**

Similar to the High profile, but without support of field coding features.

**Constrained High Profile (100 with constraint set 4 and 5)**

Similar to the Progressive High profile, but without support of B (bi-predictive) slices.

**High 10 Profile (Hi10P, 110)**

Going beyond typical mainstream consumer product capabilities, this profile builds on top of the High Profile, adding support for up to 10 bits per sample of decoded picture precision.

**High 4:2:2 Profile (Hi422P, 122)**

Primarily targeting professional applications that use interlaced video, this profile builds on top of the High 10 Profile, adding support for the 4:2:2

chroma sampling

format while using up to 10 bits per sample of decoded picture precision.

**High 4:4:4 Predictive Profile (Hi444PP, 244)**

This profile builds on top of the High 4:2:2 Profile, supporting up to 4:4:4 chroma sampling, up to 14 bits per sample, and additionally supporting efficient lossless region coding and the coding of each picture as three separate color planes.

For camcorders, editing, and professional applications, the standard contains four additional Intra-frame-only profiles, which are defined as simple subsets of other corresponding profiles. These are mostly for professional (e.g., camera and editing system) applications:

**High 10 Intra Profile (110 with constraint set 3)**

The High 10 Profile constrained to all-Intra use.

**High 4:2:2 Intra Profile (122 with constraint set 3)**

The High 4:2:2 Profile constrained to all-Intra use.

**High 4:4:4 Intra Profile (244 with constraint set 3)**

The High 4:4:4 Profile constrained to all-Intra use.

**CAVLC 4:4:4 Intra Profile (44)**

The High 4:4:4 Profile constrained to all-Intra use and to CAVLC entropy coding (i.e., not supporting CABAC).

As a result of the Scalable Video Coding (SVC) extension, the standard contains five additional *scalable profiles*, which are defined as a combination of a H.264/AVC profile for the base layer (identified by the second word in the scalable profile name) and tools that achieve the scalable extension:

**Scalable Baseline Profile (83)**

Primarily targeting video conferencing, mobile, and surveillance applications, this profile builds on top of the Constrained Baseline profile to which the base layer (a subset of the bitstream) must conform. For the scalability tools, a subset of the available tools is enabled.

**Scalable Constrained Baseline Profile (83 with constraint set 5)**

A subset of the Scalable Baseline Profile intended primarily for real-time communication applications.

**Scalable High Profile (86)**

Primarily targeting broadcast and streaming applications, this profile builds on top of the H.264/AVC High Profile to which the base layer must conform.

**Scalable Constrained High Profile (86 with constraint set 5)**

A subset of the Scalable High Profile intended primarily for real-time communication applications.

**Scalable High Intra Profile (86 with constraint set 3)**

Primarily targeting production applications, this profile is the Scalable High Profile constrained to all-Intra use.

As a result of the Multiview Video Coding (MVC) extension, the standard contains two *multiview profiles*:

**Stereo High Profile (128)**

This profile targets two-view

stereoscopic

3D video and combines the tools of the High profile with the inter-view prediction capabilities of the MVC extension.

**Multiview High Profile (118)**

This profile supports two or more views using both inter-picture (temporal) and MVC inter-view prediction, but does not support field pictures and macroblock-adaptive frame-field coding.

The Multi-resolution Frame-Compatible (MFC) extension added two more profiles:

**MFC High Profile (134)**

A profile for stereoscopic coding with two-layer resolution enhancement.

**MFC Depth High Profile (135)**

The 3D-AVC extension added two more profiles:

**Multiview Depth High Profile (138)**

This profile supports joint coding of depth map and video texture information for improved compression of 3D video content.

**Enhanced Multiview Depth High Profile (139)**

An enhanced profile for combined multiview coding with depth information.

#### Feature support in particular profiles

Feature

CBP

BP

XP

MP

ProHiP

HiP

Hi10P

Hi422P

Hi444PP

I and P slices

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Bit depth

(per sample)

8

8

8

8

8

8

8 to 10

8 to 10

8 to 14

Chroma

formats

4:2:0

4:2:0

4:2:0

4:2:0

4:2:0

4:2:0

4:2:0

4:2:0/

4:2:2

4:2:0/

4:2:2/

4:4:4

Flexible macroblock ordering (FMO)

No

Yes

Yes

No

No

No

No

No

No

Arbitrary slice ordering (ASO)

No

Yes

Yes

No

No

No

No

No

No

Redundant slices (RS)

No

Yes

Yes

No

No

No

No

No

No

Data Partitioning

No

No

Yes

No

No

No

No

No

No

SI and SP slices

No

No

Yes

No

No

No

No

No

No

Interlaced coding (PicAFF, MBAFF)

No

No

Yes

Yes

No

Yes

Yes

Yes

Yes

B slices

No

No

Yes

Yes

Yes

Yes

Yes

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

Yes

In-loop deblocking filter

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

CAVLC entropy coding

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

CABAC entropy coding

No

No

No

Yes

Yes

Yes

Yes

Yes

Yes

4:0:0 (

Greyscale

)

No

No

No

No

Yes

Yes

Yes

Yes

Yes

8×8 vs. 4×4 transform adaptivity

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Quantization scaling matrices

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Separate C

B

and C

R

QP control

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Separate color plane coding

No

No

No

No

No

No

No

No

Yes

Predictive lossless coding

No

No

No

No

No

No

No

No

Yes

### Levels

As the term is used in the standard, a "*level*" is a specified set of constraints that indicate a degree of required decoder performance for a profile. For example, a level of support within a profile specifies the maximum picture resolution, frame rate, and bit rate that a decoder may use. A decoder that conforms to a given level must be able to decode all bitstreams encoded for that level and all lower levels.

| Level | Maximum decoding speed (macroblocks/s) | Maximum frame size (macroblocks) | Maximum video bit rate for video coding layer (VCL) (Constrained Baseline, Baseline, Extended and Main Profiles) (kbits/s) | Examples for high resolution @ highest frame rate (maximum stored frames) Toggle additional details |
|---|---|---|---|---|
| 1 | 1,485 | 99 | 64 | 128×96@30.9 (8)176×144@15.0 (4) |
| 1b | 1,485 | 99 | 128 | 128×96@30.9 (8)176×144@15.0 (4) |
| 1.1 | 3,000 | 396 | 192 | 176×144@30.3 (9) 320×240@10.0 (3)352×288@7.5 (2) |
| 1.2 | 6,000 | 396 | 384 | 320×240@20.0 (7)352×288@15.2 (6) |
| 1.3 | 11,880 | 396 | 768 | 320×240@36.0 (7)352×288@30.0 (6) |
| 2 | 11,880 | 396 | 2,000 | 320×240@36.0 (7)352×288@30.0 (6) |
| 2.1 | 19,800 | 792 | 4,000 | 352×480@30.0 (7)352×576@25.0 (6) |
| 2.2 | 20,250 | 1,620 | 4,000 | 352×480@30.7 (12) 352×576@25.6 (10) 720×480@15.0 (6)720×576@12.5 (5) |
| 3 | 40,500 | 1,620 | 10,000 | 352×480@61.4 (12) 352×576@51.1 (10) 720×480@30.0 (6)720×576@25.0 (5) |
| 3.1 | 108,000 | 3,600 | 14,000 | 720×480@80.0 (13) 720×576@66.7 (11)1,280×720@30.0 (5) |
| 3.2 | 216,000 | 5,120 | 20,000 | 1,280×720@60.0 (5)1,280×1,024@42.2 (4) |
| 4 | 245,760 | 8,192 | 20,000 | 1,280×720@68.3 (9) 1,920×1,080@30.1 (4)2,048×1,024@30.0 (4) |
| 4.1 | 245,760 | 8,192 | 50,000 | 1,280×720@68.3 (9) 1,920×1,080@30.1 (4)2,048×1,024@30.0 (4) |
| 4.2 | 522,240 | 8,704 | 50,000 | 1,280×720@145.1 (9) 1,920×1,080@64.0 (4)2,048×1,080@60.0 (4) |
| 5 | 589,824 | 22,080 | 135,000 | 1,920×1,080@72.3 (13) 2,048×1,024@72.0 (13) 2,048×1,080@67.8 (12) 2,560×1,920@30.7 (5)3,672×1,536@26.7 (5) |
| 5.1 | 983,040 | 36,864 | 240,000 | 1,920×1,080@120.5 (16) 2,560×1,920@51.2 (9) 3,840×2,160@31.7 (5) 4,096×2,048@30.0 (5) 4,096×2,160@28.5 (5)4,096×2,304@26.7 (5) |
| 5.2 | 2,073,600 | 36,864 | 240,000 | 1,920×1,080@172.0 (16) 2,560×1,920@108.0 (9) 3,840×2,160@66.8 (5) 4,096×2,048@63.3 (5) 4,096×2,160@60.0 (5)4,096×2,304@56.3 (5) |
| 6 | 4,177,920 | 139,264 | 240,000 | 3,840×2,160@128.9 (16) 7,680×4,320@32.2 (5)8,192×4,320@30.2 (5) |
| 6.1 | 8,355,840 | 139,264 | 480,000 | 3,840×2,160@257.9 (16) 7,680×4,320@64.5 (5)8,192×4,320@60.4 (5) |
| 6.2 | 16,711,680 | 139,264 | 800,000 | 3,840×2,160@300.0 (16) 7,680×4,320@128.9 (5)8,192×4,320@120.9 (5) |

The maximum bit rate for the High Profile is 1.25 times that of the Constrained Baseline, Baseline, Extended and Main Profiles; 3 times for Hi10P, and 4 times for Hi422P/Hi444PP.

The number of luma samples is 16×16=256 times the number of macroblocks (and the number of luma samples per second is 256 times the number of macroblocks per second).

### Decoded picture buffering

Previously encoded pictures are used by H.264/AVC encoders to provide predictions of the values of samples in other pictures. This allows the encoder to make efficient decisions on the best way to encode a given picture. At the decoder, such pictures are stored in a virtual *decoded picture buffer* (DPB). The maximum capacity of the DPB, in units of frames (or pairs of fields), as shown in parentheses in the right column of the table above, can be computed as follows:

DpbCapacity

= min(floor(

MaxDpbMbs

/ (

PicWidthInMbs

*

FrameHeightInMbs

)), 16)

Where *MaxDpbMbs* is a constant value provided in the table below as a function of level number, and *PicWidthInMbs* and *FrameHeightInMbs* are the picture width and frame height for the coded video data, expressed in units of macroblocks (rounded up to integer values and accounting for cropping and macroblock pairing when applicable). This formula is specified in sections A.3.1.h and A.3.2.f of the 2017 edition of the standard.

Level

1

1b

1.1

1.2

1.3

2

2.1

2.2

3

3.1

3.2

4

4.1

4.2

5

5.1

5.2

6

6.1

6.2

MaxDpbMbs

396

396

900

2,376

2,376

2,376

4,752

8,100

8,100

18,000

20,480

32,768

32,768

34,816

110,400

184,320

184,320

696,320

696,320

696,320

For example, for an HDTV picture that is 1,920 samples wide (PicWidthInMbs = 120) and 1,080 samples high (FrameHeightInMbs = 68), a Level 4 decoder has a maximum DPB storage capacity of floor(32768/(120*68)) = 4 frames (or 8 fields). Thus, the value 4 is shown in parentheses in the table above in the right column of the row for Level 4 with the frame size 1920×1080.

The current picture being decoded is *not included* in the computation of DPB fullness (unless the encoder has indicated for it to be stored for use as a reference for decoding other pictures or for delayed output timing). Thus, a decoder needs to actually have sufficient memory to handle (at least) one frame *more* than the maximum capacity of the DPB as calculated above.

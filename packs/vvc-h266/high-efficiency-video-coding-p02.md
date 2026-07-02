---
title: "High Efficiency Video Coding (part 2/2)"
source: https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding
domain: vvc-h266
license: CC-BY-SA-4.0
tags: versatile video coding, h.266 codec, vvc coding tree unit, vvc video compression
fetched: 2026-07-02
part: 2/2
---

## Profiles

Feature support in some of the video profiles

Feature

Version 1

Version 2

Main

Main 10

Main 12

Main

4:2:2 10

Main

4:2:2 12

Main

4:4:4

Main

4:4:4 10

Main

4:4:4 12

Main

4:4:4 16

Intra

Bit depth

8

8 to 10

8 to 12

8 to 10

8 to 12

8

8 to 10

8 to 12

8 to 16

Chroma sampling

formats

4:2:0

4:2:0

4:2:0

4:2:0/

4:2:2

4:2:0/

4:2:2

4:2:0/

4:2:2/

4:4:4

4:2:0/

4:2:2/

4:4:4

4:2:0/

4:2:2/

4:4:4

4:2:0/

4:2:2/

4:4:4

4:0:0 (

Monochrome

)

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

High precision weighted prediction

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Chroma QP offset list

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Cross-component prediction

No

No

No

No

No

Yes

Yes

Yes

Yes

Intra smoothing disabling

No

No

No

No

No

Yes

Yes

Yes

Yes

Persistent Rice adaptation

No

No

No

No

No

Yes

Yes

Yes

Yes

RDPCM implicit/explicit

No

No

No

No

No

Yes

Yes

Yes

Yes

Transform skip block sizes larger than 4×4

No

No

No

No

No

Yes

Yes

Yes

Yes

Transform skip context/rotation

No

No

No

No

No

Yes

Yes

Yes

Yes

Extended precision processing

No

No

No

No

No

No

No

No

Yes

Version 1 of the HEVC standard defines three profiles: **Main**, **Main 10**, and **Main Still Picture**. Version 2 of HEVC adds 21 range extensions profiles, two scalable extensions profiles, and one multi-view profile. HEVC also contains provisions for additional profiles. Extensions that were added to HEVC include increased bit depth, 4:2:2/4:4:4 chroma sampling, Multiview Video Coding (MVC), and Scalable Video Coding (SVC). The HEVC range extensions, HEVC scalable extensions, and HEVC multi-view extensions were completed in July 2014. In July 2014 a draft of the second version of HEVC was released. Screen content coding (SCC) extensions were under development for screen content video, which contains text and graphics, with an expected final draft release date of 2015.

A profile is a defined set of coding tools that can be used to create a bitstream that conforms to that profile. An encoder for a profile may choose which coding tools to use as long as it generates a conforming bitstream while a decoder for a profile must support all coding tools that can be used in that profile.

### Version 1 profiles

#### Main

The Main profile allows for a bit depth of 8 bits per sample with 4:2:0 chroma sampling, which is the most common type of video used with consumer devices.

#### Main 10

The Main 10 (`Main10`) profile was added at the October 2012 HEVC meeting based on a multicompany proposal JCTVC-K0109 which proposed that a 10-bit profile be added to HEVC for consumer applications. The proposal said this was to allow for improved video quality and to support the Rec. 2020 color space that has become widely used in UHDTV systems and to be able to deliver HDR and color fidelity avoiding the banding artifacts. A variety of companies supported the proposal which included Ateme, BBC, BSkyB, Cisco, DirecTV, Ericsson, Motorola Mobility, NGCodec, NHK, RAI, ST, SVT, Thomson Video Networks, Technicolor, and ViXS Systems. The Main 10 profile allows for a bit depth of 8 to 10 bits per sample with 4:2:0 chroma sampling to support consumer use cases. HEVC decoders that conform to the Main 10 profile must be capable of decoding bitstreams made with the following profiles: Main and Main 10. A higher bit depth allows for a greater number of colors. 8 bits per sample allows for 256 shades per primary color (a total of 16.78 million colors) while 10 bits per sample allows for 1024 shades per primary color (a total of 1.07 billion colors). A higher bit depth allows for a smoother transition of color which resolves the problem known as color banding.

The Main 10 profile allows for improved video quality since it can support video with a higher bit depth than what is supported by the Main profile. Additionally, in the Main 10 profile 8-bit video can be coded with a higher bit depth of 10 bits, which allows improved coding efficiency compared to the Main profile.

Ericsson said the Main 10 profile would bring the benefits of 10 bits per sample video to consumer TV. They also said that for higher resolutions there is no bit rate penalty for encoding video at 10 bits per sample. Imagination Technologies said that 10-bit per sample video would allow for larger color spaces and is required for the Rec. 2020 color space that will be used by UHDTV. They also said the Rec. 2020 color space would drive the widespread adoption of 10-bit-per-sample video.

In a PSNR based performance comparison released in April 2013 the Main 10 profile was compared to the Main profile using a set of 3840×2160 10-bit video sequences. The 10-bit video sequences were converted to 8 bits for the Main profile and remained at 10 bits for the Main 10 profile. The reference PSNR was based on the original 10-bit video sequences. In the performance comparison the Main 10 profile provided a 5% bit rate reduction for inter frame video coding compared to the Main profile. The performance comparison states that for the tested video sequences the Main 10 profile outperformed the Main profile.

#### Main Still Picture

| Still image coding standard (test method) | Average bit rate reduction compared to |   |
|---|---|---|
| JPEG 2000 | JPEG |   |
| HEVC (PSNR) | 20% | 62% |
| HEVC (MOS) | 31% | 43% |

The Main Still Picture (`MainStillPicture`) profile allows for a single still picture to be encoded with the same constraints as the Main profile. As a subset of the Main profile the Main Still Picture profile allows for a bit depth of 8 bits per sample with 4:2:0 chroma sampling. An objective performance comparison was done in April 2012 in which HEVC reduced the average bit rate for images by 56% compared to JPEG. A PSNR based performance comparison for still image compression was done in May 2012 using the HEVC HM 6.0 encoder and the reference software encoders for the other standards. For still images HEVC reduced the average bit rate by 15.8% compared to H.264/MPEG-4 AVC, 22.6% compared to JPEG 2000, 30.0% compared to JPEG XR, 31.0% compared to WebP, and 43.0% compared to JPEG.

A performance comparison for still image compression was done in January 2013 using the HEVC HM 8.0rc2 encoder, Kakadu version 6.0 for JPEG 2000, and IJG version 6b for JPEG. The performance comparison used PSNR for the objective assessment and mean opinion score (MOS) values for the subjective assessment. The subjective assessment used the same test methodology and images as those used by the JPEG committee when it evaluated JPEG XR. For 4:2:0 chroma sampled images the average bit rate reduction for HEVC compared to JPEG 2000 was 20.26% for PSNR and 30.96% for MOS while compared to JPEG it was 61.63% for PSNR and 43.10% for MOS.

A PSNR based HEVC performance comparison for still image compression was done in April 2013 by Nokia. HEVC has a larger performance improvement for higher resolution images than lower resolution images and a larger performance improvement for lower bit rates than higher bit rates. For lossy compression to get the same PSNR as HEVC took on average 1.4× more bits with JPEG 2000, 1.6× more bits with JPEG-XR, and 2.3× more bits with JPEG.

A compression efficiency study of HEVC, JPEG, JPEG XR, and WebP was done in October 2013 by Mozilla. The study showed that HEVC was significantly better at compression than the other image formats that were tested. Four different methods for comparing image quality were used in the study which were Y-SSIM, RGB-SSIM, IW-SSIM, and PSNR-HVS-M.

### Version 2 profiles

Version 2 of HEVC adds 21 range extensions profiles, two scalable extensions profiles, and one multi-view profile: **Monochrome**, **Monochrome 12**, **Monochrome 16**, **Main 12**, **Main 4:2:2 10**, **Main 4:2:2 12**, **Main 4:4:4**, **Main 4:4:4 10**, **Main 4:4:4 12**, **Monochrome 12 Intra**, **Monochrome 16 Intra**, **Main 12 Intra**, **Main 4:2:2 10 Intra**, **Main 4:2:2 12 Intra**, **Main 4:4:4 Intra**, **Main 4:4:4 10 Intra**, **Main 4:4:4 12 Intra**, **Main 4:4:4 16 Intra**, **Main 4:4:4 Still Picture**, **Main 4:4:4 16 Still Picture**, **High Throughput 4:4:4 16 Intra**, **Scalable Main**, **Scalable Main 10**, and **Multiview Main**. All of the inter frame range extensions profiles have an Intra profile.

**Monochrome**

The Monochrome profile allows for a bit depth of 8 bits per sample with support for 4:0:0 chroma sampling.

**Monochrome 12**

The Monochrome 12 profile allows for a bit depth of 8 bits to 12 bits per sample with support for 4:0:0 chroma sampling.

**Monochrome 16**

The Monochrome 16 profile allows for a bit depth of 8 bits to 16 bits per sample with support for 4:0:0 chroma sampling. HEVC decoders that conform to the Monochrome 16 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Monochrome 12, and Monochrome 16.

**Main 12**

The Main 12 profile allows for a bit depth of 8 bits to 12 bits per sample with support for 4:0:0 and 4:2:0 chroma sampling. HEVC decoders that conform to the Main 12 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Monochrome 12, Main, Main 10, and Main 12.

**Main 4:2:2 10**

The Main 4:2:2 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0, 4:2:0, and 4:2:2 chroma sampling. HEVC decoders that conform to the Main 4:2:2 10 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, and Main 4:2:2 10.

**Main 4:2:2 12**

The Main 4:2:2 12 profile allows for a bit depth of 8 bits to 12 bits per sample with support for 4:0:0, 4:2:0, and 4:2:2 chroma sampling. HEVC decoders that conform to the Main 4:2:2 12 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Monochrome 12, Main, Main 10, Main 12, Main 4:2:2 10, and Main 4:2:2 12.

**Main 4:4:4**

The Main 4:4:4 profile allows for a bit depth of 8 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Main 4:4:4 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, and Main 4:4:4.

**Main 4:4:4 10**

The Main 4:4:4 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Main 4:4:4 10 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Main 4:2:2 10, Main 4:4:4, and Main 4:4:4 10.

**Main 4:4:4 12**

The Main 4:4:4 12 profile allows for a bit depth of 8 bits to 12 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Main 4:4:4 12 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Main 12, Main 4:2:2 10, Main 4:2:2 12, Main 4:4:4, Main 4:4:4 10, Main 4:4:4 12, and Monochrome 12.

**Main 4:4:4 16 Intra**

The Main 4:4:4 16 Intra profile allows for a bit depth of 8 bits to 16 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Main 4:4:4 16 Intra profile must be capable of decoding bitstreams made with the following profiles: Monochrome Intra, Monochrome 12 Intra, Monochrome 16 Intra, Main Intra, Main 10 Intra, Main 12 Intra, Main 4:2:2 10 Intra, Main 4:2:2 12 Intra, Main 4:4:4 Intra, Main 4:4:4 10 Intra, and Main 4:4:4 12 Intra.

**High Throughput 4:4:4 16 Intra**

The High Throughput 4:4:4 16 Intra profile allows for a bit depth of 8 bits to 16 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The High Throughput 4:4:4 16 Intra profile has an

HbrFactor

12 times higher than other HEVC profiles, allowing it to have a maximum bit rate 12 times higher than the Main 4:4:4 16 Intra profile.

The High Throughput 4:4:4 16 Intra profile is designed for high end professional content creation and decoders for this profile are not required to support other profiles.

**Main 4:4:4 Still Picture**

The Main 4:4:4 Still Picture profile allows for a single still picture to be encoded with the same constraints as the Main 4:4:4 profile. As a

subset

of the Main 4:4:4 profile, the Main 4:4:4 Still Picture profile allows for a bit depth of 8 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling.

**Main 4:4:4 16 Still Picture**

The Main 4:4:4 16 Still Picture profile allows for a single still picture to be encoded with the same constraints as the Main 4:4:4 16 Intra profile. As a

subset

of the Main 4:4:4 16 Intra profile, the Main 4:4:4 16 Still Picture profile allows for a bit depth of 8 bits to 16 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling.

**Scalable Main**

The Scalable Main profile allows for a base layer that conforms to the Main profile of HEVC.

**Scalable Main 10**

The Scalable Main 10 profile allows for a base layer that conforms to the Main 10 profile of HEVC.

**Multiview Main**

The Multiview Main profile allows for a base layer that conforms to the Main profile of HEVC.

### Version 3 and higher profiles

Version 3 of HEVC added one 3D profile: **3D Main**. The February 2016 draft of the screen content coding extensions added seven screen content coding extensions profiles, three high throughput extensions profiles, and four scalable extensions profiles: **Screen-Extended Main**, **Screen-Extended Main 10**, **Screen-Extended Main 4:4:4**, **Screen-Extended Main 4:4:4 10**, **Screen-Extended High Throughput 4:4:4**, **Screen-Extended High Throughput 4:4:4 10**, **Screen-Extended High Throughput 4:4:4 14**, **High Throughput 4:4:4**, **High Throughput 4:4:4 10**, **High Throughput 4:4:4 14**, **Scalable Monochrome**, **Scalable Monochrome 12**, **Scalable Monochrome 16**, and **Scalable Main 4:4:4**.

**3D Main**

The 3D Main profile allows for a base layer that conforms to the Main profile of HEVC.

**Screen-Extended Main**

The Screen-Extended Main profile allows for a bit depth of 8 bits per sample with support for 4:0:0 and 4:2:0 chroma sampling. HEVC decoders that conform to the Screen-Extended Main profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, and Screen-Extended Main.

**Screen-Extended Main 10**

The Screen-Extended Main 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0 and 4:2:0 chroma sampling. HEVC decoders that conform to the Screen-Extended Main 10 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Screen-Extended Main, and Screen-Extended Main 10.

**Screen-Extended Main 4:4:4**

The Screen-Extended Main 4:4:4 profile allows for a bit depth of 8 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Screen-Extended Main 4:4:4 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 4:4:4, Screen-Extended Main, and Screen-Extended Main 4:4:4.

**Screen-Extended Main 4:4:4 10**

The Screen-Extended Main 4:4:4 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. HEVC decoders that conform to the Screen-Extended Main 4:4:4 10 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Main 4:2:2 10, Main 4:4:4, Main 4:4:4 10, Screen-Extended Main, Screen-Extended Main 10, Screen-Extended Main 4:4:4, and Screen-Extended Main 4:4:4 10.

**Screen-Extended High Throughput 4:4:4**

The Screen-Extended High Throughput 4:4:4 profile allows for a bit depth of 8 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The Screen-Extended High Throughput 4:4:4 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles allowing it to have a maximum bit rate 6 times higher than the Main 4:4:4 profile. HEVC decoders that conform to the Screen-Extended High Throughput 4:4:4 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 4:4:4, Screen-Extended Main, Screen-Extended Main 4:4:4, Screen-Extended High Throughput 4:4:4, and High Throughput 4:4:4.

**Screen-Extended High Throughput 4:4:4 10**

The Screen-Extended High Throughput 4:4:4 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The Screen-Extended High Throughput 4:4:4 10 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles allowing it to have a maximum bit rate 6 times higher than the Main 4:4:4 10 profile. HEVC decoders that conform to the Screen-Extended High Throughput 4:4:4 10 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Main 4:2:2 10, Main 4:4:4, Main 4:4:4 10, Screen-Extended Main, Screen-Extended Main 10, Screen-Extended Main 4:4:4, Screen-Extended Main 4:4:4 10, Screen-Extended High Throughput 4:4:4, Screen-Extended High Throughput 4:4:4 10, High Throughput 4:4:4, and High Throughput 4:4:4.

**Screen-Extended High Throughput 4:4:4 14**

The Screen-Extended High Throughput 4:4:4 14 profile allows for a bit depth of 8 bits to 14 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The Screen-Extended High Throughput 4:4:4 14 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles. HEVC decoders that conform to the Screen-Extended High Throughput 4:4:4 14 profile must be capable of decoding bitstreams made with the following profiles: Monochrome, Main, Main 10, Main 4:2:2 10, Main 4:4:4, Main 4:4:4 10, Screen-Extended Main, Screen-Extended Main 10, Screen-Extended Main 4:4:4, Screen-Extended Main 4:4:4 10, Screen-Extended High Throughput 4:4:4, Screen-Extended High Throughput 4:4:4 10, Screen-Extended High Throughput 4:4:4 14, High Throughput 4:4:4, High Throughput 4:4:4 10, and High Throughput 4:4:4 14.

**High Throughput 4:4:4**

The High Throughput 4:4:4 profile allows for a bit depth of 8 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The High Throughput 4:4:4 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles allowing it to have a maximum bit rate 6 times higher than the Main 4:4:4 profile. HEVC decoders that conform to the High Throughput 4:4:4 profile must be capable of decoding bitstreams made with the following profiles: High Throughput 4:4:4.

**High Throughput 4:4:4 10**

The High Throughput 4:4:4 10 profile allows for a bit depth of 8 bits to 10 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The High Throughput 4:4:4 10 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles allowing it to have a maximum bit rate 6 times higher than the Main 4:4:4 10 profile. HEVC decoders that conform to the High Throughput 4:4:4 10 profile must be capable of decoding bitstreams made with the following profiles: High Throughput 4:4:4 and High Throughput 4:4:4 10.

**High Throughput 4:4:4 14**

The High Throughput 4:4:4 14 profile allows for a bit depth of 8 bits to 14 bits per sample with support for 4:0:0, 4:2:0, 4:2:2, and 4:4:4 chroma sampling. The High Throughput 4:4:4 14 profile has an HbrFactor 6 times higher than most inter frame HEVC profiles. HEVC decoders that conform to the High Throughput 4:4:4 14 profile must be capable of decoding bitstreams made with the following profiles: High Throughput 4:4:4, High Throughput 4:4:4 10, and High Throughput 4:4:4 14.

**Scalable Monochrome**

The Scalable Monochrome profile allows for a base layer that conforms to the Monochrome profile of HEVC.

**Scalable Monochrome 12**

The Scalable Monochrome 12 profile allows for a base layer that conforms to the Monochrome 12 profile of HEVC.

**Scalable Monochrome 16**

The Scalable Monochrome 16 profile allows for a base layer that conforms to the Monochrome 16 profile of HEVC.

**Scalable Main 4:4:4**

The Scalable Main 4:4:4 profile allows for a base layer that conforms to the Main 4:4:4 profile of HEVC.


## Tiers and levels

The HEVC standard defines two tiers, Main and High, and thirteen levels. A level is a set of constraints for a bitstream. For levels below level 4 only the Main tier is allowed. The Main tier is a lower tier than the High tier. The tiers were made to deal with applications that differ in terms of their maximum bit rate. The Main tier was designed for most applications while the High tier was designed for very demanding applications. A decoder that conforms to a given tier/level is required to be capable of decoding all bitstreams that are encoded for that tier/level and for all lower tiers/levels.

| Level | Max luma sample rate (samples/s) | Max luma picture size (samples) | Max bit rate for Main and Main 10 profiles (kbit/s)[A] | Example picture resolution @ highest frame rate[B] (MaxDpbSize[C]) More/Fewer examples |   |
|---|---|---|---|---|---|
| Main tier | High tier |   |   |   |   |
| 1 | 552,960 | 36,864 | 128 | – | 128×96@33.7 (6) 176×144@15 (6) |
| 2 | 3,686,400 | 122,880 | 1,500 | – | 176×144@100 (16) 352×288@30 (6) |
| 2.1 | 7,372,800 | 245,760 | 3,000 | – | 352×288@60 (12) 640×360@30 (6) |
| 3 | 16,588,800 | 552,960 | 6,000 | – | 640×360@67.5 (12) 720×576@37.5 (8) 960×540@30 (6) |
| 3.1 | 33,177,600 | 983,040 | 10,000 | – | 720×576@75 (12) 960×540@60 (8) 1280×720@33.7 (6) |
| 4 | 66,846,720 | 2,228,224 | 12,000 | 30,000 | 1,280×720@68 (12) 1,920×1,080@32 (6) 2,048×1,080@30.0 (6) |
| 4.1 | 133,693,440 | 20,000 | 50,000 | 1,280×720@136 (12) 1,920×1,080@64 (6) 2,048×1,080@60 (6) |   |
| 5 | 267,386,880 | 8,912,896 | 25,000 | 100,000 | 1,920×1,080@128 (16) 3,840×2,160@32 (6) 4,096×2,160@30 (6) |
| 5.1 | 534,773,760 | 40,000 | 160,000 | 1,920×1,080@256 (16) 3,840×2,160@64 (6) 4,096×2,160@60 (6) |   |
| 5.2 | 1,069,547,520 | 60,000 | 240,000 | 1,920×1,080@300 (16) 3,840×2,160@128 (6) 4,096×2,160@120 (6) |   |
| 6 | 1,069,547,520 | 35,651,584 | 60,000 | 240,000 | 3,840×2,160@128 (16) 7,680×4,320@32 (6) 8,192×4,320@30 (6) |
| 6.1 | 2,139,095,040 | 120,000 | 480,000 | 3,840×2,160@256 (16) 7,680×4,320@64 (6) 8,192×4,320@60 (6) |   |
| 6.2 | 4,278,190,080 | 240,000 | 800,000 | 3,840×2,160@300 (16) 7,680×4,320@128 (6) 8,192×4,320@120 (6) |   |

A

The maximum bit rate of the profile is based on the combination of bit depth, chroma sampling, and the type of profile. For bit depth the maximum bit rate increases by 1.5× for 12-bit profiles and 2× for 16-bit profiles. For chroma sampling the maximum bit rate increases by 1.5× for 4:2:2 profiles and 2× for 4:4:4 profiles. For the Intra profiles the maximum bit rate increases by 2×.

B

The maximum frame rate supported by HEVC is 300 fps.

C

The MaxDpbSize is the maximum number of pictures in the decoded picture buffer.

### Decoded picture buffer

Previously decoded pictures are stored in a decoded picture buffer (DPB), and are used by HEVC encoders to form predictions for subsequent pictures. The maximum number of pictures that can be stored in the DPB, called the DPB capacity, is 6 (including the current picture) for all HEVC levels when operating at the maximum picture size supported by the level. The DPB capacity (in units of pictures) increases from 6 to 8, 12, or 16 as the picture size decreases from the maximum picture size supported by the level. The encoder selects which specific pictures are retained in the DPB on a picture-by-picture basis, so the encoder has the flexibility to determine for itself the best way to use the DPB capacity when encoding the video content.


## Containers

MPEG has published an amendment which added HEVC support to the MPEG transport stream used by ATSC, DVB, and Blu-ray Disc; MPEG decided not to update the MPEG program stream used by DVD-Video. MPEG has also added HEVC support to the ISO base media file format. HEVC is also supported by the MPEG media transport standard. Support for HEVC was added to Matroska starting with the release of MKVToolNix v6.8.0 after a patch from DivX was merged. A draft document has been submitted to the Internet Engineering Task Force which describes a method to add HEVC support to the Real-time Transport Protocol.

Using HEVC's intra frame encoding, a still-image coded format called Better Portable Graphics (BPG) has been proposed by the programmer Fabrice Bellard. It is essentially a wrapper for images coded using the HEVC Main 4:4:4 16 Still Picture profile with up to 14 bits per sample, although it uses an abbreviated header syntax and adds explicit support for Exif, ICC profiles, and XMP metadata.


## Patent license terms

License terms and fees for HEVC patents, compared with its main competitors:

| Video format | Licensor | Codec royalties | Codec royalty exemptions | Codec royalty annual cap | Content distribution fee |
|---|---|---|---|---|---|
| **HEVC** | Via-LA | ▪ US$0.20 per unit | ▪ First 100k units each year | ▪ US$25 million | ▪ US$0 |
| Access Advance | **Region 1**: ▪ US$0.40 (mobile) ▪ US$1.20 (4K TV) ▪ US$0.20-0.80 (other) **Region 2**: ▪ US$0.20 (mobile) ▪ US$0.60 (4K TV) ▪ US$0.20–0.40 (other) | ▪ US$25,000 each year ▪ Most software HEVC implementation distributed to consumer devices after first sale | ▪ US$40 million | **Physical distribution**: ▪ $0.0225 per disc/title (Region 1) ▪ $0.01125 per disc/title (Region 2) **Non-physical distribution**: ▪ US$0 |   |
| Technicolor | tailor-made agreements | ▪ US$0 |   |   |   |
| Velos Media | ? | ▪ Presumed to charge royalty |   |   |   |
| others (AT&T, Microsoft, Motorola, Nokia, Cisco, ...) | ? |   |   |   |   |
| **AVC** | Via-LA | **Codecs to end users and OEM for PC but not part of PC OS**: ▪ US$0.20: 100k+ units/year ▪ US$0.10: 5M+ units/year **Branded OEM Codecs for PC OS**: ▪ US$0.20: 100k+ units/year ▪ US$0.10: 5M+ units/year | **Codecs to end users and OEM for PC but not part of PC OS**: ▪ First 100k units each year **Branded OEM Codecs for PC OS**: ▪ First 100k units each year | **Codecs to end users and OEM for PC but not part of PC OS**: ▪ US$9.75 million (for 2017-20 period) **Branded OEM Codecs for PC OS**: ▪ US$9.75 million (for 2017-20 period) | **Free Television**: ▪ one time $2,500 per transmission encoder, or ▪ $2,500...$10,000 annual fee **Internet Broadcast**: ▪ US$0 **Paid Subscriber Model**: ▪  00000$0/yr: 000k...100k subscribers ▪ 0$25,000/yr: 100k...250k subscribers ▪ 0$50,000/yr: 250k...500k subscribers ▪ 0$75,000/yr: 500k...1M subscribers ▪ $100,000/yr: 1M+ subscribers **Paid by Title Model**: ▪ 0...12 min: no royalty ▪ 12+ min: lower of 2% or US$0.02/title **Maximum Annual Content Related Royalty**: ▪ US$8.125 million |
| others (Nokia, Qualcomm, Broadcomm, Blackberry, Texas Instruments, MIT) | ? |   |   |   |   |
| **AV1** | Alliance for Open Media | ▪ US$0 | —N/a | ▪ US$0 |   |
| **Daala** | Mozilla & Xiph.org | ▪ US$0 | —N/a | ▪ US$0 |   |
| **VP9** | Google | ▪ US$0 | —N/a | ▪ US$0 |   |

### Provision for costless software

As with its predecessor AVC, software distributors that implement HEVC in products must pay a price per distributed copy.[i] While this licensing model is manageable for paid software, it is an obstacle to most free and open-source software, which is meant to be freely distributable. In the opinion of MulticoreWare, the developer of x265, enabling royalty-free software encoders and decoders is in the interest of accelerating HEVC adoption. HEVC Advance made an exception that specifically waives the royalties on software-only implementations (both decoders and encoders) when not bundled with hardware. However, the exempted software is not free from the licensing obligations of other patent holders (e.g. members of the MPEG LA pool).

While the obstacle to free software is no concern in for example TV broadcast networks, this problem, combined with the prospect of future collective lock-in to the format, makes several organizations like Mozilla (see OpenH264) and the Free Software Foundation Europe wary of royalty-bearing formats for internet use. Competing formats intended for internet use (VP9 and AV1) are intended to steer clear of these concerns by being royalty free (provided there are no third-party claims of patent rights).

**^i**: Regardless of how the software is licensed from the software authors (see software licensing), if what it does is patented, its use remains bound by the patent holders' rights unless the use of the patents has been authorized by a license.

### Controversy

Since November 2025, Dell and HP announced they will disable HEVC hardware decoding features in UEFI/BIOS level for some entry and middle-end laptops, due to HEVC license fee increases.


## Versatile Video Coding

In October 2015, MPEG and VCEG formed Joint Video Exploration Team (JVET) to evaluate available compression technologies and study the requirements for a next-generation video compression standard. The new algorithm should have 30–50% better compression rate for the same perceptual quality, with support for lossless and subjectively lossless compression. It should also support YCbCr 4:4:4, 4:2:2 and 4:2:0 with 10 to 16 bits per component, BT.2100 wide color gamut and high dynamic range (HDR) of more than 16 stops (with peak brightness of 1,000, 4,000 and 10,000 nits), auxiliary channels (for depth, transparency, etc.), variable and fractional frame rates from 0 to 120 Hz, scalable video coding for temporal (frame rate), spatial (resolution), SNR, color gamut and dynamic range differences, stereo/multiview coding, panoramic formats, and still picture coding. Encoding complexity of 10 times that of HEVC is expected. JVET issued a final "Call for Proposals" in October 2017, with the first working draft of the Versatile Video Coding (VVC) standard released in April 2018. The VVC standard was finalized on July 6, 2020.

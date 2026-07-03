---
title: "HDMI (part 2/2)"
source: https://en.wikipedia.org/wiki/HDMI
domain: hdmi
license: CC-BY-SA-4.0
tags: hdmi
fetched: 2026-07-03
part: 2/2
---

## Resolution and refresh frequency limits

### Refresh frequency limits for common resolutions

The maximum limits for TMDS transmission are calculated using standard data rate calculations. For FRL transmission, the limits are calculated using the capacity computation algorithm provided by the HDMI Specification. All calculations assume uncompressed RGB video with CVT-RB v2 timing. Maximum limits may differ if compression (i.e. DSC) or Y′CBCR 4:2:0 chroma subsampling are used.

Display manufacturers may also use non-standard blanking intervals (a Vendor-Specific Timing Format as defined in the HDMI Specification) rather than CVT-RB v2 to achieve even higher frequencies when bandwidth is a constraint. The refresh frequencies in the below table do not represent the absolute maximum limit of each interface, but rather an estimate based on a modern standardized timing formula. The minimum blanking intervals (and therefore the exact maximum frequency that can be achieved) will depend on the display and how many secondary data packets it requires, and therefore will differ from model to model.

Video format

TMDS character rate; maximum data rate

FRL transmission mode; maximum data rate

Shorthand

Resolution

Channel

color

depth

(bits)

165

MHz TMDS

340

MHz TMDS

600

MHz TMDS

FRL 9G

FRL 18G

FRL 24G

FRL 32G

FRL 40G

FRL 48G

FRL 64G

FRL 80G

FRL 96G

3.96 Gbit/s

8.16 Gbit/s

14.4 Gbit/s

7.88 Gbit/s

15.8 Gbit/s

21.0 Gbit/s

28.0 Gbit/s

35.0 Gbit/s

42.0 Gbit/s

56.0 Gbit/s

70.0 Gbit/s

84.0 Gbit/s

Maximum refresh frequency with CVT-RB v2 timing (Hz)

1080p

1920 × 1080

8

73

146

246

143

268

343

435

518

593

725

836

932

10

59

118

201

116

220

284

363

436

503

623

726

817

1440p

2560 × 1440

8

42

85

147

83

160

209

270

327

381

480

569

649

10

34

69

119

67

130

170

222

270

316

402

481

553

UWQHD

3440 × 1440

8

32

65

112

63

122

160

208

254

298

380

456

525

10

25

52

90

50

99

130

170

208

246

316

381

442

4K

3840 × 2160

8

39

68

38

75

98

129

159

189

245

297

348

10

31

55

30

60

79

105

130

154

200

245

288

5K

5120 × 2880

8

39

43

56

75

93

111

145

178

211

10

31

34

45

60

75

89

118

145

172

8K

7680 × 4320

8

25

34

42

50

67

83

99

10

27

34

40

54

67

80

10K

10240 × 4320

8

25

32

38

51

63

75

10

25

30

41

51

61

0–59

Hz

60–119

Hz

120–239

Hz

240+

Hz

1. 165 MHz was the maximum TMDS character rate allowed in version 1.2a of the HDMI Specification and earlier. In version 1.3, the maximum allowed speed was increased to 340 MHz, and in version 2.0 it was increased to 600 MHz. These are only the maximum speeds permitted by the specification; individual devices may be limited to any speed within the maximum allowed.
2. Calculations are based on uncompressed RGB video with 8 channels of LPCM audio

### Refresh frequency limits for standard video

HDMI 1.0 and 1.1 are restricted to transmitting only certain video formats, defined in EIA/CEA-861-B and in the HDMI Specification itself. HDMI 1.2 and all later versions allow any arbitrary resolution and frame rate (within the bandwidth limit). Formats that are not supported by the HDMI Specification (i.e., no standardized timings defined) may be implemented as a vendor-specific format. Successive versions of the HDMI Specification continue to add support for additional formats (such as 4K resolutions), but the added support is to establish standardized timings to ensure interoperability between products, not to establish which formats are or are not permitted. Video formats do not require explicit support from the HDMI Specification in order to be transmitted and displayed.

Individual products may have heavier limitations than those listed below, since HDMI devices are not required to support the maximum bandwidth of the HDMI version that they implement. Therefore, it is not guaranteed that a display will support the refresh rates listed in this table, even if the display has the required HDMI version.

Uncompressed 8 bpc (24 bit/px) color depth and RGB or Y′CBCR 4:4:4 color format are assumed on this table except where noted.

Video format

HDMI version / maximum data rate / cable certification

Shorthand

Resolution

Refresh rate (Hz)

Data rate required

1.0–1.1

1.2–1.2a

1.3–1.4b

2.0–2.0b

2.1–2.1b

2.2

3.96 Gbit/s

8.16

Gbit/s

14.4

Gbit/s

42.0

Gbit/s

84.0

Gbit/s

High speed

Premium high speed

Ultra high speed

Ultra96

720p

1280 × 720

30

720

Mbit/s

Yes

Yes

Yes

Yes

Yes

Yes

60

1.45

Gbit/s

Yes

Yes

Yes

Yes

Yes

Yes

120

2.99

Gbit/s

No

Yes

Yes

Yes

Yes

Yes

1080p

1920 × 1080

30

1.58

Gbit/s

Yes

Yes

Yes

Yes

Yes

Yes

60

3.20

Gbit/s

Yes

Yes

Yes

Yes

Yes

Yes

120

6.59

Gbit/s

No

No

Yes

Yes

Yes

Yes

144

8.00

Gbit/s

No

No

Yes

Yes

Yes

Yes

240

14.00

Gbit/s

No

No

4:2:0

Yes

Yes

Yes

1440p

2560 × 1440

30

2.78

Gbit/s

No

Yes

Yes

Yes

Yes

Yes

60

5.63

Gbit/s

No

No

Yes

Yes

Yes

Yes

75

7.09

Gbit/s

No

No

Yes

Yes

Yes

Yes

120

11.59

Gbit/s

No

No

4:2:0

Yes

Yes

Yes

144

14.08

Gbit/s

No

No

4:2:0

Yes

Yes

Yes

240

24.62

Gbit/s

No

No

No

4:2:0

Yes

Yes

4K

3840 × 2160

30

6.18

Gbit/s

No

No

Yes

Yes

Yes

Yes

60

12.54

Gbit/s

No

No

4:2:0

Yes

Yes

Yes

75

15.79

Gbit/s

No

No

4:2:0

4:2:0

Yes

Yes

120

25.82

Gbit/s

No

No

No

4:2:0

Yes

Yes

144

31.35

Gbit/s

No

No

No

No

Yes

Yes

240

54.84

Gbit/s

No

No

No

No

DSC

Yes

5K

5120 × 2880

30

10.94

Gbit/s

No

No

4:2:0

Yes

Yes

Yes

60

22.18

Gbit/s

No

No

No

4:2:0

Yes

Yes

120

45.66

Gbit/s

No

No

No

No

DSC

Yes

144

55.44

Gbit/s

No

No

No

No

DSC

Yes

240

96.98

Gbit/s

No

No

No

No

DSC

DSC

8K

7680 × 4320

30

24.48

Gbit/s

No

No

No

4:2:0

Yes

Yes

60

49.65

Gbit/s

No

No

No

No

DSC

Yes

120

102.2

Gbit/s

No

No

No

No

DSC

DSC

144

124.1

Gbit/s

No

No

No

No

4:2:2 + DSC

DSC

240

217.1

Gbit/s

No

No

No

No

No

DSC

10K

10240 × 4320

30

32.55

Gbit/s

No

No

No

No

Yes

Yes

60

66.03

Gbit/s

No

No

No

No

DSC

Yes

100

112.2

Gbit/s

No

No

No

No

DSC

DSC

120

135.9

Gbit/s

No

No

No

No

4:2:2 + DSC

DSC

144

165.0

Gbit/s

No

No

No

No

No

DSC

240

288.7

Gbit/s

No

No

No

No

No

4:2:0 + DSC

1.0–1.1

1.2–1.2a

1.3–1.4b

2.0–2.0b

2.1–2.1b

2.2

HDMI version

1. Uncompressed 8 bpc (24 bit/px) color depth with RGB or Y′CBCR 4:4:4 color format and CVT-RB v2 timing are used to calculate these data rates. Uncompressed data rate for RGB images in bits per second is calculated as bits per pixel × pixels per frame × frames per second. Pixels per frame includes blanking intervals as defined by CVT-RB v2.
2. The Standard HDMI cable certification (Category 1) only tests up to 74.25 MHz (2.2275 Gbit/s). Therefore only High Speed HDMI cables or above are rated for the maximum allowed speed, even for versions that predate the introduction of the High Speed certification.
3. Possible by using Y′CBCR with 4:2:0 subsampling
4. Possible by using Display Stream Compression (DSC)
5. Possible by using Y′CBCR with 4:2:2 subsampling and DSC together, which permits a lower DSC bit rate of 7 bit/px
6. Possible by using Y′CBCR with 4:2:0 subsampling and DSC together, which permits a lower DSC bit rate of 6 bit/px

### Refresh frequency limits for HDR10 video

HDR10 requires 10 bpc (30 bit/px) color depth, which uses 25% more bandwidth than standard 8 bpc video.

Uncompressed 10 bpc color depth and RGB or Y′CBCR 4:4:4 color format are assumed on this table except where noted.

| Video format | HDMI version / maximum data rate |   |   |   |   |   |
|---|---|---|---|---|---|---|
| Shorthand | Resolution | Refresh rate (Hz) | Data rate required | 2.0a–2.0b | 2.1–2.1b | 2.2 |
| 14.4 Gbit/s | 42.0 Gbit/s | 84.0 Gbit/s |   |   |   |   |
| 1080p | 1920 × 1080 | 60 | 4.00 Gbit/s | Yes | Yes | Yes |
| 120 | 8.24 Gbit/s | Yes | Yes | Yes |   |   |
| 144 | 10.00 Gbit/s | Yes | Yes | Yes |   |   |
| 240 | 17.50 Gbit/s | 4:2:0 | Yes | Yes |   |   |
| 1440p | 2560 × 1440 | 60 | 7.04 Gbit/s | Yes | Yes | Yes |
| 100 | 11.96 Gbit/s | Yes | Yes | Yes |   |   |
| 120 | 14.49 Gbit/s | 4:2:0 | Yes | Yes |   |   |
| 144 | 17.60 Gbit/s | 4:2:0 | Yes | Yes |   |   |
| 240 | 30.77 Gbit/s | No | Yes | Yes |   |   |
| 4K | 3840 × 2160 | 50 | 13.00 Gbit/s | Yes | Yes | Yes |
| 60 | 15.68 Gbit/s | 4:2:0 | Yes | Yes |   |   |
| 120 | 32.27 Gbit/s | No | Yes | Yes |   |   |
| 144 | 39.19 Gbit/s | No | Yes | Yes |   |   |
| 240 | 68.56 Gbit/s | No | DSC | Yes |   |   |
| 5K | 5120 × 2880 | 30 | 13.67 Gbit/s | Yes | Yes | Yes |
| 60 | 27.72 Gbit/s | 4:2:0 | Yes | Yes |   |   |
| 120 | 57.08 Gbit/s | No | DSC | Yes |   |   |
| 144 | 69.30 Gbit/s | No | DSC | Yes |   |   |
| 240 | 121.2 Gbit/s | No | DSC | DSC |   |   |
| 8K | 7680 × 4320 | 30 | 30.60 Gbit/s | No | Yes | Yes |
| 60 | 62.06 Gbit/s | No | DSC | Yes |   |   |
| 120 | 127.8 Gbit/s | No | DSC | DSC |   |   |
| 144 | 155.1 Gbit/s | No | 4:2:2 + DSC | DSC |   |   |
| 240 | 271.4 Gbit/s | No | No | DSC |   |   |
| 10K | 10240 × 4320 | 30 | 40.69 Gbit/s | No | Yes | Yes |
| 60 | 82.53 Gbit/s | No | DSC | Yes |   |   |
| 100 | 140.2 Gbit/s | No | DSC | DSC |   |   |
| 120 | 169.9 Gbit/s | No | 4:2:2 + DSC | DSC |   |   |
| 144 | 206.3 Gbit/s | No | No | DSC |   |   |
| 240 | 360.9 Gbit/s | No | No | 4:2:0 + DSC |   |   |
|   | 2.0a–2.0b | 2.1–2.1b | 2.2 |   |   |   |
| HDMI version |   |   |   |   |   |   |

1. Uncompressed 10 bpc (30 bit/px) color depth with RGB or Y′CBCR 4:4:4 color format and CVT-RB v2 timing are used to calculate these data rates. Uncompressed data rate for RGB images in bits per second is calculated as bits per pixel × pixels per frame × frames per second. Pixels per frame includes blanking intervals as defined by CVT-RB v2.
2. Possible by using Y′CBCR with 4:2:0 subsampling
3. Possible by using Display Stream Compression (DSC)
4. Possible by using Y′CBCR with 4:2:2 subsampling and DSC together, which permits a lower DSC bit rate of 7 bit/px
5. Possible by using Y′CBCR with 4:2:0 subsampling and DSC together, which permits a lower DSC bit rate of 6 bit/px

### Feature support

The features defined in the HDMI specification that an HDMI device may implement are listed below. For historical interest, the version of the HDMI specification in which the feature was first added is also listed. All features of the HDMI specification are optional; HDMI devices may implement any combination of these features.

Although the "HDMI version numbers" are commonly misused as a way of indicating that a device supports certain features, this notation has no official meaning and is considered improper by HDMI Licensing. There is no officially defined correlation between features supported by a device and any claimed "version numbers", as version numbers refer to historical editions of the HDMI specification document, not to particular classes of HDMI devices. Manufacturers are forbidden from describing their devices using HDMI version numbers, and are required to identify support for features by listing explicit support for them, but the HDMI forum has received criticism for lack of enforcement of these policies.

- Full HD Blu-ray Disc and HD DVD video (version 1.0)
- Consumer Electronic Control (CEC) (version 1.0)
- DVD-Audio (version 1.1)
- Super Audio CD (DSD) (version 1.2)
- Auto Lip-Sync Correction (version 1.3)
- Dolby TrueHD / DTS-HD Master Audio bitstream capable (version 1.3)
- Updated list of CEC commands (version 1.3a)
- 3D video (version 1.4)
- Ethernet channel (100 Mbit/s) (version 1.4)
- Audio return channel (ARC) (version 1.4)
- 4 audio streams (version 2.0)
- Dual View (version 2.0)
- Perceptual quantizer HDR EOTF (SMPTE ST 2084) (version 2.0a)
- Hybrid log–gamma (HLG) HDR EOTF (version 2.0a)
- Static HDR metadata (SMPTE ST 2086) (version 2.0a)
- Dynamic HDR metadata (SMPTE ST 2094) (version 2.0b)
- Enhanced audio return channel (eARC) (version 2.1)
- Variable Refresh Rate (VRR) (version 2.1)
- Quick Media Switching (QMS) (version 2.1)
- Quick Frame Transport (QFT) (version 2.1)
- Auto Low Latency Mode (ALLM) (version 2.1)
- Display Stream Compression (DSC) (version 2.1)
- Source-Based Tone Mapping (SBTM) (version 2.1a)

1. Even for a compressed audio codec that a given HDMI device cannot transport, the source device may be able to decode the audio codec and transmit the audio as uncompressed LPCM.
2. CEC has been in the HDMI specification since version 1.0, but only began to see implementation in consumer electronics products in 2008
3. Large number of additions and clarifications for CEC commands. One addition is CEC command, allowing for volume control of an AV receiver.

### Display Stream Compression

*Display Stream Compression* (DSC) is a VESA-developed video compression algorithm designed to enable increased display resolutions and frame rates over existing physical interfaces, and make devices smaller and lighter, with longer battery life.


## Applications

### Blu-ray Disc and HD DVD players

Blu-ray Disc and HD DVD, introduced in 2006, offer high-fidelity audio features that require HDMI for best results. HDMI 1.3 can transport Dolby Digital Plus, Dolby TrueHD, and DTS-HD Master Audio bitstreams in compressed form. This capability allows for an AV receiver with the necessary decoder to decode the compressed audio stream. The Blu-ray specification does not include video encoded with either deep color or xvYCC; thus, HDMI 1.0 can transfer Blu-ray discs at full video quality.

The HDMI 1.4 specification (released in 2009) added support for 3D video and is used by all Blu-ray 3D compatible players.

The Blu-ray Disc Association (BDA) spokespersons have stated (Sept. 2014 at IFA show in Berlin, Germany) that the Blu-ray, Ultra HD players, and 4K discs are expected to be available starting in the second half to 2015. It is anticipated that such Blu-ray UHD players will be required to include a HDMI 2.0 output that supports HDCP 2.2.

Blu-ray permits secondary audio decoding, whereby the disc content can tell the player to mix multiple audio sources together before final output. Some Blu-ray and HD DVD players can decode all of the audio codecs internally and can output LPCM audio over HDMI. Multichannel LPCM can be transported over an HDMI connection, and as long as the AV receiver implements multichannel LPCM audio over HDMI and implements HDCP, the audio reproduction is equal in resolution to HDMI 1.3 bitstream output. Some low-cost AV receivers, such as the Onkyo TX-SR506, do not allow audio processing over HDMI and are labelled as "HDMI pass through" devices. Virtually all modern AV Receivers now offer HDMI 1.4 inputs and outputs with processing for all of the audio formats offered by Blu-ray Discs and other HD video sources. During 2014 several manufacturers introduced premium AV Receivers that include one, or multiple, HDMI 2.0 inputs along with a HDMI 2.0 output(s). However, not until 2015 did most major manufacturers of AV receivers also support HDCP 2.2 as needed to support certain high quality UHD video sources, such as Blu-ray UHD players.

### Digital cameras and camcorders

Most consumer camcorders, as well as many digital cameras, are equipped with a mini-HDMI connector (type C connector).

Some cameras also have 4K capability, although cameras capable of HD video often include an HDMI interface for playback or even live preview, the image processor and the video processor of cameras usable for uncompressed video must be able to deliver the full image resolution at the specified frame rate in real time without any missing frames causing jitter. In addition, to be used as a video source, such as for streaming or switching, the camera must also be capable of removing the UI elements from the image. Therefore, usable uncompressed video out of HDMI without the device's UI elements is often called "clean HDMI".

### Personal computers

Personal computers (PCs) with a DVI interface are capable of video output to an HDMI-enabled monitor. Some PCs include an HDMI interface and may also be capable of HDMI audio output, depending on specific hardware. For example, Intel's motherboard chipsets since the 945G and NVIDIA's GeForce 8200/8300 motherboard chipsets are capable of 8-channel LPCM output over HDMI. Eight-channel LPCM audio output over HDMI with a video card was first seen with the ATI Radeon HD 4850, which was released in June 2008 and is implemented by other video cards in the ATI Radeon HD 4000 series. Linux can drive 8-channel LPCM audio over HDMI if the video card has the necessary hardware and implements the Advanced Linux Sound Architecture (ALSA). The ATI Radeon HD 4000 series implements ALSA. Cyberlink announced in June 2008 that they would update their PowerDVD playback software to allow 192 kHz/24-bit Blu-ray Disc audio decoding in Q3-Q4 of 2008. Corel's WinDVD 9 Plus currently has 96 kHz/24-bit Blu-ray Disc audio decoding.

Even with an HDMI output, a computer may not be able to produce signals that implement HDCP, Microsoft's Protected Video Path, or Microsoft's Protected Audio Path. Several early graphic cards were labelled as "HDCP-enabled" but did not have the hardware needed for HDCP; this included some graphic cards based on the ATI X1600 chipset and certain models of the NVIDIA Geforce 7900 series. The first computer monitors that could process HDCP were released in 2005; by February 2006 a dozen different models had been released. The Protected Video Path was enabled in graphic cards that had HDCP capability, since it was required for output of Blu-ray Disc and HD DVD video. In comparison, the Protected Audio Path was required only if a lossless audio bitstream (such as Dolby TrueHD or DTS-HD MA) was output. Uncompressed LPCM audio, however, does not require a Protected Audio Path, and software programs such as PowerDVD and WinDVD can decode Dolby TrueHD and DTS-HD MA and output it as LPCM. A limitation is that if the computer does not implement a Protected Audio Path, the audio must be downsampled to 16-bit 48 kHz but can still output at up to 8 channels. No graphic cards were released in 2008 that implemented the Protected Audio Path.

The Asus Xonar HDAV1.3 became the first HDMI sound card that implemented the Protected Audio Path and could both bitstream and decode lossless audio (Dolby TrueHD and DTS-HD MA), although bitstreaming is only available if using the ArcSoft TotalMedia Theatre software. It has an HDMI 1.3 input/output, and Asus says that it can work with most video cards on the market.

> Legacy interfaces such as VGA, DVI and LVDS have not kept pace, and newer standards such as DisplayPort and HDMI clearly provide the best connectivity options moving forward. In our opinion, DisplayPort 1.2 is the future interface for PC monitors, along with HDMI 1.4a for TV connectivity.

—

"Leading PC Companies Move to All Digital Display Technology, Phasing Out Analog"

. Intel. December 8, 2010. Archived from

the original

on January 18, 2016

. Retrieved

September 14,

2012

.

In September 2009, AMD announced the ATI Radeon HD 5000 series video cards, which have HDMI 1.3 output (deep color, xvYCC wide gamut capability and high bit rate audio), 8-channel LPCM over HDMI, and an integrated HD audio controller with a Protected Audio Path that allows bitstream output over HDMI for AAC, Dolby AC-3, Dolby TrueHD and DTS-HD Master Audio formats. The ATI Radeon HD 5870 released in September 2009 is the first video card that allows bitstream output over HDMI for Dolby TrueHD and DTS-HD Master Audio. The AMD Radeon HD 6000 series implements HDMI 1.4a. The AMD Radeon HD 7000 series implements HDMI 1.4b.

In December 2010, it was announced that several computer vendors and display makers including Intel, AMD, Dell, Lenovo, Samsung, and LG would stop using LVDS (actually, FPD-Link) from 2013 and legacy DVI and VGA connectors from 2015, replacing them with DisplayPort and HDMI.

On August 27, 2012, Asus announced a new 27 in (69 cm) monitor that produces its native resolution of 2560×1440 via HDMI 1.4.

On September 18, 2014, Nvidia launched GeForce GTX 980 and GTX 970 (with GM204 chip) with HDMI 2.0 support. On January 22, 2015, GeForce GTX 960 (with GM206 chip) launched with HDMI 2.0 support. On March 17, 2015, GeForce GTX TITAN X (GM200) launched with HDMI 2.0 support. On June 1, 2015, GeForce GTX 980 Ti (with GM200 chip) launched with HDMI 2.0 support. On August 20, 2015, GeForce GTX 950 (with GM206 chip) launched with HDMI 2.0 support.

On May 6, 2016, Nvidia launched the GeForce GTX 1080 (GP104 GPU) with HDMI 2.0b support.

On September 1, 2020, Nvidia launched the GeForce RTX 30 series, the world's first discrete graphics cards with support for the full 48 Gbit/s bandwidth with Display Stream Compression 1.2 of HDMI 2.1.

### Gaming consoles

Beginning with the seventh generation of video game consoles, most consoles support HDMI. Video game consoles that support HDMI include the Xbox 360 (except most pre-2007 models) (1.2a), Xbox One (1.4b), Xbox One S (2.0a), Xbox One X (2.0b), PlayStation 3 (1.3a), PlayStation 4 (1.4b), PlayStation 4 Pro (2.0a), Wii U (1.4a), Nintendo Switch (1.4b), Nintendo Switch (OLED model) (2.0a), Xbox Series X and Series S (2.1), PlayStation 5 (2.1), And Nintendo Switch 2 (2.1).

### Tablet computers

Some tablet computers implement HDMI using Micro-HDMI (type D) port, while others like the Eee Pad Transformer implement the standard using mini-HDMI (type C) ports. All iPad models have a special A/V adapter that converts Apple's Lightning connector to a standard HDMI (type A) port. Samsung has a similar proprietary thirty-pin port for their Galaxy Tab 10.1 that could adapt to HDMI as well as USB drives. The Dell Streak 5 smartphone/tablet hybrid is capable of outputting over HDMI. While the Streak uses a PDMI port, a separate cradle adds HDMI compatibility. Some tablets running Android OS provide HDMI output using a mini-HDMI (type C) port. Most new laptops and desktops now have built in HDMI as well.

### Mobile phones

Many mobile phones can produce an output of HDMI video via a micro-HDMI connector, SlimPort, MHL or other adapter.

### Legacy compatibility

HDMI can only be used with older analog-only devices (using connections such as SCART, VGA, RCA, etc.) by means of a digital-to-analog converter or AV receiver, as the interface does not carry any analog signals (unlike DVI, where devices with DVI-I ports accept or provide either digital or analog signals). Cables are available that contain the necessary electronics, but it is important to distinguish these *active* converter cables from *passive* HDMI to VGA cables (which are typically cheaper as they don't include any electronics). The passive cables are *only* useful if a user has a device that is generating or expecting HDMI signals on a VGA connector, or VGA signals on an HDMI connector; this is a non-standard feature, not implemented by most devices.


## HDMI Alternate Mode for USB Type-C

The HDMI Alternate Mode for USB-C allows HDMI-enabled sources with a USB-C connector to directly connect to standard HDMI display devices, without requiring an adapter. The standard was released in September 2016, and supports all HDMI 1.4b features such as video resolutions up to Ultra HD 30 Hz and CEC. Previously, the similar DisplayPort Alternate Mode could be used to connect to HDMI displays from USB Type-C sources, but where in that case active adapters were required to convert from DisplayPort to HDMI, HDMI Alternate Mode connects to the display natively.

The Alternate Mode reconfigures the four SuperSpeed differential pairs present in USB-C to carry the three HDMI TMDS channels and the clock signal. The two Sideband Use pins (SBU1 and SBU2) are used to carry the HDMI Ethernet and Audio Return Channel and the Hot Plug Detect functionality (HEAC+/Utility pin and HEAC−/HPD pin). As there are not enough reconfigurable pins remaining in USB-C to accommodate the DDC clock (SCL), DDC data (SDA), and CEC – these three signals are bridged between the HDMI source and sink via the USB Power Delivery 2.0 (USB-PD) protocol, and are carried over the USB-C Configuration Channel (CC) wire. This is possible because the cable is electronically marked (i.e., it contains a USB PD node) that serves to tunnel the DDC and CEC from the source over the Configuration Channel to the node in the cable, these USB-PD messages are received and relayed to the HDMI sink as regenerated DDC (SCL and SDA signals), or CEC signals.

As stated at CES in January 2023, HDMI Alternate Mode for USB Type-C is no longer being updated as there are no known products using this protocol, reducing its relevance in the current market. This will reduce consumer confusion as DisplayPort Alternate Mode is the primary video protocol of choice over USB-C.


## Relationship with DisplayPort

The DisplayPort audio/video interface was introduced in May 2006 by the Video Electronics Standards Association (VESA). Historically, HDMI Licensing LLC was publicly dismissive of DisplayPort's position in the industry, with its president stating in a 2009 interview that "there are certainly some PCs that have DisplayPort connectors on them, but these are niche applications that have not taken hold in the market."

In recent years, DisplayPort connectors have become a common feature of premium products—displays, desktop computers, and video cards; most of the companies producing DisplayPort equipment are in the computer sector. The DisplayPort website states that DisplayPort is expected to complement HDMI, but as of 2016 100% of HD and UHD TVs had HDMI connectivity. DisplayPort supported some advanced features which are useful for multimedia content creators and gamers (e.g., 5K, Adaptive-Sync), which was the reason most GPUs have DisplayPort. These features were added to the official HDMI specification slightly later, but with the introduction of HDMI 2.1, these gaps are already leveled off (e.g., VRR / Variable Refresh Rate).

DisplayPort uses a self-clocking, micro-packet-based protocol that allows for a variable number of differential pair lanes as well as flexible allocation of bandwidth between audio and video, and allows encapsulating multi-channel compressed audio formats in the audio stream. DisplayPort 1.2 supports multiple audio/video streams, variable refresh rate (FreeSync), and Dual-mode transmitters compatible with HDMI 1.2 or 1.4. Revision 1.3 increases overall transmission bandwidth to 32.4 Gbit/s with the new HBR3 mode featuring 8.1 Gbit/s per lane; it requires Dual-mode with mandatory HDMI 2.0 compatibility and HDCP 2.2. Revision 1.4 added Display Stream Compression (DSC), support for the BT.2020 color space, and HDR10 extensions from CTA-861.3, including static and dynamic metadata. Revision 1.4a was published in April 2018, updating DisplayPort's DSC implementation from 1.2 to 1.2a. Revision 2.0 increased overall bandwidth from 25.92 to 77.37 Gbit/s, enabling increased resolutions and refresh rates, increasing the resolutions and refresh rates with HDR support, and other related improvements. Revision 2.1 was published in October 2022, incorporating the new DP40 and DP80 cable certifications, which require proper operation at the UHBR10 (40 Gbit/s) and UHBR20 (80 Gbit/s) speeds introduced in version 2.0, and a bandwidth management feature to enable DisplayPort tunnelling to coexist with other I/O data traffic more efficiently over a USB4/USB Type-C connection.

The DisplayPort features an adapter detection mechanism enabling dual-mode operation and the transmission of TMDS signals allowing the conversion to DVI and HDMI 1.2/1.4/2.0 signals using a passive adapter. The same external connector is used for both protocols – when a DVI/HDMI passive adapter is attached, the transmitter circuit switches to TMDS mode. DisplayPort Dual-mode ports and cables/adapters are typically marked with the DisplayPort++ logo. Thunderbolt ports with mDP connector also supports Dual-mode passive HDMI adapters/cables. Conversion to dual-link DVI and component video (VGA/YPbPr) requires active powered adapters.

The USB 3.1 type-C connector is increasingly the standard video connector, replacing legacy video connectors such as mDP, Thunderbolt, HDMI, and VGA in mobile devices. USB-C connectors can transmit DisplayPort video to docks and displays using standard USB type-C cables or type-C to DisplayPort cables and adapters; USB-C also supports HDMI adapters that actively convert from DisplayPort to HDMI 1.4 or 2.0. DisplayPort Alternate Mode for USB type-C specification was published in 2015. USB type-C chipsets are not required to include Dual-mode, so passive DP-HDMI adapters do not work with type-C sources. A specification for "HDMI Alternate Mode for USB type-C" was released in 2016, but was discontinued in 2023, with HDMI Licensing Administration stating they knew of no adapter having ever been produced.

DisplayPort is royalty-free, though patent pool administrator Via-LA attempts to collect a $0.20 per-device charge for a bulk license to patents it regards as essential to the DisplayPort specification, while HDMI has an annual fee of US$10,000 and a per unit royalty rate of between $0.04 and $0.15.

HDMI has had a few advantages over DisplayPort, such as ability to carry Consumer Electronics Control (CEC) signals since its first generation (DisplayPort 1.3, introduced in 2014, is the earliest DisplayPort generation which can carry CEC signals).


## Relationship with MHL

Mobile High-Definition Link (MHL) is an adaptation of HDMI intended to connect mobile devices such as smartphones and tablets to high-definition televisions (HDTVs) and displays. Unlike DVI, which is compatible with HDMI using only passive cables and adapters, MHL requires that the HDMI socket be MHL-enabled, otherwise an active adapter (or dongle) is required to convert the signal to HDMI. MHL is developed by a consortium of five consumer electronics manufacturers, several of which are also behind HDMI.

MHL pares down the three TMDS channels in a standard HDMI connection to a single one running over any connector that provides at least five pins. This lets existing connectors in mobile devices – such as micro-USB – be used, avoiding the need for additional dedicated video output sockets. The USB port switches to MHL mode when it detects a compatible device is connected.

In addition to the features in common with HDMI (such as HDCP encrypted uncompressed high-definition video and eight-channel surround sound), MHL also adds the provision of power charging for the mobile device while in use, and also enables the TV remote to control it. Although support for these additional features requires connection to an MHL-enabled HDMI port, power charging can also be provided when using active MHL to HDMI adapters (connected to standard HDMI ports), provided there is a separate power connection to the adapter.

Like HDMI, MHL defines a USB-C Alternate Mode to support the MHL standard over USB-C connections.

Version 1.0 supported 720p/1080i 60 Hz (RGB/4:4:4 pixel encoding) with a bandwidth of 2.25 Gbit/s. Versions 1.3 and 2.0 added support for 1080p 60 Hz (Y′CBCR 4:2:2) with a bandwidth of 3 Gbit/s in PackedPixel mode. Version 3.0 increased the bandwidth to 6 Gbit/s to support Ultra HD (3840 × 2160) 30 Hz video, and also changed from being frame-based, like HDMI, to packet-based.

The fourth version, superMHL, increased bandwidth by operating over multiple TMDS differential pairs (up to a total of six) allowing a maximum of 36 Gbit/s. The six lanes are supported over a reversible 32-pin superMHL connector, while four lanes are supported over USB-C Alternate Mode (only a single lane is supported over micro-USB/HDMI). Display Stream Compression (DSC) is used to allow up to 8K Ultra HD (7680 × 4320) 120 Hz HDR video, and to support Ultra HD 60 Hz video over a single lane.


## HDMI Forum

On October 25, 2011, the HDMI Forum was established by the HDMI founders to create an open, nonprofit industry consortium so that interested companies can participate in the development of the HDMI specification.

All members of the HDMI Forum have equal voting rights, may participate in the Technical Working Group, and if elected can be on the Board of Directors. There is no limit to the number of companies allowed in the HDMI Forum though companies must pay an annual fee of US$15,000 with an additional annual fee of $5,000 for those companies that serve on the Board of Directors. The Board of Directors is made up of 11 companies who are elected every two years by a general vote of HDMI Forum members.

All future developments of the HDMI specification take place in the HDMI Forum and are built upon the HDMI 1.4b specification.

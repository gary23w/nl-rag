---
title: "DCI-P3"
source: https://en.wikipedia.org/wiki/DCI-P3
domain: srgb-colorspace
license: CC-BY-SA-4.0
tags: srgb color space, gamma correction, rec.709, adobe rgb
fetched: 2026-07-02
---

# DCI-P3

**DCI-P3** is an RGB color space defined in 2005 as part of the Digital Cinema Initiative, for use in theatrical digital motion picture distribution (DCDM). **Display P3** is a variant developed by Apple Inc. for wide-gamut displays.

## The standard

In 2005, Digital Cinema Initiatives, LLC in Hollywood, California released the *Digital Cinema System Specification version 1.0*, which defined the colorimetry of what would become known as the DCI-P3 color space.

According to section 8.3.4 in the specification, the blue primary color is the same as Rec. 709, sRGB, and Adobe RGB, with a dominant wavelength of 464.2 nm. The red primary is a deeper red than sRGB and Adobe RGB, as it emits a longer dominant wavelength at 614.9 nm. The red primary is also farther from the white point (being technically an imaginary color, as it is negligibly outside of the spectral locus in the chromaticity diagram), implying that it is more chromatic than the red-orange primary of sRGB.

The most significant difference is the green primary, which is much closer to the spectral locus than either sRGB or Adobe RGB. DCI-P3's green primary has a dominant wavelength of 544.2 nm. Adobe RGB's green primary is more bluish with a dominant wavelength of 534.7 nm. sRGB's green primary is more yellowish at 549.1 nm.

DCI-P3 covers 53.6% of the CIE 1931 chromaticity diagram (see inset image), which describes the color gamut of human color vision.

A smaller, practical gamut for comparison is the Pointer's gamut, which consists of diffusely reflecting surface colors. DCI-P3 covers 86.9% of Pointer's gamut, while in comparison, Rec. 709/sRGB only covers 69.4%.

While DCI-P3 was developed by the Digital Cinema Initiatives (DCI) organization, many of the relevant technical standards are published by the Society of Motion Picture and Television Engineers (SMPTE) such as **SMPTE EG 432-1** and **SMPTE RP 431-2**. On November 10, 2010, SMPTE published SMPTE EG 432-1:2010, which includes a variant of the color space using a D65 white point (about 6503.51 K) instead of the ~6300 K white point of DCI-P3. On April 6, 2011, SMPTE published SMPTE RP 431-2:2011 which defines the reference viewing environment.

Display P3 / P3-D65 (SDR) are supported in CSS Color Level 4 on Safari since 2017 (version 10.1) and Google Chrome since March 2023 (version 111) browsers.

|   | sRGB | Display P3 |
|---|---|---|
| Red |   |   |
| Green |   |   |
| Blue |   |   |

### Display technology

Initially, DCI-P3 was available with theatrical xenon-arc projection systems. This emerging technology presented challenges for filmmakers working with digital media on desktop workstations—that is, how to accurately view the colorspace of the theatrical viewing environment during the production and post-production process.

- In 2008, HP released the first "HP DreamColor" monitor which could display 97% of DCI-P3 color space.
- In 2014, Eizo introduced the first professional 4K monitor with support of the P3 color space.
- In 2015, Apple's iMac desktop became the first consumer computer with a built-in wide-gamut display, supporting the P3 color space. Apple's implementation, known as **Display P3**, uses a D65 white point, and uses the sRGB tone reproduction curve (sometimes referred to as gamma).
- In 2016, the UHD Alliance announced their specifications for Ultra HD Premium which requires devices to display at least 90% of the DCI-P3 color space (in area, not volume).
- Also in 2016, Apple, Samsung, and Microsoft released mobile and desktop devices with P3 support.

## P3 colorimetry

RGB color space parameters

Color space

Transfer Characteristics

White point

CCT

Primary colors

x

y

K

R

x

R

y

G

x

G

y

B

x

B

y

DCI-P3 (theatrical)

γ 2.6

0.314

0.351

6300

0.68

0.32

0.2651

0.69

0.15

0.06

DCI-P3 "D60 sim"

0.32168

0.33767

6000

Display P3 (D65)

sRGB

0.3127

0.3290

6500

P3-D65 (HDR)

HLG

Canon DCI-P3+

User

0.314

0.351

6300

0.74

0.27

0.22

0.7806

0.09

0.01

### DCI-P3 (P3-DCI)

Created by the Digital Cinema Initiative, DCI-P3 is designed for viewing in a fully darkened theater environment. The projection system uses a simple 2.6 gamma curve, the nominal white luminance is 48 cd/m2 (14ftL), and the white point is based on a projector with a xenon bulb, for a correlated color temperature (CCT) of ~6300 K. It is incorrect to refer to this as "D63" as this white point is not a CIE standard illuminant, and is not on the Planckian locus. Instead, the white point is slightly greener. This resulted from optimizing for best light output with the xenon arc lamp projectors commonly used in theaters.

P3-DCI primaries were formally defined in SMPTE RP 431-2.

#### DCI-P3 "D60 sim"

When mastering content utilizing a display or projector in P3 color space, users have the option of using an output transform to DCI-P3 D60-sim which matches the nominal white point of the ACES color spaces.

### P3-D65 (Display P3)

Apple Inc. developed displays using the P3 primaries, creating the corresponding Display P3 color space, also known as P3-D65. While it uses standard P3 RGB primaries, the white point is D65 instead of the DCI ~6300 K white point. The D65 white point is the existing standard for common sRGB and devices (Adobe RGB also uses D65). While the original Display P3 used an sRGB transfer curve (approximately equivalent to a gamma of 2.2), the specification was later updated to also support PQ and HLG transfer functions, but the PQ variant was subsequently deprecated. Display P3's gamut is approximately 50% larger than sRGB in volume and 25% in surface.

Many smartphones, including Apple iPhone (since iPhone 7) and Google Pixel (since Pixel 8), support capturing wide color gamut photos using P3-D65 primaries. Any such photos captured by iPhone and Android camera apps are tagged with the Display P3 ICC profile.

Netflix HDR video production deliverables commonly use P3-D65 primaries in conjunction with the PQ transfer curve.

P3-D65 primaries were formally defined in SMPTE EG 432-1.

### DCI-P3+

Canon created an expanded gamut color space they call **DCI-P3+** using the same ~6300 K white point as DCI-P3. Otherwise, P3+ has no relation to DCI-P3 nor the Digital Cinema Initiative. Unlike the DCI-P3 color space, which defines an actual display technology, Canon's DCI-P3+ color space uses imaginary primaries which cannot be realized by any physical display technology.

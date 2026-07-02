---
title: "Luma (video)"
source: https://en.wikipedia.org/wiki/Luma_(video)
domain: chroma-subsampling
license: CC-BY-SA-4.0
tags: chroma subsampling, ycbcr color, luma chroma, 4:2:0 sampling
fetched: 2026-07-02
---

# Luma (video)

In video, **luma** ( $Y'$ ) represents the brightness in an image (the "black-and-white" or achromatic portion of the image). Luma is typically paired with chroma. Luma represents the achromatic image, while the chroma components represent the color information. Converting R′G′B′ sources (such as the output of a three-CCD camera) into luma and chroma allows for chroma subsampling: because human vision has finer spatial sensitivity to luminance ("black and white") differences than chromatic differences, video systems can store and transmit chromatic information at lower resolution, optimizing perceived detail at a particular bandwidth.

## Luma versus relative luminance

| 255, 147, 255 | 255, 170, 170 | 211, 211, 0 |   |
|---|---|---|---|
| 192, 192, 255 | 200, 200, 200 | 122, 244, 0 |   |
| 0, 235, 235 | 0, 250, 125 | 0, 255, 0 |   |
| RGB values of example colors with the same relative luminance as the lightest primary color (green) using original **NTSC (1953)** primaries for ' (gamma correction) = 2.2 |   |   |   |

| 255, 203, 255 | 255, 208, 208 | 227, 227,0 |   |
|---|---|---|---|
| 216, 216, 255 | 219, 219, 219 | 124, 248, 0 |   |
| 0, 244, 244 | 0, 252, 126 | 0, 255, 0 |   |
| RGB values of example colors with the same relative luminance as the lightest primary color (green) using **BT. 709** primaries for ' (gamma correction) = 2.2 |   |   |   |

Luma is the weighted sum of gamma-compressed R′G′B′ components of a color video—the prime symbols ′ denote gamma compression. The word was proposed to prevent confusion between luma as implemented in video engineering and relative luminance as used in color science (i.e. as defined by CIE). Relative luminance is formed as a weighted sum of *linear* RGB components, not gamma-compressed ones. Even so, luma is sometimes erroneously called luminance. SMPTE EG 28 recommends the symbol $Y'$ to denote luma and the symbol Y to denote relative luminance.

### Use of relative luminance

While luma is more often encountered, relative luminance is sometimes used in video engineering when referring to the brightness of a monitor. The formula used to calculate relative luminance uses coefficients based on the CIE color matching functions and the relevant standard chromaticities of red, green, and blue (e.g., the original NTSC primaries, SMPTE C, or Rec. 709).

For the Rec. 709 (and sRGB) primaries, the linear combination, based on pure colorimetric considerations and the definition of relative luminance is:

$Y=0.2126R+0.7152G+0.0722B$

The formula used to calculate luma in the Rec. 709 spec arbitrarily also uses these same coefficients, but with gamma-compressed components:

$Y'=0.2126R'+0.7152G'+0.0722B',$

where the prime symbol ′ denotes gamma compression.

## Rec. 601 luma versus Rec. 709 luma coefficients

| 158, 0, 79 | 165, 0, 0 | 140, 70, 0 |   |
|---|---|---|---|
| 142, 0, 142 | 95, 95, 95 | 100, 100, 0 |   |
| 104, 0, 208 | 58, 116, 0 |   |   |
| 0, 0, 255 | 0, 119, 0 |   |   |
| 0,91,182 | 0, 112, 112 | 0, 118, 59 |   |
| RGB values of example colors with the same relative luminance as the darkest primary color (blue) using original **NTSC (1953)** primaries for gamma correction equal to 2.2. |   |   |   |

| 152, 0, 76 | 156, 0, 0 | 122, 61, 0 |   |
|---|---|---|---|
| 137, 0, 137 | 77, 77, 77 | 80, 80, 0 |   |
| 102, 0, 204 | 44, 88, 0 |   |   |
| 0, 0, 255 | 0, 90, 0 |   |   |
| 0, 76, 152 | 0, 86, 86 | 0, 90, 45 |   |
| RGB values of example colors with the same relative luminance as the darkest primary color (blue) using **BT. 709** primaries for gamma correction equal to 2.2. |   |   |   |

For digital formats following **CCIR 601** (i.e. most digital standard definition formats), luma is calculated with this formula:

$Y'_{\text{601}}=0.299R'+0.587G'+0.114B'$

Formats following ITU-R Recommendation **BT. 709** (i.e. most digital high definition formats) use a different formula:

$Y'_{\text{709}}=0.2126R'+0.7152G'+0.0722B'$

Modern HDTV systems use the 709 coefficients, while transitional 1035i HDTV (MUSE) formats may use the **SMPTE 240M** coefficients:

$Y'_{\text{240}}=0.212R'+0.701G'+0.087B'=Y'_{\text{145}}$

These coefficients correspond to the SMPTE RP 145 primaries (also known as "SMPTE C") in use at the time the standard was created.

The change in the luma coefficients is to provide the "theoretically correct" coefficients that reflect the corresponding standard chromaticities ('colors') of the primaries red, green, and blue. However, there is some controversy regarding this decision. The difference in luma coefficients requires that component signals must be converted between Rec. 601 and Rec. 709 to provide accurate colors. In consumer equipment, the matrix required to perform this conversion may be omitted (to reduce cost), resulting in inaccurate color.

## Luma and luminance errors

Original image without color subsampling. 200% zoom.

Image after color subsampling - Error in luminance can be seen as a dark band between Green and Magenta.

As well, the Rec. 709 luma coefficients may not necessarily provide better performance. Because of the difference between luma and relative luminance, luma does not exactly represent the luminance in an image. As a result, errors in chroma can affect luminance. Luma alone does not perfectly represent luminance; accurate luminance requires both accurate luma and chroma. Hence, errors in chroma "bleed" into the luminance of an image.

Note the bleeding in lightness near the borders. Due to the widespread usage of chroma subsampling, errors in chroma typically occur when it is lowered in resolution/bandwidth. This lowered bandwidth, coupled with high frequency chroma components, can cause visible errors in luminance. An example of a high frequency chroma component would be the line between the green and magenta bars of the SMPTE color bars test pattern. Error in luminance can be seen as a dark band that occurs in this area.

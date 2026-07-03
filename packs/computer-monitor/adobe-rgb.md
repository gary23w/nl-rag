---
title: "Adobe RGB color space"
source: https://en.wikipedia.org/wiki/Adobe_RGB
domain: computer-monitor
license: CC-BY-SA-4.0
tags: computer monitor
fetched: 2026-07-03
---

# Adobe RGB color space

(Redirected from

Adobe RGB

)

The **Adobe RGB (1998) color space** or **opRGB** is a color space developed by Adobe Inc. in 1998. It was designed to encompass most of the colors achievable on CMYK color printers, but by using RGB primary colors on a device such as a computer display. The Adobe RGB (1998) color space encompasses roughly 30% of the visible colors specified by the CIELAB color space – improving upon the gamut of the sRGB color space, primarily in cyan-green hues. It was subsequently standardized by the IEC as IEC 61966-2-5:1999 with a name opRGB (optional RGB color space) and is used in HDMI.

## Historical background

Beginning in 1997, Adobe Systems was looking into creating ICC profiles that its consumers could use in conjunction with Photoshop's new color management features. Since not many applications at the time had any ICC color management, most operating systems did not ship with useful profiles.

Lead developer of Photoshop, Thomas Knoll decided to build an ICC profile around specifications he found in the documentation for the SMPTE 240M standard, the precursor to Rec. 709 (but not in primaries: 240M also defined EOTF and thus was display referred, sRGB was created by connecting BT.470 PAL and SMPTE C). SMPTE 240M's gamut is wider than that of the BT.709 gamut and the same as SMPTE ST 170 also known as SMPTE C. However, with the release of Photoshop 5.0 nearing, Adobe made the decision to include the profile within the software.

Although users loved the wider range of reproducible colors, those familiar with the SMPTE 240M specifications contacted Adobe, informing the company that it had copied the values that described idealized primaries, not actual standard ones (in a special annex to the standard). The real values were much closer to sRGB's, which avid Photoshop consumers did not enjoy as a working environment. To make matters worse, Thomas Knoll had made an error when copying the red primary chromaticity coordinates, resulting in an even more inaccurate representation of the SMPTE standard. On the other hand red and blue primaries are the same as in PAL and green is the same as in NTSC 1953 (blue is the same as in BT.709 and sRGB).

Adobe tried numerous tactics to correct the profile, such as correcting the red primary and changing the white point to match that of the CIE Standard Illuminant D50 (though that will also change the primaries and is thus pointless), yet all of the adjustments made CMYK conversion worse than before. In the end, Adobe decided to keep the "incorrect" profile, but changed the name to *Adobe RGB (1998)* in order to avoid a trademark search or infringement.

## Specifications

### Reference viewing conditions

| Parameter | Value |
|---|---|
| White Point Luminance Level | 160.00 cd/m2 |
| Black Point Luminance Level | 0.5557 cd/m2 (0.34731% of white point luminance) |
| Contrast Ratio | 287.9 |
| Ambient Illuminance Level | 32 lx |
| Reference Display Surround Level | 32.00 cd/m2 (20% of white point luminance) |
| Viewing Surround | 2 cd/m2 |

In Adobe RGB (1998), colors are specified as [*R*,*G*,*B*] triplets, where each of the *R*, *G*, and *B* components have values ranging between 0 and 1. When displayed on a monitor, the exact chromaticities of the reference white point [1,1,1], the reference black point [0,0,0], and the primaries ([1,0,0], [0,1,0], and [0,0,1]) are specified. To meet the color appearance requirements of the color space, the luminance of the monitor must be 160.00 cd/m2 at the white point, and 0.5557 cd/m2 at the black point, which implies a contrast ratio of 287.9. Moreover, the black point shall have the same chromaticity as the white point, yet with a luminance equal to 0.34731% of the white point luminance. The ambient illumination level at the monitor faceplate when the monitor is turned off must be 32 lx.

As with sRGB, the *RGB* component values in Adobe RGB (1998) are not proportional to the luminances. Rather, a gamma of approximately 2.2 is assumed, without the linear segment near zero that is present in sRGB. The precise gamma value is 563/256, or 2.19921875. In coverage of the CIE 1931 color space the Adobe RGB (1998) color space covers 52.1%.

The chromaticities of the primary colors and the white point, both of which correspond to the CIE Standard Illuminant D65, are as follows:

|   | *x* | *y* |
|---|---|---|
| Red | 0.64 | 0.33 |
| Green | 0.21 | 0.71 |
| Blue | 0.15 | 0.06 |
| White | 0.3127 | 0.3290 |

The corresponding absolute *XYZ* tristimulus values for the reference display white and black points are as follows:

|   | *X* | *Y* | *Z* |
|---|---|---|---|
| White | 152.07 | 160.00 | 174.25 |
| Black | 0.5282 | 0.5557 | 0.6052 |

Normalized *XYZ* tristimulus values can be obtained from absolute luminance *XaYaZa* tristimulus values as follows:

$X={\frac {X_{a}-X_{K}}{X_{W}-X_{K}}}{\frac {X_{W}}{Y_{W}}}$

$Y={\frac {Y_{a}-Y_{K}}{Y_{W}-Y_{K}}}$

$Z={\frac {Z_{a}-Z_{K}}{Z_{W}-Z_{K}}}{\frac {Z_{W}}{Y_{W}}}$

where *XKYKZK* and *XWYWZW* are reference display black and white points in the table above.

The conversion between normalized XYZ to and from Adobe RGB tristimulus values can be done as follows:

${\begin{bmatrix}R\\G\\B\end{bmatrix}}={\begin{bmatrix}2.04159&-0.56501&-0.34473\\-0.96924&1.87597&0.04156\\0.01344&-0.11836&1.01517\end{bmatrix}}{\begin{bmatrix}X\\Y\\Z\end{bmatrix}}$

${\begin{bmatrix}X\\Y\\Z\end{bmatrix}}={\begin{bmatrix}0.57667&0.18556&0.18823\\0.29734&0.62736&0.07529\\0.02703&0.07069&0.99134\end{bmatrix}}{\begin{bmatrix}R\\G\\B\end{bmatrix}}$

As was later defined in the IEC standard opYCC uses BT.601 matrix for conversion to YCbCr, that can be full range matrix and limited range matrix. Display can signal YCC quantization range support and sink can send either one.

### ICC PCS color image encoding

An image in the ICC Profile Connection Space (PCS) is encoded in 24-bit Adobe RGB (1998) color image encoding. Through the application of the 3x3 matrix below (derived from the inversion of the color space chromaticity coordinates and a chromatic adaptation to CIE Standard Illuminant D50 using the Bradford transformation matrix), the input image's normalized *XYZ* tristimulus values are transformed into *RGB* tristimulus values. The component values would be clipped to the range [0, 1].

${\begin{bmatrix}R\\G\\B\end{bmatrix}}={\begin{bmatrix}1.96253&-0.61068&-0.34137\\-0.97876&1.91615&0.03342\\0.02869&-0.14067&1.34926\end{bmatrix}}{\begin{bmatrix}X\\Y\\Z\end{bmatrix}}$

The *RGB* tristimulus values are then converted to Adobe RGB *R'G'B'* component values through the use of the following component transfer functions:

$R'=R^{\frac {256}{563}},$

$G'=G^{\frac {256}{563}},$

$B'=B^{\frac {256}{563}}$

The resulting component values would be then represented in floating point or integer encodings. If it is necessary to encode values from the PCS back to the input device space, the following matrix can be implemented:

${\begin{bmatrix}X\\Y\\Z\end{bmatrix}}={\begin{bmatrix}0.60974&0.20528&0.14919\\0.31111&0.62567&0.06322\\0.01947&0.06087&0.74457\end{bmatrix}}{\begin{bmatrix}R\\G\\B\end{bmatrix}}$

## Comparison to sRGB

### Gamut

sRGB is an RGB color space proposed by HP and Microsoft in 1996 to approximate the color gamut of the (then) most common computer display devices (CRTs). Since sRGB serves as a "best guess" metric for how another person's monitor produces color, it has become the standard color space for displaying images on the Internet. sRGB's color gamut encompasses just 35% of the visible colors specified by CIE, whereas Adobe RGB (1998) encompasses slightly more than 50% of all visible colors. Adobe RGB (1998) extends into richer cyans and greens than does sRGB – for all levels of luminance. The two gamuts are often compared in mid-tone values (~50% luminance), but clear differences are evident in shadows (~25% luminance) and highlights (~75% luminance) as well. In fact, Adobe RGB (1998) expands its advantages to areas of intense orange, yellow, and magenta regions.

Although there is a significant difference between gamut ranges in the CIE *xy* chromaticity diagram, if the coordinates were to be transformed to fit on the CIE *u′v′* chromaticity diagram, which illustrates the eye's perceived variance in hue more closely, the difference in the green region is far less exaggerated. Also, although Adobe RGB (1998) can *theoretically* represent a wider gamut of colors, the color space requires special software and a complex workflow in order to utilize its full range. Otherwise, the produced colors would be squeezed into a smaller range (making them appear duller) in order to match sRGB's more widely used gamut.

### Bit depth distribution

Although the Adobe RGB (1998) working space clearly provides more colors to utilize, another factor to consider when choosing between color spaces is how each space influences the distribution of the image's bit depth. Color spaces with larger gamuts "stretch" the bits over a broader region of colors, whereas smaller gamuts concentrate these bits within a narrow region.

A similar, yet not as dramatic concentration of bit depth occurs with Adobe RGB (1998) versus sRGB, except in three dimensions rather than one. The Adobe RGB (1998) color space occupies roughly 40% more volume than the sRGB color space, which concludes that one would only be exploiting 70% of the available bit depth if the colors in Adobe RGB (1998) are unnecessary. On the contrary, one may have plenty of "spare" bits if using a 16-bit image, thus negating any reduction due to the choice of working space.

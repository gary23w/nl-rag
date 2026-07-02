---
title: "sRGB"
source: https://en.wikipedia.org/wiki/SRGB
domain: srgb-colorspace
license: CC-BY-SA-4.0
tags: srgb color space, gamma correction, rec.709, adobe rgb
fetched: 2026-07-02
---

# sRGB

**sRGB** (standard RGB) is a color space, for use on monitors, printers, and the World Wide Web. It was initially proposed by HP and Microsoft in 1996 and became an official standard of the International Electrotechnical Commission (IEC) as IEC 61966-2-1:1999. It is the current standard colorspace for the web, and it is usually the assumed colorspace for images that do not have an embedded color profile.

The sRGB standard uses the same color primaries and white point as the ITU-R BT.709 standard for HDTV, but a different transfer function (or gamma) compatible with the era's CRT displays, and assumes a viewing environment closer to typical home and office viewing conditions. Matching the behavior of PC video cards and CRT displays greatly aided sRGB's popularity.

## History

By the 1970s, most computers translated 8-bit digital data fairly linearly to a signal that was sent to a video monitor. However video monitors and TVs produced a brightness that was not linear with the input signal, roughly a power law with an exponent between 2 and 3. The exponent was commonly denoted with the letter $\gamma$ , hence the common name "gamma correction" for this function. This design has the benefit of displaying an image with much less visual artifacts, as it places the digital values closer together near black and further apart near white (where changes in brightness are less visible). This gamma varied according to CRT manufacturers, but was normalized in 1993 for use in HDTV systems, as the ITU BT.709 standard. The BT.709 standard specified OETF with a linear section near zero, transitioning to a shifted power law with exponent 1/0.45 ≈ 2.22...

sRGB gamut in

CIE 1931 XYZ

color space

sRGB gamut in the more perceptually uniform

CIELChuv

color space

sRGB was created a few years later by Hewlett-Packard and Microsoft. It was meant to describe the decoding function of most CRT computer monitors used with Windows operating systems at the time, which was still different from that assumed by BT.709. The first draft of the standard was published in 1996. A fourth draft, still incomplete, is available online. Like the BT.709, the sRGB OETF was defined as a linear section near zero that transitions to a shifted power law. The standard does specify EOTF as 2.2 pure gamma with veiling glare term, but glare is a property of the display and should not be added manually to the digital signal.

Actually using the sRGB standard became important as computer graphics software started to calculate in linear light levels in the late 1990s, and needed to use sRGB to convert from and to the common 8-bit image standards.

Images such as shown here became popular for adjusting a CRT monitor to correctly display sRGB.

Amendment 1 to IEC 61966-2-1:1999, approved in 2003, also defines a YCbCr encoding called sYCC and a conversion to more than 8 bits called bg-sRGB. The scRGB standard also tries to extend sRGB to more bits.

## Definition

### Transfer function ("gamma")

An sRGB image file contains R′G′B′ values for each pixel. 0.0 is "black" while 1.0 is the intensity of a color primary needed by "white". These floating-point values are derived from the file data; for a typical 8-bit-per-channel image the bytes are divided by 255.0.

The mapping from these values to intensity is a non-linear transfer function which is the combination of a linear function at low brightness values and a displaced power law for the rest of the range. Linear intensities RGB are derived using (same for all channels):

$R={\begin{cases}R'/12.92,&R'\leq 0.04045\\[5mu]\left({\frac {\displaystyle R'+0.055}{\displaystyle 1.055}}\right)^{2.4},&R'>0.04045\end{cases}}$

This function is quite close to $R'^{2.2}$ . However, for low values near 0.04045 the difference is perceptible; without that linear part, with an 8-bit depth, the darkest ~20 levels would all map to extremely tiny changes in linear light — differences the display couldn't distinguish after rounding. The linear section also compensates for viewing glare term in the EOTF by making small signal darker than it is with a pure 0.45-power function.

The inverse OETF as defined in the IEC standard is not used for EOTF:

$R'={\begin{cases}12.92R,&R\leq 0.0031308\\[5mu](1.055)R^{1/2.4}-0.055,&R>0.0031308\end{cases}}$

If needed by the file format, values greater than 1.0 can be used (the results will also be greater than 1.0), and values less than 0.0 can be converted as -*f*(-*x*).

These functions are similar to those of BT.709, but the values are noticeably different. Because of the rounding of the parameters, they have small discontinuities at the transition between the linear and non-linear part, on the order of 10−8, and they are not precise inverses of each other. These errors are too small to matter in practical situations. In practice many pieces of software use different close-by values (see below), or ignore the linear section, or use a plain gamma 2.2 function. The change in the images is almost imperceptible, however it will make noticeable seams when differently-converted images are overlapped, and mismatched translations back and forth accumulate color shifts. Many operating systems and programs send 8-bit sRGB images directly to video memory and assume this produces the correct levels.

#### Deriving the transfer function

A shifted power law curve that passes through (1,1) is $y=\left({\frac {x+C}{1+C}}\right)^{\gamma }$ .

A straight line that passes through (0,0), is $y=x/A$ . The transition from the linear section to the power law section should be continuous (without a sudden step) and smooth (without a sudden change of slope). To make it continuous when *x*=*X*, we must have

${\frac {X}{A}}=\left({\frac {X+C}{1+C}}\right)^{\gamma }$

To avoid a sudden change of slope where the two segments meet, the derivatives must also be equal at X:

${\frac {1}{A}}=\gamma \left({\frac {X+C}{1+C}}\right)^{\gamma -1}\left({\frac {1}{1+C}}\right)$

Solving the two equations for X and A we get

$X={\frac {C}{\gamma -1}}\;\;\;\;\;A={\frac {(1+C)^{\gamma }(\gamma -1)^{\gamma -1}}{(C^{\gamma -1})(\gamma ^{\gamma })}}$

The first draft of the sRGB standard chose $\gamma =2.4$ and then computed $C=0.055$ so that the value at $x=0.4$ was near $x^{2.2}$ . This produces $X\approx 0.03928$ and $A\approx 12.92321$ . These values, rounded to 5 digits as shown, are still incorrectly given in some publications.

However, the sRGB draft standard rounded A to $12.92$ , resulting in a small discontinuity in the curve.

The first official version of the standard was defined and published by the IEC in 1999. In this version, the rounded value of $A=12.92$ was retained, but the breakpoint X was redefined as $0.04045$ to make the curve approximately continuous. With these values, there is still a discontinuity in the slope, from $1/12.92$ just below the intersection to $1/12.70$ just above it. The final standard also corrected some small rounding errors present in the draft.

### Primaries

|   | Red | Green | Blue | White point |
|---|---|---|---|---|
| *x* | 0.6400 | 0.3000 | 0.1500 | 0.3127 |
| *y* | 0.3300 | 0.6000 | 0.0600 | 0.3290 |
| *Y* | 0.2126 | 0.7152 | 0.0722 | 1.0000 |

The sRGB standard defines the chromaticities of the red, green, and blue primaries, the colors where one of the three channels is nonzero and the other two are zero. The gamut of chromaticities that can be represented in sRGB is the color triangle defined by these primaries, which are set such that the range of colors inside the triangle is well within the range of colors visible to a human with normal trichromatic vision. As with any RGB color space, for non-negative values of R, G, and B it is not possible to represent colors outside this triangle.

The primaries come from HDTV (Rec. 709), which are somewhat different from those for older color TV systems (Rec. 601). These values were chosen to approximate the color of consumer CRT phosphors at that time.

The sRGB standard specifies the colors by providing a matrix that converts the linear values to CIE XYZ perceptual color coordinates with the 2° standard colorimetric observer. This matrix is the same specified by the BT.709 standard and these 4-digit coefficients should be considered exact:

${\begin{bmatrix}X\\Y\\Z\end{bmatrix}}={\begin{bmatrix}0.4124&0.3576&0.1805\\0.2126&0.7152&0.0722\\0.0193&0.1192&0.9505\end{bmatrix}}{\begin{bmatrix}R\\G\\B\end{bmatrix}}$

The inverse conversion, from CIE XYZ to (linear) RGB, is obtained by inverting the matrix above to a suitable numerical accuracy. The 1999 standard provides a matrix which is accurate to 4 decimal digits (enough for 8-bit samples):

${\begin{bmatrix}R\\G\\B\end{bmatrix}}={\begin{bmatrix}+3.2406&-1.5372&-0.4986\\-0.9689&+1.8758&+0.0415\\+0.0557&-0.2040&+1.0570\end{bmatrix}}{\begin{bmatrix}X\\Y\\Z\end{bmatrix}}$

The 1999 IEC standard was amended in 2003 and updated the sample matrix to have seven decimal fraction digits, enough for 16-bit samples:

${\begin{bmatrix}R\\G\\B\end{bmatrix}}={\begin{bmatrix}+3.2406255&-1.5372080&-0.4986286\\-0.9689307&+1.8757561&+0.0415175\\+0.0557101&-0.2040211&+1.0569959\end{bmatrix}}{\begin{bmatrix}X\\Y\\Z\end{bmatrix}}$

For these formulas, the *X*, *Y*, and *Z* values must be scaled so that the *Y* of D65 ("white") is 1.0 (*X* = 0.9505, *Y* = 1.0000, *Z* = 1.0890). This is usually true but some color spaces use 100 or other values (such as in CIELAB, when using specified white points).

### Viewing environment

The sRGB specification assumes a dimly lit encoding (creation) environment with an ambient correlated color temperature (CCT) of 5003 K:

| Parameter | Value |
|---|---|
| Screen luminance level | 80 cd/m2 |
| Illuminant white point | *x* = 0.3127, *y* = 0.3290 (D65) |
| Image surround reflectance | 20% (~medium gray) |
| Encoding ambient illuminance level | 64 lux |
| Encoding ambient white point | *x* = 0.3457, *y* = 0.3585 (D50) |
| Encoding viewing flare | 1.0% |
| Typical ambient illuminance level | 200 lux |
| Typical ambient white point | *x* = 0.3457, *y* = 0.3585 (D50) |
| Typical viewing flare | 5.0% |

The assumed ambient CCT differs from that of the BT.709 standard illuminant (D65), which is still retained for the screen white point. Using D50 for both would have made the white point of most photographic paper appear excessively blue. The other parameters, such as the luminance level, are representative of a typical CRT monitor.

For optimal results, the ICC recommends using the encoding viewing environment (i.e., dim, diffuse lighting) rather than the less-stringent typical viewing environment.

When the sRGB values are sent over to the display, e.g. over HDMI, you don't add any glare offset or compensate it in software, the display and the viewing environment naturally produce this small flare.

### Translation to integers

Most file formats that use sRGB store 8-bit integers. Usually these are converted from 8 bits by dividing by 255.0, and converted to 8 bits by multiplying by 255 and rounding. However some software converts to 8 bits by multiplying by 256 and rounding down. Higher-quality software often uses dithering when writing so that color banding is hidden.

Annex G of the 2003 amendment of the sRGB standard describes an alternative encoding of color values, called **bg-sRGB**, that is recommended when the number of bits per channel is 10 or more. In this case 0.0 is mapped to a *black point* K and 1.0 is mapped to a *white point* W, with all other values interpreted linearly. For 10 bits *K* = 384 and *W* = 894 is specified, and for larger numbers N of bits:

$K=3\times 2^{N-3}\quad \quad W=K+255\times 2^{N-9}$

The 12-bit scRGB format does something similar, with *K* = 1024 and *W* = 2304.

Allowing numbers greater than 1.0 allows high dynamic range images, and negative numbers allows colors outside the gamut triangle.

## Usage

Due to the standardization of sRGB on the Internet, on computers, and on printers, many low- to medium-end consumer digital cameras and scanners use sRGB as the default (or only available) working color space. If the color space of an image is unknown and encoded with 8 bits in each channel, the sRGB encoding can be assumed. Due to programmers misunderstanding the meaning of "gamma" some image files that claim they contain a gamma of 1.0 should also be assumed to be sRGB.

As the sRGB gamut mostly meets or exceeds the gamut of a low-end inkjet printer, an sRGB image is often regarded as satisfactory for home printing. The sRGB color space is sometimes avoided by high-end print publishing professionals because its color gamut is not big enough, especially in the blue-green colors, to include all the colors that can be reproduced in CMYK printing. Images intended for professional printing via a fully color-managed workflow (e.g. prepress output) sometimes use another color space such as Adobe RGB (1998), which accommodates a wider gamut and CMYK color space like Fogra39.

### Programming interface support

The two dominant programming interfaces for 3D graphics, OpenGL and Direct3D, have both incorporated support for the sRGB gamma curve. OpenGL supports textures with sRGB gamma encoded color components (first introduced with EXT_texture_sRGB extension, added to the core in OpenGL 2.1) and rendering into sRGB gamma encoded framebuffers (first introduced with EXT_framebuffer_sRGB extension, added to the core in OpenGL 3.0). Correct mipmapping and interpolation of sRGB gamma textures has direct hardware support in texturing units of most modern GPUs (for example nVidia GeForce 8 performs conversion from 8-bit texture to linear values before interpolating those values), and does not have any performance penalty.

### ICC profiles

A lookup table may be used to efficiently convert sRGB to other color spaces. The International Color Consortium (ICC) has published color profiles for this purpose, which are widely used. There are several variants, including ICCmax, version 4, and version 2.

Version 4 is generally recommended, but version 2 is still commonly used and is the most compatible with other software including browsers. However, inconsistencies have been pointed out between those ICC profiles and the IEC sRGB standard. In particular, version 2 of the ICC profile specification does not implement the piecewise parametric curve encoding ("para") as specified by the IEC sRGB standard, and has to implement the sRGB transfer function using a one-dimensional lookup table. Some implementations approximate the transfer function as 2.2 gamma, with no linear portion, called "simplified sRGB".

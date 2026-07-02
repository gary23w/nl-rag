---
title: "Colorfulness"
source: https://en.wikipedia.org/wiki/Colorfulness
domain: perceptually-uniform-colormaps
license: CC-BY-SA-4.0
tags: viridis colormap, perceptual uniformity, cielab space, rainbow colormap
fetched: 2026-07-02
---

# Colorfulness

Original image, with relatively muted colors

L*C*h (

CIELAB

) chroma increased 50%

HSL

saturation increased 50%; changing HSL saturation also affects the perceived lightness of a color

CIELAB lightness preserved, with

a

* and

b

* stripped, to make a

grayscale

image

**Colorfulness**, **chroma** and **saturation** are attributes of perceived color relating to chromatic intensity. As defined formally by the International Commission on Illumination (CIE) they respectively describe three different aspects of chromatic intensity, but the terms are often used loosely and interchangeably in contexts where these aspects are not clearly distinguished. The precise meanings of the terms vary by what other functions they are dependent on.

- **Colorfulness** is the "attribute of a visual perception according to which the perceived color of an area appears to be more or less chromatic (Any color that is absent of white, grey, or black)". The colorfulness evoked by an object depends not only on its spectral reflectance but also on the strength of the illumination, and increases with the latter unless the brightness is very high (Hunt effect).
- **Chroma** is the "colorfulness of an area judged as a proportion of the brightness of a similarly illuminated area that appears white or highly transmitting". As a result, chroma is mostly only dependent on the spectral properties, and as such is seen to describe the **object color**. It is how different from a grey *of the same lightness* such an object color appears to be.
- **Saturation** is the "colorfulness of an area judged in proportion to its brightness", which in effect is the perceived freedom from whitishness of the light coming from the area. An object with a given spectral reflectance exhibits approximately constant saturation for all levels of illumination, unless the brightness is very high.

As colorfulness, chroma, and saturation are defined as attributes of perception, they can not be physically measured as such, but they can be quantified in relation to psychometric scales intended to be perceptually even—for example, the chroma scales of the Munsell system. While the chroma and lightness of an object are its colorfulness and brightness judged in proportion to the same thing ("the brightness of a similarly illuminated area that appears white or highly transmitting"), the saturation of the light coming from that object is in effect the chroma of the object judged in proportion to its lightness. On a Munsell hue page, lines of uniform saturation thus tend to radiate from near the black point, while lines of uniform chroma are vertical.

## Chroma

The naïve definition of saturation does not specify its response function. In the CIE XYZ and RGB color spaces, the saturation is defined in terms of additive color mixing, and has the property of being proportional to any scaling centered at white or the white point illuminant. However, both color spaces are non-linear in terms of psychovisually perceived color differences. It is also possible — and sometimes desirable — to define a saturation-like quantity that is linearized in term of the psychovisual perception.

In the CIE 1976 LAB and LUV color spaces, the unnormalized **chroma** is the radial component of the cylindrical coordinate CIE LCh (lightness, chroma, hue) representation of the LAB and LUV color spaces, also denoted as CIE LCh(ab) or CIE LCh for short, and CIE LCh(uv). The transformation of $(a,b)$ to $\left(C_{ab},h_{ab}\right)$ is given by: $C_{ab}^{*}={\sqrt {a^{*2}+b^{*2}}}$ $h_{ab}=\operatorname {atan2} \left({b^{\star }},{a^{\star }}\right)$ and analogously for CIE LCh(uv).

The chroma in the CIE LCh(ab) and CIE LCh(uv) coordinates has the advantage of being more psychovisually linear, yet they are non-linear in terms of linear component color mixing. And therefore, chroma in CIE 1976 Lab and LUV color spaces is very much different from the traditional sense of "saturation".

### In color appearance models

Another, psychovisually even more accurate, but also more complex method to obtain or specify the saturation is to use a color appearance model like CIECAM02. Here, the **chroma** color appearance parameter might (depending on the color appearance model) be intertwined with e.g. the physical brightness of the illumination or the characteristics of the emitting/reflecting surface, which is more sensible psychovisually.

The CIECAM02 chroma $C,$ for example, is computed from a lightness J in addition to a naively evaluated color magnitude $t.$ In addition, a colorfulness M parameter exists alongside the chroma $C.$ It is defined as $M=CF_{B}^{0.25},$ where $F_{L}$ is dependent on the viewing condition.

## Saturation

The saturation of a color is determined by a combination of light intensity and how much it is distributed across the spectrum of different wavelengths. The purest (most saturated) color is achieved by using just one wavelength at a high intensity, such as in laser light. If the intensity drops, then as a result the saturation drops. To desaturate a color of given intensity in a subtractive system (such as watercolor), one can add white, black, gray, or the hue's complement.

Various correlates of saturation follow.

### CIELUV and CIELAB

In CIELUV, saturation is equal to the *chroma* normalized by the *lightness*: $s_{uv}={\frac {C_{uv}^{*}}{L^{*}}}=13{\sqrt {(u'-u'_{n})^{2}+(v'-v'_{n})^{2}}}$ where $\left(u_{n},v_{n}\right)$ is the chromaticity of the white point, and chroma is defined below.

By analogy, in CIELAB this would yield: $s_{ab}={\frac {C_{ab}^{*}}{L^{*}}}={\frac {\sqrt {{a^{*}}^{2}+{b^{*}}^{2}}}{L^{*}}}$

The CIE has not formally recommended this equation since CIELAB has no chromaticity diagram, and this definition therefore lacks direct connection with older concepts of saturation. Nevertheless, this equation provides a reasonable predictor of saturation, and demonstrates that adjusting the lightness in CIELAB while holding (*a**, *b**) fixed does affect the saturation.

But the following verbal definition of Manfred Richter and the corresponding formula proposed by Eva Lübbe are in agreement with the human perception of saturation: Saturation is the proportion of pure chromatic color in the total color sensation. $S_{ab}={\frac {C_{ab}^{*}}{\sqrt {{C_{ab}^{*}}^{2}+{L^{*}}^{2}}}}100\%$ where $S_{ab}$ is the saturation, $L^{*}$ the lightness and $C_{ab}^{*}$ is the chroma of the color.

### CIECAM02

In CIECAM02, saturation equals the square root of the *colorfulness* divided by the *brightness*: $s={\sqrt {\frac {M}{Q}}}$

This definition is inspired by experimental work done with the intention of remedying CIECAM97s's poor performance. M is proportional to the chroma $C,$ thus the CIECAM02 definition bears some similarity to the CIELUV definition.

### HSL and HSV

Saturation is also one of three coordinates in the HSL and HSV color spaces. However, in the HSL color space saturation exists independently of lightness. That is, both a very light color *and* a very dark color can be heavily saturated in HSL; whereas in the previous definitions—as well as in the HSV color space—colors approaching white all feature low saturation.

## Excitation purity

The **excitation purity** (purity for short) of a stimulus is the difference from the illuminant's white point to the furthest point on the chromaticity diagram with the same dominant wavelength; using the CIE 1931 color space: $p_{e}={\sqrt {\frac {\left(x-x_{n}\right)^{2}+\left(y-y_{n}\right)^{2}}{\left(x_{I}-x_{n}\right)^{2}+\left(y_{I}-y_{n}\right)^{2}}}}$ where $\left(x_{n},y_{n}\right)$ is the chromaticity of the white point and $\left(x_{I},y_{I}\right)$ is the point on the perimeter whose line segment to the white point contains the chromaticity of the stimulus. Different color spaces, such as CIELAB or CIELUV may be used, and will yield different results.

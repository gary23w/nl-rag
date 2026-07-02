---
title: "Color model"
source: https://en.wikipedia.org/wiki/Color_model
domain: color-management
license: CC-BY-SA-4.0
tags: color management, icc profile, color gamut, cie color space
fetched: 2026-07-02
---

# Color model

In color science, a **color model** is an abstract mathematical model describing the way colors can be represented as tuples of numbers, typically as three or four values or color components. It differs from a color space in that a color model is not absolute, that is, there is no way to map a color within a color model to a point in a color space.

This article describes ways in which human color vision can be modeled, and discusses some of the models in common use.

## Fundamental modeling of human color vision: Tristimulus color space

One can picture this space as a region in three-dimensional Euclidean space if one identifies the *x*, *y*, and *z* axes with the stimuli for the long-wavelength (*L*), medium-wavelength (*M*), and short-wavelength (*S*) light receptors. This is called the LMS color space. The origin, (*S*,*M*,*L*) = (0,0,0), corresponds to black. White has no definite position in this diagram; rather it is defined according to the color temperature or white balance as desired or as available from ambient lighting. The most saturated colors are located at the outer rim of the region, with brighter colors farther removed from the origin. Colors like brown or grey are perceived when, respectively, orange light and white light are received, but at a lower intensity than what it would be expected for the colors orange and white given the surrounding illumination. One can observe this phenomenon by watching the screen of an overhead projector during a meeting: one sees black lettering on a white background, even though the "black" has in fact not become darker than the white screen on which it is projected before the projector was turned on. The "black" areas have not actually become darker but appear "black" relative to the higher intensity "white" projected onto the screen around it. See also color constancy.

The human tristimulus space has the property that additive mixing of colors corresponds to the adding of vectors in this space. This makes it easy to, for example, describe the possible colors (gamut) that can be constructed from the red, green, and blue primaries in a computer display.

## Additive and subtractive color models

### RYB color model

**RYB** is a subtractive color model used in art and applied design in which red, yellow, and blue pigments are considered primary colors. The RYB color model relates specifically to color in the form of paint and pigment application in art and design. Other common color models include the light model (RGB) and the paint, pigment and ink CMY color model, which is much more accurate in terms of color gamut and intensity compared to the traditional RYB color model, the latter emerging in conjunction with the CMYK color model in the printing industry. This model was used for printing by Jacob Christoph Le Blon in 1725 and called it *Coloritto* or *harmony of colouring*, stating that the primitive (primary) colors are yellow, red and blue, while the secondary are orange, green and purple or violet.

### RGB color model

Media that transmit light (such as television) use additive color mixing with primary colors of red, green, and blue, each of which stimulates one of the three types of the eye's color receptors with as little stimulation as possible of the other two. This is called "RGB" color space. Mixtures of light of these primary colors cover a large part of the human color space and thus produce a large part of human color experiences. This is why color television sets or color computer monitors need only produce mixtures of red, green and blue light. See Additive color.

Other primary colors could in principle be used, but with red, green and blue the largest portion of the human color space can be captured. Unfortunately there is no exact consensus as to what loci in the chromaticity diagram the red, green, and blue colors should have, so the same RGB values can give rise to slightly different colors on different screens.

RGB is a *device-dependent* color model: different devices detect or reproduce a given RGB value differently, since the color elements (such as phosphors or dyes) and their response to the individual red, green, and blue levels vary from manufacturer to manufacturer, or even in the same device over time. Thus an RGB value does not define the same *color* across devices without some kind of color management.

### CMY and CMYK color models

It is possible to achieve a large range of colors seen by humans by combining cyan, magenta, and yellow transparent dyes/inks on a white substrate. These are the *subtractive* primary colors. Often a fourth ink, black, is added to improve reproduction of some dark colors. This is called the "CMY" or "CMYK" color space.

The cyan ink absorbs red light but transmits green and blue, the magenta ink absorbs green light but transmits red and blue, and the yellow ink absorbs blue light but transmits red and green. The white substrate reflects the transmitted light back to the viewer. Because in practice the CMY inks suitable for printing also reflect a little bit of color, making a deep and neutral black impossible, the K (black ink) component, usually printed last, is needed to compensate for their deficiencies. Use of a separate black ink is also economically driven when a lot of black content is expected, e.g. in text media, to reduce simultaneous use of the three colored inks. The dyes used in traditional color photographic prints and slides are much more perfectly transparent, so a K component is normally not needed or used in those media.

## Cylindrical-coordinate color models

A number of color models exist in which colors are fit into conic, cylindrical or spherical shapes, with neutrals running from black to white along a central axis, and hues corresponding to angles around the perimeter. Arrangements of this type date back to the 18th century, and continue to be developed in the most modern and scientific models.

### Background

Philipp Otto Runge

’s

Farbenkugel

(color sphere), 1810, showing the outer surface of the sphere (top two images), and horizontal and vertical cross sections (bottom two images)

Color sphere of

Johannes Itten

, 1919-20

Different color theorists have each designed unique color solids. Many are in the shape of a sphere, whereas others are warped three-dimensional ellipsoid figures—these variations being designed to express some aspect of the relationship of the colors more clearly. The color spheres conceived by Phillip Otto Runge and Johannes Itten are typical examples and prototypes for many other color solid schematics. The models of Runge and Itten are basically identical, and form the basis for the description below.

Pure, saturated hues of equal brightness are located around the equator at the periphery of the color sphere. As in the color wheel, contrasting (or complementary) hues are located opposite each other. Moving toward the center of the color sphere on the equatorial plane, colors become less and less saturated, until all colors meet at the central axis as a neutral gray. Moving vertically in the color sphere, colors become lighter (toward the top) and darker (toward the bottom). At the upper pole, all hues meet in white; at the bottom pole, all hues meet in black.

The vertical axis of the color sphere, then, is gray all along its length, varying from black at the bottom to white at the top. All pure (saturated) hues are located on the surface of the sphere, varying from light to dark down the color sphere. All impure (unsaturated hues, created by mixing contrasting colors) comprise the sphere's interior, likewise varying in brightness from top to bottom.

### HSL and HSV

Painters long mixed colors by combining relatively bright pigments with black and white. Mixtures with white are called

tints

, mixtures with black are called

shades

, and mixtures with both are called

tones

. See

Tints and shades

.

The RGB gamut can be arranged in a cube. The RGB model is not very intuitive to artists used to using traditional models based on tints, shades and tones. The HSL and HSV color models were designed to fix this.

HSL cylinder

HSV cylinder

HSL and HSV are both cylindrical geometries, with hue, their angular dimension, starting at the red primary at 0°, passing through the green primary at 120° and the blue primary at 240°, and then wrapping back to red at 360°. In each geometry, the central vertical axis comprises the *neutral*, *achromatic*, or *gray* colors, ranging from black at lightness 0 or value 0, the bottom, to white at lightness 1 or value 1, the top.

Most televisions, computer displays, and projectors produce colors by combining red, green, and blue light in varying intensities—the RGB additive primary colors. However, the relationship between the constituent amounts of red, green, and blue light and the resulting color is unintuitive, especially for inexperienced users, and for users familiar with subtractive color mixing of paints or traditional artists’ models based on tints and shades.

In an attempt to accommodate more traditional and intuitive color mixing models, computer graphics pioneers at PARC and NYIT developed the HSV model in the mid-1970s, formally described by Alvy Ray Smith in the August 1978 issue of *Computer Graphics*. In the same issue, Joblove and Greenberg described the HSL model—whose dimensions they labeled *hue*, *relative chroma*, and *intensity*—and compared it to HSV. Their model was based more upon how colors are organized and conceptualized in human vision in terms of other color-making attributes, such as hue, lightness, and chroma; as well as upon traditional color mixing methods—e.g., in painting—that involve mixing brightly colored pigments with black or white to achieve lighter, darker, or less colorful colors.

The following year, 1979, at SIGGRAPH, Tektronix introduced graphics terminals using HSL for color designation, and the Computer Graphics Standards Committee recommended it in their annual status report. These models were useful not only because they were more intuitive than raw RGB values, but also because the conversions to and from RGB were extremely fast to compute: they could run in real time on the hardware of the 1970s. Consequently, these models and similar ones have become ubiquitous throughout image editing and graphics software since then.

### Munsell color system

Munsell’s color sphere, 1900. Later, Munsell discovered that if hue, value, and chroma were to be kept perceptually uniform, achievable surface colors could not be forced into a regular shape.

Three-dimensional representation of the 1943 Munsell renotations. Notice the irregularity of the shape when compared to Munsell's earlier color sphere, at left.

Another influential older cylindrical color model is the early-20th-century Munsell color system. Albert Munsell began with a spherical arrangement in his 1905 book *A Color Notation*, but he wished to properly separate color-making attributes into separate dimensions, which he called *hue*, *value*, and *chroma*, and after taking careful measurements of perceptual responses, he realized that no symmetrical shape would do, so he reorganized his system into a lumpy blob.

Munsell's system became extremely popular, the de facto reference for American color standards—used not only for specifying the color of paints and crayons, but also, e.g., electrical wire, beer, and soil color—because it was organized based on perceptual measurements, specified colors via an easily learned and systematic triple of numbers, because the color chips sold in the *Munsell Book of Color* covered a wide gamut and remained stable over time (rather than fading), and because it was effectively marketed by Munsell's Company. In the 1940s, the Optical Society of America made extensive measurements, and adjusted the arrangement of Munsell colors, issuing a set of "renotations". The trouble with the Munsell system for computer graphics applications is that its colors are not specified via any set of simple equations, but only via its foundational measurements: effectively a lookup table. Converting from RGB ↔ Munsell requires interpolating between that table's entries, and is extremely computationally expensive in comparison with converting from RGB ↔ HSL or RGB ↔ HSV which only requires a few simple arithmetic operations.

### Natural Color System

A three-dimensional drawing of the

Ostwald color system

. First described in

Wilhelm Ostwald

(1916).

Animation showing the NCS 1950 standard color samples in the NCS color circle and hue triangles

The Swedish Natural Color System (NCS), widely used in Europe, takes a similar approach to the Ostwald bicone at right. Because it attempts to fit color into a familiarly shaped solid based on "phenomenological" instead of photometric or psychological characteristics, it suffers from some of the same disadvantages as HSL and HSV: in particular, its lightness dimension differs from perceived lightness, because it forces colorful yellow, red, green, and blue into a plane.

### Preucil hue circle

In densitometry, a model quite similar to the hue defined above is used for describing colors of CMYK process inks. In 1953, Frank Preucil developed two geometric arrangements of hue, the "Preucil hue circle" and the "Preucil hue hexagon", analogous to our *H* and *H*2, respectively, but defined relative to idealized cyan, yellow, and magenta ink colors. The "Preucil *hue error*" of an ink indicates the difference in the "hue circle" between its color and the hue of the corresponding idealized ink color. The *grayness* of an ink is *m*/*M*, where *m* and *M* are the minimum and maximum among the amounts of idealized cyan, magenta, and yellow in a density measurement.

### CIECAM02

The CIE's most recent model, CIECAM02 (CAM stands for "color appearance model"), is more theoretically sophisticated and computationally complex than earlier models. Its aims are to fix several of the problems with models such as CIELAB and CIELUV, and to explain not only responses in carefully controlled experimental environments, but also to model the color appearance of real-world scenes. Its dimensions *J* (lightness), *C* (chroma), and *h* (hue) define a polar-coordinate geometry.

## Color systems

There are various types of color systems that classify color and analyze their effects. The American Munsell color system devised by Albert H. Munsell is a famous classification that organizes various colors into a color solid based on hue, saturation and value. Other important color systems include the Swedish Natural Color System (NCS), the Optical Society of America's Uniform Color Space (OSA-UCS), and the Hungarian Coloroid system developed by Antal Nemcsics from the Budapest University of Technology and Economics. Of those, the NCS is based on the opponent-process color model, while the Munsell, the OSA-UCS and the Coloroid attempt to model color uniformity. The American Pantone and the German RAL commercial color-matching systems differ from the previous ones in that their color spaces are not based on an underlying color model. The Icelandic Spot Matching System (SMS) is a so-called media neutral color palette where all the colors can be reproduced online, on Television and in standard process printing (CMYK or better).

## Other uses of "color model"

### Models of mechanism of color vision

We also use "color model" to indicate a model or mechanism of color vision for explaining how color signals are processed from visual cones to ganglion cells. For simplicity, we call these models color mechanism models. The classical color mechanism models are Young–Helmholtz's trichromatic model and Hering's opponent-process model. Though these two theories were initially thought to be at odds, it later came to be hypothesized that the mechanisms responsible for color opponency receive signals from the three types of cones and process them at a more complex level. A widely accepted model is called the zone model. A symmetrical zone model compatible with the trichromatic theory, the opponent theory, and Smith's color transform model is called the decoding model

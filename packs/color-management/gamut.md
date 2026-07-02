---
title: "Gamut"
source: https://en.wikipedia.org/wiki/Gamut
domain: color-management
license: CC-BY-SA-4.0
tags: color management, icc profile, color gamut, cie color space
fetched: 2026-07-02
---

# Gamut

In color reproduction and colorimetry, a **gamut**, or **color gamut** /ˈɡæmət/, is a convex set containing the colors that can be accurately represented, i.e. reproduced by an output device (e.g. printer or display) or measured by an input device (e.g. camera or visual system). Devices with a larger gamut can represent more colors. Similarly, gamut may also refer to the colors within a defined color space, which is not linked to a specific device. A trichromatic gamut is often visualized as a color triangle. A less common usage defines gamut as the subset of colors contained within an image, scene or video.

## Introduction

The term *gamut* was adopted from the field of music, where the medieval Latin expression "gamma ut" meant the lowest tone of the G scale and, in time, came to imply the entire range of musical notes of which musical melodies are composed. Shakespeare's use of the term in *The Taming of the Shrew* is sometimes attributed to the author / musician Thomas Morley. In the 1850s, the term was applied to a range of colors or hue, for example by Thomas de Quincey, who wrote "Porphyry, I have heard, runs through as large a gamut of hues as marble."

The gamut of a device or process is that portion of the color space that can be represented, or reproduced. Generally, the color gamut is specified in the hue–saturation plane, as a system can usually produce colors over a wide intensity range within its color gamut. Device gamuts must use real primaries (those that can be represented by a physical spectral power distribution) and therefore are always *incomplete* (smaller than the human visible gamut). No gamut defined by a finite number of primaries can represent the entire human visible gamut. Three primaries are necessary for representing an approximation of the human visible gamut. More primaries can be used to increase the size of the gamut. For example, while painting with red, yellow and blue pigments is sufficient for modeling color vision, adding further pigments (e.g. orange or green) can increase the size of the gamut, allowing the reproduction of more saturated colors.

While processing a digital image, the most convenient color model used is the RGB model. Printing the image requires transforming the image from the original RGB color model to the printer's CMYK color model. During this process, the colors from the RGB model which are out of gamut must be somehow converted to approximate values within the CMYK model. Simply trimming only the colors which are out of gamut to the closest colors in the destination space would burn the image. There are several algorithms approximating this transformation, but none of them can be truly perfect, since those colors are simply out of the target device's capabilities. This is why identifying the colors in an image that are out of gamut in the target color space as soon as possible during processing is critical for the quality of the final product. It is also important to remember that there are colors inside the CMYK gamut that are outside the most commonly used RGB color spaces, such as sRGB and Adobe RGB.

### Color management

Color management is the process of ensuring consistent and accurate colors across devices with different gamuts. Color management handles the transformations between color gamuts and canonical color spaces to ensure that colors are represented equally on different devices. A device's gamut is defined by a color profile, usually the ICC profile, which relates the gamut to a standardized color space and allows for calibration of the device. Transforming from one gamut to a smaller gamut loses information as *out-of-gamut* colors are projected on to the smaller gamut and transforming back to the larger gamut does not regain this lost information.

## Colorimetry

Colorimetry is the measurement of color, generally in a way that mimics human color perception. Input devices such as digital cameras or scanners are made to mimic trichromatic human color perception and are based on three sensors elements with different spectral sensitivities, ideally aligned approximately with the spectral sensitivities of human photopsins. In this sense, they have a similar gamut to the human visual system. However, most of these devices violate the Luther condition and are not intended to be truly colorimetric, with the exception of tristimulus colorimeters. Higher-dimension input devices, such as multispectral imagers, hyperspectral imagers or spectrometers, capture color at a much larger gamut, dimensionally, than the human visible gamut. To be perceived by humans, the images must first be down-dimensionalized and treated with false color.

### Visible gamut

The extent of color that can be detected by the average human, approximated by the standard observer, is the *visible (or visual) gamut*. The chromaticities present in the visible gamut are usually visualized in the CIE 1931 chromaticity diagram, where the spectral locus (curved edge) represents the monochromatic (single-wavelength) or spectral colors. As current displays have a smaller gamut than the visible gamut, the colors that are out-of-gamut are reproduced as colors inside the display's gamut. Device gamuts are generally depicted in reference to the visible gamut. The standard observer represents a typical human, but colorblindness leads to a reduced visible gamut.

## Color reproduction

### Visualization of gamuts

|   | Gamuts are commonly represented as areas within the CIE 1931 chromaticity diagram. This ignores the intensity/brightness dimension of the gamut, which is not depicted. Gamuts defined by three primaries are visualized as color triangles. |
|---|---|
| The sRGB gamut projected into the CIE xyY color space. *x* and *y* are the horizontal axes and represent chromaticity. *Y* is the vertical axis and represents (linear) luminance. | Gamuts may also be represented in 3D space as a color solid, which includes a visualization of the dimension of lightness, or alternatively in some color spaces, brightness. |
| sRGB gamut in CIE 1931 XYZ color spaceOptimal color solid in CIE 1931 XYZ color space, with D65 white point | The pictures show the gamuts of the sRGB color space (left), which is approximately the one that most computer monitors and TVs have; and the theoretical gamut of surfaces (optimal color solid, or Rösch-MacAdam color solid) (under D65 illumination) (right). The left diagram shows that the shape of the RGB gamut is a triangle between red, green, and blue at lower luminosities; a triangle between cyan, magenta, and yellow at higher luminosities, and a single white point at maximum luminosity. The exact positions of the apexes depends on the emission spectra of the phosphors in the display, and on the ratio between the maximum luminosities of the three phosphors (i.e., the color balance or white point). |

### Limitations of color representation

#### Surfaces

##### Optimal colors

Optimal colors are the most chromatic colors that surfaces can have*. The color solid bounded by the set of all optimal colors is called the optimal color solid or Rösch–MacAdam color solid. For now, we are unable to produce objects with such colors, at least not without recurring to more complex physical phenomena.

**(with classical reflection. Phenomena like fluorescence or structural coloration may cause the color of objects to lie outside the optimal color solid)*

The reflectance spectrum of a color is the amount of light of each wavelength that it reflects, in proportion to a given maximum, which has the value of 1 (100%). If the reflectance spectrum of a color is 0 (0%) or 1 (100%) across the entire visible spectrum, and it has no more than two transitions between 0 and 1, or 1 and 0, then it is an optimal color. With the current state of technology, we are unable to produce any material or pigment with these properties.

Thus four types of "optimal color" spectra are possible:

- The transition goes from zero at both ends of the spectrum to one in the middle, as shown in the image at right.
- It goes from one at the ends to zero in the middle.
- It goes from 1 at the start of the visible spectrum to 0 in some point in the middle until its end.
- It goes from 0 at the start of the visible spectrum to 1 at some point in the middle until its end.

The first type produces colors that are similar to the spectral colors and follow roughly the horseshoe-shaped portion of the CIE xy chromaticity diagram (the spectral locus), but are, in surfaces, more chromatic, although less spectrally pure. The second type produces colors that are similar to (but, in surfaces, more chromatic and less spectrally pure than) the colors on the straight line in the CIE xy chromaticity diagram (the line of purples), leading to magenta or purple-like colors.

In optimal color solids, the colors of the visible spectrum are theoretically black, because their reflectance spectrum is 1 (100%) in only one wavelength, and 0 in all of the other infinite visible wavelengths that there are, meaning that they have a lightness of 0 with respect to white, and will also have 0 chroma, but, of course, 100% of spectral purity. In short: In optimal color solids, spectral colors are equivalent to black (0 lightness, 0 chroma), but have full spectral purity (they are located in the horseshoe-shaped spectral locus of the chromaticiy diagram).

In linear color spaces, such as LMS or CIE 1931 XYZ, the set of rays that start at the origin (black, (0, 0, 0)) and pass through all the points that represent the colors of the visible spectrum, and the portion of a plane that passes through the violet half-line and the red half-line (both ends of the visible spectrum), generate the "spectrum cone". The black point (coordinates (0, 0, 0)) of the optimal color solid (and only the black point) is tangent to the "spectrum cone", and the white point ((1, 1, 1)) (only the white point) is tangent to the "inverted spectrum cone", with the "inverted spectrum cone" being symmetrical to the "spectrum cone" with respect to the middle gray point ((0.5, 0.5, 0.5)). This means that, in linear color spaces, the optimal color solid is centrally symmetric.

In most color spaces, the surface of the optimal color solid is smooth, except for two points (black and white); and two sharp edges: the "warm" edge, which goes from black, to red, to orange, to yellow, to white; and the "cool" edge, which goes from black, to deep violet, to blue, to cyan, to white. This is due to the following: If the portion of the reflectance spectrum of a color is spectral red (which is located at one end of the spectrum), it will be seen as black. If the size of the portion of total or reflectance is increased, now covering from the red end of the spectrum to the yellow wavelengths, it will be seen as red. If the portion is expanded even more, covering the green wavelengths, it will be seen as orange or yellow. If it is expanded even more, it will cover more wavelengths than the yellow semichrome does, approaching white, until it is reached when the full spectrum is reflected. The described process is called "cumulation". Cumulation can be started at either end of the visible spectrum (we just described cumulation starting from the red end of the spectrum, generating the "warm" sharp edge), cumulation starting at the violet end of the spectrum will generate the "cool" sharp edge.

##### Maximum chroma colors, semichromes, or full colors

Each hue has a maximum chroma point, semichrome, or full color; objects cannot have a color of that hue with a higher chroma. They are the most chromatic, vibrant colors that objects can have. They were called **semichromes** or **full colors** by the German chemist and philosopher Wilhelm Ostwald in the early 20th century.

If B is the complementary wavelength of wavelength A, then the straight line that connects A and B passes through the achromatic axis in a linear color space, such as LMS or CIE 1931 XYZ. If the reflectance spectrum of a color is 1 (100%) for all the wavelengths between A and B, and 0 for all the wavelengths of the other half of the color space, then that color is a maximum chroma color, semichrome, or full color (this is the explanation to why they were called **semi**chromes). Thus, maximum chroma colors are a type of optimal color.

As explained, full colors are far from being monochromatic. If the spectral purity of a maximum chroma color is increased, its chroma decreases, because it will approach the visible spectrum, ergo, it will approach black.

In perceptually uniform color spaces, the lightness of the full colors varies from around 30% in the violetish blue hues, to around 90% in the yellowish hues. The chroma of each maximum chroma point also varies depending on the hue; in optimal color solids plotted in perceptually uniform color spaces, semichromes like red, green, blue, violet, and magenta have a high chroma, while semichromes like yellow, orange, and cyan have a slightly lower chroma.

##### History of the idea of optimal colors

In the beginning of the 20th century, industrial demands for a controllable way to describe colors and the new possibility to measure light spectra initiated intense research on mathematical descriptions of colors.

The idea of optimal colors was introduced by the Baltic German chemist Wilhelm Ostwald. Erwin Schrödinger showed in his 1919 article **Theorie der Pigmente von größter Leuchtkraft** (Theory of Pigments with Highest Luminosity) that the most-saturated colors that can be created with a given total reflectivity are generated by surfaces having either zero or full reflectance at any given wavelength, and the reflectivity spectrum must have at most two transitions between zero and full.

Schrödinger's work was further developed by David MacAdam and Siegfried Rösch. MacAdam was the first person to calculate precise coordinates of selected points on the boundary of the optimal color solid in the CIE 1931 color space for lightness levels from Y = 10 to 95 in steps of 10 units. This enabled him to draw the optimal color solid at an acceptable degree of precision. Because of his achievement, the boundary of the optimal color solid is called the *MacAdam limit* (1935).

On modern computers, it is possible to calculate an optimal color solid with great precision in seconds. Usually, only the MacAdam limits (the optimal colors, the boundary of the optimal color solid) are computed, because all the other (non-optimal) possible surface colors exist inside the boundary.

##### Pointer's gamut

The optimal color solid represents the **theoretical** limit of the possible colors of surfaces. However, in real life, objects are not color-optimal (at least not the ones that present ordinary reflection). This means that, in practice, the color of a surface is always less chromatic than the optimal color of the same hue and lightness. For practical applications, a smaller, more realistic gamut may be needed.

In 1980, Michael R. Pointer published a gamut for real surfaces with diffuse reflection using 4089 samples, (surfaces with specular reflection, "glossy", can fall outside of this gamut). Originally called a "Munsell Color Cascade", the limits are more commonly called *Pointer's Gamut* after his work.

While this gamut remains important as a reference for color reproduction, newer standards have been created that more accurately define the practical gamut of surfaces, like the ISO SOCS (*Standard Object Colour Spectra*), for which 53,361 surfaces were sampled, including paints, prints, flowers, leaves, human faces, textiles, etc; the ISO *Reference Colour Gamut* (ISORCG, 2007), and the ISO *Gamut of Surface Colours* (ISOGSC, 1998), which was derived from Pointer's data, 1025 Pantone samples, printed samples, and ISO SOCS data.

#### Subtractive color mixing

In subtractive color systems, the color gamut is more often an irregular, rounded region.

The gamut of a CMYK color space is, ideally, the same as that for an RGB one. In practice, due to the way raster-printed colors interact with each other and the paper and due to their non-ideal absorption spectra, the gamut has rounded corners.

#### Light sources

Light sources used as primaries in an additive color reproduction system need to be bright, so they are generally not close to monochromatic. That is, the color gamut of most variable-color light sources can be understood as a result of difficulties producing pure monochromatic (single wavelength) light. The best technological source of monochromatic light is the laser, which can be rather expensive and impractical for many systems. However, as optoelectronic technology matures, single-longitudinal-mode diode lasers are becoming less expensive, and many applications can already profit from this; such as Raman spectroscopy, holography, biomedical research, fluorescence, reprographics, interferometry, semiconductor inspection, remote detection, optical data storage, image recording, spectral analysis, printing, point-to-point free-space communications, and fiber optic communications.

Systems that use additive color processes usually have a color gamut which is roughly a convex polygon (or a slightly concave shape) in a perceptually uniform hue-chroma plane (not to be confused with the chromaticity diagram). The vertices of the polygon are the most chromatic colors that the system can produce.

### Comparison of various systems

Following is a list of representative color systems more-or-less ordered from large to small color gamut:

- A laser video projector uses three lasers to produce the broadest gamut available in practical display equipment today, derived from the fact that lasers produce truly monochromatic primaries. The systems work either by scanning the entire picture a dot at a time and modulating the laser directly at high frequency, much like the electron beams in a cathode-ray tube (CRT), or by optically spreading and then modulating the laser and scanning a line at a time, the line itself being modulated in much the same way as in a DLP projector. Lasers can also be used as a light source for a DLP projector. More than three lasers can be combined to increase the gamut range, a technique sometimes used in holography.
- Digital light processing or DLP technology is a trademarked technology from Texas Instruments. The DLP chip contains a rectangular array of up to 2 million hinge-mounted microscopic mirrors. Each of the micromirrors measures less than one-fifth the width of a human hair. A DLP chip's micromirror tilts either toward the light source in a DLP projection system (ON) or away from it (OFF). This creates a light or dark pixel on the projection surface. Current DLP projectors use a quickly rotating wheel with transparent colored "pie slices" to present each color frame successively. One rotation shows the complete image.
- Photographic film can reproduce a larger color gamut than typical television, computer, or home video systems.
- CRT and similar video displays have a roughly triangular color gamut which covers a significant portion of the visible color space. In CRTs, the limitations are due to the phosphors in the screen which produce red, green, and blue light.
- Liquid-crystal display (LCD) screens filter the light emitted by a backlight. The gamut of an LCD screen is therefore limited to the emitted spectrum of the backlight. Typical LCD screens use cold-cathode fluorescent bulbs (CCFLs) for backlights. LCD Screens with certain LED or wide-gamut CCFL backlights yield a more comprehensive gamut than CRTs. However, some LCD technologies vary the color presented by viewing angle. In-plane switching (IPS) or patterned vertical alignment screens have a wider span of colors than Twisted Nematic.
- Television normally uses a CRT, LCD, LED or plasma display, but does not take full advantage of its color display properties, due to the limitations of broadcasting. The common color profile for TV is based on ITU standard Rec. 601. HDTV is less restrictive and uses a slightly improved color profile based on ITU standard Rec. 709. Still somewhat less than, for example, computer displays using the same display technology. This is due to the use of a limited subset of RGB in broadcasting (values from 16-235), versus full RGB in computer displays, where all bits from 0 to 255 are used.
- Paint mixing, both artistic and for commercial applications, achieves a reasonably large color gamut by starting with a larger palette than the red, green, and blue of CRTs or cyan, magenta, and yellow of printing. Paint may reproduce some highly saturated colors that cannot be reproduced well by CRTs (particularly violet), but overall the color gamut is smaller.
- Printing typically uses the CMYK color space (cyan, magenta, yellow, and black). Very few printing processes do not include black; however, those processes (with the exception of dye-sublimation printers) are poor at representing low saturation, low intensity colors. Efforts have been made to expand the gamut of the printing process by adding inks of non-primary colors; these are typically orange and green (see Hexachrome) or light cyan and light magenta (see CcMmYK color model). Spot color inks of a very specific color are also sometimes used.
- A monochrome display's color gamut is a one-dimensional curve in color space.

#### Wide-color gamut

The Ultra HD Forum defines a wide-color gamut (WCG) as a color gamut wider than Rec. 709 and sRGB. Color spaces with WCGs include:

- Rec. 2020 – ITU-R Recommendation for UHDTV
- Rec. 2100 – ITU-R Recommendation for HDR-TV (same chromaticity of color primaries and white point as Rec. 2020)
- DCI-P3 and DisplayP3
- Adobe RGB color space
- DxO Wide Gamut

#### Extended-gamut printing

The print gamut achieved by using cyan, magenta, yellow, and black inks is sometimes a limitation, for example when printing colors of corporate logos. Therefore, some methods of color printing use additional ink colors to achieve a larger gamut. For example, some use green, orange, and violet inks to increase the achievable saturation of hues near those. These method are variously called heptatone color printing, extended gamut printing, and 7-color printing, etc.

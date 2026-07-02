---
title: "Color gradient"
source: https://en.wikipedia.org/wiki/Color_gradient
domain: sequential-diverging-palettes
license: CC-BY-SA-4.0
tags: sequential palette, diverging palette, color scheme, quantitative color
fetched: 2026-07-02
---

# Color gradient

In color science, a **color gradient** (also known as a **color ramp** or a **color progression**) specifies a range of position-dependent colors, usually used to fill a region.

In assigning colors to a set of values, a gradient is a continuous colormap, a type of color scheme. In computer graphics, the term swatch has come to mean a palette of active colors.

- real world color gradients or swatch books
- (RAL CLASSIC K5 color fan) RAL CLASSIC K5 color fan
- (Pantone color guide) Pantone color guide
- (cards of Pantone base colors and blends) cards of Pantone base colors and blends
- (HKS colour fan) HKS colour fan

## Definitions

- Color gradient is a set of colors arranged in a linear order (ordered)
- A continuous colormap is a curve through a colorspace

- curve through RGB colorspace
- (gray) gray
- (cubehelix[2]) cubehelix
- (HSV rainbow) HSV rainbow
- (diverging[3]) diverging

### Strict definition

A colormap is a function which associate a real value r with point c in color space C

$f:[r_{min},r_{max}]\subset \mathbf {R} \to C$

which is defined by:

- a colorspace C
- an increasing sequence of sampling points $r_{0}<...<r_{m}\in [r_{min},r_{max}]$
- a series of values in the colorspace $c_{0},...,c_{m}\in C$
- the mapping $f(r_{i})=c_{i},i=0,...,m$
- a rule for interpolating the intermediate values $r_{i-1}<r<r_{i}\in [r_{min},r_{max}]$

where:

- r is a real number $r\in [r_{min},r_{max}]\subset \mathbf {R}$
- $\mathbf {R}$ is a set of real numbers
- c is a color = point in colorspace C

## Types

Criteria for classification:

- dimension
- discrete ( classed, color scheme) / continuous
- shape
- range: full or limited. Example : pastel color with limited range of saturation.
- perceptual uniformity
- order
  - ordered (sequential) and non-ordered (categorical)
  - perceptual order
- readability for color-vision deficient or color-blind people ( colorblind-friendly)
- color space
- color depth

### Dimension

- 1D
- 2D: Multivariate map, bivariate or trivariate
- 3D

### Shapes

#### Axial gradients

An axial color gradient (sometimes also called a linear color gradient) is specified by two points, and a color at each point. The colors along the line through those points are calculated using linear interpolation, then extended perpendicular to that line. In digital imaging systems, colors are typically interpolated in an RGB color space, often using gamma compressed RGB color values, as opposed to linear. CSS and SVG both support linear gradients.

#### Radial gradients

A radial gradient is specified as a circle that has one color at the edge and another at the center. Colors are calculated by linear interpolation based on distance from the center. This can be used to approximate the diffuse reflection of light from a point source by a sphere. Both CSS and SVG support radial gradients.

#### Conic gradients

Conic or conical gradients are gradients with color transitions rotated around a center point (rather than radiating from the center). Example conic gradients include pie charts and color wheels. Conic gradients are sometimes called "sweep gradients" (for example in the OpenType specification) or angular gradients.

#### Other shapes

In vector graphics polygon meshes can be used, e.g., Adobe Illustrator supports *gradient meshes*.

### Color space

- (LCH) LCH
- (HSV) HSV

#### Effect of color space

The appearance of a gradient not only varies by the color themselves, but also by the color space the calculation is performed in. The problem usually becomes important for two reasons:

- Gamma correction to a color space. With a typical γ of around 2, it is easy to see that a gamma-enabled color space will blend darker than a linear-intensity color space, since the sum of squares of two numbers is never more than the square of their sum. The effect is most apparent in blending complementary colors like red and green, with the middle color being a dark color instead of the expected yellow. The radial and conic examples on this page clearly exhibit this error.
- Handling of other perceptual properties. In information visualization, it is undesirable to have a supposedly "flat" gradient show non-monotonic variations in lightness and saturation along the way. This is because human vision emphasizes these qualities, causing bias or confusion in interpretation.

A "linear" blend would match physical light blending and has been the standard in game engines for a long time. On the web, however, it has long been neglected for both color gradients and image scaling. Such a blend still has a subtle difference from one done in a perceptually-uniform color space.

## Examples

- 2D RGB profiles

- Gradient on HSV color wheel
- (Single hue (monochromatic) gradient) Single hue (monochromatic) gradient
- (polychromatic (multi hue) color gradient) polychromatic (multi hue) color gradient

### HSV rainbow

- HSV rainbow
- (RGB 2D profiles) RGB 2D profiles
- (HSV 2D profiles) HSV 2D profiles
- (3D RGB profile) 3D RGB profile

## Applications

- represent quantitative or ordinal values, like in heat maps. More precise description is in color box.
  - data visualisation
- fill a region: many window managers allow the screen background to be specified as a gradient. The colors produced by a gradient vary continuously with position, producing smooth color transitions.
- visualize the progression of an extended computer operation, such as a download, file transfer, or installation. See progress bar
- Coloring cartographic maps

- Color gradients in physics
- (Color temperature black body 800-12200K) Color temperature black body 800-12200K
- (Colours of the visible light spectrum) Colours of the visible light spectrum
- (classed color gradient) classed color gradient
- (Warming stripes that use classed color gradient) Warming stripes that use classed color gradient

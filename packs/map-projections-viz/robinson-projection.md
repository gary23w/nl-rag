---
title: "Robinson projection"
source: https://en.wikipedia.org/wiki/Robinson_projection
domain: map-projections-viz
license: CC-BY-SA-4.0
tags: map projection, tissot indicatrix, robinson projection, winkel tripel
fetched: 2026-07-02
---

# Robinson projection

The **Robinson projection** is a map projection of a world map that shows the entire world at once. It was created in an attempt to find a good compromise to the problem of readily showing the whole globe as a flat image.

The Robinson projection was devised by Arthur H. Robinson in 1963 in response to an appeal from the Rand McNally company, which has used the projection in general-purpose world maps since that time. Robinson published details of the projection's construction in 1974. The National Geographic Society (NGS) began using the Robinson projection for general-purpose, full world maps in 1988, replacing the Van der Grinten projection. In 1998, the NGS abandoned the Robinson projection for that use in favor of the Winkel tripel projection, as the latter "reduces the distortion of land masses as they near the poles".

## Strengths and weaknesses

The Robinson projection is neither equal-area nor conformal, abandoning both for a compromise. The creator felt that this produced a better overall view than could be achieved by adhering to either. The meridians curve gently, avoiding extremes, but thereby stretch the poles into long lines instead of leaving them as points.

Hence, distortion close to the poles is severe, but quickly declines to moderate levels moving away from them. The straight parallels imply severe angular distortion at the high latitudes toward the outer edges of the map – a fault inherent in any pseudocylindrical projection. However, at the time it was developed, the projection effectively met Rand McNally's goal to produce appealing depictions of the entire world.

> I decided to go about it backwards. … I started with a kind of artistic approach. I visualized the best-looking shapes and sizes. I worked with the variables until it got to the point where, if I changed one of them, it didn't get any better. Then I figured out the mathematical formula to produce that effect. Most mapmakers start with the mathematics.

— 1988 *New York Times* article

## Formulation

The projection is defined by the table:

| Latitude | *X* | *Y* |
|---|---|---|
| 0° | 1.0000 | 0.0000 |
| 5° | 0.9986 | 0.0620 |
| 10° | 0.9954 | 0.1240 |
| 15° | 0.9900 | 0.1860 |
| 20° | 0.9822 | 0.2480 |
| 25° | 0.9730 | 0.3100 |
| 30° | 0.9600 | 0.3720 |
| 35° | 0.9427 | 0.4340 |
| 40° | 0.9216 | 0.4958 |
| 45° | 0.8962 | 0.5571 |
| 50° | 0.8679 | 0.6176 |
| 55° | 0.8350 | 0.6769 |
| 60° | 0.7986 | 0.7346 |
| 65° | 0.7597 | 0.7903 |
| 70° | 0.7186 | 0.8435 |
| 75° | 0.6732 | 0.8936 |
| 80° | 0.6213 | 0.9394 |
| 85° | 0.5722 | 0.9761 |
| 90° | 0.5322 | 1.0000 |

The table is indexed by latitude at 5-degree intervals; intermediate values are calculated using interpolation. Robinson did not specify any particular interpolation method, but it is reported that others used either Aitken interpolation (with polynomials of unknown degrees) or cubic splines while analyzing area deformation on the Robinson projection. The *X* column is the ratio of the length of the parallel to the length of the equator; the *Y* column can be multiplied by 0.2536 to obtain the ratio of the distance of that parallel from the equator to the length of the equator.

Coordinates of points on a map are computed as follows:

${\begin{aligned}x&=0.8487\,RX(\lambda -\lambda _{0}),\\y&=1.3523\,RY,\end{aligned}}$ where *R* is the radius of the globe at the scale of the map, *λ* is the longitude of the point to plot, and *λ*0 is the central meridian chosen for the map (both *λ* and *λ*0 are expressed in radians).

Simple consequences of these formulas are:

- With *x* computed as a constant multiplier to the meridian across the entire parallel, meridians of longitude are thus equally spaced along the parallel.
- With *y* having no dependency on longitude, parallels are straight horizontal lines.

## Applications

- The Central Intelligence Agency World Factbook uses the Robinson projection in its political and physical world maps.
- The European Centre for Disease Prevention and Control recommends using the Robinson projection for mapping the whole world.

---
title: "Winkel tripel projection"
source: https://en.wikipedia.org/wiki/Winkel_tripel_projection
domain: map-projections-viz
license: CC-BY-SA-4.0
tags: map projection, tissot indicatrix, robinson projection, winkel tripel
fetched: 2026-07-02
---

# Winkel tripel projection

The **Winkel tripel projection** (**Winkel III**), a modified azimuthal map projection of the world, is one of three projections proposed by German cartographer Oswald Winkel in 1921. The projection is the arithmetic mean of the equirectangular projection and the Aitoff projection: The name *tripel* (German for 'triple') refers to Winkel's goal of minimizing three kinds of distortion: area, direction, and distance.

## Algorithm

${\begin{aligned}x&={\frac {1}{2}}\left(\lambda \cos \varphi _{1}+{\frac {2\cos \varphi \sin {\frac {\lambda }{2}}}{\operatorname {sinc} \alpha }}\right),\\y&={\frac {1}{2}}\left(\varphi +{\frac {\sin \varphi }{\operatorname {sinc} \alpha }}\right),\end{aligned}}$

where *λ* is the longitude relative to the central meridian of the projection, *$\varphi$* is the latitude, *$\varphi$*1 is the standard parallel for the equirectangular projection, sinc is the unnormalized cardinal sine function, and

$\alpha =\arccos \left(\cos \varphi \cos {\frac {\lambda }{2}}\right).$

In his proposal, Winkel set

$\varphi _{1}=\arccos {\frac {2}{\pi }}.$

A closed-form inverse mapping does not exist, and computing the inverse numerically requires the use of iterative methods.

## Comparison with other projections

David M. Goldberg and J. Richard Gott III showed that the Winkel tripel fares better against several other projections analyzed against their measures of distortion, producing minimal distance, Tissot indicatrix ellipticity and area errors, and the least skew of any of the projections they studied. By a different metric, Capek's "Q", the Winkel tripel ranked ninth among a hundred map projections of the world, behind the common Eckert IV projection and Robinson projections.

In 1998, the Winkel tripel projection replaced the Robinson projection as the standard projection for world maps made by the National Geographic Society. Many educational institutes and textbooks soon followed National Geographic's example in adopting the projection, most of which still utilize it as of 2012.

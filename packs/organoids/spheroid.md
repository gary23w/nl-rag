---
title: "Spheroid"
source: https://en.wikipedia.org/wiki/Spheroid
domain: organoids
license: CC-BY-SA-4.0
tags: organoid culture, three dimensional tissue, self organization, matrigel
fetched: 2026-07-02
---

# Spheroid

|   |   |
|---|---|
| oblate | prolate |

A **spheroid**, also known as an **ellipsoid of revolution** or **rotational ellipsoid**, is a quadric surface obtained by rotating an ellipse about one of its principal axes; in other words, an ellipsoid with two equal semi-diameters. A spheroid has circular symmetry.

If the ellipse is rotated about its major axis, the result is a **prolate spheroid**, elongated like a rugby ball. The American football is similar but has a pointier end than a spheroid could. If the ellipse is rotated about its minor axis, the result is an **oblate spheroid**, flattened like a lentil or a plain M&M. If the generating ellipse is a circle, the result is a sphere.

Due to the combined effects of gravity and rotation, the figure of the Earth (and of all planets) is not quite a sphere, but instead is slightly flattened in the direction of its axis of rotation. For that reason, in cartography and geodesy the Earth is often approximated by an oblate spheroid, known as the reference ellipsoid, instead of a sphere. The current World Geodetic System model uses a spheroid whose radius is 6,378.137 km (3,963.191 mi) at the Equator and 6,356.752 km (3,949.903 mi) at the poles.

The word *spheroid* originally meant "an approximately spherical body", admitting irregularities even beyond the bi- or tri-axial ellipsoidal shape; that is how the term is used in some older papers on geodesy (for example, referring to truncated spherical harmonic expansions of the Earth's gravity geopotential model).

## Equation

The equation of a tri-axial ellipsoid centred at the origin with semi-axes a, b and c aligned along the coordinate axes is

${\frac {x^{2}}{a^{2}}}+{\frac {y^{2}}{b^{2}}}+{\frac {z^{2}}{c^{2}}}=1.$

The equation of a spheroid with z as the symmetry axis is given by setting *a* = *b*:

${\frac {x^{2}+y^{2}}{a^{2}}}+{\frac {z^{2}}{c^{2}}}=1.$

The semi-axis a is the equatorial radius of the spheroid, and c is the distance from centre to pole along the symmetry axis. There are two possible cases:

- *c* < *a*: oblate spheroid
- *c* > *a*: prolate spheroid

The case of *a* = *c* reduces to a sphere.

## Properties

### Circumference

The equatorial circumference of a spheroid is measured around its equator and is given as:

$C_{\text{e}}=2\pi a$

The meridional or polar circumference of a spheroid is measured through its poles and is given as: $C_{\text{p}}\,=\,4a\int _{0}^{\pi /2}{\sqrt {1-e^{2}\sin ^{2}\theta }}\ d\theta$ The volumetric circumference of a spheroid is the circumference of a sphere of equal volume as the spheroid and is given as:

$C_{\text{v}}=2{\sqrt[{3}]{a^{2}c}}$

### Area

An oblate spheroid with *c* < *a* has surface area

$S_{\text{o}}=2\pi a^{2}\left(1+{\frac {1-e_{o}^{2}}{e_{o}}}\operatorname {arctanh} e_{o}\right)=2\pi a^{2}+\pi {\frac {c^{2}}{e_{o}}}\ln \left({\frac {1+e_{o}}{1-e_{o}}}\right)$

where $e_{o}^{2}=1-{\frac {c^{2}}{a^{2}}}$ . A prolate spheroid with *c* > *a* has surface area

$S_{\text{p}}=2\pi a^{2}\left(1+{\frac {c}{ae_{p}}}\arcsin \,e_{p}\right)$

where $e_{p}^{2}=1-{\frac {a^{2}}{c^{2}}}.$ In both cases, eo and ep may be identified as the eccentricity (see ellipse).

These formulas are identical in the sense that the formula for *S*o can be used to calculate the surface area of a prolate spheroid and vice versa. However, eo then becomes imaginary and can no longer directly be identified with the eccentricity. Both of these results may be cast into many other forms using standard mathematical identities and relations between parameters of the ellipse.

### Volume

The volume inside a spheroid (of any kind) is

$V={\tfrac {4}{3}}\pi a^{2}c\approx 4.19a^{2}c.$

If *A* = 2*a* is the equatorial diameter, and *C* = 2*c* is the polar diameter, the volume is

$V={\tfrac {\pi }{6}}A^{2}C\approx 0.523A^{2}C.$

### Curvature

Let a spheroid be parameterized as

${\boldsymbol {\sigma }}(\beta ,\lambda )=(a\cos \beta \cos \lambda ,a\cos \beta \sin \lambda ,c\sin \beta ),$

where β is the *reduced latitude* or *parametric latitude* and λ is the longitude, with domain −⁠π/2⁠ < *β* < +⁠π/2⁠ and −π < *λ* < +π, respectively. Then, the spheroid's Gaussian curvature is:

$K(\beta )={\frac {c^{2}}{\left(a^{2}+\left(c^{2}-a^{2}\right)\cos ^{2}\beta \right)^{2}}},$

and its mean curvature is

$H(\beta )={\frac {c\left(2a^{2}+\left(c^{2}-a^{2}\right)\cos ^{2}\beta \right)}{2a\left(a^{2}+\left(c^{2}-a^{2}\right)\cos ^{2}\beta \right)^{\frac {3}{2}}}}.$

Both of these curvatures are a function of latitude only and are always positive, so that every point on a spheroid is elliptic.

### Aspect ratio

The *aspect ratio* of an oblate spheroid/ellipse, *c* : *a*, is the ratio of the polar to equatorial lengths, while the *flattening* (also called *oblateness*) f, is the ratio of the equatorial-polar length difference to the equatorial length:

$f={\frac {a-c}{a}}=1-{\frac {c}{a}}.$

The first *eccentricity* (usually simply eccentricity, as above) is often used instead of flattening. It is defined by:

$e={\sqrt {1-{\frac {c^{2}}{a^{2}}}}}$

The relations between eccentricity and flattening are:

${\begin{aligned}e&={\sqrt {2f-f^{2}}}\\f&=1-{\sqrt {1-e^{2}}}\end{aligned}}$

All modern geodetic ellipsoids are defined by the semi-major axis plus either the semi-minor axis (giving the aspect ratio), the flattening, or the first eccentricity. While these definitions are mathematically interchangeable, real-world calculations must lose some precision. To avoid confusion, an ellipsoidal definition considers its own values to be exact in the form it gives.

## Occurrence and applications

The most common shapes for the density distribution of protons and neutrons in an atomic nucleus are spherical, prolate, and oblate spheroidal, where the polar axis is assumed to be the spin axis (or direction of the spin angular momentum vector). Deformed nuclear shapes occur as a result of the competition between electromagnetic repulsion between protons, surface tension and quantum shell effects.

Spheroids are common in 3D cell cultures. Rotating equilibrium spheroids include the Maclaurin spheroid and the Jacobi ellipsoid. Spheroid is also a shape of archaeological artifacts.

### Oblate spheroids

The oblate spheroid is the approximate shape of rotating planets and other celestial bodies, including Earth, Saturn, Jupiter, and the quickly spinning star Altair. Saturn is the most oblate planet in the Solar System, with a flattening of 0.09796. See planetary flattening and equatorial bulge for details.

Enlightenment scientist Isaac Newton, working from Jean Richer's pendulum experiments and Christiaan Huygens's theories for their interpretation, reasoned that Jupiter and Earth are oblate spheroids owing to their centrifugal force. Earth's diverse cartographic and geodetic systems are based on reference ellipsoids, all of which are oblate.

### Prolate spheroids

The prolate spheroid is the approximate shape of the ball used in American football and in rugby.

Several moons of the Solar System approximate prolate spheroids in shape, though they are closer to triaxial ellipsoids. Examples are Saturn's satellites Mimas, Enceladus, and Tethys and Uranus's satellite Miranda.

In contrast to being distorted into oblate spheroids via rapid rotation, celestial objects distort slightly into prolate spheroids via tidal forces when they orbit a massive body in a close orbit. The most extreme example is Jupiter's moon Io, which becomes slightly more or less prolate in its orbit due to a slight eccentricity, causing intense volcanism. The major axis of the prolate spheroid does not run through the satellite's poles in this case, but through the two points on its equator directly facing toward and away from the primary. This combines with the smaller oblate distortion from the synchronous rotation to cause the body to become triaxial.

The term is also used to describe the shape of some nebulae such as the Crab Nebula. Fresnel zones, used to analyze wave propagation and interference in space, are a series of concentric prolate spheroids with principal axes aligned along the direct line-of-sight between a transmitter and a receiver.

The atomic nuclei of the actinide and lanthanide elements are shaped like prolate spheroids. In anatomy, near-spheroid organs such as testis may be measured by their long and short axes.

Many submarines have a shape which can be described as prolate spheroid.

### Dynamical properties

For a spheroid having uniform density, the moment of inertia is that of an ellipsoid with an additional axis of symmetry. Given a description of a spheroid as having a major axis c, and minor axes a = b, the moments of inertia along these principal axes are C, A, and B. However, in a spheroid the minor axes are symmetrical. Therefore, our inertial terms along the major axes are:

${\begin{aligned}A=B&={\tfrac {1}{5}}M\left(a^{2}+c^{2}\right),\\C&={\tfrac {1}{5}}M\left(a^{2}+b^{2}\right)={\tfrac {2}{5}}M\left(a^{2}\right),\end{aligned}}$

where M is the mass of the body defined as

$M={\tfrac {4}{3}}\pi a^{2}c\rho .$

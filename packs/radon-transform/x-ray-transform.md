---
title: "X-ray transform"
source: https://en.wikipedia.org/wiki/X-ray_transform
domain: radon-transform
license: CC-BY-SA-4.0
tags: radon transform, filtered back projection, tomographic reconstruction, projection-slice theorem
fetched: 2026-07-02
---

# X-ray transform

In mathematics, the **X-ray transform** (also called **ray transform** or **John transform**) is an integral transform introduced by Fritz John in 1938 that is one of the cornerstones of modern integral geometry. It is very closely related to the Radon transform, and coincides with it in two dimensions. In higher dimensions, the X-ray transform of a function is defined by integrating over lines rather than over hyperplanes as in the Radon transform. The X-ray transform derives its name from X-ray tomography (used in CT scans) because the X-ray transform of a function *ƒ* represents the attenuation data of a tomographic scan through an inhomogeneous medium whose density is represented by the function *ƒ*. Inversion of the X-ray transform is therefore of practical importance because it allows one to reconstruct an unknown density *ƒ* from its known attenuation data.

In detail, if *ƒ* is a compactly supported continuous function on the Euclidean space **R***n*, then the X-ray transform of *ƒ* is the function *Xƒ* defined on the set of all lines in **R***n* by

$Xf(L)=\int _{L}f=\int _{\mathbf {R} }f(x_{0}+t\theta )dt$

where *x*0 is an initial point on the line and *θ* is a unit vector in **R***n* giving the direction of the line *L*. The latter integral is not regarded in the oriented sense: it is the integral with respect to the 1-dimensional Lebesgue measure on the Euclidean line *L*.

The X-ray transform satisfies an ultrahyperbolic wave equation called John's equation.

The Gaussian or ordinary hypergeometric function can be written as an X-ray transform.(Gelfand, Gindikin & Graev 2003, 2.1.2).

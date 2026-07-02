---
title: "Funk transform"
source: https://en.wikipedia.org/wiki/Funk_transform
domain: radon-transform
license: CC-BY-SA-4.0
tags: radon transform, filtered back projection, tomographic reconstruction, projection-slice theorem
fetched: 2026-07-02
---

# Funk transform

In the mathematical field of integral geometry, the **Funk transform** (also known as **Minkowski–Funk transform**, **Funk–Radon transform** or **spherical Radon transform**) is an integral transform defined by integrating a function on great circles of the sphere. It was introduced by Paul Funk in 1911, based on the work of Minkowski (1904). It is closely related to the Radon transform. The original motivation for studying the Funk transform was to describe Zoll metrics on the sphere.

## Definition

The Funk transform is defined as follows. Let *ƒ* be a continuous function on the d-1-sphere **S**d-1 in **R**d. Then, for a unit vector **x**, let

$Ff(\mathbf {x} )=\int _{\mathbf {u} \in C(\mathbf {x} )}f(\mathbf {u} )\,ds(\mathbf {u} )$

where the integral is carried out with respect to the arclength *ds* of the great circle *C*(**x**) consisting of all unit vectors perpendicular to **x**:

$C(\mathbf {x} )=\{\mathbf {u} \in S^{d-1}\mid \mathbf {u} \cdot \mathbf {x} =0\}.$

## Inversion

The Funk transform annihilates all odd functions, and so it is natural to confine attention to the case when *ƒ* is even. In that case, the Funk transform takes even (continuous) functions to even continuous functions, and is furthermore invertible.

### Spherical harmonics

Every square-integrable function $f\in L^{2}(S^{2})$ on the sphere can be decomposed into spherical harmonics $Y_{n}^{k}$

$f=\sum _{n=0}^{\infty }\sum _{k=-n}^{n}{\hat {f}}(n,k)Y_{n}^{k}.$

Then the Funk transform of *f* reads

$Ff=\sum _{n=0}^{\infty }\sum _{k=-n}^{n}P_{n}(0){\hat {f}}(n,k)Y_{n}^{k}$

where $P_{2n+1}(0)=0$ for odd values and

$P_{2n}(0)=(-1)^{n}\,{\frac {1\cdot 3\cdot 5\cdots 2n-1}{2\cdot 4\cdot 6\cdots 2n}}=(-1)^{n}\,{\frac {(2n-1)!!}{(2n)!!}}$

for even values. This result was shown by Funk (1913).

### Helgason's inversion formula

Another inversion formula is due to Helgason (1999). As with the Radon transform, the inversion formula relies on the dual transform *F** defined by

$(F^{*}f)(p,\mathbf {x} )={\frac {1}{2\pi \cos p}}\int _{\|\mathbf {u} \|=1,\mathbf {x} \cdot \mathbf {u} =\sin p}f(\mathbf {u} )\,|d\mathbf {u} |.$

This is the average value of the circle function *ƒ* over circles of arc distance *p* from the point **x**. The inverse transform is given by

$f(\mathbf {x} )={\frac {1}{2\pi }}\left\{{\frac {d}{du}}\int _{0}^{u}F^{*}(Ff)(\cos ^{-1}v,\mathbf {x} )v(u^{2}-v^{2})^{-1/2}\,dv\right\}_{u=1}.$

## Generalization

The classical formulation is invariant under the rotation group SO(3). It is also possible to formulate the Funk transform in a manner that makes it invariant under the special linear group SL(3,**R**) (Bailey et al. 2003). Suppose that *ƒ* is a homogeneous function of degree −2 on **R**3. Then, for linearly independent vectors **x** and **y**, define a function φ by the line integral

$\varphi (\mathbf {x} ,\mathbf {y} )={\frac {1}{2\pi }}\oint f(u\mathbf {x} +v\mathbf {y} )(u\,dv-v\,du)$

taken over a simple closed curve encircling the origin once. The differential form

$f(u\mathbf {x} +v\mathbf {y} )(u\,dv-v\,du)$

is closed, which follows by the homogeneity of *ƒ*. By a change of variables, φ satisfies

$\phi (a\mathbf {x} +b\mathbf {y} ,c\mathbf {x} +d\mathbf {y} )={\frac {1}{|ad-bc|}}\phi (\mathbf {x} ,\mathbf {y} ),$

and so gives a homogeneous function of degree −1 on the exterior square of **R**3,

$Ff(\mathbf {x} \wedge \mathbf {y} )=\phi (\mathbf {x} ,\mathbf {y} ).$

The function *Fƒ* : Λ2**R**3 → **R** agrees with the Funk transform when *ƒ* is the degree −2 homogeneous extension of a function on the sphere and the projective space associated to Λ2**R**3 is identified with the space of all circles on the sphere. Alternatively, Λ2**R**3 can be identified with **R**3 in an SL(3,**R**)-invariant manner, and so the Funk transform *F* maps smooth even homogeneous functions of degree −2 on **R**3\{0} to smooth even homogeneous functions of degree −1 on **R**3\{0}.

## Applications

The Funk-Radon transform is used in the Q-Ball method for Diffusion MRI introduced by Tuch (2004). It is also related to intersection bodies in convex geometry. Let $K\subset \mathbb {R} ^{d}$ be a star body with radial function $\rho _{K}({\boldsymbol {x}})=\max\{t:t{\boldsymbol {x}}\in K\},$ $x\in S^{d-1}$ . Then the intersection body *IK* of *K* has the radial function $\rho _{IK}=F\rho _{K}$ (Gardner 2006, p. 305).

---
title: "Abel transform"
source: https://en.wikipedia.org/wiki/Abel_transform
domain: hankel-transform
license: CC-BY-SA-4.0
tags: hankel transform, abel transform, struve function, neumann series
fetched: 2026-07-02
---

# Abel transform

In mathematics, the **Abel transform**, named for Niels Henrik Abel, is an integral transform often used in the analysis of spherically symmetric or axially symmetric functions. The Abel transform of a function *f*(*r*) is given by

$F(y)=2\int _{y}^{\infty }{\frac {f(r)r}{\sqrt {r^{2}-y^{2}}}}\,dr.$

Assuming that *f*(*r*) drops to zero more quickly than ⁠1/*r*⁠, the inverse Abel transform is given by

$f(r)=-{\frac {1}{\pi }}\int _{r}^{\infty }{\frac {dF}{dy}}\,{\frac {dy}{\sqrt {y^{2}-r^{2}}}}.$

In image analysis, the forward Abel transform is used to project an optically thin, axially symmetric emission function onto a plane, and the inverse Abel transform is used to calculate the emission function given a projection (i.e. a scan or a photograph) of that emission function.

In absorption spectroscopy of cylindrical flames or plumes, the forward Abel transform is the integrated absorbance along a ray with closest distance y from the center of the flame, while the inverse Abel transform gives the local absorption coefficient at a distance r from the center. Abel transform is limited to applications with axially symmetric geometries. For more general asymmetrical cases, more general-oriented reconstruction algorithms such as algebraic reconstruction technique (ART), maximum likelihood expectation maximization (MLEM), filtered back-projection (FBP) algorithms should be employed.

In recent years, the inverse Abel transform (and its variants) has become the cornerstone of data analysis in photofragment-ion imaging and photoelectron imaging. Among recent most notable extensions of inverse Abel transform are the "onion peeling" and "basis set expansion" (BASEX) methods of photoelectron and photoion image analysis.

## Geometrical interpretation

In two dimensions, the Abel transform *F*(*y*) can be interpreted as the projection of a circularly symmetric function *f*(*r*) along a set of parallel lines of sight at a distance y from the origin. Referring to the figure on the right, the observer (I) will see

$F(y)=\int _{-\infty }^{\infty }f\left({\sqrt {x^{2}+y^{2}}}\right)\,dx,$

where *f*(*r*) is the circularly symmetric function represented by the gray color in the figure. It is assumed that the observer is actually at *x* = ∞, so that the limits of integration are ±∞, and all lines of sight are parallel to the x axis. Realizing that the radius r is related to x and y as *r*2 = *x*2 + *y*2, it follows that

$dx={\frac {r\,dr}{\sqrt {r^{2}-y^{2}}}}$

for *x* > 0. Since *f*(*r*) is an even function in x, we may write

$F(y)=2\int _{0}^{\infty }f\left({\sqrt {x^{2}+y^{2}}}\right)\,dx=2\int _{|y|}^{\infty }f(r)\,{\frac {r\,dr}{\sqrt {r^{2}-y^{2}}}},$

which yields the Abel transform of *f*(*r*).

The Abel transform may be extended to higher dimensions. Of particular interest is the extension to three dimensions. If we have an axially symmetric function *f*(*ρ*, *z*), where *ρ*2 = *x*2 + *y*2 is the cylindrical radius, then we may want to know the projection of that function onto a plane parallel to the *z* axis. Without loss of generality, we can take that plane to be the yz plane, so that

$F(y,z)=\int _{-\infty }^{\infty }f(\rho ,z)\,dx=2\int _{y}^{\infty }{\frac {f(\rho ,z)\rho \,d\rho }{\sqrt {\rho ^{2}-y^{2}}}},$

which is just the Abel transform of *f*(*ρ*, *z*) in ρ and y.

A particular type of axial symmetry is spherical symmetry. In this case, we have a function *f*(*r*), where *r*2 = *x*2 + *y*2 + *z*2. The projection onto, say, the yz plane will then be circularly symmetric and expressible as *F*(*s*), where *s*2 = *y*2 + *z*2. Carrying out the integration, we have

$F(s)=\int _{-\infty }^{\infty }f(r)\,dx=2\int _{s}^{\infty }{\frac {f(r)r\,dr}{\sqrt {r^{2}-s^{2}}}},$

which is again, the Abel transform of *f*(*r*) in r and s.

## Verification of the inverse Abel transform

Assuming f is continuously differentiable, and f, f′ drop to zero faster than ⁠1/*r*⁠, we can integrate by parts by setting

$u=f(r),\quad v'={\frac {r}{\sqrt {r^{2}-y^{2}}}},$

to find

$F(y)=-2\int _{y}^{\infty }f'(r){\sqrt {r^{2}-y^{2}}}\,dr.$

Differentiating formally,

$F'(y)=2y\int _{y}^{\infty }{\frac {f'(r)}{\sqrt {r^{2}-y^{2}}}}\,dr.$

Now substitute this into the inverse Abel transform formula:

$-{\frac {1}{\pi }}\int _{r}^{\infty }{\frac {F'(y)}{\sqrt {y^{2}-r^{2}}}}\,dy=\int _{r}^{\infty }\int _{y}^{\infty }{\frac {-2y}{\pi {\sqrt {\left(y^{2}-r^{2}\right)\left(s^{2}-y^{2}\right)}}}}f'(s)\,dsdy.$

By Fubini's theorem, the last integral equals

$\int _{r}^{\infty }\int _{r}^{s}{\frac {-2y}{\pi {\sqrt {\left(y^{2}-r^{2}\right)\left(s^{2}-y^{2}\right)}}}}\,dyf'(s)\,ds=\int _{r}^{\infty }(-1)f'(s)\,ds=f(r).$

## Generalization of the Abel transform to discontinuous *F*(*y*)

Consider the case where *F*(*y*) is discontinuous at *y* = *y*Δ, where it abruptly changes its value by a finite amount Δ*F*. That is, *y*Δ and Δ*F* are defined by

$\Delta F\equiv \lim _{\varepsilon \rightarrow 0}{\bigl (}F(y_{\Delta }-\varepsilon )-F(y_{\Delta }+\varepsilon ){\bigr )}.$

Such a situation is encountered in tethered polymers (Polymer brush) exhibiting a vertical phase separation, where *F*(*y*) stands for the polymer density profile and $f(r)$ is related to the spatial distribution of terminal, non-tethered monomers of the polymers.

The Abel transform of a function *f*(*r*) is under these circumstances again given by:

$F(y)=2\int _{y}^{\infty }{\frac {f(r)r\,dr}{\sqrt {r^{2}-y^{2}}}}.$

Assuming *f*(*r*) drops to zero more quickly than ⁠1/*r*⁠, the inverse Abel transform is however given by

$f(r)=\left({\frac {1}{2}}\delta \left(r-y_{\Delta }\right){\sqrt {1-\left({\frac {y_{\Delta }}{r}}\right)^{2}}}-{\frac {1}{\pi }}{\frac {H\left(y_{\Delta }-r\right)}{\sqrt {y_{\Delta }^{2}-r^{2}}}}\right)\Delta F-{\frac {1}{\pi }}\int _{r}^{\infty }{\frac {dF}{dy}}{\frac {dy}{\sqrt {y^{2}-r^{2}}}}.$

where δ is the Dirac delta function and *H*(*x*) the Heaviside step function. The extended version of the Abel transform for discontinuous F is proven upon applying the Abel transform to shifted, continuous *F*(*y*), and it reduces to the classical Abel transform when Δ*F* = 0. If *F*(*y*) has more than a single discontinuity, one has to introduce shifts for any of them to come up with a generalized version of the inverse Abel transform which contains n additional terms, each of them corresponding to one of the n discontinuities.

## Relationship to other integral transforms

### Relationship to the Fourier and Hankel transforms

The Abel transform is one member of the FHA cycle of integral operators. For example, in two dimensions, if we define A as the Abel transform operator, F as the Fourier transform operator and H as the zeroth-order Hankel transform operator, then the special case of the projection-slice theorem for circularly symmetric functions states that

$FA=H.$

In other words, applying the Abel transform to a one-dimensional function and then applying the Fourier transform to that result is the same as applying the Hankel transform to that function. This concept can be extended to higher dimensions.

### Relationship to the Radon transform

Abel transform can be viewed as the Radon transform of an isotropic 2D function *f*(*r*). As *f*(*r*) is isotropic, its Radon transform is the same at different angles of the viewing axis. Thus, the Abel transform is a function of the distance along the viewing axis only.

---
title: "Hankel transform"
source: https://en.wikipedia.org/wiki/Hankel_transform
domain: hankel-transform
license: CC-BY-SA-4.0
tags: hankel transform, abel transform, struve function, neumann series
fetched: 2026-07-02
---

# Hankel transform

In mathematics, the **Hankel transform** expresses any given function *f*(*r*) as the weighted sum of an infinite number of Bessel functions of the first kind *Jν*(*kr*). The Bessel functions in the sum are all of the same order ν, but differ in a scaling factor *k* along the *r* axis. The necessary coefficient *Fν* of each Bessel function in the sum, as a function of the scaling factor *k* constitutes the transformed function. The Hankel transform is an integral transform and was first developed by the mathematician Hermann Hankel. It is also known as the **Fourier–Bessel transform**. Just as the Fourier transform for an infinite interval is related to the Fourier series over a finite interval, so the Hankel transform over an infinite interval is related to the Fourier–Bessel series over a finite interval.

## Definition

The **Hankel transform** of order $\nu$ of a function *f*(*r*) is given by

$F_{\nu }(k)=\int _{0}^{\infty }f(r)J_{\nu }(kr)\,r\,\mathrm {d} r,$

where $J_{\nu }$ is the Bessel function of the first kind of order $\nu$ with $\nu \geq -1/2$ . The inverse Hankel transform of *Fν*(*k*) is defined as

$f(r)=\int _{0}^{\infty }F_{\nu }(k)J_{\nu }(kr)\,k\,\mathrm {d} k,$

which can be readily verified using the orthogonality relationship described below.

### Domain of definition

Inverting a Hankel transform of a function *f*(*r*) is valid at every point at which *f*(*r*) is continuous, provided that the function is defined in (0, ∞), is piecewise continuous and of bounded variation in every finite subinterval in (0, ∞), and

$\int _{0}^{\infty }|f(r)|\,r^{\frac {1}{2}}\,\mathrm {d} r<\infty .$

However, like the Fourier transform, the domain can be extended by a density argument to include some functions whose above integral is not finite, for example $f(r)=(1+r)^{-3/2}$ .

### Alternative definition

An alternative definition says that the Hankel transform of *g*(*r*) is

$h_{\nu }(k)=\int _{0}^{\infty }g(r)J_{\nu }(kr)\,{\sqrt {kr}}\,\mathrm {d} r.$

The two definitions are related:

If

$g(r)=f(r){\sqrt {r}}$

, then

$h_{\nu }(k)=F_{\nu }(k){\sqrt {k}}.$

This means that, as with the previous definition, the Hankel transform defined this way is also its own inverse:

$g(r)=\int _{0}^{\infty }h_{\nu }(k)J_{\nu }(kr)\,{\sqrt {kr}}\,\mathrm {d} k.$

The obvious domain now has the condition

$\int _{0}^{\infty }|g(r)|\,\mathrm {d} r<\infty ,$

but this can be extended. According to the reference given above, we can take the integral as the limit as the upper limit goes to infinity (an improper integral rather than a Lebesgue integral), and in this way the Hankel transform and its inverse work for all functions in L2(0, ∞).

## Transforming Laplace's equation

The Hankel transform can be used to transform and solve Laplace's equation expressed in cylindrical coordinates. Under the Hankel transform, the Bessel operator becomes a multiplication by $-k^{2}$ . In the axisymmetric case, the partial differential equation is transformed as

${\mathcal {H}}_{0}\left\{{\frac {\partial ^{2}u}{\partial r^{2}}}+{\frac {1}{r}}{\frac {\partial u}{\partial r}}+{\frac {\partial ^{2}u}{\partial z^{2}}}\right\}=-k^{2}U+{\frac {\partial ^{2}}{\partial z^{2}}}U,$

where $U={\mathcal {H}}_{0}u$ . Therefore, the Laplacian in cylindrical coordinates becomes an ordinary differential equation in the transformed function U .

## Orthogonality

The Bessel functions form an orthogonal basis with respect to the weighting factor *r*:

$\int _{0}^{\infty }J_{\nu }(kr)J_{\nu }(k'r)\,r\,\mathrm {d} r={\frac {\delta (k-k')}{k}},\quad k,k'>0.$

## The Plancherel theorem and Parseval's theorem

If *f*(*r*) and *g*(*r*) are such that their Hankel transforms *Fν*(*k*) and *Gν*(*k*) are well defined, then the Plancherel theorem states

$\int _{0}^{\infty }f(r)g(r)\,r\,\mathrm {d} r=\int _{0}^{\infty }F_{\nu }(k)G_{\nu }(k)\,k\,\mathrm {d} k.$

Parseval's theorem, which states

$\int _{0}^{\infty }|f(r)|^{2}\,r\,\mathrm {d} r=\int _{0}^{\infty }|F_{\nu }(k)|^{2}\,k\,\mathrm {d} k,$

is a special case of the Plancherel theorem. These theorems can be proven using the orthogonality property.

## Relation to the multidimensional Fourier transform

The Hankel transform appears when one writes the multidimensional Fourier transform in hyperspherical coordinates, which is the reason why the Hankel transform often appears in physical problems with cylindrical or spherical symmetry.

Consider a function $f(\mathbf {r} )$ of a ${\textstyle d}$ -dimensional vector **r**. Its ${\textstyle d}$ -dimensional Fourier transform is defined as $F(\mathbf {k} )=\int _{\mathbb {R} ^{d}}f(\mathbf {r} )e^{-i\mathbf {k} \cdot \mathbf {r} }\,\mathrm {d} \mathbf {r} .$ To rewrite it in hyperspherical coordinates, we can use the decomposition of a plane wave into ${\textstyle d}$ -dimensional hyperspherical harmonics $Y_{l,m}$ : $e^{-i\mathbf {k} \cdot \mathbf {r} }=(2\pi )^{d/2}(kr)^{1-d/2}\sum _{l=0}^{+\infty }(-i)^{l}J_{d/2-1+l}(kr)\sum _{m}Y_{l,m}(\Omega _{\mathbf {k} })Y_{l,m}^{*}(\Omega _{\mathbf {r} }),$ where ${\textstyle \Omega _{\mathbf {r} }}$ and ${\textstyle \Omega _{\mathbf {k} }}$ are the sets of all hyperspherical angles in the $\mathbf {r}$ -space and $\mathbf {k}$ -space. This gives the following expression for the ${\textstyle d}$ -dimensional Fourier transform in hyperspherical coordinates: $F(\mathbf {k} )=(2\pi )^{d/2}k^{1-d/2}\sum _{l=0}^{+\infty }(-i)^{l}\sum _{m}Y_{l,m}(\Omega _{\mathbf {k} })\int _{0}^{+\infty }J_{d/2-1+l}(kr)r^{d/2}\mathrm {d} r\int f(\mathbf {r} )Y_{l,m}^{*}(\Omega _{\mathbf {r} })\mathrm {d} \Omega _{\mathbf {r} }.$ If we expand $f(\mathbf {r} )$ and $F(\mathbf {k} )$ in hyperspherical harmonics: $f(\mathbf {r} )=\sum _{l=0}^{+\infty }\sum _{m}f_{l,m}(r)Y_{l,m}(\Omega _{\mathbf {r} }),\quad F(\mathbf {k} )=\sum _{l=0}^{+\infty }\sum _{m}F_{l,m}(k)Y_{l,m}(\Omega _{\mathbf {k} }),$ the Fourier transform in hyperspherical coordinates simplifies to $k^{d/2-1}F_{l,m}(k)=(2\pi )^{d/2}(-i)^{l}\int _{0}^{+\infty }r^{d/2-1}f_{l,m}(r)J_{d/2-1+l}(kr)r\mathrm {d} r.$ This means that functions with angular dependence in form of a hyperspherical harmonic retain it upon the multidimensional Fourier transform, while the radial part undergoes the Hankel transform (up to some extra factors like ${\textstyle r^{d/2-1}}$ ).

### Special cases

#### Fourier transform in two dimensions

If a two-dimensional function *f*(**r**) is expanded in a multipole series,

$f(r,\theta )=\sum _{m=-\infty }^{\infty }f_{m}(r)e^{im\theta _{\mathbf {r} }},$

then its two-dimensional Fourier transform is given by $F(\mathbf {k} )=2\pi \sum _{m}i^{-m}e^{im\theta _{\mathbf {k} }}F_{m}(k),$ where $F_{m}(k)=\int _{0}^{\infty }f_{m}(r)J_{m}(kr)\,r\,\mathrm {d} r$ is the ${\textstyle m}$ -th order Hankel transform of $f_{m}(r)$ (in this case ${\textstyle m}$ plays the role of the angular momentum, which was denoted by ${\textstyle l}$ in the previous section).

#### Fourier transform in three dimensions

If a three-dimensional function *f*(**r**) is expanded in a multipole series over spherical harmonics,

$f(r,\theta _{\mathbf {r} },\varphi _{\mathbf {r} })=\sum _{l=0}^{+\infty }\sum _{m=-l}^{+l}f_{l,m}(r)Y_{l,m}(\theta _{\mathbf {r} },\varphi _{\mathbf {r} }),$

then its three-dimensional Fourier transform is given by $F(k,\theta _{\mathbf {k} },\varphi _{\mathbf {k} })=(2\pi )^{3/2}\sum _{l=0}^{+\infty }(-i)^{l}\sum _{m=-l}^{+l}F_{l,m}(k)Y_{l,m}(\theta _{\mathbf {k} },\varphi _{\mathbf {k} }),$ where ${\sqrt {k}}F_{l,m}(k)=\int _{0}^{+\infty }{\sqrt {r}}f_{l,m}(r)J_{l+1/2}(kr)r\mathrm {d} r.$ is the Hankel transform of ${\sqrt {r}}f_{l,m}(r)$ of order ${\textstyle (l+1/2)}$ .

This kind of Hankel transform of half-integer order is also known as the spherical Bessel transform.

#### Fourier transform in *d* dimensions (radially symmetric case)

If a *d*-dimensional function *f*(*r*) does not depend on angular coordinates, then its *d*-dimensional Fourier transform *F*(*k*) also does not depend on angular coordinates and is given by $k^{d/2-1}F(k)=(2\pi )^{d/2}\int _{0}^{+\infty }r^{d/2-1}f(r)J_{d/2-1}(kr)r\mathrm {d} r.$ which is the Hankel transform of $r^{d/2-1}f(r)$ of order ${\textstyle (d/2-1)}$ up to a factor of $(2\pi )^{d/2}$ .

#### 2D functions inside a limited radius

If a two-dimensional function *f*(**r**) is expanded in a multipole series and the expansion coefficients *fm* are sufficiently smooth near the origin and zero outside a radius R, the radial part *f*(*r*)/*rm* may be expanded into a power series of 1 − (*r*/*R*)^2:

$f_{m}(r)=r^{m}\sum _{t\geq 0}f_{m,t}\left(1-\left({\tfrac {r}{R}}\right)^{2}\right)^{t},\quad 0\leq r\leq R,$

such that the two-dimensional Fourier transform of *f*(**r**) becomes

${\begin{aligned}F(\mathbf {k} )&=2\pi \sum _{m}i^{-m}e^{im\theta _{k}}\sum _{t}f_{m,t}\int _{0}^{R}r^{m}\left(1-\left({\tfrac {r}{R}}\right)^{2}\right)^{t}J_{m}(kr)r\,\mathrm {d} r&&\\&=2\pi \sum _{m}i^{-m}e^{im\theta _{k}}R^{m+2}\sum _{t}f_{m,t}\int _{0}^{1}x^{m+1}(1-x^{2})^{t}J_{m}(kxR)\,\mathrm {d} x&&(x={\tfrac {r}{R}})\\&=2\pi \sum _{m}i^{-m}e^{im\theta _{k}}R^{m+2}\sum _{t}f_{m,t}{\frac {t!2^{t}}{(kR)^{1+t}}}J_{m+t+1}(kR),\end{aligned}}$

where the last equality follows from §6.567.1 of. The expansion coefficients *fm,t* are accessible with discrete Fourier transform techniques: if the radial distance is scaled with

$r/R\equiv \sin \theta ,\quad 1-(r/R)^{2}=\cos ^{2}\theta ,$

the Fourier-Chebyshev series coefficients *g* emerge as

$f(r)\equiv r^{m}\sum _{j}g_{m,j}\cos(j\theta )=r^{m}\sum _{j}g_{m,j}T_{j}(\cos \theta ).$

Using the re-expansion

$\cos(j\theta )=2^{j-1}\cos ^{j}\theta -{\frac {j}{1}}2^{j-3}\cos ^{j-2}\theta +{\frac {j}{2}}{\binom {j-3}{1}}2^{j-5}\cos ^{j-4}\theta -{\frac {j}{3}}{\binom {j-4}{2}}2^{j-7}\cos ^{j-6}\theta +\cdots$

yields *f**m,t* expressed as sums of *g**m,j*.

This is one flavor of fast Hankel transform techniques.

## Relation to the Fourier and Abel transforms

The Hankel transform is one member of the FHA cycle of integral operators. In two dimensions, if we define A as the Abel transform operator, F as the Fourier transform operator, and H as the zeroth-order Hankel transform operator, then the special case of the projection-slice theorem for circularly symmetric functions states that

$FA=H.$

In other words, applying the Abel transform to a 1-dimensional function and then applying the Fourier transform to that result is the same as applying the Hankel transform to that function. This concept can be extended to higher dimensions.

## Numerical evaluation

A simple and efficient approach to the numerical evaluation of the Hankel transform is based on the observation that it can be cast in the form of a convolution by a logarithmic change of variables $r=r_{0}e^{-\rho },\quad k=k_{0}\,e^{\kappa }.$ In these new variables, the Hankel transform reads ${\tilde {F}}_{\nu }(\kappa )=\int _{-\infty }^{\infty }{\tilde {f}}(\rho ){\tilde {J}}_{\nu }(\kappa -\rho )\,\mathrm {d} \rho ,$ where ${\tilde {f}}(\rho )=\left(r_{0}\,e^{-\rho }\right)^{1-n}\,f(r_{0}e^{-\rho }),$ ${\tilde {F}}_{\nu }(\kappa )=\left(k_{0}\,e^{\kappa }\right)^{1+n}\,F_{\nu }(k_{0}e^{\kappa }),$ ${\tilde {J}}_{\nu }(\kappa -\rho )=\left(k_{0}\,r_{0}\,e^{\kappa -\rho }\right)^{1+n}\,J_{\nu }(k_{0}r_{0}e^{\kappa -\rho }).$

Now the integral can be calculated numerically with ${\textstyle O(N\log N)}$ complexity using fast Fourier transform. The algorithm can be further simplified by using a known analytical expression for the Fourier transform of ${\tilde {J}}_{\nu }$ : $\int _{-\infty }^{+\infty }{\tilde {J}}_{\nu }(x)e^{-iqx}\,\mathrm {d} x={\frac {\Gamma \left({\frac {\nu +1+n-iq}{2}}\right)}{\Gamma \left({\frac {\nu +1-n+iq}{2}}\right)}}\,2^{n-iq}e^{iq\ln(k_{0}r_{0})}.$ The optimal choice of parameters $r_{0},k_{0},n$ depends on the properties of $f(r),$ in particular its asymptotic behavior at $r\to 0$ and $r\to \infty .$

This algorithm is known as the "quasi-fast Hankel transform", or simply "fast Hankel transform".

Since it is based on fast Fourier transform in logarithmic variables, $f(r)$ has to be defined on a logarithmic grid. For functions defined on a uniform grid, a number of other algorithms exist, including straightforward quadrature, methods based on the projection-slice theorem, and methods using the asymptotic expansion of Bessel functions.

## Some Hankel transform pairs

| $f(r)$ | $F_{0}(k)$ |
|---|---|
| 1 | ${\frac {\delta (k)}{k}}$ |
| ${\frac {1}{r}}$ | ${\frac {1}{k}}$ |
| r | $-{\frac {1}{k^{3}}}$ |
| $r^{3}$ | ${\frac {9}{k^{5}}}$ |
| $r^{m}$ | ${\frac {\,2^{m+1}\,\Gamma \left({\tfrac {m}{2}}+1\right)\,}{k^{m+2}\,\Gamma \left(-{\tfrac {m}{2}}\right)}},\quad -2<{\mathcal {R_{e}}}\{m\}<-{\tfrac {1}{2}}$ |
| ${\frac {1}{\sqrt {r^{2}+z^{2}\,}}}$ | ${\frac {\,e^{-k\|z\|}\,}{k}}$ |
| ${\frac {1}{\,z^{2}+r^{2}\,}}$ | $K_{0}(kz),\quad z\in \mathbb {C}$ |
| ${\frac {e^{iar}}{r}}$ | ${\frac {i}{\,{\sqrt {a^{2}-k^{2}\,}}\,}},\quad a>0,\;k<a$ |
| ${\frac {1}{\,{\sqrt {k^{2}-a^{2}\,}}\,}},\quad a>0,\;k>a$ |   |
| $e^{-{\frac {1}{2}}a^{2}r^{2}}$ | ${\frac {1}{\,a^{2}\,}}\,e^{-{\tfrac {k^{2}}{2\,a^{2}}}}$ |
| ${\frac {1}{r}}J_{0}(lr)\,e^{-sr}$ | ${\frac {2}{\,\pi {\sqrt {(k+l)^{2}+s^{2}\,}}\,}}K\left({\sqrt {{\frac {4kl}{(k+l)^{2}+s^{2}}}\,}}\right)$ |
| $-r^{2}f(r)$ | ${\frac {\,\mathrm {d} ^{2}F_{0}\,}{\mathrm {d} k^{2}}}+{\frac {1}{k}}{\frac {\,\mathrm {d} F_{0}\,}{\mathrm {d} k}}$ |

| $f(r)$ | $F_{\nu }(k)$ |
|---|---|
| $r^{s}$ | ${\frac {2^{s+1}}{\,k^{s+2}\,}}\,{\frac {\Gamma \left({\tfrac {1}{2}}(2+\nu +s)\right)}{\Gamma ({\tfrac {1}{2}}(\nu -s))}}$ |
| $r^{\nu -2s}\Gamma (s,r^{2}h)$ | ${\tfrac {1}{2}}\left({\tfrac {k}{2}}\right)^{2s-\nu -2}\gamma \left(1-s+\nu ,{\tfrac {k^{2}}{4h}}\right)$ |
| $e^{-r^{2}}r^{\nu }\,U(a,b,r^{2})$ | ${\frac {\Gamma (2+\nu -b)}{\,2\,\Gamma (2+\nu -b+a)}}\left({\tfrac {k}{2}}\right)^{\nu }\,e^{-{\frac {k^{2}}{4}}\,}\,_{1}F_{1}\left(a,2+a-b+\nu ,{\tfrac {k^{2}}{4}}\right)$ |
| $r^{n}J_{\mu }(lr)\,e^{-sr}$ | Expressable in terms of elliptic integrals. |
| $-r^{2}f(r)$ | ${\frac {\mathrm {d} ^{2}F_{\nu }}{\mathrm {d} k^{2}}}+{\frac {1}{k}}{\frac {\,\mathrm {d} F_{\nu }\,}{\mathrm {d} k}}-{\frac {\nu ^{2}}{k^{2}}}\,F_{\nu }$ |

*Kn*(*z*) is a modified Bessel function of the second kind. *K*(*z*) is the complete elliptic integral of the first kind.

The expression

${\frac {\,\mathrm {d} ^{2}F_{0}\,}{\mathrm {d} k^{2}}}+{\frac {1}{k}}{\frac {\,\mathrm {d} F_{0}\,}{\mathrm {d} k}}$

coincides with the expression for the Laplace operator in polar coordinates ( *k*, *θ* ) applied to a spherically symmetric function *F*0(*k*) .

The Hankel transform of Zernike polynomials are essentially Bessel Functions (Noll 1976):

$R_{n}^{m}(r)=(-1)^{\frac {n-m}{2}}\int _{0}^{\infty }J_{n+1}(k)J_{m}(kr)\,\mathrm {d} k$

for even *n* − *m* ≥ 0.

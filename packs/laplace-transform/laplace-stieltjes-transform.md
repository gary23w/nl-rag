---
title: "Laplace–Stieltjes transform"
source: https://en.wikipedia.org/wiki/Laplace%E2%80%93Stieltjes_transform
domain: laplace-transform
license: CC-BY-SA-4.0
tags: laplace transform, inverse laplace transform, transfer function, final value theorem
fetched: 2026-07-02
---

# Laplace–Stieltjes transform

The **Laplace–Stieltjes transform**, named for Pierre-Simon Laplace and Thomas Joannes Stieltjes, is an integral transform similar to the Laplace transform. For real-valued functions, it is the Laplace transform of a Stieltjes measure, however it is often defined for functions with values in a Banach space. It is useful in a number of areas of mathematics, including functional analysis, and certain areas of theoretical and applied probability.

## Real-valued functions

The Laplace–Stieltjes transform of a real-valued function *g* is given by a Lebesgue–Stieltjes integral of the form

$\int e^{-sx}\,dg(x)$

for *s* a complex number. As with the usual Laplace transform, one gets a slightly different transform depending on the domain of integration, and for the integral to be defined, one also needs to require that *g* be of bounded variation on the region of integration. The most common are:

- The bilateral (or two-sided) Laplace–Stieltjes transform is given by $\{{\mathcal {L}}^{*}g\}(s)=\int _{-\infty }^{\infty }e^{-sx}\,dg(x).$
- The unilateral (one-sided) Laplace–Stieltjes transform is given by $\{{\mathcal {L}}^{*}g\}(s)=\lim _{\varepsilon \to 0^{+}}\int _{-\varepsilon }^{\infty }e^{-sx}\,dg(x).$ The limit is necessary to ensure the transform captures a possible jump in *g*(*x*) at *x* = 0, as is needed to make sense of the Laplace transform of the Dirac delta function.
- More general transforms can be considered by integrating over a contour in the complex plane; see Zhavrid 2001.

The Laplace–Stieltjes transform in the case of a scalar-valued function is thus seen to be a special case of the Laplace transform of a Stieltjes measure. To wit,

${\mathcal {L}}^{*}g={\mathcal {L}}(dg).$

In particular, it shares many properties with the usual Laplace transform. For instance, the convolution theorem holds:

$\{{\mathcal {L}}^{*}(g*h)\}(s)=\{{\mathcal {L}}^{*}g\}(s)\{{\mathcal {L}}^{*}h\}(s).$

Often only real values of the variable *s* are considered, although if the integral exists as a proper Lebesgue integral for a given real value *s* = σ, then it also exists for all complex *s* with re(*s*) ≥ σ.

The Laplace–Stieltjes transform appears naturally in the following context. If *X* is a random variable with cumulative distribution function *F*, then the Laplace–Stieltjes transform is given by the expectation:

$\{{\mathcal {L}}^{*}F\}(s)=\mathrm {E} \left[e^{-sX}\right].$

The Laplace-Stieltjes transform of a real random variable's cumulative distribution function is therefore equal to the random variable's moment-generating function, but with the sign of the argument reversed.

## Vector measures

Whereas the Laplace–Stieltjes transform of a real-valued function is a special case of the Laplace transform of a measure applied to the associated Stieltjes measure, the conventional Laplace transform cannot handle vector measures: measures with values in a Banach space. These are, however, important in connection with the study of semigroups that arise in partial differential equations, harmonic analysis, and probability theory. The most important semigroups are, respectively, the heat semigroup, Riemann-Liouville semigroup, and Brownian motion and other infinitely divisible processes.

Let *g* be a function from [0,∞) to a Banach space *X* of **strongly bounded variation** over every finite interval. This means that, for every fixed subinterval [0,*T*] one has

$\sup \sum _{i}\left\|g(t_{i})-g(t_{i+1})\right\|_{X}<\infty$

where the supremum is taken over all partitions of [0,*T*]

$0=t_{0}<t_{1}<\cdots <t_{n}=T.$

The Stieltjes integral with respect to the vector measure *dg*

$\int _{0}^{T}e^{-st}dg(t)$

is defined as a Riemann–Stieltjes integral. Indeed, if π is the tagged partition of the interval [0,*T*] with subdivision 0 = *t*0 ≤ *t*1 ≤ ... ≤ *t**n* = *T*, distinguished points $\tau _{i}\in [t_{i},t_{i+1}]$ and mesh size $|\pi |=\max \left|t_{i}-t_{i+1}\right|,$ the Riemann–Stieltjes integral is defined as the value of the limit

$\lim _{|\pi |\to 0}\sum _{i=0}^{n-1}e^{-s\tau _{i}}\left[g(t_{i+1})-g(t_{i})\right]$

taken in the topology on *X*. The hypothesis of strong bounded variation guarantees convergence.

If in the topology of *X* the limit

$\lim _{T\to \infty }\int _{0}^{T}e^{-st}dg(t)$

exists, then the value of this limit is the Laplace–Stieltjes transform of *g*.

The Laplace–Stieltjes transform is closely related to other integral transforms, including the Fourier transform and the Laplace transform. In particular, note the following:

- If *g* has derivative *g'* then the Laplace–Stieltjes transform of *g* is the Laplace transform of *g′*. $\{{\mathcal {L}}^{*}g\}(s)=\{{\mathcal {L}}g'\}(s),$
- We can obtain the **Fourier–Stieltjes transform** of *g* (and, by the above note, the Fourier transform of *g′*) by $\{{\mathcal {F}}^{*}g\}(s)=\{{\mathcal {L}}^{*}g\}(is),\qquad s\in \mathbb {R} .$

## Probability distributions

If *X* is a continuous random variable with cumulative distribution function *F*(*t*) then moments of *X* can be computed using

$\operatorname {E} [X^{n}]=(-1)^{n}\left.{\frac {d^{n}\{{\mathcal {L}}^{*}F\}(s)}{ds^{n}}}\right|_{s=0}.$

### Exponential distribution

For an exponentially distributed random variable *Y* with rate parameter *λ* the LST is,

${\widetilde {Y}}(s)=\{{\mathcal {L}}^{*}F_{Y}\}(s)=\int _{0}^{\infty }e^{-st}\lambda e^{-\lambda t}dt={\frac {\lambda }{\lambda +s}}$

from which the first three moments can be computed as 1/*λ*, 2/*λ*2 and 6/*λ*3.

### Erlang distribution

For *Z* with Erlang distribution (which is the sum of *n* exponential distributions) we use the fact that the probability distribution of the sum of independent random variables is equal to the convolution of their probability distributions. So if

$Z=Y_{1}+\cdots +Y_{n}$

with the *Yi* independent then

${\widetilde {Z}}(s)={\widetilde {Y}}_{1}(s)\cdots {\widetilde {Y}}_{n}(s)$

therefore in the case where *Z* has an Erlang distribution,

${\widetilde {Z}}(s)=\left({\frac {\lambda }{\lambda +s}}\right)^{n}.$

### Uniform distribution

For *U* with uniform distribution on the interval (*a*,*b*), the transform is given by

${\widetilde {U}}(s)=\int _{a}^{b}e^{-st}{\frac {1}{b-a}}dt={\frac {e^{-sa}-e^{-sb}}{s(b-a)}}.$

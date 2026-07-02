---
title: "Hartley transform"
source: https://en.wikipedia.org/wiki/Hartley_transform
domain: integral-transforms
license: CC-BY-SA-4.0
tags: integral transform, hilbert transform, hartley transform, convolution theorem
fetched: 2026-07-02
---

# Hartley transform

In mathematics, the **Hartley transform** (**HT**) is an integral transform closely related to the Fourier transform (FT), but which transforms real-valued functions to real-valued functions. It was proposed as an alternative to the Fourier transform by Ralph V. L. Hartley in 1942, and is one of many known Fourier-related transforms. Compared to the Fourier transform, the Hartley transform has the advantages of transforming real functions to real functions (as opposed to requiring complex numbers) and of being its own inverse.

The discrete version of the transform, the discrete Hartley transform (DHT), was introduced by Ronald N. Bracewell in 1983.

The two-dimensional Hartley transform can be computed by an analog optical process similar to an optical Fourier transform (OFT), with the proposed advantage that only its amplitude and sign need to be determined rather than its complex phase. However, optical Hartley transforms do not seem to have seen widespread use.

## Definition

The Hartley transform of a function $f(t)$ is defined by:

$H(\omega )=\left\{{\mathcal {H}}f\right\}(\omega )={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }f(t)\operatorname {cas} (\omega t)\,\mathrm {d} t\,,$

where $\omega$ can in applications be an angular frequency and

$\operatorname {cas} (t)=\cos(t)+\sin(t)={\sqrt {2}}\sin(t+\pi /4)={\sqrt {2}}\cos(t-\pi /4)\,,$

is the cosine-and-sine (cas) or *Hartley* kernel. In engineering terms, this transform takes a signal (function) from the time-domain to the Hartley spectral domain (frequency domain).

### Inverse transform

The Hartley transform has the convenient property of being its own inverse (an involution):

$f=\{{\mathcal {H}}\{{\mathcal {H}}f\}\}\,.$

### Conventions

The above is in accord with Hartley's original definition, but (as with the Fourier transform) various minor details are matters of convention and can be changed without altering the essential properties:

- Instead of using the same transform for forward and inverse, one can remove the ${1}/{\sqrt {2\pi }}$ from the forward transform and use ${1}/{2\pi }$ for the inverse—or, indeed, any pair of normalizations whose product is ${1}/{2\pi }$ . (Such asymmetrical normalizations are sometimes found in both purely mathematical and engineering contexts.)
- One can also use $2\pi \nu t$ instead of $\omega t$ (i.e., frequency instead of angular frequency), in which case the ${1}/{\sqrt {2\pi }}$ coefficient is omitted entirely.
- One can use $\cos -\sin$ instead of $\cos +\sin$ as the kernel.

## Relation to Fourier transform

This transform differs from the classic Fourier transform $\ F(\omega )\equiv {\mathcal {F}}\ {\bigl \{}\ f(t)\ {\bigr \}}(\omega )\$ in the choice of the kernel; in the classic Fourier transform, we have the exponential kernel, $\ \exp \left({-\mathrm {i} \ \omega t}\right)=\cos(\omega t)-\mathrm {i} \ \sin(\omega t)\ ,$ where $\ \mathrm {i} \$ is the imaginary unit.

However, the two transforms are closely related and – assuming both use the same $\ {\tfrac {1}{\ {\sqrt {2\pi \ }}\ }}\$ normalization convention – the Fourier transform can be computed from the Hartley transform via:

$F(\omega )={\tfrac {1}{2}}{\bigl [}\ H(\omega )+H(-\omega )\ {\bigr ]}-\mathrm {i} \ {\tfrac {1}{2}}{\bigl [}\ H(\omega )-H(-\omega )\ {\bigr ]}~.$

That is, the real and imaginary parts of the Fourier transform are simply given by the even and odd parts of the Hartley transform, respectively.

Conversely, for real-valued functions $\ f(t)\ ,$ the Hartley transform is given from the Fourier transform's real and imaginary parts:

$\operatorname {\mathcal {H}} {\bigl \{}\ f\ {\bigr \}}=\operatorname {\mathcal {R_{e}}} {\bigl \{}\ {\mathcal {F}}\ f\ {\bigr \}}\ -\ \operatorname {\mathcal {I_{m}}} {\bigl \{}\ {\mathcal {F}}\ f\ {\bigr \}}={\mathcal {R_{e}}}{\Bigl \{}\ \operatorname {\mathcal {F}} \ {\bigl [}f\cdot \left(1+\mathrm {i} \right){\bigr ]}\ {\Bigr \}}\ ,$

where $\ {\mathcal {R_{e}}}\$ and $\ {\mathcal {I_{m}}}\$ denote the real and imaginary parts.

## Properties

The Hartley transform is a real linear operator, and is symmetric (and Hermitian). From the symmetric and self-inverse properties, it follows that the transform is a unitary operator (indeed, orthogonal).

Convolution using Hartley transforms is $f(x)*g(x)={\frac {F(\omega )G(\omega )+F(-\omega )G(\omega )+F(\omega )G(-\omega )-F(-\omega )G(-\omega )}{2}}$ where $F(\omega )=\{{\mathcal {H}}f\}(\omega )$ and $G(\omega )=\{{\mathcal {H}}g\}(\omega )$

Similar to the Fourier transform, the Hartley transform of an even/odd function is even/odd, respectively.

### cas

The properties of the *Hartley kernel*, for which Hartley introduced the name *cas* for the function (from *cosine and sine*) in 1942, follow directly from trigonometry, and its definition as a phase-shifted trigonometric function $\operatorname {cas} (t)={\sqrt {2}}\sin(t+\pi /4)=\sin(t)+\cos(t)$ . For example, it has an angle-addition identity of:

$2\operatorname {cas} (a+b)=\operatorname {cas} (a)\operatorname {cas} (b)+\operatorname {cas} (-a)\operatorname {cas} (b)+\operatorname {cas} (a)\operatorname {cas} (-b)-\operatorname {cas} (-a)\operatorname {cas} (-b)\,.$

Additionally:

$\operatorname {cas} (a+b)={\cos(a)\operatorname {cas} (b)}+{\sin(a)\operatorname {cas} (-b)}=\cos(b)\operatorname {cas} (a)+\sin(b)\operatorname {cas} (-a)\,,$

and its derivative is given by:

$\operatorname {cas} '(a)={\frac {d}{da}}\operatorname {cas} (a)=\cos(a)-\sin(a)=\operatorname {cas} (-a)\,.$

---
title: "Integral transform"
source: https://en.wikipedia.org/wiki/Integral_transform
domain: integral-transforms
license: CC-BY-SA-4.0
tags: integral transform, hilbert transform, hartley transform, convolution theorem
fetched: 2026-07-02
---

# Integral transform

In mathematics, an **integral transform** is a type of transformation that maps a function from its original function space into another function space via integration, where some of the properties of the original function might be more easily characterized and manipulated than in the original function space. The transformed function can generally be mapped back to the original function space using the *inverse transform*.

## General form

An integral transform is any transform *T* of the following form:

$(Tf)(u)=\int _{t_{1}}^{t_{2}}f(t)\,K(t,u)\,dt$

The input of this transform is a function *f*, and the output is another function *$Tf$*. An integral transform is a particular kind of mathematical operator.

There are numerous useful integral transforms. Each is specified by a choice of the function K of two variables, that is called the **kernel** or **nucleus** of the transform.

Some kernels have an associated *inverse kernel* $K^{-1}(u,t)$ which (roughly speaking) yields an inverse transform:

$f(t)=\int _{u_{1}}^{u_{2}}(Tf)(u)\,K^{-1}(u,t)\,du$

A *symmetric kernel* is one that is unchanged when the two variables are permuted; it is a kernel function *K* such that $K(t,u)=K(u,t)$ . In the theory of integral equations, symmetric kernels correspond to self-adjoint operators.

## Motivation

There are many classes of problems that are difficult to solve—or at least quite unwieldy algebraically—in their original representations. An integral transform "maps" an equation from its original "domain" into another domain, in which manipulating and solving the equation may be much easier than in the original domain. The solution can then be mapped back to the original domain with the inverse of the integral transform.

There are many applications of probability that rely on integral transforms, such as "pricing kernel" or stochastic discount factor, or the smoothing of data recovered from robust statistics; see kernel (statistics).

## History

The precursor of the transforms were the Fourier series to express functions in finite intervals. Later the Fourier transform was developed to remove the requirement of finite intervals.

Using the Fourier series, just about any practical function of time (the voltage across the terminals of an electronic device for example) can be represented as a sum of sines and cosines, each suitably scaled (multiplied by a constant factor), shifted (advanced or retarded in time) and "squeezed" or "stretched" (increasing or decreasing the frequency). The sines and cosines in the Fourier series are an example of an orthonormal basis.

## Usage example

As an example of an application of integral transforms, consider the Laplace transform. This is a technique that maps differential or integro-differential equations in the "time" domain into polynomial equations in what is termed the "complex frequency" domain. (Complex frequency is similar to actual, physical frequency but rather more general. Specifically, the imaginary component *ω* of the complex frequency *s* = −*σ* + *iω* corresponds to the usual concept of frequency, *viz.*, the rate at which a sinusoid cycles, whereas the real component *σ* of the complex frequency corresponds to the degree of "damping", i.e. an exponential decrease of the amplitude.) The equation cast in terms of complex frequency is readily solved in the complex frequency domain (roots of the polynomial equations in the complex frequency domain correspond to eigenvalues in the time domain), leading to a "solution" formulated in the frequency domain. Employing the inverse transform, *i.e.*, the inverse procedure of the original Laplace transform, one obtains a time-domain solution. In this example, polynomials in the complex frequency domain (typically occurring in the denominator) correspond to power series in the time domain, while axial shifts in the complex frequency domain correspond to damping by decaying exponentials in the time domain.

The Laplace transform finds wide application in physics and particularly in electrical engineering, where the characteristic equations that describe the behavior of an electric circuit in the complex frequency domain correspond to linear combinations of exponentially scaled and time-shifted damped sinusoids in the time domain. Other integral transforms find special applicability within other scientific and mathematical disciplines.

Another usage example is the kernel in the path integral:

$\psi (x,t)=\int _{-\infty }^{\infty }\psi (x',t')K(x,t;x',t')dx'.$

This states that the total amplitude $\psi (x,t)$ to arrive at $(x,t)$ is the sum (the integral) over all possible values $x'$ of the total amplitude $\psi (x',t')$ to arrive at the point $(x',t')$ multiplied by the amplitude to go from $x'$ to x [i.e. $K(x,t;x',t')$ ]. It is often referred to as the propagator for a given system. This (physics) kernel is the kernel of the integral transform. However, for each quantum system, there is a different kernel.

## Table of transforms

Table of integral transforms

Transform

Symbol

K

f

(

t

)

t

1

t

2

K

−1

u

1

u

2

Abel transform

F, f

${\frac {2t}{\sqrt {t^{2}-u^{2}}}}$

u

$\infty$

${\frac {-1}{\pi {\sqrt {u^{2}\!-\!t^{2}}}}}{\frac {d}{du}}$

t

$\infty$

Associated Legendre transform

${\mathcal {J}}_{n,m}$

$(1-x^{2})^{-m/2}P_{n}^{m}(x)$

$-1$

1

0

$\infty$

Fourier transform

${\mathcal {F}}$

$e^{-2\pi iut}$

$L_{1}$

$-\infty$

$\infty$

$e^{2\pi iut}$

$-\infty$

$\infty$

Fourier sine transform

${\mathcal {F}}_{s}$

${\sqrt {\frac {2}{\pi }}}\sin(ut)$

on

$[0,\infty )$

, real-valued

0

$\infty$

${\sqrt {\frac {2}{\pi }}}\sin(ut)$

0

$\infty$

Fourier cosine transform

${\mathcal {F}}_{c}$

${\sqrt {\frac {2}{\pi }}}\cos(ut)$

on

$[0,\infty )$

, real-valued

0

$\infty$

${\sqrt {\frac {2}{\pi }}}\cos(ut)$

0

$\infty$

Hankel transform

$t\,J_{\nu }(ut)$

0

$\infty$

$u\,J_{\nu }(ut)$

0

$\infty$

Hartley transform

${\mathcal {H}}$

${\frac {\cos(ut)+\sin(ut)}{\sqrt {2\pi }}}$

$-\infty$

$\infty$

${\frac {\cos(ut)+\sin(ut)}{\sqrt {2\pi }}}$

$-\infty$

$\infty$

Hermite transform

H

$e^{-x^{2}}H_{n}(x)$

$-\infty$

$\infty$

0

$\infty$

Hilbert transform

${\mathcal {H}}il$

${\frac {1}{\pi }}{\frac {1}{u-t}}$

$-\infty$

$\infty$

${\frac {1}{\pi }}{\frac {1}{u-t}}$

$-\infty$

$\infty$

Jacobi transform

J

$(1-x)^{\alpha }\ (1+x)^{\beta }\ P_{n}^{\alpha ,\beta }(x)$

$-1$

1

0

$\infty$

Laguerre transform

L

$e^{-x}\ x^{\alpha }\ L_{n}^{\alpha }(x)$

0

$\infty$

0

$\infty$

Laplace transform

${\mathcal {L}}$

$e^{-ut}$

0

$\infty$

${\frac {e^{ut}}{2\pi i}}$

$c\!-\!i\infty$

$c\!+\!i\infty$

Legendre transform

${\mathcal {J}}$

$P_{n}(x)\,$

$-1$

1

0

$\infty$

Mellin transform

${\mathcal {M}}$

$t^{u-1}$

0

$\infty$

${\frac {t^{-u}}{2\pi i}}\,$

$c\!-\!i\infty$

$c\!+\!i\infty$

Two-sided Laplace

transform

${\mathcal {B}}$

$e^{-ut}$

$-\infty$

$\infty$

${\frac {e^{ut}}{2\pi i}}$

$c\!-\!i\infty$

$c\!+\!i\infty$

Poisson kernel

${\frac {1-r^{2}}{1-2r\cos \theta +r^{2}}}$

0

$2\pi$

Radon transform

Rƒ

$\delta (x\cos \theta +y\sin \theta -t)$

$-\infty$

$\infty$

Weierstrass transform

${\mathcal {W}}$

${\frac {e^{-{\frac {(u-t)^{2}}{4}}}}{\sqrt {4\pi }}}\,$

$-\infty$

$\infty$

${\frac {e^{\frac {(u-t)^{2}}{4}}}{i{\sqrt {4\pi }}}}$

$c\!-\!i\infty$

$c\!+\!i\infty$

X-ray transform

Xƒ

$-\infty$

$\infty$

In the limits of integration for the inverse transform, *c* is a constant which depends on the nature of the transform function. For example, for the one and two-sided Laplace transform, *c* must be greater than the largest real part of the zeroes of the transform function.

Note that there are alternative notations and conventions for the Fourier transform.

## Different domains

Here integral transforms are defined for functions on the real numbers, but they can be defined more generally for functions on a group.

- If instead one uses functions on the circle (periodic functions), integration kernels are then biperiodic functions; convolution by functions on the circle yields circular convolution.
- If one uses functions on the cyclic group of order *n* (*Cn* or **Z**/*n***Z**), one obtains *n* × *n* matrices as integration kernels; convolution corresponds to circulant matrices.

## General theory

Although the properties of integral transforms vary widely, they have some properties in common. For example, every integral transform is a linear operator, since the integral is a linear operator, and in fact if the kernel is allowed to be a generalized function then all linear operators are integral transforms (a properly formulated version of this statement is the Schwartz kernel theorem).

The general theory of such integral equations is known as Fredholm theory. In this theory, the kernel is understood to be a compact operator acting on a Banach space of functions. Depending on the situation, the kernel is then variously referred to as the Fredholm operator, the nuclear operator or the Fredholm kernel.

---
title: "Gauss–Hermite quadrature"
source: https://en.wikipedia.org/wiki/Gauss%E2%80%93Hermite_quadrature
domain: gaussian-quadrature
license: CC-BY-SA-4.0
tags: gaussian quadrature, gauss-legendre quadrature, gauss-kronrod quadrature, clenshaw-curtis quadrature
fetched: 2026-07-02
---

# Gauss–Hermite quadrature

In numerical analysis, **Gauss–Hermite quadrature** is a form of Gaussian quadrature for approximating the value of integrals of the following kind:

$\int _{-\infty }^{+\infty }e^{-x^{2}}f(x)\,dx.$

In this case

$\int _{-\infty }^{+\infty }e^{-x^{2}}f(x)\,dx\approx \sum _{i=1}^{n}w_{i}f(x_{i})$

where *n* is the number of sample points used. The *x**i* are the roots of the physicists' version of the Hermite polynomial *H**n*(*x*) (*i* = 1,2,...,*n*), and the associated weights *w**i* are given by

$w_{i}={\frac {2^{n-1}n!{\sqrt {\pi }}}{n^{2}[H_{n-1}(x_{i})]^{2}}}.$

## Example with change of variable

Consider a function *h(y)*, where the variable *y* is normally distributed: $y\sim {\mathcal {N}}(\mu ,\sigma ^{2})$ . The expectation of *h* corresponds to the following integral:

$E[h(y)]=\int _{-\infty }^{+\infty }{\frac {1}{\sigma {\sqrt {2\pi }}}}\exp \left(-{\frac {(y-\mu )^{2}}{2\sigma ^{2}}}\right)h(y)dy$

As this does not exactly correspond to the Hermite polynomial, we need to change variables:

$x={\frac {y-\mu }{{\sqrt {2}}\sigma }}\Leftrightarrow y={\sqrt {2}}\sigma x+\mu$

Coupled with the integration by substitution, we obtain:

$E[h(y)]=\int _{-\infty }^{+\infty }{\frac {1}{\sqrt {\pi }}}\exp(-x^{2})h({\sqrt {2}}\sigma x+\mu )dx$

leading to:

$E[h(y)]\approx {\frac {1}{\sqrt {\pi }}}\sum _{i=1}^{n}w_{i}h({\sqrt {2}}\sigma x_{i}+\mu )$

As an illustration, in the simplest non-trivial case, with $n=2$ , we have $x_{1}=-{\frac {1}{\sqrt {2}}},x_{2}={\frac {1}{\sqrt {2}}}$ and $w_{1}=w_{2}={\frac {\sqrt {\pi }}{2}}$ , so the estimate reduces to:

$E[h(y)]\approx {\frac {1}{2}}(h(\mu -\sigma )+h(\mu +\sigma ))$

– i.e. the average of the function's values one standard deviation below and above the mean.

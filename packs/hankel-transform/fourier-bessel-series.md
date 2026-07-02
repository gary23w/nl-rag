---
title: "Fourier–Bessel series"
source: https://en.wikipedia.org/wiki/Fourier%E2%80%93Bessel_series
domain: hankel-transform
license: CC-BY-SA-4.0
tags: hankel transform, abel transform, struve function, neumann series
fetched: 2026-07-02
---

# Fourier–Bessel series

In mathematics, **Fourier–Bessel series** is a particular kind of generalized Fourier series (an infinite series expansion on a finite interval) based on Bessel functions.

Fourier–Bessel series are used in the solution to partial differential equations, particularly in cylindrical coordinate systems.

## Definition

The Fourier–Bessel series of a function *f*(*x*) with a domain of [0, *b*] satisfying *f*(*b*) = 0

$f:[0,b]\to \mathbb {R}$ is the representation of that function as a linear combination of many orthogonal versions of the same Bessel function of the first kind *J**α*, where the argument to each version *n* is differently scaled, according to $(J_{\alpha })_{n}(x):=J_{\alpha }\left({\frac {u_{\alpha ,n}}{b}}x\right)$ where *u**α*,*n* is a root, numbered *n* associated with the Bessel function *J**α* and *c**n* are the assigned coefficients: $f(x)\sim \sum _{n=1}^{\infty }c_{n}J_{\alpha }\left({\frac {u_{\alpha ,n}}{b}}x\right).$

## Interpretation

The Fourier–Bessel series may be thought of as a Fourier expansion in the ρ coordinate of cylindrical coordinates. Just as the Fourier series is defined for a finite interval and has a counterpart, the continuous Fourier transform over an infinite interval, so the Fourier–Bessel series has a counterpart over an infinite interval, namely the Hankel transform.

## Calculating the coefficients

As said, differently scaled Bessel Functions are orthogonal with respect to the inner product

$\langle f,g\rangle =\int _{0}^{b}xf(x)g(x)\,dx$

according to

$\int _{0}^{b}xJ_{\alpha }\left({\frac {xu_{\alpha ,n}}{b}}\right)\,J_{\alpha }\left({\frac {xu_{\alpha ,m}}{b}}\right)\,dx={\frac {b^{2}}{2}}\delta _{mn}[J_{\alpha +1}(u_{\alpha ,n})]^{2},$

(where: $\delta _{mn}$ is the Kronecker delta). The coefficients can be obtained from projecting the function *f*(*x*) onto the respective Bessel functions:

$c_{n}={\frac {\langle f,(J_{\alpha })_{n}\rangle }{\langle (J_{\alpha })_{n},(J_{\alpha })_{n}\rangle }}={\frac {\int _{0}^{b}xf(x)(J_{\alpha })_{n}(x)\,dx}{{\frac {1}{2}}(bJ_{\alpha \pm 1}(u_{\alpha ,n}))^{2}}}$

where the plus or minus sign is equally valid.

For the inverse transform, one makes use of the following representation of the Dirac delta function

${\frac {2x^{\alpha }y^{1-\alpha }}{b^{2}}}\sum _{k=1}^{\infty }{\frac {J_{\alpha }\left({\frac {xu_{\alpha ,k}}{b}}\right)\,J_{\alpha }\left({\frac {yu_{\alpha ,k}}{b}}\right)}{J_{\alpha +1}^{2}(u_{\alpha ,k})}}=\delta (x-y).$

## Applications

The Fourier–Bessel series expansion employs aperiodic and decaying Bessel functions as the basis. The Fourier–Bessel series expansion has been successfully applied in diversified areas such as Gear fault diagnosis, discrimination of odorants in a turbulent ambient, postural stability analysis, detection of voice onset time, glottal closure instants (epoch) detection, separation of speech formants, speech enhancement, and speaker identification. The Fourier–Bessel series expansion has also been used to reduce cross terms in the Wigner–Ville distribution.

## Dini series

A second Fourier–Bessel series, also known as *Dini series*, is associated with the Robin boundary condition $bf'(b)+cf(b)=0,$ where c is an arbitrary constant. The Dini series can be defined by $f(x)\sim \sum _{n=1}^{\infty }b_{n}J_{\alpha }(\gamma _{n}x/b),$

where $\gamma _{n}$ is the *n*-th zero of $xJ'_{\alpha }(x)+cJ_{\alpha }(x)$ .

The coefficients $b_{n}$ are given by $b_{n}={\frac {2\gamma _{n}^{2}}{b^{2}(c^{2}+\gamma _{n}^{2}-\alpha ^{2})J_{\alpha }^{2}(\gamma _{n})}}\int _{0}^{b}J_{\alpha }(\gamma _{n}x/b)\,f(x)\,x\,dx.$

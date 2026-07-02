---
title: "Gauss–Laguerre quadrature"
source: https://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature
domain: gaussian-quadrature
license: CC-BY-SA-4.0
tags: gaussian quadrature, gauss-legendre quadrature, gauss-kronrod quadrature, clenshaw-curtis quadrature
fetched: 2026-07-02
---

# Gauss–Laguerre quadrature

In numerical analysis **Gauss–Laguerre quadrature** (named after Carl Friedrich Gauss and Edmond Laguerre) is an extension of the Gaussian quadrature method for approximating the value of integrals of the following kind:

$\int _{0}^{\infty }e^{-x}f(x)\,dx.$

In this case

$\int _{0}^{\infty }e^{-x}f(x)\,dx\approx \sum _{i=1}^{n}w_{i}f(x_{i})$

where *x**i* is the *i*-th root of Laguerre polynomial *L**n*(*x*) and the weight *w**i* is given by

$w_{i}={\frac {x_{i}}{\left(n+1\right)^{2}\left[L_{n+1}\left(x_{i}\right)\right]^{2}}}.$

The following Python code with the SymPy library will allow for calculation of the values of $x_{i}$ and $w_{i}$ to 20 digits of precision:

```mw
from sympy import *

def lag_weights_roots(n):
    x = Symbol("x")
    roots = Poly(laguerre(n, x)).all_roots()
    x_i = [rt.evalf(20) for rt in roots]
    w_i = [(rt / ((n + 1) * laguerre(n + 1, rt)) ** 2).evalf(20) for rt in roots]
    return x_i, w_i

print(lag_weights_roots(5))
```

## For more general functions

To integrate the function f we apply the following transformation

$\int _{0}^{\infty }f(x)\,dx=\int _{0}^{\infty }f(x)e^{x}e^{-x}\,dx=\int _{0}^{\infty }g(x)e^{-x}\,dx$

where $g\left(x\right):=e^{x}f\left(x\right)$ . For the last integral one then uses Gauss-Laguerre quadrature. Note, that while this approach works from an analytical perspective, it is not always numerically stable.

## Generalized Gauss–Laguerre quadrature

More generally, one can also consider integrands that have a known $x^{\alpha }$ power-law singularity at *x*=0, for some real number $\alpha >-1$ , leading to integrals of the form:

$\int _{0}^{+\infty }x^{\alpha }e^{-x}f(x)\,dx.$

In this case, the weights are given in terms of the generalized Laguerre polynomials:

$w_{i}={\frac {\Gamma (n+\alpha +1)x_{i}}{n!(n+1)^{2}[L_{n+1}^{(\alpha )}(x_{i})]^{2}}}\,,$

where $x_{i}$ are the roots of $L_{n}^{(\alpha )}$ .

This allows one to efficiently evaluate such integrals for polynomial or smooth *f*(*x*) even when α is not an integer.

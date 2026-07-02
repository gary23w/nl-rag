---
title: "Barnes integral"
source: https://en.wikipedia.org/wiki/Barnes_integral
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Barnes integral

In mathematics, a **Barnes integral** or **Mellin–Barnes integral** is a contour integral involving a product of gamma functions. They were introduced by Ernest William Barnes (1908, 1910). They are closely related to generalized hypergeometric series.

The integral is usually taken along a contour which is a deformation of the imaginary axis passing to the right of all poles of factors of the form Γ(*a* + *s*) and to the left of all poles of factors of the form Γ(*a* − *s*).

## Hypergeometric series

The hypergeometric function is given as a Barnes integral (Barnes 1908) by

${}_{2}F_{1}(a,b;c;z)={\frac {\Gamma (c)}{\Gamma (a)\Gamma (b)}}{\frac {1}{2\pi i}}\int _{-i\infty }^{i\infty }{\frac {\Gamma (a+s)\Gamma (b+s)\Gamma (-s)}{\Gamma (c+s)}}(-z)^{s}\,ds,$

see also (Andrews, Askey & Roy 1999, Theorem 2.4.1). This equality can be obtained by moving the contour to the right while picking up the residues at *s* = 0, 1, 2, ... . for $z\ll 1$ , and by analytic continuation elsewhere. Given proper convergence conditions, one can relate more general Barnes' integrals and generalized hypergeometric functions *p**F**q* in a similar way (Slater 1966).

## Barnes lemmas

The first Barnes lemma (Barnes 1908) states

${\frac {1}{2\pi i}}\int _{-i\infty }^{i\infty }\Gamma (a+s)\Gamma (b+s)\Gamma (c-s)\Gamma (d-s)ds={\frac {\Gamma (a+c)\Gamma (a+d)\Gamma (b+c)\Gamma (b+d)}{\Gamma (a+b+c+d)}}.$

This is an analogue of Gauss's 2*F*1 summation formula, and also an extension of Euler's beta integral. The integral in it is sometimes called **Barnes's beta integral**.

The second Barnes lemma (Barnes 1910) states

${\frac {1}{2\pi i}}\int _{-i\infty }^{i\infty }{\frac {\Gamma (a+s)\Gamma (b+s)\Gamma (c+s)\Gamma (1-d-s)\Gamma (-s)}{\Gamma (e+s)}}ds$

$={\frac {\Gamma (a)\Gamma (b)\Gamma (c)\Gamma (1-d+a)\Gamma (1-d+b)\Gamma (1-d+c)}{\Gamma (e-a)\Gamma (e-b)\Gamma (e-c)}}$

where *e* = *a* + *b* + *c* − *d* + 1. This is an analogue of Saalschütz's summation formula.

## q-Barnes integrals

There are analogues of Barnes integrals for basic hypergeometric series, and many of the other results can also be extended to this case (Gasper & Rahman 2004, chapter 4).

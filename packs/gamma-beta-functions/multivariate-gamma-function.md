---
title: "Multivariate gamma function"
source: https://en.wikipedia.org/wiki/Multivariate_gamma_function
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
---

# Multivariate gamma function

In mathematics, the **multivariate gamma function** Γ*p* is a generalization of the gamma function. It is useful in multivariate statistics, appearing in the probability density function of the Wishart and inverse Wishart distributions, and the matrix variate beta distribution.

It has two equivalent definitions. One is given as the following integral over the $p\times p$ positive-definite real matrices:

$\Gamma _{p}(a)=\int _{S>0}\exp \left(-{\rm {tr}}(S)\right)\,\left|S\right|^{a-{\frac {p+1}{2}}}dS,$

where $|S|$ denotes the determinant of S . The other one, more useful to obtain a numerical result is:

$\Gamma _{p}(a)=\pi ^{p(p-1)/4}\prod _{j=1}^{p}\Gamma (a+(1-j)/2).$

In both definitions, a is a complex number whose real part satisfies $\Re (a)>(p-1)/2$ . Note that $\Gamma _{1}(a)$ reduces to the ordinary gamma function. The second of the above definitions allows to directly obtain the recursive relationships for $p\geq 2$ :

$\Gamma _{p}(a)=\pi ^{(p-1)/2}\Gamma (a)\Gamma _{p-1}(a-{\tfrac {1}{2}})=\pi ^{(p-1)/2}\Gamma _{p-1}(a)\Gamma (a+(1-p)/2).$

Thus

- $\Gamma _{2}(a)=\pi ^{1/2}\Gamma (a)\Gamma (a-1/2)$
- $\Gamma _{3}(a)=\pi ^{3/2}\Gamma (a)\Gamma (a-1/2)\Gamma (a-1)$

and so on.

This can also be extended to non-integer values of p with the expression:

$\Gamma _{p}(a)=\pi ^{p(p-1)/4}{\frac {G(a+{\frac {1}{2}})G(a+1)}{G(a+{\frac {1-p}{2}})G(a+1-{\frac {p}{2}})}}$

Where G is the Barnes G-function, the indefinite product of the Gamma function.

The function is derived by Anderson from first principles who also cites earlier work by Wishart, Mahalanobis and others.

There also exists a version of the multivariate gamma function which instead of a single complex number takes a p -dimensional vector of complex numbers as its argument. It generalizes the above defined multivariate gamma function insofar as the latter is obtained by a particular choice of multivariate argument of the former.

## Derivatives

We may define the multivariate digamma function as

$\psi _{p}(a)={\frac {\partial \log \Gamma _{p}(a)}{\partial a}}=\sum _{i=1}^{p}\psi (a+(1-i)/2),$

and the general polygamma function as

$\psi _{p}^{(n)}(a)={\frac {\partial ^{n}\log \Gamma _{p}(a)}{\partial a^{n}}}=\sum _{i=1}^{p}\psi ^{(n)}(a+(1-i)/2).$

### Calculation steps

- Since

$\Gamma _{p}(a)=\pi ^{p(p-1)/4}\prod _{j=1}^{p}\Gamma \left(a+{\frac {1-j}{2}}\right),$

it follows that

${\frac {\partial \Gamma _{p}(a)}{\partial a}}=\pi ^{p(p-1)/4}\sum _{i=1}^{p}{\frac {\partial \Gamma \left(a+{\frac {1-i}{2}}\right)}{\partial a}}\prod _{j=1,j\neq i}^{p}\Gamma \left(a+{\frac {1-j}{2}}\right).$

- By definition of the digamma function, ψ,

${\frac {\partial \Gamma (a+(1-i)/2)}{\partial a}}=\psi (a+(i-1)/2)\Gamma (a+(i-1)/2)$

it follows that

${\begin{aligned}{\frac {\partial \Gamma _{p}(a)}{\partial a}}&=\pi ^{p(p-1)/4}\prod _{j=1}^{p}\Gamma (a+(1-j)/2)\sum _{i=1}^{p}\psi (a+(1-i)/2)\\[4pt]&=\Gamma _{p}(a)\sum _{i=1}^{p}\psi (a+(1-i)/2).\end{aligned}}$

---
title: "Tanh-sinh quadrature"
source: https://en.wikipedia.org/wiki/Tanh-sinh_quadrature
domain: numerical-quadrature
license: CC-BY-SA-4.0
tags: numerical integration, simpson's rule, romberg method, adaptive quadrature
fetched: 2026-07-02
---

# Tanh-sinh quadrature

**Tanh-sinh quadrature** is a method for numerical integration introduced by Hidetoshi Takahashi and Masatake Mori in 1974. It is especially applied where singularities or infinite derivatives exist at one or both endpoints.

The method uses hyperbolic functions in the change of variables

$x=\tanh \left({\frac {1}{2}}\pi \sinh t\right)\,$

to transform an integral on the interval *x* ∈ (−1, 1) to an integral on the entire real line *t* ∈ (−∞, ∞), the two integrals having the same value. After this transformation, the integrand decays with a double exponential rate, and thus, this method is also known as the **double exponential (DE) formula**.

For a given step size h , the integral is approximated by the sum

$\int _{-1}^{1}f(x)\,dx\approx \sum _{k=-\infty }^{\infty }w_{k}f(x_{k}),$

with the abscissas

$x_{k}=\tanh \left({\frac {1}{2}}\pi \sinh kh\right)$

and the weights

$w_{k}={\frac {{\frac {1}{2}}h\pi \cosh kh}{\cosh ^{2}\left({\frac {1}{2}}\pi \sinh kh\right)}}.$

## Use

The Tanh-Sinh method is quite insensitive to endpoint behavior. Should singularities or infinite derivatives exist at one or both endpoints of the (−1, 1) interval, these are mapped to the (−∞,∞) endpoints of the transformed interval, forcing the endpoint singularities and infinite derivatives to vanish. This results is a great enhancement of the accuracy of the numerical integration procedure, which is typically performed by the Trapezoidal rule. In most cases, the transformed integrand displays a rapid roll-off (decay), enabling the numerical integrator to quickly achieve convergence.

Like Gaussian quadrature, Tanh-Sinh quadrature is well suited for arbitrary-precision integration, where an accuracy of hundreds or even thousands of digits is desired. The convergence is exponential (in the discretization sense) for sufficiently well-behaved integrands: doubling the number of evaluation points roughly doubles the number of correct digits. However, Tanh-Sinh quadrature is not as efficient as Gaussian quadrature for smooth integrands; but unlike Gaussian quadrature, tends to work equally well with integrands having singularities or infinite derivatives at one or both endpoints of the integration interval as already noted. Furthermore, Tanh-Sinh quadrature can be implemented in a progressive manner, with the step size halved each time the rule level is raised, and reusing the function values calculated on previous levels. A further advantage is that the abscissas and weights are relatively simple to compute. The cost of calculating abscissa–weight pairs for *n*-digit accuracy is roughly *n*2 log2 *n* compared to *n*3 log *n* for Gaussian quadrature.

Bailey and others have done extensive research on Tanh-Sinh quadrature, Gaussian quadrature and Error Function quadrature, as well as several of the classical quadrature methods, and found that the classical methods are not competitive with the first three methods, particularly when high-precision results are required. In a conference paper presented at RNC5 on Real Numbers and Computers (Sept 2003), when comparing Tanh-Sinh quadrature with Gaussian quadrature and Error Function quadrature, Bailey and Li found: "Overall, the Tanh-Sinh scheme appears to be the best. It combines uniformly excellent accuracy with fast run times. *It is the nearest we have to a truly all-purpose quadrature scheme at the present time.*"

Upon comparing the scheme to Gaussian quadrature and Error Function quadrature, Bailey et al. (2005) found that the Tanh-Sinh scheme "appears to be the best for integrands of the type most often encountered in experimental math research".

Bailey (2006) found that: "The Tanh-Sinh quadrature scheme *is the fastest currently known high-precision quadrature scheme*, particularly when one counts the time for computing abscissas and weights. It has been successfully employed for quadrature calculations of up to 20,000-digit precision."

In summary, the Tanh-Sinh quadrature scheme is designed so that it gives the most accurate result for the minimum number of function evaluations. In practice, the Tanh-Sinh quadrature rule is almost invariably the best rule and is often the only effective rule when extended precision results are sought.

## Implementations

- Tanh-sinh, exp-sinh, and sinh-sinh quadrature are implemented in the C++ library Boost
- Tanh-sinh quadrature is implemented in a macro-enabled Excel spreadsheet by Graeme Dennes.
- Tanh-sinh quadrature is implemented in the Haskell package integration.
- Tanh-sinh quadrature is implemented in the Python library mpmath.
- Tanh-sinh quadrature in 1, 2, and 3 dimensions is implemented in the Julia package `FastTanhSinhQuadrature`
- Tanh-sinh, exp-sinh, and sinh-sinh quadrature are implemented in the Julia package `DoubleExponentialFormulas`
- An efficient implementation of Tanh-sinh quadrature in C# by Ned Ganchovski.

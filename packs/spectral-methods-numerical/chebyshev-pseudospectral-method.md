---
title: "Chebyshev pseudospectral method"
source: https://en.wikipedia.org/wiki/Chebyshev_pseudospectral_method
domain: spectral-methods-numerical
license: CC-BY-SA-4.0
tags: spectral method, pseudo-spectral method, galerkin method, collocation method
fetched: 2026-07-02
---

# Chebyshev pseudospectral method

The **Chebyshev pseudospectral method** for optimal control problems is based on Chebyshev polynomials of the first kind. It is part of the larger theory of pseudospectral optimal control, a term coined by Ross. Unlike the Legendre pseudospectral method, the Chebyshev pseudospectral (PS) method does not immediately offer high-accuracy quadrature solutions. Consequently, two different versions of the method have been proposed: one by Elnagar et al., and another by Fahroo and Ross. The two versions differ in their quadrature techniques. The Fahroo–Ross method is more commonly used today due to the ease in implementation of the Clenshaw–Curtis quadrature technique (in contrast to Elnagar–Kazemi's cell-averaging method). In 2008, Trefethen showed that the Clenshaw–Curtis method was nearly as accurate as Gauss quadrature. This breakthrough result opened the door for a covector mapping theorem for Chebyshev PS methods. A complete mathematical theory for Chebyshev PS methods was finally developed in 2009 by Gong, Ross and Fahroo.

## Other Chebyshev methods

The Chebyshev PS method is frequently confused with other Chebyshev methods. Prior to the advent of PS methods, many authors proposed using Chebyshev polynomials to solve optimal control problems; however, none of these methods belong to the class of pseudospectral methods.

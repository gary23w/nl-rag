---
title: "Gauss–Legendre quadrature"
source: https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature
domain: gaussian-quadrature
license: CC-BY-SA-4.0
tags: gaussian quadrature, gauss-legendre quadrature, gauss-kronrod quadrature, clenshaw-curtis quadrature
fetched: 2026-07-02
---

# Gauss–Legendre quadrature

In numerical analysis, **Gauss–Legendre quadrature** is a form of Gaussian quadrature for approximating the definite integral of a function. For integrating over the interval [−1, 1], the rule takes the form:

$\int _{-1}^{1}f(x)\,dx\approx \sum _{i=1}^{n}w_{i}f(x_{i})$

where

- *n* is the number of sample points used,
- *w**i* are quadrature weights, and
- *x**i* are the roots of the *n*th Legendre polynomial.

This choice of quadrature weights *w**i* and quadrature nodes *x**i* is the unique choice that allows the quadrature rule to integrate degree 2*n* − 1 polynomials exactly.

Many algorithms have been developed for computing Gauss–Legendre quadrature rules. The Golub–Welsch algorithm presented in 1969 reduces the computation of the nodes and weights to an eigenvalue problem which is solved by the QR algorithm. This algorithm was popular, but significantly more efficient algorithms exist. Algorithms based on the Newton–Raphson method are able to compute quadrature rules for significantly larger problem sizes. In 2014, Ignace Bogaert presented explicit asymptotic formulas for the Gauss–Legendre quadrature weights and nodes, which are accurate to within double-precision machine epsilon for any choice of *n* ≥ 21. This allows for computation of nodes and weights for values of *n* exceeding one billion.

## History

Carl Friedrich Gauss was the first to derive the Gauss–Legendre quadrature rule, doing so by a calculation with continued fractions in 1814. He calculated the nodes and weights to 16 digits up to order *n*=7 by hand. Carl Gustav Jacob Jacobi discovered the connection between the quadrature rule and the orthogonal family of Legendre polynomials. As there is no closed-form formula for the quadrature weights and nodes, for many decades people were only able to hand-compute them for small *n*, and computing the quadrature had to be done by referencing tables containing the weight and node values. By 1942 these values were only known for up to *n*=16.

## Definition

For integrating *f* over $[-1,1]$ with Gauss–Legendre quadrature, the associated orthogonal polynomials are Legendre polynomials, denoted by *P**n*(*x*). With the n-th polynomial normalized so that *P**n*(1) = 1, the i-th Gauss node, xi, is the i-th root of Pn and the weights are given by the formula

$w_{i}={\frac {2}{\left(1-x_{i}^{2}\right)\left[P'_{n}(x_{i})\right]^{2}}}.$

Some low-order quadrature rules are tabulated below for integrating over $[-1,1]$ .

| Number of points, *n* | Points, xi | Weights, wi |   |   |
|---|---|---|---|---|
| 1 | 0 | 2 |   |   |
| 2 | $\pm {\frac {1}{\sqrt {3}}}$ | ±0.57735… | 1 |   |
| 3 | 0 | ${\frac {8}{9}}$ | 0.888889… |   |
| $\pm {\sqrt {\frac {3}{5}}}$ | ±0.774597… | ${\frac {5}{9}}$ | 0.555556… |   |
| 4 | $\pm {\sqrt {{\frac {3}{7}}-{\frac {2}{7}}{\sqrt {\frac {6}{5}}}}}$ | ±0.339981… | ${\frac {18+{\sqrt {30}}}{36}}$ | 0.652145… |
| $\pm {\sqrt {{\frac {3}{7}}+{\frac {2}{7}}{\sqrt {\frac {6}{5}}}}}$ | ±0.861136… | ${\frac {18-{\sqrt {30}}}{36}}$ | 0.347855… |   |
| 5 | 0 | ${\frac {128}{225}}$ | 0.568889… |   |
| $\pm {\frac {1}{3}}{\sqrt {5-2{\sqrt {\frac {10}{7}}}}}$ | ±0.538469… | ${\frac {322+13{\sqrt {70}}}{900}}$ | 0.478629… |   |
| $\pm {\frac {1}{3}}{\sqrt {5+2{\sqrt {\frac {10}{7}}}}}$ | ±0.90618… | ${\frac {322-13{\sqrt {70}}}{900}}$ | 0.236927… |   |

For integrating over a general real interval $[a,b]$ , a change of interval can be applied to convert the problem to one of integrating over $[-1,1]$ .

## Algorithms

### Newton–Raphson methods

Several researchers have developed algorithms for computing Gauss–Legendre quadrature nodes and weights based on the Newton–Raphson method for finding roots of functions. Various optimizations for this specific problem are used. For instance, some methods compute $\theta _{i}=\arccos x_{i}$ to avoid issues associated with clustering of the roots $x_{i}$ near the ends of the interval $-1$ and 1 . Some methods utilize formulas to approximate the weights and then use a few iterations of Newton-Raphson to lower the error of the approximation to below machine precision.

### Golub–Welsch

In 1969, Golub and Welsch published their method for computing Gaussian quadrature rules given the three term recurrence relation that the underlying orthogonal polynomials satisfy. They reduce the problem of computing the nodes of a Gaussian quadrature rule to the problem of finding the eigenvalues of a particular symmetric tridiagonal matrix. The QR algorithm is used to find the eigenvalues of this matrix. By taking advantage of the symmetric tridiagonal structure, the eigenvalues can be computed in ${\mathcal {O}}(n^{2})$ time, as opposed to the ${\mathcal {O}}(n^{3})$ time expected for a generic eigenvalue problem.

### Asymptotic formulas

Various methods have been developed that use approximate closed-form expressions to compute the nodes. As mentioned above, in some methods formulas are used as approximations to the nodes, after which some Newton-Raphson iterations are performed to refine the approximation. In a 2014 paper, Ignace Bogaert derives asymptotic formulas for the nodes that are exact up to machine precision for $n\geq 21$ and for the weights that are exact up to machine precision for $n\geq 30$ . This method does not require any Newton-Raphson iterations or evaluations of Bessel functions as other methods do. As shown in the paper, the method was able to compute the nodes at a problem size of one billion in 11 seconds. Since the nodes near the endpoints of $[-1,1]$ become very close to each other at this problem size, this method of computing the nodes is sufficient for essentially any practical application in double-precision floating point.

### Higher precision

Johansson and Mezzarobba describe a strategy to compute Gauss–Legendre quadrature rules in arbitrary-precision arithmetic, allowing both small and large n . A rule of order $n=1000$ with 1000 digits of precision can be calculated in around one second. Their method uses Newton–Raphson iteration together with several different techniques for evaluating Legendre polynomials. The algorithm also provides a certified error bound.

Gil, Segura and Temme describe iterative methods with fourth order convergence for the computation of Gauss–Jacobi quadratures (and, in particular, Gauss–Legendre). The methods do not require a priori estimations of the nodes to guarantee its fourth-order convergence. Computations of quadrature rules with even millions of nodes and thousands of digits become possible in a typical laptop.

## Comparison with other quadrature rules

Gauss–Legendre quadrature is optimal in a very narrow sense for computing integrals of a function *f* over [−1, 1], since no other quadrature rule integrates all degree 2*n* − 1 polynomials exactly when using *n* sample points. However, this measure of accuracy is not generally a very useful one---polynomials are very simple to integrate and this argument does not by itself guarantee better accuracy on integrating other functions.

Clenshaw–Curtis quadrature is based on approximating *f* by a polynomial interpolant at Chebyshev nodes and integrates polynomials of degree up to *n* exactly when given *n* samples. Even though it does not integrate polynomials or other functions that are analytic in a large neighborhood of [−1, 1] as well as Gauss–Legendre quadrature, Clenshaw–Curtis converges at approximately the same rate as Gauss–Legendre quadrature for most (non-analytic) integrands. Also, Clenshaw–Curtis shares the properties that Gauss–Legendre quadrature enjoys of convergence for all continuous integrands f and robustness to numerical rounding errors. Clenshaw–Curtis is straightforward to implement in ${\mathcal {O}}(n\log n)$ time by FFT-based methods.

Newton–Cotes quadrature is based on approximating *f* by a polynomial interpolant at equally-spaced points in [−1, 1], and like Clenshaw–Curtis also integrates polynomials of degree up to *n* exactly when given *n* samples. However, it suffers from Runge's phenomenon as *n* increases; Newton–Cotes does not converge for some continuous integrands *f*, and when it does converge it may suffer from numerical rounding errors. Thus, both Clenshaw–Curtis and Gauss–Legendre enjoy substantial benefits over Newton–Cotes for moderate to large *n*.

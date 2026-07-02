---
title: "Integral (part 2/2)"
source: https://en.wikipedia.org/wiki/Integral
domain: calculus
license: CC-BY-SA-4.0
tags: calculus, differential calculus, integral calculus, differentiation, antiderivative
fetched: 2026-07-02
part: 2/2
---

## Computation

### Analytical

The most basic technique for computing definite integrals of one real variable is based on the fundamental theorem of calculus. Let *f*(*x*) be the function of x to be integrated over a given interval [*a*, *b*]. Then, find an antiderivative of f; that is, a function F such that *F*′ = *f* on the interval. Provided the integrand and integral have no singularities on the path of integration, by the fundamental theorem of calculus,

∫

a

b

f

(

x

)

d

x

=

F

(

b

)

−

F

(

a

)

.

{\displaystyle \int _{a}^{b}f(x)\,dx=F(b)-F(a).}

Sometimes it is necessary to use one of the many techniques that have been developed to evaluate integrals. Most of these techniques rewrite one integral as a different one which is hopefully more tractable. Techniques include integration by substitution, integration by parts, integration by trigonometric substitution, and integration by partial fractions.

Alternative methods exist to compute more complex integrals. Many nonelementary integrals can be expanded in a Taylor series and integrated term by term. Occasionally, the resulting infinite series can be summed analytically. The method of convolution using Meijer G-functions can also be used, assuming that the integrand can be written as a product of Meijer G-functions. There are also many less common ways of calculating definite integrals; for instance, Parseval's identity can be used to transform an integral over a rectangular region into an infinite sum. Occasionally, an integral can be evaluated by a trick; for an example of this, see Gaussian integral.

Computations of volumes of solids of revolution can usually be done with disk integration or shell integration.

Specific results which have been worked out by various techniques are collected in the list of integrals.

### Symbolic

Many problems in mathematics, physics, and engineering involve integration where an explicit formula for the integral is desired. Extensive tables of integrals have been compiled and published over the years for this purpose. With the spread of computers, many professionals, educators, and students have turned to computer algebra systems that are specifically designed to perform difficult or tedious tasks, including integration. Symbolic integration has been one of the motivations for the development of the first such systems, like Macsyma and Maple.

A major mathematical difficulty in symbolic integration is that in many cases, a relatively simple function does not have integrals that can be expressed in closed form involving only elementary functions, include rational and exponential functions, logarithm, trigonometric functions and inverse trigonometric functions, and the operations of multiplication and composition. The Risch algorithm provides a general criterion to determine whether the antiderivative of an elementary function is elementary and to compute the integral if is elementary. However, functions with closed expressions of antiderivatives are the exception, and consequently, computerized algebra systems have no hope of being able to find an antiderivative for a randomly constructed elementary function. On the positive side, if the 'building blocks' for antiderivatives are fixed in advance, it may still be possible to decide whether the antiderivative of a given function can be expressed using these blocks and operations of multiplication and composition and to find the symbolic answer whenever it exists. The Risch algorithm, implemented in Mathematica, Maple and other computer algebra systems, does just that for functions and antiderivatives built from rational functions, radicals, logarithm, and exponential functions.

Some special integrands occur often enough to warrant special study. In particular, it may be useful to have, in the set of antiderivatives, the special functions (like the Legendre functions, the hypergeometric function, the gamma function, the incomplete gamma function and so on). Extending Risch's algorithm to include such functions is possible but challenging and has been an active research subject.

More recently a new approach has emerged, using *D*-finite functions, which are the solutions of linear differential equations with polynomial coefficients. Most of the elementary and special functions are *D*-finite, and the integral of a *D*-finite function is also a *D*-finite function. This provides an algorithm to express the antiderivative of a *D*-finite function as the solution of a differential equation. This theory also allows one to compute the definite integral of a *D*-function as the sum of a series given by the first coefficients and provides an algorithm to compute any coefficient.

Rule-based integration systems facilitate integration. Rubi, a computer algebra system rule-based integrator, pattern matches an extensive system of symbolic integration rules to integrate a wide variety of integrands. This system uses over 6600 integration rules to compute integrals. The method of brackets is a generalization of Ramanujan's master theorem that can be applied to a wide range of univariate and multivariate integrals. A set of rules are applied to the coefficients and exponential terms of the integrand's power series expansion to determine the integral. The method is closely related to the Mellin transform.

### Numerical

Definite integrals may be approximated using several methods of numerical integration. The rectangle method relies on dividing the region under the function into a series of rectangles corresponding to function values and multiplies by the step width to find the sum. A better approach, the trapezoidal rule, replaces the rectangles used in a Riemann sum with trapezoids. The trapezoidal rule weights the first and last values by one half, then multiplies by the step width to obtain a better approximation. The idea behind the trapezoidal rule, that more accurate approximations to the function yield better approximations to the integral, can be carried further: Simpson's rule approximates the integrand by a piecewise quadratic function.

Riemann sums, the trapezoidal rule, and Simpson's rule are examples of a family of quadrature rules called the Newton–Cotes formulas. The degree n Newton–Cotes quadrature rule approximates the polynomial on each subinterval by a degree *n* polynomial. This polynomial is chosen to interpolate the values of the function on the interval. Higher degree Newton–Cotes approximations can be more accurate, but they require more function evaluations, and they can suffer from numerical inaccuracy due to Runge's phenomenon. One solution to this problem is Clenshaw–Curtis quadrature, in which the integrand is approximated by expanding it in terms of Chebyshev polynomials.

Romberg's method halves the step widths incrementally, giving trapezoid approximations denoted by *T*(*h*0), *T*(*h*1), and so on, where *h**k*+1 is half of *h**k*. For each new step size, only half the new function values need to be computed; the others carry over from the previous size. It then interpolate a polynomial through the approximations, and extrapolate to *T*(0). Gaussian quadrature evaluates the function at the roots of a set of orthogonal polynomials. An n-point Gaussian method is exact for polynomials of degree up to 2*n* − 1.

The computation of higher-dimensional integrals (for example, volume calculations) makes important use of such alternatives as Monte Carlo integration.

### Mechanical

The area of an arbitrary two-dimensional shape can be determined using a measuring instrument called planimeter. The volume of irregular objects can be measured with precision by the fluid displaced as the object is submerged.

### Geometrical

Area can sometimes be found via geometrical compass-and-straightedge constructions of an equivalent square.

### Integration by differentiation

Kempf, Jackson and Morales demonstrated mathematical relations that allow an integral to be calculated by means of differentiation. Their calculus involves the Dirac delta function and the partial derivative operator ∂ x {\displaystyle \partial _{x}} ({\displaystyle \partial _{x}}). This can also be applied to functional integrals, allowing them to be computed by functional differentiation.


## Examples

### Using the fundamental theorem of calculus

The fundamental theorem of calculus allows straightforward calculations of basic functions:

∫

0

π

sin

⁡

(

x

)

d

x

=

−

cos

⁡

(

x

)

|

x

=

0

x

=

π

=

−

cos

⁡

(

π

)

−

(

−

cos

⁡

(

0

)

)

=

2.

{\displaystyle \int _{0}^{\pi }\sin(x)\,dx=-\cos(x){\big |}_{x=0}^{x=\pi }=-\cos(\pi )-{\big (}-\cos(0){\big )}=2.}

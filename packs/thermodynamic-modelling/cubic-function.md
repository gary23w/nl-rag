---
title: "Cubic function"
source: https://en.wikipedia.org/wiki/Cubic_function
domain: thermodynamic-modelling
license: CC-BY-SA-4.0
tags: thermodynamic modelling
fetched: 2026-07-04
---

# Cubic function

In mathematics, a **cubic function** is a function of the form $f(x)=ax^{3}+bx^{2}+cx+d,$ with ⁠ $a\neq 0$ ⁠, that is, a polynomial function of degree three. In many texts, the *coefficients* a, b, c, and d are supposed to be real numbers, and the function is considered as a real function that maps real numbers to real numbers or as a complex function that maps complex numbers to complex numbers. In other cases, the coefficients may be complex numbers, and the function is a complex function that has the set of the complex numbers as its codomain, even when the domain is restricted to the real numbers.

Setting *f*(*x*) = 0 produces a cubic equation of the form

$ax^{3}+bx^{2}+cx+d=0,$

whose solutions are called roots of the function. The derivative of a cubic function is a quadratic function.

A cubic function with real coefficients has either one or three real roots (which may not be distinct); all odd-degree polynomials with real coefficients have at least one real root.

The graph of a cubic function always has a single inflection point. It may have two critical points, a local minimum and a local maximum. Otherwise, a cubic function is monotonic. The graph of a cubic function is symmetric with respect to its inflection point; that is, it is invariant under a rotation of a half turn around this point. Up to an affine transformation, there are only three possible graphs for cubic functions.

Cubic functions are fundamental for cubic interpolation.

## History

## Critical and inflection points

The critical points of a cubic function are its stationary points, that is the points where the slope of the function is zero. Thus the critical points of a cubic function *f* defined by

f

(

x

) =

ax

3

+

bx

2

+

cx

+

d

,

occur at values of *x* such that the derivative

$3ax^{2}+2bx+c=0$

of the cubic function is zero.

The solutions of this equation are the x-values of the critical points and are given, using the quadratic formula, by

$x_{\text{critical}}={\frac {-b\pm {\sqrt {b^{2}-3ac}}}{3a}}.$

The sign of the expression Δ0 = *b*2 − 3*ac* inside the square root determines the number of critical points. If it is positive, then there are two critical points, one is a local maximum, and the other is a local minimum. If *b*2 − 3*ac* = 0, then there is only one critical point, which is an inflection point. If *b*2 − 3*ac* < 0, then there are no (real) critical points. In the two latter cases, that is, if *b*2 − 3*ac* is nonpositive, the cubic function is strictly monotonic. See the figure for an example of the case Δ0 > 0.

The inflection point of a function is where that function changes concavity. An inflection point occurs when the second derivative $f''(x)=6ax+2b,$ is zero, and the third derivative is nonzero. Thus a cubic function has always a single inflection point, which occurs at

$x_{\text{inflection}}=-{\frac {b}{3a}}.$

## Classification

The graph of a cubic function is a cubic curve, though many cubic curves are not graphs of functions.

Although cubic functions depend on four parameters, their graph can have only very few shapes. In fact, the graph of a cubic function is always similar to the graph of a function of the form

$y=x^{3}+px.$

This similarity can be built as the composition of translations parallel to the coordinates axes, a homothecy (uniform scaling), and, possibly, a reflection (mirror image) with respect to the y-axis. A further non-uniform scaling can transform the graph into the graph of one among the three cubic functions

${\begin{aligned}y&=x^{3}+x\\y&=x^{3}\\y&=x^{3}-x.\end{aligned}}$

This means that there are only three graphs of cubic functions up to an affine transformation.

The above geometric transformations can be built in the following way, when starting from a general cubic function $y=ax^{3}+bx^{2}+cx+d.$

Firstly, if *a* < 0, the change of variable *x* → −*x* allows supposing *a* > 0. After this change of variable, the new graph is the mirror image of the previous one, with respect of the y-axis.

Then, the change of variable *x* = *x*1 − ⁠*b*/3*a*⁠ provides a function of the form

$y=ax_{1}^{3}+px_{1}+q.$

This corresponds to a translation parallel to the x-axis.

The change of variable *y* = *y*1 + *q* corresponds to a translation with respect to the y-axis, and gives a function of the form

$y_{1}=ax_{1}^{3}+px_{1}.$

The change of variable $\textstyle x_{1}={\frac {x_{2}}{\sqrt {a}}},y_{1}={\frac {y_{2}}{\sqrt {a}}}$ corresponds to a uniform scaling, and give, after multiplication by ${\sqrt {a}},$ a function of the form

$y_{2}=x_{2}^{3}+px_{2},$

which is the simplest form that can be obtained by a similarity.

Then, if *p* ≠ 0, the non-uniform scaling $\textstyle x_{2}=x_{3}{\sqrt {|p|}},\quad y_{2}=y_{3}{\sqrt {|p|^{3}}}$ gives, after division by $\textstyle {\sqrt {|p|^{3}}},$

$y_{3}=x_{3}^{3}+x_{3}\operatorname {sgn}(p),$

where $\operatorname {sgn}(p)$ has the value 1 or −1, depending on the sign of p. If one defines $\operatorname {sgn}(0)=0,$ the latter form of the function applies to all cases (with $x_{2}=x_{3}$ and $y_{2}=y_{3}$ ).

## Symmetry

For a cubic function of the form $y=x^{3}+px,$ the inflection point is thus the origin. As such a function is an odd function, its graph is symmetric with respect to the inflection point, and invariant under a rotation of a half turn around the inflection point. As these properties are invariant by similarity, the following is true for all cubic functions.

*The graph of a cubic function is symmetric with respect to its inflection point, and is invariant under a rotation of a half turn around the inflection point.*

## Collinearities

The tangent lines to the graph of a cubic function at three collinear points intercept the cubic again at collinear points. This can be seen as follows.

As this property is invariant under a rigid motion, one may suppose that the function has the form

$f(x)=x^{3}+px.$

If α is a real number, then the tangent to the graph of f at the point (*α*, *f*(*α*)) is the line

{(

x

,

f

(

α

) + (

x

−

α

)

f

′(

α

))

:

x

∈

R

}

.

So, the intersection point between this line and the graph of f can be obtained solving the equation *f*(*x*) = *f*(*α*) + (*x* − *α*)*f* ′(*α*), that is

$x^{3}+px=\alpha ^{3}+p\alpha +(x-\alpha )(3\alpha ^{2}+p),$

which can be rewritten

$x^{3}-3\alpha ^{2}x+2\alpha ^{3}=0,$

and factorized as

$(x-\alpha )^{2}(x+2\alpha )=0.$

So, the tangent intercepts the cubic at

$(-2\alpha ,-8\alpha ^{3}-2p\alpha )=(-2\alpha ,-8f(\alpha )+6p\alpha ).$

So, the function that maps a point (*x*, *y*) of the graph to the other point where the tangent intercepts the graph is

$(x,y)\mapsto (-2x,-8y+6px).$

This is an affine transformation that transforms collinear points into collinear points. This proves the claimed result.

## Cubic interpolation

Given the values of a function and its derivative at two points, there is exactly one cubic function that has the same four values, which is called a cubic Hermite spline.

There are two standard ways for using this fact. Firstly, if one knows, for example by physical measurement, the values of a function and its derivative at some sampling points, one can *interpolate* the function with a continuously differentiable function, which is a piecewise cubic function.

If the value of a function is known at several points, cubic interpolation consists in approximating the function by a continuously differentiable function, which is piecewise cubic. For having a uniquely defined interpolation, two more constraints must be added, such as the values of the derivatives at the endpoints, or a zero curvature at the endpoints.

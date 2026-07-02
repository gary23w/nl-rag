---
title: "Linear interpolation"
source: https://en.wikipedia.org/wiki/Linear_interpolation
domain: animation-blending
license: CC-BY-SA-4.0
tags: animation blending, animation blend tree, keyframe interpolation, spherical linear interpolation
fetched: 2026-07-02
---

# Linear interpolation

In mathematics, **linear interpolation** (sometimes **lerp**) is a method of curve fitting using linear polynomials to construct new data points within the range of a discrete set of known data points.

## Linear interpolation between two known points

If the two known points are given by the coordinates $(x_{0},y_{0})$ and $(x_{1},y_{1})$ , the **linear interpolant** is the straight line between these points. For a value x in the interval $(x_{0},x_{1})$ , the value y along the straight line is given from the equation of slopes ${\frac {y-y_{0}}{x-x_{0}}}={\frac {y_{1}-y_{0}}{x_{1}-x_{0}}},$ which can be derived geometrically from the figure on the right. It is a special case of polynomial interpolation with $n=1$ .

Solving this equation for y , which is the unknown value at x , gives ${\begin{aligned}y&=y_{0}+(x-x_{0}){\frac {y_{1}-y_{0}}{x_{1}-x_{0}}}\\&={\frac {y_{0}(x_{1}-x_{0})}{x_{1}-x_{0}}}+{\frac {y_{1}(x-x_{0})-y_{0}(x-x_{0})}{x_{1}-x_{0}}}\\&={\frac {y_{1}x-y_{1}x_{0}-y_{0}x+y_{0}x_{0}+y_{0}x_{1}-y_{0}x_{0}}{x_{1}-x_{0}}}\\&={\frac {y_{0}(x_{1}-x)+y_{1}(x-x_{0})}{x_{1}-x_{0}}},\end{aligned}}$ which is the formula for linear interpolation in the interval $(x_{0},x_{1})$ . Outside this interval, the formula is identical to linear extrapolation.

This formula can also be understood as a weighted average. The weights are inversely related to the distance from the end points to the unknown point; the closer point has more influence than the farther point. Thus, the weights are ${\textstyle 1-(x-x_{0})/(x_{1}-x_{0})}$ and ${\textstyle 1-(x_{1}-x)/(x_{1}-x_{0})}$ , which are normalized distances between the unknown point and each of the end points. Because these sum to 1, ${\begin{aligned}y&=y_{0}\left(1-{\frac {x-x_{0}}{x_{1}-x_{0}}}\right)+y_{1}\left(1-{\frac {x_{1}-x}{x_{1}-x_{0}}}\right)\\&=y_{0}\left(1-{\frac {x-x_{0}}{x_{1}-x_{0}}}\right)+y_{1}\left({\frac {x-x_{0}}{x_{1}-x_{0}}}\right)\\&=y_{0}\left({\frac {x_{1}-x}{x_{1}-x_{0}}}\right)+y_{1}\left({\frac {x-x_{0}}{x_{1}-x_{0}}}\right)\end{aligned}}$ yielding the formula for linear interpolation given above.

## Interpolation of a data set

Linear interpolation on a set of data points (*x*0, *y*0), (*x*1, *y*1), ..., (*x*n, *y*n) is defined as piecewise linear, resulting from the concatenation of linear segment interpolants between each pair of data points. This results in a continuous curve, with a discontinuous derivative (in general), thus of differentiability class $C^{0}$ .

## Linear interpolation as an approximation

Linear interpolation is often used to approximate a value of some function f using two known values of that function at other points. The *error* of this approximation is defined as $R_{T}=f(x)-p(x),$ where p denotes the linear interpolation polynomial defined above: $p(x)=f(x_{0})+{\frac {f(x_{1})-f(x_{0})}{x_{1}-x_{0}}}(x-x_{0}).$

It can be proven using Rolle's theorem that if f has a continuous second derivative, then the error is bounded by $|R_{T}|\leq {\frac {(x_{1}-x_{0})^{2}}{8}}\max _{x_{0}\leq x\leq x_{1}}\left|f''(x)\right|.$

That is, the approximation between two points on a given function gets worse with the second derivative of the function that is approximated. This is intuitively correct as well: the "curvier" the function is, the worse the approximations made with simple linear interpolation become.

## History and applications

Linear interpolation has been used since antiquity for filling the gaps in tables. Suppose that one has a table listing the population of some country in 1970, 1980, 1990 and 2000, and that one wanted to estimate the population in 1994. Linear interpolation is an easy way to do this. It is believed that it was used in the Seleucid Empire (last three centuries BC) and by the Greek astronomer and mathematician Hipparchus (second century BC). A description of linear interpolation can be found in the ancient Chinese mathematical text called *The Nine Chapters on the Mathematical Art* (九章算術), dated from 200 BC to AD 100 and the *Almagest* (2nd century AD) by Ptolemy.

The basic operation of linear interpolation between two values is commonly used in computer graphics. In that field's jargon it is sometimes called a **lerp** (from **l**inear int**erp**olation). The term can be used as a verb or noun for the operation. e.g. "Bresenham's algorithm lerps incrementally between the two endpoints of the line."

Lerp operations are built into the hardware of all modern computer graphics processors. They are often used as building blocks for more complex operations: for example, a bilinear interpolation can be accomplished in three lerps. Because this operation is cheap, it's also a good way to implement accurate lookup tables with quick lookup for smooth functions without having too many table entries.

## Extensions

### Accuracy

If a *C*0 function is insufficient, for example if the process that has produced the data points is known to be smoother than *C*0, it is common to replace linear interpolation with spline interpolation or, in some cases, polynomial interpolation.

### Multivariate

Linear interpolation as described here is for data points in one spatial dimension. For two spatial dimensions, the extension of linear interpolation is called bilinear interpolation, and in three dimensions, trilinear interpolation. Notice, though, that these interpolants are no longer linear functions of the spatial coordinates, rather products of linear functions; this is illustrated by the clearly non-linear example of bilinear interpolation in the figure below. Other extensions of linear interpolation can be applied to other kinds of mesh such as triangular and tetrahedral meshes, including Bézier surfaces. These may be defined as indeed higher-dimensional piecewise linear functions (see second figure below).

## Programming language support

Many libraries and shading languages have a "lerp" helper-function (in GLSL known instead as **mix**), returning an interpolation between two inputs `(v0, v1)` for a parameter `t` in the closed unit interval [0, 1]. Signatures between lerp functions are variously implemented in both the forms `(v0, v1, t)` and `(t, v0, v1)`.

```mw
// Imprecise method, which does not guarantee v = v1 when t = 1, due to floating-point arithmetic error.
// This method is monotonic. This form may be used when the hardware has a native fused multiply-add instruction.
float lerp(float v0, float v1, float t) {
  return v0 + t * (v1 - v0);
}

// Precise method, which guarantees v = v1 when t = 1. This method is monotonic only when v0 * v1 < 0.
// Lerping between same values might not produce the same value
float lerp(float v0, float v1, float t) {
  return (1 - t) * v0 + t * v1;
}
```

This lerp function is commonly used for alpha blending (the parameter "*t*" is the "alpha value"), and the formula may be extended to blend multiple components of a vector (such as spatial *x*, *y*, *z* axes or *r*, *g*, *b* colour components) in parallel.

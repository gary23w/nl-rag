---
title: "Spline interpolation"
source: https://en.wikipedia.org/wiki/Spline_interpolation
domain: spline-interpolation
license: CC-BY-SA-4.0
tags: spline interpolation, cubic hermite spline, smoothing spline, thin plate spline
fetched: 2026-07-02
---

# Spline interpolation

In the mathematical field of numerical analysis, **spline interpolation** is a form of interpolation where the interpolant is a special type of piecewise polynomial called a spline. That is, instead of fitting a single, high-degree polynomial to all of the values at once, spline interpolation fits low-degree polynomials to small subsets of the values, for example, fitting nine cubic polynomials between each of the pairs of ten points, instead of fitting a single degree-nine polynomial to all of them. Spline interpolation is often preferred over polynomial interpolation because the interpolation error can be made small even when using low-degree polynomials for the spline. Spline interpolation also avoids the problem of Runge's phenomenon, in which oscillation can occur between points when interpolating using high-degree polynomials.

## Introduction

Originally, *spline* was a term for elastic rulers that were bent to pass through a number of predefined points, or *knots*. These were used to make technical drawings for shipbuilding and construction by hand, as illustrated in the figure.

We wish to model similar kinds of curves using a set of mathematical equations. Assume we have a sequence of $n+1$ knots, $(x_{0},y_{0})$ through $(x_{n},y_{n})$ . There will be a cubic polynomial $q_{i}(x)=y$ between each successive pair of knots $(x_{i-1},y_{i-1})$ and $(x_{i},y_{i})$ connecting to both of them, where $i=1,2,\dots ,n$ . So there will be n polynomials, with the first polynomial starting at $(x_{0},y_{0})$ , and the last polynomial ending at $(x_{n},y_{n})$ .

The curvature of any curve $y=y(x)$ is defined as

$\kappa ={\frac {y''}{(1+y'^{2})^{3/2}}},$

where $y'$ and $y''$ are the first and second derivatives of $y(x)$ with respect to x . To make the spline take a shape that minimizes the bending (under the constraint of passing through all knots), we will define both $y'$ and $y''$ to be continuous everywhere, including at the knots. Each successive polynomial must have equal values (which are equal to the y-value of the corresponding datapoint), derivatives, and second derivatives at their joining knots, which is to say that

${\begin{cases}q_{i}(x_{i})=q_{i+1}(x_{i})=y_{i}\\q'_{i}(x_{i})=q'_{i+1}(x_{i})\\q''_{i}(x_{i})=q''_{i+1}(x_{i})\end{cases}}\qquad 1\leq i\leq n-1.$

This can only be achieved if polynomials of degree 3 (cubic polynomials) or higher are used. The classical approach is to use polynomials of exactly degree 3 — cubic splines.

In addition to the three conditions above, a *natural cubic spline* has the condition that $q''_{1}(x_{0})=q''_{n}(x_{n})=0$ .

In addition to the three main conditions above, a *clamped cubic spline* has the conditions that $q'_{1}(x_{0})=f'(x_{0})$ and $q'_{n}(x_{n})=f'(x_{n})$ where $f'(x)$ is the derivative of the interpolated function.

In addition to the three main conditions above, a *not-a-knot spline* has the conditions that $q'''_{1}(x_{1})=q'''_{2}(x_{1})$ and $q'''_{n-1}(x_{n-1})=q'''_{n}(x_{n-1})$ .

## Algorithm to find the interpolating cubic spline

We wish to find each polynomial $q_{i}(x)$ given the points $(x_{0},y_{0})$ through $(x_{n},y_{n})$ . To do this, we will consider just a single piece of the curve, $q(x)$ , which will interpolate from $(x_{1},y_{1})$ to $(x_{2},y_{2})$ . This piece will have slopes $k_{1}$ and $k_{2}$ at its endpoints. Or, more precisely,

$q(x_{1})=y_{1},$

$q(x_{2})=y_{2},$

$q'(x_{1})=k_{1},$

$q'(x_{2})=k_{2}.$

The full equation $q(x)$ can be written in the symmetrical form

| $q(x)={\big (}1-t(x){\big )}\,y_{1}+t(x)\,y_{2}+t(x){\big (}1-t(x){\big )}{\Big (}{\big (}1-t(x){\big )}\,a+t(x)\,b{\Big )},$ |   | 1 |
|---|---|---|

where

| $t(x)={\frac {x-x_{1}}{x_{2}-x_{1}}},$ |   | 2 |
|---|---|---|

| $a=k_{1}(x_{2}-x_{1})-(y_{2}-y_{1}),$ |   | 3 |
|---|---|---|

| $b=-k_{2}(x_{2}-x_{1})+(y_{2}-y_{1}).$ |   | 4 |
|---|---|---|

But what are $k_{1}$ and $k_{2}$ ? To derive these critical values, we must consider that

$q'={\frac {dq}{dx}}={\frac {dq}{dt}}{\frac {dt}{dx}}={\frac {dq}{dt}}{\frac {1}{x_{2}-x_{1}}}.$

It then follows that

| $q'={\frac {y_{2}-y_{1}}{x_{2}-x_{1}}}+(1-2t){\frac {a(1-t)+bt}{x_{2}-x_{1}}}+t(1-t){\frac {b-a}{x_{2}-x_{1}}},$ |   | 5 |
|---|---|---|

| $q''=2{\frac {b-2a+(a-b)3t}{{(x_{2}-x_{1})}^{2}}}.$ |   | 6 |
|---|---|---|

Setting *t* = *0* and *t* = *1* respectively in equations (**5**) and (**6**), one gets from (**2**) that indeed first derivatives *q′*(*x*1) = *k*1 and *q′*(*x*2) = *k*2, and also second derivatives

| $q''(x_{1})=2{\frac {b-2a}{{(x_{2}-x_{1})}^{2}}},$ |   | 7 |
|---|---|---|

| $q''(x_{2})=2{\frac {a-2b}{{(x_{2}-x_{1})}^{2}}}.$ |   | 8 |
|---|---|---|

If now (*xi*, *yi*), *i* = 0, 1, ..., *n* are *n* + 1 points, and

| $q_{i}=(1-t)\,y_{i-1}+t\,y_{i}+t(1-t){\big (}(1-t)\,a_{i}+t\,b_{i}{\big )},$ |   | 9 |
|---|---|---|

where *i* = 1, 2, ..., *n*, and $t={\tfrac {x-x_{i-1}}{x_{i}-x_{i-1}}}$ are *n* third-degree polynomials interpolating y in the interval *x**i*−1 ≤ *x* ≤ *xi* for *i* = 1, ..., *n* such that *q′i* (*xi*) = *q′**i*+1(*xi*) for *i* = 1, ..., *n* − 1, then the *n* polynomials together define a differentiable function in the interval *x*0 ≤ *x* ≤ *xn*, and

| $a_{i}=k_{i-1}(x_{i}-x_{i-1})-(y_{i}-y_{i-1}),$ |   | 10 |
|---|---|---|

| $b_{i}=-k_{i}(x_{i}-x_{i-1})+(y_{i}-y_{i-1})$ |   | 11 |
|---|---|---|

for *i* = 1, ..., *n*, where

| $k_{0}=q_{1}'(x_{0}),$ |   | 12 |
|---|---|---|

| $k_{i}=q_{i}'(x_{i})=q_{i+1}'(x_{i}),\qquad i=1,\dots ,n-1,$ |   | 13 |
|---|---|---|

| $k_{n}=q_{n}'(x_{n}).$ |   | 14 |
|---|---|---|

If the sequence *k*0, *k*1, ..., *kn* is such that, in addition, *q′′i*(*xi*) = *q′′**i*+1(*xi*) holds for *i* = 1, ..., *n* − 1, then the resulting function will even have a continuous second derivative.

From (**7**), (**8**), (**10**) and (**11**) follows that this is the case if and only if

| ${\frac {k_{i-1}}{x_{i}-x_{i-1}}}+\left({\frac {1}{x_{i}-x_{i-1}}}+{\frac {1}{x_{i+1}-x_{i}}}\right)2k_{i}+{\frac {k_{i+1}}{x_{i+1}-x_{i}}}=3\left({\frac {y_{i}-y_{i-1}}{{(x_{i}-x_{i-1})}^{2}}}+{\frac {y_{i+1}-y_{i}}{{(x_{i+1}-x_{i})}^{2}}}\right)$ |   | 15 |
|---|---|---|

for *i* = 1, ..., *n* − 1. The relations (**15**) are *n* − 1 linear equations for the *n* + 1 values *k*0, *k*1, ..., *kn*.

For the elastic rulers being the model for the spline interpolation, one has that to the left of the left-most "knot" and to the right of the right-most "knot" the ruler can move freely and will therefore take the form of a straight line with *q′′* = 0. As q′′ should be a continuous function of x, "natural splines" in addition to the *n* − 1 linear equations (**15**) should have

$q''_{1}(x_{0})=2{\frac {3(y_{1}-y_{0})-(k_{1}+2k_{0})(x_{1}-x_{0})}{{(x_{1}-x_{0})}^{2}}}=0,$

$q''_{n}(x_{n})=-2{\frac {3(y_{n}-y_{n-1})-(2k_{n}+k_{n-1})(x_{n}-x_{n-1})}{{(x_{n}-x_{n-1})}^{2}}}=0,$

i.e. that

| ${\frac {2}{x_{1}-x_{0}}}k_{0}+{\frac {1}{x_{1}-x_{0}}}k_{1}=3{\frac {y_{1}-y_{0}}{(x_{1}-x_{0})^{2}}},$ |   | 16 |
|---|---|---|

| ${\frac {1}{x_{n}-x_{n-1}}}k_{n-1}+{\frac {2}{x_{n}-x_{n-1}}}k_{n}=3{\frac {y_{n}-y_{n-1}}{(x_{n}-x_{n-1})^{2}}}.$ |   | 17 |
|---|---|---|

Eventually, (**15**) together with (**16**) and (**17**) constitute *n* + 1 linear equations that uniquely define the *n* + 1 parameters *k*0, *k*1, ..., *kn*.

There exist other end conditions, "clamped spline", which specifies the slope at the ends of the spline, and the popular "not-a-knot spline", which requires that the third derivative is also continuous at the *x*1 and *x**n*−1 points. For the "not-a-knot" spline, the additional equations will read:

$q'''_{1}(x_{1})=q'''_{2}(x_{1})\Rightarrow {\frac {1}{\Delta x_{1}^{2}}}k_{0}+\left({\frac {1}{\Delta x_{1}^{2}}}-{\frac {1}{\Delta x_{2}^{2}}}\right)k_{1}-{\frac {1}{\Delta x_{2}^{2}}}k_{2}=2\left({\frac {\Delta y_{1}}{\Delta x_{1}^{3}}}-{\frac {\Delta y_{2}}{\Delta x_{2}^{3}}}\right),$

$q'''_{n-1}(x_{n-1})=q'''_{n}(x_{n-1})\Rightarrow {\frac {1}{\Delta x_{n-1}^{2}}}k_{n-2}+\left({\frac {1}{\Delta x_{n-1}^{2}}}-{\frac {1}{\Delta x_{n}^{2}}}\right)k_{n-1}-{\frac {1}{\Delta x_{n}^{2}}}k_{n}=2\left({\frac {\Delta y_{n-1}}{\Delta x_{n-1}^{3}}}-{\frac {\Delta y_{n}}{\Delta x_{n}^{3}}}\right),$

where $\Delta x_{i}=x_{i}-x_{i-1},\ \Delta y_{i}=y_{i}-y_{i-1}$ .

## Example

In case of three points the values for $k_{0},k_{1},k_{2}$ are found by solving the tridiagonal linear equation system

${\begin{bmatrix}a_{11}&a_{12}&0\\a_{21}&a_{22}&a_{23}\\0&a_{32}&a_{33}\\\end{bmatrix}}{\begin{bmatrix}k_{0}\\k_{1}\\k_{2}\\\end{bmatrix}}={\begin{bmatrix}b_{1}\\b_{2}\\b_{3}\\\end{bmatrix}}$

with

$a_{11}={\frac {2}{x_{1}-x_{0}}},$

$a_{12}={\frac {1}{x_{1}-x_{0}}},$

$a_{21}={\frac {1}{x_{1}-x_{0}}},$

$a_{22}=2\left({\frac {1}{x_{1}-x_{0}}}+{\frac {1}{x_{2}-x_{1}}}\right),$

$a_{23}={\frac {1}{x_{2}-x_{1}}},$

$a_{32}={\frac {1}{x_{2}-x_{1}}},$

$a_{33}={\frac {2}{x_{2}-x_{1}}},$

$b_{1}=3{\frac {y_{1}-y_{0}}{(x_{1}-x_{0})^{2}}},$

$b_{2}=3\left({\frac {y_{1}-y_{0}}{{(x_{1}-x_{0})}^{2}}}+{\frac {y_{2}-y_{1}}{{(x_{2}-x_{1})}^{2}}}\right),$

$b_{3}=3{\frac {y_{2}-y_{1}}{(x_{2}-x_{1})^{2}}}.$

For the three points

$(-1,0.5),\ (0,0),\ (3,3),$

one gets that

$k_{0}=-0.6875,\ k_{1}=-0.1250,\ k_{2}=1.5625,$

and from (**10**) and (**11**) that

$a_{1}=k_{0}(x_{1}-x_{0})-(y_{1}-y_{0})=-0.1875,$

$b_{1}=-k_{1}(x_{1}-x_{0})+(y_{1}-y_{0})=-0.3750,$

$a_{2}=k_{1}(x_{2}-x_{1})-(y_{2}-y_{1})=-3.3750,$

$b_{2}=-k_{2}(x_{2}-x_{1})+(y_{2}-y_{1})=-1.6875.$

In the figure, the spline function consisting of the two cubic polynomials $q_{1}(x)$ and $q_{2}(x)$ given by (**9**) is displayed.

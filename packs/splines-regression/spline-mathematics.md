---
title: "Spline (mathematics)"
source: https://en.wikipedia.org/wiki/Spline_(mathematics)
domain: splines-regression
license: CC-BY-SA-4.0
tags: spline interpolation, B-spline, thin plate spline, regression spline
fetched: 2026-07-02
---

# Spline (mathematics)

In mathematics, a **spline** is a function defined piecewise by polynomials. In interpolating problems, spline interpolation is often preferred to polynomial interpolation because it yields similar results, even when using low degree polynomials, while avoiding Runge's phenomenon for higher degrees.

In the computer science subfields of computer-aided design and computer graphics, the term *spline* more frequently refers to a piecewise polynomial (parametric) curve. Splines are popular curves in these subfields because of the simplicity of their construction, their ease and accuracy of evaluation, and their capacity to approximate complex shapes through curve fitting and interactive curve design.

The term spline comes from the flexible spline devices used by shipbuilders and draftsmen to draw smooth shapes.

## Introduction

The term "spline" is used to refer to a wide class of functions that are used in applications requiring data interpolation and/or smoothing. The data may be either one-dimensional or multi-dimensional. Spline functions for interpolation are normally determined as the minimizers of suitable measures of roughness (for example integral squared curvature) subject to the interpolation constraints. Smoothing splines may be viewed as generalizations of interpolation splines where the functions are determined to minimize a weighted combination of the average squared approximation error over observed data and the roughness measure. For a number of meaningful definitions of the roughness measure, the spline functions are found to be finite dimensional in nature, which is the primary reason for their utility in computations and representation. For the rest of this section, we focus entirely on one-dimensional, polynomial splines and use the term "spline" in this restricted sense.

## History

According to Gerald Farin, B-splines were explored as early as the nineteenth century by Nikolai Lobachevsky at Kazan University in Russia.

Before computers were used, numerical calculations were done by hand. Although piecewise-defined functions like the sign function or step function were used, polynomials were generally preferred because they were easier to work with. Through the advent of computers, splines have gained importance. They were first used as a replacement for polynomials in interpolation, then as a tool to construct smooth and flexible shapes in computer graphics.

It is commonly accepted that the first mathematical reference to splines is the 1946 paper by Schoenberg, which is probably the first place that the word "spline" is used in connection with smooth, piecewise polynomial approximation. However, the ideas have their roots in the aircraft and shipbuilding industries. In the foreword to (Bartels et al., 1987), Robin Forrest describes "lofting", a technique used in the British aircraft industry during World War II to construct templates for airplanes by passing thin wooden strips (called "splines") through points laid out on the floor of a large design loft, a technique borrowed from ship-hull design. For years the practice of ship design had employed models to design in the small. The successful design was then plotted on graph paper and the key points of the plot were re-plotted on larger graph paper to full size. The thin wooden strips provided an interpolation of the key points into smooth curves. The strips would be held in place at discrete points (called "ducks" by Forrest; Schoenberg used "dogs" or "rats") and between these points would assume shapes of minimum strain energy. According to Forrest, one possible impetus for a mathematical model for this process was the potential loss of the critical design components for an entire aircraft should the loft be hit by an enemy bomb. This gave rise to "conic lofting", which used conic sections to model the position of the curve between the ducks. Conic lofting was replaced by what we would call splines in the early 1960s based on work by J. C. Ferguson at Boeing and (somewhat later) by Malcolm A. Sabin at British Aircraft Corporation.

The word "spline" was originally an East Anglian dialect word.

The use of splines for modeling automobile bodies seems to have several independent beginnings. Credit is claimed on behalf of de Casteljau at Citroën, Pierre Bézier at Renault, and Birkhoff, Garabedian, and de Boor at General Motors (see Birkhoff and de Boor, 1965), all for work occurring in the very early 1960s or late 1950s. At least one of de Casteljau's papers was published, but not widely, in 1959. De Boor's work at General Motors resulted in a number of papers being published in the early 1960s, including some of the fundamental work on B-splines.

Work was also being done at Pratt & Whitney Aircraft, where two of the authors of (Ahlberg et al., 1967) — the first book-length treatment of splines — were employed, and the David Taylor Model Basin, by Feodor Theilheimer. The work at General Motors is detailed nicely in (Birkhoff, 1990) and (Young, 1997). Davis (1997) summarizes some of this material.

## Definition

We begin by limiting our discussion to polynomials in one variable. In this case, a spline is a piecewise polynomial function. This function, call it S, takes values from an interval [*a*,*b*] and maps them to $\mathbb {R} ,$ the set of real numbers, $S:[a,b]\to \mathbb {R} .$ We want S to be piecewise defined. To accomplish this, let the interval [*a*,*b*] be covered by k ordered, disjoint subintervals,

${\begin{aligned}&[t_{i},t_{i+1}],\quad i=0,\ldots ,k-1\\[4pt]&[a,b]=[t_{0},t_{1})\cup [t_{1},t_{2})\cup \cdots \cup [t_{k-2},t_{k-1})\cup [t_{k-1},t_{k})\cup [t_{k}]\\[4pt]&a=t_{0}\leq t_{1}\leq \cdots \leq t_{k-1}\leq t_{k}=b\end{aligned}}$

On each of these k "pieces" of [*a*,*b*], we want to define a polynomial, call it Pi. $P_{i}:[t_{i},t_{i+1}]\to \mathbb {R} .$ On the ith subinterval of [*a*,*b*], S is defined by Pi,

${\begin{aligned}S(t)&=P_{0}(t),&&t_{0}\leq t<t_{1},\\[2pt]S(t)&=P_{1}(t),&&t_{1}\leq t<t_{2},\\&\vdots \\S(t)&=P_{k-1}(t),&&t_{k-1}\leq t\leq t_{k}.\end{aligned}}$

The given *k* + 1 points ti are called **knots**. The vector **t** = (*t*0, …, *tk*) is called a **knot vector** for the spline. If the knots are equidistantly distributed in the interval [*a*,*b*] we say the spline is **uniform**, otherwise we say it is **non-uniform**.

If the polynomial pieces Pi each have degree at most n, then the spline is said to be of **degree** ≤ *n* (or of **order** *n* + 1).

If $S\in C^{r_{i}}$ in a neighborhood of ti, then the spline is said to be of smoothness (at least) $C^{r_{i}}$ at ti. That is, at ti the two polynomial pieces *P**i*–1 and Pi share common derivative values from the derivative of order 0 (the function value) up through the derivative of order ri (in other words, the two adjacent polynomial pieces connect with **loss of smoothness** of at most *n* – *ri*)

${\begin{aligned}P_{i-1}^{(0)}(t_{i})&=P_{i}^{(0)}(t_{i}),\\[2pt]P_{i-1}^{(1)}(t_{i})&=P_{i}^{(1)}(t_{i}),\\\vdots &\\P_{i-1}^{(r_{i})}(t_{i})&=P_{i}^{(r_{i})}(t_{i}).\end{aligned}}$

A vector **r** = (*r*1, …, *r**k*–1) such that the spline has smoothness $C^{r_{i}}$ at ti for *i* = 1, …, *k* – 1 is called a **smoothness vector** for the spline.

Given a knot vector **t**, a degree n, and a smoothness vector **r** for **t**, one can consider the set of all splines of degree ≤ *n* having knot vector **t** and smoothness vector **r**. Equipped with the operation of adding two functions (pointwise addition) and taking real multiples of functions, this set becomes a real vector space. This **spline space** is commonly denoted by $S_{n}^{\mathbf {r} }(\mathbf {t} ).$

In the mathematical study of polynomial splines the question of what happens when two knots, say ti and *t**i*+1, are taken to approach one another and become coincident has an easy answer. The polynomial piece *Pi*(*t*) disappears, and the pieces *P**i*−1(*t*) and *P**i*+1(*t*) join with the sum of the smoothness losses for ti and *t**i*+1. That is, $S(t)\in C^{n-j_{i}-j_{i+1}}[t_{i}=t_{i+1}],$ where *ji* = *n* – *ri*. This leads to a more general understanding of a knot vector. The continuity loss at any point can be considered to be the result of **multiple knots** located at that point, and a spline type can be completely characterized by its degree n and its **extended** knot vector

$(t_{0},t_{1},\cdots ,t_{1},t_{2},\cdots ,t_{2},t_{3},\cdots ,t_{k-2},t_{k-1},\cdots ,t_{k-1},t_{k})$

where ti is repeated ji times for *i* = 1, …, *k* – 1.

A parametric curve on the interval [*a*,*b*] $G(t)={\bigl (}X(t),Y(t){\bigr )},\quad t\in [a,b]$ is a **spline curve** if both X and Y are spline functions of the same degree with the same extended knot vectors on that interval.

## Examples

Suppose the interval [*a*, *b*] is [0, 3] and the subintervals are [0, 1], [1, 2], [2, 3]. Suppose the polynomial pieces are to be of degree 2, and the pieces on [0, 1] and [1, 2] must join in value and first derivative (at *t* = 1) while the pieces on [1, 2] and [2, 3] join simply in value (at *t* = 2). This would define a type of spline *S*(*t*) for which

${\begin{aligned}S(t)&=P_{0}(t)=-1+4t-t^{2},&&0\leq t<1\\[2pt]S(t)&=P_{1}(t)=2t,&&1\leq t<2\\[2pt]S(t)&=P_{2}(t)=2-t+t^{2},&&2\leq t\leq 3\end{aligned}}$

would be a member of that type, and also

${\begin{aligned}S(t)&=P_{0}(t)=-2-2t^{2},&&0\leq t<1\\[2pt]S(t)&=P_{1}(t)=1-6t+t^{2},&&1\leq t<2\\[2pt]S(t)&=P_{2}(t)=-1+t-2t^{2},&&2\leq t\leq 3\end{aligned}}$

would be a member of that type. (Note: while the polynomial piece 2*t* is not quadratic, the result is still called a quadratic spline. This demonstrates that the degree of a spline is the maximum degree of its polynomial parts.) The extended knot vector for this type of spline would be (0, 1, 2, 2, 3).

The simplest spline has degree 0. It is also called a step function. The next most simple spline has degree 1. It is also called a **linear spline**. A closed linear spline (i.e, the first knot and the last are the same) in the plane is just a polygon.

A common spline is the **natural cubic spline**. A cubic spline has degree 3 with continuity *C*2, i.e. the values and first and second derivatives are continuous. Natural means that the second derivatives of the spline polynomials are zero at the endpoints of the interval of interpolation.

$S''(a)\,=S''(b)=0.$

Thus, the graph of the spline is a straight line outside of the interval, but still smooth.

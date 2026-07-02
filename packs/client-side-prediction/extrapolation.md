---
title: "Extrapolation"
source: https://en.wikipedia.org/wiki/Extrapolation
domain: client-side-prediction
license: CC-BY-SA-4.0
tags: client-side prediction, client prediction netcode, dead reckoning, entity interpolation
fetched: 2026-07-02
---

# Extrapolation

In mathematics, **extrapolation** is a type of estimation, beyond the original observation range, of the value of a variable on the basis of its relationship with another variable. It is similar to interpolation, which produces estimates between known observations, but extrapolation is subject to greater uncertainty and a higher risk of producing meaningless results. Extrapolation may also mean extension of a method, assuming similar methods will be applicable. Extrapolation may also apply to human experience to project, extend, or expand known experience into an area not known or previously experienced. By doing so, one makes an assumption of the unknown (for example, a driver may extrapolate road conditions beyond what is currently visible and these extrapolations may be correct or incorrect). The extrapolation method can be applied in the interior reconstruction problem.

## Method

A sound choice of which extrapolation method to apply relies on *a priori knowledge* of the process that created the existing data points. Some experts have proposed the use of causal forces in the evaluation of extrapolation methods. Crucial questions are, for example, if the data can be assumed to be continuous, smooth, possibly periodic, etc.

### Linear

Linear extrapolation means creating a tangent line at the end of the known data and extending it beyond that limit. Linear extrapolation will only provide good results when used to extend the graph of an approximately linear function or not too far beyond the known data.

If the two data points nearest the point $x_{*}$ to be extrapolated are $(x_{k-1},y_{k-1})$ and $(x_{k},y_{k})$ , linear extrapolation gives the function:

$y(x_{*})=y_{k-1}+{\frac {x_{*}-x_{k-1}}{x_{k}-x_{k-1}}}(y_{k}-y_{k-1}).$

(which is identical to linear interpolation if $x_{k-1}<x_{*}<x_{k}$ ). It is possible to include more than two points, and averaging the slope of the linear interpolant, by regression-like techniques, on the data points chosen to be included. This is similar to linear prediction.

### Polynomial

A polynomial curve can be created through the entire known data or just near the end (two points for linear extrapolation, three points for quadratic extrapolation, etc.). The resulting curve can then be extended beyond the end of the known data. Polynomial extrapolation is typically done by means of Lagrange interpolation or using Newton's method of finite differences to create a Newton series that fits the data. The resulting polynomial may be used to extrapolate the data.

High-order polynomial extrapolation must be used with due care. For the example data set and problem in the figure above, anything above order 1 (linear extrapolation) will possibly yield unusable values; an error estimate of the extrapolated value will grow with the degree of the polynomial extrapolation. This is related to Runge's phenomenon.

### Conic

A conic section can be created using five points near the end of the known data. If the conic section created is an ellipse or circle, when extrapolated it will loop back and rejoin itself. An extrapolated parabola or hyperbola will not rejoin itself, but may curve back relative to the X-axis. This type of extrapolation could be done with a conic sections template (on paper) or with a computer.

### French curve

French curve extrapolation is a method suitable for any distribution that has a tendency to be exponential, but with accelerating or decelerating factors. This method has been used successfully in providing forecast projections of the growth of HIV/AIDS in the UK since 1987 and variant CJD in the UK for a number of years. Another study has shown that extrapolation can produce the same quality of forecasting results as more complex forecasting strategies.

### Geometric Extrapolation with error prediction

Can be created with 3 points of a sequence and the "moment" or "index", this type of extrapolation have 100% accuracy in predictions in a big percentage of known series database (OEIS).

Example of extrapolation with error prediction :

${\text{sequence}}=[1,2,3,5]$

${f_{1}(x,y)={\frac {x}{y}}}$

$d_{1}=f_{1}(3,2)$

${d_{2}=f_{1}(5,3)}$

$m={\text{sequence}}(5)$

$n={\text{sequence}}(3)$

${\begin{aligned}{\text{f}}(m,n,d_{1},d_{2})&={\text{round}}\left((n\cdot d_{1}-m)+(m\cdot d_{2})\right)\\&={\text{round}}\left((3\times 1.5-5\right)+(5\times 1.66))=8\end{aligned}}$

## Quality

Typically, the quality of a particular method of extrapolation is limited by the assumptions about the function made by the method. If the method assumes the data are smooth, then a non-smooth function will be poorly extrapolated.

In terms of complex time series, some experts have discovered that extrapolation is more accurate when performed through the decomposition of causal forces.

Even for proper assumptions about the function, the extrapolation can diverge severely from the function. The classic example is truncated power series representations of sin(*x*) and related trigonometric functions. For instance, taking only data from near the *x* = 0, we may estimate that the function behaves as sin(*x*) ~ *x*. In the neighborhood of *x* = 0, this is an excellent estimate. Away from *x* = 0 however, the extrapolation moves arbitrarily away from the *x*-axis while sin(*x*) remains in the interval [−1, 1]. I.e., the error increases without bound.

Taking more terms in the power series of sin(*x*) around *x* = 0 will produce better agreement over a larger interval near *x* = 0, but will produce extrapolations that eventually diverge away from the *x*-axis even faster than the linear approximation.

This divergence is a specific property of extrapolation methods and is only circumvented when the functional forms assumed by the extrapolation method (inadvertently or intentionally due to additional information) accurately represent the nature of the function being extrapolated. For particular problems, this additional information may be available, but in the general case, it is impossible to satisfy all possible function behaviors with a workably small set of potential behavior.

## In the complex plane

In complex analysis, a problem of extrapolation may be converted into an interpolation problem by the change of variable ${\hat {z}}=1/z$ . This transform exchanges the part of the complex plane inside the unit circle with the part of the complex plane outside of the unit circle. In particular, the compactification point at infinity is mapped to the origin and vice versa. Care must be taken with this transform however, since the original function may have had "features", for example poles and other singularities, at infinity that were not evident from the sampled data.

Another problem of extrapolation is loosely related to the problem of analytic continuation, where (typically) a power series representation of a function is expanded at one of its points of convergence to produce a power series with a larger radius of convergence. In effect, a set of data from a small region is used to extrapolate a function onto a larger region.

Again, analytic continuation can be thwarted by function features that were not evident from the initial data.

Also, one may use sequence transformations like Padé approximants and Levin-type sequence transformations as extrapolation methods that lead to a summation of power series that are divergent outside the original radius of convergence. In this case, one often obtains rational approximants.

## Extrapolation arguments

Extrapolation arguments are informal and unquantified arguments which assert that something is probably true beyond the range of values for which it is known to be true. For example, we believe in the reality of what we see through magnifying glasses because it agrees with what we see with the naked eye but extends beyond it; we believe in what we see through light microscopes because it agrees with what we see through magnifying glasses but extends beyond it; and similarly for electron microscopes. Such arguments are widely used in biology in extrapolating from animal studies to humans and from pilot studies to a broader population.

Like slippery slope arguments, extrapolation arguments may be strong or weak depending on such factors as how far the extrapolation goes beyond the known range.

---
title: "Smoothing spline"
source: https://en.wikipedia.org/wiki/Smoothing_spline
domain: generalized-additive-models
license: CC-BY-SA-4.0
tags: generalized additive model, backfitting, smoothing spline, kernel smoother
fetched: 2026-07-02
---

# Smoothing spline

**Smoothing splines** are function estimates, ${\hat {f}}(x)$ , obtained from a set of noisy observations $y_{i}$ of the target $f(x_{i})$ , in order to balance a measure of goodness of fit of ${\hat {f}}(x_{i})$ to $y_{i}$ with a derivative based measure of the smoothness of ${\hat {f}}(x)$ . They provide a means for smoothing noisy $x_{i},y_{i}$ data. The most familiar example is the cubic smoothing spline, but there are many other possibilities, including for the case where x is a vector quantity.

## Cubic spline definition

Let $\{x_{i},Y_{i}:i=1,\dots ,n\}$ be a set of observations, modeled by the relation $Y_{i}=f(x_{i})+\epsilon _{i}$ where the $\epsilon _{i}$ are independent, zero mean random variables. The cubic smoothing spline estimate ${\hat {f}}$ of the function f is defined to be the unique minimizer, in the Sobolev space $W_{2}^{2}$ on a compact interval, of

$\sum _{i=1}^{n}\{Y_{i}-{\hat {f}}(x_{i})\}^{2}+\lambda \int {\hat {f}}^{\prime \prime }(x)^{2}\,dx.$

Remarks:

- $\lambda \geq 0$ is a smoothing parameter, controlling the trade-off between fidelity to the data and roughness of the function estimate. This is often estimated by generalized cross-validation, or by restricted marginal likelihood (REML) which exploits the link between spline smoothing and Bayesian estimation (the smoothing penalty can be viewed as being induced by a prior on the f ).
- The integral is often evaluated over the whole real line although it is also possible to restrict the range to that of $x_{i}$ .
- As $\lambda \to 0$ (no smoothing), the smoothing spline converges to the interpolating spline.
- As $\lambda \to \infty$ (infinite smoothing), the roughness penalty becomes paramount and the estimate converges to a linear least squares estimate.
- The roughness penalty based on the second derivative is the most common in modern statistics literature, although the method can easily be adapted to penalties based on other derivatives.
- In early literature, with equally-spaced ordered $x_{i}$ , second or third-order differences were used in the penalty, rather than derivatives. See also Whittaker–Henderson smoothing.
- The penalized sum of squares smoothing objective can be replaced by a *penalized likelihood* objective in which the sum of squares terms is replaced by another log-likelihood based measure of fidelity to the data. The sum of squares term corresponds to penalized likelihood with a Gaussian assumption on the $\epsilon _{i}$ .

## Derivation of the cubic smoothing spline

It is useful to think of fitting a smoothing spline in two steps:

1. First, derive the values ${\hat {f}}(x_{i});i=1,\ldots ,n$ .
2. From these values, derive ${\hat {f}}(x)$ for all *x*.

Now, treat the second step first.

Given the vector ${\hat {m}}=({\hat {f}}(x_{1}),\ldots ,{\hat {f}}(x_{n}))^{T}$ of fitted values, the sum-of-squares part of the spline criterion is fixed. It remains only to minimize $\int {\hat {f}}''(x)^{2}\,dx$ , and the minimizer is a natural cubic spline that interpolates the points $(x_{i},{\hat {f}}(x_{i}))$ . This interpolating spline is a linear operator, and can be written in the form

${\hat {f}}(x)=\sum _{i=1}^{n}{\hat {f}}(x_{i})f_{i}(x)$

where $f_{i}(x)$ are a set of spline basis functions. As a result, the roughness penalty has the form

$\int {\hat {f}}''(x)^{2}dx={\hat {m}}^{T}A{\hat {m}}.$

where the elements of A are $\int f_{i}''(x)f_{j}''(x)dx$ . The basis functions, and hence the matrix A , depend on the configuration of the predictor variables $x_{i}$ , but not on the responses $Y_{i}$ or ${\hat {m}}$ .

A is an $n\times n$ matrix given by $A=\Delta ^{T}W^{-1}\Delta$ .

$\Delta$ is an $(n-2)\times n$ matrix of second differences with elements:

$\Delta _{ii}=1/h_{i}$ , $\Delta _{i,i+1}=-1/h_{i}-1/h_{i+1}$ , $\Delta _{i,i+2}=1/h_{i+1}$

W is an $(n-2)\times (n-2)$ symmetric tri-diagonal matrix with elements:

$W_{i-1,i}=W_{i,i-1}=h_{i}/6$ , $W_{ii}=(h_{i}+h_{i+1})/3$ and $h_{i}=\xi _{i+1}-\xi _{i}$ , the distances between successive knots (or x values).

Now back to the first step. The penalized sum-of-squares can be written as

$\{Y-{\hat {m}}\}^{T}\{Y-{\hat {m}}\}+\lambda {\hat {m}}^{T}A{\hat {m}},$

where $Y=(Y_{1},\ldots ,Y_{n})^{T}$ .

Minimizing over ${\hat {m}}$ by differentiating against ${\hat {m}}$ . This results in: $-2\{Y-{\hat {m}}\}+2\lambda A{\hat {m}}=0$ and ${\hat {m}}=(I+\lambda A)^{-1}Y.$

## De Boor's approach

De Boor's approach exploits the same idea, of finding a balance between having a smooth curve and being close to the given data.

$p\sum _{i=1}^{n}\left({\frac {Y_{i}-{\hat {f}}\left(x_{i}\right)}{\delta _{i}}}\right)^{2}+\left(1-p\right)\int \left({\hat {f}}^{\left(m\right)}\left(x\right)\right)^{2}\,dx$

where p is a parameter called smooth factor and belongs to the interval $[0,1]$ , and $\delta _{i};i=1,\dots ,n$ are the quantities controlling the extent of smoothing (they represent the weight $\delta _{i}^{-2}$ of each point $Y_{i}$ ). In practice, since cubic splines are mostly used, m is usually 2 . The solution for $m=2$ was proposed by Christian Reinsch in 1967. For $m=2$ , when p approaches 1 , ${\hat {f}}$ converges to the "natural" spline interpolant to the given data. As p approaches 0 , ${\hat {f}}$ converges to a straight line (the smoothest curve). Since finding a suitable value of p is a task of trial and error, a redundant constant S was introduced for convenience. S is used to numerically determine the value of p so that the function ${\hat {f}}$ meets the following condition:

$\sum _{i=1}^{n}\left({\frac {Y_{i}-{\hat {f}}\left(x_{i}\right)}{\delta _{i}}}\right)^{2}\leq S$

The algorithm described by de Boor starts with $p=0$ and increases p until the condition is met. If $\delta _{i}$ is an estimation of the standard deviation for $Y_{i}$ , the constant S is recommended to be chosen in the interval $\left[n-{\sqrt {2n}},n+{\sqrt {2n}}\right]$ . Having $S=0$ means the solution is the "natural" spline interpolant. Increasing S means we obtain a smoother curve by getting farther from the given data.

## Multidimensional splines

There are two main classes of method for generalizing from smoothing with respect to a scalar x to smoothing with respect to a vector x . The first approach simply generalizes the spline smoothing penalty to the multidimensional setting. For example, if trying to estimate $f(x,z)$ we might use the Thin plate spline penalty and find the ${\hat {f}}(x,z)$ minimizing

$\sum _{i=1}^{n}\{y_{i}-{\hat {f}}(x_{i},z_{i})\}^{2}+\lambda \int \left[\left({\frac {\partial ^{2}{\hat {f}}}{\partial x^{2}}}\right)^{2}+2\left({\frac {\partial ^{2}{\hat {f}}}{\partial x\partial z}}\right)^{2}+\left({\frac {\partial ^{2}{\hat {f}}}{\partial z^{2}}}\right)^{2}\right]{\textrm {d}}x\,{\textrm {d}}z.$

The thin plate spline approach can be generalized to smoothing with respect to more than two dimensions and to other orders of differentiation in the penalty. As the dimension increases there are some restrictions on the smallest order of differential that can be used, but actually Duchon's original paper, gives slightly more complicated penalties that can avoid this restriction.

The thin plate splines are isotropic, meaning that if we rotate the $x,z$ co-ordinate system the estimate will not change, but also that we are assuming that the same level of smoothing is appropriate in all directions. This is often considered reasonable when smoothing with respect to spatial location, but in many other cases isotropy is not an appropriate assumption and can lead to sensitivity to apparently arbitrary choices of measurement units. For example, if smoothing with respect to distance and time an isotropic smoother will give different results if distance is measure in metres and time in seconds, to what will occur if we change the units to centimetres and hours.

The second class of generalizations to multi-dimensional smoothing deals directly with this scale invariance issue using tensor product spline constructions. Such splines have smoothing penalties with multiple smoothing parameters, which is the price that must be paid for not assuming that the same degree of smoothness is appropriate in all directions.

Smoothing splines are related to, but distinct from:

- *Regression splines*. In this method, the data is fitted to a set of spline basis functions with a reduced set of knots, typically by least squares. No roughness penalty is used. (See also multivariate adaptive regression splines.)
- *Penalized splines*. This combines the reduced knots of regression splines, with the roughness penalty of smoothing splines.
- *Thin plate splines* and Elastic maps method for manifold learning. This method combines the least squares penalty for approximation error with the bending and stretching penalty of the approximating manifold and uses the coarse discretization of the optimization problem.

## Source code

Source code for spline smoothing can be found in the examples from Carl de Boor's book *A Practical Guide to Splines*. The examples are in the Fortran programming language. The updated sources are available also on Carl de Boor's official site .

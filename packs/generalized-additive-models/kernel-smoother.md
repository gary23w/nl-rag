---
title: "Kernel smoother"
source: https://en.wikipedia.org/wiki/Kernel_smoother
domain: generalized-additive-models
license: CC-BY-SA-4.0
tags: generalized additive model, backfitting, smoothing spline, kernel smoother
fetched: 2026-07-02
---

# Kernel smoother

A **kernel smoother** is a statistical technique to estimate a real valued function $f:\mathbb {R} ^{p}\to \mathbb {R}$ as the weighted average of neighboring observed data. The weight is defined by the *kernel*, such that closer points are given higher weights. The estimated function is smooth, and the level of smoothness is set by a single parameter. Kernel smoothing is a type of weighted moving average.

## Definitions

Let $K_{h_{\lambda }}(X_{0},X)$ be a kernel defined by

$K_{h_{\lambda }}(X_{0},X)=D\left({\frac {\left\|X-X_{0}\right\|}{h_{\lambda }(X_{0})}}\right)$

where:

- $X,X_{0}\in \mathbb {R} ^{p}$
- $\left\|\cdot \right\|$ is the Euclidean norm
- $h_{\lambda }(X_{0})$ is a parameter (kernel radius)
- *D*(*t*) is typically a positive real valued function, whose value is decreasing (or not increasing) for the increasing distance between the *X* and *X*0.

Popular kernels used for smoothing include parabolic (Epanechnikov), tricube, and Gaussian kernels.

Let $Y(X):\mathbb {R} ^{p}\to \mathbb {R}$ be a continuous function of *X*. For each $X_{0}\in \mathbb {R} ^{p}$ , the Nadaraya-Watson kernel-weighted average (smooth *Y*(*X*) estimation) is defined by

${\hat {Y}}(X_{0})={\frac {\sum \limits _{i=1}^{N}{K_{h_{\lambda }}(X_{0},X_{i})Y(X_{i})}}{\sum \limits _{i=1}^{N}{K_{h_{\lambda }}(X_{0},X_{i})}}}$

where:

- *N* is the number of observed points
- *Y*(*X**i*) are the observations at *X**i* points.

In the following sections, we describe some particular cases of kernel smoothers.

## Gaussian kernel smoother

The Gaussian kernel is one of the most widely used kernels, and is expressed with the equation below.

$K(x^{*},x_{i})=\exp \left(-{\frac {(x^{*}-x_{i})^{2}}{2b^{2}}}\right)$

Here, b is the length scale for the input space.

## Nearest neighbor smoother

The *k*-nearest neighbor algorithm can be used for defining a ***k*-nearest neighbor smoother** as follows. For each point *X*0, take *m* nearest neighbors and estimate the value of *Y*(*X*0) by averaging the values of these neighbors.

Formally, $h_{m}(X_{0})=\left\|X_{0}-X_{[m]}\right\|$ , where $X_{[m]}$ is the *m*th closest to *X*0 neighbor, and

$D(t)={\begin{cases}1/m&{\text{if }}|t|\leq 1\\0&{\text{otherwise}}\end{cases}}$

In this example, *X* is one-dimensional. For each X0, the ${\hat {Y}}(X_{0})$ is an average value of 16 closest to *X*0 points (denoted by red).

## Kernel average smoother

The idea of the kernel average smoother is the following. For each data point *X*0, choose a constant distance size *λ* (kernel radius, or window width for *p* = 1 dimension), and compute a weighted average for all data points that are closer than $\lambda$ to *X*0 (the closer to *X*0 points get higher weights).

Formally, $h_{\lambda }(X_{0})=\lambda ={\text{constant}},$ and *D*(*t*) is one of the popular kernels.

For each *X*0 the window width is constant, and the weight of each point in the window is schematically denoted by the yellow figure in the graph. It can be seen that the estimation is smooth, but the boundary points are biased. The reason for that is the non-equal number of points (from the right and from the left to the *X*0) in the window, when the *X*0 is close enough to the boundary.

## Local regression

### Local linear regression

In the two previous sections we assumed that the underlying Y(X) function is locally constant, therefore we were able to use the weighted average for the estimation. The idea of local linear regression is to fit locally a straight line (or a hyperplane for higher dimensions), and not the constant (horizontal line). After fitting the line, the estimation ${\hat {Y}}(X_{0})$ is provided by the value of this line at *X*0 point. By repeating this procedure for each *X*0, one can get the estimation function ${\hat {Y}}(X)$ . Like in previous section, the window width is constant $h_{\lambda }(X_{0})=\lambda ={\text{constant}}.$ Formally, the local linear regression is computed by solving a weighted least square problem.

For one dimension (*p* = 1):

${\begin{aligned}&\min _{\alpha (X_{0}),\beta (X_{0})}\sum \limits _{i=1}^{N}{K_{h_{\lambda }}(X_{0},X_{i})\left(Y(X_{i})-\alpha (X_{0})-\beta (X_{0})X_{i}\right)^{2}}\\&\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\Downarrow \\&\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,{\hat {Y}}(X_{0})=\alpha (X_{0})+\beta (X_{0})X_{0}\\\end{aligned}}$

The closed form solution is given by:

${\hat {Y}}(X_{0})=\left(1,X_{0}\right)\left(B^{T}W(X_{0})B\right)^{-1}B^{T}W(X_{0})y$

where:

- $y=\left(Y(X_{1}),\dots ,Y(X_{N})\right)^{T}$
- $W(X_{0})=\operatorname {diag} \left(K_{h_{\lambda }}(X_{0},X_{i})\right)_{N\times N}$
- $B^{T}=\left({\begin{matrix}1&1&\dots &1\\X_{1}&X_{2}&\dots &X_{N}\\\end{matrix}}\right)$

The resulting function is smooth, and the problem with the biased boundary points is reduced.

Local linear regression can be applied to any-dimensional space, though the question of what is a local neighborhood becomes more complicated. It is common to use k nearest training points to a test point to fit the local linear regression. This can lead to high variance of the fitted function. To bound the variance, the set of training points should contain the test point in their convex hull (see Gupta et al. reference).

### Local polynomial regression

Instead of fitting locally linear functions, one can fit polynomial functions. For p=1, one should minimize:

${\underset {\alpha (X_{0}),\beta _{j}(X_{0}),j=1,...,d}{\mathop {\min } }}\,\sum \limits _{i=1}^{N}{K_{h_{\lambda }}(X_{0},X_{i})\left(Y(X_{i})-\alpha (X_{0})-\sum \limits _{j=1}^{d}{\beta _{j}(X_{0})X_{i}^{j}}\right)^{2}}$

with ${\hat {Y}}(X_{0})=\alpha (X_{0})+\sum \limits _{j=1}^{d}{\beta _{j}(X_{0})X_{0}^{j}}$

In general case (p>1), one should minimize:

${\begin{aligned}&{\hat {\beta }}(X_{0})={\underset {\beta (X_{0})}{\mathop {\arg \min } }}\,\sum \limits _{i=1}^{N}{K_{h_{\lambda }}(X_{0},X_{i})\left(Y(X_{i})-b(X_{i})^{T}\beta (X_{0})\right)}^{2}\\&b(X)=\left({\begin{matrix}1,&X_{1},&X_{2},...&X_{1}^{2},&X_{2}^{2},...&X_{1}X_{2}\,\,\,...\\\end{matrix}}\right)\\&{\hat {Y}}(X_{0})=b(X_{0})^{T}{\hat {\beta }}(X_{0})\\\end{aligned}}$

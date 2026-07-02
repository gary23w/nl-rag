---
title: "Cross-covariance"
source: https://en.wikipedia.org/wiki/Cross-covariance
domain: canonical-correlation
license: CC-BY-SA-4.0
tags: canonical correlation, cross-covariance, angles between flats, multivariate statistics
fetched: 2026-07-02
---

# Cross-covariance

In probability and statistics, given two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ , the **cross-covariance** is a function that gives the covariance of one process with the other at pairs of time points. With the usual notation $\operatorname {E}$ for the expectation operator, if the processes have the mean functions $\mu _{X}(t)=\operatorname {\operatorname {E} } [X_{t}]$ and $\mu _{Y}(t)=\operatorname {E} [Y_{t}]$ , then the cross-covariance is given by

$\operatorname {K} _{XY}(t_{1},t_{2})=\operatorname {cov} (X_{t_{1}},Y_{t_{2}})=\operatorname {E} [(X_{t_{1}}-\mu _{X}(t_{1}))(Y_{t_{2}}-\mu _{Y}(t_{2}))]=\operatorname {E} [X_{t_{1}}Y_{t_{2}}]-\mu _{X}(t_{1})\mu _{Y}(t_{2}).\,$

Cross-covariance is related to the more commonly used cross-correlation of the processes in question.

In the case of two random vectors $\mathbf {X} =(X_{1},X_{2},\ldots ,X_{p})^{\rm {T}}$ and $\mathbf {Y} =(Y_{1},Y_{2},\ldots ,Y_{q})^{\rm {T}}$ , the cross-covariance would be a $p\times q$ matrix $\operatorname {K} _{XY}$ (often denoted $\operatorname {cov} (X,Y)$ ) with entries $\operatorname {K} _{XY}(j,k)=\operatorname {cov} (X_{j},Y_{k}).\,$ Thus the term *cross-covariance* is used in order to distinguish this concept from the covariance of a random vector $\mathbf {X}$ , which is understood to be the matrix of covariances between the scalar components of $\mathbf {X}$ itself.

In signal processing, the cross-covariance is often called cross-correlation and is a measure of similarity of two signals, commonly used to find features in an unknown signal by comparing it to a known one. It is a function of the relative time between the signals, is sometimes called the *sliding dot product*, and has applications in pattern recognition and cryptanalysis.

## Cross-covariance of random vectors

## Cross-covariance of stochastic processes

The definition of cross-covariance of random vectors may be generalized to stochastic processes as follows:

### Definition

Let $\{X(t)\}$ and $\{Y(t)\}$ denote stochastic processes. Then the cross-covariance function of the processes $K_{XY}$ is defined by:

| $\operatorname {K} _{XY}(t_{1},t_{2}){\stackrel {\mathrm {def} }{=}}\ \operatorname {cov} (X_{t_{1}},Y_{t_{2}})=\operatorname {E} \left[\left(X(t_{1})-\mu _{X}(t_{1})\right)\left(Y(t_{2})-\mu _{Y}(t_{2})\right)\right]$ |   | Eq.1 |
|---|---|---|

where $\mu _{X}(t)=\operatorname {E} \left[X(t)\right]$ and $\mu _{Y}(t)=\operatorname {E} \left[Y(t)\right]$ .

If the processes are complex-valued stochastic processes, the second factor needs to be complex conjugated:

$\operatorname {K} _{XY}(t_{1},t_{2}){\stackrel {\mathrm {def} }{=}}\ \operatorname {cov} (X_{t_{1}},Y_{t_{2}})=\operatorname {E} \left[\left(X(t_{1})-\mu _{X}(t_{1})\right){\overline {\left(Y(t_{2})-\mu _{Y}(t_{2})\right)}}\right]$

### Definition for jointly WSS processes

If $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are a jointly wide-sense stationary, then the following are true:

$\mu _{X}(t_{1})=\mu _{X}(t_{2})\triangleq \mu _{X}$

for all

$t_{1},t_{2}$

,

$\mu _{Y}(t_{1})=\mu _{Y}(t_{2})\triangleq \mu _{Y}$

for all

$t_{1},t_{2}$

and

$\operatorname {K} _{XY}(t_{1},t_{2})=\operatorname {K} _{XY}(t_{2}-t_{1},0)$

for all

$t_{1},t_{2}$

By setting $\tau =t_{2}-t_{1}$ (the time lag, or the amount of time by which the signal has been shifted), we may define

$\operatorname {K} _{XY}(\tau )=\operatorname {K} _{XY}(t_{2}-t_{1})\triangleq \operatorname {K} _{XY}(t_{1},t_{2})$

.

The cross-covariance function of two jointly WSS processes is therefore given by:

| $\operatorname {K} _{XY}(\tau )=\operatorname {cov} (X_{t},Y_{t-\tau })=\operatorname {E} [(X_{t}-\mu _{X})(Y_{t-\tau }-\mu _{Y})]=\operatorname {E} [X_{t}Y_{t-\tau }]-\mu _{X}\mu _{Y}$ |   | Eq.2 |
|---|---|---|

which is equivalent to

$\operatorname {K} _{XY}(\tau )=\operatorname {cov} (X_{t+\tau },Y_{t})=\operatorname {E} [(X_{t+\tau }-\mu _{X})(Y_{t}-\mu _{Y})]=\operatorname {E} [X_{t+\tau }Y_{t}]-\mu _{X}\mu _{Y}$

.

### Uncorrelatedness

Two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are called **uncorrelated** if their covariance $\operatorname {K} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})$ is zero for all times. Formally:

$\left\{X_{t}\right\},\left\{Y_{t}\right\}{\text{ uncorrelated}}\quad \iff \quad \operatorname {K} _{\mathbf {X} \mathbf {Y} }(t_{1},t_{2})=0\quad \forall t_{1},t_{2}$

.

## Cross-covariance of deterministic signals

The cross-covariance is also relevant in signal processing where the cross-covariance between two wide-sense stationary random processes can be estimated by averaging the product of samples measured from one process and samples measured from the other (and its time shifts). The samples included in the average can be an arbitrary subset of all the samples in the signal (e.g., samples within a finite time window or a sub-sampling of one of the signals). For a large number of samples, the average converges to the true covariance.

Cross-covariance may also refer to a **"deterministic" cross-covariance** between two signals. This consists of summing over *all* time indices. For example, for discrete-time signals $f[k]$ and $g[k]$ the cross-covariance is defined as

$(f\star g)[n]\ {\stackrel {\mathrm {def} }{=}}\ \sum _{k\in \mathbb {Z} }{\overline {f[k]}}g[n+k]=\sum _{k\in \mathbb {Z} }{\overline {f[k-n]}}g[k]$

where the line indicates that the complex conjugate is taken when the signals are complex-valued.

For continuous functions $f(x)$ and $g(x)$ the (deterministic) cross-covariance is defined as

$(f\star g)(x)\ {\stackrel {\mathrm {def} }{=}}\ \int {\overline {f(t)}}g(x+t)\,dt=\int {\overline {f(t-x)}}g(t)\,dt$

.

### Properties

The (deterministic) cross-covariance of two continuous signals is related to the convolution by

$(f\star g)(t)=({\overline {f(-\tau )}}*g(\tau ))(t)$

and the (deterministic) cross-covariance of two discrete-time signals is related to the discrete convolution by

$(f\star g)[n]=({\overline {f[-k]}}*g[k])[n]$

.

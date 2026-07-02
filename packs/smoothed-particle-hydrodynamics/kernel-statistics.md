---
title: "Kernel (statistics)"
source: https://en.wikipedia.org/wiki/Kernel_(statistics)
domain: smoothed-particle-hydrodynamics
license: CC-BY-SA-4.0
tags: smoothed-particle hydrodynamics, meshfree methods, fluid simulation, multiphase flow
fetched: 2026-07-02
---

# Kernel (statistics)

The term **kernel** is used in statistical analysis to refer to a window function. The term "kernel" has several distinct meanings in different branches of statistics.

## Bayesian statistics

In statistics, especially in Bayesian statistics, the kernel of a probability density function (pdf) or probability mass function (pmf) is the form of the pdf or pmf in which any factors that are not functions of any of the variables in the domain are omitted. Note that such factors may well be functions of the parameters of the pdf or pmf. These factors form part of the normalization factor of the probability distribution, and are unnecessary in many situations. For example, in pseudo-random number sampling, most sampling algorithms ignore the normalization factor. In addition, in Bayesian analysis of conjugate prior distributions, the normalization factors are generally ignored during the calculations, and only the kernel considered. At the end, the form of the kernel is examined, and if it matches a known distribution, the normalization factor can be reinstated. Otherwise, it may be unnecessary (for example, if the distribution only needs to be sampled from).

For many distributions, the kernel can be written in closed form, but not the normalization constant.

An example is the normal distribution. Its probability density function is

$p(x|\mu ,\sigma ^{2})={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}$

and the associated kernel is

$p(x|\mu ,\sigma ^{2})\propto e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}$

Note that the factor in front of the exponential has been omitted, even though it contains the parameter $\sigma ^{2}$ , because it is not a function of the domain variable x .

## Pattern analysis

The kernel of a reproducing kernel Hilbert space is used in the suite of techniques known as kernel methods to perform tasks such as statistical classification, regression analysis, and cluster analysis on data in an implicit space. This usage is particularly common in machine learning.

## Nonparametric statistics

In nonparametric statistics, a kernel is a weighting function used in non-parametric estimation techniques. Kernels are used in kernel density estimation to estimate random variables' density functions, or in kernel regression to estimate the conditional expectation of a random variable. Kernels are also used in time series, in the use of the periodogram to estimate the spectral density where they are known as window functions. An additional use is in the estimation of a time-varying intensity for a point process where window functions (kernels) are convolved with time-series data.

Commonly, kernel widths must also be specified when running a non-parametric estimation.

### Definition

A kernel is a non-negative real-valued integrable function *K.* For most applications, it is desirable to define the function to satisfy two additional requirements:

- Normalization:

$\int _{-\infty }^{+\infty }K(u)\,du=1\,;$

- Even-function Symmetry:

$K(-u)=K(u){\mbox{ for all values of }}u\,.$

The first requirement ensures that the method of kernel density estimation results in a probability density function. The second requirement ensures that the average of the corresponding distribution is equal to that of the sample used.

If *K* is a kernel, then so is the function *K** defined by *K**(*u*) = λ*K*(λ*u*), where λ > 0. This can be used to select a scale that is appropriate for the data.

### Kernel functions in common use

Several types of kernel functions are commonly used: uniform, triangle, Epanechnikov, quartic (biweight), tricube, triweight, Gaussian, quadratic and cosine.

In the table below, if K is given with a bounded support, then $K(u)=0$ for values of *u* lying outside the support.

| Kernel Functions, *K*(*u*) | $\textstyle \int u^{2}K(u)du$ | $\textstyle \int K(u)^{2}du$ | Efficiency relative to the Epanechnikov kernel |   |   |
|---|---|---|---|---|---|
| Uniform ("rectangular window") | $K(u)={\frac {1}{2}}$ Support: $\|u\|\leq 1$ | "Boxcar function" | ${\frac {1}{3}}$ | ${\frac {1}{2}}$ | 92.9% |
| Triangular | $K(u)=(1-\|u\|)$ Support: $\|u\|\leq 1$ |   | ${\frac {1}{6}}$ | ${\frac {2}{3}}$ | 98.6% |
| Epanechnikov (parabolic) | $K(u)={\frac {3}{4}}(1-u^{2})$ Support: $\|u\|\leq 1$ |   | ${\frac {1}{5}}$ | ${\frac {3}{5}}$ | 100% |
| Quartic (biweight) | $K(u)={\frac {15}{16}}(1-u^{2})^{2}$ Support: $\|u\|\leq 1$ |   | ${\frac {1}{7}}$ | ${\frac {5}{7}}$ | 99.4% |
| Triweight | $K(u)={\frac {35}{32}}(1-u^{2})^{3}$ Support: $\|u\|\leq 1$ |   | ${\frac {1}{9}}$ | ${\frac {350}{429}}$ | 98.7% |
| Tricube | $K(u)={\frac {70}{81}}(1-{\left\|u\right\|}^{3})^{3}$ Support: $\|u\|\leq 1$ |   | ${\frac {35}{243}}$ | ${\frac {175}{247}}$ | 99.8% |
| Gaussian | $K(u)={\frac {1}{\sqrt {2\pi }}}e^{-{\frac {1}{2}}u^{2}}$ |   | $1\,$ | ${\frac {1}{2{\sqrt {\pi }}}}$ | 95.1% |
| Cosine | $K(u)={\frac {\pi }{4}}\cos \left({\frac {\pi }{2}}u\right)$ Support: $\|u\|\leq 1$ |   | $1-{\frac {8}{\pi ^{2}}}$ | ${\frac {\pi ^{2}}{16}}$ | 99.9% |
| Logistic | $K(u)={\frac {1}{e^{u}+2+e^{-u}}}$ |   | ${\frac {\pi ^{2}}{3}}$ | ${\frac {1}{6}}$ | 88.7% |
| Sigmoid function | $K(u)={\frac {2}{\pi }}{\frac {1}{e^{u}+e^{-u}}}$ |   | ${\frac {\pi ^{2}}{4}}$ | ${\frac {2}{\pi ^{2}}}$ | 84.3% |
| Silverman kernel | $K(u)={\frac {1}{2}}e^{-{\frac {\|u\|}{\sqrt {2}}}}\cdot \sin \left({\frac {\|u\|}{\sqrt {2}}}+{\frac {\pi }{4}}\right)$ |   | 0 | ${\frac {3{\sqrt {2}}}{16}}$ | not applicable |

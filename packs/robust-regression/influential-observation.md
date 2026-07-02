---
title: "Influential observation"
source: https://en.wikipedia.org/wiki/Influential_observation
domain: robust-regression
license: CC-BY-SA-4.0
tags: robust regression, M-estimator, robust statistics, influential observation
fetched: 2026-07-02
---

# Influential observation

In statistics, an **influential observation** is an observation for a statistical calculation whose deletion from the dataset would noticeably change the result of the calculation. In particular, in regression analysis an influential observation is one whose deletion has a large effect on the parameter estimates.

## Assessment

Various methods have been proposed for measuring influence. Assume an estimated regression $\mathbf {y} =\mathbf {X} \mathbf {b} +\mathbf {e}$ , where $\mathbf {y}$ is an *n*×1 column vector for the response variable, $\mathbf {X}$ is the *n*×*k* design matrix of explanatory variables (including a constant), $\mathbf {e}$ is the *n*×1 residual vector, and $\mathbf {b}$ is a *k*×1 vector of estimates of some population parameter $\mathbf {\beta } \in \mathbb {R} ^{k}$ . Also define $\mathbf {H} \equiv \mathbf {X} \left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \right)^{-1}\mathbf {X} ^{\mathsf {T}}$ , the projection matrix of $\mathbf {X}$ . Then we have the following measures of influence:

1. ${\text{DFBETA}}_{i}\equiv \mathbf {b} -\mathbf {b} _{(-i)}={\frac {\left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \right)^{-1}\mathbf {x} _{i}^{\mathsf {T}}e_{i}}{1-h_{ii}}}$ , where $\mathbf {b} _{(-i)}$ denotes the coefficients estimated with the *i*-th row $\mathbf {x} _{i}$ of $\mathbf {X}$ deleted, $h_{ii}=\mathbf {x} _{i}\left(\mathbf {X} ^{\mathsf {T}}\mathbf {X} \right)^{-1}\mathbf {x} _{i}^{\mathsf {T}}$ denotes the *i*-th value of matrix's $\mathbf {H}$ main diagonal. Thus DFBETA measures the difference in each parameter estimate with and without the influential point. There is a DFBETA for each variable and each observation (if there are *N* observations and *k* variables there are N·k DFBETAs). Table shows DFBETAs for the third dataset from Anscombe's quartet (bottom left chart in the figure):

| x | y | intercept | slope |
|---|---|---|---|
| 10.0 | 7.46 | -0.005 | -0.044 |
| 8.0 | 6.77 | -0.037 | 0.019 |
| **13.0** | **12.74** | **-357.910** | **525.268** |
| 9.0 | 7.11 | -0.033 | 0 |
| 11.0 | 7.81 | 0.049 | -0.117 |
| 14.0 | 8.84 | 0.490 | -0.667 |
| 6.0 | 6.08 | 0.027 | -0.021 |
| 4.0 | 5.39 | 0.241 | -0.209 |
| 12.0 | 8.15 | 0.137 | -0.231 |
| 7.0 | 6.42 | -0.020 | 0.013 |
| 5.0 | 5.73 | 0.105 | -0.087 |

1. DFFITS - difference in fits
2. Cook's *D* measures the effect of removing a data point on all the parameters combined.

## Outliers, leverage and influence

An outlier may be defined as a data point that differs markedly from other observations. A high-leverage point are observations made at extreme values of independent variables. Both types of atypical observations will force the regression line to be close to the point. In Anscombe's quartet, the bottom right image has a point with high leverage and the bottom left image has an outlying point.

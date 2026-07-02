---
title: "Dickey–Fuller test"
source: https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test
domain: time-series-econometrics
license: CC-BY-SA-4.0
tags: time series econometrics, autoregressive model, cointegration analysis, volatility clustering
fetched: 2026-07-02
---

# Dickey–Fuller test

In statistics, the **Dickey–Fuller test** tests the null hypothesis that a unit root is present in an autoregressive (AR) time series model. The alternative hypothesis is different depending on which version of the test is used, but is usually stationarity or trend-stationarity. The test is named after the statisticians David Dickey and Wayne Fuller, who developed it in 1979.

## Explanation

A simple AR model is

$y_{t}=\rho y_{t-1}+u_{t}\,$

where $y_{t}$ is the variable of interest, t is the time index, $\rho$ is a coefficient, and $u_{t}$ is the error term (assumed to be white noise). A unit root is present if $\rho =1$ . The model would be non-stationary in this case.

The regression model can be written as

$\Delta y_{t}=(\rho -1)y_{t-1}+u_{t}=\delta y_{t-1}+u_{t}\,$

where $\Delta$ is the first difference operator and $\delta \equiv \rho -1$ . This model can be estimated, and testing for a unit root is equivalent to testing $\delta =0$ . Since the test is done over the residual term rather than raw data, it is not possible to use standard t-distribution to provide critical values. Therefore, this statistic t has a specific distribution simply known as the Dickey–Fuller table.

There are three main versions of the test:

1. Test for a unit root:

$\Delta y_{t}=\delta y_{t-1}+u_{t}\,$

2. Test for a unit root with constant:

$\Delta y_{t}=a_{0}+\delta y_{t-1}+u_{t}\,$

3. Test for a unit root with constant and deterministic time trend:

$\Delta y_{t}=a_{0}+a_{1}t+\delta y_{t-1}+u_{t}\,$

Each version of the test has its own critical value which depends on the size of the sample. In each case, the null hypothesis is that there is a unit root, $\delta =0$ . The tests have low statistical power in that they often cannot distinguish between true unit-root processes ( $\delta =0$ ) and near unit-root processes ( $\delta$ is close to zero). This is called the "near observation equivalence" problem.

The intuition behind the test is as follows. If the series y is stationary (or trend-stationary), then it has a tendency to return to a constant (or deterministically trending) mean. Therefore, large values will tend to be followed by smaller values (negative changes), and small values by larger values (positive changes). Accordingly, the level of the series will be a significant predictor of next period's change, and will have a negative coefficient. If, on the other hand, the series is integrated, then positive changes and negative changes will occur with probabilities that do not depend on the current level of the series; in a random walk, where you are now does not affect which way you will go next.

It is notable that

$\Delta y_{t}=a_{0}+u_{t}\,$

may be rewritten as

$y_{t}=y_{0}+\sum _{i=1}^{t}u_{i}+a_{0}t$

with a deterministic trend coming from $a_{0}t$ and a stochastic intercept term coming from $y_{0}+\sum _{i=1}^{t}u_{i}$ , resulting in what is referred to as a *stochastic trend*.

There is also an extension of the Dickey–Fuller (DF) test called the augmented Dickey–Fuller test (ADF), which removes all the structural effects (autocorrelation) in the time series and then tests using the same procedure.

## Dealing with uncertainty about including the intercept and deterministic time trend terms

Which of the three main versions of the test should be used is not a minor issue. The decision is important for the size of the unit root test (the probability of rejecting the null hypothesis of a unit root when there is one) and the power of the unit root test (the probability of rejecting the null hypothesis of a unit root when there is not one). Inappropriate exclusion of the intercept or deterministic time trend term leads to bias in the coefficient estimate for *δ*, leading to the actual size for the unit root test not matching the reported one. If the time trend term is inappropriately excluded with the $a_{0}$ term estimated, then the power of the unit root test can be substantially reduced as a trend may be captured through the random walk with drift model. On the other hand, inappropriate inclusion of the intercept or time trend term reduces the power of the unit root test, and sometimes that reduced power can be substantial.

Use of prior knowledge about whether the intercept and deterministic time trend should be included is of course ideal but not always possible. When such prior knowledge is unavailable, various testing strategies (series of ordered tests) have been suggested, e.g. by Dolado, Jenkinson, and Sosvilla-Rivero (1990) and by Enders (2004), often with the ADF extension to remove autocorrelation. Elder and Kennedy (2001) present a simple testing strategy that avoids double and triple testing for the unit root that can occur with other testing strategies, and discuss how to use prior knowledge about the existence or not of long-run growth (or shrinkage) in *y*. Hacker and Hatemi-J (2010) provide simulation results on these matters, including simulations covering the Enders (2004) and Elder and Kennedy (2001) unit-root testing strategies. Simulation results are presented in Hacker (2010) which indicate that using an information criterion such as the Schwarz information criterion may be useful in determining unit root and trend status within a Dickey–Fuller framework.

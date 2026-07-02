---
title: "Cointegration"
source: https://en.wikipedia.org/wiki/Cointegration
domain: time-series-econometrics
license: CC-BY-SA-4.0
tags: time series econometrics, autoregressive model, cointegration analysis, volatility clustering
fetched: 2026-07-02
---

# Cointegration

In econometrics, **cointegration** is a statistical property that describes a long-run equilibrium relationship among two or more time series variables, even if the individual series are non-stationary (i.e., they contain stochastic trends). In such cases, the variables may drift in the short run, but their linear combination is stationary, implying that they move together over time and remain bound by a stable equilibrium.

More formally, if several time series are individually integrated of order *d* (meaning they require *d* differences to become stationary) but a linear combination of them is integrated of a lower order, then those time series are said to be cointegrated. That is, if (*X*,*Y*,*Z*) are each integrated of order *d*, and there exist coefficients *a*,*b*,*c* such that *aX* + *bY* + *cZ* is integrated of order less than d, then *X*, *Y*, and *Z* are cointegrated.

Cointegration is a crucial concept in time series analysis, particularly when dealing with variables that exhibit trends, such as macroeconomic data. In an influential paper, Charles Nelson and Charles Plosser (1982) provided statistical evidence that many US macroeconomic time series (like GNP, wages, employment, etc.) have stochastic trends.

## Introduction

If two or more series are individually integrated (in the time series sense) but some linear combination of them has a lower order of integration, then the series are said to be cointegrated. A common example is where the individual series are first-order integrated (⁠ $I(1)$ ⁠) but some (cointegrating) vector of coefficients exists to form a stationary linear combination of them.

### History

The first to introduce and analyse the concept of spurious—or nonsense—regression was Udny Yule in 1926. Before the 1980s, many economists used linear regressions on non-stationary time series data, which Nobel laureate Clive Granger and Paul Newbold showed to be a dangerous approach that could produce spurious correlation, since standard detrending techniques can result in data that are still non-stationary. Granger's 1987 paper with Robert Engle formalized the cointegrating vector approach, and coined the term.

For integrated ⁠ $I(1)$ ⁠ processes, Granger and Newbold showed that de-trending does not work to eliminate the problem of spurious correlation, and that the superior alternative is to check for co-integration. Two series with ⁠ $I(1)$ ⁠ trends can be co-integrated only if there is a genuine relationship between the two. Thus the standard current methodology for time series regressions is to check all-time series involved for integration. If there are ⁠ $I(1)$ ⁠ series on both sides of the regression relationship, then it is possible for regressions to give misleading results.

The possible presence of cointegration must be taken into account when choosing a technique to test hypotheses concerning the relationship between two variables having unit roots (i.e. integrated of at least order one). The usual procedure for testing hypotheses concerning the relationship between non-stationary variables was to run ordinary least squares (OLS) regressions on data which had been differenced. This method is biased if the non-stationary variables are cointegrated.

For example, regressing the consumption series for any country (e.g. Fiji) against the GNP for a randomly selected dissimilar country (e.g. Afghanistan) might give a high R-squared relationship (suggesting high explanatory power on Fiji's consumption from Afghanistan's GNP). This is called spurious regression: two integrated ⁠ $I(1)$ ⁠ series which are not directly causally related may nonetheless show a significant correlation.

## Tests

The six main methods for testing for cointegration are:

### Engle–Granger two-step method

If $x_{t}$ and $y_{t}$ both have order of integration *d*=1 and are cointegrated, then a linear combination of them must be stationary for some value of $\beta$ and $u_{t}$ . In other words:

$y_{t}-\beta x_{t}=u_{t}\,$

where $u_{t}$ is stationary.

If $\beta$ is known, we can test $u_{t}$ for stationarity with an augmented Dickey–Fuller test or Phillips–Perron test. If $\beta$ is unknown, we must first estimate it. This is typically done by using ordinary least squares (by regressing $y_{t}$ on $x_{t}$ and an intercept). Then, we can run an ADF test on $u_{t}$ . However, when $\beta$ is estimated, the critical values of this ADF test are non-standard, and increase in absolute value as more regressors are included.

If the variables are found to be cointegrated, a second-stage regression is conducted. This is a regression of $\Delta y_{t}$ on the lagged regressors, $\Delta x_{t}$ and the lagged residuals from the first stage, ${\hat {u}}_{t-1}$ . The second stage regression is given as: $\Delta y_{t}=\Delta x_{t}b+\alpha u_{t-1}+\varepsilon _{t}$

If the variables are not cointegrated (if we cannot reject the null of no cointegration when testing $u_{t}$ ), then $\alpha =0$ and we estimate a differences model: $\Delta y_{t}=\Delta x_{t}b+\varepsilon _{t}$

### Johansen test

The Johansen test is a test for cointegration that allows for more than one cointegrating relationship, unlike the Engle–Granger method, but this test is subject to asymptotic properties, i.e. large samples. If the sample size is too small then the results will not be reliable and one should use Auto Regressive Distributed Lags (ARDL).

### Phillips–Ouliaris cointegration test

Peter C. B. Phillips and Sam Ouliaris (1990) show that residual-based unit root tests applied to the estimated cointegrating residuals do not have the usual Dickey–Fuller distributions under the null hypothesis of no-cointegration. Because of the spurious regression phenomenon under the null hypothesis, the distribution of these tests have asymptotic distributions that depend on (1) the number of deterministic trend terms and (2) the number of variables with which co-integration is being tested. These distributions are known as Phillips–Ouliaris distributions and critical values have been tabulated. In finite samples, a superior alternative to the use of these asymptotic critical value is to generate critical values from simulations.

### Multicointegration

In practice, cointegration is often used for two ⁠ $I(1)$ ⁠ series, but it is more generally applicable and can be used for variables integrated of higher order (to detect correlated accelerations or other second-difference effects). **Multicointegration** extends the cointegration technique beyond two variables, and occasionally to variables integrated at different orders.

### Variable shifts in long time series

Tests for cointegration assume that the cointegrating vector is constant during the period of study. In reality, it is possible that the long-run relationship between the underlying variables change (shifts in the cointegrating vector can occur). The reason for this might be technological progress, economic crises, changes in the people's preferences and behaviour accordingly, policy or regime alteration, and organizational or institutional developments. This is especially likely to be the case if the sample period is long. To take this issue into account, tests have been introduced for cointegration with one unknown structural break, and tests for cointegration with two unknown breaks are also available.

### Bayesian inference

Several Bayesian methods have been proposed to compute the posterior distribution of the number of cointegrating relationships and the cointegrating linear combinations.

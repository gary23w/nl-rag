---
title: "Augmented Dickey–Fuller test"
source: https://en.wikipedia.org/wiki/Augmented_Dickey–Fuller_test
domain: cointegration
license: CC-BY-SA-4.0
tags: cointegration, error correction model, unit root, spurious relationship
fetched: 2026-07-02
---

# Augmented Dickey–Fuller test

In statistics, an **augmented Dickey–Fuller test** (**ADF**) tests the null hypothesis that a unit root is present in a time series sample. The alternative hypothesis depends on which version of the test is used, but is usually stationarity or trend-stationarity. It is an augmented version of the Dickey–Fuller test for a larger and more complicated set of time series models.

The augmented Dickey–Fuller (ADF) statistic, used in the test, is a negative number. The more negative it is, the stronger the rejection of the hypothesis that there is a unit root at some level of confidence.

## Testing procedure

The procedure for the ADF test is the same as for the Dickey–Fuller test but it is applied to the model

$\Delta y_{t}=\alpha +\beta t+\gamma y_{t-1}+\delta _{1}\Delta y_{t-1}+\cdots +\delta _{p-1}\Delta y_{t-p+1}+\varepsilon _{t},$

where $\alpha$ is a constant, $\beta$ the coefficient on a time trend and p the lag order of the autoregressive process. Imposing the constraints $\alpha =0$ and $\beta =0$ corresponds to modelling a random walk and using the constraint $\beta =0$ corresponds to modeling a random walk with a drift. Consequently, there are three main versions of the test, analogous those of the Dickey–Fuller test. (See that article for a discussion on dealing with uncertainty about including the intercept and deterministic time trend terms in the test equation.)

By including lags of the order *p*, the ADF formulation allows for higher-order autoregressive processes. This means that the lag length *p* must be determined in order to use the test. One approach to doing this is to test down from high orders and examine the *t*-values on coefficients. An alternative approach is to examine information criteria such as the Akaike information criterion, Bayesian information criterion or the Hannan–Quinn information criterion.

The unit root test is then carried out under the null hypothesis $\gamma =0$ against the alternative hypothesis of $\gamma <0.$ Once a value for the test statistic

$\mathrm {DF} _{\tau }={\frac {\hat {\gamma }}{\operatorname {SE} ({\hat {\gamma }})}}$

is computed, it can be compared to the relevant critical value for the Dickey–Fuller test. As this test is asymmetric, we are only concerned with negative values of our test statistic $\mathrm {DF} _{\tau }$ . If the calculated test statistic is less (more negative) than the critical value, then the null hypothesis of $\gamma =0$ is rejected and no unit root is present.

## Intuition

The intuition behind the test is that if the series is characterised by a unit root process, then the lagged level of the series ( $y_{t-1}$ ) will provide no relevant information in predicting the change in $y_{t}$ besides the one obtained in the lagged changes ( $\Delta y_{t-k}$ ). In this case, the $\gamma =0$ and null hypothesis is not rejected. In contrast, when the process has no unit root, it is stationary and hence exhibits reversion to the mean - so the lagged level will provide relevant information in predicting the change of the series and the null hypothesis of a unit root will be rejected.

## Examples

A model that includes a constant and a time trend is estimated using sample of 50 observations and yields the $\mathrm {DF} _{\tau }$ statistic of −4.57. This is more negative than the tabulated critical value of −3.50, so at the 95% level, the null hypothesis of a unit root will be rejected.

| Critical values for Dickey–Fuller *t*-distribution. |   |   |   |   |
|---|---|---|---|---|
|   | Without trend | With trend |   |   |
| Sample size | 1% | 5% | 1% | 5% |
| T = 25 | −3.75 | −3.00 | −4.38 | −3.60 |
| T = 50 | −3.58 | −2.93 | −4.15 | −3.50 |
| T = 100 | −3.51 | −2.89 | −4.04 | −3.45 |
| T = 250 | −3.46 | −2.88 | −3.99 | −3.43 |
| T = 500 | −3.44 | −2.87 | −3.98 | −3.42 |
| T = ∞ | −3.43 | −2.86 | −3.96 | −3.41 |
| Source |   |   |   |   |

## Alternatives

There are alternative unit root tests such as the Phillips–Perron test (PP) or the ADF-GLS test procedure (ERS) developed by Elliott, Rothenberg and Stock (1996).

## Software implementations

- R:
  - package `forecast` function `ndiffs` handles multiple popular unit root tests
  - package `tseries` function `adf.test`
  - package `fUnitRoots` function `adfTest`
  - package `urca` function ur.df
- Gretl
- Matlab
  - the Econometrics Toolbox function `adfTest`
  - the Spatial Econometrics toolbox (free)
- SAS `PROC ARIMA`
- Stata command `dfuller`
- EViews the `Unit Root Test`
- Python
  - package `statsmodels` function `adfuller`
  - package `ARCH`
- Java project `SuanShu` package `com.numericalmethod.suanshu.stats.test.timeseries.adf` class `AugmentedDickeyFuller`
- Julia package `HypothesisTests` function `ADFTest`

---
title: "Unit root"
source: https://en.wikipedia.org/wiki/Unit_root
domain: time-series-econometrics
license: CC-BY-SA-4.0
tags: time series econometrics, autoregressive model, cointegration analysis, volatility clustering
fetched: 2026-07-02
---

# Unit root

In probability theory and statistics, a **unit root** is a property of certain stochastic processes (such as a random walk) that can create challenges for statistical inference in time series models. A linear stochastic process contains a unit root if 1 is a solution to its characteristic equation.

Processes with a unit root are non-stationary, because they do not necessarily exhibit a deterministic trend.

If the other roots of the characteristic equation lie inside the unit circle—that is, have a modulus (absolute value) less than one—then the first difference of the process will be stationary; otherwise, the process will need to be differenced multiple times to become stationary. If there are *d* unit roots, the process will have to be differenced *d* times in order to make it stationary. Due to this characteristic, unit root processes are also called **difference stationary.**

Unit root processes may sometimes be confused with trend-stationary processes; while they share many properties, they are different in many aspects. It is possible for a time series to be non-stationary, yet have no unit root and be trend-stationary. In both unit root and trend-stationary processes, the mean can be growing or decreasing over time; however, in the presence of a shock, trend-stationary processes are mean-reverting (i.e. transitory, the time series will converge again towards the growing mean, which was not affected by the shock) while unit-root processes have a permanent impact on the mean (i.e. no convergence over time).

If a root of the process's characteristic equation is larger than 1, then it is called an **explosive process**, even though such processes are sometimes inaccurately called unit roots processes.

The presence of a unit root can be tested using a unit root test.

## Definition

Consider a discrete-time stochastic process $(y_{t},t=1,2,3,\ldots )$ , and suppose that it can be written as an autoregressive process of order *p*:

$y_{t}=a_{1}y_{t-1}+a_{2}y_{t-2}+\cdots +a_{p}y_{t-p}+\varepsilon _{t}.$

Here, $(\varepsilon _{t},t=0,1,2,\ldots ,)$ is a serially uncorrelated, zero-mean stochastic process with constant variance $\sigma ^{2}$ . For convenience, assume $y_{0}=0$ . If $m=1$ is a root of the characteristic equation, of multiplicity 1:

$m^{p}-m^{p-1}a_{1}-m^{p-2}a_{2}-\cdots -a_{p}=0$

then the stochastic process has a **unit root** or, alternatively, is integrated of order one, denoted $I(1)$ . If *m* = 1 is a root of multiplicity *r*, then the stochastic process is integrated of order *r*, denoted *I*(*r*).

## Example

The first order autoregressive model, $y_{t}=a_{1}y_{t-1}+\varepsilon _{t}$ , has a unit root when $a_{1}=1$ . In this example, the characteristic equation is $m-a_{1}=0$ . The root of the equation is $m=1$ .

If the process has a unit root, then it is a non-stationary time series. That is, the moments of the stochastic process depend on t . To illustrate the effect of a unit root, we can consider the first order case, starting from *y*0 = 0:

$y_{t}=y_{t-1}+\varepsilon _{t}.$

By repeated substitution, we can write $y_{t}=y_{0}+\sum _{j=1}^{t}\varepsilon _{j}$ . Then the variance of $y_{t}$ is given by:

$\operatorname {Var} (y_{t})=\sum _{j=1}^{t}\sigma ^{2}=t\sigma ^{2}.$

The variance depends on *t* since $\operatorname {Var} (y_{1})=\sigma ^{2}$ , while $\operatorname {Var} (y_{2})=2\sigma ^{2}$ . The variance of the series is diverging to infinity with *t*.

There are various tests to check for the existence of a unit root, some of them are given by:

1. The Dickey–Fuller test (DF) or augmented Dickey–Fuller (ADF) tests
2. Testing the significance of more than one coefficients (f-test)
3. The Phillips–Perron test (PP)
4. Dickey Pantula test

In addition to autoregressive (AR) and autoregressive–moving-average (ARMA) models, other important models arise in regression analysis where the model errors may themselves have a time series structure and thus may need to be modelled by an AR or ARMA process that may have a unit root, as discussed above. The finite sample properties of regression models with first order ARMA errors, including unit roots, have been analyzed.

## Estimation when a unit root may be present

Often, ordinary least squares (OLS) is used to estimate the slope coefficients of the autoregressive model. Use of OLS relies on the stochastic process being stationary. When the stochastic process is non-stationary, the use of OLS can produce invalid estimates. Granger and Newbold called such estimates 'spurious regression' results: high R2 values and high t-ratios yielding results with no real (in their context, economic) meaning.

To estimate the slope coefficients, one should first conduct a unit root test, whose null hypothesis is that a unit root is present. If that hypothesis is rejected, one can use OLS. However, if the presence of a unit root is not rejected, then one should apply the difference operator to the series. If another unit root test shows the differenced time series to be stationary, OLS can then be applied to this series to estimate the slope coefficients.

For example, in the AR(1) case, $\Delta y_{t}=y_{t}-y_{t-1}=\varepsilon _{t}$ is stationary.

In the AR(2) case, $y_{t}=a_{1}y_{t-1}+a_{2}y_{t-2}+\varepsilon _{t}$ can be written as $(1-\lambda _{1}L)(1-\lambda _{2}L)y_{t}=\varepsilon _{t}$ where L is a lag operator that decreases the time index of a variable by one period: $Ly_{t}=y_{t-1}$ . If $\lambda _{2}=1$ , the model has a unit root and we can define $z_{t}=\Delta y_{t}$ ; then

$z_{t}=\lambda _{1}z_{t-1}+\varepsilon _{t}$

is stationary if $|\lambda _{1}|<1$ . OLS can be used to estimate the slope coefficient, $\lambda _{1}$ .

If the process has multiple unit roots, the difference operator can be applied multiple times.

## Properties and characteristics of unit-root processes

- Shocks to a unit root process have permanent effects which do not decay as they would if the process were stationary
- As noted above, a unit root process has a variance that depends on t, and diverges to infinity
- If it is known that a series has a unit root, the series can be differenced to render it stationary. For example, if a series $Y_{t}$ is I(1), the series $\Delta Y_{t}=Y_{t}-Y_{t-1}$ is I(0) (stationary). It is hence called a *difference stationary* series.

## Unit root hypothesis

Economists debate whether various economic statistics, especially output, have a unit root or are trend-stationary. A unit root process with drift is given in the first-order case by

$y_{t}=y_{t-1}+c+e_{t}$

where *c* is a constant term referred to as the "drift" term, and $e_{t}$ is white noise. Any non-zero value of the noise term, occurring for only one period, will permanently affect the value of $y_{t}$ as shown in the graph, so deviations from the line $y_{t}=a+ct$ are non-stationary; there is no reversion to any trend line. In contrast, a trend-stationary process is given by

$y_{t}=k\cdot t+u_{t}$

where *k* is the slope of the trend and $u_{t}$ is noise (white noise in the simplest case; more generally, noise following its own stationary autoregressive process). Here any transient noise will not alter the long-run tendency for $y_{t}$ to be on the trend line, as also shown in the graph. This process is said to be trend-stationary because deviations from the trend line are stationary.

The issue is particularly popular in the literature on business cycles. Research on the subject began with Nelson and Plosser whose paper on GNP and other output aggregates failed to reject the unit root hypothesis for these series. Since then, a debate—entwined with technical disputes on statistical methods—has ensued. Some economists argue that GDP has a unit root or structural break, implying that economic downturns result in permanently lower GDP levels in the long run. Other economists argue that GDP is trend-stationary: That is, when GDP dips below trend during a downturn it later returns to the level implied by the trend so that there is no permanent decrease in output. While the literature on the unit root hypothesis may consist of arcane debate on statistical methods, the hypothesis carries significant practical implications for economic forecasts and policies.

---
title: "Partial autocorrelation function"
source: https://en.wikipedia.org/wiki/Partial_autocorrelation_function
domain: time-series-arima
license: CC-BY-SA-4.0
tags: ARIMA, autoregressive model, moving-average model, Box Jenkins
fetched: 2026-07-02
---

# Partial autocorrelation function

In time series analysis, the **partial autocorrelation function** (**PACF**) gives the partial correlation of a stationary time series with its own lagged values, regressed the values of the time series at all shorter lags. It contrasts with the autocorrelation function, which does not control for other lags.

This function plays an important role in data analysis aimed at identifying the extent of the lag in an autoregressive (AR) model. The use of this function was introduced as part of the Box–Jenkins approach to time series modelling, whereby plotting the partial autocorrelative functions one could determine the appropriate lags **p** in an AR (**p**) model or in an extended ARIMA (**p**,**d**,**q**) model.

## Definition

Given a time series $z_{t}$ , the partial autocorrelation of lag k , denoted $\phi _{k,k}$ , is the autocorrelation between $z_{t}$ and $z_{t+k}$ with the linear dependence of $z_{t}$ on $z_{t+1}$ through $z_{t+k-1}$ removed. Equivalently, it is the autocorrelation between $z_{t}$ and $z_{t+k}$ that is not accounted for by lags 1 through $k-1$ , inclusive. $\phi _{1,1}=\operatorname {corr} (z_{t+1},z_{t}),{\text{ for }}k=1,$ $\phi _{k,k}=\operatorname {corr} (z_{t+k}-{\hat {z}}_{t+k},\,z_{t}-{\hat {z}}_{t}),{\text{ for }}k\geq 2,$ where ${\hat {z}}_{t+k}$ and ${\hat {z}}_{t}$ are linear combinations of $\{z_{t+1},z_{t+2},...,z_{t+k-1}\}$ that minimize the mean squared error of $z_{t+k}$ and $z_{t}$ respectively. For stationary processes, the coefficients in ${\hat {z}}_{t+k}$ and ${\hat {z}}_{t}$ are the same, but reversed: ${\hat {z}}_{t+k}=\beta _{1}z_{t+k-1}+\cdots +\beta _{k-1}z_{t+1}\qquad {\text{and}}\qquad {\hat {z}}_{t}=\beta _{1}z_{t+1}+\cdots +\beta _{k-1}z_{t+k-1}.$

## Calculation

The theoretical partial autocorrelation function of a stationary time series can be calculated by using the Durbin–Levinson Algorithm: $\phi _{n,n}={\frac {\rho (n)-\sum _{k=1}^{n-1}\phi _{n-1,k}\rho (n-k)}{1-\sum _{k=1}^{n-1}\phi _{n-1,k}\rho (k)}}$ where $\phi _{n,k}=\phi _{n-1,k}-\phi _{n,n}\phi _{n-1,n-k}$ for $1\leq k\leq n-1$ and $\rho (n)$ is the autocorrelation function.

The formula above can be used with sample autocorrelations to find the sample partial autocorrelation function of any given time series.

## Examples

The following table summarizes the partial autocorrelation function of different models:

| Model | PACF |
|---|---|
| White noise | The partial autocorrelation is 0 for all lags. |
| Autoregressive model | The partial autocorrelation for an AR(*p*) model is nonzero for lags less than or equal to *p* and 0 for lags greater than *p*. |
| Moving-average model | If $\phi _{1,1}>0$ , the partial autocorrelation oscillates to 0. |
| If $\phi _{1,1}<0$ , the partial autocorrelation geometrically decays to 0. |   |
| Autoregressive–moving-average model | An ARMA(*p*, *q*) model's partial autocorrelation geometrically decays to 0 but only after lags greater than *p*. |

The behavior of the partial autocorrelation function mirrors that of the autocorrelation function for autoregressive and moving-average models. For example, the partial autocorrelation function of an AR(*p*) series cuts off after lag *p* similar to the autocorrelation function of an MA(*q*) series with lag *q*. In addition, the autocorrelation function of an AR(*p*) process tails off just like the partial autocorrelation function of an MA(*q*) process.

## Autoregressive model identification

Partial autocorrelation is a commonly used tool for identifying the order of an autoregressive model. As previously mentioned, the partial autocorrelation of an AR(*p*) process is zero at lags greater than *p*. If an AR model is determined to be appropriate, then the sample partial autocorrelation plot is examined to help identify the order.

The partial autocorrelation of lags greater than *p* for an AR(*p*) time series are approximately independent and normal with a mean of 0. Therefore, a confidence interval can be constructed by dividing a selected z-score by ${\sqrt {n}}$ . Lags with partial autocorrelations outside of the confidence interval indicate that the AR model's order is likely greater than or equal to the lag. Plotting the partial autocorrelation function and drawing the lines of the confidence interval is a common way to analyze the order of an AR model. To evaluate the order, one examines the plot to find the lag after which the partial autocorrelations are all within the confidence interval. This lag is determined to likely be the AR model's order.

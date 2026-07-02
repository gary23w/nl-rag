---
title: "Moving-average model"
source: https://en.wikipedia.org/wiki/Moving-average_model
domain: time-series-arima
license: CC-BY-SA-4.0
tags: ARIMA, autoregressive model, moving-average model, Box Jenkins
fetched: 2026-07-02
---

# Moving-average model

In time series analysis, the **moving-average model** (**MA model**), also called the **moving-average process**, is a standard approach for modeling univariate time series.

An MA model expresses the current value of a time series as a linear function of current and past random shocks (error terms) with finite lag length. In contrast to an autoregressive model, which regresses the variable on its past values, the moving-average model relies solely on the dependency structure of the error terms.

Together with the autoregressive (AR) model, the moving-average model is a special case and key component of the more general ARMA and ARIMA models of time series, which have a more complicated stochastic structure. Contrary to the AR model, the finite MA model is always stationary.

The moving-average model should not be confused with the moving average, a distinct concept despite some similarities.

## Definition

The notation MA(*q*) refers to the moving average model of order *q*:

$X_{t}=\mu +\varepsilon _{t}+\theta _{1}\varepsilon _{t-1}+\cdots +\theta _{q}\varepsilon _{t-q}=\mu +\sum _{i=1}^{q}\theta _{i}\varepsilon _{t-i}+\varepsilon _{t},$

where $\mu$ is the mean of the series, the $\theta _{1},...,\theta _{q}$ are the coefficients of the model and $\varepsilon _{t},\varepsilon _{t-1},...,\varepsilon _{t-q}$ are the error terms. The value of *q* is called the order of the MA model. This can be equivalently written in terms of the backshift operator *B* as

$X_{t}=\mu +(1+\theta _{1}B+\cdots +\theta _{q}B^{q})\varepsilon _{t}.$

Thus, a moving-average model is conceptually a linear regression of the current value of the series against current and previous (observed) white noise error terms or random shocks. The random shocks at each point are assumed to be mutually independent and to come from the same distribution, typically a normal distribution, with location at zero and constant scale.

## Interpretation

The moving-average model is essentially a finite impulse response filter applied to white noise, with some additional interpretation placed on it. The role of the random shocks in the MA model differs from their role in the autoregressive (AR) model in two ways. First, they are propagated to future values of the time series directly: for example, $\varepsilon _{t-1}$ appears directly on the right side of the equation for $X_{t}$ . In contrast, in an AR model $\varepsilon _{t-1}$ does not appear on the right side of the $X_{t}$ equation, but it does appear on the right side of the $X_{t-1}$ equation, and $X_{t-1}$ appears on the right side of the $X_{t}$ equation, giving only an indirect effect of $\varepsilon _{t-1}$ on $X_{t}$ . Second, in the MA model a shock affects X values only for the current period and *q* periods into the future; in contrast, in the AR model a shock affects X values infinitely far into the future, because $\varepsilon _{t}$ affects $X_{t}$ , which affects $X_{t+1}$ , which affects $X_{t+2}$ , and so on forever (see Impulse response).

## Fitting the model

Fitting a moving-average model is generally more complicated than fitting an autoregressive model. This is because the lagged error terms are not observable. This means that iterative non-linear fitting procedures need to be used in place of linear least squares. Moving average models are linear combinations of past white noise terms, while autoregressive models are linear combinations of past time series values. ARMA models are more complicated than pure AR and MA models, as they combine both autoregressive and moving average components.

The autocorrelation function (ACF) of an MA(*q*) process is zero at lag *q* + 1 and greater. Therefore, we determine the appropriate maximum lag for the estimation by examining the sample autocorrelation function to see where it becomes insignificantly different from zero for all lags beyond a certain lag, which is designated as the maximum lag *q*.

Sometimes the ACF and partial autocorrelation function (PACF) will suggest that an MA model would be a better model choice and sometimes both AR and MA terms should be used in the same model (see Box–Jenkins method).

Autoregressive Integrated Moving Average (ARIMA) models are an alternative to segmented regression that can also be used for fitting a moving-average model.

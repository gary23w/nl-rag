---
title: "Stationary process"
source: https://en.wikipedia.org/wiki/Stationary_process
domain: time-series-arima
license: CC-BY-SA-4.0
tags: ARIMA, autoregressive model, moving-average model, Box Jenkins
fetched: 2026-07-02
---

# Stationary process

In mathematics and statistics, a **stationary process** (also called a **strict/strictly stationary process** or **strong/strongly stationary process**) is a stochastic process whose statistical properties, such as mean and variance, do not change over time. More formally, the joint probability distribution of the process remains the same when shifted in time. This implies that the process is statistically consistent across different time periods. Because many statistical procedures in time series analysis assume stationarity, non-stationary data are frequently transformed to achieve stationarity before analysis.

A common cause of non-stationarity is a trend in the mean, which can be due to either a unit root or a deterministic trend. In the case of a unit root, stochastic shocks have permanent effects, and the process is not mean-reverting. With a deterministic trend, the process is called trend-stationary, and shocks have only transitory effects, with the variable tending towards a deterministically evolving mean. A trend-stationary process is not strictly stationary but can be made stationary by removing the trend. Similarly, processes with unit roots can be made stationary through differencing.

Another type of non-stationary process, distinct from those with trends, is a cyclostationary process, which exhibits cyclical variations over time.

Strict stationarity, as defined above, can be too restrictive for many applications. Therefore, other forms of stationarity, such as **wide-sense stationarity** or **⁠ N ⁠th-order stationarity**, are often used. The definitions for different kinds of stationarity are not consistent among different authors (see Other terminology).

## Strict-sense stationarity

### Definition

Formally, let $\left\{X_{t}\right\}$ be a stochastic process and let $F_{X}(x_{t_{1}+\tau },\ldots ,x_{t_{n}+\tau })$ represent the cumulative distribution function of the unconditional (i.e., with no reference to any particular starting value) joint distribution of $\left\{X_{t}\right\}$ at times ⁠ $t_{1}+\tau ,\ldots ,t_{n}+\tau$ ⁠. Then, $\left\{X_{t}\right\}$ is said to be **strictly stationary**, **strongly stationary** or **strict-sense stationary** if

| $F_{X}(x_{t_{1}+\tau },\ldots ,x_{t_{n}+\tau })=F_{X}(x_{t_{1}},\ldots ,x_{t_{n}})\quad {\text{for all }}\tau ,t_{1},\ldots ,t_{n}\in \mathbb {R} {\text{ and for all }}n\in \mathbb {N} _{>0}$ |   | Eq.1 |
|---|---|---|

Since $\tau$ does not affect ⁠ $F_{X}(\cdot )$ ⁠, $F_{X}$ is independent of time.

### Examples

White noise is the simplest example of a stationary process.

An example of a discrete-time stationary process where the sample space is also discrete (so that the random variable may take one of ⁠ N ⁠ possible values) is a Bernoulli scheme. Other examples of a discrete-time stationary process with continuous sample space include some autoregressive and moving average processes that are both subsets of the autoregressive moving average model. Models with a non-trivial autoregressive component may be either stationary or non-stationary, depending on the parameter values, and important non-stationary special cases are where unit roots exist in the model.

#### Example 1

Let Y be any scalar random variable, and define a time-series $\left\{X_{t}\right\}$ by

$X_{t}=Y\qquad {\text{ for all }}t.$

Then $\left\{X_{t}\right\}$ is a stationary time series, for which realisations consist of a series of constant values, with a different constant value for each realisation. A law of large numbers does not apply on this case, as the limiting value of an average from a single realisation takes the random value determined by ⁠ Y ⁠, rather than taking the expected value of ⁠ Y ⁠.

The time average of $X_{t}$ does not converge since the process is not ergodic.

#### Example 2

As a further example of a stationary process for which any single realisation has an apparently noise-free structure, let Y have a uniform distribution on $[0,2\pi ]$ and define the time series $\left\{X_{t}\right\}$ by

$X_{t}=\cos(t+Y)\quad {\text{ for }}t\in \mathbb {R} .$

Then $\left\{X_{t}\right\}$ is strictly stationary since (⁠ $(t+Y)$ ⁠ modulo ⁠ $2\pi$ ⁠) follows the same uniform distribution as Y for any ⁠ t ⁠.

#### Example 3

Keep in mind that a weakly white noise is not necessarily strictly stationary. Let $\omega$ be a random variable uniformly distributed in the interval $(0,2\pi )$ and define the time series $\left\{z_{t}\right\}$ by

$z_{t}=\cos(t\omega )\quad (t=1,2,...)$

Then

${\begin{aligned}\mathbb {E} (z_{t})&={\frac {1}{2\pi }}\int _{0}^{2\pi }\cos(t\omega )\,d\omega =0,\\\operatorname {Var} (z_{t})&={\frac {1}{2\pi }}\int _{0}^{2\pi }\cos ^{2}(t\omega )\,d\omega =1/2,\\\operatorname {Cov} (z_{t},z_{j})&={\frac {1}{2\pi }}\int _{0}^{2\pi }\cos(t\omega )\cos(j\omega )\,d\omega =0\quad \forall t\neq j.\end{aligned}}$

So $\{z_{t}\}$ is a white noise in the weak sense (the mean and cross-covariances are zero, and the variances are all the same), however it is not strictly stationary.

## *N*th-order stationarity

In **Eq.1**, the distribution of n samples of the stochastic process must be equal to the distribution of the samples shifted in time *for all* ⁠ n ⁠. ⁠ N ⁠th-order stationarity is a weaker form of stationarity where this is only requested for all n up to a certain order ⁠ N ⁠. A random process $\left\{X_{t}\right\}$ is said to be **⁠ N ⁠th-order stationary** if:

| $F_{X}(x_{t_{1}+\tau },\ldots ,x_{t_{n}+\tau })=F_{X}(x_{t_{1}},\ldots ,x_{t_{n}})\quad {\text{for all }}\tau ,t_{1},\ldots ,t_{n}\in \mathbb {R} {\text{ and for all }}n\in \{1,\ldots ,N\}$ |   | Eq.2 |
|---|---|---|

## Weak or wide-sense stationarity

### Definition

A weaker form of stationarity commonly employed in signal processing is known as **weak-sense stationarity**, **wide-sense stationarity (WSS)**, or **covariance stationarity**. WSS random processes only require that 1st moment (i.e. the mean) and autocovariance do not vary with respect to time and that the 2nd moment is finite for all times. Any strictly stationary process that has a finite mean and covariance is also WSS.

So, a continuous time random process $\left\{X_{t}\right\}$ that is WSS has the following restrictions on its mean function $m_{X}(t)\triangleq \operatorname {E} [X_{t}]$ and autocovariance function ⁠ $K_{XX}(t_{1},t_{2})\triangleq \operatorname {E} [(X_{t_{1}}-m_{X}(t_{1}))(X_{t_{2}}-m_{X}(t_{2}))]$ ⁠:

| ${\begin{aligned}&m_{X}(t)=m_{X}(t+\tau )&&{\text{for all }}\tau ,t\in \mathbb {R} \\&K_{XX}(t_{1},t_{2})=K_{XX}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \\&\operatorname {E} [\|X_{t}\|^{2}]<\infty &&{\text{for all }}t\in \mathbb {R} \end{aligned}}$ |   | Eq.3 |
|---|---|---|

The first property implies that the mean function $m_{X}(t)$ must be constant. The second property implies that the autocovariance function depends only on the *difference* between $t_{1}$ and $t_{2}$ and only needs to be indexed by one variable rather than two variables. Thus, instead of writing,

$\,\!K_{XX}(t_{1}-t_{2},0)\,$

the notation is often abbreviated by the substitution ⁠ $\tau =t_{1}-t_{2}$ ⁠:

$K_{XX}(\tau )\triangleq K_{XX}(t_{1}-t_{2},0)$

This also implies that the autocorrelation depends only on ⁠ $\tau =t_{1}-t_{2}$ ⁠, that is

$R_{X}(t_{1},t_{2})=R_{X}(t_{1}-t_{2},0)\triangleq R_{X}(\tau ).$

The third property says that the second moments must be finite for any time ⁠ t ⁠.

### Motivation

The main advantage of wide-sense stationarity is that it places the time-series in the context of Hilbert spaces. Let ⁠ H ⁠ be the Hilbert space generated by ⁠ $\{x(t)\}$ ⁠ (that is, the closure of the set of all linear combinations of these random variables in the Hilbert space of all square-integrable random variables on the given probability space). By the positive definiteness of the autocovariance function, it follows from Bochner's theorem that there exists a positive measure $\mu$ on the real line such that ⁠ H ⁠ is isomorphic to the Hilbert subspace of ⁠ $L^{2}(\mu )$ ⁠ generated by ⁠ $\{e^{-2\pi i\xi \cdot t}\}$ ⁠. This then gives the following Fourier-type decomposition for a continuous time stationary stochastic process: there exists a stochastic process $\omega _{\xi }$ with orthogonal increments such that, for all ⁠ t ⁠:

$X_{t}=\int e^{-2\pi i\lambda \cdot t}\,d\omega _{\lambda },$

where the integral on the right-hand side is interpreted in a suitable (Riemann) sense. The same result holds for a discrete-time stationary process, with the spectral measure now defined on the unit circle.

When processing WSS random signals with linear, time-invariant (LTI) filters, it is helpful to think of the correlation function as a linear operator. Since it is a circulant operator (depends only on the difference between the two arguments), its eigenfunctions are the Fourier complex exponentials. Additionally, since the eigenfunctions of LTI operators are also complex exponentials, LTI processing of WSS random signals is highly tractable—all computations can be performed in the frequency domain. Thus, the WSS assumption is widely employed in signal processing algorithms.

### Definition for complex stochastic process

In the case where $\left\{X_{t}\right\}$ is a complex stochastic process the autocovariance function is defined as $K_{XX}(t_{1},t_{2})=\operatorname {E} [(X_{t_{1}}-m_{X}(t_{1})){\overline {(X_{t_{2}}-m_{X}(t_{2}))}}]$ and, in addition to the requirements in **Eq.3**, it is required that the pseudo-autocovariance function $J_{XX}(t_{1},t_{2})=\operatorname {E} [(X_{t_{1}}-m_{X}(t_{1}))(X_{t_{2}}-m_{X}(t_{2}))]$ depends only on the time lag. In formulas, $\left\{X_{t}\right\}$ is WSS, if

| ${\begin{aligned}&m_{X}(t)=m_{X}(t+\tau )&&{\text{for all }}\tau ,t\in \mathbb {R} \\&K_{XX}(t_{1},t_{2})=K_{XX}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \\&J_{XX}(t_{1},t_{2})=J_{XX}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \\&\operatorname {E} [\|X(t)\|^{2}]<\infty &&{\text{for all }}t\in \mathbb {R} \end{aligned}}$ |   | Eq.4 |
|---|---|---|

## Joint stationarity

The concept of stationarity may be extended to two stochastic processes.

### Joint strict-sense stationarity

Two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are called **jointly strict-sense stationary** if their joint cumulative distribution $F_{XY}(x_{t_{1}},\ldots ,x_{t_{m}},y_{t_{1}^{'}},\ldots ,y_{t_{n}^{'}})$ remains unchanged under time shifts, i.e. if

| $F_{XY}(x_{t_{1}},\ldots ,x_{t_{m}},y_{t_{1}^{'}},\ldots ,y_{t_{n}^{'}})=F_{XY}(x_{t_{1}+\tau },\ldots ,x_{t_{m}+\tau },y_{t_{1}^{'}+\tau },\ldots ,y_{t_{n}^{'}+\tau })\quad {\text{for all }}\tau ,t_{1},\ldots ,t_{m},t_{1}^{'},\ldots ,t_{n}^{'}\in \mathbb {R} {\text{ and for all }}m,n\in \mathbb {N}$ |   | Eq.5 |
|---|---|---|

### Joint (*M* + *N*)th-order stationarity

Two random processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ is said to be **jointly (⁠ $M+N$ ⁠)th-order stationary** if:

| $F_{XY}(x_{t_{1}},\ldots ,x_{t_{m}},y_{t_{1}^{'}},\ldots ,y_{t_{n}^{'}})=F_{XY}(x_{t_{1}+\tau },\ldots ,x_{t_{m}+\tau },y_{t_{1}^{'}+\tau },\ldots ,y_{t_{n}^{'}+\tau })\quad {\text{for all }}\tau ,t_{1},\ldots ,t_{m},t_{1}^{'},\ldots ,t_{n}^{'}\in \mathbb {R} {\text{ and for all }}m\in \{1,\ldots ,M\},n\in \{1,\ldots ,N\}$ |   | Eq.6 |
|---|---|---|

### Joint weak or wide-sense stationarity

Two stochastic processes $\left\{X_{t}\right\}$ and $\left\{Y_{t}\right\}$ are called **jointly wide-sense stationary** if they are both wide-sense stationary and their cross-covariance function $K_{XY}(t_{1},t_{2})=\operatorname {E} [(X_{t_{1}}-m_{X}(t_{1}))(Y_{t_{2}}-m_{Y}(t_{2}))]$ depends only on the time difference ⁠ $\tau =t_{1}-t_{2}$ ⁠. This may be summarized as follows:

| ${\begin{aligned}&m_{X}(t)=m_{X}(t+\tau )&&{\text{for all }}\tau ,t\in \mathbb {R} \\&m_{Y}(t)=m_{Y}(t+\tau )&&{\text{for all }}\tau ,t\in \mathbb {R} \\&K_{XX}(t_{1},t_{2})=K_{XX}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \\&K_{YY}(t_{1},t_{2})=K_{YY}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \\&K_{XY}(t_{1},t_{2})=K_{XY}(t_{1}-t_{2},0)&&{\text{for all }}t_{1},t_{2}\in \mathbb {R} \end{aligned}}$ |   | Eq.7 |
|---|---|---|

## Relation between types of stationarity

- If a stochastic process is ⁠ N ⁠th-order stationary, then it is also ⁠ M ⁠th-order stationary for all ⁠ $M\leq N$ ⁠.
- If a stochastic process is second order stationary (⁠ $N=2$ ⁠) and has finite second moments, then it is also wide-sense stationary.
- If a stochastic process is wide-sense stationary, it is not necessarily second-order stationary.
- If a stochastic process is strict-sense stationary and has finite second moments, it is wide-sense stationary.
- If two stochastic processes are jointly (⁠ $M+N$ ⁠)th-order stationary, this does not guarantee that the individual processes are ⁠ M ⁠th- respectively ⁠ N ⁠th-order stationary.

## Other terminology

The terminology used for types of stationarity other than strict stationarity can be rather mixed. Some examples follow.

- Priestley uses **stationary up to order** ⁠ m ⁠ if conditions similar to those given here for wide sense stationarity apply relating to moments up to order ⁠ m ⁠. Thus wide sense stationarity would be equivalent to "stationary to order 2", which is different from the definition of second-order stationarity given here.
- Honarkhah and Caers also use the assumption of stationarity in the context of multiple-point geostatistics, where higher ⁠ n ⁠-point statistics are assumed to be stationary in the spatial domain.

## Techniques to stationarize a non-stationary process

In time series analysis and stochastic processes, stationarizing a time series is a crucial preprocessing step aimed at transforming a non-stationary process into a stationary one. Several techniques exist for achieving this, depending on the type and order of non-stationarity present. For first-order non-stationarity, where the mean of the process varies over time, differencing is a common and effective method: it transforms the series by subtracting each value from its predecessor, thus stabilizing the mean. For non-stationarities up to the second order, time-frequency analysis (e.g., Wavelet transform, Wigner distribution function, or Short-time Fourier transform) can be employed to isolate and suppress time-localized, nonstationary spectral components. Additionally, surrogate data methods can be used to construct strictly stationary versions of the original time series. One of the ways for identifying non-stationary times series is the ACF plot. Sometimes, patterns will be more visible in the ACF plot than in the original time series; however, this is not always the case.

The choice of method for time series stationarization depends on the nature of the non-stationarity and the goals of the analysis, especially when building models that require strict stationarity assumptions, such as ARMA or spectral-based techniques. More details on some time series stationarization methods are presented below.

### Stationarization by means of differencing

One way to make some time series first-order stationary is to compute the differences between consecutive observations. This is known as differencing. Differencing can help stabilize the mean of a time series by removing changes in the level of a time series, and so eliminating trends. This can also remove seasonality, if differences are taken appropriately (e.g. differencing observations 1 year apart to remove a yearly trend). Transformations such as logarithms can help to stabilize the variance of a time series.

### Stationarization by means of the surrogate method

The surrogate method for stationarization works by generating a new time series that preserves certain statistical properties of the original series while removing its nonstationary components. A common approach is to apply the Fourier Transform to the original time series to obtain its magnitude and phase spectra. The magnitude spectrum, which determines the power distribution across frequencies, is retained to preserve the global autocorrelation structure. The phase spectrum, which encodes the temporal alignment of frequency components and is often responsible for time-dependent dynamics in the time series (like non-stationarities), is then randomized, typically by replacing it with a set of random phases drawn uniformly from $[-\pi ,\pi ]$ while enforcing conjugate symmetry to ensure a real-valued inverse. Applying the inverse Fourier Transform to the modified spectra yields a strictly stationary surrogate time series: one with the same power spectrum as the original but lacking the temporal structures that caused non-stationarity. This technique is often used in hypothesis tests for probing the stationarity property.

---
title: "Autoregressive model"
source: https://en.wikipedia.org/wiki/Autoregressive_model
domain: speculative-decoding
license: CC-BY-SA-4.0
tags: speculative decoding, draft model verification, llm inference acceleration, parallel token proposal, assisted generation
fetched: 2026-07-02
---

# Autoregressive model

In statistics, an **autoregressive** (**AR**) **model** is a modelled representation of a type of random process. It can be used to describe time-varying processes from many natural and artificial sources. The model specifies output variables that are dependent linearly on their own previous values on a stochastic basis. The model is in the form of a stochastic difference equation (or recurrence relation) which should not be confused with a differential equation. Together with the moving-average (MA) model, it is a special case and key component of the more general autoregressive–moving-average (ARMA) and autoregressive integrated moving average (ARIMA) models of time series, which have a more complicated stochastic structure; it is also a special case of the vector autoregressive model (VAR), which consists of a system of more than one interlocking stochastic difference equation in more than one evolving random variable.

Another important extension is the time-varying autoregressive (TVAR) model, where the autoregressive coefficients are allowed to change over time to model evolving or non-stationary processes. TVAR models are widely applied in cases where the underlying dynamics of the system are not constant, such as in sensors time series modelling, climate science, economics and finance (as econometrics), signal processing, telecommunications, radar systems, and biological signals.

Unlike the moving-average (MA) model, the autoregressive model is not always stationary; non-stationarity can arise either due to the presence of a unit root or due to time-varying model parameters, as in time-varying autoregressive models.

Large language models are called autoregressive, but they are not a classical autoregressive model in this sense because they are not linear.

## Definition

The notation $AR(p)$ indicates an autoregressive model of order *p*. The AR(*p*) model is defined as

$X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}$

where $\varphi _{1},\ldots ,\varphi _{p}$ are the *parameters* of the model, and $\varepsilon _{t}$ is white noise. This can be equivalently written using the backshift operator *B* as

$X_{t}=\sum _{i=1}^{p}\varphi _{i}B^{i}X_{t}+\varepsilon _{t}$

so that, moving the summation term to the left side and using polynomial notation, we have

$\varphi (B)X_{t}=\varepsilon _{t}$

An autoregressive model can thus be viewed as the output of an all-pole infinite impulse response filter whose input is white noise.

Some parameter constraints are necessary for the model to remain weak-sense stationary. For example, processes in the AR(1) model with $|\varphi _{1}|\geq 1$ are not stationary. More generally, for an AR(*p*) model to be weak-sense stationary, the roots of the polynomial $\Phi (z):=\textstyle 1-\sum _{i=1}^{p}\varphi _{i}z^{i}$ must lie outside the unit circle, i.e., each (complex) root $z_{i}$ must satisfy $|z_{i}|>1$ (see pages 89,92 ).

## Intertemporal effect of shocks

In an AR process, a one-time shock affects values of the evolving variable infinitely far into the future. For example, consider the AR(1) model $X_{t}=\varphi _{1}X_{t-1}+\varepsilon _{t}$ . A non-zero value for $\varepsilon _{t}$ at say time *t*=1 affects $X_{1}$ by the amount $\varepsilon _{1}$ . Then by the AR equation for $X_{2}$ in terms of $X_{1}$ , this affects $X_{2}$ by the amount $\varphi _{1}\varepsilon _{1}$ . Then by the AR equation for $X_{3}$ in terms of $X_{2}$ , this affects $X_{3}$ by the amount $\varphi _{1}^{2}\varepsilon _{1}$ . Continuing this process shows that the effect of $\varepsilon _{1}$ never ends, although if the process is stationary then the effect diminishes toward zero in the limit.

Because each shock affects *X* values infinitely far into the future from when they occur, any given value *X**t* is affected by shocks occurring infinitely far into the past. This can also be seen by rewriting the autoregression

$\varphi (B)X_{t}=\varepsilon _{t}\,$

(where the constant term has been suppressed by assuming that the variable has been measured as deviations from its mean) as

$X_{t}={\frac {1}{\varphi (B)}}\varepsilon _{t}\,.$

When the polynomial division on the right side is carried out, the polynomial in the backshift operator applied to $\varepsilon _{t}$ has an infinite order—that is, an infinite number of lagged values of $\varepsilon _{t}$ appear on the right side of the equation.

## Characteristic polynomial

The autocorrelation function of an AR(*p*) process can be expressed as

$\rho (\tau )=\sum _{k=1}^{p}a_{k}y_{k}^{-|\tau |},$

where $y_{k}$ are the roots of the polynomial

$\varphi (B)=1-\sum _{k=1}^{p}\varphi _{k}B^{k}$

where *B* is the backshift operator, where $\varphi (\cdot )$ is the function defining the autoregression, and where $\varphi _{k}$ are the coefficients in the autoregression. The formula is valid only if all the roots have multiplicity 1.

The autocorrelation function of an AR(*p*) process is a sum of decaying exponentials.

- Each real root contributes a component to the autocorrelation function that decays exponentially.
- Similarly, each pair of complex conjugate roots contributes an exponentially damped oscillation.

## Graphs of AR(*p*) processes

The simplest AR process is AR(0), which has no dependence between the terms. Only the error/innovation/noise term contributes to the output of the process, so in the figure, AR(0) corresponds to white noise.

For an AR(1) process with a positive $\varphi$ , only the previous term in the process and the noise term contribute to the output. If $\varphi$ is close to 0, then the process still looks like white noise, but as $\varphi$ approaches 1, the output gets a larger contribution from the previous term relative to the noise. This results in a "smoothing" or integration of the output, similar to a low pass filter.

For an AR(2) process, the previous two terms and the noise term contribute to the output. If both $\varphi _{1}$ and $\varphi _{2}$ are positive, the output will resemble a low pass filter, with the high frequency part of the noise decreased. If $\varphi _{1}$ is positive while $\varphi _{2}$ is negative, then the process favors changes in sign between terms of the process. The output oscillates. This can be linked to edge detection or detection of change in direction.

## Example: An AR(1) process

An AR(1) process is given by: $X_{t}=\varphi X_{t-1}+\varepsilon _{t}\,$ where $\varepsilon _{t}$ is a white noise process with zero mean and constant variance $\sigma _{\varepsilon }^{2}$ . (Note: The subscript on $\varphi _{1}$ has been dropped.) The process is weak-sense stationary if $|\varphi |<1$ since it is obtained as the output of a stable filter whose input is white noise. (If $\varphi =1$ then the variance of $X_{t}$ depends on time lag *t*, so that the variance of the series diverges to infinity as *t* goes to infinity, and is therefore not weak-sense stationary.) Assuming $|\varphi |<1$ , the mean $\operatorname {E} (X_{t})$ is identical for all values of *t* by definition of weak sense stationarity. If the mean is denoted by $\mu$ , it follows from $\operatorname {E} (X_{t})=\varphi \operatorname {E} (X_{t-1})+\operatorname {E} (\varepsilon _{t}),$ that $\mu =\varphi \mu +0,$ and hence

$\mu =0.$

The variance is

${\textrm {var}}(X_{t})=\operatorname {E} (X_{t}^{2})-\mu ^{2}={\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}},$

where $\sigma _{\varepsilon }$ is the standard deviation of $\varepsilon _{t}$ . This can be shown by noting that

${\textrm {var}}(X_{t})=\varphi ^{2}{\textrm {var}}(X_{t-1})+\sigma _{\varepsilon }^{2},$

and then by noticing that the quantity above is a stable fixed point of this relation.

The autocovariance is given by

$B_{n}=\operatorname {E} (X_{t+n}X_{t})-\mu ^{2}={\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,\,\varphi ^{|n|}.$

It can be seen that the autocovariance function decays with a decay time (also called time constant) of $\tau =1/(1-\varphi )$ .

The spectral density function is the Fourier transform of the autocovariance function. In discrete terms this will be the discrete-time Fourier transform:

$\Phi (\omega )={\frac {1}{\sqrt {2\pi }}}\,\sum _{n=-\infty }^{\infty }B_{n}e^{-i\omega n}={\frac {1}{\sqrt {2\pi }}}\,\left({\frac {\sigma _{\varepsilon }^{2}}{1+\varphi ^{2}-2\varphi \cos(\omega )}}\right).$

This expression is periodic due to the discrete nature of the $X_{j}$ , which is manifested as the cosine term in the denominator. If we assume that the sampling time ( $\Delta t=1$ ) is much smaller than the decay time ( $\tau$ ), then we can use a continuum approximation to $B_{n}$ :

$B(t)\approx {\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,\,\varphi ^{|t|}$

which yields a Lorentzian profile for the spectral density:

$\Phi (\omega )={\frac {1}{\sqrt {2\pi }}}\,{\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,{\frac {\gamma }{\pi (\gamma ^{2}+\omega ^{2})}}$

where $\gamma =1/\tau$ is the angular frequency associated with the decay time $\tau$ .

An alternative expression for $X_{t}$ can be derived by first substituting $\varphi X_{t-2}+\varepsilon _{t-1}$ for $X_{t-1}$ in the defining equation. Continuing this process *N* times yields

$X_{t}=\varphi ^{N}X_{t-N}+\sum _{k=0}^{N-1}\varphi ^{k}\varepsilon _{t-k}.$

For *N* approaching infinity, $\varphi ^{N}$ will approach zero and:

$X_{t}=\sum _{k=0}^{\infty }\varphi ^{k}\varepsilon _{t-k}.$

It is seen that $X_{t}$ is white noise convolved with the $\varphi ^{k}$ kernel plus the constant mean. If the white noise $\varepsilon _{t}$ is a Gaussian process then $X_{t}$ is also a Gaussian process. In other cases, the central limit theorem indicates that $X_{t}$ will be approximately normally distributed when $\varphi$ is close to one.

For $\varepsilon _{t}=0$ , the process $X_{t}=\varphi X_{t-1}$ will be a geometric progression (*exponential* growth or decay). In this case, the solution can be found analytically: $X_{t}=a\varphi ^{t}$ whereby a is an unknown constant (initial condition).

### Explicit mean/difference form of AR(1) process

The AR(1) model is the discrete-time analogy of the continuous Ornstein-Uhlenbeck process. It is therefore sometimes useful to understand the properties of the AR(1) model cast in an equivalent form. In this form, the AR(1) model, with process parameter $\theta \in \mathbb {R}$ , is given by

$X_{t+1}=X_{t}+(1-\theta )(\mu -X_{t})+\varepsilon _{t+1}$

, where

$|\theta |<1\,$

,

${\displaystyle \mu$

is the model mean, and

$\{\varepsilon _{t}\}$

is a white-noise process with zero mean and constant variance

$\sigma$

.

By rewriting this as $X_{t+1}=\theta X_{t}+(1-\theta )\mu +\varepsilon _{t+1}$ and then deriving (by induction) $X_{t+n}=\theta ^{n}X_{t}+(1-\theta ^{n})\mu +\sum _{i=1}^{n}\left(\theta ^{n-i}\varepsilon _{t+i}\right)$ , one can show that

$\operatorname {E} (X_{t+n}\mid X_{t})=\mu \left[1-\theta ^{n}\right]+X_{t}\theta ^{n}$

and

$\operatorname {Var} (X_{t+n}\mid X_{t})=\sigma ^{2}{\frac {1-\theta ^{2n}}{1-\theta ^{2}}}.$

## Choosing the maximum lag

The partial autocorrelation of an AR(p) process equals zero at lags larger than *p*, so the appropriate maximum lag *p* is the one after which the partial autocorrelations are all zero.

## Calculation of the AR parameters

There are many ways to estimate the coefficients, such as the ordinary least squares procedure or method of moments (through Yule–Walker equations).

The AR(*p*) model is given by the equation

$X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}.\,$

It is based on parameters $\varphi _{i}$ where *i* = 1, ..., *p*. There is a direct correspondence between these parameters and the covariance function of the process, and this correspondence can be inverted to determine the parameters from the autocorrelation function (which is itself obtained from the covariances). This is done using the Yule–Walker equations.

### Yule–Walker equations

The Yule–Walker equations, named for Udny Yule and Gilbert Walker, are the following set of equations.

$\gamma _{m}=\sum _{k=1}^{p}\varphi _{k}\gamma _{m-k}+\sigma _{\varepsilon }^{2}\delta _{m,0},$

where *m* = 0, …, *p*, yielding *p* + 1 equations. Here $\gamma _{m}$ is the autocovariance function of Xt, $\sigma _{\varepsilon }$ is the standard deviation of the input noise process, and $\delta _{m,0}$ is the Kronecker delta function.

Because the last part of an individual equation is non-zero only if *m* = 0, the set of equations can be solved by representing the equations for *m* > 0 in matrix form, thus getting the equation

${\begin{bmatrix}\gamma _{1}\\\gamma _{2}\\\gamma _{3}\\\vdots \\\gamma _{p}\\\end{bmatrix}}={\begin{bmatrix}\gamma _{0}&\gamma _{-1}&\gamma _{-2}&\cdots \\\gamma _{1}&\gamma _{0}&\gamma _{-1}&\cdots \\\gamma _{2}&\gamma _{1}&\gamma _{0}&\cdots \\\vdots &\vdots &\vdots &\ddots \\\gamma _{p-1}&\gamma _{p-2}&\gamma _{p-3}&\cdots \\\end{bmatrix}}{\begin{bmatrix}\varphi _{1}\\\varphi _{2}\\\varphi _{3}\\\vdots \\\varphi _{p}\\\end{bmatrix}}$

which can be solved for all $\{\varphi _{m};m=1,2,\dots ,p\}.$ The remaining equation for *m* = 0 is

$\gamma _{0}=\sum _{k=1}^{p}\varphi _{k}\gamma _{-k}+\sigma _{\varepsilon }^{2},$

which, once $\{\varphi _{m};m=1,2,\dots ,p\}$ are known, can be solved for $\sigma _{\varepsilon }^{2}.$

An alternative formulation is in terms of the autocorrelation function. The AR parameters are determined by the first *p*+1 elements $\rho (\tau )$ of the autocorrelation function. The full autocorrelation function can then be derived by recursively calculating

$\rho (\tau )=\sum _{k=1}^{p}\varphi _{k}\rho (k-\tau )$

Examples for some Low-order AR(*p*) processes

- *p*=1
  - $\gamma _{1}=\varphi _{1}\gamma _{0}$
  - Hence $\rho _{1}=\gamma _{1}/\gamma _{0}=\varphi _{1}$
- *p*=2
  - The Yule–Walker equations for an AR(2) process are $\gamma _{1}=\varphi _{1}\gamma _{0}+\varphi _{2}\gamma _{-1}$ $\gamma _{2}=\varphi _{1}\gamma _{1}+\varphi _{2}\gamma _{0}$
    - Remember that $\gamma _{-k}=\gamma _{k}$
    - Using the first equation yields $\rho _{1}=\gamma _{1}/\gamma _{0}={\frac {\varphi _{1}}{1-\varphi _{2}}}$
    - Using the recursion formula yields $\rho _{2}=\gamma _{2}/\gamma _{0}={\frac {\varphi _{1}^{2}-\varphi _{2}^{2}+\varphi _{2}}{1-\varphi _{2}}}$

### Estimation of AR parameters

The above equations (the Yule–Walker equations) provide several routes to estimating the parameters of an AR(*p*) model, by replacing the theoretical covariances with estimated values. Some of these variants can be described as follows:

- Estimation of autocovariances or autocorrelations. Here each of these terms is estimated separately, using conventional estimates. There are different ways of doing this and the choice between these affects the properties of the estimation scheme. For example, negative estimates of the variance can be produced by some choices.
- Formulation as a least squares regression problem in which an ordinary least squares prediction problem is constructed, basing prediction of values of *X**t* on the *p* previous values of the same series. This can be thought of as a forward-prediction scheme. The normal equations for this problem can be seen to correspond to an approximation of the matrix form of the Yule–Walker equations in which each appearance of an autocovariance of the same lag is replaced by a slightly different estimate.
- Formulation as an extended form of ordinary least squares prediction problem. Here two sets of prediction equations are combined into a single estimation scheme and a single set of normal equations. One set is the set of forward-prediction equations and the other is a corresponding set of backward prediction equations, relating to the backward representation of the AR model:

$X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t+i}+\varepsilon _{t}^{*}\,.$

Here predicted values of

X

t

would be based on the

p

future values of the same series.

This way of estimating the AR parameters is due to John Parker Burg,

and is called the Burg method:

Burg and later authors called these particular estimates "maximum entropy estimates",

but the reasoning behind this applies to the use of any set of estimated AR parameters. Compared to the estimation scheme using only the forward prediction equations, different estimates of the autocovariances are produced, and the estimates have different stability properties. Burg estimates are particularly associated with

maximum entropy spectral estimation

.

Other possible approaches to estimation include maximum likelihood estimation. Two distinct variants of maximum likelihood are available: in one (broadly equivalent to the forward prediction least squares scheme) the likelihood function considered is that corresponding to the conditional distribution of later values in the series given the initial *p* values in the series; in the second, the likelihood function considered is that corresponding to the unconditional joint distribution of all the values in the observed series. Substantial differences in the results of these approaches can occur if the observed series is short, or if the process is close to non-stationarity.

## Spectrum

The power spectral density (PSD) of an AR(*p*) process with noise variance $\mathrm {Var} (Z_{t})=\sigma _{Z}^{2}$ is

$S(f)={\frac {\sigma _{Z}^{2}}{|1-\sum _{k=1}^{p}\varphi _{k}e^{-i2\pi fk}|^{2}}}.$

### AR(0)

For white noise (AR(0))

$S(f)=\sigma _{Z}^{2}.$

### AR(1)

For AR(1)

$S(f)={\frac {\sigma _{Z}^{2}}{|1-\varphi _{1}e^{-2\pi if}|^{2}}}={\frac {\sigma _{Z}^{2}}{1+\varphi _{1}^{2}-2\varphi _{1}\cos 2\pi f}}$

- If $\varphi _{1}>0$ there is a single spectral peak at $f=0$ , often referred to as red noise. As $\varphi _{1}$ becomes nearer 1, there is stronger power at low frequencies, i.e. larger time lags. This is then a low-pass filter, when applied to full spectrum light, everything except for the red light will be filtered.
- If $\varphi _{1}<0$ there is a minimum at $f=0$ , often referred to as blue noise. This similarly acts as a high-pass filter, everything except for blue light will be filtered.

### AR(2)

The behavior of an AR(2) process is determined entirely by the roots of it characteristic equation, which is expressed in terms of the lag operator as:

$1-\varphi _{1}B-\varphi _{2}B^{2}=0,$

or equivalently by the poles of its transfer function, which is defined in the Z domain by:

$H_{z}=(1-\varphi _{1}z^{-1}-\varphi _{2}z^{-2})^{-1}.$

It follows that the poles are values of z satisfying:

$1-\varphi _{1}z^{-1}-\varphi _{2}z^{-2}=0,$

which yields:

$z_{1},z_{2}={\frac {1}{2\varphi _{2}}}\left(\varphi _{1}\pm {\sqrt {\varphi _{1}^{2}+4\varphi _{2}}}\,\right).$

$z_{1}$ and $z_{2}$ are the reciprocals of the characteristic roots, as well as the eigenvalues of the temporal update matrix:

${\begin{bmatrix}\varphi _{1}&\varphi _{2}\\1&0\end{bmatrix}}$

AR(2) processes can be split into three groups depending on the characteristics of their roots/poles:

- When $\varphi _{1}^{2}+4\varphi _{2}<0$ , the process has a pair of complex-conjugate poles, creating a mid-frequency peak at:

$f^{*}={\frac {1}{2\pi }}\cos ^{-1}\left({\frac {\varphi _{1}}{2{\sqrt {-\varphi _{2}}}}}\right),$

with bandwidth about the peak inversely proportional to the moduli of the poles:

$|z_{1}|=|z_{2}|={\sqrt {-\varphi _{2}}}.$

The terms involving square roots are all real in the case of complex poles since they exist only when $\varphi _{2}<0$ .

Otherwise the process has real roots, and:

- When $\varphi _{1}>0$ it acts as a low-pass filter on the white noise with a spectral peak at $f=0$
- When $\varphi _{1}<0$ it acts as a high-pass filter on the white noise with a spectral peak at $f=1/2$ .

The process is non-stationary when the poles are on or outside the unit circle, or equivalently when the characteristic roots are on or inside the unit circle. The process is stable when the poles are strictly within the unit circle (roots strictly outside the unit circle), or equivalently when the coefficients are in the triangle $-1\leq \varphi _{2}\leq 1-|\varphi _{1}|$ .

The full PSD function can be expressed in real form as:

$S(f)={\frac {\sigma _{Z}^{2}}{1+\varphi _{1}^{2}+\varphi _{2}^{2}-2\varphi _{1}(1-\varphi _{2})\cos(2\pi f)-2\varphi _{2}\cos(4\pi f)}}$

## Implementations in statistics packages

- R – the *stats* package includes *ar* function; the *astsa* package includes *sarima* function to fit various models including AR.
- MATLAB – the Econometrics Toolbox and System Identification Toolbox include AR models.
- MATLAB and Octave – the *TSA* toolbox contains several estimation functions for uni-variate, multivariate, and adaptive AR models.
- PyMC3 – the Bayesian statistics and probabilistic programming framework supports AR modes with *p* lags.
- *bayesloop* – supports parameter inference and model selection for the AR-1 process with time-varying parameters.
- Python – statsmodels.org hosts an AR model.

## Impulse response

The impulse response of a system is the change in an evolving variable in response to a change in the value of a shock term *k* periods earlier, as a function of *k*. Since the AR model is a special case of the vector autoregressive model, the computation of the impulse response in vector autoregression#impulse response applies here.

## *n*-step-ahead forecasting

Once the parameters of the autoregression

$X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}\,$

have been estimated, the autoregression can be used to forecast an arbitrary number of periods into the future. First use *t* to refer to the first period for which data is not yet available; substitute the known preceding values *X**t-i* for *i=*1, ..., *p* into the autoregressive equation while setting the error term $\varepsilon _{t}$ equal to zero (because we forecast *X**t* to equal its expected value, and the expected value of the unobserved error term is zero). The output of the autoregressive equation is the forecast for the first unobserved period. Next, use *t* to refer to the *next* period for which data is not yet available; again the autoregressive equation is used to make the forecast, with one difference: the value of *X* one period prior to the one now being forecast is not known, so its expected value—the predicted value arising from the previous forecasting step—is used instead. Then for future periods the same procedure is used, each time using one more forecast value on the right side of the predictive equation until, after *p* predictions, all *p* right-side values are predicted values from preceding steps.

There are four sources of uncertainty regarding predictions obtained in this manner: (1) uncertainty as to whether the autoregressive model is the correct model; (2) uncertainty about the accuracy of the forecasted values that are used as lagged values in the right side of the autoregressive equation; (3) uncertainty about the true values of the autoregressive coefficients; and (4) uncertainty about the value of the error term $\varepsilon _{t}\,$ for the period being predicted. Each of the last three can be quantified and combined to give a confidence interval for the *n*-step-ahead predictions; the confidence interval will become wider as *n* increases because of the use of an increasing number of estimated values for the right-side variables.

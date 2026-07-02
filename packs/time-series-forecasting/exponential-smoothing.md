---
title: "Exponential smoothing"
source: https://en.wikipedia.org/wiki/Exponential_smoothing
domain: time-series-forecasting
license: CC-BY-SA-4.0
tags: time series, forecasting model, arima model, seasonality trend, exponential smoothing
fetched: 2026-07-02
---

# Exponential smoothing

**Exponential smoothing** or **exponential moving average (EMA)** is a technique for smoothing time series data using the exponential window function. Whereas in the simple moving average the past observations are weighted equally, exponential functions are used to assign exponentially decreasing weights over time. It is an easily learned and easily applied procedure for making some determination based on prior assumptions by the user, such as seasonality. Exponential smoothing is often used for analysis of time-series data.

Exponential smoothing is one of many window functions commonly applied to smooth data in signal processing, acting as low-pass filters to remove high-frequency noise. This method is preceded by Poisson's use of recursive exponential window functions in convolutions from the 19th century, as well as Kolmogorov and Zurbenko's use of recursive moving averages from their studies of turbulence in the 1940s.

The raw data sequence is often represented by ${\textstyle \{x_{t}\}}$ beginning at time ${\textstyle t=0}$ , and the output of the exponential smoothing algorithm is commonly written as ${\textstyle \{s_{t}\}}$ , which may be regarded as a best estimate of what the next value of ${\textstyle x}$ will be. When the sequence of observations begins at time ${\textstyle t=0}$ , the simplest form of exponential smoothing is given by the following formulas:

${\begin{aligned}s_{0}&=x_{0}\\s_{t}&=\alpha x_{t}+(1-\alpha )s_{t-1},\quad t>0\end{aligned}}$

where ${\textstyle \alpha }$ is the *smoothing factor*, and ${\textstyle 0<\alpha <1}$ . If ${\textstyle s_{t-1}}$ is substituted into ${\textstyle s_{t}}$ continuously so that the formula of ${\textstyle s_{t}}$ is fully expressed in terms of ${\textstyle \{x_{t}\}}$ , then exponentially decaying weighting factors on each raw data ${\textstyle x_{t}}$ is revealed, showing how exponential smoothing is named.

The simple exponential smoothing is not able to predict what would be observed at ${\textstyle t+m}$ based on the raw data up to ${\textstyle t}$ , while the double exponential smoothing and triple exponential smoothing can be used for the prediction due to the presence of $b_{t}$ as the sequence of best estimates of the linear trend.

## Basic (simple) exponential smoothing

The use of the exponential window function is first attributed to Poisson as an extension of a numerical analysis technique from the 17th century, and later adopted by the signal processing community in the 1940s. Here, exponential smoothing is the application of the exponential, or Poisson, window function. Exponential smoothing was suggested in the statistical literature without citation to previous work by Robert Goodell Brown in 1956, and expanded by Charles C. Holt in 1957. The formulation below, which is the one commonly used, is attributed to Brown and is known as "Brown’s simple exponential smoothing". All the methods of Holt, Winters, and Brown may be seen as a simple application of recursive filtering, first found in the 1940s to convert finite impulse response (FIR) filters to infinite impulse response filters.

The simplest form of exponential smoothing is given by the formula:

$s_{t}=\alpha x_{t}+(1-\alpha )s_{t-1}\,,$

where $\alpha$ is the *smoothing factor*, with $0\leq \alpha \leq 1$ . In other words, the smoothed statistic $s_{t}$ is a simple weighted average of the current observation $x_{t}$ and the previous smoothed statistic $s_{t-1}$ . Simple exponential smoothing is easily applied, and it produces a smoothed statistic as soon as two observations are available. The term *smoothing factor* applied to $\alpha$ here is something of a misnomer, as larger values of $\alpha$ actually reduce the level of smoothing, and in the limiting case with $\alpha$ = 1 the smoothing output series is just the current observation. Values of $\alpha$ close to 1 have less of a smoothing effect and give greater weight to recent changes in the data, while values of $\alpha$ closer to 0 have a greater smoothing effect and are less responsive to recent changes. In the limiting case with $\alpha$ = 0, the output series is just flat or a constant as the observation ${\textstyle x_{0}}$ at the beginning of the smoothening process ${\textstyle t=0}$ .

The method for choosing $\alpha$ must be decided by the modeler. Sometimes the statistician's judgment is used to choose an appropriate factor. Alternatively, a statistical technique may be used to *optimize* the value of $\alpha$ . For example, the method of least squares might be used to determine the value of $\alpha$ for which the sum of the quantities $(s_{t}-x_{t+1})^{2}$ is minimized.

Unlike some other smoothing methods, such as the simple moving average, this technique does not require any minimum number of observations to be made before it begins to produce results. In practice, however, a "good average" will not be achieved until several samples have been averaged together; for example, a constant signal will take approximately $3/\alpha$ stages to reach 95% of the actual value. To accurately reconstruct the original signal without information loss, all stages of the exponential moving average must also be available, because older samples decay in weight exponentially. This is in contrast to a simple moving average, in which some samples can be skipped without as much loss of information due to the constant weighting of samples within the average. If a known number of samples will be missed, one can adjust a weighted average for this as well, by giving equal weight to the new sample and all those to be skipped.

This simple form of exponential smoothing is also known as an exponentially weighted moving average (EWMA). Technically it can also be classified as an autoregressive integrated moving average (ARIMA) (0,1,1) model with no constant term.

### Time constant

The time constant of an exponential moving average is the amount of time for the smoothed response of a unit step function to reach $1-1/e\approx 63.2\,\%$ of the final signal. The relationship between this time constant, $\tau$ , and the smoothing factor, $\alpha$ , is given by the following formula:

$\alpha =1-e^{-\Delta T/\tau }$

, thus

$\tau =-{\frac {\Delta T}{\ln(1-\alpha )}}$

where $\Delta T$ is the sampling time interval of the discrete time implementation. If the sampling time is fast compared to the time constant ( $\Delta T\ll \tau$ ) then, by using the Taylor expansion of the exponential function,

$\alpha \approx {\frac {\Delta T}{\tau }}$

, thus

$\tau \approx {\frac {\Delta T}{\alpha }}$

### Choosing the initial smoothed value

Note that in the definition above, $s_{0}$ (the initial output of the exponential smoothing algorithm) is being initialized to $x_{0}$ (the initial raw data or observation). Because exponential smoothing requires that, at each stage, we have the previous forecast $s_{t-1}$ , it is not obvious how to get the method started. We could assume that the initial forecast is equal to the initial value of demand; however, this approach has a serious drawback. Exponential smoothing puts substantial weight on past observations, so the initial value of demand will have an unreasonably large effect on early forecasts. This problem can be overcome by allowing the process to evolve for a reasonable number of periods (10 or more) and using the average of the demand during those periods as the initial forecast. There are many other ways of setting this initial value, but the smaller the value of $\alpha$ , the more sensitive the forecast will be on the selection of this initial smoother value $s_{0}$ .

### Optimization

For every exponential smoothing method, we also need to choose the value for the smoothing parameters. For simple exponential smoothing, there is only one smoothing parameter (*α*), but for the methods that follow there are usually more than one smoothing parameter.

There are cases where the smoothing parameters may be chosen in a subjective manner – the forecaster specifies the value of the smoothing parameters based on previous experience. However, a more robust and objective way to obtain values of the unknown parameters included in any exponential smoothing method is to estimate them from the observed data.

The unknown parameters and the initial values for any exponential smoothing method can be estimated by minimizing the sum of squared errors (SSE). The errors are specified as ${\textstyle e_{t}=y_{t}-{\hat {y}}_{t\mid t-1}}$ for ${\textstyle t=1,\ldots ,T}$ (the one-step-ahead within-sample forecast errors) where ${\textstyle y_{t}}$ and ${\textstyle {\hat {y}}_{t\mid t-1}}$ are a variable to be predicted at t and a variable as the prediction result at t (based on the previous data or prediction), respectively. Hence, we find the values of the unknown parameters and the initial values that minimize

${\text{SSE}}=\sum _{t=1}^{T}(y_{t}-{\hat {y}}_{t\mid t-1})^{2}=\sum _{t=1}^{T}e_{t}^{2}$

Unlike the regression case (where we have formulae to directly compute the regression coefficients which minimize the SSE) this involves a non-linear minimization problem, and we need to use an optimization tool to perform this.

### "Exponential" naming

The name *exponential smoothing* is attributed to the use of the exponential function as the filter impulse response in the convolution.

By direct substitution of the defining equation for simple exponential smoothing back into itself we find that

${\begin{aligned}s_{t}&=\alpha x_{t}+(1-\alpha )s_{t-1}\\[3pt]&=\alpha x_{t}+\alpha (1-\alpha )x_{t-1}+(1-\alpha )^{2}s_{t-2}\\[3pt]&=\alpha \left[x_{t}+(1-\alpha )x_{t-1}+(1-\alpha )^{2}x_{t-2}+(1-\alpha )^{3}x_{t-3}+\cdots +(1-\alpha )^{t-1}x_{1}\right]+(1-\alpha )^{t}x_{0}.\end{aligned}}$

In other words, as time passes the smoothed statistic $s_{t}$ becomes the weighted average of a greater and greater number of the past observations $s_{t-1},\ldots ,s_{t-n},\ldots$ , and the weights assigned to previous observations are proportional to the terms of the geometric progression

$1,(1-\alpha ),(1-\alpha )^{2},\ldots ,(1-\alpha )^{n},\ldots$

A geometric progression is the discrete version of an exponential function, so this is where the name for this smoothing method originated according to Statistics lore.

### Comparison with moving average

Exponential smoothing and moving average have similar defects of introducing a lag relative to the input data. While this can be corrected by shifting the result by half the window length for a symmetrical kernel, such as a moving average or gaussian, this approach is not possible for exponential smoothing since it is an IIR filter and therefore has an asymmetric kernel and frequency-dependent group delay. This means each constituent frequency is shifted by a different amount and therefore, there is no single number of samples that can be used to shift the output signal to account for the lag.

Both filters also both have roughly the same distribution of forecast error when *α* = 2/(*k* + 1) where *k* is the number of past data points in consideration of moving average. They differ in that exponential smoothing takes into account all past data, whereas moving average only takes into account *k* past data points. Computationally speaking, they also differ in that moving average requires that the past *k* data points, or the data point at lag *k* + 1 plus the most recent forecast value, to be kept, whereas exponential smoothing only needs the most recent forecast value to be kept.

In the signal processing literature, the use of non-causal (symmetric) filters is commonplace, and the exponential window function is broadly used in this fashion, but a different terminology is used: exponential smoothing is equivalent to a first-order infinite-impulse response (IIR) filter and moving average is equivalent to a finite impulse response filter with equal weighting factors.

## Double exponential smoothing (Holt linear)

Simple exponential smoothing does not do well when there is a trend in the data. In such situations, several methods were devised under the name "double exponential smoothing" or "second-order exponential smoothing," which is the recursive application of an exponential filter twice, thus being termed "double exponential smoothing". The basic idea behind double exponential smoothing is to introduce a term to take into account the possibility of a series exhibiting some form of trend. This slope component is itself updated via exponential smoothing.

One method works as follows:

Again, the raw data sequence of observations is represented by $x_{t}$ , beginning at time $t=0$ . We use $s_{t}$ to represent the smoothed value for time t , and $b_{t}$ is our best estimate of the trend at time t . The output of the algorithm is now written as $F_{t+m}$ , an estimate of the value of $x_{t+m}$ at time $m>0$ based on the raw data up to time t . Double exponential smoothing is given by the formulas

${\begin{aligned}s_{0}&=x_{0}\\b_{0}&=x_{1}-x_{0}\\\end{aligned}}$

and for $t>0$ by

${\begin{aligned}s_{t}&=\alpha x_{t}+(1-\alpha )(s_{t-1}+b_{t-1})\\b_{t}&=\beta (s_{t}-s_{t-1})+(1-\beta )b_{t-1}\\\end{aligned}}$

where $\alpha$ ( $0\leq \alpha \leq 1$ ) is the *data smoothing factor*, and $\beta$ ( $0\leq \beta \leq 1$ ) is the *trend smoothing factor*.

To forecast beyond $x_{t}$ is given by the following approximation:

$F_{t+m}=s_{t}+m\cdot b_{t}$

.

Setting the initial value b is a matter of preference. An option other than the one listed above is ${\textstyle {\frac {x_{n}-x_{0}}{n}}}$ for some n .

Note that *F*0 is undefined (there is no estimation for time 0), and according to the definition *F*1=*s*0+*b*0, which is well defined, thus further values can be evaluated.

A second method, referred to as either Brown's linear exponential smoothing (LES) or Brown's double exponential smoothing, has only one smoothing factor, $\alpha$ :

${\begin{aligned}s'_{0}&=x_{0}\\s''_{0}&=x_{0}\\s'_{t}&=\alpha x_{t}+(1-\alpha )s'_{t-1}\\s''_{t}&=\alpha s'_{t}+(1-\alpha )s''_{t-1}\\F_{t+m}&=a_{t}+mb_{t},\end{aligned}}$

where *a**t*, the estimated level at time *t*, and *b**t*, the estimated trend at time *t*, are given by

${\begin{aligned}a_{t}&=2s'_{t}-s''_{t}\\[5pt]b_{t}&={\frac {\alpha }{1-\alpha }}(s'_{t}-s''_{t}).\end{aligned}}$

## Triple exponential smoothing (Holt–Winters)

Triple exponential smoothing applies exponential smoothing three times, which is commonly used when there are three high frequency signals to be removed from a time series under study. There are different types of seasonality: 'multiplicative' and 'additive' in nature. Multiplicative signifies that the seasonal effect size depends on the current level, while additive seasonal effects do not.

If in *every* summer we sell 10,000 more balls of ice cream than we do in winter, then seasonality is *additive*. However, if we sell 6 times more ice cream in summer than in winter, that means that the difference in sales amounts moves together with the level itself: in years with overall larger consumption, the difference between summer and winter is larger and vice versa. The effect is thus *multiplicative*. Multiplicative seasonality can be represented as a constant factor, additive seasonality as an absolute amount.

Triple exponential smoothing was first suggested by Holt's student, Peter Winters, in 1960 after reading a signal processing book from the 1940s on exponential smoothing. Holt's novel idea was to repeat filtering an odd number of times greater than 1 and less than 5, which was popular with scholars of previous eras. While recursive filtering had been used previously, it was applied twice and four times to coincide with the Hadamard conjecture, while triple application required more than double the operations of singular convolution. The use of a triple application is considered a rule of thumb technique, rather than one based on theoretical foundations and has often been overemphasized by practitioners.

Suppose we have a sequence of observations $x_{t},$ beginning at time $t=0$ with a cycle of seasonal change of length L . The method calculates a trend line for the data as well as seasonal indices that weight the values in the trend line based on where that time point falls in the cycle of length L .

Let $s_{t}$ represent the smoothed value of the constant part for time t , $b_{t}$ is the sequence of best estimates of the linear trend that are superimposed on the seasonal changes, and $c_{t}$ is the sequence of seasonal correction factors. We wish to estimate $c_{t}$ at every time t mod L in the cycle that the observations take on. As a rule of thumb, a minimum of two full seasons (or $2L$ periods) of historical data is needed to initialize a set of seasonal factors.

The output of the algorithm is again written as $F_{t+m}$ , an estimate of the value of $x_{t+m}$ at time $t+m>0$ based on the raw data up to time t . Triple exponential smoothing with multiplicative seasonality is given by the formulas

${\begin{aligned}s_{0}&=x_{0}\\[5pt]s_{t}&=\alpha {\frac {x_{t}}{c_{t-L}}}+(1-\alpha )(s_{t-1}+b_{t-1})\\[5pt]b_{t}&=\beta (s_{t}-s_{t-1})+(1-\beta )b_{t-1}\\[5pt]c_{t}&=\gamma {\frac {x_{t}}{s_{t}}}+(1-\gamma )c_{t-L}\\[5pt]F_{t+m}&=(s_{t}+mb_{t})c_{t-L+1+(m-1){\bmod {L}}},\end{aligned}}$

where $\alpha$ ( $0\leq \alpha \leq 1$ ) is the *data smoothing factor*, $\beta$ ( $0\leq \beta \leq 1$ ) is the *trend smoothing factor*, and $\gamma$ ( $0\leq \gamma \leq 1$ ) is the *seasonal change smoothing factor*.

The general formula for the initial trend estimate b is

${\begin{aligned}b_{0}&={\frac {1}{L}}\left({\frac {x_{L+1}-x_{1}}{L}}+{\frac {x_{L+2}-x_{2}}{L}}+\cdots +{\frac {x_{L+L}-x_{L}}{L}}\right)\end{aligned}}$

.

Setting the initial estimates for the seasonal indices $c_{i}$ for $i=1,2,\ldots ,L$ is a bit more involved. If N is the number of complete cycles present in your data, then

$c_{i}={\frac {1}{N}}\sum _{j=1}^{N}{\frac {x_{L(j-1)+i}}{A_{j}}}\quad {\text{for }}i=1,2,\ldots ,L$

where

$A_{j}={\frac {\sum _{k=1}^{L}x_{L(j-1)+k}}{L}}\quad {\text{for }}j=1,2,\ldots ,N$

.

Note that $A_{j}$ is the average value of x in the $j^{\text{th}}$ cycle of your data.

This results in

$c_{i}={\frac {1}{N}}\sum _{j=1}^{N}{\frac {x_{L(j-1)+i}}{{\frac {1}{L}}\sum _{k=1}^{L}x_{L(j-1)+k}}}$

Triple exponential smoothing with additive seasonality is given by

${\begin{aligned}s_{0}&=x_{0}\\s_{t}&=\alpha (x_{t}-c_{t-L})+(1-\alpha )(s_{t-1}+b_{t-1})\\b_{t}&=\beta (s_{t}-s_{t-1})+(1-\beta )b_{t-1}\\c_{t}&=\gamma (x_{t}-s_{t-1}-b_{t-1})+(1-\gamma )c_{t-L}\\F_{t+m}&=s_{t}+mb_{t}+c_{t-L+1+(m-1){\bmod {L}}}.\\\end{aligned}}$

## Implementations in statistics packages

- R: the HoltWinters function in the stats package and ets function in the forecast package (a more complete implementation, generally resulting in a better performance).
- Python: the holtwinters module of the statsmodels package allow for simple, double and triple exponential smoothing.
- IBM SPSS includes Simple, Simple Seasonal, Holt's Linear Trend, Brown's Linear Trend, Damped Trend, Winters' Additive, and Winters' Multiplicative in the Time-Series modeling procedure within its Statistics and Modeler statistical packages. The default Expert Modeler feature evaluates all seven exponential smoothing models and ARIMA models with a range of nonseasonal and seasonal *p*, *d*, and *q* values, and selects the model with the lowest Bayesian Information Criterion statistic.
- Stata: tssmooth command
- LibreOffice 5.2
- Microsoft Excel 2016
- Julia: TrendDecomposition.jl package implements simple and double exponential smoothing and Holts-Winters forecasting procedure.

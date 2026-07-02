---
title: "Smoothing"
source: https://en.wikipedia.org/wiki/Smoothing
domain: state-space-models
license: CC-BY-SA-4.0
tags: state-space model, hidden Markov model, dynamic linear model, recursive estimation
fetched: 2026-07-02
---

# Smoothing

In statistics and image processing, to **smooth** a data set is to create an approximating function that attempts to capture important patterns in the data, while leaving out noise or other fine-scale structures/rapid phenomena. In smoothing, the data points of a signal are modified so individual points higher than the adjacent points (presumably because of noise) are reduced, and points that are lower than the adjacent points are increased, leading to a smoother signal.

Reducing noise by smoothing may aid in data analysis in two notable ways:

1. Help uncover more meaningful information from the underlying data, such as trends.
2. Provide analyses that are both flexible and robust.

Many different algorithms are used in smoothing, most commonly binning, kernels, and local weighted regression.

## Compared to curve fitting

Smoothing may be distinguished from the related and partially overlapping concept of curve fitting in the following ways:

- curve fitting often involves the use of an explicit function form for the result, whereas the immediate results from smoothing are the "smoothed" values with no later use made of a functional form if there is one;
- the aim of smoothing is to give a general idea of relatively slow changes of value with little attention paid to the close matching of data values, while curve fitting concentrates on achieving as close a match as possible.
- smoothing methods often have an associated tuning parameter which is used to control the extent of smoothing. Curve fitting will adjust any number of parameters of the function to obtain the 'best' fit.

## Linear smoothers

In the case that the smoothed values can be written as a linear transformation of the observed values, the smoothing operation is known as a **linear smoother**; the matrix representing the transformation is known as a **smoother matrix** or hat matrix.

The operation of applying such a matrix transformation is called convolution. Thus the matrix is also called convolution matrix or a convolution kernel. In the case of simple series of data points (rather than a multi-dimensional image), the convolution kernel is a one-dimensional vector.

## Algorithms

One of the most common algorithms is the "moving average", often used to try to capture important trends in repeated statistical surveys. In image processing and computer vision, smoothing ideas are used in scale space representations. The simplest smoothing algorithm is the "rectangular" or "unweighted sliding-average smooth". This method replaces each point in the signal with the average of "m" adjacent points, where "m" is a positive integer called the "smooth width". Usually m is an odd number. The *triangular smooth* is like the *rectangular smooth* except that it implements a weighted smoothing function.

Some specific smoothing and filter types, with their respective uses, pros and cons are:

| Algorithm | Overview and uses | Pros | Cons |
|---|---|---|---|
| Additive smoothing | used to smooth categorical data. |   |   |
| Butterworth filter | Slower roll-off than a Chebyshev Type I/Type II filter or an elliptic filter | More linear phase response in the passband than Chebyshev Type I/Type II and elliptic filters can achieve. Designed to have a frequency response as flat as possible in the passband. | requires a higher order to implement a particular stopband specification |
| Chebyshev filter | Has a steeper roll-off and more passband ripple (type I) or stopband ripple (type II) than Butterworth filters. | Minimizes the error between the idealized and the actual filter characteristic over the range of the filter | Contains ripples in the passband. |
| Digital filter | Used on a sampled, discrete-time signal to reduce or enhance certain aspects of that signal |   |   |
| Elliptic filter |   |   |   |
| Exponential smoothing | Used to reduce irregularities (random fluctuations) in time series data, thus providing a clearer view of the true underlying behaviour of the series. Also, provides an effective means of predicting future values of the time series (forecasting). |   |   |
| Kalman filter | Uses a series of measurements observed over time, containing statistical noise and other inaccuracies by estimating a joint probability distribution over the variables for each timeframe. | Estimates of unknown variables it produces tend to be more accurate than those based on a single measurement alone, when assumptions are met. | Assumes and therefore requires knowledge of how the system generating the data-points advances in time and how the measurements are acquired. |
| Kernel smoother | used to estimate a real valued function as the weighted average of neighboring observed data. most appropriate when the dimension of the predictor is low (*p* < 3), for example for data visualization. | The estimated function is smooth, and the level of smoothness is set by a single parameter. |   |
| Kolmogorov–Zurbenko filter | A type of low-pass filter Uses a series of iterations of a moving average filter of length *m*, where *m* is a positive, odd integer. | robust and nearly optimal performs well in a missing data environment, especially in multidimensional time and space where missing data can cause problems arising from spatial sparseness the two parameters each have clear interpretations so that it can be easily adopted by specialists in different areas Software implementations for time series, longitudinal and spatial data have been developed in the popular statistical package R, which facilitate the use of the KZ filter and its extensions in different areas. |   |
| Laplacian smoothing | algorithm to smooth a polygonal mesh. |   |   |
| Local regression also known as "loess" or "lowess" | A generalization of moving average and polynomial regression. Generalizes a Savitzky–Golay smoothing filter to non-regular sampling instances. | fitting simple models to localized subsets of the data to build up a function that describes the deterministic part of the variation in the data, point by point one of the chief attractions of this method is that the data analyst is not required to specify a global function of any form to fit a model to the data, only to fit segments of the data. | increased computation. Because it is so computationally intensive, LOESS would have been practically impossible to use in the era when least squares regression was being developed. |
| Low-pass filter | A filter that passes signals with a frequency lower than a selected cutoff frequency and attenuates signals with frequencies higher than the cutoff frequency. Used for continuous time realization and discrete time realization. |   |   |
| Moving average | A calculation to analyze data points by creating a series of averages of different subsets of the full data set. a smoothing technique used to make the long term trends of a time series clearer. the first element of the moving average is obtained by taking the average of the initial fixed subset of the number series commonly used with time series data to smooth out short-term fluctuations and highlight longer-term trends or cycles. | has been adjusted to allow for seasonal or cyclical components of a time series |   |
| Ramer–Douglas–Peucker algorithm | decimates a curve composed of line segments to a similar curve with fewer points. |   |   |
| Savitzky–Golay smoothing filter | Based on the least-squares fitting of polynomials to segments of the data. A specific case of Local regression ("loess" or "lowess") when the sampling instances are regular. |   |   |
| Smoothing spline |   |   |   |
| Stretched grid method | a numerical technique for finding approximate solutions of various mathematical and engineering problems that can be related to an elastic grid behavior meteorologists use the stretched grid method for weather prediction engineers use the stretched grid method to design tents and other tensile structures. |   |   |

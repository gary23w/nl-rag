---
title: "Andrews plot"
source: https://en.wikipedia.org/wiki/Andrews_plot
domain: parallel-coordinates
license: CC-BY-SA-4.0
tags: parallel coordinates, andrews plot, high dimensional, multivariate plot
fetched: 2026-07-02
---

# Andrews plot

In data visualization, an **Andrews plot** or **Andrews curve** is a way to visualize structure in high-dimensional data. It is basically a rolled-down, non-integer version of the Kent–Kiviat radar m chart, or a smoothed version of a parallel coordinate plot. It is named after the statistician David F. Andrews.

A value x is a high-dimensional datapoint if it is an element of $\mathbb {R} ^{d}$ . We can represent high-dimensional data with a number for each of their dimensions, $x=\left\{x_{1},x_{2},\ldots ,x_{d}\right\}$ . To visualize them, the Andrews plot defines a finite Fourier series:

$f_{x}(t)={\frac {x_{1}}{\sqrt {2}}}+x_{2}\sin(t)+x_{3}\cos(t)+x_{4}\sin(2t)+x_{5}\cos(2t)+\cdots$

This function is then plotted for $-\pi <t<\pi$ . Thus each data point may be viewed as a line between $-\pi$ and $\pi$ . This formula can be thought of as the projection of the data point onto the vector:

$\left({\frac {1}{\sqrt {2}}},\sin(t),\cos(t),\sin(2t),\cos(2t),\ldots \right)$

If there is structure in the data, it may be visible in the Andrews curves of the data.

These curves have been utilized in fields as different as biology, neurology, sociology and semiconductor manufacturing. Some of their uses include the quality control of products, the detection of period and outliers in time series, the visualization of learning in artificial neural networks, and correspondence analysis.

Theoretically, it is possible to project them onto an *n*-sphere. The projection onto the circle results in the aforementioned radar chart.

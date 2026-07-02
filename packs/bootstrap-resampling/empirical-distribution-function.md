---
title: "Empirical distribution function"
source: https://en.wikipedia.org/wiki/Empirical_distribution_function
domain: bootstrap-resampling
license: CC-BY-SA-4.0
tags: bootstrapping statistics, confidence interval, empirical distribution, standard error
fetched: 2026-07-02
---

# Empirical distribution function

The green curve, which asymptotically approaches heights of 0 and 1 without reaching them, is the true

cumulative distribution function

of the

standard normal distribution

. The grey hash marks represent the observations in a particular

sample

drawn from that distribution, and the horizontal steps of the blue step function (including the leftmost point in each step but not including the rightmost point) form the empirical distribution function of that sample. (

)

In statistics, an **empirical distribution function** (a.k.a. an **empirical cumulative distribution function**, **eCDF**) is the distribution function associated with the empirical measure of a sample. This cumulative distribution function is a step function that jumps up by 1/*n* at each of the *n* data points. Its value at any specified value of the measured variable is the fraction of observations of the measured variable that are less than or equal to the specified value.

The empirical distribution function is an estimate of the cumulative distribution function that generated the points in the sample. It converges with probability 1 to that underlying distribution, according to the Glivenko–Cantelli theorem. A number of results exist to quantify the rate of convergence of the empirical distribution function to the underlying cumulative distribution function. A simple empirical estimate is the frequency distribution.

## Definition

Let (*X*1, …, *X**n*) be independent, identically distributed real random variables with the common cumulative distribution function *F*(*t*). Then the **empirical distribution function** is defined as ${\widehat {F}}_{n}(t)={\frac {{\text{number of elements in the sample}}\leq t}{n}}={\frac {1}{n}}\sum _{i=1}^{n}\mathbf {1} _{X_{i}\leq t},$ where $\mathbf {1} _{A}$ is the indicator of event *A*. For a fixed *t*, the indicator $\mathbf {1} _{X_{i}\leq t}$ is a Bernoulli random variable with parameter *p* = *F*(*t*); hence $n{\widehat {F}}_{n}(t)$ is a binomial random variable with mean *nF*(*t*) and variance *nF*(*t*)(1 − *F*(*t*)). This implies that ${\widehat {F}}_{n}(t)$ is an unbiased estimator for *F*(*t*).

In some textbooks, the empirical distribution function is defined as ${\widehat {F}}_{n}(t)={\frac {1}{n+1}}\sum _{i=1}^{n}\mathbf {1} _{X_{i}\leq t}$ However, since the ratio (*n* + 1)/*n* approaches 1 as *n* goes to infinity, the asymptotic properties of the two definitions are the same.

## Asymptotic properties

By the strong law of large numbers, the estimator ${\widehat {F}}_{n}(t)$ converges to *F*(*t*) as *n* → ∞ almost surely, for every value of *t*: ${\widehat {F}}_{n}(t)\ {\xrightarrow {\text{a.s.}}}\ F(t);$ thus the estimator ${\widehat {F}}_{n}(t)$ is consistent. This expression asserts the pointwise convergence of the empirical distribution function to the true cumulative distribution function. There is a stronger result, called the Glivenko–Cantelli theorem, which states that the convergence in fact happens uniformly over *t*: $\left\|{\widehat {F}}_{n}-F\right\|_{\infty }\equiv \sup _{t\in \mathbb {R} }\left|{\widehat {F}}_{n}(t)-F(t)\right|\xrightarrow {} \ 0.$ The sup-norm in this expression is called the Kolmogorov–Smirnov statistic for testing the goodness-of-fit between the empirical distribution ${\textstyle {\widehat {F}}_{n}(t)}$ and the assumed true cumulative distribution function *F*. Other norm functions may be reasonably used here instead of the sup-norm. For example, the L2-norm gives rise to the Cramér–von Mises statistic.

The asymptotic distribution can be further characterized in several different ways. First, the central limit theorem states that *pointwise*, ${\textstyle {\widehat {F}}_{n}(t)}$ has asymptotically normal distribution with the standard ${\textstyle {\sqrt {n}}}$ rate of convergence: ${\sqrt {n}}{\big (}{\widehat {F}}_{n}(t)-F(t){\big )}\ \ {\xrightarrow {d}}\ \ {\mathcal {N}}{\Big (}0,F(t){\big (}1-F(t){\big )}{\Big )}.$ This result is extended by the Donsker’s theorem, which asserts that the *empirical process* ${\textstyle {\sqrt {n}}({\widehat {F}}_{n}-F)}$ , viewed as a function indexed by ${\textstyle t\in \mathbb {R} }$ , converges in distribution in the Skorokhod space $D[-\infty ,+\infty ]$ to the mean-zero Gaussian process ${\textstyle G_{F}=B\circ F}$ , where *B* is the standard Brownian bridge. The covariance structure of this Gaussian process is $\operatorname {E} [\,G_{F}(t_{1})G_{F}(t_{2})\,]=F(t_{1}\wedge t_{2})-F(t_{1})F(t_{2}).$ The uniform rate of convergence in Donsker’s theorem can be quantified by the result known as the Hungarian embedding: $\limsup _{n\to \infty }{\frac {\sqrt {n}}{\ln ^{2}n}}\left\|{\sqrt {n}}({\widehat {F}}_{n}-F)-G_{F,n}\right\|_{\infty }<\infty ,\quad {\text{a.s.}}$

Alternatively, the rate of convergence of ${\sqrt {n}}({\widehat {F}}_{n}-F)$ can also be quantified in terms of the asymptotic behavior of the sup-norm of this expression. Number of results exist in this venue, for example the Dvoretzky–Kiefer–Wolfowitz inequality provides bound on the tail probabilities of ${\textstyle {\sqrt {n}}\left\|{\widehat {F}}_{n}-F\right\|_{\infty }}$ : $\Pr \!{\Big (}{\sqrt {n}}\|{\widehat {F}}_{n}-F\|_{\infty }>z{\Big )}\leq 2e^{-2z^{2}}.$ In fact, Kolmogorov has shown that if the cumulative distribution function *F* is continuous, then the expression ${\textstyle {\sqrt {n}}\left\|{\widehat {F}}_{n}-F\right\|_{\infty }}$ converges in distribution to ${\textstyle \left\|B\right\|_{\infty }}$ , which has the Kolmogorov distribution that does not depend on the form of *F*.

Another result, which follows from the law of the iterated logarithm, is that $\limsup _{n\to \infty }{\sqrt {\frac {n}{2\ln \ln n}}}\left\|{\widehat {F}}_{n}-F\right\|_{\infty }\leq {\frac {1}{2}},\quad {\text{a.s.}}$ and $\liminf _{n\to \infty }{\sqrt {2n\ln \ln n}}\left\|{\widehat {F}}_{n}-F\right\|_{\infty }={\frac {\pi }{2}},\quad {\text{a.s.}}$

## Confidence intervals

As per Dvoretzky–Kiefer–Wolfowitz inequality the interval that contains the true CDF, $F(x)$ , with probability $1-\alpha$ is specified as

$F_{n}(x){-}\varepsilon \leq F(x)\leq F_{n}(x){+}\varepsilon \;{\text{ where }}\varepsilon ={\sqrt {\frac {\ln {\frac {2}{\alpha }}}{2n}}}.$

As per the above bounds, we can plot the Empirical CDF, CDF and confidence intervals for different distributions by using any one of the statistical implementations.

## Statistical implementation

A non-exhaustive list of software implementations of Empirical Distribution function includes:

- In R software, we compute an empirical cumulative distribution function, with several methods for plotting, printing and computing with such an “ecdf” object.
- In GNU Octave or MATLAB we can use Empirical cumulative distribution function (cdf) plot
- jmp from SAS, the CDF plot creates a plot of the empirical cumulative distribution function.
- Minitab, create an Empirical CDF
- Mathwave, we can fit probability distribution to our data
- Dataplot, we can plot Empirical CDF plot
- Scipy, we can use scipy.stats.ecdf
- Statsmodels, we can use statsmodels.distributions.empirical_distribution.ECDF
- Matplotlib, using the matplotlib.pyplot.ecdf function (new in version 3.8.0)
- Seaborn, using the seaborn.ecdfplot function
- Plotly, using the plotly.express.ecdf function
- Excel, we can plot Empirical CDF plot
- ArviZ, using the az.plot_dist function

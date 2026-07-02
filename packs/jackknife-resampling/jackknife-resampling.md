---
title: "Jackknife resampling"
source: https://en.wikipedia.org/wiki/Jackknife_resampling
domain: jackknife-resampling
license: CC-BY-SA-4.0
tags: jackknife resampling, bias estimator, standard error, resampling method
fetched: 2026-07-02
---

# Jackknife resampling

In statistics, the **jackknife** (jackknife cross-validation) is a cross-validation technique and, therefore, a form of resampling. It is especially useful for bias and variance estimation. The jackknife pre-dates other common resampling methods such as the bootstrap. Given a sample of size n , a jackknife estimator can be built by aggregating the parameter estimates from each subsample of size $(n-1)$ obtained by omitting one observation. The jackknife is a linear approximation of the bootstrap.

The jackknife technique was developed by Maurice Quenouille (1924–1973) from 1949 and refined in 1956. John Tukey expanded on the technique in 1958 and proposed the name "jackknife" because, like a physical jack-knife (a compact folding knife), it is a rough-and-ready tool that can improvise a solution for a variety of problems even though specific problems may be more efficiently solved with a purpose-designed tool.

## A simple example: mean estimation

The jackknife estimator of a parameter is found by systematically leaving out each observation from a dataset and calculating the parameter estimate over the remaining observations and then aggregating these calculations.

For example, if the parameter to be estimated is the population mean of random variable *x*, then for a given set of i.i.d. observations $x_{1},...,x_{n}$ the natural estimator is the sample mean: ${\bar {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}={\frac {1}{n}}\sum _{i\in [n]}x_{i},$ where the last sum used another way to indicate that the index i runs over the set $[n]=\{1,\ldots ,n\}$ .

Then we proceed as follows: For each $i\in [n]$ we compute the mean ${\bar {x}}_{(i)}$ of the jackknife subsample consisting of all but the i -th data point, and this is called the i -th jackknife replicate: ${\bar {x}}_{(i)}={\frac {1}{n-1}}\sum _{j\in [n],j\neq i}x_{j},\qquad i=1,\dots ,n.$

It could help to think that these n jackknife replicates ${\bar {x}}_{(1)},\ldots ,{\bar {x}}_{(n)}$ approximate the distribution of the sample mean ${\bar {x}}$ . A larger n improves the approximation. Then finally to get the jackknife estimator, the n jackknife replicates are averaged: ${\bar {x}}_{\text{jack}}={\frac {1}{n}}\sum _{i=1}^{n}{\bar {x}}_{(i)}.$

One may ask about the bias and the variance of ${\bar {x}}_{\text{jack}}$ . From the definition of ${\bar {x}}_{\text{jack}}$ as the average of the jackknife replicates, one could try to calculate explicitly. The bias is a trivial calculation, but the variance of ${\bar {x}}_{\text{jack}}$ is more involved, since the jackknife replicates are not independent.

For the special case of the mean, one can show explicitly that the jackknife estimate equals the usual estimate: ${\frac {1}{n}}\sum _{i=1}^{n}{\bar {x}}_{(i)}={\bar {x}}.$ This establishes the identity ${\bar {x}}_{\text{jack}}={\bar {x}}$ . Then taking expectations, we get $E[{\bar {x}}_{\text{jack}}]=E[{\bar {x}}]=E[x]$ , so ${\bar {x}}_{\text{jack}}$ is unbiased, while taking variance, we get $V[{\bar {x}}_{\text{jack}}]=V[{\bar {x}}]=V[x]/n$ . However, these properties do not generally hold for parameters other than the mean.

This simple example for the case of mean estimation is just to illustrate the construction of a jackknife estimator, while the real subtleties (and the usefulness) emerge for the case of estimating other parameters, such as higher moments than the mean or other functionals of the distribution.

${\bar {x}}_{\text{jack}}$ could be used to construct an empirical estimate of the bias of ${\bar {x}}$ , namely ${\widehat {\operatorname {bias} }}({\bar {x}})_{\text{jack}}=c({\bar {x}}_{\text{jack}}-{\bar {x}})$ with some suitable factor $c>0$ , although in this case we know that ${\bar {x}}_{\text{jack}}={\bar {x}}$ , so this construction does not add any meaningful knowledge, but it gives the correct estimation of the bias (which is zero).

A jackknife estimate of the variance of ${\bar {x}}$ can be calculated from the variance of the jackknife replicates ${\bar {x}}_{(i)}$ : ${\widehat {\operatorname {var} }}({\bar {x}})_{\text{jack}}={\frac {n-1}{n}}\sum _{i=1}^{n}({\bar {x}}_{(i)}-{\bar {x}}_{\text{jack}})^{2}={\frac {1}{n(n-1)}}\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}.$ The left equality defines the estimator ${\widehat {\operatorname {var} }}({\bar {x}})_{\text{jack}}$ , and the right equality is an identity that can be verified directly. Then taking expectations, we get $E[{\widehat {\operatorname {var} }}({\bar {x}})_{\text{jack}}]=V[x]/n=V[{\bar {x}}]$ , so this is an unbiased estimator of the variance of ${\bar {x}}$ .

## Estimating the bias of an estimator

The jackknife technique can be used to estimate (and correct) the bias of an estimator calculated over the entire sample.

Suppose $\theta$ is the target parameter of interest, which is assumed to be some functional of the distribution of x . Based on a finite set of observations $x_{1},...,x_{n}$ , which is assumed to consist of i.i.d. copies of x , the estimator ${\hat {\theta }}$ is constructed:

${\hat {\theta }}=f_{n}(x_{1},\ldots ,x_{n}).$

The value of ${\hat {\theta }}$ is sample-dependent, so this value will change from one random sample to another.

By definition, the bias of ${\hat {\theta }}$ is as follows:

${\text{bias}}({\hat {\theta }})=E[{\hat {\theta }}]-\theta .$

One may wish to compute several values of ${\hat {\theta }}$ from several samples, and average them, to calculate an empirical approximation of $E[{\hat {\theta }}]$ , but this is impossible when there are no "other samples" when the entire set of available observations $x_{1},...,x_{n}$ was used to calculate ${\hat {\theta }}$ . In this kind of situation the jackknife resampling technique may be of help.

We construct the jackknife replicates:

${\hat {\theta }}_{(1)}=f_{n-1}(x_{2},x_{3}\ldots ,x_{n})$

${\hat {\theta }}_{(2)}=f_{n-1}(x_{1},x_{3},\ldots ,x_{n})$

$\vdots$

${\hat {\theta }}_{(n)}=f_{n-1}(x_{1},x_{2},\ldots ,x_{n-1})$

where each replicate is a "leave-one-out" estimate based on the jackknife subsample consisting of all but one of the data points:

${\hat {\theta }}_{(i)}=f_{n-1}(x_{1},\ldots ,x_{i-1},x_{i+1},\ldots ,x_{n})\quad \quad i=1,\dots ,n.$

Then we define their average:

${\hat {\theta }}_{\mathrm {jack} }={\frac {1}{n}}\sum _{i=1}^{n}{\hat {\theta }}_{(i)}$

The jackknife estimate of the bias of ${\hat {\theta }}$ is given by:

${\widehat {\text{bias}}}({\hat {\theta }})_{\mathrm {jack} }=(n-1)({\hat {\theta }}_{\mathrm {jack} }-{\hat {\theta }})$

and the resulting bias-corrected jackknife estimate of $\theta$ is given by:

${\hat {\theta }}_{\text{jack}}^{*}={\hat {\theta }}-{\widehat {\text{bias}}}({\hat {\theta }})_{\mathrm {jack} }=n{\hat {\theta }}-(n-1){\hat {\theta }}_{\mathrm {jack} }.$

This removes the bias in the special case that the bias is $O(n^{-1})$ and reduces it to $O(n^{-2})$ in other cases.

## Estimating the variance of an estimator

The jackknife technique can be also used to estimate the variance of an estimator calculated over the entire sample.

## Literature

- *Berger, Y.G. (2007). "A jackknife variance estimator for unistage stratified samples with unequal probabilities". *Biometrika*. **94** (4): 953–964. doi:10.1093/biomet/asm072.*
- *Berger, Y.G.; Rao, J.N.K. (2006). "Adjusted jackknife for imputation under unequal probability sampling without replacement". *Journal of the Royal Statistical Society, Series B*. **68** (3): 531–547. doi:10.1111/j.1467-9868.2006.00555.x.*
- *Berger, Y.G.; Skinner, C.J. (2005). "A jackknife variance estimator for unequal probability sampling". *Journal of the Royal Statistical Society, Series B*. **67** (1): 79–89. doi:10.1111/j.1467-9868.2005.00489.x.*
- *Jiang, J.; Lahiri, P.; Wan, S-M. (2002). "A unified jackknife theory for empirical best prediction with M-estimation". *The Annals of Statistics*. **30** (6): 1782–810. doi:10.1214/aos/1043351257.*
- *Jones, H.L. (1974). "Jackknife estimation of functions of stratum means". *Biometrika*. **61** (2): 343–348. doi:10.2307/2334363. JSTOR 2334363.*
- *Kish, L.; Frankel, M.R. (1974). "Inference from complex samples". *Journal of the Royal Statistical Society, Series B*. **36** (1): 1–37.*
- *Krewski, D.; Rao, J.N.K. (1981). "Inference from stratified samples: properties of the linearization, jackknife and balanced repeated replication methods". *The Annals of Statistics*. **9** (5): 1010–1019. doi:10.1214/aos/1176345580.*
- *Quenouille, M.H. (1956). "Notes on bias in estimation". *Biometrika*. **43** (3–4): 353–360. doi:10.1093/biomet/43.3-4.353.*
- *Rao, J.N.K.; Shao, J. (1992). "Jackknife variance estimation with survey data under hot deck imputation". *Biometrika*. **79** (4): 811–822. doi:10.1093/biomet/79.4.811.*
- *Rao, J.N.K.; Wu, C.F.J.; Yue, K. (1992). "Some recent work on resampling methods for complex surveys". *Survey Methodology*. **18** (2): 209–217.*
- Shao, J. and Tu, D. (1995). The Jackknife and Bootstrap. Springer-Verlag, Inc.
- *Tukey, J.W. (1958). "Bias and confidence in not-quite large samples (abstract)". *The Annals of Mathematical Statistics*. **29** (2): 614.*
- *Wu, C.F.J. (1986). "Jackknife, Bootstrap and other resampling methods in regression analysis". *The Annals of Statistics*. **14** (4): 1261–1295. doi:10.1214/aos/1176350142.*

---
title: "Goodness of fit"
source: https://en.wikipedia.org/wiki/Goodness_of_fit
domain: chi-squared-tests
license: CC-BY-SA-4.0
tags: chi-squared test, contingency table, goodness of fit, G-test
fetched: 2026-07-02
---

# Goodness of fit

The **goodness of fit** of a statistical model describes how well it fits a set of observations. Measures of goodness of fit typically summarize the discrepancy between observed values and the values expected under the model in question. Such measures can be used in statistical hypothesis testing, e.g. to test for normality of residuals, to test whether two samples are drawn from identical distributions (see Kolmogorov–Smirnov test), or whether outcome frequencies follow a specified distribution (see Pearson's chi-square test). In the analysis of variance, one of the components into which the variance is partitioned may be a lack-of-fit sum of squares.

## Fit of distributions

In assessing whether a given distribution is suited to a data-set, the following tests and their underlying measures of fit can be used:

- Bayesian information criterion
- Kolmogorov–Smirnov test
- Cramér–von Mises criterion
- Anderson–Darling test
- Berk-Jones tests
- Shapiro–Wilk test
- Chi-squared test
- Akaike information criterion
- Hosmer–Lemeshow test
- Kuiper's test
- Kernelized Stein discrepancy
- Zhang's ZK, ZC and ZA tests
- Moran test
- Density Based Empirical Likelihood Ratio tests

## Regression analysis

In regression analysis, more specifically regression validation, the following topics relate to goodness of fit:

- Coefficient of determination (the R-squared measure of goodness of fit);
- Lack-of-fit sum of squares;
- Mallows's Cp criterion
- Prediction error
- Reduced chi-square

## Categorical data

The following are examples that arise in the context of categorical data.

### Pearson's chi-square test

Pearson's chi-square test uses a measure of goodness of fit which is the sum of differences between observed and expected outcome frequencies (that is, counts of observations), each squared and divided by the expectation:

$\chi ^{2}=\sum _{i=1}^{n}{{\frac {(O_{i}-E_{i})}{E_{i}}}^{2}}$ where:

- *Oi* = an observed count for bin *i*
- *Ei* = an expected count for bin *i*, asserted by the null hypothesis.

The expected frequency is calculated by: $E_{i}\,=\,{\bigg (}F(Y_{u})\,-\,F(Y_{l}){\bigg )}\,N$ where:

- *F* = the cumulative distribution function for the probability distribution being tested.
- *Yu* = the upper limit for bin *i*,
- *Yl* = the lower limit for bin *i*, and
- *N* = the sample size

The resulting value can be compared with a chi-square distribution to determine the goodness of fit. The chi-square distribution has (*k* − *c*) degrees of freedom, where *k* is the number of non-empty bins and *c* is the number of estimated parameters (including location and scale parameters and shape parameters) for the distribution plus one. For example, for a 3-parameter Weibull distribution, *c* = 4.

#### Binomial case

A binomial experiment is a sequence of independent trials in which the trials can result in one of two outcomes, success or failure. There are *n* trials each with probability of success, denoted by *p*. Provided that *np**i* ≫ 1 for every *i* (where *i* = 1, 2, ..., *k*), then

$\chi ^{2}=\sum _{i=1}^{k}{\frac {(N_{i}-np_{i})^{2}}{np_{i}}}=\sum _{\mathrm {all\ bins} }^{}{\frac {(\mathrm {O} -\mathrm {E} )^{2}}{\mathrm {E} }}.$

This has approximately a chi-square distribution with *k* − 1 degrees of freedom. The fact that there are *k* − 1 degrees of freedom is a consequence of the restriction ${\textstyle \sum N_{i}=n}$ . We know there are *k* observed bin counts, however, once any *k* − 1 are known, the remaining one is uniquely determined. Basically, one can say, there are only *k* − 1 freely determined bin counts, thus *k* − 1 degrees of freedom.

### *G*-test

*G*-tests are likelihood-ratio tests of statistical significance that are increasingly being used in situations where Pearson's chi-square tests were previously recommended.

The general formula for *G* is

$G=2\sum _{i}{O_{i}\cdot \ln \left({\frac {O_{i}}{E_{i}}}\right)},$

where ${\textstyle O_{i}}$ and ${\textstyle E_{i}}$ are the same as for the chi-square test, ${\textstyle \ln }$ denotes the natural logarithm, and the sum is taken over all non-empty bins. Furthermore, the total observed count should be equal to the total expected count: $\sum _{i}O_{i}=\sum _{i}E_{i}=N$ where ${\textstyle N}$ is the total number of observations.

*G*-tests have been recommended at least since the 1981 edition of the popular statistics textbook by Robert R. Sokal and F. James Rohlf.

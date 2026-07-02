---
title: "Score test"
source: https://en.wikipedia.org/wiki/Score_test
domain: hypothesis-testing-deep
license: CC-BY-SA-4.0
tags: hypothesis test, null hypothesis, statistical power, likelihood ratio test
fetched: 2026-07-02
---

# Score test

In statistics, the **score test** assesses constraints on statistical parameters based on the gradient of the likelihood function—known as the *score*—evaluated at the hypothesized parameter value under the null hypothesis. Intuitively, if the restricted estimator is near the maximum of the likelihood function, the score should not differ from zero by more than sampling error. While the finite sample distributions of score tests are generally unknown, they have an asymptotic χ2-distribution under the null hypothesis as first proved by C. R. Rao in 1948, a fact that can be used to determine statistical significance.

Since function maximization subject to equality constraints is most conveniently done using a Lagrangean expression of the problem, the score test can be equivalently understood as a test of the magnitude of the Lagrange multipliers associated with the constraints where, again, if the constraints are non-binding at the maximum likelihood, the vector of Lagrange multipliers should not differ from zero by more than sampling error. The equivalence of these two approaches was first shown by S. D. Silvey in 1959, which led to the name **Lagrange Multiplier (LM) test** that has become more commonly used, particularly in econometrics, since Breusch and Pagan's much-cited 1980 paper.

The main advantage of the score test over the Wald test and likelihood-ratio test is that the score test only requires the computation of the restricted estimator. This makes testing feasible when the unconstrained maximum likelihood estimate is a boundary point in the parameter space. Further, because the score test only requires the estimation of the likelihood function under the null hypothesis, it is less specific than the likelihood ratio test about the alternative hypothesis.

## Single-parameter test

### The statistic

Let L be the likelihood function which depends on a univariate parameter $\theta$ and let x be the data. The score $U(\theta )$ is defined as

$U(\theta )={\frac {\partial \log L(\theta \mid x)}{\partial \theta }}.$

The Fisher information is

$I(\theta )=-\operatorname {E} \left[\left.{\frac {\partial ^{2}}{\partial \theta ^{2}}}\log f(X;\theta )\,\right|\,\theta \right]\,,$

where ƒ is the probability density.

The statistic to test ${\mathcal {H}}_{0}:\theta =\theta _{0}$ is $S(\theta _{0})={\frac {U(\theta _{0})^{2}}{I(\theta _{0})}}$

which has an asymptotic distribution of $\chi _{1}^{2}$ , when ${\mathcal {H}}_{0}$ is true. While asymptotically identical, calculating the LM statistic using the outer-gradient-product estimator of the Fisher information matrix can lead to bias in small samples.

#### Note on notation

Note that some texts use an alternative notation, in which the statistic $S^{*}(\theta )={\sqrt {S(\theta )}}$ is tested against a normal distribution. This approach is equivalent and gives identical results.

### As most powerful test for small deviations

$\left({\frac {\partial \log L(\theta \mid x)}{\partial \theta }}\right)_{\theta =\theta _{0}}\geq C$

where L is the likelihood function, $\theta _{0}$ is the value of the parameter of interest under the null hypothesis, and C is a constant set depending on the size of the test desired (i.e. the probability of rejecting $H_{0}$ if $H_{0}$ is true; see Type I error).

The score test is the most powerful test for small deviations from $H_{0}$ . To see this, consider testing $\theta =\theta _{0}$ versus $\theta =\theta _{0}+h$ . By the Neyman–Pearson lemma, the most powerful test has the form

${\frac {L(\theta _{0}+h\mid x)}{L(\theta _{0}\mid x)}}\geq K;$

Taking the log of both sides yields

$\log L(\theta _{0}+h\mid x)-\log L(\theta _{0}\mid x)\geq \log K.$

The score test follows making the substitution (by Taylor series expansion)

$\log L(\theta _{0}+h\mid x)\approx \log L(\theta _{0}\mid x)+h\times \left({\frac {\partial \log L(\theta \mid x)}{\partial \theta }}\right)_{\theta =\theta _{0}}$

and identifying the C above with $\log(K)$ .

### Relationship with other hypothesis tests

If the null hypothesis is true, the likelihood ratio test, the Wald test, and the score test are asymptotically equivalent tests of hypotheses. When testing nested models, the statistics for each test then converge to a Chi-squared distribution with degrees of freedom equal to the difference in degrees of freedom in the two models. If the null hypothesis is not true, however, the statistics converge to a noncentral chi-squared distribution with possibly different noncentrality parameters.

## Multiple parameters

A more general score test can be derived when there is more than one parameter. Suppose that ${\widehat {\theta }}_{0}$ is the maximum likelihood estimate of $\theta$ under the null hypothesis $H_{0}$ while U and I are respectively, the score vector and the Fisher information matrix. Then

$U^{T}({\widehat {\theta }}_{0})I^{-1}({\widehat {\theta }}_{0})U({\widehat {\theta }}_{0})\sim \chi _{k}^{2}$

asymptotically under $H_{0}$ , where k is the number of constraints imposed by the null hypothesis and

$U({\widehat {\theta }}_{0})={\frac {\partial \log L({\widehat {\theta }}_{0}\mid x)}{\partial \theta }}$

and

$I({\widehat {\theta }}_{0})=-\operatorname {E} \left({\frac {\partial ^{2}\log L({\widehat {\theta }}_{0}\mid x)}{\partial \theta \,\partial \theta '}}\right).$

This can be used to test $H_{0}$ .

The actual formula for the test statistic depends on which estimator of the Fisher information matrix is being used.

## Special cases

In many situations, the score statistic reduces to another commonly used statistic.

In linear regression, the Lagrange multiplier test can be expressed as a function of the *F*-test.

When the data follows a normal distribution, the score statistic is the same as the t statistic.

When the data consists of binary observations, the score statistic is the same as the chi-squared statistic in the Pearson's chi-squared test.

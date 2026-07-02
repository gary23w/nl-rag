---
title: "Likelihood-ratio test"
source: https://en.wikipedia.org/wiki/Likelihood-ratio_test
domain: hypothesis-testing-deep
license: CC-BY-SA-4.0
tags: hypothesis test, null hypothesis, statistical power, likelihood ratio test
fetched: 2026-07-02
---

# Likelihood-ratio test

In statistics, the **likelihood-ratio test** is a hypothesis test that involves comparing the goodness of fit of two competing statistical models, typically one found by maximization over the entire parameter space and another found after imposing some constraint, based on the ratio of their likelihoods. If the more constrained model (i.e., the null hypothesis) is supported by the observed data, the two likelihoods should not differ by more than sampling error. Thus the likelihood-ratio test tests whether this ratio is significantly different from one, or equivalently whether its natural logarithm is significantly different from zero.

The likelihood-ratio test, also known as **Wilks test**, is the oldest of the three classical approaches to hypothesis testing, together with the Lagrange multiplier test and the Wald test. In fact, the latter two can be conceptualized as approximations to the likelihood-ratio test, and are asymptotically equivalent. In the case of comparing two models each of which has no unknown parameters, use of the likelihood-ratio test can be justified by the Neyman–Pearson lemma. The lemma demonstrates that the test has the highest power among all competitors.

## Definition

### General

Suppose that we have a statistical model with parameter space $\Theta$ . A null hypothesis is often stated by saying that the parameter $\theta$ lies in a specified subset $\Theta _{0}$ of $\Theta$ . The alternative hypothesis is thus that $\theta$ lies in the complement of $\Theta _{0}$ , i.e. in $\Theta ~\backslash ~\Theta _{0}$ , which is denoted by $\Theta _{0}^{\text{c}}$ . The likelihood ratio test statistic for the null hypothesis $H_{0}\,:\,\theta \in \Theta _{0}$ is given by:

$\lambda _{\text{LR}}=-2\ln \left[{\frac {~\sup _{\theta \in \Theta _{0}}{\mathcal {L}}(\theta )~}{~\sup _{\theta \in \Theta }{\mathcal {L}}(\theta )~}}\right]$

where the quantity inside the brackets is called the likelihood ratio. Here, the $\sup$ notation refers to the supremum. As all likelihoods are positive, and as the constrained maximum cannot exceed the unconstrained maximum, the likelihood ratio is bounded between zero and one and the likelihood ratio test statistic between 0 and infinity.

Often the likelihood-ratio test statistic is expressed as a difference between the log-likelihoods $\lambda _{\text{LR}}=-2\left[\ell (\theta _{0})-\ell ({\hat {\theta }})\right]$ where $\ell ({\hat {\theta }})\equiv \ln \left[\,\sup _{\theta \in \Theta }{\mathcal {L}}(\theta )\,\right]$ is the logarithm of the maximized likelihood function ${\mathcal {L}}$ , and $\ell (\theta _{0})$ is the maximal value in the special case that the null hypothesis is true (but not necessarily a value that maximizes ${\mathcal {L}}$ for the sampled data) and $\theta _{0}\in \Theta _{0}\qquad {\text{ and }}\qquad {\hat {\theta }}\in \Theta ~$ denote the respective arguments of the maxima and the allowed ranges they're embedded in. Multiplying by −2 ensures mathematically that (by Wilks' theorem) $\lambda _{\text{LR}}$ converges asymptotically to being χ²-distributed if the null hypothesis happens to be true. The finite-sample distributions of likelihood-ratio statistics are generally unknown.

The likelihood-ratio test requires that the models be nested – i.e. the more complex model can be transformed into the simpler model by imposing constraints on the former's parameters. Many common test statistics are tests for nested models and can be phrased as log-likelihood ratios or approximations thereof: e.g. the *Z*-test, the *F*-test, the *G*-test, and Pearson's chi-squared test; for an illustration with the one-sample *t*-test, see below.

If the models are not nested, then instead of the likelihood-ratio test, there is a generalization of the test that can usually be used: for details, see *relative likelihood*.

### Case of simple hypotheses

A simple-vs.-simple hypothesis test has completely specified models under both the null hypothesis and the alternative hypothesis, which for convenience are written in terms of fixed values of a notional parameter $\theta$ :

${\begin{aligned}H_{0}&:&\theta =\theta _{0},\\H_{1}&:&\theta =\theta _{1}.\end{aligned}}$ In this case, under either hypothesis, the distribution of the data is fully specified: there are no unknown parameters to estimate. For this case, a variant of the likelihood-ratio test is available:

$\Lambda (x)={\frac {~{\mathcal {L}}(\theta _{0}\mid x)~}{~{\mathcal {L}}(\theta _{1}\mid x)~}}.$

Some older references may use the reciprocal of the function above as the definition. Thus, the likelihood ratio is small if the alternative model is better than the null model.

The likelihood-ratio test provides the decision rule as follows:

- If $~\Lambda >c~$ , do not reject $H_{0}$ ;
- If $~\Lambda <c~$ , reject $H_{0}$ ;
- If $~\Lambda =c~$ , reject $H_{0}$ with probability $~q~$ .

The values c and q are usually chosen to obtain a specified significance level $\alpha$ , via the relation $q\Pr(\Lambda =c\mid H_{0})~+~\Pr(\Lambda <c\mid H_{0})~=~\alpha ~.$ The Neyman–Pearson lemma states that this likelihood-ratio test is the most powerful among all level $\alpha$ tests for this case.

## Interpretation

The likelihood ratio is a function of the data x ; therefore, it is a statistic, although unusual in that the statistic's value depends on a parameter, $\theta$ . The likelihood-ratio test rejects the null hypothesis if the value of this statistic is too small. How small is too small depends on the significance level of the test, i.e. on what probability of Type I error is considered tolerable (Type I errors consist of the rejection of a null hypothesis that is true).

The numerator corresponds to the likelihood of an observed outcome under the null hypothesis. The denominator corresponds to the maximum likelihood of an observed outcome, varying parameters over the whole parameter space. The numerator of this ratio is less than the denominator; so, the likelihood ratio is between 0 and 1. Low values of the likelihood ratio mean that the observed result was much less likely to occur under the null hypothesis as compared to the alternative. High values of the statistic mean that the observed outcome was nearly as likely to occur under the null hypothesis as the alternative, and so the null hypothesis cannot be rejected.

### An example

The following example is adapted and abridged from Stuart, Ord & Arnold (1999, §22.2).

Suppose that we have a random sample, of size n, from a population that is normally-distributed. Both the mean, μ, and the standard deviation, σ, of the population are unknown. We want to test whether the mean is equal to a given value, *μ*0 .

Thus, our null hypothesis is *H*0:  *μ* = *μ*0  and our alternative hypothesis is *H*1:  *μ* ≠ *μ*0 . The likelihood function is ${\mathcal {L}}(\mu ,\sigma \mid x)=\left(2\pi \sigma ^{2}\right)^{-n/2}\exp \left(-\sum _{i=1}^{n}{\frac {(x_{i}-\mu )^{2}}{2\sigma ^{2}}}\right)\,.$

With some calculation (omitted here), it can then be shown that $\lambda _{LR}=n\ln \left(1+{\frac {t^{2}}{n-1}}\right)$ where t is the t-statistic with *n* − 1 degrees of freedom. Hence we may use the known exact distribution of *t**n*−1 to draw inferences.

## Asymptotic distribution: Wilks’ theorem

If the distribution of the likelihood ratio corresponding to a particular null and alternative hypothesis can be explicitly determined then it can directly be used to form decision regions (to sustain or reject the null hypothesis). In most cases, however, the exact distribution of the likelihood ratio corresponding to specific hypotheses is very difficult to determine.

Assuming *H*0 is true, there is a fundamental result by Samuel S. Wilks: As the sample size n approaches $\infty$ , and if the null hypothesis lies strictly within the interior of the parameter space, the test statistic $\lambda _{\text{LR}}$ defined above will be asymptotically chi-squared distributed ( $\chi ^{2}$ ) with degrees of freedom equal to the difference in dimensionality of $\Theta$ and $\Theta _{0}$ . This implies that for a great variety of hypotheses, we can calculate the likelihood ratio $\lambda$ for the data and then compare the observed $\lambda _{\text{LR}}$ to the $\chi ^{2}$ value corresponding to a desired statistical significance as an *approximate* statistical test. Other extensions exist.

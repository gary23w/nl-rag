---
title: "Wald test"
source: https://en.wikipedia.org/wiki/Wald_test
domain: hypothesis-testing-deep
license: CC-BY-SA-4.0
tags: hypothesis test, null hypothesis, statistical power, likelihood ratio test
fetched: 2026-07-02
---

# Wald test

In statistics, the **Wald test** (named after Abraham Wald) assesses constraints on statistical parameters based on the weighted distance between the unrestricted estimate and its hypothesized value under the null hypothesis, where the weight is the precision of the estimate. Intuitively, the larger this weighted distance, the less likely it is that the constraint is true. While the finite sample distributions of Wald tests are generally unknown, it has an asymptotic χ2-distribution under the null hypothesis, a fact that can be used to determine statistical significance.

Together with the Lagrange multiplier test and the likelihood-ratio test, the Wald test is one of three classical approaches to hypothesis testing. An advantage of the Wald test over the other two is that it only requires the estimation of the unrestricted model, which lowers the computational burden as compared to the likelihood-ratio test. However, a major disadvantage is that (in finite samples) it is not invariant to changes in the representation of the null hypothesis; in other words, algebraically equivalent expressions of non-linear parameter restriction can lead to different values of the test statistic. That is because the Wald statistic is derived from a Taylor expansion, and different ways of writing equivalent nonlinear expressions lead to nontrivial differences in the corresponding Taylor coefficients. Another aberration, known as the Hauck–Donner effect, can occur in binomial models when the estimated (unconstrained) parameter is close to the boundary of the parameter space—for instance a fitted probability being extremely close to zero or one—which results in the Wald test no longer monotonically increasing in the distance between the unconstrained and constrained parameter.

## Mathematical details

Under the Wald test, the estimated ${\hat {\theta }}$ that was found as the maximizing argument of the unconstrained likelihood function is compared with a hypothesized value $\theta _{0}$ . In particular, the squared difference ${\hat {\theta }}-\theta _{0}$ is weighted by the curvature of the log-likelihood function.

### Test on a single parameter

If the hypothesis involves only a single parameter restriction, then the Wald statistic takes the following form:

$W={\frac {{({\widehat {\theta }}-\theta _{0})}^{2}}{\operatorname {var} ({\hat {\theta }})}}$

which under the null hypothesis follows an asymptotic χ2-distribution with one degree of freedom. The square root of the single-restriction Wald statistic can be understood as a (pseudo) *t*-ratio that is, however, not actually *t*-distributed except for the special case of linear regression with normally distributed errors. In general, it follows an asymptotic *z* distribution.

${\sqrt {W}}={\frac {{\widehat {\theta }}-\theta _{0}}{\operatorname {se} ({\hat {\theta }})}}$

where $\operatorname {se} ({\widehat {\theta }})$ is the standard error (SE) of the maximum likelihood estimate (MLE), the square root of the variance. There are several ways to consistently estimate the variance matrix which in finite samples leads to alternative estimates of standard errors and associated test statistics and *p*-values. The validity of still getting an asymptotically normal distribution after plugging in the MLE estimator of ${\hat {\theta }}$ into the SE relies on Slutsky's theorem.

### Test(s) on multiple parameters

The Wald test can be used to test a single hypothesis on multiple parameters, as well as to test jointly multiple hypotheses on single/multiple parameters. Let ${\hat {\theta }}_{n}$ be our sample estimator of *P* parameters (i.e., ${\hat {\theta }}_{n}$ is a $P\times 1$ vector), which is supposed to follow asymptotically a normal distribution with covariance matrix *V*, ${\sqrt {n}}({\hat {\theta }}_{n}-\theta )\,\xrightarrow {\mathcal {D}} \,N(0,V)$ . The test of *Q* hypotheses on the *P* parameters is expressed with a $Q\times P$ matrix *R*:

$H_{0}:R\theta =r$

$H_{1}:R\theta \neq r$

The distribution of the test statistic under the null hypothesis is

$(R{\hat {\theta }}_{n}-r)'[R({\hat {V}}_{n}/n)R']^{-1}(R{\hat {\theta }}_{n}-r)/Q\quad \xrightarrow {\mathcal {D}} \quad F(Q,n-P)\quad {\xrightarrow[{n\rightarrow \infty }]{\mathcal {D}}}\quad \chi _{Q}^{2}/Q,$

which in turn implies

$(R{\hat {\theta }}_{n}-r)'[R({\hat {V}}_{n}/n)R']^{-1}(R{\hat {\theta }}_{n}-r)\quad {\xrightarrow[{n\rightarrow \infty }]{\mathcal {D}}}\quad \chi _{Q}^{2},$

where ${\hat {V}}_{n}$ is an estimator of the covariance matrix.

Proof

Suppose ${\sqrt {n}}({\hat {\theta }}_{n}-\theta )\,\xrightarrow {\mathcal {D}} \,N(0,V)$ . Then, by Slutsky's theorem and by the properties of the normal distribution, multiplying by R has distribution:

$R{\sqrt {n}}({\hat {\theta }}_{n}-\theta )={\sqrt {n}}(R{\hat {\theta }}_{n}-r)\,\xrightarrow {\mathcal {D}} \,N(0,RVR')$

Recalling that a quadratic form of normal distribution has a Chi-squared distribution:

${\sqrt {n}}(R{\hat {\theta }}_{n}-r)'[RVR']^{-1}{\sqrt {n}}(R{\hat {\theta }}_{n}-r)\,\xrightarrow {\mathcal {D}} \,\chi _{Q}^{2}$

Rearranging *n* finally gives:

$(R{\hat {\theta }}_{n}-r)'[R(V/n)R']^{-1}(R{\hat {\theta }}_{n}-r)\quad \xrightarrow {\mathcal {D}} \quad \chi _{Q}^{2}$

What if the covariance matrix is not known a-priori and needs to be estimated from the data? If we have a consistent estimator ${\hat {V}}_{n}$ of V such that $V^{-1}{\hat {V}}_{n}$ has a determinant that is distributed $\chi _{n-P}^{2}$ , then by the independence of the covariance estimator and equation above, we have:

$(R{\hat {\theta }}_{n}-r)'[R({\hat {V}}_{n}/n)R']^{-1}(R{\hat {\theta }}_{n}-r)/Q\quad \xrightarrow {\mathcal {D}} \quad F(Q,n-P)$

### Nonlinear hypothesis

In the standard form, the Wald test is used to test linear hypotheses that can be represented by a single matrix *R*. If one wishes to test a non-linear hypothesis of the form:

$H_{0}:c(\theta )=0$

$H_{1}:c(\theta )\neq 0$

The test statistic becomes:

$c\left({\hat {\theta }}_{n}\right)'\left[c'\left({\hat {\theta }}_{n}\right)\left({\hat {V}}_{n}/n\right)c'\left({\hat {\theta }}_{n}\right)'\right]^{-1}c\left({\hat {\theta }}_{n}\right)\quad {\xrightarrow {\mathcal {D}}}\quad \chi _{Q}^{2}$

where $c'({\hat {\theta }}_{n})$ is the derivative of c evaluated at the sample estimator. This result is obtained using the delta method, which uses a first order approximation of the variance.

#### Non-invariance to re-parameterisations

The fact that one uses an approximation of the variance has the drawback that the Wald statistic is not-invariant to a non-linear transformation/reparametrisation of the hypothesis: it can give different answers to the same question, depending on how the question is phrased. For example, asking whether *R* = 1 is the same as asking whether log *R* = 0; but the Wald statistic for *R* = 1 is not the same as the Wald statistic for log *R* = 0 (because there is in general no neat relationship between the standard errors of *R* and log *R*, so it needs to be approximated).

## Alternatives to the Wald test

There exist several alternatives to the Wald test, namely the likelihood-ratio test and the Lagrange multiplier test (also known as the score test). Robert F. Engle showed that these three tests, the Wald test, the likelihood-ratio test and the Lagrange multiplier test are asymptotically equivalent. Although they are asymptotically equivalent, in finite samples, they could disagree enough to lead to different conclusions.

There are several reasons to prefer the likelihood ratio test or the Lagrange multiplier to the Wald test:

- Non-invariance: As argued above, the Wald test is not invariant under reparametrization, while the likelihood ratio tests will give exactly the same answer whether we work with *R*, log *R* or any other monotonic transformation of *R*.
- The other reason is that the Wald test uses two approximations (that we know the standard error or Fisher information and the maximum likelihood estimate), whereas the likelihood ratio test depends only on the ratio of likelihood functions under the null hypothesis and alternative hypothesis.
- The Wald test requires an estimate using the maximizing argument, corresponding to the "full" model. In some cases, the model is simpler under the null hypothesis, so that one might prefer to use the score test (also called Lagrange multiplier test), which has the advantage that it can be formulated in situations where the variability of the maximizing element is difficult to estimate or computing the estimate according to the maximum likelihood estimator is difficult; e.g. the Cochran–Mantel–Haenzel test is a score test.

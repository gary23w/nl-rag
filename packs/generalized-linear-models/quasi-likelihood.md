---
title: "Quasi-likelihood"
source: https://en.wikipedia.org/wiki/Quasi-likelihood
domain: generalized-linear-models
license: CC-BY-SA-4.0
tags: generalized linear model, link function, exponential family, quasi-likelihood
fetched: 2026-07-02
---

# Quasi-likelihood

In statistics, **quasi-likelihood** methods are used to estimate parameters in a statistical model when exact likelihood methods, for example maximum likelihood estimation, are computationally infeasible. Due to the wrong likelihood being used, quasi-likelihood estimators lose asymptotic efficiency compared to, e.g., maximum likelihood estimators. Under broadly applicable conditions, quasi-likelihood estimators are consistent and asymptotically normal. The asymptotic covariance matrix can be obtained using the so-called *sandwich estimator*. Examples of quasi-likelihood methods include the generalized estimating equations and pairwise likelihood approaches.

## History

The term **quasi-likelihood function** was introduced by Robert Wedderburn in 1974 to describe a function that has similar properties to the log-likelihood function but is not the log-likelihood corresponding to any actual probability distribution. He proposed to fit certain quasi-likelihood models using a straightforward extension of the algorithms used to fit generalized linear models.

## Application to overdispersion modelling

Quasi-likelihood estimation is one way of allowing for overdispersion, that is, greater variability in the data than would be expected from the statistical model used. It is most often used with models for count data or grouped binary data, i.e. data that would otherwise be modelled using the Poisson or binomial distribution.

Instead of specifying a probability distribution for the data, only a relationship between the mean and the variance is specified in the form of a variance function giving the variance as a function of the mean. Generally, this function is allowed to include a multiplicative factor known as the **overdispersion parameter** or **scale parameter** that is estimated from the data. Most commonly, the variance function is of a form such that fixing the overdispersion parameter at unity results in the variance-mean relationship of an actual probability distribution such as the binomial or Poisson. (For formulae, see the binomial data example and count data example under generalized linear models.)

### Comparison to alternatives

Random-effects models, and more generally mixed models (hierarchical models) provide an alternative method of fitting data exhibiting overdispersion using fully specified probability models. However, these methods often become complex and computationally intensive to fit to binary or count data. Quasi-likelihood methods have the advantage of relative computational simplicity, speed and robustness, as they can make use of the more straightforward algorithms developed to fit generalized linear models.

---
title: "Nuisance parameter"
source: https://en.wikipedia.org/wiki/Nuisance_parameter
domain: generalized-linear-models
license: CC-BY-SA-4.0
tags: generalized linear model, link function, exponential family, quasi-likelihood
fetched: 2026-07-02
---

# Nuisance parameter

In statistics, a **nuisance parameter** is any parameter which is unspecified but which must be accounted for in the hypothesis testing of the parameters which are of interest.

The classic example of a nuisance parameter comes from the normal distribution, a member of the location–scale family. In the case of normal distribution, the variance(s), *σ2* is often not specified or known, but one desires to hypothesis test on the mean(s). Another example might be linear regression with unknown variance in the explanatory variable (the independent variable): its variance is a nuisance parameter that must be accounted for to derive an accurate interval estimate of the regression slope, calculate p-values, hypothesis test on the slope's value; see regression dilution.

Nuisance parameters are often scale parameters, but not always; for example in errors-in-variables models, the unknown true location of each observation is a nuisance parameter. A parameter may also cease to be a "nuisance" if it becomes the object of study, is estimated from data, or known.

## Theoretical statistics

The general treatment of nuisance parameters can be broadly similar between frequentist and Bayesian approaches to theoretical statistics. It relies on an attempt to partition the likelihood function into components representing information about the parameters of interest and information about the other (nuisance) parameters. This can involve ideas about sufficient statistics and ancillary statistics. When this partition can be achieved it may be possible to complete a Bayesian analysis for the parameters of interest by determining their joint posterior distribution algebraically. The partition allows frequentist theory to develop general estimation approaches in the presence of nuisance parameters. If the partition cannot be achieved it may still be possible to make use of an approximate partition.

In some special cases, it is possible to formulate methods that circumvent the presences of nuisance parameters. The t-test provides a practically useful test because the test statistic does not depend on the unknown variance but only the sample variance. It is a case where use can be made of a pivotal quantity. However, in other cases no such circumvention is known.

## Practical statistics

Practical approaches to statistical analysis treat nuisance parameters somewhat differently in frequentist and Bayesian methodologies.

A general approach in a frequentist analysis can be based on maximum likelihood-ratio tests. These provide both significance tests and confidence intervals for the parameters of interest which are approximately valid for moderate to large sample sizes and which take account of the presence of nuisance parameters. See Basu (1977) for some general discussion and Spall and Garner (1990) for some discussion relative to the identification of parameters in linear dynamic (i.e., state space representation) models.

In Bayesian analysis, a generally applicable approach creates random samples from the joint posterior distribution of all the parameters: see Markov chain Monte Carlo. Given these, the joint distribution of only the parameters of interest can be readily found by marginalizing over the nuisance parameters. However, this approach may not always be computationally efficient if some or all of the nuisance parameters can be eliminated on a theoretical basis.

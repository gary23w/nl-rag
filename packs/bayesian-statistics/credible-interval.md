---
title: "Credible interval"
source: https://en.wikipedia.org/wiki/Credible_interval
domain: bayesian-statistics
license: CC-BY-SA-4.0
tags: bayesian statistics, conjugate prior, posterior probability, credible interval
fetched: 2026-07-02
---

# Credible interval

In Bayesian statistics, a **credible interval** is an interval used to characterize a probability distribution. It is defined such that an unobserved parameter value has a particular probability $\gamma$ to fall within it. For example, in an experiment that determines the distribution of possible values of the parameter $\mu$ , if the probability that $\mu$ lies between 35 and 45 is $\gamma =0.95$ , then $35\leq \mu \leq 45$ is a 95% credible interval.

Credible intervals are typically used to characterize posterior probability distributions or predictive probability distributions. Their generalization to disconnected or multivariate sets is called **credible set** or credible region.

Credible intervals are a Bayesian analog to confidence intervals in frequentist statistics. The two concepts arise from different philosophies: Bayesian intervals treat their bounds as fixed and the estimated parameter as a random variable, whereas frequentist confidence intervals treat their bounds as random variables and the parameter as a fixed value. Also, Bayesian credible intervals use (and indeed, require) knowledge of the situation-specific prior distribution, while the frequentist confidence intervals do not.

## Definitions

Credible sets are not unique, as any given probability distribution has an infinite number of $\gamma$ -credible sets, i.e. sets of probability $\gamma$ . For example, in the univariate case, there are multiple definitions for a suitable interval or set:

- The **smallest credible interval** (SCI), sometimes also called the **highest density interval**. This interval necessarily contains the median whenever $\gamma \geq 0.5$ . When the distribution is unimodal, this interval also contains the mode.
- The **smallest credible set** (SCS), sometimes also called the **highest density region**. For a multimodal distribution, this is not necessarily an interval as it can be disconnected. This set always contains the mode.
- A **quantile-based credible interval**, which is computed by taking the inter-quantile interval $[q_{\delta },q_{\delta +\gamma }]$ for some predefined $\delta \in [0,1-\gamma ]$ . For instance, the **median credible interval** (MCI) of probability $\gamma$ is the interval where the probability of being below the interval is as likely as being above it, that is to say the interval $[q_{(1-\gamma )/2},q_{(1+\gamma )/2}]$ . It is sometimes also called the **equal-tailed interval**, and it always contains the median. Other quantile-based credible intervals can be defined, such as the **lowest credible interval** (LCI) which is $[q_{0},q_{\gamma }]$ , or the **highest credible interval** (HCI) which is $[q_{1-\gamma },q_{1}]$ . These intervals may be more suited for bounded variables.

One may also define an interval for which the mean is the central point, assuming that the mean exists.

$\gamma$ -Smallest Credible Sets ( $\gamma$ -SCS) can easily be generalized to the multivariate case, and are bounded by probability density contour lines. They always contain the mode, but not necessarily the mean, the coordinate-wise median, nor the geometric median.

Credible intervals can also be estimated through the use of simulation techniques such as Markov chain Monte Carlo.

## Contrasts with confidence interval

A frequentist 95% confidence interval means that with a large number of repeated samples, 95% of such calculated confidence intervals would include the true value of the parameter. In frequentist terms, the parameter is *fixed* (cannot be considered to have a distribution of possible values) and the confidence interval is *random* (as it depends on the random sample).

Bayesian credible intervals differ from frequentist confidence intervals by two major aspects:

- Credible intervals are intervals whose values have a (posterior) probability density, representing the plausibility that the parameter has those values, whereas confidence intervals regard the population parameter as fixed and therefore not the object of probability. Within confidence intervals, confidence refers to the randomness of the very confidence interval under repeated trials, whereas credible intervals analyze the uncertainty of the target parameter given the data at hand.

- Credible intervals and confidence intervals treat nuisance parameters in radically different ways.

For the case of a single parameter and data that can be summarised in a single sufficient statistic, it can be shown that the credible interval and the confidence interval coincide if the unknown parameter is a location parameter (i.e. the forward probability function has the form $\mathrm {Pr} (x|\mu )=f(x-\mu )$ ), with a prior that is a uniform flat distribution; and also if the unknown parameter is a scale parameter (i.e. the forward probability function has the form $\mathrm {Pr} (x|s)=f(x/s)$ ), with a Jeffreys' prior $\mathrm {Pr} (s|I)\;\propto \;1/s$ — the latter following because taking the logarithm of such a scale parameter turns it into a location parameter with a uniform distribution. But these are distinctly special (albeit important) cases; in general no such equivalence can be made.

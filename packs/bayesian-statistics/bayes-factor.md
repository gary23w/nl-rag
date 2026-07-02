---
title: "Bayes factor"
source: https://en.wikipedia.org/wiki/Bayes_factor
domain: bayesian-statistics
license: CC-BY-SA-4.0
tags: bayesian statistics, conjugate prior, posterior probability, credible interval
fetched: 2026-07-02
---

# Bayes factor

The **Bayes factor** is a ratio of two competing statistical models represented by their evidence, and is used to quantify the support for one model over the other. The models in question can have a common set of parameters, such as a null hypothesis and an alternative, but this is not necessary; for instance, it could also be a non-linear model compared to its linear approximation. The Bayes factor can be thought of as a Bayesian analog to the likelihood-ratio test, although it uses the integrated (i.e., marginal) likelihood rather than the maximized likelihood. As such, both quantities only coincide under simple hypotheses (e.g., two specific parameter values). Also, in contrast with null hypothesis significance testing, Bayes factors support evaluation of evidence *in favor* of a null hypothesis, rather than only allowing the null to be rejected or not rejected.

Although conceptually simple, the computation of the Bayes factor can be challenging depending on the complexity of the model and the hypotheses. Since closed-form expressions of the marginal likelihood are generally not available, numerical approximations based on MCMC samples have been suggested. For certain special cases, simplified algebraic expressions can be derived; for instance, the Savage–Dickey density ratio in the case of a precise (equality constrained) hypothesis against an unrestricted alternative. Another approximation, derived by applying Laplace's approximation to the integrated likelihoods, is known as the Bayesian information criterion (BIC); in large data sets the Bayes factor will approach the BIC as the influence of the priors wanes. In small data sets, priors generally matter and must not be improper since the Bayes factor will be undefined if either of the two integrals in its ratio is not finite.

## Definition

The Bayes factor is the ratio of two marginal likelihoods; that is, the likelihoods of two statistical models integrated over the prior probabilities of their parameters.

The posterior probability $\Pr(M|D)$ of a model *M* given data *D* is given by Bayes' theorem:

$\Pr(M|D)={\frac {\Pr(D|M)\Pr(M)}{\Pr(D)}}.$

The key data-dependent term $\Pr(D|M)$ represents the probability that some data are produced under the assumption of the model *M*; evaluating it correctly is the key to Bayesian model comparison.

Given a model selection problem in which one wishes to choose between two models on the basis of observed data *D*, the plausibility of the two different models *M*1 and *M*2, parametrised by model parameter vectors $\theta _{1}$ and $\theta _{2}$ , is assessed by the Bayes factor *K* given by

$K={\frac {\Pr(D|M_{1})}{\Pr(D|M_{2})}}={\frac {\int \Pr(\theta _{1}|M_{1})\Pr(D|\theta _{1},M_{1})\,d\theta _{1}}{\int \Pr(\theta _{2}|M_{2})\Pr(D|\theta _{2},M_{2})\,d\theta _{2}}}={\frac {\frac {\Pr(M_{1}|D)\Pr(D)}{\Pr(M_{1})}}{\frac {\Pr(M_{2}|D)\Pr(D)}{\Pr(M_{2})}}}={\frac {\Pr(M_{1}|D)}{\Pr(M_{2}|D)}}{\frac {\Pr(M_{2})}{\Pr(M_{1})}}.$

When the two models have equal prior probability, so that $\Pr(M_{1})=\Pr(M_{2})$ , the Bayes factor is equal to the ratio of the posterior probabilities of *M*1 and *M*2. If instead of the Bayes factor integral, the likelihood corresponding to the maximum likelihood estimate of the parameter for each statistical model is used, then the test becomes a classical likelihood-ratio test. Unlike a likelihood-ratio test, this Bayesian model comparison does not depend on any single set of parameters, as it integrates over all parameters in each model (with respect to the respective priors). An advantage of the use of Bayes factors is that it automatically, and quite naturally, includes a penalty for including too much model structure. It thus guards against overfitting. For models where an explicit version of the likelihood is not available or too costly to evaluate numerically, approximate Bayesian computation can be used for model selection in a Bayesian framework, with the caveat that approximate-Bayesian estimates of Bayes factors are often biased.

Other approaches are:

- to treat model comparison as a decision problem, computing the expected value or cost of each model choice;
- to use minimum message length (MML).
- to use minimum description length (MDL).

## Interpretation

A value of *K* > 1 means that *M*1 is more strongly supported by the data under consideration than *M*2. Note that classical hypothesis testing gives one hypothesis (or model) preferred status (the 'null hypothesis'), and only considers evidence *against* it. The fact that a Bayes factor can produce evidence *for* and not just against a null hypothesis is one of the key advantages of this analysis method.

Harold Jeffreys gave a scale (**Jeffreys' scale**) for interpretation of K :

| *K* | dHart | bits | Strength of evidence |
|---|---|---|---|
| **< 100** | < 0 | < 0 | Negative (supports *M*2) |
| **100 to 101/2** | 0 to 5 | 0 to 1.6 | Barely worth mentioning |
| **101/2 to 101** | 5 to 10 | 1.6 to 3.3 | Substantial |
| **101 to 103/2** | 10 to 15 | 3.3 to 5.0 | Strong |
| **103/2 to 102** | 15 to 20 | 5.0 to 6.6 | Very strong |
| **> 102** | > 20 | > 6.6 | Decisive |

The second column gives the corresponding weights of evidence in decihartleys (also known as decibans); bits are added in the third column for clarity. The table continues in the other direction, so that, for example, $K\leq 10^{-2}$ is decisive evidence for $M_{2}$ .

An alternative table, widely cited, is provided by Kass and Raftery (1995):

| log10 *K* | *K* | Strength of evidence |
|---|---|---|
| **0 to 1/2** | 1 to 3.2 | Not worth more than a bare mention |
| **1/2 to 1** | 3.2 to 10 | Substantial |
| **1 to 2** | 10 to 100 | Strong |
| **> 2** | > 100 | Decisive |

According to I. J. Good, the just-noticeable difference of humans in their everyday life, when it comes to a change degree of belief in a hypothesis, is about a factor of 1.3x, or 1 deciban, or 1/3 of a bit, or from 1:1 to 5:4 in odds ratio.

## Example

Suppose we have a random variable that produces either a success or a failure. We want to compare a model $M_{1}$ where the probability of success is *q* = 1⁄2, and another model $M_{2}$ where *q* is unknown and we take a prior distribution for *q* that is uniform on [0,1]. We take a sample of 200, and find 115 successes and 85 failures. The likelihood can be calculated according to the binomial distribution:

${{200 \choose 115}q^{115}(1-q)^{85}}.$

Thus we have for $M_{1}$

$P(X=115\mid M_{1})={200 \choose 115}\left({1 \over 2}\right)^{200}\approx 0.006$

whereas for $M_{2}$ we have

$P(X=115\mid M_{2})=\int _{0}^{1}{200 \choose 115}q^{115}(1-q)^{85}dq={1 \over 201}\approx 0.005$

The ratio is then 1.2, which is "barely worth mentioning" even if it points very slightly towards $M_{1}$ .

A frequentist hypothesis test of $M_{1}$ (here considered as a null hypothesis) would have produced a very different result. Such a test says that $M_{1}$ should be rejected at the 5% significance level, since the probability of getting 115 or more successes from a sample of 200 if *q* = 1⁄2 is 0.02, and as a two-tailed test of getting a figure as extreme as or more extreme than 115 is 0.04. Note that 115 is more than two standard deviations away from 100. Thus, whereas a frequentist hypothesis test would yield significant results at the 5% significance level, the Bayes factor hardly considers this to be an extreme result. Note, however, that a non-uniform prior (for example one that reflects that you expect the number of success and failures to be of the same order of magnitude) could result in a Bayes factor that is more in agreement with the frequentist hypothesis test.

A classical likelihood-ratio test would have found the maximum likelihood estimate for *q*, namely ${\hat {q}}={\frac {115}{200}}=0.575$ , whence

$\textstyle P(X=115\mid M_{2})={{200 \choose 115}{\hat {q}}^{115}(1-{\hat {q}})^{85}}\approx 0.06$

(rather than averaging over all possible *q*). That gives a likelihood ratio of 0.1 and points towards *M*2.

$M_{2}$ is a more complex model than $M_{1}$ because it has a free parameter which allows it to model the data more closely. The ability of Bayes factors to take this into account is a reason why Bayesian inference has been put forward as a theoretical justification for and generalisation of Occam's razor, reducing Type I errors.

On the other hand, the modern method of relative likelihood takes into account the number of free parameters in the models, unlike the classical likelihood ratio. The relative likelihood method could be applied as follows. Model *M*1 has 0 parameters, and so its Akaike information criterion (AIC) value is $2\cdot 0-2\cdot \ln(0.005956)\approx 10.2467$ . Model *M*2 has 1 parameter, and so its AIC value is $2\cdot 1-2\cdot \ln(0.056991)\approx 7.7297$ . Hence *M*1 is about $\exp \left({\frac {7.7297-10.2467}{2}}\right)\approx 0.284$ times as probable as *M*2 to minimize the information loss. Thus *M*2 is slightly preferred, but *M*1 cannot be excluded.

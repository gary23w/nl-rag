---
title: "Empirical Bayes method"
source: https://en.wikipedia.org/wiki/Empirical_Bayes_method
domain: empirical-bayes
license: CC-BY-SA-4.0
tags: empirical Bayes method, prior probability, posterior probability, Bayes estimator
fetched: 2026-07-02
---

# Empirical Bayes method

**Empirical Bayes methods** are procedures for statistical inference in which the prior probability distribution is estimated from the data. This approach stands in contrast to standard Bayesian methods, for which the prior distribution is fixed before any data are observed. Despite this difference in perspective, empirical Bayes may be viewed as an approximation to a fully Bayesian treatment of a hierarchical model wherein the parameters at the highest level of the hierarchy are set to their most likely values, instead of being integrated out.

## Introduction

Empirical Bayes methods can be seen as an approximation to a fully Bayesian treatment of a hierarchical Bayes model.

In, for example, a two-stage hierarchical Bayes model, observed data $y=\{y_{1},y_{2},\dots ,y_{n}\}$ are assumed to be generated from an unobserved set of parameters $\theta =\{\theta _{1},\theta _{2},\dots ,\theta _{n}\}$ according to a probability distribution $p(y\mid \theta )\,$ . In turn, the parameters $\theta$ can be considered samples drawn from a population characterised by hyperparameters $\eta \,$ according to a probability distribution $p(\theta \mid \eta )\,$ . In the hierarchical Bayes model, though not in the empirical Bayes approximation, the hyperparameters $\eta \,$ are considered to be drawn from an unparameterized distribution $p(\eta )\,$ .

Information about a particular quantity of interest $\theta _{i}\;$ therefore comes not only from the properties of those data y that directly depend on it, but also from the properties of the population of parameters $\theta \;$ as a whole, inferred from the data as a whole, summarised by the hyperparameters $\eta \;$ .

Using Bayes' theorem,

$p(\theta \mid y)={\frac {p(y\mid \theta )p(\theta )}{p(y)}}={\frac {p(y\mid \theta )}{p(y)}}\int p(\theta \mid \eta )p(\eta )\,d\eta \,.$

In general, this integral will not be tractable analytically or symbolically and must be evaluated by numerical methods. Stochastic (random) or deterministic approximations may be used. Example stochastic methods are Markov Chain Monte Carlo and Monte Carlo sampling. Deterministic approximations are discussed in quadrature.

Alternatively, the expression can be written as

$p(\theta \mid y)=\int p(\theta \mid \eta ,y)p(\eta \mid y)\;d\eta =\int {\frac {p(y\mid \theta )p(\theta \mid \eta )}{p(y\mid \eta )}}p(\eta \mid y)\;d\eta \,,$

and the final factor in the integral can in turn be expressed as

$p(\eta \mid y)=\int p(\eta \mid \theta )p(\theta \mid y)\;d\theta .$

These suggest an iterative scheme, qualitatively similar in structure to a Gibbs sampler, to evolve successively improved approximations to $p(\theta \mid y)\;$ and $p(\eta \mid y)\;$ . First, calculate an initial approximation to $p(\theta \mid y)\;$ ignoring the $\eta$ dependence completely; then calculate an approximation to $p(\eta \mid y)\;$ based upon the initial approximate distribution of $p(\theta \mid y)\;$ ; then use this $p(\eta \mid y)\;$ to update the approximation for $p(\theta \mid y)\;$ ; then update $p(\eta \mid y)\;$ ; and so on.

When the true distribution $p(\eta \mid y)\;$ is sharply peaked, the integral determining $p(\theta \mid y)\;$ may be not much changed by replacing the probability distribution over $\eta \;$ with a point estimate $\eta ^{*}\;$ representing the distribution's peak (or, alternatively, its mean),

$p(\theta \mid y)\simeq {\frac {p(y\mid \theta )\;p(\theta \mid \eta ^{*})}{p(y\mid \eta ^{*})}}\,.$

With this approximation, the above iterative scheme becomes the EM algorithm.

The term "Empirical Bayes" can cover a wide variety of methods, but most can be regarded as an early truncation of either the above scheme or something quite like it. Point estimates, rather than the whole distribution, are typically used for the parameter(s) $\eta \;$ . The estimates for $\eta ^{*}\;$ are typically made from the first approximation to $p(\theta \mid y)\;$ without subsequent refinement. These estimates for $\eta ^{*}\;$ are usually made without considering an appropriate prior distribution for $\eta$ .

## Point estimation

### Robbins' method: non-parametric empirical Bayes (NPEB)

Robbins considered a case of sampling from a mixed distribution, where probability for each $y_{i}$ (conditional on $\theta _{i}$ ) is specified by a Poisson distribution,

$p(y_{i}\mid \theta _{i})={{\theta _{i}}^{y_{i}}e^{-\theta _{i}} \over {y_{i}}!}$

while the prior on *θ* is unspecified except that it is also i.i.d. from an unknown distribution, with cumulative distribution function $G(\theta )$ . Compound sampling arises in a variety of statistical estimation problems, such as accident rates and clinical trials. We simply seek a point prediction of $\theta _{i}$ given all the observed data. Because the prior is unspecified, we seek to do this without knowledge of *G*.

Under squared error loss (SEL), the conditional expectation E(*θ**i* | *Y**i* = *y**i*) is a reasonable quantity to use for prediction. For the Poisson compound sampling model, this quantity is

$\operatorname {E} (\theta _{i}\mid y_{i})={\int (\theta ^{y_{i}+1}e^{-\theta }/{y_{i}}!)\,dG(\theta ) \over {\int (\theta ^{y_{i}}e^{-\theta }/{y_{i}}!)\,dG(\theta })}.$

This can be simplified by multiplying both the numerator and denominator by $({y_{i}}+1)$ , yielding

$\operatorname {E} (\theta _{i}\mid y_{i})={{(y_{i}+1)p_{G}(y_{i}+1)} \over {p_{G}(y_{i})}},$

where *pG* is the marginal probability mass function obtained by integrating out *θ* over *G*.

To take advantage of this, Robbins suggested estimating the marginals with their empirical frequencies ( $\#\{Y_{j}\}$ ), yielding the fully non-parametric estimate as:

$\operatorname {E} (\theta _{i}\mid y_{i})\approx (y_{i}+1){{\#\{Y_{j}=y_{i}+1\}} \over {\#\{Y_{j}=y_{i}\}}},$

where $\#$ denotes "number of". (See also Good–Turing frequency estimation.)

**Example – Accident rates**

Suppose each customer of an insurance company has an "accident rate" Θ and is insured against accidents; the probability distribution of Θ is the underlying distribution, and is unknown. The number of accidents suffered by each customer in a specified time period has a Poisson distribution with expected value equal to the particular customer's accident rate. The actual number of accidents experienced by a customer is the observable quantity. A crude way to estimate the underlying probability distribution of the accident rate Θ is to estimate the proportion of members of the whole population suffering 0, 1, 2, 3, ... accidents during the specified time period as the corresponding proportion in the observed random sample. Having done so, it is then desired to predict the accident rate of each customer in the sample. As above, one may use the conditional expected value of the accident rate Θ given the observed number of accidents during the baseline period. Thus, if a customer suffers six accidents during the baseline period, that customer's estimated accident rate is 7 × [the proportion of the sample who suffered 7 accidents] / [the proportion of the sample who suffered 6 accidents]. Note that if the proportion of people suffering *k* accidents is a decreasing function of *k*, the customer's predicted accident rate will often be lower than their observed number of accidents.

This shrinkage effect is typical of empirical Bayes analyses.

### Gaussian

Suppose $X,Y$ are random variables, such that Y is observed, but X is hidden. The problem is to find the expectation of X , conditional on Y . Suppose further that $Y|X\sim {\mathcal {N}}(X,\Sigma )$ , that is, $Y=X+Z$ , where Z is a multivariate gaussian with variance $\Sigma$ .

Then, we have the formula $\Sigma \nabla _{y}\rho (y|x)=\rho (y|x)(x-y)$ by direct calculation with the probability density function of multivariate gaussians. Integrating over $\rho (x)dx$ , we obtain $\Sigma \nabla _{y}\rho (y)=(\mathbb {E} [x|y]-y)\rho (y)\implies \mathbb {E} [x|y]=y+\Sigma \nabla _{y}\ln \rho (y)$ In particular, this means that one can perform Bayesian estimation of X without access to either the prior density of X or the posterior density of Y . The only requirement is to have access to the score function of Y . This has applications in score-based generative modeling.

### Parametric empirical Bayes

If the likelihood and its prior take on simple parametric forms (such as 1- or 2-dimensional likelihood functions with simple conjugate priors), then the empirical Bayes problem is only to estimate the marginal $m(y\mid \eta )$ and the hyperparameters $\eta$ using the complete set of empirical measurements. For example, one common approach, called parametric empirical Bayes point estimation, is to approximate the marginal using the maximum likelihood estimate (MLE), or a moments expansion, which allows one to express the hyperparameters $\eta$ in terms of the empirical mean and variance. This simplified marginal allows one to plug in the empirical averages into a point estimate for the prior $\theta$ . The resulting equation for the prior $\theta$ is greatly simplified, as shown below.

There are several common parametric empirical Bayes models, including the Poisson–gamma model (below), the Beta-binomial model, the Gaussian–Gaussian model, the Dirichlet-multinomial model, as well specific models for Bayesian linear regression (see below) and Bayesian multivariate linear regression. More advanced approaches include hierarchical Bayes models and Bayesian mixture models.

#### Gaussian–Gaussian model

For an example of empirical Bayes estimation using a Gaussian-Gaussian model, see Empirical Bayes estimators.

#### Poisson–gamma model

For example, in the example above, let the likelihood be a Poisson distribution, and let the prior now be specified by the conjugate prior, which is a gamma distribution ( $G(\alpha ,\beta )$ ) (where $\eta =(\alpha ,\beta )$ ):

$\rho (\theta \mid \alpha ,\beta )\,d\theta ={\frac {(\theta /\beta )^{\alpha -1}\,e^{-\theta /\beta }}{\Gamma (\alpha )}}\,(d\theta /\beta ){\text{ for }}\theta >0,\alpha >0,\beta >0\,\!.$

It is straightforward to show the posterior is also a gamma distribution. Write

$\rho (\theta \mid y)\propto \rho (y\mid \theta )\rho (\theta \mid \alpha ,\beta ),$

where the marginal distribution has been omitted since it does not depend explicitly on $\theta$ . Expanding terms which do depend on $\theta$ gives the posterior as:

$\rho (\theta \mid y)\propto (\theta ^{y}\,e^{-\theta })(\theta ^{\alpha -1}\,e^{-\theta /\beta })=\theta ^{y+\alpha -1}\,e^{-\theta (1+1/\beta )}.$

So the posterior density is also a gamma distribution $G(\alpha ',\beta ')$ , where $\alpha '=y+\alpha$ , and $\beta '=(1+1/\beta )^{-1}$ . Also notice that the marginal is simply the integral of the posterior over all $\Theta$ , which turns out to be a negative binomial distribution.

To apply empirical Bayes, we will approximate the marginal using the maximum likelihood estimate (MLE). But since the posterior is a gamma distribution, the MLE of the marginal turns out to be just the mean of the posterior, which is the point estimate $\operatorname {E} (\theta \mid y)$ we need. Recalling that the mean $\mu$ of a gamma distribution $G(\alpha ',\beta ')$ is simply $\alpha '\beta '$ , we have

$\operatorname {E} (\theta \mid y)=\alpha '\beta '={\frac {{\bar {y}}+\alpha }{1+1/\beta }}={\frac {\beta }{1+\beta }}{\bar {y}}+{\frac {1}{1+\beta }}(\alpha \beta ).$

To obtain the values of $\alpha$ and $\beta$ , empirical Bayes prescribes estimating mean $\alpha \beta$ and variance $\alpha \beta ^{2}$ using the complete set of empirical data.

The resulting point estimate $\operatorname {E} (\theta \mid y)$ is therefore like a weighted average of the sample mean ${\bar {y}}$ and the prior mean $\mu =\alpha \beta$ . This turns out to be a general feature of empirical Bayes; the point estimates for the prior (i.e. mean) will look like a weighted averages of the sample estimate and the prior estimate (likewise for estimates of the variance).

---
title: "Mixture distribution"
source: https://en.wikipedia.org/wiki/Mixture_distribution
domain: mixture-models-em
license: CC-BY-SA-4.0
tags: mixture model, expectation maximization, Gaussian mixture model, latent class model
fetched: 2026-07-02
---

# Mixture distribution

In probability and statistics, a **mixture distribution** is the probability distribution of a random variable that is derived from a collection of other random variables as follows: first, a random variable is selected by chance from the collection according to given probabilities of selection, and then the value of the selected random variable is realized. The underlying random variables may be random real numbers, or they may be random vectors (each having the same dimension), in which case the mixture distribution is a multivariate distribution.

In cases where each of the underlying random variables is continuous, the outcome variable will also be continuous and its probability density function is sometimes referred to as a **mixture density**. The cumulative distribution function (and the probability density function if it exists) can be expressed as a convex combination (i.e. a weighted sum, with non-negative weights that sum to 1) of other distribution functions and density functions. The individual distributions that are combined to form the mixture distribution are called the **mixture components**, and the probabilities (or weights) associated with each component are called the **mixture weights**. The number of components in a mixture distribution is often restricted to being finite, although in some cases the components may be countably infinite in number. More general cases (i.e. an uncountable set of component distributions), as well as the countable case, are treated under the title of **compound distributions**.

A distinction needs to be made between a random variable whose distribution function or density is the sum of a set of components (i.e. a mixture distribution) and a random variable whose value is the sum of the values of two or more underlying random variables, in which case the distribution is given by the convolution operator. As an example, the sum of two jointly normally distributed random variables, each with different means, will still have a normal distribution. On the other hand, a mixture density created as a mixture of two normal distributions with different means will have two peaks provided that the two means are far enough apart, showing that this distribution is radically different from a normal distribution.

Mixture distributions arise in many contexts in the literature and arise naturally where a statistical population contains two or more subpopulations. They are also sometimes used as a means of representing non-normal distributions. Data analysis concerning statistical models involving mixture distributions is discussed under the title of mixture models, while the present article concentrates on simple probabilistic and statistical properties of mixture distributions and how these relate to properties of the underlying distributions.

## Finite and countable mixtures

Given a finite set of probability density functions *p*1(*x*), ..., *pn*(*x*), or corresponding cumulative distribution functions *P*1(*x*), ..., *Pn*(*x*) and **weights** *w*1, ..., *wn* such that *wi* ≥ 0 and ∑*wi* = 1, the mixture distribution can be represented by writing either the density, *f*, or the distribution function, *F*, as a sum (which in both cases is a convex combination): $F(x)=\sum _{i=1}^{n}\,w_{i}\,P_{i}(x),$ $f(x)=\sum _{i=1}^{n}\,w_{i}\,p_{i}(x).$ This type of mixture, being a finite sum, is called a **finite mixture,** and in applications, an unqualified reference to a "mixture density" usually means a finite mixture. The case of a countably infinite set of components is covered formally by allowing $n=\infty \!$ .

## Uncountable mixtures

Where the set of component distributions is uncountable, the result is often called a compound probability distribution. The construction of such distributions has a formal similarity to that of mixture distributions, with either infinite summations or integrals replacing the finite summations used for finite mixtures.

Consider a probability density function *p*(*x*;*a*) for a variable x, parameterized by a. That is, for each value of a in some set A, *p*(*x*;*a*) is a probability density function with respect to x. Given a probability density function w (meaning that w is nonnegative and integrates to 1), the function

$f(x)=\int _{A}\,w(a)\,p(x;a)\,da$

is again a probability density function for x. A similar integral can be written for the cumulative distribution function. Note that the formulae here reduce to the case of a finite or infinite mixture if the density w is allowed to be a generalized function representing the "derivative" of the cumulative distribution function of a discrete distribution.

## Mixtures within a parametric family

The mixture components are often not arbitrary probability distributions, but instead are members of a parametric family (such as normal distributions), with different values for a parameter or parameters. In such cases, assuming that it exists, the density can be written in the form of a sum as: $f(x;a_{1},\ldots ,a_{n})=\sum _{i=1}^{n}\,w_{i}\,p(x;a_{i})$ for one parameter, or $f(x;a_{1},\ldots ,a_{n},b_{1},\ldots ,b_{n})=\sum _{i=1}^{n}\,w_{i}\,p(x;a_{i},b_{i})$ for two parameters, and so forth.

## Properties

### Convexity

A general linear combination of probability density functions is not necessarily a probability density, since it may be negative or it may integrate to something other than 1. However, a convex combination of probability density functions preserves both of these properties (non-negativity and integrating to 1), and thus mixture densities are themselves probability density functions.

### Moments

Let *X*1, ..., *X**n* denote random variables from the n component distributions, and let X denote a random variable from the mixture distribution. Then, for any function *H*(·) for which $\operatorname {E} [H(X_{i})]$ exists, and assuming that the component densities *pi*(*x*) exist,

${\begin{aligned}\operatorname {E} [H(X)]&=\int _{-\infty }^{\infty }H(x)\sum _{i=1}^{n}w_{i}p_{i}(x)\,dx\\&=\sum _{i=1}^{n}w_{i}\int _{-\infty }^{\infty }p_{i}(x)H(x)\,dx=\sum _{i=1}^{n}w_{i}\operatorname {E} [H(X_{i})].\end{aligned}}$

The jth moment about zero (i.e. choosing *H*(*x*) = *x**j*) is simply a weighted average of the j-th moments of the components. Moments about the mean *H*(*x*) = (*x − μ*)*j* involve a binomial expansion:

${\begin{aligned}\operatorname {E} \left[{\left(X-\mu \right)}^{j}\right]&=\sum _{i=1}^{n}w_{i}\operatorname {E} \left[{\left(X_{i}-\mu _{i}+\mu _{i}-\mu \right)}^{j}\right]\\&=\sum _{i=1}^{n}w_{i}\sum _{k=0}^{j}{\binom {j}{k}}{\left(\mu _{i}-\mu \right)}^{j-k}\operatorname {E} \left[{\left(X_{i}-\mu _{i}\right)}^{k}\right],\end{aligned}}$

where *μi* denotes the mean of the i-th component.

In the case of a mixture of one-dimensional distributions with weights *wi*, means *μi* and variances *σ**i*2, the total mean and variance will be: $\operatorname {E} [X]=\mu =\sum _{i=1}^{n}w_{i}\mu _{i},$ ${\begin{aligned}\operatorname {E} \left[(X-\mu )^{2}\right]&=\sigma ^{2}\\&=\operatorname {E} [X^{2}]-\mu ^{2}&({\text{standard variance reformulation}})\\&=\left(\sum _{i=1}^{n}w_{i}\operatorname {E} \left[X_{i}^{2}\right]\right)-\mu ^{2}\\&=\sum _{i=1}^{n}w_{i}(\sigma _{i}^{2}+\mu _{i}^{2})-\mu ^{2}&(\sigma _{i}^{2}=\operatorname {E} [X_{i}^{2}]-\mu _{i}^{2}\implies \operatorname {E} [X_{i}^{2}]=\sigma _{i}^{2}+\mu _{i}^{2})\end{aligned}}$

These relations highlight the potential of mixture distributions to display non-trivial higher-order moments such as skewness and kurtosis (fat tails) and multi-modality, even in the absence of such features within the components themselves. Marron and Wand (1992) give an illustrative account of the flexibility of this framework.

### Modes

The question of multimodality is simple for some cases, such as mixtures of exponential distributions: all such mixtures are unimodal. However, for the case of mixtures of normal distributions, it is a complex one. Conditions for the number of modes in a multivariate normal mixture are explored by Ray & Lindsay extending earlier work on univariate and multivariate distributions.

Here the problem of evaluation of the modes of an n component mixture in a D dimensional space is reduced to identification of critical points (local minima, maxima and saddle points) on a manifold referred to as the ridgeline surface, which is the image of the ridgeline function $x^{*}(\alpha )=\left[\sum _{i=1}^{n}\alpha _{i}\Sigma _{i}^{-1}\right]^{-1}\times \left[\sum _{i=1}^{n}\alpha _{i}\Sigma _{i}^{-1}\mu _{i}\right],$ where $\alpha$ belongs to the $(n-1)$ -dimensional standard simplex: ${\mathcal {S}}_{n}=\left\{\alpha \in \mathbb {R} ^{n}:\alpha _{i}\in [0,1],\sum _{i=1}^{n}\alpha _{i}=1\right\}$ and $\Sigma _{i}\in \mathbb {R} ^{D\times D},\,\mu _{i}\in \mathbb {R} ^{D}$ correspond to the covariance and mean of the i-th component. Ray & Lindsay consider the case in which $n-1<D$ showing a one-to-one correspondence of modes of the mixture and those on the **ridge elevation function** $h(\alpha )=q(x^{*}(\alpha ))$ thus one may identify the modes by solving ${\frac {dh(\alpha )}{d\alpha }}=0$ with respect to $\alpha$ and determining the value $x^{*}(\alpha )$ .

Using graphical tools, the potential multi-modality of mixtures with number of components $n\in \{2,3\}$ is demonstrated; in particular it is shown that the number of modes may exceed n and that the modes may not be coincident with the component means. For two components they develop a graphical tool for analysis by instead solving the aforementioned differential with respect to the first mixing weight $w_{1}$ (which also determines the second mixing weight through $w_{2}=1-w_{1}$ ) and expressing the solutions as a function $\Pi (\alpha ),\,\alpha \in [0,1]$ so that the number and location of modes for a given value of $w_{1}$ corresponds to the number of intersections of the graph on the line $\Pi (\alpha )=w_{1}$ . This in turn can be related to the number of oscillations of the graph and therefore to solutions of ${\frac {d\Pi (\alpha )}{d\alpha }}=0$ leading to an explicit solution for the case of a two component mixture with $\Sigma _{1}=\Sigma _{2}=\Sigma$ (sometimes called a homoscedastic mixture) given by $1-\alpha (1-\alpha )d_{M}(\mu _{1},\mu _{2},\Sigma )^{2}$ where ${\textstyle d_{M}(\mu _{1},\mu _{2},\Sigma )={\sqrt {(\mu _{2}-\mu _{1})^{\mathsf {T}}\Sigma ^{-1}(\mu _{2}-\mu _{1})}}}$ is the Mahalanobis distance between $\mu _{1}$ and $\mu _{2}$ .

Since the above is quadratic it follows that in this instance there are at most two modes irrespective of the dimension or the weights.

For normal mixtures with general $n>2$ and $D>1$ , a lower bound for the maximum number of possible modes, and – conditionally on the assumption that the maximum number is finite – an upper bound are known. For those combinations of n and D for which the maximum number is known, it matches the lower bound.

## Examples

### Two normal distributions

Simple examples can be given by a mixture of two normal distributions. (See Multimodal distribution#Mixture of two normal distributions for more details.)

Given an equal (50/50) mixture of two normal distributions with the same standard deviation and different means (homoscedastic), the overall distribution will exhibit low kurtosis relative to a single normal distribution – the means of the subpopulations fall on the shoulders of the overall distribution. If sufficiently separated, namely by twice the (common) standard deviation, so $\left|\mu _{1}-\mu _{2}\right|>2\sigma ,$ these form a bimodal distribution, otherwise it simply has a wide peak. The variation of the overall population will also be greater than the variation of the two subpopulations (due to spread from different means), and thus exhibits overdispersion relative to a normal distribution with fixed variation σ, though it will not be overdispersed relative to a normal distribution with variation equal to variation of the overall population.

Alternatively, given two subpopulations with the same mean and different standard deviations, the overall population will exhibit high kurtosis, with a sharper peak and heavier tails (and correspondingly shallower shoulders) than a single distribution.

- (Univariate mixture distribution, showing bimodal distribution) Univariate mixture distribution, showing bimodal distribution
- (Multivariate mixture distribution, showing four modes) Multivariate mixture distribution, showing four modes

### A normal and a Cauchy distribution

The following example is adapted from Hampel, who credits John Tukey.

Consider the mixture distribution defined by

F

(

x

)   =   (1 − 10

−10

) (

standard normal

) + 10

−10

(

standard Cauchy

)

.

The mean of i.i.d. observations from *F*(*x*) behaves "normally" except for exorbitantly large samples, although the mean of *F*(*x*) does not even exist.

## Applications

Mixture densities are complicated densities expressible in terms of simpler densities (the mixture components), and are used both because they provide a good model for certain data sets (where different subsets of the data exhibit different characteristics and can best be modeled separately), and because they can be more mathematically tractable, because the individual mixture components can be more easily studied than the overall mixture density.

Mixture densities can be used to model a statistical population with subpopulations, where the mixture components are the densities on the subpopulations, and the weights are the proportions of each subpopulation in the overall population.

Mixture densities can also be used to model experimental error or contamination – one assumes that most of the samples measure the desired phenomenon, with some samples from a different, erroneous distribution.

Parametric statistics that assume no error often fail on such mixture densities – for example, statistics that assume normality often fail disastrously in the presence of even a few outliers – and instead one uses robust statistics.

In meta-analysis of separate studies, study heterogeneity causes distribution of results to be a mixture distribution, and leads to overdispersion of results relative to predicted error. For example, in a statistical survey, the margin of error (determined by sample size) predicts the sampling error and hence dispersion of results on repeated surveys. The presence of study heterogeneity (studies have different sampling bias) increases the dispersion relative to the margin of error.

---
title: "Estimator"
source: https://en.wikipedia.org/wiki/Estimator
domain: jackknife-resampling
license: CC-BY-SA-4.0
tags: jackknife resampling, bias estimator, standard error, resampling method
fetched: 2026-07-02
---

# Estimator

In statistics, an **estimator** is a rule for calculating an estimate of a given quantity based on observed data: thus the rule (the estimator), the quantity of interest (the estimand) and its result (the estimate) are distinguished. For example, the sample mean is a commonly used estimator of the population mean.

There are point and interval estimators. The point estimators yield single-valued results. This is in contrast to an interval estimator, where the result would be a range of plausible values. "Single value" does not necessarily mean "single number", but includes vector valued or function valued estimators.

*Estimation theory* is concerned with the properties of estimators; that is, with defining properties that can be used to compare different estimators (different rules for creating estimates) for the same quantity, based on the same data. Such properties can be used to determine the best rules to use under given circumstances. However, in robust statistics, statistical theory goes on to consider the balance between having good properties, if tightly defined assumptions hold, and having worse properties that hold under wider conditions.

## Discussion

An "estimator" or "point estimate" is a statistic (that is, a function of the data) that is used to infer the value of an unknown parameter in a statistical model. A common way of phrasing it is "the estimator is the method selected to obtain an estimate of an unknown parameter". The parameter being estimated is sometimes called the *estimand*. It can be either finite-dimensional (in parametric and semi-parametric models), or infinite-dimensional (semi-parametric and non-parametric models). If the parameter is denoted $\theta$ then the estimator is traditionally written by adding a circumflex over the symbol: ${\widehat {\theta }}$ . Being a function of the data, the estimator is itself a random variable; a particular realization of this random variable is called the "estimate". Sometimes the words "estimator" and "estimate" are used interchangeably.

The definition places virtually no restrictions on which functions of the data can be called the "estimators". The attractiveness of different estimators can be judged by looking at their properties, such as unbiasedness, mean square error, consistency, asymptotic distribution, etc. The construction and comparison of estimators are the subjects of the estimation theory. In the context of decision theory, an estimator is a type of decision rule, and its performance may be evaluated through the use of loss functions.

When the word "estimator" is used without a qualifier, it usually refers to point estimation. The estimate in this case is a single point in the parameter space. There also exists another type of estimator: interval estimators, where the estimates are subsets of the parameter space.

The problem of density estimation arises in two applications. Firstly, in estimating the probability density functions of random variables and secondly in estimating the spectral density function of a time series. In these problems the estimates are functions that can be thought of as point estimates in an infinite dimensional space, and there are corresponding interval estimation problems.

## Definition

Suppose a fixed *parameter* $\theta$ needs to be estimated. Then an "estimator" is a function that maps the sample space to a set of *sample estimates*. An estimator of $\theta$ is usually denoted by the symbol ${\widehat {\theta }}$ . It is often convenient to express the theory using the algebra of random variables: thus if X is used to denote a random variable corresponding to the observed data, the estimator (itself treated as a random variable) is symbolised as a function of that random variable, ${\widehat {\theta }}(X)$ . The estimate for a particular observed data value x (i.e. for $X=x$ ) is then ${\widehat {\theta }}(x)$ , which is a fixed value. Often an abbreviated notation is used in which ${\widehat {\theta }}$ is interpreted directly as a random variable, but this can cause confusion.

## Quantified properties

The following definitions and attributes are relevant.

### Error

For a given sample x , the "error" of the estimator ${\widehat {\theta }}$ is defined as $e(x)={\widehat {\theta }}(x)-\theta ,$ where $\theta$ is the parameter being estimated. The error, *e*, depends not only on the estimator (the estimation formula or procedure), but also on the sample.

### Mean squared error

The mean squared error of ${\widehat {\theta }}$ is defined as the expected value (probability-weighted average, over all samples) of the squared errors; that is, $\operatorname {MSE} ({\widehat {\theta }})=\operatorname {E} [({\widehat {\theta }}(X)-\theta )^{2}].$ It is used to indicate how far, on average, the collection of estimates are from the single parameter being estimated. Consider the following analogy. Suppose the parameter is the bull's-eye of a target, the estimator is the process of shooting arrows at the target, and the individual arrows are estimates (samples). Then high MSE means the average distance of the arrows from the bull's eye is high, and low MSE means the average distance from the bull's eye is low. The arrows may or may not be clustered. For example, even if all arrows hit the same point, yet grossly miss the target, the MSE is still relatively large. However, if the MSE is relatively low then the arrows are likely more highly clustered (than highly dispersed) around the target.

### Sampling deviation

For a given sample x , the *sampling deviation* of the estimator ${\widehat {\theta }}$ is defined as $d(x)={\widehat {\theta }}(x)-\operatorname {E} [{\widehat {\theta }}(X)]={\widehat {\theta }}(x)-\operatorname {E} [{\widehat {\theta }}],$ where $\operatorname {E} [{\widehat {\theta }}(X)]$ is the expected value of the estimator. The sampling deviation, d , depends not only on the estimator, but also on the sample.

### Variance

The variance of ${\widehat {\theta }}$ is the expected value of the squared sampling deviations; that is, $\operatorname {Var} ({\widehat {\theta }})=\operatorname {E} [({\widehat {\theta }}-\operatorname {E} [{\widehat {\theta }}])^{2}]$ . It is used to indicate how far, on average, the collection of estimates are from the *expected value* of the estimates. (Note the difference between MSE and variance.) If the parameter is the bull's-eye of a target, and the arrows are estimates, then a relatively high variance means the arrows are dispersed, and a relatively low variance means the arrows are clustered. Even if the variance is low, the cluster of arrows may still be far off-target, and even if the variance is high, the diffuse collection of arrows may still be unbiased. Finally, even if all arrows grossly miss the target, if they nevertheless all hit the same point, the variance is zero.

### Bias

The bias of ${\widehat {\theta }}$ is defined as $B({\widehat {\theta }})=\operatorname {E} [{\widehat {\theta }}]-\theta$ . It is the distance between the average of the collection of estimates, and the single parameter being estimated. The bias of ${\widehat {\theta }}$ is a function of the true value of $\theta$ so saying that the bias of ${\widehat {\theta }}$ is b means that for every $\theta$ the bias of ${\widehat {\theta }}$ is b .

There are two kinds of estimators: biased estimators and unbiased estimators. Whether an estimator is biased or not can be identified by the relationship between $\operatorname {E} [{\widehat {\theta }}]-\theta$ and 0:

- If $\operatorname {E} [{\widehat {\theta }}]-\theta \neq 0$ , ${\widehat {\theta }}$ is biased.
- If $\operatorname {E} [{\widehat {\theta }}]-\theta =0$ , ${\widehat {\theta }}$ is unbiased.

The bias is also the expected value of the error, since $\operatorname {E} [{\widehat {\theta }}]-\theta =\operatorname {E} [{\widehat {\theta }}-\theta ]$ . If the parameter is the bull's eye of a target and the arrows are estimates, then a relatively high absolute value for the bias means the average position of the arrows is off-target, and a relatively low absolute bias means the average position of the arrows is on target. They may be dispersed, or may be clustered. The relationship between bias and variance is analogous to the relationship between accuracy and precision.

The estimator ${\widehat {\theta }}$ is an unbiased estimator of $\theta$ if and only if $B({\widehat {\theta }})=0$ . Bias is a property of the estimator, not of the estimate. Often, people refer to a "biased estimate" or an "unbiased estimate", but they really are talking about an "estimate from a biased estimator", or an "estimate from an unbiased estimator". Also, people often confuse the "error" of a single estimate with the "bias" of an estimator. That the error for one estimate is large, does not mean the estimator is biased. In fact, even if all estimates have astronomical absolute values for their errors, if the expected value of the error is zero, the estimator is unbiased. Also, an estimator's being biased does not preclude the error of an estimate from being zero in a particular instance. The ideal situation is to have an unbiased estimator with low variance, and also try to limit the number of samples where the error is extreme (that is, to have few outliers). Yet unbiasedness is not essential. Often, if just a little bias is permitted, then an estimator can be found with lower mean squared error and/or fewer outlier sample estimates.

An alternative to the version of "unbiased" above, is "median-unbiased", where the median of the distribution of estimates agrees with the true value; thus, in the long run half the estimates will be too low and half too high. While this applies immediately only to scalar-valued estimators, it can be extended to any measure of central tendency of a distribution: see median-unbiased estimators.

In a practical problem, ${\widehat {\theta }}$ can always have functional relationship with $\theta$ . For example, if a genetic theory states there is a type of leaf (starchy green) that occurs with probability $p_{1}=1/4\cdot (\theta +2)$ , with $0<\theta <1$ . Then, for n leaves, the random variable $N_{1}$ , or the number of starchy green leaves, can be modeled with a $\mathrm {Bin} (n,p_{1})$ distribution. The number can be used to express the following estimator for $\theta$ : ${\widehat {\theta }}=4/n\cdot N_{1}-2$ . One can show that ${\widehat {\theta }}$ is an unbiased estimator for $\theta$ : ${\begin{aligned}\operatorname {E} [{\widehat {\theta }}]&=\operatorname {E} [4/n\cdot N_{1}-2]=4/n\cdot \operatorname {E} [N_{1}]-2\\[1ex]&=4/n\cdot np_{1}-2=4\cdot p_{1}-2\\[1ex]&=4\cdot 1/4\cdot (\theta +2)-2=\theta +2-2\\[1ex]&=\theta .\end{aligned}}$

### Unbiasedness

A desired property for estimators is the unbiased trait where an estimator is shown to have no systematic tendency to produce estimates larger or smaller than the true parameter. Additionally, unbiased estimators with smaller variances are preferred over larger variances because it will be closer to the "true" value of the parameter. The unbiased estimator with the smallest variance is known as the minimum-variance unbiased estimator (MVUE).

To find if an estimator ${\widehat {\theta }}$ is unbiased, it is easy to follow along the equation $\operatorname {E} [{\widehat {\theta }}]-\theta =0$ . With estimator *T* with and parameter of interest $\theta$ solving the previous equation so it is shown as $\operatorname {E} [T]=\theta$ the estimator is unbiased. Looking at the figure to the right despite ${\hat {\theta }}_{2}$ being the only unbiased estimator, if the distributions overlapped and were both centered around $\theta$ then distribution ${\hat {\theta }}_{1}$ would actually be the preferred unbiased estimator.

**Expectation** When looking at quantities in the interest of expectation for the model distribution there is an unbiased estimator which should satisfy the two equations below.

| ${\overline {X}}_{n}={\frac {1}{n}}\left(X_{1}+X_{2}+\cdots +X_{n}\right)$ |   | E1 |
|---|---|---|

| $\operatorname {E} \left[{\overline {X}}_{n}\right]=\mu$ |   | E2 |
|---|---|---|

**Variance** Similarly, when looking at quantities in the interest of variance as the model distribution there is also an unbiased estimator that should satisfy the two equations below.

| $S_{n}^{2}={\frac {1}{n-1}}\sum _{i=1}^{n}\left(X_{i}-{\bar {X}}\right)^{2}$ |   | V1 |
|---|---|---|

| $\operatorname {E} \left[S_{n}^{2}\right]=\sigma ^{2}$ |   | V2 |
|---|---|---|

Note we are dividing by *n* − 1 because if we divided with *n* we would obtain an estimator with a negative bias which would thus produce estimates that are too small for $\sigma ^{2}$ . It should also be mentioned that even though $S_{n}^{2}$ is unbiased for $\sigma ^{2}$ the reverse is not true.

### Relationships among the quantities

- The mean squared error, variance, and bias, are related: $\operatorname {MSE} ({\widehat {\theta }})=\operatorname {Var} ({\widehat {\theta }})+(B({\widehat {\theta }}))^{2},$ i.e. mean squared error = variance + square of bias. In particular, for an unbiased estimator, the variance equals the mean squared error.
- The standard deviation of an estimator ${\widehat {\theta }}$ of $\theta$ (the square root of the variance), or an estimate of the standard deviation of an estimator ${\widehat {\theta }}$ of $\theta$ , is called the *standard error* of ${\widehat {\theta }}$ .
- The bias-variance tradeoff will be used in model complexity, over-fitting and under-fitting. It is mainly used in the field of supervised learning and predictive modelling to diagnose the performance of algorithms.

### Example

Consider a random variable following a normal probability distribution $X\sim {\mathcal {N}}(\mu ,\sigma ^{2})$ , and a biased estimator of the mean $\mu =\theta$ of that distribution ${\hat {\theta }}(X)={\bar {X}}_{n}+B={\frac {1}{n}}\sum _{i=1}^{n}X_{i}+B,$ where B follows a degenerate distribution, i.e. $P(B=b)=1$ , such that $\mathrm {E} [{\hat {\theta }}(X)]=\mathrm {E} [{\bar {X}}_{n}]+\mathrm {E} [B]=\mu +b,$ $\mathrm {B} ({\hat {\theta }}(X))=b,$ ${\begin{aligned}\mathrm {Var} ({\hat {\theta }}(X))&=\mathrm {E} [({\bar {X}}_{n}+B-\mu -b)^{2}]\\[2ex]&={\color [rgb]{0.12156862745098039,0.4666666666666667,0.7058823529411765}\mathrm {E} [({\bar {X}}_{n}-\mu )^{2}]}+{\color [rgb]{1,0.4980392156862745,0.054901960784313725}\mathrm {E} [(B-b)^{2}]}+{\color [rgb]{0.17254901960784313,0.6274509803921569,0.17254901960784313}2\mathrm {E} [({\bar {X}}_{n}-\mu )(B-b)]}\\[2ex]&={\color [rgb]{0.12156862745098039,0.4666666666666667,0.7058823529411765}\mathrm {Var} ({\bar {X}}_{n}-\mu )+\mathrm {E} [({\bar {X}}_{n}-\mu )^{2}]}+{\color [rgb]{1,0.4980392156862745,0.054901960784313725}\mathrm {Var} (B-b)+\mathrm {E} [(B-b)^{2}]}\\[0.5ex]&\qquad {}+{\color [rgb]{0.17254901960784313,0.6274509803921569,0.17254901960784313}2\underbrace {\mathrm {Cov} ({\bar {X}}_{n}-\mu ,B-b)} _{|\cdots |^{2}\leqslant \mathrm {Var} ({\bar {X}}_{n}-\mu )\mathrm {Var} (B-b)=0}+2\mathrm {E} [{\bar {X}}_{n}-\mu ]\mathrm {E} [B-b]}\\&={\frac {\sigma ^{2}}{n}},\end{aligned}}$ where all the terms are zero except $\mathrm {Var} ({\bar {X}}_{n}-\mu )=\mathrm {Var} ({\bar {X}}_{n})={\frac {\sigma ^{2}}{n}}$ using the Bienaymé formula, and $\mathrm {MSE} ({\hat {\theta }}(X))=\mathrm {E} [({\bar {X}}_{n}+B-\mu )^{2}]=\mathrm {E} [({\bar {X}}_{n}-\mu )^{2}]+\mathrm {E} [B^{2}]={\frac {\sigma ^{2}}{n}}+b^{2}.$ We verify the relation between the mean square error, the variance and the bias. Below are illustrated the quantified properties of the estimation of the probability distribution mean, taking $\mu =0$ , $\sigma =1$ and $b=1/2$ .

Probability density function

$\phi$

of the standard normal distribution (blue) with a sample

$\{x_{i}\}_{n}$

of

$n=10$

values (

${\color [rgb]{1,0.4980392156862745,0.054901960784313725}\bullet }$

) and the associated estimate

${\hat {\theta }}(\{x_{i}\}_{n})$

(

${\color [rgb]{0.17254901960784313,0.6274509803921569,0.17254901960784313}\blacksquare }$

). The mean

$\theta =0$

of the original distribution and the mean

$\mathrm {E} ({\hat {\theta }})=1/2$

of the estimator (which is the mean of its sampling distribution, see right picture) are also shown, along with the error

e

and sampling deviation

d

.

Sampling distribution

of the estimator

${\hat {\theta }}(X)$

with mean, variance (square of the

standard error

), and mean square error. In red is the exact distribution that is

known

in the case where the original distribution is normal and the estimator is the (biased) sample mean. In green is shown the histogram of 20000 estimates. The histogram converges to the exact distribution in the limit of infinite samples. Note that for a given number of estimates, the

central limit theorem

ensures that the estimate distribution of the (biased) sample mean estimator also converges to the exact distribution in the limit of infinite sample size.

## Behavioral properties

### Consistency

A **consistent estimator** is an estimator whose sequence of estimates converge in probability to the quantity being estimated as the index (usually the sample size) grows without bound. In other words, increasing the sample size increases the probability of the estimator being close to the population parameter.

Mathematically, an estimator is a consistent estimator for parameter $\theta$ , if and only if for the sequence of estimates $\{t_{n}:n\in \mathbb {N} \}$ , and for all $\varepsilon >0$ , no matter how small, we have $\lim _{n\to \infty }\Pr \left\{\left|t_{n}-\theta \right|\leq \varepsilon \right\}=1.$ The consistency defined above may be called weak consistency. The sequence is *strongly consistent*, if it converges almost surely to the true value.

An estimator that converges to a *multiple* of a parameter can be made into a consistent estimator by multiplying the estimator by a scale factor, namely the true value divided by the asymptotic value of the estimator. This occurs frequently in estimation of scale parameters by measures of statistical dispersion.

### Fisher consistency

An estimator can be considered Fisher consistent as long as the estimator is the same functional of the empirical distribution function as the true distribution function. Following the formula: ${\widehat {\theta }}=h(T_{n}),\theta =h(T_{\theta })$ Where $T_{n}$ and $T_{\theta }$ are the empirical distribution function and theoretical distribution function, respectively. An easy example to see if some estimator is Fisher consistent is to check the consistency of mean and variance. For example, to check consistency for the mean ${\widehat {\mu }}={\bar {X}}$ and to check for variance confirm that ${\widehat {\sigma }}^{2}=SSD/n$ .

### Asymptotic normality

An asymptotically normal estimator is a consistent estimator whose distribution around the true parameter $\theta$ approaches a normal distribution with standard deviation shrinking in proportion to $1/{\sqrt {n}}$ as the sample size n grows. Using ${\xrightarrow {D}}$ to denote convergence in distribution, an estimator $t_{n}$ is asymptotically normal if ${\sqrt {n}}(t_{n}-\theta )\ \xrightarrow {D} \ N(0,V),$ for some V .

In this formulation $V/n$ can be called the *asymptotic variance* of the estimator. However, some authors also call V the *asymptotic variance*. Note that convergence will not necessarily have occurred for any finite n , therefore this value is only an approximation to the true variance of the estimator, while in the limit the asymptotic variance $V/n$ is simply zero. In particular, the distribution of the estimator $t_{n}$ converges weakly to a dirac delta function centered at $\theta$ .

Under mild conditions on the distribution of the data, the central limit theorem implies asymptotic normality of the sample mean ${\bar {X}}$ as an estimator of the true mean. More generally, maximum likelihood estimators are asymptotically normal under fairly weak regularity conditions — see the asymptotics section of the maximum likelihood article. However, not all estimators are asymptotically normal; the simplest examples are found when the true value of a parameter lies on the boundary of the allowable parameter region.

### Efficiency

The efficiency of an estimator is used to estimate the quantity of interest in a "minimum error" manner. In reality, there is not an explicit best estimator; there can only be a better estimator. Whether the efficiency of an estimator is better or not is based on the choice of a particular loss function, and it is reflected by two naturally desirable properties of estimators: to be unbiased $\operatorname {E} [{\widehat {\theta }}]-\theta =0$ and have minimal mean squared error (MSE) $\operatorname {E} [({\widehat {\theta }}-\theta )^{2}]$ . These cannot in general both be satisfied simultaneously: a biased estimator may have a lower mean squared error than any unbiased estimator (see estimator bias).

This equation relates the mean squared error with the estimator bias: $\operatorname {E} [({\widehat {\theta }}-\theta )^{2}]=\left(\operatorname {E} [{\widehat {\theta }}]-\theta \right)^{2}+\operatorname {Var} ({\widehat {\theta }})$ The first term represents the mean squared error; the second term represents the square of the estimator bias; and the third term represents the variance of the estimator. The quality of the estimator can be identified from the comparison between the variance, the square of the estimator bias, or the MSE. The variance of the good estimator (good efficiency) would be smaller than the variance of the bad estimator (bad efficiency). The square of an estimator bias with a good estimator would be smaller than the estimator bias with a bad estimator. The MSE of a good estimator would be smaller than the MSE of the bad estimator. Suppose there are two estimator, ${\widehat {\theta }}_{1}$ is the good estimator and ${\widehat {\theta }}_{2}$ is the bad estimator. The above relationship can be expressed by the following formulas: ${\begin{aligned}&\operatorname {Var} ({\widehat {\theta }}_{1})<\operatorname {Var} ({\widehat {\theta }}_{2}),\\[0.2cm]&\left|\operatorname {E} ({\widehat {\theta }}_{1})-\theta \right|<\left|\operatorname {E} ({\widehat {\theta }}_{2})-\theta \right|,\\[0.2cm]&\operatorname {MSE} ({\widehat {\theta }}_{1})<\operatorname {MSE} ({\widehat {\theta }}_{2}).\end{aligned}}$ Besides using formula to identify the efficiency of the estimator, it can also be identified through the graph. If an estimator is efficient, in the frequency vs. value graph, there will be a curve with high frequency at the center and low frequency on the two sides. For example:

If an estimator is not efficient, the frequency vs. value graph, there will be a relatively more gentle curve.

To put it simply, the good estimator has a narrow curve, while the bad estimator has a large curve. Plotting these two curves on one graph with a shared *y*-axis, the difference becomes more obvious.

Among unbiased estimators, there often exists one with the lowest variance, called the minimum variance unbiased estimator (MVUE). In some cases an unbiased efficient estimator exists, which, in addition to having the lowest variance among unbiased estimators, satisfies the Cramér–Rao bound, which is an absolute lower bound on variance for statistics of a variable.

Concerning such "best unbiased estimators", see also Cramér–Rao bound, Gauss–Markov theorem, Lehmann–Scheffé theorem, Rao–Blackwell theorem.

### Robustness

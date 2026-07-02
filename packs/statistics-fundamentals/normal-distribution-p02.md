---
title: "Normal distribution (part 2/3)"
source: https://en.wikipedia.org/wiki/Normal_distribution
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 2/3
---

## Statistical inference

### Estimation of parameters

It is often the case that we do not know the parameters of the normal distribution, but instead want to estimate them. That is, having a sample ${\textstyle (x_{1},\ldots ,x_{n})}$ from a normal ${\textstyle {\mathcal {N}}(\mu ,\sigma ^{2})}$ population we would like to learn the approximate values of parameters ⁠ $\mu$ ⁠ and ${\textstyle \sigma ^{2}}$ . The standard approach to this problem is the maximum likelihood method, which requires maximization of the *log-likelihood function*: ${\begin{aligned}\ln {\mathcal {L}}(\mu ,\sigma ^{2})&=\sum _{i=1}^{n}\ln f(x_{i}\mid \mu ,\sigma ^{2})\\&=-{\frac {n}{2}}\ln(2\pi )-{\frac {n}{2}}\ln \sigma ^{2}-{\frac {1}{2\sigma ^{2}}}\sum _{i=1}^{n}(x_{i}-\mu )^{2}.\end{aligned}}$ Taking derivatives with respect to ⁠ $\mu$ ⁠ and ${\textstyle \sigma ^{2}}$ and solving the resulting system of first order conditions yields the *maximum likelihood estimates*: ${\hat {\mu }}={\overline {x}}\equiv {\frac {1}{n}}\sum _{i=1}^{n}x_{i},\qquad {\hat {\sigma }}^{2}={\frac {1}{n}}\sum _{i=1}^{n}(x_{i}-{\overline {x}})^{2}.$

Then ${\textstyle \ln {\mathcal {L}}({\hat {\mu }},{\hat {\sigma }}^{2})}$ is as follows: $\ln {\mathcal {L}}({\hat {\mu }},{\hat {\sigma }}^{2})=-{\frac {n}{2}}[\ln \left(2\pi {\hat {\sigma }}^{2}\right)+1]$

#### Sample mean

Estimator $\textstyle {\hat {\mu }}$ is called the *sample mean*, since it is the arithmetic mean of all observations. The statistic $\textstyle {\overline {x}}$ is complete and sufficient for ⁠ $\mu$ ⁠, and therefore by the Lehmann–Scheffé theorem, $\textstyle {\hat {\mu }}$ is the uniformly minimum variance unbiased (UMVU) estimator. In finite samples it is distributed normally: ${\hat {\mu }}\sim {\mathcal {N}}(\mu ,\sigma ^{2}/n).$ The variance of this estimator is equal to the *μμ*-element of the inverse Fisher information matrix $\textstyle {\mathcal {I}}^{-1}$ . This implies that the estimator is finite-sample efficient. Of practical importance is the standard error of $\textstyle {\hat {\mu }}$ being proportional to $\textstyle 1/{\sqrt {n}}$ , that is, if one wishes to decrease the standard error by a factor of 10, one must increase the number of points in the sample by a factor of 100. This fact is widely used in determining sample sizes for opinion polls and the number of trials in Monte Carlo simulations.

From the standpoint of the asymptotic theory, $\textstyle {\hat {\mu }}$ is consistent, that is, it converges in probability to ⁠ $\mu$ ⁠ as ${\textstyle n\rightarrow \infty }$ . The estimator is also asymptotically normal, which is a simple corollary of it being normal in finite samples: ${\sqrt {n}}({\hat {\mu }}-\mu )\,\xrightarrow {d} \,{\mathcal {N}}(0,\sigma ^{2}).$

#### Sample variance

The estimator $\textstyle {\hat {\sigma }}^{2}$ is called the *sample variance*, since it is the variance of the sample ( ${\textstyle (x_{1},\ldots ,x_{n})}$ ). In practice, another estimator is often used instead of the $\textstyle {\hat {\sigma }}^{2}$ . This other estimator is denoted ${\textstyle s^{2}}$ , and is also called the *sample variance*, which represents a certain ambiguity in terminology; its square root ⁠ s ⁠ is called the *sample standard deviation*. The estimator ${\textstyle s^{2}}$ differs from $\textstyle {\hat {\sigma }}^{2}$ by having (*n* − 1) instead of n in the denominator (the so-called Bessel's correction): $s^{2}={\frac {n}{n-1}}{\hat {\sigma }}^{2}={\frac {1}{n-1}}\sum _{i=1}^{n}(x_{i}-{\overline {x}})^{2}.$ The difference between ${\textstyle s^{2}}$ and $\textstyle {\hat {\sigma }}^{2}$ becomes negligibly small for large n's. In finite samples however, the motivation behind the use of ${\textstyle s^{2}}$ is that it is an unbiased estimator of the underlying parameter ${\textstyle \sigma ^{2}}$ , whereas $\textstyle {\hat {\sigma }}^{2}$ is biased. Also, by the Lehmann–Scheffé theorem the estimator ${\textstyle s^{2}}$ is uniformly minimum variance unbiased (UMVU), which makes it the "best" estimator among all unbiased ones. However it can be shown that the biased estimator $\textstyle {\hat {\sigma }}^{2}$ is better than the ${\textstyle s^{2}}$ in terms of the mean squared error (MSE) criterion. In finite samples both ${\textstyle s^{2}}$ and $\textstyle {\hat {\sigma }}^{2}$ have scaled chi-squared distribution with (*n* − 1) degrees of freedom: $s^{2}\sim {\frac {\sigma ^{2}}{n-1}}\cdot \chi _{n-1}^{2},\qquad {\hat {\sigma }}^{2}\sim {\frac {\sigma ^{2}}{n}}\cdot \chi _{n-1}^{2}.$ The first of these expressions shows that the variance of ${\textstyle s^{2}}$ is equal to ${\textstyle 2\sigma ^{4}/(n-1)}$ , which is slightly greater than the *σσ*-element of the inverse Fisher information matrix $\textstyle {\mathcal {I}}^{-1}$ , which is ${\textstyle 2\sigma ^{4}/n}$ . Thus, ${\textstyle s^{2}}$ is not an efficient estimator for ${\textstyle \sigma ^{2}}$ , and moreover, since ${\textstyle s^{2}}$ is UMVU, we can conclude that the finite-sample efficient estimator for ${\textstyle \sigma ^{2}}$ does not exist.

Applying the asymptotic theory, both estimators ${\textstyle s^{2}}$ and $\textstyle {\hat {\sigma }}^{2}$ are consistent, that is they converge in probability to ${\textstyle \sigma ^{2}}$ as the sample size ${\textstyle n\rightarrow \infty }$ . The two estimators are also both asymptotically normal: ${\sqrt {n}}({\hat {\sigma }}^{2}-\sigma ^{2})\simeq {\sqrt {n}}(s^{2}-\sigma ^{2})\,\xrightarrow {d} \,{\mathcal {N}}(0,2\sigma ^{4}).$ In particular, both estimators are asymptotically efficient for ${\textstyle \sigma ^{2}}$ .

### Confidence intervals

By Cochran's theorem, for normal distributions the sample mean $\textstyle {\hat {\mu }}$ and the sample variance *s*2 are independent, which means there can be no gain in considering their joint distribution. There is also a converse theorem: if in a sample the sample mean and sample variance are independent, then the sample must have come from the normal distribution. The independence between $\textstyle {\hat {\mu }}$ and s can be employed to construct the so-called *t-statistic*: $t={\frac {{\hat {\mu }}-\mu }{s/{\sqrt {n}}}}={\frac {{\overline {x}}-\mu }{\sqrt {{\frac {1}{n(n-1)}}\sum (x_{i}-{\overline {x}})^{2}}}}\sim t_{n-1}$ This quantity t has the Student's t-distribution with (*n* − 1) degrees of freedom, and it is an ancillary statistic (independent of the value of the parameters). Inverting the distribution of this t-statistics will allow us to construct the confidence interval for μ; similarly, inverting the *χ*2 distribution of the statistic *s*2 will give us the confidence interval for *σ*2: $\mu \in \left[{\hat {\mu }}-t_{n-1,1-\alpha /2}{\frac {s}{\sqrt {n}}},\,{\hat {\mu }}+t_{n-1,1-\alpha /2}{\frac {s}{\sqrt {n}}}\right]$ $\sigma ^{2}\in \left[{\frac {n-1}{\chi _{n-1,1-\alpha /2}^{2}}}s^{2},\,{\frac {n-1}{\chi _{n-1,\alpha /2}^{2}}}s^{2}\right]$ where *t**k*,*p* and χ 2 *k,p*  are the pth quantiles of the t- and *χ*2-distributions respectively. These confidence intervals are of the *confidence level* 1 − *α*, meaning that the true values μ and *σ*2 fall outside of these intervals with probability (or significance level) α. In practice people usually take *α* = 5%, resulting in the 95% confidence intervals. The confidence interval for σ can be found by taking the square root of the interval bounds for *σ*2.

Approximate formulas can be derived from the asymptotic distributions of $\textstyle {\hat {\mu }}$ and *s*2: $\mu \in \left[{\hat {\mu }}-{\frac {|z_{\alpha /2}|}{\sqrt {n}}}s,\,{\hat {\mu }}+{\frac {|z_{\alpha /2}|}{\sqrt {n}}}s\right]$ $\sigma ^{2}\in \left[s^{2}-{\sqrt {2}}{\frac {|z_{\alpha /2}|}{\sqrt {n}}}s^{2},\,s^{2}+{\sqrt {2}}{\frac {|z_{\alpha /2}|}{\sqrt {n}}}s^{2}\right]$ The approximate formulas become valid for large values of n, and are more convenient for the manual calculation since the standard normal quantiles *z**α*/2 do not depend on n. In particular, the most popular value of *α* = 5%, results in |*z*0.025| = 1.96.

### Normality tests

Normality tests assess the likelihood that the given data set {*x*1, ..., *x**n*} comes from a normal distribution. Typically the null hypothesis *H*0 is that the observations are distributed normally with unspecified mean μ and variance *σ*2, versus the alternative *H**a* that the distribution is arbitrary. Many tests (over 40) have been devised for this problem. The more prominent of them are outlined below:

**Diagnostic plots** are more intuitively appealing but subjective at the same time, as they rely on informal human judgement to accept or reject the null hypothesis.

- Q–Q plot, also known as normal probability plot or rankit plot—is a plot of the sorted values from the data set against the expected values of the corresponding quantiles from the standard normal distribution. That is, it is a plot of point of the form (*Φ*−1(*p**k*), *x*(*k*)), where plotting points *p**k* are equal to *p**k* = (*k* − *α*)/(*n* + 1 − 2*α*) and α is an adjustment constant, which can be anything between 0 and 1. If the null hypothesis is true, the plotted points should approximately lie on a straight line.
- P–P plot – similar to the Q–Q plot, but used much less frequently. This method consists of plotting the points (*Φ*(*z*(*k*)), *p**k*), where ${\textstyle \textstyle z_{(k)}=(x_{(k)}-{\hat {\mu }})/{\hat {\sigma }}}$ . For normally distributed data this plot should lie on a straight line between (0, 0) and (1, 1).

**Goodness-of-fit tests**:

*Moment-based tests*:

- D'Agostino's K-squared test
- Jarque–Bera test
- Shapiro–Wilk test: This is based on the line in the Q–Q plot having the slope of σ. The test compares the least squares estimate of that slope with the value of the sample variance, and rejects the null hypothesis if these two quantities differ significantly.

*Tests based on the empirical distribution function*:

- Anderson–Darling test
- Lilliefors test (an adaptation of the Kolmogorov–Smirnov test)

### Bayesian analysis of the normal distribution

Bayesian analysis of normally distributed data is complicated by the many different possibilities that may be considered:

- Either the mean, or the variance, or neither, may be considered a fixed quantity.
- When the variance is unknown, analysis may be done directly in terms of the variance, or in terms of the precision, the reciprocal of the variance. The reason for expressing the formulas in terms of precision is that the analysis of most cases is simplified.
- Both univariate and multivariate cases need to be considered.
- Either conjugate or improper prior distributions may be placed on the unknown variables.
- An additional set of cases occurs in Bayesian linear regression, where in the basic model the data is assumed to be normally distributed, and normal priors are placed on the regression coefficients. The resulting analysis is similar to the basic cases of independent identically distributed data.

The formulas for the non-linear-regression cases are summarized in the conjugate prior article.

#### Sum of two quadratics

##### Scalar form

The following auxiliary formula is useful for simplifying the posterior update equations, which otherwise become fairly tedious.

$a(x-y)^{2}+b(x-z)^{2}=(a+b)\left(x-{\frac {ay+bz}{a+b}}\right)^{2}+{\frac {ab}{a+b}}(y-z)^{2}$

This equation rewrites the sum of two quadratics in x by expanding the squares, grouping the terms in x, and completing the square. Note the following about the complex constant factors attached to some of the terms:

1. The factor ${\textstyle {\frac {ay+bz}{a+b}}}$ has the form of a weighted average of y and z.
2. ${\textstyle {\frac {ab}{a+b}}={\frac {1}{{\frac {1}{a}}+{\frac {1}{b}}}}=(a^{-1}+b^{-1})^{-1}.}$ This shows that this factor can be thought of as resulting from a situation where the reciprocals of quantities a and b add directly, so to combine a and b themselves, it is necessary to reciprocate, add, and reciprocate the result again to get back into the original units. This is exactly the sort of operation performed by the harmonic mean, so it is not surprising that ${\textstyle {\frac {ab}{a+b}}}$ is one-half the harmonic mean of a and b.

##### Vector form

A similar formula can be written for the sum of two vector quadratics: If **x**, **y**, **z** are vectors of length k, and **A** and **B** are symmetric, invertible matrices of size ${\textstyle k\times k}$ , then

${\begin{aligned}&(\mathbf {y} -\mathbf {x} )'\mathbf {A} (\mathbf {y} -\mathbf {x} )+(\mathbf {x} -\mathbf {z} )'\mathbf {B} (\mathbf {x} -\mathbf {z} )\\={}&(\mathbf {x} -\mathbf {c} )'(\mathbf {A} +\mathbf {B} )(\mathbf {x} -\mathbf {c} )+(\mathbf {y} -\mathbf {z} )'(\mathbf {A} ^{-1}+\mathbf {B} ^{-1})^{-1}(\mathbf {y} -\mathbf {z} )\end{aligned}}$ where $\mathbf {c} =(\mathbf {A} +\mathbf {B} )^{-1}(\mathbf {A} \mathbf {y} +\mathbf {B} \mathbf {z} )$

The form **x**′ **A** **x** is called a quadratic form and is a scalar: $\mathbf {x} '\mathbf {A} \mathbf {x} =\sum _{i,j}a_{ij}x_{i}x_{j}$ In other words, it sums up all possible combinations of products of pairs of elements from **x**, with a separate coefficient for each. In addition, since ${\textstyle x_{i}x_{j}=x_{j}x_{i}}$ , only the sum ${\textstyle a_{ij}+a_{ji}}$ matters for any off-diagonal elements of **A**, and there is no loss of generality in assuming that **A** is symmetric. Furthermore, if **A** is symmetric, then the form ${\textstyle \mathbf {x} '\mathbf {A} \mathbf {y} =\mathbf {y} '\mathbf {A} \mathbf {x} .}$

#### Sum of differences from the mean

Another useful formula is as follows: $\sum _{i=1}^{n}(x_{i}-\mu )^{2}=\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}+n({\bar {x}}-\mu )^{2}$ where ${\textstyle {\bar {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}.}$

### With known variance

For a set of i.i.d. normally distributed data points **X** of size n where each individual point x follows ${\textstyle x\sim {\mathcal {N}}(\mu ,\sigma ^{2})}$ with known variance *σ*2, the conjugate prior distribution is also normally distributed.

This can be shown more easily by rewriting the variance as the precision, i.e. using *τ* = 1/*σ*2. Then if ${\textstyle x\sim {\mathcal {N}}(\mu ,1/\tau )}$ and ${\textstyle \mu \sim {\mathcal {N}}(\mu _{0},1/\tau _{0}),}$ we proceed as follows.

First, the likelihood function is (using the formula above for the sum of differences from the mean): ${\begin{aligned}p(\mathbf {X} \mid \mu ,\tau )&=\prod _{i=1}^{n}{\sqrt {\frac {\tau }{2\pi }}}\exp \left(-{\frac {1}{2}}\tau (x_{i}-\mu )^{2}\right)\\&=\left({\frac {\tau }{2\pi }}\right)^{n/2}\exp \left(-{\frac {1}{2}}\tau \sum _{i=1}^{n}(x_{i}-\mu )^{2}\right)\\&=\left({\frac {\tau }{2\pi }}\right)^{n/2}\exp \left[-{\frac {1}{2}}\tau \left(\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}+n({\bar {x}}-\mu )^{2}\right)\right].\end{aligned}}$

Then, we proceed as follows: ${\begin{aligned}p(\mu \mid \mathbf {X} )&\propto p(\mathbf {X} \mid \mu )p(\mu )\\&=\left({\frac {\tau }{2\pi }}\right)^{n/2}\exp \left[-{\frac {1}{2}}\tau \left(\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}+n({\bar {x}}-\mu )^{2}\right)\right]{\sqrt {\frac {\tau _{0}}{2\pi }}}\exp \left(-{\frac {1}{2}}\tau _{0}(\mu -\mu _{0})^{2}\right)\\&\propto \exp \left(-{\frac {1}{2}}\left(\tau \left(\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}+n({\bar {x}}-\mu )^{2}\right)+\tau _{0}(\mu -\mu _{0})^{2}\right)\right)\\&\propto \exp \left(-{\frac {1}{2}}\left(n\tau ({\bar {x}}-\mu )^{2}+\tau _{0}(\mu -\mu _{0})^{2}\right)\right)\\&=\exp \left(-{\frac {1}{2}}(n\tau +\tau _{0})\left(\mu -{\dfrac {n\tau {\bar {x}}+\tau _{0}\mu _{0}}{n\tau +\tau _{0}}}\right)^{2}+{\frac {n\tau \tau _{0}}{n\tau +\tau _{0}}}({\bar {x}}-\mu _{0})^{2}\right)\\&\propto \exp \left(-{\frac {1}{2}}(n\tau +\tau _{0})\left(\mu -{\dfrac {n\tau {\bar {x}}+\tau _{0}\mu _{0}}{n\tau +\tau _{0}}}\right)^{2}\right)\end{aligned}}$

In the above derivation, we used the formula above for the sum of two quadratics and eliminated all constant factors not involving μ. The result is the kernel of a normal distribution, with mean ${\textstyle {\frac {n\tau {\bar {x}}+\tau _{0}\mu _{0}}{n\tau +\tau _{0}}}}$ and precision ${\textstyle n\tau +\tau _{0}}$ , i.e. $p(\mu \mid \mathbf {X} )\sim {\mathcal {N}}\left({\frac {n\tau {\bar {x}}+\tau _{0}\mu _{0}}{n\tau +\tau _{0}}},{\frac {1}{n\tau +\tau _{0}}}\right)$

This can be written as a set of Bayesian update equations for the posterior parameters in terms of the prior parameters: ${\begin{aligned}\tau _{0}'&=\tau _{0}+n\tau \\[5pt]\mu _{0}'&={\frac {n\tau {\bar {x}}+\tau _{0}\mu _{0}}{n\tau +\tau _{0}}}\\[5pt]{\bar {x}}&={\frac {1}{n}}\sum _{i=1}^{n}x_{i}\end{aligned}}$

That is, to combine n data points with total precision of *nτ* (or equivalently, total variance of *n*/*σ*2) and mean of values ${\textstyle {\bar {x}}}$ , derive a new total precision simply by adding the total precision of the data to the prior total precision, and form a new mean through a *precision-weighted average*, i.e. a weighted average of the data mean and the prior mean, each weighted by the associated total precision. This makes logical sense if the precision is thought of as indicating the certainty of the observations: In the distribution of the posterior mean, each of the input components is weighted by its certainty, and the certainty of this distribution is the sum of the individual certainties. (For the intuition of this, compare the expression "the whole is (or is not) greater than the sum of its parts". In addition, consider that the knowledge of the posterior comes from a combination of the knowledge of the prior and likelihood, so it makes sense that we are more certain of it than of either of its components.)

The above formula reveals why it is more convenient to do Bayesian analysis of conjugate priors for the normal distribution in terms of the precision. The posterior precision is simply the sum of the prior and likelihood precisions, and the posterior mean is computed through a precision-weighted average, as described above. The same formulas can be written in terms of variance by reciprocating all the precisions, yielding the more ugly formulas ${\begin{aligned}{\sigma _{0}^{2}}'&={\frac {1}{{\frac {n}{\sigma ^{2}}}+{\frac {1}{\sigma _{0}^{2}}}}}\\[5pt]\mu _{0}'&={\frac {{\frac {n{\bar {x}}}{\sigma ^{2}}}+{\frac {\mu _{0}}{\sigma _{0}^{2}}}}{{\frac {n}{\sigma ^{2}}}+{\frac {1}{\sigma _{0}^{2}}}}}\\[5pt]{\bar {x}}&={\frac {1}{n}}\sum _{i=1}^{n}x_{i}\end{aligned}}$

#### With known mean

For a set of i.i.d. normally distributed data points **X** of size n where each individual point x follows ${\textstyle x\sim {\mathcal {N}}(\mu ,\sigma ^{2})}$ with known mean μ, the conjugate prior of the variance has an inverse gamma distribution or a scaled inverse chi-squared distribution. The two are equivalent except for having different parameterizations. Although the inverse gamma is more commonly used, we use the scaled inverse chi-squared for the sake of convenience. The prior for *σ*2 is as follows: $p(\sigma ^{2}\mid \nu _{0},\sigma _{0}^{2})={\frac {(\sigma _{0}^{2}{\frac {\nu _{0}}{2}})^{\nu _{0}/2}}{\Gamma \left({\frac {\nu _{0}}{2}}\right)}}~{\frac {\exp \left[{\frac {-\nu _{0}\sigma _{0}^{2}}{2\sigma ^{2}}}\right]}{(\sigma ^{2})^{1+{\frac {\nu _{0}}{2}}}}}\propto {\frac {\exp \left[{\frac {-\nu _{0}\sigma _{0}^{2}}{2\sigma ^{2}}}\right]}{(\sigma ^{2})^{1+{\frac {\nu _{0}}{2}}}}}$

The likelihood function from above, written in terms of the variance, is: ${\begin{aligned}p(\mathbf {X} \mid \mu ,\sigma ^{2})&=\left({\frac {1}{2\pi \sigma ^{2}}}\right)^{n/2}\exp \left[-{\frac {1}{2\sigma ^{2}}}\sum _{i=1}^{n}(x_{i}-\mu )^{2}\right]\\&=\left({\frac {1}{2\pi \sigma ^{2}}}\right)^{n/2}\exp \left[-{\frac {S}{2\sigma ^{2}}}\right]\end{aligned}}$ where $S=\sum _{i=1}^{n}(x_{i}-\mu )^{2}.$

Then: ${\begin{aligned}p(\sigma ^{2}\mid \mathbf {X} )&\propto p(\mathbf {X} \mid \sigma ^{2})p(\sigma ^{2})\\&=\left({\frac {1}{2\pi \sigma ^{2}}}\right)^{n/2}\exp \left[-{\frac {S}{2\sigma ^{2}}}\right]{\frac {(\sigma _{0}^{2}{\frac {\nu _{0}}{2}})^{\frac {\nu _{0}}{2}}}{\Gamma \left({\frac {\nu _{0}}{2}}\right)}}~{\frac {\exp \left[{\frac {-\nu _{0}\sigma _{0}^{2}}{2\sigma ^{2}}}\right]}{(\sigma ^{2})^{1+{\frac {\nu _{0}}{2}}}}}\\&\propto \left({\frac {1}{\sigma ^{2}}}\right)^{n/2}{\frac {1}{(\sigma ^{2})^{1+{\frac {\nu _{0}}{2}}}}}\exp \left[-{\frac {S}{2\sigma ^{2}}}+{\frac {-\nu _{0}\sigma _{0}^{2}}{2\sigma ^{2}}}\right]\\&={\frac {1}{(\sigma ^{2})^{1+{\frac {\nu _{0}+n}{2}}}}}\exp \left[-{\frac {\nu _{0}\sigma _{0}^{2}+S}{2\sigma ^{2}}}\right]\end{aligned}}$

The above is also a scaled inverse chi-squared distribution where ${\begin{aligned}\nu _{0}'&=\nu _{0}+n\\\nu _{0}'{\sigma _{0}^{2}}'&=\nu _{0}\sigma _{0}^{2}+\sum _{i=1}^{n}(x_{i}-\mu )^{2}\end{aligned}}$ or equivalently ${\begin{aligned}\nu _{0}'&=\nu _{0}+n\\{\sigma _{0}^{2}}'&={\frac {\nu _{0}\sigma _{0}^{2}+\sum _{i=1}^{n}(x_{i}-\mu )^{2}}{\nu _{0}+n}}\end{aligned}}$

Reparameterizing in terms of an inverse gamma distribution, the result is: ${\begin{aligned}\alpha '&=\alpha +{\frac {n}{2}}\\\beta '&=\beta +{\frac {\sum _{i=1}^{n}(x_{i}-\mu )^{2}}{2}}\end{aligned}}$

#### With unknown mean and unknown variance

For a set of i.i.d. normally distributed data points **X** of size n where each individual point x follows ${\textstyle x\sim {\mathcal {N}}(\mu ,\sigma ^{2})}$ with unknown mean μ and unknown variance *σ*2, a combined (multivariate) conjugate prior is placed over the mean and variance, consisting of a normal-inverse-gamma distribution. Logically, this originates as follows:

1. From the analysis of the case with unknown mean but known variance, we see that the update equations involve sufficient statistics computed from the data consisting of the mean of the data points and the total variance of the data points, computed in turn from the known variance divided by the number of data points.
2. From the analysis of the case with unknown variance but known mean, we see that the update equations involve sufficient statistics over the data consisting of the number of data points and sum of squared deviations.
3. Keep in mind that the posterior update values serve as the prior distribution when further data is handled. Thus, we should logically think of our priors in terms of the sufficient statistics just described, with the same semantics kept in mind as much as possible.
4. To handle the case where both mean and variance are unknown, we could place independent priors over the mean and variance, with fixed estimates of the average mean, total variance, number of data points used to compute the variance prior, and sum of squared deviations. Note however that in reality, the total variance of the mean depends on the unknown variance, and the sum of squared deviations that goes into the variance prior (appears to) depend on the unknown mean. In practice, the latter dependence is relatively unimportant: Shifting the actual mean shifts the generated points by an equal amount, and on average the squared deviations will remain the same. This is not the case, however, with the total variance of the mean: As the unknown variance increases, the total variance of the mean will increase proportionately, and we would like to capture this dependence.
5. This suggests that we create a *conditional prior* of the mean on the unknown variance, with a hyperparameter specifying the mean of the pseudo-observations associated with the prior, and another parameter specifying the number of pseudo-observations. This number serves as a scaling parameter on the variance, making it possible to control the overall variance of the mean relative to the actual variance parameter. The prior for the variance also has two hyperparameters, one specifying the sum of squared deviations of the pseudo-observations associated with the prior, and another specifying once again the number of pseudo-observations. Each of the priors has a hyperparameter specifying the number of pseudo-observations, and in each case this controls the relative variance of that prior. These are given as two separate hyperparameters so that the variance (aka the confidence) of the two priors can be controlled separately.
6. This leads immediately to the normal-inverse-gamma distribution, which is the product of the two distributions just defined, with conjugate priors used (an inverse gamma distribution over the variance, and a normal distribution over the mean, *conditional* on the variance) and with the same four parameters just defined.

The priors are normally defined as follows: ${\begin{aligned}p(\mu \mid \sigma ^{2};\mu _{0},n_{0})&\sim {\mathcal {N}}(\mu _{0},\sigma ^{2}/n_{0})\\p(\sigma ^{2};\nu _{0},\sigma _{0}^{2})&\sim I\chi ^{2}(\nu _{0},\sigma _{0}^{2})=IG(\nu _{0}/2,\nu _{0}\sigma _{0}^{2}/2)\end{aligned}}$

The update equations can be derived, and look as follows: ${\begin{aligned}{\bar {x}}&={\frac {1}{n}}\sum _{i=1}^{n}x_{i}\\\mu _{0}'&={\frac {n_{0}\mu _{0}+n{\bar {x}}}{n_{0}+n}}\\n_{0}'&=n_{0}+n\\\nu _{0}'&=\nu _{0}+n\\\nu _{0}'{\sigma _{0}^{2}}'&=\nu _{0}\sigma _{0}^{2}+\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}+{\frac {n_{0}n}{n_{0}+n}}(\mu _{0}-{\bar {x}})^{2}\end{aligned}}$ The respective numbers of pseudo-observations add the number of actual observations to them. The new mean hyperparameter is once again a weighted average, this time weighted by the relative numbers of observations. Finally, the update for ${\textstyle \nu _{0}'{\sigma _{0}^{2}}'}$ is similar to the case with known mean, but in this case the sum of squared deviations is taken with respect to the observed data mean rather than the true mean, and as a result a new interaction term needs to be added to take care of the additional error source stemming from the deviation between prior and data mean.


## Occurrence and applications

The occurrence of normal distribution in practical problems can be loosely classified into four categories:

1. Exactly normal distributions;
2. Approximately normal laws, for example when such approximation is justified by the central limit theorem; and
3. Distributions modeled as normal – the normal distribution being the distribution with maximum entropy for a given mean and variance.
4. Regression problems – the normal distribution being found after systematic effects have been modeled sufficiently well.

### Exact normality

A normal distribution occurs in some physical theories:

- The velocity distribution of independently moving and perfectly elastic spheres, which is a consequence of Maxwell's Dynamical Theory of Gases, Part I (1860).
- The ground state wave function in position space of the quantum harmonic oscillator.
- The position of a particle that experiences diffusion. If initially the particle is located at a specific point (that is its probability distribution is the Dirac delta function), then after time t its location is described by a normal distribution with variance t, which satisfies the diffusion equation  ${\textstyle {\frac {\partial }{\partial t}}f(x,t)={\frac {1}{2}}{\frac {\partial ^{2}}{\partial x^{2}}}f(x,t)}$ . If the initial location is given by a certain density function ${\textstyle g(x)}$ , then the density at time t is the convolution of g and the normal probability density function.

### Approximate normality

*Approximately* normal distributions occur in many situations, as explained by the central limit theorem. When the outcome is produced by many small effects acting *additively and independently*, its distribution will be close to normal. The normal approximation will not be valid if the effects act multiplicatively (instead of additively), or if there is a single external influence that has a considerably larger magnitude than the rest of the effects.

- In counting problems, where the central limit theorem includes a discrete-to-continuum approximation and where infinitely divisible and decomposable distributions are involved, such as
  - Binomial random variables, associated with binary response variables;
  - Poisson random variables, associated with rare events;
- Thermal radiation has a Bose–Einstein distribution on very short time scales, and a normal distribution on longer timescales due to the central limit theorem.

### Assumed normality

> I can only recognize the occurrence of the normal curve – the Laplacian curve of errors – as a very abnormal phenomenon. It is roughly approximated to in certain distributions; for this reason, and on account for its beautiful simplicity, we may, perhaps, use it as a first approximation, particularly in theoretical investigations.

— Pearson (1901)

There are statistical methods to empirically test that assumption; see the above Normality tests section.

- In biology, the *logarithm* of various variables tend to have a normal distribution, that is, they tend to have a log-normal distribution (after separation on male/female subpopulations), with examples including:
  - Measures of size of living tissue (length, height, skin area, weight);
  - The *length* of *inert* appendages (hair, claws, nails, teeth) of biological specimens, *in the direction of growth*; presumably the thickness of tree bark also falls under this category;
  - Certain physiological measurements, such as blood pressure of adult humans.
- In finance, in particular the Black–Scholes model, changes in the *logarithm* of exchange rates, price indices, and stock market indices are assumed normal (these variables behave like compound interest, not like simple interest, and so are multiplicative). Some mathematicians such as Benoit Mandelbrot have argued that log-Levy distributions, which possess heavy tails, would be a more appropriate model, in particular for the analysis for stock market crashes. The use of the assumption of normal distribution occurring in financial models has also been criticized by Nassim Nicholas Taleb in his works.
- Measurement errors in physical experiments are often modeled by a normal distribution. This use of a normal distribution does not imply that one is assuming the measurement errors are normally distributed, rather using the normal distribution produces the most conservative predictions possible given only knowledge about the mean and variance of the errors.
- In standardized testing, results can be made to have a normal distribution by either selecting the number and difficulty of questions (as in the IQ test) or transforming the raw test scores into output scores by fitting them to the normal distribution. For example, the SAT's traditional range of 200–800 is based on a normal distribution with a mean of 500 and a standard deviation of 100.

- Many scores are derived from the normal distribution, including percentile ranks (percentiles or quantiles), normal curve equivalents, stanines, z-scores, and T-scores. Additionally, some behavioral statistical procedures assume that scores are normally distributed; for example, t-tests and ANOVAs. Bell curve grading assigns relative grades based on a normal distribution of scores.
- In hydrology the distribution of long duration river discharge or rainfall, e.g. monthly and yearly totals, is often thought to be practically normal according to the central limit theorem. The plot on the right illustrates an example of fitting the normal distribution to ranked October rainfalls showing the 90% confidence belt based on the binomial distribution. The rainfall data are represented by plotting positions as part of the cumulative frequency analysis.

### Methodological problems and peer review

John Ioannidis argued that using normally distributed standard deviations as standards for validating research findings leave falsifiable predictions about phenomena that are not normally distributed untested. This includes, for example, phenomena that only appear when all necessary conditions are present and one cannot be a substitute for another in an addition-like way and phenomena that are not randomly distributed. Ioannidis argues that standard deviation-centered validation gives a false appearance of validity to hypotheses and theories where some but not all falsifiable predictions are normally distributed since the portion of falsifiable predictions that there is evidence against may and in some cases are in the non-normally distributed parts of the range of falsifiable predictions, as well as baselessly dismissing hypotheses for which none of the falsifiable predictions are normally distributed as if they were unfalsifiable when in fact they do make falsifiable predictions. It is argued by Ioannidis that many cases of mutually exclusive theories being accepted as validated by research journals are caused by failure of the journals to take in empirical falsifications of non-normally distributed predictions, and not because mutually exclusive theories are true, which they cannot be, although two mutually exclusive theories can both be wrong and a third one correct.


## Computational methods

### Generating values from normal distribution

In computer simulations, especially in applications of the Monte-Carlo method, it is often desirable to generate values that are normally distributed. The algorithms listed below all generate the standard normal deviates, since a *N*(*μ*, *σ*2) can be generated as *X* = *μ* + *σZ*, where Z is standard normal. All these algorithms rely on the availability of a random number generator U capable of producing uniform random variates.

- The most straightforward method is based on the probability integral transform property: if U is distributed uniformly on (0,1), then *Φ*−1(*U*) will have the standard normal distribution. The drawback of this method is that it relies on calculation of the probit function Φ−1, which cannot be done analytically. Some approximate methods are described in Hart (1968) and in the erf article. Wichura gives a fast algorithm for computing this function to 16 decimal places, which is used by R to compute random variates of the normal distribution.
- An easy-to-program approximate approach that relies on the central limit theorem is as follows: generate 12 uniform *U*(0,1) deviates, add them all up, and subtract 6 – the resulting random variable will have approximately standard normal distribution. In truth, the distribution will be Irwin–Hall, which is a 12-section eleventh-order polynomial approximation to the normal distribution. This random deviate will have a limited range of (−6, 6). Note that in a true normal distribution, only 0.00034% of all samples will fall outside ±6*σ*.
- The Box–Muller method uses two independent random numbers U and V distributed uniformly on (0,1). Then the two random variables X and Y $X={\sqrt {-2\ln U}}\,\cos(2\pi V),\qquad Y={\sqrt {-2\ln U}}\,\sin(2\pi V).$ will both have the standard normal distribution, and will be independent. This formulation arises because for a bivariate normal random vector (*X*, *Y*) the squared norm *X*2 + *Y*2 will have the chi-squared distribution with two degrees of freedom, which is an easily generated exponential random variable corresponding to the quantity −2 ln(*U*) in these equations; and the angle is distributed uniformly around the circle, chosen by the random variable V.
- The Marsaglia polar method is a modification of the Box–Muller method which does not require computation of the sine and cosine functions. In this method, U and V are drawn from the uniform (−1,1) distribution, and then *S* = *U*2 + *V*2 is computed. If S is greater or equal to 1, then the method starts over, otherwise the two quantities $X=U{\sqrt {\frac {-2\ln S}{S}}},\qquad Y=V{\sqrt {\frac {-2\ln S}{S}}}$ are returned. Again, X and Y are independent, standard normal random variables.
- The Ratio method is a rejection method. The algorithm proceeds as follows: The two optional steps allow the evaluation of the logarithm in the last step to be avoided in most cases. These steps can be greatly improved so that the logarithm is rarely evaluated.
  - Generate two independent uniform deviates U and V;
  - Compute *X* = √8/*e* (*V* − 0.5)/*U*;
  - Optional: if *X*2 ≤ 5 − 4*e*1/4*U* then accept X and terminate algorithm;
  - Optional: if *X*2 ≥ 4*e*−1.35/*U* + 1.4 then reject X and start over from step 1;
  - If *X*2 ≤ −4 ln *U* then accept X, otherwise start over the algorithm.
- The ziggurat algorithm is faster than the Box–Muller transform and still exact. In about 97% of all cases it uses only two random numbers, one random integer and one random uniform, one multiplication and an if-test. Only in 3% of the cases, where the combination of those two falls outside the "core of the ziggurat" (a kind of rejection sampling using logarithms), do exponentials and more uniform random numbers have to be employed.
- Integer arithmetic can be used to sample from the standard normal distribution. This method is exact in the sense that it satisfies the conditions of *ideal approximation*; i.e., it is equivalent to sampling a real number from the standard normal distribution and rounding this to the nearest representable floating point number.
- There is also some investigation into the connection between the fast Hadamard transform and the normal distribution, since the transform employs just addition and subtraction and by the central limit theorem random numbers from almost any distribution will be transformed into the normal distribution. In this regard a series of Hadamard transforms can be combined with random permutations to turn arbitrary data sets into a normally distributed data.

### Numerical approximations for the normal cumulative distribution function and normal quantile function

The standard normal cumulative distribution function is widely used in scientific and statistical computing.

The values *Φ*(*x*) may be approximated very accurately by a variety of methods, such as numerical integration, Taylor series, asymptotic series and continued fractions. Different approximations are used depending on the desired level of accuracy.

- Zelen & Severo (1964) give the approximation for *Φ*(*x*) for *x* > 0 with the absolute error |*ε*(*x*)| < 7.5·10−8 (algorithm 26.2.17): $\Phi (x)=1-\varphi (x)\left(b_{1}t+b_{2}t^{2}+b_{3}t^{3}+b_{4}t^{4}+b_{5}t^{5}\right)+\varepsilon (x),\qquad t={\frac {1}{1+b_{0}x}},$ where *ϕ*(*x*) is the standard normal probability density function, and *b*0 = 0.2316419, *b*1 = 0.319381530, *b*2 = −0.356563782, *b*3 = 1.781477937, *b*4 = −1.821255978, *b*5 = 1.330274429.
- Hart (1968) lists dozens of approximations by means of rational functions, with or without exponentials, for the erfc() function, where erfc(x) = 1 - erf(x). His algorithms vary in the degree of complexity and the resulting precision, with a maximum absolute precision of 24 digits. An algorithm by West (2009) combines Hart's algorithm 5666 with a continued fraction approximation in the tail to provide a fast computation algorithm with 16-digit precision.
- Cody (1969), after recalling the Hart68 solution is not suited for erf, gave a solution for both erf and erfc, with maximal relative error bound, via Rational Chebyshev Approximation.
- Marsaglia (2004) suggested a simple algorithm based on the Taylor series expansion $\Phi (x)={\frac {1}{2}}+\varphi (x)\left(x+{\frac {x^{3}}{3}}+{\frac {x^{5}}{3\cdot 5}}+{\frac {x^{7}}{3\cdot 5\cdot 7}}+{\frac {x^{9}}{3\cdot 5\cdot 7\cdot 9}}+\cdots \right)$ for calculating *Φ*(*x*) with arbitrary precision. The drawback of this algorithm is comparatively slow calculation time (for example it takes over 300 iterations to calculate the function with 16 digits of precision when *x* = 10).
- The GNU Scientific Library calculates values of the standard normal cumulative distribution function using Hart's algorithms and approximations with Chebyshev polynomials.
- Dia (2023) proposes the following approximation of ${\textstyle 1-\Phi }$ with a maximum relative error less than ${\textstyle 2^{-53}}$ ${\textstyle \left(\approx 1.1\times 10^{-16}\right)}$ in absolute value: for ${\textstyle x\geq 0}$ ${\textstyle {\begin{aligned}1-\Phi \left(x\right)&=\left({\frac {0.39894228040143268}{x+2.92678600515804815}}\right)\left({\frac {x^{2}+8.42742300458043240x+18.38871225773938487}{x^{2}+5.81582518933527391x+8.97280659046817350}}\right)\\&\left({\frac {x^{2}+7.30756258553673541x+18.25323235347346525}{x^{2}+5.70347935898051437x+10.27157061171363079}}\right)\left({\frac {x^{2}+5.66479518878470765x+18.61193318971775795}{x^{2}+5.51862483025707963x+12.72323261907760928}}\right)\\&\left({\frac {x^{2}+4.91396098895240075x+24.14804072812762821}{x^{2}+5.26184239579604207x+16.88639562007936908}}\right)\left({\frac {x^{2}+3.83362947800146179x+11.61511226260603247}{x^{2}+4.92081346632882033x+24.12333774572479110}}\right)e^{-{\frac {x^{2}}{2}}}\end{aligned}}}$ and for ${\textstyle x<0}$ ,

$1-\Phi \left(x\right)=1-\left(1-\Phi \left(-x\right)\right)$

Shore (1982) introduced simple approximations that may be incorporated in stochastic optimization models of engineering and operations research, like reliability engineering and inventory analysis. Denoting *p* = *Φ*(*z*), the simplest approximation for the quantile function is: $z=\Phi ^{-1}(p)=5.5556\left[1-\left({\frac {1-p}{p}}\right)^{0.1186}\right],\qquad p\geq 1/2$

This approximation delivers for z a maximum absolute error of 0.026 (for 0.5 ≤ *p* ≤ 0.9999, corresponding to 0 ≤ *z* ≤ 3.719). For *p* < 1/2 replace p by 1 − *p* and change sign. Another approximation, somewhat less accurate, is the single-parameter approximation: $z=-0.4115\left\{{\frac {1-p}{p}}+\log \left[{\frac {1-p}{p}}\right]-1\right\},\qquad p\geq 1/2$

The latter had served to derive a simple approximation for the loss integral of the normal distribution, defined by ${\begin{aligned}L(z)&=\int _{z}^{\infty }(u-z)\varphi (u)\,du=\int _{z}^{\infty }[1-\Phi (u)]\,du\\[5pt]L(z)&\approx {\begin{cases}0.4115\left({\dfrac {p}{1-p}}\right)-z,&p<1/2,\\\\0.4115\left({\dfrac {1-p}{p}}\right),&p\geq 1/2.\end{cases}}\\[5pt]{\text{or, equivalently,}}\\L(z)&\approx {\begin{cases}0.4115\left\{1-\log \left[{\frac {p}{1-p}}\right]\right\},&p<1/2,\\\\0.4115{\dfrac {1-p}{p}},&p\geq 1/2.\end{cases}}\end{aligned}}$

This approximation is particularly accurate for the right far-tail (maximum error of 10−3 for *z* ≥ 1.4). Highly accurate approximations for the cumulative distribution function, based on Response Modeling Methodology (RMM, Shore, 2011, 2012), are shown in Shore (2005).

Some more approximations can be found at: Error function#Approximation with elementary functions. In particular, small *relative* error on the whole domain for the cumulative distribution function ⁠ $\Phi$ ⁠ and the quantile function ${\textstyle \Phi ^{-1}}$ as well, is achieved via an explicitly invertible formula by Sergei Winitzki in 2008.

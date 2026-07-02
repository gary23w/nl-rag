---
title: "Kolmogorov–Smirnov test"
source: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
domain: nonparametric-tests
license: CC-BY-SA-4.0
tags: nonparametric statistics, rank correlation, sign test, Spearman correlation
fetched: 2026-07-02
---

# Kolmogorov–Smirnov test

In statistics, the **Kolmogorov–Smirnov test** (also **K–S test** or **KS test**) is a nonparametric test of the equality of continuous (or discontinuous, see Section 2.2), one-dimensional probability distributions. It can be used to test whether a sample came from a given reference probability distribution (one-sample K–S test), or to test whether or not two samples came from the same distribution (two-sample K–S test). It is named after Andrey Kolmogorov and Nikolai Smirnov, who developed it in the 1930s.

The Kolmogorov–Smirnov statistic quantifies a distance between the empirical distribution function of the sample and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples. The null distribution of this statistic is calculated under the null hypothesis that the sample is drawn from the reference distribution (in the one-sample case) or that the samples are drawn from the same distribution (in the two-sample case). In the one-sample case, the distribution considered under the null hypothesis may be continuous (see Section 2), purely discrete or mixed (see Section 2.2). In the two-sample case (see Section 3), the distribution considered under the null hypothesis is a continuous distribution but is otherwise unrestricted.

The two-sample K–S test is one of the most useful and general nonparametric methods for comparing two samples, as it is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples.

The Kolmogorov–Smirnov test can be modified to serve as a goodness of fit test. In the special case of testing for normality of the distribution, samples are standardized and compared with a standard normal distribution. This is equivalent to setting the mean and variance of the reference distribution equal to the sample estimates, and it is known that using these to define the specific reference distribution changes the null distribution of the test statistic (see Test with estimated parameters). Various studies have found that, even in this corrected form, the test is less powerful for testing normality than the Shapiro–Wilk test or Anderson–Darling test. However, these other tests have their own disadvantages. For instance, the Shapiro–Wilk test is known not to work well in samples with many identical values.

## One-sample Kolmogorov–Smirnov statistic

The empirical distribution function *F**n* for *n* independent and identically distributed (i.i.d.) ordered observations *Xi* is defined as

$F_{n}(x)={\frac {{\text{number of (elements in the sample}}\leq x)}{n}}={\frac {1}{n}}\sum _{i=1}^{n}1_{(-\infty ,x]}(X_{i}),$ where $1_{(-\infty ,x]}(X_{i})$ is the indicator function, equal to 1 if $X_{i}\leq x$ and equal to 0 otherwise.

The Kolmogorov–Smirnov statistic for a given cumulative distribution function *F*(*x*) is

$D_{n}=\sup _{x}|F_{n}(x)-F(x)|$

where sup*x* is the supremum of the set of distances. Intuitively, the statistic takes the largest absolute difference between the two distribution functions across all *x* values.

By the Glivenko–Cantelli theorem, if the sample comes from the distribution *F*(*x*), then *D**n* converges to 0 almost surely in the limit when n goes to infinity. Kolmogorov strengthened this result, by effectively providing the rate of this convergence (see Kolmogorov distribution). Donsker's theorem provides a yet stronger result.

In practice, the statistic requires a relatively large number of data points (in comparison to other goodness of fit criteria such as the Anderson–Darling test statistic) to properly reject the null hypothesis.

## Kolmogorov distribution

The Kolmogorov distribution is the distribution of the random variable

$K=\sup _{t\in [0,1]}|B(t)|$

where *B*(*t*) is the Brownian bridge. The cumulative distribution function of *K* is given by

${\begin{aligned}\operatorname {Pr} (K\leq x)&=1-2\sum _{k=1}^{\infty }(-1)^{k-1}e^{-2k^{2}x^{2}}\\&={\frac {\sqrt {2\pi }}{x}}\sum _{k=1}^{\infty }e^{-(2k-1)^{2}\pi ^{2}/(8x^{2})},\end{aligned}}$

which can also be expressed by the Jacobi theta function $\vartheta _{01}(z=0;\tau =2ix^{2}/\pi )$ . Both the form of the Kolmogorov–Smirnov test statistic and its asymptotic distribution under the null hypothesis were published by Andrey Kolmogorov, while a table of the distribution was published by Nikolai Smirnov. Recurrence relations for the distribution of the test statistic in finite samples are available.

Under null hypothesis that the sample comes from the hypothesized distribution *F*(*x*),

${\sqrt {n}}D_{n}{\xrightarrow {n\to \infty }}\sup _{t}|B(F(t))|$

in distribution, where *B*(*t*) is the Brownian bridge. If *F* is continuous then under the null hypothesis ${\sqrt {n}}D_{n}$ converges to the Kolmogorov distribution, which does not depend on *F*. This result may also be known as the Kolmogorov theorem.

The accuracy of this limit as an approximation to the exact CDF of K when n is finite is not very impressive: even when $n=1000$ , the corresponding maximum error is about $0.9~\%$ ; this error increases to $2.6~\%$ when $n=100$ and to a totally unacceptable $7~\%$ when $n=10$ . However, a very simple expedient of replacing x by $x+{\frac {1}{6{\sqrt {n}}}}+{\frac {x-1}{4n}}$

in the argument of the Jacobi theta function reduces these errors to $0.003~\%$ , $0.027\%$ , and $0.27~\%$ respectively; such accuracy would be usually considered more than adequate for all practical applications.

The *goodness-of-fit* test or the Kolmogorov–Smirnov test can be constructed by using the critical values of the Kolmogorov distribution. This test is asymptotically valid when $n\to \infty .$ It rejects the null hypothesis at level $\alpha$ if

${\sqrt {n}}D_{n}>K_{\alpha },\,$

where *K**α* is found from

$\operatorname {Pr} (K\leq K_{\alpha })=1-\alpha .\,$

The asymptotic power of this test is 1.

Fast and accurate algorithms to compute the cdf $\operatorname {Pr} (D_{n}\leq x)$ or its complement for arbitrary n and x , are available from:

- and for continuous null distributions with code in C and Java to be found in.
- for purely discrete, mixed or continuous null distribution implemented in the KSgeneral package of the R project for statistical computing, which for a given sample also computes the KS test statistic and its p-value. Alternative C++ implementation is available from.

### Test with estimated parameters

If either the form or the parameters of *F*(*x*) are determined from the data *X**i* the critical values determined in this way are invalid. In such cases, Monte Carlo or other methods may be required, but tables have been prepared for some cases. Details for the required modifications to the test statistic and for the critical values for the normal distribution and the exponential distribution have been published, and later publications also include the Gumbel distribution. The Lilliefors test represents a special case of this for the normal distribution. The logarithm transformation may help to overcome cases where the Kolmogorov test data does not seem to fit the assumption that it came from the normal distribution.

Using estimated parameters, the question arises which estimation method should be used. Usually this would be the maximum likelihood method, but e.g. for the normal distribution MLE has a large bias error on sigma. Using a moment fit or KS minimization instead has a large impact on the critical values, and also some impact on test power. If we need to decide for Student-T data with df = 2 via KS test whether the data could be normal or not, then a ML estimate based on H0 (data is normal, so using the standard deviation for scale) would give much larger KS distance, than a fit with minimum KS. In this case we should reject H0, which is often the case with MLE, because the sample standard deviation might be very large for T-2 data, but with KS minimization we may get still a too low KS to reject H0. In the Student-T case, a modified KS test with KS estimate instead of MLE, makes the KS test indeed slightly worse. However, in other cases, such a modified KS test leads to slightly better test power.

### Discrete and mixed null distribution

Under the assumption that F is non-decreasing and right-continuous, with countable (possibly infinite) number of jumps, the KS test statistic can be expressed as:

$D_{n}=\sup _{x}|F_{n}(x)-F(x)|=\sup _{0\leq t\leq 1}|F_{n}(F^{-1}(t))-F(F^{-1}(t))|.$

From the right-continuity of F , it follows that $F(F^{-1}(t))\geq t$ and $F^{-1}(F(x))\leq x$ and hence, the distribution of $D_{n}$ depends on the null distribution F , i.e., is no longer distribution-free as in the continuous case. Therefore, a fast and accurate method has been developed to compute the exact and asymptotic distribution of $D_{n}$ when F is purely discrete or mixed, implemented in C++ and in the KSgeneral package of the R language. The functions `disc_ks_test()`, `mixed_ks_test()` and `cont_ks_test()` compute also the KS test statistic and p-values for purely discrete, mixed or continuous null distributions and arbitrary sample sizes. The KS test and its p-values for discrete null distributions and small sample sizes are also computed in as part of the dgof package of the R language. Major statistical packages among which SAS `PROC NPAR1WAY`, Stata `ksmirnov` implement the KS test under the assumption that $F(x)$ is continuous, which is more conservative if the null distribution is actually not continuous (see ).

## Two-sample Kolmogorov–Smirnov test

The Kolmogorov–Smirnov test may also be used to test whether two underlying one-dimensional probability distributions differ. In this case, the Kolmogorov–Smirnov statistic is

$D_{n,m}=\sup _{x}|F_{1,n}(x)-F_{2,m}(x)|,$

where $F_{1,n}$ and $F_{2,m}$ are the empirical distribution functions of the first and the second sample respectively, and $\sup$ is the supremum function.

For large samples, the null hypothesis is rejected at level $\alpha$ if

$D_{n,m}>c(\alpha ){\sqrt {\frac {n+m}{n\cdot m}}}.$

Where n and m are the sizes of first and second sample respectively. The value of $c({\alpha })$ is given in the table below for the most common levels of $\alpha$

$\alpha$

0.20

0.15

0.10

0.05

0.025

0.01

0.005

0.001

$c({\alpha })$

1.073

1.138

1.224

1.358

1.48

1.628

1.731

1.949

and in general by

$c\left(\alpha \right)={\sqrt {-\ln \left({\tfrac {\alpha }{2}}\right)\cdot {\tfrac {1}{2}}}},$

so that the condition reads

$D_{n,m}>{\sqrt {-\ln \left({\tfrac {\alpha }{2}}\right)\cdot {\frac {n+m}{2n\cdot m}}}}.$

Here, again, the larger the sample sizes, the more sensitive the minimal bound: For a given ratio of sample sizes (e.g. $m=n$ ), the minimal bound scales in the size of either of the samples according to its inverse square root.

Note that the two-sample test checks whether the two data samples come from the same distribution. This does not specify what that common distribution is (e.g. whether it's normal or not normal). Again, tables of critical values have been published. A shortcoming of the univariate Kolmogorov–Smirnov test is that it is not very powerful because it is devised to be sensitive against all possible types of differences between two distribution functions. Some argue that the Cucconi test, originally proposed for simultaneously comparing location and scale, can be much more powerful than the Kolmogorov–Smirnov test when comparing two distribution functions.

Two-sample KS tests have been applied in economics to detect asymmetric effects and to study natural experiments.

## Setting confidence limits for the shape of a distribution function

While the Kolmogorov–Smirnov test is usually used to test whether a given *F*(*x*) is the underlying probability distribution of *F**n*(*x*), the procedure may be inverted to give confidence limits on *F*(*x*) itself. If one chooses a critical value of the test statistic *D**α* such that P(*D**n* > *D**α*) = *α*, then a band of width ±*D**α* around *F**n*(*x*) will entirely contain *F*(*x*) with probability 1 − *α*.

## The Kolmogorov–Smirnov statistic in more than one dimension

A distribution-free multivariate Kolmogorov–Smirnov goodness of fit test has been proposed by Justel, Peña and Zamar (1997). The test uses a statistic which is built using Rosenblatt's transformation, and an algorithm is developed to compute it in the bivariate case. An approximate test that can be easily computed in any dimension is also presented.

The Kolmogorov–Smirnov test statistic needs to be modified if a similar test is to be applied to multivariate data. This is not straightforward because the maximum difference between two joint cumulative distribution functions is not generally the same as the maximum difference of any of the complementary distribution functions. Thus the maximum difference will differ depending on which of $\Pr(X<x\land Y<y)$ or $\Pr(X<x\land Y>y)$ or any of the other two possible arrangements is used. One might require that the result of the test used should not depend on which choice is made.

One approach to generalizing the Kolmogorov–Smirnov statistic to higher dimensions which meets the above concern is to compare the cdfs of the two samples with all possible orderings, and take the largest of the set of resulting KS statistics. In *d* dimensions, there are 2*d* − 1 such orderings. One such variation is due to Peacock (see also Gosset for a 3D version) and another to Fasano and Franceschini (see Lopes et al. for a comparison and computational details). Critical values for the test statistic can be obtained by simulations, but depend on the dependence structure in the joint distribution.

## Implementations

The Kolmogorov–Smirnov test is implemented in many software programs. Most of these implement both the one and two sampled test.

- Mathematica has KolmogorovSmirnovTest.
- MATLAB's Statistics Toolbox has kstest and kstest2 for one-sample and two-sample Kolmogorov–Smirnov tests, respectively.
- The R package "KSgeneral" computes the KS test statistics and its p-values under arbitrary, possibly discrete, mixed or continuous null distribution.
- R's statistics base-package implements the test as ks.test {stats} in its "stats" package.
- SAS implements the test in its PROC NPAR1WAY procedure.
- In Python, the SciPy package implements the test in the scipy.stats.kstest function.
- SYSTAT (SPSS Inc., Chicago, IL)
- Java has an implementation of this test provided by Apache Commons.
- KNIME has a node implementing this test based on the above Java implementation.
- Julia has the package HypothesisTests.jl with the function ExactOneSampleKSTest(x::AbstractVector{<:Real}, d::UnivariateDistribution).
- StatsDirect (StatsDirect Ltd, Manchester, UK) implements all common variants.
- Stata (Stata Corporation, College Station, TX) implements the test in ksmirnov (Kolmogorov–Smirnov equality-of-distributions test) command.
- PSPP implements the test in its KOLMOGOROV-SMIRNOV (or using KS shortcut function).
- The Real Statistics Resource Pack for Excel runs the test as KSCRIT and KSPROB.
- ClickHouse implements the test in its kolmogorovSmirnovTest function.

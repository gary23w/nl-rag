---
title: "Median"
source: https://en.wikipedia.org/wiki/Median
domain: quantile-regression
license: CC-BY-SA-4.0
tags: quantile regression, conditional quantile, least absolute deviations, percentile estimation
fetched: 2026-07-02
---

# Median

The **median** of a set of numbers is the value separating the higher half from the lower half of a data sample, a population, or a probability distribution. For a data set, it may be thought of as the "middle" value. The basic feature of the median in describing data compared to the mean (often simply described as the "average") is that it is not skewed by a small proportion of extreme values, and therefore provides a better representation of the center. Median income, for example, may be a better way to describe the center of the income distribution because increases in the largest incomes alone have no effect on the median. For this reason, the median is of central importance in robust statistics. Median is a 2-quantile; it is the value that partitions a set into two equal parts.

## Finite set of numbers

The median of a finite list of numbers is the middle number when the numbers are arranged in order from smallest to greatest.

If the data set has an odd number of observations, the middle one is selected (after arranging in ascending order). For example, the following list of seven numbers,

1, 3, 3,

6

, 7, 8, 9

has the median of *6*, which is the fourth value.

If the data set has an even number of observations, there is no distinct middle value and the median is usually defined to be the arithmetic mean of the two middle values. For example, this data set of 8 numbers

1, 2, 3,

4, 5

, 6, 8, 9

has a median value of *4.5*, that is $(4+5)/2$ . (In more technical terms, this interprets the median as the fully trimmed mid-range).

In general, with this convention, the median can be defined as follows: For a data set x of n elements, ordered from smallest to greatest,

if

n

is odd,

$\operatorname {med} (x)=x_{(n+1)/2}$

if

n

is even,

$\operatorname {med} (x)={\frac {x_{(n/2)}+x_{((n/2)+1)}}{2}}$

| Type | Description | Example | Result |
|---|---|---|---|
| Midrange | Midway point between the minimum and the maximum of a data set | **1**, 2, 2, 3, 4, 7, **9** | **5** |
| Arithmetic mean | Sum of values of a data set divided by number of values: ${\textstyle {\bar {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}}$ | (1 + 2 + 2 + 3 + 4 + 7 + 9) / 7 | **4** |
| Median | Middle value separating the greater and lesser halves of a data set | 1, 2, 2, **3**, 4, 7, 9 | **3** |
| Mode | Most frequent value in a data set | 1, **2**, **2**, 3, 4, 7, 9 | **2** |

## Definition and notation

Formally, a median of a population is any value such that at least half of the population is less than or equal to the proposed median and at least half is greater than or equal to the proposed median. As seen above, medians may not be unique. If each set contains more than half the population, then some of the population is exactly equal to the unique median.

The median is well-defined for any ordered (one-dimensional) data and is independent of any distance metric. The median can thus be applied to student grades that are ranked but not numerical (e.g. working out a median grade when student test scores are graded from F to A). The result might be halfway between grades if there is an even number of students; for an odd number students, one specific grade is determined as the median.

A geometric median, on the other hand, is defined in any number of dimensions. A related concept, in which the outcome is forced to correspond to a member of the sample, is the medoid.

There is no widely accepted standard notation for the median, but some authors represent the median of a variable *x* as med(*x*), *x͂*, as *μ*1/2, or as *M*. In any of these cases, the use of these or other symbols for the median needs to be explicitly defined when they are introduced.

The median is a special case of other ways of summarizing the typical values associated with a statistical distribution: it is the 2nd quartile, 5th decile, and 50th percentile.

## Uses

The median can be used as a measure of location when one attaches reduced importance to extreme values, typically because a distribution is skewed, extreme values are not known, or outliers are untrustworthy, i.e., may be measurement or transcription errors.

For example, consider the multiset

1, 2, 2, 2, 3, 14.

The median is 2 in this case, as is the mode, and it might be seen as a better indication of the center than the arithmetic mean of 4, which is larger than all but one of the values. However, the widely cited empirical relationship that the mean is shifted "further into the tail" of a distribution than the median is not generally true. At most, one can say that the two statistics cannot be "too far" apart; see § Inequality relating means and medians below.

As a median is based on the middle data in a set, it is not necessary to know the value of extreme results in order to calculate it. For example, in a psychology test investigating the time needed to solve a problem, if a small number of people failed to solve the problem at all in the given time a median can still be calculated.

Because the median is simple to understand and easy to calculate, while also a robust approximation to the mean, the median is a popular summary statistic in descriptive statistics. In this context, there are several choices for a measure of variability: the range, the interquartile range, the mean absolute deviation, and the median absolute deviation.

For practical purposes, different measures of location and dispersion are often compared on the basis of how well the corresponding population values can be estimated from a sample of data. The median, estimated using the sample median, has good properties in this regard. While it is not usually optimal if a given population distribution is assumed, its properties are always reasonably good. For example, a comparison of the efficiency of candidate estimators shows that the sample mean is more statistically efficient when—and only when— data is uncontaminated by data from heavy-tailed distributions or from mixtures of distributions. Even then, the median has a 64% efficiency compared to the minimum-variance mean (for large normal samples), which is to say the variance of the median will be ~50% greater than the variance of the mean.

## Probability distributions

A median of a real-valued random variable X is a real number m that satisfies $\operatorname {P} (X<m)\leq {\frac {1}{2}}\quad {\text{and}}\quad \operatorname {P} (X>m)\leq {\frac {1}{2}}$ or, equivalently with the complementary events, $\operatorname {P} (X\geq m)\geq {\frac {1}{2}}\quad {\text{and}}\quad \operatorname {P} (X\leq m)\geq {\frac {1}{2}}\,.$ Such an m always exists, but needs not be uniquely determined. An equivalent phrasing uses the cumulative distribution function $F\colon \,\mathbb {R} \to \mathbb {R}$ of $X\colon$ $\lim _{x\to m-}F(x)\leq {\frac {1}{2}}\leq F(m)$ (cf. the drawing in the definition of expected value for arbitrary real-valued random variables).

Note that this definition does not require *X* to have an absolutely continuous distribution (which has a probability density function *f*), nor does it require a discrete one. In the former case, the inequalities can be upgraded to equality: a median satisfies $\operatorname {P} (X\leq m)=\int _{-\infty }^{m}{f(x)\,dx}={\frac {1}{2}}$ and $\operatorname {P} (X\geq m)=\int _{m}^{\infty }{f(x)\,dx}={\frac {1}{2}}\,.$

Any probability distribution on the real number set $\mathbb {R}$ has at least one median, but in pathological cases there may be more than one median: if *F* is constant 1/2 on an interval (so that *f* = 0 there), then any value of that interval is a median.

### Medians of particular distributions

The medians of certain types of distributions can be easily calculated from their parameters; furthermore, they exist even for some distributions lacking a well-defined mean, such as the Cauchy distribution:

- The median of a symmetric unimodal distribution coincides with the mode.
- The median of a symmetric distribution which possesses a mean *μ* also takes the value *μ*.
  - The median of a normal distribution with mean *μ* and variance *σ*2 is μ. In fact, for a normal distribution, mean = median = mode.
  - The median of a uniform distribution in the interval [*a*, *b*] is (*a* + *b*) / 2, which is also the mean.
- The median of a Cauchy distribution with location parameter *x*0 and scale parameter *y* is *x*0, the location parameter.
- The median of a power law distribution *x*−*a*, with exponent *a* > 1 is 21/(*a* − 1)*x*min, where *x*min is the minimum value for which the power law holds.
- The median of an exponential distribution with rate parameter *λ* is the natural logarithm of 2 divided by the rate parameter: *λ*−1ln 2.
- The median of a Weibull distribution with shape parameter *k* and scale parameter *λ* is *λ*(ln 2)1/*k*.

## Properties

### Optimality property

The *mean absolute error* of a real variable *m* with respect to the random variable *X* is $\operatorname {E} \left[\left|X-m\right|\right]$ Provided that the probability distribution of *X* is such that the above expectation exists, then *m* is a median of *X* if and only if *m* is a minimizer of the mean absolute error with respect to *X*. In particular, if *m* is a sample median, then it minimizes the arithmetic mean of the absolute deviations. Note, however, that in cases where the sample contains an even number of elements, this minimizer is not unique.

This optimization-based definition of the median is useful in statistical data-analysis, for example, in *k*-medians clustering.

### Inequality relating means and medians

If the distribution has finite variance, then the distance between the median ${\tilde {X}}$ and the mean ${\bar {X}}$ is bounded by one standard deviation.

This bound was proved by Book and Sher in 1979 for discrete samples, and more generally by Page and Murty in 1982. In a comment on a subsequent proof by O'Cinneide, Mallows in 1991 presented a compact proof that uses Jensen's inequality twice, as follows. Using |·| for the absolute value, we have

${\begin{aligned}\left|\mu -m\right|=\left|\operatorname {E} (X-m)\right|&\leq \operatorname {E} \left(\left|X-m\right|\right)\\[2ex]&\leq \operatorname {E} \left(\left|X-\mu \right|\right)\\[1ex]&\leq {\sqrt {\operatorname {E} \left({\left(X-\mu \right)}^{2}\right)}}=\sigma .\end{aligned}}$

The first and third inequalities come from Jensen's inequality applied to the absolute-value function and the square function, which are each convex. The second inequality comes from the fact that a median minimizes the absolute deviation function $a\mapsto \operatorname {E} [|X-a|]$ .

Mallows's proof can be generalized to obtain a multivariate version of the inequality simply by replacing the absolute value with a norm: $\left\|\mu -m\right\|\leq {\sqrt {\operatorname {E} \left({\left\|X-\mu \right\|}^{2}\right)}}={\sqrt {\operatorname {trace} \left(\operatorname {var} (X)\right)}}$

where *m* is a spatial median, that is, a minimizer of the function $a\mapsto \operatorname {E} (\|X-a\|).\,$ The spatial median is unique when the data-set's dimension is two or more.

An alternative proof uses the one-sided Chebyshev inequality; it appears in an inequality on location and scale parameters. This formula also follows directly from Cantelli's inequality.

#### Unimodal distributions

For the case of unimodal distributions, one can achieve a sharper bound on the distance between the median and the mean:

$\left|{\tilde {X}}-{\bar {X}}\right|\leq \left({\frac {3}{5}}\right)^{1/2}\sigma \approx 0.7746\sigma .$

A similar relation holds between the median and the mode:

$\left|{\tilde {X}}-\mathrm {mode} \right|\leq 3^{1/2}\sigma \approx 1.732\sigma .$

### Mean, median, and skew

A typical heuristic is that positively skewed distributions have mean > median. This is true for all members of the Pearson distribution family. However this is not always true. For example, the Weibull distribution family has members with positive mean, but mean < median. Violations of the rule are particularly common for discrete distributions. For example, any Poisson distribution has positive skew, but its mean < median whenever $\mu {\bmod {1}}>\ln 2$ . See for a proof sketch.

When the distribution has a monotonically decreasing probability density, the median is less than the mean, as shown in the figure.

## Jensen's inequality for medians

Jensen's inequality states that for any random variable *X* with a finite expectation *E*[*X*] and for any convex function *f*

$f(\operatorname {E} (x))\leq \operatorname {E} (f(x))$

This inequality generalizes to the median as well. We say a function *f*: **R** → **R** is a **C function** if, for any *t*,

$f^{-1}\left(\,(-\infty ,t]\,\right)=\{x\in \mathbb {R} \mid f(x)\leq t\}$ is a closed interval (allowing the degenerate cases of a single point or an empty set). Every convex function is a C function, but the reverse does not hold. If *f* is a C function, then

$f(\operatorname {med} [X])\leq \operatorname {med} [f(X)]$

If the medians are not unique, the statement holds for the corresponding suprema.

## Medians for samples

### Efficient computation of the sample median

Even though comparison-sorting *n* items requires Ω(*n* log *n*) operations, selection algorithms can compute the kth-smallest of n items with only Θ(*n*) operations. This includes the median, which is the ⁠*n*/2⁠th order statistic (or for an even number of samples, the arithmetic mean of the two middle order statistics).

Selection algorithms still have the downside of requiring Ω(*n*) memory, that is, they need to have the full sample (or a linear-sized portion of it) in memory. Because this, as well as the linear time requirement, can be prohibitive, several estimation procedures for the median have been developed. A simple one is the median of three rule, which estimates the median as the median of a three-element subsample; this is commonly used as a subroutine in the quicksort sorting algorithm, which uses an estimate of its input's median. A more robust estimator is Tukey's *ninther*, which is the median of three rule applied with limited recursion: if A is the sample laid out as an array, and

med3(

A

) = med(

A

[1],

A

[

⁠

n

/

2

⁠

],

A

[

n

])

,

then

ninther(

A

) = med(med3(

A

[1 ...

⁠

1

/

3

⁠

n

]), med3(

A

[

⁠

1

/

3

⁠

n

...

⁠

2

/

3

⁠

n

]), med3(

A

[

⁠

2

/

3

⁠

n

...

n

]))

The *remedian* is an estimator for the median that requires linear time but sub-linear memory, operating in a single pass over the sample.

### Sampling distribution

The distributions of both the sample mean and the sample median were determined by Laplace. The distribution of the sample median from a population with a density function $f(x)$ is asymptotically normal with mean m and variance

${\frac {1}{4nf(m)^{2}}}$

where m is the median of $f(x)$ and n is the sample size:

${\text{Sample median}}\sim {\mathcal {N}}{\left(\mu {=}m,\,\sigma ^{2}{=}{\frac {1}{4nf(m)^{2}}}\right)}$

A modern proof follows below. Laplace's result is now understood as a special case of the asymptotic distribution of arbitrary quantiles.

For normal samples, the density is $f(m)=1/{\sqrt {2\pi \sigma ^{2}}}$ , thus for large samples the variance of the median equals $({\pi }/{2})\cdot (\sigma ^{2}/n).$ (See also section #Efficiency below.)

#### Derivation of the asymptotic distribution

We take the sample size to be an odd number $N=2n+1$ and assume our variable continuous; the formula for the case of discrete variables is given below in § Empirical local density. The sample can be summarized as "below median", "at median", and "above median", which corresponds to a trinomial distribution with probabilities $F(v)$ , $f(v)$ and $1-F(v)$ . For a continuous variable, the probability of multiple sample values being exactly equal to the median is 0, so one can calculate the density of at the point v directly from the trinomial distribution:

$\Pr[\operatorname {med} =v]\,dv={\frac {(2n+1)!}{n!n!}}F(v)^{n}(1-F(v))^{n}f(v)\,dv.$

Now we introduce the beta function. For integer arguments $\alpha$ and $\beta$ , this can be expressed as $\mathrm {B} (\alpha ,\beta )={\frac {(\alpha -1)!(\beta -1)!}{(\alpha +\beta -1)!}}$ . Also, recall that $f(v)\,dv=dF(v)$ . Using these relationships and setting both $\alpha$ and $\beta$ equal to $n+1$ allows the last expression to be written as

${\frac {F(v)^{n}(1-F(v))^{n}}{\mathrm {B} (n+1,n+1)}}\,dF(v)$

Hence the density function of the median is a symmetric beta distribution pushed forward by F . Its mean, as we would expect, is 0.5 and its variance is $1/(4(N+2))$ . By the chain rule, the corresponding variance of the sample median is

${\frac {1}{4(N+2)f(m)^{2}}}.$

The additional 2 is negligible in the limit.

##### Empirical local density

In practice, the functions f and F above are often not known or assumed. However, they can be estimated from an observed frequency distribution. In this section, we give an example. Consider the following table, representing a sample of 3,800 (discrete-valued) observations:

v

0

0.5

1

1.5

2

2.5

3

3.5

4

4.5

5

f

(

v

)

0.000

0.008

0.010

0.013

0.083

0.108

0.328

0.220

0.202

0.023

0.005

F

(

v

)

0.000

0.008

0.018

0.031

0.114

0.222

0.550

0.770

0.972

0.995

1.000

Because the observations are discrete-valued, constructing the exact distribution of the median is not an immediate translation of the above expression for $\Pr(\operatorname {med} =v)$ ; one may (and typically does) have multiple instances of the median in one's sample. So we must sum over all these possibilities:

$\Pr(\operatorname {med} =v)=\sum _{i=0}^{n}\sum _{k=0}^{n}{\frac {N!}{i!(N-i-k)!k!}}F(v-1)^{i}(1-F(v))^{k}f(v)^{N-i-k}$

Here, *i* is the number of points strictly less than the median and *k* the number strictly greater.

Using these preliminaries, it is possible to investigate the effect of sample size on the standard errors of the mean and median. The observed mean is 3.16, the observed raw median is 3 and the observed interpolated median is 3.174. The following table gives some comparison statistics.

| Sample sizeStatistic | 3 | 9 | 15 | 21 |
|---|---|---|---|---|
| Expected value of median | 3.198 | 3.191 | 3.174 | 3.161 |
| Standard error of median (above formula) | 0.482 | 0.305 | 0.257 | 0.239 |
| Standard error of median (asymptotic approximation) | 0.879 | 0.508 | 0.393 | 0.332 |
| Standard error of mean | 0.421 | 0.243 | 0.188 | 0.159 |

The expected value of the median falls slightly as sample size increases while, as would be expected, the standard errors of both the median and the mean are proportionate to the inverse square root of the sample size. The asymptotic approximation errs on the side of caution by overestimating the standard error.

### Estimation of variance from sample data

The value of $(2f(x))^{-2}$ —the asymptotic value of $n^{-1/2}(\nu -m)$ where $\nu$ is the population median—has been studied by several authors. The standard "delete one" jackknife method produces inconsistent results. An alternative—the "delete k" method—where k grows with the sample size has been shown to be asymptotically consistent. This method may be computationally expensive for large data sets. A bootstrap estimate is known to be consistent, but converges very slowly (order of $n^{-{\frac {1}{4}}}$ ). Other methods have been proposed but their behavior may differ between large and small samples.

### Efficiency

The efficiency of the sample median, measured as the ratio of the variance of the mean to the variance of the median, depends on the sample size and on the underlying population distribution. For a sample of size $N=2n+1$ from the normal distribution, the efficiency for large N is

${\frac {2}{\pi }}{\frac {N+2}{N}}$

The efficiency tends to ${\frac {2}{\pi }}$ as N tends to infinity.

In other words, the relative variance of the median will be $\pi /2\approx 1.57$ , or 57% greater than the variance of the mean – the relative standard error of the median will be $(\pi /2)^{\frac {1}{2}}\approx 1.25$ , or 25% greater than the standard error of the mean, $\sigma /{\sqrt {n}}$ (see also section #Sampling distribution above.).

### Other estimators

For univariate distributions that are *symmetric* about one median, the Hodges–Lehmann estimator is a robust and highly efficient estimator of the population median.

If data is represented by a statistical model specifying a particular family of probability distributions, then estimates of the median can be obtained by fitting that family of probability distributions to the data and calculating the theoretical median of the fitted distribution. Pareto interpolation is an application of this when the population is assumed to have a Pareto distribution.

## Multivariate median

Previously, this article discussed the univariate median, when the sample or population had one-dimension. When the dimension is two or higher, there are multiple concepts that extend the definition of the univariate median; each such multivariate median agrees with the univariate median when the dimension is exactly one.

### Marginal median

The marginal median is defined for vectors defined with respect to a fixed set of coordinates. A marginal median is defined to be the vector whose components are univariate medians. The marginal median is easy to compute, and its properties were studied by Puri and Sen.

### Geometric median

The geometric median of a discrete set of sample points $x_{1},\ldots x_{N}$ in a Euclidean space is the point minimizing the sum of distances to the sample points.

${\hat {\mu }}={\underset {\mu \in \mathbb {R} ^{m}}{\operatorname {arg\,min} }}\sum _{n=1}^{N}\left\|\mu -x_{n}\right\|_{2}$

In contrast to the marginal median, the geometric median is equivariant with respect to Euclidean similarity transformations such as translations and rotations.

### Median in all directions

If the marginal medians for all coordinate systems coincide, then their common location may be termed the "median in all directions". This concept is relevant to voting theory on account of the median voter theorem. When it exists, the median in all directions coincides with the geometric median (at least for discrete distributions).

### Centerpoint

In statistics and computational geometry, the notion of centerpoint is a generalization of the median to data in higher-dimensional Euclidean space. Given a set of points in *d*-dimensional space, a centerpoint of the set is a point such that any hyperplane that goes through that point divides the set of points in two roughly equal subsets: the smaller part should have at least a 1/(*d* + 1) fraction of the points. Like the median, a centerpoint need not be one of the data points. Every non-empty set of points (with no duplicates) has at least one centerpoint.

## Conditional median

The conditional median occurs in the setting where we seek to estimate a random variable X from a random variable Y , which is a noisy version of X . The conditional median in this setting is given by

$m(X|Y=y)=F_{X|Y=y}^{-1}\left({\frac {1}{2}}\right)$ where $t\mapsto F_{X|Y=y}^{-1}(t)$ is the inverse of the conditional cdf (i.e., conditional quantile function) of $x\mapsto F_{X|Y}(x|y)$ . For example, a popular model is $Y=X+Z$ where Z is standard normal independent of X . The conditional median is the optimal Bayesian $L_{1}$ estimator:

$m(X|Y=y)=\arg \min _{f}\operatorname {E} \left[|X-f(Y)|\right]$

It is known that for the model $Y=X+Z$ where Z is standard normal independent of X , the estimator is linear if and only if X is Gaussian.

### Interpolated median

When dealing with a discrete variable, it is sometimes useful to regard the observed values as being midpoints of underlying continuous intervals. An example of this is a Likert scale, on which opinions or preferences are expressed on a scale with a set number of possible responses. If the scale consists of the positive integers, an observation of 3 might be regarded as representing the interval from 2.50 to 3.50. It is possible to estimate the median of the underlying variable. If, say, 22% of the observations are of value 2 or below and 55.0% are of 3 or below (so 33% have the value 3), then the median m is 3 since the median is the smallest value of x for which $F(x)$ is greater than a half. But the interpolated median is somewhere between 2.50 and 3.50. First we add half of the interval width w to the median to get the upper bound of the median interval. Then we subtract that proportion of the interval width which equals the proportion of the 33% which lies above the 50% mark. In other words, we split up the interval width pro rata to the numbers of observations. In this case, the 33% is split into 28% below the median and 5% above it so we subtract 5/33 of the interval width from the upper bound of 3.50 to give an interpolated median of 3.35. More formally, if the values $f(x)$ are known, the interpolated median can be calculated from

$m_{\text{int}}=m+w\left[{\frac {1}{2}}-{\frac {F(m)-{\frac {1}{2}}}{f(m)}}\right].$

Alternatively, if in an observed sample there are k scores above the median category, j scores in it and i scores below it then the interpolated median is given by

$m_{\text{int}}=m+{\frac {w}{2}}\left[{\frac {k-i}{j}}\right].$

### Pseudo-median

For univariate distributions that are *symmetric* about one median, the Hodges–Lehmann estimator is a robust and highly efficient estimator of the population median; for non-symmetric distributions, the Hodges–Lehmann estimator is a robust and highly efficient estimator of the population *pseudo-median*, which is the median of a symmetrized distribution and which is close to the population median. The Hodges–Lehmann estimator has been generalized to multivariate distributions.

### Variants of regression

The Theil–Sen estimator is a method for robust linear regression based on finding medians of slopes.

### Median filter

The median filter is an important tool of image processing, that can effectively remove any salt-and-pepper noise from grayscale images.

### Cluster analysis

In cluster analysis, the k-medians clustering algorithm provides a way of defining clusters, in which the criterion of maximising the distance between cluster-means that is used in k-means clustering, is replaced by maximising the distance between cluster-medians.

### Median–median line

This is a method of robust regression. The idea dates back to Wald in 1940 who suggested dividing a set of bivariate data into two halves depending on the value of the independent parameter x : a left half with values less than the median and a right half with values greater than the median. He suggested taking the means of the dependent y and independent x variables of the left and the right halves and estimating the slope of the line joining these two points. The line could then be adjusted to fit the majority of the points in the data set.

Nair and Shrivastava in 1942 suggested a similar idea but instead advocated dividing the sample into three equal parts before calculating the means of the subsamples. Brown and Mood in 1951 proposed the idea of using the medians of two subsamples rather the means. Tukey combined these ideas and recommended dividing the sample into three equal size subsamples and estimating the line based on the medians of the subsamples.

## Median-unbiased estimators

Any *mean*-unbiased estimator minimizes the risk (expected loss) with respect to the squared-error loss function, as observed by Gauss. A *median*-unbiased estimator minimizes the risk with respect to the absolute-deviation loss function, as observed by Laplace. Other loss functions are used in statistical theory, particularly in robust statistics.

The theory of median-unbiased estimators was revived by George W. Brown in 1947:

> An estimate of a one-dimensional parameter θ will be said to be median-unbiased if, for fixed θ, the median of the distribution of the estimate is at the value θ; i.e., the estimate underestimates just as often as it overestimates. This requirement seems for most purposes to accomplish as much as the mean-unbiased requirement and has the additional property that it is invariant under one-to-one transformation.

— page 584

Further properties of median-unbiased estimators have been reported.

There are methods of constructing median-unbiased estimators that are optimal (in a sense analogous to the minimum-variance property for mean-unbiased estimators). Such constructions exist for probability distributions having monotone likelihood-functions. One such procedure is an analogue of the Rao–Blackwell procedure for mean-unbiased estimators: The procedure holds for a smaller class of probability distributions than does the Rao—Blackwell procedure but for a larger class of loss functions.

## History

Scientific researchers in the ancient near east appear not to have used summary statistics altogether, instead choosing values that offered maximal consistency with a broader theory that integrated a wide variety of phenomena. Within the Mediterranean (and, later, European) scholarly community, statistics like the mean are fundamentally a medieval and early modern development. (The history of the median outside Europe and its predecessors remains relatively unstudied.)

The idea of the median appeared in the 6th century in the Talmud, in order to fairly analyze divergent appraisals. However, the concept did not spread to the broader scientific community.

Instead, the closest ancestor of the modern median is the mid-range, invented by Al-Biruni Transmission of his work to later scholars is unclear. He applied his technique to assaying currency metals, but, after he published his work, most assayers still adopted the most unfavorable value from their results, lest they appear to cheat. However, increased navigation at sea during the Age of Discovery meant that ship's navigators increasingly had to attempt to determine latitude in unfavorable weather against hostile shores, leading to renewed interest in summary statistics. Whether rediscovered or independently invented, the mid-range is recommended to nautical navigators in Harriot's "Instructions for Raleigh's Voyage to Guiana, 1595".

The idea of the median may have first appeared in Edward Wright's 1599 book *Certaine Errors in Navigation* on a section about compass navigation. Wright was reluctant to discard measured values, and may have felt that the median — incorporating a greater proportion of the dataset than the mid-range — was more likely to be correct. However, Wright did not give examples of his technique's use, making it hard to verify that he described the modern notion of median. The median (in the context of probability) certainly appeared in the correspondence of Christiaan Huygens, but as an example of a statistic that was inappropriate for actuarial practice.

The earliest recommendation of the median dates to 1757, when Roger Joseph Boscovich developed a regression method based on the *L*1 norm and therefore implicitly on the median. In 1774, Laplace made this desire explicit: he suggested the median be used as the standard estimator of the value of a posterior PDF. The specific criterion was to minimize the expected magnitude of the error; $|\alpha -\alpha ^{*}|$ where $\alpha ^{*}$ is the estimate and $\alpha$ is the true value. To this end, Laplace determined the distributions of both the sample mean and the sample median in the early 1800s. However, a decade later, Gauss and Legendre developed the least squares method, which minimizes $(\alpha -\alpha ^{*})^{2}$ to obtain the mean; the strong justification of this estimator by reference to maximum likelihood estimation based on a normal distribution means it has mostly replaced Laplace's original suggestion.

Antoine Augustin Cournot in 1843 was the first to use the term *median* (*valeur médiane*) for the value that divides a probability distribution into two equal halves. Gustav Theodor Fechner used the median (*Centralwerth*) in sociological and psychological phenomena. It had earlier been used only in astronomy and related fields. Gustav Fechner popularized the median into the formal analysis of data, although it had been used previously by Laplace, and the median appeared in a textbook by F. Y. Edgeworth. Francis Galton used the term *median* in 1881, having earlier used the terms *middle-most value* in 1869, and the *medium* in 1880.

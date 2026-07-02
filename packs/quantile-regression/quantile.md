---
title: "Quantile"
source: https://en.wikipedia.org/wiki/Quantile
domain: quantile-regression
license: CC-BY-SA-4.0
tags: quantile regression, conditional quantile, least absolute deviations, percentile estimation
fetched: 2026-07-02
---

# Quantile

In statistics and probability, **quantiles** are cut points dividing the range of a probability distribution into continuous intervals with equal probabilities or dividing the observations in a sample in the same way. Common quantiles have special names, such as *quartiles* (four groups), *deciles* (ten groups), and *percentiles* (100 groups). The groups created are termed halves, thirds, quarters, etc., though more often the terms for the quantile are used for the groups created, rather than for the cut points.

**q**-**quantiles** are values that partition a finite set of values into q subsets of (nearly) equal sizes. There are *q* − 1 subsets of the q-quantiles, one for each integer k satisfying 0 < *k* < *q*. In some cases the value of a quantile may not be uniquely determined, as can be the case for the median (2-quantile) of a uniform probability distribution on a set of even size. Quantiles can also be applied to continuous distributions, providing a way to generalize rank statistics to continuous variables (see percentile rank). When the cumulative distribution function of a random variable is known, the q-quantiles are the application of the*quantile function* (the inverse function of the cumulative distribution function) to the values {1/*q*, 2/*q*, …, (*q* − 1)/*q*}.

## Quantiles of a population

As in the computation of, for example, standard deviation, the estimation of a quantile depends upon whether one is operating with a statistical population or with a sample drawn from it. For a population, of discrete values or for a continuous population density, the k-th q-quantile is the data value where the cumulative distribution function crosses *k*/*q*. That is, x is a k-th q-quantile for a variable X if

Pr[

X

<

x

] ≤

k

/

q

or, equivalently,

Pr[

X

≥

x

] ≥ 1 −

k

/

q

and

Pr[

X

≤

x

] ≥

k

/

q

where Pr is the probability function. For a finite population of N equally probable values indexed 1, …, *N* from lowest to highest, the k-th q-quantile of this population can equivalently be computed via the value of Ip = *N* *k*/*q*. If Ip is not an integer, then round up to the next integer to get the appropriate index; the corresponding data value is the k-th q-quantile. On the other hand, if Ip is an integer then any number from the data value at that index to the data value of the next index can be taken as the quantile, and it is conventional (though arbitrary) to take the average of those two values (see Estimating quantiles from a sample).

If, instead of using integers k and q, the "p-quantile" is based on a real number p with 0 < *p* < 1 then p replaces *k*/*q* in the above formulas. This broader terminology is used when quantiles are used to parameterize continuous probability distributions. Moreover, some software programs (including Microsoft Excel) regard the minimum and maximum as the 0th and 100th percentile, respectively. However, this broader terminology is an extension beyond traditional statistics definitions.

### Examples

The following two examples use the Nearest Rank definition of quantile with rounding. For an explanation of this definition, see percentiles.

#### Even-sized population

Consider an ordered population of 10 data values [3, 6, 7, 8, 8, 10, 13, 15, 16, 20]. What are the 4-quantiles (the "quartiles") of this dataset?

| Quartile | Calculation | Result |
|---|---|---|
| Zeroth quartile | Although not universally accepted, one can also speak of the zeroth quartile. This is the minimum value of the set, so the zeroth quartile in this example would be 3. | 3 |
| First quartile | The rank of the first quartile is 10×(1/4) = 2.5, which rounds up to 3, meaning that 3 is the rank in the population (from least to greatest values) at which approximately 1/4 of the values are less than the value of the first quartile. The third value in the population is 7. | 7 |
| Second quartile | The rank of the second quartile (same as the median) is 10×(2/4) = 5, which is an integer, while the number of values (10) is an even number, so the average of both the fifth and sixth values is taken—that is (8+10)/2 = 9, though any value from 8 through to 10 could be taken to be the median. | 9 |
| Third quartile | The rank of the third quartile is 10×(3/4) = 7.5, which rounds up to 8. The eighth value in the population is 15. | 15 |
| Fourth quartile | Although not universally accepted, one can also speak of the fourth quartile. This is the maximum value of the set, so the fourth quartile in this example would be 20. Under the Nearest Rank definition of quantile, the rank of the fourth quartile is the rank of the biggest number, so the rank of the fourth quartile would be 10. | 20 |

So the first, second and third 4-quantiles (the "quartiles") of the dataset [3, 6, 7, 8, 8, 10, 13, 15, 16, 20] are [7, 9, 15]. If also required, the zeroth quartile is 3 and the fourth quartile is 20.

#### Odd-sized population

Consider an ordered population of 11 data values [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]. What are the 4-quantiles (the "quartiles") of this dataset?

| Quartile | Calculation | Result |
|---|---|---|
| Zeroth quartile | Although not universally accepted, one can also speak of the zeroth quartile. This is the minimum value of the set, so the zeroth quartile in this example would be 3. | 3 |
| First quartile | The first quartile is determined by 11×(1/4) = 2.75, which rounds up to 3, meaning that 3 is the rank in the population (from least to greatest values) at which approximately 1/4 of the values are less than the value of the first quartile. The third value in the population is 7. | 7 |
| Second quartile | The second quartile value (same as the median) is determined by 11×(2/4) = 5.5, which rounds up to 6. Therefore, 6 is the rank in the population (from least to greatest values) at which approximately 2/4 of the values are less than the value of the second quartile (or median). The sixth value in the population is 9. | 9 |
| Third quartile | The third quartile value for the original example above is determined by 11×(3/4) = 8.25, which rounds up to 9. The ninth value in the population is 15. | 15 |
| Fourth quartile | Although not universally accepted, one can also speak of the fourth quartile. This is the maximum value of the set, so the fourth quartile in this example would be 20. Under the Nearest Rank definition of quantile, the rank of the fourth quartile is the rank of the biggest number, so the rank of the fourth quartile would be 11. | 20 |

So the first, second and third 4-quantiles (the "quartiles") of the dataset [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20] are [7, 9, 15]. If also required, the zeroth quartile is 3 and the fourth quartile is 20.

### Relationship to the mean

For any population probability distribution on finitely many values, and generally for any probability distribution with a mean and variance, it is the case that $\mu -\sigma \cdot {\sqrt {\frac {1-p}{p}}}\leq Q(p)\leq \mu +\sigma \cdot {\sqrt {\frac {p}{1-p}}}\,,$ where Q(p) is the value of the p-quantile for 0 < *p* < 1 (or equivalently is the k-th q-quantile for *p* = *k*/*q*), where μ is the distribution's arithmetic mean, and where σ is the distribution's standard deviation. In particular, the median (*p* = *k*/*q* = 1/2) is never more than one standard deviation from the mean.

The above formula can be used to bound the value *μ* + *zσ* in terms of quantiles. When *z* ≥ 0, the value that is *z* standard deviations above the mean has a lower bound $\mu +z\sigma \geq Q\left({\frac {z^{2}}{1+z^{2}}}\right)\,,\mathrm {~for~} z\geq 0.$ For example, the value that is *z* = 1 standard deviation above the mean is always greater than or equal to *Q*(*p* = 0.5), the median, and the value that is *z* = 2 standard deviations above the mean is always greater than or equal to *Q*(*p* = 0.8), the fourth quintile.

When *z* ≤ 0, there is instead an upper bound $\mu +z\sigma \leq Q\left({\frac {1}{1+z^{2}}}\right)\,,\mathrm {~for~} z\leq 0.$ For example, the value *μ* + *zσ* for *z* = −3 will never exceed *Q*(*p* = 0.1), the first decile.

## Estimating quantiles from a sample

One problem which frequently arises is estimating a quantile of a (very large or infinite) population based on a finite sample of size N.

Modern statistical packages rely on a number of techniques to estimate the quantiles.

Hyndman and Fan compiled a taxonomy of nine algorithms used by various software packages. All methods compute Qp, the estimate for the p-quantile (the k-th q-quantile, where *p* = *k*/*q*) from a sample of size N by computing a real valued index h. When h is an integer, the h-th smallest of the N values, xh, is the quantile estimate. Otherwise a rounding or interpolation scheme is used to compute the quantile estimate from h, *x*⌊*h*⌋, and *x*⌈*h*⌉. (For notation, see floor and ceiling functions).

The first three are piecewise constant, changing abruptly at each data point, while the last six use linear interpolation between data points, and differ only in how the index h used to choose the point along the piecewise linear interpolation curve, is chosen.

Mathematica, Matlab, R and GNU Octave programming languages support all nine sample quantile methods. SAS includes five sample quantile methods, SciPy and Maple both include eight, EViews and Julia include the six piecewise linear functions, Stata includes two, Python includes two, and Microsoft Excel includes two. Mathematica, SciPy and Julia support arbitrary parameters for methods which allow for other, non-standard, methods. The Google Guava Java library provides the type 7 scheme in the Quantiles class.

The estimate types and interpolation schemes used include:

| Type | h | Qp | Notes |
|---|---|---|---|
| R‑1, SAS‑3, Maple‑1 | Np | *x*⌈*h*⌉ | Inverse of empirical distribution function. |
| R‑2, SAS‑5, Maple‑2, Stata | *Np* + 1/2 | (*x*⌈*h* – 1/2⌉ + *x*⌊*h* + 1/2⌋) / 2 | The same as R-1, but with averaging at discontinuities. |
| R‑3, SAS‑2 | Np | *x*⌊*h*⌉ | The observation numbered closest to Np. Here, ⌊*h*⌉ indicates rounding to the nearest integer, choosing the even integer in the case of a tie. |
| R‑4, SAS‑1, SciPy‑(0,1), Julia‑(0,1), Maple‑3 | Np | *x*⌊*h*⌋ + (*h* − ⌊*h*⌋) (*x*⌈*h*⌉ − *x*⌊*h*⌋) | Linear interpolation of the inverse of the empirical distribution function. |
| R‑5, SciPy‑(1/2,1/2), Julia‑(1/2,1/2), Maple‑4 | *Np* + 1/2 | Piecewise linear function where the knots are the values midway through the steps of the empirical distribution function. |   |
| R‑6, Excel, Python, SAS‑4, SciPy‑(0,0), Julia-(0,0), Maple‑5, Stata‑altdef | (*N* + 1)*p* | Linear interpolation of the expectations for the order statistics for the uniform distribution on [0,1]. That is, it is the linear interpolation between points (*p**h*, *x**h*), where *p**h* = *h*/(*N*+1) is the probability that the last of (*N*+1) randomly drawn values will not exceed the h-th smallest of the first N randomly drawn values. |   |
| R‑7, Excel, Python, SciPy‑(1,1), Julia-(1,1), Maple‑6, NumPy, Guava | (*N* − 1)*p* + 1 | Linear interpolation of the modes for the order statistics for the uniform distribution on [0,1]. |   |
| R‑8, SciPy‑(1/3,1/3), Julia‑(1/3,1/3), Maple‑7 | (*N* + 1/3)*p* + 1/3 | Linear interpolation of the approximate medians for order statistics. |   |
| R‑9, SciPy‑(3/8,3/8), Julia‑(3/8,3/8), Maple‑8 | (*N* + 1/4)*p* + 3/8 | The resulting quantile estimates are approximately unbiased for the expected order statistics if x is normally distributed. |   |

Notes:

- R‑1 through R‑3 are piecewise constant, with discontinuities.
- R‑4 and following are piecewise linear, without discontinuities, but differ in how h is computed.
- R‑3 and R‑4 are not symmetric in that they do not give *h* = (*N* + 1) / 2 when *p* = 1/2.
- Excel's PERCENTILE.EXC and Python's default "exclusive" method are equivalent to R‑6.
- Excel's PERCENTILE and PERCENTILE.INC and Python's optional "inclusive" method are equivalent to R‑7. This is R's and Julia's default method.
- Packages differ in how they estimate quantiles beyond the lowest and highest values in the sample, i.e. *p* < 1/*N* and *p* > (*N* − 1)/*N*. Choices include returning an error value, computing linear extrapolation, or assuming a constant value.

Of the techniques, Hyndman and Fan recommend R-8, but most statistical software packages have chosen R-6 or R-7 as the default.

The standard error of a quantile estimate can in general be estimated via the bootstrap. The Maritz–Jarrett method can also be used.

## The asymptotic distribution of the sample median

The sample median is the most examined one amongst quantiles, being an alternative to estimate a location parameter, when the expected value of the distribution does not exist, and hence the sample mean is not a meaningful estimator of a population characteristic. Moreover, the sample median is a more robust estimator than the sample mean.

One peculiarity of the sample median is its asymptotic distribution: when the sample comes from a continuous distribution, then the sample median has the anticipated Normal asymptotic distribution,

${\text{Sample median m}}\sim {\mathcal {N}}\left(\mu =m,\sigma ^{2}={\frac {1}{4Nf(m)^{2}}}\right)$

This extends to the other quantiles,

${\text{Sample quantile p}}\sim {\mathcal {N}}\left(\mu =x_{p},\sigma ^{2}={\frac {p(1-p)}{Nf(x_{p})^{2}}}\right)$

where *f*(*xp*) is the value of the distribution density at the p-th population quantile ( $x_{p}=F^{-1}(p)$ ).

But when the distribution is discrete, then the distribution of the sample median and the other quantiles fails to be Normal (see examples in https://stats.stackexchange.com/a/86638/28746).

A solution to this problem is to use an alternative definition of sample quantiles through the concept of the "mid-distribution" function, which is defined as

$F_{\text{mid}}(x)=P(X\leq x)-{\frac {1}{2}}P(X=x)$

The definition of sample quantiles through the concept of mid-distribution function can be seen as a generalization that can cover as special cases the continuous distributions. For discrete distributions the sample median as defined through this concept has an asymptotically Normal distribution, see Ma, Y., Genton, M. G., & Parzen, E. (2011). Asymptotic properties of sample quantiles of discrete distributions. Annals of the Institute of Statistical Mathematics, 63(2), 227–243.

## Approximate quantiles from a stream

Computing approximate quantiles from data arriving from a stream can be done efficiently using compressed data structures. The most popular methods are t-digest and KLL. These methods read a stream of values in a continuous fashion and can, at any time, be queried about the approximate value of a specified quantile.

Both algorithms are based on a similar idea: compressing the stream of values by summarizing identical or similar values with a weight. If the stream is made of a repetition of 100 times v1 and 100 times v2, there is no reason to keep a sorted list of 200 elements, it is enough to keep two elements and two counts to be able to recover the quantiles. With more values, these algorithms maintain a trade-off between the number of unique values stored and the precision of the resulting quantiles. Some values may be discarded from the stream and contribute to the weight of a nearby value without changing the quantile results too much. The t-digest maintains a data structure of bounded size using an approach motivated by *k*-means clustering to group similar values. The KLL algorithm uses a more sophisticated "compactor" method that leads to better control of the error bounds at the cost of requiring an unbounded size if errors must be bounded relative to p.

Both methods belong to the family of *data sketches* that are subsets of Streaming Algorithms with useful properties: t-digest or KLL sketches can be combined. Computing the sketch for a very large vector of values can be split into trivially parallel processes where sketches are computed for partitions of the vector in parallel and merged later.

The algorithms described so far directly approximate the empirical quantiles without any particular assumptions on the data, in essence the data are simply numbers or more generally, a set of items that can be ordered. These algorithms are computer science derived methods. Another class of algorithms exist which assume that the data are realizations of a random process. These are statistics derived methods, sequential nonparametric estimation algorithms in particular. There are a number of such algorithms such as those based on stochastic approximation or Hermite series estimators.

These statistics based algorithms typically have constant update time and space complexity, but have different error bound guarantees compared to computer science type methods and make more assumptions. The statistics based algorithms do present certain advantages however, particularly in the non-stationary streaming setting i.e. time-varying data. The algorithms of both classes, along with some respective advantages and disadvantages have been recently surveyed.

## Discussion

Standardized test results are commonly reported as a student scoring "in the 80th percentile", for example. This uses an alternative meaning of the word percentile as the *interval* between (in this case) the 80th and the 81st scalar percentile. This separate meaning of percentile is also used in peer-reviewed scientific research articles. The meaning used can be derived from its context.

If a distribution is symmetric, then the median is the mean (so long as the latter exists). But, in general, the median and the mean can differ. For instance, with a random variable that has an exponential distribution, any particular sample of this random variable will have roughly a 63% chance of being less than the mean. This is because the exponential distribution has a long tail for positive values but is zero for negative numbers.

Quantiles are useful measures because they are less susceptible than means to difficulties created by long-tailed distributions and outliers. Empirically, if the data being analyzed are not actually distributed according to an assumed distribution, or if there are other potential sources for outliers that are far removed from the mean, then quantiles may be more useful descriptive statistics than means and other moment-related statistics.

Closely related is the subject of least absolute deviations, a method of regression that is more robust to outliers than is least squares, in which the sum of the absolute value of the observed errors is used in place of the squared error. The connection is that the mean is the single estimate of a distribution that minimizes expected squared error while the median minimizes expected absolute error. Least absolute deviations shares the ability to be relatively insensitive to large deviations in outlying observations, although even better methods of robust regression are available.

The quantiles of a random variable are preserved under increasing transformations, in the sense that, for example, if m is the median of a random variable X, then 2*m* is the median of 2*X*, unless an arbitrary choice has been made from a range of values to specify a particular quantile. (See quantile estimation, above, for examples of such interpolation.) Quantiles can also be used in cases where only ordinal data are available.

## Other quantifications

Values that divide sorted data into equal subsets other than four have different names.

- The only 2-quantile is called the median
- The 3-quantiles are called tertiles or terciles → T
- The 4-quantiles are called quartiles → Q; the difference between upper and lower quartiles is also called the interquartile range, **midspread** or **middle fifty** → IQR = *Q*3 − *Q*1.
- The 5-quantiles are called quintiles or pentiles → QU
- The 6-quantiles are called sextiles → S
- The 7-quantiles are called septiles → SP
- The 8-quantiles are called octiles → O
- The 10-quantiles are called deciles → D
- The 12-quantiles are called duo-deciles or dodeciles → DD
- The 16-quantiles are called hexadeciles → H
- The 20-quantiles are called ventiles, vigintiles, or demi-deciles → V
- The 100-quantiles are called percentiles or centiles → P
- The 1000-quantiles have been called permilles or milliles, but these are rare and largely obsolete

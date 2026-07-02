---
title: "Standard deviation"
source: https://en.wikipedia.org/wiki/Standard_deviation
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
---

# Standard deviation

In statistics, the **standard deviation** is a measure of the amount of variation of the values of a variable about its (arithmetic) average. A low standard deviation indicates that the values of a set tend to be close to their average, while a high standard deviation indicates that the values are spread out over a wider range. Standard deviation may be abbreviated **SD** or **std dev**, and is most commonly represented in mathematical texts and equations by the lowercase Greek letter **σ** (sigma).

The standard deviation of a random variable, sample, statistical population, data set or probability distribution is the square root of its variance (the variance being the average of the squared deviations from the mean). A useful property of the standard deviation is that, unlike the variance, it is expressed in the same unit as the data. Standard deviation can also be used to calculate standard error for a finite sample, and to determine statistical significance.

When only a sample of data from a population is available, the term *standard deviation of the sample* or *sample standard deviation* can refer to either the above-mentioned quantity as applied to those data, or to a modified quantity that is an unbiased estimate of the *population standard deviation* (the standard deviation of the entire population).

## Relationship with standard error and statistical significance

The standard deviation of a population or sample and the standard error of a statistic (e.g., of the sample mean) are quite different, but related. The sample mean's standard error is the standard deviation of the set of means that would be found by drawing an infinite number of repeated samples from the population and computing a mean for each sample. The mean's standard error turns out to equal the population standard deviation divided by the square root of the sample size, and is estimated by using the sample standard deviation divided by the square root of the sample size. For example, a poll's standard error (what is reported as the margin of error of the poll) is the expected standard deviation of the estimated mean if the same poll were to be conducted multiple times. Thus, the standard error estimates the standard deviation of an estimate, which itself measures how much the estimate depends on the particular sample that was taken from the population.

In science, it is common to report both the standard deviation of the data (as a summary statistic) and the standard error of the estimate (as a measure of potential error in the findings). By convention, only effects more than two standard errors away from a null expectation are considered "statistically significant", a safeguard against spurious conclusion that is really due to random sampling error.

## Basic examples

### Population standard deviation of grades of eight students

Suppose that the entire population of interest is eight students in a particular class. Their marks are the following eight values: $2,\ 4,\ 4,\ 4,\ 5,\ 5,\ 7,\ 9.$

For a finite set of numbers, the population standard deviation is found by taking the square root of the average of the squared deviations of the values subtracted from their average value, that is: $\sigma ={\sqrt {\mathrm {average} \left((v-\mu )^{2}{\text{ for }}v\in \mathrm {values} \right)}}{\text{ where }}\mu =\mathrm {average} (\mathrm {values} ).$

These eight data points have the mean (average) of 5: $\mu ={\frac {2+4+4+4+5+5+7+9}{8}}={\frac {40}{8}}=5.$

Next, calculate the deviations of each data point from the mean. Then square the result of each: ${\begin{array}{lll}(2-5)^{2}=(-3)^{2}=9&&(5-5)^{2}=0^{2}=0\\(4-5)^{2}=(-1)^{2}=1&&(5-5)^{2}=0^{2}=0\\(4-5)^{2}=(-1)^{2}=1&&(7-5)^{2}=2^{2}=4\\(4-5)^{2}=(-1)^{2}=1&&(9-5)^{2}=4^{2}=16.\\\end{array}}$

Next, the variance is the mean of these values: $\sigma ^{2}={\frac {9+1+1+1+0+0+4+16}{8}}={\frac {32}{8}}=4$

Finally, the *population* standard deviation is the square root of the variance: $\sigma ={\sqrt {4}}=2.$

If the eight values with which we began are not the entire population of interest, then this is only one of many possible estimates of the standard deviation in the whole population. This specific one is biased, meaning that its expected value in repeated sampling deviates from the true value, but it is still consistent. Its mean squared error, on the other hand, may be lower than that of the unbiased estimator.

### Standard deviation of average height for adult men

If the population of interest is approximately normally distributed, the standard deviation provides information on the proportion of observations above or below certain values. For example, the average height for adult men in the United States is about 69 inches, with a standard deviation of around 3 inches. This means that most men (about 68%, assuming a normal distribution) have a height within 3 inches of the mean (66–72 inches) – one standard deviation – and almost all men (about 95%) have a height within 6 inches of the mean (63–75 inches) – two standard deviations. If the standard deviation were zero, then all men would share an identical height of 69 inches. Three standard deviations account for 99.73% of the sample population being studied, assuming the distribution is normal or bell-shaped (see the 68–95–99.7 rule, or the *empirical rule*, for more information).

## Definition of population values

Let μ be the expected value (the average) of a random variable X with probability density function f: $\mu \equiv \operatorname {\mathbb {E} } [X]=\int _{-\infty }^{+\infty }x\,f(x)\,{\mathrm {d} }x.$ The standard deviation σ of X is defined as $\sigma \equiv {\sqrt {\operatorname {\mathbb {E} } \left[\left(X-\mu \right)^{2}\right]}}={\sqrt {\int _{-\infty }^{+\infty }\left(x-\mu \right)^{2}f(x)\ {\mathrm {d} }x\;}}\ ,$ which can be shown to equal ${\textstyle {\sqrt {\operatorname {\mathbb {E} } \left[X^{2}\right]-\left(\operatorname {\mathbb {E} } \left[X\right]\right)^{2}}}\,.}$

In other words, the standard deviation is the square root of the variance of X.

The standard deviation of a probability distribution is the same as that of a random variable having that distribution.

Not all random variables have a standard deviation. If the distribution has fat tails going out to infinity, the standard deviation might not exist, because the integral might not converge. The normal distribution has tails going out to infinity, but its mean and standard deviation do exist, because the tails diminish quickly enough. The Pareto distribution with parameter $\alpha \in (1,2]$ has a mean, but not a standard deviation (loosely speaking, the standard deviation is infinite). The Cauchy distribution has neither a mean nor a standard deviation.

### Discrete random variable

In the case where X takes random values from a finite data set *x*1, *x*2, ..., *x**N*, with each value having the same probability, the standard deviation is

$\sigma ={\sqrt {{\frac {1}{N}}\ \left[\left(x_{1}-\mu \right)^{2}+\left(x_{2}-\mu \right)^{2}+\cdots +\left(x_{N}-\mu \right)^{2}\right]\;}}\ ,~~{\text{ where }}~~\mu \equiv {\frac {1}{N}}\left(x_{1}+\cdots +x_{N}\right)\ ,$ Note: The above expression has a built-in bias. See the discussion on Bessel's correction further down below.

or, by using summation notation,

$\sigma ={\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}\left(x_{i}-\mu \right)^{2}\;}}\ ,~~{\text{ where }}~~\mu \equiv {\frac {1}{N}}\sum _{i=1}^{N}x_{i}~.$

If, instead of having equal probabilities, the values have different probabilities, let *x*1 have probability *p*1, *x*2 have probability *p*2, ..., *x**N* have probability *p**N* . In this case, the standard deviation will be $\sigma ={\sqrt {\sum _{i=1}^{N}p_{i}\left(x_{i}-\mu \right)^{2}\;}}\ ,~~{\text{ where }}~~\mu \equiv \sum _{i=1}^{N}p_{i}x_{i}\,.$

### Continuous random variable

The standard deviation of a continuous real-valued random variable X with probability density function *p*(*x*) is $\sigma ={\sqrt {\int _{\mathbf {X} }\left(x-\mu \right)^{2}\,p(x)\,{\mathrm {d} }x}}\,,~~{\text{ where }}~~\mu \equiv \int _{\mathbf {X} }x\,p(x)\,{\mathrm {d} }x\,,$

and where the integrals are definite integrals taken for x ranging over **X**, which represents the set of possible values of the random variable X.

In the case of a parametric family of distributions, the standard deviation can often be expressed in terms of the parameters for the underlying distribution. For example, in the case of the log-normal distribution with parameters μ and *σ*2 for the underlying normal distribution, the standard deviation of the log-normal variable is given by the expression ${\sqrt {\left(e^{\sigma ^{2}}-1\right)\ e^{2\mu +\sigma ^{2}}}}\,.$

## Estimation

One can find the standard deviation of an entire population in cases (such as standardized testing) where every member of a population is sampled. In cases where that cannot be done, the standard deviation σ is estimated by examining a random sample taken from the population and computing a statistic of the sample, which is used as an estimate of the population standard deviation. Such a statistic is called an estimator, and the estimator (or the value of the estimator, namely the estimate) is called a **sample standard deviation**, and is denoted by s (possibly with modifiers).

Unlike in the case of estimating the population mean of a normal distribution, for which the sample mean is a simple estimator with many desirable properties (unbiased, efficient, maximum likelihood), there is no single estimator for the standard deviation with all these properties, and unbiased estimation of standard deviation is a very technically involved problem. Most often, the standard deviation is estimated using the *corrected sample standard deviation* (using *N* − 1), defined below, and this is often referred to as the "sample standard deviation", without qualifiers. However, other estimators are better in other respects: the uncorrected estimator (using N) yields lower mean squared error, while using *N* − 1.5 (for the normal distribution) almost eliminates bias.

### Uncorrected sample standard deviation

The formula for the *population* standard deviation (of a finite population) can be applied to the sample, using the size of the sample as the size of the population (though the actual population size from which the sample is drawn may be much larger). This estimator, denoted by *s**N*, is known as the *uncorrected sample standard deviation*, or sometimes the *standard deviation of the sample* (considered as the entire population), and is defined as follows: $s_{N}={\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}}$ where {*x*1, *x*2, …, *xN*} are the observed values of the sample items and x̄ is the mean value of these observations, while the denominator N stands for the size of the sample: this is the square root of the sample variance, which is the average of the squared deviations about the sample mean.

This is a consistent estimator (it converges in probability to the population value as the number of samples goes to infinity), and is the maximum-likelihood estimate when the population is normally distributed. However, this is a biased estimator, as the estimates are generally too low. The bias decreases as sample size grows, dropping off as 1⁄N, and thus is most significant for small or moderate sample sizes; for N > 75, the bias is below 1%. Thus for very large sample sizes, the uncorrected sample standard deviation is generally acceptable. This estimator also has a uniformly smaller mean squared error than the corrected sample standard deviation.

### Corrected sample standard deviation

If the *biased sample variance* (the second central moment of the sample, which is a downward-biased estimate of the population variance) is used to compute an estimate of the population's standard deviation, the result is $s_{N}={\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}}.$

Here taking the square root introduces further downward bias, by Jensen's inequality, due to the square root's being a concave function. The bias in the variance is easily corrected, but the bias from the square root is more difficult to correct, and depends on the distribution in question.

An unbiased estimator for the *variance* is given by applying Bessel's correction, using *N* − 1 instead of N to yield the *unbiased sample variance,* denoted *s*2: $s^{2}={\frac {1}{N-1}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}.$

This estimator is unbiased if the variance exists and the sample values are drawn independently with replacement. *N* − 1 corresponds to the number of degrees of freedom in the vector of deviations from the mean, $\textstyle (x_{1}-{\bar {x}},\;\dots ,\;x_{n}-{\bar {x}}).$

Taking square roots reintroduces bias (because the square root is a nonlinear function which does not commute with the expectation, i.e. often ${\textstyle E[{\sqrt {X}}]\neq {\sqrt {E[X]}}}$ ), yielding the *corrected sample standard deviation,* denoted by s: $s={\sqrt {{\frac {1}{N-1}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}}.$

As explained above, while *s*2 is an unbiased estimator for the population variance, s is still a biased estimator for the population standard deviation, though markedly less biased than the uncorrected sample standard deviation. This estimator is commonly used and generally known simply as the "sample standard deviation". The bias may still be large for small samples (N less than 10). As sample size increases, the amount of bias decreases. We obtain more information and the difference between ${\frac {1}{N}}$ and ${\frac {1}{N-1}}$ becomes smaller.

### Unbiased sample standard deviation

For unbiased estimation of standard deviation, there is no formula that works across all distributions, unlike for mean and variance. Instead, s is used as a basis, and is scaled by a correction factor to produce an unbiased estimate. For the normal distribution, an unbiased estimator is given by ⁠*s*/*c*4⁠, where the correction factor (which depends on N) is given in terms of the gamma function, and equals: $c_{4}(N)\,=\,{\sqrt {\frac {2}{N-1}}}\,\,\,{\frac {\Gamma {\left({\frac {N}{2}}\right)}}{\Gamma {\left({\frac {N-1}{2}}\right)}}}.$

This arises because the sampling distribution of the sample standard deviation follows a (scaled) chi distribution, and the correction factor is the mean of the chi distribution.

An approximation can be given by replacing *N* − 1 with *N* − 1.5, yielding: ${\hat {\sigma }}={\sqrt {{\frac {1}{N-1.5}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}},$

The error in this approximation decays quadratically (as ⁠1/*N*2⁠), and it is suited for all but the smallest samples or highest precision: for *N* = 3 the bias is equal to 1.3%, and for *N* = 9 the bias is less than 0.1%.

A more accurate approximation is to replace *N* − 1.5 above with *N* − 1.5 + ⁠1/8(*N* − 1)⁠.

For other distributions, the correct formula depends on the distribution, but a rule of thumb is to use the further refinement of the approximation: ${\hat {\sigma }}={\sqrt {{\frac {1}{N-1.5-{\frac {1}{4}}\gamma _{2}}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}},$

where *γ*2 denotes the population excess kurtosis. The excess kurtosis may be either known beforehand for certain distributions, or estimated from the data.

### Confidence interval of a sampled standard deviation

The standard deviation we obtain by sampling a distribution is itself not absolutely accurate, both for mathematical reasons (explained here by the confidence interval) and for practical reasons of measurement (measurement error). The mathematical effect can be described by the confidence interval or CI.

To show how a larger sample will make the confidence interval narrower, consider the following examples: A small population of *N* = 2 has only one degree of freedom for estimating the standard deviation. The result is that a 95% CI of the SD runs from 0.45 × SD to 31.9 × SD; the factors here are as follows:

$\Pr \left(q_{\frac {\alpha }{2}}<k{\frac {s^{2}}{\sigma ^{2}}}<q_{1-{\frac {\alpha }{2}}}\right)=1-\alpha ,$

where $q_{p}$ is the p-th quantile of the chi-square distribution with k degrees of freedom, and 1 − *α* is the confidence level. This is equivalent to the following:

$\Pr \left(k{\frac {s^{2}}{q_{1-{\frac {\alpha }{2}}}}}<\sigma ^{2}<k{\frac {s^{2}}{q_{\frac {\alpha }{2}}}}\right)=1-\alpha .$

With *k* = 1, *q*0.025 = 0.000982 and *q*0.975 = 5.024. The reciprocals of the square roots of these two numbers give us the factors 0.45 and 31.9 given above.

A larger population of *N* = 10 has 9 degrees of freedom for estimating the standard deviation. The same computations as above give us in this case a 95% CI running from 0.69 × SD to 1.83 × SD. So even with a sample population of 10, the actual SD can still be almost a factor 2 higher than the sampled SD. For a sample population *N* = 100, this is down to 0.88 × SD to 1.16 × SD. To be more certain that the sampled SD is close to the actual SD we need to sample a large number of points.

These same formulae can be used to obtain confidence intervals on the variance of residuals from a least squares fit under standard normal theory, where k is now the number of degrees of freedom for error.

### Bounds on standard deviation

For a set of *N* > 4 data spanning a range of values R, an upper bound on the standard deviation s is given by *s* = 0.6*R*. An estimate of the standard deviation for *N* > 100 data taken to be approximately normal follows from the heuristic that 95% of the area under the normal curve lies roughly two standard deviations to either side of the mean, so that, with 95% probability the total range of values R represents four standard deviations so that *s* ≈ *R*/4. This so-called range rule is useful in sample size estimation, as the range of possible values is easier to estimate than the standard deviation. Other divisors *K*(*N*) of the range such that *s* ≈ *R*/*K*(*N*) are available for other values of N and for non-normal distributions.

## Identities and mathematical properties

The standard deviation is invariant under changes in location, and scales directly with the scale of the random variable. Thus, for a constant c and random variables X and Y: ${\begin{aligned}\sigma (c)&=0\\\sigma (X+c)&=\sigma (X),\\\sigma (cX)&=|c|\sigma (X).\end{aligned}}$

The standard deviation of the sum of two random variables can be related to their individual standard deviations and the covariance between them:

$\sigma (X+Y)={\sqrt {\operatorname {var} (X)+\operatorname {var} (Y)+2\,\operatorname {cov} (X,Y)}}.\,$

where $\textstyle \operatorname {var} \,=\,\sigma ^{2}$ and $\textstyle \operatorname {cov}$ stand for variance and covariance, respectively.

The calculation of the sum of squared deviations can be related to moments calculated directly from the data. In the following formula, the letter E is interpreted to mean expected value, i.e., mean.

$\sigma (X)={\sqrt {\operatorname {E} \left[\left(X-\operatorname {E} [X]\right)^{2}\right]}}={\sqrt {\operatorname {E} \left[X^{2}\right]-\left(\operatorname {E} [X]\right)^{2}}}.$

The sample standard deviation can be computed as: $s(X)={\sqrt {\frac {N}{N-1}}}{\sqrt {\operatorname {E} \left[\left(X-\operatorname {E} [X]\right)^{2}\right]}}.$

For a finite population with equal probabilities at all points, we have

${\begin{aligned}{\sqrt {{\frac {1}{N}}\sum _{i=1}^{N}\left(x_{i}-{\bar {x}}\right)^{2}}}&={\sqrt {{\frac {1}{N}}\left(\sum _{i=1}^{N}x_{i}^{2}\right)-{\bar {x}}^{2}}}\\[1ex]&={\sqrt {\left({\frac {1}{N}}\sum _{i=1}^{N}x_{i}^{2}\right)-\left({\frac {1}{N}}\sum _{i=1}^{N}x_{i}\right)^{2}}},\end{aligned}}$

which means that the standard deviation is equal to the square root of the difference between the average of the squares of the values and the square of the average value.

See computational formula for the variance for proof, and for an analogous result for the sample standard deviation.

## Interpretation and application

A large standard deviation indicates that the data points can spread far from the mean and a small standard deviation indicates that they are clustered closely around the mean.

For example, each of the three populations {0, 0, 14, 14}, {0, 6, 8, 14} and {6, 6, 8, 8} has a mean of 7. Their standard deviations are 7, 5, and 1, respectively. The third population has a much smaller standard deviation than the other two because its values are all close to 7. These standard deviations have the same units as the data points themselves. If, for instance, the data set {0, 6, 8, 14} represents the ages of a population of four siblings in years, the standard deviation is 5 years. As another example, the population {1000, 1006, 1008, 1014} may represent the distances traveled by four athletes, measured in meters. It has a mean of 1007 meters, and a standard deviation of 5 meters.

Standard deviation may serve as a measure of uncertainty. In physical science, for example, the reported standard deviation of a group of repeated measurements gives the precision of those measurements. When deciding whether measurements agree with a theoretical prediction, the standard deviation of those measurements is of crucial importance: if the mean of the measurements is too far away from the prediction (with the distance measured in standard deviations), then the theory being tested probably needs to be revised. This makes sense since they fall outside the range of values that could reasonably be expected to occur if the prediction were correct and the standard deviation appropriately quantified. See prediction interval.

While the standard deviation does measure how far typical values tend to be from the mean, other measures are available. An example is the mean absolute deviation, which might be considered a more direct measure of average distance, compared to the root mean square distance inherent in the standard deviation.

### Application examples

The practical value of understanding the standard deviation of a set of values is in appreciating how much variation there is from the average (mean).

#### Experiment, industrial and hypothesis testing

Standard deviation is often used to compare real-world data against a model to test the model. For example, in industrial applications the weight of products coming off a production line may need to comply with a legally required value. By weighing some fraction of the products an average weight can be found, which will always be slightly different from the long-term average. By using standard deviations, a minimum and maximum value can be calculated that the averaged weight will be within some very high percentage of the time (99.9% or more). If it falls outside the range then the production process may or not need to be corrected. Statistical tests such as these are particularly important when the testing is relatively expensive. For example, if the product needs to be opened and drained and weighed, or if the product was otherwise used up by the test.

In experimental science, a theoretical model of reality is used. Particle physics conventionally uses a standard of "**5 sigma**" for the declaration of a discovery. A five-sigma level translates to one chance in 3.5 million that a random fluctuation would yield the result. For example, this level of certainty was required by each of two independent particle physics experiments at CERN in order to announce that the Higgs boson had been discovered, or by the LIGO Scientific Collaboration to conclusively confirm the existence of gravitational waves.

#### Weather

As a simple example, consider the average daily maximum temperatures for two cities, one inland and one on the coast. It is helpful to understand that the range of daily maximum temperatures for cities near the coast is smaller than for cities inland. Thus, while these two cities may each have the same average maximum temperature, the standard deviation of the daily maximum temperature for the coastal city will be less than that of the inland city as, on any particular day, the actual maximum temperature is more likely to be farther from the average maximum temperature for the inland city than for the coastal one.

#### Finance

In finance, standard deviation is often used as a measure of the risk associated with price-fluctuations of a given asset (stocks, bonds, property, etc.), or the risk of a portfolio of assets (actively managed mutual funds, index mutual funds, or ETFs). Risk is an important factor in determining how to efficiently manage a portfolio of investments because it determines the variation in returns on the asset or portfolio and gives investors a mathematical basis for investment decisions (known as mean-variance optimization). The fundamental concept of risk is that as it increases, the expected return on an investment should increase as well, an increase known as the risk premium. In other words, investors should expect a higher return on an investment when that investment carries a higher level of risk or uncertainty. When evaluating investments, investors should estimate both the expected return and the uncertainty of future returns. Standard deviation provides a quantified estimate of the uncertainty of future returns.

For example, assume an investor had to choose between two stocks. Stock A over the past 20 years had an average return of 10 percent, with a standard deviation of 20 percentage points (pp) and Stock B, over the same period, had average returns of 12 percent but a higher standard deviation of 30 pp. On the basis of risk and return, an investor may decide that Stock A is the safer choice, because Stock B's additional two percentage points of return is not worth the additional 10 pp standard deviation (greater risk or uncertainty of the expected return). Stock B is likely to fall short of the initial investment (but also to exceed the initial investment) more often than Stock A under the same circumstances, and is estimated to return only two percent more on average. In this example, Stock A is expected to earn about 10 percent, plus or minus 20 pp (a range of 30 percent to −10 percent), about two-thirds of the future year returns. When considering more extreme possible returns or outcomes in future, an investor should expect results of as much as 10 percent plus or minus 60 pp, or a range from 70 percent to −50 percent, which includes outcomes for three standard deviations from the average return (about 99.7 percent of probable returns).

Calculating the average (or arithmetic mean) of the return of a security over a given period will generate the expected return of the asset. For each period, subtracting the expected return from the actual return results in the difference from the mean. Squaring the difference in each period and taking the average gives the overall variance of the return of the asset. The larger the variance, the greater risk the security carries. Finding the square root of this variance will give the standard deviation of the investment tool in question.

Financial time series are known to be non-stationary series, whereas the statistical calculations above, such as standard deviation, apply only to stationary series. To apply the above statistical tools to non-stationary series, the series first must be transformed to a stationary series, enabling use of statistical tools that now have a valid basis from which to work.

### Geometric interpretation

To gain some geometric insights and clarification, we will start with a population of three values, *x*1, *x*2, *x*3. This defines a point *P* = (*x*1, *x*2, *x*3) in **R**3. Consider the line *L* = {(*r*, *r*, *r*) : *r* ∈ **R**}. This is the "main diagonal" going through the origin. If our three given values were all equal, then the standard deviation would be zero and P would lie on L. So it is not unreasonable to assume that the standard deviation is related to the *distance* of P to L. That is indeed the case. To move orthogonally from L to the point P, one begins at the point:

$M=\left({\bar {x}},{\bar {x}},{\bar {x}}\right)$

whose coordinates are the mean of the values we started out with.

| Derivation of $M=\left({\bar {x}},{\bar {x}},{\bar {x}}\right)$ |
|---|
| M is on L therefore $M=(\ell ,\ell ,\ell )$ for some $\ell \in \mathbb {R}$ . The line L is to be orthogonal to the vector from M to P. Therefore: ${\begin{aligned}L\cdot (P-M)&=0\\[4pt](r,r,r)\cdot (x_{1}-\ell ,x_{2}-\ell ,x_{3}-\ell )&=0\\[4pt]r(x_{1}-\ell +x_{2}-\ell +x_{3}-\ell )&=0\\[4pt]r\left(\sum _{i}x_{i}-3\ell \right)&=0\\[4pt]\sum _{i}x_{i}-3\ell &=0\\[4pt]{\frac {1}{3}}\sum _{i}x_{i}&=\ell \\[4pt]{\bar {x}}&=\ell \end{aligned}}$ |

A little algebra shows that the distance between P and M (which is the same as the orthogonal distance between P and the line L) ${\textstyle {\sqrt {\sum _{i}\left(x_{i}-{\bar {x}}\right)^{2}}}}$ is equal to the standard deviation of the vector (*x*1, *x*2, *x*3), multiplied by the square root of the number of dimensions of the vector (3 in this case).

### Chebyshev's inequality

An observation is rarely more than a few standard deviations away from the mean. Chebyshev's inequality ensures that, for all distributions for which the standard deviation is defined, the amount of data within a number of standard deviations of the mean is at least as much as given in the following table.

| Distance from mean | Minimum population |
|---|---|
| ${\sqrt {2}}\,\sigma$ | 50% |
| $2\sigma$ | 75% |
| $3\sigma$ | 89% |
| $4\sigma$ | 94% |
| $5\sigma$ | 96% |
| $6\sigma$ | 97% |
| $k\sigma$ | $1-{\frac {1}{k^{2}}}$ |
| ${\frac {1}{\sqrt {1-\ell }}}\,\sigma$ | $\ell$ |

### Rules for normally distributed data

The central limit theorem states that the distribution of an average of many independent, identically distributed random variables tends toward the famous bell-shaped normal distribution with a probability density function of

$f\left(x,\mu ,\sigma ^{2}\right)={\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}},$

where μ is the expected value of the random variables, σ equals their distribution's standard deviation divided by *n*1⁄2, and n is the number of random variables. The standard deviation therefore is simply a scaling variable that adjusts how broad the curve will be, though it also appears in the normalizing constant.

If a data distribution is approximately normal, then the proportion of data values within z standard deviations of the mean is defined by:

${\text{Proportion}}=\operatorname {erf} \left({\frac {z}{\sqrt {2}}}\right)$

where $\textstyle \operatorname {erf}$ is the error function. The proportion that is less than or equal to a number, x, is given by the cumulative distribution function:

${\text{Proportion}}\leq x={\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {x-\mu }{\sigma {\sqrt {2}}}}\right)\right]={\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {z}{\sqrt {2}}}\right)\right].$

If a data distribution is approximately normal then about 68 percent of the data values are within one standard deviation of the mean (mathematically, *μ* ± *σ*, where μ is the arithmetic mean), about 95 percent are within two standard deviations (*μ* ± 2*σ*), and about 99.7 percent lie within three standard deviations (*μ* ± 3*σ*). This is known as the *68–95–99.7 rule*, or *the empirical rule*.

For various values of z, the percentage of values expected to lie in and outside the symmetric interval, *CI* = (−*z'**σ*****, *z'****σ*), are as follows:

| Confidence interval | Proportion within | Proportion without |   |
|---|---|---|---|
| Percentage | Percentage | Fraction |   |
| 0.318639σ | 25% | 75% | 3 / 4 |
| 0.674490σ | 50% | 50% | 1 / 2 |
| 0.977925σ | 66.6667% | 33.3333% | 1 / 3 |
| 0.994458σ | 68% | 32% | 1 / 3.125 |
| 1σ | 68.2689492% | 31.7310508% | 1 / 3.1514872 |
| 1.281552σ | 80% | 20% | 1 / 5 |
| 1.644854σ | 90% | 10% | 1 / 10 |
| 1.959964σ | 95% | 5% | 1 / 20 |
| 2σ | 95.4499736% | 4.5500264% | 1 / 21.977895 |
| 2.575829σ | 99% | 1% | 1 / 100 |
| 3σ | 99.7300204% | 0.2699796% | 1 / 370.398 |
| 3.290527σ | 99.9% | 0.1% | 1 / 1000 |
| 3.890592σ | 99.99% | 0.01% | 1 / 10000 |
| 4σ | 99.993666% | 0.006334% | 1 / 15787 |
| 4.417173σ | 99.999% | 0.001% | 1 / 100000 |
| 4.5σ | 99.9993204653751% | 0.0006795346249% | 1 / 147159.5358 6.8 / 1000000 |
| 4.891638σ | 99.9999% | 0.0001% | 1 / 1000000 |
| 5σ | 99.9999426697% | 0.0000573303% | 1 / 1744278 |
| 5.326724σ | 99.99999% | 0.00001% | 1 / 10000000 |
| 5.730729σ | 99.999999% | 0.000001% | 1 / 100000000 |
| 6σ | 99.9999998027% | 0.0000001973% | 1 / 506797346 |
| 6.109410σ | 99.9999999% | 0.0000001% | 1 / 1000000000 |
| 6.466951σ | 99.99999999% | 0.00000001% | 1 / 10000000000 |
| 6.806502σ | 99.999999999% | 0.000000001% | 1 / 100000000000 |
| 7σ | 99.9999999997440% | 0.000000000256% | 1 / 390682215445 |

## Standard deviation matrix

The standard deviation matrix $\mathbf {S}$ is the extension of the standard deviation to multiple dimensions. It is the symmetric square root of the covariance matrix $\mathbf {\Sigma }$ .

$\mathbf {S}$ linearly scales a random vector in multiple dimensions in the same way that $\sigma$ does in one dimension. A scalar random variable x with variance $\sigma ^{2}$ can be written as $x=\sigma z$ , where z has unit variance. In the same way, a random vector ${\boldsymbol {x}}$ in several dimensions with covariance $\mathbf {\Sigma }$ can be written as ${\boldsymbol {x}}=\mathbf {S} {\boldsymbol {z}}$ , where ${\boldsymbol {z}}$ is a normalized variable with identity covariance $\mathbf {1}$ . This requires that $\mathbf {S} \mathbf {S'} =\mathbf {\Sigma }$ . There are then infinite solutions for $\mathbf {S}$ , and consequently there are multiple ways to whiten the distribution. The symmetric square root of $\mathbf {\Sigma }$ is one of the solutions.

For example, a multivariate normal vector ${\boldsymbol {x}}\sim N({\boldsymbol {\mu }},\mathbf {\Sigma } )$ can be defined as ${\boldsymbol {x}}=\mathbf {S} {\boldsymbol {z}}+{\boldsymbol {\mu }}$ , where ${\boldsymbol {z}}\sim N({\boldsymbol {0}},\mathbf {1} )$ is the multivariate standard normal.

### Properties

- The eigenvectors and eigenvalues of $\mathbf {S}$ correspond to the axes of the 1 sd error ellipsoid of the multivariate normal distribution. See *Multivariate normal distribution: geometric interpretation*.
- The standard deviation of the *projection* of the multivariate distribution (i.e. the marginal distribution) on to a line in the direction of the unit vector ${\hat {\boldsymbol {\eta }}}$ equals ${\sqrt {{\hat {\boldsymbol {\eta }}}'\mathbf {\Sigma } {\hat {\boldsymbol {\eta }}}}}=\lVert \mathbf {S} {\hat {\boldsymbol {\eta }}}\rVert$ .
- The standard deviation of a *slice* of the multivariate distribution (i.e. the conditional distribution) along the line in the direction of the unit vector ${\hat {\boldsymbol {\eta }}}$ equals ${\frac {1}{\lVert \mathbf {S} ^{-1}{\hat {\boldsymbol {\eta }}}\rVert }}$ .
- The discriminability index between two equal-covariance distributions is their Mahalanobis distance, which can also be expressed in terms of the sd matrix: $d'={\sqrt {({\boldsymbol {\mu }}_{a}-{\boldsymbol {\mu }}_{b})'{\boldsymbol {\Sigma }}^{-1}({\boldsymbol {\mu }}_{a}-{\boldsymbol {\mu }}_{b})}}=\lVert \mathbf {S} ^{-1}{\boldsymbol {d}}\rVert$ , where ${\boldsymbol {d}}={\boldsymbol {\mu }}_{a}-{\boldsymbol {\mu }}_{b}$ is the mean-difference vector.
- Since $\mathbf {S}$ scales a normalized variable, it can be used to invert the transformation, and make it decorrelated and unit-variance: ${\boldsymbol {z}}=\mathbf {S} ^{-1}({\boldsymbol {x}}-{\boldsymbol {\mu }})$ has zero mean and identity covariance. This is called the Mahalanobis whitening transform.

## Relationship between standard deviation and mean

The mean and the standard deviation of a set of data are descriptive statistics usually reported together. In a certain sense, the standard deviation is a "natural" measure of statistical dispersion if the center of the data is measured about the mean. This is because the standard deviation from the mean is smaller than from any other point. The precise statement is the following: suppose *x*1, ..., *x**n* are real numbers and define the function:

$\sigma (r)={\sqrt {{\frac {1}{N-1}}\sum _{i=1}^{N}\left(x_{i}-r\right)^{2}}}.$

Using calculus or by completing the square, it is possible to show that *σ*(*r*) has a unique minimum at the mean:

$r={\bar {x}}.\,$

Variability can also be measured by the coefficient of variation, which is the ratio of the standard deviation to the mean. It is a dimensionless number.

### Standard deviation of the mean

Often, we want some information about the precision of the mean we obtained. We can obtain this by determining the standard deviation of the sampled mean. Assuming statistical independence of the values in the sample, the **standard deviation of the mean** (**SDOM**) is related to the standard deviation of the distribution by:

$\sigma _{\text{mean}}={\frac {1}{\sqrt {N}}}\sigma ,$

where N is the number of observations in the sample used to estimate the mean. This can easily be proven with (see basic properties of the variance): ${\begin{aligned}\operatorname {var} (X)&=\sigma _{X}^{2}\\\operatorname {var} (X_{1}+X_{2})&=\operatorname {var} (X_{1})+\operatorname {var} (X_{2})\\\end{aligned}}$ (Statistical independence is assumed.) $\operatorname {var} (cX_{1})\equiv c^{2}\,\operatorname {var} (X_{1})$

hence ${\begin{aligned}\operatorname {var} ({\text{mean}})&=\operatorname {var} \left({\frac {1}{N}}\sum _{i=1}^{N}X_{i}\right)={\frac {1}{N^{2}}}\operatorname {var} \left(\sum _{i=1}^{N}X_{i}\right)\\&={\frac {1}{N^{2}}}\sum _{i=1}^{N}\operatorname {var} (X_{i})={\frac {N}{N^{2}}}\operatorname {var} (X)={\frac {1}{N}}\operatorname {var} (X).\end{aligned}}$

Resulting in: $\sigma _{\text{mean}}={\frac {\sigma }{\sqrt {N}}}.$

In order to estimate the standard deviation of the mean *σ*mean it is necessary to know the standard deviation of the entire population σ beforehand. However, in most applications this parameter is unknown. For example, if a series of 10 measurements of a previously unknown quantity is performed in a laboratory, it is possible to calculate the resulting sample mean and sample standard deviation, but it is impossible to calculate the standard deviation of the mean. However, one can estimate the standard deviation of the entire population from the sample, and thus obtain an estimate for the standard error of the mean.

## Rapid calculation methods

The following two formulas can represent a running (repeatedly updated) standard deviation. A set of two power sums *s*1 and *s*2 are computed over a set of N values of x, denoted as *x*1, ..., *x**N*:

$s_{j}=\sum _{k=1}^{N}{x_{k}^{j}}.$

Given the results of these running summations, the values N, *s*1, *s*2 can be used at any time to compute the *current* value of the running standard deviation:

$\sigma ={\frac {\sqrt {Ns_{2}-(s_{1})^{2}}}{N}}.$

Where N, as mentioned above, is the size of the set of values (or can also be regarded as *s*0).

Similarly for sample standard deviation,

$s={\sqrt {\frac {Ns_{2}-(s_{1})^{2}}{N(N-1)}}}.$

In a computer implementation, as the two *s**j* sums become large, we need to consider round-off error, arithmetic overflow, and arithmetic underflow. The method below calculates the running sums method with reduced rounding errors. This is a "one pass" algorithm for calculating variance of n samples without the need to store prior data during the calculation. Applying this method to a time series will result in successive values of standard deviation corresponding to n data points as n grows larger with each new sample, rather than a constant-width sliding window calculation.

For *k* = 1, ..., *n*:

${\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {x_{k}-A_{k-1}}{k}}\end{aligned}}$

where A is the mean value. ${\begin{aligned}Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {k-1}{k}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}$

Note: *Q*1 = 0 since *k* − 1 = 0 or *x*1 = *A*1.

Sample variance: $s_{n}^{2}={\frac {Q_{n}}{n-1}}$

Population variance: $\sigma _{n}^{2}={\frac {Q_{n}}{n}}$

### Weighted calculation

When the values $x_{k}$ are weighted with unequal weights $w_{k}$ , the power sums *s*0, s1, *s*2 are each computed as:

$s_{j}=\sum _{k=1}^{N}w_{k}x_{k}^{j}.\,$

And the standard deviation equations remain unchanged. *s*0 is now the sum of the weights and not the number of samples N.

The incremental method with reduced rounding errors can also be applied, with some additional complexity.

A running sum of weights must be computed for each k from 1 to n: ${\begin{aligned}W_{0}&=0\\W_{k}&=W_{k-1}+w_{k}\end{aligned}}$

and places where 1/*k* is used above must be replaced by $w_{k}/W_{k}$ : ${\begin{aligned}A_{0}&=0\\A_{k}&=A_{k-1}+{\frac {w_{k}}{W_{k}}}\left(x_{k}-A_{k-1}\right)\\Q_{0}&=0\\Q_{k}&=Q_{k-1}+{\frac {w_{k}W_{k-1}}{W_{k}}}\left(x_{k}-A_{k-1}\right)^{2}\\&=Q_{k-1}+w_{k}\left(x_{k}-A_{k-1}\right)\left(x_{k}-A_{k}\right)\end{aligned}}$

In the final division, $\sigma _{n}^{2}={\frac {Q_{n}}{W_{n}}}\,$

and $s_{n}^{2}={\frac {Q_{n}}{W_{n}-1}},$

or $s_{n}^{2}={\frac {n'}{n'-1}}\sigma _{n}^{2},$

where n is the total number of elements, and n′ is the number of elements with non-zero weights.

The above formulas become equal to the simpler formulas given above if weights are taken as equal to one.

## History

The term *standard deviation* was first used in writing by Karl Pearson in 1894, following his use of it in lectures. This was as a replacement for earlier alternative names for the same idea: for example, Gauss used *mean error*.

## Standard deviation index

The standard deviation index (SDI) is used in external quality assessments, particularly for medical laboratories. It is calculated as: ${\text{SDI}}={\frac {{\text{Laboratory mean}}-{\text{Consensus group mean}}}{\text{Consensus group standard deviation}}}.$

## Alternatives

Standard deviation is algebraically simpler, though in practice less robust, than the average absolute deviation.

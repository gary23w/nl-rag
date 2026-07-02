---
title: "Pearson's chi-squared test"
source: https://en.wikipedia.org/wiki/Pearson's_chi-squared_test
domain: chi-squared-tests
license: CC-BY-SA-4.0
tags: chi-squared test, contingency table, goodness of fit, G-test
fetched: 2026-07-02
---

# Pearson's chi-squared test

**Pearson's chi-squared test** or **Pearson's $\chi ^{2}$ test** is a statistical test applied to sets of categorical data to evaluate how likely it is that any observed difference between the sets arose by chance. It is the most widely used of many chi-squared tests (e.g., Yates, likelihood ratio, portmanteau test in time series, etc.) – statistical procedures whose results are evaluated by reference to the chi-squared distribution. Its properties were first investigated by Karl Pearson in 1900. In contexts where it is important to improve a distinction between the test statistic and its distribution, names similar to *Pearson χ-squared* test or statistic are used. It is a p-value test.

A simple example is testing the hypothesis that an ordinary six-sided die is "fair" (i. e., all six outcomes are equally likely to occur). In this case, the observed data is $(O_{1},O_{2},...,O_{6})$ , the number of times that the die has fallen on each number. The null hypothesis is $\mathrm {Multinomial} (N;1/6,...,1/6)$ , and ${\textstyle \chi ^{2}:=\sum \limits _{i=1}^{6}{\frac {{\left(O_{i}-N/6\right)}^{2}}{N/6}}}$ . As detailed below, if $\chi ^{2}>11.07$ , then the fairness of the die can be rejected at the level of $p<0.05$ .

## Procedure

The setup is as follows:

- Before the experiment, the experimenter fixes a certain number N of samples to take.
- The observed data is $(O_{1},O_{2},...,O_{n})$ , the count number of samples from a finite set of given categories. They satisfy ${\textstyle \sum _{i}O_{i}=N}$ .
- The null hypothesis is that the count numbers are sampled from a multinomial distribution $\mathrm {Multinomial} (N;p_{1},...,p_{n})$ . That is, the underlying data is sampled IID from a categorical distribution $\mathrm {Categorical} (p_{1},...,p_{n})$ over the given categories.
- The Pearson's chi-squared test statistic is defined as ${\textstyle \chi ^{2}:=\sum _{i}{\frac {{\left(O_{i}-Np_{i}\right)}^{2}}{Np_{i}}}}$ . The p-value of the test statistic is computed either numerically or by looking it up in a table.
- If the p-value is small enough (usually p < 0.05 by convention), then the null hypothesis is rejected, and we conclude that the observed data does not follow the multinomial distribution.

## Usage

Pearson's chi-squared test is used to assess three types of comparison: goodness of fit, homogeneity, and independence.

- A test of goodness of fit establishes whether an observed frequency distribution differs from a theoretical distribution.
- A test of homogeneity compares the distribution of counts for two or more groups using the same categorical variable (e.g. choice of activity—college, military, employment, travel—of graduates of a high school reported a year after graduation, sorted by graduation year, to see if number of graduates choosing a given activity has changed from class to class, or from decade to decade).
- A test of independence assesses whether observations consisting of measures on two variables, expressed in a contingency table, are independent of each other (e.g. polling responses from people of different nationalities to see if one's nationality is related to the response).

For all three tests, the computational procedure includes the following steps:

1. Calculate the chi-squared test statistic, $\chi ^{2}$ , which resembles a normalized sum of squared deviations between observed and theoretical frequencies (see below).
2. Determine the degrees of freedom, **df**, of that statistic.
  1. For a test of goodness-of-fit, df = Cats − Params, where *Cats* is the number of observation categories recognized by the model, and *Params* is the number of parameters in the model adjusted to make the model best fit the observations: The number of categories reduced by the number of fitted parameters in the distribution.
  2. For a test of homogeneity, df = (Rows − 1)×(Cols − 1), where *Rows* corresponds to the number of categories (i.e. rows in the associated contingency table), and *Cols* corresponds to the number of independent groups (i.e. columns in the associated contingency table).
  3. For a test of independence, df = (Rows − 1)×(Cols − 1), where in this case, *Rows* corresponds to the number of categories in one variable, and *Cols* corresponds to the number of categories in the second variable.
3. Select a desired level of confidence (significance level, *p*-value, or the corresponding alpha level) for the result of the test.
4. Compare $\chi ^{2}$ to the critical value from the chi-squared distribution with *df* degrees of freedom and the selected confidence level (one-sided, since the test is only in one direction, i.e. is the test value greater than the critical value?), which in many cases gives a good approximation of the distribution of $\chi ^{2}$ .
5. Sustain or reject the null hypothesis that the observed frequency distribution is the same as the theoretical distribution based on whether the test statistic exceeds the critical value of $\chi ^{2}$ . If the test statistic exceeds the critical value of $\chi ^{2}$ , the null hypothesis ( $H_{0}$ = there is *no* difference between the distributions) can be rejected, and the alternative hypothesis ( $H_{1}$ = there *is* a difference between the distributions) can be accepted, both with the selected level of confidence. If the test statistic falls below the threshold $\chi ^{2}$ value, then no clear conclusion can be reached, and the null hypothesis is sustained (we fail to reject the null hypothesis), though not necessarily accepted.

## Test for fit of a distribution

### Discrete uniform distribution

In this case N observations are divided among n cells. A simple application is to test the hypothesis that, in the general population, values would occur in each cell with equal frequency. The "theoretical frequency" for any cell (under the null hypothesis of a discrete uniform distribution) is thus calculated as $E_{i}={\frac {N}{n}}\,,$ and the reduction in the degrees of freedom is $p=1$ , notionally because the observed frequencies $O_{i}$ are constrained to sum to N .

One specific example of its application would be its application for log-rank test.

### Other distributions

When testing whether observations are random variables whose distribution belongs to a given family of distributions, the "theoretical frequencies" are calculated using a distribution from that family fitted in some standard way. The reduction in the degrees of freedom is calculated as $p=s+1$ , where s is the number of parameters used in fitting the distribution. For instance, when checking a three-parameter Generalized gamma distribution, $p=4$ , and when checking a normal distribution (where the parameters are mean and standard deviation), $p=3$ , and when checking a Poisson distribution (where the parameter is the expected value), $p=2$ . Thus, there will be $n-p$ degrees of freedom, where n is the number of categories.

The degrees of freedom are not based on the number of observations as with a Student's t or F-distribution. For example, if testing for a fair, six-sided die, there would be five degrees of freedom because there are six categories or parameters (each number); the number of times the die is rolled does not influence the number of degrees of freedom.

### Calculating the test-statistic

| Degrees of freedom | Probability less than the critical value |   |   |   |   |
|---|---|---|---|---|---|
| 0.90 | 0.95 | 0.975 | 0.99 | 0.999 |   |
| 1 | 2.706 | 3.841 | 5.024 | 6.635 | 10.828 |
| 2 | 4.605 | 5.991 | 7.378 | 9.210 | 13.816 |
| 3 | 6.251 | 7.815 | 9.348 | 11.345 | 16.266 |
| 4 | 7.779 | 9.488 | 11.143 | 13.277 | 18.467 |
| 5 | 9.236 | 11.070 | 12.833 | 15.086 | 20.515 |
| 6 | 10.645 | 12.592 | 14.449 | 16.812 | 22.458 |
| 7 | 12.017 | 14.067 | 16.013 | 18.475 | 24.322 |
| 8 | 13.362 | 15.507 | 17.535 | 20.090 | 26.125 |
| 9 | 14.684 | 16.919 | 19.023 | 21.666 | 27.877 |
| 10 | 15.987 | 18.307 | 20.483 | 23.209 | 29.588 |
| 11 | 17.275 | 19.675 | 21.920 | 24.725 | 31.264 |
| 12 | 18.549 | 21.026 | 23.337 | 26.217 | 32.910 |
| 13 | 19.812 | 22.362 | 24.736 | 27.688 | 34.528 |
| 14 | 21.064 | 23.685 | 26.119 | 29.141 | 36.123 |
| 15 | 22.307 | 24.996 | 27.488 | 30.578 | 37.697 |
| 16 | 23.542 | 26.296 | 28.845 | 32.000 | 39.252 |
| 17 | 24.769 | 27.587 | 30.191 | 33.409 | 40.790 |
| 18 | 25.989 | 28.869 | 31.526 | 34.805 | 42.312 |
| 19 | 27.204 | 30.144 | 32.852 | 36.191 | 43.820 |
| 20 | 28.412 | 31.410 | 34.170 | 37.566 | 45.315 |
| 21 | 29.615 | 32.671 | 35.479 | 38.932 | 46.797 |
| 22 | 30.813 | 33.924 | 36.781 | 40.289 | 48.268 |
| 23 | 32.007 | 35.172 | 38.076 | 41.638 | 49.728 |
| 24 | 33.196 | 36.415 | 39.364 | 42.980 | 51.179 |
| 25 | 34.382 | 37.652 | 40.646 | 44.314 | 52.620 |
| 26 | 35.563 | 38.885 | 41.923 | 45.642 | 54.052 |
| 27 | 36.741 | 40.113 | 43.195 | 46.963 | 55.476 |
| 28 | 37.916 | 41.337 | 44.461 | 48.278 | 56.892 |
| 29 | 39.087 | 42.557 | 45.722 | 49.588 | 58.301 |
| 30 | 40.256 | 43.773 | 46.979 | 50.892 | 59.703 |
| 31 | 41.422 | 44.985 | 48.232 | 52.191 | 61.098 |
| 32 | 42.585 | 46.194 | 49.480 | 53.486 | 62.487 |
| 33 | 43.745 | 47.400 | 50.725 | 54.776 | 63.870 |
| 34 | 44.903 | 48.602 | 51.966 | 56.061 | 65.247 |
| 35 | 46.059 | 49.802 | 53.203 | 57.342 | 66.619 |
| 36 | 47.212 | 50.998 | 54.437 | 58.619 | 67.985 |
| 37 | 48.363 | 52.192 | 55.668 | 59.893 | 69.347 |
| 38 | 49.513 | 53.384 | 56.896 | 61.162 | 70.703 |
| 39 | 50.660 | 54.572 | 58.120 | 62.428 | 72.055 |
| 40 | 51.805 | 55.758 | 59.342 | 63.691 | 73.402 |
| 41 | 52.949 | 56.942 | 60.561 | 64.950 | 74.745 |
| 42 | 54.090 | 58.124 | 61.777 | 66.206 | 76.084 |
| 43 | 55.230 | 59.304 | 62.990 | 67.459 | 77.419 |
| 44 | 56.369 | 60.481 | 64.201 | 68.710 | 78.750 |
| 45 | 57.505 | 61.656 | 65.410 | 69.957 | 80.077 |
| 46 | 58.641 | 62.830 | 66.617 | 71.201 | 81.400 |
| 47 | 59.774 | 64.001 | 67.821 | 72.443 | 82.720 |
| 48 | 60.907 | 65.171 | 69.023 | 73.683 | 84.037 |
| 49 | 62.038 | 66.339 | 70.222 | 74.919 | 85.351 |
| 50 | 63.167 | 67.505 | 71.420 | 76.154 | 86.661 |
| 51 | 64.295 | 68.669 | 72.616 | 77.386 | 87.968 |
| 52 | 65.422 | 69.832 | 73.810 | 78.616 | 89.272 |
| 53 | 66.548 | 70.993 | 75.002 | 79.843 | 90.573 |
| 54 | 67.673 | 72.153 | 76.192 | 81.069 | 91.872 |
| 55 | 68.796 | 73.311 | 77.380 | 82.292 | 93.168 |
| 56 | 69.919 | 74.468 | 78.567 | 83.513 | 94.461 |
| 57 | 71.040 | 75.624 | 79.752 | 84.733 | 95.751 |
| 58 | 72.160 | 76.778 | 80.936 | 85.950 | 97.039 |
| 59 | 73.279 | 77.931 | 82.117 | 87.166 | 98.324 |
| 60 | 74.397 | 79.082 | 83.298 | 88.379 | 99.607 |
| 61 | 75.514 | 80.232 | 84.476 | 89.591 | 100.888 |
| 62 | 76.630 | 81.381 | 85.654 | 90.802 | 102.166 |
| 63 | 77.745 | 82.529 | 86.830 | 92.010 | 103.442 |
| 64 | 78.860 | 83.675 | 88.004 | 93.217 | 104.716 |
| 65 | 79.973 | 84.821 | 89.177 | 94.422 | 105.988 |
| 66 | 81.085 | 85.965 | 90.349 | 95.626 | 107.258 |
| 67 | 82.197 | 87.108 | 91.519 | 96.828 | 108.526 |
| 68 | 83.308 | 88.250 | 92.689 | 98.028 | 109.791 |
| 69 | 84.418 | 89.391 | 93.856 | 99.228 | 111.055 |
| 70 | 85.527 | 90.531 | 95.023 | 100.425 | 112.317 |
| 71 | 86.635 | 91.670 | 96.189 | 101.621 | 113.577 |
| 72 | 87.743 | 92.808 | 97.353 | 102.816 | 114.835 |
| 73 | 88.850 | 93.945 | 98.516 | 104.010 | 116.092 |
| 74 | 89.956 | 95.081 | 99.678 | 105.202 | 117.346 |
| 75 | 91.061 | 96.217 | 100.839 | 106.393 | 118.599 |
| 76 | 92.166 | 97.351 | 101.999 | 107.583 | 119.850 |
| 77 | 93.270 | 98.484 | 103.158 | 108.771 | 121.100 |
| 78 | 94.374 | 99.617 | 104.316 | 109.958 | 122.348 |
| 79 | 95.476 | 100.749 | 105.473 | 111.144 | 123.594 |
| 80 | 96.578 | 101.879 | 106.629 | 112.329 | 124.839 |
| 81 | 97.680 | 103.010 | 107.783 | 113.512 | 126.083 |
| 82 | 98.780 | 104.139 | 108.937 | 114.695 | 127.324 |
| 83 | 99.880 | 105.267 | 110.090 | 115.876 | 128.565 |
| 84 | 100.980 | 106.395 | 111.242 | 117.057 | 129.804 |
| 85 | 102.079 | 107.522 | 112.393 | 118.236 | 131.041 |
| 86 | 103.177 | 108.648 | 113.544 | 119.414 | 132.277 |
| 87 | 104.275 | 109.773 | 114.693 | 120.591 | 133.512 |
| 88 | 105.372 | 110.898 | 115.841 | 121.767 | 134.746 |
| 89 | 106.469 | 112.022 | 116.989 | 122.942 | 135.978 |
| 90 | 107.565 | 113.145 | 118.136 | 124.116 | 137.208 |
| 91 | 108.661 | 114.268 | 119.282 | 125.289 | 138.438 |
| 92 | 109.756 | 115.390 | 120.427 | 126.462 | 139.666 |
| 93 | 110.850 | 116.511 | 121.571 | 127.633 | 140.893 |
| 94 | 111.944 | 117.632 | 122.715 | 128.803 | 142.119 |
| 95 | 113.038 | 118.752 | 123.858 | 129.973 | 143.344 |
| 96 | 114.131 | 119.871 | 125.000 | 131.141 | 144.567 |
| 97 | 115.223 | 120.990 | 126.141 | 132.309 | 145.789 |
| 98 | 116.315 | 122.108 | 127.282 | 133.476 | 147.010 |
| 99 | 117.407 | 123.225 | 128.422 | 134.642 | 148.230 |
| 100 | 118.498 | 124.342 | 129.561 | 135.807 | 149.449 |

The value of the test-statistic is

$\chi ^{2}=\sum _{i=1}^{n}{\frac {{\left(O_{i}-E_{i}\right)}^{2}}{E_{i}}}=N\sum _{i=1}^{n}{\frac {\left(O_{i}/N-p_{i}\right)^{2}}{p_{i}}}$

where

- $\chi ^{2}$ = Pearson's cumulative test statistic, which asymptotically approaches a $\chi ^{2}$ distribution.
- $O_{i}$ = the number of observations of type *i*.
- N = total number of observations
- $E_{i}=Np_{i}$ = the expected (theoretical) count of type *i*, asserted by the null hypothesis that the fraction of type *i* in the population is $p_{i}$
- n = the number of cells in the table.

The chi-squared statistic can then be used to calculate a p-value by comparing the value of the statistic to a chi-squared distribution. The number of degrees of freedom is equal to the number of cells n , minus the reduction in degrees of freedom, p .

The chi-squared statistic can be also calculated as

$\chi ^{2}=\sum _{i=1}^{n}{\frac {O_{i}^{2}}{E_{i}}}-N.$

This result is the consequence of the Binomial theorem.

The result about the numbers of degrees of freedom is valid when the original data are multinomial and hence the estimated parameters are efficient for minimizing the chi-squared statistic. More generally however, when maximum likelihood estimation does not coincide with minimum chi-squared estimation, the distribution will lie somewhere between a chi-squared distribution with $n-1-p$ and $n-1$ degrees of freedom (See for instance Chernoff and Lehmann, 1954).

The chi-squared test indicates a statistically significant association between the level of education completed and routine check-up attendance (chi2(3) = 14.6090, p = 0.002). The proportions suggest that as the level of education increases, so does the proportion of individuals attending routine check-ups. Specifically, individuals who have graduated from college or university attend routine check-ups at a higher proportion (31.52%) compared to those who have not graduated high school (8.44%). This finding may suggest that higher educational attainment is associated with a greater likelihood of engaging in health-promoting behaviors such as routine check-ups.

### Bayesian method

In Bayesian statistics, one would instead use a Dirichlet distribution as conjugate prior. If one took a uniform prior, then the maximum likelihood estimate for the population probability is the observed probability, and one may compute a credible region around this or another estimate.

## Testing for statistical independence

In this case, an "observation" consists of the values of two outcomes and the null hypothesis is that the occurrence of these outcomes is statistically independent. Each observation is allocated to one cell of a two-dimensional array of cells (called a contingency table) according to the values of the two outcomes. If there are *r* rows and *c* columns in the table, the "theoretical frequency" for a cell, given the hypothesis of independence, is

$E_{i,j}=Np_{i\cdot }p_{\cdot j},$

where N is the total sample size (the sum of all cells in the table), and

$p_{i\cdot }={\frac {O_{i\cdot }}{N}}=\sum _{j=1}^{c}{\frac {O_{i,j}}{N}},$

is the fraction of observations of type *i* ignoring the column attribute (fraction of row totals), and $p_{\cdot j}={\frac {O_{\cdot j}}{N}}=\sum _{i=1}^{r}{\frac {O_{i,j}}{N}}$

is the fraction of observations of type *j* ignoring the row attribute (fraction of column totals). The term "frequencies" refers to absolute numbers rather than already normalized values.

The value of the test-statistic is

${\begin{aligned}\chi ^{2}&=\sum _{i=1}^{r}\sum _{j=1}^{c}{\frac {{\left(O_{i,j}-E_{i,j}\right)}^{2}}{E_{i,j}}}\\[1ex]&=N\sum _{i,j}p_{i\cdot }p_{\cdot j}{\left({\frac {\left(O_{i,j}/N\right)-p_{i\cdot }p_{\cdot j}}{p_{i\cdot }p_{\cdot j}}}\right)}^{2}\end{aligned}}$

Note that $\chi ^{2}$ is 0 if and only if $O_{i,j}=E_{i,j}\forall i,j$ , i.e. only if the expected and true number of observations are equal in all cells.

Fitting the model of "independence" reduces the number of degrees of freedom by *p* = *r* + *c* − 1. The number of degrees of freedom is equal to the number of cells *rc*, minus the reduction in degrees of freedom, *p*, which reduces to (*r* − 1)(*c* − 1).

For the test of independence, also known as the test of homogeneity, a chi-squared probability of less than or equal to 0.05 (or the chi-squared statistic being at or larger than the 0.05 critical point) is commonly interpreted by applied workers as justification for rejecting the null hypothesis that the row variable is independent of the column variable. The alternative hypothesis corresponds to the variables having an association or relationship where the structure of this relationship is not specified.

## Assumptions

The chi-squared test, when used with the standard approximation that a chi-squared distribution is applicable, has the following assumptions:

**Simple random sample**

The sample data is a random sampling from a fixed distribution or population where every collection of members of the population of the given sample size has an equal probability of selection. Variants of the test have been developed for complex samples, such as where the data is weighted. Other forms can be used such as

purposive sampling

.

**Sample size (whole table)**

A sample with a sufficiently large size is assumed. If a chi squared test is conducted on a sample with a smaller size, then the chi squared test will yield an inaccurate inference. The researcher, by using chi squared test on small samples, might end up committing a

Type II error

. For small sample sizes the

Cash test

is preferred.

**Expected cell count**

Adequate expected cell counts. Some require 5 or more, and others require 10 or more. A common rule is 5 or more in all cells of a 2-by-2 table, and 5 or more in 80% of cells in larger tables, but no cells with zero expected count. When this assumption is not met,

Yates's correction

is applied.

**Independence**

The observations are always assumed to be independent of each other. This means chi-squared cannot be used to test correlated data (like matched pairs or panel data). In those cases,

McNemar's test

may be more appropriate.

A test that relies on different assumptions is Fisher's exact test; if its assumption of fixed marginal distributions is met it is substantially more accurate in obtaining a significance level, especially with few observations. In the vast majority of applications this assumption will not be met, and Fisher's exact test will be over conservative and not have correct coverage.

## Derivation

Derivation using central limit theorem

The null distribution of the Pearson statistic with *j* rows and *k* columns is approximated by the chi-squared distribution with (*k* − 1)(*j* − 1) degrees of freedom.

This approximation arises as the true distribution, under the null hypothesis, if the expected value is given by a multinomial distribution. For large sample sizes, the central limit theorem says this distribution tends toward a certain multivariate normal distribution.

### Two cells

In the special case where there are only two cells in the table, the expected values follow a binomial distribution, $O\sim \operatorname {Bin} (n,p),$ where

p

= probability, under the null hypothesis,

n

= number of observations in the sample.

In the above example the hypothesised probability of a male observation is 0.5, with 100 samples. Thus we expect to observe 50 males.

If *n* is sufficiently large, the above binomial distribution may be approximated by a Gaussian (normal) distribution and thus the Pearson test statistic approximates a chi-squared distribution, $\operatorname {Bin} (n,p)\approx {\mathcal {N}}{\big (}np,np(1-p){\big )}.$

Let *O*1 be the number of observations from the sample that are in the first cell. The Pearson test statistic can be expressed as ${\frac {(O_{1}-np)^{2}}{np}}+{\frac {{\big (}n-O_{1}-n(1-p){\big )}^{2}}{n(1-p)}},$ which can in turn be expressed as $\left({\frac {O_{1}-np}{\sqrt {np(1-p)}}}\right)^{2}.$

By the normal approximation to a binomial, this is the squared of one standard normal variate, and hence is distributed as chi-squared with 1 degree of freedom. Note that the denominator is one standard deviation of the Gaussian approximation, so can be written ${\frac {(O_{1}-\mu )^{2}}{\sigma ^{2}}}.$

So as consistent with the meaning of the chi-squared distribution, we are measuring how probable the observed number of standard deviations away from the mean is under the Gaussian approximation (which is a good approximation for large *n*).

The chi-squared distribution is then integrated on the right of the statistic value to obtain the *p*-value, which is equal to the probability of getting a statistic equal or bigger than the observed one, assuming the null hypothesis.

### Two-by-two contingency tables

When the test is applied to a contingency table containing two rows and two columns, the test is equivalent to a *Z*-test of proportions.

### Many cells

Broadly similar arguments as above lead to the desired result, though the details are more involved. One may apply an orthogonal change of variables to turn the limiting summands in the test statistic into one fewer squares of i.i.d. standard normal random variables.

Let us now prove that the distribution indeed approaches asymptotically the $\chi ^{2}$ distribution as the number of observations approaches infinity.

Let n be the number of observations, m the number of cells and $p_{i}$ the probability of an observation to fall in the *i*-th cell, for $1\leq i\leq m$ . We denote by $\{k_{i}\}$ the configuration where for each *i* there are $k_{i}$ observations in the *i*-th cell. Note that $\sum _{i=1}^{m}k_{i}=n\quad {\text{and}}\quad \sum _{i=1}^{m}p_{i}=1.$

Let $\chi _{P}^{2}(\{k_{i}\},\{p_{i}\})$ be Pearson's cumulative test statistic for such a configuration, and let $\chi _{P}^{2}(\{p_{i}\})$ be the distribution of this statistic. We will show that the latter probability approaches the $\chi ^{2}$ distribution with $m-1$ degrees of freedom, as $n\to \infty .$

For any arbitrary value T: $P{\big (}\chi _{P}^{2}(\{p_{i}\})>T{\big )}=\sum _{\{k_{i}\mid \chi _{P}^{2}(\{k_{i}\},\{p_{i}\})>T\}}{\frac {n!}{k_{1}!\cdots k_{m}!}}\prod _{i=1}^{m}{p_{i}}^{k_{i}}.$

We will use a procedure similar to the approximation in de Moivre–Laplace theorem. Contributions from small $k_{i}$ are of subleading order in n and thus for large n we may use Stirling's formula for both $n!$ and $k_{i}!$ to get the following: $P{\big (}\chi _{P}^{2}(\{p_{i}\})>T{\big )}\sim \sum _{\{k_{i}\mid \chi _{P}^{2}(\{k_{i}\},\{p_{i}\})>T\}}\prod _{i=1}^{m}\left({\frac {np_{i}}{k_{i}}}\right)^{k_{i}}{\sqrt {\frac {2\pi n}{\prod _{i=1}^{m}2\pi k_{i}}}}.$

By substituting for $x_{i}={\frac {k_{i}-np_{i}}{\sqrt {n}}},\quad i=1,\cdots ,m-1,$ we may approximate for large n the sum over the $k_{i}$ by an integral over the $x_{i}$ . Noting that $k_{m}=np_{m}-{\sqrt {n}}\sum _{i=1}^{m-1}x_{i},$ we arrive at ${\begin{aligned}P{\big (}\chi _{P}^{2}(\{p_{i}\}{\big )}>T)&\sim {\sqrt {\frac {2\pi n}{\prod _{i=1}^{m}2\pi k_{i}}}}\int _{\Omega }\left[\prod _{i=1}^{m-1}{\sqrt {n}}dx_{i}\right]\times \\&\qquad \times \left\{\prod _{i=1}^{m-1}\left(1+{\frac {x_{i}}{{\sqrt {n}}p_{i}}}\right)^{-(np_{i}+{\sqrt {n}}x_{i})}\left(1-{\frac {\sum _{i=1}^{m-1}x_{i}}{{\sqrt {n}}p_{m}}}\right)^{-\left(np_{m}-{\sqrt {n}}\sum _{i=1}^{m-1}x_{i}\right)}\right\}\\&={\sqrt {\frac {2\pi n}{\prod _{i=1}^{m}\left(2\pi np_{i}+2\pi {\sqrt {n}}x_{i}\right)}}}\int _{\Omega }\left\{\prod _{i=1}^{m-1}{{\sqrt {n}}dx_{i}}\right\}\times \\&\qquad \times \left\{\prod _{i=1}^{m-1}\exp \left[-\left(np_{i}+{\sqrt {n}}x_{i}\right)\ln \left(1+{\frac {x_{i}}{{\sqrt {n}}p_{i}}}\right)\right]\exp \left[-\left(np_{m}-{\sqrt {n}}\sum _{i=1}^{m-1}x_{i}\right)\ln \left(1-{\frac {\sum _{i=1}^{m-1}x_{i}}{{\sqrt {n}}p_{m}}}\right)\right]\right\},\end{aligned}}$ where $\Omega$ is the set defined through $\chi _{P}^{2}(\{k_{i}\},\{p_{i}\})=\chi _{P}^{2}(\{{\sqrt {n}}x_{i}+np_{i}\},\{p_{i}\})>T$ .

By expanding the logarithm and taking the leading terms in n , we get $P{\big (}\chi _{P}^{2}(\{p_{i}\})>T{\big )}\sim {\frac {1}{\sqrt {(2\pi )^{m-1}\prod _{i=1}^{m}p_{i}}}}\int _{\Omega }\left[\prod _{i=1}^{m-1}dx_{i}\right]\prod _{i=1}^{m-1}\exp \left[-{\frac {1}{2}}\sum _{i=1}^{m-1}{\frac {x_{i}^{2}}{p_{i}}}-{\frac {1}{2p_{m}}}\left(\sum _{i=1}^{m-1}x_{i}\right)^{2}\right].$

Pearson's chi, $\chi _{P}^{2}(\{k_{i}\},\{p_{i}\})=\chi _{P}^{2}(\{{\sqrt {n}}x_{i}+np_{i}\},\{p_{i}\})$ , is precisely the argument of the exponent (except for the −1/2; note that the final term in the exponent's argument is equal to $(k_{m}-np_{m})^{2}/(np_{m})$ ).

This argument can be written as $-{\frac {1}{2}}\sum _{i,j=1}^{m-1}x_{i}A_{ij}x_{j},\quad A_{ij}={\frac {\delta _{ij}}{p_{i}}}+{\frac {1}{p_{m}}},\quad i,j=1,\cdots ,m-1.$

A is a regular symmetric $(m-1)\times (m-1)$ matrix, and hence diagonalizable. It is therefore possible to make a linear change of variables in $\{x_{i}\}$ so as to get $m-1$ new variables $\{y_{i}\}$ so that $\sum _{i,j=1}^{m-1}x_{i}A_{ij}x_{j}=\sum _{i=1}^{m-1}y_{i}^{2}.$

This linear change of variables merely multiplies the integral by a constant Jacobian, so we get $P{\big (}\chi _{P}^{2}(\{p_{i}\})>T{\big )}\sim C\int _{\sum _{i=1}^{m-1}y_{i}^{2}>T}\left\{\prod _{i=1}^{m-1}dy_{i}\right\}\prod _{i=1}^{m-1}\exp \left[-{\frac {1}{2}}\left(\sum _{i=1}^{m-1}y_{i}^{2}\right)\right],$ where *C* is a constant.

This is the probability that squared sum of $m-1$ independent normally distributed variables of zero mean and unit variance will be greater than *T*, namely that $\chi ^{2}$ with $m-1$ degrees of freedom is larger than *T*.

We have thus shown that at the limit where $n\to \infty ,$ the distribution of Pearson's chi approaches the chi distribution with $m-1$ degrees of freedom.

An alternative derivation is on the multinomial distribution page.

## Examples

### Fairness of dice

A 6-sided die is thrown 60 times. The number of times it lands with 1, 2, 3, 4, 5 and 6 face up is 5, 8, 9, 8, 10 and 20, respectively. Is the die biased, according to the Pearson's chi-squared test at a significance level of 95% and/or 99%?

The null hypothesis is that the die is unbiased, hence each number is expected to occur the same number of times, in this case, ⁠60/*n*⁠ = 10. The outcomes can be tabulated as follows:

| i | $O_{i}$ | $E_{i}$ | $O_{i}-E_{i}$ | $(O_{i}-E_{i})^{2}$ |
|---|---|---|---|---|
| 1 | 5 | 10 | −5 | 25 |
| 2 | 8 | 10 | −2 | 4 |
| 3 | 9 | 10 | −1 | 1 |
| 4 | 8 | 10 | −2 | 4 |
| 5 | 10 | 10 | 0 | 0 |
| 6 | 20 | 10 | 10 | 100 |
| Sum | 134 |   |   |   |

We then consult an *Upper-tail critical values of chi-square distribution* table, the tabular value refers to the sum of the squared variables each divided by the expected outcomes. For the present example, this means $\chi ^{2}={\frac {25}{10}}+{\frac {4}{10}}+{\frac {1}{10}}+{\frac {4}{10}}+{\frac {0}{10}}+{\frac {100}{10}}=13.4.$

This is the experimental result whose unlikeliness (with a fair die) we wish to estimate.

| Degrees of freedom | Probability less than the critical value |   |   |   |   |
|---|---|---|---|---|---|
| 0.90 | *0.95* | 0.975 | *0.99* | 0.999 |   |
| 5 | 9.236 | 11.070 | 12.833 | 15.086 | 20.515 |

The experimental sum of 13.4 is between the critical values of 97.5% and 99% significance or confidence (p-value). Specifically, getting 20 rolls of 6, when the expectation is only 10 such values, is unlikely with a fair die.

### Chi-squared goodness of fit test

In this context, the frequencies of both theoretical and empirical distributions are unnormalised counts, and for a chi-squared test the total sample sizes N of both these distributions (sums of all cells of the corresponding contingency tables) have to be the same.

For example, to test the hypothesis that a random sample of 100 people has been drawn from a population in which men and women are equal in frequency, the observed number of men and women would be compared to the theoretical frequencies of 50 men and 50 women. If there were 44 men in the sample and 56 women, then

$\chi ^{2}={\frac {{\left(44-50\right)}^{2}}{50}}+{\frac {{\left(56-50\right)}^{2}}{50}}=1.44.$

If the null hypothesis is true (i.e., men and women are chosen with equal probability), the test statistic will be drawn from a chi-squared distribution with one degree of freedom (because if the male frequency is known, then the female frequency is determined).

Consultation of the chi-squared distribution for 1 degree of freedom shows that the probability of observing this difference (or a more extreme difference than this) if men and women are equally numerous in the population is approximately 0.23. This probability is higher than conventional criteria for statistical significance (0.01 or 0.05), so normally we would not reject the null hypothesis that the number of men in the population is the same as the number of women (i.e., we would consider our sample within the range of what we would expect for a 50/50 male–female ratio.)

### Chi-squared test for homogeneity

The chi-squared test for homogeneity of proportions (that is, comparing proportions across groups in a contingency table) is frequently used to verify if the rows of a given nonnegative $m\times n$ contingency matrix A are proportional.

Consider T outcomes of multinomial trials classified according to two criteria: membership in one of n groups and assignment to one of m categories. The outcomes may be arranged in an $m\times n$ contingency table, where $O_{ij}$ denotes the observed frequency in row i and column j , with row totals $O_{i\cdot }$ , column totals $O_{\cdot j}$ and grand total T .

Let $O_{ij}$ denote the observed frequency in the cell corresponding to row i and column j , for $i=1,2,\dots ,m$ and $j=1,2,\dots ,n$ . Define the row sums

$R_{i}=\sum _{j=1}^{n}O_{ij},\quad i=1,\dots ,m,$

the column sums

$C_{j}=\sum _{i=1}^{m}O_{ij},\quad j=1,\dots ,n,$

and the grand total

$T=\sum _{i=1}^{m}\sum _{j=1}^{n}O_{ij}.$

The null hypothesis is

$H_{0}:\pi _{1j}=\pi _{2j}=\cdots =\pi _{mj},\quad \forall j\in {1,\dots ,n},$

where $\pi _{ij}\in [0,1]$ denotes the proportion of individuals in group i falling into category j , with $\sum _{j=1}^{n}\pi _{ij}=1$ for each i .

Under $H_{0}$ , the expected frequency in cell $(i,j)$ is

$E_{ij}={\tfrac {R_{i}C_{j}}{T}},\quad i=1,\dots ,m;;j=1,\dots ,n.$

The Pearson chi-squared test statistic is then

$\chi _{\text{stat}}^{2}=\sum _{i=1}^{m}\sum _{j=1}^{n}{\frac {(O_{ij}-E_{ij})^{2}}{E_{ij}}}.$

For example, suppose there are two groups of students (Group 1 and Group 2) and three study preferences (Alone, With peers, Tutoring). Let $O_{ij}$ denote the observed frequency in row i (preference) and column j (group).

The observed frequencies are as follows:

| Preference | Group 1 | Group 2 | Row total |
|---|---|---|---|
| Alone | 12 | 8 | 20 |
| With peers | 18 | 22 | 40 |
| Tutoring | 10 | 30 | 40 |
| Column total | 40 | 60 | 100 |

Under the null hypothesis $H_{0}$ , the rows are proportional across groups.

The expected frequencies are computed using:

$E_{ij}={\frac {R_{i}\cdot C_{j}}{T}},$

where $R_{i}$ is the row total, $C_{j}$ is the column total, and T is the grand total.

For example, for the first row and first column:

$E_{11}={\frac {20\cdot 40}{100}}=8.$

The expected frequencies are:

| Preference | Group 1 | Group 2 |
|---|---|---|
| Alone | 8 | 12 |
| With peers | 16 | 24 |
| Tutoring | 16 | 24 |

The Pearson chi-squared statistic is then:

$\chi _{\text{stat}}^{2}=\sum _{i=1}^{3}\sum _{j=1}^{2}{\frac {(O_{ij}-E_{ij})^{2}}{E_{ij}}}=7.5.$

With $(3-1)(2-1)=2$ degrees of freedom, this value can be compared to the chi-squared distribution to test the null hypothesis.

## Pitfalls of the test

The approximation to the chi-squared distribution breaks down if expected frequencies are too low.

It will normally be acceptable so long as no more than 20% of the events have expected frequencies below 5. Where there is only 1 degree of freedom, the approximation is not reliable if expected frequencies are below 10. In this case, a better approximation can be obtained by reducing the absolute value of each difference between observed and expected frequencies by 0.5 before squaring; this is called Yates's correction for continuity.

In cases where the expected value, E, is found to be small (indicating a small underlying population probability, and/or a small number of observations), the normal approximation of the multinomial distribution can fail, and in such cases it is found to be more appropriate to use the G-test, a likelihood ratio-based test statistic. When the total sample size is small, it is necessary to use an appropriate exact test, typically either the binomial test or, for contingency tables, Fisher's exact test. This test uses the conditional distribution of the test statistic given the marginal totals, and thus assumes that the margins were determined before the study; alternatives such as Boschloo's test which do not make this assumption are uniformly more powerful.

In Pearson's test of homogeneity, if all entries of a matrix A are multiplied by a positive constant c , the Pearson chi-squared statistic is also multiplied by c :

$\chi _{\text{stat}}^{2}(cA)=c\chi _{\text{stat}}^{2}(A).$

Therefore, if all rows of A are exactly proportional,

$\chi _{\text{stat}}^{2}(cA)=c\chi _{\text{stat}}^{2}(A)=0$

for any c and any significance level $\alpha$ . Otherwise, $\chi _{\text{stat}}^{2}(cA)$ can become arbitrarily large or small as c increases or decreases. Hence, at a fixed significance level $\alpha$ , the null hypothesis $H_{0}$ will be rejected with confidence $1-\alpha$ when c is sufficiently large, and not rejected when c is sufficiently small. That is, the chi-squared statistic increases linearly when the entire contingency table is multiplied by a constant factor, reflecting the proportional scaling of observed and expected frequencies.

It can be shown that the $\chi ^{2}$ test is a low order approximation of the $\Psi$ test. The above reasons for the above issues become apparent when the higher order terms are investigated.

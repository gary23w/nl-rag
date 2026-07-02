---
title: "Exact test"
source: https://en.wikipedia.org/wiki/Exact_test
domain: fishers-exact-test
license: CC-BY-SA-4.0
tags: Fisher exact test, hypergeometric distribution, Barnard test, exact test
fetched: 2026-07-02
---

# Exact test

An **exact (significance) test** is a statistical test such that if the null hypothesis is true, then all assumptions made during the derivation of the distribution of the test statistic are met. Using an exact test provides a significance test that maintains the type I error rate of the test ( $\alpha$ ) at the desired significance level of the test. For example, an exact test at a significance level of $\alpha =5\%$ , when repeated over many samples where the null hypothesis is true, will reject at most $5\%$ of the time. This is in contrast to an *approximate test* in which the desired type I error rate is only approximately maintained (i.e.: the test might reject > 5% of the time), while this approximation may be made as close to $\alpha$ as desired by making the sample size sufficiently large.

Exact tests that are based on discrete test statistics may be conservative, indicating that the actual rejection rate lies below the nominal significance level $\alpha$ . As an example, this is the case for Fisher's exact test and its more powerful alternative, Boschloo's test. If the test statistic is continuous, it will reach the significance level exactly.

Parametric tests, such as those used in exact statistics, are exact tests when the parametric assumptions are fully met, but in practice, the use of the term *exact* (significance) *test* is reserved for non-parametric tests, i.e., tests that do not rest on parametric assumptions. However, in practice, most implementations of non-parametric test software use asymptotical algorithms to obtain the significance value, which renders the test non-exact.

Hence, when a result of statistical analysis is termed an “exact test” or specifies an “exact p-value”, this implies that the test is defined without parametric assumptions and is evaluated without making use of approximate algorithms. In principle, however, this could also signify that a parametric test has been employed in a situation where all parametric assumptions are fully met, but it is in most cases impossible to prove this completely in a real-world situation. Exceptions in which it is certain that parametric tests are exact include tests based on the binomial or Poisson distributions. The term permutation test is sometimes used as a synonym for exact test, but it should be kept in mind that all permutation tests are exact tests, but not all exact tests are permutation tests.

## Formulation

The basic equation underlying exact tests is

$\Pr({\text{exact}})=\sum _{\mathbf {y} \,:\,T(\mathbf {y} )\geq T(\mathbf {x)} }\Pr(\mathbf {y} )$

where:

- **x** is the actual observed outcome,
- Pr(**y**) is the probability under the null hypothesis of a potentially observed outcome **y**,
- *T*(**y**) is the value of the test statistic for an outcome **y**, with larger values of *T* representing cases which notionally represent greater departures from the null hypothesis,

and where the sum ranges over all outcomes **y** (including the observed one) that have the same value of the test statistic obtained for the observed sample **x**, or a larger one.

## Example: Pearson's chi-squared test versus an exact test

A simple example of this concept involves the observation that Pearson's chi-squared test is an approximate test. Suppose Pearson's chi-squared test is used to ascertain whether a six-sided die is "fair", indicating that it renders each of the six possible outcomes equally often. If the die is thrown *n* times, then one "expects" to see each outcome *n*/6 times. The test statistic is

$\sum {\frac {({\text{observed}}-{\text{expected}})^{2}}{\text{expected}}}=\sum _{k=1}^{6}{\frac {(X_{k}-n/6)^{2}}{n/6}},$

where *X**k* is the number of times outcome *k* is observed. If the null hypothesis of "fairness" is true, then the probability distribution of the test statistic can be made as close as desired to the chi-squared distribution with 5 degrees of freedom by making the sample size *n* sufficiently large. On the other hand, if *n* is small, then the probabilities based on chi-squared distributions may not be sufficiently close approximations. Finding the exact probability that this test statistic exceeds a certain value would then require a combinatorial enumeration of all outcomes of the experiment that gives rise to such a large value of the test statistic. It is then questionable whether the same test statistic ought to be used. A likelihood-ratio test might be preferred, and the test statistic might not be a monotone function of the one above.

## Example: Fisher's exact test

Fisher's exact test, based on the work of Ronald Fisher and E. J. G. Pitman in the 1930s, is exact because the sampling distribution (conditional on the marginals) is known exactly. This should be compared with Pearson's chi-squared test, which (although it tests the same null) is not exact because the distribution of the test statistic is only asymptotically correct.

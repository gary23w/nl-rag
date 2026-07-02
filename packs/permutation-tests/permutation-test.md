---
title: "Permutation test"
source: https://en.wikipedia.org/wiki/Permutation_test
domain: permutation-tests
license: CC-BY-SA-4.0
tags: permutation test, resampling method, exchangeability, randomization test
fetched: 2026-07-02
---

# Permutation test

A **permutation test** (also called re-randomization test or shuffle test) is an exact statistical hypothesis test. A permutation test involves two or more samples. The (possibly counterfactual) null hypothesis is that all samples come from the same distribution $H_{0}:F=G$ . Under the null hypothesis, the distribution of the test statistic is obtained by calculating all possible values of the test statistic under possible rearrangements of the observed data. Permutation tests are, therefore, a form of resampling.

Permutation tests can be understood as surrogate data testing where the surrogate data under the null hypothesis are obtained through permutations of the original data.

In other words, the method by which treatments are allocated to subjects in an experimental design is mirrored in the analysis of that design. If the labels are exchangeable under the null hypothesis, then the resulting tests yield exact significance levels; see also exchangeability. Confidence intervals can then be derived from the tests. The theory has evolved from the works of Ronald Fisher and E. J. G. Pitman in the 1930s.

Permutation tests should not be confused with randomized tests.

## Method

To illustrate the basic idea of a permutation test, suppose we collect random variables $X_{A}$ and $X_{B}$ for each individual from two groups A and B whose sample means are ${\bar {x}}_{A}$ and ${\bar {x}}_{B}$ , and that we want to know whether $X_{A}$ and $X_{B}$ come from the same distribution. Let $n_{A}$ and $n_{B}$ be the sample size collected from each group. The permutation test is designed to determine whether the observed difference between the sample means is large enough to reject, at some significance level, the null hypothesis H $_{0}$ that the data drawn from A is from the same distribution as the data drawn from B .

The test proceeds as follows. First, the difference in means between the two samples is calculated: this is the observed value of the test statistic, $T_{\text{obs}}$ .

Next, the observations of groups A and B are pooled, and the difference in sample means is calculated and recorded for every possible way of dividing the pooled values into two groups of size $n_{A}$ and $n_{B}$ (i.e., for every permutation of the group labels A and B). The set of these calculated differences is the exact distribution of possible differences (for this sample) under the null hypothesis that group labels are exchangeable (i.e., are randomly assigned).

The one-sided p-value of the test is calculated as the proportion of sampled permutations where the difference in means was greater than $T_{\text{obs}}$ . The two-sided p-value of the test is calculated as the proportion of sampled permutations where the absolute difference was greater than $|T_{\text{obs}}|$ . Many implementations of permutation tests require that the observed data itself be counted as one of the permutations so that the permutation p-value will never be zero.

Alternatively, if the only purpose of the test is to reject or not reject the null hypothesis, one could sort the recorded differences, and then observe if $T_{\text{obs}}$ is contained within the middle $(1-\alpha )\times 100$ % of them, for some significance level $\alpha$ . If it is not, we reject the hypothesis of identical probability curves at the $\alpha \times 100\%$ significance level.

To exploit variance reduction with paired samples, a paired permutation test must be applied, see paired difference test. This is equivalent to performing a normal, unpaired permutation test, but restricting the set of valid permutations to only those which respect the paired nature of the data by forbidding both halves of any pair from being included in the same partition. In the specific but common case where the test statistic is the mean, this is also equivalent to computing a single set of differences of each pair and iterating over all of the $2^{n}$ sign-reversals instead of the usual partitioning approach.

## Relation to parametric tests

Permutation tests are a subset of non-parametric statistics. Assuming that our experimental data come from data measured from two treatment groups, the method simply generates the distribution of mean differences under the assumption that the two groups are not distinct in terms of the measured variable. From this, one then uses the observed statistic ( $T_{\text{obs}}$ above) to see to what extent this statistic is special, i.e., the likelihood of observing the magnitude of such a value (or larger) if the treatment labels had simply been randomized after treatment.

In contrast to permutation tests, the distributions underlying many popular "classical" statistical tests, such as the *t*-test, *F*-test, *z*-test, and *χ*2 test, are obtained from theoretical probability distributions. Fisher's exact test is an example of a commonly used parametric test for evaluating the association between two dichotomous variables. When sample sizes are very large, the Pearson's chi-square test will give accurate results. For small samples, the chi-square reference distribution cannot be assumed to give a correct description of the probability distribution of the test statistic, and in this situation the use of Fisher's exact test becomes more appropriate.

Permutation tests exist in many situations where parametric tests do not (e.g., when deriving an optimal test when losses are proportional to the size of an error rather than its square). All simple and many relatively complex parametric tests have a corresponding permutation test version that is defined by using the same test statistic as the parametric test, but obtains the p-value from the sample-specific permutation distribution of that statistic, rather than from the theoretical distribution derived from the parametric assumption. For example, it is possible in this manner to construct a permutation *t*-test, a permutation ${\textstyle \chi ^{2}}$ test of association, a permutation version of Aly's test for comparing variances and so on.

The major drawbacks to permutation tests are that they

- Can be computationally intensive and may require "custom" code for difficult-to-calculate statistics. This must be rewritten for every case.
- Are primarily used to provide a p-value. The inversion of the test to get confidence regions/intervals requires even more computation.

## Advantages

Permutation tests exist for any test statistic, regardless of whether or not its distribution is known. Thus one is always free to choose the statistic which best discriminates between hypothesis and alternative and which minimizes losses.

Permutation tests can be used for analyzing unbalanced designs and for combining dependent tests on mixtures of categorical, ordinal, and metric data (Pesarin, 2001) . They can also be used to analyze qualitative data that has been quantitized (i.e., turned into numbers). Permutation tests may be ideal for analyzing quantitized data that do not satisfy statistical assumptions underlying traditional parametric tests (e.g., t-tests, ANOVA), see PERMANOVA.

Before the 1980s, the burden of creating the reference distribution was overwhelming except for data sets with small sample sizes.

Since the 1980s, the confluence of relatively inexpensive fast computers and the development of new sophisticated path algorithms applicable in special situations made the application of permutation test methods practical for a wide range of problems. It also initiated the addition of exact-test options in the main statistical software packages and the appearance of specialized software for performing a wide range of uni- and multi-variable exact tests and computing test-based "exact" confidence intervals.

## Limitations

An important assumption behind a permutation test is that the observations are exchangeable under the null hypothesis. An important consequence of this assumption is that tests of difference in location (like a permutation t-test) require equal variance under the normality assumption. In this respect, the classic permutation t-test shares the same weakness as the classical Student's t-test (the Behrens–Fisher problem). This can be addressed in the same way the classic t-test has been extended to handle unequal variances: by employing the Welch statistic with Satterthwaite adjustment to the degrees of freedom. A third alternative in this situation is to use a bootstrap-based test. Statistician Phillip Good explains the difference between permutation tests and bootstrap tests the following way: "Permutations test hypotheses concerning distributions; bootstraps test hypotheses concerning parameters. As a result, the bootstrap entails less-stringent assumptions." Bootstrap tests are not exact. In some cases, a permutation test based on a properly studentized statistic can be asymptotically exact even when the exchangeability assumption is violated. Bootstrap-based tests can test with the null hypothesis $H_{0}:F\neq G$ and, therefore, are suited for performing equivalence testing.

## Monte Carlo testing

An asymptotically equivalent permutation test can be created when there are too many possible orderings of the data to allow complete enumeration in a convenient manner. This is done by generating the reference distribution by Monte Carlo sampling, which takes a small (relative to the total number of permutations) random sample of the possible replicates. The realization that this could be applied to any permutation test on any dataset was an important breakthrough in the area of applied statistics. The earliest known references to this approach are Eden and Yates (1933) and Dwass (1957). This type of permutation test is known under various names: *approximate permutation test*, *Monte Carlo permutation tests* or *random permutation tests*.

After N random permutations, it is possible to obtain a confidence interval for the p-value based on the Binomial distribution, see Binomial proportion confidence interval. For example, if after $N=10000$ random permutations the p-value is estimated to be ${\widehat {p}}=0.05$ , then a 99% confidence interval for the true p (the one that would result from trying all possible permutations) is $\left[{\hat {p}}-z{\sqrt {\frac {0.05(1-0.05)}{10000}}},{\hat {p}}+z{\sqrt {\frac {0.05(1-0.05)}{10000}}}\right]=[0.045,0.055]$ .

On the other hand, the purpose of estimating the p-value is most often to decide whether $p\leq \alpha$ , where $\scriptstyle \ \alpha$ is the threshold at which the null hypothesis will be rejected (typically $\alpha =0.05$ ). In the example above, the confidence interval only tells us that there is roughly a 50% chance that the p-value is smaller than 0.05, i.e. it is completely unclear whether the null hypothesis should be rejected at a level $\alpha =0.05$ .

If it is only important to know whether $p\leq \alpha$ for a given $\alpha$ , it is logical to continue simulating until the statement $p\leq \alpha$ can be established to be true or false with a very low probability of error. Given a bound $\epsilon$ on the admissible probability of error (the probability of finding that ${\widehat {p}}>\alpha$ when in fact $p\leq \alpha$ or vice versa), the question of how many permutations to generate can be seen as the question of when to stop generating permutations, based on the outcomes of the simulations so far, in order to guarantee that the conclusion (which is either $p\leq \alpha$ or $p>\alpha$ ) is correct with probability at least as large as $1-\epsilon$ . ( $\epsilon$ will typically be chosen to be extremely small, e.g. 1/1000.) Stopping rules to achieve this have been developed which can be incorporated with minimal additional computational cost. In fact, depending on the true underlying p-value it will often be found that the number of simulations required is remarkably small (e.g. as low as 5 and often not larger than 100) before a decision can be reached with virtual certainty.

## Example tests

- Permutational analysis of variance
- Rank product

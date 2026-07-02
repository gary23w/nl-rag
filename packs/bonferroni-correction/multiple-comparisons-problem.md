---
title: "Multiple comparisons problem"
source: https://en.wikipedia.org/wiki/Multiple_comparisons_problem
domain: bonferroni-correction
license: CC-BY-SA-4.0
tags: Bonferroni correction, Holm Bonferroni, Sidak correction, union bound
fetched: 2026-07-02
---

# Multiple comparisons problem

**Multiple comparisons**, **multiplicity** or **multiple testing problem** occurs when many statistical tests are performed on the same dataset. Each test has its own chance of a Type I error (false positive), so the overall probability of making at least one false positive increases as the number of tests grows. In statistics, this occurs when one simultaneously considers a set of statistical inferences or estimates a subset of selected parameters based on observed values.

The probability of false positives is measured through the family-wise error rate (FWER). The larger the number of inferences made in a series of tests, the more likely erroneous inferences become. Several statistical techniques have been developed to compensate for the number of inferences being made—for example, by requiring a stricter significance threshold for individual comparisons.

## History

The problem of multiple comparisons received increased attention in the 1950s with the work of statisticians such as Tukey and Scheffé. Over the ensuing decades, many procedures were developed to address the problem. In 1996, the first international conference on multiple comparison procedures took place in Tel Aviv. Several researchers are active in this area, for example Emmanuel Candès and Vladimir Vovk.

## Definition

Multiple comparisons arise when a statistical analysis involves multiple simultaneous statistical tests, each of which has a potential to produce a "discovery". A stated confidence level generally applies only to each test considered individually, but often it is desirable to have a confidence level for the whole family of simultaneous tests. Failure to compensate for multiple comparisons can have important real-world consequences, as illustrated by the following examples:

- Suppose the treatment is a new way of teaching writing to students, and the control is the standard way of teaching writing. Students in the two groups can be compared in terms of grammar, spelling, organization, content, and so on. As more attributes are compared, it becomes increasingly likely that the treatment and control groups will appear to differ on at least one attribute due to random sampling error alone.
- Suppose we consider the efficacy of a drug in terms of the reduction of any one of a number of disease symptoms. As more symptoms are considered, it becomes increasingly likely that the drug will appear to be an improvement over existing drugs in terms of at least one symptom.

In both examples, as the number of comparisons increases, it becomes more likely that the groups being compared will appear to differ in terms of at least one attribute. Our confidence that a result will generalize to independent data should generally be weaker if it is observed as part of an analysis that involves multiple comparisons, rather than an analysis that involves only a single comparison.

For example, if one test is performed at the 5% level and the corresponding null hypothesis is true, there is only a 5% risk of incorrectly rejecting the null hypothesis. However, if 100 tests are each conducted at the 5% level and all corresponding null hypotheses are true, the expected number of incorrect rejections (also known as false positives or Type I errors) is 5. If the tests are statistically independent from each other (i.e. are performed on independent samples), the probability of at least one incorrect rejection is approximately 99.4%.

The multiple comparisons problem also applies to confidence intervals. A single confidence interval with a 95% coverage probability level will contain the true value of the parameter in 95% of samples. However, if one considers 100 confidence intervals simultaneously, each with 95% coverage probability, the expected number of non-covering intervals is 5. If the intervals are statistically independent from each other, the probability that at least one interval does not contain the population parameter is 99.4%.

Techniques have been developed to prevent the inflation of false positive rates and non-coverage rates that occur with multiple statistical tests.

### Classification of multiple hypothesis tests

The following table defines the possible outcomes when testing multiple null hypotheses. Suppose we have a number *m* of null hypotheses, denoted by: *H*1, *H*2, ..., *H**m*. Using a statistical test, we reject the null hypothesis if the test is declared significant. We do not reject the null hypothesis if the test is non-significant. Summing each type of outcome over all *Hi*  yields the following random variables:

|   | Null hypothesis is true (H0) | Alternative hypothesis is true (HA) | Total |
|---|---|---|---|
| Test is declared significant | V | S | R |
| Test is declared non-significant | U | T | $m-R$ |
| Total | $m_{0}$ | $m-m_{0}$ | m |

- m is the total number hypotheses tested
- $m_{0}$ is the number of true null hypotheses, an unknown parameter
- $m-m_{0}$ is the number of true alternative hypotheses
- V is the number of false positives (Type I error) (also called "false discoveries")
- S is the number of true positives (also called "true discoveries")
- T is the number of false negatives (Type II error)
- U is the number of true negatives
- $R=V+S$ is the number of rejected null hypotheses (also called "discoveries", either true or false)

In m hypothesis tests of which $m_{0}$ are true null hypotheses, R is an observable random variable, and S, T, U, and V are unobservable random variables.

## Controlling procedures

Probability that at least one null hypothesis is wrongly rejected, for

$\alpha _{\text{per comparison}}=0.05$

, as a function of the number of independent tests

m

.

View

source data

.

### Multiple testing correction

**Multiple testing correction** refers to making statistical tests more stringent in order to counteract the problem of multiple testing. The best known such adjustment is the Bonferroni correction, but other methods have been developed. Such methods are typically designed to control the family-wise error rate or the false discovery rate.

If *m* independent comparisons are performed, the *family-wise error rate* (FWER), is given by

${\bar {\alpha }}=1-\left(1-\alpha _{\{{\text{per comparison}}\}}\right)^{m}.$

Hence, unless the tests are perfectly positively dependent (i.e., identical), ${\bar {\alpha }}$ increases as the number of comparisons increases. If we do not assume that the comparisons are independent, then we can still say:

${\bar {\alpha }}\leq m\cdot \alpha _{\{{\text{per comparison}}\}},$

which follows from Boole's inequality. Example: $0.2649=1-(1-.05)^{6}\leq .05\times 6=0.3$

There are different ways to assure that the family-wise error rate is at most $\alpha$ . The most conservative method, which is free of dependence and distributional assumptions, is the Bonferroni correction $\alpha _{\mathrm {\{per\ comparison\}} }={\alpha }/m$ . A marginally less conservative correction can be obtained by solving the equation for the family-wise error rate of m independent comparisons for $\alpha _{\mathrm {\{per\ comparison\}} }$ . This yields $\alpha _{\{{\text{per comparison}}\}}=1-{(1-{\alpha })}^{1/m}$ , which is known as the Šidák correction. Another procedure is the Holm–Bonferroni method, which uniformly delivers more power than the simple Bonferroni correction, by testing only the lowest p-value ( $i=1$ ) against the strictest criterion, and the higher p-values ( $i>1$ ) against progressively less strict criteria. $\alpha _{\mathrm {\{per\ comparison\}} }={\alpha }/(m-i+1)$ .

The classical Bonferroni method is easy to understand but should not be used since it is overly conservative. There are online calculators to correct for multiple comparisons using the more modern Holm-Bonferroni method or the Benjamini-Hochberg procedure.

For continuous problems, one can employ Bayesian logic to compute m from the prior-to-posterior volume ratio. Continuous generalizations of the Bonferroni and Šidák correction are presented in.

## Large-scale multiple testing

Traditional methods for multiple comparisons adjustments focus on correcting for modest numbers of comparisons, often in an analysis of variance. A different set of techniques have been developed for "large-scale multiple testing", in which thousands or even greater numbers of tests are performed. For example, in genomics, when using technologies such as microarrays, expression levels of tens of thousands of genes can be measured, and genotypes for millions of genetic markers can be measured. Particularly in the field of genetic association studies, there has been a serious problem with non-replication — a result being strongly statistically significant in one study but failing to be replicated in a follow-up study. Such non-replication can have many causes, but it is widely considered that failure to fully account for the consequences of making multiple comparisons is one of the causes. It has been argued that advances in measurement and information technology have made it far easier to generate large datasets for exploratory analysis, often leading to the testing of large numbers of hypotheses with no prior basis for expecting many of the hypotheses to be true. In this situation, very high false positive rates are expected unless multiple comparisons adjustments are made.

For large-scale testing problems where the goal is to provide definitive results, the family-wise error rate remains the most accepted parameter for ascribing significance levels to statistical tests. Alternatively, if a study is viewed as exploratory, or if significant results can be easily re-tested in an independent study, control of the false discovery rate (FDR) is often preferred. The FDR, loosely defined as the expected proportion of false positives among all significant tests, allows researchers to identify a set of "candidate positives" that can be more rigorously evaluated in a follow-up study.

The practice of trying many unadjusted comparisons in the hope of finding a significant one is a known problem, whether applied unintentionally or deliberately, is sometimes called "p-hacking".

### Assessing whether any alternative hypotheses are true

A basic question faced at the outset of analyzing a large set of testing results is whether there is evidence that any of the alternative hypotheses are true. One simple meta-test that can be applied when it is assumed that the tests are independent of each other is to use the Poisson distribution as a model for the number of significant results at a given level α that would be found when all null hypotheses are true. If the observed number of positives is substantially greater than what should be expected, this suggests that there are likely to be some true positives among the significant results.

For example, if 1000 independent tests are performed, each at level α = 0.05, we expect 0.05 × 1000 = 50 significant tests to occur when all null hypotheses are true. Based on the Poisson distribution with mean 50, the probability of observing more than 61 significant tests is less than 0.05, so if more than 61 significant results are observed, it is very likely that some of them correspond to situations where the alternative hypothesis holds. A drawback of this approach is that it overstates the evidence that some of the alternative hypotheses are true when the test statistics are positively correlated, which commonly occurs in practice. . On the other hand, the approach remains valid even in the presence of correlation among the test statistics, as long as the Poisson distribution can be shown to provide a good approximation for the number of significant results. This scenario arises, for instance, when mining significant frequent itemsets from transactional datasets. Furthermore, a careful two stage analysis can bound the FDR at a pre-specified level.

Another common approach that can be used in situations where the test statistics can be standardized to Z-scores is to make a normal quantile plot of the test statistics. If the observed quantiles are markedly more dispersed than the normal quantiles, this suggests that some of the significant results may be true positives.

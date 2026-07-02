---
title: "Tukey's range test"
source: https://en.wikipedia.org/wiki/Tukey's_range_test
domain: analysis-of-variance
license: CC-BY-SA-4.0
tags: analysis of variance, F-test, sum of squares, post hoc analysis
fetched: 2026-07-02
---

# Tukey's range test

**Tukey's range test**, also known as **Tukey's test**, **Tukey method**, **Tukey's honest significance test**, or **Tukey's HSD** (**honestly significant difference**) **test**, is a single-step multiple comparison procedure and statistical test. It can be used to correctly interpret the statistical significance of the difference between means that have been selected for comparison because of their extreme values.

The method was initially developed and introduced by John Tukey for use in Analysis of Variance (ANOVA), and usually has only been taught in connection with ANOVA. However, the studentized range distribution used to determine the level of significance of the differences considered in Tukey's test has vastly broader application: It is useful for researchers who have searched their collected data for remarkable differences between groups, but then cannot validly determine how significant their discovered stand-out difference is using standard statistical distributions used for other conventional statistical tests, for which the data must have been selected at random. Since when stand-out data is compared it was by definition *not* selected at random, but rather specifically chosen because it was extreme, it needs a different, stricter interpretation provided by the likely frequency and size of the studentized range; the modern practice of "data mining" is an example where it is used.

## Development

The test was devised by John Tukey, it compares all possible pairs of means, and is based on a studentized range distribution (q) (this distribution is similar to the distribution of t from the t-test. See below).

Tukey's test compares the means of every treatment to the means of every other treatment; that is, it applies simultaneously to the set of all pairwise comparisons

$\mu _{i}-\mu _{j}\ ,$

and identifies any difference between two means that is greater than the expected standard error. The confidence coefficient for the set, when all sample sizes are equal, is exactly $\ 1-\alpha \$ for any $\ \alpha ~:~0\leq \alpha \leq 1~.$ For unequal sample sizes, the confidence coefficient is greater than $\ 1-\alpha ~.$ In other words, the Tukey method is conservative when there are unequal sample sizes.

This test is often followed by the Compact Letter Display (CLD) statistical procedure to render the output of this test more transparent to non-statistician audiences.

## Assumptions

1. The observations being tested are independent within and among the groups.
2. The subgroups associated with each mean in the test are normally distributed.
3. There is equal within-subgroup variance across the subgroups associated with each mean in the test (homogeneity of variance).

## The test statistic

Tukey's test is based on a formula very similar to that of the t-test. In fact, Tukey's test is essentially a t-test, except that it corrects for family-wise error rate.

The formula for Tukey's test is

$q_{\mathsf {s}}={\frac {\ \left|Y_{\mathsf {A}}-Y_{\mathsf {B}}\right|\ }{\ {\mathsf {SE}}\ }}\ ,$

where YA and YB are the two means being compared, and SE is the standard error for the sum of the means. The value qs is the sample's test statistic. (The notation |x| means the absolute value of x; the magnitude of x with the sign set to +, regardless of the original sign of x.)

This qs test statistic can then be compared to a q value for the chosen significance level α from a table of the studentized range distribution. If the qs value is *larger* than the critical value qα obtained from the distribution, the two means are said to be significantly different at level $\ \alpha ~:~0\leq \alpha \leq 1~.$

Since the null hypothesis for Tukey's test states that all means being compared are from the same population (i.e. *μ*1 = *μ*2 = *μ*3 = ... = *μk* ), the means should be normally distributed (according to the central limit theorem) with the same model standard deviation σ, estimated by the merged standard error, $\ {\mathsf {SE}}\ ,$ for all the samples; its calculation is discussed in the following sections. This gives rise to the normality assumption of Tukey's test.

## The studentized range (q) distribution

The Tukey method uses the studentized range distribution. Suppose that we take a sample of size n from each of k populations with the same normal distribution *N*(*μ*, *σ*2) and suppose that $\ {\bar {y}}_{\mathsf {min}}\$ is the smallest of these sample means and $\ {\bar {y}}_{\mathsf {max}}\$ is the largest of these sample means, and suppose S2 is the pooled sample variance from these samples. Then the following random variable has a Studentized range distribution:

$q\equiv {\frac {\ {\overline {y}}_{\mathsf {max}}-{\overline {y}}_{\mathsf {min}}\ }{\ S{\sqrt {2/n}}\ }}$

This definition of the statistic q given above is the basis of the critically significant value for qα discussed below, and is based on these three factors:

$\ \alpha ~\quad$

the

Type I error

rate, or the probability of rejecting a true null hypothesis;

$\ k~\quad$

the number of sub-populations being compared;

$\ {\mathsf {df}}\quad$

the number of degrees of freedom for each mean

( df = *N* − *k* ) where N is the total number of observations.)

The distribution of q has been tabulated and appears in many textbooks on statistics. In some tables the distribution of q has been tabulated without the $\ {\sqrt {2\ }}\$ factor. To understand which table it is, we can compute the result for *k* = 2 and compare it to the result of the Student's t-distribution with the same degrees of freedom and the same α . In addition, R offers a cumulative distribution function (`ptukey`) and a quantile function (`qtukey`) for q .

## Confidence limits

The Tukey confidence limits for all pairwise comparisons with confidence coefficient of at least   1 − *α*   are

${\displaystyle {\bar {y}}_{i\bullet }-{\bar {y}}_{j\bullet }\ \pm \ {\frac {\ q_{\ \alpha \$

Notice that the point estimator and the estimated variance are the same as those for a single pairwise comparison. The only difference between the confidence limits for simultaneous comparisons and those for a single comparison is the multiple of the estimated standard deviation.

Also note that the sample sizes must be equal when using the studentized range approach. $\ {\widehat {\sigma }}_{\varepsilon }\$ is the standard deviation of the entire design, not just that of the two groups being compared. It is possible to work with unequal sample sizes. In this case, one has to calculate the estimated standard deviation for each pairwise comparison as formalized by Clyde Kramer in 1956, so the procedure for unequal sample sizes is sometimes referred to as the **Tukey–Kramer method** which is as follows:

${\displaystyle {\bar {y}}_{i\bullet }-{\bar {y}}_{j\bullet }\ \pm \ {\frac {\ q_{\ \alpha \$

where *n i* and *n j* are the sizes of groups i and j respectively. The degrees of freedom for the whole design is also applied.

## Comparing ANOVA and Tukey–Kramer tests

Both ANOVA and Tukey–Kramer tests are based on the same assumptions. However, these two tests for k groups (i.e. *μ*1 = *μ*2 = ... = *μk* ) may result in logical contradictions when *k* > 2 , even if the assumptions do hold.

It is possible to generate a set of pseudorandom samples of strictly negative measure such that hypothesis *μ*1 = *μ*2 is rejected at significance level $\ 1-\alpha >0.95\$ while *μ*1 = *μ*2 = *μ*3 is not rejected even at $\ 1-\alpha =0.975~.$

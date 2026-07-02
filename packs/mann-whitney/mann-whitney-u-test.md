---
title: "Mann–Whitney U test"
source: https://en.wikipedia.org/wiki/Mann–Whitney_U_test
domain: mann-whitney
license: CC-BY-SA-4.0
tags: Mann Whitney U test, Wilcoxon rank-sum, stochastic ordering, order statistic
fetched: 2026-07-02
---

# Mann–Whitney *U* test

The **Mann–Whitney U test** (also called the **Mann–Whitney–Wilcoxon** (**MWW/MWU**), **Wilcoxon rank-sum test**, or **Wilcoxon–Mann–Whitney test**) is a nonparametric statistical test of the null hypothesis that randomly selected values *X* and *Y* from two populations have the same distribution.

The value of *U* calculated by the test can be converted to a measure of effect size by dividing it by the maximum value of U, which is the product of the sizes of the two samples being compared. This measure is the probability that the value of a random observation from the higher group will be greater than that of a random observation from the lower group.

Nonparametric tests used on two *dependent* samples are the sign test and the Wilcoxon signed-rank test.

## Assumptions and formal statement of hypotheses

Henry Mann and Donald Ransom Whitney developed the Mann–Whitney *U* test under the assumption of continuous responses with the alternative hypothesis being that one distribution is stochastically greater than the other. That is to say that the probability of a random observation from one group being larger than a random observation from the other group is 0.5. There are many other ways to formulate the null and alternative hypotheses such that the Mann–Whitney *U* test will give a valid test.

A very general formulation is to assume the following conditions:

1. All the observations from both groups are independent of each other,
2. The responses are at least ordinal (i.e., one can at least say, of any two observations, which is the greater),
3. Under the null hypothesis *H*0, the distributions of both populations are identical.
4. The alternative hypothesis *H*1 is that the distributions are not identical.

Under the general formulation, the test is only consistent when the following occurs under *H*1:

1. The probability of an observation from population *X* exceeding an observation from population *Y* is different (larger, or smaller) than the probability of an observation from *Y* exceeding an observation from *X*; i.e., P(*X* > *Y*) ≠ P(*Y* > *X*) or P(*X* > *Y*) + 0.5 · P(*X* = *Y*) ≠ 0.5.

Under more strict assumptions than the general formulation above, e.g., if the responses are assumed to be continuous and the alternative is restricted to a shift in location, i.e., *F*1(*x*) = *F*2(*x* + *δ*), we can interpret a significant Mann–Whitney *U* test as showing a difference in medians. This, however, is an interpretation, and is not the actual hypothesis being tested (see above). This practice relies on strict assumptions about the data distribution. When this assumption does not hold, it is simple to demonstrate that the test produces a statistically significant result when the medians of the two groups are in fact identical. If a test of medians is required, quantile regression explicitly tests this.

Under this location shift assumption, we can also interpret the Mann–Whitney *U* test as assessing whether the Hodges–Lehmann estimate of the difference in central tendency between the two populations differs from zero. The Hodges–Lehmann estimate for this two-sample problem is the median of all possible differences between an observation in the first sample and an observation in the second sample.

Otherwise, if both the dispersions and shapes of the distribution of both samples differ, the Mann–Whitney *U* test fails a test of medians. It is possible to show examples where medians are numerically equal while the test rejects the null hypothesis with a small p-value.

The Mann–Whitney *U* test / Wilcoxon rank-sum test is not the same as the Wilcoxon *signed*-rank test, although both are nonparametric and involve summation of ranks. The Mann–Whitney *U* test is applied to independent samples. The Wilcoxon signed-rank test is applied to matched or dependent samples.

## U statistic

Although Mann and Whitney's original paper described the test as one of stochastic superiority – in other words, as a test of whether an observation from one group was likely to be larger than an observation from the other group, the test statistic, *U*, does not give this probability. This probability can be simply calculated by dividing *U* by its maximum value, which is the product of the two sample sizes.

Let $X_{1},\ldots ,X_{n_{1}}$ be group 1, an i.i.d. sample from X , and $Y_{1},\ldots ,Y_{n_{2}}$ be group 2, an i.i.d. sample from Y , and let both samples be independent of each other. The corresponding *Mann–Whitney U statistic* is defined as the smaller of:

$U_{1}=n_{1}n_{2}+{\tfrac {n_{1}(n_{1}+1)}{2}}-R_{1},U_{2}=n_{1}n_{2}+{\tfrac {n_{2}(n_{2}+1)}{2}}-R_{2}$

with

$R_{1},R_{2}$

being the sums of the ranks in groups 1 and 2, after ranking all samples from both groups such that the smallest value obtains rank 1 and the largest rank

$n_{1}+n_{2}$

.

### Area-under-curve (AUC) statistic for ROC curves

The *U* statistic is related to the **area under the receiver operating characteristic curve** (AUC):

$\mathrm {AUC} _{1}={U_{1} \over n_{1}n_{2}}$

Note that this is the same definition as the common language effect size, i.e. the probability that a classifier will rank a randomly chosen instance from the first group higher than a randomly chosen instance from the second group.

Because of its probabilistic form, the *U* statistic can be generalized to a measure of a classifier's separation power for more than two classes:

$M={1 \over c(c-1)}\sum \mathrm {AUC} _{k,\ell }$

Where *c* is the number of classes, and the *R**k*,*ℓ* term of AUC*k*,*ℓ* considers only the ranking of the items belonging to classes *k* and *ℓ* (i.e., items belonging to all other classes are ignored) according to the classifier's estimates of the probability of those items belonging to class *k*. AUC*k*,*k* will always be zero but, unlike in the two-class case, generally AUC*k*,*ℓ* ≠ AUC*ℓ*,*k*, which is why the *M* measure sums over all (*k*,*ℓ*) pairs, in effect using the average of AUC*k*,*ℓ* and AUC*ℓ*,*k*.

## Calculations

The test involves the calculation of a statistic, usually called *U*, whose distribution under the null hypothesis is known:

- In the case of small samples, the distribution is tabulated
- For sample sizes above ~20, approximation using the normal distribution is fairly good.

Alternatively, the null distribution can be approximated using permutation tests and Monte Carlo simulations.

Some books tabulate statistics equivalent to *U*, such as the sum of ranks in one of the samples, rather than *U* itself.

The Mann–Whitney *U* test is included in most statistical packages.

It is also easily calculated by hand, especially for small samples. There are multiple ways of doing this.

**Method one:**

For comparing two small sets of observations, a direct method is quick, and gives insight into the meaning of the *U* statistic, which corresponds to the number of wins out of all pairwise contests (see the tortoise and hare example under Examples below). For each observation in one set, count the number of times this first value wins over any observations in the other set (the other value loses if this first is larger). Count 0.5 for any ties. The sum of wins and ties is *U* (i.e., $U_{1}$ ) for the first set. *U* for the other set is the converse (i.e., $U_{2}$ ).

**Method two:**

For larger samples:

1. Assign numeric ranks to all the observations (put the observations from both groups to one set), beginning with 1 for the smallest value. Where there are groups of tied values, assign a rank equal to the midpoint of unadjusted rankings (e.g., the ranks of (3, 5, 5, 5, 5, 8) are (1, 3.5, 3.5, 3.5, 3.5, 6), where the unadjusted ranks would be (1, 2, 3, 4, 5, 6)).
2. Now, add up the ranks for the observations which came from sample 1. The sum of ranks in sample 2 is now determined, since the sum of all the ranks equals *N*(*N* + 1)/2 where *N* is the total number of observations.
3. *U* is then given by:

$U_{1}=R_{1}-{n_{1}(n_{1}+1) \over 2}\,\!$

where

n

1

is the sample size for sample 1, and

R

1

is the sum of the ranks in sample 1.

Note that it doesn't matter which of the two samples is considered sample 1. An equally valid formula for

U

is

$U_{2}=R_{2}-{n_{2}(n_{2}+1) \over 2}\,\!$

The smaller value of

U

1

and

U

2

is the one used when consulting significance tables. The sum of the two values is given by

$U_{1}+U_{2}=R_{1}-{n_{1}(n_{1}+1) \over 2}+R_{2}-{n_{2}(n_{2}+1) \over 2}.\,\!$

Knowing that

R

1

+

R

2

=

N

(

N

+ 1)/2

and

N

=

n

1

+

n

2

, and doing some

algebra

, we find that the sum is

U

1

+

U

2

=

n

1

n

2

.

## Properties

The maximum value of *U* is the product of the sample sizes for the two samples (i.e., $U_{i}=n_{1}n_{2}$ ). In such a case, the "other" *U* would be 0.

## Examples

### Illustration of calculation methods

Suppose that Aesop is dissatisfied with his classic experiment in which one tortoise was found to beat one hare in a race, and decides to carry out a significance test to discover whether the results could be extended to tortoises and hares in general. He collects a sample of 6 tortoises and 6 hares, and makes them all run his race at once. The order in which they reach the finishing post (their rank order, from first to last crossing the finish line) is as follows, writing T for a tortoise and H for a hare:

T H H H H H T T T T T H

What is the value of *U*?

- Using the direct method, we take each tortoise in turn, and count the number of hares it beats, getting 6, 1, 1, 1, 1, 1, which means that *UT* = 11. Alternatively, we could take each hare in turn, and count the number of tortoises it beats. In this case, we get 5, 5, 5, 5, 5, 0, so *UH* = 25. Note that the sum of these two values for *U* = 36, which is 6×6.
- Using the indirect method:

Rank the animals by the time they take to complete the course, so give the first animal home rank 12, the second rank 11, and so forth.

The sum of the ranks achieved by the tortoises is

12 + 6 + 5 + 4 + 3 + 2 = 32

.

Therefore

U

T

= 32 − (6×7)/2 = 32 − 21 = 11

(same as method one).

The sum of the ranks achieved by the hares is

11 + 10 + 9 + 8 + 7 + 1 = 46

, leading to

U

H

= 46 − 21 = 25

.

### Example statement of results

In reporting the results of a Mann–Whitney *U* test, it is important to state:

- A measure of the central tendencies of the two groups (means or medians; since the Mann–Whitney *U* test is an ordinal test, medians are usually recommended)
- The value of *U* (perhaps with some measure of effect size, such as common language effect size or rank-biserial correlation).
- The sample sizes
- The significance level.

In practice some of this information may already have been supplied and common sense should be used in deciding whether to repeat it. A typical report might run,

"Median latencies in groups E and C were 153 and 247 ms; the distributions in the two groups differed significantly (Mann–Whitney

U

= 10.5

,

n

1

=

n

2

= 8

,

P

< 0.05

two-tailed)."

A statement that does full justice to the statistical status of the test might run,

"Outcomes of the two treatments were compared using the Wilcoxon–Mann–Whitney two-sample rank-sum test. The treatment effect (difference between treatments) was quantified using the Hodges–Lehmann (HL) estimator, which is consistent with the Wilcoxon test.

This estimator (HLΔ) is the median of all possible differences in outcomes between a subject in group B and a subject in group A. A non-parametric 0.95 confidence interval for HLΔ accompanies these estimates as does ρ, an estimate of the probability that a randomly chosen subject from population B has a higher weight than a randomly chosen subject from population A. The median [quartiles] weight for subjects on treatment A and B respectively are 147 [121, 177] and 151 [130, 180] kg. Treatment A decreased weight by HLΔ = 5 kg (0.95 CL [2, 9] kg,

2

P

= 0.02

,

ρ

= 0.58

)."

However it would be rare to find such an extensive report in a document whose major topic was not statistical inference.

## Normal approximation and tie correction

For large samples, *U* is approximately normally distributed. In that case, the standardized value

$z={\frac {U-m_{U}}{\sigma _{U}}},\,$

where *m**U* and *σ**U* are the mean and standard deviation of *U*, is approximately a standard normal deviate whose significance can be checked in tables of the normal distribution. *m**U* and *σ**U* are given by

$m_{U}={\frac {n_{1}n_{2}}{2}},\,$

and

$\sigma _{U}={\sqrt {n_{1}n_{2}(n_{1}+n_{2}+1) \over 12}}.\,$

The formula for the standard deviation is more complicated in the presence of tied ranks. If there are ties in ranks, *σ* should be adjusted as follows:

$\sigma _{\text{ties}}={\sqrt {{n_{1}n_{2}(n_{1}+n_{2}+1) \over 12}-{n_{1}n_{2}\sum _{k=1}^{K}(t_{k}^{3}-t_{k}) \over 12n(n-1)}}},\,$

where the left side is simply the variance and the right side is the adjustment for ties, *t**k* is the number of ties for the *k*th rank, and *K* is the total number of unique ranks with ties.

A more computationally-efficient form with *n*1*n*2/12 factored out is

$\sigma _{\text{ties}}={\sqrt {{n_{1}n_{2} \over 12}\left((n+1)-{\sum _{k=1}^{K}(t_{k}^{3}-t_{k}) \over n(n-1)}\right)}},$

where *n* = *n*1 + *n*2.

If the number of ties is small (and especially if there are no large tie bands) ties can be ignored when doing calculations by hand. The computer statistical packages will use the correctly adjusted formula as a matter of routine.

Note that since *U*1 + *U*2 = *n*1*n*2, the mean *n*1*n*2/2 used in the normal approximation is the mean of the two values of *U*. Therefore, the absolute value of the *z*-statistic calculated will be same whichever value of *U* is used.

## Effect sizes

It is a widely recommended practice for scientists to report an effect size for an inferential test.

### Proportion of concordance out of all pairs

The following measures are equivalent.

#### Common language effect size

One method of reporting the effect size for the Mann–Whitney *U* test is with *f*, the common language effect size. As a sample statistic, the common language effect size is computed by forming all possible pairs between the two groups, then finding the proportion of pairs that support a direction (say, that items from group 1 are larger than items from group 2). To illustrate, in a study with a sample of ten hares and ten tortoises, the total number of ordered pairs is ten times ten or 100 pairs of hares and tortoises. Suppose the results show that the hare ran faster than the tortoise in 90 of the 100 sample pairs; in that case, the sample common language effect size is 90%.

The relationship between *f* and the Mann–Whitney *U* (specifically $U_{1}$ ) is as follows:

$f={U_{1} \over n_{1}n_{2}}\,$

This is the same as the area under the curve (AUC) for the ROC curve.

#### *ρ* statistic

A statistic called *ρ* that is linearly related to *U* and widely used in studies of categorization (discrimination learning involving concepts), and elsewhere, is calculated by dividing *U* by its maximum value for the given sample sizes, which is simply *n*1×*n*2. *ρ* is thus a non-parametric measure of the overlap between two distributions; it can take values between 0 and 1, and it estimates P(*Y* > *X*) + 0.5 P(*Y* = *X*), where *X* and *Y* are randomly chosen observations from the two distributions. Both extreme values represent complete separation of the distributions, while a *ρ* of 0.5 represents complete overlap. The usefulness of the *ρ* statistic can be seen in the case of the odd example used above, where two distributions that were significantly different on a Mann–Whitney *U* test nonetheless had nearly identical medians: the *ρ* value in this case is approximately 0.723 in favour of the hares, correctly reflecting the fact that even though the median tortoise beat the median hare, the hares collectively did better than the tortoises collectively.

### Rank-biserial correlation

A method of reporting the effect size for the Mann–Whitney *U* test is with a measure of rank correlation known as the rank-biserial correlation. Edward Cureton introduced and named the measure. Like other correlational measures, the rank-biserial correlation can range from minus one to plus one, with a value of zero indicating no relationship.

There is a simple difference formula to compute the rank-biserial correlation from the common language effect size: the correlation is the difference between the proportion of pairs favorable to the hypothesis (*f*) minus its complement (i.e., the proportion that is unfavorable (*u*)). This simple difference formula is just the difference of the common language effect size of each group, and is as follows:

$r=f-u$

For example, consider the example where hares run faster than tortoises in 90 of 100 pairs. The common language effect size is 90%, so the rank-biserial correlation is 90% minus 10%, and the rank-biserial *r* = 0.80.

An alternative formula for the rank-biserial can be used to calculate it from the Mann–Whitney *U* (either $U_{1}$ or $U_{2}$ ) and the sample sizes of each group:

$r=f-(1-f)=2f-1={2U_{1} \over n_{1}n_{2}}-1=1-{2U_{2} \over n_{1}n_{2}}$

This formula is useful when the data are not available, but when there is a published report, because *U* and the sample sizes are routinely reported. Using the example above with 90 pairs that favor the hares and 10 pairs that favor the tortoise, *U*2 is the smaller of the two, so *U2* = 10. This formula then gives *r* = 1 – (2×10) / (10×10) = 0.80, which is the same result as with the simple difference formula above.

## Relation to other tests

### Comparison to Student's *t*-test

The Mann–Whitney *U* test tests a null hypothesis that the probability distribution of a randomly drawn observation from one group is the same as the probability distribution of a randomly drawn observation from the other group against an alternative that those distributions are not equal (see Mann–Whitney U test#Assumptions and formal statement of hypotheses). In contrast, a t-test tests a null hypothesis of equal means in two groups against an alternative of unequal means. Hence, except in special cases, the Mann–Whitney *U* test and the t-test do not test the same hypotheses and should be compared with this in mind.

**Ordinal data**

The Mann–Whitney

U

test is preferable to the

t

-test when the data are

ordinal

but not interval scaled, in which case the spacing between adjacent values of the scale cannot be assumed to be constant.

**Robustness**

As it compares the sums of ranks,

the Mann–Whitney

U

test is less likely than the

t

-test to spuriously indicate significance because of the presence of

outliers

. However, the Mann–Whitney

U

test may have worse

type I error

control when data are both heteroscedastic and non-normal.

**Efficiency**

When normality holds, the Mann–Whitney

U

test has an (asymptotic)

efficiency

of 3/

π

or about 0.95 when compared to the

t

-test.

For distributions sufficiently far from normal and for sufficiently large sample sizes, the Mann–Whitney

U

test is considerably more efficient than the

t

.

This comparison in efficiency, however, should be interpreted with caution, as Mann–Whitney and the t-test do not test the same quantities. If, for example, a difference of group means is of primary interest, Mann–Whitney is not an appropriate test.

The Mann–Whitney *U* test will give very similar results to performing an ordinary parametric two-sample *t*-test on the rankings of the data.

| Distribution | Efficiency |
|---|---|
| Logistic | $\pi ^{2}/9$ |
| Normal | $3/\pi$ |
| Laplace | 3/2 |
| Uniform | 1 |

### Different distributions

The Mann–Whitney *U* test is not valid for testing the null hypothesis $P(Y>X)+0.5P(Y=X)=0.5$ against the alternative hypothesis $P(Y>X)+0.5P(Y=X)\neq 0.5$ , without assuming that the distributions are the same under the null hypothesis (i.e., assuming $F_{1}=F_{2}$ ). To test between those hypotheses, better tests are available. Among those are the Brunner-Munzel and the Fligner–Policello test. Specifically, under the more general null hypothesis $P(Y>X)+0.5P(Y=X)=0.5$ , the Mann–Whitney *U* test can have inflated type I error rates even in large samples (especially if the variances of two populations are unequal and the sample sizes are different), a problem the better alternatives solve. As a result, it has been suggested to use one of the alternatives (specifically the Brunner–Munzel test) if it cannot be assumed that the distributions are equal under the null hypothesis.

#### Alternatives

If one desires a simple shift interpretation, the Mann–Whitney *U* test should *not* be used when the distributions of the two samples are very different, as it can give erroneous interpretation of significant results. In that situation, the unequal variances version of the *t*-test may give more reliable results.

Similarly, some authors (*Conover, W. J. (1999). *Practical Nonparametric Statistics -- 3rd ed*. New York: John Wiley & Sons. p. 272-281. ISBN 0-471-16068-7.*) suggest transforming the data to ranks (if they are not already ranks) and then performing the *t*-test on the transformed data, the version of the *t*-test used depending on whether or not the population variances are suspected to be different. Rank transformations do not preserve variances, but variances are recomputed from samples after rank transformations.

The Brown–Forsythe test has been suggested as an appropriate non-parametric equivalent to the *F*-test for equal variances.

A more powerful test is the Brunner-Munzel test, outperforming the Mann–Whitney *U* test in case of violated assumption of exchangeability.

The Mann–Whitney *U* test is a special case of the proportional odds model, allowing for covariate-adjustment.

See also Kolmogorov–Smirnov test.

### Kendall's tau

The Mann–Whitney *U* test is related to a number of other non-parametric statistical procedures. For example, it is equivalent to Kendall's tau correlation coefficient if one of the variables is binary (that is, it can only take two values).

## Software implementations

In many software packages, the Mann–Whitney *U* test (of the hypothesis of equal distributions against appropriate alternatives) has been poorly documented. Some packages incorrectly treat ties or fail to document asymptotic techniques (e.g., correction for continuity). A 2000 review discussed some of the following packages:

- MATLAB has ranksum in its Statistics Toolbox.
- R's statistics base-package implements the test wilcox.test in its "stats" package.
- The R function wilcoxonZ from the rcompanion package will calculate the *z* statistic for a Wilcoxon two-sample, paired, or one-sample test.
- SAS implements the test in its `PROC NPAR1WAY` procedure.
- Python has an implementation of this test provided by SciPy.
- SigmaStat (SPSS Inc., Chicago, IL)
- SYSTAT (SPSS Inc., Chicago, IL)
- Java has an implementation of this test provided by Apache Commons
- Julia has implementations of this test through several packages. In the package `HypothesisTests.jl`, this is found as `pvalue(MannWhitneyUTest(X, Y))`.
- JMP (SAS Institute Inc., Cary, NC)
- S-Plus (MathSoft, Inc., Seattle, WA)
- STATISTICA (StatSoft, Inc., Tulsa, OK)
- SPSS (SPSS Inc, Chicago)
- StatsDirect (StatsDirect Ltd, Manchester, UK) implements all common variants.
- Stata (Stata Corporation, College Station, TX) implements the test in its ranksum command.
- StatXact (Cytel Software Corporation, Cambridge, Massachusetts)
- PSPP implements the test in its WILCOXON function.
- KNIME implements the test in its Wilcoxon–Mann–Whitney Test node.
- ClickHouse implements the test in its mannWhitneyUTest function.

## History

The statistic appeared in a 1914 article by the German Gustav Deuchler (with a missing term in the variance).

In a single paper in 1945, Frank Wilcoxon proposed both the one-sample signed rank and the two-sample rank sum test, in a test of significance with a point null-hypothesis against its complementary alternative (that is, equal versus not equal). However, he only tabulated a few points for the equal-sample size case in that paper (though in a later paper he gave larger tables).

A thorough analysis of the statistic, which included a recurrence allowing the computation of tail probabilities for arbitrary sample sizes and tables for sample sizes of eight or less appeared in the article by Henry Mann and his student Donald Ransom Whitney in 1947. This article discussed alternative hypotheses, including a stochastic ordering (where the cumulative distribution functions satisfied the pointwise inequality *F**X*(*t*) < *F**Y*(*t*)). This paper also computed the first four moments and established the limiting normality of the statistic under the null hypothesis, so establishing that it is asymptotically distribution-free.

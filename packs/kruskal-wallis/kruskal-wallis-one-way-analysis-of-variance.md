---
title: "Kruskal–Wallis test"
source: https://en.wikipedia.org/wiki/Kruskal–Wallis_one-way_analysis_of_variance
domain: kruskal-wallis
license: CC-BY-SA-4.0
tags: Kruskal Wallis, Friedman test, post hoc test, rank correlation
fetched: 2026-07-02
---

# Kruskal–Wallis test

(Redirected from

Kruskal–Wallis one-way analysis of variance

)

The **Kruskal–Wallis test** by ranks, **Kruskal–Wallis H test** (named after William Kruskal and W. Allen Wallis), or **one-way ANOVA on ranks** is a non-parametric statistical test for testing whether samples originate from the same distribution. It is used for comparing two or more independent samples of equal or different sample sizes. It extends the Mann–Whitney *U* test, which is used for comparing only two groups. The parametric equivalent of the Kruskal–Wallis test is the one-way analysis of variance (ANOVA).

A significant Kruskal–Wallis test indicates that at least one sample stochastically dominates one other sample. The test does not identify where this stochastic dominance occurs or for how many pairs of groups stochastic dominance obtains. For analyzing the specific sample pairs for stochastic dominance, Dunn's test, pairwise Mann–Whitney tests with Bonferroni correction, or the more powerful but less well known Conover–Iman test are sometimes used.

It is supposed that the treatments significantly affect the response level and then there is an order among the treatments: one tends to give the lowest response, another gives the next lowest response is second, and so forth. Since it is a nonparametric method, the Kruskal–Wallis test does not assume a normal distribution of the residuals, unlike the analogous one-way analysis of variance. If the researcher can make the assumptions of an identically shaped and scaled distribution for all groups, except for any difference in medians, then the null hypothesis is that the medians of all groups are equal, and the alternative hypothesis is that at least one population median of one group is different from the population median of at least one other group. Otherwise, it is impossible to say, whether the rejection of the null hypothesis comes from the shift in locations or group dispersions. This is the same issue that happens also with the Mann-Whitney test. If the data contains potential outliers, if the population distributions have heavy tails, or if the population distributions are significantly skewed, the Kruskal–Wallis test is more powerful at detecting differences among treatments than ANOVA F-test. On the other hand, if the population distributions are normal or are light-tailed and symmetric, then ANOVA F-test will generally have greater power which is the probability of rejecting the null hypothesis when it indeed should be rejected.

## Method

1. Rank all data from all groups together; i.e., rank the data from 1 to *N* ignoring group membership. Assign any tied values the average of the ranks they would have received had they not been tied.
2. The test statistic is given by $\definecolor {Orange}{rgb}{1,0.5019607843137255,0}\definecolor {ChromeYellow}{rgb}{1,0.6549019607843137,0.011764705882352941}\definecolor {Green}{rgb}{0,0.5019607843137255,0}\definecolor {green}{rgb}{0,0.5019607843137255,0}\definecolor {Blue}{rgb}{0,0,1}\definecolor {Purple}{rgb}{0.5019607843137255,0,0.5019607843137255}H=({\color {Red}N}-1){\frac {\sum _{i=1}^{\color {Orange}g}{\color {ChromeYellow}n_{i}}({\color {Blue}{\bar {r}}_{i\cdot }}-{\color {Purple}{\bar {r}}})^{2}}{\sum _{i=1}^{\color {Orange}g}\sum _{j=1}^{\color {ChromeYellow}n_{i}}({\color {Green}r_{ij}}-{\color {Purple}{\bar {r}}})^{2}}},$ where
  - ${\textstyle \color {Red}N}$ is the total number of observations across all groups
  - ${\textstyle \definecolor {Orange}{rgb}{1,0.5019607843137255,0}\color {Orange}g}$ is the number of groups
  - ${\textstyle \definecolor {ChromeYellow}{rgb}{1,0.6549019607843137,0.011764705882352941}\color {ChromeYellow}n_{i}}$ is the number of observations in group i
  - $\definecolor {Green}{rgb}{0,0.5019607843137255,0}\definecolor {green}{rgb}{0,0.5019607843137255,0}\color {Green}r_{ij}$ is the rank (among all observations) of observation j from group i
  - $\definecolor {blue}{rgb}{0,0,1}{\color {blue}{\bar {r}}_{i\cdot }}={\frac {\sum _{j=1}^{n_{i}}{r_{ij}}}{n_{i}}}$ is the average rank of all observations in group i
  - ${\textstyle \definecolor {Purple}{rgb}{0.5019607843137255,0,0.5019607843137255}{\color {Purple}{\bar {r}}}={\tfrac {1}{2}}(N+1)}$ is the average of all the ${\textstyle \definecolor {Green}{rgb}{0,0.5019607843137255,0}\definecolor {green}{rgb}{0,0.5019607843137255,0}\color {Green}r_{ij}}$ .
3. If the data contain no ties, the denominator of the expression for H is exactly $(N-1)N(N+1)/12$ and ${\bar {r}}={\tfrac {N+1}{2}}$ . Thus ${\begin{aligned}H&={\frac {12}{N(N+1)}}\sum _{i=1}^{g}n_{i}\left({\bar {r}}_{i\cdot }-{\frac {N+1}{2}}\right)^{2}\\&={\frac {12}{N(N+1)}}\sum _{i=1}^{g}n_{i}{\bar {r}}_{i\cdot }^{2}-\ 3(N+1)\end{aligned}}$ The last formula contains only the squares of the average ranks.
4. A correction for ties if using the short-cut formula described in the previous point can be made by dividing H by $1-{\frac {\sum _{i=1}^{G}(t_{i}^{3}-t_{i})}{N^{3}-N}}$ , where ${\textstyle G}$ is the number of groupings of different tied ranks, and ${\textstyle t_{i}}$ is the number of tied values within group ${\textstyle i}$ that are tied at a particular value. This correction usually makes little difference in the value of *${\textstyle H}$* unless there are a large number of ties.
5. When performing multiple sample comparisons, the type I error tends to become inflated. Therefore, the Bonferroni procedure is used to adjust the significance level, that is, ${\bar {a}}={\frac {\alpha }{\Bbbk }}$ , where ${\bar {a}}$ is the adjusted significance level, $\alpha$ is the initial significance level, and $\Bbbk$ is the number of contrasts.
6. Finally, the decision to reject or accept the null hypothesis is made by comparing H to a critical value $H_{c}$ (obtained from a table or software) for a given significance or alpha level. If H is bigger than $H_{c}$ , the null hypothesis is rejected. If possible (no ties, sample not too big) one should compare H to the critical value obtained from the exact distribution of H . Otherwise, the distribution of H can be approximated by a chi-squared distribution with ${\textstyle g-1}$ degrees of freedom. If some $n_{i}$ values are small (i.e., less than 5) the exact probability distribution of H can be quite different from this chi-squared distribution. If a table of the chi-squared probability distribution is available, the critical value of chi-squared, $\chi _{\alpha :g-1}^{2}$ , can be found by entering the table at ${\textstyle g-1}$ degrees of freedom and looking under the desired significance or alpha level.
7. If the statistic is not significant, there is no evidence of stochastic dominance among the samples. However, if the test is significant then at least one sample stochastically dominates another sample. Then, a researcher might use sample contrasts between individual sample pairs, or *post hoc* tests using Dunn's test, which (1) properly employs the same rankings as the Kruskal–Wallis test, and (2) properly employs the pooled variance implied by the null hypothesis of the Kruskal–Wallis test in order to determine which of the sample pairs are significantly different. When performing multiple sample contrasts or tests, the Type I error rate tends to become inflated, raising concerns about multiple comparisons.

## Exact probability tables

A large amount of computing resources is required to compute exact probabilities for the Kruskal–Wallis test. Existing software only provides exact probabilities for sample sizes of less than about 30 participants. These software programs rely on the asymptotic approximation for larger sample sizes. Exact probability values for larger sample sizes are available. Spurrier (2003) published exact probability tables for samples as large as 45 participants. Meyer and Seaman (2006) produced exact probability distributions for samples as large as 105 participants.

## Exact distribution of *H*

Choi et al. made a review of two methods that had been developed to compute the exact distribution of H , proposed a new one, and compared the exact distribution to its chi-squared approximation.

## Example

### Test for differences in ozone levels by month

The following example uses data from Chambers et al. on daily readings of ozone for May 1 to September 30, 1973, in New York City. The data are in the R data set `airquality`, and the analysis is included in the documentation for the R function `kruskal.test`. Boxplots of ozone values by month are shown in the figure.

The Kruskal–Wallis test finds a significant difference (p = 6.901e-06) indicating that ozone differs among the 5 months.

```mw
kruskal.test(Ozone ~ Month, data = airquality)

	Kruskal-Wallis rank sum test

data:  Ozone by Month
Kruskal-Wallis chi-squared = 29.267, df = 4, p-value = 6.901e-06
```

To determine which months differ, post-hoc tests may be performed using a Wilcoxon rank-sum test for each pair of months, with a Bonferroni (or other) correction for multiple hypothesis testing.

```mw
pairwise.wilcox.test(airquality$Ozone, airquality$Month, p.adjust.method = "bonferroni")

	Pairwise comparisons using Wilcoxon rank sum test

data:  airquality$Ozone and airquality$Month

  5      6      7      8     
6 1.0000 -      -      -     
7 0.0003 0.1414 -      -     
8 0.0012 0.2591 1.0000 -     
9 1.0000 1.0000 0.0074 0.0325

P value adjustment method: bonferroni
```

The post-hoc tests indicate that, after Bonferroni correction for multiple testing, the following differences are significant (adjusted p < 0.05).

- Month 5 vs Months 7 and 8
- Month 9 vs Months 7 and 8

## Implementation

The Kruskal–Wallis test can be implemented in many programming tools and languages. We list here only the open source free software packages:

- In Python's SciPy package, the function `scipy.stats.kruskal` can return the test result and *p*-value.
- R base-package has an implement of this test using `kruskal.test`.
- jamovi has implemented this analysis in the ANOVA menu.
- Java has the implement provided by Apache Commons.
- In Julia, the package `HypothesisTests.jl` has the function `KruskalWallisTest(groups::AbstractVector{<:Real}...)` to compute the p-value.

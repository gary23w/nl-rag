---
title: "Friedman test"
source: https://en.wikipedia.org/wiki/Friedman_test
domain: kruskal-wallis
license: CC-BY-SA-4.0
tags: Kruskal Wallis, Friedman test, post hoc test, rank correlation
fetched: 2026-07-02
---

# Friedman test

The **Friedman test** is a non-parametric statistical test developed by Milton Friedman. Similar to the parametric repeated measures ANOVA, it is used to detect differences in treatments across multiple test attempts. The procedure involves ranking each row (or *block*) together, and then considering the values of ranks by columns. Applicable to complete block designs, it is thus a special case of the Durbin test.

Classic examples of use are:

- ${\textstyle n}$ wine judges each rate ${\textstyle k}$ different wines. Are any of the ${\textstyle k}$ wines ranked consistently higher or lower than the others?
- ${\textstyle n}$ welders each use ${\textstyle k}$ welding torches, and the ensuing welds were rated on quality. Do any of the ${\textstyle k}$ torches produce consistently better or worse welds?

The Friedman test is used for one-way repeated measures analysis of variance by ranks. In its use of ranks it is similar to the Kruskal–Wallis one-way analysis of variance by ranks.

The Friedman test is widely supported by many statistical software packages.

## Method

1. Given data $\{x_{ij}\}_{n\times k}$ , that is, a matrix with n rows (the *blocks*), k columns (the *treatments*) and a single observation at the intersection of each block and treatment, calculate the ranks *within* each block. If there are tied values, assign to each tied value the average of the ranks that would have been assigned without ties. Replace the data with a new matrix $\{r_{ij}\}_{n\times k}$ where the entry $r_{ij}$ is the rank of $x_{ij}$ within block i .
2. Find the values ${\bar {r}}_{\cdot j}={\frac {1}{n}}\sum _{i=1}^{n}{r_{ij}}$
3. The test statistic is given by $Q={\frac {12n}{k(k+1)}}\sum _{j=1}^{k}\left({\bar {r}}_{\cdot j}-{\frac {k+1}{2}}\right)^{2}$ . Note that the value of ${\textstyle Q}$ does need to be adjusted for tied values in the data.
4. Finally, when ${\textstyle n}$ or ${\textstyle k}$ is large (i.e. ${\textstyle n>15}$ or ${\textstyle k>4}$ ), the probability distribution of ${\textstyle Q}$ can be approximated by that of a chi-squared distribution. In this case the *p*-value is given by $\mathbf {P} (\chi _{k-1}^{2}\geq Q)$ . If ${\textstyle n}$ or ${\textstyle k}$ is small, the approximation to chi-square becomes poor and the *p*-value should be obtained from tables of ${\textstyle Q}$ specially prepared for the Friedman test. If the *p*-value is significant, appropriate post-hoc multiple comparisons tests would be performed.

- When using this kind of design for a binary response, one instead uses the Cochran's Q test.
- The Sign test (with a two-sided alternative) is equivalent to a Friedman test on two groups.
- Kendall's W is a normalization of the Friedman statistic between ${\textstyle 0}$ and ${\textstyle 1}$ .
- The Wilcoxon signed-rank test is a nonparametric test of nonindependent data from only two groups.
- The Skillings–Mack test is a general Friedman-type statistic that can be used in almost any block design with an arbitrary missing-data structure.
- The Wittkowski test is a general Friedman-Type statistics similar to Skillings-Mack test. When the data do not contain any missing value, it gives the same result as Friedman test. But if the data contain missing values, it is both, more precise and sensitive than Skillings-Mack test.

## Post hoc analysis

Post-hoc tests were proposed by Schaich and Hamerle (1984) as well as Conover (1971, 1980) in order to decide which groups are significantly different from each other, based upon the mean rank differences of the groups. These procedures are detailed in Bortz, Lienert and Boehnke (2000, p. 275). Eisinga, Heskes, Pelzer and Te Grotenhuis (2017) provide an exact test for pairwise comparison of Friedman rank sums, implemented in R. The Eisinga c.s. exact test offers a substantial improvement over available approximate tests, especially if the number of groups ( k ) is large and the number of blocks ( n ) is small.

Not all statistical packages support post-hoc analysis for Friedman's test, but user-contributed code exists that provides these facilities (for example in SPSS, and in R.). The R package titled PMCMRplus contains numerous non-parametric methods for post-hoc analysis after Friedman, including support for the Nemenyi test.

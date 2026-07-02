---
title: "Šidák correction"
source: https://en.wikipedia.org/wiki/Šidák_correction
domain: bonferroni-correction
license: CC-BY-SA-4.0
tags: Bonferroni correction, Holm Bonferroni, Sidak correction, union bound
fetched: 2026-07-02
---

# Šidák correction

In statistics, the **Šidák correction**, or **Dunn–Šidák correction**, is a method used to counteract the problem of multiple comparisons. It is a simple method to control the family-wise error rate. When all null hypotheses are true, the method provides familywise error control that is exact for tests that are stochastically independent, conservative for tests that are positively dependent, and liberal for tests that are negatively dependent. It is credited to a 1967 paper by the statistician and probabilist Zbyněk Šidák. The Šidák method can be used to adjust alpha levels, p-values, or confidence intervals.

## Usage

- Given *m* different null hypotheses and a familywise alpha level of $\alpha$ , each null hypothesis is rejected that has a p-value lower than $1-(1-\alpha )^{\frac {1}{m}}$ .
- This test produces a familywise Type I error rate of exactly $\alpha$ when the tests are independent of each other and all null hypotheses are true. It is less stringent than the Bonferroni correction, but only slightly. For example, for $\alpha$ = 0.05 and *m* = 10, the Bonferroni-adjusted level is 0.005 and the Šidák-adjusted level is approximately 0.005116.
- One can also compute confidence intervals matching the test decision using the Šidák correction by computing each confidence interval at the $\cdot$ (1 − α)1/*m* % level.

Though slightly less conservative than Bonferroni, it tends to be a more conservative method of familywise error control compared to many other methods, especially when tests are positively dependent.

## Proof

The Šidák correction is derived by assuming that the individual tests are independent. Let the significance threshold for each test be $\alpha _{1}$ ; then the probability that at least one of the tests is significant under this threshold is (1 - the probability that none of them are significant). Since it is assumed that they are independent, the probability that all of them are not significant is the product of the probability that each of them is not significant, or $1-(1-\alpha _{1})^{m}$ . Our intention is for this probability to equal $\alpha$ , the significance threshold for the entire series of tests. By solving for $\alpha _{1}$ , we obtain $\alpha _{1}=1-(1-\alpha )^{1/m}.$ It shows that in order to reach a given $\alpha$ level, we need to adapt the $\alpha _{1}$ values used for each test.

## Šidák correction for t-test

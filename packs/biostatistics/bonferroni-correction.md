---
title: "Bonferroni correction"
source: https://en.wikipedia.org/wiki/Bonferroni_correction
domain: biostatistics
license: CC-BY-SA-4.0
tags: biostatistics methods, survival analysis, hypothesis testing, statistical power
fetched: 2026-07-02
---

# Bonferroni correction

**Bonferroni correction** is a method to counteract the multiple comparisons problem in statistics. It is named after the mathematician Carlo Emilio Bonferroni.

## Background

Statistical hypothesis testing is based on rejecting the null hypothesis when the likelihood of the observed data would be low if the null hypothesis were true. When multiple hypotheses are tested, the probability of observing a rare event increases, so the likelihood of incorrectly rejecting a null hypothesis (i.e., making a Type I error) increases if multiple null hypotheses are true.

The Bonferroni correction compensates for that increase by testing each individual hypothesis at a significance level of $\alpha /m$ , where $\alpha$ is the desired overall alpha level and m is the number of hypotheses. For example, if a trial is testing $m=20$ hypotheses with a desired overall $\alpha =0.05$ , the Bonferroni-corrected alpha level would be $\alpha =0.05/20=0.0025$ . The method is named for its use of the Bonferroni inequalities.

The Bonferroni correction can also be applied as a p-value adjustment: Using that approach, instead of adjusting the alpha level, each p-value is multiplied by the number of tests (with adjusted p-values that exceed 1 then being reduced to 1), and the alpha level is left unchanged. The significance decisions using this approach will be the same as when using the alpha-level adjustment approach.

## Definition

Let $H_{1},\ldots ,H_{m}$ be a family of null hypotheses and let $p_{1},\ldots ,p_{m}$ be their corresponding p-values. Let m be the total number of null hypotheses, and let $m_{0}$ be the number of true null hypotheses (which is presumably unknown to the researcher). The family-wise error rate (FWER) is the probability of rejecting at least one true $H_{i}$ , that is, of making at least one type I error. The Bonferroni correction rejects the null hypothesis for each $p_{i}\leq {\frac {\alpha }{m}}$ , thereby controlling the FWER at $\leq \alpha$ . Proof of this control follows from Boole's inequality, as follows:

${\text{FWER}}=P\left\{\bigcup _{i=1}^{m_{0}}\left(p_{i}\leq {\frac {\alpha }{m}}\right)\right\}\leq \sum _{i=1}^{m_{0}}\left\{P\left(p_{i}\leq {\frac {\alpha }{m}}\right)\right\}\leq m_{0}{\frac {\alpha }{m}}\leq \alpha .$

This control does not require any assumptions about dependence among the p-values or about how many of the null hypotheses are true.

## Extensions

### Generalization

Rather than testing each hypothesis at the $\alpha /m$ level, the hypotheses may be tested at any other combination of levels that add up to $\alpha$ , provided that the level of each test is decided before looking at the data. For example, for two hypothesis tests, an overall $\alpha$ of 0.05 could be maintained by conducting one test at 0.04 and the other at 0.01.

### Confidence intervals

The procedure proposed by Dunn can be used to adjust confidence intervals. If one establishes m confidence intervals, and wishes to have an overall confidence level of $1-\alpha$ , each individual confidence interval can be adjusted to the level of $1-{\frac {\alpha }{m}}$ .

### Continuous problems

When searching for a signal in a continuous parameter space there can also be a problem of multiple comparisons, or look-elsewhere effect. For example, a physicist might be looking to discover a particle of unknown mass by considering a large range of masses; this was the case during the Nobel Prize winning detection of the Higgs boson. In such cases, one can apply a continuous generalization of the Bonferroni correction by employing Bayesian logic to relate the effective number of trials, m , to the prior-to-posterior volume ratio.

## Alternatives

There are alternative ways to control the family-wise error rate. For example, the Holm–Bonferroni method and the Šidák correction are universally more powerful procedures than the Bonferroni correction, meaning that they are always at least as powerful. But unlike the Bonferroni procedure, these methods do not control the expected number of Type I errors per family (the per-family Type I error rate).

## Criticism

With respect to Family-wise error rate (FWER) control, the Bonferroni correction can be conservative if there are a large number of tests and/or the test statistics are positively correlated, due to looseness of the union bound for significantly overlapping sets.

Multiple-testing corrections, including the Bonferroni procedure, increase the probability of Type II errors when null hypotheses are false, i.e., they reduce statistical power.

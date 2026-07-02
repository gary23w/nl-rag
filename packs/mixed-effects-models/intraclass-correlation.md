---
title: "Intraclass correlation"
source: https://en.wikipedia.org/wiki/Intraclass_correlation
domain: mixed-effects-models
license: CC-BY-SA-4.0
tags: mixed model, random effects, fixed effects, intraclass correlation
fetched: 2026-07-02
---

# Intraclass correlation

In statistics, the **intraclass correlation**, or the **intraclass correlation coefficient** (**ICC**), is a descriptive statistic that can be used when quantitative measurements are made on units that are organized into groups. It describes how strongly units in the same group resemble each other. While it is viewed as a type of correlation, unlike most other correlation measures, it operates on data structured as groups rather than data structured as paired observations.

The *intraclass correlation* is commonly used to quantify the degree to which individuals with a fixed degree of relatedness (e.g. full siblings) resemble each other in terms of a quantitative trait (see heritability). Another prominent application is the assessment of consistency or reproducibility of quantitative measurements made by different observers measuring the same quantity.

## Early ICC definition: unbiased but complex formula

The earliest work on intraclass correlations focused on the case of paired measurements, and the first intraclass correlation (ICC) statistics to be proposed were modifications of the interclass correlation (Pearson correlation).

Consider a data set consisting of *N* paired data values (*x**n*,1, *x**n*,2), for *n* = 1, ..., *N*. The intraclass correlation *r* originally proposed by Ronald Fisher is

$r={\frac {1}{Ns^{2}}}\sum _{n=1}^{N}(x_{n,1}-{\bar {x}})(x_{n,2}-{\bar {x}}),$

where

${\bar {x}}={\frac {1}{2N}}\sum _{n=1}^{N}(x_{n,1}+x_{n,2}),$

$s^{2}={\frac {1}{2N}}\left\{\sum _{n=1}^{N}(x_{n,1}-{\bar {x}})^{2}+\sum _{n=1}^{N}(x_{n,2}-{\bar {x}})^{2}\right\}.$

Later versions of this statistic used the degrees of freedom 2*N* −1 in the denominator for calculating *s*2 and *N* −1 in the denominator for calculating *r*, so that *s*2 becomes unbiased, and *r* becomes unbiased if *s* is known.

The key difference between this ICC and the interclass (Pearson) correlation is that the data are pooled to estimate the mean and variance. The reason for this is that in the setting where an intraclass correlation is desired, the pairs are considered to be unordered. For example, if we are studying the resemblance of twins, there is usually no meaningful way to order the values for the two individuals within a twin pair. Like the interclass correlation, the intraclass correlation for paired data will be confined to the interval [−1, +1].

The intraclass correlation is also defined for data sets with groups having more than 2 values. For groups consisting of three values, it is defined as

$r={\frac {1}{3Ns^{2}}}\sum _{n=1}^{N}\left\{(x_{n,1}-{\bar {x}})(x_{n,2}-{\bar {x}})+(x_{n,1}-{\bar {x}})(x_{n,3}-{\bar {x}})+(x_{n,2}-{\bar {x}})(x_{n,3}-{\bar {x}})\right\},$

where

${\bar {x}}={\frac {1}{3N}}\sum _{n=1}^{N}(x_{n,1}+x_{n,2}+x_{n,3}),$

$s^{2}={\frac {1}{3N}}\left\{\sum _{n=1}^{N}(x_{n,1}-{\bar {x}})^{2}+\sum _{n=1}^{N}(x_{n,2}-{\bar {x}})^{2}+\sum _{n=1}^{N}(x_{n,3}-{\bar {x}})^{2}\right\}.$

As the number of items per group grows, so does the number of cross-product terms in this expression grows. The following equivalent form is simpler to calculate:

$r={\frac {K}{K-1}}\cdot {\frac {N^{-1}\sum _{n=1}^{N}({\bar {x}}_{n}-{\bar {x}})^{2}}{s^{2}}}-{\frac {1}{K-1}},$

where *K* is the number of data values per group, and ${\bar {x}}_{n}$ is the sample mean of the *n*th group. This form is usually attributed to Harris. The left term is non-negative; consequently the intraclass correlation must satisfy

$r\geq {\frac {-1}{K-1}}.$

For large *K*, this ICC is nearly equal to

${\frac {N^{-1}\sum _{n=1}^{N}({\bar {x}}_{n}-{\bar {x}})^{2}}{s^{2}}},$

which can be interpreted as the fraction of the total variance that is due to variation between groups. Ronald Fisher devotes an entire chapter to intraclass correlation in his classic book *Statistical Methods for Research Workers*.

For data from a population that is completely noise, Fisher's formula produces ICC values that are distributed about 0, i.e. sometimes being negative. This is because Fisher designed the formula to be unbiased, and therefore its estimates are sometimes overestimates and sometimes underestimates. For small or 0 underlying values in the population, the ICC calculated from a sample may be negative.

## Modern ICC definitions: simpler formula but positive bias

Beginning with Ronald Fisher, the intraclass correlation has been regarded within the framework of analysis of variance (ANOVA), and more recently in the framework of random effects models. A number of ICC estimators have been proposed. Most of the estimators can be defined in terms of the random effects model

$Y_{ij}=\mu +\alpha _{j}+\varepsilon _{ij},$

where *Y**ij* is the *i*th observation in the *j*th group, *μ* is an unobserved overall mean, *αj* is an unobserved random effect shared by all values in group *j*, and *εij* is an unobserved noise term. For the model to be identified, the *αj* and *εij* are assumed to have expected value zero and to be uncorrelated with each other. Also, the *αj* are assumed to be identically distributed, and the *εij* are assumed to be identically distributed. The variance of *αj* is denoted *σ*2 *α* and the variance of *ε**ij* is denoted *σ*2 *ε*.

The population ICC in this framework is

${\frac {\sigma _{\alpha }^{2}}{\sigma _{\alpha }^{2}+\sigma _{\varepsilon }^{2}}}.$

With this framework, the ICC is the correlation of two observations from the same group.

[Proof]

For a one-way random effects model:

$Y_{ij}=\mu +\alpha _{i}+\epsilon _{ij}$

$\alpha _{i}\sim N(0,\sigma _{\alpha }^{2})$ , $\epsilon _{ij}\sim N(0,\sigma _{\varepsilon }^{2})$ , $\alpha _{i}$ s and $\epsilon _{ij}$ s independent and $\alpha _{i}$ s are independent from $\epsilon _{ij}$ s.

The variance of any observation is: $Var(Y_{ij})=\sigma _{\varepsilon }^{2}+\sigma _{\alpha }^{2}$ The covariance of two observations from the same group i (for $j\neq k$ ) is:

${\begin{aligned}{\text{Cov}}(Y_{ij},Y_{ik})&={\text{Cov}}(\mu +\alpha _{i}+\epsilon _{ij},\mu +\alpha _{i}+\epsilon _{ik})\\&={\text{Cov}}(\alpha _{i}+\epsilon _{ij},\alpha _{i}+\epsilon _{ik})\\&={\text{Cov}}(\alpha _{i},\alpha _{i})+2{\text{Cov}}(\alpha _{i},\epsilon _{ik})+{\text{Cov}}(\epsilon _{ij},\epsilon _{ik})\\&={\text{Cov}}(\alpha _{i},\alpha _{i})\\&={\text{Var}}(\alpha _{i})\\&=\sigma _{\alpha }^{2}.\\\end{aligned}}$

In this, we've used properties of the covariance.

Put together we get: ${\text{Cor}}(Y_{ij},Y_{ik})={\frac {{\text{Cov}}(Y_{ij},Y_{ik})}{\sqrt {Var(Y_{ij})Var(Y_{ik})}}}={\frac {\sigma _{\alpha }^{2}}{\sigma _{\varepsilon }^{2}+\sigma _{\alpha }^{2}}}$

An advantage of this ANOVA framework is that different groups can have different numbers of data values, which is difficult to handle using the earlier ICC statistics. This ICC is always non-negative, allowing it to be interpreted as the proportion of total variance that is "between groups." This ICC can be generalized to allow for covariate effects, in which case the ICC is interpreted as capturing the within-class similarity of the covariate-adjusted data values.

This expression can never be negative (unlike Fisher's original formula) and therefore, in samples from a population which has an ICC of 0, the ICCs in the samples will be higher than the ICC of the population.

A number of different ICC statistics have been proposed, not all of which estimate the same population parameter. There has been considerable debate about which ICC statistics are appropriate for a given use, since they may produce markedly different results for the same data.

## Relationship to Pearson's correlation coefficient

In terms of its algebraic form, Fisher's original ICC is the ICC that most resembles the Pearson correlation coefficient. One key difference between the two statistics is that in the ICC, the data are centered and scaled using a pooled mean and standard deviation, whereas in the Pearson correlation, each variable is centered and scaled by its own mean and standard deviation. This pooled scaling for the ICC makes sense because all measurements are of the same quantity (albeit on units in different groups). For example, in a paired data set where each "pair" is a single measurement made for each of two units (e.g., weighing each twin in a pair of identical twins) rather than two different measurements for a single unit (e.g., measuring height and weight for each individual), the ICC is a more natural measure of association than Pearson's correlation.

An important property of the Pearson correlation is that it is invariant to application of separate linear transformations to the two variables being compared. Thus, if we are correlating *X* and *Y*, where, say, *Y* = 2*X* + 1, the Pearson correlation between *X* and *Y* is 1 — a perfect correlation. This property does not make sense for the ICC, since there is no basis for deciding which transformation is applied to each value in a group. However, if all the data in all groups are subjected to the same linear transformation, the ICC does not change.

## Use in assessing conformity among observers

The ICC is used to assess the consistency, or conformity, of measurements made by multiple observers measuring the same quantity. For example, if several physicians are asked to score the results of a CT scan for signs of cancer progression, we can ask how consistent the scores are with each other. If the truth is known (for example, if the CT scans were on patients who subsequently underwent exploratory surgery), then the focus would generally be on how well the physicians' scores matched the truth. If the truth is not known, we can only consider the similarity among the scores. An important aspect of this problem is that there is both inter-observer and intra-observer variability. Inter-observer variability refers to systematic differences among the observers — for example, one physician may consistently score patients at a higher risk level than other physicians. Intra-observer variability refers to deviations of a particular observer's score on a particular patient that are not part of a systematic difference.

The ICC is constructed to be applied to exchangeable measurements — that is, grouped data in which there is no meaningful way to order the measurements within a group. In assessing conformity among observers, if the same observers rate each element being studied, then systematic differences among observers are likely to exist, which conflicts with the notion of exchangeability. If the ICC is used in a situation where systematic differences exist, the result is a composite measure of intra-observer and inter-observer variability. One situation where exchangeability might reasonably be presumed to hold would be where a specimen to be scored, say a blood specimen, is divided into multiple aliquots, and the aliquots are measured separately on the same instrument. In this case, exchangeability would hold as long as no effect due to the sequence of running the samples was present.

Since the *intraclass correlation coefficient* gives a composite of intra-observer and inter-observer variability, its results are sometimes considered difficult to interpret when the observers are not exchangeable. Alternative measures such as Cohen's kappa statistic, the Fleiss kappa, and the concordance correlation coefficient have been proposed as more suitable measures of agreement among non-exchangeable observers.

## Calculation in software packages

ICC is supported in the open source software package R (using the function "icc" with the packages *psy* or *irr*, or via the function "ICC" in the package *psych*.) The rptR package provides methods for the estimation of ICC and repeatabilities for Gaussian, binomial and Poisson distributed data in a mixed-model framework. Notably, the package allows estimation of adjusted ICC (i.e. controlling for other variables) and computes confidence intervals based on parametric bootstrapping and significances based on the permutation of residuals. Commercial software also supports ICC, for instance Stata or SPSS

| Shrout and Fleiss convention | McGraw and Wong convention | Name in SPSS and Stata |
|---|---|---|
| ICC(1,1) | One-way random, single score ICC(1) | One-way random, single measures |
| ICC(2,1) | Two-way random, single score ICC(A,1) | Two-way random, single measures, absolute agreement |
| ICC(3,1) | Two-way mixed, single score ICC(C,1) | Two-way mixed, single measures, consistency |
| undefined | Two-way random, single score ICC(C,1) | Two-way random, single measures, consistency |
| undefined | Two-way mixed, single score ICC(A,1) | Two-way mixed, single measures, absolute agreement |
| ICC(1,k) | One-way random, average score ICC(k) | One-way random, average measures |
| ICC(2,k) | Two-way random, average score ICC(A,k) | Two-way random, average measures, absolute agreement |
| ICC(3,k) | Two-way mixed, average score ICC(C,k) | Two-way mixed, average measures, consistency |
| undefined | Two-way random, average score ICC(C,k) | Two-way random, average measures, consistency |
| undefined | Two-way mixed, average score ICC(A,k) | Two-way mixed, average measures, absolute agreement |

The three models are:

- One-way random effects: each subject is measured by a different set of k randomly selected raters;
- Two-way random: k raters are randomly selected, then, each subject is measured by the same set of k raters;
- Two-way mixed: k fixed raters are defined. Each subject is measured by the k raters.

Number of measurements:

- Single measures: even though more than one measure is taken in the experiment, reliability is applied to a context where a single measure of a single rater will be performed;
- Average measures: the reliability is applied to a context where measures of k raters will be averaged for each subject.

Consistency or absolute agreement:

- Absolute agreement: the agreement between two raters is of interest, including systematic errors of both raters and random residual errors;
- Consistency: in the context of repeated measurements by the same rater, systematic errors of the rater are canceled and only the random residual error is kept.

The consistency ICC cannot be estimated in the one-way random effects model, as there is no way to separate the inter-rater and residual variances.

An overview and re-analysis of the three models for the single measures ICC, with an alternative recipe for their use, has also been presented by Liljequist et al. (2019).

## Interpretation

Cicchetti (1994) gives the following often quoted guidelines for interpretation for kappa or ICC inter-rater agreement measures:

- Less than 0.40—poor.
- Between 0.40 and 0.59—fair.
- Between 0.60 and 0.74—good.
- Between 0.75 and 1.00—excellent.

A different guideline is given by Koo and Li (2016):

- below 0.50: poor
- between 0.50 and 0.75: moderate
- between 0.75 and 0.90: good
- above 0.90: excellent

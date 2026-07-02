---
title: "Random effects model"
source: https://en.wikipedia.org/wiki/Random_effect
domain: mixed-effects-models
license: CC-BY-SA-4.0
tags: mixed model, random effects, fixed effects, intraclass correlation
fetched: 2026-07-02
---

# Random effects model

(Redirected from

Random effect

)

In econometrics, a **random effects model**, also called a **variance components model**, is a statistical model where the model effects are random variables. It is a kind of hierarchical linear model, which assumes that the data being analysed are drawn from a hierarchy of different populations whose differences relate to that hierarchy. A random effects model is a special case of a mixed model.

Contrast this to the biostatistics definitions, as biostatisticians use "fixed" and "random" effects to respectively refer to the population-average and subject-specific effects (and where the latter are generally assumed to be unknown, latent variables).

## Qualitative description

Random effect models assist in controlling for unobserved heterogeneity when the heterogeneity is constant over time and not correlated with independent variables. Two common assumptions can be made about the individual specific effect: the random effects assumption and the fixed effects assumption. The random effects assumption is that the individual unobserved heterogeneity is uncorrelated with the independent variables. The fixed effect assumption is that the individual specific effect can be correlated with the independent variables.

If the random effects assumption holds, the random effects estimator is more efficient than the fixed effects model.

## Simple example

Suppose m large elementary schools are chosen randomly from among thousands in a large country. Suppose also that n pupils of the same age are chosen randomly at each selected school. Their scores on a standard aptitude test are ascertained. Let $Y_{ij}$ be the score of the j -th pupil at the i -th school.

A simple way to model this variable is

$Y_{ij}=\mu +U_{i}+W_{ij},\,$

where $\mu$ is the average test score for the entire population.

In this model $U_{i}$ is the school-specific **random effect**: it measures the difference between the average score at school i and the average score in the entire country. The term $W_{ij}$ is the individual-specific random effect, i.e., it's the deviation of the j -th pupil's score from the average for the i -th school.

The model can be augmented by including additional explanatory variables, which would capture differences in scores among different groups. For example:

$Y_{ij}=\mu +\beta _{1}\mathrm {Sex} _{ij}+\beta _{2}\mathrm {ParentsEduc} _{ij}+U_{i}+W_{ij},\,$

where $\mathrm {Sex} _{ij}$ is a binary dummy variable and $\mathrm {ParentsEduc} _{ij}$ records, say, the average education level of a child's parents. This is a mixed model, not a purely random effects model, as it introduces fixed-effects terms for Sex and Parents' Education.

### Variance components

The variance of $Y_{ij}$ is the sum of the variances $\tau ^{2}$ and $\sigma ^{2}$ of $U_{i}$ and $W_{ij}$ respectively.

Let

${\overline {Y}}_{i\bullet }={\frac {1}{n}}\sum _{j=1}^{n}Y_{ij}$

be the average, not of all scores at the i -th school, but of those at the i -th school that are included in the random sample. Let

${\overline {Y}}_{\bullet \bullet }={\frac {1}{mn}}\sum _{i=1}^{m}\sum _{j=1}^{n}Y_{ij}$

be the grand average.

Let

$SSW=\sum _{i=1}^{m}\sum _{j=1}^{n}(Y_{ij}-{\overline {Y}}_{i\bullet })^{2}\,$

$SSB=n\sum _{i=1}^{m}({\overline {Y}}_{i\bullet }-{\overline {Y}}_{\bullet \bullet })^{2}\,$

be respectively the sum of squares due to differences *within* groups and the sum of squares due to difference *between* groups. Then it can be shown that

${\frac {1}{m(n-1)}}E(SSW)=\sigma ^{2}$

and

${\frac {1}{(m-1)n}}E(SSB)={\frac {\sigma ^{2}}{n}}+\tau ^{2}.$

These "expected mean squares" can be used as the basis for estimation of the "variance components" $\sigma ^{2}$ and *$\tau ^{2}$*.

The $\sigma ^{2}$ parameter is also called the intraclass correlation coefficient.

## Marginal likelihood

For random effects models the marginal likelihoods are important.

## Applications

Random effects models used in practice include the Bühlmann model of insurance contracts and the Fay-Herriot model used for small area estimation.

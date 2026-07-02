---
title: "Multivariate analysis of variance"
source: https://en.wikipedia.org/wiki/Multivariate_analysis_of_variance
domain: manova
license: CC-BY-SA-4.0
tags: multivariate analysis of variance, Wilks lambda, Hotelling T-squared, Box M test
fetched: 2026-07-02
---

# Multivariate analysis of variance

In statistics, **multivariate analysis of variance** (**MANOVA**) is a procedure for comparing multivariate sample means. As a multivariate procedure, it is used when there are two or more dependent variables, and is often followed by significance tests involving individual dependent variables separately.

Without relation to the image, the dependent variables may be k life satisfactions scores measured at sequential time points and p job satisfaction scores measured at sequential time points. In this case there are k+p dependent variables whose linear combination follows a multivariate normal distribution, multivariate variance-covariance matrix homogeneity, and linear relationship, no multicollinearity, and each without outliers.

## Model

Assume ${\textstyle n}$ ${\textstyle q}$ -dimensional observations, where the ${\textstyle i}$ ’th observation ${\textstyle y_{i}}$ is assigned to the group ${\textstyle g(i)\in \{1,\dots ,m\}}$ and is distributed around the group center ${\textstyle \mu ^{(g(i))}\in \mathbb {R} ^{q}}$ with multivariate Gaussian noise: $y_{i}=\mu ^{(g(i))}+\varepsilon _{i}\quad \varepsilon _{i}{\overset {\text{i.i.d.}}{\sim }}{\mathcal {N}}_{q}(0,\Sigma )\quad {\text{ for }}i=1,\dots ,n,$ where ${\textstyle \Sigma }$ is the covariance matrix. Then we formulate our null hypothesis as $H_{0}\!:\;\mu ^{(1)}=\mu ^{(2)}=\dots =\mu ^{(m)}.$

## Relationship with ANOVA

MANOVA is a generalized form of univariate analysis of variance (ANOVA), although, unlike univariate ANOVA, it uses the covariance between outcome variables in testing the statistical significance of the mean differences.

Where sums of squares appear in univariate analysis of variance, in multivariate analysis of variance certain positive-definite matrices appear. The diagonal entries are the same kinds of sums of squares that appear in univariate ANOVA. The off-diagonal entries are corresponding sums of products. Under normality assumptions about error distributions, the counterpart of the sum of squares due to error has a Wishart distribution.

## Hypothesis Testing

First, define the following ${\textstyle n\times q}$ matrices:

- ${\textstyle Y}$ : where the ${\textstyle i}$ -th row is equal to ${\textstyle y_{i}}$

- ${\textstyle {\hat {Y}}}$ : where the ${\textstyle i}$ -th row is the best prediction given the group membership ${\textstyle g(i)}$ . That is the mean over all observation in group ${\textstyle g(i)}$ : ${\textstyle {\frac {1}{{\text{size of group }}g(i)}}\sum _{k:g(k)=g(i)}y_{k}}$ .

- ${\textstyle {\bar {Y}}}$ : where the ${\textstyle i}$ -th row is the best prediction given no information. That is the empirical mean over all ${\textstyle n}$ observations ${\textstyle {\frac {1}{n}}\sum _{k=1}^{n}y_{k}}$

Then the matrix ${\textstyle S_{\text{model}}:=({\hat {Y}}-{\bar {Y}})^{T}({\hat {Y}}-{\bar {Y}})}$ is a generalization of the sum of squares explained by the group, and ${\textstyle S_{\text{res}}:=(Y-{\hat {Y}})^{T}(Y-{\hat {Y}})}$ is a generalization of the residual sum of squares. Note that alternatively one could also speak about covariances when the abovementioned matrices are scaled by 1/(n-1) since the subsequent test statistics do not change by multiplying ${\textstyle S_{\text{model}}}$ and ${\textstyle S_{\text{res}}}$ by the same non-zero constant.

The most common statistics are summaries based on the roots (or eigenvalues) ${\textstyle \lambda _{p}}$ of the matrix ${\textstyle A:=S_{\text{model}}S_{\text{res}}^{-1}}$

- Samuel Stanley Wilks' $\Lambda _{\text{Wilks}}=\prod _{1,\ldots ,p}(1/(1+\lambda _{p}))=\det(I+A)^{-1}=\det(S_{\text{res}})/\det(S_{\text{res}}+S_{\text{model}})$ distributed as lambda (Λ)
- the K. C. Sreedharan Pillai–M. S. Bartlett trace, $\Lambda _{\text{Pillai}}=\sum _{1,\ldots ,p}(\lambda _{p}/(1+\lambda _{p}))=\operatorname {tr} (A(I+A)^{-1})$
- the Lawley–Hotelling trace, $\Lambda _{\text{LH}}=\sum _{1,\ldots ,p}(\lambda _{p})=\operatorname {tr} (A)$
- Roy's greatest root (also called *Roy's largest root*), $\Lambda _{\text{Roy}}=\max _{p}(\lambda _{p})$

Discussion continues over the merits of each, although the greatest root leads only to a bound on significance which is not generally of practical interest. A further complication is that, except for the Roy's greatest root, the distribution of these statistics under the null hypothesis is not straightforward and can only be approximated except in a few low-dimensional cases. An algorithm for the distribution of the Roy's largest root under the null hypothesis was derived in while the distribution under the alternative is studied in.

The best-known approximation for Wilks' lambda was derived by C. R. Rao.

In the case of two groups, all the statistics are equivalent and the test reduces to Hotelling's T-square.

## Introducing covariates (MANCOVA)

One can also test if there is a group effect after adjusting for covariates. For this, follow the procedure above but substitute ${\textstyle {\hat {Y}}}$ with the predictions of the general linear model, containing the group and the covariates, and substitute ${\textstyle {\bar {Y}}}$ with the predictions of the general linear model containing only the covariates (and an intercept). Then ${\textstyle S_{\text{model}}}$ are the additional sum of squares explained by adding the grouping information and ${\textstyle S_{\text{res}}}$ is the residual sum of squares of the model containing the grouping and the covariates.

Note that in case of unbalanced data, the order of adding the covariates matters.

## Correlation of dependent variables

MANOVA's power is affected by the correlations of the dependent variables and by the effect sizes associated with those variables. For example, when there are two groups and two dependent variables, MANOVA's power is lowest when the correlation equals the ratio of the smaller to the larger standardized effect size.

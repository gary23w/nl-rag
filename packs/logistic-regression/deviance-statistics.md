---
title: "Deviance (statistics)"
source: https://en.wikipedia.org/wiki/Deviance_(statistics)
domain: logistic-regression
license: CC-BY-SA-4.0
tags: logistic regression, logit, odds ratio, probit model
fetched: 2026-07-02
---

# Deviance (statistics)

In statistics, **deviance** is a goodness-of-fit statistic for a statistical model; it is often used for statistical hypothesis testing. It is a generalization of the idea of using the sum of squares of residuals (SSR) in ordinary least squares to cases where model-fitting is achieved by maximum likelihood. It plays an important role in exponential dispersion models and generalized linear models.

Deviance can be related to Kullback–Leibler divergence.

## Definition

The unit deviance $d(y,\mu )$ is a bivariate function that satisfies the following conditions:

- $d(y,y)=0$
- $d(y,\mu )>0\quad \forall y\neq \mu$

The total deviance $D(\mathbf {y} ,{\hat {\boldsymbol {\mu }}})$ of a model with predictions ${\hat {\boldsymbol {\mu }}}$ of the observation $\mathbf {y}$ is the sum of its unit deviances: ${\textstyle D(\mathbf {y} ,{\hat {\boldsymbol {\mu }}})=\sum _{i}d(y_{i},{\hat {\mu }}_{i})}$ .

The (total) deviance for a model *M*0 with estimates ${\hat {\mu }}=E[Y|{\hat {\theta }}_{0}]$ , based on a dataset *y*, may be constructed by its likelihood as: $D(y,{\hat {\mu }})=2\left(\log \left[p(y\mid {\hat {\theta }}_{s})\right]-\log \left[p(y\mid {\hat {\theta }}_{0})\right]\right).$

Here ${\hat {\theta }}_{0}$ denotes the fitted values of the parameters in the model *M*0, while ${\hat {\theta }}_{s}$ denotes the fitted parameters for the *saturated model*: both sets of fitted values are implicitly functions of the observations *y*. Here, the **saturated model** is a model with a parameter for every observation so that the data are fitted exactly. This expression is simply 2 times the log-likelihood ratio of the full model compared to the reduced model. The deviance is used to compare two models – in particular in the case of generalized linear models (GLM) where it has a similar role to residual sum of squares from ANOVA in linear models (RSS).

Suppose in the framework of the GLM, we have two nested models, *M1* and *M2*. In particular, suppose that *M1* contains the parameters in *M2*, and *k* additional parameters. Then, under the null hypothesis that *M2* is the true model, the difference between the deviances for the two models follows, based on Wilks' theorem, an approximate chi-squared distribution with *k*-degrees of freedom. This can be used for hypothesis testing on the deviance.

Some usage of the term "deviance" can be confusing. According to Collett:

"the quantity

$-2\log {\big [}p(y\mid {\hat {\theta }}_{0}){\big ]}$

is sometimes referred to as a

deviance

. This is [...] inappropriate, since unlike the deviance used in the context of generalized linear modelling,

$-2\log {\big [}p(y\mid {\hat {\theta }}_{0}){\big ]}$

does not measure deviation from a model that is a perfect fit to the data."

However, since the principal use is in the form of the difference of the deviances of two models, this confusion in definition is usually unimportant.

## Examples

The unit deviance for the Poisson distribution is $d(y,\mu )=2\left(y\log {\frac {y}{\mu }}-y+\mu \right)$ , the unit deviance for the normal distribution with unit variance is given by $d(y,\mu )=\left(y-\mu \right)^{2}$ .

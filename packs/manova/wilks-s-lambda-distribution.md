---
title: "Wilks's lambda distribution"
source: https://en.wikipedia.org/wiki/Wilks's_lambda_distribution
domain: manova
license: CC-BY-SA-4.0
tags: multivariate analysis of variance, Wilks lambda, Hotelling T-squared, Box M test
fetched: 2026-07-02
---

# Wilks's lambda distribution

In statistics, **Wilks' lambda distribution** (named for Samuel S. Wilks), is a probability distribution used in multivariate hypothesis testing, especially with regard to the likelihood-ratio test and multivariate analysis of variance (MANOVA).

## Definitions

Wilks' lambda distribution is defined from two independent Wishart distributed variables as the ratio distribution of their determinants,

given

$\mathbf {A} \sim W_{p}(\Sigma ,m)\qquad \mathbf {B} \sim W_{p}(\Sigma ,n)$

independent and with $m\geq p$

$\lambda ={\frac {\det(\mathbf {A} )}{\det(\mathbf {A+B} )}}={\frac {1}{\det(\mathbf {I} +\mathbf {A} ^{-1}\mathbf {B} )}}\sim \Lambda (p,m,n)$

where *p* is the number of dimensions. In the context of likelihood-ratio tests *m* is typically the error degrees of freedom, and *n* is the hypothesis degrees of freedom, so that $n+m$ is the total degrees of freedom.

## Properties

There is a symmetry among the parameters of the Wilks distribution,

$\Lambda (p,m,n)\sim \Lambda (n,m+n-p,p)$

### Approximations

Computations or tables of the Wilks' distribution for higher dimensions are not readily available and one usually resorts to approximations. One approximation is attributed to M. S. Bartlett and works for large *m* allows Wilks' lambda to be approximated with a chi-squared distribution

$\left({\frac {p-n+1}{2}}-m\right)\log \Lambda (p,m,n)\sim \chi _{np}^{2}.$

Another approximation is attributed to C. R. Rao.

The distribution can be related to a product of independent beta-distributed random variables

$u_{i}\sim B\left({\frac {m+i-p}{2}},{\frac {p}{2}}\right)$

$\prod _{i=1}^{n}u_{i}\sim \Lambda (p,m,n).$

As such it can be regarded as a multivariate generalization of the beta distribution.

It follows directly that for a one-dimension problem, when the Wishart distributions are one-dimensional with $p=1$ (i.e., chi-squared-distributed), then the Wilks' distribution equals the beta-distribution with a certain parameter set,

$\Lambda (1,m,n)\sim B\left({\frac {m}{2}},{\frac {n}{2}}\right).$

From the relations between a beta and an F-distribution, Wilks' lambda can be related to the F-distribution when one of the parameters of the Wilks lambda distribution is either 1 or 2, e.g.,

${\frac {1-\Lambda (p,m,1)}{\Lambda (p,m,1)}}\sim {\frac {p}{m-p+1}}F_{p,m-p+1},$

and

${\frac {1-{\sqrt {\Lambda (p,m,2)}}}{\sqrt {\Lambda (p,m,2)}}}\sim {\frac {p}{m-p+1}}F_{2p,2(m-p+1)}.$

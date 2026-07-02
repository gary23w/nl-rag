---
title: "Nonparametric regression"
source: https://en.wikipedia.org/wiki/Nonparametric_regression
domain: kaplan-meier
license: CC-BY-SA-4.0
tags: Kaplan Meier estimator, Nelson Aalen, logrank test, survival function
fetched: 2026-07-02
---

# Nonparametric regression

**Nonparametric regression** is a form of regression analysis where the predictor does not take a predetermined form but is completely constructed using information derived from the data. That is, no parametric equation is assumed for the relationship between predictors and dependent variable. A larger sample size is needed to build a nonparametric model having the same level of uncertainty as a parametric model because the data must supply both the model structure and the parameter estimates.

## Definition

Nonparametric regression assumes the following relationship, given the random variables X and Y :

$\mathbb {E} [Y\mid X=x]=m(x),$

where $m(x)$ is some deterministic function. Linear regression is a restricted case of nonparametric regression where $m(x)$ is assumed to be a linear function of the data. Sometimes a slightly stronger assumption of additive noise is used:

$Y=m(X)+U,$

where the random variable U is the `noise term', with mean 0. Without the assumption that m belongs to a specific parametric family of functions it is impossible to get an unbiased estimate for m , however most estimators are consistent under suitable conditions.

## Common nonparametric regression algorithms

This is a non-exhaustive list of non-parametric models for regression.

- nearest neighbor smoothing (see also k-nearest neighbors algorithm)
- regression trees
- kernel regression
- local regression
- multivariate adaptive regression splines
- smoothing splines
- neural networks

## Examples

### Gaussian process regression or Kriging

In Gaussian process regression, also known as Kriging, a Gaussian prior is assumed for the regression curve. The errors are assumed to have a multivariate normal distribution and the regression curve is estimated by its posterior mode. The Gaussian prior may depend on unknown hyperparameters, which are usually estimated via empirical Bayes. The hyperparameters typically specify a prior covariance kernel. In case the kernel should also be inferred nonparametrically from the data, the critical filter can be used.

Smoothing splines have an interpretation as the posterior mode of a Gaussian process regression.

### Kernel regression

Kernel regression estimates the continuous dependent variable from a limited set of data points by convolving the data points' locations with a kernel function—approximately speaking, the kernel function specifies how to "blur" the influence of the data points so that their values can be used to predict the value for nearby locations.

### Regression trees

Decision tree learning algorithms can be applied to learn to predict a dependent variable from data. Although the original Classification And Regression Tree (CART) formulation applied only to predicting univariate data, the framework can be used to predict multivariate data, including time series.

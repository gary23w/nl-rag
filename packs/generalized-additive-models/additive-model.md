---
title: "Additive model"
source: https://en.wikipedia.org/wiki/Additive_model
domain: generalized-additive-models
license: CC-BY-SA-4.0
tags: generalized additive model, backfitting, smoothing spline, kernel smoother
fetched: 2026-07-02
---

# Additive model

In statistics, an **additive model** (**AM**) is a nonparametric regression method. It was suggested by Jerome H. Friedman and Werner Stuetzle (1981) and is an essential part of the ACE algorithm. The *AM* uses a one-dimensional smoother to build a restricted class of nonparametric regression models. Because of this, it is less affected by the curse of dimensionality than a *p*-dimensional smoother. Furthermore, the *AM* is more flexible than a standard linear model, while being more interpretable than a general regression surface at the cost of approximation errors. Problems with *AM*, like many other machine-learning methods, include model selection, overfitting, and multicollinearity.

## Description

Given a data set $\{y_{i},\,x_{i1},\ldots ,x_{ip}\}_{i=1}^{n}$ of *n* statistical units, where $\{x_{i1},\ldots ,x_{ip}\}_{i=1}^{n}$ represent predictors and $y_{i}$ is the outcome, the *additive model* takes the form

$\mathrm {E} [y_{i}|x_{i1},\ldots ,x_{ip}]=\beta _{0}+\sum _{j=1}^{p}f_{j}(x_{ij})$

or

$Y=\beta _{0}+\sum _{j=1}^{p}f_{j}(X_{j})+\varepsilon$

Where $\mathrm {E} [\epsilon ]=0$ , $\mathrm {Var} (\epsilon )=\sigma ^{2}$ and $\mathrm {E} [f_{j}(X_{j})]=0$ . The functions $f_{j}(x_{ij})$ are unknown smooth functions fit from the data. Fitting the *AM* (i.e. the functions $f_{j}(x_{ij})$ ) can be done using the backfitting algorithm proposed by Andreas Buja, Trevor Hastie and Robert Tibshirani (1989).

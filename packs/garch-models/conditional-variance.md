---
title: "Conditional variance"
source: https://en.wikipedia.org/wiki/Conditional_variance
domain: garch-models
license: CC-BY-SA-4.0
tags: ARCH model, GARCH, conditional variance, volatility clustering
fetched: 2026-07-02
---

# Conditional variance

In probability theory and statistics, a **conditional variance** is the variance of a random variable given the value(s) of one or more other variables. Particularly in econometrics, the conditional variance is also known as the **scedastic function** or **skedastic function**. Conditional variances are important parts of autoregressive conditional heteroskedasticity (ARCH) models.

## Definition

The conditional variance of a random variable *Y* given another random variable *X* is

$\operatorname {Var} (Y\mid X)=\operatorname {E} {\Big (}{\big (}Y-\operatorname {E} (Y\mid X){\big )}^{2}\;{\Big |}\;X{\Big )}.$

The conditional variance tells us how much variance is left if we use $\operatorname {E} (Y\mid X)$ to "predict" *Y*. Here, as usual, $\operatorname {E} (Y\mid X)$ stands for the conditional expectation of *Y* given *X*, which we may recall, is a random variable itself (a function of *X*, determined up to probability one). As a result, $\operatorname {Var} (Y\mid X)$ itself is a random variable (and is a function of *X*).

## Explanation, relation to least-squares

Recall that variance is the expected squared deviation between a random variable (say, *Y*) and its expected value. The expected value can be thought of as a reasonable prediction of the outcomes of the random experiment (in particular, the expected value is the best constant prediction when predictions are assessed by expected squared prediction error). Thus, one interpretation of variance is that it gives the smallest possible expected squared prediction error. If we have the knowledge of another random variable (*X*) that we can use to predict *Y*, we can potentially use this knowledge to reduce the expected squared error. As it turns out, the best prediction of *Y* given *X* is the conditional expectation. In particular, for any $f:\mathbb {R} \to \mathbb {R}$ measurable,

${\begin{aligned}\operatorname {E} [(Y-f(X))^{2}]&=\operatorname {E} [(Y-\operatorname {E} (Y|X)\,\,+\,\,\operatorname {E} (Y|X)-f(X))^{2}]\\&=\operatorname {E} [\operatorname {E} \{(Y-\operatorname {E} (Y|X)\,\,+\,\,\operatorname {E} (Y|X)-f(X))^{2}|X\}]\\&=\operatorname {E} [\operatorname {Var} (Y|X)]+\operatorname {E} [(\operatorname {E} (Y|X)-f(X))^{2}]\,.\end{aligned}}$

By selecting $f(X)=\operatorname {E} (Y|X)$ , the second, nonnegative term becomes zero, showing the claim. Here, the second equality used the law of total expectation. We also see that the expected conditional variance of *Y* given *X* shows up as the irreducible error of predicting *Y* given only the knowledge of *X*.

## Special cases, variations

### Conditioning on discrete random variables

When *X* takes on countable many values $S=\{x_{1},x_{2},\dots \}$ with positive probability, i.e., it is a discrete random variable, we can introduce $\operatorname {Var} (Y|X=x)$ , the conditional variance of *Y* given that *X=x* for any *x* from *S* as follows:

$\operatorname {Var} (Y|X=x)=\operatorname {E} ((Y-\operatorname {E} (Y\mid X=x))^{2}\mid X=x)=\operatorname {E} (Y^{2}|X=x)-\operatorname {E} (Y|X=x)^{2},$

where recall that $\operatorname {E} (Z\mid X=x)$ is the conditional expectation of *Z* given that *X=x*, which is well-defined for $x\in S$ . An alternative notation for $\operatorname {Var} (Y|X=x)$ is $\operatorname {Var} _{Y\mid X}(Y|x).$

Note that here $\operatorname {Var} (Y|X=x)$ defines a constant for possible values of *x*, and in particular, $\operatorname {Var} (Y|X=x)$ , is *not* a random variable.

The connection of this definition to $\operatorname {Var} (Y|X)$ is as follows: Let *S* be as above and define the function $v:S\to \mathbb {R}$ as $v(x)=\operatorname {Var} (Y|X=x)$ . Then, $v(X)=\operatorname {Var} (Y|X)$ almost surely.

### Definition using conditional distributions

The "conditional expectation of *Y* given *X=x*" can also be defined more generally using the conditional distribution of *Y* given *X* (this exists in this case, as both here *X* and *Y* are real-valued).

In particular, letting $P_{Y|X}$ be the (regular) conditional distribution $P_{Y|X}$ of *Y* given *X*, i.e., $P_{Y|X}:{\mathcal {B}}\times \mathbb {R} \to [0,1]$ (the intention is that $P_{Y|X}(U,x)=P(Y\in U|X=x)$ almost surely over the support of *X*), we can define

$\operatorname {Var} (Y|X=x)=\int \left(y-\int y'P_{Y|X}(dy'|x)\right)^{2}P_{Y|X}(dy|x).$

This can, of course, be specialized to when *Y* is discrete itself (replacing the integrals with sums), and also when the conditional density of *Y* given *X=x* with respect to some underlying distribution exists.

## Components of variance

The law of total variance says

$\operatorname {Var} (Y)=\operatorname {E} (\operatorname {Var} (Y\mid X))+\operatorname {Var} (\operatorname {E} (Y\mid X)).$

In words: the variance of *Y* is the sum of the expected conditional variance of *Y* given *X* and the variance of the conditional expectation of *Y* given *X*. The first term captures the variation left after "using *X* to predict *Y*", while the second term captures the variation due to the mean of the prediction of *Y* due to the randomness of *X*.

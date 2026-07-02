---
title: "Shrinkage (statistics)"
source: https://en.wikipedia.org/wiki/Shrinkage_(statistics)
domain: ridge-lasso-regression
license: CC-BY-SA-4.0
tags: ridge regression, lasso regression, shrinkage estimator, L2 regularization
fetched: 2026-07-02
---

# Shrinkage (statistics)

In statistics, **shrinkage** is the reduction in the effects of sampling variation. In regression analysis, a fitted relationship appears to perform less well on a new data set than on the data set used for fitting. In particular the value of the coefficient of determination 'shrinks'. This idea is complementary to overfitting and, separately, to the standard adjustment made in the coefficient of determination to compensate for the subjective effects of further sampling, like controlling for the potential of new explanatory terms improving the model by chance: that is, the adjustment formula itself provides "shrinkage." But the adjustment formula yields an artificial shrinkage.

A **shrinkage estimator** is an estimator that, either explicitly or implicitly, incorporates the effects of shrinkage. In loose terms this means that a naive or raw estimate is improved by combining it with other information. The term relates to the notion that the improved estimate is made closer to the value supplied by the 'other information' than the raw estimate. In this sense, shrinkage is used to regularize ill-posed inference problems.

Shrinkage is implicit in Bayesian inference and penalized likelihood inference, and explicit in James–Stein-type inference. In contrast, simple types of maximum-likelihood and least-squares estimation procedures do not include shrinkage effects, although they can be used within shrinkage estimation schemes.

## Description

Many standard estimators can be improved, in terms of mean squared error (MSE), by shrinking them towards zero (or any other finite constant value). In other words, the improvement in the estimate from the corresponding reduction in the width of the confidence interval can outweigh the worsening of the estimate introduced by biasing the estimate towards zero (see bias-variance tradeoff).

Assume that the expected value of the raw estimate is not zero and consider other estimators obtained by multiplying the raw estimate by a certain parameter. A value for this parameter can be specified so as to minimize the MSE of the new estimate. For this value of the parameter, the new estimate will have a smaller MSE than the raw one, and thus it has been improved. An effect here may be to convert an unbiased raw estimate to an improved biased one.

## Examples

An example arises in the estimation of the population variance by sample variance. For a sample size of *n*, the use of a divisor *n*−1 in the usual formula (Bessel's correction) gives an unbiased estimator, while other divisors have lower MSE, at the expense of bias. The optimal choice of divisor (weighting of shrinkage) depends on the excess kurtosis of the population, as discussed at mean squared error: variance, but one can always do better (in terms of MSE) than the unbiased estimator; for the normal distribution a divisor of *n*+1 gives one which has the minimum mean squared error.

## Methods

Types of regression that involve shrinkage estimates include ridge regression, where coefficients derived from a regular least squares regression are brought closer to zero by multiplying by a constant (the *shrinkage factor*), and lasso regression, where coefficients are brought closer to zero by adding or subtracting a constant.

The use of shrinkage estimators in the context of regression analysis, where there may be a large number of explanatory variables, has been described by Copas. Here the values of the estimated regression coefficients are shrunk towards zero with the effect of reducing the mean square error of predicted values from the model when applied to new data. A later paper by Copas applies shrinkage in a context where the problem is to predict a binary response on the basis of binary explanatory variables.

Hausser and Strimmer "develop a James-Stein-type shrinkage estimator, resulting in a procedure that is highly efficient statistically as well as computationally. Despite its simplicity, it outperforms eight other entropy estimation procedures across a diverse range of sampling scenarios and data-generating models, even in cases of severe undersampling. ... method is fully analytic and hence computationally inexpensive. Moreover, procedure simultaneously provides estimates of the entropy and of the cell frequencies. The proposed shrinkage estimators of entropy and mutual information, as well as all other investigated entropy estimators, have been implemented in R (R Development Core Team, 2008). A corresponding R package 'entropy' was deposited in the R archive CRAN under the GNU General Public License."

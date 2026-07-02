---
title: "Errors and residuals"
source: https://en.wikipedia.org/wiki/Errors_and_residuals
domain: linear-regression
license: CC-BY-SA-4.0
tags: linear regression, ordinary least squares, regression coefficients, least squares
fetched: 2026-07-02
---

# Errors and residuals

In statistics and optimization, **errors** and **residuals** are two closely related and easily confused measures of the deviation of an observed value of an element of a statistical sample from its "true value" (not necessarily observable). The **error** of an observation is the deviation of the observed value from the true value of a quantity of interest (for example, a population mean). The **residual** is the difference between the observed value and the *estimated* value of the quantity of interest (for example, a sample mean). The distinction is most important in regression analysis, where the concepts are sometimes called the **regression errors** and **regression residuals** and where they lead to the concept of studentized residuals. In econometrics, "errors" are also called **disturbances**.

## Introduction

Suppose there is a series of observations from a univariate distribution and we want to estimate the mean of that distribution (the so-called location model). In this case, the errors are the deviations of the observations from the population mean, while the residuals are the deviations of the observations from the sample mean.

A **statistical error** (or **disturbance**) is the amount by which an observation differs from its expected value, the latter being based on the whole population from which the statistical unit was chosen randomly. For example, if the mean height in a population of 21-year-old men is 1.75 meters, and one randomly chosen man is 1.80 meters tall, then the "error" is 0.05 meters; if the randomly chosen man is 1.70 meters tall, then the "error" is −0.05 meters. The expected value, being the mean of the entire population, is typically unobservable, and hence the statistical error cannot be observed either.

A **residual** (or fitting deviation), on the other hand, is an observable *estimate* of the unobservable statistical error. Consider the previous example with men's heights and suppose we have a random sample of *n* people. The *sample mean* could serve as a good estimator of the *population* mean. Then we have:

- The difference between the height of each man in the sample and the unobservable *population* mean is a *statistical error*, whereas
- The difference between the height of each man in the sample and the observable *sample* mean is a *residual*.

Note that, because of the definition of the sample mean, the sum of the residuals within a random sample is necessarily zero, and thus the residuals are necessarily *not independent*. The statistical errors, on the other hand, are independent, and their sum within the random sample is almost surely not zero.

One can standardize statistical errors (especially of a normal distribution) in a z-score (or "standard score"), and standardize residuals in a *t*-statistic, or more generally studentized residuals.

## In univariate distributions

If we assume a normally distributed population with mean μ and standard deviation σ, and choose individuals independently, then we have

$X_{1},\dots ,X_{n}\sim N\left(\mu ,\sigma ^{2}\right)\,$

and the sample mean

${\overline {X}}={X_{1}+\cdots +X_{n} \over n}$

is a random variable distributed such that

${\overline {X}}\sim N\left(\mu ,{\frac {\sigma ^{2}}{n}}\right).$

The *statistical errors* are then

$e_{i}=X_{i}-\mu ,\,$

with expected values of zero, whereas the *residuals* are

$r_{i}=X_{i}-{\overline {X}}.$

The sum of squares of the **statistical errors**, divided by *σ*2, has a chi-squared distribution with *n* degrees of freedom:

${\frac {1}{\sigma ^{2}}}\sum _{i=1}^{n}e_{i}^{2}\sim \chi _{n}^{2}.$

However, this quantity is not observable as the population mean is unknown. The sum of squares of the **residuals**, on the other hand, is observable. The quotient of that sum by σ2 has a chi-squared distribution with only *n* − 1 degrees of freedom:

${\frac {1}{\sigma ^{2}}}\sum _{i=1}^{n}r_{i}^{2}\sim \chi _{n-1}^{2}.$

This difference between *n* and *n* − 1 degrees of freedom results in Bessel's correction for the estimation of sample variance of a population with unknown mean and unknown variance. No correction is necessary if the population mean is known.

### Remark

It is remarkable that the sum of squares of the residuals and the sample mean can be shown to be independent of each other, using, e.g. Basu's theorem. That fact, and the normal and chi-squared distributions given above form the basis of calculations involving the t-statistic:

$T={\frac {{\overline {X}}_{n}-\mu _{0}}{S_{n}/{\sqrt {n}}}},$

where ${\overline {X}}_{n}-\mu _{0}$ represents the errors, $S_{n}$ represents the sample standard deviation for a sample of size *n*, and unknown *σ*, and the denominator term $S_{n}/{\sqrt {n}}$ accounts for the standard deviation of the errors according to

$\operatorname {Var} \left({\overline {X}}_{n}\right)={\frac {\sigma ^{2}}{n}}.$

The probability distributions of the numerator and the denominator separately depend on the value of the unobservable population standard deviation *σ*, but *σ* appears in both the numerator and the denominator and cancels. That is fortunate because it means that even though we do not know *σ*, we know the probability distribution of this quotient: it has a Student's t-distribution with *n* − 1 degrees of freedom. We can therefore use this quotient to find a confidence interval for *μ*. This t-statistic can be interpreted as "the number of standard errors away from the regression line."

## Regressions

In regression analysis, the distinction between *errors* and *residuals* is subtle and important, and leads to the concept of studentized residuals. Given an unobservable function that relates the independent variable to the dependent variable – say, a line – the deviations of the dependent variable observations from this function are the unobservable errors. If one runs a regression on some data, then the deviations of the dependent variable observations from the *fitted* function are the residuals. If the linear model is applicable, a scatterplot of residuals plotted against the independent variable should be random about zero with no trend to the residuals. If the data exhibit a trend, the regression model is likely incorrect; for example, the true function may be a quadratic or higher order polynomial. If they are random, or have no trend, but "fan out" - they exhibit a phenomenon called heteroscedasticity. If all of the residuals are equal, or do not fan out, they exhibit homoscedasticity.

However, a terminological difference arises in the expression mean squared error (MSE). The mean squared error of a regression is a number computed from the sum of squares of the computed *residuals*, and not of the unobservable *errors*. If that sum of squares is divided by *n*, the number of observations, the result is the mean of the squared residuals. Since this is a biased estimate of the variance of the unobserved errors, the bias is removed by dividing the sum of the squared residuals by *df* = *n* − *p* − 1, instead of *n*, where *df* is the number of degrees of freedom (*n* minus the number of parameters (excluding the intercept) p being estimated - 1). This forms an unbiased estimate of the variance of the unobserved errors, and is called the mean squared error.

Another method to calculate the mean square of error when analyzing the variance of linear regression using a technique like that used in ANOVA (they are the same because ANOVA is a type of regression), the sum of squares of the residuals (aka sum of squares of the error) is divided by the degrees of freedom (where the degrees of freedom equal *n* − *p* − 1, where *p* is the number of parameters estimated in the model (one for each variable in the regression equation, not including the intercept)). One can then also calculate the mean square of the model by dividing the sum of squares of the model minus the degrees of freedom, which is just the number of parameters. Then the F value can be calculated by dividing the mean square of the model by the mean square of the error, and we can then determine significance (which is why you want the mean squares to begin with.).

However, because of the behavior of the process of regression, the *distributions* of residuals at different data points (of the input variable) may vary *even if* the errors themselves are identically distributed. Concretely, in a linear regression where the errors are identically distributed, the variability of residuals of inputs in the middle of the domain will be *higher* than the variability of residuals at the ends of the domain: linear regressions fit endpoints better than the middle. This is also reflected in the influence functions of various data points on the regression coefficients: endpoints have more influence.

Thus to compare residuals at different inputs, one needs to adjust the residuals by the expected variability of *residuals,* which is called studentizing. This is particularly important in the case of detecting outliers, where the case in question is somehow different from the others in a dataset. For example, a large residual may be expected in the middle of the domain, but considered an outlier at the end of the domain.

## Other uses of the word "error" in statistics

The use of the term "error" as discussed in the sections above is in the sense of a deviation of a value from a hypothetical unobserved value. At least two other uses also occur in statistics, both referring to observable prediction errors:

The *mean squared error* (MSE) refers to the amount by which the values predicted by an estimator differ from the quantities being estimated (typically outside the sample from which the model was estimated). The *root mean square error* (RMSE) is the square root of MSE. The *sum of squares of errors* (SSE) is the MSE multiplied by the sample size.

*Sum of squares of residuals* (SSR) is the sum of the squares of the deviations of the actual values from the predicted values, within the sample used for estimation. This is the basis for the least squares estimate, where the regression coefficients are chosen such that the SSR is minimal (i.e. its derivative is zero).

Likewise, the *sum of absolute errors* (SAE) is the sum of the absolute values of the residuals, which is minimized in the least absolute deviations approach to regression.

The **mean error** (ME) is the bias. The *mean residual* (MR) is always zero for least-squares estimators.

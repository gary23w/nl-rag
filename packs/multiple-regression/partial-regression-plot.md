---
title: "Partial regression plot"
source: https://en.wikipedia.org/wiki/Partial_regression_plot
domain: multiple-regression
license: CC-BY-SA-4.0
tags: multiple regression, multicollinearity, variance inflation factor, partial regression
fetched: 2026-07-02
---

# Partial regression plot

In applied statistics, a **partial regression plot** attempts to show the effect of adding another variable to a model that already has one or more independent variables. Partial regression plots are also referred to as **added variable plots**, **adjusted variable plots**, and **individual coefficient plots**.

## Motivation

When performing a linear regression with a single independent variable, a scatter plot of the response variable against the independent variable provides a good indication of the nature of the relationship. If there is more than one independent variable, things become more complicated since independent variables might be (negatively or positively) correlated. Although it can still be useful to generate scatter plots of the response variable against each of the independent variables, this does not take into account the effect of the other independent variables in the model. For example, due to omitted variable bias, a simple scatter plot might display a strong positive slope between $Y_{i}$ and $X_{i}$ , even when the true multivariate coefficient $\beta _{i}$ in the full model is negative.

## Calculation

Partial regression plots are formed by:

1. Computing the residuals of regressing the response variable against the independent variables but omitting *X*i
2. Computing the residuals from regressing *X*i against the remaining independent variables
3. Plotting the residuals from (1) against the residuals from (2).

Velleman and Welsch express this mathematically as:

$Y_{\bullet [i]}\mathrm {\ versus\ } X_{i\bullet [i]}$

where

Y

•[i]

= residuals from regressing Y (the response variable) against all the independent variables except Xi

X

i•[i]

= residuals from regressing

X

i

against the remaining independent variables.

## Properties

Velleman and Welsch list the following useful properties for this plot:

1. The least squares linear fit to this plot has an intercept of 0 and a slope $\beta _{i}$ , where $\beta _{i}$ corresponds to the regression coefficient for *X*i of a regression of Y on all of the covariates.
2. The residuals from the least squares linear fit to this plot are identical to the residuals from the least squares fit of the original model (Y against all the independent variables including Xi).
3. The influences of individual data values on the estimation of a coefficient are easy to see in this plot.
4. It is easy to see many kinds of failures of the model or violations of the underlying assumptions (nonlinearity, heteroscedasticity, unusual patterns). .

Partial regression plots are related to, but distinct from, partial residual plots. Partial regression plots are most commonly used to identify data points with high leverage and influential data points that might not have high leverage. Partial residual plots are most commonly used to identify the nature of the relationship between *Y* and *X*i (given the effect of the other independent variables in the model). Note that since the simple correlation between the two sets of residuals plotted is equal to the partial correlation between the response variable and *X*i, partial regression plots will show the correct strength of the linear relationship between the response variable and *X*i. This is not true for partial residual plots. On the other hand, for the partial regression plot, the x-axis is not *X*i. This limits its usefulness in determining the need for a transformation (which is the primary purpose of the partial residual plot).

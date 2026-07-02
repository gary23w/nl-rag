---
title: "Coefficient of multiple correlation"
source: https://en.wikipedia.org/wiki/Multiple_correlation
domain: multiple-regression
license: CC-BY-SA-4.0
tags: multiple regression, multicollinearity, variance inflation factor, partial regression
fetched: 2026-07-02
---

# Coefficient of multiple correlation

(Redirected from

Multiple correlation

)

In statistics, the **coefficient of multiple correlation** is a measure of how well a given variable can be predicted using a linear function of a set of other variables. It is the correlation between the variable's values and the best predictions that can be computed linearly from the predictive variables.

The coefficient of multiple correlation takes values between 0 and 1. Higher values indicate higher predictability of the dependent variable from the independent variables, with a value of 1 indicating that the predictions are exactly correct and a value of 0 indicating that no linear combination of the independent variables is a better predictor than is the fixed mean of the dependent variable.

The coefficient of multiple correlation is known as the square root of the coefficient of determination, but under the particular assumptions that an intercept is included and that the best possible linear predictors are used, whereas the coefficient of determination is defined for more general cases, including those of nonlinear prediction and those in which the predicted values have not been derived from a model-fitting procedure.

## Definition

The coefficient of multiple correlation, denoted *R*, is a scalar that is defined as the Pearson correlation coefficient between the predicted and the actual values of the dependent variable in a linear regression model that includes an intercept.

## Computation

The square of the coefficient of multiple correlation can be computed using the vector $\mathbf {c} ={(r_{x_{1}y},r_{x_{2}y},\dots ,r_{x_{N}y})}^{\top }$ of correlations $r_{x_{n}y}$ between the predictor variables $x_{n}$ (independent variables) and the target variable y (dependent variable), and the correlation matrix $R_{xx}$ of correlations between predictor variables. It is given by

$R^{2}=\mathbf {c} ^{\top }R_{xx}^{-1}\,\mathbf {c} ,$

where $\mathbf {c} ^{\top }$ is the transpose of $\mathbf {c}$ , and $R_{xx}^{-1}$ is the inverse of the matrix

$R_{xx}=\left({\begin{array}{cccc}r_{x_{1}x_{1}}&r_{x_{1}x_{2}}&\dots &r_{x_{1}x_{N}}\\r_{x_{2}x_{1}}&\ddots &&\vdots \\\vdots &&\ddots &\\r_{x_{N}x_{1}}&\dots &&r_{x_{N}x_{N}}\end{array}}\right).$

If all the predictor variables are uncorrelated, the matrix $R_{xx}$ is the identity matrix and $R^{2}$ simply equals $\mathbf {c} ^{\top }\,\mathbf {c}$ , the sum of the squared correlations with the dependent variable. If the predictor variables are correlated among themselves, the inverse of the correlation matrix $R_{xx}$ accounts for this.

The squared coefficient of multiple correlation can also be computed as the fraction of variance of the dependent variable that is explained by the independent variables, which in turn is 1 minus the unexplained fraction. The unexplained fraction can be computed as the sum of squares of residuals—that is, the sum of the squares of the prediction errors—divided by the sum of squares of deviations of the values of the dependent variable from its expected value.

## Properties

With more than two variables being related to each other, the value of the coefficient of multiple correlation depends on the choice of dependent variable: a regression of y on x and z will in general have a different R than will a regression of z on x and y . For example, suppose that in a particular sample the variable z is uncorrelated with both x and y , while x and y are linearly related to each other. Then a regression of z on y and x will yield an R of zero, while a regression of y on x and z will yield a strictly positive R . This follows since the correlation of y with its best predictor based on x and z is in all cases at least as large as the correlation of y with its best predictor based on x alone, and in this case with z providing no explanatory power it will be exactly as large.

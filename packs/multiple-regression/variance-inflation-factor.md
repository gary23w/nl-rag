---
title: "Variance inflation factor"
source: https://en.wikipedia.org/wiki/Variance_inflation_factor
domain: multiple-regression
license: CC-BY-SA-4.0
tags: multiple regression, multicollinearity, variance inflation factor, partial regression
fetched: 2026-07-02
---

# Variance inflation factor

In statistics, the **variance inflation factor** (**VIF**) is the ratio (quotient) of the variance of a parameter estimate when fitting a full model that includes other parameters to the variance of the parameter estimate if the model is fit with only the parameter on its own. The VIF provides an index that measures how much the variance (the square of the estimate's standard deviation) of an estimated regression coefficient is increased because of collinearity.

Cuthbert Daniel claims to have invented the concept behind the variance inflation factor, but did not come up with the name.

## Definition

Consider the following linear model with *k* independent variables:

Y

=

β

0

+

β

1

X

1

+

β

2

X

2

+ ... +

β

k

X

k

+

ε

.

The standard error of the estimate of *β**j* is the square root of the *j* + 1 diagonal element of *s*2(*X*′*X*)−1, where *s* is the root mean squared error (RMSE) (note that RMSE2 is a consistent estimator of the true variance of the error term, $\sigma ^{2}$ ); *X* is the regression design matrix — a matrix such that *X**i*, *j*+1 is the value of the *j*th independent variable for the *i*th case or observation, and such that *X**i*,1, the predictor vector associated with the intercept term, equals 1 for all *i*. It turns out that the square of this standard error, the estimated variance of the estimate of *β**j*, can be equivalently expressed as:

${\widehat {\operatorname {var} }}({\hat {\beta }}_{j})={\frac {s^{2}}{(n-1){\widehat {\operatorname {var} }}(X_{j})}}\cdot {\frac {1}{1-R_{j}^{2}}},$

where *R**j*2 is the multiple *R*2 for the regression of *X**j* on the other covariates (a regression that does not involve the response variable *Y*) and ${\hat {\beta }}_{j}$ are the coefficient estimates, id est, the estimates of ${\beta }_{j}$ . This identity separates the influences of several distinct factors on the variance of the coefficient estimate:

- *s*2: greater scatter in the data around the regression surface leads to proportionately more variance in the coefficient estimates
- *n*: greater sample size results in proportionately less variance in the coefficient estimates
- ${\widehat {\operatorname {var} }}(X_{j})$ : greater variability in a particular covariate leads to proportionately less variance in the corresponding coefficient estimate

The remaining term, 1 / (1 − *R**j*2) is the VIF. It reflects all other factors that influence the uncertainty in the coefficient estimates. The VIF equals 1 when the vector *X**j* is orthogonal to each column of the design matrix for the regression of *X**j* on the other covariates. By contrast, the VIF is greater than 1 when the vector *X**j* is not orthogonal to all columns of the design matrix for the regression of *X**j* on the other covariates. Finally, note that the VIF is invariant to the scaling of the variables (that is, we could scale each variable *X**j* by a constant *c**j* without changing the VIF).

${\widehat {\operatorname {var} }}({\hat {\beta }}_{j})=s^{2}[(X^{T}X)^{-1}]_{jj}$

Now let $r=X^{T}X$ , and without losing generality, we reorder the columns of *X* to set the first column to be $X_{j}$

$r^{-1}={\begin{bmatrix}r_{j,j}&r_{j,-j}\\r_{-j,j}&r_{-j,-j}\end{bmatrix}}^{-1}$

$r_{j,j}=X_{j}^{T}X_{j},r_{j,-j}=X_{j}^{T}X_{-j},r_{-j,j}=X_{-j}^{T}X_{j},r_{-j,-j}=X_{-j}^{T}X_{-j}$

.

By using Schur complement, the element in the first row and first column in $r^{-1}$ is,

$r_{1,1}^{-1}=[r_{j,j}-r_{j,-j}r_{-j,-j}^{-1}r_{-j,j}]^{-1}$

Then we have,

${\begin{aligned}&{\widehat {\operatorname {var} }}({\hat {\beta }}_{j})=s^{2}[(X^{T}X)^{-1}]_{jj}=s^{2}r_{1,1}^{-1}\\={}&s^{2}[X_{j}^{T}X_{j}-X_{j}^{T}X_{-j}(X_{-j}^{T}X_{-j})^{-1}X_{-j}^{T}X_{j}]^{-1}\\={}&s^{2}[X_{j}^{T}X_{j}-X_{j}^{T}X_{-j}(X_{-j}^{T}X_{-j})^{-1}(X_{-j}^{T}X_{-j})(X_{-j}^{T}X_{-j})^{-1}X_{-j}^{T}X_{j}]^{-1}\\={}&s^{2}[X_{j}^{T}X_{j}-{\hat {\beta }}_{*j}^{T}(X_{-j}^{T}X_{-j}){\hat {\beta }}_{*j}]^{-1}\\={}&s^{2}{\frac {1}{\mathrm {RSS} _{j}}}\\={}&{\frac {s^{2}}{(n-1){\widehat {\operatorname {var} }}(X_{j})}}\cdot {\frac {1}{1-R_{j}^{2}}}\end{aligned}}$

Here ${\hat {\beta }}_{*j}$ is the coefficient of regression of dependent variable $X_{j}$ over covariate $X_{-j}$ . $\mathrm {RSS} _{j}$ is the corresponding residual sum of squares.

## Calculation and analysis

We can calculate *k* different VIFs (one for each *X**i*) in three steps:

### Step one

First we run an ordinary least square regression that has *X**i* as a function of all the other explanatory variables in the first equation. If *i* = 1, for example, equation would be

$X_{1}=\alpha _{0}+\alpha _{2}X_{2}+\alpha _{3}X_{3}+\cdots +\alpha _{k}X_{k}+\varepsilon$

where $\alpha _{0}$ is a constant and $\varepsilon$ is the error term.

### Step two

Then, calculate the VIF factor for ${\hat {\alpha }}_{i}$ with the following formula :

$\mathrm {VIF} _{i}={\frac {1}{1-R_{i}^{2}}}$

where *R*2*i* is the coefficient of determination of the regression equation in step one, with $X_{i}$ on the left hand side, and all other predictor variables (all the other X variables) on the right hand side.

### Step three

Analyze the magnitude of multicollinearity by considering the size of the $\operatorname {VIF} ({\hat {\alpha }}_{i})$ . A rule of thumb is that if $\operatorname {VIF} ({\hat {\alpha }}_{i})>10$ then multicollinearity is high (a cutoff of 5 is also commonly used). However, there is no value of VIF greater than 1 in which the variance of the slopes of predictors isn't inflated. As a result, including two or more variables in a multiple regression that are not orthogonal (i.e. have correlation = 0), will alter each other's slope, SE of the slope, and P-value, because there is shared variance between the predictors that can't be uniquely attributed to any one of them.

Some software instead calculates the tolerance which is just the reciprocal of the VIF. The choice of which to use is a matter of personal preference.

## Interpretation

The square root of the variance inflation factor indicates how much larger the standard error increases compared to if that variable had 0 correlation to other predictor variables in the model.

**Example** If the variance inflation factor of a predictor variable were 5.27 (√5.27 = 2.3), this means that the standard error for the coefficient of that predictor variable is 2.3 times larger than if that predictor variable had 0 correlation with the other predictor variables.

## Implementation

- `vif` function in the car R package
- `ols_vif_tol` function in the olsrr R package
- `PROC REG` in SAS System
- `variance_inflation_factor` function in statsmodels Python package
- `estat vif` in Stata
- r.vif addon for GRASS GIS
- `vif` (non categorical) and `gvif` (categorical data) functions in StatsModels Julia programing language

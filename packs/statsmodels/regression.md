---
title: "Linear Regression"
source: https://www.statsmodels.org/stable/regression.html
domain: statsmodels
license: BSD-3-Clause
tags: statsmodels library, regression analysis, generalized linear model, analysis of variance
fetched: 2026-07-02
---

# Linear Regression

Linear models with independently and identically distributed errors, and for errors with heteroscedasticity or autocorrelation. This module allows estimation by ordinary least squares (OLS), weighted least squares (WLS), generalized least squares (GLS), and feasible generalized least squares with autocorrelated AR(p) errors.

See Module Reference for commands and arguments.

## Examples

```ipython
# Load modules and data
In [1]: import numpy as np

In [2]: import statsmodels.api as sm

In [3]: spector_data = sm.datasets.spector.load()

In [4]: spector_data.exog = sm.add_constant(spector_data.exog, prepend=False)

# Fit and summarize OLS model
In [5]: mod = sm.OLS(spector_data.endog, spector_data.exog)

In [6]: res = mod.fit()

In [7]: print(res.summary())
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  GRADE   R-squared:                       0.416
Model:                            OLS   Adj. R-squared:                  0.353
Method:                 Least Squares   F-statistic:                     6.646
Date:                Fri, 05 Dec 2025   Prob (F-statistic):            0.00157
Time:                        18:37:29   Log-Likelihood:                -12.978
No. Observations:                  32   AIC:                             33.96
Df Residuals:                      28   BIC:                             39.82
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
GPA            0.4639      0.162      2.864      0.008       0.132       0.796
TUCE           0.0105      0.019      0.539      0.594      -0.029       0.050
PSI            0.3786      0.139      2.720      0.011       0.093       0.664
const         -1.4980      0.524     -2.859      0.008      -2.571      -0.425
==============================================================================
Omnibus:                        0.176   Durbin-Watson:                   2.346
Prob(Omnibus):                  0.916   Jarque-Bera (JB):                0.167
Skew:                           0.141   Prob(JB):                        0.920
Kurtosis:                       2.786   Cond. No.                         176.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

Detailed examples can be found here:

- OLS
- WLS
- GLS
- Recursive LS
- Rolling LS

## Technical Documentation

The statistical model is assumed to be

> \(Y = X\beta + \epsilon\), where \(\epsilon\sim N\left(0,\Sigma\right).\)

Depending on the properties of \(\Sigma\), we have currently four classes available:

- GLS : generalized least squares for arbitrary covariance \(\Sigma\)
- OLS : ordinary least squares for i.i.d. errors \(\Sigma=\textbf{I}\)
- WLS : weighted least squares for heteroskedastic errors \(\text{diag}\left (\Sigma\right)\)
- GLSAR : feasible generalized least squares with autocorrelated AR(p) errors \(\Sigma=\Sigma\left(\rho\right)\)

All regression models define the same methods and follow the same structure, and can be used in a similar fashion. Some of them contain additional model specific methods and attributes.

GLS is the superclass of the other regression classes except for RecursiveLS, RollingWLS and RollingOLS.

### Attributes

The following is more verbose description of the attributes which is mostly common to all regression classes

**pinv_wexogarray**

The *p* x *n* Moore-Penrose pseudoinverse of the whitened design matrix. It is approximately equal to \(\left(X^{T}\Sigma^{-1}X\right)^{-1}X^{T}\Psi\), where \(\Psi\) is defined such that \(\Psi\Psi^{T}=\Sigma^{-1}\).

**cholsimgainvarray**

The *n* x *n* upper triangular matrix \(\Psi^{T}\) that satisfies \(\Psi\Psi^{T}=\Sigma^{-1}\).

**df_modelfloat**

The model degrees of freedom. This is equal to *p* - 1, where *p* is the number of regressors. Note that the intercept is not counted as using a degree of freedom here.

**df_residfloat**

The residual degrees of freedom. This is equal *n - p* where *n* is the number of observations and *p* is the number of parameters. Note that the intercept is counted as using a degree of freedom here.

**llffloat**

The value of the likelihood function of the fitted model.

**nobsfloat**

The number of observations *n*

**normalized_cov_paramsarray**

A *p* x *p* array equal to \((X^{T}\Sigma^{-1}X)^{-1}\).

**sigmaarray**

The *n* x *n* covariance matrix of the error terms: \(\epsilon\sim N\left(0,\Sigma\right)\).

**wexogarray**

The whitened design matrix \(\Psi^{T}X\).

**wendogarray**

The whitened response variable \(\Psi^{T}Y\).

## Module Reference

### Model Classes

| `OLS`(endog[, exog, missing, hasconst]) | Ordinary Least Squares |
|---|---|
| `GLS`(endog, exog[, sigma, missing, hasconst]) | Generalized Least Squares |
| `WLS`(endog, exog[, weights, missing, hasconst]) | Weighted Least Squares |
| `GLSAR`(endog[, exog, rho, missing, hasconst]) | Generalized Least Squares with AR covariance structure |
| `yule_walker`(x[, order, method, df, inv, demean]) | Estimate AR(p) parameters from a sequence using the Yule-Walker equations. |
| `burg`(endog[, order, demean]) | Compute Burg's AP(p) parameter estimator. |

| `QuantReg`(endog, exog, **kwargs) | Quantile Regression |
|---|---|

| `RecursiveLS`(endog, exog[, constraints]) | Recursive least squares |
|---|---|

| `RollingWLS`(endog, exog[, window, weights, ...]) | Rolling Weighted Least Squares |
|---|---|
| `RollingOLS`(endog, exog[, window, min_nobs, ...]) | Rolling Ordinary Least Squares |

| `GaussianCovariance`() | An implementation of ProcessCovariance using the Gaussian kernel. |
|---|---|
| `ProcessMLE`(endog, exog, exog_scale, ...[, cov]) | Fit a Gaussian mean/variance regression model. |

| `SlicedInverseReg`(endog, exog, **kwargs) | Sliced Inverse Regression (SIR) |
|---|---|
| `PrincipalHessianDirections`(endog, exog, **kwargs) | Principal Hessian Directions (PHD) |
| `SlicedAverageVarianceEstimation`(endog, exog, ...) | Sliced Average Variance Estimation (SAVE) |

### Results Classes

Fitting a linear regression model returns a results class. OLS has a specific results class with some additional methods compared to the results class of the other linear models.

| `RegressionResults`(model, params[, ...]) | This class summarizes the fit of a linear regression model. |
|---|---|
| `OLSResults`(model, params[, ...]) | Results class for for an OLS model. |
| `PredictionResults`(predicted_mean, ...[, df, ...]) | Results class for predictions. |

| `RegularizedResults`(model, params) | Results for models estimated using regularization |
|---|---|

| `QuantRegResults`(model, params[, ...]) | Results instance for the QuantReg model |
|---|---|

| `RecursiveLSResults`(model, params, filter_results) | Class to hold results from fitting a recursive least squares model. |
|---|---|

| `RollingRegressionResults`(model, store, ...) | Results from rolling regressions |
|---|---|

| `ProcessMLEResults`(model, mlefit) | Results class for Gaussian process regression models. |
|---|---|

| `DimReductionResults`(model, params, eigs) | Results class for a dimension reduction regression. |
|---|---|

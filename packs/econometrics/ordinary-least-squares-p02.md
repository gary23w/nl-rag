---
title: "Ordinary least squares (part 2/2)"
source: https://en.wikipedia.org/wiki/Ordinary_least_squares
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
part: 2/2
---

## Example with real data

The following data set gives average heights and weights for American women aged 30–39 (source: *The World Almanac and Book of Facts, 1975*).

| Height (m) | 1.47 | 1.50 | 1.52 | 1.55 | 1.57 |   |
|---|---|---|---|---|---|---|
| Weight (kg) | 52.21 | 53.12 | 54.48 | 55.84 | 57.20 |   |
| Height (m) | 1.60 | 1.63 | 1.65 | 1.68 | 1.70 |   |
| Weight (kg) | 58.57 | 59.93 | 61.29 | 63.11 | 64.47 |   |
| Height (m) | 1.73 | 1.75 | 1.78 | 1.80 | 1.83 |   |
| Weight (kg) | 66.28 | 68.10 | 69.92 | 72.19 | 74.46 |   |

When only one dependent variable is being modeled, a scatterplot will suggest the form and strength of the relationship between the dependent variable and regressors. It might also reveal outliers, heteroscedasticity, and other aspects of the data that may complicate the interpretation of a fitted regression model. The scatterplot suggests that the relationship is strong and can be approximated as a quadratic function. OLS can handle non-linear relationships by introducing the regressor *HEIGHT*2. The regression model then becomes a multiple linear model:

$w_{i}=\beta _{1}+\beta _{2}h_{i}+\beta _{3}h_{i}^{2}+\varepsilon _{i}.$

The output from most popular statistical packages will look similar to this:

| Method | Least squares |   |   |   |
|---|---|---|---|---|
| Dependent variable | WEIGHT |   |   |   |
| Observations | 15 |   |   |   |
|   |   |   |   |   |
| Parameter | Value | Std error | t-statistic | p-value |
|   |   |   |   |   |
| $\beta _{1}$ | 128.8128 | 16.3083 | 7.8986 | 0.0000 |
| $\beta _{2}$ | −143.1620 | 19.8332 | −7.2183 | 0.0000 |
| $\beta _{3}$ | 61.9603 | 6.0084 | 10.3122 | 0.0000 |
|   |   |   |   |   |
| R2 | 0.9989 | S.E. of regression | 0.2516 |   |
| Adjusted R2 | 0.9987 | Model sum-of-sq. | 692.61 |   |
| Log-likelihood | 1.0890 | Residual sum-of-sq. | 0.7595 |   |
| Durbin–Watson stat. | 2.1013 | Total sum-of-sq. | 693.37 |   |
| Akaike criterion | 0.2548 | F-statistic | 5471.2 |   |
| Schwarz criterion | 0.3964 | p-value (F-stat) | 0.0000 |   |

In this table:

- The *Value* column gives the least squares estimates of parameters *βj*
- The *Std error* column shows standard errors of each coefficient estimate: ${\hat {\sigma }}_{j}=\left({\hat {\sigma }}^{2}\left[Q_{xx}^{-1}\right]_{jj}\right)^{\frac {1}{2}}$
- The *t-statistic* and *p-value* columns are testing whether any of the coefficients might be equal to zero. The *t*-statistic is calculated simply as $t={\hat {\beta }}_{j}/{\hat {\sigma }}_{j}$ . If the errors ε follow a normal distribution, *t* follows a Student-t distribution. Under weaker conditions, *t* is asymptotically normal. Large values of *t* indicate that the null hypothesis can be rejected and that the corresponding coefficient is not zero. The second column, *p*-value, expresses the results of the hypothesis test as a significance level. Conventionally, *p*-values smaller than 0.05 are taken as evidence that the population coefficient is nonzero.
- *R-squared* is the coefficient of determination indicating goodness-of-fit of the regression. This statistic will be equal to one if fit is perfect, and to zero when regressors *X* have no explanatory power whatsoever. This is a biased estimate of the population *R-squared*, and will never decrease if additional regressors are added, even if they are irrelevant.
- *Adjusted R-squared* is a slightly modified version of $R^{2}$ , designed to penalize for the excess number of regressors which do not add to the explanatory power of the regression. This statistic is always smaller than $R^{2}$ , can decrease as new regressors are added, and even be negative for poorly fitting models:

${\overline {R}}^{2}=1-{\frac {n-1}{n-p}}(1-R^{2})$

- *Log-likelihood* is calculated under the assumption that errors follow normal distribution. Even though the assumption is not very reasonable, this statistic may still find its use in conducting LR tests.
- *Durbin–Watson statistic* tests whether there is any evidence of serial correlation between the residuals. As a rule of thumb, the value smaller than 2 will be an evidence of positive correlation.
- *Akaike information criterion* and *Schwarz criterion* are both used for model selection. Generally when comparing two alternative models, smaller values of one of these criteria will indicate a better model.
- *Standard error of regression* is an estimate of *σ*, standard error of the error term.
- *Total sum of squares*, *model sum of squared*, and *residual sum of squares* tell us how much of the initial variation in the sample were explained by the regression.
- *F-statistic* tries to test the hypothesis that all coefficients (except the intercept) are equal to zero. This statistic has *F*(*p–1*,*n–p*) distribution under the null hypothesis and normality assumption, and its *p-value* indicates probability that the hypothesis is indeed true. Note that when errors are not normal this statistic becomes invalid, and other tests such as Wald test or LR test should be used.

Ordinary least squares analysis often includes the use of diagnostic plots designed to detect departures of the data from the assumed form of the model. These are some of the common diagnostic plots:

- Residuals against the explanatory variables in the model. A non-linear relation between these variables suggests that the linearity of the conditional mean function may not hold. Different levels of variability in the residuals for different levels of the explanatory variables suggests possible heteroscedasticity.
- Residuals against explanatory variables not in the model. Any relation of the residuals to these variables would suggest considering these variables for inclusion in the model.
- Residuals against the fitted values, ${\hat {y}}$ .
- Residuals against the preceding residual. This plot may identify serial correlations in the residuals.

An important consideration when carrying out statistical inference using regression models is how the data were sampled. In this example, the data are averages rather than measurements on individual women. The fit of the model is very good, but this does not imply that the weight of an individual woman can be predicted with high accuracy based only on her height.

### Sensitivity to rounding

This example also demonstrates that coefficients determined by these calculations are sensitive to how the data is prepared. The heights were originally given rounded to the nearest inch and have been converted and rounded to the nearest centimetre. Since the conversion factor is one inch to 2.54 cm this is *not* an exact conversion. The original inches can be recovered by Round(x/0.0254) and then re-converted to metric without rounding. If this is done the results become:

|   | Const | Height | Height2 |
|---|---|---|---|
| Converted to metric with rounding. | 128.8128 | −143.162 | 61.96033 |
| Converted to metric without rounding. | 119.0205 | −131.5076 | 58.5046 |

Using either of these equations to predict the weight of a 5' 6" (1.6764 m) woman gives similar values: 62.94 kg with rounding vs. 62.98 kg without rounding. Thus a seemingly small variation in the data has a real effect on the coefficients but a small effect on the results of the equation.

While this may look innocuous in the middle of the data range it could become significant at the extremes or in the case where the fitted model is used to project outside the data range (extrapolation).

This highlights a common error: this example is an abuse of OLS which inherently requires that the errors in the independent variable (in this case height) are zero or at least negligible. The initial rounding to nearest inch plus any actual measurement errors constitute a finite and non-negligible error. As a result, the fitted parameters are not the best estimates they are presumed to be. Though not totally spurious the error in the estimation will depend upon relative size of the *x* and *y* errors.


## Another example with less real data

### Problem statement

We can use the least square mechanism to figure out the equation of a two body orbit in polar base co-ordinates. The equation typically used is $r(\theta )={\frac {p}{1-e\cos(\theta )}}$ where $r(\theta )$ is the radius of how far the object is from one of the bodies. In the equation the parameters p and e are used to determine the path of the orbit. We have measured the following data.

| $\theta$ (in degrees) | 43 | 45 | 52 | 93 | 108 | 116 |
|---|---|---|---|---|---|---|
| $r(\theta )$ | 4.7126 | 4.5542 | 4.0419 | 2.2187 | 1.8910 | 1.7599 |

We need to find the least-squares approximation of e and p for the given data.

### Solution

First we need to represent e and p in a linear form. So we are going to rewrite the equation $r(\theta )$ as ${\frac {1}{r(\theta )}}={\frac {1}{p}}-{\frac {e}{p}}\cos(\theta )$ .

Furthermore, one could fit for apsides by expanding $\cos(\theta )$ with an extra parameter as $\cos(\theta -\theta _{0})=\cos(\theta )\cos(\theta _{0})+\sin(\theta )\sin(\theta _{0})$ , which is linear in both $\cos(\theta )$ and in the extra basis function $\sin(\theta )$ .

We use the original two-parameter form to represent our observational data as:

$A^{T}A{\binom {x}{y}}=A^{T}b,$

where:

$x=1/p\,$ ; $y=e/p\,$ ; A contains the coefficients of $1/p$ in the first column, which are all 1, and the coefficients of $e/p$ in the second column, given by $\cos(\theta )\,$ ; and $b=1/r(\theta )$ , such that:

$A={\begin{bmatrix}1&-0.731354\\1&-0.707107\\1&-0.615661\\1&\ 0.052336\\1&0.309017\\1&0.438371\end{bmatrix}},\quad b={\begin{bmatrix}0.21220\\0.21958\\0.24741\\0.45071\\0.52883\\0.56820\end{bmatrix}}.$

On solving we get ${\binom {x}{y}}={\binom {0.43478}{0.30435}}\,$ ,

so $p={\frac {1}{x}}=2.3000$ and $e=p\cdot y=0.70001$

---
title: "Simple linear regression"
source: https://en.wikipedia.org/wiki/Simple_linear_regression
domain: linear-regression
license: CC-BY-SA-4.0
tags: linear regression, ordinary least squares, regression coefficients, least squares
fetched: 2026-07-02
---

# Simple linear regression

In statistics, **simple linear regression** (**SLR**) is a linear regression model with a single explanatory variable. That is, it concerns two-dimensional sample points with one independent variable and one dependent variable (conventionally, the *x* and *y* coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variable. The adjective *simple* refers to the fact that the outcome variable is related to a single predictor.

It is common to make the additional stipulation that the ordinary least squares (OLS) method should be used: the accuracy of each predicted value is measured by its squared *residual* (vertical distance between the point of the data set and the fitted line), and the goal is to make the sum of these squared deviations as small as possible. In this case, the slope of the fitted line is equal to the correlation between y and x corrected by the ratio of standard deviations of these variables. The intercept of the fitted line is such that the line passes through the center of mass (*x*, *y*) of the data points.

## Formulation and computation

Consider the model function $y=\alpha +\beta x,$ which describes a line with slope β and y-intercept α. In general, such a relationship may not hold exactly for the largely unobserved population of values of the independent and dependent variables; we call the unobserved deviations from the above equation the errors. Suppose we observe n data pairs and call them {(*x**i*, *y**i*), *i* = 1, ..., *n*}. We can describe the underlying relationship between *y**i* and *x**i* involving this error term *ε**i* by

$y_{i}=\alpha +\beta x_{i}+\varepsilon _{i}.$

This relationship between the true (but unobserved) underlying parameters α and β and the data points is called a linear regression model.

The goal is to find estimated values ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ for the parameters α and β which would provide the "best" fit in some sense for the data points. As mentioned in the introduction, in this article the "best" fit will be understood as in the least-squares approach: a line that minimizes the sum of squared residuals (see also Errors and residuals) ${\widehat {\varepsilon }}_{i}$ (differences between actual and predicted values of the dependent variable *y*), each of which is given by, for any candidate parameter values $\alpha$ and $\beta$ ,

${\widehat {\varepsilon }}_{i}=y_{i}-\alpha -\beta x_{i}.$

In other words, ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ solve the following minimization problem:

$({\hat {\alpha }},\,{\hat {\beta }})=\operatorname {argmin} \left(Q(\alpha ,\beta )\right),$ where the objective function Q is: $Q(\alpha ,\beta )=\sum _{i=1}^{n}{\widehat {\varepsilon }}_{i}^{\,2}=\sum _{i=1}^{n}(y_{i}-\alpha -\beta x_{i})^{2}\ .$

By expanding to get a quadratic expression in $\alpha$ and $\beta ,$ we can derive minimizing values of the function arguments, denoted ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ :

${\begin{aligned}{\widehat {\alpha }}&={\bar {y}}-{\widehat {\beta }}\,{\bar {x}},\\[5pt]{\widehat {\beta }}&={\frac {\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)\left(y_{i}-{\bar {y}}\right)}{\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)^{2}}}={\frac {\sum _{i=1}^{n}\Delta x_{i}\Delta y_{i}}{\sum _{i=1}^{n}\Delta x_{i}^{2}}}\end{aligned}}$

Here we have introduced

- ${\bar {x}}$ and ${\bar {y}}$ as the average of the *x**i* and *y**i*, respectively
- $\Delta x_{i}$ and $\Delta y_{i}$ as the deviations in *x**i* and *y**i* with respect to their respective means.

### Expanded formulas

The above equations are efficient to use if the mean of the x and y variables ( ${\bar {x}}{\text{ and }}{\bar {y}}$ ) are known. If the means are not known at the time of calculation, it may be more efficient to use the expanded version of the ${\widehat {\alpha }}{\text{ and }}{\widehat {\beta }}$ equations. These expanded equations may be derived from the more general polynomial regression equations by defining the regression polynomial to be of order 1, as follows.

${\begin{bmatrix}n&\sum _{i=1}^{n}x_{i}\\[1ex]\sum _{i=1}^{n}x_{i}&\sum _{i=1}^{n}x_{i}^{2}\end{bmatrix}}{\begin{bmatrix}{\widehat {\alpha }}\\[1ex]{\widehat {\beta }}\end{bmatrix}}={\begin{bmatrix}\sum _{i=1}^{n}y_{i}\\[1ex]\sum _{i=1}^{n}y_{i}x_{i}\end{bmatrix}}$

The above system of linear equations may be solved directly, or stand-alone equations for ${\widehat {\alpha }}{\text{ and }}{\widehat {\beta }}$ may be derived by expanding the matrix equations above. The resultant equations are algebraically equivalent to the ones shown in the prior paragraph, and are shown below without proof.

${\begin{aligned}{\widehat {\alpha }}&={\frac {\sum \limits _{i=1}^{n}y_{i}\sum \limits _{i=1}^{n}x_{i}^{2}-\sum \limits _{i=1}^{n}x_{i}\sum \limits _{i=1}^{n}x_{i}y_{i}}{n\sum \limits _{i=1}^{n}x_{i}^{2}-\left(\sum \limits _{i=1}^{n}x_{i}\right)^{2}}}\\[2ex]{\widehat {\beta }}&={\frac {n\sum \limits _{i=1}^{n}x_{i}y_{i}-\sum \limits _{i=1}^{n}x_{i}\sum \limits _{i=1}^{n}y_{i}}{n\sum \limits _{i=1}^{n}x_{i}^{2}-\left(\sum \limits _{i=1}^{n}x_{i}\right)^{2}}}\end{aligned}}$

## Interpretation

### Relationship with the sample covariance matrix

The solution can be reformulated using elements of the covariance matrix: ${\widehat {\beta }}={\frac {s_{x,y}}{s_{x}^{2}}}=r_{xy}{\frac {s_{y}}{s_{x}}}$

where

- *r**xy* is the sample correlation coefficient between x and y
- *s**x* and *sy* are the uncorrected sample standard deviations of x and y
- $s_{x}^{2}$ and $s_{x,y}$ are the sample variance and sample covariance, respectively

Substituting the above expressions for ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ into the original solution yields

${\frac {y-{\bar {y}}}{s_{y}}}=r_{xy}{\frac {x-{\bar {x}}}{s_{x}}}.$

This shows that *r**xy* is the slope of the regression line of the standardized data points (and that this line passes through the origin). Since $-1\leq r_{xy}\leq 1$ then we get that if x is some measurement and y is a followup measurement from the same item, then we expect that y (on average) will be closer to the mean measurement than it was to the original value of x. This phenomenon is known as regressions toward the mean.

Generalizing the ${\bar {x}}$ notation, we can write a horizontal bar over an expression to indicate the average value of that expression over the set of samples. For example:

${\overline {xy}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}y_{i}.$

This notation allows us a concise formula for *r**xy*:

$r_{xy}={\frac {{\overline {xy}}-{\bar {x}}{\bar {y}}}{\sqrt {\left({\overline {x^{2}}}-{\bar {x}}^{2}\right)\left({\overline {y^{2}}}-{\bar {y}}^{2}\right)}}}.$

The coefficient of determination ("R squared") is equal to $r_{xy}^{2}$ when the model is linear with a single independent variable. See sample correlation coefficient for additional details.

### Interpretation about the slope

By multiplying all members of the summation in the numerator by : ${\frac {x_{i}-{\bar {x}}}{x_{i}-{\bar {x}}}}=1$ (thereby not changing it):

${\begin{aligned}{\widehat {\beta }}&={\frac {\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)\left(y_{i}-{\bar {y}}\right)}{\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)^{2}}}\\[1ex]&={\frac {\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)^{2}{\frac {y_{i}-{\bar {y}}}{x_{i}-{\bar {x}}}}}{\sum _{i=1}^{n}\left(x_{i}-{\bar {x}}\right)^{2}}}\\[1ex]&=\sum _{i=1}^{n}{\frac {\left(x_{i}-{\bar {x}}\right)^{2}}{\sum _{j=1}^{n}\left(x_{j}-{\bar {x}}\right)^{2}}}{\frac {y_{i}-{\bar {y}}}{x_{i}-{\bar {x}}}}\\[6pt]\end{aligned}}$

We can see that the slope (tangent of angle) of the regression line is the weighted average of ${\frac {y_{i}-{\bar {y}}}{x_{i}-{\bar {x}}}}$ that is the slope (tangent of angle) of the line that connects the i-th point to the average of all points, weighted by $(x_{i}-{\bar {x}})^{2}$ because the further the point is the more "important" it is, since small errors in its position will affect the slope connecting it to the center point more.

### Interpretation about the intercept

The parameter ${\widehat {\alpha }}$ is the intercept of the linear function ${\begin{aligned}{y}&={\widehat {\alpha }}\ +{\widehat {\beta }}\,{x},\\[5pt]\end{aligned}}$ . Therefore, the ${y}$ -intercept of the function found with simple linear regression is

$y_{\rm {intercept}}={\widehat {\alpha }}={\bar {y}}-{\widehat {\beta }}\,{\bar {x}}$ .

Because ${\widehat {\beta }}$ is the slope of the linear function, ${\widehat {\beta }}=\tan(\theta )$ . Therefore, the angle $\theta$ the graph of the function makes with the ${x}$ axis is equal to

$\theta =\arctan({\widehat {\beta }})$ .

### Interpretation about the correlation

In the above formulation, notice that each $x_{i}$ is a constant ("known upfront") value, while the $y_{i}$ are random variables that depend on the linear function of $x_{i}$ and the random term $\varepsilon _{i}$ . This assumption is used when deriving the standard error of the slope and showing that it is unbiased.

In this framing, when $x_{i}$ is not actually a random variable, what type of parameter does the empirical correlation $r_{xy}$ estimate? The issue is that for each value i we'll have: $E(x_{i})=x_{i}$ and $Var(x_{i})=0$ . A possible interpretation of $r_{xy}$ is to imagine that $x_{i}$ defines a random variable drawn from the empirical distribution of the x values in our sample. For example, if x had 10 values from the natural numbers: [1,2,3...,10], then we can imagine x to be a Discrete uniform distribution. Under this interpretation all $x_{i}$ have the same expectation and some positive variance. With this interpretation we can think of $r_{xy}$ as the estimator of the Pearson's correlation between the random variable y and the random variable x (as we just defined it).

## Numerical properties

1. The regression line goes through the *center of mass* point, $({\bar {x}},\,{\bar {y}})$ , if the model includes an intercept term (i.e., not forced through the origin).
2. The sum of the residuals is zero if the model includes an intercept term: $\sum _{i=1}^{n}{\widehat {\varepsilon }}_{i}=0.$
3. The residuals and x values are uncorrelated (whether or not there is an intercept term in the model), meaning: $\sum _{i=1}^{n}x_{i}{\widehat {\varepsilon }}_{i}\;=\;0$
4. The relationship between $\rho _{xy}$ (the correlation coefficient for the population) and the population variances of y ( $\sigma _{y}^{2}$ ) and the error term of $\varepsilon$ ( $\sigma _{\varepsilon }^{2}$ ) is: $\sigma _{\varepsilon }^{2}=(1-\rho _{xy}^{2})\sigma _{y}^{2}$ For extreme values of $\rho _{xy}$ this is self evident. Since when $\rho _{xy}=0$ then $\sigma _{\varepsilon }^{2}=\sigma _{y}^{2}$ . And when $\rho _{xy}=1$ then $\sigma _{\varepsilon }^{2}=0$ .

## Statistical properties

Description of the statistical properties of estimators from the simple linear regression estimates requires the use of a statistical model. The following is based on assuming the validity of a model under which the estimates are optimal. It is also possible to evaluate the properties under other assumptions, such as inhomogeneity, but this is discussed elsewhere.

### Unbiasedness

The estimators ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ are unbiased.

To formalize this assertion we must define a framework in which these estimators are random variables. We consider the residuals *ε*i as random variables drawn independently from some distribution with mean zero. In other words, for each value of x, the corresponding value of y is generated as a mean response *α* + *βx* plus an additional random variable ε called the *error term*, equal to zero on average. Under such interpretation, the least-squares estimators ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ will themselves be random variables whose means will equal the "true values" α and β. This is the definition of an unbiased estimator.

### Variance of the mean response

Since the data in this context is defined to be (*x*, *y*) pairs for every observation, the *mean response* at a given value of *x*, say *xd*, is an estimate of the mean of the *y* values in the population at the *x* value of *xd*, that is ${\hat {E}}(y\mid x_{d})\equiv {\hat {y}}_{d}\!$ . The variance of the mean response is given by:

$\operatorname {Var} \left({\hat {\alpha }}+{\hat {\beta }}x_{d}\right)=\operatorname {Var} \left({\hat {\alpha }}\right)+\left(\operatorname {Var} {\hat {\beta }}\right)x_{d}^{2}+2x_{d}\operatorname {Cov} \left({\hat {\alpha }},{\hat {\beta }}\right).$

This expression can be simplified to

$\operatorname {Var} \left({\hat {\alpha }}+{\hat {\beta }}x_{d}\right)=\sigma ^{2}\left({\frac {1}{m}}+{\frac {\left(x_{d}-{\bar {x}}\right)^{2}}{\sum (x_{i}-{\bar {x}})^{2}}}\right),$

where *m* is the number of data points.

To demonstrate this simplification, one can make use of the identity

$\sum _{i}(x_{i}-{\bar {x}})^{2}=\sum _{i}x_{i}^{2}-{\frac {1}{m}}\left(\sum _{i}x_{i}\right)^{2}.$

### Variance of the predicted response

The *predicted response* distribution is the predicted distribution of the residuals at the given point *xd*. So the variance is given by

${\begin{aligned}\operatorname {Var} \left(y_{d}-\left[{\hat {\alpha }}+{\hat {\beta }}x_{d}\right]\right)&=\operatorname {Var} (y_{d})+\operatorname {Var} \left({\hat {\alpha }}+{\hat {\beta }}x_{d}\right)-2\operatorname {Cov} \left(y_{d},\left[{\hat {\alpha }}+{\hat {\beta }}x_{d}\right]\right)\\&=\operatorname {Var} (y_{d})+\operatorname {Var} \left({\hat {\alpha }}+{\hat {\beta }}x_{d}\right).\end{aligned}}$

The second line follows from the fact that $\operatorname {Cov} \left(y_{d},\left[{\hat {\alpha }}+{\hat {\beta }}x_{d}\right]\right)$ is zero because the new prediction point is independent of the data used to fit the model. Additionally, the term $\operatorname {Var} \left({\hat {\alpha }}+{\hat {\beta }}x_{d}\right)$ was calculated earlier for the mean response.

Since $\operatorname {Var} (y_{d})=\sigma ^{2}$ (a fixed but unknown parameter that can be estimated), the variance of the predicted response is given by

${\begin{aligned}\operatorname {Var} \left(y_{d}-\left[{\hat {\alpha }}+{\hat {\beta }}x_{d}\right]\right)&=\sigma ^{2}+\sigma ^{2}\left({\frac {1}{m}}+{\frac {\left(x_{d}-{\bar {x}}\right)^{2}}{\sum (x_{i}-{\bar {x}})^{2}}}\right)\\[4pt]&=\sigma ^{2}\left(1+{\frac {1}{m}}+{\frac {(x_{d}-{\bar {x}})^{2}}{\sum (x_{i}-{\bar {x}})^{2}}}\right).\end{aligned}}$

### Confidence intervals

The formulas given in the previous section allow one to calculate the *point estimates* of α and β — that is, the coefficients of the regression line for the given set of data. However, those formulas do not tell us how precise the estimates are, i.e., how much the estimators ${\widehat {\alpha }}$ and ${\widehat {\beta }}$ vary from sample to sample for the specified sample size. Confidence intervals were devised to give a plausible set of values to the estimates one might have if one repeated the experiment a very large number of times.

The standard method of constructing confidence intervals for linear regression coefficients relies on the normality assumption, which is justified if either:

1. the errors in the regression are normally distributed (the so-called *classic regression* assumption), or
2. the number of observations n is sufficiently large, in which case the estimator is approximately normally distributed.

The latter case is justified by the central limit theorem.

#### Normality assumption

Under the first assumption above, that of the normality of the error terms, the estimator of the slope coefficient will itself be normally distributed with mean β and variance ${\textstyle \sigma ^{2}\left/\sum _{i}(x_{i}-{\bar {x}})^{2}\right.,}$ where *σ*2 is the variance of the error terms (see Proofs involving ordinary least squares). At the same time the sum of squared residuals Q is distributed proportionally to *χ*2 with *n* − 2 degrees of freedom, and independently from ${\widehat {\beta }}$ . This allows us to construct a t-value

$t={\frac {{\widehat {\beta }}-\beta }{s_{\widehat {\beta }}}}\ \sim \ t_{n-2},$

where

$s_{\widehat {\beta }}={\sqrt {\frac {{\frac {1}{n-2}}\sum _{i=1}^{n}{\widehat {\varepsilon }}_{i}^{\,2}}{\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}}}}$

is the unbiased *standard error* estimator of the estimator ${\widehat {\beta }}$ .

This t-value has a Student's t-distribution with *n* − 2 degrees of freedom. Using it we can construct a confidence interval for β:

$\beta \in \left[{\widehat {\beta }}-s_{\widehat {\beta }}t_{n-2}^{*},\ {\widehat {\beta }}+s_{\widehat {\beta }}t_{n-2}^{*}\right],$

at confidence level (1 − *γ*), where $t_{n-2}^{*}$ is the $\scriptstyle \left(1\;-\;{\frac {\gamma }{2}}\right){\text{-th}}$ quantile of the *t**n*−2 distribution. For example, if *γ* = 0.05 then the confidence level is 95%.

Similarly, the confidence interval for the intercept coefficient α is given by

$\alpha \in \left[{\widehat {\alpha }}-s_{\widehat {\alpha }}t_{n-2}^{*},\ {\widehat {\alpha }}+s_{\widehat {\alpha }}t_{n-2}^{*}\right],$

at confidence level (1 − *γ*), where

$s_{\widehat {\alpha }}=s_{\widehat {\beta }}{\sqrt {{\frac {1}{n}}\sum _{i=1}^{n}x_{i}^{2}}}={\sqrt {{\frac {1}{n(n-2)}}\left(\sum _{i=1}^{n}{\widehat {\varepsilon }}_{i}^{\,2}\right){\frac {\sum _{i=1}^{n}x_{i}^{2}}{\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}}}}}$

The confidence intervals for α and β give us the general idea where these regression coefficients are most likely to be. For example, in the Okun's law regression shown here the point estimates are

${\widehat {\alpha }}=0.859,\qquad {\widehat {\beta }}=-1.817.$

The 95% confidence intervals for these estimates are

$\alpha \in \left[\,0.76,0.96\right],\qquad \beta \in \left[-2.06,-1.58\,\right].$

In order to represent this information graphically, in the form of the confidence bands around the regression line, one has to proceed carefully and account for the joint distribution of the estimators. It can be shown that at confidence level (1 − *γ*) the confidence band has hyperbolic form given by the equation

$(\alpha +\beta \xi )\in \left[\,{\widehat {\alpha }}+{\widehat {\beta }}\xi \pm t_{n-2}^{*}{\sqrt {\left({\frac {1}{n-2}}\sum {\widehat {\varepsilon }}_{i}^{\,2}\right)\cdot \left({\frac {1}{n}}+{\frac {(\xi -{\bar {x}})^{2}}{\sum (x_{i}-{\bar {x}})^{2}}}\right)}}\,\right].$

When the model assumed the intercept is fixed and equal to 0 ( $\alpha =0$ ), the standard error of the slope turns into:

$s_{\widehat {\beta }}={\sqrt {{\frac {1}{n-1}}{\frac {\sum _{i=1}^{n}{\widehat {\varepsilon }}_{i}^{\,2}}{\sum _{i=1}^{n}x_{i}^{2}}}}}$

With: ${\hat {\varepsilon }}_{i}=y_{i}-{\hat {y}}_{i}$

#### Asymptotic assumption

The alternative second assumption states that when the number of points in the dataset is "large enough", the law of large numbers and the central limit theorem become applicable, and then the distribution of the estimators is approximately normal. Under this assumption all formulas derived in the previous section remain valid, with the only exception that the quantile *t***n*−2 of Student's *t* distribution is replaced with the quantile *q** of the standard normal distribution. Occasionally the fraction ⁠1/*n*−2⁠ is replaced with ⁠1/*n*⁠. When n is large such a change does not alter the results appreciably.

## Numerical example

This data set gives average masses for women as a function of their height in a sample of American women of age 30–39. Although the OLS article argues that it would be more appropriate to run a quadratic regression for this data, the simple linear regression model is applied here instead.

Height (m),

x

i

1.47

1.50

1.52

1.55

1.57

1.60

1.63

1.65

1.68

1.70

1.73

1.75

1.78

1.80

1.83

Mass (kg),

y

i

52.21

53.12

54.48

55.84

57.20

58.57

59.93

61.29

63.11

64.47

66.28

68.10

69.92

72.19

74.46

| i | $x_{i}$ | $y_{i}$ | $x_{i}^{2}$ | $x_{i}y_{i}$ | $y_{i}^{2}$ |
|---|---|---|---|---|---|
| 1 | 1.47 | 52.21 | 2.1609 | 76.7487 | 2725.8841 |
| 2 | 1.50 | 53.12 | 2.2500 | 79.6800 | 2821.7344 |
| 3 | 1.52 | 54.48 | 2.3104 | 82.8096 | 2968.0704 |
| 4 | 1.55 | 55.84 | 2.4025 | 86.5520 | 3118.1056 |
| 5 | 1.57 | 57.20 | 2.4649 | 89.8040 | 3271.8400 |
| 6 | 1.60 | 58.57 | 2.5600 | 93.7120 | 3430.4449 |
| 7 | 1.63 | 59.93 | 2.6569 | 97.6859 | 3591.6049 |
| 8 | 1.65 | 61.29 | 2.7225 | 101.1285 | 3756.4641 |
| 9 | 1.68 | 63.11 | 2.8224 | 106.0248 | 3982.8721 |
| 10 | 1.70 | 64.47 | 2.8900 | 109.5990 | 4156.3809 |
| 11 | 1.73 | 66.28 | 2.9929 | 114.6644 | 4393.0384 |
| 12 | 1.75 | 68.10 | 3.0625 | 119.1750 | 4637.6100 |
| 13 | 1.78 | 69.92 | 3.1684 | 124.4576 | 4888.8064 |
| 14 | 1.80 | 72.19 | 3.2400 | 129.9420 | 5211.3961 |
| 15 | 1.83 | 74.46 | 3.3489 | 136.2618 | 5544.2916 |
| $\Sigma$ | 24.76 | 931.17 | 41.0532 | 1548.2453 | 58498.5439 |

There are *n* = 15 points in this data set. Hand calculations would be started by finding the following five sums:

${\begin{aligned}S_{x}&=\sum _{i}x_{i}\,=24.76,&\qquad S_{y}&=\sum _{i}y_{i}\,=931.17,\\[5pt]S_{xx}&=\sum _{i}x_{i}^{2}=41.0532,&\;\;\,S_{yy}&=\sum _{i}y_{i}^{2}=58498.5439,\\[5pt]S_{xy}&=\sum _{i}x_{i}y_{i}=1548.2453&\end{aligned}}$

These quantities would be used to calculate the estimates of the regression coefficients, and their standard errors.

${\begin{aligned}{\widehat {\beta }}&={\frac {nS_{xy}-S_{x}S_{y}}{nS_{xx}-S_{x}^{2}}}=61.272\\[8pt]{\widehat {\alpha }}&={\frac {1}{n}}S_{y}-{\widehat {\beta }}{\frac {1}{n}}S_{x}=-39.062\\[8pt]s_{\varepsilon }^{2}&={\frac {1}{n(n-2)}}\left[nS_{yy}-S_{y}^{2}-{\widehat {\beta }}^{2}(nS_{xx}-S_{x}^{2})\right]=0.5762\\[8pt]s_{\widehat {\beta }}^{2}&={\frac {ns_{\varepsilon }^{2}}{nS_{xx}-S_{x}^{2}}}=3.1539\\[8pt]s_{\widehat {\alpha }}^{2}&=s_{\widehat {\beta }}^{2}{\frac {1}{n}}S_{xx}=8.63185\end{aligned}}$

The 0.975 quantile of Student's *t*-distribution with 13 degrees of freedom is *t**13 = 2.1604, and thus the 95% confidence intervals for α and β are

${\begin{aligned}&\alpha \in [\,{\widehat {\alpha }}\mp t_{13}^{*}s_{\widehat {\alpha }}\,]=[\,{-45.4},\ {-32.7}\,]\\[5pt]&\beta \in [\,{\widehat {\beta }}\mp t_{13}^{*}s_{\widehat {\beta }}\,]=[\,57.4,\ 65.1\,]\end{aligned}}$

The product-moment correlation coefficient might also be calculated:

${\widehat {r}}={\frac {nS_{xy}-S_{x}S_{y}}{\sqrt {(nS_{xx}-S_{x}^{2})(nS_{yy}-S_{y}^{2})}}}=0.9946$

## Alternatives

In SLR, there is an underlying assumption that only the dependent variable contains measurement error; if the explanatory variable is also measured with error, then simple regression is not appropriate for estimating the underlying relationship because it will be biased due to regression dilution.

Other estimation methods that can be used in place of ordinary least squares include least absolute deviations (minimizing the sum of absolute values of residuals) and the Theil–Sen estimator (which chooses a line whose slope is the median of the slopes determined by pairs of sample points).

Deming regression (total least squares) also finds a line that fits a set of two-dimensional sample points, but (unlike ordinary least squares, least absolute deviations, and median slope regression) it is not really an instance of simple linear regression, because it does not separate the coordinates into one dependent and one independent variable and could potentially return a vertical line as its fit. can lead to a model that attempts to fit the outliers more than the data.

### Line fitting

Line fitting is the process of constructing a straight line that has the best fit to a series of data points.

Several methods exist, considering:

- Vertical distance: Simple linear regression
- Resistance to outliers: Robust simple linear regression
- Perpendicular distance: Orthogonal regression (this is not scale-invariant i.e. changing the measurement units leads to a different line.)
- Weighted geometric distance: Deming regression
- Scale invariant approach: Major axis regression This allows for measurement error in both variables, and gives an equivalent equation if the measurement units are altered.

### Simple linear regression without the intercept term (single regressor)

Sometimes it is appropriate to force the regression line to pass through the origin, because x and y are assumed to be proportional. For the model without the intercept term, *y* = *βx*, the OLS estimator for β simplifies to

${\widehat {\beta }}={\frac {\sum _{i=1}^{n}x_{i}y_{i}}{\sum _{i=1}^{n}x_{i}^{2}}}={\frac {\overline {xy}}{\overline {x^{2}}}}$

Substituting (*x* − *h*, *y* − *k*) in place of (*x*, *y*) gives the regression through (*h*, *k*):

${\begin{aligned}{\widehat {\beta }}&={\frac {\sum _{i=1}^{n}(x_{i}-h)(y_{i}-k)}{\sum _{i=1}^{n}(x_{i}-h)^{2}}}={\frac {\overline {(x-h)(y-k)}}{\overline {(x-h)^{2}}}}\\[6pt]&={\frac {{\overline {xy}}-k{\bar {x}}-h{\bar {y}}+hk}{{\overline {x^{2}}}-2h{\bar {x}}+h^{2}}}\\[6pt]&={\frac {{\overline {xy}}-{\bar {x}}{\bar {y}}+({\bar {x}}-h)({\bar {y}}-k)}{{\overline {x^{2}}}-{\bar {x}}^{2}+({\bar {x}}-h)^{2}}}\\[6pt]&={\frac {\operatorname {Cov} (x,y)+({\bar {x}}-h)({\bar {y}}-k)}{\operatorname {Var} (x)+({\bar {x}}-h)^{2}}},\end{aligned}}$

where Cov and Var refer to the covariance and variance of the sample data (uncorrected for bias). The last form above demonstrates how moving the line away from the center of mass of the data points affects the slope.

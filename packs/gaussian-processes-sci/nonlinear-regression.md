---
title: "Nonlinear regression"
source: https://en.wikipedia.org/wiki/Nonlinear_regression
domain: gaussian-processes-sci
license: CC-BY-SA-4.0
tags: gaussian process regression, covariance function, bayesian optimization, radial basis kernel
fetched: 2026-07-02
---

# Nonlinear regression

In statistics, **nonlinear regression** is a form of regression analysis in which observational data are modeled by a function which is a nonlinear combination of the model parameters and depends on one or more independent variables. The data are fitted by a method of successive approximations (iterations).

## General

In nonlinear regression, a statistical model of the form,

$\mathbf {y} \sim f(\mathbf {x} ,{\boldsymbol {\beta }})$

relates a vector of independent variables, $\mathbf {x}$ , and its associated observed dependent variables, $\mathbf {y}$ . The function f is nonlinear in the components of the vector of parameters $\beta$ , but otherwise arbitrary. For example, the Michaelis–Menten model for enzyme kinetics has two parameters and one independent variable, related by f by:

$f(x,{\boldsymbol {\beta }})={\frac {\beta _{1}x}{\beta _{2}+x}}$

This function, which is a rectangular hyperbola, is *nonlinear* because it cannot be expressed as a linear combination of the two $\beta$ s.

Systematic error may be present in the independent variables but its treatment is outside the scope of regression analysis. If the independent variables are not error-free, this is an errors-in-variables model, also outside this scope.

Other examples of nonlinear functions include exponential functions, logarithmic functions, trigonometric functions, power functions, Gaussian function, and Lorentz distributions. Some functions, such as the exponential or logarithmic functions, can be transformed so that they are linear. When so transformed, standard linear regression can be performed but must be applied with caution. See § Linearization §§ Transformation, below, for more details. In microbiology and biotechnology, nonlinear regression is used to model complex microbial growth kinetics. While simple growth follows monoauxic functions (such as the Gompertz or Boltzmann models), multiphasic (polyauxic) growth is modeled using linear combinations of these nonlinear functions. Estimating parameters for these complex models often requires robust regression techniques (e.g., using a Lorentzian loss function to mitigate outliers) and global optimization algorithms (such as Differential evolution with L-BFGS-B) to avoid local minima and ensure biologically interpretable results.

In general, there is no closed-form expression for the best-fitting parameters, as there is in linear regression. Usually numerical optimization algorithms are applied to determine the best-fitting parameters. Again in contrast to linear regression, there may be many local minima of the function to be optimized and even the global minimum may produce a biased estimate. In practice, estimated values of the parameters are used, in conjunction with the optimization algorithm, to attempt to find the global minimum of a sum of squares.

For details concerning nonlinear data modeling see least squares and non-linear least squares.

## Regression statistics

The assumption underlying this procedure is that the model can be approximated by a linear function, namely a first-order Taylor series:

$f(x_{i},{\boldsymbol {\beta }})\approx f(x_{i},0)+\sum _{j}J_{ij}\beta _{j}$

where $J_{ij}={\frac {\partial f(x_{i},{\boldsymbol {\beta }})}{\partial \beta _{j}}}$ are Jacobian matrix elements. It follows from this that the least squares estimators are given by

${\hat {\boldsymbol {\beta }}}\approx \mathbf {(J^{T}J)^{-1}J^{T}y} ,$ compare generalized least squares with covariance matrix proportional to the unit matrix. The nonlinear regression statistics are computed and used as in linear regression statistics, but using **J** in place of **X** in the formulas.

When the function $f(x_{i},{\boldsymbol {\beta }})$ itself is not known analytically, but needs to be linearly approximated from $n+1$ , or more, known values (where n is the number of estimators), the best estimator is obtained directly from the Linear Template Fit as ${\hat {\boldsymbol {\beta }}}=((\mathbf {Y{\tilde {M}}} )^{\mathsf {T}}{\boldsymbol {\Omega }}^{-1}\mathbf {Y{\tilde {M}}} )^{-1}(\mathbf {Y{\tilde {M}}} )^{\mathsf {T}}{\boldsymbol {\Omega }}^{-1}(\mathbf {d} -\mathbf {Y{\bar {m}})}$ (see also linear least squares).

The linear approximation introduces bias into the statistics. Therefore, more caution than usual is required in interpreting statistics derived from a nonlinear model.

## Ordinary and weighted least squares

The best-fit curve is often assumed to be that which minimizes the sum of squared residuals. This is the ordinary least squares (OLS) approach. However, in cases where the dependent variable does not have constant variance, or there are some outliers, a sum of weighted squared residuals may be minimized; see weighted least squares. Each weight should ideally be equal to the reciprocal of the variance of the observation, or the reciprocal of the dependent variable to some power in the outlier case, but weights may be recomputed on each iteration, in an iteratively weighted least squares algorithm.

## Linearization

### Transformation

Some nonlinear regression problems can be moved to a linear domain by a suitable transformation of the model formulation.

For example, consider the nonlinear regression problem

$y=ae^{bx}U$

with parameters *a* and *b* and with multiplicative error term *U*. If we take the logarithm of both sides, this becomes

$\ln {(y)}=\ln {(a)}+bx+u,$

where *u* = ln(*U*), suggesting estimation of the unknown parameters by a linear regression of ln(*y*) on *x*, a computation that does not require iterative optimization. However, use of a nonlinear transformation requires caution. The influences of the data values will change, as will the error structure of the model and the interpretation of any inferential results. These may not be desired effects. On the other hand, depending on what the largest source of error is, a nonlinear transformation may distribute the errors in a Gaussian fashion, so the choice to perform a nonlinear transformation must be informed by modeling considerations.

For Michaelis–Menten kinetics, the linear Lineweaver–Burk plot

${\frac {1}{v}}={\frac {1}{V_{\max }}}+{\frac {K_{m}}{V_{\max }[S]}}$

of 1/*v* against 1/[*S*] has been much used. However, since it is very sensitive to data error and is strongly biased toward fitting the data in a particular range of the independent variable, [*S*], its use is strongly discouraged.

For error distributions that belong to the exponential family, a link function may be used to transform the parameters under the Generalized linear model framework.

### Segmentation

The *independent* or *explanatory variable* (say X) can be split up into classes or segments and linear regression can be performed per segment. Segmented regression with confidence analysis may yield the result that the *dependent* or *response* variable (say Y) behaves differently in the various segments. For example, the figure shows that the soil salinity (X) initially exerts no influence on the crop yield (Y) of mustard, until a *critical* or *threshold* value (*breakpoint*), after which the yield is affected negatively.

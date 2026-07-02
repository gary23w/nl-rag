---
title: "Polynomial regression"
source: https://en.wikipedia.org/wiki/Polynomial_regression
domain: polynomial-regression
license: CC-BY-SA-4.0
tags: polynomial regression, orthogonal polynomials, segmented regression, curve fitting
fetched: 2026-07-02
---

# Polynomial regression

In statistics, **polynomial regression** is a form of regression analysis in which the relationship between the independent variable *x* and the dependent variable *y* is modeled as a polynomial in *x*. Polynomial regression fits a nonlinear relationship between the value of *x* and the corresponding conditional mean of *y*, denoted E(*y* |*x*). Although polynomial regression fits a nonlinear model to the data, as a statistical estimation problem it is linear, in the sense that the regression function E(*y* | *x*) is linear in the unknown parameters that are estimated from the data. Thus, polynomial regression is a special case of multiple linear regression.

The explanatory (independent) variables resulting from the polynomial expansion of the "baseline" variables are known as higher-degree terms. Such variables are also used in classification settings.

## History

Polynomial regression models are usually fit using the method of least squares. The least-squares method minimizes the variance of the unbiased estimators of the coefficients, under the conditions of the Gauss–Markov theorem. The least-squares method was published in 1805 by Legendre and in 1809 by Gauss. The first design of an experiment for polynomial regression appeared in an 1815 paper of Gergonne. In the twentieth century, polynomial regression played an important role in the development of regression analysis, with a greater emphasis on issues of design and inference. More recently, the use of polynomial models has been complemented by other methods, with non-polynomial models having advantages for some classes of problems.

## Definition and example

The goal of regression analysis is to model the expected value of a dependent variable *y* in terms of the value of an independent variable (or vector of independent variables) *x*. In simple linear regression, the model

$y=\beta _{0}+\beta _{1}x+\varepsilon ,\,$

is used, where ε is an unobserved random error with mean zero conditioned on a scalar variable *x*. In this model, for each unit increase in the value of *x*, the conditional expectation of *y* increases by *β*1 units.

In many settings, such a linear relationship may not hold. For example, if we are modeling the yield of a chemical synthesis in terms of the temperature at which the synthesis takes place, we may find that the yield improves by a different amount for each unit increase in temperature. Or we may find that the yield decreases with increasing temperature (but only for a certain range of temperatures) and increases with increasing temperature in a different range of temperatures. In this case, we might propose a quadratic model of the form

$y=\beta _{0}+\beta _{1}x+\beta _{2}x^{2}+\varepsilon .\,$

In this model, when the temperature is increased from *x* to *x* + 1 units, the expected yield changes by $\beta _{1}+\beta _{2}(2x+1).$ (This can be seen by obtaining the derivative with respect to x of the regression formula.) For infinitesimal changes in *x*, the effect on *y* is given by the total derivative with respect to *x*: $\beta _{1}+2\beta _{2}x.$ The fact that the change in yield depends on *x* is what makes the relationship between *x* and *y* nonlinear even though the model is linear in the parameters to be estimated.

In general, we can model the expected value of *y* as an *n*th degree polynomial, yielding the general polynomial regression model

$y=\beta _{0}+\beta _{1}x+\beta _{2}x^{2}+\beta _{3}x^{3}+\cdots +\beta _{n}x^{n}+\varepsilon .\,$

Conveniently, these models are all linear from the point of view of estimation, since the regression function is linear in terms of the unknown parameters *β*0, *β*1, .... Therefore, for least squares analysis, the computational and inferential problems of polynomial regression can be completely addressed using the techniques of multiple regression. This is done by treating *x*, *x*2, ... as being distinct independent variables in a multiple regression model.

## Matrix form and calculation of estimates

The polynomial regression model

$y_{i}\,=\,\beta _{0}+\beta _{1}x_{i}+\beta _{2}x_{i}^{2}+\cdots +\beta _{m}x_{i}^{m}+\varepsilon _{i}\ (i=1,2,\dots ,n)$

can be expressed in matrix form in terms of a design matrix $\mathbf {X}$ , a response vector ${\vec {y}}$ , a parameter vector ${\vec {\beta }}$ , and a vector ${\vec {\varepsilon }}$ of random errors. The *i*-th row of $\mathbf {X}$ and ${\vec {y}}$ will contain the *x* and *y* value for the *i*-th data sample. Then the model can be written as a system of linear equations:

${\begin{bmatrix}y_{1}\\y_{2}\\y_{3}\\\vdots \\y_{n}\end{bmatrix}}={\begin{bmatrix}1&x_{1}&x_{1}^{2}&\dots &x_{1}^{m}\\1&x_{2}&x_{2}^{2}&\dots &x_{2}^{m}\\1&x_{3}&x_{3}^{2}&\dots &x_{3}^{m}\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&x_{n}&x_{n}^{2}&\dots &x_{n}^{m}\end{bmatrix}}{\begin{bmatrix}\beta _{0}\\\beta _{1}\\\beta _{2}\\\vdots \\\beta _{m}\end{bmatrix}}+{\begin{bmatrix}\varepsilon _{1}\\\varepsilon _{2}\\\varepsilon _{3}\\\vdots \\\varepsilon _{n}\end{bmatrix}},$

which when using pure matrix notation is written as

${\vec {y}}=\mathbf {X} {\vec {\beta }}+{\vec {\varepsilon }}.\,$

The vector of estimated polynomial regression coefficients (using ordinary least squares estimation) is

${\widehat {\vec {\beta }}}=(\mathbf {X} ^{\mathsf {T}}\mathbf {X} )^{-1}\;\mathbf {X} ^{\mathsf {T}}{\vec {y}},\,$

assuming *m* < *n* which is required for the matrix to be invertible; then since $\mathbf {X}$ is a Vandermonde matrix, the invertibility condition is guaranteed to hold if all the $x_{i}$ values are distinct. This is the unique least-squares solution. In other words, it realizes the minimum of the distance $\|{\vec {\varepsilon }}\|$ between the sample $y_{i}$ and the corresponding value of the polynomial, $\sum _{k=1}^{m}\beta _{k}x_{i}^{k}$ , that is, it realizes the minimum

$\min _{\vec {\beta }}\sum _{i=1}^{n}\left(y_{i}-\sum _{k=1}^{m}\beta _{k}x_{i}^{k}\right)^{2}.$

### Expanded formulas

The above matrix equations explain the behavior of polynomial regression well. However, to physically implement polynomial regression for a set of xy point pairs, more detail is useful. The below matrix equations for polynomial coefficients are expanded from regression theory without derivation and easily implemented.

${\begin{bmatrix}\sum _{i=1}^{n}x_{i}^{0}&\sum _{i=1}^{n}x_{i}^{1}&\sum _{i=1}^{n}x_{i}^{2}&\cdots &\sum _{i=1}^{n}x_{i}^{m}\\\sum _{i=1}^{n}x_{i}^{1}&\sum _{i=1}^{n}x_{i}^{2}&\sum _{i=1}^{n}x_{i}^{3}&\cdots &\sum _{i=1}^{n}x_{i}^{m+1}\\\sum _{i=1}^{n}x_{i}^{2}&\sum _{i=1}^{n}x_{i}^{3}&\sum _{i=1}^{n}x_{i}^{4}&\cdots &\sum _{i=1}^{n}x_{i}^{m+2}\\\vdots &\vdots &\vdots &\ddots &\vdots \\\sum _{i=1}^{n}x_{i}^{m}&\sum _{i=1}^{n}x_{i}^{m+1}&\sum _{i=1}^{n}x_{i}^{m+2}&\dots &\sum _{i=1}^{n}x_{i}^{2m}\\\end{bmatrix}}{\begin{bmatrix}\beta _{0}\\\beta _{1}\\\beta _{2}\\\cdots \\\beta _{m}\\\end{bmatrix}}={\begin{bmatrix}\sum _{i=1}^{n}y_{i}x_{i}^{0}\\\sum _{i=1}^{n}y_{i}x_{i}^{1}\\\sum _{i=1}^{n}y_{i}x_{i}^{2}\\\cdots \\\sum _{i=1}^{n}y_{i}x_{i}^{m}\\\end{bmatrix}}$

After solving the above system of linear equations for $\beta _{0}{\text{ through }}\beta _{m}$ , the regression polynomial may be constructed as follows:

${\begin{aligned}&\qquad {\widehat {y}}=\beta _{0}x^{0}+\beta _{1}x^{1}+\beta _{2}x^{2}+\cdots +\beta _{m}x^{m}\\&\qquad \\&\qquad {\text{Where:}}\\&\qquad n={\text{number of }}x_{i}y_{i}{\text{ variable pairs in the data}}\\&\qquad m={\text{order of the polynomial to be used for regression}}\\&\qquad \beta _{(0-m)}={\text{polynomial coefficient for each corresponding }}x^{(0-m)}\\&\qquad {\widehat {y}}={\text{estimated y variable based on the polynomial regression calculations.}}\end{aligned}}$

## Interpretation

Although polynomial regression is technically a special case of multiple linear regression, the interpretation of a fitted polynomial regression model requires a somewhat different perspective. It is often difficult to interpret the individual coefficients in a polynomial regression fit, since the underlying monomials can be highly correlated. For example, *x* and *x*2 have correlation around 0.97 when x is uniformly distributed on the interval (0, 1). Although the correlation can be reduced by using orthogonal polynomials, it is generally more informative to consider the fitted regression function as a whole. Point-wise or simultaneous confidence bands can then be used to provide a sense of the uncertainty in the estimate of the regression function.

## Alternative approaches

Polynomial regression is one example of regression analysis using basis functions to model a functional relationship between two quantities. More specifically, it replaces $x\in \mathbb {R} ^{d_{x}}$ in linear regression with polynomial basis $\varphi (x)\in \mathbb {R} ^{d_{\varphi }}$ , e.g. $[1,x]{\mathbin {\stackrel {\varphi }{\rightarrow }}}[1,x,x^{2},\ldots ,x^{d}]$ . A drawback of polynomial bases is that the basis functions are "non-local", meaning that the fitted value of *y* at a given value *x* = *x*0 depends strongly on data values with *x* far from *x*0. In modern statistics, polynomial basis-functions are used along with new basis functions, such as splines, radial basis functions, and wavelets. These families of basis functions offer a more parsimonious fit for many types of data.

The goal of polynomial regression is to model a non-linear relationship between the independent and dependent variables (technically, between the independent variable and the conditional mean of the dependent variable). This is similar to the goal of nonparametric regression, which aims to capture non-linear regression relationships. Therefore, non-parametric regression approaches such as smoothing can be useful alternatives to polynomial regression. Some of these methods make use of a localized form of classical polynomial regression. An advantage of traditional polynomial regression is that the inferential framework of multiple regression can be used (this also holds when using other families of basis functions such as splines).

A final alternative is to use kernelized models such as support vector regression with a polynomial kernel.

If residuals have unequal variance, a weighted least squares estimator may be used to account for that.

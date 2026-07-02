---
title: "Iteratively reweighted least squares"
source: https://en.wikipedia.org/wiki/Iteratively_reweighted_least_squares
domain: generalized-linear-models
license: CC-BY-SA-4.0
tags: generalized linear model, link function, exponential family, quasi-likelihood
fetched: 2026-07-02
---

# Iteratively reweighted least squares

The method of **iteratively reweighted least squares** (**IRLS**) is used to solve certain optimization problems with objective functions of the form of a *p*-norm, $\operatorname {arg\,min} _{\boldsymbol {\beta }}\sum _{i=1}^{n}{\big |}y_{i}-f_{i}({\boldsymbol {\beta }}){\big |}^{p},$ by an iterative method in which each step involves solving a weighted least squares problem of the form ${\boldsymbol {\beta }}^{(t+1)}=\operatorname {arg\,min} _{\boldsymbol {\beta }}\sum _{i=1}^{n}w_{i}({\boldsymbol {\beta }}^{(t)}){\big |}y_{i}-f_{i}({\boldsymbol {\beta }}){\big |}^{2}.$

IRLS is used to find the maximum likelihood estimates of a generalized linear model, and in robust regression to find an M-estimator, as a way of mitigating the influence of outliers in an otherwise normally distributed data set, for example, by minimizing the least absolute errors rather than the least square errors.

One of the advantages of IRLS over linear programming and convex programming is that it can be used with Gauss–Newton and Levenberg–Marquardt numerical algorithms.

## Examples

### *L*1 minimization for sparse recovery

IRLS can be used for ***ℓ*1** minimization and smoothed ***ℓ*p** minimization, *p* < 1, in compressed sensing problems. It has been proved that the algorithm has a linear rate of convergence for *ℓ*1 norm and superlinear for *ℓ**t* with *t* < 1, under the restricted isometry property, which is generally a sufficient condition for sparse solutions.

### *Lp* norm linear regression

To find the parameters ***β*** = (*β*1, …,*β**k*)T which minimize the *Lp* norm for the linear regression problem, ${\underset {\boldsymbol {\beta }}{\operatorname {arg\,min} }}{\big \|}\mathbf {y} -X{\boldsymbol {\beta }}\|_{p}={\underset {\boldsymbol {\beta }}{\operatorname {arg\,min} }}\sum _{i=1}^{n}\left|y_{i}-X_{i}{\boldsymbol {\beta }}\right|^{p},$ the IRLS algorithm at step *t* + 1 involves solving the weighted linear least squares problem ${\boldsymbol {\beta }}^{(t+1)}={\underset {\boldsymbol {\beta }}{\operatorname {arg\,min} }}\sum _{i=1}^{n}w_{i}^{(t)}\left|y_{i}-X_{i}{\boldsymbol {\beta }}\right|^{2}=(X^{\rm {T}}W^{(t)}X)^{-1}X^{\rm {T}}W^{(t)}\mathbf {y} ,$ where *W*(*t*) is the diagonal matrix of weights, usually with all elements set initially to $w_{i}^{(0)}=1$ and updated after each iteration to $w_{i}^{(t)}={\big |}y_{i}-X_{i}{\boldsymbol {\beta }}^{(t)}{\big |}^{p-2}.$

In the case *p* = 1, this corresponds to least absolute deviation regression (in this case, the problem would be better approached by use of linear programming methods, so the result would be exact) and the formula is $w_{i}^{(t)}={\frac {1}{{\big |}y_{i}-X_{i}{\boldsymbol {\beta }}^{(t)}{\big |}}}.$

To avoid dividing by zero, regularization must be done, so in practice the formula is $w_{i}^{(t)}={\frac {1}{\max \left\{\delta ,\left|y_{i}-X_{i}{\boldsymbol {\beta }}^{(t)}\right|\right\}}}.$ where $\delta$ is some small value, like 0.0001. Note the use of $\delta$ in the weighting function is equivalent to the Huber loss function in robust estimation.

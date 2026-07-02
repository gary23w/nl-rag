---
title: "Poisson regression"
source: https://en.wikipedia.org/wiki/Poisson_regression
domain: poisson-regression
license: CC-BY-SA-4.0
tags: poisson regression, count data, overdispersion, negative binomial
fetched: 2026-07-02
---

# Poisson regression

In statistics, **Poisson regression** is a generalized linear model form of regression analysis used to model count data and contingency tables. Poisson regression assumes the response variable *Y* has a Poisson distribution, and assumes the logarithm of its expected value can be modeled by a linear combination of unknown parameters. A Poisson regression model is sometimes known as a log-linear model, especially when used to model contingency tables.

**Negative binomial regression** is a popular generalization of Poisson regression because it loosens the highly restrictive assumption that the variance is equal to the mean made by the Poisson model. The traditional negative binomial regression model is based on the Poisson-gamma mixture distribution. This model is popular because it models the Poisson heterogeneity with a gamma distribution.

Poisson regression models are generalized linear models with the logarithm as the (canonical) link function, and the Poisson distribution function as the assumed probability distribution of the response.

## Regression models

If $\mathbf {x} \in \mathbb {R} ^{n}$ is a vector of independent variables, then the model takes the form

$\log(\operatorname {E} (Y\mid \mathbf {x} ))=\alpha +\mathbf {\beta } '\mathbf {x} ,$

where $\alpha \in \mathbb {R}$ and $\mathbf {\beta } \in \mathbb {R} ^{n}$ . Sometimes this is written more compactly as

$\log(\operatorname {E} (Y\mid \mathbf {x} ))={\boldsymbol {\theta }}'\mathbf {x} ,\,$

where $\mathbf {x}$ is now an (*n* + 1)-dimensional vector consisting of *n* independent variables concatenated to the number one. Here $\theta$ is simply $\beta$ concatenated to $\alpha$ .

Thus, when given a Poisson regression model $\theta$ and an input vector $\mathbf {x}$ , the predicted mean of the associated Poisson distribution is given by

$\operatorname {E} (Y\mid \mathbf {x} )=e^{{\boldsymbol {\theta }}'\mathbf {x} }.\,$

If $Y_{i}$ are independent observations with corresponding values $\mathbf {x} _{i}$ of the predictor variables, then $\theta$ can be estimated by maximum likelihood. The maximum-likelihood estimates lack a closed-form expression and must be found by numerical methods. The probability surface for maximum-likelihood Poisson regression is always concave, making Newton–Raphson or other gradient-based methods appropriate estimation techniques.

## Interpretation of coefficients

Suppose we have a model with a single predictor, that is, $n=1$ :

$\log(\operatorname {E} (Y\mid \mathbf {x} ))=\alpha +\beta x$

Suppose we compute the predicted values at point $(Y_{2},x_{2})$ and $(Y_{1},x_{1})$ :

$\log(\operatorname {E} (Y_{2}\mid x_{2}))=\alpha +\beta x_{2}$

$\log(\operatorname {E} (Y_{1}\mid x_{1}))=\alpha +\beta x_{1}$

By subtracting the first from the second:

$\log(\operatorname {E} (Y_{2}\mid x_{2}))-\log(\operatorname {E} (Y_{1}\mid x_{1}))=\beta (x_{2}-x_{1})$

Suppose now that $x_{2}=x_{1}+1$ . We obtain:

$\log(\operatorname {E} (Y_{2}\mid x_{2}))-\log(\operatorname {E} (Y_{1}\mid x_{1}))=\beta$

So the coefficient of the model is to be interpreted as the increase in the logarithm of the count of the outcome variable when the independent variable increases by 1.

By applying the rules of logarithms:

$\log \left({\dfrac {\operatorname {E} (Y_{2}\mid x_{2})}{\operatorname {E} (Y_{1}\mid x_{1})}}\right)=\beta$

${\dfrac {\operatorname {E} (Y_{2}\mid x_{2})}{\operatorname {E} (Y_{1}\mid x_{1})}}=e^{\beta }$

$\operatorname {E} (Y_{2}\mid x_{2})=e^{\beta }\operatorname {E} (Y_{1}\mid x_{1})$

That is, when the independent variable increases by 1, the outcome variable is multiplied by the exponentiated coefficient.

The exponentiated coefficient is also called the *incidence ratio*.

### Average partial effect

Often, the object of interest is the average partial effect or average marginal effect ${\frac {\partial E(Y|x)}{\partial x}}$ , which is interpreted as the change in the outcome Y for a one unit change in the independent variable x . The average partial effect in the Poisson model for a continuous x can be shown to be:

${\frac {\partial E(Y|x)}{\partial x}}=\exp(\theta '\mathbb {x} )\beta$

This can be estimated using the coefficient estimates from the Poisson model ${\hat {\theta }}=({\hat {\alpha }},{\hat {\beta }})$ with the observed values of $\mathbb {x}$ .

## Maximum likelihood-based parameter estimation

Given a set of parameters *θ* and an input vector *x*, the mean of the predicted Poisson distribution, as stated above, is given by

${\displaystyle \lambda$

and thus, the Poisson distribution's probability mass function is given by

$p(y\mid x;\theta )={\frac {\lambda ^{y}}{y!}}e^{-\lambda }={\frac {e^{y\theta 'x}e^{-e^{\theta 'x}}}{y!}}$

Now suppose we are given a data set consisting of *m* vectors $x_{i}\in \mathbb {R} ^{n+1},\,i=1,\ldots ,m$ , along with a set of *m* values $y_{1},\ldots ,y_{m}\in \mathbb {N}$ . Then, for a given set of parameters *θ*, the probability of attaining this particular set of data is given by

$p(y_{1},\ldots ,y_{m}\mid x_{1},\ldots ,x_{m};\theta )=\prod _{i=1}^{m}{\frac {e^{y_{i}\theta 'x_{i}}e^{-e^{\theta 'x_{i}}}}{y_{i}!}}.$

By the method of maximum likelihood, we wish to find the set of parameters *θ* that makes this probability as large as possible. To do this, the equation is first rewritten as a likelihood function in terms of *θ*:

$L(\theta \mid X,Y)=\prod _{i=1}^{m}{\frac {e^{y_{i}\theta 'x_{i}}e^{-e^{\theta 'x_{i}}}}{y_{i}!}}.$

Note that the expression on the right hand side has not actually changed. A formula in this form is typically difficult to work with; instead, one uses the *log-likelihood*:

$\ell (\theta \mid X,Y)=\log L(\theta \mid X,Y)=\sum _{i=1}^{m}\left(y_{i}\theta 'x_{i}-e^{\theta 'x_{i}}-\log(y_{i}!)\right).$

Notice that the parameters *θ* only appear in the first two terms of each term in the summation. Therefore, given that we are only interested in finding the best value for *θ* we may drop the *y**i*! and simply write

$\ell (\theta \mid X,Y)=\sum _{i=1}^{m}\left(y_{i}\theta 'x_{i}-e^{\theta 'x_{i}}\right).$

To find a maximum, we need to solve an equation ${\frac {\partial \ell (\theta \mid X,Y)}{\partial \theta }}=0$ which has no closed-form solution. However, the negative log-likelihood, $-\ell (\theta \mid X,Y)$ , is a convex function, and so standard convex optimization techniques such as gradient descent can be applied to find the optimal value of *θ*.

## Poisson regression in practice

Poisson regression may be appropriate when the dependent variable is a count, for instance of events such as the arrival of a telephone call at a call centre. The events must be independent in the sense that the arrival of one call will not make another more or less likely, but the probability per unit time of events is understood to be related to covariates such as time of day.

### "Exposure" and offset

Poisson regression may also be appropriate for rate data, where the rate is a count of events divided by some measure of that unit's *exposure* (a particular unit of observation). For example, biologists may count the number of tree species in a forest: events would be tree observations, exposure would be unit area, and rate would be the number of species per unit area. Demographers may model death rates in geographic areas as the count of deaths divided by person−years. More generally, event rates can be calculated as events per unit time, which allows the observation window to vary for each unit. In these examples, exposure is respectively unit area, person−years and unit time. In Poisson regression this is handled as an **offset**. If the rate is count/exposure, multiplying both sides of the equation by exposure moves it to the right side of the equation. When both sides of the equation are then logged, the final model contains log(exposure) as a term that is added to the regression coefficients. This logged variable, log(exposure), is called the offset variable and enters on the right-hand side of the equation with a parameter estimate (for log(exposure)) constrained to 1.

$\log(\operatorname {E} (Y\mid x))=\theta 'x$

which implies

$\log \left({\frac {\operatorname {E} (Y\mid x)}{\text{exposure}}}\right)=\log(\operatorname {E} (Y\mid x))-\log({\text{exposure}})=\theta 'x$

$\log \left(\operatorname {E} (Y\mid x)\right)=\theta 'x+\log({\text{exposure}})$

Offset in the case of a GLM in R can be achieved using the `offset()` function:

```mw
glm(y ~ offset(log(exposure)) + x, family=poisson(link=log) )
```

### Overdispersion and zero inflation

A characteristic of the Poisson distribution is that its mean is equal to its variance. In certain circumstances, it will be found that the observed variance is greater than the mean; this is known as overdispersion and indicates that the model is not appropriate. A common reason is the omission of relevant explanatory variables, or dependent observations. Under some circumstances, the problem of overdispersion can be solved by using quasi-likelihood estimation or a negative binomial distribution instead.

Ver Hoef and Boveng described the difference between quasi-Poisson (also called overdispersion with quasi-likelihood) and negative binomial (equivalent to gamma-Poisson) as follows: If *E*(*Y*) = *μ*, the quasi-Poisson model assumes var(*Y*) = *θμ* while the gamma-Poisson assumes var(*Y*) = *μ*(1 + *κμ*), where *θ* is the quasi-Poisson overdispersion parameter, and *κ* is the shape parameter of the negative binomial distribution. For both models, parameters are estimated using iteratively reweighted least squares. For quasi-Poisson, the weights are *μ*/*θ*. For negative binomial, the weights are *μ*/(1 + *κμ*). With large *μ* and substantial extra-Poisson variation, the negative binomial weights are capped at 1/*κ*. Ver Hoef and Boveng discussed an example where they selected between the two by plotting mean squared residuals vs. the mean.

Another common problem with Poisson regression is excess zeros: if there are two processes at work, one determining whether there are zero events or any events, and a Poisson process determining how many events there are, there will be more zeros than a Poisson regression would predict. An example would be the distribution of cigarettes smoked in an hour by members of a group where some individuals are non-smokers.

Other generalized linear models such as the negative binomial model or zero-inflated model may function better in these cases.

On the contrary, underdispersion may pose an issue for parameter estimation.

### Use in survival analysis

Poisson regression creates proportional hazards models, one class of survival analysis: see proportional hazards models for descriptions of Cox models.

## Extensions

### Regularized Poisson regression

When estimating the parameters for Poisson regression, one typically tries to find values for *θ* that maximize the likelihood of an expression of the form

$\sum _{i=1}^{m}\log(p(y_{i};e^{\theta 'x_{i}})),$

where *m* is the number of examples in the data set, and $p(y_{i};e^{\theta 'x_{i}})$ is the probability mass function of the Poisson distribution with the mean set to $e^{\theta 'x_{i}}$ . Regularization can be added to this optimization problem by instead maximizing

$\sum _{i=1}^{m}\log(p(y_{i};e^{\theta 'x_{i}}))-\lambda \left\|\theta \right\|_{2}^{2},$

for some positive constant $\lambda$ . This technique, similar to ridge regression, can reduce overfitting.

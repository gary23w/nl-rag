---
title: "Multicollinearity"
source: https://en.wikipedia.org/wiki/Multicollinearity
domain: multiple-regression
license: CC-BY-SA-4.0
tags: multiple regression, multicollinearity, variance inflation factor, partial regression
fetched: 2026-07-02
---

# Multicollinearity

In statistics, **multicollinearity** or **collinearity** is a situation where the predictors in a regression model are linearly dependent.

**Perfect multicollinearity** refers to a situation where the predictive variables have an *exact* linear relationship. When there is perfect collinearity, the design matrix X has less than full rank, and therefore the moment matrix $X^{\mathsf {T}}X$ cannot be inverted. In this situation, the parameter estimates of the regression are not well-defined, as the system of equations has infinitely many solutions.

**Imperfect multicollinearity** refers to a situation where the predictive variables have a *nearly* exact linear relationship.

The Gauss–Markov theorem assumes absence of perfect multicollinearity.

The adverse effect of highly correlated variables is widely known and proven many times.

To address the high collinearity of a dataset, variance inflation factor can be used to identify the collinearity of the predictor variables.

## Perfect multicollinearity

Perfect multicollinearity refers to a situation where the predictors are linearly dependent (one can be written as an exact linear function of the others). Ordinary least squares requires inverting the matrix $X^{\mathsf {T}}X$ , where

$X={\begin{bmatrix}1&X_{11}&\cdots &X_{k1}\\\vdots &\vdots &&\vdots \\1&X_{1N}&\cdots &X_{kN}\end{bmatrix}}$

is an *$N\times (k+1)$* matrix, where *N* is the number of observations, *k* is the number of explanatory variables, and *$N\geq k+1$*. If there is an exact linear relationship among the independent variables, then at least one of the columns of X is a linear combination of the others, and so the rank of X (and therefore of $X^{\mathsf {T}}X$ ) is less than *$k+1$*, and the matrix $X^{\mathsf {T}}X$ will not be invertible.

### Resolution

Perfect collinearity is typically caused by including redundant variables in a regression. For example, a dataset may include variables for income, expenses, and savings. However, because income is equal to expenses plus savings by definition, it is incorrect to include all 3 variables in a regression simultaneously. Similarly, including a dummy variable for every category (e.g., summer, autumn, winter, and spring) as well as an intercept term will result in perfect collinearity. This is known as the dummy variable trap.

The other common cause of perfect collinearity is attempting to use ordinary least squares when working with very wide datasets (those with more variables than observations). These require more advanced data analysis techniques like Bayesian hierarchical modeling to produce meaningful results.

## Numerical issues

Sometimes, the variables $X_{j}$ are nearly collinear. In this case, the matrix $X^{\mathsf {T}}X$ has an inverse, but it is ill-conditioned. A computer algorithm may or may not be able to compute an approximate inverse; even if it can, the resulting inverse may have large rounding errors.

The standard measure of ill-conditioning in a matrix is the condition index. This determines if the inversion of the matrix is numerically unstable with finite-precision numbers, indicating the potential sensitivity of the computed inverse to small changes in the original matrix. The condition number is computed by finding the maximum singular value divided by the minimum singular value of the design matrix. In the context of collinear variables, the variance inflation factor is the condition number for a particular coefficient.

### Solutions

Numerical problems in estimating can be solved by applying standard techniques from linear algebra to estimate the equations more precisely:

1. **Standardizing** **predictor variables.** Working with polynomial terms (e.g. $x_{1}$ , $x_{1}^{2}$ ), including interaction terms (i.e., $x_{1}\times x_{2}$ ) can cause multicollinearity. This is especially true when the variable in question has a limited range. Standardizing predictor variables will eliminate this special kind of multicollinearity for polynomials of up to 3rd order.
  - For higher-order polynomials, an orthogonal polynomial representation will generally fix any collinearity problems. However, polynomial regressions are generally unstable, making them unsuitable for nonparametric regression and inferior to newer methods based on smoothing splines, LOESS, or Gaussian process regression.
2. **Use an orthogonal representation of the data**. Poorly-written statistical software will sometimes fail to converge to a correct representation when variables are strongly correlated. However, it is still possible to rewrite the regression to use only uncorrelated variables by performing a change of basis.
  - For polynomial terms in particular, it is possible to rewrite the regression as a function of uncorrelated variables using orthogonal polynomials.

## Effects on coefficient estimates

In addition to causing numerical problems, imperfect collinearity makes precise estimation of variables difficult. In other words, highly correlated variables lead to poor estimates and large standard errors.

As an example, say that we notice Alice wears her boots whenever it is raining and that there are only puddles when it rains. Then, we cannot tell whether she wears boots to keep the rain from landing on her feet, or to keep her feet dry if she steps in a puddle.

The problem with trying to identify how much each of the two variables matters is that they are confounded with each other: our observations are explained equally well by either variable, so we do not know which one of them causes the observed correlations.

There are two ways to discover this information:

1. Using prior information or theory. For example, if we notice Alice never steps in puddles, we can reasonably argue puddles are not why she wears boots, as she does not need the boots to avoid puddles.
2. Collecting more data. If we observe Alice enough times, we will eventually see her on days where there are puddles but not rain (e.g. because the rain stops before she leaves home).

This confounding becomes substantially worse when researchers attempt to ignore or suppress it by excluding these variables from the regression (see #Misuse). Excluding multicollinear variables from regressions will invalidate causal inference and produce worse estimates by removing important confounders.

Multicollinearity can significantly affect the stability and interpretability of regression models. When predictor variables are highly correlated, the variance of the estimated regression coefficients increases, which may lead to large standard errors and unreliable statistical inference. As a result, coefficients may appear statistically insignificant even when the overall model has strong explanatory power. This issue does not necessarily reduce predictive performance, but it complicates the interpretation of individual predictors.

### Remedies

There are many ways to prevent multicollinearity from affecting results by planning ahead of time. However, these methods all require a researcher to decide on a procedure and analysis *before* data has been collected (see post hoc analysis and Multicollinearity § Misuse).

#### Regularized estimators

Many regression methods are naturally "robust" to multicollinearity and generally perform better than ordinary least squares regression, even when variables are independent. Regularized regression techniques such as ridge regression, LASSO, elastic net regression, or spike-and-slab regression are less sensitive to including "useless" predictors, a common cause of collinearity. These techniques can detect and remove these predictors automatically to avoid problems. Bayesian hierarchical models (provided by software like BRMS) can perform such regularization automatically, learning informative priors from the data.

Often, problems caused by the use of frequentist estimation are misunderstood or misdiagnosed as being related to multicollinearity. Researchers are often frustrated not by multicollinearity, but by their inability to incorporate relevant prior information in regressions. For example, complaints that coefficients have "wrong signs" or confidence intervals that "include unrealistic values" indicate there is important prior information that is not being incorporated into the model. When this is information is available, it should be incorporated into the prior using Bayesian regression techniques.

Stepwise regression (the procedure of excluding "collinear" or "insignificant" variables) is especially vulnerable to multicollinearity, and is one of the few procedures wholly invalidated by it (with any collinearity resulting in heavily biased estimates and invalidated p-values).

#### Improved experimental design

When conducting experiments where researchers have control over the predictive variables, researchers can often avoid collinearity by choosing an optimal experimental design in consultation with a statistician.

#### Acceptance

While the above strategies work in some situations, estimates using advanced techniques may still produce large standard errors. In such cases, the correct response to multicollinearity is to "do nothing". The scientific process often involves null or inconclusive results; not every experiment will be "successful" in the sense of decisively confirmation of the researcher's original hypothesis.

Edward Leamer notes that "The solution to the weak evidence problem is more and better data. Within the confines of the given data set there is nothing that can be done about weak evidence". Leamer notes that "bad" regression results that are often misattributed to multicollinearity instead indicate the researcher has chosen an unrealistic prior probability (generally the flat prior used in OLS).

Damodar Gujarati writes that "we should rightly accept [our data] are sometimes not very informative about parameters of interest". Olivier Blanchard quips that "multicollinearity is God's will, not a problem with OLS"; in other words, when working with observational data, researchers cannot "fix" multicollinearity, only accept it.

## Misuse

Variance inflation factors are often misused as criteria in stepwise regression (i.e. for variable inclusion/exclusion), a use that "lacks any logical basis but also is fundamentally misleading as a rule-of-thumb".

Excluding collinear variables leads to artificially small estimates for standard errors, but does not reduce the true (not estimated) standard errors for regression coefficients. Excluding variables with a high variance inflation factor also invalidates the calculated standard errors and p-values, by turning the results of the regression into a post hoc analysis.

Because collinearity leads to large standard errors and p-values, which can make publishing articles more difficult, some researchers will try to suppress inconvenient data by removing strongly-correlated variables from their regression. This procedure falls into the broader categories of p-hacking, data dredging, and post hoc analysis. Dropping (useful) collinear predictors will generally worsen the accuracy of the model and coefficient estimates.

Similarly, trying many different models or estimation procedures (e.g. ordinary least squares, ridge regression, etc.) until finding one that can "deal with" the collinearity creates a forking paths problem. P-values and confidence intervals derived from post hoc analyses are invalidated by ignoring the uncertainty in the model selection procedure.

It is reasonable to exclude unimportant predictors if they are known ahead of time to have little or no effect on the outcome; for example, local cheese production should not be used to predict the height of skyscrapers. However, this must be done when first specifying the model, prior to observing any data, and potentially-informative variables should always be included.

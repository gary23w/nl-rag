---
title: "Least squares"
source: https://en.wikipedia.org/wiki/Least_squares
domain: signal-estimation
license: CC-BY-SA-4.0
tags: estimation theory, kalman filter, maximum likelihood estimation, particle filter
fetched: 2026-07-02
---

# Least squares

In regression analysis, **least squares** is a method to determine the best-fit model by minimizing the sum of the squared residuals—the differences between observed values and the values predicted by the model.

Least squares problems fall into two categories: linear or ordinary least squares and nonlinear least squares, depending on whether or not the model functions are linear in all unknowns. The linear least-squares problem occurs in statistical regression analysis; it has a closed-form solution. The nonlinear problem is usually solved by iterative refinement; at each iteration the system is approximated by a linear one, and thus the core calculation is similar in both cases.

Polynomial least squares describes the variance in a prediction of the dependent variable as a function of the independent variable and the deviations from the fitted curve.

When the observations come from an exponential family with identity as its natural sufficient statistics and mild-conditions are satisfied (e.g. for normal, exponential, Poisson and binomial distributions), standardized least-squares estimates and maximum-likelihood estimates are identical. The method of least squares can also be derived as a method of moments estimator.

## History

The method was the culmination of several advances that took place during the course of the eighteenth century:

- The combination of different observations as being the best estimate of the true value; errors decrease with aggregation rather than increase, first appeared in Isaac Newton's work in 1671, though it went unpublished, and again in 1700. It was perhaps first expressed formally by Roger Cotes in 1722.
- The combination of different observations taken under the *same* conditions contrary to simply trying one's best to observe and record a single observation accurately. The approach was known as the method of averages. This approach was notably used by Newton while studying equinoxes in 1700, also writing down the first of the 'normal equations' known from ordinary least squares, Tobias Mayer while studying the librations of the Moon in 1750, and by Pierre-Simon Laplace in his work in explaining the differences in motion of Jupiter and Saturn in 1788.
- The combination of different observations taken under *different* conditions. The method came to be known as the method of *least absolute deviation*. It was notably performed by Roger Joseph Boscovich in his work on the shape of the Earth in 1757 and by Pierre-Simon Laplace for the same problem in 1789 and 1799.
- The development of a criterion that can be evaluated to determine when the solution with the minimum error has been achieved. Laplace tried to specify a mathematical form of the probability density for the errors and define a method of estimation that minimizes the error of estimation. For this purpose, Laplace used a symmetric two-sided exponential distribution we now call Laplace distribution to model the error distribution, and used the sum of absolute deviation as error of estimation. He felt these to be the simplest assumptions he could make, and he had hoped to obtain the arithmetic mean as the best estimate. Instead, his estimator was the posterior median.

### The method

The first clear and concise exposition of the method of least squares was published by Legendre in 1805. The technique is described as an algebraic procedure for fitting linear equations to data and Legendre demonstrates the new method by analyzing the same data as Laplace for the shape of the Earth. Within ten years after Legendre's publication, the method of least squares had been adopted as a standard tool in astronomy and geodesy in France, Italy, and Prussia, which constitutes an extraordinarily rapid acceptance of a scientific technique.

In 1809 Carl Friedrich Gauss published his method of calculating the orbits of celestial bodies. In that work he claimed to have been in possession of the method of least squares since 1795. This naturally led to a priority dispute with Legendre. However, to Gauss's credit, he went beyond Legendre and succeeded in connecting the method of least squares with the principles of probability and to the normal distribution. He had managed to complete Laplace's program of specifying a mathematical form of the probability density for the observations, depending on a finite number of unknown parameters, and define a method of estimation that minimizes the error of estimation. Gauss showed that the arithmetic mean is indeed the best estimate of the location parameter by changing both the probability density and the method of estimation. He then turned the problem around by asking what form the density should have and what method of estimation should be used to get the arithmetic mean as estimate of the location parameter. In this attempt, he invented the normal distribution.

An early demonstration of the strength of Gauss's method came when it was used to predict the future location of the newly discovered asteroid Ceres. On 1 January 1801, the Italian astronomer Giuseppe Piazzi discovered Ceres and was able to track its path for 40 days before it was lost in the glare of the Sun. Based on these data, astronomers desired to determine the location of Ceres after it emerged from behind the Sun without solving Kepler's complicated nonlinear equations of planetary motion. The only predictions that successfully allowed Hungarian astronomer Franz Xaver von Zach to relocate Ceres were those performed by the 24-year-old Gauss using least-squares analysis.

In 1810, after reading Gauss's work, Laplace, after proving the central limit theorem, used it to give a large sample justification for the method of least squares and the normal distribution. In 1822, Gauss was able to state that the least-squares approach to regression analysis is optimal in the sense that in a linear model where the errors have a mean of zero, are uncorrelated, normally distributed, and have equal variances, the best linear unbiased estimator of the coefficients is the least-squares estimator. An extended version of this result is known as the Gauss–Markov theorem.

The idea of least-squares analysis was also independently formulated by the American Robert Adrain in 1808. In the next two centuries workers in the theory of errors and in statistics found many different ways of implementing least squares.

## Problem statement

The objective consists of adjusting the parameters of a model function to best fit a data set. A simple data set consists of *n* points (data pairs) $(x_{i},y_{i})\!$ , *i* = 1, …, *n*, where $x_{i}\!$ is an independent variable and $y_{i}\!$ is a dependent variable whose value is found by observation. The model function has the form $f(x,{\boldsymbol {\beta }})$ , where *m* adjustable parameters are held in the vector ${\boldsymbol {\beta }}$ . The goal is to find the parameter values for the model that "best" fits the data. The fit of a model to a data point is measured by its residual, defined as the difference between the observed value of the dependent variable and the value predicted by the model: $r_{i}=y_{i}-f(x_{i},{\boldsymbol {\beta }}).$

The least-squares method finds the optimal parameter values by minimizing the sum of squared residuals, S : $S=\sum _{i=1}^{n}r_{i}^{2}.$

In the simplest case, $f(x_{i},{\boldsymbol {\beta }})={\boldsymbol {\beta }}$ and the result of the least-squares method is the arithmetic mean of the input data.

An example of a model in two dimensions is that of the straight line. Denoting the y-intercept as $\beta _{0}$ and the slope as $\beta _{1}$ , the model function is given by $f(x,{\boldsymbol {\beta }})=\beta _{0}+\beta _{1}x$ . See linear least squares for a fully worked out example of this model.

A data point may consist of more than one independent variable. For example, when fitting a plane to a set of height measurements, the plane is a function of two independent variables, *x* and *z*, say. In the most general case there may be one or more independent variables and one or more dependent variables at each data point.

To the right is a residual plot illustrating random fluctuations about $r_{i}=0$ , indicating that a linear model $(Y_{i}=\beta _{0}+\beta _{1}x_{i}+U_{i})$ is appropriate. $U_{i}$ is an independent, random variable.

If the residual points had some sort of a shape and were not randomly fluctuating, a linear model would not be appropriate. For example, if the residual plot had a parabolic shape as seen to the right, a parabolic model $(Y_{i}=\beta _{0}+\beta _{1}x_{i}+\beta _{2}x_{i}^{2}+U_{i})$ would be appropriate for the data. The residuals for a parabolic model can be calculated via $r_{i}=y_{i}-{\hat {\beta }}_{0}-{\hat {\beta }}_{1}x_{i}-{\hat {\beta }}_{2}x_{i}^{2}$ .

## Limitations

This regression formulation considers only observational errors in the dependent variable (but the alternative total least squares regression can account for errors in both variables). There are two rather different contexts with different implications:

- Regression for prediction. Here a model is fitted to provide a prediction rule for application in a similar situation to which the data used for fitting apply. Here the dependent variables corresponding to such future application would be subject to the same types of observation error as those in the data used for fitting. It is therefore logically consistent to use the least-squares prediction rule for such data.
- Regression for fitting a "true relationship". In standard regression analysis that leads to fitting by least squares there is an implicit assumption that errors in the independent variable are zero or strictly controlled so as to be negligible. When errors in the independent variable are non-negligible, models of measurement error can be used; such methods can lead to parameter estimates, hypothesis testing and confidence intervals that take into account the presence of observation errors in the independent variables. An alternative approach is to fit a model by total least squares; this can be viewed as taking a pragmatic approach to balancing the effects of the different sources of error in formulating an objective function for use in model-fitting.

## Solving the least squares problem

The minimum of the sum of squares is found by setting the gradient to zero. Since the model contains *m* parameters, there are *m* gradient equations: ${\frac {\partial S}{\partial \beta _{j}}}=2\sum _{i}r_{i}{\frac {\partial r_{i}}{\partial \beta _{j}}}=0,\ j=1,\ldots ,m,$ and since $r_{i}=y_{i}-f(x_{i},{\boldsymbol {\beta }})$ , the gradient equations become $-2\sum _{i}r_{i}{\frac {\partial f(x_{i},{\boldsymbol {\beta }})}{\partial \beta _{j}}}=0,\ j=1,\ldots ,m.$

The gradient equations apply to all least squares problems. Each particular problem requires particular expressions for the model and its partial derivatives.

### Linear least squares

A regression model is a linear one when the model comprises a linear combination of the parameters, i.e., $f(x,{\boldsymbol {\beta }})=\sum _{j=1}^{m}\beta _{j}\phi _{j}(x),$ where the function $\phi _{j}$ is a function of x .

Letting $X_{ij}=\phi _{j}(x_{i})$ and putting the independent and dependent variables in matrices X and $Y,$ respectively, we can compute the least squares in the following way. Note that D is the set of all data. $L(D,{\boldsymbol {\beta }})=\left\|Y-X{\boldsymbol {\beta }}\right\|^{2}=(Y-X{\boldsymbol {\beta }})^{\mathsf {T}}(Y-X{\boldsymbol {\beta }})$ $=Y^{\mathsf {T}}Y-2Y^{\mathsf {T}}X{\boldsymbol {\beta }}+{\boldsymbol {\beta }}^{\mathsf {T}}X^{\mathsf {T}}X{\boldsymbol {\beta }}$

The gradient of the loss is: ${\frac {\partial L(D,{\boldsymbol {\beta }})}{\partial {\boldsymbol {\beta }}}}={\frac {\partial \left(Y^{\mathsf {T}}Y-2Y^{\mathsf {T}}X{\boldsymbol {\beta }}+{\boldsymbol {\beta }}^{\mathsf {T}}X^{\mathsf {T}}X{\boldsymbol {\beta }}\right)}{\partial {\boldsymbol {\beta }}}}=-2X^{\mathsf {T}}Y+2X^{\mathsf {T}}X{\boldsymbol {\beta }}$

Setting the gradient of the loss to zero and solving for ${\boldsymbol {\beta }}$ , we get: $-2X^{\mathsf {T}}Y+2X^{\mathsf {T}}X{\boldsymbol {\beta }}=0\Rightarrow X^{\mathsf {T}}Y=X^{\mathsf {T}}X{\boldsymbol {\beta }}$ ${\boldsymbol {\hat {\beta }}}=\left(X^{\mathsf {T}}X\right)^{-1}X^{\mathsf {T}}Y$

### Non-linear least squares

There is, in some cases, a closed-form solution to a non-linear least squares problem – but in general there is not. In the case of no closed-form solution, numerical algorithms are used to find the value of the parameters $\beta$ that minimizes the objective. Most algorithms involve choosing initial values for the parameters. Then, the parameters are refined iteratively, that is, the values are obtained by successive approximation: ${\beta _{j}}^{k+1}={\beta _{j}}^{k}+\Delta \beta _{j},$ where a superscript *k* is an iteration number, and the vector of increments $\Delta \beta _{j}$ is called the shift vector. In some commonly used algorithms, at each iteration the model may be linearized by approximation to a first-order Taylor series expansion about ${\boldsymbol {\beta }}^{k}$ : ${\begin{aligned}f(x_{i},{\boldsymbol {\beta }})&=f^{k}(x_{i},{\boldsymbol {\beta }})+\sum _{j}{\frac {\partial f(x_{i},{\boldsymbol {\beta }})}{\partial \beta _{j}}}\left(\beta _{j}-{\beta _{j}}^{k}\right)\\[1ex]&=f^{k}(x_{i},{\boldsymbol {\beta }})+\sum _{j}J_{ij}\,\Delta \beta _{j}.\end{aligned}}$

The Jacobian **J** is a function of constants, the independent variable *and* the parameters, so it changes from one iteration to the next. The residuals are given by $r_{i}=y_{i}-f^{k}(x_{i},{\boldsymbol {\beta }})-\sum _{k=1}^{m}J_{ik}\,\Delta \beta _{k}=\Delta y_{i}-\sum _{j=1}^{m}J_{ij}\,\Delta \beta _{j}.$

To minimize the sum of squares of $r_{i}$ , the gradient equation is set to zero and solved for $\Delta \beta _{j}$ : $-2\sum _{i=1}^{n}J_{ij}\left(\Delta y_{i}-\sum _{k=1}^{m}J_{ik}\,\Delta \beta _{k}\right)=0,$ which, on rearrangement, become *m* simultaneous linear equations, the **normal equations**: $\sum _{i=1}^{n}\sum _{k=1}^{m}J_{ij}J_{ik}\,\Delta \beta _{k}=\sum _{i=1}^{n}J_{ij}\,\Delta y_{i}\qquad (j=1,\ldots ,m).$

The normal equations are written in matrix notation as $\left(\mathbf {J} ^{\mathsf {T}}\mathbf {J} \right)\Delta {\boldsymbol {\beta }}=\mathbf {J} ^{\mathsf {T}}\Delta \mathbf {y} .$

These are the defining equations of the Gauss–Newton algorithm.

### Differences between linear and nonlinear least squares

- The model function, *f*, in LLSQ (linear least squares) is a linear combination of parameters of the form $f=X_{i1}\beta _{1}+X_{i2}\beta _{2}+\cdots$ The model may represent a straight line, a parabola or any other linear combination of functions. In NLLSQ (nonlinear least squares) the parameters appear as functions, such as $\beta ^{2},e^{\beta x}$ and so forth. If the derivatives $\partial f/\partial \beta _{j}$ are either constant or depend only on the values of the independent variable, the model is linear in the parameters. Otherwise, the model is nonlinear.
- Need initial values for the parameters to find the solution to a NLLSQ problem; LLSQ does not require them.
- Solution algorithms for NLLSQ often require that the Jacobian can be calculated similar to LLSQ. Analytical expressions for the partial derivatives can be complicated. If analytical expressions are impossible to obtain either the partial derivatives must be calculated by numerical approximation or an estimate must be made of the Jacobian, often via finite differences.
- Non-convergence (failure of the algorithm to find a minimum) is a common phenomenon in NLLSQ.
- LLSQ is globally concave so non-convergence is not an issue.
- Solving NLLSQ is usually an iterative process which has to be terminated when a convergence criterion is satisfied. LLSQ solutions can be computed using direct methods, although problems with large numbers of parameters are typically solved with iterative methods, such as the Gauss–Seidel method.
- In LLSQ the solution is unique, but in NLLSQ there may be multiple minima in the sum of squares.
- Under the condition that the errors are uncorrelated with the predictor variables, LLSQ yields unbiased estimates, but even under that condition NLLSQ estimates are generally biased.

These differences must be considered whenever the solution to a nonlinear least squares problem is being sought.

## Example

Consider a simple example drawn from physics. A spring should obey Hooke's law which states that the extension of a spring y is proportional to the force, *F*, applied to it. $y=f(F,k)=kF$ constitutes the model, where *F* is the independent variable. In order to estimate the force constant, *k*, we conduct a series of *n* measurements with different forces to produce a set of data, $(F_{i},y_{i}),\ i=1,\dots ,n\!$ , where *yi* is a measured spring extension. Each experimental observation will contain some error, $\varepsilon$ , and so we may specify an empirical model for our observations, $y_{i}=kF_{i}+\varepsilon _{i}.$

There are many methods we might use to estimate the unknown parameter *k*. Since the *n* equations in the *m* variables in our data comprise an overdetermined system with one unknown and *n* equations, we estimate *k* using least squares. The sum of squares to be minimized is $S=\sum _{i=1}^{n}\left(y_{i}-kF_{i}\right)^{2}.$

The least squares estimate of the force constant, *k*, is given by ${\hat {k}}={\frac {\sum _{i}F_{i}y_{i}}{\sum _{i}F_{i}^{2}}}.$

We assume that applying force *causes* the spring to expand. After having derived the force constant by least squares fitting, we predict the extension from Hooke's law.

## Uncertainty quantification

In a least squares calculation with unit weights, or in linear regression, the variance on the *j*th parameter, denoted $\operatorname {var} ({\hat {\beta }}_{j})$ , is usually estimated with $\operatorname {var} ({\hat {\beta }}_{j})=\sigma ^{2}\left(\left[X^{\mathsf {T}}X\right]^{-1}\right)_{jj}\approx {\hat {\sigma }}^{2}C_{jj},$ ${\hat {\sigma }}^{2}\approx {\frac {S}{n-m}}$ $C=\left(X^{\mathsf {T}}X\right)^{-1},$ where the true error variance *σ*2 is replaced by an estimate, the reduced chi-squared statistic, based on the minimized value of the residual sum of squares (objective function), *S*. The denominator, *n* − *m*, is the statistical degrees of freedom; see effective degrees of freedom for generalizations. *C* is the covariance matrix.

## Statistical testing

If the probability distribution of the parameters is known or an asymptotic approximation is made, confidence limits can be found. Similarly, statistical tests on the residuals can be conducted if the probability distribution of the residuals is known or assumed. We can derive the probability distribution of any linear combination of the dependent variables if the probability distribution of experimental errors is known or assumed. Inferring is easy when assuming that the errors follow a normal distribution, consequently implying that the parameter estimates and residuals will also be normally distributed conditional on the values of the independent variables.

It is necessary to make assumptions about the nature of the experimental errors to test the results statistically. A common assumption is that the errors belong to a normal distribution. The central limit theorem supports the idea that this is a good approximation in many cases.

- The Gauss–Markov theorem. In a linear model in which the errors have expectation zero conditional on the independent variables, are uncorrelated and have equal variances, the best linear unbiased estimator of any linear combination of the observations, is its least-squares estimator. "Best" means that the least squares estimators of the parameters have minimum variance. The assumption of equal variance is valid when the errors all belong to the same distribution.
- If the errors belong to a normal distribution, the least-squares estimators are also the maximum likelihood estimators in a linear model.

However, suppose the errors are not normally distributed. In that case, a central limit theorem often nonetheless implies that the parameter estimates will be approximately normally distributed so long as the sample is reasonably large. For this reason, given the important property that the error mean is independent of the independent variables, the distribution of the error term is not an important issue in regression analysis. Specifically, it is not typically important whether the error term follows a normal distribution.

## Weighted least squares

A special case of generalized least squares called **weighted least squares** occurs when all the off-diagonal entries of Ω (the correlation matrix of the residuals) are null; the variances of the observations (along the covariance matrix diagonal) may still be unequal (heteroscedasticity). In simpler terms, heteroscedasticity is when the variance of $Y_{i}$ depends on the value of $x_{i}$ which causes the residual plot to create a "fanning out" effect towards larger or smaller $Y_{i}$ values as seen in the residual plot to the right. On the other hand, homoscedasticity is assuming that the variance of $Y_{i}$ and variance of $U_{i}$ are equal.

## Relationship to principal components

The first principal component about the mean of a set of points can be represented by that line which most closely approaches the data points (as measured by squared distance of closest approach, i.e. perpendicular to the line). In contrast, linear least squares tries to minimize the distance in the y direction only. Thus, although the two use a similar error metric, linear least squares is a method that treats one dimension of the data preferentially, while PCA treats all dimensions equally.

## Relationship to measure theory

Notable statistician Sara van de Geer used empirical process theory and the Vapnik–Chervonenkis dimension to prove a least-squares estimator can be interpreted as a measure on the space of square-integrable functions.

## Regularization

### Tikhonov regularization

In some contexts, a regularized version of the least squares solution may be preferable. Tikhonov regularization (or ridge regression) adds a constraint that $\left\|\beta \right\|_{2}^{2}$ , the squared $\ell _{2}$ -norm of the parameter vector, is not greater than a given value to the least squares formulation, leading to a constrained minimization problem. This is equivalent to the unconstrained minimization problem where the objective function is the residual sum of squares plus a penalty term $\alpha \left\|\beta \right\|_{2}^{2}$ and $\alpha$ is a tuning parameter (this is the Lagrangian form of the constrained minimization problem).

In a Bayesian context, this is equivalent to placing a zero-mean normally distributed prior on the parameter vector.

### Lasso method

An alternative regularized version of least squares is Lasso (least absolute shrinkage and selection operator), which uses the constraint that $\|\beta \|_{1}$ , the L1-norm of the parameter vector, is no greater than a given value. (One can show like above using Lagrange multipliers that this is equivalent to an unconstrained minimization of the least-squares penalty with $\alpha \|\beta \|_{1}$ added.) In a Bayesian context, this is equivalent to placing a zero-mean Laplace prior distribution on the parameter vector. The optimization problem may be solved using quadratic programming or more general convex optimization methods, as well as by specific algorithms such as the least angle regression algorithm.

One of the prime differences between Lasso and ridge regression is that in ridge regression, as the penalty is increased, all parameters are reduced while still remaining non-zero, while in Lasso, increasing the penalty will cause more and more of the parameters to be driven to zero. This is an advantage of Lasso over ridge regression, as driving parameters to zero deselects the features from the regression. Thus, Lasso automatically selects more relevant features and discards the others, whereas Ridge regression never fully discards any features. Some feature selection techniques are developed based on the LASSO including Bolasso which bootstraps samples, and FeaLect which analyzes the regression coefficients corresponding to different values of $\alpha$ to score all the features.

The *L*1-regularized formulation is useful in some contexts due to its tendency to prefer solutions where more parameters are zero, which gives solutions that depend on fewer variables. For this reason, the Lasso and its variants are fundamental to the field of compressed sensing. An extension of this approach is elastic net regularization.

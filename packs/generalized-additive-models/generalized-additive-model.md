---
title: "Generalized additive model"
source: https://en.wikipedia.org/wiki/Generalized_additive_model
domain: generalized-additive-models
license: CC-BY-SA-4.0
tags: generalized additive model, backfitting, smoothing spline, kernel smoother
fetched: 2026-07-02
---

# Generalized additive model

In statistics, a **generalized additive model** (**GAM**) is a generalized linear model in which the linear response variable depends linearly on unknown smooth functions of some predictor variables, and interest focuses on inference about these smooth functions.

GAMs were originally developed by Trevor Hastie and Robert Tibshirani to blend properties of generalized linear models with additive models. They can be interpreted as the discriminative generalization of the naive Bayes generative model.

The model relates a univariate response variable, *Y*, to some predictor variables, *x**i*. An exponential family distribution is specified for Y (for example normal, binomial or Poisson distributions) along with a link function *g* (for example the identity or log functions) relating the expected value of *Y* to the predictor variables via a structure such as

$g(\operatorname {E} (Y))=\beta _{0}+f_{1}(x_{1})+f_{2}(x_{2})+\cdots +f_{m}(x_{m}).\,\!$

The functions *f**i* may be functions with a specified parametric form (for example a polynomial, or an un-penalized regression spline of a variable) or may be specified non-parametrically, or semi-parametrically, simply as 'smooth functions', to be estimated by non-parametric means. So a typical GAM might use a scatterplot smoothing function, such as a locally weighted mean, for *f*1(*x*1), and then use a factor model for *f*2(*x*2). This flexibility to allow non-parametric fits with relaxed assumptions on the actual relationship between response and predictor, provides the potential for better fits to data than purely parametric models, but arguably with some loss of interpretability.

## Theoretical background

It had been known since the 1950s (via the Kolmogorov–Arnold representation theorem) that any multivariate continuous function could be represented as sums and compositions of univariate functions,

$f({\vec {x}})=\sum _{q=0}^{2n}\Phi _{q}\left(\sum _{p=1}^{n}\phi _{q,p}(x_{p})\right)$

.

Unfortunately, though the Kolmogorov–Arnold representation theorem asserts the existence of a function of this form, it gives no mechanism whereby one could be constructed. Certain constructive proofs exist, but they tend to require highly complicated (i.e. fractal) functions, and thus are not suitable for modeling approaches. Therefore, the generalized additive model drops the outer sum, and demands instead that the function belong to a simpler class,

$f({\vec {x}})=\Phi \left(\sum _{p=1}^{n}\phi _{p}(x_{p})\right)$

.

where $\Phi$ is a smooth monotonic function. Writing g for the inverse of $\Phi$ , this is traditionally written as

$g(f({\vec {x}}))=\sum _{i}f_{i}(x_{i})$

.

When this function is approximating the expectation of some observed quantity, it could be written as

$g(\operatorname {E} (Y))=\beta _{0}+f_{1}(x_{1})+f_{2}(x_{2})+\cdots +f_{m}(x_{m}).\,\!$

Which is the standard formulation of a generalized additive model. It was then shown that the backfitting algorithm will always converge for these functions.

## Generality

The GAM model class is quite broad, given that *smooth function* is a rather broad category. For example, a covariate $x_{j}$ may be multivariate and the corresponding $f_{j}$ a smooth function of several variables, or $f_{j}$ might be the function mapping the level of a factor to the value of a random effect. Another example is a varying coefficient (geographic regression) term such as $z_{j}f_{j}(x_{j})$ where $z_{j}$ and $x_{j}$ are both covariates. Or if $x_{j}(t)$ is itself an observation of a function, we might include a term such as $\int f_{j}(t)x_{j}(t)dt$ (sometimes known as a signal regression term). $f_{j}$ could also be a simple parametric function as might be used in any generalized linear model. The model class has been generalized in several directions, notably beyond exponential family response distributions, beyond modelling of only the mean and beyond univariate data.

## GAM fitting methods

The original GAM fitting method estimated the smooth components of the model using non-parametric smoothers (for example smoothing splines or local linear regression smoothers) via the backfitting algorithm. Backfitting works by iterative smoothing of partial residuals and provides a very general modular estimation method capable of using a wide variety of smoothing methods to estimate the $f_{j}(x_{j})$ terms. A disadvantage of backfitting is that it is difficult to integrate with the estimation of the degree of smoothness of the model terms, so that in practice the user must set these, or select between a modest set of pre-defined smoothing levels.

If the $f_{j}(x_{j})$ are represented using smoothing splines then the degree of smoothness can be estimated as part of model fitting using generalized cross validation, or by restricted maximum likelihood (REML, sometimes known as 'GML') which exploits the duality between spline smoothers and Gaussian random effects. This full spline approach carries an $O(n^{3})$ computational cost, where n is the number of observations for the response variable, rendering it somewhat impractical for moderately large datasets. More recent methods have addressed this computational cost either by up front reduction of the size of the basis used for smoothing (rank reduction) or by finding sparse representations of the smooths using Markov random fields, which are amenable to the use of sparse matrix methods for computation. These more computationally efficient methods use GCV (or AIC or similar) or REML or take a fully Bayesian approach for inference about the degree of smoothness of the model components. Estimating the degree of smoothness via REML can be viewed as an empirical Bayes method.

An alternative approach with particular advantages in high dimensional settings is to use boosting, although this typically requires bootstrapping for uncertainty quantification. GAMs fit using bagging and boosting have been found to generally outperform GAMs fit using spline methods.

## The rank reduced framework

Many modern implementations of GAMs and their extensions are built around the reduced rank smoothing approach, because it allows well founded estimation of the smoothness of the component smooths at comparatively modest computational cost, and also facilitates implementation of a number of model extensions in a way that is more difficult with other methods. At its simplest the idea is to replace the unknown smooth functions in the model with basis expansions

$f_{j}(x_{j})=\sum _{k=1}^{K_{j}}\beta _{jk}b_{jk}(x_{j})$

where the $b_{jk}(x_{j})$ are known basis functions, usually chosen for good approximation theoretic properties (for example B splines or reduced rank thin plate splines), and the $\beta _{jk}$ are coefficients to be estimated as part of model fitting. The basis dimension $K_{j}$ is chosen to be sufficiently large that we expect it to overfit the data to hand (thereby avoiding bias from model over-simplification), but small enough to retain computational efficiency. If $p=\sum _{j}K_{j}$ then the computational cost of model estimation this way will be $O(np^{2})$ .

Notice that the $f_{j}$ are only identifiable to within an intercept term (we could add any constant to $f_{1}$ while subtracting it from $f_{2}$ without changing the model predictions at all), so identifiability constraints have to be imposed on the smooth terms to remove this ambiguity. Sharpest inference about the $f_{j}$ is generally obtained by using the sum-to-zero constraints

$\sum _{i}f_{j}(x_{ji})=0$

i.e. by insisting that the sum of each the $f_{j}$ evaluated at its observed covariate values should be zero. Such linear constraints can most easily be imposed by reparametrization at the basis setup stage, so below it is assumed that this has been done.

Having replaced all the $f_{j}$ in the model with such basis expansions we have turned the GAM into a generalized linear model (GLM), with a model matrix that simply contains the basis functions evaluated at the observed $x_{j}$ values. However, because the basis dimensions, $K_{j}$ , have been chosen to be a somewhat larger than is believed to be necessary for the data, the model is over-parameterized and will overfit the data if estimated as a regular GLM. The solution to this problem is to penalize departure from smoothness in the model fitting process, controlling the weight given to the smoothing penalties using smoothing parameters. For example, consider the situation in which all the smooths are univariate functions. Writing all the parameters in one vector, $\beta$ , suppose that $D(\beta )$ is the deviance (twice the difference between saturated log likelihood and the model log likelihood) for the model. Minimizing the deviance by the usual iteratively re-weighted least squares would result in overfit, so we seek $\beta$ to minimize

$D(\beta )+\sum _{j}\lambda _{j}\int f_{j}^{\prime \prime }(x)^{2}dx$

where the integrated square second derivative penalties serve to penalize wiggliness (lack of smoothness) of the $f_{j}$ during fitting, and the smoothing parameters $\lambda _{j}$ control the tradeoff between model goodness of fit and model smoothness. In the example $\lambda _{j}\to \infty$ would ensure that the estimate of $f_{j}(x_{j})$ would be a straight line in $x_{j}$ .

Given the basis expansion for each $f_{j}$ the wiggliness penalties can be expressed as quadratic forms in the model coefficients. That is we can write

$\int f_{j}^{\prime \prime }(x)^{2}dx=\beta _{j}^{T}{\bar {S}}_{j}\beta _{j}=\beta ^{T}S_{j}\beta$

,

where ${\bar {S}}_{j}$ is a matrix of known coefficients computable from the penalty and basis, $\beta _{j}$ is the vector of coefficients for $f_{j}$ , and $S_{j}$ is just ${\bar {S}}_{j}$ padded with zeros so that the second equality holds and we can write the penalty in terms of the full coefficient vector $\beta$ . Many other smoothing penalties can be written in the same way, and given the smoothing parameters the model fitting problem now becomes

${\hat {\beta }}={\text{argmin}}_{\beta }\{D(\beta )+\sum _{j}\lambda _{j}\beta ^{T}S_{j}\beta \}$

,

which can be found using a penalized version of the usual iteratively reweighted least squares (IRLS) algorithm for GLMs: the algorithm is unchanged except that the sum of quadratic penalties is added to the working least squared objective at each iteration of the algorithm.

Penalization has several effects on inference, relative to a regular GLM. For one thing the estimates are subject to some smoothing bias, which is the price that must be paid for limiting estimator variance by penalization. However, if smoothing parameters are selected appropriately the (squared) smoothing bias introduced by penalization should be less than the reduction in variance that it produces, so that the net effect is a reduction in mean square estimation error, relative to not penalizing. A related effect of penalization is that the notion of degrees of freedom of a model has to be modified to account for the penalties' action in reducing the coefficients' freedom to vary. For example, if W is the diagonal matrix of IRLS weights at convergence, and X is the GAM model matrix, then the model effective degrees of freedom is given by ${\text{trace}}(F)$ where

$F=(X^{T}WX+\sum _{j}\lambda _{j}S_{j})^{-1}X^{T}WX$

,

is the effective degrees of freedom matrix. In fact summing just the diagonal elements of F corresponding to the coefficients of $f_{j}$ gives the effective degrees of freedom for the estimate of $f_{j}$ .

### Bayesian smoothing priors

Smoothing bias complicates interval estimation for these models, and the simplest approach turns out to involve a Bayesian approach. Understanding this Bayesian view of smoothing also helps to understand the REML and full Bayes approaches to smoothing parameter estimation. At some level smoothing penalties are imposed because we believe smooth functions to be more probable than wiggly ones, and if that is true then we might as well formalize this notion by placing a prior on model wiggliness. A very simple prior might be

$\pi (\beta )\propto \exp\{-\beta ^{T}\sum _{j}\lambda _{j}S_{j}\beta /(2\phi )\}$

(where $\phi$ is the GLM scale parameter introduced only for later convenience), but we can immediately recognize this as a multivariate normal prior with mean 0 and precision matrix $S_{\lambda }=\sum _{j}\lambda _{j}S_{j}/\phi$ . Since the penalty allows some functions through unpenalized (straight lines, given the example penalties), $S_{\lambda }$ is rank deficient, and the prior is actually improper, with a covariance matrix given by the Moore–Penrose pseudoinverse of $S_{\lambda }$ (the impropriety corresponds to ascribing infinite variance to the unpenalized components of a smooth).

Now if this prior is combined with the GLM likelihood, we find that the posterior mode for $\beta$ is exactly the ${\hat {\beta }}$ found above by penalized IRLS. Furthermore, we have the large sample result that

$\beta |y\sim N({\hat {\beta }},(X^{T}WX+S_{\lambda })^{-1}\phi ).$

which can be used to produce confidence/credible intervals for the smooth components, $f_{j}$ . The Gaussian smoothness priors are also the basis for fully Bayesian inference with GAMs, as well as methods estimating GAMs as mixed models that are essentially empirical Bayes methods.

### Smoothing parameter estimation

So far we have treated estimation and inference given the smoothing parameters, $\lambda$ , but these also need to be estimated. One approach is to take a fully Bayesian approach, defining priors on the (log) smoothing parameters, and using stochastic simulation or high order approximation methods to obtain information about the posterior of the model coefficients. An alternative is to select the smoothing parameters to optimize a prediction error criterion such as Generalized cross validation (GCV) or the Akaike information criterion (AIC). Finally we may choose to maximize the Marginal Likelihood (REML) obtained by integrating the model coefficients, $\beta$ out of the joint density of $\beta ,y$ ,

${\hat {\lambda }}={\text{argmax}}_{\lambda }\int f(y|\beta ,\lambda )\pi (\beta |\lambda )d\beta$

.

Since $f(y|\beta ,\lambda )$ is just the likelihood of $\beta$ , we can view this as choosing $\lambda$ to maximize the average likelihood of random draws from the prior. The preceding integral is usually analytically intractable but can be approximated to quite high accuracy using Laplace's method.

Smoothing parameter inference is the most computationally taxing part of model estimation/inference. For example, to optimize a GCV or marginal likelihood typically requires numerical optimization via a Newton or Quasi-Newton method, with each trial value for the (log) smoothing parameter vector requiring a penalized IRLS iteration to evaluate the corresponding ${\hat {\beta }}$ alongside the other ingredients of the GCV score or Laplace approximate marginal likelihood (LAML). Furthermore, to obtain the derivatives of the GCV or LAML, required for optimization, involves implicit differentiation to obtain the derivatives of ${\hat {\beta }}$ w.r.t. the log smoothing parameters, and this requires some care is efficiency and numerical stability are to be maintained.

## Software

Backfit GAMs were originally provided by the `gam` function in S, now ported to the R language as the `gam` package. The SAS proc `GAM` also provides backfit GAMs. The recommended package in R for GAMs is `mgcv`, which stands for *mixed GAM computational vehicle*, which is based on the reduced rank approach with automatic smoothing parameter selection. The SAS proc `GAMPL` is an alternative implementation. In Python, there is the PyGAM package, with similar features to R's mgcv. Alternatively, there is `InterpretML` package, which implements a bagging and boosting approach. There are many alternative packages. Examples include the R packages `mboost`, which implements a boosting approach; `gss`, which provides the full spline smoothing methods; `VGAM` which provides vector GAMs; and `gamlss`, which provides Generalized additive model for location, scale and shape. `BayesX` and its R interface provides GAMs and extensions via MCMC and penalized likelihood methods. The `INLA` software implements a fully Bayesian approach based on Markov random field representations exploiting sparse matrix methods.

As an example of how models can be estimated in practice with software, consider R package `mgcv`. Suppose that our R workspace contains vectors *y*, *x* and *z* and we want to estimate the model

$y_{i}=\beta _{0}+f_{1}(x_{i})+f_{2}(z_{i})+\epsilon _{i}{\text{ where }}\epsilon _{i}\sim N(0,\sigma ^{2}).$

Within R we could issue the commands

```
library(mgcv)  # load the package
b = gam(y ~ s(x) + s(z))
```

In common with most R modelling functions `gam` expects a model formula to be supplied, specifying the model structure to fit. The response variable is given to the left of the `~` while the specification of the linear predictor is given to the right. `gam` sets up bases and penalties for the smooth terms, estimates the model including its smoothing parameters and, in standard R fashion, returns a *fitted model object*, which can then be interrogated using various helper functions, such as `summary`, `plot`, `predict`, and `AIC`.

This simple example has used several default settings which it is important to be aware of. For example a Gaussian distribution and identity link has been assumed, and the smoothing parameter selection criterion was GCV. Also the smooth terms were represented using `penalized thin plate regression splines', and the basis dimension for each was set to 10 (implying a maximum of 9 degrees of freedom after identifiability constraints have been imposed). A second example illustrates how we can control these things. Suppose that we want to estimate the model

$y_{i}\sim {\text{Poi}}(\mu _{i}){\text{ where }}\log \mu _{i}=\beta _{0}+\beta _{1}x_{i}+f_{1}(t_{i})+f_{2}(v_{i},w_{i}).$

using REML smoothing parameter selection, and we expect $f_{1}$ to be a relatively complicated function which we would like to model with a penalized cubic regression spline. For $f_{2}$ we also have to decide whether v and w are naturally on the same scale so that an isotropic smoother such as thin plate spline is appropriate (specified via `s(v,w)'), or whether they are really on different scales so that we need separate smoothing penalties and smoothing parameters for v and w as provided by a tensor product smoother. Suppose we opted for the latter in this case, then the following R code would estimate the model

```
b1 = gam(y ~ x + s(t,bs="cr",k=100) + te(v,w),family=poisson,method="REML")
```

which uses a basis size of 100 for the smooth of t . The specification of distribution and link function uses the `family' objects that are standard when fitting GLMs in R or S. Note that Gaussian random effects can also be added to the linear predictor.

These examples are only intended to give a very basic flavour of the way that GAM software is used, for more detail refer to the software documentation for the various packages and the references below.

## Model checking

As with any statistical model it is important to check the model assumptions of a GAM. Residual plots should be examined in the same way as for any GLM. That is deviance residuals (or other standardized residuals) should be examined for patterns that might suggest a substantial violation of the independence or mean-variance assumptions of the model. This will usually involve plotting the standardized residuals against fitted values and covariates to look for mean-variance problems or missing pattern, and may also involve examining Correlograms (ACFs) and/or Variograms of the residuals to check for violation of independence. If the model mean-variance relationship is correct then scaled residuals should have roughly constant variance. Note that since GLMs and GAMs can be estimated using Quasi-likelihood, it follows that details of the distribution of the residuals beyond the mean-variance relationship are of relatively minor importance.

One issue that is more common with GAMs than with other GLMs is a danger of falsely concluding that data are zero inflated. The difficulty arises when data contain many zeroes that can be modelled by a Poisson or binomial with a very low expected value: the flexibility of the GAM structure will often allow representation of a very low mean over some region of covariate space, but the distribution of standardized residuals will fail to look anything like the approximate normality that introductory GLM classes teach us to expect, even if the model is perfectly correct.

The one extra check that GAMs introduce is the need to check that the degrees of freedom chosen are appropriate. This is particularly acute when using methods that do not automatically estimate the smoothness of model components. When using methods with automatic smoothing parameter selection then it is still necessary to check that the choice of basis dimension was not restrictively small, although if the effective degrees of freedom of a term estimate is comfortably below its basis dimension then this is unlikely. In any case, checking $f_{j}(x_{j})$ is based on examining pattern in the residuals with respect to $x_{j}$ . This can be done using partial residuals overlaid on the plot of ${\hat {f}}_{j}(x_{j})$ , or using permutation of the residuals to construct tests for residual pattern.

## Model selection

When smoothing parameters are estimated as part of model fitting then much of what would traditionally count as model selection has been absorbed into the fitting process: the smoothing parameters estimation has already selected between a rich family of models of different functional complexity. However smoothing parameter estimation does not typically remove a smooth term from the model altogether, because most penalties leave some functions un-penalized (e.g. straight lines are unpenalized by the spline derivative penalty given above). So the question of whether a term should be in the model at all remains. One simple approach to this issue is to add an extra penalty to each smooth term in the GAM, which penalizes the components of the smooth that would otherwise be unpenalized (and only those). Each extra penalty has its own smoothing parameter and estimation then proceeds as before, but now with the possibility that terms will be completely penalized to zero. In high dimensional settings then it may make more sense to attempt this task using the lasso or elastic net regularization. Boosting also performs term selection automatically as part of fitting.

An alternative is to use traditional stepwise regression methods for model selection. This is also the default method when smoothing parameters are not estimated as part of fitting, in which case each smooth term is usually allowed to take one of a small set of pre-defined smoothness levels within the model, and these are selected between in a stepwise fashion. Stepwise methods operate by iteratively comparing models with or without particular model terms (or possibly with different levels of term complexity), and require measures of model fit or term significance in order to decide which model to select at each stage. For example, we might use p-values for testing each term for equality to zero to decide on candidate terms for removal from a model, and we might compare Akaike information criterion (AIC) values for alternative models.

P-value computation for smooths is not straightforward, because of the effects of penalization, but approximations are available. AIC can be computed in two ways for GAMs. The marginal AIC is based on the Marginal Likelihood (see above) with the model coefficients integrated out. In this case the AIC penalty is based on the number of smoothing parameters (and any variance parameters) in the model. However, because of the well known fact that REML is not comparable between models with different fixed effects structures, we can not usually use such an AIC to compare models with different smooth terms (since their un-penalized components act like fixed effects). Basing AIC on the marginal likelihood in which only the penalized effects are integrated out is possible (the number of un-penalized coefficients now gets added to the parameter count for the AIC penalty), but this version of the marginal likelihood suffers from the tendency to oversmooth that provided the original motivation for developing REML. Given these problems GAMs are often compared using the conditional AIC, in which the model likelihood (not marginal likelihood) is used in the AIC, and the parameter count is taken as the effective degrees of freedom of the model.

Naive versions of the conditional AIC have been shown to be much too likely to select larger models in some circumstances, a difficulty attributable to neglect of smoothing parameter uncertainty when computing the effective degrees of freedom, however correcting the effective degrees of freedom for this problem restores reasonable performance.

## Caveats

Overfitting can be a problem with GAMs, especially if there is un-modelled residual auto-correlation or un-modelled overdispersion. Cross-validation can be used to detect and/or reduce overfitting problems with GAMs (or other statistical methods), and software often allows the level of penalization to be increased to force smoother fits. Estimating very large numbers of smoothing parameters is also likely to be statistically challenging, and there are known tendencies for prediction error criteria (GCV, AIC etc.) to occasionally undersmooth substantially, particularly at moderate sample sizes, with REML being somewhat less problematic in this regard.

Where appropriate, simpler models such as GLMs may be preferable to GAMs unless GAMs improve predictive ability substantially (in validation sets) for the application in question.

---
title: "Lasso (statistics)"
source: https://en.wikipedia.org/wiki/Lasso_(statistics)
domain: ridge-lasso-regression
license: CC-BY-SA-4.0
tags: ridge regression, lasso regression, shrinkage estimator, L2 regularization
fetched: 2026-07-02
---

# Lasso (statistics)

In statistics and machine learning, **lasso** (**least absolute shrinkage and selection operator**; also **Lasso**, **LASSO** or **L1 regularization**) is a regression analysis method that performs both variable selection and regularization in order to enhance the prediction accuracy and interpretability of the resulting statistical model. The lasso method assumes that the coefficients of the linear model are sparse, meaning that few of them are non-zero. It was originally introduced in geophysics, and later by Robert Tibshirani, who coined the term.

Lasso was originally formulated for linear regression models. This simple case reveals a substantial amount about the estimator. These include its relationship to ridge regression and best subset selection and the connections between lasso coefficient estimates and so-called soft thresholding. It also reveals that (like standard linear regression) the coefficient estimates do not need to be unique if covariates are collinear.

Though originally defined for linear regression, lasso regularization is easily extended to other statistical models including generalized linear models, generalized estimating equations, proportional hazards models, and M-estimators. Lasso's ability to perform subset selection relies on the form of the constraint and has a variety of interpretations including in terms of geometry, Bayesian statistics and convex analysis.

The LASSO is closely related to basis pursuit denoising.

## History

Lasso was introduced in order to improve the prediction accuracy and interpretability of regression models. It selects a reduced set of the known covariates for use in a model.

Lasso was developed independently in geophysics literature in 1986, based on prior work that used the $\ell ^{1}$ penalty for both fitting and penalization of the coefficients. Statistician Robert Tibshirani independently rediscovered and popularized it in 1996, based on Breiman's nonnegative garrote.

Prior to lasso, the most widely used method for choosing covariates was stepwise selection. That approach only improves prediction accuracy in certain cases, such as when only a few covariates have a strong relationship with the outcome. However, in other cases, it can increase prediction error.

At the time, ridge regression was the most popular technique for improving prediction accuracy. Ridge regression improves prediction error by shrinking the sum of the squares of the regression coefficients to be less than a fixed value in order to reduce overfitting, but it does not perform covariate selection and therefore does not help to make the model more interpretable.

Lasso achieves both of these goals by forcing the sum of the absolute value of the regression coefficients to be less than a fixed value, which forces certain coefficients to zero, excluding them from impacting prediction. This idea is similar to ridge regression, which also shrinks the size of the coefficients; however, ridge regression does not set coefficients to zero (and, thus, does not perform variable selection).

## Basic form

### Least squares

Consider a sample consisting of *N* cases, each of which consists of *p* covariates and a single outcome. Let $y_{i}$ be the outcome and $x_{i}:=(x_{1},x_{2},\ldots ,x_{p})_{i}^{\intercal }$ be the covariate vector for the *i* th case. Then the objective of lasso is to solve: $\min _{\beta _{0},\beta }{\biggl \{}\sum _{i=1}^{N}{\bigl (}y_{i}-\beta _{0}-x_{i}^{\intercal }\beta {\bigr )}^{2}{\biggr \}}$ subject to $\sum _{j=1}^{p}|\beta _{j}|\leq t.$

Here $\beta _{0}$ is the constant coefficient, $\beta :=(\beta _{1},\beta _{2},\ldots ,\beta _{p})$ is the coefficient vector, and t is a prespecified free parameter that determines the degree of regularization.

Letting X be the covariate matrix, so that $X_{ij}=(x_{i})_{j}$ and $x_{i}^{\intercal }$ is the *i* th row of X , the expression can be written more compactly as $\min _{\beta _{0},\beta }\left\{\left\|y-\beta _{0}-X\beta \right\|_{2}^{2}\right\}{\text{ subject to }}\|\beta \|_{1}\leq t,$ where $\|u\|_{p}={\biggl (}\sum _{i=1}^{N}|u_{i}|^{p}{\biggr )}^{1/p}$ is the standard $\ell ^{p}$ norm.

Denoting the scalar mean of the data points $x_{i}$ by ${\bar {x}}$ and the mean of the response variables $y_{i}$ by ${\bar {y}}$ , the resulting estimate for $\beta _{0}$ is ${\hat {\beta }}_{0}={\bar {y}}-{\bar {x}}^{\intercal }\beta$ , so that $y_{i}-{\hat {\beta }}_{0}-x_{i}^{\intercal }\beta =y_{i}-({\bar {y}}-{\bar {x}}^{\intercal }\beta )-x_{i}^{\intercal }\beta =(y_{i}-{\bar {y}})-(x_{i}-{\bar {x}})^{\intercal }\beta ,$ and therefore it is standard to work with variables that have been made zero-mean. Additionally, the covariates are typically standardized ${\textstyle {\bigl (}\sum _{i=1}^{N}x_{i}^{2}=1{\bigr )}}$ so that the solution does not depend on the measurement scale.

It can be helpful to rewrite $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|y-X\beta \right\|_{2}^{2}\right\}{\text{ subject to }}\|\beta \|_{1}\leq t.$ in the so-called Lagrangian form $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|y-X\beta \right\|_{2}^{2}+\lambda \|\beta \|_{1}\right\}$ where the exact relationship between t and $\lambda$ is data dependent.

### Orthonormal covariates

Some basic properties of the lasso estimator can now be considered.

Assuming first that the covariates are orthonormal so that $\ x_{i}^{\intercal }x_{j}=\delta _{ij}\ ,$ where $\ \delta _{ij}\$ is the Kronecker delta, or, equivalently, $\ X^{\intercal }X=I\ ,$ then using subgradient methods it can be shown that $\,{\begin{aligned}{\hat {\beta }}_{j}\ =\ {}&\operatorname {S} _{N,\lambda }\left({\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}\right)\ =\ {\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}\cdot \max \!\left\{\ 0,\ 1-{\frac {\ N\ \lambda \ }{\ {\bigl |}{\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}{\bigr |}\ }}\ \right\}\end{aligned}}\,$

where $\quad {\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}\ =\ (X^{\intercal }X)^{-1}X^{\intercal }y\ =\ X^{\intercal }y~.$

$\ S_{\alpha }\$ is referred to as the *soft thresholding operator*, since it translates values towards zero (making them exactly zero in the limit as they themselves approach zero) instead of setting smaller values to zero and leaving larger ones untouched as the *hard thresholding operator*, often denoted $\ H_{\alpha }\ ,$ would.

In ridge regression the objective is to minimize $\ \min _{\beta \in \mathbb {R} ^{p}}\left\{~{\tfrac {\ 1\ }{N}}{\Bigl \|}\ y-X\ \beta \ {\Bigr \|}_{2}^{2}\ +\ \lambda \ {\Bigl \|}\ \beta \ {\Bigr \|}_{2}^{2}~\right\}\$

Using $\ X^{\intercal }X=I\$ and the ridge regression formula: $\ {\hat {\beta }}={\Bigl (}\ X^{\intercal }X\ +\ N\ \lambda \ I\ {\Bigr )}^{-1}X^{\intercal }y\ ,$ yields: $\ {\hat {\beta }}_{j}=\left(1+N\ \lambda \right)^{-1}\ {\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}~.$

Ridge regression shrinks all coefficients by a uniform factor of $\ (1+N\lambda )^{-1}\$ and does not set any coefficients to zero.

It can also be compared to regression with best subset selection, in which the goal is to minimize $\ \min _{\beta \in \mathbb {R} ^{p}}\left\{~{\tfrac {1}{N}}{\Bigl \|}\ y-X\beta \ {\Bigr \|}_{2}^{2}\ +\ \lambda \ {\Bigl \|}\ \beta \ {\Bigr \|}_{0}~\right\}\$ where $\ \|\cdot \|_{0}\$ is the " $\ \ell ^{0}\$ norm", which is defined as $\ \|z\|=m\$ if exactly m components of z are nonzero. Again assuming orthonormal covariates, it can be shown that in this special case $\ {\hat {\beta }}_{j}\ =\ H_{\sqrt {N\lambda \ }}\ \left(\ {\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}\ \right)\ =\ {\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}\cdot \operatorname {\mathbb {I} } \left[~{\bigl |}{\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}{\bigr |}\geq {\sqrt {N\ \lambda \ }}~\right]\$ where $\ H_{\alpha }\$ is again the hard thresholding operator and $\ \mathbb {I} \$ is an indicator function (it is 1 if its argument is true and 0 otherwise).

Therefore, the lasso estimates share features of both ridge and best subset selection regression since they both shrink the magnitude of all the coefficients, like ridge regression and set some of them to zero, as in the best subset selection case. Additionally, while ridge regression scales all of the coefficients by a constant factor, lasso instead translates the coefficients towards zero by a constant value and sets them to zero if they reach it.

### Correlated covariates

In one special case two covariates, say *j* and *k*, are identical for each observation, so that $x_{(j)}=x_{(k)}$ , where $x_{(j),i}=x_{(k),i}$ . Then the values of $\beta _{j}$ and $\beta _{k}$ that minimize the lasso objective function are not uniquely determined. In fact, if some ${\hat {\beta }}$ in which ${\hat {\beta }}_{j}{\hat {\beta }}_{k}\geq 0$ , then if $s\in [0,1]$ replacing ${\hat {\beta }}_{j}$ by $s({\hat {\beta }}_{j}+{\hat {\beta }}_{k})$ and ${\hat {\beta }}_{k}$ by $(1-s)({\hat {\beta }}_{j}+{\hat {\beta }}_{k})$ , while keeping all the other ${\hat {\beta }}_{i}$ fixed, gives a new solution, so the lasso objective function then has a continuum of valid minimizers. Several variants of the lasso, including the Elastic net regularization, have been designed to address this shortcoming.

## General form

Lasso regularization can be extended to other objective functions such as those for generalized linear models, generalized estimating equations, proportional hazards models, and M-estimators. Given the objective function ${\frac {1}{N}}\sum _{i=1}^{N}f(x_{i},y_{i},\alpha ,\beta )$ the lasso regularized version of the estimator *s* the solution to $\min _{\alpha ,\beta }{\frac {1}{N}}\sum _{i=1}^{N}f(x_{i},y_{i},\alpha ,\beta ){\text{ subject to }}\|\beta \|_{1}\leq t$ where only $\beta$ is penalized while $\alpha$ is free to take any allowed value, just as $\beta _{0}$ was not penalized in the basic case.

## Interpretations

### Geometric interpretation

Lasso can set coefficients to zero, while the superficially similar ridge regression cannot. This is due to the difference in the shape of their constraint boundaries. Both lasso and ridge regression can be interpreted as minimizing the same objective function $\min _{\beta _{0},\beta }\left\{{\frac {1}{N}}\left\|y-\beta _{0}-X\beta \right\|_{2}^{2}\right\}$ but with respect to different constraints: $\|\beta \|_{1}\leq t$ for lasso and $\|\beta \|_{2}^{2}\leq t$ for ridge. The figure shows that the constraint region defined by the $\ell ^{1}$ norm is a square rotated so that its corners lie on the axes (in general a cross-polytope), while the region defined by the $\ell ^{2}$ norm is a circle (in general an *n*-sphere), which is rotationally invariant and, therefore, has no corners. As seen in the figure, a convex object that lies tangent to the boundary, such as the line shown, is likely to encounter a corner (or a higher-dimensional equivalent) of a hypercube, for which some components of $\beta$ are identically zero, while in the case of an *n*-sphere, the points on the boundary for which some of the components of $\beta$ are zero are not distinguished from the others and the convex object is no more likely to contact a point at which some components of $\beta$ are zero than one for which none of them are.

### Making λ easier to interpret with an accuracy-simplicity tradeoff

The lasso can be rescaled so that it becomes easy to anticipate and influence the degree of shrinkage associated with a given value of $\lambda$ . It is assumed that X is standardized with z-scores and that y is centered (zero mean). Let $\beta _{0}$ represent the hypothesized regression coefficients and let $b_{\text{OLS}}$ refer to the data-optimized ordinary least squares solutions. We can then define the Lagrangian as a tradeoff between the in-sample accuracy of the data-optimized solutions and the simplicity of sticking to the hypothesized values. This results in $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {(y-X\beta )'(y-X\beta )}{(y-X\beta _{0})'(y-X\beta _{0})}}+2\lambda \sum _{i=1}^{p}{\frac {|\beta _{i}-\beta _{0,i}|}{q_{i}}}\right\}$ where $q_{i}$ is specified below and the "prime" symbol stands for transpose. The first fraction represents relative accuracy, the second fraction relative simplicity, and $\lambda$ balances between the two.

Given a single regressor, relative simplicity can be defined by specifying $q_{i}$ as $|b_{\text{OLS}}-\beta _{0}|$ , which is the maximum amount of deviation from $\beta _{0}$ when $\lambda =0$ . Assuming that $\beta _{0}=0$ , the solution path can be defined in terms of $R^{2}$ : $b_{\ell _{1}}={\begin{cases}(1-\lambda /R^{2})b_{\text{OLS}}&{\mbox{if }}\lambda \leq R^{2},\\0&{\mbox{if }}\lambda >R^{2}.\end{cases}}$ If $\lambda =0$ , the ordinary least squares solution (OLS) is used. The hypothesized value of $\beta _{0}=0$ is selected if $\lambda$ is bigger than $R^{2}$ . Furthermore, if $R^{2}=1$ , then $\lambda$ represents the proportional influence of $\beta _{0}=0$ . In other words, $\lambda \times 100\%$ measures in percentage terms the minimal amount of influence of the hypothesized value relative to the data-optimized OLS solution.

If an $\ell _{2}$ -norm is used to penalize deviations from zero given a single regressor, the solution path is given by $b_{\ell _{2}}=\left(1+{\frac {\lambda }{R^{2}(1-\lambda )}}\right)^{-1}b_{\text{OLS}}.$ Like $b_{\ell _{1}}$ , $b_{\ell _{2}}$ moves in the direction of the point $(\lambda =R^{2},b=0)$ when $\lambda$ is close to zero; but unlike $b_{\ell _{1}}$ , the influence of $R^{2}$ diminishes in $b_{\ell _{2}}$ if $\lambda$ increases (see figure). Given multiple regressors, the moment that a parameter is activated (i.e. allowed to deviate from $\beta _{0}$ ) is also determined by a regressor's contribution to $R^{2}$ accuracy. First, $R^{2}=1-{\frac {(y-Xb)'(y-Xb)}{(y-X\beta _{0})'(y-X\beta _{0})}}.$ An $R^{2}$ of 75% means that in-sample accuracy improves by 75% if the unrestricted OLS solutions are used instead of the hypothesized $\beta _{0}$ values. The individual contribution of deviating from each hypothesis can be computed with the p x p matrix $R^{\otimes }=(X'{\tilde {y}}_{0})(X'{\tilde {y}}_{0})'(X'X)^{-1}({\tilde {y}}_{0}'{\tilde {y}}_{0})^{-1},$ where ${\tilde {y}}_{0}=y-X\beta _{0}$ . If $b=b_{\text{OLS}}$ when $R^{2}$ is computed, then the diagonal elements of $R^{\otimes }$ sum to $R^{2}$ . The diagonal $R^{\otimes }$ values may be smaller than 0 or, less often, larger than 1. If regressors are uncorrelated, then the $i^{th}$ diagonal element of $R^{\otimes }$ simply corresponds to the $r^{2}$ value between $x_{i}$ and y .

A rescaled version of the adaptive lasso of can be obtained by setting $q_{{\mbox{adaptive lasso}},i}=|b_{{\text{OLS}},i}-\beta _{0,i}|$ . If regressors are uncorrelated, the moment that the $i^{th}$ parameter is activated is given by the $i^{th}$ diagonal element of $R^{\otimes }$ . Assuming for convenience that $\beta _{0}$ is a vector of zeros, $b_{i}={\begin{cases}(1-\lambda /R_{ii}^{\otimes })b_{{\text{OLS}},i}&{\text{if }}\lambda \leq R_{ii}^{\otimes },\\0&{\text{if }}\lambda >R_{ii}^{\otimes }.\end{cases}}$ That is, if regressors are uncorrelated, $\lambda$ again specifies the minimal influence of $\beta _{0}$ . Even when regressors are correlated, the first time that a regression parameter is activated occurs when $\lambda$ is equal to the highest diagonal element of $R^{\otimes }$ .

These results can be compared to a rescaled version of the lasso by defining $q_{{\mbox{lasso}},i}={\frac {1}{p}}\sum _{l}|b_{{\text{OLS}},l}-\beta _{0,l}|$ , which is the average absolute deviation of $b_{\text{OLS}}$ from $\beta _{0}$ . Assuming that regressors are uncorrelated, then the moment of activation of the $i^{th}$ regressor is given by ${\tilde {\lambda }}_{{\text{lasso}},i}={\frac {1}{p}}{\sqrt {R_{i}^{\otimes }}}\sum _{l=1}^{p}{\sqrt {R_{l}^{\otimes }}}.$

For $p=1$ , the moment of activation is again given by ${\tilde {\lambda }}_{{\text{lasso}},i}=R^{2}$ . If $\beta _{0}$ is a vector of zeros and a subset of $p_{B}$ relevant parameters are equally responsible for a perfect fit of $R^{2}=1$ , then this subset is activated at a $\lambda$ value of ${\frac {1}{p}}$ . The moment of activation of a relevant regressor then equals ${\frac {1}{p}}{\frac {1}{\sqrt {p_{B}}}}p_{B}{\frac {1}{\sqrt {p_{B}}}}={\frac {1}{p}}$ . In other words, the inclusion of irrelevant regressors delays the moment that relevant regressors are activated by this rescaled lasso. The adaptive lasso and the lasso are special cases of a '1ASTc' estimator. The latter only groups parameters together if the absolute correlation among regressors is larger than a user-specified value.

### Bayesian interpretation

Just as ridge regression can be interpreted as linear regression for which the coefficients have been assigned normal prior distributions, lasso can be interpreted as linear regression for which the coefficients have Laplace prior distributions. The Laplace distribution is sharply peaked at zero (its first derivative is discontinuous at zero) and it concentrates its probability mass closer to zero than does the normal distribution. This provides an alternative explanation of why lasso tends to set some coefficients to zero, while ridge regression does not.

### Convex relaxation interpretation

Lasso can also be viewed as a convex relaxation of the best subset selection regression problem, which is to find the subset of $\leq k$ covariates that results in the smallest value of the objective function for some fixed $k\leq n$ , where n is the total number of covariates. The " $\ell ^{0}$ norm", $\|\cdot \|_{0}$ , (the number of nonzero entries of a vector), is the limiting case of " $\ell ^{p}$ norms", of the form $\textstyle \|x\|_{p}=\left(\sum _{i=1}^{n}|x_{j}|^{p}\right)^{1/p}$ (where the quotation marks signify that these are not really norms for $p<1$ since $\|\cdot \|_{p}$ is not convex for $p<1$ , so the triangle inequality does not hold). Therefore, since p = 1 is the smallest value for which the " $\ell ^{p}$ norm" is convex (and therefore actually a norm), lasso is, in some sense, the best convex approximation to the best subset selection problem, since the region defined by $\|x\|_{1}\leq t$ is the convex hull of the region defined by $\|x\|_{p}\leq t$ for $p<1$ .

## Generalizations

Lasso variants have been created in order to remedy limitations of the original technique and to make the method more useful for particular problems. Almost all of these focus on respecting or exploiting dependencies among the covariates.

Elastic net regularization adds an additional ridge regression-like penalty that improves performance when the number of predictors is larger than the sample size, allows the method to select strongly correlated variables together, and improves overall prediction accuracy.

Group lasso allows groups of related covariates to be selected as a single unit, which can be useful in settings where it does not make sense to include some covariates without others. Further extensions of group lasso perform variable selection within individual groups (sparse group lasso) and allow overlap between groups (overlap group lasso).

Fused lasso can account for the spatial or temporal characteristics of a problem, resulting in estimates that better match system structure. Lasso-regularized models can be fit using techniques including subgradient methods, least-angle regression (LARS), and proximal gradient methods. Determining the optimal value for the regularization parameter is an important part of ensuring that the model performs well; it is typically chosen using cross-validation.

### Elastic net

In 2005, Zou and Hastie introduced the elastic net. When *p* > *n* (the number of covariates is greater than the sample size) lasso can select only *n* covariates (even when more are associated with the outcome) and it tends to select one covariate from any set of highly correlated covariates. Additionally, even when *n* > *p*, ridge regression tends to perform better given strongly correlated covariates.

The elastic net extends lasso by adding an additional $\ell ^{2}$ penalty term giving $\min _{\beta \in \mathbb {R} ^{p}}\left\{\left\|y-X\beta \right\|_{2}^{2}+\lambda _{1}\|\beta \|_{1}+\lambda _{2}\|\beta \|_{2}^{2}\right\},$ which is equivalent to solving ${\begin{aligned}\min _{\beta _{0},\beta }\left\{\left\|y-\beta _{0}-X\beta \right\|_{2}^{2}\right\}&{\text{ subject to }}(1-\alpha )\|\beta \|_{1}+\alpha \|\beta \|_{2}^{2}\leq t,\\&{\text{ where }}\alpha ={\frac {\lambda _{2}}{\lambda _{1}+\lambda _{2}}}.\end{aligned}}$

This problem can be written in a simple lasso form $\min _{\beta ^{*}\in \mathbb {R} ^{p}}\left\{\left\|y^{*}-X^{*}\beta ^{*}\right\|_{2}^{2}+\lambda ^{*}\|\beta ^{*}\|_{1}\right\}$ letting $X_{(n+p)\times p}^{*}=(1+\lambda _{2})^{-1/2}{\binom {X}{\lambda _{2}^{1/2}I_{p\times p}}},$ $y_{(n+p)}^{*}={\binom {y}{0^{p}}},\qquad \lambda ^{*}={\frac {\lambda _{1}}{\sqrt {1+\lambda _{2}}}},$ $\beta ^{*}={\sqrt {1+\lambda _{2}}}\beta .$

Then ${\hat {\beta }}={\frac {{\hat {\beta }}^{*}}{\sqrt {1+\lambda _{2}}}}$ , which, when the covariates are orthogonal to each other, gives ${\hat {\beta }}_{j}={\frac {{\hat {\beta }}{}_{j}^{\!\;*,{\text{OLS}}}}{\sqrt {1+\lambda _{2}}}}\max {\Biggl (}0,1-{\frac {\lambda ^{*}}{{\bigl |}{\hat {\beta }}{}_{j}^{\!\;*,{\text{OLS}}}{\bigr |}}}{\Biggr )}={\frac {{\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}}{1+\lambda _{2}}}\max {\Biggl (}0,1-{\frac {\lambda _{1}}{{\bigl |}{\hat {\beta }}{}_{j}^{\!\;{\text{OLS}}}{\bigr |}}}{\Biggr )}=(1+\lambda _{2})^{-1}{\hat {\beta }}{}_{j}^{\text{lasso}}.$

So the result of the elastic net penalty is a combination of the effects of the lasso and ridge penalties.

Returning to the general case, the fact that the penalty function is now strictly convex means that if $x_{(j)}=x_{(k)}$ , ${\hat {\beta }}_{j}={\hat {\beta }}_{k}$ , which is a change from lasso. In general, if ${\hat {\beta }}_{j}{\hat {\beta _{k}}}>0$ ${\frac {|{\hat {\beta }}_{j}-{\hat {\beta _{k}}}|}{\|y\|}}\leq \lambda _{2}^{-1}{\sqrt {2(1-\rho _{jk})}},{\text{ where }}\rho =X^{\intercal }X,$ is the sample correlation matrix because the x 's are normalized.

Therefore, highly correlated covariates tend to have similar regression coefficients, with the degree of similarity depending on both $\|y\|_{1}$ and $\lambda _{2}$ , which is different from lasso. This phenomenon, in which strongly correlated covariates have similar regression coefficients, is referred to as the grouping effect. Grouping is desirable since, in applications such as tying genes to a disease, finding all the associated covariates is preferable, rather than selecting one from each set of correlated covariates, as lasso often does. In addition, selecting only one from each group typically results in increased prediction error, since the model is less robust (which is why ridge regression often outperforms lasso).

### Group lasso

In 2006, Yuan and Lin introduced the group lasso to allow predefined groups of covariates to jointly be selected into or out of a model. This is useful in many settings, perhaps most obviously when a categorical variable is coded as a collection of binary covariates. In this case, group lasso can ensure that all the variables encoding the categorical covariate are included or excluded together. Another setting in which grouping is natural is in biological studies. Since genes and proteins often lie in known pathways, which pathways are related to an outcome may be more significant than whether individual genes are. The objective function for the group lasso is a natural generalization of the standard lasso objective $\min _{\beta \in \mathbb {R} ^{p}}{\biggl \{}{\biggl \|}y-\sum _{j=1}^{J}X_{j}\beta _{j}{\biggr \|}_{2}^{2}+\lambda \sum _{j=1}^{J}\|\beta _{j}\|_{K_{j}}{\biggr \}},\qquad \|z\|_{K_{j}}=(z^{\intercal }K_{j}z)^{1/2}$ where the design matrix X and covariate vector $\beta$ have been replaced by a collection of design matrices $X_{j}$ and covariate vectors $\beta _{j}$ , one for each of the J groups. Additionally, the penalty term is now a sum over $\ell ^{2}$ norms defined by the positive definite matrices $K_{j}$ . If each covariate is in its own group and $K_{j}=I$ , then this reduces to the standard lasso, while if there is only a single group and $K_{1}=I$ , it reduces to ridge regression. Since the penalty reduces to an $\ell ^{2}$ norm on the subspaces defined by each group, it cannot select out only some of the covariates from a group, just as ridge regression cannot. However, because the penalty is the sum over the different subspace norms, as in the standard lasso, the constraint has some non-differential points, which correspond to some subspaces being identically zero. Therefore, it can set the coefficient vectors corresponding to some subspaces to zero, while only shrinking others. However, it is possible to extend the group lasso to the so-called sparse group lasso, which can select individual covariates within a group, by adding an additional $\ell ^{1}$ penalty to each group subspace. Another extension, group lasso with overlap allows covariates to be shared across groups, e.g., if a gene were to occur in two pathways.

The "gglasso" package by in R, allows for fast and efficient implementation of Group LASSO.

### Fused lasso

In some cases, the phenomenon under study may have important spatial or temporal structure that must be considered during analysis, such as time series or image-based data. In 2005, Tibshirani and colleagues introduced the fused lasso to extend the use of lasso to this type of data. The fused lasso objective function is ${\begin{aligned}&\min _{\beta }{\biggl \{}{\frac {1}{N}}\sum _{i=1}^{N}\left(y_{i}-x_{i}^{\intercal }\beta \right)^{2}{\biggr \}}\\[4pt]&{\text{ subject to }}\sum _{j=1}^{p}|\beta _{j}|\leq t_{1}{\text{ and }}\sum _{j=2}^{p}|\beta _{j}-\beta _{j-1}|\leq t_{2}.\end{aligned}}$

The first constraint is the lasso constraint, while the second directly penalizes large changes with respect to the temporal or spatial structure, which forces the coefficients to vary smoothly to reflect the system's underlying logic. Clustered lasso is a generalization of fused lasso that identifies and groups relevant covariates based on their effects (coefficients). The basic idea is to penalize the differences between the coefficients so that nonzero ones cluster. This can be modeled using the following regularization: $\sum _{i<j}^{p}|\beta _{i}-\beta _{j}|\leq t_{2}.$

In contrast, variables can be clustered into highly correlated groups, and then a single representative covariate can be extracted from each cluster.

Algorithms exist that solve the fused lasso problem, and some generalizations of it. Algorithms can solve it exactly in a finite number of operations.

### Quasi-norms and bridge regression

Lasso, elastic net, group and fused lasso construct the penalty functions from the $\ell ^{1}$ and $\ell ^{2}$ norms (with weights, if necessary). The bridge regression utilises general $\ell ^{p}$ norms ( $p\geq 1$ ) and quasinorms ( $0<p<1$ ). For example, for *p*=1/2 the analogue of lasso objective in the Lagrangian form is to solve $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|y-X\beta \right\|_{2}^{2}+\lambda {\sqrt {\|\beta \|_{1/2}}}\right\},$ where $\|\beta \|_{1/2}={\biggl (}\sum _{j=1}^{p}{\sqrt {|\beta _{j}|}}{\biggr )}^{2}$

It is claimed that the fractional quasi-norms $\ell ^{p}$ ( $0<p<1$ ) provide more meaningful results in data analysis both theoretically and empirically. The non-convexity of these quasi-norms complicates the optimization problem. To solve this problem, an expectation-minimization procedure is developed and implemented for minimization of function $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|y-X\beta \right\|_{2}^{2}+\lambda \sum _{j=1}^{p}\vartheta (\beta _{j}^{2})\right\},$ where $\vartheta (\gamma )$ is an arbitrary concave monotonically increasing function (for example, $\vartheta (\gamma )={\sqrt {\gamma }}$ gives the lasso penalty and $\vartheta (\gamma )=\gamma ^{1/4}$ gives the $\ell ^{1/2}$ penalty).

The efficient algorithm for minimization is based on piece-wise quadratic approximation of subquadratic growth (PQSQ).

### Adaptive lasso

The adaptive lasso was introduced by Zou in 2006 for linear regression and by Zhang and Lu in 2007 for proportional hazards regression.

### Prior lasso

The prior lasso was introduced for generalized linear models by Jiang et al. in 2016 to incorporate prior information, such as the importance of certain covariates. In prior lasso, such information is summarized into pseudo responses (called prior responses) ${\hat {y}}^{\mathrm {p} }$ and then an additional criterion function is added to the usual objective function with a lasso penalty. Without loss of generality, in linear regression, the new objective function can be written as $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|y-X\beta \right\|_{2}^{2}+{\frac {1}{N}}\eta \left\|{\hat {y}}^{\mathrm {p} }-X\beta \right\|_{2}^{2}+\lambda \|\beta \|_{1}\right\},$ which is equivalent to $\min _{\beta \in \mathbb {R} ^{p}}\left\{{\frac {1}{N}}\left\|{\tilde {y}}-X\beta \right\|_{2}^{2}+{\frac {\lambda }{1+\eta }}\|\beta \|_{1}\right\},$

the usual lasso objective function with the responses y being replaced by a weighted average of the observed responses and the prior responses ${\tilde {y}}=(y+\eta {\hat {y}}^{\mathrm {p} })/(1+\eta )$ (called the adjusted response values by the prior information).

In prior lasso, the parameter $\eta$ is called a balancing parameter, in that it balances the relative importance of the data and the prior information. In the extreme case of $\eta =0$ , prior lasso is reduced to lasso. If $\eta =\infty$ , prior lasso will solely rely on the prior information to fit the model. Furthermore, the balancing parameter $\eta$ has another appealing interpretation: it controls the variance of $\beta$ in its prior distribution from a Bayesian viewpoint.

Prior lasso is more efficient in parameter estimation and prediction (with a smaller estimation error and prediction error) when the prior information is of high quality, and is robust to the low quality prior information with a good choice of the balancing parameter $\eta$ .

### Ensemble lasso

Lasso can be run in an ensemble. This can be especially useful when the data is high-dimensional. The procedure involves running lasso on each of several random subsets of the data and collating the results.

## Computing lasso solutions

The loss function of the lasso is not differentiable, but a wide variety of techniques from convex analysis and optimization theory have been developed to compute the solutions path of the lasso. These include coordinate descent, subgradient methods, least-angle regression (LARS), and proximal gradient methods. Subgradient methods are the natural generalization of traditional methods such as gradient descent and stochastic gradient descent to the case in which the objective function is not differentiable at all points. LARS is a method that is closely tied to lasso models, and in many cases allows them to be fit efficiently, though it may not perform well in all circumstances. LARS generates complete solution paths. Proximal methods have become popular because of their flexibility and performance and are an area of active research. The choice of method will depend on the particular lasso variant, the data and the available resources. However, proximal methods generally perform well.

The "glmnet" package in R, where "glm" is a reference to "generalized linear models" and "net" refers to the "net" from "elastic net" provides an extremely efficient way to implement LASSO and some of its variants.

The "celer" package in Python provides a highly efficient solver for the Lasso problem, often outperforming traditional solvers like scikit-learn by up to 100 times in certain scenarios, particularly with high-dimensional datasets. This package leverages dual extrapolation techniques to achieve its performance gains. The celer package is available at GitHub.

## Choice of regularization parameter

Choosing the regularization parameter ( $\lambda$ ) is a fundamental part of lasso. A good value is essential to the performance of lasso since it controls the strength of shrinkage and variable selection, which, in moderation can improve both prediction accuracy and interpretability. However, if the regularization becomes too strong, important variables may be omitted and coefficients may be shrunk excessively, which can harm both predictive capacity and inferencing. Cross-validation is often used to find the regularization parameter.

Information criteria such as the Bayesian information criterion (BIC) and the Akaike information criterion (AIC) might be preferable to cross-validation, because they are faster to compute and their performance is less volatile in small samples. An information criterion selects the estimator's regularization parameter by maximizing a model's in-sample accuracy while penalizing its effective number of parameters/degrees of freedom. Zou et al. proposed to measure the effective degrees of freedom by counting the number of parameters that deviate from zero. The degrees of freedom approach was considered flawed by Kaufman and Rosset and Janson et al., because a model's degrees of freedom might increase even when it is penalized harder by the regularization parameter. As an alternative, the relative simplicity measure defined above can be used to count the effective number of parameters. For the lasso, this measure is given by ${\hat {\mathcal {P}}}=\sum _{i=1}^{p}{\frac {|\beta _{i}-\beta _{0,i}|}{{\frac {1}{p}}\sum _{l}|b_{{\text{OLS}},l}-\beta _{0,l}|}},$ which monotonically increases from zero to p as the regularization parameter decreases from $\infty$ to zero.

## Selected applications

LASSO has been applied in economics and finance, and was found to improve prediction and to select sometimes neglected variables, for example in corporate bankruptcy prediction literature, or high growth firms prediction.

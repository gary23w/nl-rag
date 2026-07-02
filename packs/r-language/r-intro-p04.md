---
title: "An Introduction to R (part 4/6)"
source: https://cran.r-project.org/doc/manuals/r-release/R-intro.html
domain: r-language
license: GFDL-1.3
tags: r language, rstats, cran, statistical computing
fetched: 2026-07-02
part: 4/6
---

## 11 Statistical models in R

This section presumes the reader has some familiarity with statistical methodology, in particular with regression analysis and the analysis of variance. Later we make some rather more ambitious presumptions, namely that something is known about generalized linear models and nonlinear regression.

The requirements for fitting statistical models are sufficiently well defined to make it possible to construct general tools that apply in a broad spectrum of problems.

R provides an interlocking suite of facilities that make fitting statistical models very simple. As we mention in the introduction, the basic output is minimal, and one needs to ask for the details by calling extractor functions.

### 11.1 Defining statistical models; formulae

The template for a statistical model is a linear regression model with independent, homoscedastic errors

```
y_i = sum_{j=0}^p beta_j x_{ij} + e_i,     i = 1, ..., n,
```

where the e_i are NID(0, sigma^2). In matrix terms this would be written

```
y = X  beta + e
```

where the *y* is the response vector, *X* is the *model matrix* or *design matrix* and has columns *x_0, x_1, ..., x_p*, the determining variables. Very often *x_0* will be a column of ones defining an *intercept* term.

#### Examples

Before giving a formal specification, a few examples may usefully set the picture.

Suppose `y`, `x`, `x0`, `x1`, `x2`, … are numeric variables, `X` is a matrix and `A`, `B`, `C`, … are factors. The following formulae on the left side below specify statistical models as described on the right.

**`y ~ x`**

**`y ~ 1 + x`**

Both imply the same simple linear regression model of *y* on *x*. The first has an implicit intercept term, and the second an explicit one.

**`y ~ 0 + x`**

**`y ~ -1 + x`**

**`y ~ x - 1`**

Simple linear regression of *y* on *x* through the origin (that is, without an intercept term).

**`log(y) ~ x1 + x2`**

Multiple regression of the transformed variable,log(y), on *x1* and *x2* (with an implicit intercept term).

**`y ~ poly(x,2)`**

**`y ~ 1 + x + I(x^2)`**

Polynomial regression of *y* on *x* of degree 2. The first form uses orthogonal polynomials, and the second uses explicit powers, as basis.

**`y ~ X + poly(x,2)`**

Multiple regression *y* with model matrix consisting of the matrix *X* as well as polynomial terms in *x* to degree 2.

**`y ~ A`**

Single classification analysis of variance model of *y*, with classes determined by *A*.

**`y ~ A + x`**

Single classification analysis of covariance model of *y*, with classes determined by *A*, and with covariate *x*.

**`y ~ A*B`**

**`y ~ A + B + A:B`**

**`y ~ B %in% A`**

**`y ~ A/B`**

Two factor non-additive model of *y* on *A* and *B*. The first two specify the same crossed classification and the second two specify the same nested classification. In abstract terms all four specify the same model subspace.

**`y ~ (A + B + C)^2`**

**`y ~ A*B*C - A:B:C`**

Three factor experiment but with a model containing main effects and two factor interactions only. Both formulae specify the same model.

**`y ~ A * x`**

**`y ~ A/x`**

**`y ~ A/(1 + x) - 1`**

Separate simple linear regression models of *y* on *x* within the levels of *A*, with different codings. The last form produces explicit estimates of as many different intercepts and slopes as there are levels in *A*.

**`y ~ A*B + Error(C)`**

An experiment with two treatment factors, *A* and *B*, and error strata determined by factor *C*. For example a split plot experiment, with whole plots (and hence also subplots), determined by factor *C*.

The operator `~` is used to define a *model formula* in R. The form, for an ordinary linear model, is

```
response ~ op_1 term_1 op_2 term_2 op_3 term_3 ...
```

where

***response***

is a vector or matrix, (or expression evaluating to a vector or matrix) defining the response variable(s).

***op_i***

is an operator, either `+` or `-`, implying the inclusion or exclusion of a term in the model, (the first is optional).

***term_i***

is either

- a vector or matrix expression, or `1`,
- a factor, or
- a *formula expression* consisting of factors, vectors or matrices connected by *formula operators*.

In all cases each term defines a collection of columns either to be added to or removed from the model matrix. A `1` stands for an intercept column and is by default included in the model matrix unless explicitly removed.

The *formula operators* are similar in effect to the Wilkinson and Rogers notation used by such programs as Glim and Genstat. One inevitable change is that the operator ‘`.`’ becomes ‘`:`’ since the period is a valid name character in R.

The notation is summarized below (based on Chambers & Hastie, 1992, p.29):

**`*Y* ~ *M*`**

*Y* is modeled as *M*.

**`*M_1* + *M_2*`**

Include *M_1* and *M_2*.

**`*M_1* - *M_2*`**

Include *M_1* leaving out terms of *M_2*.

**`*M_1* : *M_2*`**

The tensor product of *M_1* and *M_2*. If both terms are factors, then the “subclasses” factor.

**`*M_1* %in% *M_2*`**

Similar to `*M_1*:*M_2*`, but with a different coding.

**`*M_1* * *M_2*`**

`*M_1* + *M_2* + *M_1*:*M_2*`.

**`*M_1* / *M_2*`**

`*M_1* + *M_2* %in% *M_1*`.

**`*M*^*n*`**

All terms in *M* together with “interactions” up to order *n*

**`I(*M*)`**

Insulate *M*. Inside *M* all operators have their normal arithmetic meaning, and that term appears in the model matrix.

Note that inside the parentheses that usually enclose function arguments all operators have their normal arithmetic meaning. The function `I()` is an identity function used to allow terms in model formulae to be defined using arithmetic operators.

Note particularly that the model formulae specify the *columns of the model matrix*, the specification of the parameters being implicit. This is not the case in other contexts, for example in specifying nonlinear models.

#### 11.1.1 Contrasts

We need at least some idea how the model formulae specify the columns of the model matrix. This is easy if we have continuous variables, as each provides one column of the model matrix (and the intercept will provide a column of ones if included in the model).

What about a *k*-level factor `A`? The answer differs for unordered and ordered factors. For *unordered* factors *k - 1* columns are generated for the indicators of the second, …, *k*-th levels of the factor. (Thus the implicit parameterization is to contrast the response at each level with that at the first.) For *ordered* factors the *k - 1* columns are the orthogonal polynomials on *1, ..., k*, omitting the constant term.

Although the answer is already complicated, it is not the whole story. First, if the intercept is omitted in a model that contains a factor term, the first such term is encoded into *k* columns giving the indicators for all the levels. Second, the whole behavior can be changed by the `options` setting for `contrasts`. The default setting in R is

```
options(contrasts = c("contr.treatment", "contr.poly"))
```

The main reason for mentioning this is that R and S have different defaults for unordered factors, S using Helmert contrasts. So if you need to compare your results to those of a textbook or paper which used S-PLUS, you will need to set

```
options(contrasts = c("contr.helmert", "contr.poly"))
```

This is a deliberate difference, as treatment contrasts (R’s default) are thought easier for newcomers to interpret.

We have still not finished, as the contrast scheme to be used can be set for each term in the model using the functions `contrasts` and `C`.

We have not yet considered interaction terms: these generate the products of the columns introduced for their component terms.

Although the details are complicated, model formulae in R will normally generate the models that an expert statistician would expect, provided that marginality is preserved. Fitting, for example, a model with an interaction but not the corresponding main effects will in general lead to surprising results, and is for experts only.

### 11.2 Linear models

The basic function for fitting ordinary multiple models is `lm()`, and a streamlined version of the call is as follows:

```
> fitted.model <- lm(formula, data = data.frame)
```

For example

```
> fm2 <- lm(y ~ x1 + x2, data = production)
```

would fit a multiple regression model of *y* on *x1* and *x2* (with implicit intercept term).

The important (but technically optional) parameter `data = production` specifies that any variables needed to construct the model should come first from the `production` *data frame*. *This is the case regardless of whether data frame `production` has been attached on the search path or not*.

### 11.3 Generic functions for extracting model information

The value of `lm()` is a fitted model object; technically a list of results of class `"lm"`. Information about the fitted model can then be displayed, extracted, plotted and so on by using generic functions that orient themselves to objects of class `"lm"`. These include

```
add1    deviance   formula      predict  step
alias   drop1      kappa        print    summary
anova   effects    labels       proj     vcov
coef    family     plot         residuals
```

A brief description of the most commonly used ones is given below.

**`anova(*object_1*, *object_2*)` ¶**

Compare a submodel with an outer model and produce an analysis of variance table.

**`coef(*object*)` ¶**

Extract the regression coefficient (matrix).

Long form: `coefficients(*object*)`.

**`deviance(*object*)` ¶**

Residual sum of squares, weighted if appropriate.

**`formula(*object*)` ¶**

Extract the model formula.

**`plot(*object*)` ¶**

Produce four plots, showing residuals, fitted values and some diagnostics.

**`predict(*object*, newdata=*data.frame*)` ¶**

The data frame supplied must have variables specified with the same labels as the original. The value is a vector or matrix of predicted values corresponding to the determining variable values in *data.frame*.

**`print(*object*)` ¶**

Print a concise version of the object. Most often used implicitly.

**`residuals(*object*)` ¶**

Extract the (matrix of) residuals, weighted as appropriate.

Short form: `resid(*object*)`.

**`step(*object*)` ¶**

Select a suitable model by adding or dropping terms and preserving hierarchies. The model with the smallest value of AIC (Akaike’s An Information Criterion) discovered in the stepwise search is returned.

**`summary(*object*)` ¶**

Print a comprehensive summary of the results of the regression analysis.

**`vcov(*object*)` ¶**

Returns the variance-covariance matrix of the main parameters of a fitted model object.

### 11.4 Analysis of variance and model comparison

The model fitting function `aov(*formula*, data=*data.frame*)` operates at the simplest level in a very similar way to the function `lm()`, and most of the generic functions listed in the table in Generic functions for extracting model information apply.

It should be noted that in addition `aov()` allows an analysis of models with multiple error strata such as split plot experiments, or balanced incomplete block designs with recovery of inter-block information. The model formula

```
response ~ mean.formula + Error(strata.formula)
```

specifies a multi-stratum experiment with error strata defined by the *strata.formula*. In the simplest case, *strata.formula* is simply a factor, when it defines a two strata experiment, namely between and within the levels of the factor.

For example, with all determining variables factors, a model formula such as that in:

```
> fm <- aov(yield ~ v + n*p*k + Error(farms/blocks), data=farm.data)
```

would typically be used to describe an experiment with mean model `v + n*p*k` and three error strata, namely “between farms”, “within farms, between blocks” and “within blocks”.

#### 11.4.1 ANOVA tables

Note also that the analysis of variance table (or tables) are for a sequence of fitted models. The sums of squares shown are the decrease in the residual sums of squares resulting from an inclusion of *that term* in the model at *that place* in the sequence. Hence only for orthogonal experiments will the order of inclusion be inconsequential.

For multistratum experiments the procedure is first to project the response onto the error strata, again in sequence, and to fit the mean model to each projection. For further details, see Chambers & Hastie (1992).

A more flexible alternative to the default full ANOVA table is to compare two or more models directly using the `anova()` function.

```
> anova(fitted.model.1, fitted.model.2, ...)
```

The display is then an ANOVA table showing the differences between the fitted models when fitted in sequence. The fitted models being compared would usually be an hierarchical sequence, of course. This does not give different information to the default, but rather makes it easier to comprehend and control.

### 11.5 Updating fitted models

The `update()` function is largely a convenience function that allows a model to be fitted that differs from one previously fitted usually by just a few additional or removed terms. Its form is

```
> new.model <- update(old.model, new.formula)
```

In the *new.formula* the special name consisting of a period, ‘`.`’, only, can be used to stand for “the corresponding part of the old model formula”. For example,

```
> fm05 <- lm(y ~ x1 + x2 + x3 + x4 + x5, data = production)
> fm6  <- update(fm05, . ~ . + x6)
> smf6 <- update(fm6, sqrt(.) ~ .)
```

would fit a five variate multiple regression with variables (presumably) from the data frame `production`, fit an additional model including a sixth regressor variable, and fit a variant on the model where the response had a square root transform applied.

Note especially that if the `data=` argument is specified on the original call to the model fitting function, this information is passed on through the fitted model object to `update()` and its allies.

The name ‘.’ can also be used in other contexts, but with slightly different meaning. For example

```
> fmfull <- lm(y ~ . , data = production)
```

would fit a model with response `y` and regressor variables *all other variables in the data frame `production`*.

Other functions for exploring incremental sequences of models are `add1()`, `drop1()` and `step()`. The names of these give a good clue to their purpose, but for full details see the on-line help.

### 11.6 Generalized linear models

Generalized linear modeling is a development of linear models to accommodate both non-normal response distributions and transformations to linearity in a clean and straightforward way. A generalized linear model may be described in terms of the following sequence of assumptions:

- There is a response, *y*, of interest and stimulus variables x_1, x_2, …, whose values influence the distribution of the response.
- The stimulus variables influence the distribution of *y* through *a single linear function, only*. This linear function is called the *linear predictor*, and is usually written eta = beta_1 x_1 + beta_2 x_2 + ... + beta_p x_p, hence *x_i* has no influence on the distribution of *y* if and only if beta_i is zero.
- The distribution of *y* is of the form f_Y(y; mu, phi) = exp((A/phi) * (y lambda(mu) - gamma(lambda(mu))) + tau(y, phi)) where phi is a *scale parameter* (possibly known), and is constant for all observations, *A* represents a prior weight, assumed known but possibly varying with the observations, and mu is the mean of *y*. So it is assumed that the distribution of *y* is determined by its mean and possibly a scale parameter as well.
- The mean, mu, is a smooth invertible function of the linear predictor: mu = m(eta), eta = m^{-1}(mu) = ell(mu) and this inverse function, ell(), is called the *link function*.

These assumptions are loose enough to encompass a wide class of models useful in statistical practice, but tight enough to allow the development of a unified methodology of estimation and inference, at least approximately. The reader is referred to any of the current reference works on the subject for full details, such as McCullagh & Nelder (1989) or Dobson (1990).

#### 11.6.1 Families

The class of generalized linear models handled by facilities supplied in R includes *gaussian*, *binomial*, *poisson*, *inverse gaussian* and *gamma* response distributions and also *quasi-likelihood* models where the response distribution is not explicitly specified. In the latter case the *variance function* must be specified as a function of the mean, but in other cases this function is implied by the response distribution.

Each response distribution admits a variety of link functions to connect the mean with the linear predictor. Those automatically available are shown in the following table:

> | Family name | Link functions |
> |---|---|
> | `binomial` | `logit`, `probit`, `log`, `cloglog` |
> | `gaussian` | `identity`, `log`, `inverse` |
> | `Gamma` | `identity`, `inverse`, `log` |
> | `inverse.gaussian` | `1/mu^2`, `identity`, `inverse`, `log` |
> | `poisson` | `identity`, `log`, `sqrt` |
> | `quasi` | `logit`, `probit`, `cloglog`, `identity`, `inverse`, `log`, `1/mu^2`, `sqrt` |

The combination of a response distribution, a link function and various other pieces of information that are needed to carry out the modeling exercise is called the *family* of the generalized linear model.

#### 11.6.2 The `glm()` function

Since the distribution of the response depends on the stimulus variables through a single linear function *only*, the same mechanism as was used for linear models can still be used to specify the linear part of a generalized model. The family has to be specified in a different way.

The R function to fit a generalized linear model is `glm()` which uses the form

```
> fitted.model <- glm(formula, family=family.generator, data=data.frame)
```

The only new feature is the *family.generator*, which is the instrument by which the family is described. It is the name of a function that generates a list of functions and expressions that together define and control the model and estimation process. Although this may seem a little complicated at first sight, its use is quite simple.

The names of the standard, supplied family generators are given under “Family Name” in the table in Families. Where there is a choice of links, the name of the link may also be supplied with the family name, in parentheses as a parameter. In the case of the `quasi` family, the variance function may also be specified in this way.

Some examples make the process clear.

#### The `gaussian` family

A call such as

```
> fm <- glm(y ~ x1 + x2, family = gaussian, data = sales)
```

achieves the same result as

```
> fm <- lm(y ~ x1+x2, data=sales)
```

but much less efficiently. Note how the gaussian family is not automatically provided with a choice of links, so no parameter is allowed. If a problem requires a gaussian family with a nonstandard link, this can usually be achieved through the `quasi` family, as we shall see later.

#### The `binomial` family

Consider a small, artificial example, from Silvey (1970).

On the Aegean island of Kalythos the male inhabitants suffer from a congenital eye disease, the effects of which become more marked with increasing age. Samples of islander males of various ages were tested for blindness and the results recorded. The data is shown below:

| Age: | 20 | 35 | 45 | 55 | 70 |
|---|---|---|---|---|---|
| No. tested: | 50 | 50 | 50 | 50 | 50 |
| No. blind: | 6 | 17 | 26 | 37 | 44 |

The problem we consider is to fit both logistic and probit models to this data, and to estimate for each model the LD50, that is the age at which the chance of blindness for a male inhabitant is 50%.

If *y* is the number of blind at age *x* and *n* the number tested, both models have the form y ~ B(n, F(beta_0 + beta_1 x)) where for the probit case, F(z) = Phi(z) is the standard normal distribution function, and in the logit case (the default), F(z) = e^z/(1+e^z). In both cases the LD50 is LD50 = - beta_0/beta_1 that is, the point at which the argument of the distribution function is zero.

The first step is to set the data up as a data frame

```
> kalythos <- data.frame(x = c(20,35,45,55,70), n = rep(50,5),
                         y = c(6,17,26,37,44))
```

To fit a binomial model using `glm()` there are three possibilities for the response:

- If the response is a *vector* it is assumed to hold *binary* data, and so must be a *0/1* vector.
- If the response is a *two-column matrix* it is assumed that the first column holds the number of successes for the trial and the second holds the number of failures.
- If the response is a *factor*, its first level is taken as failure (0) and all other levels as ‘success’ (1).

Here we need the second of these conventions, so we add a matrix to our data frame:

```
> kalythos$Ymat <- cbind(kalythos$y, kalythos$n - kalythos$y)
```

To fit the models we use

```
> fmp <- glm(Ymat ~ x, family = binomial(link=probit), data = kalythos)
> fml <- glm(Ymat ~ x, family = binomial, data = kalythos)
```

Since the logit link is the default the parameter may be omitted on the second call. To see the results of each fit we could use

```
> summary(fmp)
> summary(fml)
```

Both models fit (all too) well. To find the LD50 estimate we can use a simple function:

```
> ld50 <- function(b) -b[1]/b[2]
> ldp <- ld50(coef(fmp)); ldl <- ld50(coef(fml)); c(ldp, ldl)
```

The actual estimates from this data are 43.663 years and 43.601 years respectively.

#### Poisson models

With the Poisson family the default link is the `log`, and in practice the major use of this family is to fit surrogate Poisson log-linear models to frequency data, whose actual distribution is often multinomial. This is a large and important subject we will not discuss further here. It even forms a major part of the use of non-gaussian generalized models overall.

Occasionally genuinely Poisson data arises in practice and in the past it was often analyzed as gaussian data after either a log or a square-root transformation. As a graceful alternative to the latter, a Poisson generalized linear model may be fitted as in the following example:

```
> fmod <- glm(y ~ A + B + x, family = poisson(link=sqrt),
              data = worm.counts)
```

#### Quasi-likelihood models

For all families the variance of the response will depend on the mean and will have the scale parameter as a multiplier. The form of dependence of the variance on the mean is a characteristic of the response distribution; for example for the Poisson distribution Var(y) = mu.

For quasi-likelihood estimation and inference the precise response distribution is not specified, but rather only a link function and the form of the variance function as it depends on the mean. Since quasi-likelihood estimation uses formally identical techniques to those for the gaussian distribution, this family provides a way of fitting gaussian models with non-standard link functions or variance functions, incidentally.

For example, consider fitting the non-linear regression y = theta_1 z_1 / (z_2 - theta_2) + e which may be written alternatively as y = 1 / (beta_1 x_1 + beta_2 x_2) + e where x_1 = z_2/z_1, x_2 = -1/z_1, beta_1 = 1/theta_1, and beta_2 = theta_2/theta_1. Supposing a suitable data frame to be set up we could fit this non-linear regression as

```
> nlfit <- glm(y ~ x1 + x2 - 1,
               family = quasi(link=inverse, variance=constant),
               data = biochem)
```

The reader is referred to the manual and the help document for further information, as needed.

### 11.7 Nonlinear least squares and maximum likelihood models

Certain forms of nonlinear model can be fitted by Generalized Linear Models (`glm()`). But in the majority of cases we have to approach the nonlinear curve fitting problem as one of nonlinear optimization. R’s nonlinear optimization routines are `optim()`, `nlm()` and `nlminb()`, We seek the parameter values that minimize some index of lack-of-fit, and they do this by trying out various parameter values iteratively. Unlike linear regression for example, there is no guarantee that the procedure will converge on satisfactory estimates. All the methods require initial guesses about what parameter values to try, and convergence may depend critically upon the quality of the starting values.

#### 11.7.1 Least squares

One way to fit a nonlinear model is by minimizing the sum of the squared errors (SSE) or residuals. This method makes sense if the observed errors could have plausibly arisen from a normal distribution.

Here is an example from Bates & Watts (1988), page 51. The data are:

```
> x <- c(0.02, 0.02, 0.06, 0.06, 0.11, 0.11, 0.22, 0.22, 0.56, 0.56,
         1.10, 1.10)
> y <- c(76, 47, 97, 107, 123, 139, 159, 152, 191, 201, 207, 200)
```

The fit criterion to be minimized is:

```
> fn <- function(p) sum((y - (p[1] * x)/(p[2] + x))^2)
```

In order to do the fit we need initial estimates of the parameters. One way to find sensible starting values is to plot the data, guess some parameter values, and superimpose the model curve using those values.

```
> plot(x, y)
> xfit <- seq(.02, 1.1, .05)
> yfit <- 200 * xfit/(0.1 + xfit)
> lines(spline(xfit, yfit))
```

We could do better, but these starting values of 200 and 0.1 seem adequate. Now do the fit:

```
> out <- nlm(fn, p = c(200, 0.1), hessian = TRUE)
```

After the fitting, `out$minimum` is the SSE, and `out$estimate` are the least squares estimates of the parameters. To obtain the approximate standard errors (SE) of the estimates we do:

```
> sqrt(diag(2*out$minimum/(length(y) - 2) * solve(out$hessian)))
```

The `2` which is subtracted in the line above represents the number of parameters. A 95% confidence interval would be the parameter estimate +/- 1.96 SE. We can superimpose the least squares fit on a new plot:

```
> plot(x, y)
> xfit <- seq(.02, 1.1, .05)
> yfit <- 212.68384222 * xfit/(0.06412146 + xfit)
> lines(spline(xfit, yfit))
```

The standard package **stats** provides much more extensive facilities for fitting non-linear models by least squares. The model we have just fitted is the Michaelis-Menten model, so we can use

```
> df <- data.frame(x=x, y=y)
> fit <- nls(y ~ SSmicmen(x, Vm, K), df)
> fit
Nonlinear regression model
  model:  y ~ SSmicmen(x, Vm, K)
   data:  df
          Vm            K
212.68370711   0.06412123
 residual sum-of-squares:  1195.449
> summary(fit)

Formula: y ~ SSmicmen(x, Vm, K)

Parameters:
    Estimate Std. Error t value Pr(>|t|)
Vm 2.127e+02  6.947e+00  30.615 3.24e-11
K  6.412e-02  8.281e-03   7.743 1.57e-05

Residual standard error: 10.93 on 10 degrees of freedom

Correlation of Parameter Estimates:
      Vm
K 0.7651
```

#### 11.7.2 Maximum likelihood

Maximum likelihood is a method of nonlinear model fitting that applies even if the errors are not normal. The method finds the parameter values which maximize the log likelihood, or equivalently which minimize the negative log-likelihood. Here is an example from Dobson (1990), pp. 108–111. This example fits a logistic model to dose-response data, which clearly could also be fit by `glm()`. The data are:

```
> x <- c(1.6907, 1.7242, 1.7552, 1.7842, 1.8113,
         1.8369, 1.8610, 1.8839)
> y <- c( 6, 13, 18, 28, 52, 53, 61, 60)
> n <- c(59, 60, 62, 56, 63, 59, 62, 60)
```

The negative log-likelihood to minimize is:

```
> fn <- function(p)
   sum( - (y*(p[1]+p[2]*x) - n*log(1+exp(p[1]+p[2]*x))
           + log(choose(n, y)) ))
```

We pick sensible starting values and do the fit:

```
> out <- nlm(fn, p = c(-50,20), hessian = TRUE)
```

After the fitting, `out$minimum` is the negative log-likelihood, and `out$estimate` are the maximum likelihood estimates of the parameters. To obtain the approximate SEs of the estimates we do:

```
> sqrt(diag(solve(out$hessian)))
```

A 95% confidence interval would be the parameter estimate +/- 1.96 SE.

### 11.8 Some non-standard models

We conclude this chapter with just a brief mention of some of the other facilities available in R for special regression and data analysis problems.

- **Mixed models.** The recommended **nlme** package provides functions `lme()` and `nlme()` for linear and non-linear mixed-effects models, that is linear and non-linear regressions in which some of the coefficients correspond to random effects. These functions make heavy use of formulae to specify the models.
- **Local approximating regressions.** The `loess()` function fits a nonparametric regression by using a locally weighted regression. Such regressions are useful for highlighting a trend in messy data or for data reduction to give some insight into a large data set. Function `loess` is in the standard package **stats**, together with code for projection pursuit regression.
- **Robust regression.** There are several functions available for fitting regression models in a way resistant to the influence of extreme outliers in the data. Function `lqs` in the recommended package **MASS** provides state-of-art algorithms for highly-resistant fits. Less resistant but statistically more efficient methods are available in packages, for example function `rlm` in package **MASS**.
- **Additive models.** This technique aims to construct a regression function from smooth additive functions of the determining variables, usually one for each determining variable. Functions `avas` and `ace` in package **acepack** and functions `bruto` and `mars` in package **mda** provide some examples of these techniques in user-contributed packages to R. An extension is **Generalized Additive Models**, implemented in user-contributed packages **gam** and **mgcv**.
- **Tree-based models.** Rather than seek an explicit global linear model for prediction or interpretation, tree-based models seek to bifurcate the data, recursively, at critical points of the determining variables in order to partition the data ultimately into groups that are as homogeneous as possible within, and as heterogeneous as possible between. The results often lead to insights that other data analysis methods tend not to yield. Models are again specified in the ordinary linear model form. The model fitting function is `tree()`, but many other generic functions such as `plot()` and `text()` are well adapted to displaying the results of a tree-based model fit in a graphical way. Tree models are available in R *via* the user-contributed packages **rpart** and **tree**.

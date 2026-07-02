---
title: "Logistic regression (part 2/3)"
source: https://en.wikipedia.org/wiki/Logistic_regression
domain: statsmodels
license: BSD-3-Clause
tags: statsmodels library, regression analysis, generalized linear model, analysis of variance
fetched: 2026-07-02
part: 2/3
---

## Interpretations

There are various equivalent specifications and interpretations of logistic regression, which fit into different types of more general models, and allow different generalizations.

### As a generalized linear model

The particular model used by logistic regression, which distinguishes it from standard linear regression and from other types of regression analysis used for binary-valued outcomes, is the way the probability of a particular outcome is linked to the linear predictor function:

$\operatorname {logit} (\operatorname {\mathbb {E} } [Y_{i}\mid x_{1,i},\ldots ,x_{m,i}])=\operatorname {logit} (p_{i})=\ln \left({\frac {p_{i}}{1-p_{i}}}\right)=\beta _{0}+\beta _{1}x_{1,i}+\cdots +\beta _{m}x_{m,i}$

Written using the more compact notation described above, this is:

$\operatorname {logit} (\operatorname {\mathbb {E} } [Y_{i}\mid \mathbf {X} _{i}])=\operatorname {logit} (p_{i})=\ln \left({\frac {p_{i}}{1-p_{i}}}\right)={\boldsymbol {\beta }}\cdot \mathbf {X} _{i}$

This formulation expresses logistic regression as a type of generalized linear model, which predicts variables with various types of probability distributions by fitting a linear predictor function of the above form to some sort of arbitrary transformation of the expected value of the variable.

The intuition for transforming using the logit function (the natural log of the odds) was explained above. It also has the practical effect of converting the probability (which is bounded to be between 0 and 1) to a variable that ranges over $(-\infty ,+\infty )$ — thereby matching the potential range of the linear prediction function on the right side of the equation.

Both the probabilities *p**i* and the regression coefficients are unobserved, and the means of determining them is not part of the model itself. They are typically determined by some sort of optimization procedure, e.g. maximum likelihood estimation, that finds values that best fit the observed data (i.e. that give the most accurate predictions for the data already observed), usually subject to regularization conditions that seek to exclude unlikely values, e.g. extremely large values for any of the regression coefficients. The use of a regularization condition is equivalent to doing maximum a posteriori (MAP) estimation, an extension of maximum likelihood. (Regularization is most commonly done using a squared regularizing function, which is equivalent to placing a zero-mean Gaussian prior distribution on the coefficients, but other regularizers are also possible.) Whether or not regularization is used, it is usually not possible to find a closed-form solution; instead, an iterative numerical method must be used, such as iteratively reweighted least squares (IRLS) or, more commonly these days, a quasi-Newton method such as the L-BFGS method.

The interpretation of the *β**j* parameter estimates is as the additive effect on the log of the odds for a unit change in the *j* the explanatory variable. In the case of a dichotomous explanatory variable, for instance, gender $e^{\beta }$ is the estimate of the odds of having the outcome for, say, males compared with females.

An equivalent formula uses the inverse of the logit function, which is the logistic function, i.e.:

$\operatorname {\mathbb {E} } [Y_{i}\mid \mathbf {X} _{i}]=p_{i}=\operatorname {logit} ^{-1}({\boldsymbol {\beta }}\cdot \mathbf {X} _{i})={\frac {1}{1+e^{-{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}$

The formula can also be written as a probability distribution (specifically, using a probability mass function):

$\Pr(Y_{i}=y\mid \mathbf {X} _{i})={p_{i}}^{y}(1-p_{i})^{1-y}=\left({\frac {e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}{1+e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}\right)^{y}\left(1-{\frac {e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}{1+e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}\right)^{1-y}={\frac {e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}\cdot y}}{1+e^{{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}$

### As a latent-variable model

The logistic model has an equivalent formulation as a latent-variable model. This formulation is common in the theory of discrete choice models and makes it easier to extend to certain more complicated models with multiple, correlated choices, as well as to compare logistic regression to the closely related probit model.

Imagine that, for each trial *i*, there is a continuous latent variable *Y**i** (i.e. an unobserved random variable) that is distributed as follows:

$Y_{i}^{\ast }={\boldsymbol {\beta }}\cdot \mathbf {X} _{i}+\varepsilon _{i}\,$

where

$\varepsilon _{i}\sim \operatorname {Logistic} (0,1)\,$

i.e. the latent variable can be written directly in terms of the linear predictor function and an additive random error variable that is distributed according to a standard logistic distribution.

Then *Y**i* can be viewed as an indicator for whether this latent variable is positive:

$Y_{i}={\begin{cases}1&{\text{if }}Y_{i}^{\ast }>0\ {\text{ i.e. }}{-\varepsilon _{i}}<{\boldsymbol {\beta }}\cdot \mathbf {X} _{i},\\0&{\text{otherwise.}}\end{cases}}$

The choice of modeling the error variable specifically with a standard logistic distribution, rather than a general logistic distribution with the location and scale set to arbitrary values, seems restrictive, but in fact, it is not. It must be kept in mind that we can choose the regression coefficients ourselves, and very often can use them to offset changes in the parameters of the error variable's distribution. For example, a logistic error-variable distribution with a non-zero location parameter *μ* (which sets the mean) is equivalent to a distribution with a zero location parameter, where *μ* has been added to the intercept coefficient. Both situations produce the same value for *Y**i** regardless of settings of explanatory variables. Similarly, an arbitrary scale parameter *s* is equivalent to setting the scale parameter to 1 and then dividing all regression coefficients by *s*. In the latter case, the resulting value of *Y**i**** will be smaller by a factor of *s* than in the former case, for all sets of explanatory variables — but critically, it will always remain on the same side of 0, and hence lead to the same *Y**i* choice.

(This predicts that the irrelevancy of the scale parameter may not carry over into more complex models where more than two choices are available.)

It turns out that this formulation is exactly equivalent to the preceding one, phrased in terms of the generalized linear model and without any latent variables. This can be shown as follows, using the fact that the cumulative distribution function (CDF) of the standard logistic distribution is the logistic function, which is the inverse of the logit function, i.e.

$\Pr(\varepsilon _{i}<x)=\operatorname {logit} ^{-1}(x)$

Then:

${\begin{aligned}\Pr(Y_{i}=1\mid \mathbf {X} _{i})&=\Pr(Y_{i}^{\ast }>0\mid \mathbf {X} _{i})\\[5pt]&=\Pr({\boldsymbol {\beta }}\cdot \mathbf {X} _{i}+\varepsilon _{i}>0)\\[5pt]&=\Pr(\varepsilon _{i}>-{\boldsymbol {\beta }}\cdot \mathbf {X} _{i})\\[5pt]&=\Pr(\varepsilon _{i}<{\boldsymbol {\beta }}\cdot \mathbf {X} _{i})&&{\text{(because the logistic distribution is symmetric)}}\\[5pt]&=\operatorname {logit} ^{-1}({\boldsymbol {\beta }}\cdot \mathbf {X} _{i})&\\[5pt]&=p_{i}&&{\text{(see above)}}\end{aligned}}$

This formulation—which is standard in discrete choice models—makes clear the relationship between logistic regression (the "logit model") and the probit model, which uses an error variable distributed according to a standard normal distribution instead of a standard logistic distribution. Both the logistic and normal distributions are symmetric with a basic unimodal, "bell curve" shape. The only difference is that the logistic distribution has somewhat heavier tails, which means that it is less sensitive to outlying data (and hence somewhat more robust to model mis-specifications or erroneous data).

### Two-way latent-variable model

Yet another formulation uses two separate latent variables:

${\begin{aligned}Y_{i}^{0\ast }&={\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}+\varepsilon _{0}\,\\Y_{i}^{1\ast }&={\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}+\varepsilon _{1}\,\end{aligned}}$

where

${\begin{aligned}\varepsilon _{0}&\sim \operatorname {EV} _{1}(0,1)\\\varepsilon _{1}&\sim \operatorname {EV} _{1}(0,1)\end{aligned}}$

where *EV*1(0,1) is a standard type-1 extreme value distribution: i.e.

$\Pr(\varepsilon _{0}=x)=\Pr(\varepsilon _{1}=x)=e^{-x}e^{-e^{-x}}$

Then

$Y_{i}={\begin{cases}1&{\text{if }}Y_{i}^{1\ast }>Y_{i}^{0\ast },\\0&{\text{otherwise.}}\end{cases}}$

This model has a separate latent variable and a separate set of regression coefficients for each possible outcome of the dependent variable. The reason for this separation is that it makes it easy to extend logistic regression to multi-outcome categorical variables, as in the multinomial logit model. In such a model, it is natural to model each possible outcome using a different set of regression coefficients. It is also possible to motivate each of the separate latent variables as the theoretical utility associated with making the associated choice, and thus motivate logistic regression in terms of utility theory. (In terms of utility theory, a rational actor always chooses the choice with the greatest associated utility.) This is the approach taken by economists when formulating discrete choice models, because it both provides a theoretically strong foundation and facilitates intuitions about the model, which in turn makes it easy to consider various sorts of extensions. (See the example below.)

The choice of the type-1 extreme value distribution seems fairly arbitrary, but it makes the mathematics work out, and it may be possible to justify its use through rational choice theory.

It turns out that this model is equivalent to the previous model, although this seems non-obvious, since there are now two sets of regression coefficients and error variables, and the error variables have a different distribution. In fact, this model reduces directly to the previous one with the following substitutions:

${\boldsymbol {\beta }}={\boldsymbol {\beta }}_{1}-{\boldsymbol {\beta }}_{0}$

$\varepsilon =\varepsilon _{1}-\varepsilon _{0}$

An intuition for this comes from the fact that, since we choose based on the maximum of two values, only their difference matters, not the exact values — and this effectively removes one degree of freedom. Another critical fact is that the difference of two type-1 extreme-value-distributed variables is a logistic distribution, i.e. $\varepsilon =\varepsilon _{1}-\varepsilon _{0}\sim \operatorname {Logistic} (0,1).$ We can demonstrate the equivalent as follows:

${\begin{aligned}\Pr(Y_{i}=1\mid \mathbf {X} _{i})={}&\Pr \left(Y_{i}^{1\ast }>Y_{i}^{0\ast }\mid \mathbf {X} _{i}\right)&\\[5pt]={}&\Pr \left(Y_{i}^{1\ast }-Y_{i}^{0\ast }>0\mid \mathbf {X} _{i}\right)&\\[5pt]={}&\Pr \left({\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}+\varepsilon _{1}-\left({\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}+\varepsilon _{0}\right)>0\right)&\\[5pt]={}&\Pr \left(({\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}-{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i})+(\varepsilon _{1}-\varepsilon _{0})>0\right)&\\[5pt]={}&\Pr(({\boldsymbol {\beta }}_{1}-{\boldsymbol {\beta }}_{0})\cdot \mathbf {X} _{i}+(\varepsilon _{1}-\varepsilon _{0})>0)&\\[5pt]={}&\Pr(({\boldsymbol {\beta }}_{1}-{\boldsymbol {\beta }}_{0})\cdot \mathbf {X} _{i}+\varepsilon >0)&&{\text{(substitute }}\varepsilon {\text{ as above)}}\\[5pt]={}&\Pr({\boldsymbol {\beta }}\cdot \mathbf {X} _{i}+\varepsilon >0)&&{\text{(substitute }}{\boldsymbol {\beta }}{\text{ as above)}}\\[5pt]={}&\Pr(\varepsilon >-{\boldsymbol {\beta }}\cdot \mathbf {X} _{i})&&{\text{(now, same as above model)}}\\[5pt]={}&\Pr(\varepsilon <{\boldsymbol {\beta }}\cdot \mathbf {X} _{i})&\\[5pt]={}&\operatorname {logit} ^{-1}({\boldsymbol {\beta }}\cdot \mathbf {X} _{i})\\[5pt]={}&p_{i}\end{aligned}}$

### As a "log-linear" model

Yet another formulation combines the two-way latent variable formulation above with the original formulation higher up without latent variables, and in the process provides a link to one of the standard formulations of the multinomial logit.

Here, instead of writing the logit of the probabilities *p**i* as a linear predictor, we separate the linear predictor into two, one for each of the two outcomes:

${\begin{aligned}\ln \Pr(Y_{i}=0)&={\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}-\ln Z\\\ln \Pr(Y_{i}=1)&={\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}-\ln Z\end{aligned}}$

Two separate sets of regression coefficients have been introduced, just as in the two-way latent variable model, and the two equations appear a form that writes the logarithm of the associated probability as a linear predictor, with an extra term $-\ln Z$ at the end. This term, as it turns out, serves as the normalizing factor ensuring that the result is a distribution. This can be seen by exponentiating both sides:

${\begin{aligned}\Pr(Y_{i}=0)&={\frac {1}{Z}}e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}\\[5pt]\Pr(Y_{i}=1)&={\frac {1}{Z}}e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}\end{aligned}}$

In this form it is clear that the purpose of *Z* is to ensure that the resulting distribution over *Y**i* is in fact a probability distribution, i.e. it sums to 1. This means that *Z* is simply the sum of all un-normalized probabilities, and by dividing each probability by *Z*, the probabilities become "normalized". That is:

$Z=e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}$

and the resulting equations are

${\begin{aligned}\Pr(Y_{i}=0)&={\frac {e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}}{e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}}\\[5pt]\Pr(Y_{i}=1)&={\frac {e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}{e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}}.\end{aligned}}$

Or generally:

$\Pr(Y_{i}=c)={\frac {e^{{\boldsymbol {\beta }}_{c}\cdot \mathbf {X} _{i}}}{\sum _{h}e^{{\boldsymbol {\beta }}_{h}\cdot \mathbf {X} _{i}}}}$

This shows clearly how to generalize this formulation to more than two outcomes, as in multinomial logit. This general formulation is exactly the softmax function as in

$\Pr(Y_{i}=c)=\operatorname {softmax} (c,{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i},{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i},\dots ).$

To prove that this is equivalent to the previous model, we start by recognizing the above model is overspecified, in that $\Pr(Y_{i}=0)$ and $\Pr(Y_{i}=1)$ cannot be independently specified: rather $\Pr(Y_{i}=0)+\Pr(Y_{i}=1)=1$ so knowing one automatically determines the other. As a result, the model is nonidentifiable, in that multiple combinations of ${\boldsymbol {\beta }}_{0}$ and ${\boldsymbol {\beta }}_{1}$ will produce the same probabilities for all possible explanatory variables. In fact, it can be seen that adding any constant vector to both of them will produce the same probabilities:

${\begin{aligned}\Pr(Y_{i}=1)&={\frac {e^{({\boldsymbol {\beta }}_{1}+\mathbf {C} )\cdot \mathbf {X} _{i}}}{e^{({\boldsymbol {\beta }}_{0}+\mathbf {C} )\cdot \mathbf {X} _{i}}+e^{({\boldsymbol {\beta }}_{1}+\mathbf {C} )\cdot \mathbf {X} _{i}}}}\\[5pt]&={\frac {e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}e^{\mathbf {C} \cdot \mathbf {X} _{i}}}{e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}e^{\mathbf {C} \cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}e^{\mathbf {C} \cdot \mathbf {X} _{i}}}}\\[5pt]&={\frac {e^{\mathbf {C} \cdot \mathbf {X} _{i}}e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}{e^{\mathbf {C} \cdot \mathbf {X} _{i}}(e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}})}}\\[5pt]&={\frac {e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}{e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}}.\end{aligned}}$

As a result, we can simplify matters, and restore identifiability, by picking an arbitrary value for one of the two vectors. We choose to set ${\boldsymbol {\beta }}_{0}=\mathbf {0} .$ Then,

$e^{{\boldsymbol {\beta }}_{0}\cdot \mathbf {X} _{i}}=e^{\mathbf {0} \cdot \mathbf {X} _{i}}=1$

and so

$\Pr(Y_{i}=1)={\frac {e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}{1+e^{{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}}={\frac {1}{1+e^{-{\boldsymbol {\beta }}_{1}\cdot \mathbf {X} _{i}}}}=p_{i}$

which shows that this formulation is indeed equivalent to the previous formulation. (As in the two-way latent variable formulation, any settings where ${\boldsymbol {\beta }}={\boldsymbol {\beta }}_{1}-{\boldsymbol {\beta }}_{0}$ will produce equivalent results.)

Most treatments of the multinomial logit model start out either by extending the "log-linear" formulation presented here or the two-way latent variable formulation presented above, since both clearly show the way that the model could be extended to multi-way outcomes. In general, the presentation with latent variables is more common in econometrics and political science, where discrete choice models and utility theory reign, while the "log-linear" formulation here is more common in computer science, e.g. machine learning and natural language processing.

### As a single-layer perceptron

The model has an equivalent formulation

$p_{i}={\frac {1}{1+e^{-(\beta _{0}+\beta _{1}x_{1,i}+\cdots +\beta _{k}x_{k,i})}}}.\,$

This functional form is commonly called a single-layer perceptron or single-layer artificial neural network. A single-layer neural network computes a continuous output instead of a step function. The derivative of *pi* with respect to *X* = (*x*1, ..., *x**k*) is computed from the general form:

$y={\frac {1}{1+e^{-f(X)}}}$

where *f*(*X*) is an analytic function in *X*. With this choice, the single-layer neural network is identical to the logistic regression model. This function has a continuous derivative, which allows it to be used in backpropagation. This function is also preferred because its derivative is easily calculated:

${\frac {\mathrm {d} y}{\mathrm {d} X}}=y(1-y){\frac {\mathrm {d} f}{\mathrm {d} X}}.\,$

### In terms of binomial data

A closely related model assumes that each *i* is associated not with a single Bernoulli trial but with *n**i* independent identically distributed trials, where the observation *Y**i* is the number of successes observed (the sum of the individual Bernoulli-distributed random variables), and hence follows a binomial distribution:

$Y_{i}\,\sim \operatorname {Bin} (n_{i},p_{i}),{\text{ for }}i=1,\dots ,n$

An example of this distribution is the fraction of seeds (*p**i*) that germinate after *n**i* are planted.

In terms of expected values, this model is expressed as follows:

$p_{i}=\operatorname {\mathbb {E} } \left[\left.{\frac {Y_{i}}{n_{i}}}\,\right|\,\mathbf {X} _{i}\right]\,,$

so that

$\operatorname {logit} \left(\operatorname {\mathbb {E} } \left[\left.{\frac {Y_{i}}{n_{i}}}\,\right|\,\mathbf {X} _{i}\right]\right)=\operatorname {logit} (p_{i})=\ln \left({\frac {p_{i}}{1-p_{i}}}\right)={\boldsymbol {\beta }}\cdot \mathbf {X} _{i}\,,$

Or equivalently:

$\Pr(Y_{i}=y\mid \mathbf {X} _{i})={n_{i} \choose y}p_{i}^{y}(1-p_{i})^{n_{i}-y}={n_{i} \choose y}\left({\frac {1}{1+e^{-{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}\right)^{y}\left(1-{\frac {1}{1+e^{-{\boldsymbol {\beta }}\cdot \mathbf {X} _{i}}}}\right)^{n_{i}-y}\,.$

This model can be fit using the same sorts of methods as the above more basic model.


## Model fitting

### Maximum likelihood estimation (MLE)

The regression coefficients are usually estimated using maximum likelihood estimation. Unlike linear regression with normally distributed residuals, it is not possible to find a closed-form expression for the coefficient values that maximize the likelihood function so an iterative process must be used instead; for example Newton's method. This process begins with a tentative solution, revises it slightly to see if it can be improved, and repeats this revision until no more improvement is made, at which point the process is said to have converged.

In some instances, the model may not reach convergence. Non-convergence of a model indicates that the coefficients are not meaningful because the iterative process was unable to find appropriate solutions. A failure to converge may occur for a number of reasons: having a large ratio of predictors to cases, multicollinearity, sparseness, or complete separation.

- Having a large ratio of variables to cases results in an overly conservative Wald statistic (discussed below) and can lead to non-convergence. Regularized logistic regression is specifically intended to be used in this situation.
- Multicollinearity refers to unacceptably high correlations between predictors. As multicollinearity increases, coefficients remain unbiased but standard errors increase and the likelihood of model convergence decreases. To detect multicollinearity amongst the predictors, one can conduct a linear regression analysis with the predictors of interest for the sole purpose of examining the tolerance statistic used to assess whether multicollinearity is unacceptably high.
- Sparseness in the data refers to having a large proportion of empty cells (cells with zero counts). Zero cell counts are particularly problematic with categorical predictors. With continuous predictors, the model can infer values for the zero cell counts, but this is not the case with categorical predictors. The model will not converge with zero cell counts for categorical predictors because the natural logarithm of zero is an undefined value so that the final solution to the model cannot be reached. To remedy this problem, researchers may collapse categories in a theoretically meaningful way or add a constant to all cells.
- Another numerical problem that may lead to a lack of convergence is complete separation, which refers to the instance in which the predictors perfectly predict the criterion – all cases are accurately classified and the likelihood maximized with infinite coefficients. In such instances, one should re-examine the data, as there may be some kind of error.
- One can also take semi-parametric or non-parametric approaches, e.g., via local-likelihood or nonparametric quasi-likelihood methods, which avoid assumptions of a parametric form for the index function and is robust to the choice of the link function (e.g., probit or logit).

### Iteratively reweighted least squares (IRLS)

Binary logistic regression ( $y=0$ or $y=1$ ) can, for example, be calculated using *iteratively reweighted least squares* (IRLS), which is equivalent to maximizing the log-likelihood of a Bernoulli distributed process using Newton's method. If the problem is written in vector matrix form, with parameters $\mathbf {w} ^{T}=[\beta _{0},\beta _{1},\beta _{2},\ldots ]$ , explanatory variables $\mathbf {x} (i)=[1,x_{1}(i),x_{2}(i),\ldots ]^{T}$ and expected value of the Bernoulli distribution $\mu (i)={\frac {1}{1+e^{-\mathbf {w} ^{T}\mathbf {x} (i)}}}$ , the parameters $\mathbf {w}$ can be found using the following iterative algorithm:

$\mathbf {w} _{k+1}=\left(\mathbf {X} ^{T}\mathbf {S} _{k}\mathbf {X} \right)^{-1}\mathbf {X} ^{T}\left(\mathbf {S} _{k}\mathbf {X} \mathbf {w} _{k}+\mathbf {y} -\mathbf {\boldsymbol {\mu }} _{k}\right)$

where $\mathbf {S} =\operatorname {diag} (\mu (i)(1-\mu (i)))$ is a diagonal weighting matrix, ${\boldsymbol {\mu }}=[\mu (1),\mu (2),\ldots ]$ the vector of expected values,

$\mathbf {X} ={\begin{bmatrix}1&x_{1}(1)&x_{2}(1)&\ldots \\1&x_{1}(2)&x_{2}(2)&\ldots \\\vdots &\vdots &\vdots \end{bmatrix}}$

the regressor matrix and $\mathbf {y} (i)=[y(1),y(2),\ldots ]^{T}$ the vector of response variables. More details can be found in the literature.

### Bayesian

In a Bayesian statistics context, prior distributions are normally placed on the regression coefficients, for example in the form of Gaussian distributions. There is no conjugate prior of the likelihood function in logistic regression. When Bayesian inference was performed analytically, this made the posterior distribution difficult to calculate except in very low dimensions. Now, though, automatic software such as OpenBUGS, JAGS, PyMC, Stan or Turing.jl allows these posteriors to be computed using simulation, so lack of conjugacy is not a concern. However, when the sample size or the number of parameters is large, full Bayesian simulation can be slow, and people often use approximate methods such as variational Bayesian methods and expectation propagation.

### "Rule of ten"

Widely used, the "one in ten rule", states that logistic regression models give stable values for the explanatory variables if based on a minimum of about 10 events per explanatory variable (EPV); where *event* denotes the cases belonging to the less frequent category in the dependent variable. Thus a study designed to use k explanatory variables for an event (e.g. myocardial infarction) expected to occur in a proportion p of participants in the study will require a total of $10k/p$ participants. However, there is considerable debate about the reliability of this rule, which is based on simulation studies and lacks a secure theoretical underpinning. According to some authors the rule is overly conservative in some circumstances, with the authors stating, "If we (somewhat subjectively) regard confidence interval coverage less than 93 percent, type I error greater than 7 percent, or relative bias greater than 15 percent as problematic, our results indicate that problems are fairly frequent with 2–4 EPV, uncommon with 5–9 EPV, and still observed with 10–16 EPV. The worst instances of each problem were not severe with 5–9 EPV and usually comparable to those with 10–16 EPV".

Others have found results that are not consistent with the above, using different criteria. A useful criterion is whether the fitted model will be expected to achieve the same predictive discrimination in a new sample as it appeared to achieve in the model development sample. For that criterion, 20 events per candidate variable may be required. Also, one can argue that 96 observations are needed only to estimate the model's intercept precisely enough that the margin of error in predicted probabilities is ±0.1 with a 0.95 confidence level.


## Error and significance of fit

### Deviance and likelihood ratio test ─ a simple case

In any fitting procedure, the addition of another fitting parameter to a model (e.g. the beta parameters in a logistic regression model) will almost always improve the ability of the model to predict the measured outcomes. This will be true even if the additional term has no predictive value, since the model will simply be "overfitting" to the noise in the data. The question arises as to whether the improvement gained by the addition of another fitting parameter is significant enough to recommend the inclusion of the additional term, or whether the improvement is simply that which may be expected from overfitting.

In short, for logistic regression, a statistic known as the deviance is defined which is a measure of the error between the logistic model fit and the outcome data. In the limit of a large number of data points, the deviance is chi-squared distributed, which allows a chi-squared test to be implemented in order to determine the significance of the explanatory variables.

Linear regression and logistic regression have many similarities. For example, in simple linear regression, a set of *K* data points (*xk*, *yk*) are fitted to a proposed model function of the form $y=b_{0}+b_{1}x$ . The fit is obtained by choosing the *b* parameters which minimize the sum of the squares of the residuals (the squared error term) for each data point:

$\varepsilon ^{2}=\sum _{k=1}^{K}(b_{0}+b_{1}x_{k}-y_{k})^{2}.$

The minimum value which constitutes the fit will be denoted by ${\hat {\varepsilon }}^{2}$

The idea of a null model may be introduced, in which it is assumed that the *x* variable is of no use in predicting the yk outcomes: The data points are fitted to a null model function of the form *y* = *b*0 with a squared error term:

$\varepsilon ^{2}=\sum _{k=1}^{K}(b_{0}-y_{k})^{2}.$

The fitting process consists of choosing a value of *b*0 which minimizes $\varepsilon ^{2}$ of the fit to the null model, denoted by $\varepsilon _{\varphi }^{2}$ where the $\varphi$ subscript denotes the null model. It is seen that the null model is optimized by $b_{0}={\overline {y}}$ where ${\overline {y}}$ is the mean of the *yk* values, and the optimized $\varepsilon _{\varphi }^{2}$ is:

${\hat {\varepsilon }}_{\varphi }^{2}=\sum _{k=1}^{K}({\overline {y}}-y_{k})^{2}$

which is proportional to the square of the (uncorrected) sample standard deviation of the *yk* data points.

We can imagine a case where the *yk* data points are randomly assigned to the various *xk*, and then fitted using the proposed model. Specifically, we can consider the fits of the proposed model to every permutation of the *yk* outcomes. It can be shown that the optimized error of any of these fits will never be less than the optimum error of the null model, and that the difference between these minimum error will follow a chi-squared distribution, with degrees of freedom equal those of the proposed model minus those of the null model which, in this case, will be $2-1=1$ . Using the chi-squared test, we may then estimate how many of these permuted sets of *yk* will yield a minimum error less than or equal to the minimum error using the original *yk*, and so we can estimate how significant an improvement is given by the inclusion of the *x* variable in the proposed model.

For logistic regression, the measure of goodness-of-fit is the likelihood function *L*, or its logarithm, the log-likelihood *ℓ*. The likelihood function *L* is analogous to the $\varepsilon ^{2}$ in the linear regression case, except that the likelihood is maximized rather than minimized. Denote the maximized log-likelihood of the proposed model by ${\hat {\ell }}$ .

In the case of simple binary logistic regression, the set of *K* data points are fitted in a probabilistic sense to a function of the form:

$p(x)={\frac {1}{1+e^{-t}}}$

where ⁠ $p(x)$ ⁠ is the probability that $y=1$ . The log-odds are given by:

$t=\beta _{0}+\beta _{1}x$

and the log-likelihood is:

$\ell =\sum _{k=1}^{K}\left(y_{k}\ln(p(x_{k}))+(1-y_{k})\ln(1-p(x_{k}))\right)$

For the null model, the probability that $y=1$ is given by:

$p_{\varphi }(x)={\frac {1}{1+e^{-t_{\varphi }}}}$

The log-odds for the null model are given by:

$t_{\varphi }=\beta _{0}$

and the log-likelihood is:

$\ell _{\varphi }=\sum _{k=1}^{K}\left(y_{k}\ln(p_{\varphi })+(1-y_{k})\ln(1-p_{\varphi })\right)$

Since we have $p_{\varphi }={\overline {y}}$ at the maximum of *L*, the maximum log-likelihood for the null model is

${\hat {\ell }}_{\varphi }=K(\,{\overline {y}}\ln({\overline {y}})+(1-{\overline {y}})\ln(1-{\overline {y}}))$

The optimum $\beta _{0}$ is:

$\beta _{0}=\ln \left({\frac {\overline {y}}{1-{\overline {y}}}}\right)$

where ${\overline {y}}$ is again the mean of the *yk* values. Again, we can conceptually consider the fit of the proposed model to every permutation of the *yk* and it can be shown that the maximum log-likelihood of these permutation fits will never be smaller than that of the null model:

${\hat {\ell }}\geq {\hat {\ell }}_{\varphi }$

Also, as an analog to the error of the linear regression case, we may define the deviance of a logistic regression fit as:

$D=\ln \left({\frac {{\hat {L}}^{2}}{{\hat {L}}_{\varphi }^{2}}}\right)=2({\hat {\ell }}-{\hat {\ell }}_{\varphi })$

which will always be positive or zero. The reason for this choice is that not only is the deviance a good measure of the goodness of fit, it is also approximately chi-squared distributed, with the approximation improving as the number of data points (*K*) increases, becoming exactly chi-square distributed in the limit of an infinite number of data points. As in the case of linear regression, we may use this fact to estimate the probability that a random set of data points will give a better fit than the fit obtained by the proposed model, and so have an estimate how significantly the model is improved by including the *xk* data points in the proposed model.

For the simple model of student test scores described above, the maximum value of the log-likelihood of the null model is ${\hat {\ell }}_{\varphi }=-13.8629\ldots$ The maximum value of the log-likelihood for the simple model is ${\hat {\ell }}=-8.02988\ldots$ so that the deviance is $D=2({\hat {\ell }}-{\hat {\ell }}_{\varphi })=11.6661\ldots$

Using the chi-squared test of significance, the integral of the chi-squared distribution with one degree of freedom from 11.6661... to infinity is equal to 0.00063649...

This effectively means that about 6 out of a 10,000 fits to random *yk* can be expected to have a better fit (smaller deviance) than the given *yk* and so we can conclude that the inclusion of the *x* variable and data in the proposed model is a very significant improvement over the null model. In other words, we reject the null hypothesis with $1-D\approx 99.94\%$ confidence.

### Goodness of fit summary

Goodness of fit in linear regression models is generally measured using R2. Since this has no direct analog in logistic regression, various methods including the following can be used instead.

#### Deviance and likelihood ratio tests

In linear regression analysis, one is concerned with partitioning variance via the sum of squares calculations – variance in the criterion is essentially divided into variance accounted for by the predictors and residual variance. In logistic regression analysis, deviance is used in lieu of a sum of squares calculations. Deviance is analogous to the sum of squares calculations in linear regression and is a measure of the lack of fit to the data in a logistic regression model. When a "saturated" model is available (a model with a theoretically perfect fit), deviance is calculated by comparing a given model with the saturated model. This computation gives the likelihood-ratio test:

$D=-2\ln {\frac {\text{likelihood of the fitted model}}{\text{likelihood of the saturated model}}}.$

In the above equation, D represents the deviance and ln represents the natural logarithm. The log of this likelihood ratio (the ratio of the fitted model to the saturated model) will produce a negative value, hence the need for a negative sign. D can be shown to follow an approximate chi-squared distribution. Smaller values indicate better fit as the fitted model deviates less from the saturated model. When assessed upon a chi-square distribution, nonsignificant chi-square values indicate very little unexplained variance and thus, good model fit. Conversely, a significant chi-square value indicates that a significant amount of the variance is unexplained.

When the saturated model is not available (a common case), deviance is calculated simply as −2·(log likelihood of the fitted model), and the reference to the saturated model's log likelihood can be removed from all that follows without harm.

Two measures of deviance are particularly important in logistic regression: null deviance and model deviance. The null deviance represents the difference between a model with only the intercept (which means "no predictors") and the saturated model. The model deviance represents the difference between a model with at least one predictor and the saturated model. In this respect, the null model provides a baseline upon which to compare predictor models. Given that deviance is a measure of the difference between a given model and the saturated model, smaller values indicate better fit. Thus, to assess the contribution of a predictor or set of predictors, one can subtract the model deviance from the null deviance and assess the difference on a $\chi _{s-p}^{2},$ chi-square distribution with degrees of freedom equal to the difference in the number of parameters estimated.

Let

${\begin{aligned}D_{\text{null}}&=-2\ln {\frac {\text{likelihood of null model}}{\text{likelihood of the saturated model}}}\\[6pt]D_{\text{fitted}}&=-2\ln {\frac {\text{likelihood of fitted model}}{\text{likelihood of the saturated model}}}.\end{aligned}}$

Then the difference of both is:

${\begin{aligned}D_{\text{null}}-D_{\text{fitted}}&=-2\left(\ln {\frac {\text{likelihood of null model}}{\text{likelihood of the saturated model}}}-\ln {\frac {\text{likelihood of fitted model}}{\text{likelihood of the saturated model}}}\right)\\[6pt]&=-2\ln {\frac {\left({\dfrac {\text{likelihood of null model}}{\text{likelihood of the saturated model}}}\right)}{\left({\dfrac {\text{likelihood of fitted model}}{\text{likelihood of the saturated model}}}\right)}}\\[6pt]&=-2\ln {\frac {\text{likelihood of the null model}}{\text{likelihood of fitted model}}}.\end{aligned}}$

If the model deviance is significantly smaller than the null deviance then one can conclude that the predictor or set of predictors significantly improve the model's fit. This is analogous to the F-test used in linear regression analysis to assess the significance of prediction.

#### Pseudo-R-squared

In linear regression the squared multiple correlation, R2 is used to assess goodness of fit as it represents the proportion of variance in the criterion that is explained by the predictors. In logistic regression analysis, there is no agreed upon analogous measure, but there are several competing measures each with limitations.

Four of the most commonly used indices and one less commonly used one are examined on this page:

- Likelihood ratio R2L
- Cox and Snell R2CS
- Nagelkerke R2N
- McFadden R2McF
- Tjur R2T

#### Hosmer–Lemeshow test

The Hosmer–Lemeshow test uses a test statistic that asymptotically follows a $\chi ^{2}$ distribution to assess whether or not the observed event rates match expected event rates in subgroups of the model population. This test is considered to be obsolete by some statisticians because of its dependence on arbitrary binning of predicted probabilities and relative low power.

### Coefficient significance

After fitting the model, it is likely that researchers will want to examine the contribution of individual predictors. To do so, they will want to examine the regression coefficients. In linear regression, the regression coefficients represent the change in the criterion for each unit change in the predictor. In logistic regression, however, the regression coefficients represent the change in the logit for each unit change in the predictor. Given that the logit is not intuitive, researchers are likely to focus on a predictor's effect on the exponential function of the regression coefficient – the odds ratio (see definition). In linear regression, the significance of a regression coefficient is assessed by computing a *t* test. In logistic regression, there are several different tests designed to assess the significance of an individual predictor, most notably the likelihood ratio test and the Wald statistic.

#### Likelihood ratio test

The likelihood-ratio test discussed above to assess model fit is also the recommended procedure to assess the contribution of individual "predictors" to a given model. In the case of a single predictor model, one simply compares the deviance of the predictor model with that of the null model on a chi-square distribution with a single degree of freedom. If the predictor model has significantly smaller deviance (c.f. chi-square using the difference in degrees of freedom of the two models), then one can conclude that there is a significant association between the "predictor" and the outcome. Although some common statistical packages (e.g. SPSS) do provide likelihood ratio test statistics, without this computationally intensive test it would be more difficult to assess the contribution of individual predictors in the multiple logistic regression case. To assess the contribution of individual predictors one can enter the predictors hierarchically, comparing each new model with the previous to determine the contribution of each predictor. There is some debate among statisticians about the appropriateness of so-called "stepwise" procedures. The fear is that they may not preserve nominal statistical properties and may become misleading.

#### Wald statistic

Alternatively, when assessing the contribution of individual predictors in a given model, one may examine the significance of the Wald statistic. The Wald statistic, analogous to the *t*-test in linear regression, is used to assess the significance of coefficients. The Wald statistic is the ratio of the square of the regression coefficient to the square of the standard error of the coefficient and is asymptotically distributed as a chi-square distribution.

$W_{j}={\frac {\beta _{j}^{2}}{SE_{\beta _{j}}^{2}}}$

Although several statistical packages (e.g., SPSS, SAS) report the Wald statistic to assess the contribution of individual predictors, the Wald statistic has limitations. When the regression coefficient is large, the standard error of the regression coefficient also tends to be larger increasing the probability of Type-II error. The Wald statistic also tends to be biased when data are sparse.

#### Case-control sampling

Suppose cases are rare. Then we might wish to sample them more frequently than their prevalence in the population. For example, suppose there is a disease that affects 1 person in 10,000 and to collect our data we need to do a complete physical. It may be too expensive to do thousands of physicals of healthy people in order to obtain data for only a few diseased individuals. Thus, we may evaluate more diseased individuals, perhaps all of the rare outcomes. This is also retrospective sampling, or equivalently it is called unbalanced data. As a rule of thumb, sampling controls at a rate of five times the number of cases will produce sufficient control data.

Logistic regression is unique in that it may be estimated on unbalanced data, rather than randomly sampled data, and still yield correct coefficient estimates of the effects of each independent variable on the outcome. That is to say, if we form a logistic model from such data, if the model is correct in the general population, the $\beta _{j}$ parameters are all correct except for $\beta _{0}$ . We can correct $\beta _{0}$ if we know the true prevalence as follows:

${\widehat {\beta }}_{0}^{*}={\widehat {\beta }}_{0}+\log {\frac {\pi }{1-\pi }}-\log {{\tilde {\pi }} \over {1-{\tilde {\pi }}}}$

where $\pi$ is the true prevalence and ${\tilde {\pi }}$ is the prevalence in the sample.


## Discussion

Like other forms of regression analysis, logistic regression makes use of one or more predictor variables that may be either continuous or categorical. Unlike ordinary linear regression, however, logistic regression is used for predicting dependent variables that take membership in one of a limited number of categories (treating the dependent variable in the binomial case as the outcome of a Bernoulli trial) rather than a continuous outcome. Given this difference, the assumptions of linear regression are violated. In particular, the residuals cannot be normally distributed. In addition, linear regression may make nonsensical predictions for a binary dependent variable. What is needed is a way to convert a binary variable into a continuous one that can take on any real value (negative or positive). To do that, binomial logistic regression first calculates the odds of the event happening for different levels of each independent variable, and then takes its logarithm to create a continuous criterion as a transformed version of the dependent variable. The logarithm of the odds is the logit of the probability, the logit is defined as follows: $\operatorname {logit} p=\ln {\frac {p}{1-p}}\quad {\text{for }}0<p<1\,.$

Although the dependent variable in logistic regression is Bernoulli, the logit is on an unrestricted scale. The logit function is the link function in this kind of generalized linear model, i.e. $\operatorname {logit} \operatorname {\mathcal {E}} (Y)=\beta _{0}+\beta _{1}x$

Y is the Bernoulli-distributed response variable and x is the predictor variable; the β values are the linear parameters.

The logit of the probability of success is then fitted to the predictors. The predicted value of the logit is converted back into predicted odds, via the inverse of the natural logarithm – the exponential function. Thus, although the observed dependent variable in binary logistic regression is a 0-or-1 variable, the logistic regression estimates the odds, as a continuous variable, that the dependent variable is a 'success'. In some applications, the odds are all that is needed. In others, a specific yes-or-no prediction is needed for whether the dependent variable is or is not a 'success'; this categorical prediction can be based on the computed odds of success, with predicted odds above some chosen cutoff value being translated into a prediction of success.


## Machine learning and cross-entropy loss function

In machine learning applications where logistic regression is used for binary classification, the MLE minimises the cross-entropy loss function.

Logistic regression is an important machine learning algorithm. The goal is to model the probability of a random variable Y being 0 or 1 given experimental data.

Consider a generalized linear model function parameterized by $\theta$ ,

$h_{\theta }(X)={\frac {1}{1+e^{-\theta ^{T}X}}}=\Pr(Y=1\mid X;\theta )$

Therefore,

$\Pr(Y=0\mid X;\theta )=1-h_{\theta }(X)$

and since $Y\in \{0,1\}$ , we see that $\Pr(y\mid X;\theta )$ is given by $\Pr(y\mid X;\theta )=h_{\theta }(X)^{y}(1-h_{\theta }(X))^{(1-y)}.$ We now calculate the likelihood function assuming that all the observations in the sample are independently Bernoulli distributed,

${\begin{aligned}L(\theta \mid y;x)&=\Pr(Y\mid X;\theta )\\&=\prod _{i}\Pr(y_{i}\mid x_{i};\theta )\\&=\prod _{i}h_{\theta }(x_{i})^{y_{i}}(1-h_{\theta }(x_{i}))^{(1-y_{i})}\end{aligned}}$

Typically, the log likelihood is maximized,

$N^{-1}\log L(\theta \mid y;x)=N^{-1}\sum _{i=1}^{N}\log \Pr(y_{i}\mid x_{i};\theta )$

which is maximized using optimization techniques such as gradient descent.

Assuming the $(x,y)$ pairs are drawn uniformly from the underlying distribution, then in the limit of large *N*,

${\begin{aligned}&\lim \limits _{N\rightarrow +\infty }N^{-1}\sum _{i=1}^{N}\log \Pr(y_{i}\mid x_{i};\theta )=\sum _{x\in {\mathcal {X}}}\sum _{y\in {\mathcal {Y}}}\Pr(X=x,Y=y)\log \Pr(Y=y\mid X=x;\theta )\\[6pt]={}&\sum _{x\in {\mathcal {X}}}\sum _{y\in {\mathcal {Y}}}\Pr(X=x,Y=y)\left(-\log {\frac {\Pr(Y=y\mid X=x)}{\Pr(Y=y\mid X=x;\theta )}}+\log \Pr(Y=y\mid X=x)\right)\\[6pt]={}&-D_{\text{KL}}(Y\parallel Y_{\theta })-H(Y\mid X)\end{aligned}}$

where $H(Y\mid X)$ is the conditional entropy and $D_{\text{KL}}$ is the Kullback–Leibler divergence. This leads to the intuition that by maximizing the log-likelihood of a model, you are minimizing the KL divergence of your model from the maximal entropy distribution. Intuitively searching for the model that makes the fewest assumptions in its parameters.

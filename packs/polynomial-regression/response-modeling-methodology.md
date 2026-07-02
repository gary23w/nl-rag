---
title: "Response modeling methodology"
source: https://en.wikipedia.org/wiki/Response_modeling_methodology
domain: polynomial-regression
license: CC-BY-SA-4.0
tags: polynomial regression, orthogonal polynomials, segmented regression, curve fitting
fetched: 2026-07-02
---

# Response modeling methodology

**Response modeling methodology (RMM)** is a general platform for statistical modeling of a linear/nonlinear relationship between a response variable (dependent variable) and a linear predictor (a linear combination of predictors/effects/factors/independent variables), often denoted the linear predictor function. It is generally assumed that the modeled relationship is monotone convex (delivering monotone convex function) or monotone concave (delivering monotone concave function). However, many non-monotone functions, like the quadratic equation, are special cases of the general model.

RMM was initially developed as a series of extensions to the original inverse Box–Cox transformation: $y={{(1+\lambda z)}^{1/\lambda }},$ where *y* is a percentile of the modeled response, *Y* (the modeled random variable), *z* is the respective percentile of a normal variate and λ is the Box–Cox parameter. As λ goes to zero, the inverse Box–Cox transformation becomes: $y=e^{z},$ an exponential model. Therefore, the original inverse Box-Cox transformation contains a trio of models: linear (*λ* = 1), power (*λ* ≠ 1, *λ* ≠ 0) and exponential (*λ* = 0). This implies that on estimating λ, using sample data, the final model is not determined in advance (prior to estimation) but rather as a result of estimating. In other words, data alone determine the final model.

Extensions to the inverse Box–Cox transformation were developed by Shore (2001a) and were denoted Inverse Normalizing Transformations (INTs). They had been applied to model monotone convex relationships in various engineering areas, mostly to model physical properties of chemical compounds (Shore *et al.*, 2001a, and references therein). Once it had been realized that INT models may be perceived as special cases of a much broader general approach for modeling non-linear monotone convex relationships, the new Response Modeling Methodology had been initiated and developed (Shore, 2005a, 2011 and references therein).

The RMM model expresses the relationship between a response, *Y* (the modeled random variable), and two components that deliver variation to Y:

- The linear predictor function, LP (denoted η*):* $\eta =\beta _{0}+\beta _{1}X_{1}+\cdots +\beta _{k}X_{k},$ where {*X*1,...,*X**k*} are regressor-variables (“affecting factors”) that deliver *systematic* variation to the response;
- Normal errors, delivering *random* variation to the response.

The basic RMM model describes *Y* in terms of the LP, two possibly correlated zero-mean normal errors, *ε*1 and *ε*2 (with correlation *ρ* and standard deviations *σ**ε*1 and *σ**ε*2, respectively) and a vector of parameters {*α*,*λ*,*μ*} (Shore, 2005a, 2011):

$W=\log(Y)=\mu +\left({\frac {\alpha }{\lambda }}\right)[(\eta +\varepsilon _{1})^{\lambda }-1]+\varepsilon _{2},\,$

and *ε*1 represents uncertainty (measurement imprecision or otherwise) in the explanatory variables (included in the LP). This is in addition to uncertainty associated with the response (*ε*2). Expressing *ε*1 and *ε*2 in terms of standard normal variates, *Z*1 and *Z*2, respectively, having correlation *ρ*, and conditioning *Z*2 | *Z*1 = *z*1 (*Z*2 given that *Z*1 is equal to a given value *z*1), we may write in terms of a single error, *ε*:

${\begin{aligned}\varepsilon _{1}&=\sigma _{\varepsilon _{1}}Z_{1}\,\,;\,\,\varepsilon _{2}=\sigma _{\varepsilon _{2}}Z_{2};\\[4pt]\varepsilon _{2}&=\sigma _{\varepsilon _{2}}\rho z_{1}+(1-\rho ^{2})^{(1/2)}\sigma _{\varepsilon _{2}}Z=dz_{1}+\varepsilon ,\\\end{aligned}}$

where *Z* is a standard normal variate, independent of both *Z*1 and *Z*2, *ε* is a zero-mean error and d is a parameter. From these relationships, the associated RMM quantile function is (Shore, 2011):

$w=\log(y)=\mu +\left({\frac {\alpha }{\lambda }}\right)[(\eta +cz)^{\lambda }-1]+(d)z+\varepsilon ,$

or, after re-parameterization:

$w=\log(y)=\log(M_{Y})+\left({\frac {a\eta ^{b}}{b}}\right)\left\{\left[1+\left({\frac {c}{\eta }}\right)z\right]^{b}-1\right\}+(d)z+\varepsilon ,$

where y is the percentile of the response (*Y*), *z* is the respective standard normal percentile, *ε* is the model's zero-mean normal error with constant variance, *σ*, {*a,b,c,d*} are parameters and *M**Y* is the response median (*z* = 0), dependent on values of the parameters and the value of the LP, *η*:

$\log(M_{Y})=\mu +\left({\frac {a}{b}}\right)[\eta ^{b}-1]=\log(m)+\left({\frac {a}{b}}\right)[\eta ^{b}-1],$

where *μ* (or *m*) is an additional parameter.

If it may be assumed that cz<<η, the above model for RMM quantile function can be approximated by:

$w=\log(y)=\log(M_{Y})+\left({\frac {a\eta ^{b}}{b}}\right)\left[\exp \left({\frac {bcz}{\eta }}\right)-1\right]+(d)z+\varepsilon .$

The parameter “c” cannot be “absorbed” into the parameters of the LP (η) since “c” and LP are estimated in two separate stages (as expounded below).

If the response data used to estimate the model contain values that change sign, or if the lowest response value is far from zero (for example, when data are left-truncated), a location parameter, *L*, may be added to the response so that the expressions for the quantile function and for the median become, respectively:

$w=\log(y-L)=\log(M_{Y}-L)+\left({\frac {a\eta ^{b}}{b}}\right)\left\{\left[1+\left({\frac {c}{\eta }}\right)z\right]^{b}-1\right\}+(d)z+\varepsilon \,;$

$\log(M_{Y}-L)=\mu +\left({\frac {a}{b}}\right)[\eta ^{b}-1].$

## Continuous monotonic convexity

As shown earlier, the inverse Box–Cox transformation depends on a single parameter, *λ*, which determines the final form of the model (whether linear, power or exponential). All three models thus constitute mere points on a continuous spectrum of monotonic convexity, spanned by λ. This property, where different known models become mere points on a continuous spectrum, spanned by the model's parameters, is denoted the Continuous Monotonic Convexity (CMC) property. The latter characterizes all RMM models, and it allows the basic “linear-power-exponential” cycle (underlying the inverse Box–Cox transformation) to be repeated ad infinitum, allowing for ever more convex models to be derived. Examples for such models are an exponential-power model or an exponential-exponential-power model (see explicit models expounded further on). Since the final form of the model is determined by the values of RMM parameters, this implies that the data, used to estimate the parameters, determine the final form of the estimated RMM model (as with the Box–Cox inverse transformation). The CMC property thus grant RMM models high flexibility in accommodating the data used to estimate the parameters. References given below display published results of comparisons between RMM models and existing models. These comparisons demonstrate the effectiveness of the CMC property.

## Examples of RMM models

Ignoring RMM errors (ignore the terms *cz*, *dz*, and *e* in the percentile model), we obtain the following RMM models, presented in an increasing order of monotone convexity:

${\begin{aligned}&{\text{linear: }}y=\eta &&(\alpha =1,\lambda =0);\\[5pt]&{\text{power: }}y=\eta ^{\alpha },&&(\alpha \neq 1,\lambda =0);\\[5pt]&{\text{exponential-linear: }}y=k\exp(\eta ),&&(\alpha \neq 1,\lambda =1);\\[5pt]&{\text{exponential-power: }}y=k\exp(\eta ^{\lambda }),&&(\alpha \neq 1,\lambda \neq 1;k{\text{ is a non-negative parameter}}.)\end{aligned}}$

Adding two new parameters by introducing for *η* (in the percentile model): $\exp \left[\left({\frac {\beta }{\kappa }}\right)(\eta ^{\kappa }-1)\right]$ , a new cycle of “linear-power-exponential” is iterated to produce models with stronger monotone convexity (Shore, 2005a, 2011, 2012):

${\begin{aligned}&{\text{exponential-power: }}y=k\exp(\eta ^{\lambda }),&&(\alpha \neq ,\lambda \neq 1,\beta =1,\kappa =0,\\&&&{\text{ restoring the former model}});\\[6pt]&{\text{exponential-exponential-linear: }}y=k_{1}\exp[k_{2}\exp(\eta )],&&(\alpha \neq 1,\lambda \neq 1,\beta =1,\kappa =1);\\[6pt]&{\text{exponential-exponential-power: }}y=k_{1}\exp[k_{2}\exp(\eta ^{\kappa })],&&(\alpha \neq 1,\lambda \neq 1,\beta =1,\kappa \neq 1).\end{aligned}}$

It is realized that this series of monotonic convex models, presented as they appear in a hierarchical order on the “Ladder of Monotonic Convex Functions” (Shore, 2011), is unlimited from above. However, all models are mere points on a continuous spectrum, spanned by RMM parameters. Also note that numerous growth models, like the Gompertz function, are exact special cases of the RMM model.

## Moments

The *k*-th non-central moment of *Y* is (assuming *L* = 0; Shore, 2005a, 2011):

$\operatorname {E} (Y^{k})=(M_{Y})^{k}\operatorname {E} \left\{\exp \left\{\left({\frac {k\alpha }{\lambda }}\right)[(\eta +cZ)^{\lambda }-1]+(kd)Z\right\}\right\}.$

Expanding *Y**k*, as given on the right-hand-side, into a Taylor series around zero, in terms of powers of *Z* (the standard normal variate), and then taking expectation on both sides, assuming that *cZ* ≪ *η* so that *η* + *cZ* ≈ *η*, an approximate simple expression for the *k*-th non-central moment, based on the first six terms in the expansion, is:

$\operatorname {E} (Y)^{k}\cong (M_{Y})^{k}e^{\alpha k\left(\eta ^{\lambda }-1\right)/\lambda }\left\{1+{\frac {1}{2}}(kd)^{2}+{\frac {1}{8}}(kd)^{4}\right\}.$

An analogous expression may be derived without assuming *cZ* ≪ *η*. This would result in a more accurate (however lengthy and cumbersome) expression. Once *cZ* in the above expression is neglected, *Y* becomes a log-normal random variable (with parameters that depend on *η*).

## Fitting and estimation

RMM models may be used to model *random* variation (as a general platform for distribution fitting) or to model *systematic* variation (analogously to generalized linear models, GLM).

In the former case (no systematic variation, namely, *η* = constant), RMM Quantile function is fitted to known distributions. If the underlying distribution is unknown, the RMM quantile function is estimated using available sample data. Modeling random variation with RMM is addressed and demonstrated in Shore (2011 and references therein).

In the latter case (modeling systematic variation), RMM models are estimated assuming that variation in the linear predictor (generated via variation in the regressor-variables) contribute to the overall variation of the modeled response variable (*Y*). This case is addressed and demonstrated in Shore (2005a, 2012 and relevant references therein). Estimation is conducted in two stages. First the median is estimated by minimizing the sum of absolute deviations (of fitted model from sample data points). In the second stage, the remaining two parameters (not estimated in the first stage, namely, {*c*,*d*}), are estimated. Three estimation approaches are presented in Shore (2012): maximum likelihood, moment matching and nonlinear quantile regression.

## Literature review

AS of 2021, RMM literature addresses three areas:

**(1)** Developing INTs and later the RMM approach, with allied estimation methods;

**(2)** Exploring the properties of RMM and comparing RMM effectiveness to other current modelling approaches (for distribution fitting or for modelling systematic variation);

**(3)** Applications.

Shore (2003a) developed Inverse Normalizing Transformations (INTs) in the first years of the 21st century and has applied them to various engineering disciplines like statistical process control (Shore, 2000a, b, 2001a, b, 2002a) and chemical engineering (Shore *at al.*, 2002). Subsequently, as the new Response Modeling Methodology (RMM) had been emerging and developing into a full-fledged platform for modeling monotone convex relationships (ultimately presented in a book, Shore, 2005a), RMM properties were explored (Shore, 2002b, 2004a, b, 2008a, 2011), estimation procedures developed (Shore, 2005a, b, 2012) and the new modeling methodology compared to other approaches, for modeling random variation (Shore 2005c, 2007, 2010; Shore and A’wad 2010), and for modeling systematic variation (Shore, 2008b).

Concurrently, RMM had been applied to various scientific and engineering disciplines and compared to current models and modeling approaches practiced therein. For example, chemical engineering (Shore, 2003b; Benson-Karhi *et al.*, 2007; Shacham *et al.*, 2008; Shore and Benson-Karhi, 2010), statistical process control (Shore, 2014; Shore *et al.*, 2014; Danoch and Shore, 2016), reliability engineering (Shore, 2004c; Ladany and Shore, 2007), forecasting (Shore and Benson-Karhi, 2007), ecology (Shore, 2014), and the medical profession (Shore *et al.,* 2014; Benson-Karhi *et al.*, 2017).

---
title: "Endogeneity (econometrics)"
source: https://en.wikipedia.org/wiki/Endogeneity_(econometrics)
domain: econometrics
license: CC-BY-SA-4.0
tags: econometrics, instrumental variables, panel data, gauss-markov theorem
fetched: 2026-07-02
---

# Endogeneity (econometrics)

In econometrics, **endogeneity** broadly refers to situations in which an explanatory variable is correlated with the error term.

In simplest terms, **endogeneity** means that a factor or cause one uses to explain something as an outcome is also being influenced by that same thing. For example, education can affect income, but income can also affect how much education someone gets. When this happens, one's analysis might wrongly estimate cause and effect. The thing one thinks is causing change is also being influenced by the outcome, making the results unreliable.

The concept originates from simultaneous equations models, in which one distinguishes variables whose values are determined within the economic model (endogenous) from those that are predetermined (exogenous).

Ignoring simultaneity in estimation leads to biased and inconsistent estimators, as it violates the exogeneity condition of the Gauss–Markov theorem. This issue is often overlooked in non-experimental research, which limits the validity of causal inference and the ability to draw reliable policy recommendations.

Common solutions to address endogeneity include the use of instrumental variable techniques, which provide consistent estimators by introducing variables that are correlated with the endogenous explanatory variable but uncorrelated with the error term.

Besides simultaneity, correlation between explanatory variables and the error term can arise when an unobserved or omitted variable is confounding both independent and dependent variables, or when independent variables are measured with error.

## Definition of exogeneity

In a stochastic model, the notion of the *usual exogeneity*, *sequential exogeneity*, *strong/strict exogeneity* can be defined. **Exogeneity** is articulated in such a way that a variable or variables is exogenous for parameter $\alpha$ . Even if a variable is exogenous for parameter $\alpha$ , it might be endogenous for parameter $\beta$ .

When the explanatory variables are not stochastic, then they are strong exogenous for all the parameters.

If the independent variable is correlated with the error term in a regression model then the estimate of the regression coefficient in an ordinary least squares (OLS) regression is biased; however if the correlation is not contemporaneous, then the coefficient estimate may still be consistent. There are many methods of correcting the bias, including instrumental variable regression and Heckman selection correction.

## Static models

The following are some common sources of endogeneity.

### Omitted variable

In this case, the endogeneity comes from an uncontrolled confounding variable, a variable that is correlated with both the independent variable in the model and with the error term. (Equivalently, the omitted variable affects the independent variable and separately affects the dependent variable.)

Assume that the "true" model to be estimated is

$y_{i}=\alpha +\beta x_{i}+\gamma z_{i}+u_{i}$

but $z_{i}$ is omitted from the regression model (perhaps because there is no way to measure it directly). Then the model that is actually estimated is

$y_{i}=\alpha +\beta x_{i}+\varepsilon _{i}$

where $\varepsilon _{i}=\gamma z_{i}+u_{i}$ (thus, the $z_{i}$ term has been absorbed into the error term).

If the correlation of x and z is not 0 and z separately affects y (meaning $\gamma \neq 0$ ), then x is correlated with the error term $\varepsilon$ .

Here, x is not exogenous for $\alpha$ and $\beta$ , since, given x , the distribution of y depends not only on $\alpha$ and $\beta$ , but also on z and $\gamma$ .

### Measurement error

Suppose that a perfect measure of an independent variable is impossible. That is, instead of observing $x_{i}^{*}$ , what is actually observed is $x_{i}=x_{i}^{*}+\nu _{i}$ where $\nu _{i}$ is the measurement error or "noise". In this case, a model given by

$y_{i}=\alpha +\beta x_{i}^{*}+\varepsilon _{i}$

can be written in terms of observables and error terms as

${\begin{aligned}y_{i}&=\alpha +\beta (x_{i}-\nu _{i})+\varepsilon _{i}\\[3pt]y_{i}&=\alpha +\beta x_{i}+(\varepsilon _{i}-\beta \nu _{i})\\[3pt]y_{i}&=\alpha +\beta x_{i}+u_{i}\quad ({\text{where }}u_{i}=\varepsilon _{i}-\beta \nu _{i})\end{aligned}}$

Since both $x_{i}$ and $u_{i}$ depend on $\nu _{i}$ , they are correlated, so the OLS estimation of $\beta$ will be biased downward.

Measurement error in the dependent variable, $y_{i}$ , does not cause endogeneity, though it does increase the variance of the error term.

### Simultaneity

Suppose that two variables are codetermined, with each affecting the other according to the following "structural" equations:

$y_{i}=\beta _{1}x_{i}+\gamma _{1}z_{i}+u_{i}$

$z_{i}=\beta _{2}x_{i}+\gamma _{2}y_{i}+v_{i}$

Estimating either equation by itself results in endogeneity. In the case of the first structural equation, $E(z_{i}u_{i})\neq 0$ . Solving for $z_{i}$ while assuming that $1-\gamma _{1}\gamma _{2}\neq 0$ results in

$z_{i}={\frac {\beta _{2}x_{i}+\gamma _{2}\beta _{1}}{1-\gamma _{1}\gamma _{2}}}x_{i}+{\frac {1}{1-\gamma _{1}\gamma _{2}}}v_{i}+{\frac {\gamma _{2}}{1-\gamma _{1}\gamma _{2}}}u_{i}$

.

Assuming that $x_{i}$ and $v_{i}$ are uncorrelated with $u_{i}$ ,

$\operatorname {E} (z_{i}u_{i})={\frac {\gamma _{2}}{1-\gamma _{1}\gamma _{2}}}\operatorname {E} (u_{i}u_{i})\neq 0$

.

Therefore, attempts at estimating either structural equation will be hampered by endogeneity.

## Dynamic models

The endogeneity problem is particularly relevant in the context of time series analysis of causal processes. It is common for some factors within a causal system to be dependent for their value in period *t* on the values of other factors in the causal system in period *t* − 1. Suppose that the level of pest infestation is independent of all other factors within a given period, but is influenced by the level of rainfall and fertilizer in the preceding period. In this instance it would be correct to say that infestation is exogenous within the period, but endogenous over time.

### Strict exogeneity

Let the model be *y* = *f*(*x*, *z*) + *u*. If the variable *x* is sequential exogenous for parameter $\alpha$ , and *y* does not cause *x* in the Granger sense, then the variable *x* is strongly/strictly exogenous for the parameter $\alpha$ .

### Weak exogeneity

**Weak exogeneity** is an identifying assumption which requires that the structural error term has a zero conditional expectation given the present and past values of the regressors. It is used to determine whether statistical inference about parameters of interest can be validly drawn from a conditional probability model alone, without needing to analyze the marginal distribution of the explanatory variables. While strict exogeneity is often implausible in macroeconomic and financial data due to feedback effects, weak exogeneity is the standard identifying assumption employed in these fields.

The concept was formalized by Jean-François Richard (1980) and further analyzed by Robert F. Engle, David F. Hendry, and Richard (1983) in Econometrica.

The variable $z_{t}$ is weakly exogenous for a set of specific parameters of interest, denoted as $\psi =(\phi _{1},\phi _{2})$ , if the marginal density of $z_{t}$ contains no useful information for estimating $\psi$ , that is

- the parameters of interest $\psi$ must depend only on the parameters of the conditional model ( $\phi _{1}$ ) and not on the parameters of the marginal model ( $\phi _{2}$ )
- the parameters $\phi _{1}$ and $\phi _{2}$ must be variation-free. This means that the permissible range of values for $\phi _{1}$ does not depend on the values taken by $\phi _{2}$

In a linear regression framework defined by: $z_{t}=x_{t}^{\top }\beta +\epsilon _{t}$ where $z_{t}$ is the outcome variable, $x_{t}$ are the regressors (potentially containing past values of $z_{t}$ ), and $\epsilon _{t}$ is the structural error term, this implies that the errors are orthogonal to current and past regressors. This can be expressed by the following moment condition:

$\mathbb {E} [\epsilon _{t}\mid x_{t},x_{t-1},\dots ]=0$

This condition allows for the errors to be correlated with future realizations of the regressors, accommodating feedback mechanisms where an outcome variable in one period influences regressor values in future periods.

This is in contrast to **strict exogeneity**, a more restrictive assumption which requires that the error term has a zero conditional expectation conditional on the complete set of regressors, including past, present, and future values, that is $\mathbb {E} [\epsilon _{t}\mid x_{0},x_{1},...,x_{T}]=0$ where T is the size of the sample.

Equivalently, weak exogeneity requires regressors and lagged response variables to be **predetermined**—that is, determined prior to the current period.

A common example of a weakly exogenous variable is consumption in models with credit constraints and rational expectations. Here, consumption is predetermined but not strictly exogenous. An unpredictable negative income shock will be uncorrelated with past (and potentially current) consumption, but will surely be correlated with future consumption—the individual will be forced to adjust their future consumption to accommodate their poorer state, inducing correlation. If the shock affects current consumption, predeterminedness (defined now as lags only) provides potential instruments—lagged values of the variable.

The presence of predetermined variables is a motivating factor in the Arellano–Bond estimator.

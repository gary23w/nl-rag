---
title: "Fixed effects model"
source: https://en.wikipedia.org/wiki/Fixed_effects_model
domain: mixed-effects-models
license: CC-BY-SA-4.0
tags: mixed model, random effects, fixed effects, intraclass correlation
fetched: 2026-07-02
---

# Fixed effects model

In statistics, a **fixed effects model** is a statistical model in which the model parameters are fixed or non-random quantities. This is in contrast to random effects models and mixed models in which all or some of the model parameters are random variables. In many applications including econometrics and biostatistics a fixed effects model refers to a regression model in which the group means are fixed (non-random) as opposed to a random effects model in which the group means are a random sample from a population. Generally, data can be grouped according to several observed factors. The group means could be modeled as fixed or random effects for each grouping. In a fixed effects model each group mean is a group-specific fixed quantity.

In panel data where longitudinal observations exist for the same subject, fixed effects represent the subject-specific means. In panel data analysis the term **fixed effects estimator** (also known as the **within estimator**) is used to refer to an estimator for the coefficients in the regression model including those fixed effects (one time-invariant intercept for each subject).

## Qualitative description

Such models assist in controlling for omitted variable bias due to unobserved heterogeneity when this heterogeneity is constant over time. This heterogeneity can be removed from the data through differencing, for example by subtracting the group-level average over time, or by taking a first difference which will remove any time invariant components of the model.

There are two common assumptions made about the individual specific effect: the random effects assumption and the fixed effects assumption. The random effects assumption is that the individual-specific effects are uncorrelated with the independent variables. The fixed effect assumption is that the individual-specific effects are correlated with the independent variables. If the random effects assumption holds, the random effects estimator is more efficient than the fixed effects estimator. However, if this assumption does not hold, the random effects estimator is not consistent. The Durbin–Wu–Hausman test is often used to discriminate between the fixed and the random effects models.

## Formal model and assumptions

Consider the linear unobserved effects model for N observations and T time periods:

$y_{it}=X_{it}\mathbf {\beta } +\alpha _{i}+u_{it}$

for

$t=1,\dots ,T$

and

$i=1,\dots ,N$

Where:

- $y_{it}$ is the dependent variable observed for individual i at time t .
- $X_{it}$ is the time-variant $1\times k$ (the number of independent variables) regressor vector.
- $\beta$ is the $k\times 1$ matrix of parameters.
- $\alpha _{i}$ is the unobserved time-invariant individual effect. For example, the innate ability for individuals or historical and institutional factors for countries.
- $u_{it}$ is the error term.

Unlike $X_{it}$ , $\alpha _{i}$ cannot be directly observed.

Unlike the random effects model where the unobserved $\alpha _{i}$ is independent of $X_{it}$ for all $t=1,...,T$ , the fixed effects (FE) model allows $\alpha _{i}$ to be correlated with the regressor matrix $X_{it}$ . Strict exogeneity with respect to the idiosyncratic error term $u_{it}$ is still required.

## Statistical estimation

### Fixed effects estimator

Since $\alpha _{i}$ is not observable, it cannot be directly controlled for. The FE model eliminates $\alpha _{i}$ by de-meaning the variables using the *within* transformation:

$y_{it}-{\overline {y}}_{i}=\left(X_{it}-{\overline {X}}_{i}\right)\beta +\left(\alpha _{i}-{\overline {\alpha }}_{i}\right)+\left(u_{it}-{\overline {u}}_{i}\right)\implies {\ddot {y}}_{it}={\ddot {X}}_{it}\beta +{\ddot {u}}_{it}$

where ${\overline {y}}_{i}={\frac {1}{T}}\sum \limits _{t=1}^{T}y_{it}$ , ${\overline {X}}_{i}={\frac {1}{T}}\sum \limits _{t=1}^{T}X_{it}$ , and ${\overline {u}}_{i}={\frac {1}{T}}\sum \limits _{t=1}^{T}u_{it}$ .

Since $\alpha _{i}$ is constant, ${\overline {\alpha _{i}}}=\alpha _{i}$ and hence the effect is eliminated. The FE estimator ${\hat {\beta }}_{FE}$ is then obtained by an OLS regression of ${\ddot {y}}$ on ${\ddot {X}}$ .

At least three alternatives to the *within* transformation exist with variations:

- One is to add a dummy variable for each individual $i>1$ (omitting the first individual because of multicollinearity). This is numerically, but not computationally, equivalent to the fixed effect model and only works if the sum of the number of series and the number of global parameters is smaller than the number of observations. The dummy variable approach is particularly demanding with respect to computer memory usage and it is not recommended for problems larger than the available RAM, and the applied program compilation, can accommodate.

- Second alternative is to use consecutive reiterations approach to local and global estimations. This approach is very suitable for low memory systems on which it is much more computationally efficient than the dummy variable approach.

- The third approach is a nested estimation whereby the local estimation for individual series is programmed in as a part of the model definition. This approach is the most computationally and memory efficient, but it requires proficient programming skills and access to the model programming code; although, it can be programmed including in SAS.

Finally, each of the above alternatives can be improved if the series-specific estimation is linear (within a nonlinear model), in which case the direct linear solution for individual series can be programmed in as part of the nonlinear model definition.

### First difference estimator

An alternative to the within transformation is the *first difference* transformation, which produces a different estimator. For $t=2,\dots ,T$ :

$y_{it}-y_{i,t-1}=\left(X_{it}-X_{i,t-1}\right)\beta +\left(\alpha _{i}-\alpha _{i}\right)+\left(u_{it}-u_{i,t-1}\right)\implies \Delta y_{it}=\Delta X_{it}\beta +\Delta u_{it}.$

The FD estimator ${\hat {\beta }}_{FD}$ is then obtained by an OLS regression of $\Delta y_{it}$ on $\Delta X_{it}$ .

When $T=2$ , the first difference and fixed effects estimators are numerically equivalent. For $T>2$ , they are not. If the error terms $u_{it}$ are homoskedastic with no serial correlation, the fixed effects estimator is more efficient than the first difference estimator. If $u_{it}$ follows a random walk, however, the first difference estimator is more efficient.

#### Equality of fixed effects and first difference estimators when T=2

For the special two period case ( $T=2$ ), the fixed effects (FE) estimator and the first difference (FD) estimator are numerically equivalent. This is because the FE estimator effectively "doubles the data set" used in the FD estimator. To see this, establish that the fixed effects estimator is: ${FE}_{T=2}=\left[(x_{i1}-{\bar {x}}_{i})(x_{i1}-{\bar {x}}_{i})'+(x_{i2}-{\bar {x}}_{i})(x_{i2}-{\bar {x}}_{i})'\right]^{-1}\left[(x_{i1}-{\bar {x}}_{i})(y_{i1}-{\bar {y}}_{i})+(x_{i2}-{\bar {x}}_{i})(y_{i2}-{\bar {y}}_{i})\right]$

Since each $(x_{i1}-{\bar {x}}_{i})$ can be re-written as $(x_{i1}-{\dfrac {x_{i1}+x_{i2}}{2}})={\dfrac {x_{i1}-x_{i2}}{2}}$ , we'll re-write the line as:

${FE}_{T=2}=\left[\sum _{i=1}^{N}{\dfrac {x_{i1}-x_{i2}}{2}}{\dfrac {x_{i1}-x_{i2}}{2}}'+{\dfrac {x_{i2}-x_{i1}}{2}}{\dfrac {x_{i2}-x_{i1}}{2}}'\right]^{-1}\left[\sum _{i=1}^{N}{\dfrac {x_{i1}-x_{i2}}{2}}{\dfrac {y_{i1}-y_{i2}}{2}}+{\dfrac {x_{i2}-x_{i1}}{2}}{\dfrac {y_{i2}-y_{i1}}{2}}\right]$

$=\left[\sum _{i=1}^{N}2{\dfrac {x_{i2}-x_{i1}}{2}}{\dfrac {x_{i2}-x_{i1}}{2}}'\right]^{-1}\left[\sum _{i=1}^{N}2{\dfrac {x_{i2}-x_{i1}}{2}}{\dfrac {y_{i2}-y_{i1}}{2}}\right]$

$=2\left[\sum _{i=1}^{N}(x_{i2}-x_{i1})(x_{i2}-x_{i1})'\right]^{-1}\left[\sum _{i=1}^{N}{\frac {1}{2}}(x_{i2}-x_{i1})(y_{i2}-y_{i1})\right]$

$=\left[\sum _{i=1}^{N}(x_{i2}-x_{i1})(x_{i2}-x_{i1})'\right]^{-1}\sum _{i=1}^{N}(x_{i2}-x_{i1})(y_{i2}-y_{i1})={FD}_{T=2}$

### Chamberlain method

Gary Chamberlain's method, a generalization of the within estimator, replaces $\alpha _{i}$ with its linear projection onto the explanatory variables. Writing the linear projection as:

$\alpha _{i}=\lambda _{0}+X_{i1}\lambda _{1}+X_{i2}\lambda _{2}+\dots +X_{iT}\lambda _{T}+e_{i}$

this results in the following equation:

$y_{it}=\lambda _{0}+X_{i1}\lambda _{1}+X_{i2}\lambda _{2}+\dots +X_{it}(\lambda _{t}+\mathbf {\beta } )+\dots +X_{iT}\lambda _{T}+e_{i}+u_{it}$

which can be estimated by minimum distance estimation.

### Hausman–Taylor method

Need to have more than one time-variant regressor ( X ) and time-invariant regressor ( Z ) and at least one X and one Z that are uncorrelated with $\alpha _{i}$ .

Partition the X and Z variables such that ${\begin{array}{c}X=[{\underset {TN\times K1}{X_{1it}}}\vdots {\underset {TN\times K2}{X_{2it}}}]\\Z=[{\underset {TN\times G1}{Z_{1it}}}\vdots {\underset {TN\times G2}{Z_{2it}}}]\end{array}}$ where $X_{1}$ and $Z_{1}$ are uncorrelated with $\alpha _{i}$ . Need $K1>G2$ .

Estimating $\gamma$ via OLS on ${\widehat {di}}=Z_{i}\gamma +\varphi _{it}$ using $X_{1}$ and $Z_{1}$ as instruments yields a consistent estimate.

### Generalization with input uncertainty

When there is input uncertainty for the y data, $\delta y$ , then the $\chi ^{2}$ value, rather than the sum of squared residuals, should be minimized. This can be directly achieved from substitution rules:

${\frac {y_{it}}{\delta y_{it}}}=\mathbf {\beta } {\frac {X_{it}}{\delta y_{it}}}+\alpha _{i}{\frac {1}{\delta y_{it}}}+{\frac {u_{it}}{\delta y_{it}}}$

,

then the values and standard deviations for $\mathbf {\beta }$ and $\alpha _{i}$ can be determined via classical ordinary least squares analysis and variance-covariance matrix.

## Use to test for consistency

Random effects estimators may be inconsistent sometimes in the long time series limit, if the random effects are misspecified (i.e. the model chosen for the random effects is incorrect). However, the fixed effects model may still be consistent in some situations. For example, if the time series being modeled is not stationary, random effects models assuming stationarity may not be consistent in the long-series limit. One example of this is if the time series has an upward trend. Then, as the series becomes longer, the model revises estimates for the mean of earlier periods upwards, giving increasingly biased predictions of coefficients. However, a model with fixed time effects does not pool information across time, and as a result earlier estimates will not be affected.

In situations like these where the fixed effects model is known to be consistent, the Durbin-Wu-Hausman test can be used to test whether the random effects model chosen is consistent. If $H_{0}$ is true, both ${\widehat {\beta }}_{RE}$ and ${\widehat {\beta }}_{FE}$ are consistent, but only ${\widehat {\beta }}_{RE}$ is efficient. If $H_{a}$ is true the consistency of ${\widehat {\beta }}_{RE}$ cannot be guaranteed.

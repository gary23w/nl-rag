---
title: "Vector autoregression"
source: https://en.wikipedia.org/wiki/Structural_vector_autoregression
domain: vector-autoregression
license: CC-BY-SA-4.0
tags: vector autoregression, Granger causality, impulse response, structural VAR
fetched: 2026-07-02
---

# Vector autoregression

(Redirected from

Structural vector autoregression

)

**Vector autoregression** (**VAR**) is a statistical model used to capture the relationship between multiple quantities as they change over time. VAR is a type of stochastic process model. VAR models generalize the single-variable (univariate) autoregressive model by allowing for multivariate time series. VAR models are often used in economics and the natural sciences.

Like the autoregressive model, each variable has an equation modelling its evolution over time. This equation includes the variable's lagged (past) values, the lagged values of the other variables in the model, and an error term. VAR models do not require as much knowledge about the forces influencing a variable as do structural models with simultaneous equations. The only prior knowledge required is a list of variables which can be hypothesized to affect each other over time.

## Specification

### Definition

A VAR model describes the evolution of a set of *k* variables, called *endogenous variables*, over time. Each period of time is numbered, *t* = 1, ..., *T*. The variables are collected in a vector, *yt*, which is of length *k.* (Equivalently, this vector might be described as a (*k* × 1)-matrix.) The vector is modelled as a linear function of its previous value. The vector's components are referred to as *y**i*,*t*, meaning the observation at time *t* of the *i* th variable. For example, if the first variable in the model measures the price of wheat over time, then *y*1,1998 would indicate the price of wheat in the year 1998.

VAR models are characterized by their *order*, which refers to the number of earlier time periods the model will use. Continuing the above example, a 5th-order VAR would model each year's wheat price as a linear combination of the last five years of wheat prices. A *lag* is the value of a variable in a previous time period. So in general a *p*th-order VAR refers to a VAR model which includes lags for the last *p* time periods. A *p*th-order VAR is denoted "VAR(*p*)" and sometimes called "a VAR with *p* lags". A *p*th-order VAR model is written as

$y_{t}=c+A_{1}y_{t-1}+A_{2}y_{t-2}+\cdots +A_{p}y_{t-p}+e_{t},\,$

The variables of the form *y**t*−i indicate that variable's value *i* time periods earlier and are called the "i*th* lag" of *y*t. The variable *c* is a *k*-vector of constants serving as the intercept of the model. *Ai* is a time-invariant (*k* × *k*)-matrix and *e**t* is a *k*-vector of error terms. The error terms must satisfy three conditions:

1. $\mathrm {E} (e_{t})=0\,$ . Every error term has a mean of zero.
2. $\mathrm {E} (e_{t}e_{t}')=\Omega \,$ . The contemporaneous covariance matrix of error terms is a *k* × *k* positive-semidefinite matrix denoted Ω.
3. $\mathrm {E} (e_{t}e_{t-k}')=0\,$ for any non-zero *k*. There is no correlation across time. In particular, there is no serial correlation in individual error terms.

The process of choosing the maximum lag *p* in the VAR model requires special attention because inference is dependent on correctness of the selected lag order.

### Order of integration of the variables

Note that all variables have to be of the same order of integration. The following cases are distinct:

- All the variables are I(0) (stationary): this is in the standard case, i.e. a VAR in level
- All the variables are I(*d*) (non-stationary) with *d* > 0:
  - The variables are cointegrated: the error correction term has to be included in the VAR. The model becomes a Vector error correction model (VECM) which can be seen as a restricted VAR.
  - The variables are not cointegrated: first, the variables have to be differenced d times and one has a VAR in difference.

### Concise matrix notation

One can stack the vectors in order to write a VAR(*p*) as a stochastic matrix difference equation, with a concise matrix notation:

$Y=BZ+U\,$

### Example

A VAR(1) in two variables can be written in matrix form (more compact notation) as

${\begin{bmatrix}y_{1,t}\\y_{2,t}\end{bmatrix}}={\begin{bmatrix}c_{1}\\c_{2}\end{bmatrix}}+{\begin{bmatrix}a_{1,1}&a_{1,2}\\a_{2,1}&a_{2,2}\end{bmatrix}}{\begin{bmatrix}y_{1,t-1}\\y_{2,t-1}\end{bmatrix}}+{\begin{bmatrix}e_{1,t}\\e_{2,t}\end{bmatrix}},$

(in which only a single *A* matrix appears because this example has a maximum lag *p* equal to 1), or, equivalently, as the following system of two equations

$y_{1,t}=c_{1}+a_{1,1}y_{1,t-1}+a_{1,2}y_{2,t-1}+e_{1,t}\,$

$y_{2,t}=c_{2}+a_{2,1}y_{1,t-1}+a_{2,2}y_{2,t-1}+e_{2,t}.\,$

Each variable in the model has one equation. The current (time *t*) observation of each variable depends on its own lagged values as well as on the lagged values of each other variable in the VAR.

### Writing VAR(*p*) as VAR(1)

A VAR with *p* lags can always be equivalently rewritten as a VAR with only one lag by appropriately redefining the dependent variable. The transformation amounts to stacking the lags of the VAR(*p*) variable in the new VAR(1) dependent variable and appending identities to complete the precise number of equations.

For example, the VAR(2) model

$y_{t}=c+A_{1}y_{t-1}+A_{2}y_{t-2}+e_{t}$

can be recast as the VAR(1) model

${\begin{bmatrix}y_{t}\\y_{t-1}\end{bmatrix}}={\begin{bmatrix}c\\0\end{bmatrix}}+{\begin{bmatrix}A_{1}&A_{2}\\I&0\end{bmatrix}}{\begin{bmatrix}y_{t-1}\\y_{t-2}\end{bmatrix}}+{\begin{bmatrix}e_{t}\\0\end{bmatrix}},$

where *I* is the identity matrix.

The equivalent VAR(1) form is more convenient for analytical derivations and allows more compact statements.

## Structural vs. reduced form

### Structural VAR

A ***structural VAR with p lags*** (sometimes abbreviated **SVAR**) is

$B_{0}y_{t}=c_{0}+B_{1}y_{t-1}+B_{2}y_{t-2}+\cdots +B_{p}y_{t-p}+\epsilon _{t},$

where *c*0 is a *k* × 1 vector of constants, *Bi* is a *k* × *k* matrix (for every *i* = 0, ..., *p*) and *ε**t* is a *k* × 1 vector of error terms. The main diagonal terms of the *B*0 matrix (the coefficients on the *i*th variable in the *i*th equation) are scaled to 1.

The error terms ε*t* (***structural shocks***) satisfy the conditions (1) - (3) in the definition above, with the particularity that all the elements in the off diagonal of the covariance matrix $\mathrm {E} (\epsilon _{t}\epsilon _{t}')=\Sigma$ are zero. That is, the structural shocks are uncorrelated.

For example, a two variable structural VAR(1) is:

${\begin{bmatrix}1&B_{0;1,2}\\B_{0;2,1}&1\end{bmatrix}}{\begin{bmatrix}y_{1,t}\\y_{2,t}\end{bmatrix}}={\begin{bmatrix}c_{0;1}\\c_{0;2}\end{bmatrix}}+{\begin{bmatrix}B_{1;1,1}&B_{1;1,2}\\B_{1;2,1}&B_{1;2,2}\end{bmatrix}}{\begin{bmatrix}y_{1,t-1}\\y_{2,t-1}\end{bmatrix}}+{\begin{bmatrix}\epsilon _{1,t}\\\epsilon _{2,t}\end{bmatrix}},$

where

$\Sigma =\mathrm {E} (\epsilon _{t}\epsilon _{t}')={\begin{bmatrix}\sigma _{1}^{2}&0\\0&\sigma _{2}^{2}\end{bmatrix}};$

that is, the variances of the structural shocks are denoted $\mathrm {var} (\epsilon _{i})=\sigma _{i}^{2}$ (*i* = 1, 2) and the covariance is $\mathrm {cov} (\epsilon _{1},\epsilon _{2})=0$ .

Writing the first equation explicitly and passing *y2,t* to the right hand side one obtains

$y_{1,t}=c_{0;1}-B_{0;1,2}y_{2,t}+B_{1;1,1}y_{1,t-1}+B_{1;1,2}y_{2,t-1}+\epsilon _{1,t}\,$

Note that *y*2,*t* can have a contemporaneous effect on *y1,t* if *B*0;1,2 is not zero. This is different from the case when *B*0 is the identity matrix (all off-diagonal elements are zero — the case in the initial definition), when *y*2,*t* can impact directly *y*1,*t*+1 and subsequent future values, but not *y*1,*t*.

Because of the parameter identification problem, ordinary least squares estimation of the structural VAR would yield inconsistent parameter estimates. This problem can be overcome by rewriting the VAR in reduced form.

From an economic point of view, if the joint dynamics of a set of variables can be represented by a VAR model, then the structural form is a depiction of the underlying, "structural", economic relationships. Two features of the structural form make it the preferred candidate to represent the underlying relations:

1.

Error terms are not correlated

. The structural, economic shocks which drive the dynamics of the economic variables are assumed to be

independent

, which implies zero correlation between error terms as a desired property. This is helpful for separating out the effects of economically unrelated influences in the VAR. For instance, there is no reason why an oil price shock (as an example of a

supply shock

) should be related to a shift in consumers' preferences towards a style of clothing (as an example of a

demand shock

); therefore one would expect these factors to be statistically independent.

2.

Variables can have a

contemporaneous impact

on other variables

. This is a desirable feature especially when using low frequency data. For example, an

indirect tax

rate increase would not affect

tax revenues

the day the decision is announced, but one could find an effect in that quarter's data.

### Reduced-form VAR

By premultiplying the structural VAR with the inverse of *B*0

$y_{t}=B_{0}^{-1}c_{0}+B_{0}^{-1}B_{1}y_{t-1}+B_{0}^{-1}B_{2}y_{t-2}+\cdots +B_{0}^{-1}B_{p}y_{t-p}+B_{0}^{-1}\epsilon _{t},$

and denoting

$B_{0}^{-1}c_{0}=c,\quad B_{0}^{-1}B_{i}=A_{i}{\text{ for }}i=1,\dots ,p{\text{ and }}B_{0}^{-1}\epsilon _{t}=e_{t}$

one obtains the ***p*th order reduced VAR**

$y_{t}=c+A_{1}y_{t-1}+A_{2}y_{t-2}+\cdots +A_{p}y_{t-p}+e_{t}$

Note that in the reduced form all right hand side variables are predetermined at time *t*. As there are no time *t* endogenous variables on the right hand side, no variable has a *direct* contemporaneous effect on other variables in the model.

However, the error terms in the reduced VAR are composites of the structural shocks *e**t* = *B*0−1*ε**t*. Thus, the occurrence of one structural shock *εi,t* can potentially lead to the occurrence of shocks in all error terms *ej,t*, thus creating contemporaneous movement in all endogenous variables. Consequently, the covariance matrix of the reduced VAR

$\Omega =\mathrm {E} (e_{t}e_{t}')=\mathrm {E} (B_{0}^{-1}\epsilon _{t}\epsilon _{t}'(B_{0}^{-1})')=B_{0}^{-1}\Sigma (B_{0}^{-1})'\,$

can have non-zero off-diagonal elements, thus allowing non-zero correlation between error terms.

## Estimation

### Estimation of the regression parameters

Starting from the concise matrix notation:

$Y=BZ+U\,$

- The multivariate least squares (MLS) approach for estimating B yields:

${\hat {B}}=YZ'(ZZ')^{-1}.$

This can be written alternatively as:

$\operatorname {Vec} ({\hat {B}})=((ZZ')^{-1}Z\otimes I_{k})\ \operatorname {Vec} (Y),$

where $\otimes$ denotes the Kronecker product and Vec the vectorization of the indicated matrix.

This estimator is consistent and asymptotically efficient. It is furthermore equal to the conditional maximum likelihood estimator.

- As the explanatory variables are the same in each equation, the multivariate least squares estimator is equivalent to the ordinary least squares estimator applied to each equation separately.

### Estimation of the covariance matrix of the errors

As in the standard case, the maximum likelihood estimator (MLE) of the covariance matrix differs from the ordinary least squares (OLS) estimator.

MLE estimator: ${\hat {\Sigma }}={\frac {1}{T}}\sum _{t=1}^{T}{\hat {\epsilon }}_{t}{\hat {\epsilon }}_{t}'$

OLS estimator: ${\hat {\Sigma }}={\frac {1}{T-kp-1}}\sum _{t=1}^{T}{\hat {\epsilon }}_{t}{\hat {\epsilon }}_{t}'$ for a model with a constant, *k* variables and *p* lags.

In a matrix notation, this gives:

${\hat {\Sigma }}={\frac {1}{T-kp-1}}(Y-{\hat {B}}Z)(Y-{\hat {B}}Z)'.$

### Estimation of the estimator's covariance matrix

The covariance matrix of the parameters can be estimated as

${\widehat {\mbox{Cov}}}({\mbox{Vec}}({\hat {B}}))=({ZZ'})^{-1}\otimes {\hat {\Sigma }}.\,$

### Degrees of freedom

Vector autoregression models often involve the estimation of many parameters. For example, with seven variables and four lags, each matrix of coefficients for a given lag length is 7 by 7, and the vector of constants has 7 elements, so a total of 49×4 + 7 = 203 parameters are estimated, substantially lowering the degrees of freedom of the regression (the number of data points minus the number of parameters to be estimated). This can hurt the accuracy of the parameter estimates and hence of the forecasts given by the model.

## Interpretation of estimated model

### Impulse response

Consider the first-order case (i.e., with only one lag), with equation of evolution

$y_{t}=Ay_{t-1}+e_{t},$

for evolving (state) vector y and vector e of shocks. To find, say, the effect of the *j*-th element of the vector of shocks upon the *i*-th element of the state vector 2 periods later, which is a particular impulse response, first write the above equation of evolution one period lagged:

$y_{t-1}=Ay_{t-2}+e_{t-1}.$

Use this in the original equation of evolution to obtain

$y_{t}=A^{2}y_{t-2}+Ae_{t-1}+e_{t};$

then repeat using the twice lagged equation of evolution, to obtain

$y_{t}=A^{3}y_{t-3}+A^{2}e_{t-2}+Ae_{t-1}+e_{t}.$

From this, the effect of the *j*-th component of $e_{t-2}$ upon the *i*-th component of $y_{t}$ is the *i, j* element of the matrix $A^{2}.$

It can be seen from this induction process that any shock will have an effect on the elements of *y* infinitely far forward in time, although the effect will become smaller and smaller over time assuming that the AR process is stable — that is, that all the eigenvalues of the matrix *A* are less than 1 in absolute value.

## Forecasting using an estimated VAR model

An estimated VAR model can be used for forecasting, and the quality of the forecasts can be judged, in ways that are completely analogous to the methods used in univariate autoregressive modelling.

## Applications

Christopher Sims has advocated VAR models, criticizing the claims and performance of earlier modeling in macroeconomic econometrics. He recommended VAR models, which had previously appeared in time series statistics and in system identification, a statistical specialty in control theory. Sims advocated VAR models as providing a theory-free method to estimate economic relationships, thus being an alternative to the "incredible identification restrictions" in structural models. VAR models are also increasingly used in health research for automatic analyses of diary data or sensor data. Sio Iong Ao and R. E. Caraka found that the artificial neural network can improve its performance with the addition of the hybrid vector autoregression component.

## Software

- R: The package *vars* includes functions for VAR models. Other R packages are listed in the CRAN Task View: Time Series Analysis.
- Python: The *statsmodels* package's tsa (time series analysis) module supports VARs. *PyFlux* has support for VARs and Bayesian VARs.
- SAS: VARMAX
- Stata: "var"
- EViews: "VAR"
- Gretl: "var"
- Matlab: "varm"
- Regression analysis of time series: "SYSTEM"
- LDT

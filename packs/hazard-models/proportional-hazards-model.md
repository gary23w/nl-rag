---
title: "Proportional hazards model"
source: https://en.wikipedia.org/wiki/Proportional_hazards_model
domain: hazard-models
license: CC-BY-SA-4.0
tags: failure rate, hazard function, accelerated failure time, life table
fetched: 2026-07-02
---

# Proportional hazards model

**Proportional hazards models** are a class of survival models in statistics. Survival models relate the time that passes, before some event occurs, to one or more covariates that may be associated with that quantity of time. In a proportional hazards model, the unique effect of a unit increase in a covariate is multiplicative with respect to the hazard rate. The hazard rate at time t is the probability per short time d*t* that an event will occur between t and $t+dt$ given that up to time t no event has occurred yet. For example, taking a drug may halve one's hazard rate for a stroke occurring, or, changing the material from which a manufactured component is constructed, may double its hazard rate for failure. Other types of survival models such as accelerated failure time models do not exhibit proportional hazards. The accelerated failure time model describes a situation where the biological or mechanical life history of an event is accelerated (or decelerated).

## Background

Survival models can be viewed as consisting of two parts: the underlying baseline hazard function, often denoted $\lambda _{0}(t)$ , describing how the risk of event per time unit changes over time at *baseline* levels of covariates; and the effect parameters, describing how the hazard varies in response to explanatory covariates. A typical medical example would include covariates such as treatment assignment, as well as patient characteristics such as age at start of study, gender, and the presence of other diseases at start of study, in order to reduce variability and/or control for confounding.

The *proportional hazards condition* states that covariates are multiplicatively related to the hazard. In the simplest case of stationary coefficients, for example, a treatment with a drug may, say, halve a subject's hazard at any given time t , while the baseline hazard may vary. Note however, that this does not double the lifetime of the subject; the precise effect of the covariates on the lifetime depends on the type of $\lambda _{0}(t)$ . The covariate is not restricted to binary predictors; in the case of a continuous covariate x , it is typically assumed that the hazard responds exponentially; each unit increase in x results in proportional scaling of the hazard.

## The Cox model

### Introduction

Sir David Cox observed that if the proportional hazards assumption holds (or, is assumed to hold) then it is possible to estimate the effect parameter(s), denoted $\beta _{i}$ below, without any consideration of the full hazard function. This approach to survival data is called application of the ***Cox proportional hazards model***, sometimes abbreviated to ***Cox model*** or to *proportional hazards model*. However, Cox also noted that biological interpretation of the proportional hazards assumption can be quite tricky.

Let *X**i* = (*X**i*1, … , *X**ip*) be the realized values of the *p* covariates for subject *i*. The hazard function for the Cox proportional hazards model has the form ${\begin{aligned}\lambda (t|X_{i})&=\lambda _{0}(t)\exp(\beta _{1}X_{i1}+\cdots +\beta _{p}X_{ip})\\&=\lambda _{0}(t)\exp(X_{i}\cdot \beta )\end{aligned}}$ This expression gives the hazard function at time *t* for subject *i* with covariate vector (explanatory variables) *X**i*. Note that between subjects, the baseline hazard $\lambda _{0}(t)$ is identical (has no dependency on *i*). The only difference between subjects' hazards comes from the baseline scaling factor $\exp(X_{i}\cdot \beta )$ .

### Why it is called "proportional"

To start, suppose we only have a single covariate, x , and therefore a single coefficient, $\beta _{1}$ . Our model looks like:

$\lambda (t|x)=\lambda _{0}(t)\exp(\beta _{1}x)$

Consider the effect of increasing x by 1: ${\begin{aligned}\lambda (t|x+1)&=\lambda _{0}(t)\exp(\beta _{1}(x+1))\\&=\lambda _{0}(t)\exp(\beta _{1}x+\beta _{1})\\&={\Bigl (}\lambda _{0}(t)\exp(\beta _{1}x){\Bigr )}\exp(\beta _{1})\\&=\lambda (t|x)\exp(\beta _{1})\end{aligned}}$

We can see that increasing a covariate by 1 scales the original hazard by the constant $\exp(\beta _{1})$ . Rearranging things slightly, we see that: ${\frac {\lambda (t|x+1)}{\lambda (t|x)}}=\exp(\beta _{1})$

The right-hand-side is constant over time (no term has a t in it). This relationship, $x/y={\text{constant}}$ , is called a proportional relationship.

More generally, consider two subjects, *i* and *j*, with covariates $X_{i}$ and $X_{j}$ respectively. Consider the ratio of their hazards: ${\begin{aligned}{\frac {\lambda (t|X_{i})}{\lambda (t|X_{j})}}&={\frac {\lambda _{0}(t)\exp(X_{i}\cdot \beta )}{\lambda _{0}(t)\exp(X_{j}\cdot \beta )}}\\&={\frac {{\cancel {\lambda _{0}(t)}}\exp(X_{i}\cdot \beta )}{{\cancel {\lambda _{0}(t)}}\exp(X_{j}\cdot \beta )}}\\&=\exp((X_{i}-X_{j})\cdot \beta )\end{aligned}}$

The right-hand-side isn't dependent on time, as the only time-dependent factor, $\lambda _{0}(t)$ , was cancelled out. Thus the ratio of hazards of two subjects is a constant, i.e. the hazards are proportional.

### Absence of an intercept term

Often there is an intercept term (also called a constant term or bias term) used in regression models. The Cox model lacks one because the baseline hazard, $\lambda _{0}(t)$ , takes the place of it. Let's see what would happen if we did include an intercept term anyways, denoted $\beta _{0}$ : ${\begin{aligned}\lambda (t|X_{i})&=\lambda _{0}(t)\exp(\beta _{1}X_{i1}+\cdots +\beta _{p}X_{ip}+\beta _{0})\\&=\lambda _{0}(t)\exp(X_{i}\cdot \beta )\exp(\beta _{0})\\&=\left(\exp(\beta _{0})\lambda _{0}(t)\right)\exp(X_{i}\cdot \beta )\\&=\lambda _{0}^{*}(t)\exp(X_{i}\cdot \beta )\end{aligned}}$ where we've redefined $\exp(\beta _{0})\lambda _{0}(t)$ to be a new baseline hazard, $\lambda _{0}^{*}(t)$ . Thus, the baseline hazard incorporates *all* parts of the hazard that are not dependent on the subjects' covariates, which includes any intercept term (which is constant for all subjects, by definition). In other words, adding an intercept term would make the model unidentifiable.

### Likelihood for unique times

The Cox partial likelihood, shown below, is obtained by using Breslow's estimate of the baseline hazard function, plugging it into the full likelihood and then observing that the result is a product of two factors. The first factor is the partial likelihood shown below, in which the baseline hazard has "canceled out". It is simply the probability for subjects to have experienced events in the *order* that they actually have occurred, given the set of times of occurrences and given the subjects' covariates. The second factor is free of the regression coefficients and depends on the data only through the censoring pattern. The effect of covariates estimated by any proportional hazards model can thus be reported as hazard ratios.

To calculate the partial likelihood, the probability for the order of events, let us index the *M* samples for which events have already occurred by increasing time of occurrence, *Y*1 < *Y*2 < ... < *Y*M. Covariates of all other subjects for which no event has occurred get indices *M*+1,.., *N*. The partial likelihood can be factorized into one factor for each event that has occurred. The *i* 'th factor is the probability that out of all subjects (*i*,*i*+1,..., *N*) for which no event has occurred before time *Y*i, the one that actually occurred at time *Y*i is the event for subject *i*: $L_{i}(\beta )={\frac {\lambda (Y_{i}\mid X_{i})}{\sum _{j=i}^{N}\lambda (Y_{i}\mid X_{j})}}={\frac {\lambda _{0}(Y_{i})\theta _{i}}{\sum _{j=i}^{N}\lambda _{0}(Y_{i})\theta _{j}}}={\frac {\theta _{i}}{\sum _{j=i}^{N}\theta _{j}}},$ where *θ**i* = exp(*X**i* ⋅ *β*) and the summation is over the set of subjects *j* where the event has not occurred before time *Y**i* (including subject *i* itself). Obviously 0 < *L**i*(β) ≤ 1.

Treating the subjects as statistically independent of each other, the partial likelihood for the order of events is $L(\beta )=\prod _{i=1}^{M}L_{i}(\beta )=\prod _{i:C_{i}=1}L_{i}(\beta ),$ where the subjects for which an event has occurred are indicated by *C**i* = 1 and all others by *C**i* = 0. The corresponding log partial likelihood is $\ell (\beta )=\sum _{i:C_{i}=1}\left(X_{i}\cdot \beta -\log \sum _{j:Y_{j}\geq Y_{i}}\theta _{j}\right),$ where we have written $\sum _{j=i}^{N}$ using the indexing introduced above in a more general way, as $\sum _{j:Y_{j}\geq Y_{i}}$ . Crucially, the effect of the covariates can be estimated without the need to specify the hazard function $\lambda _{0}(t)$ over time. The partial likelihood can be maximized over *β* to produce maximum partial likelihood estimates of the model parameters.

The partial score function is $\ell ^{\prime }(\beta )=\sum _{i:C_{i}=1}\left(X_{i}-{\frac {\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}X_{j}}{\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}}}\right),$

and the Hessian matrix of the partial log likelihood is $\ell ^{\prime \prime }(\beta )=-\sum _{i:C_{i}=1}\left({\frac {\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}X_{j}X_{j}^{\prime }}{\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}}}-{\frac {\left[\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}X_{j}\right]\left[\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}X_{j}^{\prime }\right]}{\left[\sum _{j:Y_{j}\geq Y_{i}}\theta _{j}\right]^{2}}}\right).$

Using this score function and Hessian matrix, the partial likelihood can be maximized using the Newton-Raphson algorithm. The inverse of the Hessian matrix, evaluated at the estimate of *β*, can be used as an approximate variance-covariance matrix for the estimate, and used to produce approximate standard errors for the regression coefficients.

### Likelihood when there exist tied times

Several approaches have been proposed to handle situations in which there are ties in the time data. *Breslow's method* describes the approach in which the procedure described above is used unmodified, even when ties are present. An alternative approach that is considered to give better results is *Efron's method*. Let *t**j* denote the unique times, let *H**j* denote the set of indices *i* such that *Y**i* = *t**j* and *C**i* = 1, and let *m**j* = |*H**j*|. Efron's approach maximizes the following partial likelihood. $L(\beta )=\prod _{j}{\frac {\prod _{i\in H_{j}}\theta _{i}}{\prod _{\ell =0}^{m_{j}-1}\left[\sum _{i:Y_{i}\geq t_{j}}\theta _{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}\right]}}.$

The corresponding log partial likelihood is $\ell (\beta )=\sum _{j}\left(\sum _{i\in H_{j}}X_{i}\cdot \beta -\sum _{\ell =0}^{m_{j}-1}\log \left(\sum _{i:Y_{i}\geq t_{j}}\theta _{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}\right)\right),$ the score function is $\ell ^{\prime }(\beta )=\sum _{j}\left(\sum _{i\in H_{j}}X_{i}-\sum _{\ell =0}^{m_{j}-1}{\frac {\sum _{i:Y_{i}\geq t_{j}}\theta _{i}X_{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}X_{i}}{\sum _{i:Y_{i}\geq t_{j}}\theta _{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}}}\right),$ and the Hessian matrix is $\ell ^{\prime \prime }(\beta )=-\sum _{j}\sum _{\ell =0}^{m_{j}-1}\left({\frac {\sum _{i:Y_{i}\geq t_{j}}\theta _{i}X_{i}X_{i}^{\prime }-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}X_{i}X_{i}^{\prime }}{\phi _{j,\ell ,m_{j}}}}-{\frac {Z_{j,\ell ,m_{j}}Z_{j,\ell ,m_{j}}^{\prime }}{\phi _{j,\ell ,m_{j}}^{2}}}\right),$ where $\phi _{j,\ell ,m_{j}}=\sum _{i:Y_{i}\geq t_{j}}\theta _{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}$ $Z_{j,\ell ,m_{j}}=\sum _{i:Y_{i}\geq t_{j}}\theta _{i}X_{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}X_{i}.$

Note that when *H**j* is empty (all observations with time *t**j* are censored), the summands in these expressions are treated as zero.

### Examples

Below are some worked examples of the Cox model in practice.

#### A single binary covariate

Suppose the endpoint we are interested in is patient survival during a 5-year observation period after a surgery. Patients can die within the 5-year period, and we record when they died, or patients can live past 5 years, and we only record that they lived past 5 years. The surgery was performed at one of two hospitals, *A* or *B*, and we would like to know if the hospital location is associated with 5-year survival. Specifically, we would like to know the *relative* increase (or decrease) in hazard from a surgery performed at hospital A compared to hospital B. Provided is some (fake) data, where each row represents a patient: *T* is how long the patient was observed for before death or 5 years (measured in months), and *C* denotes if the patient died in the 5-year period. We have encoded the hospital as a binary variable denoted *X*: 1 if from hospital *A*, 0 from hospital *B*.

| hospital | X | T | C |
|---|---|---|---|
| B | 0 | 60 | False |
| B | 0 | 32 | True |
| B | 0 | 60 | False |
| B | 0 | 60 | False |
| B | 0 | 60 | False |
| A | 1 | 4 | True |
| A | 1 | 18 | True |
| A | 1 | 60 | False |
| A | 1 | 9 | True |
| A | 1 | 31 | True |
| A | 1 | 53 | True |
| A | 1 | 17 | True |

Our single-covariate Cox proportional model looks like the following, with $\beta _{1}$ representing the hospital's effect, and *i* indexing each patient: $\overbrace {\lambda (t|X_{i})} ^{\text{hazard for i}}=\underbrace {\lambda _{0}(t)} _{{\text{baseline}} \atop {\text{hazard}}}\cdot \overbrace {\exp(\beta _{1}X_{i})} ^{\text{scaling factor for i}}$

Using statistical software, we can estimate $\beta _{1}$ to be 2.12. The hazard ratio is the *exponential* of this value, $\exp(\beta _{1})=\exp(2.12)$ . To see why, consider the ratio of hazards, specifically: ${\frac {\lambda (t|X=1)}{\lambda (t|X=0)}}={\frac {{\cancel {\lambda _{0}(t)}}\exp(\beta _{1}\cdot 1)}{{\cancel {\lambda _{0}(t)}}\exp(\beta _{1}\cdot 0)}}=\exp(\beta _{1})$

Thus, the hazard ratio of hospital A to hospital B is $\exp(2.12)=8.32$ . Putting aside statistical significance for a moment, we can make a statement saying that patients in hospital A are associated with a 8.3x higher risk of death occurring in any short period of time compared to hospital B.

There are important caveats to mention about the interpretation:

1. a 8.3x higher risk of death does not mean that 8.3x more patients will die in hospital A: survival analysis examines how quickly events occur, not simply whether they occur.
2. More specifically, "risk of death" is a measure of a rate. A rate has units, like meters per second. However, a *relative* rate does not: a bicycle can go two times faster than another bicycle (the reference bicycle), without specifying any units. Likewise, the risk of death (comparable to the speed of a bike) in hospital *A* is 8.3 times higher (faster) than the risk of death in hospital *B* (the reference group).
3. the inverse quantity, $1/8.32={\frac {1}{\exp(2.12)}}=\exp(-2.12)=0.12$ is the hazard ratio of hospital *B* relative to hospital *A*.
4. We haven't made any inferences about *probabilities* of survival between the hospitals. This is because we would need an estimate of the baseline hazard rate, $\lambda _{0}(t)$ , as well as our $\beta _{1}$ estimate. However, standard estimation of the Cox proportional hazard model does not directly estimate the baseline hazard rate.
5. Because we have ignored the only time varying component of the model, the baseline hazard rate, our estimate is timescale-invariant. For example, if we had measured time in years instead of months, we would get the same estimate.
6. It is tempting to say that the hospital *caused* the difference in hazards between the two groups, but since our study is not causal (that is, we do not know how the data was generated), we stick with terminology like "associated".

#### A single continuous covariate

To demonstrate a less traditional use case of survival analysis, the next example will be an economics question: what is the relationship between a company's price-to-earnings ratio (P/E) on their first IPO anniversary and their future survival? More specifically, if we consider a company's "birth event" to be their first IPO anniversary, and any bankruptcy, sale, going private, etc. as a "death" event the company, we'd like to know the influence of the companies' P/E ratio at their "birth" (first IPO anniversary) on their survival.

Provided is a (fake) dataset with survival data from 12 companies: *T* represents the number of days between first IPO anniversary and death (or an end date of 2022-01-01, if did not die). *C* represents if the company died before 2022-01-01 or not. P/E represents the company's price-to-earnings ratio at its 1st IPO anniversary.

| Co. | 1 year IPO date | Death date* | C | T | P/E |
|---|---|---|---|---|---|
| 0 | 2000-11-05 | 2011-01-22 | True | 3730 | 9.7 |
| 1 | 2000-12-01 | 2003-03-30 | True | 849 | 12.0 |
| 2 | 2011-01-05 | 2012-03-30 | True | 450 | 3.0 |
| 3 | 2010-05-29 | 2011-02-22 | True | 269 | 5.3 |
| 4 | 2005-06-23 | 2022-01-01 | False | 6036 | 10.8 |
| 5 | 2000-06-10 | 2002-07-24 | True | 774 | 6.3 |
| 6 | 2011-07-11 | 2014-05-01 | True | 1025 | 11.6 |
| 7 | 2007-09-27 | 2022-01-01 | False | 5210 | 10.3 |
| 8 | 2006-07-30 | 2010-06-03 | True | 1404 | 8.0 |
| 9 | 2000-07-13 | 2001-07-19 | True | 371 | 4.0 |
| 10 | 2013-06-10 | 2018-10-10 | True | 1948 | 5.9 |
| 11 | 2011-07-16 | 2014-08-15 | True | 1126 | 8.3 |

Unlike the previous example where there was a binary variable, this dataset has a continuous variable, P/E; however, the model looks similar: $\lambda (t|P_{i})=\lambda _{0}(t)\cdot \exp(\beta _{1}P_{i})$ where $P_{i}$ represents a company's P/E ratio. Running this dataset through a Cox model produces an *estimate* of the value of the unknown $\beta _{1}$ , which is -0.34. Therefore, an estimate of the entire hazard is: $\lambda (t|P_{i})=\lambda _{0}(t)\cdot \exp(-0.34P_{i})$

Since the baseline hazard, $\lambda _{0}(t)$ , was not estimated, the entire hazard is not able to be calculated. However, consider the ratio of the companies *i* and *j'*s hazards: ${\begin{aligned}{\frac {\lambda (t|P_{i})}{\lambda (t|P_{j})}}&={\frac {{\cancel {\lambda _{0}(t)}}\cdot \exp(-0.34P_{i})}{{\cancel {\lambda _{0}(t)}}\cdot \exp(-0.34P_{j})}}\\&=\exp(-0.34(P_{i}-P_{j}))\end{aligned}}$

All terms on the right are known, so calculating the ratio of hazards between companies is possible. Since there is no time-dependent term on the right (all terms are constant), the hazards are *proportional* to each other. For example, the hazard ratio of company 5 to company 2 is $\exp(-0.34(6.3-3.0))=0.33$ . This means that, within the interval of study, company 5's risk of "death" is 0.33 ≈ 1/3 as large as company 2's risk of death.

There are important caveats to mention about the interpretation:

1. The *hazard ratio* is the quantity $\exp(\beta _{1})$ , which is $\exp(-0.34)=0.71$ in the above example. From the last calculation above, an interpretation of this is as the ratio of hazards between two "subjects" that have their variables differ by one unit: if $P_{i}=P_{j}+1$ , then $\exp(\beta _{1}(P_{i}-P_{j})=\exp(\beta _{1}(1))$ . The choice of "differ by one unit" is convenience, as it communicates precisely the value of $\beta _{1}$ .
2. The baseline hazard can be represented when the scaling factor is 1, i.e. $P=0$ . $\lambda (t|P_{i}=0)=\lambda _{0}(t)\cdot \exp(-0.34\cdot 0)=\lambda _{0}(t)$ Can we interpret the baseline hazard as the hazard of a "baseline" company whose P/E happens to be 0? This interpretation of the baseline hazard as "hazard of a baseline subject" is imperfect, as the covariate being 0 is impossible in this application: a P/E of 0 is meaningless (it means the company's stock price is 0, i.e., they are "dead"). A more appropriate interpretation would be "the hazard when all variables are nil".
3. It is tempting to want to understand and interpret a value like $\exp(\beta _{1}P_{i})$ to represent the hazard of a company. However, consider what this is actually representing: $\exp(\beta _{1}P_{i})=\exp(\beta _{1}(P_{i}-0))={\frac {\exp(\beta _{1}P_{i})}{\exp(\beta _{1}0)}}={\frac {\lambda (t|P_{i})}{\lambda (t|0)}}$ . There is implicitly a ratio of hazards here, comparing company *i'*s hazard to an imaginary baseline company with 0 P/E. However, as explained above, a P/E of 0 is impossible in this application, so $\exp(\beta _{1}P_{i})$ is meaningless in this example. Ratios between plausible hazards are meaningful, however.

## Time-varying predictors and coefficients

Extensions to time dependent variables, time dependent strata, and multiple events per subject, can be incorporated by the counting process formulation of Andersen and Gill. One example of the use of hazard models with time-varying regressors is estimating the effect of unemployment insurance on unemployment spells.

In addition to allowing time-varying covariates (i.e., predictors), the Cox model may be generalized to time-varying coefficients as well. That is, the proportional effect of a treatment may vary with time; e.g. a drug may be very effective if administered within one month of morbidity, and become less effective as time goes on. The hypothesis of no change with time (stationarity) of the coefficient may then be tested. Details and software (R package) are available in Martinussen and Scheike (2006).

In this context, it could also be mentioned that it is theoretically possible to specify the effect of covariates by using additive hazards, i.e. specifying $\lambda (t|X_{i})=\lambda _{0}(t)+\beta _{1}X_{i1}+\cdots +\beta _{p}X_{ip}=\lambda _{0}(t)+X_{i}\cdot \beta .$ If such additive hazards models are used in situations where (log-)likelihood maximization is the objective, care must be taken to restrict $\lambda (t\mid X_{i})$ to non-negative values. Perhaps as a result of this complication, such models are seldom seen. If the objective is instead least squares the non-negativity restriction is not strictly required.

## Specifying the baseline hazard function

The Cox model may be specialized if a reason exists to assume that the baseline hazard follows a particular form. In this case, the baseline hazard $\lambda _{0}(t)$ is replaced by a given function. For example, assuming the hazard function to be the *Weibull* hazard function gives the *Weibull proportional hazards model*.

Incidentally, using the Weibull baseline hazard is the only circumstance under which the model satisfies both the proportional hazards, and accelerated failure time models.

The generic term *parametric proportional hazards models* can be used to describe proportional hazards models in which the hazard function is specified. The Cox proportional hazards model is sometimes called a *semiparametric model* by contrast.

Some authors use the term *Cox proportional hazards model* even when specifying the underlying hazard function, to acknowledge the debt of the entire field to David Cox.

The term *Cox regression model* (omitting *proportional hazards*) is sometimes used to describe the extension of the Cox model to include time-dependent factors. However, this usage is potentially ambiguous since the Cox proportional hazards model can itself be described as a regression model.

## Relationship to Poisson models

There is a relationship between proportional hazards models and Poisson regression models which is sometimes used to fit approximate proportional hazards models in software for Poisson regression. The usual reason for doing this is that calculation is much quicker. This was more important in the days of slower computers but can still be useful for particularly large data sets or complex problems. Laird and Olivier (1981) provide the mathematical details. They note, "we do not assume [the Poisson model] is true, but simply use it as a device for deriving the likelihood." McCullagh and Nelder's book on generalized linear models has a chapter on converting proportional hazards models to generalized linear models.

## Under high-dimensional setup

In high-dimension, when number of covariates p is large compared to the sample size n, the LASSO method is one of the classical model-selection strategies. Tibshirani (1997) has proposed a Lasso procedure for the proportional hazard regression parameter. The Lasso estimator of the regression parameter β is defined as the minimizer of the opposite of the Cox partial log-likelihood under an L1-norm type constraint. $\ell (\beta )=\sum _{j}\left(\sum _{i\in H_{j}}X_{i}\cdot \beta -\sum _{\ell =0}^{m_{j}-1}\log \left(\sum _{i:Y_{i}\geq t_{j}}\theta _{i}-{\frac {\ell }{m_{j}}}\sum _{i\in H_{j}}\theta _{i}\right)\right)+\lambda \|\beta \|_{1},$

There has been theoretical progress on this topic recently.

## Software implementations

- **Mathematica**: `CoxModelFit` function.
- **R**: `coxph()` function, located in the **survival** package.
- **SAS**: `phreg` procedure
- **Stata**: `stcox` command
- **Python**: `CoxPHFitter` located in the **lifelines** library. `phreg` in the statsmodels library.
- **SPSS**: Available under **Cox Regression**.
- **MATLAB**: `fitcox` or `coxphfit` function
- **Julia**: Available in the **Survival.jl** library.
- **JMP**: Available in **Fit Proportional Hazards** platform.
- **Prism**: Available in Survival Analyses and Multiple Variable Analyses

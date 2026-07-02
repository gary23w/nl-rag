---
title: "Kriging"
source: https://en.wikipedia.org/wiki/Kriging
domain: gaussian-processes-sci
license: CC-BY-SA-4.0
tags: gaussian process regression, covariance function, bayesian optimization, radial basis kernel
fetched: 2026-07-02
---

# Kriging

In statistics, originally in geostatistics, **kriging** or **Kriging** (/ˈkriːɡɪŋ/), also known as **Gaussian process regression**, is a method of interpolation based on Gaussian process governed by prior covariances. Under suitable assumptions of the prior, kriging gives the best linear unbiased prediction (BLUP) at unsampled locations. Interpolating methods based on other criteria such as smoothness (e.g., smoothing spline) may not yield the BLUP. The method is widely used in the domain of spatial analysis and computer experiments. The technique is also known as **Wiener–Kolmogorov prediction**, after Norbert Wiener and Andrey Kolmogorov.

The theoretical basis for the method was developed by the French mathematician Georges Matheron in 1960, based on the master's thesis of Danie G. Krige, the pioneering plotter of distance-weighted average gold grades at the Witwatersrand reef complex in South Africa. Krige sought to estimate the most likely distribution of gold based on samples from a few boreholes. The English verb is *to krige*, and the most common noun is *kriging*. The word is sometimes capitalized as *Kriging* in the literature.

Though computationally intensive in its basic formulation, kriging can be scaled to larger problems using various approximation methods.

## Main principles

Kriging predicts the value of a function at a given point by computing a weighted average of the known values of the function in the neighborhood of the point. The method is closely related to regression analysis. Both theories derive a best linear unbiased estimator based on assumptions on covariances, make use of Gauss–Markov theorem to prove independence of the estimate and error, and use very similar formulae. Even so, they are useful in different frameworks: kriging is made for estimation of a single realization of a random field, while regression models are based on multiple observations of a multivariate data set.

The kriging estimation may also be seen as a spline in a reproducing kernel Hilbert space, with the reproducing kernel given by the covariance function. The difference with the classical kriging approach is provided by the interpretation: while the spline is motivated by a minimum-norm interpolation based on a Hilbert-space structure, kriging is motivated by an expected squared prediction error based on a stochastic model.

Kriging with *polynomial trend surfaces* is mathematically identical to generalized least squares polynomial curve fitting.

Kriging can also be understood as a form of Bayesian optimization. Kriging starts with a prior distribution over functions. This prior takes the form of a Gaussian process: N samples from a function will be normally distributed, where the covariance between any two samples is the covariance function (or kernel) of the Gaussian process evaluated at the spatial location of two points. A set of values is then observed, each value associated with a spatial location. Now, a new value can be predicted at any new spatial location by combining the Gaussian prior with a Gaussian likelihood function for each of the observed values. The resulting posterior distribution is also Gaussian, with a mean and covariance that can be simply computed from the observed values, their variance, and the kernel matrix derived from the prior.

### Geostatistical estimator

In geostatistical models, sampled data are interpreted as the result of a random process. The fact that these models incorporate uncertainty in their conceptualization does not mean that the phenomenon – the forest, the aquifer, the mineral deposit – has resulted from a random process, but rather it allows one to build a methodological basis for the spatial inference of quantities in unobserved locations and to quantify the uncertainty associated with the estimator.

A stochastic process is, in the context of this model, simply a way to approach the set of data collected from the samples. The first step in geostatistical modulation is to create a random process that best describes the set of observed data.

A value from location $x_{1}$ (generic denomination of a set of geographic coordinates) is interpreted as a realization $z(x_{1})$ of the random variable $Z(x_{1})$ . In the space A , where the set of samples is dispersed, there are N realizations of the random variables $Z(x_{1}),Z(x_{2}),\ldots ,Z(x_{N})$ , correlated between themselves.

The set of random variables constitutes a random function, of which only one realization is known – the set $z(x_{i})$ of observed data. With only one realization of each random variable, it's theoretically impossible to determine any statistical parameter of the individual variables or the function. The proposed solution in the geostatistical formalism consists in *assuming* various degrees of *stationarity* in the random function, in order to make the inference of some statistic values possible.

For instance, if one assumes, based on the homogeneity of samples in area A where the variable is distributed, the hypothesis that the first moment is stationary (i.e. all random variables have the same mean), then one is assuming that the mean can be estimated by the arithmetic mean of sampled values.

The hypothesis of stationarity related to the second moment is defined in the following way: the correlation between two random variables solely depends on the spatial distance between them and is independent of their location. Thus if $\mathbf {h} =x_{2}-x_{1}$ and $h=|\mathbf {h} |$ , then:

$C{\big (}Z(x_{1}),Z(x_{2}){\big )}=C{\big (}Z(x_{i}),Z(x_{i}+\mathbf {h} ){\big )}=C(h),$

$\gamma {\big (}Z(x_{1}),Z(x_{2}){\big )}=\gamma {\big (}Z(x_{i}),Z(x_{i}+\mathbf {h} ){\big )}=\gamma (h).$

For simplicity, we define $C(x_{i},x_{j})=C{\big (}Z(x_{i}),Z(x_{j}){\big )}$ and $\gamma (x_{i},x_{j})=\gamma {\big (}Z(x_{i}),Z(x_{j}){\big )}$ .

This hypothesis allows one to infer those two measures – the variogram and the covariogram:

$\gamma (h)={\frac {1}{2|N(h)|}}\sum _{(i,j)\in N(h)}{\big (}Z(x_{i})-Z(x_{j}){\big )}^{2},$

$C(h)={\frac {1}{|N(h)|}}\sum _{(i,j)\in N(h)}{\big (}Z(x_{i})-m(h){\big )}{\big (}Z(x_{j})-m(h){\big )},$

where:

$m(h)={\frac {1}{2|N(h)|}}\sum _{(i,j)\in N(h)}\left(Z(x_{i})+Z(x_{j})\right)$

;

$N(h)$

denotes the set of pairs of observations

$i,\;j$

such that

$|x_{i}-x_{j}|=h$

, and

$|N(h)|$

is the number of pairs in the set.

In this set, $(i,\;j)$ and $(j,\;i)$ denote the same element. Generally an "approximate distance" h is used, implemented using a certain tolerance.

### Linear estimation

Spatial inference, or estimation, of a quantity $Z\colon \mathbb {R} ^{n}\to \mathbb {R}$ , at an unobserved location $x_{0}$ , is calculated from a linear combination of the observed values $z_{i}=Z(x_{i})$ and weights $w_{i}(x_{0}),\;i=1,\ldots ,N$ :

${\hat {Z}}(x_{0})={\begin{bmatrix}w_{1}&w_{2}&\cdots &w_{N}\end{bmatrix}}{\begin{bmatrix}z_{1}\\z_{2}\\\vdots \\z_{N}\end{bmatrix}}=\sum _{i=1}^{N}w_{i}(x_{0})Z(x_{i}).$

The weights $w_{i}$ are intended to summarize two extremely important procedures in a spatial inference process:

- reflect the structural "proximity" of samples to the estimation location $x_{0}$ ;
- at the same time, they should have a desegregation effect, in order to avoid bias caused by eventual sample *clusters*.

When calculating the weights $w_{i}$ , there are two objectives in the geostatistical formalism: *unbias* and *minimal variance of estimation*.

If the cloud of real values $Z(x_{0})$ is plotted against the estimated values ${\hat {Z}}(x_{0})$ , the criterion for global unbias, *intrinsic stationarity* or wide sense stationarity of the field, implies that the mean of the estimations must be equal to mean of the real values.

The second criterion says that the mean of the squared deviations ${\big (}{\hat {Z}}(x)-Z(x){\big )}$ must be minimal, which means that when the cloud of estimated values *versus* the cloud real values is more disperse, the estimator is more imprecise.

## Methods

Depending on the stochastic properties of the random field and the various degrees of stationarity assumed, different methods for calculating the weights can be deduced, i.e. different types of kriging apply. Classical methods are:

- *Ordinary kriging* assumes constant unknown mean only over the search neighborhood of $x_{0}$ .
- *Simple kriging* assumes stationarity of the first moment over the entire domain with a known mean: $E\{Z(x)\}=E\{Z(x_{0})\}=m$ , where m is the known mean.
- *Universal kriging* assumes a general polynomial trend model, such as linear trend model $\textstyle E\{Z(x)\}=\sum _{k=0}^{p}\beta _{k}f_{k}(x)$ .
- *IRFk-kriging* assumes $E\{Z(x)\}$ to be an unknown polynomial in x .
- *Indicator kriging* uses indicator functions instead of the process itself, in order to estimate transition probabilities.
  - *Multiple-indicator kriging* is a version of indicator kriging working with a family of indicators. Initially, MIK showed considerable promise as a new method that could more accurately estimate overall global mineral deposit concentrations or grades. However, these benefits have been outweighed by other inherent problems of practicality in modelling due to the inherently large block sizes used and also the lack of mining scale resolution. Conditional simulation is fast, becoming the accepted replacement technique in this case.
- *Disjunctive kriging* is a nonlinear generalisation of kriging.
- *Log-normal kriging* interpolates positive data by means of logarithms.
- *Latent kriging* assumes the various krigings on the latent level (second stage) of the nonlinear mixed-effects model to produce a spatial functional prediction. This technique is useful when analyzing a spatial functional data $\{(y_{i},x_{i},s_{i})\}_{i=1}^{n}$ , where $y_{i}=(y_{i1},y_{i2},\cdots ,y_{iT_{i}})^{\top }$ is a time series data over $T_{i}$ period, $x_{i}=(x_{i1},x_{i2},\cdots ,x_{ip})^{\top }$ is a vector of p covariates, and $s_{i}=(s_{i1},s_{i2})^{\top }$ is a spatial location (longitude, latitude) of the i -th subject.
- *Co-kriging* denotes the joint kriging of data from multiple sources with a relationship between the different data sources. Co-kriging is also possible in a Bayesian approach.
- *Bayesian kriging* departs from the optimization of unknown coefficients and hyperparameters, which is understood as a maximum likelihood estimate from the Bayesian perspective. Instead, the coefficients and hyperparameters are estimated from their expectation values. An advantage of Bayesian kriging is, that it allows to quantify the evidence for and the uncertainty of the kriging emulator. If the emulator is employed to propagate uncertainties, the quality of the kriging emulator can be assessed by comparing the emulator uncertainty to the total uncertainty (see also Bayesian Polynomial Chaos). Bayesian kriging can also be mixed with co-kriging.

### Ordinary kriging

The unknown value $Z(x_{0})$ is interpreted as a random variable located in $x_{0}$ , as well as the values of neighbors samples $Z(x_{i}),\ i=1,\ldots ,N$ . The estimator ${\hat {Z}}(x_{0})$ is also interpreted as a random variable located in $x_{0}$ , a result of the linear combination of variables.

Kriging seeks to minimize the mean square value of the following error in estimating $Z(x_{0})$ , subject to lack of bias:

$\epsilon (x_{0})={\hat {Z}}(x_{0})-Z(x_{0})={\begin{bmatrix}W^{T}&-1\end{bmatrix}}\cdot {\begin{bmatrix}Z(x_{1})&\cdots &Z(x_{N})&Z(x_{0})\end{bmatrix}}^{T}=\sum _{i=1}^{N}w_{i}(x_{0})\times Z(x_{i})-Z(x_{0}).$

The two quality criteria referred to previously can now be expressed in terms of the mean and variance of the new random variable $\epsilon (x_{0})$ :

**Lack of bias**

Since the random function is stationary, $E[Z(x_{i})]=E[Z(x_{0})]=m$ , the weights must sum to 1 in order to ensure that the model is unbiased. This can be seen as follows:

$E[\epsilon (x_{0})]=0\Leftrightarrow \sum _{i=1}^{N}w_{i}(x_{0})\times E[Z(x_{i})]-E[Z(x_{0})]=0$

$\Leftrightarrow m\sum _{i=1}^{N}w_{i}(x_{0})-m=0\Leftrightarrow \sum _{i=1}^{N}w_{i}(x_{0})=1\Leftrightarrow \mathbf {1} ^{T}\cdot W=1.$

**Minimum variance**

Two estimators can have $E[\epsilon (x_{0})]=0$ , but the dispersion around their mean determines the difference between the quality of estimators. To find an estimator with minimum variance, we need to minimize $E[\epsilon (x_{0})^{2}]$ .

${\begin{aligned}\operatorname {Var} (\epsilon (x_{0}))&=\operatorname {Var} \left({\begin{bmatrix}W^{T}&-1\end{bmatrix}}\cdot {\begin{bmatrix}Z(x_{1})&\cdots &Z(x_{N})&Z(x_{0})\end{bmatrix}}^{T}\right)\\&={\begin{bmatrix}W^{T}&-1\end{bmatrix}}\cdot \operatorname {Var} \left({\begin{bmatrix}Z(x_{1})&\cdots &Z(x_{N})&Z(x_{0})\end{bmatrix}}^{T}\right)\cdot {\begin{bmatrix}W\\-1\end{bmatrix}}.\end{aligned}}$

See covariance matrix for a detailed explanation.

$\operatorname {Var} (\epsilon (x_{0}))={\begin{bmatrix}W^{T}&-1\end{bmatrix}}\cdot {\begin{bmatrix}\operatorname {Var} _{x_{i}}&\operatorname {Cov} _{x_{i}x_{0}}\\\operatorname {Cov} _{x_{i}x_{0}}^{T}&\operatorname {Var} _{x_{0}}\end{bmatrix}}\cdot {\begin{bmatrix}W\\-1\end{bmatrix}},$

where the literals $\left\{\operatorname {Var} _{x_{i}},\operatorname {Var} _{x_{0}},\operatorname {Cov} _{x_{i}x_{0}}\right\}$ stand for

$\left\{\operatorname {Var} \left({\begin{bmatrix}Z(x_{1})&\cdots &Z(x_{N})\end{bmatrix}}^{T}\right),\operatorname {Var} {\big (}Z(x_{0}){\big )},\operatorname {Cov} \left({\begin{bmatrix}Z(x_{1})&\cdots &Z(x_{N})\end{bmatrix}}^{T},Z(x_{0})\right)\right\}.$

Once defined the covariance model or variogram, $C(\mathbf {h} )$ or $\gamma (\mathbf {h} )$ , valid in all field of analysis of $Z(x)$ , then we can write an expression for the estimation variance of any estimator in function of the covariance between the samples and the covariances between the samples and the point to estimate:

${\begin{cases}\operatorname {Var} {\big (}\epsilon (x_{0}){\big )}=W^{T}\cdot \operatorname {Var} _{x_{i}}\cdot W-\operatorname {Cov} _{x_{i}x_{0}}^{T}\cdot W-W^{T}\cdot \operatorname {Cov} _{x_{i}x_{0}}+\operatorname {Var} _{x_{0}},\\\operatorname {Var} {\big (}\epsilon (x_{0}){\big )}=\operatorname {Cov} (0)+\sum _{i}\sum _{j}w_{i}w_{j}\operatorname {Cov} (x_{i},x_{j})-2\sum _{i}w_{i}C(x_{i},x_{0}).\end{cases}}$

Some conclusions can be asserted from this expression. The variance of estimation:

- is not quantifiable to any linear estimator, once the stationarity of the mean and of the spatial covariances, or variograms, are assumed;
- grows when the covariance between the samples and the point to estimate decreases. This means that, when the samples are farther away from $x_{0}$ , the estimation becomes worse;
- grows with the a priori variance $C(0)$ of the variable $Z(x)$ ; when the variable is less disperse, the variance is lower in any point of the area A ;
- does not depend on the values of the samples, which means that the same spatial configuration (with the same geometrical relations between samples and the point to estimate) always reproduces the same estimation variance in any part of the area A ; this way, the variance does not measure the uncertainty of estimation produced by the local variable.

**System of equations**

$W={\underset {\mathbf {1} ^{T}\cdot W=1}{\operatorname {arg\,min} }}\left(W^{T}\cdot \operatorname {Var} _{x_{i}}\cdot W-\operatorname {Cov} _{x_{i}x_{0}}^{T}\cdot W-W^{T}\cdot \operatorname {Cov} _{x_{i}x_{0}}+\operatorname {Var} _{x_{0}}\right).$

Solving this optimization problem (see Lagrange multipliers) results in the *kriging system*:

${\begin{bmatrix}{\hat {W}}\\\mu \end{bmatrix}}={\begin{bmatrix}\operatorname {Var} _{x_{i}}&\mathbf {1} \\\mathbf {1} ^{T}&0\end{bmatrix}}^{-1}\cdot {\begin{bmatrix}\operatorname {Cov} _{x_{i}x_{0}}\\1\end{bmatrix}}={\begin{bmatrix}\gamma (x_{1},x_{1})&\cdots &\gamma (x_{1},x_{n})&1\\\vdots &\ddots &\vdots &\vdots \\\gamma (x_{n},x_{1})&\cdots &\gamma (x_{n},x_{n})&1\\1&\cdots &1&0\end{bmatrix}}^{-1}{\begin{bmatrix}\gamma (x_{1},x^{*})\\\vdots \\\gamma (x_{n},x^{*})\\1\end{bmatrix}}.$

The additional parameter $\mu$ is a Lagrange multiplier used in the minimization of the kriging error $\sigma _{k}^{2}(x)$ to honor the unbiasedness condition.

### Simple kriging

Simple kriging is mathematically the simplest, but the least general. It assumes the expectation of the random field is known and relies on a covariance function. However, in most applications neither the expectation nor the covariance are known beforehand.

The practical assumptions for the application of *simple kriging* are:

- Wide-sense stationarity of the field (variance stationary).
- The expectation is zero everywhere: $\mu (x)=0$ .
- Known covariance function $c(x,y)=\operatorname {Cov} {\big (}Z(x),Z(y){\big )}$ .

The covariance function is a crucial design choice, since it stipulates the properties of the Gaussian process and thereby the behaviour of the model. The covariance function encodes information about, for instance, smoothness and periodicity, which is reflected in the estimate produced. A very common covariance function is the squared exponential, which heavily favours smooth function estimates. For this reason, it can produce poor estimates in many real-world applications, especially when the true underlying function contains discontinuities and rapid changes.

**System of equations**

The *kriging weights* of *simple kriging* have no unbiasedness condition and are given by the *simple kriging equation system*:

${\begin{pmatrix}w_{1}\\\vdots \\w_{n}\end{pmatrix}}={\begin{pmatrix}c(x_{1},x_{1})&\cdots &c(x_{1},x_{n})\\\vdots &\ddots &\vdots \\c(x_{n},x_{1})&\cdots &c(x_{n},x_{n})\end{pmatrix}}^{-1}{\begin{pmatrix}c(x_{1},x_{0})\\\vdots \\c(x_{n},x_{0})\end{pmatrix}}.$

This is analogous to a linear regression of $Z(x_{0})$ on the other $z_{1},\ldots ,z_{n}$ .

**Estimation**

The interpolation by simple kriging is given by

${\hat {Z}}(x_{0})={\begin{pmatrix}z_{1}\\\vdots \\z_{n}\end{pmatrix}}'{\begin{pmatrix}c(x_{1},x_{1})&\cdots &c(x_{1},x_{n})\\\vdots &\ddots &\vdots \\c(x_{n},x_{1})&\cdots &c(x_{n},x_{n})\end{pmatrix}}^{-1}{\begin{pmatrix}c(x_{1},x_{0})\\\vdots \\c(x_{n},x_{0})\end{pmatrix}}.$

The kriging error is given by

$\operatorname {Var} {\big (}{\hat {Z}}(x_{0})-Z(x_{0}){\big )}=\underbrace {c(x_{0},x_{0})} _{\operatorname {Var} {\big (}Z(x_{0}){\big )}}-\underbrace {{\begin{pmatrix}c(x_{1},x_{0})\\\vdots \\c(x_{n},x_{0})\end{pmatrix}}'{\begin{pmatrix}c(x_{1},x_{1})&\cdots &c(x_{1},x_{n})\\\vdots &\ddots &\vdots \\c(x_{n},x_{1})&\cdots &c(x_{n},x_{n})\end{pmatrix}}^{-1}{\begin{pmatrix}c(x_{1},x_{0})\\\vdots \\c(x_{n},x_{0})\end{pmatrix}}} _{\operatorname {Var} {\big (}{\hat {Z}}(x_{0}){\big )}},$

which leads to the generalised least-squares version of the Gauss–Markov theorem (Chiles & Delfiner 1999, p. 159):

$\operatorname {Var} {\big (}Z(x_{0}){\big )}=\operatorname {Var} {\big (}{\hat {Z}}(x_{0}){\big )}+\operatorname {Var} {\big (}{\hat {Z}}(x_{0})-Z(x_{0}){\big )}.$

### Bayesian kriging

*See also Bayesian Polynomial Chaos*

### Properties

- The kriging estimation is unbiased: $E[{\hat {Z}}(x_{i})]=E[Z(x_{i})]$ .
- The kriging estimation honors the actually observed value: ${\hat {Z}}(x_{i})=Z(x_{i})$ (assuming no measurement error is incurred).
- The kriging estimation ${\hat {Z}}(x)$ is the best linear unbiased estimator of $Z(x)$ if the assumptions hold. However (e.g. Cressie 1993):
  - As with any method, if the assumptions do not hold, kriging might be bad.
  - There might be better nonlinear and/or biased methods.
  - No properties are guaranteed when the wrong variogram is used. However, typically still a "good" interpolation is achieved.
  - Best is not necessarily good: e.g. in case of no spatial dependence the kriging interpolation is only as good as the arithmetic mean.
- Kriging provides $\sigma _{k}^{2}$ as a measure of precision. However, this measure relies on the correctness of the variogram.

## Applications

Although kriging was developed originally for applications in geostatistics, it is a general method of statistical interpolation and can be applied within any discipline to sampled data from random fields that satisfy the appropriate mathematical assumptions. It can be used where spatially related data has been collected (in 2-D or 3-D) and estimates of "fill-in" data are desired in the locations (spatial gaps) between the actual measurements.

To date kriging has been used in a variety of disciplines, including the following:

- Environmental science
- Hydrogeology
- Mining
- Natural resources
- Remote sensing
- Real estate appraisal
- Integrated circuit analysis and optimization
- Modelling of microwave devices
- Astronomy
- Prediction of oil production curve of shale oil wells

### Design and analysis of computer experiments

Another very important and rapidly growing field of application, in engineering, is the interpolation of data coming out as response variables of deterministic computer simulations, e.g. finite element method (FEM) simulations. In this case, kriging is used as a metamodeling tool, i.e. a black-box model built over a designed set of computer experiments. In many practical engineering problems, such as the design of a metal forming process, a single FEM simulation might be several hours or even a few days long. It is therefore more efficient to design and run a limited number of computer simulations, and then use a kriging interpolator to rapidly predict the response in any other design point. Kriging is therefore used very often as a so-called surrogate model, implemented inside optimization routines. Kriging-based surrogate models may also be used in the case of mixed integer inputs.

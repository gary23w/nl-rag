---
title: "Covariance function"
source: https://en.wikipedia.org/wiki/Covariance_function
domain: gaussian-processes-sci
license: CC-BY-SA-4.0
tags: gaussian process regression, covariance function, bayesian optimization, radial basis kernel
fetched: 2026-07-02
---

# Covariance function

In probability theory and statistics, the **covariance function** describes how much two random variables change together (their *covariance*) with varying spatial or temporal separation. For a random field or stochastic process *Z*(*x*) on a domain *D*, a covariance function *C*(*x*, *y*) gives the covariance of the values of the random field at the two locations *x* and *y*:

$C(x,y):=\operatorname {cov} (Z(x),Z(y))=\mathbb {E} {\Big [}{\big (}Z(x)-\mathbb {E} [Z(x)]{\big )}{\big (}Z(y)-\mathbb {E} [Z(y)]{\big )}{\Big ]}.\,$

The same *C*(*x*, *y*) is called the autocovariance function in two instances: in time series (to denote exactly the same concept except that *x* and *y* refer to locations in time rather than in space), and in multivariate random fields (to refer to the covariance of a variable with itself, as opposed to the cross covariance between two different variables at different locations, Cov(*Z*(*x*1), *Y*(*x*2))).

## Admissibility

For locations *x*1, *x*2, ..., *x**N* ∈ *D* the variance of every linear combination

$X=\sum _{i=1}^{N}w_{i}Z(x_{i})$

can be computed as

$\operatorname {var} (X)=\sum _{i=1}^{N}\sum _{j=1}^{N}w_{i}C(x_{i},x_{j})w_{j}.$

A function is a valid covariance function if and only if this variance is non-negative for all possible choices of *N* and weights *w*1, ..., *w**N*. A function with this property is called positive semidefinite.

## Simplifications with stationarity

In case of a weakly stationary random field, where

$C(x_{i},x_{j})=C(x_{i}+h,x_{j}+h)\,$

for any lag *h*, the covariance function can be represented by a one-parameter function

$C_{s}(h)=C(0,h)=C(x,x+h)\,$

which is called a *covariogram* and also a *covariance function*. Implicitly the *C*(*x**i*, *x**j*) can be computed from *C**s*(*h*) by:

$C(x,y)=C_{s}(y-x).\,$

The positive definiteness of this single-argument version of the covariance function can be checked by Bochner's theorem.

## Parametric families of covariance functions

For a given variance $\sigma ^{2}$ , a simple stationary parametric covariance function is the "exponential covariance function"

$C(d)=\sigma ^{2}\exp(-d/V)$

where *V* is a scaling parameter (correlation length), and *d* = *d*(*x*,*y*) is the distance between two points. Sample paths of a Gaussian process with the exponential covariance function are not smooth. The "squared exponential" (or "Gaussian") covariance function:

$C(d)=\sigma ^{2}\exp(-(d/V)^{2})$

is a stationary covariance function with smooth sample paths.

The Matérn covariance function and rational quadratic covariance function are two parametric families of stationary covariance functions. The Matérn family includes the exponential and squared exponential covariance functions as special cases.

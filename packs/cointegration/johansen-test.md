---
title: "Johansen test"
source: https://en.wikipedia.org/wiki/Johansen_test
domain: cointegration
license: CC-BY-SA-4.0
tags: cointegration, error correction model, unit root, spurious relationship
fetched: 2026-07-02
---

# Johansen test

In statistics, the **Johansen test**, named after Søren Johansen, is a procedure for testing cointegration of several, say *k*, I(1) time series. This test permits more than one cointegrating relationship so is more generally applicable than the Engle-Granger test which is based on the Dickey–Fuller (or the augmented) test for unit roots in the residuals from a single (estimated) cointegrating relationship.

## Types

There are two types of Johansen test, either with trace or with eigenvalue, and the inferences might be a little bit different. The null hypothesis for the trace test is that the number of cointegration vectors is *r* = *r** < *k*, vs. the alternative that *r* = *k*. Testing proceeds sequentially for *r** = 1,2, etc. and the first non-rejection of the null is taken as an estimate of *r*. The null hypothesis for the "maximum eigenvalue" test is as for the trace test but the alternative is *r* = *r** + 1 and, again, testing proceeds sequentially for *r** = 1,2,etc., with the first non-rejection used as an estimator for *r*.

Just like a unit root test, there can be a constant term, a trend term, both, or neither in the model. For a general VAR(*p*) model:

$X_{t}=\mu +\Phi D_{t}+\Pi _{p}X_{t-p}+\cdots +\Pi _{1}X_{t-1}+e_{t},\quad t=1,\dots ,T$

There are two possible specifications for error correction: that is, two vector error correction models (VECM):

1. The longrun VECM:

$\Delta X_{t}=\mu +\Phi D_{t}+\Pi X_{t-p}+\Gamma _{p-1}\Delta X_{t-p+1}+\cdots +\Gamma _{1}\Delta X_{t-1}+\varepsilon _{t},\quad t=1,\dots ,T$

where

$\Gamma _{i}=\Pi _{1}+\cdots +\Pi _{i}-I,\quad i=1,\dots ,p-1.\,$

2. The transitory VECM:

$\Delta X_{t}=\mu +\Phi D_{t}+\Pi X_{t-1}-\sum _{j=1}^{p-1}\Gamma _{j}\Delta X_{t-j}+\varepsilon _{t},\quad t=1,\cdots ,T$

where

$\Gamma _{i}=\left(\Pi _{i+1}+\cdots +\Pi _{p}\right),\quad i=1,\dots ,p-1.\,$

The two are the same. In both VECM,

$\Pi =\Pi _{1}+\cdots +\Pi _{p}-I.\,$

Inferences are drawn on Π, and they will be the same, so is the explanatory power.

---
title: "Least trimmed squares"
source: https://en.wikipedia.org/wiki/Least_trimmed_squares
domain: robust-regression
license: CC-BY-SA-4.0
tags: robust regression, M-estimator, robust statistics, influential observation
fetched: 2026-07-02
---

# Least trimmed squares

**Least trimmed squares** (**LTS**), or **least trimmed sum of squares**, is a robust statistical method that fits a function to a set of data whilst not being unduly affected by the presence of outliers . It is one of a number of methods for robust regression.

## Description of method

Instead of the standard least squares method, which minimises the sum of squared residuals over *n* points, the LTS method attempts to minimise the sum of squared residuals over a subset, k , of those points. The unused $n-k$ points do not influence the fit.

In a standard least squares problem, the estimated parameter values β are defined to be those values that minimise the objective function *S*(β) of squared residuals:

$S=\sum _{i=1}^{n}r_{i}(\beta )^{2},$

where the residuals are defined as the differences between the values of the dependent variables (observations) and the model values:

$r_{i}(\beta )=y_{i}-f(x_{i},\beta ),$

and where *n* is the overall number of data points. For a least trimmed squares analysis, this objective function is replaced by one constructed in the following way. For a fixed value of β, let $r_{(j)}(\beta )$ denote the set of ordered absolute values of the residuals (in increasing order of absolute value). In this notation, the standard sum of squares function is

$S(\beta )=\sum _{j=1}^{n}r_{(j)}(\beta )^{2},$

while the objective function for LTS is

$S_{k}(\beta )=\sum _{j=1}^{k}r_{(j)}(\beta )^{2}.$

## Computational considerations

Because this method is binary, in that points are either included or excluded, no closed-form solution exists. As a result, methods for finding the LTS solution sift through combinations of the data, attempting to find the *k* subset that yields the lowest sum of squared residuals. Methods exist for low *n* that will find the exact solution; however, as *n* rises, the number of combinations grows rapidly, thus yielding methods that attempt to find approximate (but generally sufficient) solutions.

---
title: "Polynomial and rational function modeling"
source: https://en.wikipedia.org/wiki/Polynomial_and_rational_function_modeling
domain: polynomial-regression
license: CC-BY-SA-4.0
tags: polynomial regression, orthogonal polynomials, segmented regression, curve fitting
fetched: 2026-07-02
---

# Polynomial and rational function modeling

In statistical modeling (especially process modeling), polynomial functions and rational functions are sometimes used as an empirical technique for curve fitting.

## Polynomial function models

A polynomial function is one that has the form

$y=a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots +a_{2}x^{2}+a_{1}x+a_{0}$

where *n* is a non-negative integer that defines the degree of the polynomial. A polynomial with a degree of 0 is simply a constant function; with a degree of 1 is a line; with a degree of 2 is a quadratic; with a degree of 3 is a cubic, and so on.

Historically, polynomial models are among the most frequently used empirical models for curve fitting.

### Advantages

These models are popular for the following reasons.

1. Polynomial models have a simple form.
2. Polynomial models have well known and understood properties.
3. Polynomial models have moderate flexibility of shapes.
4. Polynomial models are a closed family. Changes of location and scale in the raw data result in a polynomial model being mapped to a polynomial model. That is, polynomial models are not dependent on the underlying metric.
5. Polynomial models are computationally easy to use.

### Disadvantages

However, polynomial models also have the following limitations.

1. Polynomial models have poor interpolatory properties. High-degree polynomials are notorious for oscillations between exact-fit values.
2. Polynomial models have poor extrapolatory properties. Polynomials may provide good fits within the range of data, but they will frequently deteriorate rapidly outside the range of the data.
3. Polynomial models have poor asymptotic properties. By their nature, polynomials have a finite response for finite *x* values and have an infinite response if and only if the *x* value is infinite. Thus polynomials may not model asymptotic phenomena very well.
4. While no procedure is immune to the bias-variance tradeoff, polynomial models exhibit a particularly poor tradeoff between shape and degree. In order to model data with a complicated structure, the degree of the model must be high, indicating that the associated number of parameters to be estimated will also be high. This can result in highly unstable models.

When modeling via polynomial functions is inadequate due to any of the limitations above, the use of rational functions for modeling may give a better fit.

## Rational function models

A rational function is simply the ratio of two polynomial functions.

$y={\frac {a_{n}x^{n}+a_{n-1}x^{n-1}+\ldots +a_{2}x^{2}+a_{1}x+a_{0}}{b_{m}x^{m}+b_{m-1}x^{m-1}+\ldots +b_{2}x^{2}+b_{1}x+b_{0}}}$

with *n* denoting a non-negative integer that defines the degree of the numerator and *m* denoting a non-negative integer that defines the degree of the denominator. For fitting rational function models, the constant term in the denominator is usually set to 1. Rational functions are typically identified by the degrees of the numerator and denominator. For example, a quadratic for the numerator and a cubic for the denominator is identified as a quadratic/cubic rational function. The rational function model is a generalization of the polynomial model: rational function models contain polynomial models as a subset (i.e., the case when the denominator is a constant).

### Advantages

Rational function models have the following advantages:

1. Rational function models have a moderately simple form.
2. Rational function models are a closed family. As with polynomial models, this means that rational function models are not dependent on the underlying metric.
3. Rational function models can take on an extremely wide range of shapes, accommodating a much wider range of shapes than does the polynomial family.
4. Rational function models have better interpolatory properties than polynomial models. Rational functions are typically smoother and less oscillatory than polynomial models.
5. Rational functions have excellent extrapolatory powers. Rational functions can typically be tailored to model the function not only within the domain of the data, but also so as to be in agreement with theoretical/asymptotic behavior outside the domain of interest.
6. Rational function models have excellent asymptotic properties. Rational functions can be either finite or infinite for finite values, or finite or infinite for infinite *x* values. Thus, rational functions can easily be incorporated into a rational function model.
7. Rational function models can often be used to model complicated structure with a fairly low degree in both the numerator and denominator. This in turn means that fewer coefficients will be required compared to the polynomial model.
8. Rational function models are moderately easy to handle computationally. Although they are nonlinear models, rational function models are particularly easy nonlinear models to fit.
9. One common difficulty in fitting nonlinear models is finding adequate starting values. A major advantage of rational function models is the ability to compute starting values using a linear least squares fit. To do this, *p* points are chosen from the data set, with *p* denoting the number of parameters in the rational model. For example, given the linear/quadratic model

$y={\frac {A_{0}+A_{1}x}{1+B_{1}x+B_{2}x^{2}}},$

one would need to select four representative points, and perform a linear fit on the model

$y=A_{0}+A_{1}x-B_{1}xy-B_{2}x^{2}y,$

which is derived from the previous equation by clearing the denominator. Here, the

x

and

y

contain the subset of points, not the full data set. The estimated coefficients from this linear fit are used as the starting values for fitting the nonlinear model to the full data set.

This type of fit, with the response variable appearing on both sides of the function, should only be used to obtain starting values for the nonlinear fit. The statistical properties of fits like this are not well understood.

The subset of points should be selected over the range of the data. It is not critical which points are selected, although obvious outliers should be avoided.

### Disadvantages

Rational function models have the following disadvantages:

1. The properties of the rational function family are not as well known to engineers and scientists as are those of the polynomial family. The literature on the rational function family is also more limited. Because the properties of the family are often not well understood, it can be difficult to answer the following modeling question: *Given that data has a certain shape, what values should be chosen for the degree of the numerator and the degree on the denominator?*
2. Unconstrained rational function fitting can, at times, result in undesired vertical asymptotes due to roots in the denominator polynomial. The range of *x* values affected by the function "blowing up" may be quite narrow, but such asymptotes, when they occur, are a nuisance for local interpolation in the neighborhood of the asymptote point. These asymptotes are easy to detect by a simple plot of the fitted function over the range of the data. These nuisance asymptotes occur occasionally and unpredictably, but practitioners argue that the gain in flexibility of shapes is well worth the chance that they may occur, and that such asymptotes should not discourage choosing rational function models for empirical modeling.

---
title: "Variance (part 2/2)"
source: https://en.wikipedia.org/wiki/Variance
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 2/2
---

## Generalizations

### For complex variables

If x is a scalar complex-valued random variable, with values in ⁠ $\mathbb {C}$ ⁠, then its variance is ⁠ $\operatorname {E} \left[(x-\mu )(x-\mu )^{*}\right]$ ⁠, where $x^{*}$ is the complex conjugate of ⁠ x ⁠. This variance is a real scalar.

### For vector-valued random variables

#### As a matrix

If X is a vector-valued random variable, with values in $\mathbb {R} ^{n},$ and thought of as a column vector, then a natural generalization of variance is $\operatorname {E} \left[(X-\mu ){(X-\mu )}^{\mathsf {T}}\right],$ where $\mu =\operatorname {E} (X)$ and $X^{\mathsf {T}}$ is the transpose of ⁠ X ⁠, and so is a row vector. The result is a positive semi-definite square matrix, commonly referred to as the variance-covariance matrix (or simply as the *covariance matrix*).

If X is a vector- and complex-valued random variable, with values in ⁠ $\mathbb {C} ^{n}$ ⁠, then the covariance matrix is ⁠ $\operatorname {E} \left[(X-\mu ){(X-\mu )}^{\dagger }\right]$ ⁠, where $X^{\dagger }$ is the conjugate transpose of ⁠ X ⁠. This matrix is also positive semi-definite and square.

#### As a scalar

Another generalization of variance for vector-valued random variables $X,$ which results in a scalar value rather than in a matrix, is the generalized variance ⁠ $\det(C)$ ⁠, the determinant of the covariance matrix. The generalized variance can be shown to be related to the multidimensional scatter of points around their mean.

A different generalization is obtained by considering the equation for the scalar variance, $\operatorname {Var} (X)=\operatorname {E} \left[(X-\mu )^{2}\right],$ and reinterpreting $(X-\mu )^{2}$ as the squared Euclidean distance between the random variable and its mean, or, simply as the scalar product of the vector $X-\mu$ with itself. This results in $\operatorname {E} \left[(X-\mu )^{\mathsf {T}}(X-\mu )\right]=\operatorname {tr} (C),$ which is the trace of the covariance matrix.

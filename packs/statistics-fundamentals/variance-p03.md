---
title: "Variance (part 3/3)"
source: https://en.wikipedia.org/wiki/Variance
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 3/3
---

## Moment of inertia

The variance of a probability distribution is analogous to the moment of inertia in classical mechanics of a corresponding mass distribution along a line, with respect to rotation about its center of mass. It is because of this analogy that such things as the variance are called *moments* of probability distributions. The covariance matrix is related to the moment of inertia tensor for multivariate distributions. The moment of inertia of a cloud of *n* points with a covariance matrix of Σ {\displaystyle \Sigma } ({\displaystyle \Sigma }) is given by I = n ( 1 3 × 3 tr ⁡ ( Σ ) − Σ ) . {\displaystyle I=n\left(\mathbf {1} _{3\times 3}\operatorname {tr} (\Sigma )-\Sigma \right).} ({\displaystyle I=n\left(\mathbf {1} _{3\times 3}\operatorname {tr} (\Sigma )-\Sigma \right).})

This difference between moment of inertia in physics and in statistics is clear for points that are gathered along a line. Suppose many points are close to the *x* axis and distributed along it. The covariance matrix might look like Σ = [ 10 0 0 0 0.1 0 0 0 0.1 ] . {\displaystyle \Sigma ={\begin{bmatrix}10&0&0\\0&0.1&0\\0&0&0.1\end{bmatrix}}.} ({\displaystyle \Sigma ={\begin{bmatrix}10&0&0\\0&0.1&0\\0&0&0.1\end{bmatrix}}.})

That is, there is the most variance in the *x* direction. Physicists would consider this to have a low moment *about* the *x* axis so the moment-of-inertia tensor is I = n [ 0.2 0 0 0 10.1 0 0 0 10.1 ] . {\displaystyle I=n{\begin{bmatrix}0.2&0&0\\0&10.1&0\\0&0&10.1\end{bmatrix}}.} ({\displaystyle I=n{\begin{bmatrix}0.2&0&0\\0&10.1&0\\0&0&10.1\end{bmatrix}}.})


## Semivariance

The *semivariance* is calculated in the same manner as the variance but only those observations that fall below the mean are included in the calculation: Semivariance = 1 n ∑ i : x i < μ ( x i − μ ) 2 {\displaystyle {\text{Semivariance}}={\frac {1}{n}}\sum _{i:x_{i}<\mu }{\left(x_{i}-\mu \right)}^{2}} ({\displaystyle {\text{Semivariance}}={\frac {1}{n}}\sum _{i:x_{i}<\mu }{\left(x_{i}-\mu \right)}^{2}}) It is also described as a specific measure in different fields of application. For skewed distributions, the semivariance can provide additional information that a variance does not.

For inequalities associated with the semivariance, see *Chebyshev's inequality § Semivariances*.


## Etymology

The term *variance* was first introduced by Ronald Fisher in his 1918 paper *The Correlation Between Relatives on the Supposition of Mendelian Inheritance*:

> The great body of available statistics show us that the deviations of a human measurement from its mean follow very closely the Normal Law of Errors, and, therefore, that the variability may be uniformly measured by the standard deviation corresponding to the square root of the mean square error. When there are two independent causes of variability capable of producing in an otherwise uniform population distributions with standard deviations σ 1 {\displaystyle \sigma _{1}} ({\displaystyle \sigma _{1}}) and σ 2 {\displaystyle \sigma _{2}} ({\displaystyle \sigma _{2}}), it is found that the distribution, when both causes act together, has a standard deviation σ 1 2 + σ 2 2 {\displaystyle {\sqrt {\sigma _{1}^{2}+\sigma _{2}^{2}}}} ({\displaystyle {\sqrt {\sigma _{1}^{2}+\sigma _{2}^{2}}}}). It is therefore desirable in analysing the causes of variability to deal with the square of the standard deviation as the measure of variability. We shall term this quantity the Variance...


## Generalizations

### For complex variables

If x {\displaystyle x} ({\displaystyle x}) is a scalar complex-valued random variable, with values in ⁠ C {\displaystyle \mathbb {C} } ({\displaystyle \mathbb {C} })⁠, then its variance is ⁠ E ⁡ [ ( x − μ ) ( x − μ ) ∗ ] {\displaystyle \operatorname {E} \left[(x-\mu )(x-\mu )^{*}\right]} ({\displaystyle \operatorname {E} \left[(x-\mu )(x-\mu )^{*}\right]})⁠, where x ∗ {\displaystyle x^{*}} ({\displaystyle x^{*}}) is the complex conjugate of ⁠ x {\displaystyle x} ({\displaystyle x})⁠. This variance is a real scalar.

### For vector-valued random variables

#### As a matrix

If X {\displaystyle X} ({\displaystyle X}) is a vector-valued random variable, with values in R n , {\displaystyle \mathbb {R} ^{n},} ({\displaystyle \mathbb {R} ^{n},}) and thought of as a column vector, then a natural generalization of variance is E ⁡ [ ( X − μ ) ( X − μ ) T ] , {\displaystyle \operatorname {E} \left[(X-\mu ){(X-\mu )}^{\mathsf {T}}\right],} ({\displaystyle \operatorname {E} \left[(X-\mu ){(X-\mu )}^{\mathsf {T}}\right],}) where μ = E ⁡ ( X ) {\displaystyle \mu =\operatorname {E} (X)} ({\displaystyle \mu =\operatorname {E} (X)}) and X T {\displaystyle X^{\mathsf {T}}} ({\displaystyle X^{\mathsf {T}}}) is the transpose of ⁠ X {\displaystyle X} ({\displaystyle X})⁠, and so is a row vector. The result is a positive semi-definite square matrix, commonly referred to as the variance-covariance matrix (or simply as the *covariance matrix*).

If X {\displaystyle X} ({\displaystyle X}) is a vector- and complex-valued random variable, with values in ⁠ C n {\displaystyle \mathbb {C} ^{n}} ({\displaystyle \mathbb {C} ^{n}})⁠, then the covariance matrix is ⁠ E ⁡ [ ( X − μ ) ( X − μ ) † ] {\displaystyle \operatorname {E} \left[(X-\mu ){(X-\mu )}^{\dagger }\right]} ({\displaystyle \operatorname {E} \left[(X-\mu ){(X-\mu )}^{\dagger }\right]})⁠, where X † {\displaystyle X^{\dagger }} ({\displaystyle X^{\dagger }}) is the conjugate transpose of ⁠ X {\displaystyle X} ({\displaystyle X})⁠. This matrix is also positive semi-definite and square.

#### As a scalar

Another generalization of variance for vector-valued random variables X , {\displaystyle X,} ({\displaystyle X,}) which results in a scalar value rather than in a matrix, is the generalized variance ⁠ det ( C ) {\displaystyle \det(C)} ({\displaystyle \det(C)})⁠, the determinant of the covariance matrix. The generalized variance can be shown to be related to the multidimensional scatter of points around their mean.

A different generalization is obtained by considering the equation for the scalar variance, Var ⁡ ( X ) = E ⁡ [ ( X − μ ) 2 ] , {\displaystyle \operatorname {Var} (X)=\operatorname {E} \left[(X-\mu )^{2}\right],} ({\displaystyle \operatorname {Var} (X)=\operatorname {E} \left[(X-\mu )^{2}\right],}) and reinterpreting ( X − μ ) 2 {\displaystyle (X-\mu )^{2}} ({\displaystyle (X-\mu )^{2}}) as the squared Euclidean distance between the random variable and its mean, or, simply as the scalar product of the vector X − μ {\displaystyle X-\mu } ({\displaystyle X-\mu }) with itself. This results in E ⁡ [ ( X − μ ) T ( X − μ ) ] = tr ⁡ ( C ) , {\displaystyle \operatorname {E} \left[(X-\mu )^{\mathsf {T}}(X-\mu )\right]=\operatorname {tr} (C),} ({\displaystyle \operatorname {E} \left[(X-\mu )^{\mathsf {T}}(X-\mu )\right]=\operatorname {tr} (C),}) which is the trace of the covariance matrix.

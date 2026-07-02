---
title: "Multivariate normal distribution"
source: https://en.wikipedia.org/wiki/Multivariate_normal_distribution
domain: multivariate-statistics
license: CC-BY-SA-4.0
tags: multivariate statistics, covariance matrix, Mahalanobis distance, multivariate normal
fetched: 2026-07-02
---

# Multivariate normal distribution

In probability theory and statistics, the **multivariate normal distribution**, **multivariate Gaussian distribution**, or **joint normal distribution** is a generalization of the one-dimensional (univariate) normal distribution to higher dimensions. One definition is that a random vector is said to be *k*-variate normally distributed if every linear combination of its *k* components has a univariate normal distribution. Its importance derives mainly from the multivariate central limit theorem. The multivariate normal distribution is often used to describe, at least approximately, any set of (possibly) correlated real-valued random variables, each of which clusters around a mean value.

## Definitions

### Notation and parametrization

The multivariate normal distribution of a *k*-dimensional random vector $\mathbf {X} =(X_{1},\ldots ,X_{k})^{\mathrm {T} }$ can be written in the following notation:

$\mathbf {X} \ \sim \ {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }}),$

or to make it explicitly known that $\mathbf {X}$ is *k*-dimensional,

$\mathbf {X} \ \sim \ {\mathcal {N}}_{k}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }}),$

with *k*-dimensional mean vector

${\boldsymbol {\mu }}=\operatorname {E} [\mathbf {X} ]=(\operatorname {E} [X_{1}],\operatorname {E} [X_{2}],\ldots ,\operatorname {E} [X_{k}])^{\mathrm {T} },$

and $k\times k$ covariance matrix

$\Sigma _{i,j}=\operatorname {E} [(X_{i}-\mu _{i})(X_{j}-\mu _{j})]=\operatorname {Cov} [X_{i},X_{j}]$

such that $1\leq i\leq k$ and $1\leq j\leq k$ . The inverse of the covariance matrix is called the precision matrix, denoted by ${\boldsymbol {Q}}={\boldsymbol {\Sigma }}^{-1}$ .

### Standard normal random vector

A real random vector $\mathbf {X} =(X_{1},\ldots ,X_{k})^{\mathrm {T} }$ is called a **standard normal random vector** if all of its components $X_{i}$ are independent and each is a zero-mean unit-variance normally distributed random variable, i.e. if $X_{i}\sim \ {\mathcal {N}}(0,1)$ for all $i=1\ldots k$ .

### Centered normal random vector

A real random vector $\mathbf {X} =(X_{1},\ldots ,X_{k})^{\mathrm {T} }$ is called a **centered normal random vector** if there exists a $k\times \ell$ matrix ${\boldsymbol {A}}$ such that ${\boldsymbol {A}}\mathbf {Z}$ has the same distribution as $\mathbf {X}$ where $\mathbf {Z}$ is a standard normal random vector with $\ell$ components.

### Normal random vector

A real random vector $\mathbf {X} =(X_{1},\ldots ,X_{k})^{\mathrm {T} }$ is called a **normal random vector** if there exists a random $\ell$ -vector $\mathbf {Z}$ , which is a standard normal random vector, a k -vector ${\boldsymbol {\mu }}$ , and a $k\times \ell$ matrix ${\boldsymbol {A}}$ , such that $\mathbf {X} ={\boldsymbol {A}}\mathbf {Z} +{\boldsymbol {\mu }}$ .

Formally:

$\mathbf {X} \ \sim \ {\mathcal {N}}_{k}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }})\iff {\text{there exist }}{\boldsymbol {\mu }}\in \mathbb {R} ^{k},{\boldsymbol {A}}\in \mathbb {R} ^{k\times \ell }{\text{ such that }}\mathbf {X} ={\boldsymbol {A}}\mathbf {Z} +{\boldsymbol {\mu }}{\text{ and }}\forall n=1,\ldots ,\ell :Z_{n}\sim \ {\mathcal {N}}(0,1),{\text{i.i.d.}}$

Here the covariance matrix is ${\boldsymbol {\Sigma }}={\boldsymbol {A}}{\boldsymbol {A}}^{\mathrm {T} }$ .

In the degenerate case where the covariance matrix is singular, the corresponding distribution has no density; see the section below for details. This case arises frequently in statistics; for example, in the distribution of the vector of residuals in the ordinary least squares regression. The $X_{i}$ are in general *not* independent; they can be seen as the result of applying the matrix ${\boldsymbol {A}}$ to a collection of independent Gaussian variables $\mathbf {Z}$ .

### Equivalent definitions

The following definitions are equivalent to the definition given above. A random vector $\mathbf {X} =(X_{1},\ldots ,X_{k})^{\mathrm {T} }$ has a multivariate normal distribution if it satisfies one of the following equivalent conditions.

- Every linear combination $Y=a_{1}X_{1}+\cdots +a_{k}X_{k}$ of its components is normally distributed. That is, for any constant vector $\mathbf {a} \in \mathbb {R} ^{k}$ , the random variable $Y=\mathbf {a} ^{\mathrm {T} }\mathbf {X}$ has a univariate normal distribution, where a univariate normal distribution with zero variance is a point mass on its mean.
- There is a *k*-vector $\mathbf {\mu }$ and a symmetric, positive semidefinite $k\times k$ matrix ${\boldsymbol {\Sigma }}$ , such that the characteristic function of $\mathbf {X}$ is $\varphi _{\mathbf {X} }(\mathbf {u} )=\exp {\Big (}i\mathbf {u} ^{\mathrm {T} }{\boldsymbol {\mu }}-{\tfrac {1}{2}}\mathbf {u} ^{\mathrm {T} }{\boldsymbol {\Sigma }}\mathbf {u} {\Big )}.$

The spherical normal distribution can be characterised as the unique distribution where components are independent in any orthogonal coordinate system.

### Density function

#### Non-degenerate case

The multivariate normal distribution is said to be "non-degenerate" when the symmetric covariance matrix ${\boldsymbol {\Sigma }}$ is positive definite. In this case the distribution has density

$f_{\mathbf {X} }(x_{1},\ldots ,x_{k})={\frac {\exp \left(-{\frac {1}{2}}\left({\mathbf {x} }-{\boldsymbol {\mu }}\right)^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}\left({\mathbf {x} }-{\boldsymbol {\mu }}\right)\right)}{\sqrt {(2\pi )^{k}|{\boldsymbol {\Sigma }}|}}}$

where ${\mathbf {x} }$ is a real *k*-dimensional column vector and $|{\boldsymbol {\Sigma }}|\equiv \det {\boldsymbol {\Sigma }}$ is the determinant of ${\boldsymbol {\Sigma }}$ , also known as the generalized variance. The equation above reduces to that of the univariate normal distribution if ${\boldsymbol {\Sigma }}$ is a $1\times 1$ matrix (i.e., a single real number).

The circularly symmetric version of the complex normal distribution has a slightly different form.

Each iso-density locus — the locus of points in *k*-dimensional space each of which gives the same particular value of the density — is an ellipse or its higher-dimensional generalization; hence the multivariate normal is a special case of the elliptical distributions.

The quantity ${\sqrt {({\mathbf {x} }-{\boldsymbol {\mu }})^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})}}$ is known as the Mahalanobis distance, which represents the distance of the test point ${\mathbf {x} }$ from the mean ${\boldsymbol {\mu }}$ . The squared Mahalanobis distance $({\mathbf {x} }-{\boldsymbol {\mu }})^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})$ is decomposed into a sum of *k* terms, each term being a product of three meaningful components. Note that in the case when $k=1$ , the distribution reduces to a univariate normal distribution and the Mahalanobis distance reduces to the absolute value of the standard score. See also Interval below.

#### Bivariate case

In the 2-dimensional nonsingular case ( $k=\operatorname {rank} \left(\Sigma \right)=2$ ), the probability density function of a vector ${\text{[XY]}}\prime$ is: $f(x,y)={\frac {1}{2\pi \sigma _{X}\sigma _{Y}{\sqrt {1-\rho ^{2}}}}}\exp \left(-{\frac {1}{2\left[1-\rho ^{2}\right]}}\left[\left({\frac {x-\mu _{X}}{\sigma _{X}}}\right)^{2}-2\rho \left({\frac {x-\mu _{X}}{\sigma _{X}}}\right)\left({\frac {y-\mu _{Y}}{\sigma _{Y}}}\right)+\left({\frac {y-\mu _{Y}}{\sigma _{Y}}}\right)^{2}\right]\right)$ where $\rho$ is the correlation between X and Y and where $\sigma _{X}>0$ and $\sigma _{Y}>0$ . In this case,

${\boldsymbol {\mu }}={\begin{pmatrix}\mu _{X}\\\mu _{Y}\end{pmatrix}},\quad {\boldsymbol {\Sigma }}={\begin{pmatrix}\sigma _{X}^{2}&\rho \sigma _{X}\sigma _{Y}\\\rho \sigma _{X}\sigma _{Y}&\sigma _{Y}^{2}\end{pmatrix}}.$

In the bivariate case, the first equivalent condition for multivariate reconstruction of normality can be made less restrictive as it is sufficient to verify that a countably infinite set of distinct linear combinations of X and Y are normal in order to conclude that the vector of ${\text{[XY]}}\prime$ is bivariate normal.

The bivariate iso-density loci plotted in the $x,y$ -plane are ellipses, whose principal axes are defined by the eigenvectors of the covariance matrix ${\boldsymbol {\Sigma }}$ (the major and minor semidiameters of the ellipse equal the square-root of the ordered eigenvalues).

As the absolute value of the correlation parameter $\rho$ increases, these loci are squeezed toward the following line :

$y(x)=\operatorname {sgn}(\rho ){\frac {\sigma _{Y}}{\sigma _{X}}}(x-\mu _{X})+\mu _{Y}.$

This is because this expression, with $\operatorname {sgn}(\rho )$ (where sgn is the sign function) replaced by $\rho$ , is the best linear unbiased prediction of Y given a value of X .

#### Degenerate case

If the covariance matrix ${\boldsymbol {\Sigma }}$ is not full rank, then the multivariate normal distribution is degenerate and does not have a density. More precisely, it does not have a density with respect to *k*-dimensional Lebesgue measure (which is the usual measure assumed in calculus-level probability courses). Only random vectors whose distributions are absolutely continuous with respect to a measure are said to have densities (with respect to that measure). To talk about densities but avoid dealing with measure-theoretic complications it can be simpler to restrict attention to a subset of $\operatorname {rank} ({\boldsymbol {\Sigma }})$ of the coordinates of $\mathbf {x}$ such that the covariance matrix for this subset is positive definite; then the other coordinates may be thought of as an affine function of these selected coordinates.

To talk about densities meaningfully in singular cases, then, we must select a different base measure. Using the disintegration theorem we can define a restriction of Lebesgue measure to the $\operatorname {rank} ({\boldsymbol {\Sigma }})$ -dimensional affine subspace of $\mathbb {R} ^{k}$ where the Gaussian distribution is supported, i.e. $\left\{{\boldsymbol {\mu }}+{\boldsymbol {\Sigma ^{1/2}}}\mathbf {v} :\mathbf {v} \in \mathbb {R} ^{k}\right\}$ . With respect to this measure the distribution has the density of the following motif:

$f(\mathbf {x} )={\frac {\exp \left(-{\frac {1}{2}}\left(\mathbf {x} -{\boldsymbol {\mu }}\right)^{\mathrm {T} }{\boldsymbol {\Sigma }}^{+}\left(\mathbf {x} -{\boldsymbol {\mu }}\right)\right)}{\sqrt {\det \nolimits ^{*}(2\pi {\boldsymbol {\Sigma }})}}}$

where ${\boldsymbol {\Sigma }}^{+}$ is the generalized inverse and $\det \nolimits ^{*}$ is the pseudo-determinant.

### Cumulative distribution function

The notion of cumulative distribution function (cdf) in dimension 1 can be extended in two ways to the multidimensional case, based on rectangular and ellipsoidal regions.

The first way is to define the cdf $F(\mathbf {x} )$ of a random vector $\mathbf {X}$ as the probability that all components of $\mathbf {X}$ are less than or equal to the corresponding values in the vector $\mathbf {x}$ :

$F(\mathbf {x} )=\mathbb {P} (\mathbf {X} \leq \mathbf {x} ),\quad {\text{where }}\mathbf {X} \sim {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }}).$

Though there is no closed form for $F(\mathbf {x} )$ , there are a number of algorithms that estimate it numerically.

Another way is to define the cdf $F(r)$ as the probability that a sample lies inside the ellipsoid determined by its Mahalanobis distance r from the Gaussian, a direct generalization of the standard deviation. In order to compute the values of this function, closed analytic formula exist, as follows.

#### Interval

The interval for the multivariate normal distribution yields a region consisting of those vectors **x** satisfying

$({\mathbf {x} }-{\boldsymbol {\mu }})^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})\leq \chi _{k}^{2}(p).$

Here ${\mathbf {x} }$ is a k -dimensional vector, ${\boldsymbol {\mu }}$ is the known k -dimensional mean vector, ${\boldsymbol {\Sigma }}$ is the known covariance matrix and $\chi _{k}^{2}(p)$ is the quantile function for probability p of the chi-squared distribution with k degrees of freedom. When $k=2,$ the expression defines the interior of an ellipse and the chi-squared distribution simplifies to an exponential distribution with mean equal to two (rate equal to half).

### Complementary cumulative distribution function (tail distribution)

The complementary cumulative distribution function (ccdf) or the **tail distribution** is defined as ${\overline {F}}(\mathbf {x} )=1-\mathbb {P} \left(\mathbf {X} \leq \mathbf {x} \right)$ . When $\mathbf {X} \sim {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }})$ , then the ccdf can be written as a probability the maximum of dependent Gaussian variables:

${\overline {F}}(\mathbf {x} )=\mathbb {P} \left(\bigcup _{i}\{X_{i}\geq x_{i}\}\right)=\mathbb {P} \left(\max _{i}Y_{i}\geq 0\right),\quad {\text{where }}\mathbf {Y} \sim {\mathcal {N}}\left({\boldsymbol {\mu }}-\mathbf {x} ,\,{\boldsymbol {\Sigma }}\right).$

While no simple closed formula exists for computing the ccdf, the maximum of dependent Gaussian variables can be estimated accurately via the Monte Carlo method.

## Properties

### Moments

The *k*th-order moments of **x** are given by

$\mu _{1,\ldots ,N}(\mathbf {x} )\mathrel {\stackrel {\mathrm {def} }{=}} \mu _{r_{1},\ldots ,r_{N}}(\mathbf {x} )\mathrel {\stackrel {\mathrm {def} }{=}} \operatorname {E} \left[\prod _{j=1}^{N}X_{j}^{r_{j}}\right]$

where *r*1 + *r*2 + ⋯ + *rN* = *k*.

The *k*th-order central moments are as follows

1. If *k* is odd, *μ*1, ..., *N*(**x** − ***μ***) = 0.
2. If *k* is even with *k* = 2*λ*, then $\mu _{1,\dots ,2\lambda }(\mathbf {x} -{\boldsymbol {\mu }})=\sum \left(\sigma _{ij}\sigma _{k\ell }\cdots \sigma _{XZ}\right)$

where the sum is taken over all allocations of the set $\left\{1,\ldots ,2\lambda \right\}$ into *λ* (unordered) pairs. That is, for a *k*th (= 2*λ* = 6) central moment, one sums the products of *λ* = 3 covariances (the expected value ***μ*** is taken to be 0 in the interests of parsimony):

${\begin{aligned}&\operatorname {E} [X_{1}X_{2}X_{3}X_{4}X_{5}X_{6}]\\[8pt]={}&\operatorname {E} [X_{1}X_{2}]\operatorname {E} [X_{3}X_{4}]\operatorname {E} [X_{5}X_{6}]+\operatorname {E} [X_{1}X_{2}]\operatorname {E} [X_{3}X_{5}]\operatorname {E} [X_{4}X_{6}]+\operatorname {E} [X_{1}X_{2}]\operatorname {E} [X_{3}X_{6}]\operatorname {E} [X_{4}X_{5}]\\[4pt]&{}+\operatorname {E} [X_{1}X_{3}]\operatorname {E} [X_{2}X_{4}]\operatorname {E} [X_{5}X_{6}]+\operatorname {E} [X_{1}X_{3}]\operatorname {E} [X_{2}X_{5}]\operatorname {E} [X_{4}X_{6}]+\operatorname {E} [X_{1}X_{3}]\operatorname {E} [X_{2}X_{6}]\operatorname {E} [X_{4}X_{5}]\\[4pt]&{}+\operatorname {E} [X_{1}X_{4}]\operatorname {E} [X_{2}X_{3}]\operatorname {E} [X_{5}X_{6}]+\operatorname {E} [X_{1}X_{4}]\operatorname {E} [X_{2}X_{5}]\operatorname {E} [X_{3}X_{6}]+\operatorname {E} [X_{1}X_{4}]\operatorname {E} [X_{2}X_{6}]\operatorname {E} [X_{3}X_{5}]\\[4pt]&{}+\operatorname {E} [X_{1}X_{5}]\operatorname {E} [X_{2}X_{3}]\operatorname {E} [X_{4}X_{6}]+\operatorname {E} [X_{1}X_{5}]\operatorname {E} [X_{2}X_{4}]\operatorname {E} [X_{3}X_{6}]+\operatorname {E} [X_{1}X_{5}]\operatorname {E} [X_{2}X_{6}]\operatorname {E} [X_{3}X_{4}]\\[4pt]&{}+\operatorname {E} [X_{1}X_{6}]\operatorname {E} [X_{2}X_{3}]\operatorname {E} [X_{4}X_{5}]+\operatorname {E} [X_{1}X_{6}]\operatorname {E} [X_{2}X_{4}]\operatorname {E} [X_{3}X_{5}]+\operatorname {E} [X_{1}X_{6}]\operatorname {E} [X_{2}X_{5}]\operatorname {E} [X_{3}X_{4}].\end{aligned}}$

This yields ${\tfrac {(2\lambda -1)!}{2^{\lambda -1}(\lambda -1)!}}$ terms in the sum (15 in the above case), each being the product of *λ* (in this case 3) covariances. For fourth order moments (four variables) there are three terms. For sixth-order moments there are 3 × 5 = 15 terms, and for eighth-order moments there are 3 × 5 × 7 = 105 terms.

The covariances are then determined by replacing the terms of the list $[1,\ldots ,2\lambda ]$ by the corresponding terms of the list consisting of *r*1 ones, then *r*2 twos, etc.. To illustrate this, examine the following 4th-order central moment case:

${\begin{aligned}\operatorname {E} \left[X_{i}^{4}\right]&=3\sigma _{ii}^{2}\\[4pt]\operatorname {E} \left[X_{i}^{3}X_{j}\right]&=3\sigma _{ii}\sigma _{ij}\\[4pt]\operatorname {E} \left[X_{i}^{2}X_{j}^{2}\right]&=\sigma _{ii}\sigma _{jj}+2\sigma _{ij}^{2}\\[4pt]\operatorname {E} \left[X_{i}^{2}X_{j}X_{k}\right]&=\sigma _{ii}\sigma _{jk}+2\sigma _{ij}\sigma _{ik}\\[4pt]\operatorname {E} \left[X_{i}X_{j}X_{k}X_{n}\right]&=\sigma _{ij}\sigma _{kn}+\sigma _{ik}\sigma _{jn}+\sigma _{in}\sigma _{jk}.\end{aligned}}$

where $\sigma _{ij}$ is the covariance of *Xi* and *Xj*. With the above method one first finds the general case for a *k*th moment with *k* different *X* variables, $E\left[X_{i}X_{j}X_{k}X_{n}\right]$ , and then one simplifies this accordingly. For example, for $\operatorname {E} [X_{i}^{2}X_{k}X_{n}]$ , one lets *Xi* = *X**j* and one uses the fact that $\sigma _{ii}=\sigma _{i}^{2}$ .

### Functions of a normal vector

A quadratic form of a normal vector ${\boldsymbol {x}}$ , $q({\boldsymbol {x}})={\boldsymbol {x}}'\mathbf {Q_{2}} {\boldsymbol {x}}+{\boldsymbol {q_{1}}}'{\boldsymbol {x}}+q_{0}$ (where $\mathbf {Q_{2}}$ is a matrix, ${\boldsymbol {q_{1}}}$ is a vector, and $q_{0}$ is a scalar), is a generalized chi-squared variable. The direction of a normal vector follows a projected normal distribution.

If $f({\boldsymbol {x}})$ is a general scalar-valued function of a normal vector, its probability density function, cumulative distribution function, and inverse cumulative distribution function can be computed with the numerical method of ray-tracing (Matlab code Archived 2025-02-20 at the Wayback Machine).

#### Likelihood function

If the mean and covariance matrix are known, the log likelihood of an observed vector ${\boldsymbol {x}}$ is simply the log of the probability density function:

$\ln L({\boldsymbol {x}})=-{\frac {1}{2}}\left[\ln(|{\boldsymbol {\Sigma }}|\,)+({\boldsymbol {x}}-{\boldsymbol {\mu }})'{\boldsymbol {\Sigma }}^{-1}({\boldsymbol {x}}-{\boldsymbol {\mu }})+k\ln(2\pi )\right]$

,

The circularly symmetric version of the noncentral complex case, where ${\boldsymbol {z}}$ is a vector of complex numbers, would be

$\ln L({\boldsymbol {z}})=-\ln(|{\boldsymbol {\Sigma }}|\,)-({\boldsymbol {z}}-{\boldsymbol {\mu }})^{\dagger }{\boldsymbol {\Sigma }}^{-1}({\boldsymbol {z}}-{\boldsymbol {\mu }})-k\ln(\pi )$

i.e. with the conjugate transpose (indicated by $\dagger$ ) replacing the normal transpose (indicated by ' ). This is slightly different than in the real case, because the circularly symmetric version of the complex normal distribution has a slightly different form for the normalization constant.

A similar notation is used for multiple linear regression.

Since the log likelihood of a normal vector is a quadratic form of the normal vector, it is distributed as a generalized chi-squared variable.

### Differential entropy

The differential entropy of the multivariate normal distribution is

${\begin{aligned}h\left(f\right)&=-\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }\cdots \int _{-\infty }^{\infty }f(\mathbf {x} )\ln f(\mathbf {x} )\,d\mathbf {x} \\[1ex]&={\frac {1}{2}}\ln \left|2\pi e{\boldsymbol {\Sigma }}\right|={\frac {k}{2}}\left(1+\ln 2\pi \right)+{\frac {1}{2}}\ln \left|{\boldsymbol {\Sigma }}\right|,\end{aligned}}$

where the bars denote the matrix determinant, *k* is the dimensionality of the vector space, and the result has units of nats.

### Kullback–Leibler divergence

The Kullback–Leibler divergence from ${\mathcal {N}}_{1}({\boldsymbol {\mu }}_{1},{\boldsymbol {\Sigma }}_{1})$ to ${\mathcal {N}}_{0}({\boldsymbol {\mu }}_{0},{\boldsymbol {\Sigma }}_{0})$ , for non-singular matrices Σ1 and Σ0, is:

$D_{\text{KL}}({\mathcal {N}}_{0}\parallel {\mathcal {N}}_{1})={1 \over 2}\left\{\operatorname {tr} \left({\boldsymbol {\Sigma }}_{1}^{-1}{\boldsymbol {\Sigma }}_{0}\right)+\left({\boldsymbol {\mu }}_{1}-{\boldsymbol {\mu }}_{0}\right)^{\rm {T}}{\boldsymbol {\Sigma }}_{1}^{-1}({\boldsymbol {\mu }}_{1}-{\boldsymbol {\mu }}_{0})-k+\ln {|{\boldsymbol {\Sigma }}_{1}| \over |{\boldsymbol {\Sigma }}_{0}|}\right\},$

where $|\cdot |$ denotes the matrix determinant, $tr(\cdot )$ is the trace, $\ln(\cdot )$ is the natural logarithm and k is the dimension of the vector space.

The logarithm must be taken to base *e* since the two terms following the logarithm are themselves base-*e* logarithms of expressions that are either factors of the density function or otherwise arise naturally. The equation therefore gives a result measured in nats. Dividing the entire expression above by log*e* 2 yields the divergence in bits.

When ${\boldsymbol {\mu }}_{1}={\boldsymbol {\mu }}_{0}$ ,

$D_{\text{KL}}({\mathcal {N}}_{0}\parallel {\mathcal {N}}_{1})={1 \over 2}\left\{\operatorname {tr} \left({\boldsymbol {\Sigma }}_{1}^{-1}{\boldsymbol {\Sigma }}_{0}\right)-k+\ln {|{\boldsymbol {\Sigma }}_{1}| \over |{\boldsymbol {\Sigma }}_{0}|}\right\}.$

### Mutual information

The mutual information of two multivariate normal distribution is a special case of the Kullback–Leibler divergence in which P is the full k dimensional multivariate distribution and Q is the product of the $k_{1}$ and $k_{2}$ dimensional marginal distributions X and Y , such that $k_{1}+k_{2}=k$ . The mutual information between X and Y is given by:

$I({\boldsymbol {X}},{\boldsymbol {Y}})={\frac {1}{2}}\ln \left({\frac {\det(\Sigma _{X})\det(\Sigma _{Y})}{\det(\Sigma )}}\right),$

where

$\Sigma ={\begin{bmatrix}\Sigma _{X}&\Sigma _{XY}\\\Sigma _{XY}&\Sigma _{Y}\end{bmatrix}}.$

If Q is product of k one-dimensional normal distributions, then in the notation of the Kullback–Leibler divergence section of this article, ${\boldsymbol {\Sigma }}_{1}$ is a diagonal matrix with the diagonal entries of ${\boldsymbol {\Sigma }}_{0}$ , and ${\boldsymbol {\mu }}_{1}={\boldsymbol {\mu }}_{0}$ . The resulting formula for mutual information is:

$I({\boldsymbol {X}})=-{1 \over 2}\ln |{\boldsymbol {\rho }}_{0}|,$

where ${\boldsymbol {\rho }}_{0}$ is the correlation matrix constructed from ${\boldsymbol {\Sigma }}_{0}$ .

In the bivariate case the expression for the mutual information is:

$I(x;y)=-{1 \over 2}\ln(1-\rho ^{2}).$

### Joint normality

#### Normally distributed and independent

If X and Y are normally distributed and independent, this implies they are "jointly normally distributed", i.e., the pair $(X,Y)$ must have multivariate normal distribution. However, a pair of jointly normally distributed variables need not be independent (would only be so if uncorrelated, $\rho =0$ ).

#### Two normally distributed random variables need not be jointly bivariate normal

The fact that two random variables X and Y both have a normal distribution does not imply that the pair $(X,Y)$ has a joint normal distribution. A simple example is one in which X has a normal distribution with expected value 0 and variance 1, and $Y=X$ if $|X|>c$ and $Y=-X$ if $|X|<c$ , where $c>0$ . There are similar counterexamples for more than two random variables. In general, they sum to a mixture model.

#### Correlations and independence

In general, random variables may be uncorrelated but statistically dependent. But if a random vector has a multivariate normal distribution then any two or more of its components that are uncorrelated are independent. This implies that any two or more of its components that are pairwise independent are independent. But, as pointed out just above, it is *not* true that two random variables that are (*separately*, marginally) normally distributed and uncorrelated are independent.

### Conditional distributions

If *N*-dimensional **x** is partitioned as follows

$\mathbf {x} ={\begin{bmatrix}\mathbf {x} _{1}\\\mathbf {x} _{2}\end{bmatrix}}{\text{ with sizes }}{\begin{bmatrix}q\times 1\\(N-q)\times 1\end{bmatrix}}$

and accordingly ***μ*** and **Σ** are partitioned as follows

${\boldsymbol {\mu }}={\begin{bmatrix}{\boldsymbol {\mu }}_{1}\\{\boldsymbol {\mu }}_{2}\end{bmatrix}}{\text{ with sizes }}{\begin{bmatrix}q\times 1\\(N-q)\times 1\end{bmatrix}}$

${\boldsymbol {\Sigma }}={\begin{bmatrix}{\boldsymbol {\Sigma }}_{11}&{\boldsymbol {\Sigma }}_{12}\\{\boldsymbol {\Sigma }}_{21}&{\boldsymbol {\Sigma }}_{22}\end{bmatrix}}{\text{ with sizes }}{\begin{bmatrix}q\times q&q\times (N-q)\\(N-q)\times q&(N-q)\times (N-q)\end{bmatrix}}$

then the distribution of **x**1 conditional on **x**2 = **a** is multivariate normal (**x**1 | **x**2 = **a**) ~ *N*(***μ***, **Σ**) where

${\bar {\boldsymbol {\mu }}}={\boldsymbol {\mu }}_{1}+{\boldsymbol {\Sigma }}_{12}{\boldsymbol {\Sigma }}_{22}^{-1}\left(\mathbf {a} -{\boldsymbol {\mu }}_{2}\right)$

and covariance matrix

${\overline {\boldsymbol {\Sigma }}}={\boldsymbol {\Sigma }}_{11}-{\boldsymbol {\Sigma }}_{12}{\boldsymbol {\Sigma }}_{22}^{-1}{\boldsymbol {\Sigma }}_{21}.$

Here ${\boldsymbol {\Sigma }}_{22}^{-1}$ is the generalized inverse of ${\boldsymbol {\Sigma }}_{22}$ . The matrix ${\overline {\boldsymbol {\Sigma }}}$ is the Schur complement of **Σ**22 in **Σ**. That is, the equation above is equivalent to inverting the overall covariance matrix, dropping the rows and columns corresponding to the variables being conditioned upon, and inverting back to get the conditional covariance matrix.

Note that knowing that **x**2 = **a** alters the variance, though the new variance does not depend on the specific value of **a**; perhaps more surprisingly, the mean is shifted by ${\boldsymbol {\Sigma }}_{12}{\boldsymbol {\Sigma }}_{22}^{-1}\left(\mathbf {a} -{\boldsymbol {\mu }}_{2}\right)$ ; compare this with the situation of not knowing the value of **a**, in which case **x**1 would have distribution ${\mathcal {N}}_{q}\left({\boldsymbol {\mu }}_{1},{\boldsymbol {\Sigma }}_{11}\right)$ .

An interesting fact derived in order to prove this result, is that the random vectors $\mathbf {x} _{2}$ and $\mathbf {y} _{1}=\mathbf {x} _{1}-{\boldsymbol {\Sigma }}_{12}{\boldsymbol {\Sigma }}_{22}^{-1}\mathbf {x} _{2}$ are independent.

The matrix **Σ**12**Σ**22−1 is known as the matrix of regression coefficients.

#### Bivariate case

In the bivariate case where **x** is partitioned into $X_{1}$ and $X_{2}$ , the conditional distribution of $X_{1}$ given $X_{2}$ is

$X_{1}\mid X_{2}=a\ \sim \ {\mathcal {N}}\left(\mu _{1}+{\frac {\sigma _{1}}{\sigma _{2}}}\rho (a-\mu _{2}),\,(1-\rho ^{2})\sigma _{1}^{2}\right)$

where $\rho ={\frac {\sigma _{12}}{\sigma _{1}\sigma _{2}}}$ is the correlation coefficient between $X_{1}$ and $X_{2}$ .

#### Bivariate conditional expectation

##### In the general case

${\begin{pmatrix}X_{1}\\X_{2}\end{pmatrix}}\sim {\mathcal {N}}\left({\begin{pmatrix}\mu _{1}\\\mu _{2}\end{pmatrix}},{\begin{pmatrix}\sigma _{1}^{2}&\rho \sigma _{1}\sigma _{2}\\\rho \sigma _{1}\sigma _{2}&\sigma _{2}^{2}\end{pmatrix}}\right)$

The conditional expectation of X1 given X2 is:

$\operatorname {E} (X_{1}\mid X_{2}=x_{2})=\mu _{1}+\rho {\frac {\sigma _{1}}{\sigma _{2}}}(x_{2}-\mu _{2})$

Proof: the result is obtained by taking the expectation of the conditional distribution $X_{1}\mid X_{2}$ above.

##### In the centered case with unit variances

${\begin{pmatrix}X_{1}\\X_{2}\end{pmatrix}}\sim {\mathcal {N}}\left({\begin{pmatrix}0\\0\end{pmatrix}},{\begin{pmatrix}1&\rho \\\rho &1\end{pmatrix}}\right)$

The conditional expectation of *X*1 given *X*2 is

$\operatorname {E} (X_{1}\mid X_{2}=x_{2})=\rho x_{2}$

and the conditional variance is

$\operatorname {var} (X_{1}\mid X_{2}=x_{2})=1-\rho ^{2};$

thus the conditional variance does not depend on *x*2.

The conditional expectation of *X*1 given that *X*2 is smaller/bigger than *z* is:

$\operatorname {E} (X_{1}\mid X_{2}<z)=-\rho {\varphi (z) \over \Phi (z)},$

$\operatorname {E} (X_{1}\mid X_{2}>z)=\rho {\varphi (z) \over (1-\Phi (z))},$

where the final ratio here is called the inverse Mills ratio.

Proof: the last two results are obtained using the result $\operatorname {E} (X_{1}\mid X_{2}=x_{2})=\rho x_{2}$ , so that

$\operatorname {E} (X_{1}\mid X_{2}<z)=\rho E(X_{2}\mid X_{2}<z)$

and then using the properties of the expectation of a

truncated normal distribution

.

### Marginal distributions

To obtain the marginal distribution over a subset of multivariate normal random variables, one only needs to drop the irrelevant variables (the variables that one wants to marginalize out) from the mean vector and the covariance matrix. The proof for this follows from the definitions of multivariate normal distributions and linear algebra.

*Example*

Let **X** = [*X*1, *X*2, *X*3] be multivariate normal random variables with mean vector **μ** = [*μ*1, *μ*2, *μ*3] and covariance matrix **Σ** (standard parametrization for multivariate normal distributions). Then the joint distribution of **X′** = [*X*1, *X*3] is multivariate normal with mean vector **μ′** = [*μ*1, *μ*3] and covariance matrix ${\boldsymbol {\Sigma }}'={\begin{bmatrix}{\boldsymbol {\Sigma }}_{11}&{\boldsymbol {\Sigma }}_{13}\\{\boldsymbol {\Sigma }}_{31}&{\boldsymbol {\Sigma }}_{33}\end{bmatrix}}$ .

### Affine transformation

If **Y** = **c** + **BX** is an affine transformation of $\mathbf {X} \ \sim {\mathcal {N}}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }}),$ where **c** is an $M\times 1$ vector of constants and **B** is a constant $M\times N$ matrix, then **Y** has a multivariate normal distribution with expected value **c** + **Bμ** and variance **BΣB**T i.e., $\mathbf {Y} \sim {\mathcal {N}}\left(\mathbf {c} +\mathbf {B} {\boldsymbol {\mu }},\mathbf {B} {\boldsymbol {\Sigma }}\mathbf {B} ^{\rm {T}}\right)$ . In particular, any subset of the *Xi* has a marginal distribution that is also multivariate normal. To see this, consider the following example: to extract the subset (*X*1, *X*2, *X*4)T, use

$\mathbf {B} ={\begin{bmatrix}1&0&0&0&0&\ldots &0\\0&1&0&0&0&\ldots &0\\0&0&0&1&0&\ldots &0\end{bmatrix}}$

which extracts the desired elements directly.

Another corollary is that the distribution of **Z** = **b** · **X**, where **b** is a constant vector with the same number of elements as **X** and the dot indicates the dot product, is univariate Gaussian with $Z\sim {\mathcal {N}}\left(\mathbf {b} \cdot {\boldsymbol {\mu }},\mathbf {b} ^{\rm {T}}{\boldsymbol {\Sigma }}\mathbf {b} \right)$ . This result follows by using

$\mathbf {B} ={\begin{bmatrix}b_{1}&b_{2}&\ldots &b_{n}\end{bmatrix}}=\mathbf {b} ^{\rm {T}}.$

Observe how the positive-definiteness of **Σ** implies that the variance of the dot product must be positive.

An affine transformation of **X** such as 2**X** is not the same as the sum of two independent realisations of **X**.

### Geometric interpretation

The equidensity contours of a non-singular multivariate normal distribution are ellipsoids (i.e. affine transformations of hyperspheres) centered at the mean. Hence the multivariate normal distribution is an example of the class of elliptical distributions. The directions of the principal axes of the ellipsoids are given by the eigenvectors of the covariance matrix ${\boldsymbol {\Sigma }}$ . The squared relative lengths of the principal axes are given by the corresponding eigenvalues.

If **Σ** = **UΛU**T = **UΛ**1/2(**UΛ**1/2)T is an eigendecomposition where the columns of **U** are unit eigenvectors and **Λ** is a diagonal matrix of the eigenvalues, then we have

$\mathbf {X} \ \sim {\mathcal {N}}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }})\iff \mathbf {X} \ \sim {\boldsymbol {\mu }}+\mathbf {U} {\boldsymbol {\Lambda }}^{1/2}{\mathcal {N}}(0,\mathbf {I} )\iff \mathbf {X} \ \sim {\boldsymbol {\mu }}+\mathbf {U} {\mathcal {N}}(0,{\boldsymbol {\Lambda }}).$

Moreover, **U** can be chosen to be a rotation matrix, as inverting an axis does not have any effect on *N*(0, **Λ**), but inverting a column changes the sign of **U'**s determinant. The distribution *N*(**μ**, **Σ**) is in effect *N*(0, **I**) scaled by **Λ**1/2, rotated by **U** and translated by **μ**.

Conversely, any choice of **μ**, full rank matrix **U**, and positive diagonal entries Λ*i* yields a non-singular multivariate normal distribution. If any Λ*i* is zero and **U** is square, the resulting covariance matrix **UΛU**T is singular. Geometrically this means that every contour ellipsoid is infinitely thin and has zero volume in *n*-dimensional space, as at least one of the principal axes has length of zero; this is the degenerate case.

"The radius around the true mean in a bivariate normal random variable, re-written in polar coordinates (radius and angle), follows a Hoyt distribution."

In one dimension the probability of finding a sample of the normal distribution in the interval $\mu \pm \sigma$ is approximately 68.27%, but in higher dimensions the probability of finding a sample in the region of the standard deviation ellipse is lower.

| Dimensionality | Probability |
|---|---|
| 1 | 0.6827 |
| 2 | 0.3935 |
| 3 | 0.1987 |
| 4 | 0.0902 |
| 5 | 0.0374 |
| 6 | 0.0144 |
| 7 | 0.0052 |
| 8 | 0.0018 |
| 9 | 0.0006 |
| 10 | 0.0002 |

## Statistical inference

### Parameter estimation

The derivation of the maximum-likelihood estimator of the covariance matrix of a multivariate normal distribution is straightforward.

In short, the probability density function (pdf) of a multivariate normal is

$f(\mathbf {x} )={\frac {1}{\sqrt {(2\pi )^{k}|{\boldsymbol {\Sigma }}|}}}\exp \left(-{1 \over 2}(\mathbf {x} -{\boldsymbol {\mu }})^{\rm {T}}{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})\right)$

and the ML estimator of the covariance matrix from a sample of *n* observations is

${\widehat {\boldsymbol {\Sigma }}}={1 \over n}\sum _{i=1}^{n}({\mathbf {x} }_{i}-{\overline {\mathbf {x} }})({\mathbf {x} }_{i}-{\overline {\mathbf {x} }})^{\mathrm {T} }$

which is simply the sample covariance matrix. This is a biased estimator whose expectation is

$E\left[{\widehat {\boldsymbol {\Sigma }}}\right]={\frac {n-1}{n}}{\boldsymbol {\Sigma }}.$

An unbiased sample covariance is

${\widehat {\boldsymbol {\Sigma }}}={\frac {1}{n-1}}\sum _{i=1}^{n}(\mathbf {x} _{i}-{\overline {\mathbf {x} }})(\mathbf {x} _{i}-{\overline {\mathbf {x} }})^{\rm {T}}={\frac {1}{n-1}}\left[X'\left(I-{\frac {1}{n}}\cdot J\right)X\right]$

(matrix form;

I

is the

$K\times K$

identity matrix, J is a

$K\times K$

matrix of ones; the term in parentheses is thus the

$K\times K$

centering matrix)

The Fisher information matrix for estimating the parameters of a multivariate normal distribution has a closed form expression. This can be used, for example, to compute the Cramér–Rao bound for parameter estimation in this setting. See Fisher information for more details.

### Bayesian inference

In Bayesian statistics, the conjugate prior of the mean vector is another multivariate normal distribution, and the conjugate prior of the covariance matrix is an inverse-Wishart distribution ${\mathcal {W}}^{-1}$ . Suppose then that *n* observations have been made

$\mathbf {X} =\{\mathbf {x} _{1},\dots ,\mathbf {x} _{n}\}\sim {\mathcal {N}}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }})$

and that a conjugate prior has been assigned, where

$p({\boldsymbol {\mu }},{\boldsymbol {\Sigma }})=p({\boldsymbol {\mu }}\mid {\boldsymbol {\Sigma }})\ p({\boldsymbol {\Sigma }}),$

where

$p({\boldsymbol {\mu }}\mid {\boldsymbol {\Sigma }})\sim {\mathcal {N}}({\boldsymbol {\mu }}_{0},m^{-1}{\boldsymbol {\Sigma }}),$

and

$p({\boldsymbol {\Sigma }})\sim {\mathcal {W}}^{-1}({\boldsymbol {\Psi }},n_{0}).$

Then

${\begin{array}{rcl}p({\boldsymbol {\mu }}\mid {\boldsymbol {\Sigma }},\mathbf {X} )&\sim &{\mathcal {N}}\left({\frac {n{\bar {\mathbf {x} }}+m{\boldsymbol {\mu }}_{0}}{n+m}},{\frac {1}{n+m}}{\boldsymbol {\Sigma }}\right),\\p({\boldsymbol {\Sigma }}\mid \mathbf {X} )&\sim &{\mathcal {W}}^{-1}\left({\boldsymbol {\Psi }}+n\mathbf {S} +{\frac {nm}{n+m}}({\bar {\mathbf {x} }}-{\boldsymbol {\mu }}_{0})({\bar {\mathbf {x} }}-{\boldsymbol {\mu }}_{0})',n+n_{0}\right),\end{array}}$

where

${\begin{aligned}{\bar {\mathbf {x} }}&={\frac {1}{n}}\sum _{i=1}^{n}\mathbf {x} _{i},\\\mathbf {S} &={\frac {1}{n}}\sum _{i=1}^{n}(\mathbf {x} _{i}-{\bar {\mathbf {x} }})(\mathbf {x} _{i}-{\bar {\mathbf {x} }})'.\end{aligned}}$

### Multivariate normality tests

Multivariate normality tests check a given set of data for similarity to the multivariate normal distribution. The null hypothesis is that the data set is similar to the normal distribution, therefore a sufficiently small *p*-value indicates non-normal data. Multivariate normality tests include the Cox–Small test and Smith and Jain's adaptation of the Friedman–Rafsky test created by Larry Rafsky and Jerome Friedman.

#### Mardia's test

**Mardia's test** is based on multivariate extensions of skewness and kurtosis measures. For a sample {**x**1, ..., **x***n*} of *k*-dimensional vectors we compute

${\begin{aligned}&{\widehat {\boldsymbol {\Sigma }}}={1 \over n}\sum _{j=1}^{n}\left(\mathbf {x} _{j}-{\bar {\mathbf {x} }}\right)\left(\mathbf {x} _{j}-{\bar {\mathbf {x} }}\right)^{\mathrm {T} }\\&A={1 \over 6n}\sum _{i=1}^{n}\sum _{j=1}^{n}\left[(\mathbf {x} _{i}-{\bar {\mathbf {x} }})^{\mathrm {T} }\;{\widehat {\boldsymbol {\Sigma }}}^{-1}(\mathbf {x} _{j}-{\bar {\mathbf {x} }})\right]^{3}\\&B={\sqrt {\frac {n}{8k(k+2)}}}\left\{{1 \over n}\sum _{i=1}^{n}\left[(\mathbf {x} _{i}-{\bar {\mathbf {x} }})^{\mathrm {T} }\;{\widehat {\boldsymbol {\Sigma }}}^{-1}(\mathbf {x} _{i}-{\bar {\mathbf {x} }})\right]^{2}-k(k+2)\right\}\end{aligned}}$

Under the null hypothesis of multivariate normality, the statistic *A* will have approximately a chi-squared distribution with ⁠1/6⁠⋅*k*(*k* + 1)(*k* + 2) degrees of freedom, and *B* will be approximately standard normal *N*(0,1).

Mardia's kurtosis statistic is skewed and converges very slowly to the limiting normal distribution. For medium size samples $(50\leq n<400)$ , the parameters of the asymptotic distribution of the kurtosis statistic are modified For small sample tests ( $n<50$ ) empirical critical values are used. Tables of critical values for both statistics are given by Rencher for *k* = 2, 3, 4.

Mardia's tests are affine invariant but not consistent. For example, the multivariate skewness test is not consistent against symmetric non-normal alternatives.

#### BHEP test

The **BHEP test** computes the norm of the difference between the empirical characteristic function and the theoretical characteristic function of the normal distribution. Calculation of the norm is performed in the L2(*μ*) space of square-integrable functions with respect to the Gaussian weighting function $\mu _{\beta }(\mathbf {t} )=(2\pi \beta ^{2})^{-k/2}e^{-|\mathbf {t} |^{2}/(2\beta ^{2})}$ . The test statistic is

${\begin{aligned}T_{\beta }&=\int _{\mathbb {R} ^{k}}\left|{1 \over n}\sum _{j=1}^{n}e^{i\mathbf {t} ^{\mathrm {T} }{\widehat {\boldsymbol {\Sigma }}}^{-1/2}(\mathbf {x} _{j}-{\bar {\mathbf {x} )}}}-e^{-|\mathbf {t} |^{2}/2}\right|^{2}\;{\boldsymbol {\mu }}_{\beta }(\mathbf {t} )\,d\mathbf {t} \\&={1 \over n^{2}}\sum _{i,j=1}^{n}e^{-{\beta ^{2} \over 2}(\mathbf {x} _{i}-\mathbf {x} _{j})^{\mathrm {T} }{\widehat {\boldsymbol {\Sigma }}}^{-1}(\mathbf {x} _{i}-\mathbf {x} _{j})}-{\frac {2}{n(1+\beta ^{2})^{k/2}}}\sum _{i=1}^{n}e^{-{\frac {\beta ^{2}}{2(1+\beta ^{2})}}(\mathbf {x} _{i}-{\bar {\mathbf {x} }})^{\mathrm {T} }{\widehat {\boldsymbol {\Sigma }}}^{-1}(\mathbf {x} _{i}-{\bar {\mathbf {x} }})}+{\frac {1}{(1+2\beta ^{2})^{k/2}}}\end{aligned}}$

The limiting distribution of this test statistic is a weighted sum of chi-squared random variables.

A detailed survey of these and other test procedures is available.

## Computational methods

### Drawing values from the distribution

A widely used method for drawing (sampling) a random vector **x** from the *N*-dimensional multivariate normal distribution with mean vector **μ** and covariance matrix **Σ** works as follows:

1. Find any real matrix **A** such that **AA**T = **Σ**. When **Σ** is positive-definite, the Cholesky decomposition is typically used because it is widely available, computationally efficient, and well known. If a rank-revealing (pivoted) Cholesky decomposition such as LAPACK's dpstrf() is available, it can be used in the general positive-semidefinite case as well. A slower general alternative is to use the matrix **A** = **UΛ**1/2 obtained from a spectral decomposition **Σ** = **UΛU**−1 of **Σ**.
2. Let **z** = (*z*1, ..., *zN*)T be a vector whose components are *N* independent standard normal variates (which can be generated, for example, by using the Box–Muller transform).
3. Let **x** be **μ** + **Az**. This has the desired distribution due to the affine transformation property.

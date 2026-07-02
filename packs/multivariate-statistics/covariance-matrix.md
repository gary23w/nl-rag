---
title: "Covariance matrix"
source: https://en.wikipedia.org/wiki/Covariance_matrix
domain: multivariate-statistics
license: CC-BY-SA-4.0
tags: multivariate statistics, covariance matrix, Mahalanobis distance, multivariate normal
fetched: 2026-07-02
---

# Covariance matrix

In probability theory and statistics, a **covariance matrix** (also known as **auto-covariance matrix**, **dispersion matrix**, **variance matrix**, or **variance–covariance matrix**) is a square matrix giving the covariance between each pair of elements of a given random vector.

Intuitively, the covariance matrix generalizes the notion of variance to multiple dimensions. As an example, the variation in a collection of random points in two-dimensional space cannot be characterized fully by a single number, nor would the variances in the x and y directions contain all of the necessary information; a $2\times 2$ matrix would be necessary to fully characterize the two-dimensional variation.

Any covariance matrix is symmetric and positive semi-definite and its main diagonal contains variances (i.e., the covariance of each element with itself).

The covariance matrix of a random vector $\mathbf {X}$ is typically denoted by $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ , $\Sigma$ or S .

## Definition

Throughout this article, boldfaced unsubscripted $\mathbf {X}$ and $\mathbf {Y}$ are used to refer to random vectors, and Roman subscripted $X_{i}$ and $Y_{i}$ are used to refer to scalar random variables.

If the entries in the column vector $\mathbf {X} =(X_{1},X_{2},\dots ,X_{n})^{\mathsf {T}}$ are random variables, each with finite variance and expected value, then the covariance matrix $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ is the matrix whose $(i,j)$ entry is the covariance $\operatorname {K} _{X_{i}X_{j}}=\operatorname {cov} [X_{i},X_{j}]=\operatorname {E} [(X_{i}-\operatorname {E} [X_{i}])(X_{j}-\operatorname {E} [X_{j}])]$ where the operator $\operatorname {E}$ denotes the expected value (mean) of its argument.

### Conflicting nomenclatures and notations

Nomenclatures differ. Some statisticians, following the probabilist William Feller in his two-volume book *An Introduction to Probability Theory and Its Applications*, call the matrix $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ the **variance** of the random vector $\mathbf {X}$ , because it is the natural generalization to higher dimensions of the 1-dimensional variance. Others call it the **covariance matrix**, because it is the matrix of covariances between the scalar components of the vector $\mathbf {X}$ . $\operatorname {var} (\mathbf {X} )=\operatorname {cov} (\mathbf {X} ,\mathbf {X} )=\operatorname {E} \left[(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {X} -\operatorname {E} [\mathbf {X} ])^{\mathsf {T}}\right].$

Both forms are quite standard, and there is no ambiguity between them. The matrix $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ is also often called the **variance-covariance matrix**, since the diagonal terms are in fact variances.

By comparison, the notation for the cross-covariance matrix *between* two vectors is $\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )=\operatorname {K} _{\mathbf {X} \mathbf {Y} }=\operatorname {E} \left[(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {Y} -\operatorname {E} [\mathbf {Y} ])^{\mathsf {T}}\right].$

## Properties

### Relation to the autocorrelation matrix

The auto-covariance matrix $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ is related to the autocorrelation matrix $\operatorname {R} _{\mathbf {X} \mathbf {X} }$ by $\operatorname {K} _{\mathbf {X} \mathbf {X} }=\operatorname {E} [(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {X} -\operatorname {E} [\mathbf {X} ])^{\mathsf {T}}]=\operatorname {R} _{\mathbf {X} \mathbf {X} }-\operatorname {E} [\mathbf {X} ]\operatorname {E} [\mathbf {X} ]^{\mathsf {T}}$ where the autocorrelation matrix is defined as $\operatorname {R} _{\mathbf {X} \mathbf {X} }=\operatorname {E} [\mathbf {X} \mathbf {X} ^{\mathsf {T}}]$ .

### Relation to the correlation matrix

An entity closely related to the covariance matrix is the matrix of Pearson product-moment correlation coefficients between each of the random variables in the random vector $\mathbf {X}$ , which can be written as $\operatorname {corr} (\mathbf {X} )={\big (}\operatorname {diag} (\operatorname {K} _{\mathbf {X} \mathbf {X} }){\big )}^{-{\frac {1}{2}}}\,\operatorname {K} _{\mathbf {X} \mathbf {X} }\,{\big (}\operatorname {diag} (\operatorname {K} _{\mathbf {X} \mathbf {X} }){\big )}^{-{\frac {1}{2}}},$ where $\operatorname {diag} (\operatorname {K} _{\mathbf {X} \mathbf {X} })$ is the matrix of the diagonal elements of $\operatorname {K} _{\mathbf {X} \mathbf {X} }$ (i.e., a diagonal matrix of the variances of $X_{i}$ for $i=1,\dots ,n$ ).

Equivalently, the correlation matrix can be seen as the covariance matrix of the standardized random variables $X_{i}/\sigma (X_{i})$ for $i=1,\dots ,n$ . $\operatorname {corr} (\mathbf {X} )={\begin{bmatrix}1&{\frac {\operatorname {E} [(X_{1}-\mu _{1})(X_{2}-\mu _{2})]}{\sigma (X_{1})\sigma (X_{2})}}&\cdots &{\frac {\operatorname {E} [(X_{1}-\mu _{1})(X_{n}-\mu _{n})]}{\sigma (X_{1})\sigma (X_{n})}}\\\\{\frac {\operatorname {E} [(X_{2}-\mu _{2})(X_{1}-\mu _{1})]}{\sigma (X_{2})\sigma (X_{1})}}&1&\cdots &{\frac {\operatorname {E} [(X_{2}-\mu _{2})(X_{n}-\mu _{n})]}{\sigma (X_{2})\sigma (X_{n})}}\\\\\vdots &\vdots &\ddots &\vdots \\\\{\frac {\operatorname {E} [(X_{n}-\mu _{n})(X_{1}-\mu _{1})]}{\sigma (X_{n})\sigma (X_{1})}}&{\frac {\operatorname {E} [(X_{n}-\mu _{n})(X_{2}-\mu _{2})]}{\sigma (X_{n})\sigma (X_{2})}}&\cdots &1\end{bmatrix}}.$

Each element on the principal diagonal of a correlation matrix is the correlation of a random variable with itself, which always equals 1. Each off-diagonal element is between −1 and +1 inclusive.

### Inverse of the covariance matrix

The inverse of this matrix, $\operatorname {K} _{\mathbf {X} \mathbf {X} }^{-1}$ , if it exists, is the inverse covariance matrix, also known as the *precision matrix* (or *concentration matrix*).

Just as the covariance matrix can be written as the rescaling of a correlation matrix by the marginal variances: $\operatorname {cov} (\mathbf {X} )={\begin{bmatrix}\sigma _{x_{1}}&&&0\\&\sigma _{x_{2}}&&\\&&\ddots &\\0&&&\sigma _{x_{n}}\end{bmatrix}}$

$\times {\begin{bmatrix}1&\rho _{x_{1},x_{2}}&\cdots &\rho _{x_{1},x_{n}}\\\rho _{x_{2},x_{1}}&1&\cdots &\rho _{x_{2},x_{n}}\\\vdots &\vdots &\ddots &\vdots \\\rho _{x_{n},x_{1}}&\rho _{x_{n},x_{2}}&\cdots &1\end{bmatrix}}$

$\times {\begin{bmatrix}\sigma _{x_{1}}&&&0\\&\sigma _{x_{2}}&&\\&&\ddots &\\0&&&\sigma _{x_{n}}\end{bmatrix}}$

So, using the idea of partial correlation, and partial variance, the inverse covariance matrix can be expressed analogously: $\operatorname {cov} (\mathbf {X} )^{-1}={\begin{bmatrix}{\frac {1}{\sigma _{x_{1}\mid x_{2}\dots }}}&&&0\\&{\frac {1}{\sigma _{x_{2}\mid x_{1},x_{3}\dots }}}\\&&\ddots \\0&&&{\frac {1}{\sigma _{x_{n}\mid x_{1}\dots x_{n-1}}}}\end{bmatrix}}$

$\times {\begin{bmatrix}1&-\rho _{x_{1},x_{2}\mid x_{3}\dots }&\cdots &-\rho _{x_{1},x_{n}\mid x_{2}\dots x_{n-1}}\\-\rho _{x_{2},x_{1}\mid x_{3}\dots }&1&\cdots &-\rho _{x_{2},x_{n}\mid x_{1},x_{3}\dots x_{n-1}}\\\vdots &\vdots &\ddots &\vdots \\-\rho _{x_{n},x_{1}\mid x_{2}\dots x_{n-1}}&-\rho _{x_{n},x_{2}\mid x_{1},x_{3}\dots x_{n-1}}&\cdots &1\end{bmatrix}}$

$\times {\begin{bmatrix}{\frac {1}{\sigma _{x_{1}\mid x_{2}\dots }}}&&&0\\&{\frac {1}{\sigma _{x_{2}\mid x_{1},x_{3}\dots }}}\\&&\ddots \\0&&&{\frac {1}{\sigma _{x_{n}\mid x_{1}\dots x_{n-1}}}}\end{bmatrix}}$

This duality motivates a number of other dualities between marginalizing and conditioning for Gaussian random variables.

### Basic properties

For $\operatorname {K} _{\mathbf {X} \mathbf {X} }=\operatorname {var} (\mathbf {X} )=\operatorname {E} \left[\left(\mathbf {X} -\operatorname {E} [\mathbf {X} ]\right)\left(\mathbf {X} -\operatorname {E} [\mathbf {X} ]\right)^{\mathsf {T}}\right]$ and ${\boldsymbol {\mu }}_{\mathbf {X} }=\operatorname {E} [{\textbf {X}}]$ , where $\mathbf {X} =(X_{1},\ldots ,X_{n})^{\mathsf {T}}$ is an n -dimensional random variable, the following basic properties apply:

1. $\operatorname {K} _{\mathbf {X} \mathbf {X} }=\operatorname {E} (\mathbf {XX^{\mathsf {T}}} )-{\boldsymbol {\mu }}_{\mathbf {X} }{\boldsymbol {\mu }}_{\mathbf {X} }^{\mathsf {T}}$
2. $\operatorname {K} _{\mathbf {X} \mathbf {X} }\,$ is positive-semidefinite, i.e. $\mathbf {a} ^{T}\operatorname {K} _{\mathbf {X} \mathbf {X} }\mathbf {a} \geq 0\quad {\text{for all }}\mathbf {a} \in \mathbb {R} ^{n}$

Proof

Indeed, from the property 4 it follows that under linear transformation of random variable $\mathbf {X}$ with covariation matrix $\mathbf {\Sigma _{X}} =\mathrm {cov} (\mathbf {X} )$ by linear operator $\mathbf {A}$ s.a. $\mathbf {Y} =\mathbf {A} \mathbf {X}$ , the covariation matrix is transformed as

$\mathbf {\Sigma _{Y}} =\mathrm {cov} \left(\mathbf {Y} \right)=\mathbf {A\,\Sigma _{X}\,A} ^{\top }$

.

As according to the property 3 matrix $\mathbf {\Sigma _{X}}$ is symmetric, it can be diagonalized by a linear orthogonal transformation, i.e. there exists such orthogonal matrix $\mathbf {A}$ (meanwhile $\mathbf {A} ^{\top }=\mathbf {A} ^{-1}$ ), that

$\mathbf {A\,\Sigma _{X}\,A} ^{\top }=\mathbf {A\,\Sigma _{X}\,A} ^{-1}={\mbox{diag}}(\sigma _{1},\ldots ,\sigma _{n}),$

and

$\sigma _{1},\ldots ,\sigma _{n}$

are eigenvalues of

$\mathbf {\Sigma _{X}}$

. But this means that this matrix is a covariation matrix for a random variable

$\mathbf {Y} =\mathbf {A} \mathbf {X}$

, and the main diagonal of

$\mathbf {\Sigma _{Y}} =\mathrm {cov} \left(\mathbf {Y} \right)$

consists of variances of elements of

$\mathbf {Y}$

vector. As variance is always non-negative, we conclude that

$\sigma _{i}\geq 0$

for any

i

. But this means that matrix

$\mathbf {\Sigma _{X}}$

is positive-semidefinite.

2. $\operatorname {K} _{\mathbf {X} \mathbf {X} }\,$ is symmetric, i.e. $\operatorname {K} _{\mathbf {X} \mathbf {X} }^{\mathsf {T}}=\operatorname {K} _{\mathbf {X} \mathbf {X} }$
3. For any constant (i.e. non-random) $m\times n$ matrix $\mathbf {A}$ and constant $m\times 1$ vector $\mathbf {a}$ , one has $\operatorname {var} (\mathbf {AX} +\mathbf {a} )=\mathbf {A} \,\operatorname {var} (\mathbf {X} )\,\mathbf {A} ^{\mathsf {T}}$
4. If $\mathbf {Y}$ is another random vector with the same dimension as $\mathbf {X}$ , then $\operatorname {var} (\mathbf {X} +\mathbf {Y} )=\operatorname {var} (\mathbf {X} )+\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )+\operatorname {cov} (\mathbf {Y} ,\mathbf {X} )+\operatorname {var} (\mathbf {Y} )$ where $\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )$ is the cross-covariance matrix of $\mathbf {X}$ and $\mathbf {Y}$ .

### Block matrices

The joint mean ${\boldsymbol {\mu }}$ and joint covariance matrix ${\boldsymbol {\Sigma }}$ of $\mathbf {X}$ and $\mathbf {Y}$ can be written in block form ${\boldsymbol {\mu }}={\begin{bmatrix}{\boldsymbol {\mu }}_{X}\\{\boldsymbol {\mu }}_{Y}\end{bmatrix}},\qquad {\boldsymbol {\Sigma }}={\begin{bmatrix}\operatorname {K} _{\mathbf {XX} }&\operatorname {K} _{\mathbf {XY} }\\\operatorname {K} _{\mathbf {YX} }&\operatorname {K} _{\mathbf {YY} }\end{bmatrix}}$ where $\operatorname {K} _{\mathbf {XX} }=\operatorname {var} (\mathbf {X} )$ , $\operatorname {K} _{\mathbf {YY} }=\operatorname {var} (\mathbf {Y} )$ and $\operatorname {K} _{\mathbf {XY} }=\operatorname {K} _{\mathbf {YX} }^{\mathsf {T}}=\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )$ .

$\operatorname {K} _{\mathbf {XX} }$ and $\operatorname {K} _{\mathbf {YY} }$ can be identified as the variance matrices of the marginal distributions for $\mathbf {X}$ and $\mathbf {Y}$ respectively.

If $\mathbf {X}$ and $\mathbf {Y}$ are jointly normally distributed, $\mathbf {X} ,\mathbf {Y} \sim \ {\mathcal {N}}({\boldsymbol {\mu }},\operatorname {\boldsymbol {\Sigma }} ),$ then the conditional distribution for $\mathbf {Y}$ given $\mathbf {X}$ is given by $\mathbf {Y} \mid \mathbf {X} \sim \ {\mathcal {N}}({\boldsymbol {\mu }}_{\mathbf {Y|X} },\operatorname {K} _{\mathbf {Y|X} }),$ defined by conditional mean ${\boldsymbol {\mu }}_{\mathbf {Y} |\mathbf {X} }={\boldsymbol {\mu }}_{\mathbf {Y} }+\operatorname {K} _{\mathbf {YX} }\operatorname {K} _{\mathbf {XX} }^{-1}\left(\mathbf {X} -{\boldsymbol {\mu }}_{\mathbf {X} }\right)$ and conditional variance $\operatorname {K} _{\mathbf {Y|X} }=\operatorname {K} _{\mathbf {YY} }-\operatorname {K} _{\mathbf {YX} }\operatorname {K} _{\mathbf {XX} }^{-1}\operatorname {K} _{\mathbf {XY} }.$

The matrix $\operatorname {K} _{\mathbf {YX} }\operatorname {K} _{\mathbf {XX} }^{-1}$ is known as the matrix of regression coefficients, while in linear algebra $\operatorname {K} _{\mathbf {Y|X} }$ is the Schur complement of $\operatorname {K} _{\mathbf {XX} }$ in ${\boldsymbol {\Sigma }}$ .

The matrix of regression coefficients may often be given in transpose form, $\operatorname {K} _{\mathbf {XX} }^{-1}\operatorname {K} _{\mathbf {XY} }$ , suitable for post-multiplying a row vector of explanatory variables $\mathbf {X} ^{\mathsf {T}}$ rather than pre-multiplying a column vector $\mathbf {X}$ . In this form they correspond to the coefficients obtained by inverting the matrix of the normal equations of ordinary least squares (OLS).

## Partial covariance matrix

A covariance matrix with all non-zero elements tells us that all the individual random variables are interrelated. This means that the variables are not only directly correlated, but also correlated via other variables indirectly. Often such indirect, common-mode correlations are trivial and uninteresting. They can be suppressed by calculating the partial covariance matrix, that is the part of covariance matrix that shows only the interesting part of correlations.

If two vectors of random variables $\mathbf {X}$ and $\mathbf {Y}$ are correlated via another vector $\mathbf {I}$ , the latter correlations are suppressed in a matrix $\operatorname {K} _{\mathbf {XY\mid I} }=\operatorname {pcov} (\mathbf {X} ,\mathbf {Y} \mid \mathbf {I} )=\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )-\operatorname {cov} (\mathbf {X} ,\mathbf {I} )\operatorname {cov} (\mathbf {I} ,\mathbf {I} )^{-1}\operatorname {cov} (\mathbf {I} ,\mathbf {Y} ).$ The partial covariance matrix $\operatorname {K} _{\mathbf {XY\mid I} }$ is effectively the simple covariance matrix $\operatorname {K} _{\mathbf {XY} }$ as if the uninteresting random variables $\mathbf {I}$ were held constant.

## Standard deviation matrix

The standard deviation matrix $\mathbf {S}$ is the extension of the standard deviation to multiple dimensions. It is the symmetric square root of the covariance matrix $\mathbf {\Sigma }$ .

## Covariance matrix as a parameter of a distribution

If a column vector $\mathbf {X}$ of n possibly correlated random variables is jointly normally distributed, or more generally elliptically distributed, then its probability density function $\operatorname {f} (\mathbf {X} )$ can be expressed in terms of the covariance matrix ${\boldsymbol {\Sigma }}$ as follows $\operatorname {f} (\mathbf {X} )=(2\pi )^{-n/2}|{\boldsymbol {\Sigma }}|^{-1/2}\exp \left(-{\tfrac {1}{2}}\mathbf {(X-\mu )^{\mathsf {T}}\Sigma ^{-1}(X-\mu )} \right),$ where ${\boldsymbol {\mu }}=\operatorname {E} [\mathbf {X} ]$ and $|{\boldsymbol {\Sigma }}|$ is the determinant of ${\boldsymbol {\Sigma }}$ , the so-called *generalized variance*.

## Covariance matrix as a linear operator

Applied to one vector, the covariance matrix maps a linear combination **c** of the random variables **X** onto a vector of covariances with those variables: $\mathbf {c} ^{\mathsf {T}}\Sigma =\operatorname {cov} (\mathbf {c} ^{\mathsf {T}}\mathbf {X} ,\mathbf {X} )$ . Treated as a bilinear form, it yields the covariance between the two linear combinations: $\mathbf {d} ^{\mathsf {T}}{\boldsymbol {\Sigma }}\mathbf {c} =\operatorname {cov} (\mathbf {d} ^{\mathsf {T}}\mathbf {X} ,\mathbf {c} ^{\mathsf {T}}\mathbf {X} )$ . The variance of a linear combination is then $\mathbf {c} ^{\mathsf {T}}{\boldsymbol {\Sigma }}\mathbf {c}$ , its covariance with itself.

Similarly, the (pseudo-)inverse covariance matrix provides an inner product $\langle c-\mu |\Sigma ^{+}|c-\mu \rangle$ , which induces the Mahalanobis distance, a measure of the "unlikelihood" of *c*.

## Admissibility

From basic property 4. above, let $\mathbf {b}$ be a $(p\times 1)$ real-valued vector, then $\operatorname {var} (\mathbf {b} ^{\mathsf {T}}\mathbf {X} )=\mathbf {b} ^{\mathsf {T}}\operatorname {var} (\mathbf {X} )\mathbf {b} ,\,$ which must always be nonnegative, since it is the variance of a real-valued random variable, so a covariance matrix is always a positive-semidefinite matrix.

The above argument can be expanded as follows: ${\begin{aligned}&w^{\mathsf {T}}\operatorname {E} \left[(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {X} -\operatorname {E} [\mathbf {X} ])^{\mathsf {T}}\right]w=\operatorname {E} \left[w^{\mathsf {T}}(\mathbf {X} -\operatorname {E} [\mathbf {X} ])(\mathbf {X} -\operatorname {E} [\mathbf {X} ])^{\mathsf {T}}w\right]\\&=\operatorname {E} {\big [}{\big (}w^{\mathsf {T}}(\mathbf {X} -\operatorname {E} [\mathbf {X} ]){\big )}^{2}{\big ]}\geq 0,\end{aligned}}$ where the last inequality follows from the observation that $w^{\mathsf {T}}(\mathbf {X} -\operatorname {E} [\mathbf {X} ])$ is a scalar.

Conversely, every symmetric positive semi-definite matrix is a covariance matrix. To see this, suppose M is a $p\times p$ symmetric positive-semidefinite matrix. From the finite-dimensional case of the spectral theorem, it follows that M has a nonnegative symmetric square root, which can be denoted by **M**1/2. Let $\mathbf {X}$ be any $p\times 1$ column vector-valued random variable whose covariance matrix is the $p\times p$ identity matrix. Then $\operatorname {var} (\mathbf {M} ^{1/2}\mathbf {X} )=\mathbf {M} ^{1/2}\,\operatorname {var} (\mathbf {X} )\,\mathbf {M} ^{1/2}=\mathbf {M} .$

## Complex random vectors

The variance of a complex *scalar-valued* random variable with expected value $\mu$ is conventionally defined using complex conjugation: $\operatorname {var} (Z)=\operatorname {E} \left[(Z-\mu _{Z}){\overline {(Z-\mu _{Z})}}\right],$ where the complex conjugate of a complex number z is denoted ${\overline {z}}$ ; thus the variance of a complex random variable is a real number.

If $\mathbf {Z} =(Z_{1},\ldots ,Z_{n})^{\mathsf {T}}$ is a column vector of complex-valued random variables, then the conjugate transpose $\mathbf {Z} ^{\mathsf {H}}$ is formed by *both* transposing and conjugating. In the following expression, the product of a vector with its conjugate transpose results in a square matrix called the **covariance matrix**, as its expectation: $\operatorname {K} _{\mathbf {Z} \mathbf {Z} }=\operatorname {cov} [\mathbf {Z} ,\mathbf {Z} ]=\operatorname {E} \left[(\mathbf {Z} -{\boldsymbol {\mu }}_{\mathbf {Z} })(\mathbf {Z} -{\boldsymbol {\mu }}_{\mathbf {Z} })^{\mathsf {H}}\right],$ The matrix so obtained will be Hermitian positive-semidefinite, with real numbers in the main diagonal and complex numbers off-diagonal.

**Properties**

- The covariance matrix is a Hermitian matrix, i.e. $\operatorname {K} _{\mathbf {Z} \mathbf {Z} }^{\mathsf {H}}=\operatorname {K} _{\mathbf {Z} \mathbf {Z} }$ .
- The diagonal elements of the covariance matrix are real.

### Pseudo-covariance matrix

For complex random vectors, another kind of second central moment, the **pseudo-covariance matrix** (also called **relation matrix**) is defined as follows: $\operatorname {J} _{\mathbf {Z} \mathbf {Z} }=\operatorname {cov} [\mathbf {Z} ,{\overline {\mathbf {Z} }}]=\operatorname {E} \left[(\mathbf {Z} -{\boldsymbol {\mu }}_{\mathbf {Z} })(\mathbf {Z} -{\boldsymbol {\mu }}_{\mathbf {Z} })^{\mathsf {T}}\right]$

In contrast to the covariance matrix defined above, Hermitian transposition gets replaced by transposition in the definition. Its diagonal elements may be complex valued; it is a complex symmetric matrix.

## Estimation

If $\mathbf {M} _{\mathbf {X} }$ and $\mathbf {M} _{\mathbf {Y} }$ are centered data matrices of dimension $p\times n$ and $q\times n$ respectively, i.e. with *n* columns of observations of *p* and *q* rows of variables, from which the row means have been subtracted, then, if the row means were estimated from the data, sample covariance matrices $\mathbf {Q} _{\mathbf {XX} }$ and $\mathbf {Q} _{\mathbf {XY} }$ can be defined to be $\mathbf {Q} _{\mathbf {XX} }={\frac {1}{n-1}}\mathbf {M} _{\mathbf {X} }\mathbf {M} _{\mathbf {X} }^{\mathsf {T}},\qquad \mathbf {Q} _{\mathbf {XY} }={\frac {1}{n-1}}\mathbf {M} _{\mathbf {X} }\mathbf {M} _{\mathbf {Y} }^{\mathsf {T}}$ or, if the row means were known a priori, $\mathbf {Q} _{\mathbf {XX} }={\frac {1}{n}}\mathbf {M} _{\mathbf {X} }\mathbf {M} _{\mathbf {X} }^{\mathsf {T}},\qquad \mathbf {Q} _{\mathbf {XY} }={\frac {1}{n}}\mathbf {M} _{\mathbf {X} }\mathbf {M} _{\mathbf {Y} }^{\mathsf {T}}.$

These empirical sample covariance matrices are the most straightforward and most often used estimators for the covariance matrices, but other estimators also exist, including regularised or shrinkage estimators, which may have better properties.

## Applications

The covariance matrix is a useful tool in many different areas. From it a transformation matrix can be derived, called a whitening transformation, that allows one to completely decorrelate the data or, from a different point of view, to find an optimal basis for representing the data in a compact way (see Rayleigh quotient for a formal proof and additional properties of covariance matrices). This is called principal component analysis (PCA) and the Karhunen–Loève transform (KL-transform).

The covariance matrix plays a key role in financial economics, especially in portfolio theory and its mutual fund separation theorem and in the capital asset pricing model. The matrix of covariances among various assets' returns is used to determine, under certain assumptions, the relative amounts of different assets that investors should (in a normative analysis) or are predicted to (in a positive analysis) choose to hold in a context of diversification.

### Use in optimization

The evolution strategy, a particular family of Randomized Search Heuristics, fundamentally relies on a covariance matrix in its mechanism. The characteristic mutation operator draws the update step from a multivariate normal distribution using an evolving covariance matrix. There is a formal proof that the evolution strategy's covariance matrix adapts to the inverse of the Hessian matrix of the search landscape, up to a scalar factor and small random fluctuations (proven for a single-parent strategy and a static model, as the population size increases, relying on the quadratic approximation). Intuitively, this result is supported by the rationale that the optimal covariance distribution can offer mutation steps whose equidensity probability contours match the level sets of the landscape, and so they maximize the progress rate.

### Covariance mapping

In **covariance mapping** the values of the $\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )$ or $\operatorname {pcov} (\mathbf {X} ,\mathbf {Y} \mid \mathbf {I} )$ matrix are plotted as a 2-dimensional map. When vectors $\mathbf {X}$ and $\mathbf {Y}$ are discrete random functions, the map shows statistical relations between different regions of the random functions. Statistically independent regions of the functions show up on the map as zero-level flatland, while positive or negative correlations show up, respectively, as hills or valleys.

In practice the column vectors $\mathbf {X} ,\mathbf {Y}$ , and $\mathbf {I}$ are acquired experimentally as rows of n samples, e.g. $\left[\mathbf {X} _{1},\mathbf {X} _{2},\dots ,\mathbf {X} _{n}\right]={\begin{bmatrix}X_{1}(t_{1})&X_{2}(t_{1})&\cdots &X_{n}(t_{1})\\\\X_{1}(t_{2})&X_{2}(t_{2})&\cdots &X_{n}(t_{2})\\\\\vdots &\vdots &\ddots &\vdots \\\\X_{1}(t_{m})&X_{2}(t_{m})&\cdots &X_{n}(t_{m})\end{bmatrix}},$ where $X_{j}(t_{i})$ is the *i*-th discrete value in sample *j* of the random function $X(t)$ . The expected values needed in the covariance formula are estimated using the sample mean, e.g. $\langle \mathbf {X} \rangle ={\frac {1}{n}}\sum _{j=1}^{n}\mathbf {X} _{j}$ and the covariance matrix is estimated by the sample covariance matrix $\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )\approx \langle \mathbf {XY^{\mathsf {T}}} \rangle -\langle \mathbf {X} \rangle \langle \mathbf {Y} ^{\mathsf {T}}\rangle ,$ where the angular brackets denote sample averaging as before except that the Bessel's correction should be made to avoid bias. Using this estimation the partial covariance matrix can be calculated as $\operatorname {pcov} (\mathbf {X} ,\mathbf {Y} \mid \mathbf {I} )=\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )-\operatorname {cov} (\mathbf {X} ,\mathbf {I} )\left(\operatorname {cov} (\mathbf {I} ,\mathbf {I} )\backslash \operatorname {cov} (\mathbf {I} ,\mathbf {Y} )\right),$ where the backslash denotes the left matrix division operator, which bypasses the requirement to invert a matrix and is available in some computational packages such as Matlab.

Fig. 1 illustrates how a partial covariance map is constructed on an example of an experiment performed at the FLASH free-electron laser in Hamburg. The random function $X(t)$ is the time-of-flight spectrum of ions from a Coulomb explosion of nitrogen molecules multiply ionised by a laser pulse. Since only a few hundreds of molecules are ionised at each laser pulse, the single-shot spectra are highly fluctuating. However, collecting typically $m=10^{4}$ such spectra, $\mathbf {X} _{j}(t)$ , and averaging them over j produces a smooth spectrum $\langle \mathbf {X} (t)\rangle$ , which is shown in red at the bottom of Fig. 1. The average spectrum $\langle \mathbf {X} \rangle$ reveals several nitrogen ions in a form of peaks broadened by their kinetic energy, but to find the correlations between the ionisation stages and the ion momenta requires calculating a covariance map.

In the example of Fig. 1 spectra $\mathbf {X} _{j}(t)$ and $\mathbf {Y} _{j}(t)$ are the same, except that the range of the time-of-flight t differs. Panel **a** shows $\langle \mathbf {XY^{\mathsf {T}}} \rangle$ , panel **b** shows $\langle \mathbf {X} \rangle \langle \mathbf {Y} ^{\mathsf {T}}\rangle$ and panel **c** shows their difference, which is $\operatorname {cov} (\mathbf {X} ,\mathbf {Y} )$ (note a change in the colour scale). Unfortunately, this map is overwhelmed by uninteresting, common-mode correlations induced by laser intensity fluctuating from shot to shot. To suppress such correlations the laser intensity $I_{j}$ is recorded at every shot, put into $\mathbf {I}$ and $\operatorname {pcov} (\mathbf {X} ,\mathbf {Y} \mid \mathbf {I} )$ is calculated as panels **d** and **e** show. The suppression of the uninteresting correlations is, however, imperfect because there are other sources of common-mode fluctuations than the laser intensity and in principle all these sources should be monitored in vector $\mathbf {I}$ . Yet in practice it is often sufficient to overcompensate the partial covariance correction as panel **f** shows, where interesting correlations of ion momenta are now clearly visible as straight lines centred on ionisation stages of atomic nitrogen.

### Two-dimensional infrared spectroscopy

Two-dimensional infrared spectroscopy employs correlation analysis to obtain 2D spectra of the condensed phase. There are two versions of this analysis: synchronous and asynchronous. Mathematically, the former is expressed in terms of the sample covariance matrix and the technique is equivalent to covariance mapping.

---
title: "Canonical correlation"
source: https://en.wikipedia.org/wiki/Canonical_correlation
domain: canonical-correlation
license: CC-BY-SA-4.0
tags: canonical correlation, cross-covariance, angles between flats, multivariate statistics
fetched: 2026-07-02
---

# Canonical correlation

In statistics, **canonical-correlation analysis** (**CCA**), also called **canonical variates analysis**, is a way of inferring information from cross-covariance matrices. If we have two vectors *X* = (*X*1, ..., *X**n*) and *Y* = (*Y*1, ..., *Y**m*) of random variables, and there are correlations among the variables, then canonical-correlation analysis will find linear combinations of *X* and *Y* that have a maximum correlation with each other. T. R. Knapp notes that "virtually all of the commonly encountered parametric tests of significance can be treated as special cases of canonical-correlation analysis, which is the general procedure for investigating the relationships between two sets of variables." The method was first introduced by Harold Hotelling in 1936, although in the context of angles between flats the mathematical concept was published by Camille Jordan in 1875.

CCA is now a cornerstone of multivariate statistics and multi-view learning, and a great number of interpretations and extensions have been proposed, such as probabilistic CCA, sparse CCA, multi-view CCA, deep CCA, and DeepGeoCCA. Unfortunately, perhaps because of its popularity, the literature can be inconsistent with notation. We attempt to highlight such inconsistencies in this article to help the reader make best use of the existing literature and techniques available.

Like its sister method PCA, CCA can be viewed in *population* form (corresponding to random vectors and their covariance matrices) or in *sample* form (corresponding to datasets and their sample covariance matrices). These two forms are almost exact analogues of each other, which is why their distinction is often overlooked, but they can behave very differently in high dimensional settings. We next give explicit mathematical definitions for the population problem and highlight the different objects in the so-called *canonical decomposition* - understanding the differences between these objects is crucial for interpretation of the technique.

## Population CCA definition via correlations

Given two column vectors $X=(x_{1},\dots ,x_{n})^{T}$ and $Y=(y_{1},\dots ,y_{m})^{T}$ of random variables with finite second moments, one may define the cross-covariance $\Sigma _{XY}=\operatorname {cov} (X,Y)$ to be the $n\times m$ matrix whose $(i,j)$ entry is the covariance $\operatorname {cov} (x_{i},y_{j})$ . In practice, we would estimate the covariance matrix based on sampled data from X and Y (i.e. from a pair of data matrices).

Canonical-correlation analysis seeks a sequence of vectors $a_{k}$ ( $a_{k}\in \mathbb {R} ^{n}$ ) and $b_{k}$ ( $b_{k}\in \mathbb {R} ^{m}$ ) such that the random variables $a_{k}^{T}X$ and $b_{k}^{T}Y$ maximize the correlation $\rho =\operatorname {corr} (a_{k}^{T}X,b_{k}^{T}Y)$ . The (scalar) random variables $U=a_{1}^{T}X$ and $V=b_{1}^{T}Y$ are the ***first pair of canonical variables***. Then one seeks vectors maximizing the same correlation subject to the constraint that they are to be uncorrelated with the first pair of canonical variables; this gives the ***second pair of canonical variables***. This procedure may be continued up to $\min\{m,n\}$ times.

$(a_{k},b_{k})={\underset {a,b}{\operatorname {argmax} }}\operatorname {corr} (a^{T}X,b^{T}Y)\quad {\text{ subject to }}\operatorname {cov} (a^{T}X,a_{j}^{T}X)=\operatorname {cov} (b^{T}Y,b_{j}^{T}Y)=0{\text{ for }}j=1,\dots ,k-1$

The sets of vectors $a_{k},b_{k}$ are called ***canonical directions*** or ***weight vectors*** or simply ***weights***. The 'dual' sets of vectors $\Sigma _{XX}a_{k},\Sigma _{YY}b_{k}$ are called ***canonical loading vectors*** or simply ***loadings***; these are often more straightforward to interpret than the weights.

## Computation

### Derivation

Let $\Sigma _{XY}$ be the cross-covariance matrix for any pair of (vector-shaped) random variables X and Y . The target function to maximize is

$\rho ={\frac {a^{T}\Sigma _{XY}b}{{\sqrt {a^{T}\Sigma _{XX}a}}{\sqrt {b^{T}\Sigma _{YY}b}}}}.$

The first step is to define a change of basis and define

$c=\Sigma _{XX}^{1/2}a,$

$d=\Sigma _{YY}^{1/2}b,$

where $\Sigma _{XX}^{1/2}$ and $\Sigma _{YY}^{1/2}$ can be obtained from the eigen-decomposition (or by diagonalization):

$\Sigma _{XX}^{1/2}=V_{X}D_{X}^{1/2}V_{X}^{\top },\qquad V_{X}D_{X}V_{X}^{\top }=\Sigma _{XX},$

and

$\Sigma _{YY}^{1/2}=V_{Y}D_{Y}^{1/2}V_{Y}^{\top },\qquad V_{Y}D_{Y}V_{Y}^{\top }=\Sigma _{YY}.$

Thus

$\rho ={\frac {c^{T}\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1/2}d}{{\sqrt {c^{T}c}}{\sqrt {d^{T}d}}}}.$

By the Cauchy–Schwarz inequality,

$\left(c^{T}\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1/2}\right)(d)\leq \left(c^{T}\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1/2}\Sigma _{YY}^{-1/2}\Sigma _{YX}\Sigma _{XX}^{-1/2}c\right)^{1/2}\left(d^{T}d\right)^{1/2},$

$\rho \leq {\frac {\left(c^{T}\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1}\Sigma _{YX}\Sigma _{XX}^{-1/2}c\right)^{1/2}}{\left(c^{T}c\right)^{1/2}}}.$

There is equality if the vectors d and $\Sigma _{YY}^{-1/2}\Sigma _{YX}\Sigma _{XX}^{-1/2}c$ are collinear. In addition, the maximum of correlation is attained if c is the eigenvector with the maximum eigenvalue for the matrix $\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1}\Sigma _{YX}\Sigma _{XX}^{-1/2}$ (see Rayleigh quotient). The subsequent pairs are found by using eigenvalues of decreasing magnitudes. Orthogonality is guaranteed by the symmetry of the correlation matrices.

Another way of viewing this computation is that c and d are the left and right singular vectors of the correlation matrix of X and Y corresponding to the highest singular value.

### Solution

The solution is therefore:

- c is an eigenvector of $\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1}\Sigma _{YX}\Sigma _{XX}^{-1/2}$
- d is proportional to $\Sigma _{YY}^{-1/2}\Sigma _{YX}\Sigma _{XX}^{-1/2}c$

Reciprocally, there is also:

- d is an eigenvector of $\Sigma _{YY}^{-1/2}\Sigma _{YX}\Sigma _{XX}^{-1}\Sigma _{XY}\Sigma _{YY}^{-1/2}$
- c is proportional to $\Sigma _{XX}^{-1/2}\Sigma _{XY}\Sigma _{YY}^{-1/2}d$

Reversing the change of coordinates, we have that

- a is an eigenvector of $\Sigma _{XX}^{-1}\Sigma _{XY}\Sigma _{YY}^{-1}\Sigma _{YX}$ ,
- b is proportional to $\Sigma _{YY}^{-1}\Sigma _{YX}a;$
- b is an eigenvector of $\Sigma _{YY}^{-1}\Sigma _{YX}\Sigma _{XX}^{-1}\Sigma _{XY},$
- a is proportional to $\Sigma _{XX}^{-1}\Sigma _{XY}b$ .

The canonical variables are defined by:

$U=c^{T}\Sigma _{XX}^{-1/2}X=a^{T}X$

$V=d^{T}\Sigma _{YY}^{-1/2}Y=b^{T}Y$

### Implementation

CCA can be computed using singular value decomposition on a correlation matrix. It is available as a function in

- MATLAB as canoncorr (also in Octave)
- R as the standard function cancor and several other packages, including candisc, CCA and vegan. CCP for statistical hypothesis testing in canonical correlation analysis.
- SAS as proc cancorr
- Python in the library scikit-learn, as cross decomposition and in statsmodels, as CanCorr. The CCA-Zoo library implements CCA extensions, such as probabilistic CCA, sparse CCA, multi-view CCA, and deep CCA.
- SPSS as macro CanCorr shipped with the main software
- Julia (programming language) in the MultivariateStats.jl package.

CCA computation using singular value decomposition on a correlation matrix is related to the cosine of the angles between flats. The cosine function is ill-conditioned for small angles, leading to very inaccurate computation of highly correlated principal vectors in finite precision computer arithmetic. To fix this trouble, alternative algorithms are available in

- SciPy as linear-algebra function subspace_angles
- MATLAB as FileExchange function subspacea

## Hypothesis testing

Each row can be tested for significance with the following method. Since the correlations are sorted, saying that row i is zero implies all further correlations are also zero. If we have p independent observations in a sample and ${\widehat {\rho }}_{i}$ is the estimated correlation for $i=1,\dots ,\min\{m,n\}$ . For the i th row, the test statistic is:

$\chi ^{2}=-\left(p-1-{\frac {1}{2}}(m+n+1)\right)\ln \prod _{j=i}^{\min\{m,n\}}(1-{\widehat {\rho }}_{j}^{2}),$

which is asymptotically distributed as a chi-squared with $(m-i+1)(n-i+1)$ degrees of freedom for large p . Since all the correlations from $\min\{m,n\}$ to p are logically zero (and estimated that way also) the product for the terms after this point is irrelevant.

Note that in the small sample size limit with $p<n+m$ then we are guaranteed that the top $m+n-p$ correlations will be identically 1 and hence the test is meaningless.

## Practical uses

A typical use for canonical correlation in the experimental context is to take two sets of variables and see what is common among the two sets. For example, in psychological testing, one could take two well established multidimensional personality tests such as the Minnesota Multiphasic Personality Inventory (MMPI-2) and the NEO. By seeing how the MMPI-2 factors relate to the NEO factors, one could gain insight into what dimensions were common between the tests and how much variance was shared. For example, one might find that an extraversion or neuroticism dimension accounted for a substantial amount of shared variance between the two tests.

One can also use canonical-correlation analysis to produce a model equation which relates two sets of variables, for example a set of performance measures and a set of explanatory variables, or a set of outputs and set of inputs. Constraint restrictions can be imposed on such a model to ensure it reflects theoretical requirements or intuitively obvious conditions. This type of model is known as a maximum correlation model.

Visualization of the results of canonical correlation is usually through bar plots of the coefficients of the two sets of variables for the pairs of canonical variates showing significant correlation. Some authors suggest that they are best visualized by plotting them as heliographs, a circular format with ray like bars, with each half representing the two sets of variables.

## Examples

Let $X=x_{1}$ with zero expected value, i.e., $\operatorname {E} (X)=0$ .

1. If $Y=X$ , i.e., X and Y are perfectly correlated, then, e.g., $a=1$ and $b=1$ , so that the first (and only in this example) pair of canonical variables is $U=X$ and $V=Y=X$ .
2. If $Y=-X$ , i.e., X and Y are perfectly anticorrelated, then, e.g., $a=1$ and $b=-1$ , so that the first (and only in this example) pair of canonical variables is $U=X$ and $V=-Y=X$ .

We notice that in both cases $U=V$ , which illustrates that the canonical-correlation analysis treats correlated and anticorrelated variables similarly.

## Connection to principal angles

Assuming that $X=(x_{1},\dots ,x_{n})^{T}$ and $Y=(y_{1},\dots ,y_{m})^{T}$ have zero expected values, i.e., $\operatorname {E} (X)=\operatorname {E} (Y)=0$ , their covariance matrices $\Sigma _{XX}=\operatorname {Cov} (X,X)=\operatorname {E} [XX^{T}]$ and $\Sigma _{YY}=\operatorname {Cov} (Y,Y)=\operatorname {E} [YY^{T}]$ can be viewed as Gram matrices in an inner product for the entries of X and Y , correspondingly. In this interpretation, the random variables, entries $x_{i}$ of X and $y_{j}$ of Y are treated as elements of a vector space with an inner product given by the covariance $\operatorname {cov} (x_{i},y_{j})$ ; see Covariance#Relationship to inner products.

The definition of the canonical variables U and V is then equivalent to the definition of principal vectors for the pair of subspaces spanned by the entries of X and Y with respect to this inner product. The canonical correlations $\operatorname {corr} (U,V)$ is equal to the cosine of principal angles.

## Whitening and probabilistic canonical correlation analysis

CCA can also be viewed as a special whitening transformation where the random vectors X and Y are simultaneously transformed in such a way that the cross-correlation between the whitened vectors $X^{CCA}$ and $Y^{CCA}$ is diagonal. The canonical correlations are then interpreted as regression coefficients linking $X^{CCA}$ and $Y^{CCA}$ and may also be negative. The regression view of CCA also provides a way to construct a latent variable probabilistic generative model for CCA, with uncorrelated hidden variables representing shared and non-shared variability.

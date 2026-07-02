---
title: "Multilinear subspace learning"
source: https://en.wikipedia.org/wiki/Multilinear_subspace_learning
domain: tensor-decomposition
license: CC-BY-SA-4.0
tags: tensor decomposition, tucker decomposition, canonical polyadic decomposition, tensor rank
fetched: 2026-07-02
---

# Multilinear subspace learning

**Multilinear subspace learning** is an approach for disentangling the causal factor of data formation and performing dimensionality reduction. The **Dimensionality reduction** can be performed on a data tensor that contains a collection of observations that have been vectorized, or observations that are treated as matrices and concatenated into a data tensor. Here are some examples of data tensors whose observations are vectorized or whose observations are matrices concatenated into data tensor images (2D/3D), video sequences (3D/4D), and hyperspectral cubes (3D/4D).

The mapping from a high-dimensional vector space to a set of lower dimensional vector spaces is a multilinear projection. When observations are retained in the same organizational structure as matrices or higher order tensors, their representations are computed by performing linear projections into the column space, row space and fiber space.

Multilinear subspace learning algorithms are higher-order generalizations of linear subspace learning methods such as principal component analysis (PCA), independent component analysis (ICA), linear discriminant analysis (LDA) and canonical correlation analysis (CCA).

## Background

Multilinear methods may be causal in nature and perform causal inference, or they may be simple regression methods from which no causal conclusion are drawn.

Linear subspace learning algorithms are traditional dimensionality reduction techniques that are well suited for datasets that are the result of varying a single causal factor. Unfortunately, they often become inadequate when dealing with datasets that are the result of multiple causal factors. .

Multilinear subspace learning can be applied to observations whose measurements were vectorized and organized into a data tensor for causally aware dimensionality reduction. These methods may also be employed in reducing horizontal and vertical redundancies irrespective of the causal factors when the observations are treated as a "matrix" (ie. a collection of independent column/row observations) and concatenated into a tensor.

## Algorithms

### Multilinear principal component analysis

Historically, multilinear principal component analysis has been referred to as "M-mode PCA", a terminology which was coined by Peter Kroonenberg. In 2005, Vasilescu and Terzopoulos introduced the Multilinear PCA terminology as a way to better differentiate between multilinear tensor decompositions that computed 2nd order statistics associated with each data tensor mode, and subsequent work on Multilinear Independent Component Analysis that computed higher order statistics for each tensor mode. MPCA is an extension of PCA.

### Multilinear independent component analysis

Multilinear independent component analysis is an extension of ICA.

### Multilinear linear discriminant analysis

- Multilinear extension of LDA
  - TTP-based: Discriminant Analysis with Tensor Representation (DATER)
  - TTP-based: General tensor discriminant analysis (GTDA)
  - TVP-based: Uncorrelated Multilinear Discriminant Analysis (UMLDA)

### Multilinear canonical correlation analysis

- Multilinear extension of CCA
  - TTP-based: Tensor Canonical Correlation Analysis (TCCA)
  - TVP-based: Multilinear Canonical Correlation Analysis (MCCA)
  - TVP-based: Bayesian Multilinear Canonical Correlation Analysis (BMTF)
- A TTP is a direct projection of a high-dimensional tensor to a low-dimensional tensor of the same order, using *N* projection matrices for an *N*th-order tensor. It can be performed in *N* steps with each step performing a tensor-matrix multiplication (product). The *N* steps are exchangeable. This projection is an extension of the higher-order singular value decomposition (HOSVD) to subspace learning. Hence, its origin is traced back to the Tucker decomposition in 1960s.

- A TVP is a direct projection of a high-dimensional tensor to a low-dimensional vector, which is also referred to as the rank-one projections. As TVP projects a tensor to a vector, it can be viewed as multiple projections from a tensor to a scalar. Thus, the TVP of a tensor to a *P*-dimensional vector consists of *P* projections from the tensor to a scalar. The projection from a tensor to a scalar is an elementary multilinear projection (EMP). In EMP, a tensor is projected to a point through *N* unit projection vectors. It is the projection of a tensor on a single line (resulting a scalar), with one projection vector in each mode. Thus, the TVP of a tensor object to a vector in a *P*-dimensional vector space consists of *P* EMPs. This projection is an extension of the canonical decomposition, also known as the parallel factors (PARAFAC) decomposition.

### Typical approach in MSL

There are *N* sets of parameters to be solved, one in each mode. The solution to one set often depends on the other sets (except when *N=1*, the linear case). Therefore, the suboptimal iterative procedure in is followed.

1. Initialization of the projections in each mode
2. For each mode, fixing the projection in all the other mode, and solve for the projection in the current mode.
3. Do the mode-wise optimization for a few iterations or until convergence.

This is originated from the alternating least square method for multi-way data analysis.

## Code

- MATLAB Tensor Toolbox by Sandia National Laboratories.
- The MPCA algorithm written in Matlab (MPCA+LDA included).
- The UMPCA algorithm written in Matlab (data included).
- The UMLDA algorithm written in Matlab (data included).

## Tensor data sets

- 3D gait data (third-order tensors): 128x88x20(21.2M); 64x44x20(9.9M); 32x22x10(3.2M);

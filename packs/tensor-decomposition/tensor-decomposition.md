---
title: "Tensor decomposition"
source: https://en.wikipedia.org/wiki/Tensor_decomposition
domain: tensor-decomposition
license: CC-BY-SA-4.0
tags: tensor decomposition, tucker decomposition, canonical polyadic decomposition, tensor rank
fetched: 2026-07-02
---

# Tensor decomposition

In multilinear algebra, a **tensor decomposition** is any scheme for expressing a "data tensor" (M-way array) as a sequence of elementary operations acting on other, often simpler tensors. Many tensor decompositions generalize some matrix decompositions.

Tensors are generalizations of matrices to higher dimensions (or rather to higher orders, i.e. the higher number of dimensions) and can consequently be treated as multidimensional fields. The main tensor decompositions are:

- Tensor rank decomposition;
- Higher-order singular value decomposition;
- Tucker decomposition;
- matrix product states, and operators or tensor trains;
- Online Tensor Decompositions
- hierarchical Tucker decomposition;
- block term decomposition

## Notation

This section introduces basic notations and operations that are widely used in the field.

| Symbols | Definition |
|---|---|
| ${a,{\bf {a}},{\bf {a}}^{T},\mathbf {A} ,{\mathcal {A}}}$ | scalar, vector, row, matrix, tensor |
| ${\bf {a}}={vec(.)}$ | vectorizing either a matrix or a tensor |
| ${\bf {A}}_{[m]}$ | matrixized tensor ${\mathcal {A}}$ |
| $\times _{m}$ | mode-m product |

## Introduction

A multi-way graph with K perspectives is a collection of K matrices ${X_{1},X_{2}.....X_{K}}$ with dimensions I × J (where I, J are the number of nodes). This collection of matrices is naturally represented as a tensor X of size I × J × K. In order to avoid overloading the term “dimension”, we call an I × J × K tensor a three “mode” tensor, where “modes” are the numbers of indices used to index the tensor.

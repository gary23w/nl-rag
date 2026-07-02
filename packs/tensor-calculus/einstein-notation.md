---
title: "Einstein notation"
source: https://en.wikipedia.org/wiki/Einstein_notation
domain: tensor-calculus
license: CC-BY-SA-4.0
tags: tensor calculus, tensor field, einstein notation, metric tensor
fetched: 2026-07-02
---

# Einstein notation

In mathematics, especially the usage of linear algebra in mathematical physics and differential geometry, **Einstein notation** (also known as the **Einstein summation convention** or **Einstein summation notation**) is a notational convention that implies summation over a set of indexed terms in a formula, thus achieving brevity. As part of mathematics it is a notational subset of Ricci calculus; however, it is often used in physics applications that do not distinguish between tangent and cotangent spaces. It was introduced to physics by Albert Einstein in 1916.

## Introduction

### Statement of convention

According to this convention, when an index variable appears twice in a single term and is not otherwise defined (see Free and bound variables), it implies summation of that term over all the values of the index. So where the indices can range over the set $\{1,2,3\}$ , $y=\sum _{i=1}^{3}x^{i}e_{i}=x^{1}e_{1}+x^{2}e_{2}+x^{3}e_{3}$ is simplified by the convention to: $y=x^{i}e_{i}$

The upper indices are not exponents but are indices of coordinates, coefficients or basis vectors. That is, in this context $x^{2}$ should be understood as the second component of x rather than the square of x (this can occasionally lead to ambiguity). The upper index position in $x^{i}$ is because, typically, an index occurs once in an upper (superscript) and once in a lower (subscript) position in a term (see *§ Application* below). Typically, $(x^{1}\ x^{2}\ x^{3})$ would be equivalent to the traditional $(x\ y\ z)$ .

In general relativity, a common convention is that

- the Greek alphabet is used for space and time components, where indices take on values 0, 1, 2, or 3 (frequently used letters include $\mu$ , $\nu$ , etc.),
- the Latin alphabet is used for spatial components only, where indices take on values 1, 2, or 3 (frequently used letters are i , j ,...),

In general, indices can range over any indexing set, including an infinite set. This should not be confused with a typographically similar convention used to distinguish between tensor index notation and the closely related but distinct basis-independent abstract index notation.

An index that is summed over is a *summation index*, in this case " i ". It is also called a dummy index since any symbol can replace " i " without changing the meaning of the expression (provided that it does not collide with other index symbols in the same term).

An index that is not summed over is a *free index* and should appear only once per term. If such an index does appear, it usually also appears in every other term in an equation. An example of a free index is the " i " in the equation $v_{i}=a_{i}b_{j}x^{j}$ , which is equivalent to the equation ${\textstyle v_{i}=\sum _{j}(a_{i}b_{j}x^{j})}$ .

### Application

Einstein notation can be applied in slightly different ways. Typically, each index occurs once in an upper (superscript) and once in a lower (subscript) position in a term; however, the convention can be applied more generally to any repeated indices within a term. When dealing with covariant and contravariant vectors, where the position of an index indicates the type of vector, the first case usually applies; a covariant vector can only be contracted with a contravariant vector, corresponding to summation of the products of coefficients. On the other hand, when there is a fixed coordinate basis (or when not considering coordinate vectors), one may choose to use only subscripts; see *§ Superscripts and subscripts versus only subscripts* below.

## Vector representations

### Superscripts and subscripts versus only subscripts

In terms of covariance and contravariance of vectors,

- upper indices represent components of contravariant vectors (vectors),
- lower indices represent components of covariant vectors (covectors).

They transform contravariantly or covariantly, respectively, with respect to change of basis.

In recognition of this fact, the following notation uses the same symbol both for a vector or covector and its *components*, as in: ${\begin{aligned}v=e_{i}v^{i}={\begin{bmatrix}e_{1}&e_{2}&\cdots &e_{n}\end{bmatrix}}{\begin{bmatrix}v^{1}\\v^{2}\\\vdots \\v^{n}\end{bmatrix}}\\w=w_{i}e^{i}={\begin{bmatrix}w_{1}&w_{2}&\cdots &w_{n}\end{bmatrix}}{\begin{bmatrix}e^{1}\\e^{2}\\\vdots \\e^{n}\end{bmatrix}}\end{aligned}}$

where v is the vector and $v^{i}$ are its components (not the i th covector v ), w is the covector and $w_{i}$ are its components. The basis vector elements $e_{i}$ are each column vectors, and the covector basis elements $e^{i}$ are each row covectors. (See also § Abstract description; duality, below and the examples)

In the presence of a non-degenerate form (an isomorphism $V\to V^{*}$ , for instance a Riemannian metric or Minkowski metric), one can raise and lower indices.

A basis gives such a form (via the dual basis), hence when working on $\mathbb {R} ^{n}$ with a Euclidean metric and a fixed orthonormal basis, one has the option to work with only subscripts.

However, if one changes coordinates, the way that coefficients change depends on the variance of the object, and one cannot ignore the distinction; see Covariance and contravariance of vectors.

### Mnemonics

In the above example, vectors are represented as $n\times 1$ matrices (column vectors), while covectors are represented as $1\times n$ matrices (row covectors).

When using the column vector convention:

- "**Up**per indices go **up** to down; **l**ower indices go **l**eft to right."
- "**Co**variant tensors are **row** vectors that have indices that are **below** (**co-row-below**)."
- Covectors are row vectors: ${\begin{bmatrix}w_{1}&\cdots &w_{k}\end{bmatrix}}.$ Hence the lower index indicates which *column* you are in.
- Contravariant vectors are column vectors: ${\begin{bmatrix}v^{1}\\\vdots \\v^{k}\end{bmatrix}}$ Hence the upper index indicates which *row* you are in.

### Abstract description

The virtue of Einstein notation is that it represents the invariant quantities with a simple notation.

In physics, a scalar is invariant under transformations of basis. In particular, a Lorentz scalar is invariant under a Lorentz transformation. The individual terms in the sum are not. When the basis is changed, the *components* of a vector change by a linear transformation described by a matrix. This led Einstein to propose the convention that repeated indices imply the summation is to be done.

As for covectors, they change by the inverse matrix. This is designed to guarantee that the linear function associated with the covector, the sum above, is the same no matter what the basis is.

The value of the Einstein convention is that it applies to other vector spaces built from V using the tensor product and duality. For example, $V\otimes V$ , the tensor product of V with itself, has a basis consisting of tensors of the form $\mathbf {e} _{ij}=\mathbf {e} _{i}\otimes \mathbf {e} _{j}$ . Any tensor $\mathbf {T}$ in $V\otimes V$ can be written as: $\mathbf {T} =T^{ij}\mathbf {e} _{ij}.$

The dual space $V^{*}$ of V has a basis $\mathbf {e} ^{1},\mathbf {e} ^{2},\dots ,\mathbf {e} ^{n}$ which obeys the rule $\mathbf {e} ^{i}(\mathbf {e} _{j})=\delta _{j}^{i}.$ where $\delta$ is the Kronecker delta. As $\operatorname {Hom} (V,W)=V^{*}\otimes W$ the row/column coordinates on a matrix correspond to the upper/lower indices on the tensor product.

## Common operations in this notation

In Einstein notation, the usual element reference $A_{mn}$ for the m -th row and n -th column of matrix A becomes ${A^{m}}_{n}$ . We can then write the following operations in Einstein notation as follows.

### Inner product

The inner product of two vectors is the sum of the products of their corresponding components, with the indices of one vector lowered (see #Raising and lowering indices): $\langle \mathbf {u} ,\mathbf {v} \rangle =\langle \mathbf {e} _{i},\mathbf {e} _{j}\rangle u^{i}v^{j}=u_{j}v^{j}$ In the case of an orthonormal basis, we have $u^{j}=u_{j}$ , and the expression simplifies to: $\langle \mathbf {u} ,\mathbf {v} \rangle =\sum _{j}u^{j}v^{j}=u_{j}v^{j}$

### Vector cross product

In three dimensions, the cross product of two vectors with respect to a positively oriented orthonormal basis, meaning that $\mathbf {e} _{1}\times \mathbf {e} _{2}=\mathbf {e} _{3}$ , can be expressed as: $\mathbf {u} \times \mathbf {v} =\varepsilon _{\,jk}^{i}u^{j}v^{k}\mathbf {e} _{i}$

Here, $\varepsilon _{\,jk}^{i}=\varepsilon _{ijk}$ is the Levi-Civita symbol. Since the basis is orthonormal, raising the index i does not alter the value of $\varepsilon _{ijk}$ , when treated as a tensor.

### Matrix-vector multiplication

The product of a matrix $A_{ij}$ with a column vector $v_{j}$ is: $\mathbf {u} _{i}=(\mathbf {A} \mathbf {v} )_{i}=\sum _{j=1}^{N}A_{ij}v_{j}$ equivalent to $u^{i}={A^{i}}_{j}v^{j}$

This is a special case of matrix multiplication.

### Matrix multiplication

The matrix product of two matrices $A_{ij}$ and $B_{jk}$ is: $\mathbf {C} _{ik}=(\mathbf {A} \mathbf {B} )_{ik}=\sum _{j=1}^{N}A_{ij}B_{jk}$

equivalent to ${C^{i}}_{k}={A^{i}}_{j}{B^{j}}_{k}$

### Trace

For a square matrix ${A^{i}}_{j}$ , the trace is the sum of the diagonal elements, hence the sum over a common index ${A^{i}}_{i}$ .

### Outer product

The outer product of the column vector $u^{i}$ by the row vector $v_{j}$ yields an $m\times n$ matrix $\mathbf {A}$ : ${A^{i}}_{j}=u^{i}v_{j}={(uv)^{i}}_{j}$

Since i and j represent two *different* indices, there is no summation and the indices are not eliminated by the multiplication.

### Raising and lowering indices

Given a tensor, one can raise an index or lower an index by contracting the tensor with the metric tensor, $g_{\mu \nu }$ . For example, taking the tensor ${T^{\alpha }}_{\beta }$ , one can lower an index: $g_{\mu \sigma }{T^{\sigma }}_{\beta }=T_{\mu \beta }$

Or one can raise an index: $g^{\mu \sigma }{T_{\sigma }}^{\alpha }=T^{\mu \alpha }$

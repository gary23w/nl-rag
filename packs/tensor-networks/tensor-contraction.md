---
title: "Tensor contraction"
source: https://en.wikipedia.org/wiki/Tensor_contraction
domain: tensor-networks
license: CC-BY-SA-4.0
tags: tensor network, tensor contraction, density matrix renormalization group, penrose graphical notation
fetched: 2026-07-02
---

# Tensor contraction

In multilinear algebra, a **tensor contraction** is an operation on a tensor that arises from the canonical pairing of a vector space and its dual.

This example with two small matrices (tensors) shows how it works. ${\begin{bmatrix}1&2\\3&4\end{bmatrix}}{\begin{bmatrix}5&6\\7&8\end{bmatrix}}={\begin{bmatrix}1\cdot 5+2\cdot 7&1\cdot 6+2\cdot 8\\3\cdot 5+4\cdot 7&3\cdot 6+4\cdot 8\\\end{bmatrix}}={\begin{bmatrix}19&22\\43&50\end{bmatrix}}$

When calculating with matrices or tensors, often it's useful to move the second tensor up, and put the result underneath, just for calculation purposes. That way, each row of the first matrix (1234), and each column of the second matrix (5678), point to the cell of the result that they produce. Of course, these matrices can be larger than 2x2; often 3x3 or 4x4 are used, but any size is allowed.

In simple index notation, this is written ${\textstyle \sum _{j=1}^{2}a_{ij}\times b_{jk}=c_{ik}}$ where i, j and k all range over 1, 2. Notice how the index j, in between, disappears; this is the essence of tensor contraction.

In Einstein notation, this would be ${\textstyle a_{i}{}^{j}\times b_{j}{}^{k}=c_{i}{}^{k}}$ . The superscripts work just like subscripts, with a different meaning. Only repeated, raised and lowered indices are summed over. Objects can have more than two indices, also.

Tensor contraction can be seen as a generalization of the trace.

## Abstract formulation

Let *V* be a vector space over a field *k*. The core of the contraction operation, and the simplest case, is the canonical pairing of *V* with its dual vector space *V*∗. The pairing is the linear map from the tensor product of these two spaces to the field *k*:

$C:V\otimes V^{*}\rightarrow k$

corresponding to the bilinear form

$\langle v,f\rangle =f(v)$

where *f* is in *V*∗ and *v* is in *V*. The map *C* defines the contraction operation on a tensor of type (1, 1), which is an element of $V\otimes V^{*}$ . Note that the result is a scalar (an element of *k*). In finite dimensions, using the natural isomorphism between $V\otimes V^{*}$ and the space of linear maps from *V* to *V*, one obtains a basis-free definition of the trace.

In general, a tensor of type (*m*, *n*) (with *m* ≥ 1 and *n* ≥ 1) is an element of the vector space

$V\otimes \cdots \otimes V\otimes V^{*}\otimes \cdots \otimes V^{*}$

(where there are *m* factors *V* and *n* factors *V*∗). Applying the canonical pairing to the *k*th *V* factor and the *l*th *V*∗ factor, and using the identity on all other factors, defines the (*k*, *l*) contraction operation, which is a linear map that yields a tensor of type (*m* − 1, *n* − 1). By analogy with the (1, 1) case, the general contraction operation is sometimes called the trace.

## Contraction in index notation

In tensor index notation, the basic contraction of a vector and a dual vector is denoted by

${\tilde {f}}({\vec {v}})=f_{\gamma }v^{\gamma },$

which is shorthand for the explicit coordinate summation

$f_{\gamma }v^{\gamma }=f_{1}v^{1}+f_{2}v^{2}+\cdots +f_{n}v^{n}$

(where *v**i* are the components of *v* in a particular basis and *f**i* are the components of *f* in the corresponding dual basis).

Since a general mixed dyadic tensor is a linear combination of decomposable tensors of the form $f\otimes v$ , the explicit formula for the dyadic case follows: let

$\mathbf {T} =T_{j}^{i}\mathbf {e} _{i}\otimes \mathbf {e} ^{j}$

be a mixed dyadic tensor. Then its contraction is

$T_{j}^{i}\mathbf {e} _{i}\cdot \mathbf {e} ^{j}=T_{j}^{i}\delta _{i}{}^{j}=T_{j}^{j}=T_{1}^{1}+\cdots +T_{n}^{n}$ .

A general contraction is denoted by labeling one covariant index and one contravariant index with the same letter, summation over that index being implied by the summation convention. The resulting contracted tensor inherits the remaining indices of the original tensor. For example, contracting a tensor *T* of type (2,2) on the second and third indices to create a new tensor *U* of type (1,1) is written as

$T^{ab}{}_{bc}=\sum _{b}{T^{ab}{}_{bc}}=T^{a1}{}_{1c}+T^{a2}{}_{2c}+\cdots +T^{an}{}_{nc}=U^{a}{}_{c}.$

By contrast, let

$\mathbf {T} =\mathbf {e} ^{i}\otimes \mathbf {e} ^{j}$

be an unmixed dyadic tensor. This tensor does not contract; if its base vectors are dotted, the result is the contravariant metric tensor,

$g^{ij}=\mathbf {e} ^{i}\cdot \mathbf {e} ^{j},$

whose rank is 2.

## Metric contraction

As in the previous example, contraction on a pair of indices that are either both contravariant or both covariant is not possible in general. However, in the presence of an inner product (also known as a metric) *g*, such contractions are possible. One uses the metric to raise or lower one of the indices, as needed, and then one uses the usual operation of contraction. The combined operation is known as *metric contraction*.

## Application to tensor fields

Contraction is often applied to tensor fields over spaces (e.g. Euclidean space, manifolds, or schemes). Since contraction is a purely algebraic operation, it can be applied pointwise to a tensor field, e.g. if *T* is a (1,1) tensor field on Euclidean space, then in any coordinates, its contraction (a scalar field) *U* at a point *x* is given by

$U(x)=\sum _{i}T_{i}^{i}(x)$

Since the role of *x* is not complicated here, it is often suppressed, and the notation for tensor fields becomes identical to that for purely algebraic tensors.

Over a Riemannian manifold, a metric (field of inner products) is available, and both metric and non-metric contractions are crucial to the theory. For example, the Ricci tensor is a non-metric contraction of the Riemann curvature tensor, and the scalar curvature is the unique metric contraction of the Ricci tensor.

One can also view contraction of a tensor field in the context of modules over an appropriate ring of functions on the manifold or the context of sheaves of modules over the structure sheaf; see the discussion at the end of this article.

### Tensor divergence

As an application of the contraction of a tensor field, let *V* be a vector field on a Riemannian manifold (for example, Euclidean space). Let $V^{\alpha }{}_{\beta }$ be the covariant derivative of *V* (in some choice of coordinates). In the case of Cartesian coordinates in Euclidean space, one can write

$V^{\alpha }{}_{\beta }={\partial V^{\alpha } \over \partial x^{\beta }}.$

Then changing index *β* to *α* causes the pair of indices to become bound to each other, so that the derivative contracts with itself to obtain the following sum:

$V^{\alpha }{}_{\alpha }=V^{0}{}_{0}+\cdots +V^{n}{}_{n},$

which is the divergence div *V*. Then

$\operatorname {div} V=V^{\alpha }{}_{\alpha }=0$

is a continuity equation for *V*.

In general, one can define various divergence operations on higher-rank tensor fields, as follows. If *T* is a tensor field with at least one contravariant index, taking the covariant differential and contracting the chosen contravariant index with the new covariant index corresponding to the differential results in a new tensor of rank one lower than that of *T*.

## Contraction of a pair of tensors

One can generalize the core contraction operation (vector with dual vector) in a slightly different way, by considering a pair of tensors *T* and *U*. The tensor product $T\otimes U$ is a new tensor, which, if it has at least one covariant and one contravariant index, can be contracted. The case where *T* is a vector and *U* is a dual vector is exactly the core operation introduced first in this article.

In tensor index notation, to contract two tensors with each other, one places them side by side (juxtaposed) as factors of the same term. This implements the tensor product, yielding a composite tensor. Contracting two indices in this composite tensor implements the desired contraction of the two tensors.

For example, matrices can be represented as tensors of type (1,1) with the first index being contravariant and the second index being covariant. Let $\Lambda ^{\alpha }{}_{\beta }$ be the components of one matrix and let $\mathrm {M} ^{\beta }{}_{\gamma }$ be the components of a second matrix. Then their multiplication is given by the following contraction, an example of the contraction of a pair of tensors:

$\Lambda ^{\alpha }{}_{\beta }\mathrm {M} ^{\beta }{}_{\gamma }=\mathrm {N} ^{\alpha }{}_{\gamma }.$

Also, the interior product of a vector with a differential form is a special case of the contraction of two tensors with each other.

## More general algebraic contexts

Let *R* be a commutative ring and let *M* be a finite free module over *R*. Then contraction operates on the full (mixed) tensor algebra of *M* in exactly the same way as it does in the case of vector spaces over a field. (The key fact is that the canonical pairing is still perfect in this case.)

More generally, let *O*X be a sheaf of commutative rings over a topological space *X*, e.g. *O*X could be the structure sheaf of a complex manifold, analytic space, or scheme. Let *M* be a locally free sheaf of modules over *O*X of finite rank. Then the dual of *M* is still well-behaved and contraction operations make sense in this context.

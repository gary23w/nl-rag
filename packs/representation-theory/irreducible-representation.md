---
title: "Irreducible representation"
source: https://en.wikipedia.org/wiki/Irreducible_representation
domain: representation-theory
license: CC-BY-SA-4.0
tags: representation theory, group representation, character theory, irreducible representation
fetched: 2026-07-02
---

# Irreducible representation

In mathematics, specifically in the representation theory of groups and algebras, an **irreducible representation** $(\rho ,V)$ or **irrep** of an algebraic structure A is a nonzero representation that has no proper nontrivial subrepresentation $(\rho |_{W},W)$ , with $W\subset V$ closed under the action of $\{\rho (a):a\in A\}$ .

Every finite-dimensional unitary representation on a Hilbert space V is the direct sum of irreducible representations. Irreducible representations are always **indecomposable** (i.e. cannot be decomposed further into a direct sum of representations), but the converse may not hold, e.g. the two-dimensional representation of the real numbers acting by upper triangular unipotent matrices is indecomposable but reducible.

## History

Group representation theory was generalized by Richard Brauer from the 1940s to give modular representation theory, in which the matrix operators act on a vector space over a field K of arbitrary characteristic, rather than a vector space over the field of real numbers or over the field of complex numbers. The structure analogous to an irreducible representation in the resulting theory is a simple module.

## Overview

Let $\rho$ be a representation i.e. a homomorphism $\rho :G\to GL(V)$ of a group G where V is a vector space over a field F . If we pick a basis B for V , $\rho$ can be thought of as a function (a homomorphism) from a group into a set of invertible matrices and in this context is called a **matrix representation**. However, it simplifies things greatly if we think of the space V without a basis. $\rho$ is **d-dimensional** if the vector space V it acts over has dimension d .

A linear subspace $W\subset V$ is called **G -invariant** if $\rho (g)w\in W$ for all $g\in G$ and all $w\in W$ . The co-restriction of $\rho$ to the general linear group of a G -invariant subspace $W\subset V$ is known as a **subrepresentation**. A representation $\rho :G\to GL(V)$ is said to be **irreducible** if it has only trivial subrepresentations (all representations can form a subrepresentation with the trivial G -invariant subspaces, e.g. the whole vector space V , and {0}). If there is a proper nontrivial invariant subspace, $\rho$ is said to be **reducible**.

### Notation and terminology of group representations

Group elements can be represented by matrices, although the term "represented" has a specific and precise meaning in this context. A representation of a group is a mapping from the group elements to the general linear group of matrices. As notation, let *a*, *b*, *c*, ... denote elements of a group *G* with group product signified without any symbol, so *ab* is the group product of *a* and *b* and is also an element of *G*, and let representations be indicated by *D*. The **representation of *a*** is written as

$D(a)={\begin{pmatrix}D(a)_{11}&D(a)_{12}&\cdots &D(a)_{1n}\\D(a)_{21}&D(a)_{22}&\cdots &D(a)_{2n}\\\vdots &\vdots &\ddots &\vdots \\D(a)_{n1}&D(a)_{n2}&\cdots &D(a)_{nn}\\\end{pmatrix}}$

By definition of group representations, the representation of a group product is translated into matrix multiplication of the representations:

$D(ab)=D(a)D(b)$

If *e* is the identity element of the group (so that *ae* = *ea* = *a*, etc.), then *D*(*e*) is an identity matrix, or identically a block matrix of identity matrices, since we must have

$D(ea)=D(ae)=D(a)D(e)=D(e)D(a)=D(a)$

and similarly for all other group elements. The last two statements correspond to the requirement that *D* is a group homomorphism.

### Reducible and irreducible representations

A representation is reducible if it contains a nontrivial G-invariant subspace, that is to say, all the matrices $D(a)$ can be put in upper triangular block form by the same invertible matrix P . In other words, if there is a similarity transformation:

$D'(a)\equiv P^{-1}D(a)P,$

which maps every matrix in the representation into the same pattern upper triangular blocks. Every ordered sequence minor block is a group subrepresentation. That is to say, if the representation is, for example, of dimension 2, then we have: $D'(a)=P^{-1}D(a)P={\begin{pmatrix}D^{(11)}(a)&D^{(12)}(a)\\0&D^{(22)}(a)\end{pmatrix}},$

where $D^{(11)}(a)$ is a nontrivial subrepresentation. If we are able to find a matrix P that makes $D^{(12)}(a)=0$ as well, then $D(a)$ is not only reducible but also decomposable.

**Notice:** Even if a representation is reducible, its matrix representation may still not be the upper triangular block form. It will only have this form if we choose a suitable basis, which can be obtained by applying the matrix $P^{-1}$ above to the standard basis.

### Decomposable and indecomposable representations

A representation is decomposable if all the matrices $D(a)$ can be put in block-diagonal form by the same invertible matrix P . In other words, if there is a similarity transformation:

$D'(a)\equiv P^{-1}D(a)P,$

which diagonalizes every matrix in the representation into the same pattern of diagonal blocks. Each such block is then a group subrepresentation independent from the others. The representations *D*(*a*) and *D′*(*a*) are said to be **equivalent representations**. The (*k*-dimensional, say) representation can be decomposed into a direct sum of *k* > 1 matrices:

$D'(a)=P^{-1}D(a)P={\begin{pmatrix}D^{(1)}(a)&0&\cdots &0\\0&D^{(2)}(a)&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &D^{(k)}(a)\\\end{pmatrix}}=D^{(1)}(a)\oplus D^{(2)}(a)\oplus \cdots \oplus D^{(k)}(a),$

so *D*(*a*) is **decomposable**, and it is customary to label the decomposed matrices by a superscript in brackets, as in *D*(*n*)(*a*) for *n* = 1, 2, ..., *k*, although some authors just write the numerical label without parentheses.

The dimension of *D*(*a*) is the sum of the dimensions of the blocks:

$\dim[D(a)]=\dim[D^{(1)}(a)]+\dim[D^{(2)}(a)]+\cdots +\dim[D^{(k)}(a)].$

If this is not possible, i.e. *k* = 1, then the representation is indecomposable.

**Notice**: Even if a representation is decomposable, its matrix representation may not be the diagonal block form. It will only have this form if we choose a suitable basis, which can be obtained by applying the matrix $P^{-1}$ above to the standard basis.

### Connection between irreducible representation and indecomposable representation

An irreducible representation is by nature an indecomposable one. The converse may fail; however, for finite groups, under some conditions, we do have an indecomposable representation being an irreducible representation (Maschke's theorem):

When the group G is finite, and K is a field with $char(K)\nmid |G|$ , then an indecomposable representation of G over K is an irreducible representation. In particular, this is true for $K=\mathbb {C}$ .

## Examples of irreducible representations

### Trivial representation

All groups G have a one-dimensional, irreducible trivial representation by mapping all group elements to the identity transformation.

### One-dimensional representation

Any one-dimensional representation is irreducible since it has no proper nontrivial invariant subspaces.

### Irreducible complex representations

The irreducible complex representations of a finite group G can be characterized using results from character theory. In particular, all complex representations decompose as a direct sum of irreps, and the number of irreps of G is equal to the number of conjugacy classes of G .

- The irreducible complex representations of $\mathbb {Z} /n\mathbb {Z}$ are exactly given by the maps $1\mapsto \gamma$ , where $\gamma$ is an n th root of unity.
- Let V be an n -dimensional complex representation of $S_{n}$ with basis $\{v_{i}\}_{i=1}^{n}$ . Then V decomposes as a direct sum of the irreps $V_{\text{triv}}=\mathbb {C} \left(\sum _{i=1}^{n}v_{i}\right)$ and the orthogonal subspace given by $V_{\text{std}}=\left\{\sum _{i=1}^{n}a_{i}v_{i}:a_{i}\in \mathbb {C} ,\sum _{i=1}^{n}a_{i}=0\right\}.$ The former irrep is one-dimensional and isomorphic to the trivial representation of $S_{n}$ . The latter is $n-1$ dimensional and is known as the standard representation of $S_{n}$ .
- Let G be a group. The regular representation of G is the free complex vector space on the basis $\{e_{g}\}_{g\in G}$ with the group action $g\cdot e_{g'}=e_{gg'}$ , denoted $\mathbb {C} G.$ All irreducible representations of G appear in the decomposition of $\mathbb {C} G$ as a direct sum of irreps.

### Example of an irreducible representation over **F***p*

- Let G be a p group and $V=\mathbb {F} _{p}^{n}$ be a finite dimensional irreducible representation of G over $\mathbb {F} _{p}$ . By Orbit-stabilizer theorem, the orbit of every V element acted by the p group G has size being power of p . Since the sizes of all these orbits sum up to the size of G , and $0\in V$ is in a size 1 orbit only containing itself, there must be other orbits of size 1 for the sum to match. That is, there exists some $v\in V$ such that $gv=v$ for all $g\in G$ . This forces every irreducible representation of a p group over $\mathbb {F} _{p}$ to be one dimensional.

## Applications in theoretical physics and chemistry

In quantum physics and quantum chemistry, each set of degenerate eigenstates of the Hamiltonian operator comprises a vector space V for a representation of the symmetry group of the Hamiltonian, a "multiplet", best studied through reduction to its irreducible parts. Identifying the irreducible representations therefore allows one to label the states, predict how they will split under perturbations; or transition to other states in V. Thus, in quantum mechanics, irreducible representations of the symmetry group of the system partially or completely label the energy levels of the system, allowing the selection rules to be determined.

## Lie groups

### Lorentz group

The irreps of *D*(**K**) and *D*(**J**), where **J** is the generator of rotations and **K** the generator of boosts, can be used to build to spin representations of the Lorentz group, because they are related to the spin matrices of quantum mechanics. This allows them to derive relativistic wave equations.

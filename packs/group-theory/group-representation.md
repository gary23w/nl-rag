---
title: "Group representation"
source: https://en.wikipedia.org/wiki/Group_representation
domain: group-theory
license: CC-BY-SA-4.0
tags: group theory, abstract algebra, symmetry group, abelian group
fetched: 2026-07-02
---

# Group representation

In the mathematical field of representation theory, **group representations** describe abstract groups in terms of bijective linear transformations of a vector space to itself (i.e. vector space automorphisms); in particular, they can be used to represent group elements as invertible matrices so that the group operation can be represented by matrix multiplication.

In chemistry, a group representation can relate mathematical group elements to symmetric rotations and reflections of molecules.

Representations of groups allow many group-theoretic problems to be reduced to problems in linear algebra. In physics, they describe how the symmetry group of a physical system affects the solutions of equations describing that system.

The term *representation of a group* is also used in a more general sense to mean any "description" of a group as a group of transformations of some mathematical object. More formally, a "representation" means a homomorphism from the group to the automorphism group of an object. If the object is a vector space we have a *linear representation*. Some people use *realization* for the general notion and reserve the term *representation* for the special case of linear representations. The bulk of this article describes linear representation theory; see the last section for generalizations.

## Branches of group representation theory

The representation theory of groups divides into subtheories depending on the kind of group being represented. The various theories are quite different in detail, though some basic definitions and concepts are similar. The most important divisions are:

- *Finite groups* — Group representations are a very important tool in the study of finite groups. They also arise in the applications of finite group theory to crystallography and to geometry. If the field of scalars of the vector space has characteristic *p*, and if *p* divides the order of the group, then this is called *modular representation theory*; this special case has very different properties. See Representation theory of finite groups.
- *Compact groups or locally compact groups* — Many of the results of finite group representation theory are proved by averaging over the group. These proofs can be carried over to infinite groups by replacement of the average with an integral, provided that an acceptable notion of integral can be defined. This can be done for locally compact groups, using the Haar measure. The resulting theory is a central part of harmonic analysis. The Pontryagin duality describes the theory for commutative groups, as a generalised Fourier transform. See also: Peter–Weyl theorem.
- *Lie groups* — Many important Lie groups are compact, so the results of compact representation theory apply to them. Other techniques specific to Lie groups are used as well. Most of the groups important in physics and chemistry are Lie groups, and their representation theory is crucial to the application of group theory in those fields. See Representations of Lie groups and Representations of Lie algebras.
- *Linear algebraic groups* (or more generally *affine group schemes*) — These are the analogues of Lie groups, but over more general fields than just **R** or **C**. Although linear algebraic groups have a classification that is very similar to that of Lie groups, and give rise to the same families of Lie algebras, their representations are rather different (and much less well understood). The analytic techniques used for studying Lie groups must be replaced by techniques from algebraic geometry, where the relatively weak Zariski topology causes many technical complications.
- *Non-compact topological groups* — The class of non-compact groups is too broad to construct any general representation theory, but specific special cases have been studied, sometimes using ad hoc techniques. The *semisimple Lie groups* have a deep theory, building on the compact case. The complementary *solvable* Lie groups cannot be classified in the same way. The general theory for Lie groups deals with semidirect products of the two types, by means of general results called *Mackey theory*, which is a generalization of Wigner's classification methods.

Representation theory also depends heavily on the type of vector space on which the group acts. One distinguishes between finite-dimensional representations and infinite-dimensional ones. In the infinite-dimensional case, additional structures are important (e.g. whether or not the space is a Hilbert space, Banach space, etc.).

One must also consider the type of field over which the vector space is defined. The most important case is the field of complex numbers. The other important cases are the field of real numbers, finite fields, and fields of p-adic numbers. In general, algebraically closed fields are easier to handle than non-algebraically closed ones. The characteristic of the field is also significant; many theorems for finite groups depend on the characteristic of the field not dividing the order of the group.

## Definitions

A **representation** of a group *G* on a vector space *V* over a field *K* is a group homomorphism from *G* to GL(*V*), the general linear group on *V*. That is, a representation is a map

$\rho \colon G\to \mathrm {GL} \left(V\right)$

such that

$\rho (g_{1}g_{2})=\rho (g_{1})\rho (g_{2}),\qquad {\text{for all }}g_{1},g_{2}\in G.$

Here *V* is called the **representation space** and the dimension of *V* is called the **dimension** or **degree** of the representation. It is common practice to refer to *V* itself as the representation when the homomorphism is clear from the context.

In the case where *V* is of finite dimension *n* it is common to choose a basis for *V* and identify GL(*V*) with GL(*n*, *K*), the group of $n\times n$ invertible matrices on the field *K*.

- If *G* is a topological group and *V* is a topological vector space, a **continuous representation** of *G* on *V* is a representation *ρ* such that the application Φ : *G* × *V* → *V* defined by Φ(*g*, *v*) = *ρ*(*g*)(*v*) is continuous.
- The **kernel** of a representation *ρ* of a group *G* is defined as the normal subgroup of *G* whose image under *ρ* is the identity transformation:

$\ker \rho =\left\{g\in G\mid \rho (g)=\mathrm {id} \right\}.$

A

faithful representation

is one in which the homomorphism

G

→ GL(

V

)

is

injective

; in other words, one whose kernel is the trivial subgroup {

e

} consisting only of the group's identity element.

- Given two *K* vector spaces *V* and *W*, a **map** of two representations *ρ* : *G* → GL(*V*) and *π* : *G* → GL(*W*) (also called an equivariant map) is a linear map *α* : *V* → *W* such that $\alpha \circ \rho (g)=\pi (g)\circ \alpha .$

If

α

has an inverse equivariant map, the map is called an

isomorphism

of representations and the representations are said to be

equivalent

or

isomorphic

. It is also sufficient that

α

is an equivariant map which is an isomorphism of vector spaces.

## Examples

Consider the complex number $u=e^{2\pi i/3}$ which has the property $u^{3}=1$ . The set $C_{3}=\{1,u,u^{2}\}$ forms a cyclic group under multiplication. This group has a representation $\rho$ on $\mathbb {C} ^{2}$ given by:

$\rho \left(1\right)={\begin{bmatrix}1&0\\0&1\\\end{bmatrix}}\qquad \rho \left(u\right)={\begin{bmatrix}1&0\\0&u\\\end{bmatrix}}\qquad \rho \left(u^{2}\right)={\begin{bmatrix}1&0\\0&u^{2}\\\end{bmatrix}}.$

This representation is faithful because $\rho$ is a one-to-one map.

Another representation for $C_{3}$ on $\mathbb {C} ^{2}$ , isomorphic to the previous one, is $\sigma$ given by:

$\sigma \left(1\right)={\begin{bmatrix}1&0\\0&1\\\end{bmatrix}}\qquad \sigma \left(u\right)={\begin{bmatrix}u&0\\0&1\\\end{bmatrix}}\qquad \sigma \left(u^{2}\right)={\begin{bmatrix}u^{2}&0\\0&1\\\end{bmatrix}}.$

The group $C_{3}$ may also be faithfully represented on $\mathbb {R} ^{2}$ by $\tau$ given by:

$\tau \left(1\right)={\begin{bmatrix}1&0\\0&1\\\end{bmatrix}}\qquad \tau \left(u\right)={\begin{bmatrix}a&-b\\b&a\\\end{bmatrix}}\qquad \tau \left(u^{2}\right)={\begin{bmatrix}a&b\\-b&a\\\end{bmatrix}}$

where

$a={\text{Re}}(u)=-{\tfrac {1}{2}},\qquad b={\text{Im}}(u)={\tfrac {\sqrt {3}}{2}}.$

A possible representation on $\mathbb {R} ^{3}$ is given by the set of cyclic permutation matrices v :

$\upsilon \left(1\right)={\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\\\end{bmatrix}}\qquad \upsilon \left(u\right)={\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\\\end{bmatrix}}\qquad \upsilon \left(u^{2}\right)={\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\\\end{bmatrix}}.$

Another example:

Let V be the space of homogeneous degree-3 polynomials over the complex numbers in variables $x_{1},x_{2},x_{3}.$

Then $S_{3}$ acts on V by permutation of the three variables.

For instance, $(12)$ sends $x_{1}^{3}$ to $x_{2}^{3}$ .

## Reducibility

A subspace *W* of *V* that is invariant under the group action is called a *subrepresentation*. If *V* has exactly two subrepresentations, namely the zero-dimensional subspace and *V* itself, then the representation is said to be **irreducible**; if it has a proper subrepresentation of nonzero dimension, the representation is said to be **reducible**. The representation of dimension zero is considered to be neither reducible nor irreducible, just as the number 1 is considered to be neither composite nor prime.

Under the assumption that the characteristic of the field *K* does not divide the size of the group, representations of finite groups can be decomposed into a direct sum of irreducible subrepresentations (see Maschke's theorem). This holds in particular for any representation of a finite group over the complex numbers, since the characteristic of the complex numbers is zero, which never divides the size of a group.

In the example above, the first two representations given (ρ and σ) are both decomposable into two 1-dimensional subrepresentations (given by span{(1,0)} and span{(0,1)}), while the third representation (τ) is irreducible.

## Generalizations

### Set-theoretical representations

A *set-theoretic representation* (also known as a group action or *permutation representation*) of a group *G* on a set *X* is given by a function ρ : *G* → *X**X*, the set of functions from *X* to *X*, such that for all *g*1, *g*2 in *G* and all *x* in *X*:

$\rho (1)[x]=x$

$\rho (g_{1}g_{2})[x]=\rho (g_{1})[\rho (g_{2})[x]],$

where 1 is the identity element of *G*. This condition and the axioms for a group imply that ρ(*g*) is a bijection (or permutation) for all *g* in *G*. Thus we may equivalently define a permutation representation to be a group homomorphism from G to the symmetric group S*X* of *X*.

For more information on this topic see the article on group action.

### Representations in other categories

Every group *G* can be viewed as a category with a single object; morphisms in this category are just the elements of *G*. Given an arbitrary category *C*, a *representation* of *G* in *C* is a functor from *G* to *C*. Such a functor selects an object *X* in *C* and a group homomorphism from *G* to Aut(*X*), the automorphism group of *X*.

In the case where *C* is **Vect***K*, the category of vector spaces over a field *K*, this definition is equivalent to a linear representation. Likewise, a set-theoretic representation is just a representation of *G* in the category of sets.

When *C* is **Ab**, the category of abelian groups, the objects obtained are called *G*-modules.

For another example consider the category of topological spaces, **Top**. Representations in **Top** are homomorphisms from *G* to the homeomorphism group of a topological space *X*.

Two types of representations closely related to linear representations are:

- projective representations: in the category of projective spaces. These can be described as "linear representations up to scalar transformations".
- affine representations: in the category of affine spaces. For example, the Euclidean group acts affinely upon Euclidean space.

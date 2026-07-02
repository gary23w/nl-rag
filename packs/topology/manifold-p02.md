---
title: "Manifold (part 2/2)"
source: https://en.wikipedia.org/wiki/Manifold
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
part: 2/2
---

## Maps of manifolds

Just as there are various types of manifolds, there are various types of maps of manifolds. In addition to continuous functions and smooth functions generally, there are maps with special properties. In geometric topology a basic type are embeddings, of which knot theory is a central example, and generalizations such as immersions, submersions, covering spaces, and ramified covering spaces. Basic results include the Whitney embedding theorem and Whitney immersion theorem.

In Riemannian geometry, one may ask for maps to preserve the Riemannian metric, leading to notions of isometric embeddings, isometric immersions, and Riemannian submersions; a basic result is the Nash embedding theorem.

### Scalar-valued functions

A basic example of maps between manifolds are scalar-valued functions on a manifold, $f\colon M\to \mathbb {R}$ or $f\colon M\to \mathbb {C} ,$

sometimes called regular functions or functionals, by analogy with algebraic geometry or linear algebra. These are of interest both in their own right, and to study the underlying manifold.

In geometric topology, most commonly studied are Morse functions, which yield handlebody decompositions, while in mathematical analysis, one often studies solution to partial differential equations, an important example of which is harmonic analysis, where one studies harmonic functions: the kernel of the Laplace operator. This leads to such functions as the spherical harmonics, and to heat kernel methods of studying manifolds, such as hearing the shape of a drum and some proofs of the Atiyah–Singer index theorem.


## Generalizations of manifolds

**Infinite dimensional manifolds**

The definition of a manifold can be generalized by dropping the requirement of finite dimensionality. Thus an infinite dimensional manifold is a topological space locally homeomorphic to a

topological vector space

over the reals. This omits the point-set axioms, allowing higher cardinalities and

non-Hausdorff manifolds

; and it omits finite dimension, allowing structures such as

Hilbert manifolds

to be modeled on

Hilbert spaces

,

Banach manifolds

to be modeled on

Banach spaces

, and

Fréchet manifolds

to be modeled on

Fréchet spaces

. Usually one relaxes one or the other condition: manifolds with the point-set axioms are studied in

general topology

, while infinite-dimensional manifolds are studied in

functional analysis

.

**Orbifolds**

An

orbifold

is a generalization of manifold allowing for certain kinds of "

singularities

" in the topology. Roughly speaking, it is a space which locally looks like the quotients of some simple space (

e.g.

Euclidean space) by the

actions

of various

finite groups

. The singularities correspond to fixed points of the group actions, and the actions must be compatible in a certain sense.

**Algebraic varieties and schemes**

Non-singular

algebraic varieties over the real or complex numbers are manifolds. One generalizes this first by allowing singularities, secondly by allowing different fields, and thirdly by emulating the patching construction of manifolds: just as a manifold is glued together from open subsets of Euclidean space, an

algebraic variety

is glued together from affine algebraic varieties, which are zero sets of polynomials over algebraically closed fields.

Schemes

are likewise glued together from affine schemes, which are a generalization of algebraic varieties. Both are related to manifolds, but are constructed algebraically using

sheaves

instead of atlases.

Because of

singular points

, a variety is in general not a manifold, though linguistically the French

variété

, German

Mannigfaltigkeit

and English

manifold

are largely

synonymous

. In French an algebraic variety is called

une

variété algébrique

(an

algebraic variety

), while a smooth manifold is called

une

variété différentielle

(a

differential variety

).

**Stratified space**

A "stratified space" is a space that can be divided into pieces ("strata"), with each stratum a manifold, with the strata fitting together in prescribed ways (formally, a

filtration

by closed subsets).

There are various technical definitions, notably a Whitney stratified space (see

Whitney conditions

) for smooth manifolds and a

topologically stratified space

for topological manifolds. Basic examples include

manifold with boundary

(top dimensional manifold and codimension 1 boundary) and manifolds with corners (top dimensional manifold, codimension 1 boundary, codimension 2 corners). Whitney stratified spaces are a broad class of spaces, including algebraic varieties, analytic varieties,

semialgebraic sets

, and

subanalytic sets

.

**CW-complexes**

A

CW complex

is a topological space formed by gluing disks of different dimensionality together. In general the resulting space is singular, hence not a manifold. However, they are of central interest in algebraic topology, especially in

homotopy theory

.

**Homology manifolds**

A

homology manifold

is a space that behaves like a manifold from the point of view of homology theory. These are not all manifolds, but (in high dimension) can be analyzed by surgery theory similarly to manifolds, and failure to be a manifold is a local obstruction, as in surgery theory.

**Differential spaces**

Let

M

be a nonempty set. Suppose that some family of real functions on

M

was chosen. Denote it by

$C\subseteq \mathbb {R} ^{M}$

. It is an algebra with respect to the pointwise addition and multiplication. Let

M

be equipped with the topology induced by

C

. Suppose also that the following conditions hold. First: for every

$H\in C^{\infty }\left(\mathbb {R} ^{n}\right)$

, where

$n\in \mathbb {N}$

, and arbitrary

$f_{1},\dots ,f_{n}\in C$

, the composition

$H\circ \left(f_{1},\dots ,f_{n}\right)\in C$

. Second: every function, which in every point of

M

locally coincides with some function from

C

, also belongs to

C

. A pair

$(M,C)$

for which the above conditions hold, is called a Sikorski differential space.

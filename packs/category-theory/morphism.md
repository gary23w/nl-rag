---
title: "Morphism"
source: https://en.wikipedia.org/wiki/Morphism
domain: category-theory
license: CC-BY-SA-4.0
tags: category theory, functor, monad, morphism, natural transformation
fetched: 2026-07-02
---

# Morphism

In mathematics, a **morphism** is a concept of category theory that generalizes structure-preserving maps such as homomorphism between algebraic structures, functions from a set to another set, and continuous functions between topological spaces. Although many examples of morphisms are structure-preserving maps, morphisms need not be maps, but they can be composed in a way that is similar to function composition.

Morphisms and objects are constituents of a category. Morphisms, also called *maps* or *arrows*, relate two objects called the *source* and the *target* of the morphism. There is a partial operation, called *composition*, on the morphisms of a category that is defined if the target of the first morphism equals the source of the second morphism. The composition of morphisms behaves like function composition (associativity of composition when it is defined, and existence of an identity morphism for every object), and the outcome of the composition is a morphism.

Morphisms and categories recur in much of contemporary mathematics. Originally, they were introduced for homological algebra and algebraic topology. They belong to the foundational tools of Grothendieck's scheme theory, a generalization of algebraic geometry that applies also to algebraic number theory.

## Definition

A category ${\mathcal {C}}$ consists of two classes, one of *objects* and the other of *morphisms*. There are two objects that are associated to every morphism, the *source* and the *target*. A morphism f from X to Y is a morphism with source X and target Y ; it is commonly written as $f:X\to Y$ or $X\xrightarrow {f} Y$ , the latter form being better suited for commutative diagrams.

For many common categories, an object is a set (often with some additional structure) and a morphism is a function from an object to another object. Therefore, the source and the target of a morphism are often called *domain* and *codomain* respectively.

Morphisms are equipped with a partial binary operation, called *composition* (*partial* because the composition is not necessarily defined over every pair of morphisms of a category). The composition of two morphisms f and g is defined precisely when the target of f is the source of g , and is denoted $g\circ f$ (or sometimes simply $gf$ ). The outcome of the composition is a morphism such that the source of $g\circ f$ is the source of f , and the target of $g\circ f$ is the target of g . The composition satisfies two axioms:

**Identity**

For every object

X

, there exists a morphism

$\mathrm {id} _{X}:X\to X$

called the

identity morphism

on

X

, such that for every morphism

$f:A\to B$

we have

$\mathrm {id} _{B}\circ f=f=f\circ \mathrm {id} _{A}$

.

**Associativity**

$h\circ (g\circ f)=(h\circ g)\circ f$

whenever all the compositions are defined, i.e. when the target of

f

is the source of

g

, and the target of

g

is the source of

h

.

For a concrete category (a category in which the objects are sets, possibly with additional structure, and the morphisms are structure-preserving functions), the identity morphism is just the identity function, and composition is just ordinary composition of functions.

The composition of morphisms is often represented by a commutative diagram. For example,

The collection of all morphisms from X to Y is denoted $\mathrm {Hom} _{\mathcal {C}}(X,Y)$ or simply $\mathrm {Hom} (X,Y)$ and called the **hom-set** between X and Y . Some authors write $\mathrm {Mor} _{\mathcal {C}}(X,Y)$ , $\mathrm {Mor} (X,Y)$ or ${\mathcal {C}}(X,Y)$ . The term hom-set is something of a misnomer, as the collection of morphisms is not required to be a set; a category where $\mathrm {Hom} (X,Y)$ is a set for all objects X and Y is called locally small. Because hom-sets may not be sets, some people prefer to use the term "hom-class".

The domain and codomain are in fact part of the information determining a morphism. For example, in the category of sets, where morphisms are functions, two functions may be identical as sets of ordered pairs, while having different codomains. The two functions are distinct from the viewpoint of category theory. Many authors require that the hom-classes $\mathrm {Hom} (X,Y)$ be disjoint. In practice, this is not a problem because if this disjointness does not hold, it can be assured by appending the domain and codomain to the morphisms (say, as the second and third components of an ordered triple).

## Some special morphisms

### Monomorphisms and epimorphisms

A morphism $f:X\to Y$ is called a monomorphism if $f\circ g_{1}=f\circ g_{2}$ implies $g_{1}=g_{2}$ for all morphisms $g_{1},g_{2}:Z\to X$ . A monomorphism can be called a *mono* for short, and we can use *monic* as an adjective. A morphism f has a **left inverse** or is a **split monomorphism** if there is a morphism $g:Y\to X$ such that $g\circ f=\mathrm {id} _{X}$ . Thus $f\circ g:Y\to Y$ is idempotent; that is, $(f\circ g)^{2}=f\circ (g\circ f)\circ g=f\circ g$ . The left inverse g is also called a **retraction** of f .

Morphisms with left inverses are always monomorphisms ( $f_{l}^{-1}\circ f\circ g_{1}=f_{l}^{-1}\circ f\circ g_{2}$ implies $g_{1}=g_{2}$ , where $f_{l}^{-1}$ is the left inverse of f ), but the converse is not true in general; a monomorphism may fail to have a left inverse. In concrete categories, where morphisms are functions, a morphism that has a left inverse is injective, and a morphism that is injective is a monomorphism. In concrete categories, monomorphisms are often, but not always, injective; thus the condition of being an injection is stronger than that of being a monomorphism, but weaker than that of being a split monomorphism.

Dually to monomorphisms, a morphism $f:X\to Y$ is called an epimorphism if $g_{1}\circ f=g_{2}\circ f$ implies $g_{1}=g_{2}$ for all morphisms $g_{1},g_{2}:Y\to Z$ . An epimorphism can be called an *epi* for short, and we can use *epic* as an adjective. A morphism f has a **right inverse** or is a **split epimorphism** if there is a morphism $g:Y\to X$ such that $f\circ g=\mathrm {id} _{Y}$ . The right inverse g is also called a **section** of f . Morphisms having a right inverse are always epimorphisms ( $g_{1}\circ f\circ f_{r}^{-1}=g_{2}\circ f\circ f_{r}^{-1}$ implies $g_{1}=g_{2}$ where $f_{r}^{-1}$ is the right inverse of f ), but the converse is not true in general, as an epimorphism may fail to have a right inverse.

If a monomorphism f splits with left inverse g , then g is a split epimorphism with right inverse f . In concrete categories, a function that has a right inverse is surjective. Thus, in concrete categories, epimorphisms are often, but not always, surjective. The condition of being a surjection is stronger than that of being an epimorphism, but weaker than that of being a split epimorphism. In the category of sets, the statement that every surjection has a section is equivalent to the axiom of choice.

A morphism that is both an epimorphism and a monomorphism is called a **bimorphism**.

For example, in the category of vector spaces over a fixed field, injective morphisms, monomorphisms and split monomorphisms are the same, as well as surjective morphisms, epimorphisms and split epimorphisms.

In the category of commutative rings, monomorphisms and injective morphisms are the same, while the injection from ⁠ $\mathbb {Z}$ ⁠ into ⁠ $\mathbb {Q}$ ⁠ is an epimorphism that is not surjective; it is neither a split epimorphism nor a split monomorphism. (See Homomorphism#Special homomorphisms for more details and proofs.)

### Isomorphisms

A morphism $f:X\to Y$ is called an isomorphism if there exists a morphism $g:Y\to X$ such that $f\circ g=\mathrm {id} _{Y}$ and $g\circ f=\mathrm {id} _{X}$ . If a morphism has both left-inverse and right-inverse, then the two inverses are equal, so f is an isomorphism, and g is called simply the **inverse** of f . Inverse morphisms, if they exist, are unique. The inverse g is also an isomorphism, with inverse f . Two objects with an isomorphism between them are said to be isomorphic or equivalent.

While every isomorphism is a bimorphism, a bimorphism is not necessarily an isomorphism. For example, in the category of commutative rings the inclusion $\mathbb {Z} \to \mathbb {Q}$ is a bimorphism that is not an isomorphism. However, any morphism that is both an epimorphism and a *split* monomorphism, or both a monomorphism and a *split* epimorphism, must be an isomorphism. A category, such as a **Set**, in which every bimorphism is an isomorphism is known as a **balanced category**.

### Endomorphisms and automorphisms

A morphism $f:X\to X$ (that is, a morphism with identical source and target) is an endomorphism of X . A **split endomorphism** is an idempotent endomorphism f if f admits a decomposition $f=h\circ g$ with $g\circ h=\mathrm {id}$ . In particular, the Karoubi envelope of a category splits every idempotent morphism.

An automorphism is a morphism that is both an endomorphism and an isomorphism. In every category, the automorphisms of an object always form a group, called the automorphism group of the object.

## Examples

- For algebraic structures commonly considered in algebra, such as groups, rings, modules, etc., the morphisms are usually the homomorphisms, and the notions of isomorphism, automorphism, endomorphism, epimorphism, and monomorphism are the same as the above defined ones. However, in the case of rings, "epimorphism" is often considered as a synonym of "surjection", although there are ring epimorphisms that are not surjective (e.g., when embedding the integers in the rational numbers).
- In the category of topological spaces, often denoted $\mathbf {Top}$ , the morphisms are the continuous functions and isomorphisms are called homeomorphisms. There are continuous bijections (that is, isomorphisms of sets) that are not homeomorphisms.
- In the category of smooth manifolds, the morphisms are the smooth functions and isomorphisms are called diffeomorphisms.
- In the category of small categories, the morphisms are functors.
- In a functor category, the morphisms are natural transformations.

For more examples, see Category theory.

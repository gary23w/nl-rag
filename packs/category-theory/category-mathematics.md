---
title: "Category (mathematics)"
source: https://en.wikipedia.org/wiki/Category_(mathematics)
domain: category-theory
license: CC-BY-SA-4.0
tags: category theory, functor, monad, morphism, natural transformation
fetched: 2026-07-02
---

# Category (mathematics)

In mathematics, a **category** (sometimes called an **abstract category** to distinguish it from a concrete category) is a collection of "objects" that are linked by "arrows". A category has two basic properties: the ability to compose the arrows associatively and the existence of an identity arrow for each object. A simple example is the category of sets, whose objects are sets and whose arrows are functions.

Category theory is a branch of mathematics that seeks to generalize all of mathematics in terms of categories, independent of what their objects and arrows represent. Virtually every branch of modern mathematics can be described in terms of categories, and doing so often reveals deep insights and similarities between seemingly different areas of mathematics. As such, category theory provides an alternative foundation for mathematics to set theory and other proposed axiomatic foundations. In general, the objects and arrows may be abstract entities of any kind, and the notion of category provides a fundamental and abstract way to describe mathematical entities and their relationships.

In addition to formalizing mathematics, category theory is also used to formalize many other systems in computer science, such as the semantics of programming languages.

Two categories are the same if they have the same collection of objects, the same collection of arrows, and the same associative method of composing any pair of arrows. Two *different* categories may also be considered "equivalent" for purposes of category theory, even if they do not have precisely the same structure. A mapping between two categories compatible with their respective structures is called a functor.

Well-known categories are denoted by a short capitalized word or abbreviation in bold or italics: examples include **Set**, the category of sets and set functions; **Ring**, the category of rings and ring homomorphisms; and **Top**, the category of topological spaces and continuous maps. All of the preceding categories have the identity map as identity arrows and composition as the associative operation on arrows. Any monoid can be understood as a special sort of category (with a single object whose self-morphisms are represented by the elements of the monoid), and so can any preorder.

The classic and still much used text on category theory is *Categories for the Working Mathematician* by Saunders Mac Lane. Other references are given in the References below. The basic definitions in this article are contained within the first few chapters of any of these books.

## Definition

|   | Total | Associative | Identity | Divisible |
|---|---|---|---|---|
| Partial magma | Unneeded | Unneeded | Unneeded | Unneeded |
| Semigroupoid | Unneeded | Required | Unneeded | Unneeded |
| Small category | Unneeded | Required | Required | Unneeded |
| Groupoid | Unneeded | Required | Required | Required |
| Magma | Required | Unneeded | Unneeded | Unneeded |
| Quasigroup | Required | Unneeded | Unneeded | Required |
| Unital magma | Required | Unneeded | Required | Unneeded |
| Loop | Required | Unneeded | Required | Required |
| Semigroup | Required | Required | Unneeded | Unneeded |
| Associative quasigroup | Required | Required | Unneeded | Required |
| Monoid | Required | Required | Required | Unneeded |
| Group | Required | Required | Required | Required |

There are many equivalent definitions of a category. One commonly used definition is as follows. A **category** ${\mathcal {C}}$ consists of

- a class $\operatorname {ob} ({\mathcal {C}})$ of **objects**,
- a class $\operatorname {mor} ({\mathcal {C}})$ of **morphisms** or **arrows**,
- a **domain** or **source** class function $\operatorname {dom$ ,
- a **codomain** or **target** class function $\operatorname {cod$ ,
- for every three objects $a,b,c$ , a binary operation $\operatorname {hom} (a,b)\times \operatorname {hom} (b,c)\to \operatorname {hom} (a,c)$ called **composition of morphisms**. Here $\operatorname {hom} (a,b)$ denotes the subclass of morphisms f in $\operatorname {mor} ({\mathcal {C}})$ such that $\operatorname {dom} (f)=a$ and $\operatorname {cod} (f)=b$ . Morphisms in this subclass are written $f:a\to b$ , and the composite of $f:a\to b$ and $g:b\to c$ is often written as $g\circ f$ or $gf$ .

such that the following axioms hold:

- the *associative law*: if $f:a\to b$ , $g:b\to c$ and $h:c\to d$ then $h\circ (g\circ f)=(h\circ g)\circ f$ , and
- the *left and right unit laws*: for every object x , there exists a morphism $1_{x}:x\to x$ (some authors write $\operatorname {id} _{x}$ ) called the *identity morphism for x*, such that every morphism $f:a\to x$ satisfies $1_{x}\circ f=f$ , and every morphism $g:x\to b$ satisfies $g\circ 1_{x}=g$ .

We write $f:a\to b$ , and we say " f is a morphism from a to b ". We write $\operatorname {hom} (a,b)$ (or $\operatorname {hom} _{\mathcal {C}}(a,b)$ when there may be confusion about to which category $\operatorname {hom} (a,b)$ refers) to denote the **hom-class** of all morphisms from a to b .

Some authors write the composite of morphisms in "diagrammatic order", writing $f\,;g$ (sometimes with ⨟ ) or $fg$ instead of $g\circ f$ .

From these axioms, one can prove that there is exactly one identity morphism for every object. Often the map assigning each object its identity morphism is treated as an extra part of the structure of a category, namely a class function $i:\operatorname {ob} ({\mathcal {C}})\to \operatorname {mor} ({\mathcal {C}})$ .

Some authors use a slight variant of the definition in which each object is identified with the corresponding identity morphism. This stems from the idea that the fundamental data of categories are morphisms and not objects. In fact, categories can be defined without reference to objects at all using a partial binary operation with additional properties.

## Small and large categories

A category ${\mathcal {C}}$ is called **small** if both $\operatorname {ob} ({\mathcal {C}})$ and $\operatorname {mor} ({\mathcal {C}})$ are actually sets and not proper classes, and **large** otherwise. A **locally small category** is a category such that for all objects a and b , the hom-class $\operatorname {hom} (a,b)$ is a set, called a **homset**. Many important categories in mathematics (such as the category of sets), although not small, are at least locally small. Since, in small categories, the objects form a set, a small category can be viewed as an algebraic structure similar to a monoid but without requiring closure properties. Large categories on the other hand can be used to create "structures" of algebraic structures.

## Examples

The class of all sets (as objects) together with all functions between them (as morphisms), where the composition of morphisms is the usual function composition, forms a large category, **Set**. It is the most basic and the most commonly used category in mathematics. The category **Rel** consists of all sets (as objects) with binary relations between them (as morphisms). Abstracting from relations instead of functions yields allegories, a special class of categories.

Any class can be viewed as a category whose only morphisms are the identity morphisms. Such categories are called discrete. For any given set I , the *discrete category on I* is the small category that has the elements of I as objects and only the identity morphisms as morphisms.

Any preordered set $(P,\leq )$ forms a small category, where the objects are the members of P , the morphisms are arrows pointing from x to y when $x\leq y$ . The existence of identity morphisms and the composability of the morphisms are guaranteed by the reflexivity and the transitivity of the preorder. For any two objects, there is at most one morphism from one to the other (such a category is called thin), and if $\leq$ is in addition antisymmetric, there can be at most one morphism between any two objects. In particular, any partially ordered set and any equivalence relation can be seen as a small category. Any ordinal number can be seen as a category when viewed as an ordered set.

Any monoid (any algebraic structure with a single associative binary operation and an identity element) forms a small category with a single object x . (Here, x is any fixed set.) The morphisms from x to x are precisely the elements of the monoid, the identity morphism of x is the identity of the monoid, and the categorical composition of morphisms is given by the monoid operation. Several definitions and theorems about monoids may be generalized for categories.

Similarly any group can be seen as a category with a single object in which every morphism is *invertible*, that is, for every morphism f there is a morphism g that is both left and right inverse to f under composition. A morphism that is invertible in this sense is called an isomorphism.

A groupoid is a category in which every morphism is an isomorphism. Groupoids are generalizations of groups, group actions and equivalence relations. From the point of view of category theory, a group is just a groupoid with exactly one object. Consider a topological space X and fix a base point $x_{0}$ of X , then $\pi _{1}(X,x_{0})$ is the fundamental group of the topological space X and the base point $x_{0}$ , and as a set it has the structure of group; if one then lets the base point $x_{0}$ run over all points of X and takes the union of all $\pi _{1}(X,x_{0})$ , then the resulting set has only the structure of groupoid (called the fundamental groupoid of X ): two loops (under equivalence relation of homotopy) may not have the same base point so they cannot be multiplied with each other. In the language of category theory, this means here two morphisms may not have the same source object (or target object, because in this case for any morphism the source object and the target object are same: the base point) so they cannot compose with each other.

Any directed graph (or, more generally, a quiver) generates a small category: the objects are the vertices of the graph, and the morphisms are the paths in the graph (augmented with loops as needed) where composition of morphisms is concatenation of paths. Such a category is called the *free category* generated by the graph.

The class of all preordered sets with order-preserving functions (i.e., monotone-increasing functions) as morphisms forms a category, **Ord**. It is a concrete category, i.e. a category whose objects can be identified with sets with some type of additional structure, while the morphisms are functions that respect this structure.

The class of all groups with group homomorphisms as morphisms and function composition as the composition operation forms a large category, **Grp**. Like $\mathbf {Ord}$ , $\mathbf {Grp}$ is a concrete category. The category **Ab**, consisting of all abelian groups and their group homomorphisms, is a full subcategory of $\mathbf {Grp}$ , and the prototype of an abelian category.

The class of all graphs forms another concrete category, where morphisms are graph homomorphisms (i.e., mappings between graphs which send vertices to vertices and edges to edges in a way that preserves all adjacency and incidence relations).

Examples of concrete categories are given by the following table.

| Category | Objects | Morphisms |
|---|---|---|
| **Set** | sets | functions |
| **Ord** | preordered sets | monotone-increasing functions |
| **Mon** | monoids | monoid homomorphisms |
| **Grp** | groups | group homomorphisms |
| **Grph** | graphs | graph homomorphisms |
| **Ring** | rings | ring homomorphisms |
| **Field** | fields | field homomorphisms |
| ***R*-Mod** | *R*-modules, where R is a ring | *R*-module homomorphisms |
| **Vect***K* | vector spaces over the field K | *K*-linear maps |
| **Rep***K*(*G*) | representations of a group *G* over a field *K* | equivariant maps |
| **Met** | metric spaces | short maps |
| **Meas** | measure spaces | measurable functions |
| **Stoch** | measure spaces | Markov kernels |
| **Top** | topological spaces | continuous functions |
| **Man***p* | smooth manifolds | p -times continuously differentiable maps |
| **Sch** | schemes | morphisms of schemes |

Fiber bundles with bundle maps between them form a concrete category.

The category **Cat** consists of all small categories, with functors between them as morphisms. In turn, a functor category has as objects functors between two fixed categories and as morphisms natural transformations between them.

## Construction of new categories

Any category ${\mathcal {C}}$ can itself be considered as a new category in a different way: the objects are the same as those in the original category but the arrows are those of the original category reversed. This is called the *dual* or *opposite category* and is denoted ${\mathcal {C}}^{\mathrm {op} }$ .

If ${\mathcal {C}}$ and ${\mathcal {D}}$ are categories, one can form the *product category* ${\mathcal {C}}\times {\mathcal {D}}$ : the objects are pairs consisting of one object from ${\mathcal {C}}$ and one from ${\mathcal {D}}$ , and the morphisms are also pairs, consisting of one morphism in ${\mathcal {C}}$ and one in ${\mathcal {D}}$ . Such pairs can be composed componentwise.

By identifying a collection of morphisms in ${\mathcal {C}}$ via a suitable equivalence relation $\sim$ , one can construct the *quotient category* ${\mathcal {C}}/\sim$ .

For a fixed object X of ${\mathcal {C}}$ , the *overcategory* or *slice category* ${\mathcal {C}}/X$ consists of pairs $(A,f)$ of an object A of ${\mathcal {C}}$ and a morphism $f:A\to X$ , with morphisms between $(A,f)$ and $(A',f')$ given by a morphism $g:A\to B$ in ${\mathcal {C}}$ compatible with the morphisms to X , i.e. $f'\circ g=f$ . The dual notion is that of an *undercategory* or *coslice category*, and both are special cases of a construction called *comma category*.

Given a class W of morphisms in ${\mathcal {C}}$ , the *localization* ${\mathcal {C}}[W^{-1}]$ turns the morphisms from W into isomorphisms (see below).

## Types of morphisms

A morphism $f:a\to b$ is called

- a *monomorphism* (or *monic*) if it is left-cancellable, i.e. $fg_{1}=fg_{2}$ implies $g_{1}=g_{2}$ for all morphisms $g_{1},g_{2}:x\to a$ .
- an *epimorphism* (or *epic*) if it is right-cancellable, i.e. $g_{1}f=g_{2}f$ implies $g_{1}=g_{2}$ for all morphisms $g_{1},g_{2}:b\to x$ .
- a *bimorphism* if it is both a monomorphism and an epimorphism.
- a *retraction* if it has a right inverse, i.e. if there exists a morphism $g:b\to a$ with $fg=1_{b}$ .
- a *section* if it has a left inverse, i.e. if there exists a morphism $g:b\to a$ with $gf=1_{a}$ .
- an *isomorphism* if it has an inverse, i.e. if there exists a morphism $g:b\to a$ with $fg=1_{b}$ and $gf=1_{a}$ .
- an *endomorphism* if $a=b$ . The class of endomorphisms of a is denoted $\mathrm {end} (a)$ . For locally small categories, $\mathrm {end} (a)$ is a *set* and forms a monoid under morphism composition.
- an *automorphism* if f is both an endomorphism and an isomorphism. The class of automorphisms of a is denoted $\mathrm {aut} (a)$ . For locally small categories, it forms a group under morphism composition called the *automorphism group* of a .

Every retraction is an epimorphism. Every section is a monomorphism. The following three statements are equivalent:

- f is a monomorphism and a retraction;
- f is an epimorphism and a section;
- f is an isomorphism.

Relations among morphisms (such as $fg=h$ ) can most conveniently be represented with commutative diagrams, where the objects are represented as points and the morphisms as arrows.

## Types of categories

- In many categories, e.g. **Ab** or **Vect***K*, the hom-sets $\operatorname {hom} (a,b)$ are not just sets but actually abelian groups, and the composition of morphisms is compatible with these group structures; i.e. is bilinear. Such a category is called preadditive. If, furthermore, the category has all finite products and coproducts, it is called an additive category. If all morphisms have a kernel and a cokernel, and all epimorphisms are cokernels and all monomorphisms are kernels, then we speak of an abelian category. A typical example of an abelian category is the category of abelian groups.
- The idea of hom-sets possessing some additional structure beyond being a set can be formalized in the concept of an enriched category.
- A category is called complete if all small limits exist in it. The categories of sets, abelian groups and topological spaces are complete.
- A category is called cartesian closed if it has finite direct products and a morphism defined on a finite product can always be represented by a morphism defined on just one of the factors. Examples include **Set** and $\mathbf {CPO}$ , the category of complete partial orders with Scott-continuous functions.
- A topos is a certain type of cartesian closed category in which all of mathematics can be formulated (just like classically all of mathematics is formulated in the category of sets). A topos can also be used to represent a logical theory.

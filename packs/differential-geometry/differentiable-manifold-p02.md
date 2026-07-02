---
title: "Differentiable manifold (part 2/2)"
source: https://en.wikipedia.org/wiki/Differentiable_manifold
domain: differential-geometry
license: CC-BY-SA-4.0
tags: differential geometry, smooth manifold, riemannian manifold, curvature tensor
fetched: 2026-07-02
part: 2/2
---

## Alternative definitions

### Pseudogroups

The notion of a pseudogroup provides a flexible generalization of atlases in order to allow a variety of different structures to be defined on manifolds in a uniform way. A *pseudogroup* consists of a topological space *S* and a collection Γ consisting of homeomorphisms from open subsets of *S* to other open subsets of *S* such that

1. If *f* ∈ Γ, and *U* is an open subset of the domain of *f*, then the restriction *f*|*U* is also in Γ.
2. If *f* is a homeomorphism from a union of open subsets of *S*, $\cup _{i}\,U_{i}$ , to an open subset of *S*, then *f* ∈ Γ provided $f|_{U_{i}}\in \Gamma$ for every *i*.
3. For every open *U* ⊂ *S*, the identity transformation of *U* is in Γ.
4. If *f* ∈ Γ, then *f*−1 ∈ Γ.
5. The composition of two elements of Γ is in Γ.

These last three conditions are analogous to the definition of a group. Note that Γ need not be a group, however, since the functions are not globally defined on *S*. For example, the collection of all local *Ck* diffeomorphisms on **R***n* form a pseudogroup. All biholomorphisms between open sets in **C***n* form a pseudogroup. More examples include: orientation preserving maps of **R***n*, symplectomorphisms, Möbius transformations, affine transformations, and so on. Thus, a wide variety of function classes determine pseudogroups.

An atlas (*Ui*, *φ**i*) of homeomorphisms *φ**i* from *Ui* ⊂ *M* to open subsets of a topological space *S* is said to be *compatible* with a pseudogroup Γ provided that the transition functions *φ**j* ∘ *φ**i*−1 : *φ**i*(*Ui* ∩ *Uj*) → *φ**j*(*Ui* ∩ *Uj*) are all in Γ.

A differentiable manifold is then an atlas compatible with the pseudogroup of *C**k* functions on **R***n*. A complex manifold is an atlas compatible with the biholomorphic functions on open sets in **C***n*. And so forth. Thus, pseudogroups provide a single framework in which to describe many structures on manifolds of importance to differential geometry and topology.

### Structure sheaf

Sometimes, it can be useful to use an alternative approach to endow a manifold with a *Ck*-structure. Here *k* = 1, 2, ..., ∞, or ω for real analytic manifolds. Instead of considering coordinate charts, it is possible to start with functions defined on the manifold itself. The structure sheaf of *M*, denoted **C***k*, is a sort of functor that defines, for each open set *U* ⊂ *M*, an algebra **C***k*(*U*) of continuous functions *U* → **R**. A structure sheaf **C***k* is said to give *M* the structure of a *C**k* manifold of dimension *n* provided that, for any *p* ∈ *M*, there exists a neighborhood *U* of *p* and *n* functions *x*1, ..., *x**n* ∈ **C***k*(*U*) such that the map *f* = (*x*1, ..., *xn*) : *U* → **R***n* is a homeomorphism onto an open set in **R***n*, and such that **C***k*|*U* is the pullback of the sheaf of *k*-times continuously differentiable functions on **R***n*.

In particular, this latter condition means that any function *h* in **C***k*(*V*), for *V*, can be written uniquely as *h*(*x*) = *H*(*x*1(*x*), ..., *x**n*(*x*)), where *H* is a *k*-times differentiable function on *f*(*V*) (an open set in **R***n*). Thus, the sheaf-theoretic viewpoint is that the functions on a differentiable manifold can be expressed in local coordinates as differentiable functions on **R***n*, and *a fortiori* this is sufficient to characterize the differential structure on the manifold.

#### Sheaves of local rings

A similar, but more technical, approach to defining differentiable manifolds can be formulated using the notion of a ringed space. This approach is strongly influenced by the theory of schemes in algebraic geometry, but uses local rings of the germs of differentiable functions. It is especially popular in the context of *complex* manifolds.

We begin by describing the basic structure sheaf on **R***n*. If *U* is an open set in **R***n*, let

O

(

U

) =

C

k

(

U

,

R

)

consist of all real-valued *k*-times continuously differentiable functions on *U*. As *U* varies, this determines a sheaf of rings on **R**n. The stalk **O***p* for *p* ∈ **R***n* consists of germs of functions near *p*, and is an algebra over **R**. In particular, this is a local ring whose unique maximal ideal consists of those functions that vanish at *p*. The pair (**R***n*, **O**) is an example of a locally ringed space: it is a topological space equipped with a sheaf whose stalks are each local rings.

A differentiable manifold (of class *Ck*) consists of a pair (*M*, **O***M*) where *M* is a second countable Hausdorff space, and **O***M* is a sheaf of local **R**-algebras defined on *M*, such that the locally ringed space (*M*, **O***M*) is locally isomorphic to (**R***n*, **O**). In this way, differentiable manifolds can be thought of as schemes modeled on **R***n*. This means that for each point *p* ∈ *M*, there is a neighborhood *U* of *p*, and a pair of functions (*f*, *f*#), where

1. *f* : *U* → *f*(*U*) ⊂ **R***n* is a homeomorphism onto an open set in **R***n*.
2. *f*#: **O**|*f*(*U*) → *f*∗ (**O***M*|*U*) is an isomorphism of sheaves.
3. The localization of *f*# is an isomorphism of local rings

f

#

f

(

p

)

:

O

f

(

p

)

→

O

M

,

p

.

There are a number of important motivations for studying differentiable manifolds within this abstract framework. First, there is no *a priori* reason that the model space needs to be **R**n. For example, (in particular in algebraic geometry), one could take this to be the space of complex numbers **C***n* equipped with the sheaf of holomorphic functions (thus arriving at the spaces of complex analytic geometry), or the sheaf of polynomials (thus arriving at the spaces of interest in complex *algebraic* geometry). In broader terms, this concept can be adapted for any suitable notion of a scheme (see topos theory). Second, coordinates are no longer explicitly necessary to the construction. The analog of a coordinate system is the pair (*f*, *f*#), but these merely quantify the idea of *local isomorphism* rather than being central to the discussion (as in the case of charts and atlases). Third, the sheaf **O***M* is not manifestly a sheaf of functions at all. Rather, it emerges as a sheaf of functions as a *consequence* of the construction (via the quotients of local rings by their maximal ideals). Hence, it is a more primitive definition of the structure (see synthetic differential geometry).

A final advantage of this approach is that it allows for natural direct descriptions of many of the fundamental objects of study to differential geometry and topology.

- The cotangent space at a point is *Ip*/*Ip*2, where *Ip* is the maximal ideal of the stalk **O***M*,*p*.
- In general, the entire cotangent bundle can be obtained by a related technique (see cotangent bundle for details).
- Taylor series (and jets) can be approached in a coordinate-independent manner using the *I**p*-adic filtration on **O***M*,*p*.
- The tangent bundle (or more precisely its sheaf of sections) can be identified with the sheaf of morphisms of **O***M* into the ring of dual numbers.


## Generalizations

The category of smooth manifolds with smooth maps lacks certain desirable properties, and people have tried to generalize smooth manifolds in order to rectify this. Diffeological spaces use a different notion of chart known as a "plot". Frölicher spaces and orbifolds are other attempts.

A rectifiable set generalizes the idea of a piece-wise smooth or rectifiable curve to higher dimensions; however, rectifiable sets are not in general manifolds.

Banach manifolds and Fréchet manifolds, in particular manifolds of mappings are infinite dimensional differentiable manifolds.

### Non-commutative geometry

For a *Ck* manifold *M*, the set of real-valued *Ck* functions on the manifold forms an algebra under pointwise addition and multiplication, called the *algebra of scalar fields* or simply the *algebra of scalars*. This algebra has the constant function 1 as the multiplicative identity, and is a differentiable analog of the ring of regular functions in algebraic geometry.

It is possible to reconstruct a manifold from its algebra of scalars, first as a set, but also as a topological space – this is an application of the Banach–Stone theorem, and is more formally known as the spectrum of a C*-algebra. First, there is a one-to-one correspondence between the points of *M* and the algebra homomorphisms *φ*: *Ck*(*M*) → **R**, as such a homomorphism *φ* corresponds to a codimension one ideal in *Ck*(*M*) (namely the kernel of *φ*), which is necessarily a maximal ideal. On the converse, every maximal ideal in this algebra is an ideal of functions vanishing at a single point, which demonstrates that MSpec (the Max Spec) of *Ck*(*M*) recovers *M* as a point set, though in fact it recovers *M* as a topological space.

One can define various geometric structures algebraically in terms of the algebra of scalars, and these definitions often generalize to algebraic geometry (interpreting rings geometrically) and operator theory (interpreting Banach spaces geometrically). For example, the tangent bundle to *M* can be defined as the derivations of the algebra of smooth functions on *M*.

This "algebraization" of a manifold (replacing a geometric object with an algebra) leads to the notion of a C*-algebra – a commutative C*-algebra being precisely the ring of scalars of a manifold, by Banach–Stone, and allows one to consider *non*commutative C*-algebras as non-commutative generalizations of manifolds. This is the basis of the field of noncommutative geometry.

---
title: "Stalk (sheaf)"
source: https://en.wikipedia.org/wiki/Stalk_(sheaf)
domain: sheaf-theory
license: CC-BY-SA-4.0
tags: sheaf theory, sheaf cohomology, grothendieck topology, ringed space
fetched: 2026-07-02
---

# Stalk (sheaf)

In mathematics, the **stalk** of a sheaf is a mathematical construction capturing the behaviour of a sheaf around a given point.

## Motivation and definition

Sheaves are defined on open sets, but the underlying topological space *X* consists of points. It is reasonable to attempt to isolate the behavior of a sheaf at a single fixed point *x* of *X*. Conceptually speaking, we do this by looking at small neighborhoods of the point. If we look at a sufficiently small neighborhood of *x*, the behavior of the sheaf ${\mathcal {F}}$ on that small neighborhood should be the same as the behavior of ${\mathcal {F}}$ at that point. Of course, no single neighborhood will be small enough, so we will have to take a limit of some sort.

The precise definition is as follows: the stalk of ${\mathcal {F}}$ at x , usually denoted ${\mathcal {F}}_{x}$ , is:

${\mathcal {F}}_{x}:=\varinjlim _{U\ni x}{\mathcal {F}}(U).$

Here the direct limit is indexed over all the open sets containing *x*, with order relation induced by reverse inclusion ( $U\leq V$ , if $U\supseteq V$ ). By definition (or universal property) of the direct limit, an element of the stalk is a germ of sections, an equivalence class of elements $f_{U}\in {\mathcal {F}}(U)$ , where two such sections $f_{U}$ and $f_{V}$ are considered equivalent if the restrictions of the two sections coincide on some neighborhood of *x*.

### Alternative definition

There is another approach to defining a stalk that is useful in some contexts. Choose a point x of X , and let i be the inclusion of the one point space $\{x\}$ into X . Then the stalk ${\mathcal {F}}_{x}$ is the same as the inverse image sheaf $i^{-1}{\mathcal {F}}$ . Notice that the only open sets of the one point space $\{x\}$ are $\{x\}$ and $\emptyset$ , and there is no data over the empty set. Over $\{x\}$ , however, we get:

$i^{-1}{\mathcal {F}}(\{x\})=\varinjlim _{U\supseteq \{x\}}{\mathcal {F}}(U)=\varinjlim _{U\ni x}{\mathcal {F}}(U)={\mathcal {F}}_{x}.$

## Remarks

For some categories **C** the direct limit used to define the stalk may not exist. However, it exists for most categories that occur in practice, such as the category of sets or most categories of algebraic objects such as abelian groups or rings, which are namely cocomplete.

There is a natural morphism ${\mathcal {F}}(U)\to {\mathcal {F}}_{x}$ for any open set U containing *x*: it takes a section s in ${\mathcal {F}}(U)$ to its *germ*, that is, its equivalence class in the direct limit. This is a generalization of the usual concept of a germ, which can be recovered by looking at the stalks of the sheaf of continuous functions on *X*.

## Examples

### Constant sheaves

The constant sheaf ${\underline {S}}$ associated to some set, S , (or group, ring, etc.) is a sheaf for which ${\underline {S}}_{x}=S$ for all x in X .

### Sheaves of analytic functions

For example, in the sheaf of analytic functions on an analytic manifold, a germ of a function at a point determines the function in a small neighborhood of a point. This is because the germ records the function's power series expansion, and all analytic functions are by definition locally equal to their power series. Using analytic continuation, we find that the germ at a point determines the function on any connected open set where the function can be everywhere defined. (This does not imply that all the restriction maps of this sheaf are injective!)

### Sheaves of smooth functions

In contrast, for the sheaf of smooth functions on a smooth manifold, germs contain some local information, but are not enough to reconstruct the function on any open neighborhood. For example, let $f:\mathbb {R} \to \mathbb {R}$ be a bump function that is identically one in a neighborhood of the origin and identically zero far away from the origin. On any sufficiently small neighborhood containing the origin, f is identically one, so at the origin it has the same germ as the constant function with value 1. Suppose that we want to reconstruct *f* from its germ. Even if we know in advance that *f* is a bump function, the germ does not tell us how large its bump is. From what the germ tells us, the bump could be infinitely wide, that is, *f* could equal the constant function with value 1. We cannot even reconstruct *f* on a small open neighborhood *U* containing the origin, because we cannot tell whether the bump of *f* fits entirely in *U* or whether it is so large that *f* is identically one in *U*.

On the other hand, germs of smooth functions can distinguish between the constant function with value one and the function $1+e^{-1/x^{2}}$ , because the latter function is not identically one on any neighborhood of the origin. This example shows that germs contain more information than the power series expansion of a function, because the power series of $1+e^{-1/x^{2}}$ is identically one. (This extra information is related to the fact that the stalk of the sheaf of smooth functions at the origin is a non-Noetherian ring. The Krull intersection theorem says that this cannot happen for a Noetherian ring.)

### Quasi-coherent sheaves

On an affine scheme $X=\mathrm {Spec} (A)$ , the stalk of a quasi-coherent sheaf *${\mathcal {F}}$* corresponding to an A -module M in a point *x* corresponding to a prime ideal p is just the localization $M_{p}$ .

### Skyscraper sheaf

On any topological space, the skyscraper sheaf associated to a closed point x and a group or ring G has the stalks 0 off x and G on x —hence the name skyscraper. This idea makes more sense if one adopts the common visualisation of functions mapping from some space above to a space below; with this visualisation, any function that maps $G\to x$ has G positioned directly above x . The same property holds for any point x if the topological space in question is a T1 space, since every point of a T1 space is closed. This feature is the basis of the construction of Godement resolutions, used for example in algebraic geometry to get functorial injective resolutions of sheaves.

## Properties of the stalk

As outlined in the introduction, stalks capture the local behaviour of a sheaf. As a sheaf is supposed to be determined by its local restrictions (see gluing axiom), it can be expected that the stalks capture a fair amount of the information that the sheaf is encoding. This is indeed true:

- A morphism of sheaves is an isomorphism, epimorphism, or monomorphism, respectively, if and only if the induced morphisms on all stalks have the same property. (However it is not true that two sheaves, all of whose stalks are isomorphic, are isomorphic, too, because there may be no map between the sheaves in question.)

In particular:

- A sheaf is zero (if we are dealing with sheaves of groups), if and only if all stalks of the sheaf vanish. Therefore, the exactness of a given functor can be tested on the stalks, which is often easier as one can pass to smaller and smaller neighbourhoods.

Both statements are false for presheaves. However, stalks of sheaves and presheaves are tightly linked:

- Given a presheaf ${\mathcal {P}}$ and its sheafification ${\mathcal {F}}={\mathcal {P}}^{+}$ , the stalks of ${\mathcal {P}}$ and ${\mathcal {F}}$ agree. This follows from the fact that the sheaf ${\mathcal {F}}={\mathcal {P}}^{+}$ is the image of ${\mathcal {P}}$ through the left adjoint $(-)^{+}:\mathbf {Set} ^{{\mathcal {O}}(X)^{op}}\to Sh(X)$ (because the sheafification functor is left adjoint to the inclusion functor $Sh(X)\to \mathbf {Set} ^{{\mathcal {O}}(X)^{op}}$ ) and the fact that left adjoints preserve colimits.

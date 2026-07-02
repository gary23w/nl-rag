---
title: "Topological K-theory"
source: https://en.wikipedia.org/wiki/Topological_K-theory
domain: k-theory
license: CC-BY-SA-4.0
tags: topological k-theory, algebraic k-theory, grothendieck group, vector bundle
fetched: 2026-07-02
---

# Topological *K*-theory

In mathematics, **topological K-theory** is a branch of algebraic topology. It was founded to study vector bundles on topological spaces, by means of ideas now recognised as (general) K-theory that were introduced by Alexander Grothendieck. The early work on topological K-theory is due to Michael Atiyah and Friedrich Hirzebruch.

## Definitions

Let X be a compact Hausdorff space and $k=\mathbb {R}$ or $\mathbb {C}$ . Then $K_{k}(X)$ is defined to be the Grothendieck group of the commutative monoid of isomorphism classes of finite-dimensional k-vector bundles over X under Whitney sum. Tensor product of bundles gives K-theory a commutative ring structure. Without subscripts, $K(X)$ usually denotes complex K-theory whereas real K-theory is sometimes written as $KO(X)$ . The remaining discussion is focused on complex K-theory.

As a first example, note that the K-theory of a point is the integers. This is because vector bundles over a point are trivial and thus classified by their rank and the Grothendieck group of the natural numbers is the integers.

There is also a reduced version of K-theory, ${\widetilde {K}}(X)$ , defined for X a compact pointed space (cf. reduced homology). This reduced theory is intuitively *K*(*X*) modulo trivial bundles. It is defined as the group of stable equivalence classes of bundles. Two bundles E and F are said to be **stably isomorphic** if there are trivial bundles $\varepsilon _{1}$ and $\varepsilon _{2}$ , so that $E\oplus \varepsilon _{1}\cong F\oplus \varepsilon _{2}$ . This equivalence relation results in a group since every vector bundle can be completed to a trivial bundle by summing with its orthogonal complement. Alternatively, ${\widetilde {K}}(X)$ can be defined as the kernel of the map $K(X)\to K(x_{0})\cong \mathbb {Z}$ induced by the inclusion of the base point *x*0 into X.

K-theory forms a multiplicative (generalized) cohomology theory as follows. The short exact sequence of a pair of pointed spaces (*X*, *A*)

${\widetilde {K}}(X/A)\to {\widetilde {K}}(X)\to {\widetilde {K}}(A)$

extends to a long exact sequence

$\cdots \to {\widetilde {K}}(SX)\to {\widetilde {K}}(SA)\to {\widetilde {K}}(X/A)\to {\widetilde {K}}(X)\to {\widetilde {K}}(A).$

Let *Sn* be the n-th reduced suspension of a space and then define

${\widetilde {K}}^{-n}(X):={\widetilde {K}}(S^{n}X),\qquad n\geq 0.$

Negative indices are chosen so that the coboundary maps increase dimension.

It is often useful to have an unreduced version of these groups, simply by defining:

$K^{-n}(X)={\widetilde {K}}^{-n}(X_{+}).$

Here $X_{+}$ is X with a disjoint basepoint labeled '+' adjoined.

Finally, the Bott periodicity theorem as formulated below extends the theories to positive integers.

## Properties

- $K^{n}$ (respectively, ${\widetilde {K}}^{n}$ ) is a contravariant functor from the homotopy category of (pointed) spaces to the category of commutative rings. Thus, for instance, the K-theory over contractible spaces is always $\mathbb {Z} .$
- The spectrum of K-theory is $BU\times \mathbb {Z}$ (with the discrete topology on $\mathbb {Z}$ ), i.e. $K(X)\cong [X_{+},\mathbb {Z} \times BU],$ where [ , ] denotes pointed homotopy classes and *BU* is the colimit of the classifying spaces of the unitary groups: $BU(n)\cong \operatorname {Gr} (n,\mathbb {C} ^{\infty }).$ Similarly, ${\widetilde {K}}(X)\cong [X,\mathbb {Z} \times BU].$ For real K-theory use *BO*.
- There is a natural ring homomorphism $K^{0}(X)\to H^{2*}(X,\mathbb {Q} ),$ the Chern character, such that $K^{0}(X)\otimes \mathbb {Q} \to H^{2*}(X,\mathbb {Q} )$ is an isomorphism.
- The equivalent of the Steenrod operations in K-theory are the Adams operations. They can be used to define characteristic classes in topological K-theory.
- The Splitting principle of topological K-theory allows one to reduce statements about arbitrary vector bundles to statements about sums of line bundles.
- The Thom isomorphism theorem in topological K-theory is $K(X)\cong {\widetilde {K}}(T(E)),$ where *T*(*E*) is the Thom space of the vector bundle E over X. This holds whenever E is a spin-bundle.
- The Atiyah-Hirzebruch spectral sequence allows computation of K-groups from ordinary cohomology groups.
- Topological K-theory can be generalized vastly to a functor on C*-algebras, see operator K-theory and KK-theory.

## Bott periodicity

The phenomenon of periodicity named after Raoul Bott (see Bott periodicity theorem) can be formulated this way:

- $K(X\times \mathbb {S} ^{2})=K(X)\otimes K(\mathbb {S} ^{2}),$ and $K(\mathbb {S} ^{2})=\mathbb {Z} [H]/(H-1)^{2}$ where *H* is the class of the tautological bundle on $\mathbb {S} ^{2}=\mathbb {P} ^{1}(\mathbb {C} ),$ i.e. the Riemann sphere.
- ${\widetilde {K}}^{n+2}(X)={\widetilde {K}}^{n}(X).$
- $\Omega ^{2}BU\cong BU\times \mathbb {Z} .$

In real K-theory there is a similar periodicity, but modulo 8.

## Applications

Topological K-theory has been applied in John Frank Adams’ proof of the “Hopf invariant one” problem via Adams operations. Adams also proved an upper bound for the number of linearly-independent vector fields on spheres.

## Chern character

Michael Atiyah and Friedrich Hirzebruch proved a theorem relating the topological K-theory of a finite CW complex X with its rational cohomology. In particular, they showed that there exists a homomorphism

$ch:K_{\text{top}}^{*}(X)\otimes \mathbb {Q} \to H^{*}(X;\mathbb {Q} )$

such that

${\begin{aligned}K_{\text{top}}^{0}(X)\otimes \mathbb {Q} &\cong \bigoplus _{k}H^{2k}(X;\mathbb {Q} )\\K_{\text{top}}^{1}(X)\otimes \mathbb {Q} &\cong \bigoplus _{k}H^{2k+1}(X;\mathbb {Q} )\end{aligned}}$

There is an algebraic analogue relating the Grothendieck group of coherent sheaves and the Chow ring of a smooth projective variety X .

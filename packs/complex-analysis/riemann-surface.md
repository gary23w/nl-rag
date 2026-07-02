---
title: "Riemann surface"
source: https://en.wikipedia.org/wiki/Riemann_surface
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Riemann surface

In mathematics, particularly in complex analysis, a **Riemann surface** is a connected one-dimensional complex manifold. These surfaces were first studied by and are named after Bernhard Riemann. Riemann surfaces can be thought of as deformed versions of the complex plane: locally near every point they look like patches of the complex plane, but the global topology can be quite different. For example, they can look like a sphere or a torus or several sheets glued together.

Examples of Riemann surfaces include graphs of multivalued functions such as ${\sqrt {z}}$ or $\log(z)$ , e.g. the subset of pairs $(z,w)\in \mathbb {C} ^{2}$ with $w=\log(z)$ .

Every Riemann surface is a surface: a two-dimensional real manifold, but it contains more structure (specifically a complex structure). Conversely, a two-dimensional real manifold can be turned into a Riemann surface (usually in several inequivalent ways) if and only if it is orientable and metrizable. Given this, the sphere and torus admit complex structures but the Möbius strip, Klein bottle and real projective plane do not. Every compact Riemann surface is a complex algebraic curve by Chow's theorem and the Riemann–Roch theorem.

## Definitions

There are several equivalent definitions of a Riemann surface.

1. A Riemann surface X is a connected complex manifold of complex dimension one. This means that X is a connected Hausdorff space that is endowed with an atlas of charts to the open unit disk of the complex plane: for every point $x\in X$ there is a neighbourhood of x that is homeomorphic to the open unit disk of the complex plane, and the transition maps between two overlapping charts are required to be holomorphic.
2. A Riemann surface is a (connected) oriented manifold of (real) dimension two – a two-sided surface – together with a conformal structure. Again, manifold means that locally at any point x of X , the space is homeomorphic to a subset of the real plane. The supplement "Riemann" signifies that X is endowed with an additional structure that allows angle measurement on the manifold, namely an equivalence class of so-called Riemannian metrics. Two such metrics are considered equivalent if the angles they measure are the same. Choosing an equivalence class of metrics on X is the additional datum of the conformal structure.

A complex structure gives rise to a conformal structure by choosing the standard Euclidean metric given on the complex plane and transporting it to X by means of the charts. Showing that a conformal structure determines a complex structure is more difficult.

## Examples

- The complex plane $\mathbb {C}$ is the most basic Riemann surface.
- Every nonempty connected open subset of the complex plane $U\subseteq \mathbb {C}$ is a Riemann surface. More generally, every non-empty open subset of a Riemann surface is a Riemann surface.
- The 2-sphere $S^{2}$ has a unique Riemann surface structure, called the **Riemann sphere**. It has two open subsets that we identify with the complex plane by stereographically projecting from the north or south poles $\mathbb {C} \hookrightarrow S^{2}\hookleftarrow \mathbb {C}$ . On the intersection of these two open sets, composing one embedding with the inverse of the other gives $\mathbb {C} ^{\times }\to \mathbb {C} ^{\times }:z\mapsto z^{-1}$ . This transition map is holomorphic, so these two embeddings define a Riemann surface structure on $S^{2}$ . As sets, $S^{2}=\mathbb {C} \cup \{\infty \}$ . The Riemann sphere has another description, as the projective line $\mathbb {CP} ^{1}=(\mathbb {C} ^{2}\setminus \{0\})/\mathbb {C} ^{\times }$ .
- The 2-torus $T^{2}$ has many different Riemann surface structures, all of the form $\mathbb {C} /(\mathbb {Z} +\tau \mathbb {Z} )$ , where $\tau$ is any complex non-real number. These are called **elliptic curves**.
- Important examples of non-compact Riemann surfaces are provided by analytic continuation.

### Algebraic curves

- If $P(x,y)$ is any complex polynomial in two variables, its vanishing locus $\{(x,y):P(x,y)=0\}\subseteq \mathbb {C} ^{2}$ defines a Riemann surface provided there are no points on this locus with $\partial P/\partial x=\partial P/\partial y=0$ (or we restrict to an open subset containing no such points). This is an example of an algebraic curve.
- Every elliptic curve is an algebraic curve, given by (the compactification of) the locus $y^{2}=x^{3}+ax+b$ for certain complex numbers a and b depending on $\tau$ . A point $z\in \mathbb {C} /(\mathbb {Z} +\tau \mathbb {Z} )$ is sent to $(x,y)=(\wp (z),\wp '(z))$ , where $\wp$ is the Weierstrass elliptic function.
- Likewise, genus g surfaces have Riemann surface structures, as (compactifications of) hyperelliptic surfaces $y^{2}=Q(x)$ , where Q is a complex polynomial of degree $2g+1$ such that the above has no singular points. When $g>1$ , there are other Riemann surface structures of genus g .

- ('"`UNIQ--postMath-0000002D-QINU`"') $f(z)=\arcsin z$
- ('"`UNIQ--postMath-0000002E-QINU`"') $f(z)=\log z$
- ('"`UNIQ--postMath-0000002F-QINU`"') $f(z)={\sqrt {z}}$
- ('"`UNIQ--postMath-00000030-QINU`"') $f(z)={\sqrt[{3}]{z}}$
- ('"`UNIQ--postMath-00000031-QINU`"') $f(z)={\sqrt[{4}]{z}}$

## Further definitions and properties

As with any map between complex manifolds, a function $f:M\to N$ between two Riemann surfaces M and N is called *holomorphic* if for every chart g in the atlas of M and every chart h in the atlas of N , the map $h\circ f\circ g^{-1}$ is holomorphic (as a function from $\mathbb {C}$ to $\mathbb {C}$ ) wherever it is defined. The composition of two holomorphic maps is holomorphic. The two Riemann surfaces M and N are called *biholomorphic* (or *conformally equivalent* to emphasize the conformal point of view) if there exists a bijective holomorphic function from M to N whose inverse is also holomorphic (it turns out that the latter condition is automatic and can therefore be omitted). Two conformally equivalent Riemann surfaces are for all practical purposes identical.

### Orientability

Each Riemann surface, being a complex manifold, is orientable as a real manifold. For complex charts f and g with transition function $h=f(g^{-1}(z))$ , h can be considered as a map from an open set of $\mathbb {R} ^{2}$ to $\mathbb {R} ^{2}$ whose Jacobian in a point z is just the real linear map given by multiplication by the complex number $h'(z)$ . However, the real determinant of multiplication by a complex number $\alpha$ equals $|\alpha |^{2}$ , so the Jacobian of h has positive determinant. Consequently, the complex atlas is an oriented atlas.

### Functions

Every non-compact Riemann surface admits non-constant holomorphic functions (with values in $\mathbb {C}$ ). In fact, every non-compact Riemann surface is a Stein manifold.

In contrast, on a compact Riemann surface X every holomorphic function with values in $\mathbb {C}$ is constant due to the maximum principle. However, there always exist non-constant meromorphic functions (holomorphic functions with values in the Riemann sphere $\mathbb {C} \cup \{\infty \}$ ). More precisely, the function field of X is a finite extension of $\mathbb {C} (t)$ , the function field in one variable, i.e. any two meromorphic functions are algebraically dependent. This statement generalizes to higher dimensions, see Siegel (1955). Meromorphic functions can be given fairly explicitly, in terms of Riemann theta functions and the Abel–Jacobi map of the surface.

### Algebraicity

All compact Riemann surfaces are algebraic curves since they can be embedded into some $\mathbb {CP} ^{n}$ . This follows from the Kodaira embedding theorem and the fact there exists a positive line bundle on any complex curve.

## Analytic vs. algebraic

The existence of non-constant meromorphic functions can be used to show that any compact Riemann surface is a projective variety, i.e. can be given by polynomial equations inside a projective space. Actually, it can be shown that every compact Riemann surface can be embedded into complex projective 3-space. This is a surprising theorem: Riemann surfaces are given by locally patching charts. If one global condition, namely compactness, is added, the surface is necessarily algebraic. This feature of Riemann surfaces allows one to study them with either the means of analytic or algebraic geometry. The corresponding statement for higher-dimensional objects is false, i.e. there are compact complex 2-manifolds which are not algebraic. On the other hand, every projective complex manifold is necessarily algebraic, see Chow's theorem.

As an example, consider the torus $T:=\mathbb {C} /(\mathbb {Z} +\tau \mathbb {Z} )$ . The Weierstrass function $\wp _{\tau }(z)$ belonging to the lattice $\mathbb {Z} +\tau \mathbb {Z}$ is a meromorphic function on T . This function and its derivative $\wp '_{\tau }(z)$ generate the function field of T . There is an equation

$[\wp '(z)]^{2}=4[\wp (z)]^{3}-g_{2}\wp (z)-g_{3}$

where the coefficients $g_{2}$ and $g_{3}$ depend on $\tau$ , thus giving an elliptic curve $E_{\tau }$ in the sense of algebraic geometry. Reversing this is accomplished by the j -invariant $j(E)$ , which can be used to determine $\tau$ and hence a torus.

## Classification of Riemann surfaces

The set of all Riemann surfaces can be divided into three subsets: hyperbolic, parabolic and elliptic Riemann surfaces. Geometrically, these correspond to surfaces with negative, vanishing or positive constant sectional curvature. That is, every connected Riemann surface X admits a unique complete 2-dimensional real Riemann metric with constant curvature equal to $-1$ , 0 or 1 that belongs to the conformal class of Riemannian metrics determined by its structure as a Riemann surface. This can be seen as a consequence of the existence of isothermal coordinates.

In complex analytic terms, the Poincaré–Koebe uniformization theorem (a generalization of the Riemann mapping theorem) states that every simply connected Riemann surface is conformally equivalent to one of the following:

- The Riemann sphere ${\widehat {\mathbb {C} }}:=\mathbb {C} \cup \{\infty \}$ , which is isomorphic to $\mathbb {P} ^{1}(\mathbb {C} )$ ;
- The complex plane $\mathbb {C}$ ;
- The open disk $\mathbb {D} :=\{z\in \mathbb {C} :|z|<1\}$ , which is isomorphic to the upper half-plane $\mathbb {H} :=\{z\in \mathbb {C} :\operatorname {Im} (z)>0\}$ .

A Riemann surface is elliptic, parabolic or hyperbolic according to whether its universal cover is isomorphic to $\mathbb {P} ^{1}(\mathbb {C} )$ , $\mathbb {C}$ or $\mathbb {D}$ . The elements in each class admit a more precise description.

### Elliptic Riemann surfaces

The Riemann sphere $\mathbb {P} ^{1}(\mathbb {C} )$ is the only example, as there is no group acting on it by biholomorphic transformations freely and properly discontinuously and so any Riemann surface whose universal cover is isomorphic to $\mathbb {P} ^{1}(\mathbb {C} )$ must itself be isomorphic to it.

### Parabolic Riemann surfaces

If X is a Riemann surface whose universal cover is isomorphic to the complex plane $\mathbb {C}$ then it is isomorphic to one of the following surfaces:

- $\mathbb {C}$ itself;
- The quotient $\mathbb {C} /\mathbb {Z}$ ;
- A quotient $\mathbb {C} /(\mathbb {Z} +\tau \mathbb {Z} )$ , where $\tau \in \mathbb {C}$ with $\operatorname {Im} (\tau )>0$ .

Topologically there are only three types: the plane, the cylinder and the torus. But while in the two former case the (parabolic) Riemann surface structure is unique, varying the parameter $\tau$ in the third case gives non-isomorphic Riemann surfaces. The description by the parameter $\tau$ gives the Teichmüller space of "marked" Riemann surfaces (in addition to the Riemann surface structure one adds the topological data of a "marking", which can be seen as a fixed homeomorphism to the torus). To obtain the analytic moduli space (forgetting the marking) one takes the quotient of Teichmüller space by the mapping class group. In this case it is the modular curve.

### Hyperbolic Riemann surfaces

In the remaining cases, X is a hyperbolic Riemann surface, that is isomorphic to a quotient of the upper half-plane by a Fuchsian group (this is sometimes called a Fuchsian model for the surface). The topological type of X can be any orientable surface save the torus and sphere.

A case of particular interest is when X is compact. Then its topological type is described by its genus $g\geq 2$ . Its Teichmüller space and moduli space are $(6g-6)$ -dimensional. A similar classification of Riemann surfaces of finite type (that is homeomorphic to a closed surface minus a finite number of points) can be given. However, in general the moduli space of Riemann surfaces of infinite topological type is too large to admit such a description.

## Maps between Riemann surfaces

The geometric classification is reflected in maps between Riemann surfaces, as detailed in Liouville's theorem and the Little Picard theorem: maps from hyperbolic to parabolic to elliptic are easy, but maps from elliptic to parabolic or parabolic to hyperbolic are very constrained (indeed, generally constant!). There are inclusions of the disc in the plane in the sphere:

$\Delta \subset \mathbb {C} \subset {\widehat {\mathbb {C} }}$

but any holomorphic map from the sphere to the plane is constant, any holomorphic map from the plane into the unit disk is constant (Liouville's theorem), and in fact any holomorphic map from the plane into the plane minus two points is constant (Little Picard theorem)!

### Punctured spheres

These statements are clarified by considering the type of a Riemann sphere ${\widehat {\mathbb {C} }}$ with a number of punctures. With no punctures, it is the Riemann sphere, which is elliptic. With one puncture, which can be placed at infinity, it is the complex plane, which is parabolic. With two punctures, it is the punctured plane or alternatively annulus or cylinder, which is parabolic. With three or more punctures, it is hyperbolic – compare pair of pants. One can map from one puncture to two, via the exponential map (which is entire and has an essential singularity at infinity, so not defined at infinity, and misses zero and infinity), but all maps from zero punctures to one or more, or one or two punctures to three or more are constant.

### Ramified covering spaces

Continuing in this vein, compact Riemann surfaces can map to surfaces of *lower* genus, but not to *higher* genus, except as constant maps. This is because holomorphic and meromorphic maps behave locally like

$z\mapsto z^{n}$

for integer n , so non-constant maps are ramified covering maps, and for compact Riemann surfaces these are constrained by the Riemann–Hurwitz formula in algebraic topology, which relates the Euler characteristic of a space and a ramified cover.

For example, hyperbolic Riemann surfaces are ramified covering spaces of the sphere (they have non-constant meromorphic functions), but the sphere does not cover or otherwise map to higher genus surfaces, except as a constant.

## Isometries of Riemann surfaces

The isometry group of a uniformized Riemann surface (equivalently, the conformal automorphism group) reflects its geometry:

- genus 0 – the isometry group of the sphere is the Möbius group of projective transforms of the complex line,
- the isometry group of the plane is the subgroup fixing infinity, and of the punctured plane is the subgroup leaving invariant the set containing only infinity and zero: either fixing them both, or interchanging them $(1/z)$ .
- the isometry group of the upper half-plane is the real Möbius group; this is conjugate to the automorphism group of the disk.
- genus 1 – the isometry group of a torus is in general generated by translations (as an Abelian variety) and the rotation by $180^{\circ }$ . In special cases there can be additional rotations and reflections.
- For genus $g\geq 2$ , the isometry group is finite, and has order at most $84(g-1)$ , by Hurwitz's automorphisms theorem; surfaces that realize this bound are called **Hurwitz surfaces**.
- It is known that every finite group can be realized as the full group of isometries of some Riemann surface.

  - For genus 2 the order is maximized by the Bolza surface, with order 48.
  - For genus 3 the order is maximized by the Klein quartic, with order 168; this is the first Hurwitz surface, and its automorphism group is isomorphic to the unique simple group of order 168, which is the second-smallest non-abelian simple group. This group is isomorphic to both $\mathrm {PSL} (2,7)$ and $\mathrm {PSL} (3,2)$ .
  - For genus 4, Bring's surface is a highly symmetric surface.
  - For genus 7 the order is maximized by the Macbeath surface, with order 504; this is the second Hurwitz surface, and its automorphism group is isomorphic to $\mathrm {PSL} (2,8)$ , the fourth-smallest non-abelian simple group.

## Function-theoretic classification

The classification scheme above is typically used by geometers. There is a different classification for Riemann surfaces that is typically used by complex analysts. It employs a different definition for "parabolic" and "hyperbolic". In this alternative classification scheme, a Riemann surface is called *parabolic* if there are no non-constant negative subharmonic functions on the surface and is otherwise called *hyperbolic*.

This class of hyperbolic surfaces is further subdivided into subclasses according to whether function spaces other than the negative subharmonic functions are degenerate, e.g. Riemann surfaces on which all bounded holomorphic functions are constant, or on which all bounded harmonic functions are constant, or on which all positive harmonic functions are constant, etc.

To avoid confusion, call the classification based on metrics of constant curvature the *geometric classification*, and the one based on degeneracy of function spaces *the function-theoretic classification*. For example, the Riemann surface $\mathbb {C} \setminus \{0,1\}$ "is parabolic in the function-theoretic classification but it is hyperbolic in the geometric classification.

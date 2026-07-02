---
title: "Sheaf cohomology"
source: https://en.wikipedia.org/wiki/Sheaf_cohomology
domain: sheaf-theory
license: CC-BY-SA-4.0
tags: sheaf theory, sheaf cohomology, grothendieck topology, ringed space
fetched: 2026-07-02
---

# Sheaf cohomology

In mathematics, **sheaf cohomology** is the application of homological algebra to analyze the global sections of a sheaf on a topological space. Broadly speaking, sheaf cohomology describes the obstructions (holes) to solving a geometric problem globally when it can be solved locally. The central work for the study of sheaf cohomology is Grothendieck's 1957 Tôhoku paper.

Sheaves, sheaf cohomology, and spectral sequences were introduced by Jean Leray at the prisoner-of-war camp Oflag XVII-A in Austria. From 1940 to 1945, Leray and other prisoners organized a "université en captivité" in the camp.

Leray's definitions were simplified and clarified in the 1950s. It became clear that sheaf cohomology was not only a new approach to cohomology in algebraic topology, but also a powerful method in complex analytic geometry and algebraic geometry. These subjects often involve constructing global functions with specified local properties, and sheaf cohomology is ideally suited to such problems. Many earlier results such as the Riemann–Roch theorem and the Hodge theorem have been generalized or understood better using sheaf cohomology.

## Definition

The category of sheaves of abelian groups on a topological space *X* is an abelian category, and so it makes sense to ask when a morphism *f*: *B* → *C* of sheaves is injective (a monomorphism) or surjective (an epimorphism). One answer is that *f* is injective (respectively surjective) if and only if the associated homomorphism on stalks *B**x* → *C**x* is injective (respectively surjective) for every point *x* in *X*. It follows that *f* is injective if and only if the homomorphism *B*(*U*) → *C*(*U*) of sections over *U* is injective for every open set *U* in *X*. Surjectivity is more subtle, however: the morphism *f* is surjective if and only if for every open set *U* in *X*, every section *s* of *C* over *U*, and every point *x* in *U*, there is an open neighborhood *V* of *x* in *U* such that *s* restricted to *V* is the image of some section of *B* over *V*. (In words: every section of *C* lifts *locally* to sections of *B*.)

As a result, the question arises: given a surjection *B* → *C* of sheaves and a section *s* of *C* over *X*, when is *s* the image of a section of *B* over *X*? This is a model for all kinds of local-vs.-global questions in geometry. Sheaf cohomology gives a satisfactory general answer. Namely, let *A* be the kernel of the surjection *B* → *C*, giving a short exact sequence

$0\to A\to B\to C\to 0$

of sheaves on *X*. Then there is a long exact sequence of abelian groups, called sheaf cohomology groups:

$0\to H^{0}(X,A)\to H^{0}(X,B)\to H^{0}(X,C)\to H^{1}(X,A)\to \cdots ,$

where *H*0(*X*,*A*) is the group *A*(*X*) of global sections of *A* on *X*. For example, if the group *H*1(*X*,*A*) is zero, then this exact sequence implies that every global section of *C* lifts to a global section of *B*. More broadly, the exact sequence makes knowledge of higher cohomology groups a fundamental tool in aiming to understand sections of sheaves.

Grothendieck's definition of sheaf cohomology, now standard, uses the language of homological algebra. The essential point is to fix a topological space *X* and think of cohomology as a functor from sheaves of abelian groups on *X* to abelian groups. In more detail, start with the functor *E* ↦ *E*(*X*) from sheaves of abelian groups on *X* to abelian groups. This is left exact, but in general not right exact. Then the groups *H**i*(*X*,*E*) for integers *i* are defined as the right derived functors of the functor *E* ↦ *E*(*X*). This makes it automatic that *H**i*(*X*,*E*) is zero for *i* < 0, and that *H*0(*X*,*E*) is the group *E*(*X*) of global sections. The long exact sequence above is also straightforward from this definition.

The definition of derived functors uses that the category of sheaves of abelian groups on any topological space *X* has enough injectives; that is, for every sheaf *E* there is an injective sheaf *I* with an injection *E* → *I*. It follows that every sheaf *E* has an injective resolution:

$0\to E\to I_{0}\to I_{1}\to I_{2}\to \cdots .$

Then the sheaf cohomology groups *H**i*(*X*,*E*) are the cohomology groups (the kernel of one homomorphism modulo the image of the previous one) of the chain complex of abelian groups:

$0\to I_{0}(X)\to I_{1}(X)\to I_{2}(X)\to \cdots .$

Standard arguments in homological algebra imply that these cohomology groups are independent of the choice of injective resolution of *E*.

The definition is rarely used directly to compute sheaf cohomology. It is nonetheless powerful, because it works in great generality (any sheaf of abelian groups on any topological space), and it easily implies the formal properties of sheaf cohomology, such as the long exact sequence above. For specific classes of spaces or sheaves, there are many tools for computing sheaf cohomology, some discussed below.

## Functoriality

For any continuous map *f*: *X* → *Y* of topological spaces, and any sheaf *E* of abelian groups on *Y*, there is a **pullback homomorphism**

$f^{*}\colon H^{j}(Y,E)\to H^{j}(X,f^{*}(E))$

for every integer *j*, where *f**(*E*) denotes the inverse image sheaf or **pullback sheaf**. If *f* is the inclusion of a subspace *X* of *Y*, *f**(*E*) is the **restriction** of *E* to *X*, often just called *E* again, and the pullback of a section *s* from *Y* to *X* is called the restriction *s*|*X*.

Pullback homomorphisms are used in the Mayer–Vietoris sequence, an important computational result. Namely, let *X* be a topological space which is a union of two open subsets *U* and *V*, and let *E* be a sheaf on *X*. Then there is a long exact sequence of abelian groups:

$0\to H^{0}(X,E)\to H^{0}(U,E)\oplus H^{0}(V,E)\to H^{0}(U\cap V,E)\to H^{1}(X,E)\to \cdots .$

## Sheaf cohomology with constant coefficients

For a topological space X and an abelian group A , the constant sheaf $A_{X}$ means the sheaf of locally constant functions with values in A . The sheaf cohomology groups $H^{j}(X,A_{X})$ with constant coefficients are often written simply as $H^{j}(X,A)$ , unless this could cause confusion with another version of cohomology such as singular cohomology.

For a continuous map *f*: *X* → *Y* and an abelian group *A*, the pullback sheaf *f**(*A**Y*) is isomorphic to *A**X*. As a result, the pullback homomorphism makes sheaf cohomology with constant coefficients into a contravariant functor from topological spaces to abelian groups.

For any spaces *X* and *Y* and any abelian group *A*, two homotopic maps *f* and *g* from *X* to *Y* induce the *same* homomorphism on sheaf cohomology:

$f^{*}=g^{*}:H^{j}(Y,A)\to H^{j}(X,A).$

It follows that two homotopy equivalent spaces have isomorphic sheaf cohomology with constant coefficients.

Let *X* be a paracompact Hausdorff space which is locally contractible, even in the weak sense that every open neighborhood *U* of a point *x* contains an open neighborhood *V* of *x* such that the inclusion *V* → *U* is homotopic to a constant map. Then the singular cohomology groups of *X* with coefficients in an abelian group *A* are isomorphic to sheaf cohomology with constant coefficients, *H**(*X*,*A**X*). For example, this holds for *X* a topological manifold or a CW complex.

As a result, many of the basic calculations of sheaf cohomology with constant coefficients are the same as calculations of singular cohomology. See the article on cohomology for the cohomology of spheres, projective spaces, tori, and surfaces.

For arbitrary topological spaces, singular cohomology and sheaf cohomology (with constant coefficients) can be different. This happens even for *H*0. The singular cohomology *H*0(*X*,**Z**) is the group of all functions from the set of path components of *X* to the integers **Z**, whereas sheaf cohomology *H*0(*X*,**Z***X*) is the group of locally constant functions from *X* to **Z**. These are different, for example, when *X* is the Cantor set. Indeed, the sheaf cohomology *H*0(*X*,**Z***X*) is a countable abelian group in that case, whereas the singular cohomology *H*0(*X*,**Z**) is the group of *all* functions from *X* to **Z**, which has cardinality

$2^{2^{\aleph _{0}}}.$

For a paracompact Hausdorff space *X* and any sheaf *E* of abelian groups on *X*, the cohomology groups *H**j*(*X*,*E*) are zero for *j* greater than the covering dimension of *X*. (This does not hold in the same generality for singular cohomology: for example, there is a compact subset of Euclidean space **R**3 that has nonzero singular cohomology in infinitely many degrees.) The covering dimension agrees with the usual notion of dimension for a topological manifold or a CW complex.

## Flabby and soft sheaves

A sheaf *E* of abelian groups on a topological space *X* is called **acyclic** if *H**j*(*X*,*E*) = 0 for all *j* > 0. By the long exact sequence of sheaf cohomology, the cohomology of any sheaf can be computed from any acyclic resolution of *E* (rather than an injective resolution). Injective sheaves are acyclic, but for computations it is useful to have other examples of acyclic sheaves.

A sheaf *E* on *X* is called **flabby** (French: *flasque*) if every section of *E* on an open subset of *X* extends to a section of *E* on all of *X*. Flabby sheaves are acyclic. Godement defined sheaf cohomology via a canonical flabby resolution of any sheaf; since flabby sheaves are acyclic, Godement's definition agrees with the definition of sheaf cohomology above.

A sheaf *E* on a paracompact Hausdorff space *X* is called **soft** if every section of the restriction of *E* to a closed subset of *X* extends to a section of *E* on all of *X*. Every soft sheaf is acyclic.

Some examples of soft sheaves are the sheaf of real-valued continuous functions on any paracompact Hausdorff space, or the sheaf of smooth (*C*∞) functions on any smooth manifold. More generally, any sheaf of modules over a soft sheaf of commutative rings is soft; for example, the sheaf of smooth sections of a vector bundle over a smooth manifold is soft.

For example, these results form part of the proof of de Rham's theorem. For a smooth manifold *X*, the Poincaré lemma says that the de Rham complex is a resolution of the constant sheaf **R***X*:

$0\to \mathbf {R} _{X}\to \Omega _{X}^{0}\to \Omega _{X}^{1}\to \cdots ,$

where Ω*X**j* is the sheaf of smooth *j*-forms and the map Ω*X**j* → Ω*X**j*+1 is the exterior derivative *d*. By the results above, the sheaves Ω*X**j* are soft and therefore acyclic. It follows that the sheaf cohomology of *X* with real coefficients is isomorphic to the de Rham cohomology of *X*, defined as the cohomology of the complex of real vector spaces:

$0\to \Omega _{X}^{0}(X)\to \Omega _{X}^{1}(X)\to \cdots .$

The other part of de Rham's theorem is to identify sheaf cohomology and singular cohomology of *X* with real coefficients; that holds in greater generality, as discussed above.

## Čech cohomology

Čech cohomology is an approximation to sheaf cohomology that is often useful for computations. Namely, let ${\mathcal {U}}$ be an open cover of a topological space *X*, and let *E* be a sheaf of abelian groups on *X*. Write the open sets in the cover as *U**i* for elements *i* of a set *I*, and fix an ordering of *I*. Then Čech cohomology $H^{j}({\mathcal {U}},E)$ is defined as the cohomology of an explicit complex of abelian groups with *j*th group

$C^{j}({\mathcal {U}},E)=\prod _{i_{0}<\cdots <i_{j}}E(U_{i_{0}}\cap \cdots \cap U_{i_{j}}).$

There is a natural homomorphism $H^{j}({\mathcal {U}},E)\to H^{j}(X,E)$ . Thus Čech cohomology is an approximation to sheaf cohomology using only the sections of *E* on finite intersections of the open sets *U**i*.

If every finite intersection *V* of the open sets in ${\mathcal {U}}$ has no higher cohomology with coefficients in *E*, meaning that *H**j*(*V*,*E*) = 0 for all *j* > 0, then the homomorphism from Čech cohomology $H^{j}({\mathcal {U}},E)$ to sheaf cohomology is an isomorphism.

Another approach to relating Čech cohomology to sheaf cohomology is as follows. The **Čech cohomology groups** ${\check {H}}^{j}(X,E)$ are defined as the direct limit of $H^{j}({\mathcal {U}},E)$ over all open covers ${\mathcal {U}}$ of *X* (where open covers are ordered by refinement). There is a homomorphism ${\check {H}}^{j}(X,E)\to H^{j}(X,E)$ from Čech cohomology to sheaf cohomology, which is an isomorphism for *j* ≤ 1. For arbitrary topological spaces, Čech cohomology can differ from sheaf cohomology in higher degrees. Conveniently, however, Čech cohomology is isomorphic to sheaf cohomology for any sheaf on a paracompact Hausdorff space.

The isomorphism ${\check {H}}^{1}(X,E)\cong H^{1}(X,E)$ implies a description of *H*1(*X*,*E*) for any sheaf *E* of abelian groups on a topological space *X*: this group classifies the *E*-**torsors** (also called principal *E*-bundles) over *X*, up to isomorphism. (This statement generalizes to any sheaf of groups *G*, not necessarily abelian, using the non-abelian cohomology set *H*1(*X*,*G*).) By definition, an *E*-torsor over *X* is a sheaf *S* of sets together with an action of *E* on *X* such that every point in *X* has an open neighborhood on which *S* is isomorphic to *E*, with *E* acting on itself by translation. For example, on a ringed space (*X*,*O**X*), it follows that the Picard group of invertible sheaves on *X* is isomorphic to the sheaf cohomology group *H*1(*X*,*O**X**), where *O**X** is the sheaf of units in *O**X*.

## Relative cohomology

For a subset *Y* of a topological space *X* and a sheaf *E* of abelian groups on *X*, one can define **relative cohomology** groups:

$H_{Y}^{j}(X,E)=H^{j}(X,X-Y;E)$

for integers *j*. Other names are the cohomology of *X* with **support** in *Y*, or (when *Y* is closed in *X*) **local cohomology**. A long exact sequence relates relative cohomology to sheaf cohomology in the usual sense:

$\cdots \to H_{Y}^{j}(X,E)\to H^{j}(X,E)\to H^{j}(X-Y,E)\to H_{Y}^{j+1}(X,E)\to \cdots .$

When *Y* is closed in *X*, cohomology with support in *Y* can be defined as the derived functors of the functor

$H_{Y}^{0}(X,E):=\{s\in E(X):s|_{X-Y}=0\},$

the group of sections of *E* that are supported on *Y*.

There are several isomorphisms known as **excision**. For example, if *X* is a topological space with subspaces *Y* and *U* such that the closure of *Y* is contained in the interior of *U*, and *E* is a sheaf on *X*, then the restriction

$H_{Y}^{j}(X,E)\to H_{Y}^{j}(U,E)$

is an isomorphism. (So cohomology with support in a closed subset *Y* only depends on the behavior of the space *X* and the sheaf *E* near *Y*.) Also, if *X* is a paracompact Hausdorff space that is the union of closed subsets *A* and *B*, and *E* is a sheaf on *X*, then the restriction

$H^{j}(X,B;E)\to H^{j}(A,A\cap B;E)$

is an isomorphism.

## Cohomology with compact support

Let *X* be a locally compact topological space. (In this article, a locally compact space is understood to be Hausdorff.) For a sheaf *E* of abelian groups on *X*, one can define **cohomology with compact support** *H*c*j*(*X*,*E*). These groups are defined as the derived functors of the functor of compactly supported sections:

$H_{c}^{0}(X,E)=\{s\in E(X):{\text{there is a compact subset }}K{\text{ of }}X{\text{ with }}s|_{X-K}=0\}.$

There is a natural homomorphism *H*c*j*(*X*,*E*) → *H**j*(*X*,*E*), which is an isomorphism for *X* compact.

For a sheaf *E* on a locally compact space *X*, the compactly supported cohomology of *X* × **R** with coefficients in the pullback of *E* is a shift of the compactly supported cohomology of *X*:

$H_{c}^{j+1}(X\times \mathbf {R} ,E)\cong H_{c}^{j}(X,E).$

It follows, for example, that *H**c**j*(**R***n*,**Z**) is isomorphic to **Z** if *j* = *n* and is zero otherwise.

Compactly supported cohomology is not functorial with respect to arbitrary continuous maps. For a proper map *f*: *Y* → *X* of locally compact spaces and a sheaf *E* on *X*, however, there is a pullback homomorphism

$f^{*}\colon H_{c}^{j}(X,E)\to H_{c}^{j}(Y,f^{*}(E))$

on compactly supported cohomology. Also, for an open subset *U* of a locally compact space *X* and a sheaf *E* on *X*, there is a pushforward homomorphism known as **extension by zero**:

$H_{c}^{j}(U,E)\to H_{c}^{j}(X,E).$

Both homomorphisms occur in the long exact **localization sequence** for compactly supported cohomology, for a locally compact space *X* and a closed subset *Y*:

$\cdots \to H_{c}^{j}(X-Y,E)\to H_{c}^{j}(X,E)\to H_{c}^{j}(Y,E)\to H_{c}^{j+1}(X-Y,E)\to \cdots .$

## Cup product

For any sheaves *A* and *B* of abelian groups on a topological space *X*, there is a bilinear map, the **cup product**

$H^{i}(X,A)\times H^{j}(X,B)\to H^{i+j}(X,A\otimes B),$

for all *i* and *j*. Here *A*⊗*B* denotes the tensor product over **Z**, but if *A* and *B* are sheaves of modules over some sheaf *O**X* of commutative rings, then one can map further from *H**i*+*j*(X,*A*⊗**Z***B*) to *H**i*+*j*(X,*A*⊗*O**X**B*). In particular, for a sheaf *O**X* of commutative rings, the cup product makes the direct sum

$H^{*}(X,O_{X})=\bigoplus _{j}H^{j}(X,O_{X})$

into a graded-commutative ring, meaning that

$vu=(-1)^{ij}uv$

for all *u* in *H**i* and *v* in *H**j*.

## Complexes of sheaves

The definition of sheaf cohomology as a derived functor extends to define cohomology of a topological space *X* with coefficients in any complex *E* of sheaves:

$\cdots \to E_{j}\to E_{j+1}\to E_{j+2}\to \cdots$

In particular, if the complex *E* is bounded below (the sheaf *E**j* is zero for *j* sufficiently negative), then *E* has an **injective resolution** *I* just as a single sheaf does. (By definition, *I* is a bounded below complex of injective sheaves with a chain map *E* → *I* that is a quasi-isomorphism.) Then the cohomology groups *H**j*(*X*,*E*) are defined as the cohomology of the complex of abelian groups

$\cdots \to I_{j}(X)\to I_{j+1}(X)\to I_{j+2}(X)\to \cdots .$

The cohomology of a space with coefficients in a complex of sheaves was earlier called hypercohomology, but usually now just "cohomology".

More generally, for any complex of sheaves *E* (not necessarily bounded below) on a space *X*, the cohomology group *H**j*(*X*,*E*) is defined as a group of morphisms in the derived category of sheaves on *X*:

$H^{j}(X,E)=\operatorname {Hom} _{D(X)}(\mathbf {Z} _{X},E[j]),$

where **Z***X* is the constant sheaf associated to the integers, and *E*[*j*] means the complex *E* shifted *j* steps to the left.

## Poincaré duality and generalizations

A central result in topology is the **Poincaré duality** theorem: for a closed oriented connected topological manifold *X* of dimension *n* and a field *k*, the group *H**n*(*X*,*k*) is isomorphic to *k*, and the cup product

$H^{j}(X,k)\times H^{n-j}(X,k)\to H^{n}(X,k)\cong k$

is a perfect pairing for all integers *j*. That is, the resulting map from *H**j*(*X*,*k*) to the dual space *H**n*−*j*(*X*,*k*)* is an isomorphism. In particular, the vector spaces *H**j*(*X*,*k*) and *H**n*−*j*(*X*,*k*)* have the same (finite) dimension.

Many generalizations are possible using the language of sheaf cohomology. If *X* is an oriented *n*-manifold, not necessarily compact or connected, and *k* is a field, then cohomology is the dual of cohomology with compact support:

$H^{j}(X,k)\cong H_{c}^{n-j}(X,k)^{*}.$

For any manifold *X* and field *k*, there is a sheaf *o**X* on *X*, the **orientation sheaf**, which is locally (but perhaps not globally) isomorphic to the constant sheaf *k*. One version of Poincaré duality for an arbitrary *n*-manifold *X* is the isomorphism:

$H^{j}(X,o_{X})\cong H_{c}^{n-j}(X,k)^{*}.$

More generally, if *E* is a locally constant sheaf of *k*-vector spaces on an *n*-manifold *X* and the stalks of *E* have finite dimension, then there is an isomorphism

$H^{j}(X,E^{*}\otimes o_{X})\cong H_{c}^{n-j}(X,E)^{*}.$

With coefficients in an arbitrary commutative ring rather than a field, Poincaré duality is naturally formulated as an isomorphism from cohomology to Borel–Moore homology.

**Verdier duality** is a vast generalization. For any locally compact space *X* of finite dimension and any field *k*, there is an object *D**X* in the derived category *D*(*X*) of sheaves on *X* called the **dualizing complex** (with coefficients in *k*). One case of Verdier duality is the isomorphism:

$H^{j}(X,D_{X})\cong H_{c}^{-j}(X,k)^{*}.$

For an *n*-manifold *X*, the dualizing complex *D**X* is isomorphic to the shift *o**X*[*n*] of the orientation sheaf. As a result, Verdier duality includes Poincaré duality as a special case.

**Alexander duality** is another useful generalization of Poincaré duality. For any closed subset *X* of an oriented *n*-manifold *M* and any field *k*, there is an isomorphism:

$H_{X}^{j}(M,k)\cong H_{c}^{n-j}(X,k)^{*}.$

This is interesting already for *X* a compact subset of *M* = **R***n*, where it says (roughly speaking) that the cohomology of **R***n*−*X* is the dual of the sheaf cohomology of *X*. In this statement, it is essential to consider sheaf cohomology rather than singular cohomology, unless one makes extra assumptions on *X* such as local contractibility.

## Higher direct images and the Leray spectral sequence

Let *f*: *X* → *Y* be a continuous map of topological spaces, and let *E* be a sheaf of abelian groups on *X*. The direct image sheaf *f***E* is the sheaf on *Y* defined by

$(f_{*}E)(U)=E(f^{-1}(U))$

for any open subset *U* of *Y*. For example, if *f* is the map from *X* to a point, then *f***E* is the sheaf on a point corresponding to the group *E*(*X*) of global sections of *E*.

The functor *f** from sheaves on *X* to sheaves on *Y* is left exact, but in general not right exact. The higher direct image sheaves R*i**f***E* on *Y* are defined as the right derived functors of the functor *f**. Another description is that R*i**f***E* is the sheaf associated to the presheaf

$U\mapsto H^{i}(f^{-1}(U),E)$

on *Y*. Thus, the higher direct image sheaves describe the cohomology of inverse images of small open sets in *Y*, roughly speaking.

The **Leray spectral sequence** relates cohomology on *X* to cohomology on *Y*. Namely, for any continuous map *f*: *X* → *Y* and any sheaf *E* on *X*, there is a spectral sequence

$E_{2}^{ij}=H^{i}(Y,R^{j}f_{*}E)\Rightarrow H^{i+j}(X,E).$

This is a very general result. The special case where *f* is a fibration and *E* is a constant sheaf plays an important role in homotopy theory under the name of the Serre spectral sequence. In that case, the higher direct image sheaves are locally constant, with stalks the cohomology groups of the fibers *F* of *f*, and so the Serre spectral sequence can be written as

$E_{2}^{ij}=H^{i}(Y,H^{j}(F,A))\Rightarrow H^{i+j}(X,A)$

for an abelian group *A*.

A simple but useful case of the Leray spectral sequence is that for any closed subset *X* of a topological space *Y* and any sheaf *E* on *X*, writing *f*: *X* → *Y* for the inclusion, there is an isomorphism

$H^{i}(Y,f_{*}E)\cong H^{i}(X,E).$

As a result, any question about sheaf cohomology on a closed subspace can be translated to a question about the direct image sheaf on the ambient space.

## Finiteness of cohomology

There is a strong finiteness result on sheaf cohomology. Let *X* be a compact Hausdorff space, and let *R* be a principal ideal domain, for example a field or the ring **Z** of integers. Let *E* be a sheaf of *R*-modules on *X*, and assume that *E* has "locally finitely generated cohomology", meaning that for each point *x* in *X*, each integer *j*, and each open neighborhood *U* of *x*, there is an open neighborhood *V* ⊂ *U* of *x* such that the image of *H**j*(*U*,*E*) → *H**j*(*V*,*E*) is a finitely generated *R*-module. Then the cohomology groups *H**j*(*X*,*E*) are finitely generated *R*-modules.

For example, for a compact Hausdorff space *X* that is locally contractible (in the weak sense discussed above), the sheaf cohomology group *H**j*(*X*,**Z**) is finitely generated for every integer *j*.

One case where the finiteness result applies is that of a constructible sheaf. Let *X* be a topologically stratified space. In particular, *X* comes with a sequence of closed subsets

$X=X_{n}\supset X_{n-1}\supset \cdots \supset X_{-1}=\emptyset$

such that each difference *X**i*−*X**i*−1 is a topological manifold of dimension *i*. A sheaf *E* of *R*-modules on *X* is **constructible** with respect to the given stratification if the restriction of *E* to each stratum *X**i*−*X**i*−1 is locally constant, with stalk a finitely generated *R*-module. A sheaf *E* on *X* that is constructible with respect to the given stratification has locally finitely generated cohomology. If *X* is compact, it follows that the cohomology groups *H**j*(*X*,*E*) of *X* with coefficients in a constructible sheaf are finitely generated.

More generally, suppose that *X* is compactifiable, meaning that there is a compact stratified space *W* containing *X* as an open subset, with *W*–*X* a union of connected components of strata. Then, for any constructible sheaf *E* of *R*-modules on *X*, the *R*-modules *H**j*(*X*,*E*) and *H**c**j*(*X*,*E*) are finitely generated. For example, any complex algebraic variety *X*, with its classical (Euclidean) topology, is compactifiable in this sense.

## Cohomology of coherent sheaves

In algebraic geometry and complex analytic geometry, coherent sheaves are a class of sheaves of particular geometric importance. For example, an algebraic vector bundle (on a locally Noetherian scheme) or a holomorphic vector bundle (on a complex analytic space) can be viewed as a coherent sheaf, but coherent sheaves have the advantage over vector bundles that they form an abelian category. On a scheme, it is also useful to consider the quasi-coherent sheaves, which include the locally free sheaves of infinite rank.

A great deal is known about the cohomology groups of a scheme or complex analytic space with coefficients in a coherent sheaf. This theory is a key technical tool in algebraic geometry. Among the main theorems are results on the vanishing of cohomology in various situations, results on finite-dimensionality of cohomology, comparisons between coherent sheaf cohomology and singular cohomology such as Hodge theory, and formulas on Euler characteristics in coherent sheaf cohomology such as the Riemann–Roch theorem.

## Sheaves on a site

In the 1960s, Grothendieck defined the notion of a **site**, meaning a category equipped with a Grothendieck topology. A site *C* axiomatizes the notion of a set of morphisms *V*α → *U* in *C* being a *covering* of *U*. A topological space *X* determines a site in a natural way: the category *C* has objects the open subsets of *X*, with morphisms being inclusions, and with a set of morphisms *V*α → *U* being called a covering of *U* if and only if *U* is the union of the open subsets *V*α. The motivating example of a Grothendieck topology beyond that case was the étale topology on schemes. Since then, many other Grothendieck topologies have been used in algebraic geometry: the fpqc topology, the Nisnevich topology, and so on.

The definition of a sheaf works on any site. So one can talk about a sheaf of sets on a site, a sheaf of abelian groups on a site, and so on. The definition of sheaf cohomology as a derived functor also works on a site. So one has sheaf cohomology groups *H**j*(*X*, *E*) for any object *X* of a site and any sheaf *E* of abelian groups. For the étale topology, this gives the notion of étale cohomology, which led to the proof of the Weil conjectures. Crystalline cohomology and many other cohomology theories in algebraic geometry are also defined as sheaf cohomology on an appropriate site.

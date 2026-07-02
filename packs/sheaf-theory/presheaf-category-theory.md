---
title: "Presheaf (category theory)"
source: https://en.wikipedia.org/wiki/Presheaf_(category_theory)
domain: sheaf-theory
license: CC-BY-SA-4.0
tags: sheaf theory, sheaf cohomology, grothendieck topology, ringed space
fetched: 2026-07-02
---

# Presheaf (category theory)

In category theory, a branch of mathematics, a **presheaf** on a category C is a functor $F\colon C^{\mathrm {op} }\to \mathbf {Set}$ . If C is the poset of open sets in a topological space, interpreted as a category, then one recovers the usual notion of presheaf on a topological space.

A morphism of presheaves is defined to be a natural transformation of functors. This makes the collection of all presheaves on C into a category, and is an example of a functor category. It is often written as ${\widehat {C}}=\mathbf {Set} ^{C^{\mathrm {op} }}$ and it is called the **category of presheaves** on C . A functor into ${\widehat {C}}$ is sometimes called a profunctor.

A presheaf that is naturally isomorphic to the contravariant hom-functor Hom(–, *A*) for some object *A* of **C** is called a representable presheaf.

Some authors refer to a functor $F\colon C^{\mathrm {op} }\to \mathbf {V}$ as a **$\mathbf {V}$ -valued presheaf**.

## Examples

- A simplicial set is a **Set**-valued presheaf on the simplex category $C=\Delta$ .
- A directed multigraph is a presheaf on the category with two objects and two parallel morphisms between them i.e. $C=(E{\overset {s}{\underset {t}{\longrightarrow }}}V)$ .
- An arrow category is a presheaf on the category with two objects and one morphism between them. i.e. $C=(E{\overset {f}{\longrightarrow }}V)$ .
- A right group action is a presheaf on the category created from a group G , i.e. a category with one object and invertible morphisms.

## Properties

- When C is a small category, the functor category ${\widehat {C}}=\mathbf {Set} ^{C^{\mathrm {op} }}$ is cartesian closed.
- The poset of subobjects of P form a Heyting algebra, whenever P is an object of ${\widehat {C}}=\mathbf {Set} ^{C^{\mathrm {op} }}$ for small C .
- For any morphism $f:X\to Y$ of ${\widehat {C}}$ , the pullback functor of subobjects $f^{*}:\mathrm {Sub} _{\widehat {C}}(Y)\to \mathrm {Sub} _{\widehat {C}}(X)$ has a right adjoint, denoted $\forall _{f}$ , and a left adjoint, $\exists _{f}$ . These are the universal and existential quantifiers.
- A locally small category C embeds fully and faithfully into the category ${\widehat {C}}$ of set-valued presheaves via the Yoneda embedding which to every object A of C associates the hom functor $C(-,A)$ .
- The category ${\widehat {C}}$ admits small limits and small colimits. See limit and colimit of presheaves for further discussion.
- The density theorem states that every presheaf is a colimit of representable presheaves; in fact, ${\widehat {C}}$ is the colimit completion of C (see #Universal property below.)

## Universal property

The construction $C\mapsto {\widehat {C}}=\mathbf {Fct} (C^{\text{op}},\mathbf {Set} )$ is called the **colimit completion** of *C* because of the following universal property:

**Proposition**—Let *C*, *D* be categories and assume *D* admits small colimits. Then each functor $\eta :C\to D$ factorizes as

$C{\overset {y}{\longrightarrow }}{\widehat {C}}{\overset {\widetilde {\eta }}{\longrightarrow }}D$

where *y* is the Yoneda embedding and ${\widetilde {\eta }}:{\widehat {C}}\to D$ is a, unique up to isomorphism, colimit-preserving functor called the **Yoneda extension** of $\eta$ .

*Proof*: Given a presheaf *F*, by the density theorem, we can write $F=\varinjlim yU_{i}$ where $U_{i}$ are objects in *C*. Then let ${\widetilde {\eta }}F=\varinjlim \eta U_{i},$ which exists by assumption. Since $\varinjlim -$ is functorial, this determines the functor ${\widetilde {\eta }}:{\widehat {C}}\to D$ . Succinctly, ${\widetilde {\eta }}$ is the left Kan extension of $\eta$ along *y*; hence, the name "Yoneda extension". To see ${\widetilde {\eta }}$ commutes with small colimits, we show ${\widetilde {\eta }}$ is a left-adjoint (to some functor). Define ${\mathcal {H}}om(\eta ,-):D\to {\widehat {C}}$ to be the functor given by: for each object *M* in *D* and each object *U* in *C*,

${\mathcal {H}}om(\eta ,M)(U)=\operatorname {Hom} _{D}(\eta U,M).$

Then, for each object *M* in *D*, since ${\mathcal {H}}om(\eta ,M)(U_{i})=\operatorname {Hom} (yU_{i},{\mathcal {H}}om(\eta ,M))$ by the Yoneda lemma, we have:

${\begin{aligned}\operatorname {Hom} _{D}({\widetilde {\eta }}F,M)&=\operatorname {Hom} _{D}(\varinjlim \eta U_{i},M)=\varprojlim \operatorname {Hom} _{D}(\eta U_{i},M)=\varprojlim {\mathcal {H}}om(\eta ,M)(U_{i})\\&=\operatorname {Hom} _{\widehat {C}}(F,{\mathcal {H}}om(\eta ,M)),\end{aligned}}$

which is to say ${\widetilde {\eta }}$ is a left-adjoint to ${\mathcal {H}}om(\eta ,-)$ . $\square$

The proposition yields several corollaries. For example, the proposition implies that the construction $C\mapsto {\widehat {C}}$ is functorial: i.e., each functor $C\to D$ determines the functor ${\widehat {C}}\to {\widehat {D}}$ .

## Variants

A **presheaf of spaces** on an ∞-category *C* is a contravariant functor from *C* to the ∞-category of spaces (for example, the nerve of the category of CW-complexes.) It is an ∞-category version of a presheaf of sets, as a "set" is replaced by a "space". The notion is used, among other things, in the ∞-category formulation of Yoneda's lemma that says: $C\to {\widehat {C}}$ is fully faithful (here *C* can be just a simplicial set.)

A **copresheaf** of a category *C* is a presheaf of *Cop*. In other words, it is a covariant functor from *C* to *Set*.

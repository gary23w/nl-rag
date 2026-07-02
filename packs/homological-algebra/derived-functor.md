---
title: "Derived functor"
source: https://en.wikipedia.org/wiki/Derived_functor
domain: homological-algebra
license: CC-BY-SA-4.0
tags: homological algebra, chain complex, exact sequence, derived functor
fetched: 2026-07-02
---

# Derived functor

In mathematics, specifically category theory, certain functors may be *derived* to obtain other functors closely related to the original ones. This operation, while fairly abstract, unifies a number of constructions throughout mathematics.

## Motivation

It was noted in various quite different settings that a short exact sequence often gives rise to a "long exact sequence". **Derived functors** clarify and generalize many of these observations.

Suppose we are given a covariant left exact functor $F:\mathbf {A} \to \mathbf {B}$ between two abelian categories $\mathbf {A}$ and $\mathbf {B}$ . If

$0\to A\to B\to C\to 0$

is a short exact sequence in $\mathbf {A}$ , then applying F yields the exact sequence

$0\to F(A)\to F(B)\to F(C)$

,

and one could ask how to continue this sequence to the right to form a long exact sequence.

Strictly speaking, this question is ill-posed, since there are always numerous different ways to continue a given exact sequence to the right. However, it turns out that if $\mathbf {A}$ is "nice enough", there is one canonical way of doing so, given by the right derived functors of F . For every $i\geq 1$ , there is a functor $R^{i}F:\mathbf {A} \to \mathbf {B}$ , and the above sequence continues like so:

$0\to F(A)\to F(B)\to F(C)\to R^{1}F(A)\to R^{1}F(B)\to R^{1}F(C)\to R^{2}F(A)\to R^{2}F(B)\to \cdots$

From this we see that F is an exact functor if and only if $R^{1}F=0$ ; so in a sense the right derived functors of F measure "how far" F is from being exact.

If the object A in the above short exact sequence is injective, then the sequence splits. Applying any additive functor to a split sequence results in a split sequence, so in particular $R^{1}F(A)=0$ . Right derived functors (for $i>0$ ) are zero on injectives: this is the motivation for the construction given below.

## Construction and first properties

The crucial assumption we need to make about our abelian category **A** is that it has *enough injectives*, meaning that for every object *A* in **A** there exists a monomorphism *A* → *I* where *I* is an injective object in **A**.

The right derived functors of the covariant left-exact functor *F* : **A** → **B** are then defined as follows. Start with an object *X* of **A**. Because there are enough injectives, we can construct a long exact sequence of the form

$0\to X\to I^{0}\to I^{1}\to I^{2}\to \cdots$

where the *I* *i* are all injective (this is known as an *injective resolution* of *X*). Applying the functor *F* to this sequence, and chopping off the first term, we obtain the cochain complex

$0\to F(I^{0})\to F(I^{1})\to F(I^{2})\to \cdots$

Note: this is in general *not* an exact sequence anymore. But we can compute its cohomology at the *i*-th spot (the kernel of the map from *F*(*I**i*) modulo the image of the map to *F*(*I**i*)); we call the result *RiF*(*X*). Of course, various things have to be checked: the result does not depend on the given injective resolution of *X*, and any morphism *X* → *Y* naturally yields a morphism *RiF*(*X*) → *RiF*(*Y*), so that we indeed obtain a functor. Note that left exactness means that 0 → *F*(*X*) → *F*(*I*0) → *F*(*I*1) is exact, so *R*0*F*(*X*) = *F*(*X*), so we only get something interesting for *i*>0.

(Technically, to produce well-defined derivatives of *F*, we would have to fix an injective resolution for every object of **A**. This choice of injective resolutions then yields functors *RiF*. Different choices of resolutions yield naturally isomorphic functors, so in the end the choice doesn't really matter.)

The above-mentioned property of turning short exact sequences into long exact sequences is a consequence of the snake lemma. This tells us that the collection of derived functors is a δ-functor.

If *X* is itself injective, then we can choose the injective resolution 0 → *X* → *X* → 0, and we obtain that *RiF*(*X*) = 0 for all *i* ≥ 1. In practice, this fact, together with the long exact sequence property, is often used to compute the values of right derived functors.

An equivalent way to compute *RiF*(*X*) is the following: take an injective resolution of *X* as above, and let *K**i* be the image of the map *I**i*-1→*Ii* (for *i*=0, define *I**i*-1=0), which is the same as the kernel of *I**i*→*I**i*+1. Let φ*i* : *I**i*-1→*K**i* be the corresponding surjective map. Then *RiF*(*X*) is the cokernel of *F*(φ*i*).

## Variations

If one starts with a covariant *right-exact* functor G , and the category **A** has enough projectives (i.e. for every object A of **A** there exists an epimorphism $P\rightarrow A$ where P is a projective object), then one can define analogously the left-derived functors $L_{i}G$ . For an object X of **A** we first construct a projective resolution of the form

$\cdots \to P_{2}\to P_{1}\to P_{0}\to X\to 0$

where the $P_{i}$ are projective. We apply G to this sequence, chop off the last term, and compute homology to get $L_{i}G(X)$ . As before, $L_{0}G(X)=G(X)$ .

In this case, the long exact sequence will grow "to the left" rather than to the right:

$0\to A\to B\to C\to 0$

is turned into

$\cdots \to L_{2}G(C)\to L_{1}G(A)\to L_{1}G(B)\to L_{1}G(C)\to G(A)\to G(B)\to G(C)\to 0$

.

Left derived functors are zero on all projective objects.

One may also start with a *contravariant* left-exact functor F ; the resulting right-derived functors are then also contravariant. The short exact sequence

$0\to A\to B\to C\to 0$

is turned into the long exact sequence

$0\to F(C)\to F(B)\to F(A)\to R^{1}F(C)\to R^{1}F(B)\to R^{1}F(A)\to R^{2}F(C)\to \cdots$

These right derived functors are zero on projectives and are therefore computed via projective resolutions.

## Examples

- If A is an abelian category, then its category of morphisms $A^{\{\ast \to \ast \}}$ is also abelian. The functor $\ker :A^{\{\ast \to \ast \}}\to A$ which maps each morphism to its kernel is left exact. Its right derived functors are

$R^{i}(\ker )(f)={\begin{cases}\ker(f)&i=0\\\operatorname {coker} (f)&i=1\\0&i>1\end{cases}}$

Dually the functor

$\operatorname {coker}$

is right exact and its left derived functors are

$L_{i}(\operatorname {coker} )(f)={\begin{cases}\operatorname {coker} (f)&i=0\\\ker(f)&i=1\\0&i>1\end{cases}}$

This is a manifestation of the

snake lemma

.

### Homology and cohomology

#### Sheaf cohomology

If X is a topological space, then the category $Sh(X)$ of all sheaves of abelian groups on X is an abelian category with enough injectives. The functor $\Gamma :Sh(X)\to Ab$ which assigns to each such sheaf ${\mathcal {F}}$ the group $\Gamma ({\mathcal {F}}):={\mathcal {F}}(X)$ of global sections is left exact, and the right derived functors are the sheaf cohomology functors, usually written as $H^{i}(X,{\mathcal {F}})$ . Slightly more generally: if $(X,{\mathcal {O}}_{X})$ is a ringed space, then the category of all sheaves of ${\mathcal {O}}_{X}$ -modules is an abelian category with enough injectives, and we can again construct sheaf cohomology as the right derived functors of the global section functor.

There are various notions of cohomology which are a special case of this:

- **De Rham cohomology** is the sheaf cohomology of the sheaf of locally constant $\mathbb {R}$ -valued functions on a manifold. The De Rham complex is a resolution of this sheaf not by injective sheaves, but by fine sheaves.
- **Étale cohomology** is another cohomology theory for sheaves over a scheme. It is the right derived functor of the global sections of abelian sheaves on the étale site.

#### Ext functors

If R is a ring, then the category of all left R -modules is an abelian category with enough injectives. If A is a fixed left R -module, then the functor $\operatorname {Hom} (A,-):R{\text{-Mod}}\to {\mathfrak {Ab}}$ is left exact, and its right derived functors are the Ext functors $\operatorname {Ext} _{R}^{i}(A,-)$ . Alternatively $\operatorname {Ext} _{R}^{i}(-,B)$ can also be obtained as the left derived functor of the right exact functor $\operatorname {Hom} _{R}(-,B):R{\text{-Mod}}\to {\mathfrak {Ab}}^{op}$ .

Various notions of cohomology are special cases of Ext functors and therefore also derived functors.

- **Group cohomology** is the right derived functor of the invariants functor $(-)^{G}:k[G]{\text{-Mod}}\to k[G]{\text{-Mod}}$ which is the same as $\operatorname {Hom} _{k[G]}(k,-)$ (where k is the trivial $k[G]$ -module) and therefore $H^{i}(G,M)=\operatorname {Ext} _{k[G]}^{i}(k,M)$ .
- **Lie algebra cohomology** of a Lie algebra ${\mathfrak {g}}$ over some commutative ring k is the right derived functor of the invariants functor $(-)^{\mathfrak {g}}:{\mathfrak {g}}{\text{-Mod}}\to k{\text{-Mod}}$ which is the same as $\operatorname {Hom} _{U({\mathfrak {g}})}(k,-)$ (where k is again the trivial ${\mathfrak {g}}$ -module and $U({\mathfrak {g}})$ is the universal enveloping algebra of ${\mathfrak {g}}$ ). Therefore $H^{i}({\mathfrak {g}},M)=\operatorname {Ext} _{U({\mathfrak {g}})}^{i}(k,M)$ .
- **Hochschild cohomology** of some k -algebra A is the right derived functor of invariants $(-)^{A}:(A,A){\text{-Bimod}}\to k{\text{-Mod}}$ mapping a bimodule M to its center, also called its set of invariants $M^{A}:=Z(M):=\{m\in M\mid \forall a\in A:am=ma\}$ which is the same as $\operatorname {Hom} _{A^{e}}(A,M)$ (where $A^{e}:=A\otimes _{k}A^{op}$ is the enveloping algebra of A and A is considered an $(A,A)$ -bimodule via the usual left and right multiplication). Therefore $HH^{i}(A,M)=\operatorname {Ext} _{A^{e}}^{i}(A,M)$ :

#### Tor functors

The category of left R -modules also has enough projectives. If A is a fixed right R -module, then the tensor product with A gives a right exact covariant functor $A\otimes _{R}-:R{\text{-Mod}}\to Ab$ ; The category of modules has enough projectives so that left derived functors always exists. The left derived functors of the tensor functor are the Tor functors $\operatorname {Tor} _{i}^{R}(A,-)$ . Equivalently $\operatorname {Tor} _{i}^{R}(-,B)$ can be defined symmetrically as the left derived functors of $-\otimes B$ . In fact one can combine both definitions and define $\operatorname {Tor} _{i}^{R}(-,-)$ as the left derived of $-\otimes -:{\text{Mod-}}R\times R{\text{-Mod}}\to Ab$ .

This includes several notions of homology as special cases. This often mirrors the situation with Ext functors and cohomology.

- **Group homology** is the left derived functor of taking coinvariants $(-)_{G}:k[G]{\text{-Mod}}\to k{\text{-Mod}}$ which is the same as $k\otimes _{k[G]}-$ .
- **Lie algebra homology** is the left derived functor of taking coinvariants ${\mathfrak {g}}{\text{-Mod}}\to k{\text{-Mod}},M\mapsto M/[{\mathfrak {g}},M]$ which is the same as $k\otimes _{U({\mathfrak {g}})}-$ .
- **Hochschild homology** is the left derived functor of taking coinvariants $(A,A){\text{-Bimod}}\to k{\text{-Mod}},M\mapsto M/[A,M]$ which is the same as $A\otimes _{A^{e}}-$ .

Instead of taking individual left derived functors one can also take the total derived functor of the tensor functor. This gives rise to the derived tensor product $-\otimes ^{L}-:D({\text{Mod-}}R)\times D(R{\text{-Mod}})\to D(Ab)$ where D is the derived category.

## Naturality

Derived functors and the long exact sequences are "natural" in several technical senses.

First, given a commutative diagram of the form

${\begin{array}{ccccccccc}0&\to &A_{1}&{\xrightarrow {f_{1}}}&B_{1}&{\xrightarrow {g_{1}}}&C_{1}&\to &0\\&&\alpha \downarrow \quad &&\beta \downarrow \quad &&\gamma \downarrow \quad &&\\0&\to &A_{2}&{\xrightarrow {f_{2}}}&B_{2}&{\xrightarrow {g_{2}}}&C_{2}&\to &0\end{array}}$

(where the rows are exact), the two resulting long exact sequences are related by commuting squares:

Second, suppose η : *F* → *G* is a natural transformation from the left exact functor *F* to the left exact functor *G*. Then natural transformations *Ri*η : *RiF* → *RiG* are induced, and indeed *Ri* becomes a functor from the functor category of all left exact functors from **A** to **B** to the full functor category of all functors from **A** to **B**. Furthermore, this functor is compatible with the long exact sequences in the following sense: if $0\to A\xrightarrow {f} B\xrightarrow {g} C\to 0$ is a short exact sequence, then a commutative diagram

is induced.

Both of these naturalities follow from the naturality of the sequence provided by the snake lemma.

Conversely, the following characterization of derived functors holds: given a family of functors *R**i*: **A** → **B**, satisfying the above, i.e. mapping short exact sequences to long exact sequences, such that for every injective object *I* of **A**, *R**i*(*I*)=0 for every positive *i*, then these functors are the right derived functors of *R*0.

## Generalization

The more modern (and more general) approach to derived functors uses the language of derived categories.

In 1968 Quillen developed the theory of model categories, which give an abstract category-theoretic system of fibrations, cofibrations and weak equivalences. Typically one is interested in the underlying homotopy category obtained by localizing against the weak equivalences. A Quillen adjunction is an adjunction between model categories that descends to an adjunction between the homotopy categories. For example, the category of topological spaces and the category of simplicial sets both admit Quillen model structures whose nerve and realization adjunction gives a Quillen adjunction that is in fact an equivalence of homotopy categories. Particular objects in a model structure have “nice properties” (concerning the existence of lifts against particular morphisms), the “fibrant” and “cofibrant” objects, and every object is weakly equivalent to a fibrant-cofibrant “resolution.”

Although originally developed to handle the category of topological spaces Quillen model structures appear in numerous places in mathematics; in particular the category of chain complexes from any Abelian category (modules, sheaves of modules on a topological space or scheme, etc.) admit a model structure whose weak equivalences are those morphisms between chain complexes preserving homology. Often we have a functor between two such model categories (e.g. the global sections functor sending a complex of Abelian sheaves to the obvious complex of Abelian groups) that preserves weak equivalences *within the subcategory of “good” (fibrant or cofibrant) objects*. By first taking a fibrant or cofibrant resolution of an object and then applying that functor, we have successfully extended it to the whole category in such a way that weak equivalences are always preserved (and hence it descends to a functor from the homotopy category). This is the “derived functor.” The “derived functors” of sheaf cohomology, for example, are the homologies of the output of this derived functor. Applying these to a sheaf of Abelian groups interpreted in the obvious way as a complex concentrated in homology, they measure the failure of the global sections functor to preserve weak equivalences of such, its failure of “exactness.” General theory of model structures shows the uniqueness of this construction (that it does not depend of choice of fibrant or cofibrant resolution, etc.)

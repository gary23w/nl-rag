---
title: "Natural transformation"
source: https://en.wikipedia.org/wiki/Natural_transformation
domain: monad-transformers
license: CC-BY-SA-4.0
tags: monad transformer, monad stack, kleisli category, free monad
fetched: 2026-07-02
---

# Natural transformation

In category theory, a branch of mathematics, a **natural transformation** provides a way of transforming one functor into another while respecting the internal structure (i.e., the composition of morphisms) of the categories involved. Hence, a natural transformation can be considered to be a "morphism of functors". Informally, the notion of a natural transformation states that a particular map between functors can be done consistently over an entire category.

Indeed, this intuition can be formalized to define so-called functor categories. Natural transformations are, after categories and functors, one of the most fundamental notions of category theory and consequently appear in the majority of its applications.

## Definition

If F and G are functors between the categories ${\mathcal {C}}$ and ${\mathcal {D}}$ (both from ${\mathcal {C}}$ to ${\mathcal {D}}$ ), then a **natural transformation** $\eta$ from F to G is a family of morphisms $(\eta _{X})_{X\in {\text{ob}}({\mathcal {C}})}$ , where $\eta _{X}:F(X)\to G(X)$ . The morphism $\eta _{X}$ is called "the **component** of $\eta$ at X " or "the X component of $\eta$ ." The components of $\eta$ are such that for every morphism $f:X\to Y$ in ${\mathcal {C}}$ we have $\eta _{Y}\circ F(f)=G(f)\circ \eta _{X}.$

This equation can be conveniently expressed by the following commutative diagram:

If both F and G are instead contravariant functors, the vertical arrows in the right diagram are reversed. If $\eta$ is a natural transformation from F to G , we also write $\eta :F\to G$ or $\eta :F\Rightarrow G$ . This is also expressed by saying the family of morphisms $\eta _{X}:F(X)\to G(X)$ is **natural** in X .

If, for every object X in ${\mathcal {C}}$ , the morphism $\eta _{X}$ is an isomorphism in ${\mathcal {D}}$ , then $\eta$ is said to be a **natural isomorphism** (or sometimes **natural equivalence** or **isomorphism of functors**). Two functors F and G are called *naturally isomorphic* or simply *isomorphic* if there exists a natural isomorphism from F to G in their category.

An **infranatural transformation** $\eta :F\Rightarrow G$ is simply the family of components for all X in ${\mathcal {C}}$ . Thus, a natural transformation is a special case of an infranatural transformation for which $\eta _{Y}\circ F(f)=G(f)\circ \eta _{X}$ for every morphism $f:X\to Y$ in ${\mathcal {C}}$ . The **naturalizer** of $\eta$ , $\operatorname {nat} (\eta )$ , is the largest subcategory ${\mathcal {C}}_{S}\subseteq {\mathcal {C}}$ (S for subcategory) containing all the objects of ${\mathcal {C}}$ on which $\eta$ restricts to a natural transformation. Alternatively put, $\operatorname {nat} (\eta )$ is the largest ${\mathcal {C}}_{S}\subseteq {\mathcal {C}}$ such that ${\displaystyle \,\eta |_{{\mathcal {C}}_{S}}\$ .

## Examples

### Opposite group

Statements such as

"Every group is naturally isomorphic to its

opposite group

"

abound in modern mathematics. We will now give the precise meaning of this statement as well as its proof. Consider the category ${\textbf {Grp}}$ of all groups with group homomorphisms as morphisms. If $(G,*)$ is a group, we define its opposite group $(G^{\text{op}},{*}^{\text{op}})$ as follows: $G^{\text{op}}$ is the same set as G , and the operation $*^{\text{op}}$ is defined by $a*^{\text{op}}b=b*a$ . All multiplications in $G^{\text{op}}$ are thus "turned around". Forming the opposite group becomes a (covariant) functor from ${\textbf {Grp}}$ to ${\textbf {Grp}}$ if we define $f^{\text{op}}=f$ for any group homomorphism $f:G\to H$ . Note that $f^{\text{op}}$ is indeed a group homomorphism from $G^{\text{op}}$ to $H^{\text{op}}$ :

$f^{\text{op}}(a*^{\text{op}}b)=f(b*a)=f(b)*f(a)=f^{\text{op}}(a)*^{\text{op}}f^{\text{op}}(b).$

The content of the above statement is:

"The identity functor

${\text{Id}}_{\textbf {Grp}}:{\textbf {Grp}}\to {\textbf {Grp}}$

is naturally isomorphic to the opposite functor

${\text{op}}:{\textbf {Grp}}\to {\textbf {Grp}}$

"

To prove this, we need to provide isomorphisms $\eta _{G}:G\to G^{\text{op}}$ for every group G , such that the above diagram commutes. Set $\eta _{G}(a)=a^{-1}$ . The formulas $(a*b)^{-1}=b^{-1}*a^{-1}=a^{-1}*^{\text{op}}b^{-1}$ and $(a^{-1})^{-1}=a$ show that $\eta _{G}$ is a group homomorphism with inverse $\eta _{G^{\text{op}}}$ . To prove the naturality, we start with a group homomorphism $f:G\to H$ and show $\eta _{H}\circ f=f^{\text{op}}\circ \eta _{G}$ , i.e. $(f(a))^{-1}=f^{\text{op}}(a^{-1})$ for all a in G . This is true since $f^{\text{op}}=f$ and every group homomorphism has the property $(f(a))^{-1}=f(a^{-1})$ .

### Abelianization

Given a group G , we can define its abelianization $G^{\text{ab}}=G/[G,G]$ , where $[G,G]$ denotes the commutator subgroup of G . Let $\pi _{G}:G\to G^{\text{ab}}$ denote the projection map onto the cosets of $[G,G]$ . This homomorphism is "natural in G ", i.e., it defines a natural transformation, which we now check. Let H be a group. For any homomorphism $f:G\to H$ , we have that $[G,G]$ is contained in the kernel of $\pi _{H}\circ f$ , because any homomorphism into an abelian group kills the commutator subgroup. Then $\pi _{H}\circ f$ factors through $G^{\text{ab}}$ as $f^{\text{ab}}\circ \pi _{G}=\pi _{H}\circ f$ for a unique homomorphism $f^{\text{ab}}:G^{\text{ab}}\to H^{\text{ab}}$ . This makes ${\text{ab}}:{\textbf {Grp}}\to {\textbf {Grp}}$ a functor and $\pi$ a natural transformation, but not a natural isomorphism, from the identity functor to ${\text{ab}}$ .

### Hurewicz homomorphism

Functors and natural transformations abound in algebraic topology, with the Hurewicz homomorphisms serving as examples. For any pointed topological space $(X,x)$ and positive integer n there exists a group homomorphism

$h_{n}\colon \pi _{n}(X,x)\to H_{n}(X)$

from the n -th homotopy group of $(X,x)$ to the n -th homology group of X . Both $\pi _{n}$ and $H_{n}$ are functors from the category **Top*** of pointed topological spaces to the category **Grp** of groups, and $h_{n}$ is a natural transformation from $\pi _{n}$ to $H_{n}$ .

### Determinant

Given commutative rings R and S with a ring homomorphism $f:R\to S$ , the respective groups of invertible $n\times n$ matrices ${\text{GL}}_{n}(R)$ and ${\text{GL}}_{n}(S)$ inherit a homomorphism which we denote by ${\text{GL}}_{n}(f)$ , obtained by applying f to each matrix entry. Similarly, f restricts to a group homomorphism $f^{*}:R^{*}\to S^{*}$ , where $R^{*}$ denotes the group of units of R . In fact, ${\text{GL}}_{n}$ and * are functors from the category of commutative rings ${\textbf {CRing}}$ to ${\textbf {Grp}}$ . The determinant on the group ${\text{GL}}_{n}(R)$ , denoted by ${\text{det}}_{R}$ , is a group homomorphism

${\mbox{det}}_{R}\colon {\mbox{GL}}_{n}(R)\to R^{*}$

which is natural in R : because the determinant is defined by the same formula for every ring, $f^{*}\circ {\text{det}}_{R}={\text{det}}_{S}\circ {\text{GL}}_{n}(f)$ holds. This makes the determinant a natural transformation from ${\text{GL}}_{n}$ to * .

### Double dual of a vector space

If K is a field, then for every vector space V over K we have a "natural" injective linear map $V\to V^{**}$ from the vector space into its double dual. These maps are "natural" in the following sense: the double dual operation is a functor, and the maps are the components of a natural transformation from the identity functor to the double dual functor.

### Finite calculus

For every abelian group G , the set ${\text{Hom}}_{\textbf {Set}}(\mathbb {Z} ,U(G))$ of functions from the integers to the underlying set of G forms an abelian group $V_{\mathbb {Z} }(G)$ under pointwise addition. (Here U is the standard forgetful functor $U:{\textbf {Ab}}\to {\textbf {Set}}$ .) Given an ${\textbf {Ab}}$ morphism $\varphi :G\to G'$ , the map $V_{\mathbb {Z} }(\varphi ):V_{\mathbb {Z} }(G)\to V_{\mathbb {Z} }(G')$ given by left composing $\varphi$ with the elements of the former is itself a homomorphism of abelian groups; in this way we obtain a functor $V_{\mathbb {Z} }:{\textbf {Ab}}\to {\textbf {Ab}}$ . The finite difference operator $\Delta _{G}$ taking each function $f:\mathbb {Z} \to U(G)$ to $\Delta (f):n\mapsto f(n+1)-f(n)$ is a map from $V_{\mathbb {Z} }(G)$ to itself, and the collection $\Delta$ of such maps gives a natural transformation $\Delta :V_{\mathbb {Z} }\to V_{\mathbb {Z} }$ .

### Tensor and Hom of modules

Let $\varphi :M\longrightarrow M^{\prime }$ be an R -module homomorphism of right modules. For every left module N there is a natural map $\varphi \otimes N:M\otimes _{R}N\longrightarrow M^{\prime }\otimes _{R}N$ , form a natural transformation $\eta :M\otimes _{R}-\implies M'\otimes _{R}-$ . For every right module N there is a natural map $\eta _{N}:{\text{Hom}}_{R}(M',N)\longrightarrow {\text{Hom}}_{R}(M,N)$ defined by $\eta _{N}(f)=f\varphi$ , form a natural transformation ${\displaystyle \eta$ .

### Tensor-hom adjunction

Consider the category ${\textbf {Ab}}$ of abelian groups and group homomorphisms. For all abelian groups X , Y and Z we have a group isomorphism

${\text{Hom}}(X\otimes Y,Z)\to {\text{Hom}}(X,{\text{Hom}}(Y,Z))$

.

These isomorphisms are "natural" in the sense that they define a natural transformation between the two involved functors ${\textbf {Ab}}^{\text{op}}\times {\textbf {Ab}}^{\text{op}}\times {\textbf {Ab}}\to {\textbf {Ab}}$ . (Here "op" is the opposite category of ${\textbf {Ab}}$ , not to be confused with the trivial opposite group functor on ${\textbf {Ab}}$  !)

This is formally the tensor-hom adjunction, and is an archetypal example of a pair of adjoint functors. Natural transformations arise frequently in conjunction with adjoint functors, and indeed, adjoint functors are defined by a certain natural isomorphism. Additionally, every pair of adjoint functors comes equipped with two natural transformations (generally not isomorphisms) called the *unit* and *counit*.

## Unnatural isomorphism

The notion of a natural transformation is categorical, and states (informally) that a particular map between functors can be done consistently over an entire category. Informally, a particular map (esp. an isomorphism) between individual objects (not entire categories) is referred to as a "natural isomorphism", meaning implicitly that it is actually defined on the entire category, and defines a natural transformation of functors; formalizing this intuition was a motivating factor in the development of category theory.

Conversely, a particular map between particular objects may be called an **unnatural isomorphism** (or "an isomorphism that is not natural") if the map cannot be extended to a natural transformation on the entire category. Given an object $X,$ a functor G (taking for simplicity the first functor to be the identity) and an isomorphism $\eta \colon X\to G(X),$ proof of unnaturality is most easily shown by giving an automorphism $A\colon X\to X$ that does not commute with this isomorphism (so $\eta \circ A\neq G(A)\circ \eta$ ). More strongly, if one wishes to prove that X and $G(X)$ are not naturally isomorphic, without reference to a particular isomorphism, this requires showing that for *any* isomorphism $\eta$ , there is some A with which it does not commute; in some cases a single automorphism A works for all candidate isomorphisms $\eta$ while in other cases one must show how to construct a different $A_{\eta }$ for each isomorphism. The maps of the category play a crucial role – any infranatural transform is natural if the only maps are the identity map, for instance.

This is similar (but more categorical) to concepts in group theory or module theory, where a given decomposition of an object into a direct sum is "not natural", or rather "not unique", as automorphisms exist that do not preserve the direct sum decomposition – see Structure theorem for finitely generated modules over a principal ideal domain § Uniqueness for example.

Some authors distinguish notationally, using $\cong$ for a natural isomorphism and $\approx$ for an unnatural isomorphism, reserving = for equality (usually equality of maps).

### Example: dual of a finite-dimensional vector space

Every finite-dimensional vector space is isomorphic to its dual space, but there may be many different isomorphisms between the two spaces. There is in general no natural isomorphism between a finite-dimensional vector space and its dual space. However, related categories (with additional structure and restrictions on the maps) do have a natural isomorphism, as described below.

The dual space of a finite-dimensional vector space is again a finite-dimensional vector space of the same dimension, and these are thus isomorphic, since dimension is the only invariant of finite-dimensional vector spaces over a given field. However, in the absence of additional constraints (such as a requirement that maps preserve the chosen basis), the map from a space to its dual is not unique, and thus such an isomorphism requires a choice, and is "not natural". On the category of finite-dimensional vector spaces and linear maps, one can define an infranatural isomorphism from vector spaces to their dual by choosing an isomorphism for each space (say, by choosing a basis for every vector space and taking the corresponding isomorphism), but this will not define a natural transformation. Intuitively this is because it required a choice, rigorously because *any* such choice of isomorphisms will not commute with, say, the zero map; see (Mac Lane & Birkhoff 1999, §VI.4) for detailed discussion.

Starting from finite-dimensional vector spaces (as objects) and the identity and dual functors, one can define a natural isomorphism, but this requires first adding additional structure, then restricting the maps from "all linear maps" to "linear maps that respect this structure". Explicitly, for each vector space, require that it comes with the data of an isomorphism to its dual, $\eta _{V}\colon V\to V^{*}$ . In other words, take as objects vector spaces with a nondegenerate bilinear form $b_{V}\colon V\times V\to K$ . This defines an infranatural isomorphism (isomorphism for each object). One then restricts the maps to only those maps $T\colon V\to U$ that commute with the isomorphisms: $T^{*}(\eta _{U}(T(v)))=\eta _{V}(v)$ or in other words, preserve the bilinear form: $b_{U}(T(v),T(w))=b_{V}(v,w)$ . (These maps define the *naturalizer* of the isomorphisms.) The resulting category, with objects finite-dimensional vector spaces with a nondegenerate bilinear form, and maps linear transforms that respect the bilinear form, by construction has a natural isomorphism from the identity to the dual (each space has an isomorphism to its dual, and the maps in the category are required to commute). Viewed in this light, this construction (add transforms for each object, restrict maps to commute with these) is completely general, and does not depend on any particular properties of vector spaces.

In this category (finite-dimensional vector spaces with a nondegenerate bilinear form, maps linear transforms that respect the bilinear form), the dual of a map between vector spaces can be identified as a transpose. Often for reasons of geometric interest this is specialized to a subcategory, by requiring that the nondegenerate bilinear forms have additional properties, such as being symmetric (orthogonal matrices), symmetric and positive definite (inner product space), symmetric sesquilinear (Hermitian spaces), skew-symmetric and totally isotropic (symplectic vector space), etc. – in all these categories a vector space is naturally identified with its dual, by the nondegenerate bilinear form.

## Operations with natural transformations

### Vertical composition

If $\eta :F\Rightarrow G$ and $\epsilon :G\Rightarrow H$ are natural transformations between functors $F,G,H:C\to D$ , then we can compose them to get a natural transformation $\epsilon \circ \eta :F\Rightarrow H$ . This is done component-wise:

$(\epsilon \circ \eta )_{X}=\epsilon _{X}\circ \eta _{X}$

.

This vertical composition of natural transformations is associative and has an identity, and allows one to consider the collection of all functors $C\to D$ itself as a category (see below under Functor categories). The identity natural transformation $\mathrm {id} _{F}$ on functor F has components $(\mathrm {id} _{F})_{X}=\mathrm {id} _{F(X)}$ .

For

$\eta :F\Rightarrow G$

,

$\mathrm {id} _{G}\circ \eta =\eta =\eta \circ \mathrm {id} _{F}$

.

### Horizontal composition

If $\eta :F\Rightarrow G$ is a natural transformation between functors $F,G:C\to D$ and $\epsilon :J\Rightarrow K$ is a natural transformation between functors $J,K:D\to E$ , then the composition of functors allows a composition of natural transformations $\epsilon *\eta :J\circ F\Rightarrow K\circ G$ with components

$(\epsilon *\eta )_{X}=\epsilon _{G(X)}\circ J(\eta _{X})=K(\eta _{X})\circ \epsilon _{F(X)}$

.

By using whiskering (see below), we can write

$(\epsilon *\eta )_{X}=(\epsilon G)_{X}\circ (J\eta )_{X}=(K\eta )_{X}\circ (\epsilon F)_{X}$

,

hence

$\epsilon *\eta =\epsilon G\circ J\eta =K\eta \circ \epsilon F$

.

This horizontal composition of natural transformations is also associative with identity. This identity is the identity natural transformation on the identity functor, i.e., the natural transformation that associate to each object its identity morphism: for object X in category C , $(\mathrm {id} _{\mathrm {id} _{C}})_{X}=\mathrm {id} _{\mathrm {id} _{C}(X)}=\mathrm {id} _{X}$ .

For

$\eta :F\Rightarrow G$

with

$F,G:C\to D$

,

$\mathrm {id} _{\mathrm {id} _{D}}*\eta =\eta =\eta *\mathrm {id} _{\mathrm {id} _{C}}$

.

As identity functors $\mathrm {id} _{C}$ and $\mathrm {id} _{D}$ are functors, the identity for horizontal composition is also the identity for vertical composition, but not vice versa.

### Whiskering

Whiskering is an external binary operation between a functor and a natural transformation.

If $\eta :F\Rightarrow G$ is a natural transformation between functors $F,G:C\to D$ , and $H:D\to E$ is another functor, then we can form the natural transformation $H\eta :H\circ F\Rightarrow H\circ G$ by defining

$(H\eta )_{X}=H(\eta _{X})$

.

If on the other hand $K:B\to C$ is a functor, the natural transformation $\eta K:F\circ K\Rightarrow G\circ K$ is defined by

$(\eta K)_{X}=\eta _{K(X)}$

.

It's also a horizontal composition where one of the natural transformations is the identity natural transformation:

$H\eta =\mathrm {id} _{H}*\eta$

and

$\eta K=\eta *\mathrm {id} _{K}$

.

Note that $\mathrm {id} _{H}$ (resp. $\mathrm {id} _{K}$ ) is generally not the left (resp. right) identity of horizontal composition * ( $H\eta \neq \eta$ and $\eta K\neq \eta$ in general), except if H (resp. K ) is the identity functor of the category D (resp. C ).

### Interchange law

The two operations are related by an identity which exchanges vertical composition with horizontal composition: if we have four natural transformations $\alpha ,\alpha ',\beta ,\beta '$ as shown on the image to the right, then the following identity holds:

$(\beta '\circ \alpha ')*(\beta \circ \alpha )=(\beta '*\beta )\circ (\alpha '*\alpha )$

.

Vertical and horizontal compositions are also linked through identity natural transformations:

for

$F:C\to D$

and

$G:D\to E$

,

$\mathrm {id} _{G}*\mathrm {id} _{F}=\mathrm {id} _{G\circ F}$

.

As whiskering is horizontal composition with an identity, the interchange law gives immediately the compact formulas of horizontal composition of $\eta :F\Rightarrow G$ and $\epsilon :J\Rightarrow K$ without having to analyze components and the commutative diagram:

${\begin{aligned}\epsilon *\eta &=(\epsilon \circ \mathrm {id} _{J})*(\mathrm {id} _{G}\circ \eta )=(\epsilon *\mathrm {id} _{G})\circ (\mathrm {id} _{J}*\eta )=\epsilon G\circ J\eta \\&=(\mathrm {id} _{K}\circ \epsilon )*(\eta \circ \mathrm {id} _{F})=(\mathrm {id} _{K}*\eta )\circ (\epsilon *\mathrm {id} _{F})=K\eta \circ \epsilon F\end{aligned}}$

.

## Functor categories

If C is any category and I is a small category, we can form the functor category $C^{I}$ having as objects all functors from I to C and as morphisms the natural transformations between those functors. This forms a category since for any functor F there is an identity natural transformation $1_{F}:F\to F$ (which assigns to every object X the identity morphism on $F(X)$ ) and the composition of two natural transformations (the "vertical composition" above) is again a natural transformation.

The isomorphisms in $C^{I}$ are precisely the natural isomorphisms. That is, a natural transformation $\eta :F\to G$ is a natural isomorphism if and only if there exists a natural transformation $\epsilon :G\to F$ such that $\eta \epsilon =1_{G}$ and $\epsilon \eta =1_{F}$ .

The functor category $C^{I}$ is especially useful if I arises from a directed graph. For instance, if I is the category of the directed graph • → •, then $C^{I}$ has as objects the morphisms of C , and a morphism between $\phi :U\to V$ and $\psi :X\to Y$ in $C^{I}$ is a pair of morphisms $f:U\to X$ and $g:V\to Y$ in C such that the "square commutes", i.e. $\psi \circ f=g\circ \phi$ .

More generally, one can build the 2-category ${\textbf {Cat}}$ whose

- 0-cells (objects) are the small categories,
- 1-cells (arrows) between two objects C and D are the functors from C to D ,
- 2-cells between two 1-cells (functors) $F:C\to D$ and $G:C\to D$ are the natural transformations from F to G .

The horizontal and vertical compositions are the compositions between natural transformations described previously. A functor category $C^{I}$ is then simply a hom-category in this category (smallness issues aside).

### More examples

Every limit and colimit provides an example for a simple natural transformation, as a cone amounts to a natural transformation with the diagonal functor as domain. Indeed, if limits and colimits are defined directly in terms of their universal property, they are universal morphisms in a functor category.

## Yoneda lemma

If X is an object of a locally small category C , then the assignment $Y\mapsto {\text{Hom}}_{C}(X,Y)$ defines a covariant functor $F_{X}:C\to {\textbf {Set}}$ . This functor is called *representable* (more generally, a representable functor is any functor naturally isomorphic to this functor for an appropriate choice of X ). The natural transformations from a representable functor to an arbitrary functor $F:C\to {\textbf {Set}}$ are completely known and easy to describe; this is the content of the Yoneda lemma.

## Historical notes

Saunders Mac Lane, one of the founders of category theory, is said to have remarked, "I didn't invent categories to study functors; I invented them to study natural transformations." Just as the study of groups is not complete without a study of homomorphisms, so the study of categories is not complete without the study of functors. The reason for Mac Lane's comment is that the study of functors is itself not complete without the study of natural transformations.

The context of Mac Lane's remark was the axiomatic theory of homology. Different ways of constructing homology could be shown to coincide: for example in the case of a simplicial complex the groups defined directly (simplicial homology) would be isomorphic to those of the singular theory. What cannot easily be expressed without the language of natural transformations is how homology groups are compatible with morphisms between objects, and how two equivalent homology theories not only have the same homology groups, but also the same morphisms between those groups.

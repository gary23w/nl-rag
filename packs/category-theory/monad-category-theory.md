---
title: "Monad (category theory)"
source: https://en.wikipedia.org/wiki/Monad_(category_theory)
domain: category-theory
license: CC-BY-SA-4.0
tags: category theory, functor, monad, morphism, natural transformation
fetched: 2026-07-02
---

# Monad (category theory)

In category theory, a branch of mathematics, a **monad** is a triple $(T,\eta ,\mu )$ consisting of a functor *T* from a category to itself and two natural transformations $\eta ,\mu$ that satisfy versions of the associativity and unitality axioms. Equivalently, a monad is a monoid in the category of endofunctors of some fixed category (an endofunctor is a functor mapping a category to itself).

For example, if $F,G$ are functors adjoint to each other, then $T=G\circ F$ together with $\eta ,\mu$ determined by the adjoint relation is a monad.

According to mathematician John Baez, a monad can be considered at least in two ways:

1. A monad as a generalized monoid; this is clear since a monad is a monoid in a certain category,
2. A monad as a tool for studying algebraic gadgets; for example, a group can be described by a certain monad.

Monads are used in the theory of pairs of adjoint functors, and they generalize closure operators on partially ordered sets to arbitrary categories. Monads are also useful in the theory of datatypes, the denotational semantics of imperative programming languages, and in functional programming languages, allowing languages without mutable state to do things such as simulate for-loops; see Monad (functional programming).

A monad is also called, especially in old literature, a **triple**, **triad**, **standard construction** and **fundamental construction**.

## Introduction and definition

A monad is a certain type of endofunctor. For example, if F and G are a pair of adjoint functors, with F left adjoint to G , then the composition $G\circ F$ is a monad. If F and G are inverse to each other, the corresponding monad is the identity functor. In general, adjunctions are not equivalences—they relate categories of different natures. The monad theory matters as part of the effort to capture what it is that adjunctions 'preserve'. The other half of the theory, of what can be learned likewise from consideration of $F\circ G$ , is discussed under the dual theory of *comonads*.

### Formal definition

Throughout this article, C denotes a category. A *monad* on C consists of an endofunctor $T\colon C\to C$ together with two natural transformations: $\eta \colon 1_{C}\to T$ (where $1_{C}$ denotes the identity functor on C ) and $\mu \colon T^{2}\to T$ (where $T^{2}$ is the functor $T\circ T$ from C to C ). These are required to fulfill the following conditions (sometimes called coherence conditions):

- $\mu \circ T\mu =\mu \circ \mu T$ (as natural transformations $T^{3}\to T$ ); here $T\mu$ and $\mu T$ are formed by "horizontal composition".
- $\mu \circ T\eta =\mu \circ \eta T=1_{T}$ (as natural transformations $T\to T$ ; here $1_{T}$ denotes the identity transformation from T to T ).

We can rewrite these conditions using the following commutative diagrams:

|   |   |   |
|---|---|---|

See the article on natural transformations for the explanation of the notations $T\mu$ and $\mu T$ , or see below the commutative diagrams not using these notions:

|   |   |   |
|---|---|---|

The first axiom is akin to the associativity in monoids if we think of $\mu$ as the monoid's binary operation, and the second axiom is akin to the existence of an identity element (which we think of as given by $\eta$ ). Indeed, a monad on C can alternatively be defined as a monoid in the category $\mathbf {End} _{C}$ whose objects are the endofunctors of C and whose morphisms are the natural transformations between them, with the monoidal structure induced by the composition of endofunctors.

### The power set monad

The *power set monad* is a monad ${\mathcal {P}}$ on the category $\mathbf {Set}$ : For a set A let $T(A)$ be the power set of A and for a function $f\colon A\to B$ let $T(f)$ be the function between the power sets induced by taking direct images under f . For every set A , we have a map $\eta _{A}\colon A\to T(A)$ , which assigns to every $a\in A$ the singleton $\{a\}$ . The function

$\mu _{A}\colon T(T(A))\to T(A)$

takes a set of sets to its union. These data describe a monad.

### Remarks

The axioms of a monad are formally similar to the monoid axioms. In fact, monads are a type of monoid object; they are precisely the monoids among endofunctors $\operatorname {End} (C)$ , with the multiplication given by composition of endofunctors.

Composition of monads is not, in general, a monad. For example, the double power set functor ${\mathcal {P}}\circ {\mathcal {P}}$ does not admit any monad structure.

### Comonads

The categorical dual definition is a formal definition of a *comonad* (or *cotriple*); this can be said quickly in the terms that a comonad for a category C is a monad for the opposite category $C^{\mathrm {op} }$ . It is therefore a functor U from C to itself, with a set of axioms for *counit* and *comultiplication* that come from reversing the arrows everywhere in the definition just given.

Monads are to monoids as comonads are to *comonoids*. Every set is a comonoid in a unique way, so comonoids are less familiar in abstract algebra than monoids; however, comonoids in the category of vector spaces with its usual tensor product are important and widely studied under the name of coalgebras.

### Terminological history

The notion of monad was invented by Roger Godement in 1958 under the name "standard construction". Monad has been called "dual standard construction", "triple", "monoid" and "triad". The term "monad" is used at latest 1967, by Jean Bénabou.

## Examples

### Identity

The identity functor on a category C is a monad. Its multiplication and unit are the identity function on the objects of C .

### Monads arising from adjunctions

Any adjunction

$F:C\rightleftarrows D:G$

gives rise to a monad on *C*. This very widespread construction works as follows: the endofunctor is the composite

$T=G\circ F.$

This endofunctor is quickly seen to be a monad, where the unit map stems from the unit map $\operatorname {id} _{C}\to G\circ F$ of the adjunction, and the multiplication map is constructed using the counit map of the adjunction:

$T^{2}=G\circ F\circ G\circ F\xrightarrow {G\circ {\text{counit}}\circ F} G\circ F=T.$

In fact, **any monad can be found as an explicit adjunction of functors** using the Eilenberg–Moore category $C^{T}$ (the category of T -algebras).

#### Double dualization

The *double dualization monad*, for a fixed field *k* arises from the adjunction

$(-)^{*}:\mathbf {Vect} _{k}\rightleftarrows \mathbf {Vect} _{k}^{op}:(-)^{*}$

where both functors are given by sending a vector space *V* to its dual vector space $V^{*}:=\operatorname {Hom} (V,k)$ . The associated monad sends a vector space *V* to its double dual $V^{**}$ . This monad is discussed, in much greater generality, by Kock (1970).

#### Closure operators on partially ordered sets

For categories arising from partially ordered sets $(P,\leq )$ (with a single morphism from x to y if and only if $x\leq y$ ), then the formalism becomes much simpler: adjoint pairs are Galois connections and monads are closure operators.

#### Free-forgetful adjunctions

For example, let G be the forgetful functor from the category **Grp** of groups to the category **Set** of sets, and let F be the free group functor from the category of sets to the category of groups. Then F is left adjoint of G . In this case, the associated monad $T=G\circ F$ takes a set X and returns the underlying set of the free group $\mathrm {Free} (X)$ . The unit map of this monad is given by the maps

$X\to T(X)$

including any set X into the set $\mathrm {Free} (X)$ in the natural way, as strings of length 1. Further, the multiplication of this monad is the map

$T(T(X))\to T(X)$

made out of a natural concatenation or 'flattening' of 'strings of strings'. This amounts to two natural transformations. The preceding example about free groups can be generalized to any type of algebra in the sense of a variety of algebras in universal algebra. Thus, every such type of algebra gives rise to a monad on the category of sets. Importantly, the algebra type can be recovered from the monad (as the category of Eilenberg–Moore algebras), so monads can also be seen as generalizing varieties of universal algebras.

Another monad arising from an adjunction is when T is the endofunctor on the category of vector spaces which maps a vector space V to its tensor algebra $T(V)$ , and which maps linear maps to their tensor product. We then have a natural transformation corresponding to the embedding of V into its tensor algebra, and a natural transformation corresponding to the map from $T(T(V))$ to $T(V)$ obtained by simply expanding all tensor products.

### Codensity monads

Under mild conditions, functors not admitting a left adjoint also give rise to a monad, the so-called codensity monad. For example, the inclusion

$\mathbf {FinSet} \subset \mathbf {Set}$

does not admit a left adjoint. Its codensity monad is the monad on sets sending any set *X* to the set of ultrafilters on *X*. This and similar examples are discussed in Leinster (2013).

### Monads used in denotational semantics

The following monads over the category of sets are used in denotational semantics of imperative programming languages, and analogous constructions are used in functional programming.

#### The maybe monad

The endofunctor of the **maybe** or **partiality** monad adds a disjoint point:

$(-)_{*}:\mathbf {Set} \to \mathbf {Set}$

$X\mapsto X\cup \{*\}$

The unit is given by the inclusion of a set X into $X_{*}$ :

$\eta _{X}:X\to X_{*}$

$x\mapsto x$

The multiplication maps elements of X to themselves, and the two disjoint points in $(X_{*})_{*}$ to the one in $X_{*}$ .

In both functional programming and denotational semantics, the maybe monad models partial computations, that is, computations that may fail.

#### The state monad

Given a set S , the endofunctor of the **state monad** maps each set X to the set of functions $S\to S\times X$ . That is $S(X)=\{f:S\to S\times X\}$ , and $S(S(X))=\{f:S\to S\times (S\to S\times X)\}$ .

The component of the unit at X maps each element $x\in X$ to the function

$\eta _{X}(x):S\to S\times X$

$s\mapsto (s,x)$

The multiplication maps the function $f:S\to S\times (S\to S\times X),s\mapsto (s',f')$ to the function

$\mu _{X}(f):S\to S\times X$

$s\mapsto f'(s')$

In more detail, given $f\in S(S(X))$ which is the pair $f=(f_{1},f_{2})$ where $f_{1}:S\to S$ and $f_{2}:S\to (S\to S\times X)$ , so that $f(s)={\big (}f_{1}(s),f_{2}(s):S\to (S\times X){\big )}$ .

We can reverse Curry $f_{2}$ to give $f_{3}:(S\times S)\to (S\times X)$ . This in turn can be split into $f_{4}:(S\times S)\to S$ and $f_{5}:(S\times S)\to X)$ so that

$f_{2}(s_{1})(s_{2})=f_{3}(s_{1},s_{2})={\Big (}f_{4}(s_{1},s_{2}),f_{5}(s_{1},s_{2}){\Big )}$

Then we can re-express $f\in S(S(X))$ as

$f:S\times S\to S\times S\times X,\qquad f(s_{1},s_{2})={\Big (}f_{1}(s_{1}),f_{4}(s_{1},s_{2}),f_{5}(s_{1},s_{2}){\Big )}$

We can now give the join as $\mu _{X}(f):S\to S\times X$

${\big (}\mu _{X}(f){\big )}(s)={\Big (}f_{4}(s,f_{1}(s)),f_{5}(s,f_{1}(s)){\Big )}$

In functional programming and denotational semantics, the state monad models stateful computations.

#### The environment monad

Given a set E , the endofunctor of the **reader** or **environment monad** maps each set X to the set of functions $E\to X$ . Thus, the endofunctor of this monad is exactly the hom functor $\mathrm {Hom} (E,-)$ . The component of the unit at X maps each element $x\in X$ to the constant function $e\mapsto x$ .

The multiplication maps a two-variable function $f:E\to (E\to X)$ to its "diagonal component" $(e\mapsto f(e,e)):E\to X$ . In other words, multiplication is precomposition with

$\Delta :E\to E\times E$

$e\mapsto (e,e).$

In functional programming and denotational semantics, the environment monad models computations with access to some read-only data.

#### The list and set monads

The **list** or **nondeterminism monad** maps a set *X* to the set of finite sequences (i.e., lists) with elements from *X*. The unit maps an element *x* in *X* to the singleton list [x]. The multiplication concatenates a list of lists into a single list.

In functional programming, the list monad is used to model nondeterministic computations. The covariant powerset monad is also known as the **set monad**, and is also used to model nondeterministic computation.

## Algebras for a monad

Given a monad $(T,\eta ,\mu )$ on a category C , it is natural to consider *T -algebras*, i.e., objects of C acted upon by T in a way which is compatible with the unit and multiplication of the monad. More formally, a T -algebra $(x,h)$ is an object x of C together with an arrow $h\colon Tx\to x$ of C called the *structure map* of the algebra such that the diagrams

|   |   | and |   |   |
|---|---|---|---|---|

commute.

A morphism $f\colon (x,h)\to (x',h')$ of T -algebras is an arrow $f\colon x\to x'$ of C such that the diagram

commutes. T -algebras form a category called the *Eilenberg–Moore category* and denoted by $C^{T}$ .

### Examples

#### Algebras over the free group monad

For example, for the free group monad discussed above, a T -algebra is a set X together with a map from the free group generated by X towards X subject to associativity and unitality conditions. Such a structure is equivalent to saying that X is a group itself.

#### Algebras over the distribution monad

Another example is the ***distribution monad*** ${\mathcal {D}}$ on the category of sets. It is defined by sending a set X to the set of functions $f:X\to [0,1]$ with finite support and such that their sum is equal to 1 . In set-builder notation, this is the set ${\mathcal {D}}(X)=\left\{f:X\to [0,1]:{\begin{matrix}\#{\text{supp}}(f)<+\infty \\\sum _{x\in X}f(x)=1\end{matrix}}\right\}$ By inspection of the definitions, it can be shown that algebras over the distribution monad are equivalent to convex sets, i.e., sets equipped with operations $x+_{r}y$ for $r\in [0,1]$ subject to axioms resembling the behavior of convex linear combinations $rx+(1-r)y$ in Euclidean space.

#### Algebras over the symmetric monad

Another useful example of a monad is the symmetric algebra functor on the category of R -modules for a commutative ring R . ${\text{Sym}}^{\bullet }(-):{\text{Mod}}(R)\to {\text{Mod}}(R)$ sending an R -module M to the direct sum of symmetric tensor powers ${\text{Sym}}^{\bullet }(M)=\bigoplus _{k=0}^{\infty }{\text{Sym}}^{k}(M)$ where ${\text{Sym}}^{0}(M)=R$ . For example, ${\text{Sym}}^{\bullet }(R^{\oplus n})\cong R[x_{1},\ldots ,x_{n}]$ where the R -algebra on the right is considered as a module. Then, an algebra over this monad are commutative R -algebras. There are also algebras over the monads for the alternating tensors ${\text{Alt}}^{\bullet }(-)$ and total tensor functors $T^{\bullet }(-)$ giving anti-symmetric R -algebras, and free R -algebras, so ${\begin{aligned}{\text{Alt}}^{\bullet }(R^{\oplus n})&=R(x_{1},\ldots ,x_{n})\\{\text{T}}^{\bullet }(R^{\oplus n})&=R\langle x_{1},\ldots ,x_{n}\rangle \end{aligned}}$ where the first ring is the free anti-symmetric algebra over R in n -generators and the second ring is the free algebra over R in n -generators.

#### Commutative algebras in E-infinity ring spectra

There is an analogous construction for commutative $\mathbb {S}$ -algebraspg 113 which gives commutative A -algebras for a commutative $\mathbb {S}$ -algebra A . If ${\mathcal {M}}_{A}$ is the category of A -modules, then the functor $\mathbb {P$ is the monad given by $\mathbb {P} (M)=\bigvee _{j\geq 0}M^{j}/\Sigma _{j}$ where $M^{j}=M\wedge _{A}\cdots \wedge _{A}M$ j -times. Then there is an associated category ${\mathcal {C}}_{A}$ of commutative A -algebras from the category of algebras over this monad.

## Monads and adjunctions

As was mentioned above, any adjunction gives rise to a monad. Conversely, every monad arises from some adjunction, namely the free–forgetful adjunction

$T(-):C\rightleftarrows C^{T}:{\text{forget}}$

whose left adjoint sends an object *X* to the free *T*-algebra *T*(*X*). However, there are usually several distinct adjunctions giving rise to a monad: let $\mathbf {Adj} (C,T)$ be the category whose objects are the adjunctions $(F,G,e,\varepsilon )$ such that $(GF,e,G\varepsilon F)=(T,\eta ,\mu )$ and whose arrows are the morphisms of adjunctions that are the identity on C . Then the above free–forgetful adjunction involving the Eilenberg–Moore category $C^{T}$ is a terminal object in $\mathbf {Adj} (C,T)$ . An initial object is the Kleisli category, which is by definition the full subcategory of $C^{T}$ consisting only of free *T*-algebras, i.e., *T*-algebras of the form $T(x)$ for some object *x* of *C*.

### Monadic adjunctions

Given any adjunction $(F:C\to D,G:D\to C,\eta ,\varepsilon )$ with associated monad *T*, the functor *G* can be factored as

$D{\overset {\widetilde {G}}{\longrightarrow }}C^{T}\xrightarrow {\text{forget}} C,$

i.e., *G*(*Y*) can be naturally endowed with a *T*-algebra structure for any *Y* in *D*. The adjunction is called a **monadic adjunction** if the first functor ${\tilde {G}}$ yields an equivalence of categories between *D* and the Eilenberg–Moore category $C^{T}$ . By extension, a functor $G\colon D\to C$ is said to be **monadic** if it has a left adjoint F forming a monadic adjunction. For example, the free–forgetful adjunction between groups and sets is monadic, since algebras over the associated monad are groups, as was mentioned above. In general, knowing that an adjunction is monadic allows one to reconstruct objects in *D* out of objects in *C* and the *T*-action.

### Beck's monadicity theorem

*Beck's monadicity theorem* gives a necessary and sufficient condition for an adjunction to be monadic. A simplified version of this theorem states that *G* is monadic if and only if it is conservative (or *G* reflects isomorphisms, i.e., a morphism in *D* is an isomorphism if and only if its image under *G* is an isomorphism in *C*) and *G* preserves coequalizers.

For example, the forgetful functor from the category of compact Hausdorff spaces to sets is monadic. However the forgetful functor from all topological spaces to sets is not conservative since there are continuous bijective maps (between non-compact or non-Hausdorff spaces) that fail to be homeomorphisms. Thus, this forgetful functor is not monadic. The dual version of Beck's theorem, characterizing comonadic adjunctions, is relevant in different fields such as topos theory and topics in algebraic geometry related to descent. A first example of a comonadic adjunction is the adjunction

$-\otimes _{A}B:\mathbf {Mod} _{A}\rightleftarrows \mathbf {Mod} _{B}:\operatorname {forget}$

for a ring homomorphism $A\to B$ between commutative rings. This adjunction is comonadic, by Beck's theorem, if and only if *B* is faithfully flat as an *A*-module. It thus allows to descend *B*-modules, equipped with a descent datum (i.e., an action of the comonad given by the adjunction) to *A*-modules. The resulting theory of faithfully flat descent is widely applied in algebraic geometry.

## Uses

Monads are used in functional programming to express types of sequential computation (sometimes with side-effects). See monads in functional programming, and the more mathematically oriented Wikibook module b:Haskell/Category theory.

Monads are used in the denotational semantics of impure functional and imperative programming languages.

In categorical logic, an analogy has been drawn between the monad-comonad theory, and modal logic via closure operators, interior algebras, and their relation to models of S4 and intuitionistic logics.

## Generalization

Monad is also defined in a any weak 2-category, which is defined as a lax 2-functor from terminal category $\mathbb {1}$ to 2-category Cat. The theory of 2-monads was introduced by Blackwell–Kelly–Power, and 2-monads without prefixes are usually a strict notion. A notion that weakens monad laws so that they hold "up to coherent invertible modifications" is called pseudomonad. While there are attempts to define monad preserving composition only up to a noninvertible transformation, there is no obvious general notion of lax monad on a weak 2-category, since there is no good 2-category (or even a weak 3-category) of weak 2-categories that contain lax or oplax functors. The lax monad was first introduced by Bunge, but other definitions different from lax monad à la Bunge.

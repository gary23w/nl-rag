---
title: "Flat module"
source: https://en.wikipedia.org/wiki/Flat_module
domain: module-theory
license: CC-BY-SA-4.0
tags: module theory, projective module, injective module, flat module
fetched: 2026-07-02
---

# Flat module

In algebra, **flat modules** include free modules, projective modules, and, over a principal ideal domain, torsion-free modules. Formally, a module *M* over a ring *R* is *flat* if taking the tensor product over *R* with *M* preserves exact sequences. A module is **faithfully flat** if taking the tensor product with a sequence produces an exact sequence if and only if the original sequence is exact.

Flatness was introduced by Jean-Pierre Serre (1956) in his paper *Géometrie Algébrique et Géométrie Analytique*.

## Definition

A left module M over a ring R is *flat* if the following condition is satisfied: for every injective linear map $\varphi :K\to L$ of right R-modules, the map

$\varphi \otimes _{R}M:K\otimes _{R}M\to L\otimes _{R}M$

is also injective, where $\varphi \otimes _{R}M$ is the map induced by $k\otimes m\mapsto \varphi (k)\otimes m.$

For this definition, it is enough to restrict the injections $\varphi$ to the inclusions of finitely generated ideals into R.

Equivalently, an R-module M is flat if the tensor product with M is an exact functor; that is if, for every short exact sequence of R-modules $0\rightarrow K\rightarrow L\rightarrow J\rightarrow 0,$ the sequence $0\rightarrow K\otimes _{R}M\rightarrow L\otimes _{R}M\rightarrow J\otimes _{R}M\rightarrow 0$ is also exact. (This is an equivalent definition since the tensor product is a right exact functor.)

These definitions apply also if R is a non-commutative ring, and M is a left R-module; in this case, K, L and J must be right R-modules, and the tensor products are not R-modules in general, but only abelian groups.

### Characterizations

Flatness can also be characterized by the following equational condition, which means that R-linear relations in M stem from linear relations in R.

A left R-module M is flat if and only if, for every linear relation

${\textstyle \sum _{i=1}^{m}r_{i}x_{i}=0}$

with $r_{i}\in R$ and $x_{i}\in M$ , there exist elements $y_{j}\in M$ and $a_{i,j}\in R,$ such that

${\textstyle \sum _{i=1}^{m}r_{i}a_{i,j}=0\qquad }$

for

$j=1,\ldots ,n,$

and

${\textstyle x_{i}=\sum _{j=1}^{n}a_{i,j}y_{j}\qquad }$

for

$i=1,\ldots ,m.$

It is equivalent to define n elements of a module, and a linear map from $R^{n}$ to this module, which maps the standard basis of $R^{n}$ to the n elements. This allows rewriting the previous characterization in terms of homomorphisms, as follows.

An R-module M is flat if and only if the following condition holds: for every map $f:F\to M,$ where F is a finitely generated free R-module, and for every finitely generated R-submodule K of $\ker f,$ the map f factors through a map g to a free R-module G such that $g(K)=0:$

## Relations to other module properties

Flatness is related to various other module properties, such as being free, projective, or torsion-free. In particular, every flat module is torsion-free, every projective module is flat, and every free module is projective.

There are finitely generated modules that are flat and not projective. However, finitely generated flat modules are all projective over the rings that are most commonly considered. Moreover, a finitely generated module is flat if and only it is locally free, meaning all the localizations at prime ideals are free modules.

This is partly summarized in the following graphic.

### Torsion-free modules

Every flat module is torsion-free. This results from the above characterization in terms of relations by taking *m* = 1.

The converse holds over the integers, and more generally over principal ideal domains and Dedekind rings.

An integral domain over which every torsion-free module is flat is called a Prüfer domain.

### Free and projective modules

A module M is projective if and only if there is a free module G and two linear maps $i:M\to G$ and $p:G\to M$ such that $p\circ i=\mathrm {id} _{M}.$ In particular, every free module is projective (take $G=M$ and $i=p=\mathrm {id} _{M}$ ).

Every projective module is flat. This can be proven from the above characterizations of flatness and projectivity in terms of linear maps by taking $g=i\circ f$ and $h=p.$

Conversely, finitely generated flat modules are projective under mild conditions that are generally satisfied in commutative algebra and algebraic geometry. This makes the concept of flatness useful mainly for modules that are not finitely generated.

A finitely presented module (that is the quotient of a finitely generated free module by a finitely generated submodule) that is flat is always projective. This can be proven by taking f surjective and $K=\ker f$ in the above characterization of flatness in terms of linear maps. The condition $g(K)=0$ implies the existence of a linear map $i:M\to G$ such that $i\circ f=g,$ and thus $h\circ i\circ f=h\circ g=f.$ As f is surjective, one has thus $h\circ i=\mathrm {id} _{M},$ and M is projective.

Over a Noetherian ring, every finitely generated flat module is projective, since every finitely generated module is finitely presented. The same result is true over an integral domain, even if it is not Noetherian.

On a local ring every finitely generated flat module is free.

A finitely generated flat module that is not projective can be built as follows. Let $R=F^{\mathbb {N} }$ be the set of the infinite sequences whose terms belong to a fixed field F. It is a commutative ring with addition and multiplication defined componentwise. This ring is absolutely flat (that is, every module is flat). The module $R/I,$ where I is the ideal of the sequences with a finite number of nonzero terms, is thus flat and finitely generated (only one generator), but it is not projective.

### Non-examples

- If I is an ideal in a Noetherian commutative ring R, then $R/I$ is not a flat module, except if I is generated by an idempotent (that is an element equal to its square). In particular, if R is an integral domain, $R/I$ is flat only if I equals R or is the zero ideal.
- Over an integral domain, a flat module is torsion free. Thus a module that contains nonzero torsion elements is not flat. In particular $\mathbb {Q} /\mathbb {Z}$ and all fields of positive characteristics are non-flat $\mathbb {Z}$ -modules, where $\mathbb {Z}$ is the ring of integers, and $\mathbb {Q}$ is the field of the rational numbers.

### Direct sums, limits and products

The direct sum $\textstyle \bigoplus _{i\in I}M_{i}$ of modules is flat if and only if each $M_{i}$ is flat.

The direct limit of flat modules is flat. In particular, the direct limit of free modules is flat. Conversely, every flat module can be written as the direct limit of finitely-generated free modules.

Direct products of flat modules need not in general be flat. In fact, given a ring R, every direct product of flat R-modules is flat if and only if R is a coherent ring (that is, every finitely generated ideal is finitely presented).

## Flat ring extensions

A ring homomorphism $R\to S$ is *flat* if S is a flat R-module for the module structure induced by the homomorphism. For example, the polynomial ring *R*[*t*] is flat over R, for any ring R.

For any multiplicative subset S of a commutative ring R , the localization $S^{-1}R$ is a flat *R*-algebra (it is projective only in exceptional cases). For example, $\mathbb {Q}$ is flat and not projective over $\mathbb {Z} .$

If I is an ideal of a Noetherian commutative ring $R,$ the completion ${\widehat {R}}$ of R with respect to I is flat. It is faithfully flat if and only if I is contained in the Jacobson radical of $A.$ (See also Zariski ring.)

## Local property

In this section, R denotes a commutative ring. If ${\mathfrak {p}}$ is a prime ideal of R, the localization at ${\mathfrak {p}}$ is, as usual, denoted with ${\mathfrak {p}}$ as an index. That is, $R_{\mathfrak {p}}=(R\setminus {\mathfrak {p}})^{-1}R,$ and, if M is an R-module, $M_{\mathfrak {p}}=(R\setminus {\mathfrak {p}})^{-1}M=R_{\mathfrak {p}}\otimes _{R}M.$

If M is an R-module the three following conditions are equivalent:

- M is a flat R -module;
- $M_{\mathfrak {p}}$ is a flat $R_{\mathfrak {p}}$ -module for every prime ideal ${\mathfrak {p}};$
- $M_{\mathfrak {m}}$ is a flat $R_{\mathfrak {m}}$ -module for every maximal ideal ${\mathfrak {m}}.$

This property is fundamental in commutative algebra and algebraic geometry, since it reduces the study of flatness to the case of local rings. They are often expressed by saying that flatness is a local property.

### Flat morphisms of schemes

The definition of a flat morphism of schemes results immediately from the local property of flatness.

A morphism $f:X\to Y$ of schemes is a flat morphism if the induced map on local rings

${\mathcal {O}}_{Y,f(x)}\to {\mathcal {O}}_{X,x}$

is a flat ring homomorphism for any point *x* in *X*.

Thus, properties of flat (or faithfully flat) ring homomorphisms extend naturally to geometric properties of flat morphisms in algebraic geometry.

For example, consider the flat $\mathbb {C} [t]$ -algebra $R=\mathbb {C} [t,x,y]/(xy-t)$ (see below). The inclusion $\mathbb {C} [t]\hookrightarrow R$ induces the flat morphism

${\displaystyle \pi$

The (geometric) fiber $\pi ^{-1}(t)$ is the curve given by the equation $xy=t.$ (See also flat degeneration and deformation to normal cone.)

Let $S=R[x_{1},\dots ,x_{r}]$ be a polynomial ring over a commutative Noetherian ring R and $f\in S$ a nonzerodivisor. Then $S/fS$ is flat over R if and only if f is primitive (the coefficients generate the unit ideal). An example is $\mathbb {C} [t,x,y]/(xy-t),$ which is flat (and even free) over $\mathbb {C} [t]$ (see also below for the geometric meaning). Such flat extensions can be used to yield examples of flat modules that are not free and do not result from a localization.

## Faithful flatness

A module is *faithfully flat* if taking the tensor product with a sequence produces an exact sequence if and only if the original sequence is exact. Although the concept is defined for modules over a non-necessary commutative ring, it is used mainly for commutative algebras. So, this is the only case that is considered here, even if some results can be generalized to the case of modules over a non-commutaive ring.

In this section, $f\colon R\to S$ is a ring homomorphism of commutative rings, which gives to S the structures of an R -algebra and an R -module. If S is a R -module flat (or faithfully flat), one says commonly that S is flat (or faithfully flat) over $R,$ and that f is flat (or faithfully flat).

If S is flat over $R,$ the following conditions are equivalent.

- S is faithfully flat.
- For each maximal ideal ${\mathfrak {m}}$ of R , one has ${\mathfrak {m}}S\neq S.$
- If M is a nonzero R -module, then $M\otimes _{R}S\neq 0.$
- For every prime ideal ${\mathfrak {p}}$ of $R,$ there is a prime ideal ${\mathfrak {P}}$ of S such that ${\mathfrak {p}}=f^{-1}({\mathfrak {P}}).$ In other words, the map $f^{*}\colon \operatorname {Spec} (S)\to \operatorname {Spec} (R)$ induced by f on the spectra is surjective.
- $f,$ is injective, and R is a pure subring of $S;$ that is, $M\to M\otimes _{R}S$ is injective for every R -module M .

The second condition implies that a flat local homomorphism of local rings is faithfully flat. It follows from the last condition that $I=IS\cap R$ for every ideal I of R (take $M=R/I$ ). In particular, if S is a Noetherian ring, then R is also Noetherian.

The second-last condition can be stated in the following strengthened form: $\operatorname {Spec} (S)\to \operatorname {Spec} (R)$ is *submersive*, which means that the Zariski topology of $\operatorname {Spec} (R)$ is the quotient topology of that of $\operatorname {Spec} (S)$ (this is a special case of the fact that a faithfully flat quasi-compact morphism of schemes has this property.). See also *Flat morphism § Properties of flat morphisms*.

### Examples

- A ring homomorphism $R\to S$ such that S is a nonzero free R-module is faithfully flat. For example:
  - Every field extension is faithfully flat. This property is implicitly behind the use of complexification for proving results on real vector spaces.
  - A polynomial ring is a faithfully flat extension of its ring of coefficients.
  - If $p\in R[x]$ is a monic polynomial, the inclusion $R\hookrightarrow R[t]/\langle p\rangle$ is faithfully flat.
- Let $t_{1},\ldots ,t_{k}\in R.$ The direct product $\textstyle \prod _{i}R[t_{i}^{-1}]$ of the localizations at the $t_{i}$ is faithfully flat over R if and only if $t_{1},\ldots ,t_{k}$ generate the unit ideal of R (that is, if 1 is a linear combination of the $t_{i}$ ).
- The direct sum of the localizations $R_{\mathfrak {p}}$ of R at all its prime ideals is a faithfully flat module that is not an algebra, except if there are finitely many prime ideals.

The two last examples are implicitly behind the wide use of localization in commutative algebra and algebraic geometry.

- For a given ring homomorphism $f:A\to B,$ there is an associated complex called the Amitsur complex:

$0\to A{\overset {f}{\to }}B{\overset {\delta ^{0}}{\to }}B\otimes _{A}B{\overset {\delta ^{1}}{\to }}B\otimes _{A}B\otimes _{A}B\to \cdots$ where the coboundary operators $\delta ^{n}$ are the alternating sums of the maps obtained by inserting 1 in each spot; e.g., $\delta ^{0}(b)=b\otimes 1-1\otimes b$ . Then (Grothendieck) this complex is exact if f is faithfully flat.

### Faithfully flat local homomorphisms

Here is one characterization of a faithfully flat homomorphism for a not-necessarily-flat homomorphism. Given an injective local homomorphism $(R,{\mathfrak {m}})\hookrightarrow (S,{\mathfrak {n}})$ such that ${\mathfrak {m}}S$ is an ${\mathfrak {n}}$ -primary ideal, the homomorphism $S\to B$ is faithfully flat if and only if the theorem of transition holds for it; that is, for each ${\mathfrak {m}}$ -primary ideal ${\mathfrak {q}}$ of R , $\operatorname {length} _{S}(S/{\mathfrak {q}}S)=\operatorname {length} _{S}(S/{\mathfrak {m}}S)\operatorname {length} _{R}(R/{\mathfrak {q}}).$

## Homological characterization using Tor functors

Flatness may also be expressed using the Tor functors, the left derived functors of the tensor product. A left R -module M is flat if and only if

$\operatorname {Tor} _{n}^{R}(X,M)=0$

for all

$n\geq 1$

and all right

R

-modules

X

).

In fact, it is enough to check that the first Tor term vanishes, i.e., *M* is flat if and only if

$\operatorname {Tor} _{1}^{R}(N,M)=0$

for any R -module N or, even more restrictively, when $N=R/I$ and $I\subset R$ is any finitely generated ideal.

Using the Tor functor's long exact sequences, one can then easily prove facts about a short exact sequence

$0\to A{\overset {f}{\longrightarrow }}B{\overset {g}{\longrightarrow }}C\to 0$

If A and C are flat, then so is B . Also, if B and C are flat, then so is A . If A and B are flat, C need not be flat in general. However, if A is pure in B and B is flat, then A and C are flat.

## Flat resolutions

A **flat resolution** of a module M is a resolution of the form

$\cdots \to F_{2}\to F_{1}\to F_{0}\to M\to 0,$

where the $F_{i}$ are all flat modules. Any free or projective resolution is necessarily a flat resolution. Flat resolutions can be used to compute the Tor functor.

The *length* of a finite flat resolution is the first subscript *n* such that $F_{n}$ is nonzero and $F_{i}=0$ for $i>n$ . If a module M admits a finite flat resolution, the minimal length among all finite flat resolutions of M is called its flat dimension and denoted $\operatorname {fd} (M)$ . If M does not admit a finite flat resolution, then by convention the flat dimension is said to be infinite. As an example, consider a module M such that $\operatorname {fd} (M)=0$ . In this situation, the exactness of the sequence $0\to F_{0}\to M\to 0$ indicates that the arrow in the center is an isomorphism, and hence M itself is flat.

In some areas of module theory, a flat resolution must satisfy the additional requirement that each map is a flat pre-cover of the kernel of the map to the right. For projective resolutions, this condition is almost invisible: a projective pre-cover is simply an epimorphism from a projective module. These ideas are inspired from Auslander's work in approximations. These ideas are also familiar from the more common notion of minimal projective resolutions, where each map is required to be a projective cover of the kernel of the map to the right. However, projective covers need not exist in general, so minimal projective resolutions are only of limited use over rings like the integers.

## Flat covers

While projective covers for modules do not always exist, it was speculated that for general rings, every module would have a flat cover, that is, every module *M* would be the epimorphic image of a flat module *F* such that every map from a flat module onto *M* factors through *F*, and any endomorphism of *F* over *M* is an automorphism. This **flat cover conjecture** was explicitly first stated in Enochs (1981, p. 196). The conjecture turned out to be true, resolved positively and proved simultaneously by L. Bican, R. El Bashir and E. Enochs. This was preceded by important contributions by P. Eklof, J. Trlifaj and J. Xu.

Since flat covers exist for all modules over all rings, minimal flat resolutions can take the place of minimal projective resolutions in many circumstances. The measurement of the departure of flat resolutions from projective resolutions is called *relative homological algebra*, and is covered in classics such as Mac Lane (1963) and in more recent works focussing on flat resolutions such as Enochs and Jenda (2000).

## In constructive mathematics

Flat modules have increased importance in constructive mathematics, where projective modules are less useful. For example, that all free modules are projective is equivalent to the full axiom of choice, so theorems about projective modules, even if proved constructively, do not necessarily apply to free modules. In contrast, no choice is needed to prove that free modules are flat, so theorems about flat modules can still apply.

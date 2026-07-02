---
title: "Localization (commutative algebra)"
source: https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
domain: commutative-algebra
license: CC-BY-SA-4.0
tags: commutative algebra, noetherian ring, krull dimension, grobner basis
fetched: 2026-07-02
---

# Localization (commutative algebra)

In commutative algebra and algebraic geometry, **localization** is a formal way to introduce the "denominators" to a given ring or module. That is, it introduces a new ring/module out of an existing ring/module *R*, so that it consists of fractions ${\frac {m}{s}},$ such that the denominator *s* belongs to a given subset *S* of *R*. If *S* is the set of the non-zero elements of an integral domain, then the localization is the field of fractions: this case generalizes the construction of the field $\mathbb {Q}$ of rational numbers from the ring $\mathbb {Z}$ of integers.

The technique has become fundamental, particularly in algebraic geometry, as it provides a natural link to sheaf theory. In fact, the term *localization* originated in algebraic geometry: if *R* is a ring of functions defined on some geometric object (algebraic variety) *V*, and one wants to study this variety "locally" near a point *p*, then one considers the set *S* of all functions that are not zero at *p* and localizes *R* with respect to *S*. The resulting ring $S^{-1}R$ contains information about the behavior of *V* near *p*, and excludes information that is not "local", such as the zeros of functions that are outside *V* (cf. the example given at local ring).

## Localization of a ring

The localization of a commutative ring R by a multiplicatively closed set S is a new ring $S^{-1}R$ whose elements are fractions with numerators in R and denominators in S.

If the ring is an integral domain the construction generalizes and follows closely that of the field of fractions, and, in particular, that of the rational numbers as the field of fractions of the integers. For rings that have zero divisors, the construction is similar but requires more care.

### Multiplicative set

Localization is commonly done with respect to a multiplicatively closed set S (also called a *multiplicative set* or a *multiplicative system*) of elements of a ring R, that is a subset of R that is closed under multiplication, and contains 1.

The requirement that S must be a multiplicative set is natural, since it implies that all denominators introduced by the localization belong to S. The localization by a set U that is not multiplicatively closed can also be defined, by taking as possible denominators all products of elements of U. However, the same localization is obtained by using the multiplicatively closed set S of all products of elements of U. As this often makes reasoning and notation simpler, it is standard practice to consider only localizations by multiplicative sets.

For example, the localization by a single element s introduces fractions of the form ${\tfrac {a}{s}},$ but also products of such fractions, such as ${\tfrac {ab}{s^{2}}}.$ So, the denominators will belong to the multiplicative set $\{1,s,s^{2},s^{3},\ldots \}$ of the powers of s. Therefore, one generally talks of "the localization by the powers of an element" rather than of "the localization by an element".

The localization of a ring R by a multiplicative set S is generally denoted $S^{-1}R,$ but other notations are commonly used in some special cases: if $S=\{1,t,t^{2},\ldots \}$ consists of the powers of a single element, $S^{-1}R$ is often denoted $R_{t};$ if $S=R\setminus {\mathfrak {p}}$ is the complement of a prime ideal ${\mathfrak {p}}$ , then $S^{-1}R$ is denoted $R_{\mathfrak {p}}.$

*In the remainder of this article, only localizations by a multiplicative set are considered.*

### Integral domains

When the ring R is an integral domain and S does not contain 0, the ring $S^{-1}R$ is a subring of the field of fractions of R. As such, the localization of a domain is a domain.

More precisely, it is the subring of the field of fractions of R, that consists of the fractions ${\tfrac {a}{s}}$ such that $s\in S.$ This is a subring since the sum ${\tfrac {a}{s}}+{\tfrac {b}{t}}={\tfrac {at+bs}{st}},$ and the product ${\tfrac {a}{s}}\,{\tfrac {b}{t}}={\tfrac {ab}{st}}$ of two elements of $S^{-1}R$ are in $S^{-1}R.$ This results from the defining property of a multiplicative set, which implies also that $1={\tfrac {1}{1}}\in S^{-1}R.$ In this case, R is a subring of $S^{-1}R.$ It is shown below that this is no longer true in general, typically when S contains zero divisors.

For example, the decimal fractions are the localization of the ring of integers by the multiplicative set of the powers of ten. In this case, $S^{-1}R$ consists of the rational numbers that can be written as ${\tfrac {n}{10^{k}}},$ where n is an integer, and k is a nonnegative integer.

### General construction

In the general case, a problem arises with zero divisors. Let S be a multiplicative set in a commutative ring R. Suppose that $s\in S,$ and $0\neq a\in R$ is a zero divisor with $as=0.$ Then ${\tfrac {a}{1}}$ is the image in $S^{-1}R$ of $a\in R,$ and one has ${\tfrac {a}{1}}={\tfrac {as}{s}}={\tfrac {0}{s}}={\tfrac {0}{1}}.$ Thus some nonzero elements of R must be zero in $S^{-1}R.$ The construction that follows is designed for taking this into account.

Given R and S as above, one considers the equivalence relation on $R\times S$ that is defined by $(r_{1},s_{1})\sim (r_{2},s_{2})$ if there exists a $t\in S$ such that $t(s_{1}r_{2}-s_{2}r_{1})=0.$

The localization $S^{-1}R$ is defined as the set of the equivalence classes for this relation. The class of (*r*, *s*) is denoted as ${\frac {r}{s}},$ $r/s,$ or $s^{-1}r.$ So, one has ${\tfrac {r_{1}}{s_{1}}}={\tfrac {r_{2}}{s_{2}}}$ if and only if there is a $t\in S$ such that $t(s_{1}r_{2}-s_{2}r_{1})=0.$ The reason for the t is to handle cases such as the above ${\tfrac {a}{1}}={\tfrac {0}{1}},$ where $s_{1}r_{2}-s_{2}r_{1}$ is nonzero even though the fractions should be regarded as equal.

The localization $S^{-1}R$ is a commutative ring with addition

${\frac {r_{1}}{s_{1}}}+{\frac {r_{2}}{s_{2}}}={\frac {r_{1}s_{2}+r_{2}s_{1}}{s_{1}s_{2}}},$

multiplication

${\frac {r_{1}}{s_{1}}}\,{\frac {r_{2}}{s_{2}}}={\frac {r_{1}r_{2}}{s_{1}s_{2}}},$

additive identity ${\tfrac {0}{1}},$ and multiplicative identity ${\tfrac {1}{1}}.$

The function

$j:r\mapsto {\frac {r}{1}},$

known as the *canonical localization map*, defines a ring homomorphism from R into $S^{-1}R,$ which is injective if and only if S does not contain any zero divisors.

If $0\in S,$ then $S^{-1}R$ is the zero ring that has only one unique element 0.

If S is the set of all regular elements of R (that is the elements that are not zero divisors), $S^{-1}R$ is called the total ring of fractions of R.

### Universal property

The (above defined) ring homomorphism $j\colon R\to S^{-1}R$ satisfies a universal property that is described below. This characterizes $S^{-1}R$ up to an isomorphism. So all properties of localizations can be deduced from the universal property, independently from the way they have been constructed. Moreover, many important properties of localization are easily deduced from the general properties of universal properties, while their direct proof may be more technical.

The universal property satisfied by $j\colon R\to S^{-1}R$ is the following:

If

$f\colon R\to T$

is a ring homomorphism that maps every element of

S

to a

unit

(invertible element) in

T

, there exists a unique ring homomorphism

$g\colon S^{-1}R\to T$

such that

$f=g\circ j.$

Using category theory, this can be expressed by saying that localization is a functor that is left adjoint to a forgetful functor. More precisely, let ${\mathcal {C}}$ and ${\mathcal {D}}$ be the categories whose objects are pairs of a commutative ring and a submonoid of, respectively, the multiplicative monoid or the group of units of the ring. The morphisms of these categories are the ring homomorphisms that map the submonoid of the first object into the submonoid of the second one. Finally, let ${\mathcal {F}}\colon {\mathcal {D}}\to {\mathcal {C}}$ be the forgetful functor that forgets that the elements of the second element of the pair are invertible.

Then the factorization $f=g\circ j$ of the universal property defines a bijection

$\hom _{\mathcal {C}}((R,S),{\mathcal {F}}(T,U))\to \hom _{\mathcal {D}}((S^{-1}R,j(S)),(T,U)).$

This may seem a rather tricky way of expressing the universal property, but it is useful for showing easily many properties, by using the fact that the composition of two left adjoint functors is a left adjoint functor.

### Examples

- If $R=\mathbb {Z}$ is the ring of integers, and $S=\mathbb {Z} \setminus \{0\},$ then $S^{-1}R$ is the field $\mathbb {Q}$ of the rational numbers.
- If R is an integral domain, and $S=R\setminus \{0\},$ then $S^{-1}R$ is the field of fractions of R. The preceding example is a special case of this one.
- If R is a commutative ring, and if S is the subset of its elements that are not zero divisors, then $S^{-1}R$ is the total ring of fractions of R. In this case, S is the largest multiplicative set such that the homomorphism $R\to S^{-1}R$ is injective. The preceding example is a special case of this one.
- If x is an element of a commutative ring R and $S=\{1,x,x^{2},\ldots \},$ then $S^{-1}R$ can be identified (is canonically isomorphic to) $R[x^{-1}]=R[s]/(xs-1).$ (The proof consists of showing that this ring satisfies the above universal property.) The ring $S^{-1}R$ is generally denoted $R_{x}$ . This sort of localization plays a fundamental role in the definition of an affine scheme.
- If ${\mathfrak {p}}$ is a prime ideal of a commutative ring R, the set complement $S=R\setminus {\mathfrak {p}}$ of ${\mathfrak {p}}$ in R is a multiplicative set (by the definition of a prime ideal). The ring $S^{-1}R$ is a local ring that is generally denoted $R_{\mathfrak {p}},$ and called *the local ring of R at* ${\mathfrak {p}}.$ This sort of localization is fundamental in commutative algebra, because many properties of a commutative ring can be read on its local rings. Such a property is often called a local property. For example, a ring is regular if and only if all its local rings are regular.

### Ring properties

Localization is a rich construction that has many useful properties. In this section, only the properties relative to rings and to a single localization are considered. Properties concerning ideals, modules, or several multiplicative sets are considered in other sections.

- $S^{-1}R=0$ if and only if S contains 0 .
- The ring homomorphism $R\to S^{-1}R$ is injective if and only if S does not contain any zero divisors.
- The ring homomorphism $R\to S^{-1}R$ is an epimorphism in the category of rings, that is not surjective in general.
- The ring $S^{-1}R$ is a flat R-module (see § Localization of a module for details).
- The ideals of $S^{-1}R$ are the extensions of ideals of R by $j:R\to S^{-1}R$ , $r\mapsto r/1$ ; that is, for an ideal I of R , $j(I)(S^{-1}R)=\{r/s\in S^{-1}R:r\in I\}$ is an ideal of $S^{-1}R$ and is often denoted $I(S^{-1}R)$ or $S^{-1}I$ (this notation comes from equivalently regarding this ideal as the localization of I as an R -module by S , see below); the ideal is a proper ideal if and only if $I\cap S=\emptyset$ .
- If $S=R\setminus {\mathfrak {p}}$ is the complement of a prime ideal ${\mathfrak {p}}$ of R , then $S^{-1}R,$ denoted $R_{\mathfrak {p}},$ is a local ring; that is, it has only one maximal ideal, ${\mathfrak {p}}R_{\mathfrak {p}}$ (i.e., the extension of ${\mathfrak {p}}$ by $j:R\to S^{-1}R\ (=R_{\mathfrak {p}})$ defined above, sometimes denoted ${\mathfrak {p}}_{\mathfrak {p}}$ ), and $\kappa ({\mathfrak {p}})=R_{\mathfrak {p}}/{\mathfrak {p}}R_{\mathfrak {p}}$ is the residue field of *R* at ${\mathfrak {p}}$ .
- Localization commutes with formations of finite sums, products, intersections and radicals; e.g., if ${\sqrt {I}}$ denote the radical of an ideal I in R , then

${\sqrt {I}}\cdot S^{-1}R={\sqrt {I\cdot S^{-1}R}}\,.$

In particular,

R

is

reduced

if and only if its total ring of fractions is reduced.

- Localization commutes with taking quotients; that is, if *I* is an ideal of *R*, then $S^{-1}R/S^{-1}I\cong {\overline {S}}^{-1}(R/I)$ , where ${\overline {S}}$ is the image of *S* in $R/I$ .
- Let R be an integral domain with the field of fractions K . Then its localization $R_{\mathfrak {p}}$ at a prime ideal ${\mathfrak {p}}$ can be viewed as a subring of K . Moreover,

$R=\bigcap _{\mathfrak {p}}R_{\mathfrak {p}}=\bigcap _{\mathfrak {m}}R_{\mathfrak {m}}$

where the first intersection is over all prime ideals and the second over the maximal ideals.

- There is a bijection between the set of prime ideals of $S^{-1}R$ and the set of prime ideals of R that are disjoint from S . This bijection is induced by the given homomorphism $R\to S^{-1}R$ .

### Saturation of a multiplicative set

Let $S\subseteq R$ be a multiplicative set. The *saturation* ${\hat {S}}$ of S is the set

${\hat {S}}=\{r\in R\colon \exists s\in R,rs\in S\}.$

The multiplicative set S is *saturated* if it equals its saturation, that is, if ${\hat {S}}=S$ , or equivalently, if $rs\in S$ implies that r and s are in S.

If S is not saturated, and $rs\in S,$ then ${\frac {s}{rs}}$ is a multiplicative inverse of the image of r in $S^{-1}R.$ So, the images of the elements of ${\hat {S}}$ are all invertible in $S^{-1}R,$ and the universal property implies that $S^{-1}R$ and ${\hat {S}}{}^{-1}R$ are canonically isomorphic, that is, there is a unique isomorphism between them that fixes the images of the elements of R.

If S and T are two multiplicative sets, then $S^{-1}R$ and $T^{-1}R$ are isomorphic if and only if they have the same saturation, or, equivalently, if s belongs to one of the multiplicative sets, then there exists $t\in R$ such that st belongs to the other.

Saturated multiplicative sets are not widely used explicitly, since, for verifying that a set is saturated, one must know *all* units of the ring.

## Terminology explained by the context

The term *localization* originates in the general trend of modern mathematics to study geometrical and topological objects *locally*, that is in terms of their behavior near each point. Examples of this trend are the fundamental concepts of manifolds, germs and sheafs. In algebraic geometry, an affine algebraic set can be identified with a quotient ring of a polynomial ring in such a way that the points of the algebraic set correspond to the maximal ideals of the ring (this is Hilbert's Nullstellensatz). This correspondence has been generalized for making the set of the prime ideals of a commutative ring a topological space equipped with the Zariski topology; this topological space is called the spectrum of the ring.

In this context, a *localization* by a multiplicative set may be viewed as the restriction of the spectrum of a ring to the subspace of the prime ideals (viewed as *points*) that do not intersect the multiplicative set.

Two classes of localizations are more commonly considered:

- The multiplicative set is the complement of a prime ideal ${\mathfrak {p}}$ of a ring R. In this case, one speaks of the "localization at ${\mathfrak {p}}$ ", or "localization at a point". The resulting ring, denoted $R_{\mathfrak {p}}$ is a local ring, and is the algebraic analog of a ring of germs.
- The multiplicative set consists of all powers of an element t of a ring R. The resulting ring is commonly denoted $R_{t},$ and its spectrum is the Zariski open set of the prime ideals that do not contain t. Thus the localization is the analog of the restriction of a topological space to a neighborhood of a point (every prime ideal has a neighborhood basis consisting of Zariski open sets of this form).

In number theory and algebraic topology, when working over the ring $\mathbb {Z}$ of integers, one refers to a property relative to an integer n as a property true *at* n or *away* from n, depending on the localization that is considered. "**Away from** n" means that the property is considered after localization by the powers of n, and, if p is a prime number, "at p" means that the property is considered after localization at the prime ideal $p\mathbb {Z}$ . This terminology can be explained by the fact that, if p is prime, the nonzero prime ideals of the localization of $\mathbb {Z}$ are either the singleton set {*p*} or its complement in the set of prime numbers.

## Localization and saturation of ideals

Let S be a multiplicative set in a commutative ring R, and $j\colon R\to S^{-1}R$ be the canonical ring homomorphism. Given an ideal I in R, let $S^{-1}I$ be the set of the fractions in $S^{-1}R$ whose numerator is in I. This is an ideal of $S^{-1}R,$ which is generated by *j*(*I*), and called the *localization* of I by S.

The *saturation* of I by S is $j^{-1}(S^{-1}I);$ it is an ideal of R, which can also defined as the set of the elements $r\in R$ such that there exists $s\in S$ with $sr\in I.$

Many properties of ideals are either preserved by saturation and localization, or can be characterized by simpler properties of localization and saturation. In what follows, S is a multiplicative set in a ring R, and I and J are ideals of R; the saturation of an ideal I by a multiplicative set S is denoted $\operatorname {sat} _{S}(I),$ or, when the multiplicative set S is clear from the context, $\operatorname {sat} (I).$

- $1\in S^{-1}I\quad \iff \quad 1\in \operatorname {sat} (I)\quad \iff \quad S\cap I\neq \emptyset$
- $I\subseteq J\quad \ \implies \quad \ S^{-1}I\subseteq S^{-1}J\quad \ {\text{and}}\quad \ \operatorname {sat} (I)\subseteq \operatorname {sat} (J)$ (this is not always true for strict inclusions)
- $S^{-1}(I\cap J)=S^{-1}I\cap S^{-1}J,\qquad \,\operatorname {sat} (I\cap J)=\operatorname {sat} (I)\cap \operatorname {sat} (J)$
- $S^{-1}(I+J)=S^{-1}I+S^{-1}J,\qquad \operatorname {sat} (I+J)=\operatorname {sat} (I)+\operatorname {sat} (J)$
- $S^{-1}(I\cdot J)=S^{-1}I\cdot S^{-1}J,\qquad \quad \operatorname {sat} (I\cdot J)=\operatorname {sat} (I)\cdot \operatorname {sat} (J)$
- If ${\mathfrak {p}}$ is a prime ideal such that ${\mathfrak {p}}\cap S=\emptyset ,$ then $S^{-1}{\mathfrak {p}}$ is a prime ideal and ${\mathfrak {p}}=\operatorname {sat} ({\mathfrak {p}})$ ; if the intersection is nonempty, then $S^{-1}{\mathfrak {p}}=S^{-1}R$ and $\operatorname {sat} ({\mathfrak {p}})=R.$

## Localization of a module

Let R be a commutative ring, S be a multiplicative set in R , and M be an R -module. The **localization of the module** M by S , denoted $S^{-1}M$ , is an $S^{-1}R$ -module that is constructed exactly as the localization of R , except that the numerators of the fractions belong to M . That is, as a set, it consists of equivalence classes, denoted ${\frac {m}{s}}$ , of pairs $(m,s)$ , where $m\in M$ and $s\in S,$ and two pairs $(m,s)$ and $(n,t)$ are equivalent if there is an element u in S such that

$u(sn-tm)=0.$

Addition and scalar multiplication are defined as for usual fractions (in the following formula, $r\in R,$ $s,t\in S,$ and $m,n\in M$ ):

${\frac {m}{s}}+{\frac {n}{t}}={\frac {tm+sn}{st}},$

${\frac {r}{s}}{\frac {m}{t}}={\frac {rm}{st}}.$

Moreover, $S^{-1}M$ is also an R -module with scalar multiplication

$r\,{\frac {m}{s}}={\frac {r}{1}}{\frac {m}{s}}={\frac {rm}{s}}.$

It is straightforward to check that these operations are well-defined, that is, they give the same result for different choices of representatives of fractions.

The localization of a module can be equivalently defined by using tensor products:

$S^{-1}M=S^{-1}R\otimes _{R}M.$

The proof of equivalence (up to a canonical isomorphism) can be done by showing that the two definitions satisfy the same universal property.

### Module properties

If M is a submodule of an R-module N, and S is a multiplicative set in R, one has $S^{-1}M\subseteq S^{-1}N.$ This implies that, if $f\colon M\to N$ is an injective module homomorphism, then

$S^{-1}R\otimes _{R}f:\quad S^{-1}R\otimes _{R}M\to S^{-1}R\otimes _{R}N$

is also an injective homomorphism.

Since the tensor product is a right exact functor, this implies that localization by S maps exact sequences of R-modules to exact sequences of $S^{-1}R$ -modules. In other words, localization is an exact functor, and $S^{-1}R$ is a flat R-module.

This flatness and the fact that localization solves a universal property make that localization preserves many properties of modules and rings, and is compatible with solutions of other universal properties. For example, the natural map

$S^{-1}(M\otimes _{R}N)\to S^{-1}M\otimes _{S^{-1}R}S^{-1}N$

is an isomorphism. If M is a finitely presented module, the natural map

$S^{-1}\operatorname {Hom} _{R}(M,N)\to \operatorname {Hom} _{S^{-1}R}(S^{-1}M,S^{-1}N)$

is also an isomorphism.

If a module *M* is a finitely generated over *R*, one has

$S^{-1}(\operatorname {Ann} _{R}(M))=\operatorname {Ann} _{S^{-1}R}(S^{-1}M),$

where $\operatorname {Ann}$ denotes annihilator, that is the ideal of the elements of the ring that map to zero all elements of the module. In particular,

$S^{-1}M=0\quad \iff \quad S\cap \operatorname {Ann} _{R}(M)\neq \emptyset ,$

that is, if $tM=0$ for some $t\in S.$

## Localization at primes

The definition of a prime ideal implies immediately that the complement $S=R\setminus {\mathfrak {p}}$ of a prime ideal ${\mathfrak {p}}$ in a commutative ring R is a multiplicative set. In this case, the localization $S^{-1}R$ is commonly denoted $R_{\mathfrak {p}}.$ The ring $R_{\mathfrak {p}}$ is a local ring, that is called *the local ring of R* at ${\mathfrak {p}}.$ This means that ${\mathfrak {p}}\,R_{\mathfrak {p}}={\mathfrak {p}}\otimes _{R}R_{\mathfrak {p}}$ is the unique maximal ideal of the ring $R_{\mathfrak {p}}.$ Analogously one can define the localization of a module M at a prime ideal ${\mathfrak {p}}$ of R. Again, the localization $S^{-1}M$ is commonly denoted $M_{\mathfrak {p}}$ .

Such localizations are fundamental for commutative algebra and algebraic geometry for several reasons. One is that local rings are often easier to study than general commutative rings, in particular because of Nakayama lemma. However, the main reason is that many properties are true for a ring if and only if they are true for all its local rings. For example, a ring is regular if and only if all its local rings are regular local rings.

Properties of a ring that can be characterized on its local rings are called *local properties*, and are often the algebraic counterpart of geometric local properties of algebraic varieties, which are properties that can be studied by restriction to a small neighborhood of each point of the variety. (There is another concept of local property that refers to localization to Zariski open sets; see § Localization to Zariski open sets, below.)

Many local properties are a consequence of the fact that the module

$\bigoplus _{\mathfrak {p}}R_{\mathfrak {p}}$

is a faithfully flat module when the direct sum is taken over all prime ideals (or over all maximal ideals of R). See also Faithfully flat descent.

### Examples of local properties

A property P of an R-module M is a *local property* if the following conditions are equivalent:

- P holds for M.
- P holds for all $M_{\mathfrak {p}},$ where ${\mathfrak {p}}$ is a prime ideal of R.
- P holds for all $M_{\mathfrak {m}},$ where ${\mathfrak {m}}$ is a maximal ideal of R.

The following are local properties:

- M is zero.
- M is torsion-free (in the case where R is a commutative domain).
- M is a flat module.
- M is an invertible module (in the case where R is a commutative domain, and M is a submodule of the field of fractions of R).
- $f\colon M\to N$ is injective (resp. surjective), where N is another R-module.

On the other hand, some properties are not local properties. For example, an infinite direct product of fields is not an integral domain nor a Noetherian ring, while all its local rings are fields, and therefore Noetherian integral domains.

## Non-commutative case

Localizing non-commutative rings is more difficult. While the localization exists for every set *S* of prospective units, it might take a different form to the one described above. One condition which ensures that the localization is well behaved is the Ore condition.

One case for non-commutative rings where localization has a clear interest is for rings of differential operators. It has the interpretation, for example, of adjoining a formal inverse *D*−1 for a differentiation operator *D*. This is done in many contexts in methods for differential equations. There is now a large mathematical theory about it, named microlocalization, connecting with numerous other branches. The *micro-* tag is to do with connections with Fourier theory, in particular.

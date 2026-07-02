---
title: "Dedekind domain"
source: https://en.wikipedia.org/wiki/Dedekind_domain
domain: algebraic-number-theory
license: CC-BY-SA-4.0
tags: algebraic number theory, ring of integers, ideal class group, dedekind domain
fetched: 2026-07-02
---

# Dedekind domain

In mathematics, a **Dedekind domain** or **Dedekind ring**, named after Richard Dedekind, is an integral domain in which every nonzero proper ideal factors into a product of prime ideals. It can be shown that such a factorization is then necessarily unique up to the order of the factors. There are at least three other characterizations of Dedekind domains that are sometimes taken as the definition: see below.

A field is a commutative ring in which there are no nontrivial proper ideals, so that any field is a Dedekind domain, however in a rather vacuous way. Some authors add the requirement that a Dedekind domain not be a field. Many more authors state theorems for Dedekind domains with the implicit proviso that they may require trivial modifications for the case of fields.

An immediate consequence of the definition is that every principal ideal domain (PID) is a Dedekind domain. In fact a Dedekind domain is a unique factorization domain (UFD) if and only if it is a PID.

## The prehistory of Dedekind domains

In the 19th century it became a common technique to gain insight into integer solutions of polynomial equations using rings of algebraic numbers of higher degree. For instance, fix a positive integer m . In the attempt to determine which integers are represented by the quadratic form $x^{2}+my^{2}$ , it is natural to factor the quadratic form into $(x+{\sqrt {-m}}y)(x-{\sqrt {-m}}y)$ , the factorization taking place in the ring of integers of the quadratic field $\mathbb {Q} ({\sqrt {-m}})$ . Similarly, for a positive integer n the polynomial $z^{n}-y^{n}$ (which is relevant for solving the Fermat equation $x^{n}+y^{n}=z^{n}$ ) can be factored over the ring $\mathbb {Z} [\zeta _{n}]$ , where $\zeta _{n}$ is a primitive *n*-th root of unity.

For a few small values of m and n these rings of algebraic integers are PIDs, and this can be seen as an explanation of the classical successes of Fermat ( $m=1,n=4$ ) and Euler ( $m=2,3,n=3$ ). By this time a procedure for determining whether the ring of all algebraic integers of a given quadratic field $\mathbb {Q} ({\sqrt {D}})$ is a PID was well known to the quadratic form theorists. Especially, Gauss had looked at the case of imaginary quadratic fields: he found exactly nine values of $D<0$ for which the ring of integers is a PID and conjectured that there were no further values. (Gauss's conjecture was proven more than one hundred years later by Kurt Heegner, Alan Baker and Harold Stark.) However, this was understood (only) in the language of equivalence classes of quadratic forms, so that in particular the analogy between quadratic forms and the Fermat equation seems not to have been perceived. In 1847 Gabriel Lamé announced a solution of Fermat's Last Theorem for all $n>2$ ; that is, that the Fermat equation has no solutions in nonzero integers, but it turned out that his solution hinged on the assumption that the cyclotomic ring $\mathbb {Z} [\zeta _{n}]$ is a UFD. Ernst Kummer had shown three years before that this was not the case already for $n=23$ (the full, finite list of values for which $\mathbb {Z} [\zeta _{n}]$ is a UFD is now known). At the same time, Kummer developed powerful new methods to prove Fermat's Last Theorem at least for a large class of prime exponents n using what we now recognize as the fact that the ring $\mathbb {Z} [\zeta _{n}]$ is a Dedekind domain. In fact Kummer worked not with ideals but with "ideal numbers", and the modern definition of an ideal was given by Dedekind.

By the 20th century, algebraists and number theorists had come to realize that the condition of being a PID is rather delicate, whereas the condition of being a Dedekind domain is quite robust. For instance the ring of ordinary integers is a PID, but as seen above the ring ${\mathcal {O}}_{K}$ of algebraic integers in a number field K need not be a PID. In fact, although Gauss also conjectured that there are infinitely many primes p such that the ring of integers of $\mathbb {Q} ({\sqrt {p}})$ is a PID, it is not yet known whether there are infinitely many number fields K (of arbitrary degree) such that ${\mathcal {O}}_{K}$ is a PID. On the other hand, the ring of integers in a number field is always a Dedekind domain.

Another illustration of the delicate/robust dichotomy is the fact that being a Dedekind domain is, among Noetherian domains, a **local** property: a Noetherian domain R is Dedekind iff for every maximal ideal M of R the localization $R_{M}$ is a Dedekind ring. But a local domain is a Dedekind ring iff it is a PID iff it is a discrete valuation ring (DVR), so the same local characterization cannot hold for PIDs: rather, one may say that the concept of a Dedekind ring is the **globalization** of that of a DVR.

## Alternative definitions

For an integral domain R that is not a field, all of the following conditions are equivalent:

(DD1)

Every nonzero proper ideal factors into primes.

(DD2)

R

is Noetherian, and the localization at each maximal ideal is a discrete valuation ring.

(DD3)

Every nonzero

fractional ideal

of

R

is invertible.

(DD4)

R

is an

integrally closed

, Noetherian domain with

Krull dimension

one (that is, every nonzero prime ideal is maximal).

(DD5)

For any two ideals

I

and

J

in

R

,

I

is contained in

J

if and only if

J

divides

I

as ideals. That is, there exists an ideal

H

such that

$I=JH$

. A commutative ring (not necessarily a domain) with unity satisfying this condition is called a containment-division ring (CDR).

Thus a Dedekind domain is a domain that either is a field, or satisfies any one, and hence all five, of (DD1) through (DD5). Which of these conditions one takes as the definition is therefore merely a matter of taste. In practice, it is often easiest to verify (DD4).

Any ideal in a Dedekind domain is generated by at most two elements. In fact, a stronger condition gives another characterization of Dedekind domains: an integral domain R is a Dedekind domain if and only if for any nonzero ideal $I\subset R$ and nonzero $a\in I$ there exists $b\in I$ such that $I=(a,b)$ .

A Krull domain is a higher-dimensional analog of a Dedekind domain: a Dedekind domain that is not a field is a Krull domain of dimension 1. This notion can be used to study the various characterizations of a Dedekind domain. In fact, this is the definition of a Dedekind domain used in Bourbaki's "Commutative algebra".

A Dedekind domain can also be characterized in terms of homological algebra: an integral domain is a Dedekind domain if and only if it is a hereditary ring; that is, every submodule of a projective module over it is projective. Similarly, an integral domain is a Dedekind domain if and only if every divisible module over it is injective.

## Some examples of Dedekind domains

All principal ideal domains and therefore all discrete valuation rings are Dedekind domains.

The ring $R={\mathcal {O}}_{K}$ of algebraic integers in a number field *K* is Noetherian, integrally closed, and of dimension one: to see the last property, observe that for any nonzero prime ideal *I* of *R*, *R*/*I* is a finite set, and recall that a finite integral domain is a field; so by (DD4) *R* is a Dedekind domain. As above, this includes all the examples considered by Kummer and Dedekind and was the motivating case for the general definition, and these remain among the most studied examples.

The other class of Dedekind rings that is arguably of equal importance comes from geometry: let *C* be a nonsingular geometrically integral *affine* algebraic curve over a field *k*. Then the coordinate ring *k*[*C*] of regular functions on *C* is a Dedekind domain. This is largely clear simply from translating geometric terms into algebra: the coordinate ring of any affine variety is, by definition, a finitely generated *k*-algebra, hence Noetherian; moreover *curve* means *dimension one* and *nonsingular* implies (and, in dimension one, is equivalent to) *normal*, which by definition means *integrally closed*.

Both of these constructions can be viewed as special cases of the following basic result:

**Theorem**: Let *R* be a Dedekind domain with fraction field *K*. Let *L* be a finite degree field extension of *K* and denote by *S* the integral closure of *R* in *L*. Then *S* is itself a Dedekind domain.

Applying this theorem when *R* is itself a PID gives us a way of building Dedekind domains out of PIDs. Taking *R* = **Z**, this construction says precisely that rings of integers of number fields are Dedekind domains. Taking *R* = *k*[*t*], one obtains the above case of nonsingular affine curves as branched coverings of the affine line.

Zariski and Samuel were sufficiently taken with this construction to ask whether every Dedekind domain arises from it; that is, by starting with a PID and taking the integral closure in a finite degree field extension. A surprisingly simple negative answer was given by L. Claborn.

If the situation is as above but the extension *L* of *K* is algebraic of infinite degree, then it is still possible for the integral closure *S* of *R* in *L* to be a Dedekind domain, but it is not guaranteed. For example, take again *R* = **Z**, *K* = **Q** and now take *L* to be the field ${\overline {\textbf {Q}}}$ of all algebraic numbers. The integral closure is then the ring ${\overline {\textbf {Z}}}$ of all algebraic integers. Since the square root of an algebraic integer is again an algebraic integer, it is not possible to factor any nonzero nonunit algebraic integer into a finite product of irreducible elements, which implies that ${\overline {\textbf {Z}}}$ is not even Noetherian. In general, the integral closure of a Dedekind domain in an infinite algebraic extension is a Prüfer domain; it turns out that the ring of algebraic integers is slightly more special than this: it is a Bézout domain.

## Fractional ideals and the class group

Let *R* be an integral domain with fraction field *K*. A fractional ideal is a nonzero *R*-submodule *I* of *K* for which there exists a nonzero *x* in *K* such that $xI\subset R.$

Given two fractional ideals *I* and *J*, one defines their product *IJ* as the set of all finite sums $\sum _{n}i_{n}j_{n},\,i_{n}\in I,\,j_{n}\in J$ : the product *IJ* is again a fractional ideal. The set Frac(*R*) of all fractional ideals endowed with the above product is a commutative semigroup and in fact a monoid: the identity element is the fractional ideal *R*.

For any fractional ideal *I*, one may define the fractional ideal

$I^{*}=(R:I)=\{x\in K\mid xI\subset R\}.$

One then tautologically has $I^{*}I\subset R$ . In fact one has equality if and only if *I*, as an element of the monoid of Frac(*R*), is invertible. In other words, if *I* has any inverse, then the inverse must be $I^{*}$ .

A **principal fractional ideal** is one of the form $xR$ for some nonzero *x* in *K*. Note that each principal fractional ideal is invertible, the inverse of $xR$ being simply ${\frac {1}{x}}R$ . We denote the subgroup of principal fractional ideals by Prin(*R*).

A domain *R* is a PID if and only if every fractional ideal is principal. In this case, we have Frac(*R*) = Prin(*R*) = $K^{\times }/R^{\times }$ , since two principal fractional ideals $xR$ and $yR$ are equal iff $xy^{-1}$ is a unit in *R*.

For a general domain *R*, it is meaningful to take the quotient of the monoid Frac(*R*) of all fractional ideals by the submonoid Prin(*R*) of principal fractional ideals. However this quotient itself is generally only a monoid. In fact it is easy to see that the class of a fractional ideal I in Frac(*R*)/Prin(*R*) is invertible if and only if I itself is invertible.

Now we can appreciate (DD3): in a Dedekind domain (and only in a Dedekind domain) every fractional ideal is invertible. Thus these are precisely the class of domains for which Frac(*R*)/Prin(*R*) forms a group, the ideal class group Cl(*R*) of *R*. This group is trivial if and only if *R* is a PID, so can be viewed as quantifying the obstruction to a general Dedekind domain being a PID.

For an arbitrary domain one may define the Picard group Pic(*R*) as the group of invertible fractional ideals Inv(*R*) modulo the subgroup of principal fractional ideals. For a Dedekind domain this is of course the same as the ideal class group. However, on a more general class of domains, including Noetherian domains and Krull domains, the ideal class group is constructed in a different way, and there is a canonical homomorphism

Pic(

R

) → Cl(

R

)

which is however generally neither injective nor surjective. This is an affine analogue of the distinction between Cartier divisors and Weil divisors on a singular algebraic variety.

A theorem of L. Claborn asserts that for any abelian group *G* whatsoever, there exists a Dedekind domain *R* whose ideal class group is isomorphic to *G*. Later, C.R. Leedham-Green showed that such an *R* may be constructed as the integral closure of a PID in a quadratic field extension. In 1976, M. Rosen showed how to realize any countable abelian group as the class group of a Dedekind domain that is a subring of the rational function field of an elliptic curve, and conjectured that such an "elliptic" construction should be possible for a general abelian group. Rosen's conjecture was proven in 2008 by P.L. Clark.

In contrast, one of the basic theorems in algebraic number theory asserts that the class group of the ring of integers of a number field is finite. Its cardinality is called the class number.

## Finitely generated modules over a Dedekind domain

In view of the well known and exceedingly useful structure theorem for finitely generated modules over a principal ideal domain (PID), it is natural to ask for a corresponding theory for finitely generated modules over a Dedekind domain.

Let us briefly recall the structure theory in the case of a finitely generated module M over a PID R . We define the torsion submodule T to be the set of elements m of M such that $rm=0$ for some nonzero r in R . Then:

(M1) T can be decomposed into a direct sum of cyclic torsion modules, each of the form $R/I$ for some nonzero ideal I of R . By the Chinese Remainder Theorem, each $R/I$ can further be decomposed into a direct sum of submodules of the form $R/P^{i}$ , where $P^{i}$ is a power of a prime ideal. This decomposition need not be unique, but any two decompositions

$T\cong R/P_{1}^{a_{1}}\oplus \cdots \oplus R/P_{r}^{a_{r}}\cong R/Q_{1}^{b_{1}}\oplus \cdots \oplus R/Q_{s}^{b_{s}}$

differ only in the order of the factors.

(M2) The torsion submodule is a direct summand. That is, there exists a complementary submodule P of M such that $M=T\oplus P$ .

(M3PID) P isomorphic to $R^{n}$ for a uniquely determined non-negative integer n . In particular, P is a finitely generated free module.

Now let M be a finitely generated module over an arbitrary Dedekind domain R . Then (M1) and (M2) hold verbatim. However, it follows from (M3PID) that a finitely generated torsionfree module P over a PID is free. In particular, it asserts that all fractional ideals are principal, a statement that is false whenever R is not a PID. In other words, the nontriviality of the class group $Cl(R)$ causes (M3PID) to fail. Remarkably, the additional structure in torsionfree finitely generated modules over an arbitrary Dedekind domain is precisely controlled by the class group, as we now explain. Over an arbitrary Dedekind domain one has

(M3DD) P is isomorphic to a direct sum of rank one projective modules: $P\cong I_{1}\oplus \cdots \oplus I_{r}$ . Moreover, for any rank one projective modules $I_{1},\ldots ,I_{r},J_{1},\ldots ,J_{s}$ , one has

$I_{1}\oplus \cdots \oplus I_{r}\cong J_{1}\oplus \cdots \oplus J_{s}$

if and only if

$r=s$

and

$I_{1}\otimes \cdots \otimes I_{r}\cong J_{1}\otimes \cdots \otimes J_{s}.\,$

Rank one projective modules can be identified with fractional ideals, and the last condition can be rephrased as

$[I_{1}\cdots I_{r}]=[J_{1}\cdots J_{s}]\in Cl(R).$

Thus a finitely generated torsionfree module of rank $n>0$ can be expressed as $R^{n-1}\oplus I$ , where I is a rank one projective module. The **Steinitz class** for P over R is the class $[I]$ of I in $Cl(R)$ : it is uniquely determined. A consequence of this is:

Theorem: Let R be a Dedekind domain. Then $K_{0}(R)\cong \mathbb {Z} \oplus Cl(R)$ , where $K_{0}(R)$ is the Grothendieck group of the commutative monoid of finitely generated projective R modules.

These results were established by Ernst Steinitz in 1912.

An additional consequence of this structure, which is not implicit in the preceding theorem, is that if the two projective modules over a Dedekind domain have the same class in the Grothendieck group, then they are in fact abstractly isomorphic.

## Locally Dedekind rings

There exist integral domains R that are locally but not globally Dedekind: the localization of R at each maximal ideal is a Dedekind ring (equivalently, a DVR) but R itself is not Dedekind. As mentioned above, such a ring cannot be Noetherian. It seems that the first examples of such rings were constructed by N. Nakano in 1953. In the literature such rings are sometimes called "proper almost Dedekind rings".

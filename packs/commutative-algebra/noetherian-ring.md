---
title: "Noetherian ring"
source: https://en.wikipedia.org/wiki/Noetherian_ring
domain: commutative-algebra
license: CC-BY-SA-4.0
tags: commutative algebra, noetherian ring, krull dimension, grobner basis
fetched: 2026-07-02
---

# Noetherian ring

In mathematics, a **Noetherian ring** is a ring that satisfies the ascending chain condition on left and right ideals. If the chain condition is satisfied only for left ideals or for right ideals, then the ring is said **left-Noetherian** or **right-Noetherian** respectively. Formally, every increasing sequence $I_{1}\subseteq I_{2}\subseteq I_{3}\subseteq \cdots$ of left (or right) ideals has a largest element; that is, there exists an n such that $I_{n}=I_{n+1}=\cdots .$

Equivalently, a ring is left-Noetherian (respectively right-Noetherian) if every left ideal (respectively right-ideal) is finitely generated. A ring is Noetherian if it is both left- and right-Noetherian.

Noetherian rings are fundamental in both commutative and noncommutative ring theory since many rings that are encountered in mathematics are Noetherian (in particular the ring of integers, polynomial rings, and rings of algebraic integers in number fields), and many general theorems on rings rely heavily on the Noetherian property (for example, the Lasker–Noether theorem and the Krull intersection theorem).

Noetherian rings are named after Emmy Noether, but the importance of the concept was recognized earlier by David Hilbert, with the proof of Hilbert's basis theorem (which asserts that polynomial rings are Noetherian) and Hilbert's syzygy theorem.

## Characterizations

For noncommutative rings, it is necessary to distinguish between three very similar concepts:

- A ring is **left-Noetherian** if it satisfies the ascending chain condition on left ideals.
- A ring is **right-Noetherian** if it satisfies the ascending chain condition on right ideals.
- A ring is **Noetherian** if it is both left- and right-Noetherian.

For commutative rings, all three concepts coincide, but in general they are different. There are rings that are left-Noetherian and not right-Noetherian, and vice versa.

There are other, equivalent, definitions for a ring *R* to be left-Noetherian:

- Every left ideal *I* in *R* is finitely generated, i.e. there exist elements $a_{1},\ldots ,a_{n}$ in *I* such that $I=Ra_{1}+\cdots +Ra_{n}$ .
- Every non-empty set of left ideals of *R*, partially ordered by inclusion, has a maximal element.

Similar results hold for right-Noetherian rings.

The following condition is also an equivalent condition for a ring *R* to be left-Noetherian and it is Hilbert's original formulation:

- Given a sequence $f_{1},f_{2},\dots$ of elements in *R*, there exists an integer n such that each $f_{i}$ is a finite linear combination ${\textstyle f_{i}=\sum _{j=1}^{n}r_{j}f_{j}}$ with coefficients $r_{j}$ in *R*.

For a commutative ring to be Noetherian it suffices that every prime ideal of the ring is finitely generated. However, it is not enough to ask that all the maximal ideals are finitely generated, as there is a non-Noetherian local ring whose maximal ideal is principal (see a counterexample to Krull's intersection theorem at Local ring#Commutative case.)

## Properties

- If *R* is a Noetherian ring, then the polynomial ring $R[X]$ is Noetherian by the Hilbert's basis theorem. By induction, $R[X_{1},\ldots ,X_{n}]$ is a Noetherian ring. Also, *R*[[*X*]], the power series ring, is a Noetherian ring.
- If *R* is a Noetherian ring and *I* is a two-sided ideal, then the quotient ring *R*/*I* is also Noetherian. Stated differently, the image of any ring homomorphism of a Noetherian ring is Noetherian.
- Every finitely-generated commutative algebra over a commutative Noetherian ring is Noetherian. (This follows from the two previous properties.)
- A ring *R* is left-Noetherian if and only if every finitely generated left *R*-module is a Noetherian module.
- If a commutative ring admits a faithful Noetherian module over it, then the ring is a Noetherian ring.
- (Eakin–Nagata) If a ring *A* is a subring of a commutative Noetherian ring *B* such that *B* is a finitely generated module over *A*, then *A* is a Noetherian ring.
- Similarly, if a ring *A* is a subring of a commutative Noetherian ring *B* such that *B* is faithfully flat over *A* (or more generally exhibits *A* as a pure subring), then *A* is a Noetherian ring (see the "faithfully flat" article for the reasoning).
- Every localization of a commutative Noetherian ring is Noetherian.
- A consequence of the Akizuki–Hopkins–Levitzki theorem is that every left Artinian ring is left Noetherian. Another consequence is that a left Artinian ring is right Noetherian if and only if it is right Artinian. The analogous statements with "right" and "left" interchanged are also true.
- A left Noetherian ring is left coherent and a left Noetherian domain is a left Ore domain.
- (Bass) A ring is (left/right) Noetherian if and only if every direct sum of injective (left/right) modules is injective. Every left injective module over a left Noetherian module can be decomposed as a direct sum of indecomposable injective modules. See also #Implication on injective modules below.
- In a commutative Noetherian ring, there are only finitely many minimal prime ideals. Also, the descending chain condition holds on prime ideals.
- In a commutative Noetherian domain *R*, every element can be factorized into irreducible elements (in short, *R* is a factorization domain). Thus, if, in addition, the factorization is unique up to multiplication of the factors by units, then *R* is a unique factorization domain.

## Examples

- Any field, including the fields of rational numbers, real numbers, and complex numbers, is Noetherian. (A field only has two ideals — itself and (0).)
- Any principal ideal ring, such as the integers, is Noetherian since every ideal is generated by a single element. This includes principal ideal domains and Euclidean domains.
- A Dedekind domain (e.g., rings of integers) is a Noetherian domain in which every ideal is generated by at most two elements.
- The coordinate ring of an affine variety is a Noetherian ring, as a consequence of the Hilbert basis theorem.
- The enveloping algebra *U* of a finite-dimensional Lie algebra ${\mathfrak {g}}$ is a both left and right Noetherian ring; this follows from the fact that the associated graded ring of *U* is a quotient of $\operatorname {Sym} ({\mathfrak {g}})$ , which is a polynomial ring over a field (the PBW theorem); thus, Noetherian. For the same reason, the Weyl algebra, and more general rings of differential operators, are Noetherian.
- The ring of polynomials in finitely-many variables over the integers or a field is Noetherian.

Rings that are not Noetherian tend to be (in some sense) very large. Here are some examples of non-Noetherian rings:

- The ring of polynomials in infinitely-many variables, *X*1, *X*2, *X*3, etc. The sequence of ideals (*X*1), (*X*1, *X*2), (*X*1, *X*2, *X*3), etc. is ascending, and does not terminate.
- The ring of all algebraic integers is not Noetherian. For example, it contains the infinite ascending chain of principal ideals: (2), (21/2), (21/4), (21/8), ...
- The ring of continuous functions from the real numbers to the real numbers is not Noetherian: Let *In* be the ideal of all continuous functions *f* such that *f*(*x*) = 0 for all *x* ≥ *n*. The sequence of ideals *I*0, *I*1, *I*2, etc., is an ascending chain that does not terminate.
- The ring of stable homotopy groups of spheres is not Noetherian.

However, a non-Noetherian ring can be a subring of a Noetherian ring. Since any integral domain is a subring of a field, any integral domain that is not Noetherian provides an example. To give a less trivial example,

- The ring of rational functions generated by *x* and *y*/*x**n* over a field *k* is a subring of the field *k*(*x*,*y*) in only two variables.

Indeed, there are rings that are right Noetherian, but not left Noetherian, so that one must be careful in measuring the "size" of a ring this way. For example, if *L* is a subgroup of **Q**2 isomorphic to **Z**, let *R* be the ring of homomorphisms *f* from **Q**2 to itself satisfying *f*(*L*) ⊂ *L*. Choosing a basis, we can describe the same ring *R* as

$R=\left\{\left.{\begin{bmatrix}a&\beta \\0&\gamma \end{bmatrix}}\,\right\vert \,a\in \mathbf {Z} ,\beta \in \mathbf {Q} ,\gamma \in \mathbf {Q} \right\}.$

This ring is right Noetherian, but not left Noetherian; the subset *I* ⊂ *R* consisting of elements with *a* = 0 and *γ* = 0 is a left ideal that is not finitely generated as a left *R*-module.

If *R* is a commutative subring of a left Noetherian ring *S*, and *S* is finitely generated as a left *R*-module, then *R* is Noetherian. (In the special case when *S* is commutative, this is known as Eakin's theorem.) However, this is not true if *R* is not commutative: the ring *R* of the previous paragraph is a subring of the left Noetherian ring *S* = Hom(**Q**2, **Q**2), and *S* is finitely generated as a left *R*-module, but *R* is not left Noetherian.

A unique factorization domain is not necessarily a Noetherian ring. It does satisfy a weaker condition: the ascending chain condition on principal ideals. A ring of polynomials in infinitely-many variables is an example of a non-Noetherian unique factorization domain.

A valuation ring is not Noetherian unless it is a principal ideal domain. It gives an example of a ring that arises naturally in algebraic geometry but is not Noetherian.

### Noetherian group rings

Consider the group ring $R[G]$ of a group G over a ring R . It is a ring, and an associative algebra over R if R is commutative. For a group G and a commutative ring R , the following two conditions are equivalent.

- The ring $R[G]$ is left-Noetherian.
- The ring $R[G]$ is right-Noetherian.

This is because there is a bijection between the left and right ideals of the group ring in this case, via the R -associative algebra homomorphism

$R[G]\to R[G]^{\operatorname {op} },$

$g\mapsto g^{-1}\qquad (\forall g\in G).$

Let G be a group and R a ring. If $R[G]$ is left/right/two-sided Noetherian, then R is left/right/two-sided Noetherian and G is a Noetherian group. Conversely, if R is a Noetherian commutative ring and G is an extension of a Noetherian solvable group (i.e. a polycyclic group) by a finite group, then $R[G]$ is two-sided Noetherian. On the other hand, however, there is a Noetherian group G whose group ring over any Noetherian commutative ring is not two-sided Noetherian.

## Key theorems

Many important theorems in ring theory (especially the theory of commutative rings) rely on the assumptions that the rings are Noetherian.

### Commutative case

- Over a commutative Noetherian ring, each ideal has a primary decomposition, meaning that it can be written as an intersection of finitely many primary ideals (whose radicals are all distinct) where an ideal *Q* is called primary if it is proper and whenever *xy* ∈ *Q*, either *x* ∈ *Q* or *y* *n* ∈ *Q* for some positive integer *n*. For example, if an element $f=p_{1}^{n_{1}}\cdots p_{r}^{n_{r}}$ is a product of powers of distinct prime elements, then $(f)=(p_{1}^{n_{1}})\cap \cdots \cap (p_{r}^{n_{r}})$ and thus the primary decomposition is a direct generalization of prime factorization of integers and polynomials.
- A Noetherian ring is defined in terms of ascending chains of ideals. The Artin–Rees lemma, on the other hand, gives some information about a descending chain of ideals given by powers of ideals $I\supseteq I^{2}\supseteq I^{3}\supseteq \cdots$ . It is a technical tool that is used to prove other key theorems such as the Krull intersection theorem.
- The dimension theory of commutative rings behaves poorly over non-Noetherian rings; the very fundamental theorem, Krull's principal ideal theorem, already relies on the "Noetherian" assumption. Here, in fact, the "Noetherian" assumption is often not enough and (Noetherian) universally catenary rings, those satisfying a certain dimension-theoretic assumption, are often used instead. Noetherian rings appearing in applications are mostly universally catenary.

### Non-commutative case

- Goldie's theorem

## Implication on injective modules

Given a ring, there is a close connection between the behaviors of injective modules over the ring and whether the ring is a Noetherian ring or not. Namely, given a ring *R*, the following are equivalent:

- *R* is a left Noetherian ring.
- (Bass) Each direct sum of injective left *R*-modules is injective.
- Each injective left *R*-module is a direct sum of indecomposable injective modules.
- (Faith–Walker) There exists a cardinal number ${\mathfrak {c}}$ such that each injective left module over *R* is a direct sum of ${\mathfrak {c}}$ -generated modules (a module is ${\mathfrak {c}}$ -generated if it has a generating set of cardinality at most ${\mathfrak {c}}$ ).
- There exists a left *R*-module *H* such that every left *R*-module embeds into a direct sum of copies of *H*.

The endomorphism ring of an indecomposable injective module is local and thus Azumaya's theorem says that, over a left Noetherian ring, each indecomposable decomposition of an injective module is equivalent to one another (a variant of the Krull–Schmidt theorem).

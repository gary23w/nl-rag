---
title: "Lattice (order)"
source: https://en.wikipedia.org/wiki/Lattice_(order)
domain: abstract-interpretation
license: CC-BY-SA-4.0
tags: abstract interpretation, galois connection, abstract domain, widening operator
fetched: 2026-07-02
---

# Lattice (order)

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

A **lattice** is an abstract structure studied in the mathematical subdisciplines of order theory and abstract algebra. It consists of a partially ordered set in which every pair of elements has a unique supremum (also called a least upper bound or join) and a unique infimum (also called a greatest lower bound or meet). An example is given by the power set of a set, partially ordered by inclusion, for which the supremum is the union and the infimum is the intersection. Another example is given by the natural numbers, partially ordered by divisibility, for which the supremum is the least common multiple and the infimum is the greatest common divisor.

Lattices can also be characterized as algebraic structures satisfying certain axiomatic identities. Since the two definitions are equivalent, lattice theory draws on both order theory and universal algebra. The class of lattices can be generalized to semilattices, and some notable subclasses of lattices are Heyting algebras, Boolean algebras, distributive lattices, and geometric lattices (matroids). These *lattice-like* structures all admit order-theoretic as well as algebraic descriptions.

The sub-field that studies lattices is called **lattice theory**.

## Definition

A lattice can be defined either order-theoretically as a partially ordered set, or as an algebraic structure.

### As partially ordered set

A partially ordered set (poset) $(L,\leq )$ is called a **lattice** if it is both a join- and a meet-semilattice, i.e. each two-element subset $\{a,b\}\subseteq L$ has a join (i.e. least upper bound, denoted by $a\vee b$ ) and dually a meet (i.e. greatest lower bound, denoted by $a\wedge b$ ). This definition makes $\,\wedge \,$ and $\,\vee \,$ binary operations. Both operations are monotone with respect to the given order: $a_{1}\leq a_{2}$ and $b_{1}\leq b_{2}$ implies that $a_{1}\vee b_{1}\leq a_{2}\vee b_{2}$ and $a_{1}\wedge b_{1}\leq a_{2}\wedge b_{2}.$

It follows by an induction argument that every non-empty finite subset of a lattice has a least upper bound and a greatest lower bound. With additional assumptions, further conclusions may be possible; see *Completeness (order theory)* for more discussion of this subject. That article also discusses how one may rephrase the above definition in terms of the existence of suitable Galois connections between related partially ordered sets—an approach of special interest for the category theoretic approach to lattices, and for formal concept analysis.

Given a subset of a lattice, $H\subseteq L,$ meet and join restrict to partial functions – they are undefined if their value is not in the subset $H.$ The resulting structure on H is called a **partial lattice**. In addition to this extrinsic definition as a subset of some other algebraic structure (a lattice), a partial lattice can also be intrinsically defined as a set with two partial binary operations satisfying certain axioms.

### As algebraic structure

A **lattice** is an algebraic structure $(L,\vee ,\wedge )$ , consisting of a set L and two binary, commutative and associative operations $\vee$ and $\wedge$ on L satisfying the following axiomatic identities (sometimes called *absorption laws*) for all elements $a,b\in L$  : $a\vee (a\wedge b)=a$ $a\wedge (a\vee b)=a$

The following two identities are also usually regarded as axioms, even though they follow from the two absorption laws taken together. These are called *idempotent laws*. $a\vee a=a$ $a\wedge a=a$

These axioms assert that both $(L,\vee )$ and $(L,\wedge )$ are semilattices. The absorption laws, the only axioms above in which both meet and join appear, distinguish a lattice from an arbitrary pair of semilattice structures and assure that the two semilattices interact appropriately. In particular, each semilattice is the dual of the other. The absorption laws can be viewed as a requirement that the meet and join semilattices define the same partial order.

### Connection between the two definitions

An order-theoretic lattice gives rise to the two binary operations $\vee$ and $\wedge .$ Since the commutative, associative and absorption laws can easily be verified for these operations, they make $(L,\vee ,\wedge )$ into a lattice in the algebraic sense.

The converse is also true. Given an algebraically defined lattice $(L,\vee ,\wedge ),$ one can define a partial order $\leq$ on L by setting $a\leq b{\text{ if }}a=a\wedge b,{\text{ or }}$ $a\leq b{\text{ if }}b=a\vee b,$ for all elements $a,b\in L.$ The laws of absorption ensure that both definitions are equivalent: $a=a\wedge b{\text{ implies }}b=b\vee (b\wedge a)=(a\wedge b)\vee b=a\vee b$ and dually for the other direction.

One can now check that the relation $\leq$ introduced in this way defines a partial ordering within which binary meets and joins are given through the original operations $\vee$ and $\wedge .$

Since the two definitions of a lattice are equivalent, one may freely invoke aspects of either definition in any way that suits the purpose at hand.

## Bounded lattice

A **bounded lattice** is a lattice that additionally has a **greatest element** (also called **maximum**, or **top** element, and denoted by 1 or $\top$ ) and a **least element** (also called **minimum**, or **bottom**, denoted by 0 or $\bot$ ), which satisfy $0\leq x\leq 1\;{\text{ for every }}x\in L.$

A bounded lattice may also be defined as an algebraic structure of the form $(L,\vee ,\wedge ,0,1)$ such that $(L,\vee ,\wedge )$ is a lattice, 0 (the lattice's bottom) is the identity element for the join operation $\vee ,$ and 1 (the lattice's top) is the identity element for the meet operation $\wedge .$ $a\vee 0=a$ $a\wedge 1=a$

It can be shown that a partially ordered set is a bounded lattice if and only if every finite set of elements (including the empty set) has a join and a meet.

Every lattice can be embedded into a bounded lattice by adding a greatest and a least element. Furthermore, every non-empty finite lattice is bounded, by taking the join (respectively, meet) of all elements, denoted by ${\textstyle 1=\bigvee L=a_{1}\lor \cdots \lor a_{n}}$ (respectively ${\textstyle 0=\bigwedge L=a_{1}\land \cdots \land a_{n}}$ ) where $L=\left\{a_{1},\ldots ,a_{n}\right\}$ is the set of all elements.

## Connection to other algebraic structures

Lattices have some connections to the family of group-like algebraic structures. Because meet and join both commute and associate, a lattice can be viewed as consisting of two commutative semigroups having the same domain. For a bounded lattice, these semigroups are in fact commutative monoids. The absorption law is the only defining identity that is peculiar to lattice theory. A bounded lattice can also be thought of as a commutative rig without the distributive axiom.

By commutativity, associativity and idempotence one can think of join and meet as operations on non-empty finite sets, rather than on pairs of elements. In a bounded lattice the join and meet of the empty set can also be defined (as 0 and $1,$ respectively). This makes bounded lattices somewhat more natural than general lattices, and many authors require all lattices to be bounded.

The algebraic interpretation of lattices plays an essential role in universal algebra.

## Examples

- (Pic. 1: Subsets of '"`UNIQ--postMath-00000049-QINU`"' under set inclusion. The name "lattice" is suggested by the form of the Hasse diagram depicting it.) **Pic. 1:** Subsets of $\{x,y,z\},$ under set inclusion. The name "lattice" is suggested by the form of the Hasse diagram depicting it.
- (Pic. 2: Lattice of integer divisors of 60, ordered by "divides".) **Pic. 2:** Lattice of integer divisors of 60, ordered by "*divides*".
- (Pic. 3: Lattice of partitions of '"`UNIQ--postMath-0000004A-QINU`"' ordered by "refines".) **Pic. 3:** Lattice of partitions of $\{1,2,3,4\},$ ordered by "*refines*".
- (Pic. 4: Lattice of positive integers, ordered by '"`UNIQ--postMath-0000004B-QINU`"') **Pic. 4:** Lattice of positive integers, ordered by $\,\leq ,$
- (Pic. 5: Lattice of nonnegative integer pairs, ordered componentwise.) **Pic. 5:** Lattice of nonnegative integer pairs, ordered componentwise.

- For any set $A,$ the collection of all subsets of A (called the power set of A ) can be ordered via subset inclusion to obtain a lattice bounded by A itself and the empty set. In this lattice, the supremum is provided by set union and the infimum is provided by set intersection (see Pic. 1).
- For any set $A,$ the collection of all finite subsets of $A,$ ordered by inclusion, is also a lattice, and will be bounded if and only if A is finite.
- For any set $A,$ the collection of all partitions of $A,$ ordered by refinement, is a lattice (see Pic. 3).
- The positive integers in their usual order form an unbounded lattice, under the operations of "min" and "max". 1 is bottom; there is no top (see Pic. 4).
- The Cartesian square of the natural numbers, ordered so that $(a,b)\leq (c,d)$ if $a\leq c{\text{ and }}b\leq d.$ The pair $(0,0)$ is the bottom element; there is no top (see Pic. 5).
- The natural numbers also form a lattice under the operations of taking the greatest common divisor and least common multiple, with divisibility as the order relation: $a\leq b$ if a divides $b.$ 1 is bottom; 0 is top. Pic. 2 shows a finite sublattice.
- Every complete lattice (also see below) is a (rather specific) bounded lattice. This class gives rise to a broad range of practical examples.
- The set of compact elements of an arithmetic complete lattice is a lattice with a least element, where the lattice operations are given by restricting the respective operations of the arithmetic lattice. This is the specific property that distinguishes arithmetic lattices from algebraic lattices, for which the compacts only form a join-semilattice. Both of these classes of complete lattices are studied in domain theory.

Further examples of lattices are given for each of the additional properties discussed below.

## Examples of non-lattices

|   |
|---|

|   |
|---|

|   |
|---|

Most partially ordered sets are not lattices, including the following.

- A discrete poset, meaning a poset such that $x\leq y$ implies $x=y,$ is a lattice if and only if it has at most one element. In particular the two-element discrete poset is not a lattice.
- Although the set $\{1,2,3,6\}$ partially ordered by divisibility is a lattice, the set $\{1,2,3\}$ so ordered is not a lattice because the pair 2, 3 lacks a join; similarly, 2, 3 lacks a meet in $\{2,3,6\}.$
- The set $\{1,2,3,12,18,36\}$ partially ordered by divisibility is not a lattice. Every pair of elements has an upper bound and a lower bound, but the pair 2, 3 has three upper bounds, namely 12, 18, and 36, none of which is the least of those three under divisibility (12 and 18 do not divide each other). Likewise the pair 12, 18 has three lower bounds, namely 1, 2, and 3, none of which is the greatest of those three under divisibility (2 and 3 do not divide each other).

## Morphisms of lattices

The appropriate notion of a morphism between two lattices flows easily from the above algebraic definition. Given two lattices $\left(L,\vee _{L},\wedge _{L}\right)$ and $\left(M,\vee _{M},\wedge _{M}\right),$ a **lattice homomorphism** from *L* to *M* is a function $f:L\to M$ such that for all $a,b\in L:$ $f\left(a\vee _{L}b\right)=f(a)\vee _{M}f(b),{\text{ and }}$ $f\left(a\wedge _{L}b\right)=f(a)\wedge _{M}f(b).$

Thus f is a homomorphism of the two underlying semilattices. When lattices with more structure are considered, the morphisms should "respect" the extra structure, too. In particular, a **bounded-lattice homomorphism** (usually called just "lattice homomorphism") f between two bounded lattices L and M should also have the following property: $f\left(0_{L}\right)=0_{M},{\text{ and }}$ $f\left(1_{L}\right)=1_{M}.$

In the order-theoretic formulation, these conditions just state that a homomorphism of lattices is a function preserving binary meets and joins. For bounded lattices, preservation of least and greatest elements is just preservation of join and meet of the empty set.

Any homomorphism of lattices is necessarily monotone with respect to the associated ordering relation; see Limit preserving function. The converse is not true: monotonicity by no means implies the required preservation of meets and joins (see Pic. 9), although an order-preserving bijection is a homomorphism if its inverse is also order-preserving.

Given the standard definition of isomorphisms as invertible morphisms, a **lattice isomorphism** is just a bijective lattice homomorphism. Similarly, a **lattice endomorphism** is a lattice homomorphism from a lattice to itself, and a **lattice automorphism** is a bijective lattice endomorphism. Lattices and their homomorphisms form a category.

Let $\mathbb {L}$ and $\mathbb {L} '$ be two lattices with **0** and **1**. A homomorphism from $\mathbb {L}$ to $\mathbb {L} '$ is called **0**,**1**-*separating* if and only if $f^{-1}\{f(0)\}=\{0\}$ ( f separates **0**) and $f^{-1}\{f(1)\}=\{1\}$ ( f separates 1).

## Sublattices

A **sublattice** of a lattice L is a subset of L that is a lattice with the same meet and join operations as $L.$ That is, if L is a lattice and M is a subset of L such that for every pair of elements $a,b\in M$ both $a\wedge b$ and $a\vee b$ are in $M,$ then M is a sublattice of $L.$

A sublattice M of a lattice L is a *convex sublattice* of $L,$ if $x\leq z\leq y$ and $x,y\in M$ implies that z belongs to $M,$ for all elements $x,y,z\in L.$

## Properties of lattices

We now introduce a number of important properties that lead to interesting special classes of lattices. One, boundedness, has already been discussed.

### Completeness

A poset is called a **complete lattice** if *all* its subsets have both a join and a meet. In particular, every complete lattice is a bounded lattice. While bounded lattice homomorphisms in general preserve only finite joins and meets, complete lattice homomorphisms are required to preserve arbitrary joins and meets.

Every poset that is a complete semilattice is also a complete lattice. Related to this result is the interesting phenomenon that there are various competing notions of homomorphism for this class of posets, depending on whether they are seen as complete lattices, complete join-semilattices, complete meet-semilattices, or as join-complete or meet-complete lattices.

"Partial lattice" is not the opposite of "complete lattice" – rather, "partial lattice", "lattice", and "complete lattice" are increasingly restrictive definitions.

### Conditional completeness

A **conditionally complete lattice** is a lattice in which every *nonempty* subset *that has an upper bound* has a join (that is, a least upper bound). Such lattices provide the most direct generalization of the completeness axiom of the real numbers. A conditionally complete lattice is either a complete lattice, or a complete lattice without its maximum element $1,$ its minimum element $0,$ or both.

### Distributivity

|   |
|---|

|   |
|---|

Since lattices come with two binary operations, it is natural to ask whether one of them distributes over the other, that is, whether one or the other of the following dual laws holds for every three elements $a,b,c\in L,$ :

**Distributivity of $\vee$ over $\wedge$**

$a\vee (b\wedge c)=(a\vee b)\wedge (a\vee c).$

**Distributivity of $\wedge$ over $\vee$**

$a\wedge (b\vee c)=(a\wedge b)\vee (a\wedge c).$

A lattice that satisfies the first or, equivalently (as it turns out), the second axiom, is called a **distributive lattice**. The only non-distributive lattices with fewer than 6 elements are called M3 and N5; they are shown in Pictures 10 and 11, respectively. A lattice is distributive if and only if it does not have a sublattice isomorphic to M3 or N5. Each distributive lattice is isomorphic to a lattice of sets (with union and intersection as join and meet, respectively).

For an overview of stronger notions of distributivity that are appropriate for complete lattices and that are used to define more special classes of lattices such as frames and completely distributive lattices, see distributivity in order theory.

### Modularity

For some applications the distributivity condition is too strong, and the following weaker property is often useful. A lattice $(L,\vee ,\wedge )$ is **modular** if, for all elements $a,b,c\in L,$ the following identity holds: $(a\wedge c)\vee (b\wedge c)=((a\wedge c)\vee b)\wedge c.$ (*Modular identity*) This condition is equivalent to the following axiom: $a\leq c$ implies $a\vee (b\wedge c)=(a\vee b)\wedge c.$ (*Modular law*) In fact, the inequality $a\vee (b\wedge c)\leq (a\vee b)\wedge c$ holds in any lattice when $a\leq c$ . A lattice is modular if and only if it does not have a sublattice isomorphic to N5 (shown in Pic. 11). Besides distributive lattices, examples of modular lattices are the lattice of submodules of a module (hence *modular*), the lattice of two-sided ideals of a ring, and the lattice of normal subgroups of a group. The set of first-order terms with the ordering "is more specific than" is a non-modular lattice used in automated reasoning.

### Semimodularity

A finite lattice is modular if and only if it is both upper and lower semimodular. For a lattice of finite length, the (upper) semimodularity is equivalent to the condition that the lattice is graded and its rank function r satisfies the following condition:

```
  
    
      
        r
        (
        x
        )
        +
        r
        (
        y
        )
        ≥
        r
        (
        x
        ∧
        y
        )
        +
        r
        (
        x
        ∨
        y
        )
        .
      
    
    {\displaystyle r(x)+r(y)\geq r(x\wedge y)+r(x\vee y).}
  
```

Another equivalent (for graded lattices) condition is Birkhoff's condition:

for each

x

and

y

in

$L,$

if

x

and

y

both cover

$x\wedge y,$

then

$x\vee y$

covers both

x

and

$y.$

A lattice is called lower semimodular if its dual is semimodular. For finite lattices this means that the previous conditions hold with $\vee$ and $\wedge$ exchanged, "covers" exchanged with "is covered by", and inequalities reversed.

### Continuity and algebraicity

In domain theory, it is natural to seek to approximate the elements in a partial order by "much simpler" elements. This leads to the class of continuous posets, consisting of posets where every element can be obtained as the supremum of a directed set of elements that are way-below the element. If one can additionally restrict these to the compact elements of a poset for obtaining these directed sets, then the poset is even algebraic. Both concepts can be applied to lattices as follows:

- A **continuous lattice** is a complete lattice that is continuous as a poset.
- An **algebraic lattice** is a complete lattice that is algebraic as a poset.

Both of these classes have interesting properties. For example, continuous lattices can be characterized as algebraic structures (with infinitary operations) satisfying certain identities. While such a characterization is not known for algebraic lattices, they can be described "syntactically" via Scott information systems.

### Complements and pseudo-complements

Let L be a bounded lattice with greatest element 1 and least element 0. Two elements x and y of L are **complements** of each other if and only if: $x\vee y=1\quad {\text{ and }}\quad x\wedge y=0.$

In general, some elements of a bounded lattice might not have a complement, and others might have more than one complement. For example, the set $\{0,1/2,1\}$ with its usual ordering is a bounded lattice, and ${\tfrac {1}{2}}$ does not have a complement. In the bounded lattice N5, the element a has two complements, viz. b and c (see Pic. 11). A bounded lattice for which every element has a complement is called a complemented lattice.

A complemented lattice that is also distributive is a Boolean algebra. For a distributive lattice, the complement of $x,$ when it exists, is unique.

In the case that the complement is unique, we write ${\textstyle \lnot x=y}$ and equivalently, ${\textstyle \lnot y=x.}$ The corresponding unary operation over $L,$ called complementation, introduces an analogue of logical negation into lattice theory.

Heyting algebras are an example of distributive lattices where some members might be lacking complements. Every element z of a Heyting algebra has, on the other hand, a pseudo-complement, also denoted ${\textstyle \lnot x.}$ The pseudo-complement is the greatest element y such that $x\wedge y=0.$ If the pseudo-complement of every element of a Heyting algebra is in fact a complement, then the Heyting algebra is in fact a Boolean algebra.

### Jordan–Dedekind chain condition

A **chain** from $x_{0}$ to $x_{n}$ is a set $\left\{x_{0},x_{1},\ldots ,x_{n}\right\},$ where $x_{0}<x_{1}<x_{2}<\ldots <x_{n}.$ The **length** of this chain is *n*, or one less than its number of elements. A chain is **maximal** if $x_{i}$ covers $x_{i-1}$ for all $1\leq i\leq n.$

If for any pair, x and $y,$ where $x<y,$ all maximal chains from x to y have the same length, then the lattice is said to satisfy the **Jordan–Dedekind chain condition**.

### Graded/ranked

A lattice $(L,\leq )$ is called **graded**, sometimes **ranked** (but see Ranked poset for an alternative meaning), if it can be equipped with a **rank function** $r:L\to \mathbb {N}$ sometimes to $\mathbb {Z}$ , compatible with the ordering (so $r(x)<r(y)$ whenever $x<y$ ) such that whenever y covers $x,$ then $r(y)=r(x)+1.$ The value of the rank function for a lattice element is called its **rank**.

A lattice element y is said to cover another element $x,$ if $y>x,$ but there does not exist a z such that $y>z>x.$ Here, $y>x$ means $x\leq y$ and $x\neq y.$

## Free lattices

Any set X may be used to generate the **free semilattice** $FX.$ The free semilattice is defined to consist of all of the finite subsets of $X,$ with the semilattice operation given by ordinary set union. The free semilattice has the universal property. For the **free lattice** over a set $X,$ Whitman gave a construction based on polynomials over X 's members.

## Flat lattices

Any (usually multielement) set X may also be used to define a **flat lattice**, the least lattice in which the set's elements are incomparable or, equivalently, the rank-3 lattice where X is exactly the set of elements of intermediate rank.

## Important lattice-theoretic notions

We now define some order-theoretic notions of importance to lattice theory. In the following, let x be an element of some lattice $L.$ x is called:

- **Join irreducible** if $x=a\vee b$ implies $x=a{\text{ or }}x=b.$ for all $a,b\in L.$ If L has a bottom element $0,$ some authors require $x\neq 0$ . When the first condition is generalized to arbitrary joins $\bigvee _{i\in I}a_{i},$ x is called **completely join irreducible** (or $\vee$ -irreducible). The dual notion is **meet irreducibility** ( $\wedge$ -irreducible). For example, in Pic. 2, the elements 2, 3, 4, and 5 are join irreducible, while 12, 15, 20, and 30 are meet irreducible. Depending on definition, the bottom element 1 and top element 60 may or may not be considered join irreducible and meet irreducible, respectively. In the lattice of real numbers with the usual order, each element is join irreducible, but none is completely join irreducible.
- **Join prime** if $x\leq a\vee b$ implies $x\leq a{\text{ or }}x\leq b.$ Again some authors require $x\neq 0$ , although this is unusual. This too can be generalized to obtain the notion **completely join prime**. The dual notion is **meet prime**. Every join-prime element is also join irreducible, and every meet-prime element is also meet irreducible. The converse holds if L is distributive.

Let L have a bottom element 0. An element x of L is an atom if $0<x$ and there exists no element $y\in L$ such that $0<y<x.$ Then L is called:

- Atomic if for every nonzero element x of $L,$ there exists an atom a of L such that $a\leq x;$
- Atomistic if every element of L is a supremum of atoms.

However, many sources and mathematical communities use the term "atomic" to mean "atomistic" as defined above.

The notions of ideals and the dual notion of filters refer to particular kinds of subsets of a partially ordered set, and are therefore important for lattice theory. Details can be found in the respective entries.

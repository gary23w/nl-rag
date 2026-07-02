---
title: "Partially ordered set"
source: https://en.wikipedia.org/wiki/Partially_ordered_set
domain: cpo-theory
license: CC-BY-SA-4.0
tags: complete partial order, directed-complete partial order, chain-complete poset, least upper bound
fetched: 2026-07-02
---

# Partially ordered set

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, especially order theory, a **partial order** on a set is an arrangement such that, for certain pairs of elements, one precedes the other. The word *partial* is used to indicate that not every pair of elements needs to be comparable; that is, there may be pairs for which neither element precedes the other. Partial orders thus generalize total orders, in which every pair is comparable.

Formally, a partial order is a homogeneous binary relation that is reflexive, antisymmetric, and transitive. A **partially ordered set** (**poset** for short) is an ordered pair $P=(X,\leq )$ consisting of a set X (called the *ground set* of P ) and a partial order $\leq$ on X . When the meaning is clear from context and there is no ambiguity about the partial order, the set X itself is sometimes called a poset.

## Partial order relations

The term *partial order* usually refers to the reflexive partial order relations, referred to in this article as *non-strict* partial orders. However some authors use the term for the other common type of partial order relations, the irreflexive partial order relations, also called strict partial orders. Strict and non-strict partial orders can be put into a one-to-one correspondence, so for every strict partial order there is a unique corresponding non-strict partial order, and vice versa.

### Partial orders

A **reflexive**, **weak**, or **non-strict partial order**, commonly referred to simply as a **partial order**, is a homogeneous relation ≤ on a set P that is reflexive, antisymmetric, and transitive. That is, for all $a,b,c\in P,$ it must satisfy:

1. Reflexivity: $a\leq a$ , i.e. every element is related to itself.
2. Antisymmetry: if $a\leq b$ and $b\leq a$ then $a=b$ , i.e. no two distinct elements precede each other.
3. Transitivity: if $a\leq b$ and $b\leq c$ then $a\leq c$ .

A non-strict partial order is also known as an antisymmetric preorder.

### Strict partial orders

An **irreflexive**, **strong**, or **strict partial order** is a homogeneous relation < on a set P that is irreflexive, asymmetric and transitive; that is, it satisfies the following conditions for all $a,b,c\in P:$

1. Irreflexivity: $\neg \left(a<a\right)$ , i.e. no element is related to itself (also called anti-reflexive).
2. Asymmetry: if $a<b$ then not $b<a$ .
3. Transitivity: if $a<b$ and $b<c$ then $a<c$ .

A transitive relation is asymmetric if and only if it is irreflexive. So the definition is the same if it omits either irreflexivity or asymmetry (but not both).

A strict partial order is also known as a strict preorder.

### Correspondence of strict and non-strict partial order relations

Strict and non-strict partial orders on a set P are closely related. A non-strict partial order $\leq$ may be converted to a strict partial order by removing all relationships of the form $a\leq a;$ that is, the strict partial order is the set $<\;:=\ \leq \ \setminus \ \Delta _{P}$ where $\Delta _{P}:=\{(p,p):p\in P\}$ is the identity relation on $P\times P$ and $\;\setminus \;$ denotes set subtraction. Conversely, a strict partial order < on P may be converted to a non-strict partial order by adjoining all relationships of that form; that is, $\leq \;:=\;\Delta _{P}\;\cup \;<\;$ is a non-strict partial order. Thus, if $\leq$ is a non-strict partial order, then the corresponding strict partial order < is the irreflexive kernel given by $a<b{\text{ if }}a\leq b{\text{ and }}a\neq b.$ Conversely, if < is a strict partial order, then the corresponding non-strict partial order $\leq$ is the reflexive closure given by: $a\leq b{\text{ if }}a<b{\text{ or }}a=b.$

### Dual orders

The *dual* (or *opposite*) $R^{\text{op}}$ of a partial order relation R is defined by letting $R^{\text{op}}$ be the converse relation of R , i.e. $xR^{\text{op}}y$ if and only if $yRx$ . The dual of a non-strict partial order is a non-strict partial order, and the dual of a strict partial order is a strict partial order. The dual of a dual of a relation is the original relation.

## Notation

Given a set P and a partial order relation, typically the non-strict partial order $\leq$ , we may uniquely extend our notation to define four partial order relations $\leq ,$ $<,$ $\geq ,$ and > , where $\leq$ is a non-strict partial order relation on P , < is the associated strict partial order relation on P (the irreflexive kernel of $\leq$ ), $\geq$ is the dual of $\leq$ , and > is the dual of < . Strictly speaking, the term *partially ordered set* refers to a set with all of these relations defined appropriately. But practically, one need only consider a single relation, $(P,\leq )$ or $(P,<)$ , or, in rare instances, the non-strict and strict relations together, $(P,\leq ,<)$ .

The term *ordered set* is sometimes used as a shorthand for *partially ordered set*, as long as it is clear from the context that no other kind of order is meant. In particular, totally ordered sets can also be referred to as "ordered sets", especially in areas where these structures are more common than posets. Some authors use different symbols than $\leq$ such as $\sqsubseteq$ or $\preceq$ to distinguish partial orders from total orders.

When referring to partial orders, $\leq$ should not be taken as the complement of > . The relation > is the converse of the irreflexive kernel of $\leq$ , which is always a subset of the complement of $\leq$ , but > is equal to the complement of $\leq$ if, and only if, $\leq$ is a total order.

## Alternative definitions

Another way of defining a partial order, found in computer science, is via a notion of comparison. Specifically, given $\leq ,<,\geq ,{\text{ and }}>$ as defined previously, it can be observed that two elements *x* and *y* may stand in any of four mutually exclusive relationships to each other: either *x* < *y*, or *x* = *y*, or *x* > *y*, or *x* and *y* are *incomparable*. This can be represented by a function ${\text{compare}}:P\times P\to \{<,>,=,\vert \}$ that returns one of four codes when given two elements. This definition is equivalent to a *partial order on a setoid*, where equality is taken to be a defined equivalence relation rather than set equality.

Wallis defines a more general notion of a *partial order relation* as any homogeneous relation that is transitive and antisymmetric. This includes both reflexive and irreflexive partial orders as subtypes.

A finite poset can be visualized through its Hasse diagram. Specifically, taking a strict partial order relation $(P,<)$ , a directed acyclic graph (DAG) may be constructed by taking each element of P to be a node and each element of < to be an edge. The transitive reduction of this DAG is then the Hasse diagram. Similarly this process can be reversed to construct strict partial orders from certain DAGs. In contrast, the graph associated to a non-strict partial order has self-loops at every node and therefore is not a DAG; when a non-strict order is said to be depicted by a Hasse diagram, actually the corresponding strict order is shown.

## Examples

Standard examples of posets arising in mathematics include:

- The real numbers, or in general any totally ordered set, ordered by the standard *less-than-or-equal* relation ≤, is a partial order.
- On the real numbers $\mathbb {R}$ , the usual less than relation < is a strict partial order. The same is also true of the usual greater than relation > on $\mathbb {R}$ .
- By definition, every strict weak order is a strict partial order.
- The set of subsets of a given set (its power set) ordered by inclusion (see Fig. 1). Similarly, the set of sequences ordered by subsequence, and the set of strings ordered by substring.
- The set of natural numbers equipped with the relation of divisibility. (see Fig. 3 and Fig. 6)
- The vertex set of a directed acyclic graph ordered by reachability.
- The set of subspaces of a vector space ordered by inclusion.
- For a partially ordered set *P*, the sequence space containing all sequences of elements from *P*, where sequence *a* precedes sequence *b* if every item in *a* precedes the corresponding item in *b*. Formally, $\left(a_{n}\right)_{n\in \mathbb {N} }\leq \left(b_{n}\right)_{n\in \mathbb {N} }$ if and only if $a_{n}\leq b_{n}$ for all $n\in \mathbb {N}$ ; that is, a componentwise order.
- For a set *X* and a partially ordered set *P*, the function space containing all functions from *X* to *P*, where *f* ≤ *g* if and only if *f*(*x*) ≤ *g*(*x*) for all $x\in X.$
- A fence, a partially ordered set defined by an alternating sequence of order relations *a* < *b* > *c* < *d* ...
- The set of events in special relativity and, in most cases, general relativity, where for two events *X* and *Y*, *X* ≤ *Y* if and only if *Y* is in the future light cone of *X*. An event *Y* can be causally affected by *X* only if *X* ≤ *Y*.

One familiar example of a partially ordered set is a collection of people ordered by genealogical descendancy. Some pairs of people bear the descendant-ancestor relationship, but other pairs of people are incomparable, with neither being a descendant of the other.

### Orders on the Cartesian product of partially ordered sets

Fig. 4a

Lexicographic order on

$\mathbb {N} \times \mathbb {N}$

Fig. 4b

Product order on

$\mathbb {N} \times \mathbb {N}$

Fig. 4c

Reflexive closure of strict direct product order on

$\mathbb {N} \times \mathbb {N} .$

Elements

covered

by

(3, 3)

and covering

(3, 3)

are highlighted in green and red, respectively.

In order of increasing strength, i.e., decreasing sets of pairs, three of the possible partial orders on the Cartesian product of two partially ordered sets are (see Fig. 4):

- the lexicographical order:   (*a*, *b*) ≤ (*c*, *d*) if *a* < *c* or (*a* = *c* and *b* ≤ *d*);
- the product order:   (*a*, *b*) ≤ (*c*, *d*) if *a* ≤ *c* and *b* ≤ *d*;
- the reflexive closure of the direct product of the corresponding strict orders:   (*a*, *b*) ≤ (*c*, *d*) if (*a* < *c* and *b* < *d*) or (*a* = *c* and *b* = *d*).

All three can similarly be defined for the Cartesian product of more than two sets.

Applied to ordered vector spaces over the same field, the result is in each case also an ordered vector space.

See also orders on the Cartesian product of totally ordered sets.

### Sums of partially ordered sets

Another way to combine two (disjoint) posets is the **ordinal sum** (or **linear sum**), *Z* = *X* ⊕ *Y*, defined on the union of the underlying sets *X* and *Y* by the order *a* ≤*Z* *b* if and only if:

- *a*, *b* ∈ *X* with *a* ≤*X* *b*, or
- *a*, *b* ∈ *Y* with *a* ≤*Y* *b*, or
- *a* ∈ *X* and *b* ∈ *Y*.

If two posets are well-ordered, then so is their ordinal sum.

Series-parallel partial orders are formed from the ordinal sum operation (in this context called series composition) and another operation called parallel composition. Parallel composition is the disjoint union of two partially ordered sets, with no order relation between elements of one set and elements of the other set.

## Derived notions

The examples use the poset $({\mathcal {P}}(\{x,y,z\}),\subseteq )$ consisting of the set of all subsets of a three-element set $\{x,y,z\},$ ordered by set inclusion (see Fig. 1).

- *a* is *related to* *b* when *a* ≤ *b*. This does not imply that *b* is also related to *a*, because the relation need not be symmetric. For example, $\{x\}$ is related to $\{x,y\},$ but not the reverse.
- *a* and *b* are *comparable* if *a* ≤ *b* or *b* ≤ *a*. Otherwise they are *incomparable*. For example, $\{x\}$ and $\{x,y,z\}$ are comparable, while $\{x\}$ and $\{y\}$ are not.
- A *total order* or *linear order* is a partial order under which every pair of elements is comparable, i.e. trichotomy holds. For example, the natural numbers with their standard order.
- A *chain* is a subset of a poset that is a totally ordered set. For example, $\{\{\,\},\{x\},\{x,y,z\}\}$ is a chain.
- An *antichain* is a subset of a poset in which no two distinct elements are comparable. For example, the set of singletons $\{\{x\},\{y\},\{z\}\}.$
- An element *a* is said to be *strictly less than* an element *b*, if *a* ≤ *b* and $a\neq b.$ For example, $\{x\}$ is strictly less than $\{x,y\}.$
- An element *a* is said to be *covered* by another element *b*, written *a* ⋖ *b* (or *a* <: *b*), if *a* is strictly less than *b* and no third element *c* fits between them; formally: if both *a* ≤ *b* and $a\neq b$ are true, and *a* ≤ *c* ≤ *b* is false for each *c* with $a\neq c\neq b.$ Using the strict order <, the relation *a* ⋖ *b* can be equivalently rephrased as "*a* < *b* but not *a* < *c* < *b* for any *c*". For example, $\{x\}$ is covered by $\{x,z\},$ but is not covered by $\{x,y,z\}.$

### Extrema

There are several notions of "greatest" and "least" element in a poset $P,$ notably:

- Greatest element and least element: An element $g\in P$ is a *greatest element* if $a\leq g$ for every element $a\in P.$ An element $m\in P$ is a *least element* if $m\leq a$ for every element $a\in P.$ A poset can only have one greatest or least element. In our running example, the set $\{x,y,z\}$ is the greatest element, and $\{\,\}$ is the least.
- Maximal elements and minimal elements: An element $g\in P$ is a maximal element if there is no element $a\in P$ such that $a>g.$ Similarly, an element $m\in P$ is a minimal element if there is no element $a\in P$ such that $a<m.$ If a poset has a greatest element, it must be the unique maximal element, but otherwise there can be more than one maximal element, and similarly for least elements and minimal elements. In our running example, $\{x,y,z\}$ and $\{\,\}$ are the maximal and minimal elements. Removing these, there are 3 maximal elements and 3 minimal elements (see Fig. 5).
- Upper and lower bounds: For a subset *A* of *P*, an element *x* in *P* is an upper bound of *A* if *a* ≤ *x*, for each element *a* in *A*. In particular, *x* need not be in *A* to be an upper bound of *A*. Similarly, an element *x* in *P* is a lower bound of *A* if *a* ≥ *x*, for each element *a* in *A*. A greatest element of *P* is an upper bound of *P* itself, and a least element is a lower bound of *P*. In our example, the set $\{x,y\}$ is an *upper bound* for the collection of elements $\{\{x\},\{y\}\}.$

As another example, consider the positive integers, ordered by divisibility: 1 is a least element, as it divides all other elements; on the other hand this poset does not have a greatest element. This partially ordered set does not even have any maximal elements, since any *g* divides for instance 2*g*, which is distinct from it, so *g* is not maximal. If the number 1 is excluded, while keeping divisibility as ordering on the elements greater than 1, then the resulting poset does not have a least element, but any prime number is a minimal element for it. In this poset, 60 is an upper bound (though not a least upper bound) of the subset $\{2,3,5,10\},$ which does not have any lower bound (since 1 is not in the poset); on the other hand 2 is a lower bound of the subset of powers of 2, which does not have any upper bound. If the number 0 is included, this will be the greatest element, since this is a multiple of every integer (see Fig. 6).

## Mappings between partially ordered sets

Fig. 7a

Order-preserving, but not order-reflecting map (since

f

(

u

) ≼

f

(

v

)

, but not u

$\leq$

v)

Fig. 7b

Order isomorphism between the divisors of 120 (partially ordered by divisibility) and the divisor-closed subsets of

{2, 3, 4, 5, 8}

(partially ordered by set inclusion)

Given two partially ordered sets (*S*, ≤) and (*T*, ≼), a function $f:S\to T$ is called **order-preserving**, or **monotone**, or **isotone**, if for all $x,y\in S,$ $x\leq y$ implies *f*(*x*) ≼ *f*(*y*). If (*U*, ≲) is also a partially ordered set, and both $f:S\to T$ and $g:T\to U$ are order-preserving, their composition $g\circ f:S\to U$ is order-preserving, too. A function $f:S\to T$ is called **order-reflecting** if for all $x,y\in S,$ *f*(*x*) ≼ *f*(*y*) implies $x\leq y.$ If f is both order-preserving and order-reflecting, then it is called an **order-embedding** of (*S*, ≤) into (*T*, ≼). In the latter case, f is necessarily injective, since $f(x)=f(y)$ implies $x\leq y{\text{ and }}y\leq x$ and in turn $x=y$ according to the antisymmetry of $\leq .$ If an order-embedding between two posets *S* and *T* exists, one says that *S* can be **embedded** into *T*. If an order-embedding $f:S\to T$ is bijective, it is called an **order isomorphism**, and the partial orders (*S*, ≤) and (*T*, ≼) are said to be **isomorphic**. Isomorphic orders have structurally similar Hasse diagrams (see Fig. 7a). It can be shown that if order-preserving maps $f:S\to T$ and $g:T\to U$ exist such that $g\circ f$ and $f\circ g$ yields the identity function on *S* and *T*, respectively, then *S* and *T* are order-isomorphic.

For example, a mapping $f:\mathbb {N} \to \mathbb {P} (\mathbb {N} )$ from the set of natural numbers (ordered by divisibility) to the power set of natural numbers (ordered by set inclusion) can be defined by taking each number to the set of its prime divisors. It is order-preserving: if x divides y, then each prime divisor of x is also a prime divisor of y. However, it is neither injective (since it maps both 12 and 6 to $\{2,3\}$ ) nor order-reflecting (since 12 does not divide 6). Taking instead each number to the set of its prime power divisors defines a map $g:\mathbb {N} \to \mathbb {P} (\mathbb {N} )$ that is order-preserving, order-reflecting, and hence an order-embedding. It is not an order-isomorphism (since it, for instance, does not map any number to the set $\{4\}$ ), but it can be made one by restricting its codomain to $g(\mathbb {N} ).$ Fig. 7b shows a subset of $\mathbb {N}$ and its isomorphic image under g. The construction of such an order-isomorphism into a power set can be generalized to a wide class of partial orders, called distributive lattices; see *Birkhoff's representation theorem*.

## Number of partial orders

Sequence A001035 in OEIS gives the number of partial orders on a set of *n* labeled elements:

Number of

n

-element binary relations of different types

Elem­ents

Any

Transitive

Reflexive

Symmetric

Preorder

Partial order

Total preorder

Total order

Equivalence relation

0

1

1

1

1

1

1

1

1

1

1

2

2

1

2

1

1

1

1

1

2

16

13

4

8

4

3

3

2

2

3

512

171

64

64

29

19

13

6

5

4

65,536

3,994

4,096

1,024

355

219

75

24

15

n

2

n

2

2

n

(

n

−1)

2

n

(

n

+1)/2

∑

n

k

=0

k

!

S

(

n

,

k

)

n

!

∑

n

k

=0

S

(

n

,

k

)

OEIS

A002416

A006905

A053763

A006125

A000798

A001035

A000670

A000142

A000110

Note that *S*(*n*, *k*) refers to Stirling numbers of the second kind.

The number of strict partial orders is the same as that of partial orders.

If the count is made only up to isomorphism, the sequence 1, 1, 2, 5, 16, 63, 318, ... (sequence A000112 in the OEIS) is obtained.

## Subposets

A poset $P^{*}=(X^{*},\leq ^{*})$ is called a **subposet** of another poset $P=(X,\leq )$ provided that $X^{*}$ is a subset of X and $\leq ^{*}$ is a subset of $\leq$ . The latter condition is equivalent to the requirement that for any x and y in $X^{*}$ (and thus also in X ), if $x\leq ^{*}y$ then $x\leq y$ .

If $P^{*}$ is a subposet of P and furthermore, for all x and y in $X^{*}$ , whenever $x\leq y$ we also have $x\leq ^{*}y$ , then we call $P^{*}$ the subposet of P **induced** by $X^{*}$ , and write $P^{*}=P[X^{*}]$ .

## Linear extension

A partial order $\leq ^{*}$ on a set X is called an **extension** of another partial order $\leq$ on X provided that for all elements $x,y\in X,$ whenever $x\leq y,$ it is also the case that $x\leq ^{*}y.$ A linear extension is an extension that is also a linear (that is, total) order. As a classic example, the lexicographic order of totally ordered sets is a linear extension of their product order. Every partial order can be extended to a total order (order-extension principle).

In computer science, algorithms for finding linear extensions of partial orders (represented as the reachability orders of directed acyclic graphs) are called topological sorting.

## In category theory

Every poset (and every preordered set) may be considered as a category where, for objects x and $y,$ there is at most one morphism from x to $y.$ More explicitly, let hom(*x*, *y*) = {(*x*, *y*)} if *x* ≤ *y* (and otherwise the empty set) and $(y,z)\circ (x,y)=(x,z).$ Such categories are sometimes called *thin*.

Posets are equivalent to one another if and only if they are isomorphic. In a poset, the smallest element, if it exists, is an initial object, and the largest element, if it exists, is a terminal object. Also, every preordered set is equivalent to a poset. Finally, every subcategory of a poset is isomorphism-closed.

## Partial orders in topological spaces

If P is a partially ordered set that has also been given the structure of a topological space, then it is customary to assume that $\{(a,b):a\leq b\}$ is a closed subset of the topological product space $P\times P.$ Under this assumption partial order relations are well behaved at limits in the sense that if $\lim _{i\to \infty }a_{i}=a,$ and $\lim _{i\to \infty }b_{i}=b,$ and for all $i,$ $a_{i}\leq b_{i},$ then $a\leq b.$

## Intervals

A **convex set** in a poset *P* is a subset I of *P* with the property that, for any *x* and *y* in I and any *z* in *P*, if *x* ≤ *z* ≤ *y*, then *z* is also in I. This definition generalizes the definition of intervals of real numbers. When there is possible confusion with convex sets of geometry, one uses **order-convex** instead of "convex".

A **convex sublattice** of a lattice *L* is a sublattice of *L* that is also a convex set of *L*. Every nonempty convex sublattice can be uniquely represented as the intersection of a filter and an ideal of *L*.

An **interval** in a poset *P* is a subset that can be defined with interval notation:

- For *a* ≤ *b*, the *closed interval* [*a*, *b*] is the set of elements *x* satisfying *a* ≤ *x* ≤ *b* (that is, *a* ≤ *x* and *x* ≤ *b*). It contains at least the elements *a* and *b*.
- Using the corresponding strict relation "<", the *open interval* (*a*, *b*) is the set of elements *x* satisfying *a* < *x* < *b* (i.e. *a* < *x* and *x* < *b*). An open interval may be empty even if *a* < *b*. For example, the open interval (0, 1) on the integers is empty since there is no integer x such that 0 < *x* < 1.
- The *half-open intervals* [*a*, *b*) and (*a*, *b*] are defined similarly.

Whenever *a* ≤ *b* does not hold, all these intervals are empty. Every interval is a convex set, but the converse does not hold; for example, in the poset of divisors of 120, ordered by divisibility (see Fig. 7b), the set {1, 2, 4, 5, 8} is convex, but not an interval.

An interval I is bounded if there exist elements $a,b\in P$ such that *I* ⊆ [*a*, *b*]. Every interval that can be represented in interval notation is obviously bounded, but the converse is not true. For example, let *P* = (0, 1) ∪ (1, 2) ∪ (2, 3) as a subposet of the real numbers. The subset (1, 2) is a bounded interval, but it has no infimum or supremum in *P*, so it cannot be written in interval notation using elements of *P*.

A poset is called locally finite if every bounded interval is finite. For example, the integers are locally finite under their natural ordering. The lexicographical order on the cartesian product $\mathbb {N} \times \mathbb {N}$ is not locally finite, since (1, 2) ≤ (1, 3) ≤ (1, 4) ≤ (1, 5) ≤ ... ≤ (2, 1). Using the interval notation, the property "*a* is covered by *b*" can be rephrased equivalently as $[a,b]=\{a,b\}.$

This concept of an interval in a partial order should not be confused with the particular class of partial orders known as the interval orders.

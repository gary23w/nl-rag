---
title: "Abelian group"
source: https://en.wikipedia.org/wiki/Abelian_group
domain: time-translation-symmetry
license: CC-BY-SA-4.0
tags: time-translation symmetry
fetched: 2026-07-04
---

# Abelian group

In mathematics, an **abelian group**,[note 1] also called a **commutative group**, is a group in which the result of applying the group operation to two group elements does not depend on the order in which they are written. That is, the group operation is commutative. With addition as an operation, the integers and the real numbers form abelian groups, and the concept of an abelian group may be viewed as a generalization of these examples. Abelian groups are named after the Norwegian mathematician Niels Henrik Abel.

The concept of an abelian group underlies many fundamental algebraic structures, such as fields, rings, vector spaces, and algebras. The theory of abelian groups is generally simpler than that of their non-abelian counterparts, and finite abelian groups are very well understood and fully classified.

## Definition

An abelian group is a set A , together with an operation ･ , that combines any two elements a and b of A to form another element of $A,$ denoted $a\cdot b$ . The symbol ･ is a general placeholder for a concretely given operation. To qualify as an abelian group, the set and operation, $(A,\cdot )$ , must satisfy four requirements known as the *abelian group axioms*:

**Associativity**

For all

a

,

b

, and

c

in

A

, the equation

$(a\cdot b)\cdot c=a\cdot (b\cdot c)$

holds.

**Identity element**

There exists an element

e

in

A

, such that for all elements

a

in

A

, the equation

$e\cdot a=a\cdot e=a$

holds.

**Inverse element**

For each

a

in

A

there exists an element

b

in

A

such that

$a\cdot b=b\cdot a=e$

, where

e

is the identity element.

**Commutativity**

For all

a

,

b

in

A

,

$a\cdot b=b\cdot a$

.

Some authors further include as requirements some properties that belong to the definition of an operation: that the operation is *defined* for any ordered pair of elements of A, that the result is *well-defined*, and that the result *belongs to* A.

A group in which the group operation is not commutative is called a *non-abelian group* or *non-commutative group*.

## Facts

### Notation

There are two main notational conventions for abelian groups – additive and multiplicative.

| Convention | Operation | Identity | Powers | Inverse |
|---|---|---|---|---|
| Addition | $x+y$ | 0 | $nx$ | $-x$ |
| Multiplication | $x\cdot y$ or $xy$ | 1 | $x^{n}$ | $x^{-1}$ |

Generally, the multiplicative notation is the usual notation for groups, while the additive notation is the usual notation for modules and rings. The additive notation may also be used to emphasize that a particular group is abelian, whenever both abelian and non-abelian groups are considered, with some notable exceptions being near-rings and partially ordered groups, where an operation is written additively even when non-abelian.

### Multiplication table

To verify that a finite group is abelian, a table (matrix) – known as a Cayley table – can be constructed in a similar fashion to a multiplication table. If the group is $G=\{g_{1}=e,g_{2},\dots ,g_{n}\}$ under the operation $\cdot$ , the $(i,j)$ -th entry of this table contains the product $g_{i}\cdot g_{j}$ .

The group is abelian if and only if this table is symmetric about the main diagonal, which means that for all $i,j=1,...,n$ , the $(i,j)$ entry of the table equals the $(j,i)$ entry. Indeed, this equality expresses that $g_{i}\cdot g_{j}=g_{j}\cdot g_{i}.$

## Examples

- The group consisting of only the identity element is abelian.
- For the integers and the operation addition + , denoted $(\mathbb {Z} ,+)$ , the operation + combines any two integers to form a third integer, addition is associative, zero is the additive identity, every integer n has an additive inverse, $-n$ , and the addition operation is commutative since $n+m=m+n$ for any two integers m and n .
- Every cyclic group G is abelian, because if x , y are in G , then $xy=a^{m}a^{n}=a^{m+n}=a^{n}a^{m}=yx$ . Thus the integers, $\mathbb {Z}$ , form an abelian group under addition, as do the integers modulo n , $\mathbb {Z} /n\mathbb {Z}$ .
- Every ring is an abelian group with respect to its addition operation. In a commutative ring the invertible elements, or units, form an abelian multiplicative group. In particular, the real numbers are an abelian group under addition, and the nonzero real numbers are an abelian group under multiplication.
- Every subgroup of an abelian group is normal, so each subgroup gives rise to a quotient group. Subgroups, quotients, and direct sums of abelian groups are again abelian. The finite simple abelian groups are exactly the cyclic groups of prime order.
- The concepts of abelian group and $\mathbb {Z}$ -module agree. More specifically, every $\mathbb {Z}$ -module is an abelian group with its operation of addition, and every abelian group is a module over the ring of integers $\mathbb {Z}$ in a unique way.

In general, matrices, even invertible matrices, do not form an abelian group under multiplication because matrix multiplication is generally not commutative. However, some groups of matrices are abelian groups under matrix multiplication – one example is the group of $2\times 2$ rotation matrices.

## Historical remarks

Camille Jordan named abelian groups after the Norwegian mathematician Niels Henrik Abel, who had found that the commutativity of the group of a polynomial implies that the roots of the polynomial can be calculated by using radicals.

## Properties

If n is a natural number and x is an element of an abelian group G written additively, then $nx$ can be defined as $x+x+\cdots +x$ ( n summands) and $(-n)x=-(nx)$ . In this way, G becomes a module over the ring $\mathbb {Z}$ of integers. In fact, the modules over $\mathbb {Z}$ can be identified with the abelian groups.

Theorems about abelian groups (i.e. modules over the principal ideal domain $\mathbb {Z}$ ) can often be generalized to theorems about modules over an arbitrary principal ideal domain. A typical example is the classification of finitely generated abelian groups which is a specialization of the structure theorem for finitely generated modules over a principal ideal domain. In the case of finitely generated abelian groups, this theorem guarantees that an abelian group splits as a direct sum of a torsion group and a free abelian group. The former may be written as a direct sum of finitely many groups of the form $\mathbb {Z} /p^{k}\mathbb {Z}$ for p prime, and the latter is a direct sum of finitely many copies of $\mathbb {Z}$ .

If $f,g:G\to H$ are two group homomorphisms between abelian groups, then their sum $f+g$ , defined by $(f+g)(x)=f(x)+g(x)$ , is again a homomorphism. (This is not true if H is a non-abelian group.) The set ${\text{Hom}}(G,H)$ of all group homomorphisms from G to H is therefore an abelian group in its own right.

Somewhat akin to the dimension of vector spaces, every abelian group has a *rank*. It is defined as the maximal cardinality of a set of linearly independent (over the integers) elements of the group. Finite abelian groups and torsion groups have rank zero, and every abelian group of rank zero is a torsion group. The integers and the rational numbers have rank one, as well as every nonzero additive subgroup of the rationals. On the other hand, the multiplicative group of the nonzero rationals has an infinite rank, as it is a free abelian group with the set of the prime numbers as a basis (this results from the fundamental theorem of arithmetic).

The center $Z(G)$ of a group G is the set of elements that commute with every element of G . A group G is abelian if and only if it is equal to its center $Z(G)$ . The center of a group G is always a characteristic abelian subgroup of G . If the quotient group $G/Z(G)$ of a group by its center is cyclic then G is abelian.

## Finite abelian groups

Cyclic groups of integers modulo n , $\mathbb {Z} /n\mathbb {Z}$ , were among the first examples of groups. It turns out that an arbitrary finite abelian group is isomorphic to a direct sum of finite cyclic groups of prime power order, and these orders are uniquely determined, forming a complete system of invariants. The automorphism group of a finite abelian group can be described directly in terms of these invariants. The theory had been first developed in the 1879 paper of Georg Frobenius and Ludwig Stickelberger and later was both simplified and generalized to finitely generated modules over a principal ideal domain, forming an important chapter of linear algebra.

Any group of prime order is isomorphic to a cyclic group and therefore abelian. Any group whose order is a square of a prime number is also abelian. In fact, for every prime number p there are (up to isomorphism) exactly two groups of order $p^{2}$ , namely $\mathbb {Z} _{p^{2}}$ and $\mathbb {Z} _{p}\times \mathbb {Z} _{p}$ .

### Classification

The **fundamental theorem of finite abelian groups** states that every finite abelian group G can be expressed as the direct sum of cyclic subgroups of prime-power order; it is also known as the **basis theorem for finite abelian groups**. Moreover, automorphism groups of cyclic groups are examples of abelian groups. This is generalized by the fundamental theorem of finitely generated abelian groups, with finite groups being the special case when *G* has zero rank; this in turn admits numerous further generalizations.

The classification was proven by Leopold Kronecker in 1870, though it was not stated in modern group-theoretic terms until later, and was preceded by a similar classification of quadratic forms by Carl Friedrich Gauss in 1801; see history for details.

The cyclic group $\mathbb {Z} _{mn}$ of order $mn$ is isomorphic to the direct sum of $\mathbb {Z} _{m}$ and $\mathbb {Z} _{n}$ if and only if m and n are coprime. It follows that any finite abelian group G is isomorphic to a direct sum of the form

$\bigoplus _{i=1}^{u}\ \mathbb {Z} _{k_{i}}$

in either of the following canonical ways:

- the numbers $k_{1},k_{2},\dots ,k_{u}$ are powers of (not necessarily distinct) primes,
- or $k_{1}$ divides $k_{2}$ , which divides $k_{3}$ , and so on up to $k_{u}$ .

For example, $\mathbb {Z} _{15}$ can be expressed as the direct sum of two cyclic subgroups of order 3 and 5: $\mathbb {Z} _{15}\cong \{0,5,10\}\oplus \{0,3,6,9,12\}$ . The same can be said for any abelian group of order 15, leading to the remarkable conclusion that all abelian groups of order 15 are isomorphic.

For another example, every abelian group of order 8 is isomorphic to either $\mathbb {Z} _{8}$ (the integers 0 to 7 under addition modulo 8), $\mathbb {Z} _{4}\oplus \mathbb {Z} _{2}$ (the odd integers 1 to 15 under multiplication modulo 16), or $\mathbb {Z} _{2}\oplus \mathbb {Z} _{2}\oplus \mathbb {Z} _{2}$ .

See also list of small groups for finite abelian groups of order 30 or less.

### Automorphisms

One can apply the fundamental theorem to count (and sometimes determine) the automorphisms of a given finite abelian group G . To do this, one uses the fact that if G splits as a direct sum $H\oplus K$ of subgroups of coprime order, then

$\operatorname {Aut} (H\oplus K)\cong \operatorname {Aut} (H)\oplus \operatorname {Aut} (K).$

Given this, the fundamental theorem shows that to compute the automorphism group of G it suffices to compute the automorphism groups of the Sylow p -subgroups separately (that is, all direct sums of cyclic subgroups, each with order a power of p ). Fix a prime p and suppose the exponents $e_{i}$ of the cyclic factors of the Sylow p -subgroup are arranged in increasing order:

$e_{1}\leq e_{2}\leq \cdots \leq e_{n}$

for some $n>0$ . One needs to find the automorphisms of

$\mathbb {Z} _{p^{e_{1}}}\oplus \cdots \oplus \mathbb {Z} _{p^{e_{n}}}.$

One special case is when $n=1$ , so that there is only one cyclic prime-power factor in the Sylow p -subgroup P . In this case the theory of automorphisms of a finite cyclic group can be used. Another special case is when n is arbitrary but $e_{i}=1$ for $1\leq i\leq n$ . Here, one is considering P to be of the form

$\mathbb {Z} _{p}\oplus \cdots \oplus \mathbb {Z} _{p},$

so elements of this subgroup can be viewed as comprising a vector space of dimension n over the finite field of p elements $\mathbb {F} _{p}$ . The automorphisms of this subgroup are therefore given by the invertible linear transformations, so

$\operatorname {Aut} (P)\cong \mathrm {GL} (n,\mathbb {F} _{p}),$

where $\mathrm {GL}$ is the appropriate general linear group. This is easily shown to have order

$\left|\operatorname {Aut} (P)\right|=(p^{n}-1)\cdots (p^{n}-p^{n-1}).$

In the most general case, where the $e_{i}$ and n are arbitrary, the automorphism group is more difficult to determine. It is known, however, that if one defines

$d_{k}=\max\{r\mid e_{r}=e_{k}\}$

and

$c_{k}=\min\{r\mid e_{r}=e_{k}\}$

then one has in particular $k\leq d_{k}$ , $c_{k}\leq k$ , and

$\left|\operatorname {Aut} (P)\right|=\prod _{k=1}^{n}(p^{d_{k}}-p^{k-1})\prod _{j=1}^{n}(p^{e_{j}})^{n-d_{j}}\prod _{i=1}^{n}(p^{e_{i}-1})^{n-c_{i}+1}.$

One can check that this yields the orders in the previous examples as special cases (see Hillar & Rhea).

## Finitely generated abelian groups

An abelian group A is finitely generated if it contains a finite set of elements (called *generators*) $G=\{x_{1},\ldots ,x_{n}\}$ such that every element of the group is a linear combination with integer coefficients of elements of G.

Let L be a free abelian group with basis $B=\{b_{1},\ldots ,b_{n}\}.$ There is a unique group homomorphism $p\colon L\to A,$ such that

$p(b_{i})=x_{i}\quad {\text{for }}i=1,\ldots ,n.$

This homomorphism is surjective, and its kernel is finitely generated (since integers form a Noetherian ring). Consider the matrix M with integer entries, such that the entries of its jth column are the coefficients of the jth generator of the kernel. Then, the abelian group is isomorphic to the cokernel of linear map defined by M. Conversely every integer matrix defines a finitely generated abelian group.

It follows that the study of finitely generated abelian groups is totally equivalent with the study of integer matrices. In particular, changing the generating set of A is equivalent with multiplying M on the left by a unimodular matrix (that is, an invertible integer matrix whose inverse is also an integer matrix). Changing the generating set of the kernel of M is equivalent with multiplying M on the right by a unimodular matrix.

The Smith normal form of M is a matrix

$S=UMV,$

where U and V are unimodular, and S is a matrix such that all non-diagonal entries are zero, the non-zero diagonal entries ⁠ $d_{1,1},\ldots ,d_{k,k}$ ⁠ are the first ones, and ⁠ $d_{j,j}$ ⁠ is a divisor of ⁠ $d_{i,i}$ ⁠ for *i* > *j*. The existence and the shape of the Smith normal form proves that the finitely generated abelian group A is the direct sum

$\mathbb {Z} ^{r}\oplus \mathbb {Z} /d_{1,1}\mathbb {Z} \oplus \cdots \oplus \mathbb {Z} /d_{k,k}\mathbb {Z} ,$

where r is the number of zero rows at the bottom of S (and also the rank of the group). This is the fundamental theorem of finitely generated abelian groups.

The existence of algorithms for Smith normal form shows that the fundamental theorem of finitely generated abelian groups is not only a theorem of abstract existence, but provides a way for computing expression of finitely generated abelian groups as direct sums.

## Infinite abelian groups

The simplest infinite abelian group is the infinite cyclic group $\mathbb {Z}$ . Any finitely generated abelian group A is isomorphic to the direct sum of r copies of $\mathbb {Z}$ and a finite abelian group, which in turn is decomposable into a direct sum of finitely many cyclic groups of prime power orders. Even though the decomposition is not unique, the number r , called the rank of A , and the prime powers giving the orders of finite cyclic summands are uniquely determined.

By contrast, classification of general infinitely generated abelian groups is far from complete. Divisible groups, i.e. abelian groups A in which the equation $nx=a$ admits a solution $x\in A$ for any natural number n and element a of A , constitute one important class of infinite abelian groups that can be completely characterized. Every divisible group is isomorphic to a direct sum, with summands isomorphic to $\mathbb {Q}$ and Prüfer groups $\mathbb {Q} _{p}/\mathbb {Z} _{p}$ for various prime numbers p , and the cardinality of the set of summands of each type is uniquely determined. Moreover, if a divisible group A is a subgroup of an abelian group G then A admits a direct complement: a subgroup C of G such that $G=A\oplus C$ . Thus divisible groups are injective modules in the category of abelian groups, and conversely, every injective abelian group is divisible (Baer's criterion). An abelian group without non-zero divisible subgroups is called **reduced**.

Two important special classes of infinite abelian groups with diametrically opposite properties are *torsion groups* and *torsion-free groups*, exemplified by the groups $\mathbb {Q} /\mathbb {Z}$ (periodic) and $\mathbb {Q}$ (torsion-free).

### Torsion groups

An abelian group is called **periodic** or **torsion**, if every element has finite order. A direct sum of finite cyclic groups is periodic. Although the converse statement is not true in general, some special cases are known. The first and second Prüfer theorems state that if A is a periodic group, and it either has a **bounded exponent**, i.e., $nA=0$ for some natural number n , or is countable and the p -heights of the elements of A are finite for each p , then A is isomorphic to a direct sum of finite cyclic groups. The cardinality of the set of direct summands isomorphic to $\mathbb {Z} /p^{m}\mathbb {Z}$ in such a decomposition is an invariant of A . These theorems were later subsumed in the **Kulikov criterion**. In a different direction, Helmut Ulm found an extension of the second Prüfer theorem to countable abelian p -groups with elements of infinite height: those groups are completely classified by means of their Ulm invariants.

### Torsion-free and mixed groups

An abelian group is called **torsion-free** if every non-zero element has infinite order. Several classes of torsion-free abelian groups have been studied extensively:

- Free abelian groups, i.e. arbitrary direct sums of $\mathbb {Z}$
- Cotorsion and algebraically compact torsion-free groups such as the p -adic integers
- Slender groups

An abelian group that is neither periodic nor torsion-free is called **mixed**. If A is an abelian group and $T(A)$ is its torsion subgroup, then the factor group $A/T(A)$ is torsion-free. However, in general the torsion subgroup is not a direct summand of A , so A is *not* isomorphic to $T(A)\oplus A/T(A)$ . Thus the theory of mixed groups involves more than simply combining the results about periodic and torsion-free groups. The additive group $\mathbb {Z}$ of integers is torsion-free $\mathbb {Z}$ -module.

### Invariants and classification

One of the most basic invariants of an infinite abelian group A is its rank: the cardinality of the maximal linearly independent subset of A . Abelian groups of rank 0 are precisely the periodic groups, while torsion-free abelian groups of rank 1 are necessarily subgroups of $\mathbb {Q}$ and can be completely described. More generally, a torsion-free abelian group of finite rank r is a subgroup of $\mathbb {Q} _{r}$ . On the other hand, the group of p -adic integers $\mathbb {Z} _{p}$ is a torsion-free abelian group of infinite $\mathbb {Z}$ -rank and the groups $\mathbb {Z} _{p}^{n}$ with different n are non-isomorphic, so this invariant does not even fully capture properties of some familiar groups.

The classification theorems for finitely generated, divisible, countable periodic, and rank 1 torsion-free abelian groups explained above were all obtained before 1950 and form a foundation of the classification of more general infinite abelian groups. Important technical tools used in classification of infinite abelian groups are pure and basic subgroups. Introduction of various invariants of torsion-free abelian groups has been one avenue of further progress. See the books by Irving Kaplansky, László Fuchs, Phillip Griffith, and David Arnold, as well as the proceedings of the conferences on Abelian Group Theory published in *Lecture Notes in Mathematics* for more recent findings.

### Additive groups of rings

The additive group of a ring is an abelian group, but not all abelian groups are additive groups of rings (with nontrivial multiplication). Some important topics in this area of study are:

- Tensor product
- A.L.S. Corner's results on countable torsion-free groups
- Shelah's work to remove cardinality restrictions
- Burnside ring

## Relation to other mathematical topics

Many large abelian groups possess a natural topology, which turns them into topological groups.

The collection of all abelian groups, together with the homomorphisms between them, forms the category ${\textbf {Ab}}$ , the prototype of an abelian category.

Wanda Szmielew (1955) proved that the first-order theory of abelian groups, unlike its non-abelian counterpart, is decidable. Most algebraic structures other than Boolean algebras are undecidable.

There are still many areas of current research:

- Amongst torsion-free abelian groups of finite rank, only the finitely generated case and the rank 1 case are well understood.
- There are many unsolved problems in the theory of infinite-rank torsion-free abelian groups.
- While countable torsion abelian groups are well understood through simple presentations and Ulm invariants, the case of countable mixed groups is much less mature.
- Many mild extensions of the first-order theory of abelian groups are known to be undecidable.
- Finite abelian groups remain a topic of research in computational group theory.

Moreover, abelian groups of infinite order lead, quite surprisingly, to deep questions about the set theory commonly assumed to underlie all of mathematics. Take the Whitehead problem: are all Whitehead groups of infinite order also free abelian groups? In the 1970s, Saharon Shelah proved that the Whitehead problem is:

- Undecidable in ZFC (Zermelo–Fraenkel axioms), the conventional axiomatic set theory from which nearly all of present-day mathematics can be derived. The Whitehead problem is also the first question in ordinary mathematics proved undecidable in ZFC;
- Undecidable even if ZFC is augmented by taking the generalized continuum hypothesis as an axiom;
- Positively answered if ZFC is augmented with the axiom of constructibility (see statements true in L).

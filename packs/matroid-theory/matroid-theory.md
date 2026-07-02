---
title: "Matroid"
source: https://en.wikipedia.org/wiki/Matroid_theory
domain: matroid-theory
license: CC-BY-SA-4.0
tags: matroid theory, oriented matroid, tutte polynomial, matroid intersection
fetched: 2026-07-02
---

# Matroid

(Redirected from

Matroid theory

)

In combinatorics, a **matroid** /ˈmeɪtrɔɪd/ is a structure that abstracts and generalizes the notion of linear independence in vector spaces. There are many equivalent ways to define a matroid axiomatically, the most significant being in terms of: independent sets; bases or circuits; rank functions; closure operators; and closed sets or *flats*. In the language of partially ordered sets, a finite simple matroid is equivalent to a geometric lattice.

Matroid theory borrows extensively from the terms used in both linear algebra and graph theory, largely because it is the abstraction of various notions of central importance in these fields. Matroids have found applications in geometry, topology, combinatorial optimization, network theory, and coding theory.

## Definition

There are many equivalent ways to define a (finite) matroid.

### Independent sets

In terms of independence, a finite matroid M is a pair $(E,{\mathcal {I}})$ , where E is a finite set (called the *ground set*) and ${\mathcal {I}}$ is a family of subsets of E (called the *independent sets*) with the following properties:

- (I1) The empty set is independent, i.e., $\emptyset \in {\mathcal {I}}$ .

- (I2) Every subset of an independent set is independent, i.e., for each $A'\subseteq A$ , if $A\in {\mathcal {I}}$ then $A'\in {\mathcal {I}}$ . This is sometimes called the *hereditary property*, or the *downward-closed* property.

- (I3) If A and B are two independent sets (i.e., each set is independent) and A has more elements than B , then there exists $x\in A\setminus B$ such that $B\cup \{x\}$ is independent. This is sometimes called the *augmentation property* or the *independent set exchange property* (cf. Steinitz exchange lemma)

The first two properties define a combinatorial structure known as an independence system (or abstract simplicial complex). Actually, assuming (I2), property (I1) is equivalent to the fact that at least one subset of E is independent, i.e., ${\mathcal {I}}\neq \emptyset$ .

### Bases and circuits

A subset of the ground set E that is not independent is called *dependent*.

A maximal independent set – that is, an independent set that becomes dependent upon adding any element of E – is called a *basis* for the matroid.

A *circuit* in a matroid M is a minimal dependent subset of E – that is, a dependent set whose proper subsets are all independent. The term arises because the circuits of graphic matroids are cycles in the corresponding graphs.

The dependent sets, the bases, or the circuits of a matroid characterize the matroid completely: a set is independent if and only if it is not dependent, if and only if it is a subset of a basis, and if and only if it does not contain a circuit. The collections of dependent sets, of bases, and of circuits each have simple properties that may be taken as axioms for a matroid. For instance, one may define a matroid M to be a pair $(E,{\mathcal {B}})$ , where E is a finite set as before and ${\mathcal {B}}$ is a collection of subsets of E , called *bases*, with the following properties:

- (B1) ${\mathcal {B}}$ is nonempty.

- (B2) If A and B are distinct members of ${\mathcal {B}}$ and $a\in A\smallsetminus B$ , then there exists an element $b\in B\smallsetminus A$ such that $(A\smallsetminus \{a\})\cup \{b\}\in {\mathcal {B}}$ .

This property (B2) is called the *basis exchange property*. It follows from this property that no member of ${\mathcal {B}}$ can be a proper subset of any other.

### Rank functions

It is a basic result of matroid theory, directly analogous to a similar theorem of bases in linear algebra, that any two bases of a matroid M have the same number of elements. This number is called the *rank* of M . If M is a matroid on E , and A is a subset of E , then a matroid on A can be defined by considering a subset of A to be independent if and only if it is independent in M . This allows us to talk about *submatroids* and about the rank of any subset of E . The rank of a subset A is given by the *rank function* $r(A)$ of the matroid, which has the following properties:

- (R1) The value of the rank function is always a non-negative integer.

- (R2) For any subset $A\subset E$ , we have $r(A)\leq |A|$ .

- (R3) For any two subsets $A,B\subset E$ , we have: $r(A\cup B)+r(A\cap B)\leq r(A)+r(B)$ . That is, the rank is a submodular function.

- (R4) For any set A and element x , we have: $r(A)\leq r(A\cup \{x\})\leq r(A)+1$ . From the first inequality it follows more generally that, if $A\subseteq B\subseteq E$ , then $r(A)\leq r(B)\leq r(E)$ . That is, rank is a monotonic function.

These properties can be used as one of the alternative definitions of a finite matroid: If $(E,r)$ satisfies these properties, then the independent sets of a matroid over E can be defined as those subsets A of E with $r(A)=|A|$ . In the language of partially ordered sets, such a matroid structure is equivalent to the geometric lattice whose elements are the subsets $A\subset M$ , partially ordered by inclusion.

The difference $|A|-r(A)$ is called the *nullity* of the subset A . It is the minimum number of elements that must be removed from A to obtain an independent set. The nullity of E in M is called the nullity of M . The difference $r(E)-r(A)$ is sometimes called the *corank* of the subset A .

### Closure operators

Let M be a matroid on a finite set E , with rank function r as above. The *closure* or *span* $\operatorname {cl} (A)$ of a subset A of E is the set

$\operatorname {cl} (A)={\Bigl \{}\ x\in E\mid r(A)=r{\bigl (}A\cup \{x\}{\bigr )}{\Bigr \}}$

.

This defines a closure operator $\operatorname {cl$ where ${\mathcal {P}}$ denotes the power set, with the following properties:

- (C1) For all subsets X of E , $X\subseteq \operatorname {cl} (X).$

- (C2) For all subsets X of E , $\operatorname {cl} (X)=\operatorname {cl} \left(\operatorname {cl} \left(X\right)\right).$

- (C3) For all subsets X and Y of E with $X\subseteq Y$ , $\operatorname {cl} (X)\subseteq \operatorname {cl} (Y).$

- (C4) For all elements a and b from E and all subsets Y of E , if $a\in \operatorname {cl} (Y\cup \{b\})\smallsetminus \operatorname {cl} (Y)$ then $b\in \operatorname {cl} (Y\cup \{a\})\smallsetminus \operatorname {cl} (Y).$

The first three of these properties are the defining properties of a closure operator. The fourth is sometimes called the *Mac Lane–Steinitz exchange property*. These properties may be taken as another definition of matroid: every function $\operatorname {cl$ that obeys these properties determines a matroid.

### Flats

A set whose closure equals itself is said to be *closed*, or a *flat* or *subspace* of the matroid. A set is closed if it is maximal for its rank, meaning that the addition of any other element to the set would increase the rank. The closed sets of a matroid are characterized by a covering partition property:

- (F1) The whole point set E is closed.

- (F2) If S and T are flats, then $S\cap T$ is a flat.

- (F3) If S is a flat, then each element of $E\smallsetminus S$ is in precisely one of the flats T that cover S (meaning that T properly contains S , but there is no flat U between S and T ).

The class ${\mathcal {L}}(M)$ of all flats, partially ordered by set inclusion, forms a matroid lattice. Conversely, every matroid lattice L forms a matroid over its set E of atoms under the following closure operator: for a set S of atoms with join $\bigvee S$ ,

$\operatorname {cl} (S)=\{x\in E\mid x\leq \bigvee S\}.$

The flats of this matroid correspond one-for-one with the elements of the lattice; the flat corresponding to lattice element y is the set

$\{x\in E\mid x\leq y\}.$

Thus, the lattice of flats of this matroid is naturally isomorphic to L .

### Hyperplanes (coatoms)

In a matroid of rank r , a flat of rank $r-1$ is called a *hyperplane*, or *co-atoms* or *copoints*. These are the maximal proper flats; that is, the only superset of a hyperplane that is also a flat is the set E of all the elements of the matroid. An equivalent definition is that a coatom is a subset of *E* that does not span *M*, but such that adding any other element to it does make a spanning set.

The family ${\mathcal {H}}$ of hyperplanes of a matroid has the following properties, which may be taken as yet another axiomatization of matroids:

- (H1) The ground set E itself is not a hyperplane.

- (H2) There do not exist distinct sets X and Y in ${\mathcal {H}}$ with $X\subseteq Y$ . That is, the hyperplanes form a Sperner family.

- (H3) For every $x\in E$ and distinct $Y,Z\in {\mathcal {H}}$ with $x\notin Y\cup Z$ , there exists $X\in {\mathcal {H}}$ with $(Y\cap Z)\cup \{x\}\subseteq X$ .

### Graphoids

Minty (1966) defined a *graphoid* as a triple $(L,C,D)$ in which C and D are classes of nonempty subsets of L such that

- (G1) no element of C (called a "circuit") contains another,

- (G2) no element of D (called a "cocircuit") contains another,

- (G3) no set in C and set in D intersect in exactly one element, and

- (G4) whenever L is represented as the disjoint union of subsets $R,G,B$ with $G=\{g\}$ (a singleton set), then either an $X\in C$ exists such that $g\in X\subseteq R\cup G$ or a $Y\in D$ exists such that $g\in Y\subseteq B\cup G$ .

He proved that there is a matroid for which C is the class of circuits and D is the class of cocircuits. Conversely, if C and D are the circuit and cocircuit classes of a matroid M with ground set E , then $(E,C,D)$ is a graphoid. Thus, graphoids give a *self-dual cryptomorphic axiomatization* of matroids.

## Examples

### Free matroid

Let E be a finite set. The set of all subsets of E defines the independent sets of a matroid. It is called the free matroid over E .

### Uniform matroids

Let E be a finite set and k a natural number. One may define a matroid on E by taking every k element subset of E to be a basis. This is known as the *uniform matroid* of rank k . A uniform matroid with rank k and with n elements is denoted $U_{k,n}$ . All uniform matroids of rank at least 2 are simple (see § Additional terms). The uniform matroid of rank 2 on n points is called the n  *point line*. A matroid is uniform if and only if it has no circuits of size less than one plus the rank of the matroid. The direct sums of uniform matroids are called partition matroids.

In the uniform matroid $U_{0,n}$ , every element is a loop (an element that does not belong to any independent set), and in the uniform matroid $U_{n,n}$ , every element is a coloop (an element that belongs to all bases). The direct sum of matroids of these two types is a partition matroid in which every element is a loop or a coloop; it is called a *discrete matroid*. An equivalent definition of a discrete matroid is a matroid in which every proper, non-empty subset of the ground set E is a separator.

### Matroids from linear algebra

Matroid theory developed mainly out of a deep examination of the properties of independence and dimension in vector spaces. There are two ways to present the matroids defined in this way:

If

E

is any finite subset of a

vector space

V

, then we can define a matroid

M

on

E

by taking the independent sets of

M

to be the

linearly independent

subsets of

E

.

The validity of the independent set axioms for this matroid follows from the Steinitz exchange lemma.

If

M

is a matroid that can be defined in this way, we say the set

E

represents

M

.

Matroids of this kind are called

vector matroids

.

An important example of a matroid defined in this way is the Fano matroid, a rank three matroid derived from the Fano plane, a finite geometry with seven points (the seven elements of the matroid) and seven lines (the proper nontrivial flats of the matroid). It is a linear matroid whose elements may be described as the seven nonzero points in a three dimensional vector space over the finite field GF(2). However, it is not possible to provide a similar representation for the Fano matroid using the real numbers in place of GF(2).

A matrix A with entries in a field gives rise to a matroid M on its set of columns. The dependent sets of columns in the matroid are those that are linearly dependent as vectors.

This matroid is called the

column matroid

of

A

, and

A

is said to

represent

M

.

For instance, the Fano matroid can be represented in this way as a 3 × 7 (0,1) matrix. Column matroids are just vector matroids under another name, but there are often reasons to favor the matrix representation.

A matroid that is equivalent to a vector matroid, although it may be presented differently, is called *representable* or *linear*. If M is equivalent to a vector matroid over a field F , then we say M is *representable over* F ; in particular, M is *real representable* if it is representable over the real numbers. For instance, although a graphic matroid (see below) is presented in terms of a graph, it is also representable by vectors over any field.

A basic problem in matroid theory is to characterize the matroids that may be represented over a given field $F;$ Rota's conjecture describes a possible characterization for every finite field. The main results so far are characterizations of binary matroids (those representable over GF(2)) due to Tutte (1950s), of ternary matroids (representable over the 3 element field) due to Reid and Bixby, and separately to Seymour (1970s), and of quaternary matroids (representable over the 4 element field) due to Geelen, Gerards & Kapoor (2000). A proof of Rota's conjecture was announced, but not published, in 2014 by Geelen, Gerards, and Whittle.

A regular matroid is a matroid that is representable over all possible fields. The Vámos matroid is the simplest example of a matroid that is not representable over any field.

### Matroids from graph theory

A second original source for the theory of matroids is graph theory.

Every finite graph (or multigraph) G gives rise to a matroid $M(G)$ as follows: take as E the set of all edges in G and consider a set of edges independent if and only if it is a forest; that is, if it does not contain a simple cycle. Then $M(G)$ is called a *cycle matroid*. Matroids derived in this way are *graphic matroids*. Not every matroid is graphic, but all matroids on three elements are graphic. Every graphic matroid is regular.

Other matroids on graphs were discovered subsequently:

- The bicircular matroid of a graph is defined by calling a set of edges independent if every connected subset contains at most one cycle ie a set of edges is independent if and only if it is a pseudoforest .

- In any directed or undirected graph G let E and F be two distinguished sets of vertices. In the set E , define a subset U to be independent if there are $|U|$ vertex-disjoint paths from F onto U . This defines a matroid on E called a *gammoid*: a *strict gammoid* is one for which the set E is the whole vertex set of G .

- In a bipartite graph $G=(U,V,E)$ , one may form a matroid in which the elements are vertices on one side U of the bipartition, and the independent subsets are sets of endpoints of matchings of the graph. This is called a *transversal matroid*, and it is a special case of a gammoid. The transversal matroids are the dual matroids to the strict gammoids.

- Graphic matroids have been generalized to matroids from signed graphs, gain graphs, and biased graphs. A graph G with a distinguished linear class ${\mathcal {B}}$ of cycles, known as a "biased graph" $(G,{\mathcal {B}})$ , has two matroids, known as the *frame matroid* and the *lift matroid* of the biased graph.

If every cycle belongs to the distinguished class, these matroids coincide with the cycle matroid of

G

. If no cycle is distinguished, the frame matroid is the bicircular matroid of

G

. A signed graph, whose edges are labeled by signs, and a gain graph, which is a graph whose edges are labeled orientably from a group, each give rise to a biased graph and therefore have frame and lift matroids.

- The Laman graphs form the bases of the two-dimensional rigidity matroid, a matroid defined in the theory of structural rigidity.

- Let G be a connected graph and E be its edge set. Let I be the collection of subsets F of E such that $G-F$ is still connected. Then $M^{*}(G)$ , whose element set is E and with I as its class of independent sets, is a matroid called the *bond matroid* of G .

The rank function

$r(F)$

is the

cyclomatic number

of the subgraph induced on the edge subset

F

, which equals the number of edges outside a maximal forest of that subgraph, and also the number of independent cycles in it.

### Matroids from field extensions

A third original source of matroid theory is field theory.

An extension of a field gives rise to a matroid:

Suppose

F

and

K

are fields with

K

containing

F

. Let

E

be any finite subset of

K

.

Define a subset

S

of

E

to be

algebraically independent

if the extension field

$F(S)$

has

transcendence degree

equal to

$|S|$

.

A matroid that is equivalent to a matroid of this kind is called an algebraic matroid. The problem of characterizing algebraic matroids is extremely difficult; little is known about it. The Vámos matroid provides an example of a matroid that is not algebraic.

## Basic constructions

There are some standard ways to make new matroids out of old ones.

### Duality

If M is a finite matroid, we can define the *orthogonal* or *dual matroid* $M^{*}$ by taking the same underlying set and calling a set a *basis* in $M^{*}$ if and only if its complement is a basis in M . It is not difficult to verify that $M^{*}$ is a matroid and that the dual of $M^{*}$ is M .

The dual can be described equally well in terms of other ways to define a matroid. For instance:

- A set is independent in $M^{*}$ if and only if its complement spans M .

- A set is a circuit of $M^{*}$ if and only if its complement is a coatom in M .

- The rank function of the dual is $r^{*}(S)=|S|-r(M)+r\left(E\smallsetminus S\right)$ .

According to a matroid version of Kuratowski's theorem, the dual of a graphic matroid M is a graphic matroid if and only if M is the matroid of a planar graph. In this case, the dual of M is the matroid of the dual graph of G . The dual of a vector matroid representable over a particular field F is also representable over F . The dual of a transversal matroid is a strict gammoid and vice versa.

**Example**

The cycle matroid of a graph is the dual matroid of its bond matroid.

### Minors

If *M* is a matroid with element set *E*, and *S* is a subset of *E*, the *restriction* of *M* to *S*, written *M* |*S*, is the matroid on the set *S* whose independent sets are the independent sets of *M* that are contained in *S*. Its circuits are the circuits of *M* that are contained in *S* and its rank function is that of *M* restricted to subsets of *S*.

In linear algebra, this corresponds to restricting to the subspace generated by the vectors in *S*. Equivalently if *T* = *M*−*S* this may be termed the *deletion* of *T*, written *M*\*T* or *M*−*T*. The submatroids of *M* are precisely the results of a sequence of deletions: the order is irrelevant.

The dual operation of restriction is contraction. If *T* is a subset of *E*, the *contraction* of *M* by *T*, written *M*/*T*, is the matroid on the underlying set *E* − *T* whose rank function is $r'(A)=r(A\cup T)-r(T)$ . In linear algebra, this corresponds to looking at the quotient space by the linear space generated by the vectors in *T*, together with the images of the vectors in *E* − *T*.

A matroid *N* that is obtained from *M* by a sequence of restriction and contraction operations is called a minor of *M*. We say *M* *contains* *N* *as a minor*. Many important families of matroids may be characterized by the minor-minimal matroids that do not belong to the family; these are called *forbidden* or *excluded minors*.

### Sums and unions

Let *M* be a matroid with an underlying set of elements *E*, and let *N* be another matroid on an underlying set *F*. The *direct sum* of matroids *M* and *N* is the matroid whose underlying set is the disjoint union of *E* and *F*, and whose independent sets are the disjoint unions of an independent set of *M* with an independent set of *N*.

The *union* of *M* and *N* is the matroid whose underlying set is the union (not the disjoint union) of *E* and *F*, and whose independent sets are those subsets that are the union of an independent set in *M* and one in *N*. Usually the term "union" is applied when *E* = *F*, but that assumption is not essential. If *E* and *F* are disjoint, the union is the direct sum.

## Additional terms

Let *M* be a matroid with an underlying set of elements *E*.

- *E* may be called the *ground set* of *M*. Its elements may be called the *points* of *M*.

- A subset of *E* *spans* *M* if its closure is *E*. A set is said to *span* a closed set *K* if its closure is *K*.

- The girth of a matroid is the size of its smallest circuit or dependent set.

- An element that forms a single-element circuit of *M* is called a *loop*. Equivalently, an element is a loop if it belongs to no basis.

- An element that belongs to no circuit is called a *coloop* or *isthmus*. Equivalently, an element is a coloop if it belongs to every basis.

Loop and coloops are mutually dual.

- If a two-element set {*f, g*} is a circuit of *M*, then *f* and *g* are *parallel* in *M*.

- A matroid is called *simple* if it has no circuits consisting of 1 or 2 elements. That is, it has no loops and no parallel elements. The term *combinatorial geometry* is also used. A simple matroid obtained from another matroid *M* by deleting all loops and deleting one element from each 2-element circuit until no 2 element circuits remain is called a *simplification* of *M*. A matroid is *co-simple* if its dual matroid is simple.

- A union of circuits is sometimes called a *cycle* of *M*. A cycle is therefore the complement of a flat of the dual matroid. (This usage conflicts with the common meaning of "cycle" in graph theory.)

- A *separator* of *M* is a subset *S* of *E* such that $r(S)+r(E-S)=r(M)$ . A *proper* or *non-trivial separator* is a separator that is neither *E* nor the empty set. An *irreducible separator* is a non-empty separator that contains no other non-empty separator. The irreducible separators partition the ground set *E*.

- A matroid that cannot be written as the direct sum of two nonempty matroids, or equivalently that has no proper separators, is called *connected* or *irreducible*. A matroid is connected if and only if its dual is connected.

- A maximal irreducible submatroid of *M* is called a *component* of *M*. A component is the restriction of *M* to an irreducible separator, and contrariwise, the restriction of *M* to an irreducible separator is a component. A separator is a union of components.

- A matroid *M* is called a *frame matroid* if it, or a matroid that contains it, has a basis such that all the points of *M* are contained in the lines that join pairs of basis elements.

- A matroid is called a paving matroid if all of its circuits have size at least equal to its rank.

- The basis polytope $P_{M}$ is the convex hull of the indicator vectors of the bases of M

- The independence polytope of M is the convex hull of the indicator vectors of the independent sets of M .

## Algorithms

Several important combinatorial optimization problems can be solved efficiently on every matroid. In particular:

- Finding a **maximum-weight independent set in a weighted matroid** can be solved by a greedy algorithm. This fact may even be used to characterize matroids: if a family *F* of sets, closed under taking subsets, has the property that, no matter how the sets are weighted, the greedy algorithm finds a maximum-weight set in the family, then *F* must be the family of independent sets of a matroid.

- The **matroid partitioning problem** is to partition the elements of a matroid into as few independent sets as possible, and the **matroid packing problem** is to find as many disjoint spanning sets as possible. Both can be solved in polynomial time, and can be generalized to the problem of computing the rank or finding an independent set in a matroid sum.

- A **matroid intersection** of two or more matroids on the same ground set is the family of sets that are simultaneously independent in each of the matroids. The problem of finding the largest set, or the maximum weighted set, in the intersection of two matroids can be found in polynomial time, and provides a solution to many other important combinatorial optimization problems. For instance, maximum matching in bipartite graphs can be expressed as a problem of intersecting two partition matroids. However, finding the largest set in an intersection of three or more matroids is NP-complete.

## Matroid software

Two standalone systems for calculations with matroids are Kingan's Oid and Hlineny's Macek. Both of them are open-sourced packages. "Oid" is an interactive, extensible software system for experimenting with matroids. "Macek" is a specialized software system with tools and routines for reasonably efficient combinatorial computations with representable matroids.

Both open source mathematics software systems SAGE and Macaulay2 contain matroid packages. Maple has a package for dealing with matroids since the version 2024.

## Polynomial invariants

There are two especially significant polynomials associated to a finite matroid *M* on the ground set *E*. Each is a *matroid invariant*, which means that isomorphic matroids have the same polynomial.

### Characteristic polynomial

The *characteristic polynomial* of *M* – sometimes called the *chromatic polynomial*, although it does not count colorings – is defined to be

$p_{M}(\lambda ):=\sum _{S\subseteq E}(-1)^{|S|}\lambda ^{r(E)-r(S)},$

or equivalently (as long as the empty set is closed in *M*) as

$p_{M}(\lambda ):=\sum _{A}\mu (\emptyset ,A)\lambda ^{r(E)-r(A)},$

where μ denotes the Möbius function of the geometric lattice of the matroid and the sum is taken over all the flats A of the matroid.

- When *M* is the cycle matroid *M*(*G*) of a graph *G*, the characteristic polynomial is a slight transformation of the chromatic polynomial, which is given by χ*G* (λ) = *λ*c*p**M*(*G*) (*λ*), where *c* is the number of connected components of *G*.

- When *M* is the bond matroid *M**(*G*) of a graph *G*, the characteristic polynomial equals the flow polynomial of *G*.

- When *M* is the matroid *M*(*A*) of an arrangement *A* of linear hyperplanes in $\mathbb {R} ^{n}$ (or *F**n* where *F* is any field), the characteristic polynomial of the arrangement is given by *p**A* (*λ*) = *λ**n*−*r*(*M*)*p**M* (*λ*).

#### Beta invariant

The *beta invariant* of a matroid, introduced by Crapo (1967), may be expressed in terms of the characteristic polynomial p as an evaluation of the derivative

$\beta (M)=(-1)^{r(M)-1}p_{M}'(1)$

or directly as

$\beta (M)=(-1)^{r(M)}\sum _{X\subseteq E}(-1)^{|X|}r(X).$

The beta invariant is non-negative, and is zero if and only if M is disconnected, or empty, or a loop. Otherwise it depends only on the lattice of flats of M . If M has no loops and coloops then $\beta (M)=\beta (M^{*})$ .

### Whitney numbers

The *Whitney numbers of the first kind* of M are the coefficients of the powers of $\lambda$ in the characteristic polynomial. Specifically, the i th Whitney number $w_{i}(M)$ is the coefficient of $\lambda ^{r(M)-i}$ and is the sum of Möbius function values:

$w_{i}(M)=\sum \{\mu (\emptyset ,A):r(A)=i\},$

summed over flats of the right rank. These numbers alternate in sign, so that $(-1)^{i}w_{i}(M)>0$ for $0\leq i\leq r(M)$ .

The *Whitney numbers of the second kind* of M are the numbers of flats of each rank. That is, $W_{i}(M)$ is the number of rank  i flats.

The Whitney numbers of both kinds generalize the Stirling numbers of the first and second kind, which are the Whitney numbers of the cycle matroid of the complete graph, and equivalently of the partition lattice. They were named after Hassler Whitney, the (co)founder of matroid theory, by Gian-Carlo Rota. The name has been extended to the similar numbers for finite ranked partially ordered sets.

### Tutte polynomial

The *Tutte polynomial* of a matroid, $T_{M}(x,y)$ , generalizes the characteristic polynomial to two variables. This gives it more combinatorial interpretations, and also gives it the duality property

$T_{M^{*}}(x,y)=T_{M}(y,x),$

which implies a number of dualities between properties of M and properties of $M^{*}$ . One definition of the Tutte polynomial is

$T_{M}(x,y)=\sum _{S\subseteq E}(x-1)^{r(M)-r(S)}\ (y-1)^{|S|-r(S)}.$

This expresses the Tutte polynomial as an evaluation of the *co-rank-nullity* or *rank generating polynomial*,

$R_{M}(u,v)=\sum _{S\subseteq E}u^{r(M)-r(S)}v^{|S|-r(S)}.$

From this definition it is easy to see that the characteristic polynomial is, up to a simple factor, an evaluation of $T_{M}$ , specifically,

$p_{M}(\lambda )=(-1)^{r(M)}T_{M}(1-\lambda ,0).$

Another definition is in terms of internal and external activities and a sum over bases, reflecting the fact that $T(1,1)$ is the number of bases. This, which sums over fewer subsets but has more complicated terms, was Tutte's original definition.

There is a further definition in terms of recursion by deletion and contraction. The deletion-contraction identity is

$F(M)=F(M-e)+F(M/e)$

when e is neither a loop nor a coloop. An invariant of matroids (i.e., a function that takes the same value on isomorphic matroids) satisfying this recursion and the multiplicative condition

$F(M\oplus M')=F(M)F(M')$

is said to be a *Tutte–Grothendieck invariant*. The Tutte polynomial is the most general such invariant; that is, the Tutte polynomial is a Tutte–Grothendieck invariant and every such invariant is an evaluation of the Tutte polynomial.

The Tutte polynomial $T_{G}$ of a graph is the Tutte polynomial $T_{M(G)}$ of its cycle matroid.

## Infinite matroids

The theory of infinite matroids is much more complicated than that of finite matroids and forms a subject of its own. For a long time, one of the difficulties has been that there were many reasonable and useful definitions, none of which appeared to capture all the important aspects of finite matroid theory. For instance, it seemed to be hard to have bases, circuits, and duality together in one notion of infinite matroids.

The simplest definition of an infinite matroid is to require *finite rank*; that is, the rank of *E* is finite. This theory is similar to that of finite matroids except for the failure of duality due to the fact that the dual of an infinite matroid of finite rank does not have finite rank. Finite-rank matroids include any subsets of finite-dimensional vector spaces and of field extensions of finite transcendence degree.

The next simplest infinite generalization is finitary matroids, also known as pregeometries. A matroid with possibly infinite ground set is *finitary* if it has the property that

$x\in \operatorname {cl} (Y)\ \Leftrightarrow \ {\text{ there is a finite set }}Y'\subseteq Y{\text{ such that }}x\in \operatorname {cl} (Y').$

Equivalently, every dependent set contains a finite dependent set.

Examples are linear dependence of arbitrary subsets of infinite-dimensional vector spaces (but not infinite dependencies as in Hilbert and Banach spaces), and algebraic dependence in arbitrary subsets of field extensions of possibly infinite transcendence degree. Again, the class of finitary matroid is not self-dual, because the dual of a finitary matroid is not finitary.

Finitary infinite matroids are studied in model theory, a branch of mathematical logic with strong ties to algebra.

In the late 1960s matroid theorists asked for a more general notion that shares the different aspects of finite matroids and generalizes their duality. Many notions of infinite matroids were defined in response to this challenge, but the question remained open. One of the approaches examined by D.A. Higgs became known as *B-matroids* and was studied by Higgs, Oxley, and others in the 1960s and 1970s. According to a recent result by Bruhn et al. (2013), it solves the problem: Arriving at the same notion independently, they provided five equivalent systems of axiom—in terms of independence, bases, circuits, closure and rank. The duality of B-matroids generalizes dualities that can be observed in infinite graphs.

The independence axioms are as follows:

1. The empty set is independent.
2. Every subset of an independent set is independent.
3. For every nonmaximal (under set inclusion) independent set I and maximal independent set J , there is $x\in J\smallsetminus I$ such that $I\cup \{x\}$ is independent.
4. For every subset X of the base space, every independent subset I of X can be extended to a maximal independent subset of X .

With these axioms, every matroid has a dual.

## History

Matroid theory was introduced by Whitney (1935). It was also independently discovered by Takeo Nakasawa, whose work was forgotten for many years (Nishimura & Kuroda (2009)).

In his seminal paper, Whitney provided two axioms for independence, and defined any structure adhering to these axioms to be "matroids". His key observation was that these axioms provide an abstraction of "independence" that is common to both graphs and matrices. Because of this, many of the terms used in matroid theory resemble the terms for their analogous concepts in linear algebra or graph theory.

Almost immediately after Whitney first wrote about matroids, an important article was written by MacLane (1936) on the relation of matroids to projective geometry. A year later, van der Waerden (1937) noted similarities between algebraic and linear dependence in his classic textbook on Modern Algebra.

In the 1940s Richard Rado developed further theory under the name "independence systems" with an eye towards transversal theory, where his name for the subject is still sometimes used.

In the 1950s W.T. Tutte became the foremost figure in matroid theory, a position he retained for many years. His contributions were plentiful, including

- the characterization of binary, regular, and graphic matroids by excluded minors

- the regular-matroid representability theorem

- the theory of chain groups and their matroids

and the tools he used to prove many of his results:

- the "Path theorem"

- "Tutte homotopy theorem" (see, e.g., Tutte (1965))

which are so complicated that later theorists have gone to great trouble to eliminate the need for them in proofs.

Crapo (1969) and Brylawski (1972) generalized to matroids Tutte's "dichromate", a graphic polynomial now known as the Tutte polynomial (named by Crapo). Their work has recently (especially in the 2000s) been followed by a flood of papers—though not as many as on the Tutte polynomial of a graph.

In 1976 Dominic Welsh published the first comprehensive book on matroid theory.

Paul Seymour's decomposition theorem for regular matroids (Seymour (1980)) was the most significant and influential work of the late 1970s and the 1980s. Another fundamental contribution, by Kahn & Kung (1982), showed why projective geometries and Dowling geometries play such an important role in matroid theory.

By the 1980s there were many other important contributors, but one should not omit to mention Geoff Whittle's extension to ternary matroids of Tutte's characterization of binary matroids that are representable over the rationals (Whittle 1995), perhaps the biggest single contribution of the 1990s.

In the current period (since around 2000) the Matroid Minors Project of Geelen, Gerards, Whittle, and others, has produced substantial advances in the structure theory of matroids. Many others have also contributed to that part of matroid theory, which (in the first and second decades of the 21st century) is flourishing.

## Researchers

Mathematicians who pioneered the study of matroids include

Susumu Kuroda

Saunders MacLane

Richard Rado

Takeo Nakasawa

Hirokazu Nishimura

William T. Tutte

B. L. van der Waerden

Hassler Whitney

Some of the other major contributors are

Jack Edmonds

Jim Geelen

Eugene Lawler

László Lovász

Gian-Carlo Rota

Paul D. Seymour

Dominic Welsh

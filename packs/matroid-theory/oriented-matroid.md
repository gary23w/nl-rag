---
title: "Oriented matroid"
source: https://en.wikipedia.org/wiki/Oriented_matroid
domain: matroid-theory
license: CC-BY-SA-4.0
tags: matroid theory, oriented matroid, tutte polynomial, matroid intersection
fetched: 2026-07-02
---

# Oriented matroid

An **oriented matroid** is a mathematical structure that abstracts the properties of directed graphs, vector arrangements over ordered fields, and hyperplane arrangements over ordered fields. In comparison, an ordinary (i.e., non-oriented) matroid abstracts the dependence properties that are common both to graphs, which are not necessarily *directed*, and to arrangements of vectors over fields, which are not necessarily *ordered*.

All oriented matroids have an underlying matroid. Thus, results on ordinary matroids can be applied to oriented matroids. However, the converse is false; some matroids cannot become an oriented matroid by *orienting* an underlying structure (e.g., circuits or independent sets). The distinction between matroids and oriented matroids is discussed further below.

Matroids are often useful in areas such as dimension theory and algorithms. Because of an oriented matroid's inclusion of additional details about the *oriented* nature of a structure, its usefulness extends further into several areas including geometry and optimization.

## History

The first appearance of oriented matroids was in a 1966 article by George J. Minty and was confined to regular matroids.

Subsequently R.T. Rockafellar (1969) suggested the problem of generalizing Minty's concept to real vector spaces. His proposal helped lead to the development of the general theory.

## Background

In order to abstract the concept of orientation on the edges of a graph to sets, one needs the ability to assign "direction" to the elements of a set. The way this achieved is with the following definition of *signed sets*.

- A *signed set*, X , combines a set of objects, ${\underline {X}}$ , with an ordered *bipartition* $(X^{+},X^{-})$ of that set into two disjoint subsets: $X^{+}$ and $X^{-}$ .

The members of

$X^{+}$

are called the

positive elements

; members of

$X^{-}$

are the

negative elements

.

- The set ${\underline {X}}=X^{+}\cup X^{-}$ is called the *support* of X .
- The *empty signed set*, $\emptyset$ , is defined as the empty set ${\underline {\emptyset }}$ combined with an (ordered) bipartition of it into two empty sets: $\emptyset ^{+}$ and $\emptyset ^{-}$ .
- The signed set Y is the *opposite* of X , written $Y=-X$ , if $Y^{+}=X^{-}$ and $Y^{-}=X^{+}.$

Given an element x of the support, we will write x for a positive element and $-x$ for a negative element. In this way, a signed set is just adding negative signs to distinguished elements. This will make sense as a "direction" only when we consider orientations of larger structures. Then the sign of each element will encode its direction relative to this orientation.

## Axiomatizations

Like ordinary matroids, several equivalent systems of axioms exist. (Such structures that possess multiple equivalent axiomatizations are called cryptomorphic.)

### Circuit axioms

Let E be any set. We refer to E as the *ground set*. Let ${\mathcal {C}}$ be a collection of *signed sets*, each of which is *supported* by a subset of E . If the following axioms hold for ${\mathcal {C}}$ , then equivalently ${\mathcal {C}}$ is the set of *signed circuits* for an *oriented matroid* on E .

- (C0) $\emptyset \notin {\mathcal {C}}$
- (C1) (symmetric) ${\text{ For all }}X\in {\mathcal {C}},~-\!X\in {\mathcal {C}}.$
- (C2) (incomparable) ${\text{ For all }}X,Y\in {\mathcal {C}},~~{\text{ if }}{\underline {X}}\subseteq {\underline {Y}}{\text{ then }}(X=Y{\text{ or }}X=-Y).$
- (C3) (weak elimination) ${\text{ For all }}X,Y\in {\mathcal {C}},X\neq -Y{\text{ with an }}e\in X^{+}\cap Y^{-}{\text{ there is a }}Z\in {\mathcal {C}}{\text{ such that }}$
  - $Z^{+}\subseteq (X^{+}\cup Y^{+})\setminus \{e\}{\text{ and }}$
  - $Z^{-}\subseteq (X^{-}\cup Y^{-})\setminus \{e\}.$

### Vector Axioms

The *composition* of signed sets X and Y is the signed set $X\circ Y$ defined by ${\underline {X\circ Y}}={\underline {X}}\cup {\underline {Y}}$ , $(X\circ Y)^{+}=X^{+}\cup \left(Y^{+}\setminus X^{-}\right)$ , and $(X\circ Y)^{-}=X^{-}\cup \left(Y^{-}\setminus X^{+}\right)$ . The *vectors* of an oriented matroid are the compositions of circuits. The vectors ${\mathcal {V}}$ of an oriented matroid satisfy the following axioms:

- $\emptyset \in {\mathcal {V}}$
- ${\mathcal {V}}=-{\mathcal {V}}$
- for all $X,Y\in {\mathcal {V}}$ , $X\circ Y\in {\mathcal {V}}$
- for all $X,Y\in {\mathcal {V}}$ , $e\in X^{+}\cap Y^{-}$ and $f\in ({\underline {X}}\setminus {\underline {Y}})\cup ({\underline {Y}}\setminus {\underline {X}})\cup (X^{+}\cap Y^{+})\cup (X^{-}\cap Y^{-})$ , there is a $Z\in {\mathcal {V}}$ , such that
  - $Z^{+}\subset X^{+}\cup Y^{+}\setminus e$ ,
  - $Z^{-}\subset X^{-}\cup Y^{-}\setminus e$ , and
  - $f\in {\underline {Z}}$ .

The *covectors* of an oriented matroid are the vectors of its dual oriented matroid.

### Chirotope axioms

Let E be as above. For each non-negative integer r , a *chirotope of rank r* is a function $\chi \colon E^{r}\to \{-1,0,1\}$ that satisfies the following axioms:

- (B0) *(non-trivial)*: $\chi$ is not identically zero
- (B1) *(alternating)*: For any permutation $\sigma$ and $x_{1},\dots ,x_{r}\in E$ , $\chi \left(x_{\sigma (1)},\dots ,x_{\sigma (r)}\right)=\operatorname {sgn} (\sigma )\chi \left(x_{1},\dots ,x_{r}\right)$ , where $\operatorname {sgn} (\sigma )$ is the sign of the permutation.
- (B2) *(exchange)*: For any $x_{1},\dots ,x_{r},y_{1},\dots ,y_{r}\in E$ such that $\chi (y_{i},x_{2},\dots ,x_{r})\chi (y_{1},\dots ,y_{i-1},x_{1},y_{i+1},\dots ,y_{r})\geq 0$ for each i , then we also have $\chi \left(x_{1},\dots ,x_{r}\right)\chi \left(y_{1},\dots ,y_{r}\right)\geq 0$ .

The term *chirotope* is derived from the mathematical notion of chirality, which is a concept abstracted from chemistry, where it is used to distinguish molecules that have the same structure except for a reflection.

### Equivalence

Every chirotope of rank r gives rise to a set of bases of a matroid on E consisting of those r -element subsets that $\chi$ assigns a nonzero value. The chirotope can then sign the circuits of that matroid. If C is a circuit of the described matroid, then $C\subset \{x_{1},\dots ,x_{r},x_{r+1}\}$ where $\{x_{1},\dots ,x_{r}\}$ is a basis. Then C can be signed with positive elements

$C^{+}=\{x_{i}:(-1)^{i}\chi (x_{1},\dots ,x_{i-1},x_{i+1},\dots ,x_{r+1})=1\}$

and negative elements the complement. Thus a chirotope gives rise to the *oriented bases* of an oriented matroid. In this sense, (B0) is the nonempty axiom for bases and (B2) is the basis exchange property.

## Examples

Oriented matroids are often introduced (e.g., Bachem and Kern) as an abstraction for directed graphs or systems of linear inequalities. Below are the explicit constructions.

### Directed graphs

Given a digraph, we define a signed circuit from the standard circuit of the graph by the following method. The support of the signed circuit $\textstyle {\underline {X}}$ is the standard set of edges in a minimal cycle. We go along the cycle in the clockwise or anticlockwise direction assigning those edges whose orientation agrees with the direction to the positive elements $\textstyle X^{+}$ and those edges whose orientation disagrees with the direction to the negative elements $\textstyle X^{-}$ . If $\textstyle {\mathcal {C}}$ is the set of all such $\textstyle X$ , then $\textstyle {\mathcal {C}}$ is the set of signed circuits of an oriented matroid on the set of edges of the directed graph.

If we consider the directed graph on the right, then we can see that there are only two (graph) circuits, namely $\textstyle \{(1,2),(1,3),(3,2)\}$ and $\textstyle \{(3,4),(4,3)\}$ . Then there are only four possible signed circuits corresponding to clockwise and anticlockwise orientations, namely $\textstyle \{(1,2),-(1,3),-(3,2)\}$ , $\textstyle \{-(1,2),(1,3),(3,2)\}$ , $\textstyle \{(3,4),(4,3)\}$ , and $\textstyle \{-(3,4),-(4,3)\}$ . These four sets form the set of signed circuits of an oriented matroid on the set $\textstyle \{(1,2),(1,3),(3,2),(3,4),(4,3)\}$ .

This is opposed to the ordinary directed graphic matroid for the same graph, whose only circuit is $\textstyle \{(3,4),(4,3)\}$ , as the other edges cannot form a directed cycle without flipping the direction of some of them.

### Linear algebra

If $\textstyle E$ is any finite subset of $\textstyle \mathbb {R} ^{n}$ , then the set of minimal linearly dependent sets forms the circuit set of a matroid on $\textstyle E$ . To extend this construction to oriented matroids, for each circuit $\textstyle \{v_{1},\dots ,v_{m}\}$ there is a minimal linear dependence

$\sum _{i=1}^{m}\lambda _{i}v_{i}=0$

with $\textstyle \lambda _{i}\in \mathbb {R}$ . Then the signed circuit $\textstyle X=\{X^{+},X^{-}\}$ has positive elements $\textstyle X^{+}=\{v_{i}:\lambda _{i}>0\}$ and negative elements $\textstyle X^{-}=\{v_{i}:\lambda _{i}<0\}$ . The set of all such $\textstyle X$ forms the set of signed circuits of an oriented matroid on $\textstyle E$ . Oriented matroids that can be realized this way are called representable.

Given the same set of vectors E , we can define the same oriented matroid with a chirotope $\chi :E^{r}\rightarrow \{-1,0,1\}$ . For any $x_{1},\dots ,x_{r}\in E$ let

$\chi (x_{1},\dots ,x_{r})=\operatorname {sgn} (\det(x_{1},\dots ,x_{r}))$

where the right hand side of the equation is the sign of the determinant. Then $\chi$ is the chirotope of the same oriented matroid on the set E .

### Hyperplane arrangements

A real hyperplane arrangement ${\mathcal {A}}=\{H_{1},\ldots ,H_{n}\}$ is a finite set of hyperplanes in $\mathbb {R} ^{d}$ , each containing the origin. By picking one side of each hyperplane to be the positive side, we obtain an arrangement of half-spaces. A half-space arrangement breaks down the ambient space into a finite collection of cells, each defined by which side of each hyperplane it lands on. That is, assign each point $x\in \mathbb {R} ^{d}$ to the signed set $X=(X^{+},X^{-})$ with $i\in X^{+}$ if x is on the positive side of $H_{i}$ and $i\in X^{-}$ if x is on the negative side of $H_{i}$ . This collection of signed sets defines the set of covectors of the oriented matroid, which are the vectors of the dual oriented matroid.

Each rank-3 oriented matroid is equivalent to an arrangement of pseudolines, and each oriented matroid which is also *uniform* is equivalent to a **simple** pseudoline arrangement (where every 2 lines cross exactly once, and no 3 lines cross at the same point). Tools for dealing with one form can therefore be used to analyze its equivalent form for either study.

### Convex polytope

Günter M. Ziegler introduces oriented matroids via convex polytopes.

## Results

### Orientability

A standard matroid is called *orientable* if its circuits are the supports of signed circuits of some oriented matroid. It is known that all real representable matroids are orientable. It is also known that the class of orientable matroids is closed under taking minors, however the list of forbidden minors for orientable matroids is known to be infinite. In this sense, oriented matroids is a much stricter formalization than regular matroids.

### Duality

Just as a matroid has a unique duals, an oriented matroid has a unique dual, often called its "orthogonal dual". What this means is that the underlying matroids are dual and that the cocircuits are signed so that they are "orthogonal" to every circuit. Two signed sets are said to be *orthogonal* if the intersection of their supports is empty or if the restriction of their positive elements to the intersection and negative elements to the intersection form two nonidentical and non-opposite signed sets. The existence and uniqueness of the dual oriented matroid depends on the fact that every signed circuit is orthogonal to every signed cocircuit.

To see why orthogonality is necessary for uniqueness one needs only to look to the digraph example above. We know that for planar graphs the dual of the circuit matroid is the circuit matroid of the graph's planar dual. Thus there are as many different dual pairs of oriented matroids based on the matroid of the graph as there are ways to orient the graph and in a corresponding way its dual.

To see the explicit construction of this unique orthogonal dual oriented matroid, consider an oriented matroid's chirotope $\chi :E^{r}\rightarrow \{-1,0,1\}$ . If we consider a list of elements of $x_{1},\dots ,x_{k}\in E$ as a cyclic permutation then we define $\operatorname {sgn} (x_{1},\dots ,x_{k})$ to be the sign of the associated permutation. If $\chi ^{*}:E^{|E|-r}\rightarrow \{-1,0,1\}$ is defined as

$\chi ^{*}(x_{1},\dots ,x_{r})\mapsto \chi (x_{r+1},\dots ,x_{|E|})\operatorname {sgn} (x_{1},\dots ,x_{r},x_{r+1},\dots ,x_{|E|}),$

then $\chi ^{*}$ is the chirotope of the unique orthogonal dual oriented matroid.

### Topological representation

Not all oriented matroids are representable—that is, not all have realizations as point configurations, or, equivalently, hyperplane arrangements. However, in some sense, all oriented matroids come close to having realizations as hyperplane arrangements. In particular, the **Folkman–Lawrence topological representation theorem** states that any oriented matroid has a realization as an arrangement of pseudospheres. A d -dimensional *pseudosphere* is an embedding of $e:S^{d}\hookrightarrow S^{d+1}$ such that there exists a homeomorphism $h:S^{d+1}\rightarrow S^{d+1}$ so that $h\circ e$ embeds $S^{d}$ as an equator of $S^{d+1}$ . In this sense a pseudosphere is just a tame sphere (as opposed to wild spheres). A *pseudosphere arrangement in $S^{d}$* is a collection of pseudospheres that intersect along pseudospheres. Finally, the Folkman–Lawrence topological representation theorem states that every oriented matroid of rank $d+1$ can be obtained from a pseudosphere arrangement in $S^{d}$ . It is named after Jon Folkman and Jim Lawrence, who published it in 1978.

### Geometry

The theory of oriented matroids has influenced the development of combinatorial geometry, especially the theory of convex polytopes, zonotopes, and configurations of vectors (equivalently, arrangements of hyperplanes). Many results—Carathéodory's theorem, Helly's theorem, Radon's theorem, the Hahn–Banach theorem, the Krein–Milman theorem, the lemma of Farkas—can be formulated using appropriate oriented matroids.

### Optimization

The development of an axiom system for oriented matroids was initiated by R. Tyrrell Rockafellar to describe the sign patterns of the matrices arising through the pivoting operations of Dantzig's simplex algorithm; Rockafellar was inspired by Albert W. Tucker's studies of such sign patterns in "Tucker tableaux".

The theory of oriented matroids has led to breakthroughs in combinatorial optimization. In linear programming, it was the language in which Robert G. Bland formulated his pivoting rule, by which the simplex algorithm avoids cycles. Similarly, it was used by Terlaky and Zhang to prove that their criss-cross algorithms have finite termination for linear programming problems. Similar results were made in convex quadratic programming by Todd and Terlaky. It has been applied to linear-fractional programming, quadratic-programming problems, and linear complementarity problems.

Outside of combinatorial optimization, oriented matroid theory also appears in convex minimization in Rockafellar's theory of "monotropic programming" and related notions of "fortified descent". Similarly, matroid theory has influenced the development of combinatorial algorithms, particularly the greedy algorithm. More generally, a greedoid is useful for studying the finite termination of algorithms.

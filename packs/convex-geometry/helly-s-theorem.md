---
title: "Helly's theorem"
source: https://en.wikipedia.org/wiki/Helly's_theorem
domain: convex-geometry
license: CC-BY-SA-4.0
tags: convex geometry, convex polytope, supporting hyperplane, helly's theorem
fetched: 2026-07-02
---

# Helly's theorem

**Helly's theorem** is a basic result in discrete geometry on the intersection of convex sets. It was discovered by Eduard Helly in 1913, but not published by him until 1923, by which time alternative proofs by Radon (1921) and König (1922) had already appeared. Helly's theorem gave rise to the notion of a Helly family.

## Statement

Let *X*1, ..., *Xn* be a finite collection of convex subsets of $\mathbb {R} ^{d}$ , with $n\geq d+1$ . If the intersection of every $d+1$ of these sets is nonempty, then the whole collection has a nonempty intersection; that is,

$\bigcap _{j=1}^{n}X_{j}\neq \varnothing .$

For infinite collections one has to assume compactness:

Let $\{X_{\alpha }\}$ be a collection of compact convex subsets of $\mathbb {R} ^{d}$ , such that every subcollection of cardinality at most $d+1$ has nonempty intersection. Then the whole collection has nonempty intersection.

## Proof

We prove the finite version, using Radon's theorem as in the proof by Radon (1921). The infinite version then follows by the finite intersection property characterization of compactness: a collection of closed subsets of a compact space has a non-empty intersection if and only if every finite subcollection has a non-empty intersection (once you fix a single set, the intersection of all others with it are closed subsets of a fixed compact space).

The proof is by induction:

**Base case:** Let *n* = *d* + 2. By our assumptions, for every *j* = 1, ..., *n* there is a point *xj* that is in the common intersection of all *Xi* with the possible exception of *Xj*. Now we apply Radon's theorem to the set *A* = {*x*1, ..., *xn*}, which furnishes us with disjoint subsets *A*1, *A*2 of A such that the convex hull of *A*1 intersects the convex hull of *A*2. Suppose that p is a point in the intersection of these two convex hulls. We claim that

$p\in \bigcap _{j=1}^{n}X_{j}.$

Indeed, consider any *j* ∈ {1, ..., *n*}. We shall prove that *p* ∈ *Xj*. Note that the only element of A that may not be in *Xj* is *xj*. If *xj* ∈ *A*1, then *xj* ∉ *A*2, and therefore *Xj* ⊃ *A*2. Since *Xj* is convex, it then also contains the convex hull of *A*2 and therefore also *p* ∈ *Xj*. Likewise, if *xj* ∉ *A*1, then *Xj* ⊃ *A*1, and by the same reasoning *p* ∈ *Xj*. Since p is in every *Xj*, it must also be in the intersection.

Above, we have assumed that the points *x*1, ..., *xn* are all distinct. If this is not the case, say *xi* = *xk* for some *i* ≠ *k*, then *xi* is in every one of the sets *Xj*, and again we conclude that the intersection is nonempty. This completes the proof in the case *n* = *d* + 2.

**Inductive Step:** Suppose *n* > *d* + 2 and that the statement is true for *n*−1. The argument above shows that any subcollection of *d* + 2 sets will have nonempty intersection. We may then consider the collection where we replace the two sets *X**n*−1 and *Xn* with the single set *X**n*−1 ∩ *Xn*. In this new collection, every subcollection of *d* + 1 sets will have nonempty intersection. The inductive hypothesis therefore applies, and shows that this new collection has nonempty intersection. This implies the same for the original collection, and completes the proof.

**Topological proof of the base case**

Let $X=X_{1}\cup \cdots \cup X_{n+2}$ , and consider the cover ${\mathcal {U}}=\{X_{i}\}_{i=1}^{n+2}$ . Since the intersection of convex sets is convex, every non-empty finite intersection of elements of ${\mathcal {U}}$ is contractible. Hence ${\mathcal {U}}$ is a good cover.

By the basic nerve lemma, X is homotopy equivalent to the geometric realization $|{\mathcal {N}}|$ of the nerve ${\mathcal {N}}$ of the cover. Assuming that

$X_{1}\cap \cdots \cap X_{n+2}=\varnothing ,$ the nerve ${\mathcal {N}}$ is the boundary complex of the simplex $\Delta ^{n+1}$ consisting of all the n -faces. Therefore $|{\mathcal {N}}|$ is homeomorphic to $S^{n}$ . It follows that $H_{n}(X)\cong H_{n}(S^{n})\cong \mathbb {Z} .$ This is a contradiction, since X is a non-compact n -dimensional manifold, and the top homology group of a non-compact manifold is zero.

## Colorful Helly theorem

The **colorful Helly theorem** is an extension of Helly's theorem in which, instead of one collection, there are *d*+1 collections of convex subsets of **R***d*.

If, for *every* choice of a *transversal* – one set from every collection – there is a point in common to all the chosen sets, then for *at least one* of the collections, there is a point in common to all sets in the collection.

Figuratively, one can consider the *d*+1 collections to be of *d*+1 different colors. Then the theorem says that, if every choice of one-set-per-color has a non-empty intersection, then there exists a color such that all sets of that color have a non-empty intersection.

## Fractional Helly theorem

For every *a* > 0 there is some *b* > 0 such that, if *X*1, ..., *Xn* are *n* convex subsets of **R***d*, and at least an *a*-fraction of (*d*+1)-tuples of the sets have a point in common, then a fraction of at least *b* of the sets have a point in common.

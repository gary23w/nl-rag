---
title: "Dual matroid"
source: https://en.wikipedia.org/wiki/Dual_matroid
domain: matroid-theory
license: CC-BY-SA-4.0
tags: matroid theory, oriented matroid, tutte polynomial, matroid intersection
fetched: 2026-07-02
---

# Dual matroid

In matroid theory, the **dual** of a matroid M is another matroid $M^{\ast }$ that has the same elements as M , and in which a set is independent if and only if M has a basis set disjoint from it.

Matroid duals go back to the original paper by Hassler Whitney defining matroids. They generalize to matroids the notions of plane graph duality.

## Basic properties

Duality is an involution: for all M , $(M^{\ast })^{\ast }=M$ .

An alternative definition of the dual matroid is that its basis sets are the complements of the basis sets of M . The basis exchange axiom, used to define matroids from their bases, is self-complementary, so the dual of a matroid is necessarily a matroid.

The flats of M are complementary to the cyclic sets (unions of circuits) of $M^{\ast }$ , and vice versa.

If r is the rank function of a matroid M on ground set E , then the rank function of the dual matroid is $r^{\ast }(S)=r(E\setminus S)+|S|-r(E)$ .

## Minors

A matroid minor is formed from a larger matroid M by two operations: the restriction $M\setminus x$ deletes element x from M without changing the independence or rank of the remaining sets, and the contraction $M/x$ deletes x from M after subtracting one from the rank of every set it belongs to. These two operations are dual: $M\setminus x=(M^{\ast }/x)^{\ast }$ and $M/x=(M^{\ast }\setminus x)^{\ast }$ . Thus, a minor of a dual is the same thing as a dual of a minor.

## Self-dual matroids

An individual matroid is self-dual (generalizing e.g. the self-dual polyhedra for graphic matroids) if it is isomorphic to its own dual. The isomorphism may, but is not required to, leave the elements of the matroid fixed. Any algorithm that tests whether a given matroid is self-dual, given access to the matroid via an independence oracle, must perform an exponential number of oracle queries, and therefore cannot take polynomial time.

## Matroid families

Many important matroid families are self-dual, meaning that a matroid belongs to the family if and only if its dual does. Many other matroid families come in dual pairs. Examples of this phenomenon include:

- The binary matroids (matroids representable over GF(2)), the matroids representable over any other field, and the regular matroids, are all self-dual families.
- The gammoids form a self-dual family. The strict gammoids are dual to the transversal matroids.
- The uniform matroids and partition matroids are self-dual. The dual to a uniform matroid $U{}_{n}^{r}$ is the uniform matroid $U{}_{n}^{n-r}$ . Within the family of uniform matroids, any matroid where $r=n/2$ is dual exactly to itself.
- The dual of a graphic matroid is itself graphic if and only if the underlying graph is planar; the matroid of the dual of a planar graph is the same as the dual of the matroid of the graph. Thus, the family of graphic matroids of planar graphs is self-dual.
- Among the graphic matroids, and more generally among the binary matroids, the bipartite matroids (matroids in which every circuit is even) are dual to the Eulerian matroids (matroids that can be partitioned into disjoint circuits).

It is an open problem whether the family of algebraic matroids is self-dual.

If *V* is a vector space and *V** is its orthogonal complement, then the linear matroid of *V* and the linear matroid of *V** are duals. As a corollary, the dual of any linear matroid is a linear matroid.

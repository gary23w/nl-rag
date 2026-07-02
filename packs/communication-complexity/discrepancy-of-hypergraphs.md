---
title: "Discrepancy of hypergraphs"
source: https://en.wikipedia.org/wiki/Discrepancy_of_hypergraphs
domain: communication-complexity
license: CC-BY-SA-4.0
tags: communication complexity, two party protocol, fooling set, discrepancy method
fetched: 2026-07-02
---

# Discrepancy of hypergraphs

**Discrepancy of hypergraphs** is an area of discrepancy theory that studies the discrepancy of general set systems.

## Definitions

In the classical setting, we aim at partitioning the vertices of a hypergraph ${\mathcal {H}}=(V,{\mathcal {E}})$ into two classes in such a way that ideally each hyperedge contains the same number of vertices in both classes. A partition into two classes can be represented by a coloring $\chi \colon V\rightarrow \{-1,+1\}$ . We call −1 and +1 *colors*. The color-classes $\chi ^{-1}(-1)$ and $\chi ^{-1}(+1)$ form the corresponding partition. For a hyperedge $E\in {\mathcal {E}}$ , set

$\chi (E):=\sum _{v\in E}\chi (v).$

The *discrepancy of ${\mathcal {H}}$ with respect to $\chi$* and the *discrepancy of ${\mathcal {H}}$* are defined by

$\operatorname {disc} ({\mathcal {H}},\chi ):=\;\max _{E\in {\mathcal {E}}}|\chi (E)|,$

$\operatorname {disc} ({\mathcal {H}}):=\min _{\chi :V\rightarrow \{-1,+1\}}\operatorname {disc} ({\mathcal {H}},\chi ).$

These notions as well as the term 'discrepancy' seem to have appeared for the first time in a paper of Beck. Earlier results on this problem include the famous lower bound on the discrepancy of arithmetic progressions by Roth and upper bounds for this problem and other results by Erdős and Spencer and Sárközi. At that time, discrepancy problems were called *quasi-Ramsey problems*.

## Examples

To get some intuition for this concept, let's have a look at a few examples.

- If all edges of ${\mathcal {H}}$ intersect trivially, i.e. $E_{1}\cap E_{2}=\varnothing$ for any two distinct edges $E_{1},E_{2}\in {\mathcal {E}}$ , then the discrepancy is zero, if all edges have even cardinality, and one, if there is an odd cardinality edge.
- The other extreme is marked by the *complete hypergraph* $(V,2^{V})$ . In this case the discrepancy is $\lceil {\frac {1}{2}}|V|\rceil$ . Any 2-coloring will have a color class of at least this size, and this set is also an edge. On the other hand, any coloring $\chi$ with color classes of size $\lceil {\frac {1}{2}}|V|\rceil$ and $\lfloor {\frac {1}{2}}|V|\rfloor$ proves that the discrepancy is not larger than $\lceil {\frac {1}{2}}|V|\rceil$ . It seems that the discrepancy reflects how chaotic the hyperedges of ${\mathcal {H}}$ intersect. Things are not that easy, however, as the following example shows.
- Set $n=4k$ , $k\in {\mathcal {N}}$ and ${\mathcal {H}}_{n}=([n],\{E\subseteq [n]\mid |E\cap [2k]|=|E\setminus [2k]|\})$ . In words, ${\mathcal {H}}_{n}$ is the hypergraph on 4*k* vertices {1,...,4*k*}, whose edges are all subsets that have the same number of elements in {1,...,2*k*} as in {2*k*+1,...,4*k*}. Now ${\mathcal {H}}_{n}$ has many (more than ${\binom {n/2}{n/4}}^{2}=\Theta ({\frac {1}{n}}2^{n})$ ) complicatedly intersecting edges. However, its discrepancy is zero, since we can color {1,...,2*k*} in one color and {2*k*+1,...,4*k*} in another color.

The last example shows that we cannot expect to determine the discrepancy by looking at a single parameter like the number of hyperedges. Still, the size of the hypergraph yields first upper bounds.

## General hypergraphs

**1.** For any hypergraph *${\mathcal {H}}$* with *n* vertices and *m* edges:

- $\operatorname {disc} ({\mathcal {H}})\leq {\sqrt {2n\ln(2m)}}.$

The proof is a simple application of the probabilistic method. Let $\chi :V\rightarrow \{-1,1\}$ be a random coloring, i.e. we have

$\Pr(\chi (v)=-1)=\Pr(\chi (v)=1)={\frac {1}{2}}$

independently for all $v\in V$ . Since $\chi (E)=\sum _{v\in E}\chi (v)$ is a sum of independent −1, 1 random variables. So we have $\Pr(|\chi (E)|>\lambda )<2\exp(-\lambda ^{2}/(2n))$ for all $E\subseteq V$ and $\lambda \geq 0$ . Taking $\lambda ={\sqrt {2n\ln(2m)}}$ gives

$\Pr(\operatorname {disc} ({\mathcal {H}},\chi )>\lambda )\leq \sum _{E\in {\mathcal {E}}}\Pr(|\chi (E)|>\lambda )<1.$

Since a random coloring with positive probability has discrepancy at most $\lambda$ , in particular, there are colorings that have discrepancy at most $\lambda$ . Hence $\operatorname {disc} ({\mathcal {H}})\leq \lambda .\ \Box$

**2.** For any hypergraph *${\mathcal {H}}$*with *n* vertices and *m* edges *such that $m\geq n$ :*

- *$\operatorname {disc} ({\mathcal {H}})\in O({\sqrt {n}}).$*

To prove this, a much more sophisticated approach using the entropy function was necessary. Of course this is particularly interesting for $m=O(n)$ . In the case $m=n$ , $\operatorname {disc} ({\mathcal {H}})\leq 6{\sqrt {n}}$ can be shown for n large enough. Therefore, this result is usually known to as 'Six Standard Deviations Suffice'. It is considered to be one of the milestones of discrepancy theory. The entropy method has seen numerous other applications, e.g. in the proof of the tight upper bound for the arithmetic progressions of Matoušek and Spencer or the upper bound in terms of the primal shatter function due to Matoušek.

## Hypergraphs of bounded degree

Better discrepancy bounds can be attained when the hypergraph has a *bounded degree*, that is, each vertex of ${\mathcal {H}}$ is contained in at most *t* edges, for some small *t*. In particular:

- Beck and Fiala proved that $\operatorname {disc} ({\mathcal {H}})<2t$ ; this is known as the Beck–Fiala theorem. They conjectured that $\operatorname {disc} ({\mathcal {H}})=O({\sqrt {t}})$ .
- Bednarchak and Helm and Helm improved the Beck-Fiala bound in tiny steps to $\operatorname {disc} ({\mathcal {H}})\leq 2t-3$ (for a slightly restricted situation, i.e. $t\geq 3$ ).
- Bukh improved this in 2016 to $2t-\log ^{*}t$ , where $\log ^{*}t$ denotes the iterated logarithm.
- A corollary of Beck's paper – the first time the notion of discrepancy explicitly appeared – shows $\operatorname {disc} ({\mathcal {H}})\leq C{\sqrt {t\log m}}\log n$ for some constant C.
- The latest improvement in this direction is due to Banaszczyk: $\operatorname {disc} ({\mathcal {H}})=O({\sqrt {t\log n}})$ .

## Special hypergraphs

Better bounds on the discrepancy are possible for hypergraphs with a special structure, such as:

- Discrepancy of permutations - when the vertices are the integers 1,...,*n*, and the hyperedges are all the intervals of some *m* given permutations on the integers.
- Geometric discrepancy - when the vertices are points in a Euclidean space, and the hyperedges are geometric objects, such as rectangles or half-spaces.

- Arithmetic progressions (Roth, Sárközy, Beck, Matoušek & Spencer)
- Six Standard Deviations Suffice (Spencer)

## Major open problems

- Komlós Conjecture

## Applications

- Numerical Integration: Monte Carlo methods in high dimensions.
- Computational Geometry: Divide and conquer algorithms.
- Image Processing: Halftoning

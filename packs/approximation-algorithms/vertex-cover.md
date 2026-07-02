---
title: "Vertex cover"
source: https://en.wikipedia.org/wiki/Vertex_cover
domain: approximation-algorithms
license: CC-BY-SA-4.0
tags: approximation algorithm, approximation ratio, polynomial-time approximation scheme, hardness of approximation
fetched: 2026-07-02
---

# Vertex cover

In graph theory, a **vertex cover** (sometimes **node cover**) of a graph is a set of vertices that includes at least one endpoint of every edge of the graph.

In computer science, the problem of finding a **minimum vertex cover** is a classical optimization problem. It is NP-hard, so it cannot be solved by a polynomial-time algorithm if P ≠ NP. Moreover, it is hard to approximate – it cannot be approximated up to a factor smaller than 2 if the unique games conjecture is true. On the other hand, it has several simple 2-factor approximations. It is a typical example of an NP-hard optimization problem that has an approximation algorithm. Its decision version, the **vertex cover problem**, was one of Karp's 21 NP-complete problems and is therefore a classical NP-complete problem in computational complexity theory. Furthermore, the vertex cover problem is fixed-parameter tractable and a central problem in parameterized complexity theory.

The minimum vertex cover problem can be formulated as a half-integral, linear program whose dual linear program is the maximum matching problem.

Vertex cover problems have been generalized to hypergraphs, see *Vertex cover in hypergraphs*.

## Definition

Formally, a vertex cover $V'$ of an undirected graph $G=(V,E)$ is a subset of V such that $(uv\in E)\Rightarrow (u\in V'\lor v\in V')$ , that is to say it is a set of vertices $V'$ where every edge has at least one endpoint in the vertex cover $V'$ . Such a set is said to *cover* the edges of G . The upper figure shows two examples of vertex covers, with some vertex cover $V'$ marked in red.

A *minimum vertex cover* is a vertex cover of smallest possible size. The vertex cover number $\tau$ is the size of a minimum vertex cover, i.e. $\tau =|V'|$ . The lower figure shows examples of minimum vertex covers in the previous graphs.

### Examples

- The set of all vertices is a vertex cover.
- The endpoints of any maximal matching form a vertex cover.
- The complete bipartite graph $K_{m,n}$ has a minimum vertex cover of size $\tau (K_{m,n})=\min\{\,m,n\,\}$ .

### Properties

- A set of vertices is a vertex cover if and only if its complement is an independent set.
- Consequently, the number of vertices of a graph is equal to its minimum vertex cover number plus the size of a maximum independent set.

## Computational problem

The **minimum vertex cover problem** is the optimization problem of finding a smallest vertex cover in a given graph.

INSTANCE: Graph

G

OUTPUT: Smallest number

k

such that

G

has a vertex cover of size

k

.

If the problem is stated as a decision problem, it is called the **vertex cover problem**:

INSTANCE: Graph

G

and positive integer

k

.

QUESTION: Does

G

have a vertex cover of size at most

k

?

They are equivalent under polynomial-time reduction by using binary search. The vertex cover problem is an NP-complete problem: it was one of Karp's 21 NP-complete problems. It is often used in computational complexity theory as a starting point for NP-hardness proofs.

### ILP formulation

Assume that every vertex has an associated cost of $c(v)\geq 0$ . The (weighted) minimum vertex cover problem can be formulated as the following integer linear program (ILP).

| minimize | $\textstyle \sum _{v\in V}c(v)x_{v}$ |   | (minimize the total cost) |   |
|---|---|---|---|---|
| subject to | $x_{u}+x_{v}\geq 1$ | for all $\{u,v\}\in E$ |   | (cover every edge of the graph), |
|   | $x_{v}\in \{0,1\}$ | for all $v\in V$ . |   | (every vertex is either in the vertex cover or not) |

This ILP belongs to the more general class of ILPs for covering problems. The integrality gap of this ILP is 2 , so its relaxation (allowing each variable to be in the interval from 0 to 1, rather than requiring the variables to be only 0 or 1) gives a factor- 2 approximation algorithm for the minimum vertex cover problem. Furthermore, the linear programming relaxation of that ILP is *half-integral*, that is, there exists an optimal solution for which each entry $x_{v}$ is either 0, 1/2, or 1. A 2-approximate vertex cover can be obtained from this fractional solution by selecting the subset of vertices whose variables are nonzero.

### Exact evaluation

The decision variant of the vertex cover problem is NP-complete, which means it is unlikely that there is an efficient algorithm to solve it exactly for arbitrary graphs. NP-completeness can be proven by reduction from 3-satisfiability or, as Karp did, by reduction from the clique problem. Vertex cover remains NP-complete even in cubic graphs and even in planar graphs of degree at most 3.

For bipartite graphs, the equivalence between vertex cover and maximum matching described by Kőnig's theorem allows the bipartite vertex cover problem to be solved in polynomial time.

For tree graphs, an algorithm finds a minimal vertex cover in polynomial time by finding the first leaf in the tree and adding its parent to the minimal vertex cover, then deleting the leaf and parent and all associated edges and continuing repeatedly until no edges remain in the tree.

#### Fixed-parameter tractability

An exhaustive search algorithm can solve the problem in time 2*k**n**O*(1), where *k* is the size of the vertex cover. Vertex cover is therefore fixed-parameter tractable, and if we are only interested in small *k*, we can solve the problem in polynomial time. One algorithmic technique that works here is called *bounded search tree algorithm*, and its idea is to repeatedly choose some vertex and recursively branch, with two cases at each step: place either the current vertex or all its neighbours into the vertex cover. The algorithm for solving vertex cover that achieves the best asymptotic dependence on the parameter runs in time $O(1.2738^{k}+(k\cdot n))$ . The klam value of this time bound (an estimate for the largest parameter value that could be solved in a reasonable amount of time) is approximately 190. That is, unless additional algorithmic improvements can be found, this algorithm is suitable only for instances whose vertex cover number is 190 or less. Under reasonable complexity-theoretic assumptions, namely the exponential time hypothesis, the running time cannot be improved to 2*o*(*k*), even when n is $O(k)$ .

However, for planar graphs, and more generally, for graphs excluding some fixed graph as a minor, a vertex cover of size *k* can be found in time *$2^{O({\sqrt {k}})}n^{O(1)}$*, i.e., the problem is subexponential fixed-parameter tractable. This algorithm is again optimal, in the sense that, under the exponential time hypothesis, no algorithm can solve vertex cover on planar graphs in time *$2^{o({\sqrt {k}})}n^{O(1)}$*.

### Approximate evaluation

One can find a factor-2 approximation by repeatedly taking *both* endpoints of an edge into the vertex cover, then removing them from the graph. Put otherwise, we find a maximal matching *M* with a greedy algorithm and construct a vertex cover *C* that consists of all endpoints of the edges in *M*. In the following figure, a maximal matching *M* is marked with red, and the vertex cover *C* is marked with blue.

The set *C* constructed this way is a vertex cover: suppose that an edge *e* is not covered by *C*; then *M* ∪ {*e*} is a matching and *e* ∉ *M*, which is a contradiction with the assumption that *M* is maximal. Furthermore, if *e* = {*u*, *v*} ∈ *M*, then any vertex cover – including an optimal vertex cover – must contain *u* or *v* (or both); otherwise the edge *e* is not covered. That is, an optimal cover contains at least *one* endpoint of each edge in *M*; in total, the set *C* is at most 2 times as large as the optimal vertex cover.

This simple algorithm was discovered independently by Fanica Gavril and Mihalis Yannakakis.

More involved techniques show that there are approximation algorithms with a slightly better approximation factor. For example, an approximation algorithm with an approximation factor of ${\textstyle 2-\Theta \left(1/{\sqrt {\log |V|}}\right)}$ is known. The problem can be approximated with an approximation factor $2/(1+\delta )$ in $\delta$ - dense graphs.

#### Inapproximability

No better constant-factor approximation algorithm than the above one is known. The minimum vertex cover problem is APX-complete, that is, it cannot be approximated arbitrarily well unless **P** = **NP**. Using techniques from the PCP theorem, Dinur and Safra proved in 2005 that minimum vertex cover cannot be approximated within a factor of 1.3606 for any sufficiently large vertex degree unless **P** = **NP**. Later, the factor was improved to ${\sqrt {2}}-\epsilon$ for any $\epsilon >0$ . Moreover, if the unique games conjecture is true then minimum vertex cover cannot be approximated within any constant factor better than 2.

Although finding the minimum-size vertex cover is equivalent to finding the maximum-size independent set, as described above, the two problems are not equivalent in an approximation-preserving way: The Independent Set problem has *no* constant-factor approximation unless **P** = **NP**.

#### Pseudocode

Approximation algorithm:

```mw
APPROXIMATION-VERTEX-COVER(G)
C = ∅
E'= G.E

while E' ≠ ∅:
    let (u, v) be an arbitrary edge of E'
    C = C ∪ {u, v}
    remove from E' every edge incident on either u or v

return C
```

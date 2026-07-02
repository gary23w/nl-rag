---
title: "Dominating set"
source: https://en.wikipedia.org/wiki/Dominating_set
domain: kernelization
license: CC-BY-SA-4.0
tags: kernelization technique, problem kernel, data reduction rule, vertex cover kernel
fetched: 2026-07-02
---

# Dominating set

In graph theory, a **dominating set** for a graph *G* is a subset *D* of its vertices, such that any vertex of *G* is in *D*, or has a neighbor in *D*. The **domination number** γ(*G*) is the number of vertices in a smallest dominating set for G.

The **dominating set problem** concerns testing whether γ(*G*) ≤ *K* for a given graph G and input K; it is a classical NP-complete decision problem in computational complexity theory. Therefore it is believed that there may be no efficient algorithm that can compute γ(*G*) for all graphs *G*. However, there are efficient approximation algorithms, as well as efficient exact algorithms for certain graph classes.

Dominating sets are of practical interest in several areas. In wireless networking, dominating sets are used to find efficient routes within ad-hoc mobile networks. They have also been used in document summarization, and in designing secure systems for electrical grids.

Dominating sets are closely related to independent sets: an independent set is also a dominating set if and only if it is a maximal independent set, so any maximal independent set in a graph is necessarily also a minimal dominating set.

## Formal definition

Given an undirected graph *G* = (*V*, *E*), a subset of vertices $D\subseteq V$ is called a **dominating set** if for every vertex $u\in V\setminus D$ , there is a vertex $v\in D$ such that $\{u,v\}\in E$ .

Every graph has at least one dominating set: if $D=V=$ the set of all vertices, then by definition *D* is a dominating set, since there is no vertex $u\in V\setminus D$ . A more interesting challenge is to find small dominating sets. The **domination number** of *G* is defined as: $\gamma (G):=\min\{|D|:D{\text{ is a dominating set of }}G\}$ .

## History

The domination problem was studied from the 1950s onwards, but the rate of research on domination significantly increased in the mid-1970s. In 1972, Richard Karp proved the set cover problem to be NP-complete. This had immediate implications for the dominating set problem, as there are straightforward vertex to set and edge to non-disjoint-intersection bijections between the two problems. This proved the dominating set problem to be NP-complete as well.

## Algorithms and computational complexity

The set cover problem is a well-known NP-hard problem – the decision version of set covering was one of Karp's 21 NP-complete problems. There exist a pair of polynomial-time L-reductions between the minimum dominating set problem and the set cover problem. These reductions (see below) show that an efficient algorithm for the minimum dominating set problem would provide an efficient algorithm for the set cover problem, and vice versa. Moreover, the reductions preserve the approximation ratio: for any α, a polynomial-time α-approximation algorithm for minimum dominating sets would provide a polynomial-time α-approximation algorithm for the set cover problem and vice versa. Both problems are in fact Log-APX-complete.

The approximability of set covering is also well understood: a logarithmic approximation factor can be found by using a simple greedy algorithm, and finding a sublogarithmic approximation factor is NP-hard. More specifically, the greedy algorithm provides a factor 1 + log|*V*| approximation of a minimum dominating set, and no polynomial time algorithm can achieve an approximation factor better than *c* log|*V*| for some *c* > 0 unless P = NP.

### L-reductions

The following two reductions show that the minimum dominating set problem and the set cover problem are equivalent under L-reductions: given an instance of one problem, we can construct an equivalent instance of the other problem.

#### From dominating set to set covering

Given a graph *G* = (*V*, *E*) with *V* = {1, 2, ..., *n*}, construct a set cover instance (*U*, *S*) as follows: the universe U is V, and the family of subsets is *S* = {*S*1, *S*2, ..., *S**n*} such that Sv consists of the vertex v and all vertices adjacent to v in G.

Now if D is a dominating set for G, then *C* = {*S**v* : *v* ∈ *D*} is a feasible solution of the set cover problem, with |*C*| = |*D*|. Conversely, if *C* = {*S**v* : *v* ∈ *D*} is a feasible solution of the set cover problem, then D is a dominating set for G, with |*D*| = |*C*|.

Hence the size of a minimum dominating set for G equals the size of a minimum set cover for (*U*, *S*). Furthermore, there is a simple algorithm that maps a dominating set to a set cover of the same size and vice versa. In particular, an efficient α-approximation algorithm for set covering provides an efficient α-approximation algorithm for minimum dominating sets.

For example, given the graph

G

shown on the right, we construct a set cover instance with the universe

U

= {1, 2, ..., 6}

and the subsets

S

1

= {1, 2, 5},

S

2

= {1, 2, 3, 5},

S

3

= {2, 3, 4, 6},

S

4

= {3, 4},

S

5

= {1, 2, 5, 6},

and

S

6

= {3, 5, 6}.

In this example,

D

= {3, 5}

is a dominating set for

G

– this corresponds to the set cover

C

= {

S

3

,

S

5

}.

For example, the vertex

4 ∈

V

is dominated by the vertex

3 ∈

D

, and the element

4 ∈

U

is contained in the set

S

3

∈

C

.

#### From set covering to dominating set

Let (*S*, *U*) be an instance of the set cover problem with the universe U and the family of subsets *S* = {*S**i* : *i* ∈ *I*}; we assume that U and the index set I are disjoint. Construct a graph *G* = (*V*, *E*) as follows: the set of vertices is *V* = *I* ∪ *U*, there is an edge {*i*, *j*} ∈ *E* between each pair *i*, *j* ∈ *I*, and there is also an edge {*i*, *u*} for each *i* ∈ *I* and *u* ∈ *S**i*. That is, G is a split graph: I is a clique and U is an independent set.

Now if *C* = {*S**i* : *i* ∈ *D*} is a feasible solution of the set cover problem for some subset *D* ⊆ *I*, then D is a dominating set for G, with |*D*| = |*C*|: First, for each *u* ∈ *U* there is an *i* ∈ *D* such that *u* ∈ *S**i*, and by construction, u and i are adjacent in G; hence u is dominated by i. Second, since D must be nonempty, each *i* ∈ *I* is adjacent to a vertex in D.

Conversely, let D be a dominating set for G. Then it is possible to construct another dominating set X such that |*X*| ≤ |*D*| and *X* ⊆ *I*: simply replace each *u* ∈ *D* ∩ *U* by a neighbour *i* ∈ *I* of u. Then *C* = {*S**i* : *i* ∈ *X*} is a feasible solution of the set cover problem, with |*C*| = |*X*| ≤ |*D*|.

The illustration on the right show the construction for

U

= {

a

,

b

,

c

,

d

,

e

},

I

= {1, 2, 3, 4},

S

1

= {

a

,

b

,

c

},

S

2

= {

a

,

b

},

S

3

= {

b

,

c

,

d

},

and

S

4

= {

c

,

d

,

e

}.

In this example,

C

= {

S

1

,

S

4

}

is a set cover; this corresponds to the dominating set

D

= {1, 4}.

D

= {

a

, 3, 4}

is another dominating set for the graph

G

. Given

D

, we can construct a dominating set

X

= {1, 3, 4}

which is not larger than

D

and which is a subset of

I

. The dominating set

X

corresponds to the set cover

C

= {

S

1

,

S

3

,

S

4

}.

### Special cases

If the graph has maximum degree Δ, then the greedy approximation algorithm finds an *O*(log Δ)-approximation of a minimum dominating set. Also, let dg be the cardinality of dominating set obtained using greedy approximation then following relation holds, $d_{g}\leq N+1-{\sqrt {2M+1}}$ , where N is number of nodes and M is number of edges in given undirected graph. For fixed Δ, this qualifies as a dominating set for APX membership; in fact, it is APX-complete.

The problem admits a polynomial-time approximation scheme (PTAS) for special cases such as unit disk graphs and planar graphs. A minimum dominating set can be found in linear time in series–parallel graphs.

### Exact algorithms

A minimum dominating set of an n-vertex graph can be found in time *O*(2*n**n*) by inspecting all vertex subsets. Fomin, Grandoni & Kratsch (2009) show how to find a minimum dominating set in time *O*(1.5137*n*) and exponential space, and in time *O*(1.5264*n*) and polynomial space. A faster algorithm, using *O*(1.5048*n*) time was found by van Rooij, Nederlof & van Dijk (2009), who also show that the number of minimum dominating sets can be computed in this time. The number of minimal dominating sets is at most 1.7159*n* and all such sets can be listed in time *O*(1.7159*n*).

### Parameterized complexity

Finding a dominating set of size k plays a central role in the theory of parameterized complexity. It is the most well-known problem complete for the class W[2] and used in many reductions to show intractability of other problems. In particular, the problem is not fixed-parameter tractable in the sense that no algorithm with running time *f*(*k*)*n*O(1) for any function f exists unless the W-hierarchy collapses to FPT=W[2].

On the other hand, if the input graph is planar, the problem remains NP-hard, but a fixed-parameter algorithm is known. In fact, the problem has a kernel of size linear in k, and running times that are exponential in √*k* and cubic in n may be obtained by applying dynamic programming to a branch-decomposition of the kernel. More generally, the dominating set problem and many variants of the problem are fixed-parameter tractable when parameterized by both the size of the dominating set and the size of the smallest forbidden complete bipartite subgraph; that is, the problem is FPT on biclique-free graphs, a very general class of sparse graphs that includes the planar graphs.

The complementary set to a dominating set, a nonblocker, can be found by a fixed-parameter algorithm on any graph.

## Variants

An **independent dominating set** is a dominating set that is also an independent set, or equivalently, a maximal independent set. The **independent domination number** $i(G)$ is the minimum size of an independent dominating set of G. Since the minimum is taken over fewer sets, $\gamma (G)\leq i(G)$ for all graphs G, and the inequality can be strict. Equality holds for claw-free graphs; since every line graph is claw-free, it follows that the minimum maximal matching and the minimum edge dominating set of any graph have the same size.

An **independence dominating set** of a graph G is a set that dominates every independent set of G . The **independence domination number** $i\gamma (G)$ is the maximum, over all independent sets A of G , of the smallest set dominating A . Dominating only independent sets requires potentially fewer vertices than dominating all vertices, so $i\gamma (G)\leq \gamma (G)$ for all graphs G , and the ratio $\gamma (G)/i\gamma (G)$ can be arbitrarily large.

A **connected dominating set** is a dominating set that is also connected. If S is a connected dominating set, one can form a spanning tree of G in which S forms the set of non-leaf vertices of the tree; conversely, if T is any spanning tree in a graph with more than two vertices, the non-leaf vertices of T form a connected dominating set. Therefore, finding minimum connected dominating sets is equivalent to finding spanning trees with the maximum possible number of leaves.

A **total dominating set** is a set of vertices such that all vertices in the graph, *including* the vertices in the dominating set themselves, have a neighbor in the dominating set. That is: for every vertex $u\in V$ , there is a vertex $v\in D$ such that $\{u,v\}\in E$ . Figure (c) above shows a dominating set that is a connected dominating set and a total dominating set; the examples in figures (a) and (b) are neither. In contrast to a simple dominating set, a total dominating set may not exist. For example, a graph with one or more vertices and no edges does not have a total dominating set. The **total domination number** $\gamma ^{\text{total}}(G)$ is defined as the minimum size of a total dominating set of *G*; obviously, $\gamma ^{\text{total}}(G)\geq \gamma (G)$ .

A **dominating edge-set** is a set of edges (vertex pairs) whose union is a dominating set; such a set may not exist (for example, a graph with one or more vertices and no edges does not have it). If it exists, then the union of all its edges is a total dominating set. Therefore, the smallest size of an edge-dominating set is at least $\gamma ^{\text{total}}(G)/2$ .

In contrast, an **edge-dominating set** is a set D of edges, such that every edge not in D is adjacent to at least one edge in D ; such a set always exists (for example, the set of all edges is an edge-dominating set).

A **k-dominating set** is a set of vertices such that each vertex not in the set has at least k neighbors in the set (a standard dominating set is a 1-dominating set). Similarly, a **k-tuple dominating set** is a set of vertices such that each vertex in the graph has at least k neighbors in the set (a total dominating set is a 1-tuple dominating set). An (1 + log *n*)-approximation of a minimum k-tuple dominating set can be found in polynomial time. Every graph admits a k-dominating set (for example, the set of all vertices); but only graphs with minimum degree *k* − 1 admit a k-tuple dominating set. However, even if the graph admits k-tuple dominating set, a minimum k-tuple dominating set can be nearly k times as large as a minimum k-dominating set for the same graph; An (1.7 + log Δ)-approximation of a minimum k-dominating set can be found in polynomial time as well.

A **fractional dominating set** is defined from a *fractional dominating function*, a function $f:V(G)\to [0,1]$ such that for every vertex $v\in V$ , the sum of f over the closed neighborhood $N[v]$ is at least 1. The **fractional domination number** $\gamma _{f}(G)$ is the minimum total weight (sum of all vertex values) of such a function, and satisfies $\gamma _{f}(G)\leq \gamma (G)$ . For a k -regular graph with n vertices ( $k\geq 1$ ), the fractional domination number equals $n/(k+1)$ .

A **star-dominating set** is a subset D of V such that, for every vertex v in V , the star of v (the set of edges adjacent to v ) intersects the star of some vertex in D . Clearly, if G has isolated vertices then it has no star-dominating sets (since the star of isolated vertices is empty). If G has no isolated vertices, then every dominating set is a star-dominating set and vice versa. The distinction between star-domination and usual domination is more substantial when their fractional variants are considered.

A **domatic partition** is a partition of the vertices into disjoint dominating sets. The domatic number is the maximum size of a domatic partition.

An **eternal dominating set** is a dynamic version of domination in which a vertex v in dominating set D is chosen and replaced with a neighbor u ( u is not in D ) such that the modified D is also a dominating set and this process can be repeated over any infinite sequence of choices of vertices  v .

An **efficient dominating set** (also called an e.d. set or independent perfect dominating set) is a dominating set with the additional property that every vertex in the graph is dominated by **exactly one** vertex in the set.

A **Roman dominating set** is defined through a *Roman dominating function*, which assigns to each vertex a value from $\{0,1,2\}$ such that every vertex assigned 0 is adjacent to at least one vertex assigned 2. The **Roman domination number** $\gamma _{R}(G)$ is the minimum sum of all vertex values over all such functions. The concept is inspired by a defensive strategy of the Roman Empire, where vertices represent cities and values represent stationed legions. For any graph G , $\gamma (G)\leq \gamma _{R}(G)\leq 2\gamma (G)$ , with the lower bound achieved only by the empty graph.

A **global dominating set** is a dominating set of a graph G that is also a dominating set of the complement graph ${\overline {G}}$ . The **global domination number** $\gamma _{g}(G)$ is the minimum cardinality of a global dominating set. Equivalently, a dominating set S is a global dominating set if and only if for each vertex $v\in V-S$ , there exists a vertex $u\in S$ such that u is not adjacent to v . By definition, $\gamma _{g}(G)=\gamma _{g}{\big (}{\overline {G}}{\big )}$ and $\gamma (G)\leq \gamma _{g}(G)$ . For a graph G with p vertices, $\gamma _{g}(G)=p$ if and only if $G=K_{p}$ or $G={\overline {K_{p}}}$ .

A **certified dominating set** is a dominating set in which every vertex in the set has either zero or at least two neighbours outside the set. The **certified domination number** $\gamma _{\text{cer}}(G)$ is the minimum size of a certified dominating set. Clearly, $\gamma _{\text{cer}}(G)\geq \gamma (G)$ , and equality holds whenever the graph has no *weak support vertex* (in particular, when $\delta (G)\geq 2$ ). For a connected graph, $\gamma _{\text{cer}}(G)\leq 2\gamma (G)$ .

A **paired dominating set** of a graph $G=(V,E)$ is a dominating set S of vertices such that the induced subgraph $G[S]$ contains at least one perfect matching. The **paired domination number** $\gamma _{p}(G)$ is the minimum cardinality of a paired dominating set of G . The concept models a situation in which guards are placed at vertices of a graph to dominate (protect) all vertices, with the additional constraint that each guard is assigned another adjacent guard as a backup.

Other variants include

- restrained dominating set,
- secure dominating set,
- triple connected dominating set,
- signed dominating set,
- minus dominating set, and
- friendly dominating set.

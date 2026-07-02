---
title: "Maximum flow problem"
source: https://en.wikipedia.org/wiki/Maximum_flow_problem
domain: graph-algorithms
license: CC-BY-SA-4.0
tags: graph algorithms, breadth-first search, shortest path, minimum spanning tree
fetched: 2026-07-02
---

# Maximum flow problem

In optimization theory, **maximum flow problems** involve finding a feasible flow through a flow network that obtains the maximum possible flow rate.

The maximum flow problem can be seen as a special case of more complex network flow problems, such as the circulation problem. The maximum value of an s-t flow (i.e., flow from source s to sink t) is equal to the minimum capacity of an s-t cut (i.e., cut severing s from t) in the network, as stated in the max-flow min-cut theorem.

## History

The maximum flow problem was first formulated in 1954 by T. E. Harris and F. S. Ross as a simplified model of Soviet railway traffic flow.

In 1955, Lester R. Ford, Jr. and Delbert R. Fulkerson created the first known algorithm, the Ford–Fulkerson algorithm. In their 1955 paper, Ford and Fulkerson wrote that the problem of Harris and Ross is formulated as follows (see p. 5):

> Consider a rail network connecting two cities by way of a number of intermediate cities, where each link of the network has a number assigned to it representing its capacity. Assuming a steady state condition, find a maximal flow from one given city to the other.

In their book *Flows in Networks*, in 1962, Ford and Fulkerson wrote:

> It was posed to the authors in the spring of 1955 by T. E. Harris, who, in conjunction with General F. S. Ross (Ret.), had formulated a simplified model of railway traffic flow, and pinpointed this particular problem as the central one suggested by the model [11].

where [11] refers to the 1955 secret report *Fundamentals of a Method for Evaluating Rail net Capacities* by Harris and Ross (see p. 5).

Over the years, various improved solutions to the maximum flow problem were discovered, notably the shortest augmenting path algorithm of Edmonds and Karp and independently Dinitz; the blocking flow algorithm of Dinitz; the push-relabel algorithm of Goldberg and Tarjan; and the binary blocking flow algorithm of Goldberg and Rao. The algorithms of Sherman and Kelner, Lee, Orecchia and Sidford, respectively, find an approximately optimal maximum flow but only work in undirected graphs.

In 2013 James B. Orlin published a paper describing an $O(|V||E|)$ algorithm.

In 2022 Li Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg, and Sushant Sachdeva published an almost-linear time algorithm running in $O(|E|^{1+o(1)})$ for the minimum-cost flow problem of which the maximum flow problem is a particular case. For the single-source shortest path (SSSP) problem with negative weights – another particular case of a minimum-cost flow problem – an algorithm running in almost-linear time has also been reported. Both algorithms were deemed best papers at the 2022 Symposium on Foundations of Computer Science.

## Definition

First we establish some notation:

- Let $N=(V,E)$ be a flow network with $s,t\in V$ being the source and the sink of N respectively.
- If g is a function on the edges of N then its value on $(u,v)\in E$ is denoted by $g_{uv}$ or $g(u,v).$

**Definition.** The **capacity** of an edge is the maximum amount of flow that can pass through an edge. Formally it is a map $c:E\to \mathbb {R} ^{+}.$

**Definition.** A **flow** is a map $f:E\to \mathbb {R}$ that satisfies the following:

- *Capacity constraint*. The flow of an edge cannot exceed its capacity, in other words: $f_{uv}\leq c_{uv}$ for all $(u,v)\in E.$
- *Conservation of flows.* The sum of the flows entering a node must equal the sum of the flows exiting that node, except for the source and the sink. Or:

$\forall v\in V\setminus \{s,t\}:\quad \sum _{u:(u,v)\in E,f_{uv}>0}f_{uv}=\sum _{u:(v,u)\in E,f_{vu}>0}f_{vu}.$

*Remark*. Flows are skew symmetric: $f_{uv}=-f_{vu}$ for all $(u,v)\in E.$

**Definition.** The **value of flow** is the amount of flow passing from the source to the sink. Formally for a flow $f:E\to \mathbb {R} ^{+}$ it is given by:

$|f|=\sum _{v:\ (s,v)\in E}f_{sv}=\sum _{u:\ (u,t)\in E}f_{ut}.$

**Definition.** The **maximum flow problem** is to route as much flow as possible from the source to the sink, in other words find the flow $f_{\textrm {max}}$ with maximum value.

Note that several maximum flows may exist, and if arbitrary real (or even arbitrary rational) values of flow are permitted (instead of just integers), there is either exactly one maximum flow, or infinitely many, since there are infinitely many linear combinations of the base maximum flows. In other words, if we send x units of flow on edge u in one maximum flow, and $y>x$ units of flow on u in another maximum flow, then for each $\Delta \in [0,y-x]$ we can send $x+\Delta$ units on u and route the flow on remaining edges accordingly, to obtain another maximum flow. If flow values can be any real or rational numbers, then there are infinitely many such $\Delta$ values for each pair $x,y$ .

## Algorithms

The following tables show the historical development of algorithms for solving the maximum flow problem. Many of the listed publications include similar tables comparing their results to earlier works.

### Strongly polynomial

A strongly-polynomial time algorithm has polynomial time bounds that depend only on the number of inputs, but do not depend on the magnitude of these numbers. Here, the inputs are the vertices (numbered below as V ) and edges (numbered as E ). The complexity of each algorithm is stated using big O notation.

| Method | Year | Complexity | Description |
|---|---|---|---|
| Edmonds–Karp algorithm | 1969 | $O(VE^{2})$ | A specialization of Ford–Fulkerson, finding augmenting paths with breadth-first search. |
| Dinic's algorithm | 1970 | $O(V^{2}E)$ (arbitrary weights) $O(\min\{V^{2/3},E^{1/2}\}E)$ (unit weights) | Repeated phases that build a "layered" subgraph of residual graph edges belonging to shortest paths, using breadth-first search, and then find a blocking flow (a maximum flow in this layered graph) in time $O(VE)$ per phase. The shortest path length increases in each phase so there are at most $V-1$ phases. |
| Karzanov's algorithm | 1974 | $O(V^{3})$ | A predecessor to the push-relabel algorithm using preflows (flow functions allowing excess at vertices) to find a blocking flow in each phase of Dinic's algorithm in time $O(V^{2})$ per phase. The first cubic-time flow algorithm. |
| Cherkassky's algorithm | 1977 | $O{\bigl (}V^{2}{\sqrt {E}}{\bigr )}$ | Combines the blocking flow methods of Dinic (within blocks of consecutive BFS layers) and Karzanov (to combine blocks). The first subcubic strongly polynomial time bound for sparse graphs. Remained best for some values of E until KRT 1988. |
| Malhotra, Kumar, and Maheshwari | 1978 | $O(V^{3})$ | Not an improvement in complexity over Karzanov, but a simplification. Finds blocking flows by repeatedly finding a "reference node" of the layered graph and a flow that saturates all its incoming or outgoing edges, in time proportional to the number of nodes plus the number of saturated edges. |
| Galil's algorithm | 1978 | $O(V^{5/3}E^{2/3})$ | Modifies Cherkasky's algorithm by replacing the method for finding flows within blocks of consecutive layers. |
| Galil, Naamad, and Shiloach | 1978 | $O{\bigl (}VE(\log V)^{2}{\bigr )}$ | Uses tree contraction on a breadth-first search forest of the layered graph to speed up blocking flows. The first of many $O(VE\operatorname {polylog} V)$ algorithms, still the best polynomial exponents for a strongly polynomial algorithm. |
| Blocking flow with link/cut trees. | 1981 | $O(VE\log V)$ | Introduces the link/cut tree data structure and uses it to find augmenting paths in layered networks in logarithmic amortized time per path. |
| Push–relabel algorithm with link/cut trees | 1986 | $O\left(VE\log {\frac {V^{2}}{E}}\right)$ | The push-relabel algorithm maintains a preflow, and a height function estimating residual distance to the sink. It modifies the preflow by pushing excess to lower-height vertices and increases the height function at vertices without residual edges to lower heights, until all excess returns to the source. Link/cut trees allow pushes along paths rather than one edge at a time. |
| Cheriyan and Hagerup | 1989 | randomized, $O{\bigl (}VE+V^{2}(\log V)^{2}{\bigr )}$ with high probability | Push-relabel on a subgraph to which one edge is added at a time, prioritizing pushes of high excess amounts, with randomly permuted adjacency lists |
| Alon | 1989 | $O(VE+V^{8/3}\log V)$ | Derandomization of Cheriyan and Hagerup |
| Cheriyan, Hagerup, and Mehlhorn | 1990 | $\displaystyle O\left({\frac {V^{3}}{\log V}}\right)$ | Uses Alon's derandomization of Cheriyan and Hagerup with ideas related to the Method of Four Russians to speed up the search for height-reducing edges on which to push excess. |
| King, Rao, and Tarjan | 1992 | $O(VE+V^{2+\varepsilon })$ for any $\varepsilon >0$ | Another derandomization of Cheriyan and Hagerup. Preliminary version of King, Rao, and Tarjan 1994 with weaker bounds. |
| Phillips and Westbrook | 1993 | $O(VE\log _{E/V}V+V(\log V)^{2+\varepsilon })$ for any $\varepsilon >0$ | Improved from King, Rao, and Tarjan 1992 using similar ideas. |
| King, Rao, and Tarjan | 1994 | $O\left(VE\log _{\frac {E}{V\log V}}V\right)$ | Improved from Phillips and Westbrook using similar ideas. |
| Orlin | 2013 | $O(VE)$ | Applies a pseudopolynomial algorithm of Goldberg and Rao to a compressed network, maintained using data structures for dynamic transitive closure. Takes time $O{\bigr (}VE+E^{31/16}(\log V)^{2}{\bigr )}$ , which simplifies to $O(VE)$ for $E=O(V^{16/15-\varepsilon })$ , while previous bounds simplify to $O(VE)$ for $E=\Omega (V^{1+\epsilon })$ . |
| Orlin and Gong | 2021 | $\displaystyle O\left({\frac {VE\log V}{\log \log V+\log {\tfrac {E}{V}}}}\right)$ | Based on a pseudopolynomial algorithm of Ahuja, Orlin, and Tarjan. Faster than King, Rao, and Tarjan and does not use link/cut trees, but not faster than Orlin + KRT. |

### Pseudo-polynomial and weakly polynomial

In parallel to the development of strongly-polynomial flow algorithms, there has been a long line of pseudo-polynomial and weakly polynomial time bounds, whose running time depends on the magnitude of the input capacities. Here, the value U refers to the largest edge capacity after rescaling all capacities to integer values. (If the network contains irrational capacities, this rescaling may not be possible and these algorithms may not produce exact solutions or may fail to converge even to an approximate solution.) The difference between pseudo-polynomial and weakly polynomial is that a pseudo-polynomial bound may be polynomial in U , but for a weakly polynomial bound it can be polynomial only in $\log U$ .

| Method | Year | Complexity | Description |
|---|---|---|---|
| Ford–Fulkerson algorithm | 1956 | $O(EU)$ | As long as there is an open path through the residual graph, send the minimum of the residual capacities on that path. |
| Binary blocking flow algorithm | 1998 | $O\left(E\cdot \min\{V^{2/3},E^{1/2}\}\cdot \log {\frac {V^{2}}{E}}\cdot \log U\right)$ |   |
| Kathuria-Liu-Sidford algorithm | 2020 | $E^{4/3+o(1)}U^{1/3}$ | Interior point methods and edge boosting using $\ell _{p}$ -norm flows. Builds on earlier algorithm of Madry, which achieved runtime ${\tilde {O}}(E^{10/7}U^{1/7})$ . |
| BLNPSSSW / BLLSSSW algorithm | 2020 | ${\tilde {O}}((E+V^{3/2})\log U)$ | Interior point methods and dynamic maintenance of electric flows with expander decompositions. |
| Gao-Liu-Peng algorithm | 2021 | ${\tilde {O}}(E^{{\frac {3}{2}}-{\frac {1}{328}}}\log U)$ | Gao, Liu, and Peng's algorithm revolves around dynamically maintaining the augmenting electrical flows at the core of the interior point method based algorithm from [Mądry JACM ‘16]. This entails designing data structures that, in limited settings, return edges with large electric energy in a graph undergoing resistance updates. |
| Chen, Kyng, Liu, Peng, Gutenberg and Sachdeva's algorithm | 2022 | $O(E^{1+o(1)}\log U)$ The exact complexity is not stated clearly in the paper, but appears to be $E\exp O(\log ^{7/8}E\log \log E)\log U$ | Chen, Kyng, Liu, Peng, Gutenberg and Sachdeva's algorithm solves maximum flow and minimum-cost flow in almost linear time by building the flow through a sequence of $E^{1+o(1)}$ approximate undirected minimum-ratio cycles, each of which is computed and processed in amortized $E^{o(1)}$ time using a dynamic data structure. |
| Bernstein, Blikstad, Saranurak, Tu | 2024 | $O(n^{2+o(1)}\log U)$ randomized algorithm when the edge capacities come from the set $\{1,\dots ,U\}$ | The algorithm is a variant of the push-relabel algorithm by introducing the *weighted* variant. The paper establishes a weight function on directed and acyclic graphs (DAG), and attempts to imitate it on general graphs using directed expander hierarchies, which induce a natural vertex ordering that produces the weight function similar to that of the DAG special case. The randomization aspect (and subsequently, the $n^{o(1)}$ factor) comes from the difficulty in applying directed expander hierarchies to the computation of *sparse cuts*, which do not allow for natural dynamic updating. |

## Integral flow theorem

The integral flow theorem states that

If each edge in a flow network has integral capacity, then there exists an integral maximal flow.

The claim is not only that the value of the flow is an integer, which follows directly from the max-flow min-cut theorem, but that the flow on *every edge* is integral. This is crucial for many combinatorial applications (see below), where the flow across an edge may encode whether the item corresponding to that edge is to be included in the set sought or not.

## Application

### Multi-source multi-sink maximum flow problem

Given a network $N=(V,E)$ with a set of sources $S=\{s_{1},\ldots ,s_{n}\}$ and a set of sinks $T=\{t_{1},\ldots ,t_{m}\}$ instead of only one source and one sink, we are to find the maximum flow across N . We can transform the multi-source multi-sink problem into a maximum flow problem by adding a *consolidated source* connecting to each vertex in S and a *consolidated sink*connected by each vertex in T (also known as *supersource* and *supersink*) with infinite capacity on each edge (See Fig. 4.1.1.).

### Maximum cardinality bipartite matching

Given a bipartite graph $G=(X\cup Y,E)$ , we are to find a maximum cardinality matching in G , that is a matching that contains the largest possible number of edges. This problem can be transformed into a maximum flow problem by constructing a network $N=(X\cup Y\cup \{s,t\},E')$ , where

1. $E'$ contains the edges in G directed from X to Y .
2. $(s,x)\in E'$ for each $x\in X$ and $(y,t)\in E'$ for each $y\in Y$ .
3. $c(e)=1$ for each $e\in E'$ (See Fig. 4.3.1).

Then the value of the maximum flow in N is equal to the size of the maximum matching in G , and a maximum cardinality matching can be found by taking those edges that have flow 1 in an integral max-flow.

### Minimum path cover in directed acyclic graph

Given a directed acyclic graph $G=(V,E)$ , we are to find the minimum number of vertex-disjoint paths to cover each vertex in V . We can construct a bipartite graph $G'=(V_{\textrm {out}}\cup V_{\textrm {in}},E')$ from G , where

1. $V_{\textrm {out}}=\{v_{\textrm {out}}\mid v\in V\land v{\text{ has outgoing edge(s)}}\}$
2. $V_{\textrm {in}}=\{v_{\textrm {in}}\mid v\in V\land v{\text{ has incoming edge(s)}}\}$
3. $E'=\{(u_{\textrm {out}},v_{\textrm {in}})\in V_{out}\times V_{in}\mid (u,v)\in E\}$ .

Then it can be shown that $G'$ has a matching M of size m if and only if G has a vertex-disjoint path cover C containing m edges and $n-m$ paths, where n is the number of vertices in G . Therefore, the problem can be solved by finding the maximum cardinality matching in $G'$ instead.

Assume we have found a matching M of $G'$ , and constructed the cover C from it. Intuitively, if two vertices $u_{\mathrm {out} },v_{\mathrm {in} }$ are matched in M , then the edge $(u,v)$ is contained in C . Clearly the number of edges in C is m . To see that C is vertex-disjoint, consider the following:

1. Each vertex $v_{\textrm {out}}$ in $G'$ can either be *non-matched* in M , in which case there are no edges leaving v in C ; or it can be *matched*, in which case there is exactly one edge leaving v in C . In either case, no more than one edge leaves any vertex v in C .
2. Similarly for each vertex $v_{\textrm {in}}$ in $G'$ – if it is matched, there is a single incoming edge into v in C ; otherwise v has no incoming edges in C .

Thus no vertex has two incoming or two outgoing edges in C , which means all paths in C are vertex-disjoint.

To show that the cover C has size $n-m$ , we start with an empty cover and build it incrementally. To add a vertex u to the cover, we can either add it to an existing path, or create a new path of length zero starting at that vertex. The former case is applicable whenever either $(u,v)\in E$ and some path in the cover starts at v , or $(v,u)\in E$ and some path ends at v . The latter case is always applicable. In the former case, the total number of edges in the cover is increased by 1 and the number of paths stays the same; in the latter case the number of paths is increased and the number of edges stays the same. It is now clear that after covering all n vertices, the sum of the number of paths and edges in the cover is n . Therefore, if the number of edges in the cover is m , the number of paths is $n-m$ .

### Maximum flow with vertex capacities

Let $N=(V,E)$ be a network. Suppose there is capacity at each node in addition to edge capacity, that is, a mapping $c:V\to \mathbb {R} ^{+},$ such that the flow f has to satisfy not only the capacity constraint and the conservation of flows, but also the vertex capacity constraint

$\sum _{i\in V}f_{iv}\leq c(v)\qquad \forall v\in V\backslash \{s,t\}.$

In other words, the amount of flow passing through a vertex cannot exceed its capacity. To find the maximum flow across N , we can transform the problem into the maximum flow problem in the original sense by expanding N . First, each $v\in V$ is replaced by $v_{\text{in}}$ and $v_{\text{out}}$ , where $v_{\text{in}}$ is connected by edges going into v and $v_{\text{out}}$ is connected to edges coming out from v , then assign capacity $c(v)$ to the edge connecting $v_{\text{in}}$ and $v_{\text{out}}$ (see Fig. 4.4.1). In this expanded network, the vertex capacity constraint is removed and therefore the problem can be treated as the original maximum flow problem.

### Maximum number of paths from s to t

Given a directed graph $G=(V,E)$ and two vertices s and t , we are to find the maximum number of paths from s to t . This problem has several variants:

1. The paths must be edge-disjoint. This problem can be transformed to a maximum flow problem by constructing a network $N=(V,E)$ from G , with s and t being the source and the sink of N respectively, and assigning each edge a capacity of 1 . In this network, the maximum flow is k iff there are k edge-disjoint paths.

2. The paths must be independent, i.e., vertex-disjoint (except for s and t ). We can construct a network $N=(V,E)$ from G with vertex capacities, where the capacities of all vertices and all edges are 1 . Then the value of the maximum flow is equal to the maximum number of independent paths from s to t .

3. In addition to the paths being edge-disjoint and/or vertex disjoint, the paths also have a length constraint: we count only paths whose length is exactly k , or at most k . Most variants of this problem are NP-complete, except for small values of k .

### Closure problem

A **closure** of a directed graph is a set of vertices *C*, such that no edges leave *C*. The **closure problem** is the task of finding the maximum-weight or minimum-weight closure in a vertex-weighted directed graph. It may be solved in polynomial time using a reduction to the maximum flow problem.

## Real world applications

### Baseball elimination

In the baseball elimination problem there are *n* teams competing in a league. At a specific stage of the league season, *w**i* is the number of wins and *r**i* is the number of games left to play for team *i* and *r*ij is the number of games left against team *j*. A team is eliminated if it has no chance to finish the season in the first place. The task of the baseball elimination problem is to determine which teams are eliminated at each point during the season. Schwartz proposed a method which reduces this problem to maximum network flow. In this method a network is created to determine whether team *k* is eliminated.

Let *G* = (*V*, *E*) be a network with *s*,*t* ∈ *V* being the source and the sink respectively. One adds a game node*ij* – which represents the number of plays between these two teams. We also add a team node for each team and connect each game node {*i*, *j*} with *i* < *j* to *V*, and connects each of them from *s* by an edge with capacity *r**ij* – which represents the number of plays between these two teams. We also add a team node for each team and connect each game node {*i*, *j*} with two team nodes *i* and *j* to ensure one of them wins. One does not need to restrict the flow value on these edges. Finally, edges are made from team node *i* to the sink node *t* and the capacity of *w**k* + *r**k* – *w**i* is set to prevent team *i* from winning more than *w**k* + *r**k*. Let *S* be the set of all teams participating in the league and let

$r(S-\{k\})=\sum _{i,j\in \{S-\{k\}\} \atop i<j}r_{ij}$

.

In this method it is claimed team *k* is not eliminated if and only if a flow value of size *r*(*S* − {*k*}) exists in network *G*. In the mentioned article it is proved that this flow value is the maximum flow value from *s* to *t*.

### Airline scheduling

In the airline industry a major problem is the scheduling of the flight crews. The airline scheduling problem can be considered as an application of extended maximum network flow. The input of this problem is a set of flights *F* which contains the information about where and when each flight departs and arrives. In one version of airline scheduling the goal is to produce a feasible schedule with at most *k* crews.

To solve this problem one uses a variation of the circulation problem called bounded circulation which is the generalization of network flow problems, with the added constraint of a lower bound on edge flows.

Let *G* = (*V*, *E*) be a network with *s*,*t* ∈ *V* as the source and the sink nodes. For the source and destination of every flight *i*, one adds two nodes to *V*, node *s**i* as the source and node *d**i* as the destination node of flight *i*. One also adds the following edges to *E*:

1. An edge with capacity [0, 1] between *s* and each *s**i*.
2. An edge with capacity [0, 1] between each *d**i* and *t*.
3. An edge with capacity [1, 1] between each pair of *s**i* and *d**i*.
4. An edge with capacity [0, 1] between each *d**i* and *s**j*, if source *s**j* is reachable with a reasonable amount of time and cost from the destination of flight *i*.
5. An edge with capacity [0, ∞] between *s* and *t*.

In the mentioned method, it is claimed and proved that finding a flow value of *k* in *G* between *s* and *t* is equal to finding a feasible schedule for flight set *F* with at most *k* crews.

Another version of airline scheduling is finding the minimum needed crews to perform all the flights. To find an answer to this problem, a bipartite graph *G'* = (*A* ∪ *B*, *E*) is created where each flight has a copy in set *A* and set *B*. If the same plane can perform flight *j* after flight *i*, *i*∈*A* is connected to *j*∈*B*. A matching in G' induces a schedule for *F* and obviously maximum bipartite matching in this graph produces an airline schedule with minimum number of crews. As it is mentioned in the Application part of this article, the maximum cardinality bipartite matching is an application of maximum flow problem.

### Circulation–demand problem

There are some factories that produce goods and some villages where the goods have to be delivered. They are connected by a networks of roads with each road having a capacity c for maximum goods that can flow through it. The problem is to find if there is a circulation that satisfies the demand. This problem can be transformed into a maximum-flow problem.

1. Add a source node s and add edges from it to every factory node fi with capacity pi where pi is the production rate of factory fi.
2. Add a sink node t and add edges from all villages vi to t with capacity di where di is the demand rate of village vi.

Let *G* = (*V*, *E*) be this new network. There exists a circulation that satisfies the demand if and only if :

Maximum flow value(

G

)

$=\sum _{i\in v}d_{i}$

.

If there exists a circulation, looking at the max-flow solution would give the answer as to how much goods have to be sent on a particular road for satisfying the demands.

The problem can be extended by adding a lower bound on the flow on some edges.

### Image segmentation

In their book, Kleinberg and Tardos present an algorithm for segmenting an image. They present an algorithm to find the background and the foreground in an image. More precisely, the algorithm takes a bitmap as an input modelled as follows: *ai* ≥ 0 is the likelihood that pixel *i* belongs to the foreground, *bi* ≥ 0 in the likelihood that pixel *i* belongs to the background, and *pij* is the penalty if two adjacent pixels *i* and *j* are placed one in the foreground and the other in the background. The goal is to find a partition (*A*, *B*) of the set of pixels that maximize the following quantity

$q(A,B)=\sum _{i\in A}a_{i}+\sum _{i\in B}b_{i}-\sum _{\begin{matrix}i,j{\text{ adjacent}}\\|A\cap \{i,j\}|=1\end{matrix}}p_{ij}$

,

Indeed, for pixels in *A* (considered as the foreground), we gain *ai*; for all pixels in *B* (considered as the background), we gain *bi*. On the border, between two adjacent pixels *i* and *j*, we loose *pij*. It is equivalent to minimize the quantity

$q'(A,B)=\sum _{i\in A}b_{i}+\sum _{i\in B}a_{i}+\sum _{\begin{matrix}i,j{\text{ adjacent}}\\|A\cap \{i,j\}|=1\end{matrix}}p_{ij}$

because

$q(A,B)=\sum _{i\in A\cup B}a_{i}+\sum _{i\in A\cup B}b_{i}-q'(A,B).$

We now construct the network whose nodes are the pixel, plus a source and a sink, see Figure on the right. We connect the source to pixel *i* by an edge of weight *ai*. We connect the pixel *i* to the sink by an edge of weight *bi*. We connect pixel *i* to pixel *j* with weight *pij*. Now, it remains to compute a minimum cut in that network (or equivalently a maximum flow). The last figure shows a minimum cut.

## Extensions

1. In the **minimum-cost flow problem**, each edge (*u*,v) also has a **cost-coefficient** *auv* in addition to its capacity. If the flow through the edge is *fuv*, then the total cost is *auvfuv.* It is required to find a flow of a given size *d*, with the smallest cost. In most variants, the cost-coefficients may be either positive or negative. There are various polynomial-time algorithms for this problem.

2. The maximum-flow problem can be augmented by **disjunctive constraints**: a *negative disjunctive constraint* says that a certain pair of edges cannot simultaneously have a nonzero flow; a *positive disjunctive constraints* says that, in a certain pair of edges, at least one must have a nonzero flow. With negative constraints, the problem becomes strongly NP-hard even for simple networks. With positive constraints, the problem is polynomial if fractional flows are allowed, but may be strongly NP-hard when the flows must be integral.

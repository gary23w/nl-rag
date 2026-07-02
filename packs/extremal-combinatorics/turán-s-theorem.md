---
title: "Turán's theorem"
source: https://en.wikipedia.org/wiki/Tur%C3%A1n's_theorem
domain: extremal-combinatorics
license: CC-BY-SA-4.0
tags: extremal combinatorics, probabilistic method, dilworth's theorem, turan theorem
fetched: 2026-07-02
---

# Turán's theorem

In graph theory, **Turán's theorem** bounds the number of edges that can be included in an undirected graph that does not have a complete subgraph of a given size. It is one of the central results of extremal graph theory, an area studying the largest or smallest graphs with given properties, and is a special case of the forbidden subgraph problem on the maximum number of edges in a graph that does not have a given subgraph.

An example of an n -vertex graph that does not contain any $(r+1)$ -vertex clique $K_{r+1}$ may be formed by partitioning the set of n vertices into r parts of equal or nearly equal size, and connecting two vertices by an edge whenever they belong to two different parts. The resulting graph is the Turán graph $T(n,r)$ . Turán's theorem states that the Turán graph has the largest number of edges among all *K**r*+1-free n-vertex graphs.

Turán's theorem, and the Turán graphs giving its extreme case, were first described and studied by Hungarian mathematician Pál Turán in 1941. The special case of the theorem for triangle-free graphs is known as **Mantel's theorem**; it was stated in 1907 by Willem Mantel, a Dutch mathematician.

## Statement

Turán's theorem states that every graph G with n vertices that does not contain $K_{r+1}$ as a subgraph has at most as many edges as the Turán graph $T(n,r)$ . For a fixed value of r , this graph has $\left(1-{\frac {1}{r}}+o(1)\right){\frac {n^{2}}{2}}$ edges, using little-o notation. Intuitively, this means that as n gets larger, the fraction of edges included in $T(n,r)$ gets closer and closer to $1-{\frac {1}{r}}$ . Many of the following proofs only give the upper bound of $\left(1-{\frac {1}{r}}\right){\frac {n^{2}}{2}}$ .

## Proofs

Aigner & Ziegler (2018) list five different proofs of Turán's theorem. Many of the proofs involve reducing to the case where the graph is a complete multipartite graph, and showing that the number of edges is maximized when there are r parts of size as close as possible to equal.

### Induction

This was Turán's original proof. Take a $K_{r+1}$ -free graph on n vertices with the maximal number of edges. Find a $K_{r}$ (which exists by maximality), and partition the vertices into the set A of the r vertices in the $K_{r}$ and the set B of the $n-r$ other vertices.

Now, one can bound edges above as follows:

- There are exactly ${\binom {r}{2}}$ edges within A .
- There are at most $(r-1)|B|=(r-1)(n-r)$ edges between A and B , since no vertex in B can connect to all of A .
- The number of edges within B is at most the number of edges of $T(n-r,r)$ by the inductive hypothesis.

Adding these bounds gives the result.

### Maximal Degree Vertex

This proof is due to Paul Erdős. Take the vertex v of largest degree. Consider the set A of vertices not adjacent to v and the set B of vertices adjacent to v .

Now, delete all edges within A and draw all edges between A and B . This increases the number of edges by our maximality assumption and keeps the graph $K_{r+1}$ -free. Now, B is $K_{r}$ -free, so the same argument can be repeated on B .

Repeating this argument eventually produces a graph in the same form as a Turán graph, which is a collection of independent sets, with edges between each two vertices from different independent sets. A simple calculation shows that the number of edges of this graph is maximized when all independent set sizes are as close to equal as possible.

### Complete Multipartite Optimization

This proof, as well as the Zykov Symmetrization proof, involve reducing to the case where the graph is a complete multipartite graph, and showing that the number of edges is maximized when there are r independent sets of size as close as possible to equal. This step can be done as follows:

Let $S_{1},S_{2},\ldots ,S_{r}$ be the independent sets of the multipartite graph. Since two vertices have an edge between them if and only if they are not in the same independent set, the number of edges is

$\sum _{i\neq j}\left|S_{i}\right|\left|S_{j}\right|={\frac {1}{2}}\left(n^{2}-\sum _{i}\left|S_{i}\right|^{2}\right),$

where the left hand side follows from direct counting, and the right hand side follows from complementary counting. To show the $\left(1-{\frac {1}{r}}\right){\frac {n^{2}}{2}}$ bound, applying the Cauchy–Schwarz inequality to the ${\textstyle \sum \limits _{i}\left|S_{i}\right|^{2}}$ term on the right hand side suffices, since ${\textstyle \sum \limits _{i}\left|S_{i}\right|=n}$ .

To prove the Turán Graph is optimal, one can argue that no two $S_{i}$ differ by more than one in size. In particular, supposing that we have $\left|S_{i}\right|\geq \left|S_{j}\right|+2$ for some $i\neq j$ , moving one vertex from $S_{i}$ to $S_{j}$ (and adjusting edges accordingly) would increase the value of the sum. This can be seen by examining the changes to either side of the above expression for the number of edges, or by noting that the degree of the moved vertex increases.

### Lagrangian

This proof is due to Motzkin & Straus (1965). They begin by considering a $K_{r+1}$ free graph with vertices labelled $1,2,\ldots ,n$ , and considering maximizing the function $f(x_{1},x_{2},\ldots ,x_{n})=\sum _{i,j\ {\text{adjacent}}}x_{i}x_{j}$ over all nonnegative $x_{1},x_{2},\ldots ,x_{n}$ with sum 1 . This function is known as the Lagrangian of the graph and its edges.

The idea behind their proof is that if $x_{i},x_{j}$ are both nonzero while $i,j$ are not adjacent in the graph, the function $f(x_{1},\ldots ,x_{i}-t,\ldots ,x_{j}+t,\ldots ,x_{n})$ is linear in t . Hence, one can either replace $(x_{i},x_{j})$ with either $(x_{i}+x_{j},0)$ or $(0,x_{i}+x_{j})$ without decreasing the value of the function. Hence, there is a point with at most r nonzero variables where the function is maximized.

Now, the Cauchy–Schwarz inequality gives that the maximal value is at most ${\frac {1}{2}}\left(1-{\frac {1}{r}}\right)$ . Plugging in $x_{i}={\frac {1}{n}}$ for all i gives that the maximal value is at least ${\frac {|E|}{n^{2}}}$ , giving the desired bound.

### Probabilistic Method

The key claim in this proof was independently found by Caro and Wei. This proof is due to Noga Alon and Joel Spencer, from their book *The Probabilistic Method*. The proof shows that every graph with degrees $d_{1},d_{2},\ldots ,d_{n}$ has an independent set of size at least $S={\frac {1}{d_{1}+1}}+{\frac {1}{d_{2}+1}}+\cdots +{\frac {1}{d_{n}+1}}.$ The proof attempts to find such an independent set as follows:

- Consider a random permutation of the vertices of a $K_{r+1}$ -free graph
- Select every vertex that is adjacent to none of the vertices before it.

A vertex of degree d is included in this with probability ${\frac {1}{d+1}}$ , so this process gives an average of S vertices in the chosen set.

Applying this fact to the complement graph and bounding the size of the chosen set using the Cauchy–Schwarz inequality proves Turán's theorem. See Method of conditional probabilities § Turán's theorem for more.

### Zykov Symmetrization

Aigner and Ziegler call the final one of their five proofs "the most beautiful of them all". Its origins are unclear, but the approach is often referred to as Zykov Symmetrization as it was used in Zykov's proof of a generalization of Turán's Theorem . This proof goes by taking a $K_{r+1}$ -free graph, and applying steps to make it more similar to the Turán Graph while increasing edge count.

In particular, given a $K_{r+1}$ -free graph, the following steps are applied:

- If $u,v$ are non-adjacent vertices and u has a higher degree than v , replace v with a copy of u . Repeat this until all non-adjacent vertices have the same degree.
- If $u,v,w$ are vertices with $u,v$ and $v,w$ non-adjacent but $u,w$ adjacent, then replace both u and w with copies of v .

All of these steps keep the graph $K_{r+1}$ free while increasing the number of edges.

Now, non-adjacency forms an equivalence relation. The equivalence classes give that any maximal graph the same form as a Turán graph. As in the maximal degree vertex proof, a simple calculation shows that the number of edges is maximized when all independent set sizes are as close to equal as possible.

## Mantel's theorem

The special case of Turán's theorem for $r=2$ is Mantel's theorem: The maximum number of edges in an n -vertex triangle-free graph is $\lfloor n^{2}/4\rfloor .$ In other words, one must delete slightly over half of the edges in $K_{n}$ to obtain a triangle-free graph.

A strengthened form of Mantel's theorem states that any Hamiltonian graph with at least $n^{2}/4$ edges must either be the complete bipartite graph $K_{n/2,n/2}$ or it must be pancyclic: not only does it contain a triangle, it must also contain cycles of all other possible lengths up to the number of vertices in the graph.

Another strengthening of Mantel's theorem states that the edges of every n -vertex graph may be covered by at most $\lfloor n^{2}/4\rfloor$ cliques which are either edges or triangles. As a corollary, the graph's intersection number (the minimum number of cliques needed to cover all its edges) is at most $\lfloor n^{2}/4\rfloor$ .

## Hypergraphs and the Turán density

There is no analogous of Turán's theorem for k -uniform hypergraphs. In fact, in Turán's original paper, he asked for the maximum number of hyperedges an n -vertex 3 -uniform hypergraph can have without containing the complete 3 -uniform hypergraph on 4 vertices, $K_{4}^{(3)}$ . This maximum number of hyperedges is known as the *extremal number*. More precisely and more generally, for a hypergraph F , the extremal number of F for n vertices, ex $(n,F)$ , is the maximum number of hyperedges an n -vertex k -uniform hypergraph can have without containing a copy of F . To obtain a cleaner parameter, the Turán density of F is defined by the following limit $\pi (F)=\lim _{n\to \infty }{\frac {{\text{ex}}(n,F)}{\binom {n}{k}}}.$ It is easy to see that ${\text{ex}}(n,F)/{\tbinom {n}{k}}$ is non increasing sequence, and therefore, the limit above always converges. In this language, an (approximate) answer to Turán's question above, about $K_{4}^{(3)}$ , corresponds to determining the Turán density $\pi (K_{4}^{(3)})$ . One can also check that $\pi (K_{t}^{(k)})=1-\Theta _{k}(t^{k-1})$ . An upper bound for this can be obtained from the probabilistic method or supersaturation, while a lower bound is given by the complement of the disjoint union of $\lfloor (t-1)/(k-1)\rfloor$ cliques.

## Generalizations

### Other Forbidden Subgraphs

Turán's theorem shows that the largest number of edges in a $K_{r+1}$ -free graph is $\left(1-{\frac {1}{r}}+o(1)\right){\frac {n^{2}}{2}}$ . The Erdős–Stone theorem finds the number of edges up to a $o(n^{2})$ error in all other graphs:

> (Erdős–Stone) Suppose H is a graph with chromatic number $\chi (H)$ . The largest possible number of edges in a graph where H does not appear as a subgraph is $\left(1-{\frac {1}{\chi (H)-1}}+o(1)\right){\frac {n^{2}}{2}}$ where the $o(1)$ constant only depends on H .

One can see that the Turán graph $T(n,\chi (H)-1)$ cannot contain any copies of H , so the Turán graph establishes the lower bound. As a $K_{r+1}$ has chromatic number $r+1$ , Turán's theorem is the special case in which H is a $K_{r+1}$ .

The general question of how many edges can be included in a graph without a copy of some H is the forbidden subgraph problem.

### Maximizing Other Quantities

Another natural extension of Turán's theorem is the following question: if a graph has no $K_{r+1}$ s, how many copies of $K_{a}$ can it have? Turán's theorem is the case where $a=2$ . Zykov's Theorem answers this question:

> (Zykov's Theorem) The graph on n vertices with no $K_{r+1}$ s and the largest possible number of $K_{a}$ s is the Turán graph $T(n,r)$

This was first shown by Zykov (1949) using Zykov Symmetrization. Since the Turán Graph contains r parts with size around ${\frac {n}{r}}$ , the number of $K_{a}$ s in $T(n,r)$ is around ${\binom {r}{a}}\left({\frac {n}{r}}\right)^{a}$ . A paper by Alon and Shikhelman in 2016 gives the following generalization, which is similar to the Erdos-Stone generalization of Turán's theorem:

> (Alon-Shikhelman, 2016) Let H be a graph with chromatic number $\chi (H)>a$ . The largest possible number of $K_{a}$ s in a graph with no copy of H is $(1+o(1)){\binom {\chi (H)-1}{a}}\left({\frac {n}{\chi (H)-1}}\right)^{a}.$

As in Erdős–Stone, the Turán graph $T(n,\chi (H)-1)$ attains the desired number of copies of $K_{a}$ .

### Edge-Clique region

Turan's theorem states that if a graph has edge homomorphism density strictly above $1-{\frac {1}{r-1}}$ , it has a nonzero number of $K_{r}$ s. One could ask the far more general question: if you are given the edge density of a graph, what can you say about the density of $K_{r}$ s?

An issue with answering this question is that for a given density, there may be some bound not attained by any graph, but approached by some infinite sequence of graphs. To deal with this, weighted graphs or graphons are often considered. In particular, graphons contain the limit of any infinite sequence of graphs.

For a given edge density d , the construction for the largest $K_{r}$ density is as follows:

> Take a number of vertices N approaching infinity. Pick a set of ${\sqrt {d}}N$ of the vertices, and connect two vertices if and only if they are in the chosen set.

This gives a $K_{r}$ density of $d^{k/2}.$ The construction for the smallest $K_{r}$ density is as follows:

> Take a number of vertices approaching infinity. Let t be the integer such that $1-{\frac {1}{t-1}}<d\leq 1-{\frac {1}{t}}$ . Take a t -partite graph where all parts but the unique smallest part have the same size, and sizes of the parts are chosen such that the total edge density is d .

For $d\leq 1-{\frac {1}{r-1}}$ , this gives a graph that is $(r-1)$ -partite and hence gives no $K_{r}$ s.

The lower bound was proven by Razborov (2008) for the case of triangles, and was later generalized to all cliques by Reiher (2016). The upper bound is a consequence of the Kruskal–Katona theorem .

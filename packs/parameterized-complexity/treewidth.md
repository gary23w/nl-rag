---
title: "Treewidth"
source: https://en.wikipedia.org/wiki/Treewidth
domain: parameterized-complexity
license: CC-BY-SA-4.0
tags: parameterized complexity, fixed parameter tractable, w hierarchy, treewidth parameter
fetched: 2026-07-02
---

# Treewidth

In graph theory, the **treewidth** of an undirected graph is an integer number which specifies, informally, how far the graph is from being a tree. The smallest treewidth is 1; the graphs with treewidth 1 are exactly the trees and the forests. An example of graphs with treewidth at most 2 are the series–parallel graphs. The maximal graphs with treewidth exactly k are called *k-trees*, and the graphs with treewidth at most k are called *partial k-trees*. Many other well-studied graph families also have bounded treewidth.

Treewidth may be formally defined in several equivalent ways: in terms of the size of the largest vertex set in a tree decomposition of the graph, in terms of the size of the largest clique in a chordal completion of the graph, in terms of the maximum order of a haven describing a strategy for a pursuit–evasion game on the graph, or in terms of the maximum order of a bramble, a collection of connected subgraphs that all touch each other.

Treewidth is commonly used as a parameter in the parameterized complexity analysis of graph algorithms. Many algorithms that are NP-hard for general graphs, become easier when the treewidth is bounded by a constant.

The concept of treewidth was originally introduced by Umberto Bertelè and Francesco Brioschi (1972) under the name of *dimension*. It was later rediscovered by Rudolf Halin (1976), based on properties that it shares with a different graph parameter, the Hadwiger number. Later it was again rediscovered by Neil Robertson and Paul Seymour (1984) and has since been studied by many other authors.

## Definition

A tree decomposition of a graph $G=(V,E)$ is a tree T in which each node is associated with a subset of vertices called a "bag". (The term *node* is used to refer to a vertex of T to avoid confusion with vertices of G ). The bags $X_{1},\dots X_{t}$ must satisfy the following properties:

1. Each graph vertex is contained in at least one bag: $\textstyle \bigcup _{i}X_{i}=V$
2. If bags $X_{i}$ and $X_{j}$ both contain a vertex v , then all bags $X_{k}$ associated with nodes in the (unique) path of T between $X_{i}$ and $X_{j}$ also contain v as well. Equivalently, the bags containing vertex v are associated with a connected subtree of T .
3. For every edge $(v,w)$ in the graph, there is at least one bag $X_{i}$ that contains both v and w . That is, vertices are adjacent in the graph only when their corresponding subtrees have a node in common. (However, two vertices may belong to a bag without being adjacent to each other.)

The *width* of a tree decomposition is the size of its largest bag $X_{i}$ minus one. The **treewidth** $\operatorname {tw} (G)$ of a graph G is the minimum width among all possible tree decompositions of G . In this definition, the size of the largest set is diminished by one in order to make the treewidth of a tree equal to one.

Equivalently, the treewidth of G is one less than the size of the largest clique in the chordal graph containing G with the smallest clique number. A chordal graph with this clique size may be obtained by adding to G an edge between every two vertices for which at least one bag contains both vertices.

Treewidth may also be characterized in terms of havens, functions describing an evasion strategy for a certain pursuit–evasion game defined on a graph. A graph G has treewidth k if and only if it has a haven of order $k+1$ but of no higher order, where a haven of order $k+1$ is a function $\beta$ that maps each set X of at most k vertices in G into one of the connected components of $G\setminus X$ and that obeys the monotonicity property that $\beta (Y)\subseteq \beta (X)$ whenever $X\subset Y$ .

A similar characterization can also be made using brambles, families of connected subgraphs that all touch each other (meaning either that they share a vertex or are connected by an edge). The order of a bramble is the smallest hitting set for the family of subgraphs, and the treewidth of a graph is one less than the maximum order of a bramble.

## Examples

Every complete graph $K_{n}$ has treewidth $n-1$ . This is most easily seen using the definition of treewidth in terms of chordal graphs: the complete graph is already chordal, and adding more edges cannot reduce the size of its largest clique.

A connected graph with at least two vertices has treewidth 1 if and only if it is a tree. A tree has treewidth one by the same reasoning as for complete graphs (namely, it is chordal, and has maximum clique size two). Conversely, if a graph has a cycle, then every chordal completion of the graph includes at least one triangle consisting of three consecutive vertices of the cycle, from which it follows that its treewidth is at least two.

## Bounded treewidth

### Graph families with bounded treewidth

For any fixed constant k , the graphs of treewidth at most k are called the partial k -trees. Other families of graphs with bounded treewidth include the cactus graphs, pseudoforests, series–parallel graphs, outerplanar graphs, Halin graphs, and Apollonian networks. The control-flow graphs arising in the compilation of structured programs also have bounded treewidth, which allows certain tasks such as register allocation to be performed efficiently on them.

The planar graphs do not have bounded treewidth, because the $n\times n$ grid graph is a planar graph with treewidth exactly n . Therefore, if F is a minor-closed graph family with bounded treewidth, it cannot include all planar graphs. Conversely, if some planar graph cannot occur as a minor for graphs in family F , then there is a constant k such that all graphs in F have treewidth at most k . That is, the following three conditions are equivalent to each other:

1. F is a minor-closed family of bounded-treewidth graphs;
2. One of the finitely many forbidden minors characterizing F is planar;
3. F is a minor-closed graph family that does not include all planar graphs.

### Forbidden minors

For every finite value of k , the graphs of treewidth at most k may be characterized by a finite set of forbidden minors. (That is, any graph of treewidth greater than k includes one of the graphs in the set as a minor.) Each of these sets of forbidden minors includes at least one planar graph.

- For $k=1$ , the unique forbidden minor is a 3-vertex cycle graph.
- For $k=2$ , the unique forbidden minor is the 4-vertex complete graph $K_{4}$ .
- For $k=3$ , there are four forbidden minors: $K_{5}$ , the graph of the octahedron, the pentagonal prism graph, and the Wagner graph. Of these, the two polyhedral graphs are planar.

For larger values of k , the number of forbidden minors grows at least as quickly as an exponential function of ${\sqrt {k}}$ . However, known upper bounds on the size and number of forbidden minors are much higher than this lower bound.

## Algorithms

### Computing the treewidth

It is ${\mathsf {NP}}$ -complete to determine whether a given graph G has treewidth at most a given variable k . However, when k is any fixed constant, the graphs with treewidth k can be recognized, and a width k tree decomposition constructed for them, in linear time. The time dependence of this algorithm on k is exponential.

Due to the roles the treewidth plays in an enormous number of fields, different practical and theoretical algorithms computing the treewidth of a graph were developed. Depending on the application on hand, one can prefer better approximation ratio, or better dependence in the running time from the size of the input or the treewidth. The table below provides an overview of some of the treewidth algorithms. Here k is the treewidth and n is the number of vertices of an input graph G . Each of the algorithms outputs in time $f(k)\cdot g(n)$ a decomposition of width given in the Approximation column. For example, the algorithm of Bodlaender (1996) in time $2^{O(k^{3})}\cdot n$ either constructs a tree decomposition of the input graph G of width at most k or reports that the treewidth of G is more than k . Similarly, the algorithm of Bodlaender et al. (2016) in time $2^{O(k)}\cdot n$ either constructs a tree decomposition of the input graph G of width at most $5k+4$ or reports that the treewidth of G is more than k . Korhonen (2021) improved the width of the decomposition to $2k+1$ in the same running time.

| Approximation | *f*(*k*) | *g*(*n*) | reference |
|---|---|---|---|
| exact | 1 | $O(n^{k+2})$ | Arnborg, Corneil & Proskurowski (1987) |
| $4k+3$ | $O(3^{3k})$ | $O(n^{2})$ | Robertson & Seymour (1995) |
| $8k+7$ | $2^{O(k\log n)}$ | $O(n\log ^{2}n)$ | Lagergren (1996) |
| $5k+4$ (or $7k+6$ ) | $2^{O(k\log n)}$ | $O(n\log n)$ | Reed (1992) |
| exact | $2^{O(k^{3})}$ | $O(n)$ | Bodlaender (1996) |
| $O\left(k\cdot {\sqrt {\log k}}\right)$ | 1 | $n^{O(1)}$ | Feige, Hajiaghayi & Lee (2008) |
| $4.5k+4$ | $2^{3k}$ | $O(n^{2})$ | Amir (2010) |
| ${\tfrac {11}{3}}k+4$ | $2^{3.6982k}$ | $O(n^{3}\log ^{4}n)$ | Amir (2010) |
| exact | 1 | $O(1.7347^{n})$ | Fomin, Todinca & Villanger (2015) |
| $3k+2$ | $2^{O(k)}$ | $O(n\log n)$ | Bodlaender et al. (2016) |
| $5k+4$ | $2^{O(k)}$ | $O(n)$ | Bodlaender et al. (2016) |
| $k^{2}$ | $k^{7}$ | $O(n\log n)$ | Fomin et al. (2018) |
| $5k+4$ | $2^{8.765k}$ | $O(n\log n)$ | Belbasi & Fürer (2021a) |
| $2k+1$ | $2^{O(k)}$ | $O(n)$ | Korhonen (2021) |
| $5k+4$ | $2^{6.755k}$ | $O(n\log n)$ | Belbasi & Fürer (2021b) |
| exact | $2^{O(k^{2})}$ | $O(n^{4})$ | Korhonen & Lokshtanov (2023) |
| $(1+\varepsilon )k$ | $k^{O(k/\varepsilon )}$ | $O(n^{4})$ | Korhonen & Lokshtanov (2023) |

Unsolved problem in mathematics

Can the treewidth of

planar graphs

be computed in polynomial time?

More unsolved problems in mathematics

It is not known whether determining the treewidth of planar graphs is NP-complete, or whether their treewidth can be computed in polynomial time.

In practice, an algorithm of Shoikhet & Geiger (1997) can determine the treewidth of graphs with up to 100 vertices and treewidth up to 11, finding a chordal completion of these graphs with the optimal treewidth.

For larger graphs, one can use search-based techniques such as branch and bound search to compute the treewidth. These algorithms are anytime in that when stopped early, they will output an upper bound on the treewidth. An algorithm of this type was proposed in 2004 by Vibhav Gogate and Rina Dechter. To provide a lower bound on treewidth for the branches of this search, they construct a graph minor by repeatedly contracting an edge between a minimum degree vertex and one of its neighbors, until just one vertex remains. The maximum of the minimum degree over these constructed minors is guaranteed to be a lower bound on the treewidth of the graph. Alex Dow and Rich Korf further improved this algorithm using best-first search.

### Solving other problems on graphs of small treewidth

At the beginning of the 1970s, it was observed that a large class of combinatorial optimization problems defined on graphs could be efficiently solved by non serial dynamic programming as long as the graph had a bounded *dimension*, a parameter shown to be equivalent to treewidth by Bodlaender (1998). Later, several authors independently observed at the end of the 1980s that many algorithmic problems that are NP-complete for arbitrary graphs may be solved efficiently by dynamic programming for graphs of bounded treewidth, using the tree-decompositions of these graphs.

As an example, the problem of coloring a graph of treewidth k may be solved by using a dynamic programming algorithm on a tree decomposition of the graph. For each bag $X_{i}$ of the tree decomposition, and each partition of the vertices of $X_{i}$ into color classes, the algorithm determines whether that coloring is valid and can be extended to all descendant nodes in the tree decomposition, by combining information of a similar type computed and stored at those nodes. The resulting algorithm finds an optimal coloring of an n -vertex graph in time $O(k^{k+O(1)}n)$ , a time bound that makes this problem fixed-parameter tractable.

### Courcelle's theorem

For a large class of problems, there is a linear time algorithm to solve a problem from the class if a tree-decomposition with constant bounded treewidth is provided. Specifically, Courcelle's theorem states that if a graph problem can be expressed in the logic of graphs using monadic second order logic, then it can be solved in linear time on graphs with bounded treewidth. Monadic second order logic is a language to describe graph properties that uses the following constructions:

- Logic operations, such as $\wedge ,\vee ,\neg ,\Rightarrow$
- Membership tests, such as $e\in E$ , $v\in V$
- Quantifications over vertices, edges, sets of vertices, and/or sets of edges, such as $\forall v\in V$ , $\exists e\in E$ , $\exists I\subset V$ , $\forall F\subset E$
- Vertex–edge incidence tests ( u is an endpoint of e ), and some extensions that allow for things such as optimization.

Consider for example the 3-coloring problem for graphs. For a graph $G=(V,E)$ , this problem asks if it is possible to assign each vertex $v\in V$ one of three colors such that no two adjacent vertices are assigned the same color. This problem can be expressed in monadic second order logic as $\exists W_{1}\subseteq V\ \exists W_{2}\subseteq V\ \exists W_{3}\subseteq V\ \left({\begin{aligned}&\forall v\in V\ (v\in W_{1}\vee v\in W_{2}\vee v\in W_{3})\wedge {}\\&\operatorname {independent} (W_{1})\wedge {}\\&\operatorname {independent} (W_{2})\wedge {}\\&\operatorname {independent} (W_{3})\\\end{aligned}}\right),$ where $W_{1}$ , $W_{2}$ , $W_{3}$ represent the subsets of vertices having each of the three colors, and where the subexpressions $\operatorname {independent} (W_{i})$ are defined to mean $\operatorname {independent} (W_{i})\equiv \forall e\in E\ \exists v\in V\ (\operatorname {endpoint} (v,e)\wedge \neg v\in W_{i}).$ (It is not necessary to include in this formula the requirement that the sets $W_{i}$ be disjoint.) Therefore, by Courcelle's results, the 3-coloring problem can be solved in linear time for a graph given a tree-decomposition of bounded constant treewidth.

### Pathwidth

The pathwidth of a graph has a very similar definition to treewidth via tree decompositions, but is restricted to tree decompositions in which the underlying tree of the decomposition is a path graph. Alternatively, the pathwidth may be defined from interval graphs analogously to the definition of treewidth from chordal graphs. As a consequence, the pathwidth of a graph is always at least as large as its treewidth, but it can only be larger by a logarithmic factor. Another parameter, the graph bandwidth, has an analogous definition from proper interval graphs, and is at least as large as the pathwidth. Other related parameters include the tree-depth, a number that is bounded for a minor-closed graph family if and only if the family excludes a path, and the degeneracy, a measure of the sparsity of a graph that is at most equal to its treewidth.

### Grid minor size

Because the treewidth of an $n\times n$ grid graph is n , the treewidth of a graph G is always greater than or equal to the size of the largest square grid minor of G . In the other direction, the *grid minor theorem* by Robertson and Seymour shows that there exists an unbounded function f such that the largest square grid minor of a graph of treewidth k has size at least $f(k)$ . The best bounds known on f are that f must be at least $\Omega (k^{d})$ for some fixed constant $d>0$ , and at most $O\left({\sqrt {r/\log r}}\right).$

(For the $\Omega$ notation in the lower bound, see big O notation.) Tighter bounds are known for restricted graph families, leading to efficient algorithms for many graph optimization problems on those families through the theory of bidimensionality. Halin's grid theorem provides an analogue of the relation between treewidth and grid minor size for infinite graphs.

### Diameter and local treewidth

A family F of graphs closed under taking subgraphs is said to have **bounded local treewidth**, or the **diameter-treewidth property**, if the treewidth of the graphs in the family is upper bounded by a function of their diameter. If the class is also assumed to be closed under taking minors, then F has bounded local treewidth if and only if one of the forbidden minors for F is an apex graph. The original proofs of this result showed that treewidth in an apex-minor-free graph family grows at most doubly exponentially as a function of diameter; later this was reduced to singly exponential and finally to a linear bound. Bounded local treewidth is closely related to the algorithmic theory of bidimensionality, and every graph property definable in first order logic can be decided for an apex-minor-free graph family in an amount of time that is only slightly superlinear.

It is also possible for a class of graphs that is not closed under minors to have bounded local treewidth. In particular this is trivially true for a class of bounded degree graphs, as bounded diameter subgraphs have bounded size. Another example is given by 1-planar graphs, graphs that can be drawn in the plane with one crossing per edge, and more generally for the graphs that can be drawn on a surface of bounded genus with a bounded number of crossings per edge. As with minor-closed graph families of bounded local treewidth, this property has pointed the way to efficient approximation algorithms for these graphs.

### Hadwiger number and S-functions

Halin (1976) defines a class of graph parameters that he calls S-functions, which include the treewidth. These functions from graphs to integers are required to be zero on graphs with no edges, to be minor-monotone (a function f is referred to as "minor-monotone" if, whenever H is a minor of G , one has $f(H)\leq f(G)$ ), to increase by one when a new vertex is added that is adjacent to all previous vertices, and to take the larger value from the two subgraphs on either side of a clique separator. The set of all such functions forms a complete lattice under the operations of elementwise minimization and maximization. The top element in this lattice is the treewidth, and the bottom element is the Hadwiger number, the size of the largest complete minor in the given graph.

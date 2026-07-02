---
title: "Graph minor"
source: https://en.wikipedia.org/wiki/Graph_minor
domain: graph-minors
license: CC-BY-SA-4.0
tags: graph minor, robertson-seymour theorem, tree decomposition, forbidden minor
fetched: 2026-07-02
---

# Graph minor

In graph theory, an undirected graph H is called a **minor** of the undirected graph G if H can be formed from G by deleting edges and vertices and by contracting edges.

The theory of graph minors began with Wagner's theorem that a graph is planar if and only if its minors include neither the complete graph *K*5 nor the complete bipartite graph *K*3,3. The Robertson–Seymour theorem implies that an analogous forbidden minor characterization exists for every property of graphs that is preserved by deletions and edge contractions. For every fixed graph H, it is possible to test whether H is a minor of an input graph G in polynomial time; together with the forbidden minor characterization this implies that every graph property preserved by deletions and contractions may be recognized in polynomial time.

Other results and conjectures involving graph minors include the graph structure theorem, according to which the graphs that do not have H as a minor may be formed by gluing together simpler pieces, and Hadwiger's conjecture relating the inability to color a graph to the existence of a large complete graph as a minor of it. Important variants of graph minors include the topological minors and immersion minors.

## Definitions

An edge contraction is an operation that removes an edge from a graph while simultaneously merging the two vertices it used to connect. An undirected graph H is a minor of another undirected graph G if a graph isomorphic to H can be obtained from G by contracting some edges, deleting some edges, and deleting some isolated vertices. The order in which a sequence of such contractions and deletions is performed on G does not affect the resulting graph H.

Graph minors are often studied in the more general context of matroid minors. In this context, it is common to assume that all graphs are connected, with self-loops and multiple edges allowed (that is, they are multigraphs rather than simple graphs); the contraction of a loop and the deletion of a cut-edge are forbidden operations. This point of view has the advantage that edge deletions leave the rank of a graph unchanged, and edge contractions always reduce the rank by one.

In other contexts (such as with the study of pseudoforests) it makes more sense to allow the deletion of a cut-edge, and to allow disconnected graphs, but to forbid multigraphs. In this variation of graph minor theory, a graph is always simplified after any edge contraction to eliminate its self-loops and multiple edges.

A function f is referred to as "minor-monotone" if, whenever H is a minor of G, one has *f*(*H*) ≤ *f*(*G*).

## Example

In the following example, graph *H* is a minor of graph *G*:

H. (graph H)

G. (graph G)

The following diagram illustrates this. First construct a subgraph of *G* by deleting the dashed edges (and the resulting isolated vertex), and then contract the gray edge (merging the two vertices it connects):

(transformation from G to H)

## Major results and conjectures

It is straightforward to verify that the graph minor relation forms a partial order on the isomorphism classes of finite undirected graphs: it is transitive (a minor of a minor of G is a minor of G itself), and G and H can only be minors of each other if they are isomorphic because any nontrivial minor operation removes edges or vertices. A deep result by Neil Robertson and Paul Seymour states that this partial order is actually a well-quasi-ordering: if an infinite list (*G*1, *G*2, …) of finite graphs is given, then there always exist two indices *i* < *j* such that Gi is a minor of Gj. Another equivalent way of stating this is that any set of graphs can have only a finite number of minimal elements under the minor ordering. This result proved a conjecture formerly known as Wagner's conjecture, after Klaus Wagner; Wagner had conjectured it long earlier, but only published it in 1970.

In the course of their proof, Seymour and Robertson also prove the graph structure theorem in which they determine, for any fixed graph H, the rough structure of any graph that does not have H as a minor. The statement of the theorem is itself long and involved, but in short it establishes that such a graph must have the structure of a clique-sum of smaller graphs that are modified in small ways from graphs embedded on surfaces of bounded genus. Thus, their theory establishes fundamental connections between graph minors and topological embeddings of graphs.

For any graph H, the simple H-minor-free graphs must be sparse, which means that the number of edges is less than some constant multiple of the number of vertices. More specifically, if H has h vertices, then a simple n-vertex simple H-minor-free graph can have at most $\scriptstyle O(nh{\sqrt {\log h}})$ edges, and some Kh-minor-free graphs have at least this many edges. Thus, if H has h vertices, then H-minor-free graphs have average degree $\scriptstyle O(h{\sqrt {\log h}})$ and furthermore degeneracy $\scriptstyle O(h{\sqrt {\log h}})$ . Additionally, the H-minor-free graphs have a separator theorem similar to the planar separator theorem for planar graphs: for any fixed H, and any n-vertex H-minor-free graph G, it is possible to find a subset of $\scriptstyle O({\sqrt {n}})$ vertices whose removal splits G into two (possibly disconnected) subgraphs with at most 2*n*⁄3 vertices per subgraph. Even stronger, for any fixed H, H-minor-free graphs have treewidth $\scriptstyle O({\sqrt {n}})$ .

The Hadwiger conjecture in graph theory proposes that if a graph G does not contain a minor isomorphic to the complete graph on k vertices, then G has a proper coloring with *k* – 1 colors. The case *k* = 5 is a restatement of the four color theorem. The Hadwiger conjecture has been proven for *k* ≤ 6, but is unknown in the general case. Bollobás, Catlin & Erdős (1980) call it "one of the deepest unsolved problems in graph theory." Another result relating the four-color theorem to graph minors is the snark theorem announced by Robertson, Sanders, Seymour, and Thomas, a strengthening of the four-color theorem conjectured by W. T. Tutte and stating that any bridgeless 3-regular graph that requires four colors in an edge coloring must have the Petersen graph as a minor.

## Minor-closed graph families

Many families of graphs have the property that every minor of a graph in *F* is also in *F*; such a class is said to be *minor-closed*. For instance, in any planar graph, or any embedding of a graph on a fixed topological surface, neither the removal of edges nor the contraction of edges can increase the genus of the embedding; therefore, planar graphs and the graphs embeddable on any fixed surface form minor-closed families.

If *F* is a minor-closed family, then (because of the well-quasi-ordering property of minors) among the graphs that do not belong to *F* there is a finite set *X* of minor-minimal graphs. These graphs are forbidden minors for *F*: a graph belongs to *F* if and only if it does not contain as a minor any graph in *X*. That is, every minor-closed family *F* can be characterized as the family of *X*-minor-free graphs for some finite set *X* of forbidden minors. The best-known example of a characterization of this type is Wagner's theorem characterizing the planar graphs as the graphs having neither K5 nor K3,3 as minors.

In some cases, the properties of the graphs in a minor-closed family may be closely connected to the properties of their excluded minors. For example a minor-closed graph family *F* has bounded pathwidth if and only if its forbidden minors include a forest, *F* has bounded tree-depth if and only if its forbidden minors include a disjoint union of path graphs, *F* has bounded treewidth if and only if its forbidden minors include a planar graph, and *F* has bounded local treewidth (a functional relationship between diameter and treewidth) if and only if its forbidden minors include an apex graph (a graph that can be made planar by the removal of a single vertex). If *H* can be drawn in the plane with only a single crossing (that is, it has crossing number one) then the *H*-minor-free graphs have a simplified structure theorem in which they are formed as clique-sums of planar graphs and graphs of bounded treewidth. For instance, both *K*5 and *K*3,3 have crossing number one, and as Wagner showed the *K*5-free graphs are exactly the 3-clique-sums of planar graphs and the eight-vertex Wagner graph, while the *K*3,3-free graphs are exactly the 2-clique-sums of planar graphs and *K*5.

## Variations

### Topological minors

A graph *H* is called a **topological minor** of a graph *G* if a subdivision of *H* is isomorphic to a subgraph of *G*. Every topological minor is also a minor. The converse however is not true in general (for instance the complete graph *K*5 in the Petersen graph is a minor but not a topological one), but holds for graph with maximum degree not greater than three.

The topological minor relation is not a well-quasi-ordering on the set of finite graphs and hence the result of Robertson and Seymour does not apply to topological minors. However it is straightforward to construct finite forbidden topological minor characterizations from finite forbidden minor characterizations by replacing every branch set with *k* outgoing edges by every tree on *k* leaves that has down degree at least two.

### Induced minors

A graph *H* is called an **induced minor** of a graph *G* if it can be obtained from an induced subgraph of *G* by contracting edges. Otherwise, *G* is said to be *H*-induced minor-free. Induced minors have been used to study string graphs, the intersection graphs of plane curves, because every induced minor of a string graph is another string graph. The string graphs provide an example of a family of graphs with infinitely many obstacles in the induced minor order, where an obstacle is a graph that is not in the family but for which all proper induced minors are in the family.

### Immersion minor

A graph operation called *lifting* is central in a concept called *immersions*. The *lifting* is an operation on adjacent edges. Given three vertices *v*, *u*, and *w*, where *(v,u)* and *(u,w)* are edges in the graph, the lifting of *vuw*, or equivalent of *(v,u), (u,w)* is the operation that deletes the two edges *(v,u)* and *(u,w)* and adds the edge *(v,w)*. In the case where *(v,w)* already was present, *v* and *w* will now be connected by more than one edge, and hence this operation is intrinsically a multi-graph operation.

In the case where a graph *H* can be obtained from a graph *G* by a sequence of lifting operations (on *G*) and then finding an isomorphic subgraph, we say that *H* is an immersion minor of *G*. There is yet another way of defining immersion minors, which is equivalent to the lifting operation. We say that *H* is an immersion minor of *G* if there exists an injective mapping from vertices in *H* to vertices in *G* where the images of adjacent elements of *H* are connected in *G* by edge-disjoint paths.

The immersion minor relation is a well-quasi-ordering on the set of finite graphs and hence the result of Robertson and Seymour applies to immersion minors. This furthermore means that every immersion minor-closed family is characterized by a finite family of forbidden immersion minors.

In graph drawing, immersion minors arise as the planarizations of non-planar graphs: from a drawing of a graph in the plane, with crossings, one can form an immersion minor by replacing each crossing point by a new vertex, and in the process also subdividing each crossed edge into a path. This allows drawing methods for planar graphs to be extended to non-planar graphs.

### Shallow minors

A shallow minor of a graph *G* is a minor in which the edges of *G* that were contracted to form the minor form a collection of disjoint subgraphs with low diameter. Shallow minors interpolate between the theories of graph minors and subgraphs, in that shallow minors with high depth coincide with the usual type of graph minor, while the shallow minors with depth zero are exactly the subgraphs. They also allow the theory of graph minors to be extended to classes of graphs such as the 1-planar graphs that are not closed under taking minors.

### Parity conditions

An alternative and equivalent definition of a graph minor is that *H* is a minor of *G* whenever the vertices of *H* can be represented by a collection of vertex-disjoint subtrees of *G*, such that if two vertices are adjacent in *H*, there exists an edge with its endpoints in the corresponding two trees in *G*. An odd minor restricts this definition by adding parity conditions to these subtrees. If *H* is represented by a collection of subtrees of *G* as above, then *H* is an odd minor of *G* whenever it is possible to assign two colors to the vertices of *G* in such a way that each edge of *G* within a subtree is properly colored (its endpoints have different colors) and each edge of *G* that represents an adjacency between two subtrees is monochromatic (both its endpoints are the same color). Unlike for the usual kind of graph minors, graphs with forbidden odd minors are not necessarily sparse. The Hadwiger conjecture, that *k*-chromatic graphs necessarily contain *k*-vertex complete graphs as minors, has also been studied from the point of view of odd minors.

A different parity-based extension of the notion of graph minors is the concept of a bipartite minor, which produces a bipartite graph whenever the starting graph is bipartite. A graph *H* is a bipartite minor of another graph *G* whenever *H* can be obtained from *G* by deleting vertices, deleting edges, and collapsing pairs of vertices that are at distance two from each other along a peripheral cycle of the graph. A form of Wagner's theorem applies for bipartite minors: A bipartite graph *G* is a planar graph if and only if it does not have the utility graph *K*3,3 as a bipartite minor.

## Algorithms

The problem of deciding whether a graph *G* contains *H* as a minor is NP-complete in general; for instance, if *H* is a cycle graph with the same number of vertices as *G*, then *H* is a minor of *G* if and only if *G* contains a Hamiltonian cycle. However, when *G* is part of the input but *H* is fixed, it can be solved in polynomial time. More specifically, the running time for testing whether *H* is a minor of *G* in this case is *O*(*n*3), where *n* is the number of vertices in *G* and the big O notation hides a constant that depends superexponentially on *H*; since the original Graph Minors result, this algorithm has been improved to *O*(*n*2) time. Thus, by applying the polynomial time algorithm for testing whether a given graph contains any of the forbidden minors, it is theoretically possible to recognize the members of any minor-closed family in polynomial time. This result is not used in practice since the hidden constant is so huge (needing three layers of Knuth's up-arrow notation to express) as to rule out any application, making it a galactic algorithm. Furthermore, in order to apply this result constructively, it is necessary to know what the forbidden minors of the graph family are. In some cases, the forbidden minors are known, or can be computed.

In the case where *H* is a fixed planar graph, then we can test in linear time in an input graph *G* whether *H* is a minor of *G*. In cases where *H* is not fixed, faster algorithms are known in the case where *G* is planar.

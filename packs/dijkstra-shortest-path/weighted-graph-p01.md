---
title: "Glossary of graph theory (part 1/2)"
source: https://en.wikipedia.org/wiki/Weighted_graph
domain: dijkstra-shortest-path
license: CC-BY-SA-4.0
tags: dijkstra algorithm, shortest path, graph traversal, priority queue
fetched: 2026-07-02
part: 1/2
---

# Glossary of graph theory

(Redirected from

Weighted graph

)

This is a **glossary of graph theory**. Graph theory is the study of graphs, systems of nodes or vertices connected in pairs by lines or edges.


## Symbols

***Square brackets [ ]***

G

[

S

]

is the

induced subgraph

of a graph

G

for vertex subset

S

.

***Prime symbol '***

The

prime symbol

is often used to modify notation for graph invariants so that it applies to the

line graph

instead of the given graph. For instance,

α

(

G

)

is the independence number of a graph;

α

′(

G

)

is the matching number of the graph, which equals the independence number of its line graph. Similarly,

χ

(

G

)

is the chromatic number of a graph;

χ

′(

G

)

is the chromatic index of the graph, which equals the chromatic number of its line graph.


## A

***absorbing***

An absorbing set

A

of a directed graph

G

is a set of vertices such that for any vertex

$v\in G\setminus A$

, there is an edge from

v

towards a vertex of

A

.

***achromatic***

The

achromatic number

of a graph is the maximum number of colors in a complete coloring.

***acyclic***

1.

A graph is acyclic if it has no cycles. An undirected acyclic graph is the same thing as a

forest

. An acyclic directed graph, which is a digraph without directed cycles, is often called a

directed acyclic graph

, especially in computer science.

2.

An

acyclic coloring

of an undirected graph is a proper coloring in which every two color classes induce a forest.

***adjacency matrix***

The

adjacency matrix

of a graph is a matrix whose rows and columns are both indexed by vertices of the graph, with a one in the cell for row

i

and column

j

when vertices

i

and

j

are adjacent, and a zero otherwise.

***adjacent***

1.

The relation between two vertices that are both endpoints of the same edge.

2.

The relation between two distinct edges that share an end vertex.

****α****

For a graph

G

,

α

(

G

)

(using the Greek letter alpha) is its independence number (see

independent

), and

α

′(

G

)

is its matching number (see

matching

).

***alternating***

In a graph with a matching, an alternating path is a path whose edges alternate between matched and unmatched edges. An alternating cycle is, similarly, a cycle whose edges alternate between matched and unmatched edges. An augmenting path is an alternating path that starts and ends at unsaturated vertices. A larger matching can be found as the

symmetric difference

of the matching and the augmenting path; a matching is maximum if and only if it has no augmenting path.

***antichain***

In a

directed acyclic graph

, a subset

S

of vertices that are pairwise incomparable, i.e., for any

$x\leq y$

in

S

, there is no directed path from

x

to

y

or from

y

to

x

. Inspired by the notion of

antichains

in

partially ordered sets

.

***anti-edge***

Synonym for

non-edge

, a pair of non-adjacent vertices.

***anti-triangle***

A three-vertex independent set, the complement of a triangle.

***apex***

1.

An

apex graph

is a graph in which one vertex can be removed, leaving a

planar

subgraph. The removed vertex is called the apex. A

k

-apex graph is a graph that can be made planar by the removal of

k

vertices.

2.

Synonym for

universal vertex

, a vertex adjacent to all other vertices.

***arborescence***

Synonym for a rooted and directed tree; see

tree

.

***arc***

See

edge

.

***arrow***

An

ordered pair

of

vertices

, such as an

edge

in a

directed graph

. An arrow

(

x

,

y

)

has a

tail

x

, a

head

y

, and a

direction

from

x

to

y

;

y

is said to be the

direct successor

to

x

and

x

the

direct predecessor

to

y

. The arrow

(

y

,

x

)

is the

inverted arrow

of the arrow

(

x

,

y

)

.

***articulation point***

A

vertex

in a

connected graph

whose removal would

disconnect

the graph. More generally, a vertex whose removal increases the number of

component

s.

***-ary***

A

k

-ary tree

is a rooted tree in which every internal vertex has no more than

k

children. A 1-ary tree is just a path. A 2-ary tree is also called a

binary tree

, although that term more properly refers to 2-ary trees in which the children of each node are distinguished as being left or right children (with at most one of each type). A

k

-ary tree is said to be complete if every internal vertex has exactly

k

children.

***augmenting***

A special type of alternating path; see

alternating

.

***automorphism***

A

graph automorphism

is a symmetry of a graph, an isomorphism from the graph to itself.


## B

***bag***

One of the sets of vertices in a

tree decomposition

.

***balanced***

A bipartite or multipartite graph is balanced if each two subsets of its vertex partition have sizes within one of each other.

***ball***

A ball (also known as a neighborhood ball or distance ball) is the set of all vertices that are at most distance r from a vertex. More formally, for a given vertex v and radius r, the ball B(v,r) consists of all vertices whose shortest path distance to v is less than or equal to r.

***bandwidth***

The

bandwidth

of a graph

G

is the minimum, over all orderings of vertices of

G

, of the length of the longest edge (the number of steps in the ordering between its two endpoints). It is also one less than the size of the maximum clique in a proper interval completion of

G

, chosen to minimize the clique size.

***biclique***

Synonym for

complete bipartite graph

or complete bipartite subgraph; see

complete

.

***biconnected***

Usually a synonym for

2

-vertex-connected

, but sometimes includes

K

2

though it is not 2-connected. See

connected

; for

biconnected components

, see

component

.

***binding number***

The smallest possible ratio of the number of neighbors of a proper subset of vertices to the size of the subset.

***bipartite***

A

bipartite graph

is a graph whose vertices can be divided into two disjoint sets such that the vertices in one set are not connected to each other, but may be connected to vertices in the other set. Put another way, a bipartite graph is a graph with no odd cycles; equivalently, it is a graph that may be properly colored with two colors. Bipartite graphs are often written

G

= (

U

,

V

,

E

)

where

U

and

V

are the subsets of vertices of each color. However, unless the graph is connected, it may not have a unique 2-coloring.

***biregular***

A

biregular graph

is a

bipartite

graph in which there are only two different vertex degrees, one for each set of the vertex bipartition.

***block***

1.

A block of a graph

G

is a maximal subgraph which is either an isolated vertex, a bridge edge, or a 2-connected subgraph. If a block is 2-connected, every pair of vertices in it belong to a common cycle. Every edge of a graph belongs in exactly one block.

2.

The block graph of a graph

G

is another graph whose vertices are the blocks of

G

, with an edge connecting two vertices when the corresponding blocks share an articulation point; that is, it is the intersection graph of the blocks of

G

. The block graph of any graph is a

forest

.

3.

The block-cut (or block-cutpoint) graph of a graph

G

is a bipartite graph where one partite set consists of the cut-vertices of

G

, and the other has a vertex

$b_{i}$

for each block

$B_{i}$

of

G

. When

G

is connected, its block-cutpoint graph is a tree.

4.

A

block graph

(also called a clique tree if connected, and sometimes erroneously called a Husimi tree) is a graph all of whose blocks are complete graphs. A

forest

is a block graph; so in particular the block graph of any graph is a block graph, and every block graph may be constructed as the block graph of a graph.

***bond***

A

minimal

cut-set

: a set of edges whose removal disconnects the graph, for which no proper subset has the same property.

***book***

1.

A

book

, book graph, or triangular book is a complete tripartite graph

K

1,1,

n

; a collection of

n

triangles joined at a shared edge.

2.

Another type of graph, also called a book, or a quadrilateral book, is a collection of

4

-cycles joined at a shared edge; the Cartesian product of a star with an edge.

3.

A

book embedding

is an embedding of a graph onto a topological book, a space formed by joining a collection of half-planes along a shared line. Usually, the vertices of the embedding are required to be on the line, which is called the spine of the embedding, and the edges of the embedding are required to lie within a single half-plane, one of the pages of the book.

***boundary***

1.

In a

graph embedding

, a boundary walk is the subgraph containing all incident edges and vertices to a

face

.

***bramble***

A

bramble

is a collection of mutually touching connected subgraphs, where two subgraphs touch if they share a vertex or each includes one endpoint of an edge. The order of a bramble is the smallest size of a set of vertices that has a nonempty intersection with all of the subgraphs. The treewidth of a graph is the maximum order of any of its brambles.

***branch***

A path of degree-two vertices, ending at vertices whose degree is unequal to two.

***branch-decomposition***

A

branch-decomposition

of

G

is a hierarchical clustering of the edges of

G

, represented by an unrooted binary tree with its leaves labeled by the edges of

G

. The width of a branch-decomposition is the maximum, over edges

e

of this binary tree, of the number of shared vertices between the subgraphs determined by the edges of

G

in the two subtrees separated by

e

. The branchwidth of

G

is the minimum width of any branch-decomposition of

G

.

***branchwidth***

See

branch-decomposition

.

***bridge***

1.

A

bridge

, isthmus, or cut edge is an edge whose removal would disconnect the graph. A bridgeless graph is one that has no bridges; equivalently, a 2-edge-connected graph.

2.

A bridge of a subgraph

H

is a maximal connected subgraph separated from the rest of the graph by

H

. That is, it is a maximal subgraph that is edge-disjoint from

H

and in which each two vertices and edges belong to a path that is internally disjoint from

H

.

H

may be a set of vertices. A chord is a one-edge bridge. In

planarity testing

,

H

is a cycle and a

peripheral cycle

is a cycle with at most one bridge; it must be a face boundary in any planar embedding of its graph.

3.

A bridge of a cycle can also mean a path that connects two vertices of a cycle but is shorter than either of the paths in the cycle connecting the same two vertices. A

bridged graph

is a graph in which every cycle of four or more vertices has a bridge.

***bridgeless***

A

bridgeless

or isthmus-free graph is a graph that has no bridge edges (i.e., isthmi); that is, each connected component is a

2-edge-connected graph

.

***butterfly***

1.

The

butterfly graph

has five vertices and six edges; it is formed by two triangles that share a vertex.

2.

The butterfly network is a graph used as a network architecture in distributed computing, closely related to the

cube-connected cycles

.


## C

****C****

C

n

is an

n

-vertex

cycle graph

; see

cycle

.

***cactus***

A

cactus graph

, cactus tree, cactus, or Husimi tree is a connected graph in which each edge belongs to at most one cycle. Its blocks are cycles or single edges. If, in addition, each vertex belongs to at most two blocks, then it is called a Christmas cactus.

***cage***

A

cage

is a regular graph with the smallest possible order for its girth.

***canonical***

***canonization***

A

canonical form

of a graph is an invariant such that two graphs have equal invariants if and only if they are isomorphic. Canonical forms may also be called canonical invariants or complete invariants, and are sometimes defined only for the graphs within a particular family of graphs.

Graph canonization

is the process of computing a canonical form.

***card***

A graph formed from a given graph by deleting one vertex, especially in the context of the

reconstruction conjecture

. See also

deck

, the multiset of all cards of a graph.

***carving width***

Carving width is a notion of graph width analogous to branchwidth, but using hierarchical clusterings of vertices instead of hierarchical clusterings of edges.

***caterpillar***

A

caterpillar tree

or caterpillar is a tree in which the internal nodes induce a path.

***center***

The

center

of a graph is the set of vertices of minimum

eccentricity

.

***centroid***

A

centroid

of a tree is a vertex

v

such that if rooted at

v

, no other vertex has subtree size greater than half the size of the tree.

***chain***

1.

Synonym for

walk

.

2.

When applying methods from

algebraic topology

to graphs, an element of a

chain complex

, namely a set of vertices or a set of edges.

***Cheeger constant***

See

expansion

.

***cherry***

A cherry is a path on three vertices.

****χ****

χ

(

G

)

(using the Greek letter chi) is the chromatic number of

G

and

χ

′(

G

)

is its chromatic index; see

chromatic

and

coloring

.

***child***

In a rooted tree, a child of a vertex

v

is a neighbor of

v

along an outgoing edge, one that is directed away from the root.

***chord***

***chordal***

1.

A chord of a cycle is an edge that does not belong to the cycle, for which both endpoints belong to the cycle.

2.

A

chordal graph

is a graph in which every cycle of four or more vertices has a chord, so the only induced cycles are triangles.

3.

A

strongly chordal graph

is a chordal graph in which every cycle of length six or more has an odd chord.

4.

A

chordal bipartite graph

is not chordal (unless it is a forest); it is a bipartite graph in which every cycle of six or more vertices has a chord, so the only induced cycles are 4-cycles.

5.

A

chord of a circle

is a line segment connecting two points on the circle; the

intersection graph

of a collection of chords is called a

circle graph

.

***chromatic***

Having to do with coloring; see

color

. Chromatic graph theory is the theory of graph coloring. The

chromatic number

χ

(

G

)

is the minimum number of colors needed in a proper coloring of

G

.

χ

′(

G

)

is the

chromatic index

of

G

, the minimum number of colors needed in a proper

edge coloring

of

G

.

***choosable***

***choosability***

A graph is

k

-choosable if it has a

list coloring

whenever each vertex has a list of

k

available colors. The choosability of the graph is the smallest

k

for which it is

k

-choosable.

***circle***

A

circle graph

is the

intersection graph

of chords of a circle.

***circuit***

A circuit may refer to a closed trail or an element of the

cycle space

(an Eulerian spanning subgraph). The

circuit rank

of a graph is the dimension of its cycle space.

***circumference***

The

circumference

of a graph is the length of its longest simple cycle. The graph is Hamiltonian if and only if its circumference equals its order.

***class***

1.

A

class

of graphs or family of graphs is a (usually infinite) collection of graphs, often defined as the graphs having some specific property. The word "class" is used rather than "set" because, unless special restrictions are made (such as restricting the vertices to be drawn from a particular set, and defining edges to be sets of two vertices) classes of graphs are usually not sets when formalized using set theory.

2.

A color class of a colored graph is the set of vertices or edges having one particular color.

3.

In the context of

Vizing's theorem

, on edge coloring simple graphs, a graph is said to be of class one if its chromatic index equals its maximum degree, and class two if its chromatic index equals one plus the degree. According to Vizing's theorem, all simple graphs are either of class one or class two.

***claw***

A

claw

is a tree with one internal vertex and three leaves, or equivalently the complete bipartite graph

K

1,3

. A

claw-free graph

is a graph that does not have an induced subgraph that is a claw.

***clique***

A

clique

is a set of mutually adjacent vertices (or the complete subgraph induced by that set). Sometimes a clique is defined as a maximal set of mutually adjacent vertices (or maximal complete subgraph), one that is not part of any larger such set (or subgraph). A

k

-clique is a clique of order

k

. The

clique number

ω

(

G

)

of a graph

G

is the order of its largest clique. The

clique graph

of a graph

G

is the

intersection graph

of the maximal cliques in

G

. See also

biclique

, a complete bipartite subgraph.

***clique tree***

A synonym for a

block graph

.

***clique-width***

The

clique-width

of a graph

G

is the minimum number of distinct labels needed to construct

G

by operations that create a labeled vertex, form the disjoint union of two labeled graphs, add an edge connecting all pairs of vertices with given labels, or relabel all vertices with a given label. The graphs of clique-width at most

2

are exactly the

cographs

.

***closed***

1.

A closed neighborhood is one that includes its central vertex; see

neighbourhood

.

2.

A closed walk is one that starts and ends at the same vertex; see

walk

.

3.

A graph is transitively closed if it equals its own transitive closure; see

transitive

.

4.

A graph property is closed under some operation on graphs if, whenever the argument or arguments to the operation have the property, then so does the result. For instance, hereditary properties are closed under induced subgraphs; monotone properties are closed under subgraphs; and minor-closed properties are closed under minors.

***closure***

1.

For the transitive closure of a directed graph, see

transitive

.

2.

A closure of a directed graph is a set of vertices that have no outgoing edges to vertices outside the closure. For instance, a sink is a one-vertex closure. The

closure problem

is the problem of finding a closure of minimum or maximum weight.

***co-***

This prefix has various meanings usually involving

complement graphs

. For instance, a

cograph

is a graph produced by operations that include complementation; a

cocoloring

is a coloring in which each vertex induces either an independent set (as in proper coloring) or a clique (as in a coloring of the complement).

***color***

***coloring***

1.

A

graph coloring

is a labeling of the vertices of a graph by elements from a given set of colors, or equivalently a partition of the vertices into subsets, called "color classes", each of which is associated with one of the colors.

2.

Some authors use "coloring", without qualification, to mean a proper coloring, one that assigns different colors to the endpoints of each edge. In graph coloring, the goal is to find a proper coloring that uses as few colors as possible; for instance,

bipartite graphs

are the graphs that have colorings with only two colors, and the

four color theorem

states that every

planar graph

can be colored with at most four colors. A graph is said to be

k

-colored if it has been (properly) colored with

k

colors, and

k

-colorable or

k

-chromatic if this is possible.

3.

Many variations of coloring have been studied, including

edge coloring

(coloring edges so that no two edges with the same endpoint share a color),

list coloring

(proper coloring with each vertex restricted to a subset of the available colors),

acyclic coloring

(every 2-colored subgraph is acyclic), co-coloring (every color class induces an independent set or a clique),

complete coloring

(every two color classes share an edge), and

total coloring

(both edges and vertices are colored).

4.

The coloring number of a graph is one plus the

degeneracy

. It is so called because applying a greedy coloring algorithm to a degeneracy ordering of the graph uses at most this many colors.

***commuting graph***

A

commuting graph

of a

group

or more generally a

semigroup

is an

undirected graph

in which the vertices are elements of the group/semigroup and there is an edge between any pair of elements that

commute

(that is, there is an edge between vertices

x

and

y

if and only if

xy

=

yx

).

***comparability***

An undirected graph is a

comparability graph

if its vertices are the elements of a

partially ordered set

and two vertices are adjacent when they are comparable in the partial order. Equivalently, a comparability graph is a graph that has a transitive orientation. Many other classes of graphs can be defined as the comparability graphs of special types of partial order.

***complement***

The

complement graph

${\bar {G}}$

of a simple graph

G

is another graph on the same vertex set as

G

, with an edge for each two vertices that are not adjacent in

G

.

***complete***

1.

A

complete graph

is one in which every two vertices are adjacent: all edges that could exist are present. A complete graph with

n

vertices is often denoted

K

n

. A

complete bipartite graph

is one in which every two vertices on opposite sides of the partition of vertices are adjacent. A complete bipartite graph with

a

vertices on one side of the partition and

b

vertices on the other side is often denoted

K

a

,

b

. The same terminology and notation has also been extended to

complete multipartite graphs

, graphs in which the vertices are divided into more than two subsets and every pair of vertices in different subsets are adjacent; if the numbers of vertices in the subsets are

a

,

b

,

c

, ...

then this graph is denoted

K

a

,

b

,

c

, ...

.

2.

A completion of a given graph is a supergraph that has some desired property. For instance, a

chordal completion

is a supergraph that is a chordal graph.

3.

A complete matching is a synonym for a

perfect matching

; see

matching

.

4.

A

complete coloring

is a proper coloring in which each pairs of colors is used for the endpoints of at least one edge. Every coloring with a minimum number of colors is complete, but there may exist complete colorings with larger numbers of colors. The

achromatic number

of a graph is the maximum number of colors in a complete coloring.

5.

A complete invariant of a graph is a synonym for a canonical form, an invariant that has different values for non-isomorphic graphs.

***component***

A

connected component

of a graph is a maximal connected subgraph. The term is also used for maximal subgraphs or subsets of a graph's vertices that have some higher order of connectivity, including

biconnected components

,

triconnected components

, and

strongly connected components

.

***condensation***

The

condensation

of a directed graph

G

is a directed acyclic graph with one vertex for each strongly connected component of

G

, and an edge connecting pairs of components that contain the two endpoints of at least one edge in

G

.

***cone***

A graph that contains a

universal vertex

.

***connect***

Cause to be

connected

.

***connected***

A

connected graph

is one in which each pair of vertices forms the endpoints of a path. Higher forms of connectivity include strong connectivity in directed graphs (for each two vertices there are paths from one to the other in both directions),

k

-vertex-connected graphs

(removing fewer than

k

vertices cannot disconnect the graph), and

k

-edge-connected graphs

(removing fewer than

k

edges cannot disconnect the graph).

***connected component***

Synonym for

component

.

***contraction***

Edge contraction

is an elementary operation that removes an edge from a graph while merging the two vertices that it previously joined. Vertex contraction (sometimes called vertex identification) is similar, but the two vertices are not necessarily connected by an edge. Path contraction occurs upon the set of edges in a path that contract to form a single edge between the endpoints of the path. The inverse of edge contraction is vertex splitting.

***converse***

The converse graph is a synonym for the transpose graph; see

transpose

.

***core***

1.

A

k

-core

is the induced subgraph formed by removing all vertices of degree less than

k

, and all vertices whose degree becomes less than

k

after earlier removals. See

degeneracy

.

2.

A

core

is a graph

G

such that every

graph homomorphism

from

G

to itself is an isomorphism.

3.

The

core

of a graph

G

is a minimal graph

H

such that there exist homomorphisms from

G

to

H

and vice versa.

H

is unique up to isomorphism. It can be represented as an induced subgraph of

G

, and is a core in the sense that all of its self-homomorphisms are isomorphisms.

4.

In the theory of graph matchings, the core of a graph is an aspect of its

Dulmage–Mendelsohn decomposition

, formed as the union of all maximum matchings.

***cotree***

1.

The complement of a

spanning tree

.

2.

A rooted tree structure used to describe a

cograph

, in which each cograph vertex is a leaf of the tree, each internal node of the tree is labeled with 0 or 1, and two cograph vertices are adjacent if and only if their lowest common ancestor in the tree is labeled 1.

***cover***

A

vertex cover

is a set of vertices incident to every edge in a graph. An

edge cover

is a set of edges incident to every vertex in a graph. A set of subgraphs of a graph covers that graph if its

union

– taken vertex-wise and edge-wise – is equal to the graph.

***critical***

A critical graph for a given property is a graph that has the property but such that every subgraph formed by deleting a single vertex does not have the property. For instance, a

factor-critical graph

is one that has a perfect matching (a 1-factor) for every vertex deletion, but (because it has an odd number of vertices) has no perfect matching itself. Compare

hypo-

, used for graphs which do not have a property but for which every one-vertex deletion does.

***cube***

***cubic***

1.

Cube graph

, the eight-vertex graph of the vertices and edges of a cube.

2.

Hypercube graph

, a higher-dimensional generalization of the cube graph.

3.

Folded cube graph

, formed from a hypercube by adding a matching connecting opposite vertices.

4.

Halved cube graph

, the

half-square

of a hypercube graph.

5.

Partial cube

, a distance-preserving subgraph of a hypercube.

6.

The cube of a graph

G

is the

graph power

G

3

.

7.

Cubic graph

, another name for a

3

-regular graph, one in which each vertex has three incident edges.

8.

Cube-connected cycles

, a cubic graph formed by replacing each vertex of a hypercube by a cycle.

***cut***

***cut-set***

A

cut

is a partition of the vertices of a graph into two subsets, or the set (also known as a cut-set) of edges that span such a partition, if that set is non-empty. An edge is said to span the partition if it has endpoints in both subsets. Thus, the removal of a cut-set from a connected graph disconnects it.

***cut point***

See

articulation point

.

***cut space***

The

cut space

of a graph is a

GF(2)

-

vector space

having the

cut-set

s of the graph as its elements and

symmetric difference

of sets as its vector addition operation.

***cycle***

1.

A

cycle

may be either a kind of graph or a kind of

walk

. As a walk it may be either be a closed walk (also called a

tour

) or more usually a closed walk without repeated vertices and consequently edges (also called a simple cycle). In the latter case it is usually regarded as a graph, i.e., the choices of first vertex and direction are usually considered unimportant; that is,

cyclic permutations

and reversals of the walk produce the same cycle. Important special types of cycle include

Hamiltonian cycles

,

induced cycles

,

peripheral cycles

, and the shortest cycle, which defines the

girth

of a graph. A

k

-cycle is a cycle of length

k

; for instance a

2

-cycle is a

digon

and a

3

-cycle is a triangle. A

cycle graph

is a graph that is itself a simple cycle; a cycle graph with

n

vertices is commonly denoted

C

n

.

2.

The

cycle space

is a

vector space

generated by the simple cycles in a graph, often over the field of 2 elements but also over other fields.


## D

***DAG***

Abbreviation for

directed acyclic graph

, a directed graph without any directed cycles.

***deck***

The multiset of graphs formed from a single graph

G

by deleting a single vertex in all possible ways, especially in the context of the

reconstruction conjecture

. An edge-deck is formed in the same way by deleting a single edge in all possible ways. The graphs in a deck are also called

cards

. See also

critical

(graphs that have a property that is not held by any card) and

hypo-

(graphs that do not have a property that is held by all cards).

***decomposition***

See

tree decomposition

,

path decomposition

, or

branch-decomposition

.

***degenerate***

***degeneracy***

A

k

-degenerate graph is an undirected graph in which every induced subgraph has minimum degree at most

k

. The

degeneracy

of a graph is the smallest

k

for which it is

k

-degenerate. A degeneracy ordering is an ordering of the vertices such that each vertex has minimum degree in the induced subgraph of it and all later vertices; in a degeneracy ordering of a

k

-degenerate graph, every vertex has at most

k

later neighbours. Degeneracy is also known as the

k

-core number, width, and linkage, and one plus the degeneracy is also called the coloring number or Szekeres–Wilf number.

k

-degenerate graphs have also been called

k

-inductive graphs.

***degree***

1.

The

degree

of a vertex in a graph is its number of incident edges.

The degree of a graph

G

(or its maximum degree) is the maximum of the degrees of its vertices, often denoted

Δ

(

G

)

; the minimum degree of

G

is the minimum of its vertex degrees, often denoted

δ

(

G

)

. Degree is sometimes called

valency

; the degree of

v

in

G

may be denoted

d

G

(

v

)

,

d

(

G

)

, or

deg(

v

)

. The total degree is the sum of the degrees of all vertices; by the

handshaking lemma

it is an even number. The

degree sequence

is the collection of degrees of all vertices, in sorted order from largest to smallest. In a directed graph, one may distinguish the in-degree (number of incoming edges) and out-degree (number of outgoing edges).

2.

The homomorphism degree of a graph is a synonym for its

Hadwiger number

, the order of the largest clique minor.

***Δ, *δ****

Δ

(

G

)

(using the Greek letter delta) is the maximum degree of a vertex in

G

, and

δ

(

G

)

is the minimum degree; see

degree

.

***density***

In a graph of

n

nodes, the density is the ratio of the number of edges of the graph to the number of edges in a complete graph on

n

nodes. See

dense graph

.

***depth***

The depth of a node in a rooted tree is the number of edges in the path from the root to the node. For instance, the depth of the root is 0 and the depth of any one of its adjacent nodes is 1. It is the level of a node minus one. Note, however, that some authors instead use

depth

as a synonym for the

level

of a node.

***diameter***

The

diameter

of a connected graph is the maximum length of a

shortest path

. That is, it is the maximum of the distances between pairs of vertices in the graph. If the graph has weights on its edges, then its weighted diameter measures path length by the sum of the edge weights along a path, while the unweighted diameter measures path length by the number of edges. For disconnected graphs, definitions vary: the diameter may be defined as infinite, or as the largest diameter of a connected component, or it may be undefined.

***diamond***

The

diamond graph

is an undirected graph with four vertices and five edges.

***diconnected***

Strong

ly

connected

. (Not to be confused with

disconnected

)

***digon***

A

digon

is a simple cycle of length two in a directed graph or a multigraph. Digons cannot occur in

simple

undirected graphs as they require repeating the same edge twice, which violates the definition of

simple

.

***digraph***

Synonym for

directed graph

.

***dipath***

See

directed path

.

***direct predecessor***

The tail of a directed edge whose head is the given vertex.

***direct successor***

The head of a directed edge whose tail is the given vertex.

***directed***

A

directed graph

is one in which the edges have a distinguished direction, from one vertex to another.

In a

mixed graph

, a directed edge is again one that has a distinguished direction; directed edges may also be called arcs or arrows.

***directed arc***

See

arrow

.

***directed edge***

See

arrow

.

***directed line***

See

arrow

.

***directed path***

A

path

in which all the

edge

s

have the same

direction

. If a directed path leads from

vertex

x

to vertex

y

,

x

is a

predecessor

of

y

,

y

is a

successor

of

x

, and

y

is said to be

reachable

from

x

.

***direction***

1.

The

asymmetric relation

between two

adjacent

vertices

in a

graph

, represented as an

arrow

.

2.

The asymmetric relation between two vertices in a

directed path

.

***disconnect***

Cause to be

disconnected

.

***disconnected***

Not

connected

.

***disjoint***

1.

Two subgraphs are edge disjoint if they share no edges, and vertex disjoint if they share no vertices.

2.

The disjoint union of two or more graphs is a graph whose vertex and edge sets are the

disjoint unions

of the corresponding sets.

***dissociation number***

A subset of vertices in a graph

G

is called

dissociation

if it induces a

subgraph

with maximum

degree

1.

***distance***

The

distance

between any two vertices in a graph is the length of the shortest path having the two vertices as its endpoints.

***domatic***

A domatic partition of a graph is a partition of the vertices into dominating sets. The

domatic number

of the graph is the maximum number of dominating sets in such a partition.

***dominating***

A

dominating set

is a set of vertices that includes or is adjacent to every vertex in the graph; not to be confused with a vertex cover, a vertex set that is incident to all edges in the graph. Important special types of dominating sets include independent dominating sets (dominating sets that are also independent sets) and connected dominating sets (dominating sets that induced connected subgraphs). A single-vertex dominating set may also be called a universal vertex. The domination number of a graph is the number of vertices in the smallest dominating set.

***dual***

A

dual graph

of a plane graph

G

is a graph that has a vertex for each face of

G

.


## E

****E****

E

(

G

)

is the edge set of

G

; see

edge set

.

***ear***

An ear of a graph is a path whose endpoints may coincide but in which otherwise there are no repetitions of vertices or edges.

***ear decomposition***

An

ear decomposition

is a partition of the edges of a graph into a sequence of ears, each of whose endpoints (after the first one) belong to a previous ear and each of whose interior points do not belong to any previous ear. An open ear is a simple path (an ear without repeated vertices), and an open ear decomposition is an ear decomposition in which each ear after the first is open; a graph has an open ear decomposition if and only if it is biconnected. An ear is odd if it has an odd number of edges, and an odd ear decomposition is an ear decomposition in which each ear is odd; a graph has an odd ear decomposition if and only if it is factor-critical.

***eccentricity***

The eccentricity of a vertex is the farthest distance from it to any other vertex.

***edge***

An edge is (together with vertices) one of the two basic units out of which graphs are constructed. Each edge has two (or in hypergraphs, more) vertices to which it is attached, called its endpoints. Edges may be directed or undirected; undirected edges are also called lines and directed edges are also called arcs or arrows. In an undirected

simple graph

, an edge may be represented as the set of its vertices, and in a directed simple graph it may be represented as an ordered pair of its vertices. An edge that connects vertices

x

and

y

is sometimes written

xy

.

***edge cut***

A set of

edge

s whose removal

disconnects

the

graph

. A one-edge cut is called a

bridge

,

isthmus

, or

cut edge

.

***edge set***

The set of edges of a given graph

G

, sometimes denoted by

E

(

G

)

.

***edgeless graph***

The

edgeless graph

or totally disconnected graph on a given set of vertices is the graph that has no edges. It is sometimes called the empty graph, but this term can also refer to a graph with no vertices.

***embedding***

A

graph embedding

is a topological representation of a graph as a subset of a topological space with each vertex represented as a point, each edge represented as a curve having the endpoints of the edge as endpoints of the curve, and no other intersections between vertices or edges. A

planar graph

is a graph that has such an embedding onto the Euclidean plane, and a

toroidal graph

is a graph that has such an embedding onto a torus. The

genus

of a graph is the minimum possible genus of a two-dimensional

manifold

onto which it can be embedded.

***empty graph***

1.

An

edgeless graph

on a nonempty set of vertices.

2.

The

order-zero graph

, a graph with no vertices and no edges.

***end***

An

end

of an infinite graph is an equivalence class of rays, where two rays are equivalent if there is a third ray that includes infinitely many vertices from both of them.

***endpoint***

One of the two vertices joined by a given edge, or one of the first or last vertex of a walk, trail or path. The first endpoint of a given directed edge is called the

tail

and the second endpoint is called the

head

.

***enumeration***

Graph enumeration

is the problem of counting the graphs in a given class of graphs, as a function of their order. More generally, enumeration problems can refer either to problems of counting a certain class of combinatorial objects (such as cliques, independent sets, colorings, or spanning trees), or of algorithmically listing all such objects.

***Eulerian***

An

Eulerian path

is a walk that uses every edge of a graph exactly once. An Eulerian circuit (also called an Eulerian cycle or an Euler tour) is a closed walk that uses every edge exactly once. An Eulerian graph is a graph that has an Eulerian circuit. For an undirected graph, this means that the graph is connected and every vertex has even degree. For a directed graph, this means that the graph is strongly connected and every vertex has in-degree equal to the out-degree. In some cases, the connectivity requirement is loosened, and a graph meeting only the degree requirements is called Eulerian.

***even***

Divisible by two; for instance, an even cycle is a cycle whose length is even.

***expander***

An

expander graph

is a graph whose edge expansion, vertex expansion, or spectral expansion is bounded away from zero.

***expansion***

1.

The edge expansion, isoperimetric number, or

Cheeger constant

of a graph

G

is the minimum ratio, over subsets

S

of at most half of the vertices of

G

, of the number of edges leaving

S

to the number of vertices in

S

.

2.

The vertex expansion, vertex isoperimetric number, or magnification of a graph

G

is the minimum ratio, over subsets

S

of at most half of the vertices of

G

, of the number of vertices outside but adjacent to

S

to the number of vertices in

S

.

3.

The unique neighbor expansion of a graph

G

is the minimum ratio, over subsets of at most half of the vertices of

G

, of the number of vertices outside

S

but adjacent to a unique vertex in

S

to the number of vertices in

S

.

4.

The spectral expansion of a

d

-regular graph

G

is the

spectral gap

between the largest eigenvalue

d

of its adjacency matrix and the second-largest eigenvalue.

5.

A family of graphs has

bounded expansion

if all its

r

-shallow minors have a ratio of edges to vertices bounded by a function of

r

, and polynomial expansion if the function of

r

is a polynomial.


## F

***face***

In a

plane graph

or

graph embedding

, a connected component of the subset of the plane or surface of the embedding that is disjoint from the graph. For an embedding in the plane, all but one face will be bounded; the one exceptional face that extends to infinity is called the outer (or infinite) face.

***factor***

A factor of a graph is a spanning subgraph: a subgraph that includes all of the vertices of the graph. The term is primarily used in the context of regular subgraphs: a

k

-factor is a factor that is

k

-regular. In particular, a

1

-factor is the same thing as a perfect matching. A

factor-critical graph

is a graph for which deleting any one vertex produces a graph with a

1

-factor.

***factorization***

A

graph factorization

is a partition of the edges of the graph into factors; a

k

-factorization is a partition into

k

-factors. For instance a

1

-factorization is an edge coloring with the additional property that each vertex is incident to an edge of each color.

***family***

A synonym for

class

.

***finite***

A graph is finite if it has a finite number of vertices and a finite number of edges. Many sources assume that all graphs are finite without explicitly saying so. A graph is locally finite if each vertex has a finite number of incident edges. An infinite graph is a graph that is not finite: it has infinitely many vertices, infinitely many edges, or both.

***first order***

The first order

logic of graphs

is a form of logic in which variables represent vertices of a graph, and there exists a binary predicate to test whether two vertices are adjacent. To be distinguished from second order logic, in which variables can also represent sets of vertices or edges.

***-flap***

For a set of vertices

X

, an

X

-flap is a connected component of the induced subgraph formed by deleting

X

. The flap terminology is commonly used in the context of

havens

, functions that map small sets of vertices to their flaps. See also the

bridge

of a cycle, which is either a flap of the cycle vertices or a chord of the cycle.

***forbidden***

A

forbidden graph characterization

is a characterization of a family of graphs as being the graphs that do not have certain other graphs as subgraphs, induced subgraphs, or minors. If

H

is one of the graphs that does not occur as a subgraph, induced subgraph, or minor, then

H

is said to be forbidden.

***forcing graph***

A

forcing graph

is a graph

H

such that evaluating the subgraph density of

H

in the graphs of a graph sequence

G(n)

is sufficient to test whether that sequence is

quasi-random

.

***forest***

A

forest

is an undirected graph without cycles (a disjoint union of unrooted trees), or a directed graph formed as a disjoint union of rooted trees.

***free edge***

An

edge

which is not in a

matching

.

***free vertex***

1.

A

vertex

not on a matched

edge

in a

matching

2.

A vertex which has not been matched.

***Frucht***

1.

Robert Frucht

2.

The

Frucht graph

, one of the two smallest cubic graphs with no nontrivial symmetries.

3.

Frucht's theorem

that every finite group is the group of symmetries of a finite graph.

***full***

Synonym for

induced

.

***functional graph***

A

functional graph

is a directed graph where every vertex has out-degree one. Equivalently, a functional graph is a maximal directed pseudoforest.


## G

****G****

A variable often used to denote a graph.

***genus***

The genus of a graph is the minimum genus of a surface onto which it can be embedded; see

embedding

.

***geodesic***

As a noun, a geodesic is a synonym for a

shortest path

. When used as an adjective, it means related to shortest paths or shortest path distances.

***giant***

In the theory of

random graphs

, a giant component is a connected component that contains a constant fraction of the vertices of the graph. In standard models of random graphs, there is typically at most one giant component.

***girth***

The

girth

of a graph is the length of its shortest cycle.

***graph***

The fundamental object of study in graph theory, a system of vertices connected in pairs by edges. Often subdivided into

directed graphs

or

undirected graphs

according to whether the edges have an orientation or not.

Mixed graphs

include both types of edges.

***greedy***

Produced by a

greedy algorithm

. For instance, a

greedy coloring

of a graph is a coloring produced by considering the vertices in some sequence and assigning each vertex the first available color.

***Grötzsch***

1.

Herbert Grötzsch

2.

The

Grötzsch graph

, the smallest triangle-free graph requiring four colors in any proper coloring.

3.

Grötzsch's theorem

that triangle-free planar graphs can always be colored with at most three colors.

***Grundy number***

1.

The

Grundy number

of a graph is the maximum number of colors produced by a

greedy coloring

, with a badly-chosen vertex ordering.

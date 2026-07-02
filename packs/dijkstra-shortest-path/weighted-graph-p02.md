---
title: "Glossary of graph theory (part 2/2)"
source: https://en.wikipedia.org/wiki/Weighted_graph
domain: dijkstra-shortest-path
license: CC-BY-SA-4.0
tags: dijkstra algorithm, shortest path, graph traversal, priority queue
fetched: 2026-07-02
part: 2/2
---

## H

****H****

A variable often used to denote a graph, especially when another graph has already been denoted by

G

.

****H*-coloring***

An

H

-coloring of a graph

G

(where

H

is also a graph) is a homomorphism from

H

to

G

.

****H*-free***

A graph is

H

-free if it does not have an induced subgraph isomorphic to

H

, that is, if

H

is a forbidden induced subgraph. The

H

-free graphs are the family of all graphs (or, often, all finite graphs) that are

H

-free.

For instance the

triangle-free graphs

are the graphs that do not have a

triangle graph

as a subgraph. The property of being

H

-free is always hereditary. A graph is

H

-minor-free if it does not have a minor isomorphic to

H

.

***Hadwiger***

1.

Hugo Hadwiger

2.

The

Hadwiger number

of a graph is the order of the largest complete minor of the graph. It is also called the contraction clique number or the homomorphism degree.

3.

The

Hadwiger conjecture

is the conjecture that the Hadwiger number is never less than the chromatic number.

***Hamiltonian***

A

Hamiltonian path

or Hamiltonian cycle is a simple spanning path or simple spanning cycle: it covers all of the vertices in the graph exactly once. A graph is Hamiltonian if it contains a Hamiltonian cycle, and traceable if it contains a Hamiltonian path.

***haven***

A

k

-

haven

is a function that maps every set

X

of fewer than

k

vertices to one of its flaps, often satisfying additional consistency conditions. The order of a haven is the number

k

. Havens can be used to characterize the treewidth of finite graphs and the ends and Hadwiger numbers of infinite graphs.

***height***

1.

The

height

of a node in a rooted tree is the number of edges in a longest path, going away from the root (i.e. its nodes have strictly increasing depth), that starts at that node and ends at a leaf.

2.

The

height

of a rooted tree is the height of its root. That is, the

height

of a tree is the number of edges in a longest possible path, going away from the root, that starts at the root and ends at a leaf.

3.

The

height

of a

directed acyclic graph

is the maximum length of a directed path in this graph.

***hereditary***

A

hereditary property

of graphs is a property that is closed under induced subgraphs: if

G

has a hereditary property, then so must every induced subgraph of

G

. Compare

monotone

(closed under all subgraphs) or

minor-closed

(closed under minors).

***hexagon***

A simple cycle consisting of exactly six edges and six vertices.

***hole***

A hole is an induced cycle of length four or more. An odd hole is a hole of odd length. An anti-hole is an induced subgraph of order four whose complement is a cycle; equivalently, it is a hole in the complement graph. This terminology is mainly used in the context of perfect graphs, which are characterized by the

strong perfect graph theorem

as being the graphs with no odd holes or odd anti-holes. The hole-free graphs are the same as the

chordal graphs

.

***homomorphic equivalence***

Two graphs are

homomorphically equivalent

if there exist two homomorphisms, one from each graph to the other graph.

***homomorphism***

1.

A

graph homomorphism

is a mapping from the vertex set of one graph to the vertex set of another graph that maps adjacent vertices to adjacent vertices. This type of mapping between graphs is the one that is most commonly used in category-theoretic approaches to graph theory. A proper graph coloring can equivalently be described as a homomorphism to a complete graph.

2.

The homomorphism degree of a graph is a synonym for its

Hadwiger number

, the order of the largest clique minor.

***hyperarc***

A directed

hyperedge

having a source and target set.

***hyperedge***

An

edge

in a

hypergraph

, having any number of endpoints, in contrast to the requirement that edges of graphs have exactly two endpoints.

***hypercube***

A

hypercube graph

is a graph formed from the vertices and edges of a geometric

hypercube

.

***hypergraph***

A

hypergraph

is a generalization of a graph in which each edge (called a hyperedge in this context) may have more than two endpoints.

***hypo-***

This prefix, in combination with a graph property, indicates a graph that does not have the property but such that every subgraph formed by deleting a single vertex does have the property. For instance, a

hypohamiltonian graph

is one that does not have a Hamiltonian cycle, but for which every one-vertex deletion produces a Hamiltonian subgraph. Compare

critical

, used for graphs which have a property but for which every one-vertex deletion does not.


## I

***in-degree***

The number of incoming edges in a directed graph; see

degree

.

***incidence***

An

incidence

in a graph is a vertex-edge pair such that the vertex is an endpoint of the edge.

***incidence matrix***

The

incidence matrix

of a graph is a matrix whose rows are indexed by vertices of the graph, and whose columns are indexed by edges, with a one in the cell for row

i

and column

j

when vertex

i

and edge

j

are incident, and a zero otherwise.

***incident***

(Adjective) The relation between an edge and one of its endpoints.

***incomparability***

An incomparability graph is the complement of a

comparability graph

; see

comparability

.

***independent***

1.

An

independent set

is a set of vertices that induces an edgeless subgraph. It may also be called a stable set or a coclique. The

independence number

α

(

G

)

is the size of the

maximum independent set

.

2.

In the

graphic matroid

of a graph, a subset of edges is independent if the corresponding subgraph is a tree or forest. In the

bicircular matroid

, a subset of edges is independent if the corresponding subgraph is a

pseudoforest

.

***indifference***

An

indifference graph

is another name for a proper interval graph or unit interval graph; see

proper

.

***induced***

An

induced subgraph

or full subgraph of a graph is a subgraph formed from a subset of vertices and from all of the edges that have both endpoints in the subset. Special cases include

induced paths

and

induced cycles

, induced subgraphs that are paths or cycles.

***inductive***

Synonym for

degenerate

.

***infinite***

An infinite graph is one that is not finite; see

finite

.

***internal***

A vertex of a path or tree is internal if it is not a leaf; that is, if its degree is greater than one. Two paths are internally disjoint (some people call it

independent

) if they do not have any vertex in common, except the first and last ones.

***intersection***

1.

The intersection of two graphs is their largest common subgraph, the graph formed by the vertices and edges that belong to both graphs.

2.

An

intersection graph

is a graph whose vertices correspond to sets or geometric objects, with an edge between two vertices exactly when the corresponding two sets or objects have a nonempty intersection. Several classes of graphs may be defined as the intersection graphs of certain types of objects, for instance

chordal graphs

(intersection graphs of subtrees of a tree),

circle graphs

(intersection graphs of chords of a circle),

interval graphs

(intersection graphs of intervals of a line),

line graphs

(intersection graphs of the edges of a graph), and

clique graphs

(intersection graphs of the maximal cliques of a graph). Every graph is an intersection graph for some family of sets, and this family is called an intersection representation of the graph. The

intersection number

of a graph

G

is the minimum total number of elements in any intersection representation of

G

.

***interval***

1.

An

interval graph

is an

intersection graph

of

intervals of a line

.

2.

The interval

[

u

,

v

]

in a graph is the union of all shortest paths from

u

to

v

.

3.

Interval thickness is a synonym for

pathwidth

.

***invariant***

A synonym of

property

.

***inverted arrow***

An

arrow

with an opposite

direction

compared to another arrow. The arrow

(

y

,

x

)

is the inverted arrow of the arrow

(

x

,

y

)

.

***isolated***

An isolated vertex of a graph is a vertex whose degree is zero, that is, a vertex with no incident edges.

***isomorphic***

Two graphs are isomorphic if there is an isomorphism between them; see

isomorphism

.

***isomorphism***

A

graph isomorphism

is a one-to-one incidence preserving correspondence of the vertices and edges of one graph to the vertices and edges of another graph. Two graphs related in this way are said to be isomorphic.

***isoperimetric***

See

expansion

.

***isthmus***

Synonym for

bridge

, in the sense of an edge whose removal disconnects the graph.


## J

***join***

The

join

of two graphs is formed from their

disjoint union

by adding an edge from each vertex of one graph to each vertex of the other. Equivalently, it is the complement of the disjoint union of the complements.


## K

****K****

For the notation for complete graphs, complete bipartite graphs, and complete multipartite graphs, see

complete

.

****κ****

κ

(

G

)

(using the Greek letter kappa) can refer to the

vertex connectivity

of

G

or to the

clique number

of

G

.

***kernel***

A kernel of a directed graph is a set of vertices which is both

stable

and

absorbing

.

***knot***

An inescapable section of a

directed graph

. See

knot (mathematics)

and

knot theory

.


## L

****L****

L

(

G

)

is the

line graph

of

G

; see

line

.

***label***

1.

Information associated with a vertex or edge of a graph. A labeled graph is a graph whose vertices or edges have labels. The terms

vertex-labeled

or

edge-labeled

may be used to specify which objects of a graph have labels.

Graph labeling

refers to several different problems of assigning labels to graphs subject to certain constraints. See also

graph coloring

, in which the labels are interpreted as colors.

2.

In the context of

graph enumeration

, the vertices of a graph are said to be labeled if they are all distinguishable from each other. For instance, this can be made to be true by fixing a one-to-one correspondence between the vertices and the integers from 1 to the order of the graph. When vertices are labeled, graphs that are isomorphic to each other (but with different vertex orderings) are counted as separate objects. In contrast, when the vertices are unlabeled, graphs that are isomorphic to each other are not counted separately.

***leaf***

1.

A leaf vertex or pendant vertex (especially in a tree) is a vertex whose degree is

1

. A leaf edge or pendant edge is the edge connecting a leaf vertex to its single neighbour.

2.

A

leaf power

of a tree is a graph whose vertices are the leaves of the tree and whose edges connect leaves whose distance in the tree is at most a given threshold.

***length***

In an unweighted graph, the length of a cycle, path, or walk is the number of edges it uses. In a weighted graph, it may instead be the sum of the weights of the edges that it uses. Length is used to define the

shortest path

,

girth

(shortest cycle length), and

longest path

between two vertices in a graph.

***level***

1.

This is the

depth

of a node plus 1, although some

define it instead to be synonym of

depth

. A node's level in a rooted tree is the number of nodes in the path from the root to the node. For instance, the root has level 1 and any one of its adjacent nodes has level 2.

2.

A set of all node having the same level or depth.

***line***

A synonym for an undirected edge. The

line graph

L

(

G

)

of a graph

G

is a graph with a vertex for each edge of

G

and an edge for each pair of edges that share an endpoint in

G

.

***linkage***

A synonym for

degeneracy

.

***list***

1.

An

adjacency list

is a computer representation of graphs for use in graph algorithms.

2.

List coloring

is a variation of graph coloring in which each vertex has a list of available colors.

***local***

A local property of a graph is a property that is determined only by the

neighbourhoods

of the vertices in the graph. For instance, a graph is locally finite if all of its neighborhoods are finite.

***loop***

A

loop

or self-loop is an edge both of whose endpoints are the same vertex. It forms a cycle of length

1

. These are not allowed in simple graphs.


## M

***magnification***

Synonym for vertex

expansion

.

***matching***

A

matching

is a set of edges in which no two share any vertex. A vertex is matched or saturated if it is one of the endpoints of an edge in the matching. A

perfect matching

or complete matching is a matching that matches every vertex; it may also be called a 1-factor, and can only exist when the order is even. A near-perfect matching, in a graph with odd order, is one that saturates all but one vertex. A

maximum matching

is a matching that uses as many edges as possible; the matching number

α

′(

G

)

of a graph

G

is the number of edges in a maximum matching. A

maximal matching

is a matching to which no additional edges can be added.

***maximal***

1.

A subgraph of given graph

G

is maximal for a particular property if it has that property but no other supergraph of it that is also a subgraph of

G

also has the same property. That is, it is a

maximal element

of the subgraphs with the property. For instance, a

maximal clique

is a complete subgraph that cannot be expanded to a larger complete subgraph. The word "maximal" should be distinguished from "maximum": a maximum subgraph is always maximal, but not necessarily vice versa.

2.

A simple graph with a given property is maximal for that property if it is not possible to add any more edges to it (keeping the vertex set unchanged) while preserving both the simplicity of the graph and the property. Thus, for instance, a

maximal planar graph

is a planar graph such that adding any more edges to it would create a non-planar graph.

***maximum***

A subgraph of a given graph

G

is maximum for a particular property if it is the largest subgraph (by order or size) among all subgraphs with that property. For instance, a

maximum clique

is any of the largest cliques in a given graph.

***median***

1.

A median of a triple of vertices, a vertex that belongs to shortest paths between all pairs of vertices, especially in median graphs and

modular graphs

.

2.

A

median graph

is a graph in which every three vertices have a unique median.

***Meyniel***

1.

Henri Meyniel, French graph theorist.

2.

A

Meyniel graph

is a graph in which every odd cycle of length five or more has at least two chords.

***minimal***

A subgraph of given graph is minimal for a particular property if it has that property but no proper subgraph of it also has the same property. That is, it is a

minimal element

of the subgraphs with the property.

***minimum cut***

A

cut

whose

cut-set

has minimum total weight, possibly restricted to cuts that separate a designated pair of vertices; they are characterized by the

max-flow min-cut theorem

.

***minor***

A graph

H

is a

minor

of another graph

G

if

H

can be obtained by deleting edges or vertices from

G

and contracting edges in

G

. It is a

shallow minor

if it can be formed as a minor in such a way that the subgraphs of

G

that were contracted to form vertices of

H

all have small diameter.

H

is a

topological minor

of

G

if

G

has a subgraph that is a

subdivision

of

H

. A graph is

H

-minor-free if it does not have

H

as a minor. A family of graphs is minor-closed if it is closed under minors; the

Robertson–Seymour theorem

characterizes minor-closed families as having a finite set of

forbidden

minors.

***mixed***

A

mixed graph

is a graph that may include both directed and undirected edges.

***modular***

1.

Modular graph

, a graph in which each triple of vertices has at least one median vertex that belongs to shortest paths between all pairs of the triple.

2.

Modular decomposition

, a decomposition of a graph into subgraphs within which all vertices connect to the rest of the graph in the same way.

3.

Modularity

of a graph clustering, the difference of the number of cross-cluster edges from its expected value.

***monotone***

A monotone property of graphs is a property that is closed under subgraphs: if

G

has a monotone property, then so must every subgraph of

G

. Compare

hereditary

(closed under induced subgraphs) or

minor-closed

(closed under minors).

***Moore graph***

A

Moore graph

is a regular graph for which the Moore bound is met exactly. The Moore bound is an inequality relating the degree, diameter, and order of a graph, proved by

Edward F. Moore

. Every Moore graph is a cage.

***multigraph***

A

multigraph

is a graph that allows multiple adjacencies (and, often, self-loops); a graph that is not required to be simple.

***multiple adjacency***

A multiple adjacency or multiple edge is a set of more than one edge that all have the same endpoints (in the same direction, in the case of directed graphs). A graph with multiple edges is often called a multigraph.

***multiplicity***

The multiplicity of an edge is the number of edges in a multiple adjacency. The multiplicity of a graph is the maximum multiplicity of any of its edges.


## N

****N****

1.

For the notation for open and closed neighborhoods, see

neighbourhood

.

2.

A lower-case

n

is often used (especially in computer science) to denote the number of vertices in a given graph.

***neighbor***

***neighbour***

A vertex that is adjacent to a given vertex.

***neighborhood***

***neighbourhood***

The

open neighbourhood

(or neighborhood) of a vertex

v

is the subgraph induced by all vertices that are adjacent to

v

. The closed neighbourhood is defined in the same way but also includes

v

itself. The open neighborhood of

v

in

G

may be denoted

N

G

(

v

)

or

N

(

v

)

, and the closed neighborhood may be denoted

N

G

[

v

]

or

N

[

v

]

. When the openness or closedness of a neighborhood is not specified, it is assumed to be open.

***network***

A graph in which attributes (e.g. names) are associated with the nodes and/or edges.

***node***

A synonym for

vertex

.

***non-edge***

A non-edge or anti-edge is a pair of vertices that are not adjacent; the edges of the complement graph.

***null graph***

See

empty graph

.


## O

***odd***

1.

An odd cycle is a cycle whose length is odd. The

odd girth

of a non-bipartite graph is the length of its shortest odd cycle. An odd hole is a special case of an odd cycle: one that is induced and has four or more vertices.

2.

An odd vertex is a vertex whose degree is odd. By the

handshaking lemma

every finite undirected graph has an even number of odd vertices.

3.

An odd ear is a simple path or simple cycle with an odd number of edges, used in odd ear decompositions of factor-critical graphs; see

ear

.

4.

An odd chord is an edge connecting two vertices that are an odd distance apart in an even cycle. Odd chords are used to define

strongly chordal graphs

.

5.

An

odd graph

is a special case of a

Kneser graph

, having one vertex for each

(

n

−

1)

-element subset of a

(2

n

−

1)

-element set, and an edge connecting two subsets when their corresponding sets are disjoint.

***open***

1.

See

neighbourhood

.

2.

See

walk

.

***order***

1.

The order of a graph

G

is the number of its vertices,

|

V

(

G

)|

. The variable

n

is often used for this quantity. See also

size

, the number of edges.

2.

A type of

logic of graphs

; see

first order

and

second order

.

3.

An order or ordering of a graph is an arrangement of its vertices into a sequence, especially in the context of

topological ordering

(an order of a directed acyclic graph in which every edge goes from an earlier vertex to a later vertex in the order) and

degeneracy ordering

(an order in which each vertex has minimum degree in the induced subgraph of it and all later vertices).

4.

For the order of a haven or bramble, see

haven

and

bramble

.

***orientation***

***oriented***

1.

An

orientation

of an undirected graph is an assignment of directions to its edges, making it into a directed graph. An oriented graph is one that has been assigned an orientation. So, for instance, a

polytree

is an oriented tree; it differs from a directed tree (an arborescence) in that there is no requirement of consistency in the directions of its edges. Other special types of orientation include

tournaments

, orientations of complete graphs;

strong orientations

, orientations that are strongly connected;

acyclic orientations

, orientations that are acyclic;

Eulerian orientations

, orientations that are Eulerian; and

transitive orientations

, orientations that are transitively closed.

2.

Oriented graph, used by some authors as a synonym for a

directed graph

.

***out-degree***

See

degree

.

***outer***

See

face

.

***outerplanar***

An

outerplanar graph

is a graph that can be embedded in the plane (without crossings) so that all vertices are on the outer face of the graph.


## P

***parent***

In a rooted tree, a parent of a vertex

v

is a neighbor of

v

along the incoming edge, the one that is directed toward the root.

***path***

A

path

may either be a walk or a walk without repeated vertices and consequently edges (also called a simple path), depending on the source. Important special cases include

induced paths

and

shortest paths

.

***path decomposition***

A

path decomposition

of a graph

G

is a tree decomposition whose underlying tree is a path. Its width is defined in the same way as for tree decompositions, as one less than the size of the largest bag. The minimum width of any path decomposition of

G

is the pathwidth of

G

.

***pathwidth***

The

pathwidth

of a graph

G

is the minimum width of a path decomposition of

G

. It may also be defined in terms of the clique number of an interval completion of

G

. It is always between the bandwidth and the treewidth of

G

. It is also known as interval thickness, vertex separation number, or node searching number.

***pendant***

See

leaf

.

***perfect***

1.

A

perfect graph

is a graph in which, in every induced subgraph, the chromatic number equals the clique number. The

perfect graph theorem

and

strong perfect graph theorem

are two theorems about perfect graphs, the former proving that their complements are also perfect and the latter proving that they are exactly the graphs with no odd holes or anti-holes.

2.

A

perfectly orderable graph

is a graph whose vertices can be ordered in such a way that a greedy coloring algorithm with this ordering optimally colors every induced subgraph. The perfectly orderable graphs are a subclass of the perfect graphs.

3.

A

perfect matching

is a matching that saturates every vertex; see

matching

.

4.

A perfect

1-factorization

is a partition of the edges of a graph into perfect matchings so that each two matchings form a Hamiltonian cycle.

***peripheral***

1.

A

peripheral cycle

or non-separating cycle is a cycle with at most one bridge.

2.

A peripheral vertex is a vertex whose

eccentricity

is maximum. In a tree, this must be a leaf.

***Petersen***

1.

Julius Petersen

(1839–1910), Danish graph theorist.

2.

The

Petersen graph

, a 10-vertex 15-edge graph frequently used as a counterexample.

3.

Petersen's theorem

that every bridgeless cubic graph has a perfect matching.

***planar***

A

planar graph

is a graph that has an

embedding

onto the Euclidean plane. A plane graph is a planar graph for which a particular embedding has already been fixed. A

k

-planar graph is one that can be drawn in the plane with at most

k

crossings per edge.

***polytree***

A

polytree

is an oriented tree; equivalently, a directed acyclic graph whose underlying undirected graph is a tree.

***power***

1.

A

graph power

G

k

of a graph

G

is another graph on the same vertex set; two vertices are adjacent in

G

k

when they are at distance at most

k

in

G

. A

leaf power

is a closely related concept, derived from a power of a tree by taking the subgraph induced by the tree's leaves.

2.

Power graph analysis

is a method for analyzing complex networks by identifying cliques, bicliques, and stars within the network.

3.

Power laws

in the

degree distributions

of

scale-free networks

are a phenomenon in which the number of vertices of a given degree is proportional to a power of the degree.

***predecessor***

A

vertex

coming before a given vertex in a

directed path

.

***prime***

1.

A

prime graph

is defined from an algebraic

group

, with a vertex for each

prime number

that divides the order of the group.

2.

In the theory of

modular decomposition

, a prime graph is a graph without any nontrivial modules.

3.

In the theory of

splits

, cuts whose cut-set is a complete bipartite graph, a prime graph is a graph without any splits. Every quotient graph of a maximal decomposition by splits is a prime graph, a star, or a complete graph.

4.

A prime graph for the

Cartesian product of graphs

is a connected graph that is not itself a product. Every connected graph can be uniquely factored into a Cartesian product of prime graphs.

***proper***

1.

A proper subgraph is a subgraph that removes at least one vertex or edge relative to the whole graph; for finite graphs, proper subgraphs are never isomorphic to the whole graph, but for infinite graphs they can be.

2.

A proper coloring is an assignment of colors to the vertices of a graph (a coloring) that assigns different colors to the endpoints of each edge; see

color

.

3.

A

proper interval graph

or proper circular arc graph is an intersection graph of a collection of intervals or circular arcs (respectively) such that no interval or arc contains another interval or arc. Proper interval graphs are also called unit interval graphs (because they can always be represented by unit intervals) or indifference graphs.

***property***

A

graph property

is something that can be true of some graphs and false of others, and that depends only on the graph structure and not on incidental information such as labels. Graph properties may equivalently be described in terms of classes of graphs (the graphs that have a given property). More generally, a graph property may also be a function of graphs that is again independent of incidental information, such as the size, order, or degree sequence of a graph; this more general definition of a property is also called an invariant of the graph.

***pseudoforest***

A

pseudoforest

is an undirected graph in which each connected component has at most one cycle, or a directed graph in which each vertex has at most one outgoing edge.

***pseudograph***

A pseudograph is a graph or multigraph that allows self-loops.


## Q

***quasi-line graph***

A quasi-line graph or locally co-bipartite graph is a graph in which the open neighborhood of every vertex can be partitioned into two cliques. These graphs are always

claw-free

and they include as a special case the

line graphs

. They are used in the structure theory of claw-free graphs.

***quasi-random graph sequence***

A

quasi-random graph sequence

is a sequence of graphs that shares several properties with a sequence of

random graphs

generated according to the

Erdős–Rényi random graph model

.

***quiver***

A

quiver

is a directed multigraph, as used in

category theory

. The edges of a quiver are called arrows.


## R

***radius***

The radius of a graph is the minimum

eccentricity

of any vertex.

***Ramanujan***

A

Ramanujan graph

is a graph whose spectral expansion is as large as possible. That is, it is a

d

-regular graph, such that the second-largest eigenvalue of its adjacency matrix is at most

$2{\sqrt {d-1}}$

.

***ray***

A ray, in an infinite graph, is an infinite simple path with exactly one endpoint. The

ends

of a graph are equivalence classes of rays.

***reachability***

The ability to get from one

vertex

to another within a

graph

.

***reachable***

Has an affirmative

reachability

. A

vertex

y

is said to be reachable from a vertex

x

if there exists a

path

from

x

to

y

.

***recognizable***

In the context of the

reconstruction conjecture

, a graph property is recognizable if its truth can be determined from the deck of the graph. Many graph properties are known to be recognizable. If the reconstruction conjecture is true, all graph properties are recognizable.

***reconstruction***

The

reconstruction conjecture

states that each undirected graph

G

is uniquely determined by its

deck

, a multiset of graphs formed by removing one vertex from

G

in all possible ways. In this context, reconstruction is the formation of a graph from its deck.

***rectangle***

A simple cycle consisting of exactly four edges and four vertices.

***regular***

A graph is

d

-regular when all of its vertices have degree

d

. A

regular graph

is a graph that is

d

-regular for some

d

.

***regular tournament***

A regular tournament is a tournament where in-degree equals out-degree for all vertices.

***reverse***

See

transpose

.

***root***

1.

A designated vertex in a graph, particularly in directed trees and

rooted graphs

.

2.

The inverse operation to a

graph power

: a

k

th root of a graph

G

is another graph on the same vertex set such that two vertices are adjacent in

G

if and only if they have distance at most

k

in the root.


## S

***saturated***

See

matching

.

***searching number***

Node searching number is a synonym for

pathwidth

.

***second order***

The second order

logic of graphs

is a form of logic in which variables may represent vertices, edges, sets of vertices, and (sometimes) sets of edges. This logic includes predicates for testing whether a vertex and edge are incident, as well as whether a vertex or edge belongs to a set. To be distinguished from first order logic, in which variables can only represent vertices.

***self-loop***

Synonym for

loop

.

***separating vertex***

See

articulation point

.

***separation number***

Vertex separation number is a synonym for

pathwidth

.

***sibling***

In a rooted tree, a sibling of a vertex

v

is a vertex which has the same parent vertex as

v

.

***simplicial vertex***

A

simplicial vertex

is a vertex whose closed

neighborhood

forms a

clique

.

***simple***

1.

A

simple graph

is a graph without loops and without multiple adjacencies. That is, each edge connects two distinct endpoints and no two edges have the same endpoints. A simple edge is an edge that is not part of a multiple adjacency. In many cases, graphs are assumed to be simple unless specified otherwise.

2.

A simple path or a simple cycle is a path or cycle that has no repeated vertices and consequently no repeated edges.

***sink***

A sink, in a directed graph, is a vertex with no outgoing edges (out-degree equals 0).

***size***

The size of a graph

G

is the number of its edges,

|

E

(

G

)|

.

The variable

m

is often used for this quantity. See also

order

, the number of vertices.

***small-world network***

A

small-world network

is a graph in which most nodes are not neighbors of one another, but most nodes can be reached from every other node by a small number of hops or steps. Specifically, a small-world network is defined to be a graph where the typical distance

L

between two randomly chosen nodes (the number of steps required) grows proportionally to the logarithm of the number of nodes

N

in the network

***snark***

A

snark

is a simple, connected, bridgeless cubic graph with chromatic index equal to 4.

***source***

A source, in a directed graph, is a vertex with no incoming edges (in-degree equals 0).

***space***

In

algebraic graph theory

, several

vector spaces

over the

binary field

may be associated with a graph. Each has sets of edges or vertices for its vectors, and

symmetric difference

of sets as its vector sum operation. The

edge space

is the space of all sets of edges, and the

vertex space

is the space of all sets of vertices. The

cut space

is a subspace of the edge space that has the cut-sets of the graph as its elements. The

cycle space

has the Eulerian spanning subgraphs as its elements.

***spanner***

A spanner is a (usually sparse) graph whose shortest path distances approximate those in a dense graph or other metric space. Variations include

geometric spanners

, graphs whose vertices are points in a geometric space;

tree spanners

, spanning trees of a graph whose distances approximate the graph distances, and graph spanners, sparse subgraphs of a dense graph whose distances approximate the original graph's distances. A greedy spanner is a graph spanner constructed by a greedy algorithm, generally one that considers all edges from shortest to longest and keeps the ones that are needed to preserve the distance approximation.

***spanning***

A subgraph is spanning when it includes all of the vertices of the given graph. Important cases include

spanning trees

(spanning subgraphs that are trees) and

perfect matchings

(spanning subgraphs that are matchings). A spanning subgraph may also be called a

factor

, especially (but not only) when it is regular.

***sparse***

A

sparse graph

is one that has few edges relative to its number of vertices. In some definitions the same property should also be true for all subgraphs of the given graph.

***spectral***

***spectrum***

The spectrum of a graph is the collection of

eigenvalues

of its adjacency matrix.

Spectral graph theory

is the branch of graph theory that uses spectra to analyze graphs. See also spectral

expansion

.

***split***

1.

A

split graph

is a graph whose vertices can be partitioned into a clique and an independent set. A related class of graphs, the double split graphs, are used in the proof of the strong perfect graph theorem.

2.

A

split

of an arbitrary graph is a partition of its vertices into two nonempty subsets, such that the edges spanning this cut form a complete bipartite subgraph. The splits of a graph can be represented by a tree structure called its

split decomposition

. A split is called a strong split when it is not crossed by any other split. A split is called nontrivial when both of its sides have more than one vertex. A graph is called prime when it has no nontrivial splits.

3.

Vertex splitting

(sometimes called vertex cleaving) is an elementary graph operation that splits a vertex into two, where these two new vertices are adjacent to the vertices that the original vertex was adjacent to. The inverse of vertex splitting is vertex contraction.

***square***

1.

The square of a graph

G

is the

graph power

G

2

; in the other direction,

G

is the square root of

G

2

. The

half-square

of a bipartite graph is the subgraph of its square induced by one side of the bipartition.

2.

A

squaregraph

is a planar graph that can be drawn so that all bounded faces are 4-cycles and all vertices of degree ≤ 3 belong to the outer face.

3.

A square grid graph is a

lattice graph

defined from points in the plane with integer coordinates connected by unit-length edges.

***stable***

A stable set is a synonym for an

independent set

.

***star***

A

star

is a tree with one internal vertex; equivalently, it is a complete bipartite graph

K

1,

n

for some

n

≥ 2

. The special case of a star with three leaves is called a claw.

***strength***

The

strength of a graph

is the minimum ratio of the number of edges removed from the graph to components created, over all possible removals; it is analogous to toughness, based on vertex removals.

***strong***

1.

For strong connectivity and

strongly connected components

of directed graphs, see

connected

and

component

. A

strong orientation

is an orientation that is strongly connected; see

orientation

.

2.

For the

strong perfect graph theorem

, see

perfect

.

3.

A

strongly regular graph

is a regular graph in which every two adjacent vertices have the same number of shared neighbours and every two non-adjacent vertices have the same number of shared neighbours.

4.

A

strongly chordal graph

is a chordal graph in which every even cycle of length six or more has an odd chord.

5.

A strongly perfect graph is a graph in which every induced subgraph has an independent set meeting all maximal cliques. The

Meyniel graphs

are also called "very strongly perfect graphs" because in them, every vertex belongs to such an independent set.

***subforest***

A subgraph of a

forest

.

***subgraph***

A subgraph of a graph

G

is another graph formed from a subset of the vertices and edges of

G

. The vertex subset must include all endpoints of the edge subset, but may also include additional vertices. A

spanning subgraph

is one that includes all vertices of the graph; an

induced subgraph

is one that includes all the edges whose endpoints belong to the vertex subset.

***subtree***

A subtree is a connected subgraph of a tree. Sometimes, for rooted trees, subtrees are defined to be a special type of connected subgraph, formed by all vertices and edges reachable from a chosen vertex.

***successor***

A

vertex

coming after a given vertex in a

directed path

.

***superconcentrator***

A superconcentrator is a graph with two designated and equal-sized subsets of vertices

I

and

O

, such that for every two equal-sized subsets

S

of

I

and

T

of

O

there exists a family of disjoint paths connecting every vertex in

S

to a vertex in

T

. Some sources require in addition that a superconcentrator be a directed acyclic graph, with

I

as its sources and

O

as its sinks.

***supergraph***

A graph formed by adding vertices, edges, or both to a given graph. If

H

is a subgraph of

G

, then

G

is a supergraph of

H

.


## T

***theta***

1.

A theta graph is the union of three internally disjoint (simple) paths that have the same two distinct end vertices.

2.

The

theta graph

of a collection of points in the Euclidean plane is constructed by constructing a system of cones surrounding each point and adding one edge per cone, to the point whose projection onto a central ray of the cone is smallest.

3.

The

Lovász number

or Lovász theta function of a graph is a graph invariant related to the clique number and chromatic number that can be computed in polynomial time by semidefinite programming.

***Thomsen graph***

The

Thomsen graph

is a name for the

complete bipartite graph

$K_{3,3}$

.

***topological***

1.

A

topological graph

is a representation of the vertices and edges of a graph by points and curves in the plane (not necessarily avoiding crossings).

2.

Topological graph theory

is the study of graph embeddings.

3.

Topological sorting

is the algorithmic problem of arranging a directed acyclic graph into a topological order, a vertex sequence such that each edge goes from an earlier vertex to a later vertex in the sequence.

***totally disconnected***

Synonym for

edgeless

.

***tour***

A closed trail, a

walk

that starts and ends at the same vertex and has no repeated edges. Euler tours are tours that use all of the graph edges; see

Eulerian

.

***tournament***

A

tournament

is an orientation of a complete graph; that is, it is a directed graph such that every two vertices are connected by exactly one directed edge (going in only one of the two directions between the two vertices).

***traceable***

A

traceable graph

is a graph that contains a Hamiltonian path.

***trail***

A

walk

without repeated edges.

***transitive***

Having to do with the

transitive property

. The

transitive closure

of a given directed graph is a graph on the same vertex set that has an edge from one vertex to another whenever the original graph has a path connecting the same two vertices. A

transitive reduction

of a graph is a minimal graph having the same transitive closure; directed acyclic graphs have a unique transitive reduction. A

transitive orientation

is an orientation of a graph that is its own transitive closure; it exists only for

comparability graphs

.

***transpose***

The

transpose graph

of a given directed graph is a graph on the same vertices, with each edge reversed in direction. It may also be called the converse or reverse of the graph.

***tree***

1.

A

tree

is an undirected graph that is both connected and acyclic, or a directed graph in which there exists a unique walk from one vertex (the root of the tree) to all remaining vertices.

2.

A

k

-tree

is a graph formed by gluing

(

k

+ 1)

-cliques together on shared

k

-cliques. A tree in the ordinary sense is a

1

-tree according to this definition.

***tree decomposition***

A

tree decomposition

of a graph

G

is a tree whose nodes are labeled with sets of vertices of

G

; these sets are called bags. For each vertex

v

, the bags that contain

v

must induce a subtree of the tree, and for each edge

uv

there must exist a bag that contains both

u

and

v

. The width of a tree decomposition is one less than the maximum number of vertices in any of its bags; the treewidth of

G

is the minimum width of any tree decomposition of

G

.

***treewidth***

The

treewidth

of a graph

G

is the minimum width of a tree decomposition of

G

. It can also be defined in terms of the clique number of a

chordal completion

of

G

, the order of a

haven

of

G

, or the order of a

bramble

of

G

.

***triangle***

A cycle of length three in a graph. A

triangle-free graph

is an undirected graph that does not have any triangle subgraphs.

***trivial***

A trivial graph is a graph with 0 or 1 vertices.

A graph with 0 vertices is also called

null graph

.

***Turán***

1.

Pál Turán

2.

A

Turán graph

is a balanced complete multipartite graph.

3.

Turán's theorem

states that Turán graphs have the maximum number of edges among all clique-free graphs of a given order.

4.

Turán's brick factory problem

asks for the minimum number of crossings in a drawing of a complete bipartite graph.

***twin***

Two vertices

u,v

are true twins if they have the same closed

neighborhood

:

N

G

[

u

] =

N

G

[

v

]

(this implies

u

and

v

are neighbors), and they are false twins if they have the same open neighborhood:

N

G

(

u

) =

N

G

(

v

))

(this implies

u

and

v

are not neighbors).


## U

***unary vertex***

In a rooted tree, a unary vertex is a vertex which has exactly one child vertex.

***undirected***

An

undirected graph

is a graph in which the two endpoints of each edge are not distinguished from each other. See also

directed

and

mixed

. In a

mixed graph

, an undirected edge is again one in which the endpoints are not distinguished from each other.

***uniform***

A hypergraph is

k

-uniform when all its edges have

k

endpoints, and uniform when it is

k

-uniform for some

k

. For instance, ordinary graphs are the same as

2

-uniform hypergraphs.

***universal***

1.

A

universal graph

is a graph that contains as subgraphs all graphs in a given family of graphs, or all graphs of a given size or order within a given family of graphs.

2.

A

universal vertex

(also called an apex or dominating vertex) is a vertex that is adjacent to every other vertex in the graph. For instance,

wheel graphs

and connected

threshold graphs

always have a universal vertex.

3.

In the

logic of graphs

, a vertex that is

universally quantified

in a formula may be called a universal vertex for that formula.

***unweighted graph***

A

graph

whose

vertices

and

edge

s have not been assigned

weight

s; the opposite of a

weighted graph

.

***utility graph***

The

utility graph

is a name for the

complete bipartite graph

$K_{3,3}$

.


## V

****V****

See

vertex set

.

***valency***

Synonym for

degree

.

***vertex***

A

vertex

(plural vertices) is (together with edges) one of the two basic units out of which graphs are constructed. Vertices of graphs are often considered to be atomic objects, with no internal structure.

***vertex cut***

***separating set***

A set of

vertices

whose removal

disconnects

the

graph

. A one-vertex cut is called an

articulation point

or

cut vertex

.

***vertex set***

The set of vertices of a given graph

G

, sometimes denoted by

V

(

G

)

.

***vertices***

See

vertex

.

***Vizing***

1.

Vadim G. Vizing

2.

Vizing's theorem

that the chromatic index is at most one more than the maximum degree.

3.

Vizing's conjecture

on the domination number of Cartesian products of graphs.

***volume***

The sum of the degrees of a set of vertices.


## W

***W***

The letter

W

is used in notation for

wheel graphs

and

windmill graphs

. The notation is not standardized.

***Wagner***

1.

Klaus Wagner

2.

The

Wagner graph

, an eight-vertex Möbius ladder.

3.

Wagner's theorem

characterizing planar graphs by their forbidden minors.

4.

Wagner's theorem characterizing the

K

5

-minor-free graphs.

***walk***

A

walk

is a finite or infinite

sequence

of

edges

which joins a sequence of

vertices

. Walks are also sometimes called

chains

.

A walk is

open

if its first and last vertices are distinct, and

closed

if they are repeated.

***weakly connected***

A

directed

graph is called weakly connected if replacing all of its directed edges with undirected edges produces a connected (undirected) graph.

***weight***

A numerical value, assigned as a label to a vertex or edge of a graph. The weight of a subgraph is the sum of the weights of the vertices or edges within that subgraph.

***weighted graph***

A

graph

whose

vertices

or

edge

s have been assigned

weight

s. A vertex-weighted graph has weights on its vertices and an edge-weighted graph has weights on its edges.

***well-colored***

A

well-colored graph

is a graph all of whose

greedy colorings

use the same number of colors.

***well-covered***

A

well-covered graph

is a graph all of whose maximal independent sets are the same size.

***wheel***

A

wheel graph

is a graph formed by adding a

universal vertex

to a simple cycle.

***width***

1.

A synonym for

degeneracy

.

2.

For other graph invariants known as width, see

bandwidth

,

branchwidth

,

clique-width

,

pathwidth

, and

treewidth

.

3.

The width of a tree decomposition or path decomposition is one less than the maximum size of one of its bags, and may be used to define treewidth and pathwidth.

4.

The width of a

directed acyclic graph

is the maximum cardinality of an antichain.

***windmill***

A

windmill graph

is the union of a collection of cliques, all of the same order as each other, with one shared vertex belonging to all the cliques and all other vertices and edges distinct.

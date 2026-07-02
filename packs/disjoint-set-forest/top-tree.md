---
title: "Top tree"
source: https://en.wikipedia.org/wiki/Top_tree
domain: disjoint-set-forest
license: CC-BY-SA-4.0
tags: disjoint-set data structure, union-find forest, connected components structure, path compression
fetched: 2026-07-02
---

# Top tree

A **top tree** is a data structure based on a binary tree for unrooted dynamic trees that is used mainly for various path-related operations. It allows simple divide-and-conquer algorithms. It has since been augmented to maintain dynamically various properties of a tree such as diameter, center and median.

A top tree $\Re$ is defined for an *underlying tree* T and a set $\partial {T}$ of at most two vertices called as External Boundary Vertices

## Glossary

### Boundary Node

See Boundary Vertex

### Boundary Vertex

A vertex in a connected subtree is a *Boundary Vertex* if it is connected to a vertex outside the subtree by an edge.

#### External Boundary Vertices

Up to a pair of vertices in the top tree $\Re$ can be called as External Boundary Vertices, they can be thought of as Boundary Vertices of the cluster which represents the entire top tree.

### Cluster

A *cluster* is a connected subtree with at most two Boundary Vertices. The set of Boundary Vertices of a given cluster C is denoted as $\partial {C}.$ With each cluster C the user may associate some meta information $I({\mathcal {C}}),$ and give methods to maintain it under the various internal operations.

#### Path Cluster

If $\pi ({\mathcal {C}})$ contains at least one edge then C is called a *Path Cluster*.

#### Point Cluster

See Leaf Cluster

#### Leaf Cluster

If $\pi ({\mathcal {C}})$ does not contain any edge i.e. C has only one Boundary Vertex then C is called a *Leaf Cluster*.

#### Edge Cluster

A Cluster containing a single edge is called an *Edge Cluster*.

##### Leaf Edge Cluster

A Leaf in the original Cluster is represented by a Cluster with just a single Boundary Vertex and is called a *Leaf Edge Cluster*.

##### Path Edge Cluster

Edge Clusters with two Boundary Nodes are called *Path Edge Cluster*.

### Internal Node

A node in ${\mathcal {C}}\setminus \partial {C}$ is called an *Internal Node* of C.

### Cluster Path

The path between the Boundary Vertices of C is called the *cluster path* of C and it is denoted by $\pi ({\mathcal {C}}).$

### Mergeable Clusters

Two Clusters A and B are *Mergeable* if ${\mathcal {A}}\cap {\mathcal {B}}$ is a singleton set (they have exactly one node in common) and ${\mathcal {A}}\cup {\mathcal {B}}$ is a Cluster.

## Introduction

*Top trees* are used for maintaining a Dynamic forest (set of trees) under link and cut operations.

The basic idea is to maintain a balanced Binary tree $\Re$ of logarithmic height in the number of nodes in the original tree T( i.e. in ${\mathcal {O}}(\log n)$ time); the **top tree** essentially represents the recursive subdivision of the original tree T into clusters.

In general the tree T may have weight on its edges.

There is a one-to-one correspondence with the edges of the original tree T and the leaf nodes of the top tree $\Re$ and each internal node of $\Re$ represents a cluster that is formed due to the union of the clusters that are its children.

The top tree data structure can be initialized in ${\mathcal {O}}(n)$ time.

Therefore the top tree $\Re$ over $({\mathcal {T}},\partial {T})$ is a binary tree such that

- The nodes of $\Re$ are clusters of $({\mathcal {T}},\partial {T})$ ;
- The leaves of $\Re$ are the edges of T;
- Sibling clusters are neighbours in the sense that they intersect in a single vertex, and then their parent cluster is their union.
- Root of $\Re$ is the tree T itself, with a set of at most two External Boundary Vertices.

A tree with a single vertex has an empty top tree, and one with just an edge is just a single node.

These trees are freely augmentable allowing the user a wide variety of flexibility and productivity without going into the details of the internal workings of the data structure, something which is also referred to as the *Black Box*.

## Dynamic Operations

The following three are the user allowable Forest Updates.

- **Link(v, w):** Where v and w are vertices in different trees T1 and T2. It returns a single top tree representing $\Re _{v}\cup \Re _{w}\cup {(v,w)}$
- **Cut(v, w)**: Removes the edge ${(v,w)}$ from a tree T with top tree $\Re ,$ thereby turning it into two trees T*v* and T*w* and returning two top trees $\Re _{v}$ and $\Re _{w}$ .
- **Expose(S)**: Is called as a subroutine for implementing most of the queries on a top tree. S contains at most 2 vertices. It makes original external vertices to be normal vertices and makes vertices from S the new External Boundary Vertices of the top tree. If S is nonempty it returns the new Root cluster C with $\partial {C}=S.$ **Expose({v,w})** fails if the vertices are from different trees.

## Internal Operations

The Forest updates are all carried out by a sequence of at most ${\mathcal {O}}(\log n)$ Internal Operations, the sequence of which is computed in further ${\mathcal {O}}(\log n)$ time. It may happen that during a tree update, a leaf cluster may change to a path cluster and the converse. Updates to top tree are done exclusively by these internal operations.

The $I({\mathcal {C}})$ is updated by calling a user defined function associated with each internal operation.

**$\mathrm {Merge} ({\mathcal {A}},{\mathcal {B}})$**

Here

A

and

B

are

Mergeable Clusters

, it returns

C

as the parent cluster of

A

and

B

and with boundary vertices as the boundary vertices of

${\mathcal {A}}\cup {\mathcal {B}}.$

Computes

$I({\mathcal {C}})$

using

$I({\mathcal {A}})$

and

$I({\mathcal {B}}).$

**$\mathrm {Split} ({\mathcal {C}})$**

Here

C

is the root cluster

${\mathcal {A}}\cup {\mathcal {B}}.$

It updates

$I({\mathcal {A}})$

and

$I({\mathcal {B}})$

using

$I({\mathcal {C}})$

and then it deletes the cluster

C

from

$\Re$

.

Split is usually implemented using $\mathrm {Clean} ({\mathcal {C}})$ method which calls user method for updates of $I({\mathcal {A}})$ and $I({\mathcal {B}})$ using $I({\mathcal {C}})$ and updates $I({\mathcal {C}})$ such that it's known there is no pending update needed in its children. Then the C is discarded without calling user defined functions. **Clean** is often required for queries without need to **Split**. If Split does not use Clean subroutine, and Clean is required, its effect could be achieved with overhead by combining **Merge** and **Split**.

The next two functions are analogous to the above two and are used for base clusters.

**$\mathrm {Create} (v,w)$**

Creates a cluster

C

for the edge

$(v,w).$

Sets

$\partial {C}=\partial (v,w).$

$I({\mathcal {C}})$

is computed from scratch.

**$\mathrm {Eradicate} ({\mathcal {C}})$**

C

is the edge cluster

$(v,w).$

User defined function is called to process

$I({\mathcal {C}})$

and then the cluster

C

is deleted from the top tree.

User can define **Choose $({\mathcal {C}}){:}$** operation which for a root (nonleaf) cluster selects one of its child clusters. The top tree blackbox provides **Search $({\mathcal {C}}){:}$** routine, which organizes **Choose** queries and reorganization of the top tree (using the Internal operations) such that it locates the only edge in intersection of all selected clusters. Sometimes the search should be limited to a path. There is a variant of nonlocal search for such purposes. If there are two external boundary vertices in the root cluster C, the edge is searched only on the path $\pi ({\mathcal {C}})$ . It is sufficient to do following modification: If only one of root cluster children is path cluster, it is selected by default without calling the **Choose** operation.

Finding i-th edge on longer path from v to w could be done by **C=Expose({v,w})** followed by **Search(C)** with appropriate **Choose**. To implement the **Choose** we use global variable representing v and global variable representing i. Choose selects the cluster A with $v\in \partial {A}$ iff length of $\pi ({\mathcal {A}})$ is at least i. To support the operation the length must be maintained in the I.

Similar task could be formulated for graph with edges with nonunit lengths. In that case the distance could address an edge or a vertex between two edges. We could define Choose such that the edge leading to the vertex is returned in the latter case. There could be defined update increasing all edge lengths along a path by a constant. In such scenario these updates are done in constant time just in root cluster. **Clean** is required to distribute the delayed update to the children. The **Clean** should be called before the **Choose** is invoked. To maintain length in I would in that case require to maintain unitlength in I as well.

Finding center of tree containing vertex v could be done by finding either bicenter edge or edge with center as one endpoint. The edge could be found by **C=Expose({v})** followed by **Search(C)** with appropriate **Choose**. The choose selects between children A, B with $a\in \partial {A}\cap \partial {B}$ the child with higher maxdistance(a). To support the operation the maximal distance in the cluster subtree from a boundary vertex should be maintained in the I. That requires maintenance of the cluster path length as well.

## Interesting Results and Applications

A number of interesting applications originally implemented by other methods have been easily implemented using the top tree's interface. Some of them include

- [SLEATOR AND TARJAN 1983]. We can maintain a dynamic collection of weighted trees in ${\mathcal {O}}(\log n)$ time per link and cut, supporting queries about the maximum edge weight between any two vertices in $O(\log n)$ time.
  - Proof outline: It involves maintaining at each node the maximum weight (⁠ ${\max }_{wt}$ ⁠) on its cluster path, if it is a point cluster then ${\max }_{wt}({\mathcal {C}})$ is initialised as $-\infty .$ When a cluster is a union of two clusters then it is the maximum value of the two merged clusters. If we have to find the max wt between v and w then we do ${\mathcal {C}}=\mathrm {Expose} (v,w),$ and report ${\max }_{wt}({\mathcal {C}}).$
- [SLEATOR AND TARJAN 1983]. In the scenario of the above application we can also add a common weight x to all edges on a given path v · · ·w in ${\mathcal {O}}(\log n)$ time.
  - Proof outline: We introduce a weight called extra(C) to be added to all the edges in $\pi ({\mathcal {C}}).$ Which is maintained appropriately ; split(C) requires that, for each path child A of C, we set ${\max }_{wt}(A):={\max }_{wt}({\mathcal {A}})+\mathrm {extra} ({\mathcal {C}})$ and $\mathrm {extra} ({\mathcal {A}}):=\mathrm {extra} ({\mathcal {A}})+\mathrm {extra} ({\mathcal {C}})$ . For C := join(A, B), we set ${\max }_{wt}({\mathcal {C}}):=\max\{{\max }_{wt}({\mathcal {A}}),{\max }_{wt}({\mathcal {B}})\}$ and $\mathrm {extra} ({\mathcal {C}}):=0$ . Finally, to find the maximum weight on the path v · · · w, we set ${\mathcal {C}}:=\mathrm {Expose} (v,w)$ and return ${\max }_{wt}({\mathcal {C}})$ .
- [GOLDBERG ET AL. 1991]. We can ask for the maximum weight in the underlying tree containing a given vertex v in ${\mathcal {O}}(\log n)$ time.
  - Proof outline: This requires maintaining additional information about the maximum weight non cluster path edge in a cluster under the Merge and Split operations.
- The distance between two vertices v and w can be found in ${\mathcal {O}}(\log n)$ time as $\mathrm {length} (\mathrm {Expose} (v,w))$ .
  - Proof outline:We will maintain the length length(C) of the cluster path. The length is maintained as the maximum weight except that, if C is created by a join(Merge), length(C) is the sum of lengths stored with its path children.
- Queries regarding diameter of a tree and its subsequent maintenance takes ${\mathcal {O}}(\log n)$ time.
- The Center and Median can me maintained under Link(Merge) and Cut(Split) operations and queried by non local search in ${\mathcal {O}}(\log n)$ time.

- Top trees are used in state-of-the-art algorithms for dynamic two-edge connectivity. In this problem, similarly to dynamic connectivity, the graph is subject to edge deletions and insertions, as well as queries asking whether a pair of vertices are two-edge connected, or there is a bridge separating them. Holm, de Lichtenberg, and Thorup give a deterministic algorithm with amortized update time $O(\log ^{4}n)$ , and $O(\log n/\log \log n)$ query time. Subsequent work by Holm, Rotenberg, and Thorup improves this to an amortized update time of $O(\log ^{2}n\log ^{2}\log n)$ , also using top trees

- The graph could be maintained allowing to update the edge set and ask queries on vertex 2-connectivity. Amortized complexity of updates is $O(\log ^{5}n)$ . Queries could be implemented even faster. The algorithm is not trivial, $I({\mathcal {C}})$ uses $\Theta (\log ^{2}n)$ space.

- Top trees can be used to compress trees in a way that is never much worse than DAG compression, but may be exponentially better.

## Implementation

Top trees have been implemented in a variety of ways, some of them include implementation using a *Multilevel Partition* (Top-trees and dynamic graph algorithms Jacob Holm and Kristian de Lichtenberg. Technical Report), and even by using Sleator-Tarjan s-t trees (typically with amortized time bounds), Frederickson's Topology Trees (with worst case time bounds) (Alstrup et al. Maintaining Information in Fully Dynamic Trees with Top Trees).

Amortized implementations are more simple, and with small multiplicative factors in time complexity. On the contrary the worst case implementations allow speeding up queries by switching off unneeded info updates during the query (implemented by persistence techniques). After the query is answered the original state of the top tree is used and the query version is discarded.

### Using Multilevel Partitioning

Any partitioning of clusters of a tree T can be represented by a Cluster Partition Tree CPT $({\mathcal {T}}),$ by replacing each cluster in the tree T by an edge. If we use a strategy P for partitioning T then the CPT would be CPTP ${\mathcal {T}}.$ This is done recursively till only one edge remains.

We would notice that all the nodes of the corresponding top tree $\Re$ are uniquely mapped into the edges of this multilevel partition. There may be some edges in the multilevel partition that do not correspond to any node in the top tree, these are the edges which represent only a single child in the level below it, i.e. a simple cluster. Only the edges that correspond to composite clusters correspond to nodes in the top tree $\Re .$

A partitioning strategy is important while we partition the Tree T into clusters. Only a careful strategy ensures that we end up in an ${\mathcal {O}}(\log n)$ height Multilevel Partition ( and therefore the top tree).

- The number of edges in subsequent levels should decrease by a constant factor.
- If a lower level is changed by an update then we should be able to update the one immediately above it using at most a constant number of insertions and deletions.

The above partitioning strategy ensures the maintenance of the top tree in ${\mathcal {O}}(\log n)$ time.

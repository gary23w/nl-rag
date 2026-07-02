---
title: "Spectral graph theory"
source: https://en.wikipedia.org/wiki/Spectral_graph_theory
domain: spectral-graph-theory
license: CC-BY-SA-4.0
tags: spectral graph theory, graph laplacian, adjacency matrix spectrum, algebraic connectivity
fetched: 2026-07-02
---

# Spectral graph theory

In mathematics, **spectral graph theory** is the study of the properties of a graph in relationship to the characteristic polynomial, eigenvalues, and eigenvectors of matrices associated with the graph, such as its adjacency matrix or Laplacian matrix.

The adjacency matrix of a simple undirected graph is a real symmetric matrix and is therefore orthogonally diagonalizable; its eigenvalues are real algebraic integers.

While the adjacency matrix depends on the vertex labeling, its spectrum is a graph invariant, although not a complete one.

Spectral graph theory is also concerned with graph parameters that are defined via multiplicities of eigenvalues of matrices associated to the graph, such as the Colin de Verdière number.

## Cospectral graphs

Two graphs are called **cospectral** or **isospectral** if the adjacency matrices of the graphs are isospectral, that is, if the adjacency matrices have the same eigenvalues with multiplicity.

Cospectral graphs need not be isomorphic, but isomorphic graphs are always cospectral.

### Graphs determined by their spectrum

A graph G is said to be determined by its spectrum if any other graph with the same spectrum as G is isomorphic to G .

Some first examples of families of graphs that are determined by their spectrum include:

- The complete graphs.
- The finite starlike trees.

### Cospectral mates

Two graphs are said to be cospectral mates if they are cospectral but are non-isomorphic.

The smallest pair of cospectral mates is {*K*1,4, *C*4 ∪ *K*1}, comprising the 5-vertex star and the graph union of the 4-vertex cycle and the single-vertex graph. The first example of cospectral graphs was reported by Collatz and Sinogowitz in 1957.

The smallest pair of polyhedral cospectral mates are enneahedra with eight vertices each.

### Finding cospectral graphs

Almost all trees are cospectral, i.e., as the number of vertices grows, the fraction of trees for which there exists a cospectral tree goes to 1.

A pair of regular graphs are cospectral if and only if their complements are cospectral.

A pair of distance-regular graphs are cospectral if and only if they have the same intersection array.

Cospectral graphs can also be constructed by means of the Sunada method.

Another important source of cospectral graphs are the point-collinearity graphs and the line-intersection graphs of point-line geometries. These graphs are always cospectral but are often non-isomorphic.

## Cheeger inequality

The famous Cheeger's inequality from Riemannian geometry has a discrete analogue involving the Laplacian matrix; this is perhaps the most important theorem in spectral graph theory and one of the most useful facts in algorithmic applications. It approximates the sparsest cut of a graph through the second eigenvalue of its Laplacian.

### Cheeger constant

The **Cheeger constant** (also **Cheeger number** or **isoperimetric number**) of a graph is a numerical measure of whether or not a graph has a "bottleneck". The Cheeger constant as a measure of "bottleneckedness" is of great interest in many areas: for example, constructing well-connected networks of computers, card shuffling, and low-dimensional topology (in particular, the study of hyperbolic 3-manifolds).

More formally, the Cheeger constant *h*(*G*) of a graph *G* on *n* vertices is defined as

$h(G)=\min _{0<|S|\leq {\frac {n}{2}}}{\frac {|\partial (S)|}{|S|}},$

where the minimum is over all nonempty sets *S* of at most *n*/2 vertices and ∂(*S*) is the *edge boundary* of *S*, i.e., the set of edges with exactly one endpoint in *S*.

### Cheeger inequality

When the graph *G* is *d*-regular, there is a relationship between *h*(*G*) and the spectral gap *d* − λ2 of *G*. An inequality due to Dodziuk and independently Alon and Milman states that

${\frac {1}{2}}(d-\lambda _{2})\leq h(G)\leq {\sqrt {2d(d-\lambda _{2})}}.$

This inequality is closely related to the Cheeger bound for Markov chains and can be seen as a discrete version of Cheeger's inequality in Riemannian geometry.

For general connected graphs that are not necessarily regular, an alternative inequality is given by Chung

${\frac {1}{2}}{\lambda }\leq {\mathbf {h} }(G)\leq {\sqrt {2\lambda }},$

where $\lambda$ is the least nontrivial eigenvalue of the normalized Laplacian, and ${\mathbf {h} }(G)$ is the (normalized) Cheeger constant

${\mathbf {h} }(G)=\min _{\emptyset \not =S\subset V(G)}{\frac {|\partial (S)|}{\min({\mathrm {vol} }(S),{\mathrm {vol} }({\bar {S}}))}}$

where ${\mathrm {vol} }(Y)$ is the sum of degrees of vertices in Y .

## Hoffman–Delsarte inequality

There is an eigenvalue bound for independent sets in regular graphs, originally due to Alan J. Hoffman and Philippe Delsarte.

Suppose that G is a k -regular graph on n vertices with least eigenvalue $\lambda _{\mathrm {min} }$ . Then: $\alpha (G)\leq {\frac {n}{1-{\frac {k}{\lambda _{\mathrm {min} }}}}}$ where $\alpha (G)$ denotes its independence number.

This bound has been applied to establish e.g. algebraic proofs of the Erdős–Ko–Rado theorem and its analogue for intersecting families of subspaces over finite fields.

For general graphs which are not necessarily regular, a similar upper bound for the independence number can be derived by using the maximum eigenvalue $\lambda '_{max}$ of the normalized Laplacian of G : $\alpha (G)\leq n(1-{\frac {1}{\lambda '_{\mathrm {max} }}}){\frac {\mathrm {maxdeg} }{\mathrm {mindeg} }}$ where ${\mathrm {maxdeg} }$ and ${\mathrm {mindeg} }$ denote the maximum and minimum degree in G , respectively. This a consequence of a more general inequality (pp. 109 in ): ${\mathrm {vol} }(X)\leq (1-{\frac {1}{\lambda '_{\mathrm {max} }}}){\mathrm {vol} }(V(G))$ where X is an independent set of vertices and ${\mathrm {vol} }(Y)$ denotes the sum of degrees of vertices in Y .

## Historical outline

Spectral graph theory emerged in the 1950s and 1960s. Besides graph theoretic research on the relationship between structural and spectral properties of graphs, another major source was research in quantum chemistry, but the connections between these two lines of work were not discovered until much later. The 1980 monograph *Spectra of Graphs* by Cvetković, Doob, and Sachs summarised nearly all research to date in the area. In 1988 it was updated by the survey *Recent Results in the Theory of Graph Spectra*. The 3rd edition of *Spectra of Graphs* (1995) contains a summary of the further recent contributions to the subject.

The field of discrete geometric analysis, created and developed by Toshikazu Sunada in the 2000s, deals with spectral graph theory in terms of discrete Laplacians associated with weighted graphs. It finds application in various other fields, including shape analysis.

A more recent development in spectral graph theory is vertex-frequency analysis, a set of techniques for solving problems in many real-life applications such as signal processing.

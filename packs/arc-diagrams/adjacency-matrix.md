---
title: "Adjacency matrix"
source: https://en.wikipedia.org/wiki/Adjacency_matrix
domain: arc-diagrams
license: CC-BY-SA-4.0
tags: arc diagram, one dimensional layout, circular layout, node ordering
fetched: 2026-07-02
---

# Adjacency matrix

In graph theory and computer science, an **adjacency matrix** is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not within the graph.

In the special case of a finite simple graph, the adjacency matrix is a (0,1)-matrix with zeros on its diagonal. If the graph is undirected (i.e. all of its edges are bidirectional), the adjacency matrix is symmetric. The relationship between a graph and the eigenvalues and eigenvectors of its adjacency matrix is studied in spectral graph theory.

The adjacency matrix of a graph should be distinguished from its incidence matrix, a different matrix representation whose elements indicate whether vertex–edge pairs are incident or not, and its degree matrix, which contains information about the degree of each vertex.

## Definition

For a simple graph with vertex set *U* = {*u*1, ..., *u**n*}, the adjacency matrix is a square *n* × *n* matrix A such that its element Aij is 1 when there is an edge from vertex *u*i to vertex *u*j, and 0 when there is no edge. The diagonal elements of the matrix are all 0, since edges from a vertex to itself (loops) are not allowed in simple graphs. It is also sometimes useful in algebraic graph theory to replace the nonzero elements with algebraic variables. The same concept can be extended to multigraphs and graphs with loops by storing the number of edges between each two vertices in the corresponding matrix element, and by allowing nonzero diagonal elements. Loops may be counted either once (as a single edge) or twice (as two vertex-edge incidences), as long as a consistent convention is followed. Undirected graphs often use the latter convention of counting loops twice, whereas directed graphs typically use the former convention.

### Of a bipartite graph

The adjacency matrix A of a bipartite graph whose two parts have r and s vertices can be written in the form

$A={\begin{pmatrix}0_{r,r}&B\\B^{\mathsf {T}}&0_{s,s}\end{pmatrix}},$

where B is an *r* × *s* matrix, and 0*r*,*r* and 0*s*,*s* represent the *r* × *r* and *s* × *s* zero matrices. In this case, the smaller matrix B uniquely represents the graph, and the remaining parts of A can be discarded as redundant. B is sometimes called the *biadjacency matrix*.

Formally, let *G* = (*U*, *V*, *E*) be a bipartite graph with parts *U* = {*u*1, ..., *u**r*}, *V* = {*v*1, ..., *v**s*} and edges E. The biadjacency matrix is the *r* × *s* 0–1 matrix B in which *b**i*,*j* = 1 if and only if (*u**i*, *v**j*) ∈ *E*.

If G is a bipartite multigraph or weighted graph, then the elements b*i,j* are taken to be the number of edges between the vertices or the weight of the edge (*u**i*, *v**j*), respectively.

### Variations

An (*a*, *b*, *c*)-adjacency matrix A of a simple graph has *A**i*,*j* = *a* if (*i*, *j*) is an edge, b if it is not, and c on the diagonal. The Seidel adjacency matrix is a (−1, 1, 0)-adjacency matrix. This matrix is used in studying strongly regular graphs and two-graphs.

The distance matrix has in position (*i*, *j*) the distance between vertices vi and vj. The distance is the length of a shortest path connecting the vertices. Unless lengths of edges are explicitly provided, the length of a path is the number of edges in it. The distance matrix resembles a high power of the adjacency matrix, but instead of telling only whether or not two vertices are connected (i.e., the connection matrix, which contains Boolean values), it gives the exact distance between them.

## Examples

### Undirected graphs

The convention followed here (for undirected graphs) is that each edge adds 1 to the appropriate cell in the matrix, and each loop (an edge from a vertex to itself) adds 2 to the appropriate cell on the diagonal in the matrix. This allows the degree of a vertex to be easily found by taking the sum of the values in either its respective row or column in the adjacency matrix.

| Labeled graph | Adjacency matrix |
|---|---|
|   | ${\begin{pmatrix}2&1&0&0&1&0\\1&0&1&0&1&0\\0&1&0&1&0&0\\0&0&1&0&1&1\\1&1&0&1&0&0\\0&0&0&1&0&0\end{pmatrix}}$ Coordinates are 1–6. |
| Nauru graph | Coordinates are 0–23. White fields are zeros, colored fields are ones. |

### Directed graphs

The adjacency matrix of a directed graph can be asymmetric. One can define the adjacency matrix of a directed graph either such that

1. a non-zero element Aij indicates an edge from i to j or
2. it indicates an edge from j to i.

The former definition is commonly used in graph theory and social network analysis (e.g., sociology, political science, economics, psychology). The latter is more common in other applied sciences (e.g., dynamical systems, physics, network science) where A is sometimes used to describe linear dynamics on graphs.

Using the first definition, the in-degrees of a vertex can be computed by summing the entries of the corresponding column and the out-degree of vertex by summing the entries of the corresponding row. When using the second definition, the in-degree of a vertex is given by the corresponding row sum and the out-degree is given by the corresponding column sum.

| Labeled graph | Adjacency matrix |
|---|---|
| Directed Cayley graph of S4 | Coordinates are 0–23. As the graph is directed, the matrix is not necessarily symmetric. |

### Trivial graphs

The adjacency matrix of a complete graph contains all ones except along the diagonal where there are only zeros. The adjacency matrix of an empty graph is a zero matrix.

## Properties

### Spectrum

The adjacency matrix of an undirected simple graph is symmetric, and therefore has a complete set of real eigenvalues and an orthogonal eigenvector basis. The set of eigenvalues of a graph is the **spectrum** of the graph. It is common to denote the eigenvalues by $\lambda _{1}\geq \lambda _{2}\geq \cdots \geq \lambda _{n}.$

The greatest eigenvalue $\lambda _{1}$ is bounded above by the maximum degree. This can be seen as result of the Perron–Frobenius theorem, but it can be proved easily. Let v be one eigenvector associated to $\lambda _{1}$ and x the entry in which v has maximum absolute value. Without loss of generality assume vx is positive since otherwise you simply take the eigenvector -v, also associated to $\lambda _{1}$ . Then

$\lambda _{1}v_{x}=(Av)_{x}=\sum _{y=1}^{n}A_{x,y}v_{y}\leq \sum _{y=1}^{n}A_{x,y}v_{x}=v_{x}\deg(x).$

For d-regular graphs, d is the first eigenvalue of A for the vector *v* = (1, ..., 1) (it is easy to check that it is an eigenvalue and it is the maximum because of the above bound). The multiplicity of this eigenvalue is the number of connected components of G, in particular $\lambda _{1}>\lambda _{2}$ for connected graphs. It can be shown that for each eigenvalue $\lambda _{i}$ , its opposite $-\lambda _{i}=\lambda _{n+1-i}$ is also an eigenvalue of A if G is a bipartite graph. In particular −d is an eigenvalue of any d-regular bipartite graph.

The difference $\lambda _{1}-\lambda _{2}$ is called the spectral gap and it is related to the expansion of G. It is also useful to introduce the spectral radius of A denoted by $\lambda (G)=\max _{\left|\lambda _{i}\right|<d}|\lambda _{i}|$ . This number is bounded by $\lambda (G)\geq 2{\sqrt {d-1}}-o(1)$ . This bound is tight in the Ramanujan graphs.

### Isomorphism and invariants

Suppose two directed or undirected graphs *G*1 and *G*2 with adjacency matrices *A*1 and *A*2 are given. *G*1 and *G*2 are isomorphic if and only if there exists a permutation matrix P such that

$PA_{1}P^{-1}=A_{2}.$

In particular, *A*1 and *A*2 are similar and therefore have the same minimal polynomial, characteristic polynomial, eigenvalues, determinant and trace. These can therefore serve as isomorphism invariants of graphs. However, two graphs may possess the same set of eigenvalues but not be isomorphic. Such linear operators are said to be isospectral.

### Matrix powers

If A is the adjacency matrix of the directed or undirected graph G, then the matrix *A**n* (i.e., the matrix product of n copies of A) has an interesting interpretation: the element (*i*, *j*) gives the number of (directed or undirected) walks of length n from vertex i to vertex j. If n is the smallest nonnegative integer, such that for some i, j, the element (*i*, *j*) of *A**n* is positive, then n is the distance between vertex i and vertex j. A great example of how this is useful is in counting the number of triangles in an undirected graph G, which is exactly the trace of *A*3 divided by 3 or 6 depending on whether the graph is directed or not. We divide by those values to compensate for the overcounting of each triangle. In an undirected graph, each triangle will be counted twice for all three nodes, because the path can be followed clockwise or counterclockwise : ijk or ikj. The adjacency matrix can be used to determine whether or not the graph is connected.

If a directed graph has a nilpotent adjacency matrix (i.e., if there exists n such that *A**n* is the zero matrix), then it is a directed acyclic graph.

## Data structures

The adjacency matrix may be used as a data structure for the representation of graphs in computer programs for manipulating graphs. Boolean data types are used, such as `True` and `False` in Python. The main alternative data structure, also in use for this application, is the adjacency list.

The space needed to represent an adjacency matrix and the time needed to perform operations on them is dependent on the matrix representation chosen for the underlying matrix. Sparse matrix representations only store non-zero matrix entries and implicitly represent the zero entries. They can, for example, be used to represent sparse graphs without incurring the space overhead from storing the many zero entries in the adjacency matrix of the sparse graph. In the following section the adjacency matrix is assumed to be represented by an array data structure so that zero and non-zero entries are all directly represented in storage.

Because each entry in the adjacency matrix requires only one bit, it can be represented in a very compact way, occupying only |*V* |2 / 8 bytes to represent a directed graph, or (by using a packed triangular format and only storing the lower triangular part of the matrix) approximately |*V* |2 / 16 bytes to represent an undirected graph. Although slightly more succinct representations are possible, this method gets close to the information-theoretic lower bound for the minimum number of bits needed to represent all n-vertex graphs. For storing graphs in text files, fewer bits per byte can be used to ensure that all bytes are text characters, for instance by using a Base64 representation. Besides avoiding wasted space, this compactness encourages locality of reference. However, for a large sparse graph, adjacency lists require less storage space, because they do not waste any space representing edges that are *not* present.

An alternative form of adjacency matrix (which, however, requires a larger amount of space) replaces the numbers in each element of the matrix with pointers to edge objects (when edges are present) or null pointers (when there is no edge). It is also possible to store edge weights directly in the elements of an adjacency matrix.

Besides the space tradeoff, the different data structures also facilitate different operations. Finding all vertices adjacent to a given vertex in an adjacency list is as simple as reading the list, and takes time proportional to the number of neighbors. With an adjacency matrix, an entire row must instead be scanned, which takes a larger amount of time, proportional to the number of vertices in the whole graph. On the other hand, testing whether there is an edge between two given vertices can be determined at once with an adjacency matrix, while requiring time proportional to the minimum degree of the two vertices with the adjacency list.

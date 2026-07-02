---
title: "Sperner's lemma"
source: https://en.wikipedia.org/wiki/Sperner's_lemma
domain: nash-equilibrium-computation
license: CC-BY-SA-4.0
tags: nash equilibrium computation, lemke howson algorithm, ppad complete, fixed point argument
fetched: 2026-07-02
---

# Sperner's lemma

In mathematics, **Sperner's lemma** is a combinatorial result on colorings of triangulations, analogous to the Brouwer fixed point theorem, which is equivalent to it. It states that every **Sperner coloring** (described below) of a triangulation of an n -dimensional simplex contains a cell whose vertices all have different colors.

The initial result of this kind was proved by Emanuel Sperner, in relation with proofs of invariance of domain. Sperner colorings have been used for effective computation of fixed points and in root-finding algorithms, and are applied in fair division (cake cutting) algorithms.

According to the Soviet *Mathematical Encyclopaedia* (ed. I.M. Vinogradov), a related 1929 theorem (of Knaster, Borsuk and Mazurkiewicz) had also become known as the *Sperner lemma* – this point is discussed in the English translation (ed. M. Hazewinkel). It is now commonly known as the Knaster–Kuratowski–Mazurkiewicz lemma.

## Statement

### One-dimensional case

In one dimension, Sperner's Lemma can be regarded as a discrete version of the intermediate value theorem. In this case, it essentially says that if a discrete function takes only the values 0 and 1, begins at the value 0 and ends at the value 1, then it must switch values an odd number of times.

### Two-dimensional case

The two-dimensional case is the one referred to most frequently. It is stated as follows:

Subdivide a triangle ABC arbitrarily into a triangulation consisting of smaller triangles meeting edge to edge. Then a Sperner coloring of the triangulation is defined as an assignment of three colors to the vertices of the triangulation such that

1. Each of the three vertices A, B, and C of the initial triangle has a distinct color
2. The vertices that lie along any edge of triangle ABC have only two colors, the two colors at the endpoints of the edge. For example, each vertex on AC must have the same color as A or C.

Then every Sperner coloring of every triangulation has at least one "rainbow triangle", a smaller triangle in the triangulation that has its vertices colored with all three different colors. More precisely, there must be an odd number of rainbow triangles.

### Multidimensional case

In the general case the lemma refers to an n-dimensional simplex:

${\mathcal {A}}=A_{1}A_{2}\ldots A_{n+1}.$

Consider any triangulation T, a disjoint division of ${\mathcal {A}}$ into smaller n-dimensional simplices, again meeting face-to-face. Denote the coloring function as:

$f:S\to \{1,2,3,\dots ,n,n+1\},$

where S is the set of vertices of T. A coloring function defines a Sperner coloring when:

1. The vertices of the large simplex are colored with different colors, that is, without loss of generality, *f*(*Ai*) = *i* for 1 ≤ *i* ≤ *n* + 1.
2. Vertices of T located on any k-dimensional subface of the large simplex

$A_{i_{1}}A_{i_{2}}\ldots A_{i_{k+1}}$

are colored only with the colors

$i_{1},i_{2},\ldots ,i_{k+1}.$

Then every Sperner coloring of every triangulation of the n-dimensional simplex has an odd number of instances of a *rainbow simplex*, meaning a simplex whose vertices are colored with all *n* + 1 colors. In particular, there must be at least one rainbow simplex.

## Proofs

### Proof by induction

We shall first address the two-dimensional case. Consider a graph G built from the triangulation T as follows:

The vertices of

G

are the members of

T

plus the area outside the triangle. Two vertices are connected with an edge if their corresponding areas share a common border with one endpoint colored 1 and the other colored 2.

Note that on the interval AB there is an odd number of borders colored 1-2 (simply because A is colored 1, B is colored 2; and as we move along AB, there must be an odd number of color changes in order to get different colors at the beginning and at the end). On the intervals BC and CA, there are no borders colored 1-2 at all. Therefore, the vertex of G corresponding to the outer area has an odd degree. By the handshaking lemma, G has an even number of vertices with odd degree. Therefore, the remaining graph, excluding the outer area, has an odd number of vertices with odd degree corresponding to members of T.

It can be easily seen that the only possible degree of a triangle from T is 0, 1, or 2, and that the degree 1 corresponds to a triangle colored with the three colors 1, 2, and 3.

Thus we have obtained a slightly stronger conclusion, which says that in a triangulation T there is an odd number (and at least one) of full-colored triangles.

A multidimensional case can be proved by induction on the dimension of a simplex. We apply the same reasoning, as in the two-dimensional case, to conclude that in a n-dimensional triangulation there is an odd number of full-colored simplices.

### Commentary

Here is an elaboration of the proof given previously, for a reader new to graph theory.

This diagram numbers the colors of the vertices of the example given previously. The small triangles whose vertices all have different numbers are shaded in the graph. Each small triangle becomes a node in the new graph derived from the triangulation. The small letters identify the areas, eight inside the figure, and area i designates the space outside of it.

As described previously, those nodes that share an edge whose endpoints are numbered 1 and 2 are joined in the derived graph. For example, node d shares an edge with the outer area i, and its vertices all have different numbers, so it is also shaded. Node b is not shaded because two vertices have the same number, but it is joined to the outer area.

One could add a new full-numbered triangle, say by inserting a node numbered 3 into the edge between 1 and 1 of node a, and joining that node to the other vertex of a. Doing so would have to create a pair of new nodes, like the situation with nodes f and g.

### Proof without induction

Andrew McLennan and Rabee Tourky presented a different proof, using the volume of a simplex. It proceeds in one step, with no induction.

## Computing a Sperner simplex

Suppose there is a *d*-dimensional simplex of side-length *N*, and it is triangulated into sub-simplices of side-length 1. There is a function that, given any vertex of the triangulation, returns its color. The coloring is guaranteed to satisfy Sperner's boundary condition. How many times do we have to call the function in order to find a rainbow simplex? Obviously, we can go over all the triangulation vertices, whose number is O(*Nd*), which is polynomial in *N* when the dimension is fixed. But, can it be done in time O(poly(log *N*)), which is polynomial in the binary representation of N?

This problem was first studied by Christos Papadimitriou. He introduced a complexity class called PPAD, which contains this as well as related problems (such as finding a Brouwer fixed point). He proved that finding a Sperner simplex is PPAD-complete even for *d*=3. Some 15 years later, Chen and Deng proved PPAD-completeness even for *d*=2. It is believed that PPAD-hard problems cannot be solved in time O(poly(log *N*)).

## Generalizations

### Subsets of labels

Suppose that each vertex of the triangulation may be labeled with multiple colors, so that the coloring function is *F* : *S* → 2[*n*+1].

For every sub-simplex, the set of labelings on its vertices is a set-family over the set of colors [*n* + 1]. This set-family can be seen as a hypergraph.

If, for every vertex v on a face of the simplex, the colors in *f*(*v*) are a subset of the set of colors on the face endpoints, then there exists a sub-simplex with a *balanced labeling* – a labeling in which the corresponding hypergraph admits a perfect fractional matching. To illustrate, here are some balanced labeling examples for *n* = 2:

- ({1}, {2}, {3}) - balanced by the weights (1, 1, 1).
- ({1,2}, {2,3}, {3,1}) - balanced by the weights (1/2, 1/2, 1/2).
- ({1,2}, {2,3}, {1}) - balanced by the weights (0, 1, 1).

This was proved by Shapley in 1973. It is a combinatorial analogue of the KKMS lemma.

### Polytopal variants

Suppose that we have a d-dimensional polytope P with n vertices. P is triangulated, and each vertex of the triangulation is labeled with a label from {1, …, *n*}. Every main vertex i is labeled i. A sub-simplex is called *fully-labeled* if it is d-dimensional, and each of its *d* + 1 vertices has a different label. If every vertex in a face F of P is labeled with one of the labels on the endpoints of F, then there are at least *n* – *d* fully-labeled simplices. Some special cases are:

- *d* = *n* – 1. In this case, P is a simplex. The polytopal Sperner lemma guarantees that there is at least 1 fully-labeled simplex. That is, it reduces to Sperner's lemma.
- *d* = 2. Suppose a two-dimensional polygon with n vertices is triangulated and labeled using the labels 1, …, *n* such that, on each face between vertex i and vertex *i* + 1 (mod *n*), only the labels i and *i* + 1 are used. Then, there are at least *n* – 2 sub-triangles in which three different labels are used.

The general statement was conjectured by Atanassov in 1996, who proved it for the case *d* = 2. The proof of the general case was first given by de Loera, Peterson, and Su in 2002. They provide two proofs: the first is non-constructive and uses the notion of *pebble sets*; the second is constructive and is based on arguments of following paths in graphs.

Meunier extended the theorem from polytopes to *polytopal bodies,* which need not be convex or simply-connected. In particular, if P is a polytope, then the set of its faces is a polytopal body. In every Sperner labeling of a polytopal body with vertices *v*1, …, *vn*, there are at least:

$n-d-1+\left\lceil {\frac {\min _{i=1}^{n}\deg _{B(P)}(v_{i})}{d}}\right\rceil$

fully-labeled simplices such that any pair of these simplices receives two different labelings. The degree deg*B*(*P*)(*vi*) is the number of edges of *B*(*P*) to which vi belongs. Since the degree is at least d, the lower bound is at least *n* – *d*. But it can be larger. For example, for the cyclic polytope in 4 dimensions with n vertices, the lower bound is:

$n-4-1+\left\lceil {\frac {n-1}{4}}\right\rceil \approx {\frac {5}{4}}n.$

Musin further extended the theorem to d-dimensional piecewise-linear manifolds, with or without a boundary.

Asada, Frick, Pisharody, Polevy, Stoner, Tsang and Wellner further extended the theorem to pseudomanifolds with boundary, and improved the lower bound on the number of facets with pairwise-distinct labels.

### Cubic variants

Suppose that, instead of a simplex triangulated into sub-simplices, we have an n-dimensional cube partitioned into smaller n-dimensional cubes.

Harold W. Kuhn proved the following lemma. Suppose the cube [0,*M*]*n*, for some integer M, is partitioned into Mn unit cubes. Suppose each vertex of the partition is labeled with a label from {1, …, *n* + 1}, such that for every vertex v: (1) if *vi* = 0 then the label on v is at most i; (2) if *vi*=*M* then the label on v is not i. Then there exists a unit cube with all the labels {1, …, *n* + 1} (some of them more than once). The special case *n* = 2 is: suppose a square is partitioned into sub-squares, and each vertex is labeled with a label from {1,2,3}. The left edge is labeled with 1 (= at most 1); the bottom edge is labeled with 1 or 2 (= at most 2); the top edge is labeled with 1 or 3 (= not 2); and the right edge is labeled with 2 or 3 (= not 1). Then there is a square labeled with 1,2,3.

Another variant, related to the Poincaré–Miranda theorem, is as follows. Suppose the cube [0,*M*]*n* is partitioned into Mn unit cubes. Suppose each vertex is labeled with a binary vector of length n, such that for every vertex v: (1) if *vi* = 0 then the coordinate i of label on v is 0; (2) if *vi* = *M* then coordinate i of the label on v is 1; (3) if two vertices are neighbors, then their labels differ by at most one coordinate. Then there exists a unit cube in which all 2*n* labels are different. In two dimensions, another way to formulate this theorem is: in any labeling that satisfies conditions (1) and (2), there is at least one cell in which the sum of labels is 0 [a 1-dimensional cell with (1,1) and (-1,-1) labels, or a 2-dimensional cells with all four different labels].

Wolsey strengthened these two results by proving that the number of completely-labeled cubes is odd.

Musin extended these results to general quadrangulations.

### Rainbow variants

Suppose that, instead of a single labeling, we have n different Sperner labelings. We consider pairs (simplex, permutation) such that, the label of each vertex of the simplex is chosen from a different labeling (so for each simplex, there are *n*! different pairs). Then there are at least *n*! fully labeled pairs. This was proved by Ravindra Bapat for any triangulation. A simpler proof, which only works for specific triangulations, was presented later by Su.

Another way to state this lemma is as follows. Suppose there are n people, each of whom produces a different Sperner labeling of the same triangulation. Then, there exists a simplex, and a matching of the people to its vertices, such that each vertex is labeled by its owner differently (one person labels its vertex by 1, another person labels its vertex by 2, etc.). Moreover, there are at least *n*! such matchings. This can be used to find an envy-free cake-cutting with connected pieces.

Asada, Frick, Pisharody, Polevy, Stoner, Tsang and Wellner extended this theorem to pseudomanifolds with boundary.

More generally, suppose we have m different Sperner labelings, where m may be different than n. Then:

1. For any positive integers *k*1, …, *km* whose sum is *m* + *n* – 1, there exists a baby-simplex on which, for every *i* ∈ {1, …, *m*}, labeling number i uses at least ki (out of n) distinct labels. Moreover, each label is used by at least one (out of m) labeling.
2. For any positive integers *I*1, …, *Im*whose sum is *m* + *n* – 1, there exists a baby-simplex on which, for every *j* ∈ {1, …, *n*},, the label j is used by at least lj (out of m) different labelings.

Both versions reduce to Sperner's lemma when *m* = 1, or when all m labelings are identical.

See for similar generalizations.

### Oriented variants

| Sequence | Degree |
|---|---|
| 123 | 1 (one 1-2 switch and no 2-1 switch) |
| 12321 | 0 (one 1-2 switch minus one 2-1 switch) |
| 1232 | 0 (as above; recall sequence is cyclic) |
| 1231231 | 2 (two 1-2 switches and no 2-1 switch) |

Brown and Cairns strengthened Sperner's lemma by considering the *orientation* of simplices. Each sub-simplex has an orientation that can be either +1 or -1 (if it is fully-labeled), or 0 (if it is not fully-labeled). They proved that the sum of all orientations of simplices is +1. In particular, this implies that there is an odd number of fully-labeled simplices.

As an example for *n* = 3, suppose a triangle is triangulated and labeled with {1,2,3}. Consider the cyclic sequence of labels on the boundary of the triangle. Define the *degree* of the labeling as the number of switches from 1 to 2, minus the number of switches from 2 to 1. See examples in the table at the right. Note that the degree is the same if we count switches from 2 to 3 minus 3 to 2, or from 3 to 1 minus 1 to 3.

Musin proved that *the number of fully labeled triangles is at least the degree of the labeling*. In particular, if the degree is nonzero, then there exists at least one fully labeled triangle.

If a labeling satisfies the Sperner condition, then its degree is exactly 1: there are 1-2 and 2-1 switches only in the side between vertices 1 and 2, and the number of 1-2 switches must be one more than the number of 2-1 switches (when walking from vertex 1 to vertex 2). Therefore, the original Sperner lemma follows from Musin's theorem.

### Trees and cycles

There is a similar lemma about finite and infinite trees and cycles.

Mirzakhani and Vondrak study a weaker variant of a Sperner labeling, in which the only requirement is that label *i* is not used on the face opposite to vertex *i*. They call it *Sperner-admissible labeling*. They show that there are Sperner-admissible labelings in which every cell contains at most 4 labels. They also prove an optimal lower bound on the number of cells that must have at least two different labels in each Sperner-admissible labeling. They also prove that, for any Sperner-admissible partition of the regular simplex, the total area of the boundary between the parts is minimized by the Voronoi partition.

## Applications

Sperner colorings have been used for effective computation of fixed points. A Sperner coloring can be constructed such that fully labeled simplices correspond to fixed points of a given function. By making a triangulation smaller and smaller, one can show that the limit of the fully labeled simplices is exactly the fixed point. Hence, the technique provides a way to approximate fixed points. A related application is the numerical detection of periodic orbits and symbolic dynamics. Sperner's lemma can also be used in root-finding algorithms and fair division algorithms; see Simmons–Su protocols.

Sperner's lemma is one of the key ingredients of the proof of Monsky's theorem, that a square cannot be cut into an odd number of equal-area triangles.

Sperner's lemma can be used to find a competitive equilibrium in an exchange economy, although there are more efficient ways to find it.

Fifty years after first publishing it, Sperner presented a survey on the development, influence and applications of his combinatorial lemma.

## Equivalent results

There are several fixed-point theorems which come in three equivalent variants: an algebraic topology variant, a combinatorial variant and a set-covering variant. Each variant can be proved separately using totally different arguments, but each variant can also be reduced to the other variants in its row. Additionally, each result in the top row can be deduced from the one below it in the same column.

| Algebraic topology | Combinatorics | Set covering |
|---|---|---|
| Brouwer fixed-point theorem | Sperner's lemma | Knaster–Kuratowski–Mazurkiewicz lemma |
| Borsuk–Ulam theorem | Tucker's lemma | Lusternik–Schnirelmann theorem |

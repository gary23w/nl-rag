---
title: "Simplicial complex"
source: https://en.wikipedia.org/wiki/Simplicial_complex
domain: algebraic-topology
license: CC-BY-SA-4.0
tags: algebraic topology, homotopy theory, homology group, fundamental group
fetched: 2026-07-02
---

# Simplicial complex

In mathematics, a **simplicial complex** is a structured set of *simplices* (for example, points, line segments, triangles, and their *n*-dimensional counterparts) such that all the faces and intersections of the elements are also included in the set (see illustration). Simplicial complexes should not be confused with the more abstract notion of a simplicial set appearing in modern simplicial homotopy theory. The purely combinatorial counterpart to a simplicial complex is an abstract simplicial complex. To distinguish a simplicial complex from an abstract simplicial complex, the former is often called a **geometric simplicial complex**.

## Definitions

A **simplicial complex** ${\mathcal {K}}$ is a set of simplices that satisfies the following conditions:

1. Every face of a simplex from ${\mathcal {K}}$ is also in ${\mathcal {K}}$ .
2. The non-empty intersection of any two simplices $\sigma _{1},\sigma _{2}\in {\mathcal {K}}$ is a face of both $\sigma _{1}$ and $\sigma _{2}$ .

See also the definition of an abstract simplicial complex, which loosely speaking is a simplicial complex without an associated geometry.

A **simplicial *k*-complex** ${\mathcal {K}}$ is a simplicial complex where the largest dimension of any simplex in ${\mathcal {K}}$ equals *k*. For instance, a simplicial 2-complex must contain at least one triangle, and must not contain any tetrahedra or higher-dimensional simplices.

A **pure** or **homogeneous** simplicial *k*-complex ${\mathcal {K}}$ is a simplicial complex where every simplex of dimension less than *k* is a face of some simplex $\sigma \in {\mathcal {K}}$ of dimension exactly *k*. Informally, a pure 1-complex "looks" like it's made of a bunch of lines, a 2-complex "looks" like it's made of a bunch of triangles, etc. An example of a *non*-homogeneous complex is a triangle with a line segment attached to one of its vertices. Pure simplicial complexes can be thought of as triangulations and provide a definition of polytopes.

A **facet** is a maximal simplex, i.e., any simplex in a complex that is *not* a face of any larger simplex. (Note the difference from a "face" of a simplex). A pure simplicial complex can be thought of as a complex where all facets have the same dimension. For (boundary complexes of) simplicial polytopes this coincides with the meaning from polyhedral combinatorics.

Sometimes the term *face* is used to refer to a simplex of a complex, not to be confused with a face of a simplex.

For a simplicial complex embedded in a *k*-dimensional space, the *k*-faces are sometimes referred to as its **cells**. The term *cell* is sometimes used in a broader sense to denote a set homeomorphic to a simplex, leading to the definition of cell complex.

The **underlying space**, sometimes called the **carrier** of a simplicial complex, is the union of its simplices. It is usually denoted by $|{\mathcal {K}}|$ or $\|{\mathcal {K}}\|$ .

## Support

The relative interiors of all simplices in ${\mathcal {K}}$ form a partition of its underlying space $|{\mathcal {K}}|$ : for each point $x\in |{\mathcal {K}}|$ , there is exactly one simplex in ${\mathcal {K}}$ containing x in its relative interior. This simplex is called the **support** of *x* and denoted $\operatorname {supp} (x)$ .

## Closure, star, and link

- (Two simplices and their closure.) Two simplices and their **closure**.
- (A vertex and its star.) A vertex and its **star**.
- (A vertex and its link.) A vertex and its **link**.

Let *K* be a simplicial complex and let *S* be a collection of simplices in *K*.

The **closure** of *S* (denoted $\mathrm {Cl} \ S$ ) is the smallest simplicial subcomplex of *K* that contains each simplex in *S*. $\mathrm {Cl} \ S$ is obtained by repeatedly adding to *S* each face of every simplex in *S*.

The **star** of *S* (denoted $\mathrm {st} \ S$ ) is the union of the stars of each simplex in *S*. For a single simplex *s*, the star of *s* is the set of simplices in *K* that have *s* as a face. The star of *S* is generally not a simplicial complex itself, so some authors define the **closed star** of S (denoted $\mathrm {St} \ S$ ) as $\mathrm {Cl} \ \mathrm {st} \ S$ the closure of the star of S.

The **link** of *S* (denoted $\mathrm {Lk} \ S$ ) equals $\mathrm {Cl} {\big (}\mathrm {st} (S){\big )}\setminus \mathrm {st} {\big (}\mathrm {Cl} (S){\big )}$ . It is the closed star of *S* minus the stars of all faces of *S*.

## Algebraic topology

In algebraic topology, simplicial complexes are often useful for concrete calculations. For the definition of homology groups of a simplicial complex, one can read the corresponding chain complex directly, provided that consistent orientations are made of all simplices. The requirements of homotopy theory lead to the use of more general spaces, the CW complexes. Infinite complexes are a technical tool basic in algebraic topology. In algebraic topology, a compact topological space which is homeomorphic to the geometric realization of a finite simplicial complex is usually called a polyhedron (see Spanier 1966, Maunder 1996, Hilton & Wylie 1967).

## Combinatorics

Combinatorialists often study the ***f*-vector** of a simplicial d-complex Δ, which is the integer sequence $(f_{0},f_{1},f_{2},\ldots ,f_{d+1})$ , where *f**i* is the number of (*i*−1)-dimensional faces of Δ (by convention, *f*0 = 1 unless Δ is the empty complex). For instance, if Δ is the boundary of the octahedron, then its *f*-vector is (1, 6, 12, 8), and if Δ is the first simplicial complex pictured above, its *f*-vector is (1, 18, 23, 8, 1). A complete characterization of the possible *f*-vectors of simplicial complexes is given by the Kruskal–Katona theorem.

By using the *f*-vector of a simplicial *d*-complex Δ as coefficients of a polynomial (written in decreasing order of exponents), we obtain the **f-polynomial** of Δ. In our two examples above, the *f*-polynomials would be $x^{3}+6x^{2}+12x+8$ and $x^{4}+18x^{3}+23x^{2}+8x+1$ , respectively.

Combinatorists are often quite interested in the **h-vector** of a simplicial complex Δ, which is the sequence of coefficients of the polynomial that results from plugging *x* − 1 into the *f*-polynomial of Δ. Formally, if we write *F*Δ(*x*) to mean the *f*-polynomial of Δ, then the **h-polynomial** of Δ is

$F_{\Delta }(x-1)=h_{0}x^{d+1}+h_{1}x^{d}+h_{2}x^{d-1}+\cdots +h_{d}x+h_{d+1}$

and the *h*-vector of Δ is

$(h_{0},h_{1},h_{2},\cdots ,h_{d+1}).$

We calculate the h-vector of the octahedron boundary (our first example) as follows:

$F(x-1)=(x-1)^{3}+6(x-1)^{2}+12(x-1)+8=x^{3}+3x^{2}+3x+1.$

So the *h*-vector of the boundary of the octahedron is (1, 3, 3, 1). It is not an accident this *h*-vector is symmetric. In fact, this happens whenever Δ is the boundary of a simplicial polytope (these are the Dehn–Sommerville equations). In general, however, the *h*-vector of a simplicial complex is not even necessarily positive. For instance, if we take Δ to be the 2-complex given by two triangles intersecting only at a common vertex, the resulting *h*-vector is (1, 3, −2).

A complete characterization of all simplicial polytope *h*-vectors is given by the celebrated g-theorem of Stanley, Billera, and Lee.

Simplicial complexes can be seen to have the same geometric structure as the contact graph of a sphere packing (a graph where vertices are the centers of spheres and edges exist if the corresponding packing elements touch each other) and as such can be used to determine the combinatorics of sphere packings, such as the number of touching pairs (1-simplices), touching triplets (2-simplices), and touching quadruples (3-simplices) in a sphere packing.

## Triangulation

A triangulation of a topological space X is a homeomorphism $t:|{\mathcal {T}}|\rightarrow X$ where ${\mathcal {T}}$ is a simplicial complex.

Topological spaces do not necessarily admit a triangulation and if they do, it is never unique. Topological manifolds of dimension $d\leq 3$ are always triangulable, but not necessarily for $d>3$ .

Differentiable manifolds of any dimension $d\geq 1$ admit triangulations.

## Embedding

Any abstract d -dimensional simplicial complex can be embedded in a $(2d+1)$ -dimensional space. This result is piecewise linear counterpart of the (weak) Whitney embedding theorem.

## Computational problems

The simplicial complex recognition problem is: given a finite simplicial complex, decide whether it is homeomorphic to a given geometric object. This problem is undecidable for any *d*-dimensional manifolds for $d\geq 5$ .

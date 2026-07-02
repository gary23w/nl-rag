---
title: "Convex set"
source: https://en.wikipedia.org/wiki/Convex_set
domain: convex-geometry
license: CC-BY-SA-4.0
tags: convex geometry, convex polytope, supporting hyperplane, helly's theorem
fetched: 2026-07-02
---

# Convex set

In geometry, a set of points is **convex** if it contains every line segment between two points in the set. For example, a solid cube is a convex set, but anything that is hollow or has an indent, such as a crescent shape, is not convex.

The boundary of a convex set in the plane is always a convex curve. The intersection of all the convex sets that contain a given subset A of Euclidean space is called the convex hull of A. It is the smallest convex set containing A.

A convex function is a real-valued function defined on an interval with the property that its epigraph (the set of points on or above the graph of the function) is a convex set. Convex minimization is a subfield of optimization that studies the problem of minimizing convex functions over convex sets. The branch of mathematics devoted to the study of properties of convex sets and convex functions is called convex analysis.

Spaces in which convex sets are defined include the Euclidean spaces, the affine spaces over the real numbers, and certain non-Euclidean geometries.

## Definitions

Let S be a vector space or an affine space over the real numbers, or, more generally, over some ordered field (this includes Euclidean spaces, which are affine spaces). A subset C of S is convex if, for all x and y in C, the line segment connecting x and y is included in C.

This means that the affine combination (1 − *t*)*x* + *ty* belongs to C for all x,y in C and t in the interval [0, 1]. This implies that convexity is invariant under affine transformations. Further, it implies that a convex set in a real or complex topological vector space is path-connected (and therefore also connected).

A set C is **strictly convex** if for every x and y in C, every point on the line segment connecting x and y other than the endpoints is inside the topological interior of C. A closed convex subset is strictly convex if and only if every one of its boundary points is an extreme point.

A set C is absolutely convex if it is convex and balanced.

### Examples

The convex subsets of **R** (the set of real numbers) are the intervals and the points of **R**. Some examples of convex subsets of the Euclidean plane are solid regular polygons, solid triangles, and intersections of solid triangles. Some examples of convex subsets of a Euclidean 3-dimensional space are the Archimedean solids and the Platonic solids. The Kepler-Poinsot polyhedra are examples of non-convex sets.

### Non-convex set

A set that is not convex is called a *non-convex set*. A polygon that is not a convex polygon is sometimes called a concave polygon, and some sources more generally use the term *concave set* to mean a non-convex set, but most authorities prohibit this usage.

The complement of a convex set, such as the epigraph of a concave function, is sometimes called a *reverse convex set*, especially in the context of mathematical optimization.

## Properties

Given r points *u*1, ..., *ur* in a convex set S, and r nonnegative numbers *λ*1, ..., *λr* such that *λ*1 + ... + *λr* = 1, the affine combination $\sum _{k=1}^{r}\lambda _{k}u_{k}$ belongs to S. As the definition of a convex set is the case *r* = 2, this property characterizes convex sets.

Such an affine combination is called a convex combination of *u*1, ..., *ur*. The **convex hull** of a subset S of a real vector space is defined as the intersection of all convex sets that contain S. More concretely, the convex hull is the set of all convex combinations of points in S. In particular, this is a convex set.

A *(bounded) convex polytope* is the convex hull of a finite subset of some Euclidean space **R***n*.

### Intersections and unions

The collection of convex subsets of a vector space, an affine space, or a Euclidean space has the following properties:

1. The empty set and the whole space are convex.
2. The intersection of any collection of convex sets is convex.
3. The *union* of a collection of convex sets is convex if those sets form a chain (a totally ordered set) under inclusion. For this property, the restriction to chains is important, as the union of two convex sets need not be convex.

### Closed convex sets

Closed convex sets are convex sets that contain all their limit points. They can be characterised as the intersections of *closed half-spaces* (sets of points in space that lie on and to one side of a hyperplane).

From what has just been said, it is clear that such intersections are convex, and they will also be closed sets. To prove the converse, i.e., every closed convex set may be represented as such intersection, one needs the supporting hyperplane theorem in the form that for a given closed convex set C and point P outside it, there is a closed half-space H that contains C and not P. The supporting hyperplane theorem is a special case of the Hahn–Banach theorem of functional analysis.

### Face of a convex set

A **face** of a convex set C is a convex subset F of C such that whenever a point p in F lies strictly between two points x and y in C , both x and y must be in F . Equivalently, for any $x,y\in C$ and any real number $0<t<1$ such that $(1-t)x+ty$ is in F , x and y must be in F . According to this definition, C itself and the empty set are faces of C ; these are sometimes called the *trivial faces* of C . An **extreme point** of C is a point that is a face of C .

Let C be a convex set in $\mathbb {R} ^{n}$ that is compact (or equivalently, closed and bounded). Then C is the convex hull of its extreme points. More generally, each compact convex set in a locally convex topological vector space is the closed convex hull of its extreme points (the Krein–Milman theorem).

For example:

- A triangle in the plane (including the region inside) is a compact convex set. Its nontrivial faces are the three vertices and the three edges. (So the only extreme points are the three vertices.)
- The only nontrivial faces of the closed unit disk $\{(x,y)\in \mathbb {R} ^{2}:x^{2}+y^{2}\leq 1\}$ are its extreme points, namely the points on the unit circle $S^{1}=\{(x,y)\in \mathbb {R} ^{2}:x^{2}+y^{2}=1\}$ .

### Convex sets and rectangles

Let C be a convex body in the plane (a convex set whose interior is non-empty). We can inscribe a rectangle *r* in C such that a homothetic copy *R* of *r* is circumscribed about C. The positive homothety ratio is at most 2 and: ${\tfrac {1}{2}}\cdot \operatorname {Area} (R)\leq \operatorname {Area} (C)\leq 2\cdot \operatorname {Area} (r)$

### Blaschke-Santaló diagrams

The set ${\mathcal {K}}^{2}$ of all planar convex bodies can be parameterized in terms of the convex body diameter *D*, its inradius *r* (the biggest circle contained in the convex body) and its circumradius *R* (the smallest circle containing the convex body). In fact, this set can be described by the set of inequalities given by $2r\leq D\leq 2R$ $R\leq {\frac {\sqrt {3}}{3}}D$ $r+R\leq D$ $D^{2}{\sqrt {4R^{2}-D^{2}}}\leq 2R(2R+{\sqrt {4R^{2}-D^{2}}})$ and can be visualized as the image of the function *g* that maps a convex body to the **R**2 point given by (*r*/*R*, *D*/2*R*). The image of this function is known a (*r*, *D*, *R*) Blachke-Santaló diagram.

Alternatively, the set ${\mathcal {K}}^{2}$ can also be parametrized by its width (the smallest distance between any two different parallel support hyperplanes), perimeter and area.

### Other properties

Let *X* be a topological vector space and $C\subseteq X$ be convex.

- $\operatorname {Cl} C$ and $\operatorname {Int} C$ are both convex (i.e. the closure and interior of convex sets are convex).
- If $a\in \operatorname {Int} C$ and $b\in \operatorname {Cl} C$ then $[a,b[\,\subseteq \operatorname {Int} C$ (where $[a,b[\,:=\left\{(1-r)a+rb:0\leq r<1\right\}$ ).
- If $\operatorname {Int} C\neq \emptyset$ then:
  - $\operatorname {cl} \left(\operatorname {Int} C\right)=\operatorname {Cl} C$ , and
  - $\operatorname {Int} C=\operatorname {Int} \left(\operatorname {Cl} C\right)=C^{i}$ , where $C^{i}$ is the algebraic interior of *C*.

## Convex hulls and Minkowski sums

### Convex hulls

Every subset A of the vector space is contained within a smallest convex set (called the *convex hull* of A), namely the intersection of all convex sets containing A. The convex-hull operator Conv() has the characteristic properties of a closure operator:

- *extensive*: *S* ⊆ Conv(*S*),
- *non-decreasing*: *S* ⊆ *T* implies that Conv(*S*) ⊆ Conv(*T*), and
- *idempotent*: Conv(Conv(*S*)) = Conv(*S*).

The convex-hull operation is needed for the set of convex sets to form a lattice, in which the "*join*" operation is the convex hull of the union of two convex sets $\operatorname {Conv} (S)\vee \operatorname {Conv} (T)=\operatorname {Conv} (S\cup T)=\operatorname {Conv} {\bigl (}\operatorname {Conv} (S)\cup \operatorname {Conv} (T){\bigr )}.$ The intersection of any collection of convex sets is itself convex, so the convex subsets of a (real or complex) vector space form a complete lattice.

### Minkowski addition

In a real vector-space, the *Minkowski sum* of two (non-empty) sets, *S*1 and *S*2, is defined to be the set *S*1 + *S*2 formed by the addition of vectors element-wise from the summand-sets $S_{1}+S_{2}=\{x_{1}+x_{2}:x_{1}\in S_{1},x_{2}\in S_{2}\}.$ More generally, the *Minkowski sum* of a finite family of (non-empty) sets *Sn* is the set formed by element-wise addition of vectors $\sum _{n}S_{n}=\left\{\sum _{n}x_{n}:x_{n}\in S_{n}\right\}.$

For Minkowski addition, the *zero set* {0} containing only the zero vector 0 has special importance: For every non-empty subset S of a vector space $S+\{0\}=S;$ in algebraic terminology, {0} is the identity element of Minkowski addition (on the collection of non-empty sets).

### Convex hulls of Minkowski sums

Minkowski addition behaves well with respect to the operation of taking convex hulls, as shown by the following proposition:

Let *S*1, *S*2 be subsets of a real vector-space, the convex hull of their Minkowski sum is the Minkowski sum of their convex hulls $\operatorname {Conv} (S_{1}+S_{2})=\operatorname {Conv} (S_{1})+\operatorname {Conv} (S_{2}).$

This result holds more generally for each finite collection of non-empty sets: ${\text{Conv}}\left(\sum _{n}S_{n}\right)=\sum _{n}{\text{Conv}}\left(S_{n}\right).$

In mathematical terminology, the operations of Minkowski summation and of forming convex hulls are commuting operations.

### Minkowski sums of convex sets

The Minkowski sum of two compact convex sets is compact. The sum of a compact convex set and a closed convex set is closed.

The following famous theorem, proved by Dieudonné in 1966, gives a sufficient condition for the difference of two closed convex subsets to be closed. It uses the concept of a **recession cone** of a non-empty convex subset *S*, defined as: $\operatorname {rec} S=\left\{x\in X\,:\,x+S\subseteq S\right\},$ where this set is a convex cone containing $0\in X$ and satisfying $S+\operatorname {rec} S=S$ . Note that if *S* is closed and convex then $\operatorname {rec} S$ is closed and for all $s_{0}\in S$ , $\operatorname {rec} S=\bigcap _{t>0}t(S-s_{0}).$

**Theorem** (Dieudonné). Let *A* and *B* be non-empty, closed, and convex subsets of a locally convex topological vector space such that $\operatorname {rec} A\cap \operatorname {rec} B$ is a linear subspace. If *A* or *B* is locally compact then *A* − *B* is closed.

## Generalizations and extensions for convexity

The notion of convexity in the Euclidean space may be generalized by modifying the definition in some or other aspects. The common name "generalized convexity" is used, because the resulting objects retain certain properties of convex sets.

### Star-convex (star-shaped) sets

Let C be a set in a real or complex vector space. C is **star convex (star-shaped)** if there exists an *x*0 in C such that the line segment from *x*0 to any point y in C is contained in C. Hence a non-empty convex set is always star-convex but a star-convex set is not always convex.

### Orthogonal convexity

An example of generalized convexity is **orthogonal convexity**.

A set S in the Euclidean space is called **orthogonally convex** or **ortho-convex**, if any segment parallel to any of the coordinate axes connecting two points of S lies totally within S. It is easy to prove that an intersection of any collection of orthoconvex sets is orthoconvex. Some other properties of convex sets are valid as well.

### Non-Euclidean geometry

The definition of a convex set and a convex hull extends naturally to geometries which are not Euclidean by defining a geodesically convex set to be one that contains the geodesics joining any two points in the set.

### Order topology

Convexity can be extended for a totally ordered set X endowed with the order topology.

Let *Y* ⊆ *X*. The subspace Y is a convex set if for each pair of points *a*, *b* in Y such that *a* ≤ *b*, the interval [*a*, *b*] = {*x* ∈ *X* | *a* ≤ *x* ≤ *b*} is contained in Y. That is, Y is convex if and only if for all *a*, *b* in Y, *a* ≤ *b* implies [*a*, *b*] ⊆ *Y*.

A convex set is *not* connected in general: a counter-example is given by the subspace {1,2,3} in **Z**, which is both convex and not connected.

### Convexity spaces

The notion of convexity may be generalised to other objects, if certain properties of convexity are selected as axioms.

Given a set X, a **convexity** over X is a collection *𝒞* of subsets of X satisfying the following axioms:

1. The empty set and X are in *𝒞*.
2. The intersection of any collection from *𝒞* is in *𝒞*.
3. The union of a chain (with respect to the inclusion relation) of elements of *𝒞* is in *𝒞*.

The elements of *𝒞* are called convex sets and the pair (*X*, *𝒞*) is called a **convexity space**. For the ordinary convexity, the first two axioms hold, and the third one is trivial.

For an alternative definition of abstract convexity, more suited to discrete geometry, see the *convex geometries* associated with antimatroids.

### Convex spaces

Convexity can be generalised as an abstract algebraic structure: a space is convex if it is possible to take convex combinations of points.

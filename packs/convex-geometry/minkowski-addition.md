---
title: "Minkowski addition"
source: https://en.wikipedia.org/wiki/Minkowski_addition
domain: convex-geometry
license: CC-BY-SA-4.0
tags: convex geometry, convex polytope, supporting hyperplane, helly's theorem
fetched: 2026-07-02
---

# Minkowski addition

In mathematics, the **sumset** of two subsets A and B of an (additive) abelian group is formed by adding each element of A to each element of B: $A+B=\{a+b\mid a\in A,\ b\in B\}.$

In geometry, the **Minkowski sum** of two subsets A and B of a Euclidean space is the set of the points whose position vectors form the sumset of the position vectors of A and B. The Minkowski sum depends on the choice of an origin in the Euclidean space. As a change of origin amounts to translate the Minkowski sum, the Minkowski sum is defined up to a translation, and its shape and orientation are well defined.

The **Minkowski difference** (also *Minkowski subtraction*, *Minkowski decomposition*, or *geometric difference*) is the corresponding inverse, where ${\textstyle (A-B)}$ produces a set that could be summed with *B* to recover *A*. This is defined as the complement of the Minkowski sum of the complement of *A* with the reflection of *B* about the origin.

${\begin{aligned}-B&=\{\mathbf {-b} \,|\,\mathbf {b} \in B\}\\A-B&=(A^{\complement }+(-B))^{\complement }\end{aligned}}$

This definition allows a symmetrical relationship between the Minkowski sum and difference. Note that alternately taking the sum and difference with *B* is not necessarily equivalent. The sum can fill gaps which the difference may not re-open, and the difference can erase small islands which the sum cannot recreate from nothing.

${\begin{aligned}(A-B)+B&\subseteq A\\(A+B)-B&\supseteq A\\A-B&=(A^{\complement }+(-B))^{\complement }\\A+B&=(A^{\complement }-(-B))^{\complement }\\\end{aligned}}$

In 2D image processing the Minkowski sum and difference are known as dilation and erosion.

An alternative definition of the Minkowski difference is sometimes used for computing intersection of convex shapes. This is not equivalent to the previous definition, and is not an inverse of the sum operation. Instead it replaces the vector addition of the Minkowski sum with a vector subtraction. If the two convex shapes intersect, the resulting set will contain the origin.

$A-B=\{\mathbf {a} -\mathbf {b} \,|\,\mathbf {a} \in A,\ \mathbf {b} \in B\}=A+(-B)$

The concept is named for Hermann Minkowski.

## Example

For example, if we have two sets *A* and *B*, each consisting of three position vectors (informally, three points), representing the vertices of two triangles in ${\textstyle \mathbb {R} ^{2}}$ , with coordinates

$A=\{(1,0),(0,1),(0,-1)\}$

and

$B=\{(0,0),(1,1),(1,-1)\}$

then their Minkowski sum is

$A+B=\{(1,0),(2,1),(2,-1),(0,1),(1,2),(1,0),(0,-1),(1,0),(1,-2)\},$

which comprises the vertices of a hexagon and its center.

For Minkowski addition, the *zero set*, ${\textstyle \{0\},}$ containing only the zero vector, 0, is an identity element: for every subset *S* of a vector space,

$S+\{0\}=S.$

The empty set is important in Minkowski addition, because the empty set annihilates every other subset: for every subset *S* of a vector space, its sum with the empty set is empty:

$S+\emptyset =\emptyset .$

For another example, consider the Minkowski sums of open or closed balls in the field ${\textstyle \mathbb {K} ,}$ which is either the real numbers ${\textstyle \mathbb {R} }$ or complex numbers ${\textstyle \mathbb {C} }$ . If ${\textstyle B_{r}:=\{s\in \mathbb {K}$ is the closed ball of radius ${\textstyle r\in [0,\infty ]}$ centered at ${\textstyle 0}$ in ${\textstyle \mathbb {K} }$ then for any ${\textstyle r,s\in [0,\infty ]}$ , ${\textstyle B_{r}+B_{s}=B_{r+s}}$ and also ${\textstyle cB_{r}=B_{|c|r}}$ will hold for any scalar ${\textstyle c\in \mathbb {K} }$ such that the product ${\textstyle |c|r}$ is defined (which happens when ${\textstyle c\neq 0}$ or ${\textstyle r\neq \infty }$ ). If ${\textstyle r}$ , ${\textstyle s}$ , and ${\textstyle c}$ are all non-zero then the same equalities would still hold had ${\textstyle B_{r}}$ been defined to be the open ball, rather than the closed ball, centered at 0 (the non-zero assumption is needed because the open ball of radius 0 is the empty set). The Minkowski sum of a closed ball and an open ball is an open ball. More generally, the Minkowski sum of an open subset with *any* other set will be an open subset.

If ${\textstyle G=\{(x,1/x):0\neq x\in \mathbb {R} \}}$ is the graph of ${\textstyle f(x)={\frac {1}{x}}}$ and if and ${\textstyle Y=\{0\}\times \mathbb {R} }$ is the ${\textstyle y}$ -axis in ${\textstyle X=\mathbb {R} ^{2}}$ then the Minkowski sum of these two closed subsets of the plane is the open set ${\textstyle G+Y=\{(x,y)\in \mathbb {R} ^{2}:x\neq 0\}=\mathbb {R} ^{2}\setminus Y}$ consisting of everything other than the ${\textstyle y}$ -axis. This shows that the Minkowski sum of two closed sets is not necessarily a closed set. However, the Minkowski sum of two closed subsets will be a closed subset if at least one of these sets is also a compact subset.

## Convex hulls of Minkowski sums

Minkowski addition behaves well with respect to the operation of taking convex hulls, as shown by the following proposition:

For all non-empty subsets

${\textstyle S_{1}}$

and

${\textstyle S_{2}}$

of a real vector space, the convex hull of their Minkowski sum is the Minkowski sum of their convex hulls:

$\operatorname {Conv} (S_{1}+S_{2})=\operatorname {Conv} (S_{1})+\operatorname {Conv} (S_{2}).$

This result holds more generally for any finite collection of non-empty sets:

$\operatorname {Conv} \left(\sum {S_{n}}\right)=\sum \operatorname {Conv} (S_{n}).$

In mathematical terminology, the operations of Minkowski summation and of forming convex hulls are commuting operations.

If ${\textstyle S}$ is a convex set then $\mu S+\lambda S$ is also a convex set; furthermore

$\mu S+\lambda S=(\mu +\lambda )S$

for every ${\textstyle \mu ,\lambda \geq 0}$ . Conversely, if this "distributive property" holds for all non-negative real numbers, ${\textstyle \mu }$ and ${\textstyle \lambda }$ , then the set is convex.

The figure to the right shows an example of a non-convex set for which ${\textstyle 2A\subsetneq A+A.}$

An example in one dimension is: ${\textstyle B=[1,2]\cup [4,5].}$ It can be easily calculated that ${\textstyle 2B=[2,4]\cup [8,10]}$ but ${\textstyle B+B=[2,4]\cup [5,7]\cup [8,10],}$ hence again ${\textstyle 2B\subsetneq B+B.}$

Minkowski sums act linearly on the perimeter of two-dimensional convex bodies: the perimeter of the sum equals the sum of perimeters. Additionally, if ${\textstyle K}$ is (the interior of) a curve of constant width, then the Minkowski sum of ${\textstyle K}$ and of its 180° rotation is a disk. These two facts can be combined to give a short proof of Barbier's theorem on the perimeter of curves of constant width.

## Applications

Minkowski addition plays a central role in mathematical morphology. It arises in the brush-and-stroke paradigm of 2D computer graphics (with various uses, notably by Donald E. Knuth in Metafont), and as the solid sweep operation of 3D computer graphics. It has also been shown to be closely connected to the Earth mover's distance, and by extension, optimal transport.

### Motion planning

Minkowski sums are used in motion planning of an object among obstacles. They are used for the computation of the configuration space, which is the set of all admissible positions of the object. In the simple model of translational motion of an object in the plane, where the position of an object may be uniquely specified by the position of a fixed point of this object, the configuration space are the Minkowski sum of the set of obstacles and the movable object placed at the origin and rotated 180 degrees.

### Numerical control (NC) machining

In numerical control machining, the programming of the NC tool exploits the fact that the Minkowski sum of the cutting piece with its trajectory gives the shape of the cut in the material.

### 3D solid modeling

In OpenSCAD Minkowski sums are used to outline a shape with another shape creating a composite of both shapes.

### Aggregation theory

Minkowski sums are also frequently used in aggregation theory when individual objects to be aggregated are characterized via sets.

### Collision detection

Minkowski sums, specifically Minkowski differences, are often used alongside GJK algorithms to compute collision detection for convex hulls in physics engines.

## Algorithms for computing Minkowski sums

### Planar case

#### Two convex polygons in the plane

For two convex polygons *P* and *Q* in the plane with *m* and *n* vertices, their Minkowski sum is a convex polygon with at most *m* + *n* vertices and may be computed in time O(*m* + *n*) by a very simple procedure, which may be informally described as follows. Assume that the edges of a polygon are given and the direction, say, counterclockwise, along the polygon boundary. Then it is easily seen that these edges of the convex polygon are ordered by polar angle. Let us merge the ordered sequences of the directed edges from *P* and *Q* into a single ordered sequence *S*. Imagine that these edges are solid arrows which can be moved freely while keeping them parallel to their original direction. Assemble these arrows in the order of the sequence *S* by attaching the tail of the next arrow to the head of the previous arrow. It turns out that the resulting polygonal chain will in fact be a convex polygon which is the Minkowski sum of *P* and *Q*.

#### Other

If one polygon is convex and another one is not, the complexity of their Minkowski sum is O(*nm*). If both of them are nonconvex, their Minkowski sum complexity is O((*mn*)2).

## Essential Minkowski sum

There is also a notion of the **essential Minkowski sum** +e of two subsets of Euclidean space. The usual Minkowski sum can be written as

$A+B=\left\{z\in \mathbb {R} ^{n}\,|\,A\cap (z-B)\neq \emptyset \right\}.$

Thus, the **essential Minkowski sum** is defined by

$A+_{\mathrm {e} }B=\left\{z\in \mathbb {R} ^{n}\,|\,\mu \left[A\cap (z-B)\right]>0\right\},$

where *μ* denotes the *n*-dimensional Lebesgue measure. The reason for the term "essential" is the following property of indicator functions: while

$1_{A\,+\,B}(z)=\sup _{x\,\in \,\mathbb {R} ^{n}}1_{A}(x)1_{B}(z-x),$

it can be seen that

$1_{A\,+_{\mathrm {e} }\,B}(z)=\mathop {\mathrm {ess\,sup} } _{x\,\in \,\mathbb {R} ^{n}}1_{A}(x)1_{B}(z-x),$

where "ess sup" denotes the essential supremum.

## *Lp* Minkowski sum

For *K* and *L* compact convex subsets in ${\textstyle \mathbb {R} ^{n}}$ , the Minkowski sum can be described by the support function of the convex sets:

$h_{K+L}=h_{K}+h_{L}.$

For *p* ≥ 1, Firey defined the ***L**p* Minkowski sum** *K* +*p* *L* of compact convex sets *K* and *L* in $\mathbb {R} ^{n}$ containing the origin as

$h_{K+_{p}L}^{p}=h_{K}^{p}+h_{L}^{p}.$

By the Minkowski inequality, the function *hK+pL* is again positive homogeneous and convex and hence the support function of a compact convex set. This definition is fundamental in the *L**p* Brunn-Minkowski theory.

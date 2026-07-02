---
title: "Extreme point"
source: https://en.wikipedia.org/wiki/Extreme_point
domain: gift-wrapping
license: CC-BY-SA-4.0
tags: gift wrapping algorithm, jarvis march, convex hull output, beneath beyond
fetched: 2026-07-02
---

# Extreme point

In mathematics, an **extreme point** of a convex set S in a real or complex vector space or affine space is a point in S that does not lie in any open line segment joining two points of $S.$ The extreme points of a line segment are called its *endpoints*. In linear programming problems, an extreme point is also called *vertex* or *corner point* of $S.$

## Definition

Throughout, it is assumed that X is a real or complex vector space or affine space.

For any $p,x,y\in X,$ say that p **lies between** x and y if $x\neq y$ and there exists a $0<t<1$ such that $p=tx+(1-t)y.$

If K is a subset of X and $p\in K,$ then p is called an **extreme point** of K if it does not lie between any two *distinct* points of $K.$ That is, if there does *not* exist $x,y\in K$ and $0<t<1$ such that $x\neq y$ and $p=tx+(1-t)y.$ The set of all extreme points of K is denoted by $\operatorname {extreme} (K).$

**Generalizations**

If S is a subset of a vector space then a linear sub-variety (that is, an affine subspace) A of the vector space is called a *support variety* if A meets S (that is, $A\cap S$ is not empty) and every open segment $I\subseteq S$ whose interior meets A is necessarily a subset of $A.$ A 0-dimensional support variety is called an extreme point of $S.$

### Characterizations

The **midpoint** of two elements x and y in a vector space is the vector ${\tfrac {1}{2}}(x+y).$

For any elements x and y in a vector space, the set $[x,y]=\{tx+(1-t)y:0\leq t\leq 1\}$ is called the **closed line segment** or **closed interval** between x and $y.$ The **open line segment** or **open interval** between x and y is $(x,x)=\varnothing$ when $x=y$ while it is $(x,y)=\{tx+(1-t)y:0<t<1\}$ when $x\neq y.$ The points x and y are called the **endpoints** of these interval. An interval is said to be a **non−degenerate interval** or a **proper interval** if its endpoints are distinct. The **midpoint of an interval** is the midpoint of its endpoints.

The closed interval $[x,y]$ is equal to the convex hull of $(x,y)$ if (and only if) $x\neq y.$ So if K is convex and $x,y\in K,$ then $[x,y]\subseteq K.$

If K is a nonempty subset of X and F is a nonempty subset of $K,$ then F is called a **face** of K if whenever a point $p\in F$ lies between two points of $K,$ then those two points necessarily belong to $F.$

**Theorem**—Let K be a non-empty convex subset of a vector space X and let $p\in K.$ Then the following statements are equivalent:

1. p is an extreme point of $K.$
2. $K\setminus \{p\}$ is convex.
3. p is not the midpoint of a non-degenerate line segment contained in $K.$
4. for any $x,y\in K,$ if $p\in [x,y]$ then $x=p{\text{ or }}y=p.$
5. if $x\in X$ is such that both $p+x$ and $p-x$ belong to $K,$ then $x=0.$
6. $\{p\}$ is a face of $K.$

## Examples

If $a<b$ are two real numbers then a and b are extreme points of the interval $[a,b].$ However, the open interval $(a,b)$ has no extreme points. Any open interval in $\mathbb {R}$ has no extreme points while any non-degenerate closed interval not equal to $\mathbb {R}$ does have extreme points (that is, the closed interval's endpoint(s)). More generally, any open subset of finite-dimensional Euclidean space $\mathbb {R} ^{n}$ has no extreme points.

The extreme points of the closed unit disk in $\mathbb {R} ^{2}$ is the unit circle.

The perimeter of any convex polygon in the plane is a face of that polygon. The vertices of any convex polygon in the plane $\mathbb {R} ^{2}$ are the extreme points of that polygon.

An injective linear map $F:X\to Y$ sends the extreme points of a convex set $C\subseteq X$ to the extreme points of the convex set $F(X).$ This is also true for injective affine maps.

## Properties

The extreme points of a compact convex set form a Baire space (with the subspace topology) but this set may *fail* to be closed in $X.$

## Theorems

### Krein–Milman theorem

The Krein–Milman theorem is arguably one of the most well-known theorems about extreme points.

**Theorem**—If S is convex and compact in a locally convex topological vector space, then S is the closed convex hull of its extreme points: In particular, such a set has extreme points.

### For Banach spaces

These theorems are for Banach spaces with the Radon–Nikodym property.

A theorem of Joram Lindenstrauss states that, in a Banach space with the Radon–Nikodym property, a nonempty closed and bounded set has an extreme point. (In infinite-dimensional spaces, the property of compactness is stronger than the joint properties of being closed and being bounded.)

**Theorem** (Gerald Edgar)—Let E be a Banach space with the Radon–Nikodym property, let C be a separable, closed, bounded, convex subset of $E,$ and let a be a point in $C.$ Then there is a probability measure p on the universally measurable sets in C such that a is the barycenter of $p,$ and the set of extreme points of C has p -measure 1.

Edgar’s theorem implies Lindenstrauss’s theorem.

A closed convex subset of a topological vector space is called *strictly convex* if every one of its (topological) boundary points is an extreme point. The unit ball of any Hilbert space is a strictly convex set.

### *k*-extreme points

More generally, a point in a convex set S is **k -extreme** if it lies in the interior of a k -dimensional convex set within $S,$ but not a $k+1$ -dimensional convex set within $S.$ Thus, an extreme point is also a 0 -extreme point. If S is a polytope, then the k -extreme points are exactly the interior points of the k -dimensional faces of $S.$ More generally, for any convex set $S,$ the k -extreme points are partitioned into k -dimensional open faces.

The finite-dimensional Krein–Milman theorem, which is due to Minkowski, can be quickly proved using the concept of k -extreme points. If S is closed, bounded, and n -dimensional, and if p is a point in $S,$ then p is k -extreme for some $k\leq n.$ The theorem asserts that p is a convex combination of extreme points. If $k=0$ then it is immediate. Otherwise p lies on a line segment in S which can be maximally extended (because S is closed and bounded). If the endpoints of the segment are q and $r,$ then their extreme rank must be less than that of $p,$ and the theorem follows by induction.

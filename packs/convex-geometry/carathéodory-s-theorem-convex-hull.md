---
title: "Carathéodory's theorem (convex hull)"
source: https://en.wikipedia.org/wiki/Carath%C3%A9odory's_theorem_(convex_hull)
domain: convex-geometry
license: CC-BY-SA-4.0
tags: convex geometry, convex polytope, supporting hyperplane, helly's theorem
fetched: 2026-07-02
---

# Carathéodory's theorem (convex hull)

**Carathéodory's theorem** is a theorem in convex geometry. It states that if a point x lies in the convex hull $\mathrm {Conv} (P)$ of a set $P\subset \mathbb {R} ^{d}$ , then x lies in some *d*-dimensional simplex with vertices in P . Equivalently, x can be written as the convex combination of $d+1$ or fewer points in P . Additionally, x can be written as the convex combination of at most $d+1$ *extremal* points in P , as non-extremal points can be removed from P without changing the membership of *x* in the convex hull.

An equivalent theorem for conical combinations states that if a point x lies in the conical hull $\mathrm {Cone} (P)$ of a set $P\subset \mathbb {R} ^{d}$ , then x can be written as the conical combination of at most d points in P .

Two other theorems of Helly and Radon are closely related to Carathéodory's theorem: the latter theorem can be used to prove the former theorems and vice versa.

The result is named for Constantin Carathéodory, who proved the theorem in 1911 for the case when P is compact. In 1914 Ernst Steinitz expanded Carathéodory's theorem for arbitrary sets.

## Example

Carathéodory's theorem in 2 dimensions states that we can construct a triangle consisting of points from *P* that encloses any point in the convex hull of *P*.

For example, let *P* = {(0,0), (0,1), (1,0), (1,1)}. The convex hull of this set is a square. Let *x* = (1/4, 1/4) in the convex hull of *P*. We can then construct a set {(0,0),(0,1),(1,0)} = *P*′, the convex hull of which is a triangle and encloses *x.*

## Proof

**Note:** We will only use the fact that $\mathbb {R}$ is an ordered field, so the theorem and proof works even when $\mathbb {R}$ is replaced by any field $\mathbb {F}$ , together with a total order.

We first formally state Carathéodory's theorem:

**Carathéodory's theorem**—If $x\in \mathrm {Cone} (S)\subset \mathbb {R} ^{d}$ , then x is the nonnegative sum of at most d points of S .

If $x\in \mathrm {Conv} (S)\subset \mathbb {R} ^{d}$ , then x is the convex sum of at most $d+1$ points of S .

The essence of Carathéodory's theorem is in the finite case. This reduction to the finite case is possible because $\mathrm {Conv} (S)$ is the set of *finite* convex combination of elements of S (see the convex hull page for details).

**Lemma**—If $q_{1},...,q_{N}\in \mathbb {R} ^{d}$ then $\forall x\in \mathrm {Cone} (\{q_{1},...,q_{N}\})$ , there exist $w_{1},...,w_{N}\geq 0$ such that $x=\sum _{n}w_{n}q_{n}$ , and at most d of them are nonzero.

With the lemma, Carathéodory's theorem is a simple extension:

Proof of Carathéodory's theorem

For the first part: take any $x\in \mathrm {Cone} (S)$ , represent $x=\sum _{n=1}^{N}w_{n}q_{n}$ for some $q_{1},...,q_{N}\in S$ and $w_{n}\geq 0$ , then $x\in \mathrm {Cone} (\{q_{1},...,q_{N}\})$ , and we use the lemma.

The second part reduces to the first part by "lifting up one dimension", a common trick used to reduce affine geometry to linear algebra, and reduce convex bodies to convex cones.

Explicitly, let $S\subset \mathbb {R} ^{d}$ , then identify $\mathbb {R} ^{d}$ with the subset $\{w\in \mathbb {R} ^{d+1}:w_{d+1}=1\}$ . This induces an embedding of S into $S\times \{1\}\subset \mathbb {R} ^{d+1}$ .

Any $x\in \mathrm {Conv} (S)$ has a representation $x=\sum _{n=1}^{N}w_{n}q_{n}$ , with $\sum _{n=1}^{N}w_{n}=1$ and $w_{n}\geq 0$ ; x has a "lifted" representation $(x,1)=\sum _{n=1}^{N}w_{n}(q_{n},1)$ , and so, by the first part, it has a representation $(x,1)=\sum _{n=1}^{N}w'_{n}(q_{n},1)$ with $w'_{n}\geq 0$ , where at most $d+1$ of $w'_{n}$ are nonzero. That is, $x=\sum _{n=1}^{N}w'_{n}q_{n}$ and $1=\sum _{n=1}^{N}w'_{n}$ , which completes the proof.

Proof of lemma

This is trivial when $N\leq d$ . If we can prove it for all $N=d+1$ , then by induction we have proved it for all $N\geq d+1$ . Thus it remains to prove it for $N=d+1$ . This we prove by induction on d .

Base case: $d=1,N=2$ , trivial.

Induction case. Represent $x=\sum _{n=1}^{d+1}w_{n}q_{n}$ . If some $w_{n}=0$ , then the proof is finished. So assume all $w_{n}>0$

If $\{q_{1},...,q_{d}\}$ is linearly dependent, then we can use induction on its linear span to eliminate one nonzero term in $\sum _{n=1}^{d}{\frac {w_{n}}{w_{1}+\cdots +w_{d}}}q_{n}$ , and thus eliminate it in $x=\sum _{n=1}^{d+1}w_{n}q_{n}$ as well.

Else, there exists $(u_{1},...,u_{d})\in \mathbb {R} ^{d}$ , such that $\sum _{n=1}^{d}u_{n}q_{n}=q_{d+1}$ . Then we can interpolate a full interval of representations:

$x=\sum _{n=1}^{d}(w_{n}+\theta w_{d+1}u_{n})q_{n}+(1-\theta )w_{d+1}q_{d+1};\quad \theta \in [0,1]$

If $w_{n}+w_{d+1}u_{n}\geq 0$ for all $n=1,...,d$ , then set $\theta =1$ . Otherwise, let $\theta$ be the smallest $\theta$ such that one of $w_{n}+\theta w_{d+1}u_{n}=0$ . Then we obtain a representation of x as a linear combination with non-negative coefficients, with at most d nonzero terms.

Alternative proofs use Helly's theorem or the Perron–Frobenius theorem.

## Variants

### Carathéodory's number

For any nonempty $P\subset \mathbb {R} ^{d}$ , define its **Carathéodory's number** to be the smallest integer r , such that for any $x\in \mathrm {Conv} (P)$ , there exists a representation of x as a convex sum of up to r elements in P .

Carathéodory's theorem simply states that any nonempty subset of $\mathbb {R} ^{d}$ has Carathéodory's number $\leq d+1$ . This upper bound is not necessarily reached. For example, the unit sphere in $\mathbb {R} ^{d}$ has Carathéodory's number equal to 2, since any point inside the sphere is the convex sum of two points on the sphere.

With additional assumptions on $P\subset \mathbb {R} ^{d}$ , upper bounds strictly lower than $d+1$ can be obtained.

### Dimensionless variant

Caratheodory's theorem type results where the diameter replaces the dependency on the dimension are well known. An explicit statement of a no-dimensional Caratheodory's theorem was provided by Barman. It is probable that this theorem was stated much earlier, as it is an easy consequence of the analysis of the Perceptron algorithm of Novikoff. Specifically, for every positive integer r and every point within the convex hull of a finite point set P , there exists an r -point subset R such that the given point is within distance $\operatorname {diam} P/{\sqrt {2r}}$ of the convex hull of R .

### Colorful Carathéodory theorem

Let *X*1, ..., *X**d*+1 be sets in **R***d* and let *x* be a point contained in the intersection of the convex hulls of all these *d*+1 sets.

Then there is a set *T* = {*x*1, ..., *x**d*+1}, where *x*1 ∈ *X*1, ..., *x**d*+1 ∈ *X**d*+1, such that the convex hull of *T* contains the point *x*.

By viewing the sets *X*1, ..., *X**d*+1 as different colors, the set *T* is made by points of all colors, hence the "colorful" in the theorem's name. The set *T* is also called a *rainbow simplex*, since it is a *d*-dimensional simplex in which each corner has a different color.

This theorem has a variant in which the convex hull is replaced by the conical hull. Let *X*1, ..., *X**d* be sets in **R**d and let *x* be a point contained in the intersection of the *conical hulls* of all these *d* sets. Then there is a set *T* = {*x*1, ..., *x**d*}, where *x*1 ∈ *X*1, ..., *x**d* ∈ *X**d*, such that the *conical hull* of *T* contains the point *x*.

Mustafa and Ray extended this colorful theorem from points to convex bodies.

The computational problem of finding the colorful set lies in the intersection of the complexity classes PPAD and PLS.

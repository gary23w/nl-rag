---
title: "Metric space (part 1/2)"
source: https://en.wikipedia.org/wiki/Metric_(mathematics)
domain: metrics-cardinality
license: CC-BY-SA-4.0
tags: metric cardinality, label dimensions explosion, time series count, tag value blowup
fetched: 2026-07-02
part: 1/2
---

# Metric space

(Redirected from

Metric (mathematics)

)

In mathematics, a **metric space** is a set together with a notion of distance between its points. The distance is measured by a function called a **metric** or **distance function**. Metric spaces are a general setting for studying many of the concepts of mathematical analysis and geometry.

The most familiar example of a metric space is 3-dimensional Euclidean space with its usual notion of distance. Other well-known examples are a sphere equipped with the angular distance and the hyperbolic plane. A metric may correspond to a metaphorical, rather than physical, notion of distance. For example, the set of 100-character Unicode strings can be equipped with the Hamming distance, which measures the number of characters that need to be changed to get from one string to another.

Metric spaces appear in many different branches of mathematics. For example, Riemannian manifolds, normed vector spaces, and graphs may be viewed as metric spaces. In abstract algebra, the field of *p*-adic numbers is the completion of the field of rational numbers with respect to a certain metric. Metric spaces are also studied in their own right in **metric geometry** and **analysis on metric spaces**.

Many notions of analysis, including balls, completeness, as well as uniform, Lipschitz, and Hölder continuity can be defined for metric spaces. Other notions, such as continuity, compactness, and open and closed sets can be defined for metric spaces, but also in the even more general setting of topological spaces.


## Definition and illustration

### Motivation

To see the utility of different notions of distance, consider the surface of the Earth as a set of points. We can measure the distance between two such points by the length of the shortest path along the surface, "as the crow flies"; this is particularly useful for shipping and aviation. We can also measure the straight-line distance between two points through the Earth's interior; this notion is, for example, natural in seismology, since it roughly corresponds to the length of time it takes for seismic waves to travel between those two points.

The notion of distance encoded by the metric space axioms has relatively few requirements. This generality gives metric spaces a lot of flexibility. At the same time, the notion is strong enough to encode many intuitive facts about what distance means. This means that general results about metric spaces can be applied in many different contexts.

Like many fundamental mathematical concepts, the metric on a metric space can be interpreted in many different ways. A particular metric may not be best thought of as measuring physical distance, but, instead, as the cost of changing from one state to another (as with Wasserstein metrics on spaces of measures) or the degree of difference between two objects (for example, the Hamming distance between two strings of characters, or the Gromov–Hausdorff distance between metric spaces themselves).

### Definition

Formally, a **metric space** is an ordered pair (*M*, *d*) where M is a set (whose elements are called points), and d is a **metric** on M, i.e., a function $d\,\colon M\times M\to \mathbb {R}$ satisfying the following axioms for all points $x,y,z\in M$ :

1. The distance from a point to itself is zero: $d(x,x)=0$
2. (Positivity) The distance between two distinct points is always positive: ${\text{If }}x\neq y{\text{, then }}d(x,y)>0$
3. (Symmetry) The distance from x to y is always the same as the distance from y to x: $d(x,y)=d(y,x)$
4. The triangle inequality holds: $d(x,z)\leq d(x,y)+d(y,z)$ This is a natural property of both physical and metaphorical notions of distance: you can arrive at z from x by taking a detour through y, but this will not make your journey any shorter than the direct path.

It is traditional to write M as an abbreviation for (*M*, *d*) when it is understood what d is.

### Simple examples

#### The real numbers

The real numbers with the distance function $d(x,y)=|y-x|$ given by the absolute difference form a metric space. Many properties of metric spaces and functions between them are generalizations of concepts in real analysis and coincide with those concepts when applied to the real line.

#### Metrics on Euclidean spaces

The Euclidean plane $\mathbb {R} ^{2}$ can be equipped with many different metrics. The Euclidean distance familiar from school mathematics can be defined by $d_{2}((x_{1},y_{1}),(x_{2},y_{2}))={\sqrt {(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}}.$

The *taxicab* or *Manhattan* distance is defined by $d_{1}((x_{1},y_{1}),(x_{2},y_{2}))=|x_{2}-x_{1}|+|y_{2}-y_{1}|$ and can be thought of as the distance you need to travel along horizontal and vertical lines to get from one point to the other, as illustrated at the top of the article.

The *maximum*, $L^{\infty }$ , or *Chebyshev distance* is defined by $d_{\infty }((x_{1},y_{1}),(x_{2},y_{2}))=\max\{|x_{2}-x_{1}|,|y_{2}-y_{1}|\}.$ This distance does not have an easy explanation in terms of paths in the plane, but it still satisfies the metric space axioms. It can be thought of similarly to the number of moves a king would have to make on a chess board to travel from one point to another on the given space.

In fact, these three distances, while they have distinct properties, are similar in some ways. Informally, points that are close in one are close in the others, too. This observation can be quantified with the formula $d_{\infty }(p,q)\leq d_{2}(p,q)\leq d_{1}(p,q)\leq 2d_{\infty }(p,q),$ which holds for every pair of points $p,q\in \mathbb {R} ^{2}$ . Moreover, there exists a continuous family of distances $d_{\alpha }$ for $\alpha \in (1,\infty )$ that interpolates between these three distances. It is defined by $d_{\alpha }((x_{1},y_{1}),(x_{2},y_{2}))=\left(\vert x_{2}-x_{1}\vert ^{\alpha }+\vert y_{2}-y_{1}\vert ^{\alpha }\right)^{1/\alpha }.$

A radically different distance can be defined by setting $d(p,q)={\begin{cases}0,&{\text{if }}p=q,\\1,&{\text{otherwise.}}\end{cases}}$ In this *discrete metric*, all distinct points are 1 unit apart: none of them are close to each other, and none of them are very far away from each other either. Intuitively, the discrete metric no longer remembers that the set is a plane, but treats it just as an undifferentiated set of points.

All of these metrics can be easily extended to make sense on $\mathbb {R} ^{n}$ as well as $\mathbb {R} ^{2}$ .

#### Subspaces

Given a metric space (*M*, *d*) and a subset $A\subseteq M$ , we can consider A to be a metric space by measuring distances the same way we would in M. Formally, the *induced metric* on A is a function $d_{A}:A\times A\to \mathbb {R}$ defined by $d_{A}(x,y)=d(x,y).$ For example, if we take the two-dimensional sphere S2 as a subset of $\mathbb {R} ^{3}$ , the Euclidean metric on $\mathbb {R} ^{3}$ induces the straight-line metric on S2 described above. Two more useful examples are the open interval (0, 1) and the closed interval [0, 1] thought of as subspaces of the real line.


## History

Arthur Cayley, in his article "On Distance", extended metric concepts beyond Euclidean geometry into domains bounded by a conic in a projective space. His distance was given by logarithm of a cross ratio. Any projectivity leaving the conic stable also leaves the cross ratio constant, so isometries are implicit. This method provides models for elliptic geometry and hyperbolic geometry, and Felix Klein, in several publications, established the field of non-euclidean geometry through the use of the Cayley-Klein metric.

The idea of an abstract space with metric properties was addressed in 1906 by René Maurice Fréchet and the term *metric space* was coined by Felix Hausdorff in 1914.

Fréchet's work laid the foundation for understanding convergence, continuity, and other key concepts in non-geometric spaces. This allowed mathematicians to study functions and sequences in a broader and more flexible way. This was important for the growing field of functional analysis. Mathematicians like Hausdorff and Stefan Banach further refined and expanded the framework of metric spaces. Hausdorff introduced topological spaces as a generalization of metric spaces. Banach's work in functional analysis heavily relied on the metric structure. Over time, metric spaces became a central part of modern mathematics. They have influenced various fields including topology, geometry, and applied mathematics. Metric spaces continue to play a crucial role in the study of abstract mathematical concepts.


## Basic notions

A distance function is enough to define notions of closeness and convergence that were first developed in real analysis. Properties that depend on the structure of a metric space are referred to as *metric properties*. Every metric space is also a topological space, and some metric properties can also be rephrased without reference to distance in the language of topology; that is, they are really topological properties.

### The topology of a metric space

For any point x in a metric space M and any real number *r* > 0, the *open ball* of radius r around x is defined to be the set of points that are strictly less than distance r from x: $B_{r}(x)=\{y\in M:d(x,y)<r\}.$ This is a natural way to define a set of points that are relatively close to x. Therefore, a set $N\subseteq M$ is a *neighborhood* of x (informally, it contains all points "close enough" to x) if it contains an open ball of radius r around x for some *r* > 0.

An *open set* is a set which is a neighborhood of all its points. It follows that the open balls form a base for a topology on M. In other words, the open sets of M are exactly the unions of open balls. As in any topology, closed sets are the complements of open sets. Sets may be both open and closed as well as neither open nor closed.

This topology does not carry all the information about the metric space. For example, the distances *d*1, *d*2, and *d*∞ defined above all induce the same topology on $\mathbb {R} ^{2}$ , although they behave differently in many respects. Similarly, $\mathbb {R}$ with the Euclidean metric and its subspace the interval (0, 1) with the induced metric are homeomorphic but have very different metric properties.

Conversely, not every topological space can be given a metric. Topological spaces which are compatible with a metric are called *metrizable* and are particularly well-behaved in many ways: in particular, they are paracompact Hausdorff spaces (hence normal) and first-countable. The Nagata–Smirnov metrization theorem gives a characterization of metrizability in terms of other topological properties, without reference to metrics.

### Convergence

Convergence of sequences in Euclidean space is defined as follows:

A sequence

(

x

n

)

converges to a point

x

if for every

ε > 0

there is an integer

N

such that for all

n

>

N

,

d

(

x

n

,

x

) < ε

.

Convergence of sequences in a topological space is defined as follows:

A sequence

(

x

n

)

converges to a point

x

if for every open set

U

containing

x

there is an integer

N

such that for all

n

>

N

,

$x_{n}\in U$

.

In metric spaces, both of these definitions make sense and they are equivalent. This is a general pattern for topological properties of metric spaces: while they can be defined in a purely topological way, there is often a way that uses the metric which is easier to state or more familiar from real analysis.

### Completeness

Informally, a metric space is *complete* if it has no "missing points": every sequence that looks like it should converge to something actually converges.

To make this precise: a sequence (*xn*) in a metric space M is a Cauchy sequence if for every ε > 0 there is an integer N such that for all *m*, *n* > *N*, *d*(*xm*, *xn*) < ε. By the triangle inequality, any convergent sequence is a Cauchy sequence: if xm and xn are both less than ε away from the limit, then they are less than 2ε away from each other. If the converse is true—every Cauchy sequence in M converges—then M is complete.

Euclidean spaces are complete, as is $\mathbb {R} ^{2}$ with the other metrics described above. Two examples of spaces which are not complete are (0, 1) and the rationals, each with the metric induced from $\mathbb {R}$ . One can think of (0, 1) as "missing" its endpoints 0 and 1. The rationals are missing all the irrationals, since any irrational has a sequence of rationals converging to it in $\mathbb {R}$ (for example, its successive decimal approximations). These examples show that completeness is *not* a topological property, since $\mathbb {R}$ is complete but the homeomorphic space (0, 1) is not.

This notion of "missing points" can be made precise. In fact, every metric space has a unique *completion*, which is a complete space that contains the given space as a dense subset. For example, [0, 1] is the completion of (0, 1), and the real numbers are the completion of the rationals.

Since complete spaces are generally easier to work with, completions are important throughout mathematics. For example, in abstract algebra, the *p*-adic numbers are defined as the completion of the rationals under a different metric. Completion is particularly common as a tool in functional analysis. Often one has a set of nice functions and a way of measuring distances between them. Taking the completion of this metric space gives a new set of functions which may be less nice, but nevertheless useful because they behave similarly to the original nice functions in important ways. For example, weak solutions to differential equations typically live in a completion (a Sobolev space) rather than the original space of nice functions for which the differential equation actually makes sense.

### Bounded and totally bounded spaces

A metric space M is *bounded* if there is an r such that no pair of points in M is more than distance r apart. The least such r is called the diameter of M.

The space M is called *precompact* or *totally bounded* if for every *r* > 0 there is a finite cover of M by open balls of radius r. Every totally bounded space is bounded. To see this, start with a finite cover by r-balls for some arbitrary r. Since the subset of M consisting of the centers of these balls is finite, it has finite diameter, say D. By the triangle inequality, the diameter of the whole space is at most *D* + 2*r*. The converse does not hold: an example of a metric space that is bounded but not totally bounded is $\mathbb {R} ^{2}$ (or any other infinite set) with the discrete metric.

### Compactness

Compactness is a topological property which generalizes the properties of a closed and bounded subset of Euclidean space. There are several equivalent definitions of compactness in metric spaces:

1. A metric space M is compact if every open cover has a finite subcover (the usual topological definition).
2. A metric space M is compact if every sequence has a convergent subsequence. (For general topological spaces this is called sequential compactness and is not equivalent to compactness.)
3. A metric space M is compact if it is complete and totally bounded. (This definition is written in terms of metric properties and does not make sense for a general topological space, but it is nevertheless topologically invariant since it is equivalent to compactness.)

One example of a compact space is the closed interval [0, 1].

Compactness is important for similar reasons to completeness: it makes it easy to find limits. Another important tool is Lebesgue's number lemma, which shows that for any open cover of a compact space, every point is relatively deep inside one of the sets of the cover.


## Functions between metric spaces

Unlike in the case of topological spaces or algebraic structures such as groups or rings, there is no single "right" type of structure-preserving function between metric spaces. Instead, one works with different types of functions depending on one's goals. Throughout this section, suppose that $(M_{1},d_{1})$ and $(M_{2},d_{2})$ are two metric spaces. The words "function" and "map" are used interchangeably.

### Isometries

One interpretation of a "structure-preserving" map is one that fully preserves the distance function:

A function

$f:M_{1}\to M_{2}$

is

distance-preserving

if for every pair of points

x

and

y

in

M

1

,

$d_{2}(f(x),f(y))=d_{1}(x,y).$

It follows from the metric space axioms that a distance-preserving function is injective. A bijective distance-preserving function is called an *isometry*. One perhaps non-obvious example of an isometry between spaces described in this article is the map $f:(\mathbb {R} ^{2},d_{1})\to (\mathbb {R} ^{2},d_{\infty })$ defined by $f(x,y)=(x+y,x-y).$

If there is an isometry between the spaces *M*1 and *M*2, they are said to be *isometric*. Metric spaces that are isometric are essentially identical.

### Continuous maps

On the other end of the spectrum, one can forget entirely about the metric structure and study continuous maps, which only preserve topological structure. There are several equivalent definitions of continuity for metric spaces. The most important are:

- **Topological definition.** A function $f\,\colon M_{1}\to M_{2}$ is continuous if for every open set U in *M*2, the preimage $f^{-1}(U)$ is open.
- **Sequential continuity.** A function $f\,\colon M_{1}\to M_{2}$ is continuous if whenever a sequence (*xn*) converges to a point x in *M*1, the sequence $f(x_{1}),f(x_{2}),\ldots$ converges to the point *f*(*x*) in *M*2.

(These first two definitions are

not

equivalent for all topological spaces.)

- **ε–δ definition.** A function $f\,\colon M_{1}\to M_{2}$ is continuous if for every point x in *M*1 and every ε > 0 there exists δ > 0 such that for all y in *M*1 we have $d_{1}(x,y)<\delta \implies d_{2}(f(x),f(y))<\varepsilon .$

A *homeomorphism* is a continuous bijection whose inverse is also continuous; if there is a homeomorphism between *M*1 and *M*2, they are said to be *homeomorphic*. Homeomorphic spaces are the same from the point of view of topology, but may have very different metric properties. For example, $\mathbb {R}$ is unbounded and complete, while (0, 1) is bounded but not complete.

### Uniformly continuous maps

A function $f\,\colon M_{1}\to M_{2}$ is *uniformly continuous* if for every real number ε > 0 there exists δ > 0 such that for all points x and y in *M*1 such that $d(x,y)<\delta$ , we have $d_{2}(f(x),f(y))<\varepsilon .$

The only difference between this definition and the ε–δ definition of continuity is the order of quantifiers: the choice of δ must depend only on ε and not on the point x. However, this subtle change makes a big difference. For example, uniformly continuous maps take Cauchy sequences in *M*1 to Cauchy sequences in *M*2. In other words, uniform continuity preserves some metric properties which are not purely topological.

On the other hand, the Heine–Cantor theorem states that if *M*1 is compact, then every continuous map is uniformly continuous. In other words, uniform continuity cannot distinguish any non-topological features of compact metric spaces.

### Lipschitz maps and contractions

A Lipschitz map is one that stretches distances by at most a bounded factor. Formally, given a real number *K* > 0, the map $f\,\colon M_{1}\to M_{2}$ is K-*Lipschitz* if $d_{2}(f(x),f(y))\leq Kd_{1}(x,y)\quad {\text{for all}}\quad x,y\in M_{1}.$ Lipschitz maps are particularly important in metric geometry, since they provide more flexibility than distance-preserving maps, but still make essential use of the metric. For example, a curve in a metric space is rectifiable (has finite length) if and only if it has a Lipschitz reparametrization.

A 1-Lipschitz map is sometimes called a *nonexpanding* or *metric map*. Metric maps are commonly taken to be the morphisms of the category of metric spaces.

A K-Lipschitz map for *K* < 1 is called a *contraction*. The Banach fixed-point theorem states that if M is a complete metric space, then every contraction $f:M\to M$ admits a unique fixed point. If the metric space M is compact, the result holds for a slightly weaker condition on f: a map $f:M\to M$ admits a unique fixed point if $d(f(x),f(y))<d(x,y)\quad {\mbox{for all}}\quad x\neq y\in M_{1}.$

### Quasi-isometries

A quasi-isometry is a map that preserves the "large-scale structure" of a metric space. Quasi-isometries need not be continuous. For example, $\mathbb {R} ^{2}$ and its subspace $\mathbb {Z} ^{2}$ are quasi-isometric, even though one is connected and the other is discrete. The equivalence relation of quasi-isometry is important in geometric group theory: the Švarc–Milnor lemma states that all spaces on which a group acts geometrically are quasi-isometric.

Formally, the map $f\,\colon M_{1}\to M_{2}$ is a *quasi-isometric embedding* if there exist constants *A* ≥ 1 and *B* ≥ 0 such that ${\frac {1}{A}}d_{2}(f(x),f(y))-B\leq d_{1}(x,y)\leq Ad_{2}(f(x),f(y))+B\quad {\text{ for all }}\quad x,y\in M_{1}.$ It is a *quasi-isometry* if in addition it is *quasi-surjective*, i.e. there is a constant *C* ≥ 0 such that every point in $M_{2}$ is at distance at most C from some point in the image $f(M_{1})$ .

### Notions of metric space equivalence

Given two metric spaces $(M_{1},d_{1})$ and $(M_{2},d_{2})$ :

- They are called **homeomorphic** (topologically isomorphic) if there is a homeomorphism between them (i.e., a continuous bijection with a continuous inverse). If $M_{1}=M_{2}$ and the identity map is a homeomorphism, then $d_{1}$ and $d_{2}$ are said to be **topologically equivalent**.
- They are called **uniformic** (uniformly isomorphic) if there is a uniform isomorphism between them (i.e., a uniformly continuous bijection with a uniformly continuous inverse).
- They are called **bilipschitz homeomorphic** if there is a bilipschitz bijection between them (i.e., a Lipschitz bijection with a Lipschitz inverse).
- They are called **isometric** if there is a (bijective) isometry between them. In this case, the two metric spaces are essentially identical.
- They are called **quasi-isometric** if there is a quasi-isometry between them.


## Metric spaces with additional structure

### Normed vector spaces

A normed vector space is a vector space equipped with a *norm*, which is a function that measures the length of vectors. The norm of a vector v is typically denoted by $\lVert v\rVert$ . Any normed vector space can be equipped with a metric in which the distance between two vectors x and y is given by $d(x,y):=\lVert x-y\rVert .$ The metric d is said to be *induced* by the norm $\lVert {\cdot }\rVert$ .

Conversely, if a metric d on a vector space X is

- translation invariant: $d(x,y)=d(x+a,y+a)$ for every x, y, and a in X; and
- absolutely homogeneous: $d(\alpha x,\alpha y)=|\alpha |d(x,y)$ for every x and y in X and real number α;

then ${\displaystyle \lVert x\rVert$ is a norm induced by the metric. A similar relationship holds between seminorms and pseudometrics.

Among examples of metrics induced by a norm are the metrics *d*1, *d*2, and *d*∞ on $\mathbb {R} ^{2}$ , which are induced by the Manhattan norm, the Euclidean norm, and the maximum norm, respectively. More generally, the Kuratowski embedding allows one to see any metric space as a subspace of a normed vector space.

Infinite-dimensional normed vector spaces, particularly spaces of functions, are studied in functional analysis. Completeness is particularly important in this context: a complete normed vector space is known as a Banach space. An unusual property of normed vector spaces is that linear transformations between them are continuous if and only if they are Lipschitz. Such transformations are known as bounded operators.

### Length spaces

A curve in a metric space (*M*, *d*) is a continuous function ${\displaystyle \gamma$ . The length of γ is measured by $L(\gamma )=\sup _{0=x_{0}<x_{1}<\cdots <x_{n}=T}\left\{\sum _{k=1}^{n}d(\gamma (x_{k-1}),\gamma (x_{k}))\right\}.$ In general, this supremum may be infinite; a curve of finite length is called *rectifiable*. Suppose that the length of the curve γ is equal to the distance between its endpoints—that is, it is the shortest possible path between its endpoints. After reparametrization by arc length, γ becomes a *geodesic*: a curve which is a distance-preserving function. A geodesic is a shortest possible path between any two of its points.

A *geodesic metric space* is a metric space which admits a geodesic between any two of its points. The spaces $(\mathbb {R} ^{2},d_{1})$ and $(\mathbb {R} ^{2},d_{2})$ are both geodesic metric spaces. In $(\mathbb {R} ^{2},d_{2})$ , geodesics are unique, but in $(\mathbb {R} ^{2},d_{1})$ , there are often infinitely many geodesics between two points, as shown in the figure at the top of the article.

The space M is a *length space* (or the metric d is *intrinsic*) if the distance between any two points x and y is the infimum of lengths of paths between them. Unlike in a geodesic metric space, the infimum does not have to be attained. An example of a length space which is not geodesic is the Euclidean plane minus the origin: the points (1, 0) and (-1, 0) can be joined by paths of length arbitrarily close to 2, but not by a path of length 2. An example of a metric space which is not a length space is given by the straight-line metric on the sphere: the straight line between two points through the center of the Earth is shorter than any path along the surface.

Given any metric space (*M*, *d*), one can define a new, intrinsic distance function *d*intrinsic on M by setting the distance between points x and y to be the infimum of the d-lengths of paths between them. For instance, if d is the straight-line distance on the sphere, then *d*intrinsic is the great-circle distance. However, in some cases *d*intrinsic may have infinite values. For example, if M is the Koch snowflake with the subspace metric d induced from $\mathbb {R} ^{2}$ , then the resulting intrinsic distance is infinite for any pair of distinct points.

### Riemannian manifolds

A Riemannian manifold is a space equipped with a Riemannian metric tensor, which determines lengths of tangent vectors at every point. This can be thought of defining a notion of distance infinitesimally. In particular, a differentiable path ${\displaystyle \gamma$ in a Riemannian manifold M has length defined as the integral of the length of the tangent vector to the path: $L(\gamma )=\int _{0}^{T}|{\dot {\gamma }}(t)|dt.$ On a connected Riemannian manifold, one then defines the distance between two points as the infimum of lengths of smooth paths between them. This construction generalizes to other kinds of infinitesimal metrics on manifolds, such as sub-Riemannian and Finsler metrics.

The Riemannian metric is uniquely determined by the distance function; this means that in principle, all information about a Riemannian manifold can be recovered from its distance function. One direction in metric geometry is finding purely metric ("synthetic") formulations of properties of Riemannian manifolds. For example, a Riemannian manifold is a CAT(*k*) space (a synthetic condition which depends purely on the metric) if and only if its sectional curvature is bounded above by k. Thus CAT(*k*) spaces generalize upper curvature bounds to general metric spaces.

### Metric measure spaces

Real analysis makes use of both the metric on $\mathbb {R} ^{n}$ and the Lebesgue measure. Therefore, generalizations of many ideas from analysis naturally reside in metric measure spaces: spaces that have both a measure and a metric which are compatible with each other. Formally, a *metric measure space* is a metric space equipped with a Borel regular measure such that every ball has positive measure. For example Euclidean spaces of dimension n, and more generally n-dimensional Riemannian manifolds, naturally have the structure of a metric measure space, equipped with the Lebesgue measure. Certain fractal metric spaces such as the Sierpiński gasket can be equipped with the α-dimensional Hausdorff measure where α is the Hausdorff dimension. In general, however, a metric space may not have an "obvious" choice of measure.

One application of metric measure spaces is generalizing the notion of Ricci curvature beyond Riemannian manifolds. Just as CAT(*k*) and Alexandrov spaces generalize sectional curvature bounds, RCD spaces are a class of metric measure spaces which generalize lower bounds on Ricci curvature.


## Further examples and applications

### Graphs and finite metric spaces

A metric space is *discrete* if its induced topology is the discrete topology. Although many concepts, such as completeness and compactness, are not interesting for such spaces, they are nevertheless an object of study in several branches of mathematics. In particular, finite metric spaces (those having a finite number of points) are studied in combinatorics and theoretical computer science. Embeddings in other metric spaces are particularly well-studied. For example, not every finite metric space can be isometrically embedded in a Euclidean space or in Hilbert space. On the other hand, in the worst case the required distortion (bilipschitz constant) is only logarithmic in the number of points.

For any undirected connected graph G, the set V of vertices of G can be turned into a metric space by defining the distance between vertices x and y to be the length of the shortest edge path connecting them. In graph theory, this is also called the shortest-path distance or geodesic distance. In geometric group theory this construction is applied to the Cayley graph of a (typically infinite) finitely-generated group, yielding the word metric. Up to quasi-isometry, the word metric depends only on the group and not on the chosen finite generating set.

### Metric embeddings and approximations

An important area of study in finite metric spaces is the embedding of complex metric spaces into simpler ones while controlling the distortion of distances. This is particularly useful in computer science and discrete mathematics, where algorithms often perform more efficiently on simpler structures like tree metrics.

A significant result in this area is that any finite metric space can be probabilistically embedded into a *tree metric* with an expected distortion of $O(\log n)$ , where n is the number of points in the metric space.

This embedding is notable because it achieves the best possible asymptotic bound on distortion, matching the lower bound of $\Omega (\log n)$ . The tree metrics produced in this embedding *dominate* the original metrics, meaning that distances in the tree are greater than or equal to those in the original space. This property is particularly useful for designing approximation algorithms, as it allows for the preservation of distance-related properties while simplifying the underlying structure.

The result has significant implications for various computational problems:

- **Network design**: Improves approximation algorithms for problems like the *Group Steiner tree problem* (a generalization of the *Steiner tree problem*) and *Buy-at-bulk network design* (a problem in *Network planning and design*) by simplifying the metric space to a tree metric.
- **Clustering**: Enhances algorithms for clustering problems where hierarchical clustering can be performed more efficiently on tree metrics.
- **Online algorithms**: Benefits problems like the *k-server problem* and *metrical task system* by providing better competitive ratios through simplified metrics.

The technique involves constructing a hierarchical decomposition of the original metric space and converting it into a tree metric via a randomized algorithm. The $O(\log n)$ distortion bound has led to improved approximation ratios in several algorithmic problems, demonstrating the practical significance of this theoretical result.

### Distances between mathematical objects

In modern mathematics, one often studies spaces whose points are themselves mathematical objects. A distance function on such a space generally aims to measure the dissimilarity between two objects. Here are some examples:

- **Functions to a metric space.** If X is any set and M is a metric space, then the set of all bounded functions $f\colon X\to M$ (i.e. those functions whose image is a bounded subset of M ) can be turned into a metric space by defining the distance between two bounded functions f and g to be $d(f,g)=\sup _{x\in X}d(f(x),g(x)).$ This metric is called the uniform metric or supremum metric. If M is complete, then this function space is complete as well; moreover, if X is also a topological space, then the subspace consisting of all bounded continuous functions from X to M is also complete. When X is a subspace of $\mathbb {R} ^{n}$ , this function space is known as a classical Wiener space.
- **String metrics and edit distances.** There are many ways of measuring distances between strings of characters, which may represent sentences in computational linguistics or code words in coding theory. *Edit distances* attempt to measure the number of changes necessary to get from one string to another. For example, the Hamming distance measures the minimal number of substitutions needed, while the Levenshtein distance measures the minimal number of deletions, insertions, and substitutions; both of these can be thought of as distances in an appropriate graph.
- Graph edit distance is a measure of dissimilarity between two graphs, defined as the minimal number of graph edit operations required to transform one graph into another.
- Wasserstein metrics measure the distance between two measures on the same metric space. The Wasserstein distance between two measures is, roughly speaking, the cost of transporting one to the other.
- The set of all m by n matrices over some field is a metric space with respect to the rank distance $d(A,B)=\mathrm {rank} (B-A)$ .
- The Helly metric in game theory measures the difference between strategies in a game.

### Hausdorff and Gromov–Hausdorff distance

The idea of spaces of mathematical objects can also be applied to subsets of a metric space, as well as metric spaces themselves. Hausdorff and Gromov–Hausdorff distance define metrics on the set of compact subsets of a metric space and the set of compact metric spaces, respectively.

Suppose (*M*, *d*) is a metric space, and let S be a subset of M. The *distance from S to a point x of M* is, informally, the distance from x to the closest point of S. However, since there may not be a single closest point, it is defined via an infimum: $d(x,S)=\inf\{d(x,s):s\in S\}.$ In particular, $d(x,S)=0$ if and only if x belongs to the closure of S. Furthermore, distances between points and sets satisfy a version of the triangle inequality: $d(x,S)\leq d(x,y)+d(y,S),$ and therefore the map $d_{S}:M\to \mathbb {R}$ defined by $d_{S}(x)=d(x,S)$ is continuous. Incidentally, this shows that metric spaces are completely regular.

Given two subsets S and T of M, their *Hausdorff distance* is $d_{H}(S,T)=\max\{\sup\{d(s,T):s\in S\},\sup\{d(t,S):t\in T\}\}.$ Informally, two sets S and T are close to each other in the Hausdorff distance if no element of S is too far from T and vice versa. For example, if S is an open set in Euclidean space T is an ε-net inside S, then $d_{H}(S,T)<\varepsilon$ . In general, the Hausdorff distance $d_{H}(S,T)$ can be infinite or zero. However, the Hausdorff distance between two distinct compact sets is always positive and finite. Thus the Hausdorff distance defines a metric on the set of compact subsets of M.

The Gromov–Hausdorff metric defines a distance between (isometry classes of) compact metric spaces. The *Gromov–Hausdorff distance* between compact spaces X and Y is the infimum of the Hausdorff distance over all metric spaces Z that contain X and Y as subspaces. While the exact value of the Gromov–Hausdorff distance is rarely useful to know, the resulting topology has found many applications.

### Miscellaneous examples

- Given a metric space (*X*, *d*) and an increasing concave function $f\colon [0,\infty )\to [0,\infty )$ such that *f*(*t*) = 0 if and only if *t* = 0, then $d_{f}(x,y)=f(d(x,y))$ is also a metric on X. If *f*(*t*) = *t*α for some real number α < 1, such a metric is known as a **snowflake** of d.
- The tight span of a metric space is another metric space which can be thought of as an abstract version of the convex hull.
- The *knight's move metric*, the minimal number of knight's moves to reach one point in $\mathbb {Z} ^{2}$ from another, is a metric on $\mathbb {Z} ^{2}$ .
- The British Rail metric (also called the "post office metric" or the "French railway metric") on a normed vector space is given by $d(x,y)=\lVert x\rVert +\lVert y\rVert$ for distinct points x and y , and $d(x,x)=0$ . More generally $\lVert \cdot \rVert$ can be replaced with a function f taking an arbitrary set S to non-negative reals and taking the value 0 at most once: then the metric is defined on S by $d(x,y)=f(x)+f(y)$ for distinct points x and y , and $d(x,x)=0$ . The name alludes to the tendency of railway journeys to proceed via London (or Paris) irrespective of their final destination.
- The Robinson–Foulds metric used for calculating the distances between Phylogenetic trees in Phylogenetics


## Constructions

### Product metric spaces

If $(M_{1},d_{1}),\ldots ,(M_{n},d_{n})$ are metric spaces, and N is the Euclidean norm on $\mathbb {R} ^{n}$ , then ${\bigl (}M_{1}\times \cdots \times M_{n},d_{\times }{\bigr )}$ is a metric space, where the product metric is defined by $d_{\times }{\bigl (}(x_{1},\ldots ,x_{n}),(y_{1},\ldots ,y_{n}){\bigr )}=N{\bigl (}d_{1}(x_{1},y_{1}),\ldots ,d_{n}(x_{n},y_{n}){\bigr )},$ and the induced topology agrees with the product topology. By the equivalence of norms in finite dimensions, a topologically equivalent metric is obtained if N is the taxicab norm, a p-norm, the maximum norm, or any other norm which is non-decreasing as the coordinates of a positive n-tuple increase (yielding the triangle inequality).

Similarly, a metric on the topological product of countably many metric spaces can be obtained using the metric $d(x,y)=\sum _{i=1}^{\infty }{\frac {1}{2^{i}}}{\frac {d_{i}(x_{i},y_{i})}{1+d_{i}(x_{i},y_{i})}}.$

The topological product of uncountably many metric spaces need not be metrizable. For example, an uncountable product of copies of $\mathbb {R}$ is not first-countable and thus is not metrizable.

### Quotient metric spaces

If M is a metric space with metric d, and $\sim$ is an equivalence relation on M, then we can endow the quotient set $M/\!\sim$ with a pseudometric. The distance between two equivalence classes $[x]$ and $[y]$ is defined as $d'([x],[y])=\inf\{d(p_{1},q_{1})+d(p_{2},q_{2})+\dotsb +d(p_{n},q_{n})\},$ where the infimum is taken over all finite sequences $(p_{1},p_{2},\dots ,p_{n})$ and $(q_{1},q_{2},\dots ,q_{n})$ with $p_{1}\sim x$ , $q_{n}\sim y$ , $q_{i}\sim p_{i+1},i=1,2,\dots ,n-1$ . In general this will only define a pseudometric, i.e. $d'([x],[y])=0$ does not necessarily imply that $[x]=[y]$ . However, for some equivalence relations (e.g., those given by gluing together polyhedra along faces), $d'$ is a metric.

The quotient metric $d'$ is characterized by the following universal property. If $f\,\colon (M,d)\to (X,\delta )$ is a metric (i.e. 1-Lipschitz) map between metric spaces satisfying *f*(*x*) = *f*(*y*) whenever $x\sim y$ , then the induced function ${\overline {f}}\,\colon {M/\sim }\to X$ , given by ${\overline {f}}([x])=f(x)$ , is a metric map ${\overline {f}}\,\colon (M/\sim ,d')\to (X,\delta ).$

The quotient metric does not always induce the quotient topology. For example, the topological quotient of the metric space $\mathbb {N} \times [0,1]$ identifying all points of the form $(n,0)$ is not metrizable since it is not first-countable, but the quotient metric is a well-defined metric on the same set which induces a coarser topology. Moreover, different metrics on the original topological space (a disjoint union of countably many intervals) lead to different topologies on the quotient.

A topological space is sequential if and only if it is a (topological) quotient of a metric space.

---
title: "Isoperimetric inequality"
source: https://en.wikipedia.org/wiki/Isoperimetric_inequality
domain: calculus-of-variations
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, principle of least action, isoperimetric inequality
fetched: 2026-07-02
---

# Isoperimetric inequality

In mathematics, the **isoperimetric inequality** is a geometric inequality involving the square of the circumference of a closed curve in the plane and the area of a plane region it encloses, as well as its various generalizations. *Isoperimetric* literally means "having the same perimeter". Specifically, the isoperimetric inequality states, for the length *L* of a closed plane curve and the area *A* of the region that it encloses, that

$4\pi A\leq L^{2},$

and that equality holds if and only if the curve is a circle.

The **isoperimetric problem** is to determine a plane figure of the largest possible area whose boundary has a specified length. The closely related *Dido's problem* asks for a region of the maximal area bounded by a straight line and a curvilinear arc whose endpoints belong to that line. It is named after Dido, the legendary founder and first queen of Carthage. The solution to the isoperimetric problem is given by a circle and was known already in Ancient Greece. However, the first mathematically rigorous proof of this fact was obtained only in the 19th century. Since then, many other proofs have been found.

The isoperimetric problem has been extended in multiple ways, for example, to curves on surfaces and to regions in higher-dimensional spaces. Perhaps the most familiar physical manifestation of the 3-dimensional isoperimetric inequality is the shape of a drop of water. Namely, a drop will typically assume a symmetric round shape. Since the amount of water in a drop is fixed, surface tension forces the drop into a shape which minimizes the surface area of the drop, namely a round sphere.

## The isoperimetric problem in the plane

The classical *isoperimetric problem* dates back to antiquity. The problem can be stated as follows: Among all closed curves in the plane of fixed perimeter, which curve (if any) maximizes the area of its enclosed region? This question can be shown to be equivalent to the following problem: Among all closed curves in the plane enclosing a fixed area, which curve (if any) minimizes the perimeter?

This problem is conceptually related to the principle of least action in physics, in that it can be restated: what is the principle of action which encloses the greatest area, with the greatest economy of effort? The 15th-century philosopher and scientist, Cardinal Nicholas of Cusa, considered rotational action, the process by which a circle is generated, to be the most direct reflection, in the realm of sensory impressions, of the process by which the universe is created. German astronomer and astrologer Johannes Kepler invoked the isoperimetric principle in discussing the morphology of the Solar System, in *Mysterium Cosmographicum* (*The Sacred Mystery of the Cosmos*, 1596).

Although the circle appears to be an obvious solution to the problem, proving this fact is rather difficult. The first progress toward the solution was made by Swiss geometer Jakob Steiner in 1838, using a geometric method later named *Steiner symmetrisation*. Steiner showed that if a solution existed, then it must be the circle. Steiner's proof was completed later by several other mathematicians.

Steiner begins with some geometric constructions which are easily understood; for example, it can be shown that any closed curve enclosing a region that is not fully convex can be modified to enclose more area, by "flipping" the concave areas so that they become convex. It can further be shown that any closed curve which is not fully symmetrical can be "tilted" so that it encloses more area. The one shape that is perfectly convex and symmetrical is the circle, although this, in itself, does not represent a rigorous proof of the isoperimetric theorem (see external links).

## On a plane

The solution to the isoperimetric problem is usually expressed in the form of an inequality that relates the length *L* of a closed curve and the area *A* of the planar region that it encloses. The **isoperimetric inequality** states that

$4\pi A\leq L^{2},$

and that the equality holds if and only if the curve is a circle. The area of a disk of radius *R* is *πR*2 and the circumference of the circle is 2*πR*, so both sides of the inequality are equal to 4*π*2*R*2 in this case.

Dozens of proofs of the isoperimetric inequality have been found. In 1902, Hurwitz published a short proof using the Fourier series that applies to arbitrary rectifiable curves (not assumed to be smooth). An elegant direct proof based on comparison of a smooth simple closed curve with an appropriate circle was given by E. Schmidt in 1938. It uses only the arc length formula, expression for the area of a plane region from Green's theorem, and the Cauchy–Schwarz inequality.

For a given closed curve, the **isoperimetric quotient** is defined as the ratio of its area and that of the circle having the same perimeter. This is equal to

$Q={\frac {4\pi A}{L^{2}}}$

and the isoperimetric inequality says that *Q* ≤ 1. Equivalently, the isoperimetric ratio *L*2/*A* is at least 4π for every curve.

The isoperimetric quotient of a regular *n*-gon is

$Q_{n}={\frac {\pi }{n\tan(\pi /n)}}.$

Let C be a smooth regular convex closed curve. Then the **improved isoperimetric inequality** states the following

$L^{2}\geqslant 4\pi A+8\pi \left|{\widetilde {A}}_{0.5}\right|,$

where $L,A,{\widetilde {A}}_{0.5}$ denote the length of C , the area of the region bounded by C and the oriented area of the Wigner caustic of C , respectively, and the equality holds if and only if C is a curve of constant width.

## On a sphere

Let *C* be a simple closed curve on a sphere of radius 1. Denote by *L* the length of *C* and by *A* the area enclosed by *C*. The **spherical isoperimetric inequality** states that

$L^{2}\geq A(4\pi -A),$

and that the equality holds if and only if the curve is a circle. There are, in fact, two ways to measure the spherical area enclosed by a simple closed curve, but the inequality is symmetric with the respect to taking the complement.

This inequality was discovered by Paul Lévy (1919) who also extended it to higher dimensions and general surfaces.

In the more general case of arbitrary radius *R*, it is known that

$L^{2}\geq 4\pi A-{\frac {A^{2}}{R^{2}}}.$

## In Euclidean space

The isoperimetric inequality states that a sphere has the smallest surface area per given volume. Given a bounded open set $S\subset \mathbb {R} ^{n}$ with $C^{1}$ boundary, having surface area $\operatorname {per} (S)$ and volume $\operatorname {vol} (S)$ , the isoperimetric inequality states

$\operatorname {per} (S)\geq n\operatorname {vol} (S)^{(n-1)/n}\,\operatorname {vol} (B_{1})^{1/n},$

where $B_{1}\subset \mathbb {R} ^{n}$ is a unit ball. The equality holds when S is a ball in $\mathbb {R} ^{n}$ . Under additional restrictions on the set (such as convexity, regularity, smooth boundary), the equality holds for a ball only. But in full generality the situation is more complicated. The relevant result of Schmidt (1949, Sect. 20.7) (for a simpler proof see Baebler (1957)) is clarified in Hadwiger (1957, Sect. 5.2.5) as follows. An extremal set consists of a ball and a "corona" that contributes neither to the volume nor to the surface area. That is, the equality holds for a compact set S if and only if S contains a closed ball B such that $\operatorname {vol} (B)=\operatorname {vol} (S)$ and $\operatorname {per} (B)=\operatorname {per} (S).$ For example, the "corona" may be a curve.

The proof of the inequality follows directly from Brunn–Minkowski inequality between a set S and a ball with radius $\epsilon$ , i.e. $B_{\epsilon }=\epsilon B_{1}$ . Indeed, $\operatorname {vol} (A+B_{\epsilon })\geq (\operatorname {vol} (A)^{1/n}+\operatorname {vol} (B_{\epsilon })^{1/n})^{n}\geq \operatorname {vol} (A)+n\operatorname {vol} (A)^{(n-1)/n}\epsilon \operatorname {vol} (B_{1})^{1/n}.$ The isoperimetric inequality follows by subtracting ${\textstyle \operatorname {vol} (A)}$ , dividing by $\epsilon$ , and taking the limit as $\epsilon \to 0.$ (Osserman (1978); Federer (1969, §3.2.43)).

In full generality (Federer 1969, §3.2.43), the isoperimetric inequality states that for any set $S\subset \mathbb {R} ^{n}$ whose closure has finite Lebesgue measure

$n\,\omega _{n}^{1/n}L^{n}({\bar {S}})^{(n-1)/n}\leq M_{*}^{n-1}(\partial S)$

where $M_{*}^{n-1}$ is the (*n*-1)-dimensional Minkowski content, *Ln* is the *n*-dimensional Lebesgue measure, and *ωn* is the volume of the unit ball in $\mathbb {R} ^{n}$ . If the boundary of *S* is rectifiable, then the Minkowski content is the (*n*-1)-dimensional Hausdorff measure.

The *n*-dimensional isoperimetric inequality is equivalent (for sufficiently smooth domains) to the Sobolev inequality on $\mathbb {R} ^{n}$ with optimal constant:

$\left(\int _{\mathbb {R} ^{n}}|u|^{n/(n-1)}\right)^{(n-1)/n}\leq n^{-1}\omega _{n}^{-1/n}\int _{\mathbb {R} ^{n}}|\nabla u|$

for all $u\in W^{1,1}(\mathbb {R} ^{n})$ .

## In Hadamard manifolds

Hadamard manifolds are complete simply connected manifolds with nonpositive curvature. Thus they generalize the Euclidean space $\mathbb {R} ^{n}$ , which is a Hadamard manifold with curvature zero. In 1970's and early 80's, Thierry Aubin, Misha Gromov, Yuri Burago, and Viktor Zalgaller conjectured that the Euclidean isoperimetric inequality

$\operatorname {per} (S)\geq n\operatorname {vol} (S)^{(n-1)/n}\operatorname {vol} (B_{1})^{1/n}$

holds for bounded sets S in Hadamard manifolds, which has become known as the Cartan–Hadamard conjecture. In dimension 2 this had already been established in 1926 by André Weil, who was a student of Hadamard at the time. In dimensions 3 and 4 the conjecture was proved by Bruce Kleiner in 1992, and Chris Croke in 1984 respectively.

## In a metric measure space

Most of the work on isoperimetric problem has been done in the context of smooth regions in Euclidean spaces, or more generally, in Riemannian manifolds. However, the isoperimetric problem can be formulated in much greater generality, using the notion of *Minkowski content*. Let $(X,\mu ,d)$ be a *metric measure space*: *X* is a metric space with metric *d*, and *μ* is a Borel measure on *X*. The *boundary measure*, or Minkowski content, of a measurable subset *A* of *X* is defined as the lim inf

$\mu ^{+}(A)=\liminf _{\varepsilon \to 0+}{\frac {\mu (A_{\varepsilon })-\mu (A)}{\varepsilon }},$

where

$A_{\varepsilon }=\{x\in X|d(x,A)\leq \varepsilon \}$

is the ε-*extension* of *A*.

The isoperimetric problem in *X* asks how small can $\mu ^{+}(A)$ be for a given *μ*(*A*). If *X* is the Euclidean plane with the usual distance and the Lebesgue measure then this question generalizes the classical isoperimetric problem to planar regions whose boundary is not necessarily smooth, although the answer turns out to be the same.

The function

$I(a)=\inf\{\mu ^{+}(A)|\mu (A)=a\}$

is called the *isoperimetric profile* of the metric measure space $(X,\mu ,d)$ . Isoperimetric profiles have been studied for Cayley graphs of discrete groups and for special classes of Riemannian manifolds (where usually only regions *A* with regular boundary are considered).

## For graphs

In graph theory, isoperimetric inequalities are at the heart of the study of expander graphs, which are sparse graphs that have strong connectivity properties. Expander constructions have spawned research in pure and applied mathematics, with several applications to complexity theory, design of robust computer networks, and the theory of error-correcting codes.

Isoperimetric inequalities for graphs relate the size of vertex subsets to the size of their boundary, which is usually measured by the number of edges leaving the subset (edge expansion) or by the number of neighbouring vertices (vertex expansion). For a graph G and a number k , the following are two standard isoperimetric parameters for graphs.

- The edge isoperimetric parameter: $\Phi _{E}(G,k)=\min _{S\subseteq V}\left\{|E(S,{\overline {S}})|:|S|=k\right\}$
- The vertex isoperimetric parameter: $\Phi _{V}(G,k)=\min _{S\subseteq V}\left\{|\Gamma (S)\setminus S|:|S|=k\right\}$

Here $E(S,{\overline {S}})$ denotes the set of edges leaving S and $\Gamma (S)$ denotes the set of vertices that have a neighbour in S . The isoperimetric problem consists of understanding how the parameters $\Phi _{E}$ and $\Phi _{V}$ behave for natural families of graphs.

### Example: Isoperimetric inequalities for hypercubes

The d -dimensional hypercube $Q_{d}$ is the graph whose vertices are all Boolean vectors of length d , that is, the set $\{0,1\}^{d}$ . Two such vectors are connected by an edge in $Q_{d}$ if they are equal up to a single bit flip, that is, their Hamming distance is exactly one. The following are the isoperimetric inequalities for the Boolean hypercube.

#### Edge isoperimetric inequality

The edge isoperimetric inequality of the hypercube is $\Phi _{E}(Q_{d},k)\geq k(d-\log _{2}k)$ . This bound is tight, as is witnessed by each set S that is the set of vertices of any subcube of $Q_{d}$ .

#### Vertex isoperimetric inequality

Harper's theorem says that *Hamming balls* have the smallest vertex boundary among all sets of a given size. Hamming balls are sets that contain all points of Hamming weight at most r and no points of Hamming weight larger than $r+1$ for some integer r . This theorem implies that any set $S\subseteq V$ with

$|S|\geq \sum _{i=0}^{r}{d \choose i}$

satisfies

$|S\cup \Gamma (S)|\geq \sum _{i=0}^{r+1}{d \choose i}.$

As a special case, consider set sizes $k=|S|$ of the form

$k={d \choose 0}+{d \choose 1}+\dots +{d \choose r}$

for some integer r . Then the above implies that the exact vertex isoperimetric parameter is

$\Phi _{V}(Q_{d},k)={d \choose r+1}.$

## Isoperimetric inequality for triangles

The isoperimetric inequality for triangles in terms of perimeter *p* and area *T* states that

$p^{2}\geq 12{\sqrt {3}}\cdot T,$

with equality for the equilateral triangle. This is implied, via the AM–GM inequality, by a stronger inequality which has also been called the isoperimetric inequality for triangles:

$T\leq {\frac {\sqrt {3}}{4}}(abc)^{2/3}.$

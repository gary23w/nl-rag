---
title: "Morse theory"
source: https://en.wikipedia.org/wiki/Morse_theory
domain: differential-topology
license: CC-BY-SA-4.0
tags: differential topology, smooth manifold, morse theory, de rham cohomology
fetched: 2026-07-02
---

# Morse theory

In mathematics, specifically in differential topology, **Morse theory** enables one to analyze the topology of a manifold by studying differentiable functions on that manifold. According to the basic insights of Marston Morse, a typical differentiable function on a manifold will reflect the topology quite directly. Morse theory allows one to find CW structures and handle decompositions on manifolds and to obtain substantial information about their homology.

Before Morse, Arthur Cayley and James Clerk Maxwell had developed some of the ideas of Morse theory in the context of topography. Morse originally applied his theory to geodesics (critical points of the energy functional on the space of paths). These techniques were used in Raoul Bott's proof of his periodicity theorem.

The analogue of Morse theory for complex manifolds is Picard–Lefschetz theory.

## Basic concepts

To illustrate, consider a mountainous landscape surface M (more generally, a manifold). If f is the function $M\to \mathbb {R}$ giving the elevation of each point, then the inverse image of a point in $\mathbb {R}$ is a contour line (more generally, a level set). Each connected component of a contour line is either a point, a simple closed curve, or a closed curve with double point(s). Contour lines may also have points of higher order (triple points, etc.), but these are unstable and may be removed by a slight deformation of the landscape. Double points in contour lines occur at saddle points, or passes, where the surrounding landscape curves up in one direction and down in the other.

Imagine flooding this landscape with water. When the water reaches elevation a , the underwater surface is $M^{a}\,{\stackrel {\text{def}}{=}}\,f^{-1}(-\infty ,a]$ , the points with elevation a or below. Consider how the topology of this surface changes as the water rises. It appears unchanged except when a passes the height of a critical point, where the gradient of f is 0 (more generally, the Jacobian matrix acting as a linear map between tangent spaces does not have maximal rank). In other words, the topology of $M^{a}$ does not change except when the water either (1) starts filling a basin, (2) covers a saddle (a mountain pass), or (3) submerges a peak.

To these three types of critical points—basins, passes, and peaks (i.e. minima, saddles, and maxima)—one associates a number called the index, the number of independent directions in which f decreases from the point. More precisely, the index of a non-degenerate critical point p of f is the dimension of the largest subspace of the tangent space to M at p on which the Hessian of f is negative definite. The indices of basins, passes, and peaks are $0,1,$ and $2,$ respectively.

Considering a more general surface, let M be a torus oriented as in the picture, with f again taking a point to its height above the plane. One can again analyze how the topology of the underwater surface $M^{a}$ changes as the water level a rises.

Starting from the bottom of the torus, let $p,q,r,$ and s be the four critical points of index $0,1,1,$ and 2 corresponding to the basin, two saddles, and peak, respectively. When a is less than $f(p)=0,$ then $M^{a}$ is the empty set. After a passes the level of $p,$ when $0<a<f(q),$ then $M^{a}$ is a disk, which is homotopy equivalent to a point (a 0-cell) which has been "attached" to the empty set. Next, when a exceeds the level of $q,$ and $f(q)<a<f(r),$ then $M^{a}$ is a cylinder, and is homotopy equivalent to a disk with a 1-cell attached (image at left). Once a passes the level of $r,$ and $f(r)<a<f(s),$ then $M^{a}$ is a torus with a disk removed, which is homotopy equivalent to a cylinder with a 1-cell attached (image at right). Finally, when a is greater than the critical level of $s,$ $M^{a}$ is a torus, i.e. a torus with a disk (a 2-cell) removed and re-attached.

This illustrates the following rule: the topology of $M^{a}$ does not change except when a passes the height of a critical point; at this point, a $\gamma$ -cell is attached to $M^{a}$ , where $\gamma$ is the index of the point. This does not address what happens when two critical points are at the same height, which can be resolved by a slight perturbation of $f.$ In the case of a landscape or a manifold embedded in Euclidean space, this perturbation might simply be tilting slightly, rotating the coordinate system.

One must take care to make the critical points non-degenerate. To see what can pose a problem, let $M=\mathbb {R}$ and let $f(x)=x^{3}.$ Then 0 is a critical point of $f,$ but the topology of $M^{a}$ does not change when a passes $0.$ The problem is that the second derivative is $f''(0)=0$ —that is, the Hessian of f vanishes and the critical point is degenerate. This situation is unstable, since by slightly deforming f to $f(x)=x^{3}+\epsilon x$ , the degenerate critical point is either removed ( $\epsilon >0$ ) or breaks up into two non-degenerate critical points ( $\epsilon <0$ ).

## Formal development

For a real-valued smooth function $f:M\to \mathbb {R}$ on a differentiable manifold $M,$ the points where the differential of f vanishes are called critical points of f and their images under f are called critical values. If at a critical point p the matrix of second partial derivatives (the Hessian matrix) is non-singular, then p is called a ***non-degenerate critical point***; if the Hessian is singular then p is a ***degenerate critical point***.

For the functions $f(x)=a+bx+cx^{2}+dx^{3}+\cdots$ from $\mathbb {R}$ to $\mathbb {R} ,$ f has a critical point at the origin if $b=0,$ which is non-degenerate if $c\neq 0$ (that is, f is of the form $a+cx^{2}+\cdots$ ) and degenerate if $c=0$ (that is, f is of the form $a+dx^{3}+\cdots$ ). A less trivial example of a degenerate critical point is the origin of the monkey saddle.

The **index** of a non-degenerate critical point p of f is the dimension of the largest subspace of the tangent space to M at p on which the Hessian is negative definite. This corresponds to the intuitive notion that the index is the number of directions in which f decreases. The degeneracy and index of a critical point are independent of the choice of the local coordinate system used, as shown by Sylvester's Law.

### Morse lemma

Let p be a non-degenerate critical point of $f\colon M\to \mathbb {R} .$ Then there exists a chart $\left(x_{1},x_{2},\ldots ,x_{n}\right)$ in a neighborhood U of p such that $x_{i}(p)=0$ for all i and $f(x)=f(p)-x_{1}^{2}-\cdots -x_{\gamma }^{2}+x_{\gamma +1}^{2}+\cdots +x_{n}^{2}$ throughout $U.$ Here $\gamma$ is equal to the index of f at p . As a corollary of the Morse lemma, one sees that non-degenerate critical points are isolated. (Regarding an extension to the complex domain see Complex Morse Lemma. For a generalization, see Morse–Palais lemma).

### Fundamental theorems

A smooth real-valued function on a manifold M is a **Morse function** if it has no degenerate critical points. A basic result of Morse theory says that almost all functions are Morse functions. Technically, the Morse functions form an open, dense subset of all smooth functions $M\to \mathbb {R}$ in the $C^{2}$ topology. This is sometimes expressed as "a typical function is Morse" or "a generic function is Morse".

As indicated before, we are interested in the question of when the topology of $M^{a}=f^{-1}(-\infty ,a]$ changes as a varies. Half of the answer to this question is given by the following theorem.

Theorem.

Suppose

f

is a smooth real-valued function on

$M,$

$a<b,$

$f^{-1}[a,b]$

is

compact

, and there are no critical values between

a

and

$b.$

Then

$M^{a}$

is

diffeomorphic

to

$M^{b},$

and

$M^{b}$

deformation retracts

onto

$M^{a}.$

It is also of interest to know how the topology of $M^{a}$ changes when a passes a critical point. The following theorem answers that question.

Theorem.

Suppose

f

is a smooth real-valued function on

M

and

p

is a non-degenerate critical point of

f

of index

$\gamma ,$

and that

$f(p)=q.$

Suppose

$f^{-1}[q-\varepsilon ,q+\varepsilon ]$

is compact and contains no critical points besides

$p.$

Then

$M^{q+\varepsilon }$

is

homotopy equivalent

to

$M^{q-\varepsilon }$

with a

$\gamma$

-cell attached.

These results generalize and formalize the 'rule' stated in the previous section.

Using the two previous results and the fact that there exists a Morse function on any differentiable manifold, one can prove that any differentiable manifold is a CW complex with an n -cell for each critical point of index $n.$ To do this, one needs the technical fact that one can arrange to have a single critical point on each critical level, which is usually proven by using gradient-like vector fields to rearrange the critical points.

### Morse inequalities

Morse theory can be used to prove some strong results on the homology of manifolds. The number of critical points of index $\gamma$ of $f:M\to \mathbb {R}$ is equal to the number of $\gamma$ cells in the CW structure on M obtained from "climbing" $f.$ Using the fact that the alternating sum of the ranks of the homology groups of a topological space is equal to the alternating sum of the ranks of the chain groups from which the homology is computed, then by using the cellular chain groups (see cellular homology) it is clear that the Euler characteristic $\chi (M)$ is equal to the sum $\sum (-1)^{\gamma }C^{\gamma }\,=\chi (M)$ where $C^{\gamma }$ is the number of critical points of index $\gamma .$ Also by cellular homology, the rank of the n th homology group of a CW complex M is less than or equal to the number of n -cells in $M.$ Therefore, the rank of the $\gamma$ th homology group, that is, the Betti number $b_{\gamma }(M)$ , is less than or equal to the number of critical points of index $\gamma$ of a Morse function on $M.$ These facts can be strengthened to obtain the ***Morse inequalities***: $C^{\gamma }-C^{\gamma -1}\pm \cdots +(-1)^{\gamma }C^{0}\geq b_{\gamma }(M)-b_{\gamma -1}(M)\pm \cdots +(-1)^{\gamma }b_{0}(M).$

In particular, for any $\gamma \in \{0,\ldots ,n=\dim M\},$ one has $C^{\gamma }\geq b_{\gamma }(M).$

This gives a powerful tool to study manifold topology. Suppose on a closed manifold there exists a Morse function $f:M\to \mathbb {R}$ with precisely *k* critical points. In what way does the existence of the function f restrict M ? The case $k=2$ was studied by Georges Reeb in 1952; the Reeb sphere theorem states that M is homeomorphic to a sphere $S^{n}.$ The case $k=3$ is possible only in a small number of low dimensions, and *M* is homeomorphic to an Eells–Kuiper manifold. In 1982 Edward Witten developed an analytic approach to the Morse inequalities by considering the de Rham complex for the perturbed operator $d_{t}=e^{-tf}de^{tf}.$

### Application to classification of closed 2-manifolds

Morse theory has been used to classify closed 2-manifolds up to diffeomorphism. If M is oriented, then M is classified by its genus g and is diffeomorphic to a sphere with g handles: thus if $g=0,$ M is diffeomorphic to the 2-sphere; and if $g>0,$ M is diffeomorphic to the connected sum of g 2-tori. If N is unorientable, it is classified by a number $g>0$ and is diffeomorphic to the connected sum of g real projective spaces $\mathbf {RP} ^{2}.$ In particular two closed 2-manifolds are homeomorphic if and only if they are diffeomorphic.

### Morse homology

Morse homology is a particularly easy way to understand the homology of smooth manifolds. It is defined using a generic choice of Morse function and Riemannian metric. The basic theorem is that the resulting homology is an invariant of the manifold (that is, independent of the function and metric) and isomorphic to the singular homology of the manifold; this implies that the Morse and singular Betti numbers agree and gives an immediate proof of the Morse inequalities. An infinite dimensional analog of Morse homology in symplectic geometry is known as Floer homology.

## Morse–Bott theory

The notion of a Morse function can be generalized to consider functions that have nondegenerate manifolds of critical points. A **Morse–Bott function** is a smooth function on a manifold whose critical set is a closed submanifold and whose Hessian is non-degenerate in the normal direction. (Equivalently, the kernel of the Hessian at a critical point equals the tangent space to the critical submanifold.) A Morse function is the special case where the critical manifolds are zero-dimensional (so the Hessian at critical points is non-degenerate in every direction, that is, has no kernel).

The index is most naturally thought of as a pair $\left(i_{-},i_{+}\right),$ where $i_{-}$ is the dimension of the unstable manifold at a given point of the critical manifold, and $i_{+}$ is equal to $i_{-}$ plus the dimension of the critical manifold. If the Morse–Bott function is perturbed by a small function on the critical locus, the index of all critical points of the perturbed function on a critical manifold of the unperturbed function will lie between $i_{-}$ and $i_{+}.$

Morse–Bott functions are useful because generic Morse functions are difficult to work with; the functions one can visualize, and with which one can easily calculate, typically have symmetries. They often lead to positive-dimensional critical manifolds. Raoul Bott used Morse–Bott theory in his original proof of the Bott periodicity theorem.

Round functions are examples of Morse–Bott functions, where the critical sets are (disjoint unions of) circles.

Morse homology can also be formulated for Morse–Bott functions; the differential in Morse–Bott homology is computed by a spectral sequence. Frederic Bourgeois sketched an approach in the course of his work on a Morse–Bott version of symplectic field theory, but this work was never published due to substantial analytic difficulties.

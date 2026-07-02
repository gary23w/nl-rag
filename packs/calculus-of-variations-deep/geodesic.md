---
title: "Geodesic"
source: https://en.wikipedia.org/wiki/Geodesic
domain: calculus-of-variations-deep
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, beltrami identity, hamilton principle
fetched: 2026-07-02
---

# Geodesic

In geometry, a **geodesic** (/ˌdʒiː.əˈdɛsɪk, -oʊ-, -ˈdiːsɪk, -zɪk/) is a curve representing in some sense the locally shortest path (arc) between two points in a surface, or more generally in a Riemannian manifold. The term also has meaning in any differentiable manifold with a connection. It is a generalization of the notion of a "straight line".

The noun *geodesic* and the adjective *geodetic* come from *geodesy*, the science of measuring the size and shape of Earth, though many of the underlying principles can be applied to any ellipsoidal geometry. In the original sense, a geodesic was the shortest route between two points on the Earth's surface. For a spherical Earth, it is a segment of a great circle (see also great-circle distance). The term has since been generalized to more abstract mathematical spaces; for example, in graph theory, one might consider a geodesic between two vertices/nodes of a graph.

In a Riemannian manifold or submanifold, geodesics are characterised by the property of having vanishing geodesic curvature. More generally, in the presence of an affine connection, a geodesic is defined to be a curve whose tangent vectors remain parallel if they are transported along it. Applying this to the Levi-Civita connection of a Riemannian metric recovers the previous notion.

Geodesics are of particular importance in general relativity. Timelike geodesics in general relativity describe the motion of free falling test particles.

## Introduction

A locally shortest path between two given points in a curved space, assumed to be a Riemannian manifold, can be defined by using the equation for the length of a curve (a function *f* from an open interval of **R** to the space), and then minimizing this length between the points using the calculus of variations. This has some minor technical problems because there is an infinite-dimensional space of different ways to parameterize the shortest path. It is simpler to restrict the set of curves to those that are parameterized "with constant speed" 1, meaning that the distance from *f*(*s*) to *f*(*t*) along the curve equals |*s*−*t*|. Equivalently, a different quantity may be used, termed the energy of the curve; minimizing the energy leads to the same equations for a geodesic (here "constant velocity" is a consequence of minimization). Intuitively, one can understand this second formulation by noting that an elastic band stretched between two points will contract its width, and in so doing will minimize its energy. The resulting shape of the band is a geodesic.

It is possible that several different curves between two points minimize the distance, as is the case for two diametrically opposite points on a sphere. In such a case, any of these curves is a geodesic.

A contiguous segment of a geodesic is again a geodesic.

In general, geodesics are not the same as "shortest curves" between two points, though the two concepts are closely related. The difference is that geodesics are only *locally* the shortest distance between points, and are parameterized with "constant speed". Going the "long way round" on a great circle between two points on a sphere is a geodesic but not the shortest path between the points. The map $t\to t^{2}$ from the unit interval on the real number line to itself gives the shortest path between 0 and 1, but is not a geodesic because the velocity of the corresponding motion of a point is not constant.

Geodesics are commonly seen in the study of Riemannian geometry and more generally metric geometry. In general relativity, geodesics in spacetime describe the motion of point particles under the influence of gravity alone. In particular, the path taken by a falling rock, an orbiting satellite, or the shape of a planetary orbit are all geodesics in curved spacetime. More generally, the topic of sub-Riemannian geometry deals with the paths that objects may take when they are not free, and their movement is constrained in various ways.

This article presents the mathematical formalism involved in defining, finding, and proving the existence of geodesics, in the case of Riemannian manifolds. The article Levi-Civita connection discusses the more general case of a pseudo-Riemannian manifold and geodesic (general relativity) discusses the special case of general relativity in greater detail.

### Examples

The most familiar examples are the straight lines in Euclidean geometry. On a sphere, the images of geodesics are the great circles. The shortest path from point *A* to point *B* on a sphere is given by the shorter arc of the great circle passing through *A* and *B*. If *A* and *B* are antipodal points, then there are *infinitely many* shortest paths between them. Geodesics on an ellipsoid behave in a more complicated way than on a sphere; in particular, they are not closed in general (see figure).

### Triangles

A **geodesic triangle** is formed by the geodesics joining each pair out of three points on a given surface. On the sphere, the geodesics are great circle arcs, forming a spherical triangle.

## Metric geometry

In metric geometry, a geodesic is a curve which is everywhere locally a distance minimizer. More precisely, a curve *γ* : *I* → *M* from an interval *I* of the reals to the metric space *M* is a **geodesic** if there is a constant *v* ≥ 0 such that for any *t* ∈ *I* there is a neighborhood *J* of *t* in *I* such that for any *t*1, *t*2 ∈ *J* we have

$d(\gamma (t_{1}),\gamma (t_{2}))=v\left|t_{1}-t_{2}\right|.$

This generalizes the notion of geodesic for Riemannian manifolds. However, in metric geometry the geodesic considered is often equipped with natural parameterization, i.e. in the above identity *v* = 1 and

$d(\gamma (t_{1}),\gamma (t_{2}))=\left|t_{1}-t_{2}\right|.$

If the last equality is satisfied for all *t*1, *t*2 ∈ *I*, the geodesic is called a **minimizing geodesic** or **shortest path**.

In general, a metric space may have no geodesics, except constant curves. At the other extreme, any two points in a length metric space are joined by a minimizing sequence of rectifiable paths, although this minimizing sequence need not converge to a geodesic. The metric Hopf-Rinow theorem provides situations where a length space is automatically a geodesic space.

Common examples of geodesic metric spaces that are often not manifolds include metric graphs, (locally compact) metric polyhedral complexes, infinite-dimensional pre-Hilbert spaces, and real trees.

## Riemannian geometry

In a Riemannian manifold M with metric tensor g , the length L of a continuously differentiable curve $\gamma :[a,b]\to M$ is defined by

$L(\gamma )=\int _{a}^{b}{\sqrt {g_{\gamma (t)}({\dot {\gamma }}(t),{\dot {\gamma }}(t))}}\,dt.$

The distance $d(p,q)$ between two points p and q of M is defined as the infimum of the length taken over all continuous, piecewise continuously differentiable curves $\gamma :[a,b]\to M$ such that $\gamma (a)=p$ and $\gamma (b)=q$ . In Riemannian geometry, all geodesics are locally distance-minimizing paths, but the converse is not true. In fact, only paths that are both locally distance minimizing and parameterized proportionately to arc-length are geodesics.

Another equivalent way of defining geodesics on a Riemannian manifold, is to define them as the minima of the following action or energy functional

$E(\gamma )={\frac {1}{2}}\int _{a}^{b}g_{\gamma (t)}({\dot {\gamma }}(t),{\dot {\gamma }}(t))\,dt.$

All minima of E are also minima of L , but L is a bigger set since paths that are minima of L can be arbitrarily re-parameterized (without changing their length), while minima of E cannot. For a piecewise $C^{1}$ curve (more generally, a $W^{1,2}$ curve), the Cauchy–Schwarz inequality gives

$L(\gamma )^{2}\leq 2(b-a)E(\gamma )$

with equality if and only if $g(\gamma ',\gamma ')$ is equal to a constant a.e.; the path should be travelled at constant speed. It happens that minimizers of $E(\gamma )$ also minimize $L(\gamma )$ , because they turn out to be affinely parameterized, and the inequality is an equality. The usefulness of this approach is that the problem of seeking minimizers of E is a more robust variational problem. Indeed, $E(\gamma )$ is a "convex function" of $\gamma$ , so that within each isotopy class of "reasonable functions", one ought to expect existence, uniqueness, and regularity of minimizers. In contrast, "minimizers" of the functional $L(\gamma )$ are generally not very regular, because arbitrary reparameterizations are allowed.

The Euler–Lagrange equations of motion for the functional E are then given in local coordinates by

${\frac {d^{2}x^{\lambda }}{dt^{2}}}+\Gamma _{\mu \nu }^{\lambda }{\frac {dx^{\mu }}{dt}}{\frac {dx^{\nu }}{dt}}=0,$

where $\Gamma _{\mu \nu }^{\lambda }$ are the Christoffel symbols of the metric. This is the **geodesic equation**, discussed below.

### Calculus of variations

Techniques of the classical calculus of variations can be applied to examine the energy functional E . The first variation of energy is defined in local coordinates by

$\delta E(\gamma )(\varphi )=\left.{\frac {\partial }{\partial t}}\right|_{t=0}E(\gamma +t\varphi ).$

The critical points of the first variation are precisely the geodesics. The second variation is defined by

$\delta ^{2}E(\gamma )(\varphi ,\psi )=\left.{\frac {\partial ^{2}}{\partial s\,\partial t}}\right|_{s=t=0}E(\gamma +t\varphi +s\psi ).$

In an appropriate sense, zeros of the second variation along a geodesic $\gamma$ arise along Jacobi fields. Jacobi fields are thus regarded as variations through geodesics.

By applying variational techniques from classical mechanics, one can also regard geodesics as Hamiltonian flows. They are solutions of the associated Hamilton equations, with (pseudo-)Riemannian metric taken as Hamiltonian.

## Affine geodesics

A **geodesic** on a smooth manifold M with an affine connection $\nabla$ is defined as a curve $\gamma (t)$ such that parallel transport along the curve preserves the tangent vector to the curve, so

| $\nabla _{\dot {\gamma }}{\dot {\gamma }}=0$ |   | 1 |
|---|---|---|

at each point along the curve, where ${\dot {\gamma }}$ is the derivative with respect to t . More precisely, in order to define the covariant derivative of ${\dot {\gamma }}$ it is necessary first to extend ${\dot {\gamma }}$ to a continuously differentiable vector field in an open set. However, the resulting value of (**1**) is independent of the choice of extension.

Using local coordinates on M , we can write the **geodesic equation** (using the summation convention) as

${\frac {d^{2}\gamma ^{\lambda }}{dt^{2}}}+\Gamma _{\mu \nu }^{\lambda }{\frac {d\gamma ^{\mu }}{dt}}{\frac {d\gamma ^{\nu }}{dt}}=0\ ,$

where $\gamma ^{\mu }=x^{\mu }\circ \gamma (t)$ are the coordinates of the curve $\gamma (t)$ and $\Gamma _{\mu \nu }^{\lambda }$ are the Christoffel symbols of the connection $\nabla$ . This is an ordinary differential equation for the coordinates. It has a unique solution, given an initial position and an initial velocity. Therefore, from the point of view of classical mechanics, geodesics can be thought of as trajectories of free particles in a manifold. Indeed, the equation $\nabla _{\dot {\gamma }}{\dot {\gamma }}=0$ means that the acceleration vector of the curve has no components in the direction of the surface (and therefore it is perpendicular to the tangent plane of the surface at each point of the curve). So, the motion is completely determined by the bending of the surface. This is also the idea of general relativity where particles move on geodesics and the bending is caused by gravity.

### Existence and uniqueness

The *local existence and uniqueness theorem* for geodesics states that geodesics on a smooth manifold with an affine connection exist, and are unique. More precisely:

For any point

p

in

M

and for any vector

V

in

T

p

M

(the

tangent space

to

M

at

p

) there exists a unique geodesic

$\gamma \,$

:

I

→

M

such that

$\gamma (0)=p\,$

and

${\dot {\gamma }}(0)=V,$

where

I

is a maximal

open interval

in

R

containing 0.

The proof of this theorem follows from the theory of ordinary differential equations, by noticing that the geodesic equation is a second-order ODE. Existence and uniqueness then follow from the Picard–Lindelöf theorem for the solutions of ODEs with prescribed initial conditions. γ depends smoothly on both *p* and *V*.

In general, *I* may not be all of **R** as for example for an open disc in **R**2. Any γ extends to all of ℝ if and only if M is geodesically complete.

### Geodesic flow

**Geodesic flow** is a local **R**-action on the tangent bundle *TM* of a manifold *M* defined in the following way

$G^{t}(V)={\dot {\gamma }}_{V}(t)$

where *t* ∈ **R**, *V* ∈ *TM* and $\gamma _{V}$ denotes the geodesic with initial data ${\dot {\gamma }}_{V}(0)=V$ . Thus, *$G^{t}(V)=\exp(tV)$* is the exponential map of the vector *tV*. A closed orbit of the geodesic flow corresponds to a closed geodesic on *M*.

On a (pseudo-)Riemannian manifold, the geodesic flow is identified with a Hamiltonian flow on the cotangent bundle. The Hamiltonian is then given by the inverse of the (pseudo-)Riemannian metric, evaluated against the canonical one-form. In particular the flow preserves the (pseudo-)Riemannian metric g , i.e.

$g(G^{t}(V),G^{t}(V))=g(V,V).\,$

In particular, when *V* is a unit vector, $\gamma _{V}$ remains unit speed throughout, so the geodesic flow is tangent to the unit tangent bundle. Liouville's theorem implies invariance of a kinematic measure on the unit tangent bundle.

### Geodesic spray

The geodesic flow defines a family of curves in the tangent bundle. The derivatives of these curves define a vector field on the total space of the tangent bundle, known as the **geodesic spray**.

More precisely, an affine connection gives rise to a splitting of the double tangent bundle TT*M* into horizontal and vertical bundles:

$TTM=H\oplus V.$

The double tangent bundle can be visualized as the space of simultaneous changes of both the base point and velocity, without committing to any method to transport velocity across base points.

For any $x\in M,\;v\in T_{x}M$ , the vertical fiber $V_{(x,v)}$ is determined by the projection map $\pi :TM\to M$ . It consists of all ways to change the velocity v while fixing the base point x , and it is essentially a copy of $T_{x}M$ translated from $(x,0)$ to $(x,v)$ . The affine connection then selects where $(x,v)$ would land under a change of base point while "fixing" velocity, which spans out the horizontal fiber $H_{(x,v)}$ . Conversely, given the split, transporting a vector v along a trajectory $\gamma$ simply means dragging the vector along the horizontal bundle, i.e. lifting the trajectory twice, from $\gamma (t)$ in M to $(\gamma (t),{\dot {\gamma }}(t))$ in $TM$ to $(\gamma (t),v(t),a(t))$ in H , with the condition that $d\pi (\gamma (t),v,a(t))=(\gamma (t),{\dot {\gamma }}(t))$ .

The geodesic spray is the unique horizontal vector field *W* satisfying

$d\pi W_{(x,v)}=(x,v)$

at each point $x\in M,\;v\in T_{x}M$ , here $d\pi :TTM\to TM$ denotes the pushforward (differential) along the projection $\pi :TM\to M$ . Intuitively, $d\pi$ discards the change to velocity and preserves change to base point.

More generally, the same construction allows one to construct a vector field for any Ehresmann connection on the tangent bundle. For the resulting vector field to be a spray (on the deleted tangent bundle T*M* \ {0}) it is enough that the connection be equivariant under positive rescalings, that is, it is enough that, if $w\in T_{x}M$ is transported by $\gamma$ to $w'\in T_{x'}M$ , then $kw$ must be transported to $kw'$ for any $k>0$ . It is not necessary that, if $u\in T_{x}M$ is also transported to $u'\in T_{x'}M$ , then $w+u$ must be transported $w'+u'$ .

That is, (cf. Ehresmann connection#Vector bundles and covariant derivatives) it is enough that the horizontal distribution satisfy

$H_{\lambda X}=d(S_{\lambda })_{X}H_{X}\,$

for every *X* ∈ T*M* \ {0} and λ > 0. Here *d*(*S*λ) is the pushforward along the scalar homothety $S_{\lambda }:X\mapsto \lambda X.$ A particular case of a non-linear connection arising in this manner is that associated to a Finsler manifold.

Equivariance under positive rescalings is necessary to ensure that vector transport is well-defined along directed paths, that is, given any parameterization $\gamma :I\to M$ of the curve, and any strictly monotonically increasing "change of timing" $f:\mathbb {R} \to \mathbb {R}$ , the new parameterization $\gamma \circ f$ still produces the same vector transport. Without equivariance under positive rescalings, vector transport along a directed path depends on the specific parameterization.

### Affine and projective geodesics

Equation (**1**) is invariant under affine reparameterizations; that is, parameterizations of the form

$t\mapsto at+b$

where *a* and *b* are constant real numbers. Thus apart from specifying a certain class of embedded curves, the geodesic equation also determines a preferred class of parameterizations on each of the curves. Accordingly, solutions of (**1**) are called geodesics with **affine parameter**.

An affine connection is *determined by* its family of affinely parameterized geodesics, up to torsion (Spivak 1999, Chapter 6, Addendum I). The torsion itself does not, in fact, affect the family of geodesics, since the geodesic equation depends only on the symmetric part of the connection. More precisely, if $\nabla ,{\bar {\nabla }}$ are two connections such that the difference tensor

$D(X,Y)=\nabla _{X}Y-{\bar {\nabla }}_{X}Y$

is skew-symmetric, then $\nabla$ and ${\bar {\nabla }}$ have the same geodesics, with the same affine parameterizations. Furthermore, there is a unique connection having the same geodesics as $\nabla$ , but with vanishing torsion.

Geodesics without a particular parameterization are described by a projective connection.

## Computational methods

Efficient solvers for the minimal geodesic problem on surfaces have been proposed by Mitchell, Kimmel, Crane, and others.

## Ribbon test

A ribbon "test" is a way of finding a geodesic on a physical surface. The idea is to fit a bit of paper around a straight line (a ribbon) onto a curved surface as closely as possible without stretching or squishing the ribbon (without changing its internal geometry).

For example, when a ribbon is wound as a ring around a cone, the ribbon would not lie on the cone's surface but stick out, so that circle is not a geodesic on the cone. If the ribbon is adjusted so that all its parts touch the cone's surface, it would give an approximation to a geodesic.

Mathematically the ribbon test can be formulated as finding a mapping $f:N(\ell )\to S$ of a neighborhood N of a line $\ell$ in a plane into a surface S so that the mapping f "doesn't change the distances around $\ell$ by much"; that is, at the distance $\varepsilon$ from l we have $g_{N}-f^{*}(g_{S})=O(\varepsilon ^{2})$ where $g_{N}$ and $g_{S}$ are metrics on N and S .

## Examples of applications

While geometric in nature, the idea of a shortest path is so general that it easily finds extensive use in nearly all sciences, and in some other disciplines as well.

### Topology and geometric group theory

- In a surface with negative Euler characteristic, any (free) homotopy class determines a unique (closed) geodesic for a hyperbolic metric. These geodesics contribute significantly to the geometric understanding of the action of mapping classes.
- Geodesic metric spaces and length spaces behave particularly well with isometric group actions (Švarc-Milnor lemma, Hopf-Rinow theorem, Morse lemma...). They are often an adequate framework for generalizing results from Riemannian geometry to constructions that reflect the geometry of a group. For instance, Gromov-hyperbolicity can be understood in terms of geodesic triangle thinness, and CAT(0) can be stated in terms of angles between geodesics.

### Probability, statistics and machine learning

- Optimal transport can be understood as the problem of finding geodesic paths in spaces of measures.
- In information geometry, divergences such as the Kullback-Leibler divergence play a role analogous to that of a Riemannian metric, allowing analogies for connections and geodesics.

### Physics

- In classical mechanics, trajectories minimize an energy according to the Hamilton-Jacobi equation, which can be regarded as a similar idea to geodesics. In some special cases, the two notions actually coincide.
- Relativity theory models spacetime as a Lorentzian manifold, where light follows Lorentzian geodesics.

### Chemistry

- In theoretical and computational chemistry, the intrinsic reaction coordinate of a potential energy surface (PES) can be calculated as a geodesic between local minima (intermediates) and saddle points (transition states).
- In molecular dynamics, protein conformations can be treated as points on a curved manifold, wherein geodesics represent the shortest, least-distorting paths between structures and can help approximate observed transitions and intramolecular interactions.

### Biology

- The study of how the nervous system optimizes muscular movement may be approached by endowing a configuration space of the body with a Riemannian metric that measures the effort, so that the problem can be stated in terms of geodesy.
- Geodesic distance is often used to measure the length of paths for signal propagation in neurons.
- The structures of geodesics in large molecules plays a role in the study of protein folds.
- The structure of compound eyes, many parts of which are being held together and supported by a geodesic dome grid on the outside surface of the eye.

### Engineering

Geodesics serve as the basis to calculate:

- geodesic airframes; see geodesic airframe or geodetic airframe
- horizontal distances on or near Earth; see Earth geodesics
- mapping images on surfaces, for rendering; see UV mapping
- robot motion planning (e.g., when painting car parts); see Shortest path problem
- geodesic shortest path (GSP) correction over Poisson surface reconstruction (e.g. in digital dentistry); without GSP reconstruction often results in self-intersections within the surface

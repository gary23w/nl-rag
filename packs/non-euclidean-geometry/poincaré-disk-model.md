---
title: "Poincaré disk model"
source: https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model
domain: non-euclidean-geometry
license: CC-BY-SA-4.0
tags: non-euclidean geometry, hyperbolic geometry, elliptic geometry, parallel postulate
fetched: 2026-07-02
---

# Poincaré disk model

In geometry, the **Poincaré disk model**, also called the **conformal disk model**, is a model of 2-dimensional hyperbolic geometry in which all points are inside the unit disk, and straight lines are either circular arcs contained within the disk that are orthogonal to the unit circle or diameters of the unit circle.

The group of orientation preserving isometries of the disk model is given by the projective special unitary group PSU(1,1), the quotient of the special unitary group SU(1,1) by its center {*I*, −*I*}.

Along with the Klein model and the Poincaré half-space model, it was proposed by Eugenio Beltrami who used these models to show that hyperbolic geometry was equiconsistent with Euclidean geometry. It is named after Henri Poincaré, because his rediscovery of this representation fourteen years later became better known than the original work of Beltrami.

The **Poincaré ball model** is the similar model for *3* or *n*-dimensional hyperbolic geometry in which the points of the geometry are in the *n*-dimensional unit ball.

## History

The disk model was first described by Bernhard Riemann in an 1854 lecture (published 1868), which inspired an 1868 paper by Eugenio Beltrami. Henri Poincaré employed it in his 1882 treatment of hyperbolic, parabolic and elliptic functions, but it became widely known following Poincaré's presentation in his 1905 philosophical treatise, *Science and Hypothesis*. There he describes a world, now known as the Poincaré disk, in which space was Euclidean, but which appeared to its inhabitants to satisfy the axioms of hyperbolic geometry:

> "Suppose, for example, a world enclosed in a large sphere and subject to the following laws: The temperature is not uniform; it is greatest at their centre, and gradually decreases as we move towards the circumference of the sphere, where it is absolute zero. The law of this temperature is as follows: If R be the radius of the sphere, and r the distance of the point considered from the centre, the absolute temperature will be proportional to $R^{2}-r^{2}$ . Further, I shall suppose that in this world all bodies have the same co-efficient of dilatation, so that the linear dilatation of any body is proportional to its absolute temperature. Finally, I shall assume that a body transported from one point to another of different temperature is instantaneously in thermal equilibrium with its new environment. ... If they construct a geometry, it will not be like ours, which is the study of the movements of our invariable solids; it will be the study of the changes of position which they will have thus distinguished, and will be 'non-Euclidean displacements,' and *this will be non-Euclidean geometry*. So that beings like ourselves, educated in such a world, will not have the same geometry as ours." (pp.65-68)

Poincaré's disk was an important piece of evidence for the hypothesis that the choice of spatial geometry is conventional rather than factual, especially in the influential philosophical discussions of Rudolf Carnap and of Hans Reichenbach.

## Lines and distance

Hyperbolic **straight lines** or geodesics consist of all arcs of Euclidean circles contained within the disk that are orthogonal to the boundary of the disk, plus all diameters of the disk.

Distances in this model are Cayley–Klein metrics. Given two distinct points *p* and *q* inside the disk, the unique hyperbolic line connecting them intersects the boundary at two ideal points, *a* and *b*. Label them so that the points are, in order, *a*, *p*, *q*, *b*, that is, so that |*aq*| > |*ap*| and |*pb*| > |*qb*|.

The hyperbolic distance between *p* and *q* is then

$d(p,q)=\ln {\frac {\left|aq\right|\,\left|pb\right|}{\left|ap\right|\,\left|qb\right|}}.$

The vertical bars indicate Euclidean length of the line segment connecting the points between them in the model (not along the circle arc); ln is the natural logarithm.

Equivalently, if *u* and *v* are two vectors in real *n*-dimensional vector space **R***n* with the usual Euclidean norm, both of which have norm less than 1, then we may define an isometric invariant by

$\delta (u,v)=2{\frac {\lVert u-v\rVert ^{2}}{(1-\lVert u\rVert ^{2})(1-\lVert v\rVert ^{2})}}\,,$

where $\lVert \cdot \rVert$ denotes the usual Euclidean norm. Then the distance function is

${\begin{aligned}d(u,v)&=\operatorname {arcosh} (1+\delta (u,v))\\&=2\operatorname {arsinh} {\sqrt {\frac {\delta (u,v)}{2}}}\\\,&=2\ln {\frac {\lVert u-v\rVert +{\sqrt {\lVert u\rVert ^{2}\lVert v\rVert ^{2}-2u\cdot v+1}}}{\sqrt {(1-\lVert u\rVert ^{2})(1-\lVert v\rVert ^{2})}}}.\end{aligned}}$

Such a distance function is defined for any two vectors of norm less than one, and makes the set of such vectors into a metric space which is a model of hyperbolic space of constant curvature −1. The model has the conformal property that the angle between two intersecting curves in hyperbolic space is the same as the angle in the model.

Specializing to the case where one of the points is the origin and the Euclidean distance between the points is *r*, the hyperbolic distance is: $\ln \left({\frac {1+r}{1-r}}\right)=2\operatorname {artanh} r$ where $\operatorname {artanh}$ is the inverse hyperbolic function of the hyperbolic tangent. If the two points lie on the same radius and point $x'=(r',\theta )$ lies between the origin and point $x=(r,\theta )$ , their hyperbolic distance is $\ln \left({\frac {1+r}{1-r}}\cdot {\frac {1-r'}{1+r'}}\right)=2(\operatorname {artanh} r-\operatorname {artanh} r').$ This reduces to the previous special case if $r'=0$ .

## Metric and curvature

The associated metric tensor of the Poincaré disk model is given by

$ds^{2}=4{\frac {\sum _{i}dx_{i}^{2}}{\left(1-\sum _{i}x_{i}^{2}\right)^{2}}}={\frac {4\,\lVert d\mathbf {x} \rVert {\vphantom {l}}^{2}}{{\bigl (}1-\lVert \mathbf {x} \rVert {\vphantom {l}}^{2}{\bigr )}^{2}}}$

where the *x**i* are the Cartesian coordinates of the ambient Euclidean space. (In comparison, the equation for the corresponding metric of the stereographic projection of the unit sphere looks equivalent, except for a sign difference in the denominator.)

An orthonormal frame with respect to this Riemannian metric is given by

$e_{i}={\frac {1}{2}}{\Bigl (}1-|\mathbf {x} |^{2}{\Bigr )}{\frac {\partial }{\partial x^{i}}},$

with dual coframe of 1-forms

$\theta ^{i}={\frac {2}{1-|\mathbf {x} |{\vphantom {l}}^{2}}}\,dx^{i}.$

### In two dimensions

In two dimensions, with respect to these frames and the Levi-Civita connection, the connection forms are given by the unique skew-symmetric matrix of 1-forms $\omega$ that is torsion-free, i.e., that satisfies the matrix equation $0=d\theta +\omega \wedge \theta$ . Solving this equation for $\omega$ yields

$\omega ={\frac {2(y\,dx-x\,dy)}{1-|\mathbf {x} |{\vphantom {l}}^{2}}}{\begin{pmatrix}0&1\\-1&0\end{pmatrix}},$

where the curvature matrix is

$\Omega =d\omega +\omega \wedge \omega =d\omega +0={\frac {-4\,dx\wedge dy}{{\bigl (}1-|\mathbf {x} |{\vphantom {l}}^{2}{\bigr )}^{2}}}{\begin{pmatrix}0&1\\-1&0\end{pmatrix}}.$

Therefore, the curvature of the hyperbolic disk is

$K=\Omega _{2}^{1}(e_{1},e_{2})=-1.$

## Construction of lines

### By compass and straightedge

The unique hyperbolic line through two points P and Q not on a diameter of the boundary circle can be constructed by:

- let $P'$ be the inversion in the boundary circle of point P
- let $Q'$ be the inversion in the boundary circle of point Q
- let M be the midpoint of segment $PP'$
- let N be the midpoint of segment $QQ'$
- Draw line m through M perpendicular to segment $PP'$
- Draw line n through N perpendicular to segment $QQ'$
- let C be where line m and line n intersect.
- Draw circle c with center C and going through P (and Q ).
- The part of circle c that is inside the disk is the hyperbolic line.

If P and Q are on a diameter of the boundary circle that diameter is the hyperbolic line.

Another way is:

- let M be the midpoint of segment $PQ$
- Draw line m through M perpendicular to segment $PQ$
- let $P'$ be the inversion in the boundary circle of point P
- let N be the midpoint of segment $PP'$
- Draw line n through N perpendicular to segment $PP'$
- let C be where line m and line n intersect.
- Draw circle c with center C and going through P (and Q ).
- The part of circle c that is inside the disk is the hyperbolic line.

### By analytic geometry

A basic construction of analytic geometry is to find a line through two given points. In the Poincaré disk model, lines in the plane are defined by portions of circles having equations of the form

$x^{2}+y^{2}+ax+by+1=0\,,$

which is the general form of a circle orthogonal to the unit circle, or else by diameters. Given two points *u = (u1,u2)* and *v = (v1,v2)* in the disk which do not lie on a diameter, we can solve for the circle of this form passing through both points, and obtain

${\begin{aligned}x^{2}+y^{2}&{}+{\frac {u_{2}(v_{1}^{2}+v_{2}^{2}+1)-v_{2}(u_{1}^{2}+u_{2}^{2}+1)}{u_{1}v_{2}-u_{2}v_{1}}}x\\[8pt]&{}+{\frac {v_{1}(u_{1}^{2}+u_{2}^{2}+1)-u_{1}(v_{1}^{2}+v_{2}^{2}+1)}{u_{1}v_{2}-u_{2}v_{1}}}y+1=0\,.\end{aligned}}$

If the points *u* and *v* are points on the boundary of the disk not lying at the endpoints of a diameter, the above simplifies to

$x^{2}+y^{2}+{\frac {2(u_{2}-v_{2})}{u_{1}v_{2}-u_{2}v_{1}}}x+{\frac {2(v_{1}-u_{1})}{u_{1}v_{2}-u_{2}v_{1}}}y+1=0\,.$

## Angles

We may compute the angle between the circular arc whose endpoints (*ideal points*) are given by unit vectors *u* and *v*, and the arc whose endpoints are *s* and *t*, by means of a formula. Since the ideal points are the same in the Klein model and the Poincaré disk model, the formulas are identical for each model.

If both models' lines are diameters, so that *v* = −*u* and *t* = −*s*, then we are merely finding the angle between two unit vectors, and the formula for the angle θ is

$\cos(\theta )=u\cdot s\,.$

If *v* = −*u* but not *t* = −*s*, the formula becomes, in terms of the wedge product ( $\wedge$ ),

$\cos ^{2}(\theta )={\frac {P^{2}}{QR}},$

where

$P=u\cdot (s-t)\,,$

$Q=u\cdot u\,,$

$R=(s-t)\cdot (s-t)-(s\wedge t)\cdot (s\wedge t)\,.$

If both chords are not diameters, the general formula obtains

$\cos ^{2}(\theta )={\frac {P^{2}}{QR}}\,,$

where

$P=(u-v)\cdot (s-t)-(u\wedge v)\cdot (s\wedge t)\,,$

$Q=(u-v)\cdot (u-v)-(u\wedge v)\cdot (u\wedge v)\,,$

$R=(s-t)\cdot (s-t)-(s\wedge t)\cdot (s\wedge t)\,.$

Using the Binet–Cauchy identity and the fact that these are unit vectors we may rewrite the above expressions purely in terms of the dot product, as

$P=(u-v)\cdot (s-t)+(u\cdot t)(v\cdot s)-(u\cdot s)(v\cdot t)\,.$

$Q=(1-u\cdot v)^{2}\,,$

$R=(1-s\cdot t)^{2}\,.$

## Cycles

In the Euclidean plane the generalized circles (curves of constant curvature) are lines and circles. On the sphere, they are great and small circles. In the hyperbolic plane, there are 4 distinct types of generalized circles or *cycles*: circles, horocycles, hypercycles, and geodesics (or "hyperbolic lines"). In the Poincaré disk model, all of these are represented by straight lines or circles.

A Euclidean circle:

- that is completely inside the disk is a **hyperbolic circle**;
- that is inside the disk and tangent to the boundary is a **horocycle**;
- that intersects the boundary orthogonally is a **hyperbolic line**; and
- that intersects the boundary non-orthogonally is a **hypercycle**.

A Euclidean chord of the boundary circle:

- that goes through the center is a hyperbolic line; and
- that does not go through the center is a hypercycle.

### Circles

A **circle** (the set of all points in a plane that are at a given distance from a given point, its center) is a circle completely inside the disk not touching or intersecting its boundary. The hyperbolic center of the circle in the model does not in general correspond to the Euclidean center of the circle, but they are on the same radius of the Poincaré disk. (The Euclidean center is always closer to the center of the disk than the hyperbolic center.)

### Hypercycles

A **hypercycle** (the set of all points in a plane that are on one side and at a given distance from a given line, its axis) is a Euclidean circle arc or chord of the boundary circle that intersects the boundary circle at a positive but non-right angle. Its axis is the hyperbolic line that shares the same two ideal points. This is also known as an equidistant curve.

### Horocycles

A **horocycle** (a curve whose normal or perpendicular geodesics are limiting parallels, all converging asymptotically to the same ideal point), is a circle inside the disk that is tangent to the boundary circle of the disk. The point where it touches the boundary circle is not part of the horocycle. It is an ideal point and is the hyperbolic center of the horocycle. It is also the point to which all the perpendicular geodesics converge.

In the Poincaré disk model, the Euclidean points representing opposite "ends" of a horocycle converge to its center on the boundary circle, but in the hyperbolic plane every point of a horocycle is infinitely far from its center, and opposite ends of the horocycle are not connected. (Euclidean intuition can be misleading because the scale of the model increases to infinity at the boundary circle.)

## Relation to other models of hyperbolic geometry

### Relation to the Klein disk model

The Beltrami–Klein model (or Klein disk model) and the Poincaré disk are both models that project the whole hyperbolic plane in a disk. The two models are related through a projection on or from the hemisphere model. The Klein disk model is an orthographic projection to the hemisphere model while the Poincaré disk model is a stereographic projection.

An advantage of the Klein disk model is that lines in this model are Euclidean straight chords. A disadvantage is that the Klein disk model is not conformal (circles and angles are distorted).

When projecting the same lines in both models on one disk both lines go through the same two ideal points. (the ideal points remain on the same spot) also the pole of the chord in the Klein disk model is the center of the circle that contains the arc in the Poincaré disk model.

A point (*x*,*y*) in the Poincaré disk model maps to ${\textstyle \left({\frac {2x}{1+x^{2}+y^{2}}}\ ,\ {\frac {2y}{1+x^{2}+y^{2}}}\right)}$ in the Klein model.

A point (*x*,*y*) in the Klein model maps to ${\textstyle \left({\frac {x}{1+{\sqrt {1-x^{2}-y^{2}}}}}\ ,\ \ {\frac {y}{1+{\sqrt {1-x^{2}-y^{2}}}}}\right)}$ in the Poincaré disk model.

For ideal points $x^{2}+y^{2}=1$ and the formulas become $x=x\ ,\ y=y$ so the points are fixed.

If u is a vector of norm less than one representing a point of the Poincaré disk model, then the corresponding point of the Klein disk model is given by: $s={\frac {2u}{1+u\cdot u}}.$

Conversely, from a vector s of norm less than one representing a point of the Beltrami–Klein model, the corresponding point of the Poincaré disk model is given by: $u={\frac {s}{1+{\sqrt {1-s\cdot s}}}}={\frac {\left(1-{\sqrt {1-s\cdot s}}\right)s}{s\cdot s}}.$

### Relation to the Poincaré half-plane model

The Poincaré disk model and the Poincaré half-plane model are related by a Möbius transformation. If $u\in \mathbb {D}$ is a complex number of norm less than one representing a point of the Poincaré disk model, then the corresponding point $z\in \mathbb {H}$ of the upper half plane is given by the inverse of the Cayley transform ${\textstyle C:\mathbb {H} \to \mathbb {D} }$ : $C^{-1}(u)=z=i{\frac {1+u}{1-u}}.$ Under $C^{-1}$ , the points $\{0,1,-i,i\}\in \mathbb {D}$ are mapped to $\{i,\infty ,1,-1\}\in \mathbb {H}$ .

In terms of real coordinates, a point (*x*,*y*) in the disk model maps to ${\textstyle \left({\frac {2x}{x^{2}+(1-y)^{2}}}\ ,\ {\frac {1-x^{2}-y^{2}}{x^{2}+(1-y)^{2}}}\right)\,}$ in the halfplane model.

A point (*x*,*y*) in the halfplane model maps to ${\textstyle \left({\frac {2x}{x^{2}+(1+y)^{2}}}\ ,\ {\frac {x^{2}+y^{2}-1}{x^{2}+(1+y)^{2}}}\right)\,}$ in the disk model.

### Relation to the hyperboloid model

The Poincaré disk model, as well as the Beltrami–Klein model, are related to the hyperboloid model projectively. If we have a point [*t*, *x*1, ..., *x**n*] on the upper sheet of the hyperboloid of the hyperboloid model, thereby defining a point in the hyperboloid model, we may project it onto the hyperplane *t* = 0 by intersecting it with a line drawn through [−1, 0, ..., 0]. The result is the corresponding point of the Poincaré disk model.

For Cartesian coordinates (*t*, *xi*) on the hyperboloid and (*yi*) on the plane, the conversion formulas are: $y_{i}={\frac {x_{i}}{1+t}}$ $(t,x_{i})={\frac {\left(1+\sum {y_{i}^{2}},\,2y_{i}\right)}{1-\sum {y_{i}^{2}}}}\,.$

Compare the formulas for stereographic projection between a sphere and a plane.

- (The hyperboloid model can be represented as the equation t2 = x12 + x22 + 1, t > 1. It can be used to construct a Poincaré disk model as a projection viewed from (t = −1, x1 = 0, x2 = 0), projecting the upper half hyperboloid onto the unit disk at t = 0. The red geodesic in the Poincaré disk model projects to the brown geodesic on the green hyperboloid.) The hyperboloid model can be represented as the equation *t*2 = *x*12 + *x*22 + 1, *t* > 1. It can be used to construct a Poincaré disk model as a projection viewed from (*t* = −1, *x*1 = 0, *x*2 = 0), projecting the upper half hyperboloid onto the unit disk at *t* = 0. The red geodesic in the Poincaré disk model projects to the brown geodesic on the green hyperboloid.
- Animation of a partial {7,3} hyperbolic tiling of the hyperboloid rotated into the Poincaré perspective.

## Artistic realizations

M. C. Escher explored the concept of representing infinity on a two-dimensional plane. Discussions with Canadian mathematician Harold Scott MacDonald Coxeter around 1956 inspired Escher's interest in hyperbolic tessellations, which are regular tilings of the hyperbolic plane. Escher's wood engravings *Circle Limit I–IV* demonstrate this concept between 1958 and 1960, the final one being *Circle Limit IV: Heaven and Hell* in 1960. According to Bruno Ernst, the best of them is *Circle Limit III*.

*HyperRogue*, a roguelike game, uses the hyperbolic plane for its world geometry, and also uses the Poincaré disk model.

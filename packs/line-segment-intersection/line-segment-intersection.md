---
title: "Intersection (geometry)"
source: https://en.wikipedia.org/wiki/Line_segment_intersection
domain: line-segment-intersection
license: CC-BY-SA-4.0
tags: line segment intersection, bentley ottmann algorithm, sweep line, computational geometry
fetched: 2026-07-02
---

# Intersection (geometry)

(Redirected from

Line segment intersection

)

In geometry, an **intersection** between geometric objects (seen as sets of points) is a point, line, or curve common to two or more objects (such as lines, curves, planes, and surfaces). The simplest case in Euclidean geometry is the line–line intersection between two distinct lines, which either is one point (sometimes called a *vertex*) or empty (if the lines are parallel). Other types of geometric intersection include:

- Line–plane intersection
- Line–sphere intersection
- Intersection of a polyhedron with a line
- Line segment intersection
- Intersection curve

Determination of the intersection of flats – linear geometric objects embedded in a higher-dimensional space – is a simple task of linear algebra, namely the solution of a system of linear equations. In general the determination of an intersection leads to non-linear equations, which can be solved numerically, for example using Newton iteration. Intersection problems between a line and a conic section (circle, ellipse, parabola, etc.) or a quadric (sphere, cylinder, hyperboloid, etc.) lead to quadratic equations that can be easily solved. Intersections between quadrics lead to quartic equations that can be solved algebraically.

The notion of intersection from geometry has been exended to the status of an operation with sets, intersection (set theory), in works by Giuseppe Peano.

## On a plane

### Two lines

For the determination of the intersection point of two non-parallel lines

$a_{1}x+b_{1}y=c_{1},\ a_{2}x+b_{2}y=c_{2}$

one gets, from Cramer's rule or by substituting out a variable, the coordinates of the intersection point $(x_{s},y_{s})$  :

$x_{s}={\frac {c_{1}b_{2}-c_{2}b_{1}}{a_{1}b_{2}-a_{2}b_{1}}},\quad y_{s}={\frac {a_{1}c_{2}-a_{2}c_{1}}{a_{1}b_{2}-a_{2}b_{1}}}.\$

(If $a_{1}b_{2}-a_{2}b_{1}=0$ the lines are parallel and these formulas cannot be used because they involve dividing by 0.)

### Two line segments

For two non-parallel line segments $(x_{1},y_{1}),(x_{2},y_{2})$ and $(x_{3},y_{3}),(x_{4},y_{4})$ there is not necessarily an intersection point (see diagram), because the intersection point $(x_{0},y_{0})$ of the corresponding lines need not to be contained in the line segments. In order to check the situation one uses parametric representations of the lines:

$(x(s),y(s))=(x_{1}+s(x_{2}-x_{1}),y_{1}+s(y_{2}-y_{1})),$

$(x(t),y(t))=(x_{3}+t(x_{4}-x_{3}),y_{3}+t(y_{4}-y_{3})).$

The line segments intersect only in a common point $(x_{0},y_{0})$ of the corresponding lines if the corresponding parameters $s_{0},t_{0}$ fulfill the condition $0\leq s_{0},t_{0}\leq 1$ . The parameters $s_{0},t_{0}$ are the solution of the linear system

$s(x_{2}-x_{1})-t(x_{4}-x_{3})=x_{3}-x_{1},$

$s(y_{2}-y_{1})-t(y_{4}-y_{3})=y_{3}-y_{1}\ .$

It can be solved for *s* and *t* using Cramer's rule (see above). If the condition $0\leq s_{0},t_{0}\leq 1$ is fulfilled one inserts $s_{0}$ or $t_{0}$ into the corresponding parametric representation and gets the intersection point $(x_{0},y_{0})$ .

*Example:* For the line segments $(1,1),(3,2)$ and $(1,4),(2,-1)$ one gets the linear system

$2s-t=0$

$s+5t=3$

and $s_{0}={\tfrac {3}{11}},t_{0}={\tfrac {6}{11}}$ . That means: the lines intersect at point $({\tfrac {17}{11}},{\tfrac {14}{11}})$ .

*Remark:* Considering lines, instead of segments, determined by pairs of points, each condition $0\leq s_{0},t_{0}\leq 1$ can be dropped and the method yields the intersection point of the lines (see above).

### A line and a circle

For the intersection of

- line $ax+by=c$ and circle $x^{2}+y^{2}=r^{2}$

one solves the line equation for x or y and substitutes it into the equation of the circle and gets for the solution (using the formula of a quadratic equation) $(x_{1},y_{1}),(x_{2},y_{2})$ with

$x_{1/2}={\frac {ac\pm b{\sqrt {r^{2}(a^{2}+b^{2})-c^{2}}}}{a^{2}+b^{2}}}\ ,$

$y_{1/2}={\frac {bc\mp a{\sqrt {r^{2}(a^{2}+b^{2})-c^{2}}}}{a^{2}+b^{2}}}\ ,$

if $r^{2}(a^{2}+b^{2})-c^{2}>0\ .$ If this condition holds with strict inequality, there are two intersection points; in this case the line is called a secant line of the circle, and the line segment connecting the intersection points is called a chord of the circle.

If $r^{2}(a^{2}+b^{2})-c^{2}=0$ holds, there exists only one intersection point and the line is tangent to the circle. If the weak inequality does not hold, the line does not intersect the circle.

Another quick way to derive the intersection points is the ansatz $(x_{1/2},y_{1/2})=s(a,b)\pm t(b,-a)$ , solving first for s using the line equation, which simplifies to $s(a^{2}+b^{2})=c$ and then for t using the circle equation, which simplifies to $(s^{2}+t^{2})(a^{2}+b^{2})=r^{2}$ .

If the circle's midpoint is not the origin, see. The intersection of a line and a parabola or hyperbola may be treated analogously.

### Two circles

The determination of the intersection points of two circles

- $(x-x_{1})^{2}+(y-y_{1})^{2}=r_{1}^{2},\ \quad (x-x_{2})^{2}+(y-y_{2})^{2}=r_{2}^{2}$

can be reduced to the previous case of intersecting a line and a circle. By subtraction of the two given equations one gets the line equation:

$2(x_{2}-x_{1})x+2(y_{2}-y_{1})y=r_{1}^{2}-x_{1}^{2}-y_{1}^{2}-r_{2}^{2}+x_{2}^{2}+y_{2}^{2}.$

This special line is the radical line of the two circles.

**Special case $\;x_{1}=y_{1}=y_{2}=0$  :** In this case the origin is the center of the first circle and the second center lies on the x-axis (s. diagram). The equation of the radical line simplifies to $\;2x_{2}x=r_{1}^{2}-r_{2}^{2}+x_{2}^{2}\;$ and the points of intersection can be written as $(x_{0},\pm y_{0})$ with

$x_{0}={\frac {r_{1}^{2}-r_{2}^{2}+x_{2}^{2}}{2x_{2}}},\quad y_{0}={\sqrt {r_{1}^{2}-x_{0}^{2}}}\ .$

In case of $r_{1}^{2}<x_{0}^{2}$ the circles have no points in common. In case of $r_{1}^{2}=x_{0}^{2}$ the circles have one point in common and the radical line is a common tangent.

Any general case as written above can be transformed by a shift and a rotation into the special case.

The intersection of two disks (the interiors of the two circles) forms a shape called a lens.

### Two conic sections

The problem of intersection of an ellipse/hyperbola/parabola with another conic section leads to a system of quadratic equations, which can be solved in special cases easily by elimination of one coordinate. Special properties of conic sections may be used to obtain a solution. In general the intersection points can be determined by solving the equation by a Newton iteration. If a) both conics are given implicitly (by an equation) a 2-dimensional Newton iteration b) one implicitly and the other parametrically given a 1-dimensional Newton iteration is necessary. See next section.

### Two smooth curves

Two curves in $\mathbb {R} ^{2}$ (two-dimensional space), which are continuously differentiable (i.e. there is no sharp bend), have an intersection point, if they have a point of the plane in common and have at this point (see diagram):

a) different tangent lines (

transversal intersection

, after

transversality

), or

b) the tangent line in common and they are crossing each other (

touching intersection

, after

tangency

).

If both the curves have a point S and the tangent line there in common but do not cross each other, they are just *touching* at point S.

Because touching intersections appear rarely and are difficult to deal with, the following considerations omit this case. In any case below all necessary differential conditions are presupposed. The determination of intersection points always leads to one or two non-linear equations which can be solved by Newton iteration. A list of the appearing cases follows:

- If *both curves are explicitly* given: $y=f_{1}(x),\ y=f_{2}(x)$ , equating them yields the equation

$f_{1}(x)=f_{2}(x)\ .$

- If *both curves are parametrically* given: $C_{1}:(x_{1}(t),y_{1}(t)),\ C_{2}:(x_{2}(s),y_{2}(s)).$

Equating them yields two equations in two variables:

$x_{1}(t)=x_{2}(s),\ y_{1}(t)=y_{2}(s)\ .$

- If *one curve is parametrically and the other implicitly* given: $C_{1}:(x_{1}(t),y_{1}(t)),\ C_{2}:f(x,y)=0.$

This is the simplest case besides the explicit case. One has to insert the parametric representation of

$C_{1}$

into the equation

$f(x,y)=0$

of curve

$C_{2}$

and one gets the equation:

$f(x_{1}(t),y_{2}(t))=0\ .$

- If *both curves are implicitly* given: $C_{1}:f_{1}(x,y)=0,\ C_{2}:f_{2}(x,y)=0.$

Here, an intersection point is a solution of the system

$f_{1}(x,y)=0,\ f_{2}(x,y)=0\ .$

Any Newton iteration needs convenient starting values, which can be derived by a visualization of both the curves. A parametrically or explicitly given curve can easily be visualized, because to any parameter t or x respectively it is easy to calculate the corresponding point. For implicitly given curves this task is not as easy. In this case one has to determine a curve point with help of starting values and an iteration. See .

*Examples:*

1:

$C_{1}:(t,t^{3})$

and circle

$C_{2}:(x-1)^{2}+(y-1)^{2}-10=0$

(see diagram).

The Newton iteration

$t_{n+1}:=t_{n}-{\frac {f(t_{n})}{f'(t_{n})}}$

for function

$f(t)=(t-1)^{2}+(t^{3}-1)^{2}-10$

has to be done. As start values one can choose −1 and 1.5.

The intersection points are: (−1.1073, −1.3578), (1.6011, 4.1046)

2:

$C_{1}:f_{1}(x,y)=x^{4}+y^{4}-1=0,$

$C_{2}:f_{2}(x,y)=(x-0.5)^{2}+(y-0.5)^{2}-1=0$

(see diagram).

The Newton iteration

${x_{n+1} \choose y_{n+1}}={x_{n}+\delta _{x} \choose y_{n}+\delta _{y}}$

has to be performed, where

${\delta _{x} \choose \delta _{y}}$

is the solution of the linear system

${\begin{pmatrix}{\frac {\partial f_{1}}{\partial x}}&{\frac {\partial f_{1}}{\partial y}}\\{\frac {\partial f_{2}}{\partial x}}&{\frac {\partial f_{2}}{\partial y}}\end{pmatrix}}{\delta _{x} \choose \delta _{y}}={-f_{1} \choose -f_{2}}$

at point

$(x_{n},y_{n})$

. As starting values one can choose(−0.5, 1) and (1, −0.5).

The linear system can be solved by Cramer's rule.

The intersection points are (−0.3686, 0.9953) and (0.9953, −0.3686).

### Two polygons

If one wants to determine the intersection points of two polygons, one can check the intersection of any pair of line segments of the polygons (see above). For polygons with many segments this method is rather time-consuming. In practice one accelerates the intersection algorithm by using *window tests*. In this case one divides the polygons into small sub-polygons and determines the smallest window (rectangle with sides parallel to the coordinate axes) for any sub-polygon. Before starting the time-consuming determination of the intersection point of two line segments any pair of windows is tested for common points. See.

## In space (three dimensions)

In 3-dimensional space there are intersection points (common points) between curves and surfaces. In the following sections we consider *transversal intersection* only.

### A line and a plane

The intersection of a line and a plane *in general position* in three dimensions is a point.

Commonly a line in space is represented parametrically $(x(t),y(t),z(t))$ and a plane by an equation $ax+by+cz=d$ . Inserting the parameter representation into the equation yields the linear equation

$ax(t)+by(t)+cz(t)=d\ ,$

for parameter $t_{0}$ of the intersection point $(x(t_{0}),y(t_{0}),z(t_{0}))$ .

If the linear equation has no solution, the line either lies on the plane or is parallel to it.

### Three planes

If a line is defined by two intersecting planes $\varepsilon _{i}:\ {\vec {n}}_{i}\cdot {\vec {x}}=d_{i},\ i=1,2$ and should be intersected by a third plane $\varepsilon _{3}:\ {\vec {n}}_{3}\cdot {\vec {x}}=d_{3}$ , the common intersection point of the three planes has to be evaluated.

Three planes $\varepsilon _{i}:\ {\vec {n}}_{i}\cdot {\vec {x}}=d_{i},\ i=1,2,3$ with linear independent normal vectors ${\vec {n}}_{1},{\vec {n}}_{2},{\vec {n}}_{3}$ have the intersection point

${\vec {p}}_{0}={\frac {d_{1}({\vec {n}}_{2}\times {\vec {n}}_{3})+d_{2}({\vec {n}}_{3}\times {\vec {n}}_{1})+d_{3}({\vec {n}}_{1}\times {\vec {n}}_{2})}{{\vec {n}}_{1}\cdot ({\vec {n}}_{2}\times {\vec {n}}_{3})}}\ .$

For the proof one should establish ${\vec {n}}_{i}\cdot {\vec {p}}_{0}=d_{i},\ i=1,2,3,$ using the rules of a scalar triple product. If the scalar triple product equals to 0, then planes either do not have the triple intersection or it is a line (or a plane, if all three planes are the same).

### A curve and a surface

Analogously to the plane case the following cases lead to non-linear systems, which can be solved using a 1- or 3-dimensional Newton iteration.

- parametric curve $C:(x(t),y(t),z(t))$ and

parametric surface

$S:(x(u,v),y(u,v),z(u,v))\ ,$

- parametric curve $C:(x(t),y(t),z(t))$ and

implicit surface

$S:f(x,y,z)=0\ .$

**Example:**

parametric curve

$C:(t,t^{2},t^{3})$

and

implicit surface

$S:x^{4}+y^{4}+z^{4}-1=0$

(s. picture).

The intersection points are: (−0.8587, 0.7374, −0.6332), (0.8587, 0.7374, 0.6332).

A line–sphere intersection is a simple special case.

Like the case of a line and a plane, the intersection of a curve and a surface *in general position* consists of discrete points, but a curve may be partly or totally contained in a surface.

### A line and a polyhedron

### Two surfaces

Two transversally intersecting surfaces give an intersection curve. The most simple case is the intersection line of two non-parallel planes.

### A sphere and a plane

When the intersection of a sphere and a plane is not empty or a single point, it is a circle. This can be seen as follows:

Let *S* be a sphere with center *O*, *P* a plane which intersects *S*. Draw *OE* perpendicular to *P* and meeting *P* at *E*. Let *A* and *B* be any two different points in the intersection. Then *AOE* and *BOE* are right triangles with a common side, *OE*, and hypotenuses *AO* and *BO* equal. Therefore, the remaining sides *AE* and *BE* are equal. This proves that all points in the intersection are the same distance from the point *E* in the plane *P*, in other words all points in the intersection lie on a circle *C* with center *E*. This proves that the intersection of *P* and *S* is contained in *C*. Note that *OE* is the axis of the circle.

Now consider a point *D* of the circle *C*. Since *C* lies in *P*, so does *D*. On the other hand, the triangles *AOE* and *DOE* are right triangles with a common side, *OE*, and legs *EA* and *ED* equal. Therefore, the hypotenuses *AO* and *DO* are equal, and equal to the radius of *S*, so that *D* lies in *S*. This proves that *C* is contained in the intersection of *P* and *S*.

As a corollary, on a sphere there is exactly one circle that can be drawn through three given points.

The proof can be extended to show that the points on a circle are all a common angular distance from one of its poles.

Compare also conic sections, which can produce ovals.

### Two spheres

To show that a non-trivial intersection of two spheres is a circle, assume (without loss of generality) that one sphere (with radius R ) is centered at the origin. Points on this sphere satisfy

$x^{2}+y^{2}+z^{2}=R^{2}.$

Also without loss of generality, assume that the second sphere, with radius r , is centered at a point on the positive x-axis, at distance a from the origin. Its points satisfy

$(x-a)^{2}+y^{2}+z^{2}=r^{2}.$

The intersection of the spheres is the set of points satisfying both equations. Subtracting the equations gives

${\begin{aligned}(x-a)^{2}-x^{2}&=r^{2}-R^{2}\\a^{2}-2ax&=r^{2}-R^{2}\\x&={\frac {a^{2}+R^{2}-r^{2}}{2a}}.\end{aligned}}$

In the singular case $a=0$ , the spheres are concentric. There are two possibilities: if $R=r$ , the spheres coincide, and the intersection is the entire sphere; if $R\not =r$ , the spheres are disjoint and the intersection is empty. When *a* is nonzero, the intersection lies in a vertical plane with this x-coordinate, which may intersect both of the spheres, be tangent to both spheres, or external to both spheres. The result follows from the previous proof for sphere-plane intersections.

---
title: "Envelope (mathematics)"
source: https://en.wikipedia.org/wiki/Envelope_(mathematics)
domain: convex-hull-trick
license: CC-BY-SA-4.0
tags: convex hull trick, dynamic programming optimization, lower envelope of lines, monotone stack
fetched: 2026-07-02
---

# Envelope (mathematics)

In geometry, an **envelope** of a planar family of curves is a curve that is tangent to each member of the family at some point, and these points of tangency together form the whole envelope. Classically, a point on the envelope can be thought of as the intersection of two "infinitesimally adjacent" curves, meaning the limit of intersections of nearby curves. This idea can be generalized to an envelope of surfaces in space, and so on to higher dimensions.

To have an envelope, it is necessary that the individual members of the family of curves are differentiable curves as the concept of tangency does not apply otherwise, and there has to be a smooth transition proceeding through the members. But these conditions are not sufficient – a given family may fail to have an envelope. A simple example of this is given by a family of concentric circles of expanding radius.

## Envelope of a family of curves

Let each curve $C_{t}$ in the family be given as the solution of an equation $f_{t}(x,y)=0$ (see implicit curve), where t is a parameter. Write $F(t,x,y)=f_{t}(x,y)$ and assume F is differentiable.

The envelope of the family $C_{t}$ is then defined as the set ${\mathcal {D}}$ of points $(x,y)$ for which, simultaneously,

$F(t,x,y)=0~~{\mathsf {and}}~~{\partial F \over \partial t}(t,x,y)=0$

for some value of t , where $\partial F/\partial t$ is the partial derivative of F with respect to t .

If t and u , $t\neq u$ are two values of the parameter then the intersection of the curves $C_{t}$ and $C_{u}$ is given by

$F(t,x,y)=F(u,x,y)=0\,$

or, equivalently,

$F(t,x,y)=0~~{\mathsf {and}}~~{\frac {F(u,x,y)-F(t,x,y)}{u-t}}=0.$

Letting $u\to t$ gives the definition above.

An important special case is when $F(t,x,y)$ is a polynomial in t . This includes, by clearing denominators, the case where $F(t,x,y)$ is a rational function in t . In this case, the definition amounts to t being a double root of $F(t,x,y)$ , so the equation of the envelope can be found by setting the discriminant of F to 0 (because the definition demands $F=0$ at some t and first derivative $F=0$ i.e. its value 0 and it is min/max at that t ).

For example, let $C_{t}$ be the line whose x and y intercepts are t and $11-t$ , this is shown in the animation above. The equation of $C_{t}$ is

${\frac {x}{t}}+{\frac {y}{11-t}}=1$

or, clearing fractions,

$x(11-t)+yt-t(11-t)=t^{2}+(-x+y-11)t+11x=0.\,$

The equation of the envelope is then

$(-x+y-11)^{2}-44x=(x-y)^{2}-22(x+y)+121=0.\,$

Often when F is not a rational function of the parameter it may be reduced to this case by an appropriate substitution. For example, if the family is given by $C_{\theta }$ with an equation of the form $u(x,y)\cos \theta +v(x,y)\sin \theta =w(x,y)$ , then putting $t=e^{i\theta }$ , $\cos \theta =(t+1/t)/2$ , $\sin \theta =(t-1/t)/2i$ changes the equation of the curve to

$u{1 \over 2}\left(t+{1 \over t}\right)+v{1 \over 2i}\left(t-{1 \over t}\right)=w$

or

$(u-iv)t^{2}-2wt+(u+iv)=0.\,$

The equation of the envelope is then given by setting the discriminant to 0 :

$(u-iv)(u+iv)-w^{2}=0\,$

or

$u^{2}+v^{2}=w^{2}.\,$

### Alternative definitions

1. The envelope $E_{1}$ is the limit of intersections of nearby curves $C_{t}$ .
2. The envelope $E_{2}$ is a curve tangent to all of the $C_{t}$ .
3. The envelope $E_{3}$ is the boundary of the region filled by the curves $C_{t}$ .

Then $E_{1}\subseteq {\mathcal {D}}$ , $E_{2}\subseteq {\mathcal {D}}$ and $E_{3}\subseteq {\mathcal {D}}$ , where ${\mathcal {D}}$ is the set of points defined at the beginning of this subsection's parent section.

## Examples

### Example 1

These definitions $E_{1}$ , $E_{2}$ , and $E_{3}$ of the envelope may be different sets. Consider for instance the curve $y=x^{3}$ parametrised by ${\displaystyle \gamma$ where $\gamma (t)=(t,t^{3})$ . The one-parameter family of curves will be given by the tangent lines to $\gamma$ .

First we calculate the discriminant ${\mathcal {D}}$ . The generating function is

$F(t,(x,y))=3t^{2}x-y-2t^{3}.$

Calculating the partial derivative $F_{t}=6t(x-t)$ . It follows that either $x=t$ or $t=0$ . First assume that $x=t$ and $t\neq 0$ . Substituting into F : $F(t,(t,y))=t^{3}-y\,$ and so, assuming that $t\neq 0$ , it follows that $F=F_{t}=0$ if and only if $(x,y)=(t,t^{3})$ . Next, assuming that $t=0$ and substituting into F gives $F(0,(x,y))=-y$ . So, assuming $t=0$ , it follows that $F=F_{t}=0$ if and only if $y=0$ . Thus the discriminant is the original curve and its tangent line at $\gamma (0)$ :

${\mathcal {D}}=\{(x,y)\in \mathbb {R} ^{2}:y=x^{3}\}\cup \{(x,y)\in \mathbb {R} ^{2}:y=0\}\ .$

Next we calculate $E_{1}$ . One curve is given by $F(t,(x,y))=0$ and a nearby curve is given by $F(t+\varepsilon ,(x,y))=0$ where $\varepsilon$ is some very small number. The intersection point comes from looking at the limit of $F(t,(x,y))=F(t+\varepsilon ,(x,y))$ as $\varepsilon$ tends to zero. Notice that $F(t,(x,y))=F(t+\varepsilon ,(x,y))$ if and only if

$L:=F(t,(x,y))-F(t+\varepsilon ,(x,y))=2\varepsilon ^{3}+6\varepsilon t^{2}+6\varepsilon ^{2}t-(3\varepsilon ^{2}+6\varepsilon t)x=0.$

If $t\neq 0$ then L has only a single factor of $\varepsilon$ . Assuming that $t\neq 0$ then the intersection is given by

$\lim _{\varepsilon \to 0}{\frac {1}{\varepsilon }}L=6t(t-x)\ .$

Since $t\neq 0$ it follows that $x=t$ . The y value is calculated by knowing that this point must lie on a tangent line to the original curve $\gamma$ : that $F(t,(x,y))=0$ . Substituting and solving gives $y=t^{3}$ . When $t=0$ , L is divisible by $\varepsilon ^{2}$ . Assuming that $t=0$ then the intersection is given by

$\lim _{\varepsilon \to 0}{\frac {1}{\varepsilon ^{2}}}L=3x\ .$

It follows that $x=0$ , and knowing that $F(t,(x,y))=0$ gives $y=0$ . It follows that

$E_{1}=\{(x,y)\in \mathbb {R} ^{2}:y=x^{3}\}\ .$

Next we calculate $E_{2}$ . The curve itself is the curve that is tangent to all of its own tangent lines. It follows that

$E_{2}=\{(x,y)\in \mathbb {R} ^{2}:y=x^{3}\}\ .$

Finally we calculate $E_{3}$ . Every point in the plane has at least one tangent line to $\gamma$ passing through it, and so region filled by the tangent lines is the whole plane. The boundary $E_{3}$ is therefore the empty set. Indeed, consider a point in the plane, say $(x_{0},y_{0})$ . This point lies on a tangent line if and only if there exists a t such that

$F(t,(x_{0},y_{0}))=3t^{2}x_{0}-y_{0}-2t^{3}=0\ .$

This is a cubic in t and as such has at least one real solution. It follows that at least one tangent line to $\gamma$ must pass through any given point in the plane. If $y>x^{3}$ and $y>0$ then each point $(x,y)$ has exactly one tangent line to $\gamma$ passing through it. The same is true if $y<x^{3}$ and $y<0$ . If $y<x^{3}$ and $y>0$ then each point $(x,y)$ has exactly three distinct tangent lines to $\gamma$ passing through it. The same is true if $y>x^{3}$ and $y<0$ . If $y=x^{3}$ and $y\neq 0$ then each point $(x,y)$ has exactly two tangent lines to $\gamma$ passing through it (this corresponds to the cubic having one ordinary root and one repeated root). The same is true if $y\neq x^{3}$ and $y=0$ . If $y=x^{3}$ and $x=0$ , i.e., $x=y=0$ , then this point has a single tangent line to $\gamma$ passing through it (this corresponds to the cubic having one real root of multiplicity 3). It follows that

$E_{3}=\varnothing .$

### Example 2

In string art it is common to cross-connect two lines of equally spaced pins. What curve is formed?

For simplicity, set the pins on the x - and y -axes; a non-orthogonal layout is a rotation and scaling away. A general straight-line thread connects the two points $(0,k-t)$ and $(t,0)$ , where k is an arbitrary scaling constant, and the family of lines is generated by varying the parameter t . From simple geometry, the equation of this straight line is $y=-(k-t)x/t+k-t$ . Rearranging and casting in the form $F(x,y,t)=0$ gives:

| $F(x,y,t)=-{\frac {kx}{t}}-t+x+k-y=0\,$ |   | 1 |
|---|---|---|

Now differentiate $F(x,y,t)$ with respect to t and set the result equal to zero, to get

| ${\frac {\partial F(x,y,t)}{\partial t}}={\frac {kx}{t^{2}}}-1=0\,$ |   | 2 |
|---|---|---|

These two equations jointly define the equation of the envelope. From (2) we have:

$t={\sqrt {kx}}\,$

Substituting this value of t into (1) and simplifying gives an equation for the envelope:

| $y=({\sqrt {x}}-{\sqrt {k}})^{2}\,$ |   | 3 |
|---|---|---|

Or, rearranging into a more elegant form that shows the symmetry between x and y :

| ${\sqrt {x}}+{\sqrt {y}}={\sqrt {k}}$ |   | 4 |
|---|---|---|

We can take a rotation of the axes where the b axis is the line $y=x$ oriented northeast and the a axis is the line $y=-x$ oriented southeast. These new axes are related to the original $x-y$ axes by $x=(b+a)/{\sqrt {2}}$ and $y=(b-a)/{\sqrt {2}}$ . We obtain, after substitution into (4) and expansion and simplification,

| $b={\frac {1}{k{\sqrt {2}}}}a^{2}+{\frac {k}{2{\sqrt {2}}}},$ |   | 5 |
|---|---|---|

which is apparently the equation for a parabola with axis along $a=0$ , or $y=x$ .

### Example 3

Let $I\subset \mathbb {R}$ be an open interval and let $\gamma :I\to \mathbb {R} ^{2}$ be a smooth plane curve parametrised by arc length. Consider the one-parameter family of normal lines to $\gamma (I)$ . A line is normal to $\gamma$ at $\gamma (t)$ if it passes through $\gamma (t)$ and is perpendicular to the tangent vector to $\gamma$ at $\gamma (t)$ . Let $\mathbf {T}$ denote the unit tangent vector to $\gamma$ and let $\mathbf {N}$ denote the unit normal vector. Using a dot to denote the dot product, the generating family for the one-parameter family of normal lines is given by $F:I\times \mathbb {R} ^{2}\to \mathbb {R}$ where

$F(t,{\mathbf {x} })=({\mathbf {x} }-\gamma (t))\cdot {\mathbf {T} }(t)\ .$

Clearly $(x-y)\cdot \mathbf {T} =0$ if and only if $x-\gamma$ is perpendicular to $\mathbf {T}$ , or equivalently, if and only if $x-\gamma$ is parallel to $\mathbf {N}$ , or equivalently, if and only if $x=\gamma +\lambda \mathbf {N}$ for some λ ∈ **R**. It follows that

$L_{t_{0}}:=\{{\mathbf {x} }\in \mathbb {R} ^{2}:F(t_{0},{\mathbf {x} })=0\}$

is exactly the normal line to $\gamma$ at $\gamma (t_{0})$ . To find the discriminant of F we need to compute its partial derivative with respect to t :

${\frac {\partial F}{\partial t}}(t,{\mathbf {x} })=\kappa (t)({\mathbf {x} }-\gamma (t))\cdot {\mathbf {N} }(t)-1\ ,$

where $\kappa$ is the plane curve curvature of $\gamma$ . It has been seen that $F=0$ if and only if $x-\gamma =\lambda \mathbf {N}$ for some $\lambda \in \mathbb {R}$ . Assuming that $F=0$ gives

${\frac {\partial F}{\partial t}}=\lambda \kappa (t)-1\ .$

Assuming that $\kappa \neq 0$ it follows that $\lambda =1/\kappa$ and so

${\mathcal {D}}=\gamma (t)+{\frac {1}{\kappa (t)}}{\mathbf {N} }(t)\ .$

This is exactly the evolute of the curve $\gamma$ .

### Example 4

The following example shows that in some cases the envelope of a family of curves may be seen as the topologic boundary of a union of sets, whose boundaries are the curves of the envelope. For $s>0$ and $t>0$ consider the (open) right triangle in a Cartesian plane with vertices $(0,0)$ , $(s,0)$ and $(0,t)$

$T_{s,t}:=\left\{(x,y)\in \mathbb {R} _{+}^{2}:\ {\frac {x}{s}}+{\frac {y}{t}}<1\right\}.$

Fix an exponent $\alpha >0$ , and consider the union of all the triangles $T_{s,t}$ subjected to the constraint $\textstyle s^{\alpha }+t^{\alpha }=1$ , that is the open set

$\Delta _{\alpha }:=\bigcup _{s^{\alpha }+t^{\alpha }=1}T_{s,t}.$

To write a Cartesian representation for $\textstyle \Delta _{\alpha }$ , start with any $\textstyle s>0$ , $\textstyle t>0$ satisfying $\textstyle s^{\alpha }+t^{\alpha }=1$ and any $\textstyle (x,y)\in \mathbb {R} _{+}^{2}$ . The Hölder inequality in $\textstyle \mathbb {R} ^{2}$ with respect to the conjugated exponents $p:=1+{\frac {1}{\alpha }}$ and $\textstyle q:={1+\alpha }$ gives:

$x^{\frac {\alpha }{\alpha +1}}+y^{\frac {\alpha }{\alpha +1}}\leq \left({\frac {x}{s}}+{\frac {y}{t}}\right)^{\frac {\alpha }{\alpha +1}}{\Big (}s^{\alpha }+t^{\alpha }{\Big )}^{\frac {1}{\alpha +1}}=\left({\frac {x}{s}}+{\frac {y}{t}}\right)^{\frac {\alpha }{\alpha +1}}$

,

with equality if and only if $\textstyle s:\,t=x^{\frac {1}{1+\alpha }}:\,y^{\frac {1}{1+\alpha }}$ . In terms of a union of sets the latter inequality reads: the point $(x,y)\in \mathbb {R} _{+}^{2}$ belongs to the set $\textstyle \Delta _{\alpha }$ , that is, it belongs to some $\textstyle T_{s,t}$ with $\textstyle s^{\alpha }+t^{\alpha }=1$ , if and only if it satisfies

$x^{\frac {\alpha }{\alpha +1}}+y^{\frac {\alpha }{\alpha +1}}<1.$

Moreover, the boundary in $\mathbb {R} _{+}^{2}$ of the set $\textstyle \Delta _{\alpha }$ is the envelope of the corresponding family of line segments

$\left\{(x,y)\in \mathbb {R} _{+}^{2}:\ {\frac {x}{s}}+{\frac {y}{t}}=1\right\}\ ,\qquad s^{\alpha }+t^{\alpha }=1$

(that is, the hypotenuses of the triangles), and has Cartesian equation

$x^{\frac {\alpha }{\alpha +1}}+y^{\frac {\alpha }{\alpha +1}}=1.$

Notice that, in particular, the value $\alpha =1$ gives the arc of parabola of the Example 2, and the value $\alpha =2$ (meaning that all hypotenuses are unit length segments) gives the astroid.

### Example 5

We consider the following example of envelope in motion. Suppose at initial height 0 , one casts a projectile into the air with constant initial velocity v but different elevation angles $\theta$ . Let x be the horizontal axis in the motion surface, and let y denote the vertical axis. Then the motion gives the following differential dynamical system:

${\frac {d^{2}y}{dt^{2}}}=-g,\;{\frac {d^{2}x}{dt^{2}}}=0,$

which satisfies four initial conditions:

${\frac {dx}{dt}}{\bigg |}_{t=0}=v\cos \theta ,\;{\frac {dy}{dt}}{\bigg |}_{t=0}=v\sin \theta ,\;x{\bigg |}_{t=0}=y{\bigg |}_{t=0}=0.$

Here t denotes motion time, $\theta$ is elevation angle, g denotes gravitational acceleration, and v is the constant initial speed (not velocity). The solution of the above system can take an implicit form:

$F(x,y,\theta )=x\tan \theta -{\frac {gx^{2}}{2v^{2}\cos ^{2}\theta }}-y=0.$

To find its envelope equation, one may compute the desired derivative:

${\frac {\partial F}{\partial \theta }}={\frac {x}{\cos ^{2}\theta }}-{\frac {gx^{2}\tan \theta }{v^{2}\cos ^{2}\theta }}=0.$

By eliminating $\theta$ , one may reach the following envelope equation:

$y={\frac {v^{2}}{2g}}-{\frac {g}{2v^{2}}}x^{2}.$

Clearly the resulted envelope is also a concave parabola.

## Envelope of a family of surfaces

A **one-parameter family of surfaces** in three-dimensional Euclidean space is given by a set of equations

$F(x,y,z,a)=0$

depending on a real parameter a . For example, the tangent planes to a surface along a curve in the surface form such a family.

Two surfaces corresponding to different values a and $a'$ intersect in a common curve defined by

$F(x,y,z,a)=0,\,\,{F(x,y,z,a^{\prime })-F(x,y,z,a) \over a^{\prime }-a}=0.$

In the limit as $a'$ approaches a , this curve tends to a curve contained in the surface at a

$F(x,y,z,a)=0,\,\,{\partial F \over \partial a}(x,y,z,a)=0.$

This curve is called the **characteristic** of the family at a . As a varies the locus of these characteristic curves defines a surface called the **envelope** of the family of surfaces.

> The envelope of a family of surfaces is tangent to each surface in the family along the characteristic curve in that surface.

## Generalisations

The idea of an envelope of a family of smooth submanifolds follows naturally. In general, if we have a family of submanifolds with codimension c then we need to have at least a c -parameter family of such submanifolds. For example: a one-parameter family of curves in three-space ( $c=2$ ) does not, generically, have an envelope.

## Applications

### Ordinary differential equations

Envelopes are connected to the study of ordinary differential equations (ODEs), and in particular singular solutions of ODEs. Consider, for example, the one-parameter family of tangent lines to the parabola $y=x^{2}$ . These are given by the generating family $F(t,(x,y))=t^{2}-2tx+y$ . The zero level set $F(t_{0},(x,y))=0$ gives the equation of the tangent line to the parabola at the point $(t_{0},t_{0}^{2})$ . The equation $t^{2}-2tx+y=0$ can always be solved for y as a function of x and so, consider

$t^{2}-2tx+y(x)=0.\$

Substituting

$t=\left({\frac {dy}{dx}}\right)/2$

gives the ODE

$\left({\frac {dy}{dx}}\right)^{2}\!\!-4x{\frac {dy}{dx}}+4y=0.$

Not surprisingly $y=2tx-t^{2}$ are all solutions to this ODE. However, the envelope of this one-parameter family of lines, which is the parabola $y=x^{2}$ , is also a solution to this ODE. Another famous example is Clairaut's equation.

### Partial differential equations

Envelopes can be used to construct more complicated solutions of first order partial differential equations (PDEs) from simpler ones. Let $F(x,u,\nabla u)=0$ be a first order PDE, where x is a variable with values in an open set $\Omega \subset \mathbb {R} ^{n}$ , u is an unknown real-valued function, $\nabla u$ is the gradient of u , and F is a continuously differentiable function that is regular in $\nabla u$ . Suppose that $u(x;a)$ is an m -parameter family of solutions: that is, for each fixed $a\in A\subset \mathbb {R} ^{m}$ , $u(x;a)$ is a solution of the differential equation. A new solution of the differential equation can be constructed by first solving (if possible)

$D_{a}u(x;a)=0\,$

for $a=\varphi (x)$ as a function of x . The envelope of the family of functions $\{u(\cdot ,a)\}_{a\in A}$ is defined by

$v(x)=u(x;\varphi (x)),\quad x\in \Omega ,$

and also solves the differential equation (provided that it exists as a continuously differentiable function).

Geometrically, the graph of $v(x)$ is everywhere tangent to the graph of some member of the family $u(x;a)$ . Since the differential equation is first order, it only puts a condition on the tangent plane to the graph, so that any function everywhere tangent to a solution must also be a solution. The same idea underlies the solution of a first order equation as an integral of the Monge cone. The Monge cone is a cone field in the $\mathbb {R} ^{n+1}$ of the $(x,u)$ variables cut out by the envelope of the tangent spaces to the first order PDE at each point. A solution of the PDE is then an envelope of the cone field.

In Riemannian geometry, if a smooth family of geodesics through a point P in a Riemannian manifold has an envelope, then P has a conjugate point where any geodesic of the family intersects the envelope. The same is true more generally in the calculus of variations: if a family of extremals to a functional through a given point P has an envelope, then a point where an extremal intersects the envelope is a conjugate point to P .

### Caustics

In geometrical optics, a caustic is the envelope of a family of light rays. In this picture there is an arc of a circle. The light rays (shown in blue) are coming from a source *at infinity*, and so arrive parallel. When they hit the circular arc the light rays are scattered in different directions according to the law of reflection. When a light ray hits the arc at a point the light will be reflected as though it had been reflected by the arc's tangent line at that point. The reflected light rays give a one-parameter family of lines in the plane. The envelope of these lines is the reflective caustic. A reflective caustic will generically consist of smooth points and ordinary cusp points.

From the point of view of the calculus of variations, Fermat's principle (in its modern form) implies that light rays are the extremals for the length functional

$L[\gamma ]=\int _{a}^{b}|\gamma '(t)|\,dt$

among smooth curves $\gamma$ on $[a,b]$ with fixed endpoints $\gamma (a)$ and $\gamma (b)$ . The caustic determined by a given point P (in the image the point is at infinity) is the set of conjugate points to P .

### Huygens's principle

Light may pass through anisotropic inhomogeneous media at different rates depending on the direction and starting position of a light ray. The boundary of the set of points to which light can travel from a given point q after a time t is known as the wave front after time t , denoted here by $\Phi _{q}(t)$ . It consists of precisely the points that can be reached from q in time t by travelling at the speed of light. Huygens's principle asserts that the wave front set $\Phi _{q_{0}}\!(s+t)$ is the envelope of the family of wave fronts $\Phi _{q}(s)$ for $q\in \Phi _{q_{0}}(t)$ . More generally, the point $q_{0}$ could be replaced by any curve, surface or closed set in space.

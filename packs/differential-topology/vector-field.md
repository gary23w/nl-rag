---
title: "Vector field"
source: https://en.wikipedia.org/wiki/Vector_field
domain: differential-topology
license: CC-BY-SA-4.0
tags: differential topology, smooth manifold, morse theory, de rham cohomology
fetched: 2026-07-02
---

# Vector field

In vector calculus and physics, a **vector field** is an assignment of a vector to each point in a space, most commonly Euclidean space $\mathbb {R} ^{n}$ . A vector field on a plane can be visualized as a collection of arrows with given magnitudes and directions, each attached to a point on the plane. Vector fields often have unit of measurement (for example, metres or kilometres per hour), forming a vector physical quantity. They may be used to model, for example, the speed and direction of a moving fluid throughout three dimensional space, such as the wind, or the strength and direction of some force, such as the magnetic or gravitational force, as it changes from one point to another point.

The elements of differential and integral calculus extend naturally to vector fields. When a vector field represents force, the line integral of a vector field represents the work done by a force moving along a path, and under this interpretation conservation of energy is exhibited as a special case of the fundamental theorem of calculus. Vector fields can usefully be thought of as representing the velocity of a moving flow in space, and this physical intuition leads to notions such as the divergence (which represents the rate of change of volume of a flow) and curl (which represents the rotation of a flow).

A vector field is a special case of a *vector-valued function*, whose domain's dimension has no relation to the dimension of its range; for example, the position vector of a space curve is defined only for smaller subset of the ambient space. Likewise, n coordinates, a vector field on a domain in *n*-dimensional Euclidean space $\mathbb {R} ^{n}$ can be represented as a vector-valued function that associates an *n*-tuple of real numbers to each point of the domain. This representation of a vector field depends on the coordinate system, and there is a well-defined transformation law (*covariance and contravariance of vectors*) in passing from one coordinate system to the other.

Vector fields are often discussed on open subsets of Euclidean space, but also make sense on other subsets such as surfaces, where they associate an arrow tangent to the surface at each point (a tangent vector). More generally, vector fields are defined on differentiable manifolds, which are spaces that look like Euclidean space on small scales, but may have more complicated structure on larger scales. In this setting, a vector field gives a tangent vector at each point of the manifold (that is, a section of the tangent bundle to the manifold). Vector fields are one kind of tensor field.

## Definition

### Vector fields on subsets of Euclidean space

Two representations of the same vector field:

v

(

x

,

y

) = −

r

. The arrows depict the field at discrete points, however, the field exists everywhere.

Given a subset *S* of **R***n*, a **vector field** is represented by a vector-valued function *V*: *S* → **R***n* in standard Cartesian coordinates (*x*1, …, *x**n*). If each component of *V* is continuous, then *V* is a continuous vector field. It is common to focus on **smooth** vector fields, meaning that each component is a smooth function (differentiable any number of times). A vector field can be visualized as assigning a vector to individual points within an *n*-dimensional space.

One standard notation is to write ${\frac {\partial }{\partial x_{1}}},\ldots ,{\frac {\partial }{\partial x_{n}}}$ for the unit vectors in the coordinate directions. In these terms, every smooth vector field V on an open subset S of ${\mathbf {R} }^{n}$ can be written as $\sum _{i=1}^{n}V_{i}(x_{1},\ldots ,x_{n}){\frac {\partial }{\partial x_{i}}}$ for some smooth functions $V_{1},\ldots ,V_{n}$ on S . The reason for this notation is that a vector field determines a linear map from the space of smooth functions to itself, $V\colon C^{\infty }(S)\to C^{\infty }(S)$ , given by differentiating in the direction of the vector field.

**Example**: The vector field $-x_{2}{\frac {\partial }{\partial x_{1}}}+x_{1}{\frac {\partial }{\partial x_{2}}}$ describes a counterclockwise rotation around the origin in $\mathbf {R} ^{2}$ . To show that the function $x_{1}^{2}+x_{2}^{2}$ is rotationally invariant, compute: $\left(-x_{2}{\frac {\partial }{\partial x_{1}}}+x_{1}{\frac {\partial }{\partial x_{2}}}\right)\left(x_{1}^{2}+x_{2}^{2}\right)=-x_{2}(2x_{1})+x_{1}(2x_{2})=0.$

Given vector fields *V*, *W* defined on *S* and a smooth function f defined on *S*, the operations of scalar multiplication and vector addition, ${\begin{aligned}(fV)(p)&:=f(p)V(p)\\(V+W)(p)&:=V(p)+W(p),\end{aligned}}$ make the smooth vector fields into a module over the ring of smooth functions, where multiplication of functions is defined pointwise.

### Coordinate transformation law

In physics, a vector is additionally distinguished by how its coordinates change when one measures the same vector with respect to a different background coordinate system. The transformation properties of vectors distinguish a vector as a geometrically distinct entity from a simple list of scalars, or from a covector.

Thus, suppose that (*x*1, ..., *x**n*) is a choice of Cartesian coordinates, in terms of which the components of the vector V are $V_{x}=(V_{1,x},\dots ,V_{n,x})$ and suppose that (*y*1,...,*y**n*) are *n* functions of the *x**i* defining a different coordinate system. Then the components of the vector *V* in the new coordinates are required to satisfy the transformation law

| $V_{i,y}=\sum _{j=1}^{n}{\frac {\partial y_{i}}{\partial x_{j}}}V_{j,x}.$ |   | 1 |
|---|---|---|

Such a transformation law is called contravariant. A similar transformation law characterizes vector fields in physics: specifically, a vector field is a specification of *n* functions in each coordinate system subject to the transformation law (**1**) relating the different coordinate systems.

Vector fields are thus contrasted with scalar fields, which associate a number or *scalar* to every point in space, and are also contrasted with simple lists of scalar fields, which do not transform under coordinate changes.

### Vector fields on manifolds

Given a differentiable manifold M , a **vector field** on M is an assignment of a tangent vector to each point in M . More precisely, a vector field F is a mapping from M into the tangent bundle $TM$ so that $p\circ F$ is the identity mapping where p denotes the projection from $TM$ to M . In other words, a vector field is a section of the tangent bundle.

An alternative definition: A smooth vector field X on a manifold M is a linear map $X:C^{\infty }(M)\to C^{\infty }(M)$ such that X is a derivation: $X(fg)=fX(g)+X(f)g$ for all $f,g\in C^{\infty }(M)$ .

If the manifold M is smooth or analytic—that is, the change of coordinates is smooth (analytic)—then one can make sense of the notion of smooth (analytic) vector fields. The collection of all smooth vector fields on a smooth manifold M is often denoted by $\Gamma (TM)$ or $C^{\infty }(M,TM)$ (especially when thinking of vector fields as sections); the collection of all smooth vector fields is also denoted by ${\textstyle {\mathfrak {X}}(M)}$ (a fraktur "X").

## Examples

- A vector field for the movement of air on Earth will associate for every point on the surface of the Earth a vector with the wind speed and direction for that point. This can be drawn using arrows to represent the wind; the length (magnitude) of the arrow will be an indication of the wind speed. A "high" on the usual barometric pressure map would then act as a source (arrows pointing away), and a "low" would be a sink (arrows pointing towards), since air tends to move from high pressure areas to low pressure areas.
- Velocity field of a moving fluid. In this case, a velocity vector is associated to each point in the fluid.
- Streamlines, streaklines and pathlines are 3 types of lines that can be made from (time-dependent) vector fields. They are:
  - streaklines: the line produced by particles passing through a specific fixed point over various times
  - pathlines: showing the path that a given particle (of zero mass) would follow.
  - streamlines (or fieldlines): the path of a particle influenced by the instantaneous field (i.e., the path of a particle if the field is held fixed).
- Magnetic fields. The fieldlines can be revealed using small iron filings.
- Maxwell's equations allow us to use a given set of initial and boundary conditions to deduce, for every point in Euclidean space, a magnitude and direction for the force experienced by a charged test particle at that point; the resulting vector field is the electric field.
- A gravitational field generated by any massive object is also a vector field. For example, the gravitational field vectors for a spherically symmetric body would all point towards the sphere's center with the magnitude of the vectors reducing as radial distance from the body increases.

### Gradient field in Euclidean spaces

Vector fields can be constructed out of scalar fields using the gradient operator (denoted by the del: ∇).

A vector field *V* defined on an open set *S* is called a **gradient field** or a **conservative field** if there exists a real-valued function (a scalar field) *f* on *S* such that $V=\nabla f=\left({\frac {\partial f}{\partial x_{1}}},{\frac {\partial f}{\partial x_{2}}},{\frac {\partial f}{\partial x_{3}}},\dots ,{\frac {\partial f}{\partial x_{n}}}\right).$

The associated flow is called the **gradient flow**, and is used in the method of gradient descent.

The path integral along any closed curve *γ* (*γ*(0) = *γ*(1)) in a conservative field is zero: $\oint _{\gamma }V(\mathbf {x} )\cdot \mathrm {d} \mathbf {x} =\oint _{\gamma }\nabla f(\mathbf {x} )\cdot \mathrm {d} \mathbf {x} =f(\gamma (1))-f(\gamma (0)).$

### Central field in euclidean spaces

A *C*∞-vector field over **R***n* \ {0} is called a **central field** if $V(T(p))=T(V(p))\qquad (T\in \mathrm {O} (n,\mathbb {R} ))$ where O(*n*, **R**) is the orthogonal group. We say central fields are invariant under orthogonal transformations around 0.

The point 0 is called the **center** of the field.

Since orthogonal transformations are actually rotations and reflections, the invariance conditions mean that vectors of a central field are always directed towards, or away from, 0; this is an alternate (and simpler) definition. A central field is always a gradient field, since defining it on one semiaxis and integrating gives an antigradient.

## Operations on vector fields

### Line integral

A common technique in physics is to integrate a vector field along a curve, also called determining its line integral. Intuitively this is summing up all vector components in line with the tangents to the curve, expressed as their scalar products. For example, given a particle in a force field (e.g. gravitation), where each vector at some point in space represents the force acting there on the particle, the line integral along a certain path is the work done on the particle, when it travels along this path. Intuitively, it is the sum of the scalar products of the force vector and the small tangent vector in each point along the curve.

The line integral is constructed analogously to the Riemann integral and it exists if the curve is rectifiable (has finite length) and the vector field is continuous.

Given a vector field V and a curve γ, parametrized by t in [*a*, *b*] (where a and b are real numbers), the line integral is defined as $\int _{\gamma }V(\mathbf {x} )\cdot \mathrm {d} \mathbf {x} =\int _{a}^{b}V(\gamma (t))\cdot {\dot {\gamma }}(t)\,\mathrm {d} t.$

To show vector field topology one can use line integral convolution.

### Divergence

The divergence of a vector field on Euclidean space is a function (or scalar field). In three-dimensions, the divergence is defined by $\operatorname {div} \mathbf {F} =\nabla \cdot \mathbf {F} ={\frac {\partial F_{1}}{\partial x}}+{\frac {\partial F_{2}}{\partial y}}+{\frac {\partial F_{3}}{\partial z}},$

with the obvious generalization to arbitrary dimensions. The divergence at a point represents the degree to which a small volume around the point is a source or a sink for the vector flow, a result which is made precise by the divergence theorem.

The divergence can also be defined on a Riemannian manifold, that is, a manifold with a Riemannian metric that measures the length of vectors.

### Curl in three dimensions

The curl is an operation which takes a vector field and produces another vector field. The curl is defined only in three dimensions, but some properties of the curl can be captured in higher dimensions with the exterior derivative. In three dimensions, it is defined by $\operatorname {curl} \mathbf {F} =\nabla \times \mathbf {F} =\left({\frac {\partial F_{3}}{\partial y}}-{\frac {\partial F_{2}}{\partial z}}\right)\mathbf {e} _{1}-\left({\frac {\partial F_{3}}{\partial x}}-{\frac {\partial F_{1}}{\partial z}}\right)\mathbf {e} _{2}+\left({\frac {\partial F_{2}}{\partial x}}-{\frac {\partial F_{1}}{\partial y}}\right)\mathbf {e} _{3}.$

The curl measures the density of the angular momentum of the vector flow at a point, that is, the amount to which the flow circulates around a fixed axis. This intuitive description is made precise by Stokes' theorem.

### Index of a vector field

The index of a vector field is an integer that helps describe its behaviour around an isolated zero (i.e., an isolated singularity of the field). In the plane, the index takes the value −1 at a saddle singularity but +1 at a source or sink singularity.

Let *n be* the dimension of the manifold on which the vector field is defined. Take a closed surface (homeomorphic to the (n-1)-sphere) S around the zero, so that no other zeros lie in the interior of S. A map from this sphere to a unit sphere of dimension *n* − 1 can be constructed by dividing each vector on this sphere by its length to form a unit length vector, which is a point on the unit sphere S*n*−1. This defines a continuous map from S to S*n*−1. The index of the vector field at the point is the degree of this map. It can be shown that this integer does not depend on the choice of S, and therefore depends only on the vector field itself.

The index is not defined at any non-singular point (i.e., a point where the vector is non-zero). It is equal to +1 around a source, and more generally equal to (−1)*k* around a saddle that has *k* contracting dimensions and *n*−*k* expanding dimensions.

**The index of the vector field** as a whole is defined when it has just finitely many zeroes. In this case, all zeroes are isolated, and the index of the vector field is defined to be the sum of the indices at all zeroes.

For an ordinary (2-dimensional) sphere in three-dimensional space, it can be shown that the index of any vector field on the sphere must be 2. This shows that every such vector field must have a zero. This implies the hairy ball theorem.

For a vector field on a compact manifold with finitely many zeroes, the Poincaré-Hopf theorem states that the vector field's index is the manifold's Euler characteristic.

## Physical intuition

Michael Faraday, in his concept of *lines of force,* emphasized that the field *itself* should be an object of study, which it has become throughout physics in the form of field theory.

In addition to the magnetic field, other phenomena that were modeled by Faraday include the electrical field and light field.

In recent decades, many phenomenological formulations of irreversible dynamics and evolution equations in physics, from the mechanics of complex fluids and solids to chemical kinetics and quantum thermodynamics, have converged towards the geometric idea of "steepest entropy ascent" or "gradient flow" as a consistent universal modeling framework that guarantees compatibility with the second law of thermodynamics and extends well-known near-equilibrium results such as Onsager reciprocity to the far-nonequilibrium realm.

## Flow curves

Consider the flow of a fluid through a region of space. At any given time, any point of the fluid has a particular velocity associated with it; thus there is a vector field associated to any flow. The converse is also true: it is possible to associate a flow to a vector field having that vector field as its velocity.

Given a vector field V defined on S , one defines curves $\gamma (t)$ on S such that for each t in an interval I , $\gamma '(t)=V(\gamma (t))\,.$

By the Picard–Lindelöf theorem, if V is Lipschitz continuous there is a *unique* $C^{1}$ -curve $\gamma _{x}$ for each point x in S so that, for some $\varepsilon >0$ , ${\begin{aligned}\gamma _{x}(0)&=x\\\gamma '_{x}(t)&=V(\gamma _{x}(t))\qquad \forall t\in (-\varepsilon ,+\varepsilon )\subset \mathbb {R} .\end{aligned}}$

The curves $\gamma _{x}$ are called **integral curves** or **trajectories** (or less commonly, flow lines) of the vector field V and partition S into equivalence classes. It is not always possible to extend the interval $(-\varepsilon ,+\varepsilon )$ to the whole real number line. The flow may for example reach the edge of S in a finite time. In two or three dimensions one can visualize the vector field as giving rise to a flow on S . If we drop a particle into this flow at a point p it will move along the curve $\gamma _{p}$ in the flow depending on the initial point p . If p is a stationary point of V (i.e., the vector field is equal to the zero vector at the point p ), then the particle will remain at p .

Typical applications are pathline in fluid, geodesic flow, and one-parameter subgroups and the exponential map in Lie groups.

### Complete vector fields

By definition, a vector field on M is called **complete** if each of its flow curves exists for all time. In particular, compactly supported vector fields on a manifold are complete. If X is a complete vector field on M , then the one-parameter group of diffeomorphisms generated by the flow along X exists for all time; it is described by a smooth mapping $\mathbf {R} \times M\to M.$ On a compact manifold without boundary, every smooth vector field is complete. An example of an **incomplete** vector field V on the real line $\mathbb {R}$ is given by $V(x)=x^{2}$ . For, the differential equation ${\textstyle x'(t)=x^{2}}$ , with initial condition $x(0)=x_{0}$ , has as its unique solution ${\textstyle x(t)={\frac {x_{0}}{1-tx_{0}}}}$ if $x_{0}\neq 0$ (and $x(t)=0$ for all $t\in \mathbb {R}$ if $x_{0}=0$ ). Hence for $x_{0}\neq 0$ , $x(t)$ is undefined at ${\textstyle t={\frac {1}{x_{0}}}}$ so cannot be defined for all values of t .

### The Lie bracket

The flows associated to two vector fields need not commute with each other. Their failure to commute is described by the Lie bracket of two vector fields, which is again a vector field. The Lie bracket has a simple definition in terms of the action of vector fields on smooth functions f : $[X,Y](f):=X(Y(f))-Y(X(f)).$

## *f*-relatedness

Given a smooth function between manifolds, $f:M\to N$ , the derivative is an induced map on tangent bundles, $f_{*}:TM\to TN$ . Given vector fields $V:M\to TM$ and $W:N\to TN$ , we say that W is f -related to V if the equation $W\circ f=f_{*}\circ V$ holds.

If $V_{i}$ is f -related to $W_{i}$ , $i=1,2$ , then the Lie bracket $[V_{1},V_{2}]$ is f -related to $[W_{1},W_{2}]$ .

## Generalizations

Replacing vectors by *p*-vectors (*p*th exterior power of vectors) yields *p*-vector fields; taking the dual space and exterior powers yields differential *k*-forms, and combining these yields general tensor fields.

Algebraically, vector fields can be characterized as derivations of the algebra of smooth functions on the manifold, which leads to defining a vector field on a commutative algebra as a derivation on the algebra, which is developed in the theory of differential calculus over commutative algebras.

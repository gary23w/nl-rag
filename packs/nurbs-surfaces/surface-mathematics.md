---
title: "Surface (mathematics)"
source: https://en.wikipedia.org/wiki/Surface_(mathematics)
domain: nurbs-surfaces
license: CC-BY-SA-4.0
tags: nurbs surface, non-uniform rational b-spline, nurbs control point, b-spline surface modeling
fetched: 2026-07-02
---

# Surface (mathematics)

In mathematics, a **surface** is a mathematical model of the common concept of a surface. It is a generalization of a plane, but, unlike a plane, it may be curved (this is analogous to a curve generalizing a straight line). An example of a non-flat surface is the sphere.

There are several more precise definitions, depending on the context and the mathematical tools that are used for the study. The simplest mathematical surfaces are planes and spheres in the Euclidean 3-space. Typically, in algebraic geometry, a surface may cross itself (and may have other singularities), while, in topology and differential geometry, it may not.

A surface is a topological space of dimension two; this means that a moving point on a surface may move in two directions (it has two degrees of freedom). In other words, around almost every point, there is a *coordinate patch* on which a two-dimensional coordinate system is defined. For example, the surface of the Earth resembles (ideally) a sphere, and latitude and longitude provide two-dimensional coordinates on it (except at the poles and along the 180th meridian).

## Definitions

Often, a surface is defined by equations that are satisfied by the coordinates of its points. This is the case for the graph of a continuous function of two variables. The set of the zeros of a function of three variables is a surface, which is called an implicit surface. If the defining three-variable function is a polynomial, the surface is an algebraic surface. For example, the unit sphere is an algebraic surface, as it may be defined by the implicit equation

$x^{2}+y^{2}+z^{2}-1=0.$

A surface may also be defined as the image, in some space of dimension at least 3, of a continuous function of two variables (some further conditions are required to ensure that the image is not a curve). In this case, one says that one has a parametric surface, which is *parametrized* by these two variables, called *parameters*. For example, the unit sphere may be parametrized by the Euler angles, also called longitude u and latitude v by

${\begin{aligned}x&=\cos(u)\cos(v)\\y&=\sin(u)\cos(v)\\z&=\sin(v)\,.\end{aligned}}$

Parametric equations of surfaces are often irregular at some points. For example, all but two points of the unit sphere, are the image, by the above parametrization, of exactly one pair of Euler angles (modulo 2π). For the remaining two points (the north and south poles), one has cos *v* = 0, and the longitude *u* may take any values. Also, there are surfaces for which there cannot exist a single parametrization that covers the whole surface. Therefore, one often considers surfaces which are parametrized by several parametric equations, whose images cover the surface. This is formalized by the concept of manifold: in the context of manifolds, typically in topology and differential geometry, a surface is a manifold of dimension two; this means that a surface is a topological space such that every point has a neighborhood which is homeomorphic to an open subset of the Euclidean plane (see Surface (topology) and Surface (differential geometry)). This allows defining surfaces in spaces of dimension higher than three, and even *abstract surfaces*, which are not contained in any other space. On the other hand, this excludes surfaces that have singularities, such as the vertex of a conical surface or points where a surface crosses itself.

In classical geometry, a surface is generally defined as a locus of a point or a line. For example, a sphere is the locus of a point which is at a given distance of a fixed point, called the center; a conical surface is the locus of a line passing through a fixed point and crossing a curve; a surface of revolution is the locus of a curve rotating around a line. A ruled surface is the locus of a moving line satisfying some constraints; in modern terminology, a ruled surface is a surface, which is a union of lines.

## Terminology

There are several kinds of surfaces that are considered in mathematics. An unambiguous terminology is thus necessary to distinguish them when needed. A *topological surface* is a surface that is a manifold of dimension two (see § Topological surface). A *differentiable surface* is a surfaces that is a differentiable manifold (see § Differentiable surface). Every differentiable surface is a topological surface, but the converse is false.

A "surface" is often implicitly supposed to be contained in a Euclidean space of dimension 3, typically **R**3. A surface that is contained in a projective space is called a projective surface (see § Projective surface). A surface that is not supposed to be included in another space is called an *abstract surface*.

## Examples

- The graph of a continuous function of two variables, defined over a connected open subset of **R**2 is a *topological surface*. If the function is differentiable, the graph is a *differentiable surface*.
- A plane is both an algebraic surface and a differentiable surface. It is also a ruled surface and a surface of revolution.
- A circular cylinder (that is, the locus of a line crossing a circle and parallel to a given direction) is an algebraic surface and a differentiable surface.
- A circular cone (locus of a line crossing a circle, and passing through a fixed point, the *apex*, which is outside the plane of the circle) is an algebraic surface which is not a differentiable surface. If one removes the apex, the remainder of the cone is the union of two differentiable surfaces.
- The surface of a polyhedron is a topological surface, which is neither a differentiable surface nor an algebraic surface.
- A hyperbolic paraboloid (the graph of the function *z* = *xy*) is a differentiable surface and an algebraic surface. It is also a ruled surface, and, for this reason, is often used in architecture.
- A two-sheet hyperboloid is an algebraic surface and the union of two non-intersecting differentiable surfaces.

## Parametric surface

A **parametric surface** is the image of an open subset of the Euclidean plane (typically $\mathbb {R} ^{2}$ ) by a continuous function, in a topological space, generally a Euclidean space of dimension at least three. Usually the function is supposed to be continuously differentiable, and this will be always the case in this article.

Specifically, a parametric surface in $\mathbb {R} ^{3}$ is given by three functions of two variables u and v, called *parameters*

${\begin{aligned}x&=f_{1}(u,v),\\[4pt]y&=f_{2}(u,v),\\[4pt]z&=f_{3}(u,v)\,.\end{aligned}}$

As the image of such a function may be a curve (for example, if the three functions are constant with respect to v), a further condition is required, generally that, for almost all values of the parameters, the Jacobian matrix

${\begin{bmatrix}{\dfrac {\partial f_{1}}{\partial u}}&{\dfrac {\partial f_{1}}{\partial v}}\\[6pt]{\dfrac {\partial f_{2}}{\partial u}}&{\dfrac {\partial f_{2}}{\partial v}}\\[6pt]{\dfrac {\partial f_{3}}{\partial u}}&{\dfrac {\partial f_{3}}{\partial v}}\end{bmatrix}}$

has rank two. Here "almost all" means that the values of the parameters where the rank is two contain a dense open subset of the range of the parametrization. For surfaces in a space of higher dimension, the condition is the same, except for the number of columns of the Jacobian matrix.

### Tangent plane and normal vector

A point p where the above Jacobian matrix has rank two is called *regular*, or, more properly, the parametrization is called *regular* at p.

The *tangent plane* at a regular point p is the unique plane passing through p and having a direction parallel to the two row vectors of the Jacobian matrix. The tangent plane is an affine concept, because its definition is independent of the choice of a metric. In other words, any affine transformation maps the tangent plane to the surface at a point to the tangent plane to the image of the surface at the image of the point.

The *normal line* at a point of a surface is the unique line passing through the point and perpendicular to the tangent plane; a *normal vector* is a vector which is parallel to the normal line.

For other differential invariants of surfaces, in the neighborhood of a point, see Differential geometry of surfaces.

### Irregular point and singular point

A point of a parametric surface which is not regular is **irregular**. There are several kinds of irregular points.

It may occur that an irregular point becomes regular, if one changes the parametrization. This is the case of the poles in the parametrization of the unit sphere by Euler angles: it suffices to permute the role of the different coordinate axes for changing the poles.

On the other hand, consider the circular cone of parametric equation

${\begin{aligned}x&=t\cos(u)\\y&=t\sin(u)\\z&=t\,.\end{aligned}}$

The apex of the cone is the origin (0, 0, 0), and is obtained for *t* = 0. It is an irregular point that remains irregular, whichever parametrization is chosen (otherwise, there would exist a unique tangent plane). Such an irregular point, where the tangent plane is undefined, is said **singular**.

There is another kind of singular points. There are the **self-crossing points**, that is the points where the surface crosses itself. In other words, these are the points which are obtained for (at least) two different values of the parameters.

### Graph of a bivariate function

Let *z* = *f*(*x*, *y*) be a function of two real variables, a *bivariate function*. This is a parametric surface, parametrized as

${\begin{aligned}x&=t\\y&=u\\z&=f(t,u)\,.\end{aligned}}$

Every point of this surface is regular, as the two first columns of the Jacobian matrix form the identity matrix of rank two.

### Rational surface

A **rational surface** is a surface that may be parametrized by rational functions of two variables. That is, if *fi*(*t*, *u*) are, for *i* = 0, 1, 2, 3, polynomials in two indeterminates, then the parametric surface, defined by

${\begin{aligned}x&={\frac {f_{1}(t,u)}{f_{0}(t,u)}},\\[6pt]y&={\frac {f_{2}(t,u)}{f_{0}(t,u)}},\\[6pt]z&={\frac {f_{3}(t,u)}{f_{0}(t,u)}}\,,\end{aligned}}$

is a rational surface.

A rational surface is an algebraic surface, but most algebraic surfaces are not rational.

## Implicit surface

An implicit surface in a Euclidean space (or, more generally, in an affine space) of dimension 3 is the set of the common zeros of a differentiable function of three variables

$f(x,y,z)=0.$

Implicit means that the equation defines implicitly one of the variables as a function of the other variables. This is made more exact by the implicit function theorem: if *f*(*x*0, *y*0, *z*0) = 0, and the partial derivative in z of f is not zero at (*x*0, *y*0, *z*0), then there exists a differentiable function *φ*(*x*, *y*) such that

$f(x,y,\varphi (x,y))=0$

in a neighbourhood of (*x*0, *y*0, *z*0). In other words, the implicit surface is the graph of a function near a point of the surface where the partial derivative in z is nonzero. An implicit surface has thus, locally, a parametric representation, except at the points of the surface where the three partial derivatives are zero.

### Regular points and tangent plane

A point of the surface where at least one partial derivative of f is nonzero is called **regular**. At such a point $(x_{0},y_{0},z_{0})$ , the tangent plane and the direction of the normal are well defined, and may be deduced, with the implicit function theorem from the definition given above, in § Tangent plane and normal vector. The direction of the normal is the gradient, that is the vector

$\left[{\frac {\partial f}{\partial x}}(x_{0},y_{0},z_{0}),{\frac {\partial f}{\partial y}}(x_{0},y_{0},z_{0}),{\frac {\partial f}{\partial z}}(x_{0},y_{0},z_{0})\right].$

The tangent plane is defined by its implicit equation

${\frac {\partial f}{\partial x}}(x_{0},y_{0},z_{0})(x-x_{0})+{\frac {\partial f}{\partial y}}(x_{0},y_{0},z_{0})(y-y_{0})+{\frac {\partial f}{\partial z}}(x_{0},y_{0},z_{0})(z-z_{0})=0.$

### Singular point

A **singular point** of an implicit surface (in $\mathbb {R} ^{3}$ ) is a point of the surface where the implicit equation holds and the three partial derivatives of its defining function are all zero. Therefore, the singular points are the solutions of a system of four equations in three indeterminates. As most such systems have no solution, many surfaces do not have any singular point. A surface with no singular point is called *regular* or *non-singular*.

The study of surfaces near their singular points and the classification of the singular points is singularity theory. A singular point is isolated if there is no other singular point in a neighborhood of it. Otherwise, the singular points may form a curve. This is in particular the case for self-crossing surfaces.

## Algebraic surface

Originally, an algebraic surface was a surface which could be defined by an implicit equation

$f(x,y,z)=0,$

where *f* is a polynomial in three indeterminates, with real coefficients.

The concept has been extended in several directions, by defining surfaces over arbitrary fields, and by considering surfaces in spaces of arbitrary dimension or in projective spaces. Abstract algebraic surfaces, which are not explicitly embedded in another space, are also considered.

### Surfaces over arbitrary fields

Polynomials with coefficients in any field are accepted for defining an algebraic surface. However, the field of coefficients of a polynomial is not well defined, as, for example, a polynomial with rational coefficients may also be considered as a polynomial with real or complex coefficients. Therefore, the concept of *point* of the surface has been generalized in the following way.

Given a polynomial *f*(*x*, *y*, *z*), let *k* be the smallest field containing the coefficients, and *K* be an algebraically closed extension of *k*, of infinite transcendence degree. Then a *point* of the surface is an element of *K*3 which is a solution of the equation

$f(x,y,z)=0.$

If the polynomial has real coefficients, the field *K* is the complex field, and a point of the surface that belongs to $\mathbb {R} ^{3}$ (a usual point) is called a *real point*. A point that belongs to *k*3 is called *rational over k*, or simply a *rational point*, if *k* is the field of rational numbers.

### Projective surface

A **projective surface** in a projective space of dimension three is the set of points whose homogeneous coordinates are zeros of a single homogeneous polynomial in four variables. More generally, a projective surface is a subset of a projective space, which is a projective variety of dimension two.

Projective surfaces are strongly related to affine surfaces (that is, ordinary algebraic surfaces). One passes from a projective surface to the corresponding affine surface by setting to one some coordinate or indeterminate of the defining polynomials (usually the last one). Conversely, one passes from an affine surface to its associated projective surface (called *projective completion*) by homogenizing the defining polynomial (in case of surfaces in a space of dimension three), or by homogenizing all polynomials of the defining ideal (for surfaces in a space of higher dimension).

### In higher dimensional spaces

One cannot define the concept of an algebraic surface in a space of dimension higher than three without a general definition of an algebraic variety and of the dimension of an algebraic variety. In fact, an algebraic surface is an *algebraic variety of dimension two*.

More precisely, an algebraic surface in a space of dimension n is the set of the common zeros of at least *n* – 2 polynomials, but these polynomials must satisfy further conditions that may be not immediate to verify. Firstly, the polynomials must not define a variety or an algebraic set of higher dimension, which is typically the case if one of the polynomials is in the ideal generated by the others. Generally, *n* – 2 polynomials define an algebraic set of dimension two or higher. If the dimension is two, the algebraic set may have several irreducible components. If there is only one component the *n* – 2 polynomials define a surface, which is a complete intersection. If there are several components, then one needs further polynomials for selecting a specific component.

Most authors consider as an algebraic surface only algebraic varieties of dimension two, but some also consider as surfaces all algebraic sets whose irreducible components have the dimension two.

In the case of surfaces in a space of dimension three, every surface is a complete intersection, and a surface is defined by a single polynomial, which is irreducible or not, depending on whether non-irreducible algebraic sets of dimension two are considered as surfaces or not.

## Topological surface

In topology, a surface is generally defined as a manifold of dimension two. This means that a topological surface is a topological space such that every point has a neighborhood that is homeomorphic to an open subset of a Euclidean plane.

Every topological surface is homeomorphic to a polyhedral surface such that all facets are triangles. The combinatorial study of such arrangements of triangles (or, more generally, of higher-dimensional simplexes) is the starting object of algebraic topology. This allows the characterization of the properties of surfaces in terms of purely algebraic invariants, such as the genus and homology groups.

The homeomorphism classes of surfaces have been completely described (see Surface (topology)).

## Differentiable surface

In mathematics, the differential geometry of surfaces deals with the differential geometry of smooth surfaces with various additional structures, most often, a Riemannian metric.

Surfaces have been extensively studied from various perspectives: *extrinsically*, relating to their embedding in Euclidean space and *intrinsically*, reflecting their properties determined solely by the distance within the surface as measured along curves on the surface. One of the fundamental concepts investigated is the Gaussian curvature, first studied in depth by Carl Friedrich Gauss, who showed that curvature was an intrinsic property of a surface, independent of its isometric embedding in Euclidean space.

Surfaces naturally arise as graphs of functions of a pair of variables, and sometimes appear in parametric form or as loci associated to space curves. An important role in their study has been played by Lie groups (in the spirit of the Erlangen program), namely the symmetry groups of the Euclidean plane, the sphere and the hyperbolic plane. These Lie groups can be used to describe surfaces of constant Gaussian curvature; they also provide an essential ingredient in the modern approach to intrinsic differential geometry through connections. On the other hand, extrinsic properties relying on an embedding of a surface in Euclidean space have also been extensively studied. This is well illustrated by the non-linear Euler–Lagrange equations in the calculus of variations: although Euler developed the one variable equations to understand geodesics, defined independently of an embedding, one of Lagrange's main applications of the two variable equations was to minimal surfaces, a concept that can only be defined in terms of an embedding.

## Fractal surface

A fractal landscape or fractal surface is generated using a stochastic algorithm designed to produce fractal behavior that mimics the appearance of natural terrain. In other words, the surface resulting from the procedure is not a deterministic, but rather a random surface that exhibits fractal behavior.

Many natural phenomena exhibit some form of statistical self-similarity that can be modeled by fractal surfaces. Moreover, variations in surface texture provide important visual cues to the orientation and slopes of surfaces, and the use of almost self-similar fractal patterns can help create natural looking visual effects. The modeling of the Earth's rough surfaces via fractional Brownian motion was first proposed by Benoit Mandelbrot.

Because the intended result of the process is to produce a landscape, rather than a mathematical function, processes are frequently applied to such landscapes that may affect the stationarity and even the overall fractal behavior of such a surface, in the interests of producing a more convincing landscape.

According to R. R. Shearer, the generation of natural looking surfaces and landscapes was a major turning point in art history, where the distinction between geometric, computer generated images and natural, man made art became blurred. The first use of a fractal-generated landscape in a film was in 1982 for the movie *Star Trek II: The Wrath of Khan*. Loren Carpenter refined the techniques of Mandelbrot to create an alien landscape.

## In computer graphics

In technical applications of 3D computer graphics (CAx) such as computer-aided design and computer-aided manufacturing, surfaces are one way of representing objects. The other ways are wireframe (lines and curves) and solids. Point clouds are also sometimes used as temporary ways to represent an object, with the goal of using the points to create one or more of the three permanent representations.

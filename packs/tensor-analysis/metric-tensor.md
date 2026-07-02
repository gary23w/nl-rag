---
title: "Metric tensor"
source: https://en.wikipedia.org/wiki/Metric_tensor
domain: tensor-analysis
license: CC-BY-SA-4.0
tags: tensor calculus, covariant derivative, metric tensor, christoffel symbols
fetched: 2026-07-02
---

# Metric tensor

In the mathematical field of differential geometry, a **metric tensor** (or simply **metric**) is an additional structure on a manifold M (such as a surface) that allows defining distances and angles, just as the inner product on a Euclidean space allows defining distances and angles there. More precisely, a metric tensor at a point p of M is a bilinear form defined on the tangent space at p (that is, a bilinear function that maps pairs of tangent vectors to real numbers), and a metric field on M consists of a metric tensor at each point p of M that varies smoothly with p.

A metric tensor g is *positive-definite* if $g(v,v)>0$ for every nonzero vector v. A manifold equipped with a positive-definite metric tensor is known as a Riemannian manifold. Such a metric tensor can be thought of as specifying *infinitesimal* distance on the manifold. On a Riemannian manifold M, the length of a smooth curve between two points p and q can be defined by integration, and the distance between p and q can be defined as the infimum of the lengths of all such curves; this makes M a metric space. Conversely, the metric tensor itself is the derivative of the distance function (taken in a suitable manner).

While the notion of a metric tensor was known in some sense to mathematicians such as Gauss from the early 19th century, it was not until the early 20th century that its properties as a tensor were understood by, in particular, Gregorio Ricci-Curbastro and Tullio Levi-Civita, who first codified the notion of a tensor. The metric tensor is an example of a tensor field.

The components of a metric tensor in a coordinate basis take on the form of a symmetric matrix whose entries transform covariantly under changes to the coordinate system. Thus a metric tensor is a covariant symmetric tensor. From the coordinate-independent point of view, a metric tensor field is defined to be a nondegenerate symmetric bilinear form on each tangent space that varies smoothly from point to point.

## Introduction

Carl Friedrich Gauss in his 1827 *Disquisitiones generales circa superficies curvas* (*General investigations of curved surfaces*) considered a surface parametrically, with the Cartesian coordinates x, y, and z of points on the surface depending on two auxiliary variables u and v. Thus a parametric surface is (in today's terms) a vector-valued function

${\vec {r}}(u,\,v)={\bigl (}x(u,\,v),\,y(u,\,v),\,z(u,\,v){\bigr )}$

depending on an ordered pair of real variables (*u*, *v*), and defined in an open set D in the uv-plane. One of the chief aims of Gauss's investigations was to deduce those features of the surface which could be described by a function which would remain unchanged if the surface underwent a transformation in space (such as bending the surface without stretching it), or a change in the particular parametric form of the same geometrical surface.

One natural such invariant quantity is the length of a curve drawn along the surface. Another is the angle between a pair of curves drawn along the surface and meeting at a common point. A third such quantity is the area of a piece of the surface. The study of these invariants of a surface led Gauss to introduce the predecessor of the modern notion of the metric tensor.

The metric tensor is ${\textstyle {\begin{bmatrix}E&F\\F&G\end{bmatrix}}}$ in the description below; E, F, and G in the matrix can contain any number as long as the matrix is positive definite.

### Arc length

If the variables u and v are taken to depend on a third variable, t, taking values in an interval [*a*, *b*], then *r*→(*u*(*t*), *v*(*t*)) will trace out a parametric curve in parametric surface M. The arc length of that curve is given by the integral

${\begin{aligned}s&=\int _{a}^{b}\left\|{\frac {d}{dt}}{\vec {r}}(u(t),v(t))\right\|\,dt\\[5pt]&=\int _{a}^{b}{\sqrt {u'(t)^{2}\,{\vec {r}}_{u}\cdot {\vec {r}}_{u}+2u'(t)v'(t)\,{\vec {r}}_{u}\cdot {\vec {r}}_{v}+v'(t)^{2}\,{\vec {r}}_{v}\cdot {\vec {r}}_{v}}}\,dt\,,\end{aligned}}$

where $\left\|\cdot \right\|$ represents the Euclidean norm. Here the chain rule has been applied, and the subscripts denote partial derivatives:

${\vec {r}}_{u}={\frac {\partial {\vec {r}}}{\partial u}}\,,\quad {\vec {r}}_{v}={\frac {\partial {\vec {r}}}{\partial v}}\,.$

The integrand is the restriction to the curve of the square root of the (quadratic) differential

| $(ds)^{2}=E\,(du)^{2}+2F\,du\,dv+G\,(dv)^{2},$ |   | 1 |
|---|---|---|

where

| $E={\vec {r}}_{u}\cdot {\vec {r}}_{u},\quad F={\vec {r}}_{u}\cdot {\vec {r}}_{v},\quad G={\vec {r}}_{v}\cdot {\vec {r}}_{v}.$ |   | 2 |
|---|---|---|

The quantity ds in (**1**) is called the line element, while *ds*2 is called the first fundamental form of M. Intuitively, it represents the principal part of the square of the displacement undergone by *r*→(*u*, *v*) when u is increased by du units, and v is increased by dv units.

Using matrix notation, the first fundamental form becomes

$ds^{2}={\begin{bmatrix}du&dv\end{bmatrix}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}du\\dv\end{bmatrix}}$

### Coordinate transformations

Suppose now that a different parameterization is selected, by allowing u and v to depend on another pair of variables *u*′ and *v*′. Then the analog of (**2**) for the new variables is

| $E'={\vec {r}}_{u'}\cdot {\vec {r}}_{u'},\quad F'={\vec {r}}_{u'}\cdot {\vec {r}}_{v'},\quad G'={\vec {r}}_{v'}\cdot {\vec {r}}_{v'}.$ |   | 2' |
|---|---|---|

The chain rule relates *E*′, *F*′, and *G*′ to E, F, and G via the matrix equation

| ${\begin{bmatrix}E'&F'\\F'&G'\end{bmatrix}}={\begin{bmatrix}{\frac {\partial u}{\partial u'}}&{\frac {\partial u}{\partial v'}}\\{\frac {\partial v}{\partial u'}}&{\frac {\partial v}{\partial v'}}\end{bmatrix}}^{\mathsf {T}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}{\frac {\partial u}{\partial u'}}&{\frac {\partial u}{\partial v'}}\\{\frac {\partial v}{\partial u'}}&{\frac {\partial v}{\partial v'}}\end{bmatrix}}$ |   | 3 |
|---|---|---|

where the superscript T denotes the matrix transpose. The matrix with the coefficients E, F, and G arranged in this way therefore transforms by the Jacobian matrix of the coordinate change

$J={\begin{bmatrix}{\frac {\partial u}{\partial u'}}&{\frac {\partial u}{\partial v'}}\\{\frac {\partial v}{\partial u'}}&{\frac {\partial v}{\partial v'}}\end{bmatrix}}\,.$

A matrix which transforms in this way is one kind of what is called a tensor. The matrix

${\begin{bmatrix}E&F\\F&G\end{bmatrix}}$

with the transformation law (**3**) is known as the metric tensor of the surface.

### Invariance of arclength under coordinate transformations

Ricci-Curbastro & Levi-Civita (1900) first observed the significance of a system of coefficients E, F, and G, that transformed in this way on passing from one system of coordinates to another. The upshot is that the first fundamental form (**1**) is *invariant* under changes in the coordinate system, and that this follows exclusively from the transformation properties of E, F, and G. Indeed, by the chain rule,

${\begin{bmatrix}du\\dv\end{bmatrix}}={\begin{bmatrix}{\dfrac {\partial u}{\partial u'}}&{\dfrac {\partial u}{\partial v'}}\\{\dfrac {\partial v}{\partial u'}}&{\dfrac {\partial v}{\partial v'}}\end{bmatrix}}{\begin{bmatrix}du'\\dv'\end{bmatrix}}$

so that

${\begin{aligned}ds^{2}&={\begin{bmatrix}du&dv\end{bmatrix}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}du\\dv\end{bmatrix}}\\[6pt]&={\begin{bmatrix}du'&dv'\end{bmatrix}}{\begin{bmatrix}{\dfrac {\partial u}{\partial u'}}&{\dfrac {\partial u}{\partial v'}}\\[6pt]{\dfrac {\partial v}{\partial u'}}&{\dfrac {\partial v}{\partial v'}}\end{bmatrix}}^{\mathsf {T}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}{\dfrac {\partial u}{\partial u'}}&{\dfrac {\partial u}{\partial v'}}\\[6pt]{\dfrac {\partial v}{\partial u'}}&{\dfrac {\partial v}{\partial v'}}\end{bmatrix}}{\begin{bmatrix}du'\\dv'\end{bmatrix}}\\[6pt]&={\begin{bmatrix}du'&dv'\end{bmatrix}}{\begin{bmatrix}E'&F'\\F'&G'\end{bmatrix}}{\begin{bmatrix}du'\\dv'\end{bmatrix}}\\[6pt]&=(ds')^{2}\,.\end{aligned}}$

### Length and angle

Another interpretation of the metric tensor, also considered by Gauss, is that it provides a way in which to compute the length of tangent vectors to the surface, as well as the angle between two tangent vectors. In contemporary terms, the metric tensor allows one to compute the dot product of tangent vectors in a manner independent of the parametric description of the surface. Any tangent vector at a point of the parametric surface M can be written in the form

$\mathbf {p} =p_{1}{\vec {r}}_{u}+p_{2}{\vec {r}}_{v}$

for suitable real numbers *p*1 and *p*2. If two tangent vectors are given:

${\begin{aligned}\mathbf {a} &=a_{1}{\vec {r}}_{u}+a_{2}{\vec {r}}_{v}\\\mathbf {b} &=b_{1}{\vec {r}}_{u}+b_{2}{\vec {r}}_{v}\end{aligned}}$

then using the bilinearity of the dot product,

${\begin{aligned}\mathbf {a} \cdot \mathbf {b} &=a_{1}b_{1}{\vec {r}}_{u}\cdot {\vec {r}}_{u}+a_{1}b_{2}{\vec {r}}_{u}\cdot {\vec {r}}_{v}+a_{2}b_{1}{\vec {r}}_{v}\cdot {\vec {r}}_{u}+a_{2}b_{2}{\vec {r}}_{v}\cdot {\vec {r}}_{v}\\[8pt]&=a_{1}b_{1}E+a_{1}b_{2}F+a_{2}b_{1}F+a_{2}b_{2}G.\\[8pt]&={\begin{bmatrix}a_{1}&a_{2}\end{bmatrix}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}b_{1}\\b_{2}\end{bmatrix}}\,.\end{aligned}}$

This is plainly a function of the four variables *a*1, *b*1, *a*2, and *b*2. It is more profitably viewed, however, as a function that takes a pair of arguments **a** = [*a*1 *a*2] and **b** = [*b*1 *b*2] which are vectors in the uv-plane. That is, put

$g(\mathbf {a} ,\mathbf {b} )=a_{1}b_{1}E+a_{1}b_{2}F+a_{2}b_{1}F+a_{2}b_{2}G\,.$

This is a symmetric function in **a** and **b**, meaning that

$g(\mathbf {a} ,\mathbf {b} )=g(\mathbf {b} ,\mathbf {a} )\,.$

It is also bilinear, meaning that it is linear in each variable **a** and **b** separately. That is,

${\begin{aligned}g\left(\lambda \mathbf {a} +\mu \mathbf {a} ',\mathbf {b} \right)&=\lambda g(\mathbf {a} ,\mathbf {b} )+\mu g\left(\mathbf {a} ',\mathbf {b} \right),\quad {\text{and}}\\g\left(\mathbf {a} ,\lambda \mathbf {b} +\mu \mathbf {b} '\right)&=\lambda g(\mathbf {a} ,\mathbf {b} )+\mu g\left(\mathbf {a} ,\mathbf {b} '\right)\end{aligned}}$

for any vectors **a**, **a**′, **b**, and **b**′ in the uv plane, and any real numbers μ and λ.

In particular, the length of a tangent vector **a** is given by

$\left\|\mathbf {a} \right\|={\sqrt {g(\mathbf {a} ,\mathbf {a} )}}$

and the angle θ between two vectors **a** and **b** is calculated by

$\cos(\theta )={\frac {g(\mathbf {a} ,\mathbf {b} )}{\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|}}\,.$

### Area

The surface area is another numerical quantity which should depend only on the surface itself, and not on how it is parameterized. If the surface M is parameterized by the function *r*→(*u*, *v*) over the domain D in the uv-plane, then the surface area of M is given by the integral

$\iint _{D}\left|{\vec {r}}_{u}\times {\vec {r}}_{v}\right|\,du\,dv$

where × denotes the cross product, and the absolute value denotes the length of a vector in Euclidean space. By Lagrange's identity for the cross product, the integral can be written

${\begin{aligned}&\iint _{D}{\sqrt {\left({\vec {r}}_{u}\cdot {\vec {r}}_{u}\right)\left({\vec {r}}_{v}\cdot {\vec {r}}_{v}\right)-\left({\vec {r}}_{u}\cdot {\vec {r}}_{v}\right)^{2}}}\,du\,dv\\[5pt]={}&\iint _{D}{\sqrt {EG-F^{2}}}\,du\,dv\\[5pt]={}&\iint _{D}{\sqrt {\det {\begin{bmatrix}E&F\\F&G\end{bmatrix}}}}\,du\,dv\end{aligned}}$

where det is the determinant.

## Definition

Let M be a smooth manifold of dimension n; for instance a surface (in the case *n* = 2) or hypersurface in the Cartesian space $\mathbb {R} ^{n+1}$ . At each point *p* ∈ *M* there is a vector space T*p**M*, called the tangent space, consisting of all tangent vectors to the manifold at the point p. A metric tensor at p is a function *g**p*(*X**p*, *Y**p*) which takes as inputs a pair of tangent vectors *X**p* and *Y**p* at p, and produces as an output a real number (scalar), so that the following conditions are satisfied:

- *g**p* is bilinear. A function of two vector arguments is bilinear if it is linear separately in each argument. Thus if *U**p*, *V**p*, *Y**p* are three tangent vectors at p and a and b are real numbers, then ${\begin{aligned}g_{p}(aU_{p}+bV_{p},Y_{p})&=ag_{p}(U_{p},Y_{p})+bg_{p}(V_{p},Y_{p})\,,\quad {\text{and}}\\g_{p}(Y_{p},aU_{p}+bV_{p})&=ag_{p}(Y_{p},U_{p})+bg_{p}(Y_{p},V_{p})\,.\end{aligned}}$
- *g**p* is symmetric. A function of two vector arguments is symmetric provided that for all vectors *X**p* and *Y**p*, $g_{p}(X_{p},Y_{p})=g_{p}(Y_{p},X_{p})\,.$
- *g**p* is nondegenerate. A bilinear function is nondegenerate provided that, for every tangent vector *X**p* ≠ 0, the function $Y_{p}\mapsto g_{p}(X_{p},Y_{p})$ obtained by holding *X**p* constant and allowing *Y**p* to vary is not identically zero. That is, for every *X**p* ≠ 0 there exists a *Y**p* such that *g**p*(*X**p*, *Y**p*) ≠ 0.

A metric tensor field g on M assigns to each point p of M a metric tensor *g**p* in the tangent space at p in a way that varies smoothly with p. More precisely, given any open subset U of manifold M and any (smooth) vector fields X and Y on U, the real function $g(X,Y)(p)=g_{p}(X_{p},Y_{p})$ is a smooth function of p.

## Components of the metric

The components of the metric in any basis of vector fields, or frame, **f** = (*X*1, ..., *X**n*) are given by

| $g_{ij}[\mathbf {f} ]=g\left(X_{i},X_{j}\right).$ |   | 4 |
|---|---|---|

The *n*2 functions *g**ij*[**f**] form the entries of an *n* × *n* symmetric matrix, *G*[**f**]. If

$v=\sum _{i=1}^{n}v^{i}X_{i}\,,\quad w=\sum _{i=1}^{n}w^{i}X_{i}$

are two vectors at *p* ∈ *U*, then the value of the metric applied to v and w is determined by the coefficients (**4**) by bilinearity:

$g(v,w)=\sum _{i,j=1}^{n}v^{i}w^{j}g\left(X_{i},X_{j}\right)=\sum _{i,j=1}^{n}v^{i}w^{j}g_{ij}[\mathbf {f} ]$

Denoting the matrix (*g**ij*[**f**]) by *G*[**f**] and arranging the components of the vectors v and w into column vectors **v**[**f**] and **w**[**f**],

$g(v,w)=\mathbf {v} [\mathbf {f} ]^{\mathsf {T}}G[\mathbf {f} ]\mathbf {w} [\mathbf {f} ]=\mathbf {w} [\mathbf {f} ]^{\mathsf {T}}G[\mathbf {f} ]\mathbf {v} [\mathbf {f} ]$

where **v**[**f**]T and **w**[**f**]T denote the transpose of the vectors **v**[**f**] and **w**[**f**], respectively. Under a change of basis of the form

$\mathbf {f} \mapsto \mathbf {f} '=\left(\sum _{k}X_{k}a_{k1},\dots ,\sum _{k}X_{k}a_{kn}\right)=\mathbf {f} A$

for some invertible *n* × *n* matrix *A* = (*a**ij*), the matrix of components of the metric changes by A as well. That is,

$G[\mathbf {f} A]=A^{\mathsf {T}}G[\mathbf {f} ]A$

or, in terms of the entries of this matrix,

$g_{ij}[\mathbf {f} A]=\sum _{k,l=1}^{n}a_{ki}g_{kl}[\mathbf {f} ]a_{lj}\,.$

For this reason, the system of quantities *g**ij*[**f**] is said to transform covariantly with respect to changes in the frame **f**.

### Metric in coordinates

A system of n real-valued functions (*x*1, ..., *x**n*), giving a local coordinate system on an open set U in M, determines a basis of vector fields on U

$\mathbf {f} =\left(X_{1}={\frac {\partial }{\partial x^{1}}},\dots ,X_{n}={\frac {\partial }{\partial x^{n}}}\right)\,.$

The metric g has components relative to this frame given by

$g_{ij}\left[\mathbf {f} \right]=g\left({\frac {\partial }{\partial x^{i}}},{\frac {\partial }{\partial x^{j}}}\right)\,.$

Relative to a new system of local coordinates, say

$y^{i}=y^{i}(x^{1},x^{2},\dots ,x^{n}),\quad i=1,2,\dots ,n$

the metric tensor will determine a different matrix of coefficients,

$g_{ij}\left[\mathbf {f} '\right]=g\left({\frac {\partial }{\partial y^{i}}},{\frac {\partial }{\partial y^{j}}}\right).$

This new system of functions is related to the original *g**ij*(**f**) by means of the chain rule

${\frac {\partial }{\partial y^{i}}}=\sum _{k=1}^{n}{\frac {\partial x^{k}}{\partial y^{i}}}{\frac {\partial }{\partial x^{k}}}$

so that

$g_{ij}\left[\mathbf {f} '\right]=\sum _{k,l=1}^{n}{\frac {\partial x^{k}}{\partial y^{i}}}g_{kl}\left[\mathbf {f} \right]{\frac {\partial x^{l}}{\partial y^{j}}}.$

Or, in terms of the matrices *G*[**f**] = (*g**ij*[**f**]) and *G*[**f**′] = (*g**ij*[**f**′]),

$G\left[\mathbf {f} '\right]=\left((Dy)^{-1}\right)^{\mathsf {T}}G\left[\mathbf {f} \right](Dy)^{-1}$

where Dy denotes the Jacobian matrix of the coordinate change.

### Signature of a metric

Associated to any metric tensor is the quadratic form defined in each tangent space by

$q_{m}(X_{m})=g_{m}(X_{m},X_{m})\,,\quad X_{m}\in T_{m}M.$

If *q**m* is positive for all non-zero *X**m*, then the metric is positive-definite at m. If the metric is positive-definite at every *m* ∈ *M*, then g is called a Riemannian metric. More generally, if the quadratic forms *q**m* have constant signature independent of m, then the signature of g is this signature, and g is called a pseudo-Riemannian metric. If M is connected, then the signature of qm does not depend on m.

By Sylvester's law of inertia, a basis of tangent vectors *X**i* can be chosen locally so that the quadratic form diagonalizes in the following manner

$q_{m}\left(\sum _{i}\xi ^{i}X_{i}\right)=\left(\xi ^{1}\right)^{2}+\left(\xi ^{2}\right)^{2}+\cdots +\left(\xi ^{p}\right)^{2}-\left(\xi ^{p+1}\right)^{2}-\cdots -\left(\xi ^{n}\right)^{2}$

for some p between 1 and n. Any two such expressions of q (at the same point m of M) will have the same number p of positive signs. The signature of g is the pair of integers (*p*, *n* − *p*), signifying that there are p positive signs and *n* − *p* negative signs in any such expression. Equivalently, the metric has signature (*p*, *n* − *p*) if the matrix *g**ij* of the metric has p positive and *n* − *p* negative eigenvalues.

Certain metric signatures which arise frequently in applications are:

- If g has signature (*n*, 0), then g is a Riemannian metric, and M is called a Riemannian manifold. Otherwise, g is a pseudo-Riemannian metric, and M is called a pseudo-Riemannian manifold (the term semi-Riemannian is also used).
- If M is four-dimensional with signature (1, 3) or (3, 1), then the metric is called Lorentzian. More generally, a metric tensor in dimension n other than 4 of signature (1, *n* − 1) or (*n* − 1, 1) is sometimes also called Lorentzian.
- If M is 2*n*-dimensional and g has signature (*n*, *n*), then the metric is called ultrahyperbolic.

### Inverse metric

Let **f** = (*X*1, ..., *X**n*) be a basis of vector fields, and as above let *G*[**f**] be the matrix of coefficients

$g_{ij}[\mathbf {f} ]=g\left(X_{i},X_{j}\right)\,.$

One can consider the inverse matrix *G*[**f**]−1, which is identified with the **inverse metric** (or *conjugate* or *dual metric*). The inverse metric satisfies a transformation law when the frame **f** is changed by a matrix A via

| $G[\mathbf {f} A]^{-1}=A^{-1}G[\mathbf {f} ]^{-1}\left(A^{-1}\right)^{\mathsf {T}}.$ |   | 5 |
|---|---|---|

The inverse metric transforms *contravariantly*, or with respect to the inverse of the change of basis matrix A. Whereas the metric itself provides a way to measure the length of (or angle between) vector fields, the inverse metric supplies a means of measuring the length of (or angle between) covector fields; that is, fields of linear functionals.

To see this, suppose that α is a covector field. To wit, for each point p, α determines a function *α**p* defined on tangent vectors at p so that the following linearity condition holds for all tangent vectors *X**p* and *Y**p*, and all real numbers a and b:

$\alpha _{p}\left(aX_{p}+bY_{p}\right)=a\alpha _{p}\left(X_{p}\right)+b\alpha _{p}\left(Y_{p}\right)\,.$

As p varies, α is assumed to be a smooth function in the sense that

$p\mapsto \alpha _{p}\left(X_{p}\right)$

is a smooth function of p for any smooth vector field X.

Any covector field α has components in the basis of vector fields **f**. These are determined by

$\alpha _{i}=\alpha \left(X_{i}\right)\,,\quad i=1,2,\dots ,n\,.$

Denote the row vector of these components by

$\alpha [\mathbf {f} ]={\big \lbrack }{\begin{array}{cccc}\alpha _{1}&\alpha _{2}&\dots &\alpha _{n}\end{array}}{\big \rbrack }\,.$

Under a change of **f** by a matrix A, *α*[**f**] changes by the rule

$\alpha [\mathbf {f} A]=\alpha [\mathbf {f} ]A\,.$

That is, the row vector of components *α*[**f**] transforms as a *covariant* vector.

For a pair α and β of covector fields, define the inverse metric applied to these two covectors by

| ${\tilde {g}}(\alpha ,\beta )=\alpha [\mathbf {f} ]G[\mathbf {f} ]^{-1}\beta [\mathbf {f} ]^{\mathsf {T}}.$ |   | 6 |
|---|---|---|

The resulting definition, although it involves the choice of basis **f**, does not actually depend on **f** in an essential way. Indeed, changing basis to **f***A* gives

${\begin{aligned}&\alpha [\mathbf {f} A]G[\mathbf {f} A]^{-1}\beta [\mathbf {f} A]^{\mathsf {T}}\\={}&\left(\alpha [\mathbf {f} ]A\right)\left(A^{-1}G[\mathbf {f} ]^{-1}\left(A^{-1}\right)^{\mathsf {T}}\right)\left(A^{\mathsf {T}}\beta [\mathbf {f} ]^{\mathsf {T}}\right)\\={}&\alpha [\mathbf {f} ]G[\mathbf {f} ]^{-1}\beta [\mathbf {f} ]^{\mathsf {T}}.\end{aligned}}$

So that the right-hand side of equation (**6**) is unaffected by changing the basis **f** to any other basis **f***A* whatsoever. Consequently, the equation may be assigned a meaning independently of the choice of basis. The entries of the matrix *G*[**f**] are denoted by *g**ij*, where the indices i and j have been raised to indicate the transformation law (**5**).

### Raising and lowering indices

In a basis of vector fields **f** = (*X*1, ..., *X**n*), any smooth tangent vector field X can be written in the form

| $X=v^{1}[\mathbf {f} ]X_{1}+v^{2}[\mathbf {f} ]X_{2}+\dots +v^{n}[\mathbf {f} ]X_{n}=\mathbf {f} {\begin{bmatrix}v^{1}[\mathbf {f} ]\\v^{2}[\mathbf {f} ]\\\vdots \\v^{n}[\mathbf {f} ]\end{bmatrix}}=\mathbf {f} v[\mathbf {f} ]$ |   | 7 |
|---|---|---|

for some uniquely determined smooth functions *v*1, ..., *v**n*. Upon changing the basis **f** by a nonsingular matrix A, the coefficients *v**i* change in such a way that equation (**7**) remains true. That is,

$X=\mathbf {fA} v[\mathbf {fA} ]=\mathbf {f} v[\mathbf {f} ]\,.$

Consequently, *v*[**f***A*] = *A*−1*v*[**f**]. In other words, the components of a vector transform *contravariantly* (that is, inversely or in the opposite way) under a change of basis by the nonsingular matrix A. The contravariance of the components of *v*[**f**] is notationally designated by placing the indices of *v**i*[**f**] in the upper position.

A frame also allows covectors to be expressed in terms of their components. For the basis of vector fields **f** = (*X*1, ..., *X**n*) define the dual basis to be the linear functionals (*θ*1[**f**], ..., *θ**n*[**f**]) such that

$\theta ^{i}[\mathbf {f} ](X_{j})={\begin{cases}1&\mathrm {if} \ i=j\\0&\mathrm {if} \ i\not =j.\end{cases}}$

That is, *θ**i*[**f**](*X**j*) = *δ**j**i*, the Kronecker delta. Let

$\theta [\mathbf {f} ]={\begin{bmatrix}\theta ^{1}[\mathbf {f} ]\\\theta ^{2}[\mathbf {f} ]\\\vdots \\\theta ^{n}[\mathbf {f} ]\end{bmatrix}}.$

Under a change of basis **f** ↦ **f***A* for a nonsingular matrix *A*, *θ*[**f**] transforms via

$\theta [\mathbf {f} A]=A^{-1}\theta [\mathbf {f} ].$

Any linear functional α on tangent vectors can be expanded in terms of the dual basis θ

| ${\begin{aligned}\alpha &=a_{1}[\mathbf {f} ]\theta ^{1}[\mathbf {f} ]+a_{2}[\mathbf {f} ]\theta ^{2}[\mathbf {f} ]+\cdots +a_{n}[\mathbf {f} ]\theta ^{n}[\mathbf {f} ]\\[8pt]&={\big \lbrack }{\begin{array}{cccc}a_{1}[\mathbf {f} ]&a_{2}[\mathbf {f} ]&\dots &a_{n}[\mathbf {f} ]\end{array}}{\big \rbrack }\theta [\mathbf {f} ]\\[8pt]&=a[\mathbf {f} ]\theta [\mathbf {f} ]\end{aligned}}$ |   | 8 |
|---|---|---|

where *a*[**f**] denotes the row vector [ *a*1[**f**] ... *a**n*[**f**] ]. The components *a**i* transform when the basis **f** is replaced by **f***A* in such a way that equation (**8**) continues to hold. That is,

$\alpha =a[\mathbf {f} A]\theta [\mathbf {f} A]=a[\mathbf {f} ]\theta [\mathbf {f} ]$

whence, because *θ*[**f***A*] = *A*−1*θ*[**f**], it follows that *a*[**f***A*] = *a*[**f**]*A*. That is, the components a transform *covariantly* (by the matrix A rather than its inverse). The covariance of the components of *a*[**f**] is notationally designated by placing the indices of *a**i*[**f**] in the lower position.

Now, the metric tensor gives a means to identify vectors and covectors as follows. Holding *X**p* fixed, the function

$g_{p}(X_{p},-):Y_{p}\mapsto g_{p}(X_{p},Y_{p})$

of tangent vector *Y**p* defines a linear functional on the tangent space at p. This operation takes a vector *X**p* at a point p and produces a covector *g**p*(*X**p*, −). In a basis of vector fields **f**, if a vector field X has components *v*[**f**], then the components of the covector field *g*(*X*, −) in the dual basis are given by the entries of the row vector

$a[\mathbf {f} ]=v[\mathbf {f} ]^{\mathsf {T}}G[\mathbf {f} ].$

Under a change of basis **f** ↦ **f***A*, the right-hand side of this equation transforms via

$v[\mathbf {f} A]^{\mathsf {T}}G[\mathbf {f} A]=v[\mathbf {f} ]^{\mathsf {T}}\left(A^{-1}\right)^{\mathsf {T}}A^{\mathsf {T}}G[\mathbf {f} ]A=v[\mathbf {f} ]^{\mathsf {T}}G[\mathbf {f} ]A$

so that *a*[**f***A*] = *a*[**f**]*A*: a transforms covariantly. The operation of associating to the (contravariant) components of a vector field *v*[**f**] = [ *v*1[**f**] *v*2[**f**] ... *v**n*[**f**] ]T the (covariant) components of the covector field *a*[**f**] = [ *a*1[**f**] *a*2[**f**] … *a**n*[**f**] ], where

$a_{i}[\mathbf {f} ]=\sum _{k=1}^{n}v^{k}[\mathbf {f} ]g_{ki}[\mathbf {f} ]$

is called **lowering the index**.

To *raise the index*, one applies the same construction but with the inverse metric instead of the metric. If *a*[**f**] = [ *a*1[**f**] *a*2[**f**] ... *a**n*[**f**] ] are the components of a covector in the dual basis *θ*[**f**], then the column vector

| $v[\mathbf {f} ]=G^{-1}[\mathbf {f} ]a[\mathbf {f} ]^{\mathsf {T}}$ |   | 9 |
|---|---|---|

has components which transform contravariantly:

$v[\mathbf {f} A]=A^{-1}v[\mathbf {f} ].$

Consequently, the quantity *X* = **f***v*[**f**] does not depend on the choice of basis **f** in an essential way, and thus defines a vector field on M. The operation (**9**) associating to the (covariant) components of a covector *a*[**f**] the (contravariant) components of a vector *v*[**f**] given is called **raising the index**. In components, (**9**) is

$v^{i}[\mathbf {f} ]=\sum _{k=1}^{n}g^{ik}[\mathbf {f} ]a_{k}[\mathbf {f} ].$

### Induced metric

Let U be an open set in **ℝ***n*, and let φ be a continuously differentiable function from U into the Euclidean space **ℝ***m*, where *m* > *n*. The mapping φ is called an immersion if its differential is injective at every point of U. The image of φ is called an immersed submanifold. More specifically, for *m* = 3, which means that the ambient Euclidean space is **ℝ***3*, the induced metric tensor is called the first fundamental form.

Suppose that φ is an immersion onto the submanifold *M* ⊂ **R***m*. The usual Euclidean dot product in **ℝ***m* is a metric which, when restricted to vectors tangent to M, gives a means for taking the dot product of these tangent vectors. This is called the **induced metric**.

Suppose that v is a tangent vector at a point of U, say

$v=v^{1}\mathbf {e} _{1}+\dots +v^{n}\mathbf {e} _{n}$

where **e***i* are the standard coordinate vectors in **ℝ***n*. When φ is applied to U, the vector v goes over to the vector tangent to M given by

$\varphi _{*}(v)=\sum _{i=1}^{n}\sum _{a=1}^{m}v^{i}{\frac {\partial \varphi ^{a}}{\partial x^{i}}}\mathbf {e} _{a}\,.$

(This is called the pushforward of v along φ.) Given two such vectors, v and w, the induced metric is defined by

$g(v,w)=\varphi _{*}(v)\cdot \varphi _{*}(w).$

It follows from a straightforward calculation that the matrix of the induced metric in the basis of coordinate vector fields **e** is given by

$G(\mathbf {e} )=(D\varphi )^{\mathsf {T}}(D\varphi )$

where Dφ is the Jacobian matrix:

$D\varphi ={\begin{bmatrix}{\frac {\partial \varphi ^{1}}{\partial x^{1}}}&{\frac {\partial \varphi ^{1}}{\partial x^{2}}}&\dots &{\frac {\partial \varphi ^{1}}{\partial x^{n}}}\\[1ex]{\frac {\partial \varphi ^{2}}{\partial x^{1}}}&{\frac {\partial \varphi ^{2}}{\partial x^{2}}}&\dots &{\frac {\partial \varphi ^{2}}{\partial x^{n}}}\\\vdots &\vdots &\ddots &\vdots \\{\frac {\partial \varphi ^{m}}{\partial x^{1}}}&{\frac {\partial \varphi ^{m}}{\partial x^{2}}}&\dots &{\frac {\partial \varphi ^{m}}{\partial x^{n}}}\end{bmatrix}}.$

## Intrinsic definitions of a metric

The notion of a metric can be defined intrinsically using the language of fiber bundles and vector bundles. In these terms, a **metric tensor** is a function

| $g:\mathrm {T} M\times _{M}\mathrm {T} M\to \mathbf {R}$ |   | 10 |
|---|---|---|

from the fiber product of the tangent bundle of M with itself to **R** such that the restriction of g to each fiber is a nondegenerate bilinear mapping

$g_{p}:\mathrm {T} _{p}M\times \mathrm {T} _{p}M\to \mathbf {R} .$

The mapping (**10**) is required to be continuous, and often continuously differentiable, smooth, or real analytic, depending on the case of interest, and whether M can support such a structure.

### Metric as a section of a bundle

By the universal property of the tensor product, any bilinear mapping (**10**) gives rise naturally to a section *g*⊗ of the dual of the tensor product bundle of T*M* with itself

$g_{\otimes }\in \Gamma \left((\mathrm {T} M\otimes \mathrm {T} M)^{*}\right).$

The section *g*⊗ is defined on simple elements of T*M* ⊗ T*M* by

$g_{\otimes }(v\otimes w)=g(v,w)$

and is defined on arbitrary elements of T*M* ⊗ T*M* by extending linearly to linear combinations of simple elements. The original bilinear form g is symmetric if and only if

$g_{\otimes }\circ \tau =g_{\otimes }$

where

$\tau :\mathrm {T} M\otimes \mathrm {T} M\xrightarrow {\cong } TM\otimes TM$

is the braiding map.

Since M is finite-dimensional, there is a natural isomorphism

$(\mathrm {T} M\otimes \mathrm {T} M)^{*}\cong \mathrm {T} ^{*}M\otimes \mathrm {T} ^{*}M,$

so that *g*⊗ is regarded also as a section of the bundle T**M* ⊗ T**M* of the cotangent bundle T**M* with itself. Since g is symmetric as a bilinear mapping, it follows that *g*⊗ is a symmetric tensor.

### Metric in a vector bundle

More generally, one may speak of a metric in a vector bundle. If E is a vector bundle over a manifold M, then a metric is a mapping

$g:E\times _{M}E\to \mathbf {R}$

from the fiber product of E to **R** which is bilinear in each fiber:

$g_{p}:E_{p}\times E_{p}\to \mathbf {R} .$

Using duality as above, a metric is often identified with a section of the tensor product bundle *E** ⊗ *E**.

### Tangent–cotangent isomorphism

The metric tensor gives a natural isomorphism from the tangent bundle to the cotangent bundle, sometimes called the musical isomorphism. This isomorphism is obtained by setting, for each tangent vector *X**p* ∈ T*p**M*,

$S_{g}X_{p}\,{\stackrel {\text{def}}{=}}\,g(X_{p},-),$

the linear functional on T*p**M* which sends a tangent vector *Y**p* at p to *g**p*(*X**p*,*Y**p*). That is, in terms of the pairing [−, −] between T*p**M* and its dual space T∗ *p**M*,

$[S_{g}X_{p},Y_{p}]=g_{p}(X_{p},Y_{p})$

for all tangent vectors *X**p* and *Y**p*. The mapping *S**g* is a linear transformation from T*p**M* to T∗ *p**M*. It follows from the definition of non-degeneracy that the kernel of *S**g* is reduced to zero, and so by the rank–nullity theorem, *S**g* is a linear isomorphism. Furthermore, *S**g* is a symmetric linear transformation in the sense that

$[S_{g}X_{p},Y_{p}]=[S_{g}Y_{p},X_{p}]$

for all tangent vectors *X**p* and *Y**p*.

Conversely, any linear isomorphism *S* : T*p**M* → T∗ *p**M* defines a non-degenerate bilinear form on T*p**M* by means of

$g_{S}(X_{p},Y_{p})=[SX_{p},Y_{p}]\,.$

This bilinear form is symmetric if and only if S is symmetric. There is thus a natural one-to-one correspondence between symmetric bilinear forms on T*p**M* and symmetric linear isomorphisms of T*p**M* to the dual T∗ *p**M*.

As p varies over M, *S**g* defines a section of the bundle Hom(T*M*, T**M*) of vector bundle isomorphisms of the tangent bundle to the cotangent bundle. This section has the same smoothness as g: it is continuous, differentiable, smooth, or real-analytic according as g. The mapping *S**g*, which associates to every vector field on M a covector field on M gives an abstract formulation of "lowering the index" on a vector field. The inverse of *S**g* is a mapping T**M* → T*M* which, analogously, gives an abstract formulation of "raising the index" on a covector field.

The inverse *S*−1 *g* defines a linear mapping

$S_{g}^{-1}:\mathrm {T} ^{*}M\to \mathrm {T} M$

which is nonsingular and symmetric in the sense that

$\left[S_{g}^{-1}\alpha ,\beta \right]=\left[S_{g}^{-1}\beta ,\alpha \right]$

for all covectors α, β. Such a nonsingular symmetric mapping gives rise (by the tensor-hom adjunction) to a map

$\mathrm {T} ^{*}M\otimes \mathrm {T} ^{*}M\to \mathbf {R}$

or by the double dual isomorphism to a section of the tensor product

$\mathrm {T} M\otimes \mathrm {T} M.$

## Arclength and the line element

Suppose that g is a Riemannian metric on M. In a local coordinate system *x**i*, *i* = 1, 2, …, *n*, the metric tensor appears as a matrix, denoted here by **G**, whose entries are the components *g**ij* of the metric tensor relative to the coordinate vector fields.

Let *γ*(*t*) be a piecewise-differentiable parametric curve in M, for *a* ≤ *t* ≤ *b*. The arclength of the curve is defined by

$L=\int _{a}^{b}{\sqrt {\sum _{i,j=1}^{n}g_{ij}(\gamma (t))\left({\frac {d}{dt}}x^{i}\circ \gamma (t)\right)\left({\frac {d}{dt}}x^{j}\circ \gamma (t)\right)}}\,dt\,.$

In connection with this geometrical application, the quadratic differential form

$ds^{2}=\sum _{i,j=1}^{n}g_{ij}(p)dx^{i}dx^{j}$

is called the first fundamental form associated to the metric, while ds is the line element. When *ds*2 is pulled back to the image of a curve in M, it represents the square of the differential with respect to arclength.

For a pseudo-Riemannian metric, the length formula above is not always defined, because the term under the square root may become negative. We generally only define the length of a curve when the quantity under the square root is always of one sign or the other. In this case, define

$L=\int _{a}^{b}{\sqrt {\left|\sum _{i,j=1}^{n}g_{ij}(\gamma (t))\left({\frac {d}{dt}}x^{i}\circ \gamma (t)\right)\left({\frac {d}{dt}}x^{j}\circ \gamma (t)\right)\right|}}\,dt\,.$

While these formulas use coordinate expressions, they are in fact independent of the coordinates chosen; they depend only on the metric, and the curve along which the formula is integrated.

### The energy, variational principles and geodesics

Given a segment of a curve, another frequently defined quantity is the (kinetic) **energy** of the curve:

$E={\frac {1}{2}}\int _{a}^{b}\sum _{i,j=1}^{n}g_{ij}(\gamma (t))\left({\frac {d}{dt}}x^{i}\circ \gamma (t)\right)\left({\frac {d}{dt}}x^{j}\circ \gamma (t)\right)\,dt\,.$

This usage comes from physics, specifically, classical mechanics, where the integral E can be seen to directly correspond to the kinetic energy of a point particle moving on the surface of a manifold. Thus, for example, in Jacobi's formulation of Maupertuis' principle, the metric tensor can be seen to correspond to the mass tensor of a moving particle.

In many cases, whenever a calculation calls for the length to be used, a similar calculation using the energy may be done as well. This often leads to simpler formulas by avoiding the need for the square-root. Thus, for example, the geodesic equations may be obtained by applying variational principles to either the length or the energy. In the latter case, the geodesic equations are seen to arise from the principle of least action: they describe the motion of a "free particle" (a particle feeling no forces) that is confined to move on the manifold, but otherwise moves freely, with constant momentum, within the manifold.

## Canonical measure and volume form

In analogy with the case of surfaces, a metric tensor on an n-dimensional paracompact manifold M gives rise to a natural way to measure the n-dimensional volume of subsets of the manifold. The resulting natural positive Borel measure allows one to develop a theory of integrating functions on the manifold by means of the associated Lebesgue integral.

A measure can be defined, by the Riesz representation theorem, by giving a positive linear functional Λ on the space *C*0(*M*) of compactly supported continuous functions on M. More precisely, if M is a manifold with a (pseudo-)Riemannian metric tensor g, then there is a unique positive Borel measure *μ**g* such that for any coordinate chart (*U*, *φ*), $\Lambda f=\int _{U}f\,d\mu _{g}=\int _{\varphi (U)}f\circ \varphi ^{-1}(x){\sqrt {\left|\det g\right|}}\,dx$ for all f supported in U. Here det *g* is the determinant of the matrix formed by the components of the metric tensor in the coordinate chart. That Λ is well-defined on functions supported in coordinate neighborhoods is justified by Jacobian change of variables. It extends to a unique positive linear functional on *C*0(*M*) by means of a partition of unity.

If M is also oriented, then it is possible to define a natural volume form from the metric tensor. In a positively oriented coordinate system (*x**1*, ..., *x**n*) the volume form is represented as $\omega ={\sqrt {\left|\det g\right|}}\,dx^{1}\wedge \cdots \wedge dx^{n}$ where the *dx**i* are the coordinate differentials and ∧ denotes the exterior product in the algebra of differential forms. The volume form also gives a way to integrate functions on the manifold, and this geometric integral agrees with the integral obtained by the canonical Borel measure.

## Examples

### Euclidean metric

The most familiar example is that of elementary Euclidean geometry: the two-dimensional Euclidean metric tensor. In the usual Cartesian (*x*, *y*) coordinates, we can write

$g={\begin{bmatrix}1&0\\0&1\end{bmatrix}}\,.$

The length of a curve reduces to the formula:

$L=\int _{a}^{b}{\sqrt {(dx)^{2}+(dy)^{2}}}\,.$

The Euclidean metric in some other common coordinate systems can be written as follows.

Polar coordinates (*r*, *θ*):

${\begin{aligned}x&=r\cos \theta \\y&=r\sin \theta \\J&={\begin{bmatrix}\cos \theta &-r\sin \theta \\\sin \theta &r\cos \theta \end{bmatrix}}\,.\end{aligned}}$

So

$g=J^{\mathsf {T}}J={\begin{bmatrix}\cos ^{2}\theta +\sin ^{2}\theta &-r\sin \theta \cos \theta +r\sin \theta \cos \theta \\-r\cos \theta \sin \theta +r\cos \theta \sin \theta &r^{2}\sin ^{2}\theta +r^{2}\cos ^{2}\theta \end{bmatrix}}={\begin{bmatrix}1&0\\0&r^{2}\end{bmatrix}}$

by trigonometric identities.

In general, in a Cartesian coordinate system *x**i* on a Euclidean space, the partial derivatives ∂ / ∂*xi* are orthonormal with respect to the Euclidean metric. Thus the metric tensor is the Kronecker delta δ*ij* in this coordinate system. The metric tensor with respect to arbitrary (possibly curvilinear) coordinates *qi* is given by

$g_{ij}=\sum _{kl}\delta _{kl}{\frac {\partial x^{k}}{\partial q^{i}}}{\frac {\partial x^{l}}{\partial q^{j}}}=\sum _{k}{\frac {\partial x^{k}}{\partial q^{i}}}{\frac {\partial x^{k}}{\partial q^{j}}}.$

#### The round metric on a sphere

The unit sphere in **ℝ**3 comes equipped with a natural metric induced from the ambient Euclidean metric, through the process explained in the induced metric section. In standard spherical coordinates (*θ*, *φ*), with *θ* the colatitude, the angle measured from the z-axis, and φ the angle from the x-axis in the xy-plane, the metric takes the form

$g={\begin{bmatrix}1&0\\0&\sin ^{2}\theta \end{bmatrix}}\,.$

This is usually written in the form

$ds^{2}=d\theta ^{2}+\sin ^{2}\theta \,d\varphi ^{2}\,.$

### Lorentzian metrics from relativity

In flat Minkowski space (special relativity), with coordinates

$r^{\mu }\rightarrow \left(x^{0},x^{1},x^{2},x^{3}\right)=(ct,x,y,z)\,,$

the metric is, depending on choice of metric signature,

$g={\begin{bmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{bmatrix}}\quad {\text{or}}\quad g={\begin{bmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}}\,.$

For a curve with—for example—constant time coordinate, the length formula with this metric reduces to the usual length formula. For a timelike curve, the length formula gives the proper time along the curve.

In this case, the spacetime interval is written as

$ds^{2}=c^{2}dt^{2}-dx^{2}-dy^{2}-dz^{2}=dr^{\mu }dr_{\mu }=g_{\mu \nu }dr^{\mu }dr^{\nu }\,.$

The Schwarzschild metric describes the spacetime around a spherically symmetric body, such as a planet, or a black hole. With coordinates

$\left(x^{0},x^{1},x^{2},x^{3}\right)=(ct,r,\theta ,\varphi )\,,$

we can write the metric as

$g_{\mu \nu }={\begin{bmatrix}\left(1-{\frac {2GM}{rc^{2}}}\right)&0&0&0\\0&-\left(1-{\frac {2GM}{rc^{2}}}\right)^{-1}&0&0\\0&0&-r^{2}&0\\0&0&0&-r^{2}\sin ^{2}\theta \end{bmatrix}}\,,$

where G (inside the matrix) is the gravitational constant and M represents the total mass–energy content of the central object.

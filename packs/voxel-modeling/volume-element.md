---
title: "Volume element"
source: https://en.wikipedia.org/wiki/Volume_element
domain: voxel-modeling
license: CC-BY-SA-4.0
tags: voxel modeling, voxel volume element, constructive solid geometry voxel, voxel grid representation
fetched: 2026-07-02
---

# Volume element

In mathematics, a **volume element** provides a means for integrating a function with respect to volume in various coordinate systems such as spherical coordinates and cylindrical coordinates. Thus a volume element is an expression of the form $\mathrm {d} V=\rho (u_{1},u_{2},u_{3})\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}\,\mathrm {d} u_{3}$ where the $u_{i}$ are the coordinates, so that the volume of any set B can be computed by $\operatorname {Volume} (B)=\int _{B}\rho (u_{1},u_{2},u_{3})\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}\,\mathrm {d} u_{3}.$ For example, in spherical coordinates $\mathrm {d} V=u_{1}^{2}\sin u_{2}\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}\,\mathrm {d} u_{3}$ , and so $\rho =u_{1}^{2}\sin u_{2}$ .

The notion of a volume element is not limited to three dimensions: in two dimensions it is often known as the **area element**, and in this setting it is useful for doing surface integrals. Under changes of coordinates, the volume element changes by the absolute value of the Jacobian determinant of the coordinate transformation (by the change of variables formula). This fact allows volume elements to be defined as a kind of measure on a manifold. On an orientable differentiable manifold, a volume element typically arises from a volume form: a top degree differential form. On a non-orientable manifold, the volume element is typically the absolute value of a (locally defined) volume form: it defines a 1-density.

## Volume element in Euclidean space

In Euclidean space, the volume element is given by the product of the differentials of the Cartesian coordinates $\mathrm {d} V=\mathrm {d} x\,\mathrm {d} y\,\mathrm {d} z.$ In different coordinate systems of the form $x=x(u_{1},u_{2},u_{3})$ , $y=y(u_{1},u_{2},u_{3})$ , $z=z(u_{1},u_{2},u_{3})$ , the volume element changes by the Jacobian (determinant) of the coordinate change: $\mathrm {d} V=\left|{\frac {\partial (x,y,z)}{\partial (u_{1},u_{2},u_{3})}}\right|\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}\,\mathrm {d} u_{3}.$ For example, in spherical coordinates (mathematical convention) ${\begin{aligned}x&=\rho \cos \theta \sin \phi \\y&=\rho \sin \theta \sin \phi \\z&=\rho \cos \phi \end{aligned}}$ the Jacobian determinant is $\left|{\frac {\partial (x,y,z)}{\partial (\rho ,\phi ,\theta )}}\right|=\rho ^{2}\sin \phi$ so that $\mathrm {d} V=\rho ^{2}\sin \phi \,\mathrm {d} \rho \,\mathrm {d} \theta \,\mathrm {d} \phi .$ This can be seen as a special case of the fact that differential forms transform through a pullback $F^{*}$ as $F^{*}(u\;dy^{1}\wedge \cdots \wedge dy^{n})=(u\circ F)\det \left({\frac {\partial F^{j}}{\partial x^{i}}}\right)\mathrm {d} x^{1}\wedge \cdots \wedge \mathrm {d} x^{n}$

## Volume element of a linear subspace

Consider the linear subspace of the *n*-dimensional Euclidean space **R***n* that is spanned by a collection of linearly independent vectors $X_{1},\dots ,X_{k}.$ To find the volume element of the subspace, it is useful to know the fact from linear algebra that the volume of the parallelepiped spanned by the $X_{i}$ is the square root of the determinant of the Gramian matrix of the $X_{i}$ : ${\sqrt {\det(X_{i}\cdot X_{j})_{i,j=1\dots k}}}.$

Any point *p* in the subspace can be given coordinates $(u_{1},u_{2},\dots ,u_{k})$ such that $p=u_{1}X_{1}+\cdots +u_{k}X_{k}.$ At a point *p*, if we form a small parallelepiped with sides $\mathrm {d} u_{i}$ , then the volume of that parallelepiped is the square root of the determinant of the Grammian matrix ${\sqrt {\det \left((du_{i}X_{i})\cdot (du_{j}X_{j})\right)_{i,j=1\dots k}}}={\sqrt {\det(X_{i}\cdot X_{j})_{i,j=1\dots k}}}\;\mathrm {d} u_{1}\,\mathrm {d} u_{2}\,\cdots \,\mathrm {d} u_{k}.$ This therefore defines the volume form in the linear subspace.

## Volume element of manifolds

On an *oriented* Riemannian manifold of dimension *n*, the volume element is a volume form equal to the Hodge dual of the unit constant function, $f(x)=1$ : $\omega =\star 1.$ Equivalently, the volume element is precisely the Levi-Civita tensor $\epsilon$ . In coordinates, $\omega =\epsilon ={\sqrt {\left|\det g\right|}}\,\mathrm {d} x^{1}\wedge \cdots \wedge \mathrm {d} x^{n}$ where $\det g$ is the determinant of the metric tensor *g* written in the coordinate system.

### Area element of a surface

A simple example of a volume element can be explored by considering a two-dimensional surface embedded in *n*-dimensional Euclidean space. Such a volume element is sometimes called an *area element*. Consider a subset $U\subset \mathbb {R} ^{2}$ and a mapping function $\varphi :U\to \mathbb {R} ^{n}$ thus defining a surface embedded in $\mathbb {R} ^{n}$ . In two dimensions, volume is just area, and a volume element gives a way to determine the area of parts of the surface. Thus a volume element is an expression of the form $f(u_{1},u_{2})\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}$ that allows one to compute the area of a set *B* lying on the surface by computing the integral $\operatorname {Area} (B)=\int _{B}f(u_{1},u_{2})\,\mathrm {d} u_{1}\,\mathrm {d} u_{2}.$

Here we will find the volume element on the surface that defines area in the usual sense. The Jacobian matrix of the mapping is $J_{ij}={\frac {\partial \varphi _{i}}{\partial u_{j}}}$ with index *i* running from 1 to *n*, and *j* running from 1 to 2. The Euclidean metric in the *n*-dimensional space induces a metric $g=J^{T}J$ on the set *U*, with matrix elements $g_{ij}=\sum _{k=1}^{n}J_{ki}J_{kj}=\sum _{k=1}^{n}{\frac {\partial \varphi _{k}}{\partial u_{i}}}{\frac {\partial \varphi _{k}}{\partial u_{j}}}.$

The determinant of the metric is given by $\det g=\left|{\frac {\partial \varphi }{\partial u_{1}}}\wedge {\frac {\partial \varphi }{\partial u_{2}}}\right|^{2}=\det(J^{T}J)$

For a regular surface, this determinant is non-vanishing; equivalently, the Jacobian matrix has rank 2.

Now consider a change of coordinates on *U*, given by a diffeomorphism $f\colon U\to U,$ so that the coordinates $(u_{1},u_{2})$ are given in terms of $(v_{1},v_{2})$ by $(u_{1},u_{2})=f(v_{1},v_{2})$ . The Jacobian matrix of this transformation is given by $F_{ij}={\frac {\partial f_{i}}{\partial v_{j}}}.$

In the new coordinates, we have ${\frac {\partial \varphi _{i}}{\partial v_{j}}}=\sum _{k=1}^{2}{\frac {\partial \varphi _{i}}{\partial u_{k}}}{\frac {\partial f_{k}}{\partial v_{j}}}$ and so the metric transforms as ${\tilde {g}}=F^{T}gF$ where ${\tilde {g}}$ is the pullback metric in the *v* coordinate system. The determinant is $\det {\tilde {g}}=\det g\left(\det F\right)^{2}.$

Given the above construction, it should now be straightforward to understand how the volume element is invariant under an orientation-preserving change of coordinates.

In two dimensions, the volume is just the area. The area of a subset $B\subset U$ is given by the integral ${\begin{aligned}{\mbox{Area}}(B)&=\iint _{B}{\sqrt {\det g}}\;\mathrm {d} u_{1}\;\mathrm {d} u_{2}\\[1.6ex]&=\iint _{B}{\sqrt {\det g}}\left|\det F\right|\;\mathrm {d} v_{1}\;\mathrm {d} v_{2}\\[1.6ex]&=\iint _{B}{\sqrt {\det {\tilde {g}}}}\;\mathrm {d} v_{1}\;\mathrm {d} v_{2}.\end{aligned}}$

Thus, in either coordinate system, the volume element takes the same expression: the expression of the volume element is invariant under a change of coordinates.

Note that there was nothing particular to two dimensions in the above presentation; the above trivially generalizes to arbitrary dimensions.

### Example: Sphere

For example, consider the sphere with radius *r* centered at the origin in **R**3. This can be parametrized using spherical coordinates with the map $\phi (u_{1},u_{2})=(r\cos u_{1}\sin u_{2},r\sin u_{1}\sin u_{2},r\cos u_{2}).$ Then $g={\begin{pmatrix}r^{2}\sin ^{2}u_{2}&0\\0&r^{2}\end{pmatrix}},$ and the area element is $\omega ={\sqrt {\det g}}\;\mathrm {d} u_{1}\mathrm {d} u_{2}=r^{2}\sin u_{2}\,\mathrm {d} u_{1}\mathrm {d} u_{2}.$

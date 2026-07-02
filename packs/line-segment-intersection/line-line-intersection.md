---
title: "Line–line intersection"
source: https://en.wikipedia.org/wiki/Line–line_intersection
domain: line-segment-intersection
license: CC-BY-SA-4.0
tags: line segment intersection, bentley ottmann algorithm, sweep line, computational geometry
fetched: 2026-07-02
---

# Line–line intersection

In Euclidean geometry, the **intersection of a line and a line** can be the empty set, a single point, or a line (if they coincide). Distinguishing these cases and finding the intersection have uses, for example, in computer graphics, motion planning, and collision detection.

In a Euclidean space, if two lines are not coplanar, they have no point of intersection and are called skew lines. If they are coplanar, however, there are three possibilities: if they coincide (are the same line), they have all of their infinitely many points in common; if they are distinct but have the same direction, they are said to be parallel and have no points in common; otherwise, they have a single point of intersection, denoted as singleton set, for instance $\{A\}$ .

Non-Euclidean geometry describes spaces in which one line may not be parallel to any other lines, such as a sphere, and spaces where multiple lines through a single point may all be parallel to another line. In spherical and elliptic geometries, every pair of lines intersects, while in hyperbolic geometry there exist infinitely many distinct lines through a given point that do not intersect a given line. Projective geometry provides a unifying framework in which these different behaviors can be described by extending the notion of intersection to include ideal points, so that any two distinct lines intersect in exactly one point.

## Formulas

A necessary condition for two lines to intersect is that they are in the same plane—that is, are not skew lines. Satisfaction of this condition is equivalent to the tetrahedron with vertices at two of the points on one line and two of the points on the other line being degenerate in the sense of having zero volume. For the algebraic form of this condition, see Skew lines § Testing for skewness.

### Given two points on each line

First we consider the intersection of two lines *L*1 and *L*2 in two-dimensional space, with line *L*1 being defined by two distinct points (*x*1, *y*1) and (*x*2, *y*2), and line *L*2 being defined by two distinct points (*x*3, *y*3) and (*x*4, *y*4).

The intersection P of line *L*1 and *L*2 can be defined using determinants.

$P_{x}={\frac {\begin{vmatrix}{\begin{vmatrix}x_{1}&y_{1}\\x_{2}&y_{2}\end{vmatrix}}&{\begin{vmatrix}x_{1}&1\\x_{2}&1\end{vmatrix}}\\\\{\begin{vmatrix}x_{3}&y_{3}\\x_{4}&y_{4}\end{vmatrix}}&{\begin{vmatrix}x_{3}&1\\x_{4}&1\end{vmatrix}}\end{vmatrix}}{\begin{vmatrix}{\begin{vmatrix}x_{1}&1\\x_{2}&1\end{vmatrix}}&{\begin{vmatrix}y_{1}&1\\y_{2}&1\end{vmatrix}}\\\\{\begin{vmatrix}x_{3}&1\\x_{4}&1\end{vmatrix}}&{\begin{vmatrix}y_{3}&1\\y_{4}&1\end{vmatrix}}\end{vmatrix}}}\,\!\qquad P_{y}={\frac {\begin{vmatrix}{\begin{vmatrix}x_{1}&y_{1}\\x_{2}&y_{2}\end{vmatrix}}&{\begin{vmatrix}y_{1}&1\\y_{2}&1\end{vmatrix}}\\\\{\begin{vmatrix}x_{3}&y_{3}\\x_{4}&y_{4}\end{vmatrix}}&{\begin{vmatrix}y_{3}&1\\y_{4}&1\end{vmatrix}}\end{vmatrix}}{\begin{vmatrix}{\begin{vmatrix}x_{1}&1\\x_{2}&1\end{vmatrix}}&{\begin{vmatrix}y_{1}&1\\y_{2}&1\end{vmatrix}}\\\\{\begin{vmatrix}x_{3}&1\\x_{4}&1\end{vmatrix}}&{\begin{vmatrix}y_{3}&1\\y_{4}&1\end{vmatrix}}\end{vmatrix}}}\,\!$

The determinants can be written out as:

${\begin{aligned}P_{x}&={\frac {(x_{1}y_{2}-y_{1}x_{2})(x_{3}-x_{4})-(x_{1}-x_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}}\\[4px]P_{y}&={\frac {(x_{1}y_{2}-y_{1}x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}}\end{aligned}}$

When the two lines are parallel or coincident, the denominator is zero.

### Given two points on each line segment

The intersection point above is for the infinitely long lines defined by the points, rather than the line segments between the points, and can produce an intersection point not contained in either of the two line segments. In order to find the position of the intersection with respect to the line segments, we can define lines *L*1 and *L*2 in terms of first degree Bézier parameters:

$L_{1}={\begin{bmatrix}x_{1}\\y_{1}\end{bmatrix}}+t{\begin{bmatrix}x_{2}-x_{1}\\y_{2}-y_{1}\end{bmatrix}},\qquad L_{2}={\begin{bmatrix}x_{3}\\y_{3}\end{bmatrix}}+u{\begin{bmatrix}x_{4}-x_{3}\\y_{4}-y_{3}\end{bmatrix}}$

(where t and u are real numbers). The intersection point of the lines is found with one of the following values of t or u, where

$t={\frac {\begin{vmatrix}x_{1}-x_{3}&x_{3}-x_{4}\\y_{1}-y_{3}&y_{3}-y_{4}\end{vmatrix}}{\begin{vmatrix}x_{1}-x_{2}&x_{3}-x_{4}\\y_{1}-y_{2}&y_{3}-y_{4}\end{vmatrix}}}={\frac {(x_{1}-x_{3})(y_{3}-y_{4})-(y_{1}-y_{3})(x_{3}-x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}}$

and

$u=-{\frac {\begin{vmatrix}x_{1}-x_{2}&x_{1}-x_{3}\\y_{1}-y_{2}&y_{1}-y_{3}\end{vmatrix}}{\begin{vmatrix}x_{1}-x_{2}&x_{3}-x_{4}\\y_{1}-y_{2}&y_{3}-y_{4}\end{vmatrix}}}=-{\frac {(x_{1}-x_{2})(y_{1}-y_{3})-(y_{1}-y_{2})(x_{1}-x_{3})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}},$

with

$(P_{x},P_{y})={\bigl (}x_{1}+t(x_{2}-x_{1}),\;y_{1}+t(y_{2}-y_{1}){\bigr )}\quad {\text{or}}\quad (P_{x},P_{y})={\bigl (}x_{3}+u(x_{4}-x_{3}),\;y_{3}+u(y_{4}-y_{3}){\bigr )}$

There will be an intersection if 0 ≤ *t* ≤ 1 and 0 ≤ *u* ≤ 1. The intersection point falls within the first line segment if 0 ≤ *t* ≤ 1, and it falls within the second line segment if 0 ≤ *u* ≤ 1. These inequalities can be tested without the need for division, allowing rapid determination of the existence of any line segment intersection before calculating its exact point.

In the case where the two line segments share an x axis and $x_{2}=x_{1}+1$ , t and u simplify to $t=u={\frac {y_{1}-y_{3}}{y_{1}-y_{2}-y_{3}+y_{4}}},$ with $(P_{x},P_{y})={\bigl (}x_{1}+t,\;y_{1}+t(y_{2}-y_{1}){\bigr )}\quad {\text{or}}\quad (P_{x},P_{y})={\bigl (}x_{1}+t,\;y_{3}+t(y_{4}-y_{3}){\bigr )}.$

### Given two line equations

The x and y coordinates of the point of intersection of two non-vertical lines can easily be found using the following substitutions and rearrangements.

Suppose that two lines have the equations *y* = *ax* + *c* and *y* = *bx* + *d* where a and b are the slopes (gradients) of the lines and where c and d are the y-intercepts of the lines. At the point where the two lines intersect (if they do), both y coordinates will be the same, hence the following equality:

$ax+c=bx+d.$

We can rearrange this expression in order to extract the value of x,

$ax-bx=d-c,$

and so,

$x={\frac {d-c}{a-b}}.$

To find the y coordinate, all we need to do is substitute the value of x into either one of the two line equations, for example, into the first:

$y=a{\frac {d-c}{a-b}}+c.$

Hence, the point of intersection is

$P=\left({\frac {d-c}{a-b}},a{\frac {d-c}{a-b}}+c\right).$

Note that if *a* = *b* then the two lines are parallel and they do not intersect, unless *c* = *d* as well, in which case the lines are coincident and they intersect at every point.

### Using homogeneous coordinates

By using homogeneous coordinates, the intersection point of two implicitly defined lines can be determined quite easily. In 2D, every point can be defined as a projection of a 3D point, given as the ordered triple (*x*, *y*, *w*). The mapping from 3D to 2D coordinates is (*x*′, *y*′) = (⁠*x*/*w*⁠, ⁠*y*/*w*⁠). We can convert 2D points to homogeneous coordinates by defining them as (*x*, *y*, 1).

Assume that we want to find intersection of two infinite lines in 2-dimensional space, defined as *a*1*x* + *b*1*y* + *c*1 = 0 and *a*2*x* + *b*2*y* + *c*2 = 0. We can represent these two lines in line coordinates as *U*1 = (*a*1, *b*1, *c*1) and *U*2 = (*a*2, *b*2, *c*2). The intersection *P*′ of two lines is then simply given by

$P'=(a_{p},b_{p},c_{p})=U_{1}\times U_{2}=(b_{1}c_{2}-b_{2}c_{1},a_{2}c_{1}-a_{1}c_{2},a_{1}b_{2}-a_{2}b_{1})$

If *cp* = 0, the lines do not intersect.

## More than two lines

The intersection of two lines can be generalized to involve additional lines. The existence of and expression for the n-line intersection problem are as follows.

### In two dimensions

In two dimensions, more than two lines almost certainly do not intersect at a single point. To determine if they do and, if so, to find the intersection point, write the ith equation (*i* = 1, …, *n*) as

${\begin{bmatrix}a_{i1}&a_{i2}\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}=b_{i},$

and stack these equations into matrix form as

$\mathbf {A} \mathbf {w} =\mathbf {b} ,$

where the ith row of the *n* × 2 matrix **A** is [*a**i*1, *a**i*2], **w** is the 2 × 1 vector [*x* *y*], and the ith element of the column vector **b** is *b**i*. If **A** has independent columns, its rank is 2. Then if and only if the rank of the augmented matrix [**A** | **b**] is also 2, there exists a solution of the matrix equation and thus an intersection point of the n lines. The intersection point, if it exists, is given by

$\mathbf {w} =\mathbf {A} ^{\mathrm {g} }\mathbf {b} =\left(\mathbf {A} ^{\mathsf {T}}\mathbf {A} \right)^{-1}\mathbf {A} ^{\mathsf {T}}\mathbf {b} ,$

where **A**g is the Moore–Penrose generalized inverse of **A** (which has the form shown because **A** has full column rank). Alternatively, the solution can be found by jointly solving any two independent equations. But if the rank of **A** is only 1, then if the rank of the augmented matrix is 2 there is no solution but if its rank is 1 then all of the lines coincide with each other.

### In three dimensions

The above approach can be readily extended to three dimensions. In three or more dimensions, even two lines almost certainly do not intersect; pairs of non-parallel lines that do not intersect are called skew lines. But if an intersection does exist it can be found, as follows.

In three dimensions a line is represented by the intersection of two planes, each of which has an equation of the form

${\begin{bmatrix}a_{i1}&a_{i2}&a_{i3}\end{bmatrix}}{\begin{bmatrix}x\\y\\z\end{bmatrix}}=b_{i}.$

Thus a set of n lines can be represented by 2*n* equations in the 3-dimensional coordinate vector **w**:

$\mathbf {A} \mathbf {w} =\mathbf {b}$

where now **A** is 2*n* × 3 and **b** is 2*n* × 1. As before there is a unique intersection point if and only if **A** has full column rank and the augmented matrix [**A** | **b**] does not, and the unique intersection if it exists is given by

$\mathbf {w} =\left(\mathbf {A} ^{\mathsf {T}}\mathbf {A} \right)^{-1}\mathbf {A} ^{\mathsf {T}}\mathbf {b} .$

## Nearest points to skew lines

In two or more dimensions, we can usually find a point that is mutually closest to two or more lines in a least-squares sense.

### In two dimensions

In the two-dimensional case, first, represent line i as a point **p***i* on the line and a unit normal vector **n̂***i*, perpendicular to that line. That is, if **x**1 and **x**2 are points on line 1, then let **p**1 = **x**1 and let

$\mathbf {\hat {n}} _{1}:={\begin{bmatrix}0&-1\\1&0\end{bmatrix}}{\frac {\mathbf {x} _{2}-\mathbf {x} _{1}}{\|\mathbf {x} _{2}-\mathbf {x} _{1}\|}}$

which is the unit vector along the line, rotated by a right angle.

The distance from a point **x** to the line (**p**, **n̂**) is given by

$d{\bigl (}\mathbf {x} ,(\mathbf {p} ,\mathbf {\hat {n}} ){\bigr )}={\bigl |}(\mathbf {x} -\mathbf {p} )\cdot \mathbf {\hat {n}} {\bigr |}=\left|(\mathbf {x} -\mathbf {p} )^{\mathsf {T}}\mathbf {\hat {n}} \right|=\left|\mathbf {\hat {n}} ^{\mathsf {T}}(\mathbf {x} -\mathbf {p} )\right|={\sqrt {(\mathbf {x} -\mathbf {p} )^{\mathsf {T}}\mathbf {\hat {n}} \mathbf {\hat {n}} ^{\mathsf {T}}(\mathbf {x} -\mathbf {p} )}}.$

And so the squared distance from a point **x** to a line is

$d{\bigl (}\mathbf {x} ,(\mathbf {p} ,\mathbf {\hat {n}} ){\bigr )}^{2}=(\mathbf {x} -\mathbf {p} )^{\mathsf {T}}\left(\mathbf {\hat {n}} \mathbf {\hat {n}} ^{\mathsf {T}}\right)(\mathbf {x} -\mathbf {p} ).$

The sum of squared distances to many lines is the cost function:

$E(\mathbf {x} )=\sum _{i}(\mathbf {x} -\mathbf {p} _{i})^{\mathsf {T}}\left(\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)(\mathbf {x} -\mathbf {p} _{i}).$

This can be rearranged:

${\begin{aligned}E(\mathbf {x} )&=\sum _{i}\mathbf {x} ^{\mathsf {T}}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {x} -\mathbf {x} ^{\mathsf {T}}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}-\mathbf {p} _{i}^{\mathsf {T}}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {x} +\mathbf {p} _{i}^{\mathsf {T}}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}\\&=\mathbf {x} ^{\mathsf {T}}\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\mathbf {x} -2\mathbf {x} ^{\mathsf {T}}\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}\right)+\sum _{i}\mathbf {p} _{i}^{\mathsf {T}}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}.\end{aligned}}$

To find the minimum, we differentiate with respect to **x** and set the result equal to the zero vector:

${\frac {\partial E(\mathbf {x} )}{\partial \mathbf {x} }}={\boldsymbol {0}}=2\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\mathbf {x} -2\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}\right)$

so

$\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\mathbf {x} =\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}$

and so

$\mathbf {x} =\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)^{-1}\left(\sum _{i}\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\mathbf {p} _{i}\right).$

### In more than two dimensions

While **n̂***i* is not well-defined in more than two dimensions, this can be generalized to any number of dimensions by noting that **n̂***i* **n̂***i*T is simply the symmetric matrix with all eigenvalues unity except for a zero eigenvalue in the direction along the line providing a seminorm on the distance between **p***i* and another point giving the distance to the line. In any number of dimensions, if **v̂***i* is a unit vector *along* the ith line, then

$\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}$

becomes

$\mathbf {I} -\mathbf {\hat {v}} _{i}\mathbf {\hat {v}} _{i}^{\mathsf {T}}$

where **I** is the identity matrix, and so

$x=\left(\sum _{i}\mathbf {I} -\mathbf {\hat {v}} _{i}\mathbf {\hat {v}} _{i}^{\mathsf {T}}\right)^{-1}\left(\sum _{i}\left(\mathbf {I} -\mathbf {\hat {v}} _{i}\mathbf {\hat {v}} _{i}^{\mathsf {T}}\right)\mathbf {p} _{i}\right).$

### General derivation

In order to find the intersection point of a set of lines, we calculate the point with minimum distance to them. Each line is defined by an origin **a***i* and a unit direction vector **n̂***i*. The square of the distance from a point **p** to one of the lines is given from Pythagoras:

$d_{i}^{2}=\left\|\mathbf {p} -\mathbf {a} _{i}\right\|^{2}-\left(\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}\mathbf {\hat {n}} _{i}\right)^{2}=\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}\left(\mathbf {p} -\mathbf {a} _{i}\right)-\left(\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}\mathbf {\hat {n}} _{i}\right)^{2}$

where (**p** − **a***i*)T **n̂***i* is the projection of **p** − **a***i* on line i. The sum of distances to the square to all lines is

$\sum _{i}d_{i}^{2}=\sum _{i}\left({\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}}\left(\mathbf {p} -\mathbf {a} _{i}\right)-{\left(\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}\mathbf {\hat {n}} _{i}\right)^{2}}\right)$

To minimize this expression, we differentiate it with respect to **p**.

$\sum _{i}\left(2\left(\mathbf {p} -\mathbf {a} _{i}\right)-2\left(\left(\mathbf {p} -\mathbf {a} _{i}\right)^{\mathsf {T}}\mathbf {\hat {n}} _{i}\right)\mathbf {\hat {n}} _{i}\right)={\boldsymbol {0}}$

$\sum _{i}\left(\mathbf {p} -\mathbf {a} _{i}\right)=\sum _{i}\left(\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\left(\mathbf {p} -\mathbf {a} _{i}\right)$

which results in

$\left(\sum _{i}\left(\mathbf {I} -\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\right)\mathbf {p} =\sum _{i}\left(\mathbf {I} -\mathbf {\hat {n}} _{i}\mathbf {\hat {n}} _{i}^{\mathsf {T}}\right)\mathbf {a} _{i}$

where **I** is the identity matrix. This is a matrix **Sp** = **C**, with solution **p** = **S**+**C**, where **S**+ is the pseudo-inverse of **S**.

## Non-Euclidean geometry

In spherical geometry, lines are represented by great circles, defined as the intersections of a sphere $S^{2}=\{x\in \mathbb {R} ^{3}:\|x\|=R\}$ with planes through the origin.

Two great circles lying in planes with unit normal vectors $\mathbf {\hat {n}} _{1}$ and $\mathbf {\hat {n}} _{2}$ intersect at two antipodal points, which (up to normalization) can be expressed by

$\mathbf {x} =\pm {\frac {\mathbf {n} _{1}\times \mathbf {n} _{2}}{\|\mathbf {n} _{1}\times \mathbf {n} _{2}\|}}$

Every pair of lines intersects in two antipodal points, so there are no parallel lines in spherical geometry.

In elliptic geometry, the space may be regarded as a quotient of spherical geometry in which antipodal points are identified. Lines in this geometry correspond to great circles with antipodal points considered equivalent, so each pair of lines intersects in exactly one point. Unlike spherical geometry, this identification eliminates the distinction between the two intersection points, producing a finite but unbounded space without parallel lines.

In hyperbolic geometry, line–line intersection behavior differs from that of Euclidean and positively curved geometries. Given a line $\ell$ and a point $P\not \in \ell$ , there exist infinitely many distinct lines through P that do not intersect $\ell$ . Two lines may intersect in exactly one point, be asymptotically parallel, or be ultraparallel (disjoint with a common perpendicular). This behavior reflects the constant negative Gaussian curvature $K<0$ of hyperbolic space and the failure of the Euclidean parallel postulate. Line–line intersection is therefore not guaranteed and depends on the incidence relations of the geometry rather than on metric distance alone.

In projective geometry, any two distinct lines intersect in exactly one point by construction. This is achieved by adjoining ideal points (points at infinity), so that parallel lines in Euclidean geometry meet at a single projective point. Lines are modeled as one-dimensional projective subspaces, and incidence relations are fundamental, while notions of distance, angle, and curvature are not. Projective geometry thus provides a unifying framework in which Euclidean, elliptic, and hyperbolic geometries can be studied via appropriate projective models.

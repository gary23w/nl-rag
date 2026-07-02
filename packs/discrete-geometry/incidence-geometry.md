---
title: "Incidence (geometry)"
source: https://en.wikipedia.org/wiki/Incidence_(geometry)
domain: discrete-geometry
license: CC-BY-SA-4.0
tags: discrete geometry, sphere packing, kissing number, geometric lattice
fetched: 2026-07-02
---

# Incidence (geometry)

In geometry, an **incidence** relation is a heterogeneous relation that captures the idea being expressed when phrases such as "a point *lies on* a line" or "a line is *contained in* a plane" are used. The most basic incidence relation is that between a point, *P*, and a line, *l*, sometimes denoted *P* I *l*. If *P* and *l* are incident, *P* I *l*, the pair (*P*, *l*) is called a *flag*.

There are many expressions used in common language to describe incidence (for example, a line *passes through* a point, a point *lies in* a plane, etc.) but the term "incidence" is preferred because it does not have the additional connotations that these other terms have, and it can be used in a symmetric manner. Statements such as "line *l*1 intersects line *l*2" are also statements about incidence relations, but in this case, it is because this is a shorthand way of saying that "there exists a point *P* that is incident with both line *l*1 and line *l*2". When one type of object can be thought of as a set of the other type of object (*viz*., a plane is a set of points) then an incidence relation may be viewed as containment.

Statements such as "any two lines in a plane meet" are called *incidence propositions*. This particular statement is true in a projective plane, though not true in the Euclidean plane where lines may be parallel. Historically, projective geometry was developed in order to make the propositions of incidence true without exceptions, such as those caused by the existence of parallels. From the point of view of synthetic geometry, projective geometry *should be* developed using such propositions as axioms. This is most significant for projective planes due to the universal validity of Desargues' theorem in higher dimensions.

In contrast, the analytic approach is to define projective space based on linear algebra and utilizing homogeneous co-ordinates. The propositions of incidence are derived from the following basic result on vector spaces: given subspaces *U* and *W* of a (finite-dimensional) vector space *V*, the dimension of their intersection is dim *U* + dim *W* − dim (*U* + *W*). Bearing in mind that the geometric dimension of the projective space **P**(*V*) associated to *V* is dim *V* − 1 and that the geometric dimension of any subspace is positive, the basic proposition of incidence in this setting can take the form: linear subspaces *L* and *M* of projective space *P* meet provided dim *L* + dim *M* ≥ dim *P*.

The following sections are limited to projective planes defined over fields, often denoted by PG(2, *F*), where *F* is a field, or **P**2*F*. However these computations can be naturally extended to higher-dimensional projective spaces, and the field may be replaced by a division ring (or skewfield) provided that one pays attention to the fact that multiplication is not commutative in that case.

## PG(2,*F*)

Let *V* be the three-dimensional vector space defined over the field *F*. The projective plane **P**(*V*) = PG(2, *F*) consists of the one-dimensional vector subspaces of *V*, called *points*, and the two-dimensional vector subspaces of *V*, called *lines*. Incidence of a point and a line is given by containment of the one-dimensional subspace in the two-dimensional subspace.

Fix a basis for *V* so that we may describe its vectors as coordinate triples (with respect to that basis). A one-dimensional vector subspace consists of a non-zero vector and all of its scalar multiples. The non-zero scalar multiples, written as coordinate triples, are the homogeneous coordinates of the given point, called *point coordinates*. With respect to this basis, the solution space of a single linear equation {(*x*, *y*, *z*) | *ax* + *by* + *cz* = 0} is a two-dimensional subspace of *V*, and hence a line of **P**(*V*). This line may be denoted by *line coordinates* [*a*, *b*, *c*], which are also homogeneous coordinates since non-zero scalar multiples would give the same line. Other notations are also widely used. Point coordinates may be written as column vectors, (*x*, *y*, *z*)T, with colons, (*x* : *y* : *z*), or with a subscript, (*x*, *y*, *z*)P. Correspondingly, line coordinates may be written as row vectors, (*a*, *b*, *c*), with colons, [*a* : *b* : *c*] or with a subscript, (*a*, *b*, *c*)L. Other variations are also possible.

## Incidence expressed algebraically

Given a point *P* = (*x*, *y*, *z*) and a line *l* = [*a*, *b*, *c*], written in terms of point and line coordinates, the point is incident with the line (often written as *P* I *l*), if and only if,

ax

+

by

+

cz

= 0

.

This can be expressed in other notations as:

$ax+by+cz=[a,b,c]\cdot (x,y,z)=(a,b,c)_{L}\cdot (x,y,z)_{P}=$

$=[a:b:c]\cdot (x:y:z)=(a,b,c)\left({\begin{matrix}x\\y\\z\end{matrix}}\right)=0.$

No matter what notation is employed, when the homogeneous coordinates of the point and line are just considered as ordered triples, their incidence is expressed as having their dot product equal 0.

## The line incident with a pair of distinct points

Let *P*1 and *P*2 be a pair of distinct points with homogeneous coordinates (*x*1, *y*1, *z*1) and (*x*2, *y*2, *z*2) respectively. These points determine a unique line *l* with an equation of the form *ax* + *by* + *cz* = 0 and must satisfy the equations:

ax

1

+

by

1

+

cz

1

= 0

and

ax

2

+

by

2

+

cz

2

= 0

.

In matrix form this system of simultaneous linear equations can be expressed as:

$\left({\begin{matrix}x&y&z\\x_{1}&y_{1}&z_{1}\\x_{2}&y_{2}&z_{2}\end{matrix}}\right)\left({\begin{matrix}a\\b\\c\end{matrix}}\right)=\left({\begin{matrix}0\\0\\0\end{matrix}}\right).$

This system has a nontrivial solution if and only if the determinant,

$\left|{\begin{matrix}x&y&z\\x_{1}&y_{1}&z_{1}\\x_{2}&y_{2}&z_{2}\end{matrix}}\right|=0.$

Expansion of this determinantal equation produces a homogeneous linear equation, which must be the equation of line *l*. Therefore, up to a common non-zero constant factor we have *l* = [*a*, *b*, *c*] where:

a

=

y

1

z

2

-

y

2

z

1

,

b

=

x

2

z

1

-

x

1

z

2

, and

c

=

x

1

y

2

-

x

2

y

1

.

In terms of the scalar triple product notation for vectors, the equation of this line may be written as:

P

⋅

P

1

×

P

2

= 0

,

where *P* = (*x*, *y*, *z*) is a generic point.

### Collinearity

Points that are incident with the same line are said to be *collinear*. The set of all points incident with the same line is called a range.

If *P*1 = (*x*1, *y*1, *z*1), *P*2 = (*x*2, *y*2, *z*2), and *P*3 = (*x*3, *y*3, *z*3), then these points are collinear if and only if

$\left|{\begin{matrix}x_{1}&y_{1}&z_{1}\\x_{2}&y_{2}&z_{2}\\x_{3}&y_{3}&z_{3}\end{matrix}}\right|=0,$

i.e., if and only if the determinant of the homogeneous coordinates of the points is equal to zero.

For more than 3 points this can be generalized as a rank test: $P_{1},...,P_{n}$ with the homogenous coordinates $(x_{1},y_{1},z_{1}),...,(x_{n},y_{n},z_{n})$ are collinear if and only if

> $\operatorname {rank} {\begin{pmatrix}x_{1}&y_{1}&z_{1}\\\vdots &\vdots &\vdots \\x_{n}&y_{n}&z_{n}\end{pmatrix}}<3$ .

According to the Gram determinant test, whether the matrix P above has less than full rank is equivalent to $\det(P^{\mathsf {T}}P)=0$ .

## Intersection of a pair of lines

Let *l*1 = [*a*1, *b*1, *c*1] and *l*2 = [*a*2, *b*2, *c*2] be a pair of distinct lines. Then the intersection of lines *l*1 and *l*2 is point a *P* = (*x*0, *y*0, *z*0) that is the simultaneous solution (up to a scalar factor) of the system of linear equations:

a

1

x

+

b

1

y

+

c

1

z

= 0

and

a

2

x

+

b

2

y

+

c

2

z

= 0

.

The solution of this system gives:

x

0

=

b

1

c

2

-

b

2

c

1

,

y

0

=

a

2

c

1

-

a

1

c

2

, and

z

0

=

a

1

b

2

-

a

2

b

1

.

Alternatively, consider another line *l* = [*a*, *b*, *c*] passing through the point *P*, that is, the homogeneous coordinates of *P* satisfy the equation:

ax

+

by

+

cz

= 0

.

Combining this equation with the two that define *P*, we can seek a non-trivial solution of the matrix equation:

$\left({\begin{matrix}a&b&c\\a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\end{matrix}}\right)\left({\begin{matrix}x\\y\\z\end{matrix}}\right)=\left({\begin{matrix}0\\0\\0\end{matrix}}\right).$

Such a solution exists provided the determinant,

$\left|{\begin{matrix}a&b&c\\a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\end{matrix}}\right|=0.$

The coefficients of *a*, *b* and *c* in this equation give the homogeneous coordinates of *P*.

The equation of the generic line passing through the point *P* in scalar triple product notation is:

l

⋅

l

1

×

l

2

= 0

.

### Concurrence

Lines that meet at the same point are said to be *concurrent*. The set of all lines in a plane incident with the same point is called a *pencil of lines* centered at that point. The computation of the intersection of two lines shows that the entire pencil of lines centered at a point is determined by any two of the lines that intersect at that point. It immediately follows that the algebraic condition for three lines, [*a*1, *b*1, *c*1], [*a*2, *b*2, *c*2], [*a*3, *b*3, *c*3] to be concurrent is that the determinant,

$\left|{\begin{matrix}a_{1}&b_{1}&c_{1}\\a_{2}&b_{2}&c_{2}\\a_{3}&b_{3}&c_{3}\end{matrix}}\right|=0.$

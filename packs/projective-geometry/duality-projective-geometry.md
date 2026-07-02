---
title: "Duality (projective geometry)"
source: https://en.wikipedia.org/wiki/Duality_(projective_geometry)
domain: projective-geometry
license: CC-BY-SA-4.0
tags: projective geometry, projective plane, homogeneous coordinates, desargues theorem
fetched: 2026-07-02
---

# Duality (projective geometry)

In projective geometry, **duality** or **plane duality** is a formalization of the striking symmetry of the roles played by points and lines in the definitions and theorems of projective planes. There are two approaches to the subject of duality, one through language (§ Principle of duality) and the other a more functional approach through special mappings. These are completely equivalent and either treatment has as its starting point the axiomatic version of the geometries under consideration. In the functional approach there is a map between related geometries that is called a ***duality***. Such a map can be constructed in many ways. The concept of plane duality readily extends to *space duality* and beyond that to duality in any finite-dimensional projective geometry.

## Principle of duality

A projective plane *C* may be defined axiomatically as an incidence structure, in terms of a set *P* of *points*, a set *L* of *lines*, and an incidence relation I that determines which points lie on which lines. These sets can be used to define a **plane dual structure**.

Interchange the role of "points" and "lines" in

C

= (

P

,

L

, I)

to obtain the *dual structure*

C

∗

= (

L

,

P

, I

∗

)

,

where I∗ is the converse relation of I. *C*∗ is also a projective plane, called the **dual plane** of *C*.

If *C* and *C*∗ are isomorphic, then *C* is called ***self-dual***. The projective planes PG(2, *K*) for any field (or, more generally, for every division ring (skewfield) isomorphic to its dual) *K* are self-dual. In particular, Desarguesian planes of finite order are always self-dual. However, there are non-Desarguesian planes which are not self-dual, such as the Hall planes and some that are, such as the Hughes planes.

In a projective plane a statement involving points, lines and incidence between them that is obtained from another such statement by interchanging the words "point" and "line" and making whatever grammatical adjustments that are necessary, is called the **plane dual statement** of the first. The plane dual statement of "Two points are on a unique line" is "Two lines meet at a unique point". Forming the plane dual of a statement is known as *dualizing* the statement.

If a statement is true in a projective plane *C*, then the plane dual of that statement must be true in the dual plane *C*∗. This follows since dualizing each statement in the proof "in *C*" gives a corresponding statement of the proof "in *C*∗".

The ***principle of plane duality*** says that dualizing any theorem in a self-dual projective plane *C* produces another theorem valid in *C*.

The above concepts can be generalized to talk about space duality, where the terms "points" and "planes" are interchanged (and lines remain lines). This leads to the *principle of space duality*.

These principles provide a good reason for preferring to use a "symmetric" term for the incidence relation. Thus instead of saying "a point lies on a line" one should say "a point is incident with a line" since dualizing the latter only involves interchanging point and line ("a line is incident with a point").

The validity of the principle of plane duality follows from the axiomatic definition of a projective plane. The three axioms of this definition can be written so that they are self-dual statements implying that the dual of a projective plane is also a projective plane. The dual of a true statement in a projective plane is therefore a true statement in the dual projective plane and the implication is that for self-dual planes, the dual of a true statement in that plane is also a true statement in that plane.

### Dual theorems

As the real projective plane, PG(2, **R**), is self-dual there are a number of pairs of well known results that are duals of each other. Some of these are:

- Desargues' theorem ⇔ Converse of Desargues' theorem
- Pascal's theorem ⇔ Brianchon's theorem
- Menelaus' theorem ⇔ Ceva's theorem

### Dual configurations

Not only statements, but also systems of points and lines can be dualized.

A set of *m* points and *n* lines is called an (*m**c*, *n**d*) *configuration* if *c* of the *n* lines pass through each point and *d* of the *m* points lie on each line. The dual of an (*m**c*, *n**d*) configuration, is an (*n**d*, *m**c*) configuration. Thus, the dual of a quadrangle, a (43, 62) configuration of four points and six lines, is a quadrilateral, a (62, 43) configuration of six points and four lines.

The set of all points on a line, called a projective range, has as its dual a pencil of lines, the set of all lines on a point, in two dimensions, or a pencil of hyperplanes in higher dimensions. A line segment on a projective line has as its dual the shape swept out by these lines or hyperplanes, a double wedge.

## Duality as a mapping

### Plane dualities

A **plane duality** is a map from a projective plane *C* = (*P*, *L*, I) to its *dual plane* *C*∗ = (*L*, *P*, I∗) (see § Principle of duality above) which preserves incidence. That is, a plane duality *σ* will map points to lines and lines to points (*P**σ* = *L* and *L**σ* = *P*) in such a way that if a point *Q* is on a line *m* (denoted by *Q* I *m*) then *Q* I *m* ⇔ *m**σ* I∗*Q**σ*. A plane duality which is an isomorphism is called a *correlation*. The existence of a correlation means that the projective plane *C* is *self-dual*.

The projective plane *C* in this definition need not be a Desarguesian plane. However, if it is, that is, *C* = PG(2, *K*) with *K* a division ring (skewfield), then a duality, as defined below for general projective spaces, gives a plane duality on *C* that satisfies the above definition.

### In general projective spaces

A duality *δ* of a projective space is a permutation of the subspaces of PG(*n*, *K*) (also denoted by *K***P***n*) with *K* a field (or more generally a skewfield (division ring)) that reverses inclusion, that is:

S

⊆

T

implies

S

δ

⊇

T

δ

for all subspaces

S

,

T

of

PG(

n

,

K

)

.

Consequently, a duality interchanges objects of dimension *r* with objects of dimension *n* − 1 − *r* ( = codimension *r* + 1). That is, in a projective space of dimension *n*, the points (dimension 0) correspond to hyperplanes (codimension 1), the lines joining two points (dimension 1) correspond to the intersection of two hyperplanes (codimension 2), and so on.

#### Classification of dualities

The *dual* *V*∗ of a finite-dimensional (right) vector space *V* over a skewfield *K* can be regarded as a (right) vector space of the same dimension over the opposite skewfield *K*o. There is thus an inclusion-reversing bijection between the projective spaces PG(*n*, *K*) and PG(*n*, *K*o). If *K* and *K*o are isomorphic then there exists a duality on PG(*n*, *K*). Conversely, if PG(*n*, *K*) admits a duality for *n* > 1, then *K* and *K*o are isomorphic.

Let π be a duality of PG(*n*, *K*) for *n* > 1. If π is composed with the natural isomorphism between PG(*n*, *K*) and PG(*n*, *K*o), the composition *θ* is an incidence preserving bijection between PG(*n*, *K*) and PG(*n*, *K*o). By the Fundamental theorem of projective geometry *θ* is induced by a semilinear map *T*: *V* → *V*∗ with associated isomorphism *σ*: *K* → *K*o, which can be viewed as an antiautomorphism of *K*. In the classical literature, π would be called a **reciprocity** in general, and if *σ* = id it would be called a **correlation** (and *K* would necessarily be a field). Some authors suppress the role of the natural isomorphism and call *θ* a duality. When this is done, a duality may be thought of as a collineation between a pair of specially related projective spaces and called a reciprocity. If this collineation is a projectivity then it is called a correlation.

Let *T**w* = *T*(*w*) denote the linear functional of *V*∗ associated with the vector *w* in *V*. Define the form *φ*: *V* × *V* → *K* by:

$\varphi (v,w)=T_{w}(v).$

*φ* is a nondegenerate sesquilinear form with companion antiautomorphism *σ*.

Any duality of PG(*n*, *K*) for *n* > 1 is induced by a nondegenerate sesquilinear form on the underlying vector space (with a companion antiautomorphism) and conversely.

## Homogeneous coordinate formulation

Homogeneous coordinates may be used to give an algebraic description of dualities. To simplify this discussion we shall assume that *K* is a field, but everything can be done in the same way when *K* is a skewfield as long as attention is paid to the fact that multiplication need not be a commutative operation.

The points of PG(*n*, *K*) can be taken to be the nonzero vectors in the (*n* + 1)-dimensional vector space over *K*, where we identify two vectors which differ by a scalar factor. Another way to put it is that the points of *n*-dimensional projective space are the 1-dimensional vector subspaces, which may be visualized as the lines through the origin in *K**n*+1. Also the *n*- (vector) dimensional subspaces of *K**n*+1 represent the (*n* − 1)- (geometric) dimensional hyperplanes of projective *n*-space over *K*, i.e., PG(*n*, *K*).

A nonzero vector **u** = (*u*0, *u*1, ..., *un*) in *K**n*+1 also determines an (*n* − 1) - geometric dimensional subspace (hyperplane) H**u**, by

H

u

= {(

x

0

,

x

1

, ...,

x

n

) :

u

0

x

0

+ ... +

u

n

x

n

= 0}

.

When a vector **u** is used to define a hyperplane in this way it shall be denoted by **u**H, while if it is designating a point we will use **u**P. They are referred to as *point coordinates* or *hyperplane coordinates* respectively (in the important two-dimensional case, hyperplane coordinates are called *line coordinates*). Some authors distinguish how a vector is to be interpreted by writing hyperplane coordinates as horizontal (row) vectors while point coordinates are written as vertical (column) vectors. Thus, if **u** is a column vector we would have **u**P = **u** while **u**H = **u**T. In terms of the usual dot product, H**u** = {**x**P : **u**H ⋅ **x**P = 0}. Since *K* is a field, the dot product is symmetrical, meaning **u**H ⋅ **x**P = *u*0*x*0 + *u*1*x*1 + ... + *unxn* = *x*0*u*0 + *x*1*u*1 + ... + *xnun* = **x**H ⋅ **u**P.

### A fundamental example

A simple reciprocity (actually a correlation) can be given by **u**P ↔ **u**H between points and hyperplanes. This extends to a reciprocity between the line generated by two points and the intersection of two such hyperplanes, and so forth.

Specifically, in the projective plane, PG(2, *K*), with *K* a field, we have the correlation given by: points in homogeneous coordinates (*a*, *b*, *c*) ↔ lines with equations *ax* + *by* + *cz* = *0*. In a projective space, PG(3, *K*), a correlation is given by: points in homogeneous coordinates (*a*, *b*, *c*, *d*) ↔ planes with equations *ax* + *by* + *cz* + *dw* = 0. This correlation would also map a line determined by two points (*a*1, *b*1, *c*1, *d*1) and (*a*2, *b*2, *c*2, *d*2) to the line which is the intersection of the two planes with equations *a*1*x* + *b*1*y* + *c*1*z* + *d*1*w* = 0 and *a*2*x* + *b*2*y* + *c*2*z* + *d*2*w* = 0.

The associated sesquilinear form for this correlation is:

φ

(

u

,

x

) =

u

H

⋅

x

P

=

u

0

x

0

+

u

1

x

1

+ ... +

u

n

x

n

,

where the companion antiautomorphism *σ* = id. This is therefore a bilinear form (note that *K* must be a field). This can be written in matrix form (with respect to the standard basis) as:

φ

(

u

,

x

) =

u

H

G

x

P

,

where *G* is the (*n* + 1) × (*n* + 1) identity matrix, using the convention that **u**H is a row vector and **x**P is a column vector.

The correlation is given by:

$\pi (\mathbf {x} _{P})=(G\mathbf {x} _{P})^{\mathsf {T}}=(\mathbf {x} _{P})^{\mathsf {T}}=\mathbf {x} _{H}.$

#### Geometric interpretation in the real projective plane

This correlation in the case of PG(2, **R**) can be described geometrically using the model of the real projective plane which is a "unit sphere with antipodes identified", or equivalently, the model of lines and planes through the origin of the vector space **R**3. Associate to any line through the origin the unique plane through the origin which is perpendicular (orthogonal) to the line. When, in the model, these lines are considered to be the points and the planes the lines of the projective plane PG(2, **R**), this association becomes a correlation (actually a polarity) of the projective plane. The sphere model is obtained by intersecting the lines and planes through the origin with a unit sphere centered at the origin. The lines meet the sphere in antipodal points which must then be identified to obtain a point of the projective plane, and the planes meet the sphere in great circles which are thus the lines of the projective plane.

That this association "preserves" incidence is most easily seen from the lines and planes model. A point incident with a line in the projective plane corresponds to a line through the origin lying in a plane through the origin in the model. Applying the association, the plane becomes a line through the origin perpendicular to the plane it is associated with. This image line is perpendicular to every line of the plane which passes through the origin, in particular the original line (point of the projective plane). All lines that are perpendicular to the original line at the origin lie in the unique plane which is orthogonal to the original line, that is, the image plane under the association. Thus, the image line lies in the image plane and the association preserves incidence.

### Matrix form

As in the above example, matrices can be used to represent dualities. Let π be a duality of PG(*n*, *K*) for *n* > 1 and let *φ* be the associated sesquilinear form (with companion antiautomorphism *σ*) on the underlying (*n* + 1)-dimensional vector space *V*. Given a basis { *e*i } of *V*, we may represent this form by:

$\varphi (\mathbf {u} ,\mathbf {x} )=\mathbf {u} ^{\mathsf {T}}G(\mathbf {x} ^{\sigma }),$

where *G* is a nonsingular (*n* + 1) × (*n* + 1) matrix over *K* and the vectors are written as column vectors. The notation **x***σ* means that the antiautomorphism *σ* is applied to each coordinate of the vector **x**.

Now define the duality in terms of point coordinates by:

$\pi (\mathbf {x} )=(G(\mathbf {x} ^{\sigma }))^{\mathsf {T}}.$

## Polarity

A duality that is an involution (has order two) is called a **polarity**. It is necessary to distinguish between polarities of general projective spaces and those that arise from the slightly more general definition of plane duality. It is also possible to give more precise statements in the case of a finite geometry, so we shall emphasize the results in finite projective planes.

### Polarities of general projective spaces

If π is a duality of PG(*n*, *K*), with *K* a skewfield, then a common notation is defined by π(*S*) = *S*⊥ for a subspace *S* of PG(*n*, *K*). Hence, a polarity is a duality for which *S*⊥⊥ = *S* for every subspace *S* of PG(*n*, *K*). It is also common to bypass mentioning the dual space and write, in terms of the associated sesquilinear form:

$S^{\bot }=\{\mathbf {u} {\text{ in }}V\colon \varphi (\mathbf {u} ,\mathbf {x} )=0{\text{ for all }}\mathbf {x} {\text{ in }}S\}.$

A sesquilinear form *φ* is *reflexive* if *φ*(**u**, **x**) = 0 implies *φ*(**x**, **u**) = 0.

A duality is a polarity if and only if the (nondegenerate) sesquilinear form defining it is reflexive.

Polarities have been classified, a result of Birkhoff & von Neumann (1936) that has been reproven several times. Let *V* be a (left) vector space over the skewfield *K* and *φ* be a reflexive nondegenerate sesquilinear form on *V* with companion anti-automorphism *σ*. If *φ* is the sesquilinear form associated with a polarity then either:

1. *σ* = id (hence, *K* is a field) and *φ*(**u**, **x**) = *φ*(**x**, **u**) for all **u**, **x** in *V*, that is, *φ* is a bilinear form. In this case, the polarity is called **orthogonal** (or **ordinary**). If the characteristic of the field *K* is two, then to be in this case there must exist a vector **z** with *φ*(**z**, **z**) ≠ 0, and the polarity is called a **pseudo polarity**.
2. *σ* = id (hence, *K* is a field) and *φ*(**u**, **u**) = 0 for all **u** in *V*. The polarity is called a **null polarity** (or a **symplectic polarity**) and can only exist when the projective dimension *n* is odd.
3. *σ*2 = id ≠ *σ* (here *K* need not be a field) and *φ*(**u**, **x**) = *φ*(**x**, **u**)*σ* for all **u**, **x** in *V*. Such a polarity is called a **unitary polarity** (or a **Hermitian polarity**).

A point *P* of PG(*n*, *K*) is an **absolute point** (self-conjugate point) with respect to polarity ⊥ if *P* I *P*⊥. Similarly, a hyperplane *H* is an **absolute hyperplane** (self-conjugate hyperplane) if *H*⊥ I *H*. Expressed in other terms, a point **x** is an absolute point of polarity π with associated sesquilinear form *φ* if *φ*(**x**, **x**) = 0 and if *φ* is written in terms of matrix *G*, **x**T *G* **x***σ* = 0.

The set of absolute points of each type of polarity can be described. We again restrict the discussion to the case that *K* is a field.

1. If *K* is a field whose characteristic is not two, the set of absolute points of an orthogonal polarity form a nonsingular quadric (if *K* is infinite, this might be empty). If the characteristic is two, the absolute points of a pseudo polarity form a hyperplane.
2. All the points of the space PG(2*s* + 1, *K*) are absolute points of a null polarity.
3. The absolute points of a Hermitian polarity form a Hermitian variety, which may be empty if *K* is infinite.

When composed with itself, the correlation *φ*(**x**P) = **x**H (in any dimension) produces the identity function, so it is a polarity. The set of absolute points of this polarity would be the points whose homogeneous coordinates satisfy the equation:

x

H

⋅

x

P

=

x

0

x

0

+

x

1

x

1

+ ... +

x

n

x

n

=

x

0

2

+

x

1

2

+ ... +

x

n

2

= 0

.

Which points are in this point set depends on the field *K*. If *K* = **R** then the set is empty, there are no absolute points (and no absolute hyperplanes). On the other hand, if *K* = **C** the set of absolute points form a nondegenerate quadric (a conic in two-dimensional space). If *K* is a finite field of odd characteristic the absolute points also form a quadric, but if the characteristic is even the absolute points form a hyperplane (this is an example of a pseudo polarity).

Under any duality, the point *P* is called the **pole** of the hyperplane *P*⊥, and this hyperplane is called the **polar** of the point *P*. Using this terminology, the absolute points of a polarity are the points that are incident with their polars and the absolute hyperplanes are the hyperplanes that are incident with their poles.

### Polarities in finite projective planes

By Wedderburn's theorem every finite skewfield is a field and an automorphism of order two (other than the identity) can only exist in a finite field whose order is a square. These facts help to simplify the general situation for finite Desarguesian planes. We have:

If π is a polarity of the finite Desarguesian projective plane PG(2, *q*) where *q* = *p**e* for some prime *p*, then the number of absolute points of π is *q* + 1 if π is orthogonal or *q*3/2 + 1 if π is unitary. In the orthogonal case, the absolute points lie on a conic if *p* is odd or form a line if *p* = 2. The unitary case can only occur if *q* is a square; the absolute points and absolute lines form a unital.

In the general projective plane case where duality means *plane duality*, the definitions of polarity, absolute elements, pole and polar remain the same.

Let **P** denote a projective plane of order *n*. Counting arguments can establish that for a polarity π of **P**:

The number of non-absolute points (lines) incident with a non-absolute line (point) is even.

Furthermore,

The polarity π has at least *n* + 1 absolute points and if *n* is not a square, exactly *n* + 1 absolute points. If π has exactly *n* + 1 absolute points then;

1. if *n* is odd, the absolute points form an oval whose tangents are the absolute lines; or
2. if *n* is even, the absolute points are collinear on a non-absolute line.

An upper bound on the number of absolute points in the case that *n* is a square was given by Seib and a purely combinatorial argument can establish:

A polarity π in a projective plane of square order *n* = *s*2 has at most *s*3 + 1 absolute points. Furthermore, if the number of absolute points is *s*3 + 1, then the absolute points and absolute lines form a unital (i.e., every line of the plane meets this set of absolute points in either 1 or *s* + 1 points).

## Poles and polars

### Reciprocation in the Euclidean plane

A method that can be used to construct a polarity of the real projective plane has, as its starting point, a construction of a partial duality in the Euclidean plane.

In the Euclidean plane, fix a circle *C* with center *O* and radius *r*. For each point *P* other than *O* define an image point *Q* so that *OP* ⋅ *OQ* = *r*2. The mapping defined by *P* → *Q* is called **inversion** with respect to circle *C*. The line *p* through *Q* which is perpendicular to the line *OP* is called the **polar** of the point *P* with respect to circle *C*.

Let *q* be a line not passing through *O*. Drop a perpendicular from *O* to *q*, meeting *q* at the point *P* (this is the point of *q* that is closest to *O*). The image *Q* of *P* under inversion with respect to *C* is called the **pole** of *q*. If a point *M* is on a line *q* (not passing through *O*) then the pole of *q* lies on the polar of *M* and vice versa. The incidence preserving process, in which points and lines are transformed into their polars and poles with respect to *C* is called **reciprocation**.

In order to turn this process into a correlation, the Euclidean plane (which is not a projective plane) needs to be expanded to the extended euclidean plane by adding a line at infinity and points at infinity which lie on this line. In this expanded plane, we define the polar of the point *O* to be the line at infinity (and *O* is the pole of the line at infinity), and the poles of the lines through *O* are the points of infinity where, if a line has slope *s* (≠ 0) its pole is the infinite point associated to the parallel class of lines with slope −1/*s*. The pole of the *x*-axis is the point of infinity of the vertical lines and the pole of the *y*-axis is the point of infinity of the horizontal lines.

The construction of a correlation based on inversion in a circle given above can be generalized by using inversion in a conic section (in the extended real plane). The correlations constructed in this manner are of order two, that is, polarities.

#### Algebraic formulation

We shall describe this polarity algebraically by following the above construction in the case that *C* is the unit circle (i.e., *r* = 1) centered at the origin.

An affine point *P*, other than the origin, with Cartesian coordinates (*a*, *b*) has as its inverse in the unit circle the point *Q* with coordinates,

$\left({\frac {a}{a^{2}+b^{2}}},{\frac {b}{a^{2}+b^{2}}}\right).$

The line passing through *Q* that is perpendicular to the line *OP* has equation *ax* + *by* = 1.

Switching to homogeneous coordinates using the embedding (*a*, *b*) ↦ (*a*, *b*, 1), the extension to the real projective plane is obtained by permitting the last coordinate to be 0. Recalling that point coordinates are written as column vectors and line coordinates as row vectors, we may express this polarity by:

$\pi :\mathbb {R} P^{2}\rightarrow \mathbb {R} P^{2}$

such that

$\pi \left((x,y,z)^{\mathsf {T}}\right)=(x,y,-z).$

Or, using the alternate notation, π((*x*, *y*, *z*)P) = (*x*, *y*, −*z*)L. The matrix of the associated sesquilinear form (with respect to the standard basis) is:

$G=\left({\begin{matrix}1&0&0\\0&1&0\\0&0&-1\end{matrix}}\right).$

The absolute points of this polarity are given by the solutions of:

$0=P^{\mathsf {T}}GP=x^{2}+y^{2}-z^{2},$

where ***P***T= (*x*, *y*, *z*). Note that restricted to the Euclidean plane (that is, set *z* = 1) this is just the unit circle, the circle of inversion.

### Synthetic approach

The theory of poles and polars of a conic in a projective plane can be developed without the use of coordinates and other metric concepts.

Let *C* be a conic in PG(2, *F*) where *F* is a field not of characteristic two, and let *P* be a point of this plane not on *C*. Two distinct secant lines to the conic, say *AB* and *JK* determine four points on the conic (*A*, *B*, *J*, *K*) that form a quadrangle. The point *P* is a vertex of the diagonal triangle of this quadrangle. The *polar* of *P* with respect to *C* is the side of the diagonal triangle opposite *P*.

The theory of projective harmonic conjugates of points on a line can also be used to define this relationship. Using the same notation as above;

If a variable line through the point *P* is a secant of the conic *C*, the harmonic conjugates of *P* with respect to the two points of *C* on the secant all lie on the *polar* of *P*.

### Properties

There are several properties that polarities in a projective plane have.

Given a polarity π, a point *P* lies on line *q*, the polar of point *Q* if and only if *Q* lies on *p*, the polar of *P*.

Points *P* and *Q* that are in this relation are called **conjugate** points with respect to π. Absolute points are called **self-conjugate** in keeping with this definition since they are incident with their own polars. Conjugate lines are defined dually.

The line joining two self-conjugate points cannot be a self-conjugate line.

A line cannot contain more than two self-conjugate points.

A polarity induces an involution of conjugate points on any line that is not self-conjugate.

A triangle in which each vertex is the pole of the opposite side is called a **self-polar** triangle.

A correlation that maps the three vertices of a triangle to their opposite sides respectively is a polarity and this triangle is self-polar with respect to this polarity.

## History

The principle of duality is due to Joseph Diaz Gergonne (1771−1859) a champion of the then emerging field of Analytic geometry and founder and editor of the first journal devoted entirely to mathematics, *Annales de mathématiques pures et appliquées*. Gergonne and Charles Julien Brianchon (1785−1864) developed the concept of plane duality. Gergonne coined the terms "duality" and "polar" (but "pole" is due to F.-J. Servois) and adopted the style of writing dual statements side by side in his journal.

Jean-Victor Poncelet (1788−1867) author of the first text on projective geometry, *Traité des propriétés projectives des figures*, was a synthetic geometer who systematically developed the theory of poles and polars with respect to a conic. Poncelet maintained that the principle of duality was a consequence of the theory of poles and polars.

Julius Plücker (1801−1868) is credited with extending the concept of duality to three and higher dimensional projective spaces.

Poncelet and Gergonne started out as earnest but friendly rivals presenting their different points of view and techniques in papers appearing in *Annales de Gergonne*. Antagonism grew over the issue of priority in claiming the principle of duality as their own. A young Plücker was caught up in this feud when a paper he had submitted to Gergonne was so heavily edited by the time it was published that Poncelet was misled into believing that Plücker had plagiarized him. The vitriolic attack by Poncelet was countered by Plücker with the support of Gergonne and ultimately the onus was placed on Gergonne. Of this feud, Pierre Samuel has quipped that since both men were in the French army and Poncelet was a general while Gergonne a mere captain, Poncelet's view prevailed, at least among their French contemporaries.

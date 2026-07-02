---
title: "Cross-ratio"
source: https://en.wikipedia.org/wiki/Cross-ratio
domain: projective-geometry
license: CC-BY-SA-4.0
tags: projective geometry, projective plane, homogeneous coordinates, desargues theorem
fetched: 2026-07-02
---

# Cross-ratio

In geometry, the **cross-ratio**, also called the **double ratio** and **anharmonic ratio**, is a number associated with a list of four collinear points, particularly points on a projective line. Given four points A, B, C, D on a line, their cross ratio is defined as

$(A,B;C,D)={\frac {AC\cdot BD}{BC\cdot AD}}$

where an orientation of the line determines the sign of each distance and the distance is measured as projected into Euclidean space. (If one of the four points is the line's point at infinity, then the two distances involving that point are dropped from the formula.) The point D is the harmonic conjugate of C with respect to A and B precisely if the cross-ratio of the quadruple is −1, called the *harmonic ratio*. The cross-ratio can therefore be regarded as measuring the quadruple's deviation from this ratio; hence the name *anharmonic ratio*.

The cross-ratio is preserved by linear fractional transformations. It is essentially the only projective invariant of a quadruple of collinear points; this underlies its importance for projective geometry.

The cross-ratio had been defined in deep antiquity, possibly already by Euclid, and was considered by Pappus, who noted its key invariance property. It was extensively studied in the 19th century.

Variants of this concept exist for a quadruple of concurrent lines on the projective plane and a quadruple of points on the Riemann sphere. In the Cayley–Klein model of hyperbolic geometry, the distance between points is expressed in terms of a certain cross-ratio.

## Terminology and history

Pappus of Alexandria made implicit use of concepts equivalent to the cross-ratio in his *Collection: Book VII*. Early users of Pappus included Isaac Newton, Michel Chasles, and Robert Simson. In 1986 Alexander Jones made a translation of the original by Pappus, then wrote a commentary on how the lemmas of Pappus relate to modern terminology.

Modern use of the cross ratio in projective geometry began with Lazare Carnot in 1803 with his book *Géométrie de Position*. Chasles coined the French term *rapport anharmonique* [anharmonic ratio] in 1837. German geometers call it *das Doppelverhältnis* [double ratio].

Carl von Staudt was unsatisfied with past definitions of the cross-ratio relying on algebraic manipulation of Euclidean distances rather than being based purely on synthetic projective geometry concepts. In 1847, von Staudt demonstrated that the algebraic structure is implicit in projective geometry, by creating an algebra based on construction of the projective harmonic conjugate, which he called a *throw* (German: *Wurf*): given three points on a line, the harmonic conjugate is a fourth point that makes the cross ratio equal to −1. His *algebra of throws* provides an approach to numerical propositions, usually taken as axioms, but proven in projective geometry.

The English term "cross-ratio" was introduced in 1878 by William Kingdon Clifford.

## Definition

If A, B, C, and D are four points on an oriented affine line, their cross ratio is:

$(A,B;C,D)={\frac {AC:BC}{AD:BD}},$

with the notation $WX:YZ$ defined to mean the signed ratio of the displacement from W to X to the displacement from Y to Z. For collinear displacements this is a dimensionless quantity.

If the displacements themselves are taken to be signed real numbers, then the cross ratio between points can be written

$(A,B;C,D)={\frac {AC}{BC}}{\bigg /}{\frac {AD}{BD}}={\frac {AC\cdot BD}{BC\cdot AD}}.$

If ${\widehat {\mathbb {R} }}=\mathbb {R} \cup \{\infty \}$ is the projectively extended real line, the cross-ratio of four distinct numbers $x_{1},x_{2},x_{3},x_{4}$ in ${\widehat {\mathbb {R} }}$ is given by

$(x_{1},x_{2};x_{3},x_{4})={\frac {x_{3}-x_{1}}{x_{3}-x_{2}}}{\bigg /}{\frac {x_{4}-x_{1}}{x_{4}-x_{2}}}={\frac {(x_{3}-x_{1})(x_{4}-x_{2})}{(x_{3}-x_{2})(x_{4}-x_{1})}}.$

When one of $x_{1},x_{2},x_{3},x_{4}$ is the point at infinity ( $\infty$ ), this reduces to e.g.

$(\infty ,x_{2};x_{3},x_{4})={\frac {(x_{3}-\infty )(x_{4}-x_{2})}{(x_{3}-x_{2})(x_{4}-\infty )}}={\frac {(x_{4}-x_{2})}{(x_{3}-x_{2})}}.$

The same formulas can be applied to four distinct complex numbers or, more generally, to elements of any field, and can also be projectively extended as above to the case when one of them is $\infty ={\tfrac {1}{0}}.$

The cross ratio can for example be defined for pencils of lines, circles, or conics. For instance, the cross-ratio of 4 coaxial circles can be defined in numerous equivalent ways:

- Let A be a point of intersection of the circles on their radical axis, if it exists. Then the cross-ratio of the circles can be defined as the cross-ratio of the tangents to the circles through A .
- More generally, given any point in the plane, the 4 polars of this point with respect to those circles are concurrent and their cross-ratio doesn't depend on the chosen point.
- By taking the lines orthogonal to the tangents at A and projecting on the line on which lies the circle centers, we deduce it is equal to the cross-ratio of the circle centers.
- It can be proven through an inversion that the cross-ratio of these circles can be equivalently defined as the cross-ratio of the second points of intersection different than A of a circle (and in a degenerate case a line) that passes through A .

## Properties

The cross ratio of the four collinear points A, B, C, and D can be written as

$(A,B;C,D)={\frac {AC:CB}{AD:DB}}$

where ${\textstyle AC:CB}$ describes the ratio with which the point C divides the line segment AB, and ${\textstyle AD:DB}$ describes the ratio with which the point D divides that same line segment. The cross ratio then appears as a ratio of ratios, describing how the two points C and D are situated with respect to the line segment AB. As long as the points A, B, C, and D are distinct, the cross ratio (*A*, *B*; *C*, *D*) will be a non-zero real number. We can easily deduce that

- (*A*, *B*; *C*, *D*) < 0 if and only if one of the points C or D lies between the points A and B and the other does not
- (*A*, *B*; *C*, *D*) = 1 / (*A*, *B*; *D*, *C*)
- (*A*, *B*; *C*, *D*) = (*C*, *D*; *A*, *B*)
- (*A*, *B*; *C*, *D*) ≠ (*A*, *B*; *C*, *E*) ⇔ *D* ≠ *E*

### Six cross-ratios

Four points can be ordered in 4! = 4 × 3 × 2 × 1 = 24 ways, but there are only six ways for partitioning them into two unordered pairs. Thus, four points can have only six different cross-ratios, which are related as:

${\begin{aligned}&(A,B;C,D)=(B,A;D,C)=(C,D;A,B)=(D,C;B,A)=\lambda ,{\vphantom {\frac {1}{1}}}\\[4mu]&(A,B;D,C)=(B,A;C,D)=(C,D;B,A)=(D,C;A,B)={\frac {1}{\lambda }},\\[4mu]&(A,C;B,D)=(B,D;A,C)=(C,A;D,B)=(D,B;C,A)=1-\lambda ,{\vphantom {\frac {1}{1}}}\\[4mu]&(A,C;D,B)=(B,D;C,A)=(C,A;B,D)=(D,B;A,C)={\frac {1}{1-\lambda }},\\[4mu]&(A,D;B,C)=(B,C;A,D)=(C,B;D,A)=(D,A;C,B)={\frac {\lambda -1}{\lambda }},\\[4mu]&(A,D;C,B)=(B,C;D,A)=(C,B;A,D)=(D,A;B,C)={\frac {\lambda }{\lambda -1}}.\end{aligned}}$

See *Anharmonic group* below.

## Projective geometry

The cross-ratio is a **projective invariant** in the sense that it is preserved by the projective transformations of a projective line.

In particular, if four points lie on a straight line ${\textstyle L}$ in ${\textstyle {\mathbf {R}}^{2}}$ then their cross-ratio is a well-defined quantity, because any choice of the origin and even of the scale on the line will yield the same value of the cross-ratio.

Furthermore, let ${\textstyle \{L_{i}\mid 1\leq i\leq 4\}}$ be four distinct lines in the plane passing through the same point ${\textstyle Q}$ . Then any line ${\textstyle L}$ not passing through ${\textstyle Q}$ intersects these lines in four distinct points ${\textstyle P_{i}}$ (if ${\textstyle L}$ is parallel to ${\textstyle L_{i}}$ then the corresponding intersection point is "at infinity"). It turns out that the cross-ratio of these points (taken in a fixed order) does not depend on the choice of a line ${\textstyle L}$ , and hence it is an invariant of the 4-tuple of lines ${\textstyle L_{i}.}$

This can be understood as follows: if ${\textstyle L}$ and ${\textstyle L'}$ are two lines not passing through ${\textstyle Q}$ then the perspective transformation from ${\textstyle L}$ to ${\textstyle L'}$ with the center ${\textstyle Q}$ is a projective transformation that takes the quadruple ${\textstyle \{P_{i}\}}$ of points on ${\textstyle L}$ into the quadruple ${\textstyle \{P_{i}'\}}$ of points on ${\textstyle L'}$ .

Therefore, the invariance of the cross-ratio under projective automorphisms of the line implies (in fact, is equivalent to) the independence of the cross-ratio of the four collinear points ${\textstyle \{P_{i}\}}$ on the lines ${\textstyle \{L_{i}\}}$ from the choice of the line that contains them.

## Definition in homogeneous coordinates

If four collinear points are represented in homogeneous coordinates by vectors $\alpha ,\beta ,\gamma ,\delta$ such that $\gamma =a\alpha +b\beta$ and $\delta =c\alpha +d\beta$ , then their cross-ratio is $(b/a)/(d/c)$ .

## Role in non-Euclidean geometry

Arthur Cayley and Felix Klein found an application of the cross-ratio to non-Euclidean geometry. Given a nonsingular conic C in the real projective plane, its stabilizer $G_{C}$ in the projective group $G=\operatorname {PGL} (3,\mathbb {R} )$ acts transitively on the points in the interior of C . However, there is an invariant for the action of $G_{C}$ on *pairs* of points. In fact, every such invariant is expressible as a function of the appropriate cross-ratio.

### Hyperbolic geometry

Explicitly, let the conic be the unit circle. For any two points P and Q, inside the unit circle . If the line connecting them intersects the circle in two points, X and Y and the points are, in order, *X*, *P*, *Q*, *Y*. Then the hyperbolic distance between P and Q in the Cayley–Klein model of the hyperbolic plane can be expressed as

$d_{h}(P,Q)={\frac {1}{2}}\left|\log {\frac {|XQ||PY|}{|XP||QY|}}\right|$

(the factor one half is needed to make the curvature −1). Since the cross-ratio is invariant under projective transformations, it follows that the hyperbolic distance is invariant under the projective transformations that preserve the conic C.

Conversely, the group G acts transitively on the set of pairs of points (*p*, *q*) in the unit disk at a fixed hyperbolic distance.

Later, partly through the influence of Henri Poincaré, the cross ratio of four complex numbers on a circle was used for hyperbolic metrics. Being on a circle means the four points are the image of four real points under a Möbius transformation, and hence the cross ratio is a real number. The Poincaré half-plane model and Poincaré disk model are two models of hyperbolic geometry in the complex projective line.

These models are instances of Cayley–Klein metrics.

## Anharmonic group and Klein four-group

The cross-ratio may be defined by any of these four expressions:

$(A,B;C,D)=(B,A;D,C)=(C,D;A,B)=(D,C;B,A).$

These differ by the following permutations of the variables (in cycle notation):

$1,\ (\,A\,B\,)(\,C\,D\,),\ (\,A\,C\,)(\,B\,D\,),\ (\,A\,D\,)(\,B\,C\,).$

We may consider the permutations of the four variables as an action of the symmetric group S4 on functions of the four variables. Since the above four permutations leave the cross ratio unaltered, they form the stabilizer K of the cross-ratio under this action, and this induces an effective action of the quotient group $\mathrm {S} _{4}/K$ on the orbit of the cross-ratio. The four permutations in K provide a realization of the Klein four-group in S4, and the quotient $\mathrm {S} _{4}/K$ is isomorphic to the symmetric group S3.

Thus, the other permutations of the four variables alter the cross-ratio to give the following six values, which are the orbit of the six-element group $\mathrm {S} _{4}/K\cong \mathrm {S} _{3}$ :

${\begin{aligned}(A,B;C,D)&=\lambda &(A,B;D,C)&={\frac {1}{\lambda }},\\[4mu](A,C;D,B)&={\frac {1}{1-\lambda }}&(A,C;B,D)&=1-\lambda ,\\[4mu](A,D;C,B)&={\frac {\lambda }{\lambda -1}}&(A,D;B,C)&={\frac {\lambda -1}{\lambda }}.\end{aligned}}$

As functions of $\lambda ,$ these are examples of Möbius transformations, which under composition of functions form the Mobius group PGL(2, **C**). The six transformations form a subgroup known as the **anharmonic group**, again isomorphic to S3. They are the torsion elements (elliptic transforms) in PGL(2, **C**). Namely, ${\textstyle {\tfrac {1}{\lambda }}}$ , $1-\lambda \,$ , and ${\textstyle {\tfrac {\lambda }{\lambda -1}}}$ are of order 2 with respective fixed points $-1,$ ${\textstyle {\tfrac {1}{2}},}$ and $2,$ (namely, the orbit of the harmonic cross-ratio). Meanwhile, the elements ${\textstyle {\tfrac {1}{1-\lambda }}}$ and ${\textstyle {\tfrac {\lambda -1}{\lambda }}}$ are of order 3 in PGL(2, **C**), and each fixes both values ${\textstyle e^{\pm i\pi /3}={\tfrac {1}{2}}\pm {\tfrac {\sqrt {3}}{2}}i}$ of the "most symmetric" cross-ratio (the solutions to $x^{2}-x+1$ , the primitive sixth roots of unity). The order 2 elements exchange these two elements (as they do any pair other than their fixed points), and thus the action of the anharmonic group on $e^{\pm i\pi /3}$ gives the quotient map of symmetric groups $\mathrm {S} _{3}\to \mathrm {S} _{2}$ .

Further, the fixed points of the individual 2-cycles are, respectively, $-1,$ ${\textstyle {\tfrac {1}{2}},}$ and $2,$ and this set is also preserved and permuted by the 3-cycles. Geometrically, this can be visualized as the rotation group of the trigonal dihedron, which is isomorphic to the dihedral group of the triangle *D*3, as illustrated at right. Algebraically, this corresponds to the action of S3 on the 2-cycles (its Sylow 2-subgroups) by conjugation and realizes the isomorphism with the group of inner automorphisms, ${\textstyle \mathrm {S} _{3}\mathrel {\overset {\sim }{\to }} \operatorname {Inn} (\mathrm {S} _{3})\cong \mathrm {S} _{3}.}$

The anharmonic group is generated by ${\textstyle \lambda \mapsto {\tfrac {1}{\lambda }}}$ and ${\textstyle \lambda \mapsto 1-\lambda .}$ Its action on $\{0,1,\infty \}$ gives an isomorphism with S3. It may also be realised as the six Möbius transformations mentioned, which yields a projective representation of S3 over any field (since it is defined with integer entries), and is always faithful/injective (since no two terms differ only by 1/−1). Over the field with two elements, the projective line only has three points, so this representation is an isomorphism, and is the exceptional isomorphism $\mathrm {S} _{3}\approx \mathrm {PGL} (2,\mathbb {Z} _{2})$ . In characteristic 3, this stabilizes the point $-1=[-1:1]$ , which corresponds to the orbit of the harmonic cross-ratio being only a single point, since ${\textstyle 2={\tfrac {1}{2}}=-1}$ . Over the field with three elements, the projective line has only 4 points and $\mathrm {S} _{4}\approx \mathrm {PGL} (2,\mathbb {Z} _{3})$ , and thus the representation is exactly the stabilizer of the harmonic cross-ratio, yielding an embedding $\mathrm {S} _{3}\hookrightarrow \mathrm {S} _{4}$ equals the stabilizer of the point $-1$ .

### Exceptional orbits

For certain values of $\lambda$ there will be greater symmetry and therefore fewer than six possible values for the cross-ratio. These values of $\lambda$ correspond to fixed points of the action of S3 on the Riemann sphere (given by the above six functions); or, equivalently, those points with a non-trivial stabilizer in this permutation group.

The first set of fixed points is $\{0,1,\infty \}.$ However, the cross-ratio can never take on these values if the points A, B, C, and D are all distinct. These values are limit values as one pair of coordinates approach each other:

${\begin{aligned}(Z,B;Z,D)&=(A,Z;C,Z)=0,\\[4mu](Z,Z;C,D)&=(A,B;Z,Z)=1,\\[4mu](Z,B;C,Z)&=(A,Z;Z,D)=\infty .\end{aligned}}$

The second set of fixed points is ${\textstyle {\big \{}{-1},{\tfrac {1}{2}},2{\big \}}.}$ This situation is what is classically called the **harmonic cross-ratio**, and arises in projective harmonic conjugates. In the real case, there are no other exceptional orbits.

In the complex case, the most symmetric cross-ratio occurs when $\lambda =e^{\pm i\pi /3}$ . These are then the only two values of the cross-ratio, and these are acted on according to the sign of the permutation.

## Transformational approach

The cross-ratio is invariant under the projective transformations of the line. In the case of a complex projective line, or the Riemann sphere, these transformations are known as Möbius transformations. A general Möbius transformation has the form

$f(z)={\frac {az+b}{cz+d}}\;,\quad {\mbox{where }}a,b,c,d\in \mathbb {C} {\mbox{ and }}ad-bc\neq 0.$

These transformations form a group acting on the Riemann sphere, the Möbius group.

The projective invariance of the cross-ratio means that

$(f(z_{1}),f(z_{2});f(z_{3}),f(z_{4}))=(z_{1},z_{2};z_{3},z_{4}).\$

The cross-ratio is real if and only if the four points are either collinear or concyclic, reflecting the fact that every Möbius transformation maps generalized circles to generalized circles.

The action of the Möbius group is simply transitive on the set of triples of distinct points of the Riemann sphere: given any ordered triple of distinct points, $(z_{2},z_{3},z_{4})$ , there is a unique Möbius transformation $f(z)$ that maps it to the triple $(0,1,\infty )$ . This transformation can be conveniently described using the cross-ratio: since $(z,z_{2};z_{3},z_{4})$ must equal $(f(z),1;0,\infty )$ , which in turn equals $f(z)$ , we obtain

$f(z)=(z,z_{2};z_{3},z_{4}).$

An alternative explanation for the invariance of the cross-ratio is based on the fact that the group of projective transformations of a line is generated by the translations, the homotheties, and the multiplicative inversion. The differences $z_{j}-z_{k}$ are invariant under the translations

$z\mapsto z+a$

where a is a constant in the ground field $\mathbb {F}$ . Furthermore, the division ratios are invariant under a homothety

$z\mapsto bz$

for a non-zero constant b in $\mathbb {F}$ . Therefore, the cross-ratio is invariant under the affine transformations.

In order to obtain a well-defined inversion mapping

$T:z\mapsto z^{-1},$

the affine line needs to be augmented by the point at infinity, denoted $\infty$ , forming the projective line $\mathrm {P} ^{1}(\mathbb {F} )$ . Each affine mapping $f:\mathbb {F} \to \mathbb {F}$ can be uniquely extended to a mapping of $\mathrm {P} ^{1}(\mathbb {F} )$ into itself that fixes the point at infinity. The map T swaps 0 and $\infty$ . The projective group is generated by T and the affine mappings extended to $\mathrm {P} ^{1}(\mathbb {F} )$ . In the case $\mathbb {F} =\mathbb {C}$ , the complex plane, this results in the Möbius group. Since the cross-ratio is also invariant under T , it is invariant under any projective mapping of $\mathrm {P} ^{1}(\mathbb {F} )$ into itself.

### Co-ordinate description

If we write the complex points as vectors ${\vec {x_{n}}}=[\Re (z_{n}),\Im (z_{n})]^{\mathrm {T} }$ and define $x_{nm}=x_{n}-x_{m}$ , and let $(a,b)$ be the dot product of a with b , then the real part of the cross ratio is given by:

$C_{1}={\frac {(x_{12},x_{14})(x_{23},x_{34})-(x_{12},x_{34})(x_{14},x_{23})+(x_{12},x_{23})(x_{14},x_{34})}{|x_{23}|^{2}|x_{14}|^{2}}}$

This is an invariant of the 2-dimensional special conformal transformation such as inversion $x^{\mu }\rightarrow {\frac {x^{\mu }}{|x|^{2}}}$ .

The imaginary part must make use of the 2-dimensional cross product $a\times b=[a,b]=a_{2}b_{1}-a_{1}b_{2}$

$C_{2}={\frac {(x_{12},x_{14})[x_{34},x_{23}]-(x_{43},x_{23})[x_{12},x_{34}]}{|x_{23}|^{2}|x_{14}|^{2}}}$

## Ring homography

The concept of cross ratio only depends on the ring operations of addition, multiplication, and inversion (though inversion of a given element is not certain in a ring). One approach to cross ratio interprets it as a homography that takes three designated points to 0, 1, and ∞. Under restrictions having to do with inverses, it is possible to generate such a mapping with ring operations in the projective line over a ring. The cross ratio of four points is the evaluation of this homography at the fourth point.

## Differential-geometric point of view

The theory takes on a differential calculus aspect as the four points are brought into proximity. This leads to the theory of the Schwarzian derivative, and more generally of projective connections.

## Higher-dimensional generalizations

The cross-ratio does not generalize in a simple manner to higher dimensions, due to other geometric properties of configurations of points, notably collinearity – configuration spaces are more complicated, and distinct k-tuples of points are not in general position.

While the projective linear group of the projective line is 3-transitive (any three distinct points can be mapped to any other three points), and indeed simply 3-transitive (there is a *unique* projective map taking any triple to another triple), with the cross ratio thus being the unique projective invariant of a set of four points, there are basic geometric invariants in higher dimension. The projective linear group of n-space $\mathbf {P} ^{n}=\mathbf {P} (K^{n+1})$ has (*n* + 1)2 − 1 dimensions (because it is $\mathrm {PGL} (n,K)=\mathbf {P} (\mathrm {GL} (n+1,K)),$ projectivization removing one dimension), but in other dimensions the projective linear group is only 2-transitive – because three collinear points must be mapped to three collinear points (which is not a restriction in the projective line) – and thus there is not a "generalized cross ratio" providing the unique invariant of *n*2 points.

Collinearity is not the only geometric property of configurations of points that must be maintained – for example, five points determine a conic, but six general points do not lie on a conic, so whether any 6-tuple of points lies on a conic is also a projective invariant. One can study orbits of points in general position – in the line "general position" is equivalent to being distinct, while in higher dimensions it requires geometric considerations, as discussed – but, as the above indicates, this is more complicated and less informative.

However, a generalization to Riemann surfaces of positive genus exists, using the Abel–Jacobi map and theta functions.

### Volume cross-ratio

Let $V_{0},\dots ,V_{n-2},V_{j},V_{k},V_{l},V_{n}$ be non-zero vectors in $K^{n+1}$ . Their volume cross-ratio is

> $C(V_{0},\dots ,V_{n-2};V_{j},V_{k},V_{l},V_{n})={\frac {\mathrm {det} (V_{0},\dots ,V_{n-2},V_{j},V_{k})\mathrm {det} (V_{0},\dots ,V_{n-2},V_{l},V_{n})}{\mathrm {det} (V_{0},\dots ,V_{n-2},V_{j},V_{l})\mathrm {det} (V_{0},\dots ,V_{n-2},V_{k},V_{n})}}.$

This is quantity is projective invariant, and any function invariant under the action of the $\mathrm {PGL} (n,K)$ can be retrieved as a function of the volume cross-ratio. When $n=1$ , this retrieves the classical cross-ratio.

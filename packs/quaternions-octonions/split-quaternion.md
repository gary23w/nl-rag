---
title: "Split-quaternion"
source: https://en.wikipedia.org/wiki/Split-quaternion
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
---

# Split-quaternion

| × | 1 | i | j | k |
|---|---|---|---|---|
| 1 | 1 | i | j | k |
| i | i | −1 | k | −j |
| j | j | −k | 1 | −i |
| k | k | j | i | 1 |

In abstract algebra, the **split-quaternions** or **coquaternions** form an algebraic structure introduced by James Cockle in 1849 under the latter name. They form an associative algebra of dimension four over the real numbers.

After introduction in the 20th century of coordinate-free definitions of rings and algebras, it was proved that the algebra of split-quaternions is isomorphic to the ring of the 2×2 real matrices. So the study of split-quaternions can be reduced to the study of real matrices, and this may explain why there are few mentions of split-quaternions in the mathematical literature of the 20th and 21st centuries. The split-quaternions are also equivalent to the Clifford algebras Cl2,0(**R**) ≅ Cl1,1(**R**) over the real numbers, and so the study of split-quaternions is also subsumed in the study of Clifford algebra and geometric algebra in the mathematics and physics literature.

## Definition

The *split-quaternions* are the linear combinations (with real coefficients) of four basis elements 1, i, j, k that satisfy the following product rules:

i

2

= −1

,

j

2

= 1

,

k

2

= 1

,

ij = k = −ji

.

By associativity, these relations imply

jk = −i = −kj

,

ki = j = −ik

,

and also ijk = 1.

So, the split-quaternions form a real vector space of dimension four with {1, i, j, k} as a basis. They form also a noncommutative ring, by extending the above product rules by distributivity to all split-quaternions.

The square matrices

${\begin{aligned}{\boldsymbol {1}}={\begin{pmatrix}1&0\\0&1\end{pmatrix}},\qquad &{\boldsymbol {i}}={\begin{pmatrix}0&1\\-1&0\end{pmatrix}},\\{\boldsymbol {j}}={\begin{pmatrix}0&1\\1&0\end{pmatrix}},\qquad &{\boldsymbol {k}}={\begin{pmatrix}1&0\\0&-1\end{pmatrix}}.\end{aligned}}$

satisfy the same multiplication table as the corresponding split-quaternions. As these matrices form a basis of the two-by-two matrices, the unique linear function that maps 1, i, j, k to ${\boldsymbol {1}},{\boldsymbol {i}},{\boldsymbol {j}},{\boldsymbol {k}}$ (respectively) induces an algebra isomorphism from the split-quaternions to the two-by-two real matrices.

The above multiplication rules imply that the eight elements 1, i, j, k, −1, −i, −j, −k form a group under this multiplication, which is isomorphic to the dihedral group D4, the symmetry group of a square.

To see this, consider a square whose vertices are the points whose $x{\text{,}}\,y$ coordinates are -1 or +1 so that the vertices ${\begin{pmatrix}x\\y\end{pmatrix}}$ of the square listed CW from azimuth +45° are ${\bigg \{}\mathbf {x} _{1}={\begin{pmatrix}+1\\+1\end{pmatrix}}{\text{,}}\;\mathbf {x} _{2}={\begin{pmatrix}+1\\-1\end{pmatrix}}{\text{,}}\;\mathbf {x} _{3}={\begin{pmatrix}-1\\-1\end{pmatrix}}{\text{,}}\;\mathbf {x} _{4}={\begin{pmatrix}-1\\+1\end{pmatrix}}{\bigg \}}$ The matrix ${\boldsymbol {i}}$ has determinant $+1$ and gives a clockwise rotation of a quarter of a turn, since $\mathbf {x} _{2}=\mathbf {i} \,\mathbf {x} _{1}{\text{,}}\;\mathbf {x} _{3}=\mathbf {i} \,\mathbf {x} _{2}{\text{,}}\;\mathbf {x} _{4}=\mathbf {i} \,\mathbf {x} _{3}{\text{,}}\;\mathbf {x} _{1}=\mathbf {i} \,\mathbf {x} _{4}$ The matrix ${\boldsymbol {j}}$ has determinant -1 and is the reflection about the first diagonal. It fixes the vertices $\mathbf {x} _{1}$ and $\mathbf {x} _{3}$ and reflects the vertices $\mathbf {x} _{2}$ and $\mathbf {x} _{4}$ into each other. The matrix ${\boldsymbol {k}}$ is a reflection about the x axis. It does $\mathbf {x} _{1}\leftrightarrow \mathbf {x} _{2}$ and $\mathbf {x} _{3}\leftrightarrow \mathbf {x} _{4}$ . The negative of the identity matrix is the square of the matrix $\mathbf {i}$ , has determinant $+1$ , and rotates the square by 180° about the origin. It does $\mathbf {x} _{1}\leftrightarrow \mathbf {x} _{3}$ and $\mathbf {x} _{2}\leftrightarrow \mathbf {x} _{4}$ .

## Properties

Like the quaternions introduced by Hamilton in 1843, they form a four dimensional real associative algebra. But like the real algebra of 2×2 matrices – and unlike the real algebra of quaternions – the split-quaternions contain nontrivial zero divisors, nilpotent elements, and idempotents. (For example, ⁠1/2⁠(1 + j) is an idempotent zero-divisor, and i − j is nilpotent.) As an algebra over the real numbers, the algebra of split-quaternions is isomorphic to the algebra of 2×2 real matrices by the above defined isomorphism.

This isomorphism allows identifying each split-quaternion with a 2×2 matrix. So every property of split-quaternions corresponds to a similar property of matrices, which is often named differently.

The *conjugate* of a split-quaternion *q* = *w* + *x*i + *y*j + *z*k, is *q*∗ = *w* − *x*i − *y*j − *z*k. In term of matrices, the conjugate is the cofactor matrix obtained by exchanging the diagonal entries and changing the sign of the other two entries.

The product of a split-quaternion with its conjugate is the isotropic quadratic form:

$N(q)=qq^{*}=w^{2}+x^{2}-y^{2}-z^{2},$

which is called the *norm* of the split-quaternion or the determinant of the associated matrix.

The real part of a split-quaternion *q* = *w* + *x*i + *y*j + *z*k is *w* = (*q*∗ + *q*)/2. It equals the trace of associated matrix.

The norm of a product of two split-quaternions is the product of their norms. Equivalently, the determinant of a product of matrices is the product of their determinants. This property means that split-quaternions form a composition algebra. As there are nonzero split-quaternions having a zero norm, split-quaternions form a "split composition algebra" – hence their name.

A split-quaternion with a nonzero norm has a multiplicative inverse, namely *q*∗/*N*(*q*). In terms of matrices, this is equivalent to the Cramer rule that asserts that a matrix is invertible if and only its determinant is nonzero, and, in this case, the inverse of the matrix is the quotient of the adjugate matrix by the determinant. The adjugate matrix is the transpose of the cofactor matrix and is also known as the adjoint or adjunct matrix.

The isomorphism between split-quaternions and 2×2 real matrices shows that the multiplicative group of split-quaternions with a nonzero norm is isomorphic with $\operatorname {GL} (2,\mathbb {R} ),$ and the group of split quaternions of norm 1 is isomorphic with $\operatorname {SL} (2,\mathbb {R} ).$

Geometrically, the split-quaternions can be compared to Hamilton's quaternions as pencils of planes. In both cases the real numbers form the axis of a pencil. In Hamilton quaternions there is a sphere of imaginary units, and any pair of antipodal imaginary units generates a complex plane with the real line. For split-quaternions there are hyperboloids of hyperbolic and imaginary units that generate split-complex or ordinary complex planes, as described below in § Stratification.

## Representation as complex matrices

There is a representation of the split-quaternions as a unital associative subalgebra of the 2×2 matrices with complex entries. This representation can be defined by the algebra homomorphism that maps a split-quaternion *w* + *x*i + *y*j + *z*k to the matrix

${\begin{pmatrix}w+xi&y+zi\\y-zi&w-xi\end{pmatrix}}.$

Here, i (italic) is the imaginary unit, not to be confused with the split quaternion basis element i (upright roman).

The image of this homomorphism is the matrix ring formed by the matrices of the form

${\begin{pmatrix}u&v\\v^{*}&u^{*}\end{pmatrix}},$

where the superscript $^{*}$ denotes a complex conjugate.

This homomorphism maps respectively the split-quaternions i, j, k on the matrices

${\begin{pmatrix}i&0\\0&-i\end{pmatrix}},\quad {\begin{pmatrix}0&1\\1&0\end{pmatrix}},\quad {\begin{pmatrix}0&i\\-i&0\end{pmatrix}}.$

The isomorphism of algebras is completed by use of matrix multiplication to verify the identities involving i, j, and k. For instance,

$jk={\begin{pmatrix}0&1\\1&0\end{pmatrix}}{\begin{pmatrix}0&i\\-i&0\end{pmatrix}}={\begin{pmatrix}-i&0\\0&i\end{pmatrix}}=-i.$

It follows that for a split quaternion represented as a complex matrix, the conjugate is the matrix of the cofactors, and the norm is the determinant.

With the representation of split quaternions as complex matrices, the matrices of determinant 1 form the special unitary group SU(1,1), which is used to describe hyperbolic motions of the Poincaré disk model in hyperbolic geometry.

## Generation from split-complex numbers

Split-quaternions may be generated by modified Cayley–Dickson construction similar to the method of L. E. Dickson and Adrian Albert. for the division algebras **C**, **H**, and **O**. The multiplication rule $(a,b)(c,d)\ =\ (ac+d^{*}b,\ da+bc^{*})$ is used when producing the doubled product in the real-split cases. The doubled conjugate $(a,b)^{*}=(a^{*},-b),$ so that $N(a,b)\ =\ (a,b)(a,b)^{*}\ =\ (aa^{*}-bb^{*},0).$ If *a* and *b* are split-complex numbers and split-quaternion $q=(a,b)=((w+zj),(y+xj)),$

then $N(q)=aa^{*}-bb^{*}=w^{2}-z^{2}-(y^{2}-x^{2})=w^{2}+x^{2}-y^{2}-z^{2}.$

## Stratification

In this section, the real subalgebras generated by a single split-quaternion are studied and classified.

Let *p* = *w* + *x*i + *y*j + *z*k be a split-quaternion. Its *real part* is *w* = ⁠1/2⁠(*p* + *p**). Let *q* = *p* – *w* = ⁠1/2⁠(*p* – *p**) be its *nonreal part*. One has *q** = –*q*, and therefore $p^{2}=w^{2}+2wq-N(q).$ It follows that *p*2 is a real number if and only *p* is either a real number (*q* = 0 and *p* = *w*) or a *purely nonreal split quaternion* (*w* = 0 and *p* = *q*).

The structure of the subalgebra $\mathbb {R} [p]$ generated by p follows straightforwardly. One has

$\mathbb {R} [p]=\mathbb {R} [q]=\{a+bq\mid a,b\in \mathbb {R} \},$

and this is a commutative algebra. Its dimension is two except if p is real (in this case, the subalgebra is simply $\mathbb {R}$ ).

The nonreal elements of $\mathbb {R} [p]$ whose square is real have the form *aq* with $a\in \mathbb {R} .$

Three cases have to be considered, which are detailed in the next subsections.

### Nilpotent case

With above notation, if $q^{2}=0,$ (that is, if *q* is nilpotent), then *N*(*q*) = 0, that is, $x^{2}-y^{2}-z^{2}=0.$ This implies that there exist w and t in $\mathbb {R}$ such that 0 ≤ *t* < 2π and

$p=w+a\mathrm {i} +a\cos(t)\mathrm {j} +a\sin(t)\mathrm {k} .$

This is a parametrization of all split-quaternions whose nonreal part is nilpotent.

This is also a parameterization of these subalgebras by the points of a circle: the split-quaternions of the form $\mathrm {i} +\cos(t)\mathrm {j} +\sin(t)\mathrm {k}$ form a circle; a subalgebra generated by a nilpotent element contains exactly one point of the circle; and the circle does not contain any other point.

The algebra generated by a nilpotent element is isomorphic to $\mathbb {R} [X]/\langle X^{2}\rangle$ and to the plane of dual numbers.

### Imaginary units

This is the case where *N*(*q*) > 0. Letting ${\textstyle n={\sqrt {N(q)}},}$ one has

$q^{2}=-q^{*}q=N(q)=n^{2}=x^{2}-y^{2}-z^{2}.$

It follows that ⁠1/*n*⁠ *q* belongs to the hyperboloid of two sheets of equation $x^{2}-y^{2}-z^{2}=1.$ Therefore, there are real numbers *n*, *t*, *u* such that 0 ≤ *t* < 2π and

$p=w+n\cosh(u)\mathrm {i} +n\sinh(u)\cos(t)\mathrm {j} +n\sinh(u)\sin(t)\mathrm {k} .$

This is a parametrization of all split-quaternions whose nonreal part has a positive norm.

This is also a parameterization of the corresponding subalgebras by the pairs of opposite points of a hyperboloid of two sheets: the split-quaternions of the form $\cosh(u)\mathrm {i} +\sinh(u)\cos(t)\mathrm {j} +\sinh(u)\sin(t)\mathrm {k}$ form a hyperboloid of two sheets; a subalgebra generated by a split-quaternion with a nonreal part of positive norm contains exactly two opposite points on this hyperboloid, one on each sheet; and the hyperboloid does not contain any other point.

The algebra generated by a split-quaternion with a nonreal part of positive norm is isomorphic to $\mathbb {R} [X]/\langle X^{2}+1\rangle$ and to the field $\mathbb {C}$ of complex numbers.

### Hyperbolic units

This is the case where *N*(*q*) < 0. Letting ${\textstyle n={\sqrt {-N(q)}},}$ one has

$q^{2}=-q^{*}q=N(q)=-n^{2}=x^{2}-y^{2}-z^{2}.$

It follows that ⁠1/*n*⁠ *q* belongs to the hyperboloid of one sheet of equation *y*2 + *z*2 − *x*2 = 1. Therefore, there are real numbers *n*, *t*, *u* such that 0 ≤ *t* < 2π and

$p=w+n\sinh(u)\mathrm {i} +n\cosh(u)\cos(t)\mathrm {j} +n\cosh(u)\sin(t)\mathrm {k} .$

This is a parametrization of all split-quaternions whose nonreal part has a negative norm.

This is also a parameterization of the corresponding subalgebras by the pairs of opposite points of a hyperboloid of one sheet: the split-quaternions of the form $\sinh(u)\mathrm {i} +\cosh(u)\cos(t)\mathrm {j} +\cosh(u)\sin(t)\mathrm {k}$ form a hyperboloid of one sheet; a subalgebra generated by a split-quaternion with a nonreal part of negative norm contains exactly two opposite points on this hyperboloid; and the hyperboloid does not contain any other point.

The algebra generated by a split-quaternion with a nonreal part of negative norm is isomorphic to $\mathbb {R} [X]/\langle X^{2}-1\rangle$ and to the ring of split-complex numbers. It is also isomorphic (as an algebra) to $\mathbb {R} ^{2}$ by the mapping defined by ${\textstyle (1,0)\mapsto {\frac {1+X}{2}},\quad (0,1)\mapsto {\frac {1-X}{2}}.}$

### Stratification by the norm

As seen above, the purely nonreal split-quaternions of norm –1, 1 and 0 form respectively a hyperboloid of one sheet, a hyperboloid of two sheets and a circular cone in the space of non real quaternions.

These surfaces are pairwise asymptote and do not intersect. Their complement consist of six connected regions:

- the two regions located on the concave side of the hyperboloid of two sheets, where $N(q)>1$
- the two regions between the hyperboloid of two sheets and the cone, where $0<N(q)<1$
- the region between the cone and the hyperboloid of one sheet where $-1<N(q)<0$
- the region outside the hyperboloid of one sheet, where $N(q)<-1$

This stratification can be refined by considering split-quaternions of a fixed norm: for every real number *n* ≠ 0 the purely nonreal split-quaternions of norm *n* form an hyperboloid. All these hyperboloids are asymptote to the above cone, and none of these surfaces intersect any other. As the set of the purely nonreal split-quaternions is the disjoint union of these surfaces, this provides the desired stratification.

## Colour space

Split quaternions have been applied to colour balance The model refers to the Jordan algebra of symmetric matrices representing the algebra. The model reconciles trichromacy with Hering's opponency and uses the Cayley–Klein model of hyperbolic geometry for chromatic distances.

## Historical notes

The coquaternions were initially introduced (under that name) in 1849 by James Cockle in the London–Edinburgh–Dublin Philosophical Magazine. The introductory papers by Cockle were recalled in the 1904 *Bibliography* of the Quaternion Association.

In 1878 W. K. Clifford nearly described representation of split-quaternions with matrices: He used *K* to express the imaginary unit ${\begin{pmatrix}0&1\\-1&0\end{pmatrix}}$ . The only flaw was a missing minus sign in the equation

$JK={\begin{pmatrix}0&1\\1&0\end{pmatrix}}{\begin{pmatrix}0&1\\-1&0\end{pmatrix}}={\begin{pmatrix}-1&0\\0&1\end{pmatrix}}=-I.$

Alexander Macfarlane called the structure of split-quaternion vectors an *exspherical system* when he was speaking at the International Congress of Mathematicians in Paris in 1900. Macfarlane considered the "hyperboloidal counterpart to spherical analysis" in a 1910 article "Unification and Development of the Principles of the Algebra of Space" in the *Bulletin* of the Quaternion Association.

Hans Beck compared split-quaternion transformations to the circle-permuting property of Möbius transformations in 1910. The split-quaternion structure has also been mentioned briefly in the *Annals of Mathematics*.

## Synonyms

- Para-quaternions (Ivanov and Zamkovoy 2005, Mohaupt 2006) Manifolds with para-quaternionic structures are studied in differential geometry and string theory. In the para-quaternionic literature, k is replaced with −k.
- Exspherical system (Macfarlane 1900)
- Split-quaternions (Rosenfeld 1988)
- Antiquaternions (Rosenfeld 1988)
- Pseudoquaternions (Yaglom 1968 Rosenfeld 1988)

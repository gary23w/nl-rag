---
title: "Cross product (part 1/2)"
source: https://en.wikipedia.org/wiki/Cross_product
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 1/2
---

# Cross product

In mathematics, the **cross product** or **vector product** (occasionally **directed area product**, to emphasize its geometric significance) is a binary operation on two vectors in a three-dimensional oriented Euclidean vector space (named here E ), and is denoted by the symbol $\times$ . Given two linearly independent vectors **a** and **b**, the cross product, **a** × **b** (read "a cross b"), is a vector that is perpendicular to both **a** and **b**, and thus normal to the plane containing them. It has many applications in mathematics, physics, engineering, and computer programming. It should not be confused with the dot product (projection product).

The magnitude of the cross product equals the area of a parallelogram with the vectors for sides; in particular, the magnitude of the product of two perpendicular vectors is the product of their lengths. The units of the cross-product are the product of the units of each vector. If two vectors are parallel or are anti-parallel (that is, they are linearly dependent), or if either one has zero length, then their cross product is zero.

The cross product is anticommutative (that is, **a** × **b** = − **b** × **a**) and is distributive over addition, that is, **a** × (**b** + **c**) = **a** × **b** + **a** × **c**. The space E together with the cross product is an algebra over the real numbers, which is neither commutative nor associative, but is a Lie algebra with the cross product being the Lie bracket.

Like the dot product, it depends on the metric of the space under consideration, but unlike the dot product, it also depends on a choice of an orientation of the space (this is why the space must be oriented). The cross product is invariant under a rotation of the basis but is changed into its opposite by an odd permutation of the basis vectors. Therefore, the cross product is a pseudovector.

In connection with the cross product, the exterior product of vectors can be used in arbitrary dimensions (with a bivector or 2-form result) and is independent of the orientation of the space.

The product can be generalized in various ways, using the orientation and metric structure just as for the traditional 3-dimensional cross product; one can, in n dimensions, take the product of *n* − 1 vectors to produce a vector perpendicular to all of them. But if the product is limited to non-trivial binary products with vector results, it exists only in three and seven dimensions. The cross-product in seven dimensions has undesirable properties (e.g. it fails to satisfy the Jacobi identity), so it is not used in mathematical physics to represent quantities such as multi-dimensional space-time. (See § Generalizations below for other dimensions.)


## Definition

The cross product of two vectors **a** and **b** is defined only in three-dimensional space and is denoted by **a** × **b**. In physics and applied mathematics, the wedge notation **a** ∧ **b** is often used (in conjunction with the name *vector product*), although in pure mathematics such notation is usually reserved for just the exterior product, an abstraction of the vector product to n dimensions.

The cross product **a** × **b** is defined as a vector **c** that is perpendicular (orthogonal) to both **a** and **b**, with a direction given by the right-hand rule and a magnitude equal to the area of the parallelogram that the vectors span.

The cross product is defined by the formula

$\mathbf {a} \times \mathbf {b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\sin(\theta )\,\mathbf {n} ,$

where

- *θ* is the angle between **a** and **b** in the plane containing them (hence, it is between 0° and 180°),
- ‖**a**‖ and ‖**b**‖ are the magnitudes of vectors **a** and **b**,
- **n** is a unit vector perpendicular to the plane containing **a** and **b**, with direction such that the ordered set (**a**, **b**, **n**) is positively oriented.

If the vectors **a** and **b** are parallel (that is, the angle *θ* between them is either 0° or 180°), by the above formula, the cross product of **a** and **b** is the zero vector **0**.

### Direction

The direction of the vector **n** depends on the chosen orientation of the space. Conventionally, it is given by the right-hand rule, where one simply points the forefinger of the right hand in the direction of **a** and the middle finger in the direction of **b**. Then, the vector **n** is coming out of the thumb (see the adjacent picture). Using this rule implies that the cross product is anti-commutative; that is, **b** × **a** = −(**a** × **b**). By pointing the forefinger toward **b** first, and then pointing the middle finger toward **a**, the thumb will be forced in the opposite direction, reversing the sign of the product vector.

As the cross product operator depends on the orientation of the space, in general the cross product of two vectors is not a "true" vector, but a pseudovector.


## Names and origin

In 1842, William Rowan Hamilton first described the algebra of quaternions and the non-commutative Hamilton product. In particular, when the Hamilton product of two vectors (that is, pure quaternions with zero scalar part) is performed, it results in a quaternion with a scalar and vector part. The scalar and vector part of this Hamilton product corresponds to the negative of dot product and cross product of the two vectors.

In 1881, Josiah Willard Gibbs, and independently Oliver Heaviside, introduced the notation for both the dot product and the cross product using a period (**a** ⋅ **b**) and an "×" (**a** × **b**), respectively, to denote them.

In 1877, to emphasize the fact that the result of a dot product is a scalar while the result of a cross product is a vector, William Kingdon Clifford coined the alternative names **scalar product** and **vector product** for the two operations. These alternative names are still widely used in the literature.

Both the cross notation (**a** × **b**) and the name *cross product* were possibly inspired by the fact that each scalar component of **a** × **b** is computed by multiplying non-corresponding components of **a** and **b**. Conversely, a dot product **a** ⋅ **b** involves multiplications between corresponding components of **a** and **b**. As explained below, the cross product can be expressed in the form of a determinant of a special 3 × 3 matrix. According to Sarrus's rule, this involves multiplications between matrix elements identified by crossed diagonals.


## Computing

### Coordinate notation

If $(\mathbf {\color {blue}{i}} ,\mathbf {\color {red}{j}} ,\mathbf {\color {green}{k}} )$ is a positively oriented orthonormal basis, the basis vectors satisfy the following equalities ${\begin{alignedat}{2}\mathbf {\color {blue}{i}} &\times \mathbf {\color {red}{j}} &&=\mathbf {\color {green}{k}} \\\mathbf {\color {red}{j}} &\times \mathbf {\color {green}{k}} &&=\mathbf {\color {blue}{i}} \\\mathbf {\color {green}{k}} &\times \mathbf {\color {blue}{i}} &&=\mathbf {\color {red}{j}} \end{alignedat}}$ A mnemonic for these formulas is that they can be deduced from any other of them by a cyclic permutation of the basis vectors. This mnemonic applies also to many formulas given in this article.

The anticommutativity of the cross product, implies that ${\begin{alignedat}{2}\mathbf {\color {red}{j}} &\times \mathbf {\color {blue}{i}} &&=-\mathbf {\color {green}{k}} \\\mathbf {\color {green}{k}} &\times \mathbf {\color {red}{j}} &&=-\mathbf {\color {blue}{i}} \\\mathbf {\color {blue}{i}} &\times \mathbf {\color {green}{k}} &&=-\mathbf {\color {red}{j}} \end{alignedat}}$

The anticommutativity of the cross product (and the obvious lack of linear independence) also implies that $\mathbf {\color {blue}{i}} \times \mathbf {\color {blue}{i}} =\mathbf {\color {red}{j}} \times \mathbf {\color {red}{j}} =\mathbf {\color {green}{k}} \times \mathbf {\color {green}{k}} =\mathbf {0}$ (the zero vector).

These equalities, together with the distributivity and linearity of the cross product (though neither follows easily from the definition given above), are sufficient to determine the cross product of any two vectors **a** and **b**. Each vector can be defined as the sum of three orthogonal components parallel to the standard basis vectors: ${\begin{alignedat}{3}\mathbf {a} &=a_{1}\mathbf {\color {blue}{i}} &&+a_{2}\mathbf {\color {red}{j}} &&+a_{3}\mathbf {\color {green}{k}} \\\mathbf {b} &=b_{1}\mathbf {\color {blue}{i}} &&+b_{2}\mathbf {\color {red}{j}} &&+b_{3}\mathbf {\color {green}{k}} \end{alignedat}}$

Their cross product **a** × **b** can be expanded using distributivity: ${\begin{aligned}\mathbf {a} \times \mathbf {b} ={}&(a_{1}\mathbf {\color {blue}{i}} +a_{2}\mathbf {\color {red}{j}} +a_{3}\mathbf {\color {green}{k}} )\times (b_{1}\mathbf {\color {blue}{i}} +b_{2}\mathbf {\color {red}{j}} +b_{3}\mathbf {\color {green}{k}} )\\[1ex]={}&a_{1}b_{1}(\mathbf {\color {blue}{i}} \times \mathbf {\color {blue}{i}} )+a_{1}b_{2}(\mathbf {\color {blue}{i}} \times \mathbf {\color {red}{j}} )+a_{1}b_{3}(\mathbf {\color {blue}{i}} \times \mathbf {\color {green}{k}} )+{}\\&a_{2}b_{1}(\mathbf {\color {red}{j}} \times \mathbf {\color {blue}{i}} )+a_{2}b_{2}(\mathbf {\color {red}{j}} \times \mathbf {\color {red}{j}} )+a_{2}b_{3}(\mathbf {\color {red}{j}} \times \mathbf {\color {green}{k}} )+{}\\&a_{3}b_{1}(\mathbf {\color {green}{k}} \times \mathbf {\color {blue}{i}} )+a_{3}b_{2}(\mathbf {\color {green}{k}} \times \mathbf {\color {red}{j}} )+a_{3}b_{3}(\mathbf {\color {green}{k}} \times \mathbf {\color {green}{k}} )\\\end{aligned}}$

This can be interpreted as the decomposition of **a** × **b** into the sum of nine simpler cross products involving vectors aligned with **i**, **j**, or **k**. Each one of these nine cross products operates on two vectors that are easy to handle as they are either parallel or orthogonal to each other. From this decomposition, by using the above-mentioned equalities and collecting similar terms, we obtain: ${\begin{aligned}\mathbf {a} \times \mathbf {b} ={}&\quad \ a_{1}b_{1}\mathbf {0} +a_{1}b_{2}\mathbf {\color {green}{k}} -a_{1}b_{3}\mathbf {\color {red}{j}} \\&-a_{2}b_{1}\mathbf {\color {green}{k}} +a_{2}b_{2}\mathbf {0} +a_{2}b_{3}\mathbf {\color {blue}{i}} \\&+a_{3}b_{1}\mathbf {\color {red}{j}} \ -a_{3}b_{2}\mathbf {\color {blue}{i}} \ +a_{3}b_{3}\mathbf {0} \\[1ex]={}&(a_{2}b_{3}-a_{3}b_{2})\mathbf {\color {blue}{i}} +(a_{3}b_{1}-a_{1}b_{3})\mathbf {\color {red}{j}} +(a_{1}b_{2}-a_{2}b_{1})\mathbf {\color {green}{k}} \end{aligned}}$

meaning that the three scalar components of the resulting vector **s** = *s*1**i** + *s*2**j** + *s*3**k** = **a** × **b** are ${\begin{aligned}s_{1}&=a_{2}b_{3}-a_{3}b_{2}\\s_{2}&=a_{3}b_{1}-a_{1}b_{3}\\s_{3}&=a_{1}b_{2}-a_{2}b_{1}\end{aligned}}$

Using column vectors, we can represent the same result as follows: ${\begin{bmatrix}s_{1}\\s_{2}\\s_{3}\end{bmatrix}}={\begin{bmatrix}a_{2}b_{3}-a_{3}b_{2}\\a_{3}b_{1}-a_{1}b_{3}\\a_{1}b_{2}-a_{2}b_{1}\end{bmatrix}}$

### Matrix notation

The cross product can also be expressed as the formal determinant:

$\mathbf {a\times b} ={\begin{vmatrix}\mathbf {i} &\mathbf {j} &\mathbf {k} \\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\\\end{vmatrix}}$

This determinant can be computed using Sarrus's rule or cofactor expansion. Using Sarrus's rule, it expands to ${\begin{aligned}\mathbf {a} \times \mathbf {b} &=(a_{2}b_{3}\mathbf {i} +a_{3}b_{1}\mathbf {j} +a_{1}b_{2}\mathbf {k} )-(a_{3}b_{2}\mathbf {i} +a_{1}b_{3}\mathbf {j} +a_{2}b_{1}\mathbf {k} )\\&=(a_{2}b_{3}-a_{3}b_{2})\mathbf {i} -(a_{1}b_{3}-a_{3}b_{1})\mathbf {j} +(a_{1}b_{2}-a_{2}b_{1})\mathbf {k} .\end{aligned}}$

which gives the components of the resulting vector directly.

### Using Levi-Civita tensors

- In any basis, the cross-product $a\times b$ is given by the tensorial formula $E_{ijk}a^{i}b^{j}$ where $E_{ijk}$ is the covariant Levi-Civita tensor (we note the position of the indices). That corresponds to the intrinsic formula given here.
- In an orthonormal basis *having the same orientation as the space*, $a\times b$ is given by the pseudo-tensorial formula $\varepsilon _{ijk}a^{i}b^{j}$ where $\varepsilon _{ijk}$ is the Levi-Civita symbol (which is a pseudo-tensor). That is the formula used for everyday physics but it works only for this special choice of basis.
- In any orthonormal basis, $a\times b$ is given by the pseudo-tensorial formula $(-1)^{B}\varepsilon _{ijk}a^{i}b^{j}$ where $(-1)^{B}=\pm 1$ indicates whether the basis has the same orientation as the space or not.

The latter formula avoids having to change the orientation of the space when we inverse an orthonormal basis.


## Properties

### Geometric meaning

The magnitude of the cross product can be interpreted as the positive area of the parallelogram having **a** and **b** as sides (see Figure 1): $\left\|\mathbf {a} \times \mathbf {b} \right\|=\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\left|\sin \theta \right|.$

Indeed, one can also compute the volume *V* of a parallelepiped having **a**, **b** and **c** as edges by using a combination of a cross product and a dot product, called scalar triple product (see Figure 2):

$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )=\mathbf {c} \cdot (\mathbf {a} \times \mathbf {b} ).$

Since the result of the scalar triple product may be negative, the volume of the parallelepiped is given by its absolute value:

$V=|\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )|.$

Because the magnitude of the cross product goes by the sine of the angle between its arguments, the cross product can be thought of as a measure of *perpendicularity* in the same way that the dot product is a measure of *parallelism*. Given two unit vectors, their cross product has a magnitude of 1 if the two are perpendicular and a magnitude of zero if the two are parallel. The dot product of two unit vectors behaves just oppositely: it is zero when the unit vectors are perpendicular and 1 if the unit vectors are parallel.

Unit vectors enable two convenient identities: the dot product of two unit vectors yields the cosine (which may be positive or negative) of the angle between the two unit vectors. The magnitude of the cross product of the two unit vectors yields the sine (which will always be positive).

### Algebraic properties

If the cross product of two vectors is the zero vector (that is, **a** × **b** = **0**), then either one or both of the inputs is the zero vector, (**a** = **0** or **b** = **0**) or else they are parallel or antiparallel (**a** ∥ **b**) so that the sine of the angle between them is zero (*θ* = 0° or *θ* = 180° and sin *θ* = 0).

The self cross product of a vector is the zero vector: $\mathbf {a} \times \mathbf {a} =\mathbf {0} .$ The cross product is anticommutative, $\mathbf {a} \times \mathbf {b} =-(\mathbf {b} \times \mathbf {a} ),$ distributive over addition, $\mathbf {a} \times (\mathbf {b} +\mathbf {c} )=(\mathbf {a} \times \mathbf {b} )+(\mathbf {a} \times \mathbf {c} ),$ and compatible with scalar multiplication so that $(r\,\mathbf {a} )\times \mathbf {b} =\mathbf {a} \times (r\,\mathbf {b} )=r\,(\mathbf {a} \times \mathbf {b} ).$

It is not associative, but satisfies the Jacobi identity: $\mathbf {a} \times (\mathbf {b} \times \mathbf {c} )+\mathbf {b} \times (\mathbf {c} \times \mathbf {a} )+\mathbf {c} \times (\mathbf {a} \times \mathbf {b} )=\mathbf {0} .$ Distributivity, linearity and Jacobi identity show that the **R**3 vector space together with vector addition and the cross product forms a Lie algebra, the Lie algebra of the real orthogonal group in 3 dimensions, SO(3). The cross product does not obey the cancellation law; that is, **a** × **b** = **a** × **c** with **a** ≠ **0** does not imply **b** = **c**, but only that: ${\begin{aligned}\mathbf {0} &=(\mathbf {a} \times \mathbf {b} )-(\mathbf {a} \times \mathbf {c} )\\&=\mathbf {a} \times (\mathbf {b} -\mathbf {c} ).\end{aligned}}$

This can be the case where **b** and **c** cancel, but additionally where **a** and **b** − **c** are parallel; that is, they are related by a scale factor *t*, leading to: $\mathbf {c} =\mathbf {b} +t\,\mathbf {a} ,$ for some scalar *t*.

If, in addition to **a** × **b** = **a** × **c** and **a** ≠ **0** as above, it is the case that **a** ⋅ **b** = **a** ⋅ **c** then ${\begin{aligned}\mathbf {a} \times (\mathbf {b} -\mathbf {c} )&=\mathbf {0} \\\mathbf {a} \cdot (\mathbf {b} -\mathbf {c} )&=0,\end{aligned}}$ As **b** − **c** cannot be simultaneously parallel (for the cross product to be **0**) and perpendicular (for the dot product to be 0) to **a**, it must be the case that **b** and **c** cancel: **b** = **c**.

From the geometrical definition, the cross product is invariant under proper rotations about the axis defined by **a** × **b**. In formulae: $(R\mathbf {a} )\times (R\mathbf {b} )=R(\mathbf {a} \times \mathbf {b} ),$ where R is a rotation matrix with $\det(R)=1$ .

More generally, the cross product obeys the following identity under matrix transformations: $(M\mathbf {a} )\times (M\mathbf {b} )=(\det M)\left(M^{-1}\right)^{\mathrm {T} }(\mathbf {a} \times \mathbf {b} )=\operatorname {cof} M(\mathbf {a} \times \mathbf {b} )$ where M is a 3-by-3 matrix and $\left(M^{-1}\right)^{\mathrm {T} }$ is the transpose of the inverse and $\operatorname {cof}$ is the cofactor matrix. It can be readily seen how this formula reduces to the former one if M is a rotation matrix. If M is a 3-by-3 symmetric matrix applied to a generic cross product $\mathbf {a} \times \mathbf {b}$ , the following relation holds true: $M(\mathbf {a} \times \mathbf {b} )=\operatorname {Tr} (M)(\mathbf {a} \times \mathbf {b} )-\mathbf {a} \times M\mathbf {b} +\mathbf {b} \times M\mathbf {a}$ The cross product of two vectors lies in the null space of the 2 × 3 matrix with the vectors as rows: $\mathbf {a} \times \mathbf {b} \in NS\left({\begin{bmatrix}\mathbf {a} \\\mathbf {b} \end{bmatrix}}\right).$ For the sum of two cross products, the following identity holds: $\mathbf {a} \times \mathbf {b} +\mathbf {c} \times \mathbf {d} =(\mathbf {a} -\mathbf {c} )\times (\mathbf {b} -\mathbf {d} )+\mathbf {a} \times \mathbf {d} +\mathbf {c} \times \mathbf {b} .$

### Differentiation

The product rule of differential calculus applies to any bilinear operation, and therefore also to the cross product: ${\frac {d}{dt}}(\mathbf {a} \times \mathbf {b} )={\frac {d\mathbf {a} }{dt}}\times \mathbf {b} +\mathbf {a} \times {\frac {d\mathbf {b} }{dt}},$

where **a** and **b** are vectors that depend on the real variable *t*.

### Triple product expansion

The cross product is used in both forms of the triple product. The scalar triple product of three vectors is defined as

$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} ),$

It is the signed volume of the parallelepiped with edges **a**, **b** and **c** and as such the vectors can be used in any order that's an even permutation of the above ordering. The following therefore are equal:

$\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )=\mathbf {c} \cdot (\mathbf {a} \times \mathbf {b} ),$

The vector triple product is the cross product of a vector with the result of another cross product, and is related to the dot product by the following formula

${\begin{aligned}\mathbf {a} \times (\mathbf {b} \times \mathbf {c} )=\mathbf {b} (\mathbf {a} \cdot \mathbf {c} )-\mathbf {c} (\mathbf {a} \cdot \mathbf {b} )\\(\mathbf {a} \times \mathbf {b} )\times \mathbf {c} =\mathbf {b} (\mathbf {c} \cdot \mathbf {a} )-\mathbf {a} (\mathbf {b} \cdot \mathbf {c} )\end{aligned}}$

The mnemonic "BAC minus CAB" is used to remember the order of the vectors in the right hand member. This formula is used in physics to simplify vector calculations. A special case, regarding gradients and useful in vector calculus, is ${\begin{aligned}\nabla \times (\nabla \times \mathbf {f} )&=\nabla (\nabla \cdot \mathbf {f} )-(\nabla \cdot \nabla )\mathbf {f} \\&=\nabla (\nabla \cdot \mathbf {f} )-\nabla ^{2}\mathbf {f} ,\\\end{aligned}}$

where ∇2 is the vector Laplacian operator.

Other identities relate the cross product to the scalar triple product: ${\begin{aligned}(\mathbf {a} \times \mathbf {b} )\times (\mathbf {a} \times \mathbf {c} )&=(\mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} ))\mathbf {a} \\(\mathbf {a} \times \mathbf {b} )\cdot (\mathbf {c} \times \mathbf {d} )&=\mathbf {b} ^{\mathrm {T} }\left(\left(\mathbf {c} ^{\mathrm {T} }\mathbf {a} \right)I-\mathbf {c} \mathbf {a} ^{\mathrm {T} }\right)\mathbf {d} \\&=(\mathbf {a} \cdot \mathbf {c} )(\mathbf {b} \cdot \mathbf {d} )-(\mathbf {a} \cdot \mathbf {d} )(\mathbf {b} \cdot \mathbf {c} )\end{aligned}}$

where *I* is the identity matrix.

### Alternative formulation

The cross product and the dot product are related by: $\left\|\mathbf {a} \times \mathbf {b} \right\|^{2}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a} \cdot \mathbf {b} )^{2}.$

The right-hand side is the Gram determinant of **a** and **b**, the square of the area of the parallelogram defined by the vectors. This condition determines the magnitude of the cross product. Namely, since the dot product is defined, in terms of the angle *θ* between the two vectors, as:

$\mathbf {a\cdot b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\cos \theta ,$

the above given relationship can be rewritten as follows:

$\left\|\mathbf {a\times b} \right\|^{2}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}\left(1-\cos ^{2}\theta \right).$

Invoking the Pythagorean trigonometric identity one obtains: $\left\|\mathbf {a} \times \mathbf {b} \right\|=\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\left|\sin \theta \right|,$

which is the magnitude of the cross product expressed in terms of *θ*, equal to the area of the parallelogram defined by **a** and **b** (see definition above).

The combination of this requirement and the property that the cross product be orthogonal to its constituents **a** and **b** provides an alternative definition of the cross product.

### Cross product inverse

Given two vectors **a** and **c** with **a**≠**0**, the equation **a** × **b** = **c** admits solutions for **b** if and only if **a** is orthogonal to **c** (that is, if **a** ⋅ **c** = 0). In that case, there exists an infinite family of solutions for **b**, which are $\mathbf {b} ={\frac {\mathbf {c} \times \mathbf {a} }{\left\|\mathbf {a} \right\|^{2}}}+t\mathbf {a} ,$ where *t* is an arbitrary constant.

This can be derived using the triple product expansion: $\mathbf {c} \times \mathbf {a} =(\mathbf {a} \times \mathbf {b} )\times \mathbf {a} =\left\|\mathbf {a} \right\|^{2}\mathbf {b} -(\mathbf {a} \cdot \mathbf {b} )\mathbf {a}$ Rearrange to solve for **b** to give $\mathbf {b} ={\frac {\mathbf {c} \times \mathbf {a} }{\left\|\mathbf {a} \right\|^{2}}}+{\frac {\mathbf {a} \cdot \mathbf {b} }{\left\|\mathbf {a} \right\|^{2}}}\mathbf {a}$ The coefficient of the last term can be simplified to just the arbitrary constant *t* to yield the result shown above.


## Lagrange's identity

The relation $\left\|\mathbf {a} \times \mathbf {b} \right\|^{2}=\det {\begin{bmatrix}\mathbf {a} \cdot \mathbf {a} &\mathbf {a} \cdot \mathbf {b} \\\mathbf {a} \cdot \mathbf {b} &\mathbf {b} \cdot \mathbf {b} \end{bmatrix}}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a} \cdot \mathbf {b} )^{2}$

can be compared with another relation involving the right-hand side, namely Lagrange's identity expressed as

$\sum _{1\leq i<j\leq n}\left(a_{i}b_{j}-a_{j}b_{i}\right)^{2}=\left\|\mathbf {a} \right\|^{2}\left\|\mathbf {b} \right\|^{2}-(\mathbf {a\cdot b} )^{2},$

where **a** and **b** may be *n*-dimensional vectors. This also shows that the Riemannian volume form for surfaces is exactly the surface element from vector calculus. In the case where *n* = 3, combining these two equations results in the expression for the magnitude of the cross product in terms of its components:

${\begin{aligned}\|\mathbf {a} \times \mathbf {b} \|^{2}&=\sum _{1\leq i<j\leq 3}(a_{i}b_{j}-a_{j}b_{i})^{2}\\&=(a_{1}b_{2}-b_{1}a_{2})^{2}+(a_{2}b_{3}-a_{3}b_{2})^{2}+(a_{3}b_{1}-a_{1}b_{3})^{2}.\end{aligned}}$

The same result is found directly using the components of the cross product found from $\mathbf {a} \times \mathbf {b} =\det {\begin{bmatrix}{\hat {\mathbf {i} }}&{\hat {\mathbf {j} }}&{\hat {\mathbf {k} }}\\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\\\end{bmatrix}}.$

In **R**3, Lagrange's equation is a special case of the multiplicativity |**vw**| = |**v**||**w**| of the norm in the quaternion algebra.

It is a special case of another formula, also sometimes called Lagrange's identity, which is the three dimensional case of the Binet–Cauchy identity:

$(\mathbf {a} \times \mathbf {b} )\cdot (\mathbf {c} \times \mathbf {d} )=(\mathbf {a} \cdot \mathbf {c} )(\mathbf {b} \cdot \mathbf {d} )-(\mathbf {a} \cdot \mathbf {d} )(\mathbf {b} \cdot \mathbf {c} ).$

If **a** = **c** and **b** = **d**, this simplifies to the formula above.


## Alternative ways to compute

### Conversion to matrix multiplication

The vector cross product also can be expressed as the product of a skew-symmetric matrix and a vector: ${\begin{aligned}\mathbf {a} \times \mathbf {b} =[\mathbf {a} ]_{\times }\mathbf {b} &={\begin{bmatrix}\,0&\!-a_{3}&\,\,a_{2}\\\,\,a_{3}&0&\!-a_{1}\\-a_{2}&\,\,a_{1}&\,0\end{bmatrix}}{\begin{bmatrix}b_{1}\\b_{2}\\b_{3}\end{bmatrix}}\\\mathbf {a} \times \mathbf {b} ={[\mathbf {b} ]_{\times }}^{\mathrm {\!\!T} }\mathbf {a} &={\begin{bmatrix}\,0&\,\,b_{3}&\!-b_{2}\\-b_{3}&0&\,\,b_{1}\\\,\,b_{2}&\!-b_{1}&\,0\end{bmatrix}}{\begin{bmatrix}a_{1}\\a_{2}\\a_{3}\end{bmatrix}},\end{aligned}}$ where the superscript T refers to the transpose operation, and [**a**]× is defined by $[\mathbf {a} ]_{\times }{\stackrel {\rm {def}}{=}}{\begin{bmatrix}\,\,0&\!-a_{3}&\,\,\,a_{2}\\\,\,\,a_{3}&0&\!-a_{1}\\\!-a_{2}&\,\,a_{1}&\,\,0\end{bmatrix}}.$

The columns [**a**]×,i of the skew-symmetric matrix for a vector **a** can be also obtained by calculating the cross product with unit vectors. That is, $[\mathbf {a} ]_{\times ,i}=\mathbf {a} \times \mathbf {{\hat {e}}_{i}} ,\;i\in \{1,2,3\}$ or $[\mathbf {a} ]_{\times }=\sum _{i=1}^{3}\left(\mathbf {a} \times \mathbf {{\hat {e}}_{i}} \right)\otimes \mathbf {{\hat {e}}_{i}} ,$ where $\otimes$ is the outer product operator.

Also, if **a** is itself expressed as a cross product: $\mathbf {a} =\mathbf {c} \times \mathbf {d}$ then $[\mathbf {a} ]_{\times }=\mathbf {d} \mathbf {c} ^{\mathrm {T} }-\mathbf {c} \mathbf {d} ^{\mathrm {T} }.$

Proof by substitution

Evaluation of the cross product gives $\mathbf {a} =\mathbf {c} \times \mathbf {d} ={\begin{pmatrix}c_{2}d_{3}-c_{3}d_{2}\\c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}\end{pmatrix}}$ Hence, the left hand side equals $[\mathbf {a} ]_{\times }={\begin{bmatrix}0&c_{2}d_{1}-c_{1}d_{2}&c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}&0&c_{3}d_{2}-c_{2}d_{3}\\c_{1}d_{3}-c_{3}d_{1}&c_{2}d_{3}-c_{3}d_{2}&0\end{bmatrix}}$ Now, for the right hand side, $\mathbf {c} \mathbf {d} ^{\mathrm {T} }={\begin{bmatrix}c_{1}d_{1}&c_{1}d_{2}&c_{1}d_{3}\\c_{2}d_{1}&c_{2}d_{2}&c_{2}d_{3}\\c_{3}d_{1}&c_{3}d_{2}&c_{3}d_{3}\end{bmatrix}}$ And its transpose is $\mathbf {d} \mathbf {c} ^{\mathrm {T} }={\begin{bmatrix}c_{1}d_{1}&c_{2}d_{1}&c_{3}d_{1}\\c_{1}d_{2}&c_{2}d_{2}&c_{3}d_{2}\\c_{1}d_{3}&c_{2}d_{3}&c_{3}d_{3}\end{bmatrix}}$ Evaluation of the right hand side gives $\mathbf {d} \mathbf {c} ^{\mathrm {T} }-\mathbf {c} \mathbf {d} ^{\mathrm {T} }={\begin{bmatrix}0&c_{2}d_{1}-c_{1}d_{2}&c_{3}d_{1}-c_{1}d_{3}\\c_{1}d_{2}-c_{2}d_{1}&0&c_{3}d_{2}-c_{2}d_{3}\\c_{1}d_{3}-c_{3}d_{1}&c_{2}d_{3}-c_{3}d_{2}&0\end{bmatrix}}$ Comparison shows that the left hand side equals the right hand side.

This result can be generalized to higher dimensions using geometric algebra. In particular in any dimension bivectors can be identified with skew-symmetric matrices, so the product between a skew-symmetric matrix and vector is equivalent to the grade-1 part of the product of a bivector and vector. In three dimensions bivectors are dual to vectors so the product is equivalent to the cross product, with the bivector instead of its vector dual. In higher dimensions the product can still be calculated but bivectors have more degrees of freedom and are not equivalent to vectors.

This notation is also often much easier to work with, for example, in epipolar geometry.

From the general properties of the cross product follows immediately that $[\mathbf {a} ]_{\times }\,\mathbf {a} =\mathbf {0}$   and   $\mathbf {a} ^{\mathrm {T} }\,[\mathbf {a} ]_{\times }=\mathbf {0}$ and from fact that [**a**]× is skew-symmetric it follows that $\mathbf {b} ^{\mathrm {T} }\,[\mathbf {a} ]_{\times }\,\mathbf {b} =0.$

The above-mentioned triple product expansion (bac–cab rule) can be easily proven using this notation.

As mentioned above, the Lie algebra **R**3 with cross product is isomorphic to the Lie algebra **so(3)**, whose elements can be identified with the 3×3 skew-symmetric matrices. The map **a** → [**a**]× provides an isomorphism between **R**3 and **so(3)**. Under this map, the cross product of 3-vectors corresponds to the commutator of 3x3 skew-symmetric matrices.

| Matrix conversion for cross product with canonical base vectors |
|---|
| Denoting with $\mathbf {e} _{i}\in \mathbf {R} ^{3\times 1}$ the i -th canonical base vector, the cross product of a generic vector $\mathbf {v} \in \mathbf {R} ^{3\times 1}$ with $\mathbf {e} _{i}$ is given by: $\mathbf {v} \times \mathbf {e} _{i}=\mathbf {C} _{i}\mathbf {v}$ , where $\mathbf {C} _{1}={\begin{bmatrix}0&0&0\\0&0&1\\0&-1&0\end{bmatrix}},\quad \mathbf {C} _{2}={\begin{bmatrix}0&0&-1\\0&0&0\\1&0&0\end{bmatrix}},\quad \mathbf {C} _{3}={\begin{bmatrix}0&1&0\\-1&0&0\\0&0&0\end{bmatrix}}$ These matrices share the following properties: $\mathbf {C} _{i}^{\textrm {T}}=-\mathbf {C} _{i}$ (skew-symmetric); Both trace and determinant are zero; ${\text{rank}}(\mathbf {C} _{i})=2$ ; $\mathbf {C} _{i}\mathbf {C} _{i}^{\textrm {T}}=\mathbf {P} _{\mathbf {e} _{i}}^{^{\perp }}$ (see below); The orthogonal projection matrix of a vector $\mathbf {v} \neq \mathbf {0}$ is given by $\mathbf {P} _{\mathbf {v} }=\mathbf {v} \left(\mathbf {v} ^{\textrm {T}}\mathbf {v} \right)^{-1}\mathbf {v} ^{T}$ . The projection matrix onto the orthogonal complement is given by $\mathbf {P} _{\mathbf {v} }^{^{\perp }}=\mathbf {I} -\mathbf {P} _{\mathbf {v} }$ , where $\mathbf {I}$ is the identity matrix. For the special case of $\mathbf {v} =\mathbf {e} _{i}$ , it can be verified that $\mathbf {P} _{\mathbf {e} _{1}}^{^{\perp }}={\begin{bmatrix}0&0&0\\0&1&0\\0&0&1\end{bmatrix}},\quad \mathbf {P} _{\mathbf {e} _{2}}^{^{\perp }}={\begin{bmatrix}1&0&0\\0&0&0\\0&0&1\end{bmatrix}},\quad \mathbf {P} _{\mathbf {e} _{3}}^{^{\perp }}={\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix}}$ For other properties of orthogonal projection matrices, see projection (linear algebra). |

### Index notation for tensors

The cross product can alternatively be defined in terms of the Levi-Civita tensor *Eijk* and a dot product *ηmi*, which are useful in converting vector notation for tensor applications:

$\mathbf {c} =\mathbf {a\times b} \Leftrightarrow \ c^{m}=\sum _{i=1}^{3}\sum _{j=1}^{3}\sum _{k=1}^{3}\eta ^{mi}E_{ijk}a^{j}b^{k}$

where the indices $i,j,k$ correspond to vector components. This characterization of the cross product is often expressed more compactly using the Einstein summation convention as $\mathbf {c} =\mathbf {a\times b} \Leftrightarrow \ c^{m}=\eta ^{mi}E_{ijk}a^{j}b^{k}$

in which repeated indices are summed over the values 1 to 3.

In a positively-oriented orthonormal basis *ηmi* = *δ**mi* (the Kronecker delta) and $E_{ijk}=\varepsilon _{ijk}$ (the Levi-Civita symbol). In that case, this representation is another form of the skew-symmetric representation of the cross product:

$[\varepsilon _{ijk}a^{j}]=[\mathbf {a} ]_{\times }.$

In classical mechanics: representing the cross product by using the Levi-Civita symbol can cause mechanical symmetries to be obvious when physical systems are isotropic. (An example: consider a particle in a Hooke's law potential in three-space, free to oscillate in three dimensions; none of these dimensions are "special" in any sense, so symmetries lie in the cross-product-represented angular momentum, which are made clear by the above-mentioned Levi–Civita representation).

### Mnemonic

The word "xyzzy" can be used to remember the definition of the cross product.

If

$\mathbf {a} =\mathbf {b} \times \mathbf {c}$

where:

$\mathbf {a} ={\begin{bmatrix}a_{x}\\a_{y}\\a_{z}\end{bmatrix}},\ \mathbf {b} ={\begin{bmatrix}b_{x}\\b_{y}\\b_{z}\end{bmatrix}},\ \mathbf {c} ={\begin{bmatrix}c_{x}\\c_{y}\\c_{z}\end{bmatrix}}$

then:

$a_{x}=b_{y}c_{z}-b_{z}c_{y}$ $a_{y}=b_{z}c_{x}-b_{x}c_{z}$ $a_{z}=b_{x}c_{y}-b_{y}c_{x}.$

The second and third equations can be obtained from the first by simply vertically rotating the subscripts, *x* → *y* → *z* → *x*. The problem, of course, is how to remember the first equation, and two options are available for this purpose: either to remember the relevant two diagonals of Sarrus's scheme (those containing ***i***), or to remember the xyzzy sequence.

Since the first diagonal in Sarrus's scheme is just the main diagonal of the above-mentioned 3×3 matrix, the first three letters of the word xyzzy can be very easily remembered.

### Cross visualization

Similarly to the mnemonic device above, a "cross" or X can be visualized between the two vectors in the equation. This may be helpful for remembering the correct cross product formula.

If

$\mathbf {a} =\mathbf {b} \times \mathbf {c}$

then:

$\mathbf {a} ={\begin{bmatrix}b_{x}\\b_{y}\\b_{z}\end{bmatrix}}\times {\begin{bmatrix}c_{x}\\c_{y}\\c_{z}\end{bmatrix}}.$

If we want to obtain the formula for $a_{x}$ we simply drop the $b_{x}$ and $c_{x}$ from the formula, and take the next two components down:

$a_{x}={\begin{bmatrix}b_{y}\\b_{z}\end{bmatrix}}\times {\begin{bmatrix}c_{y}\\c_{z}\end{bmatrix}}.$

When doing this for $a_{y}$ the next two elements down should "wrap around" the matrix so that after the z component comes the x component. For clarity, when performing this operation for $a_{y}$ , the next two components should be z and x (in that order). While for $a_{z}$ the next two components should be taken as x and y.

$a_{y}={\begin{bmatrix}b_{z}\\b_{x}\end{bmatrix}}\times {\begin{bmatrix}c_{z}\\c_{x}\end{bmatrix}},\ a_{z}={\begin{bmatrix}b_{x}\\b_{y}\end{bmatrix}}\times {\begin{bmatrix}c_{x}\\c_{y}\end{bmatrix}}$

For $a_{x}$ then, if we visualize the cross operator as pointing from an element on the left to an element on the right, we can take the first element on the left and simply multiply by the element that the cross points to in the right-hand matrix. We then subtract the next element down on the left, multiplied by the element that the cross points to here as well. This results in our $a_{x}$ formula –

$a_{x}=b_{y}c_{z}-b_{z}c_{y}.$

We can do this in the same way for $a_{y}$ and $a_{z}$ to construct their associated formulas.


## Applications

The cross product has applications in various contexts. For example, it is used in computational geometry, physics and engineering. A non-exhaustive list of examples follows.

### Computational geometry

The cross product appears in the calculation of the distance of two skew lines (lines not in the same plane) from each other in three-dimensional space.

The cross product can be used to calculate the normal for a triangle or polygon, an operation frequently performed in computer graphics. For example, the winding of a polygon (clockwise or anticlockwise) about a point within the polygon can be calculated by triangulating the polygon (like spoking a wheel) and summing the angles (between the spokes) using the cross product to keep track of the sign of each angle.

In computational geometry of the plane, the cross product is used to determine the sign of the acute angle defined by three points $p_{1}=(x_{1},y_{1}),p_{2}=(x_{2},y_{2})$ and $p_{3}=(x_{3},y_{3})$ . It corresponds to the direction (upward or downward) of the cross product of the two coplanar vectors defined by the two pairs of points $(p_{1},p_{2})$ and $(p_{1},p_{3})$ . The sign of the acute angle is the sign of the expression $P=(x_{2}-x_{1})(y_{3}-y_{1})-(y_{2}-y_{1})(x_{3}-x_{1}),$ which is the signed length of the cross product of the two vectors. To use the cross product, simply extend the 2D vectors $p_{1},p_{2},p_{3}$ to co-planar 3D vectors by setting $z_{k}=0$ for each of them.

In the "right-handed" coordinate system, if the result is 0, the points are collinear; if it is positive, the three points constitute a positive angle of rotation around $p_{1}$ from $p_{2}$ to $p_{3}$ , otherwise a negative angle. From another point of view, the sign of P tells whether $p_{3}$ lies to the left or to the right of line $p_{1},p_{2}.$

The cross product is used in calculating the volume of a polyhedron such as a tetrahedron or parallelepiped.

### Angular momentum and torque

The angular momentum **L** of a particle about a given origin is defined as:

$\mathbf {L} =\mathbf {r} \times \mathbf {p} ,$

where **r** is the position vector of the particle relative to the origin, **p** is the linear momentum of the particle.

In the same way, the moment **M** of a force **F**B applied at point B around point A is given as:

$\mathbf {M} _{\mathrm {A} }=\mathbf {r} _{\mathrm {AB} }\times \mathbf {F} _{\mathrm {B} }\,$

In mechanics the *moment of a force* is also called *torque* and written as $\mathbf {\tau }$

Since position **r**, linear momentum **p** and force **F** are all *true* vectors, both the angular momentum **L** and the moment of a force **M** are *pseudovectors* or *axial vectors*.

### Rigid body

The cross product frequently appears in the description of rigid motions. Two points *P* and *Q* on a rigid body can be related by:

$\mathbf {v} _{P}-\mathbf {v} _{Q}={\boldsymbol {\omega }}\times \left(\mathbf {r} _{P}-\mathbf {r} _{Q}\right)\,$

where $\mathbf {r}$ is the point's position, $\mathbf {v}$ is its velocity and ${\boldsymbol {\omega }}$ is the body's angular velocity.

Since position $\mathbf {r}$ and velocity $\mathbf {v}$ are *true* vectors, the angular velocity ${\boldsymbol {\omega }}$ is a *pseudovector* or *axial vector*.

### Lorentz force

The cross product is used to describe the Lorentz force experienced by a moving electric charge *qe*: $\mathbf {F} =q_{e}\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right)$

Since velocity **v**, force **F** and electric field **E** are all *true* vectors, the magnetic field **B** is a *pseudovector*.

### Other

In vector calculus, the cross product is used to define the formula for the vector operator curl.

The trick of rewriting a cross product in terms of a matrix multiplication appears frequently in epipolar and multi-view geometry, in particular when deriving matching constraints.


## As an external product

The cross product can be defined in terms of the exterior product. It can be generalized to an external product in other than three dimensions. This generalization allows a natural geometric interpretation of the cross product. In exterior algebra the exterior product of two vectors is a bivector. A bivector is an oriented plane element, in much the same way that a vector is an oriented line element. Given two vectors *a* and *b*, one can view the bivector *a* ∧ *b* as the oriented parallelogram spanned by *a* and *b*. The cross product is then obtained by taking the Hodge star of the bivector *a* ∧ *b*, mapping 2-vectors to vectors:

$a\times b=\star (a\wedge b).$

This can be thought of as the oriented multi-dimensional element "perpendicular" to the bivector. In a *d-*dimensional space, Hodge star takes a *k*-vector to a (*d–k*)-vector; thus only in *d =* 3 dimensions is the result an element of dimension one (3–2 = 1), i.e. a vector. For example, in *d =* 4 dimensions, the cross product of two vectors has dimension 4–2 = 2, giving a bivector. Thus, only in three dimensions does cross product define an algebra structure to multiply vectors.

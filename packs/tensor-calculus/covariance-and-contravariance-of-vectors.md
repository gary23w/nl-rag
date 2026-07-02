---
title: "Covariance and contravariance of vectors"
source: https://en.wikipedia.org/wiki/Covariance_and_contravariance_of_vectors
domain: tensor-calculus
license: CC-BY-SA-4.0
tags: tensor calculus, tensor field, einstein notation, metric tensor
fetched: 2026-07-02
---

# Covariance and contravariance of vectors

In physics, especially in multilinear algebra and tensor analysis, **covariance** and **contravariance** describe how the quantitative description of certain geometric or physical entities changes with a change of basis. Briefly, a contravariant vector is a list of numbers that transforms oppositely to a change of basis, and a covariant vector is a list of numbers that transforms in the same way. Contravariant vectors are often just called *vectors* and covariant vectors are called *covectors* or *dual vectors*. The terms *covariant* and *contravariant* were introduced by James Joseph Sylvester in 1851.

Curvilinear coordinate systems, such as cylindrical or spherical coordinates, are often used in physical and geometric problems. Associated with any coordinate system is a natural choice of coordinate basis for vectors based at each point of the space, and covariance and contravariance are particularly important for understanding how the coordinate description of a vector changes by passing from one coordinate system to another. Tensors are objects in multilinear algebra that can have aspects of both covariance and contravariance.

## Introduction

In physics, a vector typically arises as the outcome of a measurement or series of measurements, and is represented as a list (or tuple) of numbers such as

$(v_{1},v_{2},v_{3}).$

The numbers in the list depend on the choice of coordinate system. For instance, if the vector represents position with respect to an observer (position vector), then the coordinate system may be obtained from a system of rigid rods, or reference axes, along which the components *v*1, *v*2, and *v*3 are measured. For a vector to represent a geometric object, it must be possible to describe how it looks in any other coordinate system. That is to say, the components of the vectors will *transform* in a certain way in passing from one coordinate system to another.

A simple illustrative case is that of a Euclidean vector. For a vector, once a set of basis vectors has been defined, then the components of that vector will always vary *opposite* to that of the basis vectors. That vector is therefore defined as a *contravariant* tensor. Take a standard position vector for example. By changing the scale of the reference axes from meters to centimeters (that is, *dividing* the scale of the reference axes by 100, so that the basis vectors now are $.01$ meters long), the components of the measured position vector are *multiplied* by 100. A vector's components change scale *inversely* to changes in scale to the reference axes, and consequently a vector is called a *contravariant* tensor.

A *vector*, which is an example of a *contravariant* tensor, has components that transform inversely to the transformation of the reference axes, (with example transformations including rotation and dilation). The vector itself does not change under these operations; instead, the components of the vector change in a way that cancels the change in the spatial axes. In other words, if the reference axes were rotated in one direction, the component representation of the vector would rotate in exactly the opposite way. Similarly, if the reference axes were stretched in one direction, the components of the vector, would reduce in an exactly compensating way. Mathematically, if the coordinate system undergoes a transformation described by an $n\times n$ invertible matrix *M*, so that the basis vectors transform according to ${\begin{bmatrix}\mathbf {e} _{1}^{\prime }\ \mathbf {e} _{2}^{\prime }\ ...\ \mathbf {e} _{n}^{\prime }\end{bmatrix}}={\begin{bmatrix}\mathbf {e} _{1}\ \mathbf {e} _{2}\ ...\ \mathbf {e} _{n}\end{bmatrix}}M$ , then the components of a vector **v** in the original basis ( $v^{i}$ ) must be similarly transformed via ${\begin{bmatrix}v^{1}{^{\prime }}\\v^{2}{^{\prime }}\\...\\v^{n}{^{\prime }}\end{bmatrix}}=M^{-1}{\begin{bmatrix}v^{1}\\v^{2}\\...\\v^{n}\end{bmatrix}}$ . The components of a *vector* are often represented arranged in a column.

By contrast, a *covector* has components that transform like the reference axes. It lives in the dual vector space, and represents a linear map from vectors to scalars. The dot product operator involving vectors is a good example of a covector. To illustrate, assume we have a covector defined as $\mathbf {v} \ \cdot$ , where $\mathbf {v}$ is a vector. The components of this covector in some arbitrary basis are ${\begin{bmatrix}\mathbf {v} \cdot \mathbf {e} _{1}&\mathbf {v} \cdot \mathbf {e} _{2}&...&\mathbf {v} \cdot \mathbf {e} _{n}\end{bmatrix}}$ , with ${\begin{bmatrix}\mathbf {e} _{1}\ \mathbf {e} _{2}\ ...\ \mathbf {e} _{n}\end{bmatrix}}$ being the basis vectors in the corresponding vector space. (This can be derived by noting that we want to get the correct answer for the dot product operation when multiplying by an arbitrary vector $\mathbf {w}$ , with components ${\begin{bmatrix}w^{1}\\w^{2}\\...\\w^{n}\end{bmatrix}}$ ). The covariance of these covector components is then seen by noting that if a transformation described by an $n\times n$ invertible matrix *M* were to be applied to the basis vectors in the corresponding vector space, ${\begin{bmatrix}\mathbf {e} _{1}^{\prime }\ \mathbf {e} _{2}^{\prime }\ ...\ \mathbf {e} _{n}^{\prime }\end{bmatrix}}={\begin{bmatrix}\mathbf {e} _{1}\ \mathbf {e} _{2}\ ...\ \mathbf {e} _{n}\end{bmatrix}}M$ , then the components of the covector $\mathbf {v} \ \cdot$ will transform with the same matrix M , namely, ${\begin{bmatrix}\mathbf {v} \cdot \mathbf {e} _{1}^{\prime }&\mathbf {v} \cdot \mathbf {e} _{2}^{\prime }&...&\mathbf {v} \cdot \mathbf {e} _{n}^{\prime }\end{bmatrix}}={\begin{bmatrix}\mathbf {v} \cdot \mathbf {e} _{1}&\mathbf {v} \cdot \mathbf {e} _{2}&...&\mathbf {v} \cdot \mathbf {e} _{n}\end{bmatrix}}M$ . The components of a *covector* are often represented arranged in a row.

A third concept related to covariance and contravariance is invariance. A scalar (also called type-0 or rank-0 tensor) is an object that does not vary with the change in basis. An example of a physical observable that is a scalar is the mass of a particle. The single, scalar value of mass is independent to changes in basis vectors and consequently is called *invariant*. The magnitude of a vector (such as distance) is another example of an invariant, because it remains fixed even if geometrical vector components vary. (For example, for a position vector of length 3 meters, if all Cartesian basis vectors are changed from 1 meters in length to $.01$ meters in length, the length of the position vector remains unchanged at 3 meters, although the vector components will all increase by a factor of $100$ ). The scalar product of a vector and a covector is invariant, because one has components that vary with the base change, and the other has components that vary oppositely, and the two effects cancel out. One thus says that covectors are *dual* to vectors.

Thus, to summarize:

- A vector or tangent vector, has components that *contra-vary* with a change of basis to compensate. That is, the matrix that transforms the vector components must be the inverse of the matrix that transforms the basis vectors. The components of vectors (as opposed to those of covectors) are said to be **contravariant**. In Einstein notation (implicit summation over repeated index), contravariant components are denoted with *upper indices* as in $\mathbf {v} =v^{i}\mathbf {e} _{i}$
- A covector or cotangent vector has components that *co-vary* with a change of basis in the corresponding (initial) vector space. That is, the components must be transformed by the same matrix as the change of basis matrix in the corresponding (initial) vector space. The components of covectors (as opposed to those of vectors) are said to be **covariant**. In Einstein notation, covariant components are denoted with *lower indices* as in $\mathbf {w} =w_{i}\mathbf {e} ^{i}.$
- The scalar product of a vector and covector is the scalar $v^{i}w_{i}$ , which is invariant. It is the duality pairing of vectors and covectors.

## Definition

The general formulation of covariance and contravariance refers to how the components of a coordinate vector transform under a change of basis (passive transformation). Thus let *V* be a vector space of dimension *n* over a field of scalars *S*, and let each of **f** = (*X*1, ..., *X**n*) and **f**′ = (*Y*1, ..., *Y**n*) be a basis of *V*. Also, let the change of basis from **f** to **f**′ be given by

| $\mathbf {f} \mapsto \mathbf {f} '={\biggl (}\sum _{i}a_{1}^{i}X_{i},\dots ,\sum _{i}a_{n}^{i}X_{i}{\biggr )}=\mathbf {f} A$ |   | 1 |
|---|---|---|

for some invertible *n*×*n* matrix *A* with entries $a_{j}^{i}$ . Here, each vector *Y**j* of the **f**′ basis is a linear combination of the vectors *X**i* of the **f** basis, so that

$Y_{j}=\sum _{i}a_{j}^{i}X_{i},$

which are the columns of the matrix product $\mathbf {f} A$ .

### Contravariant transformation

A vector v in *V* is expressed uniquely as a linear combination of the elements $X_{i}$ of the **f** basis as

| $v=\sum _{i}v^{i}[\mathbf {f} ]X_{i},$ |   | 2 |
|---|---|---|

where *v**i*[**f**] are elements of the field *S* known as the **components** of *v* in the **f** basis. Denote the column vector of components of *v* by **v**[**f**]:

$\mathbf {v} [\mathbf {f} ]={\begin{bmatrix}v^{1}[\mathbf {f} ]\\v^{2}[\mathbf {f} ]\\\vdots \\v^{n}[\mathbf {f} ]\end{bmatrix}}$

so that (**2**) can be rewritten as a matrix product

$v=\mathbf {f} \,\mathbf {v} [\mathbf {f} ].$

The vector *v* may also be expressed in terms of the **f**′ basis, so that

$v=\mathbf {f'} \,\mathbf {v} [\mathbf {f'} ].$

However, since the vector *v* itself is invariant under the choice of basis,

$\mathbf {f} \,\mathbf {v} [\mathbf {f} ]=v=\mathbf {f'} \,\mathbf {v} [\mathbf {f'} ].$

The invariance of *v* combined with the relationship (**1**) between **f** and **f**′ implies that

$\mathbf {f} \,\mathbf {v} [\mathbf {f} ]=\mathbf {f} A\,\mathbf {v} [\mathbf {f} A],$

giving the transformation rule

$\mathbf {v} [\mathbf {f'} ]=\mathbf {v} [\mathbf {f} A]=A^{-1}\mathbf {v} [\mathbf {f} ].$

In terms of components,

$v^{i}[\mathbf {f} A]=\sum _{j}{\tilde {a}}_{j}^{i}v^{j}[\mathbf {f} ]$

where the coefficients ${\tilde {a}}_{j}^{i}$ are the entries of the inverse matrix of *A*.

Because the components of the vector *v* transform with the *inverse* of the matrix *A*, these components are said to **transform contravariantly** under a change of basis.

The way *A* relates the two pairs is depicted in the following informal diagram using an arrow. The reversal of the arrow indicates a contravariant change: ${\begin{aligned}\mathbf {f} &\longrightarrow \mathbf {f'} \\v[\mathbf {f} ]&\longleftarrow v[\mathbf {f'} ]\end{aligned}}$

### Covariant transformation

A linear functional *α* on *V* is expressed uniquely in terms of its **components** (elements in *S*) in the **f** basis as

$\alpha (X_{i})=\alpha _{i}[\mathbf {f} ],\quad i=1,2,\dots ,n.$

These components are the action of *α* on the basis vectors *X**i* of the **f** basis.

Under the change of basis from **f** to **f**′ (via **1**), the components transform so that

| ${\begin{aligned}\alpha _{i}[\mathbf {f} A]&=\alpha (Y_{i})\\&=\alpha {\biggl (}\sum _{j}a_{i}^{j}X_{j}{\biggr )}\\&=\sum _{j}a_{i}^{j}\alpha (X_{j})\\&=\sum _{j}a_{i}^{j}\alpha _{j}[\mathbf {f} ].\end{aligned}}$ |   | 3 |
|---|---|---|

Denote the row vector of components of *α* by *α*[**f**]:

$\mathbf {\alpha } [\mathbf {f} ]={\begin{bmatrix}\alpha _{1}[\mathbf {f} ],\alpha _{2}[\mathbf {f} ],\dots ,\alpha _{n}[\mathbf {f} ]\end{bmatrix}}$

so that (**3**) can be rewritten as the matrix product

$\alpha [\mathbf {f} A]=\alpha [\mathbf {f} ]A.$

Because the components of the linear functional α transform with the matrix *A*, these components are said to **transform covariantly** under a change of basis.

The way *A* relates the two pairs is depicted in the following informal diagram using an arrow. A covariant relationship is indicated since the arrows travel in the same direction: ${\begin{aligned}\mathbf {f} &\longrightarrow \mathbf {f'} \\\alpha [\mathbf {f} ]&\longrightarrow \alpha [\mathbf {f'} ]\end{aligned}}$

Had a column vector representation been used instead, the transformation law would be the transpose $\alpha ^{\mathrm {T} }[\mathbf {f} A]=A^{\mathrm {T} }\alpha ^{\mathrm {T} }[\mathbf {f} ].$

## Coordinates

The choice of basis **f** on the vector space *V* defines uniquely a set of coordinate functions on *V*, by means of $x^{i}[\mathbf {f} ](v)=v^{i}[\mathbf {f} ].$ The coordinates on *V* are therefore contravariant in the sense that $x^{i}[\mathbf {f} A]=\sum _{k=1}^{n}{\tilde {a}}_{k}^{i}x^{k}[\mathbf {f} ].$ Conversely, a system of *n* quantities *v**i* that transform like the coordinates *x**i* on *V* defines a contravariant vector (or simply vector). A system of *n* quantities that transform oppositely to the coordinates is then a covariant vector (or covector).

This formulation of contravariance and covariance is often more natural in applications in which there is a coordinate space (a manifold) on which vectors live as tangent vectors or cotangent vectors. Given a local coordinate system *x**i* on the manifold, the reference axes for the coordinate system are the vector fields $X_{1}={\frac {\partial }{\partial x^{1}}},\dots ,X_{n}={\frac {\partial }{\partial x^{n}}}.$ This gives rise to the frame **f** = (*X*1, ..., *X**n*) at every point of the coordinate patch.

If *y**i* is a different coordinate system and $Y_{1}={\frac {\partial }{\partial y^{1}}},\dots ,Y_{n}={\frac {\partial }{\partial y^{n}}},$ then the frame **f'** is related to the frame **f** by the inverse of the Jacobian matrix of the coordinate transition: $\mathbf {f} '=\mathbf {f} J^{-1},\quad J=\left({\frac {\partial y^{i}}{\partial x^{j}}}\right)_{i,j=1}^{n}.$ Or, in indices, ${\frac {\partial }{\partial y^{i}}}=\sum _{j=1}^{n}{\frac {\partial x^{j}}{\partial y^{i}}}{\frac {\partial }{\partial x^{j}}}.$

A tangent vector is by definition a vector that is a linear combination of the coordinate partials $\partial /\partial x^{i}$ . Thus a tangent vector is defined by $v=\sum _{i=1}^{n}v^{i}[\mathbf {f} ]X_{i}=\mathbf {f} \ \mathbf {v} [\mathbf {f} ].$

Such a vector is contravariant with respect to change of frame. Under changes in the coordinate system, one has $\mathbf {v} \left[\mathbf {f} '\right]=\mathbf {v} \left[\mathbf {f} J^{-1}\right]=J\,\mathbf {v} [\mathbf {f} ].$

Therefore, the components of a tangent vector transform via $v^{i}\left[\mathbf {f} '\right]=\sum _{j=1}^{n}{\frac {\partial y^{i}}{\partial x^{j}}}v^{j}[\mathbf {f} ].$

Accordingly, a system of *n* quantities *v**i* depending on the coordinates that transform in this way on passing from one coordinate system to another is called a contravariant vector.

## Covariant and contravariant components of a vector with a metric

In a finite-dimensional vector space *V* over a field *K* with a non-degenerate symmetric bilinear form *g* : *V* × *V* → *K* (which may be referred to as the metric tensor), there is little distinction between covariant and contravariant vectors, because the bilinear form allows covectors to be identified with vectors. That is, a vector *v* uniquely determines a covector *α* via $\alpha (w)=g(v,w)$ for all vectors *w*. Conversely, each covector *α* determines a unique vector *v* by this equation. Because of this identification of vectors with covectors, one may speak of the **covariant components** or **contravariant components** of a vector, that is, they are just representations of the same vector using the reciprocal basis.

Given a basis **f** = (*X*1, ..., *X**n*) of *V*, there is a unique reciprocal basis **f**# = (*Y*1, ..., *Y**n*) of *V* determined by requiring that $g(Y^{i},X_{j})=\delta _{j}^{i},$ the Kronecker delta. In terms of these bases, any vector *v* can be written in two ways: ${\begin{aligned}v&=\sum _{i}v^{i}[\mathbf {f} ]X_{i}=\mathbf {f} \,\mathbf {v} [\mathbf {f} ]\\&=\sum _{i}v_{i}[\mathbf {f^{\sharp }} ]Y^{i}=\mathbf {f} ^{\sharp }\mathbf {v} ^{\sharp }[\mathbf {f} ].\end{aligned}}$ The components *v**i*[**f**] are the **contravariant components** of the vector *v* in the basis **f**, and the components *v**i*[**f**] are the **covariant components** of *v* in the basis **f**. The terminology is justified because under a change of basis,

$\mathbf {v} [\mathbf {f} A]=A^{-1}\mathbf {v} [\mathbf {f} ],\quad \mathbf {v} ^{\sharp }[\mathbf {f} A]=A^{T}\mathbf {v} ^{\sharp }[\mathbf {f} ]$ where A is an invertible $n\times n$ matrix, and the matrix transpose has its usual meaning.

### Euclidean plane

In the Euclidean plane, the dot product allows for vectors to be identified with covectors. If $\mathbf {e} _{1},\mathbf {e} _{2}$ is a basis, then the dual basis $\mathbf {e} ^{1},\mathbf {e} ^{2}$ satisfies ${\begin{aligned}\mathbf {e} ^{1}\cdot \mathbf {e} _{1}=1,&\quad \mathbf {e} ^{1}\cdot \mathbf {e} _{2}=0\\\mathbf {e} ^{2}\cdot \mathbf {e} _{1}=0,&\quad \mathbf {e} ^{2}\cdot \mathbf {e} _{2}=1.\end{aligned}}$

Thus, **e**1 and **e**2 are perpendicular to each other, as are **e**2 and **e**1, and the lengths of **e**1 and **e**2 normalized against **e**1 and **e**2, respectively.

#### Example

For example, suppose that we are given a basis **e**1, **e**2 consisting of a pair of vectors making a 45° angle with one another, such that **e**1 has length 2 and **e**2 has length 1. Then the dual basis vectors are given as follows:

- **e**2 is the result of rotating **e**1 through an angle of 90° (where the sense is measured by assuming the pair **e**1, **e**2 to be positively oriented), and then rescaling so that **e**2 ⋅ **e**2 = 1 holds.
- **e**1 is the result of rotating **e**2 through an angle of 90°, and then rescaling so that **e**1 ⋅ **e**1 = 1 holds.

Applying these rules, we find $\mathbf {e} ^{1}={\frac {1}{2}}\mathbf {e} _{1}-{\frac {1}{\sqrt {2}}}\mathbf {e} _{2}$ and $\mathbf {e} ^{2}=-{\frac {1}{\sqrt {2}}}\mathbf {e} _{1}+2\mathbf {e} _{2}.$

Thus the change of basis matrix in going from the original basis to the reciprocal basis is $R={\begin{bmatrix}{\frac {1}{2}}&-{\frac {1}{\sqrt {2}}}\\-{\frac {1}{\sqrt {2}}}&2\end{bmatrix}},$ since $[\mathbf {e} ^{1}\ \mathbf {e} ^{2}]=[\mathbf {e} _{1}\ \mathbf {e} _{2}]{\begin{bmatrix}{\frac {1}{2}}&-{\frac {1}{\sqrt {2}}}\\-{\frac {1}{\sqrt {2}}}&2\end{bmatrix}}.$

For instance, the vector $v={\frac {3}{2}}\mathbf {e} _{1}+2\mathbf {e} _{2}$ is a vector with contravariant components $v^{1}={\frac {3}{2}},\quad v^{2}=2.$

The covariant components are obtained by equating the two expressions for the vector *v*: $v=v_{1}\mathbf {e} ^{1}+v_{2}\mathbf {e} ^{2}=v^{1}\mathbf {e} _{1}+v^{2}\mathbf {e} _{2}$ so ${\begin{aligned}{\begin{bmatrix}v_{1}\\v_{2}\end{bmatrix}}&=R^{-1}{\begin{bmatrix}v^{1}\\v^{2}\end{bmatrix}}\\&={\begin{bmatrix}4&{\sqrt {2}}\\{\sqrt {2}}&1\end{bmatrix}}{\begin{bmatrix}v^{1}\\v^{2}\end{bmatrix}}\\&={\begin{bmatrix}6+2{\sqrt {2}}\\2+{\frac {3}{\sqrt {2}}}\end{bmatrix}}\end{aligned}}.$

### Three-dimensional Euclidean space

In the three-dimensional Euclidean space, one can also determine explicitly the dual basis to a given set of basis vectors **e**1, **e**2, **e**3 of *E*3 that are not necessarily assumed to be orthogonal nor of unit norm. The dual basis vectors are:

$\mathbf {e} ^{1}={\frac {\mathbf {e} _{2}\times \mathbf {e} _{3}}{\mathbf {e} _{1}\cdot (\mathbf {e} _{2}\times \mathbf {e} _{3})}};\qquad \mathbf {e} ^{2}={\frac {\mathbf {e} _{3}\times \mathbf {e} _{1}}{\mathbf {e} _{2}\cdot (\mathbf {e} _{3}\times \mathbf {e} _{1})}};\qquad \mathbf {e} ^{3}={\frac {\mathbf {e} _{1}\times \mathbf {e} _{2}}{\mathbf {e} _{3}\cdot (\mathbf {e} _{1}\times \mathbf {e} _{2})}}.$

Even when the **e**i and **e**i are not orthonormal, they are still mutually reciprocal: $\mathbf {e} ^{i}\cdot \mathbf {e} _{j}=\delta _{j}^{i},$

Then the contravariant components of any vector **v** can be obtained by the dot product of **v** with the dual basis vectors:

$q^{1}=\mathbf {v} \cdot \mathbf {e} ^{1};\qquad q^{2}=\mathbf {v} \cdot \mathbf {e} ^{2};\qquad q^{3}=\mathbf {v} \cdot \mathbf {e} ^{3}.$

Likewise, the covariant components of **v** can be obtained from the dot product of **v** with basis vectors, viz.

$q_{1}=\mathbf {v} \cdot \mathbf {e} _{1};\qquad q_{2}=\mathbf {v} \cdot \mathbf {e} _{2};\qquad q_{3}=\mathbf {v} \cdot \mathbf {e} _{3}.$

Then **v** can be expressed in two (reciprocal) ways, viz. $\mathbf {v} =q^{i}\mathbf {e} _{i}=q^{1}\mathbf {e} _{1}+q^{2}\mathbf {e} _{2}+q^{3}\mathbf {e} _{3}.$ or $\mathbf {v} =q_{i}\mathbf {e} ^{i}=q_{1}\mathbf {e} ^{1}+q_{2}\mathbf {e} ^{2}+q_{3}\mathbf {e} ^{3}$ Combining the above relations, we have $\mathbf {v} =(\mathbf {v} \cdot \mathbf {e} ^{i})\mathbf {e} _{i}=(\mathbf {v} \cdot \mathbf {e} _{i})\mathbf {e} ^{i}$ and we can convert between the basis and dual basis with $q_{i}=\mathbf {v} \cdot \mathbf {e} _{i}=(q^{j}\mathbf {e} _{j})\cdot \mathbf {e} _{i}=(\mathbf {e} _{j}\cdot \mathbf {e} _{i})q^{j}$ and $q^{i}=\mathbf {v} \cdot \mathbf {e} ^{i}=(q_{j}\mathbf {e} ^{j})\cdot \mathbf {e} ^{i}=(\mathbf {e} ^{j}\cdot \mathbf {e} ^{i})q_{j}.$

If the basis vectors are orthonormal, then they are the same as the dual basis vectors.

### Vector spaces of any dimension

The following applies to any vector space of dimension *n* equipped with a non-degenerate commutative and distributive dot product, and thus also to the Euclidean spaces of any dimension.

All indices in the formulas run from 1 to *n*. The Einstein notation for the implicit summation of the terms with the same upstairs (contravariant) and downstairs (covariant) indices is followed.

The historical and geometrical meaning of the terms *contravariant* and *covariant* will be explained at the end of this section.

#### Definitions

1. **Covariant basis** of a vector space of dimension *n*: $\mathbf {e_{j}} \triangleq$ {any linearly independent basis for which in general is $\mathbf {e_{i}} \cdot \mathbf {e_{j}} \neq \delta _{ij}$ }, i.e. not necessarily orthonormal (D.1).
2. **Contravariant components** of a vector $\mathbf {v}$ : $v^{i}\triangleq \{v^{i}\mid \mathbf {v} =v^{i}\mathbf {e_{i}} \}$ (D.2).
3. **Dual (contravariant) basis** of a vector space of dimension *n*: $\mathbf {e^{i}} \triangleq \{\mathbf {e^{i}} :\mathbf {e^{i}} \cdot \mathbf {e_{j}} =\delta _{j}^{i}\}$ (D.3).
4. **Covariant components** of a vector $\mathbf {v}$ : $v_{i}\triangleq \{v_{i}\mid \mathbf {v} =v_{i}\mathbf {e^{i}} \}$ (D.4).
5. **Components of the covariant metric tensor**: $g_{ij}\triangleq \mathbf {e_{i}} \cdot \mathbf {e_{j}}$ ; the metric tensor can be considered a square matrix, since it only has two covariant indices: $G\triangleq \{g_{ij}\}$ ; for the commutative property of the dot product, the $g_{ij}$ are symmetric (D.5).
6. **Components of the contravariant metric tensor**: $g^{ij}\triangleq \{h_{ij}:G^{-1}=\{h_{ij}\}\}$ ; these are the elements of the inverse of the covariant metric tensor/matrix $G^{-1}$ , and for the properties of the inverse of a symmetric matrix, they're also symmetric (D.6).

#### Corollaries

- $g^{ij}g_{jk}=\delta _{k}^{i}$ (1). *Proof:* from the properties of the inverse matrix (D.6).
- $\mathbf {e} ^{i}=g^{ij}\mathbf {e} _{j}$ (2). *Proof:* let's suppose that $\{A^{ij}\mid \mathbf {e} ^{i}=A^{ij}\mathbf {e} _{j}\}$ ; we will show that $A^{ij}=g^{ij}$ . Taking the dot product of both sides with $\mathbf {e} _{k}$ : ${\begin{aligned}&\mathbf {e} ^{i}\cdot \mathbf {e} _{k}=(A^{ij}\mathbf {e} _{j})\cdot \mathbf {e} _{k}\\\xrightarrow {\text{(D.3,D.5)}} {}&A^{ij}g_{jk}=\delta _{k}^{i};\end{aligned}}$ multiplying both sides by $g^{mk}$ : ${\begin{aligned}&g^{mk}A^{ij}g_{jk}=g^{mk}\delta _{k}^{i}\\\xrightarrow {\text{(D.5)}} {}&\;g^{mk}g_{kj}A^{ij}=g^{mi}\\\xrightarrow {\text{(1)}} {}&\;\delta _{j}^{m}A^{ij}=g^{mi}\\\longrightarrow {}&\;A^{im}=g^{mi}{\stackrel {\text{(D.6)}}{=}}g^{im}.\quad \blacksquare \end{aligned}}$
- $\mathbf {e} ^{i}\cdot \mathbf {e} ^{j}=g^{ij}$ (3). *Proof:* ${\begin{aligned}&\mathbf {e} ^{i}{\stackrel {\text{(2)}}{{}={}}}g^{ik}\mathbf {e} _{k};\\&\mathbf {e} ^{j}{\stackrel {\text{(2)}}{{}={}}}g^{jm}\mathbf {e} _{m}\\\longrightarrow {}&\mathbf {e} ^{i}\cdot \mathbf {e} ^{j}=g^{ik}g^{jm}(\mathbf {e} _{k}\cdot \mathbf {e} _{m}){\stackrel {\text{(D.5)}}{{}={}}}g^{ik}g^{jm}g_{km}{\stackrel {\text{(1)}}{{}={}}}\delta _{m}^{i}g^{jm}=g^{ji}{\stackrel {\text{(D.6)}}{{}={}}}g^{ij}.\quad \blacksquare \end{aligned}}$
- $\mathbf {e} _{i}=g_{ij}\mathbf {e} ^{j}$ (4). *Proof:* let's suppose that $\{B_{ij}\mid \mathbf {e} _{i}=B_{ij}\mathbf {e} ^{j}\}$ ; we will show that $B_{ij}=g_{ij}$ . Taking the dot product of both sides with $\mathbf {e} ^{k}$ : $\mathbf {e} _{i}\cdot \mathbf {e} ^{k}=(B_{ij}\mathbf {e} ^{j})\cdot \mathbf {e} ^{k}{\stackrel {\text{(D.3,3)}}{\to }}B_{ij}g^{jk}=\delta _{i}^{k}$ ; multiplying both sides by $g_{mk}$ : ${\begin{aligned}&g_{mk}B_{ij}g^{jk}=g_{mk}\delta _{i}^{k}\\\xrightarrow {\text{(D.5)}} {}&g_{mk}g^{kj}B_{ij}=g_{mi}\\\xrightarrow {\text{(1)}} {}&\delta _{m}^{j}B_{ij}=g_{mi}\\\longrightarrow {}&B_{im}=g_{mi}{\stackrel {\text{(D.5)}}{{}={}}}g_{im}.\quad \blacksquare \end{aligned}}$
- $v^{i}=g^{ij}v_{j}$ (5). *Proof:* ${\begin{aligned}&\mathbf {v} {\stackrel {\text{(D.2)}}{=}}v^{i}\mathbf {e} _{i};\\&\mathbf {v} {\stackrel {\text{(D.4)}}{=}}v_{j}\mathbf {e} ^{j}{\stackrel {\text{(2)}}{=}}v_{j}(g^{ji}\mathbf {e} _{i})\\\longrightarrow {}&v^{i}\mathbf {e} _{i}=v_{j}g^{ji}\mathbf {e} _{i},\\\forall i&:v^{i}=g^{ji}v_{j}{\stackrel {\text{(D.6)}}{=}}g^{ij}v_{j}.\quad \blacksquare \end{aligned}}$
- $v_{i}=g_{ij}v^{j}$ (6). *Proof:* specular to (5).
- $v_{i}=\mathbf {v} \cdot \mathbf {e} _{i}$ (7). *Proof:* ${\begin{aligned}\mathbf {v} \cdot \mathbf {e} _{i}{\stackrel {\text{(D.4)}}{{}={}}}(v_{j}\mathbf {e} ^{j})\cdot \mathbf {e} _{i}{\stackrel {\text{(D.3)}}{{}={}}}v_{j}\delta _{i}^{j}=v_{i}.\quad \blacksquare \end{aligned}}$
- $v^{i}=\mathbf {v} \cdot \mathbf {e} ^{i}$ (8). *Proof:* specular to (7).
- $\mathbf {u} \cdot \mathbf {v} =g_{ij}u^{i}v^{j}$ (9). *Proof:* $\mathbf {u} \cdot \mathbf {v} {\stackrel {\text{(D.2)}}{{}={}}}(u^{i}\mathbf {e} _{i})\cdot (v^{j}\mathbf {e} _{j})=(\mathbf {e} _{i}\cdot \mathbf {e} _{j})u^{i}v^{j}{\stackrel {\text{(D.5)}}{{}={}}}g_{ij}u^{i}v^{j}.\quad \blacksquare$
- $\mathbf {u} \cdot \mathbf {v} =g^{ij}u_{i}v_{j}$ (10). *Proof:* specular to (9).

#### Historical and geometrical meaning

Considering this figure for the case of an Euclidean space with $n=2$ , since $\mathbf {v} =\mathbf {OA} +\mathbf {OB}$ , if we want to express $\mathbf {v}$ in terms of the covariant basis, we have to multiply the basis vectors by the coefficients $v^{1}={\frac {\vert \mathbf {OA} \vert }{\vert \mathbf {e_{1}} \vert }}$ , $v^{2}={\frac {\vert \mathbf {OB} \vert }{\vert \mathbf {e_{2}} \vert }}$ .

With $\mathbf {v}$ and thus $\mathbf {OA}$ and $\mathbf {OB}$ fixed, if the module of $\mathbf {e_{i}}$ increases, the value of the $v^{i}$ component decreases, and that's why they're called *contra*-variant (with respect to the variation of the basis vectors module).

Symmetrically, corollary (7) states that the $v_{i}$ components equal the dot product $\mathbf {v} \cdot \mathbf {e_{i}}$ between the vector and the covariant basis vectors, and since this is directly proportional to the basis vectors module, they're called *co*-variant.

If we consider the dual (contravariant) basis, the situation is perfectly specular: the covariant components are *contra*-variant with respect to the module of the dual basis vectors, while the contravariant components are *co*-variant.

So in the end it all boils down to a matter of convention: historically the first non-orthonormal basis of the vector space of choice was called "covariant", its dual basis "contravariant", and the corresponding components named specularly.

If the covariant basis becomes orthonormal, the dual contravariant basis aligns with it and the covariant components collapse into the contravariant ones, the most familiar situation when dealing with geometrical Euclidean vectors. G and $G^{-1}$ become the identity matrix I , and:

${\begin{aligned}g_{ij}&=\delta _{ij},\\g^{ij}&=\delta ^{ij},\\[1ex]\mathbf {u} \cdot \mathbf {v} &=\delta _{ij}u^{i}v^{j}=\sum _{i}u^{i}v^{i}\\&=\delta ^{ij}u_{i}v_{j}=\sum _{i}u_{i}v_{i}.\end{aligned}}$

If the metric is non-Euclidean, but for instance Minkowskian like in the special relativity and general relativity theories, the basis are never orthonormal, even in the case of special relativity where G and $G^{-1}$ become, for $n=4,\ \eta \triangleq \operatorname {diag} (1,-1,-1,-1)$ . In this scenario, the covariant and contravariant components always differ.

## Use in tensor analysis

The distinction between covariance and contravariance is particularly important for computations with tensors, which often have **mixed variance**. This means that they have both covariant and contravariant components, or both vector and covector components. The valence of a tensor is the number of covariant and contravariant terms, and in Einstein notation, covariant components have lower indices, while contravariant components have upper indices. The duality between covariance and contravariance intervenes whenever a vector or tensor quantity is represented by its components, although modern differential geometry uses more sophisticated index-free methods to represent tensors.

In tensor analysis, a **covariant** vector varies more or less reciprocally to a corresponding contravariant vector. Expressions for lengths, areas and volumes of objects in the vector space can then be given in terms of tensors with covariant and contravariant indices. Under simple expansions and contractions of the coordinates, the reciprocity is exact; under affine transformations the components of a vector intermingle on going between covariant and contravariant expression.

On a manifold, a tensor field will typically have multiple, upper and lower indices, where Einstein notation is widely used. When the manifold is equipped with a metric, covariant and contravariant indices become very closely related to one another. Contravariant indices can be turned into covariant indices by contracting with the metric tensor. The reverse is possible by contracting with the (matrix) inverse of the metric tensor. Note that in general, no such relation exists in spaces not endowed with a metric tensor. Furthermore, from a more abstract standpoint, a tensor is simply "there" and its components of either kind are only calculational artifacts whose values depend on the chosen coordinates.

The explanation in geometric terms is that a general tensor will have contravariant indices as well as covariant indices, because it has parts that live in the tangent bundle as well as the cotangent bundle.

A contravariant vector is one which transforms like ${\frac {dx^{\mu }}{d\tau }}$ , where $x^{\mu }\!$ are the coordinates of a particle at its proper time $\tau$ . A covariant vector is one which transforms like ${\frac {\partial \varphi }{\partial x^{\mu }}}$ , where $\varphi$ is a scalar field.

## Algebra and geometry

In category theory, there are covariant functors and contravariant functors. The assignment of the dual space to a vector space is a standard example of a contravariant functor. Contravariant (resp. covariant) vectors are contravariant (resp. covariant) functors from a ${\text{GL}}(n)$ -torsor to the fundamental representation of ${\text{GL}}(n)$ . Similarly, tensors of higher degree are functors with values in other representations of ${\text{GL}}(n)$ . However, some constructions of multilinear algebra are of "mixed" variance, which prevents them from being functors.

In differential geometry, the components of a vector relative to a basis of the tangent bundle are covariant if they change with the same linear transformation as a change of basis. They are contravariant if they change by the inverse transformation. This is sometimes a source of confusion for two distinct but related reasons. The first is that vectors whose components are covariant (called covectors or 1-forms) actually pull back under smooth functions, meaning that the operation assigning the space of covectors to a smooth manifold is actually a *contravariant* functor. Likewise, vectors whose components are contravariant push forward under smooth mappings, so the operation assigning the space of (contravariant) vectors to a smooth manifold is a *covariant* functor. Secondly, in the classical approach to differential geometry, it is not bases of the tangent bundle that are the most primitive object, but rather changes in the coordinate system. Vectors with contravariant components transform in the same way as changes in the coordinates (because these actually change oppositely to the induced change of basis). Likewise, vectors with covariant components transform in the opposite way as changes in the coordinates.

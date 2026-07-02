---
title: "Matrix multiplication"
source: https://en.wikipedia.org/wiki/Matrix_multiplication
domain: tensor-processing-unit
license: CC-BY-SA-4.0
tags: tensor processing unit, ai accelerator hardware, matrix multiplication engine, hardware acceleration
fetched: 2026-07-02
---

# Matrix multiplication

In mathematics, specifically in linear algebra, **matrix multiplication** is a binary operation that produces a matrix from two matrices. For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix. The resulting matrix, known as the **matrix product**, has the number of rows of the first and the number of columns of the second matrix. The product of matrices **A** and **B** is denoted as **AB**.

Matrix multiplication was first described by the French mathematician Jacques Philippe Marie Binet in 1812, to represent the composition of linear maps that are represented by matrices. Matrix multiplication is thus a basic tool of linear algebra, and as such has numerous applications in many areas of mathematics, as well as in applied mathematics, statistics, physics, economics, and engineering. Computing matrix products is a central operation in all computational applications of linear algebra.

## Notation

This article will use the following notational conventions: matrices are represented by capital letters in bold, e.g. **A**; vectors in lowercase bold, e.g. **a**; and entries of vectors and matrices are italic (they are numbers from a field), e.g. *A* and *a*. Index notation is often the clearest way to express definitions, and is used as standard in the literature. The entry in row i, column j of matrix **A** is indicated by (**A**)*ij*, *A**ij* or *a**ij*. In contrast, a single subscript, e.g. **A**1, **A**2, is used to select a matrix (not a matrix entry) from a collection of matrices.

## Definitions

### Matrix times matrix

If **A** is an *m* × *n* matrix and **B** is an *n* × *p* matrix, $\mathbf {A} ={\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\\\end{pmatrix}},\quad \mathbf {B} ={\begin{pmatrix}b_{11}&b_{12}&\cdots &b_{1p}\\b_{21}&b_{22}&\cdots &b_{2p}\\\vdots &\vdots &\ddots &\vdots \\b_{n1}&b_{n2}&\cdots &b_{np}\\\end{pmatrix}}$ the *matrix product* **C** = **AB** (denoted without multiplication signs or dots) is defined to be the *m* × *p* matrix $\mathbf {C} ={\begin{pmatrix}c_{11}&c_{12}&\cdots &c_{1p}\\c_{21}&c_{22}&\cdots &c_{2p}\\\vdots &\vdots &\ddots &\vdots \\c_{m1}&c_{m2}&\cdots &c_{mp}\\\end{pmatrix}}$ such that $c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots +a_{in}b_{nj}=\sum _{k=1}^{n}a_{ik}b_{kj},$ for *i* = 1, ..., *m* and *j* = 1, ..., *p*.

That is, the entry ⁠ $c_{ij}$ ⁠ of the product is obtained by multiplying term-by-term the entries of the ith row of **A** and the jth column of **B**, and summing these n products. In other words, ⁠ $c_{ij}$ ⁠ is the dot product of the ith row of **A** and the jth column of **B**.

Therefore, **AB** can also be written as $\mathbf {C} ={\begin{pmatrix}a_{11}b_{11}+\cdots +a_{1n}b_{n1}&a_{11}b_{12}+\cdots +a_{1n}b_{n2}&\cdots &a_{11}b_{1p}+\cdots +a_{1n}b_{np}\\a_{21}b_{11}+\cdots +a_{2n}b_{n1}&a_{21}b_{12}+\cdots +a_{2n}b_{n2}&\cdots &a_{21}b_{1p}+\cdots +a_{2n}b_{np}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}b_{11}+\cdots +a_{mn}b_{n1}&a_{m1}b_{12}+\cdots +a_{mn}b_{n2}&\cdots &a_{m1}b_{1p}+\cdots +a_{mn}b_{np}\\\end{pmatrix}}$

Thus the product **AB** is defined if and only if the number of columns in **A** equals the number of rows in **B**, in this case *n*.

In most scenarios, the entries are numbers, but they may be any kind of mathematical objects for which an addition and a multiplication are defined, that are associative, and such that the addition is commutative, and the multiplication is distributive with respect to the addition. In particular, the entries may be matrices themselves (see block matrix).

### Matrix times vector

A vector $\mathbf {x}$ of length n can be viewed as a column vector, corresponding to an $n\times 1$ matrix $\mathbf {X}$ whose entries are given by $\mathbf {X} _{i1}=\mathbf {x} _{i}.$ If $\mathbf {A}$ is an $m\times n$ matrix, the matrix-times-vector product denoted by $\mathbf {Ax}$ is then the vector $\mathbf {y}$ that, viewed as a column vector, is equal to the $m\times 1$ matrix $\mathbf {AX} .$ In index notation, this amounts to:

$y_{i}=\sum _{j=1}^{n}a_{ij}x_{j}.$

One way of looking at this is that the changes from "plain" vector to column vector and back are assumed and left implicit.

### Vector times matrix

Similarly, a vector $\mathbf {x}$ of length n can be viewed as a row vector, corresponding to a $1\times n$ matrix. To make it clear that a row vector is meant, it is customary in this context to represent it as the transpose of a column vector; thus, one will see notations such as $\mathbf {x} ^{\mathrm {T} }\mathbf {A} .$ The identity $\mathbf {x} ^{\mathrm {T} }\mathbf {A} =(\mathbf {A} ^{\mathrm {T} }\mathbf {x} )^{\mathrm {T} }$ holds. In index notation, if $\mathbf {A}$ is an $n\times p$ matrix, $\mathbf {x} ^{\mathrm {T} }\mathbf {A} =\mathbf {y} ^{\mathrm {T} }$ amounts to: $y_{k}=\sum _{j=1}^{n}x_{j}a_{jk}.$

### Vector times vector

A vector with n components can be represented as a *1* × *n* matrix (a row-vector) or as a *n* × *1* matrix (a column-vector). Assuming that $\mathbf {a}$ and $\mathbf {b}$ are both column-vectors the dot product (or inner product) $\mathbf {a} \cdot \mathbf {b}$ is equal to the single entry of the $1\times 1$ matrix resulting from the matrix multiplication of the row-vector $\mathbf {a} ^{\mathrm {T} }$ with the column-vector $\mathbf {b}$ , i.e. $\mathbf {a} ^{\mathrm {T} }\mathbf {b}$ .

The matrix multiplication between the column-vector $\mathbf {a}$ and the row-vector $\mathbf {b} ^{\mathrm {T} }$ , also known as outer-product $\mathbf {a} \mathbf {b} ^{\mathrm {T} }$ , will, instead, give a *n* × *n* matrix.

### Illustration

The figure to the right illustrates diagrammatically the product of two matrices **A** and **B**, showing how each intersection in the product matrix corresponds to a row of **A** and a column of **B**. ${\overset {4\times 2{\text{ matrix}}}{\begin{bmatrix}a_{11}&a_{12}\\\cdot &\cdot \\a_{31}&a_{32}\\\cdot &\cdot \\\end{bmatrix}}}{\overset {2\times 3{\text{ matrix}}}{\begin{bmatrix}\cdot &b_{12}&b_{13}\\\cdot &b_{22}&b_{23}\\\end{bmatrix}}}={\overset {4\times 3{\text{ matrix}}}{\begin{bmatrix}\cdot &c_{12}&\cdot \\\cdot &\cdot &\cdot \\\cdot &\cdot &c_{33}\\\cdot &\cdot &\cdot \\\end{bmatrix}}}$

The values at the intersections, marked with circles in figure to the right, are: ${\begin{aligned}c_{12}&=a_{11}b_{12}+a_{12}b_{22}\\c_{33}&=a_{31}b_{13}+a_{32}b_{23}.\end{aligned}}$

## Fundamental applications

Historically, matrix multiplication has been introduced for facilitating and clarifying computations in linear algebra. This strong relationship between matrix multiplication and linear algebra remains fundamental in all mathematics, as well as in physics, chemistry, engineering and computer science.

### Linear maps

If a vector space has a finite basis, its vectors are each uniquely represented by a finite sequence of scalars, called a coordinate vector, whose elements are the coordinates of the vector on the basis. These coordinate vectors form another vector space, which is isomorphic to the original vector space. A coordinate vector is commonly organized as a column matrix (also called a *column vector*), which is a matrix with only one column. So, a column vector represents both a coordinate vector, and a vector of the original vector space.

A linear map A from a vector space of dimension n into a vector space of dimension m maps a column vector

$\mathbf {x} ={\begin{pmatrix}x_{1}\\x_{2}\\\vdots \\x_{n}\end{pmatrix}}$

onto the column vector

$\mathbf {y} =A(\mathbf {x} )={\begin{pmatrix}a_{11}x_{1}+\cdots +a_{1n}x_{n}\\a_{21}x_{1}+\cdots +a_{2n}x_{n}\\\vdots \\a_{m1}x_{1}+\cdots +a_{mn}x_{n}\end{pmatrix}}.$

The linear map A is thus defined by the matrix

$\mathbf {A} ={\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\\\end{pmatrix}},$

and maps the column vector $\mathbf {x}$ to the matrix product

$\mathbf {y} =\mathbf {Ax} .$

If B is another linear map from the preceding vector space of dimension m, into a vector space of dimension p, it is represented by a ⁠ $p\times m$ ⁠ matrix $\mathbf {B} .$ A straightforward computation shows that the matrix of the composite map ⁠ $B\circ A$ ⁠ is the matrix product $\mathbf {BA} .$ The general formula ⁠ $(B\circ A)(\mathbf {x} )=B(A(\mathbf {x} ))$ ⁠) that defines the function composition is instanced here as a specific case of associativity of matrix product (see § Associativity below):

$(\mathbf {BA} )\mathbf {x} =\mathbf {B} (\mathbf {Ax} )=\mathbf {BAx} .$

#### Geometric rotations

Using a Cartesian coordinate system in a Euclidean plane, the rotation by an angle $\alpha$ around the origin is a linear map. More precisely, ${\begin{bmatrix}x'\\y'\end{bmatrix}}={\begin{bmatrix}\cos \alpha &-\sin \alpha \\\sin \alpha &\cos \alpha \end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}},$ where the source point $(x,y)$ and its image $(x',y')$ are written as column vectors.

The composition of the rotation by $\alpha$ and that by $\beta$ then corresponds to the matrix product ${\begin{bmatrix}\cos \beta &-\sin \beta \\\sin \beta &\cos \beta \end{bmatrix}}{\begin{bmatrix}\cos \alpha &-\sin \alpha \\\sin \alpha &\cos \alpha \end{bmatrix}}={\begin{bmatrix}\cos \beta \cos \alpha -\sin \beta \sin \alpha &-\cos \beta \sin \alpha -\sin \beta \cos \alpha \\\sin \beta \cos \alpha +\cos \beta \sin \alpha &-\sin \beta \sin \alpha +\cos \beta \cos \alpha \end{bmatrix}}={\begin{bmatrix}\cos(\alpha +\beta )&-\sin(\alpha +\beta )\\\sin(\alpha +\beta )&\cos(\alpha +\beta )\end{bmatrix}},$ where appropriate trigonometric identities are employed for the second equality. That is, the composition corresponds to the rotation by angle $\alpha +\beta$ , as expected.

#### Resource allocation in economics

As an example, a fictitious factory uses 4 kinds of basic commodities, $b_{1},b_{2},b_{3},b_{4}$ to produce 3 kinds of intermediate goods, $m_{1},m_{2},m_{3}$ , which in turn are used to produce 3 kinds of final products, $f_{1},f_{2},f_{3}$ . The matrices

$\mathbf {A} ={\begin{pmatrix}1&0&1\\2&1&1\\0&1&1\\1&1&2\\\end{pmatrix}}$

and

$\mathbf {B} ={\begin{pmatrix}1&2&1\\2&3&1\\4&2&2\\\end{pmatrix}}$

provide the amount of basic commodities needed for a given amount of intermediate goods, and the amount of intermediate goods needed for a given amount of final products, respectively. For example, to produce one unit of intermediate good $m_{1}$ , one unit of basic commodity $b_{1}$ , two units of $b_{2}$ , no units of $b_{3}$ , and one unit of $b_{4}$ are needed, corresponding to the first column of $\mathbf {A}$ .

Using matrix multiplication, compute

$\mathbf {AB} ={\begin{pmatrix}5&4&3\\8&9&5\\\ 6&5&3\\11&9&6\\\end{pmatrix}};$

this matrix directly provides the amounts of basic commodities needed for given amounts of final goods. For example, the bottom left entry of $\mathbf {AB}$ is computed as $1\cdot 1+1\cdot 2+2\cdot 4=11$ , reflecting that $11$ units of $b_{4}$ are needed to produce one unit of $f_{1}$ . Indeed, one $b_{4}$ unit is needed for $m_{1}$ , one for each of two $m_{2}$ , and 2 for each of the four $m_{3}$ units that go into the $f_{1}$ unit, see picture.

In order to produce e.g. 100 units of the final product $f_{1}$ , 80 units of $f_{2}$ , and 60 units of $f_{3}$ , the necessary amounts of basic goods can be computed as

$(\mathbf {AB} ){\begin{pmatrix}100\\80\\60\\\end{pmatrix}}={\begin{pmatrix}1000\\1820\\1180\\2180\end{pmatrix}},$

that is, $1000$ units of $b_{1}$ , $1820$ units of $b_{2}$ , $1180$ units of $b_{3}$ , $2180$ units of $b_{4}$ are needed. Similarly, the product matrix $\mathbf {AB}$ can be used to compute the needed amounts of basic goods for other final-good amount data.

### System of linear equations

The general form of a system of linear equations is

${\begin{matrix}a_{11}x_{1}+\cdots +a_{1n}x_{n}=b_{1},\\a_{21}x_{1}+\cdots +a_{2n}x_{n}=b_{2},\\\vdots \\a_{m1}x_{1}+\cdots +a_{mn}x_{n}=b_{m}.\end{matrix}}$

Using same notation as above, such a system is equivalent with the single matrix equation

$\mathbf {Ax} =\mathbf {b} .$

### Dot product, bilinear form and sesquilinear form

The dot product of two column vectors is the unique entry of the matrix product

$\mathbf {x} ^{\mathsf {T}}\mathbf {y} ,$

where $\mathbf {x} ^{\mathsf {T}}$ is the row vector obtained by transposing $\mathbf {x}$ . (As usual, a 1×1 matrix is identified with its unique entry.)

More generally, any bilinear form over a vector space of finite dimension may be expressed as a matrix product

$\mathbf {x} ^{\mathsf {T}}\mathbf {Ay} ,$

and any sesquilinear form may be expressed as

$\mathbf {x} ^{\dagger }\mathbf {Ay} ,$

where $\mathbf {x} ^{\dagger }$ denotes the conjugate transpose of $\mathbf {x}$ (conjugate of the transpose, or equivalently transpose of the conjugate).

## General properties

Matrix multiplication shares some properties with usual multiplication. However, matrix multiplication is not defined if the number of columns of the first factor differs from the number of rows of the second factor, and it is non-commutative, even when the product remains defined after changing the order of the factors.

### Non-commutativity

An operation is commutative if, given two elements **A** and **B** such that the product $\mathbf {A} \mathbf {B}$ is defined, then $\mathbf {B} \mathbf {A}$ is also defined, and $\mathbf {A} \mathbf {B} =\mathbf {B} \mathbf {A} .$

If **A** and **B** are matrices of respective sizes ⁠ $m\times n$ ⁠ and ⁠ $p\times q$ ⁠, then $\mathbf {A} \mathbf {B}$ is defined if ⁠ $n=p$ ⁠, and $\mathbf {B} \mathbf {A}$ is defined if ⁠ $m=q$ ⁠. Therefore, if one of the products is defined, the other one need not be defined. If ⁠ $m=q\neq n=p$ ⁠, the two products are defined, but have different sizes; thus they cannot be equal. Only if ⁠ $m=q=n=p$ ⁠, that is, if **A** and **B** are square matrices of the same size, are both products defined and of the same size. Even in this case, one has in general

$\mathbf {A} \mathbf {B} \neq \mathbf {B} \mathbf {A} .$

For example

${\begin{pmatrix}0&1\\0&0\end{pmatrix}}{\begin{pmatrix}0&0\\1&0\end{pmatrix}}={\begin{pmatrix}1&0\\0&0\end{pmatrix}},$

but

${\begin{pmatrix}0&0\\1&0\end{pmatrix}}{\begin{pmatrix}0&1\\0&0\end{pmatrix}}={\begin{pmatrix}0&0\\0&1\end{pmatrix}}.$

This example may be expanded for showing that, if **A** is a ⁠ $n\times n$ ⁠ matrix with entries in a field F, then $\mathbf {A} \mathbf {B} =\mathbf {B} \mathbf {A}$ for every ⁠ $n\times n$ ⁠ matrix **B** with entries in F, if and only if $\mathbf {A} =c\,\mathbf {I}$ where ⁠ $c\in F$ ⁠, and **I** is the ⁠ $n\times n$ ⁠ identity matrix. If, instead of a field, the entries are supposed to belong to a ring, then one must add the condition that c belongs to the center of the ring.

One special case where commutativity does occur is when **D** and **E** are two (square) diagonal matrices (of the same size); then **DE** = **ED**. Again, if the matrices are over a general ring rather than a field, the corresponding entries in each must also commute with each other for this to hold.

### Distributivity

The matrix product is distributive with respect to matrix addition. That is, if **A**, **B**, **C**, **D** are matrices of respective sizes *m* × *n*, *n* × *p*, *n* × *p*, and *p* × *q*, respectively, one has (left distributivity)

$\mathbf {A} (\mathbf {B} +\mathbf {C} )=\mathbf {AB} +\mathbf {AC} ,$

and (right distributivity)

$(\mathbf {B} +\mathbf {C} )\mathbf {D} =\mathbf {BD} +\mathbf {CD} .$

This results from the distributivity for coefficients by

$\sum _{k}a_{ik}(b_{kj}+c_{kj})=\sum _{k}a_{ik}b_{kj}+\sum _{k}a_{ik}c_{kj}$

$\sum _{k}(b_{ik}+c_{ik})d_{kj}=\sum _{k}b_{ik}d_{kj}+\sum _{k}c_{ik}d_{kj}.$

### Product with a scalar

If **A** is a matrix and c a scalar, then the matrices $c\mathbf {A}$ and $\mathbf {A} c$ are obtained by left or right multiplying all entries of **A** by c. If the scalars have the commutative property, then $c\mathbf {A} =\mathbf {A} c.$

If the product $\mathbf {AB}$ is defined (that is, the number of columns of **A** equals the number of rows of **B**), then

$c(\mathbf {AB} )=(c\mathbf {A} )\mathbf {B}$

and

$(\mathbf {A} \mathbf {B} )c=\mathbf {A} (\mathbf {B} c).$

If the scalars have the commutative property, then all four matrices are equal. More generally, all four are equal if *c* belongs to the center of a ring containing the entries of the matrices, because in this case, *c***X** = **X***c* for all matrices **X**.

These properties result from the bilinearity of the product of scalars:

$c\left(\sum _{k}a_{ik}b_{kj}\right)=\sum _{k}(ca_{ik})b_{kj}$

$\left(\sum _{k}a_{ik}b_{kj}\right)c=\sum _{k}a_{ik}(b_{kj}c).$

### Transpose

If the scalars have the commutative property, the transpose of a product of matrices is the product, in the reverse order, of the transposes of the factors. That is

$(\mathbf {AB} )^{\mathsf {T}}=\mathbf {B} ^{\mathsf {T}}\mathbf {A} ^{\mathsf {T}}$

where T denotes the transpose, that is the interchange of rows and columns.

This identity does not hold for noncommutative entries, since the order between the entries of **A** and **B** is reversed, when one expands the definition of the matrix product.

### Complex conjugate

If **A** and **B** have complex entries, then

$(\mathbf {AB} )^{*}=\mathbf {A} ^{*}\mathbf {B} ^{*}$

where * denotes the entry-wise complex conjugate of a matrix.

This results from applying to the definition of matrix product the fact that the conjugate of a sum is the sum of the conjugates of the summands and the conjugate of a product is the product of the conjugates of the factors.

Transposition acts on the indices of the entries, while conjugation acts independently on the entries themselves. It results that, if **A** and **B** have complex entries, one has

$(\mathbf {AB} )^{\dagger }=\mathbf {B} ^{\dagger }\mathbf {A} ^{\dagger },$

where † denotes the conjugate transpose (conjugate of the transpose, or equivalently transpose of the conjugate).

### Associativity

Given three matrices **A**, **B** and **C**, the products (**AB**)**C** and **A**(**BC**) are defined if and only if the number of columns of **A** equals the number of rows of **B**, and the number of columns of **B** equals the number of rows of **C** (in particular, if one of the products is defined, then the other is also defined). In this case, one has the associative property

$(\mathbf {AB} )\mathbf {C} =\mathbf {A} (\mathbf {BC} ).$

As for any associative operation, this allows omitting parentheses, and writing the above products as ⁠ $\mathbf {ABC} .$ ⁠

This extends naturally to the product of any number of matrices provided that the dimensions match. That is, if **A**1, **A**2, ..., **A***n* are matrices such that the number of columns of **A***i* equals the number of rows of **A***i* + 1 for *i* = 1, ..., *n* – 1, then the product

$\prod _{i=1}^{n}\mathbf {A} _{i}=\mathbf {A} _{1}\mathbf {A} _{2}\cdots \mathbf {A} _{n}$

is defined and does not depend on the order of the multiplications, if the order of the matrices is kept fixed.

These properties may be proved by straightforward but complicated summation manipulations. This result also follows from the fact that matrices represent linear maps. Therefore, the associative property of matrices is simply a specific case of the associative property of function composition.

#### Computational complexity depends on parenthesization

Although the result of a sequence of matrix products does not depend on the order of operation (provided that the order of the matrices is not changed), the computational complexity may depend dramatically on this order.

For example, if **A**, **B** and **C** are matrices of respective sizes 10×30, 30×5, 5×60, computing (**AB**)**C** needs 10×30×5 + 10×5×60 = 4,500 multiplications, while computing **A**(**BC**) needs 30×5×60 + 10×30×60 = 27,000 multiplications.

Algorithms have been designed for choosing the best order of products; see Matrix chain multiplication. When the number n of matrices increases, it has been shown that the choice of the best order has a complexity of $O(n\log n).$

#### Application to similarity

Any invertible matrix $\mathbf {P}$ defines a similarity transformation (on square matrices of the same size as $\mathbf {P}$ )

$S_{\mathbf {P} }(\mathbf {A} )=\mathbf {P} ^{-1}\mathbf {A} \mathbf {P} .$

Similarity transformations map product to products, that is

$S_{\mathbf {P} }(\mathbf {AB} )=S_{\mathbf {P} }(\mathbf {A} )S_{\mathbf {P} }(\mathbf {B} ).$

In fact, one has

$\mathbf {P} ^{-1}(\mathbf {AB} )\mathbf {P} =\mathbf {P} ^{-1}\mathbf {A} (\mathbf {P} \mathbf {P} ^{-1})\mathbf {B} \mathbf {P} =(\mathbf {P} ^{-1}\mathbf {A} \mathbf {P} )(\mathbf {P} ^{-1}\mathbf {B} \mathbf {P} ).$

## Square matrices

Let us denote ${\mathcal {M}}_{n}(R)$ the set of *n*×*n* square matrices with entries in a ring R, which, in practice, is often a field.

In ${\mathcal {M}}_{n}(R)$ , the product is defined for every pair of matrices. This makes ${\mathcal {M}}_{n}(R)$ a ring, which has the identity matrix **I** as an identity element (the matrix whose diagonal entries are equal to 1 and all other entries are 0). This ring is also an associative R-algebra.

If *n* > 1, many matrices do not have a multiplicative inverse. For example, a matrix such that all entries of a row (or a column) are 0 does not have an inverse. If it exists, the inverse of a matrix **A** is denoted **A**−1, and, thus verifies

$\mathbf {A} \mathbf {A} ^{-1}=\mathbf {A} ^{-1}\mathbf {A} =\mathbf {I} .$

A matrix that has an inverse is an invertible matrix. Otherwise, it is a singular matrix.

A product of matrices is invertible if and only if each factor is invertible. In this case, one has

$(\mathbf {A} \mathbf {B} )^{-1}=\mathbf {B} ^{-1}\mathbf {A} ^{-1}.$

When R is commutative, and, in particular, when it is a field, the determinant of a product is the product of the determinants. As determinants are scalars, and scalars commute, one has thus

$\det(\mathbf {AB} )=\det(\mathbf {BA} )=\det(\mathbf {A} )\det(\mathbf {B} ).$

The other matrix invariants do not behave as well with products. Nevertheless, if R is commutative, **AB** and **BA** have the same trace, the same characteristic polynomial, and the same eigenvalues with the same multiplicities. However, the eigenvectors are generally different if **AB** ≠ **BA**.

### Powers of a matrix

One may raise a square matrix to any nonnegative integer power multiplying it by itself repeatedly in the same way as for ordinary numbers. That is,

$\mathbf {A} ^{0}=\mathbf {I} ,$

$\mathbf {A} ^{1}=\mathbf {A} ,$

$\mathbf {A} ^{k}=\underbrace {\mathbf {A} \mathbf {A} \cdots \mathbf {A} } _{k{\text{ times}}}.$

Computing the kth power of a matrix needs *k* – 1 times the time of a single matrix multiplication, if it is done with the trivial algorithm (repeated multiplication). As this may be very time consuming, one generally prefers using exponentiation by squaring, which requires less than 2 log2 *k* matrix multiplications, and is therefore much more efficient.

An easy case for exponentiation is that of a diagonal matrix. Since the product of diagonal matrices amounts to simply multiplying corresponding diagonal elements together, the kth power of a diagonal matrix is obtained by raising the entries to the power k:

${\begin{bmatrix}a_{11}&0&\cdots &0\\0&a_{22}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &a_{nn}\end{bmatrix}}^{k}={\begin{bmatrix}a_{11}^{k}&0&\cdots &0\\0&a_{22}^{k}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &a_{nn}^{k}\end{bmatrix}}.$

## Abstract algebra

The definition of matrix product requires that the entries belong to a semiring, and does not require multiplication of elements of the semiring to be commutative. In many applications, the matrix elements belong to a field, although the tropical semiring is also a common choice for graph shortest path problems. Even in the case of matrices over fields, the product is not commutative in general, although it is associative and is distributive over matrix addition. The identity matrices (which are the square matrices whose entries are zero outside of the main diagonal and 1 on the main diagonal) are identity elements of the matrix product. It follows that the *n* × *n* matrices over a ring form a ring, which is noncommutative except if *n* = 1 and the ground ring is commutative.

A square matrix may have a multiplicative inverse, called an inverse matrix. In the common case where the entries belong to a commutative ring R, a matrix has an inverse if and only if its determinant has a multiplicative inverse in R. The determinant of a product of square matrices is the product of the determinants of the factors. The *n* × *n* matrices that have an inverse form a group under matrix multiplication, the subgroups of which are called matrix groups. Many classical groups (including all finite groups) are isomorphic to matrix groups; this is the starting point of the theory of group representations.

Matrices are the morphisms of a category, the category of matrices. The objects are the natural numbers that measure the size of matrices, and the composition of morphisms is matrix multiplication. The source of a morphism is the number of columns of the corresponding matrix, and the target is the number of rows.

## Computational complexity

The matrix multiplication algorithm that results from the definition requires, in the worst case, ⁠ $n^{3}$ ⁠ multiplications and ⁠ $(n-1)n^{2}$ ⁠ additions of scalars to compute the product of two square *n*×*n* matrices. Its computational complexity is therefore ⁠ $O(n^{3})$ ⁠, in a model of computation for which the scalar operations take constant time.

Rather surprisingly, this complexity is not optimal, as shown in 1969 by Volker Strassen, who provided an algorithm, now called Strassen's algorithm, with a complexity of $O(n^{\log _{2}7})\approx O(n^{2.8074}).$ Strassen's algorithm can be parallelized to further improve the performance. As of January 2024, the best peer-reviewed matrix multiplication algorithm is by Virginia Vassilevska Williams, Yinzhan Xu, Zixuan Xu, and Renfei Zhou and has complexity *O*(*n*2.371552). It is not known whether matrix multiplication can be performed in *n*2 + o(1) time. This would be optimal, since one must read the ⁠ $n^{2}$ ⁠ elements of a matrix in order to multiply it with another matrix.

Since matrix multiplication forms the basis for many algorithms, and many operations on matrices even have the same complexity as matrix multiplication (up to a multiplicative constant), the computational complexity of matrix multiplication appears throughout numerical linear algebra and theoretical computer science.

## Generalizations

Other types of products of matrices include:

- Block matrix operations
- Cracovian product, defined as **A** ∧ **B** = **B**T**A**
- Frobenius inner product, the dot product of matrices considered as vectors, or, equivalently the sum of the entries of the Hadamard product
- Hadamard product of two matrices of the same size, resulting in a matrix of the same size, which is the product entry-by-entry
- Kronecker product or tensor product, the generalization to any size of the preceding
- Khatri–Rao product and face-splitting product
- Outer product, also called dyadic product or tensor product of two column matrices, which is $\mathbf {a} \mathbf {b} ^{\mathsf {T}}$
- Scalar multiplication

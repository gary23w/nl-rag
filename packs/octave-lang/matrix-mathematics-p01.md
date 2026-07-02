---
title: "Matrix (mathematics) (part 1/2)"
source: https://en.wikipedia.org/wiki/Matrix_(mathematics)
domain: octave-lang
license: CC-BY-SA-4.0
tags: gnu octave, octave language, octave script
fetched: 2026-07-02
part: 1/2
---

# Matrix (mathematics)

In mathematics, a **matrix** (pl.: **matrices**) is a rectangular array of numbers or other mathematical objects with elements or entries arranged in rows and columns, usually satisfying certain properties of addition and multiplication.

For example, ${\begin{bmatrix}1&9&-13\\20&5&-6\end{bmatrix}}$ denotes a matrix with two rows and three columns. This is often referred to as a "two-by-three matrix", a 2 × 3 matrix, or a matrix of dimension 2 × 3.

In linear algebra, matrices are used as linear maps. In geometry, matrices are used for geometric transformations (for example rotations) and coordinate changes. In numerical analysis, many computational problems are solved by reducing them to a matrix computation, and this often involves computing with matrices of huge dimensions. Matrices are used in most areas of mathematics and scientific fields, either directly, or through their use in geometry and numerical analysis.

*Square matrices*, matrices with the same number of rows and columns, play a major role in matrix theory. The determinant of a square matrix is a number associated with the matrix, which is fundamental for the study of a square matrix; for example, a square matrix is invertible if and only if it has a nonzero determinant and the eigenvalues of a square matrix are the roots of its characteristic polynomial, $\det(\lambda I-A)$ .

**Matrix theory** is the branch of mathematics that focuses on the study of matrices. It was initially a sub-branch of linear algebra, but soon grew to include subjects related to graph theory, algebra, combinatorics and statistics.


## Definition

A matrix is a rectangular array of numbers (or other mathematical objects), called the "entries" of the matrix. Matrices are subject to standard operations such as addition and multiplication. Most commonly, a matrix over a field F is a rectangular array of elements of ⁠ F ⁠. A **real matrix** and a **complex matrix** are matrices whose entries are respectively real numbers or complex numbers. More general types of entries are discussed below. For instance, this is a real matrix: $\mathbf {A} ={\begin{bmatrix}-1.3&0.6\\20.4&5.5\\9.7&-6.2\end{bmatrix}}.$

The numbers (or other objects) in the matrix are called its *entries* or its *elements*. The horizontal and vertical lines of entries in a matrix are respectively called *rows* and *columns*.

### Size

The size of a matrix is defined by the number of rows and columns it contains. There is no limit to the number of rows and columns that a matrix (in the usual sense) can have as long as they are positive integers. A matrix with m rows and n columns is called an m × n matrix, or m-by-n matrix, where m and n are called its **dimensions**. For example, the matrix ${\mathbf {A} }$ above is a 3 × 2 matrix.

Matrices with a single row are called *row matrices* or *row vectors*, and those with a single column are called *column matrices* or *column vectors*. A matrix with the same number of rows and columns is called a *square matrix*. A matrix with an infinite number of rows or columns (or both) is called an *infinite matrix*. In some contexts, such as computer algebra programs, it is useful to consider a matrix with no rows or no columns, called an *empty matrix*.

| Name | Size | Example | Description |
|---|---|---|---|
| Row matrix | $1\times n$ | ${\begin{bmatrix}3&7&2\end{bmatrix}}$ | A matrix with one row and more than one columns, sometimes used to represent a vector |
| Column matrix | $n\times 1$ | ${\begin{bmatrix}4\\1\\8\end{bmatrix}}$ | A matrix with one column and more than one rows, sometimes used to represent a vector |
| Square matrix | $n\times n$ | ${\begin{bmatrix}9&13&5\\1&11&7\\2&6&3\end{bmatrix}}$ | A matrix with the same number of rows and columns, sometimes used to represent a linear transformation from a vector space to itself, such as reflection, rotation, or shearing. |


## Notation

The specifics of symbolic matrix notation vary widely, with some prevailing trends. Matrices are commonly written in square brackets or parentheses, so that an m × n matrix $\mathbf {A}$ is represented as $\mathbf {A} ={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\end{bmatrix}}={\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\end{pmatrix}}.$ This may be abbreviated by writing only a single generic term, possibly along with indices, as in $\mathbf {A} =\left(a_{ij}\right),\quad \left[a_{ij}\right],\quad {\text{or}}\quad \left(a_{ij}\right)_{1\leq i\leq m,\;1\leq j\leq n}$ or $\mathbf {A} =(a_{i,j})_{1\leq i,j\leq n}$ in the case that ⁠ $n=m$ ⁠.

Matrices are usually symbolized using upper-case letters (such as ${\mathbf {A} }$ in the examples above), while the corresponding lower-case letters, with two subscript indices (e.g., ⁠ $a_{11}$ ⁠, or ⁠ $a_{1,1}$ ⁠), represent the entries. In addition to using upper-case letters to symbolize matrices, many authors use a special typographical style, commonly boldface roman (non-italic), to further distinguish matrices from other mathematical objects. An alternative notation involves the use of a double-underline with the variable name, with or without boldface style, as in ⁠ ${\underline {\underline {A}}}$ ⁠.

The entry in the *i*th row and *j*th column of a matrix **A** is sometimes referred to as the ${i,j}$ or $(i,j)$ entry of the matrix, and commonly denoted by $a_{i,j}$ or ⁠ $a_{ij}$ ⁠. Alternative notations for that entry are ${\mathbf {A} [i,j]}$ and ⁠ $\mathbf {A} _{i,j}$ ⁠. For example, the $(1,3)$ entry of the following matrix $\mathbf {A}$ is 5 (also denoted ⁠ $a_{13}$ ⁠, ⁠ $a_{1,3}$ ⁠, $\mathbf {A} [1,3]$ or ⁠ ${\mathbf {A} }_{1,3}$ ⁠): $\mathbf {A} ={\begin{bmatrix}4&-7&\color {red}{5}&0\\-2&0&11&8\\19&1&-3&12\end{bmatrix}}$

Sometimes, the entries of a matrix can be defined by a formula such as ⁠ $a_{i,j}=f(i,j)$ ⁠. For example, each of the entries of the following matrix $\mathbf {A}$ is determined by the formula ⁠ $a_{ij}=i-j$ ⁠. $\mathbf {A} ={\begin{bmatrix}0&-1&-2&-3\\1&0&-1&-2\\2&1&0&-1\end{bmatrix}}$ In this case, the matrix itself is sometimes defined by that formula, within square brackets or double parentheses. For example, the matrix above is defined as ${\mathbf {A} }=[i-j]$ or ⁠ $\mathbf {A} =((i-j))$ ⁠. If matrix size is m × n, the above-mentioned formula $f(i,j)$ is valid for any $i=1,\dots ,m$ and any ⁠ $j=1,\dots ,n$ ⁠. This can be specified separately or indicated using m × n as a subscript. For instance, the matrix $\mathbf {A}$ above is 3 × 4, and can be defined as ${\mathbf {A} }=[i-j](i=1,2,3;j=1,\dots ,4)$ or ⁠ $\mathbf {A} =[i-j]_{3\times 4}$ ⁠.

Some programming languages utilize doubly subscripted arrays (or arrays of arrays) to represent an {m-by-n matrix. Some programming languages start the numbering of array indexes at zero, in which case the entries of an m × n matrix are indexed by $0\leq i\leq m-1$ and ⁠ $0\leq j\leq n-1$ ⁠. This article follows the more common convention in mathematical writing where enumeration starts from 1.

The set of all m-by-n real matrices is often denoted ⁠ ${\mathcal {M}}(m,n)$ ⁠, or ⁠ ${\mathcal {M}}_{m\times n}(\mathbb {R} )$ ⁠. The set of all m × n matrices over another field, or over a ring *R*, is similarly denoted ⁠ ${\mathcal {M}}(m,n,R)$ ⁠, or ⁠ ${\mathcal {M}}_{m\times n}(R)$ ⁠. If *m* = *n*, such as in the case of square matrices, one does not repeat the dimension: ⁠ ${\mathcal {M}}(n,R)$ ⁠, or ⁠ ${\mathcal {M}}_{n}(R)$ ⁠. Often, ⁠ M ⁠, or ⁠ $\operatorname {Mat}$ ⁠, is used in place of ⁠ ${\mathcal {M}}$ ⁠.


## Basic operations

Several basic operations can be applied to matrices. Some, such as *transposition* and *submatrix* do not depend on the nature of the entries. Others, such as *matrix addition*, *scalar multiplication*, *matrix multiplication*, and *row operations* involve operations on matrix entries and therefore require that matrix entries are numbers or belong to a field or a ring.

In this section, it is supposed that matrix entries belong to a fixed ring, which is typically a field of numbers.

### Addition

Matrix addition and subtraction require matrices of a consistent size, and are calculated entrywise. The *sum* **A** + **B** and the difference **A** − **B** of two m × n matrices are:

${\begin{aligned}({\mathbf {A}}+{\mathbf {B}})_{i,j}={\mathbf {A}}_{i,j}+{\mathbf {B}}_{i,j},\quad 1\leq i\leq m,\quad 1\leq j\leq n.\\({\mathbf {A}}-{\mathbf {B}})_{i,j}={\mathbf {A}}_{i,j}-{\mathbf {B}}_{i,j},\quad 1\leq i\leq m,\quad 1\leq j\leq n.\end{aligned}}$

For example,

${\begin{bmatrix}1&3&1\\1&0&0\end{bmatrix}}+{\begin{bmatrix}0&0&5\\7&5&0\end{bmatrix}}={\begin{bmatrix}1+0&3+0&1+5\\1+7&0+5&0+0\end{bmatrix}}={\begin{bmatrix}1&3&6\\8&5&0\end{bmatrix}}$

Familiar properties of numbers extend to these operations on matrices: for example, addition is commutative, that is, the matrix sum does not depend on the order of the summands: **A** + **B** = **B** + **A**.

### Scalar multiplication

The product *c***A** of a number c (also called a scalar in this context) and a matrix **A** is computed by multiplying each entry of **A** by c: $(c{\mathbf {A}})_{i,j}=c\cdot {\mathbf {A}}_{i,j}$ This operation is called *scalar multiplication*, but its result is not named "scalar product" to avoid confusion, since "scalar product" is often used as a synonym for "inner product". For example:

$2\cdot {\begin{bmatrix}1&8&-3\\4&-2&5\end{bmatrix}}={\begin{bmatrix}2\cdot 1&2\cdot 8&2\cdot -3\\2\cdot 4&2\cdot -2&2\cdot 5\end{bmatrix}}={\begin{bmatrix}2&16&-6\\8&-4&10\end{bmatrix}}$

Matrix subtraction is consistent with composition of matrix addition with scalar multiplication by –1:

$\mathbf {A} -\mathbf {B} =\mathbf {A} +(-1)\cdot \mathbf {B}$

### Transpose

The *transpose* of an m × n matrix **A** is the n × m matrix **A**T (also denoted **A**tr or t**A**) formed by turning rows into columns and vice versa: $\left({\mathbf {A}}^{\rm {T}}\right)_{i,j}={\mathbf {A}}_{j,i}.$ For example: ${\begin{bmatrix}1&2&3\\0&-6&7\end{bmatrix}}^{\mathrm {T} }={\begin{bmatrix}1&0\\2&-6\\3&7\end{bmatrix}}$

The transpose is compatible with addition and scalar multiplication, as expressed by (*c***A**)T = *c*(**A**T) and (**A** + **B**)T = **A**T + **B**T. Finally, (**A**T)T = **A**.

### Matrix multiplication

*Multiplication* of two matrices corresponds to the composition of linear transformations represented by each matrix. It is defined if and only if the number of columns of the left matrix is the same as the number of rows of the right matrix. If **A** is an m × n matrix and **B** is an n × p matrix, then their *matrix product* **AB** is the m × p matrix whose entries are given by the dot product of the corresponding row of **A** and the corresponding column of **B**: $[\mathbf {AB} ]_{i,j}=a_{i,1}b_{1,j}+a_{i,2}b_{2,j}+\cdots +a_{i,n}b_{n,j}=\sum _{r=1}^{n}a_{i,r}b_{r,j},$ where 1 ≤ *i* ≤ *m* and 1 ≤ *j* ≤ *p*. For example, the underlined entry 2340 in the product is calculated as (2 × 1000) + (3 × 100) + (4 × 10) = 2340: ${\begin{aligned}{\begin{bmatrix}{\underline {2}}&{\underline {3}}&{\underline {4}}\\1&0&0\\\end{bmatrix}}{\begin{bmatrix}0&{\underline {1000}}\\1&{\underline {100}}\\0&{\underline {10}}\\\end{bmatrix}}&={\begin{bmatrix}3&{\underline {2340}}\\0&1000\\\end{bmatrix}}.\end{aligned}}$

Matrix multiplication satisfies the rules (**AB**)**C** = **A**(**BC**) (associativity), and (**A** + **B**)**C** = **AC** + **BC** as well as **C**(**A** + **B**) = **CA** + **CB** (left and right distributivity), whenever the size of the matrices is such that the various products are defined. The product **AB** may be defined without **BA** being defined, namely if **A** and **B** are m × n and n × k matrices, respectively, and *m* ≠ *k*. Even if both products are defined, they generally need not be equal, that is: ${\mathbf {AB}}\neq {\mathbf {BA}}.$

In other words, matrix multiplication is not commutative, in marked contrast to (rational, real, or complex) numbers, whose product is independent of the order of the factors. An example of two matrices not commuting with each other is: ${\begin{bmatrix}1&2\\3&4\\\end{bmatrix}}{\begin{bmatrix}0&1\\0&0\\\end{bmatrix}}={\begin{bmatrix}0&1\\0&3\\\end{bmatrix}},$ whereas ${\begin{bmatrix}0&1\\0&0\\\end{bmatrix}}{\begin{bmatrix}1&2\\3&4\\\end{bmatrix}}={\begin{bmatrix}3&4\\0&0\\\end{bmatrix}}.$

Besides the ordinary matrix multiplication just described, other less frequently used operations on matrices that can be considered forms of multiplication also exist, such as the Hadamard product and the Kronecker product. They arise in solving matrix equations such as the Sylvester equation.

### Row operations

There are three types of row operations:

1. row addition, that is, adding a row to another.
2. row multiplication, that is, multiplying all entries of a row by a non-zero constant;
3. row switching, that is, interchanging two rows of a matrix;

These operations are used in several ways, including solving linear equations and finding matrix inverses with Gauss elimination and Gauss–Jordan elimination, respectively.

### Submatrix

A **submatrix** of a matrix is a matrix obtained by deleting any collection of rows or columns or both. For example, from the following 3 × 4 matrix, we can construct a 2 × 3 submatrix by removing row 3 and column 2: $\mathbf {A} ={\begin{bmatrix}1&\color {red}{2}&3&4\\5&\color {red}{6}&7&8\\\color {red}{9}&\color {red}{10}&\color {red}{11}&\color {red}{12}\end{bmatrix}}\rightarrow {\begin{bmatrix}1&3&4\\5&7&8\end{bmatrix}}.$

The minors and cofactors of a matrix are found by computing the determinant of certain submatrices.

A **principal submatrix** is a square submatrix obtained by removing certain rows and columns. The definition varies from author to author. According to some authors, a principal submatrix is a submatrix in which the set of row indices that remain is the same as the set of column indices that remain. Other authors define a principal submatrix as one in which the first k rows and columns, for some number k, are the ones that remain; this type of submatrix has also been called a **leading principal submatrix**.


## Linear equations

Matrices can be used to compactly write and work with multiple linear equations, that is, systems of linear equations. For example, if **A** is an m × n matrix, **x** designates a column vector (that is, n × 1 matrix) of n variables *x*1, *x*2, ..., *x**n*, and **b** is an m × 1 column vector, then the matrix equation $\mathbf {Ax} =\mathbf {b}$ is equivalent to the system of linear equations ${\begin{aligned}a_{1,1}x_{1}+a_{1,2}x_{2}+&\cdots +a_{1,n}x_{n}=b_{1}\\&\ \ \vdots \\a_{m,1}x_{1}+a_{m,2}x_{2}+&\cdots +a_{m,n}x_{n}=b_{m}\end{aligned}}$

Using matrices, this can be solved more compactly than would be possible by writing out all the equations separately. If *n* = *m* and the equations are independent, then this can be done by writing $\mathbf {x} =\mathbf {A} ^{-1}\mathbf {b}$ where **A**−1 is the inverse matrix of **A**. If **A** has no inverse, solutions—if any—can be found using its generalized inverse.


## Linear transformations

Matrices and matrix multiplication reveal their essential features when related to *linear transformations*, also known as *linear maps*. A real m-by-n matrix **A** gives rise to a linear transformation $\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ mapping each vector **x** in ⁠ $\mathbb {R} ^{n}$ ⁠ to the (matrix) product **Ax**, which is a vector in ⁠ $\mathbb {R} ^{m}.$ ⁠ Conversely, each linear transformation $f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ arises from a unique m-by-n matrix **A**: explicitly, the (*i*, *j*)-entry of **A** is the ith coordinate of *f* (**e***j*), where **e***j* = (0, ..., 0, 1, 0, ..., 0) is the unit vector with 1 in the jth position and 0 elsewhere. The matrix **A** is said to represent the linear map f, and **A** is called the *transformation matrix* of f.

For example, the 2 × 2 matrix $\mathbf {A} ={\begin{bmatrix}a&c\\b&d\end{bmatrix}}$ can be viewed as the transform of the unit square into a parallelogram with vertices at (0, 0), (*a*, *b*), (*a* + *c*, *b* + *d*), and (*c*, *d*). The parallelogram pictured at the right is obtained by multiplying **A** with each of the column vectors ⁠ $\left[{\begin{smallmatrix}0\\0\end{smallmatrix}}\right]$ ⁠, ⁠ $\left[{\begin{smallmatrix}1\\0\end{smallmatrix}}\right]$ ⁠, ⁠ $\left[{\begin{smallmatrix}1\\1\end{smallmatrix}}\right]$ ⁠, and ⁠ $\left[{\begin{smallmatrix}0\\1\end{smallmatrix}}\right]$ ⁠ in turn. These vectors define the vertices of the unit square. The following table shows several 2 × 2 real matrices with the associated linear maps of ⁠ $\mathbb {R} ^{2}$ ⁠. The blue original is mapped to the green grid and shapes. The origin (0, 0) is marked with a black point.

| Horizontal shear with *m* = 1.25. | Reflection through the vertical axis | Squeeze mapping with *r* = 3/2 | Scaling by a factor of 3/2 | Rotation by π/6 = 30° |
|---|---|---|---|---|
| ${\begin{bmatrix}1&1.25\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}-1&0\\0&1\end{bmatrix}}$ | ${\begin{bmatrix}{\frac {3}{2}}&0\\0&{\frac {2}{3}}\end{bmatrix}}$ | ${\begin{bmatrix}{\frac {3}{2}}&0\\0&{\frac {3}{2}}\end{bmatrix}}$ | ${\begin{bmatrix}\cos \left({\frac {\pi }{6}}\right)&-\sin \left({\frac {\pi }{6}}\right)\\\sin \left({\frac {\pi }{6}}\right)&\cos \left({\frac {\pi }{6}}\right)\end{bmatrix}}$ |
|   |   |   |   |   |

Under the 1-to-1 correspondence between matrices and linear maps, matrix multiplication corresponds to composition of maps: if a k-by-m matrix **B** represents another linear map ⁠ $g:\mathbb {R} ^{m}\to \mathbb {R} ^{k}$ ⁠, then the composition *g* ∘ *f* is represented by **BA** since $(g\circ f)({\mathbf {x}})=g(f({\mathbf {x}}))=g({\mathbf {Ax}})={\mathbf {B}}({\mathbf {Ax}})=({\mathbf {BA}}){\mathbf {x}}.$

The last equality follows from the above-mentioned associativity of matrix multiplication.

The rank of a matrix **A** is the maximum number of linearly independent row vectors of the matrix, which is the same as the maximum number of linearly independent column vectors. Equivalently it is the dimension of the image of the linear map represented by **A**. The rank–nullity theorem states that the dimension of the kernel of a matrix plus the rank equals the number of columns of the matrix.


## Square matrix

A square matrix is a matrix with the same number of rows and columns. An n-by-n matrix is known as a square matrix of order n. Any two square matrices of the same order can be added and multiplied. The entries aii form the main diagonal of a square matrix. They lie on the imaginary line running from the top left corner to the bottom right corner of the matrix.

Square matrices of a given dimension form a noncommutative ring, which is one of the most common examples of a noncommutative ring.

### Main types

| Name | Example with *n* = 3 |
|---|---|
| Diagonal matrix | ${\begin{bmatrix}a_{11}&0&0\\0&a_{22}&0\\0&0&a_{33}\\\end{bmatrix}}$ |
| Lower triangular matrix | ${\begin{bmatrix}a_{11}&0&0\\a_{21}&a_{22}&0\\a_{31}&a_{32}&a_{33}\\\end{bmatrix}}$ |
| Upper triangular matrix | ${\begin{bmatrix}a_{11}&a_{12}&a_{13}\\0&a_{22}&a_{23}\\0&0&a_{33}\\\end{bmatrix}}$ |

#### Diagonal and triangular matrix

If all entries of **A** below the main diagonal are zero, **A** is called an *upper triangular matrix*. Similarly, if all entries of **A** above the main diagonal are zero, **A** is called a *lower triangular matrix*. If all entries outside the main diagonal are zero, **A** is called a diagonal matrix.

#### Identity matrix

The *identity matrix* **I***n* of size n is the n-by-n matrix in which all the elements on the main diagonal are equal to 1 and all other elements are equal to 0, for example, ${\begin{aligned}\mathbf {I} _{1}&={\begin{bmatrix}1\end{bmatrix}},\\[4pt]\mathbf {I} _{2}&={\begin{bmatrix}1&0\\0&1\end{bmatrix}},\\[4pt]\vdots &\\[4pt]\mathbf {I} _{n}&={\begin{bmatrix}1&0&\cdots &0\\0&1&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &1\end{bmatrix}}\end{aligned}}$ It is a square matrix of order n, and also a special kind of diagonal matrix. It is called an identity matrix because multiplication with it leaves a matrix unchanged: ${\mathbf {AI}}_{n}={\mathbf {I}}_{m}{\mathbf {A}}={\mathbf {A}}$ for any m-by-n matrix **A**.

A scalar multiple of an identity matrix is called a *scalar* matrix.

#### Symmetric or skew-symmetric matrix

A square matrix **A** that is equal to its transpose, that is, **A** = **A**T, is a symmetric matrix. If instead, **A** is equal to the negative of its transpose, that is, **A** = −**A**T, then **A** is a skew-symmetric matrix. In complex matrices, symmetry is often replaced by the concept of Hermitian matrices, which satisfies **A**∗ = **A**, where the star or asterisk denotes the conjugate transpose of the matrix, that is, the transpose of the complex conjugate of **A**.

By the spectral theorem, real symmetric matrices and complex Hermitian matrices have an eigenbasis; that is, every vector is expressible as a linear combination of eigenvectors. In both cases, all eigenvalues are real. This theorem can be generalized to infinite-dimensional situations related to matrices with infinitely many rows and columns.

#### Invertible matrix and its inverse

A square matrix **A** is called *invertible* or *non-singular* if there exists a matrix **B** such that ${\mathbf {AB}}={\mathbf {BA}}={\mathbf {I}}_{n},$ where **I***n* is the n × n identity matrix with 1 for each entry on the main diagonal and 0 elsewhere. If **B** exists, it is unique and is called the *inverse matrix* of **A**, denoted **A**−1.

There are many algorithms for testing whether a square matrix is invertible, and, if it is, computing its inverse. One of the oldest, which is still in common use is Gaussian elimination.

#### Definite matrix

| Positive definite matrix | Indefinite matrix |
|---|---|
| ${\begin{bmatrix}{\frac {1}{4}}&0\\0&1\\\end{bmatrix}}$ | ${\begin{bmatrix}{\frac {1}{4}}&0\\0&-{\frac {1}{4}}\end{bmatrix}}$ |
| $Q(x,y)={\frac {1}{4}}x^{2}+y^{2}$ | $Q(x,y)={\frac {1}{4}}x^{2}-{\frac {1}{4}}y^{2}$ |
| Points such that ${\textstyle Q(x,y)=1}$ (Ellipse) | Points such that ${\textstyle Q(x,y)=1}$ (Hyperbola) |

A symmetric real matrix **A** is called *positive-definite* if the associated quadratic form $f({\mathbf {x}})={\mathbf {x}}^{\rm {T}}{\mathbf {Ax}}$ has a positive value for every nonzero vector **x** in ⁠ $\mathbb {R} ^{n}$ ⁠. If *f*(**x**) yields only negative values then **A** is *negative-definite*; if f does produce both negative and positive values then **A** is *indefinite*. If the quadratic form f yields only non-negative values (positive or zero), the symmetric matrix is called *positive-semidefinite* (or if only non-positive values, then negative-semidefinite); hence the matrix is indefinite precisely when it is neither positive-semidefinite nor negative-semidefinite.

A symmetric matrix is positive-definite if and only if all its eigenvalues are positive, that is, the matrix is positive-semidefinite and it is invertible. The table at the right shows two possibilities for 2-by-2 matrices. The eigenvalues of a diagonal matrix are simply the entries along the diagonal, and so in these examples, the eigenvalues can be read directly from the matrices themselves. The first matrix has two eigenvalues that are both positive, while the second has one that is positive and another that is negative.

Allowing as input two different vectors instead yields the bilinear form associated to **A**: $B_{\mathbf {A}}({\mathbf {x}},{\mathbf {y}})={\mathbf {x}}^{\rm {T}}{\mathbf {Ay}}.$

In the case of complex matrices, the same terminology and results apply, with *symmetric matrix*, *quadratic form*, *bilinear form*, and *transpose* **x**T replaced respectively by Hermitian matrix, Hermitian form, sesquilinear form, and conjugate transpose **x**H.

#### Orthogonal matrix

An *orthogonal matrix* is a square matrix with real entries whose columns and rows are orthogonal unit vectors (that is, orthonormal vectors). Equivalently, a matrix **A** is orthogonal if its transpose is equal to its inverse: $\mathbf {A} ^{\mathrm {T} }=\mathbf {A} ^{-1},\,$ which entails $\mathbf {A} ^{\mathrm {T} }\mathbf {A} =\mathbf {A} \mathbf {A} ^{\mathrm {T} }=\mathbf {I} _{n},$ where **I***n* is the identity matrix of size n.

An orthogonal matrix **A** is necessarily invertible (with inverse **A**−1 = **A**T), unitary (**A**−1 = **A***), and normal (**A*****A** = **AA***). The determinant of any orthogonal matrix is either +1 or −1. A *special orthogonal matrix* is an orthogonal matrix with determinant +1. As a linear transformation, every orthogonal matrix with determinant +1 is a pure rotation without reflection, i.e., the transformation preserves the orientation of the transformed structure, while every orthogonal matrix with determinant −1 reverses the orientation, i.e., is a composition of a pure reflection and a (possibly null) rotation. The identity matrices have determinant 1 and are pure rotations by an angle zero.

The complex analog of an orthogonal matrix is a unitary matrix.

### Main operations

#### Trace

The trace, tr(**A**) of a square matrix **A** is the sum of its diagonal entries. While matrix multiplication is not commutative as mentioned above, the trace of the product of two matrices is independent of the order of the factors: $\operatorname {tr} (\mathbf {AB} )=\operatorname {tr} (\mathbf {BA} ).$ This is immediate from the definition of matrix multiplication: $\operatorname {tr} (\mathbf {AB} )=\sum _{i=1}^{m}\sum _{j=1}^{n}a_{ij}b_{ji}=\operatorname {tr} (\mathbf {BA} ).$ It follows that the trace of the product of more than two matrices is independent of cyclic permutations of the matrices; however, this does not in general apply for arbitrary permutations. For example, tr(**ABC**) ≠ tr(**BAC**), in general. Also, the trace of a matrix is equal to that of its transpose, that is, $\operatorname {tr} ({\mathbf {A}})=\operatorname {tr} ({\mathbf {A}}^{\rm {T}}).$

#### Determinant

The *determinant* of a square matrix **A** (denoted det(**A**) or |**A**|) is a number encoding certain properties of the matrix. A matrix is invertible if and only if its determinant is nonzero. Its absolute value equals the area (in ⁠ $\mathbb {R} ^{2}$ ⁠) or volume (in ⁠ $\mathbb {R} ^{3}$ ⁠) of the image of the unit square (or cube), while its sign corresponds to the orientation of the corresponding linear map: the determinant is positive if and only if the orientation is preserved.

The determinant of 2 × 2 matrices is given by $\det {\begin{bmatrix}a&b\\c&d\end{bmatrix}}=ad-bc.$ The determinant of 3 × 3 matrices involves six terms (rule of Sarrus). The more lengthy Leibniz formula generalizes these two formulae to all dimensions.

The determinant of a product of square matrices equals the product of their determinants: $\det({\mathbf {AB}})=\det({\mathbf {A}})\cdot \det({\mathbf {B}}),$ or using alternate notation: $|{\mathbf {AB}}|=|{\mathbf {A}}|\cdot |{\mathbf {B}}|.$ Adding a multiple of any row to another row, or a multiple of any column to another column, does not change the determinant. Interchanging two rows or two columns affects the determinant by multiplying it by −1. Using these operations, any matrix can be transformed to a lower (or upper) triangular matrix, and for such matrices, the determinant equals the product of the entries on the main diagonal; this provides a method to calculate the determinant of any matrix. Finally, the Laplace expansion expresses the determinant in terms of minors, that is, determinants of smaller matrices. This expansion can be used for a recursive definition of determinants (taking as starting case the determinant of a 1 × 1 matrix, which is its unique entry, or even the determinant of a 0 × 0 matrix, which is 1), that can be seen to be equivalent to the Leibniz formula. Determinants can be used to solve linear systems using Cramer's rule, where the division of the determinants of two related square matrices equates to the value of each of the system's variables.

#### Eigenvalues and eigenvectors

A number ${\textstyle \lambda }$ and a nonzero vector **v** satisfying $\mathbf {A} \mathbf {v} =\lambda \mathbf {v}$ are called an *eigenvalue* and an *eigenvector* of **A**, respectively. The number λ is an eigenvalue of an n × n matrix **A** if and only if (**A** − *λ***I***n*) is not invertible, which is equivalent to $\det(\mathbf {A} -\lambda \mathbf {I} )=0.$ The polynomial *p***A** in an indeterminate X given by evaluation of the determinant det(*X***I***n* − **A**) is called the characteristic polynomial of **A**. It is a monic polynomial of degree n. Therefore the polynomial equation *p***A**(*λ*) = 0 has at most n different solutions, that is, eigenvalues of the matrix. They may be complex even if the entries of **A** are real. According to the Cayley–Hamilton theorem, *p***A**(**A**) = **0**, that is, the result of substituting the matrix itself into its characteristic polynomial yields the zero matrix.


## Computational aspects

Matrix calculations can be often performed with different techniques. Many problems can be solved by both direct algorithms and iterative approaches. For example, the eigenvectors of a square matrix can be obtained by finding a sequence of vectors **x***n* converging to an eigenvector when n tends to infinity.

To choose the most appropriate algorithm for each specific problem, it is important to determine both the effectiveness and precision of all the available algorithms. The domain studying these matters is called numerical linear algebra. As with other numerical situations, two main aspects are the complexity of algorithms and their numerical stability.

Determining the complexity of an algorithm means finding upper bounds or estimates of how many elementary operations such as additions and multiplications of scalars are necessary to perform some algorithm, for example, multiplication of matrices. Calculating the matrix product of two n-by-n matrices using the definition given above needs *n*3 multiplications, since for any of the *n*2 entries of the product, n multiplications are necessary. The Strassen algorithm outperforms this "naive" algorithm; it needs only *n*2.807 multiplications. Theoretically faster but impractical matrix multiplication algorithms have been developed, as have speedups to this problem using parallel algorithms or distributed computation systems such as MapReduce.

In many practical situations, additional information about the matrices involved is known. An important case concerns sparse matrices, that is, matrices whose entries are mostly zero. There are specifically adapted algorithms for, say, solving linear systems **Ax** = **b** for sparse matrices **A**, such as the conjugate gradient method.

An algorithm is, roughly speaking, numerically stable if little deviations in the input values do not lead to big deviations in the result. For example, one can calculate the inverse of a matrix by computing its adjugate matrix: ${\mathbf {A}}^{-1}=\operatorname {adj} ({\mathbf {A}})/\det({\mathbf {A}}).$ However, this may lead to significant rounding errors if the determinant of the matrix is very small. The norm of a matrix can be used to capture the conditioning of linear algebraic problems, such as computing a matrix's inverse.


## Decomposition

There are several methods to render matrices into a more easily accessible form. They are generally referred to as *matrix decomposition* or *matrix factorization* techniques. These techniques are of interest because they can make computations easier.

The LU decomposition factors matrices as a product of lower (**L**) and an upper triangular matrices (**U**). Once this decomposition is calculated, linear systems can be solved more efficiently by a simple technique called forward and back substitution. Likewise, inverses of triangular matrices are algorithmically easier to calculate. The *Gaussian elimination* is a similar algorithm; it transforms any matrix to row echelon form. Both methods proceed by multiplying the matrix by suitable elementary matrices, which correspond to permuting rows or columns and adding multiples of one row to another row. Singular value decomposition (SVD) expresses any matrix **A** as a product **UDV**∗, where **U** and **V** are unitary matrices and **D** is a diagonal matrix.

The eigendecomposition or *diagonalization* expresses **A** as a product **VDV**−1, where **D** is a diagonal matrix and **V** is a suitable invertible matrix. If **A** can be written in this form, it is called diagonalizable. More generally, and applicable to all matrices, the Jordan decomposition transforms a matrix into Jordan normal form, that is to say matrices whose only nonzero entries are the eigenvalues *λ*1 to λn of **A**, placed on the main diagonal and possibly entries equal to one directly above the main diagonal, as shown at the right. Given the eigendecomposition, the nth power of **A** (that is, n-fold iterated matrix multiplication) can be calculated via ${\mathbf {A}}^{n}=({\mathbf {VDV}}^{-1})^{n}={\mathbf {VDV}}^{-1}{\mathbf {VDV}}^{-1}\ldots {\mathbf {VDV}}^{-1}={\mathbf {VD}}^{n}{\mathbf {V}}^{-1}$ and the power of a diagonal matrix can be calculated by taking the corresponding powers of the diagonal entries, which is much easier than doing the exponentiation for **A** instead. This can be used to compute the matrix exponential *e***A**, a need frequently arising in solving linear differential equations, matrix logarithms and square roots of matrices. To avoid numerically ill-conditioned situations, further algorithms such as the Schur decomposition can be employed.


## Abstract algebraic aspects and generalizations

Matrices can be generalized in different ways. Abstract algebra uses matrices with entries in more general fields or even rings, while linear algebra codifies properties of matrices in the notion of linear maps. It is possible to consider matrices with infinitely many columns and rows. Another extension is tensors, which can be seen as higher-dimensional arrays of numbers, as opposed to vectors, which can often be realized as sequences of numbers, while matrices are rectangular or two-dimensional arrays of numbers. Matrices, subject to certain requirements tend to form groups known as matrix groups. Similarly under certain conditions matrices form rings known as matrix rings. Though the product of matrices is not in general commutative, certain matrices form fields sometimes called matrix fields. (However the term "matrix field" is ambiguous, also referring to certain forms of physical fields that continuously map points of some space to matrices.) In general, matrices over any ring and their multiplication can be represented as the arrows and composition of arrows in a category, the category of matrices over that ring. The objects of this category are natural numbers, representing the dimensions of the matrices.

### Matrices with entries in a field or ring

This article focuses on matrices whose entries are real or complex numbers. However, matrices can be considered with much more general types of entries than real or complex numbers. As a first step of generalization, any field, that is, a set where addition, subtraction, multiplication, and division operations are defined and well-behaved, may be used instead of ⁠ $\mathbb {R}$ ⁠ or ⁠ $\mathbb {C}$ ⁠, for example rational numbers or finite fields. For example, coding theory makes use of matrices over finite fields. Wherever eigenvalues are considered, as these are roots of a polynomial, they may exist only in a larger field than that of the entries of the matrix. For instance, they may be complex in the case of a matrix with real entries. The possibility to reinterpret the entries of a matrix as elements of a larger field (for example, to view a real matrix as a complex matrix whose entries happen to be all real) then allows considering each square matrix to possess a full set of eigenvalues. Alternatively one can consider only matrices with entries in an algebraically closed field, such as ⁠ $\mathbb {C} ,$ ⁠ from the outset.

Matrices whose entries are polynomials, and more generally, matrices with entries in a ring R are widely used in mathematics. Rings are a more general notion than fields in that a division operation need not exist. The very same addition and multiplication operations of matrices extend to this setting, too. The set M(*n*, *R*) (also denoted M*n*(R)) of all square n-by-n matrices over R is a ring called matrix ring, isomorphic to the endomorphism ring of the left R-module Rn. If the ring R is commutative, that is, its multiplication is commutative, then the ring M(*n*, *R*) is also an associative algebra over *R*. The determinant of square matrices over a commutative ring R can still be defined using the Leibniz formula; such a matrix is invertible if and only if its determinant is invertible in R, generalizing the situation over a field F, where every nonzero element is invertible. Matrices over superrings are called supermatrices.

Matrices do not always have all their entries in the same ring – or even in any ring at all. One special but common case is block matrices, which may be considered as matrices whose entries themselves are matrices. The entries need not be square matrices, and thus need not be members of any ring; but in order to multiply them, their sizes must fulfill certain conditions: each pair of submatrices that are multiplied in forming the overall product must have compatible sizes.

### Relationship to linear maps

Linear maps $\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ are equivalent to m-by-n matrices, as described above. More generally, any linear map *f* : *V* → *W* between finite-dimensional vector spaces can be described by a matrix **A** = (*aij*), after choosing bases **v**1, ..., **v***n* of V, and **w**1, ..., **w***m* of W (so n is the dimension of V and m is the dimension of W), which is such that $f(\mathbf {v} _{j})=\sum _{i=1}^{m}a_{i,j}\mathbf {w} _{i}\qquad {\mbox{for}}\ j=1,\ldots ,n.$ In other words, column j of **A** expresses the image of **v***j* in terms of the basis vectors **w***i* of W; thus this relation uniquely determines the entries of the matrix **A**. The matrix depends on the choice of the bases: different choices of bases give rise to different, but equivalent matrices. Many of the above concrete notions can be reinterpreted in this light, for example, the transpose matrix **A**T describes the transpose of the linear map given by **A**, concerning the dual bases.

These properties can be restated more naturally: the category of matrices with entries in a field k with multiplication as composition is equivalent to the category of finite-dimensional vector spaces and linear maps over this field.

More generally, the set of m × n matrices can be used to represent the R-linear maps between the free modules Rm and Rn for an arbitrary ring R with unity. When *n* = *m* composition of these maps is possible, and this gives rise to the matrix ring of n × n matrices representing the endomorphism ring of Rn.

### Matrix groups

A group is a mathematical structure consisting of a set of objects together with a binary operation, that is, an operation combining any two objects to a third, subject to certain requirements. A group in which the objects are invertible ⁠ $n\times n$ ⁠ matrices and the group operation is matrix multiplication is called a *matrix group* of degree ⁠ n ⁠. Every such matrix group is a subgroup of (that is, a smaller group contained within) the group of *all* invertible ⁠ $n\times n$ ⁠ matrices, the general linear group of degree ⁠ n ⁠.

Any property of square matrices that is preserved under matrix products and inverses can be used to define a matrix group. For example, the set of all ⁠ $n\times n$ ⁠ matrices whose determinant is 1 form a group called the special linear group of degree ⁠ n ⁠. The set of orthogonal matrices, determined by the condition ${\mathbf {M}}^{\rm {T}}{\mathbf {M}}={\mathbf {I}},$ form the orthogonal group. Every orthogonal matrix has determinant 1 or −1. Orthogonal matrices with determinant 1 form a group called the *special orthogonal group*.

Every finite group is isomorphic to a matrix group, as one can see by considering the regular representation of the symmetric group. General groups can be studied using matrix groups, which are comparatively well understood, using representation theory.

### Infinite matrices

It is also possible to consider matrices with infinitely many rows and columns. The basic operations introduced above are defined the same way in this case. Matrix multiplication, however, and all operations stemming therefrom are only meaningful when restricted to certain matrices, since the sum featuring in the above definition of the matrix product will contain an infinity of summands. An easy way to circumvent this issue is to restrict to *finitary matrices* all of whose rows (or columns) contain only finitely many nonzero terms. As in the finite case (see above), where matrices describe linear maps, infinite matrices can be used to describe operators on Hilbert spaces, where convergence and continuity questions arise. However, the explicit point of view of matrices tends to obfuscate the matter, and the abstract and more powerful tools of functional analysis are used instead, by relating matrices to linear maps (as in the finite case above), but imposing additional convergence and continuity constraints.

### Empty matrix

An *empty matrix* is a matrix in which the number of rows or columns (or both) is zero. Empty matrices can be a useful base case for certain recursive constructions, and can help to deal with maps involving the zero vector space. For example, if **A** is a 3 × 0 matrix and **B** is a 0 × 3 matrix, then **AB** is the 3 × 3 zero matrix corresponding to the null map from a 3-dimensional space V to itself, while **BA** is a 0 × 0 matrix. There is no common notation for empty matrices, but most computer algebra systems allow creating and computing with them. The determinant of the 0 × 0 matrix is conventionally defined to be 1, consistent with the empty product occurring in the Leibniz formula for the determinant. This value is also needed for consistency with the 2 × 2 case of the Desnanot–Jacobi identity relating determinants to the determinants of smaller matrices.

### Matrices with entries in a semiring

A semiring is similar to a ring, but elements need not have additive inverses, therefore one cannot do subtraction freely there. The definition of addition and multiplication of matrices with entries in a ring applies to matrices with entries in a semiring without modification. Matrices of fixed size with entries in a semiring form a commutative monoid $\operatorname {Mat} (m,n;R)$ under addition. Square matrices of fixed size with entries in a semiring form a semiring $\operatorname {Mat} (n;R)$ under addition and multiplication.

The determinant of an n × n square matrix M with entries in a commutative semiring R cannot be defined in general because the definition would involve additive inverses of semiring elements. What plays its role instead is the pair of positive and negative determinants

$\det \nolimits _{+}M=\sum _{\sigma \in \operatorname {Alt} (n)}M_{1\sigma (1)}\cdots M_{n\sigma (n)}$

$\det \nolimits _{-}M=\sum _{\sigma \in \operatorname {Sym} (n)\setminus \operatorname {Alt} (n)}M_{1\sigma (1)}\cdots M_{n\sigma (n)}$

where the sums are taken over even permutations and odd permutations, respectively.

### Matrices with entries in a category

Matrices and their multiplication can be defined with entries objects of a category equipped with a "tensor product" similar to multiplication in a ring, having coproducts similar to addition in a ring, in that the former is distributive over the latter. However, the multiplication thus defined may be only associative in a sense weaker than usual. These are part of a bigger structure called the *bicategory of matrices*. The complete description of the above summary for interested readers follows.

Let $({\mathcal {C}},\otimes ,I)$ be a monoidal category satisfying the following two conditions:

- All (small) coproducts exist; in particular, let $\varnothing$ be an initial object.
- The functor $\otimes$ is distributive over coproducts; i.e., for all object X and a family of objects $(Y_{i})_{i\in I}$ in ${\mathcal {C}}$ , the canonical ${\mathcal {C}}$ -morphisms $\coprod _{i\in I}(X\otimes Y_{i})\to X\otimes \coprod _{i\in I}Y_{i}$ $\coprod _{i\in I}(Y_{i}\otimes X)\to \left(\coprod _{i\in I}Y_{i}\right)\otimes X$ are isomorphisms. In particular, the canonical morphisms $\varnothing \to X\otimes \varnothing$ and $\varnothing \to \varnothing \otimes X$ are isomorphisms.

Then, the bicategory of ${\mathcal {C}}$ -matrices $\operatorname {Mat} ({\mathcal {C}})$ is as follows:

- The objects are the sets.
- A 1-morphism $M\colon A\to B$ is a map $M\colon A\times B\to \operatorname {Ob} ({\mathcal {C}})$ ; this is just a matrix over ${\mathcal {C}}$ .
  - The composition of 1-morphisms $M\colon A\to B$ and $N\colon B\to C$ , which can be understood as matrix multiplication, is $(N\circ M)(a,c)=\coprod _{b\in B}M(a,b)\otimes N(b,c).$
  - The identity 1-morphism on A is $\operatorname {id} _{A}(a,b)={\begin{cases}I&a=b\\\varnothing &a\neq b\end{cases}}.$
- A 2-morphism between 1-morphisms $M,N\colon A\to B$ is a family of ${\mathcal {C}}$ -morphisms $(f_{ab}\colon M(a,b)\to N(a,b))_{(a,b)\in A\times B}$ . The definition of vertical and horizontal composition of 2-morphisms is natural: the vertical composition is componentwise composition of ${\mathcal {C}}$ -morphisms; the horizontal composition is that derived from the functoriality of $\otimes$ and the universal property of coproducts.

In general, the bicategory of matrices need not be a strict 2-category. For example, the composition of 1-morphisms may not be associative in the usual strict sense, but only up to coherent isomorphism.

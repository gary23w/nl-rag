---
title: "Determinant (part 1/2)"
source: https://en.wikipedia.org/wiki/Determinant
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 1/2
---

# Determinant

In mathematics, the **determinant** is a scalar-valued function of the entries of a square matrix. The determinant of a matrix *A* is commonly denoted det(*A*), det *A*, or |*A*|. Its value characterizes some properties of the matrix and the linear map represented, on a given basis, by the matrix. In particular, the determinant is nonzero if and only if the matrix is invertible and the corresponding linear map is an isomorphism. However, if the determinant is zero, the matrix is referred to as singular, meaning it does not have an inverse.

The determinant is completely determined by the two following properties: the determinant of a product of matrices is the product of their determinants, and the determinant of a triangular matrix is the product of its diagonal entries.

The determinant of a 2 × 2 matrix is

${\begin{vmatrix}a&b\\c&d\end{vmatrix}}=ad-bc,$

and the determinant of a 3 × 3 matrix is

${\begin{vmatrix}a&b&c\\d&e&f\\g&h&i\end{vmatrix}}=aei+bfg+cdh-ceg-bdi-afh.$

The determinant of an *n* × *n* matrix can be defined in several equivalent ways, the most common being the Leibniz formula, which expresses the determinant as a sum of $n!$ (the factorial of n) signed products of matrix entries. It can be computed by the Laplace expansion, which expresses the determinant as a linear combination of determinants of submatrices, or with Gaussian elimination, which allows computing a row echelon form with the same determinant, equal to the product of the diagonal entries of the row echelon form.

Determinants can also be defined by some of their properties. Namely, the determinant is the unique function defined on the *n* × *n* matrices that has the four following properties:

1. The determinant of the identity matrix is 1.
2. The exchange of two rows multiplies the determinant by −1.
3. Multiplying a row by a number multiplies the determinant by this number.
4. Adding a multiple of one row to another row does not change the determinant.

The above properties relating to rows (properties 2–4) may be replaced by the corresponding statements with respect to columns.

The determinant is invariant under matrix similarity. This implies that, given a linear endomorphism of a finite-dimensional vector space, the determinant of the matrix that represents it on a basis does not depend on the chosen basis. This allows defining the *determinant* of a linear endomorphism, which does not depend on the choice of a coordinate system.

Determinants occur throughout mathematics. For example, a matrix is often used to represent the coefficients in a system of linear equations, and determinants can be used to solve these equations (Cramer's rule), although other methods of solution are computationally much more efficient. Determinants are used for defining the characteristic polynomial of a square matrix, whose roots are the eigenvalues. In geometry, the signed n-dimensional volume of a n-dimensional parallelepiped is expressed by a determinant, and the determinant of a linear endomorphism determines how the orientation and the n-dimensional volume are transformed under the endomorphism. This is used in calculus with exterior differential forms and the Jacobian determinant, in particular for changes of variables in multiple integrals.


## Two by two matrices

The determinant of a 2 × 2 matrix ${\begin{pmatrix}a&b\\c&d\end{pmatrix}}$ is denoted either by "det" or by vertical bars around the matrix, and is defined as

$\det {\begin{pmatrix}a&b\\c&d\end{pmatrix}}={\begin{vmatrix}a&b\\c&d\end{vmatrix}}=ad-bc.$

For example,

$\det {\begin{pmatrix}3&7\\1&-4\end{pmatrix}}={\begin{vmatrix}3&7\\1&{-4}\end{vmatrix}}=(3\cdot (-4))-(7\cdot 1)=-19.$

### First properties

The determinant has several key properties that can be proved by direct evaluation of the definition for $2\times 2$ -matrices, and that continue to hold for determinants of larger matrices. They are as follows: first, the determinant of the identity matrix ${\begin{pmatrix}1&0\\0&1\end{pmatrix}}$ is 1. Second, the determinant is zero if two rows are the same:

${\begin{vmatrix}a&b\\a&b\end{vmatrix}}=ab-ba=0.$

This holds similarly if the two columns are the same. Moreover,

${\begin{vmatrix}a&b+b'\\c&d+d'\end{vmatrix}}=a(d+d')-(b+b')c={\begin{vmatrix}a&b\\c&d\end{vmatrix}}+{\begin{vmatrix}a&b'\\c&d'\end{vmatrix}}.$

Finally, if any column is multiplied by some number r (i.e., all entries in that column are multiplied by that number), the determinant is also multiplied by that number:

${\begin{vmatrix}r\cdot a&b\\r\cdot c&d\end{vmatrix}}=rad-brc=r(ad-bc)=r\cdot {\begin{vmatrix}a&b\\c&d\end{vmatrix}}.$


## Geometric meaning

If the matrix entries are real numbers, the matrix A represents the linear map that maps the basis vectors to the columns of A. The images of the basis vectors form a parallelogram that represents the image of the unit square under the mapping. The parallelogram defined by the columns of the above matrix is the one with vertices at (0, 0), (*a*, *c*), (*a* + *b*, *c* + *d*), and (*b*, *d*), as shown in the accompanying diagram.

The absolute value of *ad* − *bc* is the area of the parallelogram, and thus represents the scale factor by which areas are transformed by A.

The absolute value of the determinant together with the sign becomes the signed area of the parallelogram. The signed area is the same as the usual area, except that it is negative when the angle from the first to the second vector defining the parallelogram turns in a clockwise direction (which is opposite to the direction one would get for the identity matrix).

To show that *ad* − *bc* is the signed area, one may consider a matrix containing two vectors **u** ≡ (*a*, *c*) and **v** ≡ (*b*, *d*) representing the parallelogram's sides. The signed area can be expressed as |**u**| |**v**| sin *θ* for the angle *θ* between the vectors, which is simply base times height, the length of one vector times the perpendicular component of the other. Due to the sine this already is the signed area, yet it may be expressed more conveniently using the cosine of the complementary angle to a perpendicular vector, e.g. **u**⊥ = (−*c*, *a*), so that |**u**⊥| |**v**| cos *θ′* becomes the signed area in question, which can be determined by the pattern of the scalar product to be equal to *ad* − *bc* according to the following equations:

${\text{Signed area}}=|{\boldsymbol {u}}|\,|{\boldsymbol {v}}|\,\sin \,\theta =\left|{\boldsymbol {u}}^{\perp }\right|\,\left|{\boldsymbol {v}}\right|\,\cos \,\theta '={\begin{pmatrix}-c\\a\end{pmatrix}}\cdot {\begin{pmatrix}b\\d\end{pmatrix}}=ad-bc.$

Thus the determinant gives the area scale factor and the orientation induced by the mapping represented by *A*. When the determinant is equal to one, the linear mapping defined by the matrix preserves area and orientation.

If an *n* × *n* real matrix *A* is written in terms of its column vectors $A=\left[{\begin{array}{c|c|c|c}\mathbf {a} _{1}&\mathbf {a} _{2}&\cdots &\mathbf {a} _{n}\end{array}}\right]$ , then

$A{\begin{pmatrix}1\\0\\\vdots \\0\end{pmatrix}}=\mathbf {a} _{1},\quad A{\begin{pmatrix}0\\1\\\vdots \\0\end{pmatrix}}=\mathbf {a} _{2},\quad \ldots ,\quad A{\begin{pmatrix}0\\0\\\vdots \\1\end{pmatrix}}=\mathbf {a} _{n}.$

This means that A maps the unit *n*-cube to the *n*-dimensional parallelotope defined by the vectors $\mathbf {a} _{1},\mathbf {a} _{2},\ldots ,\mathbf {a} _{n},$ the region $P=\left\{c_{1}\mathbf {a} _{1}+\cdots +c_{n}\mathbf {a} _{n}\mid 0\leq c_{i}\leq 1\ \forall i\right\}$ ( ${\textstyle \forall }$ stands for "for all" as a logical symbol.)

The determinant gives the signed *n*-dimensional volume of this parallelotope, $\det(A)=\pm {\text{vol}}(P),$ and hence describes more generally the *n*-dimensional volume scale factor of the linear transformation produced by *A*. (The sign shows whether the transformation preserves or reverses orientation.) In particular, if the determinant is zero, then this parallelotope has volume zero and is not fully *n*-dimensional, which indicates that the dimension of the image of *A* is less than *n*. This means that *A* produces a linear transformation which is neither onto nor one-to-one, and so is not invertible.


## Definition

Let *A* be a square matrix with *n* rows and *n* columns, so that it can be written as

$A={\begin{bmatrix}a_{1,1}&a_{1,2}&\cdots &a_{1,n}\\a_{2,1}&a_{2,2}&\cdots &a_{2,n}\\\vdots &\vdots &\ddots &\vdots \\a_{n,1}&a_{n,2}&\cdots &a_{n,n}\end{bmatrix}}.$

The entries $a_{1,1}$ etc. are, for many purposes, real or complex numbers. As discussed below, the determinant is also defined for matrices whose entries are in a commutative ring.

The determinant of *A* is denoted by det(*A*), or it can be denoted directly in terms of the matrix entries by writing enclosing bars instead of brackets:

${\begin{vmatrix}a_{1,1}&a_{1,2}&\cdots &a_{1,n}\\a_{2,1}&a_{2,2}&\cdots &a_{2,n}\\\vdots &\vdots &\ddots &\vdots \\a_{n,1}&a_{n,2}&\cdots &a_{n,n}\end{vmatrix}}.$

There are various equivalent ways to define the determinant of a square matrix *A*, i.e. one with the same number of rows and columns: the determinant can be defined via the Leibniz formula, an explicit formula involving sums of products of certain entries of the matrix. The determinant can also be characterized as the unique function depending on the entries of the matrix satisfying certain properties. This approach can also be used to compute determinants by simplifying the matrices in question.

### Leibniz formula

#### 3 × 3 matrices

The *Leibniz formula* for the determinant of a 3 × 3 matrix is the following:

${\begin{vmatrix}a&b&c\\d&e&f\\g&h&i\end{vmatrix}}=aei+bfg+cdh-ceg-bdi-afh.\$

In this expression, each term has one factor from each row, all in different columns, arranged in increasing row order. For example, *bdi* has *b* from the first row second column, *d* from the second row first column, and *i* from the third row third column. The signs are determined by how many transpositions of factors are necessary to arrange the factors in increasing order of their columns (given that the terms are arranged left-to-right in increasing row order): positive for an even number of transpositions and negative for an odd number. For the example of *bdi*, the single transposition of *bd* to *db* gives *dbi,* whose three factors are from the first, second and third columns respectively; this is an odd number of transpositions, so the term appears with negative sign.

The rule of Sarrus is a mnemonic for the expanded form of this determinant: the sum of the products of three diagonal north-west to south-east lines of matrix elements, minus the sum of the products of three diagonal south-west to north-east lines of elements, when the copies of the first two columns of the matrix are written beside it as in the illustration. This scheme for calculating the determinant of a 3 × 3 matrix does not carry over into higher dimensions.

#### *n* × *n* matrices

Generalizing the above to higher dimensions, the determinant of an $n\times n$ matrix is an expression involving permutations and their signatures. A permutation of the set $\{1,2,\dots ,n\}$ is a bijective function $\sigma$ from this set to itself, with values $\sigma (1),\sigma (2),\ldots ,\sigma (n)$ exhausting the entire set. The set of all such permutations, called the symmetric group, is commonly denoted $S_{n}$ . The signature $\operatorname {sgn}(\sigma )$ of a permutation $\sigma$ is $+1,$ if the permutation can be obtained with an even number of transpositions (exchanges of two entries); otherwise, it is $-1.$

Given a matrix

$A={\begin{bmatrix}a_{1,1}\ldots a_{1,n}\\\vdots \qquad \vdots \\a_{n,1}\ldots a_{n,n}\end{bmatrix}},$

the Leibniz formula for its determinant is, using sigma notation for the sum,

$\det(A)={\begin{vmatrix}a_{1,1}\ldots a_{1,n}\\\vdots \qquad \vdots \\a_{n,1}\ldots a_{n,n}\end{vmatrix}}=\sum _{\sigma \in S_{n}}\operatorname {sgn}(\sigma )a_{1,\sigma (1)}\cdots a_{n,\sigma (n)}.$

Using pi notation for the product, this can be shortened into

$\det(A)=\sum _{\sigma \in S_{n}}\left(\operatorname {sgn}(\sigma )\prod _{i=1}^{n}a_{i,\sigma (i)}\right)$

.

The Levi-Civita symbol $\varepsilon _{i_{1},\ldots ,i_{n}}$ is defined on the n-tuples of integers in $\{1,\ldots ,n\}$ as 0 if two of the integers are equal, and otherwise as the signature of the permutation defined by the *n-*tuple of integers. With the Levi-Civita symbol, the Leibniz formula becomes

$\det(A)=\sum _{i_{1},i_{2},\ldots ,i_{n}}\varepsilon _{i_{1}\cdots i_{n}}a_{1,i_{1}}\!\cdots a_{n,i_{n}},$

where the sum is taken over all n-tuples of integers in $\{1,\ldots ,n\}.$


## Properties

### Characterization of the determinant

The determinant can be characterized by the following three key properties. To state these, it is convenient to regard an $n\times n$ matrix *A* as being composed of its n columns, so denoted as

$A={\big (}a_{1},\dots ,a_{n}{\big )},$

where the column vector $a_{i}$ (for each *i*) is composed of the entries of the matrix in the *i*-th column.

2. $\det \left(I\right)=1$ , where I is an identity matrix.
4. The determinant is *multilinear*: if the *j*th column of a matrix A is written as a linear combination $a_{j}=r\cdot v+w$ of two column vectors *v* and *w* and a number *r*, then the determinant of *A* is expressible as a similar linear combination: ${\begin{aligned}|A|&={\big |}a_{1},\dots ,a_{j-1},r\cdot v+w,a_{j+1},\dots ,a_{n}|\\&=r\cdot |a_{1},\dots ,v,\dots a_{n}|+|a_{1},\dots ,w,\dots ,a_{n}|\end{aligned}}$
6. The determinant is *alternating*: whenever two columns of a matrix are identical, its determinant is 0: $|a_{1},\dots ,v,\dots ,v,\dots ,a_{n}|=0.$

If the determinant is defined using the Leibniz formula as above, these three properties can be proved by direct inspection of that formula. Some authors also approach the determinant directly using these three properties: it can be shown that there is exactly one function that assigns to any $n\times n$ matrix *A* a number that satisfies these three properties. This also shows that this more abstract approach to the determinant yields the same definition as the one using the Leibniz formula.

To see this it suffices to expand the determinant by multi-linearity in the columns into a (huge) linear combination of determinants of matrices in which each column is a standard basis vector. These determinants are either 0 (if the columns are linearly dependent, by property 3) or else ±1 (by property 1 and 3 - the minus sign appears when the columns are permuted according to an odd permutation), so the linear combination gives the expression above in terms of the Levi-Civita symbol. While less technical in appearance, this characterization cannot entirely replace the Leibniz formula in defining the determinant, since without it the existence of an appropriate function is not clear.

### Immediate consequences

These rules have several further consequences:

- The determinant is a homogeneous function, i.e., $\det(cA)=c^{n}\det(A)$ (for an $n\times n$ matrix A ).
- Interchanging any pair of columns of a matrix multiplies its determinant by −1. This follows from the determinant being multilinear and alternating (properties 2 and 3 above): $|a_{1},\dots ,a_{j},\dots a_{i},\dots ,a_{n}|=-|a_{1},\dots ,a_{i},\dots ,a_{j},\dots ,a_{n}|.$ This formula can be applied iteratively when several columns are swapped. For example $|a_{3},a_{1},a_{2},a_{4}\dots ,a_{n}|=-|a_{1},a_{3},a_{2},a_{4},\dots ,a_{n}|=|a_{1},a_{2},a_{3},a_{4},\dots ,a_{n}|.$ Yet more generally, any permutation of the columns multiplies the determinant by the sign of the permutation.
- If some column can be expressed as a linear combination of the *other* columns (i.e. the columns of the matrix form a linearly dependent set), the determinant is 0. As a special case, this includes: if some column is such that all its entries are zero, then the determinant of that matrix is 0.
- Adding a scalar multiple of one column to *another* column does not change the value of the determinant. This is a consequence of multilinearity and being alternative: by multilinearity the determinant changes by a multiple of the determinant of a matrix with two equal columns, which determinant is 0, since the determinant is alternating.
- If A is a triangular matrix, i.e. $a_{ij}=0$ , whenever $i>j$ or, alternatively, whenever $i<j$ , then its determinant equals the product of the diagonal entries: $\det(A)=a_{11}a_{22}\cdots a_{nn}=\prod _{i=1}^{n}a_{ii}.$ Indeed, such a matrix can be reduced, by appropriately adding multiples of the columns with fewer nonzero entries to those with more entries, to a diagonal matrix (without changing the determinant). For such a matrix, using the linearity in each column reduces to the identity matrix, in which case the stated formula holds by the very first characterizing property of determinants. Alternatively, this formula can also be deduced from the Leibniz formula, since the only permutation $\sigma$ which gives a non-zero contribution is the identity permutation.

#### Example

These characterizing properties and their consequences listed above are both theoretically significant, but can also be used to compute determinants for concrete matrices. In fact, Gaussian elimination can be applied to bring any matrix into upper triangular form, and the steps in this algorithm affect the determinant in a controlled way. The following concrete example illustrates the computation of the determinant of the matrix A using that method:

$A={\begin{bmatrix}-2&-1&2\\2&1&4\\-3&3&-1\end{bmatrix}}.$

| Matrix | $B={\begin{bmatrix}-3&-1&2\\3&1&4\\0&3&-1\end{bmatrix}}$ | $C={\begin{bmatrix}-3&5&2\\3&13&4\\0&0&-1\end{bmatrix}}$ | $D={\begin{bmatrix}5&-3&2\\13&3&4\\0&0&-1\end{bmatrix}}$ | $E={\begin{bmatrix}18&-3&2\\0&3&4\\0&0&-1\end{bmatrix}}$ |
|---|---|---|---|---|
| Obtained by | add the second column to the first | add 3 times the third column to the second | swap the first two columns | add $-{\frac {13}{3}}$ times the second column to the first |
| Determinant | $\|A\|=\|B\|$ | $\|B\|=\|C\|$ | $\|D\|=-\|C\|$ | $\|E\|=\|D\|$ |

Combining these equalities gives $|A|=-|E|=-(18\cdot 3\cdot (-1))=54.$

### Transpose

The determinant of the transpose of A equals the determinant of *A*:

$\det \left(A^{\textsf {T}}\right)=\det(A)$

.

This can be proven by inspecting the Leibniz formula. This implies that in all the properties mentioned above, the word "column" can be replaced by "row" throughout. For example, viewing an *n* × *n* matrix as being composed of *n* rows, the determinant is an *n*-linear function.

### Multiplicativity and matrix groups

The determinant is a *multiplicative map*, i.e., for square matrices A and B of equal size, the determinant of a matrix product equals the product of their determinants:

$\det(AB)=\det(A)\det(B)$

This key fact can be proven by observing that, for a fixed matrix B , both sides of the equation are alternating and multilinear as a function depending on the columns of A . Moreover, they both take the value $\det B$ when A is the identity matrix. The above-mentioned unique characterization of alternating multilinear maps therefore shows this claim.

A matrix A with entries in a field is invertible precisely if its determinant is nonzero. This follows from the multiplicativity of the determinant and the formula for the inverse involving the adjugate matrix mentioned below. In this event, the determinant of the inverse matrix is given by

$\det \left(A^{-1}\right)={\frac {1}{\det(A)}}=[\det(A)]^{-1}$

.

In particular, products and inverses of matrices with non-zero determinant (respectively, determinant one) still have this property. Thus, the set of such matrices (of fixed size n over a field K ) forms a group known as the general linear group $\operatorname {GL} _{n}(K)$ (respectively, a subgroup called the special linear group $\operatorname {SL} _{n}(K)\subset \operatorname {GL} _{n}(K)$ . More generally, the word "special" indicates the subgroup of another matrix group of matrices of determinant one. Examples include the special orthogonal group (which if *n* is 2 or 3 consists of all rotation matrices), and the special unitary group.

Because the determinant respects multiplication and inverses, it is in fact a group homomorphism from $\operatorname {GL} _{n}(K)$ into the multiplicative group $K^{\times }$ of nonzero elements of K . This homomorphism is surjective and its kernel is $\operatorname {SL} _{n}(K)$ (the matrices with determinant one). Hence, by the first isomorphism theorem, this shows that $\operatorname {SL} _{n}(K)$ is a normal subgroup of $\operatorname {GL} _{n}(K)$ , and that the quotient group $\operatorname {GL} _{n}(K)/\operatorname {SL} _{n}(K)$ is isomorphic to $K^{\times }$ .

The Cauchy–Binet formula is a generalization of that product formula for *rectangular* matrices. This formula can also be recast as a multiplicative formula for compound matrices whose entries are the determinants of all quadratic submatrices of a given matrix.

### Laplace expansion

Laplace expansion expresses the determinant of a matrix A recursively in terms of determinants of smaller matrices, known as its minors. The minor $M_{i,j}$ is defined to be the determinant of the $(n-1)\times (n-1)$ matrix that results from A by removing the i -th row and the j -th column. The expression $(-1)^{i+j}M_{i,j}$ is known as a cofactor. For every i , one has the equality

$\det(A)=\sum _{j=1}^{n}(-1)^{i+j}a_{i,j}M_{i,j},$

which is called the *Laplace expansion along the ith row*. For example, the Laplace expansion along the first row ( $i=1$ ) gives the following formula:

${\begin{vmatrix}a&b&c\\d&e&f\\g&h&i\end{vmatrix}}=a{\begin{vmatrix}e&f\\h&i\end{vmatrix}}-b{\begin{vmatrix}d&f\\g&i\end{vmatrix}}+c{\begin{vmatrix}d&e\\g&h\end{vmatrix}}$

Unwinding the determinants of these $2\times 2$ -matrices gives back the Leibniz formula mentioned above. Similarly, the *Laplace expansion along the j -th column* is the equality

$\det(A)=\sum _{i=1}^{n}(-1)^{i+j}a_{i,j}M_{i,j}.$

Laplace expansion can be used iteratively for computing determinants, but this approach is inefficient for large matrices. However, it is useful for computing the determinants of highly symmetric matrix such as the Vandermonde matrix ${\begin{vmatrix}1&1&1&\cdots &1\\x_{1}&x_{2}&x_{3}&\cdots &x_{n}\\x_{1}^{2}&x_{2}^{2}&x_{3}^{2}&\cdots &x_{n}^{2}\\\vdots &\vdots &\vdots &\ddots &\vdots \\x_{1}^{n-1}&x_{2}^{n-1}&x_{3}^{n-1}&\cdots &x_{n}^{n-1}\end{vmatrix}}=\prod _{1\leq i<j\leq n}\left(x_{j}-x_{i}\right).$ The *n*-term Laplace expansion along a row or column can be generalized to write an *n* x *n* determinant as a sum of ${\tbinom {n}{k}}$ terms, each the product of the determinant of a *k* x *k* submatrix and the determinant of the complementary (*n−k*) x (*n−k*) submatrix.

### Adjugate matrix

The adjugate matrix $\operatorname {adj} (A)$ is the transpose of the matrix of the cofactors, that is,

$(\operatorname {adj} (A))_{i,j}=(-1)^{i+j}M_{ji}.$

For every matrix, one has

$(\det A)I=A\operatorname {adj} A=(\operatorname {adj} A)\,A.$

Thus the adjugate matrix can be used for expressing the inverse of a nonsingular matrix:

$A^{-1}={\frac {1}{\det A}}\operatorname {adj} A.$

### Block matrices

The formula for the determinant of a $2\times 2$ matrix above continues to hold, under appropriate further assumptions, for a block matrix, i.e., a matrix composed of four submatrices $A,B,C,D$ of dimension $m\times m$ , $m\times n$ , $n\times m$ and $n\times n$ , respectively. The easiest such formula, which can be proven using either the Leibniz formula or a factorization involving the Schur complement, is

$\det {\begin{pmatrix}A&0\\C&D\end{pmatrix}}=\det(A)\det(D)=\det {\begin{pmatrix}A&B\\0&D\end{pmatrix}}.$

If A is invertible, then it follows with results from the section on multiplicativity that

${\begin{aligned}\det {\begin{pmatrix}A&B\\C&D\end{pmatrix}}&=\det(A)\det {\begin{pmatrix}A&B\\C&D\end{pmatrix}}\underbrace {\det {\begin{pmatrix}A^{-1}&-A^{-1}B\\0&I_{n}\end{pmatrix}}} _{=\,\det(A^{-1})\,=\,(\det A)^{-1}}\\&=\det(A)\det {\begin{pmatrix}I_{m}&0\\CA^{-1}&D-CA^{-1}B\end{pmatrix}}\\&=\det(A)\det(D-CA^{-1}B),\end{aligned}}$

which simplifies to $\det(A)(D-CA^{-1}B)$ when D is a $1\times 1$ matrix.

A similar result holds when D is invertible, namely

${\begin{aligned}\det {\begin{pmatrix}A&B\\C&D\end{pmatrix}}&=\det(D)\det {\begin{pmatrix}A&B\\C&D\end{pmatrix}}\underbrace {\det {\begin{pmatrix}I_{m}&0\\-D^{-1}C&D^{-1}\end{pmatrix}}} _{=\,\det(D^{-1})\,=\,(\det D)^{-1}}\\&=\det(D)\det {\begin{pmatrix}A-BD^{-1}C&BD^{-1}\\0&I_{n}\end{pmatrix}}\\&=\det(D)\det(A-BD^{-1}C).\end{aligned}}$

Both results can be combined to derive Sylvester's determinant theorem, which is also stated below.

If the blocks are square matrices of the *same* size further formulas hold. For example, if C and D commute (i.e., $CD=DC$ ), then

$\det {\begin{pmatrix}A&B\\C&D\end{pmatrix}}=\det(AD-BC).$

This formula has been generalized to matrices composed of more than $2\times 2$ blocks, again under appropriate commutativity conditions among the individual blocks.

For $A=D$ and $B=C$ , the following formula holds (even if A and B do not commute).

$\det {\begin{pmatrix}A&B\\B&A\end{pmatrix}}=\det {\begin{pmatrix}A+B&B\\B+A&A\end{pmatrix}}=\det {\begin{pmatrix}A+B&B\\0&A-B\end{pmatrix}}=\det(A+B)\det(A-B).$

It is possible to compute the determinant by the block matrices in a fast way with the use of fast matrix multiplication algorithms in the time $O({n^{\omega }})$ for $~2.37\leq \omega <3$ , by the $LU$ decomposition.

### Sylvester's determinant theorem

Sylvester's determinant theorem states that for *A*, an *m* × *n* matrix, and *B*, an *n* × *m* matrix (so that *A* and *B* have dimensions allowing them to be multiplied in either order forming a square matrix):

$\det \left(I_{\mathit {m}}+AB\right)=\det \left(I_{\mathit {n}}+BA\right),$

where *I**m* and *I**n* are the *m* × *m* and *n* × *n* identity matrices, respectively.

From this general result several consequences follow.

1. For the case of column vector *c* and row vector *r*, each with *m* components, the formula allows quick calculation of the determinant of a matrix that differs from the identity matrix by a matrix of rank 1: $\det \left(I_{\mathit {m}}+cr\right)=1+rc.$
2. More generally, for any invertible *m* × *m* matrix *X*, $\det(X+AB)=\det(X)\det \left(I_{\mathit {n}}+BX^{-1}A\right),$
3. For a column and row vector as above: $\det(X+cr)=\det(X)\det \left(1+rX^{-1}c\right)=\det(X)+r\,\operatorname {adj} (X)\,c.$
4. For square matrices A and B of the same size, the matrices $AB$ and $BA$ have the same characteristic polynomials (hence the same eigenvalues).

A generalization is $\det \left(Z+AWB\right)=\det \left(Z\right)\det \left(W\right)\det \left(W^{-1}+BZ^{-1}A\right)$ (see Matrix determinant lemma), where *Z* is an *m* × *m* invertible matrix and *W* is an *n* × *n* invertible matrix.

### Sum

The determinant of the sum $A+B$ of two square matrices of the same size is not in general expressible in terms of the determinants of *A* and of *B*.

However, for positive semidefinite matrices A , B and C of equal size, $\det(A+B+C)+\det(C)\geq \det(A+C)+\det(B+C){\text{,}}$ with the corollary $\det(A+B)\geq \det(A)+\det(B){\text{.}}$

Brunn–Minkowski theorem implies that the nth root of determinant is a concave function, when restricted to Hermitian positive-definite $n\times n$ matrices. Therefore, if A and B are Hermitian positive-definite $n\times n$ matrices, one has ${\sqrt[{n}]{\det(A+B)}}\geq {\sqrt[{n}]{\det(A)}}+{\sqrt[{n}]{\det(B)}},$ since the nth root of the determinant is a homogeneous function.

#### Sum identity for 2×2 matrices

For the special case of $2\times 2$ matrices with complex entries, the determinant of the sum can be written in terms of determinants and traces in the following identity:

$\det(A+B)=\det(A)+\det(B)+{\text{tr}}(A){\text{tr}}(B)-{\text{tr}}(AB).$


## Properties of the determinant in relation to other notions

### Eigenvalues and characteristic polynomial

The determinant is closely related to two other central concepts in linear algebra, the eigenvalues and the characteristic polynomial of a matrix. Let A be an $n\times n$ matrix with complex entries. Then, by the Fundamental Theorem of Algebra, A must have exactly *n* eigenvalues $\lambda _{1},\lambda _{2},\ldots ,\lambda _{n}$ . (Here it is understood that an eigenvalue with algebraic multiplicity μ occurs μ times in this list.) Then, it turns out the determinant of A is equal to the *product* of these eigenvalues,

$\det(A)=\prod _{i=1}^{n}\lambda _{i}=\lambda _{1}\lambda _{2}\cdots \lambda _{n}.$

The product of all non-zero eigenvalues is referred to as pseudo-determinant.

From this, one immediately sees that the determinant of a matrix A is zero if and only if 0 is an eigenvalue of A . In other words, A is invertible if and only if 0 is not an eigenvalue of A .

The characteristic polynomial is defined as

$\chi _{A}(t)=\det(t\cdot I-A).$

Here, t is the indeterminate of the polynomial and I is the identity matrix of the same size as A . By means of this polynomial, determinants can be used to find the eigenvalues of the matrix A : they are precisely the roots of this polynomial, i.e., those complex numbers $\lambda$ such that

$\chi _{A}(\lambda )=0.$

A Hermitian matrix is positive definite if all its eigenvalues are positive. Sylvester's criterion asserts that this is equivalent to the determinants of the submatrices

$A_{k}:={\begin{bmatrix}a_{1,1}&a_{1,2}&\cdots &a_{1,k}\\a_{2,1}&a_{2,2}&\cdots &a_{2,k}\\\vdots &\vdots &\ddots &\vdots \\a_{k,1}&a_{k,2}&\cdots &a_{k,k}\end{bmatrix}}$

being positive, for all k between 1 and n .

### Trace

The trace tr(*A*) is by definition the sum of the diagonal entries of A and also equals the sum of the eigenvalues. Thus, for complex matrices A,

$\det(\exp(A))=\exp(\operatorname {tr} (A))$

or, for real matrices A,

$\operatorname {tr} (A)=\log(\det(\exp(A))).$

Here exp(A) denotes the matrix exponential of A, because every eigenvalue λ of A corresponds to the eigenvalue exp(λ) of exp(A). In particular, given any logarithm of A, that is, any matrix L satisfying

$\exp(L)=A$

the determinant of A is given by

$\det(A)=\exp(\operatorname {tr} (L)).$

For example, for *n* = 2, *n* = 3, and *n* = 4, respectively,

${\begin{aligned}\det(A)&={\frac {1}{2}}\left(\left(\operatorname {tr} (A)\right)^{2}-\operatorname {tr} \left(A^{2}\right)\right),\\\det(A)&={\frac {1}{6}}\left(\left(\operatorname {tr} (A)\right)^{3}-3\operatorname {tr} (A)~\operatorname {tr} \left(A^{2}\right)+2\operatorname {tr} \left(A^{3}\right)\right),\\\det(A)&={\frac {1}{24}}\left(\left(\operatorname {tr} (A)\right)^{4}-6\operatorname {tr} \left(A^{2}\right)\left(\operatorname {tr} (A)\right)^{2}+3\left(\operatorname {tr} \left(A^{2}\right)\right)^{2}+8\operatorname {tr} \left(A^{3}\right)~\operatorname {tr} (A)-6\operatorname {tr} \left(A^{4}\right)\right).\end{aligned}}$

cf. Cayley-Hamilton theorem. Such expressions are deducible from combinatorial arguments, Newton's identities, or the Faddeev–LeVerrier algorithm. That is, for generic n, det*A* = (−1)*n**c*0 the signed constant term of the characteristic polynomial, determined recursively from

$c_{n}=1;~~~c_{n-m}=-{\frac {1}{m}}\sum _{k=1}^{m}c_{n-m+k}\operatorname {tr} \left(A^{k}\right)~~(1\leq m\leq n)~.$

In the general case, this may also be obtained from

$\det(A)=\sum _{\begin{array}{c}k_{1},k_{2},\ldots ,k_{n}\geq 0\\k_{1}+2k_{2}+\cdots +nk_{n}=n\end{array}}\prod _{l=1}^{n}{\frac {(-1)^{k_{l}+1}}{l^{k_{l}}k_{l}!}}\operatorname {tr} \left(A^{l}\right)^{k_{l}},$

where the sum is taken over the set of all integers *kl* ≥ 0 satisfying the equation

$\sum _{l=1}^{n}lk_{l}=n.$

The formula can be expressed in terms of the complete exponential Bell polynomial of *n* arguments *s**l* = −(*l* – 1)! tr(*A**l*) as

$\det(A)={\frac {(-1)^{n}}{n!}}B_{n}(s_{1},s_{2},\ldots ,s_{n}).$

This formula can also be used to find the determinant of a matrix *AIJ* with multidimensional indices *I* = (*i*1, *i*2, ..., *ir*) and *J* = (*j*1, *j*2, ..., *jr*). The product and trace of such matrices are defined in a natural way as

$(AB)_{J}^{I}=\sum _{K}A_{K}^{I}B_{J}^{K},\operatorname {tr} (A)=\sum _{I}A_{I}^{I}.$

An important arbitrary dimension n identity can be obtained from the Mercator series expansion of the logarithm when the expansion converges. If every eigenvalue of *A* is less than 1 in absolute value,

$\det(I+A)=\sum _{k=0}^{\infty }{\frac {1}{k!}}\left(-\sum _{j=1}^{\infty }{\frac {(-1)^{j}}{j}}\operatorname {tr} \left(A^{j}\right)\right)^{k}\,,$

where *I* is the identity matrix. More generally, if

$\sum _{k=0}^{\infty }{\frac {1}{k!}}\left(-\sum _{j=1}^{\infty }{\frac {(-1)^{j}s^{j}}{j}}\operatorname {tr} \left(A^{j}\right)\right)^{k}\,,$

is expanded as a formal power series in s then all coefficients of sm for *m* > *n* are zero and the remaining polynomial is det(*I* + *sA*).

### Upper and lower bounds

For a positive definite matrix *A*, the trace operator gives the following tight lower and upper bounds on the log determinant

$\operatorname {tr} \left(I-A^{-1}\right)\leq \log \det(A)\leq \operatorname {tr} (A-I)$

with equality if and only if *A* = *I*. This relationship can be derived via the formula for the Kullback–Leibler divergence between two multivariate normal distributions.

Also,

${\frac {n}{\operatorname {tr} \left(A^{-1}\right)}}\leq \det(A)^{\frac {1}{n}}\leq {\frac {1}{n}}\operatorname {tr} (A)\leq {\sqrt {{\frac {1}{n}}\operatorname {tr} \left(A^{2}\right)}}.$

These inequalities can be proved by expressing the traces and the determinant in terms of the eigenvalues. As such, they represent the well-known fact that the harmonic mean is less than the geometric mean, which is less than the arithmetic mean, which is, in turn, less than the root mean square.

### Derivative

The Leibniz formula shows that the determinant of real (or analogously for complex) square matrices is a polynomial function from $\mathbf {R} ^{n\times n}$ to $\mathbf {R}$ . In particular, it is everywhere differentiable. Its derivative can be expressed using Jacobi's formula:

${\frac {d\det(A)}{d\alpha }}=\operatorname {tr} \left(\operatorname {adj} (A){\frac {dA}{d\alpha }}\right).$

where $\operatorname {adj} (A)$ denotes the adjugate of A . In particular, if A is invertible, we have

${\frac {d\det(A)}{d\alpha }}=\det(A)\operatorname {tr} \left(A^{-1}{\frac {dA}{d\alpha }}\right).$

Expressed in terms of the entries of A , these are

${\frac {\partial \det(A)}{\partial A_{ij}}}=\operatorname {adj} (A)_{ji}=\det(A)\left(A^{-1}\right)_{ji}.$

Yet another equivalent formulation is

$\det(A+\epsilon X)-\det(A)=\operatorname {tr} (\operatorname {adj} (A)X)\epsilon +O\left(\epsilon ^{2}\right)=\det(A)\operatorname {tr} \left(A^{-1}X\right)\epsilon +O\left(\epsilon ^{2}\right)$

,

using big O notation. The special case where $A=I$ , the identity matrix, yields

$\det(I+\epsilon X)=1+\operatorname {tr} (X)\epsilon +O\left(\epsilon ^{2}\right).$

This identity is used in describing Lie algebras associated to certain matrix Lie groups. For example, the special linear group $\operatorname {SL} _{n}$ is defined by the equation $\det A=1$ . The above formula shows that its Lie algebra is the special linear Lie algebra ${\mathfrak {sl}}_{n}$ consisting of those matrices having trace zero.

Writing a $3\times 3$ matrix as $A={\begin{bmatrix}a&b&c\end{bmatrix}}$ where $a,b,c$ are column vectors of length 3, then the gradient over one of the three vectors may be written as the cross product of the other two:

${\begin{aligned}\nabla _{\mathbf {a} }\det(A)&=\mathbf {b} \times \mathbf {c} \\\nabla _{\mathbf {b} }\det(A)&=\mathbf {c} \times \mathbf {a} \\\nabla _{\mathbf {c} }\det(A)&=\mathbf {a} \times \mathbf {b} .\end{aligned}}$


## History

Historically, determinants were used long before matrices: A determinant was originally defined as a property of a system of linear equations. The determinant "determines" whether the system has a unique solution (which occurs precisely if the determinant is non-zero). In Europe, solutions of linear systems of two equations were expressed by Cardano in 1545 by a determinant-like entity.

Determinants proper originated separately from the work of Seki Takakazu in 1683 in Japan and parallelly of Leibniz in 1693. Cramer (1750) stated, without proof, Cramer's rule. Both Cramer and also Bézout (1779) were led to determinants by the question of plane curves passing through a given set of points.

Vandermonde (1771) first recognized determinants as independent functions. Laplace (1772) gave the general method of expanding a determinant in terms of its complementary minors: Vandermonde had already given a special case. Immediately following, Lagrange (1773) treated determinants of the second and third order and applied it to questions of elimination theory; he proved many special cases of general identities.

Gauss (1801) made the next advance. Like Lagrange, he made much use of determinants in the theory of numbers. He introduced the word "determinant" (Laplace had used "resultant"), though not in the present signification, but rather as applied to the discriminant of a quadratic form. Gauss also arrived at the notion of reciprocal (inverse) determinants, and came very near the multiplication theorem.

The next contributor of importance is Binet (1811, 1812), who formally stated the theorem relating to the product of two matrices of *m* columns and *n* rows, which for the special case of *m* = *n* reduces to the multiplication theorem. On the same day (November 30, 1812) that Binet presented his paper to the Academy, Cauchy also presented one on the subject. (See Cauchy–Binet formula.) In this he used the word "determinant" in its present sense, summarized and simplified what was then known on the subject, improved the notation, and gave the multiplication theorem with a proof more satisfactory than Binet's. With him begins the theory in its generality.

Jacobi (1841) used the functional determinant which Sylvester later called the Jacobian. In his memoirs in *Crelle's Journal* for 1841 he specially treats this subject, as well as the class of alternating functions which Sylvester has called *alternants*. About the time of Jacobi's last memoirs, Sylvester (1839) and Cayley began their work. Cayley 1841 introduced the modern notation for the determinant using vertical bars.

The study of special forms of determinants has been the natural result of the completion of the general theory. Axisymmetric determinants have been studied by Lebesgue, Hesse, and Sylvester; persymmetric determinants by Sylvester and Hankel; circulants by Catalan, Spottiswoode, Glaisher, and Scott; skew determinants and Pfaffians, in connection with the theory of orthogonal transformation, by Cayley; continuants by Sylvester; Wronskians (so called by Muir) by Christoffel and Frobenius; compound determinants by Sylvester, Reiss, and Picquet; Jacobians and Hessians by Sylvester; and symmetric gauche determinants by Trudi. Of the textbooks on the subject Spottiswoode's was the first. In America, Hanus (1886), Weld (1893), and Muir/Metzler (1933) published treatises.


## Applications

### Cramer's rule

Determinants can be used to describe the solutions of a linear system of equations, written in matrix form as $Ax=b$ . This equation has a unique solution x if and only if $\det(A)$ is nonzero. In this case, the solution is given by Cramer's rule:

$x_{i}={\frac {\det(A_{i})}{\det(A)}}\qquad i=1,2,3,\ldots ,n$

where $A_{i}$ is the matrix formed by replacing the i -th column of A by the column vector b . This follows immediately by column expansion of the determinant, i.e.

$\det(A_{i})=\det {\begin{bmatrix}a_{1}&\ldots &b&\ldots &a_{n}\end{bmatrix}}$

$=\sum _{j=1}^{n}x_{j}\det {\begin{bmatrix}a_{1}&\ldots &a_{i-1}&a_{j}&a_{i+1}&\ldots &a_{n}\end{bmatrix}}=x_{i}\det(A)$

where the vectors $a_{j}$ are the columns of *A*. The rule is also implied by the identity

$A\,\operatorname {adj} (A)=\operatorname {adj} (A)\,A=\det(A)\,I_{n}.$

Cramer's rule can be implemented in $\operatorname {O} (n^{3})$ time, which is comparable to more common methods of solving systems of linear equations, such as LU, QR, or singular value decomposition.

### Linear independence

Determinants can be used to characterize linearly dependent vectors: $\det A$ is zero if and only if the column vectors of the matrix A are linearly dependent. For example, given two linearly independent vectors $v_{1},v_{2}\in \mathbf {R} ^{3}$ , a third vector $v_{3}$ lies in the plane spanned by the former two vectors exactly if the determinant of the $3\times 3$ matrix consisting of the three vectors is zero. The same idea is also used in the theory of differential equations: given functions $f_{1}(x),\dots ,f_{n}(x)$ (supposed to be $n-1$ times differentiable), the Wronskian is defined to be

$W(f_{1},\ldots ,f_{n})(x)={\begin{vmatrix}f_{1}(x)&f_{2}(x)&\cdots &f_{n}(x)\\f_{1}'(x)&f_{2}'(x)&\cdots &f_{n}'(x)\\\vdots &\vdots &\ddots &\vdots \\f_{1}^{(n-1)}(x)&f_{2}^{(n-1)}(x)&\cdots &f_{n}^{(n-1)}(x)\end{vmatrix}}.$

It is non-zero (for some x ) in a specified interval if and only if the given functions and all their derivatives up to order $n-1$ are linearly independent. If it can be shown that the Wronskian is zero everywhere on an interval then, in the case of analytic functions, this implies the given functions are linearly dependent. See the Wronskian and linear independence. Another such use of the determinant is the resultant, which gives a criterion when two polynomials have a common root.

### Cross Product

The computation of a cross product is equivalent to finding the formal determinant a specific 3 by 3 matrix. Specifically, for vectors $\mathbf {a} =a_{1}\mathbf {i} +a_{2}\mathbf {j} +a_{3}\mathbf {k}$ , and $\mathbf {b} =b_{1}\mathbf {i} +b_{2}\mathbf {j} +b_{3}\mathbf {k}$ :

$\mathbf {a\times b} =\det {\begin{pmatrix}\mathbf {i} &\mathbf {j} &\mathbf {k} \\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\\\end{pmatrix}}$

### Orientation of a basis

The determinant can be thought of as assigning a number to every sequence of *n* vectors in **R***n*, by using the square matrix whose columns are the given vectors. The determinant will be nonzero if and only if the sequence of vectors is a *basis* for **R***n*. In that case, the sign of the determinant determines whether the orientation of the basis is consistent with or opposite to the orientation of the standard basis. In the case of an orthogonal basis, the magnitude of the determinant is equal to the *product* of the lengths of the basis vectors. For instance, an orthogonal matrix with entries in **R***n* represents an orthonormal basis in Euclidean space, and hence has determinant of ±1 (since all the vectors have length 1). The determinant is +1 if and only if the basis has the same orientation. It is −1 if and only if the basis has the opposite orientation.

More generally, if the determinant of *A* is positive, *A* represents an orientation-preserving linear transformation (if *A* is an orthogonal 2 × 2 or 3 × 3 matrix, this is a rotation), while if it is negative, *A* switches the orientation of the basis.

### Volume and Jacobian determinant

As pointed out above, the absolute value of the determinant of real vectors is equal to the volume of the parallelepiped spanned by those vectors. As a consequence, if $f:\mathbf {R} ^{n}\to \mathbf {R} ^{n}$ is the linear map given by multiplication with a matrix A , and $S\subset \mathbf {R} ^{n}$ is any measurable subset, then the volume of $f(S)$ is given by $|\det(A)|$ times the volume of S . More generally, if the linear map $f:\mathbf {R} ^{n}\to \mathbf {R} ^{m}$ is represented by the $m\times n$ matrix A , then the ratio between the n -dimensional volumes of $f(S)$ and S is given by:

${\frac {\operatorname {volume} (f(S))}{\operatorname {volume} (S)}}={\sqrt {\det \left(A^{\textsf {T}}A\right)}}.$

When $m<n$ this is zero.

By calculating the volume of the tetrahedron bounded by four points, they can be used to identify skew lines. The volume of any tetrahedron, given its vertices $a,b,c,d$ , ${\frac {1}{6}}\cdot |\det(a-b,b-c,c-d)|$ , or any other combination of pairs of vertices that form a spanning tree over the vertices.

For a general differentiable function, much of the above carries over by considering the Jacobian matrix of *f*. For

$f:\mathbf {R} ^{n}\rightarrow \mathbf {R} ^{n},$

the Jacobian matrix is the *n* × *n* matrix whose entries are given by the partial derivatives

$D(f)=\left({\frac {\partial f_{i}}{\partial x_{j}}}\right)_{1\leq i,j\leq n}.$

Its determinant, the Jacobian determinant, appears in the higher-dimensional version of integration by substitution: for suitable functions *f* and an open subset *U* of **R***n* (the domain of *f*), the integral over *f*(*U*) of some other function *φ* : **R***n* → **R***m* is given by

$\int _{f(U)}\phi (\mathbf {v} )\,d\mathbf {v} =\int _{U}\phi (f(\mathbf {u} ))\left|\det(\operatorname {D} f)(\mathbf {u} )\right|\,d\mathbf {u} .$

The Jacobian also occurs in the inverse function theorem.

When applied to the field of Cartography, the determinant can be used to measure the rate of expansion of a map near the poles.

### Areas and Collinearity

The determinant provides a convenient way to calculate the area of a triangle in the xy-plane. The area of a triangle whose vertices are $(x_{1},y_{1})$ , $(x_{2},y_{2})$ and $(x_{3},y_{3})$ is given by:

$\pm {\frac {1}{2}}\det {\begin{pmatrix}x_{1}&y_{1}&1\\x_{2}&y_{2}&1\\x_{3}&y_{3}&1\end{pmatrix}}$

where the sign $\pm$ is chosen to yield a positive area. An immediate corollary of this result is that if the determinant is zero, there is no triangle, which implies the points are collinear. The determinant, therefore, provides a useful tool to test for collinearity.

Since two points uniquely identify a line in the xy-plane, one of the rows in the determinant can be replaced with any arbitrary point $(x,y)$ to express the general equation of a line through points $(x_{1},y_{1})$ and $(x_{2},y_{2})$ as:

$\det {\begin{pmatrix}x&y&1\\x_{1}&y_{1}&1\\x_{2}&y_{2}&1\end{pmatrix}}=0.$

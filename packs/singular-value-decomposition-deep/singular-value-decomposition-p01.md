---
title: "Singular value decomposition (part 1/2)"
source: https://en.wikipedia.org/wiki/Singular_value_decomposition
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
part: 1/2
---

# Singular value decomposition

In linear algebra, the **singular value decomposition** (**SVD**) is a factorization of a real or complex matrix into a rotation, followed by a scaling, followed by another rotation. It generalizes the eigendecomposition of a square normal matrix with an orthonormal eigenbasis to any ⁠ $m\times n$ ⁠ matrix. It is related to the polar decomposition.

Specifically, the singular value decomposition of an $m\times n$ complex matrix ⁠ $\mathbf {M}$ ⁠ is a factorization of the form ⁠ $\mathbf {M} =\mathbf {U\Sigma V} ^{*}$ ⁠, where ⁠ $\mathbf {U}$ ⁠ is an ⁠ $m\times m$ ⁠ complex unitary matrix, $\mathbf {\Sigma }$ is an $m\times n$ rectangular diagonal matrix with non-negative real numbers on the diagonal, ⁠ $\mathbf {V}$ ⁠ is an $n\times n$ complex unitary matrix, and $\mathbf {V} ^{*}$ is the conjugate transpose of ⁠ $\mathbf {V}$ ⁠. Such decompositions always exist for any complex matrix. If ⁠ $\mathbf {M}$ ⁠ is real, then ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ can be guaranteed to be real orthogonal matrices; in such contexts, the SVD is often denoted ⁠ $\mathbf {U\Sigma V} ^{\mathsf {T}}$ ⁠.

The diagonal entries $\sigma _{i}=\mathbf {\Sigma } _{ii}$ of $\mathbf {\Sigma }$ are uniquely determined by ⁠ $\mathbf {M}$ ⁠ up to reordering and are known as the singular values of ⁠ $\mathbf {M}$ ⁠. The number of non-zero singular values is equal to the rank of ⁠ $\mathbf {M}$ ⁠. The columns of ⁠ $\mathbf {U}$ ⁠ and the columns of ⁠ $\mathbf {V}$ ⁠ are called left-singular vectors and right-singular vectors of ⁠ $\mathbf {M}$ ⁠, respectively. They form two sets of orthonormal bases ⁠ $\mathbf {u} _{1},\ldots ,\mathbf {u} _{m}$ ⁠ and ⁠ $\mathbf {v} _{1},\ldots ,\mathbf {v} _{n}$ ⁠, and if they are sorted so that the singular values $\sigma _{i}$ equal to zero are all in the highest-numbered columns (or rows), the singular value decomposition can be written as $\mathbf {M} =\sum _{i=1}^{r}\sigma _{i}\mathbf {u} _{i}\mathbf {v} _{i}^{*},$ where $r\leq \min\{m,n\}$ is the rank of ⁠ $\mathbf {M}$ ⁠.

For any ⁠ $(j,k)\in \{1,\dots ,m\}\times \{1,\dots ,n\}$ ⁠, taking the ⁠ $(j,k)$ ⁠-entry directly yields $\mathbf {M} _{j,k}=\sum _{i=1}^{r}\sigma _{i}\mathbf {U} _{j,i}{\overline {\mathbf {V} _{k,i}}}.$

The SVD is not unique. However, it is always possible to choose the decomposition such that the singular values $\mathbf {\Sigma } _{ii}$ are in descending order. In this case, $\mathbf {\Sigma }$ (but not ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠) is uniquely determined by ⁠ $\mathbf {M}$ ⁠.

The terminology "SVD" sometimes refers to the **compact SVD**, a similar decomposition ⁠ $\mathbf {M} =\mathbf {U} _{r}\mathbf {\Sigma } _{r}\mathbf {V} ^{*}\!\!\!\!_{r}\,$ ⁠ in which ⁠ $\mathbf {\Sigma } _{r}$ ⁠ is square diagonal of size ⁠ $r\times r$ ⁠, where ⁠ $r\leq \min\{m,n\}$ ⁠ is the rank of ⁠ $\mathbf {M}$ ⁠, and has only the non-zero singular values. In this variant, ⁠ $\mathbf {U} _{r}$ ⁠ is an ⁠ $m\times r$ ⁠ semi-unitary matrix and $\mathbf {V} \!_{r}$ is an ⁠ $n\times r$ ⁠ semi-unitary matrix, such that ⁠ $\mathbf {U} _{r}^{*}\mathbf {U} _{r}=\mathbf {V} ^{*}\!\!\!\!_{r}~\mathbf {V} \!_{r}=\mathbf {I} _{r}$ ⁠.

Mathematical applications of the SVD include computing the pseudoinverse, matrix approximation, and determining the rank, range, and null space of a matrix. The SVD is also extremely useful in many areas of science, engineering, and statistics, such as signal processing, least squares fitting of data, and process control.


## Intuitive interpretations

### Rotation, coordinate scaling, and reflection

In the special case when ⁠ $\mathbf {M}$ ⁠ is an ⁠ $m\times m$ ⁠ real square matrix, the matrices ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ can be chosen to be real ⁠ $m\times m$ ⁠ matrices too. In that case, "unitary" is the same as "orthogonal". Then, interpreting both unitary matrices as well as the diagonal matrix, summarized here as ⁠ $\mathbf {A}$ ⁠, as a linear transformation ⁠ $\mathbf {x} \mapsto \mathbf {Ax}$ ⁠ of the space ⁠ $\mathbb {R} ^{m}$ ⁠, the matrices ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ represent rotations or reflections of the space, while ⁠ $\mathbf {\Sigma }$ ⁠ represents the scaling of each coordinate ⁠ $\mathbf {x} _{i}$ ⁠ by the factor ⁠ $\sigma _{i}$ ⁠. Thus the SVD decomposition breaks down any linear transformation of ⁠ $\mathbb {R} ^{m}$ ⁠ into a composition of three geometrical transformations: a rotation or reflection (⁠ $\mathbf {V} ^{*}$ ⁠), followed by a coordinate-by-coordinate scaling (⁠ $\mathbf {\Sigma }$ ⁠), followed by another rotation or reflection (⁠ $\mathbf {U}$ ⁠).

In particular, if ⁠ $\mathbf {M}$ ⁠ has a positive determinant, then ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ can be chosen to be both rotations with reflections, or both rotations without reflections. If the determinant is negative, exactly one of them will have a reflection. If the determinant is zero, each can be independently chosen to be of either type.

If the matrix ⁠ $\mathbf {M}$ ⁠ is real but not square, namely ⁠ $m\times n$ ⁠ with ⁠ $m\neq n$ ⁠, it can be interpreted as a linear transformation from ⁠ $\mathbb {R} ^{n}$ ⁠ to ⁠ $\mathbb {R} ^{m}$ ⁠. Then ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ can be chosen to be rotations/reflections of ⁠ $\mathbb {R} ^{m}$ ⁠ and ⁠ $\mathbb {R} ^{n}$ ⁠, respectively; and ⁠ $\mathbf {\Sigma }$ ⁠, besides scaling the first ⁠ $\min\{m,n\}$ ⁠ coordinates, also extends the vector with zeros, i.e. removes trailing coordinates, so as to turn ⁠ $\mathbb {R} ^{n}$ ⁠ into ⁠ $\mathbb {R} ^{m}$ ⁠.

### Singular values as semiaxes of an ellipse or ellipsoid

As shown in the figure, the singular values can be interpreted as the magnitude of the semiaxes of an ellipse in 2D. This concept can be generalized to ⁠ n ⁠-dimensional Euclidean space, with the singular values of any ⁠ $n\times n$ ⁠ square matrix being viewed as the magnitude of the semiaxis of an ⁠ n ⁠-dimensional ellipsoid. Similarly, the singular values of any ⁠ $m\times n$ ⁠ matrix can be viewed as the magnitude of the semiaxis of an ⁠ n ⁠-dimensional ellipsoid in ⁠ m ⁠-dimensional space, for example as an ellipse in a (tilted) 2D plane in a 3D space. Singular values encode magnitude of the semiaxis, while singular vectors encode direction. See below for further details.

### The columns of U and V are orthonormal bases

Since ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ are unitary, the columns of each of them form a set of orthonormal vectors, which can be regarded as basis vectors. The matrix ⁠ $\mathbf {M}$ ⁠ maps the basis vector ⁠ $\mathbf {V} _{i}$ ⁠ to the stretched unit vector ⁠ $\sigma _{i}\mathbf {U} _{i}$ ⁠. By the definition of a unitary matrix, the same is true for their conjugate transposes ⁠ $\mathbf {U} ^{*}$ ⁠ and ⁠ $\mathbf {V}$ ⁠, except the geometric interpretation of the singular values as stretches is lost. In short, the columns of ⁠ $\mathbf {U}$ ⁠, ⁠ $\mathbf {U} ^{*}$ ⁠, ⁠ $\mathbf {V}$ ⁠, and ⁠ $\mathbf {V} ^{*}$ ⁠ are orthonormal bases. When ⁠ $\mathbf {M}$ ⁠ is a positive-semidefinite Hermitian matrix, ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ are both equal to the unitary matrix used to diagonalize ⁠ $\mathbf {M}$ ⁠. However, when ⁠ $\mathbf {M}$ ⁠ is not positive-semidefinite and Hermitian but still diagonalizable, its eigendecomposition and singular value decomposition are distinct.

### Relation to the four fundamental subspaces

- The first ⁠ r ⁠ columns of ⁠ $\mathbf {U}$ ⁠ are a basis of the column space of ⁠ $\mathbf {M}$ ⁠.
- The last ⁠ $m-r$ ⁠ columns of ⁠ $\mathbf {U}$ ⁠ are a basis of the null space of ⁠ $\mathbf {M} ^{*}$ ⁠.
- The first ⁠ r ⁠ columns of ⁠ $\mathbf {V}$ ⁠ are a basis of the column space of ⁠ $\mathbf {M} ^{*}$ ⁠ (the row space of ⁠ $\mathbf {M}$ ⁠ in the real case).
- The last ⁠ $n-r$ ⁠ columns of ⁠ $\mathbf {V}$ ⁠ are a basis of the null space of ⁠ $\mathbf {M}$ ⁠.

### Geometric meaning

Because ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ are unitary, we know that the columns ⁠ $\mathbf {U} _{1},\ldots ,\mathbf {U} _{m}$ ⁠ of ⁠ $\mathbf {U}$ ⁠ yield an orthonormal basis of ⁠ $K^{m}$ ⁠ and the columns ⁠ $\mathbf {V} _{1},\ldots ,\mathbf {V} _{n}$ ⁠ of ⁠ $\mathbf {V}$ ⁠ yield an orthonormal basis of ⁠ $K^{n}$ ⁠ (with respect to the standard scalar products on these spaces).

The linear transformation $T\!\!:\left\{{\begin{aligned}K^{n}&\to K^{m}\\x&\mapsto \mathbf {M} x\end{aligned}}\right\}$ has a particularly simple description with respect to these orthonormal bases: we have $T(\mathbf {V} _{i})=\sigma _{i}\mathbf {U} _{i},\qquad i=1,\ldots ,\min\{m,n\},$ where ⁠ $\sigma _{i}$ ⁠ is the ⁠ i ⁠-th diagonal entry of ⁠ $\mathbf {\Sigma }$ ⁠, and ⁠ $T(\mathbf {V} _{i})=0$ ⁠ for ⁠ $i>\min\{m,n\}$ ⁠.

The geometric content of the SVD theorem can thus be summarized as follows: for every linear map ⁠ $T\!\!:K^{n}\to K^{m}$ ⁠ one can find orthonormal bases of ⁠ $K^{n}$ ⁠ and ⁠ $K^{m}$ ⁠ such that ⁠ T ⁠ maps the ⁠ i ⁠-th basis vector of ⁠ $K^{n}$ ⁠ to a non-negative multiple of the ⁠ i ⁠-th basis vector of ⁠ $K^{m}$ ⁠, and sends the leftover basis vectors to zero. With respect to these bases, the map ⁠ T ⁠ is therefore represented by a diagonal matrix with non-negative real diagonal entries.

To get a more visual flavor of singular values and SVD factorization – at least when working on real vector spaces – consider the sphere ⁠ S ⁠ of radius one in ⁠ $\mathbb {R} ^{n}$ ⁠. The linear map ⁠ T ⁠ maps this sphere onto an ellipsoid in ⁠ $\mathbb {R} ^{m}$ ⁠. Non-zero singular values are simply the lengths of the semi-axes of this ellipsoid. Especially when ⁠ $n=m$ ⁠, and all the singular values are distinct and non-zero, the SVD of the linear map ⁠ T ⁠ can be easily analyzed as a succession of three consecutive moves: consider the ellipsoid ⁠ $T(S)$ ⁠ and specifically its axes; then consider the directions in ⁠ $\mathbb {R} ^{n}$ ⁠ sent by ⁠ T ⁠ onto these axes. These directions happen to be mutually orthogonal. Apply first an isometry ⁠ $\mathbf {V} ^{*}$ ⁠ sending these directions to the coordinate axes of ⁠ $\mathbb {R} ^{n}$ ⁠. On a second move, apply an endomorphism ⁠ $\mathbf {D}$ ⁠ diagonalized along the coordinate axes and stretching or shrinking in each direction, using the semi-axis lengths of ⁠ $T(S)$ ⁠ as scaling coefficients. The composition ⁠ $\mathbf {D} \circ \mathbf {V} ^{*}$ ⁠ then sends the unit-sphere onto an ellipsoid isometric to ⁠ $T(S)$ ⁠. To define the third and last move, apply an isometry ⁠ $\mathbf {U}$ ⁠ to this ellipsoid to obtain ⁠ $T(S)$ ⁠. As can be easily checked, the composition ⁠ $\mathbf {U} \circ \mathbf {D} \circ \mathbf {V} ^{*}$ ⁠ coincides with ⁠ T ⁠.


## Example

For example, the ⁠ $4\times 5$ ⁠ matrix ⁠ $\mathbf {M}$ ⁠ below can be decomposed as ⁠ $\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}$ ⁠: ${\begin{aligned}\mathbf {M} &={\begin{bmatrix}1&0&0&0&2\\0&0&3&0&0\\0&0&0&0&0\\0&2&0&0&0\end{bmatrix}}\\&={\begin{bmatrix}\color {PineGreen}0&\color {BrickRed}1&\color {BlueViolet}0&\color {CadetBlue}0\\\color {PineGreen}1&\color {BrickRed}0&\color {BlueViolet}0&\color {CadetBlue}0\\\color {PineGreen}0&\color {BrickRed}0&\color {BlueViolet}0&\color {CadetBlue}1\\\color {PineGreen}0&\color {BrickRed}0&\color {BlueViolet}1&\color {CadetBlue}0\end{bmatrix}}{\begin{bmatrix}\color {PineGreen}3&\color {Gray}0&\color {Gray}0&\color {Gray}0&\color {Gray}0\\\color {Gray}0&\color {BrickRed}{\sqrt {5}}&\color {Gray}0&\color {Gray}0&\color {Gray}0\\\color {Gray}0&\color {Gray}0&\color {BlueViolet}2&\color {Gray}0&\color {Gray}0\\\color {Gray}0&\color {Gray}0&\color {Gray}0&\color {CadetBlue}0&\color {Gray}0\end{bmatrix}}{\begin{bmatrix}\color {PineGreen}0&\color {PineGreen}0&\color {PineGreen}1&\color {PineGreen}0&\color {PineGreen}0\\\color {BrickRed}{\tfrac {1}{\sqrt {5}}}&\color {BrickRed}0&\color {BrickRed}0&\color {BrickRed}0&\color {BrickRed}{\tfrac {2}{\sqrt {5}}}\\\color {BlueViolet}0&\color {BlueViolet}1&\color {BlueViolet}0&\color {BlueViolet}0&\color {BlueViolet}0\\\color {CadetBlue}0&\color {CadetBlue}0&\color {CadetBlue}0&\color {CadetBlue}1&\color {CadetBlue}0\\\color {CadetBlue}{\tfrac {2}{\sqrt {5}}}&\color {CadetBlue}0&\color {CadetBlue}0&\color {CadetBlue}0&\color {CadetBlue}-{\tfrac {1}{\sqrt {5}}}\end{bmatrix}}\\&=\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}.\end{aligned}}$

The singular values of ⁠ $\mathbf {M}$ ⁠ are the diagonal entries of ⁠ $\mathbf {\Sigma }$ ⁠: ${\color {PineGreen}3},{\color {BrickRed}{\sqrt {5}}},{\color {BlueViolet}2},{\color {CadetBlue}0}$ . The corresponding left- and right-singular vectors are the columns of ⁠ $\mathbf {U}$ ⁠ and rows of ⁠ $\mathbf {V} ^{*}$ ⁠, respectively.

The matrices ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ are unitary (and as real-valued matrices, orthogonal), meaning ⁠ $\mathbf {U} \mathbf {U} ^{*}=\mathbf {I} _{4}$ ⁠ and ⁠ $\mathbf {V} \mathbf {V} ^{*}=\mathbf {I} _{5}$ ⁠, where ⁠ $\mathbf {I} _{k}$ ⁠ is the ⁠ $k\times k$ ⁠ identity matrix.

The matrix ⁠ $\mathbf {M}$ ⁠ has rank ⁠ 3 ⁠, so there are only three non-zero singular values. This particular singular value decomposition is not unique; for instance, the last two rows of ⁠ $\mathbf {V} ^{*}$ ⁠ do not contribute to the product because they are multiplied by zero, so are substantially arbitrary, and can be replaced with any pair of unit vectors which are orthogonal to each-other and the other rows. Likewise for the last column of ⁠ $\mathbf {U}$ ⁠.

The compact SVD eliminates the rows and columns from ⁠ $\mathbf {\Sigma }$ ⁠ which consist entirely of zeros, and also the superfluous corresponding columns of ⁠ $\mathbf {U}$ ⁠ and rows of ⁠ $\mathbf {V} ^{*}$ ⁠: $\mathbf {M} ={\begin{bmatrix}\color {PineGreen}0&\color {BrickRed}1&\color {BlueViolet}0\\\color {PineGreen}1&\color {BrickRed}0&\color {BlueViolet}0\\\color {PineGreen}0&\color {BrickRed}0&\color {BlueViolet}0\\\color {PineGreen}0&\color {BrickRed}0&\color {BlueViolet}1\end{bmatrix}}{\begin{bmatrix}\color {PineGreen}3&\color {Gray}0&\color {Gray}0\\\color {Gray}0&\color {BrickRed}{\sqrt {5}}&\color {Gray}0\\\color {Gray}0&\color {Gray}0&\color {BlueViolet}2\\\end{bmatrix}}{\begin{bmatrix}\color {PineGreen}0&\color {PineGreen}0&\color {PineGreen}1&\color {PineGreen}0&\color {PineGreen}0\\\color {BrickRed}{\tfrac {1}{\sqrt {5}}}&\color {BrickRed}0&\color {BrickRed}0&\color {BrickRed}0&\color {BrickRed}{\tfrac {2}{\sqrt {5}}}\\\color {BlueViolet}0&\color {BlueViolet}1&\color {BlueViolet}0&\color {BlueViolet}0&\color {BlueViolet}0\end{bmatrix}}.$

Instead of the product of three matrices, the SVD of ⁠ $\mathbf {M}$ ⁠ can be written as a sum of three rank-⁠ 1 ⁠ matrices, each formed as the outer product of one column ⁠ $\mathbf {u} _{j}$ ⁠ of ⁠ $\mathbf {U}$ ⁠ times the corresponding row ⁠ $\mathbf {v} _{j}^{*}$ ⁠ of ⁠ $\mathbf {V} ^{*}$ ⁠, scaled by the corresponding singular value ⁠ $\sigma _{j}$ ⁠:

${\begin{aligned}\mathbf {M} &=\sum _{j}\sigma _{j}\mathbf {u} _{j}\mathbf {v} _{j}^{*}={\color {PineGreen}3\mathbf {u} _{1}\mathbf {v} _{1}^{*}}+{\color {BrickRed}{\sqrt {5}}\mathbf {u} _{2}\mathbf {v} _{2}^{*}}+{\color {BlueViolet}2\mathbf {u} _{3}\mathbf {v} _{3}^{*}}\\&={\color {PineGreen}{\begin{bmatrix}0&0&0&0&0\\0&0&3&0&0\\0&0&0&0&0\\0&0&0&0&0\end{bmatrix}}}+{\color {BrickRed}{\begin{bmatrix}1&0&0&0&2\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\end{bmatrix}}}+{\color {BlueViolet}{\begin{bmatrix}0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&2&0&0&0\end{bmatrix}}}.\end{aligned}}$


## SVD and spectral decomposition

### Singular values, singular vectors, and their relation to the SVD

A non-negative real number ⁠ $\sigma$ ⁠ is a **singular value** for ⁠ $\mathbf {M}$ ⁠ if and only if there exist unit vectors ⁠ $\mathbf {u}$ ⁠ in ⁠ $K^{m}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ in ⁠ $K^{n}$ ⁠ such that ${\begin{cases}\mathbf {Mv} \!\!\!&=\,\,\sigma \mathbf {u} ,\\[3mu]\mathbf {M^{*}u} \!\!\!&=\,\,\sigma \mathbf {v} .\end{cases}}$

The vectors ⁠ $\mathbf {u}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ are called **left-singular** and **right-singular vectors** for ⁠ $\sigma$ ⁠, respectively.

In any singular value decomposition $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*},$ the diagonal entries of ⁠ $\mathbf {\Sigma }$ ⁠ are equal to the singular values of ⁠ $\mathbf {M}$ ⁠. The first ⁠ $p=\min\{m,n\}$ ⁠ columns of ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ are, respectively, left- and right-singular vectors for the corresponding singular values. Consequently, the above [where?] theorem implies that:

- An ⁠ $m\times n$ ⁠ matrix ⁠ $\mathbf {M}$ ⁠ has at most ⁠ p ⁠ distinct singular values.
- It is always possible to find a unitary basis ⁠ $\mathbf {U}$ ⁠ for ⁠ $K^{m}$ ⁠ with a subset of basis vectors spanning the left-singular vectors of each singular value of ⁠ $\mathbf {M}$ ⁠.
- It is always possible to find a unitary basis ⁠ $\mathbf {V}$ ⁠ for ⁠ $K^{n}$ ⁠ with a subset of basis vectors spanning the right-singular vectors of each singular value of ⁠ $\mathbf {M}$ ⁠.

A singular value for which we can find two left- (or right-) singular vectors that are linearly independent is called *degenerate*. If ⁠ $\mathbf {u} _{1}$ ⁠ and ⁠ $\mathbf {u} _{2}$ ⁠ are two left-singular vectors which both correspond to the singular value ⁠ $\sigma$ ⁠, then any normalized linear combination of the two vectors is also a left-singular vector corresponding to the singular value ⁠ $\sigma$ ⁠. The similar statement is true for right-singular vectors. The numbers of independent left- and right-singular vectors coincide, and these singular vectors appear in the same columns of ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠: those corresponding to the diagonal elements of ⁠ $\mathbf {\Sigma }$ ⁠ with the same value ⁠ $\sigma$ ⁠.

As an exception, the left- and right-singular vectors of singular value ⁠ 0 ⁠ comprise all unit vectors in the cokernel and kernel, respectively, of ⁠ $\mathbf {M}$ ⁠. By the rank–nullity theorem, these subspaces cannot have the same dimension if ⁠ $m\neq n$ ⁠. Even when all singular values are non-zero, if ⁠ $m>n$ ⁠, then the cokernel is non-trivial, in which case ⁠ $\mathbf {U}$ ⁠ is padded with ⁠ $m-n$ ⁠ orthogonal [orthonormal?] vectors from the cokernel. Conversely, if ⁠ $m<n$ ⁠, then ⁠ $\mathbf {V}$ ⁠ is padded by ⁠ $n-m$ ⁠ orthogonal [orthonormal?] vectors from the kernel. However, if the singular value ⁠ 0 ⁠ exists, the extra columns of ⁠ $\mathbf {U}$ ⁠ or ⁠ $\mathbf {V}$ ⁠ already appear as left- or right-singular vectors.

Non-degenerate singular values always have unique left- and right-singular vectors, up to multiplication by a (unit) phase factor ⁠ $e^{i\varphi }$ ⁠ (for the real case, up to a sign). Consequently, if all singular values of a square matrix ⁠ $\mathbf {M}$ ⁠ are non-degenerate and non-zero, then its singular value decomposition is unique, up to multiplication of a column of ⁠ $\mathbf {U}$ ⁠ by a (unit) phase factor and simultaneous multiplication of the corresponding column of ⁠ $\mathbf {V}$ ⁠ by the same (unit) phase factor.

In general, the SVD is unique up to arbitrary unitary transformations applied uniformly to the column vectors of both ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ of ⁠ $\mathbf {M}$ ⁠.

### Relation to eigenvalue decomposition

The singular value decomposition is very general in the sense that it can be applied to any ⁠ $m\times n$ ⁠ matrix, whereas eigenvalue decomposition can only be applied to square diagonalizable matrices. Nevertheless, the two decompositions are related.

If ⁠ $\mathbf {M}$ ⁠ has SVD ⁠ $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*},$ ⁠ the following two relations hold: ${\begin{aligned}\mathbf {M} ^{*}\mathbf {M} &=\mathbf {V} \mathbf {\Sigma } ^{*}\mathbf {U} ^{*}\,\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}=\mathbf {V} (\mathbf {\Sigma } ^{*}\mathbf {\Sigma } )\mathbf {V} ^{*},\\[3mu]\mathbf {M} \mathbf {M} ^{*}&=\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}\,\mathbf {V} \mathbf {\Sigma } ^{*}\mathbf {U} ^{*}=\mathbf {U} (\mathbf {\Sigma } \mathbf {\Sigma } ^{*})\mathbf {U} ^{*}.\end{aligned}}$

The right-hand sides of these relations describe the eigenvalue decompositions of the left-hand sides. Consequently:

- The columns of ⁠ $\mathbf {V}$ ⁠ (referred to as right-singular vectors) are eigenvectors of ⁠ $\mathbf {M} ^{*}\mathbf {M} .$ ⁠
- The columns of ⁠ $\mathbf {U}$ ⁠ (referred to as left-singular vectors) are eigenvectors of ⁠ $\mathbf {M} \mathbf {M} ^{*}.$ ⁠
- The non-zero elements of ⁠ $\mathbf {\Sigma }$ ⁠ (non-zero singular values) are the square roots of the non-zero eigenvalues of ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠ or ⁠ $\mathbf {M} \mathbf {M} ^{*}.$ ⁠

In the special case of ⁠ $\mathbf {M}$ ⁠ being a normal matrix, and thus also square, the spectral theorem ensures that it can be unitarily diagonalized using a basis of eigenvectors, and thus decomposed as ⁠ $\mathbf {M} =\mathbf {U} \mathbf {D} \mathbf {U} ^{*}$ ⁠ for some unitary matrix ⁠ $\mathbf {U}$ ⁠ and diagonal matrix ⁠ $\mathbf {D}$ ⁠ with complex elements ⁠ $\sigma _{i}$ ⁠ along the diagonal. When ⁠ $\mathbf {M}$ ⁠ is positive semi-definite, ⁠ $\sigma _{i}$ ⁠ will be non-negative real numbers so that the decomposition ⁠ $\mathbf {M} =\mathbf {U} \mathbf {D} \mathbf {U} ^{*}$ ⁠ is also a singular value decomposition. Otherwise, it can be recast as an SVD by moving the phase ⁠ $e^{i\varphi }$ ⁠ of each ⁠ $\sigma _{i}$ ⁠ to either its corresponding ⁠ $\mathbf {V} _{i}$ ⁠ or ⁠ $\mathbf {U} _{i}.$ ⁠ The natural connection of the SVD to non-normal matrices is through the polar decomposition theorem: ⁠ $\mathbf {M} =\mathbf {S} \mathbf {R} ,$ ⁠ where ⁠ $\mathbf {S} =\mathbf {U} \mathbf {\Sigma } \mathbf {U} ^{*}$ ⁠ is positive semidefinite and normal, and ⁠ $\mathbf {R} =\mathbf {U} \mathbf {V} ^{*}$ ⁠ is unitary.

Thus, except for positive semi-definite matrices, the eigenvalue decomposition and SVD of ⁠ $\mathbf {M} ,$ ⁠ while related, differ: the eigenvalue decomposition is ⁠ $\mathbf {M} =\mathbf {U} \mathbf {D} \mathbf {U} ^{-1},$ ⁠ where ⁠ $\mathbf {U}$ ⁠ is not necessarily unitary and ⁠ $\mathbf {D}$ ⁠ is not necessarily positive semi-definite, while the SVD is ⁠ $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*},$ ⁠ where ⁠ $\mathbf {\Sigma }$ ⁠ is diagonal and positive semi-definite, and ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V}$ ⁠ are unitary matrices that are not necessarily related except through the matrix ⁠ $\mathbf {M} .$ ⁠ While only non-defective square matrices have an eigenvalue decomposition, any ⁠ $m\times n$ ⁠ matrix has a SVD.


## Applications of the SVD

### Pseudoinverse

The singular value decomposition can be used for computing the pseudoinverse of a matrix. The pseudoinverse of the matrix ⁠ $\mathbf {M}$ ⁠ with singular value decomposition ⁠ $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}$ ⁠ is $\mathbf {M} ^{+}=\mathbf {V} {\boldsymbol {\Sigma }}^{+}\mathbf {U} ^{\ast },$ where ${\boldsymbol {\Sigma }}^{+}$ is the pseudoinverse of ${\boldsymbol {\Sigma }}$ , which is formed by replacing every non-zero diagonal entry by its reciprocal and transposing the resulting matrix. The pseudoinverse is one way to solve linear least squares problems.

### Solving homogeneous linear equations

A set of homogeneous linear equations can be written as ⁠ $\mathbf {A} \mathbf {x} =\mathbf {0}$ ⁠ for a matrix ⁠ $\mathbf {A}$ ⁠, vector ⁠ $\mathbf {x}$ ⁠, and zero vector ⁠ $\mathbf {0}$ ⁠. A typical situation is that ⁠ $\mathbf {A}$ ⁠ is known and a non-zero ⁠ $\mathbf {x}$ ⁠ is to be determined which satisfies the equation. Such an ⁠ $\mathbf {x}$ ⁠ belongs to ⁠ $\mathbf {A}$ ⁠'s null space and is sometimes called a (right) null vector of ⁠ $\mathbf {A} .$ ⁠ The vector ⁠ $\mathbf {x}$ ⁠ can be characterized as a right-singular vector corresponding to a singular value of ⁠ $\mathbf {A}$ ⁠ that is zero. This observation means that if ⁠ $\mathbf {A}$ ⁠ is a square matrix and has no vanishing singular value, the equation has no non-zero ⁠ $\mathbf {x}$ ⁠ as a solution. It also means that if there are several vanishing singular values, any linear combination of the corresponding right-singular vectors is a valid solution. Analogously to the definition of a (right) null vector, a non-zero ⁠ $\mathbf {x}$ ⁠ satisfying ⁠ $\mathbf {x} ^{*}\mathbf {A} =\mathbf {0}$ ⁠ with ⁠ $\mathbf {x} ^{*}$ ⁠ denoting the conjugate transpose of ⁠ $\mathbf {x}$ ⁠ is called a left null vector of ⁠ $\mathbf {A} .$ ⁠

### Total least squares minimization

A total least squares problem seeks the vector ⁠ $\mathbf {x}$ ⁠ that minimizes the 2-norm of a vector ⁠ $\mathbf {A} \mathbf {x}$ ⁠ under the constraint $\|\mathbf {x} \|=1.$ The solution turns out to be the right-singular vector of ⁠ $\mathbf {A}$ ⁠ corresponding to the smallest singular value.

### Range, null space and rank

Another application of the SVD is that it provides an explicit representation of the range and null space of a matrix ⁠ $\mathbf {M} .$ ⁠ The right-singular vectors corresponding to vanishing singular values of ⁠ $\mathbf {M}$ ⁠ span the null space of ⁠ $\mathbf {M}$ ⁠ and the left-singular vectors corresponding to the non-zero singular values of ⁠ $\mathbf {M}$ ⁠ span the range of ⁠ $\mathbf {M} .$ ⁠

As a consequence, the rank of ⁠ $\mathbf {M}$ ⁠ equals the number of non-zero singular values which is the same as the number of non-zero diagonal elements in $\mathbf {\Sigma }$ . In numerical linear algebra the singular values can be used to determine the *effective rank* of a matrix, as rounding error may lead to small but non-zero singular values in a rank deficient matrix. Singular values beyond a significant gap are assumed to be numerically equivalent to zero.

### Low-rank matrix approximation

Some practical applications need to solve the problem of approximating a matrix ⁠ $\mathbf {M}$ ⁠ with another matrix ${\tilde {\mathbf {M} }}$ , said to be truncated, which has a specific rank ⁠ r ⁠. In the case that the approximation is based on minimizing the Frobenius norm of the difference between ⁠ $\mathbf {M}$ ⁠ and ⁠ ${\tilde {\mathbf {M} }}$ ⁠ under the constraint that $\operatorname {rank} {\bigl (}{\tilde {\mathbf {M} }}{\bigr )}=r,$ it turns out that the solution is given by the SVD of ⁠ $\mathbf {M} ,$ ⁠ namely ${\tilde {\mathbf {M} }}=\mathbf {U} {\tilde {\mathbf {\Sigma } }}\mathbf {V} ^{*},$ where ${\tilde {\mathbf {\Sigma } }}$ is the same matrix as $\mathbf {\Sigma }$ except that it contains only the ⁠ r ⁠ largest singular values (the other singular values are replaced by zero). This is known as the **Eckart–Young theorem**, as it was proved by those two authors in 1936.

### Image compression

One practical consequence of the low-rank approximation given by SVD is that a greyscale image represented as an $m\times n$ matrix $\mathbf {A}$ , can be efficiently represented by keeping the first k singular values and corresponding vectors. The truncated decomposition

$\mathbf {A} _{k}=\sum _{j=1}^{k}\sigma _{j}\mathbf {u} _{j}\mathbf {v} _{j}^{T}$ gives an image with the best 2-norm error out of all rank k approximations. Thus, the task becomes finding an approximation that balances retaining perceptual fidelity with the number of vectors required to reconstruct the image. Storing $\mathbf {A} _{k}$ requires only $k(n+m+1)$ floating-point numbers compared to $nm$ integers. This same idea extends to color images by applying this operation to each channel or stacking the channels into one matrix.

Since the singular values of most natural images decay quickly, most of their variance is often captured by a small k . For a 1528 × 1225 greyscale image, we can achieve a relative error of $.7\%$ with as little as $k=100$ . In practice, however, computing the SVD can be too computationally expensive and the resulting compression is typically less storage efficient than a specialized algorithm such as JPEG.

### Separable models

The SVD can be thought of as decomposing a matrix into a weighted, ordered sum of separable matrices. By separable, we mean that a matrix ⁠ $\mathbf {A}$ ⁠ can be written as an outer product of two vectors ⁠ $\mathbf {A} =\mathbf {u} \otimes \mathbf {v} ,$ ⁠ or, in coordinates, ⁠ $A_{ij}=u_{i}v_{j}.$ ⁠ Specifically, the matrix ⁠ $\mathbf {M}$ ⁠ can be decomposed as,

$\mathbf {M} =\sum _{i}\mathbf {A} _{i}=\sum _{i}\sigma _{i}\mathbf {U} _{i}\otimes \mathbf {V} _{i}.$

Here ⁠ $\mathbf {U} _{i}$ ⁠ and ⁠ $\mathbf {V} _{i}$ ⁠ are the ⁠ i ⁠-th columns of the corresponding SVD matrices, ⁠ $\sigma _{i}$ ⁠ are the ordered singular values, and each ⁠ $\mathbf {A} _{i}$ ⁠ is separable. The SVD can be used to find the decomposition of an image processing filter into separable horizontal and vertical filters. Note that the number of non-zero ⁠ $\sigma _{i}$ ⁠ is exactly the rank of the matrix. Separable models often arise in biological systems, and the SVD factorization is useful to analyze such systems. For example, some visual area V1 simple cells' receptive fields can be well described by a Gabor filter in the space domain multiplied by a modulation function in the time domain. Thus, given a linear filter evaluated through, for example, reverse correlation, one can rearrange the two spatial dimensions into one dimension, thus yielding a two-dimensional filter (space, time) which can be decomposed through SVD. The first column of ⁠ $\mathbf {U}$ ⁠ in the SVD factorization is then a Gabor while the first column of ⁠ $\mathbf {V}$ ⁠ represents the time modulation (or vice versa). One may then define an index of separability

$\alpha ={\frac {\sigma _{1}^{2}}{\sum _{i}\sigma _{i}^{2}}},$

which is the fraction of the power in the matrix M which is accounted for by the first separable matrix in the decomposition.

### Nearest orthogonal matrix

It is possible to use the SVD of a square matrix ⁠ $\mathbf {A}$ ⁠ to determine the orthogonal matrix ⁠ $\mathbf {Q}$ ⁠ closest to ⁠ $\mathbf {A} .$ ⁠ The closeness of fit is measured by the Frobenius norm of ⁠ $\mathbf {Q} -\mathbf {A} .$ ⁠ The solution is the product ⁠ $\mathbf {U} \mathbf {V} ^{*}.$ ⁠ This intuitively makes sense because an orthogonal matrix would have the decomposition ⁠ $\mathbf {U} \mathbf {I} \mathbf {V} ^{*}$ ⁠ where ⁠ $\mathbf {I}$ ⁠ is the identity matrix, so that if ⁠ $\mathbf {A} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}$ ⁠ then the product ⁠ $\mathbf {A} =\mathbf {U} \mathbf {V} ^{*}$ ⁠ amounts to replacing the singular values with ones. Equivalently, the solution is the unitary matrix ⁠ $\mathbf {R} =\mathbf {U} \mathbf {V} ^{*}$ ⁠ of the Polar Decomposition $\mathbf {M} =\mathbf {R} \mathbf {P} =\mathbf {P} '\mathbf {R}$ in either order of stretch and rotation, as described above.

A similar problem, with interesting applications in shape analysis, is the orthogonal Procrustes problem, which consists of finding an orthogonal matrix ⁠ $\mathbf {Q}$ ⁠ which most closely maps ⁠ $\mathbf {A}$ ⁠ to ⁠ $\mathbf {B} .$ ⁠ Specifically, $\mathbf {Q} ={\underset {\Omega }{\operatorname {argmin} }}\|\mathbf {A} {\boldsymbol {\Omega }}-\mathbf {B} \|_{F}\quad {\text{subject to}}\quad {\boldsymbol {\Omega }}^{\operatorname {T} }{\boldsymbol {\Omega }}=\mathbf {I} ,$ where $\|\cdot \|_{F}$ denotes the Frobenius norm.

This problem is equivalent to finding the nearest orthogonal matrix to a given matrix $\mathbf {M} =\mathbf {A} ^{\operatorname {T} }\mathbf {B}$ .

### The Kabsch algorithm

The Kabsch algorithm (called Wahba's problem in other fields) uses SVD to compute the optimal rotation (with respect to least-squares minimization) that will align a set of points with a corresponding set of points. It is used, among other applications, to compare the structures of molecules.

### Principal Component Analysis

The SVD can be used to construct the principal components in principal component analysis as follows:

Let $\mathbf {X} \in \mathbb {R} ^{N\times p}$ be a data matrix where each of the N rows is a (feature-wise) mean-centered observation, each of dimension p .

The SVD of $\mathbf {X}$ is: $\mathbf {X} =\mathbf {V} {\boldsymbol {\Sigma }}\mathbf {U} ^{\ast }$

We see that $\mathbf {V} {\boldsymbol {\Sigma }}$ contains the scores of the rows of $\mathbf {X}$ (i.e. each observation), and $\mathbf {U}$ is the matrix whose columns are principal component loading vectors.

### Signal processing

The SVD and pseudoinverse have been successfully applied to signal processing, image processing and big data (e.g., in genomic signal processing).

### Other examples

The SVD is also applied extensively to the study of linear inverse problems and is useful in the analysis of regularization methods such as that of Tikhonov. It is widely used in statistics, where it is related to principal component analysis and to correspondence analysis, and in signal processing and pattern recognition. It is also used in output-only modal analysis, where the non-scaled mode shapes can be determined from the singular vectors. Yet another usage is latent semantic indexing in natural-language text processing.

In general numerical computation involving linear or linearized systems, there is a universal constant that characterizes the regularity or singularity of a problem, which is the system's "condition number" $\kappa :=\sigma _{\text{max}}/\sigma _{\text{min}}$ . It often controls the error rate or convergence rate of a given computational scheme on such systems.

The SVD also plays a crucial role in the field of quantum information, in a form often referred to as the Schmidt decomposition. Through it, states of two quantum systems are naturally decomposed, providing a necessary and sufficient condition for them to be entangled: if the rank of the $\mathbf {\Sigma }$ matrix is larger than one.

One application of SVD to rather large matrices is in numerical weather prediction, where Lanczos methods are used to estimate the most linearly quickly growing few perturbations to the central numerical weather prediction over a given initial forward time period; i.e., the singular vectors corresponding to the largest singular values of the linearized propagator for the global weather over that time interval. The output singular vectors in this case are entire weather systems. These perturbations are then run through the full nonlinear model to generate an ensemble forecast, giving a handle on some of the uncertainty that should be allowed for around the current central prediction.

SVD has also been applied to reduced order modelling. The aim of reduced order modelling is to reduce the number of degrees of freedom in a complex system which is to be modeled. SVD was coupled with radial basis functions to interpolate solutions to three-dimensional unsteady flow problems.

Interestingly, SVD has been used to improve gravitational waveform modeling by the ground-based gravitational-wave interferometer aLIGO. SVD can help to increase the accuracy and speed of waveform generation to support gravitational-waves searches and update two different waveform models.

Singular value decomposition is used in recommender systems to predict people's item ratings. Distributed algorithms have been developed for the purpose of calculating the SVD on clusters of commodity machines.

Low-rank SVD has been applied for hotspot detection from spatiotemporal data with application to disease outbreak detection. A combination of SVD and higher-order SVD also has been applied for real time event detection from complex data streams (multivariate data with space and time dimensions) in disease surveillance.

In astrodynamics, the SVD and its variants are used as an option to determine suitable maneuver directions for transfer trajectory design and orbital station-keeping.

The SVD can be used to measure the similarity between real-valued matrices. By measuring the angles between the singular vectors, the inherent two-dimensional structure of matrices is accounted for. This method was shown to outperform cosine similarity and Frobenius norm in most cases, including brain activity measurements from neuroscience experiments.

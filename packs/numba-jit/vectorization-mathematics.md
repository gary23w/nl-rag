---
title: "Vectorization (mathematics)"
source: https://en.wikipedia.org/wiki/Vectorization_(mathematics)
domain: numba-jit
license: BSD-3-Clause
tags: numba compiler, just-in-time compilation, automatic vectorization, llvm backend
fetched: 2026-07-02
---

# Vectorization (mathematics)

In mathematics, especially in linear algebra and matrix theory, the **vectorization** of a matrix is a linear transformation which converts the matrix into a vector. Specifically, the vectorization of a *m* × *n* matrix *A*, denoted vec(*A*), is the *mn* × 1 column vector obtained by stacking the columns of the matrix *A* on top of one another: $\operatorname {vec} (A)=[a_{1,1},\ldots ,a_{m,1},a_{1,2},\ldots ,a_{m,2},\ldots ,a_{1,n},\ldots ,a_{m,n}]^{\mathrm {\top } }$ Here, $a_{i,j}$ represents the element in the *i*-th row and *j*-th column of *A*, and the superscript ${}^{\mathrm {\top } }$ denotes the transpose. In other words, vec(*A*) is a vector containing the entries of *A* in column-major order.

Vectorization expresses, through coordinates, the isomorphism $\mathbf {R} ^{m\times n}\cong \mathbf {R} ^{mn}$ between these (i.e., of matrices and vectors) as vector spaces.

For example, for the 2×2 matrix $A={\begin{bmatrix}a&b\\c&d\end{bmatrix}}$ , the vectorization is $\operatorname {vec} (A)={\begin{bmatrix}a\\c\\b\\d\end{bmatrix}}$ .

The connection between the vectorization of *A* and the vectorization of its transpose is given by the commutation matrix.

## Compatibility with Kronecker products

The vectorization is frequently used together with the Kronecker product to express matrix multiplication as a linear transformation on matrices. In particular, $\operatorname {vec} (ABC)=(C^{\mathrm {\top } }\otimes A)\operatorname {vec} (B)$ for matrices *A*, *B*, and *C* of dimensions *k*×*l*, *l*×*m*, and *m*×*n*. For example, if $\operatorname {ad} _{A}(X)=AX-XA$ (the adjoint endomorphism of the Lie algebra gl(*n*, **C**) of all *n*×*n* matrices with complex entries), then $\operatorname {vec} (\operatorname {ad} _{A}(X))=(A\otimes I_{n}-I_{n}\otimes A^{\mathrm {\top } }){\text{vec}}(X)$ , where $I_{n}$ is the *n*×*n* identity matrix.

There are two other useful formulations: ${\begin{aligned}\operatorname {vec} (ABC)&=(I_{n}\otimes AB)\operatorname {vec} (C)=(C^{\mathrm {\top } }B^{\mathrm {\top } }\otimes I_{k})\operatorname {vec} (A)\\\operatorname {vec} (AB)&=(I_{m}\otimes A)\operatorname {vec} (B)=(B^{\mathrm {\top } }\otimes I_{k})\operatorname {vec} (A)\end{aligned}}$

If *B* is a diagonal matrix (i.e., ${\textstyle B=\operatorname {diag} (b_{1},\dots ,b_{n})}$ ), the vectorization can be written using the column-wise Kronecker product ${\textstyle \ast }$ (see Khatri-Rao product) and the main diagonal ${\textstyle b={\begin{bmatrix}b_{1},\dots ,b_{n}\end{bmatrix}}^{\mathrm {\top } }}$ of *B*: $\operatorname {vec} (ABC)=(C^{\mathrm {\top } }\ast A)b$

More generally, it has been shown that vectorization is a self-adjunction in the monoidal closed structure of any category of matrices.

## Compatibility with Hadamard products

Vectorization is an algebra homomorphism from the space of *n* × *n* matrices with the Hadamard (entrywise) product to **C***n*2 with its Hadamard product: $\operatorname {vec} (A\circ B)=\operatorname {vec} (A)\circ \operatorname {vec} (B).$

## Compatibility with inner products

Vectorization is a unitary transformation from the space of *n*×*n* matrices with the Frobenius (or Hilbert–Schmidt) inner product to **C***n*2: $\operatorname {tr} (A^{\dagger }B)=\operatorname {vec} (A)^{\dagger }\operatorname {vec} (B),$ where the superscript † denotes the conjugate transpose.

## Vectorization as a linear sum

The matrix vectorization operation can be written in terms of a linear sum. Let **X** be an *m* × *n* matrix that we want to vectorize, and let **e***i* be the *i*-th canonical basis vector for the *n*-dimensional space, that is ${\textstyle \mathbf {e} _{i}=\left[0,\dots ,0,1,0,\dots ,0\right]^{\mathrm {T} }}$ . Let **B***i* be a (*mn*) × *m* block matrix defined as follows: $\mathbf {B} _{i}={\begin{bmatrix}\mathbf {0} \\\vdots \\\mathbf {0} \\\mathbf {I} _{m}\\\mathbf {0} \\\vdots \\\mathbf {0} \end{bmatrix}}=\mathbf {e} _{i}\otimes \mathbf {I} _{m}$

**B***i* consists of *n* block matrices of size *m* × *m*, stacked column-wise, and all these matrices are all-zero except for the *i*-th one, which is a *m* × *m* identity matrix **I***m*.

Then the vectorized version of **X** can be expressed as follows: $\operatorname {vec} (\mathbf {X} )=\sum _{i=1}^{n}\mathbf {B} _{i}\mathbf {X} \mathbf {e} _{i}$

Multiplication of **X** by **e***i* extracts the *i*-th column, while multiplication by **B***i* puts it into the desired position in the final vector.

Alternatively, the linear sum can be expressed using the Kronecker product: $\operatorname {vec} (\mathbf {X} )=\sum _{i=1}^{n}\mathbf {e} _{i}\otimes \mathbf {X} \mathbf {e} _{i}$

## Half-vectorization

For a symmetric matrix *A*, the vector vec(*A*) contains more information than is strictly necessary, since the matrix is completely determined by the symmetry together with the lower triangular portion, that is, the *n*(*n* + 1)/2 entries on and below the main diagonal. For such matrices, the **half-vectorization** is sometimes more useful than the vectorization. The half-vectorization, vech(*A*), of a symmetric *n* × *n* matrix *A* is the *n*(*n* + 1)/2 × 1 column vector obtained by vectorizing only the lower triangular part of *A*: $\operatorname {vech} (A)=[A_{1,1},\ldots ,A_{n,1},A_{2,2},\ldots ,A_{n,2},\ldots ,A_{n-1,n-1},A_{n,n-1},A_{n,n}]^{\mathrm {\top } }.$

For example, for the 2×2 matrix $A={\begin{bmatrix}a&b\\b&d\end{bmatrix}}$ , the half-vectorization is $\operatorname {vech} (A)={\begin{bmatrix}a\\b\\d\end{bmatrix}}$ .

There exist unique matrices transforming the half-vectorization of a matrix to its vectorization and vice versa called, respectively, the duplication matrix and the elimination matrix.

## Programming language

Programming languages that implement matrices may have easy means for vectorization. In Matlab/GNU Octave a matrix `A` can be vectorized by `A(:)`. GNU Octave also allows vectorization and half-vectorization with `vec(A)` and `vech(A)` respectively. Julia has the `vec(A)` function as well. In Python NumPy arrays implement the `flatten` method, while in R the desired effect can be achieved via the `c()` or `as.vector()` functions or, more efficiently, by removing the dimensions attribute of a matrix `A` with `dim(A) <- NULL`. In R, function `vec()` of package 'ks' allows vectorization and function `vech()` implemented in both packages 'ks' and 'sn' allows half-vectorization.

## Applications

Vectorization is used in matrix calculus and its applications in establishing e.g., moments of random vectors and matrices, asymptotics, as well as Jacobian and Hessian matrices. It is also used in local sensitivity and statistical diagnostics.

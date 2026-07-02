---
title: "Singular value decomposition (part 2/2)"
source: https://en.wikipedia.org/wiki/Singular_value_decomposition
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
part: 2/2
---

## Proof of existence

An eigenvalue ⁠ $\lambda$ ⁠ of a matrix ⁠ $\mathbf {M}$ ⁠ is characterized by the algebraic relation ⁠ $\mathbf {M} \mathbf {u} =\lambda \mathbf {u} .$ ⁠ When ⁠ $\mathbf {M}$ ⁠ is Hermitian, a variational characterization is also available. Let ⁠ $\mathbf {M}$ ⁠ be a real ⁠ $n\times n$ ⁠ symmetric matrix. Define

$f:\left\{{\begin{aligned}\mathbb {R} ^{n}&\to \mathbb {R} \\\mathbf {x} &\mapsto \mathbf {x} ^{\operatorname {T} }\mathbf {M} \mathbf {x} \end{aligned}}\right.$

By the extreme value theorem, this continuous function attains a maximum at some ⁠ $\mathbf {u}$ ⁠ when restricted to the unit sphere $\{\|\mathbf {x} \|=1\}.$ By the Lagrange multipliers theorem, ⁠ $\mathbf {u}$ ⁠ necessarily satisfies $\nabla \mathbf {u} ^{\operatorname {T} }\mathbf {M} \mathbf {u} -\lambda \cdot \nabla \mathbf {u} ^{\operatorname {T} }\mathbf {u} =\mathbf {0}$ for some real number ⁠ $\lambda .$ ⁠ The nabla symbol, ⁠ $\nabla$ ⁠, is the del operator (differentiation with respect to ⁠ $\mathbf {x}$ ⁠). Using the symmetry of ⁠ $\mathbf {M}$ ⁠ we obtain $\nabla \mathbf {x} ^{\operatorname {T} }\mathbf {M} \mathbf {x} -\lambda \cdot \nabla \mathbf {x} ^{\operatorname {T} }\mathbf {x} =2(\mathbf {M} -\lambda \mathbf {I} )\mathbf {x} .$

Therefore ⁠ $\mathbf {M} \mathbf {u} =\lambda \mathbf {u} ,$ ⁠ so ⁠ $\mathbf {u}$ ⁠ is a unit length eigenvector of ⁠ $\mathbf {M} .$ ⁠ For every unit length eigenvector ⁠ $\mathbf {v}$ ⁠ of ⁠ $\mathbf {M}$ ⁠ its eigenvalue is ⁠ $f(\mathbf {v} ),$ ⁠ so ⁠ $\lambda$ ⁠ is the largest eigenvalue of ⁠ $\mathbf {M} .$ ⁠ The same calculation performed on the orthogonal complement of ⁠ $\mathbf {u}$ ⁠ gives the next largest eigenvalue and so on. The complex Hermitian case is similar; there ⁠ $f(\mathbf {x} )=\mathbf {x} ^{*}\mathbf {M} \mathbf {x}$ ⁠ is a real-valued function of ⁠ $2n$ ⁠ real variables.

Singular values are similar in that they can be described algebraically or from variational principles. Although, unlike the eigenvalue case, Hermiticity, or symmetry, of ⁠ $\mathbf {M}$ ⁠ is no longer required.

This section gives these two arguments for existence of singular value decomposition.

### Based on the spectral theorem

Let $\mathbf {M}$ be an ⁠ $m\times n$ ⁠ complex matrix. Since $\mathbf {M} ^{*}\mathbf {M}$ is positive semi-definite and Hermitian, by the spectral theorem, there exists an ⁠ $n\times n$ ⁠ unitary matrix $\mathbf {V}$ such that $\mathbf {V} ^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} ={\bar {\mathbf {D} }}={\begin{bmatrix}\mathbf {D} &0\\0&0\end{bmatrix}},$ where $\mathbf {D}$ is diagonal and positive definite, of dimension $\ell \times \ell$ , with $\ell$ the number of non-zero eigenvalues of $\mathbf {M} ^{*}\mathbf {M}$ (which can be shown to verify $\ell \leq \min(n,m)$ ). Note that $\mathbf {V}$ is here by definition a matrix whose i -th column is the i -th eigenvector of $\mathbf {M} ^{*}\mathbf {M}$ , corresponding to the eigenvalue ${\bar {\mathbf {D} }}_{ii}$ . Moreover, the j -th column of $\mathbf {V}$ , for $j>\ell$ , is an eigenvector of $\mathbf {M} ^{*}\mathbf {M}$ with eigenvalue ${\bar {\mathbf {D} }}_{jj}=0$ . This can be expressed by writing $\mathbf {V}$ as $\mathbf {V} ={\begin{bmatrix}\mathbf {V} _{1}&\mathbf {V} _{2}\end{bmatrix}}$ , where the columns of $\mathbf {V} _{1}$ and $\mathbf {V} _{2}$ therefore contain the eigenvectors of $\mathbf {M} ^{*}\mathbf {M}$ corresponding to non-zero and zero eigenvalues, respectively. Using this rewriting of $\mathbf {V}$ , the equation becomes: ${\begin{bmatrix}\mathbf {V} _{1}^{*}\\\mathbf {V} _{2}^{*}\end{bmatrix}}\mathbf {M} ^{*}\mathbf {M} \,{\begin{bmatrix}\mathbf {V} _{1}&\!\!\mathbf {V} _{2}\end{bmatrix}}={\begin{bmatrix}\mathbf {V} _{1}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{1}&\mathbf {V} _{1}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{2}\\\mathbf {V} _{2}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{1}&\mathbf {V} _{2}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{2}\end{bmatrix}}={\begin{bmatrix}\mathbf {D} &0\\0&0\end{bmatrix}}.$

This implies that $\mathbf {V} _{1}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{1}=\mathbf {D} ,\quad \mathbf {V} _{2}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{2}=\mathbf {0} .$

Moreover, the second equation implies $\mathbf {M} \mathbf {V} _{2}=\mathbf {0}$ . Finally, the unitary-ness of $\mathbf {V}$ translates, in terms of $\mathbf {V} _{1}$ and $\mathbf {V} _{2}$ , into the following conditions: ${\begin{aligned}\mathbf {V} _{1}^{*}\mathbf {V} _{1}&=\mathbf {I} _{1},\\\mathbf {V} _{2}^{*}\mathbf {V} _{2}&=\mathbf {I} _{2},\\\mathbf {V} _{1}\mathbf {V} _{1}^{*}+\mathbf {V} _{2}\mathbf {V} _{2}^{*}&=\mathbf {I} _{12},\end{aligned}}$ where the subscripts on the identity matrices are used to remark that they are of different dimensions.

Let us now define $\mathbf {U} _{1}=\mathbf {M} \mathbf {V} _{1}\mathbf {D} ^{-{\frac {1}{2}}}.$

Then, $\mathbf {U} _{1}\mathbf {D} ^{\frac {1}{2}}\mathbf {V} _{1}^{*}=\mathbf {M} \mathbf {V} _{1}\mathbf {D} ^{-{\frac {1}{2}}}\mathbf {D} ^{\frac {1}{2}}\mathbf {V} _{1}^{*}=\mathbf {M} (\mathbf {I} -\mathbf {V} _{2}\mathbf {V} _{2}^{*})=\mathbf {M} -(\mathbf {M} \mathbf {V} _{2})\mathbf {V} _{2}^{*}=\mathbf {M} ,$

since $\mathbf {M} \mathbf {V} _{2}=\mathbf {0} .$ This can be also seen as immediate consequence of the fact that $\mathbf {M} \mathbf {V} _{1}\mathbf {V} _{1}^{*}=\mathbf {M}$ . This is equivalent to the observation that if $\{{\boldsymbol {v}}_{i}\}_{i=1}^{\ell }$ is the set of eigenvectors of $\mathbf {M} ^{*}\mathbf {M}$ corresponding to non-vanishing eigenvalues $\{\lambda _{i}\}_{i=1}^{\ell }$ , then $\{\mathbf {M} {\boldsymbol {v}}_{i}\}_{i=1}^{\ell }$ is a set of orthogonal vectors, and ${\bigl \{}\lambda _{i}^{-1/2}\mathbf {M} {\boldsymbol {v}}_{i}{\bigr \}}{\vphantom {|}}_{i=1}^{\ell }$ is a (generally not complete) set of *orthonormal* vectors. This matches with the matrix formalism used above denoting with $\mathbf {V} _{1}$ the matrix whose columns are $\{{\boldsymbol {v}}_{i}\}_{i=1}^{\ell }$ , with $\mathbf {V} _{2}$ the matrix whose columns are the eigenvectors of $\mathbf {M} ^{*}\mathbf {M}$ with vanishing eigenvalue, and $\mathbf {U} _{1}$ the matrix whose columns are the vectors ${\bigl \{}\lambda _{i}^{-1/2}\mathbf {M} {\boldsymbol {v}}_{i}{\bigr \}}{\vphantom {|}}_{i=1}^{\ell }$ .

We see that this is almost the desired result, except that $\mathbf {U} _{1}$ and $\mathbf {V} _{1}$ are in general not unitary, since they might not be square. However, we do know that the number of rows of $\mathbf {U} _{1}$ is no smaller than the number of columns, since the dimensions of $\mathbf {D}$ is no greater than m and n . Also, since $\mathbf {U} _{1}^{*}\mathbf {U} _{1}=\mathbf {D} ^{-{\frac {1}{2}}}\mathbf {V} _{1}^{*}\mathbf {M} ^{*}\mathbf {M} \mathbf {V} _{1}\mathbf {D} ^{-{\frac {1}{2}}}=\mathbf {D} ^{-{\frac {1}{2}}}\mathbf {D} \mathbf {D} ^{-{\frac {1}{2}}}=\mathbf {I_{1}} ,$ the columns in $\mathbf {U} _{1}$ are orthonormal and can be extended to an orthonormal basis. This means that we can choose $\mathbf {U} _{2}$ such that $\mathbf {U} ={\begin{bmatrix}\mathbf {U} _{1}&\mathbf {U} _{2}\end{bmatrix}}$ is unitary.

For ⁠ $\mathbf {V} _{1}$ ⁠ we already have ⁠ $\mathbf {V} _{2}$ ⁠ to make it unitary. Now, define $\mathbf {\Sigma } ={\begin{bmatrix}{\begin{bmatrix}\mathbf {D} ^{\frac {1}{2}}&0\\0&0\end{bmatrix}}\\0\end{bmatrix}},$

where extra zero rows are added **or removed** to make the number of zero rows equal the number of columns of ⁠ $\mathbf {U} _{2},$ ⁠ and hence the overall dimensions of $\mathbf {\Sigma }$ equal to $m\times n$ . Then ${\begin{bmatrix}\mathbf {U} _{1}&\mathbf {U} _{2}\end{bmatrix}}{\begin{bmatrix}{\begin{bmatrix}\mathbf {} D^{\frac {1}{2}}&0\\0&0\end{bmatrix}}\\0\end{bmatrix}}{\begin{bmatrix}\mathbf {V} _{1}&\mathbf {V} _{2}\end{bmatrix}}^{*}={\begin{bmatrix}\mathbf {U} _{1}&\mathbf {U} _{2}\end{bmatrix}}{\begin{bmatrix}\mathbf {D} ^{\frac {1}{2}}\mathbf {V} _{1}^{*}\\0\end{bmatrix}}=\mathbf {U} _{1}\mathbf {D} ^{\frac {1}{2}}\mathbf {V} _{1}^{*}=\mathbf {M} ,$ which is the desired result: $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}.$

Notice the argument could begin with diagonalizing ⁠ $\mathbf {M} \mathbf {M} ^{*}$ ⁠ rather than ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠ (This shows directly that ⁠ $\mathbf {M} \mathbf {M} ^{*}$ ⁠ and ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠ have the same non-zero eigenvalues).

### Based on variational characterization

The singular values can also be characterized as the maxima of ⁠ $\mathbf {u} ^{\mathrm {T} }\mathbf {M} \mathbf {v} ,$ ⁠ considered as a function of ⁠ $\mathbf {u}$ ⁠ and ⁠ $\mathbf {v} ,$ ⁠ over particular subspaces. The singular vectors are the values of ⁠ $\mathbf {u}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ where these maxima are attained.

Let ⁠ $\mathbf {M}$ ⁠ denote an ⁠ $m\times n$ ⁠ matrix with real entries. Let ⁠ $S^{k-1}$ ⁠ be the unit $(k-1)$ -sphere in $\mathbb {R} ^{k}$ , and define $\sigma (\mathbf {u} ,\mathbf {v} )=\mathbf {u} ^{\operatorname {T} }\mathbf {M} \mathbf {v} ,$ $\mathbf {u} \in S^{m-1},$ $\mathbf {v} \in S^{n-1}.$

Consider the function ⁠ $\sigma$ ⁠ restricted to ⁠ $S^{m-1}\times S^{n-1}.$ ⁠ Since both ⁠ $S^{m-1}$ ⁠ and ⁠ $S^{n-1}$ ⁠ are compact sets, their product is also compact. Furthermore, since ⁠ $\sigma$ ⁠ is continuous, it attains a largest value for at least one pair of vectors ⁠ $\mathbf {u}$ ⁠ in ⁠ $S^{m-1}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ in ⁠ $S^{n-1}.$ ⁠ This largest value is denoted ⁠ $\sigma _{1}$ ⁠ and the corresponding vectors are denoted ⁠ $\mathbf {u} _{1}$ ⁠ and ⁠ $\mathbf {v} _{1}.$ ⁠ Since ⁠ $\sigma _{1}$ ⁠ is the largest value of ⁠ $\sigma (\mathbf {u} ,\mathbf {v} )$ ⁠ it must be non-negative. If it were negative, changing the sign of either ⁠ $\mathbf {u} _{1}$ ⁠ or ⁠ $\mathbf {v} _{1}$ ⁠ would make it positive and therefore larger.

**Statement**—⁠ $\mathbf {u} _{1}$ ⁠ and ⁠ $\mathbf {v} _{1}$ ⁠ are left and right-singular vectors of ⁠ $\mathbf {M}$ ⁠ with corresponding singular value ⁠ $\sigma _{1}.$ ⁠

Proof

Similar to the eigenvalues case, by assumption the two vectors satisfy the Lagrange multiplier equation: $\nabla \sigma =\nabla \mathbf {u} ^{\operatorname {T} }\mathbf {M} \mathbf {v} -\lambda _{1}\cdot \nabla \mathbf {u} ^{\operatorname {T} }\mathbf {u} -\lambda _{2}\cdot \nabla \mathbf {v} ^{\operatorname {T} }\mathbf {v}$

After some algebra, this becomes ${\begin{aligned}\mathbf {M} \mathbf {v} _{1}&=2\lambda _{1}\mathbf {u} _{1}+0,\\\mathbf {M} ^{\operatorname {T} }\mathbf {u} _{1}&=0+2\lambda _{2}\mathbf {v} _{1}.\end{aligned}}$

Multiplying the first equation from left by ⁠ $\mathbf {u} _{1}^{\textrm {T}}$ ⁠ and the second equation from left by ⁠ $\mathbf {v} _{1}^{\textrm {T}}$ ⁠ and taking $\|\mathbf {u} \|=\|\mathbf {v} \|=1$ into account gives $\sigma _{1}=2\lambda _{1}=2\lambda _{2}.$

Plugging this into the pair of equations above, we have ${\begin{aligned}\mathbf {M} \mathbf {v} _{1}&=\sigma _{1}\mathbf {u} _{1},\\\mathbf {M} ^{\operatorname {T} }\mathbf {u} _{1}&=\sigma _{1}\mathbf {v} _{1}.\end{aligned}}$

This proves the statement.

More singular vectors and singular values can be found by maximizing ⁠ $\sigma (\mathbf {u} ,\mathbf {v} )$ ⁠ over normalized ⁠ $\mathbf {u}$ ⁠ and ⁠ $\mathbf {v}$ ⁠ which are orthogonal to ⁠ $\mathbf {u} _{1}$ ⁠ and ⁠ $\mathbf {v} _{1},$ ⁠ respectively.

The passage from real to complex is similar to the eigenvalue case.


## Calculating the SVD

### One-sided Jacobi algorithm

One-sided Jacobi algorithm is an iterative algorithm, where a matrix is iteratively transformed into a matrix with orthogonal columns. The elementary iteration is given as a Jacobi rotation, $M\leftarrow MJ(p,q,\theta ),$ where the angle $\theta$ of the Jacobi rotation matrix $J(p,q,\theta )$ is chosen such that after the rotation the columns with numbers p and q become orthogonal. The indices $(p,q)$ are swept cyclically, $(p=1\dots m,q=p+1\dots m)$ , where m is the number of columns.

After the algorithm has converged, the singular value decomposition $M=USV^{T}$ is recovered as follows: the matrix V is the accumulation of Jacobi rotation matrices, the matrix U is given by normalising the columns of the transformed matrix M , and the singular values are given as the norms of the columns of the transformed matrix M .

### Two-sided Jacobi algorithm

Two-sided Jacobi SVD algorithm—a generalization of the Jacobi eigenvalue algorithm—is an iterative algorithm where a square matrix is iteratively transformed into a diagonal matrix. If the matrix is not square the QR decomposition is performed first and then the algorithm is applied to the R matrix. The elementary iteration zeroes a pair of off-diagonal elements by first applying a Givens rotation to symmetrize the pair of elements and then applying a Jacobi transformation to zero them, $M\leftarrow J^{T}GMJ$ where G is the Givens rotation matrix with the angle chosen such that the given pair of off-diagonal elements become equal after the rotation, and where J is the Jacobi transformation matrix that zeroes these off-diagonal elements. The iterations proceeds exactly as in the Jacobi eigenvalue algorithm: by cyclic sweeps over all off-diagonal elements.

After the algorithm has converged the resulting diagonal matrix contains the singular values. The matrices U and V are accumulated as follows: ${\begin{aligned}U&\leftarrow UG^{T}J,\\V&\leftarrow VJ.\end{aligned}}$

### Numerical approach

The singular value decomposition can be computed using the following observations:

- The left-singular vectors of ⁠ $\mathbf {M}$ ⁠ are a set of orthonormal eigenvectors of ⁠ $\mathbf {M} \mathbf {M} ^{*}$ ⁠.
- The right-singular vectors of ⁠ $\mathbf {M}$ ⁠ are a set of orthonormal eigenvectors of ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠.
- The non-zero singular values of ⁠ $\mathbf {M}$ ⁠ (found on the diagonal entries of $\mathbf {\Sigma }$ ) are the square roots of the non-zero eigenvalues of both ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠ and ⁠ $\mathbf {M} \mathbf {M} ^{*}$ ⁠.

The SVD of a matrix ⁠ $\mathbf {M}$ ⁠ is typically computed by a two-step procedure. In the first step, the matrix is reduced to a bidiagonal matrix. This takes order ⁠ $O(mn^{2})$ ⁠ floating-point operations (*flop*), assuming that ⁠ $m\geq n.$ ⁠ The second step is to compute the SVD of the bidiagonal matrix. This step can only be done with an iterative method (as with eigenvalue algorithms). However, in practice it suffices to compute the SVD up to a certain precision, like the machine epsilon. If this precision is considered constant, then the second step takes ⁠ $O(n)$ ⁠ iterations, each costing ⁠ $O(n)$ ⁠ flops. Thus, the first step is more expensive, and the overall cost is ⁠ $O(mn^{2})$ ⁠ flops.

The first step can be done using Householder reflections for a cost of ⁠ $4mn^{2}-4n^{3}/3$ ⁠ flops, assuming that only the singular values are needed and not the singular vectors. If ⁠ m ⁠ is much larger than ⁠ n ⁠ then it is advantageous to first reduce the matrix ⁠ $\mathbf {M}$ ⁠ to a triangular matrix with the QR decomposition and then use Householder reflections to further reduce the matrix to bidiagonal form; the combined cost is ⁠ $2mn^{2}+2n^{3}$ ⁠ flops.

The second step can be done by a variant of the QR algorithm for the computation of eigenvalues, which was first described by Golub and Kahan in 1965. The LAPACK subroutine `DBDSQR` implements this iterative method, with some modifications to cover the case where the singular values are very small. Together with a first step using Householder reflections and, if appropriate, QR decomposition, this forms the `DGESVD` routine for the computation of the singular value decomposition.

The same algorithm is implemented in the GNU Scientific Library (GSL). The GSL also offers an alternative method that uses a one-sided Jacobi orthogonalization in step 2. This method computes the SVD of the bidiagonal matrix by solving a sequence of ⁠ $2\times 2$ ⁠ SVD problems, similar to how the Jacobi eigenvalue algorithm solves a sequence of ⁠ $2\times 2$ ⁠ eigenvalue methods. Yet another method for step 2 uses the idea of divide-and-conquer eigenvalue algorithms.

There is an alternative way that does not explicitly use the eigenvalue decomposition. Usually the singular value problem of a matrix ⁠ $\mathbf {M}$ ⁠ is converted into an equivalent symmetric eigenvalue problem such as ⁠ $\mathbf {M} \mathbf {M} ^{*},$ ⁠ ⁠ $\mathbf {M} ^{*}\mathbf {M} ,$ ⁠ or

${\begin{bmatrix}\mathbf {0} &\mathbf {M} \\\mathbf {M} ^{*}&\mathbf {0} \end{bmatrix}}.$

The approaches that use eigenvalue decompositions are based on the QR algorithm, which is well-developed to be stable and fast. Note that the singular values are real and right- and left- singular vectors are not required to form similarity transformations. One can iteratively alternate between the QR decomposition and the LQ decomposition to find the real diagonal Hermitian matrices. The QR decomposition gives ⁠ $\mathbf {M} \Rightarrow \mathbf {Q} \mathbf {R}$ ⁠ and the LQ decomposition of ⁠ $\mathbf {R}$ ⁠ gives ⁠ $\mathbf {R} \Rightarrow \mathbf {L} \mathbf {P} ^{*}.$ ⁠ Thus, at every iteration, we have ⁠ $\mathbf {M} \Rightarrow \mathbf {Q} \mathbf {L} \mathbf {P} ^{*},$ ⁠ update ⁠ $\mathbf {M} \Leftarrow \mathbf {L}$ ⁠ and repeat the orthogonalizations. Eventually, this iteration between QR decomposition and LQ decomposition produces left- and right- unitary singular matrices. This approach cannot readily be accelerated, as the QR algorithm can with spectral shifts or deflation. This is because the shift method is not easily defined without using similarity transformations. However, this iterative approach is very simple to implement, so is a good choice when speed does not matter. This method also provides insight into how purely orthogonal/unitary transformations can obtain the SVD.

### Computational complexity of SVD

The methods above yield ⁠ $O(mn^{2})$ ⁠ algorithms for the SVD of an $m\times n$ matrix M where $m\geq n$ .

Demmel, Dumitriu and Holtz show that for a symmetric M (i.e. $m=n$ ) the SVD can normwise stably be computed in $O(n^{\omega +\eta })$ arithmetic operations where $\omega$ is the matrix multiplication exponent and $\eta >0$ is any constant, i.e. essentially in matrix multiplication time.

### Analytic result of 2 × 2 SVD

The singular values of a ⁠ $2\times 2$ ⁠ matrix can be found analytically. Let the matrix be $\mathbf {M} =z_{0}\mathbf {I} +z_{1}\sigma _{1}+z_{2}\sigma _{2}+z_{3}\sigma _{3}$

where $z_{i}\in \mathbb {C}$ are complex numbers that parameterize the matrix, ⁠ $\mathbf {I}$ ⁠ is the identity matrix, and $\sigma _{i}$ denote the Pauli matrices. Then its two singular values are given by

${\begin{aligned}\sigma _{\pm }&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm {\sqrt {{\bigl (}|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}{\bigr )}^{2}-|z_{0}^{2}-z_{1}^{2}-z_{2}^{2}-z_{3}^{2}|^{2}}}}}\\&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm 2{\sqrt {(\operatorname {Re} z_{0}z_{1}^{*})^{2}+(\operatorname {Re} z_{0}z_{2}^{*})^{2}+(\operatorname {Re} z_{0}z_{3}^{*})^{2}+(\operatorname {Im} z_{1}z_{2}^{*})^{2}+(\operatorname {Im} z_{2}z_{3}^{*})^{2}+(\operatorname {Im} z_{3}z_{1}^{*})^{2}}}}}\end{aligned}}$


## Reduced SVDs

In applications it is quite unusual for the full SVD, including a full unitary decomposition of the null-space of the matrix, to be required. Instead, it is often sufficient (as well as faster, and more economical for storage) to compute a reduced version of the SVD. The following can be distinguished for an ⁠ $m\times n$ ⁠ matrix ⁠ $\mathbf {M}$ ⁠ of rank ⁠ r ⁠:

### Thin SVD

The thin, or economy-sized, SVD of a matrix ⁠ $\mathbf {M}$ ⁠ is given by

$\mathbf {M} =\mathbf {U} _{k}\mathbf {\Sigma } _{k}\mathbf {V} _{k}^{*},$

where $k=\min(m,n),$ the matrices ⁠ $\mathbf {U} _{k}$ ⁠ and ⁠ $\mathbf {V} _{k}$ ⁠ contain only the first ⁠ k ⁠ columns of ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ,$ ⁠ and ⁠ $\mathbf {\Sigma } _{k}$ ⁠ contains only the first ⁠ k ⁠ singular values from ⁠ $\mathbf {\Sigma } .$ ⁠ The matrix ⁠ $\mathbf {U} _{k}$ ⁠ is thus ⁠ $m\times k,$ ⁠ ⁠ $\mathbf {\Sigma } _{k}$ ⁠ is ⁠ $k\times k$ ⁠ diagonal, and ⁠ $\mathbf {V} _{k}^{*}$ ⁠ is ⁠ $k\times n.$ ⁠

The thin SVD uses significantly less space and computation time if ⁠ $k\ll \max(m,n).$ ⁠ The first stage in its calculation will usually be a QR decomposition of ⁠ $\mathbf {M} ,$ ⁠ which can make for a significantly quicker calculation in this case.

### Compact SVD

The compact SVD of a matrix ⁠ $\mathbf {M}$ ⁠ is given by

$\mathbf {M} =\mathbf {U} _{r}\mathbf {\Sigma } _{r}\mathbf {V} _{r}^{*}.$

Only the ⁠ r ⁠ column vectors of ⁠ $\mathbf {U}$ ⁠ and ⁠ r ⁠ row vectors of ⁠ $\mathbf {V} ^{*}$ ⁠ corresponding to the non-zero singular values ⁠ $\mathbf {\Sigma } _{r}$ ⁠ are calculated. The remaining vectors of ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ^{*}$ ⁠ are not calculated. This is quicker and more economical than the thin SVD if ⁠ $r\ll \min(m,n).$ ⁠ The matrix ⁠ $\mathbf {U} _{r}$ ⁠ is thus ⁠ $m\times r,$ ⁠ ⁠ $\mathbf {\Sigma } _{r}$ ⁠ is ⁠ $r\times r$ ⁠ diagonal, and ⁠ $\mathbf {V} _{r}^{*}$ ⁠ is ⁠ $r\times n.$ ⁠

### Truncated SVD

In many applications the number ⁠ r ⁠ of the non-zero singular values is large making even the Compact SVD impractical to compute. In such cases, the smallest singular values may need to be truncated to compute only ⁠ $t\ll r$ ⁠ non-zero singular values. The truncated SVD is no longer an exact decomposition of the original matrix ⁠ $\mathbf {M} ,$ ⁠ but rather provides the optimal low-rank matrix approximation ⁠ ${\tilde {\mathbf {M} }}$ ⁠ by any matrix of a fixed rank ⁠ t ⁠

${\tilde {\mathbf {M} }}=\mathbf {U} _{t}\mathbf {\Sigma } _{t}\mathbf {V} _{t}^{*},$

where matrix ⁠ $\mathbf {U} _{t}$ ⁠ is ⁠ $m\times t,$ ⁠ ⁠ $\mathbf {\Sigma } _{t}$ ⁠ is ⁠ $t\times t$ ⁠ diagonal, and ⁠ $\mathbf {V} _{t}^{*}$ ⁠ is ⁠ $t\times n.$ ⁠ Only the ⁠ t ⁠ column vectors of ⁠ $\mathbf {U}$ ⁠ and ⁠ t ⁠ row vectors of ⁠ $\mathbf {V} ^{*}$ ⁠ corresponding to the ⁠ t ⁠ largest singular values ⁠ $\mathbf {\Sigma } _{t}$ ⁠ are calculated. This can be much quicker and more economical than the compact SVD if ⁠ $t\ll r,$ ⁠ but requires a completely different toolset of numerical solvers.

In applications that require an approximation to the Moore–Penrose inverse of the matrix ⁠ $\mathbf {M} ,$ ⁠ the smallest singular values of ⁠ $\mathbf {M}$ ⁠ are of interest, which are more challenging to compute compared to the largest ones.

Truncated SVD is employed in latent semantic indexing.


## Norms

### Ky Fan norms

The sum of the ⁠ k ⁠ largest singular values of ⁠ $\mathbf {M}$ ⁠ is a matrix norm, the Ky Fan ⁠ k ⁠-norm of ⁠ $\mathbf {M} .$ ⁠

The first of the Ky Fan norms, the Ky Fan 1-norm, is the same as the operator norm of ⁠ $\mathbf {M}$ ⁠ as a linear operator with respect to the Euclidean norms of ⁠ $K^{m}$ ⁠ and ⁠ $K^{n}.$ ⁠ In other words, the Ky Fan 1-norm is the operator norm induced by the standard $\ell ^{2}$ Euclidean inner product. For this reason, it is also called the operator 2-norm. One can easily verify the relationship between the Ky Fan 1-norm and singular values. It is true in general, for a bounded operator ⁠ $\mathbf {M}$ ⁠ on (possibly infinite-dimensional) Hilbert spaces

$\|\mathbf {M} \|=\|\mathbf {M} ^{*}\mathbf {M} \|^{\frac {1}{2}}$

But, in the matrix case, ⁠ $(\mathbf {M} ^{*}\mathbf {M} )^{1/2}$ ⁠ is a normal matrix, so $\|\mathbf {M} ^{*}\mathbf {M} \|^{1/2}$ is the largest eigenvalue of ⁠ $(\mathbf {M} ^{*}\mathbf {M} )^{1/2},$ ⁠ i.e. the largest singular value of ⁠ $\mathbf {M} .$ ⁠

The last of the Ky Fan norms, the sum of all singular values, is the trace norm (also known as the 'nuclear norm'), defined by $\|\mathbf {M} \|=\operatorname {Tr} (\mathbf {M} ^{*}\mathbf {M} )^{1/2}$ (the eigenvalues of ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠ are the squares of the singular values).

### Hilbert–Schmidt norm

The singular values are related to another norm on the space of operators. Consider the Hilbert–Schmidt inner product on the ⁠ $n\times n$ ⁠ matrices, defined by

$\langle \mathbf {M} ,\mathbf {N} \rangle =\operatorname {tr} \left(\mathbf {N} ^{*}\mathbf {M} \right).$

So the induced norm is

$\|\mathbf {M} \|={\sqrt {\langle \mathbf {M} ,\mathbf {M} \rangle }}={\sqrt {\operatorname {tr} \left(\mathbf {M} ^{*}\mathbf {M} \right)}}.$

Since the trace is invariant under unitary equivalence, this shows

$\|\mathbf {M} \|={\sqrt {{\vphantom {\bigg |}}\sum _{i}\sigma _{i}^{2}}}$

where ⁠ $\sigma _{i}$ ⁠ are the singular values of ⁠ $\mathbf {M} .$ ⁠ This is called the **Frobenius norm**, **Schatten 2-norm**, or **Hilbert–Schmidt norm** of ⁠ $\mathbf {M} .$ ⁠ Direct calculation shows that the Frobenius norm of ⁠ $\mathbf {M} =(m_{ij})$ ⁠ coincides with:

${\sqrt {{\vphantom {\bigg |}}\sum _{ij}|m_{ij}|^{2}}}.$

In addition, the Frobenius norm and the trace norm (the nuclear norm) are special cases of the Schatten norm.


## Variations and generalizations

### Scale-invariant SVD

The singular values of a matrix ⁠ $\mathbf {A}$ ⁠ are uniquely defined and are invariant with respect to left and/or right unitary transformations of ⁠ $\mathbf {A} .$ ⁠ In other words, the singular values of ⁠ $\mathbf {U} \mathbf {A} \mathbf {V} ,$ ⁠ for unitary matrices ⁠ $\mathbf {U}$ ⁠ and ⁠ $\mathbf {V} ,$ ⁠ are equal to the singular values of ⁠ $\mathbf {A} .$ ⁠ This is an important property for applications in which it is necessary to preserve Euclidean distances and invariance with respect to rotations.

The Scale-Invariant SVD, or SI-SVD, is analogous to the conventional SVD except that its uniquely-determined singular values are invariant with respect to diagonal transformations of ⁠ $\mathbf {A} .$ ⁠ In other words, the singular values of ⁠ $\mathbf {D} \mathbf {A} \mathbf {E} ,$ ⁠ for invertible diagonal matrices ⁠ $\mathbf {D}$ ⁠ and ⁠ $\mathbf {E} ,$ ⁠ are equal to the singular values of ⁠ $\mathbf {A} .$ ⁠ This is an important property for applications for which invariance to the choice of units on variables (e.g., metric versus imperial units) is needed.

### Bounded operators on Hilbert spaces

The factorization ⁠ $\mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}$ ⁠ can be extended to a bounded operator ⁠ $\mathbf {M}$ ⁠ on a separable Hilbert space ⁠ $H.$ ⁠ Namely, for any bounded operator ⁠ $\mathbf {M} ,$ ⁠ there exist a partial isometry ⁠ $\mathbf {U} ,$ ⁠ a unitary ⁠ $\mathbf {V} ,$ ⁠ a measure space ⁠ $(X,\mu ),$ ⁠ and a non-negative measurable ⁠ f ⁠ such that

$\mathbf {M} =\mathbf {U} T_{f}\mathbf {V} ^{*}$

where ⁠ $T_{f}$ ⁠ is the multiplication by ⁠ f ⁠ on ⁠ $L^{2}(X,\mu ).$ ⁠

This can be shown by mimicking the linear algebraic argument for the matrix case above. ⁠ $\mathbf {V} T_{f}\mathbf {V} ^{*}$ ⁠ is the unique positive square root of ⁠ $\mathbf {M} ^{*}\mathbf {M} ,$ ⁠ as given by the Borel functional calculus for self-adjoint operators. The reason why ⁠ $\mathbf {U}$ ⁠ need not be unitary is that, unlike the finite-dimensional case, given an isometry ⁠ $U_{1}$ ⁠ with nontrivial kernel, a suitable ⁠ $U_{2}$ ⁠ may not be found such that

${\begin{bmatrix}U_{1}\\U_{2}\end{bmatrix}}$

is a unitary operator.

As for matrices, the singular value factorization is equivalent to the polar decomposition for operators: we can simply write

$\mathbf {M} =\mathbf {U} \mathbf {V} ^{*}\cdot \mathbf {V} T_{f}\mathbf {V} ^{*}$

and notice that ⁠ $\mathbf {U} \mathbf {V} ^{*}$ ⁠ is still a partial isometry while ⁠ $\mathbf {V} T_{f}\mathbf {V} ^{*}$ ⁠ is positive.

### Singular values and compact operators

The notion of singular values and left/right-singular vectors can be extended to compact operator on Hilbert space as they have a discrete spectrum. If ⁠ T ⁠ is compact, every non-zero ⁠ $\lambda$ ⁠ in its spectrum is an eigenvalue. Furthermore, a compact self-adjoint operator can be diagonalized by its eigenvectors. If ⁠ $\mathbf {M}$ ⁠ is compact, so is ⁠ $\mathbf {M} ^{*}\mathbf {M}$ ⁠. Applying the diagonalization result, the unitary image of its positive square root ⁠ $T_{f}$ ⁠ has a set of orthonormal eigenvectors ⁠ $\{e_{i}\}$ ⁠ corresponding to strictly positive eigenvalues ⁠ $\{\sigma _{i}\}$ ⁠. For any ⁠ $\psi$ ⁠ in ⁠ $H,$ ⁠

$\mathbf {M} \psi =\mathbf {U} T_{f}\mathbf {V} ^{*}\psi =\sum _{i}\left\langle \mathbf {U} T_{f}\mathbf {V} ^{*}\psi ,\mathbf {U} e_{i}\right\rangle \mathbf {U} e_{i}=\sum _{i}\sigma _{i}\left\langle \psi ,\mathbf {V} e_{i}\right\rangle \mathbf {U} e_{i},$

where the series converges in the norm topology on ⁠ $H.$ ⁠ Notice how this resembles the expression from the finite-dimensional case. ⁠ $\sigma _{i}$ ⁠ are called the singular values of ⁠ $\mathbf {M} .$ ⁠ ⁠ $\{\mathbf {U} e_{i}\}$ ⁠ (resp. ⁠ $\{\mathbf {V} e_{i}\}$ ⁠) can be considered the left-singular (resp. right-singular) vectors of ⁠ $\mathbf {M} .$ ⁠

Compact operators on a Hilbert space are the closure of finite-rank operators in the uniform operator topology. The above series expression gives an explicit such representation. An immediate consequence of this is:

Theorem.

⁠

$\mathbf {M}$

⁠

is compact if and only if

⁠

$\mathbf {M} ^{*}\mathbf {M}$

⁠

is compact.


## History

The singular value decomposition was originally developed by differential geometers, who wished to determine whether a real bilinear form could be made equal to another by independent orthogonal transformations of the two spaces it acts on. Eugenio Beltrami and Camille Jordan discovered independently, in 1873 and 1874 respectively, that the singular values of the bilinear forms, represented as a matrix, form a complete set of invariants for bilinear forms under orthogonal substitutions. James Joseph Sylvester also arrived at the singular value decomposition for real square matrices in 1889, apparently independently of both Beltrami and Jordan. Sylvester called the singular values the *canonical multipliers* of the matrix ⁠ $\mathbf {A} .$ ⁠ The fourth mathematician to discover the singular value decomposition independently is Autonne in 1915, who arrived at it via the polar decomposition. The first proof of the singular value decomposition for rectangular and complex matrices seems to be by Carl Eckart and Gale J. Young in 1936; they saw it as a generalization of the principal axis transformation for Hermitian matrices.

In 1907, Erhard Schmidt defined an analog of singular values for integral operators (which are compact, under some weak technical assumptions); it seems he was unaware of the parallel work on singular values of finite matrices. This theory was further developed by Émile Picard in 1910, who is the first to call the numbers $\sigma _{k}$ *singular values* (or in French, *valeurs singulières*).

Practical methods for computing the SVD date back to Kogbetliantz in 1954–1955 and Hestenes in 1958, resembling closely the Jacobi eigenvalue algorithm, which uses plane rotations or Givens rotations. However, these were replaced by the method of Gene Golub and William Kahan published in 1965, which uses Householder transformations or reflections. In 1970, Golub and Christian Reinsch published a variant of the Golub/Kahan algorithm that is still the one most-used today.

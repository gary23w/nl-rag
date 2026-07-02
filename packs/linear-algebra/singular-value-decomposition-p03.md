---
title: "Singular value decomposition (part 3/3)"
source: https://en.wikipedia.org/wiki/Singular_value_decomposition
domain: linear-algebra
license: CC-BY-SA-4.0
tags: linear algebra, matrix algebra, matrices, eigenvalue, vector space, dot product
fetched: 2026-07-02
part: 3/3
---

## Calculating the SVD

### One-sided Jacobi algorithm

One-sided Jacobi algorithm is an iterative algorithm, where a matrix is iteratively transformed into a matrix with orthogonal columns. The elementary iteration is given as a Jacobi rotation, M ← M J ( p , q , θ ) , {\displaystyle M\leftarrow MJ(p,q,\theta ),} ({\displaystyle M\leftarrow MJ(p,q,\theta ),}) where the angle θ {\displaystyle \theta } ({\displaystyle \theta }) of the Jacobi rotation matrix J ( p , q , θ ) {\displaystyle J(p,q,\theta )} ({\displaystyle J(p,q,\theta )}) is chosen such that after the rotation the columns with numbers p {\displaystyle p} ({\displaystyle p}) and q {\displaystyle q} ({\displaystyle q}) become orthogonal. The indices ( p , q ) {\displaystyle (p,q)} ({\displaystyle (p,q)}) are swept cyclically, ( p = 1 … m , q = p + 1 … m ) {\displaystyle (p=1\dots m,q=p+1\dots m)} ({\displaystyle (p=1\dots m,q=p+1\dots m)}), where m {\displaystyle m} ({\displaystyle m}) is the number of columns.

After the algorithm has converged, the singular value decomposition M = U S V T {\displaystyle M=USV^{T}} ({\displaystyle M=USV^{T}}) is recovered as follows: the matrix V {\displaystyle V} ({\displaystyle V}) is the accumulation of Jacobi rotation matrices, the matrix U {\displaystyle U} ({\displaystyle U}) is given by normalising the columns of the transformed matrix M {\displaystyle M} ({\displaystyle M}), and the singular values are given as the norms of the columns of the transformed matrix M {\displaystyle M} ({\displaystyle M}).

### Two-sided Jacobi algorithm

Two-sided Jacobi SVD algorithm—a generalization of the Jacobi eigenvalue algorithm—is an iterative algorithm where a square matrix is iteratively transformed into a diagonal matrix. If the matrix is not square the QR decomposition is performed first and then the algorithm is applied to the R {\displaystyle R} ({\displaystyle R}) matrix. The elementary iteration zeroes a pair of off-diagonal elements by first applying a Givens rotation to symmetrize the pair of elements and then applying a Jacobi transformation to zero them, M ← J T G M J {\displaystyle M\leftarrow J^{T}GMJ} ({\displaystyle M\leftarrow J^{T}GMJ}) where G {\displaystyle G} ({\displaystyle G}) is the Givens rotation matrix with the angle chosen such that the given pair of off-diagonal elements become equal after the rotation, and where J {\displaystyle J} ({\displaystyle J}) is the Jacobi transformation matrix that zeroes these off-diagonal elements. The iterations proceeds exactly as in the Jacobi eigenvalue algorithm: by cyclic sweeps over all off-diagonal elements.

After the algorithm has converged the resulting diagonal matrix contains the singular values. The matrices U {\displaystyle U} ({\displaystyle U}) and V {\displaystyle V} ({\displaystyle V}) are accumulated as follows: U ← U G T J , V ← V J . {\displaystyle {\begin{aligned}U&\leftarrow UG^{T}J,\\V&\leftarrow VJ.\end{aligned}}} ({\displaystyle {\begin{aligned}U&\leftarrow UG^{T}J,\\V&\leftarrow VJ.\end{aligned}}})

### Numerical approach

The singular value decomposition can be computed using the following observations:

- The left-singular vectors of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ are a set of orthonormal eigenvectors of ⁠ M M ∗ {\displaystyle \mathbf {M} \mathbf {M} ^{*}} ({\displaystyle \mathbf {M} \mathbf {M} ^{*}})⁠.
- The right-singular vectors of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ are a set of orthonormal eigenvectors of ⁠ M ∗ M {\displaystyle \mathbf {M} ^{*}\mathbf {M} } ({\displaystyle \mathbf {M} ^{*}\mathbf {M} })⁠.
- The non-zero singular values of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ (found on the diagonal entries of Σ {\displaystyle \mathbf {\Sigma } } ({\displaystyle \mathbf {\Sigma } })) are the square roots of the non-zero eigenvalues of both ⁠ M ∗ M {\displaystyle \mathbf {M} ^{*}\mathbf {M} } ({\displaystyle \mathbf {M} ^{*}\mathbf {M} })⁠ and ⁠ M M ∗ {\displaystyle \mathbf {M} \mathbf {M} ^{*}} ({\displaystyle \mathbf {M} \mathbf {M} ^{*}})⁠.

The SVD of a matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is typically computed by a two-step procedure. In the first step, the matrix is reduced to a bidiagonal matrix. This takes order ⁠ O ( m n 2 ) {\displaystyle O(mn^{2})} ({\displaystyle O(mn^{2})})⁠ floating-point operations (*flop*), assuming that ⁠ m ≥ n . {\displaystyle m\geq n.} ({\displaystyle m\geq n.})⁠ The second step is to compute the SVD of the bidiagonal matrix. This step can only be done with an iterative method (as with eigenvalue algorithms). However, in practice it suffices to compute the SVD up to a certain precision, like the machine epsilon. If this precision is considered constant, then the second step takes ⁠ O ( n ) {\displaystyle O(n)} ({\displaystyle O(n)})⁠ iterations, each costing ⁠ O ( n ) {\displaystyle O(n)} ({\displaystyle O(n)})⁠ flops. Thus, the first step is more expensive, and the overall cost is ⁠ O ( m n 2 ) {\displaystyle O(mn^{2})} ({\displaystyle O(mn^{2})})⁠ flops.

The first step can be done using Householder reflections for a cost of ⁠ 4 m n 2 − 4 n 3 / 3 {\displaystyle 4mn^{2}-4n^{3}/3} ({\displaystyle 4mn^{2}-4n^{3}/3})⁠ flops, assuming that only the singular values are needed and not the singular vectors. If ⁠ m {\displaystyle m} ({\displaystyle m})⁠ is much larger than ⁠ n {\displaystyle n} ({\displaystyle n})⁠ then it is advantageous to first reduce the matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ to a triangular matrix with the QR decomposition and then use Householder reflections to further reduce the matrix to bidiagonal form; the combined cost is ⁠ 2 m n 2 + 2 n 3 {\displaystyle 2mn^{2}+2n^{3}} ({\displaystyle 2mn^{2}+2n^{3}})⁠ flops.

The second step can be done by a variant of the QR algorithm for the computation of eigenvalues, which was first described by Golub and Kahan in 1965. The LAPACK subroutine `DBDSQR` implements this iterative method, with some modifications to cover the case where the singular values are very small. Together with a first step using Householder reflections and, if appropriate, QR decomposition, this forms the `DGESVD` routine for the computation of the singular value decomposition.

The same algorithm is implemented in the GNU Scientific Library (GSL). The GSL also offers an alternative method that uses a one-sided Jacobi orthogonalization in step 2. This method computes the SVD of the bidiagonal matrix by solving a sequence of ⁠ 2 × 2 {\displaystyle 2\times 2} ({\displaystyle 2\times 2})⁠ SVD problems, similar to how the Jacobi eigenvalue algorithm solves a sequence of ⁠ 2 × 2 {\displaystyle 2\times 2} ({\displaystyle 2\times 2})⁠ eigenvalue methods. Yet another method for step 2 uses the idea of divide-and-conquer eigenvalue algorithms.

There is an alternative way that does not explicitly use the eigenvalue decomposition. Usually the singular value problem of a matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is converted into an equivalent symmetric eigenvalue problem such as ⁠ M M ∗ , {\displaystyle \mathbf {M} \mathbf {M} ^{*},} ({\displaystyle \mathbf {M} \mathbf {M} ^{*},})⁠ ⁠ M ∗ M , {\displaystyle \mathbf {M} ^{*}\mathbf {M} ,} ({\displaystyle \mathbf {M} ^{*}\mathbf {M} ,})⁠ or

[ 0 M M ∗ 0 ] . {\displaystyle {\begin{bmatrix}\mathbf {0} &\mathbf {M} \\\mathbf {M} ^{*}&\mathbf {0} \end{bmatrix}}.} ({\displaystyle {\begin{bmatrix}\mathbf {0} &\mathbf {M} \\\mathbf {M} ^{*}&\mathbf {0} \end{bmatrix}}.})

The approaches that use eigenvalue decompositions are based on the QR algorithm, which is well-developed to be stable and fast. Note that the singular values are real and right- and left- singular vectors are not required to form similarity transformations. One can iteratively alternate between the QR decomposition and the LQ decomposition to find the real diagonal Hermitian matrices. The QR decomposition gives ⁠ M ⇒ Q R {\displaystyle \mathbf {M} \Rightarrow \mathbf {Q} \mathbf {R} } ({\displaystyle \mathbf {M} \Rightarrow \mathbf {Q} \mathbf {R} })⁠ and the LQ decomposition of ⁠ R {\displaystyle \mathbf {R} } ({\displaystyle \mathbf {R} })⁠ gives ⁠ R ⇒ L P ∗ . {\displaystyle \mathbf {R} \Rightarrow \mathbf {L} \mathbf {P} ^{*}.} ({\displaystyle \mathbf {R} \Rightarrow \mathbf {L} \mathbf {P} ^{*}.})⁠ Thus, at every iteration, we have ⁠ M ⇒ Q L P ∗ , {\displaystyle \mathbf {M} \Rightarrow \mathbf {Q} \mathbf {L} \mathbf {P} ^{*},} ({\displaystyle \mathbf {M} \Rightarrow \mathbf {Q} \mathbf {L} \mathbf {P} ^{*},})⁠ update ⁠ M ⇐ L {\displaystyle \mathbf {M} \Leftarrow \mathbf {L} } ({\displaystyle \mathbf {M} \Leftarrow \mathbf {L} })⁠ and repeat the orthogonalizations. Eventually, this iteration between QR decomposition and LQ decomposition produces left- and right- unitary singular matrices. This approach cannot readily be accelerated, as the QR algorithm can with spectral shifts or deflation. This is because the shift method is not easily defined without using similarity transformations. However, this iterative approach is very simple to implement, so is a good choice when speed does not matter. This method also provides insight into how purely orthogonal/unitary transformations can obtain the SVD.

### Computational complexity of SVD

The methods above yield ⁠ O ( m n 2 ) {\displaystyle O(mn^{2})} ({\displaystyle O(mn^{2})})⁠ algorithms for the SVD of an m × n {\displaystyle m\times n} ({\displaystyle m\times n}) matrix M {\displaystyle M} ({\displaystyle M}) where m ≥ n {\displaystyle m\geq n} ({\displaystyle m\geq n}).

Demmel, Dumitriu and Holtz show that for a symmetric M {\displaystyle M} ({\displaystyle M}) (i.e. m = n {\displaystyle m=n} ({\displaystyle m=n})) the SVD can normwise stably be computed in O ( n ω + η ) {\displaystyle O(n^{\omega +\eta })} ({\displaystyle O(n^{\omega +\eta })}) arithmetic operations where ω {\displaystyle \omega } ({\displaystyle \omega }) is the matrix multiplication exponent and η > 0 {\displaystyle \eta >0} ({\displaystyle \eta >0}) is any constant, i.e. essentially in matrix multiplication time.

### Analytic result of 2 × 2 SVD

The singular values of a ⁠ 2 × 2 {\displaystyle 2\times 2} ({\displaystyle 2\times 2})⁠ matrix can be found analytically. Let the matrix be M = z 0 I + z 1 σ 1 + z 2 σ 2 + z 3 σ 3 {\displaystyle \mathbf {M} =z_{0}\mathbf {I} +z_{1}\sigma _{1}+z_{2}\sigma _{2}+z_{3}\sigma _{3}} ({\displaystyle \mathbf {M} =z_{0}\mathbf {I} +z_{1}\sigma _{1}+z_{2}\sigma _{2}+z_{3}\sigma _{3}})

where z i ∈ C {\displaystyle z_{i}\in \mathbb {C} } ({\displaystyle z_{i}\in \mathbb {C} }) are complex numbers that parameterize the matrix, ⁠ I {\displaystyle \mathbf {I} } ({\displaystyle \mathbf {I} })⁠ is the identity matrix, and σ i {\displaystyle \sigma _{i}} ({\displaystyle \sigma _{i}}) denote the Pauli matrices. Then its two singular values are given by

σ ± = | z 0 | 2 + | z 1 | 2 + | z 2 | 2 + | z 3 | 2 ± ( | z 0 | 2 + | z 1 | 2 + | z 2 | 2 + | z 3 | 2 ) 2 − | z 0 2 − z 1 2 − z 2 2 − z 3 2 | 2 = | z 0 | 2 + | z 1 | 2 + | z 2 | 2 + | z 3 | 2 ± 2 ( Re ⁡ z 0 z 1 ∗ ) 2 + ( Re ⁡ z 0 z 2 ∗ ) 2 + ( Re ⁡ z 0 z 3 ∗ ) 2 + ( Im ⁡ z 1 z 2 ∗ ) 2 + ( Im ⁡ z 2 z 3 ∗ ) 2 + ( Im ⁡ z 3 z 1 ∗ ) 2 {\displaystyle {\begin{aligned}\sigma _{\pm }&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm {\sqrt {{\bigl (}|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}{\bigr )}^{2}-|z_{0}^{2}-z_{1}^{2}-z_{2}^{2}-z_{3}^{2}|^{2}}}}}\\&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm 2{\sqrt {(\operatorname {Re} z_{0}z_{1}^{*})^{2}+(\operatorname {Re} z_{0}z_{2}^{*})^{2}+(\operatorname {Re} z_{0}z_{3}^{*})^{2}+(\operatorname {Im} z_{1}z_{2}^{*})^{2}+(\operatorname {Im} z_{2}z_{3}^{*})^{2}+(\operatorname {Im} z_{3}z_{1}^{*})^{2}}}}}\end{aligned}}} ({\displaystyle {\begin{aligned}\sigma _{\pm }&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm {\sqrt {{\bigl (}|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}{\bigr )}^{2}-|z_{0}^{2}-z_{1}^{2}-z_{2}^{2}-z_{3}^{2}|^{2}}}}}\\&={\sqrt {|z_{0}|^{2}+|z_{1}|^{2}+|z_{2}|^{2}+|z_{3}|^{2}\pm 2{\sqrt {(\operatorname {Re} z_{0}z_{1}^{*})^{2}+(\operatorname {Re} z_{0}z_{2}^{*})^{2}+(\operatorname {Re} z_{0}z_{3}^{*})^{2}+(\operatorname {Im} z_{1}z_{2}^{*})^{2}+(\operatorname {Im} z_{2}z_{3}^{*})^{2}+(\operatorname {Im} z_{3}z_{1}^{*})^{2}}}}}\end{aligned}}})


## Reduced SVDs

In applications it is quite unusual for the full SVD, including a full unitary decomposition of the null-space of the matrix, to be required. Instead, it is often sufficient (as well as faster, and more economical for storage) to compute a reduced version of the SVD. The following can be distinguished for an ⁠ m × n {\displaystyle m\times n} ({\displaystyle m\times n})⁠ matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ of rank ⁠ r {\displaystyle r} ({\displaystyle r})⁠:

### Thin SVD

The thin, or economy-sized, SVD of a matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is given by

M = U k Σ k V k ∗ , {\displaystyle \mathbf {M} =\mathbf {U} _{k}\mathbf {\Sigma } _{k}\mathbf {V} _{k}^{*},} ({\displaystyle \mathbf {M} =\mathbf {U} _{k}\mathbf {\Sigma } _{k}\mathbf {V} _{k}^{*},})

where k = min ( m , n ) , {\displaystyle k=\min(m,n),} ({\displaystyle k=\min(m,n),}) the matrices ⁠ U k {\displaystyle \mathbf {U} _{k}} ({\displaystyle \mathbf {U} _{k}})⁠ and ⁠ V k {\displaystyle \mathbf {V} _{k}} ({\displaystyle \mathbf {V} _{k}})⁠ contain only the first ⁠ k {\displaystyle k} ({\displaystyle k})⁠ columns of ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ and ⁠ V , {\displaystyle \mathbf {V} ,} ({\displaystyle \mathbf {V} ,})⁠ and ⁠ Σ k {\displaystyle \mathbf {\Sigma } _{k}} ({\displaystyle \mathbf {\Sigma } _{k}})⁠ contains only the first ⁠ k {\displaystyle k} ({\displaystyle k})⁠ singular values from ⁠ Σ . {\displaystyle \mathbf {\Sigma } .} ({\displaystyle \mathbf {\Sigma } .})⁠ The matrix ⁠ U k {\displaystyle \mathbf {U} _{k}} ({\displaystyle \mathbf {U} _{k}})⁠ is thus ⁠ m × k , {\displaystyle m\times k,} ({\displaystyle m\times k,})⁠ ⁠ Σ k {\displaystyle \mathbf {\Sigma } _{k}} ({\displaystyle \mathbf {\Sigma } _{k}})⁠ is ⁠ k × k {\displaystyle k\times k} ({\displaystyle k\times k})⁠ diagonal, and ⁠ V k ∗ {\displaystyle \mathbf {V} _{k}^{*}} ({\displaystyle \mathbf {V} _{k}^{*}})⁠ is ⁠ k × n . {\displaystyle k\times n.} ({\displaystyle k\times n.})⁠

The thin SVD uses significantly less space and computation time if ⁠ k ≪ max ( m , n ) . {\displaystyle k\ll \max(m,n).} ({\displaystyle k\ll \max(m,n).})⁠ The first stage in its calculation will usually be a QR decomposition of ⁠ M , {\displaystyle \mathbf {M} ,} ({\displaystyle \mathbf {M} ,})⁠ which can make for a significantly quicker calculation in this case.

### Compact SVD

The compact SVD of a matrix ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is given by

M = U r Σ r V r ∗ . {\displaystyle \mathbf {M} =\mathbf {U} _{r}\mathbf {\Sigma } _{r}\mathbf {V} _{r}^{*}.} ({\displaystyle \mathbf {M} =\mathbf {U} _{r}\mathbf {\Sigma } _{r}\mathbf {V} _{r}^{*}.})

Only the ⁠ r {\displaystyle r} ({\displaystyle r})⁠ column vectors of ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ and ⁠ r {\displaystyle r} ({\displaystyle r})⁠ row vectors of ⁠ V ∗ {\displaystyle \mathbf {V} ^{*}} ({\displaystyle \mathbf {V} ^{*}})⁠ corresponding to the non-zero singular values ⁠ Σ r {\displaystyle \mathbf {\Sigma } _{r}} ({\displaystyle \mathbf {\Sigma } _{r}})⁠ are calculated. The remaining vectors of ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ and ⁠ V ∗ {\displaystyle \mathbf {V} ^{*}} ({\displaystyle \mathbf {V} ^{*}})⁠ are not calculated. This is quicker and more economical than the thin SVD if ⁠ r ≪ min ( m , n ) . {\displaystyle r\ll \min(m,n).} ({\displaystyle r\ll \min(m,n).})⁠ The matrix ⁠ U r {\displaystyle \mathbf {U} _{r}} ({\displaystyle \mathbf {U} _{r}})⁠ is thus ⁠ m × r , {\displaystyle m\times r,} ({\displaystyle m\times r,})⁠ ⁠ Σ r {\displaystyle \mathbf {\Sigma } _{r}} ({\displaystyle \mathbf {\Sigma } _{r}})⁠ is ⁠ r × r {\displaystyle r\times r} ({\displaystyle r\times r})⁠ diagonal, and ⁠ V r ∗ {\displaystyle \mathbf {V} _{r}^{*}} ({\displaystyle \mathbf {V} _{r}^{*}})⁠ is ⁠ r × n . {\displaystyle r\times n.} ({\displaystyle r\times n.})⁠

### Truncated SVD

In many applications the number ⁠ r {\displaystyle r} ({\displaystyle r})⁠ of the non-zero singular values is large making even the Compact SVD impractical to compute. In such cases, the smallest singular values may need to be truncated to compute only ⁠ t ≪ r {\displaystyle t\ll r} ({\displaystyle t\ll r})⁠ non-zero singular values. The truncated SVD is no longer an exact decomposition of the original matrix ⁠ M , {\displaystyle \mathbf {M} ,} ({\displaystyle \mathbf {M} ,})⁠ but rather provides the optimal low-rank matrix approximation ⁠ M ~ {\displaystyle {\tilde {\mathbf {M} }}} ({\displaystyle {\tilde {\mathbf {M} }}})⁠ by any matrix of a fixed rank ⁠ t {\displaystyle t} ({\displaystyle t})⁠

M ~ = U t Σ t V t ∗ , {\displaystyle {\tilde {\mathbf {M} }}=\mathbf {U} _{t}\mathbf {\Sigma } _{t}\mathbf {V} _{t}^{*},} ({\displaystyle {\tilde {\mathbf {M} }}=\mathbf {U} _{t}\mathbf {\Sigma } _{t}\mathbf {V} _{t}^{*},})

where matrix ⁠ U t {\displaystyle \mathbf {U} _{t}} ({\displaystyle \mathbf {U} _{t}})⁠ is ⁠ m × t , {\displaystyle m\times t,} ({\displaystyle m\times t,})⁠ ⁠ Σ t {\displaystyle \mathbf {\Sigma } _{t}} ({\displaystyle \mathbf {\Sigma } _{t}})⁠ is ⁠ t × t {\displaystyle t\times t} ({\displaystyle t\times t})⁠ diagonal, and ⁠ V t ∗ {\displaystyle \mathbf {V} _{t}^{*}} ({\displaystyle \mathbf {V} _{t}^{*}})⁠ is ⁠ t × n . {\displaystyle t\times n.} ({\displaystyle t\times n.})⁠ Only the ⁠ t {\displaystyle t} ({\displaystyle t})⁠ column vectors of ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ and ⁠ t {\displaystyle t} ({\displaystyle t})⁠ row vectors of ⁠ V ∗ {\displaystyle \mathbf {V} ^{*}} ({\displaystyle \mathbf {V} ^{*}})⁠ corresponding to the ⁠ t {\displaystyle t} ({\displaystyle t})⁠ largest singular values ⁠ Σ t {\displaystyle \mathbf {\Sigma } _{t}} ({\displaystyle \mathbf {\Sigma } _{t}})⁠ are calculated. This can be much quicker and more economical than the compact SVD if ⁠ t ≪ r , {\displaystyle t\ll r,} ({\displaystyle t\ll r,})⁠ but requires a completely different toolset of numerical solvers.

In applications that require an approximation to the Moore–Penrose inverse of the matrix ⁠ M , {\displaystyle \mathbf {M} ,} ({\displaystyle \mathbf {M} ,})⁠ the smallest singular values of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ are of interest, which are more challenging to compute compared to the largest ones.

Truncated SVD is employed in latent semantic indexing.


## Norms

### Ky Fan norms

The sum of the ⁠ k {\displaystyle k} ({\displaystyle k})⁠ largest singular values of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is a matrix norm, the Ky Fan ⁠ k {\displaystyle k} ({\displaystyle k})⁠-norm of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠

The first of the Ky Fan norms, the Ky Fan 1-norm, is the same as the operator norm of ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ as a linear operator with respect to the Euclidean norms of ⁠ K m {\displaystyle K^{m}} ({\displaystyle K^{m}})⁠ and ⁠ K n . {\displaystyle K^{n}.} ({\displaystyle K^{n}.})⁠ In other words, the Ky Fan 1-norm is the operator norm induced by the standard ℓ 2 {\displaystyle \ell ^{2}} ({\displaystyle \ell ^{2}}) Euclidean inner product. For this reason, it is also called the operator 2-norm. One can easily verify the relationship between the Ky Fan 1-norm and singular values. It is true in general, for a bounded operator ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ on (possibly infinite-dimensional) Hilbert spaces

‖ M ‖ = ‖ M ∗ M ‖ 1 2 {\displaystyle \|\mathbf {M} \|=\|\mathbf {M} ^{*}\mathbf {M} \|^{\frac {1}{2}}} ({\displaystyle \|\mathbf {M} \|=\|\mathbf {M} ^{*}\mathbf {M} \|^{\frac {1}{2}}})

But, in the matrix case, ⁠ ( M ∗ M ) 1 / 2 {\displaystyle (\mathbf {M} ^{*}\mathbf {M} )^{1/2}} ({\displaystyle (\mathbf {M} ^{*}\mathbf {M} )^{1/2}})⁠ is a normal matrix, so ‖ M ∗ M ‖ 1 / 2 {\displaystyle \|\mathbf {M} ^{*}\mathbf {M} \|^{1/2}} ({\displaystyle \|\mathbf {M} ^{*}\mathbf {M} \|^{1/2}}) is the largest eigenvalue of ⁠ ( M ∗ M ) 1 / 2 , {\displaystyle (\mathbf {M} ^{*}\mathbf {M} )^{1/2},} ({\displaystyle (\mathbf {M} ^{*}\mathbf {M} )^{1/2},})⁠ i.e. the largest singular value of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠

The last of the Ky Fan norms, the sum of all singular values, is the trace norm (also known as the 'nuclear norm'), defined by ‖ M ‖ = Tr ⁡ ( M ∗ M ) 1 / 2 {\displaystyle \|\mathbf {M} \|=\operatorname {Tr} (\mathbf {M} ^{*}\mathbf {M} )^{1/2}} ({\displaystyle \|\mathbf {M} \|=\operatorname {Tr} (\mathbf {M} ^{*}\mathbf {M} )^{1/2}}) (the eigenvalues of ⁠ M ∗ M {\displaystyle \mathbf {M} ^{*}\mathbf {M} } ({\displaystyle \mathbf {M} ^{*}\mathbf {M} })⁠ are the squares of the singular values).

### Hilbert–Schmidt norm

The singular values are related to another norm on the space of operators. Consider the Hilbert–Schmidt inner product on the ⁠ n × n {\displaystyle n\times n} ({\displaystyle n\times n})⁠ matrices, defined by

⟨ M , N ⟩ = tr ⁡ ( N ∗ M ) . {\displaystyle \langle \mathbf {M} ,\mathbf {N} \rangle =\operatorname {tr} \left(\mathbf {N} ^{*}\mathbf {M} \right).} ({\displaystyle \langle \mathbf {M} ,\mathbf {N} \rangle =\operatorname {tr} \left(\mathbf {N} ^{*}\mathbf {M} \right).})

So the induced norm is

‖ M ‖ = ⟨ M , M ⟩ = tr ⁡ ( M ∗ M ) . {\displaystyle \|\mathbf {M} \|={\sqrt {\langle \mathbf {M} ,\mathbf {M} \rangle }}={\sqrt {\operatorname {tr} \left(\mathbf {M} ^{*}\mathbf {M} \right)}}.} ({\displaystyle \|\mathbf {M} \|={\sqrt {\langle \mathbf {M} ,\mathbf {M} \rangle }}={\sqrt {\operatorname {tr} \left(\mathbf {M} ^{*}\mathbf {M} \right)}}.})

Since the trace is invariant under unitary equivalence, this shows

‖ M ‖ = | ∑ i σ i 2 {\displaystyle \|\mathbf {M} \|={\sqrt {{\vphantom {\bigg |}}\sum _{i}\sigma _{i}^{2}}}} ({\displaystyle \|\mathbf {M} \|={\sqrt {{\vphantom {\bigg |}}\sum _{i}\sigma _{i}^{2}}}})

where ⁠ σ i {\displaystyle \sigma _{i}} ({\displaystyle \sigma _{i}})⁠ are the singular values of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠ This is called the **Frobenius norm**, **Schatten 2-norm**, or **Hilbert–Schmidt norm** of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠ Direct calculation shows that the Frobenius norm of ⁠ M = ( m i j ) {\displaystyle \mathbf {M} =(m_{ij})} ({\displaystyle \mathbf {M} =(m_{ij})})⁠ coincides with:

| ∑ i j | m i j | 2 . {\displaystyle {\sqrt {{\vphantom {\bigg |}}\sum _{ij}|m_{ij}|^{2}}}.} ({\displaystyle {\sqrt {{\vphantom {\bigg |}}\sum _{ij}|m_{ij}|^{2}}}.})

In addition, the Frobenius norm and the trace norm (the nuclear norm) are special cases of the Schatten norm.


## Variations and generalizations

### Scale-invariant SVD

The singular values of a matrix ⁠ A {\displaystyle \mathbf {A} } ({\displaystyle \mathbf {A} })⁠ are uniquely defined and are invariant with respect to left and/or right unitary transformations of ⁠ A . {\displaystyle \mathbf {A} .} ({\displaystyle \mathbf {A} .})⁠ In other words, the singular values of ⁠ U A V , {\displaystyle \mathbf {U} \mathbf {A} \mathbf {V} ,} ({\displaystyle \mathbf {U} \mathbf {A} \mathbf {V} ,})⁠ for unitary matrices ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ and ⁠ V , {\displaystyle \mathbf {V} ,} ({\displaystyle \mathbf {V} ,})⁠ are equal to the singular values of ⁠ A . {\displaystyle \mathbf {A} .} ({\displaystyle \mathbf {A} .})⁠ This is an important property for applications in which it is necessary to preserve Euclidean distances and invariance with respect to rotations.

The Scale-Invariant SVD, or SI-SVD, is analogous to the conventional SVD except that its uniquely-determined singular values are invariant with respect to diagonal transformations of ⁠ A . {\displaystyle \mathbf {A} .} ({\displaystyle \mathbf {A} .})⁠ In other words, the singular values of ⁠ D A E , {\displaystyle \mathbf {D} \mathbf {A} \mathbf {E} ,} ({\displaystyle \mathbf {D} \mathbf {A} \mathbf {E} ,})⁠ for invertible diagonal matrices ⁠ D {\displaystyle \mathbf {D} } ({\displaystyle \mathbf {D} })⁠ and ⁠ E , {\displaystyle \mathbf {E} ,} ({\displaystyle \mathbf {E} ,})⁠ are equal to the singular values of ⁠ A . {\displaystyle \mathbf {A} .} ({\displaystyle \mathbf {A} .})⁠ This is an important property for applications for which invariance to the choice of units on variables (e.g., metric versus imperial units) is needed.

### Bounded operators on Hilbert spaces

The factorization ⁠ M = U Σ V ∗ {\displaystyle \mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}} ({\displaystyle \mathbf {M} =\mathbf {U} \mathbf {\Sigma } \mathbf {V} ^{*}})⁠ can be extended to a bounded operator ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ on a separable Hilbert space ⁠ H . {\displaystyle H.} ({\displaystyle H.})⁠ Namely, for any bounded operator ⁠ M , {\displaystyle \mathbf {M} ,} ({\displaystyle \mathbf {M} ,})⁠ there exist a partial isometry ⁠ U , {\displaystyle \mathbf {U} ,} ({\displaystyle \mathbf {U} ,})⁠ a unitary ⁠ V , {\displaystyle \mathbf {V} ,} ({\displaystyle \mathbf {V} ,})⁠ a measure space ⁠ ( X , μ ) , {\displaystyle (X,\mu ),} ({\displaystyle (X,\mu ),})⁠ and a non-negative measurable ⁠ f {\displaystyle f} ({\displaystyle f})⁠ such that

M = U T f V ∗ {\displaystyle \mathbf {M} =\mathbf {U} T_{f}\mathbf {V} ^{*}} ({\displaystyle \mathbf {M} =\mathbf {U} T_{f}\mathbf {V} ^{*}})

where ⁠ T f {\displaystyle T_{f}} ({\displaystyle T_{f}})⁠ is the multiplication by ⁠ f {\displaystyle f} ({\displaystyle f})⁠ on ⁠ L 2 ( X , μ ) . {\displaystyle L^{2}(X,\mu ).} ({\displaystyle L^{2}(X,\mu ).})⁠

This can be shown by mimicking the linear algebraic argument for the matrix case above. ⁠ V T f V ∗ {\displaystyle \mathbf {V} T_{f}\mathbf {V} ^{*}} ({\displaystyle \mathbf {V} T_{f}\mathbf {V} ^{*}})⁠ is the unique positive square root of ⁠ M ∗ M , {\displaystyle \mathbf {M} ^{*}\mathbf {M} ,} ({\displaystyle \mathbf {M} ^{*}\mathbf {M} ,})⁠ as given by the Borel functional calculus for self-adjoint operators. The reason why ⁠ U {\displaystyle \mathbf {U} } ({\displaystyle \mathbf {U} })⁠ need not be unitary is that, unlike the finite-dimensional case, given an isometry ⁠ U 1 {\displaystyle U_{1}} ({\displaystyle U_{1}})⁠ with nontrivial kernel, a suitable ⁠ U 2 {\displaystyle U_{2}} ({\displaystyle U_{2}})⁠ may not be found such that

[ U 1 U 2 ] {\displaystyle {\begin{bmatrix}U_{1}\\U_{2}\end{bmatrix}}} ({\displaystyle {\begin{bmatrix}U_{1}\\U_{2}\end{bmatrix}}})

is a unitary operator.

As for matrices, the singular value factorization is equivalent to the polar decomposition for operators: we can simply write

M = U V ∗ ⋅ V T f V ∗ {\displaystyle \mathbf {M} =\mathbf {U} \mathbf {V} ^{*}\cdot \mathbf {V} T_{f}\mathbf {V} ^{*}} ({\displaystyle \mathbf {M} =\mathbf {U} \mathbf {V} ^{*}\cdot \mathbf {V} T_{f}\mathbf {V} ^{*}})

and notice that ⁠ U V ∗ {\displaystyle \mathbf {U} \mathbf {V} ^{*}} ({\displaystyle \mathbf {U} \mathbf {V} ^{*}})⁠ is still a partial isometry while ⁠ V T f V ∗ {\displaystyle \mathbf {V} T_{f}\mathbf {V} ^{*}} ({\displaystyle \mathbf {V} T_{f}\mathbf {V} ^{*}})⁠ is positive.

### Singular values and compact operators

The notion of singular values and left/right-singular vectors can be extended to compact operator on Hilbert space as they have a discrete spectrum. If ⁠ T {\displaystyle T} ({\displaystyle T})⁠ is compact, every non-zero ⁠ λ {\displaystyle \lambda } ({\displaystyle \lambda })⁠ in its spectrum is an eigenvalue. Furthermore, a compact self-adjoint operator can be diagonalized by its eigenvectors. If ⁠ M {\displaystyle \mathbf {M} } ({\displaystyle \mathbf {M} })⁠ is compact, so is ⁠ M ∗ M {\displaystyle \mathbf {M} ^{*}\mathbf {M} } ({\displaystyle \mathbf {M} ^{*}\mathbf {M} })⁠. Applying the diagonalization result, the unitary image of its positive square root ⁠ T f {\displaystyle T_{f}} ({\displaystyle T_{f}})⁠ has a set of orthonormal eigenvectors ⁠ { e i } {\displaystyle \{e_{i}\}} ({\displaystyle \{e_{i}\}})⁠ corresponding to strictly positive eigenvalues ⁠ { σ i } {\displaystyle \{\sigma _{i}\}} ({\displaystyle \{\sigma _{i}\}})⁠. For any ⁠ ψ {\displaystyle \psi } ({\displaystyle \psi })⁠ in ⁠ H , {\displaystyle H,} ({\displaystyle H,})⁠

M ψ = U T f V ∗ ψ = ∑ i ⟨ U T f V ∗ ψ , U e i ⟩ U e i = ∑ i σ i ⟨ ψ , V e i ⟩ U e i , {\displaystyle \mathbf {M} \psi =\mathbf {U} T_{f}\mathbf {V} ^{*}\psi =\sum _{i}\left\langle \mathbf {U} T_{f}\mathbf {V} ^{*}\psi ,\mathbf {U} e_{i}\right\rangle \mathbf {U} e_{i}=\sum _{i}\sigma _{i}\left\langle \psi ,\mathbf {V} e_{i}\right\rangle \mathbf {U} e_{i},} ({\displaystyle \mathbf {M} \psi =\mathbf {U} T_{f}\mathbf {V} ^{*}\psi =\sum _{i}\left\langle \mathbf {U} T_{f}\mathbf {V} ^{*}\psi ,\mathbf {U} e_{i}\right\rangle \mathbf {U} e_{i}=\sum _{i}\sigma _{i}\left\langle \psi ,\mathbf {V} e_{i}\right\rangle \mathbf {U} e_{i},})

where the series converges in the norm topology on ⁠ H . {\displaystyle H.} ({\displaystyle H.})⁠ Notice how this resembles the expression from the finite-dimensional case. ⁠ σ i {\displaystyle \sigma _{i}} ({\displaystyle \sigma _{i}})⁠ are called the singular values of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠ ⁠ { U e i } {\displaystyle \{\mathbf {U} e_{i}\}} ({\displaystyle \{\mathbf {U} e_{i}\}})⁠ (resp. ⁠ { V e i } {\displaystyle \{\mathbf {V} e_{i}\}} ({\displaystyle \{\mathbf {V} e_{i}\}})⁠) can be considered the left-singular (resp. right-singular) vectors of ⁠ M . {\displaystyle \mathbf {M} .} ({\displaystyle \mathbf {M} .})⁠

Compact operators on a Hilbert space are the closure of finite-rank operators in the uniform operator topology. The above series expression gives an explicit such representation. An immediate consequence of this is:

Theorem.

⁠

M

{\displaystyle \mathbf {M} }

⁠

is compact if and only if

⁠

M

∗

M

{\displaystyle \mathbf {M} ^{*}\mathbf {M} }

⁠

is compact.


## History

The singular value decomposition was originally developed by differential geometers, who wished to determine whether a real bilinear form could be made equal to another by independent orthogonal transformations of the two spaces it acts on. Eugenio Beltrami and Camille Jordan discovered independently, in 1873 and 1874 respectively, that the singular values of the bilinear forms, represented as a matrix, form a complete set of invariants for bilinear forms under orthogonal substitutions. James Joseph Sylvester also arrived at the singular value decomposition for real square matrices in 1889, apparently independently of both Beltrami and Jordan. Sylvester called the singular values the *canonical multipliers* of the matrix ⁠ A . {\displaystyle \mathbf {A} .} ({\displaystyle \mathbf {A} .})⁠ The fourth mathematician to discover the singular value decomposition independently is Autonne in 1915, who arrived at it via the polar decomposition. The first proof of the singular value decomposition for rectangular and complex matrices seems to be by Carl Eckart and Gale J. Young in 1936; they saw it as a generalization of the principal axis transformation for Hermitian matrices.

In 1907, Erhard Schmidt defined an analog of singular values for integral operators (which are compact, under some weak technical assumptions); it seems he was unaware of the parallel work on singular values of finite matrices. This theory was further developed by Émile Picard in 1910, who is the first to call the numbers σ k {\displaystyle \sigma _{k}} ({\displaystyle \sigma _{k}}) *singular values* (or in French, *valeurs singulières*).

Practical methods for computing the SVD date back to Kogbetliantz in 1954–1955 and Hestenes in 1958, resembling closely the Jacobi eigenvalue algorithm, which uses plane rotations or Givens rotations. However, these were replaced by the method of Gene Golub and William Kahan published in 1965, which uses Householder transformations or reflections. In 1970, Golub and Christian Reinsch published a variant of the Golub/Kahan algorithm that is still the one most-used today.

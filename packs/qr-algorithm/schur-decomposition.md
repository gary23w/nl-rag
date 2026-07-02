---
title: "Schur decomposition"
source: https://en.wikipedia.org/wiki/Schur_decomposition
domain: qr-algorithm
license: CC-BY-SA-4.0
tags: qr algorithm, qr decomposition, hessenberg matrix, givens rotation
fetched: 2026-07-02
---

# Schur decomposition

In linear algebra, the **Schur decomposition** or **Schur triangulation**, named after Issai Schur, is a matrix decomposition. It allows one to write an arbitrary complex square matrix as unitarily similar to an upper triangular matrix whose diagonal elements are the eigenvalues of the original matrix.

## Statement

The complex Schur decomposition reads as follows: if A is an *n* × *n* square matrix with complex entries, then *A* can be expressed as $A=QUQ^{-1}$ for some unitary matrix *Q* (so that the inverse *Q*−1 is also the conjugate transpose *Q** of *Q*), and some upper triangular matrix *U*. This is called a **Schur form** of *A*. Since *U* is similar to *A*, it has the same spectrum, and since it is triangular, its eigenvalues are the diagonal entries of *U*.

The Schur decomposition implies that there exists a nested sequence of *A*-invariant subspaces {0} = *V*0 ⊂ *V*1 ⊂ ⋯ ⊂ *Vn* = **C***n*, and that there exists an ordered orthonormal basis (for the standard Hermitian form of **C***n*) such that the first *i* basis vectors span *V**i* for each *i* occurring in the nested sequence. Phrased somewhat differently, the first part says that a linear operator *J* on a complex finite-dimensional vector space stabilizes a complete flag (*V*1, ..., *Vn*).

There is also a real Schur decomposition. If A is an *n* × *n* square matrix with real entries, then *A* can be expressed as $A=QHQ^{-1}$ where Q is an orthogonal matrix and H is either upper or lower quasi-triangular. A quasi-triangular matrix is a matrix that when expressed as a block matrix of *2* × *2* and *1* × *1* blocks is triangular. This is a stronger property than being Hessenberg. Just as in the complex case, a family of commuting real matrices {*Ai*} may be simultaneously brought to quasi-triangular form by an orthogonal matrix. There exists an orthogonal matrix *Q* such that, for every *Ai* in the given family, $H_{i}=QA_{i}Q^{-1}$ is upper quasi-triangular.

## Proof

A constructive proof for the Schur decomposition is as follows: every operator *A* on a complex finite-dimensional vector space has an eigenvalue *λ*, corresponding to some eigenspace *Vλ*. Let *Vλ*⊥ be its orthogonal complement. It is clear that, with respect to this orthogonal decomposition, *A* has matrix representation (one can pick here any orthonormal bases *Z*1 and *Z*2 spanning *Vλ* and *Vλ*⊥ respectively) ${\begin{bmatrix}Z_{1}&Z_{2}\end{bmatrix}}^{*}A{\begin{bmatrix}Z_{1}&Z_{2}\end{bmatrix}}={\begin{bmatrix}\lambda \,I_{\lambda }&A_{12}\\0&A_{22}\end{bmatrix}}:{\begin{matrix}V_{\lambda }\\\oplus \\V_{\lambda }^{\perp }\end{matrix}}\rightarrow {\begin{matrix}V_{\lambda }\\\oplus \\V_{\lambda }^{\perp }\end{matrix}}$ where *Iλ* is the identity operator on *Vλ*. The above matrix would be upper-triangular except for the *A*22 block. But exactly the same procedure can be applied to the sub-matrix *A*22, viewed as an operator on *Vλ*⊥, and its submatrices. Continue this way until the resulting matrix is upper triangular. Since each conjugation increases the dimension of the upper-triangular block by at least one, this process takes at most *n* steps. Thus the space **C***n* will be exhausted and the procedure has yielded the desired result.

The above argument can be slightly restated as follows: let *λ* be an eigenvalue of *A*, corresponding to some eigenspace *Vλ*. *A* induces an operator *T* on the quotient space **C***n*/*Vλ*. This operator is precisely the *A*22 submatrix from above. As before, *T* would have an eigenspace, say *Wμ* ⊂ **C***n* modulo *Vλ*. Notice the preimage of *Wμ* under the quotient map is an invariant subspace of *A* that contains *Vλ*. Continue this way until the resulting quotient space has dimension 0. Then the successive preimages of the eigenspaces found at each step form a flag that *A* stabilizes.

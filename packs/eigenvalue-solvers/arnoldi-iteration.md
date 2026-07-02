---
title: "Arnoldi iteration"
source: https://en.wikipedia.org/wiki/Arnoldi_iteration
domain: eigenvalue-solvers
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, lanczos algorithm, arnoldi iteration, qr algorithm
fetched: 2026-07-02
---

# Arnoldi iteration

In numerical linear algebra, the **Arnoldi iteration** is an eigenvalue algorithm and an important example of an iterative method. Arnoldi finds an approximation to the eigenvalues and eigenvectors of general (possibly non-Hermitian) matrices by constructing an orthonormal basis of the Krylov subspace, which makes it particularly useful when dealing with large sparse matrices.

The Arnoldi method belongs to a class of linear algebra algorithms that give a partial result after a small number of iterations, in contrast to so-called *direct methods* which must complete to give any useful results (see for example, Householder transformation). The partial result in this case being the first few vectors of the basis the algorithm is building.

When applied to Hermitian matrices it reduces to the Lanczos algorithm. The Arnoldi iteration was invented by W. E. Arnoldi in 1951.

## Krylov subspaces and the power iteration

An intuitive method for finding the largest (in absolute value) eigenvalue of a given *m* × *m* matrix A is the power iteration: starting with an arbitrary initial vector *b*, calculate *Ab*, *A*2*b*, *A*3*b*, ... normalizing the result after every application of the matrix *A*.

This sequence converges to the eigenvector corresponding to the eigenvalue with the largest absolute value, $\lambda _{1}$ . However, much potentially useful computation is wasted by using only the final result, $A^{n-1}b$ . This suggests that instead, we form the so-called *Krylov matrix*:

$K_{n}={\begin{bmatrix}b&Ab&A^{2}b&\cdots &A^{n-1}b\end{bmatrix}}.$

The columns of this matrix are not in general orthogonal, but we can extract an orthogonal basis, via a method such as Gram–Schmidt orthogonalization. The resulting set of vectors is thus an orthogonal basis of the *Krylov subspace*, ${\mathcal {K}}_{n}$ . We may expect the vectors of this basis to span good approximations of the eigenvectors corresponding to the n largest eigenvalues, for the same reason that $A^{n-1}b$ approximates the dominant eigenvector.

## The Arnoldi iteration

The Arnoldi iteration uses the modified Gram–Schmidt process to produce a sequence of orthonormal vectors, *q*1, *q*2, *q*3, ..., called the *Arnoldi vectors*, such that for every *n*, the vectors *q*1, ..., *q**n* span the Krylov subspace ${\mathcal {K}}_{n}$ . Explicitly, the algorithm is as follows:

```
Start with an arbitrary vector q1 with norm 1.
Repeat for k = 2, 3, ...
    qk := A qk−1
    for j from 1 to k − 1
        hj,k−1 :=  qj* qk
        qk := qk − hj,k−1 qj
    hk,k−1 := ‖qk‖
    qk := qk / hk,k−1
```

The *j*-loop projects out the component of $q_{k}$ in the directions of $q_{1},\dots ,q_{k-1}$ . This ensures the orthogonality of all the generated vectors.

The algorithm breaks down when *q**k* is the zero vector. This happens when the minimal polynomial of *A* is of degree *k*. In most applications of the Arnoldi iteration, including the eigenvalue algorithm below and GMRES, the algorithm has converged at this point.

Every step of the *k*-loop takes one matrix-vector product and approximately 4*mk* floating point operations.

In the programming language Python with support of the NumPy library:

```mw
import numpy as np

def arnoldi_iteration(A, b, n: int):
    """Compute a basis of the (n + 1)-Krylov subspace of the matrix A.

    This is the space spanned by the vectors {b, Ab, ..., A^n b}.

    Parameters
    ----------
    A : array_like
        An m × m array.
    b : array_like
        Initial vector (length m).
    n : int
        One less than the dimension of the Krylov subspace, or equivalently the *degree* of the Krylov space. Must be >= 1.
    
    Returns
    -------
    Q : numpy.array
        An m x (n + 1) array, where the columns are an orthonormal basis of the Krylov subspace.
    h : numpy.array
        An (n + 1) x n array. A on basis Q. It is upper Hessenberg.
    """
    eps = 1e-12
    h = np.zeros((n + 1, n))
    Q = np.zeros((A.shape[0], n + 1))
    # Normalize the input vector
    Q[:, 0] = b / np.linalg.norm(b, 2)  # Use it as the first Krylov vector
    for k in range(1, n + 1):
        v = np.dot(A, Q[:, k - 1])  # Generate a new candidate vector
        for j in range(k):  # Subtract the projections on previous vectors
            h[j, k - 1] = np.dot(Q[:, j].conj(), v)
            v = v - h[j, k - 1] * Q[:, j]
        h[k, k - 1] = np.linalg.norm(v, 2)
        if h[k, k - 1] > eps:  # Add the produced vector to the list, unless
            Q[:, k] = v / h[k, k - 1]
        else:  # If that happens, stop iterating.
            return Q, h
    return Q, h
```

## Properties of the Arnoldi iteration

Let *Q**n* denote the *m*-by-*n* matrix formed by the first *n* Arnoldi vectors *q*1, *q*2, ..., *q**n*, and let *H**n* be the (upper Hessenberg) matrix formed by the numbers *h**j*,*k* computed by the algorithm:

$H_{n}=Q_{n}^{*}AQ_{n}.$

The orthogonalization method has to be specifically chosen such that the lower Arnoldi/Krylov components are removed from higher Krylov vectors. As $Aq_{i}$ can be expressed in terms of *q*1, ..., *q**i*+1 by construction, they are orthogonal to *q**i*+2, ..., *q**n*,

We then have

$H_{n}={\begin{bmatrix}h_{1,1}&h_{1,2}&h_{1,3}&\cdots &h_{1,n}\\h_{2,1}&h_{2,2}&h_{2,3}&\cdots &h_{2,n}\\0&h_{3,2}&h_{3,3}&\cdots &h_{3,n}\\\vdots &\ddots &\ddots &\ddots &\vdots \\0&\cdots &0&h_{n,n-1}&h_{n,n}\end{bmatrix}}.$

The matrix *H**n* can be viewed as *A* in the subspace ${\mathcal {K}}_{n}$ with the Arnoldi vectors as an orthogonal basis; *A* is orthogonally projected onto ${\mathcal {K}}_{n}$ . The matrix *H**n* can be characterized by the following optimality condition. The characteristic polynomial of *H**n* minimizes ||*p*(*A*)*q*1||2 among all monic polynomials of degree *n*. This optimality problem has a unique solution if and only if the Arnoldi iteration does not break down.

The relation between the *Q* matrices in subsequent iterations is given by

$AQ_{n}=Q_{n+1}{\tilde {H}}_{n}$

where

${\tilde {H}}_{n}={\begin{bmatrix}h_{1,1}&h_{1,2}&h_{1,3}&\cdots &h_{1,n}\\h_{2,1}&h_{2,2}&h_{2,3}&\cdots &h_{2,n}\\0&h_{3,2}&h_{3,3}&\cdots &h_{3,n}\\\vdots &\ddots &\ddots &\ddots &\vdots \\\vdots &&0&h_{n,n-1}&h_{n,n}\\0&\cdots &\cdots &0&h_{n+1,n}\end{bmatrix}}$

is an (*n*+1)-by-*n* matrix formed by adding an extra row to *H**n*.

## Finding eigenvalues with the Arnoldi iteration

The idea of the Arnoldi iteration as an eigenvalue algorithm is to compute the eigenvalues in the Krylov subspace. The eigenvalues of *H**n* are called the *Ritz eigenvalues*. Since *H**n* is a Hessenberg matrix of modest size, its eigenvalues can be computed efficiently, for instance with the QR algorithm, or somewhat related, Francis' algorithm. Also Francis' algorithm itself can be considered to be related to power iterations, operating on nested Krylov subspace. In fact, the most basic form of Francis' algorithm appears to be to choose *b* to be equal to *Ae*1, and extending *n* to the full dimension of *A*. Improved versions include one or more shifts, and higher powers of *A* may be applied in a single steps.

This is an example of the Rayleigh-Ritz method.

It is often observed in practice that some of the Ritz eigenvalues converge to eigenvalues of *A*. Since *H**n* is *n*-by-*n*, it has at most *n* eigenvalues, and not all eigenvalues of *A* can be approximated. Typically, the Ritz eigenvalues converge to the largest eigenvalues of *A*. To get the smallest eigenvalues of *A*, the inverse (operation) of *A* should be used instead. This can be related to the characterization of *H**n* as the matrix whose characteristic polynomial minimizes ||*p*(*A*)*q*1|| in the following way. A good way to get *p*(*A*) small is to choose the polynomial *p* such that *p*(*x*) is small whenever *x* is an eigenvalue of *A*. Hence, the zeros of *p* (and thus the Ritz eigenvalues) will be close to the eigenvalues of *A*.

However, the details are not fully understood yet. This is in contrast to the case where *A* is Hermitian. In that situation, the Arnoldi iteration becomes the Lanczos iteration, for which the theory is more complete.

## Restarted Arnoldi iteration

Due to practical storage consideration, common implementations of Arnoldi methods typically restart after a fixed number of iterations. One approach is the Implicitly Restarted Arnoldi Method (IRAM) by Lehoucq and Sorensen, which was popularized in the free and open source software package ARPACK. Another approach is the Krylov-Schur Algorithm by G. W. Stewart, which is more stable and simpler to implement than IRAM.

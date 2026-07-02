---
title: "Cholesky decomposition"
source: https://en.wikipedia.org/wiki/Cholesky_decomposition
domain: numerical-linear-algebra
license: CC-BY-SA-4.0
tags: numerical linear algebra, matrix decomposition, conjugate gradient method, krylov subspace
fetched: 2026-07-02
---

# Cholesky decomposition

In linear algebra, the **Cholesky decomposition** or **Cholesky factorization** (pronounced /ʃəˈlɛski/ *shə-LES-kee*) is a decomposition of a Hermitian, positive-definite matrix into the product of a lower triangular matrix and its conjugate transpose, which is useful for efficient numerical solutions, e.g., Monte Carlo simulations. It was discovered by André-Louis Cholesky for real matrices, and posthumously published in 1924. When it is applicable, the Cholesky decomposition is roughly twice as efficient as the LU decomposition for solving systems of linear equations.

## Statement

The Cholesky decomposition of a Hermitian positive-definite matrix **A** is a decomposition of the form

$\mathbf {A} =\mathbf {LL} ^{*},$

where **L** is a lower triangular matrix with real and positive diagonal entries, and **L*** denotes the conjugate transpose of **L**. Every Hermitian positive-definite matrix (and thus also every real symmetric positive-definite matrix) has a Cholesky decomposition and the lower triangular matrix is unique if we impose the diagonal to be strictly positive.

The converse holds trivially: if **A** can be written as **LL*** for some invertible **L**, lower triangular or otherwise, then **A** is Hermitian and positive definite.

When **A** is a real matrix (hence symmetric positive-definite), the factorization may be written $\mathbf {A} =\mathbf {LL} ^{\mathsf {T}},$ where **L** is a real lower triangular matrix with positive diagonal entries.

### Positive semidefinite matrices

If a Hermitian matrix **A** is only positive semidefinite, instead of positive definite, then it still has a decomposition of the form **A** = **LL*** where the diagonal entries of **L** are allowed to be zero. The decomposition need not be unique, for example: ${\begin{bmatrix}0&0\\0&1\end{bmatrix}}=\mathbf {L} \mathbf {L} ^{*},\quad \quad \mathbf {L} ={\begin{bmatrix}0&0\\\cos \theta &\sin \theta \end{bmatrix}},$ for any θ. However, if the rank of **A** is r, then there is a unique lower triangular **L** with exactly r positive diagonal elements and *n* − *r* columns containing all zeroes.

Alternatively, the decomposition can be made unique when a pivoting choice is fixed. Formally, if **A** is an *n* × *n* positive semidefinite matrix of rank r, then there is at least one permutation matrix **P** such that **P A P**T has a unique decomposition of the form **P A P**T = **L L*** with ${\textstyle \mathbf {L} ={\begin{bmatrix}\mathbf {L} _{1}&0\\\mathbf {L} _{2}&0\end{bmatrix}}}$ , where **L**1 is an *r* × *r* lower triangular matrix with positive diagonal.

## LDL decomposition

A closely related variant of the classical Cholesky decomposition is the LDL decomposition, also known as Bunch-Kaufman factorization

$\mathbf {A} =\mathbf {LDL} ^{*},$

where **L** is a lower unit triangular (unitriangular) matrix, and **D** is a diagonal matrix. That is, the diagonal elements of **L** are required to be 1 at the cost of introducing an additional diagonal matrix **D** in the decomposition. The main advantage is that the LDL decomposition can be computed and used with essentially the same algorithms, but avoids extracting square roots.

For this reason, the LDL decomposition is often called the *square-root-free Cholesky* decomposition. For real matrices, the factorization has the form **A** = **LDL**T and is often referred to as **LDLT decomposition** (or **LDLT** decomposition, or **LDL′**). It is reminiscent of the eigendecomposition of real symmetric matrices, **A** = **QΛQ**T, but is quite different in practice because **Λ** and **D** are not similar matrices.

The LDL decomposition is related to the classical Cholesky decomposition of the form **LL*** as follows:

$\mathbf {A} =\mathbf {LDL} ^{*}=\mathbf {L} \mathbf {D} ^{1/2}\left(\mathbf {D} ^{1/2}\right)^{*}\mathbf {L} ^{*}=\mathbf {L} \mathbf {D} ^{1/2}\left(\mathbf {L} \mathbf {D} ^{1/2}\right)^{*}.$

Conversely, given the classical Cholesky decomposition ${\textstyle \mathbf {A} =\mathbf {C} \mathbf {C} ^{*}}$ of a positive definite matrix, if **S** is a diagonal matrix that contains the main diagonal of ${\textstyle \mathbf {C} }$ , then **A** can be decomposed as ${\textstyle \mathbf {L} \mathbf {D} \mathbf {L} ^{*}}$ where $\mathbf {L} =\mathbf {C} \mathbf {S} ^{-1}$ (this rescales each column to make diagonal elements 1), $\mathbf {D} =\mathbf {S} \mathbf {S} ^{*}.$

If **A** is positive definite then the diagonal elements of **D** are all positive. For positive semidefinite **A**, an ${\textstyle \mathbf {L} \mathbf {D} \mathbf {L} ^{*}}$ decomposition exists where the number of non-zero elements on the diagonal **D** is exactly the rank of **A**. Some indefinite matrices for which no Cholesky decomposition exists have an LDL decomposition with negative entries in **D**: it suffices that the first *n* − 1 leading principal minors of **A** are non-singular.

## Example

Here is the Cholesky decomposition of a symmetric real matrix:

${\begin{aligned}{\begin{pmatrix}4&12&-16\\12&37&-43\\-16&-43&98\\\end{pmatrix}}={\begin{pmatrix}2&0&0\\6&1&0\\-8&5&3\\\end{pmatrix}}{\begin{pmatrix}2&6&-8\\0&1&5\\0&0&3\\\end{pmatrix}}.\end{aligned}}$

And here is its LDLT decomposition:

${\begin{aligned}{\begin{pmatrix}4&12&-16\\12&37&-43\\-16&-43&98\\\end{pmatrix}}&={\begin{pmatrix}1&0&0\\3&1&0\\-4&5&1\\\end{pmatrix}}{\begin{pmatrix}4&0&0\\0&1&0\\0&0&9\\\end{pmatrix}}{\begin{pmatrix}1&3&-4\\0&1&5\\0&0&1\\\end{pmatrix}}.\end{aligned}}$

## Geometric interpretation

The Cholesky decomposition is equivalent to a particular choice of conjugate axes of an ellipsoid. In detail, let the ellipsoid be defined as ${\textstyle y^{T}Ay=1}$ , then by definition, a set of vectors ${\textstyle v_{1},...,v_{n}}$ are conjugate axes of the ellipsoid iff ${\textstyle v_{i}^{T}Av_{j}=\delta _{ij}}$ . Then, the ellipsoid is precisely $\left\{\sum _{i}x_{i}v_{i}:x^{T}x=1\right\}=f(\mathbb {S} ^{n})$ where ${\textstyle f}$ maps the basis vector ${\textstyle e_{i}\mapsto v_{i}}$ , and ${\textstyle \mathbb {S} ^{n}}$ is the unit sphere in n dimensions. That is, the ellipsoid is a linear image of the unit sphere.

Define the matrix ${\textstyle V:=[v_{1}|v_{2}|\cdots |v_{n}]}$ , then ${\textstyle v_{i}^{T}Av_{j}=\delta _{ij}}$ is equivalent to ${\textstyle V^{T}AV=I}$ . Different choices of the conjugate axes correspond to different decompositions.

The Cholesky decomposition corresponds to choosing ${\textstyle v_{1}}$ to be parallel to the first axis, ${\textstyle v_{2}}$ to be within the plane spanned by the first two axes, and so on. This makes ${\textstyle V}$ an upper-triangular matrix. Then, there is ${\textstyle A=LL^{T}}$ , where ${\textstyle L=(V^{-1})^{T}}$ is lower-triangular.

Similarly, principal component analysis corresponds to choosing ${\textstyle v_{1},...,v_{n}}$ to be perpendicular. Then, let ${\textstyle \lambda =1/\|v_{i}\|^{2}}$ and ${\textstyle \Sigma =\mathrm {diag} (\lambda _{1},...,\lambda _{n})}$ , and there is ${\textstyle V=U\Sigma ^{-1/2}}$ where ${\textstyle U}$ is an orthogonal matrix. This then yields ${\textstyle A=U\Sigma U^{T}}$ .

## Applications

### Numerical solution of system of linear equations

The Cholesky decomposition is mainly used for the numerical solution of linear equations ${\textstyle \mathbf {Ax} =\mathbf {b} }$ . If **A** is symmetric and positive definite, then ${\textstyle \mathbf {Ax} =\mathbf {b} }$ can be solved by first computing the Cholesky decomposition ${\textstyle \mathbf {A} =\mathbf {LL} ^{\mathrm {*} }}$ , then solving ${\textstyle \mathbf {Ly} =\mathbf {b} }$ for **y** by forward substitution, and finally solving ${\textstyle \mathbf {L^{*}x} =\mathbf {y} }$ for **x** by back substitution.

An alternative way to eliminate taking square roots in the ${\textstyle \mathbf {LL} ^{\mathrm {*} }}$ decomposition is to compute the LDL decomposition ${\textstyle \mathbf {A} =\mathbf {LDL} ^{\mathrm {*} }}$ , then solving ${\textstyle \mathbf {Ly} =\mathbf {b} }$ for **y**, and finally solving ${\textstyle \mathbf {DL} ^{\mathrm {*} }\mathbf {x} =\mathbf {y} }$ .

For linear systems that can be put into symmetric form, the Cholesky decomposition (or its LDL variant) is the method of choice, for superior efficiency and numerical stability. Compared to the LU decomposition, it is roughly twice as efficient.

### Linear least squares

In linear least squares problem one seeks a solution **x** of an over-determined system **Ax** = **l**, such that quadratic norm of the residual vector **Ax-l** is minimum. This may be accomplished by solving by Cholesky decomposition normal equations $\mathbf {Nx} =\mathbf {A} ^{\mathsf {T}}\mathbf {l}$ , where $\mathbf {N} =\mathbf {A} ^{\mathsf {T}}\mathbf {A}$ is symmetric positive definite. Symmetric equation matrix may also come from an energy functional, which must be positive from physical considerations; this happens frequently in the numerical solution of partial differential equations.

Such method is economic and works well in many applications, however it fails for near singular **N**. This is best illustrated in pathological case of square $\mathbf {A}$ , where determinant of **N** is square of that of the original system **Ax** = **l**. Then it is best to apply SVD or QR decomposition. Givens QR has the advantage that similarly to normal equations there is no need to keep the whole matrix **A** as it is possible to update Cholesky factor with consecutive rows of **A**.

### Non-linear optimization

Non-linear least squares are a particular case of nonlinear optimization. Let ${\textstyle \mathbf {f} (\mathbf {x} )=\mathbf {l} }$ be an over-determined system of equations with a non-linear function $\mathbf {f}$ returning vector results. The aim is to minimize square norm of residuals ${\textstyle \mathbf {v} =\mathbf {f} (\mathbf {x} )-\mathbf {l} }$ . An approximate Newton's method solution is obtained by expanding $\mathbf {f}$ into curtailed Taylor series ${\bf {f(x_{\rm {0}}+\delta x)\approx f(x_{\rm {0}})+(\partial f/\partial x)\delta x}}$ yielding linear least squares problem for ${\bf {\delta x}}$

${\bf {(\partial f/\partial x)\delta x=l-f(x_{\rm {0}})=v,\;\;\min _{\delta x}=\|v\|^{2}}}.$

Of course because of neglect of higher Taylor terms such solution is only approximate, if it ever exists. Now one could update expansion point to ${\bf {x_{\rm {n+1}}=x_{\rm {n}}+\delta x}}$ and repeat the whole procedure, hoping that (i) iterations converge to a solution and (ii) that the solution is the one needed. Unfortunately neither is guaranteed and must be verified.

Non-linear least squares may be also applied to the linear least squares problem by setting ${\bf {x_{\rm {0}}=0}}$ and ${\bf {f(x_{\rm {0}})=Ax}}$ . This may be useful if Cholesky decomposition yields an inaccurate inverse ${\bf {R^{\rm {-1}}}}$ for the triangle matrix where ${\bf {R^{\rm {T}}R=N}}$ , because of rounding errors. Such a procedure is called a *differential correction* of the solution. As long as iterations converge, by virtue of the Banach fixed-point theorem they yield the solution with a precision that is only limited by the precision of the calculated residuals ${\bf {v=Ax-l}}$ . The precision is independent rounding errors in ${\bf {R^{\rm {-1}}}}$ . Poor ${\bf {R^{\rm {-1}}}}$ may restrict region of initial ${\bf {x_{\rm {0}}}}$ yielding convergence or altogether preventing it. Usually convergence is slower e.g. linear so that ${\bf {\|\delta x_{\rm {n+1}}\|\approx \|=\alpha \delta x_{\rm {n}}\|}}$ where constant $\alpha <1$ . Such slow convergence may be sped by *Aitken $\delta ^{2}$* method. If calculation of ${\bf {R^{\rm {-1}}}}$ is very costly, it is possible to use it from previous iterations as long as convergence is maintained. Such Cholesky procedure may work even for Hilbert matrices, notoriously difficult to invert.

Non-linear multi-variate functions may be minimized over their parameters using variants of Newton's method called *quasi-Newton* methods. At iteration k, the search steps in a direction ${\textstyle p_{k}}$ defined by solving ${\textstyle B_{k}p_{k}=-g_{k}}$ for ${\textstyle p_{k}}$ , where ${\textstyle p_{k}}$ is the step direction, ${\textstyle g_{k}}$ is the gradient, and ${\textstyle B_{k}}$ is an approximation to the Hessian matrix formed by repeating rank-1 updates at each iteration. Two well-known update formulas are called Davidon–Fletcher–Powell (DFP) and Broyden–Fletcher–Goldfarb–Shanno (BFGS). Loss of the positive-definite condition through round-off error is avoided if rather than updating an approximation to the inverse of the Hessian, one updates the Cholesky decomposition of an approximation of the Hessian matrix itself.

### Monte Carlo simulation

The Cholesky decomposition is commonly used in the Monte Carlo method for simulating systems with multiple correlated variables. The covariance matrix is decomposed to give the lower-triangular **L**. Applying this to a vector of uncorrelated observations in a sample **u** produces a sample vector **Lu** with the covariance properties of the system being modeled.

The following simplified example shows the economy one gets from the Cholesky decomposition: suppose the goal is to generate two correlated normal variables ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ with given correlation coefficient ${\textstyle \rho }$ . To accomplish that, it is necessary to first generate two uncorrelated Gaussian random variables ${\textstyle z_{1}}$ and ${\textstyle z_{2}}$ (for example, via a Box–Muller transform). Given the required correlation coefficient ${\textstyle \rho }$ , the correlated normal variables can be obtained via the transformations ${\textstyle x_{1}=z_{1}}$ and ${\textstyle x_{2}=\rho z_{1}+{\sqrt {1-\rho ^{2}}}z_{2}}$ .

### Kalman filters

Unscented Kalman filters commonly use the Cholesky decomposition to choose a set of so-called sigma points. The Kalman filter tracks the average state of a system as a vector **x** of length N and covariance as an *N* × *N* matrix **P**. The matrix **P** is always positive semi-definite and can be decomposed into **LL**T. The columns of **L** can be added and subtracted from the mean **x** to form a set of 2*N* vectors called *sigma points*. These sigma points completely capture the mean and covariance of the system state.

### Matrix inversion

The explicit inverse of a Hermitian matrix can be computed by Cholesky decomposition, in a manner similar to solving linear systems, using ${\textstyle n^{3}}$ operations ( ${\textstyle {\tfrac {1}{2}}n^{3}}$ multiplications). The entire inversion can even be efficiently performed in-place.

A non-Hermitian matrix **B** can also be inverted using the following identity, where **BB*** will always be Hermitian:

$\mathbf {B} ^{-1}=\mathbf {B} ^{*}(\mathbf {BB} ^{*})^{-1}.$

### Data Imputation

Cholesky decomposition can also be used to impute data. Variations of the expectation maximization algorithm among other data imputation algorithms, make use of Cholesky decomposition.

## Computation

There are various methods for calculating the Cholesky decomposition. The computational complexity of commonly used algorithms is *O*(*n*3) in general. The algorithms described below all involve about (1/3)*n*3 FLOPs (*n*3/6 multiplications and the same number of additions) for real flavors and (4/3)*n*3 FLOPs for complex flavors, where n is the size of the matrix **A**. Hence, they have half the cost of the LU decomposition, which uses 2*n*3/3 FLOPs (see Trefethen and Bau 1997).

Which of the algorithms below is faster depends on the details of the implementation. Generally, the first algorithm will be slightly slower because it accesses the data in a less regular manner. The Cholesky decomposition was shown to be numerically stable without need for pivoting.

### The Cholesky algorithm

The **Cholesky algorithm**, used to calculate the decomposition matrix **L**, is a modified version of Gaussian elimination.

The recursive algorithm starts with *i* := 1 and

A

(1)

:=

A

.

At step i, the matrix **A**(*i*) has the following form: $\mathbf {A} ^{(i)}={\begin{pmatrix}\mathbf {I} _{i-1}&0&0\\0&a_{i,i}&\mathbf {b} _{i}^{*}\\0&\mathbf {b} _{i}&\mathbf {B} ^{(i)}\end{pmatrix}},$ where **I***i*−1 denotes the identity matrix of dimension *i* − 1.

If the matrix **L***i* is defined by $\mathbf {L} _{i}:={\begin{pmatrix}\mathbf {I} _{i-1}&0&0\\0&{\sqrt {a_{i,i}}}&0\\0&{\frac {1}{\sqrt {a_{i,i}}}}\mathbf {b} _{i}&\mathbf {I} _{n-i}\end{pmatrix}},$ (note that *a**i,i* > 0 since **A**(*i*) is positive definite), then **A**(*i*) can be written as $\mathbf {A} ^{(i)}=\mathbf {L} _{i}\mathbf {A} ^{(i+1)}\mathbf {L} _{i}^{*}$ where $\mathbf {A} ^{(i+1)}={\begin{pmatrix}\mathbf {I} _{i-1}&0&0\\0&1&0\\0&0&\mathbf {B} ^{(i)}-{\frac {1}{a_{i,i}}}\mathbf {b} _{i}\mathbf {b} _{i}^{*}\end{pmatrix}}.$ Note that **b***i* **b***i** is an outer product, therefore this algorithm is called the *outer-product version* in (Golub & Van Loan).

This is repeated for i from 1 to n. After n steps, **A**(*n*+1) = **I** is obtained, and hence, the lower triangular matrix L sought for is calculated as

$\mathbf {L} :=\mathbf {L} _{1}\mathbf {L} _{2}\dots \mathbf {L} _{n}.$

### The Cholesky–Banachiewicz and Cholesky–Crout algorithms

If the equation ${\begin{aligned}\mathbf {A} =\mathbf {LL} ^{T}&={\begin{pmatrix}L_{11}&0&0\\L_{21}&L_{22}&0\\L_{31}&L_{32}&L_{33}\\\end{pmatrix}}{\begin{pmatrix}L_{11}&L_{21}&L_{31}\\0&L_{22}&L_{32}\\0&0&L_{33}\end{pmatrix}}\\[8pt]&={\begin{pmatrix}L_{11}^{2}&&({\text{symmetric}})\\L_{21}L_{11}&L_{21}^{2}+L_{22}^{2}&\\L_{31}L_{11}&L_{31}L_{21}+L_{32}L_{22}&L_{31}^{2}+L_{32}^{2}+L_{33}^{2}\end{pmatrix}},\end{aligned}}$

is written out, the following is obtained:

${\begin{aligned}\mathbf {L} ={\begin{pmatrix}{\sqrt {A_{11}}}&0&0\\A_{21}/L_{11}&{\sqrt {A_{22}-L_{21}^{2}}}&0\\A_{31}/L_{11}&\left(A_{32}-L_{31}L_{21}\right)/L_{22}&{\sqrt {A_{33}-L_{31}^{2}-L_{32}^{2}}}\end{pmatrix}}\end{aligned}}$

and therefore the following formulas for the entries of **L**:

$L_{j,j}=(\pm ){\sqrt {A_{j,j}-\sum _{k=1}^{j-1}L_{j,k}^{2}}},$ $L_{i,j}={\frac {1}{L_{j,j}}}\left(A_{i,j}-\sum _{k=1}^{j-1}L_{i,k}L_{j,k}\right)\quad {\text{for }}i>j.$

For complex and real matrices, inconsequential arbitrary sign changes of diagonal and associated off-diagonal elements are allowed. The expression under the square root is always positive if **A** is real and positive-definite.

For complex Hermitian matrix, the following formula applies:

$L_{j,j}={\sqrt {A_{j,j}-\sum _{k=1}^{j-1}L_{j,k}^{*}L_{j,k}}},$ $L_{i,j}={\frac {1}{L_{j,j}}}\left(A_{i,j}-\sum _{k=1}^{j-1}L_{j,k}^{*}L_{i,k}\right)\quad {\text{for }}i>j.$

and it can be shown that $L_{j,j}$ is always *real* and positive if **A** is positive-definite.

So it now is possible to compute the (*i*, *j*) entry if the entries to the left and above are known. The computation is usually arranged in either of the following orders:

- The **Cholesky–Banachiewicz algorithm** starts from the upper left corner of the matrix L and proceeds to calculate the matrix row by row.

```mw
for (i = 0; i < dimensionSize; i++) {
    for (j = 0; j <= i; j++) {
        float sum = 0;
        for (k = 0; k < j; k++)
            sum += L[i][k] * L[j][k];

        if (i == j)
            L[i][j] = sqrt(A[i][i] - sum);
        else
            L[i][j] = (1.0 / L[j][j] * (A[i][j] - sum));
    }
}
```

The above algorithm can be succinctly expressed as combining a dot product and matrix multiplication in vectorized programming languages such as Fortran as the following,

```mw
do i = 1, size(A,1)
    L(i,i) = sqrt(A(i,i) - dot_product(L(i,1:i-1), L(i,1:i-1)))
    L(i+1:,i) = (A(i+1:,i) - matmul(conjg(L(i,1:i-1)), L(i+1:,1:i-1))) / L(i,i)
end do
```

where `conjg` refers to complex conjugate of the elements.

- The **Cholesky–Crout algorithm** starts from the upper left corner of the matrix L and proceeds to calculate the matrix column by column. for (j = 0; j < dimensionSize; j++) { float sum = 0; for (k = 0; k < j; k++) { sum += L[j][k] * L[j][k]; } L[j][j] = sqrt(A[j][j] - sum); for (i = j + 1; i < dimensionSize; i++) { sum = 0; for (k = 0; k < j; k++) { sum += L[i][k] * L[j][k]; } L[i][j] = (1.0 / L[j][j] * (A[i][j] - sum)); } }

The above algorithm can be succinctly expressed as combining a dot product and matrix multiplication in vectorized programming languages such as Fortran as the following,

```mw
do i = 1, size(A,1)
    L(i,i) = sqrt(A(i,i) - dot_product(L(1:i-1,i), L(1:i-1,i)))
    L(i,i+1:) = (A(i,i+1:) - matmul(conjg(L(1:i-1,i)), L(1:i-1,i+1:))) / L(i,i)
end do
```

where `conjg` refers to complex conjugate of the elements.

Either pattern of access allows the entire computation to be performed in-place if desired.

### Stability of the computation

Suppose that there is a desire to solve a well-conditioned system of linear equations. If the LU decomposition is used, then the algorithm is unstable unless some sort of pivoting strategy is used. In the latter case, the error depends on the so-called growth factor of the matrix, which is usually (but not always) small.

Now, suppose that the Cholesky decomposition is applicable. As mentioned above, the algorithm will be twice as fast. Furthermore, no pivoting is necessary, and the error will always be small. Specifically, if **Ax** = **b**, and **y** denotes the computed solution, then **y** solves the perturbed system (**A** + **E**)**y** = **b**, where $\|\mathbf {E} \|_{2}\leq c_{n}\varepsilon \|\mathbf {A} \|_{2}.$ Here ||·||2 is the matrix 2-norm, *cn* is a small constant depending on n, and ε denotes the unit round-off.

One concern with the Cholesky decomposition to be aware of is the use of square roots. If the matrix being factorized is positive definite as required, the numbers under the square roots are always positive *in exact arithmetic*. Unfortunately, the numbers can become negative because of round-off errors, in which case the algorithm cannot continue. However, this can only happen if the matrix is very ill-conditioned. One way to address this is to add a diagonal correction matrix to the matrix being decomposed in an attempt to promote the positive-definiteness. While this might lessen the accuracy of the decomposition, it can be very favorable for other reasons; for example, when performing Newton's method in optimization, adding a diagonal matrix can improve stability when far from the optimum.

### LDL decomposition

An alternative form, eliminating the need to take square roots when **A** is symmetric, is the symmetric indefinite factorization ${\begin{aligned}\mathbf {A} =\mathbf {LDL} ^{\mathrm {T} }&={\begin{pmatrix}1&0&0\\L_{21}&1&0\\L_{31}&L_{32}&1\\\end{pmatrix}}{\begin{pmatrix}D_{1}&0&0\\0&D_{2}&0\\0&0&D_{3}\\\end{pmatrix}}{\begin{pmatrix}1&L_{21}&L_{31}\\0&1&L_{32}\\0&0&1\\\end{pmatrix}}\\[8pt]&={\begin{pmatrix}D_{1}&&(\mathrm {symmetric} )\\L_{21}D_{1}&L_{21}^{2}D_{1}+D_{2}&\\L_{31}D_{1}&L_{31}L_{21}D_{1}+L_{32}D_{2}&L_{31}^{2}D_{1}+L_{32}^{2}D_{2}+D_{3}.\end{pmatrix}}.\end{aligned}}$

The following recursive relations apply for the entries of **D** and **L**: $D_{j}=A_{jj}-\sum _{k=1}^{j-1}L_{jk}^{2}D_{k},$ $L_{ij}={\frac {1}{D_{j}}}\left(A_{ij}-\sum _{k=1}^{j-1}L_{ik}L_{jk}D_{k}\right)\quad {\text{for }}i>j.$

This works as long as the generated diagonal elements in **D** stay non-zero. The decomposition is then unique. **D** and **L** are real if **A** is real.

For complex Hermitian matrix **A**, the following formula applies:

$D_{j}=A_{jj}-\sum _{k=1}^{j-1}L_{jk}L_{jk}^{*}D_{k},$ $L_{ij}={\frac {1}{D_{j}}}\left(A_{ij}-\sum _{k=1}^{j-1}L_{ik}L_{jk}^{*}D_{k}\right)\quad {\text{for }}i>j.$

Again, the pattern of access allows the entire computation to be performed in-place if desired.

### Block variant

When used on indefinite matrices, the **LDL*** factorization is known to be unstable without careful pivoting; specifically, the elements of the factorization can grow arbitrarily. A possible improvement is to perform the factorization on block sub-matrices, commonly 2 × 2:

${\begin{aligned}\mathbf {A} =\mathbf {LDL} ^{\mathrm {T} }&={\begin{pmatrix}\mathbf {I} &0&0\\\mathbf {L} _{21}&\mathbf {I} &0\\\mathbf {L} _{31}&\mathbf {L} _{32}&\mathbf {I} \\\end{pmatrix}}{\begin{pmatrix}\mathbf {D} _{1}&0&0\\0&\mathbf {D} _{2}&0\\0&0&\mathbf {D} _{3}\\\end{pmatrix}}{\begin{pmatrix}\mathbf {I} &\mathbf {L} _{21}^{\mathrm {T} }&\mathbf {L} _{31}^{\mathrm {T} }\\0&\mathbf {I} &\mathbf {L} _{32}^{\mathrm {T} }\\0&0&\mathbf {I} \\\end{pmatrix}}\\[8pt]&={\begin{pmatrix}\mathbf {D} _{1}&&(\mathrm {symmetric} )\\\mathbf {L} _{21}\mathbf {D} _{1}&\mathbf {L} _{21}\mathbf {D} _{1}\mathbf {L} _{21}^{\mathrm {T} }+\mathbf {D} _{2}&\\\mathbf {L} _{31}\mathbf {D} _{1}&\mathbf {L} _{31}\mathbf {D} _{1}\mathbf {L} _{21}^{\mathrm {T} }+\mathbf {L} _{32}\mathbf {D} _{2}&\mathbf {L} _{31}\mathbf {D} _{1}\mathbf {L} _{31}^{\mathrm {T} }+\mathbf {L} _{32}\mathbf {D} _{2}\mathbf {L} _{32}^{\mathrm {T} }+\mathbf {D} _{3}\end{pmatrix}},\end{aligned}}$

where every element in the matrices above is a square submatrix. From this, these analogous recursive relations follow:

$\mathbf {D} _{j}=\mathbf {A} _{jj}-\sum _{k=1}^{j-1}\mathbf {L} _{jk}\mathbf {D} _{k}\mathbf {L} _{jk}^{\mathrm {T} },$ $\mathbf {L} _{ij}=\left(\mathbf {A} _{ij}-\sum _{k=1}^{j-1}\mathbf {L} _{ik}\mathbf {D} _{k}\mathbf {L} _{jk}^{\mathrm {T} }\right)\mathbf {D} _{j}^{-1}.$

This involves matrix products and explicit inversion, thus limiting the practical block size.

### Updating the decomposition

A task that often arises in practice is that one needs to update a Cholesky decomposition. In more details, one has already computed the Cholesky decomposition ${\textstyle \mathbf {A} =\mathbf {L} \mathbf {L} ^{*}}$ of some matrix ${\textstyle \mathbf {A} }$ , then one changes the matrix ${\textstyle \mathbf {A} }$ in some way into another matrix, say ${\textstyle {\tilde {\mathbf {A} }}}$ , and one wants to compute the Cholesky decomposition of the updated matrix: ${\textstyle {\tilde {\mathbf {A} }}={\tilde {\mathbf {L} }}{\tilde {\mathbf {L} }}^{*}}$ . The question is now whether one can use the Cholesky decomposition of ${\textstyle \mathbf {A} }$ that was computed before to compute the Cholesky decomposition of ${\textstyle {\tilde {\mathbf {A} }}}$ .

#### Rank-one update

The specific case, where the updated matrix ${\textstyle {\tilde {\mathbf {A} }}}$ is related to the matrix ${\textstyle \mathbf {A} }$ by ${\textstyle {\tilde {\mathbf {A} }}=\mathbf {A} +c\,\mathbf {x} \mathbf {x} ^{*}}$ , is known as a *rank-one update*. Here the constant c is allowed to be negative, but must always be such that the new matrix ${\textstyle {\tilde {\mathbf {A} }}}$ is still positive definite.

Here is a function written in Matlab syntax that realizes a rank-one update:

```mw
function L=updateChol(L,x,c)
% given the L*L' Cholesky decomposition of a matrix, compute the updated
% factor L so that we have the Cholesky decomposition of L*L'+c*x*x';
n=length(x);
for k=1:n-1
    l=L(:,k); % old value of k-th column
    lk=l(k);
    xk=x(k);
    dk=sqrt(lk^2+c*xk^2); % new diagonal value
    L(:,k)=(lk/dk)*l+(c*xk/dk)*x; % new column value
    x=x-l*(xk/lk);
    c=c*(lk/dk)^2;
end
L(n,n)=sqrt(L(n,n)^2+c*x(n)^2);
end
```

A *rank-n update* is one where for a matrix ${\textstyle \mathbf {M} }$ one updates the decomposition such that ${\textstyle {\tilde {\mathbf {A} }}=\mathbf {A} +\mathbf {M} \mathbf {M} ^{*}}$ . This can be achieved by successively performing rank-one updates for each of the columns of ${\textstyle \mathbf {M} }$ .

#### Adding and removing rows and columns

If a symmetric and positive definite matrix ${\textstyle \mathbf {A} }$ is represented in block form as

$\mathbf {A} ={\begin{pmatrix}\mathbf {A} _{11}&\mathbf {A} _{13}\\\mathbf {A} _{13}^{\mathrm {T} }&\mathbf {A} _{33}\\\end{pmatrix}}$

and its upper Cholesky factor $\mathbf {L} ={\begin{pmatrix}\mathbf {L} _{11}&\mathbf {L} _{13}\\0&\mathbf {L} _{33}\\\end{pmatrix}},$

then for a new matrix ${\textstyle {\tilde {\mathbf {A} }}}$ , which is the same as ${\textstyle \mathbf {A} }$ but with the insertion of new rows and columns, ${\begin{aligned}{\tilde {\mathbf {A} }}&={\begin{pmatrix}\mathbf {A} _{11}&\mathbf {A} _{12}&\mathbf {A} _{13}\\\mathbf {A} _{12}^{\mathrm {T} }&\mathbf {A} _{22}&\mathbf {A} _{23}\\\mathbf {A} _{13}^{\mathrm {T} }&\mathbf {A} _{23}^{\mathrm {T} }&\mathbf {A} _{33}\\\end{pmatrix}}\end{aligned}}$

Now there is an interest in finding the Cholesky factorization of ${\textstyle {\tilde {\mathbf {A} }}}$ , which can be called ${\textstyle {\tilde {\mathbf {S} }}}$ , without directly computing the entire decomposition. ${\begin{aligned}{\tilde {\mathbf {S} }}&={\begin{pmatrix}\mathbf {S} _{11}&\mathbf {S} _{12}&\mathbf {S} _{13}\\0&\mathbf {S} _{22}&\mathbf {S} _{23}\\0&0&\mathbf {S} _{33}\\\end{pmatrix}}.\end{aligned}}$

Writing ${\textstyle \mathbf {A} \setminus \mathbf {b} }$ for the solution of ${\textstyle \mathbf {A} \mathbf {x} =\mathbf {b} }$ , which can be found easily for triangular matrices, and ${\textstyle {\text{chol}}(\mathbf {M} )}$ for the Cholesky decomposition of ${\textstyle \mathbf {M} }$ , the following relations can be found: ${\begin{aligned}\mathbf {S} _{11}&=\mathbf {L} _{11},\\\mathbf {S} _{12}&=\mathbf {L} _{11}^{\mathrm {T} }\setminus \mathbf {A} _{12},\\\mathbf {S} _{13}&=\mathbf {L} _{13},\\\mathbf {S} _{22}&=\mathrm {chol} \left(\mathbf {A} _{22}-\mathbf {S} _{12}^{\mathrm {T} }\mathbf {S} _{12}\right),\\\mathbf {S} _{23}&=\mathbf {S} _{22}^{\mathrm {T} }\setminus \left(\mathbf {A} _{23}-\mathbf {S} _{12}^{\mathrm {T} }\mathbf {S} _{13}\right),\\\mathbf {S} _{33}&=\mathrm {chol} \left(\mathbf {L} _{33}^{\mathrm {T} }\mathbf {L} _{33}-\mathbf {S} _{23}^{\mathrm {T} }\mathbf {S} _{23}\right).\end{aligned}}$

These formulas may be used to determine the Cholesky factor after the insertion of rows or columns in any position, if the row and column dimensions are appropriately set (including to zero). The inverse problem,

${\begin{aligned}{\tilde {\mathbf {A} }}&={\begin{pmatrix}\mathbf {A} _{11}&\mathbf {A} _{12}&\mathbf {A} _{13}\\\mathbf {A} _{12}^{\mathrm {T} }&\mathbf {A} _{22}&\mathbf {A} _{23}\\\mathbf {A} _{13}^{\mathrm {T} }&\mathbf {A} _{23}^{\mathrm {T} }&\mathbf {A} _{33}\\\end{pmatrix}}\end{aligned}}$ with known Cholesky decomposition ${\begin{aligned}{\tilde {\mathbf {S} }}&={\begin{pmatrix}\mathbf {S} _{11}&\mathbf {S} _{12}&\mathbf {S} _{13}\\0&\mathbf {S} _{22}&\mathbf {S} _{23}\\0&0&\mathbf {S} _{33}\\\end{pmatrix}}\end{aligned}}$

and the desire to determine the Cholesky factor ${\begin{aligned}\mathbf {L} &={\begin{pmatrix}\mathbf {L} _{11}&\mathbf {L} _{13}\\0&\mathbf {L} _{33}\\\end{pmatrix}}\end{aligned}}$

of the matrix ${\textstyle \mathbf {A} }$ with rows and columns removed, ${\begin{aligned}\mathbf {A} &={\begin{pmatrix}\mathbf {A} _{11}&\mathbf {A} _{13}\\\mathbf {A} _{13}^{\mathrm {T} }&\mathbf {A} _{33}\\\end{pmatrix}},\end{aligned}}$

yields the following rules: ${\begin{aligned}\mathbf {L} _{11}&=\mathbf {S} _{11},\\\mathbf {L} _{13}&=\mathbf {S} _{13},\\\mathbf {L} _{33}&=\mathrm {chol} \left(\mathbf {S} _{33}^{\mathrm {T} }\mathbf {S} _{33}+\mathbf {S} _{23}^{\mathrm {T} }\mathbf {S} _{23}\right).\end{aligned}}$

Notice that the equations above that involve finding the Cholesky decomposition of a new matrix are all of the form ${\textstyle {\tilde {\mathbf {A} }}=\mathbf {A} +c\,\mathbf {x} \mathbf {x} ^{*}}$ for some constant $c=\pm 1$ , which allows them to be efficiently calculated using procedure detailed in the previous section.

## Proof for positive semi-definite matrices

### Proof by limiting argument

The above algorithms show that every positive definite matrix ${\textstyle \mathbf {A} }$ has a Cholesky decomposition. This result can be extended to the positive semi-definite case by a limiting argument. The argument is not fully constructive, i.e., it gives no explicit numerical algorithms for computing Cholesky factors.

If ${\textstyle \mathbf {A} }$ is an ${\textstyle n\times n}$ positive semi-definite matrix, then the sequence ${\textstyle \left(\mathbf {A} _{k}\right)_{k}:=\left(\mathbf {A} +{\frac {1}{k}}\mathbf {I} _{n}\right)_{k}}$ consists of positive definite matrices. (This is an immediate consequence of, for example, the spectral mapping theorem for the polynomial functional calculus.) Also, $\mathbf {A} _{k}\rightarrow \mathbf {A} \quad {\text{for}}\quad k\rightarrow \infty$ in operator norm. From the positive definite case, each ${\textstyle \mathbf {A} _{k}}$ has Cholesky decomposition ${\textstyle \mathbf {A} _{k}=\mathbf {L} _{k}\mathbf {L} _{k}^{*}}$ . By property of the operator norm,

$\|\mathbf {L} _{k}\|^{2}\leq \|\mathbf {L} _{k}\mathbf {L} _{k}^{*}\|=\|\mathbf {A} _{k}\|\,.$

The ${\textstyle \leq }$ holds because ${\textstyle M_{n}(\mathbb {C} )}$ equipped with the operator norm is a C* algebra. So ${\textstyle \left(\mathbf {L} _{k}\right)_{k}}$ is a bounded set in the Banach space of operators, therefore relatively compact (because the underlying vector space is finite-dimensional). Consequently, it has a convergent subsequence, also denoted by ${\textstyle \left(\mathbf {L} _{k}\right)_{k}}$ , with limit ${\textstyle \mathbf {L} }$ . It can be easily checked that this ${\textstyle \mathbf {L} }$ has the desired properties, i.e. ${\textstyle \mathbf {A} =\mathbf {L} \mathbf {L} ^{*}}$ , and ${\textstyle \mathbf {L} }$ is lower triangular with non-negative diagonal entries: for all ${\textstyle x}$ and ${\textstyle y}$ ,

$\langle \mathbf {A} x,y\rangle =\left\langle \lim \mathbf {A} _{k}x,y\right\rangle =\langle \lim \mathbf {L} _{k}\mathbf {L} _{k}^{*}x,y\rangle =\langle \mathbf {L} \mathbf {L} ^{*}x,y\rangle \,.$

Therefore, ${\textstyle \mathbf {A} =\mathbf {L} \mathbf {L} ^{*}}$ . Because the underlying vector space is finite-dimensional, all topologies on the space of operators are equivalent. So ${\textstyle \left(\mathbf {L} _{k}\right)_{k}}$ tends to ${\textstyle \mathbf {L} }$ in norm means ${\textstyle \left(\mathbf {L} _{k}\right)_{k}}$ tends to ${\textstyle \mathbf {L} }$ entrywise. This in turn implies that, since each ${\textstyle \mathbf {L} _{k}}$ is lower triangular with non-negative diagonal entries, ${\textstyle \mathbf {L} }$ is also.

### Proof by QR decomposition

Let ${\textstyle \mathbf {A} }$ be a positive semi-definite Hermitian matrix. Then it can be written as a product of its square root matrix, ${\textstyle \mathbf {A} =\mathbf {B} \mathbf {B} ^{*}}$ . Now QR decomposition can be applied to ${\textstyle \mathbf {B} ^{*}}$ , resulting in ${\textstyle \mathbf {B} ^{*}=\mathbf {Q} \mathbf {R} }$ , where ${\textstyle \mathbf {Q} }$ is unitary and ${\textstyle \mathbf {R} }$ is upper triangular. Inserting the decomposition into the original equality yields ${\textstyle A=\mathbf {B} \mathbf {B} ^{*}=(\mathbf {QR} )^{*}\mathbf {QR} =\mathbf {R} ^{*}\mathbf {Q} ^{*}\mathbf {QR} =\mathbf {R} ^{*}\mathbf {R} }$ . Setting ${\textstyle \mathbf {L} =\mathbf {R} ^{*}}$ completes the proof.

## Generalization

The Cholesky factorization can be generalized to (not necessarily finite) matrices with operator entries. Let ${\textstyle \{{\mathcal {H}}_{n}\}}$ be a sequence of Hilbert spaces. Consider the operator matrix

$\mathbf {A} ={\begin{bmatrix}\mathbf {A} _{11}&\mathbf {A} _{12}&\mathbf {A} _{13}&\;\\\mathbf {A} _{12}^{*}&\mathbf {A} _{22}&\mathbf {A} _{23}&\;\\\mathbf {A} _{13}^{*}&\mathbf {A} _{23}^{*}&\mathbf {A} _{33}&\;\\\;&\;&\;&\ddots \end{bmatrix}}$

acting on the direct sum

${\mathcal {H}}=\bigoplus _{n}{\mathcal {H}}_{n},$

where each

$\mathbf {A} _{ij}:{\mathcal {H}}_{j}\rightarrow {\mathcal {H}}_{i}$

is a bounded operator. If **A** is positive (semidefinite) in the sense that for all finite k and for any

$h\in \bigoplus _{n=1}^{k}{\mathcal {H}}_{k},$

there is ${\textstyle \langle h,\mathbf {A} h\rangle \geq 0}$ , then there exists a lower triangular operator matrix **L** such that **A** = **LL***. One can also take the diagonal entries of **L** to be positive.

## Implementations in programming libraries

- C programming language: the GNU Scientific Library provides several implementations of Cholesky decomposition.
- Maxima computer algebra system: function `cholesky` computes Cholesky decomposition.
- GNU Octave numerical computations system provides several functions to calculate, update, and apply a Cholesky decomposition.
- The LAPACK library provides a high performance implementation of the Cholesky decomposition that can be accessed from Fortran, C and most languages. The Cholesky decomposition is available through the `*POTRF` family of subroutines, and the LDL decomposition through the `*HETRF` family of subroutines.
- In Python, the function `cholesky` from the `numpy.linalg` module performs Cholesky decomposition. The `scipy.linalg` module contains the `ldl` function for the LDL decomposition.
- In Matlab, the `chol` function gives the Cholesky decomposition. Note that `chol` uses the upper triangular factor of the input matrix by default, i.e. it computes ${\textstyle A=R^{*}R}$ where ${\textstyle R}$ is upper triangular. A flag can be passed to use the lower triangular factor instead.
- In R, the `chol` function returns the upper triangular Cholesky factor. You can obtain the lower triangular Cholesky factor by taking the transpose of the output.
- In Julia, the `cholesky` function from the `LinearAlgebra` standard library gives the Cholesky decomposition.
- In Mathematica, the function "`CholeskyDecomposition`" can be applied to a matrix.
- In C++, multiple linear algebra libraries support this decomposition:
  - The Armadillo (C++ library) supplies the command `chol` to perform Cholesky decomposition.
  - The Eigen library supplies Cholesky factorizations for both sparse and dense matrices.
  - In the ROOT package, the `TDecompChol` class is available.

- In Analytica, the function `Decompose` gives the Cholesky decomposition.
- The Apache Commons Math library has an implementation which can be used in Java, Scala and any other JVM language.

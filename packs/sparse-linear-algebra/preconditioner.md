---
title: "Preconditioner"
source: https://en.wikipedia.org/wiki/Preconditioner
domain: sparse-linear-algebra
license: CC-BY-SA-4.0
tags: sparse matrix, iterative method solver, preconditioner, conjugate gradient method
fetched: 2026-07-02
---

# Preconditioner

In mathematics, **preconditioning** is the application of a transformation, called the **preconditioner**, that conditions a given problem into a form that is more suitable for numerical solving methods. Preconditioning is typically related to reducing a condition number of the problem. The preconditioned problem is then usually solved by an iterative method.

## Preconditioning for linear systems

In linear algebra and numerical analysis, a **preconditioner** P of a matrix A is a matrix such that $P^{-1}A$ has a smaller condition number than A . It is also common to call $T=P^{-1}$ the preconditioner, rather than P , since P itself is rarely explicitly available. In modern preconditioning, the application of $T=P^{-1}$ , i.e., multiplication of a column vector, or a block of column vectors, by $T=P^{-1}$ , is commonly performed in a matrix-free fashion, i.e., where neither P , nor $T=P^{-1}$ (and often not even A ) are explicitly available in a matrix form.

Preconditioners are useful in iterative methods to solve a linear system $Ax=b$ for x since the rate of convergence for most iterative linear solvers increases because the condition number of a matrix decreases as a result of preconditioning. Preconditioned iterative solvers typically outperform direct solvers, e.g., Gaussian elimination, for large, especially for sparse, matrices. Iterative solvers can be used as matrix-free methods, i.e. become the only choice if the coefficient matrix A is not stored explicitly, but is accessed by evaluating matrix-vector products.

### Description

Instead of solving the original linear system $Ax=b$ for x , one may consider the **right** preconditioned system $AP^{-1}(Px)=b$ and solve $AP^{-1}y=b$ for y and $Px=y$ for x .

Alternatively, one may solve the **left** preconditioned system $P^{-1}(Ax-b)=0.$

Both systems give the same solution as the original system as long as the preconditioner matrix P is nonsingular. The left preconditioning is more traditional.

The **two-sided** preconditioned system $QAP^{-1}(Px)=Qb$ may be beneficial, e.g., to preserve the matrix symmetry: if the original matrix A is real symmetric and real preconditioners Q and P satisfy $Q^{T}=P^{-1}$ then the preconditioned matrix $QAP^{-1}$ is also symmetric. The two-sided preconditioning is common for **diagonal scaling** where the preconditioners Q and P are diagonal and scaling is applied both to columns and rows of the original matrix A , e.g., in order to decrease the dynamic range of entries of the matrix.

The goal of preconditioning is reducing the condition number, e.g., of the left or right preconditioned system matrix $P^{-1}A$ or $AP^{-1}$ . Small condition numbers benefit fast convergence of iterative solvers and improve stability of the solution with respect to perturbations in the system matrix and the right-hand side, e.g., allowing for more aggressive quantization of the matrix entries using lower computer precision.

The preconditioned matrix $P^{-1}A$ or $AP^{-1}$ is rarely explicitly formed. Only the action of applying the preconditioner solve operation $P^{-1}$ to a given vector may need to be computed.

Typically there is a trade-off in the choice of P . Since the operator $P^{-1}$ must be applied at each step of the iterative linear solver, it should have a small cost (computing time) of applying the $P^{-1}$ operation. The cheapest preconditioner would therefore be $P=I$ since then $P^{-1}=I.$ Clearly, this results in the original linear system and the preconditioner does nothing. At the other extreme, the choice $P=A$ gives $P^{-1}A=AP^{-1}=I,$ which has optimal condition number of 1, requiring a single iteration for convergence; however in this case $P^{-1}=A^{-1},$ and applying the preconditioner is as difficult as solving the original system. One therefore chooses P as somewhere between these two extremes, in an attempt to achieve a minimal number of linear iterations while keeping the operator $P^{-1}$ as simple as possible. Some examples of typical preconditioning approaches are detailed below.

### Preconditioned iterative methods

Preconditioned iterative methods for $Ax-b=0$ are, in most cases, mathematically equivalent to standard iterative methods applied to the preconditioned system $P^{-1}(Ax-b)=0.$ For example, the standard Richardson iteration for solving $Ax-b=0$ is $\mathbf {x} _{n+1}=\mathbf {x} _{n}-\gamma _{n}(A\mathbf {x} _{n}-\mathbf {b} ),\ n\geq 0.$

Applied to the preconditioned system $P^{-1}(Ax-b)=0,$ it turns into a preconditioned method $\mathbf {x} _{n+1}=\mathbf {x} _{n}-\gamma _{n}P^{-1}(A\mathbf {x} _{n}-\mathbf {b} ),\ n\geq 0.$

Examples of popular preconditioned iterative methods for linear systems include the preconditioned conjugate gradient method, the biconjugate gradient method, and generalized minimal residual method. Iterative methods, which use scalar products to compute the iterative parameters, require corresponding changes in the scalar product together with substituting $P^{-1}(Ax-b)=0$ for $Ax-b=0.$

#### Matrix splitting

A stationary iterative method is determined by the matrix splitting $A=M-N$ and the iteration matrix $C=I-M^{-1}A$ . Assuming that

- the system matrix A is symmetric positive-definite,
- the splitting matrix M is symmetric positive-definite,
- the stationary iterative method is convergent, as determined by $\rho (C)<1$ ,

the condition number $\kappa (M^{-1}A)$ is bounded above by $\kappa (M^{-1}A)\leq {\frac {1+\rho (C)}{1-\rho (C)}}\,.$

### Geometric interpretation

For a symmetric positive definite matrix A the preconditioner P is typically chosen to be symmetric positive definite as well. The preconditioned operator $P^{-1}A$ is then also symmetric positive definite, but with respect to the P -based scalar product. In this case, the desired effect in applying a preconditioner is to make the quadratic form of the preconditioned operator $P^{-1}A$ with respect to the P -based scalar product to be nearly spherical.

### Variable and non-linear preconditioning

Denoting $T=P^{-1}$ , we highlight that preconditioning is practically implemented as multiplying some vector r by T , i.e., computing the product $Tr.$ In many applications, T is not given as a matrix, but rather as an operator $T(r)$ acting on the vector r . Some popular preconditioners, however, change with r and the dependence on r may not be linear. Typical examples involve using non-linear iterative methods, e.g., the conjugate gradient method, as a part of the preconditioner construction. Such preconditioners may be practically very efficient, however, their behavior is hard to predict theoretically.

### Random preconditioning

One interesting particular case of variable preconditioning is random preconditioning, e.g., multigrid preconditioning on random coarse grids. If used in gradient descent methods, random preconditioning can be viewed as an implementation of stochastic gradient descent and can lead to faster convergence, compared to fixed preconditioning, since it breaks the asymptotic "zig-zag" pattern of the gradient descent.

### Spectrally equivalent preconditioning

The most common use of preconditioning is for iterative solution of linear systems resulting from approximations of partial differential equations. The better the approximation quality, the larger the matrix size is. In such a case, the goal of optimal preconditioning is, on the one side, to make the spectral condition number of $P^{-1}A$ to be bounded from above by a constant independent of the matrix size, which is called *spectrally equivalent* preconditioning by D'yakonov. On the other hand, the cost of application of the $P^{-1}$ should ideally be proportional (also independent of the matrix size) to the cost of multiplication of A by a vector.

### Examples

#### Jacobi (or diagonal) preconditioner

The **Jacobi preconditioner** is one of the simplest forms of preconditioning, in which the preconditioner is chosen to be the diagonal of the matrix $P=\mathrm {diag} (A).$ Assuming $A_{ii}\neq 0,\forall i$ , we get $P_{ij}^{-1}={\frac {\delta _{ij}}{A_{ij}}}.$ It is efficient for diagonally dominant matrices A . It is used in analysis software for beam problems or 1-D problems (EX:- STAAD.Pro)

#### SPAI

The **Sparse Approximate Inverse** preconditioner minimises $\|AT-I\|_{F},$ where $\|\cdot \|_{F}$ is the Frobenius norm and $T=P^{-1}$ is from some suitably constrained set of sparse matrices. Under the Frobenius norm, this reduces to solving numerous independent least-squares problems (one for every column). The entries in T must be restricted to some sparsity pattern or the problem remains as difficult and time-consuming as finding the exact inverse of A . The method was introduced by M.J. Grote and T. Huckle together with an approach to selecting sparsity patterns.

#### Other preconditioners

- Incomplete Cholesky factorization
- Incomplete LU factorization
- Successive over-relaxation
  - Symmetric successive over-relaxation
- Multigrid preconditioning

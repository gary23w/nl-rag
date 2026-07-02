---
title: "Generalized minimal residual method"
source: https://en.wikipedia.org/wiki/Generalized_minimal_residual_method
domain: sparse-linear-algebra
license: CC-BY-SA-4.0
tags: sparse matrix, iterative method solver, preconditioner, conjugate gradient method
fetched: 2026-07-02
---

# Generalized minimal residual method

In mathematics, the **generalized minimal residual method (GMRES)** is an iterative method for the numerical solution of an indefinite nonsymmetric system of linear equations. The method approximates the solution by the vector in a Krylov subspace with minimal residual. The Arnoldi iteration is used to find this vector.

The GMRES method was developed by Yousef Saad and Martin H. Schultz in 1986. It is a generalization and improvement of the MINRES method due to Paige and Saunders in 1975. The MINRES method requires the matrix to be symmetric, but has the advantage that it only requires handling of three vectors. GMRES is a special case of the DIIS method developed by Peter Pulay in 1980. DIIS is applicable to non-linear systems.

## The method

Denote the Euclidean norm of any vector **v**by $\|v\|$ . Denote the (square) system of linear equations to be solved by $Ax=b.$ The matrix *A* is assumed to be invertible of size *m*-by-*m*. Furthermore, it is assumed that **b** is normalized, i.e., that $\|b\|=1$ .

The *n*-th Krylov subspace for this problem is $K_{n}=K_{n}(A,r_{0})=\operatorname {span} \,\{r_{0},Ar_{0},A^{2}r_{0},\ldots ,A^{n-1}r_{0}\}.\,$ where $r_{0}=b-Ax_{0}$ is the initial residual given an initial guess $x_{0}\neq 0$ . Clearly $r_{0}=b$ if $x_{0}=0$ .

GMRES approximates the exact solution of $Ax=b$ by the vector $x_{n}\in x_{0}+K_{n}$ that minimizes the Euclidean norm of the residual $r_{n}=b-Ax_{n}$ .

The vectors $r_{0},Ar_{0},\ldots A^{n-1}r_{0}$ might be close to linearly dependent, so instead of this basis, the Arnoldi iteration is used to find orthonormal vectors $q_{1},q_{2},\ldots ,q_{n}\,$ which form a basis for $K_{n}$ . In particular, $q_{1}=\|r_{0}\|_{2}^{-1}r_{0}$ .

Therefore, the vector $x_{n}\in x_{0}+K_{n}$ can be written as $x_{n}=x_{0}+Q_{n}y_{n}$ with $y_{n}\in \mathbb {R} ^{n}$ , where $Q_{n}$ is the *m*-by-*n* matrix formed by $q_{1},\ldots ,q_{n}$ . In other words, finding the *n*-th approximation of the solution (i.e., $x_{n}$ ) is reduced to finding the vector $y_{n}$ , which is determined via minimizing the residue as described below.

The Arnoldi process also constructs ${\tilde {H}}_{n}$ , an ( $n+1$ )-by- n upper Hessenberg matrix which satisfies $AQ_{n}=Q_{n+1}{\tilde {H}}_{n}\,$ an equality which is used to simplify the calculation of $y_{n}$ (see § Solving the least squares problem). Note that, for symmetric matrices, a symmetric tri-diagonal matrix is actually achieved, resulting in the MINRES method.

Because columns of $Q_{n}$ are orthonormal, we have ${\begin{aligned}\left\|r_{n}\right\|&=\left\|b-Ax_{n}\right\|\\&=\left\|b-A(x_{0}+Q_{n}y_{n})\right\|\\&=\left\|r_{0}-AQ_{n}y_{n}\right\|\\&=\left\|\beta q_{1}-AQ_{n}y_{n}\right\|\\&=\left\|\beta q_{1}-Q_{n+1}{\tilde {H}}_{n}y_{n}\right\|\\&=\left\|Q_{n+1}(\beta e_{1}-{\tilde {H}}_{n}y_{n})\right\|\\&=\left\|\beta e_{1}-{\tilde {H}}_{n}y_{n}\right\|\end{aligned}}$ where $e_{1}=(1,0,0,\ldots ,0)^{T}\,$ is the first vector in the standard basis of $\mathbb {R} ^{n+1}$ , and $\beta =\|r_{0}\|\,,$ $r_{0}$ being the first trial residual vector (usually b ). Hence, $x_{n}$ can be found by minimizing the Euclidean norm of the residual $r_{n}={\tilde {H}}_{n}y_{n}-\beta e_{1}.$ This is a linear least squares problem of size *n*.

This yields the GMRES method. On the n -th iteration:

1. calculate $q_{n}$ with the Arnoldi method;
2. find the $y_{n}$ which minimizes $\|r_{n}\|$ ;
3. compute $x_{n}=x_{0}+Q_{n}y_{n}$ ;
4. repeat if the residual is not yet small enough.

At every iteration, a matrix-vector product $Aq_{n}$ must be computed. This costs about $2m^{2}$ floating-point operations for general dense matrices of size m , but the cost can decrease to $O(m)$ for sparse matrices. In addition to the matrix-vector product, $O(nm)$ floating-point operations must be computed at the *n* -th iteration.

## Convergence

The *n*th iterate minimizes the residual in the Krylov subspace $K_{n}$ . Since every subspace is contained in the next subspace, the residual does not increase. After *m* iterations, where *m* is the size of the matrix *A*, the Krylov space *K**m* is the whole of **R***m* and hence the GMRES method arrives at the exact solution. However, the idea is that after a small number of iterations (relative to *m*), the vector *x**n* is already a good approximation to the exact solution.

This does not happen in general. Indeed, a theorem of Greenbaum, Pták and Strakoš states that for every nonincreasing sequence *a*1, ..., *a**m*−1, *a**m* = 0, one can find a matrix *A* such that the ‖*r**n*‖ = *a**n* for all *n*, where *r**n* is the residual defined above. In particular, it is possible to find a matrix for which the residual stays constant for *m* − 1 iterations, and only drops to zero at the last iteration.

In practice, though, GMRES often performs well. This can be proven in specific situations. If the symmetric part of *A*, that is $(A^{T}+A)/2$ , is positive definite, then $\|r_{n}\|\leq \left(1-{\frac {\lambda _{\min }^{2}(1/2(A^{T}+A))}{\lambda _{\max }(A^{T}A)}}\right)^{n/2}\|r_{0}\|,$ where $\lambda _{\mathrm {min} }(M)$ and $\lambda _{\mathrm {max} }(M)$ denote the smallest and largest eigenvalue of the matrix M , respectively.

If *A* is symmetric and positive definite, then we even have $\|r_{n}\|\leq \left({\frac {\kappa _{2}(A)^{2}-1}{\kappa _{2}(A)^{2}}}\right)^{n/2}\|r_{0}\|.$ where $\kappa _{2}(A)$ denotes the condition number of *A* in the Euclidean norm.

In the general case, where *A* is not positive definite, we have ${\frac {\|r_{n}\|}{\|b\|}}\leq \inf _{p\in P_{n}}\|p(A)\|\leq \kappa _{2}(V)\inf _{p\in P_{n}}\max _{\lambda \in \sigma (A)}|p(\lambda )|,\,$ where *P**n* denotes the set of polynomials of degree at most *n* with *p*(0) = 1, *V* is the matrix appearing in the spectral decomposition of *A*, and *σ*(*A*) is the spectrum of *A*. Roughly speaking, this says that fast convergence occurs when the eigenvalues of *A* are clustered away from the origin and *A* is not too far from normality.

All these inequalities bound only the residuals instead of the actual error, that is, the distance between the current iterate *x**n* and the exact solution.

## Extensions of the method

Like other iterative methods, GMRES is usually combined with a preconditioning method in order to speed up convergence.

The cost of the iterations grow as O(*n*2), where *n* is the iteration number. Therefore, the method is sometimes restarted after a number, say *k*, of iterations, with *x**k* as initial guess. The resulting method is called GMRES(*k*) or Restarted GMRES. For non-positive definite matrices, this method may suffer from stagnation in convergence as the restarted subspace is often close to the earlier subspace.

The shortcomings of GMRES and restarted GMRES are addressed by the recycling of Krylov subspace in the GCRO type methods such as GCROT and GCRODR. Recycling of Krylov subspaces in GMRES can also speed up convergence when sequences of linear systems need to be solved.

## Comparison with other solvers

The Arnoldi iteration reduces to the Lanczos iteration for symmetric matrices. The corresponding Krylov subspace method is the minimal residual method (MinRes) of Paige and Saunders. Unlike the unsymmetric case, the MinRes method is given by a three-term recurrence relation. It can be shown that there is no Krylov subspace method for general matrices, which is given by a short recurrence relation and yet minimizes the norms of the residuals, as GMRES does.

Another class of methods builds on the unsymmetric Lanczos iteration, in particular the BiCG method. These use a three-term recurrence relation, but they do not attain the minimum residual, and hence the residual does not decrease monotonically for these methods. Convergence is not even guaranteed.

The third class is formed by methods like CGS and BiCGSTAB. These also work with a three-term recurrence relation (hence, without optimality) and they can even terminate prematurely without achieving convergence. The idea behind these methods is to choose the generating polynomials of the iteration sequence suitably.

None of these three classes is the best for all matrices; there are always examples in which one class outperforms the other. Therefore, multiple solvers are tried in practice to see which one is the best for a given problem.

## Solving the least squares problem

One part of the GMRES method is to find the vector $y_{n}$ which minimizes $\left\|{\tilde {H}}_{n}y_{n}-\beta e_{1}\right\|.$ Note that ${\tilde {H}}_{n}$ is an (*n* + 1)-by-*n* matrix, hence it gives an over-constrained linear system of *n*+1 equations for *n* unknowns.

The minimum can be computed using a QR decomposition: find an (*n* + 1)-by-(*n* + 1) orthogonal matrix Ω*n* and an (*n* + 1)-by-*n* upper triangular matrix ${\tilde {R}}_{n}$ such that $\Omega _{n}{\tilde {H}}_{n}={\tilde {R}}_{n}.$ The triangular matrix has one more row than it has columns, so its bottom row consists of zero. Hence, it can be decomposed as ${\tilde {R}}_{n}={\begin{bmatrix}R_{n}\\0\end{bmatrix}},$ where $R_{n}$ is an *n*-by-*n* (thus square) triangular matrix.

The QR decomposition can be updated cheaply from one iteration to the next, because the Hessenberg matrices differ only by a row of zeros and a column: ${\tilde {H}}_{n+1}={\begin{bmatrix}{\tilde {H}}_{n}&h_{n+1}\\0&h_{n+2,n+1}\end{bmatrix}},$ where *h**n+1* = (*h*1,*n*+1, ..., *h**n*+1,*n*+1)T. This implies that premultiplying the Hessenberg matrix with Ω*n*, augmented with zeroes and a row with multiplicative identity, yields almost a triangular matrix: ${\begin{bmatrix}\Omega _{n}&0\\0&1\end{bmatrix}}{\tilde {H}}_{n+1}={\begin{bmatrix}R_{n}&r_{n+1}\\0&\rho \\0&\sigma \end{bmatrix}}$ This would be triangular if σ is zero. To remedy this, one needs the Givens rotation $G_{n}={\begin{bmatrix}I_{n}&0&0\\0&c_{n}&s_{n}\\0&-s_{n}&c_{n}\end{bmatrix}}$ where $c_{n}={\frac {\rho }{\sqrt {\rho ^{2}+\sigma ^{2}}}}\quad {\text{and}}\quad s_{n}={\frac {\sigma }{\sqrt {\rho ^{2}+\sigma ^{2}}}}.$ With this Givens rotation, we form $\Omega _{n+1}=G_{n}{\begin{bmatrix}\Omega _{n}&0\\0&1\end{bmatrix}}.$ Indeed, $\Omega _{n+1}{\tilde {H}}_{n+1}={\begin{bmatrix}R_{n}&r_{n+1}\\0&r_{n+1,n+1}\\0&0\end{bmatrix}}$ is a triangular matrix with ${\textstyle r_{n+1,n+1}={\sqrt {\rho ^{2}+\sigma ^{2}}}}$ .

Given the QR decomposition, the minimization problem is easily solved by noting that ${\begin{aligned}\left\|{\tilde {H}}_{n}y_{n}-\beta e_{1}\right\|&=\left\|\Omega _{n}({\tilde {H}}_{n}y_{n}-\beta e_{1})\right\|\\&=\left\|{\tilde {R}}_{n}y_{n}-\beta \Omega _{n}e_{1}\right\|.\end{aligned}}$ Denoting the vector $\beta \Omega _{n}e_{1}$ by ${\tilde {g}}_{n}={\begin{bmatrix}g_{n}\\\gamma _{n}\end{bmatrix}}$ with *g**n* ∈ **R***n* and γ*n* ∈ **R**, this is ${\begin{aligned}\left\|{\tilde {H}}_{n}y_{n}-\beta e_{1}\right\|&=\left\|{\tilde {R}}_{n}y_{n}-\beta \Omega _{n}e_{1}\right\|\\&=\left\|{\begin{bmatrix}R_{n}\\0\end{bmatrix}}y_{n}-{\begin{bmatrix}g_{n}\\\gamma _{n}\end{bmatrix}}\right\|.\end{aligned}}$ The vector *y* that minimizes this expression is given by $y_{n}=R_{n}^{-1}g_{n}.$ Again, the vectors $g_{n}$ are easy to update.

## Example code

### Regular GMRES (MATLAB / GNU Octave)

```mw
function [x, e] = gmres(A, b, x, max_iterations, threshold)
  n = length(A);
  m = max_iterations;

  % use x as the initial vector
  r = b - A * x;

  beta = norm(r);
  % Relative residual will be tracked and compared to input threshold for convergence check
  b_norm = norm(b);

  % initialize the 1D vectors
  sn = zeros(m, 1);
  cs = zeros(m, 1);
  g = zeros(m+1, 1);
  g(1) = beta;
  Q(:,1) = r / beta;
  for k = 1:m

    % Run arnoldi
    [H(1:k+1, k), Q(:, k+1)] = arnoldi(A, Q, k);
    
    % Eliminate the last element in H ith row (thus computing R in-place), and update the rotation matrix
    [H(1:k+1, k), cs(k), sn(k)] = apply_givens_rotation(H(1:k+1,k), cs, sn, k);
    
    % Apply Givens rotation to compute newly extended g
    g(k + 1) = -sn(k) * g(k);
    g(k)     =  cs(k) * g(k);

    % At minimum, ||r_k|| = |g(k+1)|
    current_relative_tol = abs(g(k + 1)) / b_norm;
    if (current_relative_tol <= threshold)
      break;
    end
  end
  % if threshold is not reached, k = m at this point (and not m+1) 
  
  % calculate the result
  y = H(1:k, 1:k) \ g(1:k);
  x = x + Q(:, 1:k) * y;
end

%----------------------------------------------------%
%                  Arnoldi Function                  %
%----------------------------------------------------%
function [h, q] = arnoldi(A, Q, k)
  q = A*Q(:,k);   % Krylov Vector
  for i = 1:k     % Modified Gram-Schmidt, keeping the Hessenberg matrix
    h(i) = q' * Q(:, i);
    q = q - h(i) * Q(:, i);
  end
  h(k + 1) = norm(q);
  q = q / h(k + 1);
end

%---------------------------------------------------------------------%
%                  Applying Givens Rotation to H col                  %
%---------------------------------------------------------------------%
function [h, cs_k, sn_k] = apply_givens_rotation(h, cs, sn, k)
  % apply for ith column
  for i = 1:k-1
    temp   =  cs(i) * h(i) + sn(i) * h(i + 1);
    h(i+1) = -sn(i) * h(i) + cs(i) * h(i + 1);
    h(i)   = temp;
  end

  % update the next sin cos values for rotation
  [cs_k, sn_k] = givens_rotation(h(k), h(k + 1));

  % eliminate H(i + 1, i)
  h(k) = cs_k * h(k) + sn_k * h(k + 1);
  h(k + 1) = 0.0;
end

%%----Calculate the Givens rotation matrix----%%
function [cs, sn] = givens_rotation(v1, v2)
%  if (v1 == 0)
%    cs = 0;
%    sn = 1;
%  else
    t = sqrt(v1^2 + v2^2);
%    cs = abs(v1) / t;
%    sn = cs * v2 / v1;
    cs = v1 / t;  % see http://www.netlib.org/eispack/comqr.f
    sn = v2 / t;
%  end
end
```

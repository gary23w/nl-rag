---
title: "Limited-memory BFGS"
source: https://en.wikipedia.org/wiki/Limited-memory_BFGS
domain: quasi-newton-bfgs
license: CC-BY-SA-4.0
tags: quasi newton method, bfgs update, limited memory bfgs, hessian approximation
fetched: 2026-07-02
---

# Limited-memory BFGS

**Limited-memory BFGS** (**L-BFGS** or **LM-BFGS**) is an optimization algorithm in the collection of quasi-Newton methods that approximates the Broyden–Fletcher–Goldfarb–Shanno algorithm (BFGS) using a limited amount of computer memory. It is a popular algorithm for parameter estimation in machine learning. The algorithm's target problem is to minimize $f(\mathbf {x} )$ over unconstrained values of the real-vector $\mathbf {x}$ where f is a differentiable scalar function.

Like the original BFGS, L-BFGS uses an estimate of the inverse Hessian matrix to steer its search through variable space, but where BFGS stores a dense $n\times n$ approximation to the inverse Hessian (*n* being the number of variables in the problem), L-BFGS stores only a few vectors that represent the approximation implicitly. Due to its resulting linear memory requirement, the L-BFGS method is particularly well suited for optimization problems with many variables. Instead of the inverse Hessian **H***k*, L-BFGS maintains a history of the past *m* updates of the position **x** and gradient ∇*f*(**x**), where generally the history size *m* can be small (often $m<10$ ). These updates are used to implicitly do operations requiring the **H***k*-vector product.

## Algorithm

The algorithm starts with an initial estimate of the optimal value, $\mathbf {x} _{0}$ , and proceeds iteratively to refine that estimate with a sequence of better estimates $\mathbf {x} _{1},\mathbf {x} _{2},\ldots$ . The derivatives of the function $g_{k}:=\nabla f(\mathbf {x} _{k})$ are used as a key driver of the algorithm to identify the direction of steepest descent, and also to form an estimate of the Hessian matrix (second derivative) of $f(\mathbf {x} )$ .

L-BFGS shares many features with other quasi-Newton algorithms, but is very different in how the matrix-vector multiplication $d_{k}=-H_{k}g_{k}$ is carried out, where $d_{k}$ is the approximate Newton's direction, $g_{k}$ is the current gradient, and $H_{k}$ is the inverse of the Hessian matrix. There are multiple published approaches using a history of updates to form this direction vector. Here, we give a common approach, the so-called "two loop recursion."

We take as given $x_{k}$ , the position at the k-th iteration, and $g_{k}\equiv \nabla f(x_{k})$ where f is the function being minimized, and all vectors are column vectors. We also assume that we have stored the last m updates of the form

$s_{k}=x_{k+1}-x_{k}$

$y_{k}=g_{k+1}-g_{k}$

.

We define $\rho _{k}={\frac {1}{y_{k}^{\top }s_{k}}}$ , and $H_{k}^{0}$ will be the 'initial' approximate of the inverse Hessian that our estimate at iteration k begins with.

The algorithm is based on the BFGS recursion for the inverse Hessian as

$H_{k+1}=(I-\rho _{k}s_{k}y_{k}^{\top })H_{k}(I-\rho _{k}y_{k}s_{k}^{\top })+\rho _{k}s_{k}s_{k}^{\top }.$

For a fixed k we define a sequence of vectors $q_{k-m},\ldots ,q_{k}$ as $q_{k}:=g_{k}$ and $q_{i}:=(I-\rho _{i}y_{i}s_{i}^{\top })q_{i+1}$ . Then a recursive algorithm for calculating $q_{i}$ from $q_{i+1}$ is to define $\alpha _{i}:=\rho _{i}s_{i}^{\top }q_{i+1}$ and $q_{i}=q_{i+1}-\alpha _{i}y_{i}$ . We also define another sequence of vectors $z_{k-m},\ldots ,z_{k}$ as $z_{i}:=H_{i}q_{i}$ . There is another recursive algorithm for calculating these vectors which is to define $z_{k-m}=H_{k}^{0}q_{k-m}$ and then recursively define $\beta _{i}:=\rho _{i}y_{i}^{\top }z_{i}$ and $z_{i+1}=z_{i}+(\alpha _{i}-\beta _{i})s_{i}$ . The value of $z_{k}$ is then our ascent direction.

Thus we can compute the descent direction as follows:

${\begin{array}{l}q=g_{k}\\{\mathtt {For}}\ i=k-1,k-2,\ldots ,k-m\\\qquad \alpha _{i}=\rho _{i}s_{i}^{\top }q\\\qquad q=q-\alpha _{i}y_{i}\\\gamma _{k}={\frac {s_{k-m}^{\top }y_{k-m}}{y_{k-m}^{\top }y_{k-m}}}\\H_{k}^{0}=\gamma _{k}I\\z=H_{k}^{0}q\\{\mathtt {For}}\ i=k-m,k-m+1,\ldots ,k-1\\\qquad \beta _{i}=\rho _{i}y_{i}^{\top }z\\\qquad z=z+s_{i}(\alpha _{i}-\beta _{i})\\z=-z\end{array}}$

This formulation gives the search direction for the minimization problem, i.e., $z=-H_{k}g_{k}$ . For maximization problems, one should thus take -z instead. Note that the initial approximate inverse Hessian $H_{k}^{0}$ is chosen as a diagonal matrix or even a multiple of the identity matrix since this is numerically efficient.

The scaling of the initial matrix $\gamma _{k}$ ensures that the search direction is well scaled and therefore the unit step length is accepted in most iterations. A Wolfe line search is used to ensure that the curvature condition is satisfied and the BFGS updating is stable. Note that some software implementations use an Armijo backtracking line search, but cannot guarantee that the curvature condition $y_{k}^{\top }s_{k}>0$ will be satisfied by the chosen step since a step length greater than 1 may be needed to satisfy this condition. Some implementations address this by skipping the BFGS update when $y_{k}^{\top }s_{k}$ is negative or too close to zero, but this approach is not generally recommended since the updates may be skipped too often to allow the Hessian approximation $H_{k}$ to capture important curvature information. Some solvers employ so called damped (L)BFGS update which modifies quantities $s_{k}$ and $y_{k}$ in order to satisfy the curvature condition.

The two-loop recursion formula is widely used by unconstrained optimizers due to its efficiency in multiplying by the inverse Hessian. However, it does not allow for the explicit formation of either the direct or inverse Hessian and is incompatible with non-box constraints. An alternative approach is the compact representation, which involves a low-rank representation for the direct and/or inverse Hessian. This represents the Hessian as a sum of a diagonal matrix and a low-rank update. Such a representation enables the use of L-BFGS in constrained settings, for example, as part of the SQP method.

## Applications

L-BFGS has been called "the algorithm of choice" for fitting log-linear (MaxEnt) models and conditional random fields with $\ell _{2}$ -regularization.

## Variants

Since BFGS (and hence L-BFGS) is designed to minimize smooth functions without constraints, the L-BFGS algorithm must be modified to handle functions that include non-differentiable components or constraints. A popular class of modifications are called active-set methods, based on the concept of the active set. The idea is that when restricted to a small neighborhood of the current iterate, the function and constraints can be simplified.

### L-BFGS-B

The **L-BFGS-B** algorithm extends L-BFGS to handle simple box constraints (a.k.a. bound constraints) on variables; that is, constraints of the form *li* ≤ *xi* ≤ *ui* where li and ui are per-variable constant lower and upper bounds, respectively (for each xi, either or both bounds may be omitted). The method works by identifying fixed and free variables at every step (using a simple gradient method), and then using the L-BFGS method on the free variables only to get higher accuracy, and then repeating the process.

### OWL-QN

**Orthant-wise limited-memory quasi-Newton** (**OWL-QN**) is an L-BFGS variant for fitting $\ell _{1}$ -regularized models, exploiting the inherent sparsity of such models. It minimizes functions of the form

$f({\vec {x}})=g({\vec {x}})+C\|{\vec {x}}\|_{1}$

where g is a differentiable convex loss function. The method is an active-set type method: at each iterate, it estimates the sign of each component of the variable, and restricts the subsequent step to have the same sign. Once the sign is fixed, the non-differentiable $\|{\vec {x}}\|_{1}$ term becomes a smooth linear term which can be handled by L-BFGS. After an L-BFGS step, the method allows some variables to change sign, and repeats the process.

### O-LBFGS

Schraudolph *et al.* present an online approximation to both BFGS and L-BFGS. Similar to stochastic gradient descent, this can be used to reduce the computational complexity by evaluating the error function and gradient on a randomly drawn subset of the overall dataset in each iteration. It has been shown that O-LBFGS has a global almost sure convergence while the online approximation of BFGS (O-BFGS) is not necessarily convergent.

## Implementation of variants

Notable open source implementations include:

- ALGLIB implements L-BFGS in C++ and C# as well as a separate box/linearly constrained version, BLEIC.
- R's `optim` general-purpose optimizer routine uses the L-BFGS-B method.
- SciPy's optimization module's minimize method also includes an option to use L-BFGS-B.
- Julia's `Optim.jl` also implements the L-BFGS and L-BFGS-B algorithm.
- Stan implements L-BFGS together with automatic differentiation as an option to solve maximum likelihood estimation and maximum a posteriori estimation problems.

Notable non open source implementations include:

- The L-BFGS-B variant also exists as ACM TOMS algorithm 778. In February 2011, some of the authors of the original L-BFGS-B code posted a major update (version 3.0).
- A reference implementation in Fortran 77 (and with a Fortran 90 interface). This version, as well as older versions, has been converted to many other languages.
- An OWL-QN C++ implementation by its designers.

## Works cited

1. *Liu, D. C.; Nocedal, J. (1989). "On the Limited Memory Method for Large Scale Optimization". *Mathematical Programming B*. **45** (3): 503–528. CiteSeerX 10.1.1.110.6443. doi:10.1007/BF01589116. S2CID 5681609.*
2. *Malouf, Robert (2002). "A comparison of algorithms for maximum entropy parameter estimation". *Proceedings of the Sixth Conference on Natural Language Learning (CoNLL-2002)*. pp. 49–55. doi:10.3115/1118853.1118871.*
3. *Andrew, Galen; Gao, Jianfeng (2007). "Scalable training of L₁-regularized log-linear models". *Proceedings of the 24th International Conference on Machine Learning*. doi:10.1145/1273496.1273501. ISBN 9781595937933. S2CID 5853259.*
4. *Matthies, H.; Strang, G. (1979). "The solution of non linear finite element equations". *International Journal for Numerical Methods in Engineering*. **14** (11): 1613–1626. Bibcode:1979IJNME..14.1613M. doi:10.1002/nme.1620141104.*
5. *Nocedal, J. (1980). "Updating Quasi-Newton Matrices with Limited Storage". *Mathematics of Computation*. **35** (151): 773–782. doi:10.1090/S0025-5718-1980-0572855-7.*
6. *Byrd, R. H.; Nocedal, J.; Schnabel, R. B. (1994). "Representations of Quasi-Newton Matrices and their use in Limited Memory Methods". *Mathematical Programming*. **63** (4): 129–156. doi:10.1007/BF01582063. S2CID 5581219.*
7. *Byrd, R. H.; Lu, P.; Nocedal, J.; Zhu, C. (1995). "A Limited Memory Algorithm for Bound Constrained Optimization". *SIAM J. Sci. Comput.* **16** (5): 1190–1208. Bibcode:1995SJSC...16.1190B. doi:10.1137/0916069. S2CID 6398414.*
8. *Zhu, C.; Byrd, Richard H.; Lu, Peihuang; Nocedal, Jorge (1997). "L-BFGS-B: Algorithm 778: L-BFGS-B, FORTRAN routines for large scale bound constrained optimization". *ACM Transactions on Mathematical Software*. **23** (4): 550–560. doi:10.1145/279232.279236. S2CID 207228122.*
9. *Schraudolph, N.; Yu, J.; Günter, S. (2007). *A stochastic quasi-Newton method for online convex optimization*. AISTATS.*
10. *Mokhtari, A.; Ribeiro, A. (2015). "Global convergence of online limited memory BFGS" (PDF). *Journal of Machine Learning Research*. **16**: 3151–3181. arXiv:1409.2045.*
11. *Mokhtari, A.; Ribeiro, A. (2014). "RES: Regularized Stochastic BFGS Algorithm". *IEEE Transactions on Signal Processing*. **62** (23): 6089–6104. arXiv:1401.7625. Bibcode:2014ITSP...62.6089M. CiteSeerX 10.1.1.756.3003. doi:10.1109/TSP.2014.2357775. S2CID 15214938.*
12. *"Official Documentation of Optim.jl". *Documentation Optim.jl*.*
13. *"TOMS Home". *toms.acm.org*.*
14. *Morales, J. L.; Nocedal, J. (2011). "Remark on "algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound constrained optimization"". *ACM Transactions on Mathematical Software*. **38**: 1–4. doi:10.1145/2049662.2049669. S2CID 16742561.*
15. *"L-BFGS-B Nonlinear Optimization Code". *users.iems.northwestern.edu*.*
16. *"Orthant-Wise Limited-memory Quasi-Newton Optimizer for L1-regularized Objectives". *Microsoft Download Center*.*

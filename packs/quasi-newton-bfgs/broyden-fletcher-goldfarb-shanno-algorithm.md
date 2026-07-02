---
title: "Broyden–Fletcher–Goldfarb–Shanno algorithm"
source: https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm
domain: quasi-newton-bfgs
license: CC-BY-SA-4.0
tags: quasi newton method, bfgs update, limited memory bfgs, hessian approximation
fetched: 2026-07-02
---

# Broyden–Fletcher–Goldfarb–Shanno algorithm

In numerical optimization, the **Broyden–Fletcher–Goldfarb–Shanno** (**BFGS**) **algorithm** is an iterative method for solving unconstrained nonlinear optimization problems. Like the related Davidon–Fletcher–Powell method, BFGS determines the descent direction by preconditioning the gradient with curvature information. It does so by gradually improving an approximation to the Hessian matrix of the loss function, obtained only from gradient evaluations (or approximate gradient evaluations) via a generalized secant method.

Since the updates of the BFGS curvature matrix do not require matrix inversion, its computational complexity is only ${\mathcal {O}}(n^{2})$ , compared to ${\mathcal {O}}(n^{3})$ in Newton's method. Also in common use is L-BFGS, which is a limited-memory version of BFGS that is particularly suited to problems with very large numbers of variables (e.g., >1000). The BFGS-B variant handles simple box constraints. The BFGS matrix also admits a compact representation, which makes it better suited for large constrained problems.

The algorithm is named after Charles George Broyden, Roger Fletcher, Donald Goldfarb and David Shanno. It is an instance of a more general algorithm by John Greenstadt.

## Rationale

The optimization problem is to minimize $f(\mathbf {x} )$ , where $\mathbf {x}$ is a vector in $\mathbb {R} ^{n}$ , and f is a differentiable scalar function. There are no constraints on the values that $\mathbf {x}$ can take.

The algorithm begins at an initial estimate $\mathbf {x} _{0}$ for the optimal value and proceeds iteratively to get a better estimate at each stage.

The search direction **p***k* at stage *k* is given by the solution of the analogue of the Newton equation:

$B_{k}\mathbf {p} _{k}=-\nabla f(\mathbf {x} _{k}),$

where $B_{k}$ is an approximation to the Hessian matrix at $\mathbf {x} _{k}$ , which is updated iteratively at each stage, and $\nabla f(\mathbf {x} _{k})$ is the gradient of the function evaluated at **x***k*. A line search in the direction **p***k* is then used to find the next point **x***k*+1 by minimizing $f(\mathbf {x} _{k}+\gamma \mathbf {p} _{k})$ over the scalar $\gamma >0.$

The quasi-Newton condition imposed on the update of $B_{k}$ is

$B_{k+1}(\mathbf {x} _{k+1}-\mathbf {x} _{k})=\nabla f(\mathbf {x} _{k+1})-\nabla f(\mathbf {x} _{k}).$

Let $\mathbf {y} _{k}=\nabla f(\mathbf {x} _{k+1})-\nabla f(\mathbf {x} _{k})$ and $\mathbf {s} _{k}=\mathbf {x} _{k+1}-\mathbf {x} _{k}$ , then $B_{k+1}$ satisfies

$B_{k+1}\mathbf {s} _{k}=\mathbf {y} _{k}$

,

which is the secant equation.

The curvature condition $\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}>0$ should be satisfied for $B_{k+1}$ to be positive definite, which can be verified by pre-multiplying the secant equation with $\mathbf {s} _{k}^{\mathsf {T}}$ . If the function is not strongly convex, then the condition has to be enforced explicitly e.g. by finding a point **x***k*+1 satisfying the Wolfe conditions, which entail the curvature condition, using line search.

Instead of requiring the full Hessian matrix at the point $\mathbf {x} _{k+1}$ to be computed as $B_{k+1}$ , the approximate Hessian at stage *k* is updated by the addition of two matrices:

$B_{k+1}=B_{k}+U_{k}+V_{k}.$

Both $U_{k}$ and $V_{k}$ are symmetric rank-one matrices, but their sum is a rank-two update matrix. BFGS and DFP updating matrix both differ from its predecessor by a rank-two matrix. Another simpler rank-one method is known as symmetric rank-one method, which does not guarantee the positive definiteness. In order to maintain the symmetry and positive definiteness of $B_{k+1}$ , the update form can be chosen as $B_{k+1}=B_{k}+\alpha \mathbf {u} \mathbf {u} ^{\mathsf {T}}+\beta \mathbf {v} \mathbf {v} ^{\mathsf {T}}$ . Imposing the secant condition, $B_{k+1}\mathbf {s} _{k}=\mathbf {y} _{k}$ . Choosing $\mathbf {u} =\mathbf {y} _{k}$ and $\mathbf {v} =B_{k}\mathbf {s} _{k}$ , we can obtain:

$\alpha ={\frac {1}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}},$

$\beta =-{\frac {1}{\mathbf {s} _{k}^{\mathsf {T}}B_{k}\mathbf {s} _{k}}}.$

Finally, we substitute $\alpha$ and $\beta$ into $B_{k+1}=B_{k}+\alpha \mathbf {u} \mathbf {u} ^{\mathsf {T}}+\beta \mathbf {v} \mathbf {v} ^{\mathsf {T}}$ and get the update equation of $B_{k+1}$ :

$B_{k+1}=B_{k}+{\frac {\mathbf {y} _{k}\mathbf {y} _{k}^{\mathsf {T}}}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}}-{\frac {B_{k}\mathbf {s} _{k}\mathbf {s} _{k}^{\mathsf {T}}B_{k}^{\mathsf {T}}}{\mathbf {s} _{k}^{\mathsf {T}}B_{k}\mathbf {s} _{k}}}.$

## Algorithm

Consider the following unconstrained optimization problem ${\begin{aligned}{\underset {\mathbf {x} \in \mathbb {R} ^{n}}{\text{minimize}}}\quad &f(\mathbf {x} ),\end{aligned}}$ where $f:\mathbb {R} ^{n}\to \mathbb {R}$ is a nonlinear, twice-differentiable objective function.

From an initial guess $\mathbf {x} _{0}\in \mathbb {R} ^{n}$ and an initial guess of the Hessian matrix $B_{0}\in \mathbb {R} ^{n\times n}$ the following steps are repeated as $\mathbf {x} _{k}$ converges to the solution:

1. Obtain a direction $\mathbf {p} _{k}$ by solving $B_{k}\mathbf {p} _{k}=-\nabla f(\mathbf {x} _{k})$ .
2. Perform a one-dimensional optimization (line search) to find an acceptable stepsize $\alpha _{k}$ in the direction found in the first step. If an exact line search is performed, then $\alpha _{k}=\arg \min _{\alpha }f(\mathbf {x} _{k}+\alpha \mathbf {p} _{k})$ . In practice, an inexact line search usually suffices, with an acceptable $\alpha _{k}$ satisfying Wolfe conditions.
3. Set $\mathbf {s} _{k}=\alpha _{k}\mathbf {p} _{k}$ and update $\mathbf {x} _{k+1}=\mathbf {x} _{k}+\mathbf {s} _{k}$ .
4. $\mathbf {y} _{k}={\nabla f(\mathbf {x} _{k+1})-\nabla f(\mathbf {x} _{k})}$ .
5. $B_{k+1}=B_{k}+{\frac {\mathbf {y} _{k}\mathbf {y} _{k}^{\mathsf {T}}}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}}-{\frac {B_{k}\mathbf {s} _{k}\mathbf {s} _{k}^{\mathsf {T}}B_{k}^{\mathsf {T}}}{\mathbf {s} _{k}^{\mathsf {T}}B_{k}\mathbf {s} _{k}}}$ .

Convergence can be determined by observing the norm of the gradient; given some $\epsilon >0$ , one may stop the algorithm when $||\nabla f(\mathbf {x} _{k})||\leq \epsilon .$ If $B_{0}$ is initialized with $B_{0}=I$ , the first step will be equivalent to a gradient descent, but further steps are more and more refined by $B_{k}$ , the approximation to the Hessian.

The first step of the algorithm is carried out using the inverse of the matrix $B_{k}$ , which can be obtained efficiently by applying the Sherman–Morrison formula to the step 5 of the algorithm, giving

$B_{k+1}^{-1}=\left(I-{\frac {\mathbf {s} _{k}\mathbf {y} _{k}^{\mathsf {T}}}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}}\right)B_{k}^{-1}\left(I-{\frac {\mathbf {y} _{k}\mathbf {s} _{k}^{\mathsf {T}}}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}}\right)+{\frac {\mathbf {s} _{k}\mathbf {s} _{k}^{\mathsf {T}}}{\mathbf {y} _{k}^{\mathsf {T}}\mathbf {s} _{k}}}.$

This can be computed efficiently without temporary matrices, recognizing that $B_{k}^{-1}$ is symmetric, and that $\mathbf {y} _{k}^{\mathsf {T}}B_{k}^{-1}\mathbf {y} _{k}$ and $\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}$ are scalars, using an expansion such as

$B_{k+1}^{-1}=B_{k}^{-1}+{\frac {(\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}+\mathbf {y} _{k}^{\mathsf {T}}B_{k}^{-1}\mathbf {y} _{k})(\mathbf {s} _{k}\mathbf {s} _{k}^{\mathsf {T}})}{(\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k})^{2}}}-{\frac {B_{k}^{-1}\mathbf {y} _{k}\mathbf {s} _{k}^{\mathsf {T}}+\mathbf {s} _{k}\mathbf {y} _{k}^{\mathsf {T}}B_{k}^{-1}}{\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}}}.$

Therefore, in order to avoid any matrix inversion, the **inverse** of the Hessian can be approximated instead of the Hessian itself: $H_{k}{\overset {\operatorname {def} }{=}}B_{k}^{-1}.$

From an initial guess $\mathbf {x} _{0}$ and an approximate **inverted** Hessian matrix $H_{0}$ the following steps are repeated as $\mathbf {x} _{k}$ converges to the solution:

1. Obtain a direction $\mathbf {p} _{k}$ by solving $\mathbf {p} _{k}=-H_{k}\nabla f(\mathbf {x} _{k})$ .
2. Perform a one-dimensional optimization (line search) to find an acceptable stepsize $\alpha _{k}$ in the direction found in the first step. If an exact line search is performed, then $\alpha _{k}=\arg \min _{\alpha }f(\mathbf {x} _{k}+\alpha \mathbf {p} _{k})$ . In practice, an inexact line search usually suffices, with an acceptable $\alpha _{k}$ satisfying Wolfe conditions.
3. Set $\mathbf {s} _{k}=\alpha _{k}\mathbf {p} _{k}$ and update $\mathbf {x} _{k+1}=\mathbf {x} _{k}+\mathbf {s} _{k}$ .
4. $\mathbf {y} _{k}={\nabla f(\mathbf {x} _{k+1})-\nabla f(\mathbf {x} _{k})}$ .
5. $H_{k+1}=H_{k}+{\frac {(\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}+\mathbf {y} _{k}^{\mathsf {T}}H_{k}\mathbf {y} _{k})(\mathbf {s} _{k}\mathbf {s} _{k}^{\mathsf {T}})}{(\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k})^{2}}}-{\frac {H_{k}\mathbf {y} _{k}\mathbf {s} _{k}^{\mathsf {T}}+\mathbf {s} _{k}\mathbf {y} _{k}^{\mathsf {T}}H_{k}}{\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}}}$ .

In statistical estimation problems (such as maximum likelihood or Bayesian inference), credible intervals or confidence intervals for the solution can be estimated from the inverse of the final Hessian matrix . However, these quantities are technically defined by the true Hessian matrix, and the BFGS approximation may not converge to the true Hessian matrix.

## Further developments

The BFGS update formula heavily relies on the curvature $\mathbf {s} _{k}^{\mathsf {T}}\mathbf {y} _{k}$ being strictly positive and bounded away from zero. This condition is satisfied when we perform a line search with Wolfe conditions on a convex target. However, some real-life applications (like Sequential Quadratic Programming methods) routinely produce negative or nearly-zero curvatures. This can occur when optimizing a nonconvex target or when employing a trust-region approach instead of a line search. It is also possible to produce spurious values due to noise in the target.

In such cases, one of the so-called damped BFGS updates can be used (see ) which modify $\mathbf {s} _{k}$ and/or $\mathbf {y} _{k}$ in order to obtain a more robust update.

## Notable implementations

Notable open source implementations are:

- ALGLIB implements BFGS and its limited-memory version in C++ and C#
- GNU Octave uses a form of BFGS in its `fsolve` function, with trust region extensions.
- The GSL implements BFGS as gsl_multimin_fdfminimizer_vector_bfgs2.
- In R, the BFGS algorithm (and the L-BFGS-B version that allows box constraints) is implemented as an option of the base function optim().
- In SciPy, the scipy.optimize.fmin_bfgs function implements BFGS. It is also possible to run BFGS using any of the L-BFGS algorithms by setting the parameter L to a very large number. It is also one of the default methods used when running scipy.optimize.minimize with no constraints.
- In Julia, the Optim.jl package implements BFGS and L-BFGS as a solver option to the optimize() function (among other options).
- Stan implements BFGS together with automatic differentiation as an option to solve maximum likelihood estimation and maximum a posteriori estimation problems.

Notable proprietary implementations include:

- The large scale nonlinear optimization software Artelys Knitro implements, among others, both BFGS and L-BFGS algorithms.
- In the MATLAB Optimization Toolbox, the fminunc function uses BFGS with cubic line search when the problem size is set to "medium scale."
- Mathematica includes BFGS.
- LS-DYNA also uses BFGS to solve implicit Problems.

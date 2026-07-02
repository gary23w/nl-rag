---
title: "Anderson acceleration"
source: https://en.wikipedia.org/wiki/Anderson_acceleration
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Anderson acceleration

In mathematics, **Anderson acceleration**, also called **Anderson mixing**, is a method for the acceleration of the convergence rate of fixed-point iterations. Introduced by Donald G. Anderson, this technique can be used to find the solution to fixed point equations $f(x)=x$ often arising in the field of computational science.

## Definition

Given a function $f:\mathbb {R} ^{n}\to \mathbb {R} ^{n}$ , consider the problem of finding a fixed point of f , which is a solution to the equation $f(x)=x$ . A classical approach to the problem is to employ a fixed-point iteration scheme; that is, given an initial guess $x_{0}$ for the solution, to compute the sequence $x_{k+1}=f(x_{k})$ until some convergence criterion is met. However, the convergence of such a scheme is not guaranteed in general; moreover, the rate of convergence is usually linear, which can become too slow if the evaluation of the function f is computationally expensive. Anderson acceleration is a method to accelerate the convergence of the fixed-point sequence.

Define the residual $g(x)=f(x)-x$ , and denote $f_{k}=f(x_{k})$ and $g_{k}=g(x_{k})$ (where $x_{k}$ corresponds to the sequence of iterates from the previous paragraph). Given an initial guess $x_{0}$ and an integer parameter $m\geq 1$ , the method can be formulated as follows:

$x_{1}=f(x_{0})$

$\forall k=1,2,\dots$

$m_{k}=\min\{m,k\}$

$G_{k}={\begin{bmatrix}g_{k-m_{k}}&\dots &g_{k}\end{bmatrix}}$

$\alpha _{k}=\operatorname {argmin} _{\alpha \in A_{k}}\|G_{k}\alpha \|_{2},\quad {\text{where}}\;A_{k}=\{\alpha =(\alpha _{0},\dots ,\alpha _{m_{k}})\in \mathbb {R} ^{m_{k}+1}:\sum _{i=0}^{m_{k}}\alpha _{i}=1\}$

$x_{k+1}=\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}f_{k-m_{k}+i}$

where the matrix–vector multiplication $G_{k}\alpha =\sum _{i=0}^{m_{k}}(\alpha )_{i}g_{k-m_{k}+i}$ , and $(\alpha )_{i}$ is the i th element of $\alpha$ . Conventional stopping criteria can be used to end the iterations of the method. For example, iterations can be stopped when $\|x_{k+1}-x_{k}\|$ falls under a prescribed tolerance, or when the residual $g(x_{k})$ falls under a prescribed tolerance.

With respect to the standard fixed-point iteration, the method has been found to converge faster and be more robust, and in some cases avoid the divergence of the fixed-point sequence.

### Derivation

For the solution $x^{*}$ , we know that $f(x^{*})=x^{*}$ , which is equivalent to saying that $g(x^{*})={\vec {0}}$ . We can therefore rephrase the problem as an optimization problem where we want to minimize $\|g(x)\|_{2}$ .

Instead of going directly from $x_{k}$ to $x_{k+1}$ by choosing $x_{k+1}=f(x_{k})$ as in fixed-point iteration, let's consider an intermediate point $x'_{k+1}$ that we choose to be the linear combination $x'_{k+1}=X_{k}\alpha _{k}$ , where the coefficient vector $\alpha _{k}\in A_{k}$ , and $X_{k}={\begin{bmatrix}x_{k-m_{k}}&\dots &x_{k}\end{bmatrix}}$ is the matrix containing the last $m_{k}+1$ points, and choose $x'_{k+1}$ such that it minimizes $\|g(x'_{k+1})\|_{2}$ . Since the elements in $\alpha _{k}$ sum to one, we can make the first order approximation

${\begin{aligned}g(X_{k}\alpha _{k})&=g\!\left(\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}x_{k-m_{k}+i}\right)\\&\approx \sum _{i=0}^{m_{k}}(\alpha _{k})_{i}g(x_{k-m_{k}+i})\\&=\;G_{k}\alpha _{k}\end{aligned}}$

and our problem becomes to find the $\alpha$ that minimizes $\|G_{k}\alpha \|_{2}$ . After having found $\alpha _{k}$ , we could in principle calculate $x'_{k+1}$ .

However, since f is designed to bring a point closer to $x^{*}$ , $f(x'_{k+1})$ is probably closer to $x^{*}$ than $x'_{k+1}$ is, so it makes sense to choose $x_{k+1}=f(x'_{k+1})$ rather than $x_{k+1}=x'_{k+1}$ . Furthermore, since the elements in $\alpha _{k}$ sum to one, we can make the first order approximation

${\begin{aligned}f(x'_{k+1})&=f\left(\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}x_{k-m_{k}+i}\right)\\&\approx \sum _{i=0}^{m_{k}}(\alpha _{k})_{i}f(x_{k-m_{k}+i})\\&=\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}f_{k-m_{k}+i}\,.\end{aligned}}$

We therefore choose

$x_{k+1}=\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}f_{k-m_{k}+i}$ .

### Solution of the minimization problem

At each iteration of the algorithm, the constrained optimization problem $\operatorname {argmin} \|G_{k}\alpha \|_{2}$ , subject to $\alpha \in A_{k}$ needs to be solved. The problem can be recast in several equivalent formulations, yielding different solution methods which may result in a more convenient implementation:

- defining the matrices ${\mathcal {G}}_{k}={\begin{bmatrix}g_{k-m_{k}+1}-g_{k-m_{k}}&\dots &g_{k}-g_{k-1}\end{bmatrix}}$ and ${\mathcal {X}}_{k}={\begin{bmatrix}x_{k-m_{k}+1}-x_{k-m_{k}}&\dots &x_{k}-x_{k-1}\end{bmatrix}}$ , solve $\gamma _{k}=\operatorname {argmin} _{\gamma \in \mathbb {R} ^{m_{k}}}\|g_{k}-{\mathcal {G}}_{k}\gamma \|_{2}$ , and set $x_{k+1}=x_{k}+g_{k}-({\mathcal {X}}_{k}+{\mathcal {G}}_{k})\gamma _{k}$ ;
- solve $\theta _{k}=\{(\theta _{k})_{i}\}_{i=1}^{m_{k}}=\operatorname {argmin} _{\theta \in \mathbb {R} ^{m_{k}}}\left\|g_{k}+\sum _{i=1}^{m_{k}}\theta _{i}(g_{k-i}-g_{k})\right\|_{2}$ , then set $x_{k+1}=x_{k}+g_{k}+\sum _{j=1}^{m_{k}}(\theta _{k})_{j}(x_{k-j}-x_{k}+g_{k-j}-g_{k})$ .

For both choices, the optimization problem is in the form of an unconstrained linear least-squares problem, which can be solved by standard methods including QR decomposition and singular value decomposition, possibly including regularization techniques to deal with rank deficiencies and conditioning issues in the optimization problem. Solving the least-squares problem by solving the normal equations is generally not advisable due to potential numerical instabilities and generally high computational cost.

Stagnation in the method (i.e. subsequent iterations with the same value, $x_{k+1}=x_{k}$ ) causes the method to break down, due to the singularity of the least-squares problem. Similarly, near-stagnation ( $x_{k+1}\approx x_{k}$ ) results in bad conditioning of the least squares problem. Moreover, the choice of the parameter m might be relevant in determining the conditioning of the least-squares problem, as discussed below.

### Relaxation

The algorithm can be modified introducing a variable relaxation parameter (or mixing parameter) $\beta _{k}>0$ . At each step, compute the new iterate as $x_{k+1}=(1-\beta _{k})\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}x_{k-m_{k}+i}+\beta _{k}\sum _{i=0}^{m_{k}}(\alpha _{k})_{i}f(x_{k-m_{k}+i})\;.$ The choice of $\beta _{k}$ is crucial to the convergence properties of the method; in principle, $\beta _{k}$ might vary at each iteration, although it is often chosen to be constant.

### Choice of m

The parameter m determines how much information from previous iterations is used to compute the new iteration $x_{k+1}$ . On the one hand, if m is chosen to be too small, too little information is used and convergence may be undesirably slow. On the other hand, if m is too large, information from old iterations may be retained for too many subsequent iterations, so that again convergence may be slow. Moreover, the choice of m affects the size of the optimization problem. A too large value of m may worsen the conditioning of the least squares problem and the cost of its solution. In general, the particular problem to be solved determines the best choice of the m parameter.

### Choice of mk

With respect to the algorithm described above, the choice of $m_{k}$ at each iteration can be modified. One possibility is to choose $m_{k}=k$ for each iteration k (sometimes referred to as Anderson acceleration without truncation). This way, every new iteration $x_{k+1}$ is computed using all the previously computed iterations. A more sophisticated technique is based on choosing $m_{k}$ so as to maintain a small enough conditioning for the least-squares problem.

## Relations to other classes of methods

Newton's method can be applied to the solution of $f(x)-x=0$ to compute a fixed point of $f(x)$ with quadratic convergence. However, such method requires the evaluation of the exact derivative of $f(x)$ , which can be very costly. Approximating the derivative by means of finite differences is a possible alternative, but it requires multiple evaluations of $f(x)$ at each iteration, which again can become very costly. Anderson acceleration requires only one evaluation of the function $f(x)$ per iteration, and no evaluation of its derivative. On the other hand, the convergence of an Anderson-accelerated fixed point sequence is still linear in general.

Several authors have pointed out similarities between the Anderson acceleration scheme and other methods for the solution of non-linear equations. In particular:

- Eyert and Fang and Saad interpreted the algorithm within the class of quasi-Newton and multisecant methods, that generalize the well known secant method, for the solution of the non-linear equation $g(x)=0$ ; they also showed how the scheme can be seen as a method in the Broyden class;
- Walker and Ni showed that the Anderson acceleration scheme is equivalent to the GMRES method in the case of linear problems (i.e. the problem of finding a solution to $A\mathbf {x} =\mathbf {x}$ for some square matrix A ), and can thus be seen as a generalization of GMRES to the non-linear case; a similar result was found by Washio and Oosterlee.

Moreover, several equivalent or nearly equivalent methods have been independently developed by other authors, although most often in the context of some specific application of interest rather than as a general method for fixed point equations.

## Example MATLAB implementation

The following is an example implementation in MATLAB language of the Anderson acceleration scheme for finding the fixed-point of the function $f(x)=\sin(x)+\arctan(x)$ . Notice that:

- the optimization problem was solved in the form $\gamma _{k}=\operatorname {argmin} _{\gamma \in \mathbb {R} ^{m_{k}}}\|g_{k}-{\mathcal {G}}_{k}\gamma \|_{2}$ using QR decomposition;
- the computation of the QR decomposition is sub-optimal: indeed, at each iteration a single column is added to the matrix ${\mathcal {G}}_{k}$ , and possibly a single column is removed; this fact can be exploited to efficiently update the QR decomposition with less computational effort;
- the algorithm can be made more memory-efficient by storing only the latest few iterations and residuals, if the whole vector of iterations $x_{k}$ is not needed;
- the code is straightforwardly generalized to the case of a vector-valued $f(x)$ .

```mw
f = @(x) sin(x) + atan(x); % Function whose fixed point is to be computed.
x0 = 1; % Initial guess.

k_max = 100; % Maximum number of iterations.
tol_res = 1e-6; % Tolerance on the residual.
m = 3; % Parameter m.

x = [x0, f(x0)]; % Vector of iterates x.
g = f(x) - x; % Vector of residuals.

G_k = g(2) - g(1); % Matrix of increments in residuals.
X_k = x(2) - x(1); % Matrix of increments in x.

k = 2;
while k < k_max && abs(g(k)) > tol_res
    m_k = min(k, m);
 
    % Solve the optimization problem by QR decomposition.
    [Q, R] = qr(G_k);
    gamma_k = R \ (Q' * g(k));
 
    % Compute new iterate and new residual.
    x(k + 1) = x(k) + g(k) - (X_k + G_k) * gamma_k;
    g(k + 1) = f(x(k + 1)) - x(k + 1);
 
    % Update increment matrices with new elements.
    X_k = [X_k, x(k + 1) - x(k)];
    G_k = [G_k, g(k + 1) - g(k)];
 
    n = size(X_k, 2);
    if n > m_k
        X_k = X_k(:, n - m_k + 1:end);
        G_k = G_k(:, n - m_k + 1:end);
    end
 
    k = k + 1;
end

% Prints result: Computed fixed point 2.013444 after 9 iterations
fprintf("Computed fixed point %f after %d iterations\n", x(end), k);
```

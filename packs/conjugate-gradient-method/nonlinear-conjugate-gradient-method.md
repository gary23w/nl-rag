---
title: "Nonlinear conjugate gradient method"
source: https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method
domain: conjugate-gradient-method
license: CC-BY-SA-4.0
tags: conjugate gradient method, nonlinear conjugate gradient, line search, steepest descent
fetched: 2026-07-02
---

# Nonlinear conjugate gradient method

In numerical optimization, the **nonlinear conjugate gradient method** generalizes the conjugate gradient method to nonlinear optimization. For a quadratic function $\displaystyle f(x)$

$\displaystyle f(x)=\|Ax-b\|^{2},$

the minimum of f is obtained when the gradient is 0:

$\nabla _{x}f=2A^{T}(Ax-b)=0$

.

Whereas linear conjugate gradient seeks a solution to the linear equation $\displaystyle A^{T}Ax=A^{T}b$ , the nonlinear conjugate gradient method is generally used to find the local minimum of a nonlinear function using its gradient $\nabla _{x}f$ alone. It works when the function is approximately quadratic near the minimum, which is the case when the function is twice differentiable at the minimum and the second derivative is non-singular there.

Given a function $\displaystyle f(x)$ of N variables to minimize, its gradient $\nabla _{x}f$ indicates the direction of maximum increase. One simply starts in the opposite (steepest descent) direction:

$\Delta x_{0}=-\nabla _{x}f(x_{0})$

with an adjustable step length $\displaystyle \alpha$ and performs a line search in this direction until it reaches the minimum of $\displaystyle f$ :

$\displaystyle \alpha _{0}:=\arg \min _{\alpha }f(x_{0}+\alpha \Delta x_{0})$

,

$\displaystyle x_{1}=x_{0}+\alpha _{0}\Delta x_{0}$

After this first iteration in the steepest direction $\displaystyle \Delta x_{0}$ , the following steps constitute one iteration of moving along a subsequent conjugate direction $\displaystyle s_{n}$ , where $\displaystyle s_{0}=\Delta x_{0}$ :

1. Calculate the steepest direction: $\Delta x_{n}=-\nabla _{x}f(x_{n})$ ,
2. Compute $\displaystyle \beta _{n}$ according to one of the formulas below,
3. Update the conjugate direction: $\displaystyle s_{n}=\Delta x_{n}+\beta _{n}s_{n-1}$
4. Perform a line search: optimize $\displaystyle \alpha _{n}=\arg \min _{\alpha }f(x_{n}+\alpha s_{n})$ ,
5. Update the position: $\displaystyle x_{n+1}=x_{n}+\alpha _{n}s_{n}$ ,

With a pure quadratic function the minimum is reached within *N* iterations (excepting roundoff error), but a non-quadratic function will make slower progress. Subsequent search directions lose conjugacy requiring the search direction to be reset to the steepest descent direction at least every *N* iterations, or sooner if progress stops. However, resetting every iteration turns the method into steepest descent. The algorithm stops when it finds the minimum, determined when no progress is made after a direction reset (i.e. in the steepest descent direction), or when some tolerance criterion is reached.

Within a linear approximation, the parameters $\displaystyle \alpha$ and $\displaystyle \beta$ are the same as in the linear conjugate gradient method but have been obtained with line searches. The conjugate gradient method can follow narrow (ill-conditioned) valleys, where the steepest descent method slows down and follows a criss-cross pattern.

Four of the best known formulas for $\displaystyle \beta _{n}$ are named after their developers:

- Fletcher–Reeves:

$\beta _{n}^{FR}={\frac {\Delta x_{n}^{T}\Delta x_{n}}{\Delta x_{n-1}^{T}\Delta x_{n-1}}}.$

- Polak–Ribière:

$\beta _{n}^{PR}={\frac {\Delta x_{n}^{T}(\Delta x_{n}-\Delta x_{n-1})}{\Delta x_{n-1}^{T}\Delta x_{n-1}}}.$

- Hestenes–Stiefel:

$\beta _{n}^{HS}={\frac {\Delta x_{n}^{T}(\Delta x_{n}-\Delta x_{n-1})}{-s_{n-1}^{T}(\Delta x_{n}-\Delta x_{n-1})}}.$

- Dai–Yuan:

$\beta _{n}^{DY}={\frac {\Delta x_{n}^{T}\Delta x_{n}}{-s_{n-1}^{T}(\Delta x_{n}-\Delta x_{n-1})}}.$

.

These formulas are equivalent for a quadratic function, but for nonlinear optimization the preferred formula is a matter of heuristics or taste. A popular choice is $\displaystyle \beta =\max\{0,\beta ^{PR}\}$ , which provides a direction reset automatically.

Algorithms based on Newton's method potentially converge much faster. There, both step direction and length are computed from the gradient as the solution of a linear system of equations, with the coefficient matrix being the exact Hessian matrix (for Newton's method proper) or an estimate thereof (in the quasi-Newton methods, where the observed change in the gradient during the iterations is used to update the Hessian estimate). For high-dimensional problems, the exact computation of the Hessian is usually prohibitively expensive, and even its storage can be problematic, requiring $O(N^{2})$ memory (but see the limited-memory L-BFGS quasi-Newton method).

The conjugate gradient method can also be derived using optimal control theory. In this accelerated optimization theory, the conjugate gradient method falls out as a nonlinear optimal feedback controller,

$u=k(x,{\dot {x}}):=-\gamma _{a}\nabla _{x}f(x)-\gamma _{b}{\dot {x}}$

for the double integrator system,

${\ddot {x}}=u$

The quantities $\gamma _{a}>0$ and $\gamma _{b}>0$ are variable feedback gains.

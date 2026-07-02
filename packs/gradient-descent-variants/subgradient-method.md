---
title: "Subgradient method"
source: https://en.wikipedia.org/wiki/Subgradient_method
domain: gradient-descent-variants
license: CC-BY-SA-4.0
tags: gradient descent variants, momentum method, nesterov acceleration, adagrad rmsprop
fetched: 2026-07-02
---

# Subgradient method

**Subgradient methods** are convex optimization methods which use subderivatives. Originally developed by Naum Z. Shor and others in the 1960s and 1970s, subgradient methods are convergent when applied even to a non-differentiable objective function. When the objective function is differentiable, subgradient methods for unconstrained problems use the same search direction as the method of gradient descent.

Subgradient methods are slower than Newton's method when applied to minimize twice continuously differentiable convex functions. However, Newton's method fails to converge on problems that have non-differentiable kinks.

In recent years, some interior-point methods have been suggested for convex minimization problems, but subgradient projection methods and related bundle methods of descent remain competitive. For convex minimization problems with very large number of dimensions, subgradient-projection methods are suitable, because they require little storage.

Subgradient projection methods are often applied to large-scale problems with decomposition techniques. Such decomposition methods often allow a simple distributed method for a problem.

## Classical subgradient rules

Let $f:\mathbb {R} ^{n}\to \mathbb {R}$ be a convex function with domain $\mathbb {R} ^{n}.$ A classical subgradient method iterates $x^{(k+1)}=x^{(k)}-\alpha _{k}g^{(k)}\$ where $g^{(k)}$ denotes *any* subgradient of $f\$ at $x^{(k)},\$ and $x^{(k)}$ is the $k^{th}$ iterate of $x.$ If $f\$ is differentiable, then its only subgradient is the gradient vector $\nabla f$ itself. It may happen that $-g^{(k)}$ is not a descent direction for $f\$ at $x^{(k)}.$ We therefore maintain a list $f_{\rm {best}}\$ that keeps track of the lowest objective function value found so far, i.e. $f_{\rm {best}}^{(k)}=\min\{f_{\rm {best}}^{(k-1)},f(x^{(k)})\}.$

### Step size rules

Many different types of step-size rules are used by subgradient methods. This article notes five classical step-size rules for which convergence proofs are known:

- Constant step size, $\alpha _{k}=\alpha .$
- Constant step length, $\alpha _{k}=\gamma /\lVert g^{(k)}\rVert _{2},$ which gives $\lVert x^{(k+1)}-x^{(k)}\rVert _{2}=\gamma .$
- Square summable but not summable step size, i.e. any step sizes satisfying $\alpha _{k}\geq 0,\qquad \sum _{k=1}^{\infty }\alpha _{k}^{2}<\infty ,\qquad \sum _{k=1}^{\infty }\alpha _{k}=\infty .$
- Nonsummable diminishing, i.e. any step sizes satisfying $\alpha _{k}\geq 0,\qquad \lim _{k\to \infty }\alpha _{k}=0,\qquad \sum _{k=1}^{\infty }\alpha _{k}=\infty .$
- Nonsummable diminishing step lengths, i.e. $\alpha _{k}=\gamma _{k}/\lVert g^{(k)}\rVert _{2},$ where $\gamma _{k}\geq 0,\qquad \lim _{k\to \infty }\gamma _{k}=0,\qquad \sum _{k=1}^{\infty }\gamma _{k}=\infty .$

For all five rules, the step-sizes are determined "off-line", before the method is iterated; the step-sizes do not depend on preceding iterations. This "off-line" property of subgradient methods differs from the "on-line" step-size rules used for descent methods for differentiable functions: Many methods for minimizing differentiable functions satisfy Wolfe's sufficient conditions for convergence, where step-sizes typically depend on the current point and the current search-direction. An extensive discussion of stepsize rules for subgradient methods, including incremental versions, is given in the books by Bertsekas and by Bertsekas, Nedic, and Ozdaglar.

### Convergence results

For constant step-length and scaled subgradients having Euclidean norm equal to one, the subgradient method converges to an arbitrarily close approximation to the minimum value, that is

$\lim _{k\to \infty }f_{\rm {best}}^{(k)}-f^{*}<\epsilon$

by a result of

Shor

.

These classical subgradient methods have poor performance and are no longer recommended for general use. However, they are still used widely in specialized applications because they are simple and they can be easily adapted to take advantage of the special structure of the problem at hand.

## Subgradient-projection and bundle methods

During the 1970s, Claude Lemaréchal and Phil Wolfe proposed "bundle methods" of descent for problems of convex minimization. The meaning of the term "bundle methods" has changed significantly since that time. Modern versions and full convergence analysis were provided by Kiwiel. Contemporary bundle-methods often use "level control" rules for choosing step-sizes, developing techniques from the "subgradient-projection" method of Boris T. Polyak (1969). However, there are problems on which bundle methods offer little advantage over subgradient-projection methods.

## Constrained optimization

### Projected subgradient

One extension of the subgradient method is the **projected subgradient method**, which solves the constrained optimization problem

minimize

$f(x)\$

subject to

$x\in {\mathcal {C}}$

where ${\mathcal {C}}$ is a convex set. The projected subgradient method uses the iteration $x^{(k+1)}=P\left(x^{(k)}-\alpha _{k}g^{(k)}\right)$ where P is projection on ${\mathcal {C}}$ and $g^{(k)}$ is any subgradient of $f\$ at $x^{(k)}.$

### General constraints

The subgradient method can be extended to solve the inequality constrained problem

minimize

$f_{0}(x)\$

subject to

$f_{i}(x)\leq 0,\quad i=1,\ldots ,m$

where $f_{i}$ are convex. The algorithm takes the same form as the unconstrained case $x^{(k+1)}=x^{(k)}-\alpha _{k}g^{(k)}\$ where $\alpha _{k}>0$ is a step size, and $g^{(k)}$ is a subgradient of the objective or one of the constraint functions at $x.\$ Take $g^{(k)}={\begin{cases}\partial f_{0}(x)&{\text{ if }}f_{i}(x)\leq 0\;\forall i=1\dots m\\\partial f_{j}(x)&{\text{ for some }}j{\text{ such that }}f_{j}(x)>0\end{cases}}$ where $\partial f$ denotes the subdifferential of $f.\$ If the current point is feasible, the algorithm uses an objective subgradient; if the current point is infeasible, the algorithm chooses a subgradient of any violated constraint.

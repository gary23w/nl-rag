---
title: "Proximal operator"
source: https://en.wikipedia.org/wiki/Proximal_operator
domain: convex-analysis
license: CC-BY-SA-4.0
tags: convex analysis, convex conjugate, proximal operator, fenchel duality
fetched: 2026-07-02
---

# Proximal operator

In mathematical optimization, the **proximal** operator is an operator associated with a proper, lower semi-continuous convex function f from a Hilbert space ${\mathcal {X}}$ to $[-\infty ,+\infty ]$ , and is defined by:

$\operatorname {prox} _{f}(v)=\arg \min _{x\in {\mathcal {X}}}\left(f(x)+{\frac {1}{2}}\|x-v\|_{\mathcal {X}}^{2}\right).$

For any function in this class, the minimizer of the right-hand side above is unique, hence making the proximal operator well-defined. The proximal operator is used in proximal gradient methods, which is frequently used in optimization algorithms associated with non-differentiable optimization problems such as total variation denoising.

## Properties

The ${\text{prox}}$ of a proper, lower semi-continuous convex function f enjoys several useful properties for optimization.

- Fixed points of ${\text{prox}}_{f}$ are minimizers of f : $\{x\in {\mathcal {X}}\ |\ {\text{prox}}_{f}x=x\}=\arg \min f$ .
- Global convergence to a minimizer is defined as follows: If $\arg \min f\neq \varnothing$ , then for any initial point $x_{0}\in {\mathcal {X}}$ , the recursion $(\forall n\in \mathbb {N} )\quad x_{n+1}={\text{prox}}_{f}x_{n}$ yields convergence $x_{n}\to x\in \arg \min f$ as $n\to +\infty$ . This convergence may be weak if ${\mathcal {X}}$ is infinite dimensional.
- The proximal operator can be seen as a generalization of the projection operator. Indeed, in the specific case where f is the 0- $\infty$ characteristic function $\iota _{C}$ of a nonempty, closed, convex set C we have that

${\begin{aligned}\operatorname {prox} _{\iota _{C}}(x)&=\operatorname {argmin} \limits _{y}{\begin{cases}{\frac {1}{2}}\left\|x-y\right\|_{2}^{2}&{\text{if }}y\in C\\+\infty &{\text{if }}y\notin C\end{cases}}\\&=\operatorname {argmin} \limits _{y\in C}{\frac {1}{2}}\left\|x-y\right\|_{2}^{2}\end{aligned}}$

showing that the proximity operator is indeed a generalisation of the projection operator.

- A function is firmly non-expansive if $(\forall (x,y)\in {\mathcal {X}}^{2})\quad \|{\text{prox}}_{f}x-{\text{prox}}_{f}y\|^{2}\leq \langle x-y\ ,{\text{prox}}_{f}x-{\text{prox}}_{f}y\rangle$ .
- The proximal operator of a function is related to the gradient of the Moreau envelope $M_{\lambda f}$ of a function $\lambda f$ by the following identity: $\nabla M_{\lambda f}(x)={\frac {1}{\lambda }}(x-\mathrm {prox} _{\lambda f}(x))$ .
- The proximity operator of f is characterized by inclusion $p=\operatorname {prox} _{f}(x)\Leftrightarrow x-p\in \partial f(p)$ , where $\partial f$ is the subdifferential of f , given by

$\partial f(x)=\{u\in \mathbb {R} ^{N}\mid \forall y\in \mathbb {R} ^{N},(y-x)^{\mathrm {T} }u+f(x)\leq f(y)\}$

In particular, If

f

is differentiable then the above equation reduces to

$p=\operatorname {prox} _{f}(x)\Leftrightarrow x-p=\nabla f(p)$

.

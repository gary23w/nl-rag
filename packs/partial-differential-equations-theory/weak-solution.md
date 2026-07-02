---
title: "Weak solution"
source: https://en.wikipedia.org/wiki/Weak_solution
domain: partial-differential-equations-theory
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, sobolev space
fetched: 2026-07-02
---

# Weak solution

In mathematics, a **weak solution** (also called a **generalized solution**) to an ordinary or partial differential equation is a function for which the derivatives may not all exist but which is nonetheless deemed to satisfy the equation in some precisely defined sense. There are many different definitions of weak solution, appropriate for different classes of equations. One of the most important is based on the notion of distributions.

Avoiding the language of distributions, one starts with a differential equation and rewrites it in such a way that no derivatives of the solution of the equation show up (the new form is called the weak formulation, and the solutions to it are called weak solutions). Somewhat surprisingly, a differential equation may have solutions that are not differentiable, and the weak formulation allows one to find such solutions.

Weak solutions are important because many differential equations encountered in modelling real-world phenomena do not admit of sufficiently smooth solutions, and the only way of solving such equations is using the weak formulation. Even in situations where an equation does have differentiable solutions, it is often convenient to first prove the existence of weak solutions and only later show that those solutions are in fact smooth enough.

Examples of equations that have weak solutions but fail to have strong solutions include the Tanaka equation and Tsirelson's stochastic differential equation.

## A concrete example

As an illustration of the concept, consider the first-order wave equation:

| ${\frac {\partial u}{\partial t}}+{\frac {\partial u}{\partial x}}=0$ |   | 1 |
|---|---|---|

where *u* = *u*(*t*, *x*) is a function of two real variables. To indirectly probe the properties of a possible solution *u*, one integrates it against an arbitrary smooth function $\varphi \,\!$ of compact support, known as a *test function,* taking

$\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }u(t,x)\,\varphi (t,x)\,dx\,dt$

For example, if $\varphi$ is a smooth probability distribution concentrated near a point $(t,x)=(t_{\circ },x_{\circ })$ , the integral is approximately $u(t_{\circ },x_{\circ })$ . Notice that while the integrals go from $-\infty$ to $\infty$ , they are essentially over a finite box where $\varphi$ is non-zero.

Thus, assume a solution *u* is continuously differentiable on the Euclidean space **R**2, multiply the equation (**1**) by a test function $\varphi$ (smooth of compact support), and integrate:

$\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }{\frac {\partial u(t,x)}{\partial t}}\varphi (t,x)\,\mathrm {d} t\,\mathrm {d} x+\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }{\frac {\partial u(t,x)}{\partial x}}\varphi (t,x)\,\mathrm {d} t\,\mathrm {d} x=0.$

Using Fubini's theorem, which allows one to interchange the order of integration, as well as integration by parts (in *t* for the first term and in *x* for the second term) this equation becomes:

| $\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }u(t,x){\frac {\partial \varphi (t,x)}{\partial t}}\,\mathrm {d} t\,\mathrm {d} x+\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }u(t,x){\frac {\partial \varphi (t,x)}{\partial x}}\,\mathrm {d} t\,\mathrm {d} x=0.$ |   | 2 |
|---|---|---|

(Boundary terms vanish since $\varphi$ is zero outside a finite box.) We have shown that equation (**1**) implies equation (**2**) as long as *u* is continuously differentiable.

The key to the concept of weak solution is that there exist functions *u* that satisfy equation (**2**) for any $\varphi$ , but such *u* may not be differentiable and so cannot satisfy equation (**1**). An example is *u*(*t*, *x*) = |*t* − *x*|, as one may check by splitting the integrals over regions *x* ≥ *t* and *x* ≤ *t*, where *u* is smooth, and reversing the above computation using integration by parts. A *weak solution* of equation (**1**) means *any* solution *u* of equation (**2**) over all test functions $\varphi$ .

## General case

The general idea that follows from this example is that, when solving a differential equation in *u*, one can rewrite it using a test function $\varphi$ , such that whatever derivatives in *u* show up in the equation, they are "transferred" via integration by parts to $\varphi$ , resulting in an equation without derivatives of *u*. This new equation generalizes the original equation to include solutions that are not necessarily differentiable.

The approach illustrated above works in great generality. Indeed, consider a linear differential operator in an open set *W* in **R***n*:

$P(x,\partial )u(x)=\sum a_{\alpha _{1},\alpha _{2},\dots ,\alpha _{n}}(x)\,\partial ^{\alpha _{1}}\partial ^{\alpha _{2}}\cdots \partial ^{\alpha _{n}}u(x),$

where the multi-index (*α*1, *α*2, ..., *α**n*) varies over some finite set in **N***n* and the coefficients $a_{\alpha _{1},\alpha _{2},\dots ,\alpha _{n}}$ are smooth enough functions of *x* in **R***n*.

The differential equation *P*(*x*, *∂*)*u*(*x*) = 0 can, after being multiplied by a smooth test function $\varphi$ with compact support in *W* and integrated by parts, be written as

$\int _{W}u(x)Q(x,\partial )\varphi (x)\,\mathrm {d} x=0$

where the differential operator *Q*(*x*, *∂*) is given by the formula

$Q(x,\partial )\varphi (x)=\sum (-1)^{|\alpha |}\partial ^{\alpha _{1}}\partial ^{\alpha _{2}}\cdots \partial ^{\alpha _{n}}\left[a_{\alpha _{1},\alpha _{2},\dots ,\alpha _{n}}(x)\varphi (x)\right].$

The number

$(-1)^{|\alpha |}=(-1)^{\alpha _{1}+\alpha _{2}+\cdots +\alpha _{n}}$

shows up because one needs *α*1 + *α*2 + ⋯ + *α**n* integrations by parts to transfer all the partial derivatives from *u* to $\varphi$ in each term of the differential equation, and each integration by parts entails a multiplication by −1.

The differential operator *Q*(*x*, *∂*) is the **formal adjoint** of *P*(*x*, *∂*) (cf. adjoint of an operator).

In summary, if the original (strong) problem was to find an |*α*|-times differentiable function *u* defined on the open set *W* such that

$P(x,\partial )u(x)=0{\text{ for all }}x\in W$

(a so-called **strong solution**), then an integrable function *u* would be said to be a **weak solution** if

$\int _{W}u(x)\,Q(x,\partial )\varphi (x)\,\mathrm {d} x=0$

for every smooth function $\varphi$ with compact support in *W*.

## Other kinds of weak solution

The notion of weak solution based on distributions is sometimes inadequate. In the case of hyperbolic systems, the notion of weak solution based on distributions does not guarantee uniqueness, and it is necessary to supplement it with entropy conditions or some other selection criterion. In fully nonlinear PDE such as the Hamilton–Jacobi equation, there is a very different definition of weak solution called viscosity solution.

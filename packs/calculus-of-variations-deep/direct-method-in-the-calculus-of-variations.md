---
title: "Direct method in the calculus of variations"
source: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
domain: calculus-of-variations-deep
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, beltrami identity, hamilton principle
fetched: 2026-07-02
---

# Direct method in the calculus of variations

In mathematics, the **direct method in the calculus of variations** is a general method for constructing a proof of the existence of a minimizer for a given functional, introduced by Stanisław Zaremba and David Hilbert around 1900. The method relies on methods of functional analysis and topology. As well as being used to prove the existence of a solution, direct methods may be used to compute the solution to desired accuracy.

## The method

The calculus of variations deals with functionals $J:V\to {\bar {\mathbb {R} }}$ , where V is some function space and ${\bar {\mathbb {R} }}=\mathbb {R} \cup \{\infty \}$ . The main interest of the subject is to find *minimizers* for such functionals, that is, functions $v\in V$ such that $J(v)\leq J(u)$ for all $u\in V$ .

The standard tool for obtaining necessary conditions for a function to be a minimizer is the Euler–Lagrange equation. But seeking a minimizer amongst functions satisfying these may lead to false conclusions if the existence of a minimizer is not established beforehand.

The functional J must be bounded from below to have a minimizer. This means

$\inf\{J(u)|u\in V\}>-\infty .\,$

This condition is not enough to know that a minimizer exists, but it shows the existence of a *minimizing sequence*, that is, a sequence $(u_{n})$ in V such that $J(u_{n})\to \inf\{J(u)|u\in V\}.$

The direct method may be broken into the following steps

1. Take a minimizing sequence $(u_{n})$ for J .
2. Show that $(u_{n})$ admits some subsequence $(u_{n_{k}})$ , that converges to a $u_{0}\in V$ with respect to a topology $\tau$ on V .
3. Show that J is sequentially lower semi-continuous with respect to the topology $\tau$ .

To see that this shows the existence of a minimizer, consider the following characterization of sequentially lower-semicontinuous functions.

The function

J

is sequentially lower-semicontinuous if

$\liminf _{n\to \infty }J(u_{n})\geq J(u_{0})$

for any convergent sequence

$u_{n}\to u_{0}$

in

V

.

The conclusions follows from

$\inf\{J(u)|u\in V\}=\lim _{n\to \infty }J(u_{n})=\lim _{k\to \infty }J(u_{n_{k}})\geq J(u_{0})\geq \inf\{J(u)|u\in V\}$

,

in other words

$J(u_{0})=\inf\{J(u)|u\in V\}$

.

## Details

### Banach spaces

The direct method may often be applied with success when the space V is a subset of a separable reflexive Banach space W . In this case the sequential Banach–Alaoglu theorem implies that any bounded sequence $(u_{n})$ in V has a subsequence that converges to some $u_{0}$ in W with respect to the weak topology. If V is sequentially closed in W , so that $u_{0}$ is in V , the direct method may be applied to a functional $J:V\to {\bar {\mathbb {R} }}$ by showing

1. J is bounded from below,
2. any minimizing sequence for J is bounded, and
3. J is weakly sequentially lower semi-continuous, i.e., for any weakly convergent sequence $u_{n}\to u_{0}$ it holds that $\liminf _{n\to \infty }J(u_{n})\geq J(u_{0})$ .

The second part is usually accomplished by showing that J admits some growth condition. An example is

$J(x)\geq \alpha \lVert x\rVert ^{q}-\beta$

for some

$\alpha >0$

,

$q\geq 1$

and

$\beta \geq 0$

.

A functional with this property is sometimes called coercive. Showing sequential lower semi-continuity is usually the most difficult part when applying the direct method. See below for some theorems for a general class of functionals.

### Sobolev spaces

The typical functional in the calculus of variations is an integral of the form

$J(u)=\int _{\Omega }F(x,u(x),\nabla u(x))dx$

where $\Omega$ is a subset of $\mathbb {R} ^{n}$ and F is a real-valued function on $\Omega \times \mathbb {R} ^{m}\times \mathbb {R} ^{mn}$ . The argument of J is a differentiable function $u:\Omega \to \mathbb {R} ^{m}$ , and its Jacobian $\nabla u(x)$ is identified with a $mn$ -vector.

When deriving the Euler–Lagrange equation, the common approach is to assume $\Omega$ has a $C^{2}$ boundary and let the domain of definition for J be $C^{2}(\Omega ,\mathbb {R} ^{m})$ . This space is a Banach space when endowed with the supremum norm, but it is not reflexive. When applying the direct method, the functional is usually defined on a Sobolev space $W^{1,p}(\Omega ,\mathbb {R} ^{m})$ with $p>1$ , which is a reflexive Banach space. The derivatives of u in the formula for J must then be taken as weak derivatives.

Another common function space is $W_{g}^{1,p}(\Omega ,\mathbb {R} ^{m})$ which is the affine sub space of $W^{1,p}(\Omega ,\mathbb {R} ^{m})$ of functions whose trace is some fixed function g in the image of the trace operator. This restriction allows finding minimizers of the functional J that satisfy some desired boundary conditions. This is similar to solving the Euler–Lagrange equation with Dirichlet boundary conditions. Additionally there are settings in which there are minimizers in $W_{g}^{1,p}(\Omega ,\mathbb {R} ^{m})$ but not in $W^{1,p}(\Omega ,\mathbb {R} ^{m})$ . The idea of solving minimization problems while restricting the values on the boundary can be further generalized by looking on function spaces where the trace is fixed only on a part of the boundary, and can be arbitrary on the rest.

The next section presents theorems regarding weak sequential lower semi-continuity of functionals of the above type.

## Sequential lower semi-continuity of integrals

As many functionals in the calculus of variations are of the form

$J(u)=\int _{\Omega }F(x,u(x),\nabla u(x))dx$

,

where $\Omega \subseteq \mathbb {R} ^{n}$ is open, theorems characterizing functions F for which J is weakly sequentially lower-semicontinuous in $W^{1,p}(\Omega ,\mathbb {R} ^{m})$ with $p\geq 1$ is of great importance.

In general one has the following:

Assume that

F

is a function that has the following properties:

1. The function F is a Carathéodory function.
2. There exist $a\in L^{q}(\Omega ,\mathbb {R} ^{mn})$ with Hölder conjugate $q={\tfrac {p}{p-1}}$ and $b\in L^{1}(\Omega )$ such that the following inequality holds true for almost every $x\in \Omega$ and every $(y,A)\in \mathbb {R} ^{m}\times \mathbb {R} ^{mn}$ : $F(x,y,A)\geq \langle a(x),A\rangle +b(x)$ . Here, $\langle a(x),A\rangle$ denotes the Frobenius inner product of $a(x)$ and A in $\mathbb {R} ^{mn}$ ).

If the function

$A\mapsto F(x,y,A)$

is convex for almost every

$x\in \Omega$

and every

$y\in \mathbb {R} ^{m}$

,

then

J

is sequentially weakly lower semi-continuous.

When $n=1$ or $m=1$ the following converse-like theorem holds

Assume that

F

is continuous and satisfies

$|F(x,y,A)|\leq a(x,|y|,|A|)$

for every

$(x,y,A)$

, and a fixed function

$a(x,|y|,|A|)$

increasing in

$|y|$

and

$|A|$

, and locally integrable in

x

. If

J

is sequentially weakly lower semi-continuous, then for any given

$(x,y)\in \Omega \times \mathbb {R} ^{m}$

the function

$A\mapsto F(x,y,A)$

is convex.

In conclusion, when $m=1$ or $n=1$ , the functional J , assuming reasonable growth and boundedness on F , is weakly sequentially lower semi-continuous if, and only if the function $A\mapsto F(x,y,A)$ is convex.

However, there are many interesting cases where one cannot assume that F is convex. The following theorem proves sequential lower semi-continuity using a weaker notion of convexity:

Assume that

$F:\Omega \times \mathbb {R} ^{m}\times \mathbb {R} ^{mn}\to [0,\infty )$

is a function that has the following properties:

1. The function F is a Carathéodory function.
2. The function F has p -growth for some $p>1$ : There exists a constant C such that for every $y\in \mathbb {R} ^{m}$ and for almost every $x\in \Omega$ $|F(x,y,A)|\leq C(1+|y|^{p}+|A|^{p})$ .
3. For every $y\in \mathbb {R} ^{m}$ and for almost every $x\in \Omega$ , the function $A\mapsto F(x,y,A)$ is quasiconvex: there exists a cube $D\subseteq \mathbb {R} ^{n}$ such that for every $A\in \mathbb {R} ^{mn},\varphi \in W_{0}^{1,\infty }(\Omega ,\mathbb {R} ^{m})$ it holds:

$F(x,y,A)\leq |D|^{-1}\int _{D}F(x,y,A+\nabla \varphi (z))dz$

where

$|D|$

is the

volume

of

D

.

Then

J

is sequentially weakly lower semi-continuous in

$W^{1,p}(\Omega ,\mathbb {R} ^{m})$

.

A converse like theorem in this case is the following:

Assume that

F

is continuous and satisfies

$|F(x,y,A)|\leq a(x,|y|,|A|)$

for every

$(x,y,A)$

, and a fixed function

$a(x,|y|,|A|)$

increasing in

$|y|$

and

$|A|$

, and locally integrable in

x

. If

J

is sequentially weakly lower semi-continuous, then for any given

$(x,y)\in \Omega \times \mathbb {R} ^{m}$

the function

$A\mapsto F(x,y,A)$

is

quasiconvex

. The claim is true even when both

$m,n$

are bigger than

1

and coincides with the previous claim when

$m=1$

or

$n=1$

, since then quasiconvexity is equivalent to convexity.

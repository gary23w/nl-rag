---
title: "Convex conjugate"
source: https://en.wikipedia.org/wiki/Convex_conjugate
domain: convex-analysis
license: CC-BY-SA-4.0
tags: convex analysis, convex conjugate, proximal operator, fenchel duality
fetched: 2026-07-02
---

# Convex conjugate

In mathematics and mathematical optimization, the **convex conjugate** of a function is a generalization of the Legendre transformation which applies to non-convex functions. It is also known as **Legendre–Fenchel transformation**, **Fenchel transformation**, or **Fenchel conjugate** (after Adrien-Marie Legendre and Werner Fenchel). The convex conjugate is widely used for constructing the dual problem in optimization theory, thus generalizing Lagrangian duality.

## Definition

Let X be a real topological vector space and let $X^{*}$ be the dual space to X . Denote by

$\langle \cdot ,\cdot \rangle :X^{*}\times X\to \mathbb {R}$

the canonical dual pairing, which is defined by $\left\langle x^{*},x\right\rangle =x^{*}(x).$

For a function $f:X\to \mathbb {R} \cup \{-\infty ,+\infty \}$ taking values on the extended real number line, its ***convex conjugate*** is the function

$f^{*}:X^{*}\to \mathbb {R} \cup \{-\infty ,+\infty \}$

whose value at $x^{*}\in X^{*}$ is defined to be the supremum:

$f^{*}\left(x^{*}\right):=\sup \left\{\left\langle x^{*},x\right\rangle -f(x)~\colon ~x\in X\right\},$

or, equivalently, in terms of the infimum:

$f^{*}\left(x^{*}\right):=-\inf \left\{f(x)-\left\langle x^{*},x\right\rangle ~\colon ~x\in X\right\}.$

This definition can be interpreted as an encoding of the convex hull of the function's epigraph in terms of its supporting hyperplanes.

## Examples

For more examples, see § Table of selected convex conjugates.

- The convex conjugate of an affine function $f(x)=\left\langle a,x\right\rangle -b$ is $f^{*}\left(x^{*}\right)={\begin{cases}b,&x^{*}=a\\+\infty ,&x^{*}\neq a.\end{cases}}$
- The convex conjugate of a power function $f(x)={\frac {1}{p}}|x|^{p},1<p<\infty$ is $f^{*}\left(x^{*}\right)={\frac {1}{q}}|x^{*}|^{q},1<q<\infty ,{\text{where}}{\tfrac {1}{p}}+{\tfrac {1}{q}}=1.$
- The convex conjugate of the absolute value function $f(x)=\left|x\right|$ is $f^{*}\left(x^{*}\right)={\begin{cases}0,&\left|x^{*}\right|\leq 1\\\infty ,&\left|x^{*}\right|>1.\end{cases}}$
- The convex conjugate of the exponential function $f(x)=e^{x}$ is $f^{*}\left(x^{*}\right)={\begin{cases}x^{*}\ln x^{*}-x^{*},&x^{*}>0\\0,&x^{*}=0\\\infty ,&x^{*}<0.\end{cases}}$

The convex conjugate and Legendre transform of the exponential function agree except that the domain of the convex conjugate is strictly larger as the Legendre transform is only defined for positive real numbers.

### Connection with expected shortfall (average value at risk)

See this article for example.

Let *F* denote a cumulative distribution function of a random variable *X*. Then (integrating by parts), $f(x):=\int _{-\infty }^{x}F(u)\,du=\operatorname {E} \left[\max(0,x-X)\right]=x-\operatorname {E} \left[\min(x,X)\right]$ has the convex conjugate $f^{*}(p)=\int _{0}^{p}F^{-1}(q)\,dq=(p-1)F^{-1}(p)+\operatorname {E} \left[\min(F^{-1}(p),X)\right]=pF^{-1}(p)-\operatorname {E} \left[\max(0,F^{-1}(p)-X)\right].$

### Ordering

A particular interpretation has the transform $f^{\text{inc}}(x):=\arg \sup _{t}t\cdot x-\int _{0}^{1}\max\{t-f(u),0\}\,du,$ as this is a nondecreasing rearrangement of the initial function *f*; in particular, $f^{\text{inc}}=f$ for *f* nondecreasing.

## Properties

The convex conjugate of a closed convex function is again a closed convex function. The convex conjugate of a polyhedral convex function (a convex function with polyhedral epigraph) is again a polyhedral convex function.

### Order reversing

Declare that $f\leq g$ if and only if $f(x)\leq g(x)$ for all $x.$ Then convex-conjugation is order-reversing, which by definition means that if $f\leq g$ then $f^{*}\geq g^{*}.$

For a family of functions $\left(f_{\alpha }\right)_{\alpha }$ it follows from the fact that supremums may be interchanged that

$\left(\inf _{\alpha }f_{\alpha }\right)^{*}(x^{*})=\sup _{\alpha }f_{\alpha }^{*}(x^{*}),$

and from the max–min inequality that

$\left(\sup _{\alpha }f_{\alpha }\right)^{*}(x^{*})\leq \inf _{\alpha }f_{\alpha }^{*}(x^{*}).$

### Biconjugate

The convex conjugate of a function is always lower semi-continuous. The **biconjugate** $f^{**}$ (the convex conjugate of the convex conjugate) is also the closed convex hull, i.e. the largest lower semi-continuous convex function with $f^{**}\leq f.$ For proper functions $f,$

$f=f^{**}$

if and only if

f

is convex and lower semi-continuous, by the

Fenchel–Moreau theorem

.

The Fenchel inequality (below) implies $f^{**}\leq f$ . More precisely, $f^{**}$ is the greatest lower semicontinuous convex function not exceeding f , often described as the closed convex envelope of f . In particular, by the Fenchel–Moreau theorem, a proper function is equal to its biconjugate if and only if it is convex and lower semicontinuous.

### Fenchel's inequality

For any function f and its convex conjugate *f* *, **Fenchel's inequality** (also known as the **Fenchel–Young inequality**) holds for every $x\in X$ and $p\in X^{*}$ :

$\left\langle p,x\right\rangle \leq f(x)+f^{*}(p).$

Furthermore, the equality holds only when $p\in \partial f(x)$ , where $\partial f(x)$ is the subgradient. The proof follows from the definition of convex conjugate: $f^{*}(p)=\sup _{\tilde {x}}\left\{\langle p,{\tilde {x}}\rangle -f({\tilde {x}})\right\}\geq \langle p,x\rangle -f(x).$

### Convexity

For two functions $f_{0}$ and $f_{1}$ and a number $0\leq \lambda \leq 1$ the convexity relation

$\left((1-\lambda )f_{0}+\lambda f_{1}\right)^{*}\leq (1-\lambda )f_{0}^{*}+\lambda f_{1}^{*}$

holds. The ${*}$ operation is a convex mapping itself.

### Infimal convolution

The **infimal convolution** (or epi-sum) of two functions f and g is defined as

$\left(f\operatorname {\Box } g\right)(x)=\inf \left\{f(x-y)+g(y)\mid y\in \mathbb {R} ^{n}\right\}.$

The operation $\operatorname {\Box }$ is symmetric (commutative) and associative, i.e.

$f\Box g=g\Box f,\qquad (f\Box g)\Box h=f\Box (g\Box h).$

Let $f_{1},\ldots ,f_{m}$ be proper, convex and lower semicontinuous functions on $\mathbb {R} ^{n}.$ Then the infimal convolution is convex and lower semicontinuous (but not necessarily proper), and satisfies

$\left(f_{1}\operatorname {\Box } \cdots \operatorname {\Box } f_{m}\right)^{*}=f_{1}^{*}+\cdots +f_{m}^{*},$

or, equivalently,

$\left(f_{1}+\cdots +f_{m}\right)^{*}=f_{1}^{*}\operatorname {\Box } \cdots \operatorname {\Box } f_{m}^{*},$

which expresses the behaviour of convex conjugation with respect to sums of functions.

The infimal convolution of two functions has a geometric interpretation: The (strict) epigraph of the infimal convolution of two functions is the Minkowski sum of the (strict) epigraphs of those functions.

### Maximizing argument

If the function f is differentiable, then its derivative is the maximizing argument in the computation of the convex conjugate:

$f^{\prime }(x)=x^{*}(x):=\arg \sup _{x^{*}}{\langle x,x^{*}\rangle }-f^{*}\left(x^{*}\right)$

and

$f^{{*}\prime }\left(x^{*}\right)=x\left(x^{*}\right):=\arg \sup _{x}{\langle x,x^{*}\rangle }-f(x);$

hence

$x=\nabla f^{*}\left(\nabla f(x)\right),$

$x^{*}=\nabla f\left(\nabla f^{*}\left(x^{*}\right)\right),$

and moreover

$f^{\prime \prime }(x)\cdot f^{{*}\prime \prime }\left(x^{*}(x)\right)=1,$

$f^{{*}\prime \prime }\left(x^{*}\right)\cdot f^{\prime \prime }\left(x(x^{*})\right)=1.$

### Scaling properties

If for some $\gamma >0,$ $g(x)=\alpha +\beta x+\gamma \cdot f\left(\lambda x+\delta \right)$ , then

$g^{*}\left(x^{*}\right)=-\alpha -\delta {\frac {x^{*}-\beta }{\lambda }}+\gamma \cdot f^{*}\left({\frac {x^{*}-\beta }{\lambda \gamma }}\right).$

### Behavior under linear transformations

Let $A:X\to Y$ be a bounded linear operator. For any convex function f on $X,$

$\left(Af\right)^{*}=f^{*}A^{*}$

where

$(Af)(y)=\inf\{f(x):x\in X,Ax=y\}$

is the preimage of f with respect to A and $A^{*}$ is the adjoint operator of $A.$

A closed convex function f is symmetric with respect to a given set G of orthogonal linear transformations,

$f(Ax)=f(x)$

for all

x

and all

$A\in G$

if and only if its convex conjugate $f^{*}$ is symmetric with respect to $G.$

## Table of selected convex conjugates

The following table provides Legendre transforms for many common functions as well as a few useful properties.

| $g(x)$ | $\operatorname {dom} (g)$ | $g^{*}(x^{*})$ | $\operatorname {dom} (g^{*})$ |
|---|---|---|---|
| $f(ax)$ (where $a\neq 0$ ) | X | $f^{*}\left({\frac {x^{*}}{a}}\right)$ | $X^{*}$ |
| $f(x+b)$ | X | $f^{*}(x^{*})-\langle b,x^{*}\rangle$ | $X^{*}$ |
| $af(x)$ (where $a>0$ ) | X | $af^{*}\left({\frac {x^{*}}{a}}\right)$ | $X^{*}$ |
| $\alpha +\beta x+\gamma \cdot f(\lambda x+\delta )$ | X | $-\alpha -\delta {\frac {x^{*}-\beta }{\lambda }}+\gamma \cdot f^{*}\left({\frac {x^{*}-\beta }{\gamma \lambda }}\right)\quad (\gamma >0)$ | $X^{*}$ |
| ${\frac {\|x\|^{p}}{p}}$ (where $p>1$ ) | $\mathbb {R}$ | ${\frac {\|x^{*}\|^{q}}{q}}$ (where ${\frac {1}{p}}+{\frac {1}{q}}=1$ ) | $\mathbb {R}$ |
| ${\frac {-x^{p}}{p}}$ (where $0<p<1$ ) | $\mathbb {R} _{+}$ | ${\frac {-(-x^{*})^{q}}{q}}$ (where ${\frac {1}{p}}+{\frac {1}{q}}=1$ ) | $\mathbb {R} _{--}$ |
| ${\sqrt {1+x^{2}}}$ | $\mathbb {R}$ | $-{\sqrt {1-(x^{*})^{2}}}$ | $[-1,1]$ |
| $-\log(x)$ | $\mathbb {R} _{++}$ | $-(1+\log(-x^{*}))$ | $\mathbb {R} _{--}$ |
| $e^{x}$ | $\mathbb {R}$ | ${\begin{cases}x^{*}\log(x^{*})-x^{*}&{\text{if }}x^{*}>0\\0&{\text{if }}x^{*}=0\end{cases}}$ | $\mathbb {R} _{+}$ |
| $\log \left(1+e^{x}\right)$ | $\mathbb {R}$ | ${\begin{cases}x^{*}\log(x^{*})+(1-x^{*})\log(1-x^{*})&{\text{if }}0<x^{*}<1\\0&{\text{if }}x^{*}=0,1\end{cases}}$ | $[0,1]$ |
| $-\log \left(1-e^{x}\right)$ | $\mathbb {R} _{--}$ | ${\begin{cases}x^{*}\log(x^{*})-(1+x^{*})\log(1+x^{*})&{\text{if }}x^{*}>0\\0&{\text{if }}x^{*}=0\end{cases}}$ | $\mathbb {R} _{+}$ |

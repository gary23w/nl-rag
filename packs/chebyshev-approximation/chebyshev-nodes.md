---
title: "Chebyshev nodes"
source: https://en.wikipedia.org/wiki/Chebyshev_nodes
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
---

# Chebyshev nodes

In numerical analysis, **Chebyshev nodes** (also called **Chebyshev points** or a **Chebyshev grid**) are a set of specific algebraic numbers used as nodes for polynomial interpolation and numerical integration. They are the projection of a set of equispaced points on the unit circle onto the real interval $[-1,1]$ , the circle's diameter.

There are two kinds of Chebyshev nodes. The ⁠ n ⁠ *Chebyshev nodes of the first kind*, also called the **Chebyshev–Gauss nodes** or **Chebyshev zeros**, are the zeros of a Chebyshev polynomial of the first kind, ⁠ $T_{n}$ ⁠. The corresponding ⁠ $n+1$ ⁠ *Chebyshev nodes of the second kind*, also called the **Chebyshev–Lobatto nodes** or **Chebyshev extrema**, are the extrema of ⁠ $T_{n}$ ⁠, which are also the zeros of a Chebyshev polynomial of the second kind, ⁠ $U_{n-1}$ ⁠, along with the two endpoints of the interval. Both types of numbers are commonly referred to as *Chebyshev nodes* or *Chebyshev points* in literature. They are named after 19th century Russian mathematician Pafnuty Chebyshev, who first introduced Chebyshev polynomials.

Unlike some other interpolation nodes, the Chebyshev nodes "nest": the existing nodes are retained when doubling the number of nodes, reducing computation for each grid refinement by half. Polynomial interpolants constructed from Chebyshev nodes minimize the effect of Runge's phenomenon. They can be easily converted to a representation as a weighted sum of Chebyshev polynomials using the fast Fourier transform.

## Definition

For a given positive integer n , the ⁠ n ⁠ Chebyshev nodes of the first kind are given by

$x_{k}=\cos {\frac {{\bigl (}k+{\tfrac {1}{2}}{\bigr )}\pi }{n}},\quad k=0,\ldots ,n-1.$

This is the projection of ⁠ $2n$ ⁠ equispaced points on the unit circle onto the interval ⁠ $[-1,1]$ ⁠, the circle's diameter. These points are also the roots of ⁠ $T_{n}$ ⁠, the Chebyshev polynomial of the first kind with degree ⁠ n ⁠.

The ⁠ $n+1$ ⁠ Chebyshev nodes of the second kind are given by

$x_{k}=\cos {\frac {k\pi }{n}},\quad k=0,\ldots ,n.$

This is also the projection of ⁠ $2n$ ⁠ equispaced points on the unit circle onto ⁠ $[-1,1]$ ⁠, this time including the endpoints of the interval, each of which is only the projection of one point on the circle rather than two. These points are also the extrema of ⁠ $T_{n}$ ⁠ in ⁠ $[-1,1]$ ⁠, the places where it takes the value ⁠ $\pm 1$ ⁠. The interior points among the nodes, not including the endpoints, are also the zeros of ⁠ $U_{n-1}$ ⁠, a Chebyshev polynomial of the second kind, a rescaling of the derivative of ⁠ $T_{n}$ ⁠.

For nodes over an arbitrary interval $[a,b]$ an affine transformation from $[-1,1]$ can be used: ${\tilde {x}}_{k}={\tfrac {1}{2}}(a+b)+{\tfrac {1}{2}}(b-a)x_{k}.$

## Properties

Both kinds of nodes are always symmetric about zero, the midpoint of the interval.

## Examples

The node sets for the first few integers n are: ${\begin{aligned}{\text{roots}}(T_{0})&=\{\},&{\text{roots}}(U_{0})&=\{\},&{\text{extrema}}(T_{1})&=\{-1,+1\},\\{\text{roots}}(T_{1})&=\{0\},&{\text{roots}}(U_{1})&=\{0\},&{\text{extrema}}(T_{2})&=\{-1,0,+1\},\\{\text{roots}}(T_{2})&=\{-1/{\sqrt {2}},+1/{\sqrt {2}}\},&{\text{roots}}(U_{2})&=\{-1/2,+1/2\},&{\text{extrema}}(T_{3})&=\{-1,-1/2,+1/2,+1\}\\\end{aligned}}$

While these sets are sorted by ascending values, the defining formulas given above generate the Chebyshev nodes in reverse order from the greatest to the smallest.

## Approximation

The Chebyshev nodes are important in approximation theory because they form a particularly good set of nodes for polynomial interpolation. Given a function *f* on the interval $[-1,+1]$ and n points $x_{1},x_{2},\ldots ,x_{n},$ in that interval, the interpolation polynomial is that unique polynomial $P_{n-1}$ of degree at most $n-1$ which has value $f(x_{i})$ at each point $x_{i}$ . The interpolation error at x is $f(x)-P_{n-1}(x)={\frac {f^{(n)}(\xi )}{n!}}\prod _{i=1}^{n}(x-x_{i})$ for some $\xi$ (depending on x) in [−1, 1]. So it is logical to try to minimize $\max _{x\in [-1,1]}{\biggl |}\prod _{i=1}^{n}(x-x_{i}){\biggr |}.$

This product is a *monic* polynomial of degree n. It may be shown that the maximum absolute value (maximum norm) of any such polynomial is bounded from below by 21−*n*. This bound is attained by the scaled Chebyshev polynomials 21−*n* *T**n*, which are also monic. (Recall that |*T**n*(*x*)| ≤ 1 for *x* ∈ [−1, 1].) Therefore, when the interpolation nodes *x**i* are the roots of *T**n*, the error satisfies $\left|f(x)-P_{n-1}(x)\right|\leq {\frac {1}{2^{n-1}n!}}\max _{\xi \in [-1,1]}\left|f^{(n)}(\xi )\right|.$ For an arbitrary interval [*a*, *b*] a change of variable shows that $\left|f(x)-P_{n-1}(x)\right|\leq {\frac {1}{2^{n-1}n!}}\left({\frac {b-a}{2}}\right)^{n}\max _{\xi \in [a,b]}\left|f^{(n)}(\xi )\right|.$

## Modified even-order nodes

Some applications for interpolation nodes, such as the design of equally terminated passive Chebyshev filters, cannot use even-order Chebyshev nodes directly due to the lack of a root at 0. Instead, the Chebyshev nodes can be moved toward zero, with a double root at zero directly, using a transformation:

${\tilde {x}}_{k}=\operatorname {sgn} (x_{k}){\sqrt {\frac {x_{k}^{2}-x_{n/2}^{2}}{1-x_{n/2}^{2}}}}$

For example, Chebyshev nodes of the first kind of order 4 are ${0.9239,0.3827,-0.3827,-0.9239}$ , with $x_{n/2}=0.382683$ . Applying the transformation yields new nodes ${0.910180,0,0,-0.910180}$ . The modified even-order nodes now include zero twice.

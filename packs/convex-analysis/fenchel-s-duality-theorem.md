---
title: "Fenchel's duality theorem"
source: https://en.wikipedia.org/wiki/Fenchel%27s_duality_theorem
domain: convex-analysis
license: CC-BY-SA-4.0
tags: convex analysis, convex conjugate, proximal operator, fenchel duality
fetched: 2026-07-02
---

# Fenchel's duality theorem

In mathematics, **Fenchel's duality theorem** is a result in the theory of convex functions named after Werner Fenchel.

Let f be a proper convex function on $\mathbb {R} ^{n}$ and let g be a proper concave function on $\mathbb {R} ^{n}$ . Then, if regularity conditions are satisfied,

$\inf _{x}(f(x)-g(x))=\sup _{p}(g_{*}(p)-f^{*}(p)).$

where $f^{*}$ is the convex conjugate of f (also referred to as the Fenchel–Legendre transform) and $g_{*}$ is the concave conjugate of g . That is,

$f^{*}\left(x^{*}\right):=\sup \left\{\left.\left\langle x^{*},x\right\rangle -f\left(x\right)\right|x\in \mathbb {R} ^{n}\right\}$

$g_{*}\left(x^{*}\right):=\inf \left\{\left.\left\langle x^{*},x\right\rangle -g\left(x\right)\right|x\in \mathbb {R} ^{n}\right\}$

## Mathematical theorem

Let *X* and *Y* be Banach spaces, $f:X\to \mathbb {R} \cup \{+\infty \}$ and $g:Y\to \mathbb {R} \cup \{+\infty \}$ be convex functions and $A:X\to Y$ be a bounded linear map. Then the Fenchel problems:

$p^{*}=\inf _{x\in X}\{f(x)+g(Ax)\}$

$d^{*}=\sup _{y^{*}\in Y^{*}}\{-f^{*}(A^{*}y^{*})-g^{*}(-y^{*})\}$

satisfy weak duality, i.e. $p^{*}\geq d^{*}$ . Note that $f^{*}$ and $g^{*}$ are the convex conjugates of f and g , respectively, and $A^{*}$ is the adjoint operator. The perturbation function for this dual problem is given by $F(x,y)=f(x)+g(Ax-y)$ .

Suppose that f , g , and A satisfy either

1. f and g are lower semi-continuous and $0\in \operatorname {core} (\operatorname {dom} g-A\operatorname {dom} f)$ where $\operatorname {core}$ is the algebraic interior and $\operatorname {dom} h$ , where h is some function, is the set $\{z:h(z)<+\infty \}$ , or
2. $A\operatorname {dom} f\cap \operatorname {cont} g\neq \emptyset$ where $\operatorname {cont}$ are the points where the function is continuous.

Then strong duality holds, i.e. $p^{*}=d^{*}$ . If $d^{*}\in \mathbb {R}$ then supremum is attained.

## One-dimensional illustration

In the following figure, the minimization problem on the left side of the equation is illustrated. One seeks to vary *x* such that the vertical distance between the convex and concave curves at *x* is as small as possible. The position of the vertical line in the figure is the (approximate) optimum.

The next figure illustrates the maximization problem on the right hand side of the above equation. Tangents are drawn to each of the two curves such that both tangents have the same slope *p*. The problem is to adjust *p* in such a way that the two tangents are as far away from each other as possible (more precisely, such that the points where they intersect the y-axis are as far from each other as possible). Imagine the two tangents as metal bars with vertical springs between them that push them apart and against the two parabolas that are fixed in place.

Fenchel's theorem states that the two problems have the same solution. The points having the minimum vertical separation are also the tangency points for the maximally separated parallel tangents.

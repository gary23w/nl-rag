---
title: "Subderivative"
source: https://en.wikipedia.org/wiki/Subderivative
domain: convex-analysis
license: CC-BY-SA-4.0
tags: convex analysis, convex conjugate, proximal operator, fenchel duality
fetched: 2026-07-02
---

# Subderivative

In mathematics, the **subderivative** (or **subgradient**) generalizes the derivative to convex functions which are not necessarily differentiable. The set of subderivatives at a point is called the **subdifferential** at that point. Subderivatives arise in convex analysis, the study of convex functions, often in connection to convex optimization.

Let $f:I\to \mathbb {R}$ be a real-valued convex function defined on an open interval of the real line. Such a function need not be differentiable at all points: For example, the absolute value function $f(x)=|x|$ is non-differentiable when $x=0$ . However, as seen in the graph on the right (where $f(x)$ in blue has non-differentiable kinks similar to the absolute value function), for any $x_{0}$ in the domain of the function one can draw a line which goes through the point $(x_{0},f(x_{0}))$ and which is everywhere either touching or below the graph of *f*. The slope of such a line is called a *subderivative*.

## Definition

Rigorously, a *subderivative* of a convex function $f:I\to \mathbb {R}$ at a point $x_{0}$ in the open interval I is a real number c such that $f(x)-f(x_{0})\geq c(x-x_{0})$ for all $x\in I$ . By the converse of the mean value theorem, the set of subderivatives at $x_{0}$ for a convex function is a nonempty closed interval $[a,b]$ , where a and b are the one-sided limits $a=\lim _{x\to x_{0}^{-}}{\frac {f(x)-f(x_{0})}{x-x_{0}}},$ $b=\lim _{x\to x_{0}^{+}}{\frac {f(x)-f(x_{0})}{x-x_{0}}}.$ The interval $[a,b]$ of all subderivatives is called the **subdifferential** of the function f at $x_{0}$ , denoted by $\partial f(x_{0})$ . If f is convex, then its subdifferential at any point is non-empty. Moreover, if its subdifferential at $x_{0}$ contains exactly one subderivative, then f is differentiable at $x_{0}$ and $\partial f(x_{0})=\{f'(x_{0})\}$ .

## Examples

Consider the function $f(x)=|x|$ which is convex. Then, the subdifferential at the origin is the interval $[-1,1]$ . The subdifferential at any point $x_{0}<0$ is the singleton set $\{-1\}$ , while the subdifferential at any point $x_{0}>0$ is the singleton set $\{1\}$ . This is similar to the sign function, but is not single-valued at 0 , instead including all possible subderivatives.

More generally, if $f(x)=\|x\|$ is a norm on a normed space X , then for $x\neq 0$ ,

$\partial f(x)=\{x^{*}\in X^{*}:\langle x^{*},x\rangle =\|x\|,\ \|x^{*}\|_{*}=1\},$

while

$\partial f(0)=\{x^{*}\in X^{*}:\|x^{*}\|_{*}\leq 1\}.$

## Properties

- A convex function $f:I\to \mathbb {R}$ is differentiable at $x_{0}$ if and only if the subdifferential is a singleton set, which is $\{f'(x_{0})\}$ .
- A point $x_{0}$ is a global minimum of a convex function f if and only if zero is contained in the subdifferential. For instance, in the figure above, one may draw a horizontal "subtangent line" to the graph of f at $(x_{0},f(x_{0}))$ . This last property is a generalization of the fact that the derivative of a function differentiable at a local minimum is zero.
- If f and g are convex functions with subdifferentials $\partial f(x)$ and $\partial g(x)$ with x being the interior point of one of the functions, then the subdifferential of $f+g$ is $\partial (f+g)(x)=\partial f(x)+\partial g(x)$ (where the addition operator denotes the Minkowski sum). This reads as "the subdifferential of a sum is the sum of the subdifferentials."

## The subgradient

The concepts of subderivative and subdifferential can be generalized to functions of several variables. If $f:U\to \mathbb {R}$ is a real-valued convex function defined on a convex open set in the Euclidean space $\mathbb {R} ^{n}$ , a vector v in that space is called a **subgradient** at $x_{0}\in U$ if for any $x\in U$ one has that

$f(x)-f(x_{0})\geq v\cdot (x-x_{0}),$

where the dot denotes the dot product. The set of all subgradients at $x_{0}$ is called the **subdifferential** at $x_{0}$ and is denoted $\partial f(x_{0})$ . The subdifferential is always a nonempty convex compact set.

These concepts generalize further to convex functions $f:U\to \mathbb {R}$ on a convex set in a locally convex space V . A functional $v^{*}$ in the dual space $V^{*}$ is called a *subgradient* at $x_{0}$ in U if for all $x\in U$ ,

$f(x)-f(x_{0})\geq v^{*}(x-x_{0}).$

The set of all subgradients at $x_{0}$ is called the subdifferential at $x_{0}$ and is again denoted $\partial f(x_{0})$ . The subdifferential is always a convex closed set. It can be an empty set; consider for example an unbounded operator, which is convex, but has no subgradient. If f is continuous, the subdifferential is nonempty.

## Relation to convex conjugacy

For a proper convex function $f:X\to (-\infty ,+\infty ]$ on a locally convex space, the subdifferential can be characterized using the convex conjugate. The Fenchel–Young inequality states that

$f(x)+f^{*}(x^{*})\geq \langle x^{*},x\rangle$

for all $x\in X$ and $x^{*}\in X^{*}$ . Equality holds if and only if $x^{*}$ is a subgradient of f at x ; that is,

$x^{*}\in \partial f(x)$

if and only if

$f(x)+f^{*}(x^{*})=\langle x^{*},x\rangle .$

Equivalently,

$\partial f(x)=\{x^{*}\in X^{*}:\langle x^{*},x\rangle -f(x)=f^{*}(x^{*})\}.$

Geometrically, this says that the affine function

$z\mapsto \langle x^{*},z\rangle -f^{*}(x^{*})$

supports f from below at x .

## History

The subdifferential on convex functions was introduced by Jean Jacques Moreau and R. Tyrrell Rockafellar in the early 1960s. The *generalized subdifferential* for nonconvex functions was introduced by Francis H. Clarke and R. Tyrrell Rockafellar in the early 1980s.

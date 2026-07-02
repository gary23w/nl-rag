---
title: "Wronskian"
source: https://en.wikipedia.org/wiki/Wronskian
domain: differential-equations-ode
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, laplace transform, linear differential equation
fetched: 2026-07-02
---

# Wronskian

In mathematics, the **Wronskian** of n differentiable functions is the determinant of a matrix formed by the functions and their derivatives up to order $n-1$ . It was introduced in 1812 by the Polish mathematician Józef Wroński, and is used in the study of differential equations, where it can show the linear independence of certain sets of solutions.

## Definition

The Wrońskian of two differentiable functions f and g is $W(f,g)=fg'-gf'$ .

More generally, for n real- or complex-valued functions $f_{1},\dots ,f_{n}$ , which are $n-1$ times differentiable on an interval I , the Wronskian $W(f_{1},\ldots ,f_{n})$ is the function

$W(f_{1},\ldots ,f_{n})(x)={\begin{vmatrix}f_{1}(x)&f_{2}(x)&\cdots &f_{n}(x)\\f_{1}'(x)&f_{2}'(x)&\cdots &f_{n}'(x)\\\vdots &\vdots &\ddots &\vdots \\f_{1}^{(n-1)}(x)&f_{2}^{(n-1)}(x)&\cdots &f_{n}^{(n-1)}(x)\end{vmatrix}}$

defined for all $x\in I$ .

This is the determinant of the matrix constructed by placing the functions in the first row, their first derivatives of the functions in the second row, and so on through the $(n-1)$ -st derivative, thus forming a square matrix.

When the functions are solutions of a linear differential equation, the Wrońskian can be found explicitly using Abel's identity, even if the functions themselves are not known explicitly. (See below.)

## The Wronskian and linear independence

If the functions are linearly dependent, then so are the columns of the Wrońskian (since differentiation is a linear operation), and the Wrońskian vanishes. Thus, one may show that a set of differentiable functions is linearly independent on an interval by showing that their Wrońskian does not vanish identically. It may, however, vanish at isolated points.

A common misconception is that $W=0$ everywhere implies linear dependence. Peano (1889) pointed out that the functions *x*2 and |*x*|***·** x* have continuous derivatives and their Wrońskian vanishes everywhere, yet they are not linearly dependent in any neighborhood of 0. There are several extra conditions which combine with vanishing of the Wronskian in an interval to imply linear dependence.

- Maxime Bôcher observed that if the functions are analytic, then the vanishing of the Wrońskian in an interval implies that they are linearly dependent.
- Bôcher (1901) gave several other conditions for the vanishing of the Wrońskian to imply linear dependence; for example, if the Wrońskian of *n* functions is identically zero and the *n* Wrońskians of *n* – 1 of them do not all vanish at any point then the functions are linearly dependent.
- Wolsson (1989a) gave a more general condition that together with the vanishing of the Wronskian implies linear dependence.

Over fields of characteristic p the Wronskian may vanish even for linearly independent polynomials; for example, the Wronskian of $x^{p}$ and the constant function 1 is identically zero.

## Application to linear differential equations

In general, for an n th order linear differential equation, if $n-1$ solutions are known, the last one can be determined by using the Wronskian.

Consider the second order differential equation in Lagrange's notation: $y''=a(x)y'+b(x)y$ where $a(x)$ , $b(x)$ are known, and y is the unknown function to be found. Let us call $y_{1},y_{2}$ the two solutions of the equation and form their Wronskian $W(x)=y_{1}y'_{2}-y_{2}y'_{1}$

Then differentiating $W(x)$ and using the fact that $y_{i}$ obey the above differential equation shows that $W'(x)=a(x)W(x)$

Therefore, the Wronskian obeys a simple first order differential equation and can be exactly solved: $W(x)=C~e^{A(x)}$ where $A'(x)=a(x)$ and C is a constant.

Now suppose that we know one of the solutions, say $y_{2}$ . Then, by the definition of the Wrońskian, $y_{1}$ obeys a first order differential equation: $y'_{1}-{\frac {y'_{2}}{y_{2}}}y_{1}=-W(x)/y_{2}$ and can be solved exactly (at least in theory).

The method is easily generalized to higher order equations.

The relationship between the Wronskian and linear independence can also be strengthened in the context of a differential equation. If we have n linearly independent functions that are all solutions of the same monic n th-order homogeneous-linear ordinary differential equation $y^{(n)}+Ly=0$ (where L is a linear differential operator with respect to x of order less than n ) on some interval I , then their Wronskian is zero *nowhere* on I . Thus, counterexamples like $x^{2}$ and $x{|x|}$ (whose Wronskian is zero everywhere) or even $x^{2}$ and 1 (whose Wronskian $2x$ is zero somewhere) are ruled out; neither pair can consist of solutions to the same second-order differential equation of this type. (It's true that $x^{2}$ and 1 are both solutions to the same *third*-order differential equation $y^{(3)}=0$ . But the Wronskian $-2$ of the *three* independent solutions $x^{2}$ , x , and 1 is nowhere zero.)

## Generalized Wronskians

For *n* functions of several variables, a **generalized Wronskian**is a determinant of an *n* by *n* matrix with entries *Di*(*fj*) (with 0 ≤ *i* < *n*), where each *Di* is some constant coefficient linear partial differential operator of order *i*. If the functions are linearly dependent then all generalized Wronskians vanish. As in the single variable case the converse is not true in general: if all generalized Wronskians vanish, this does not imply that the functions are linearly dependent. However, the converse is true in many special cases. For example, if the functions are polynomials and all generalized Wronskians vanish, then the functions are linearly dependent. Roth used this result about generalized Wronskians in his proof of Roth's theorem. For more general conditions under which the converse is valid see Wolsson (1989b).

## History

The Wrońskian was introduced by Józef Hoene-Wroński (1812) and given its current name by Thomas Muir (1882, Chapter XVIII).

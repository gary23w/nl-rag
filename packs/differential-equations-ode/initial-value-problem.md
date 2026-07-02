---
title: "Initial value problem"
source: https://en.wikipedia.org/wiki/Initial_value_problem
domain: differential-equations-ode
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, laplace transform, linear differential equation
fetched: 2026-07-02
---

# Initial value problem

In calculus, an **initial value problem** (**IVP**) is an ordinary differential equation together with an initial condition which specifies the value of the unknown function at a given point in the domain. Modeling a system in physics or other sciences frequently amounts to solving an initial value problem. In that context, the IVP is a differential equation which specifies how the system evolves with time plus the initial conditions of the problem.

## Definition

An **initial value problem** is a differential equation

$y'(t)=f(t,y(t))$

with

$f\colon \Omega \subset \mathbb {R} \times \mathbb {R} ^{n}\to \mathbb {R} ^{n}$

where

$\Omega$

is an

open set

of

$\mathbb {R} \times \mathbb {R} ^{n}$

,

together with a point in the domain of f

$(t_{0},y_{0})\in \Omega ,$

called the initial condition.

A **solution** to an initial value problem is a function y that is a solution to the differential equation and satisfies

$y(t_{0})=y_{0}.$

In higher dimensions, the differential equation is replaced with a family of equations $y_{i}'(t)=f_{i}(t,y_{1}(t),y_{2}(t),\dotsc )$ , and $y(t)$ is viewed as the vector $(y_{1}(t),\dotsc ,y_{n}(t))$ , most commonly associated with the position in space. More generally, the unknown function y can take values on infinite dimensional spaces, such as Banach spaces or spaces of distributions.

Initial value problems are extended to higher orders by treating the derivatives in the same way as an independent function, e.g. $y''(t)=f(t,y(t),y'(t))$ . For this second-order differential equation, two initial conditions are needed, for example the numerical values of $y(0)$ and $y'(0)$ .

## Existence and uniqueness of solutions

The Picard–Lindelöf theorem guarantees a unique solution on some interval containing *t*0 if *f* is continuous on a region containing *t*0 and *y*0 and satisfies the Lipschitz condition on the variable *y*. The proof of this theorem proceeds by reformulating the problem as an equivalent integral equation. The integral can be considered an operator which maps one function into another, such that the solution is a fixed point of the operator. The Banach fixed point theorem is then invoked to show that there exists a unique fixed point, which is the solution of the initial value problem.

An older proof of the Picard–Lindelöf theorem constructs a sequence of functions which converge to the solution of the integral equation, and thus, the solution of the initial value problem. Such a construction is sometimes called "Picard's method" or "the method of successive approximations". This version is essentially a special case of the Banach fixed point theorem.

Hiroshi Okamura obtained a necessary and sufficient condition for the solution of an initial value problem to be unique. This condition has to do with the existence of a Lyapunov function for the system.

In some situations, the function *f* is not of class *C*1, or even Lipschitz, so the usual result guaranteeing the local existence of a unique solution does not apply. The Peano existence theorem however proves that even for *f* merely continuous, solutions are guaranteed to exist locally in time; the problem is that there is no guarantee of uniqueness. The result may be found in Coddington & Levinson (1955, Theorem 1.3) or Robinson (2001, Theorem 2.6). An even more general result is the Carathéodory existence theorem, which proves existence for some discontinuous functions *f*.

## Examples

A simple example is to solve $y'(t)=0.85y(t)$ and $y(0)=19$ . We are trying to find a formula for $y(t)$ that satisfies these two equations.

Rearrange the equation so that y is on the left hand side

${\frac {y'(t)}{y(t)}}=0.85$

Now integrate both sides with respect to t (this introduces an unknown constant B ).

$\int {\frac {y'(t)}{y(t)}}\,dt=\int 0.85\,dt$

$\ln |y(t)|=0.85t+B$

Eliminate the logarithm with exponentiation on both sides

$|y(t)|=e^{B}e^{0.85t}$

Let C be a new unknown constant, $C=\pm e^{B}$ , so

$y(t)=Ce^{0.85t}$

Now we need to find a value for C . Use $y(0)=19$ as given at the start and substitute 0 for t and 19 for y

$19=Ce^{0.85\cdot 0}$

$C=19$

this gives the final solution of $y(t)=19e^{0.85t}$ .

**Second example**

The solution of

$y'+3y=6t+5,\qquad y(0)=3$

can be found to be

$y(t)=2e^{-3t}+2t+1.\,$

Indeed,

${\begin{aligned}y'+3y&={\tfrac {d}{dt}}(2e^{-3t}+2t+1)+3(2e^{-3t}+2t+1)\\&=(-6e^{-3t}+2)+(6e^{-3t}+6t+3)\\&=6t+5.\end{aligned}}$

and $y(0)=2+0+1=3$ , so the given function satisfies the ODE and the initial condition.

**Third example**

The solution of

$y'=y^{\frac {2}{3}},\qquad y(0)=0$

$\int {\frac {y'}{y^{\frac {2}{3}}}}\,dt=\int y^{-{\frac {2}{3}}}\,dy=\int 1\,dt$

$3(y(t))^{\frac {1}{3}}=t+B$

Applying initial conditions we get $B=0$ , hence the solution:

$y(t)={\frac {t^{3}}{27}}$ .

However, the following function is also a solution of the initial value problem:

$f(t)=\left\{{\begin{array}{lll}{\frac {(t-t_{1})^{3}}{27}}&{\text{if}}&t\leq t_{1}\\0&{\text{if}}&t_{1}\leq x\leq t_{2}\\{\frac {(t-t_{2})^{3}}{27}}&{\text{if}}&t_{2}\leq t\\\end{array}}\right.$

The function is differentiable everywhere and continuous, while satisfying the differential equation as well as the initial value problem. Thus, this is an example of such a problem with infinite number of solutions.

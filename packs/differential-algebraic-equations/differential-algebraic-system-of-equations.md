---
title: "Differential-algebraic system of equations"
source: https://en.wikipedia.org/wiki/Differential-algebraic_system_of_equations
domain: differential-algebraic-equations
license: CC-BY-SA-4.0
tags: differential-algebraic equations, backward differentiation formula, method of lines, runge-kutta methods
fetched: 2026-07-02
---

# Differential-algebraic system of equations

In mathematics, a **differential-algebraic system of equations** (**DAE**) is a system of equations that either contains differential equations and algebraic equations, or is equivalent to such a system.

The set of the solutions of such a system is a *differential algebraic variety*, and corresponds to an ideal in a differential algebra of differential polynomials.

In the univariate case, a DAE in the variable *t* can be written as a single equation of the form

$F({\dot {x}},x,t)=0,$

where $x(t)$ is a vector of unknown functions and the overdot denotes the time derivative, i.e., ${\dot {x}}={\frac {dx}{dt}}$ .

They are distinct from ordinary differential equation (ODE) in that a DAE is not completely solvable for the derivatives of all components of the function *x* because these may not all appear (i.e. some equations are algebraic); technically the distinction between an implicit ODE system [that may be rendered explicit] and a DAE system is that the Jacobian matrix ${\frac {\partial F({\dot {x}},x,t)}{\partial {\dot {x}}}}$ is a singular matrix for a DAE system. This distinction between ODEs and DAEs is made because DAEs have different characteristics and are generally more difficult to solve.

In practical terms, the distinction between DAEs and ODEs is often that the solution of a DAE system depends on the derivatives of the input signal and not just the signal itself as in the case of ODEs; this issue is commonly encountered in nonlinear systems with hysteresis, such as the Schmitt trigger.

This difference is more clearly visible if the system may be rewritten so that instead of *x* we consider a pair $(x,y)$ of vectors of dependent variables and the DAE has the form

${\begin{aligned}{\dot {x}}(t)&=f(x(t),y(t),t),\\0&=g(x(t),y(t),t).\end{aligned}}$

where

$x(t)\in \mathbb {R} ^{n}$

,

$y(t)\in \mathbb {R} ^{m}$

,

$f:\mathbb {R} ^{n+m+1}\to \mathbb {R} ^{n}$

and

$g:\mathbb {R} ^{n+m+1}\to \mathbb {R} ^{m}.$

A DAE system of this form is called *semi-explicit*. Every solution of the second half *g* of the equation defines a unique direction for *x* via the first half *f* of the equations, while the direction for *y* is arbitrary. But not every point *(x,y,t)* is a solution of *g*. The variables in *x* and the first half *f* of the equations get the attribute *differential*. The components of *y* and the second half *g* of the equations are called the *algebraic* variables or equations of the system. [The term *algebraic* in the context of DAEs only means *free of derivatives* and is not related to (abstract) algebra.]

The solution of a DAE consists of two parts, first the search for consistent initial values and second the computation of a trajectory. To find consistent initial values it is often necessary to consider the derivatives of some of the component functions of the DAE. The highest order of a derivative that is necessary for this process is called the *differentiation index*. The equations derived in computing the index and consistent initial values may also be of use in the computation of the trajectory. A semi-explicit DAE system can be converted to an implicit one by decreasing the differentiation index by one, and vice versa.

## Other forms of DAEs

The distinction of DAEs to ODEs becomes apparent if some of the dependent variables occur without their derivatives. The vector of dependent variables may then be written as pair $(x,y)$ and the system of differential equations of the DAE appears in the form

$F\left({\dot {x}},x,y,t\right)=0$

where

- x , a vector in $\mathbb {R} ^{n}$ , are dependent variables for which derivatives are present (*differential variables*),
- y , a vector in $\mathbb {R} ^{m}$ , are dependent variables for which no derivatives are present (*algebraic variables*),
- t , a scalar (usually time) is an independent variable.
- F is a vector of $n+m$ functions that involve subsets of these $n+m+1$ variables and n derivatives.

As a whole, the set of DAEs is a function

$F:\mathbb {R} ^{(2n+m+1)}\to \mathbb {R} ^{(n+m)}.$

Initial conditions must be a solution of the system of equations of the form

$F\left({\dot {x}}(t_{0}),\,x(t_{0}),y(t_{0}),t_{0}\right)=0.$

## Examples

The behaviour of a pendulum of length *L* with center in (0,0) in Cartesian coordinates (*x*,*y*) is described by the Euler–Lagrange equations

${\begin{aligned}{\dot {x}}&=u,&{\dot {y}}&=v,\\{\dot {u}}&=\lambda x,&{\dot {v}}&=\lambda y-g,\\x^{2}+y^{2}&=L^{2},\end{aligned}}$

where $\lambda$ is a Lagrange multiplier. The momentum variables *u* and *v* should be constrained by the law of conservation of energy and their direction should point along the circle. Neither condition is explicit in those equations. Differentiation of the last equation leads to

${\begin{aligned}&&{\dot {x}}\,x+{\dot {y}}\,y&=0\\\Rightarrow &&u\,x+v\,y&=0,\end{aligned}}$

restricting the direction of motion to the tangent of the circle. The next derivative of this equation implies

${\begin{aligned}&&{\dot {u}}\,x+{\dot {v}}\,y+u\,{\dot {x}}+v\,{\dot {y}}&=0,\\\Rightarrow &&\lambda (x^{2}+y^{2})-gy+u^{2}+v^{2}&=0,\\\Rightarrow &&L^{2}\,\lambda -gy+u^{2}+v^{2}&=0,\end{aligned}}$

and the derivative of that last identity simplifies to $L^{2}{\dot {\lambda }}-3gv=0$ which implies the conservation of energy since after integration the constant $E={\tfrac {3}{2}}gy-{\tfrac {1}{2}}L^{2}\lambda ={\frac {1}{2}}(u^{2}+v^{2})+gy$ is the sum of kinetic and potential energy.

To obtain unique derivative values for all dependent variables the last equation was three times differentiated. This gives a differentiation index of 3, which is typical for constrained mechanical systems.

If initial values $(x_{0},u_{0})$ and a sign for *y* are given, the other variables are determined via $y=\pm {\sqrt {L^{2}-x^{2}}}$ , and if $y\neq 0$ then $v=-ux/y$ and $\lambda =(gy-u^{2}-v^{2})/L^{2}$ . To proceed to the next point it is sufficient to get the derivatives of *x* and *u*, that is, the system to solve is now

${\begin{aligned}{\dot {x}}&=u,\\{\dot {u}}&=\lambda x,\\[0.3em]0&=x^{2}+y^{2}-L^{2},\\0&=ux+vy,\\0&=u^{2}-gy+v^{2}+L^{2}\,\lambda .\end{aligned}}$

This is a semi-explicit DAE of index 1. Another set of similar equations may be obtained starting from $(y_{0},v_{0})$ and a sign for *x*.

DAEs also naturally occur in the modelling of circuits with non-linear devices. Modified nodal analysis employing DAEs is used for example in the ubiquitous SPICE family of numeric circuit simulators. Similarly, Fraunhofer's Analog Insydes Mathematica package can be used to derive DAEs from a netlist and then simplify or even solve the equations symbolically in some cases. It is worth noting that the index of a DAE (of a circuit) can be made arbitrarily high by cascading/coupling via capacitors operational amplifiers with positive feedback.

## Semi-explicit DAE of index 1

DAE of the form

${\begin{aligned}{\dot {x}}&=f(x,y,t),\\0&=g(x,y,t).\end{aligned}}$

are called semi-explicit. The index-1 property requires that *g* is solvable for *y*. In other words, the differentiation index is 1 if by differentiation of the algebraic equations for *t* an implicit ODE system results,

${\begin{aligned}{\dot {x}}&=f(x,y,t)\\0&=\partial _{x}g(x,y,t){\dot {x}}+\partial _{y}g(x,y,t){\dot {y}}+\partial _{t}g(x,y,t),\end{aligned}}$

which is solvable for $({\dot {x}},\,{\dot {y}})$ if $\det \left(\partial _{y}g(x,y,t)\right)\neq 0.$

Every sufficiently smooth DAE is almost everywhere reducible to this semi-explicit index-1 form.

## Numerical treatment of DAE and applications

Two major problems in solving DAEs are *index reduction* and *consistent initial conditions*. Most numerical solvers require ordinary differential equations and algebraic equations of the form

${\begin{aligned}{\frac {dx}{dt}}&=f\left(x,y,t\right),\\0&=g\left(x,y,t\right).\end{aligned}}$

It is a non-trivial task to convert arbitrary DAE systems into ODEs for solution by pure ODE solvers. Techniques which can be employed include *Pantelides algorithm* and *dummy derivative index reduction method*. Alternatively, a direct solution of high-index DAEs with inconsistent initial conditions is also possible. This solution approach involves a transformation of the derivative elements through *orthogonal collocation on finite elements* or *direct transcription* into algebraic expressions. This allows DAEs of any index to be solved without rearrangement in the open equation form

${\begin{aligned}0&=f\left({\frac {dx}{dt}},x,y,t\right),\\0&=g\left(x,y,t\right).\end{aligned}}$

Once the model has been converted to algebraic equation form, it is solvable by large-scale nonlinear programming solvers (see APMonitor).

### Tractability

Several measures of DAEs tractability in terms of numerical methods have developed, such as *differentiation index*, *perturbation index*, *tractability index*, *geometric index*, and the *Kronecker index*.

## Structural analysis for DAEs

We use the $\Sigma$ -method to analyze a DAE. We construct for the DAE a signature matrix $\Sigma =(\sigma _{i,j})$ , where each row corresponds to each equation $f_{i}$ and each column corresponds to each variable $x_{j}$ . The entry in position $(i,j)$ is $\sigma _{i,j}$ , which denotes the highest order of derivative to which $x_{j}$ occurs in $f_{i}$ , or $-\infty$ if $x_{j}$ does not occur in $f_{i}$ .

For the pendulum DAE above, the variables are $(x_{1},x_{2},x_{3},x_{4},x_{5})=(x,y,u,v,\lambda )$ . The corresponding signature matrix is

$\Sigma ={\begin{bmatrix}1&-&0^{\bullet }&-&-\\-&1^{\bullet }&-&0&-\\0&-&1&-&0^{\bullet }\\-&0&-&1^{\bullet }&0\\0^{\bullet }&0&-&-&-\end{bmatrix}}$

---
title: "Finite difference method"
source: https://en.wikipedia.org/wiki/Finite_difference_method
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Finite difference method

In numerical analysis, **finite-difference methods** (**FDM**) are a class of numerical techniques for solving differential equations by approximating derivatives with finite differences. Both the spatial domain and time domain (if applicable) are discretized, or broken into a finite number of intervals, and the values of the solution at the end points of the intervals are approximated by solving algebraic equations containing finite differences and values from nearby points.

Finite difference methods convert ordinary differential equations (ODE) or partial differential equations (PDE), which may be nonlinear, into a system of linear equations that can be solved by matrix algebra techniques. Modern computers can perform these linear algebra computations efficiently, and this, along with their relative ease of implementation, has led to the widespread use of FDM in modern numerical analysis. Today, FDMs are one of the most common approaches to the numerical solution of PDE, along with finite element methods.

## Derive difference quotient from Taylor's polynomial

For a *n*-times differentiable function, by Taylor's theorem the Taylor series expansion is given as $f(x_{0}+h)=f(x_{0})+{\frac {f'(x_{0})}{1!}}h+{\frac {f^{(2)}(x_{0})}{2!}}h^{2}+\cdots +{\frac {f^{(n)}(x_{0})}{n!}}h^{n}+R_{n}(x),$

Where *n*! denotes the factorial of *n*, and *R**n*(*x*) is a remainder term, denoting the difference between the Taylor polynomial of degree *n* and the original function.

Following is the process to derive an approximation for the first derivative of the function *f* by first truncating the Taylor polynomial plus remainder: $f(x_{0}+h)=f(x_{0})+f'(x_{0})h+R_{1}(x).$ Dividing across by *h* gives: ${f(x_{0}+h) \over h}={f(x_{0}) \over h}+f'(x_{0})+{R_{1}(x) \over h}$ Solving for $f'(x_{0})$ : $f'(x_{0})={f(x_{0}+h)-f(x_{0}) \over h}-{R_{1}(x) \over h}.$

Assuming that $R_{1}(x)$ is sufficiently small, the approximation of the first derivative of *f* is: $f'(x_{0})\approx {f(x_{0}+h)-f(x_{0}) \over h}.$

This is similar to the definition of derivative, which is: $f'(x_{0})=\lim _{h\to 0}{\frac {f(x_{0}+h)-f(x_{0})}{h}}.$ except for the limit towards zero (the method is named after this).

## Accuracy and order

The error in a method's solution is defined as the difference between the approximation and the exact analytical solution. The two sources of error in finite difference methods are round-off error, the loss of precision due to computer rounding of decimal quantities, and truncation error or discretization error, the difference between the exact solution of the original differential equation and the exact quantity assuming perfect arithmetic (no round-off).

To use a finite difference method to approximate the solution to a problem, one must first discretize the problem's domain. This is usually done by dividing the domain into a uniform grid (see image). This means that finite-difference methods produce sets of discrete numerical approximations to the derivative, often in a "time-stepping" manner.

An expression of general interest is the local truncation error of a method. Typically expressed using Big-O notation, local truncation error refers to the error from a single application of a method. That is, it is the quantity $f'(x_{i})-f'_{i}$ if $f'(x_{i})$ refers to the exact value and $f'_{i}$ to the numerical approximation. The remainder term of the Taylor polynomial can be used to analyze local truncation error. Using the Lagrange form of the remainder from the Taylor polynomial for $f(x_{0}+h)$ , which is $R_{n}(x_{0}+h)={\frac {f^{(n+1)}(\xi )}{(n+1)!}}(h)^{n+1}\,,\quad x_{0}<\xi <x_{0}+h,$ the dominant term of the local truncation error can be discovered. For example, again using the forward-difference formula for the first derivative, knowing that $f(x_{i})=f(x_{0}+ih)$ , $f(x_{0}+ih)=f(x_{0})+f'(x_{0})ih+{\frac {f''(\xi )}{2!}}(ih)^{2},$ and with some algebraic manipulation, this leads to ${\frac {f(x_{0}+ih)-f(x_{0})}{ih}}=f'(x_{0})+{\frac {f''(\xi )}{2!}}ih,$ and further noting that the quantity on the left is the approximation from the finite difference method and that the quantity on the right is the exact quantity of interest plus a remainder, clearly that remainder is the local truncation error. A final expression of this example and its order is: ${\frac {f(x_{0}+ih)-f(x_{0})}{ih}}=f'(x_{0})+O(h).$

In this case, the local truncation error is proportional to the step sizes. The quality and duration of simulated FDM solution depends on the discretization equation selection and the step sizes (time and space steps). The data quality and simulation duration increase significantly with smaller step size. Therefore, a reasonable balance between data quality and simulation duration is necessary for practical usage. Large time steps are useful for increasing simulation speed in practice. However, time steps which are too large may create instabilities and affect the data quality.

The von Neumann and Courant-Friedrichs-Lewy criteria are often evaluated to determine the numerical model stability.

## Example: ordinary differential equation

For example, consider the ordinary differential equation $u'(x)=3u(x)+2.$ The Euler method for solving this equation uses the finite difference quotient ${\frac {u(x+h)-u(x)}{h}}\approx u'(x)$ to approximate the differential equation by first substituting it for $u'(x)$ then applying a little algebra (multiplying both sides by *h*, and then adding $u(x)$ to both sides) to get $u(x+h)\approx u(x)+h(3u(x)+2).$ The last equation is a finite-difference equation, and solving this equation gives an approximate solution to the differential equation.

## Example: The heat equation

Consider the normalized heat equation in one dimension, with homogeneous Dirichlet boundary conditions

${\begin{cases}U_{t}=U_{xx}\\U(0,t)=U(1,t)=0&{\text{(boundary condition)}}\\U(x,0)=U_{0}(x)&{\text{(initial condition)}}\end{cases}}$

One way to numerically solve this equation is to approximate all the derivatives by finite differences. First partition the domain in space using a mesh $x_{0},\dots ,x_{J}$ and in time using a mesh $t_{0},\dots ,t_{N}$ . Assume a uniform partition both in space and in time, so the difference between two consecutive space points will be *h* and between two consecutive time points will be *k*. The points

$u(x_{j},t_{n})=u_{j}^{n}$

will represent the numerical approximation of $u(x_{j},t_{n}).$

### Explicit method

Using a forward difference **at time $t_{n}$** and a second-order central difference for the space derivative at position $x_{j}$ (FTCS) gives the recurrence equation:

${\frac {u_{j}^{n+1}-u_{j}^{n}}{k}}={\frac {u_{j+1}^{n}-2u_{j}^{n}+u_{j-1}^{n}}{h^{2}}}.$

This is an explicit method for solving the one-dimensional heat equation.

One can obtain $u_{j}^{n+1}$ from the other values this way:

$u_{j}^{n+1}=(1-2r)u_{j}^{n}+ru_{j-1}^{n}+ru_{j+1}^{n}$

where $r=k/h^{2}.$

So, with this recurrence relation, and knowing the values at time *n*, one can obtain the corresponding values at time *n*+1. $u_{0}^{n}$ and $u_{J}^{n}$ must be replaced by the boundary conditions, in this example they are both 0.

This explicit method is known to be numerically stable and convergent whenever $r\leq 1/2$ . The numerical errors are proportional to the time step and the square of the space step: $\Delta u=O(k)+O(h^{2})$

### Implicit method

Using the backward difference **at time $t_{n+1}$** and a second-order central difference for the space derivative at position $x_{j}$ (The Backward Time, Centered Space Method "BTCS") gives the recurrence equation:

${\frac {u_{j}^{n+1}-u_{j}^{n}}{k}}={\frac {u_{j+1}^{n+1}-2u_{j}^{n+1}+u_{j-1}^{n+1}}{h^{2}}}.$

This is an implicit method for solving the one-dimensional heat equation.

One can obtain $u_{j}^{n+1}$ from solving a system of linear equations:

$(1+2r)u_{j}^{n+1}-ru_{j-1}^{n+1}-ru_{j+1}^{n+1}=u_{j}^{n}$

The scheme is always numerically stable and convergent but usually more numerically intensive than the explicit method as it requires solving a system of numerical equations on each time step. The errors are linear over the time step and quadratic over the space step: $\Delta u=O(k)+O(h^{2}).$

### Crank–Nicolson method

Finally, using the central difference at time $t_{n+1/2}$ and a second-order central difference for the space derivative at position $x_{j}$ ("CTCS") gives the recurrence equation:

${\frac {u_{j}^{n+1}-u_{j}^{n}}{k}}={\frac {1}{2}}\left({\frac {u_{j+1}^{n+1}-2u_{j}^{n+1}+u_{j-1}^{n+1}}{h^{2}}}+{\frac {u_{j+1}^{n}-2u_{j}^{n}+u_{j-1}^{n}}{h^{2}}}\right).$

This formula is known as the Crank–Nicolson method.

One can obtain $u_{j}^{n+1}$ from solving a system of linear equations:

$(2+2r)u_{j}^{n+1}-ru_{j-1}^{n+1}-ru_{j+1}^{n+1}=(2-2r)u_{j}^{n}+ru_{j-1}^{n}+ru_{j+1}^{n}$

The scheme is always numerically stable and convergent but usually more numerically intensive as it requires solving a system of numerical equations on each time step. The errors are quadratic over both the time step and the space step: $\Delta u=O(k^{2})+O(h^{2}).$

### Comparison

To summarize, usually the Crank–Nicolson scheme is the most accurate scheme for small time steps. For larger time steps, the implicit scheme works better since it is less computationally demanding. The explicit scheme is the least accurate and can be unstable, but is also the easiest to implement and the least numerically intensive.

Here is an example. The figures below present the solutions given by the above methods to approximate the heat equation

$U_{t}=\alpha U_{xx},\quad \alpha ={\frac {1}{\pi ^{2}}},$

with the boundary condition

$U(0,t)=U(1,t)=0.$

The exact solution is

$U(x,t)={\frac {1}{\pi ^{2}}}e^{-t}\sin(\pi x).$

Comparison of Finite Difference Methods

Explicit method (

not

stable)

Implicit method (stable)

Crank-Nicolson method (stable)

## Example: The Laplace operator

The (continuous) Laplace operator in n -dimensions is given by $\Delta u(x)=\sum _{i=1}^{n}\partial _{i}^{2}u(x)$ . The discrete Laplace operator $\Delta _{h}u$ depends on the dimension n .

In 1D the Laplace operator is approximated as $\Delta u(x)=u''(x)\approx {\frac {u(x-h)-2u(x)+u(x+h)}{h^{2}}}=:\Delta _{h}u(x)\,.$ This approximation is usually expressed via the following stencil $\Delta _{h}={\frac {1}{h^{2}}}{\begin{bmatrix}1&-2&1\end{bmatrix}}$ and which represents a symmetric, tridiagonal matrix. For an equidistant grid one gets a Toeplitz matrix.

The 2D case shows all the characteristics of the more general n-dimensional case. Each second partial derivative needs to be approximated similar to the 1D case ${\begin{aligned}\Delta u(x,y)&=u_{xx}(x,y)+u_{yy}(x,y)\\&\approx {\frac {u(x-h,y)-2u(x,y)+u(x+h,y)}{h^{2}}}+{\frac {u(x,y-h)-2u(x,y)+u(x,y+h)}{h^{2}}}\\&={\frac {u(x-h,y)+u(x+h,y)-4u(x,y)+u(x,y-h)+u(x,y+h)}{h^{2}}}\\&=:\Delta _{h}u(x,y)\,,\end{aligned}}$ which is usually given by the following stencil $\Delta _{h}={\frac {1}{h^{2}}}{\begin{bmatrix}&1\\1&-4&1\\&1\end{bmatrix}}\,.$

### Consistency

Consistency of the above-mentioned approximation can be shown for highly regular functions, such as $u\in C^{4}(\Omega )$ . The statement is $\Delta u-\Delta _{h}u={\mathcal {O}}(h^{2})\,.$

To prove this, one needs to substitute Taylor Series expansions up to order 3 into the discrete Laplace operator.

### Properties

#### Subharmonic

Similar to continuous subharmonic functions one can define *subharmonic functions* for finite-difference approximations $u_{h}$ $-\Delta _{h}u_{h}\leq 0\,.$

#### Mean value

One can define a general stencil of *positive type* via ${\begin{bmatrix}&\alpha _{N}\\\alpha _{W}&-\alpha _{C}&\alpha _{E}\\&\alpha _{S}\end{bmatrix}}\,,\quad \alpha _{i}>0\,,\quad \alpha _{C}=\sum _{i\in \{N,E,S,W\}}\alpha _{i}\,.$

If $u_{h}$ is (discrete) subharmonic then the following*mean value property* holds $u_{h}(x_{C})\leq {\frac {\sum _{i\in \{N,E,S,W\}}\alpha _{i}u_{h}(x_{i})}{\sum _{i\in \{N,E,S,W\}}\alpha _{i}}}\,,$ where the approximation is evaluated on points of the grid, and the stencil is assumed to be of positive type.

A similar mean value property also holds for the continuous case.

#### Maximum principle

For a (discrete) subharmonic function $u_{h}$ the following holds $\max _{\Omega _{h}}u_{h}\leq \max _{\partial \Omega _{h}}u_{h}\,,$ where $\Omega _{h},\partial \Omega _{h}$ are discretizations of the continuous domain $\Omega$ , respectively the boundary $\partial \Omega$ .

A similar maximum principle also holds for the continuous case.

## The SBP-SAT method

The SBP-SAT (*summation by parts - simultaneous approximation term*) method is a stable and accurate technique for discretizing and imposing boundary conditions of a well-posed linear partial differential equation using high order finite differences.

The method is based on finite differences where the differentiation operators exhibit summation-by-parts properties. Typically, these operators consist of differentiation matrices with central difference stencils in the interior with carefully chosen one-sided boundary stencils designed to mimic integration-by-parts in the discrete setting. Using the SAT technique, the boundary conditions of the PDE are imposed weakly, where the boundary values are "pulled" towards the desired conditions rather than exactly fulfilled. If the tuning parameters (inherent to the SAT technique) are chosen properly, the resulting system of ODE's will exhibit similar energy behavior as the continuous PDE, i.e. the system has no non-physical energy growth. This guarantees stability if an integration scheme with a stability region that includes parts of the imaginary axis, such as the fourth order Runge-Kutta method, is used. This makes the SAT technique an attractive method of imposing boundary conditions for higher order finite difference methods, in contrast to for example the injection method, which typically will not be stable if high order differentiation operators are used. The additive formulation of the SAT terms can simplify the efficient implementations of this method on GPUs or other modern high performance architectures by treating boundary conditions as separate correction terms, in contrast to finite difference methods that impose boundary conditions through direct injection of boundary data.

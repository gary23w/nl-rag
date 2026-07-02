---
title: "Crank–Nicolson method"
source: https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Crank–Nicolson method

In numerical analysis, the **Crank–Nicolson method** is a finite difference method used for numerically solving the heat equation and similar partial differential equations. It is a second-order method in time. It is implicit in time, can be written as an implicit Runge–Kutta method, and it is numerically stable. The method was developed by John Crank and Phyllis Nicolson in the 1940s.

For diffusion equations (and many other equations), it can be shown the Crank–Nicolson method is unconditionally stable. However, the approximate solutions can still contain (decaying) spurious oscillations if the ratio of time step $\Delta t$ times the thermal diffusivity to the square of space step, $\Delta x^{2}$ , is large (typically, larger than 1/2 per Von Neumann stability analysis). For this reason, whenever large time steps or high spatial resolution is necessary, the less accurate backward Euler method is often used, which is both stable and immune to oscillations.

## Principle

The Crank–Nicolson method is based on the trapezoidal rule, giving second-order convergence in time. For linear equations, the trapezoidal rule is equivalent to the implicit midpoint method—the simplest example of a Gauss–Legendre implicit Runge–Kutta method—which also has the property of being a geometric integrator. For example, in one dimension, suppose the partial differential equation is ${\frac {\partial u}{\partial t}}=F\left(u,x,t,{\frac {\partial u}{\partial x}},{\frac {\partial ^{2}u}{\partial x^{2}}}\right).$

Letting $u(i\Delta x,n\Delta t)=u_{i}^{n}$ and $F_{i}^{n}=F$ evaluated for $i,n$ and $u_{i}^{n}$ , the equation for Crank–Nicolson method is a combination of the forward Euler method at n and the backward Euler method at $n+1$ (note, however, that the method itself is *not* simply the average of those two methods, as the backward Euler equation has an implicit dependence on the solution):

| ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}=F_{i}^{n}\left(u,x,t,{\frac {\partial u}{\partial x}},{\frac {\partial ^{2}u}{\partial x^{2}}}\right)$ | forward Euler |
|---|---|
| ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}=F_{i}^{n+1}\left(u,x,t,{\frac {\partial u}{\partial x}},{\frac {\partial ^{2}u}{\partial x^{2}}}\right)$ | backward Euler |
| ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}={\frac {1}{2}}\left[F_{i}^{n+1}\left(u,x,t,{\frac {\partial u}{\partial x}},{\frac {\partial ^{2}u}{\partial x^{2}}}\right)+F_{i}^{n}\left(u,x,t,{\frac {\partial u}{\partial x}},{\frac {\partial ^{2}u}{\partial x^{2}}}\right)\right]$ | Crank–Nicolson |

Note that this is an *implicit method*: to get the "next" value of u in time, a system of algebraic equations must be solved. If the partial differential equation is nonlinear, the discretization will also be nonlinear, so that advancing in time will involve the solution of a system of nonlinear algebraic equations, though linearizations are possible. In many problems, especially linear diffusion, the algebraic problem is tridiagonal and may be efficiently solved with the tridiagonal matrix algorithm, which gives a fast ${\mathcal {O}}(N)$ direct solution, as opposed to the usual ${\mathcal {O}}(N^{3})$ for a full matrix, in which N indicates the matrix size.

## Example: 1D diffusion

The Crank–Nicolson method is often applied to diffusion problems. As an example, for linear diffusion,

${\frac {\partial u}{\partial t}}=a{\frac {\partial ^{2}u}{\partial x^{2}}},$

applying a finite difference spatial discretization for the right-hand side, the Crank–Nicolson discretization is then

${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}={\frac {a}{2(\Delta x)^{2}}}\left((u_{i+1}^{n+1}-2u_{i}^{n+1}+u_{i-1}^{n+1})+(u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n})\right)$

or, letting $r={\frac {a\Delta t}{2(\Delta x)^{2}}}$ ,

$-ru_{i+1}^{n+1}+(1+2r)u_{i}^{n+1}-ru_{i-1}^{n+1}=ru_{i+1}^{n}+(1-2r)u_{i}^{n}+ru_{i-1}^{n}.$

Given that the terms on the right-hand side of the equation are known, this is a tridiagonal problem, so that $u_{i}^{n+1}$ may be efficiently solved by using the tridiagonal matrix algorithm in favor over the much more costly matrix inversion.

A quasilinear equation, such as (this is a minimalistic example and not general)

${\frac {\partial u}{\partial t}}=a(u){\frac {\partial ^{2}u}{\partial x^{2}}},$

would lead to a nonlinear system of algebraic equations, which could not be easily solved as above; however, it is possible in some cases to linearize the problem by using the old value for a , that is, $a_{i}^{n}(u)$ instead of $a_{i}^{n+1}(u)$ . Other times, it may be possible to estimate $a_{i}^{n+1}(u)$ using an explicit method and maintain stability.

## Example: 1D diffusion with advection for steady flow, with multiple channel connections

This is a solution usually employed for many purposes when there is a contamination problem in streams or rivers under steady flow conditions, but information is given in one dimension only. Often the problem can be simplified into a 1-dimensional problem and still yield useful information.

Here we model the concentration of a solute contaminant in water. This problem is composed of three parts: the known diffusion equation ( $D_{x}$ chosen as constant), an advective component (which means that the system is evolving in space due to a velocity field), which we choose to be a constant $U_{x}$ , and a lateral interaction between longitudinal channels ( k ):

| ${\frac {\partial C}{\partial t}}=D_{x}{\frac {\partial ^{2}C}{\partial x^{2}}}-U_{x}{\frac {\partial C}{\partial x}}-k(C-C_{N})-k(C-C_{M}),$ |   | 1 |
|---|---|---|

where C is the concentration of the contaminant, and subscripts N and M correspond to *previous* and *next* channel.

The Crank–Nicolson method (where i represents position, and j time) transforms each component of the PDE into the following:

| ${\frac {\partial C}{\partial t}}\Rightarrow {\frac {C_{i}^{j+1}-C_{i}^{j}}{\Delta t}},$ |   | 2 |
|---|---|---|

| ${\frac {\partial ^{2}C}{\partial x^{2}}}\Rightarrow {\frac {1}{2(\Delta x)^{2}}}\left((C_{i+1}^{j+1}-2C_{i}^{j+1}+C_{i-1}^{j+1})+(C_{i+1}^{j}-2C_{i}^{j}+C_{i-1}^{j})\right),$ |   | 3 |
|---|---|---|

| ${\frac {\partial C}{\partial x}}\Rightarrow {\frac {1}{2}}\left({\frac {(C_{i+1}^{j+1}-C_{i-1}^{j+1})}{2(\Delta x)}}+{\frac {(C_{i+1}^{j}-C_{i-1}^{j})}{2(\Delta x)}}\right),$ |   | 4 |
|---|---|---|

| $C\Rightarrow {\frac {1}{2}}(C_{i}^{j+1}+C_{i}^{j}),$ |   | 5 |
|---|---|---|

| $C_{N}\Rightarrow {\frac {1}{2}}(C_{Ni}^{j+1}+C_{Ni}^{j}),$ |   | 6 |
|---|---|---|

| $C_{M}\Rightarrow {\frac {1}{2}}(C_{Mi}^{j+1}+C_{Mi}^{j}).$ |   | 7 |
|---|---|---|

Now we create the following constants to simplify the algebra:

$\lambda ={\frac {D_{x}\,\Delta t}{2\,\Delta x^{2}}},$

$\alpha ={\frac {U_{x}\,\Delta t}{4\,\Delta x}},$

$\beta ={\frac {k\,\Delta t}{2}},$

and substitute (**2**), (**3**), (**4**), (**5**), (**6**), (**7**), $\alpha$ , $\beta$ and $\lambda$ into (**1**). We then put the *new time* terms on the left ( $j+1$ ) and the *present time* terms on the right ( j ) to get

$-\beta C_{Ni}^{j+1}-(\lambda +\alpha )C_{i-1}^{j+1}+(1+2\lambda +2\beta )C_{i}^{j+1}-(\lambda -\alpha )C_{i+1}^{j+1}-\beta C_{Mi}^{j+1}={}$

$\qquad \beta C_{Ni}^{j}+(\lambda +\alpha )C_{i-1}^{j}+(1-2\lambda -2\beta )C_{i}^{j}+(\lambda -\alpha )C_{i+1}^{j}+\beta C_{Mi}^{j}.$

To model the *first* channel, we realize that it can only be in contact with the following channel ( M ), so the expression is simplified to

$-(\lambda +\alpha )C_{i-1}^{j+1}+(1+2\lambda +\beta )C_{i}^{j+1}-(\lambda -\alpha )C_{i+1}^{j+1}-\beta C_{Mi}^{j+1}={}$

$\qquad {}+(\lambda +\alpha )C_{i-1}^{j}+(1-2\lambda -\beta )C_{i}^{j}+(\lambda -\alpha )C_{i+1}^{j}+\beta C_{Mi}^{j}.$

In the same way, to model the *last* channel, we realize that it can only be in contact with the previous channel ( N ), so the expression is simplified to

$-\beta C_{Ni}^{j+1}-(\lambda +\alpha )C_{i-1}^{j+1}+(1+2\lambda +\beta )C_{i}^{j+1}-(\lambda -\alpha )C_{i+1}^{j+1}={}$

$\qquad \beta C_{Ni}^{j}+(\lambda +\alpha )C_{i-1}^{j}+(1-2\lambda -\beta )C_{i}^{j}+(\lambda -\alpha )C_{i+1}^{j}.$

To solve this linear system of equations, we must now see that boundary conditions must be given first to the beginning of the channels:

$C_{0}^{j}$

: boundary condition for the channel at present time step,

$C_{0}^{j+1}$

: boundary condition for the channel at next time step,

$C_{N0}^{j}$

: boundary condition for the previous channel to the one analyzed at present time step,

$C_{M0}^{j}$

: boundary condition for the next channel to the one analyzed at present time step.

For the last cell of the channels ( z ), the most convenient condition becomes an adiabatic one, so

$\left.{\frac {\partial C}{\partial x}}\right|_{x=z}={\frac {C_{i+1}-C_{i-1}}{2\,\Delta x}}=0.$

This condition is satisfied if and only if (regardless of a null value)

$C_{i+1}^{j+1}=C_{i-1}^{j+1}.$

Let us solve this problem (in a matrix form) for the case of 3 channels and 5 nodes (including the initial boundary condition). We express this as a linear system problem:

$\mathbf {AA} \,\mathbf {C^{j+1}} =\mathbf {BB} \,\mathbf {C^{j}} +\mathbf {d} ,$

where

$\mathbf {C^{j+1}} ={\begin{bmatrix}C_{11}^{j+1}\\C_{12}^{j+1}\\C_{13}^{j+1}\\C_{14}^{j+1}\\C_{21}^{j+1}\\C_{22}^{j+1}\\C_{23}^{j+1}\\C_{24}^{j+1}\\C_{31}^{j+1}\\C_{32}^{j+1}\\C_{33}^{j+1}\\C_{34}^{j+1}\end{bmatrix}},\quad \mathbf {C^{j}} ={\begin{bmatrix}C_{11}^{j}\\C_{12}^{j}\\C_{13}^{j}\\C_{14}^{j}\\C_{21}^{j}\\C_{22}^{j}\\C_{23}^{j}\\C_{24}^{j}\\C_{31}^{j}\\C_{32}^{j}\\C_{33}^{j}\\C_{34}^{j}\end{bmatrix}}.$

Now we must realize that **AA** and **BB** should be arrays made of four different subarrays (remember that only three channels are considered for this example, but it covers the main part discussed above):

$\mathbf {AA} ={\begin{bmatrix}AA1&AA3&0\\AA3&AA2&AA3\\0&AA3&AA1\end{bmatrix}},\quad \mathbf {BB} ={\begin{bmatrix}BB1&-AA3&0\\-AA3&BB2&-AA3\\0&-AA3&BB1\end{bmatrix}},$

where the elements mentioned above correspond to the next arrays, and an additional 4×4 full of zeros. Please note that the sizes of AA and BB are 12×12:

$\mathbf {AA1} ={\begin{bmatrix}(1+2\lambda +\beta )&-(\lambda -\alpha )&0&0\\-(\lambda +\alpha )&(1+2\lambda +\beta )&-(\lambda -\alpha )&0\\0&-(\lambda +\alpha )&(1+2\lambda +\beta )&-(\lambda -\alpha )\\0&0&-2\lambda &(1+2\lambda +\beta )\end{bmatrix}},$

$\mathbf {AA2} ={\begin{bmatrix}(1+2\lambda +2\beta )&-(\lambda -\alpha )&0&0\\-(\lambda +\alpha )&(1+2\lambda +2\beta )&-(\lambda -\alpha )&0\\0&-(\lambda +\alpha )&(1+2\lambda +2\beta )&-(\lambda -\alpha )\\0&0&-2\lambda &(1+2\lambda +2\beta )\end{bmatrix}},$

$\mathbf {AA3} ={\begin{bmatrix}-\beta &0&0&0\\0&-\beta &0&0\\0&0&-\beta &0\\0&0&0&-\beta \end{bmatrix}},$

$\mathbf {BB1} ={\begin{bmatrix}(1-2\lambda -\beta )&(\lambda -\alpha )&0&0\\(\lambda +\alpha )&(1-2\lambda -\beta )&(\lambda -\alpha )&0\\0&(\lambda +\alpha )&(1-2\lambda -\beta )&(\lambda -\alpha )\\0&0&2\lambda &(1-2\lambda -\beta )\end{bmatrix}},$

$\mathbf {BB2} ={\begin{bmatrix}(1-2\lambda -2\beta )&(\lambda -\alpha )&0&0\\(\lambda +\alpha )&(1-2\lambda -2\beta )&(\lambda -\alpha )&0\\0&(\lambda +\alpha )&(1-2\lambda -2\beta )&(\lambda -\alpha )\\0&0&2\lambda &(1-2\lambda -2\beta )\end{bmatrix}}.$

The **d** vector here is used to hold the boundary conditions. In this example it is a 12×1 vector:

$\mathbf {d} ={\begin{bmatrix}(\lambda +\alpha )(C_{10}^{j+1}+C_{10}^{j})\\0\\0\\0\\(\lambda +\alpha )(C_{20}^{j+1}+C_{20}^{j})\\0\\0\\0\\(\lambda +\alpha )(C_{30}^{j+1}+C_{30}^{j})\\0\\0\\0\end{bmatrix}}.$

To find the concentration at any time, one must iterate the following equation:

$\mathbf {C^{j+1}} =\mathbf {AA} ^{-1}(\mathbf {BB} \,\mathbf {C^{j}} +\mathbf {d} ).$

## Example: 2D diffusion

When extending into two dimensions on a uniform Cartesian grid, the derivation is similar and the results may lead to a system of band-diagonal equations rather than tridiagonal ones. The two-dimensional heat equation

${\frac {\partial u}{\partial t}}=a\,\nabla ^{2}u,$

${\frac {\partial u}{\partial t}}=a\left({\frac {\partial ^{2}u}{\partial x^{2}}}+{\frac {\partial ^{2}u}{\partial y^{2}}}\right)$

can be solved with the Crank–Nicolson discretization of

${\begin{aligned}u_{i,j}^{n+1}={}&u_{i,j}^{n}+{\frac {1}{2}}{\frac {a\Delta t}{(\Delta x)^{2}}}{\big [}(u_{i+1,j}^{n+1}+u_{i-1,j}^{n+1}+u_{i,j+1}^{n+1}+u_{i,j-1}^{n+1}-4u_{i,j}^{n+1})\\&+(u_{i+1,j}^{n}+u_{i-1,j}^{n}+u_{i,j+1}^{n}+u_{i,j-1}^{n}-4u_{i,j}^{n}){\big ]},\end{aligned}}$

assuming that a square grid is used, so that $\Delta x=\Delta y$ . This equation can be simplified somewhat by rearranging terms and using the CFL number

$\mu ={\frac {a\,\Delta t}{(\Delta x)^{2}}}.$

For the Crank–Nicolson numerical scheme, a low CFL number is not required for stability, however, it is required for numerical accuracy. We can now write the scheme as

$(1+2\mu )u_{i,j}^{n+1}-{\frac {\mu }{2}}\left(u_{i+1,j}^{n+1}+u_{i-1,j}^{n+1}+u_{i,j+1}^{n+1}+u_{i,j-1}^{n+1}\right)$

$\qquad =(1-2\mu )u_{i,j}^{n}+{\frac {\mu }{2}}\left(u_{i+1,j}^{n}+u_{i-1,j}^{n}+u_{i,j+1}^{n}+u_{i,j-1}^{n}\right).$

Solving such a linear system is costly. Hence an alternating-direction implicit method can be implemented to solve the numerical PDE, whereby one dimension is treated implicitly, and other dimension explicitly for half of the assigned time step and conversely for the remainder half of the time step. The benefit of this strategy is that the implicit solver only requires a tridiagonal matrix algorithm to be solved. The difference between the true Crank–Nicolson solution and ADI approximated solution has an order of accuracy of $O(\Delta t^{4})$ and hence can be ignored with a sufficiently small time step.

## Crank–Nicolson for nonlinear problems

Because the Crank–Nicolson method is implicit, it is generally impossible to solve exactly. Instead, an iterative technique should be used to converge to the solution. One option is to use Newton's method to converge on the prediction, but this requires the computation of the Jacobian. For a high-dimensional system like those in computational fluid dynamics or numerical relativity, it may be infeasible to compute this Jacobian.

A Jacobian-free alternative is fixed-point iteration. If f is the velocity of the system, then the Crank–Nicolson prediction will be a fixed point of the map $\Phi (x)=x_{0}+{\frac {h}{2}}\left[f(x_{0})+f(x)\right].$ If the map iteration $x^{(i+1)}=\Phi (x^{(i)})$ does not converge, the parameterized map $\Theta (x,\alpha )=\alpha x+(1-\alpha )\Phi (x)$ , with $\alpha \in (0,1)$ , may be better behaved. In expanded form, the update formula is

$x^{i+1}=\alpha x^{i}+(1-\alpha )\left[x_{0}+{\frac {h}{2}}\left(f(x_{0})+f(x^{i})\right)\right],$

where $x^{i}$ is the current guess and $x_{i-1}$ is the previous time-step.

Even for high-dimensional systems, iteration of this map can converge surprisingly quickly.

## Application in financial mathematics

Because a number of other phenomena can be modeled with the heat equation (often called the diffusion equation in financial mathematics), the Crank–Nicolson method has been applied to those areas as well. Particularly, the Black–Scholes option pricing model's differential equation can be transformed into the heat equation, and thus numerical solutions for option pricing can be obtained with the Crank–Nicolson method.

The importance of this for finance is that option pricing problems, when extended beyond the standard assumptions (e.g. incorporating changing dividends), cannot be solved in closed form, but can be solved using this method. Note however, that for non-smooth final conditions (which happen for most financial instruments), the Crank–Nicolson method is not satisfactory as numerical oscillations are not damped. For vanilla options, this results in oscillation in the gamma value around the strike price. Therefore, special damping initialization steps are necessary (e.g., fully implicit finite difference method).

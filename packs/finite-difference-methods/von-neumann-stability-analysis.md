---
title: "Von Neumann stability analysis"
source: https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Von Neumann stability analysis

In numerical analysis, **von Neumann stability analysis** (also known as Fourier stability analysis) is a procedure used to check the stability of finite difference schemes as applied to linear partial differential equations. The analysis is based on the Fourier decomposition of numerical error and was developed at Los Alamos National Laboratory after having been briefly described in a 1947 article by British researchers John Crank and Phyllis Nicolson. This method is an example of explicit time integration where the function that defines governing equation is evaluated at the current time. Later, the method was given a more rigorous treatment in an article co-authored by John von Neumann, wherein it is described as a "heuristic procedure" patterned after the more rigorous Courant–Friedrichs–Lewy condition.

## Numerical stability

The stability of numerical schemes is closely associated with numerical error. A finite difference scheme is stable if the errors made at one time step of the calculation do not cause the errors to be magnified as the computations are continued. A *neutrally stable scheme* is one in which errors remain constant as the computations are carried forward. If the errors decay and eventually damp out, the numerical scheme is said to be stable. If, on the contrary, the errors grow with time the numerical scheme is said to be unstable. The stability of numerical schemes can be investigated by performing von Neumann stability analysis. For time-dependent problems, stability guarantees that the numerical method produces a bounded solution whenever the solution of the exact differential equation is bounded. Stability, in general, can be difficult to investigate, especially when the equation under consideration is nonlinear.

In certain cases, von Neumann stability is necessary and sufficient for stability in the sense of Lax–Richtmyer (as used in the Lax equivalence theorem): The PDE and the finite difference scheme models are linear; the PDE is constant-coefficient with periodic boundary conditions and has only two independent variables; and the scheme uses no more than two time levels. Von Neumann stability is necessary in a much wider variety of cases. It is often used in place of a more detailed stability analysis to provide a good guess at the restrictions (if any) on the step sizes used in the scheme because of its relative simplicity.

## Illustration of the method

The von Neumann method is based on the decomposition of the errors into Fourier series. To illustrate the procedure, consider the one-dimensional heat equation ${\frac {\partial u}{\partial t}}=\alpha {\frac {\partial ^{2}u}{\partial x^{2}}}$ defined on the spatial interval L , with the notation $u_{j}^{n}=u(x_{j},t^{n})$ where $x_{j}$ are the specific *x* values, and $t^{n}$ are the sequence of *t* values.

We can discretize the heat equation as

| $u_{j}^{n+1}=u_{j}^{n}+r\left(u_{j+1}^{n}-2u_{j}^{n}+u_{j-1}^{n}\right)$ |   | 1 |
|---|---|---|

where $r={\frac {\alpha \,\Delta t}{\left(\Delta x\right)^{2}}}$

Then the solution $u_{j}^{n}$ of the discrete equation approximates the analytical solution $u(x,t)$ of the PDE on the grid.

Define the round-off error $\epsilon _{j}^{n}$ as $\epsilon _{j}^{n}=N_{j}^{n}-u_{j}^{n}$ where $u_{j}^{n}$ is the solution of the discretized equation (**1**) that would be computed in the absence of round-off error, and $N_{j}^{n}$ is the numerical solution obtained in finite precision arithmetic. Since the exact solution $u_{j}^{n}$ must satisfy the discretized equation exactly, the error $\epsilon _{j}^{n}$ must also satisfy the discretized equation. Here we assumed that $N_{j}^{n}$ satisfies the equation, too (this is only true in machine precision). Thus

| $\epsilon _{j}^{n+1}=\epsilon _{j}^{n}+r\left(\epsilon _{j+1}^{n}-2\epsilon _{j}^{n}+\epsilon _{j-1}^{n}\right)$ |   | 2 |
|---|---|---|

is a recurrence relation for the error. Equations (**1**) and (**2**) show that both the error and the numerical solution have the same growth or decay behavior with respect to time. For linear differential equations with periodic boundary condition, the spatial variation of error may be expanded in a finite Fourier series with respect to x , in the interval L , as

| $\epsilon (x,t)=\sum _{m=-M}^{M}E_{m}(t)e^{{i}k_{m}x}$ |   | 3 |
|---|---|---|

where the wavenumber $k_{m}={\frac {\pi m}{L}}$ with $m=-M,\dots ,-2,-1,0,1,2,\dots ,M$ and $M=L/\Delta x$ . The time dependence of the error is included by assuming that the amplitude of error $E_{m}$ is a function of time. Often the assumption is made that the error grows or decays exponentially with time, but this is not necessary for the stability analysis.

If the boundary condition is not periodic, then we may use the finite Fourier integral with respect to x :

| $\epsilon (x,t)=\int _{-{\frac {\pi }{\Delta x}}}^{\frac {\pi }{\Delta x}}E_{k}(t)e^{ikx}dk$ |   | 4 |
|---|---|---|

Since the difference equation for error is linear (the behavior of each term of the series is the same as series itself), it is enough to consider the growth of error of a typical term:

| $\epsilon _{m}(x,t)=E_{m}(t)e^{ik_{m}x}$ |   | 5a |
|---|---|---|

if a Fourier series is used or

| $\epsilon _{k}(x,t)=E_{k}(t)e^{ikx}$ |   | 5b |
|---|---|---|

if a Fourier integral is used.

As the Fourier series can be considered to be a special case of the Fourier integral, we will continue the development using the expressions for the Fourier integral.

The stability characteristics can be studied using just this form for the error with no loss in generality. To find out how error varies in steps of time, substitute equation (**5b**) into equation (**2**), after noting that ${\begin{aligned}\epsilon _{j}^{n}&=E_{m}(t)e^{ik_{m}x}\\\epsilon _{j}^{n+1}&=E_{m}(t+\Delta t)e^{ik_{m}x}\\\epsilon _{j+1}^{n}&=E_{m}(t)e^{ik_{m}(x+\Delta x)}\\\epsilon _{j-1}^{n}&=E_{m}(t)e^{ik_{m}(x-\Delta x)},\end{aligned}}$ to yield (after simplification)

| ${\frac {E_{m}(t+\Delta t)}{E_{m}(t)}}=1+r\left(e^{ik_{m}\Delta x}+e^{-ik_{m}\Delta x}-2\right).$ |   | 6 |
|---|---|---|

Introducing $\theta =k_{m}\Delta x\in [-\pi ,\pi ]$ and using the identities $\sin \left({\frac {\theta }{2}}\right)={\frac {e^{i\theta /2}-e^{-i\theta /2}}{2i}}\qquad \rightarrow \qquad \sin ^{2}\left({\frac {\theta }{2}}\right)=-{\frac {e^{i\theta }+e^{-i\theta }-2}{4}}$ equation (**6**) may be written as

| ${\frac {E_{m}(t+\Delta t)}{E_{m}(t)}}=1-4r\sin ^{2}(\theta /2)$ |   | 7 |
|---|---|---|

Define the amplification factor

| $G\equiv {\frac {E_{m}(t+\Delta t)}{E_{m}(t)}}$ |   | 8 |
|---|---|---|

The necessary and sufficient condition for the error to remain bounded is that $|G|\leq 1.$ Thus, from equations (**7**) and (**8**), the condition for stability is given by

| $\left\|1-4r\sin ^{2}(\theta /2)\right\|\leq 1$ |   | 9 |
|---|---|---|

Note that the term $4r\sin ^{2}(\theta /2)$ is always positive. Thus, to satisfy Equation (**9**):

| $4r\sin ^{2}(\theta /2)\leq 2$ |   | 10 |
|---|---|---|

For the above condition to hold for all m (and therefore all $\sin ^{2}(\theta /2)$ ). The highest value the sinusoidal term can take is 1 and for that particular choice if the upper threshold condition is satisfied, then so will be for all grid points, thus we have

| $r={\frac {\alpha \Delta t}{\left(\Delta x\right)^{2}}}\leq {\frac {1}{2}}$ |   | 11 |
|---|---|---|

Equation (**11**) gives the stability requirement for the FTCS scheme as applied to one-dimensional heat equation. It says that for a given $\Delta x$ , the allowed value of $\Delta t$ must be small enough to satisfy equation (**10**).

Similar analysis shows that a FTCS scheme for linear advection is unconditionally unstable.

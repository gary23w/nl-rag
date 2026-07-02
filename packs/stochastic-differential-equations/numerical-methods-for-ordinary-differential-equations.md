---
title: "Numerical methods for ordinary differential equations"
source: https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations
domain: stochastic-differential-equations
license: CC-BY-SA-4.0
tags: stochastic differential equation, euler-maruyama method, milstein method, langevin equation
fetched: 2026-07-02
---

# Numerical methods for ordinary differential equations

**Numerical methods for ordinary differential equations** are methods used to find numerical approximations to the solutions of ordinary differential equations (ODEs). Their use is also known as "numerical integration", although this term can also refer to the computation of integrals.

Many differential equations cannot be solved exactly. For practical purposes, however – such as in engineering – a numeric approximation to the solution is often sufficient. The algorithms studied here can be used to compute such an approximation. An alternative method is to use techniques from calculus to obtain a series expansion of the solution.

Ordinary differential equations occur in many scientific disciplines, including physics, chemistry, biology, and economics. In addition, some methods in numerical partial differential equations convert the partial differential equation into an ordinary differential equation, which must then be solved.

## The problem

A first-order differential equation is an Initial value problem (IVP) of the form,

| $y'(t)=f(t,y(t)),\qquad y(t_{0})=y_{0},$ |   | 1 |
|---|---|---|

where f is a function $f:[t_{0},\infty )\times \mathbb {R} ^{d}\to \mathbb {R} ^{d}$ , and the initial condition $y_{0}\in \mathbb {R} ^{d}$ is a given vector. *First-order* means that only the first derivative of *y* appears in the equation, and higher derivatives are absent.

Without loss of generality to higher-order systems, we restrict ourselves to *first-order* differential equations, because a higher-order ODE can be converted into a larger system of first-order equations by introducing extra variables. For example, the second-order equation *y*′′ = −*y* can be rewritten as two first-order equations: *y*′ = *z* and *z*′ = −*y*.

In this section, we describe numerical methods for IVPs, and remark that *boundary value problems* (BVPs) require a different set of tools. In a BVP, one defines values, or components of the solution *y* at more than one point. Because of this, different methods need to be used to solve BVPs. For example, the shooting method (and its variants) or global methods like finite differences, Galerkin methods, or collocation methods are appropriate for that class of problems.

The Picard–Lindelöf theorem states that there is a unique solution, provided *f* is Lipschitz-continuous.

## Methods

Numerical methods for solving first-order IVPs often fall into one of two large categories: linear multistep methods, or Runge–Kutta methods. A further division can be realized by dividing methods into those that are explicit and those that are implicit. For example, implicit linear multistep methods include Adams-Moulton methods, and backward differentiation methods (BDF), whereas implicit Runge–Kutta methods include diagonally implicit Runge–Kutta (DIRK), singly diagonally implicit Runge–Kutta (SDIRK), and Gauss–Radau (based on Gaussian quadrature) numerical methods. Explicit examples from the linear multistep family include the Adams–Bashforth methods, and any Runge–Kutta method with a lower diagonal Butcher tableau is explicit. A loose rule of thumb dictates that stiff differential equations require the use of implicit schemes, whereas non-stiff problems can be solved more efficiently with explicit schemes.

The so-called general linear methods (GLMs) are a generalization of the above two large classes of methods.

### Euler method

From any point on a curve, you can find an approximation of a nearby point on the curve by moving a short distance along a line tangent to the curve.

Starting with the differential equation (**1**), we replace the derivative *y*′ by the finite difference approximation

| $y'(t)\approx {\frac {y(t+h)-y(t)}{h}},$ |   | 2 |
|---|---|---|

which when re-arranged yields the following formula $y(t+h)\approx y(t)+hy'(t)$ and using (**1**) gives:

| $y(t+h)\approx y(t)+hf(t,y(t)).$ |   | 3 |
|---|---|---|

This formula is usually applied in the following way. We choose a step size *h*, and we construct the sequence $t_{0},t_{1}=t_{0}+h,t_{2}=t_{0}+2h,\dots$ We denote by $y_{n}$ a numerical estimate of the exact solution $y(t_{n})$ . Motivated by (**3**), we compute these estimates by the following recursive scheme

| $y_{n+1}=y_{n}+hf(t_{n},y_{n}).$ |   | 4 |
|---|---|---|

This is the *Euler method* (or *forward Euler method*, in contrast with the *backward Euler method*, to be described below). The method is named after Leonhard Euler who described it in 1768.

The Euler method is an example of an *explicit* method. This means that the new value *y**n*+1 is defined in terms of things that are already known, like *y**n*.

### Backward Euler method

If, instead of (**2**), we use the approximation

| $y'(t)\approx {\frac {y(t)-y(t-h)}{h}},$ |   | 5 |
|---|---|---|

we get the *backward Euler method*:

| $y_{n+1}=y_{n}+hf(t_{n+1},y_{n+1}).$ |   | 6 |
|---|---|---|

The backward Euler method is an *implicit* method, meaning that we have to solve an equation to find *y**n*+1. One often uses fixed-point iteration or (some modification of) the Newton–Raphson method to achieve this.

It costs more time to solve this equation than explicit methods; this cost must be taken into consideration when one selects the method to use. The advantage of implicit methods such as (**6**) is that they are usually more stable for solving a stiff equation, meaning that a larger step size *h* can be used.

### First-order exponential integrator method

Exponential integrators describe a large class of integrators that have recently seen a lot of development. They date back to at least the 1960s.

In place of (**1**), we assume the differential equation is either of the form

| $y'(t)=-A\,y+{\mathcal {N}}(y),$ |   | 7 |
|---|---|---|

or it has been locally linearized about a background state to produce a linear term $-Ay$ and a nonlinear term ${\mathcal {N}}(y)$ .

Exponential integrators are constructed by multiplying (**7**) by ${\textstyle e^{At}}$ , and exactly integrating the result over a time interval $[t_{n},t_{n+1}]$ where $t_{n+1}=t_{n}{+}h$ : $y_{n+1}=e^{-Ah}y_{n}+\int _{0}^{h}e^{-(h-\tau )A}{\mathcal {N}}{\left(y\left(t_{n}+\tau \right)\right)}\,d\tau .$ This integral equation is exact, but it does not define the integral.

The first-order exponential integrator can be realized by holding ${\mathcal {N}}(y(t_{n}+\tau ))$ constant over the full interval:

| $y_{n+1}=e^{-Ah}y_{n}+A^{-1}\left(1-e^{-Ah}\right){\mathcal {N}}{\left(y(t_{n})\right)}\ .$ |   | 8 |
|---|---|---|

### Generalizations

The Euler method is often not accurate enough. In more precise terms, it only has order one (the concept of *order* is explained below). This caused mathematicians to look for higher-order methods.

One possibility is to use not only the previously computed value *y**n* to determine *y**n*+1, but to make the solution depend on more past values. This yields a so-called *multistep method*. Perhaps the simplest is the leapfrog method which is second order and (roughly speaking) relies on two time values.

Almost all practical multistep methods fall within the family of linear multistep methods, which have the form ${\begin{aligned}&{}\alpha _{k}y_{n+k}+\alpha _{k-1}y_{n+k-1}+\cdots +\alpha _{0}y_{n}\\&{}\quad =h\left[\beta _{k}f(t_{n+k},y_{n+k})+\beta _{k-1}f(t_{n+k-1},y_{n+k-1})+\cdots +\beta _{0}f(t_{n},y_{n})\right].\end{aligned}}$

Another possibility is to use more points in the interval $[t_{n},t_{n+1}]$ . This leads to the family of Runge–Kutta methods, named after Carl Runge and Martin Kutta. One of their fourth-order methods is especially popular.

### Advanced features

A good implementation of one of these methods for solving an ODE entails more than the time-stepping formula.

It is often inefficient to use the same step size all the time, so *variable step-size methods* have been developed. Usually, the step size is chosen such that the (local) error per step is below some tolerance level. This means that the methods must also compute an *error indicator*, an estimate of the local error.

An extension of this idea is to choose dynamically between different methods of different orders (this is called a *variable order method*). Methods based on Richardson extrapolation, such as the Bulirsch–Stoer algorithm, are often used to construct various methods of different orders.

Other desirable features include:

- *dense output*: cheap numerical approximations for the whole integration interval, and not only at the points *t*0, *t*1, *t*2, ...
- *event location*: finding the times where, say, a particular function vanishes. This typically requires the use of a root-finding algorithm.
- support for parallel computing.
- when used for integrating with respect to time, time reversibility

### Alternative methods

Many methods do not fall within the framework discussed here. Some classes of alternative methods are:

- *multiderivative methods*, which use not only the function *f* but also its derivatives. This class includes *Hermite–Obreschkoff methods* and *Fehlberg methods*, as well as methods like the Parker–Sochacki method or Bychkov–Scherbakov method, which compute the coefficients of the Taylor series of the solution *y* recursively.
- *methods for second order ODEs*. We said that all higher-order ODEs can be transformed to first-order ODEs of the form (1). While this is certainly true, it may not be the best way to proceed. In particular, *Nyström methods* work directly with second-order equations.
- *geometric integration methods* are especially designed for special classes of ODEs (for example, symplectic integrators for the solution of Hamiltonian equations). They take care that the numerical solution respects the underlying structure or geometry of these classes.
- *Quantized state systems methods* are a family of ODE integration methods based on the idea of state quantization. They are efficient when simulating sparse systems with frequent discontinuities.

### Parallel-in-time methods

Some IVPs require integration at such high temporal resolution and/or over such long time intervals that classical serial time-stepping methods become computationally infeasible to run in real-time (e.g. IVPs in numerical weather prediction, plasma modelling, and molecular dynamics). Parallel-in-time (PinT) methods have been developed in response to these issues in order to reduce simulation runtimes through the use of parallel computing.

Early PinT methods (the earliest being proposed in the 1960s) were initially overlooked by researchers due to the fact that the parallel computing architectures that they required were not yet widely available. With more computing power available, interest was renewed in the early 2000s with the development of Parareal, a flexible, easy-to-use PinT algorithm that is suitable for solving a wide variety of IVPs. The advent of exascale computing has meant that PinT algorithms are attracting increasing research attention and are being developed in such a way that they can harness the world's most powerful supercomputers. The most popular methods as of 2023 include Parareal, PFASST, ParaDiag, and MGRIT.

## Analysis

Numerical analysis is not only the design of numerical methods, but also their analysis. Three central concepts in this analysis are:

- *convergence*: whether the method approximates the solution,
- *order*: how well it approximates the solution, and
- *stability*: whether errors are damped out.

### Convergence

A numerical method is said to be *convergent* if the numerical solution approaches the exact solution as the step size *h* goes to 0. More precisely, we require that for every ODE (1) with a Lipschitz function *f* and every *t** > 0,

$\lim _{h\to 0^{+}}\max _{n=0,1,\dots ,\lfloor t^{*}/h\rfloor }\left\|y_{n,h}-y(t_{n})\right\|=0.$

All the methods mentioned above are convergent.

### Consistency and order

Suppose the numerical method is

$y_{n+k}=\Psi (t_{n+k};y_{n},y_{n+1},\dots ,y_{n+k-1};h).\,$

The *local (truncation) error* of the method is the error committed by one step of the method. That is, it is the difference between the result given by the method, assuming that no error was made in earlier steps, and the exact solution:

$\delta _{n+k}^{h}=\Psi {\left(t_{n+k};y(t_{n}),y(t_{n+1}),\dots ,y(t_{n+k-1});h\right)}-y(t_{n+k}).$

The method is said to be *consistent* if $\lim _{h\to 0}{\frac {\delta _{n+k}^{h}}{h}}=0.$ The method has *order* p if $\delta _{n+k}^{h}=O(h^{p+1})\quad {\text{as }}h\to 0.$ Hence a method is consistent if it has an order greater than 0. The (forward) Euler method (4) and the backward Euler method (6) introduced above both have order 1, so they are consistent. Most methods being used in practice attain higher order. Consistency is a necessary condition for convergence, but not sufficient; for a method to be convergent, it must be both consistent and zero-stable.

A related concept is the *global (truncation) error*, the error sustained in all the steps one needs to reach a fixed time t . Explicitly, the global error at time t is $y_{N}-y(t)$ where $N=(t-t_{0})/h$ . The global error of a p -th order one-step method is $O(h^{p})$ ; in particular, such a method is convergent. This statement is not necessarily true for multi-step methods.

### Stability and stiffness

For some differential equations, application of standard methods—such as the Euler method, explicit Runge–Kutta methods, or multistep methods (for example, Adams–Bashforth methods)—exhibit instability in the solutions, though other methods may produce stable solutions. This "difficult behaviour" in the equation (which may not necessarily be complex itself) is described as *stiffness*, and is often caused by the presence of different time scales in the underlying problem. For example, a collision in a mechanical system like in an impact oscillator typically occurs at much smaller time scale than the time for the motion of objects; this discrepancy makes for very "sharp turns" in the curves of the state parameters.

Stiff problems are ubiquitous in chemical kinetics, control theory, solid mechanics, weather forecasting, biology, plasma physics, and electronics. One way to overcome stiffness is to extend the notion of differential equation to that of differential inclusion, which allows for and models non-smoothness.

## History

Below is a timeline of some important developments in this field.

- 1768 - Leonhard Euler publishes his method.
- 1824 - Augustin Louis Cauchy proves convergence of the Euler method. In this proof, Cauchy uses the implicit Euler method.
- 1855 - First mention of the multistep methods of John Couch Adams in a letter written by Francis Bashforth.
- 1895 - Carl Runge publishes the first Runge–Kutta method.
- 1901 - Martin Kutta describes the popular fourth-order Runge–Kutta method.
- 1910 - Lewis Fry Richardson announces his extrapolation method, Richardson extrapolation.
- 1952 - Charles F. Curtiss and Joseph Oakland Hirschfelder coin the term *stiff equations*.
- 1963 - Germund Dahlquist introduces *A-stability* of integration methods.

## Numerical solutions to second-order one-dimensional boundary value problems

Boundary value problems (BVPs) are usually solved numerically by solving an approximately equivalent matrix problem obtained by discretizing the original BVP. The most commonly used method for numerically solving BVPs in one dimension is called the Finite Difference Method. This method takes advantage of linear combinations of point values to construct finite difference coefficients that describe derivatives of the function. For example, the second-order central difference approximation to the first derivative is given by:

$u'(x_{i})={\frac {u_{i+1}-u_{i-1}}{2h}}+{\mathcal {O}}(h^{2}),$

and the second-order central difference for the second derivative is given by:

$u''(x_{i})={\frac {u_{i+1}-2u_{i}+u_{i-1}}{h^{2}}}+{\mathcal {O}}(h^{2}).$

In both of these formulae, $h=x_{i}-x_{i-1}$ is the distance between neighbouring *x* values on the discretized domain. One then constructs a linear system that can then be solved by standard matrix methods. For example, suppose the equation to be solved is:

${\begin{aligned}&{\frac {d^{2}u}{dx^{2}}}=u,\\[1ex]&u(0)=0,\\&u(1)=1.\end{aligned}}$

The next step would be to discretize the problem and use linear derivative approximations such as

$u''_{i}={\frac {u_{i+1}-2u_{i}+u_{i-1}}{h^{2}}}$

and solve the resulting system of linear equations. This would lead to equations such as:

${\frac {u_{i+1}-2u_{i}+u_{i-1}}{h^{2}}}-u_{i}=0,\quad \forall i={1,2,3,\dots ,n-1}.$

On first viewing, this system of equations appears to have difficulty associated with the fact that the equation involves no terms that are not multiplied by variables, but in fact this is false. At *i* = 1 and *n* − 1 there is a term involving the boundary values $u(0)=u_{0}$ and $u(1)=u_{n}$ and since these two values are known, one can simply substitute them into this equation and as a result have a non-homogeneous system of linear equations that has non-trivial solutions.

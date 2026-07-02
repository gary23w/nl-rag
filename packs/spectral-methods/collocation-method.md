---
title: "Collocation method"
source: https://en.wikipedia.org/wiki/Collocation_method
domain: spectral-methods
license: CC-BY-SA-4.0
tags: spectral method, pseudo-spectral method, chebyshev polynomials, collocation method
fetched: 2026-07-02
---

# Collocation method

In mathematics, a **collocation method** is a method for the numerical solution of ordinary differential equations, partial differential equations and integral equations. The idea is to choose a finite-dimensional space of candidate solutions (usually polynomials up to a certain degree) and a number of points in the domain (called *collocation points*), and to select that solution which satisfies the given equation at the collocation points.

## Ordinary differential equations

Suppose that the ordinary differential equation $y'(t)=f(t,y(t)),\quad y(t_{0})=y_{0},$ is to be solved over the interval $[t_{0},t_{0}+h]$ . Choose $c_{k}$ from 0 ≤ *c*1< *c*2< ... < *c**n* ≤ 1.

The corresponding (polynomial) collocation method approximates the solution *y* by the polynomial *p* of degree *n* which satisfies the initial condition $p(t_{0})=y_{0}$ , and the differential equation $p'(t_{k})=f(t_{k},p(t_{k}))$ at all *collocation points* $t_{k}=t_{0}+c_{k}h$ for $k=1,\ldots ,n$ . This gives *n* + 1 conditions, which matches the *n* + 1 parameters needed to specify a polynomial of degree *n*.

All these collocation methods are in fact implicit Runge–Kutta methods. The coefficients *c**k* in the Butcher tableau of a Runge–Kutta method are the collocation points. However, not all implicit Runge–Kutta methods are collocation methods.

### Example: The trapezoidal rule

Pick, as an example, the two collocation points *c*1 = 0 and *c*2 = 1 (so *n* = 2). The collocation conditions are

${\begin{aligned}p(t_{0})&=y_{0},\\p'(t_{0})&=f(t_{0},p(t_{0})),\\p'(t_{0}{+}h)&=f(t_{0}{+}h,p(t_{0}{+}h)).\end{aligned}}$

There are three conditions, so *p* should be a polynomial of degree 2. Write *p* in the form

$p(t)=\alpha (t-t_{0})^{2}+\beta (t-t_{0})+\gamma \,$

to simplify the computations. Then the collocation conditions can be solved to give the coefficients

${\begin{aligned}\alpha &={\frac {1}{2h}}{\Big (}f(t_{0}{+}h,p(t_{0}{+}h))-f(t_{0},p(t_{0})){\Big )},\\\beta &=f(t_{0},p(t_{0})),\\\gamma &=y_{0}.\end{aligned}}$

The collocation method is now given (implicitly) by

$y_{1}=p(t_{0}+h)=y_{0}+{\frac {1}{2}}h{\Big (}f(t_{0}{+}h,y_{1})+f(t_{0},y_{0}){\Big )},\,$

where *y*1 = *p*(*t*0 + *h*) is the approximate solution at *t* = *t*1 = *t*0 + *h*.

This method is known as the "trapezoidal rule" for differential equations. Indeed, this method can also be derived by rewriting the differential equation as

$y(t)=y(t_{0})+\int _{t_{0}}^{t}f(\tau ,y(\tau ))\,d\tau ,\,$

and approximating the integral on the right-hand side by the trapezoidal rule for integrals.

### Other examples

The Gauss–Legendre methods use the points of Gauss–Legendre quadrature as collocation points. The Gauss–Legendre method based on *s* points has order 2*s*. All Gauss–Legendre methods are A-stable.

In fact, one can show that the order of a collocation method corresponds to the order of the quadrature rule that one would get using the collocation points as weights.

## Orthogonal collocation method

In direct collocation method, we are essentially performing variational calculus with the finite-dimensional subspace of piecewise linear functions (as in trapezoidal rule), or cubic functions, or other piecewise polynomial functions. In orthogonal collocation method, we instead use the finite-dimensional subspace spanned by the first N vectors in some orthogonal polynomial basis, such as the Legendre polynomials.

## Applications

### Motorsport

Top F1 teams began switching from Quasi-Static simulation to collocation methods in 2010s to simulate the time it takes for a car to go around a circuit. It is thought that Sauber were one of the first teams to make this transition. Traditional Quasi-Static simulation involves the construction of a gLat-gLong-vCar performance envelope for the car, then starting at each apex (minimum car speed) and accelerating forwards, and backwards through the braking zone using this envelope to stitch a lap together. It is a gross simplification of the problem because the envelope is steady state so ignores any of the dynamics that occur, for example, the car can switch instantaneously between understeer and oversteer.

The switch to collocation methods in simulation involved casting the entire lap as an optimisation problem, broken down by distance steps around the lap which describe the car physics at each point. The objective is to minimise laptime and error in the physics at each point. Once the optimisation is complete, the collocation method finds the minimum laptime for a particular car setup around a circuit by varying brake/throttle and steering wheel angle while obeying the physics at every point. Additional constraints can be added to the objective function alongside minimisation of laptime, such as energy constraints (fuel, electrical, tyre sliding, brakes), and temperature constraints (tyres, battery temperature), and additional controls, such as multiple throttle pedals controlling power to all four wheels can be added to the physics. This allows for extremely complex problems to be solved optimally.

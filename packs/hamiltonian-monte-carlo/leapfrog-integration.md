---
title: "Leapfrog integration"
source: https://en.wikipedia.org/wiki/Leapfrog_integration
domain: hamiltonian-monte-carlo
license: CC-BY-SA-4.0
tags: Hamiltonian Monte Carlo, leapfrog integration, Hamiltonian mechanics, detailed balance
fetched: 2026-07-02
---

# Leapfrog integration

In numerical analysis, **leapfrog integration** is a method for numerically integrating differential equations of the form ${\ddot {x}}={\frac {d^{2}x}{dt^{2}}}=A(x),$ or equivalently of the form ${\dot {v}}={\frac {dv}{dt}}=A(x),\qquad {\dot {x}}={\frac {dx}{dt}}=v,$ particularly in the case of a dynamical system of classical mechanics.

The method is known by different names in different disciplines. In particular, it is similar to the **velocity Verlet** method, which is a variant of Verlet integration. Leapfrog integration is equivalent to updating positions $x(t)$ and velocities $v(t)={\dot {x}}(t)$ at different interleaved time points, staggered in such a way that they "leapfrog" over each other.

Leapfrog integration is a second-order method, in contrast to Euler integration, which is only first-order, yet requires the same number of function evaluations per step. Unlike Euler integration, it is stable for oscillatory motion, as long as the time-step $\Delta t$ is constant, and $\Delta t<2/\omega$ .

Using Yoshida coefficients, applying the leapfrog integrator multiple times with the correct timesteps, a much higher order integrator can be generated.

## Algorithm

In leapfrog integration, the equations for updating position and velocity are ${\begin{aligned}a_{i}&=A(x_{i}),\\v_{i+1/2}&=v_{i-1/2}+a_{i}\,\Delta t,\\x_{i+1}&=x_{i}+v_{i+1/2}\,\Delta t,\end{aligned}}$

where $x_{i}$ is position at step i , $v_{i+1/2\,}$ is the velocity, or first derivative of x , at step $i+1/2\,$ , $a_{i}=A(x_{i})$ is the acceleration, or second derivative of x , at step i , and $\Delta t$ is the size of each time step. These equations can be expressed in a form that gives velocity at integer steps as well: ${\begin{aligned}x_{i+1}&=x_{i}+v_{i}\,\Delta t+{\tfrac {1}{2}}\,a_{i}\,\Delta t^{\,2},\\v_{i+1}&=v_{i}+{\tfrac {1}{2}}(a_{i}+a_{i+1})\,\Delta t.\end{aligned}}$ However, in this synchronized form, the time-step $\Delta t$ must be constant to maintain stability.

The synchronised form can be re-arranged to the 'kick-drift-kick' form; ${\begin{aligned}v_{i+1/2}&=v_{i}+{\tfrac {1}{2}}a_{i}\Delta t,\\[2pt]x_{i+1}&=x_{i}+v_{i+1/2}\Delta t,\\[2pt]v_{i+1}&=v_{i+1/2}+{\tfrac {1}{2}}a_{i+1}\Delta t,\end{aligned}}$ which is primarily used where variable time-steps are required. The separation of the acceleration calculation onto the beginning and end of a step means that if time resolution is increased by a factor of two ( $\Delta t\rightarrow \Delta t/2$ ), then only one extra (computationally expensive) acceleration calculation is required.

One use of this equation is in Newtonian gravity simulations, since in that case the acceleration depends only on the positions of the gravitating masses (and not on their velocities).

There are two primary strengths to leapfrog integration when applied to mechanics problems. The first is the time-reversibility of the Leapfrog method. One can integrate forward *n* steps, and then reverse the direction of integration and integrate backwards *n* steps to arrive at the same starting position. The second strength is its symplectic nature, which implies that it conserves the (slightly modified; see symplectic integrator) energy of a Hamiltonian dynamical system. This is especially useful when computing orbital dynamics, as many other integration schemes, such as the (order-4) Runge–Kutta method, do not conserve energy and allow the system to drift substantially over time.

Because of its time-reversibility, and because it is a symplectic integrator, leapfrog integration is also used in Hamiltonian Monte Carlo, a method for drawing random samples from a probability distribution whose overall normalization is unknown.

## Yoshida algorithms

The leapfrog integrator can be converted into higher order integrators using techniques due to Haruo Yoshida. In this approach, the leapfrog is applied over a number of different timesteps. It turns out that when the correct timesteps are used in sequence, the errors cancel and far higher order integrators can be easily produced.

### 4th order Yoshida integrator

One step under the 4th order Yoshida integrator requires four intermediary steps. The position and velocity are computed at different times. Only three (computationally expensive) acceleration calculations are required.

The equations for the 4th order integrator to update position and velocity are

${\begin{aligned}x_{i}^{1}&=x_{i}+c_{1}\,v_{i}\,\Delta t,&v_{i}^{1}&=v_{i}+d_{1}\,a(x_{i}^{1})\,\Delta t,\\x_{i}^{2}&=x_{i}^{1}+c_{2}\,v_{i}^{1}\,\Delta t,&v_{i}^{2}&=v_{i}^{1}+d_{2}\,a(x_{i}^{2})\,\Delta t,\\x_{i}^{3}&=x_{i}^{2}+c_{3}\,v_{i}^{2}\,\Delta t,&v_{i}^{3}&=v_{i}^{2}+d_{3}\,a(x_{i}^{3})\,\Delta t,\\x_{i+1}&\equiv x_{i}^{4}=x_{i}^{3}+c_{4}\,v_{i}^{3}\,\Delta t,&v_{i+1}&\equiv v_{i}^{4}=v_{i}^{3}\\\end{aligned}}$

where $x_{i},v_{i}$ are the starting position and velocity, $x_{i}^{n},v_{i}^{n}$ are intermediary position and velocity at intermediary step n , $a(x_{i}^{n})$ is the acceleration at the position $x_{i}^{n}$ , and $x_{i+1},v_{i+1}$ are the final position and velocity under one 4th order Yoshida step.

Coefficients $(c_{1},c_{2},c_{3},c_{4})$ and $(d_{1},d_{2},d_{3})$ are derived in (see the equation (4.6))

${\begin{aligned}w_{0}&\equiv -{\frac {\sqrt[{3}]{2}}{2-{\sqrt[{3}]{2}}}},&w_{1}&\equiv {\frac {1}{2-{\sqrt[{3}]{2}}}},\\[1ex]c_{1}&=c_{4}\equiv {\frac {w_{1}}{2}},&c_{2}=c_{3}&\equiv {\frac {w_{0}+w_{1}}{2}},\\[1ex]d_{1}&=d_{3}\equiv w_{1},&d_{2}&\equiv w_{0}\\\end{aligned}}$

All intermediary steps form one $\Delta t$ step which implies that coefficients sum up to one: ${\textstyle \sum _{i=1}^{4}c_{i}=1}$ and ${\textstyle \sum _{i=1}^{3}d_{i}=1}$ . Note that position and velocity are computed at different times and some intermediary steps are backwards in time. To illustrate this, we give the numerical values of $c_{n}$ coefficients: $c_{1}=0.6756$ , $c_{2}=-0.1756$ , $c_{3}=-0.1756$ , $c_{4}=0.6756.$

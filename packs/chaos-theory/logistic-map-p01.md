---
title: "Logistic map (part 1/4)"
source: https://en.wikipedia.org/wiki/Logistic_map
domain: chaos-theory
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
part: 1/4
---

# Logistic map

The **logistic map** is a discrete dynamical system defined by the quadratic difference equation

| $x_{n+1}=rx_{n}(1-x_{n}).$ |   | 1 |
|---|---|---|

It is a recurrence relation and a polynomial mapping of degree 2. It is often referred to as an archetypal example of how complex, chaotic behaviour can arise from very simple nonlinear dynamical equations.

The map was initially utilized by Edward Lorenz in the 1960s to showcase properties of irregular solutions in climate systems. It was popularized in a 1976 paper by the biologist Robert May, in part as a discrete-time demographic model analogous to the logistic equation written down by Pierre François Verhulst. Other researchers who have contributed to the study of the logistic map include Stanisław Ulam, John von Neumann, Pekka Myrberg, Oleksandr Sharkovsky, Nicholas Metropolis, and Mitchell Feigenbaum.


## Two introductory examples

### Dynamical systems example

In the logistic map, *x* is a variable, and *r* is a parameter. It is a map in the sense that it maps a configuration or phase space to itself (in this simple case the space is one dimensional in the variable *x*):

| $f\colon x\mapsto rx(1-x).$ |   | 1-2 |
|---|---|---|

It can be interpreted as a tool to get next position in the configuration space after one time step. The difference equation is a discrete version of the logistic differential equation, which can be compared to a time evolution equation of the system.

Given an appropriate value for the parameter *r* and performing calculations starting from an initial condition $x_{0}$ , we obtain the sequence $x_{0}$ , $x_{1}$ , $x_{2}$ , ..., which can be interpreted as a sequence of time steps in the evolution of the system.

In the field of dynamical systems, this sequence is called an orbit, and the orbit changes depending on the value given to the parameter. When the parameter is changed, the orbit of the logistic map can change in various ways, such as settling on a single value, repeating several values periodically, or showing non-periodic fluctuations known as chaos.

Another way to understand this sequence is to iterate the logistic map (here represented by $f(x)$ ) to the initial state $x_{0}$ : ${\begin{aligned}x_{1}&=f(x_{0}),\\x_{2}&=f(x_{1})=f(f(x_{0})),\\x_{3}&=f(x_{2})=f(f(f(x_{0}))),\\x_{4}&=\dots \\\end{aligned}}$

This was the initial approach of Henri Poincaré to study dynamical systems and ultimately chaos starting from the study of fixed points or, in other words, states that do not change over time (i.e. when $x_{n}=...=x_{1}=x_{0}=f(x_{0})$ ). Many chaotic systems such as the Mandelbrot set emerge from iteration of very simple quadratic nonlinear functions such as the logistic map.

### Demographic model example

Taking the biological population model as an example xn is a number between zero and one, which represents the ratio of existing population to the maximum possible population. This nonlinear difference equation is intended to capture two effects:

- *reproduction*, where the population will increase at a rate proportional to the current population when the population size is small,
- *starvation* (density-dependent mortality), where the growth rate will decrease at a rate proportional to the value obtained by taking the theoretical "carrying capacity" of the environment less the current population.

The usual values of interest for the parameter r are those in the interval [0, 4], so that xn remains bounded on [0, 1]. The *r* = 4 case of the logistic map is a nonlinear transformation of both the bit-shift map and the *μ* = 2 case of the tent map. If *r* > 4, this leads to negative population sizes. (This problem does not appear in the older Ricker model, which also exhibits chaotic dynamics.) One can also consider values of r in the interval [−2, 0], so that xn remains bounded on [−0.5, 1.5].

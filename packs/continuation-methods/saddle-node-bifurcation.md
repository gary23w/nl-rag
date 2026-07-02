---
title: "Saddle-node bifurcation"
source: https://en.wikipedia.org/wiki/Saddle-node_bifurcation
domain: continuation-methods
license: CC-BY-SA-4.0
tags: numerical continuation, homotopy continuation, bifurcation theory, predictor-corrector method
fetched: 2026-07-02
---

# Saddle-node bifurcation

In the mathematical area of bifurcation theory a **saddle-node bifurcation**, **tangential bifurcation** or **fold bifurcation** is a local bifurcation in which two fixed points (or equilibria) of a dynamical system collide and annihilate each other. The term 'saddle-node bifurcation' is most often used in reference to continuous dynamical systems. In discrete dynamical systems, the same bifurcation is often instead called a **fold bifurcation**. Another name is **blue sky bifurcation** in reference to the sudden creation of two fixed points.

If the phase space is one-dimensional, one of the equilibrium points is unstable (the saddle), while the other is stable (the node).

Saddle-node bifurcations may be associated with hysteresis loops and catastrophes.

## Normal form

A typical example of a differential equation with a saddle-node bifurcation is:

${\frac {dx}{dt}}=r+x^{2}.$

Here x is the state variable and r is the bifurcation parameter.

- If $r<0$ there are two equilibrium points, a stable equilibrium point at $-{\sqrt {-r}}$ and an unstable one at $+{\sqrt {-r}}$ .
- At $r=0$ (the bifurcation point) there is exactly one equilibrium point. At this point the fixed point is no longer hyperbolic. In this case the fixed point is called a saddle-node fixed point.
- If $r>0$ there are no equilibrium points.

In fact, this is a normal form of a saddle-node bifurcation. A scalar differential equation ${\tfrac {dx}{dt}}=f(r,x)$ which has a fixed point at $x=0$ for $r=0$ with ${\tfrac {\partial f}{\partial x}}(0,0)=0$ is locally topologically equivalent to ${\frac {dx}{dt}}=r\pm x^{2}$ , provided it satisfies ${\tfrac {\partial ^{2}\!f}{\partial x^{2}}}(0,0)\neq 0$ and ${\tfrac {\partial f}{\partial r}}(0,0)\neq 0$ . The first condition is the nondegeneracy condition and the second condition is the transversality condition.

## Example in two dimensions

An example of a saddle-node bifurcation in two dimensions occurs in the two-dimensional dynamical system:

${\frac {dx}{dt}}=\alpha -x^{2}$

${\frac {dy}{dt}}=-y.$

As can be seen by the animation obtained by plotting phase portraits by varying the parameter $\alpha$ ,

- When $\alpha$ is negative, there are no equilibrium points.
- When $\alpha =0$ , there is a saddle-node point.
- When $\alpha$ is positive, there are two equilibrium points: that is, one saddle point and one node (either an attractor or a repellor).

Other examples are in modelling biological switches. Recently, it was shown that under certain conditions, the Einstein field equations of General Relativity have the same form as a fold bifurcation. A non-autonomous version of the saddle-node bifurcation (i.e. the parameter is time-dependent) has also been studied.

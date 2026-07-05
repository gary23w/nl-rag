---
title: "Action (physics)"
source: https://en.wikipedia.org/wiki/Action_(physics)
domain: angular-displacement
license: CC-BY-SA-4.0
tags: angular displacement
fetched: 2026-07-05
---

# Action (physics)

In physics, **action** is a scalar quantity that describes how the balance of kinetic versus potential energy of a physical system changes with trajectory. Action is significant because it is an input to the principle of stationary action, an approach to classical mechanics that is simpler for multiple objects. Action and the variational principle are used in Feynman's formulation of quantum mechanics and in general relativity. For systems with small values of action close to the Planck constant, quantum effects are significant.

In the simple case of a single particle moving with a constant velocity (thereby undergoing uniform linear motion), the action is the momentum of the particle times the distance it moves, added up along its path; equivalently, action is the difference between the particle's kinetic energy and its potential energy, times the duration for which it has that amount of energy.

More formally, action is a mathematical functional which takes the trajectory (also called path or history) of the system as its argument and has a real number as its result. Generally, the action takes different values for different paths. Action has dimensions of energy × time or momentum × length, and its SI unit is joule-second (like the Planck constant h).

## Introduction

Introductory physics often begins with Newton's laws of motion, relating force and motion; action is part of a completely equivalent alternative approach with practical and educational advantages. However, the concept took many decades to supplant Newtonian approaches and remains a challenge to introduce to students.

### Simple example

For a trajectory of a ball moving in the air on Earth the **action** is defined between two points in time, *t*1 and *t*2 as the kinetic energy (KE) minus the potential energy (PE), integrated over time. $S=\int _{t_{1}}^{t_{2}}{\bigl (}\mathrm {KE} (t)-\mathrm {PE} (t){\bigr )}dt$ The action balances kinetic against potential energy.

The kinetic energy of a ball of mass m is ⁠1/2⁠*mv*2 where v is the velocity of the ball; the potential energy is mgx where g is the acceleration due to gravity and x its height. Then the action between *t*1 and *t*2 is $S=\int _{t_{1}}^{t_{2}}\left({\tfrac {1}{2}}mv^{2}(t)-mgx(t)\right)dt$ The action value depends upon the trajectory taken by the ball through *x*(*t*) and *v*(*t*). This makes the action an input to the powerful stationary-action principle for classical and for quantum mechanics. Newton's equations of motion for the ball can be derived from the action using the stationary-action principle, but the advantages of action-based mechanics only begin to appear in cases where Newton's laws are difficult to apply. Replace the ball with an electron: classical mechanics fails but stationary action continues to work. The energy difference in the simple action definition, kinetic minus potential energy, is generalized and called the Lagrangian for more complex cases.

### Planck's quantum of action

The Planck constant, written as h, is the quantum (the minimal possible amount) of action. It is related to the quantum of angular momentum, ħ, by the relation *ħ* = ⁠*h*/2*π*⁠. These constants have units of energy times time. They appear in all significant quantum equations, such as the uncertainty principle and the de Broglie wavelength. Whenever the value of the action approaches the Planck constant, quantum effects are significant.

## History

Pierre Louis Maupertuis and Leonhard Euler working in the 1740s developed early versions of the action principle. Joseph Louis Lagrange clarified the mathematics when he invented the calculus of variations. William Rowan Hamilton made the next big breakthrough, formulating Hamilton's principle in 1853. Hamilton's principle became the cornerstone for classical work with different forms of action until Richard Feynman and Julian Schwinger developed quantum action principles.

## Definitions

Expressed in mathematical language, using the calculus of variations, the evolution of a physical system (that is, how the system actually progresses from one state to another) corresponds to a stationary point (usually, a minimum) of the action. Action has the dimensions of [energy] × [time], and its SI unit is joule-second, which is identical to the unit of angular momentum.

Several different definitions of "the action" are in common use in physics. The action is usually an integral over time. However, when the action pertains to fields, it may be integrated over spatial variables as well. In some cases, the action is integrated along the path followed by the physical system.

The action is typically represented as an integral over time, taken along the path of the system between the initial time and the final time of the development of the system: ${\mathcal {S}}=\int _{t_{1}}^{t_{2}}L\,dt,$ where the integrand L is called the Lagrangian. For the action integral to be well-defined, the trajectory has to be bounded in time and space.

### Action (functional)

Most commonly, the term is used for a functional 𝒮 which takes a function of time and (for fields) space as input and returns a scalar. In classical mechanics, the input function is the evolution **q**(*t*) of the system between times *t*1 and *t*2, where **q** represents the generalized coordinates. The action 𝒮[**q**(*t*)] is defined as the integral of the Lagrangian L for an input evolution between the two times: ${\mathcal {S}}[\mathbf {q} (t)]=\int _{t_{1}}^{t_{2}}L{\bigl (}\mathbf {q} (t),{\dot {\mathbf {q} }}(t),t{\bigr )}\,dt,$ where the endpoints of the evolution are fixed and defined as **q**1 = **q**(*t*1) and **q**2 = **q**(*t*2). According to Hamilton's principle, the true evolution **q**true(*t*) is an evolution for which the action 𝒮[**q**(*t*)] is stationary (a minimum, maximum, or a saddle point). This principle results in the equations of motion in Lagrangian mechanics.

### Abbreviated action (functional)

In addition to the action functional, there is another functional called the *abbreviated action*. In the abbreviated action, the input function is the *path* followed by the physical system without regard to its parameterization by time. For example, the path of a planetary orbit is an ellipse, and the path of a particle in a uniform gravitational field is a parabola; in both cases, the path does not depend on how fast the particle traverses the path.

The abbreviated action 𝒮0 (sometimes written as W) is defined as the integral of the generalized momenta, $p_{i}={\frac {\partial L(q,t)}{\partial {\dot {q}}_{i}}},$ for a system Lagrangian L along a path in the generalized coordinates *qi*: ${\mathcal {S}}_{0}=\int _{q_{1}}^{q_{2}}\mathbf {p} \cdot d\mathbf {q} =\int _{q_{1}}^{q_{2}}\sum _{i}p_{i}\,dq_{i}.$ where *q*1 and *q*2 are the starting and ending coordinates. According to Maupertuis's principle, the true path of the system is a path for which the abbreviated action is stationary.

### Hamilton's characteristic function

When the total energy E is conserved, the Hamilton–Jacobi equation can be solved with the additive separation of variables: $S(q_{1},\dots ,q_{N},t)=W(q_{1},\dots ,q_{N})-E\cdot t,$ where the time-independent function *W*(*q*1,*q*2,…,*qN*) is called *Hamilton's characteristic function*. The physical significance of this function is understood by taking its total time derivative

${\frac {dW}{dt}}={\frac {\partial W}{\partial q_{i}}}{\dot {q}}_{i}=p_{i}{\dot {q}}_{i}.$

This can be integrated to give

$W(q_{1},\dots ,q_{N})=\int p_{i}{\dot {q}}_{i}\,dt=\int p_{i}\,dq_{i},$

which is just the abbreviated action.

### Action of a generalized coordinate

A variable *Jk* in the action-angle coordinates, called the "action" of the generalized coordinate *qk*, is defined by integrating a single generalized momentum around a closed path in phase space, corresponding to rotating or oscillating motion:

$J_{k}=\oint p_{k}\,dq_{k}$

The corresponding canonical variable conjugate to *Jk* is its "angle" *wk*, for reasons described more fully under action-angle coordinates. The integration is only over a single variable *qk* and, therefore, unlike the integrated dot product in the abbreviated action integral above. The *Jk* variable equals the change in *Sk*(*qk*) as *qk* is varied around the closed path. For several physical systems of interest, *Jk* is either a constant or varies very slowly; hence, the variable *Jk* is often used in perturbation calculations and in determining adiabatic invariants. For example, they are used in the calculation of planetary and satellite orbits.

### Single relativistic particle

When relativistic effects are significant, the action of a point particle of mass m travelling a world line C parametrized by the proper time τ is $S=-mc^{2}\int _{C}\,d\tau .$

If instead, the particle is parametrized by the coordinate time t of the particle and the coordinate time ranges from *t*1 to *t*2, then the action becomes $S=\int _{t1}^{t2}L\,dt,$ where the Lagrangian is $L=-mc^{2}{\sqrt {-c^{-2}g_{\mu \nu }{\frac {dx^{\mu }}{dt}}{\frac {dx^{\nu }}{dt}}}}\approx -mc^{2}{\sqrt {1-{\frac {v^{2}}{c^{2}}}}},$

where *gμν* is the metric tensor ≈ (−*c*2,1,1,1).

Physical laws are frequently expressed as differential equations, which describe how physical quantities such as position and momentum change continuously with time, space or a generalization thereof. Given the initial and boundary conditions for the situation, the "solution" to these empirical equations is one or more functions that describe the behavior of the system and are called *equations of motion*.

*Action* is a part of an alternative approach to finding such equations of motion. Classical mechanics postulates that the path actually followed by a physical system is that for which the *action is minimized*, or more generally, is stationary. In other words, the action satisfies a variational principle: the principle of stationary action (see also below). The action is defined by an integral, and the classical equations of motion of a system can be derived by minimizing the value of that integral.

The action principle provides deep insights into physics, and is an important concept in modern theoretical physics. Various action principles and related concepts are summarized below.

### Maupertuis's principle

In classical mechanics, Maupertuis's principle (named after Pierre Louis Maupertuis) states that the path followed by a physical system is the one of least length (with a suitable interpretation of path and length). Maupertuis's principle uses the abbreviated action between two generalized points on a path.

### Hamilton's principal function

Hamilton's principle states that the differential equations of motion for *any* physical system can be re-formulated as an equivalent integral equation. Thus, there are two distinct approaches for formulating dynamical models.

Hamilton's principle applies not only to the classical mechanics of a single particle, but also to classical fields such as the electromagnetic and gravitational fields. Hamilton's principle has also been extended to quantum mechanics and quantum field theory—in particular the path integral formulation of quantum mechanics makes use of the concept—where a physical system explores all possible paths, with the phase of the probability amplitude for each path being determined by the action for the path; the final probability amplitude adds all paths using their complex amplitude and phase.

### Hamilton–Jacobi equation

Hamilton's principal function *S* = *S*(*q*,*t*;*q*0,*t*0) is obtained from the action functional 𝒮 by fixing the initial time *t*0 and the initial endpoint *q*0, while allowing the upper time limit t and the second endpoint q to vary. The Hamilton's principal function satisfies the Hamilton–Jacobi equation, a formulation of classical mechanics. Due to a similarity with the Schrödinger equation, the Hamilton–Jacobi equation provides, arguably, the most direct link with quantum mechanics.

### Euler–Lagrange equations

In Lagrangian mechanics, the requirement that the action integral be stationary under small perturbations is equivalent to a set of differential equations (called the Euler–Lagrange equations) that may be obtained using the calculus of variations.

### Classical fields

The **action principle** can be extended to obtain the equations of motion for fields, such as the electromagnetic field or gravitational field. Maxwell's equations can be derived as conditions of stationary action.

The Einstein equation utilizes the *Einstein–Hilbert action* as constrained by a variational principle. The trajectory (path in spacetime) of a body in a gravitational field can be found using the action principle. For a free falling body, this trajectory is a geodesic.

### Conservation laws

Implications of symmetries in a physical situation can be found with the action principle, together with the Euler–Lagrange equations, which are derived from the action principle. An example is Noether's theorem, which states that to every continuous symmetry in a physical situation there corresponds a conservation law (and conversely). This deep connection requires that the action principle be assumed.

### Path integral formulation of quantum field theory

In quantum mechanics, the system does not follow a single path whose action is stationary, but the behavior of the system depends on all permitted paths and the value of their action. The action corresponding to the various paths is used to calculate the path integral, which gives the probability amplitudes of the various outcomes.

Although equivalent in classical mechanics with Newton's laws, the **action principle** is better suited for generalizations and plays an important role in modern physics. Indeed, this principle is one of the great generalizations in physical science. It is best understood within quantum mechanics, particularly in Richard Feynman's path integral formulation, where it arises out of destructive interference of quantum amplitudes.

### Modern extensions

The action principle can be generalized still further. For example, the action need not be an integral, because nonlocal actions are possible. The configuration space need not even be a functional space, given certain features such as noncommutative geometry. However, a physical basis for these mathematical extensions remains to be established experimentally.

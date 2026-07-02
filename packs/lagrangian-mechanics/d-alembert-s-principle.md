---
title: "d'Alembert's principle"
source: https://en.wikipedia.org/wiki/D'Alembert's_principle
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
---

# d'Alembert's principle

**D'Alembert's principle**, also known as the **Lagrange–d'Alembert principle**, is a statement of the fundamental classical laws of motion. It is named after its discoverer, the French physicist and mathematician Jean le Rond d'Alembert, and Italian-French mathematician Joseph Louis Lagrange. D'Alembert's principle generalizes the principle of virtual work from static to dynamical systems by introducing *forces of inertia* which, when added to the applied forces in a system, result in *dynamic equilibrium*.

D'Alembert's principle can be applied in cases of kinematic constraints that depend on velocities. The principle does not apply for irreversible displacements, such as sliding friction, and more general specification of the irreversibility is required.

## Statement of the principle

The principle states that the sum of the differences between the forces acting on a system of massive particles and the time derivatives of the momenta of the system itself projected onto any virtual displacement consistent with the constraints of the system is zero. Thus, in mathematical notation, d'Alembert's principle is written as follows, $\sum _{i}(\mathbf {F} _{i}-m_{i}{\dot {\mathbf {v} }}_{i}-{\dot {m}}_{i}\mathbf {v} _{i})\cdot \delta \mathbf {r} _{i}=0,$

where:

- i is an integer used to indicate (via subscript) a variable corresponding to a particular particle in the system,
- $\mathbf {F} _{i}$ is the total applied force (excluding constraint forces) on the i -th particle,
- $m_{i}$ is the mass of the i -th particle,
- $\mathbf {v} _{i}$ is the velocity of the i -th particle,
- $\delta \mathbf {r} _{i}$ is the virtual displacement of the i -th particle, consistent with the constraints.

Newton's dot notation is used to represent the derivative with respect to time. The above equation is often called d'Alembert's principle, but it was first written in this variational form by Joseph Louis Lagrange. D'Alembert's contribution was to demonstrate that in the totality of a dynamic system the forces of constraint vanish. That is to say that the generalized forces $\mathbf {Q} _{j}$ need not include constraint forces. It is equivalent to the somewhat more cumbersome Gauss's principle of least constraint.

## Derivations

### General case with variable mass

The general statement of d'Alembert's principle mentions "the time derivatives of the momenta of the system." By Newton's second law, the first time derivative of momentum is the force. The momentum of the i -th mass is the product of its mass and velocity: $\mathbf {p} _{i}=m_{i}\mathbf {v} _{i}$ and its time derivative is ${\dot {\mathbf {p} }}_{i}={\dot {m}}_{i}\mathbf {v} _{i}+m_{i}{\dot {\mathbf {v} }}_{i}.$

In many applications, the masses are constant and this equation reduces to ${\dot {\mathbf {p} }}_{i}=m_{i}{\dot {\mathbf {v} }}_{i}=m_{i}\mathbf {a} _{i}.$

However, some applications involve changing masses (for example, chains being rolled up or being unrolled) and in those cases both terms ${\dot {m}}_{i}\mathbf {v} _{i}$ and $m_{i}{\dot {\mathbf {v} }}_{i}$ have to remain present, giving $\sum _{i}(\mathbf {F} _{i}-m_{i}\mathbf {a} _{i}-{\dot {m}}_{i}\mathbf {v} _{i})\cdot \delta \mathbf {r} _{i}=0.$ If the variable mass is ejected with a velocity $\mathbf {w} _{i}$ the principle has an additional term: $\sum _{i}(\mathbf {F} _{i}-m_{i}\mathbf {a} _{i}-{\dot {m}}_{i}(\mathbf {v} _{i}-\mathbf {w} _{i}))\cdot \delta \mathbf {r} _{i}=0.$

### Special case with constant mass

Consider Newton's law for a system of particles of constant mass, i . The total force on each particle is $\mathbf {F} _{i}^{(T)}=m_{i}\mathbf {a} _{i},$ where

- $\mathbf {F} _{i}^{(T)}$ are the total forces acting on the system's particles,
- $m_{i}\mathbf {a} _{i}$ are the inertial forces that result from the total forces.

Moving the inertial forces to the left gives an expression that can be considered to represent quasi-static equilibrium, but which is really just a small algebraic manipulation of Newton's law: $\mathbf {F} _{i}^{(T)}-m_{i}\mathbf {a} _{i}=\mathbf {0} .$

Considering the virtual work, $\delta W$ , done by the total and inertial forces together through an arbitrary virtual displacement, $\delta \mathbf {r} _{i}$ , of the system leads to a zero identity, since the forces involved sum to zero for each particle.

$\delta W=\sum _{i}\mathbf {F} _{i}^{(T)}\cdot \delta \mathbf {r} _{i}-\sum _{i}m_{i}\mathbf {a} _{i}\cdot \delta \mathbf {r} _{i}=0$

The original vector equation could be recovered by recognizing that the work expression must hold for arbitrary displacements. Separating the total forces into applied forces, $\mathbf {F} _{i}$ , and constraint forces, $\mathbf {C} _{i}$ , yields $\delta W=\sum _{i}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}+\sum _{i}\mathbf {C} _{i}\cdot \delta \mathbf {r} _{i}-\sum _{i}m_{i}\mathbf {a} _{i}\cdot \delta \mathbf {r} _{i}=0.$

If arbitrary virtual displacements are assumed to be in directions that are orthogonal to the constraint forces (which is not usually the case, so this derivation works only for special cases), the constraint forces don't do any work, ${\textstyle \sum _{i}\mathbf {C} _{i}\cdot \delta \mathbf {r} _{i}=0}$ . Such displacements are said to be *consistent* with the constraints. This leads to the formulation of *d'Alembert's principle*, which states that the difference of applied forces and inertial forces for a dynamic system does no virtual work: $\delta W=\sum _{i}(\mathbf {F} _{i}-m_{i}\mathbf {a} _{i})\cdot \delta \mathbf {r} _{i}=0.$

There is also a corresponding principle for static systems called the principle of virtual work for applied forces.

## D'Alembert's principle of inertial forces

D'Alembert showed that one can transform an accelerating rigid body into an equivalent static system by adding the so-called "inertial force" and "inertial torque" or moment. The inertial force must act through the center of mass and the inertial torque can act anywhere. The system can then be analyzed exactly as a static system subjected to this "inertial force and moment" and the external forces. The advantage is that in the equivalent static system one can take moments about any point (not just the center of mass). This often leads to simpler calculations because any force (in turn) can be eliminated from the moment equations by choosing the appropriate point about which to apply the moment equation (sum of moments = zero). Even in the course of Fundamentals of Dynamics and Kinematics of machines, this principle helps in analyzing the forces that act on a link of a mechanism when it is in motion. In textbooks of engineering dynamics, this is sometimes referred to as *d'Alembert's principle*.

Some educators caution that attempts to use d'Alembert inertial mechanics lead students to make frequent sign errors. A potential cause for these errors is the sign of the inertial forces. Inertial forces can be used to describe an apparent force in a non-inertial reference frame that has an acceleration $\mathbf {a}$ with respect to an inertial reference frame. In such a non-inertial reference frame, a mass that is at rest and has zero acceleration in an inertial reference system, because no forces are acting on it, will still have an acceleration $-\mathbf {a}$ and an apparent inertial, or pseudo or fictitious force $-m\mathbf {a}$ will seem to act on it: in this situation the inertial force has a minus sign.

## Dynamic equilibrium

D'Alembert's form of the principle of virtual work states that a system of rigid bodies is in dynamic equilibrium when the virtual work of the sum of the applied forces and the inertial forces is zero for any virtual displacement of the system. Thus, dynamic equilibrium of a system of n rigid bodies with m generalized coordinates requires $\delta W=\left(Q_{1}+Q_{1}^{*}\right)\delta q_{1}+\dots +\left(Q_{m}+Q_{m}^{*}\right)\delta q_{m}=0,$ for any set of virtual displacements $\delta q_{j}$ with $Q_{j}$ being a generalized applied force and $Q_{j}^{*}$ being a generalized inertia force. This condition yields m equations, $Q_{j}+Q_{j}^{*}=0,\quad j=1,\ldots ,m,$ which can also be written as ${\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}=Q_{j},\quad j=1,\ldots ,m.$ The result is a set of m equations of motion that define the dynamics of the rigid body system.

## Formulation using the Lagrangian

D'Alembert's principle can be rewritten in terms of the Lagrangian $L=T-V$ of the system as a generalized version of Hamilton's principle for the case of point particles, as follows, $\delta \int _{t_{1}}^{t_{2}}L(\mathbf {r} ,{\dot {\mathbf {r} }},t)dt+\sum _{i}\int _{t_{1}}^{t_{2}}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}dt=0,$ where:

- $\mathbf {r} =(\mathbf {r} _{1},...,\mathbf {r} _{N})$

- $\mathbf {F} _{i}$ are the applied forces

- $\delta \mathbf {r} _{i}$ is the virtual displacement of the i -th particle, consistent with the constraints $\sum _{i}\mathbf {C} _{i}\cdot \delta \mathbf {r} _{i}=0$
- the critical curve satisfies the constraints $\sum _{i}\mathbf {C} _{i}\cdot {\dot {\mathbf {r} }}_{i}=0$

With the Lagrangian $L(\mathbf {r} ,{\dot {\mathbf {r} }},t)=\sum _{i}{\frac {1}{2}}m_{i}{\dot {\mathbf {r} }}_{i}^{2},$ the previous statement of d'Alembert principle is recovered.

## Generalization for thermodynamics

An extension of d'Alembert's principle can be used in thermodynamics. For instance, for an adiabatically closed thermodynamic system described by a Lagrangian depending on a single entropy *S* and with constant masses $m_{i}$ , such as $L(\mathbf {r} ,{\dot {\mathbf {r} }},S,t)=\sum _{i}{\frac {1}{2}}m_{i}{\dot {\mathbf {r} }}_{i}^{2}-V(\mathbf {r} ,S),$ it is written as follows $\delta \int _{t_{1}}^{t_{2}}L(\mathbf {r} ,{\dot {\mathbf {r} }},S,t)dt+\sum _{i}\int _{t_{1}}^{t_{2}}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}dt=0,$ where the previous constraints ${\textstyle \sum _{i}\mathbf {C} _{i}\cdot \delta \mathbf {r} _{i}=0}$ and ${\textstyle \sum _{i}\mathbf {C} _{i}\cdot {\dot {\mathbf {r} }}_{i}=0}$ are generalized to involve the entropy as:

- $\sum _{i}\mathbf {C} _{i}\cdot \delta \mathbf {r} _{i}+T\delta S=0$
- $\sum _{i}\mathbf {C} _{i}\cdot {\dot {\mathbf {r} }}_{i}+T{\dot {S}}=0.$

Here $T=\partial V/\partial S$ is the temperature of the system, $\mathbf {F} _{i}$ are the external forces, $\mathbf {C} _{i}$ are the internal dissipative forces. It results in the mechanical and thermal balance equations: $m_{i}\mathbf {a} _{i}=-{\frac {\partial V}{\partial \mathbf {r} _{i}}}+\mathbf {C} _{i}+\mathbf {F} _{i},\;\;i=1,...,N\qquad \qquad T{\dot {S}}=-\sum _{i}\mathbf {C} _{i}\cdot {\dot {\mathbf {r} }}_{i}.$ Typical applications of the principle include thermo-mechanical systems, membrane transport, and chemical reactions.

For $\delta S={\dot {S}}=0$ the classical d'Alembert principle and equations are recovered.

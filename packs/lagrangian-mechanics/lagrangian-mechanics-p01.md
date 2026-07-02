---
title: "Lagrangian mechanics (part 1/2)"
source: https://en.wikipedia.org/wiki/Lagrangian_mechanics
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
part: 1/2
---

# Lagrangian mechanics

In physics, **Lagrangian mechanics** is an alternate formulation of classical mechanics founded on the d'Alembert principle of virtual work. It was introduced by the Italian-French mathematician and astronomer Joseph-Louis Lagrange in his presentation to the Turin Academy of Science in 1760 culminating in his 1788 grand opus, *Mécanique analytique*. Lagrange's approach greatly simplifies the analysis of many problems in mechanics, and it had crucial influence on other branches of physics, including relativity and quantum field theory.

Lagrangian mechanics describes a mechanical system as a pair (*M*, *L*) consisting of a configuration space *M* and a smooth function ${\textstyle L}$ within that space called a ***Lagrangian***. For many systems, *L* = *T* − *V*, where *T* and *V* are the kinetic and potential energy of the system, respectively.

The stationary action principle requires that the action functional of the system derived from *L* must remain at a stationary point (specifically, a maximum, minimum, or saddle point) throughout the time evolution of the system. This constraint allows the calculation of the equations of motion of the system using Lagrange's equations.


## Introduction

Newton's laws and the concept of forces are the usual starting point for teaching about mechanical systems. This method works well for many problems, but for others the approach is nightmarishly complicated. For example, in calculation of the motion of a torus rolling on a horizontal surface with a pearl sliding inside, the time-varying constraint forces like the angular velocity of the torus and the motion of the pearl in relation to the torus made it difficult to determine the motion of the torus with Newton's equations. Lagrangian mechanics adopts energy rather than force as its basic ingredient, leading to more abstract equations capable of tackling more complex problems.

Particularly, Lagrange's approach was to set up independent generalized coordinates for the position and speed of every object, which allows the writing down of a general form of the Lagrangian (total kinetic energy minus potential energy of the system) and summing this over all possible paths of motion of the particles yielded a formula for the 'action', which he minimized to give a generalized set of equations. This summed quantity is minimized along the path that the particle actually takes. This choice eliminates the need for the constraint force to enter into the resultant generalized system of equations. There are fewer equations since one is not directly calculating the influence of the constraint on the particle at a given moment.

For a wide variety of physical systems, if the size and shape of a massive object are negligible, it is a useful simplification to treat it as a point particle. For a system of *N* point particles with masses *m*1, *m*2, ..., *mN*, each particle has a position vector, denoted **r**1, **r**2, ..., **r***N*. Cartesian coordinates are often sufficient, so **r**1 = (*x*1, *y*1, *z*1), **r**2 = (*x*2, *y*2, *z*2) and so on. In three-dimensional space, each position vector requires three coordinates to uniquely define the location of a point, so there are 3*N* coordinates to uniquely define the configuration of the system. These are all specific points in space to locate the particles; a general point in space is written **r** = (*x*, *y*, *z*). The velocity of each particle is how fast the particle moves along its path of motion, and is the time derivative of its position, thus $\mathbf {v} _{1}={\frac {d\mathbf {r} _{1}}{dt}},\mathbf {v} _{2}={\frac {d\mathbf {r} _{2}}{dt}},\ldots ,\mathbf {v} _{N}={\frac {d\mathbf {r} _{N}}{dt}}.$ In Newtonian mechanics, the equations of motion are given by Newton's laws. The second law "net force equals mass times acceleration", $\sum \mathbf {F} =m{\frac {d^{2}\mathbf {r} }{dt^{2}}},$ applies to each particle. For an *N*-particle system in 3 dimensions, there are 3*N* second-degree ordinary differential equations in the positions of the particles to solve for.

### Lagrangian

Instead of forces, Lagrangian mechanics uses the energies in the system. The central quantity of Lagrangian mechanics is the **Lagrangian**, a function which summarizes the dynamics of the entire system. Overall, the Lagrangian has units of energy, but no single expression for all physical systems. Any function which generates the correct equations of motion, in agreement with physical laws, can be taken as a Lagrangian. It is nevertheless possible to construct general expressions for large classes of applications. The *non-relativistic* Lagrangian for a system of particles in the absence of an electromagnetic field is given by $L=T-V,$ where $T={\frac {1}{2}}\sum _{k=1}^{N}m_{k}v_{k}^{2}$ is the total kinetic energy of the system, equaling the sum Σ of the kinetic energies of the N particles. Each particle labeled k has mass $m_{k},$ and *v**k*2 = **v***k* · **v***k* is the magnitude squared of its velocity, equivalent to the dot product of the velocity with itself.

Kinetic energy *T* is the energy of the system's motion and is a function only of the velocities **v***k*, not the positions **r***k*, nor time *t*, so *T* = *T*(**v**1, **v**2, ...).

*V*, the potential energy of the system, reflects the energy of interaction between the particles, i.e. how much energy any one particle has due to all the others, together with any external influences. For conservative forces (e.g. Newtonian gravity), it is a function of the position vectors of the particles only, so *V* = *V*(**r**1, **r**2, ...). For those non-conservative forces which can be derived from an appropriate potential (e.g. electromagnetic potential), the velocities will appear also, *V* = *V*(**r**1, **r**2, ..., **v**1, **v**2, ...). If there is some external field or external driving force changing with time, the potential changes with time, so most generally *V* = *V*(**r**1, **r**2, ..., **v**1, **v**2, ..., *t*).

### Mathematical formulation (for finite particle systems)

An equivalent but more mathematically formal definition of the Lagrangian is as follows. For a system of *N* particles in three-dimensional space, the configuration space of the system is a smooth manifold $Q\subseteq \mathbb {R} ^{3N}$ , where each configuration $q\in Q$ specifies the spatial positions of each of the particles at a given instant of time, and the manifold is composed of all the configurations that are allowed by the constraints on the system.

The Lagrangian is a smooth function: $L:TQ\times \mathbb {R} \to \mathbb {R} ,$ where $TQ\subseteq \mathbb {R} ^{6N}$ is the tangent bundle of the configuration space. That is, each element in $TQ$ represents both the positions and the velocities of the particles, and can be written as a tuple $(q_{1},\ldots ,q_{N},{\dot {q}}_{1},\ldots {\dot {q}}_{N})$ with $q_{i}$ and ${\dot {q}}_{i}$ specifying a position and a velocity of the i'th particle respectively. The time dependence $t\in \mathbb {R}$ allows for the Lagrangian to describe time-dependent forces or potentials.

A trajectory of the system is a smooth function $q:[t_{0},t_{1}]\to Q,$ describing the evolution of the configuration over time. Its velocity is the time derivative ${\dot {q}}(t)\in T_{q(t)}Q$ of $q(t)$ , and the pair $(q(t),{\dot {q}}(t))\in TQ$ is thus an element of the bundle for any t . The action functional of the trajectory can therefore be defined as the integral of the Lagrangian along the path: $S[q]=\int _{t_{0}}^{t_{1}}L(q(t),{\dot {q}}(t),t)\,dt.$

The laws of motion in Lagrangian mechanics are derived from the postulate that among all trajectories between two given configurations, the actual one that will be taken by the system must be a critical point (often but not necessarily a local minimum) of the action functional. This leads to the Euler–Lagrange equations (see also below).


## Equations of motion

For a system of particles with masses $m_{1},\ldots ,m_{N}$ , the kinetic energy is: $T(q,{\dot {q}})={\frac {1}{2}}\sum _{i=1}^{N}m_{i}\|{\dot {q}}_{i}\|^{2},$ where ${\dot {q}}_{i}\in \mathbb {R} ^{3}$ is the velocity of particle *i*.

The potential energy $V(q,t)$ depends only on the configuration (and possibly on time), and typically arises from conservative forces.

The standard *Lagrangian* is given by the difference: $L(q,{\dot {q}},t)=T(q,{\dot {q}})-V(q,t).$

This formulation covers both conservative and time-dependent systems and forms the basis for generalizations to continuous systems (fields), constrained systems, and systems with curved configuration spaces.

If *T* or *V* or both depend explicitly on time due to time-varying constraints or external influences, the Lagrangian *L*(**r**1, **r**2, ... **v**1, **v**2, ... *t*) is *explicitly time-dependent*. If neither the potential nor the kinetic energy depend on time, then the Lagrangian *L*(**r**1, **r**2, ... **v**1, **v**2, ...) is *explicitly independent of time*. In either case, the Lagrangian always has implicit time dependence through the generalized coordinates.

With these definitions, *Lagrange's equations* are

Lagrange's equations

${\frac {\partial L}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {\mathbf {r} }}_{k}}}+\sum _{i=1}^{C}\lambda _{i}{\frac {\partial f_{i}}{\partial \mathbf {r} _{k}}}=0,$

where *k* = 1, 2, ..., *N* labels the particles, there is a Lagrange multiplier *λi* for each constraint equation *f**i*, and ${\frac {\partial }{\partial \mathbf {r} _{k}}}\equiv \left({\frac {\partial }{\partial x_{k}}},{\frac {\partial }{\partial y_{k}}},{\frac {\partial }{\partial z_{k}}}\right),\quad {\frac {\partial }{\partial {\dot {\mathbf {r} }}_{k}}}\equiv \left({\frac {\partial }{\partial {\dot {x}}_{k}}},{\frac {\partial }{\partial {\dot {y}}_{k}}},{\frac {\partial }{\partial {\dot {z}}_{k}}}\right)$ are each shorthands for a vector of partial derivatives ∂/∂ with respect to the indicated variables (not a derivative with respect to the entire vector). Each overdot is a shorthand for a time derivative. This procedure does increase the number of equations to solve compared to Newton's laws, from 3*N* to 3*N* + *C*, because there are 3*N* coupled second-order differential equations in the position coordinates and multipliers, plus *C* constraint equations. However, when solved alongside the position coordinates of the particles, the multipliers can yield information about the constraint forces. The coordinates do not need to be eliminated by solving the constraint equations.

In the Lagrangian, the position coordinates and velocity components are all independent variables, and derivatives of the Lagrangian are taken with respect to these separately according to the usual differentiation rules (e.g. the partial derivative of *L* with respect to the *z* velocity component of particle 2, defined by *v**z*,2 = *dz*2/*dt*, is just ∂*L*/∂*v**z*,2; no awkward chain rules or total derivatives need to be used to relate the velocity component to the corresponding coordinate *z*2).

In each constraint equation, one coordinate is redundant because it is determined from the other coordinates. The number of *independent* coordinates is therefore *n* = 3*N* − *C*. We can transform each position vector to a common set of *n* generalized coordinates, conveniently written as an *n*-tuple **q** = (*q*1, *q*2, ... *qn*), by expressing each position vector, and hence the position coordinates, as functions of the generalized coordinates and time: $\mathbf {r} _{k}=\mathbf {r} _{k}(\mathbf {q} ,t)={\big (}x_{k}(\mathbf {q} ,t),y_{k}(\mathbf {q} ,t),z_{k}(\mathbf {q} ,t),t{\big )}.$

The vector **q** is a point in the configuration space of the system. The time derivatives of the generalized coordinates are called the generalized velocities, and for each particle the transformation of its velocity vector, the total derivative of its position with respect to time, is ${\dot {q}}_{j}={\frac {\mathrm {d} q_{j}}{\mathrm {d} t}},\quad \mathbf {v} _{k}=\sum _{j=1}^{n}{\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}{\dot {q}}_{j}+{\frac {\partial \mathbf {r} _{k}}{\partial t}}.$

Given this **v***k*, the kinetic energy *in generalized coordinates* depends on the generalized velocities, generalized coordinates, and time if the position vectors depend explicitly on time due to time-varying constraints, so $T=T(\mathbf {q} ,{\dot {\mathbf {q} }},t).$

With these definitions, the **Euler–Lagrange equations**,

Lagrange's equations

${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {\partial L}{\partial {\dot {q}}_{j}}}\right)={\frac {\partial L}{\partial q_{j}}}$

are mathematical results from the calculus of variations, which can also be used in mechanics. Substituting in the Lagrangian *L*(**q**, d**q**/d*t*, *t*) gives the equations of motion of the system. The number of equations has decreased compared to Newtonian mechanics, from 3*N* to *n* = 3*N* − *C* coupled second-order differential equations in the generalized coordinates. These equations do not include constraint forces at all, only non-constraint forces need to be accounted for.

Although the equations of motion include partial derivatives, the results of the partial derivatives are still ordinary differential equations in the position coordinates of the particles. The total time derivative denoted d/d*t* often involves implicit differentiation. Both equations are linear in the Lagrangian, but generally are nonlinear coupled equations in the coordinates.

### Extensions

As already noted, this form of *L* is applicable to many important classes of system, but not everywhere. For relativistic Lagrangian mechanics it must be replaced as a whole by a function consistent with special relativity (scalar under Lorentz transformations) or general relativity (4-scalar). Where a magnetic field is present, the expression for the potential energy needs restating. And for dissipative forces (e.g., friction), another function must be introduced alongside Lagrangian often referred to as a "Rayleigh dissipation function" to account for the loss of energy.

One or more of the particles may each be subject to one or more holonomic constraints; such a constraint is described by an equation of the form *f*(**r**, *t*) = 0. If the number of constraints in the system is *C*, then each constraint has an equation *f*1(**r**, *t*) = 0, *f*2(**r**, *t*) = 0, ..., *fC*(**r**, *t*) = 0, each of which could apply to any of the particles. If particle *k* is subject to constraint *i*, then *fi*(**r***k*, *t*) = 0. At any instant of time, the coordinates of a constrained particle are linked together and not independent. The constraint equations determine the allowed paths the particles can move along, but not where they are or how fast they go at every instant of time. Nonholonomic constraints depend on the particle velocities, accelerations, or higher derivatives of position. Lagrangian mechanics *can only be applied to systems whose constraints, if any, are all holonomic*. Three examples of nonholonomic constraints are: when the constraint equations are non-integrable, when the constraints have inequalities, or when the constraints involve complicated non-conservative forces like friction. Nonholonomic constraints require special treatment, and one may have to revert to Newtonian mechanics or use other methods.


## From Newtonian to Lagrangian mechanics

### Newton's laws

For simplicity, Newton's laws can be illustrated for one particle without much loss of generality (for a system of *N* particles, all of these equations apply to each particle in the system). The equation of motion for a particle of constant mass *m* is Newton's second law of 1687, in modern vector notation $\mathbf {F} =m\mathbf {a} ,$ where **a** is its acceleration and **F** the resultant force acting *on* it. Where the mass is varying, the equation needs to be generalised to take the time derivative of the momentum. In three spatial dimensions, this is a system of three coupled second-order ordinary differential equations to solve, since there are three components in this vector equation. The solution is the position vector **r** of the particle at time *t*, subject to the initial conditions of **r** and **v** when *t* = 0.

Newton's laws are easy to use in Cartesian coordinates, but Cartesian coordinates are not always convenient, and for other coordinate systems the equations of motion can become complicated. In a set of curvilinear coordinates ***ξ*** = (*ξ*1, *ξ*2, *ξ*3), the law in tensor index notation is the *"Lagrangian form"* $F^{a}=m\left({\frac {\mathrm {d} ^{2}\xi ^{a}}{\mathrm {d} t^{2}}}+\Gamma ^{a}{}_{bc}{\frac {\mathrm {d} \xi ^{b}}{\mathrm {d} t}}{\frac {\mathrm {d} \xi ^{c}}{\mathrm {d} t}}\right)=g^{ak}\left({\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial T}{\partial {\dot {\xi }}^{k}}}-{\frac {\partial T}{\partial \xi ^{k}}}\right),\quad {\dot {\xi }}^{a}\equiv {\frac {\mathrm {d} \xi ^{a}}{\mathrm {d} t}},$ where *F**a* is the *a*-th contravariant component of the resultant force acting on the particle, Γ*a**bc* are the Christoffel symbols of the second kind, $T={\frac {1}{2}}mg_{bc}{\frac {\mathrm {d} \xi ^{b}}{\mathrm {d} t}}{\frac {\mathrm {d} \xi ^{c}}{\mathrm {d} t}}$ is the kinetic energy of the particle, and *gbc* the covariant components of the *metric tensor* of the curvilinear coordinate system. All the indices *a*, *b*, *c*, each take the values 1, 2, 3. Curvilinear coordinates are not the same as generalized coordinates.

It may seem like an overcomplication to cast Newton's law in this form, but there are advantages. The acceleration components in terms of the Christoffel symbols can be avoided by evaluating derivatives of the kinetic energy instead. If there is no resultant force acting on the particle, **F** = **0**, it does not accelerate, but moves with constant velocity in a straight line. Mathematically, the solutions of the differential equation are *geodesics*, the curves of extremal length between two points in space (these may end up being minimal, that is the shortest paths, but not necessarily). In flat 3D real space the geodesics are simply straight lines. So for a free particle, Newton's second law coincides with the geodesic equation and states that free particles follow geodesics, the extremal trajectories it can move along. If the particle is subject to forces **F** ≠ **0**, the particle accelerates due to forces acting on it and deviates away from the geodesics it would follow if free. With appropriate extensions of the quantities given here in flat 3D space to 4D curved spacetime, the above form of Newton's law also carries over to Einstein's general relativity, in which case free particles follow geodesics in curved spacetime that are no longer "straight lines" in the ordinary sense.

However, we still need to know the total resultant force **F** acting on the particle, which in turn requires the resultant non-constraint force **N** plus the resultant constraint force **C**, $\mathbf {F} =\mathbf {C} +\mathbf {N} .$

The constraint forces can be complicated, since they generally depend on time. Also, if there are constraints, the curvilinear coordinates are not independent but related by one or more constraint equations.

The constraint forces can either be eliminated from the equations of motion, so only the non-constraint forces remain, or included by including the constraint equations in the equations of motion.

### D'Alembert's principle

One degree of freedom.

Two degrees of freedom.

Constraint force

C

and virtual displacement

δ

r

for a particle of mass

m

confined to a curve. The resultant non-constraint force is

N

.

A fundamental result in analytical mechanics is D'Alembert's principle, introduced in 1708 by Jacques Bernoulli to understand static equilibrium, and developed by D'Alembert in 1743 to solve dynamical problems. The principle asserts for *N* particles the virtual work, i.e. the work along a virtual displacement, $\delta \mathbf {r} _{k}$ , is zero: $\sum _{k=1}^{N}(\mathbf {N} _{k}+\mathbf {C} _{k}-m_{k}\mathbf {a} _{k})\cdot \delta \mathbf {r} _{k}=0.$

The *virtual displacements*, $\delta \mathbf {r} _{k}$ , are by definition infinitesimal changes in the configuration of the system consistent with the constraint forces acting on the system *at an instant of time*, i.e. in such a way that the constraint forces maintain the constrained motion. They are not the same as the actual displacements in the system, which are caused by the resultant constraint and non-constraint forces acting on the particle to accelerate and move it. Virtual work is the work done along a virtual displacement for any force (constraint or non-constraint).

Since the constraint forces act perpendicular to the motion of each particle in the system to maintain the constraints, the total virtual work by the constraint forces acting on the system is zero: $\sum _{k=1}^{N}\mathbf {C} _{k}\cdot \delta \mathbf {r} _{k}=0,$ so that $\sum _{k=1}^{N}(\mathbf {N} _{k}-m_{k}\mathbf {a} _{k})\cdot \delta \mathbf {r} _{k}=0.$

Thus D'Alembert's principle allows us to concentrate on only the applied non-constraint forces, and exclude the constraint forces in the equations of motion. The form shown is also independent of the choice of coordinates. However, it cannot be readily used to set up the equations of motion in an arbitrary coordinate system since the displacements $\delta \mathbf {r} _{k}$ might be connected by a constraint equation, which prevents us from setting the *N* individual summands to 0. We will therefore seek a system of mutually independent coordinates for which the total sum will be 0 if and only if the individual summands are 0. Setting each of the summands to 0 will eventually give us our separated equations of motion.

### Equations of motion from D'Alembert's principle

If there are constraints on particle *k*, then since the coordinates of the position **r***k* = (*x**k*, *y**k*, *z**k*) are linked together by a constraint equation, so are those of the virtual displacements *δ***r***k* = (*δx**k*, *δy**k*, *δz**k*). Since the generalized coordinates are independent, we can avoid the complications with the *δ***r***k* by converting to virtual displacements in the generalized coordinates. These are related in the same form as a total differential, $\delta \mathbf {r} _{k}=\sum _{j=1}^{n}{\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}\delta q_{j}.$

There is no partial time derivative with respect to time multiplied by a time increment, since this is a virtual displacement, one along the constraints in an *instant* of time.

The first term in D'Alembert's principle above is the virtual work done by the non-constraint forces **N***k* along the virtual displacements *δ***r***k*, and can without loss of generality be converted into the generalized analogues by the definition of generalized forces $Q_{j}=\sum _{k=1}^{N}\mathbf {N} _{k}\cdot {\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}},$ so that $\sum _{k=1}^{N}\mathbf {N} _{k}\cdot \delta \mathbf {r} _{k}=\sum _{k=1}^{N}\mathbf {N} _{k}\cdot \sum _{j=1}^{n}{\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}\delta q_{j}=\sum _{j=1}^{n}Q_{j}\delta q_{j}.$

This is half of the conversion to generalized coordinates. It remains to convert the acceleration term into generalized coordinates, which is not immediately obvious. Recalling the Lagrange form of Newton's second law, the partial derivatives of the kinetic energy with respect to the generalized coordinates and velocities can be found to give the desired result: $\sum _{k=1}^{N}m_{k}\mathbf {a} _{k}\cdot {\frac {\partial \mathbf {r} _{k}}{\partial q_{j}}}={\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}.$

Now D'Alembert's principle is in the generalized coordinates as required, $\sum _{j=1}^{n}\left[Q_{j}-\left({\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}\right)\right]\delta q_{j}=0,$ and since these virtual displacements *δq**j* are independent and nonzero, the coefficients can be equated to zero, resulting in **Lagrange's equations** or the **generalized equations of motion**, $Q_{j}={\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}$

These equations are equivalent to Newton's laws *for the non-constraint forces*. The generalized forces in this equation are derived from the non-constraint forces only – the constraint forces have been excluded from D'Alembert's principle and do not need to be found. The generalized forces may be non-conservative, provided they satisfy D'Alembert's principle.

### Euler–Lagrange equations and Hamilton's principle

For a non-conservative force which depends on velocity, it *may* be possible to find a potential energy function *V* that depends on positions and velocities. If the generalized forces *Q**i* can be derived from a potential *V* such that $Q_{j}={\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial V}{\partial {\dot {q}}_{j}}}-{\frac {\partial V}{\partial q_{j}}},$ equating to Lagrange's equations and defining the Lagrangian as *L* = *T* − *V* obtains **Lagrange's equations of the second kind** or the **Euler–Lagrange equations** of motion ${\frac {\partial L}{\partial q_{j}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}_{j}}}=0.$

However, the Euler–Lagrange equations can only account for non-conservative forces *if* a potential can be found as shown. This may not always be possible for non-conservative forces, and Lagrange's equations do not involve any potential, only generalized forces; therefore they are more general than the Euler–Lagrange equations.

The Euler–Lagrange equations also follow from the calculus of variations. The *variation* of the Lagrangian is $\delta L=\sum _{j=1}^{n}\left({\frac {\partial L}{\partial q_{j}}}\delta q_{j}+{\frac {\partial L}{\partial {\dot {q}}_{j}}}\delta {\dot {q}}_{j}\right),\quad \delta {\dot {q}}_{j}\equiv \delta {\frac {\mathrm {d} q_{j}}{\mathrm {d} t}}\equiv {\frac {\mathrm {d} (\delta q_{j})}{\mathrm {d} t}},$ which has a form similar to the total differential of *L*, but the virtual displacements and their time derivatives replace differentials, and there is no time increment in accordance with the definition of the virtual displacements. An integration by parts with respect to time can transfer the time derivative of *δq**j* to the ∂*L*/∂(d*qj*/d*t*), in the process exchanging d(*δq**j*)/d*t* for *δq**j*, allowing the independent virtual displacements to be factorized from the derivatives of the Lagrangian, ${\begin{aligned}\int _{t_{1}}^{t_{2}}\delta L\,\mathrm {d} t&=\int _{t_{1}}^{t_{2}}\sum _{j=1}^{n}\left({\frac {\partial L}{\partial q_{j}}}\delta q_{j}+{\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {\partial L}{\partial {\dot {q}}_{j}}}\delta q_{j}\right)-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}_{j}}}\delta q_{j}\right)\,\mathrm {d} t\\&=\sum _{j=1}^{n}\left[{\frac {\partial L}{\partial {\dot {q}}_{j}}}\delta q_{j}\right]_{t_{1}}^{t_{2}}+\int _{t_{1}}^{t_{2}}\sum _{j=1}^{n}\left({\frac {\partial L}{\partial q_{j}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}_{j}}}\right)\delta q_{j}\,\mathrm {d} t.\end{aligned}}$

Now, if the condition *δq**j*(*t*1) = *δq**j*(*t*2) = 0 holds for all *j*, the terms not integrated are zero. If in addition the entire time integral of *δL* is zero, then because the *δq**j* are independent, and the only way for a definite integral to be zero is if the integrand equals zero, each of the coefficients of *δq**j* must also be zero. Then we obtain the equations of motion. This can be summarized by **Hamilton's principle**: $\int _{t_{1}}^{t_{2}}\delta L\,\mathrm {d} t=0.$

The time integral of the Lagrangian is another quantity called the action, defined as $S=\int _{t_{1}}^{t_{2}}L\,\mathrm {d} t,$ which is a *functional*; it takes in the Lagrangian function for all times between *t*1 and *t*2 and returns a scalar value. Its dimensions are the same as [angular momentum], [energy]·[time], or [length]·[momentum]. With this definition Hamilton's principle is $\delta S=0.$

Instead of thinking about particles accelerating in response to applied forces, one might think of them picking out the path with a stationary action, with the end points of the path in configuration space held fixed at the initial and final times. Hamilton's principle is one of several action principles.

Historically, the idea of finding the shortest path a particle can follow subject to a force motivated the first applications of the calculus of variations to mechanical problems, such as the Brachistochrone problem solved by Jean Bernoulli in 1696, as well as Leibniz, Daniel Bernoulli, L'Hôpital around the same time, and Newton the following year. Newton himself was thinking along the lines of the variational calculus, but did not publish. These ideas in turn lead to the variational principles of mechanics, of Fermat, Maupertuis, Euler, Hamilton, and others.

Hamilton's principle can be applied to nonholonomic constraints if the constraint equations can be put into a certain form, a linear combination of first order differentials in the coordinates. The resulting constraint equation can be rearranged into first order differential equation. This will not be given here.

### Lagrange multipliers and constraints

The Lagrangian *L* can be varied in the Cartesian **r***k* coordinates, for *N* particles, $\int _{t_{1}}^{t_{2}}\sum _{k=1}^{N}\left({\frac {\partial L}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {\mathbf {r} }}_{k}}}\right)\cdot \delta \mathbf {r} _{k}\,\mathrm {d} t=0.$

Hamilton's principle is still valid even if the coordinates *L* is expressed in are not independent, here **r***k*, but the constraints are still assumed to be holonomic. As always the end points are fixed *δ***r***k*(*t*1) = *δ***r***k*(*t*2) = **0** for all *k*. What cannot be done is to simply equate the coefficients of *δ***r***k* to zero because the *δ***r***k* are not independent. Instead, the method of Lagrange multipliers can be used to include the constraints. Multiplying each constraint equation *f**i*(**r***k*, *t*) = 0 by a Lagrange multiplier *λ**i* for *i* = 1, 2, ..., *C*, and adding the results to the original Lagrangian, gives the new Lagrangian $L'=L(\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,{\dot {\mathbf {r} }}_{1},{\dot {\mathbf {r} }}_{2},\ldots ,t)+\sum _{i=1}^{C}\lambda _{i}(t)f_{i}(\mathbf {r} _{k},t).$

The Lagrange multipliers are arbitrary functions of time *t*, but not functions of the coordinates **r***k*, so the multipliers are on equal footing with the position coordinates. Varying this new Lagrangian and integrating with respect to time gives $\int _{t_{1}}^{t_{2}}\delta L'\mathrm {d} t=\int _{t_{1}}^{t_{2}}\sum _{k=1}^{N}\left({\frac {\partial L}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {\mathbf {r} }}_{k}}}+\sum _{i=1}^{C}\lambda _{i}{\frac {\partial f_{i}}{\partial \mathbf {r} _{k}}}\right)\cdot \delta \mathbf {r} _{k}\,\mathrm {d} t=0.$

The introduced multipliers can be found so that the coefficients of *δ***r***k* are zero, even though the **r***k* are not independent. The equations of motion follow. From the preceding analysis, obtaining the solution to this integral is equivalent to the statement ${\frac {\partial L'}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L'}{\partial {\dot {\mathbf {r} }}_{k}}}=0\quad \Rightarrow \quad {\frac {\partial L}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {\mathbf {r} }}_{k}}}+\sum _{i=1}^{C}\lambda _{i}{\frac {\partial f_{i}}{\partial \mathbf {r} _{k}}}=0,$ which are **Lagrange's equations of the first kind**. Also, the *λ**i* Euler-Lagrange equations for the new Lagrangian return the constraint equations ${\frac {\partial L'}{\partial \lambda _{i}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L'}{\partial {\dot {\lambda }}_{i}}}=0\quad \Rightarrow \quad f_{i}(\mathbf {r} _{k},t)=0.$

For the case of a conservative force given by the gradient of some potential energy *V*, a function of the **r**k coordinates only, substituting the Lagrangian *L* = *T* − *V* gives $\underbrace {{\frac {\partial T}{\partial \mathbf {r} _{k}}}-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial T}{\partial {\dot {\mathbf {r} }}_{k}}}} _{-\mathbf {F} _{k}}+\underbrace {-{\frac {\partial V}{\partial \mathbf {r} _{k}}}} _{\mathbf {N} _{k}}+\sum _{i=1}^{C}\lambda _{i}{\frac {\partial f_{i}}{\partial \mathbf {r} _{k}}}=0,$ and identifying the derivatives of kinetic energy as the (negative of the) resultant force, and the derivatives of the potential equaling the non-constraint force, it follows the constraint forces are $\mathbf {C} _{k}=\sum _{i=1}^{C}\lambda _{i}{\frac {\partial f_{i}}{\partial \mathbf {r} _{k}}},$ thus giving the constraint forces explicitly in terms of the constraint equations and the Lagrange multipliers.

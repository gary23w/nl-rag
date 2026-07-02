---
title: "Two-body problem"
source: https://en.wikipedia.org/wiki/Two-body_problem
domain: celestial-mechanics-physics
license: CC-BY-SA-4.0
tags: celestial mechanics, orbital mechanics, kepler's laws, three-body problem
fetched: 2026-07-02
---

# Two-body problem

Left:

Two bodies of similar

mass

orbiting a common

barycenter

external to both bodies, with

elliptic orbits

. This model is typical of

binary stars

.

Right:

Two bodies with a "slight" difference in mass orbiting a common barycenter. Their sizes and this type of orbit are similar to the

Pluto–Charon system

(in which the barycenter is external to both bodies), as well as the

Earth

–

Moon

system (in which the barycenter is internal to the larger body).

In classical mechanics, the **two-body problem** is used to calculate and predict the motion of two massive bodies that are orbiting each other in space. The problem assumes that the two bodies are perfect spheres that never collide with one another and that all external forces are negligible compared to the force of interaction between the two bodies.

The most prominent example of the classical two-body problem is the gravitational case (see also Kepler problem), arising in astronomy for predicting the orbits (or escapes from orbit) of objects such as satellites, planets, and stars. A two-point-particle model of such a system nearly always describes its behavior well enough to provide useful insights and predictions.

A simpler "one-body" model, the "central-force problem", treats one object as the immobile source of a force acting on the other. One then seeks to predict the motion of the single remaining mobile object. Such an approximation can give useful results when one object is much more massive than the other (as with a light planet orbiting a heavy star, where the star can be treated as essentially stationary).

However, the one-body approximation is usually unnecessary except as a stepping stone. For many forces, including gravitational ones, the general version of the two-body problem can be reduced to a pair of one-body problems, allowing it to be solved completely, and giving a solution simple enough to be used effectively.

By contrast, the three-body problem (and, more generally, the *n*-body problem for *n* > 2) cannot be solved generally, except in special cases.

## Results for prominent cases

### Gravitation and other inverse-square examples

The two-body problem is interesting in astronomy because pairs of astronomical objects are often moving rapidly in arbitrary directions (so their motions become interesting), widely separated from one another (so they will not collide) and even more widely separated from other objects (so outside influences will be small enough to be ignored safely).

Under the force of gravity, each member of a pair of such objects will orbit their mutual center of mass in an elliptical pattern, unless they are moving fast enough to escape one another entirely, in which case their paths will diverge along other planar conic sections. If one object is very much heavier than the other, it will move far less than the other with reference to the shared center of mass. The mutual center of mass may even be inside the larger object.

For the derivation of the solutions to the problem, see Classical central-force problem or Kepler problem.

In principle, the same solutions apply to macroscopic problems involving objects interacting not only through gravity, but also through any conservative force obeying the inverse-square law, with electrostatic attraction being an obvious physical example. In practice, such problems rarely arise. Except perhaps in experimental apparatus or other specialized equipment, we rarely encounter electrostatically interacting objects which are moving fast enough, and in such a direction, as to avoid colliding, and/or which are isolated enough from their surroundings.

The dynamical system of a two-body system under the influence of torque turns out to be a Sturm-Liouville equation.

### Inapplicability to subatomic systems

Although we can describe the repulsion and attraction of particles in the atom using the same laws that apply to the leaves of an electroscope, we need quantum mechanics to predict how the particles will behave under those forces. Most behavior of subatomic systems *cannot* be predicted under the classical assumptions underlying this article or using the mathematics here.

Electrons in an atom are sometimes described as "orbiting" its nucleus, following an early conjecture of Niels Bohr (this is the source of the term "orbital"). However, electrons don't actually orbit nuclei in any meaningful sense, and quantum mechanics are necessary for any useful understanding of the electron's real behavior. Solving the classical two-body problem for an electron orbiting an atomic nucleus is misleading and does not produce many useful insights.

## Reduction to two independent, one-body problems

The complete two-body problem can be solved by re-formulating it as two one-body problems: a trivial one and one that involves solving for the motion of one particle in an external potential. Since many one-body problems can be solved exactly, the corresponding two-body problem can also be solved.

Let **x**1 and **x**2 be the vector positions of the two bodies, and *m*1 and *m*2 be their masses. The goal is to determine the trajectories **x**1(*t*) and **x**2(*t*) for all times *t*, given the initial positions **x**1(*t* = 0) and **x**2(*t* = 0) and the initial velocities **v**1(*t* = 0) and **v**2(*t* = 0).

When applied to the two masses, Newton's second law states that

| $\mathbf {F} _{12}(\mathbf {x} _{1},\mathbf {x} _{2})=m_{1}{\ddot {\mathbf {x} }}_{1}$ |   | Equation 1 |
|---|---|---|

| $\mathbf {F} _{21}(\mathbf {x} _{1},\mathbf {x} _{2})=m_{2}{\ddot {\mathbf {x} }}_{2}$ |   | Equation 2 |
|---|---|---|

where **F**12 is the force on mass 1 due to its interactions with mass 2, and **F**21 is the force on mass 2 due to its interactions with mass 1. The two dots on top of the **x** position vectors denote their second derivative with respect to time, or their acceleration vectors.

Adding and subtracting these two equations decouples them into two one-body problems, which can be solved independently. *Adding* equations (1) and (**2**) results in an equation describing the center of mass (barycenter) motion. By contrast, *subtracting* equation (2) from equation (1) results in an equation that describes how the vector **r** = **x**1 − **x**2 between the masses changes with time. The solutions of these independent one-body problems can be combined to obtain the solutions for the trajectories **x**1(*t*) and **x**2(*t*).

Let $\mathbf {R}$ be the position of the center of mass (barycenter) of the system. Addition of the force equations (1) and (2) yields $m_{1}{\ddot {\mathbf {x} }}_{1}+m_{2}{\ddot {\mathbf {x} }}_{2}=(m_{1}+m_{2}){\ddot {\mathbf {R} }}=\mathbf {F} _{12}+\mathbf {F} _{21}=0$ where we have used Newton's third law **F**12 = −**F**21 and where ${\ddot {\mathbf {R} }}\equiv {\frac {m_{1}{\ddot {\mathbf {x} }}_{1}+m_{2}{\ddot {\mathbf {x} }}_{2}}{m_{1}+m_{2}}}.$

The resulting equation: ${\ddot {\mathbf {R} }}=0$ shows that the velocity $\mathbf {v} ={\frac {dR}{dt}}$ of the center of mass is constant, from which follows that the total momentum *m*1 **v**1 + *m*2 **v**2 is also constant (conservation of momentum). Hence, the position **R**(*t*) of the center of mass can be determined at all times from the initial positions and velocities.

### Displacement vector motion (2nd one-body problem)

Dividing both force equations by the respective masses, subtracting the second equation from the first, and rearranging gives the equation ${\ddot {\mathbf {r} }}={\ddot {\mathbf {x} }}_{1}-{\ddot {\mathbf {x} }}_{2}=\left({\frac {\mathbf {F} _{12}}{m_{1}}}-{\frac {\mathbf {F} _{21}}{m_{2}}}\right)=\left({\frac {1}{m_{1}}}+{\frac {1}{m_{2}}}\right)\mathbf {F} _{12}$ where we have again used Newton's third law **F**12 = −**F**21 and where **r** is the displacement vector from mass 2 to mass 1, as defined above.

The force between the two objects, which originates in the two objects, should only be a function of their separation **r** and not of their absolute positions **x**1 and **x**2; otherwise, there would not be translational symmetry, and the laws of physics would have to change from place to place. The subtracted equation can therefore be written: $\mu {\ddot {\mathbf {r} }}=\mathbf {F} _{12}(\mathbf {x} _{1},\mathbf {x} _{2})=\mathbf {F} (\mathbf {r} )$ where $\mu$ is the reduced mass $\mu ={\frac {1}{{\frac {1}{m_{1}}}+{\frac {1}{m_{2}}}}}={\frac {m_{1}m_{2}}{m_{1}+m_{2}}}.$

Solving the equation for **r**(*t*) is the key to the two-body problem. The solution depends on the specific force between the bodies, which is defined by $\mathbf {F} (\mathbf {r} )$ . For the case where $\mathbf {F} (\mathbf {r} )$ follows an inverse-square law, see the Kepler problem.

Once **R**(*t*) and **r**(*t*) have been determined, the original trajectories may be obtained $\mathbf {x} _{1}(t)=\mathbf {R} (t)+{\frac {m_{2}}{m_{1}+m_{2}}}\mathbf {r} (t)$ $\mathbf {x} _{2}(t)=\mathbf {R} (t)-{\frac {m_{1}}{m_{1}+m_{2}}}\mathbf {r} (t)$ as may be verified by substituting the definitions of **R** and **r** into the right-hand sides of these two equations.

## Two-body motion is planar

The motion of two bodies with respect to each other always lies in a plane (in the center of mass frame).

Proof: Defining the linear momentum **p** and the angular momentum **L** of the system, with respect to the center of mass, by the equations $\mathbf {L} =\mathbf {r} \times \mathbf {p} =\mathbf {r} \times \mu {\frac {d\mathbf {r} }{dt}},$

where μ is the reduced mass and **r** is the relative position **r**2 − **r**1 (with these written taking the center of mass as the origin, and thus both parallel to **r**) the rate of change of the angular momentum **L** equals the net torque **N** $\mathbf {N} ={\frac {d\mathbf {L} }{dt}}={\dot {\mathbf {r} }}\times \mu {\dot {\mathbf {r} }}+\mathbf {r} \times \mu {\ddot {\mathbf {r} }}\ ,$ and using the property of the vector cross product that **v** × **w** = **0** for any vectors **v** and **w** pointing in the same direction,

$\mathbf {N} \ =\ {\frac {d\mathbf {L} }{dt}}=\mathbf {r} \times \mathbf {F} \ ,$ with **F** = *μ* *d*2**r**/*dt*2.

Introducing the assumption (true of most physical forces, as they obey Newton's strong third law of motion) that the force between two particles acts along the line between their positions, it follows that **r** × **F** = **0** and the angular momentum vector **L** is constant (conserved). Therefore, the displacement vector **r** and its velocity **v** are always in the plane perpendicular to the constant vector **L**.

## Energy of the two-body system

If the force **F**(**r**) is conservative then the system has a potential energy *U*(**r**), so the total energy can be written as $E_{\text{tot}}={\frac {1}{2}}m_{1}{\dot {\mathbf {x} }}_{1}^{2}+{\frac {1}{2}}m_{2}{\dot {\mathbf {x} }}_{2}^{2}+U(\mathbf {r} )={\frac {1}{2}}(m_{1}+m_{2}){\dot {\mathbf {R} }}^{2}+{1 \over 2}\mu {\dot {\mathbf {r} }}^{2}+U(\mathbf {r} )$

In the center of mass frame the kinetic energy is the lowest and the total energy becomes $E={\frac {1}{2}}\mu {\dot {\mathbf {r} }}^{2}+U(\mathbf {r} )$ The coordinates **x**1 and **x**2 can be expressed as $\mathbf {x} _{1}={\frac {\mu }{m_{1}}}\mathbf {r}$ $\mathbf {x} _{2}=-{\frac {\mu }{m_{2}}}\mathbf {r}$ and in a similar way the energy *E* is related to the energies *E*1 and *E*2 that separately contain the kinetic energy of each body: ${\begin{aligned}E_{1}&={\frac {\mu }{m_{1}}}E={\frac {1}{2}}m_{1}{\dot {\mathbf {x} }}_{1}^{2}+{\frac {\mu }{m_{1}}}U(\mathbf {r} )\\[4pt]E_{2}&={\frac {\mu }{m_{2}}}E={\frac {1}{2}}m_{2}{\dot {\mathbf {x} }}_{2}^{2}+{\frac {\mu }{m_{2}}}U(\mathbf {r} )\\[4pt]E_{\text{tot}}&=E_{1}+E_{2}\end{aligned}}$

## Central forces

For many physical problems, the force **F**(**r**) is a central force, i.e., it is of the form $\mathbf {F} (\mathbf {r} )=F(r){\hat {\mathbf {r} }}$ where *r* = |**r**| and **r̂** = **r**/*r* is the corresponding unit vector. We now have: $\mu {\ddot {\mathbf {r} }}={F}(r){\hat {\mathbf {r} }}\ ,$ where *F*(*r*) is negative in the case of an attractive force.

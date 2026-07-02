---
title: "Hamilton's principle"
source: https://en.wikipedia.org/wiki/Hamilton%27s_principle
domain: calculus-of-variations-deep
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, beltrami identity, hamilton principle
fetched: 2026-07-02
---

# Hamilton's principle

In physics, **Hamilton's principle** is William Rowan Hamilton's formulation of the principle of stationary action. It states that the dynamics of a physical system are determined by a variational problem for a functional based on a single function, the Lagrangian, which may contain all physical information concerning the system and the forces acting on it. The variational problem is equivalent to and allows for the derivation of the *differential* equations of motion of the physical system. Although formulated originally for classical mechanics, Hamilton's principle also applies to classical fields such as the electromagnetic and gravitational fields, and plays an important role in quantum mechanics, quantum field theory and criticality theories.

## Mathematical formulation

Hamilton's principle states that the true evolution **q**(*t*) of a system described by N generalized coordinates **q** = (*q*1, *q*2, ..., *q**N*) between two specified states **q**1 = **q**(*t*1) and **q**2 = **q**(*t*2) at two specified times *t*1 and *t*2 is a stationary point (a point where the variation is zero) of the action functional ${\mathcal {S}}[\mathbf {q} ]\ {\stackrel {\mathrm {def} }{=}}\ \int _{t_{1}}^{t_{2}}L(\mathbf {q} (t),{\dot {\mathbf {q} }}(t),t)\,dt$ where $L(\mathbf {q} ,{\dot {\mathbf {q} }},t)$ is the Lagrangian function for the system. In other words, any *first-order* perturbation of the true evolution results in (at most) *second-order* changes in ${\mathcal {S}}$ . The action ${\mathcal {S}}$ is a functional, i.e., something that takes as its input a function and returns a single number, a scalar. In terms of functional analysis, Hamilton's principle states that the true evolution of a physical system is a solution of the functional equation

Hamilton's principle

${\frac {\delta {\mathcal {S}}}{\delta \mathbf {q} (t)}}=0.$

That is, the system takes a path in configuration space for which the action is stationary, with fixed boundary conditions at the beginning and the end of the path.

### Derivation from Newton's laws of motion

Although Hamilton's principle can be viewed as a postulate effectively replacing Newton's laws of motion, it can also be derived from Newton's laws. Starting with d'Alembert's principle:

$\sum _{i}(\mathbf {F} _{i}-m_{i}\mathbf {a} _{i})\cdot \delta \mathbf {r} _{i}=0.$

Where i is the index of a mass, $\mathbf {F} _{i}$ is applied force (excluding constraint forces), ${\textbf {a}}_{i}$ is acceleration of the mass, and $\delta \mathbf {r} _{i}$ is the virtual displacement of the i -th mass consistent with the constraints. The above equation holds true for all times t so a definite integral with respect to t must also be 0:

$\int _{t_{1}}^{t_{2}}\sum _{i}(\mathbf {F} _{i}-m_{i}{\ddot {\mathbf {r} }}_{i})\cdot \delta \mathbf {r} _{i}dt=0.$

$\delta \mathbf {r} _{i}$ , the sum, and the integral can all be distributed:

$\int _{t_{1}}^{t_{2}}\sum _{i}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}dt-\int _{t_{1}}^{t_{2}}\sum _{i}m_{i}{\ddot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i}dt=0$

Looking at the second term we can use the product rule to find the relation:

${\frac {d}{dt}}(m_{i}{\dot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i})=m_{i}{\ddot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i}+m_{i}{\dot {\mathbf {r} }}_{i}\cdot {\frac {d}{dt}}(\delta \mathbf {r} _{i})$

Variation $\delta$ and the time derivative ${\frac {d}{dt}}$ commute (meaning ${\frac {d}{dt}}\delta \mathbf {r} =\delta {\dot {\mathbf {r} }}$ ), so we can rearrange this to isolate our acceleration term:

$m_{i}{\ddot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i}={\frac {d}{dt}}(m_{i}{\dot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i})-m_{i}{\dot {\mathbf {r} }}_{i}\cdot \delta {\dot {\mathbf {r} }}_{i}$

Substituting this into the integral we get:

$\int _{t_{1}}^{t_{2}}\sum _{i}m_{i}{\ddot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i}\,dt=\sum _{i}\left[m_{i}{\dot {\mathbf {r} }}_{i}\cdot \delta \mathbf {r} _{i}\right]_{t_{1}}^{t_{2}}-\int _{t_{1}}^{t_{2}}\sum _{i}m_{i}{\dot {\mathbf {r} }}_{i}\cdot \delta {\dot {\mathbf {r} }}_{i}\,dt$

In Hamilton's principle, we define the variations such that they vanish at the endpoints: $\delta \mathbf {r} _{i}(t_{1})=\delta \mathbf {r} _{i}(t_{2})=0$ . This makes the first term on the right disappear completely. Also $\delta ({\dot {\mathbf {r} }}^{2})=2{\dot {\mathbf {r} }}\cdot \delta {\dot {\mathbf {r} }}$ so the remaining term is:

$-\int _{t_{1}}^{t_{2}}\delta \left(\sum _{i}{\frac {1}{2}}m_{i}{\dot {\mathbf {r} }}_{i}^{2}\right)dt=-\int _{t_{1}}^{t_{2}}\delta T\,dt$

Where T is the total kinetic energy. Looking at the applied force term, if the forces are conservative, they can be derived from a potential energy $V(\mathbf {r} _{1},\mathbf {r} _{2},\dots )$ . The work done by these forces during a virtual displacement is:

$\sum _{i}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}=-\sum _{i}\nabla _{i}V\cdot \delta \mathbf {r} _{i}=-\delta V$

Substituting everything back into the integral gives:

$\int _{t_{1}}^{t_{2}}(-\delta V-(-\delta T))\,dt=0$ $\delta \int _{t_{1}}^{t_{2}}(T-V)\,dt=0$

Here the Lagrangian $L=T-V$ . This is Hamilton's principle for a non-relativistic system of masses in the absence of an electromagnetic field.

### Euler–Lagrange equations derived from the action integral

Requiring that the true trajectory **q**(*t*) be a stationary point of the action functional ${\mathcal {S}}$ is equivalent to a set of differential equations for **q**(*t*) (the **Euler–Lagrange equations**), which may be derived as follows.

Let **q**(*t*) represent the true evolution of the system between two specified states **q**1 = **q**(*t*1) and **q**2 = **q**(*t*2) at two specified times *t*1 and *t*2, and let **ε**(*t*) be a small perturbation that is zero at the endpoints of the trajectory ${\boldsymbol {\varepsilon }}(t_{1})={\boldsymbol {\varepsilon }}(t_{2})\ {\stackrel {\mathrm {def} }{=}}\ 0$

To first order in the perturbation **ε**(*t*), the change in the action functional $\delta {\mathcal {S}}$ would be ${\begin{aligned}\delta {\mathcal {S}}&=\int _{t_{1}}^{t_{2}}\;\left[L(\mathbf {q} +{\boldsymbol {\varepsilon }},{\dot {\mathbf {q} }}+{\dot {\boldsymbol {\varepsilon }}})-L(\mathbf {q} ,{\dot {\mathbf {q} }})\right]dt\\&=\int _{t_{1}}^{t_{2}}\;\left({\boldsymbol {\varepsilon }}\cdot {\frac {\partial L}{\partial \mathbf {q} }}+{\dot {\boldsymbol {\varepsilon }}}\cdot {\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right)\,dt\end{aligned}}$ where we have expanded the Lagrangian *L* to first order in the perturbation **ε**(*t*).

Applying integration by parts to the last term results in $\delta {\mathcal {S}}=\left[{\boldsymbol {\varepsilon }}\cdot {\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right]_{t_{1}}^{t_{2}}+\int _{t_{1}}^{t_{2}}\;\left({\boldsymbol {\varepsilon }}\cdot {\frac {\partial L}{\partial \mathbf {q} }}-{\boldsymbol {\varepsilon }}\cdot {\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right)\,dt$

The boundary conditions ${\boldsymbol {\varepsilon }}(t_{1})={\boldsymbol {\varepsilon }}(t_{2})\ {\stackrel {\mathrm {def} }{=}}\ 0$ causes the first term to vanish $\delta {\mathcal {S}}=\int _{t_{1}}^{t_{2}}\;{\boldsymbol {\varepsilon }}\cdot \left({\frac {\partial L}{\partial \mathbf {q} }}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}\right)\,dt$

Hamilton's principle requires that this first-order change $\delta {\mathcal {S}}$ is zero for all possible perturbations **ε**(*t*), i.e., the true path is a stationary point of the action functional ${\mathcal {S}}$ (either a minimum, maximum or saddle point). This requirement can be satisfied if and only if

Euler–Lagrange equations

${\frac {\partial L}{\partial \mathbf {q} }}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}=0$

These equations are called the Euler–Lagrange equations for the variational problem.

### Example: Free particle in polar coordinates

Trivial examples help to appreciate the use of the action principle via the Euler–Lagrange equations. A free particle (mass *m* and velocity *v*) in Euclidean space moves in a straight line. Using the Euler–Lagrange equations, this can be shown in polar coordinates as follows. In the absence of a potential, the Lagrangian is simply equal to the kinetic energy $L={\frac {1}{2}}mv^{2}={\frac {1}{2}}m\left({\dot {x}}^{2}+{\dot {y}}^{2}\right)$ in orthonormal (*x*,*y*) coordinates, where the dot represents differentiation with respect to the curve parameter (usually the time, *t*). Therefore, upon application of the Euler–Lagrange equations, ${\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {x}}}}\right)-{\frac {\partial L}{\partial x}}=0\qquad \Rightarrow \qquad m{\ddot {x}}=0$

And likewise for *y*. Thus the Euler–Lagrange formulation can be used to derive Newton's laws.

In polar coordinates (*r*, *φ*) the kinetic energy and hence the Lagrangian becomes $L={\frac {1}{2}}m\left({\dot {r}}^{2}+r^{2}{\dot {\varphi }}^{2}\right).$

The radial r and φ components of the Euler–Lagrange equations become, respectively ${\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {r}}}}\right)-{\frac {\partial L}{\partial r}}=0\qquad \Rightarrow \qquad {\ddot {r}}-r{\dot {\varphi }}^{2}=0$ ${\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {\varphi }}}}\right)-{\frac {\partial L}{\partial \varphi }}=0\qquad \Rightarrow \qquad {\ddot {\varphi }}+{\frac {2}{r}}{\dot {r}}{\dot {\varphi }}=0.$

remembering that r is also dependent on time and the product rule is needed to compute the total time derivative ${\textstyle {\frac {d}{dt}}mr^{2}{\dot {\varphi }}}$ .

The solution of these two equations is given by $r={\sqrt {(at+b)^{2}+c^{2}}}$ $\varphi =\tan ^{-1}\left({\frac {at+b}{c}}\right)+d$ for a set of constants *a*, *b*, *c*, *d* determined by initial conditions. Thus, indeed, *the solution is a straight line* given in polar coordinates: *a* is the velocity, *c* is the distance of the closest approach to the origin, and *d* is the angle of motion.

## Applied to deformable bodies

Hamilton's principle is an important variational principle in elastodynamics. As opposed to a system composed of rigid bodies, deformable bodies have an infinite number of degrees of freedom and occupy continuous regions of space; consequently, the state of the system is described by using continuous functions of space and time. The extended Hamilton Principle for such bodies is given by $\int _{t_{1}}^{t_{2}}\left[\delta W_{e}+\delta T-\delta U\right]dt=0$ where T is the kinetic energy, U is the elastic energy, *W*e is the work done by external loads on the body, and *t*1, *t*2 the initial and final times. If the system is conservative, the work done by external forces may be derived from a scalar potential V. In this case, $\delta \int _{t_{1}}^{t_{2}}\left[T-(U+V)\right]dt=0.$ This is called Hamilton's principle and it is invariant under coordinate transformations.

## Comparison with Maupertuis' principle

Hamilton's principle and Maupertuis' principle are occasionally confused and both have been called the principle of least action. They differ in three important ways:

- *their definition of the action...* Maupertuis' principle uses an integral over the generalized coordinates known as the **abbreviated action** or reduced action ${\mathcal {S}}_{0}\ {\stackrel {\mathrm {def} }{=}}\ \int \mathbf {p} \cdot d\mathbf {q}$ where **p** = (*p*1, *p*2, ..., *pN*) are the conjugate momenta defined above. By contrast, Hamilton's principle uses ${\mathcal {S}}$ , the integral of the Lagrangian over time.
- *the solution that they determine...* Hamilton's principle determines the trajectory **q**(*t*) as a function of time, whereas Maupertuis' principle determines only the shape of the trajectory in the generalized coordinates. For example, Maupertuis' principle determines the shape of the ellipse on which a particle moves under the influence of an inverse-square central force such as gravity, but does not describe *per se* how the particle moves along that trajectory. (However, this time parameterization may be determined from the trajectory itself in subsequent calculations using the conservation of energy). By contrast, Hamilton's principle directly specifies the motion along the ellipse as a function of time.
- *...and the constraints on the variation.* Maupertuis' principle requires that the two endpoint states *q*1 and *q*2 be given and that energy be conserved along every trajectory (same energy for each trajectory). This forces the endpoint times to be varied as well. By contrast, Hamilton's principle does not require the conservation of energy, but does require that the endpoint times *t*1 and *t*2 be specified as well as the endpoint states *q*1 and *q*2.

## Action principle for fields

### Classical field theory

The **action principle** can be extended to obtain the equations of motion for fields, such as the electromagnetic field or gravity.

The Einstein equation utilizes the *Einstein–Hilbert action* as constrained by a variational principle.

The path of a body in a gravitational field (i.e. free fall in space time, a so-called geodesic) can be found using the action principle.

### Quantum mechanics and quantum field theory

In quantum mechanics, the system does not follow a single path whose action is stationary, but the behavior of the system depends on all imaginable paths and the value of their action. The action corresponding to the various paths is used to calculate the path integral, that gives the probability amplitudes of the various outcomes.

Although equivalent in classical mechanics with Newton's laws, the action principle is better suited for generalizations and plays an important role in modern physics. Indeed, this principle is one of the great generalizations in physical science. In particular, it is fully appreciated and best understood within quantum mechanics. Richard Feynman's path integral formulation of quantum mechanics is based on a stationary-action principle, using path integrals. Maxwell's equations can be derived as conditions of stationary action.

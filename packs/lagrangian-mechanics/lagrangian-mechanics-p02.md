---
title: "Lagrangian mechanics (part 2/2)"
source: https://en.wikipedia.org/wiki/Lagrangian_mechanics
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
part: 2/2
---

## Properties of the Lagrangian

### Non-uniqueness

The Lagrangian of a given system is not unique. A Lagrangian *L* can be multiplied by a nonzero constant *a* and shifted by an arbitrary constant *b*, and the new Lagrangian *L*′ = *aL* + *b* will describe the same motion as *L*. If one restricts as above to trajectories **q** over a given time interval [*t*st, *t*fin] and fixed end points *P*st = **q**(*t*st) and *P*fin = **q**(*t*fin), then two Lagrangians describing the same system can differ by the "total time derivative" of a function *f*(**q**, *t*): $L'(\mathbf {q} ,{\dot {\mathbf {q} }},t)=L(\mathbf {q} ,{\dot {\mathbf {q} }},t)+{\frac {\mathrm {d} f(\mathbf {q} ,t)}{\mathrm {d} t}},$ where ${\textstyle {\frac {\mathrm {d} f(\mathbf {q} ,t)}{\mathrm {d} t}}}$ means ${\textstyle {\frac {\partial f(\mathbf {q} ,t)}{\partial t}}+\sum _{i}{\frac {\partial f(\mathbf {q} ,t)}{\partial q_{i}}}{\dot {q}}_{i}.}$

Both Lagrangians *L* and *L*′ produce the same equations of motion since the corresponding actions *S* and *S*′ are related via ${\begin{aligned}S'[\mathbf {q} ]&=\int _{t_{\text{st}}}^{t_{\text{fin}}}L'(\mathbf {q} (t),{\dot {\mathbf {q} }}(t),t)\,dt\\&=\int _{t_{\text{st}}}^{t_{\text{fin}}}L(\mathbf {q} (t),{\dot {\mathbf {q} }}(t),t)\,dt+\int _{t_{\text{st}}}^{t_{\text{fin}}}{\frac {\mathrm {d} f(\mathbf {q} (t),t)}{\mathrm {d} t}}\,dt\\&=S[\mathbf {q} ]+f(P_{\text{fin}},t_{\text{fin}})-f(P_{\text{st}},t_{\text{st}}),\end{aligned}}$ with the last two components *f*(*P*fin, *t*fin) and *f*(*P*st, *t*st) independent of **q**.

### Invariance under point transformations

Given a set of generalized coordinates **q**, if we change these variables to a new set of generalized coordinates **Q** according to a point transformation **Q** = **Q**(**q**, *t*) which is invertible as **q** = **q**(**Q**, *t*), the new Lagrangian *L*′ is a function of the new coordinates and similarly for the constraints ${\begin{aligned}L'(\mathbf {Q} ,{\dot {\mathbf {Q} }},t)&=L(\mathbf {q} (\mathbf {Q} ,t),{\dot {\mathbf {q} }}(\mathbf {Q} ,{\dot {\mathbf {Q} }},t),t),\\\phi _{j}'(\mathbf {Q} ,t)&=\phi _{j}(\mathbf {q} (\mathbf {Q} ,t),t)\end{aligned}}$ and by the chain rule for partial differentiation, Lagrange's equations are invariant under this transformation;

${\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L'}{\partial {\dot {Q}}_{i}}}={\frac {\partial L'}{\partial Q_{i}}}+\sum _{j}\lambda _{j}{\frac {\partial \phi '_{j}}{\partial Q_{i}}}.$

Proof

For a coordinate transformation $Q_{i}=Q_{i}(\mathbf {q} ,t)$ , we have $d{Q_{i}}=\sum _{k}{\frac {\partial Q_{i}}{\partial q_{k}}}d{q_{k}}+{\frac {\partial Q_{k}}{\partial t}}dt,$ which implies that ${\dot {Q_{i}}}=\sum _{k}{\frac {\partial Q_{i}}{\partial q_{k}}}(\mathbf {q} ,t)\,{\dot {q}}_{k}+{\frac {\partial Q_{k}}{\partial t}}(\mathbf {q} ,t)$ which implies that ${\frac {\partial {\dot {Q_{i}}}}{\partial {\dot {q}}_{k}}}={\frac {\partial Q_{i}}{\partial q_{k}}}$ .

It also follows that: ${\frac {\partial {\dot {Q_{i}}}}{\partial q_{j}}}=\sum _{k}{\frac {\partial ^{2}Q_{i}}{\partial q_{j}\partial q_{k}}}(\mathbf {q} ,t)\,{\dot {q}}_{k}+{\frac {\partial ^{2}Q_{k}}{\partial q_{j}\partial t}}(\mathbf {q} ,t)$ and similarly: ${\frac {d}{dt}}\left({\frac {\partial {Q_{i}}}{\partial q_{j}}}\right)=\sum _{k}{\frac {\partial ^{2}Q_{i}}{\partial q_{k}\partial q_{j}}}(\mathbf {q} ,t)\,{\dot {q}}_{k}+{\frac {\partial ^{2}Q_{k}}{\partial t\partial q_{j}}}(\mathbf {q} ,t)$ which imply that ${\frac {d}{dt}}\left({\frac {\partial Q_{i}}{\partial q_{k}}}\right)={\frac {\partial {\dot {Q}}_{i}}{\partial q_{k}}}$ . The two derived relations can be employed in the proof.

Starting from Euler Lagrange equations in initial set of generalized coordinates, we have: ${\begin{aligned}{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}_{i}}}-{\frac {{\partial }L}{\partial q_{i}}}-\sum _{j}\lambda _{j}{\frac {\partial \phi _{j}}{\partial q_{i}}}=0\\\sum _{k}\left({\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {Q}}_{k}}}{\frac {\partial {\dot {Q}}_{k}}{\partial {\dot {q}}_{i}}}\right)-{\frac {{\partial }L}{\partial Q_{k}}}{\frac {\partial Q_{k}}{\partial {q}_{i}}}-{\frac {{\partial }L}{\partial {\dot {Q}}_{k}}}{\frac {\partial {\dot {Q}}_{k}}{\partial {q}_{i}}}-\sum _{j}\lambda _{j}{\frac {\partial \phi _{j}}{\partial Q_{k}}}{\frac {\partial Q_{k}}{\partial q_{i}}}\right)=0\\\sum _{k}\left({\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {Q}}_{k}}}\right){\frac {\partial {\dot {Q}}_{k}}{\partial {\dot {q}}_{i}}}+{\frac {\partial L}{\partial {\dot {Q}}_{k}}}{\frac {d}{dt}}\left({\frac {\partial {\dot {Q}}_{k}}{\partial {\dot {q}}_{i}}}\right)-{\frac {{\partial }L}{\partial Q_{k}}}{\frac {\partial {\dot {Q}}_{k}}{\partial {\dot {q}}_{i}}}-{\frac {{\partial }L}{\partial {\dot {Q}}_{k}}}{\frac {d}{dt}}\left({\frac {\partial Q_{k}}{\partial q_{i}}}\right)-\sum _{j}\lambda _{j}{\frac {\partial \phi _{j}}{\partial Q_{k}}}{\frac {\partial Q_{k}}{\partial q_{i}}}\right)=0\\\sum _{k}\left({\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {Q}}_{k}}}\right)-{\frac {\partial L}{\partial Q_{k}}}-\sum _{j}\lambda _{j}{\frac {\partial \phi _{j}}{\partial Q_{k}}}\right){\frac {\partial Q_{k}}{\partial q_{i}}}=0\\\end{aligned}}$

Since the transformation from $q\rightarrow Q$ is invertible, it follows that the form of the Euler-Lagrange equation is invariant i.e., ${\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {Q}}_{i}}}-{\frac {{\partial }L}{\partial Q_{i}}}-\sum _{j}\lambda _{j}{\frac {\partial \phi _{j}}{\partial Q_{i}}}=0.$

### Cyclic coordinates and conserved momenta

An important property of the Lagrangian is that conserved quantities can easily be read off from it. The *generalized momentum* "canonically conjugate to" the coordinate *qi* is defined by $p_{i}={\frac {\partial L}{\partial {\dot {q}}_{i}}}.$

If the Lagrangian *L* does *not* depend on some coordinate *qi*, it follows immediately from the Euler–Lagrange equations that ${\dot {p}}_{i}={\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}_{i}}}={\frac {\partial L}{\partial q_{i}}}=0$ and integrating shows the corresponding generalized momentum equals a constant, a conserved quantity. This is a special case of Noether's theorem. Such coordinates are called "cyclic" or "ignorable".

For example, a system may have a Lagrangian $L(r,\theta ,{\dot {s}},{\dot {z}},{\dot {r}},{\dot {\theta }},{\dot {\phi }},t),$ where *r* and *z* are lengths along straight lines, *s* is an arc length along some curve, and *θ* and *φ* are angles. Notice *z*, *s*, and *φ* are all absent in the Lagrangian even though their velocities are not. Then the momenta $p_{z}={\frac {\partial L}{\partial {\dot {z}}}},\quad p_{s}={\frac {\partial L}{\partial {\dot {s}}}},\quad p_{\phi }={\frac {\partial L}{\partial {\dot {\phi }}}},$ are all conserved quantities. The units and nature of each generalized momentum will depend on the corresponding coordinate; in this case *p**z* is a translational momentum in the *z* direction, *p**s* is also a translational momentum along the curve *s* is measured, and *p**φ* is an angular momentum in the plane the angle *φ* is measured in. However complicated the motion of the system is, all the coordinates and velocities will vary in such a way that these momenta are conserved.

### Energy

Given a Lagrangian $L,$ the Hamiltonian of the corresponding mechanical system is, by definition, $H={\biggl (}\sum _{i=1}^{n}{\dot {q}}_{i}{\frac {\partial L}{\partial {\dot {q}}_{i}}}{\biggr )}-L.$ This quantity will be equivalent to energy if the generalized coordinates are natural coordinates, i.e., they have no explicit time dependence when expressing position vector: $\mathbf {r} =\mathbf {r} (q_{1},\cdots ,q_{n})$ . From: $T={\frac {m}{2}}v^{2}={\frac {m}{2}}\sum _{i,j}\left({\frac {\partial {\vec {r}}}{\partial q_{i}}}{\dot {q}}_{i}\right)\cdot \left({\frac {\partial {\vec {r}}}{\partial q_{j}}}{\dot {q}}_{j}\right)={\frac {m}{2}}\sum _{i,j}a_{ij}{\dot {q}}_{i}{\dot {q}}_{j}$ $\sum _{k=1}^{n}{\dot {q}}_{k}{\frac {\partial L}{\partial {\dot {q}}_{k}}}=\sum _{k=1}^{n}{\dot {q}}_{k}{\frac {\partial T}{\partial {\dot {q}}_{k}}}={\frac {m}{2}}\left(2\sum _{i,j}a_{ij}{\dot {q}}_{i}{\dot {q}}_{j}\right)=2T$ $H=\left(\sum _{i=1}^{n}{\dot {q}}_{i}{\frac {\partial L}{\partial {\dot {q}}_{i}}}\right)-L=2T-(T-V)=T+V=E$ where $a_{ij}={\frac {\partial \mathbf {r} }{\partial q_{i}}}\cdot {\frac {\partial \mathbf {r} }{\partial q_{j}}}$ is a symmetric matrix that is defined for the derivation.

#### Invariance under coordinate transformations

At every time instant *t*, the energy is invariant under configuration space coordinate changes **q** → **Q**, i.e. (using natural coordinates) $E(\mathbf {q} ,{\dot {\mathbf {q} }},t)=E(\mathbf {Q} ,{\dot {\mathbf {Q} }},t).$ Besides this result, the proof below shows that, under such change of coordinates, the derivatives $\partial L/\partial {\dot {q}}_{i}$ change as coefficients of a linear form.

Proof

For a coordinate transformation **Q** = *F*(**q**), we have $d\mathbf {Q} =F_{*}(\mathbf {q} )d\mathbf {q} ,$ where $F_{*}(\mathbf {q} )$ is the tangent map of the vector space $\left\{\sum _{i=1}^{n}{\dot {q}}_{i}\cdot \left(\left.{\frac {\partial }{\partial q_{i}}}\right|_{\mathbf {q} }\right)\ {\biggl |}\ {\dot {q}}_{i}\in \mathbb {R} \right\}$ to the vector space $\left\{\sum _{i=1}^{n}{\dot {Q}}_{i}\cdot \left(\left.{\frac {\partial }{\partial Q_{i}}}\right|_{F(\mathbf {q} )}\right)\ {\biggl |}\ {\dot {Q}}_{i}\in \mathbb {R} \right\},$ and $\textstyle F_{*}(\mathbf {q} )=\left(\left.{\frac {\partial F_{i}}{\partial q_{j}}}\right|_{\mathbf {q} }\right)_{i,j=1}^{n}$ is the Jacobian. In the coordinates ${\dot {q}}_{i}$ and ${\dot {Q}}_{i},$ the previous formula for $d\mathbf {Q}$ has the form ${\dot {\mathbf {Q} }}=F_{*}(\mathbf {q} ){\dot {\mathbf {q} }}.$ After differentiation involving the product rule, $d{\dot {\mathbf {Q} }}=G(\mathbf {q} ,{\dot {\mathbf {q} }})d\mathbf {q} +F_{*}(\mathbf {q} )d{\dot {\mathbf {q} }},$ where ${\begin{aligned}G(\mathbf {q} ,{\dot {\mathbf {q} }})d\mathbf {q} &\,{\stackrel {\text{def}}{=}}\,d(F_{*}(\mathbf {q} )){\dot {\mathbf {q} }}=\left(\sum _{k=1}^{n}{\frac {\partial ^{2}F_{i}}{\partial q_{j}\partial q_{k}}}{\biggl |}_{\mathbf {q} }dq_{k}\right)_{i,j=1}^{n}{\dot {\mathbf {q} }}=\left(\sum _{j=1}^{n}{\dot {q}}_{j}\sum _{k=1}^{n}{\frac {\partial ^{2}F_{i}}{\partial q_{j}\partial q_{k}}}{\biggl |}_{\mathbf {q} }dq_{k}\right)_{i=1,\ldots ,n}^{T}\\&=\left(\sum _{k=1}^{n}dq_{k}\sum _{j=1}^{n}{\frac {\partial ^{2}F_{i}}{\partial q_{j}\partial q_{k}}}{\biggl |}_{\mathbf {q} }{\dot {q}}_{j}\right)_{i=1,\ldots ,n}^{T}=\left(\sum _{j=1}^{n}{\frac {\partial ^{2}F_{i}}{\partial q_{j}\partial q_{k}}}{\biggl |}_{\mathbf {q} }{\dot {q}}_{j}\right)_{i,k=1}^{n}d\mathbf {q} .\end{aligned}}$

In vector notation, ${\begin{aligned}dL(\mathbf {Q} ,{\dot {\mathbf {Q} }},t)&={\frac {\partial L}{\partial \mathbf {Q} }}d\mathbf {Q} +{\frac {\partial L}{\partial {\dot {\mathbf {Q} }}}}d{\dot {\mathbf {Q} }}+{\frac {\partial L}{\partial t}}dt\\&=\left({\frac {\partial L}{\partial \mathbf {Q} }}F_{*}(\mathbf {q} )+{\frac {\partial L}{\partial {\dot {\mathbf {Q} }}}}G(\mathbf {q} ,{\dot {\mathbf {q} }})\right)d\mathbf {q} +{\frac {\partial L}{\partial {\dot {\mathbf {Q} }}}}F_{*}(\mathbf {q} )d{\dot {\mathbf {q} }}+{\frac {\partial L}{\partial t}}.\end{aligned}}$

On the other hand, $dL(\mathbf {q} ,{\dot {\mathbf {q} }},t)={\frac {\partial L}{\partial \mathbf {q} }}d\mathbf {q} +{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}d{\dot {\mathbf {q} }}+{\frac {\partial L}{\partial t}}dt.$

It was mentioned earlier that Lagrangians do not depend on the choice of configuration space coordinates, i.e. $L(\mathbf {Q} ,{\dot {\mathbf {Q} }},t)=L(\mathbf {q} ,{\dot {\mathbf {q} }},t).$ One implication of this is that $dL(\mathbf {Q} ,{\dot {\mathbf {Q} }},t)=dL(\mathbf {q} ,{\dot {\mathbf {q} }},t),$ and ${\frac {\partial L}{\partial {\dot {\mathbf {Q} }}}}F_{*}(\mathbf {q} )={\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}.$ This demonstrates that, for each $\mathbf {q} ,$ ${\dot {\mathbf {q} }},$ and $t,$ $\textstyle \sum \limits _{i=1}^{n}{\frac {\partial L}{\partial {\dot {q}}_{i}}}d{\dot {q}}_{i}$ is a well-defined linear form whose coefficients $\textstyle {\frac {\partial L}{\partial {\dot {q}}_{i}}}$ are contravariant 1-tensors. Applying both sides of the equation to ${\dot {\mathbf {q} }}$ and using the above formula for ${\dot {\mathbf {Q} }}$ yields ${\dot {\mathbf {Q} }}{\frac {\partial L}{\partial {\dot {\mathbf {Q} }}}}={\dot {\mathbf {q} }}{\frac {\partial L}{\partial {\dot {\mathbf {q} }}}}.$ The invariance of the energy E follows.

#### Conservation

In Lagrangian mechanics, the system is closed if and only if its Lagrangian L does not explicitly depend on time. The energy conservation law states that the energy E of a closed system is an integral of motion.

More precisely, let **q** = **q**(*t*) be an *extremal*. (In other words, **q** satisfies the Euler–Lagrange equations). Taking the total time-derivative of *L* along this extremal and using the EL equations leads to ${\begin{aligned}{\frac {dL}{dt}}&={\dot {\mathbf {q} }}{\frac {\partial L}{\partial \mathbf {q} }}+{\ddot {\mathbf {q} }}{\frac {\partial L}{\partial \mathbf {\dot {q}} }}+{\frac {\partial L}{\partial t}}\\-{\frac {\partial L}{\partial t}}&={\frac {d}{dt}}\left({\frac {\partial L}{\partial \mathbf {\dot {q}} }}\right){\dot {\mathbf {q} }}+{\ddot {\mathbf {q} }}{\frac {\partial L}{\partial \mathbf {\dot {q}} }}-{\dot {L}}\\-{\frac {\partial L}{\partial t}}&={\frac {d}{dt}}\left({\frac {\partial L}{\partial \mathbf {\dot {q}} }}\mathbf {\dot {q}} -L\right)={\frac {dH}{dt}}\end{aligned}}$

If the Lagrangian *L* does not explicitly depend on time, then ∂*L*/∂*t* = 0, then *H* does not vary with time evolution of particle, indeed, an integral of motion, meaning that $H(\mathbf {q} (t),{\dot {\mathbf {q} }}(t),t)={\text{constant of time}}.$ Hence, if the chosen coordinates were natural coordinates, the energy is conserved.

#### Kinetic and potential energies

Under all these circumstances, the constant $E=T+V$ is the total energy of the system. The kinetic and potential energies still change as the system evolves, but the motion of the system will be such that their sum, the total energy, is constant. This is a valuable simplification, since the energy *E* is a constant of integration that counts as an arbitrary constant for the problem, and it may be possible to integrate the velocities from this energy relation to solve for the coordinates.

### Mechanical similarity

If the potential energy is a homogeneous function of the coordinates and independent of time, and all position vectors are scaled by the same nonzero constant *α*, **r***k*′ = *α***r***k*, so that $V(\alpha \mathbf {r} _{1},\alpha \mathbf {r} _{2},\ldots ,\alpha \mathbf {r} _{N})=\alpha ^{N}V(\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N})$ and time is scaled by a factor *β*, *t*′ = *βt*, then the velocities **v***k* are scaled by a factor of *α*/*β* and the kinetic energy *T* by (*α*/*β*)2. The entire Lagrangian has been scaled by the same factor if ${\frac {\alpha ^{2}}{\beta ^{2}}}=\alpha ^{N}\quad \Rightarrow \quad \beta =\alpha ^{1-{\frac {N}{2}}}.$

Since the lengths and times have been scaled, the trajectories of the particles in the system follow geometrically similar paths differing in size. The length *l* traversed in time *t* in the original trajectory corresponds to a new length *l*′ traversed in time *t*′ in the new trajectory, given by the ratios ${\frac {t'}{t}}=\left({\frac {l'}{l}}\right)^{1-{\frac {N}{2}}}.$

### Interacting particles

For a given system, if two subsystems *A* and *B* are non-interacting, the Lagrangian *L* of the overall system is the sum of the Lagrangians *L**A* and *L**B* for the subsystems: $L=L_{A}+L_{B}.$

If they do interact this is not possible. In some situations, it may be possible to separate the Lagrangian of the system *L* into the sum of non-interacting Lagrangians, plus another Lagrangian *L**AB* containing information about the interaction, $L=L_{A}+L_{B}+L_{AB}.$

This may be physically motivated by taking the non-interacting Lagrangians to be kinetic energies only, while the interaction Lagrangian is the system's total potential energy. Also, in the limiting case of negligible interaction, *L**AB* tends to zero reducing to the non-interacting case above.

The extension to more than two non-interacting subsystems is straightforward – the overall Lagrangian is the sum of the separate Lagrangians for each subsystem. If there are interactions, then interaction Lagrangians may be added.

### Consequences of singular Lagrangians

From the Euler-Lagrange equations, it follows that: ${\begin{aligned}&{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}_{i}}}-{\frac {\partial L}{\partial q_{i}}}=0\\&{\frac {\partial ^{2}L}{\partial q_{j}\partial {\dot {q}}_{i}}}{\frac {dq_{j}}{dt}}+{\frac {\partial ^{2}L}{\partial {\dot {q}}_{j}\partial {\dot {q}}_{i}}}{\frac {d{\dot {q}}_{j}}{dt}}+{\frac {\partial L}{\partial t}}-{\frac {\partial L}{\partial q_{i}}}=0\\&\sum _{j}W_{ij}(q,{\dot {q}},t){\ddot {q}}_{j}={\frac {\partial L}{\partial q_{i}}}-{\frac {\partial L}{\partial t}}-\sum _{j}{\frac {\partial ^{2}L}{\partial {\dot {q}}_{i}\partial q_{j}}}{\dot {q}}_{j},\\\end{aligned}}$

where the matrix is defined as $W_{ij}={\frac {\partial ^{2}L}{\partial {\dot {q}}_{i}\partial {\dot {q}}_{j}}}$ . If the matrix W is non-singular, the above equations can be solved to represent ${\ddot {q}}$ as a function of $({\dot {q}},q,t)$ . If the matrix is non-invertible, it would not be possible to represent all ${\ddot {q}}$ 's as a function of $({\dot {q}},q,t)$ but also, the Hamiltonian equations of motions will not take the standard form.


## Examples

The following examples apply Lagrange's equations of the second kind to mechanical problems.

### Conservative force

A particle of mass *m* moves under the influence of a conservative force derived from the gradient ∇ of a scalar potential, $\mathbf {F} =-{\boldsymbol {\nabla }}V(\mathbf {r} ).$

If there are more particles, in accordance with the above results, the total kinetic energy is a sum over all the particle kinetic energies, and the potential is a function of all the coordinates.

#### Cartesian coordinates

The Lagrangian of the particle can be written $L(x,y,z,{\dot {x}},{\dot {y}},{\dot {z}})={\frac {1}{2}}m({\dot {x}}^{2}+{\dot {y}}^{2}+{\dot {z}}^{2})-V(x,y,z).$

The equations of motion for the particle are found by applying the Euler–Lagrange equation, for the *x* coordinate ${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {\partial L}{\partial {\dot {x}}}}\right)={\frac {\partial L}{\partial x}},$ with derivatives ${\frac {\partial L}{\partial x}}=-{\frac {\partial V}{\partial x}},\quad {\frac {\partial L}{\partial {\dot {x}}}}=m{\dot {x}},\quad {\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {\partial L}{\partial {\dot {x}}}}\right)=m{\ddot {x}},$ hence $m{\ddot {x}}=-{\frac {\partial V}{\partial x}},$ and similarly for the *y* and *z* coordinates. Collecting the equations in vector form we find $m{\ddot {\mathbf {r} }}=-{\boldsymbol {\nabla }}V$ which is Newton's second law of motion for a particle subject to a conservative force.

#### Polar coordinates in 2D and 3D

Using the spherical coordinates (*r*, *θ*, *φ*) as commonly used in physics (ISO 80000-2:2019 convention), where *r* is the radial distance to origin, *θ* is polar angle (also known as colatitude, zenith angle, normal angle, or inclination angle), and *φ* is the azimuthal angle, the Lagrangian for a central potential is $L={\frac {m}{2}}({\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}+r^{2}\sin ^{2}\theta \,{\dot {\varphi }}^{2})-V(r).$ So, in spherical coordinates, the Euler–Lagrange equations are $m{\ddot {r}}-mr({\dot {\theta }}^{2}+\sin ^{2}\theta \,{\dot {\varphi }}^{2})+{\frac {\partial V}{\partial r}}=0,$ ${\frac {\mathrm {d} }{\mathrm {d} t}}(mr^{2}{\dot {\theta }})-mr^{2}\sin \theta \cos \theta \,{\dot {\varphi }}^{2}=0,$ ${\frac {\mathrm {d} }{\mathrm {d} t}}(mr^{2}\sin ^{2}\theta \,{\dot {\varphi }})=0.$ The *φ* coordinate is cyclic since it does not appear in the Lagrangian, so the conserved momentum in the system is the angular momentum $p_{\varphi }={\frac {\partial L}{\partial {\dot {\varphi }}}}=mr^{2}\sin ^{2}\theta {\dot {\varphi }},$ in which *r*, *θ* and *dφ*/*dt* can all vary with time, but only in such a way that *p**φ* is constant.

The Lagrangian in two-dimensional polar coordinates is recovered by fixing *θ* to the constant value *π*/2.

### Pendulum on a movable support

Consider a pendulum of mass *m* and length *ℓ*, which is attached to a support with mass *M*, which can move along a line in the x -direction. Let x be the coordinate along the line of the support, and let us denote the position of the pendulum by the angle $\theta$ from the vertical. The coordinates and velocity components of the pendulum bob are ${\begin{array}{rll}&x_{\mathrm {pend} }=x+\ell \sin \theta &\quad \Rightarrow \quad {\dot {x}}_{\mathrm {pend} }={\dot {x}}+\ell {\dot {\theta }}\cos \theta \\&y_{\mathrm {pend} }=-\ell \cos \theta &\quad \Rightarrow \quad {\dot {y}}_{\mathrm {pend} }=\ell {\dot {\theta }}\sin \theta .\end{array}}$

The generalized coordinates can be taken to be x and $\theta$ . The kinetic energy of the system is then $T={\frac {1}{2}}M{\dot {x}}^{2}+{\frac {1}{2}}m\left({\dot {x}}_{\mathrm {pend} }^{2}+{\dot {y}}_{\mathrm {pend} }^{2}\right)$ and the potential energy is $V=mgy_{\mathrm {pend} }$ giving the Lagrangian ${\begin{array}{rcl}L&=&T-V\\&=&{\frac {1}{2}}M{\dot {x}}^{2}+{\frac {1}{2}}m\left[\left({\dot {x}}+\ell {\dot {\theta }}\cos \theta \right)^{2}+\left(\ell {\dot {\theta }}\sin \theta \right)^{2}\right]+mg\ell \cos \theta \\&=&{\frac {1}{2}}\left(M+m\right){\dot {x}}^{2}+m{\dot {x}}\ell {\dot {\theta }}\cos \theta +{\frac {1}{2}}m\ell ^{2}{\dot {\theta }}^{2}+mg\ell \cos \theta .\end{array}}$

Since *x* is absent from the Lagrangian, it is a cyclic coordinate. The conserved momentum is $p_{x}={\frac {\partial L}{\partial {\dot {x}}}}=(M+m){\dot {x}}+m\ell {\dot {\theta }}\cos \theta ,$ and the Lagrange equation for the support coordinate x is $(M+m){\ddot {x}}+m\ell {\ddot {\theta }}\cos \theta -m\ell {\dot {\theta }}^{2}\sin \theta =0.$

The Lagrange equation for the angle *θ* is ${\frac {\mathrm {d} }{\mathrm {d} t}}\left[m({\dot {x}}\ell \cos \theta +\ell ^{2}{\dot {\theta }})\right]+m\ell ({\dot {x}}{\dot {\theta }}+g)\sin \theta =0;$ and simplifying ${\ddot {\theta }}+{\frac {\ddot {x}}{\ell }}\cos \theta +{\frac {g}{\ell }}\sin \theta =0.$

These equations may look quite complicated, but finding them with Newton's laws would have required carefully identifying all forces, which would have been much more laborious and prone to errors. By considering limit cases, the correctness of this system can be verified: For example, ${\ddot {x}}\to 0$ should give the equations of motion for a simple pendulum that is at rest in some inertial frame, while ${\ddot {\theta }}\to 0$ should give the equations for a pendulum in a constantly accelerating system, etc. Furthermore, it is trivial to obtain the results numerically, given suitable starting conditions and a chosen time step, by stepping through the results iteratively.

### Two-body central force problem

Two bodies of masses *m*1 and *m*2 with position vectors **r**1 and **r**2 are in orbit about each other due to an attractive central potential *V*. We may write down the Lagrangian in terms of the position coordinates as they are, but it is an established procedure to convert the two-body problem into a one-body problem as follows. Introduce the Jacobi coordinates; the separation of the bodies **r** = **r**2 − **r**1 and the location of the center of mass **R** = (*m*1**r**1 + *m*2**r**2)/(*m*1 + *m*2). The Lagrangian is then $L=\underbrace {{\frac {1}{2}}M{\dot {\mathbf {R} }}^{2}} _{L_{\text{cm}}}+\underbrace {{\frac {1}{2}}\mu {\dot {\mathbf {r} }}^{2}-V(|\mathbf {r} |)} _{L_{\text{rel}}}$ where *M* = *m*1 + *m*2 is the total mass, *μ* = *m*1*m*2/(*m*1 + *m*2) is the reduced mass, and *V* the potential of the radial force, which depends only on the magnitude of the separation |**r**| = |**r**2 − **r**1|. The Lagrangian splits into a *center-of-mass* term *L*cm and a *relative motion* term *L*rel.

The Euler–Lagrange equation for **R** is simply $M{\ddot {\mathbf {R} }}=0,$ which states the center of mass moves in a straight line at constant velocity.

Since the relative motion only depends on the magnitude of the separation, it is ideal to use polar coordinates (*r*, *θ*) and take *r* = |**r**|, $L_{\text{rel}}={\frac {1}{2}}\mu \left({\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}\right)-V(r),$ so *θ* is a cyclic coordinate with the corresponding conserved (angular) momentum $p_{\theta }={\frac {\partial L_{\text{rel}}}{\partial {\dot {\theta }}}}=\mu r^{2}{\dot {\theta }}=\ell .$

The radial coordinate *r* and angular velocity d*θ*/d*t* can vary with time, but only in such a way that *ℓ* is constant. The Lagrange equation for *r* is $\mu r{\dot {\theta }}^{2}-{\frac {dV}{dr}}=\mu {\ddot {r}}.$

This equation is identical to the radial equation obtained using Newton's laws in a *co-rotating* reference frame, that is, a frame rotating with the reduced mass so it appears stationary. Eliminating the angular velocity d*θ*/d*t* from this radial equation, $\mu {\ddot {r}}=-{\frac {\mathrm {d} V}{\mathrm {d} r}}+{\frac {\ell ^{2}}{\mu r^{3}}}.$ which is the equation of motion for a one-dimensional problem in which a particle of mass *μ* is subjected to the inward central force −d*V*/d*r* and a second outward force, called in this context the *(Lagrangian) centrifugal force* (see centrifugal force#Other uses of the term): $F_{\mathrm {cf} }=\mu r{\dot {\theta }}^{2}={\frac {\ell ^{2}}{\mu r^{3}}}.$

Of course, if one remains entirely within the one-dimensional formulation, *ℓ* enters only as some imposed parameter of the external outward force, and its interpretation as angular momentum depends upon the more general two-dimensional problem from which the one-dimensional problem originated.

If one arrives at this equation using Newtonian mechanics in a co-rotating frame, the interpretation is evident as the centrifugal force in that frame due to the rotation of the frame itself. If one arrives at this equation directly by using the generalized coordinates (*r*, *θ*) and simply following the Lagrangian formulation without thinking about frames at all, the interpretation is that the centrifugal force is an outgrowth of *using polar coordinates*. As Hildebrand says:

"Since such quantities are not true physical forces, they are often called *inertia forces*. Their presence or absence depends, not upon the particular problem at hand, but *upon the coordinate system chosen*." In particular, if Cartesian coordinates are chosen, the centrifugal force disappears, and the formulation involves only the central force itself, which provides the centripetal force for a curved motion.

This viewpoint, that fictitious forces originate in the choice of coordinates, often is expressed by users of the Lagrangian method. This view arises naturally in the Lagrangian approach, because the frame of reference is (possibly unconsciously) selected by the choice of coordinates. For example, see for a comparison of Lagrangians in an inertial and in a noninertial frame of reference. See also the discussion of "total" and "updated" Lagrangian formulations in. Unfortunately, this usage of "inertial force" conflicts with the Newtonian idea of an inertial force. In the Newtonian view, an inertial force originates in the acceleration of the frame of observation (the fact that it is not an inertial frame of reference), not in the choice of coordinate system. To keep matters clear, it is safest to refer to the Lagrangian inertial forces as *generalized* inertial forces, to distinguish them from the Newtonian vector inertial forces. That is, one should avoid following Hildebrand when he says (p. 155) "we deal *always* with *generalized* forces, velocities accelerations, and momenta. For brevity, the adjective "generalized" will be omitted frequently."

It is known that the Lagrangian of a system is not unique. Within the Lagrangian formalism the Newtonian fictitious forces can be identified by the existence of alternative Lagrangians in which the fictitious forces disappear, sometimes found by exploiting the symmetry of the system.


## Extensions to include non-conservative forces

### Dissipative forces

Dissipation (i.e. non-conservative systems) can also be treated with an effective Lagrangian formulated by a certain doubling of the degrees of freedom.

In a more general formulation, the forces could be both conservative and viscous. If an appropriate transformation can be found from the **F***i*, Rayleigh suggests using a dissipation function, *D*, of the following form: $D={\frac {1}{2}}\sum _{j=1}^{m}\sum _{k=1}^{m}C_{jk}{\dot {q}}_{j}{\dot {q}}_{k},$ where *C**jk* are constants that are related to the damping coefficients in the physical system, though not necessarily equal to them. If *D* is defined this way, then $Q_{j}=-{\frac {\partial V}{\partial q_{j}}}-{\frac {\partial D}{\partial {\dot {q}}_{j}}}$ and ${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {\partial L}{\partial {\dot {q}}_{j}}}\right)-{\frac {\partial L}{\partial q_{j}}}+{\frac {\partial D}{\partial {\dot {q}}_{j}}}=0.$

### Electromagnetism

A test particle is a particle whose mass and charge are assumed to be so small that its effect on external system is insignificant. It is often a hypothetical simplified point particle with no properties other than mass and charge. Real particles like electrons and up quarks are more complex and have additional terms in their Lagrangians. Not only can the fields form non conservative potentials, these potentials can also be velocity dependent.

The Lagrangian for a charged particle with electrical charge *q*, interacting with an electromagnetic field, is the prototypical example of a velocity-dependent potential. The electric scalar potential *ϕ* = *ϕ*(**r**, *t*) and magnetic vector potential **A** = **A**(**r**, *t*) are defined from the electric field **E** = **E**(**r**, *t*) and magnetic field **B** = **B**(**r**, *t*) as follows: $\mathbf {E} =-{\boldsymbol {\nabla }}\phi -{\frac {\partial \mathbf {A} }{\partial t}},\quad \mathbf {B} ={\boldsymbol {\nabla }}\times \mathbf {A} .$

The Lagrangian of a massive charged test particle in an electromagnetic field $L={\tfrac {1}{2}}m{\dot {\mathbf {r} }}^{2}+q\,{\dot {\mathbf {r} }}\cdot \mathbf {A} -q\phi ,$ is called minimal coupling. This is a good example of when the common rule of thumb that the Lagrangian is the kinetic energy minus the potential energy is incorrect. Combined with Euler–Lagrange equation, it produces the Lorentz force law $m{\ddot {\mathbf {r} }}=q\mathbf {E} +q{\dot {\mathbf {r} }}\times \mathbf {B}$

Under gauge transformation: $\mathbf {A} \rightarrow \mathbf {A} +{\boldsymbol {\nabla }}f,\quad \phi \rightarrow \phi -{\dot {f}},$ where *f*(**r**,*t*) is any scalar function of space and time, the aforementioned Lagrangian transforms like: $L\rightarrow L+q\left({\dot {\mathbf {r} }}\cdot {\boldsymbol {\nabla }}+{\frac {\partial }{\partial t}}\right)f=L+q{\frac {df}{dt}},$ which still produces the same Lorentz force law.

Note that the canonical momentum (conjugate to position **r**) is the kinetic momentum plus a contribution from the **A** field (known as the potential momentum): $\mathbf {p} ={\frac {\partial L}{\partial {\dot {\mathbf {r} }}}}=m{\dot {\mathbf {r} }}+q\mathbf {A} .$

This relation is also used in the minimal coupling prescription in quantum mechanics and quantum field theory. From this expression, we can see that the canonical momentum **p** is not gauge invariant, and therefore not a measurable physical quantity; However, if **r** is cyclic (i.e. Lagrangian is independent of position **r**), which happens if the *ϕ* and **A** fields are uniform, then this canonical momentum **p** given here is the conserved momentum, while the measurable physical kinetic momentum *m***v** is not.


## Other contexts and formulations

The ideas in Lagrangian mechanics have numerous applications in other areas of physics, and can adopt generalized results from the calculus of variations.

### Alternative formulations of classical mechanics

A closely related formulation of classical mechanics is Hamiltonian mechanics. The Hamiltonian is defined by $H=\sum _{i=1}^{n}{\dot {q}}_{i}{\frac {\partial L}{\partial {\dot {q}}_{i}}}-L$ and can be obtained by performing a Legendre transformation on the Lagrangian, which introduces new variables canonically conjugate to the original variables. For example, given a set of generalized coordinates, the variables canonically conjugate are the generalized momenta. This doubles the number of variables, but makes differential equations first order. The Hamiltonian is a particularly ubiquitous quantity in quantum mechanics (see Hamiltonian (quantum mechanics)).

Routhian mechanics is a hybrid formulation of Lagrangian and Hamiltonian mechanics, which is not often used in practice but an efficient formulation for cyclic coordinates.

### Momentum space formulation

The Euler–Lagrange equations can also be formulated in terms of the generalized momenta rather than generalized coordinates. Performing a Legendre transformation on the generalized coordinate Lagrangian *L*(**q**, d**q**/d*t*, *t*) obtains the generalized momenta Lagrangian *L*′(**p**, d**p**/d*t*, *t*) in terms of the original Lagrangian, as well the EL equations in terms of the generalized momenta. Both Lagrangians contain the same information, and either can be used to solve for the motion of the system. In practice generalized coordinates are more convenient to use and interpret than generalized momenta.

### Higher derivatives of generalized coordinates

There is no mathematical reason to restrict the derivatives of generalized coordinates to first order only. It is possible to derive modified EL equations for a Lagrangian containing higher order derivatives, see Euler–Lagrange equation for details. However, from the physical point-of-view there is an obstacle to include time derivatives higher than the first order, which is implied by Ostrogradsky's construction of a canonical formalism for nondegenerate higher derivative Lagrangians, see Ostrogradsky instability

### Optics

Lagrangian mechanics can be applied to geometrical optics, by applying variational principles to rays of light in a medium, and solving the EL equations gives the equations of the paths the light rays follow.

### Relativistic formulation

Lagrangian mechanics can be formulated in special relativity and general relativity. Some features of Lagrangian mechanics are retained in the relativistic theories but difficulties quickly appear in other respects. In particular, the EL equations take the same form, and the connection between cyclic coordinates and conserved momenta still applies, however the Lagrangian must be modified and is not simply the kinetic minus the potential energy of a particle. Also, it is not straightforward to handle multiparticle systems in a manifestly covariant way, it may be possible if a particular frame of reference is singled out.

### Quantum mechanics

In quantum mechanics, action and quantum-mechanical phase are related via the Planck constant, and the principle of stationary action can be understood in terms of constructive interference of wave functions.

In 1948, Feynman discovered the path integral formulation extending the principle of least action to quantum mechanics for electrons and photons. In this formulation, particles travel every possible path between the initial and final states; the probability of a specific final state is obtained by summing over all possible trajectories leading to it. In the classical regime, the path integral formulation cleanly reproduces Hamilton's principle, and Fermat's principle in optics.

### Classical field theory

In Lagrangian mechanics, the generalized coordinates form a discrete set of variables that define the configuration of a system. In classical field theory, the physical system is not a set of discrete particles, but rather a continuous field *ϕ*(**r**, *t*) defined over a region of 3D space. Associated with the field is a Lagrangian density ${\mathcal {L}}(\phi ,\nabla \phi ,{\dot {\phi }},\mathbf {r} ,t)$ defined in terms of the field and its space and time derivatives at a location **r** and time *t*. Analogous to the particle case, for non-relativistic applications the Lagrangian density is also the kinetic energy density of the field, minus its potential energy density (this is not true in general, and the Lagrangian density has to be "reverse engineered"). The Lagrangian is then the volume integral of the Lagrangian density over 3D space $L(t)=\int {\mathcal {L}}\,\mathrm {d} ^{3}\mathbf {r}$ where d3**r** is a 3D differential volume element. The Lagrangian is a function of time since the Lagrangian density has implicit space dependence via the fields, and may have explicit spatial dependence, but these are removed in the integral, leaving only time in as the variable for the Lagrangian.

### Noether's theorem

The action principle, and the Lagrangian formalism, are tied closely to Noether's theorem, which connects physical conserved quantities to continuous symmetries of a physical system.

If the Lagrangian is invariant under a symmetry, then the resulting equations of motion are also invariant under that symmetry. This characteristic is very helpful in showing that theories are consistent with either special relativity or general relativity.

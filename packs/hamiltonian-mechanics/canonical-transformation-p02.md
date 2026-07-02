---
title: "Canonical transformation (part 2/2)"
source: https://en.wikipedia.org/wiki/Canonical_transformation
domain: hamiltonian-mechanics
license: CC-BY-SA-4.0
tags: hamiltonian mechanics, phase space, canonical transformation, poisson bracket
fetched: 2026-07-02
part: 2/2
---

## Infinitesimal canonical transformation

Consider the canonical transformation that depends on a continuous parameter $\alpha$ , as follows:

${\begin{aligned}&Q(q,p,t;\alpha )\quad \quad \quad &Q(q,p,t;0)=q\\&P(q,p,t;\alpha )\quad \quad {\text{with}}\quad &P(q,p,t;0)=p\\\end{aligned}}$

For infinitesimal values of $\alpha$ , the corresponding transformations are called as *infinitesimal canonical transformations* which are also known as differential canonical transformations.

### Explicit construction

Consider the following generating function:

$G_{2}(q,P,t)=qP+\alpha G(q,P,t)$

Since for $\alpha =0$ , $G_{2}=qP$ has the resulting canonical transformation, $Q=q$ and $P=p$ , this type of generating function can be used for infinitesimal canonical transformation by restricting $\alpha$ to an infinitesimal value.

From the conditions of generators of second type:

${\begin{aligned}{p}&={\frac {\partial G_{2}}{\partial {q}}}=P+\alpha {\frac {\partial G}{\partial {q}}}(q,P,t)\\{Q}&={\frac {\partial G_{2}}{\partial {P}}}=q+\alpha {\frac {\partial G}{\partial {P}}}(q,P,t)\\\end{aligned}}$

Since $P=P(q,p,t;\alpha )$ , changing the variables of the function G to $G(q,p,t)$ and neglecting terms of higher order of $\alpha$ , gives:

${\begin{aligned}{p}&=P+\alpha {\frac {\partial G}{\partial {q}}}(q,p,t)\\{Q}&=q+\alpha {\frac {\partial G}{\partial p}}(q,p,t)\\\end{aligned}}$

Infinitesimal canonical transformations can also be derived using the matrix form of the symplectic condition. The function $G(q,p,t)$ is very significant in infinitesimal canonical transformations and is referred to as the generator of infinitesimal canonical transformation.

### Active and passive transformations

In the active view of transformations, the coordinate system is changed without the physical system changing, whereas in the passive view of transformation, the coordinate system is retained and the physical system is said to undergo transformations.

#### Active view of transformation

Thus, using the relations from infinitesimal canonical transformations, the change in the system states under active view of the canonical transformation is said to be:

${\begin{aligned}&\delta q=\alpha {\frac {\partial G}{\partial p}}(q,p,t)\quad {\text{and}}\quad \delta p=-\alpha {\frac {\partial G}{\partial q}}(q,p,t),\\\end{aligned}}$

or as $\delta \eta =\alpha J\nabla _{\eta }G$ in matrix form.

For any function $u(\eta )$ , it changes under active view of the transformation according to:

$\delta u=u(\eta +\delta \eta )-u(\eta )=(\nabla _{\eta }u)^{T}\delta \eta =\alpha (\nabla _{\eta }u)^{T}J(\nabla _{\eta }G)=\alpha \{u,G\}.$

#### Passive view of transformation

Considering the change of Hamiltonians in the passive view, i.e., for a fixed point, $K(Q=q_{0},P=p_{0},t)-H(q=q_{0},p=p_{0},t)=\left(H(q_{0}',p_{0}',t)+{\frac {\partial G_{2}}{\partial t}}\right)-H(q_{0},p_{0},t)=-\delta H+\alpha {\frac {\partial G}{\partial t}}=\alpha \left(\{G,H\}+{\frac {\partial G}{\partial t}}\right)=\alpha {\frac {dG}{dt}}$

where ${\textstyle (q=q_{0}',p=p_{0}')}$ are mapped to the point, ${\textstyle (Q=q_{0},P=p_{0})}$ by the infinitesimal canonical transformation, and similar change of variables for $G(q,P,t)$ to $G(q,p,t)$ is considered up-to first order of $\alpha$ . Hence, if the Hamiltonian is invariant for infinitesimal canonical transformations, its generator is a constant of motion.

### Generators of dynamical symmetry transformations

Consider the transformation where the change of coordinates also depends on the generalized velocities.

${\begin{aligned}q^{r}\to q^{r}+\delta q^{r}\\\delta q^{r}=\epsilon \phi ^{r}(q,{\dot {q}},t)\\\end{aligned}}$

If the above is a dynamical symmetry, then the lagrangian changes by:

$\delta L=\epsilon {\frac {d}{dt}}F(q,{\dot {q}},t)$

and the new Lagrangian is said to be dynamically equivalent to the old Lagrangian as it ensures the resultant equations of motion being the same. The change in generalized velocity and momentum term can be derived as:

${\begin{aligned}p={\frac {\partial L}{\partial {\dot {q}}}},\quad &{\dot {q}}={\frac {dq}{dt}}\\\delta p_{r}={\frac {\partial ^{2}L}{\partial q^{s}\partial {\dot {q}}^{r}}}\delta q^{s}+{\frac {\partial ^{2}L}{\partial {\dot {q}}^{s}\partial {\dot {q}}^{r}}}\delta {\dot {q}}^{s},\quad &\delta {\dot {q}}^{r}=\epsilon {\frac {\partial \phi ^{r}}{\partial q^{s}}}{\dot {q}}^{s}+\epsilon {\frac {\partial \phi ^{r}}{\partial {\dot {q}}^{s}}}{\ddot {q}}^{s}+\epsilon {\frac {\partial \phi ^{r}}{\partial t}}\\\end{aligned}}$

#### Generator of transformation

Using the change in Lagrangian property of a dynamical symmetry:

${\frac {d}{dt}}F={\frac {\partial F}{\partial q^{r}}}{\dot {q}}^{r}+{\frac {\partial F}{\partial {\dot {q}}^{r}}}{\ddot {q}}^{r}+{\frac {\partial F}{\partial t}}={\frac {\delta L}{\epsilon }}=\left({\frac {\partial L}{\partial q^{r}}}\phi ^{r}+{\frac {\partial L}{\partial {\dot {q}}^{r}}}{\frac {\partial \phi ^{r}}{\partial t}}\right)+p_{s}{\frac {\partial \phi ^{s}}{\partial q^{r}}}{\dot {q}}^{r}+p_{s}{\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{r}}}{\ddot {q}}^{r}$

Since the ${\ddot {q}}$ terms appear only once in either side and the equation must hold independent of dynamics or equation of motion that relate ${\ddot {q}}$ to $(q,{\dot {q}},t)$ , it's coefficients must be equal for this to be true, giving the relation: ${\textstyle p_{s}{\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{r}}}={\frac {\partial F}{\partial {\dot {q}}^{r}}}}$ using which, it can be shown that

$\{q^{r},\epsilon (p_{s}\phi ^{s}-F)\}=\delta q^{r},\quad \{p_{r},\epsilon (p_{s}\phi ^{s}-F)\}=\delta p_{r}+\epsilon \left({\frac {\partial L}{\partial q^{s}}}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}^{s}}}\right){\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{r}}}$

Hence, the term $p\phi -F$ generates the canonical dynamical symmetry transformation if either the Euler Lagrange relation gives zero, or if ${\frac {\partial \phi _{s}}{\partial {\dot {q}}^{r}}}=0\,\forall s,r$ which is a infinitesimal point transformation. Note that in the point transformation condition, the quantity generates the transformation regardless of if the Euler Lagrange equations are satisfied and since they do not depend on the dynamics of the problem are said to be a purely kinematic relation.

Similar results are obtained in classical field theory, for example, in a Lorentz invariant Lagrangian density where corresponding conserved charges, momentum density $P^{\mu }$ generates translation of fields and $M^{\mu \nu }$ of Lorentz invariance generates Lorentz transformation of fields.

| Proof |
|---|
| Firstly, the change in momentum can be expressed in a more useful form as follows: $\delta p_{r}={\frac {\partial ^{2}L}{\partial q^{s}\partial {\dot {q}}^{r}}}\delta q^{s}+{\frac {\partial ^{2}L}{\partial {\dot {q}}^{s}\partial {\dot {q}}^{r}}}\delta {\dot {q}}^{s}={\frac {\partial }{\partial {\dot {q}}^{r}}}\left({\frac {\partial L}{\partial q^{s}}}\delta q^{s}+{\frac {\partial L}{\partial {\dot {q}}^{s}}}\delta {\dot {q}}^{s}\right)-{\frac {\partial L}{\partial q^{s}}}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta q^{s})-{\frac {\partial L}{\partial {\dot {q}}^{s}}}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta {\dot {q}}^{s})={\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta L)-p_{s}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta {\dot {q}}^{s})-{\frac {\partial L}{\partial q^{s}}}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta q^{s})$ Simplifying the required poisson brackets, ${\begin{aligned}\{q^{r},\epsilon (p_{s}\phi ^{s}-F)\}=\epsilon \left(\phi _{r}+{\frac {\partial {\dot {q}}^{m}}{\partial p_{r}}}{\cancelto {=0}{\left(p_{s}{\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{m}}}-{\frac {\partial F}{\partial {\dot {q}}^{m}}}\right)}}\right)&=\delta q^{r}\\\{p_{r},\epsilon (p_{s}\phi ^{s}-F)\}=\epsilon \left(-p_{s}{\frac {\partial \phi ^{s}}{\partial q^{r}}}+{\frac {\partial F}{\partial q^{r}}}+{\cancelto {=0}{\left({\frac {\partial F}{\partial {\dot {q}}^{m}}}-p_{s}{\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{m}}}\right)}}\left({\frac {\partial {\dot {q}}^{m}}{\partial q^{r}}}\right)_{q,p,t}\right)&=\epsilon \left(-p_{s}{\frac {\partial \phi ^{s}}{\partial q^{r}}}+{\frac {\partial F}{\partial q^{r}}}\right)\\\end{aligned}}$ As a preliminary result, for any function of $(q,{\dot {q}},t)$ , while accounting for dynamic behavior of ${\ddot {q}}$ : ${\frac {\partial }{\partial {\dot {q}}^{r}}}{\frac {d}{dt}}-{\frac {d}{dt}}{\frac {\partial }{\partial {\dot {q}}^{r}}}={\frac {\partial }{\partial q^{r}}}+{\frac {\partial {\ddot {q}}^{s}}{\partial {\dot {q}}^{r}}}{\frac {\partial }{\partial {\dot {q}}^{s}}}$ which can be used to calculate the quantity: ${\frac {\partial }{\partial {\dot {q}}^{r}}}\left({\frac {dF}{dt}}\right)-p_{s}\left({\frac {\partial }{\partial {\dot {q}}^{r}}}\left({\frac {d}{dt}}\phi ^{s}\right)\right)-{\dot {p}}_{s}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\phi ^{s})={\frac {d}{dt}}{\cancel {\left({\frac {\partial }{\partial {\dot {q}}^{r}}}F-p_{s}{\frac {\partial }{\partial {\dot {q}}^{r}}}\phi ^{s}\right)}}+{\frac {\partial {\ddot {q}}^{s}}{\partial {\dot {q}}^{r}}}{\cancel {\left({\frac {\partial }{\partial {\dot {q}}^{s}}}F-p_{m}{\frac {\partial }{\partial {\dot {q}}^{s}}}\phi ^{m}\right)}}-p_{s}{\frac {\partial \phi ^{s}}{\partial q^{r}}}+{\frac {\partial F}{\partial q^{r}}}=\{p_{r},(p\phi -F)\}$ This relation can be restated and combined with the formula for $\delta p_{r}$ to give the required relation for momentum. $\{p_{r},\epsilon (p_{s}\phi ^{s}-F)\}={\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta L)-p_{s}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta {\dot {q}}^{s})-{\dot {p}}_{s}{\frac {\partial }{\partial {\dot {q}}^{r}}}(\delta q^{s})=\delta p_{r}+\epsilon \left({\frac {\partial L}{\partial q^{s}}}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}^{s}}}\right){\frac {\partial \phi ^{s}}{\partial {\dot {q}}^{r}}}$ |

#### Noether Invariant

Using Euler Lagrange relation for the provided Lagrangian, the invariants of motion can be derived as: $\delta L-\epsilon {\frac {d}{dt}}F(q,{\dot {q}},t)=\epsilon \phi {\cancelto {=0}{\left({\frac {\partial }{\partial q}}-{\frac {d}{dt}}{\frac {\partial }{\partial {\dot {q}}}}\right)L}}+\epsilon {\frac {d}{dt}}\left(\phi {\frac {\partial }{\partial {\dot {q}}}}L-F\right)=\epsilon {\frac {d}{dt}}\left(\phi {\frac {\partial }{\partial {\dot {q}}}}L-F\right)=0$

Hence $\left(\phi {\frac {\partial }{\partial {\dot {q}}}}L-F\right)=p\phi -F$ is a constant of motion. Hence, the derived Noether invariant also generates the same symmetry transformation as shown previously.

### Examples of ICT

#### Time evolution

Taking $G(q,p,t)=H(q,p,t)$ and $\alpha =dt$ , then $\delta \eta =(J\nabla _{\eta }H)dt={\dot {\eta }}dt=d\eta$ . Thus the continuous application of such a transformation maps the coordinates $\eta (\tau )$ to $\eta (\tau +t)$ . Hence if the Hamiltonian is time translation invariant, i.e. does not have explicit time dependence, its value is conserved for the motion.

#### Translation

Taking $G(q,p,t)=p_{k}$ , $\delta p_{i}=0$ and $\delta q_{i}=\alpha \delta _{ik}$ . Hence, the canonical momentum generates a shift in the corresponding generalized coordinate and if the Hamiltonian is invariant of translation, the momentum is a constant of motion.

#### Rotation

Consider an orthogonal system for an N-particle system:

${\begin{array}{l}{\mathbf {q} =\left(x_{1},y_{1},z_{1},\ldots ,x_{n},y_{n},z_{n}\right),}\\{\mathbf {p} =\left(p_{1x},p_{1y},p_{1z},\ldots ,p_{nx},p_{ny},p_{nz}\right).}\end{array}}$

Choosing the generator to be: $G=L_{z}=\sum _{i=1}^{n}\left(x_{i}p_{iy}-y_{i}p_{ix}\right)$ and the infinitesimal value of $\alpha =\delta \phi$ , then the change in the coordinates is given for x by:

${\begin{array}{c}{\delta x_{i}=\{x_{i},G\}\delta \phi =\displaystyle \sum _{j}\{x_{i},x_{j}p_{jy}-y_{j}p_{jx}\}\delta \phi =\displaystyle \sum _{j}(\underbrace {\{x_{i},x_{j}p_{jy}\}} _{=0}-{\{x_{i},y_{j}p_{jx}\}}})\delta \phi \\{=\displaystyle -\sum _{j}y_{j}\underbrace {\{x_{i},p_{jx}\}} _{=\delta _{ij}}\delta \phi =-y_{i}\delta \phi }\end{array}}$

and similarly for y:

${\begin{array}{c}\delta y_{i}=\{y_{i},G\}\delta \phi =\displaystyle \sum _{j}\{y_{i},x_{j}p_{jy}-y_{j}p_{jx}\}\delta \phi =\displaystyle \sum _{j}(\{y_{i},x_{j}p_{jy}\}-\underbrace {\{y_{i},y_{j}p_{jx}\}} _{=0})\delta \phi \\{=\displaystyle \sum _{j}x_{j}\underbrace {\{y_{i},p_{jy}\}} _{=\delta _{ij}}\delta \phi =x_{i}\delta \phi \,,}\end{array}}$

whereas the z component of all particles is unchanged: ${\textstyle \delta z_{i}=\left\{z_{i},G\right\}\delta \phi =\sum _{j}\left\{z_{i},x_{j}p_{jy}-y_{j}p_{jx}\right\}\delta \phi =0}$ .

These transformations correspond to rotation about the z axis by angle $\delta \phi$ in its first order approximation. Hence, repeated application of the infinitesimal canonical transformation generates a rotation of system of particles about the z axis. If the Hamiltonian is invariant under rotation about the z axis, the generator, the component of angular momentum along the axis of rotation, is an invariant of motion.


## One parameter subgroup of Canonical transformations

Allowing the values of $\alpha$ to take continuous range of values in:

${\begin{aligned}&Q(q,p,t;\alpha )\quad \quad \quad &Q(q,p,t;0)=q\\&P(q,p,t;\alpha )\quad \quad {\text{with}}\quad &P(q,p,t;0)=p\\\end{aligned}}$

which can be expressed as $\epsilon ^{\mu }(\eta ,t;\alpha )$ where $\epsilon ^{\mu }(\eta ,t;0)=\eta ^{\mu }$ .

One parameter subgroup of Canonical transformations are those where the generator of the transformation can be used to generate coordinates where $\epsilon ^{\mu }(\epsilon (\eta ,t;\alpha _{1});\alpha _{2})=\epsilon ^{\mu }(\eta ,t;\alpha _{1}+\alpha _{2})$ is satisfied, i.e. composition of two canonical transformations of parameter $\alpha _{1}$ and $\alpha _{2}$ are the same as that of a single canonical transformation of parameter $\alpha _{1}+\alpha _{2}$ .

The condition on the transformations of the one parameter subgroup kind can be expressed equivalently as a differential equation:

$\delta \epsilon ^{\mu }(\eta ,t;\alpha )=\delta \alpha \{\epsilon ^{\nu },G\}=\delta \alpha J^{\mu \nu }{\frac {\partial G}{\partial \epsilon ^{\nu }}}(\epsilon (\eta ,t;\alpha ),t)\implies {\frac {d\epsilon ^{\mu }(\eta ,t;\alpha )}{d\alpha }}=J^{\mu \nu }{\frac {\partial G}{\partial \epsilon ^{\nu }}}(\epsilon (\eta ,t;\alpha ),t)$

for all $\eta$ given that the generator has no explicit dependence on $\alpha$ . The conditions $\epsilon ^{\mu }(\epsilon (\eta ,t;\alpha _{1});\alpha _{2})=\epsilon ^{\mu }(\eta ,t;\alpha _{1}+\alpha _{2})$ can be recovered since this equation is trivially satisfied when $\alpha _{2}=0$ which is considered initial values and the differential equations of both sides are of the same form implying the relation due to uniqueness of solutions with given initial values. Hence one parameter subgroups of canonical transformations are extension of infinitesimal canonical transformations to finite values of $\alpha$ by using the same functional form of its generator independent of parameter $\alpha$ .

As a consequence of the generator having no explicit dependence on $\alpha$ , the generator is also implicitly independent of $\alpha$ .

${\frac {dG(\epsilon (\eta ;\alpha ),t)}{d\alpha }}=\{G,G\}=0,\,\forall \alpha \implies G(\epsilon (\eta ;\alpha ),t)=G(\eta ,t)$

This can be used to express the differential equation as:

${\frac {d\epsilon ^{\mu }(\eta ,t;\alpha )}{d\alpha }}=\{\epsilon ^{\mu }(\eta ,t;\alpha ),G(\eta ,t)\}_{\eta }=:-{\tilde {G}}\epsilon ^{\mu }$

where the linear differential operator is defined as ${\tilde {G}}:=(\nabla _{\eta }G)^{T}J\nabla _{\eta }$ .

### Active view of transformation

Upon iteratively solving the differential equation, the solution of the differential equation follows as:

$\epsilon (\eta ,t;\alpha )=\eta +\alpha \{\eta ,G(\eta ,t)\}+{\frac {1}{2!}}\alpha ^{2}\{\{\eta ,G(\eta ,t)\},G(\eta ,t)\}+\cdots =e^{-\alpha {\tilde {G}}}\eta$

Change in function values ${\frac {df(\epsilon (\eta ;\alpha ),t)}{d\alpha }}=\{f(\epsilon (\eta ;\alpha ),t),G(\eta ,t)\}_{\eta }=:-{\tilde {G}}f(\epsilon (\eta ;\alpha ),t)$ by taking repeatedly in steps and using $\epsilon (\eta ,t;0)=\eta$ we get similarly

$f(e^{-\alpha {\tilde {G}}}\eta ,t)=f(\epsilon (\eta ;\alpha ),t)=f(\eta ,t)+\alpha \{f(\eta ,t),G(\eta ,t)\}+{\frac {1}{2!}}\alpha ^{2}\{\{f(\eta ,t),G(\eta ,t)\},G(\eta ,t)\}+\cdots =e^{-\alpha {\tilde {G}}}f(\eta ,t)$

### Passive view of transformation

Change in a function can be invoked by preserving its values on the same physical states in phase space as $f(\epsilon ,t)=f(\epsilon (\eta ;\alpha ),t)=f'(\epsilon (\eta ;\alpha +\delta \alpha ),t)=f'(\epsilon ',t)$ can be expressed as upto first order as:

$\delta 'f=f'(\epsilon )-f(\epsilon )=f'(\epsilon )-f'(\epsilon ')\approx f(\epsilon (\eta ;\alpha -\delta \alpha ))-f(\epsilon (\eta ;\alpha ))=-\delta \alpha \{f,G\}$

Including the change in the function as some explicit dependence on parameter of transformation $\alpha$ , it can be expressed as $f(\epsilon ,t;\alpha )$ where it is explicitly dependent on $\alpha$ such that ${\frac {\partial f(\epsilon ,t;\alpha )}{\partial \alpha }}=-\{f,G\}$ which indicates that the function transforms oppositely to that due to the coordinates to preserve well defined mapping from a physical point in phase space to its scalar values. It is also possible that functions transform without needing to preserve its values on the same physical states in phase space. Such as, for example, the Hamiltonian whose explicit dependence on the canonical transformation can be different from the above form, restated from its previous derivation as

${\frac {\partial H(\epsilon ,t;\alpha )}{\partial \alpha }}={\frac {dG}{dt}}$

which is similar to previous relation but also accounts for any explicit time dependence of the generator. Hence, if the Hamiltonian is invariant in passive view for infinitesimal canonical transformations, its generator is a constant of motion.


## Motion as canonical transformation

Motion itself (or, equivalently, a shift in the time origin) is a canonical transformation. If $\mathbf {Q} (t)\equiv \mathbf {q} (t+\tau )$ and $\mathbf {P} (t)\equiv \mathbf {p} (t+\tau )$ , then Hamilton's principle is automatically satisfied $\delta \int _{t_{1}}^{t_{2}}\left[\mathbf {P} \cdot {\dot {\mathbf {Q} }}-K(\mathbf {Q} ,\mathbf {P} ,t)\right]dt=\delta \int _{t_{1}+\tau }^{t_{2}+\tau }\left[\mathbf {p} \cdot {\dot {\mathbf {q} }}-H(\mathbf {q} ,\mathbf {p} ,t+\tau )\right]dt=0$ since a valid trajectory $(\mathbf {q} (t),\mathbf {p} (t))$ should always satisfy Hamilton's principle, regardless of the endpoints.


## Examples

- The translation $\mathbf {Q} (\mathbf {q} ,\mathbf {p} )=\mathbf {q} +\mathbf {a} ,\mathbf {P} (\mathbf {q} ,\mathbf {p} )=\mathbf {p} +\mathbf {b}$ where $\mathbf {a} ,\mathbf {b}$ are two constant vectors is a canonical transformation. Indeed, the Jacobian matrix is the identity, which is symplectic: $I^{\text{T}}JI=J$ .
- Set $\mathbf {x} =(q,p)$ and $\mathbf {X} =(Q,P)$ , the transformation $\mathbf {X} (\mathbf {x} )=R\mathbf {x}$ where $R\in SO(2)$ is a rotation matrix of order 2 is canonical. Keeping in mind that special orthogonal matrices obey $R^{\text{T}}R=I$ it's easy to see that the Jacobian is symplectic. However, this example only works in dimension 2: $SO(2)$ is the only special orthogonal group in which every matrix is symplectic. Note that the rotation here acts on $(q,p)$ and not on q and p independently, so these are not the same as a physical rotation of an orthogonal spatial coordinate system.
- The transformation $(Q(q,p),P(q,p))=(q+f(p),p)$ , where $f(p)$ is an arbitrary function of p , is canonical. Jacobian matrix is indeed given by ${\frac {\partial X}{\partial x}}={\begin{bmatrix}1&f'(p)\\0&1\end{bmatrix}}$ which is symplectic.


## Modern mathematical description

In mathematical terms, canonical coordinates are any coordinates on the phase space (cotangent bundle) of the system that allow the canonical one-form to be written as $\sum _{i}p_{i}\,dq^{i}$ up to a total differential (exact form). The change of variable between one set of canonical coordinates and another is a **canonical transformation**. The index of the generalized coordinates **q** is written here as a *superscript* ( $q^{i}$ ), not as a *subscript* as done above ( $q_{i}$ ). The superscript conveys the contravariant transformation properties of the generalized coordinates, and does *not* mean that the coordinate is being raised to a power. Further details may be found at the symplectomorphism article.


## History

The first major application of the canonical transformation was in 1846, by Charles Delaunay, in the study of the Earth-Moon-Sun system. This work resulted in the publication of a pair of large volumes as *Mémoires* by the French Academy of Sciences, in 1860 and 1867.

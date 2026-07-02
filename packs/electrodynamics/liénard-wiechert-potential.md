---
title: "Liénard–Wiechert potential"
source: https://en.wikipedia.org/wiki/Li%C3%A9nard%E2%80%93Wiechert_potential
domain: electrodynamics
license: CC-BY-SA-4.0
tags: classical electrodynamics, poynting vector, electromagnetic radiation, retarded potential
fetched: 2026-07-02
---

# Liénard–Wiechert potential

The **Liénard–Wiechert potentials** describe the classical electromagnetic effect of a moving electric point charge in terms of a vector potential and a scalar potential in the Lorenz gauge. Stemming directly from Maxwell's equations, these describe the complete, relativistically correct, time-varying electromagnetic field for a point charge in arbitrary motion, but are not corrected for quantum mechanical effects. Electromagnetic radiation in the form of waves can be obtained from these potentials. These expressions were developed in part by Alfred-Marie Liénard in 1898 and independently by Emil Wiechert in 1900.

## Equations

### Definition of Liénard–Wiechert potentials

Consider a point charge q exhibiting a prescribed motion along the trajectory $\mathbf {r} _{0}(t)$ with the velocity $\mathbf {v} (t)=d\mathbf {r} _{0}/dt$ . Let $\mathbf {r}$ be the observation point P at time t . The radius vector from the charge q to P is defined as $\mathbf {R} (t)=\mathbf {r} -\mathbf {r} _{0}(t)$ and the distance as $R=|\mathbf {R} |$ . The retarded time $t_{r}$ , in the context of distributions of charges and currents, is determined by solving the equation

$t=t_{r}+{\frac {R(t_{r})}{c}}.$

For each value of t , this equation is guaranteed to have only one root for $t_{r}$ , provided the $v=|\mathbf {v} |<c$ . By solving the above implicit equation, we obtain the retarded time $t_{r}$ as a function of t and $\mathbf {r}$ (and of the details about particle trajectory)

$t_{r}=t_{r}(\mathbf {r} ,t)$

.

The Liénard–Wiechert potentials $\varphi$ (scalar potential field) and $\mathbf {A}$ (vector potential field) are, for a source point charge q at position $\mathbf {r} _{s}$ traveling with velocity $\mathbf {v} _{s}$ :

$\varphi (\mathbf {r} ,t)=\left\{{\frac {q}{\left(R-{\frac {1}{c}}\mathbf {v} \cdot \mathbf {R} \right)}}\right\}_{t_{r}}$

and

$\mathbf {A} (\mathbf {r} ,t)=\left\{{\frac {q\mathbf {v} }{c\left(R-{\frac {1}{c}}\mathbf {v} \cdot \mathbf {R} \right)}}\right\}_{t_{r}}$

where the subscript $t_{r}$ denotes quantities evaluated at time $t_{r}$ , i.e., $R-{\frac {1}{c}}\mathbf {v} \cdot \mathbf {R} =R(t_{r})-{\frac {1}{c}}\mathbf {v} (t_{r})\cdot \mathbf {R} (t_{r})$ . These potentials can also be written in a covariant way, where the electromagnetic four-potential $A^{\mu }$ at $x^{\mu }=(ct,\mathbf {r} )$ is:

$A^{\mu }=\left.{\frac {qu^{\mu }}{R_{\nu }u^{\nu }}}\right|_{t_{r}}$

where $u^{\mu }=(\gamma ,\gamma \mathbf {v} /c)$ is the four-velocity of the particle with the Lorentz factor $\gamma =1/(1-v^{2}/c^{2})^{1/2}$ and $R^{\nu }=[c(t-t'),\mathbf {r} -\mathbf {r} ']$ which obeys $R_{\nu }R^{\nu }=0$ (the equation satisfied by the retarded time).

### Field computation

We can calculate the electric and magnetic fields directly from the potentials using the definitions:

$\mathbf {E} =-{\frac {1}{c}}{\dfrac {\partial \mathbf {A} }{\partial t}}-\nabla \varphi$ and $\mathbf {H} =\nabla \times \mathbf {A}$

The calculation is nontrivial and requires a number of steps. The electric and magnetic fields are (in non-covariant form):

$\mathbf {E} (\mathbf {r} ,t)=\left\{{\frac {q\left(\mathbf {R} -{\frac {1}{c}}R\mathbf {v} \right)}{\gamma ^{2}\left(R-{\frac {1}{c}}\mathbf {R} \cdot \mathbf {v} \right)^{3}}}+{\frac {q\mathbf {R} \times \left[\left(\mathbf {R} -{\frac {1}{c}}R\mathbf {v} \right)\times {\dot {\mathbf {v} }}\right]}{c^{2}\left(R-{\frac {1}{c}}\mathbf {R} \cdot \mathbf {v} \right)^{3}}}\right\}_{t_{r}}$

and

$\mathbf {H} (\mathbf {r} ,t)=\left\{{\frac {\mathbf {R} }{R}}\right\}_{t_{r}}\times \mathbf {E}$

where ${\textstyle {\dot {\mathbf {v} }}=\partial \mathbf {v} /\partial t}$ is the acceleration of the charge q . The magnetic field is orthogonal everywhere to the electric field.

The first term, depending on the charge velocity and not the acceleration, is linked to the Coulomb-like contribution. In other words, it represents the potentials for a uniformly moving charge. At large distances, indeed, this contribution to the field decreases like $1/R^{2}$ .

The second term, depending on the acceleration, is related to the electromagnetic radiation by the accelerating charge and its contribution to the field decreases like $1/R$ at large distances and therefore dominates the Coulomb-like contribution. If the particle acceleration ${\dot {\mathbf {v} }}$ and if this is zero, the charge does not radiate (emit electromagnetic radiation). This term requires additionally that a component of the charge acceleration be in a direction transverse to the line which connects the charge q and the observer of the field $\mathbf {E} (\mathbf {r} ,t)$ . The direction of the field associated with this radiative term is toward the fully time-retarded position of the charge (i.e. where the charge was when it was accelerated).

#### Static field

The $\mathbf {R} -{\frac {1}{c}}R\mathbf {v}$ part of the first term of the electric field updates the direction of the field toward the instantaneous position of the charge, if it continues to move with constant velocity $\mathbf {v}$ . This term is connected with the "static" part of the electromagnetic field of the charge. On the illustration, we observe an event that happened in the center of the sphere and that propagated at the speed of light. The problem is that when the speed of the particle is very close to the speed of light, the particle is then almost on the wave front which explains this strong electrostatic field on the front as we are now very close to the particle. Note that outside the propagation sphere, the electric field has its initial state (no connection with the event we observe). When the speed is very close to the speed of light, we consider that the electric field becomes almost flat in the transverse plane, a bit like a "pancake", with an opening angle on $1/\gamma$ .

## Derivation

The starting point is Maxwell's equations in the potential formulation using the Lorenz gauge:

$\nabla ^{2}\varphi -{1 \over c^{2}}{\partial ^{2}\varphi \over \partial t^{2}}=-4\pi \rho ,$ $\nabla ^{2}\mathbf {A} -{1 \over c^{2}}{\partial ^{2}\mathbf {A} \over \partial t^{2}}=-{\frac {4\pi }{c}}\mathbf {j} .$

Generally, the retarded solutions for the scalar and vector potentials (SI units) are $\varphi (\mathbf {r} ,t)=\int {\frac {\rho (\mathbf {r} ',t_{r})}{|\mathbf {r} -\mathbf {r} '|}}d^{3}\mathbf {r} '+\varphi _{0}(\mathbf {r} ,t)$ and $\mathbf {A} (\mathbf {r} ,t)={\frac {1}{c}}\int {\frac {\mathbf {j} (\mathbf {r} ',t_{r})}{|\mathbf {r} -\mathbf {r} '|}}d^{3}\mathbf {r} '+\mathbf {A} _{0}(\mathbf {r} ,t)$

where $\varphi _{0}(\mathbf {r} ,t)$ and $\mathbf {A} _{0}(\mathbf {r} ,t)$ satisfy the homogeneous wave equation with no sources and boundary conditions and they represent external field acting on the system. In the case that there are no boundaries surrounding the sources then $\varphi _{0}(\mathbf {r} ,t)=0$ and $\mathbf {A} _{0}(\mathbf {r} ,t)=0$ . Imposing the conditions and rewriting the integrals by introducing a time integration, as well, we get

$\varphi (\mathbf {r} ,t)=\int \int {\frac {\rho (\mathbf {r} ',t')}{|\mathbf {r} -\mathbf {r} '|}}\delta (t'-t_{r})dt'd^{3}\mathbf {r} '$ and $\mathbf {A} (\mathbf {r} ,t)={\frac {1}{c}}\int \int {\frac {\mathbf {j} (\mathbf {r} ',t')}{|\mathbf {r} -\mathbf {r} '|}}\delta (t'-t_{r})dt'd^{3}\mathbf {r} '.$

For a moving point charge, the charge and current densities are as follows:

$\rho (\mathbf {r} ',t')=q\delta (\mathbf {r'} -\mathbf {r} _{0}(t'))$ $\mathbf {j} (\mathbf {r} ',t')=q\mathbf {v} (t')\delta (\mathbf {r'} -\mathbf {r} _{0}(t')).$

Substituting into the expressions for the potential gives $\varphi (\mathbf {r} ,t)=\iint {\frac {q\delta (\mathbf {r'} -\mathbf {r} _{s}(t'))}{|\mathbf {r} -\mathbf {r} '|}}\delta (t'-t_{r})\,dt'\,d^{3}\mathbf {r} '$ $\mathbf {A} (\mathbf {r} ,t)={\frac {1}{c}}\iint {\frac {q\mathbf {v} (t')\delta (\mathbf {r'} -\mathbf {r} _{s}(t'))}{|\mathbf {r} -\mathbf {r} '|}}\delta (t'-t_{r})\,dt'\,d^{3}\mathbf {r} '$

Exchange the order of integration and carrying out the volume integral, we obtain $\varphi (\mathbf {r} ,t)=\int {\frac {q}{|\mathbf {r} -\mathbf {r} _{0}(t')|}}\delta \left(t'-t+{\frac {1}{c}}|\mathbf {r} -\mathbf {r} _{0}(t')|\right)dt'$ $\mathbf {A} (\mathbf {r} ,t)={\frac {1}{c}}\int {\frac {q\mathbf {v} (t')}{|\mathbf {r} -\mathbf {r} _{0}(t')|}}\delta \left(t'-t+{\frac {1}{c}}|\mathbf {r} -\mathbf {r} _{0}(t')|\right)\,dt'.$

These integrals can be evaluated using the identity

$\delta [F(t')]={\frac {\delta (t'-t_{r})}{F'(t_{r})}},\quad F(t_{r})=0$

where the last equation $F(t_{r})=0$ determines $t_{r}$ . In our case, $t_{r}$ is the retarded time. Performing the integration leads to the required Liénard–Wiechert potentials.

### Lorenz gauge, electric and magnetic fields

In order to calculate the derivatives of $\varphi$ and $\mathbf {A}$ it is convenient to first compute the derivatives of the retarded time. Taking the derivatives of both sides of its defining equation (remembering that $\mathbf {r_{s}} =\mathbf {r_{s}} (t_{r})$ ): $t_{r}+{\frac {1}{c}}|\mathbf {r} -\mathbf {r_{s}} |=t$ Differentiating with respect to t, ${\frac {dt_{r}}{dt}}+{\frac {1}{c}}{\frac {dt_{r}}{dt}}{\frac {d|\mathbf {r} -\mathbf {r_{s}} |}{dt_{r}}}=1$

${\frac {dt_{r}}{dt}}\left(1-{\frac {\mathbf {v} \cdot \mathbf {R} }{Rc}}\right)=1$

${\frac {dt_{r}}{dt}}={\frac {1}{\left(1-{\frac {\mathbf {v} \cdot \mathbf {R} }{Rc}}\right)}}$

Similarly, taking the gradient with respect to $\mathbf {r}$ and using the multivariable chain rule gives

${\boldsymbol {\nabla }}t_{r}+{\frac {1}{c}}{\boldsymbol {\nabla }}|\mathbf {r} -\mathbf {r_{s}} |=0$

${\boldsymbol {\nabla }}t_{r}+{\frac {1}{c}}\left({\boldsymbol {\nabla }}t_{r}{\frac {d|\mathbf {r} -\mathbf {r_{s}} |}{dt_{r}}}+{\frac {\mathbf {R} }{R}}\right)=0$

${\boldsymbol {\nabla }}t_{r}=-{\frac {\mathbf {R} }{c\left(R-{\frac {1}{c}}\mathbf {R} \cdot \mathbf {v} \right)}}$

It follows that

${\frac {d|\mathbf {r} -\mathbf {r_{s}} |}{dt}}={\frac {dt_{r}}{dt}}{\frac {d|\mathbf {r} -\mathbf {r_{s}} |}{dt_{r}}}={\frac {-\mathbf {R} \cdot \mathbf {v} }{\left(R-{\frac {1}{c}}\mathbf {R} \cdot \mathbf {v} \right)}}$

${\boldsymbol {\nabla }}|\mathbf {r} -\mathbf {r_{s}} |={\boldsymbol {\nabla }}t_{r}{\frac {d|\mathbf {r} -\mathbf {r_{s}} |}{dt_{r}}}+{\frac {\mathbf {R} }{R}}={\frac {\mathbf {R} }{\left(R-{\frac {1}{c}}\mathbf {R} \cdot \mathbf {v} \right)}}.$

These can be used in calculating the derivatives of the vector potential and the resulting expressions are

${\begin{aligned}{\frac {d\varphi }{dt}}=&-{\frac {q}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{2}}}{\frac {d}{dt}}\left[(|\mathbf {r} -\mathbf {r_{s}} |(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})\right]\\=&-{\frac {q}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{2}}}{\frac {d}{dt}}\left[|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}\right]\\=&-{\frac {qc}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\left[-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}+{\beta _{s}}^{2}-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right]\end{aligned}}$

${\begin{aligned}{\boldsymbol {\nabla }}\cdot \mathbf {A} =&-{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{2}}}{\big (}{\boldsymbol {\nabla }}\left[\left(|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}\right)\right]\cdot {\boldsymbol {\beta }}_{s}-\left[\left(|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}\right)\right]{\boldsymbol {\nabla }}\cdot {\boldsymbol {\beta }}_{s}{\big )}\\=&-{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\cdot \\&\left[(\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})-{\beta }_{s}^{2}(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})-{\beta }_{s}^{2}\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}+\left((\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right)(\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})+{\big (}|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}{\big )}(\mathbf {n} _{s}\cdot {\dot {\boldsymbol {\beta }}}_{s}/c)\right]\\=&{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\left[\beta _{s}^{2}-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right]\end{aligned}}$

These show that the Lorenz gauge is satisfied, namely that ${\textstyle {\frac {d\varphi }{dt}}+c^{2}{\boldsymbol {\nabla }}\cdot \mathbf {A} =0}$ .

Similarly one calculates:

${\boldsymbol {\nabla }}\varphi =-{\frac {q}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\left[\mathbf {n} _{s}\left(1-{\beta _{s}}^{2}+(\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right)-{\boldsymbol {\beta }}_{s}(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})\right]$

${\frac {d\mathbf {A} }{dt}}={\frac {q}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\left[{\boldsymbol {\beta }}_{s}\left(\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}-{\beta _{s}}^{2}+(\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right)+|\mathbf {r} -\mathbf {r_{s}} |{\dot {\boldsymbol {\beta }}}_{s}(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})/c\right]$

By noting that for any vectors $\mathbf {u}$ , $\mathbf {v}$ , $\mathbf {w}$ : $\mathbf {u} \times (\mathbf {v} \times \mathbf {w} )=(\mathbf {u} \cdot \mathbf {w} )\mathbf {v} -(\mathbf {u} \cdot \mathbf {v} )\mathbf {w}$ The expression for the electric field mentioned above becomes ${\begin{aligned}\mathbf {E} (\mathbf {r} ,t)=&{\frac {q}{4\pi \epsilon _{0}}}{\frac {1}{|\mathbf {r} -\mathbf {r} _{s}|^{2}(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})^{3}}}\cdot \\&\left[\left(\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}\right)(1-{\beta _{s}}^{2})+|\mathbf {r} -\mathbf {r} _{s}|(\mathbf {n} _{s}\cdot {\dot {\boldsymbol {\beta }}}_{s}/c)(\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s})-|\mathbf {r} -\mathbf {r} _{s}|{\big (}\mathbf {n} _{s}\cdot (\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}){\big )}{\dot {\boldsymbol {\beta }}}_{s}/c\right]\end{aligned}}$ which is easily seen to be equal to $-{\boldsymbol {\nabla }}\varphi -{\frac {d\mathbf {A} }{dt}}$

Similarly ${\boldsymbol {\nabla }}\times \mathbf {A}$ gives the expression of the magnetic field mentioned above: ${\begin{aligned}{\mathbf {B} }=&{\boldsymbol {\nabla }}\times \mathbf {A} \\[1ex]=&-{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{2}}}{\big (}{\boldsymbol {\nabla }}\left[\left(|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}\right)\right]\times {\boldsymbol {\beta }}_{s}-\left[\left(|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}\right)\right]{\boldsymbol {\nabla }}\times {\boldsymbol {\beta }}_{s}{\big )}\\=&-{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r_{s}} |^{2}\left(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s}\right)^{3}}}\cdot \\&\qquad \left[(\mathbf {n} _{s}\times {\boldsymbol {\beta }}_{s})-({\boldsymbol {\beta }}_{s}\times {\boldsymbol {\beta }}_{s})(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})-{\beta }_{s}^{2}\mathbf {n} _{s}\times {\boldsymbol {\beta }}_{s}+\left((\mathbf {r} -\mathbf {r_{s}} )\cdot {\dot {\boldsymbol {\beta }}}_{s}/c\right)(\mathbf {n} _{s}\times {\boldsymbol {\beta }}_{s})+{\big (}|\mathbf {r} -\mathbf {r_{s}} |-(\mathbf {r} -\mathbf {r_{s}} )\cdot {\boldsymbol {\beta }}_{s}{\big )}(\mathbf {n} _{s}\times {\dot {\boldsymbol {\beta }}}_{s}/c)\right]\\=&-{\frac {q}{4\pi \epsilon _{0}c}}{\frac {1}{|\mathbf {r} -\mathbf {r} _{s}|^{2}(1-\mathbf {n} _{s}\cdot {\boldsymbol {\beta }}_{s})^{3}}}\cdot \\&\qquad \left[\left(\mathbf {n} _{s}\times {\boldsymbol {\beta }}_{s}\right)(1-{\beta _{s}}^{2})+|\mathbf {r} -\mathbf {r} _{s}|(\mathbf {n} _{s}\cdot {\dot {\boldsymbol {\beta }}}_{s}/c)(\mathbf {n} _{s}\times {\boldsymbol {\beta }}_{s})+|\mathbf {r} -\mathbf {r} _{s}|{\big (}\mathbf {n} _{s}\cdot (\mathbf {n} _{s}-{\boldsymbol {\beta }}_{s}){\big )}\mathbf {n} _{s}\times {\dot {\boldsymbol {\beta }}}_{s}/c\right]\\[1ex]=&{\frac {\mathbf {n} _{s}}{c}}\times \mathbf {E} \end{aligned}}$ The source terms $\mathbf {r} _{s}$ , $\mathbf {n} _{s}$ , and $\mathbf {\beta } _{s}$ are to be evaluated at the retarded time.

## Implications

The study of classical electrodynamics was instrumental in Albert Einstein's development of the theory of relativity. Analysis of the motion and propagation of electromagnetic waves led to the special relativity description of space and time. The Liénard–Wiechert formulation is an important launchpad into a deeper analysis of relativistic moving particles.

The Liénard–Wiechert description is accurate for a large, independently moving particle (i.e. the treatment is "classical" and the acceleration of the charge is due to a force independent of the electromagnetic field). The Liénard–Wiechert formulation always provides two sets of solutions: Advanced fields are absorbed by the charges and retarded fields are emitted. Schwarzschild and Fokker considered the advanced field of a system of moving charges, and the retarded field of a system of charges having the same geometry and opposite charges. Linearity of Maxwell's equations in vacuum allows one to add both systems, so that the charges disappear: This trick allows Maxwell's equations to become linear in matter. Multiplying electric parameters of both problems by arbitrary real constants produces a coherent interaction of light with matter which generalizes Einstein's theory which is now considered as founding theory of lasers: it is not necessary to study a large set of identical molecules to get coherent amplification in the mode obtained by arbitrary multiplications of advanced and retarded fields. To compute energy, it is necessary to use the absolute fields which include the zero point field; otherwise, an error appears, for instance in photon counting.

It is important to take into account the zero point field discovered by Planck. It replaces Einstein's "A" coefficient and explains that the classical electron is stable on Rydberg's classical orbits. Moreover, introducing the fluctuations of the zero point field produces Willis E. Lamb's correction of levels of H atom.

Quantum electrodynamics helped bring together the radiative behavior with the quantum constraints. It introduces quantization of normal modes of the electromagnetic field in assumed perfect optical resonators.

## Universal speed limit

The force on a particle at a given location ***r*** and time *t* depends in a complicated way on the position of the source particles at an earlier time *t*r due to the finite speed, c, at which electromagnetic information travels. A particle on Earth 'sees' a charged particle accelerate on the Moon as this acceleration happened 1.5 seconds ago, and a charged particle's acceleration on the Sun as happened 500 seconds ago. This earlier time in which an event happens such that a particle at location ***r*** 'sees' this event at a later time *t* is called the retarded time, *tr*. The retarded time varies with position; for example the retarded time at the Moon is 1.5 seconds before the current time and the retarded time on the Sun is 500 s before the current time on the Earth. The retarded time *tr*=*tr*(***r***,*t*) is defined implicitly by

$t_{r}=t-{\frac {R(t_{r})}{c}}$

where $R(t_{r})$ is the distance of the particle from the source at the retarded time. Only electromagnetic wave effects depend fully on the retarded time.

A novel feature in the Liénard–Wiechert potential is seen in the breakup of its terms into two types of field terms (see below), only one of which depends fully on the retarded time. The first of these is the static electric (or magnetic) field term that depends only on the distance to the moving charge, and does not depend on the retarded time at all, if the velocity of the source is constant. The other term is dynamic, in that it requires that the moving charge be *accelerating* with a component perpendicular to the line connecting the charge and the observer and does not appear unless the source changes velocity. This second term is connected with electromagnetic radiation.

The first term describes near field effects from the charge, and its direction in space is updated with a term that corrects for any constant-velocity motion of the charge on its distant static field, so that the distant static field appears at distance from the charge, with **no** aberration of light or light-time correction. This term, which corrects for time-retardation delays in the direction of the static field, is required by Lorentz invariance. A charge moving with a constant velocity must appear to a distant observer in exactly the same way as a static charge appears to a moving observer, and in the latter case, the direction of the static field must change instantaneously, with no time-delay. Thus, static fields (the first term) point exactly at the true instantaneous (non-retarded) position of the charged object if its velocity has not changed over the retarded time delay. This is true over any distance separating objects.

The second term, however, which contains information about the acceleration and other unique behavior of the charge that cannot be removed by changing the Lorentz frame (inertial reference frame of the observer), is fully dependent for direction on the time-retarded position of the source. Thus, electromagnetic radiation (described by the second term) always appears to come from the direction of the position of the emitting charge **at the retarded time**. Only this second term describes information transfer about the behavior of the charge, which transfer occurs (radiates from the charge) at the speed of light. At "far" distances (longer than several wavelengths of radiation), the 1/R dependence of this term makes electromagnetic field effects (the value of this field term) more powerful than "static" field effects, which are described by the 1/R2 field of the first (static) term and thus decay more rapidly with distance from the charge.

### Existence and uniqueness of the retarded time

#### Existence

The retarded time is not guaranteed to exist in general. For example, if, in a given frame of reference, an electron has just been created, then at this very moment another electron does not yet feel its electromagnetic force at all. However, under certain conditions, there always exists a retarded time. For example, if the source charge has existed for an unlimited amount of time, during which it has always travelled at a speed not exceeding $v_{M}<c$ , then there exists a valid retarded time $t_{r}$ . This can be seen by considering the function $f(t')=|\mathbf {r} -\mathbf {r} _{s}(t')|-c(t-t')$ . At the present time $t'=t$ ; $f(t')=|\mathbf {r} -\mathbf {r} _{s}(t')|-c(t-t')=|\mathbf {r} -\mathbf {r} _{s}(t')|\geq 0$ . The derivative $f'(t')$ is given by

$f'(t')={\frac {\mathbf {r} -\mathbf {r} _{s}(t_{r})}{|\mathbf {r} -\mathbf {r} _{s}(t_{r})|}}\cdot (-\mathbf {v} _{s}(t'))+c\geq c-\left|{\frac {\mathbf {r} -\mathbf {r} _{s}(t_{r})}{|\mathbf {r} -\mathbf {r} _{s}(t_{r})|}}\right|\,|\mathbf {v} _{s}(t')|=c-|\mathbf {v} _{s}(t')|\geq c-v_{M}>0$

By the mean value theorem, $f(t-\Delta t)\leq f(t)-f'(t)\Delta t\leq f(t)-(c-v_{M})\Delta t$ . By making $\Delta t$ sufficiently large, this can become negative, *i.e.*, at some point in the past, $f(t')<0$ . By the intermediate value theorem, there exists an intermediate $t_{r}$ with $f(t_{r})=0$ , the defining equation of the retarded time. Intuitively, as the source charge moves back in time, the cross section of its light cone at present time expands faster than it can recede, so eventually it must reach the point $\mathbf {r}$ . This is not necessarily true if the source charge's speed is allowed to be arbitrarily close to c , *i.e.*, if for any given speed $v<c$ there was some time in the past when the charge was moving at this speed. In this case the cross section of the light cone at present time approaches the point $\mathbf {r}$ as the observer travels back in time but does not necessarily ever reach it.

#### Uniqueness

For a given point $(\mathbf {r} ,t)$ and trajectory of the point source $\mathbf {r} _{s}(t')$ , there is at most one value of the retarded time $t_{r}$ , *i.e.*, one value $t_{r}$ such that $|\mathbf {r} -\mathbf {r} _{s}(t_{r})|=c(t-t_{r})$ . This can be realized by assuming that there are two retarded times $t_{1}$ and $t_{2}$ , with $t_{1}\leq t_{2}$ . Then, $|\mathbf {r} -\mathbf {r} _{s}(t_{1})|=c(t-t_{1})$ and $|\mathbf {r} -\mathbf {r} _{s}(t_{2})|=c(t-t_{2})$ . Subtracting gives $c(t_{2}-t_{1})=|\mathbf {r} -\mathbf {r} _{s}(t_{1})|-|\mathbf {r} -\mathbf {r} _{s}(t_{2})|\leq |\mathbf {r} _{s}(t_{2})-\mathbf {r} _{s}(t_{1})|$ by the triangle inequality. Unless $t_{2}=t_{1}$ , this then implies that the average velocity of the charge between $t_{1}$ and $t_{2}$ is $|\mathbf {r} _{s}(t_{2})-\mathbf {r} _{s}(t_{1})|/(t_{2}-t_{1})\geq c$ , which is impossible. The intuitive interpretation is that one can only ever "see" the point source at one location/time at once unless it travels at least at the speed of light to another location. As the source moves forward in time, the cross section of its light cone at present time contracts faster than the source can approach, so it can never intersect the point $\mathbf {r}$ again.

The conclusion is that, under certain conditions, the retarded time exists and is unique.

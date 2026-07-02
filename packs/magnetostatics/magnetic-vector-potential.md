---
title: "Magnetic vector potential"
source: https://en.wikipedia.org/wiki/Magnetic_vector_potential
domain: magnetostatics
license: CC-BY-SA-4.0
tags: magnetostatic field, biot-savart law, magnetic dipole, magnetic vector potential
fetched: 2026-07-02
---

# Magnetic vector potential

In classical electromagnetism, **magnetic vector potential** (often denoted **A**) is the vector quantity defined so that its curl is equal to the magnetic field, **B**: ${\textstyle \nabla \times \mathbf {A} =\mathbf {B} }$ . Together with the electric potential *φ*, the magnetic vector potential can be used to specify the electric field **E** as well. Therefore, many equations of electromagnetism can be written either in terms of the fields **E** and **B**, or equivalently in terms of the potentials *φ* and **A**. In more advanced theories such as quantum mechanics, most equations use potentials rather than fields.

Magnetic vector potential was independently introduced by Franz Ernst Neumann and Wilhelm Eduard Weber in 1845 and in 1846, respectively to discuss Ampère's circuital law. William Thomson also introduced the modern version of the vector potential in 1847, along with the formula relating it to the magnetic field.

## Unit conventions

This article uses the SI system.

In the SI system, the units of **A** are V·s·m−1 or Wb·m−1 and are the same as that of momentum per unit charge, or force per unit current.

## Definition

The magnetic vector potential, $\mathbf {A}$ , is a vector field, and the electric potential, $\phi$ , is a scalar field such that: $\mathbf {B} =\nabla \times \mathbf {A} \ ,\quad \mathbf {E} =-\nabla \phi -{\frac {\partial \mathbf {A} }{\partial t}},$ where $\mathbf {B}$ is the magnetic field and $\mathbf {E}$ is the electric field. In magnetostatics where there is no time-varying current or charge distribution, only the first equation is needed. (In the context of electrodynamics, the terms *vector potential* and *scalar potential* are used for *magnetic vector potential* and *electric potential*, respectively. In mathematics, vector potential and scalar potential can be generalized to higher dimensions.)

If electric and magnetic fields are defined as above from potentials, they automatically satisfy two of Maxwell's equations: Gauss's law for magnetism and Faraday's law. For example, if $\mathbf {A}$ is continuous and well-defined everywhere, then it is guaranteed not to result in magnetic monopoles. (In the mathematical theory of magnetic monopoles, $\mathbf {A}$ is allowed to be either undefined or multiple-valued in some places; see magnetic monopole for details).

Starting with the above definitions and remembering that the divergence of the curl is zero and the curl of the gradient is the zero vector: ${\begin{aligned}\nabla \cdot \mathbf {B} &=\nabla \cdot \left(\nabla \times \mathbf {A} \right)=0\ ,\\\nabla \times \mathbf {E} &=\nabla \times \left(-\nabla \phi -{\frac {\partial \mathbf {A} }{\partial t}}\right)=-{\frac {\partial }{\partial t}}\left(\nabla \times \mathbf {A} \right)=-{\frac {\partial \mathbf {B} }{\partial t}}~.\end{aligned}}$

Alternatively, the existence of $\mathbf {A}$ and $\phi$ is guaranteed from these two laws using Helmholtz's theorem. For example, since the magnetic field is divergence-free (Gauss's law for magnetism; i.e., $\nabla \cdot \mathbf {B} =0$ ), $\mathbf {A}$ always exists that satisfies the above definition.

The vector potential $\mathbf {A}$ is used when studying the Lagrangian in classical mechanics and in quantum mechanics (see Schrödinger equation for charged particles, Dirac equation, Aharonov–Bohm effect).

In minimal coupling, $q\mathbf {A}$ is called the potential momentum, and is part of the canonical momentum.

The line integral of $\mathbf {A}$ over a closed loop, $\Gamma$ , is equal to the magnetic flux, $\Phi _{\mathbf {B} }$ , through a surface, S , that it encloses: $\oint _{\Gamma }\mathbf {A} \,\cdot \ d{\mathbf {\Gamma } }=\iint _{S}\nabla \times \mathbf {A} \ \cdot \ d\mathbf {S} =\Phi _{\mathbf {B} }~.$

Therefore, the units of $\mathbf {A}$ are also equivalent to weber per metre. The above equation is useful in the flux quantization of superconducting loops.

In the Coulomb gauge $\nabla \cdot \mathbf {A} =0$ , there is a formal analogy between the relationship between the vector potential and the magnetic field to Ampere's law $\nabla \times \mathbf {B} =\mu _{0}\mathbf {J}$ . Thus, when finding the vector potential of a given magnetic field, one can use the same methods one uses when finding the magnetic field given a current distribution.

Although the magnetic field, $\mathbf {B}$ , is a pseudovector (also called axial vector), the vector potential, $\mathbf {A}$ , is a polar vector. This means that if the right-hand rule for cross products were replaced with a left-hand rule, but without changing any other equations or definitions, then $\mathbf {B}$ would switch signs, but **A** would not change. This is an example of a general theorem: The curl of a polar vector is a pseudovector, and vice versa.

## Magnetostatics in the Coulomb gauge

In magnetostatics, if the Coulomb gauge $\ \nabla \cdot \mathbf {A} =0$ is imposed, then there is an analogy between $\mathbf {A} ,\mathbf {J}$ and $V,\rho$ in electrostatics: $\nabla ^{2}\mathbf {A} =-\mu _{0}\mathbf {J}$ just like the electrostatic equation $\nabla ^{2}V=-{\frac {\rho }{\epsilon _{0}}}$

Likewise one can integrate to obtain the potentials: $\mathbf {A} (\mathbf {r} )={\frac {\mu _{0}}{4\pi }}\int _{R}{\frac {\mathbf {J} (\mathbf {r} ')}{\left|\mathbf {r} -\mathbf {r} '\right|}}\mathrm {d} ^{3}r'$ just like the equation for the electric potential: $V(\mathbf {r} )={\frac {1}{4\pi \varepsilon _{0}}}\int _{R}{\frac {\rho (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\mathrm {d} ^{3}r'$

## Interpretation as potential momentum

By equating Newton's second law with the Lorentz force law we can obtain $m{\frac {\mathrm {d} v}{\mathrm {d} t}}=q\left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right).$ Dotting this with the velocity yields ${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {1}{2}}mv^{2}\right)=q\mathbf {v} \cdot \left(\mathbf {E} +\mathbf {v} \times \mathbf {B} \right).$ With the dot product of the cross product being zero, substituting $\mathbf {E} =-\nabla \phi -{\frac {\partial \mathbf {A} }{\partial t}},$ and the convective derivative of $\phi$ in the above equation then gives ${\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {1}{2}}mv^{2}+q\phi \right)={\frac {\partial }{\partial t}}q\left(\phi -\mathbf {v} \cdot \mathbf {A} \right)$ which tells us the time derivative of the "generalized energy" ${\frac {1}{2}}mv^{2}+q\phi$ in terms of a velocity dependent potential $q\left(\phi -\mathbf {v} \cdot \mathbf {A} \right)$ , and ${\frac {\mathrm {d} }{\mathrm {d} t}}\left(mv+q\mathbf {A} \right)=-\nabla q\left(\phi -\mathbf {v} \cdot \mathbf {A} \right)$ which gives the time derivative of the generalized momentum $m\mathbf {v} +q\mathbf {A}$ in terms of the (minus) gradient of the same velocity dependent potential.

Thus, when the (partial) time derivative of the velocity dependent potential $q(\phi -\mathbf {v} \cdot \mathbf {A} )$ is zero, the generalized energy is conserved, and likewise when the gradient is zero, the generalized momentum is conserved. As a special case, if the potentials are time or space symmetric, then the generalized energy or momentum respectively will be conserved. Likewise the fields contribute $q\mathbf {r} \times \mathbf {A}$ to the generalized angular momentum, and rotational symmetries will provide conservation laws for the components.

Relativistically, we have the single equation ${\frac {\mathrm {d} }{\mathrm {d} \tau }}\left(p^{\mu }+qA^{\mu }\right)=\partial _{\mu }\left(U^{\nu }\cdot A^{\nu }\right)$ where

- $\tau$ is the proper time,
- $p^{\mu }$ is the four momentum $(E/c,\gamma m\mathbf {v} )$
- $U^{\nu }$ is the four velocity $\gamma (c,\mathbf {v} )$
- $A^{\nu }$ is the four potential $(\phi /c,\mathbf {A} )$
- $\partial _{\mu }$ is the four gradient $({\frac {\partial }{\partial \left(ct\right)}},-\nabla )$

### Analytical mechanics of a charged particle

In a field with electric potential $\ \phi \$ and magnetic potential $\ \mathbf {A}$ , the Lagrangian ( $\ {\mathcal {L}}\$ ) and the Hamiltonian ( $\ {\mathcal {H}}\$ ) of a particle with mass $\ m\$ and charge $\ q\$ are ${\begin{aligned}{\mathcal {L}}&={\frac {1}{2}}m\ \mathbf {v} ^{2}+q\ \mathbf {v} \cdot \mathbf {A} -q\ \phi \ ,\\{\mathcal {H}}&={\frac {1}{2m}}\left(\mathbf {p} -q\mathbf {A} \right)^{2}+q\ \phi ~.\end{aligned}}$

The generalized momentum $\mathbf {p}$ is ${\frac {\partial {\mathcal {L}}}{\partial v}}=m\mathbf {v} +q\mathbf {A}$ . The generalized force is $\nabla {\mathcal {L}}=-q\nabla \left(\phi -\mathbf {v} \cdot \mathbf {A} \right)$ . These are exactly the quantities from the previous section. In this framework, the conservation laws come from Noether's theorem.

### Example: Solenoid

Consider a charged particle of charge q located distance r outside a solenoid oriented on the z that is suddenly turned off. By Faraday's law of induction, an electric field will be induced that will impart an impulse to the particle equal to $q\Phi _{0}/2\pi r{\hat {\phi }}$ where $\Phi _{0}$ is the initial magnetic flux through a cross section of the solenoid.

We can analyze this problem from the perspective of generalized momentum conservation. Using the analogy to Ampere's law, the magnetic vector potential is $\mathbf {A} (r)=\Phi _{0}/2\pi r{\hat {\phi }}$ . Since $\mathbf {p} +q\mathbf {A}$ is conserved, after the solenoid is turned off the particle will have momentum equal to $q\mathbf {A} =q\Phi _{0}/2\pi r{\hat {\phi }}$

Additionally, because of the symmetry, the z component of the generalized angular momentum is conserved. By looking at the Poynting vector of the configuration, one can deduce that the fields have nonzero total angular momentum pointing along the solenoid. This is the angular momentum transferred to the fields.

## Gauge choices

The above definition does not define the magnetic vector potential uniquely because, by definition, we can arbitrarily add curl-free components to the magnetic potential without changing the observed magnetic field. Thus, there is a degree of freedom available when choosing $\mathbf {A}$ . This condition is known as gauge invariance.

Two common gauge choices are

- The Lorenz gauge: $\ \nabla \cdot \mathbf {A} +{\frac {1}{\ c^{2}}}{\frac {\partial \phi }{\partial t}}=0$
- The Coulomb gauge: $\ \nabla \cdot \mathbf {A} =0$

### Lorenz gauge

In other gauges, the formulas for $\mathbf {A}$ and $\phi$ are different; for example, see *Coulomb gauge* for another possibility.

#### Time domain

Using the above definition of the potentials and applying it to the other two Maxwell's equations (the ones that are not automatically satisfied) results in a complicated differential equation that can be simplified using the Lorenz gauge where $\mathbf {A}$ is chosen to satisfy: $\nabla \cdot \mathbf {A} +{\frac {1}{\ c^{2}}}{\frac {\partial \phi }{\partial t}}=0$

Using the Lorenz gauge, the electromagnetic wave equations can be written compactly in terms of the potentials,

- Wave equation of the scalar potential $\nabla ^{2}\phi -{\frac {1}{c^{2}}}{\frac {\partial ^{2}\phi }{\partial t^{2}}}=-{\frac {\rho }{\epsilon _{0}}}$
- Wave equation of the vector potential $\nabla ^{2}\mathbf {A} -{\frac {1}{c^{2}}}{\frac {\partial ^{2}\mathbf {A} }{\partial t^{2}}}=-\mu _{0}\mathbf {J}$

The solutions of Maxwell's equations in the Lorenz gauge (see Feynman and Jackson) with the boundary condition that both potentials go to zero sufficiently fast as they approach infinity are called the retarded potentials, which are the magnetic vector potential $\mathbf {A} (\mathbf {r} ,t)$ and the electric scalar potential $\phi (\mathbf {r} ,t)$ due to a current distribution of current density $\mathbf {J} (\mathbf {r} ,t)$ , charge density $\rho (\mathbf {r} ,t)$ , and volume $\Omega$ , within which $\rho$ and $\mathbf {J}$ are non-zero at least sometimes and some places):

- Solutions ${\begin{aligned}\mathbf {A} \!\left(\mathbf {r} ,t\right)&={\frac {\mu _{0}}{\ 4\pi \ }}\int _{\Omega }{\frac {\mathbf {J} {\left(\mathbf {r} ',t'\right)}}{R}}\ d^{3}\mathbf {r} '\\\phi \!\left(\mathbf {r} ,t\right)&={\frac {1}{4\pi \epsilon _{0}}}\int _{\Omega }{\frac {\rho {\left(\mathbf {r} ',t'\right)}}{R}}\ d^{3}\mathbf {r} '\end{aligned}}$

where the fields at position vector $\mathbf {r}$ and time t are calculated from sources at distant position $\mathbf {r} '$ at an earlier time $t'.$ The location $\mathbf {r} '$ is a source point in the charge or current distribution (also the integration variable, within volume $\Omega$ ). The earlier time $t'$ is called the *retarded time*, and calculated as $t'=t-{\frac {\ R\ }{c}}~.$ where $R={\bigl \|}\mathbf {r} -\mathbf {r} '{\bigr \|}~.$

With these equations:

- The Lorenz gauge condition is satisfied: $\ \nabla \cdot \mathbf {A} +{\frac {1}{\ c^{2}}}{\frac {\partial \phi }{\partial t}}=0~.$
- The position of $\mathbf {r}$ , the point at which values for $\phi$ and $\mathbf {A}$ are found, only enters the equation as part of the scalar distance from $\mathbf {r} '$ to $\mathbf {r} .$ The direction from $\mathbf {r} '$ to $\mathbf {r}$ does not enter into the equation. The only thing that matters about a source point is how far away it is.
- The integrand uses *retarded time*, $t'.$ This reflects the fact that changes in the sources propagate at the speed of light. Hence the charge and current densities affecting the electric and magnetic potential at $\mathbf {r}$ and t , from remote location $\mathbf {r} '$ must also be at some prior time $t'.$
- The equation for $\mathbf {A}$ is a vector equation. In Cartesian coordinates, the equation separates into three scalar equations: ${\begin{aligned}A_{x}{\left(\mathbf {r} ,t\right)}&={\frac {\mu _{0}}{\ 4\pi \ }}\int _{\Omega }{\frac {J_{x}{\left(\mathbf {r} ',t'\right)}}{R}}\,d^{3}\mathbf {r} '\ ,\\A_{y}{\left(\mathbf {r} ,t\right)}&={\frac {\mu _{0}}{\ 4\pi \ }}\int _{\Omega }{\frac {J_{y}{\left(\mathbf {r} ',t'\right)}}{R}}\,d^{3}\mathbf {r} '\ ,\\A_{z}{\left(\mathbf {r} ,t\right)}&={\frac {\mu _{0}}{\ 4\pi \ }}\int _{\Omega }{\frac {J_{z}{\left(\mathbf {r} ',t'\right)}}{R}}\,d^{3}\mathbf {r} '~.\end{aligned}}$ In this form it is apparent that the component of $\mathbf {A}$ in a given direction depends only on the components of $\mathbf {J}$ that are in the same direction. If the current is carried in a straight wire, $\mathbf {A}$ points in the same direction as the wire.

#### Frequency domain

The preceding time domain equations can be expressed in the frequency domain.

- Lorenz gauge $\nabla \cdot \mathbf {A} +{\frac {j\omega }{c^{2}}}\phi =0$ or $\phi ={\frac {j\omega }{k^{2}}}\nabla \cdot \mathbf {A}$
- Solutions ${\begin{aligned}\mathbf {A} \!\left(\mathbf {r} ,\omega \right)&={\frac {\mu _{0}}{\ 4\pi \ }}\int _{\Omega }{\frac {\mathbf {J} {\left(\mathbf {r} ',\omega \right)}}{R}}\ e^{-jkR}d^{3}\mathbf {r} '\\\phi \!\left(\mathbf {r} ,\omega \right)&={\frac {1}{4\pi \epsilon _{0}}}\int _{\Omega }{\frac {\rho {\left(\mathbf {r} ',\omega \right)}}{R}}\ e^{-jkR}d^{3}\mathbf {r} '\end{aligned}}$
- Wave equations ${\begin{aligned}\nabla ^{2}\phi +k^{2}\phi &=-{\frac {\rho }{\epsilon _{0}}}\\\nabla ^{2}\mathbf {A} +k^{2}\mathbf {A} &=-\mu _{0}\mathbf {J} .\end{aligned}}$
- Electromagnetic field equations ${\begin{aligned}\mathbf {B} &=\nabla \times \mathbf {A} \\\mathbf {E} &=-\nabla \phi -j\omega \mathbf {A} =-j\omega \mathbf {A} -j{\frac {\omega }{k^{2}}}\nabla (\nabla \cdot \mathbf {A} )\end{aligned}}$

where

- $\phi$ and $\rho$ are scalar phasors.
- $\mathbf {A}$ , $\mathbf {B}$ , $\mathbf {E}$ , and $\mathbf {J}$ are vector phasors.
- $k={\frac {\omega }{c}}$

There are a few notable things about $\mathbf {A}$ and $\phi$ calculated in this way:

- The Lorenz gauge condition is satisfied: $\textstyle \phi =-{\frac {c^{2}}{j\omega }}\nabla \cdot \mathbf {A} .$ This implies that the frequency domain electric potential, $\phi$ , can be computed entirely from the current density distribution, $\mathbf {J}$ .
- The position of $\mathbf {r} ,$ the point at which values for $\phi$ and $\mathbf {A}$ are found, only enters the equation as part of the scalar distance from $\mathbf {r} '$ to $\ \mathbf {r} .$ The direction from $\mathbf {r} '$ to $\mathbf {r}$ does not enter into the equation. The only thing that matters about a source point is how far away it is.
- The integrand uses the phase shift term $e^{-jkR}$ which plays a role equivalent to *retarded time*. This reflects the fact that changes in the sources propagate at the speed of light; propagation delay in the time domain is equivalent to a phase shift in the frequency domain.
- The equation for $\mathbf {A}$ is a vector equation. In Cartesian coordinates, the equation separates into three scalar equations: ${\begin{aligned}\mathbf {A} _{x}\!\left(\mathbf {r} ,\omega \right)&={\frac {\mu _{0}}{4\pi }}\int _{\Omega }{\frac {\mathbf {J} _{x}{\left(\mathbf {r} ',\omega \right)}}{R}}\,e^{-jkR}\,d^{3}\mathbf {r} ',\\\mathbf {A} _{y}\!\left(\mathbf {r} ,\omega \right)&={\frac {\mu _{0}}{4\pi }}\int _{\Omega }{\frac {\mathbf {J} _{y}{\left(\mathbf {r} ',\omega \right)}}{R}}\,e^{-jkR}\,d^{3}\mathbf {r} ',\\\mathbf {A} _{z}\!\left(\mathbf {r} ,\omega \right)&={\frac {\mu _{0}}{4\pi }}\int _{\Omega }{\frac {\mathbf {J} _{z}{\left(\mathbf {r} ',\omega \right)}}{R}}\,e^{-jkR}\,d^{3}\mathbf {r} '\end{aligned}}$ In this form it is apparent that the component of $\mathbf {A}$ in a given direction depends only on the components of $\ \mathbf {J} \$ that are in the same direction. If the current is carried in a straight wire, $\mathbf {A}$ points in the same direction as the wire.

## Depiction of the A-field

See Feynman for the depiction of the $\mathbf {A}$ field around a long thin solenoid.

Since $\nabla \times \mathbf {B} =\mu _{0}\ \mathbf {J}$ assuming quasi-static conditions, i.e.

${\frac {\ \partial \mathbf {E} \ }{\partial t}}\to 0\$

and

$\ \nabla \times \mathbf {A} =\mathbf {B}$

,

the lines and contours of $\ \mathbf {A} \$ relate to $\ \mathbf {B} \$ like the lines and contours of $\mathbf {B}$ relate to $\ \mathbf {J} .$ Thus, a depiction of the $\mathbf {A}$ field around a loop of $\mathbf {B}$ flux (as would be produced in a toroidal inductor) is qualitatively the same as the $\mathbf {B}$ field around a loop of current.

The figure to the right is an artist's depiction of the $\mathbf {A}$ field. The thicker lines indicate paths of higher average intensity (shorter paths have higher intensity so that the path integral is the same). The lines are drawn to (aesthetically) impart the general look of the $\mathbf {A}$ field.

The drawing tacitly assumes $\nabla \cdot \mathbf {A} =0$ , true under any one of the following assumptions:

- the Coulomb gauge is assumed
- the Lorenz gauge is assumed and there is no distribution of charge, $\rho =0$
- the Lorenz gauge is assumed and zero frequency is assumed
- the Lorenz gauge is assumed and a non-zero frequency, but still assumed sufficiently low to neglect the term $\textstyle {\frac {1}{c}}{\frac {\partial \phi }{\partial t}}$

## Electromagnetic four-potential

In the context of special relativity, it is natural to join the magnetic vector potential together with the (scalar) electric potential into the electromagnetic potential, also called *four-potential*.

One motivation for doing so is that the four-potential is a mathematical four-vector. Thus, using standard four-vector transformation rules, if the electric and magnetic potentials are known in one inertial reference frame, they can be simply calculated in any other inertial reference frame.

Another, related motivation is that the content of classical electromagnetism can be written in a concise and convenient form using the electromagnetic four potential, especially when the Lorenz gauge is used. In particular, in abstract index notation, the set of Maxwell's equations (in the Lorenz gauge) may be written (in Gaussian units) as follows: ${\begin{aligned}\partial ^{\nu }A_{\nu }&=0\\\Box ^{2}A_{\nu }&={\frac {4\pi }{\ c\ }}\ J_{\nu }\end{aligned}}$ where $\ \Box ^{2}\$ is the d'Alembertian and $\ J\$ is the four-current. The first equation is the Lorenz gauge condition while the second contains Maxwell's equations. The four-potential also plays a very important role in quantum electrodynamics.

## Interpretation

By the Helmholtz theorem, a vector field is described completely by its divergence and curl. As **A** was initially defined solely by its curl ( ${\textstyle \nabla \times \mathbf {A} =\mathbf {B} }$ ), we are justified by choosing any definition of $\nabla \cdot \mathbf {A}$ , provided that we consistently use this definition in all subsequent analysis. All such definitions are valid, and lead to different sets of equations which describe the same phenomena, and the solutions of the equations for any choice of $\nabla \cdot \mathbf {A}$ lead to the same electromagnetic fields, and the same physical predictions about the fields and charges.

It is natural to think that if a quantity exhibits this degree of freedom in its choice, then it should not be interpreted as a real physical quantity. After all, if we can freely choose $\nabla \cdot \mathbf {A}$ to be anything, then $\mathbf {A}$ is not unique. One may ask: what is the "true" value of $\mathbf {A}$ measured in an experiment? If $\mathbf {A}$ is not unique, then the only logical answer must be that we can never measure the value of $\mathbf {A}$ . On this basis, it is often stated that it is not a real physical quantity and it is believed that the fields $\mathbf {E}$ and $\mathbf {B}$ are the true physical quantities.

However, there is at least one experiment in which value of the $\mathbf {E}$ and $\mathbf {B}$ are both zero at the location of a charged particle, but it is nevertheless affected by the presence of a local magnetic vector potential; see the Aharonov–Bohm effect for details. Nevertheless, even in the Aharonov–Bohm experiment, the divergence $\mathbf {A}$ never enters the calculations; only $\nabla \times \mathbf {A}$ along the path of the particle determines the measurable effect.

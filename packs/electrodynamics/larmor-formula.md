---
title: "Larmor formula"
source: https://en.wikipedia.org/wiki/Larmor_formula
domain: electrodynamics
license: CC-BY-SA-4.0
tags: classical electrodynamics, poynting vector, electromagnetic radiation, retarded potential
fetched: 2026-07-02
---

# Larmor formula

In electrodynamics, the **Larmor formula** is used to calculate the total power radiated by a nonrelativistic point charge as it accelerates. It was first derived by Joseph Larmor in 1897, in the context of the wave theory of light.

When any charged particle (such as an electron, a proton, or an ion) accelerates, energy is radiated in the form of electromagnetic waves. For a particle whose velocity is small relative to the speed of light (i.e., nonrelativistic), the total power that the particle radiates (when considered as a point charge) can be calculated by the Larmor formula: ${\begin{aligned}P&={\frac {2}{3}}{\frac {q^{2}}{4\pi \varepsilon _{0}c}}\left({\frac {\dot {v}}{c}}\right)^{2}={\frac {2}{3}}{\frac {q^{2}a^{2}}{4\pi \varepsilon _{0}c^{3}}}\\[0.6ex]&={\frac {q^{2}a^{2}}{6\pi \varepsilon _{0}c^{3}}}=\mu _{0}{\frac {q^{2}a^{2}}{6\pi c}}&{\text{ (SI units)}}\\[1.5ex]P&={\frac {2}{3}}{\frac {q^{2}a^{2}}{c^{3}}}&{\text{ (cgs units)}}\end{aligned}}$ where ${\dot {v}}$ or a is the proper acceleration, q is the charge, c is the speed of light, and $\mu _{0}=1/\varepsilon _{0}c^{2}$ is the vacuum permeability. A relativistic generalization is given by the Liénard–Wiechert potentials.

In either unit system, the power radiated by a single electron can be expressed in terms of the classical electron radius and electron mass as: $P={\frac {2}{3}}{\frac {m_{e}r_{e}a^{2}}{c}}$

One implication is that an electron orbiting around a nucleus, as in the Bohr model, should lose energy, fall to the nucleus and the atom should collapse. This puzzle was not solved until quantum theory was introduced.

## Derivation

To calculate the power radiated by a point charge q at a position $\mathbf {r} (t)$ , with a velocity, $\mathbf {v} (t),$ we integrate the Poynting vector over the surface of a sphere of radius *R*, to get: $P={\frac {cR^{2}}{4\pi }}\oint \mathbf {\hat {r}} \cdot [\mathbf {E} (\mathbf {r} ,t)\times \mathbf {B} (\mathbf {r} ,t)]d\Omega .$ The electric and magnetic fields are given by the Liénard–Wiechert field equations, ${\begin{aligned}\mathbf {E} (\mathbf {r} ,t)&={\frac {q\left(\mathbf {\hat {r}} _{r}-{\boldsymbol {\beta }}_{r}\right)}{r_{r}^{2}\gamma _{r}^{2}{\left(1-\mathbf {{\hat {r}}_{r}} \cdot {\boldsymbol {\beta }}_{r}\right)}^{3}}}+{\frac {q}{c}}\;{\frac {\mathbf {\hat {r}} _{r}\times \left[\left(\mathbf {\hat {r}} _{r}-{\boldsymbol {\beta }}_{r}\right)\times {\dot {\boldsymbol {\beta }}}_{r}\right]}{r_{r}{\left(1-\mathbf {\hat {r}} _{r}\cdot {\boldsymbol {\beta }}_{r}\right)}^{3}}}\\[1ex]\mathbf {B} (\mathbf {r} ,t)&={\hat {\mathbf {r} }}\times \mathbf {E} (\mathbf {r} ,t).\end{aligned}}$ The radius vector, ${\mathbf {r} }_{r}$ , is the distance from the charged particle's position at the retarded time to the point of observation of the electromagnetic fields at the present time, ${\boldsymbol {\beta }}$ is the charge's velocity divided by c , ${\dot {\boldsymbol {\beta }}}$ is the charge's acceleration divided by c , and $\gamma =(1-\beta ^{2})^{-1/2}$ . The variables, ${\mathbf {r} }_{r}$ , ${\boldsymbol {\beta }}_{r}$ , $\gamma _{r}$ , and ${\mathbf {a} }_{r}$ are all evaluated at the retarded time, $t_{r}=t-r_{r}/c$ .

We make a Lorentz transformation to the rest frame of the point charge where $\mathbf {v} '=0$ , and ${\begin{aligned}\mathbf {a'} _{\parallel }&=\mathbf {a} _{\parallel }\gamma ^{3},&\mathbf {a} '_{\perp }&=\mathbf {a} _{\perp }\gamma ^{2}.\end{aligned}}$ Here, ${\mathbf {a} '}_{\parallel }$ is the rest frame acceleration parallel to $\mathbf {v}$ , and $\mathbf {a} '_{\perp }$ is the rest frame acceleration perpendicular to $\mathbf {v}$ .

We integrate the rest frame Poynting vector over the surface of a sphere of radius *R*', to get. $P'={\frac {cR'^{2}}{4\pi }}\oint \mathbf {\hat {r}} '\cdot \left[\mathbf {E} '(\mathbf {r} ',t')\times \mathbf {B} '(\mathbf {r} ',t')\right]d\Omega ',$ We take the limit $R'\to 0.$ In this limit, $t'_{r}=t'$ , and ${\mathbf {a} '}_{r}={\mathbf {a} '},$ so the electric field is given by $\mathbf {E} '(\mathbf {r} ',t')={\frac {q\mathbf {\hat {r}} '}{r'^{2}}}+{\frac {q\left[\mathbf {\hat {r}} '\left(\mathbf {\hat {r}} '\cdot \mathbf {a} '\right)-\mathbf {a} '\right]}{c^{2}r'}},$ with all variables evaluated at the present time.

Then, the surface integral for the radiated power reduces to $P'={\frac {q^{2}}{4\pi c^{3}}}\oint {\mathbf {\hat {r}} '}\cdot \left[\mathbf {a} '\times \left({\hat {\mathbf {r} }}'\times \mathbf {a} '\right)\right]d\Omega '={\frac {2q^{2}a'^{2}}{3c^{3}}}.$ The radiated power can be put back in terms of the original acceleration in the moving frame, to give $P'={\frac {2q^{2}}{3c^{3}}}\left(a_{\parallel }^{2}\gamma ^{6}+a_{\perp }^{2}\gamma ^{4}\right)={\frac {2q^{2}\gamma ^{6}}{3c^{3}}}\left[a^{2}-{\left(\mathbf {v} \times \mathbf {a} /c\right)}^{2}\right].$ The variables in this equation are in the original moving frame, but the rate of energy emission on the left hand side of the equation is still given in terms of the rest frame variables. However, the right-hand side will be shown below to be a Lorentz invariant, so radiated power can be Lorentz transformed to the moving frame, finally giving $P={\frac {2q^{2}\gamma ^{4}}{3c^{3}}}\left(a_{\parallel }^{2}\gamma ^{2}+a_{\perp }^{2}\right)={\frac {2q^{2}\gamma ^{6}}{3c^{3}}}\left[a^{2}-{\left(\mathbf {v} \times \mathbf {a} /c\right)}^{2}\right].$ This result (in two forms) is the same as Liénard's relativistic extension of Larmor's formula, and is given here with all variables at the present time. Its nonrelativistic reduction reduces to Larmor's original formula.

For high-energies, it appears that the power radiated for acceleration parallel to the velocity is a factor $\gamma ^{2}$ larger than that for perpendicular acceleration. However, writing the Liénard formula in terms of the velocity gives a misleading implication. In terms of momentum instead of velocity, the Liénard formula becomes

$P={\frac {2q^{2}}{3c^{3}m^{2}}}\left[\left({\frac {d\mathbf {p} }{dt}}\right)_{\parallel }^{2}+\gamma ^{2}\left({\frac {d\mathbf {p} }{dt}}\right)_{\perp }^{2}\right].$

This shows that the power emitted for $d\mathbf {p} /dt$ perpendicular to the velocity is larger by a factor of $\gamma ^{2}$ than the power for $d\mathbf {p} /dt$ parallel to the velocity. This results in radiation damping being negligible for linear accelerators, but a limiting factor for circular accelerators.

### Covariant form

The radiated power is actually a Lorentz scalar, given in covariant form as

$P=-{\frac {2}{3}}{\frac {q^{2}}{m^{2}c^{3}}}{\frac {dp_{\mu }}{d\tau }}{\frac {dp^{\mu }}{d\tau }}.$

To show this, we reduce the four-vector scalar product to vector notation. We start with ${\frac {dp_{\mu }}{d\tau }}{\frac {dp^{\mu }}{d\tau }}=\gamma ^{2}\left[\left({\frac {dp_{0}}{dt}}\right)^{2}-\left({\frac {d\mathbf {p} }{dt}}\right)^{2}\right].$

The time derivatives are

${\frac {dp_{0}}{dt}}={\frac {d}{dt}}(m\gamma )=m\gamma ^{3}va_{\parallel }$ ${\frac {d\mathbf {p} }{dt}}={\frac {d}{dt}}\left(m\mathbf {v} \gamma \right)=m\gamma ^{3}\left(\mathbf {a} _{\parallel }+\mathbf {a} _{\perp }/\gamma ^{2}\right).$ When these derivatives are used, we get ${\frac {dp_{\mu }}{d\tau }}{\frac {dp^{\mu }}{d\tau }}=-m^{2}\gamma ^{4}\left(\gamma ^{2}\mathbf {a} _{\parallel }^{2}+{\mathbf {a} }_{\perp }^{2}\right).$

With this expression for the scalar product, the manifestly invariant form for the power agrees with the vector form above, demonstrating that the radiated power is a Lorentz scalar

### Angular distribution

The angular distribution of radiated power is given by a general formula, applicable whether or not the particle is relativistic. In CGS units, this formula is $P={\frac {2}{3}}{\frac {q^{2}}{m^{2}c^{3}}}{\left|{\dot {\mathbf {p} }}\right|}^{2}.$ ${\frac {dP}{d\Omega }}={\frac {q^{2}}{4\pi c}}{\frac {\left|\mathbf {\hat {n}} \times \left[(\mathbf {\hat {n}} -{\boldsymbol {\beta }})\times {\dot {\boldsymbol {\beta }}}\right]\right|^{2}}{{\left(1-\mathbf {\hat {n}} \cdot {\boldsymbol {\beta }}\right)}^{5}}},$ where $\mathbf {\hat {n}}$ is a unit vector pointing from the particle towards the observer. In the case of linear motion (velocity parallel to acceleration), this simplifies to ${\frac {dP}{d\Omega }}={\frac {q^{2}a^{2}}{4\pi c^{3}}}{\frac {\sin ^{2}\theta }{{\left(1-\beta \cos \theta \right)}^{5}}},$ where $\theta$ is the angle between the observer and the particle's motion.

### Radiation reaction

The radiation from a charged particle carries energy and momentum. In order to satisfy energy and momentum conservation, the charged particle must experience a recoil at the time of emission. The radiation must exert an additional force on the charged particle. This force is known as Abraham-Lorentz force while its non-relativistic limit is known as the Lorentz self-force and relativistic forms are known as Lorentz-Dirac force or Abraham-Lorentz-Dirac force. The radiation reaction phenomenon is one of the key problems and consequences of the Larmor formula. According to classical electrodynamics, a charged particle produces electromagnetic radiation as it accelerates. The particle loses momentum and energy as a result of the radiation, which is carrying it away from it. The radiation response force, on the other hand, also acts on the charged particle as a result of the radiation.

The dynamics of charged particles are significantly impacted by the existence of this force. In particular, it causes a change in their motion that may be accounted for by the Larmor formula, a factor in the Lorentz-Dirac equation.

According to the Lorentz-Dirac equation, a charged particle's velocity will be influenced by a "self-force" resulting from its own radiation. Such non-physical behavior as runaway solutions, when the particle's velocity or energy become infinite in a finite amount of time, might result from this self-force.

A resolution to the paradoxes resulting from the introduction of a self-force due to the emission of electromagnetic radiation, is that there is no self-force produced. The acceleration of a charged particle produces electromagnetic radiation, whose outgoing energy reduces the energy of the charged particle. This results in 'radiation reaction' that decreases the acceleration of the charged particle, not as a self force, but just as less acceleration of the particle.

### Atomic physics

The invention of quantum physics, notably the Bohr model of the atom, was able to explain this gap between the classical prediction and the actual reality. The Bohr model proposed that transitions between distinct energy levels, which electrons could only inhabit, might account for the observed spectral lines of atoms. The wave-like properties of electrons and the idea of energy quantization were used to explain the stability of these electron orbits.

The Larmor formula can only be used for non-relativistic particles, which limits its usefulness. The Liénard-Wiechert potential is a more comprehensive formula that must be employed for particles travelling at relativistic speeds. In certain situations, more intricate calculations including numerical techniques or perturbation theory could be necessary to precisely compute the radiation the charged particle emits.

## In special relativity

There is an extension for Larmor formula in special relativity. The radiation power given a four-acceleration $a^{\mu }$ would be

$P=(q^{2}/6\pi \varepsilon _{o}c^{3})(a^{\mu }a_{\mu })$

Lienard-Wiechert formula appears as the restriction of this equation when using a 3-acceleration vector.

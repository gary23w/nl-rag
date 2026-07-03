---
title: "Abraham–Lorentz force"
source: https://en.wikipedia.org/wiki/Abraham%E2%80%93Lorentz_force
domain: electrical-resistance-and-conductance
license: CC-BY-SA-4.0
tags: electrical resistance and conductance
fetched: 2026-07-03
---

# Abraham–Lorentz force

In the physics of electromagnetism, the **Abraham–Lorentz force** (also known as the **Lorentz–Abraham force**) is the reaction force on an accelerating charged particle caused by the particle emitting electromagnetic radiation by self-interaction. It is also called the **radiation reaction force**, the **radiation damping force**, or the **self-force**. It is named after the physicists Max Abraham and Hendrik Lorentz.

The formula, although predating the theory of special relativity, was initially calculated for non-relativistic velocity approximations. It was extended to arbitrary velocities by Max Abraham and was shown to be physically consistent by George Adolphus Schott. The non-relativistic form is called **Lorentz self-force** while the relativistic version is called the **Lorentz–Dirac force** or collectively known as **Abraham–Lorentz–Dirac force**. The equations are in the domain of classical physics, not quantum physics, and therefore may not be valid at distances of roughly the Compton wavelength or below. There are, however, two analogs of the formula that are both fully quantum and relativistic: one is called the "Abraham–Lorentz–Dirac–Langevin equation", the other is the self-force on a moving mirror.

The force is proportional to the square of the object's charge, multiplied by the jerk that it is experiencing. (Jerk is the rate of change of acceleration.) The force points in the direction of the jerk. For example, in a cyclotron, where the jerk points opposite to the velocity, the radiation reaction is directed opposite to the velocity of the particle, providing a braking action. The Abraham–Lorentz force is the source of the radiation resistance of a radio antenna radiating radio waves.

There are pathological solutions of the Abraham–Lorentz–Dirac equation in which a particle accelerates *in advance* of the application of a force, so-called *pre-acceleration* solutions. Since this would represent an effect occurring before its cause (retrocausality), some theories have speculated that the equation allows signals to travel backward in time, thus challenging the physical principle of causality. One resolution of this problem was discussed by Arthur D. Yaghjian and was further discussed by Fritz Rohrlich and Rodrigo Medina. Furthermore, some authors argue that a radiation reaction force is unnecessary, introducing a corresponding stress-energy tensor that naturally conserves energy and momentum in Minkowski space and other suitable spacetimes.

## Definition and description

The **Lorentz self-force** derived for non-relativistic velocity approximation $v\ll c$ , is given in SI units by: $\mathbf {F} _{\mathrm {rad} }={\frac {\mu _{0}q^{2}}{6\pi c}}\mathbf {\dot {a}} ={\frac {q^{2}}{6\pi \varepsilon _{0}c^{3}}}\mathbf {\dot {a}} ={\frac {2}{3}}{\frac {q^{2}}{4\pi \varepsilon _{0}c^{3}}}\mathbf {\dot {a}}$ or in Gaussian units by $\mathbf {F} _{\mathrm {rad} }={2 \over 3}{\frac {q^{2}}{c^{3}}}\mathbf {\dot {a}} .$ where $\mathbf {F} _{\mathrm {rad} }$ is the force, $\mathbf {\dot {a}}$ is the derivative of acceleration, or the third derivative of displacement, also called jerk, *μ*0 is the magnetic constant, *ε*0 is the electric constant, *c* is the speed of light in free space, and *q* is the electric charge of the particle.

Physically, an accelerating charge emits radiation (according to the Larmor formula), which carries momentum away from the charge. Since momentum is conserved, the charge is pushed in the direction opposite the direction of the emitted radiation. In fact the formula above for radiation force can be *derived* from the Larmor formula, as shown below.

The **Abraham–Lorentz force**, a generalization of Lorentz self-force for arbitrary velocities is given by: $\mathbf {F} _{\mathrm {rad} }={\frac {\mu _{0}q^{2}}{6\pi c}}\left(\gamma ^{2}{\dot {a}}+{\frac {\gamma ^{4}v(v\cdot {\dot {a}})}{c^{2}}}+{\frac {3\gamma ^{4}a(v\cdot a)}{c^{2}}}+{\frac {3\gamma ^{6}v(v\cdot a)^{2}}{c^{4}}}\right)$

Where $\gamma$ is the Lorentz factor associated with v , the velocity of particle. The formula is consistent with special relativity and reduces to Lorentz's self-force expression for low velocity limit.

The covariant form of radiation reaction deduced by Dirac for arbitrary shape of elementary charges is found to be: $F_{\mu }^{\mathrm {rad} }={\frac {\mu _{0}q^{2}}{6\pi mc}}\left[{\frac {d^{2}p_{\mu }}{d\tau ^{2}}}+{\frac {p_{\mu }}{m^{2}c^{2}}}\left({\frac {dp_{\nu }}{d\tau }}{\frac {dp^{\nu }}{d\tau }}\right)\right]$

## History

The first calculation of electromagnetic radiation energy due to current was given by George Francis FitzGerald in 1883, in which radiation resistance appears. However, dipole antenna experiments by Heinrich Hertz made a bigger impact and gathered commentary by Poincaré on the *amortissement* or damping of the oscillator due to the emission of radiation. Qualitative discussions surrounding damping effects of radiation emitted by accelerating charges was sparked by Henri Poincaré in 1891. In 1892, Hendrik Lorentz derived the self-interaction force of charges for low velocities but did not relate it to radiation losses. Suggestion of a relationship between radiation energy loss and self-force was first made by Max Planck. Planck's concept of the damping force, which did not assume any particular shape for elementary charged particles, was applied by Max Abraham to find the radiation resistance of an antenna in 1898, which remains the most practical application of the phenomenon.

In the early 1900s, Abraham formulated a generalization of the Lorentz self-force to arbitrary velocities, the physical consistency of which was later shown by George Adolphus Schott. Schott was able to derive the Abraham equation and attributed "acceleration energy" to be the source of energy of the electromagnetic radiation. Originally submitted as an essay for the 1908 Adams Prize, he won the competition and had the essay published as a book in 1912. The relationship between self-force and radiation reaction became well-established at this point. Wolfgang Pauli first obtained the covariant form of the radiation reaction and in 1938, Paul Dirac found that the equation of motion of charged particles, without assuming the shape of the particle, contained Abraham's formula within reasonable approximations. The equations derived by Dirac are considered exact within the limits of classical theory.

## Background

In classical electrodynamics, problems are typically divided into two classes:

1. Problems in which the charge and current *sources* of fields are specified and the *fields* are calculated, and
2. The reverse situation, problems in which the fields are specified and the motion of particles are calculated.

In some fields of physics, such as plasma physics and the calculation of transport coefficients (conductivity, diffusivity, *etc.*), the fields generated by the sources and the motion of the sources are solved self-consistently. In such cases, however, the motion of a selected source is calculated in response to fields generated by all other sources. Rarely is the motion of a particle (source) due to the fields generated by that same particle calculated. The reason for this is twofold:

1. Neglect of the "self-fields" usually leads to answers that are accurate enough for many applications, and
2. Inclusion of self-fields leads to problems in physics such as renormalization, some of which are still unsolved, that relate to the very nature of matter and energy.

These conceptual problems created by self-fields are highlighted in a standard graduate text. [Jackson]

> The difficulties presented by this problem touch one of the most fundamental aspects of physics, the nature of the elementary particle. Although partial solutions, workable within limited areas, can be given, the basic problem remains unsolved. One might hope that the transition from classical to quantum-mechanical treatments would remove the difficulties. While there is still hope that this may eventually occur, the present quantum-mechanical discussions are beset with even more elaborate troubles than the classical ones. It is one of the triumphs of comparatively recent years (~ 1948–1950) that the concepts of Lorentz covariance and gauge invariance were exploited sufficiently cleverly to circumvent these difficulties in quantum electrodynamics and so allow the calculation of very small radiative effects to extremely high precision, in full agreement with experiment. From a fundamental point of view, however, the difficulties remain.

The Abraham–Lorentz force is the result of the most fundamental calculation of the effect of self-generated fields. It arises from the observation that accelerating charges emit radiation. The Abraham–Lorentz force is the average force that an accelerating charged particle feels in the recoil from the emission of radiation. The introduction of quantum effects leads one to quantum electrodynamics. The self-fields in quantum electrodynamics generate a finite number of infinities in the calculations that can be removed by the process of renormalization. This has led to a theory that is able to make the most accurate predictions that humans have made to date. (See precision tests of QED.) The renormalization process fails, however, when applied to the gravitational force. The infinities in that case are infinite in number, which causes the failure of renormalization. Therefore, general relativity has an unsolved self-field problem. String theory and loop quantum gravity are current attempts to resolve this problem, formally called the problem of radiation reaction or the problem of self-force.

## Derivation

The simplest derivation for the self-force is found for periodic motion from the Larmor formula for the power radiated from a point charge that moves with velocity much lower than that of speed of light: $P={\frac {\mu _{0}q^{2}}{6\pi c}}\mathbf {a} ^{2}.$

If we assume the motion of a charged particle is periodic, then the average work done on the particle by the Abraham–Lorentz force is the negative of the Larmor power integrated over one period from $\tau _{1}$ to $\tau _{2}$ : $\int _{\tau _{1}}^{\tau _{2}}\mathbf {F} _{\mathrm {rad} }\cdot \mathbf {v} dt=\int _{\tau _{1}}^{\tau _{2}}-Pdt=-\int _{\tau _{1}}^{\tau _{2}}{\frac {\mu _{0}q^{2}}{6\pi c}}\mathbf {a} ^{2}dt=-\int _{\tau _{1}}^{\tau _{2}}{\frac {\mu _{0}q^{2}}{6\pi c}}{\frac {d\mathbf {v} }{dt}}\cdot {\frac {d\mathbf {v} }{dt}}dt.$

The above expression can be integrated by parts. If we assume that there is periodic motion, the boundary term in the integral by parts disappears: $\int _{\tau _{1}}^{\tau _{2}}\mathbf {F} _{\mathrm {rad} }\cdot \mathbf {v} dt=-{\frac {\mu _{0}q^{2}}{6\pi c}}{\frac {d\mathbf {v} }{dt}}\cdot \mathbf {v} {\bigg |}_{\tau _{1}}^{\tau _{2}}+\int _{\tau _{1}}^{\tau _{2}}{\frac {\mu _{0}q^{2}}{6\pi c}}{\frac {d^{2}\mathbf {v} }{dt^{2}}}\cdot \mathbf {v} dt=-0+\int _{\tau _{1}}^{\tau _{2}}{\frac {\mu _{0}q^{2}}{6\pi c}}\mathbf {\dot {a}} \cdot \mathbf {v} dt.$

Clearly, we can identify the Lorentz self-force equation which is applicable to slow moving particles as: $\mathbf {F} _{\mathrm {rad} }={\frac {\mu _{0}q^{2}}{6\pi c}}\mathbf {{\dot {a}}.}$ A more rigorous derivation, which does not require periodic motion, was found using an effective field theory formulation.

A generalized equation for arbitrary velocities was formulated by Max Abraham, which is found to be consistent with special relativity. An alternative derivation, making use of theory of relativity which was well established at that time, was found by Dirac without any assumption of the shape of the charged particle.

## Signals from the future

Below is an illustration of how a classical analysis can lead to surprising results. The classical theory can be seen to challenge standard pictures of causality, thus signaling either a breakdown or a need for extension of the theory. In this case the extension is to quantum mechanics and its relativistic counterpart quantum field theory. See the quote from Rohrlich in the introduction concerning "the importance of obeying the validity limits of a physical theory".

For a particle in an external force $\mathbf {F} _{\mathrm {ext} }$ , we have $m{\dot {\mathbf {v} }}=\mathbf {F} _{\mathrm {rad} }+\mathbf {F} _{\mathrm {ext} }=mt_{0}{\ddot {\mathbf {v} }}+\mathbf {F} _{\mathrm {ext} }.$ where $t_{0}={\frac {\mu _{0}q^{2}}{6\pi mc}}.$

This equation can be integrated once to obtain $m{\dot {\mathbf {v} }}={1 \over t_{0}}\int _{t}^{\infty }\exp \left(-{t'-t \over t_{0}}\right)\,\mathbf {F} _{\mathrm {ext} }(t')\,dt'.$

The integral extends from the present to infinitely far in the future. Thus future values of the force affect the acceleration of the particle in the present. The future values are weighted by the factor $\exp \left(-{t'-t \over t_{0}}\right)$ which falls off rapidly for times greater than $t_{0}$ in the future. Therefore, signals from an interval approximately $t_{0}$ into the future affect the acceleration in the present. For an electron, this time is approximately $10^{-24}$ sec, which is the time it takes for a light wave to travel across the "size" of an electron, the classical electron radius. One way to define this "size" is as follows: it is (up to some constant factor) the distance r such that two electrons placed at rest at a distance r apart and allowed to fly apart, would have sufficient energy to reach half the speed of light. In other words, it forms the length (or time, or energy) scale where something as light as an electron would be fully relativistic. It is worth noting that this expression does not involve the Planck constant at all, so although it indicates something is wrong at this length scale, it does not directly relate to quantum uncertainty, or to the frequency–energy relation of a photon. Although it is common in quantum mechanics to treat $\hbar \to 0$ as a "classical limit", some speculate that even the classical theory needs renormalization, no matter how the Planck constant would be fixed.

## Abraham–Lorentz–Dirac force

To find the relativistic generalization, Dirac renormalized the mass in the equation of motion with the Abraham–Lorentz force in 1938. This renormalized equation of motion is called the Abraham–Lorentz–Dirac equation of motion.

### Definition

The expression derived by Dirac is given in signature (− + + +) by $F_{\mu }^{\mathrm {rad} }={\frac {\mu _{0}q^{2}}{6\pi mc}}\left[{\frac {d^{2}p_{\mu }}{d\tau ^{2}}}-{\frac {p_{\mu }}{m^{2}c^{2}}}\left({\frac {dp_{\nu }}{d\tau }}{\frac {dp^{\nu }}{d\tau }}\right)\right].$

With Liénard's relativistic generalization of Larmor's formula in the co-moving frame, $P={\frac {\mu _{0}q^{2}a^{2}\gamma ^{6}}{6\pi c}},$ one can show this to be a valid force by manipulating the time average equation for power: ${\frac {1}{\Delta t}}\int _{0}^{t}Pdt={\frac {1}{\Delta t}}\int _{0}^{t}{\textbf {F}}\cdot {\textbf {v}}\,dt.$

## Paradoxes

### Pre-acceleration

Similar to the non-relativistic case, there are pathological solutions using the Abraham–Lorentz–Dirac equation that anticipate a change in the external force and according to which the particle accelerates *in advance* of the application of a force, so-called *preacceleration* solutions. One resolution of this problem was discussed by Yaghjian, and is further discussed by Rohrlich and Medina.

### Runaway solutions

Runaway solutions are solutions to ALD equations that suggest the force on objects will increase exponentially over time. They are considered unphysical.

### Hyperbolic motion

The ALD equations are known to be zero for constant acceleration or hyperbolic motion in Minkowski spacetime diagram. The subject of whether in such condition electromagnetic radiation exists was matter of debate until Fritz Rohrlich resolved the problem by showing that hyperbolically moving charges do emit radiation. Subsequently, the issue is discussed in context of energy conservation and equivalence principle which is classically resolved by considering "acceleration energy" or Schott energy.

## Self-interactions

However the antidamping mechanism resulting from the Abraham–Lorentz force can be compensated by other nonlinear terms, which are frequently disregarded in the expansions of the retarded Liénard–Wiechert potential.

## Landau–Lifshitz radiation damping force

The Abraham–Lorentz–Dirac force leads to some pathological solutions. In order to avoid this, Lev Landau and Evgeny Lifshitz came with the following formula for radiation damping force, which is valid when the radiation damping force is small compared with the Lorentz force in some frame of reference (assuming it exists),

$g^{i}={\frac {2e^{3}}{3mc^{3}}}\left\{{\frac {\partial F^{ik}}{\partial x^{l}}}u_{k}u^{l}-{\frac {e}{mc^{2}}}\left[F^{il}F_{kl}u^{k}-(F_{kl}u^{l})(F^{km}u_{m})u^{i}\right]\right\}$

so that the equation of motion of the charge e in an external field $F^{ik}$ can be written as

$mc{\frac {du^{i}}{ds}}={\frac {e}{c}}F^{ik}u_{k}+g^{i}.$

Here $u^{i}=(\gamma ,\gamma \mathbf {v} /c)$ is the four-velocity of the particle, $\gamma =1/{\sqrt {1-v^{2}/c^{2}}}$ is the Lorentz factor and $\mathbf {v}$ is the three-dimensional velocity vector. The three-dimensional Landau–Lifshitz radiation damping force can be written as

$\mathbf {F} _{\mathrm {rad} }={\frac {2e^{3}\gamma }{3mc^{3}}}\left\{{\frac {D\mathbf {E} }{Dt}}+{\frac {1}{c}}\mathbf {v} \times {\frac {D\mathbf {H} }{Dt}}\right\}+{\frac {2e^{4}}{3m^{2}c^{4}}}\left[\mathbf {E} \times \mathbf {H} +{\frac {1}{c}}\mathbf {H} \times (\mathbf {H} \times \mathbf {v} )+{\frac {1}{c}}\mathbf {E} (\mathbf {v} \cdot \mathbf {E} )\right]-{\frac {2e^{4}\gamma ^{2}\mathbf {v} }{3m^{2}c^{5}}}\left[\left(\mathbf {E} +{\frac {1}{c}}\mathbf {v} \times \mathbf {H} \right)^{2}-{\frac {1}{c^{2}}}(\mathbf {E} \cdot \mathbf {v} )^{2}\right]$

where $D/Dt=\partial /\partial t+\mathbf {v} \cdot \nabla$ is the total derivative.

## Experimental observations

While the Abraham–Lorentz force is largely neglected for many experimental considerations, it gains importance for plasmonic excitations in larger nanoparticles due to large local field enhancements. Radiation damping acts as a limiting factor for the plasmonic excitations in surface-enhanced Raman scattering. The damping force was shown to broaden surface plasmon resonances in gold nanoparticles, nanorods and clusters.

The effects of radiation damping on nuclear magnetic resonance were also observed by Nicolaas Bloembergen and Robert Pound, who reported its dominance over spin–spin and spin–lattice relaxation mechanisms for certain cases.

The Abraham–Lorentz force has been observed in the semiclassical regime in experiments which involve the scattering of a relativistic beam of electrons with a high intensity laser. In the experiments, a supersonic jet of helium gas is intercepted by a high-intensity (1018–1020 W/cm2) laser. The laser ionizes the helium gas and accelerates the electrons via what is known as the "laser-wakefield" effect. A second high-intensity laser beam is then propagated counter to this accelerated electron beam. In a small number of cases, inverse-Compton scattering occurs between the photons and the electron beam, and the spectra of the scattered electrons and photons are measured. The photon spectra are then compared with spectra calculated from Monte Carlo simulations that use either the QED or classical LL equations of motion.

## Collective effects

The effects of radiation reaction are often considered within the framework of single-particle dynamics. However, interesting phenomena arise when a collection of charged particles is subjected to strong electromagnetic fields, such as in a plasma. In such scenarios, the collective behavior of the plasma can significantly modify its properties due to radiation reaction effects. Theoretical studies have shown that in environments with strong magnetic fields, like those found around pulsars and magnetars, radiation reaction cooling can alter the collective dynamics of the plasma. This modification can lead to instabilities within the plasma. Specifically, in the high magnetic fields typical of these astrophysical objects, the momentum distribution of particles is bunched and becomes anisotropic due to radiation reaction forces, potentially driving plasma instabilities and affecting overall plasma behavior. Among these instabilities, the firehose instability can arise due to the anisotropic pressure, and electron cyclotron maser due to population inversion in the rings.

## Radiation reaction without the Abraham-Lorentz force

An alternate mechanism for radiation reaction on a point charge accelerated by an external force, is that the charge's increase in energy is diminished by the energy carried away by electromagnetic radiation. This reduces the particle's acceleration without an additional force, and the paradoxes it causes are not there.

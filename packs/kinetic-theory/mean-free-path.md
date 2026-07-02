---
title: "Mean free path"
source: https://en.wikipedia.org/wiki/Mean_free_path
domain: kinetic-theory
license: CC-BY-SA-4.0
tags: kinetic theory of gases, mean free path, boltzmann equation, ideal gas law
fetched: 2026-07-02
---

# Mean free path

In physics, **mean free path** is the average distance over which a moving particle (such as an atom, a molecule, or a photon) travels before substantially changing its direction or energy (or, in a specific context, other properties), typically as a result of one or more successive collisions with other particles.

## Scattering theory

Imagine a beam of particles being shot through a target, and consider an infinitesimally thin slab of the target (see the figure). The atoms (or particles) that might stop a beam particle are shown in red. The magnitude of the mean free path depends on the characteristics of the system. Assuming that all the target particles are at rest but only the beam particle is moving, that gives an expression for the mean free path:

$\ell =(\sigma n)^{-1},$

where ℓ is the mean free path, n is the number of target particles per unit volume, and σ is the effective cross-sectional area for collision per target particle.

The area of the slab is *L*2, and its volume is *L*2 *dx*. The typical number of stopping atoms in the slab is the concentration n times the volume, i.e., *n L*2 *dx*. The probability that a beam particle will be stopped in that slab is the net area of the stopping atoms divided by the total area of the slab:

${\mathcal {P}}({\text{stopping within }}dx)={\frac {{\text{Area}}_{\text{atoms}}}{{\text{Area}}_{\text{slab}}}}={\frac {\sigma nL^{2}\,dx}{L^{2}}}=n\sigma \,dx,$

where σ is the cross-sectional area (or, more formally, the "scattering cross-section") of one atom.

The drop in beam intensity equals the incoming beam intensity multiplied by the probability of the particle being stopped within the slab:

$dI=-In\sigma \,dx.$

This is an ordinary differential equation:

${\frac {dI}{dx}}=-In\sigma {\overset {\text{def}}{=}}-{\frac {I}{\ell }},$

whose solution is known as the Beer–Lambert law and has the form $I=I_{0}e^{-x/\ell }$ , where x is the distance traveled by the beam through the target, and *I*0 is the beam intensity before it entered the target; ℓ is called the mean free path because it equals the mean distance traveled by a beam particle before being stopped. To see this, note that the probability that a particle is absorbed between x and *x* + *dx* is given by

$d{\mathcal {P}}(x)={\frac {I(x)-I(x+dx)}{I_{0}}}={\frac {1}{\ell }}e^{-x/\ell }dx.$

Thus the expectation value (or average, or simply mean) of x is

$\langle x\rangle {\overset {\text{def}}{=}}\int _{0}^{\infty }xd{\mathcal {P}}(x)=\int _{0}^{\infty }{\frac {x}{\ell }}e^{-x/\ell }\,dx=\ell .$

The fraction of particles that are not stopped (attenuated) by the slab is called the transmission $T=I/I_{0}=e^{-x/\ell }$ , where x is equal to the thickness of the slab.

## Kinetic theory of gases

In the kinetic theory of gases, the *mean free path* of a particle, such as a molecule, is the average distance the particle travels between collisions with other moving particles. The derivation above assumed the target particles to be at rest; therefore, in reality, the formula $\ell =(n\sigma )^{-1}$ holds for a beam particle with a high speed v relative to the velocities of an ensemble of identical particles with random locations. In that case, the motions of target particles are comparatively negligible, hence the relative velocity $v_{\text{rel}}\approx v$ .

If, on the other hand, the beam particle is part of an established equilibrium with identical particles, then the square of relative velocity is:

$\left\langle \mathbf {v} _{\text{relative}}^{2}\right\rangle =\left\langle \left(\mathbf {v} _{1}-\mathbf {v} _{2}\right)^{2}\right\rangle =\left\langle \mathbf {v} _{1}^{2}+\mathbf {v} _{2}^{2}-2\mathbf {v} _{1}\cdot \mathbf {v} _{2}\right\rangle .$

In equilibrium, $\mathbf {v} _{1}$ and $\mathbf {v} _{2}$ are random and uncorrelated, therefore $\langle \mathbf {v} _{1}\cdot \mathbf {v} _{2}\rangle =0$ , and the relative speed is

$v_{\text{rel}}={\sqrt {\langle \mathbf {v} _{\text{relative}}^{2}\rangle }}={\sqrt {\langle \mathbf {v} _{1}^{2}+\mathbf {v} _{2}^{2}\rangle }}={\sqrt {2}}v.$

This means that the number of collisions is ${\sqrt {2}}$ times the number with stationary targets. Therefore, the following relationship applies:

$\ell =\left({\sqrt {2}}\,n\sigma \right)^{-1},$

and using $n=N/V=p/(k_{\text{B}}T)$ (ideal gas law) and $\sigma =\pi d^{2}$ (effective cross-sectional area for spherical particles with diameter d ), it may be shown that the mean free path is

$\ell ={\frac {k_{\text{B}}T}{{\sqrt {2}}\pi d^{2}p}},$

where $k_{\text{B}}$ is the Boltzmann constant, p is the pressure of the gas and T is the absolute temperature.

In practice, the diameter of gas molecules is not well defined. In fact, the kinetic diameter of a molecule is defined in terms of the mean free path. Typically, gas molecules do not behave like hard spheres, but rather attract each other at larger distances and repel each other at shorter distances, as can be described with a Lennard-Jones potential. One way to deal with such "soft" molecules is to use the Lennard-Jones σ parameter as the diameter.

Another way is to assume a hard-sphere gas that has the same viscosity as the actual gas being considered. This leads to a mean free path

$\ell ={\frac {\mu }{\rho }}{\sqrt {\frac {\pi m}{2k_{\text{B}}T}}}={\frac {\mu }{p}}{\sqrt {\frac {\pi k_{\text{B}}T}{2m}}},$

where m is the molecular mass, $\rho =mp/(k_{\text{B}}T)$ is the density of ideal gas, and *μ* is the dynamic viscosity. This expression can be put into the following convenient form

$\ell ={\frac {\mu }{p}}{\sqrt {\frac {\pi R_{\text{specific}}T}{2}}},$

with $R_{\text{specific}}=k_{\text{B}}/m$ being the specific gas constant, equal to 287 J/(kg.K) for air. Viscosity *μ* is low, 18.5 μPa·s at (25 °C, 1 bar), and p-dependent.

The following table lists some typical values for air at different pressures at room temperature. Note that different definitions of the molecular diameter, as well as different assumptions about the value of atmospheric pressure (100 vs 101.3 kPa) and room temperature (293.15 vs 296.15 K (20-23 °C) or even 300 K) can lead to slightly different values of the mean free path.

| Vacuum range | Pressure in hPa (mbar) | Pressure in mmHg (Torr) | number density (Molecules / cm3) | number density (Molecules / m3) | Mean free path |
|---|---|---|---|---|---|
| Ambient pressure | 1013 | 759.8 | 2.7 × 1019 | 2.7 × 1025 | 64 – 68 nm |
| Low vacuum | 300 – 1 | 220 – 8×10−1 | 1019 – 1016 | 1025 – 1022 | 0.1 – 100 μm |
| Medium vacuum | 1 – 10−3 (0.1 Pa) | 8×10−1 – 8×10−4 | 1016 – 1013 | 1022 – 1019 | 0.1 – 100 mm |
| High vacuum | 10−3 – 10−7 (10 μPa) | 8×10−4 – 8×10−8 | 1013 – 109 | 1019 – 1015 | 10 cm – 1 km |
| Ultra-high vacuum | 10−7 – 10−12 (0.1 nPa) | 8×10−8 – 8×10−13 | 109 – 104 | 1015 – 1010 | 1 km – 105 km |
| Extremely high vacuum | <10−12 | <8×10−13 | <104 | <1010 | >105 km |

## In other fields

### Radiography

In gamma-ray radiography the *mean free path* of a pencil beam of mono-energetic photons is the average distance a photon travels between collisions with atoms of the target material. It depends on the material and the energy of the photons:

$\ell =\mu ^{-1}=((\mu /\rho )\rho )^{-1},$

where *μ* is the linear attenuation coefficient, *μ/ρ* is the mass attenuation coefficient and *ρ* is the density of the material. The mass attenuation coefficient can be looked up or calculated for any material and energy combination using the National Institute of Standards and Technology (NIST) databases.

In X-ray radiography the calculation of the *mean free path* is more complicated, because photons are not mono-energetic, but have some distribution of energies called a spectrum. As photons move through the target material, they are attenuated with probabilities depending on their energy, as a result their distribution changes in process called spectrum hardening. Because of spectrum hardening, the *mean free path* of the X-ray spectrum changes with distance.

Sometimes one measures the thickness of a material in the *number of mean free paths*. Material with the thickness of one *mean free path* will attenuate to 37% (1/*e*) of photons. This concept is closely related to half-value layer (HVL): a material with a thickness of one HVL will attenuate 50% of photons. A standard x-ray image is a transmission image, an image with negative logarithm of its intensities is sometimes called a *number of mean free paths* image.

### Electronics

In macroscopic charge transport, the mean free path of a charge carrier in a metal $\ell$ is proportional to the electrical mobility $\mu$ , a value directly related to electrical conductivity, that is: $\mu ={\frac {q\tau }{m}}={\frac {q\ell }{m^{*}v_{\text{F}}}},$

where *q* is the charge, $\tau$ is the mean free time, *m** is the effective mass, and *v*F is the Fermi velocity of the charge carrier. The Fermi velocity can easily be derived from the Fermi energy via the non-relativistic kinetic energy equation. In thin films, however, the film thickness can be smaller than the predicted mean free path, making surface scattering much more noticeable, effectively increasing the resistivity.

Electron mobility through a medium with dimensions smaller than the mean free path of electrons occurs through ballistic conduction or ballistic transport. In such scenarios electrons alter their motion only in collisions with conductor walls.

### Optics

If one takes a suspension of non-light-absorbing particles of diameter *d* with a volume fraction *Φ*, the mean free path of the photons is:

$\ell ={\frac {2d}{3\Phi Q_{\text{s}}}},$

where *Q*s is the scattering efficiency factor. *Q*s can be evaluated numerically for spherical particles using Mie theory.

### Acoustics

In an otherwise empty cavity, the mean free path of a single particle bouncing off the walls is:

$\ell ={\frac {FV}{S}},$

where *V* is the volume of the cavity, *S* is the total inside surface area of the cavity, and *F* is a constant related to the shape of the cavity. For most simple cavity shapes, *F* is approximately 4.

This relation is used in the derivation of the Sabine equation in acoustics, using a geometrical approximation of sound propagation.

### Nuclear and particle physics

In particle physics the concept of the mean free path is not commonly used, being replaced by the similar concept of attenuation length. In particular, for high-energy photons, which mostly interact by electron–positron pair production, the radiation length is used much like the mean free path in radiography.

Independent-particle models in nuclear physics require the undisturbed orbiting of nucleons within the nucleus before they interact with other nucleons.

> The effective mean free path of a nucleon in nuclear matter must be somewhat larger than the nuclear dimensions in order to allow the use of the independent particle model. This requirement seems to be in contradiction to the assumptions made in the theory ... We are facing here one of the fundamental problems of nuclear structure physics which has yet to be solved.

— John Markus Blatt and Victor Weisskopf, *Theoretical nuclear physics* (1952)

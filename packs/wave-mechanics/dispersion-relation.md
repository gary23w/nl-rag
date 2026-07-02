---
title: "Dispersion relation"
source: https://en.wikipedia.org/wiki/Dispersion_relation
domain: wave-mechanics
license: CC-BY-SA-4.0
tags: wave equation, dispersion relation, group velocity, wave packet
fetched: 2026-07-02
---

# Dispersion relation

In the physical sciences and electrical engineering, **dispersion relations** describe the effect of dispersion on the properties of waves in a medium. A dispersion relation relates the wavelength or wavenumber of a wave to its frequency. Given the dispersion relation, one can calculate the frequency-dependent phase velocity and group velocity of each sinusoidal component of a wave in the medium, as a function of frequency. In addition to the geometry-dependent and material-dependent dispersion relations, the overarching Kramers–Kronig relations describe the frequency-dependence of wave propagation and attenuation.

Dispersion may be caused either by geometric boundary conditions (waveguides, shallow water) or by interaction of the waves with the transmitting medium. Elementary particles, considered as matter waves, have a nontrivial dispersion relation, even in the absence of geometric constraints and other media.

In the presence of dispersion, a wave does not propagate with an unchanging waveform, giving rise to the distinct frequency-dependent phase velocity and group velocity.

## Dispersion

Dispersion occurs when sinusoidal waves of different wavelengths have different propagation velocities, so that a wave packet of mixed wavelengths tends to spread out in space. The speed of a plane wave, v , is a function of the wave's wavelength $\lambda$ :

$v=v(\lambda ).$

The wave's speed, wavelength, and frequency, *f*, are related by the identity

$v(\lambda )=\lambda \ f(\lambda ).$

The function $f(\lambda )$ expresses the dispersion relation of the given medium. Dispersion relations are more commonly expressed in terms of the angular frequency $\omega =2\pi f$ and wavenumber $k=2\pi /\lambda$ . Rewriting the relation above in these variables gives

$\omega (k)=v(k)\cdot k.$

where we now view *f* as a function of *k*. The use of *ω*(*k*) to describe the dispersion relation has become standard because both the phase velocity *ω*/*k* and the group velocity *dω*/*dk* have convenient representations via this function.

The plane waves being considered can be described by

$A(x,t)=A_{0}e^{2\pi i{\frac {x-vt}{\lambda }}}=A_{0}e^{i(kx-\omega t)},$

where

- *A* is the amplitude of the wave,
- *A*0 = *A*(0, 0),
- *x* is a position along the wave's direction of travel, and
- *t* is the time at which the wave is described.

## Plane waves in vacuum

Plane waves in vacuum are the simplest case of wave propagation: no geometric constraint, no interaction with a transmitting medium.

### Electromagnetic waves in vacuum

For electromagnetic waves in vacuum, the angular frequency is proportional to the wavenumber: $\omega =ck.$

This is a *linear* dispersion relation, in which case the waves are said to be **non-dispersive**. That is, the phase velocity and the group velocity are the same: $v={\frac {\omega }{k}}={\frac {d\omega }{dk}}=c,$ and thus both are equal to the speed of light in vacuum, which is frequency-independent.

### De Broglie dispersion relations

For de Broglie matter waves the frequency dispersion relation is non-linear: $\omega (k)\approx {\frac {m_{0}c^{2}}{\hbar }}+{\frac {\hbar k^{2}}{2m_{0}}}\,.$ The equation says the matter wave frequency $\omega$ in vacuum varies with wavenumber ( $k=2\pi /\lambda$ ) in the non-relativistic approximation. The variation has two parts: a constant part due to the de Broglie frequency of the rest mass ( $\hbar \omega _{0}=m_{0}c^{2}$ ) and a quadratic part due to kinetic energy.

#### Derivation

While applications of matter waves occur at non-relativistic velocity, de Broglie applied special relativity to derive his waves. Starting from the relativistic energy–momentum relation: $E^{2}=(p{\textrm {c}})^{2}+\left(m_{0}{\textrm {c}}^{2}\right)^{2}\,$ use the de Broglie relations for energy and momentum for matter waves, $E=\hbar \omega \,,\quad \mathbf {p} =\hbar \mathbf {k} \,,$ where *ω* is the angular frequency and **k** is the wavevector with magnitude |**k**| = *k*, equal to the wave number. Divide by $\hbar$ and take the square root. This gives the **relativistic frequency dispersion relation**: $\omega (k)={\sqrt {k^{2}c^{2}+\left({\frac {m_{0}c^{2}}{\hbar }}\right)^{2}}}\,.$

Practical work with matter waves occurs at non-relativistic velocity. To approximate, we pull out the rest-mass dependent frequency: $\omega ={\frac {m_{0}c^{2}}{\hbar }}{\sqrt {1+\left({\frac {\hbar k}{m_{0}c}}\right)^{2}}}\,.$

Then we see that the $\hbar /c$ factor is very small so for k not too large, we expand ${\sqrt {1+x^{2}}}\approx 1+x^{2}/2,$ and multiply: $\omega (k)\approx {\frac {m_{0}c^{2}}{\hbar }}+{\frac {\hbar k^{2}}{2m_{0}}}\,.$ This gives the non-relativistic approximation discussed above. If we start with the non-relativistic Schrödinger equation we will end up without the first, rest mass, term.

| *Animation:* phase and group velocity of electrons |
|---|
| This animation portrays the de Broglie phase and group velocities (in slow motion) of three free electrons traveling over a field 0.4 ångströms in width. The momentum per unit mass (proper velocity) of the middle electron is lightspeed, so that its group velocity is 0.707 *c*. The top electron has twice the momentum, while the bottom electron has half. Note that as the momentum increases, the phase velocity decreases down to *c*, whereas the group velocity increases up to *c*, until the wave packet and its phase maxima move together near the speed of light, whereas the wavelength continues to decrease without bound. Both transverse and longitudinal coherence widths (packet sizes) of such high energy electrons in the lab may be orders of magnitude larger than the ones shown here. |

## Frequency versus wavenumber

As mentioned above, when the focus in a medium is on refraction rather than absorption—that is, on the real part of the refractive index—it is common to refer to the functional dependence of angular frequency on wavenumber as the *dispersion relation*. For particles, this translates to a knowledge of energy as a function of momentum.

### Waves and optics

The name "dispersion relation" originally comes from optics. It is possible to make the effective speed of light dependent on wavelength by making light pass through a material which has a non-constant index of refraction, or by using light in a non-uniform medium such as a waveguide. In this case, the waveform will spread over time, such that a narrow pulse will become an extended pulse, i.e., be dispersed. In these materials, ${\frac {\partial \omega }{\partial k}}$ is known as the group velocity and corresponds to the speed at which the peak of the pulse propagates, a value different from the phase velocity.

### Deep water waves

The dispersion relation for deep water waves is often written as

$\omega ={\sqrt {gk}},$

where *g* is the acceleration due to gravity. Deep water, in this respect, is commonly denoted as the case where the water depth is larger than half the wavelength. In this case the phase velocity is

$v_{p}={\frac {\omega }{k}}={\sqrt {\frac {g}{k}}},$

and the group velocity is

$v_{g}={\frac {d\omega }{dk}}={\frac {1}{2}}v_{p}.$

### Waves on a string

For an ideal string, the dispersion relation can be written as

$\omega =k{\sqrt {\frac {T}{\mu }}},$

where *T* is the tension force in the string, and *μ* is the string's mass per unit length. As for the case of electromagnetic waves in vacuum, ideal strings are thus a non-dispersive medium, i.e. the phase and group velocities are equal and independent (to first order) of vibration frequency.

For a nonideal string, where stiffness is taken into account, the dispersion relation is written as

$\omega ^{2}={\frac {T}{\mu }}k^{2}+\alpha k^{4},$

where $\alpha$ is a constant that depends on the string.

### Electron band structure

In the study of solids, the study of the dispersion relation of electrons is of paramount importance. The periodicity of crystals means that many levels of energy are possible for a given momentum and that some energies might not be available at any momentum. The collection of all possible energies and momenta is known as the band structure of a material. Properties of the band structure define whether the material is an insulator, semiconductor or conductor.

### Phonons

Phonons are to sound waves in a solid what photons are to light: they are the quanta that carry it. The dispersion relation of phonons is also non-trivial and important, being directly related to the acoustic and thermal properties of a material. For most systems, the phonons can be categorized into two main types: those whose bands become zero at the center of the Brillouin zone are called acoustic phonons, since they correspond to classical sound in the limit of long wavelengths. The others are optical phonons, since they can be excited by electromagnetic radiation.

### Electron optics

With high-energy (e.g., 200 keV, 32 fJ) electrons in a transmission electron microscope, the energy dependence of higher-order Laue zone (HOLZ) lines in convergent beam electron diffraction (CBED) patterns allows one, in effect, to *directly image* cross-sections of a crystal's three-dimensional dispersion surface. This dynamical effect has found application in the precise measurement of lattice parameters, beam energy, and more recently for the electronics industry: lattice strain.

## History

Isaac Newton studied refraction in prisms but failed to recognize the material dependence of the dispersion relation, dismissing the work of another researcher whose measurement of a prism's dispersion did not match Newton's own.

Dispersion of waves on water was studied by Pierre-Simon Laplace in 1776.

The universality of the Kramers–Kronig relations (1926–27) became apparent with subsequent papers on the dispersion relation's connection to causality in the scattering theory of all types of waves and particles.

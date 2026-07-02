---
title: "Stimulated emission"
source: https://en.wikipedia.org/wiki/Stimulated_emission
domain: laser-physics
license: CC-BY-SA-4.0
tags: laser physics, stimulated emission, population inversion, optical cavity
fetched: 2026-07-02
---

# Stimulated emission

**Stimulated emission** is the process by which an incoming photon of a specific frequency can interact with an excited atomic electron (or other excited molecular state), causing it to drop to a lower energy level. The liberated energy transfers to the electromagnetic field, creating a new photon with a frequency, polarization, and direction of travel that are all identical to the photons of the incident wave. This is in contrast to spontaneous emission, which occurs at a characteristic rate for each of the atoms/oscillators in the upper energy state regardless of the external electromagnetic field.

The phenomenon of stimulated emission was predicted by Albert Einstein in 1916, introducing what is now called the Einstein B Coefficient. Einstein's work became the theoretical foundation of the maser and the laser. The process is identical in form to atomic absorption in which the energy of an absorbed photon causes an identical but opposite atomic transition: from the lower level to a higher energy level.

## Overview

Stimulated emission occurs when an atom in an excited state an interacts with an electromagnetic field. If the difference in energy between the excited state and a lower energy state matches the energy of occupied modes in the field, a photon can be emitted that matches the field photons in phase, energy, and polarization. Schematically, for an atom with two energy levels, the process is shown below:

Stimulated emission requires an electromagnetic field. The reverse process is absorption which consumes a photon from the field to raise the energy level of the atom, creating an excited state. In the absence of a field, the excited state will decay and emit a photon in a random process called "spontaneous emission". This is the mechanism of fluorescence and thermal emission.

## History

Stimulated emission was a theoretical discovery by Albert Einstein within the framework of the old quantum theory, wherein the emission is described in terms of photons that are the quanta of the EM field. Einstein published a series of three papers on this topic. The key work was his 1917 paper which introduced spontaneous and stimulated emission, as well as the Einstein coefficients. Einstein's theory of radiation was ahead of its time and prefigures the modern theory of quantum electrodynamics and quantum optics by several decades.

## Einstein's quantum radiation model

Stimulated emission can be modelled mathematically by considering an atom that may be in one of two electronic energy states, a lower level state (possibly the ground state) (1) and an *excited state* (2), with energies *E*1 and *E*2 respectively.

If the atom is in the excited state, it may decay into the lower state by the process of spontaneous emission, releasing the difference in energies between the two states as a photon. The photon will have frequency *ν*0 and energy *hν*0, given by: $E_{2}-E_{1}=h\,\nu _{0}$ where *h* is the Planck constant.

Alternatively, if the excited-state atom is perturbed by an electric field of frequency *ν*0, it may emit an additional photon of the same frequency and in phase, thus augmenting the external field, leaving the atom in the lower energy state. This process is known as stimulated emission.

In a group of such atoms, if the number of atoms in the excited state is given by *N*2, the rate at which stimulated emission occurs is given by ${\frac {\partial N_{2}}{\partial t}}=-{\frac {\partial N_{1}}{\partial t}}=-B_{21}\,\rho (\nu )\,N_{2}$ where the proportionality constant *B*21 is known as the *Einstein B coefficient* for that particular transition, and *ρ*(*ν*) is the radiation density of the incident field at frequency *ν*. The rate of emission is thus proportional to the number of atoms in the excited state *N*2, and to the density of incident photons.

At the same time, there will be a process of atomic absorption which *removes* energy from the field while raising electrons from the lower state to the upper state. Its rate is precisely the negative of the stimulated emission rate, ${\frac {\partial N_{2}}{\partial t}}=-{\frac {\partial N_{1}}{\partial t}}=B_{12}\,\rho (\nu )\,N_{1}.$ The rate of absorption is thus proportional to the number of atoms in the lower state, *N*1.

In his 1917 derivation of Planck's law, Einstein show that the high temperature limit requires that the stimulated-emission and absorption rates are the same (assuming identical degeneracy weights): $B_{12}=B_{21}.$ and furthermore the Wien distribution law requires that the spontaneous emission rate is proportional to the stimulated emission rate: ${\frac {A_{ba}}{B_{ba}}}\propto \nu ^{3},\ (h\nu \gg kT)$

## Calculating the coefficients

The B coefficients can be calculated using dipole approximation and time dependent perturbation theory in quantum mechanics as: $B_{ab}={\frac {e^{2}}{6\epsilon _{0}\hbar ^{2}}}|\langle a|{\vec {r}}|b\rangle |^{2}$ where *B* corresponds to energy distribution in terms of frequency *ν*. The B coefficient may vary based on choice of energy distribution function used, however, the product of energy distribution function and its respective *B* coefficient remains same.

## Properties

The notable characteristic of stimulated emission compared to everyday light sources (which depend on spontaneous emission) is that the emitted photons have the same frequency, phase, polarization, and direction of propagation as the incident photons. The photons involved are thus mutually coherent. The two photons are completely indistinguishable particles and can be considered "cloned biphotons". These photons are not entangled. When a population inversion ( $\Delta N>0$ ) is present, therefore, optical amplification of incident radiation will take place.

## Spectral line shape

Although energy generated by stimulated emission is always at the exact frequency of the field which has stimulated it, the above rate equation refers only to excitation at the particular optical frequency $\nu _{0}$ corresponding to the energy of the transition. At frequencies offset from $\nu _{0}$ the strength of stimulated (or spontaneous) emission will be decreased according to the so-called line shape. Considering only homogeneous broadening affecting an atomic or molecular resonance, the spectral line shape function is described as a Lorentzian distribution $g'(\nu )={1 \over \pi }{(\Gamma /2) \over (\nu -\nu _{0})^{2}+(\Gamma /2)^{2}}$ where $\Gamma$ is the full width at half maximum or FWHM bandwidth.

The peak value of the Lorentzian line shape occurs at the line center, $\nu =\nu _{0}$ . A line shape function can be normalized so that its value at $\nu _{0}$ is unity; in the case of a Lorentzian we obtain $g(\nu )={g'(\nu ) \over g'(\nu _{0})}={(\Gamma /2)^{2} \over (\nu -\nu _{0})^{2}+(\Gamma /2)^{2}}.$

Thus stimulated emission at frequencies away from $\nu _{0}$ is reduced by this factor. In practice there may also be broadening of the line shape due to inhomogeneous broadening, most notably due to the Doppler effect resulting from the distribution of velocities in a gas at a certain temperature. This has a Gaussian shape and reduces the peak strength of the line shape function. In a practical problem the full line shape function can be computed through a convolution of the individual line shape functions involved. Therefore, optical amplification will add power to an incident optical field at frequency $\nu$ at a rate given by $P=h\nu \,g(\nu )\,B_{21}\,\rho (\nu )\,\Delta N.$

## Stimulated emission cross section

The stimulated emission cross section is $\sigma _{21}(\nu )=A_{21}{\frac {\lambda ^{2}}{8\pi n^{2}}}g'(\nu )$ where

- *A*21 is the Einstein *A* coefficient,
- *λ* is the wavelength in vacuum,
- *n* is the refractive index of the medium (dimensionless), and
- *g*′(*ν*) is the spectral line shape function.

## Classical model

Stimulated emission can also occur in classical models, without reference to photons or quantum-mechanics. The classical electromagnetic field interacts with a classical medium and increases its energy (absorption) or decreases its energy (stimulated emission).

## Optical amplification

Stimulated emission can provide a physical mechanism for optical amplification. If an external source of energy stimulates more than 50% of the atoms in the ground state to transition into the excited state, then what is called a population inversion is created. When light of the appropriate frequency passes through the inverted medium, the photons are either absorbed by the atoms that remain in the ground state or the photons stimulate the excited atoms to emit additional photons of the same frequency, phase, and direction. Since more atoms are in the excited state than in the ground state then an amplification of the input intensity results.

The population inversion, in units of atoms per cubic metre, is

$\Delta N_{21}=N_{2}-{g_{2} \over g_{1}}N_{1}$

where *g*1 and *g*2 are the degeneracies of energy levels 1 and 2, respectively.

### Small signal gain equation

The intensity (in watts per square metre) of the stimulated emission is governed by the following differential equation:

${dI \over dz}=\sigma _{21}(\nu )\cdot \Delta N_{21}\cdot I(z)$

as long as the intensity *I*(*z*) is small enough so that it does not have a significant effect on the magnitude of the population inversion. Grouping the first two factors together, this equation simplifies as

${dI \over dz}=\gamma _{0}(\nu )\cdot I(z)$

where

$\gamma _{0}(\nu )=\sigma _{21}(\nu )\cdot \Delta N_{21}$

is the *small-signal gain coefficient* (in units of radians per metre). We can solve the differential equation using separation of variables:

${dI \over I(z)}=\gamma _{0}(\nu )\cdot dz$

Integrating, we find:

$\ln \left({I(z) \over I_{in}}\right)=\gamma _{0}(\nu )\cdot z$

or

$I(z)=I_{in}e^{\gamma _{0}(\nu )z}$

where

$I_{in}=I(z=0)\,$

is the optical intensity of the input signal (in watts per square metre).

### Saturation intensity

The saturation intensity *I*S is defined as the input intensity at which the gain of the optical amplifier drops to exactly half of the small-signal gain. We can compute the saturation intensity as

$I_{S}={h\nu \over \sigma (\nu )\cdot \tau _{S}}$

where

h

is the

Planck constant

, and

$\tau _{\text{S}}$

is the saturation

time constant

, which depends on the spontaneous emission lifetimes of the various transitions between the energy levels related to the amplification.

$\nu$

is the frequency in Hz

The minimum value of $I_{\text{S}}(\nu )$ occurs on resonance, where the cross section $\sigma (\nu )$ is the largest. This minimum value is:

$I_{\text{sat}}={\frac {\pi }{3}}{hc \over \lambda ^{3}\tau _{S}}$

For a simple two-level atom with a natural linewidth $\Gamma$ , the saturation time constant $\tau _{\text{S}}=\Gamma ^{-1}$ .

### General gain equation

The general form of the gain equation, which applies regardless of the input intensity, derives from the general differential equation for the intensity *I* as a function of position *z* in the gain medium:

${dI \over dz}={\gamma _{0}(\nu ) \over 1+{\bar {g}}(\nu ){I(z) \over I_{S}}}\cdot I(z)$

where $I_{S}$ is saturation intensity. To solve, we first rearrange the equation in order to separate the variables, intensity *I* and position *z*:

${dI \over I(z)}\left[1+{\bar {g}}(\nu ){I(z) \over I_{S}}\right]=\gamma _{0}(\nu )\cdot dz$

Integrating both sides, we obtain

$\ln \left({I(z) \over I_{in}}\right)+{\bar {g}}(\nu ){I(z)-I_{in} \over I_{S}}=\gamma _{0}(\nu )\cdot z$

or

$\ln \left({I(z) \over I_{in}}\right)+{\bar {g}}(\nu ){I_{in} \over I_{S}}\left({I(z) \over I_{in}}-1\right)=\gamma _{0}(\nu )\cdot z$

The gain *G* of the amplifier is defined as the optical intensity *I* at position *z* divided by the input intensity:

$G=G(z)={I(z) \over I_{in}}$

Substituting this definition into the prior equation, we find the **general gain equation**:

$\ln \left(G\right)+{\bar {g}}(\nu ){I_{in} \over I_{S}}\left(G-1\right)=\gamma _{0}(\nu )\cdot z$

### Small signal approximation

In the special case where the input signal is small compared to the saturation intensity, in other words,

$I_{in}\ll I_{S}\,$

then the general gain equation gives the small signal gain as

$\ln(G)=\ln(G_{0})=\gamma _{0}(\nu )\cdot z$

or

$G=G_{0}=e^{\gamma _{0}(\nu )z}$

which is identical to the small signal gain equation (see above).

### Large signal asymptotic behaviour

For large input signals, where

$I_{in}\gg I_{S}\,$

the gain approaches unity

$G\rightarrow 1$

and the general gain equation approaches a linear asymptote:

$I(z)=I_{in}+{\gamma _{0}(\nu )\cdot z \over {\bar {g}}(\nu )}I_{S}$

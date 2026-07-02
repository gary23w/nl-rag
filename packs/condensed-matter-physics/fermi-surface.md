---
title: "Fermi surface"
source: https://en.wikipedia.org/wiki/Fermi_surface
domain: condensed-matter-physics
license: CC-BY-SA-4.0
tags: condensed matter physics, crystal structure, electronic band structure, fermi surface
fetched: 2026-07-02
---

# Fermi surface

In condensed matter physics, the **Fermi surface** is the surface in reciprocal space which separates occupied electron states from unoccupied electron states at zero temperature. The shape of the Fermi surface is derived from the periodicity and symmetry of the crystalline lattice and from the occupation of electronic energy bands. The existence of a Fermi surface is a direct consequence of the Pauli exclusion principle, which allows a maximum of one electron per quantum state. The study of the Fermi surfaces of materials is called **fermiology**.

## Theory

Consider a spin-less ideal Fermi gas of N particles. According to Fermi–Dirac statistics, the mean occupation number of a state with energy $\epsilon _{i}$ is given by

$\langle n_{i}\rangle ={\frac {1}{e^{(\epsilon _{i}-\mu )/k_{\rm {B}}T}+1}},$

where

- $\left\langle n_{i}\right\rangle$ is the mean occupation number of the i th state
- $\epsilon _{i}$ is the kinetic energy of the i th state
- $\mu$ is the chemical potential (at zero temperature, this is the maximum kinetic energy the particle can have, i.e. Fermi energy $E_{\rm {F}}$ )
- T is the absolute temperature
- $k_{\rm {B}}$ is the Boltzmann constant

Suppose we consider the limit $T\to 0$ . Then we have,

$\left\langle n_{i}\right\rangle \to {\begin{cases}1&(\epsilon _{i}<\mu )\\0&(\epsilon _{i}>\mu )\end{cases}}.$

By the Pauli exclusion principle, no two fermions can be in the same state. Additionally, at zero temperature the enthalpy of the electrons must be minimal, meaning that they cannot change state. If, for a particle in some state, there existed an unoccupied lower state that it could occupy, then the energy difference between those states would give the electron an additional enthalpy. Hence, the enthalpy of the electron would not be minimal. Therefore, at zero temperature all the lowest energy states must be saturated. For a large ensemble the Fermi level will be approximately equal to the chemical potential of the system, and hence every state below this energy must be occupied. Thus, particles fill up all energy levels below the Fermi level at absolute zero, which is equivalent to saying that is the energy level below which there are exactly N states.

In momentum space, these particles fill up a ball of radius $k_{\rm {F}}$ , the surface of which is called the Fermi surface.

The linear response of a metal to an electric, magnetic, or thermal gradient is determined by the shape of the Fermi surface, because currents are due to changes in the occupancy of states near the Fermi energy. In reciprocal space, the Fermi surface of an ideal Fermi gas is a sphere of radius

$k_{\rm {F}}={\frac {p_{\rm {F}}}{\hbar }}={\frac {\sqrt {2mE_{\rm {F}}}}{\hbar }}$

,

determined by the valence electron concentration where $\hbar$ is the reduced Planck constant. A material whose Fermi level falls in a gap between bands is an insulator or semiconductor depending on the size of the bandgap. When a material's Fermi level falls in a bandgap, there is no Fermi surface.

Materials with complex crystal structures can have quite intricate Fermi surfaces. **Figure 2** illustrates the anisotropic Fermi surface of graphite, which has both electron and hole pockets in its Fermi surface due to multiple bands crossing the Fermi energy along the $\mathbf {k} _{z}$ direction. Often in a metal, the Fermi surface radius $k_{\rm {F}}$ is larger than the size of the first Brillouin zone, which results in a portion of the Fermi surface lying in the second (or higher) zones. As with the band structure itself, the Fermi surface can be displayed in an extended-zone scheme where $\mathbf {k}$ is allowed to have arbitrarily large values or a reduced-zone scheme where wavevectors are shown modulo ${\textstyle {\frac {2\pi }{a}}}$ (in the 1-dimensional case) where a is the lattice constant. In the three-dimensional case the reduced zone scheme means that from any wavevector $\mathbf {k}$ there is an appropriate number of reciprocal lattice vectors $\mathbf {K}$ subtracted that the new $\mathbf {k}$ now is closer to the origin in $\mathbf {k}$ -space than to any $\mathbf {K}$ . Solids with a large density of states at the Fermi level become unstable at low temperatures and tend to form ground states where the condensation energy comes from opening a gap at the Fermi surface. Examples of such ground states are superconductors, ferromagnets, Jahn–Teller distortions and spin density waves.

The state occupancy of fermions like electrons is governed by Fermi–Dirac statistics so at finite temperatures the Fermi surface is accordingly broadened. In principle all fermion energy level populations are bound by a Fermi surface although the term is not generally used outside of condensed-matter physics.

## Experimental determination

Electronic Fermi surfaces have been measured through observation of the oscillation of transport properties in magnetic fields H , for example the de Haas–van Alphen effect (dHvA) and the Shubnikov–de Haas effect (SdH). The former is an oscillation in magnetic susceptibility and the latter in resistivity. The oscillations are periodic versus $1/H$ and occur because of the quantization of energy levels in the plane perpendicular to a magnetic field, a phenomenon first predicted by Lev Landau. The new states are called Landau levels and are separated by an energy $\hbar \omega _{\rm {c}}$ where $\omega _{\rm {c}}=eH/m^{*}c$ is called the cyclotron frequency, e is the electronic charge, $m^{*}$ is the electron effective mass and c is the speed of light. In a famous result, Lars Onsager proved that the period of oscillation $\Delta H$ is related to the cross-section of the Fermi surface (typically given in Å−2) perpendicular to the magnetic field direction $A_{\perp }$ by the equation

> $A_{\perp }={\frac {2\pi e\Delta H}{\hbar c}}$ .

Thus the determination of the periods of oscillation for various applied field directions allows mapping of the Fermi surface. Observation of the dHvA and SdH oscillations requires magnetic fields large enough that the circumference of the cyclotron orbit is smaller than a mean free path. Therefore, dHvA and SdH experiments are usually performed at high-field facilities like the High Field Magnet Laboratory in Netherlands, Grenoble High Magnetic Field Laboratory in France, the Tsukuba Magnet Laboratory in Japan or the National High Magnetic Field Laboratory in the United States.

The most direct experimental technique to resolve the electronic structure of crystals in the momentum-energy space (see reciprocal lattice), and, consequently, the Fermi surface, is the angle-resolved photoemission spectroscopy (ARPES). An example of the Fermi surface of superconducting cuprates measured by ARPES is shown in **Figure 3**.

### Measurement using ACAR

With positron annihilation it is also possible to determine the Fermi surface as the annihilation process conserves the momentum of the initial particle. Since a positron in a solid will thermalize prior to annihilation, the annihilation radiation carries the information about the electron momentum. The corresponding experimental technique is called Angular Correlation of electron-positron Annihilation Radiation (ACAR) as it measures the angular deviation from 180° of both annihilation quanta. In this way it is possible to probe the electron momentum density of a solid and determine the Fermi surface. Furthermore, using spin polarized positrons, the momentum distribution for the two spin states in magnetized materials can be obtained.

ACAR has many advantages and disadvantages compared to other experimental techniques: It does not rely on UHV conditions, cryogenic temperatures, high magnetic fields or fully ordered alloys. However, ACAR needs samples with a low vacancy concentration as they act as effective traps for positrons. In this way, the first determination of a *smeared Fermi surface* in a 30% alloy was obtained in 1978.

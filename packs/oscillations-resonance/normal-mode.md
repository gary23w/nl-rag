---
title: "Normal mode"
source: https://en.wikipedia.org/wiki/Normal_mode
domain: oscillations-resonance
license: CC-BY-SA-4.0
tags: harmonic oscillator, simple harmonic motion, damped oscillation, normal mode
fetched: 2026-07-02
---

# Normal mode

A **normal mode** of a dynamical system is a pattern of motion in which all parts of the system move sinusoidally with the same frequency and with a fixed phase relation. The free motion described by the normal modes takes place at fixed frequencies. These fixed frequencies of the normal modes of a system are known as its natural frequencies or resonant frequencies. A physical object, such as a building, bridge, or molecule, has a set of normal modes and their natural frequencies that depend on its structure, materials and boundary conditions.

The most general motion of a linear system is a superposition of its normal modes. The modes are "normal" in the sense that they move independently. An excitation of one mode will never cause excitation of a different mode. In mathematical terms, normal modes are orthogonal to each other.

## General definitions

### Mode

In the wave theory of physics and engineering, a **mode** in a dynamical system is a standing wave state of excitation, in which all the components of the system will be affected sinusoidally at a fixed frequency associated with that mode.

Because no real system can perfectly fit under the standing wave framework, the *mode* concept is taken as a general characterization of specific states of oscillation, thus treating the dynamic system in a *linear* fashion, in which linear superposition of states can be performed.

Typical examples include:

- In a mechanical dynamical system, a vibrating rope is the most clear example of a mode, in which the rope is the medium, the stress on the rope is the excitation, and the displacement of the rope with respect to its static state is the modal variable.
- In an acoustic dynamical system, a single sound pitch is a mode, in which the air is the medium, the sound pressure in the air is the excitation, and the displacement of the air molecules is the modal variable.
- In a structural dynamical system, a high tall building oscillating under its most flexural axis is a mode, in which all the material of the building -under the proper numerical simplifications- is the medium, the seismic/wind/environmental solicitations are the excitations and the displacements are the modal variable.
- In an electrical dynamical system, a resonant cavity made of thin metal walls, enclosing a hollow space, for a particle accelerator is a pure standing wave system, and thus an example of a mode, in which the hollow space of the cavity is the medium, the RF source (a Klystron or another RF source) is the excitation and the electromagnetic field is the modal variable.
- When relating to music, normal modes of vibrating instruments (strings, air pipes, drums, etc.) are called "overtones".

The concept of normal modes also finds application in other dynamical systems, such as optics, quantum mechanics, atmospheric dynamics and molecular dynamics.

Most dynamical systems can be excited in several modes, possibly simultaneously. Each mode is characterized by one or several frequencies, according to the modal variable field. For example, a vibrating rope in 2D space is defined by a single-frequency (1D axial displacement), but a vibrating rope in 3D space is defined by two frequencies (2D axial displacement).

For a given amplitude on the modal variable, each mode will store a specific amount of energy because of the sinusoidal excitation.

The *normal* or *dominant* mode of a system with multiple modes will be the mode storing the minimum amount of energy for a given amplitude of the modal variable, or, equivalently, for a given stored amount of energy, the dominant mode will be the mode imposing the maximum amplitude of the modal variable.

### Mode numbers

A mode of vibration is characterized by a modal frequency and a mode shape. It is numbered according to the number of half waves in the vibration. For example, if a vibrating beam with both ends pinned displayed a mode shape of half of a sine wave (one peak on the vibrating beam) it would be vibrating in mode 1. If it had a full sine wave (one peak and one trough) it would be vibrating in mode 2.

In a system with two or more dimensions, such as the pictured disk, each dimension is given a mode number. Using polar coordinates, we have a radial coordinate and an angular coordinate. If one measured from the center outward along the radial coordinate one would encounter a full wave, so the mode number in the radial direction is 2. The other direction is trickier, because only half of the disk is considered due to the anti-symmetric (also called skew-symmetry) nature of a disk's vibration in the angular direction. Thus, measuring 180° along the angular direction you would encounter a half wave, so the mode number in the angular direction is 1. So the mode number of the system is 2–1 or 1–2, depending on which coordinate is considered the "first" and which is considered the "second" coordinate (so it is important to always indicate which mode number matches with each coordinate direction).

In linear systems each mode is entirely independent of all other modes. In general all modes have different frequencies (with lower modes having lower frequencies) and different mode shapes.

### Nodes

In a one-dimensional system at a given mode the vibration will have nodes, or places where the displacement is always zero. These nodes correspond to points in the mode shape where the mode shape is zero. Since the vibration of a system is given by the mode shape multiplied by a time function, the displacement of the node points remain zero at all times.

When expanded to a two dimensional system, these nodes become lines where the displacement is always zero. If you watch the animation above you will see two circles (one about halfway between the edge and center, and the other on the edge itself) and a straight line bisecting the disk, where the displacement is close to zero. In an idealized system these lines equal zero exactly, as shown to the right.

## In mechanical systems

In the analysis of conservative systems with small displacements from equilibrium, important in acoustics, molecular spectra, and electrical circuits, the system can be transformed to new coordinates called **normal coordinates.** Each normal coordinate corresponds to a single vibrational frequency of the system and the corresponding motion of the system is called the normal mode of vibration.

### Coupled oscillators

Consider two equal bodies (not affected by gravity), each of mass m, attached to three springs, each with spring constant k. They are attached in the following manner, forming a system that is physically symmetric:

where the edge points are fixed and cannot move. Let *x*1(*t*) denote the horizontal displacement of the left mass, and *x*2(*t*) denote the displacement of the right mass.

Denoting acceleration (the second derivative of *x*(*t*) with respect to time) as ${\textstyle {\ddot {x}}}$ , the equations of motion are:

${\begin{aligned}m{\ddot {x}}_{1}&=-kx_{1}+k(x_{2}-x_{1})=-2kx_{1}+kx_{2}\\m{\ddot {x}}_{2}&=-kx_{2}+k(x_{1}-x_{2})=-2kx_{2}+kx_{1}\end{aligned}}$

Since we expect oscillatory motion of a normal mode (where ω is the same for both masses), we try:

${\begin{aligned}x_{1}(t)&=A_{1}e^{i\omega t}\\x_{2}(t)&=A_{2}e^{i\omega t}\end{aligned}}$

Substituting these into the equations of motion gives us:

${\begin{aligned}-\omega ^{2}mA_{1}e^{i\omega t}&=-2kA_{1}e^{i\omega t}+kA_{2}e^{i\omega t}\\-\omega ^{2}mA_{2}e^{i\omega t}&=kA_{1}e^{i\omega t}-2kA_{2}e^{i\omega t}\end{aligned}}$

Omitting the exponential factor (because it is common to all terms) and simplifying yields:

${\begin{aligned}(\omega ^{2}m-2k)A_{1}+kA_{2}&=0\\kA_{1}+(\omega ^{2}m-2k)A_{2}&=0\end{aligned}}$

And in matrix representation:

${\begin{bmatrix}\omega ^{2}m-2k&k\\k&\omega ^{2}m-2k\end{bmatrix}}{\begin{pmatrix}A_{1}\\A_{2}\end{pmatrix}}=0$

If the matrix on the left is invertible, the unique solution is the trivial solution (*A*1, *A*2) = (*x*1, *x*2) = (0, 0). The non trivial solutions are to be found for those values of ω whereby the matrix on the left is singular; i.e. is not invertible. It follows that the determinant of the matrix must be equal to 0, so:

$(\omega ^{2}m-2k)^{2}-k^{2}=0$

Solving for ω, the two positive solutions are:

${\begin{aligned}\omega _{1}&={\sqrt {\frac {k}{m}}}\\\omega _{2}&={\sqrt {\frac {3k}{m}}}\end{aligned}}$

Substituting *ω*1 into the matrix and solving for (*A*1, *A*2), yields (1, 1). Substituting *ω*2 results in (1, −1). (These vectors are eigenvectors, and the frequencies are eigenvalues.)

The first normal mode is: ${\vec {\eta }}_{1}={\begin{pmatrix}x_{1}^{1}(t)\\x_{2}^{1}(t)\end{pmatrix}}=c_{1}{\begin{pmatrix}1\\1\end{pmatrix}}\cos {(\omega _{1}t+\varphi _{1})}$

Which corresponds to both masses moving in the same direction at the same time. This mode is called antisymmetric.

The second normal mode is:

${\vec {\eta }}_{2}={\begin{pmatrix}x_{1}^{2}(t)\\x_{2}^{2}(t)\end{pmatrix}}=c_{2}{\begin{pmatrix}1\\-1\end{pmatrix}}\cos {(\omega _{2}t+\varphi _{2})}$

This corresponds to the masses moving in the opposite directions, while the center of mass remains stationary. This mode is called symmetric.

The general solution is a superposition of the **normal modes** where *c*1, *c*2, *φ*1, and *φ*2 are determined by the initial conditions of the problem.

The process demonstrated here can be generalized and formulated using the formalism of Lagrangian mechanics or Hamiltonian mechanics.

### Standing waves

A standing wave is a continuous form of normal mode. In a standing wave, all the space elements (i.e. (*x*, *y*, *z*) coordinates) are oscillating in the same frequency and in phase (reaching the equilibrium point together), but each has a different amplitude.

The general form of a standing wave is:

$\Psi (t)=f(x,y,z)(A\cos(\omega t)+B\sin(\omega t))$

where *f*(*x*, *y*, *z*) represents the dependence of amplitude on location and the cosine/sine are the oscillations in time.

Physically, standing waves are formed by the interference (superposition) of waves and their reflections (although one may also say the opposite; that a moving wave is a superposition of standing waves). The geometric shape of the medium determines what would be the interference pattern, thus determines the *f*(*x*, *y*, *z*) form of the standing wave. This space-dependence is called a **normal mode**.

Usually, for problems with continuous dependence on (*x*, *y*, *z*) there is no single or finite number of normal modes, but there are infinitely many normal modes. If the problem is bounded (i.e. it is defined on a finite section of space) there are countably many normal modes (usually numbered *n* = 1, 2, 3, ...). If the problem is not bounded, there is a continuous spectrum of normal modes.

### Elastic solids

In any solid at any temperature, the primary particles (e.g. atoms or molecules) are not stationary, but rather vibrate about mean positions. In insulators the capacity of the solid to store thermal energy is due almost entirely to these vibrations. Many physical properties of the solid (e.g. modulus of elasticity) can be predicted given knowledge of the frequencies with which the particles vibrate. The simplest assumption (by Einstein) is that all the particles oscillate about their mean positions with the same natural frequency ν. This is equivalent to the assumption that all atoms vibrate independently with a frequency ν. Einstein also assumed that the allowed energy states of these oscillations are harmonics, or integral multiples of hν. The spectrum of waveforms can be described mathematically using a Fourier series of sinusoidal density fluctuations (or thermal phonons).

Debye subsequently recognized that each oscillator is intimately coupled to its neighboring oscillators at all times. Thus, by replacing Einstein's identical uncoupled oscillators with the same number of coupled oscillators, Debye correlated the elastic vibrations of a one-dimensional solid with the number of mathematically special modes of vibration of a stretched string (see figure). The pure tone of lowest pitch or frequency is referred to as the fundamental and the multiples of that frequency are called its harmonic overtones. He assigned to one of the oscillators the frequency of the fundamental vibration of the whole block of solid. He assigned to the remaining oscillators the frequencies of the harmonics of that fundamental, with the highest of all these frequencies being limited by the motion of the smallest primary unit.

The normal modes of vibration of a crystal are in general superpositions of many overtones, each with an appropriate amplitude and phase. Longer wavelength (low frequency) phonons are exactly those acoustical vibrations which are considered in the theory of sound. Both longitudinal and transverse waves can be propagated through a solid, while, in general, only longitudinal waves are supported by fluids.

In the longitudinal mode, the displacement of particles from their positions of equilibrium coincides with the propagation direction of the wave. Mechanical longitudinal waves have been also referred to as **compression waves**. For transverse modes, individual particles move perpendicular to the propagation of the wave.

According to quantum theory, the mean energy of a normal vibrational mode of a crystalline solid with characteristic frequency ν is:

$E(\nu )={\frac {1}{2}}h\nu +{\frac {h\nu }{e^{h\nu /kT}-1}}$

The term (1/2)*hν* represents the "zero-point energy", or the energy which an oscillator will have at absolute zero. *E*(*ν*) tends to the classic value kT at high temperatures

$E(\nu )=kT\left[1+{\frac {1}{12}}\left({\frac {h\nu }{kT}}\right)^{2}+O\left({\frac {h\nu }{kT}}\right)^{4}+\cdots \right]$

By knowing the thermodynamic formula,

$\left({\frac {\partial S}{\partial E}}\right)_{N,V}={\frac {1}{T}}$

the entropy per normal mode is:

${\begin{aligned}S\left(\nu \right)&=\int _{0}^{T}{\frac {d}{dT}}E\left(\nu \right){\frac {dT}{T}}\\[10pt]&={\frac {E\left(\nu \right)}{T}}-k\log \left(1-e^{-{\frac {h\nu }{kT}}}\right)\end{aligned}}$

The free energy is:

$F(\nu )=E-TS=kT\log \left(1-e^{-{\frac {h\nu }{kT}}}\right)$

which, for *kT* ≫ *hν*, tends to:

$F(\nu )=kT\log \left({\frac {h\nu }{kT}}\right)$

In order to calculate the internal energy and the specific heat, we must know the number of normal vibrational modes a frequency between the values ν and *ν* + *dν*. Allow this number to be *f*(*ν*)*dν*. Since the total number of normal modes is 3*N*, the function *f*(*ν*) is given by:

$\int f(\nu )\,d\nu =3N$

The integration is performed over all frequencies of the crystal. Then the internal energy U will be given by:

$U=\int f(\nu )E(\nu )\,d\nu$

## In quantum mechanics

Bound states in quantum mechanics are analogous to modes. The waves in quantum systems are oscillations in probability amplitude rather than material displacement. The frequency of oscillation, f, relates to the mode energy by *E* = *hf* where h is the Planck constant. Thus a system like an atom consists of a linear combination of modes of definite energy. These energies are characteristic of the particular atom. The (complex) square of the probability amplitude at a point in space gives the probability of measuring an electron at that location. The spatial distribution of this probability is characteristic of the atom.

## In seismology

Normal modes are generated in the Earth from long wavelength seismic waves from large earthquakes interfering to form standing waves.

For an elastic, isotropic, homogeneous sphere, spheroidal, toroidal and radial (or breathing) modes arise. Spheroidal modes only involve P and SV waves (like Rayleigh waves) and depend on overtone number n and angular order l but have degeneracy of azimuthal order m. Increasing l concentrates fundamental branch closer to surface and at large l this tends to Rayleigh waves. Toroidal modes only involve SH waves (like Love waves) and do not exist in fluid outer core. Radial modes are just a subset of spheroidal modes with *l* = 0. The degeneracy does not exist on Earth as it is broken by rotation, ellipticity and 3D heterogeneous velocity and density structure.

It may be assumed that each mode can be isolated, the self-coupling approximation, or that many modes close in frequency resonate, the cross-coupling approximation. Self-coupling will solely change the phase velocity and not the number of waves around a great circle, resulting in a stretching or shrinking of standing wave pattern. Modal cross-coupling occurs due to the rotation of the Earth, from aspherical elastic structure, or due to Earth's ellipticity and leads to a mixing of fundamental spheroidal and toroidal modes.

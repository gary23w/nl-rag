---
title: "Acoustic wave"
source: https://en.wikipedia.org/wiki/Acoustic_wave
domain: acoustics-physics
license: CC-BY-SA-4.0
tags: acoustic wave, standing wave, doppler effect, sound resonance
fetched: 2026-07-02
---

# Acoustic wave

**Acoustic waves** are types of mechanical waves that propagate through matter—such as gas, liquid, and/or solids—by causing the particles of the medium to displace from their equilibrium positions. These waves carry energy and are characterized by properties like acoustic pressure, particle velocity, and acoustic intensity. The speed of an acoustic wave depends on the properties of the medium it travels through and on temperature; for example, it travels at approximately 343 meters per second in air, and 1480 meters per second in water. Acoustic waves encompass a broad range of phenomena, from audible sound to seismic waves and ultrasound, finding applications in diverse fields like acoustics, engineering, and medicine.

## Wave properties

An acoustic wave is a mechanical wave that transmits energy through the movements of atoms and molecules. Acoustic waves transmit through fluids in a longitudinal manner (movement of particles are parallel to the direction of propagation of the wave); in contrast to electromagnetic waves that transmit in transverse manner (movement of particles at a right angle to the direction of propagation of the wave). However, in solids, acoustic waves transmit in both longitudinal and transverse manners due to presence of shear moduli in such a state of matter.

### Acoustic wave equation

The acoustic wave equation describes the propagation of sound waves. The acoustic wave equation for sound pressure in one dimension is given by ${\partial ^{2}p \over \partial x^{2}}-{1 \over c^{2}}{\partial ^{2}p \over \partial t^{2}}=0$ where

- p is sound pressure in Pa
- x is position in the direction of propagation of the wave, in m
- c is speed of sound in m/s
- t is time in s

The wave equation for particle velocity has the same shape and is given by ${\partial ^{2}u \over \partial x^{2}}-{1 \over c^{2}}{\partial ^{2}u \over \partial t^{2}}=0$ where

- u is particle velocity in m/s

For lossy media, more intricate models need to be applied in order to take into account frequency-dependent attenuation and phase speed. Such models include acoustic wave equations that incorporate fractional derivative terms, see also the acoustic attenuation article.

D'Alembert gave the general solution for the lossless wave equation. For sound pressure, a solution would be $p=R\cos(\omega t-kx)+(1-R)\cos(\omega t+kx)$ where

- $\omega$ is angular frequency in rad/s
- t is time in s
- k is wave number in rad·m−1
- R is a coefficient without unit

For $R=1$ the wave becomes a travelling wave moving rightwards, for $R=0$ the wave becomes a travelling wave moving leftwards. A standing wave can be obtained by $R=0.5$ .

### Phase

In a travelling wave pressure and particle velocity are in phase, which means the phase angle between the two quantities is zero.

This can be easily proven using the ideal gas law $pV=nRT$ where

- p is pressure in Pa
- V is volume in m3
- n is amount in mol
- R is the universal gas constant with value ${\textstyle 8.314\,472(15)~{\frac {\mathrm {J} }{\mathrm {mol~K} }}}$

Consider a volume V . As an acoustic wave propagates through the volume, adiabatic compression and decompression occurs. For adiabatic change the following relation between volume V of a parcel of fluid and pressure p holds ${\partial V \over V_{m}}={-1 \over \ \gamma }{\partial p \over p_{m}}$ where $\gamma$ is the adiabatic index without unit and the subscript m denotes the mean value of the respective variable.

As a sound wave propagates through a volume, the horizontal displacement of a particle $\eta$ occurs along the wave propagation direction. ${\partial \eta \over V_{m}}A={\partial V \over V_{m}}={-1 \over \ \gamma }{\partial p \over p_{m}}$ where

- A is cross-sectional area in m2

From this equation it can be seen that when pressure is at its maximum, particle displacement from average position reaches zero. As mentioned before, the oscillating pressure for a rightward traveling wave can be given by $p=p_{0}\cos(\omega t-kx)$ Since displacement is maximum when pressure is zero there is a 90 degrees phase difference, so displacement is given by $\eta =\eta _{0}\sin(\omega t-kx)$ Particle velocity is the first derivative of particle displacement: $u=\partial \eta /\partial t$ . Differentiation of a sine gives a cosine again $u=u_{0}\cos(\omega t-kx)$

During adiabatic change, temperature changes with pressure as well following ${\partial T \over T_{m}}={\gamma -1 \over \ \gamma }{\partial p \over p_{m}}$ This fact is exploited within the field of thermoacoustics.

### Propagation speed

The propagation speed, or acoustic velocity, of acoustic waves is a function of the medium of propagation. In general, the acoustic velocity *c* is given by the Newton-Laplace equation: $c={\sqrt {\frac {C}{\rho }}}$ where

- *C* is a coefficient of stiffness, the bulk modulus (or the modulus of bulk elasticity for gas mediums),
- $\rho$ is the density in kg/m3

Thus the acoustic velocity increases with the stiffness (the resistance of an elastic body to deformation by an applied force) of the material, and decreases with the density. For general equations of state, if classical mechanics is used, the acoustic velocity c is given by $c^{2}={\frac {\partial p}{\partial \rho }}$ with p as the pressure and $\rho$ the density, where differentiation is taken with respect to adiabatic change.

## Phenomena

Acoustic waves are elastic waves that exhibit phenomena like diffraction, reflection and interference. Note that sound waves in air are not polarized since they oscillate along the same direction as they move.

### Interference

Interference is the addition of two or more waves that results in a new wave pattern. Interference of sound waves can be observed when two loudspeakers transmit the same signal. At certain locations constructive interference occurs, doubling the local sound pressure. And at other locations destructive interference occurs, causing a local sound pressure of zero pascals.

### Standing wave

A standing wave is a special kind of wave that can occur in a resonator. In a resonator superposition of the incident and reflective wave occurs, causing a standing wave. Pressure and particle velocity are 90 degrees out of phase in a standing wave.

Consider a tube with two closed ends acting as a resonator. The resonator has normal modes at frequencies given by $f={\frac {Nc}{2d}}\qquad \qquad N\in \{1,2,3,\dots \}$ where

- c is the speed of sound in m/s
- d is the length of the tube in m

At the ends particle velocity becomes zero since there can be no particle displacement. Pressure however doubles at the ends because of interference of the incident wave with the reflective wave. As pressure is maximum at the ends while velocity is zero, there is a 90 degrees phase difference between them.

### Reflection

An acoustic travelling wave can be reflected by a solid surface. If a travelling wave is reflected, the reflected wave can interfere with the incident wave causing a standing wave in the near field. As a consequence, the local pressure in the near field is doubled, and the particle velocity becomes zero.

Attenuation causes the reflected wave to decrease in power as distance from the reflective material increases. As the power of the reflective wave decreases compared to the power of the incident wave, interference also decreases. And as interference decreases, so does the phase difference between sound pressure and particle velocity. At a large enough distance from the reflective material, there is no interference left anymore. At this distance one can speak of the far field.

The amount of reflection is given by the reflection coefficient which is the ratio of the reflected intensity over the incident intensity $R={\frac {p_{\text{reflected}}}{p_{\text{incident}}}}$

### Absorption

Acoustic waves can be absorbed. The amount of absorption is given by the absorption coefficient which is given by $\alpha =1-R^{2}$ where

- $\alpha$ is the absorption coefficient without a unit
- R is the reflection coefficient without a unit

Often acoustic absorption of materials is given in decibels instead.

### Layered media

When an acoustic wave propagates through a non-homogeneous medium, it will undergo diffraction at the impurities it encounters or at the interfaces between layers of different materials. This is a phenomenon very similar to that of the refraction, absorption and transmission of light in Bragg mirrors. The concept of acoustic wave propagation through periodic media is exploited with great success in acoustic metamaterial engineering.

The acoustic absorption, reflection and transmission in multilayer materials can be calculated with the transfer-matrix method.

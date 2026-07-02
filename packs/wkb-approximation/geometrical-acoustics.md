---
title: "Geometrical acoustics"
source: https://en.wikipedia.org/wiki/Geometrical_acoustics
domain: wkb-approximation
license: CC-BY-SA-4.0
tags: wkb approximation, eikonal equation, semiclassical physics, stokes phenomenon
fetched: 2026-07-02
---

# Geometrical acoustics

**Geometrical acoustics** or **ray acoustics** is a branch of acoustics that studies propagation of sound on the basis of the concept of **acoustic rays**, defined as lines along which the acoustic energy is transported. This concept is similar to geometrical optics, or ray optics, that studies light propagation in terms of optical rays. Geometrical acoustics is an approximate theory, valid in the limiting case of very small wavelengths, or very high frequencies. The principal task of geometrical acoustics is to determine the trajectories of sound rays. The rays have the simplest form in a homogeneous medium, where they are straight lines. If the acoustic parameters of the medium are functions of spatial coordinates, the ray trajectories become curvilinear, describing sound reflection, refraction, possible focusing, etc. The equations of geometric acoustics have essentially the same form as those of geometric optics. The same laws of reflection and refraction hold for sound rays as for light rays. Geometrical acoustics does not take into account such important wave effects as diffraction. However, it provides a very good approximation when the wavelength is very small compared to the characteristic dimensions of inhomogeneous inclusions through which the sound propagates.

## Mathematical description

The below discussion is from Landau and Lifshitz. If the amplitude and the direction of propagation varies slowly over the distances of wavelength, then an arbitrary sound wave can be approximated locally as a plane wave. In this case, the velocity potential can be written as

$\phi =\mathrm {e} ^{\mathrm {i} \psi }$

For plane wave $\psi ={\boldsymbol {k}}\cdot {\boldsymbol {r}}-\omega t+\alpha$ , where ${\boldsymbol {k}}$ is a constant wavenumber vector, $\omega$ is a constant frequency, ${\boldsymbol {r}}$ is the radius vector, t is the time and $\alpha$ is some arbitrary complex constant. The function $\psi$ is called the *eikonal*. We expect the eikonal to vary slowly with coordinates and time consistent with the approximation, then in that case, a Taylor series expansion provides

$\psi =\psi _{o}+{\boldsymbol {r}}\cdot {\frac {\partial \psi }{\partial {\boldsymbol {r}}}}+t{\frac {\partial \psi }{\partial t}}.$

Equating the two terms for $\psi$ , one finds

${\boldsymbol {k}}={\frac {\partial \psi }{\partial {\boldsymbol {r}}}},\quad \omega =-{\frac {\partial \psi }{\partial t}}$

For sound waves, the relation $\omega ^{2}=c^{2}k^{2}$ holds, where c is the speed of sound and k is the magnitude of the wavenumber vector. Therefore, the eikonal satisfies a first order nonlinear partial differential equation,

$\left({\frac {\partial \psi }{\partial x}}\right)^{2}+\left({\frac {\partial \psi }{\partial y}}\right)^{2}+\left({\frac {\partial \psi }{\partial z}}\right)^{2}-{\frac {1}{c^{2}}}\left({\frac {\partial \psi }{\partial t}}\right)^{2}=0.$

where c can be a function of coordinates if the fluid is not homogeneous. The above equation is same as Hamilton–Jacobi equation where the eikonal can be considered as the *action*. Since Hamilton–Jacobi equation is equivalent to Hamilton's equations, by analogy, one finds that

${\frac {\mathrm {d} {\boldsymbol {k}}}{\mathrm {d} t}}=-{\frac {\partial \omega }{\partial {\boldsymbol {r}}}},\quad {\frac {\mathrm {d} {\boldsymbol {r}}}{\mathrm {d} t}}={\frac {\partial \omega }{\partial {\boldsymbol {k}}}}$

## Practical applications

Practical applications of the methods of geometrical acoustics can be found in very different areas of acoustics. For example, in architectural acoustics the rectilinear trajectories of sound rays make it possible to determine reverberation time in a very simple way. The operation of fathometers and hydrolocators is based on measurements of the time required for sound rays to travel to a reflecting object and back. The ray concept is used in designing sound focusing systems. Also, the approximate theory of sound propagation in inhomogeneous media (such as the ocean and the atmosphere) has been developed largely on the basis of the laws of geometrical acoustics.

The methods of geometrical acoustics have a limited range of applicability because the ray concept itself is only valid for those cases where the amplitude and direction of a wave undergo little changes over distances of the order of wavelength of a sound wave. More specifically, it is necessary that the dimensions of the rooms or obstacles in the sound path should be much greater than the wavelength. If the characteristic dimensions for a given problem become comparable to the wavelength, then wave diffraction begins to play an important part, and this is not covered by geometric acoustics.

## Software applications

The concept of geometrical acoustics is widely used in software applications. Some software applications that use geometrical acoustics for their calculations are ODEON, Enhanced Acoustic Simulator for Engineers, Olive Tree Lab Terrain, CATT-Acoustic™ and COMSOL Multiphysics.

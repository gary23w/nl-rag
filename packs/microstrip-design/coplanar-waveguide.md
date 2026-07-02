---
title: "Coplanar waveguide"
source: https://en.wikipedia.org/wiki/Coplanar_waveguide
domain: microstrip-design
license: CC-BY-SA-4.0
tags: microstrip line, coplanar waveguide, microstrip antenna, stripline board
fetched: 2026-07-02
---

# Coplanar waveguide

Coplanar waveguide is a type of electrical planar transmission line which can be fabricated using printed circuit board technology, and is used to convey microwave-frequency signals. On a smaller scale, coplanar waveguide transmission lines are also built into monolithic microwave integrated circuits.

Conventional **coplanar waveguide** (**CPW**) consists of a single conducting track printed onto a dielectric substrate, together with a pair of return conductors, one to either side of the track. All three conductors are on the same side of the substrate, and hence are *coplanar*. The return conductors are separated from the central track by a small gap, which has an unvarying width along the length of the line. Away from the central conductor, the return conductors usually extend to an indefinite but large distance, so that each is notionally a semi-infinite plane.

**Conductor-backed coplanar waveguide** (**CBCPW**), also known as **coplanar waveguide with ground** (**CPWG**), is a common variant which has a ground plane covering the entire back-face of the substrate. The ground-plane serves as a third return conductor.

Coplanar waveguide was invented in 1969 by Cheng P. Wen, primarily as a means by which non-reciprocal components such as gyrators and isolators could be incorporated in planar transmission line circuits.

The electromagnetic wave carried by a coplanar waveguide exists partly in the dielectric substrate, and partly in the air above it. In general, the dielectric constant of the substrate will be different (and greater) than that of the air, so that the wave is travelling in an inhomogeneous medium. In consequence CPW will not support a true TEM wave; at non-zero frequencies, both the E and H fields will have longitudinal components (a hybrid mode). However, these longitudinal components are usually small and the mode is better described as quasi-TEM.

## Application to nonreciprocal gyromagnetic devices

Nonreciprocal gyromagnetic devices such as resonant isolators and differential phase shifters depend on a microwave signal presenting a rotating (circularly polarized) magnetic field to a statically magnetized ferrite body. CPW can be designed to produce just such a rotating magnetic field in the two slots between the central and side conductors.

The dielectric substrate has no direct effect on the magnetic field of a microwave signal travelling along the CPW line. For the magnetic field, the CPW is then symmetrical in the plane of the metalization, between the substrate side and the air side. Consequently, currents flowing along parallel paths on opposite faces of each conductor (on the air-side and on the substrate-side) are subject to the same inductance, and the overall current tends to be divided equally between the two faces.

Conversely, the substrate *does* affect the electric field, so that the substrate side contributes a larger capacitance across the slots than does the air side. Electric charge can accumulate or be depleted more readily on the substrate face of the conductors than on the air face. As a result, at those points on the wave where the current reverses direction, charge will spill over the edges of the metalization between the air face and the substrate face. This secondary current over the edges gives rise to a longitudinal (parallel with the line), magnetic field in each of the slots, which is in quadrature with the vertical (normal to the substrate surface) magnetic field associated with the main current along the conductors.

If the dielectric constant of the substrate is much greater than unity, then the magnitude of the longitudinal magnetic field approaches that of the vertical field, so that the combined magnetic field in the slots approaches circular polarization.

## Application in solid state physics

Coplanar waveguides play an important role in the field of solid state quantum computing, e.g. for the coupling of microwave photons to a superconducting qubit. In particular the research field of circuit quantum electrodynamics was initiated with coplanar waveguide resonators as crucial elements that allow for high field strength and thus strong coupling to a superconducting qubit by confining a microwave photon to a volume that is much smaller than the cube of the wavelength. To further enhance this coupling, superconducting coplanar waveguide resonators with extremely low losses were applied. (The quality factors of such superconducting coplanar resonators at low temperatures can exceed 106 even in the low-power limit.) Coplanar resonators can also be employed as quantum buses to couple multiple qubits to each other.

Another application of coplanar waveguides in solid state research is for studies involving magnetic resonance, e.g. for electron spin resonance spectroscopy or for magnonics.

Coplanar waveguide resonators have also been employed to characterize the material properties of (high-Tc) superconducting thin films.

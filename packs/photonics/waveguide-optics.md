---
title: "Waveguide (optics)"
source: https://en.wikipedia.org/wiki/Waveguide_(optics)
domain: photonics
license: CC-BY-SA-4.0
tags: integrated photonics, optical fiber, photonic crystal, nonlinear optics
fetched: 2026-07-02
---

# Waveguide (optics)

An **optical waveguide** is a physical structure that guides electromagnetic waves in the optical spectrum. Common types of optical waveguides include optical fiber waveguides, transparent dielectric waveguides made of plastic and glass, liquid light guides, and liquid waveguides.

Optical waveguides are used as components in integrated optical circuits or as the transmission medium in local and long-haul optical communication systems. They can also be used in optical head-mounted displays in augmented reality.

Optical waveguides can be classified according to their geometry (planar, strip, or fiber waveguides), mode structure (single-mode, multi-mode), refractive index distribution (step or gradient index), and material (glass, polymer, semiconductor).

## Total internal reflection

The basic principles behind optical waveguides can be described using the concepts of geometrical or ray optics, as illustrated in the diagram.

Light passing into a medium with higher refractive index bends toward the normal by the process of refraction (Figure **a.**). Take, for example, light passing from air into glass. Similarly, light traveling in the opposite direction (from glass into air) takes the same path, bending away from the normal. This is a consequence of time-reversal symmetry. Each ray in air (black) can be mapped to a ray in the glass (blue), as shown in Figure **b**. There is a one-to-one correspondence. But because of refraction, some of the rays in the glass are left out (red). The remaining rays are trapped in the glass by a process called *total internal reflection*. They are incident on the glass-air interface at an angle above the *critical angle*. These extra rays correspond to a higher *density of states* in more-advanced formulations based on the Green's function.

Using total internal reflection, light can be trapped and guided in a dielectric waveguide (Figure **c**). The red rays bounce off both the top and bottom surface of the high index medium. They're guided even if the slab curves or bends, so long as it bends slowly. This is the basic principle behind fiber optics in which light is guided along a high index glass *core* in a lower index glass *cladding* (Figure **d**).

Ray optics only gives a rough picture of how waveguides work. Maxwell's equations can be solved by analytical or numerical methods for a full-field description of a dielectric waveguide.

## Dielectric slab waveguide

Perhaps the simplest optical waveguide is the dielectric **slab waveguide**, also called a **planar waveguide**. Owing to their simplicity, slab waveguides are often used as toy models but also find application in on-chip devices like arrayed waveguide gratings and acousto-optic filters and modulators.

The slab waveguide consists of three layers of materials with different dielectric constants, extending infinitely in the directions parallel to their interfaces. Light is confined in the middle layer by total internal reflection if the refractive index of the middle layer is larger than that of the surrounding layers.

The slab waveguide is essentially a one-dimensional waveguide. It traps light only normal to the dielectric interfaces. For guided modes, the field in domain II in the diagram is propagating and can be treated as a plane wave. The field in domains I and III evanescently decay away from the slab. The plane wave in domain II bounces between the top and bottom interfaces at some angle typically specified by the ${\vec {\beta }}$ , the wave vector in the plane of the slab. Guided modes constructively interfere on one complete roundtrip in the slab. At each frequency, one or more modes can be found giving a set of eigenvalues $(\omega ,{\vec {\beta }})$ which can be used to construct a band diagram or dispersion relation.

Because guided modes are trapped in the slab, they cannot be excited by light incident on the top or bottom interfaces. Light can be *end-fire or butte coupled* by injecting it with a lens in the plane of the slab. Alternatively a coupling element may be used to couple light into the waveguide, such as a grating coupler or prism coupler.

There are two technologies: diffractive waveguides and reflective waveguides.

## Two-dimensional waveguide

### Strip waveguide

A **strip waveguide** is basically a strip of the layer confined between cladding layers. The simplest case is a **rectangular waveguide**, which is formed when the guiding layer of the slab waveguide is restricted in both transverse directions rather than just one. Rectangular waveguides are used in integrated optical circuits and in laser diodes. They are commonly used as the basis of such optical components as Mach–Zehnder interferometers and wavelength division multiplexers. The cavities of laser diodes are frequently constructed as rectangular optical waveguides. Optical waveguides with rectangular geometry are produced by a variety of means, usually by a planar process.

The field distribution in a rectangular waveguide cannot be solved analytically, however approximate solution methods, such as Marcatili's method, Extended Marcatili's method and Kumar's method, are known.

### Rib waveguide

A **rib waveguide** is a waveguide in which the guiding layer basically consists of the slab with a strip (or several strips) superimposed onto it. Rib waveguides also provide confinement of the wave in two dimensions and near-unity confinement is possible in multi-layer rib structures.

### Segmented waveguide and photonic crystal waveguide

Optical waveguides typically maintain a constant cross-section along their direction of propagation. This is for example the case for strip and of rib waveguides. However, waveguides can also have periodic changes in their cross-section while still allowing lossless transmission of light via so-called Bloch modes. Such waveguides are referred to as segmented waveguides (with a 1D patterning along the direction of propagation) or as photonic crystal waveguides (with a 2D or 3D patterning).

### Laser-inscribed waveguide

Optical waveguides find their most important application in photonics. Configuring the waveguides in 3D space provides integration between electronic components on a chip and optical fibers. Such waveguides may be designed for a single mode propagation of infrared light at telecommunication wavelengths, and configured to deliver optical signal between input and output locations with very low loss.

One of the methods for constructing such waveguides utilizes photorefractive effect in transparent materials. An increase in the refractive index of a material may be induced by nonlinear absorption of pulsed laser light. In order to maximize the increase of the refractive index, a very short (typically femtosecond) laser pulses are used, and focused with a high NA microscope objective. By translating the focal spot through a bulk transparent material the waveguides can be directly written. A variation of this method uses a low NA microscope objective and translates the focal spot along the beam axis. This improves the overlap between the focused laser beam and the photorefractive material, thus reducing power needed from the laser. When transparent material is exposed to an unfocused laser beam of sufficient brightness to initiate photorefractive effect, the waveguides may start forming on their own as a result of an accumulated self-focusing. The formation of such waveguides leads to a breakup of the laser beam. Continued exposure results in a buildup of the refractive index towards the centerline of each waveguide, and collapse of the mode field diameter of the propagating light. Such waveguides remain permanently in the glass and can be photographed off-line (see the picture on the right).

## Light pipe

Light pipes are tubes or cylinders of solid material used to guide light a short distance. In electronics, plastic light pipes are used to guide light from LEDs on a circuit board to the user interface surface. In buildings, light pipes are used to transfer illumination from outside the building to where it is needed inside.

## Optical fiber waveguide

Optical fiber is typically a circular cross-section *dielectric waveguide* consisting of a dielectric material surrounded by another dielectric material with a lower refractive index. Optical fibers are most commonly made from silica glass, however other glass materials are used for certain applications and plastic optical fiber can be used for short-distance applications.

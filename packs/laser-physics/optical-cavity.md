---
title: "Optical cavity"
source: https://en.wikipedia.org/wiki/Optical_cavity
domain: laser-physics
license: CC-BY-SA-4.0
tags: laser physics, stimulated emission, population inversion, optical cavity
fetched: 2026-07-02
---

# Optical cavity

An **optical cavity**, **resonating cavity** or **optical resonator** is an arrangement of mirrors or other optical elements that confines light waves similarly to how a cavity resonator confines microwaves. Optical cavities are a major component of lasers, surrounding the gain medium and providing feedback of the laser light. They are also used in optical parametric oscillators and some interferometers. Light confined in the cavity reflects multiple times, producing modes with certain resonance frequencies. Modes can be decomposed into longitudinal modes that differ only in frequency and transverse modes that have different intensity patterns across the cross section of the beam. Many types of optical cavities produce standing wave modes.

Different resonator types are distinguished by the focal lengths of the two mirrors and the distance between them. Flat mirrors are not often used because of the difficulty of aligning them to the needed precision. The geometry (resonator type) must be chosen so that the beam remains stable, i.e. the size of the beam does not continually grow with multiple reflections. Resonator types are also designed to meet other criteria such as a minimum beam waist or having no focal point (and therefore no intense light at a single point) inside the cavity.

Optical cavities are designed to have a large Q factor, meaning a beam undergoes many oscillation cycles with little attenuation. In the regime of high Q values, this is equivalent to the frequency line width being small compared to the resonant frequency of the cavity.

## Resonator modes

Light confined in a resonator will reflect multiple times from the mirrors, and due to the effects of interference, only certain patterns and frequencies of radiation will be sustained by the resonator, with the others being suppressed by destructive interference. In general, radiation patterns which are reproduced on every round-trip of the light through the resonator are the most stable. These are known as the *modes* of the resonator.

Resonator modes can be divided into two types: longitudinal modes, which differ in frequency from each other; and transverse modes, which may differ in both frequency and the intensity pattern of the light. The basic, or fundamental transverse mode of a resonator is a Gaussian beam.

## Resonator types

The most common types of optical cavities consist of two facing plane (flat) or spherical mirrors. The simplest of these is the plane-parallel or Fabry–Pérot cavity, consisting of two opposing flat mirrors. While simple, this arrangement is rarely used in large-scale lasers due to the difficulty of alignment; the mirrors must be aligned parallel within a few seconds of arc, or "walkoff" of the intracavity beam will result in it spilling out of the sides of the cavity. However, this problem is much reduced for very short cavities with a small mirror separation distance (*L* < 1 cm). Plane-parallel resonators are therefore commonly used in microchip and microcavity lasers and semiconductor lasers. In these cases, rather than using separate mirrors, a reflective optical coating may be directly applied to the laser medium itself. The plane-parallel resonator is also the basis of the Fabry–Pérot interferometer.

For a resonator with two mirrors with radii of curvature *R*1 and *R*2, there are a number of common cavity configurations. If the two radii are equal to half the cavity length (*R*1 = *R*2 = *L* / 2), a concentric or spherical resonator results. This type of cavity produces a diffraction-limited beam waist in the centre of the cavity, with large beam diameters at the mirrors, filling the whole mirror aperture. Similar to this is the hemispherical cavity, with one plane mirror and one mirror of radius equal to the cavity length.

A common and important design is the confocal resonator, with mirrors of equal radii to the cavity length (*R*1 = *R*2 = *L*). This design produces the smallest possible beam diameter at the cavity mirrors for a given cavity length, and is often used in lasers where the purity of the transverse mode pattern is important.

A concave-convex cavity has one convex mirror with a negative radius of curvature. This design produces no intracavity focus of the beam, and is thus useful in very high-power lasers where the intensity of the light might be damaging to the intracavity medium if brought to a focus.

Less common resonator types include optical ring resonators and whispering-gallery mode resonators, in which a resonance is formed by waves moving in a closed loop rather than reflecting between two mirrors.

## Stability

Only certain ranges of values for *R*1, *R*2, and *L* produce stable resonators in which periodic refocussing of the intracavity beam is produced. If the cavity is unstable, the beam size will grow without limit, eventually growing larger than the size of the cavity mirrors and being lost. By using methods such as ray transfer matrix analysis, it is possible to calculate a stability criterion:

$0\leqslant \left(1-{\frac {L}{R_{1}}}\right)\left(1-{\frac {L}{R_{2}}}\right)\leqslant 1.$

Values which satisfy the inequality correspond to stable resonators.

The stability can be shown graphically by defining a stability parameter, *g* for each mirror:

$g_{1}=1-{\frac {L}{R_{1}}},\qquad g_{2}=1-{\frac {L}{R_{2}}}$

,

and plotting *g*1 against *g*2 as shown. Areas bounded by the line *g*1 *g*2 = 1 and the axes are stable. Cavities at points exactly on the line are marginally stable; small variations in cavity length can cause the resonator to become unstable, and so lasers using these cavities are in practice often operated just inside the stability line.

A simple geometric statement describes the regions of stability: A cavity is stable if the line segments between the mirrors and their centers of curvature overlap, but one does not lie entirely within the other.

In the confocal cavity, if a ray is deviated from its original direction in the middle of the cavity, its displacement after reflecting from one of the mirrors is larger than in any other cavity design. This prevents amplified spontaneous emission and is important for designing high power amplifiers with good beam quality.

## Practical resonators

If the optical cavity is not empty (e.g., a laser cavity which contains the gain medium), the value of *L* needs to be adjusted to account for the index of refraction of the medium. Optical elements such as lenses placed in the cavity alter the stability and mode size. In addition, for most gain media, thermal and other inhomogeneities create a variable lensing effect in the medium, which must be considered in the design of the laser resonator.

Practical laser resonators may contain more than two mirrors; three- and four-mirror arrangements are common, producing a "folded cavity". Commonly, a pair of curved mirrors form one or more confocal sections, with the rest of the cavity being quasi-collimated and using plane mirrors. The shape of the laser beam depends on the type of resonator: The beam produced by stable, paraxial resonators can be well modeled by a Gaussian beam. In special cases the beam can be described as a single transverse mode and the spatial properties can be well described by the Gaussian beam, itself. More generally, this beam may be described as a superposition of transverse modes. Accurate description of such a beam involves expansion over some complete, orthogonal set of functions (over two-dimensions) such as Hermite polynomials or the Ince polynomials. Unstable laser resonators on the other hand, have been shown to produce fractal shaped beams.

Some intracavity elements are usually placed at a beam waist between folded sections. Examples include acousto-optic modulators for cavity dumping and vacuum spatial filters for transverse mode control. For some low power lasers, the laser gain medium itself may be positioned at a beam waist. Other elements, such as filters, prisms and diffraction gratings often need large quasi-collimated beams.

These designs allow compensation of the cavity beam's astigmatism, which is produced by Brewster-cut elements in the cavity. A Z-shaped arrangement of the cavity also compensates for coma while the 'delta' or X-shaped cavity does not.

Out of plane resonators lead to rotation of the beam profile and more stability. The heat generated in the gain medium leads to frequency drift of the cavity, therefore the frequency can be actively stabilized by locking it to unpowered cavity. Similarly the pointing stability of a laser may still be improved by spatial filtering by an optical fibre.

### Alignment

Precise alignment is important when assembling an optical cavity. For best output power and beam quality, optical elements must be aligned such that the path followed by the beam is centered through each element.

Simple cavities are often aligned with an alignment laser—a well-collimated visible laser that can be directed along the axis of the cavity. Observation of the path of the beam and its reflections from various optical elements allows the elements' positions and tilts to be adjusted.

More complex cavities may be aligned using devices such as electronic autocollimators and laser beam profilers.

## Optical delay lines

Optical cavities can also be used as multipass optical delay lines, folding a light beam so that a long path-length may be achieved in a small space. A plane-parallel cavity with flat mirrors produces a flat zigzag light path, but as discussed above, these designs are very sensitive to mechanical disturbances and walk-off. When curved mirrors are used in a nearly confocal configuration, the beam travels on a circular zigzag path. The latter is called a Herriott-type delay line. A fixed insertion mirror is placed off-axis near one of the curved mirrors, and a mobile pickup mirror is similarly placed near the other curved mirror. A flat linear stage with one pickup mirror is used in case of flat mirrors and a rotational stage with two mirrors is used for the Herriott-type delay line.

The rotation of the beam inside the cavity alters the polarization state of the beam. To compensate for this, a single pass delay line is also needed, made of either a three or two mirrors in a 3d respective 2d retro-reflection configuration on top of a linear stage. To adjust for beam divergence a second car on the linear stage with two lenses can be used. The two lenses act as a telescope producing a flat phase front of a Gaussian beam on a virtual end mirror.

---
title: "Huygens–Fresnel principle"
source: https://en.wikipedia.org/wiki/Huygens%E2%80%93Fresnel_principle
domain: wave-optics
license: CC-BY-SA-4.0
tags: wave interference, fresnel diffraction, fraunhofer diffraction, diffraction grating
fetched: 2026-07-02
---

# Huygens–Fresnel principle

The **Huygens–Fresnel principle** (named after Dutch physicist Christiaan Huygens and French physicist Augustin-Jean Fresnel) states that every point on a wavefront is itself the source of spherical wavelets and that the secondary wavelets emanating from different points mutually interfere. The sum of these spherical wavelets forms a new wavefront. As such, the Huygens–Fresnel principle is a method of analysis applied to problems of luminous wave propagation both in the far-field limit and in near-field diffraction as well as reflection.

## History

In 1678, Huygens proposed that every point reached by a luminous disturbance becomes a source of a spherical wave. The sum of these secondary waves determines the form of the wave at any subsequent time; the overall procedure is referred to as **Huygens's construction**. He assumed that the secondary waves traveled only in the "forward" direction, but it is not explained in the theory why this is the case. He was able to provide a qualitative explanation of linear and spherical wave propagation, and to derive the laws of reflection and refraction using this principle, but could not explain the deviations from rectilinear propagation that occur when light encounters edges, apertures and screens, commonly known as diffraction effects.

In 1818, Fresnel showed that Huygens's principle, together with his own principle of interference, could explain both the rectilinear propagation of light and also diffraction effects. To obtain agreement with the experimental results, he had to include additional arbitrary assumptions about the phase and amplitude of the secondary waves, as well as an obliquity factor. These assumptions have no obvious physical foundation, but led to predictions that agreed with many experimental observations, including the Poisson spot.

Poisson was a member of the French Academy, which reviewed Fresnel's work. He used Fresnel's theory to predict that a bright spot ought to appear in the center of the shadow of a small disc, and deduced from this that the theory was incorrect. However, François Arago, another member of the committee, performed the experiment and showed that the prediction was correct. This success was important evidence in favor of the wave theory of light over then predominant corpuscular theory.

In 1882, Gustav Kirchhoff analyzed Fresnel's theory in a rigorous mathematical formulation, as an approximate form of an integral theorem. Very few rigorous solutions to diffraction problems are known, however, and most problems in optics are adequately treated using the Huygens–Fresnel principle.

In 1939 Edward Copson, extended Huygens's original principle to consider the polarization of light, which requires a vector potential, in contrast to the scalar potential of a simple ocean wave or sound wave.

In antenna theory and engineering, the reformulation of the Huygens–Fresnel principle for radiating current sources is known as surface equivalence principle.

Issues in Huygens–Fresnel theory continue to be of interest. In 1991, David A. B. Miller suggested that treating the source as a dipole (not the monopole assumed by Huygens) will cancel waves propagating in the reverse direction, making Huygens's construction quantitatively correct. In 2021, Forrest L. Anderson showed that treating the wavelets as Dirac delta functions, summing and differentiating the summation is sufficient to cancel reverse propagating waves.

## Examples

### Refraction

The apparent change in direction of a light ray as it enters a sheet of glass at an angle can be understood by the Huygens's construction. Each point on the surface of the glass gives a secondary wavelet. These wavelets propagate at a slower velocity in the glass, making less forward progress than their counterparts in air. When the wavelets are summed, the resulting wavefront propagates at an angle to the direction of the wavefront in air.

In an inhomogeneous medium with a variable index of refraction, different parts of the wavefront propagate at different speeds. Consequently, the wavefront bends around in the direction of the higher index.

### Diffraction

## Huygens's principle as a microscopic model

The Huygens–Fresnel principle provides a reasonable basis for understanding and predicting the classical wave propagation of light. However, there are limitations to the principle, namely the same approximations made for deriving the Kirchhoff's diffraction formula and the approximations of near field due to Fresnel. These can be summarized in the fact that the wavelength of light is much smaller than the dimensions of any optical components encountered.

Kirchhoff's diffraction formula provides a rigorous mathematical foundation for diffraction, based on the wave equation. The arbitrary assumptions made by Fresnel to arrive at the Huygens–Fresnel equation emerge automatically from the mathematics in this derivation.

A simple example of the operation of the principle can be observed when an open doorway connects two rooms and a sound is produced in a remote corner of one of them. A person in the other room will hear the sound as if it originated at the doorway. As far as the second room is concerned, the vibrating air in the doorway is the source of the sound.

## Mathematical expression of the principle

Consider the case of a point source located at a point **P**0, vibrating at a frequency *f*. The disturbance may be described by a complex variable *U*0 known as the complex amplitude. It produces a spherical wave with wavelength λ, wavenumber *k* = 2*π*/*λ*. Within a constant of proportionality, the complex amplitude of the primary wave at the point **Q** located at a distance *r*0 from **P**0 is:

$U(r_{0})\propto {\frac {U_{0}e^{ikr_{0}}}{r_{0}}}.$

Note that magnitude decreases in inverse proportion to the distance traveled, and the phase changes as *k* times the distance traveled.

Using Huygens's theory and the principle of superposition of waves, the complex amplitude at a further point **P** is found by summing the contribution from each point on the sphere of radius *r*0. In order to obtain agreement with experimental results, Fresnel found that the individual contributions from the secondary waves on the sphere had to be multiplied by a constant, −*i*/λ, and by an additional inclination factor, *K*(χ). The first assumption implies that the secondary waves oscillate at a quarter of a cycle out of phase with respect to the primary wave and the second implies that the magnitude of the secondary waves is in a ratio of 1:λ to the primary wave. He also assumed that *K*(χ) had a maximum value when χ = 0, and was equal to zero when χ = π/2, where χ is the angle between the normal of the primary wavefront and the normal of the secondary wavefront. The complex amplitude at **P**, due to the contribution of secondary waves, is then given by:

$U(P)=-{\frac {i}{\lambda }}U(r_{0})\int _{S}{\frac {e^{iks}}{s}}K(\chi )\,dS$

where *S* describes the surface of the sphere, and *s* is the distance between **Q** and **P**.

Fresnel used a zone construction method to find approximate values of *K* for the different zones, which enabled him to make predictions that were in agreement with experimental results. The integral theorem of Kirchhoff includes the basic idea of Huygens–Fresnel principle. Kirchhoff showed that in many cases, the theorem can be approximated to a simpler form that is equivalent to the formation of Fresnel's formulation.

For an aperture illumination consisting of a single expanding spherical wave, if the radius of the curvature of the wave is sufficiently large, Kirchhoff gave the following expression for *K*(χ):

$~K(\chi )={\frac {1}{2}}(1+\cos \chi )$

*K* has a maximum value at χ = 0 as in the Huygens–Fresnel principle; however, *K* is not equal to zero at χ = π/2, but at χ = π.

The above derivation of *K*(χ) assumed that the diffracting aperture is illuminated by a single spherical wave with a sufficiently large radius of curvature. However, the principle holds for more general illuminations. An arbitrary illumination can be decomposed into a collection of point sources, and the linearity of the wave equation can be invoked to apply the principle to each point source individually. *K*(χ) can be generally expressed as:

$~K(\chi )=\cos \chi$

In this case, *K* satisfies the conditions stated above (maximum value at χ = 0 and zero at χ = π/2).

## Generalized Huygens's principle

The generalized Huygens's principle can be expressed for $t'>t$ in the form:

$\psi (\mathbf {x} ',t')=i\int d^{3}x\,G(\mathbf {x} ',t';\mathbf {x} ,t)\psi (\mathbf {x} ,t)$

where *G* is known as the Green's function or *propagator*, which propagates the wave function $\psi$ in time.

This generalized principle is the basis for Feynman's approach to quantum electrodynamics. Feynman described the generalized principle in the following way:

> "Actually, Huygens's principle is not correct in optics. It is replaced by Kirchoff's [sic] modification which requires that both the amplitude and its derivative must be known on the adjacent surface. This is a consequence of the fact that the wave equation in optics is second order in time. The wave equation of quantum mechanics is first order in time; therefore, Huygens's principle is correct for matter waves, action replacing time."

## Feynman's path integral and the modern photon wave function

Huygens's theory served as a fundamental explanation of the wave nature of light interference and was further developed by Fresnel and Young, but did not fully resolve all observations, such as the low-intensity double-slit experiment first performed by G. I. Taylor in 1909. It was not until the early and mid-1900s that quantum theory discussions, particularly the early discussions at the 1927 Brussels Solvay Conference, where Louis de Broglie proposed his de Broglie hypothesis that the photon is guided by a wave function.

The wave function presents a much different explanation of the observed light and dark bands in a double slit experiment. In this conception, the photon follows a path that is a probabilistic choice of one of many possible paths in the electromagnetic field. These probable paths form the pattern: in dark areas, no photons are landing, and in bright areas, many photons are landing. The set of possible photon paths is consistent with Richard Feynman's path integral theory, the paths determined by the surroundings: the photon's originating point (atom), the slit, and the screen and by tracking and summing phases. The wave function is a solution to this geometry. The wave function approach was further supported by additional double-slit experiments in Italy and Japan in the 1970s and 1980s with electrons.

## Quantum field theory

Huygens's principle can be seen as a consequence of the homogeneity of space—space is uniform in all locations. Any disturbance created in a sufficiently small region of homogeneous space (or in a homogeneous medium) propagates from that region in all geodesic directions. The waves produced by this disturbance, in turn, create disturbances in other regions, and so on. The superposition of all the waves results in the observed pattern of wave propagation.

Homogeneity of space is fundamental to quantum field theory (QFT), where the wave function of any object propagates along all available unobstructed paths. When integrated along all possible paths, with a phase factor proportional to the action, the interference of the wave-functions correctly predicts observable phenomena. Every point on the wavefront acts as the source of secondary wavelets that spread out in the light cone with the same speed as the wave. The new wavefront is found by constructing the surface tangent to the secondary wavelets.

## In other spatial dimensions

In 1900, Jacques Hadamard observed that Huygens's principle was broken when the number of spatial dimensions is even. From this, he developed a set of conjectures that remain an active topic of research. In particular, it has been discovered that Huygens's principle holds on a large class of homogeneous spaces derived from the Coxeter group (so, for example, the Weyl groups of simple Lie algebras).

The traditional statement of Huygens's principle for the d'Alembertian gives rise to the KdV hierarchy; analogously, the Dirac operator gives rise to the AKNS hierarchy.

---
title: "Dispersion (optics)"
source: https://en.wikipedia.org/wiki/Anomalous_dispersion
domain: x-ray-crystallography-protein
license: CC-BY-SA-4.0
tags: macromolecular crystallography, phase problem, diffraction pattern, resolution
fetched: 2026-07-02
---

# Dispersion (optics)

(Redirected from

Anomalous dispersion

)

**Dispersion** is the phenomenon in which the phase velocity of a wave depends on its frequency. Sometimes the term **chromatic dispersion** is used to refer to optics specifically, as opposed to wave propagation in general. A medium having this common property may be termed a **dispersive medium**.

Although the term is used in the field of optics to describe light and other electromagnetic waves, dispersion in the same sense can apply to any sort of wave motion such as acoustic dispersion in the case of sound and seismic waves, and in gravity waves (ocean waves). Within optics, dispersion is a property of telecommunication signals along transmission lines (such as microwaves in coaxial cable) or the pulses of light in optical fiber.

In optics, one important and familiar consequence of dispersion is the change in the angle of refraction of different colors of light, as seen in the spectrum produced by a dispersive prism and in chromatic aberration of lenses. Design of compound achromatic lenses, in which chromatic aberration is largely cancelled, uses a quantification of a glass's dispersion given by its Abbe number *V*, where *lower* Abbe numbers correspond to *greater* dispersion over the visible spectrum. In some applications such as telecommunications, the absolute phase of a wave is often not important but only the propagation of wave packets or "pulses"; in that case one is interested only in variations of group velocity with frequency, so-called group-velocity dispersion.

All common transmission media also vary in attenuation (normalized to transmission length) as a function of frequency, leading to attenuation distortion; this is not dispersion, although sometimes reflections at closely spaced impedance boundaries (e.g. crimped segments in a cable) can produce signal distortion which further aggravates inconsistent transit time as observed across signal bandwidth.

## Examples

Dispersion causes a rainbow's spatial separation of a white light into components of different wavelengths (different colors). However, dispersion also has an effect in many other circumstances: for example, group-velocity dispersion causes pulses to spread in optical fibers, degrading signals over long distances; also, a cancellation between group-velocity dispersion and nonlinear effects leads to soliton waves.

## Material and waveguide dispersion

Most often, chromatic dispersion refers to bulk material dispersion, that is, the change in refractive index with optical frequency. However, in a waveguide there is also the phenomenon of *waveguide dispersion*, in which case a wave's phase velocity in a structure depends on its frequency simply due to the structure's geometry. More generally, "waveguide" dispersion can occur for waves propagating through any inhomogeneous structure (e.g., a photonic crystal), whether or not the waves are confined to some region. In a waveguide, *both* types of dispersion will generally be present, although they are not strictly additive. For example, in fiber optics the material and waveguide dispersion can effectively cancel each other out to produce a zero-dispersion wavelength, important for fast fiber-optic communication.

## Material dispersion in optics

Material dispersion can be a desirable or undesirable effect in optical applications. The dispersion of light by glass prisms is used to construct spectrometers and spectroradiometers. However, in lenses, dispersion causes chromatic aberration, an undesired effect that may degrade images in microscopes, telescopes, and photographic objectives.

The *phase velocity* *v* of a wave in a given uniform medium is given by

$v={\frac {c}{n}},$

where *c* is the speed of light in vacuum, and *n* is the refractive index of the medium.

In general, the refractive index is some function of the frequency *f* of the light, thus *n* = *n*(*f*), or alternatively, with respect to the wave's wavelength *n* = *n*(*λ*). The wavelength dependence of a material's refractive index is usually quantified by its Abbe number or its coefficients in an empirical formula such as the Cauchy or Sellmeier equations.

Because of the Kramers–Kronig relations, the wavelength dependence of the real part of the refractive index is related to the material absorption, described by the imaginary part of the refractive index (also called the extinction coefficient). In particular, for non-magnetic materials (*μ* = *μ*0), the susceptibility *χ* that appears in the Kramers–Kronig relations is the electric susceptibility *χ*e = *n*2 − 1.

The most commonly seen consequence of dispersion in optics is the separation of white light into a color spectrum by a prism. From Snell's law it can be seen that the angle of refraction of light in a prism depends on the refractive index of the prism material. Since that refractive index varies with wavelength, it follows that the angle that the light is refracted by will also vary with wavelength, causing an angular separation of the colors known as *angular dispersion*.

For visible light, the refraction index *n* of most transparent materials (e.g., air, glasses) decreases with increasing wavelength *λ*:

$1<n(\lambda _{\text{red}})<n(\lambda _{\text{yellow}})<n(\lambda _{\text{blue}}),$

or generally,

${\frac {dn}{d\lambda }}<0.$

In this case, the medium is said to have *normal dispersion*. However, if the index increases with increasing wavelength (which is typically the case in the ultraviolet), the medium is said to have *anomalous dispersion*.

At the interface of such a material with air or vacuum (index of ~1), Snell's law predicts that light incident at an angle *θ* to the normal will be refracted at an angle arcsin(⁠sin *θ*/*n*⁠). Thus, in the case of normal dispersion, blue light, with a higher refractive index, will be bent more strongly than red light, resulting in the well-known rainbow pattern.

## Group-velocity dispersion

Beyond simply describing a change in the phase velocity over wavelength, a more serious consequence of dispersion in many applications is termed group-velocity dispersion (GVD). While phase velocity *v* is defined as *v* = *c*/*n*, this describes only one frequency component. When different frequency components are combined, as when considering a signal or a pulse, one is often more interested in the group velocity, which describes the speed at which a pulse or information superimposed on a wave (modulation) propagates. In the accompanying animation, it can be seen that the wave itself (orange-brown) travels at a phase velocity much faster than the speed of the *envelope* (black), which corresponds to the group velocity. This pulse might be a communications signal, for instance, and its information only travels at the group velocity rate, even though it consists of wavefronts advancing at a faster rate (the phase velocity).

It is possible to calculate the group velocity from the refractive-index curve *n*(*ω*) or more directly from the wavenumber *k* = *ωn*/*c*, where *ω* is the radian frequency *ω* = 2*πf*. Whereas one expression for the phase velocity is *v*p = *ω*/*k*, the group velocity can be expressed using the derivative: *v*g = *dω*/*dk*. Or in terms of the phase velocity *v*p,

$v_{\text{g}}={\frac {v_{\text{p}}}{1-{\dfrac {\omega }{v_{\text{p}}}}{\dfrac {dv_{\text{p}}}{d\omega }}}}.$

When dispersion is present, not only the group velocity is not equal to the phase velocity, but generally it itself varies with wavelength. This is known as group-velocity dispersion and causes a short pulse of light to be broadened, as the different-frequency components within the pulse travel at different velocities. Group-velocity dispersion is quantified as the derivative of the *reciprocal* of the group velocity with respect to angular frequency, which results in *group-velocity dispersion* = *d*2*k*/*dω*2.

If a light pulse is propagated through a material with positive group-velocity dispersion, then the shorter-wavelength components travel slower than the longer-wavelength components. The pulse therefore becomes *positively chirped*, or *up-chirped*, increasing in frequency with time. On the other hand, if a pulse travels through a material with negative group-velocity dispersion, shorter-wavelength components travel faster than the longer ones, and the pulse becomes *negatively chirped*, or *down-chirped*, decreasing in frequency with time.

An everyday example of a negatively chirped signal in the acoustic domain is that of an approaching train hitting deformities on a welded track. The sound caused by the train itself is impulsive and travels much faster in the metal tracks than in air, so that the train can be heard well before it arrives. However, from afar it is not heard as causing impulses, but leads to a distinctive descending chirp, amidst reverberation caused by the complexity of the vibrational modes of the track. Group-velocity dispersion can be heard in that the volume of the sounds stays audible for a surprisingly long time, up to several seconds.

## Dispersion control

The result of GVD, whether negative or positive, is ultimately temporal spreading of the pulse. This makes dispersion management extremely important in optical communications systems based on optical fiber, since if dispersion is too high, a group of pulses representing a bit-stream will spread in time and merge, rendering the bit-stream unintelligible. This limits the length of fiber that a signal can be sent down without regeneration. One possible answer to this problem is to send signals down the optical fibre at a wavelength where the GVD is zero (e.g., around 1.3–1.5 μm in silica fibres), so pulses at this wavelength suffer minimal spreading from dispersion. In practice, however, this approach causes more problems than it solves because zero GVD unacceptably amplifies other nonlinear effects (such as four-wave mixing). Another possible option is to use soliton pulses in the regime of negative dispersion, a form of optical pulse which uses a nonlinear optical effect to self-maintain its shape. Solitons have the practical problem, however, that they require a certain power level to be maintained in the pulse for the nonlinear effect to be of the correct strength. Instead, the solution that is currently used in practice is to perform dispersion compensation, typically by matching the fiber with another fiber of opposite-sign dispersion so that the dispersion effects cancel; such compensation is ultimately limited by nonlinear effects such as self-phase modulation, which interact with dispersion to make it very difficult to undo.

Dispersion control is also important in lasers that produce short pulses. The overall dispersion of the optical resonator is a major factor in determining the duration of the pulses emitted by the laser. A pair of prisms can be arranged to produce net negative dispersion, which can be used to balance the usually positive dispersion of the laser medium. Diffraction gratings can also be used to produce dispersive effects; these are often used in high-power laser amplifier systems. Recently, an alternative to prisms and gratings has been developed: chirped mirrors. These dielectric mirrors are coated so that different wavelengths have different penetration lengths, and therefore different group delays. The coating layers can be tailored to achieve a net negative dispersion.

## In waveguides

Waveguides are highly dispersive due to their geometry (rather than just to their material composition). Optical fibers are a sort of waveguide for optical frequencies (light) widely used in modern telecommunications systems. The rate at which data can be transported on a single fiber is limited by pulse broadening due to chromatic dispersion among other phenomena.

In general, for a waveguide mode with an angular frequency *ω*(*β*) at a propagation constant *β* (so that the electromagnetic fields in the propagation direction *z* oscillate proportional to *e**i*(*βz*−*ωt*)), the group-velocity dispersion parameter *D* is defined as

$D=-{\frac {2\pi c}{\lambda ^{2}}}{\frac {d^{2}\beta }{d\omega ^{2}}}={\frac {2\pi c}{v_{g}^{2}\lambda ^{2}}}{\frac {dv_{g}}{d\omega }},$

where *λ* = 2π*c*/*ω* is the vacuum wavelength, and *v*g = *dω*/*dβ* is the group velocity. This formula generalizes the one in the previous section for homogeneous media and includes both waveguide dispersion and material dispersion. The reason for defining the dispersion in this way is that |*D*| is the (asymptotic) temporal pulse spreading Δ*t* per unit bandwidth Δ*λ* per unit distance travelled, commonly reported in ps/(nm⋅km) for optical fibers.

In the case of multi-mode optical fibers, so-called modal dispersion will also lead to pulse broadening. Even in single-mode fibers, pulse broadening can occur as a result of polarization mode dispersion (since there are still two polarization modes). These are *not* examples of chromatic dispersion, as they are not dependent on the wavelength or bandwidth of the pulses propagated.

## Higher-order dispersion over broad bandwidths

When a broad range of frequencies (a broad bandwidth) is present in a single wavepacket, such as in an ultrashort pulse or a chirped pulse or other forms of spread spectrum transmission, it may not be accurate to approximate the dispersion by a constant over the entire bandwidth, and more complex calculations are required to compute effects such as pulse spreading.

In particular, the dispersion parameter *D* defined above is obtained from only one derivative of the group velocity. Higher derivatives are known as *higher-order dispersion*. These terms are simply a Taylor series expansion of the dispersion relation *β*(*ω*) of the medium or waveguide around some particular frequency. Their effects can be computed via numerical evaluation of Fourier transforms of the waveform, via integration of higher-order slowly varying envelope approximations, by a split-step method (which can use the exact dispersion relation rather than a Taylor series), or by direct simulation of the full Maxwell's equations rather than an approximate envelope equation.

## Spatial dispersion

In electromagnetics and optics, the term *dispersion* generally refers to aforementioned temporal or frequency dispersion. Spatial dispersion refers to the non-local response of the medium to the space; this can be reworded as the wavevector dependence of the permittivity. For an exemplary anisotropic medium, the spatial relation between electric and electric displacement field can be expressed as a convolution:

$D_{i}(t,r)=E_{i}(t,r)+\int _{0}^{\infty }\int f_{ik}(\tau ;r,r')E_{k}(t-\tau ,r')\,dV'\,d\tau ,$

where the kernel $f_{ik}$ is dielectric response (susceptibility); its indices make it in general a tensor to account for the anisotropy of the medium. Spatial dispersion is negligible in most macroscopic cases, where the scale of variation of $E_{k}(t-\tau ,r')$ is much larger than atomic dimensions, because the dielectric kernel dies out at macroscopic distances. Nevertheless, it can result in non-negligible macroscopic effects, particularly in conducting media such as metals, electrolytes and plasmas. Spatial dispersion also plays role in optical activity and Doppler broadening, as well as in the theory of metamaterials.

## In gemology

| Mineral name | nB − nG | nC − nF |
|---|---|---|
| Hematite | 0.500 | — |
| Cinnabar (HgS) | 0.40 | — |
| synth. Rutile | 0.330 | 0.190 |
| Rutile (TiO2) | 0.280 | 0.120–0.180 |
| Anatase (TiO2) | 0.213–0.259 | — |
| Wulfenite | 0.203 | 0.133 |
| Vanadinite | 0.202 | — |
| Fabulite | 0.190 | 0.109 |
| Sphalerite (ZnS) | 0.156 | 0.088 |
| Sulfur (S) | 0.155 | — |
| Stibiotantalite | 0.146 | — |
| Goethite (FeO(OH)) | 0.14 | — |
| Brookite (TiO2) | 0.131 | 0.12–1.80 |
| Linobate | 0.13 | 0.075 |
| Zincite (ZnO) | 0.127 | — |
| synth. Moissanite (SiC) | 0.104 | — |
| Cassiterite (SnO2) | 0.071 | 0.035 |
| Zirconia (ZrO2) | 0.060 | 0.035 |
| Powellite (CaMoO4) | 0.058 | — |
| Andradite | 0.057 | — |
| Demantoid | 0.057 | 0.034 |
| Cerussite | 0.055 | 0.033–0.050 |
| Titanite | 0.051 | 0.019–0.038 |
| Benitoite | 0.046 | 0.026 |
| Anglesite | 0.044 | 0.025 |
| Diamond (C) | 0.044 | 0.025 |
| synth. Cassiterite (SnO2) | 0.041 | — |
| Flint glass | 0.041 | — |
| Hyacinth | 0.039 | — |
| Jargoon | 0.039 | — |
| Starlite | 0.039 | — |
| Scheelite | 0.038 | 0.026 |
| Zircon (ZrSiO4) | 0.039 | 0.022 |
| GGG | 0.038 | 0.022 |
| Dioptase | 0.036 | 0.021 |
| Whe Vinay wellite | 0.034 | — |
| Gypsum | 0.033 | 0.008 |
| Alabaster | 0.033 | — |
| Epidote | 0.03 | 0.012–0.027 |
| Tanzanite | 0.030 | 0.011 |
| Thulite | 0.03 | 0.011 |
| Zoisite | 0.03 | — |
| YAG | 0.028 | 0.015 |
| Spessartine | 0.027 | 0.015 |
| Uvarovite | 0.027 | 0.014–0.021 |
| Almandine | 0.027 | 0.013–0.016 |
| Hessonite | 0.027 | 0.013–0.015 |
| Willemite | 0.027 | — |
| Pleonaste | 0.026 | — |
| Rhodolite | 0.026 | — |
| Boracite | 0.024 | 0.012 |
| Cryolite | 0.024 | — |
| Staurolite | 0.023 | 0.012–0.013 |
| Pyrope | 0.022 | 0.013–0.016 |
| Diaspore | 0.02 | — |
| Grossular | 0.020 | 0.012 |
| Hemimorphite | 0.020 | 0.013 |
| Kyanite | 0.020 | 0.011 |
| Peridot | 0.020 | 0.012–0.013 |
| Spinel | 0.020 | 0.011 |
| Vesuvianite | 0.019–0.025 | 0.014 |
| Gahnite | 0.019–0.021 | — |
| Clinozoisite | 0.019 | 0.011–0.014 |
| Labradorite | 0.019 | 0.010 |
| Axinite | 0.018–0.020 | 0.011 |
| Diopside | 0.018–0.020 | 0.01 |
| Ekanite | 0.018 | 0.012 |
| Corundum (Al2O3) | 0.018 | 0.011 |
| synth. Corundum | 0.018 | 0.011 |
| Ruby (Al2O3) | 0.018 | 0.011 |
| Sapphire (Al2O3) | 0.018 | 0.011 |
| Kornerupine | 0.018 | 0.010 |
| Sinhalite | 0.018 | 0.010 |
| Sodalite | 0.018 | 0.009 |
| Rhodizite | 0.018 | — |
| Hiddenite | 0.017 | 0.010 |
| Kunzite | 0.017 | 0.010 |
| Spodumene | 0.017 | 0.010 |
| Tourmaline | 0.017 | 0.009–0.011 |
| Cordierite | 0.017 | 0.009 |
| Danburite | 0.017 | 0.009 |
| Herderite | 0.017 | 0.008–0.009 |
| Rubellite | 0.017 | 0.008–0.009 |
| Achroite | 0.017 | — |
| Dravite | 0.017 | — |
| Elbaite | 0.017 | — |
| Indicolite | 0.017 | — |
| Liddicoatite | 0.017 | — |
| Scapolite | 0.017 | — |
| Schorl | 0.017 | — |
| Verdelite | 0.017 | — |
| Andalusite | 0.016 | 0.009 |
| Baryte (BaSO4) | 0.016 | 0.009 |
| Euclase | 0.016 | 0.009 |
| Datolite | 0.016 | — |
| Alexandrite | 0.015 | 0.011 |
| Chrysoberyl | 0.015 | 0.011 |
| Rhodochrosite | 0.015 | 0.010–0.020 |
| Sillimanite | 0.015 | 0.009–0.012 |
| Hambergite | 0.015 | 0.009–0.010 |
| Pyroxmangite | 0.015 | — |
| synth. Scheelite | 0.015 | — |
| Smithsonite | 0.014–0.031 | 0.008–0.017 |
| Amblygonite | 0.014–0.015 | 0.008 |
| Aquamarine | 0.014 | 0.009–0.013 |
| Beryl | 0.014 | 0.009–0.013 |
| Emerald | 0.014 | 0.009–0.013 |
| Heliodor | 0.014 | 0.009–0.013 |
| Morganite | 0.014 | 0.009–0.013 |
| Brazilianite | 0.014 | 0.008 |
| Celestine | 0.014 | 0.008 |
| Topaz | 0.014 | 0.008 |
| Goshenite | 0.014 | — |
| Apatite | 0.013 | 0.008–0.010 |
| Aventurine | 0.013 | 0.008 |
| Amethyst (SiO2) | 0.013 | 0.008 |
| Citrine quartz | 0.013 | 0.008 |
| Prasiolite | 0.013 | 0.008 |
| Quartz (SiO2) | 0.013 | 0.008 |
| Rose quartz (SiO2) | 0.013 | 0.008 |
| Smoky quartz (SiO2) | 0.013 | 0.008 |
| Anhydrite | 0.013 | — |
| Dolomite | 0.013 | — |
| Morion | 0.013 | — |
| Feldspar | 0.012 | 0.008 |
| Moonstone | 0.012 | 0.008 |
| Orthoclase | 0.012 | 0.008 |
| Pollucite | 0.012 | 0.007 |
| Albite | 0.012 | — |
| Bytownite | 0.012 | — |
| synth. Emerald | 0.012 | — |
| Magnesite (MgCO3) | 0.012 | — |
| Sanidine | 0.012 | — |
| Sunstone | 0.012 | — |
| synth. Alexandrite | 0.011 | — |
| synth. Sapphire (Al2O3) | 0.011 | — |
| Phosphophyllite | 0.010–0.011 | — |
| Phenakite | 0.01 | 0.009 |
| Cancrinite | 0.010 | 0.008–0.009 |
| Leucite | 0.010 | 0.008 |
| Enstatite | 0.010 | — |
| Obsidian | 0.010 | — |
| Anorthite | 0.009–0.010 | — |
| Actinolite | 0.009 | — |
| Jeremejevite | 0.009 | — |
| Nepheline | 0.008–0.009 | — |
| Apophyllite | 0.008 | — |
| Hauyne | 0.008 | — |
| Natrolite | 0.008 | — |
| synth. Quartz (SiO2) | 0.008 | — |
| Aragonite | 0.007–0.012 | — |
| Augelite | 0.007 | — |
| Beryllonite | 0.010 | 0.007 |
| Strontianite | 0.008–0.028 | — |
| Calcite (CaCO3) | 0.008–0.017 | 0.013–0.014 |
| Fluorite (CaF2) | 0.007 | 0.004 |
| Tremolite | 0.006–0.007 | — |

In the technical terminology of gemology, *dispersion* is the difference in the refractive index of a material at the B and G (686.7 nm and 430.8 nm) or C and F (656.3 nm and 486.1 nm) Fraunhofer wavelengths, and is meant to express the degree to which a prism cut from the gemstone demonstrates "fire". Fire is a colloquial term used by gemologists to describe a gemstone's dispersive nature or lack thereof. Dispersion is a material property. The amount of fire demonstrated by a given gemstone is a function of the gemstone's facet angles, the polish quality, the lighting environment, the material's refractive index, the saturation of color, and the orientation of the viewer relative to the gemstone.

## In imaging

In photographic and microscopic lenses, dispersion causes chromatic aberration, which causes the different colors in the image not to overlap properly. Various techniques have been developed to counteract this, such as the use of achromats, multielement lenses with glasses of different dispersion. They are constructed in such a way that the chromatic aberrations of the different parts cancel out.

## Pulsar emissions

Pulsars are spinning neutron stars that emit pulses at very regular intervals ranging from milliseconds to seconds. Astronomers believe that the pulses are emitted simultaneously over a wide range of frequencies. However, as observed on Earth, the components of each pulse emitted at higher radio frequencies arrive before those emitted at lower frequencies. This dispersion occurs because of the ionized component of the interstellar medium, mainly the free electrons, which make the group velocity frequency-dependent. The extra delay added at a frequency ν is

$t=k_{\text{DM}}\cdot \left({\frac {\text{DM}}{\nu ^{2}}}\right),$

where the dispersion constant *k*DM is given by

$k_{\text{DM}}={\frac {e^{2}}{2\pi m_{\text{e}}c}}\approx 4.149~{\text{GHz}}^{2}\,{\text{pc}}^{-1}\,{\text{cm}}^{3}\,{\text{ms}},$

and the **dispersion measure** (DM) is the column density of free electrons (total electron content) – i.e. the number density of electrons *n*e integrated along the path traveled by the photon from the pulsar to the Earth – and is given by

${\text{DM}}=\int _{0}^{d}n_{e}\,dl$

with units of parsecs per cubic centimetre (1 pc/cm3 = 30.857×1021 m−2).

Typically for astronomical observations, this delay cannot be measured directly, since the emission time is unknown. What *can* be measured is the difference in arrival times at two different frequencies. The delay Δ*t* between a high-frequency νhi and a low-frequency νlo component of a pulse will be

$\Delta t=k_{\text{DM}}\cdot {\text{DM}}\cdot \left({\frac {1}{\nu _{\text{lo}}^{2}}}-{\frac {1}{\nu _{\text{hi}}^{2}}}\right).$

Rewriting the above equation in terms of Δ*t* allows one to determine the DM by measuring pulse arrival times at multiple frequencies. This in turn can be used to study the interstellar medium, as well as allow observations of pulsars at different frequencies to be combined.

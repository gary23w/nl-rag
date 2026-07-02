---
title: "Radiance"
source: https://en.wikipedia.org/wiki/Radiance
domain: image-based-lighting
license: CC-BY-SA-4.0
tags: image based lighting, environment map lighting, reflection probe ibl, hdr environment map
fetched: 2026-07-02
---

# Radiance

In radiometry, **radiance** is the radiant flux emitted, reflected, transmitted or received by a given surface, per unit solid angle per unit projected area. Radiance is used to characterize diffuse emission and reflection of electromagnetic radiation, and to quantify emission of neutrinos and other particles. The SI unit of radiance is the watt per steradian per square metre (W·sr−1·m−2). It is a *directional* quantity: the radiance of a surface depends on the direction from which it is being observed.

The related quantity spectral radiance is the radiance of a surface per unit frequency or wavelength, depending on whether the spectrum is taken as a function of frequency or of wavelength.

Historically, radiance was called "intensity" and spectral radiance was called "specific intensity". Many fields still use this nomenclature. It is especially dominant in heat transfer, astrophysics and astronomy. "Intensity" has many other meanings in physics, with the most common being power per unit area (so the radiance is the intensity per solid angle in this case).

## Description

Radiance is useful because it indicates how much of the power emitted, reflected, transmitted, or received by a surface will be received by an optical system looking at that surface from a specified angle of view. In this case, the solid angle of interest is the solid angle subtended by the optical system's entrance pupil. Since the eye is an optical system, radiance and its cousin luminance are good indicators of how bright an object will appear. For this reason, radiance and luminance are both sometimes called "brightness". This usage is now discouraged (see the article Brightness for a discussion). The nonstandard usage of "brightness" for "radiance" persists in some fields, notably laser physics.

The radiance divided by the index of refraction squared is invariant in geometric optics. This means that for an ideal optical system in air, the radiance at the output is the same as the input radiance. This is sometimes called *conservation of radiance*. For real, passive, optical systems, the output radiance is *at most* equal to the input, unless the index of refraction changes. As an example, if you form a demagnified image with a lens, the optical power is concentrated into a smaller area, so the irradiance is higher at the image. The light at the image plane, however, fills a larger solid angle so the radiance comes out to be the same assuming there is no loss at the lens.

Spectral radiance expresses radiance as a function of frequency or wavelength. Radiance is the integral of the spectral radiance over all frequencies or wavelengths. For radiation emitted by the surface of an ideal black body at a given temperature, spectral radiance is governed by Planck's law, while the integral of its radiance, over the hemisphere into which its surface radiates, is given by the Stefan–Boltzmann law. Its surface is Lambertian, so that its radiance is uniform with respect to angle of view, and is simply the Stefan–Boltzmann integral divided by π. This factor is obtained from the solid angle 2π steradians of a hemisphere decreased by integration over the cosine of the zenith angle.

## Mathematical definitions

### Radiance

**Radiance** of a *surface*, denoted *L*e,Ω ("e" for "energetic", to avoid confusion with photometric quantities, and "Ω" to indicate this is a directional quantity), is defined as

$L_{\mathrm {e} ,\Omega }={\frac {\partial ^{2}\Phi _{\mathrm {e} }}{\partial \Omega \,\partial (A\cos \theta )}},$

where

- ∂ is the partial derivative symbol;
- Φe is the radiant flux emitted, reflected, transmitted or received;
- Ω is the solid angle;
- *A* cos *θ* is the *projected* area.

In general *L*e,Ω is a function of viewing direction, depending on *θ* through cos *θ* and azimuth angle through ∂Φe/∂Ω. For the special case of a Lambertian surface, ∂2Φe/(∂Ω ∂*A*) is proportional to cos *θ*, and *L*e,Ω is isotropic (independent of viewing direction).

When calculating the radiance emitted by a source, *A* refers to an area on the surface of the source, and Ω to the solid angle into which the light is emitted. When calculating radiance received by a detector, *A* refers to an area on the surface of the detector and Ω to the solid angle subtended by the source as viewed from that detector. When radiance is conserved, as discussed above, the radiance emitted by a source is the same as that received by a detector observing it.

### Spectral radiance

**Spectral radiance in frequency** of a *surface*, denoted *L*e,Ω,ν, is defined as

$L_{\mathrm {e} ,\Omega ,\nu }={\frac {\partial L_{\mathrm {e} ,\Omega }}{\partial \nu }},$

where *ν* is the frequency.

**Spectral radiance in wavelength** of a *surface*, denoted *L*e,Ω,λ, is defined as

$L_{\mathrm {e} ,\Omega ,\lambda }={\frac {\partial L_{\mathrm {e} ,\Omega }}{\partial \lambda }},$

where *λ* is the wavelength.

## Conservation of basic radiance

Radiance of a surface is related to étendue by

$L_{\mathrm {e} ,\Omega }=n^{2}{\frac {\partial \Phi _{\mathrm {e} }}{\partial G}},$

where

- *n* is the refractive index in which that surface is immersed;
- *G* is the étendue of the light beam.

As the light travels through an ideal optical system, both the étendue and the radiant flux are conserved. Therefore, *basic radiance* defined by

$L_{\mathrm {e} ,\Omega }^{*}={\frac {L_{\mathrm {e} ,\Omega }}{n^{2}}}$

is also conserved. In real systems, the étendue may increase (for example due to scattering) or the radiant flux may decrease (for example due to absorption) and, therefore, basic radiance may decrease. However, étendue may not decrease and radiant flux may not increase and, therefore, basic radiance may not increase.

## SI radiometry units

| Quantity | Unit | Dimension | Notes |   |   |
|---|---|---|---|---|---|
| Name | Symbol | Name | Symbol |   |   |
| Radiant energy | *Q*e | joule | J | **M**⋅**L**2⋅**T**−2 | Energy of electromagnetic radiation. |
| Radiant energy density | *w*e | joule per cubic metre | J/m3 | **M**⋅**L**−1⋅**T**−2 | Radiant energy per unit volume. |
| Radiant flux | Φe | watt | W = J/s | **M**⋅**L**2⋅**T**−3 | Radiant energy emitted, reflected, transmitted or received, per unit time. This is sometimes also called "radiant power", and called luminosity in astronomy. |
| Spectral flux | Φe,*ν* | watt per hertz | W/Hz | **M**⋅**L**2⋅**T** −2 | Radiant flux per unit frequency or wavelength. The latter is commonly measured in W⋅nm−1. |
| Φe,*λ* | watt per metre | W/m | **M**⋅**L**⋅**T**−3 |   |   |
| Radiant intensity | *I*e,Ω | watt per steradian | W/sr | **M**⋅**L**2⋅**T**−3 | Radiant flux emitted, reflected, transmitted or received, per unit solid angle. This is a *directional* quantity. |
| Spectral intensity | *I*e,Ω,*ν* | watt per steradian per hertz | W⋅sr−1⋅Hz−1 | **M**⋅**L**2⋅**T**−2 | Radiant intensity per unit frequency or wavelength. The latter is commonly measured in W⋅sr−1⋅nm−1. This is a *directional* quantity. |
| *I*e,Ω,*λ* | watt per steradian per metre | W⋅sr−1⋅m−1 | **M**⋅**L**⋅**T**−3 |   |   |
| Radiance | *L*e,Ω | watt per steradian per square metre | W⋅sr−1⋅m−2 | **M**⋅**T**−3 | Radiant flux emitted, reflected, transmitted or received by a *surface*, per unit solid angle per unit projected area. This is a *directional* quantity. This is sometimes also called "intensity". |
| Spectral radiance Specific intensity | *L*e,Ω,*ν* | watt per steradian per square metre per hertz | W⋅sr−1⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiance of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅sr−1⋅m−2⋅nm−1. This is a *directional* quantity. This is sometimes also called "spectral intensity". |
| *L*e,Ω,*λ* | watt per steradian per square metre, per metre | W⋅sr−1⋅m−3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Irradiance Flux density | *E*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *received* by a *surface* per unit area. This is sometimes also called "intensity". |
| Spectral irradiance Spectral flux density | *E*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Irradiance of a *surface* per unit frequency or wavelength. This is sometimes also called "spectral intensity". Non-SI units of spectral flux density include jansky (1 Jy = 10−26 W⋅m−2⋅Hz−1) and solar flux unit (1 sfu = 10−22 W⋅m−2⋅Hz−1 = 104 Jy). |
| *E*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiosity | *J*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *leaving* (emitted, reflected and transmitted by) a *surface* per unit area. This is sometimes also called "intensity". |
| Spectral radiosity | *J*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiosity of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅m−2⋅nm−1. This is sometimes also called "spectral intensity". |
| *J*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiant exitance | *M*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *emitted* by a *surface* per unit area. This is the emitted component of radiosity. "Radiant emittance" is an old term for this quantity. This is sometimes also called "intensity". |
| Spectral exitance | *M*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiant exitance of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅m−2⋅nm−1. "Spectral emittance" is an old term for this quantity. This is sometimes also called "spectral intensity". |
| *M*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiant exposure | *H*e | joule per square metre | J/m2 | **M**⋅**T**−2 | Radiant energy received by a *surface* per unit area, or equivalently irradiance of a *surface* integrated over time of irradiation. This is sometimes also called "radiant fluence". |
| Spectral exposure | *H*e,*ν* | joule per square metre per hertz | J⋅m−2⋅Hz−1 | **M**⋅**T**−1 | Radiant exposure of a *surface* per unit frequency or wavelength. The latter is commonly measured in J⋅m−2⋅nm−1. This is sometimes also called "spectral fluence". |
| *H*e,*λ* | joule per square metre, per metre | J/m3 | **M**⋅**L**−1⋅**T**−2 |   |   |
| See also: SIRadiometryPhotometry |   |   |   |   |   |

1. Standards organizations recommend that radiometric quantities should be denoted with suffix "e" (for "energetic") to avoid confusion with photometric or photon quantities.
2. Alternative symbols sometimes seen: W or E for radiant energy, P or F for radiant flux, I for irradiance, W for radiant exitance.
3. Spectral quantities given per unit frequency are denoted with suffix "*ν*" (Greek letter nu, not to be confused with a letter "v", indicating a photometric quantity.)
4. Spectral quantities given per unit wavelength are denoted with suffix "*λ*".
5. Directional quantities are denoted with suffix "Ω".

---
title: "Irradiance"
source: https://en.wikipedia.org/wiki/Irradiance
domain: light-probes
license: CC-BY-SA-4.0
tags: light probe capture, spherical harmonic lighting, irradiance probe, precomputed radiance transfer
fetched: 2026-07-02
---

# Irradiance

In radiometry, **irradiance** is the radiant flux *received* by a *surface* per unit area. The SI unit of irradiance is the watt per square metre (symbol W⋅m−2 or W/m2). The CGS unit erg per square centimetre per second (erg⋅cm−2⋅s−1) is often used in astronomy. Irradiance is often called intensity, but this term is avoided in radiometry where such usage leads to confusion with radiant intensity. In astrophysics, irradiance is called *radiant flux*.

**Spectral irradiance** is the irradiance of a surface per unit frequency or wavelength, depending on whether the spectrum is taken as a function of frequency or of wavelength. The two forms have different dimensions and units: spectral irradiance of a frequency spectrum is measured in watts per square metre per hertz (W⋅m−2⋅Hz−1), while spectral irradiance of a wavelength spectrum is measured in watts per square metre per metre (W⋅m−3), or more commonly watts per square metre per nanometre (W⋅m−2⋅nm−1).

## Mathematical definitions

### Irradiance

Irradiance of a surface, denoted *E*e ("e" for "energetic", to avoid confusion with photometric quantities), is defined as

$E_{\mathrm {e} }={\frac {\partial \Phi _{\mathrm {e} }}{\partial A}},$

where

- ∂ is the partial derivative symbol;
- Φe is the radiant flux received;
- *A* is the area.

The radiant flux *emitted* by a surface is called radiant exitance.

### Spectral irradiance

Spectral irradiance in frequency of a surface, denoted *E*e,ν, is defined as

$E_{\mathrm {e} ,\nu }={\frac {\partial E_{\mathrm {e} }}{\partial \nu }},$

where *ν* is the frequency.

Spectral irradiance in wavelength of a surface, denoted *E*e,λ, is defined as

$E_{\mathrm {e} ,\lambda }={\frac {\partial E_{\mathrm {e} }}{\partial \lambda }},$

where *λ* is the wavelength.

## Property

Irradiance of a surface is also, according to the definition of radiant flux, equal to the time-average of the component of the Poynting vector perpendicular to the surface:

$E_{\mathrm {e} }=\langle |\mathbf {S} |\rangle \cos \alpha ,$

where

- ⟨ • ⟩ is the time-average;
- **S** is the Poynting vector;
- *α* is the angle between a unit vector normal to the surface and **S**.

For a propagating *sinusoidal* linearly polarized electromagnetic plane wave, the Poynting vector always points to the direction of propagation while oscillating in magnitude. The irradiance of a surface is then given by

$E_{\mathrm {e} }={\frac {n}{2\mu _{0}c}}E_{\mathrm {m} }^{2}\cos \alpha ={\frac {n\varepsilon _{0}c}{2}}E_{\mathrm {m} }^{2}\cos \alpha ={\frac {n}{2Z_{0}}}E_{\mathrm {m} }^{2}\cos \alpha ,$

where

- *E*m is the amplitude of the wave's electric field;
- *n* is the refractive index of the medium of propagation;
- *c* is the speed of light in vacuum;

- μ0 is the vacuum permeability;

- ε0 is the vacuum permittivity;
  - ${\textstyle c={\frac {1}{\sqrt {\varepsilon _{0}\mu _{0}}}}}$
  - ${\textstyle Z_{0}=\mu _{0}c}$ is the impedance of free space.

This formula assumes that the magnetic susceptibility is negligible; i.e. that *μ*r ≈ 1 (*μ* ≈ μ0) where *μ*r is the relative magnetic permeability of the propagation medium. This assumption is typically valid in transparent media in the optical frequency range.

## Point source

A point source of light produces spherical wavefronts. The irradiance in this case varies inversely with the square of the distance from the source.

$E={\frac {P}{A}}={\frac {P}{4\pi r^{2}}},$

where

- r is the distance;
- P is the radiant flux;
- A is the surface area of a sphere of radius r.

For quick approximations, this equation indicates that doubling the distance reduces irradiation to one quarter; or similarly, to double irradiation, reduce the distance to 71%.

In astronomy, stars are routinely treated as point sources even though they are much larger than the Earth. This is a good approximation because the distance from even a nearby star to the Earth is much larger than the star's diameter. For instance, the irradiance of Alpha Centauri A (radiant flux: 1.5 L☉, distance: 4.34 ly) is about 2.7 × 10−8 W/m2 on Earth.

## Solar irradiance

The global irradiance on a horizontal surface on Earth consists of the direct irradiance *E*e,dir and diffuse irradiance *E*e,diff. On a tilted plane, there is another irradiance component, *E*e,refl, which is the component that is reflected from the ground. The average ground reflection is about 20% of the global irradiance. Hence, the irradiance *E*e on a tilted plane consists of three components:

$E_{\mathrm {e} }=E_{\mathrm {e} ,\mathrm {dir} }+E_{\mathrm {e} ,\mathrm {diff} }+E_{\mathrm {e} ,\mathrm {refl} }.$

The integral of solar irradiance over a time period is called "solar exposure" or "insolation".

Average solar irradiance at the top of the Earth's atmosphere is roughly 1361 W/m2, but at surface irradiance is approximately 1000 W/m2 on a clear day.

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

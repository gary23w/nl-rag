---
title: "Sound pressure"
source: https://en.wikipedia.org/wiki/Sound_pressure
domain: spatial-audio-hrtf
license: CC-BY-SA-4.0
tags: hrtf spatial audio, head related transfer function, binaural audio rendering, 3d sound localization
fetched: 2026-07-02
---

# Sound pressure

**Sound pressure** or **acoustic pressure** is the local pressure deviation from the ambient (average or equilibrium) atmospheric pressure, caused by a sound wave. In air, sound pressure can be measured using a microphone, and in water with a hydrophone. The SI unit of sound pressure is the pascal (Pa).

## Mathematical definition

A sound wave in a transmission medium causes a deviation (sound pressure, a *dynamic* pressure) in the local ambient pressure, a *static* pressure.

Sound pressure, denoted *p*, is defined by $p_{\text{total}}=p_{\text{stat}}+p,$ where

- *p*total is the total pressure,
- *p*stat is the static pressure.

## Sound measurements

### Sound intensity

In a sound wave, the complementary variable to sound pressure is the particle velocity. Together, they determine the sound intensity of the wave.

*Sound intensity*, denoted **I** and measured in W·m−2 in SI units, is defined by $\mathbf {I} =p\mathbf {v} ,$ where

- *p* is the sound pressure,
- **v** is the particle velocity.

### Acoustic impedance

*Acoustic impedance*, denoted *Z* and measured in Pa·m−3·s in SI units, is defined by $Z(s)={\frac {{\hat {p}}(s)}{{\hat {Q}}(s)}},$ where

- ${\hat {p}}(s)$ is the Laplace transform of sound pressure,
- ${\hat {Q}}(s)$ is the Laplace transform of sound volume flow rate.

*Specific acoustic impedance*, denoted *z* and measured in Pa·m−1·s in SI units, is defined by $z(s)={\frac {{\hat {p}}(s)}{{\hat {v}}(s)}},$ where

- ${\hat {p}}(s)$ is the Laplace transform of sound pressure,
- ${\hat {v}}(s)$ is the Laplace transform of particle velocity.

### Particle displacement

The *particle displacement* of a *progressive sine wave* is given by $\delta (\mathbf {r} ,t)=\delta _{\text{m}}\cos(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{\delta ,0}),$ where

- $\delta _{\text{m}}$ is the amplitude of the particle displacement,
- $\varphi _{\delta ,0}$ is the phase shift of the particle displacement,
- **k** is the angular wavevector,
- *ω* is the angular frequency.

It follows that the particle velocity and the sound pressure along the direction of propagation of the sound wave *x* are given by $v(\mathbf {r} ,t)={\frac {\partial \delta }{\partial t}}(\mathbf {r} ,t)=\omega \delta _{\text{m}}\cos \left(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{\delta ,0}+{\frac {\pi }{2}}\right)=v_{\text{m}}\cos(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{v,0}),$ $p(\mathbf {r} ,t)=-\rho c^{2}{\frac {\partial \delta }{\partial x}}(\mathbf {r} ,t)=\rho c^{2}k_{x}\delta _{\text{m}}\cos \left(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{\delta ,0}+{\frac {\pi }{2}}\right)=p_{\text{m}}\cos(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{p,0}),$ where

- *v*m is the amplitude of the particle velocity,
- $\varphi _{v,0}$ is the phase shift of the particle velocity,
- *p*m is the amplitude of the acoustic pressure,
- $\varphi _{p,0}$ is the phase shift of the acoustic pressure.

Taking the Laplace transforms of *v* and *p* with respect to time yields ${\hat {v}}(\mathbf {r} ,s)=v_{\text{m}}{\frac {s\cos \varphi _{v,0}-\omega \sin \varphi _{v,0}}{s^{2}+\omega ^{2}}},$ ${\hat {p}}(\mathbf {r} ,s)=p_{\text{m}}{\frac {s\cos \varphi _{p,0}-\omega \sin \varphi _{p,0}}{s^{2}+\omega ^{2}}}.$

Since $\varphi _{v,0}=\varphi _{p,0}$ , the amplitude of the specific acoustic impedance is given by $z_{\text{m}}(\mathbf {r} ,s)=|z(\mathbf {r} ,s)|=\left|{\frac {{\hat {p}}(\mathbf {r} ,s)}{{\hat {v}}(\mathbf {r} ,s)}}\right|={\frac {p_{\text{m}}}{v_{\text{m}}}}={\frac {\rho c^{2}k_{x}}{\omega }}.$

Consequently, the amplitude of the particle displacement is related to that of the acoustic velocity and the sound pressure by $\delta _{\text{m}}={\frac {v_{\text{m}}}{\omega }},$ $\delta _{\text{m}}={\frac {p_{\text{m}}}{\omega z_{\text{m}}(\mathbf {r} ,s)}}.$

## Inverse-proportional law

When measuring the sound pressure created by a sound source, it is important to measure the distance from the object as well, since the sound pressure of a *spherical* sound wave decreases as 1/*r* from the centre of the sphere (and not as 1/*r*2, like the sound intensity): $p(r)\propto {\frac {1}{r}}.$

This relationship is an *inverse-proportional law*.

If the sound pressure *p*1 is measured at a distance *r*1 from the centre of the sphere, the sound pressure *p*2 at another position *r*2 can be calculated: $p_{2}={\frac {r_{1}}{r_{2}}}\,p_{1}.$

The inverse-proportional law for sound pressure comes from the inverse-square law for sound intensity: $I(r)\propto {\frac {1}{r^{2}}}.$ Indeed, $I(r)=p(r)v(r)=p(r)\left[p*z^{-1}\right](r)\propto p^{2}(r),$ where

- v is the particle velocity,
- * is the convolution operator,
- *z*−1 is the convolution inverse of the specific acoustic impedance,

hence the inverse-proportional law: $p(r)\propto {\frac {1}{r}}.$

## Sound pressure level

**Sound pressure level** (**SPL**) or **acoustic pressure level** (**APL**) is a logarithmic measure of the effective pressure of a sound relative to a reference value.

Sound pressure level, denoted *L**p* and measured in dB, is defined by: $L_{p}=\ln \left({\frac {p^{2}}{p_{0}^{2}}}\right)~{\text{Np}}=2\log _{10}\left({\frac {p}{p_{0}}}\right)~{\text{B}}=20\log _{10}\left({\frac {p}{p_{0}}}\right)~{\text{dB}},$ where

- *p* is the root mean square sound pressure,
- *p*0 is a **reference sound pressure**,
- 1 Np is the neper,
- 1 B = (⁠1/2⁠ ln 10) Np is the bel,
- 1 dB = (⁠1/20⁠ ln 10) Np is the decibel.

The commonly used reference sound pressure in air is

p

0

= 20 μPa,

which is often considered as the threshold of human hearing (roughly the sound of a mosquito flying 3 m away). The proper notations for sound pressure level using this reference are *L**p*/(20 μPa) or *L**p* (re 20 μPa), but the suffix notations dB SPL, dB(SPL), dBSPL, and dBSPL are very common, even if they are not accepted by the SI.

Most sound-level measurements will be made relative to this reference, meaning 1 Pa will equal an SPL of $20\log _{10}\left({\frac {1}{2\times 10^{-5}}}\right)~{\text{dB}}\approx 94~{\text{dB}}$ . In other media, such as underwater, a reference level of 1 μPa is used. These references are defined in ANSI S1.1-2013.

The main instrument for measuring sound levels in the environment is the sound level meter. Most sound level meters provide readings in A, C, and Z-weighted decibels and must meet international standards such as IEC 61672-2013.

### Examples

The lower limit of audibility is defined as SPL of 0 dB, but the upper limit is not as clearly defined. While 1 atm (194 dB peak or 191 dB SPL) is the largest pressure variation an undistorted sound wave can have in Earth's atmosphere (i. e., if the thermodynamic properties of the air are disregarded; in reality, the sound waves become progressively non-linear starting over 150 dB), larger sound waves can be present in other atmospheres or other media, such as underwater or through the Earth.

Ears detect changes in sound pressure. Human hearing does not have a flat spectral sensitivity (frequency response) relative to frequency versus amplitude. Humans do not perceive low- and high-frequency sounds as well as they perceive sounds between 3,000 and 4,000 Hz, as shown in the equal-loudness contour. Because the frequency response of human hearing changes with amplitude, three weightings have been established for measuring sound pressure: A, B and C.

In order to distinguish the different sound measures, a suffix is used: A-weighted sound pressure level is written either as dBA or LA, B-weighted sound pressure level is written either as dBB or LB, and C-weighted sound pressure level is written either as dBC or LC. Unweighted sound pressure level is called "linear sound pressure level" and is often written as dBL or just L. Some sound measuring instruments use the letter "Z" as an indication of linear SPL.

### Distance

The distance of the measuring microphone from a sound source is often omitted when SPL measurements are quoted, making the data useless, due to the inherent effect of the inverse proportional law. In the case of ambient environmental measurements of "background" noise, distance need not be quoted, as no single source is present, but when measuring the noise level of a specific piece of equipment, the distance should always be stated. A distance of one metre (1 m) from the source is a frequently used standard distance. Because of the effects of reflected noise within a closed room, the use of an anechoic chamber allows sound to be comparable to measurements made in a free field environment.

According to the inverse proportional law, when sound level *L**p*1 is measured at a distance *r*1, the sound level *L**p*2 at the distance *r*2 is $L_{p_{2}}=L_{p_{1}}+20\log _{10}\left({\frac {r_{1}}{r_{2}}}\right)~{\text{dB}}.$

### Multiple sources

The formula for the sum of the sound pressure levels of *n* incoherent radiating sources is $L_{\Sigma }=10\log _{10}\left({\frac {p_{1}^{2}+p_{2}^{2}+\dots +p_{n}^{2}}{p_{0}^{2}}}\right)~{\text{dB}}=10\log _{10}\left[\left({\frac {p_{1}}{p_{0}}}\right)^{2}+\left({\frac {p_{2}}{p_{0}}}\right)^{2}+\dots +\left({\frac {p_{n}}{p_{0}}}\right)^{2}\right]~{\text{dB}}.$

Inserting the formulas $\left({\frac {p_{i}}{p_{0}}}\right)^{2}=10^{\frac {L_{i}}{10~{\text{dB}}}},\quad i=1,2,\ldots ,n$ in the formula for the sum of the sound pressure levels yields $L_{\Sigma }=10\log _{10}\left(10^{\frac {L_{1}}{10~{\text{dB}}}}+10^{\frac {L_{2}}{10~{\text{dB}}}}+\dots +10^{\frac {L_{n}}{10~{\text{dB}}}}\right)~{\text{dB}}.$

## Examples of sound pressure

| Source of sound | Distance | Sound pressure level |   |
|---|---|---|---|
| (Pa) | (dBSPL) |   |   |
| Shock wave (distorted sound waves > 1 atm; waveform valleys are clipped at zero pressure) |   | >1×105 | >191 |
| Simple open-ended thermoacoustic device |   | 1.3×104 | 176 |
| 1883 eruption of Krakatoa | 165 km | 8×103 | 172 |
| .30-06 rifle being fired | 1 m to shooter's side | 7×103 | 171 |
| Firecracker | 0.5 m | 7×103 | 171 |
| Stun grenade | Ambient | (1.6–8)×103 | 158–172 |
| 9-inch (23 cm) party balloon inflated to rupture | At ear | 4.9×103 | 168 |
| 9-inch (23 cm) diameter balloon crushed to rupture | At ear | 1.8×103 | 159 |
| 9-inch (23 cm) party balloon inflated to rupture | 0.5 m | 1.4×103 | 157 |
| 9-inch (23 cm) diameter balloon popped with a pin | At ear | 1.1×103 | 155 |
| LRAD 1000Xi Long Range Acoustic Device | 1 m | 8.9×102 | 153 |
| 9-inch (23 cm) party balloon inflated to rupture | 1 m | 730 | 151 |
| Jet engine | 1 m | 630 | 150 |
| 9-inch (23 cm) diameter balloon crushed to rupture | 0.95 m | 450 | 147 |
| 9-inch (23 cm) diameter balloon popped with a pin | 1 m | 280 | 143 |
| Maximum instantaneous peak (C-weighted) for amplified sound at "safe listening" venues/events per WHO's global standard | Ambient | 200 | 140 |
| Instantaneous peak workplace noise (C-weighted) which legally obligates use of hearing protection by workers in the EU | At ear | 140 | 137 |
| Instantaneous peak workplace noise (C-weighted) which legally obligates employers to offer hearing protectors to workers in the EU | At ear | 112 | 135 |
| Loudest human voice | 1 inch | 110 | 135 |
| Trumpet | 0.5 m | 63.2 | 130 |
| Vuvuzela horn | 1 m | 20.0 | 120 |
| Threshold of pain | At ear | 20–100 | 120–134 |
| Risk of instantaneous noise-induced hearing loss | At ear | 20.0 | 120 |
| Maximum instantaneous peak (C-weighted) for amplified sound at children's venues/events complying with WHO's global safe listening standard | Ambient | 20.0 | 120 |
| Jet engine | 100–30 m | 6–200 | 110–140 |
| Two-stroke chainsaw | 1 m | 6 | 110 |
| Jackhammer | 1 m | 2.00 | 100 |
| Sound level limit (A-weighted, moving average over 15-minute interval) at safe listening venues/events per WHO global standard | Ambient | 2.00 | 100 |
| NIOSH recommended exposure limit (REL) for workplace noise (15-minute average, A-weighted) | At ear | 2.00 | 100 |
| NIOSH REL for workplace noise (30-minute average, A-weighted) | At ear | 1.42 | 97 |
| Sound level limit (A-weighted, moving average over 15-minute interval) at children's venues/events per WHO's "safe listening" global standard | Ambient | 1.0 | 94 |
| NIOSH REL for workplace noise (1-hour average, A-weighted) | At ear | 1.0 | 94 |
| NIOSH REL for workplace noise (2-hour average, A-weighted) | At ear | 0.71 | 91 |
| Sound level limit (A-weighted, moving average over 15-minute interval) at venues/events for "young children" per WHO's safe listening global standard | Ambient | 0.63 | 90 |
| NIOSH REL for workplace noise (4-hour average, A-weighted) | At ear | 0.50 | 88 |
| NIOSH recommended exposure limit (REL) for workplace noise (average over 8-hour workday, A-weighted) | At ear | 0.36 | 85 |
| Hearing damage (over long-term exposure, need not be continuous) | At ear | 0.36 | 85 |
| Workplace noise level (8-hour daily average, A-weighted) that legally obligates use of hearing protection by workers in the EU | At ear | 0.36 | 85 |
| Vacuum cleaner, A-weighted (1981) | 1.8 m | 0.36 | 85 |
| Workplace noise level (8-hour daily average, A-weighted) that legally obligates employers to offer hearing protectors to workers in the EU | At ear | 0.2 | 80 |
| Average level (A-weighted) at 40 hours per week (on a rolling basis) equivalent to the "sound allowance" for a "safe listening device" in "Mode 1: WHO standard level for adults" per WHO/ITU-T Rec. H.870 | At ear | 0.2 | 80 |
| Average level (A-weighted) at 40 hours per week (on a rolling basis) equivalent to the "sound allowance" for a "safe listening device" in "Mode 2: WHO standard level for sensitive users (e.g. children)" per WHO/ITU-T Rec. H.870 | At ear | 0.11 | 75 |
| Television (A-weighted) | Ambient | 0.11 | 75 |
| EPA-identified maximum to protect against hearing loss and other disruptive effects from noise, such as sleep disturbance, stress, learning detriment, etc. | Ambient | 0.06 | 70 |
| Passenger car at 30 km/h (electric and combustion engines) | 10 m | 0.04–0.06 | 65–70 |
| Normal conversation | 1 m | 2×10−3–0.02 | 40–60 |
| Passenger car at 10 km/h (combustion) | 10 m | 13×10−3 | 56 |
| Passenger car at 10 km/h (electric) | 10 m | 6×10−3 | 50 |
| Very calm room | Ambient | (2–6)×10−4 | 20–30 |
| Light leaf rustling, calm breathing | Ambient | 6×10−5 | 10 |
| Auditory threshold at 1 kHz | At ear | 2.00×10−5 | 0 |
| Anechoic chamber, Orfield Labs, A-weighted | Ambient | 6.8×10−6 | −9.4 |
| Anechoic chamber, University of Salford, A-weighted | Ambient | 4.8×10−6 | −12.4 |
| Anechoic chamber, Microsoft, A-weighted | Ambient | 1.90×10−6 | −20.35 |

1. All values listed are the effective sound pressure unless otherwise stated.

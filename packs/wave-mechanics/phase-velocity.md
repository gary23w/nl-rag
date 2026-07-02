---
title: "Phase velocity"
source: https://en.wikipedia.org/wiki/Phase_velocity
domain: wave-mechanics
license: CC-BY-SA-4.0
tags: wave equation, dispersion relation, group velocity, wave packet
fetched: 2026-07-02
---

# Phase velocity

The **phase velocity** of a wave is the speed of any wavefront, a surface of constant phase. This is the velocity at which the phase of any constant-frequency component of the wave travels. For such a spectral component, any given phase of the wave (for example, the crest) will appear to travel at the phase velocity. The phase velocity of light waves is not a physically meaningful quantity and is not related to information transfer.

## Sinusoidal or plane waves

For a simple sinusoidal wave the phase velocity is given in terms of the wavelength λ (lambda) and time period T as $v_{\mathrm {p} }={\frac {\lambda }{T}}.$ Equivalently, in terms of the wave's angular frequency ω, which specifies angular change per unit of time, and wavenumber (or angular wave number) k, which represent the angular change per unit of space,

$v_{\mathrm {p} }={\frac {\omega }{k}}.$

## Beats

The previous definition of phase velocity has been demonstrated for an isolated wave. However, such a definition can be extended to a beat of waves, or to a signal composed of multiple waves. For this it is necessary to mathematically write the beat or signal as a low frequency envelope multiplying a carrier. Thus the phase velocity of the carrier determines the phase velocity of the wave set.

## Dispersion

In the context of electromagnetics and optics, the frequency is some function *ω*(*k*) of the wave number, so in general, the phase velocity and the group velocity depend on specific medium and frequency. The ratio between the speed of light *c* and the phase velocity *v**p* is known as the refractive index, *n* = *c* / *v**p* = *ck* / *ω*.

In this way, we can obtain another form for group velocity for electromagnetics. Writing *n* = *n*(ω), a quick way to derive this form is to observe $k={\frac {1}{c}}\omega n(\omega )\implies dk={\frac {1}{c}}\left(n(\omega )+\omega {\frac {\partial }{\partial \omega }}n(\omega )\right)d\omega .$ We can then rearrange the above to obtain $v_{g}={\frac {\partial w}{\partial k}}={\frac {c}{n+\omega {\frac {\partial n}{\partial \omega }}}}.$

From this formula, we see that the group velocity is equal to the phase velocity only when the refractive index is independent of frequency ${\textstyle \partial n/\partial \omega =0}$ . When this occurs, the medium is called non-dispersive, as opposed to dispersive, where various properties of the medium depend on the frequency ω. The relation $\omega (k)$ is known as the dispersion relation of the medium.

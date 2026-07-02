---
title: "Cutoff frequency"
source: https://en.wikipedia.org/wiki/Cutoff_frequency
domain: waveguides
license: CC-BY-SA-4.0
tags: rectangular waveguide, cutoff frequency, transverse mode, waveguide filter
fetched: 2026-07-02
---

# Cutoff frequency

In physics and electrical engineering, a **cutoff frequency**, **corner frequency**, or **break frequency** is a boundary in a system's frequency response at which energy flowing through the system begins to be reduced (attenuated or reflected) rather than passing through.

Typically in electronic systems such as filters and communication channels, cutoff frequency applies to an edge in a lowpass, highpass, bandpass, or band-stop characteristic – a frequency characterizing a boundary between a passband and a stopband. It is sometimes taken to be the point in the filter response where a transition band and passband meet, for example, as defined by a **half-power bandwidth** (or half-power point), a frequency for which the output of the circuit is approximately −3.01 dB of the nominal passband value. Alternatively, a stopband corner frequency may be specified as a point where a transition band and a stopband meet: a frequency for which the attenuation is larger than the required stopband attenuation, which for example may be 30 dB or 100 dB.

In the case of a waveguide or an antenna, the cutoff frequencies correspond to the lower and upper **cutoff wavelengths**.

## Electronics

In electronics, cutoff frequency or corner frequency is the frequency either above or below which the power output of a circuit, such as a line, amplifier, or electronic filter has fallen to a given proportion of the power in the passband. Most frequently this proportion is one half the passband power, also referred to as the 3 dB point since a fall of 3 dB corresponds approximately to half power. As a voltage ratio this is a fall to ${\textstyle {\sqrt {1/2}}\ \approx \ 0.707}$ of the passband voltage.

The **half-power bandwidth** is a commonly used definition for the cutoff frequency. This occurs when the output voltage has dropped to ${\tfrac {1}{\sqrt {2}}}\approx {\text{0.707}}$ of the filter's nominal passband voltage and the power has dropped by half. A bandpass amplifier will have two half-power points, while a low-pass amplifier or a high-pass amplifier will have only one.

The bandwidth of a filter or amplifier is usually defined as the difference between the lower and upper half-power points. This is, therefore, also known as the 3 dB bandwidth. There is no lower half-power point for a low-pass amplifier, so the bandwidth is measured relative to DC, i.e., 0 Hz. There is no upper half-power point for an ideal high-pass amplifier, its bandwidth is theoretically infinite. In practice the stopband and transition band are used to characterize a high-pass.

Other ratios besides the 3 dB point may also be relevant, for example see § Chebyshev filters below. Far from the cutoff frequency in the transition band, the rate of increase of attenuation (roll-off) with logarithm of frequency is asymptotic to a constant. For a first-order network, the roll-off is −20 dB per decade (approximately −6 dB per octave.)

### Single-pole transfer function example

The transfer function for the simplest low-pass filter, $H(s)={\frac {1}{1+\alpha s}},$ has a single pole at *s* = −1/*α*. The magnitude of this function in the *jω* plane is $\left|H(j\omega )\right|=\left|{\frac {1}{1+\alpha j\omega }}\right|={\sqrt {\frac {1}{1+\alpha ^{2}\omega ^{2}}}}.$

At cutoff $\left|H(j\omega _{\mathrm {c} })\right|={\frac {1}{\sqrt {2}}}={\sqrt {\frac {1}{1+\alpha ^{2}\omega _{\mathrm {c} }^{2}}}}.$

Hence, the cutoff frequency is given by $\omega _{\mathrm {c} }={\frac {1}{\alpha }}.$

Where s is the s-plane variable, ω is angular frequency and *j* is the imaginary unit.

### Chebyshev filters

Sometimes other ratios are more convenient than the 3 dB point. For instance, in the case of the Chebyshev filter it is usual to define the cutoff frequency as the point after the last peak in the frequency response at which the level has fallen to the design value of the passband ripple. The amount of ripple in this class of filter can be set by the designer to any desired value, hence the ratio used could be any value.

## Radio communications

In radio communication, skywave communication is a technique in which radio waves are transmitted at an angle into the sky and reflected back to Earth by layers of charged particles in the ionosphere. In this context, the term *cutoff frequency* refers to the maximum usable frequency, the frequency above which a radio wave fails to reflect off the ionosphere at the incidence angle required for transmission between two specified points by reflection from the layer.

## Waveguides

The cutoff frequency of an electromagnetic waveguide is the lowest frequency for which a mode will propagate in it. In fiber optics, it is more common to consider the **cutoff wavelength**, the maximum wavelength that will propagate in an optical fiber or waveguide. The cutoff frequency is found with the characteristic equation of the Helmholtz equation for electromagnetic waves, which is derived from the electromagnetic wave equation by setting the longitudinal wave number equal to zero and solving for the frequency. Thus, any exciting frequency lower than the cutoff frequency will attenuate, rather than propagate. The following derivation assumes lossless walls. The value of c, the speed of light, should be taken to be the group velocity of light in whatever material fills the waveguide.

For a rectangular waveguide, the cutoff frequency is $\omega _{c}=c{\sqrt {\left({\frac {m\pi }{a}}\right)^{2}+\left({\frac {n\pi }{b}}\right)^{2}}},$ where $m,n\geq 0$ are the mode numbers for the rectangle's sides of length a and b respectively. For TE modes, $m,n\geq 0$ (but $m=n=0$ is not allowed), while for TM modes $m,n\geq 1$ .

The cutoff frequency of the TM01 mode (next higher from dominant mode TE11) in a waveguide of circular cross-section (the transverse-magnetic mode with no angular dependence and lowest radial dependence) is given by $\omega _{c}=c{\frac {\chi _{01}}{r}}=c{\frac {2.4048}{r}},$ where r is the radius of the waveguide, and $\chi _{01}$ is the first root of $J_{0}(r)$ , the Bessel function of the first kind of order 1.

The dominant mode TE11 cutoff frequency is given by $\omega _{c}=c{\frac {\chi _{11}}{r}}=c{\frac {1.8412}{r}}$

However, the dominant mode cutoff frequency can be reduced by the introduction of baffle inside the circular cross-section waveguide. For a single-mode optical fiber, the cutoff wavelength is the wavelength at which the normalized frequency is approximately equal to 2.405.

### Mathematical analysis

The starting point is the wave equation (which is derived from the Maxwell equations), $\left(\nabla ^{2}-{\frac {1}{c^{2}}}{\frac {\partial ^{2}}{\partial {t}^{2}}}\right)\psi (\mathbf {r} ,t)=0,$ which becomes a Helmholtz equation by considering only functions of the form $\psi (x,y,z,t)=\psi (x,y,z)e^{i\omega t}.$ Substituting and evaluating the time derivative gives $\left(\nabla ^{2}+{\frac {\omega ^{2}}{c^{2}}}\right)\psi (x,y,z)=0.$ The function $\psi$ here refers to whichever field (the electric field or the magnetic field) has no vector component in the longitudinal direction - the "transverse" field. It is a property of all the eigenmodes of the electromagnetic waveguide that at least one of the two fields is transverse. The *z* axis is defined to be along the axis of the waveguide.

The "longitudinal" derivative in the Laplacian can further be reduced by considering only functions of the form $\psi (x,y,z,t)=\psi (x,y)e^{i\left(\omega t-k_{z}z\right)},$ where $k_{z}$ is the longitudinal wavenumber, resulting in $\left(\nabla _{T}^{2}-k_{z}^{2}+{\frac {\omega ^{2}}{c^{2}}}\right)\psi (x,y,z)=0,$ where subscript T indicates a 2-dimensional transverse Laplacian. The final step depends on the geometry of the waveguide. The easiest geometry to solve is the rectangular waveguide. In that case, the remainder of the Laplacian can be evaluated to its characteristic equation by considering solutions of the form $\psi (x,y,z,t)=\psi _{0}e^{i\left(\omega t-k_{z}z-k_{x}x-k_{y}y\right)}.$ Thus for the rectangular guide the Laplacian is evaluated, and we arrive at ${\frac {\omega ^{2}}{c^{2}}}=k_{x}^{2}+k_{y}^{2}+k_{z}^{2}$ The transverse wavenumbers can be specified from the standing wave boundary conditions for a rectangular geometry cross-section with dimensions a and b: $k_{x}={\frac {n\pi }{a}},$ $k_{y}={\frac {m\pi }{b}},$ where n and m are the two integers representing a specific eigenmode. Performing the final substitution, we obtain ${\frac {\omega ^{2}}{c^{2}}}=\left({\frac {n\pi }{a}}\right)^{2}+\left({\frac {m\pi }{b}}\right)^{2}+k_{z}^{2},$ which is the dispersion relation in the rectangular waveguide. The cutoff frequency $\omega _{c}$ is the critical frequency between propagation and attenuation, which corresponds to the frequency at which the longitudinal wavenumber $k_{z}$ is zero. It is given by $\omega _{c}=c{\sqrt {\left({\frac {n\pi }{a}}\right)^{2}+\left({\frac {m\pi }{b}}\right)^{2}}}$ The wave equations are also valid below the cutoff frequency, where the longitudinal wave number is imaginary. In this case, the field decays exponentially along the waveguide axis and the wave is thus evanescent.

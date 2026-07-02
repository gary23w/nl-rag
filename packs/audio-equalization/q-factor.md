---
title: "Q factor"
source: https://en.wikipedia.org/wiki/Q_factor
domain: audio-equalization
license: CC-BY-SA-4.0
tags: audio equalization, parametric equalizer, iir filter eq, audio filter dsp
fetched: 2026-07-02
---

# *Q* factor

In physics and engineering, the **quality factor** or **Q factor** is a dimensionless parameter that describes how underdamped an oscillator or resonator is. Resonators with high quality factors have low damping, so that they ring or vibrate longer. For example, a pendulum suspended from a precision bearing, oscillating in air, has a high Q, while a pendulum immersed in oil has a low one.

There are two definitions of Q that give numerically similar, but not identical, results. The more general definition is the ratio of the initial energy stored in the resonator to the energy lost in one radian of the cycle of oscillation. An alternative definition of Q factor, more applicable to high Q oscillators, is as the ratio of a resonator's centre frequency to its bandwidth when subject to an oscillating driving force.

## Explanation

The Q factor is a parameter that describes the resonance behavior of a damped harmonic oscillator (resonator). Sinusoidally driven resonators having higher Q factors resonate with greater amplitudes (at the resonant frequency) but have a smaller range of frequencies around that frequency for which they resonate; the range of frequencies for which the oscillator resonates is called the bandwidth. Thus, a high-Q tuned circuit in a radio receiver would be more difficult to tune, but would have more selectivity; it would do a better job of filtering out signals from other stations that lie nearby on the spectrum. High-Q oscillators oscillate with a smaller range of frequencies and are more stable.

The quality factor of devices varies substantially from system to system, depending on their function and design. Systems for which damping is important (such as dampers keeping a door from slamming shut) have Q near 1⁄2. Clocks, lasers, and other resonating systems that need either strong resonance or high frequency stability have high quality factors. Tuning forks have quality factors around 1000. The quality factor of atomic clocks, superconducting RF cavities used in accelerators, and some high-Q lasers can reach 1011 and higher.

There are many alternative quantities used by physicists and engineers to describe how damped an oscillator is. Important examples include: the damping ratio, relative bandwidth, linewidth and bandwidth measured in octaves.

The concept of Q originated with K. S. Johnson of Western Electric Company's Engineering Department while evaluating the quality of coils (inductors). His choice of the symbol Q was only because, at the time, all other letters of the alphabet were taken. The term was not intended as an abbreviation for "quality" or "quality factor", although these terms have grown to be associated with it.

## Definition

The definition of Q since its first use in 1914 has been generalized to apply to coils and condensers, resonant circuits, resonant devices, resonant transmission lines, cavity resonators,. It has expanded beyond the electronics field to apply to dynamical systems in general: mechanical and acoustic resonators, material Q and quantum systems such as spectral lines and particle resonances, and optical resonators such as laser cavities. There are two common definitions for Q, which apply generally to all these systems but are not exactly equivalent. They become approximately equivalent as Q becomes larger, meaning the resonator becomes less damped.

### Bandwidth definition

One of these definitions, which is more applicable to high Q devices, is the frequency-to-bandwidth ratio of the resonator:

$Q\mathrel {\stackrel {\text{def}}{=}} {\frac {f_{\mathrm {r} }}{\Delta f}}={\frac {\omega _{\mathrm {r} }}{\Delta \omega }},$

where *f*r is the resonant frequency, Δ*f* is the **resonance width** or full width at half maximum (FWHM) i.e. the bandwidth over which the power of vibration is greater than half the power at the resonant frequency, *ω*r = 2*πf*r is the angular resonant frequency, and Δ*ω* is the angular half-power bandwidth.

Under this definition, Q is the reciprocal of fractional bandwidth.

### Stored energy definition

The other common nearly equivalent definition for Q is the ratio of the energy stored in the oscillating resonator to the energy dissipated per cycle by damping processes:

$Q\mathrel {\stackrel {\text{def}}{=}} 2\pi \times {\frac {\text{energy stored}}{\text{energy dissipated per cycle}}}=2\pi f_{\mathrm {r} }\times {\frac {\text{energy stored}}{\text{power loss}}}.$

The factor 2*π* makes Q expressible in simpler terms, involving only the coefficients of the second-order differential equation describing most resonant systems, electrical or mechanical. In electrical systems, the stored energy is the sum of energies stored in lossless inductors and capacitors; the lost energy is the sum of the energies dissipated in resistors per cycle. In mechanical systems, the stored energy is the sum of the potential and kinetic energies at some point in time; the lost energy is the work done by an external force, per cycle, to maintain amplitude.

More generally and in the context of reactive component specification (especially inductors), the frequency-dependent definition of Q is used:

$Q(\omega )=\omega \times {\frac {\text{maximum energy stored}}{\text{power loss}}},$

where ω is the angular frequency at which the stored energy and power loss are measured. This definition is consistent with its usage in describing circuits with a single reactive element (capacitor or inductor), where it can be shown to be equal to the ratio of reactive power to real power. (*See* Individual reactive components.)

## Q-factor and damping

The Q-factor determines the qualitative behavior of simple damped oscillators. (For mathematical details about these systems and their behavior see harmonic oscillator and linear time invariant (LTI) system.)

Starting from the stored energy definition, it can be shown that $Q={\frac {1}{2\zeta }}$ , where $\zeta$ is the damping ratio. There are three key distinct cases:

- A system with **low quality factor** (*Q* < ⁠1/2⁠) is said to be **overdamped**. Such a system doesn't oscillate at all, but when displaced from its equilibrium steady-state output it returns to it by exponential decay, approaching the steady state value asymptotically. It has an impulse response that is the sum of two decaying exponential functions with different rates of decay. As the quality factor decreases the slower decay mode becomes stronger relative to the faster mode and dominates the system's response resulting in a slower system. A second-order low-pass filter with a very low quality factor has a nearly first-order step response; the system's output responds to a step input by slowly rising toward an asymptote.
- A system with **high quality factor** (*Q* > ⁠1/2⁠) is said to be **underdamped**. Underdamped systems combine oscillation at a specific frequency with a decay of the amplitude of the signal. Underdamped systems with a low quality factor (a little above *Q* = ⁠1/2⁠) may oscillate only once or a few times before dying out. As the quality factor increases, the relative amount of damping decreases. A high-quality bell rings with a single pure tone for a very long time after being struck. A purely oscillatory system, such as a bell that rings forever, has an infinite quality factor. More generally, the output of a second-order low-pass filter with a very high quality factor responds to a step input by quickly rising above, oscillating around, and eventually converging to a steady-state value.
- A system with an **intermediate quality factor** (*Q* = ⁠1/2⁠) is said to be **critically damped**. Like an overdamped system, the output does not oscillate, and does not overshoot its steady-state output (i.e., it approaches a steady-state asymptote). Like an underdamped response, the output of such a system responds quickly to a unit step input. Critical damping results in the fastest response (approach to the final value) possible without overshoot. Real system specifications usually allow some overshoot for a faster initial response or require a slower initial response to provide a safety margin against overshoot.

In negative feedback systems, the dominant closed-loop response is often well-modeled by a second-order system. The phase margin of the open-loop system sets the quality factor Q of the closed-loop system; as the phase margin decreases, the approximate second-order closed-loop system is made more oscillatory (i.e., has a higher quality factor).

### Some examples

- A unity-gain Sallen–Key lowpass filter topology with equal capacitors and equal resistors is critically damped (i.e., *Q* = ⁠1/2⁠).
- A second-order Bessel filter (i.e., continuous-time filter with flattest group delay) has an underdamped *Q* = ⁠1/√3⁠.
- A second-order Butterworth filter (i.e., continuous-time filter with the flattest passband frequency response) has an underdamped *Q* = ⁠1/√2⁠.
- A pendulum's Q-factor is: *Q* = *Mω*/*Γ*, where M is the mass of the bob, *ω* = 2*π*/*T* is the pendulum's radian frequency of oscillation, and Γ is the frictional damping force on the pendulum per unit velocity.
- The design of a high-energy (near terahertz) gyrotron considers both diffractive Q-factor, ${\textstyle Q_{D}\approx 30\left({\frac {L}{\lambda }}\right)^{2}}$ as a function of resonator length L, wavelength λ, and ohmic Q-factor (TE*m,p*–modes) $Q_{\Omega }={\frac {R_{\mathrm {w} }}{\delta }}{\frac {1-m^{2}}{v_{m,p}^{2}}},$ where *R*w is the cavity wall radius, δ is the skin depth of the cavity wall, vm,p is the eigenvalue scalar (m is the azimuth index, p is the radial index; in this application, skin depth is ${\textstyle \delta ={1}/{\sqrt {\pi f\sigma u_{o}}}}$ )
- In medical ultrasonography, a transducer with a high Q-factor is suitable for doppler ultrasonography because of its long ring-down time, where it can measure the velocities of blood flow. Meanwhile, a transducer with a low Q-factor has a short ring-down time and is suitable for organ imaging because it can receive a broad range of reflected echoes from bodily organs.

## Physical interpretation

Physically speaking, Q is approximately the ratio of the stored energy to the energy dissipated over one radian of the oscillation; or nearly equivalently, at high enough Q values, 2π times the ratio of the total energy stored and the energy lost in a single cycle.

It is a dimensionless parameter that compares the exponential time constant τ for decay of an oscillating physical system's amplitude to its oscillation period. Equivalently, it compares the frequency at which a system oscillates to the rate at which it dissipates its energy. More precisely, the frequency and period used should be based on the system's natural frequency, which at low Q values is somewhat higher than the oscillation frequency as measured by zero crossings.

Equivalently (for large values of Q), the Q factor is approximately the number of oscillations required for a freely oscillating system's energy to fall off to *e*−2*π*, or about 1⁄535 or 0.2%, of its original energy. This means the amplitude falls off to approximately *e*−*π* or 4% of its original amplitude.

The width (bandwidth) of the resonance is given by (approximately): $\Delta f={\frac {f_{\mathrm {N} }}{Q}},\,$ where *f*N is the natural frequency, and Δ*f*, the bandwidth, is the width of the range of frequencies for which the energy is at least half its peak value.

The resonant frequency is often expressed in natural units (radians per second), rather than using the *f*N in hertz, as $\omega _{\mathrm {N} }=2\pi f_{\mathrm {N} }.$

The factors Q, damping ratio ζ, natural frequency *ω*N, attenuation rate α, and exponential time constant τ are related such that:

$Q={\frac {1}{2\zeta }}={\frac {\omega _{\mathrm {N} }}{2\alpha }}={\frac {\tau \omega _{\mathrm {N} }}{2}},$

and the damping ratio can be expressed as:

$\zeta ={\frac {1}{2Q}}={\alpha \over \omega _{\mathrm {N} }}={1 \over \tau \omega _{\mathrm {N} }}.$

The envelope of oscillation decays proportional to *e*−*αt* or *e*−*t/τ*, where α and τ can be expressed as:

$\alpha ={\omega _{\mathrm {N} } \over 2Q}=\zeta \omega _{\mathrm {N} }={1 \over \tau }$ and $\tau ={2Q \over \omega _{\mathrm {N} }}={1 \over \zeta \omega _{\mathrm {N} }}={\frac {1}{\alpha }}.$

The energy of oscillation, or the power dissipation, decays twice as fast, that is, as the square of the amplitude, as *e*−2*αt* or *e*−2*t/τ*.

For a two-pole lowpass filter, the transfer function of the filter is

$H(s)={\frac {\omega _{\mathrm {N} }^{2}}{s^{2}+\underbrace {\frac {\omega _{\mathrm {N} }}{Q}} _{2\zeta \omega _{\mathrm {N} }=2\alpha }s+\omega _{\mathrm {N} }^{2}}}\,$

For this system, when *Q* > ⁠1/2⁠ (i.e., when the system is underdamped), it has two complex conjugate poles that each have a real part of −α. That is, the attenuation parameter α represents the rate of exponential decay of the oscillations (that is, of the output after an impulse) into the system. A higher quality factor implies a lower attenuation rate, and so high-Q systems oscillate for many cycles. For example, high-quality bells have an approximately pure sinusoidal tone for a long time after being struck by a hammer.

| Filter type (2nd order) | Transfer function *H*(*s*) |
|---|---|
| Lowpass | ${\frac {\omega _{\mathrm {N} }^{2}}{s^{2}+{\frac {\omega _{\mathrm {N} }}{Q}}s+\omega _{\mathrm {N} }^{2}}}$ |
| Bandpass | ${\frac {{\frac {\omega _{\mathrm {N} }}{Q}}s}{s^{2}+{\frac {\omega _{\mathrm {N} }}{Q}}s+\omega _{\mathrm {N} }^{2}}}$ |
| Notch (bandstop) | ${\frac {s^{2}+\omega _{\mathrm {N} }^{2}}{s^{2}+{\frac {\omega _{\mathrm {N} }}{Q}}s+\omega _{\mathrm {N} }^{2}}}$ |
| Highpass | ${\frac {s^{2}}{s^{2}+{\frac {\omega _{\mathrm {N} }}{Q}}s+\omega _{\mathrm {N} }^{2}}}$ |

## Electrical systems

For an electrically resonant system, the *Q* factor represents the effect of electrical resistance and, for electromechanical resonators such as quartz crystals, mechanical friction.

### Relationship between Q and bandwidth

The 2-sided bandwidth relative to a resonant frequency of *F*0 (Hz) is ${\frac {F_{0}}{Q}}$ .

For example, an antenna tuned to have a Q value of 10 and a centre frequency of 100 kHz would have a 3 dB bandwidth of 10 kHz.

In audio, bandwidth is often expressed in terms of octaves. Then the relationship between Q and bandwidth is

$Q={\frac {2^{\frac {BW}{2}}}{2^{BW}-1}}={\frac {1}{2\sinh \left({\frac {1}{2}}\ln(2)BW\right)}},$ where BW is the bandwidth in octaves.

### RLC circuits

In an ideal series RLC circuit, and in a tuned radio frequency receiver (TRF) the Q factor is:

$Q={\frac {1}{R}}{\sqrt {\frac {L}{C}}}={\frac {\omega _{0}L}{R}}={\frac {1}{\omega _{0}RC}}$

where R, L, and C are the resistance, inductance and capacitance of the tuned circuit, respectively. Larger series resistances correspond to lower circuit Q values.

For a parallel RLC circuit, the Q factor is the inverse of the series case:

$Q=R{\sqrt {\frac {C}{L}}}={\frac {R}{\omega _{0}L}}=\omega _{0}RC$

Consider a circuit where R, L, and C are all in parallel. The lower the parallel resistance is, the more effect it will have in damping the circuit and thus result in lower Q. This is useful in filter design to determine the bandwidth.

In a parallel LC circuit where the main loss is the resistance of the inductor, R, in series with the inductance, L, Q is as in the series circuit. This is a common circumstance for resonators, where limiting the resistance of the inductor to improve Q and narrow the bandwidth is the desired result.

### Individual reactive components

The Q of an individual reactive component depends on the frequency at which it is evaluated, which is typically the resonant frequency of the circuit that it is used in. The Q of an inductor with a series loss resistance is the Q of a resonant circuit using that inductor (including its series loss) and a perfect capacitor.

$Q_{L}={\frac {X_{L}}{R_{L}}}={\frac {\omega _{0}L}{R_{L}}}$

where:

- *ω*0 is the resonance frequency in radians per second;
- L is the inductance;
- XL is the inductive reactance; and
- RL is the series resistance of the inductor.

The Q of a capacitor with a series loss resistance is the same as the Q of a resonant circuit using that capacitor with a perfect inductor:

$Q_{C}={\frac {-X_{C}}{R_{C}}}={\frac {1}{\omega _{0}CR_{C}}}$

where:

- *ω*0 is the resonance frequency in radians per second;
- C is the capacitance;
- XC is the capacitive reactance; and
- RC is the series resistance of the capacitor.

In general, the Q of a resonator involving a series combination of a capacitor and an inductor can be determined from the Q values of the components, whether their losses come from series resistance or otherwise:

$Q={\frac {1}{{\frac {1}{Q_{L}}}+{\frac {1}{Q_{C}}}}}$

## Mechanical systems

For a single damped mass-spring system, the Q factor represents the effect of simplified viscous damping or drag, where the damping force or drag force is proportional to velocity. The formula for the Q factor is: $Q={\frac {\sqrt {Mk}}{D}},\,$ where M is the mass, k is the spring constant, and D is the damping coefficient, defined by the equation *F*damping = −*Dv*, where v is the velocity.

## Acoustical systems

The Q of a musical instrument is critical; an excessively high Q in a resonator will not evenly amplify the multiple frequencies an instrument produces. For this reason, string instruments often have bodies with complex shapes, so that they produce a wide range of frequencies fairly evenly.

The Q of a brass instrument or wind instrument needs to be high enough to pick one frequency out of the broader-spectrum buzzing of the lips or reed. By contrast, a vuvuzela is made of flexible plastic, and therefore has a very low Q for a brass instrument, giving it a muddy, breathy tone. Instruments made of stiffer plastic, brass, or wood have higher Q values. An excessively high Q can make it harder to hit a note. Q in an instrument may vary across frequencies, but this may not be desirable.

Helmholtz resonators have a very high Q, as they are designed for picking out a very narrow range of frequencies.

## Optical systems

In optics, the Q factor of a resonant cavity is given by $Q={\frac {2\pi f_{o}\,E}{P}},\,$ where fo is the resonant frequency, E is the stored energy in the cavity, and *P* = −⁠*dE*/*dt*⁠ is the power dissipated. The optical Q is equal to the ratio of the resonant frequency to the bandwidth of the cavity resonance. The average lifetime of a resonant photon in the cavity is proportional to the cavity's Q. If the Q factor of a laser's cavity is abruptly changed from a low value to a high one, the laser will emit a pulse of light that is much more intense than the laser's normal continuous output. This technique is known as Q-switching. Q factor is of particular importance in plasmonics, where loss is linked to the damping of the surface plasmon resonance. While loss is normally considered a hindrance in the development of plasmonic devices, it is possible to leverage this property to present new enhanced functionalities.

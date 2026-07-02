---
title: "Resonance"
source: https://en.wikipedia.org/wiki/Resonance
domain: acoustics-physics
license: CC-BY-SA-4.0
tags: acoustic wave, standing wave, doppler effect, sound resonance
fetched: 2026-07-02
---

# Resonance

**Resonance** is a phenomenon that occurs when an object or system is subjected to an external force or vibration whose frequency matches a **resonant frequency** (or **resonance frequency**) of the system, defined as a frequency that generates a maximum amplitude response in the system. When this happens, the object or system absorbs energy from the external force and starts vibrating with a larger amplitude. Resonance can occur in various systems, such as mechanical, electrical, or acoustic systems, and it is often desirable in certain applications, such as musical instruments or radio receivers. However, resonance can also be detrimental, leading to excessive vibrations or even structural failure in some cases.

All systems, including molecular systems and particles, tend to vibrate at a natural frequency depending upon their structure; when there is very little damping this frequency is approximately equal to, but slightly above, the resonant frequency. When an oscillating force, an external vibration, is applied at a resonant frequency of a dynamic system, object, or particle, the outside vibration will cause the system to oscillate at a higher amplitude (with more force) than when the same force is applied at other, non-resonant frequencies.

The resonant frequencies of a system can be identified when the response to an external vibration creates an amplitude that is a relative maximum within the system. Small periodic forces that are near a resonant frequency of the system have the ability to produce large amplitude oscillations in the system due to the storage of vibrational energy.

Resonance phenomena occur with all types of vibrations or waves: there is mechanical resonance, orbital resonance, acoustic resonance, electromagnetic resonance, nuclear magnetic resonance (NMR), electron spin resonance (ESR) and resonance of quantum wave functions. Resonant systems can be used to generate vibrations of a specific frequency (e.g., musical instruments), or pick out specific frequencies from a complex vibration containing many frequencies (e.g., filters).

The term *resonance* (from Latin *resonantia*, 'echo', from *resonare*, 'resound') originated from the field of acoustics discussed by Galileo Galilei in his book *Dialogues Concerning Two New Sciences*, particularly the sympathetic resonance observed in musical instruments, e.g., when one string starts to vibrate and produce sound after a different one is struck.

## Overview

Resonance occurs when a system is able to store and easily transfer energy between two or more different storage modes (such as kinetic energy and potential energy in the case of a simple pendulum). However, there are some losses from cycle to cycle, called damping. When damping is small, the resonant frequency is approximately equal to the natural frequency of the system, which is a frequency of unforced vibrations. Some systems have multiple and distinct resonant frequencies.

## Examples

A familiar example is a playground swing, which acts as a pendulum. Pushing a person in a swing in time with the natural interval of the swing (its resonant frequency) makes the swing go higher and higher (maximum amplitude), while attempts to push the swing at a faster or slower tempo produce smaller arcs. This is because the energy the swing absorbs is maximized when the pushes match the swing's natural oscillations.

Resonance occurs widely in nature, and is exploited in many devices. It is the mechanism by which virtually all sinusoidal waves and vibrations are generated. For example, when hard objects like metal, glass, or wood are struck, there are brief resonant vibrations in the object. Light and other short wavelength electromagnetic radiation is produced by resonance on an atomic scale, such as electrons in atoms. Other examples of resonance include:

- Timekeeping mechanisms of modern clocks and watches, e.g., the balance wheel in a mechanical watch and the quartz crystal in a quartz watch
- Tidal resonance of the Bay of Fundy
- Acoustic resonances of musical instruments and the human vocal tract
- Shattering of a crystal wineglass when exposed to a musical tone of the right pitch (its resonant frequency)
- Friction idiophones, such as making a glass object (glass, bottle, vase) vibrate by rubbing around its rim with a fingertip
- Electrical resonance of tuned circuits in radios and TVs that allow radio frequencies to be selectively received
- Creation of coherent light by optical resonance in a laser cavity
- Orbital resonance as exemplified by some moons of the Solar System's giant planets and resonant groups such as the plutinos
- Material resonances in atomic scale are the basis of several spectroscopic techniques that are used in condensed matter physics
  - Electron spin resonance
  - Mössbauer effect
  - Nuclear magnetic resonance

## Linear systems

Resonance manifests itself in many linear and nonlinear systems as oscillations around an equilibrium point. When the system is driven by a sinusoidal external input, a measured output of the system may oscillate in response. The ratio of the amplitude of the output's steady-state oscillations to the input's oscillations is called the gain, and the gain can be a function of the frequency of the sinusoidal external input. Peaks in the gain at certain frequencies correspond to resonances, where the amplitude of the measured output's oscillations are disproportionately large.

Since many linear and nonlinear systems that oscillate are modeled as harmonic oscillators near their equilibria, a derivation of the resonant frequency for a driven, damped harmonic oscillator is shown. An RLC circuit is used to illustrate connections between resonance and a system's transfer function, frequency response, poles, and zeroes. Building off the RLC circuit example, these connections for higher-order linear systems with multiple inputs and outputs are generalized.

### The driven, damped harmonic oscillator

Consider a damped mass on a spring driven by a sinusoidal, externally applied force. Newton's second law takes the form

| $m{\frac {\mathrm {d} ^{2}x}{\mathrm {d} t^{2}}}=F_{0}\sin(\omega t)-kx-c{\frac {\mathrm {d} x}{\mathrm {d} t}},$ |   | 1 |
|---|---|---|

where *m* is the mass, *x* is the displacement of the mass from the equilibrium point, *F*0 is the driving amplitude, *ω* is the driving angular frequency, *k* is the spring constant, and *c* is the viscous damping coefficient. This can be rewritten in the form

| ${\frac {\mathrm {d} ^{2}x}{\mathrm {d} t^{2}}}+2\zeta \omega _{0}{\frac {\mathrm {d} x}{\mathrm {d} t}}+\omega _{0}^{2}x={\frac {F_{0}}{m}}\sin(\omega t),$ |   | 2 |
|---|---|---|

where

- ${\textstyle \omega _{0}={\sqrt {k/m}}}$ is called the *undamped angular frequency of the oscillator* or the *natural frequency*,
- $\zeta ={\frac {c}{2{\sqrt {mk}}}}$ is called the *damping ratio*.

Many sources also refer to *ω*0 as the *resonant frequency*. However, as shown below, when analyzing oscillations of the displacement *x*(*t*), the resonant frequency is close to but not the same as *ω*0. In general the resonant frequency is close to but not necessarily the same as the natural frequency. The RLC circuit example in the next section gives examples of different resonant frequencies for the same system.

The general solution of Equation (**2**) is the sum of a transient solution that depends on initial conditions and a steady state solution that is independent of initial conditions and depends only on the driving amplitude *F*0, driving frequency *ω*, undamped angular frequency *ω*0, and the damping ratio *ζ*. The transient solution decays in a relatively short amount of time, so to study resonance it is sufficient to consider the steady state solution.

It is possible to write the steady-state solution for *x*(*t*) as a function proportional to the driving force with an induced phase change, *φ*.

| $x(t)={\frac {F_{0}}{m{\sqrt {\left(2\omega \omega _{0}\zeta \right)^{2}+(\omega _{0}^{2}-\omega ^{2})^{2}}}}}\sin(\omega t+\varphi ),$ |   | 3 |
|---|---|---|

where $\varphi =\arctan \left({\frac {2\omega \omega _{0}\zeta }{\omega ^{2}-\omega _{0}^{2}}}\right)+n\pi .$

The phase value is usually taken to be between −180° and 0 so it represents a phase lag for both positive and negative values of the arctan argument.

Resonance occurs when, at certain driving frequencies, the steady-state amplitude of *x*(*t*) is large compared to its amplitude at other driving frequencies. For the mass on a spring, resonance corresponds physically to the mass's oscillations having large displacements from the spring's equilibrium position at certain driving frequencies. Looking at the amplitude of *x*(*t*) as a function of the driving frequency *ω*, the amplitude is maximal at the driving frequency $\omega _{r}=\omega _{0}{\sqrt {1-2\zeta ^{2}}}.$

*ω**r* is the **resonant frequency** for this system. Again, the resonant frequency does not equal the undamped angular frequency *ω*0 of the oscillator. They are proportional, and if the damping ratio goes to zero they are the same, but for non-zero damping they are not the same frequency. As shown in the figure, resonance may also occur at other frequencies near the resonant frequency, including *ω*0, but the maximum response is at the resonant frequency.

Also, *ω**r* is only real and non-zero if ${\textstyle \zeta <1/{\sqrt {2}}}$ , so this system can only resonate when the harmonic oscillator is significantly underdamped. For systems with a very small damping ratio and a driving frequency near the resonant frequency, the steady state oscillations can become very large.

#### The pendulum

For other driven, damped harmonic oscillators whose equations of motion do not look exactly like the mass on a spring example, the resonant frequency remains $\omega _{r}=\omega _{0}{\sqrt {1-2\zeta ^{2}}},$ but the definitions of *ω*0 and *ζ* change based on the physics of the system. For a pendulum of length *ℓ* and small displacement angle *θ*, Equation (**1**) becomes $m\ell {\frac {\mathrm {d} ^{2}\theta }{\mathrm {d} t^{2}}}=F_{0}\sin(\omega t)-mg\theta -c\ell {\frac {\mathrm {d} \theta }{\mathrm {d} t}}$

and therefore

- $\omega _{0}={\sqrt {\frac {g}{\ell }}},$
- $\zeta ={\frac {c}{2m}}{\sqrt {\frac {\ell }{g}}}.$

### RLC series circuits

Consider a circuit consisting of a resistor with resistance *R*, an inductor with inductance *L*, and a capacitor with capacitance *C* connected in series with current *i*(*t*) and driven by a voltage source with voltage *v**in*(*t*). The voltage drop around the circuit is

| $L{\frac {di(t)}{dt}}+Ri(t)+V(0)+{\frac {1}{C}}\int _{0}^{t}i(\tau )d\tau =v_{\text{in}}(t).$ |   | 4 |
|---|---|---|

Rather than analyzing a candidate solution to this equation like in the mass on a spring example above, this section will analyze the frequency response of this circuit. Taking the Laplace transform of Equation (**4**), $sLI(s)+RI(s)+{\frac {1}{sC}}I(s)=V_{\text{in}}(s),$ where *I*(*s*) and *V**in*(*s*) are the Laplace transform of the current and input voltage, respectively, and *s* is a complex frequency parameter in the Laplace domain. Rearranging terms, $I(s)={\frac {s}{s^{2}L+Rs+{\frac {1}{C}}}}V_{\text{in}}(s).$

#### Voltage across the capacitor

An RLC circuit in series presents several options for where to measure an output voltage. Suppose the output voltage of interest is the voltage drop across the capacitor. As shown above, in the Laplace domain this voltage is $V_{\text{out}}(s)={\frac {1}{sC}}I(s)$ or $V_{\text{out}}={\frac {1}{LC(s^{2}+{\frac {R}{L}}s+{\frac {1}{LC}})}}V_{\text{in}}(s).$

Define for this circuit a natural frequency and a damping ratio, $\omega _{0}={\frac {1}{\sqrt {LC}}},$ $\zeta ={\frac {R}{2}}{\sqrt {\frac {C}{L}}}.$

The ratio of the output voltage to the input voltage becomes $H(s)\triangleq {\frac {V_{\text{out}}(s)}{V_{\text{in}}(s)}}={\frac {\omega _{0}^{2}}{s^{2}+2\zeta \omega _{0}s+\omega _{0}^{2}}}$

*H*(*s*) is the transfer function between the input voltage and the output voltage. This transfer function has two poles–roots of the polynomial in the transfer function's denominator–at

| $s=-\zeta \omega _{0}\pm i\omega _{0}{\sqrt {1-\zeta ^{2}}}$ |   | 5 |
|---|---|---|

and no zeros–roots of the polynomial in the transfer function's numerator. Moreover, for $\zeta \leq 1$ , the magnitude of these poles is the natural frequency *ω*0 and that for $\zeta <1/{\sqrt {2}}$ , our condition for resonance in the harmonic oscillator example, the poles are closer to the imaginary axis than to the real axis.

Evaluating *H*(*s*) along the imaginary axis *s* = *iω*, the transfer function describes the frequency response of this circuit. Equivalently, the frequency response can be analyzed by taking the Fourier transform of Equation (**4**) instead of the Laplace transform. The transfer function, which is also complex, can be written as a gain and phase, $H(i\omega )=G(\omega )e^{i\Phi (\omega )}.$

A sinusoidal input voltage at frequency *ω* results in an output voltage at the same frequency that has been scaled by *G*(*ω*) and has a phase shift *Φ*(*ω*). The gain and phase can be plotted versus frequency on a Bode plot. For the RLC circuit's capacitor voltage, the gain of the transfer function *H*(*iω*) is

| $G(\omega )={\frac {\omega _{0}^{2}}{\sqrt {\left(2\omega \omega _{0}\zeta \right)^{2}+(\omega _{0}^{2}-\omega ^{2})^{2}}}}.$ |   | 6 |
|---|---|---|

Note the similarity between the gain here and the amplitude in Equation (**3**). Once again, the gain is maximized at the **resonant frequency** $\omega _{r}=\omega _{0}{\sqrt {1-2\zeta ^{2}}}.$

Here, the resonance corresponds physically to having a relatively large amplitude for the steady state oscillations of the voltage across the capacitor compared to its amplitude at other driving frequencies.

#### Voltage across the inductor

The resonant frequency need not always take the form given in the examples above. For the RLC circuit, suppose instead that the output voltage of interest is the voltage across the inductor. As shown above, in the Laplace domain the voltage across the inductor is $V_{\text{out}}(s)=sLI(s),$ $V_{\text{out}}(s)={\frac {s^{2}}{s^{2}+{\frac {R}{L}}s+{\frac {1}{LC}}}}V_{\text{in}}(s),$ $V_{\text{out}}(s)={\frac {s^{2}}{s^{2}+2\zeta \omega _{0}s+\omega _{0}^{2}}}V_{\text{in}}(s),$

using the same definitions for *ω*0 and *ζ* as in the previous example. The transfer function between *V*in(*s*) and this new *V*out(*s*) across the inductor is $H(s)={\frac {s^{2}}{s^{2}+2\zeta \omega _{0}s+\omega _{0}^{2}}}.$

This transfer function has the same poles as the transfer function in the previous example, but it also has two zeroes in the numerator at *s* = 0. Evaluating *H*(*s*) along the imaginary axis, its gain becomes $G(\omega )={\frac {\omega ^{2}}{\sqrt {\left(2\omega \omega _{0}\zeta \right)^{2}+(\omega _{0}^{2}-\omega ^{2})^{2}}}}.$

Compared to the gain in Equation (**6**) using the capacitor voltage as the output, this gain has a factor of *ω*2 in the numerator and will therefore have a different resonant frequency that maximizes the gain. That frequency is $\omega _{r}={\frac {\omega _{0}}{\sqrt {1-2\zeta ^{2}}}},$

So for the same RLC circuit but with the voltage across the inductor as the output, the resonant frequency is now *larger* than the natural frequency, though it still tends towards the natural frequency as the damping ratio goes to zero. That the same circuit can have different resonant frequencies for different choices of output is not contradictory. As shown in Equation (**4**), the voltage drop across the circuit is divided among the three circuit elements, and each element has different dynamics. The capacitor's voltage grows slowly by integrating the current over time and is therefore more sensitive to lower frequencies, whereas the inductor's voltage grows when the current changes rapidly and is therefore more sensitive to higher frequencies. While the circuit as a whole has a natural frequency where it tends to oscillate, the different dynamics of each circuit element make each element resonate at a slightly different frequency.

#### Voltage across the resistor

Suppose that the output voltage of interest is the voltage across the resistor. In the Laplace domain the voltage across the resistor is $V_{\text{out}}(s)=RI(s),$ $V_{\text{out}}(s)={\frac {Rs}{L\left(s^{2}+{\frac {R}{L}}s+{\frac {1}{LC}}\right)}}V_{\text{in}}(s),$

and using the same natural frequency and damping ratio as in the capacitor example the transfer function is $H(s)={\frac {2\zeta \omega _{0}s}{s^{2}+2\zeta \omega _{0}s+\omega _{0}^{2}}}.$

This transfer function also has the same poles as the previous RLC circuit examples, but it only has one zero in the numerator at *s* = 0. For this transfer function, its gain is $G(\omega )={\frac {2\zeta \omega _{0}\omega }{\sqrt {\left(2\omega \omega _{0}\zeta \right)^{2}+(\omega _{0}^{2}-\omega ^{2})^{2}}}}.$

The resonant frequency that maximizes this gain is $\omega _{r}=\omega _{0},$ and the gain is one at this frequency, so the voltage across the resistor resonates *at* the circuit's natural frequency and at this frequency the amplitude of the voltage across the resistor equals the input voltage's amplitude.

#### Antiresonance

Some systems exhibit antiresonance that can be analyzed in the same way as resonance. For antiresonance, the amplitude of the response of the system at certain frequencies is disproportionately *small* rather than being disproportionately large. In the RLC circuit example, this phenomenon can be observed by analyzing both the inductor and the capacitor combined.

Suppose that the output voltage of interest in the RLC circuit is the voltage across the inductor *and* the capacitor combined in series. Equation (**4**) showed that the sum of the voltages across the three circuit elements sums to the input voltage, so measuring the output voltage as the sum of the inductor and capacitor voltages combined is the same as *v**in* minus the voltage drop across the resistor. The previous example showed that at the natural frequency of the system, the amplitude of the voltage drop across the resistor *equals* the amplitude of *v**in*, and therefore the voltage across the inductor and capacitor combined has zero amplitude. We can show this with the transfer function.

The sum of the inductor and capacitor voltages is $V_{\text{out}}(s)=(sL+{\frac {1}{sC}})I(s),$ $V_{\text{out}}(s)={\frac {s^{2}+{\frac {1}{LC}}}{s^{2}+{\frac {R}{L}}s+{\frac {1}{LC}}}}V_{\text{in}}(s).$

Using the same natural frequency and damping ratios as the previous examples, the transfer function is $H(s)={\frac {s^{2}+\omega _{0}^{2}}{s^{2}+2\zeta \omega _{0}s+\omega _{0}^{2}}}.$

This transfer has the same poles as the previous examples but has zeroes at

| $s=\pm i\omega _{0}.$ |   | 7 |
|---|---|---|

Evaluating the transfer function along the imaginary axis, its gain is $G(\omega )={\frac {\omega _{0}^{2}-\omega ^{2}}{\sqrt {\left(2\omega \omega _{0}\zeta \right)^{2}+(\omega _{0}^{2}-\omega ^{2})^{2}}}}.$

Rather than look for resonance, i.e., peaks of the gain, notice that the gain goes to zero at *ω* = *ω*0, which complements our analysis of the resistor's voltage. This is called **antiresonance**, which has the opposite effect of resonance. Rather than result in outputs that are disproportionately large at this frequency, this circuit with this choice of output has no response at all at this frequency. The frequency that is filtered out corresponds exactly to the zeroes of the transfer function, which were shown in Equation (**7**) and were on the imaginary axis.

#### Relationships between resonance and frequency response in the RLC series circuit example

These RLC circuit examples illustrate how resonance is related to the frequency response of the system. Specifically, these examples illustrate:

- How resonant frequencies can be found by looking for peaks in the gain of the transfer function between the input and output of the system, for example in a Bode magnitude plot
- How the resonant frequency for a single system can be different for different choices of system output
- The connection between the system's natural frequency, the system's damping ratio, and the system's resonant frequency
- The connection between the system's natural frequency and the magnitude of the transfer function's poles, pointed out in Equation (**5**), and therefore a connection between the poles and the resonant frequency
- A connection between the transfer function's zeroes and the shape of the gain as a function of frequency, and therefore a connection between the zeroes and the resonant frequency that maximizes gain
- A connection between the transfer function's zeroes and antiresonance

The next section extends these concepts to resonance in a general linear system.

### Generalizing resonance and antiresonance for linear systems

Next consider an arbitrary linear system with multiple inputs and outputs. For example, in state-space representation a third order linear time-invariant system with three inputs and two outputs might be written as ${\begin{bmatrix}{\dot {x}}_{1}\\{\dot {x}}_{2}\\{\dot {x}}_{3}\end{bmatrix}}=A{\begin{bmatrix}x_{1}(t)\\x_{2}(t)\\x_{3}(t)\end{bmatrix}}+B{\begin{bmatrix}u_{1}(t)\\u_{2}(t)\\u_{3}(t)\end{bmatrix}},$ ${\begin{bmatrix}y_{1}(t)\\y_{2}(t)\end{bmatrix}}=C{\begin{bmatrix}x_{1}(t)\\x_{2}(t)\\x_{3}(t)\end{bmatrix}}+D{\begin{bmatrix}u_{1}(t)\\u_{2}(t)\\u_{3}(t)\end{bmatrix}},$ where *u**i*(*t*) are the inputs, *x**i*(t) are the state variables, *y**i*(*t*) are the outputs, and *A*, *B*, *C*, and *D* are matrices describing the dynamics between the variables.

This system has a transfer function matrix whose elements are the transfer functions between the various inputs and outputs. For example, ${\begin{bmatrix}Y_{1}(s)\\Y_{2}(s)\end{bmatrix}}={\begin{bmatrix}H_{11}(s)&H_{12}(s)&H_{13}(s)\\H_{21}(s)&H_{22}(s)&H_{23}(s)\end{bmatrix}}{\begin{bmatrix}U_{1}(s)\\U_{2}(s)\\U_{3}(s)\end{bmatrix}}.$

Each *H**ij*(*s*) is a scalar transfer function linking one of the inputs to one of the outputs. The RLC circuit examples above had one input voltage and showed four possible output voltages–across the capacitor, across the inductor, across the resistor, and across the capacitor and inductor combined in series–each with its own transfer function. If the RLC circuit were set up to measure all four of these output voltages, that system would have a 4×1 transfer function matrix linking the single input to each of the four outputs.

Evaluated along the imaginary axis, each *H**ij*(*iω*) can be written as a gain and phase shift, $H_{ij}(i\omega )=G_{ij}(\omega )e^{i\Phi _{ij}(\omega )}.$

Peaks in the gain at certain frequencies correspond to resonances between that transfer function's input and output, assuming the system is stable.

Each transfer function *H**ij*(*s*) can also be written as a fraction whose numerator and denominator are polynomials of *s*. $H_{ij}(s)={\frac {N_{ij}(s)}{D_{ij}(s)}}.$

The complex roots of the numerator are called zeroes, and the complex roots of the denominator are called poles. For a stable system, the positions of these poles and zeroes on the complex plane give some indication of whether the system can resonate or antiresonate and at which frequencies. In particular, any stable or marginally stable, complex conjugate pair of poles with imaginary components can be written in terms of a natural frequency and a damping ratio as $s=-\zeta \omega _{0}\pm i\omega _{0}{\sqrt {1-\zeta ^{2}}},$ as in Equation (**5**). The natural frequency *ω*0 of that pole is the magnitude of the position of the pole on the complex plane and the damping ratio of that pole determines how quickly that oscillation decays. In general,

- Complex conjugate pairs of *poles* near the imaginary axis correspond to a peak or resonance in the frequency response in the vicinity of the pole's natural frequency. If the pair of poles is *on* the imaginary axis, the gain is infinite at that frequency.
- Complex conjugate pairs of *zeroes* near the imaginary axis correspond to a notch or antiresonance in the frequency response in the vicinity of the zero's frequency, i.e., the frequency equal to the magnitude of the zero. If the pair of zeroes is *on* the imaginary axis, the gain is zero at that frequency.

In the RLC circuit example, the first generalization relating poles to resonance is observed in Equation (**5**). The second generalization relating zeroes to antiresonance is observed in Equation (**7**). In the examples of the harmonic oscillator, the RLC circuit capacitor voltage, and the RLC circuit inductor voltage, "poles near the imaginary axis" corresponds to the significantly underdamped condition ζ < 1/ ${\sqrt {2}}$ .

## Standing waves

A physical system can have as many natural frequencies as it has degrees of freedom and can resonate near each of those natural frequencies. A mass on a spring, which has one degree of freedom, has one natural frequency. A double pendulum, which has two degrees of freedom, can have two natural frequencies. As the number of coupled harmonic oscillators increases, the time it takes to transfer energy from one to the next becomes significant. Systems with very large numbers of degrees of freedom can be thought of as continuous rather than as having discrete oscillators.

Energy transfers from one oscillator to the next in the form of waves. For example, the string of a guitar or the surface of water in a bowl can be modeled as a continuum of small coupled oscillators and waves can travel along them. In many cases these systems have the potential to resonate at certain frequencies, forming standing waves with large-amplitude oscillations at fixed positions. Resonance in the form of standing waves underlies many familiar phenomena, such as the sound produced by musical instruments, electromagnetic cavities used in lasers and microwave ovens, and energy levels of atoms.

### Standing waves on a string

When a string of fixed length is driven at a particular frequency, a wave propagates along the string at the same frequency. The waves reflect off the ends of the string, and eventually a steady state is reached with waves traveling in both directions. The waveform is the superposition of the waves.

At certain frequencies, the steady state waveform does not appear to travel along the string. At fixed positions called nodes, the string is never displaced. Between the nodes the string oscillates and exactly halfway between the nodes, at positions called anti-nodes, where the oscillations have their largest amplitude.

For a string of length L with fixed ends, the displacement $y(x,t)$ of the string perpendicular to the x -axis at time t is $y(x,t)=2y_{\text{max}}\sin(kx)\cos(2\pi ft),$

where

- $y_{\text{max}}$ is the amplitude of the left- and right-traveling waves interfering to form the standing wave,
- k is the wave number,
- f is the frequency.

The frequencies that resonate and form standing waves relate to the length of the string as $f={\frac {nv}{2L}},$ $n=1,2,3,\dots$

where v is the speed of the wave and the integer n denotes different modes or harmonics. The standing wave with *n* = 1 oscillates at the fundamental frequency and has a wavelength that is twice the length of the string. The possible modes of oscillation form a harmonic series.

## Types

### Mechanical

Mechanical resonance is the tendency of a mechanical system to absorb more energy when the frequency of its oscillations matches the system's natural frequency of vibration than it does at other frequencies. It may cause violent swaying motions and even catastrophic failure in improperly constructed structures including bridges, buildings, trains, and aircraft. When designing objects, engineers must ensure the mechanical resonance frequencies of the component parts do not match driving vibrational frequencies of motors or other oscillating parts, a phenomenon known as resonance disaster.

Avoiding resonance disasters is a major concern in every building, tower, and bridge construction project. As a countermeasure, shock mounts can be installed to absorb resonant frequencies and thus dissipate the absorbed energy. The Taipei 101 building relies on a 660-tonne pendulum (730-short-ton)—a tuned mass damper—to cancel resonance. Furthermore, the structure is designed to resonate at a frequency that does not typically occur. Buildings in seismic zones are often constructed to take into account the oscillating frequencies of expected ground motion. In addition, engineers designing objects having engines must ensure that the mechanical resonant frequencies of the component parts do not match driving vibrational frequencies of the motors or other strongly oscillating parts.

Clocks keep time by mechanical resonance in a balance wheel, pendulum, or quartz crystal.

The cadence of runners has been hypothesized to be energetically favorable due to resonance between the elastic energy stored in the lower limb and the mass of the runner.

### Acoustic

Acoustic resonance is a branch of mechanical resonance that is concerned with the mechanical vibrations across the frequency range of human hearing, in other words sound. For humans, hearing is normally limited to frequencies between about 20 Hz and 20,000 Hz (20 kHz), Many objects and materials act as resonators with resonant frequencies within this range, and when struck vibrate mechanically, pushing on the surrounding air to create sound waves. This is the source of many percussive sounds we hear.

Acoustic resonance is an important consideration for instrument builders, as most acoustic instruments use resonators, such as the strings and body of a violin, the length of tube in a flute, and the shape of, and tension on, a drum membrane.

Like mechanical resonance, acoustic resonance can result in catastrophic failure of the object at resonance. The classic example of this is breaking a wine glass with sound at the precise resonant frequency of the glass, although this is difficult in practice.

### Electrical

Electrical resonance occurs in an electric circuit at a particular *resonant frequency* when the impedance of the circuit is at a minimum in a series circuit or at maximum in a parallel circuit (usually when the transfer function peaks in absolute value). Resonance in circuits are used for both transmitting and receiving wireless communications such as television, cell phones and radio.

### Optical

An optical cavity, also called an *optical resonator*, is an arrangement of mirrors that forms a standing wave cavity resonator for light waves. Optical cavities are a major component of lasers, surrounding the gain medium and providing feedback of the laser light. They are also used in optical parametric oscillators and some interferometers. Light confined in the cavity reflects multiple times producing standing waves for certain resonant frequencies. The standing wave patterns produced are called "modes". Longitudinal modes differ only in frequency while transverse modes differ for different frequencies and have different intensity patterns across the cross-section of the beam. Ring resonators and whispering galleries are examples of optical resonators that do not form standing waves.

Different resonator types are distinguished by the focal lengths of the two mirrors and the distance between them; flat mirrors are not often used because of the difficulty of aligning them precisely. The geometry (resonator type) must be chosen so the beam remains stable, i.e., the beam size does not continue to grow with each reflection. Resonator types are also designed to meet other criteria such as minimum beam waist or having no focal point (and therefore intense light at that point) inside the cavity.

Optical cavities are designed to have a very large *Q* factor. A beam reflects a large number of times with little attenuation—therefore the frequency line width of the beam is small compared to the frequency of the laser.

Additional optical resonances are guided-mode resonances and surface plasmon resonance, which result in anomalous reflection and high evanescent fields at resonance. In this case, the resonant modes are guided modes of a waveguide or surface plasmon modes of a dielectric-metallic interface. These modes are usually excited by a subwavelength grating.

### Orbital

In celestial mechanics, an orbital resonance occurs when two orbiting bodies exert a regular, periodic gravitational influence on each other, usually due to their orbital periods being related by a ratio of two small integers. Orbital resonances greatly enhance the mutual gravitational influence of the bodies. In most cases, this results in an *unstable* interaction, in which the bodies exchange momentum and shift orbits until the resonance no longer exists. Under some circumstances, a resonant system can be stable and self-correcting, so that the bodies remain in resonance. Examples are the 1:2:4 resonance of Jupiter's moons Ganymede, Europa, and Io, and the 2:3 resonance between Pluto and Neptune. Unstable resonances with Saturn's inner moons give rise to gaps in the rings of Saturn. The special case of 1:1 resonance (between bodies with similar orbital radii) causes large Solar System bodies to clear the neighborhood around their orbits by ejecting nearly everything else around them; this effect is used in the current definition of a planet.

### Atomic, particle, and molecular

Nuclear magnetic resonance (NMR) is the name given to a physical resonance phenomenon involving the observation of specific quantum mechanical magnetic properties of an atomic nucleus in the presence of an applied, external magnetic field. Many scientific techniques exploit NMR phenomena to study molecular physics, crystals, and non-crystalline materials through NMR spectroscopy. NMR is also routinely used in advanced medical imaging techniques, such as in magnetic resonance imaging (MRI).

All nuclei containing odd numbers of nucleons have an intrinsic angular momentum and magnetic moment. A key feature of NMR is that the resonant frequency of a particular substance is directly proportional to the strength of the applied magnetic field. It is this feature that is exploited in imaging techniques; if a sample is placed in a non-uniform magnetic field then the resonant frequencies of the sample's nuclei depend on where in the field they are located. Therefore, the particle can be located quite precisely by its resonant frequency.

Electron paramagnetic resonance, otherwise known as *electron spin resonance* (ESR), is a spectroscopic technique similar to NMR, but uses unpaired electrons instead. Materials for which this can be applied are much more limited since the material needs to both have an unpaired spin and be paramagnetic.

The Mössbauer effect is the resonant and recoil-free emission and absorption of gamma ray photons by atoms bound in a solid form.

Resonance in particle physics appears in similar circumstances to classical physics at the level of quantum mechanics and quantum field theory. Resonances can also be thought of as unstable particles, with the formula in the Universal resonance curve section of this article applying if *Γ* is the particle's decay rate and $\omega _{0}$ is the particle's mass *M*. In that case, the formula comes from the particle's propagator, with its mass replaced by the complex number *M* + *iΓ*. The formula is further related to the particle's decay rate by the optical theorem.

## Disadvantages

A column of soldiers marching in regular step on a narrow and structurally flexible bridge can set it into dangerously large amplitude oscillations. On April 12, 1831, the Broughton Suspension Bridge near Salford, England collapsed while a group of British soldiers were marching across. Since then, the British Army has had a standing order for soldiers to break stride when marching across bridges, to avoid resonance from their regular marching pattern affecting the bridge.

Vibrations of a motor or engine can induce resonant vibration in its supporting structures if their natural frequency is close to that of the vibrations of the engine. A common example is the rattling sound of a bus body when the engine is left idling.

Structural resonance of a suspension bridge induced by winds can lead to its catastrophic collapse. Several early suspension bridges in Europe and United States were destroyed by structural resonance induced by modest winds. The collapse of the Tacoma Narrows Bridge on 7 November 1940 is characterized in physics as a classic example of resonance. It has been argued by Robert H. Scanlan and others that the destruction was instead caused by aeroelastic flutter, a complicated interaction between the bridge and the winds passing through it—an example of a self oscillation, or a kind of "self-sustaining vibration" as referred to in the nonlinear theory of vibrations.

## Q factor

The *Q* factor or *quality factor* is a dimensionless parameter that describes how under-damped an oscillator or resonator is, and characterizes the bandwidth of a resonator relative to its center frequency. A high value for *Q* indicates a lower rate of energy loss relative to the stored energy, i.e., the system is lightly damped. The parameter is defined by the equation: $Q=2\pi {\text{ }}{\frac {\text{ maximum energy stored}}{\text{total energy lost per cycle at resonance}}}$ .

The higher the Q factor, the greater the amplitude at the resonant frequency, and the smaller the *bandwidth*, or range of frequencies around resonance occurs. In electrical resonance, a high-*Q* circuit in a radio receiver is more difficult to tune, but has greater selectivity, and so would be better at filtering out signals from other stations. High Q oscillators are more stable.

Examples that normally have a low Q factor include door closers (Q=0.5). Systems with high Q factors include tuning forks (Q=1000), atomic clocks and lasers (Q≈1011).

## Universal resonance curve

The exact response of a resonance, especially for frequencies far from the resonant frequency, depends on the details of the physical system, and is usually not exactly symmetric about the resonant frequency, as illustrated for the simple harmonic oscillator above.

For a lightly damped linear oscillator with a resonance frequency $\omega _{0}$ , the *intensity* of oscillations I when the system is driven with a driving frequency *$\omega$* is typically approximated by the following formula that is symmetric about the resonance frequency: $I(\omega )\equiv |\chi |^{2}\propto {\frac {1}{(\omega -\omega _{0})^{2}+\left({\frac {\Gamma }{2}}\right)^{2}}}.$

Where the susceptibility $\chi (\omega )$ links the amplitude of the oscillator to the driving force in frequency space: $x(\omega )=\chi (\omega )F(\omega )$

The intensity is defined as the square of the amplitude of the oscillations. This is a Lorentzian function, or Cauchy distribution, and this response is found in many physical situations involving resonant systems. Γ is a parameter dependent on the damping of the oscillator, and is known as the *linewidth* of the resonance. Heavily damped oscillators tend to have broad linewidths, and respond to a wider range of driving frequencies around the resonant frequency. The linewidth is inversely proportional to the *Q* factor, which is a measure of the sharpness of the resonance.

In radio engineering and electronics engineering, this approximate symmetric response is known as the *universal resonance curve*, a concept introduced by Frederick E. Terman in 1932 to simplify the approximate analysis of radio circuits with a range of center frequencies and *Q* values.

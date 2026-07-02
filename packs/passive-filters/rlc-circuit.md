---
title: "RLC circuit"
source: https://en.wikipedia.org/wiki/RLC_circuit
domain: passive-filters
license: CC-BY-SA-4.0
tags: passive filter, constant k filter, m-derived filter, resonant circuit
fetched: 2026-07-02
---

# RLC circuit

An **RLC circuit** is an electrical circuit consisting of a resistor (R), an inductor (L), and a capacitor (C), connected in series or in parallel. The name of the circuit is derived from the letters that are used to denote the constituent components of this circuit, where the sequence of the components may vary from RLC.

The circuit forms a harmonic oscillator for current, and resonates in a manner similar to an LC circuit. Introducing the resistor increases the decay of these oscillations, which is also known as damping. The resistor also reduces the peak resonant frequency. Some resistance is unavoidable even if a resistor is not specifically included as a component.

RLC circuits have many applications as oscillator circuits. Radio receivers and television sets use them for tuning to select a narrow frequency range from ambient radio waves. In this role, the circuit is often referred to as a tuned circuit. An RLC circuit can be used as a band-pass filter, band-stop filter, low-pass filter or high-pass filter. The tuning application, for instance, is an example of band-pass filtering. The RLC filter is described as a *second-order* circuit, meaning that any voltage or current in the circuit can be described by a second-order differential equation in circuit analysis.

The three circuit elements, R, L and C, can be combined in a number of different topologies. All three elements in series or all three elements in parallel are the simplest in concept and the most straightforward to analyse. There are, however, other arrangements, some with practical importance in real circuits. One issue often encountered is the need to take into account inductor resistance. Inductors are typically constructed from coils of wire, the resistance of which is not usually desirable, but it often has a significant effect on the circuit.

## Basic concepts

### Resonance

An important property of this circuit is its ability to resonate at a specific frequency, the resonance frequency, *f*0. Frequencies are measured in units of hertz. In this article, angular frequency, *ω*0, is used because it is more mathematically convenient. This is measured in radians per second. They are related to each other by a simple proportion,

$\omega _{0}=2\pi f_{0}\,.$

Resonance occurs because energy for this situation is stored in two different ways: in an electric field as the capacitor is charged and in a magnetic field as current flows through the inductor. Energy can be transferred from one to the other within the circuit and this can be oscillatory. A mechanical analogy is a weight suspended on a spring which will oscillate up and down when released. This is no passing metaphor; a weight on a spring is described by exactly the same second order differential equation as an RLC circuit and for all the properties of the one system there will be found an analogous property of the other. The mechanical property answering to the resistor in the circuit is friction in the spring–weight system. Friction will slowly bring any oscillation to a halt if there is no external force driving it. Likewise, the resistance in an RLC circuit will "damp" the oscillation, diminishing it with time if there is no driving AC power source in the circuit.

The resonant frequency is defined as the frequency at which the impedance of the circuit is at a minimum. Equivalently, it can be defined as the frequency at which the impedance is purely real (that is, purely resistive). This occurs because the impedances of the inductor and capacitor at resonant frequency are equal but of opposite sign and cancel out. Circuits where L and C are in parallel rather than series actually have a maximum impedance rather than a minimum impedance. For this reason they are often described as antiresonators; it is still usual, however, to name the frequency at which this occurs as the resonant frequency.

### Natural frequency

The resonance frequency is defined in terms of the impedance presented to a driving source. It is still possible for the circuit to carry on oscillating (for a time) after the driving source has been removed or it is subjected to a step in voltage (including a step down to zero). This is similar to the way that a tuning fork will carry on ringing after it has been struck, and the effect is often called ringing. This effect is the peak natural resonance frequency of the circuit and in general is not exactly the same as the driven resonance frequency, although the two will usually be quite close to each other. Various terms are used by different authors to distinguish the two, but resonance frequency unqualified usually means the driven resonance frequency. The driven frequency may be called the undamped resonance frequency or undamped natural frequency and the peak frequency may be called the damped resonance frequency or the damped natural frequency. The reason for this terminology is that the driven resonance frequency in a series or parallel resonant circuit has the value.

$\omega _{0}={\frac {1}{\sqrt {L\,C~}}}\,~.$

This is exactly the same as the resonance frequency of a lossless LC circuit – that is, one with no resistor present. The resonant frequency for a *driven* RLC circuit is the same as a circuit in which there is no damping, hence undamped resonant frequency. The resonant frequency peak amplitude, on the other hand, does depend on the value of the resistor and is described as the damped resonant frequency. A *highly damped* circuit will fail to resonate at all, when not driven. A circuit with a value of resistor that causes it to be just on the edge of ringing is called critically damped. Either side of critically damped are described as underdamped (ringing happens) and overdamped (ringing is suppressed).

Circuits with topologies more complex than straightforward series or parallel (some examples described later in the article) have a driven resonance frequency that deviates from $\ \omega _{0}=1/{\sqrt {L\,C~}}\$ , and for those the undamped resonance frequency, damped resonance frequency and driven resonance frequency can all be different.

### Damping

Damping is caused by the resistance in the circuit. It determines whether or not the circuit will resonate naturally (that is, without a driving source). Circuits that will resonate in this way are described as underdamped and those that will not are overdamped. Damping attenuation (symbol α) is measured in nepers per second. However, the unitless damping factor (symbol ζ, zeta) is often a more useful measure, which is related to α by

$\ \zeta ={\frac {\alpha }{\ \omega _{0}\ }}\ .$

The special case of *ζ* = 1 is called *critical damping* and represents the case of a circuit that is just on the border of oscillation. It is the minimum damping that can be applied without causing oscillation.

### Bandwidth

The resonance effect can be used for filtering, the rapid change in impedance near resonance can be used to pass or block signals close to the resonance frequency. Both band-pass and band-stop filters can be constructed and some filter circuits are shown later in the article. A key parameter in filter design is bandwidth. The bandwidth is measured between the cutoff frequencies, most frequently defined as the frequencies at which the power passed through the circuit has fallen to half the value passed at resonance. There are two of these half-power frequencies, one above, and one below the resonance frequency

$\Delta \omega =\omega _{2}-\omega _{1}\,,$

where Δ*ω* is the bandwidth, *ω*1 is the lower half-power frequency and *ω*2 is the upper half-power frequency. The bandwidth is related to attenuation by

$\Delta \omega =2\alpha \,,$

where the units are radians per second and nepers per second respectively. Other units may require a conversion factor. A more general measure of bandwidth is the fractional bandwidth, which expresses the bandwidth as a fraction of the resonance frequency and is given by

$B_{\mathrm {f} }={\frac {\Delta \omega }{\omega _{0}}}\,.$

The fractional bandwidth is also often stated as a percentage. The damping of filter circuits is adjusted to result in the required bandwidth. A narrow band filter, such as a notch filter, requires low damping. A wide band filter requires high damping.

### Q factor

The Q factor is a widespread measure used to characterise resonators. It is defined as the peak energy stored in the circuit divided by the average energy dissipated in it per radian at resonance. Low-Q circuits are therefore damped and lossy and high-Q circuits are underdamped and prone to amplitude extremes if driven at the resonant frequency. Q is related to bandwidth; low-Q circuits are wide-band and high-Q circuits are narrow-band. In fact, it happens that Q is the inverse of fractional bandwidth

$Q={\frac {1}{\,B_{\mathrm {f} }\,}}={\frac {\omega _{\text{o}}}{\,\operatorname {\Delta } \omega \,}}\;.$

Q factor is directly proportional to selectivity, as the Q factor depends inversely on bandwidth.

For a series resonant circuit (as shown below), the Q factor can be calculated as follows:

$Q={\frac {X}{\,R\;}}={\frac {1}{\,\omega _{\text{o}}R\,C\,}}={\frac {\,\omega _{\text{o}}L\,}{R}}={\frac {1}{\,R\;}}{\sqrt {{\frac {L}{\,C\,}}\,}}={\frac {\,Z_{\text{o}}\,}{R\;}}\;,$

where $\,X\,$ is the reactance *either* of $\,L\,$ or of $\,C\,$ at resonance, and $\,Z_{\text{o}}\equiv {\sqrt {{\frac {L}{\,C\,}}\,}}\;.$

### Scaled parameters

The parameters ζ, *B*f, and Q are all scaled to *ω*0. This means that circuits which have similar parameters share similar characteristics regardless of whether or not they are operating in the same frequency band.

The article next gives the analysis for the series RLC circuit in detail. Other configurations are not described in such detail, but the key differences from the series case are given. The general form of the differential equations given in the series circuit section are applicable to all second order circuits and can be used to describe the voltage or current in any element of each circuit.

## Series circuit

In this circuit, the three components are all in series with the voltage source. The governing differential equation can be found by substituting into Kirchhoff's voltage law (KVL) the constitutive equation for each of the three elements. From KVL,

$V_{\mathrm {R} }(t)+V_{\mathrm {L} }(t)+V_{\mathrm {C} }(t)=V(t)\,,$

where VR, *V*L and *V*C are the voltages across R, L, and C, respectively, and *V*(*t*) is the voltage from the source. All are a function of time *t*, since they may be time-varying.

Substituting $V_{R}(t)=R\ I(t)\,,$ $\,V_{\mathrm {L} }(t)=L{\frac {\mathrm {d} I(t)}{\mathrm {d} t}}\,$ and $\,V_{\mathrm {C} }(t)=V_{\mathrm {C} }(0)+{\frac {1}{\,C\,}}\int _{0}^{t}I(\tau )\,\mathrm {d} \tau \,$ into the equation above yields:

$RI(t)+L{\frac {\,\mathrm {d} I(t)\,}{\mathrm {d} t}}+V_{\mathrm {C} }(0)+{\frac {1}{\,C\,}}\int _{0}^{t}I(\tau )\,\mathrm {d} \tau =V(t)\;.$

For the case where the source is an unchanging voltage, taking the time derivative and dividing by L (and reordering the first two terms and eliminating the 0 from taking the derivative of the constant 3rd term) leads to the following second order differential equation:

${\frac {\mathrm {d} ^{2}}{\mathrm {d} t^{2}}}I(t)+{\frac {R}{\,L\,}}{\frac {\mathrm {d} }{\mathrm {d} t}}I(t)+{\frac {1}{\,L\,C\,}}I(t)=0\;.$

This can usefully be expressed in a more generally applicable form:

${\frac {\mathrm {d} ^{2}}{\mathrm {d} t^{2}}}I(t)+2\alpha {\frac {\mathrm {d} }{\mathrm {d} t}}I(t)+\omega _{0}^{2}I(t)=0\;.$

α and *ω*0 are both in units of angular frequency. α is called the *neper frequency*, or *attenuation*, and is a measure of how fast the transient response of the circuit will die away after the stimulus has been removed. Neper occurs in the name because the units can also be considered to be nepers per second, neper being a logarithmic unit of attenuation. *ω*0 is the angular resonance frequency.

For the case of the series RLC circuit these two parameters are given by:

${\begin{aligned}\alpha &={\frac {R}{\,2L\,}}\\\omega _{0}&={\frac {1}{\,{\sqrt {L\,C\,}}\,}}\;.\end{aligned}}$

A useful parameter is the *damping factor*, ζ, which is defined as the ratio of these two; although, sometimes ζ is not used, and α is referred to as *damping factor* instead; hence requiring careful specification of one's use of that term.

$\zeta \equiv {\frac {\alpha }{\,\omega _{0}\,}}\;.$

In the case of the series RLC circuit, the damping factor is given by

$\zeta ={\frac {\,R\,}{2}}{\sqrt {{\frac {C}{\,L\,}}\,}}={\frac {1}{\ 2Q\ }}~.$

The value of the damping factor determines the type of transient that the circuit will exhibit.

### Transient response

The differential equation has the characteristic equation,

$s^{2}+2\alpha s+\omega _{0}^{2}=0\,.$

The roots of the equation in s-domain are,

${\begin{aligned}s_{1}&=-\alpha +{\sqrt {\alpha ^{2}-\omega _{0}^{2}\,}}=-\omega _{0}\left(\zeta -{\sqrt {\zeta ^{2}-1\,}}\right)={\frac {-\omega _{0}}{\ \zeta +{\sqrt {\zeta ^{2}-1\ }}\ }}\ ,\\s_{2}&=-\alpha -{\sqrt {\alpha ^{2}-\omega _{0}^{2}\,}}=-\omega _{0}\left(\zeta +{\sqrt {\zeta ^{2}-1\,}}\right)\;.\end{aligned}}$

The general solution of the differential equation is an exponential in either root or a linear superposition of both,

$I(t)=A_{1}e^{s_{1}t}+A_{2}e^{s_{2}t}\;.$

The coefficients *A*1 and *A*2 are determined by the boundary conditions of the specific problem being analysed. That is, they are set by the values of the currents and voltages in the circuit at the onset of the transient and the presumed value they will settle to after infinite time. The differential equation for the circuit solves in three different ways depending on the value of ζ. These are overdamped (*ζ* > 1), underdamped (*ζ* < 1), and critically damped (*ζ* = 1).

#### Overdamped response

The overdamped response (*ζ* > 1) is

$I(t)=A_{1}e^{-\omega _{0}\left(\zeta +{\sqrt {\zeta ^{2}-1}}\right)t}+A_{2}e^{-\omega _{0}\left(\zeta -{\sqrt {\zeta ^{2}-1}}\right)t}\;.$

The overdamped response is a decay of the transient current without oscillation.

#### Underdamped response

The underdamped response (*ζ* < 1) is

$I(t)=B_{1}e^{-\alpha t}\cos(\omega _{\mathrm {d} }t)+B_{2}e^{-\alpha t}\sin(\omega _{\mathrm {d} }t)\,.$

By applying standard trigonometric identities the two trigonometric functions may be expressed as a single sinusoid with phase shift,

$I(t)=B_{3}e^{-\alpha t}\sin(\omega _{\mathrm {d} }t+\varphi )\;.$

The underdamped response is a decaying oscillation at frequency *ω*d. The oscillation decays at a rate determined by the attenuation α. The exponential in α describes the envelope of the oscillation. *B*1 and *B*2 (or *B*3 and the phase shift φ in the second form) are arbitrary constants determined by boundary conditions. The frequency *ω*d is given by

$\omega _{\mathrm {d} }={\sqrt {\omega _{0}^{2}-\alpha ^{2}}}=\omega _{0}{\sqrt {1-\zeta ^{2}\,}}\;.$

This is called the damped resonance frequency or the damped natural frequency. It is the frequency the circuit will naturally oscillate at if not driven by an external source. The resonance frequency, *ω*0, which is the frequency at which the circuit will resonate when driven by an external oscillation, may often be referred to as the undamped resonance frequency to distinguish it.

#### Critically damped response

The critically damped response (*ζ* = 1) is

$I(t)=D_{1}te^{-\alpha t}+D_{2}e^{-\alpha t}\;.$

The critically damped response represents the circuit response that decays in the fastest possible time without going into oscillation. This consideration is important in control systems where it is required to reach the desired state as quickly as possible without overshooting. *D*1 and *D*2 are arbitrary constants determined by boundary conditions.

### Laplace domain

The series RLC can be analyzed for both transient and steady AC state behavior using the Laplace transform. If the voltage source above produces a waveform with Laplace-transformed *V*(*s*) (where s is the complex frequency *s* = *σ* + *jω*), Kirchhoff's voltage law (KVL) can be applied in the Laplace domain:

$V(s)=I(s)\left(R+L\,s+{\frac {1}{\,C\,s\,}}\right)\,,$

where *I*(*s*) is the Laplace-transformed current through all components. Solving for *I*(*s*):

$I(s)={\frac {1}{\,R+L\,s+{\frac {1}{\,C\,s\,}}\,}}V(s)\;.$

And rearranging, we have

$I(s)={\frac {s}{\,L\ \left(s^{2}+{\frac {R}{\,L\,}}s+{\frac {1}{\,L\,C\,}}\right)\,}}V(s)\;.$

#### Laplace admittance

Solving for the Laplace admittance *Y*(*s*):

$Y(s)={\frac {I(s)}{\,V(s)\,}}={\frac {s}{\,L\ \left(s^{2}+{\frac {R}{\,L\,}}s+{\frac {1}{\,L\,C\,}}\right)\,}}\,.$

Simplifying using parameters α and *ω*0 defined in the previous section, we have

$Y(s)={\frac {I(s)}{\,V(s)\,}}={\frac {s}{\,L\ \left(s^{2}+2\alpha s+\omega _{0}^{2}\right)\,}}\;.$

#### Poles and zeros

The zeros of *Y*(*s*) are those values of s where *Y*(*s*) = 0:

$s=0\quad {\mbox{and}}\quad |s|\rightarrow \infty \;.$

The poles of *Y*(*s*) are those values of s where *Y*(*s*) → ∞. By the quadratic formula, we find

$s=-\alpha \pm {\sqrt {\alpha ^{2}-\omega _{0}^{2}\,}}\;.$

The poles of *Y*(*s*) are identical to the roots *s*1 and *s*2 of the characteristic polynomial of the differential equation in the section above.

#### General solution

For an arbitrary *V*(*t*), the solution obtained by inverse transform of *I*(*s*) is:

- In the underdamped case, *ω*0 > *α*: $I(t)={\frac {1}{\,L\,}}\ \int _{0}^{t}V(t-\tau )e^{-\alpha \tau }\left[\cos(\omega _{\mathrm {d} }\tau )-{\frac {\alpha }{\ \omega _{\mathrm {d} }\ }}\sin(\omega _{\mathrm {d} }\tau )\right]\,d\tau \,,$
- In the critically damped case, *ω*0 = *α*: $\ I(t)={\frac {1}{\ L\ }}\ \int _{0}^{t}V(t-\tau )e^{-\alpha \tau }\ \left[\ 1-\alpha \tau \ \right]\ \mathrm {d} \tau \ ,$
- In the overdamped case, *ω*0 < *α*: $\ I(t)={\frac {1}{\ L\ }}\ \int _{0}^{t}V(t-\tau )e^{-\alpha \tau }\left[\cosh(\omega _{\mathrm {r} }\tau )-{\frac {\alpha }{\ \omega _{\mathrm {r} }\ }}\sinh(\omega _{\mathrm {r} }\tau )\right]\,d\tau \ ,$

where *ω*r = √*α*2 − *ω*02, and cosh and sinh are the usual hyperbolic functions.

#### Sinusoidal steady state

Sinusoidal steady state is represented by letting *s* = *jω*, where j is the imaginary unit. Taking the magnitude of the above equation with this substitution:

${\big |}Y(j\omega ){\big |}={\frac {1}{{\sqrt {R^{2}+\left(\omega L-{\frac {1}{\,\omega C\,}}\right)^{2}}}\,}}\;.$

and the current as a function of ω can be found from

${\big |}I(j\omega ){\big |}={\big |}Y(j\omega ){\big |}\cdot {\bigl |}V(j\omega ){\bigr |}\;.$

There is a peak value of |*I*(*jω*)|. The value of ω at this peak is, in this particular case, equal to the undamped natural resonance frequency. This means that the maximum voltage across the resistor, and thus maximum heat dissipation, occurs at the natural frequency.

$\omega _{0}={\frac {1}{\,{\sqrt {L\ C\ }}\,}}\;.$

From the frequency response of the current, the frequency response of the voltages across the various circuit elements can also be determined (see figure). Moreover, the maximum voltage across the capacitor happens at a frequency

$\omega _{C}={\frac {\ {\sqrt {{\tfrac {L}{\ C\ }}-{\tfrac {1}{2}}R^{2}}}\ }{L}}=\omega _{0}{\sqrt {1-2\zeta ^{2}}}\;,$

whereas the maximum voltage across the inductor occurs at

$\omega _{L}={\frac {1}{\ C{\sqrt {{\tfrac {L}{\ C\ }}-{\tfrac {1}{2}}R^{2}\ }}\ }}={\frac {\omega _{0}}{\sqrt {1-2\zeta ^{2}}}}\;,$

where $\zeta ={\frac {R}{2}}{\sqrt {\frac {C}{L}}}$ for a series RLC circuit, as shown above.

It holds: $\omega _{C}<\omega _{0}<\omega _{L}$ .

## Parallel circuit

The properties of the parallel RLC circuit can be obtained from the duality relationship of electrical circuits and considering that the parallel RLC is the dual impedance of a series RLC. Considering this, it becomes clear that the differential equations describing this circuit are identical to the general form of those describing a series RLC.

For the parallel circuit, the attenuation α is given by

$\alpha ={\frac {1}{\,2\,R\,C\,}}$

and the damping factor is consequently

$\zeta ={\frac {1}{\,2\,R\,}}{\sqrt {{\frac {L}{C}}~}}\,~.$

Likewise, the other scaled parameters, fractional bandwidth and Q are also reciprocals of each other. This means that a wide-band, low-Q circuit in one topology will become a narrow-band, high-Q circuit in the other topology when constructed from components with identical values. The fractional bandwidth and Q of the parallel circuit are given by

${\begin{aligned}B_{\mathrm {f} }&={\frac {1}{\,R\,}}{\sqrt {{\frac {L}{C}}~}}\\Q&=R{\sqrt {{\frac {C}{L}}~}}\,~.\end{aligned}}$

Notice that the formulas here are the reciprocals of the formulas for the series circuit, given above.

### Frequency domain

The complex admittance of this circuit is given by adding up the admittances of the components:

${\begin{aligned}{\frac {1}{\,Z\,}}&={\frac {1}{\,Z_{L}\,}}+{\frac {1}{\,Z_{C}\,}}+{\frac {1}{\,Z_{R}\,}}\\&={\frac {1}{\,j\,\omega \,L\,}}+j\,\omega \,C+{\frac {1}{\,R\,}}\,.\end{aligned}}$

The change from a series arrangement to a parallel arrangement results in the circuit having a peak in impedance at resonance rather than a minimum, so the circuit is an anti-resonator.

The graph opposite shows that there is a minimum in the frequency response of the current at the resonance frequency $~\omega _{0}=1/{\sqrt {\,L\,C~}}~$ when the circuit is driven by a constant voltage. On the other hand, if driven by a constant current, there would be a maximum in the voltage which would follow the same curve as the current in the series circuit.

## Other configurations

A series resistor with the inductor in a parallel LC circuit as shown in Figure 4 is a topology commonly encountered where there is a need to take into account the resistance of the coil winding and its self-capacitance. Parallel LC circuits are frequently used for bandpass filtering and the Q is largely governed by this resistance. The resonant frequency of this circuit is

$\ \omega _{0}={\sqrt {{\frac {1}{\ LC\ }}-\left({\frac {R}{\ L\ }}\right)^{2}~}}\ .$

This is the resonant frequency of the circuit defined as the frequency at which the admittance has zero imaginary part. The frequency that appears in the generalised form of the characteristic equation (which is the same for this circuit as previously)

$\ s^{2}+2\alpha s+{\omega '_{0}}^{2}=0\$

is not the same frequency. In this case it is the natural, *undamped* resonant frequency:

$\ \omega '_{0}\equiv {\frac {1}{\ {\sqrt {LC~}}\ }}\ .$

The frequency *ω*max, at which the impedance magnitude is maximum, is given by

$\ \omega _{\mathrm {max} }=\omega '_{0}\ {\sqrt {-{\frac {1}{\ Q_{L}^{2}\ ~}}+{\sqrt {1+{\frac {2}{\ Q_{L}^{2}\ }}~}}~}}\ ,$

where *QL* ≡ ⁠*ω′*0*L*/*R*⁠ is the quality factor of the coil. This can be well approximated by

$\ \omega _{\mathrm {max} }\approx \omega '_{0}\ {\sqrt {1-{\frac {1}{\ 2Q_{L}^{4}\ }}~}}\ .$

Furthermore, the exact maximum impedance magnitude is given by

$\ |Z|_{\mathrm {max} }={\frac {RQ_{L}^{2}}{\ {\sqrt {2Q_{L}{\sqrt {Q_{L}^{2}+2\ }}-\left(2Q_{L}^{2}+1\right)~}}\ }}={\frac {RQ_{L}}{\ {\sqrt {2{\sqrt {1+2/Q_{L}^{2}\ }}-\left(2+1/Q_{L}^{2}\right)~}}\ }}\ .$

For values of $\ Q_{L}\gg 1\ ,$ this can be well approximated by

$\ |Z|_{\mathrm {max} }\approx RQ_{L}^{2}\ .$

In the same vein, a resistor in parallel with the capacitor in a series LC circuit can be used to represent a capacitor with a lossy dielectric. This configuration is shown in Figure 5. The resonant frequency (frequency at which the impedance has zero imaginary part) in this case is given by

$\ \omega _{0}={\sqrt {{\frac {1}{\ LC\ }}-{\frac {1}{\ (RC)^{2}\ }}\ }}\ ,$

while the frequency *ω*m at which the impedance magnitude is minimum is given by

$\ \omega _{\mathrm {m} }=\omega '_{0}\ {\sqrt {-{\frac {1}{\ Q_{C}^{2}\ }}+{\sqrt {1+{\frac {2}{\ Q_{C}^{2}\ }}\ }}\ }}\ ,$

where *QC* = *ω′*0*RC*.

## History

The first evidence that a capacitor could produce electrical oscillations was discovered in 1826 by French scientist Felix Savary. He found that when a Leyden jar was discharged through a wire wound around an iron needle, sometimes the needle was left magnetized in one direction and sometimes in the opposite direction. He correctly deduced that this was caused by a damped oscillating discharge current in the wire, which reversed the magnetization of the needle back and forth until it was too small to have an effect, leaving the needle magnetized in a random direction.

American physicist Joseph Henry repeated Savary's experiment in 1842 and came to the same conclusion, apparently independently. British scientist William Thomson (Lord Kelvin) in 1853 showed mathematically that the discharge of a Leyden jar through an inductance should be oscillatory, and derived its resonant frequency.

British radio researcher Oliver Lodge, by discharging a large battery of Leyden jars through a long wire, created a tuned circuit with its resonant frequency in the audio range, which produced a musical tone from the spark when it was discharged. In 1857, German physicist Berend Wilhelm Feddersen photographed the spark produced by a resonant Leyden jar circuit in a rotating mirror, providing visible evidence of the oscillations. In 1868, Scottish physicist James Clerk Maxwell calculated the effect of applying an alternating current to a circuit with inductance and capacitance, showing that the response is maximum at the resonant frequency.

The first example of an electrical resonance curve was published in 1887 by German physicist Heinrich Hertz in his pioneering paper on the discovery of radio waves, showing the length of spark obtainable from his spark-gap LC resonator detectors as a function of frequency.

One of the first demonstrations of resonance between tuned circuits was Lodge's "syntonic jars" experiment around 1889 He placed two resonant circuits next to each other, each consisting of a Leyden jar connected to an adjustable one-turn coil with a spark gap. When a high voltage from an induction coil was applied to one tuned circuit, creating sparks and thus oscillating currents, sparks were excited in the other tuned circuit only when the inductors were adjusted to resonance. Lodge and some English scientists preferred the term "*syntony*" for this effect, but the term "*resonance*" eventually stuck.

The first practical use for RLC circuits was in the 1890s in spark-gap radio transmitters to allow the receiver to be tuned to the transmitter. The first patent for a radio system that allowed tuning was filed by Lodge in 1897, although the first practical systems were invented in 1900 by Anglo Italian radio pioneer Guglielmo Marconi.

## Applications

### Variable tuned circuits

A very frequent use of these circuits is in the tuning circuits of analogue radios. Adjustable tuning is commonly achieved with a parallel plate variable capacitor which allows the value of C to be changed and tune to stations on different frequencies. For the IF stage in the radio where the tuning is preset in the factory, the more usual solution is an adjustable core in the inductor to adjust L. In this design, the core (made of a high permeability material that has the effect of increasing inductance) is threaded so that it can be screwed further in, or screwed further out of the inductor winding as required.

### Filters

|   |   |
|---|---|
|   |   |
|   |   |

In the filtering application, the resistor becomes the load that the filter is working into. The value of the damping factor is chosen based on the desired bandwidth of the filter. For a wider bandwidth, a larger value of the damping factor is required (and vice versa). The three components give the designer three degrees of freedom. Two of these are required to set the bandwidth and resonant frequency. The designer is still left with one which can be used to scale R, L and C to convenient practical values. Alternatively, R may be predetermined by the external circuitry which will use the last degree of freedom.

#### Low-pass filter

An RLC circuit can be used as a low-pass filter. The circuit configuration is shown in Figure 6. The corner frequency, that is, the frequency of the 3 dB point, is given by

$\omega _{\mathrm {c} }={\frac {1}{\sqrt {LC}}}\,.$

This is also the bandwidth of the filter. The damping factor is given by

$\zeta ={\frac {1}{2R_{L}}}{\sqrt {\frac {L}{C}}}\,.$

#### High-pass filter

A high-pass filter is shown in Figure 7. The corner frequency is the same as the low-pass filter:

$\omega _{\mathrm {c} }={\frac {1}{\sqrt {LC}}}\,.$

The filter has a stop-band of this width.

#### Band-pass filter

A band-pass filter can be formed with an RLC circuit by either placing a series LC circuit in series with the load resistor or else by placing a parallel LC circuit in parallel with the load resistor. These arrangements are shown in Figures 8 and 9 respectively. The centre frequency is given by

$\omega _{\mathrm {c} }={\frac {1}{\sqrt {LC}}}\,,$

and the bandwidth for the series circuit is

$\Delta \omega ={\frac {R_{L}}{L}}\,.$

The shunt version of the circuit is intended to be driven by a high impedance source, that is, a constant current source. Under those conditions the bandwidth is

$\Delta \omega ={\frac {1}{CR_{L}}}\,.$

#### Band-stop filter

Figure 10 shows a band-stop filter formed by a series LC circuit in shunt across the load. Figure 11 is a band-stop filter formed by a parallel LC circuit in series with the load. The first case requires a high impedance source so that the current is diverted into the resonator when it becomes low impedance at resonance. The second case requires a low impedance source so that the voltage is dropped across the antiresonator when it becomes high impedance at resonance.

### Oscillators

For applications in oscillator circuits, it is generally desirable to make the attenuation (or equivalently, the damping factor) as small as possible. In practice, this objective requires making the circuit's resistance R as small as physically possible for a series circuit, or alternatively increasing R to as much as possible for a parallel circuit. In either case, the RLC circuit becomes a good approximation to an ideal LC circuit. However, for very low-attenuation circuits (high Q-factor), issues such as dielectric losses of coils and capacitors can become important.

In an oscillator circuit

$\alpha \ll \omega _{0}\,,$

or equivalently

$\zeta \ll 1\,.$

As a result,

$\omega _{\mathrm {d} }\approx \omega _{0}\,.$

### Voltage multiplier

In a series RLC circuit at resonance, the current is limited only by the resistance of the circuit

$I={\frac {V}{R}}\,.$

If R is small, consisting only of the inductor winding resistance say, then this current will be large. It will drop a voltage across the inductor of

$V_{L}={\frac {V}{R}}\omega _{0}L\,.$

An equal magnitude voltage will also be seen across the capacitor but in antiphase to the inductor. If R can be made sufficiently small, these voltages can be several times the input voltage. The voltage ratio is, in fact, the Q of the circuit,

${\frac {V_{L}}{V}}=Q\,.$

A similar effect is observed with currents in the parallel circuit. Even though the circuit appears as high impedance to the external source, there is a large current circulating in the internal loop of the parallel inductor and capacitor.

### Pulse discharge circuit

An overdamped series RLC circuit can be used as a pulse discharge circuit. Often it is useful to know the values of components that could be used to produce a waveform. This is described by the form

$I(t)=I_{0}\left(\,e^{-\alpha \,t}-e^{-\beta \,t}\right)\,.$

Such a circuit could consist of an energy storage capacitor, a load in the form of a resistance, some circuit inductance and a switch – all in series. The initial conditions are that the capacitor is at voltage, *V*0, and there is no current flowing in the inductor. If the inductance L is known, then the remaining parameters are given by the following – capacitance:

$C={\frac {1}{~L\,\alpha \,\beta \,~}}\,,$

resistance (total of circuit and load):

$R=L\,(\,\alpha +\beta \,)\,,$

initial terminal voltage of capacitor:

$V_{0}=-I_{0}L\,\alpha \,\beta \,\left({\frac {1}{\beta }}-{\frac {1}{\alpha }}\right)\,.$

Rearranging for the case where R is known – capacitance:

$C={\frac {~\alpha +\beta ~}{R\,\alpha \,\beta }}\,,$

inductance (total of circuit and load):

$L={\frac {R}{\,\alpha +\beta ~}}\,,$

initial terminal voltage of capacitor:

$V_{0}={\frac {\,-I_{0}R\,\alpha \,\beta ~}{\alpha +\beta }}\left({\frac {1}{\beta }}-{\frac {1}{\alpha }}\right)\,.$

---
title: "Electrical impedance"
source: https://en.wikipedia.org/wiki/Electrical_impedance
domain: ferrite-bead
license: CC-BY-SA-4.0
tags: ferrite bead
fetched: 2026-07-03
---

# Electrical impedance

In electrical engineering, **impedance** is the opposition to alternating current presented by the combined effect of resistance and reactance in a circuit.

Quantitatively, the impedance of a two-terminal circuit element is the ratio of the complex representation of the sinusoidal voltage between its terminals, to the complex representation of the current flowing through it. In general, it depends upon the frequency of the sinusoidal voltage.

Impedance extends the concept of resistance to alternating current (AC) circuits, and possesses both magnitude and phase, unlike resistance, which has only magnitude.

Impedance can be represented as a complex number, with the same units as resistance, for which the SI unit is the ohm (Ω). Its symbol is usually *Z*, and it may be represented by writing its magnitude and phase in the polar form |*Z*|*∠θ*. However, Cartesian complex number representation is often more powerful for circuit analysis purposes.

The notion of impedance is useful for performing AC analysis of electrical networks, because it allows relating sinusoidal voltages and currents by a simple linear law. In multiple port networks, the two-terminal definition of impedance is inadequate, but the complex voltages at the ports and the currents flowing through them are still linearly related by the impedance matrix.

The reciprocal of impedance is admittance, whose SI unit is the siemens.

Instruments used to measure the electrical impedance are called impedance analyzers.

## History

Perhaps the earliest use of complex numbers in circuit analysis was by Johann Victor Wietlisbach in 1879 in analysing the Maxwell bridge. Wietlisbach avoided using differential equations by expressing AC currents and voltages as exponential functions with imaginary exponents (see § Validity of complex representation). Wietlisbach found the required voltage was given by multiplying the current by a complex number (impedance), although he did not identify this as a general parameter in its own right.

The term *impedance* was coined by Oliver Heaviside in July 1886. Heaviside recognised that the "resistance operator" (impedance) in his operational calculus was a complex number. In 1887 he showed that there was an AC equivalent to Ohm's law.

Arthur Kennelly published an influential paper on impedance in 1893. Kennelly arrived at a complex number representation in a rather more direct way than using imaginary exponential functions. Kennelly followed the graphical representation of impedance (showing resistance, reactance, and impedance as the lengths of the sides of a right angle triangle) developed by John Ambrose Fleming in 1889. Impedances could thus be added vectorially. Kennelly realised that this graphical representation of impedance was directly analogous to graphical representation of complex numbers (Argand diagram). Problems in impedance calculation could thus be approached algebraically with a complex number representation. Later that same year, Kennelly's work was generalised to all AC circuits by Charles Proteus Steinmetz. Steinmetz not only represented impedances by complex numbers but also voltages and currents. Unlike Kennelly, Steinmetz was thus able to express AC equivalents of DC laws such as Ohm's and Kirchhoff's laws. Steinmetz's work was highly influential in spreading the technique amongst engineers.

## Introduction

In addition to resistance as seen in DC circuits, impedance in AC circuits includes the effects of the induction of voltages in conductors by the magnetic fields (inductance), and the electrostatic storage of charge induced by voltages between conductors (capacitance). The impedance caused by these two effects is collectively referred to as reactance and forms the imaginary part of complex impedance whereas resistance forms the real part.

## Complex impedance

The impedance of a two-terminal circuit element is represented as a complex quantity Z . The polar form conveniently captures both magnitude and phase characteristics as

$\ Z=|Z|e^{j\arg(Z)}$

where the magnitude $|Z|$ represents the ratio of the voltage difference amplitude to the amplitude of the current, while the argument $\arg(Z)$ (commonly given the symbol $\theta$ ) gives the phase difference between voltage and current. In electrical engineering, the letter i is used for electric current, so the imaginary unit is instead represented by the letter j .

In Cartesian form, impedance is defined as

$\ Z=R+jX$

where the real part of impedance is the resistance R and the imaginary part is the reactance X.

Where it is needed to add or subtract impedances, the cartesian form is more convenient; but when quantities are multiplied or divided, the calculation becomes simpler if the polar form is used. A circuit calculation, such as finding the total impedance of two impedances in parallel, may require conversion between forms several times during the calculation. Conversion between the forms follows the normal conversion rules of complex numbers.

## Complex voltage and current

To simplify calculations, sinusoidal voltage and current waves are commonly represented as complex-valued functions of time denoted as V and I .

${\begin{aligned}V&=|V|e^{j(\omega t+\phi _{V})},\\I&=|I|e^{j(\omega t+\phi _{I})}.\end{aligned}}$

The impedance of a bipolar circuit is defined as the ratio of these quantities:

$Z={\frac {V}{I}}={\frac {|V|}{|I|}}e^{j(\phi _{V}-\phi _{I})}.$

Hence, denoting $\theta =\phi _{V}-\phi _{I}$ , we have

${\begin{aligned}\left|V\right|&=\left|I\right|\left|Z\right|,\\\phi _{V}&=\phi _{I}+\theta .\end{aligned}}$

The magnitude equation is the familiar Ohm's law applied to the voltage and current amplitudes, while the second equation defines the phase relationship.

### Validity of complex representation

This representation using complex exponentials may be justified by noting that (by Euler's formula):

$\ \cos(\omega t+\phi )={\tfrac {1}{2}}\left[e^{j(\omega t+\phi )}+e^{-j(\omega t+\phi )}\right]$

The real-valued sinusoidal function representing either voltage or current may be broken into two complex-valued functions. By the principle of superposition, we may analyse the behaviour of the sinusoid on the left-hand side by analysing the behaviour of the two complex terms on the right-hand side. Given the symmetry, we only need to perform the analysis for one right-hand term. The results are identical for the other. At the end of any calculation, we may return to real-valued sinusoids by further noting that

$\ \cos(\omega t+\phi )=\operatorname {Re} \left\{e^{j(\omega t+\phi )}\right\}$

### Ohm's law

The meaning of electrical impedance can be understood by substituting it into Ohm's law. Assuming a two-terminal circuit element with impedance Z is driven by a sinusoidal voltage or current as above, there holds

$V=IZ=I\left|Z\right|e^{j\arg(Z)}$

The magnitude of the impedance $|Z|$ acts just like resistance, giving the drop in voltage amplitude across an impedance Z for a given current I . The phase factor tells us that the current lags the voltage by a phase $\theta =\arg(Z)$ (i.e., in the time domain, the current signal is shifted ${\textstyle {\frac {\theta }{2\pi }}T}$ later with respect to the voltage signal).

Just as impedance extends Ohm's law to cover AC circuits, other results from DC circuit analysis, such as voltage division, current division, Thévenin's theorem and Norton's theorem, can also be extended to AC circuits by replacing resistance with impedance.

### Phasors

A phasor is represented by a constant complex number, usually expressed in exponential form, representing the complex amplitude (magnitude and phase) of a sinusoidal function of time. Phasors are used by electrical engineers to simplify computations involving sinusoids (such as in AC circuits), where they can often reduce a differential equation problem to an algebraic one.

The impedance of a circuit element can be defined as the ratio of the phasor voltage across the element to the phasor current through the element, as determined by the relative amplitudes and phases of the voltage and current. This is identical to the definition from Ohm's law given above, recognising that the factors of $e^{j\omega t}$ cancel.

## Device examples

### Resistor

The impedance of an ideal resistor is purely real and is called *resistive impedance*:

$\ Z_{R}=R$

In this case, the voltage and current waveforms are proportional and in phase.

### Inductor and capacitor (in the steady state)

Ideal inductors and capacitors have a purely imaginary *reactive impedance*:

the impedance of inductors increases as frequency increases;

$Z_{L}=j\omega L$

the impedance of capacitors decreases as frequency increases;

$Z_{C}={\frac {1}{j\omega C}}$

In both cases, for an applied sinusoidal voltage, the resulting current is also sinusoidal, but in quadrature, 90 degrees out of phase with the voltage. However, the phases have opposite signs: in an inductor, the current is *lagging*; in a capacitor the current is *leading*.

Note the following identities for the imaginary unit and its reciprocal:

${\begin{aligned}j&\equiv \cos {\left({\frac {\pi }{2}}\right)}+j\sin {\left({\frac {\pi }{2}}\right)}\equiv e^{j{\frac {\pi }{2}}}\\{\frac {1}{j}}\equiv -j&\equiv \cos {\left(-{\frac {\pi }{2}}\right)}+j\sin {\left(-{\frac {\pi }{2}}\right)}\equiv e^{j\left(-{\frac {\pi }{2}}\right)}\end{aligned}}$

Thus the inductor and capacitor impedance equations can be rewritten in polar form:

${\begin{aligned}Z_{L}&=\omega Le^{j{\frac {\pi }{2}}}\\Z_{C}&={\frac {1}{\omega C}}e^{j\left(-{\frac {\pi }{2}}\right)}\end{aligned}}$

The magnitude gives the change in voltage amplitude for a given current amplitude through the impedance, while the exponential factors give the phase relationship.

### Deriving the device-specific impedances

What follows below is a derivation of impedance for each of the three basic circuit elements: the resistor, the capacitor, and the inductor. Although the idea can be extended to define the relationship between the voltage and current of any arbitrary signal, these derivations assume sinusoidal signals. In fact, this applies to any arbitrary periodic signals, because these can be approximated as a sum of sinusoids through Fourier analysis.

#### Resistor

For a resistor, there is the relation $v_{\text{R}}{\mathord {\left(t\right)}}=i_{\text{R}}{\mathord {\left(t\right)}}R$

which is Ohm's law.

Considering the voltage signal to be $v_{\text{R}}(t)=V_{p}\sin(\omega t)$

it follows that ${\frac {v_{\text{R}}{\mathord {\left(t\right)}}}{i_{\text{R}}{\mathord {\left(t\right)}}}}={\frac {V_{p}\sin(\omega t)}{I_{p}\sin {\mathord {\left(\omega t\right)}}}}=R$

This says that the ratio of AC voltage amplitude to alternating current (AC) amplitude across a resistor is R , and that the AC voltage leads the current across a resistor by 0 degrees.

This result is commonly expressed as $Z_{\text{resistor}}=R$

#### Capacitor (in the steady state)

For a capacitor, there is the relation: $i_{\text{C}}(t)=C{\frac {\mathrm {d} v_{\text{C}}(t)}{\mathrm {d} t}}$

Considering the voltage signal to be $v_{\text{C}}(t)=V_{p}e^{j\omega t}$

it follows that ${\frac {\mathrm {d} v_{\text{C}}(t)}{\mathrm {d} t}}=j\omega V_{p}e^{j\omega t}$

and thus, as previously, $Z_{\text{capacitor}}={\frac {v_{\text{C}}{\mathord {\left(t\right)}}}{i_{\text{C}}{\mathord {\left(t\right)}}}}={\frac {1}{j\omega C}}.$

Conversely, if the current through the circuit is assumed to be sinusoidal, its complex representation being $i_{\text{C}}(t)=I_{p}e^{j\omega t}$ then integrating the differential equation $i_{\text{C}}(t)=C{\frac {\mathrm {d} v_{\text{C}}(t)}{\mathrm {d} t}}$ leads to $v_{C}(t)={\frac {1}{j\omega C}}I_{p}e^{j\omega t}+{\text{Const.}}={\frac {1}{j\omega C}}i_{C}(t)+{\text{Const.}}$ The *Const* term represents a fixed potential bias superimposed to the AC sinusoidal potential, that plays no role in AC analysis. For this purpose, this term can be assumed to be 0, hence again the impedance $Z_{\text{capacitor}}={\frac {1}{j\omega C}}.$

#### Inductor (in the steady state)

For the inductor, we have the relation (from Faraday's law): $v_{\text{L}}(t)=L{\frac {\mathrm {d} i_{\text{L}}(t)}{\mathrm {d} t}}$

This time, considering the current signal to be: $i_{\text{L}}(t)=I_{p}\sin(\omega t)$

it follows that: ${\frac {\mathrm {d} i_{\text{L}}(t)}{\mathrm {d} t}}=\omega I_{p}\cos {\mathord {\left(\omega t\right)}}$

This result is commonly expressed in polar form as $Z_{\text{inductor}}=\omega Le^{j{\frac {\pi }{2}}}$

or, using Euler's formula, as $Z_{\text{inductor}}=j\omega L$

As in the case of capacitors, it is also possible to derive this formula directly from the complex representations of the voltages and currents, or by assuming a sinusoidal voltage between the two poles of the inductor. In the latter case, integrating the differential equation above leads to a constant term for the current, that represents a fixed DC bias flowing through the inductor. This is set to zero because AC analysis using frequency domain impedance considers one frequency at a time and DC represents a separate frequency of zero hertz in this context.

## Generalised s-plane impedance

The impedance of capacitors and inductors were defined above in terms of *$j\omega$*, but this simplification can strictly be applied only to circuits that are driven with steady state AC and DC signals, a condition called the *steady state*. The mere act of turning a signal source ON or OFF violates this steady state condition. To allow evaluation of the transient response in addition to the steady state of a circuit, the concept of impedance can be extended to a circuit energised with any arbitrary signal by using complex frequency $s{=}\sigma {+}j\omega$ instead of just $j\omega$ . Signals are expressed in terms of complex frequency by taking the Laplace transform of the time domain expression of the signal. The impedance of the basic circuit elements in this more general notation is as follows:

| Element | Impedance expression |
|---|---|
| Resistor | $R\,$ |
| Inductor | $sL\,$ |
| Capacitor | ${\frac {1}{sC}}\,$ |

For a steady state signal, s simplifies to $j\omega$ . This further simplifies to $s{=}0$ for a DC-only circuit, in which case every inductor will behave as a short circuit and every capacitor will behave as an open circuit.

### Formal derivation

The impedance Z of an electrical component is defined as the ratio between the Laplace transforms of the voltage over it and the current through it, i.e.

$Z(s)={\frac {{\mathcal {L}}\{v(t)\}}{{\mathcal {L}}\{i(t)\}}}={\frac {V(s)}{I(s)}}\qquad {\text{(general impedance)}}$

where $s=\sigma +j\omega$ is the complex Laplace parameter.

#### Inductor

Using the current–voltage relationship of an inductor $[v(t){=}L{\tfrac {\mathrm {d} i(t)}{\mathrm {d} t}}]$ , the Laplace transform of its voltage is: ${\mathcal {L}}\{v(t)\}={\mathcal {L}}\left\{L\,{\tfrac {\mathrm {d} i(t)}{\mathrm {d} t}}\right\}=sL\,{\mathcal {L}}\{i(t)\}\,.$

Rearranging so that ${\mathcal {L}}\{v(t)\}$ is divided by ${\mathcal {L}}\{i(t)\}$ provides the inductor's impedance: $Z_{L}(s){=}sL$ .

#### Capacitor

Using the current–voltage relationship of a capacitor $[i(t){=}C{\tfrac {\mathrm {d} v(t)}{\mathrm {d} t}}]$ , the Laplace transform of its current is:

${\mathcal {L}}\{i(t)\}={\mathcal {L}}\left\{C\,{\tfrac {\mathrm {d} v(t)}{\mathrm {d} t}}\right\}=sC\,{\mathcal {L}}\{v(t)\}\,.$

Rearranging so that ${\mathcal {L}}\{v(t)\}$ is divided by ${\mathcal {L}}\{i(t)\}$ provides the capacitor's impedance: $Z_{C}(s){=}{\tfrac {1}{sC}}$ .

### Relation to phasors

In the phasor regime (steady state, meaning all signals are represented mathematically as simple complex exponentials $v(t)={\hat {V}}\,e^{j\omega t}$ and $i(t)={\hat {I}}\,e^{j\omega t}$ oscillating at a common frequency $\omega$ ), impedance can simply be calculated as the voltage-to-current ratio, in which the common time-dependent factor cancels out:

$Z(\omega )={\frac {v(t)}{i(t)}}={\frac {{\hat {V}}\,e^{j\omega t}}{{\hat {I}}\,e^{j\omega t}}}={\frac {\hat {V}}{\hat {I}}}\qquad {\text{(phasor-regime impedance)}}$

The phasor domain is sometimes dubbed the frequency domain, although it lacks one of the dimensions of the Laplace parameter. For steady-state, the polar form of the complex impedance relates the amplitude and phase of the voltage and current. In particular:

- The magnitude of the complex impedance is the ratio of the voltage amplitude to the current amplitude;
- The phase of the complex impedance is the phase shift by which the current lags the voltage.

These two relationships hold even after taking the real part of the complex exponentials (see phasors), which is the part of the signal one actually measures in real-life circuits.

## Resistance vs reactance

Resistance and reactance together determine the magnitude and phase of the impedance through the following relations:

${\begin{aligned}|Z|&={\sqrt {ZZ^{*}}}={\sqrt {R^{2}+X^{2}}}\\\theta &=\arctan {\left({\frac {X}{R}}\right)}\end{aligned}}$

In many applications, the relative phase of the voltage and current is not critical so only the magnitude of the impedance is significant.

### Resistance

Resistance R is the real part of impedance; a device with a purely resistive impedance exhibits no phase shift between the voltage and current.

$\ R=|Z|\cos {\theta }\quad$

### Reactance

Reactance X is the imaginary part of the impedance; a component with a finite reactance induces a phase shift $\theta$ between the voltage across it and the current through it.

$\ X=|Z|\sin {\theta }\quad$

A purely reactive component is distinguished by the sinusoidal voltage across the component being in quadrature with the sinusoidal current through the component. This implies that the component alternately absorbs energy from the circuit and then returns energy to the circuit. A pure reactance does not dissipate any power.

#### Capacitive reactance

A capacitor has a purely reactive impedance that is inversely proportional to the signal frequency. A capacitor consists of two conductors separated by an insulator, also known as a dielectric.

$X_{\mathsf {C}}={\frac {-1}{\omega \,C}}={\frac {-1}{2\pi f\,C}}~.$

The minus sign indicates that the imaginary part of the impedance is negative.

At low frequencies, a capacitor approaches an open circuit so no current flows through it.

A DC voltage applied across a capacitor causes charge to accumulate on one side; the electric field due to the accumulated charge is the source of the opposition to the current. When the potential associated with the charge exactly balances the applied voltage, the current goes to zero.

Driven by an AC supply, a capacitor accumulates only a limited charge before the potential difference changes sign and the charge dissipates. The higher the frequency, the less charge accumulates and the smaller the opposition to the current.

#### Inductive reactance

Inductive reactance $X_{L}$ is proportional to the signal frequency f and the inductance L .

$X_{L}=\omega L=2\pi fL\quad$

An inductor consists of a coiled conductor. Faraday's law of electromagnetic induction gives the back emf ${\mathcal {E}}$ (voltage opposing current) due to a rate-of-change of magnetic flux density B through a current loop.

${\mathcal {E}}=-{{d\Phi _{B}} \over dt}\quad$

For an inductor consisting of a coil with N loops this gives:

${\mathcal {E}}=-N{d\Phi _{B} \over dt}\quad$

The back-emf is the source of the opposition to current flow. A constant direct current has a zero rate-of-change, and sees an inductor as a short-circuit (it is typically made from a material with a low resistivity). An alternating current has a time-averaged rate-of-change that is proportional to frequency, this causes the increase in inductive reactance with frequency.

#### Total reactance

The total reactance is given by

${X=X_{L}+X_{C}}$ ( $X_{C}$ is negative)

so that the total impedance is

$\ Z=R+jX$

## Combining impedances

The total impedance of many simple networks of components can be calculated using the rules for combining impedances in series and parallel. The rules are identical to those for combining resistances, except that the numbers in general are complex numbers. The general case, however, requires equivalent impedance transforms in addition to series and parallel.

### Series combination

For components connected in series, the current through each circuit element is the same; the total impedance is the sum of the component impedances.

$\ Z_{\text{eq}}=Z_{1}+Z_{2}+\cdots +Z_{n}\quad$

Or explicitly in real and imaginary terms: $\ Z_{\text{eq}}=R+jX=(R_{1}+R_{2}+\cdots +R_{n})+j(X_{1}+X_{2}+\cdots +X_{n})\quad$

### Parallel combination

For components connected in parallel, the voltage across each circuit element is the same; the ratio of currents through any two elements is the inverse ratio of their impedances.

Hence the inverse total impedance is the sum of the inverses of the component impedances: ${\frac {1}{Z_{\text{eq}}}}={\frac {1}{Z_{1}}}+{\frac {1}{Z_{2}}}+\cdots +{\frac {1}{Z_{n}}}$

or, when n = 2: ${\frac {1}{Z_{\text{eq}}}}={\frac {1}{Z_{1}}}+{\frac {1}{Z_{2}}}={\frac {Z_{1}+Z_{2}}{Z_{1}Z_{2}}}$ $\ Z_{\text{eq}}={\frac {Z_{1}Z_{2}}{Z_{1}+Z_{2}}}$

The equivalent impedance $Z_{\text{eq}}$ can be calculated in terms of the equivalent series resistance $R_{\text{eq}}$ and reactance $X_{\text{eq}}$ .

${\begin{aligned}Z_{\text{eq}}&=R_{\text{eq}}+jX_{\text{eq}}\\R_{\text{eq}}&={\frac {(X_{1}R_{2}+X_{2}R_{1})(X_{1}+X_{2})+(R_{1}R_{2}-X_{1}X_{2})(R_{1}+R_{2})}{(R_{1}+R_{2})^{2}+(X_{1}+X_{2})^{2}}}\\X_{\text{eq}}&={\frac {(X_{1}R_{2}+X_{2}R_{1})(R_{1}+R_{2})-(R_{1}R_{2}-X_{1}X_{2})(X_{1}+X_{2})}{(R_{1}+R_{2})^{2}+(X_{1}+X_{2})^{2}}}\end{aligned}}$

## Measurement

The measurement of the impedance of devices and transmission lines is a practical problem in radio technology and other fields. Measurements of impedance may be carried out at one frequency, or the variation of device impedance over a range of frequencies may be of interest. The impedance may be measured or displayed directly in ohms, or other values related to impedance may be displayed; for example, in a radio antenna, the standing wave ratio or reflection coefficient may be more useful than the impedance alone. The measurement of impedance requires the measurement of the magnitude of voltage and current, and the phase difference between them. Impedance is often measured by "bridge" methods, similar to the direct-current Wheatstone bridge; a calibrated reference impedance is adjusted to balance off the effect of the impedance of the device under test. Impedance measurement in power electronic devices may require simultaneous measurement and provision of power to the operating device.

The impedance of a device can be calculated by complex division of the voltage and current. The impedance of the device can be calculated by applying a sinusoidal voltage to the device in series with a resistor, and measuring the voltage across the resistor and across the device. Performing this measurement by sweeping the frequencies of the applied signal provides the impedance phase and magnitude.

The use of an impulse response may be used in combination with the fast Fourier transform (FFT) to rapidly measure the electrical impedance of various electrical devices.

The LCR meter measures a component's inductance (L), capacitance (C), and resistance (R); from these values, the impedance at any frequency can be calculated.

### Example

Consider a parallel LC tank circuit. The complex impedance of the circuit is $Z(\omega )={\frac {j\omega L}{1-\omega ^{2}LC}}.$ It is immediately seen that the value of ${\textstyle {1 \over |Z|}}$ is minimal (actually equal to 0 in this case) whenever $\omega ^{2}LC=1.$ Therefore, the fundamental resonance angular frequency is $\omega ={1 \over {\sqrt {LC}}}.$

## Variable impedance

In general, neither impedance nor admittance can vary with time, since they are defined for complex exponentials in which −∞ < *t* < +∞. If the complex exponential voltage to current ratio changes over time or amplitude, the circuit element cannot be described using the frequency domain. However, many components and systems (e.g., varicaps that are used in radio tuners) may exhibit non-linear or time-varying voltage to current ratios that seem to be linear time-invariant (LTI) for small signals and over small observation windows, so they can be roughly described as if they had a time-varying impedance. This description is an approximation: Over large signal swings or wide observation windows, the voltage to current relationship will not be LTI and cannot be described by impedance.

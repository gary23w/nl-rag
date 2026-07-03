---
title: "Electrical reactance"
source: https://en.wikipedia.org/wiki/Electrical_reactance
domain: electrical-reactance
license: CC-BY-SA-4.0
tags: electrical reactance
fetched: 2026-07-03
---

# Electrical reactance

In electrical circuits, **reactance** is the opposition presented to alternating current by inductance and capacitance. It is measured in ohms. Along with resistance, it is one of two elements of impedance; however, while both elements involve transfer of electrical energy, no dissipation of electrical energy as heat occurs in reactance; instead, the reactance stores energy until a quarter-cycle later when the energy is returned to the circuit. Greater reactance gives smaller current for the same applied voltage.

Reactance is used to compute amplitude and phase changes of sinusoidal alternating current going through a circuit element. Like resistance, reactance is measured in ohms, with positive values indicating **inductive** reactance and negative indicating **capacitive** reactance. It is denoted by the symbol ⁠ X ⁠. An ideal resistor has zero reactance, whereas ideal reactors have no shunt conductance and no series resistance. As frequency increases, inductive reactance increases and capacitive reactance decreases.

## Comparison to resistance

Reactance is similar to resistance in that larger reactance leads to smaller currents for the same applied voltage. Furthermore, a circuit made entirely of elements that have only reactance (and no resistance) can be treated the same way as a circuit made entirely of resistances. These same techniques can also be used to combine elements with reactance with elements with resistance, but complex numbers are typically needed. This is treated below in the section on impedance.

There are several important differences between reactance and resistance, though. First, reactance changes the phase so that the current through the element is shifted by a quarter of a cycle relative to the phase of the voltage applied across the element. Second, power is not dissipated in a purely reactive element but is stored instead. Third, reactances can be negative so that they can 'cancel' each other out. Finally, the main circuit elements that have reactance (capacitors and inductors) have a frequency dependent reactance, unlike resistors which have the same resistance for all frequencies, at least in the ideal case.

The term *reactance* was first suggested by French engineer Édouard Hospitalier in *L'Industrie Electrique* on 10 May 1893. It was officially adopted by the American Institute of Electrical Engineers in May 1894.

## Capacitive reactance

A capacitor consists of two conductors separated by an insulator, also known as a dielectric.

**Capacitive reactance** is an opposition to the change of voltage across an element. Capacitive reactance $X_{C}$ is inversely proportional to the signal frequency f (or angular frequency $\omega$ ) and the capacitance ⁠ C ⁠.

There are two choices in the literature for defining reactance for a capacitor. One is to use a uniform notion of reactance as the imaginary part of impedance, in which case the reactance of a capacitor is the negative number, $X_{C}=-{\frac {1}{\omega C}}=-{\frac {1}{2\pi fC}}.$

Another choice is to define capacitive reactance as a positive number, $X_{C}={\frac {1}{\omega C}}={\frac {1}{2\pi fC}}.$

In this case however one needs to remember to add a negative sign for the impedance of a capacitor, i.e. ⁠ $Z_{c}=-jX_{c}$ ⁠.

At ⁠ $f=0$ ⁠, the magnitude of the capacitor's reactance is infinite, behaving like an open circuit (preventing any current from flowing through the dielectric). As frequency increases, the magnitude of reactance decreases, allowing more current to flow. As f approaches ⁠ $\infty$ ⁠, the capacitor's reactance approaches ⁠ 0 ⁠, behaving like a short circuit.

The application of a DC voltage across a capacitor causes positive charge to accumulate on one side and negative charge to accumulate on the other side; the electric field due to the accumulated charge is the source of the opposition to the current. When the potential associated with the charge exactly balances the applied voltage, the current goes to zero.

Driven by an AC supply (ideal AC current source), a capacitor will only accumulate a limited amount of charge before the potential difference changes polarity and the charge is returned to the source. The higher the frequency, the less charge will accumulate and the smaller the opposition to the current.

## Inductive reactance

Inductive reactance is a property exhibited by an inductor, and inductive reactance exists based on the fact that an electric current produces a magnetic field around it. In the context of an AC circuit (although this concept applies any time current is changing), this magnetic field is constantly changing as a result of current that oscillates back and forth. It is this change in magnetic field that induces another electric current to flow in the same wire – called counter-electromotive force (counter-EMF) – in a direction such as to oppose the flow of the current originally responsible for producing the magnetic field (known as Lenz's law). Hence, **inductive reactance** is an opposition to the change of current through an element.

For an ideal inductor in an AC circuit, the inhibitive effect on change in current flow results in a delay, or a phase shift, of the alternating current with respect to alternating voltage. Specifically, an ideal inductor (with no resistance) will cause the current to lag the voltage by a quarter cycle, or 90°.

In electric power systems, inductive reactance (and capacitive reactance, however inductive reactance is more common) can limit the power capacity of an AC transmission line, because power is not completely transferred when voltage and current are out-of-phase (detailed above). That is, current will flow for an out-of-phase system, however real power at certain times will not be transferred, because there will be points during which instantaneous current is positive while instantaneous voltage is negative, or vice versa, implying negative power transfer. Hence, real work is not performed when power transfer is "negative". However, current still flows even when a system is out-of-phase, which causes transmission lines to heat up due to current flow. Consequently, transmission lines can only heat up so much (or else they would physically sag too much, due to the heat expanding the metal transmission lines), so transmission line operators have a "ceiling" on the amount of current that can flow through a given line, and excessive inductive reactance can limit the power capacity of a line. Power providers utilize capacitors to shift the phase and minimize the losses, based on usage patterns.

Inductive reactance $X_{L}$ is proportional to the sinusoidal signal frequency f and the inductance ⁠ L ⁠, which depends on the physical shape of the inductor: $X_{L}=\omega L=2\pi fL.$

The average current flowing through an inductance L in series with a sinusoidal AC voltage source of RMS amplitude A and frequency f is equal to: $I_{L}={A \over \omega L}={A \over 2\pi fL}.$

Because a square wave has multiple amplitudes at sinusoidal harmonics, the average current flowing through an inductance L in series with a square wave AC voltage source of RMS amplitude A and frequency f is equal to: $I_{L}={A\pi ^{2} \over 8\omega L}={A\pi \over 16fL},$ making it appear as if the inductive reactance to a square wave was about 19% smaller $X_{L}={16 \over \pi }fL$ than the reactance to the AC sine wave.

Any conductor of finite dimensions has inductance; the inductance is made larger by the multiple turns in an electromagnetic coil. Faraday's law of electromagnetic induction gives the counter-emf ${\mathcal {E}}$ (voltage opposing current) due to a rate-of-change of magnetic flux density $\scriptstyle {B}$ through a current loop: ${\mathcal {E}}=-{{d\Phi _{B}} \over dt}.$

For an inductor consisting of a coil with N loops this gives: ${\mathcal {E}}=-N{d\Phi _{B} \over dt}.$

The counter-emf is the source of the opposition to current flow. A constant direct current has a zero rate-of-change, and sees an inductor as a short-circuit (it is typically made from a material with a low resistivity). An alternating current has a time-averaged rate-of-change that is proportional to frequency, this causes the increase in inductive reactance with frequency.

## Impedance

Both reactance X and resistance R are components of impedance ⁠ $\mathbf {Z}$ ⁠: $\mathbf {Z} =R+\mathbf {j} X,$ where:

- $\mathbf {Z}$ is the complex impedance, measured in ohms;
- R is the resistance, measured in ohms – it is the real part of the impedance ${R={\text{Re}}{(\mathbf {Z} )}}$ ;
- X is the reactance, measured in ohms – it is the imaginary part of the impedance ${X={\text{Im}}{(\mathbf {Z} )}}$ ; and
- $\mathbf {j}$ is the square root of negative one, usually represented by $\mathbf {i}$ in non-electrical formulas. $\mathbf {j}$ is used so as not to confuse the imaginary unit with current, commonly represented by ⁠ $\mathbf {i}$ ⁠.

When both a capacitor and an inductor are placed in series in a circuit, their contributions to the total circuit impedance are opposite. Capacitive reactance $X_{C}$ and inductive reactance $X_{L}$ contribute to the total reactance X as follows: ${X=X_{L}+X_{C}=\omega L-{\frac {1}{\omega C}}},$ where:

- $X_{L}$ is the inductive reactance, measured in ohms;
- $X_{C}$ is the capacitive reactance, measured in ohms; and
- $\omega$ is the angular frequency, $2\pi$ times the frequency in Hz.

Hence:

- if ⁠ $\scriptstyle X>0$ ⁠, the total reactance is said to be inductive;
- if ⁠ $\scriptstyle X=0$ ⁠, then the impedance is purely resistive;
- if ⁠ $\scriptstyle X<0$ ⁠, the total reactance is said to be capacitive.

Note however that if $X_{L}$ and $X_{C}$ are assumed both positive by definition, then the intermediary formula changes to a difference: ${X=X_{L}-X_{C}=\omega L-{\frac {1}{\omega C}}},$ but the ultimate value is the same.

### Phase relationship

The phase of the voltage across a purely reactive device (i.e. with zero parasitic resistance) *lags* the current by ${\tfrac {\pi }{2}}$ radians for a capacitive reactance and *leads* the current by ${\tfrac {\pi }{2}}$ radians for an inductive reactance. Without knowledge of both the resistance and reactance the relationship between voltage and current cannot be determined.

The origin of the different signs for capacitive and inductive reactance is the phase factor $e^{\pm \mathbf {j} {\frac {\pi }{2}}}$ in the impedance: ${\begin{aligned}\mathbf {Z} _{C}&={1 \over \omega C}e^{-\mathbf {j} {\pi \over 2}}=\mathbf {j} \left({-{\frac {1}{\omega C}}}\right)=\mathbf {j} X_{C},\\\mathbf {Z} _{L}&=\omega Le^{\mathbf {j} {\pi \over 2}}=\mathbf {j} \omega L=\mathbf {j} X_{L}\quad .\end{aligned}}$

For a reactive component the sinusoidal voltage across the component is in quadrature (a ${\tfrac {\pi }{2}}$ phase difference) with the sinusoidal current through the component. The component alternately absorbs energy from the circuit and then returns energy to the circuit, thus a pure reactance does not dissipate power.

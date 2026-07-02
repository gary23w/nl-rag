---
title: "Instrumentation amplifier"
source: https://en.wikipedia.org/wiki/Instrumentation_amplifier
domain: instrumentation-amplifier
license: CC-BY-SA-4.0
tags: instrumentation amplifier, common-mode rejection ratio, differential amplifier, operational amplifier
fetched: 2026-07-02
---

# Instrumentation amplifier

An **instrumentation amplifier** (sometimes shorthanded as **in-amp** or **InAmp**) is a precision differential amplifier that has been outfitted with input buffer amplifiers, which eliminate the need for input impedance matching and thus make the amplifier particularly suitable for use in measurement and test equipment. Additional characteristics include very low DC offset, low drift, low noise, very high open-loop gain, very high common-mode rejection ratio, and very high input impedances. Instrumentation amplifiers are used where great accuracy and stability of the circuit both short- and long-term are required.

Although the instrumentation amplifier is usually shown schematically identical to a standard operational amplifier (op-amp), the electronic instrumentation amplifier is almost always internally composed of 3 op-amps. These are arranged so that there is one op-amp to buffer each input (+, −), and one to produce the desired output with adequate impedance matching for the function.

While the instrumentation amplifier is optimized for the task of precise amplification of high-impedance voltage signals, this design choice comes at the cost of flexibility: the instrumentation amplifier is thus not intended to perform integration, differentiation, rectification, or any other non-voltage-gain function, which are best left to op-amps.

The most commonly used instrumentation amplifier circuit is shown in the figure. The gain of the circuit is

$A_{v}={\frac {V_{\text{out}}}{V_{2}-V_{1}}}=\left(1+{\frac {2R_{1}}{R_{\text{gain}}}}\right){\frac {R_{3}}{R_{2}}}.$

The rightmost amplifier, along with the resistors labelled $R_{2}$ and $R_{3}$ is just the standard differential-amplifier circuit, with gain $R_{3}/R_{2}$ and differential input resistance $2\cdot R_{2}$ . The two amplifiers on the left are the buffers. With $R_{\text{gain}}$ removed (open-circuited), they are simple unity-gain buffers; the circuit will work in that state, with gain simply equal to $R_{3}/R_{2}$ and high input impedance because of the buffers. The buffer gain could be increased by putting resistors between the buffer inverting inputs and ground to shunt away some of the negative feedback; however, the single resistor $R_{\text{gain}}$ between the two inverting inputs is a much more elegant method: it increases the differential-mode gain of the buffer pair while leaving the common-mode gain equal to 1. This increases the common-mode rejection ratio (CMRR) of the circuit and also enables the buffers to handle much larger common-mode signals without clipping than would be the case if they were separate and had the same gain. Another benefit of the method is that it boosts the gain using a single resistor rather than a pair, thus avoiding a resistor-matching problem and very conveniently allowing the gain of the circuit to be changed by changing the value of a single resistor. A set of switch-selectable resistors or even a potentiometer can be used for $R_{\text{gain}}$ , providing easy changes to the gain of the circuit, without the complexity of having to switch matched pairs of resistors.

The ideal common-mode gain of an instrumentation amplifier is zero. In the circuit shown, common-mode gain is caused by mismatch in the resistor ratios $R_{2}/R_{3}$ and by the mismatch in common-mode gains of the two input op-amps. Obtaining very closely matched resistors is a significant difficulty in fabricating these circuits, as is optimizing the common-mode performance.

An instrumentation amplifier can also be built with two op-amps to save on cost, but the gain must be higher than two (+6 dB).

Instrumentation amplifiers can be built with individual op-amps and precision resistors, but are also available in integrated circuit form from several manufacturers (including Texas Instruments, Analog Devices, and Renesas Electronics). An IC instrumentation amplifier typically contains closely matched laser-trimmed resistors, and therefore offers excellent common-mode rejection. Examples include INA128, AD8221, LT1167 and MAX4194.

Instrumentation amplifiers can also be designed using "indirect current-feedback architecture", which extend the operating range of these amplifiers to the negative power supply rail, and in some cases the positive power supply rail. This can be particularly useful in single-supply systems, where the negative power rail is simply the circuit ground (GND). Examples of parts utilizing this architecture are MAX4208/MAX4209 and AD8129/AD8130 Archived 11 November 2014 at the Wayback Machine.

## Types

**Feedback-free instrumentation amplifier** is the high-input-impedance differential amplifier designed without the external feedback network. This allows reduction in the number of amplifiers (one instead of three), reduced noise (no thermal noise is brought on by the feedback resistors) and increased bandwidth (no frequency compensation is needed). Chopper-stabilized (or zero-drift) instrumentation amplifiers such as the LTC2053 use a switching-input frontend to eliminate DC offset errors and drift.

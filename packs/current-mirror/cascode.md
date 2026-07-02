---
title: "Cascode"
source: https://en.wikipedia.org/wiki/Cascode
domain: current-mirror
license: CC-BY-SA-4.0
tags: current mirror, Wilson current mirror, cascode stage, output impedance
fetched: 2026-07-02
---

# Cascode

The **cascode** is a two-stage amplifier that consists of a common emitter stage feeding into a common base stage when using bipolar junction transistors (BJTs) or alternatively a common source stage feeding a common gate stage when using field-effect transistors (FETs).

Because there is no direct coupling from the output to input, the Miller effect is eliminated, contributing to a much higher bandwidth. Compared to a single amplifier stage, this combination may have one or more of the following characteristics: higher input–output isolation, higher input impedance, high output impedance, higher bandwidth.

## History

The use of a cascode (sometimes verbified to *cascoding*) is a common technique for improving analog circuit performance, applicable to both vacuum tubes and transistors. The name "cascode" was coined in an article written by Frederick Vinton Hunt and Roger Wayne Hickman in 1939, in a discussion on the application of voltage stabilizers. They proposed a cascade of two triodes (the first one with a common cathode setup, the second one with a common grid) as a replacement for a pentode, and so the name may be assumed to be an abbreviation of "casc(aded triode amplifier having characteristics similar to, but less noisy than, a single pent)ode". Cascode circuits were employed in early television sets for the 'front-end' or tuner because of their low noise and wider bandwidth.

Bipolar Junction Transistors have collector-base parasitic capacitance in the low picofarad to fractional picofarad range. The Miller effect means that when this capacitance is in the feedback path, it results in an effective input capacitance that is multiplied by the stage gain: a feedback capacitance of only 1.0 pF in a circuit with a voltage gain of 50 results in an effective input capacitance of 51 pF. While this can be overcome in radio frequency circuits/tuned circuits by "neutralising" feedback in opposition, it is more difficult to combat in wideband circuits such as video amplifiers, whose bandwidths range from analog television (some 5 MHz for PAL), to at least 86 MHz in the older VGA format (UXGA, 1600 × 1200, 60 Hz refresh). Video amplifiers cannot operate to such high frequencies with any appreciable collector-base feedback, so the cascode, with its very low effective feedback capacitance, is the design-of-choice for video amplifiers in CRT-based monitors.

**Hybrid cascode amplifiers** use different device types for the lower and upper elements. A low-voltage device such as a bipolar junction transistor or field-effect transistor is often used as the lower transconductance element, while a higher-voltage device above it withstands large voltage swings and suppresses Miller capacitance. Tektronix published a theoretical analysis of tube–transistor hybrid cascode stages in the 1960s, deriving gain equations and comparing their behavior with all-tube cascodes and pentode amplifiers. This approach was used in commercial audio equipment; manufacturer schematics for some Music Man guitar amplifiers show a solid-state device cascoded with a vacuum tube.

In the 1960s, **MOS tetrode devices** were described and analyzed as cascode structures formed from two merged MOS triodes. The reduced Miller effect of this configuration enabled operation at frequencies exceeding 200 MHz. Such devices were treated as cascode pairs in analyses of high-frequency MOS behavior. A later example is the BF961 dual-gate MOS tetrode, whose internal structure reflects this approach.

## Operation

Figure 1 shows an example of a cascode amplifier with a common-source amplifier as the input stage driven by a signal source, *V*in. This input stage drives a common-gate amplifier as the output stage, with output signal *V*out.

As the lower FET conducts it changes the upper FET's source voltage, and the upper FET conducts due to the changed potential between its gate and source.

The major advantage of this circuit arrangement stems from the placement of the upper field-effect transistor (FET) as the load of the input (lower) FET's output terminal (drain). Because at operating frequencies the upper FET's gate is effectively grounded, the upper FET's source voltage (and therefore the input transistor's drain) is held at nearly constant voltage during operation. In other words, the upper FET exhibits a low input resistance to the lower FET, making the voltage gain of the lower FET very small, which dramatically reduces the Miller effect feedback capacitance from the lower FET's drain to gate. This loss of voltage gain is recovered by the upper FET. Thus, the upper transistor permits the lower FET to operate with minimal negative (Miller) feedback, improving its bandwidth.

The upper FET gate is electrically grounded, so charge and discharge of the stray capacitance, *C*dg, between drain and gate is simply through *R*D and the output load (say *R*out), and the frequency response is affected only for frequencies above the associated RC time constant *τ* = *C*dg *R*D//*R*out, namely *f* = 1/(2*πτ*), a rather high frequency because *C*dg is small. That is, the upper FET gate does not suffer from Miller amplification of *C*dg.

If the upper FET stage were operated alone using its source as input node (that is, common-gate (CG) configuration), it would have a good voltage gain and wide bandwidth. However, its low input impedance would limit its usefulness to very low-impedance voltage drivers. Adding the lower FET results in a high input impedance, allowing the cascode stage to be driven by a high-impedance source.

If one were to replace the upper FET with a typical inductive/resistive load and take the output from the input transistor's drain (that is, a common-source (CS) configuration), the CS configuration would offer the same input impedance as the cascode, but the cascode configuration would offer a potentially greater gain and much greater bandwidth.

### Stability

The cascode arrangement is also very stable. Its output is effectively isolated from the input both electrically and physically. The lower transistor has nearly constant voltage at both drain and source, and thus there is essentially "nothing" to feed back into its gate. The upper transistor has nearly constant voltage at its gate and source. Thus, the only nodes with significant voltage on them are the input and output, and these are separated by the central connection of nearly constant voltage and by the physical distance of two transistors. Thus in practice there is little feedback from the output to the input. Metal shielding is both effective and easy to provide between the two transistors for even greater isolation when required. This would be difficult in one-transistor amplifier circuits, which at high frequencies would require neutralization.

### Biasing

As shown, the cascode circuit using two "stacked" FETs imposes some restrictions on the two FETs – namely, the upper FET must be biased so its source voltage is high enough (the lower FET drain voltage may swing too low, causing it to saturate). Ensurance of this condition for FETs requires careful selection for the pair or special biasing of the upper FET gate, increasing cost.

The cascode circuit can also be built using bipolar transistors, or MOSFETs, or even one FET (or MOSFET) and one BJT. This circuit arrangement was very common in VHF television tuners when they employed vacuum tubes.

### Advantages

The cascode arrangement offers high gain, high bandwidth, high slew rate, high stability, and high input impedance. As a two-transistor circuit, the parts count is very low.

### Disadvantages

The cascode circuit requires two transistors and requires a relatively high supply voltage. For the two-FET cascode, both transistors must be biased with ample *V*DS in operation, imposing a lower limit on the supply voltage.

### Dual-gate version

A dual-gate MOSFET often functions as a "one-transistor" cascode. Common in the front ends of sensitive VHF receivers, a dual-gate MOSFET is operated as a common-source amplifier with the primary gate (usually designated "gate 1" by MOSFET manufacturers) connected to the input and the second gate grounded (bypassed). Internally, there is one channel covered by the two adjacent gates; therefore, the resulting circuit is electrically a cascode composed of two FETs, the common lower-drain-to-upper-source connection merely being that portion of the single channel that lies physically adjacent to the border between the two gates.

### Mixer in superheterodyne receivers

A cascode circuit is very useful as a multiplying mixer circuit in superheterodyne receivers. At the lower gate the RF signal is fed to the mixer, and at the upper gate the local oscillator signal is fed to the mixer. Both signals are multiplied by the mixer, and the difference frequency, the intermediate frequency, is taken from the upper drain of the cascode mixer.

This was further developed by cascoding whole differential-amplifier stages to form the balanced mixer, and then the *Gilbert cell* double-balanced mixer.

## Other applications

With the rise of integrated circuits, transistors have become cheap in terms of silicon die area. In MOSFET technology especially, cascoding can be used in current mirrors to increase the output impedance of the output current source.

A modified version of the cascode can also be used as a modulator, particularly for amplitude modulation. The upper device supplies the audio signal, and the lower is the RF amplifier device.

A cascode may also be combined with a voltage ladder to form a high-voltage transistor. The input transistor may be of any low-*U*CEO type, while the others, acting as stacked linear series voltage regulators, should be able to withstand a considerable fraction of the supply voltage. Note that for a large output-voltage swing, their base voltages should *not* be bypassed to ground by capacitors, and the uppermost ladder resistor should be able to withstand the full supply voltage. This shows that a linear series voltage regulator is actually a current buffer with its *input* and *output* designations swapped.

## Two-port parameters

The cascode configuration can be represented as a simple voltage amplifier (or more accurately, as a *g*-parameter two-port network) by using its input impedance, output impedance, and voltage gain. These parameters are related to the corresponding *g*-parameters below. Other useful properties not considered here are circuit bandwidth and dynamic range.

### BJT cascode: low-frequency small-signal parameters

The idealized small-signal equivalent circuit can be constructed for the circuit in figure 2 by replacing the current sources with open circuits and the capacitors with short circuits, assuming they are large enough to act as short circuits at the frequencies of interest. The BJTs can be represented in the small-signal circuit by the hybrid-π model.

|   | Definition | Expression |
|---|---|---|
| **Voltage gain** | $A_{\text{v}}=g_{21}=\left.{\frac {v_{\text{out}}}{v_{\text{in}}}}\right\|_{i_{\text{out}}=0}$ | $-g_{m2}(r_{\pi 1}\|\|r_{{\text{O}}2})(g_{m1}r_{{\text{O}}1}+1)$ |
| **Input resistance** | $R_{\text{in}}={\frac {1}{g_{11}}}=\left.{\frac {v_{\text{in}}}{i_{\text{in}}}}\right\|_{i_{\text{out}}=0}$ | $r_{\pi 2}$ |
| **Output resistance** | $R_{\text{out}}=g_{22}=\left.{\frac {v_{\text{out}}}{i_{\text{out}}}}\right\|_{v_{\text{in}}=0}$ | $r_{{\text{O}}1}+(g_{m1}r_{{\text{O}}1}+1)(r_{\pi 1}\|\|r_{{\text{O}}2})$ |

### MOSFET cascode: low-frequency small-signal parameters

Similarly, the small-signal parameters can be derived for the MOSFET version, also replacing the MOSFET by its hybrid-π model equivalent. This derivation can be simplified by noting that the MOSFET gate current is zero, so the small-signal model for the BJT becomes that of the MOSFET in the limit of zero base current:

$I_{\text{B}}\to 0\Rightarrow r_{\pi }={\frac {V_{\text{T}}}{I_{\text{B}}}}\to \infty ,$

where *V*T is the thermal voltage.

|   | Definition | Expression |
|---|---|---|
| **Voltage gain** | $A_{\text{v}}=g_{21}={\begin{matrix}{v_{\text{out}} \over v_{\text{in}}}\end{matrix}}{\Big \|}_{i_{\text{out}}=0}$ | ${-(g_{\text{m1}}r_{\text{O1}}+1)g_{\text{m2}}r_{\mathrm {O2} }}$ |
| **Input resistance** | $R_{\mathrm {in} }={\begin{matrix}{\frac {1}{g_{11}}}\end{matrix}}={\begin{matrix}{\frac {v_{\text{in}}}{i_{\text{in}}}}\end{matrix}}{\Big \|}_{i_{\text{out}}=0}$ | $\infty$ |
| **Output resistance** | $R_{\text{out}}=g_{22}={\begin{matrix}{\frac {v_{\text{out}}}{i_{\text{out}}}}\end{matrix}}{\Big \|}_{v_{\text{in}}=0}$ | $\left(r_{\mathrm {O1} }+r_{\mathrm {O2} }\right)\left(1+g_{\mathrm {m1} }(r_{\mathrm {O1} }\|\|r_{\mathrm {O2} })\right)$ |

The combination of factors *g*m*r*O occurs often in the above formulas, inviting further examination. For the bipolar transistor this product is (see hybrid-pi model):

$g_{\text{m}}r_{\text{O}}={\frac {I_{\text{C}}}{V_{\text{T}}}}{\frac {V_{\text{A}}+V_{\text{CE}}}{I_{\text{C}}}}={\frac {V_{\text{A}}+V_{\text{CE}}}{V_{\text{T}}}}.$

In a typical discrete bipolar device the Early voltage *V*A ≈ 100 V and the thermal voltage near room temperature is *V*T ≈ 25 mV, making *g*m*r*O ≈ 4000, a rather large number.

From the article on hybrid-pi model, we find for the MOSFET in the active mode:

$g_{\text{m}}r_{\text{O}}={\frac {2I_{\text{D}}}{V_{\text{GS}}-V_{\text{th}}}}{\frac {1/\lambda +V_{\text{DS}}}{I_{\text{D}}}}={\frac {2(1/\lambda +V_{\text{DS}})}{V_{\text{GS}}-V_{\text{th}}}}.$

At the 65-nanometer technology node, *I*D ≈ 1.2 mA/μ of width, supply voltage is *V*DD = 1.1 V; *V*th ≈ 165 mV, and *V*ov = *V*GS − *V*th ≈ 5%VDD ≈ 55 mV. Taking a typical length as twice the minimum, *L* = 2 *L*min = 0.130 μm and a typical value of *λ* ≈ 1/(4 V/μm *L*), we find 1/*λ* ≈ 2 V, and *g*m*r*O ≈ 110, still a large value. The point is that because *g*m*r*O is large almost regardless of the technology, the tabulated gain and the output resistance for both the MOSFET and the bipolar cascode are very large. That fact has implications in the discussion that follows.

### Low-frequency design

The g-parameters found in the above formulas can be used to construct a small-signal voltage amplifier with the same gain, input and output resistance as the original cascode (an equivalent circuit). This circuit applies only at frequencies low enough that the transistor parasitic capacitances do not matter. The figure shows the original cascode (Fig. 1) and the equivalent voltage amplifier or g-equivalent two-port (Fig. 4). The equivalent circuit allows easier calculations of the behavior of the circuit for different drivers and loads. In the figure a Thévenin equivalent voltage source with Thévenin resistance *R*S drives the amplifier, and at the output a simple load resistor *R*L is attached. Using the equivalent circuit, the input voltage to the amplifier is (see *Voltage divider*):

${\upsilon }_{\text{in}}={\upsilon }_{\text{s}}{\begin{matrix}{\frac {R_{\text{in}}}{R_{\text{S}}+R_{\text{in}}}}\end{matrix}}$

,

which shows the importance of using a driver with resistance *R*S << *R*in to avoid attenuation of the signal entering the amplifier. From the above amplifier characteristics, we see that *R*in is infinite for the MOSFET cascode, so no attenuation of input signal occurs in that case. The BJT cascode is more restrictive because *R*in = *r*π2.

In a similar fashion, the output signal from the equivalent circuit is

${\upsilon }_{\text{out}}=A_{\text{v}}\ {\upsilon }_{\text{in}}{\begin{matrix}{\frac {R_{\text{L}}}{R_{\text{L}}+R_{\text{out}}}}\end{matrix}}$

.

In low-frequency circuits, a high voltage gain is typically desired, hence the importance of using a load with resistance *R*L >> *R*out to avoid attenuation of the signal reaching the load. The formulas for *Rout* can be used either to design an amplifier with a sufficiently small output resistance compared to the load or, if that cannot be done, to decide upon a modified circuit, for example, to add a voltage follower that matches the load better.

The earlier estimate showed that the cascode output resistance is very large. The implication is that many load resistances will not satisfy the condition *R*L >> *R*out (an important exception is driving a MOSFET as the load, which has infinite low frequency input impedance). However, the failure to satisfy the condition *R*L >> *R*out is not catastrophic because the cascode gain also is very large. If the designer is willing, the large gain can be sacrificed to allow a low load resistance; for *R*L << *R*out the gain simplifies as follows:

${\upsilon }_{\text{out}}=A_{\text{v}}\ {\upsilon }_{\text{in}}{\begin{matrix}{\frac {R_{\text{L}}}{R_{\text{L}}+R_{\text{out}}}}\approx A_{\text{v}}\ {\upsilon }_{\text{in}}{\frac {R_{\text{L}}}{R_{\text{out}}}}={\frac {A_{\text{v}}}{R_{\text{out}}}}\ {\upsilon }_{\text{in}}R_{\text{L}}\approx -g_{\text{m2}}R_{\text{L}}{\upsilon }_{\text{in}}\end{matrix}}$

.

This gain is the same as that for the input transistor acting alone. Thus, even sacrificing gain, the cascode produces the same gain as the single-transistor transconductance amplifier, but with wider bandwidth.

Because the amplifiers are wide bandwidth, the same approach can determine the bandwidth of the circuit when a load capacitor is attached (with or without a load resistor). The assumption needed is that the load capacitance is large enough that it controls the frequency dependence, and bandwidth is not controlled by the neglected parasitic capacitances of the transistors themselves.

### High-frequency design

At high frequencies, the parasitic capacitances of the transistors (gate-to-drain, gate-to-source, drain-to body, and bipolar equivalents) must be included in the hybrid-π models to obtain an accurate frequency response. The design goals also differ from the emphasis on overall high gain as described above for low-frequency design. In high frequency circuits, impedance matching at the input and output of the amplifier is typically desired in order to eliminate signal reflections and maximize power gain. In the cascode, the isolation between the input and output ports is still characterized by a small reverse transmission term *g*12, making it easier to design matching networks because the amplifier is approximately unilateral.

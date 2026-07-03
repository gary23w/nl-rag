---
title: "Common emitter"
source: https://en.wikipedia.org/wiki/Common_emitter
domain: decoupling-electronics
license: CC-BY-SA-4.0
tags: decoupling electronics
fetched: 2026-07-03
---

# Common emitter

In electronics, a **common-emitter** amplifier is one of three basic single-stage bipolar-junction-transistor (BJT) amplifier topologies, typically used as a voltage amplifier. It offers high current gain (typically 200), medium input resistance and a high output resistance. The output of a common emitter amplifier is inverted; i.e. for a sine wave input signal, the output signal is 180 degrees out of phase with respect to the input.

In this circuit, the base terminal of the transistor serves as the input, the collector is the output, and the emitter is *common* to both (for example, it may be tied to ground reference or a power supply rail), hence its name. The analogous FET circuit is the common-source amplifier, and the analogous tube circuit is the common-cathode amplifier.

## Emitter degeneration

Common-emitter amplifiers give the amplifier an inverted output and can have a very high gain that may vary widely from one transistor to the next. The gain is a strong function of both temperature and bias current, and so the actual gain is somewhat unpredictable. Stability is another problem associated with such high-gain circuits due to any unintentional positive feedback that may be present.

Other problems associated with the circuit are the low input dynamic range imposed by the small-signal limit; there is high distortion if this limit is exceeded and the transistor ceases to behave like its small-signal model. One common way of alleviating these issues is with *emitter degeneration*. This refers to the addition of a small resistor between the emitter and the common signal source (e.g., the ground reference or a power supply rail). This impedance $R_{\text{E}}$ reduces the overall transconductance $G_{m}=g_{m}$ of the circuit by a factor of $g_{m}R_{\text{E}}+1$ , which makes the voltage gain

$A_{\text{v}}\triangleq {\frac {v_{\text{out}}}{v_{\text{in}}}}={\frac {-g_{m}R_{\text{C}}}{g_{m}R_{\text{E}}+1}}\approx -{\frac {R_{\text{C}}}{R_{\text{E}}}},$

where $g_{m}R_{\text{E}}\gg 1$ .

The voltage gain depends almost exclusively on the ratio of the resistors $R_{\text{C}}/R_{\text{E}}$ rather than the transistor's intrinsic and unpredictable characteristics. The distortion and stability characteristics of the circuit are thus improved at the expense of a reduction in gain.

(While this is often described as "negative feedback", as it reduces gain, raises input impedance, and reduces distortion, it predates the invention of the negative feedback amplifier and does not reduce output impedance or increase bandwidth, as a true negative feedback amplifier would do.)

## Characteristics

At low frequencies and using a simplified hybrid-pi model, the following small-signal characteristics can be derived.

|   | Definition | Expression |   |
|---|---|---|---|
| With emitter degeneration | Without emitter degeneration; i.e., *R*E = 0 |   |   |
| **Current gain** | $A_{\text{i}}\triangleq {\frac {i_{\text{out}}}{i_{\text{in}}}}\,$ | $\beta \,$ | $\beta$ |
| **Voltage gain** | $A_{\text{v}}\triangleq {\frac {v_{\text{out}}}{v_{\text{in}}}}\,$ | $-{\frac {\beta R_{\text{C}}}{r_{\pi }+(\beta +1)R_{\text{E}}}}\,$ | $-g_{m}R_{\text{C}}$ |
| **Input impedance** | $r_{\text{in}}\triangleq {\frac {v_{\text{in}}}{i_{\text{in}}}}\,$ | $r_{\pi }+(\beta +1)R_{\text{E}}\,$ | $r_{\pi }$ |
| **Output impedance** | $r_{\text{out}}\triangleq {\frac {v_{\text{out}}}{i_{\text{out}}}}\,$ | $R_{\text{C}}\,$ | $R_{\text{C}}$ |

If the emitter degeneration resistor is not present, then $R_{\text{E}}=0\,\Omega$ , and the expressions effectively simplify to the ones given by the rightmost column (note that the voltage gain is an ideal value; the actual gain is somewhat unpredictable). As expected, when *$R_{\text{E}}\,$* is increased, the input impedance is increased and the voltage gain $A_{\text{v}}\,$ is reduced.

### Bandwidth

The bandwidth of the common-emitter amplifier tends to be low due to high capacitance resulting from the Miller effect. The parasitic base-collector capacitance $C_{\text{CB}}\,$ appears like a larger parasitic capacitor $C_{\text{CB}}(1-A_{\text{v}})\,$ (where $A_{\text{v}}\,$ is negative) from the base to ground. This large capacitor greatly decreases the bandwidth of the amplifier as it makes the time constant of the parasitic input RC filter $r_{\text{s}}(1-A_{\text{V}})C_{\text{CB}}\,$ where $r_{\text{s}}\,$ is the output impedance of the signal source connected to the ideal base.

The problem can be mitigated in several ways, including:

- Reduction of the voltage gain magnitude $\left|A_{\text{v}}\right|\,$ (e.g., by using emitter degeneration).
- Reduction of the output impedance $r_{\text{s}}\,$ of the signal source connected to the base (e.g., by using an emitter follower or some other voltage follower).
- Using a cascode configuration, which inserts a low input impedance current buffer (e.g. a common base amplifier) between the transistor's collector and the load. This configuration holds the transistor's collector voltage roughly constant, thus making the base to collector gain zero and hence (ideally) removing the Miller effect.
- Using a differential amplifier topology like an emitter follower driving a grounded-base amplifier; as long as the emitter follower is truly a common-collector amplifier, the Miller effect is removed.

The Miller effect negatively affects the performance of the common source amplifier in the same way (and has similar solutions). When an AC signal is applied to the transistor amplifier it causes the base voltage VB to fluctuate in value at the AC signal. The positive half of the applied signal will cause an increase in the value of VB this turn will increase the base current IB and cause a corresponding increase in emitter current IE and collector current IC. As a result, the collector emitter voltage will be reduced because of the increase voltage drop across RL. The negative alternation of an AC signal will cause a decrease in IB this action then causes a corresponding decrease in IE through RL.

It is also named common-emitter amplifier because the emitter of the transistor is common to both the input circuit and output circuit. The input signal is applied across the ground and the base circuit of the transistor. The output signal appears across ground and the collector of the transistor. Since the emitter is connected to the ground, it is common to signals, input and output.

The common-emitter circuit is the most widely used of junction transistor amplifiers. As compared with the common-base connection, it has higher input impedance and lower output impedance. A single power supply is easily used for biasing. In addition, higher voltage and power gains are usually obtained for common-emitter (CE) operation.

Current gain in the common emitter circuit is obtained from the base and the collector circuit currents. Because a very small change in base current produces a large change in collector current, the current gain (β) is always greater than unity for the common-emitter circuit, a typical value is about 50.

## Applications

### Low-frequency voltage amplifier

A typical example of the use of a common-emitter amplifier is shown in Figure 3.

The input capacitor C removes any DC component of the input, and the resistors R1 and R2 bias the transistor so that it will remain in active mode for the entire range of the input. The output is an inverted copy of the AC component of the input that has been amplified by the ratio *R*C/*R*E and shifted by an amount determined by all four resistors. Because *R*C is often large, the output impedance of this circuit can be prohibitively high. To alleviate this problem, *R*C is kept as low as possible and the amplifier is followed by a voltage buffer like an emitter follower.

### Radio

Common-emitter amplifiers are also used in radio frequency circuits, for example to amplify faint signals received by an antenna. In this case it is common to replace the load resistor with a tuned circuit. This may be done to limit the bandwidth to a narrow band centered around the intended operating frequency. More importantly it also allows the circuit to operate at higher frequencies as the tuned circuit can be used to resonate any inter-electrode and stray capacitances, which normally limit the frequency response. Common emitters are also commonly used as low-noise amplifiers.

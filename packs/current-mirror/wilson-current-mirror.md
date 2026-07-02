---
title: "Wilson current mirror"
source: https://en.wikipedia.org/wiki/Wilson_current_mirror
domain: current-mirror
license: CC-BY-SA-4.0
tags: current mirror, Wilson current mirror, cascode stage, output impedance
fetched: 2026-07-02
---

# Wilson current mirror

A **Wilson current mirror** is a three-terminal circuit (Fig. 1) that accepts an input current at the input terminal and provides a "mirrored" current source or sink output at the output terminal. The mirrored current is a precise copy of the input current.

It may be used as a **Wilson current source** by applying a constant bias current to the input branch as in Fig. 2. The circuit is named after George R. Wilson, an integrated circuit design engineer who worked for Tektronix. Wilson devised this configuration in 1967 when he and Barrie Gilbert challenged each other to find an improved current mirror overnight that would use only three transistors. Wilson won the challenge.

## Circuit operation

There are three principal metrics of how well a current mirror will perform as part of a larger circuit.

- The first measure is the static error, i.e., the difference between the input and output currents expressed as a fraction of the input current. Minimizing this difference is critical in such applications of a current mirror as the differential to single-ended output signal conversion in a differential amplifier stage because this difference controls the common mode and power supply rejection ratios.
- The second measure is the output impedance of the current source or equivalently its inverse, the output conductance. This impedance affects stage gain when a current source is used as an active load and affects common mode gain when the source provides the tail current of a differential pair
- The last metric is the pair of minimum voltages from the common terminal, usually a power rail connection, to the input and output terminals that are required for proper operation of the circuit. These voltages affect the headroom to the power supply rails that are available for the circuitry in which the current mirror is embedded.

An approximate analysis due to Gilbert shows how the Wilson current mirror works and why its static error should be very low. Transistors Q1 and Q2 in Fig. 1 are a matched pair sharing the same emitter and base potentials and therefore have $\scriptstyle i_{C1}~=~i_{C2}$ and $\scriptstyle i_{B1}~=~i_{B2}$ . This is a simple two-transistor current mirror with $\scriptstyle i_{E3}$ as its input and $\scriptstyle i_{C1}$ as its output. When a current $\scriptstyle i_{\text{in}}$ is applied to the input node (the connection between the base of Q3 and collector of Q1), the voltage from that node to ground begins to increase. As it exceeds the voltage required to bias the emitter-base junction of Q3, Q3 acts as an emitter follower or common collector amplifier and the base voltage of Q1 and Q2 begins to rise. As this base voltage increases, current begins to flow in the collector of Q1. All increases in voltage and current stop when the sum of the collector current of Q1 and base current of Q3 exactly balance $\scriptstyle i_{\text{in}}$ . Under this condition all three transistors have nearly equal collector currents and therefore approximately equal base currents. Let $\scriptstyle i_{B}~=~i_{B1}~=~i_{B2}~\approx ~i_{B3}$ . Then the collector current of Q1 is $\scriptstyle i_{\text{in}}\,-\,i_{B}$ ; the collector current of Q2 is exactly equal to that of Q1 so the emitter current of Q3 is $\scriptstyle i_{E3}~=~i_{C2}\,+\,2i_{B}~=~i_{\text{in}}\,-\,i_{B}\,+\,2i_{B}~=~i_{\text{in}}\,+\,i_{B}$ . The collector current of Q3 is its emitter current minus the base current so $\scriptstyle i_{\text{out}}~=~i_{\text{in}}\,+\,i_{B}\,-\,i_{B}~=~i_{\text{in}}$ . In this approximation, the static error is zero.

### Difference of input and output currents

A more exact formal analysis shows the expected static error. We assume:

1. All transistors have the same current gain β.
2. Q1 and Q2 are matched, and they share the same base-emitter voltage, so their collector currents are equal.

Therefore, $\scriptstyle i_{C1}~=~i_{C2}~\equiv ~i_{C}$ and $\scriptstyle i_{B1}~=~i_{B2}~\equiv ~i_{B}$ . The base current of Q3 is given by, $\scriptstyle i_{B3}~=~{\frac {i_{C3}}{\beta }}$ and the emitter current by,

$i_{E3}={\frac {\beta +1}{\beta }}i_{C3}$

... (1)

From the sum of currents at the node shared by the emitter of Q3, the collector of Q2 and the bases of Q1 and Q2, the emitter current of Q3 must be:

$i_{E3}=i_{C2}+i_{B1}+i_{B2}=i_{C}+2i_{B}={\frac {\beta +2}{\beta }}i_{C}$

... (2)

Equating the expressions for $\scriptstyle i_{E3}$ in (1) and (2) gives:

$i_{C}=\left({\frac {\beta +1}{\beta +2}}\right)i_{C3}$

... (3)

The sum of currents at the input node implies that $\scriptstyle i_{\text{in}}~=~i_{C1}\,+\,i_{B3}~=~i_{C}\,+\,{\frac {i_{C3}}{\beta }}$ . Substituting for $\scriptstyle i_{C}$ from (3) leads to: $\scriptstyle i_{\text{in}}~=~\left({\frac {\beta \,+\,1}{\beta \,+\,2}}\,+\,{\frac {1}{\beta }}\right)i_{C3}$ or $\scriptstyle i_{C3}~=~\left({\frac {\beta \left(\beta \,+\,2\right)}{\beta \left(\beta \,+\,2\right)\,+\,2}}\right)i_{\text{in}}$ .

Because $\scriptstyle i_{C3}$ is the output current, the static error, the difference between the input and output currents, is:

$i_{\text{in}}-i_{\text{out}}={\frac {2i_{\text{in}}}{\beta \left(\beta +2\right)+2}}\approx {\frac {2i_{\text{in}}}{\beta ^{2}}}$

... (4)

With NPN transistors, the current gain, $\scriptstyle \beta$ , is of the order of 100, and, in principle, the mismatch is about 1:5000.

For the Wilson current source of Fig. 2, the input current of the mirror is $\scriptstyle I_{R1}~=~{\frac {1}{R1}}\left(V_{CC}\,-\,V_{BE2}\,-\,V_{BE3}\right)$ . The base-emitter voltages, $\scriptstyle V_{BE}$ , are typically between 0.5 and 0.75 volts so some authors approximate this result as $\scriptstyle I_{\text{out}}\approx {\frac {V_{CC}\,-\,1.4\ V}{R1}}$ . The output current is thus substantially dependent only on VCC and R1 and the circuit acts as a constant current source, that is, the current remains constant with variations in the impedance of the load. However, variations in VCC or changes in the value of R1 due to temperature will be reflected in variations in the output current. This method of direct generation of a reference current from the power supply using a resistor rarely has adequate stability for practical applications and more complex circuits are used to provide reference currents independent of temperature and supply voltages.

Equation (4) substantially underestimates the differences between the input and output currents that are generally found in this circuit for three reasons. First, the emitter-collector voltages of the inner current mirror formed by Q1 and Q2 are not the same. Transistor Q2 is diode-connected and has $\scriptstyle v_{CE2}~=~v_{BE2}$ , which is typically on the order of 0.6 to 0.7 volts. The collector emitter voltage of Q1 is higher by the base-emitter voltage of Q3 and therefore is about twice the value across Q2. The Early effect (base-width modulation) in Q1 will force its collector current to be slightly higher than that of Q2. This problem can be essentially eliminated by the addition of a fourth transistor, shown as Q4 in the improved Wilson current mirror of Fig. 4a. Q4 is diode-connected in series with the collector of Q1, lowering its collector voltage until it is approximately equal to $\scriptstyle v_{CE}$ for Q2.

Second, the Wilson current mirror is susceptible to mismatches in the current gain, $\scriptstyle \beta$ , of its transistors, particularly the match between $\scriptstyle \beta _{3}$ and the current gains of the matched pair Q1 and Q2. Accounting for $\scriptstyle \beta$ differences among all three transistors, one can show that $\scriptstyle i_{\text{in}}\,-\,i_{\text{out}}~=~{\frac {2\left({\overline {\beta _{12}}}\,-\,\beta _{3}\right)\,+\,2}{{\overline {\beta _{12}}}\beta _{3}\,+\,2{\overline {\beta _{12}}}\,+\,2}}$ where $\scriptstyle {\overline {\beta _{12}}}$ is the harmonic mean of the current gains of Q1 and Q2 or $\scriptstyle {\overline {\beta _{12}}}~=~2\left[{\frac {1}{\beta _{1}}}\,+\,{\frac {1}{\beta _{2}}}\right]^{-1}$ . Beta mismatches of five percent or more are reported to be common, causing an order of magnitude increase in the static error.

Finally, the collector current in a bipolar transistor for low and moderate emitter currents conforms closely to the relation $\scriptstyle i_{C}~=~I_{SC}\exp \left({\frac {v_{BE}}{V_{T}}}\right)$ where $\scriptstyle V_{T}~=~{\frac {kT}{q}}$ is the thermal voltage and $\scriptstyle I_{SC}$ is a constant dependent on temperature, doping concentrations, and collector-emitter voltage. Matched currents in transistors Q1 and Q2 depend on conformity to the same equation but observed mismatches in $\scriptstyle I_{SC}$ are geometry dependent and range from $\scriptstyle \pm 1{\text{ to }}\pm 10$ percent. Such differences between Q1 and Q2 lead directly to static errors of the same percentage for the entire mirror. Careful layout and transistor design must be used to minimize this source of error. For example, Q1 and Q2 may each be implemented as a pair of paralleled transistors arranged as a cross-coupled quad in a common-centric layout to reduce effects of local gradients in current gain. If the mirror is to be used at a fixed bias level, matching resistors in the emitters of this pair can transfer some of the matching problem from the transistors to those resistors.

### Input and output impedances and frequency response

A circuit is a current source only to the extent that its output current is independent of its output voltage. In the circuits of Fig. 1 and Fig. 2, the output voltage of importance is the potential from the collector of Q3 to ground. The measure of that independence is the output impedance of the circuit, the ratio of a change in output voltage to the change in current it causes. Fig. 3 shows a small signal model of a Wilson current mirror drawn with a test voltage source, $\scriptstyle v_{\text{test}}$ , attached to the output. The output impedance is the ratio: $\scriptstyle z_{\text{out}}~\equiv ~{\frac {v_{\text{test}}}{i_{\text{test}}}}$ . At low frequency this ratio is real and represents an output resistance.

In Fig. 3, transistors Q1 and Q2 are shown as forming a standard two-transistor current mirror. It is sufficient for calculating the output impedance to assume that the output current of this current mirror sub-circuit, $\scriptstyle i_{c1}$ , is equal to the input current, $\scriptstyle i_{e3}$ , or $\scriptstyle i_{c1}~\approx ~i_{e3}$ . Transistor Q3 is represented by its low-frequency hybrid-pi model with a current controlled dependent current source for the collector current.

The sum of currents at the emitter node of Q3 implies that:

$i_{\text{test}}=i_{e3}+i_{c1}=2i_{c1}{\text{ or }}i_{c1}={\frac {1}{2}}i_{\text{test}}$

... (5)

Because the dynamic resistance of the diode-connected transistor Q2, the input resistance of the two-transistor current mirror, is much smaller than $\scriptstyle r_{O3}$ , the test voltage, $\scriptstyle v_{\text{test}}$ , effectively appears across the collector-emitter terminals of Q3. The base current of Q3 is $\scriptstyle i_{b3}~=~-i_{c1}$ . Using equation (5) for $\scriptstyle i_{c1}$ , the sum of currents at the collector node of Q3 becomes $\scriptstyle i_{\text{test}}~=~{\frac {v_{\text{test}}}{r_{O3}}}\,-\,{\frac {\beta }{2}}i_{\text{test}}$ . Solving for the output impedance gives:

$z_{\text{out}}={\frac {v_{\text{test}}}{i_{\text{test}}}}=\left(1+{\frac {\beta }{2}}\right)r_{O3}\approx {\frac {\beta }{2}}r_{O3}$

... (6)

In a standard two-transistor current mirror, the output impedance would be the dynamic early resistance of the output transistor, the equivalent of which in this case is $\scriptstyle r_{O3}$ . The Wilson current mirror has an output impedance that is higher by the factor $\scriptstyle {\frac {\beta }{2}}$ , on the order of 50 times.

The input impedance of a current mirror is the ratio of the change in input voltage (the potential from the input terminal to ground in Fig. 1 and Fig. 2) to the change in input current that causes it. Since the change in output current is very nearly equal to any change in input current, the change in the base-emitter voltage of Q3 is $\scriptstyle \Delta V_{BE3}~=~{\frac {\Delta I_{\text{in}}}{g_{m3}}}$ . Eq. (3) shows that the collector of Q2 changes by nearly the same amount, so $\scriptstyle \Delta V_{BE2}~\approx ~{\frac {\Delta I_{\text{in}}}{g_{m2}}}$ . The input voltage is the sum of the base-emitter voltages of Q2 and Q3; the collector currents of Q2 and Q3 are nearly equal implying that $\scriptstyle g_{m2}~=~g_{m3}$ . The input impedance is $\scriptstyle z_{\text{in}}~=~{\frac {2}{g_{m3}}}$ . Using the standard formula for $\scriptstyle g_{m}~=~{\frac {I_{C}}{V_{T}}}$ leads to:

$z_{\text{in}}={\frac {2kT}{qI_{\text{in}}}}$

... (7)

where $\scriptstyle {\frac {kT}{q}}=V_{T}$ is the usual *thermal voltage*, the product of the Boltzmann constant and absolute temperature divided by the charge of an electron. This impedance is twice the value of $\scriptstyle z_{\text{in}}$ for the standard two-transistor current mirror.

Current mirrors are frequently used in the signal path of an integrated circuit, for example, for differential to single-ended signal conversion within an operational amplifier. At low bias currents, the impedances in the circuit are high enough that the effect of frequency may be dominated by device and parasitic capacitances shunting the input and output nodes to ground, lowering the input and output impedances. The collector-base capacitance, $\scriptstyle C_{\mu 3}$ , of Q3 is one component of that capacitive load. The collector of Q3 is the output node of the mirror and its base is the input node. When any current flows in $\scriptstyle C_{\mu 3}$ , that current becomes an input to the mirror and the current is doubled at the output. Effectively the contribution from Q3 to the total output capacitance is $\scriptstyle 2C_{\mu 3}$ . If the output of the Wilson mirror is connected to a relatively high impedance node, the voltage gain of the mirror may be high. In that case the input impedance of the mirror may be affected by the Miller effect because of $\scriptstyle C_{\mu 3}$ , although the low input impedance of the mirror mitigates this effect.

When the circuit is biased at higher currents that maximize the frequency response of the transistor current gain, it is possible to operate a Wilson current mirror with satisfactory results at frequencies up to approximately one tenth of the transition frequency of the transistors. The transition frequency of a bipolar transistor, $\scriptstyle f_{T}$ , is the frequency at which the short-circuit common-emitter current gain falls to unity. It is effectively the highest frequency for which a transistor may supply useful gain in an amplifier. The transition frequency is a function of the collector current, increasing with increasing current until a broad maximum at a collector current slightly less than what causes the onset of high injection. In simple models of the bipolar transistor when the collector is grounded, $\scriptstyle \beta \left(f\right)$ shows a single-pole frequency response so $\scriptstyle f_{T}$ is also the current gain-bandwidth product. Crudely this implies that at $\scriptstyle {\frac {f_{T}}{10}}$ , $\scriptstyle \beta \left({\frac {f_{T}}{10}}\right)~\approx ~-j10$ . By equation (4) one might expect the magnitude of the ratio of output to input current at that frequency to differ from unity by about 2%.

The Wilson current mirror achieves the high output impedance of equation (6) by negative feedback rather than by emitter degeneration as cascoded mirrors or sources with resistor degeneration do. The node impedance of the only internal node of the mirror, the node at the emitter of Q3 and the collector of Q2, is quite low. At low frequency, that impedance is given by $\scriptstyle {\frac {V_{T}}{\beta I_{\text{in}}}}~=~{\frac {kT}{q\beta I_{\text{in}}}}$ . For a device biased at 1 mA having a current gain of 100, this evaluates to 0.26 ohms at 25 °C. Any change in output current with output voltage results in a change in the emitter current of Q3 but very little change in the emitter node voltage. The change in $\scriptstyle i_{E3}$ is fed back through Q2 and Q1 to the input node where it changes the base current of Q3 in a way that reduces the net change in output current, thus closing the feedback loop.

Circuits that contain negative feedback loops, whether current or voltage loops, with loop gains near or above unity may exhibit undesirable anomalies in frequency response when the phase shift of the signal inside the loop is sufficient to convert negative into positive feedback. For the current feedback loop of the Wilson current mirror this effect appears as a strong broad resonant peak in the ratio of the output to input current, $\scriptstyle H_{WCM}\left(s\right)~\equiv ~{\frac {i_{\text{out}}\left(s\right)}{i_{\text{in}}\left(s\right)}}$ , at about $\scriptstyle {\frac {f_{T}}{3}}$ . Gilbert shows a simulation of a Wilson current mirror implemented in NPN transistors with $\scriptstyle f_{T}~=~3.0$ GHz and current gain $\scriptstyle \beta ~=~100$ that shows a peak of 7.5 dB $\scriptstyle \left(\left|H_{WCM}\left(s\right)\right|~=~2.4\right)$ at 1.2 GHz. This behavior is very undesirable and can be largely eliminated by further modification of the basic mirror circuit. Fig. 4b show a possible variant on the Wilson mirror that reduces this peak by disconnecting the bases of Q1 and Q2 from the collector of Q2 and adding a second emitter to Q3 to drive the bases of the internal mirror. For the same bias conditions and device type, this circuit exhibits flat frequency response to 50 MHz, has a peak response less than 0.7 dB $\scriptstyle \left(\left|H_{WCM}\left(s\right)\right|~=~1.08\right)$ at 160 MHz and falls below its low-frequency response at 350 MHz.

### Minimum operating voltages

The compliance of a current source, that is, the range of output voltage over which the output current remains approximately constant, affects the potentials available to bias and operate the circuitry in which the source is embedded. For example, in Fig. 2 the voltage available to the "Load" is the difference between the supply voltage $\scriptstyle V_{CC}$ and the collector voltage of Q3. The collector of Q3 is the output node of the mirror and the potential of that collector relative to ground is the output voltage of the mirror, that is, $\scriptstyle v_{\text{mirror out}}~=~v_{BE2}\,+\,v_{CE3}$ and the "load" voltage is $\scriptstyle V_{CC}\,-\,v_{\text{mirror out}}$ . The "load" voltage range is maximized at the minimum $\scriptstyle v_{\text{mirror out}}$ . Also, when a current mirror source is used as an active load for one stage of a system, the input to the next stage is often directly connected between the source output node and the same power rail as the mirror. This may require that the minimum $\scriptstyle v_{\text{mirror out}}$ be kept as small as possible to simplify biasing the succeeding stage and to make it possible to turn that stage fully off under transient or overdrive conditions.

The minimum output voltage of the Wilson current mirror must exceed the base emitter voltage of Q2 by enough that Q3 will operate in active mode rather than saturation. Gilbert reports data on a representative implementation of a Wilson current mirror that showed constant output current for an output voltage as low as 880 millivolts. Since the circuit was biased for high frequency operation ( $\scriptstyle V_{BE}~\geq ~0.7$ ), this represents a saturation voltage for Q3 of 0.1 to 0.2 volts. By contrast, the standard two-transistor mirror operates down to the saturation voltage of its output transistor.

The input voltage of the Wilson current mirror is $\scriptstyle v_{\text{in}}=v_{BE2}+v_{BE3}$ . The input node is a low impedance node so its voltage remains approximately constant during operation at $\scriptstyle 2V_{BE}\approx 1.4$ volts. The equivalent voltage for the standard two-transistor mirror is only one base-emitter drop, $\scriptstyle V_{BE}$ , or half that of the Wilson mirror. The headroom (the potential difference between the opposite power rail and the input of the mirror) available to the circuitry that generates the input current to the mirror is the difference of the power supply voltage and the mirror input voltage. The higher input voltage and higher minimum output voltage of the Wilson current mirror configuration may become problematic for circuits with low supply voltages, particularly supply voltages less than three volts as are sometimes found in battery powered devices.

## A four-transistor improved mirror

Adding a fourth transistor to the Wilson current mirror as in Fig. 4a equalizes the collector voltages of Q1 and Q2 by lowering the collector voltage of Q1 by an amount equal to VBE4. This has three effects: first, it removes any mismatch between Q1 and Q2 due to the Early effect in Q1. This is the only first order source of mismatch in the three-transistor Wilson current mirror Second, at high currents the current gain, *β*, of transistors decreases and the relation of collector current to base-emitter voltage deviates from $\scriptstyle i_{C}~=~I_{S}\exp \left({\frac {v_{BE}}{V_{T}}}\right)$ . The severity of these effects depends on the collector voltage. By forcing a match between the collector voltages of Q1 and Q2, the circuit makes the performance degradation at high current on the input and output branches symmetric. This extends the linear operating range of the circuit substantially. In one reported measurement on a circuit implemented with a transistor array for an application requiring 10 mA output, the addition of the fourth transistor extended the operating current for which the circuit showed less than 1% difference between input and output currents by at least a factor of two over the three transistor version.

Finally, equalizing the collector voltages also equalizes the power dissipated in Q1 and Q2 and that tends to reduce mismatch from the effects of temperature on VBE.

## Advantages and limitations

There are a number of other possible current mirror configurations in addition to the standard two-transistor mirror that a designer may choose to use. These include ones in which the mismatch from base current are reduced with an emitter follower, circuits that use cascoded structures or resistor degeneration to lower the static error and raise output impedance, and gain-boosted current mirrors that use an internal error amplifier to improve the effectiveness of cascoding. The Wilson current mirror has the particular advantages over alternatives that:

- The static error, the input-output current difference, is reduced to very small levels attributable almost entirely to random device mismatches while the output impedance is raised by a factor of $\scriptstyle {\frac {\beta }{2}}$ simultaneously.
- The circuit uses minimum resources. It does not require additional bias voltages or large area resistors as do cascoded or resistively degenerated mirrors.
- The low impedance of its input and internal nodes makes it possible to bias the circuit for operation at frequencies up to $\scriptstyle {\frac {f_{T}}{10}}$ .
- The four-transistor version of the circuit has extended linearity for operation at high currents.

The Wilson current mirror has the limitations that:

- The minimum potentials from input or output to the common rail connection that are needed for proper operation are higher than for the standard two-transistor mirror. This reduces the headroom available to generate the input current and limits the compliance of the output.
- This mirror uses feedback to raise the output impedance in such a way that the output transistor contributes collector current fluctuation noise to the output. All three transistors of the Wilson current mirror add noise to the output.
- When the circuit is biased for high frequency operation with maximum $\scriptstyle f_{T}$ , the negative feedback loop that maximizes the output impedance may cause peaking in the frequency response of the mirror. For stable, low-noise operation it may be necessary to modify the circuit to eliminate this effect.
- In some applications of a current mirror, particularly for biasing and active load applications, it is advantageous to produce multiple current sources from a single input reference current. This is not possible in the Wilson configuration while maintaining an accurate match of the input current to the output currents.

## MOSFET implementation

When the Wilson current mirror is used in CMOS circuits, it is usually in the four transistor form as in Fig. 5. If the transistor pairs M1/M2 and M3/M4 are exactly matched and the input and output potentials are approximately equal, then in principle there is no static error, the input and output currents are equal because there is no low frequency or DC current into the gate of a MOSFET. However, there are always mismatches between transistors caused by random lithographic variation in device geometry and by variations in threshold voltage between devices.

For long-channel MOSFETs operating in saturation at fixed drain-source voltage, $\scriptstyle V_{DS}$ , the drain current is proportional to device sizes and to the magnitude of the difference between the gate-source voltage and the device threshold voltage as

$i_{D}\propto {\frac {W}{L}}\left(v_{GS}-V_{TH}\right)^{2}$

... (8)

where $\scriptstyle W$ is the device width, $\scriptstyle L$ is its length and $\scriptstyle V_{TH}$ the device threshold voltage. Random lithographic variations are reflected as different values of the $\scriptstyle {\frac {W}{L}}$ ratio of each transistor. Similarly threshold variations appear as small differences in the value of $\scriptstyle V_{TH}$ for each transistor. Let $\scriptstyle \Delta {\frac {W}{L}}~\equiv ~{\frac {W_{2}}{L_{2}}}\,-\,{\frac {W_{1}}{L_{1}}}$ and $\scriptstyle \Delta V_{TH}~=~V_{TH2}\,-\,V_{TH1}$ . The mirror circuit of Fig. 5 forces the drain current of M1 to equal the input current and the output configuration assures that the output current equals the drain current of M2. Expanding equation (8) in a two-variable Taylor series about $\scriptstyle i_{D1}$ and truncating after the first linear term, leads to an expression for the mismatch of the drain currents of M1 and M2 as:

$i_{\text{in}}\,-\,i_{\text{out}}~=~\left({\frac {2\,\Delta V_{TH}}{V_{GS1}\,-\,V_{TH1}}}\,-\,{\frac {\Delta {\frac {W}{L}}}{\frac {W_{1}}{L_{1}}}}\right)i_{\text{in}}$

... (9)

The statistics of the variation in threshold voltage of matched pairs across a wafer have been studied extensively. The standard deviation of the threshold voltage variation depends on the absolute size of the devices, the minimum feature size of the manufacturing process, and the body voltage and is typically 1 to 3 millivolts. Therefore, to keep the contribution of the threshold voltage term in equation (9) to a percent or less requires biasing the transistors with the gate-source voltage exceeding the threshold by several tenths of a volt. This has the subsidiary effect of lowering the contribution of the mirror transistors to the output current noise because the drain current noise density in a MOSFET is proportional to the transconductance and therefore inversely proportional to $\scriptstyle V_{GS}\,-\,V_{TH}$ .

Similarly, careful layout is required to minimize the effect of the second, geometric term in (9) that is proportional to $\scriptstyle \Delta {\frac {W}{L}}$ . One possibility is to subdivide transistors M1 and M2 into multiple devices in parallel that are arranged in a common-centric or interdigitated layout with or without dummy guard structures on the perimeter.

The output impedance of the MOSFET Wilson current mirror can be calculated in the same way as for the bipolar version. If there is no body effect in M4, the low frequency output impedance is given by $\scriptstyle z_{O}~\approx ~\left(1\,+\,g_{m4}r_{O1}\right)r_{O4}$ . For M4 not to have a body-source potential, it must be implemented in a separate body well. However, the more common practice is for all four transistors to share a common body connection. The drain of M2 is a relatively low impedance node and this limits the body effect. The output impedance in that case is:

$z_{O}\approx \left(2+g_{m4}r_{O1}\right)r_{O4}$

... (10)

As in the case of the bipolar transistor version of this circuit, the output impedance is much larger than it would be for the standard two-transistor current mirror. Since $\scriptstyle r_{O4}$ would be the same as the output impedance of the standard mirror, the ratio of the two is $\scriptstyle 2\,+\,g_{m4}r_{O1}$ , which is often quite large.

The principal limitation on the use of the Wilson current mirror in MOS circuits is the high minimum voltages between the ground connection in Fig. 5 and the input and output nodes that are required for proper operation of all transistors in saturation. The voltage difference between the input node and ground is $\scriptstyle v_{GS1}+v_{GS4}$ . The threshold voltage of MOS devices is usually between 0.4 and 1.0 volts with no body effect depending on the manufacturing technology. Because $\scriptstyle v_{GS}$ must exceed the threshold voltage by a few tenths of a volt to have satisfactory input-output current match, the total input to ground potential is comparable to 2.0 volts. This difference is increased when the transistors share a common body terminal and the body effect in M4 raises its threshold voltage. On the output side of the mirror, the minimum voltage to ground is $\scriptstyle v_{GS2}+v_{GS4}-V_{TH4}$ . This voltage is likely to be significantly greater than 1.0 volts. Both potential differences leave insufficient headroom for the circuitry that provides the input current and uses the output current unless the power supply voltage is higher than 3 volts. Many contemporary integrated circuits are designed to use low voltage power supplies to accommodate the limitations of short-channel transistors, to meet the need for battery operated devices and to have high power efficiency in general. The result is that new designs tend to use some variant of a wide swing cascode current mirror configuration. In the case of extremely low power supply voltages of one volt or less, the use of current mirrors may be abandoned entirely.

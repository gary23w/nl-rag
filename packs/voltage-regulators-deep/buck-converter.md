---
title: "Buck converter"
source: https://en.wikipedia.org/wiki/Buck_converter
domain: voltage-regulators-deep
license: CC-BY-SA-4.0
tags: voltage regulator, linear regulator, low-dropout regulator, switched-mode power supply
fetched: 2026-07-02
---

# Buck converter

A **buck converter** or **step-down converter** is a DC-to-DC converter which decreases voltage, while increasing current, from its input (*supply*) to its output (*load*). It is a class of switched-mode power supply. Switching converters (such as buck converters) provide much greater power efficiency as DC-to-DC converters than linear regulators, which are simpler circuits that dissipate power as heat, but do not step up output current. The efficiency of buck converters can be very high, often over 90%, making them useful for tasks such as converting a computer's main supply voltage, which is usually 12 V, down to lower voltages needed by USB, DRAM and the CPU, which are usually 5, 3.3 or 1.8 V.

Buck converters typically contain at least two semiconductors (a diode and a transistor, although modern buck converters frequently replace the diode with a second transistor used for synchronous rectification) and at least an inductor as energy storage element, usually in combination with a capacitor. To reduce voltage ripple, filters made of capacitors (sometimes in combination with additional inductors) are normally added to such a converter's output (load-side filter) and input (supply-side filter). Its name derives from the inductor that “bucks” or opposes the supply voltage.

Buck converters typically operate with a switching frequency range from 100 kHz to a few MHz. A higher switching frequency allows for use of smaller inductors and capacitors, but also increases lost efficiency to more frequent transistor switching.

## Theory

The basic concept of a buck converter is:

1. Use the higher-than-needed voltage of the source to quickly induce a current into an inductor ("on" in fig. 2 and 4).
2. Disconnect the source and use the inertia of the current in the inductor to provide more current than the source delivers ("off" in fig. 2 and 4). To close the circuit with the source disconnected, a second switch, usually a diode, is needed.

During on-state, the source may need to momentarily provide more current than its rating for constant load allows, but the on-time is too short for the source to take damage. During off-state, no current is drawn from the source, and the components can cool down. The average current draw over both states needs to be below the source specification.

To even out voltage spikes from the switching between on-state and off-state, a capacitor is used on the output side.

A mechanical analogy for a buck converter would be to pedal a bicycle in single, strong bursts (force ~ voltage), and let the bicycle roll in between (inertia ~ inductor).

The basic operation of the buck converter has the current in an inductor controlled by two switches (fig. 2). In a physical implementation, these switches are realized by a transistor and a diode, or two transistors (which avoids the loss associated with the diode's voltage drop).

### Idealised case

The conceptual model of the buck converter is best understood in terms of the relation between current and voltage of the inductor. Beginning with the switch open (off-state), the current in the circuit is zero. When the switch is first closed (on-state), the current will begin to increase, and the inductor will produce an opposing voltage across its terminals in response to the changing current. This voltage drop counteracts the voltage of the source and therefore reduces the net voltage across the load. Over time, the rate of change of current decreases, and the voltage across the inductor also then decreases, increasing the voltage at the load. During this time, the inductor stores energy in the form of a magnetic field.

If the switch is opened while the current is still changing, then there will always be a voltage drop across the inductor, so the net voltage at the load will always be less than the input voltage source. When the switch is opened again (off-state), the voltage source will be removed from the circuit, and the current will decrease. The decreasing current will produce a voltage drop across the inductor (opposite to the drop at on-state), and now the inductor becomes a current source. The stored energy in the inductor's magnetic field supports the current flow through the load. This current, flowing while the input voltage source is disconnected, when appended to the current flowing during on-state, totals to current greater than the average input current (being zero during off-state).

The increase in average current makes up for the reduction in voltage, and ideally preserves the power provided to the load. During the off-state, the inductor is discharging its stored energy into the rest of the circuit. If the switch is closed again before the inductor fully discharges (on-state), the voltage at the load will always be greater than zero.

#### Continuous mode

Buck converters operate in continuous mode if the current through the inductor ( $I_{\text{L}}$ ) never falls to zero during the commutation cycle. In this mode, the operating principle is described by the plots in figure 4:

- When the switch pictured above is closed (top of figure 2), the voltage across the inductor is $V_{\text{L}}=V_{\text{i}}-V_{\text{o}}$ . The current through the inductor rises linearly (in approximation, so long as the voltage drop is almost constant). As the diode is reverse-biased by the voltage source $V_{\text{i}}$ , no current flows through it;
- When the switch is opened (bottom of figure 2), the diode is forward biased. The voltage across the inductor is $V_{\text{L}}=-V_{\text{o}}$ (neglecting diode drop). Current $I_{\text{L}}$ decreases.

The energy stored in inductor L is

$E={\frac {1}{2}}LI_{\text{L}}^{2}$

Therefore, it can be seen that the energy stored in L increases during on-time as $I_{\text{L}}$ increases and then decreases during the off-state. L is used to transfer energy from the input to the output of the converter.

The rate of change of $I_{\text{L}}$ can be calculated from:

$V_{\text{L}}=L{\frac {\mathrm {d} I_{\text{L}}}{\mathrm {d} t}}$

With $V_{\text{L}}$ equal to $V_{\text{i}}-V_{\text{o}}$ during the on-state and to $-V_{\text{o}}$ during the off-state. Therefore, the increase in current during the on-state is given by:

${\begin{aligned}\Delta I_{L_{\text{on}}}&=\int _{0}^{t_{\text{on}}}{\frac {V_{\text{L}}}{L}}\,\mathrm {d} t={\frac {V_{\text{i}}-V_{\text{o}}}{L}}t_{\text{on}},&t_{\text{on}}&=DT\end{aligned}}$

where D is a scalar called the duty cycle with a value between 0 and 1.

Conversely, the decrease in current during the off-state is given by:

${\begin{aligned}\Delta I_{L_{\text{off}}}&=\int _{t_{\text{on}}}^{T=t_{\text{on}}+t_{\text{off}}}{\frac {V_{\text{L}}}{L}}\,\mathrm {d} t=-{\frac {V_{\text{o}}}{L}}t_{\text{off}},&t_{\text{off}}&=(1-D)T\end{aligned}}$

Assuming that the converter operates in the steady state, the energy stored in each component at the end of a commutation cycle T is equal to that at the beginning of the cycle. That means that the current $I_{\text{L}}$ is the same at $t=0$ and at $t=T$ (figure 4).

So, from the above equations it can be written as:

${\begin{aligned}\Delta I_{L_{\text{on}}}+\Delta I_{L_{\text{off}}}&=0\\{\frac {V_{\text{i}}-V_{\text{o}}}{L}}t_{\text{on}}-{\frac {V_{\text{o}}}{L}}t_{\text{off}}&=0\end{aligned}}$

The above integrations can be done graphically. In figure 4, $\Delta I_{L_{\text{on}}}$ is proportional to the area of the yellow surface, and $\Delta I_{L_{\text{off}}}$ to the area of the orange surface, as these surfaces are defined by the inductor voltage (red lines). As these surfaces are simple rectangles, their areas can be found easily: $\left(V_{\text{i}}-V_{\text{o}}\right)t_{\text{on}}$ for the yellow rectangle and $-V_{\text{o}}t_{\text{off}}$ for the orange one. For steady state operation, these areas must be equal.

As can be seen in figure 4, $t_{\text{on}}=DT$ and $t_{\text{off}}=(1-D)T$ .

This yields:

${\begin{aligned}\left(V_{\text{i}}-V_{\text{o}}\right)DT-V_{\text{o}}(1-D)T&=0\\DV_{\text{i}}-V_{\text{o}}&=0\\{}\Rightarrow D&={\frac {V_{\text{o}}}{V_{\text{i}}}}\end{aligned}}$

From this equation, it can be seen that the output voltage of the converter varies linearly with the duty cycle for a given input voltage. As the duty cycle D is equal to the ratio between $t_{\text{on}}$ and the period T , it cannot be more than 1. Therefore, $V_{\text{o}}\leq V_{\text{i}}$ . This is why this converter is referred to as *step-down converter*.

So, for example, stepping 12 V down to 3 V (output voltage equal to one quarter of the input voltage) would require a duty cycle of 25%, in this theoretically ideal circuit.

#### Discontinuous mode

In some cases, the amount of energy required by the load is too small. In this case, the current through the inductor falls to zero during part of the period. The only difference in the principle described above is that the inductor is completely discharged at the end of the commutation cycle (see figure 5). This has, however, some effect on the previous equations.

The inductor current falling below zero results in the discharging of the output capacitor during each cycle and therefore higher switching losses. A different control technique known as pulse-frequency modulation can be used to minimize these losses.

We still consider that the converter operates in steady state. Therefore, the energy in the inductor is the same at the beginning and at the end of the cycle (in the case of discontinuous mode, it is zero). This means that the average value of the inductor voltage (VL) is zero; i.e., that the area of the yellow and orange rectangles in figure 5 are the same. This yields:

$\left(V_{\text{i}}-V_{\text{o}}\right)DT-V_{\text{o}}\delta T=0$

So the value of δ is:

$\delta ={\frac {V_{\text{i}}-V_{\text{o}}}{V_{\text{o}}}}D$

The output current delivered to the load ( $I_{\text{o}}$ ) is constant, as we consider that the output capacitor is large enough to maintain a constant voltage across its terminals during a commutation cycle. This implies that the current flowing through the capacitor has a zero average value. Therefore, we have :

${\overline {I_{\text{L}}}}=I_{\text{o}}$

Where ${\overline {I_{\text{L}}}}$ is the average value of the inductor current. As can be seen in figure 5, the inductor current waveform has a triangular shape. Therefore, the average value of IL can be sorted out geometrically as follows:

${\begin{aligned}{\overline {I_{\text{L}}}}&=\left({\frac {1}{2}}I_{L_{\text{max}}}DT+{\frac {1}{2}}I_{L_{\text{max}}}\delta T\right){\frac {1}{T}}\\&={\frac {1}{2}}I_{L_{\text{max}}}\left(D+\delta \right)\\&=I_{\text{o}}\end{aligned}}$

The inductor current is zero at the beginning and rises during ton up to ILmax. That means that ILmax is equal to:

$I_{L_{\text{max}}}={\frac {V_{\text{i}}-V_{\text{o}}}{L}}DT$

Substituting the value of ILmax in the previous equation leads to:

$I_{\text{o}}={\frac {\left(V_{\text{i}}-V_{\text{o}}\right)DT\left(D+\delta \right)}{2L}}$

And substituting δ by the expression given above yields:

$I_{\text{o}}={\frac {\left(V_{\text{i}}-V_{\text{o}}\right)DT\left(D+{\frac {V_{\text{i}}-V_{\text{o}}}{V_{\text{o}}}}D\right)}{2L}}$

This expression can be rewritten as:

$V_{\text{o}}=V_{\text{i}}{\frac {1}{{\frac {2LI_{\text{o}}}{D^{2}V_{\text{i}}T}}+1}}$

It can be seen that the output voltage of a buck converter operating in discontinuous mode is much more complicated than its counterpart of the continuous mode. Furthermore, the output voltage is now a function not only of the input voltage (Vi) and the duty cycle D, but also of the inductor value (L), the commutation period (T) and the output current (Io).

#### From discontinuous to continuous mode (and vice versa)

The converter operates in discontinuous mode when low current is drawn by the load, and in continuous mode at higher load current levels. The limit between discontinuous and continuous modes is reached when the inductor current falls to zero exactly at the end of the commutation cycle. Using the notations of figure 5, this corresponds to :

${\begin{aligned}DT+\delta T&=T\\\Rightarrow D+\delta &=1\end{aligned}}$

Therefore, the output current (equal to the average inductor current) at the limit between discontinuous and continuous modes is (see above):

$I_{{\text{o}}_{\text{lim}}}={\frac {I_{L_{\text{max}}}}{2}}\left(D+\delta \right)={\frac {I_{L_{\text{max}}}}{2}}$

Substituting ILmax by its value:

$I_{o_{\text{lim}}}={\frac {V_{\text{i}}-V_{\text{o}}}{2L}}DT$

On the limit between the two modes, the output voltage obeys both the expressions given respectively in the continuous and the discontinuous sections. In particular, the former is

$V_{\text{o}}=DV_{\text{i}}$

So Iolim can be written as:

$I_{o_{\text{lim}}}={\frac {V_{\text{i}}\left(1-D\right)}{2L}}DT$

Let's now introduce two more notations:

- the normalized voltage, defined by $\left|V_{\text{o}}\right|={\frac {V_{\text{o}}}{V_{\text{i}}}}$ . It is zero when $V_{\text{o}}=0$ , and 1 when $V_{\text{o}}=V_{\text{i}}$  ;
- the normalized current, defined by $\left|I_{\text{o}}\right|={\frac {L}{TV_{\text{i}}}}I_{\text{o}}$ . The term ${\frac {TV_{\text{i}}}{L}}$ is equal to the maximum increase of the inductor current during a cycle; i.e., the increase of the inductor current with a duty cycle D=1. So, in steady state operation of the converter, this means that $\left|I_{\text{o}}\right|$ equals 0 for no output current, and 1 for the maximum current the converter can deliver.

Using these notations, we have:

- in continuous mode: $\left|V_{\text{o}}\right|=D$
- in discontinuous mode: ${\begin{aligned}\left|V_{\text{o}}\right|&={\frac {1}{{\frac {2LI_{\text{o}}}{D^{2}V_{\text{i}}T}}+1}}\\&={\frac {1}{{\frac {2\left|I_{\text{o}}\right|}{D^{2}}}+1}}\\&={\frac {D^{2}}{2\left|I_{\text{o}}\right|+D^{2}}}\end{aligned}}$

the current at the limit between continuous and discontinuous mode is:

${\begin{aligned}I_{o_{\text{lim}}}&={\frac {V_{\text{i}}}{2L}}D\left(1-D\right)T\\&={\frac {I_{\text{o}}}{2\left|I_{\text{o}}\right|}}D\left(1-D\right)\end{aligned}}$

Therefore, the locus of the limit between continuous and discontinuous modes is given by:

${\frac {\left(1-D\right)D}{2\left|I_{\text{o}}\right|}}=1$

These expressions have been plotted in figure 6. From this, it can be deduced that in continuous mode, the output voltage does only depend on the duty cycle, whereas it is far more complex in the discontinuous mode. This is important from a control point of view.

On the circuit level, the detection of the boundary between CCM and DCM are usually provided by an inductor current sensing, requiring high accuracy and fast detectors as:

### Real-world factors

The analysis above was conducted with the assumptions:

- The output capacitor has enough capacitance to supply power to the load (a simple resistance) without any noticeable variation in its voltage.
- The voltage drop across the diode when forward biased is zero
- No commutation losses in the switch nor in the diode

These assumptions can be fairly far from reality, and the imperfections of the real components can have a detrimental effect on the operation of the converter.

#### Output voltage ripple (continuous mode)

Output voltage ripple is the name given to the phenomenon where the output voltage rises during the On-state and falls during the Off-state. Several factors contribute to this including, but not limited to, switching frequency, output capacitance, inductor, load and any current limiting features of the control circuitry. At the most basic level the output voltage will rise and fall as a result of the output capacitor charging and discharging:

$dV_{\text{o}}={\frac {idT}{C}}$

We can best approximate output ripple voltage by shifting the output current versus time waveform (continuous mode) down so that the average output current is along the time axis. When we do this, we see the AC current waveform flowing into and out of the output capacitor (sawtooth waveform). We note that *V*c-min (where *V*c is the capacitor voltage) occurs at *t*on/2 (just after capacitor has discharged) and *V*c-max at *t*off/2. By integrating *I*d*t* (= d*Q* ; as *I* = d*Q*/d*t*, *C* = *Q*/*V* so d*V* = d*Q*/*C*) under the output current waveform through writing output ripple voltage as d*V* = *I*d*t*/*C* we integrate the area above the axis to get the peak-to-peak ripple voltage as: Δ*V* = Δ*I* *T*/8*C* (where Δ*I* is the peak-to-peak ripple current and *T* is the time period of ripple. A full explanation is given there.) We note from basic AC circuit theory that our ripple voltage should be roughly sinusoidal: capacitor impedance times ripple current peak-to-peak value, or Δ*V* = Δ*I* / (ω*C*) where ω = 2π*f*, *f* is the ripple frequency, and *f* = 1/*T*, *T* the ripple period. This gives: Δ*V* = Δ*I* *T*/2π*C*), and we compare to this value to confirm the above in that we have a factor of 8 vs a factor of ~ 6.3 from basic AC circuit theory for a sinusoid. This gives confidence in our assessment here of ripple voltage. The paragraph directly below pertains that directly above and may be incorrect. Use the equations in this paragraph. Once again, please see talk tab for more: pertaining output ripple voltage and AoE (Art of Electronics 3rd edition).

During the off-state, the current in this equation is the load current. In the on-state the current is the difference between the switch current (or source current) and the load current. The duration of time (d*T*) is defined by the duty cycle and by the switching frequency.

For the on-state:

$dT_{\text{on}}=DT={\frac {D}{f}}$

For the off-state:

$dT_{\text{off}}=(1-D)T={\frac {1-D}{f}}$

Qualitatively, as the output capacitance or switching frequency increase, the magnitude of the ripple decreases. Output voltage ripple is typically a design specification for the power supply and is selected based on several factors. Capacitor selection is normally determined based on cost, physical size and non-idealities of various capacitor types. Switching frequency selection is typically determined based on efficiency requirements, which tends to decrease at higher operating frequencies, as described below in Effects of non-ideality on the efficiency. Higher switching frequency can also raise EMI concerns.

Output voltage ripple is one of the disadvantages of a switching power supply, and can also be a measure of its quality.

#### Effects on the efficiency

The simplified analysis above, does not account for non-idealities of the circuit components nor does it account for the required control circuitry. Power losses due to the control circuitry are usually insignificant when compared with the losses in the power devices (switches, diodes, inductors, etc.) The non-idealities of the power devices account for the bulk of the power losses in the converter.

Both static and dynamic power losses occur in any switching regulator. Static power losses include $I^{2}R$ (conduction) losses in the wires or PCB traces, as well as in the switches and inductor, as in any electrical circuit. Dynamic power losses occur as a result of switching, such as the charging and discharging of the switch gate, and are proportional to the switching frequency.

It is useful to begin by calculating the duty cycle for a non-ideal buck converter, which is:

$D={\frac {V_{\text{o}}+(V_{\text{sw,sync}}+V_{\text{L}})}{V_{\text{i}}-V_{\text{sw}}+V_{\text{sw,sync}}}}$

where:

- *V*sw is the voltage drop on the power switch,
- *V*sw,sync is the voltage drop on the synchronous switch or diode, and
- *V*L is the voltage drop on the inductor.

The voltage drops described above are all static power losses which are dependent primarily on DC current, and can therefore be easily calculated. For a diode drop, *V*sw and *V*sw,sync may already be known, based on the properties of the selected device.

${\begin{aligned}V_{\text{sw}}&=I_{\text{sw}}R_{\text{on}}=DI_{\text{o}}R_{\text{on}}\\V_{\text{sw,sync}}&=I_{\text{sw,sync}}R_{\text{on}}=(1-D)I_{\text{o}}R_{\text{on}}\\V_{\text{L}}&=I_{\text{L}}R_{\text{DC}}\end{aligned}}$

where:

- *R*on is the on-resistance of each switch, and
- *R*DC is the DC resistance of the inductor.

The duty cycle equation is somewhat recursive. A rough analysis can be made by first calculating the values *V*sw and *V*sw,sync using the ideal duty cycle equation.

For a MOSFET voltage drop, a common approximation is to use RDSon from the MOSFET's datasheet in Ohm's law, V = IDSRDSon(sat). This approximation is acceptable because the MOSFET is in the linear state, with a relatively constant drain-source resistance. This approximation is only valid at relatively low VDS values. For more accurate calculations, MOSFET datasheets contain graphs on the VDS and IDS relationship at multiple VGS values. Observe VDS at the VGS and IDS which most closely match what is expected in the buck converter.

In addition, power loss occurs as a result of leakage currents. This power loss is simply

$P_{\text{leakage}}=I_{\text{leakage}}V$

where:

- *I*leakage is the leakage current of the switch, and
- *V* is the voltage across the switch.

Dynamic power losses are due to the switching behavior of the selected pass devices (MOSFETs, power transistors, IGBTs, etc.). These losses include turn-on and turn-off switching losses and switch transition losses.

Switch turn-on and turn-off losses are easily lumped together as

$P_{\text{SW}}={\frac {VI_{\text{o}}(t_{\text{rise}}+t_{\text{fall}})}{6T}}$

where:

- *V* is the voltage across the switch while the switch is off,
- *t*rise and *t*fall are the switch rise and fall times, and
- *T* is the switching period

but this does not take into account the parasitic capacitance of the MOSFET which makes the *Miller plate*. Then, the switch losses will be more like:

$P_{\text{SW}}={\frac {VI_{\text{o}}\left(t_{\text{rise}}+t_{\text{fall}}\right)}{2T}}$

When a MOSFET is used for the lower switch, additional losses may occur during the time between the turn-off of the high-side switch and the turn-on of the low-side switch, when the body diode of the low-side MOSFET conducts the output current. This time, known as the non-overlap time, prevents "shoot-through", a condition in which both switches are simultaneously turned on. The onset of shoot-through generates severe power loss and heat. Proper selection of non-overlap time must balance the risk of shoot-through with the increased power loss caused by conduction of the body diode. Many MOSFET based buck converters also include a diode to aid the lower MOSFET body diode with conduction during the non-overlap time. When a diode is used exclusively for the lower switch, diode forward turn-on time can reduce efficiency and lead to voltage overshoot.

Power loss on the body diode is also proportional to switching frequency and is

$P_{\text{D,body}}=V_{\text{F}}I_{\text{o}}t_{\text{no}}f_{\text{SW}}$

where:

- *VF* is the forward voltage of the body diode, and
- *tno* is the selected non-overlap time.

Finally, power losses occur as a result of the power required to turn the switches on and off. For MOSFET switches, these losses are dominated by the energy required to charge and discharge the capacitance of the MOSFET gate between the threshold voltage and the selected gate voltage. These switch transition losses occur primarily in the gate driver, and can be minimized by selecting MOSFETs with low gate charge, by driving the MOSFET gate to a lower voltage (at the cost of increased MOSFET conduction losses), or by operating at a lower frequency.

$P_{\text{Gdrive}}=Q_{\text{G}}V_{\text{GS}}f_{\text{SW}}$

where:

- *Q*G is the gate charge of the selected MOSFET, and
- *V*GS is the peak gate-source voltage.

For N-MOSFETs, the high-side switch must be driven to a higher voltage than *Vi*. To achieve this, MOSFET gate drivers typically feed the MOSFET output voltage back into the gate driver. The gate driver then adds its own supply voltage to the MOSFET output voltage when driving the high-side MOSFETs to achieve a *VGS* equal to the gate driver supply voltage. Because the low-side *VGS* is the gate driver supply voltage, this results in very similar *VGS* values for high-side and low-side MOSFETs.

A complete design for a buck converter includes a tradeoff analysis of the various power losses. Designers balance these losses according to the expected uses of the finished design. A converter expected to have a low switching frequency does not require switches with low gate transition losses; a converter operating at a high duty cycle requires a low-side switch with low conduction losses.

### Specific structures

#### Synchronous rectification

A synchronous buck converter is a modified version of the basic buck converter circuit topology in which the diode, D, is replaced by a second switch, S2. This modification is a tradeoff between increased cost and improved efficiency.

In a standard buck converter, the flyback diode turns on, on its own, shortly after the switch turns off, as a result of the rising voltage across the diode. This voltage drop across the diode results in a power loss which is equal to

$P_{\text{D}}=V_{\text{D}}(1-D)I_{\text{o}}$

where:

- *V*D is the voltage drop across the diode at the load current *Io*,
- *D* is the duty cycle, and
- *Io* is the load current.

By replacing the diode with a switch selected for low loss, the converter efficiency can be improved. For example, a MOSFET with very low *R*DSon might be selected for *S*2, providing power loss on switch 2 which is

$P_{S_{2}}=I_{\text{o}}^{2}R_{\text{DSon}}(1-D)$

In both cases, power loss is strongly dependent on the duty cycle, D. Power loss on the freewheeling diode or lower switch will be proportional to its on-time. Therefore, systems designed for low duty cycle operation will suffer from higher losses in the freewheeling diode or lower switch, and for such systems it is advantageous to consider a synchronous buck converter design.

Consider a computer power supply, where the input is 5 V, the output is 3.3 V, and the load current is 10 A. In this case, the duty cycle will be 66% and the diode would be on for 34% of the time. A typical diode with forward voltage of 0.7 V would suffer a power loss of 2.38 W. A well-selected MOSFET with RDSon of 0.015 Ω, however, would waste only 0.51 W in conduction loss. This translates to improved efficiency and reduced heat generation.

Another advantage of the synchronous converter is that it is bi-directional, which lends itself to applications requiring regenerative braking. When power is transferred in the "reverse" direction, it acts much like a boost converter.

The advantages of the synchronous buck converter do not come without cost. First, the lower switch typically costs more than the freewheeling diode. Second, the complexity of the converter is vastly increased due to the need for a complementary-output switch driver.

Such a driver must prevent both switches from being turned on at the same time, a fault known as "shootthrough". The simplest technique for avoiding shootthrough is a time delay between the turn-off of S1 to the turn-on of S2, and vice versa. However, setting this time delay long enough to ensure that S1 and S2 are never both on will itself result in excess power loss. An improved technique for preventing this condition is known as adaptive "non-overlap" protection, in which the voltage at the switch node (the point where S1, S2 and L are joined) is sensed to determine its state. When the switch node voltage passes a preset threshold, the time delay is started. The driver can thus adjust to many types of switches without the excessive power loss this flexibility would cause with a fixed non-overlap time.

Both low side and high side switches may be turned off in response to a load transient and the body diode in the low side MOSFET or another diode in parallel with it becomes active. The higher voltage drop on the low side switch is then of benefit, helping to reduce current output and meet the new load requirement sooner.

#### Multiphase buck

The multiphase buck converter is a circuit topology where basic buck converter circuits are placed in parallel between the input and load. Each of the *n* "phases" is turned on at equally spaced intervals over the switching period. This circuit is typically used with the synchronous buck topology, described above.

This type of converter can respond to load changes as quickly as if it switched *n* times faster, without the increase in switching losses that would cause. Thus, it can respond to rapidly changing loads, such as modern microprocessors.

There is also a significant decrease in switching ripple. Not only is there the decrease due to the increased effective frequency, but any time that *n* times the duty cycle is an integer, the switching ripple goes to 0; the rate at which the inductor current is increasing in the phases which are switched on exactly matches the rate at which it is decreasing in the phases which are switched off.

Another advantage is that the load current is split among the *n* phases of the multiphase converter. This load splitting allows the heat losses on each of the switches to be spread across a larger area.

This circuit topology is used in computer motherboards to convert the 12 VDC power supply to a lower voltage (around 1 V), suitable for the CPU. Modern CPU power requirements can exceed 200 W, can change very rapidly, and have very tight ripple requirements, less than 10 mV. Typical CPU power supplies found on mainstream motherboards use 3 or 4 phases, while high-end systems can have 16 or more phases.

One major challenge inherent in the multiphase converter is ensuring the load current is balanced evenly across the *n* phases. This current balancing can be performed in a number of ways. Current can be measured "losslessly" by sensing the voltage across the inductor or the lower switch (when it is turned on). This technique is considered lossless because it relies on resistive losses inherent in the buck converter topology. Another technique is to insert a small resistor in the circuit and measure the voltage across it. This approach is more accurate and adjustable, but incurs several costs—space, efficiency and money.

Finally, the current can be measured at the input. Voltage can be measured losslessly, across the upper switch, or using a power resistor, to approximate the current being drawn. This approach is technically more challenging, since switching noise cannot be easily filtered out. However, it is less expensive than having a sense resistor for each phase.

## Efficiency

There are two main phenomena impacting the efficiency: conduction losses and switching losses.

Conduction losses happen when current is flowing through the components and thus depend on the load. They are caused by Joule effect in the resistance when the transistor or MOSFET switch is conducting, the inductor winding resistance, and the capacitor equivalent series resistance. Losses are proportional to the square of the current in this case. Conduction losses are also generated by the diode forward voltage drop (usually 0.7 V or 0.4 V for Schottky diode), and are proportional to the current in this case.

Switching losses happen in the transistor and diode when the voltage and the current overlap during the transitions between closed and open states. A Schottky diode can be used to minimize the switching losses caused by the reverse recovery of a regular PN diode. The switching losses are proportional to the switching frequency.

In a complete real-world buck converter, there is also a command circuit to regulate the output voltage or the inductor current. This circuit and the MOSFET gate controller have a power consumption, impacting the overall efficiency of the converter.

## Impedance matching

A buck converter can be used to maximize the power transfer through the use of impedance matching. An application of this is in a *maximum power point tracker* commonly used in photovoltaic systems. This is particularly useful in applications where the impedances are dynamically changing.

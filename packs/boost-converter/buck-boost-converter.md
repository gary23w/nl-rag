---
title: "Buck–boost converter"
source: https://en.wikipedia.org/wiki/Buck-boost_converter
domain: boost-converter
license: CC-BY-SA-4.0
tags: boost converter, buck-boost converter, power converter, step-up converter
fetched: 2026-07-02
---

# Buck–boost converter

(Redirected from

Buck-boost converter

)

The **buck–boost converter** is a type of DC-to-DC converter that has an output voltage magnitude that is either greater than or less than the input voltage magnitude. It is equivalent to a flyback converter using a single inductor instead of a transformer. Two different topologies are called *buck–boost converter*. Both of them can produce a range of output voltages, ranging from much larger (in absolute magnitude) than the input voltage, down to almost zero.

In the inverting topology, the output voltage is of the opposite polarity than the input. This is a switched-mode power supply with a similar circuit configuration to the boost converter and the buck converter. The output voltage is adjustable based on the duty cycle of the switching transistor. One possible drawback of this converter is that the switch does not have a terminal at ground; this complicates the driving circuitry. However, this drawback is of no consequence if the power supply is isolated from the load circuit (if, for example, the supply is a battery) because the supply and diode polarity can simply be reversed. When they can be reversed, the switch can be placed either on the ground side or the supply side.

When a buck (step-down) converter is combined with a boost (step-up) converter, the output voltage is typically of the same polarity of the input, and can be lower or higher than the input. Such a non-inverting buck–boost converter may use a single inductor which is used for both the buck inductor mode and the boost inductor mode, using switches instead of diodes, sometimes called a "four-switch buck–boost converter", it may use multiple inductors but only a single switch as in the SEPIC and Ćuk topologies.

## Principle of operation of the inverting topology

The basic principle of the inverting buck–boost converter is fairly simple (see figure 2):

- while in the On-state, the input voltage source is directly connected to the inductor (L). This results in accumulating energy in L. In this state, the capacitor supplies energy to the output load.
- while in the Off-state, the inductor is connected to the output load and capacitor, so energy is transferred from L to C and R.

Compared to the buck and boost converters, the characteristics of the inverting buck–boost converter are mainly:

- polarity of the output voltage is opposite to that of the input;
- the output voltage can vary continuously from 0 to −∞ (for an ideal converter). The output voltage ranges for a buck and a boost converter are respectively *V*i to 0 and *V*i to ∞.

### Conceptual overview

Like the buck and boost converters, the operation of the buck–boost is best understood in terms of the inductor's "reluctance" to allow rapid change in current. From the initial state in which nothing is charged and the switch is open, the current through the inductor is zero. When the switch is first closed, the blocking diode prevents current from flowing into the right hand side of the circuit, so it must all flow through the inductor. However, since the inductor doesn't allow rapid current change, it will initially keep the current low by opposing the voltage provided by the source.

Over time, the inductor will allow the current to slowly increase. In an ideal circuit the voltage across the inductor would remain constant, but when the inherent resistance of wiring, switch and the inductor itself is taken into account, the effective (electro-motive) voltage across the inductor will decrease as the current increases. Also during this time, the inductor will store energy in the form of a magnetic field.

### Continuous mode

If the current through the inductor L never falls to zero during a commutation cycle, the converter is said to operate in continuous mode. The current and voltage waveforms in an ideal converter can be seen in Figure 3.

From *t* = 0 to *t* = *DT*, the converter is in on-state, so the switch S is closed. The rate of change in the inductor current *I*L is therefore given by ${\frac {\mathop {} \!\mathrm {d} I_{\mathrm {L} }}{\mathop {} \!\mathrm {d} t}}={\frac {V_{\mathrm {i} }}{L}}.$

At the end of the on-state, the increase of *I*L is therefore: $\Delta I_{\mathrm {L} ,{\text{On}}}=\int _{0}^{DT}\mathop {} \!\mathrm {d} I_{\mathrm {L} }=\int _{0}^{DT}{\frac {V_{\mathrm {i} }}{L}}\,\mathop {} \!\mathrm {d} t={\frac {V_{\mathrm {i} }DT}{L}}.$

D is the duty cycle. It represents the fraction of the commutation period T during which the switch is on. Therefore D ranges between 0 (S is never on) and 1 (S is always on).

During the off-state, the switch S is open, so the inductor current flows through the load. If we assume zero voltage drop in the diode, and a capacitor large enough for its voltage to remain constant, the evolution of *I*L is: ${\frac {\mathop {} \!\mathrm {d} I_{\mathrm {L} }}{\mathop {} \!\mathrm {d} t}}={\frac {V_{\mathrm {o} }}{L}},$

Therefore, the variation of *I*L during the off-period is: $\Delta I_{\mathrm {L} ,{\text{Off}}}=\int _{0}^{\left(1-D\right)T}\mathop {} \!\mathrm {d} I_{\mathrm {L} }=\int _{0}^{\left(1-D\right)T}{\frac {V_{\mathrm {o} }}{L}}\mathop {} \!\mathrm {d} t={\frac {V_{\mathrm {o} }\left(1-D\right)T}{L}}.$

As we consider that the converter operates in steady-state conditions, the amount of energy stored in each of its components has to be the same at the beginning and at the end of a commutation cycle. As the energy in an inductor is given by: $E={\frac {1}{2}}LI_{\mathrm {L} }^{2},$ it is obvious that the value of *I*L at the end of the off state must be the same with the value of *I*L at the beginning of the on-state, i.e. the sum of the variations of *I*L during the on and the off states must be zero: $\Delta I_{\mathrm {L} ,{\text{On}}}+\Delta I_{\mathrm {L} ,{\text{Off}}}=0.$

Substituting $\Delta I_{\mathrm {L} ,{\text{On}}}$ and $\Delta I_{\mathrm {L} ,{\text{Off}}}$ by their expressions yields: ${\frac {V_{\mathrm {i} }DT}{L}}+{\frac {V_{\mathrm {o} }\left(1-D\right)T}{L}}=0.$

This can be written as: ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}=-{\frac {D}{1-D}}.$

This in return yields that: $D={\frac {V_{\mathrm {o} }}{V_{\mathrm {o} }-V_{\mathrm {i} }}}$

From the above expression it can be seen that the polarity of the output voltage is always negative (because the duty cycle goes from 0 to 1), and that its absolute value increases with D, theoretically up to minus infinity when D approaches 1. Apart from the polarity, this converter is either step-up (a boost converter) or step-down (a buck converter). Thus it is named a buck–boost converter.

### Discontinuous mode

In some cases, the amount of energy required by the load is small enough to be transferred in a time smaller than the whole commutation period. In this case, the current through the inductor falls to zero during part of the period. The only difference in the principle described above is that the inductor is completely discharged at the end of the commutation cycle (see waveforms in figure 4). Although slight, the difference has a strong effect on the output voltage equation. It can be calculated as follows:

Because the inductor current at the beginning of the cycle is zero, its maximum value $I_{\mathrm {L} ,{\text{max}}}$ (at *t* = *DT*) is $I_{\mathrm {L} ,{\text{max}}}={\frac {V_{\mathrm {i} }DT}{L}}.$

During the off-period, *I*L falls to zero after δT: $I_{\mathrm {L} ,{\text{max}}}+{\frac {V_{\mathrm {o} }\delta T}{L}}=0.$

Using the two previous equations, δ is: $\delta =-{\frac {V_{\mathrm {i} }D}{V_{\mathrm {o} }}}.$

The load current *I*o is equal to the average diode current *I*D. As can be seen on figure 4, the diode current is equal to the inductor current during the off-state. Therefore, the output current can be written as: $I_{\mathrm {o} }={\bar {I_{\mathrm {D} }}}={\frac {I_{\mathrm {L} ,{\text{max}}}}{2}}\delta .$

Replacing *I*L,max and δ by their respective expressions yields: ${\begin{aligned}I_{\mathrm {o} }&=-{\frac {V_{\mathrm {i} }DT}{2L}}{\frac {V_{\mathrm {i} }D}{V_{\mathrm {o} }}}\\&=-{\frac {V_{\mathrm {i} }^{2}D^{2}T}{2LV_{\mathrm {o} }}}.\end{aligned}}$

Therefore, the output voltage gain can be written as: ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}=-{\frac {V_{\mathrm {i} }D^{2}T}{2LI_{\mathrm {o} }}}.$

Compared to the expression of the output voltage gain for the continuous mode, this expression is much more complicated. Furthermore, in discontinuous operation, the output voltage not only depends on the duty cycle, but also on the inductor value, the input voltage and the output current.

### Limit between continuous and discontinuous modes

As told at the beginning of this section, the converter operates in discontinuous mode when low current is drawn by the load, and in continuous mode at higher load current levels. The limit between discontinuous and continuous modes is reached when the inductor current falls to zero exactly at the end of the commutation cycle. with the notations of figure 4, this corresponds to: ${\begin{aligned}DT+\delta T&=T\\D+\delta &=1.\end{aligned}}$

In this case, the output current *I*o,lim (output current at the limit between continuous and discontinuous modes) is given by: $I_{\mathrm {o} ,{\text{lim}}}={\bar {I_{\mathrm {D} }}}={\frac {I_{\mathrm {L} ,{\text{max}}}}{2}}\left(1-D\right).$

Replacing *I*L,max by the expression given in the § Discontinuous mode section yields: $I_{\mathrm {o} ,{\text{lim}}}={\frac {V_{\mathrm {i} }DT}{2L}}\left(1-D\right).$

As *I*o,lim is the current at the limit between continuous and discontinuous modes of operations, it satisfies the expressions of both modes. Therefore, using the expression of the output voltage in continuous mode, the previous expression can be written as: $I_{\mathrm {o} _{\text{lim}}}={\frac {V_{\mathrm {i} }DT}{2L}}{\frac {V_{\mathrm {i} }}{V_{\mathrm {o} }}}\left(-D\right).$

Let's now introduce two more notations:

- the normalized voltage, defined by ⁠ $\scriptstyle \left|V_{\mathrm {o} }\right|={\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}$ ⁠. It corresponds to the gain in voltage of the converter;
- the normalized current, defined by ⁠ $\scriptstyle \left|I_{\mathrm {o} }\right|={\frac {L}{TV_{\mathrm {i} }}}I_{\mathrm {o} }$ ⁠. The term ⁠ $\scriptstyle {\frac {TV_{\mathrm {i} }}{L}}$ ⁠ is equal to the maximum increase of the inductor current during a cycle; i.e., the increase of the inductor current with a duty cycle *D* = 1. So, in steady state operation of the converter, this means that |*I*o| equals 0 for no output current, and 1 for the maximum current the converter can deliver.

Using these notations, we have:

- in continuous mode, ⁠ $\scriptstyle \left|V_{\mathrm {o} }\right|=-{\frac {D}{1-D}}$ ⁠;
- in discontinuous mode, ⁠ $\scriptstyle \left|V_{\mathrm {o} }\right|=-{\frac {D^{2}}{2\left|I_{\mathrm {o} }\right|}}$ ⁠;
- the current at the limit between continuous and discontinuous mode is $I_{\mathrm {o} ,{\text{lim}}}={\frac {V_{\mathrm {i} }T}{2L}}D\left(1-D\right)={\frac {I_{\mathrm {o} ,{\text{lim}}}}{2\left|I_{o}\right|}}D\left(1-D\right).$ Therefore, the locus of the limit between continuous and discontinuous modes is given by ${\frac {1}{2\left|I_{\mathrm {o} }\right|}}D\left(1-D\right)=1.$

These expressions have been plotted in figure 5. The difference in behavior between the continuous and discontinuous modes can be seen clearly.

## Principles of operation of the four-switch topology

The four-switch converter combines the buck and boost converters. It can operate in either the buck or the boost mode. In either mode, only one switch controls the duty cycle, another is for commutation and must be operated inversely to the former one, and the remaining two switches are in a fixed position. A two-switch buck–boost converter can be built with two diodes, but upgrading the diodes to FET switches doesn't cost much extra while efficiency improves due to the lower voltage drop.

## Non-ideal circuit

### Effect of parasitic resistances

In the analysis above, no dissipative elements (resistors) have been considered. That means that the power is transmitted without losses from the input voltage source to the load. However, parasitic resistances exist in all circuits, due to the resistivity of the materials they are made from. Therefore, a fraction of the power managed by the converter is dissipated by these parasitic resistances.

For the sake of simplicity, we consider here that the inductor is the only non-ideal component, and that it is equivalent to an inductor and a resistor in series. This assumption is acceptable because an inductor is made of one long wound piece of wire, so it is likely to exhibit a non-negligible parasitic resistance *R*L. Furthermore, current flows through the inductor both in the on and the off states.

Using the state-space averaging method, we can write: $V_{\mathrm {i} }={\bar {V_{\mathrm {L} }}}+{\bar {V_{\mathrm {S} }}}$

where ${\bar {V_{\mathrm {L} }}}$ and ${\bar {V_{\mathrm {S} }}}$ are respectively the average voltage across the inductor and the switch over the commutation cycle. If we consider that the converter operates in steady-state, the average current through the inductor is constant. The average voltage across the inductor is: ${\bar {V_{\mathrm {L} }}}=L{\frac {\mathrm {d} {\bar {I_{\mathrm {L} }}}}{\mathrm {d} t}}+R_{\mathrm {L} }{\bar {I_{\mathrm {L} }}}=R_{\mathrm {L} }{\bar {I_{\mathrm {L} }}}.$

When the switch is in the on-state, *V*S = 0. When it is off, the diode is forward biased (we consider the continuous mode operation), therefore *V*S = *V*i − *V*o Therefore, the average voltage across the switch is: ${\bar {V_{\mathrm {S} }}}=D\,0+(1-D)(V_{\mathrm {i} }-V_{\mathrm {o} })=(1-D)(V_{\mathrm {i} }-V_{\mathrm {o} }).$

The output current is the opposite of the inductor current during the off-state. The average inductor current is therefore: ${\bar {I_{\mathrm {L} }}}={\frac {-I_{\mathrm {o} }}{1-D}}.$ Assuming the output current and voltage have negligible ripple, the load of the converter can be considered purely resistive. If R is the resistance of the load, the above expression becomes: ${\bar {I_{\mathrm {L} }}}={\frac {-V_{\mathrm {o} }}{(1-D)R}}.$

Using the previous equations, the input voltage becomes: $V_{\mathrm {i} }=R_{\mathrm {L} }{\frac {-V_{\mathrm {o} }}{(1-D)R}}+(1-D)(V_{\mathrm {i} }-V_{\mathrm {o} }).$

This can be written as: ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}={\frac {-D}{{\frac {R_{\mathrm {L} }}{R(1-D)}}+1-D}}.$

If the inductor resistance is zero, the equation above becomes equal to that of the *ideal* case. But when *R*L increases, the voltage gain of the converter decreases compared to the ideal case. Furthermore, the influence of *R*L increases with the duty cycle. This is summarized in figure 6.

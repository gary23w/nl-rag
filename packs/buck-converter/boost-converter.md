---
title: "Boost converter"
source: https://en.wikipedia.org/wiki/Boost_converter
domain: buck-converter
license: CC-BY-SA-4.0
tags: buck converter, boost converter, buck-boost converter, Cuk converter
fetched: 2026-07-02
---

# Boost converter

A **boost converter** or **step-up converter** is a DC-to-DC converter that increases voltage, while decreasing current, from its input (*supply*) to its output (*load*).

It is a class of switched-mode power supply (SMPS) containing at least two semiconductors, a diode and a transistor, and at least one energy storage element: a capacitor, inductor, or the two in combination. To reduce voltage ripple, filters made of capacitors (sometimes in combination with inductors) are normally added to such a converter's output (load-side filter) and input (supply-side filter).

## Overview

Power for the boost converter can come from any suitable DC source, such as batteries, solar panels, rectifiers, and DC generators. A process that changes one DC voltage to a different DC voltage is called DC-to-DC conversion. A boost converter is a DC-to-DC converter with an output voltage greater than the source voltage. A boost converter is sometimes called a step-up converter since it "steps up" the source voltage. Since power ( ${\textstyle P=U\cdot I}$ ) must be conserved, the output current is lower than the source current.

The hydraulic ram can be seen as the hydraulic analogue to a boost converter.

## History

For high efficiency, the switched-mode power supply (SMPS) switch must turn on and off quickly and have low losses. The advent of a commercial semiconductor switch in the 1950s represented a major milestone that made SMPSs such as the boost converter possible. The major DC-to-DC converters were developed in the early 1960s when semiconductor switches had become available. The aerospace industry’s need for small, lightweight, and efficient power converters led to the converter’s rapid development.

Switched systems such as SMPS are a challenge to design since their models depend on whether a switch is opened or closed. R. D. Middlebrook from Caltech in 1977 published the models for DC-to-DC converters used today. Middlebrook averaged the circuit configurations for each switch state in a technique called state-space averaging. This simplification reduced two systems into one. The new model led to insightful design equations which helped the growth of SMPS.

## Applications

### Battery power systems

Battery power systems often stack cells in series to achieve higher voltage. However, sufficient stacking of cells is not possible in many high voltage applications due to lack of space. Boost converters can increase the voltage and reduce the number of cells. Two battery-powered applications that use boost converters are used in hybrid electric vehicles (HEV) and lighting systems.

The NHW20 model Toyota Prius HEV uses a 500 V motor. Without a boost converter, the Prius would need nearly 417 cells to power the motor. However, a Prius actually uses only 168 cells and boosts the battery voltage from 202 V to 500 V. Boost converters also power devices at smaller scale applications, such as portable lighting systems. A white LED typically requires 3.3 V to emit light, and a boost converter can step up the voltage from a single 1.5 V alkaline cell to power the lamp.

### Joule thief

An unregulated boost converter is used as the voltage increase mechanism in the circuit known as the "Joule thief", based on blocking oscillator concepts. This circuit topology is used with low power battery applications, and is aimed at the ability of a boost converter to "steal" the remaining energy in a battery. This energy would otherwise be wasted since the low voltage of a nearly depleted battery makes it unusable for a normal load. This voltage decrease occurs as batteries become depleted, and is a characteristic of the ubiquitous alkaline battery. Since the equation for power is ⁠ $\textstyle P={\frac {V^{2}}{R}}$ ⁠, and ⁠ R ⁠ tends to be stable, power available to the load goes down significantly as voltage decreases.

### Photovoltaic cells

The special kind of boost-converters called voltage-lift type boost converters are used in solar photovoltaic (PV) systems. These power converters add up the passive components (diode, inductor and capacitor) of a traditional boost-converter to improve the power quality and increase the performance of complete PV system.

## Circuit analysis

### Operation

The key principle that drives the boost converter is the tendency of an inductor to resist changes in current by either increasing or decreasing the energy stored in the inductor's magnetic field. In a boost converter, the output voltage is always higher than the input voltage. A schematic of a boost power stage is shown in Figure 1.

**Closed switch**

When the switch is closed ('on-state'), current flows through the inductor in the clockwise direction and the inductor stores some energy by generating a magnetic field. The polarity of the left side of the inductor is positive.

**Opened switch**

When the switch is opened ('off-state'), the magnetic field previously created will be reduced in energy to maintain the current through the inductor. The polarity of the inductor will be reversed, which means the left side of the inductor will become negative. As a result, the current from both the voltage source and the inductor in series will add together and be redirected through the now forward-biased diode

D

towards the load.

If the switch is cycled fast enough, the inductor will not discharge fully in between charging stages, and the load will always see a voltage greater than that of the input source alone when the switch is opened. Also, while the switch is opened, the capacitor, in parallel with the load, is charged to this combined voltage. When the switch is then closed, and the right-hand side is shorted out from the left-hand side, the capacitor is, therefore, able to provide the voltage and energy to the load. During this time, the blocking diode prevents the capacitor from discharging through the switch. The switch must, of course, be opened again fast enough to prevent the capacitor from discharging too much.

The basic principle of a boost converter consists of two distinct states (Figure 2):

**on-state**

In the on-state, the switch

S

(

Figure 1

) is closed, resulting in an increase in the inductor current;

**off-state**

In the off-state, the switch is open, and the only path offered to inductor current is through the

flyback diode

D

, the capacitor

C

, and the load

R

. This results in transferring the energy accumulated during the on-state into the capacitor.

The input current is the same as the inductor current, as shown in Figure 2. So, it is not discontinuous as in the buck converter, and the requirements on the input filter are relaxed compared to a buck converter.

#### Continuous mode

When a boost converter operates in continuous mode, the current through the inductor, ⁠ $I_{\mathrm {L} }$ ⁠, never falls to zero. Figure 3 shows the typical waveforms of inductor current and voltage in a converter operating in this mode.

In the steady state, the DC (average) voltage across the inductor must be zero so that after each cycle, the inductor returns the same state because the voltage across the inductor is proportional to the rate of change of current through it (explained in more detail below). Note in Figure 1 that the left-hand side of ⁠ L ⁠ is at ⁠ $V_{\mathrm {i} }$ ⁠, and the right-hand side of ⁠ L ⁠ sees the $V_{\mathrm {S} }$ voltage waveform from Figure 3. The average value of $V_{\mathrm {S} }$ is ⁠ $(1-D)V_{\mathrm {o} }$ ⁠, where ⁠ D ⁠ is the duty cycle of the waveform driving the switch. From this we get the **ideal transfer function**: $V_{\mathrm {i} }=(1-D)V_{\mathrm {o} }$ or ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}={\frac {1}{1-D}}.$

We get the same result from a more detailed analysis as follows: The output voltage can be calculated as follows in the case of an ideal converter (i.e., using components with an ideal behaviour) operating in steady conditions:

During the on-state, the switch S is closed, which makes the input voltage $V_{\mathrm {i} }$ appear across the inductor, which causes a change in current $I_{\mathrm {L} }$ flowing through the inductor during a time period t by the formula: ${\frac {\Delta I_{\mathrm {L} }}{\Delta t}}={\frac {V_{\mathrm {i} }}{L}},$ where ⁠ L ⁠ is the inductor value.

At the end of the on-state, the increase of $I_{\mathrm {L} }$ is therefore ${\begin{aligned}\Delta I_{\mathrm {L} {\text{,on}}}&={\frac {1}{L}}\int _{0}^{DT}V_{\mathrm {i} }\mathop {} \!dt\\&={\frac {DT}{L}}V_{\mathrm {i} },\end{aligned}}$ where D is the duty cycle. It represents the fraction of the commutation period T during which the switch is on. Therefore, D ranges between 0 (S is never on) and 1 (S is always on).

During the off-state, the switch S is open, so the inductor current flows through the load. If we consider zero voltage drop in the diode and a capacitor large enough for its voltage to remain constant, the evolution of $I_{\mathrm {L} }$ is: $V_{\mathrm {i} }-V_{\mathrm {o} }=L{\frac {dI_{\mathrm {L} }}{dt}}.$

Therefore, the variation of $I_{\mathrm {L} }$ during the off-period is: ${\begin{aligned}\Delta I_{\mathrm {L} {\text{,off}}}&=\int _{DT}^{T}{\frac {\left(V_{\mathrm {i} }-V_{\mathrm {o} }\right)\mathop {} }{L}}\mathop {} \!dt\\&={\frac {\left(V_{\mathrm {i} }-V_{\mathrm {o} }\right)\left(1-D\right)T}{L}}.\end{aligned}}$

As we consider that the converter operates in steady state conditions, the amount of energy stored in each of its components has to be the same at the beginning and at the end of a commutation cycle. In particular, the energy stored in the inductor is given by: $E={\frac {1}{2}}LI_{\mathrm {L} }^{2}.$

So, the inductor current has to be the same at the start and end of the commutation cycle. This means the overall change in the current (the sum of the changes) is zero: $\Delta I_{\mathrm {L} {\text{,on}}}+\Delta I_{\mathrm {L} {\text{,off}}}=0.$

Substituting $\Delta I_{\mathrm {L} {\text{,on}}}$ and $\Delta I_{\mathrm {L} {\text{,off}}}$ by their expressions yields: $\Delta I_{\mathrm {L} {\text{,on}}}+\Delta I_{\mathrm {L} {\text{,off}}}={\frac {V_{\mathrm {i} }DT}{L}}+{\frac {\left(V_{\mathrm {i} }-V_{\mathrm {o} }\right)\left(1-D\right)T}{L}}=0.$

This can be written as: ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}={\frac {1}{1-D}}.$

The above equation shows that the output voltage is always higher than the input voltage (as the duty cycle goes from 0 to 1), and that it increases with ⁠ D ⁠, theoretically to infinity as D approaches 1. This is why this converter is sometimes referred to as a 'step-up' converter.

Rearranging the equation reveals the duty cycle to be: $D=1-{\frac {V_{\mathrm {i} }}{V_{\mathrm {o} }}}.$

#### Discontinuous mode

If the ripple amplitude of the current is too high, the inductor may be completely discharged before the end of a whole commutation cycle. This commonly occurs under light loads. In this case, the current through the inductor falls to zero during part of the period (see waveforms in Figure 4). Although the difference is slight, it has a strong effect on the output voltage equation.

The voltage gain can be calculated as follows:

As the inductor current at the beginning of the cycle is zero, its maximum value $I_{\mathrm {L} {\text{,max}}}$ (at ⁠ $t=DT$ ⁠) is $I_{\mathrm {L} {\text{,max}}}={\frac {V_{\mathrm {i} }DT}{L}}$

During the off-period, $I_{\mathrm {L} }$ falls to zero after ⁠ $\delta T$ ⁠: $I_{\mathrm {L} {\text{,max}}}+{\frac {\left(V_{\mathrm {i} }-V_{\mathrm {o} }\right)\delta T}{L}}=0.$

Using the two previous equations, $\delta$ is: $\delta ={\frac {V_{\mathrm {i} }D}{V_{\mathrm {o} }-V_{\mathrm {i} }}}$

The load current $I_{\mathrm {o} }$ is equal to the average diode current ⁠ $I_{\mathrm {D} }$ ⁠. As can be seen in Figure 4, the diode current is equal to the inductor current during the off-state. The average value of $I_{\mathrm {o} }$ can be sorted out geometrically from Figure 4. Therefore, the output current can be written as: ${\begin{aligned}I_{\mathrm {o} }&={\bar {I}}_{\mathrm {D} }\\&={\frac {I_{\mathrm {L} {\text{,max}}}}{2}}\delta .\end{aligned}}$

Replacing $I_{\mathrm {L} {\text{,max}}}$ and $\delta$ by their respective expressions yields: ${\begin{aligned}I_{\mathrm {o} }&={\frac {V_{\mathrm {i} }DT}{2L}}\cdot {\frac {V_{\mathrm {i} }D}{V_{\mathrm {o} }-V_{\mathrm {i} }}}\\&={\frac {V_{\mathrm {i} }^{2}D^{2}T}{2L\left(V_{\mathrm {o} }-V_{\mathrm {i} }\right)}}.\end{aligned}}$

Therefore, the output voltage gain can be written as ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}=1+{\frac {V_{\mathrm {i} }D^{2}T}{2LI_{\mathrm {o} }}}.$

Compared to the expression of the output voltage gain for continuous mode, this expression is much more complicated. Furthermore, in discontinuous operation, the output voltage gain not only depends on the duty cycle ⁠ D ⁠, but also on the inductor value ⁠ L ⁠, the input voltage ⁠ $V_{\mathrm {i} }$ ⁠, the commutation period ⁠ T ⁠, and the output current ⁠ $I_{\mathrm {o} }$ ⁠.

Substituting ${\textstyle I_{\mathrm {o} }={\frac {V_{\mathrm {o} }}{R}}}$ into the equation, where R is the load, the output voltage gain can be rewritten as: ${\frac {V_{\mathrm {o} }}{V_{\mathrm {i} }}}={\frac {1+{\sqrt {1+{\frac {4D^{2}}{K}}}}}{2}},$ where $K={\frac {2L}{RT}}.$

---
title: "Ćuk converter"
source: https://en.wikipedia.org/wiki/Ćuk_converter
domain: buck-converter
license: CC-BY-SA-4.0
tags: buck converter, boost converter, buck-boost converter, Cuk converter
fetched: 2026-07-02
---

# Ćuk converter

The **Ćuk converter** (Serbo-Croatian: [tɕûːk], English: /ˈtʃuːk/) is a type of buck-boost converter with low ripple current. A Ćuk converter can be seen as a combination of boost converter and buck converter, having one switching device and a mutual capacitor, to couple the energy.

Similar to the buck-boost converter with inverting topology, the output voltage of non-isolated Ćuk converter is typically inverted, with lower or higher values with respect to the input voltage. While DC-to-DC converters usually use the inductor as a main energy-storage component, the Ćuk converter instead uses the capacitor as the main energy-storage component. It is named after Slobodan Ćuk of the California Institute of Technology, who first presented the design.

## Non-isolated Ćuk converter

There are variations on the basic Ćuk converter. For example, the coils may share a single magnetic core, which drops the output ripple, and adds efficiency. Because the power transfer flows continuously via the capacitor, this type of switcher has minimized EMI radiation. The Ćuk converter allows energy to flow bidirectionally by using a diode and a switch.

### Operating principle

A non-isolated Ćuk converter comprises two inductors, two capacitors, a switch (usually a transistor), and a diode. Its schematic can be seen in figure 1. It is an inverting converter, so the output voltage is negative with respect to the input voltage.

The main **advantage** of this converter is the continuous currents at the input and output of the converter.  The main **disadvantage** is the high current stress on the switch, as it carries the sum of the input current and the output current.

The capacitor C1 is used to transfer energy. It is connected alternately to the input and to the output of the converter *via* the commutation of the transistor and the diode (see figures 2 and 3).

The two inductors L1 and L2 are used to convert respectively the input voltage source (*Vs*) and the output voltage (*Vo*) into current sources. At a short time scale, an inductor can be considered as a current source as it maintains a constant current. This conversion is necessary because if the capacitor were connected directly to the voltage source, the current would be limited only by the parasitic resistance, resulting in high energy loss. Charging a capacitor with a current source (the inductor) prevents resistive current limiting and its associated energy loss.

As with other converters (buck converter, boost converter, buck–boost converter) the Ćuk converter can operate in either continuous or discontinuous current mode. However, unlike these converters, it can also operate in *discontinuous voltage mode* (the voltage across the capacitor drops to zero during the commutation cycle).

### Continuous mode

In steady state, the energy stored in each inductor has to remain the same at the beginning and at the end of a commutation cycle. The energy in an inductor is given by:

$E={\frac {1}{2}}LI^{2}.$

This implies that the current through each inductor has to be the same at the beginning and the end of the commutation cycle. As the evolution of the current through an inductor is related to the voltage across it:

$V_{L}=L{\frac {dI}{dt}},$

it can be seen that the average value of each inductor's voltage over a commutation period has to be zero to satisfy the steady-state requirements. (Another way to see this is to recognize that the average voltage across any inductor must be zero lest its current rise without limit.)

If we consider that the capacitors *C1* and *C2* are large enough for the voltage ripple across them to be negligible, the inductor voltages become:

- in the **off-state**, inductor *L1* is connected in series with *Vs* and *C1* (see figure 2). Therefore ${\textstyle V_{L1}=V_{s}-V_{C1}}$ . As the diode *D* is forward biased (we consider zero voltage drop), *L2* is directly connected to the output capacitor. Therefore $V_{L2}=V_{o}$
- in the **on-state**, inductor *L1* is directly connected to the input source. Therefore ${\textstyle V_{L1}=V_{s}}$ . Inductor *L2* is connected in series with *C1* and the output capacitor, so $V_{L2}=V_{o}+V_{C1}$

The converter operates in *on state* from ${\textstyle t=0}$ to ${\textstyle t=DT}$ (*D* is the duty cycle), and in *off state* from *D·T* to *T* (that is, during a period equal to ${\textstyle (1-D)T}$ ). The average values of *VL1* and *VL2* are therefore:

${\bar {V}}_{L1}=D\cdot V_{s}+\left(1-D\right)\cdot \left(V_{s}-V_{C1}\right)=V_{s}-(1-D)\cdot V_{C1}$

${\bar {V}}_{L2}=D\left(V_{o}+V_{C1}\right)+\left(1-D\right)\cdot V_{o}=V_{o}+D\cdot V_{C1}$

As both average voltage have to be zero to satisfy the steady-state conditions, using the last equation we can write:

$V_{C1}=-{\frac {V_{o}}{D}}$

So the average voltage across L1 becomes:

${\bar {V}}_{L1}=V_{s}+(1-D)\cdot {\frac {V_{o}}{D}}=0$

Which can be written as:

${\frac {V_{o}}{V_{s}}}=-{\frac {D}{1-D}}$

It can be seen that this relation is the same as that obtained for the buck–boost converter.

### Discontinuous mode

Like all DC/DC converters, Ćuk converters rely on the ability of the inductors in the circuit to provide continuous current, in much the same way a capacitor in a rectifier filter provides continuous voltage. If this inductor is too small or below the "critical inductance", then the inductor current slope will be discontinuous where the current goes to zero. This state of operation is usually not studied in much depth as it is generally not used beyond a demonstrating of why the minimum inductance is crucial, although it may occur when maintaining a standby voltage at a much lower current than the converter was designed for.

The minimum inductance is given by:

$L_{1}min={\frac {(1-D)^{2}R}{2Df_{s}}}$

Where $f_{s}$ is the switching frequency.

## Isolated Ćuk converter

Coupled inductor isolated Ćuk converter.

Integrated magnetics Ćuk converter.

For isolated version of Ćuk converter, an AC transformer and an additional capacitor must be added. Because the isolated Ćuk converter is isolated, the output-voltage polarity can be chosen freely.

As the non-isolated Ćuk converter, the isolated Ćuk converter can have an output voltage magnitude that is either greater than or less than the input voltage magnitude, even with a 1:1 AC transformer. However, the turns ratio can be controlled to reduce device stress on the input side. Additionally, the parasitic elements of the transformer, namely leakage inductance and magnetizing inductance can be used to modify the circuit into a resonant converter circuit which has much improved efficiency.

### Inductor coupling

Instead of using two discrete inductor components, many designers implement a *coupled inductor Ćuk converter*, using a single magnetic component that includes both inductors on the same core. The transformer action between the inductors inside that component gives a *coupled inductor Ćuk converter* with lower output ripple than a Ćuk converter using two independent discrete inductor components.

### Zeta converter

A zeta converter is a non-isolated, non-inverting, buck-boost power supply topology. Unlike the Ćuk and SEPIC converters, which are configured with a standard boost converter consisting of a series inductor and parallel switch, a zeta converter is configured with a buck converter constructed from a series switch and parallel inductor. The zeta converter typically uses a high-side PFET for the series switch, in contrast to the typical implementation of a low-side NFET in Ćuk and SEPIC converters. The zeta converter topology benefits from lower output voltage ripple and easier compensation than SEPIC converters. The tradeoff is higher input voltage ripple, the need for a large capacitor, and a specialised controller capable of driving a PFET.

### Single-ended primary-inductor converter (SEPIC)

A SEPIC is a non-isolated, non-inverting DC-to-DC converter topology, it is similar to the Ćuk converter, but has the output inductor and diode swapped in position and the output capacitor flipped if it is polarized, it also has the same relation of input and output voltage. The converter has the tradeoff of having discontinuous output current and therefore higher ripple on the output voltage and current

## Patents

- US Patent 4257087, filed in 1979, "*DC-to-DC switching converter with zero input and output current ripple and integrated magnetics circuits*", inventor Slobodan Ćuk.
- US Patent 4274133, filed in 1979, "*DC-to-DC Converter having reduced ripple without need for adjustments*", inventor Slobodan Ćuk and R. D. Middlebrook.
- US Patent 4184197, filed in 1977, "*DC-to-DC switching converter*", inventor Slobodan Ćuk and R. D. Middlebrook.

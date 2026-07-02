---
title: "Wheatstone bridge"
source: https://en.wikipedia.org/wiki/Wheatstone_bridge
domain: load-cells-strain
license: CC-BY-SA-4.0
tags: load cell, strain gauge, wheatstone bridge, force-sensing resistor
fetched: 2026-07-02
---

# Wheatstone bridge

A **Wheatstone bridge** is an electrical circuit used to measure an unknown electrical resistance by balancing two legs of a bridge circuit, one leg of which includes the unknown component. The primary benefit of the circuit is its ability to provide extremely accurate measurements (in contrast with something like a simple voltage divider). Its operation is similar to the original potentiometer.

The Wheatstone bridge was invented by Samuel Hunter Christie (sometimes spelled "Christy") in 1833 and improved and popularized by Sir Charles Wheatstone in 1843. One of the Wheatstone bridge's initial uses was for soil analysis and comparison.

## Operation

In the figure, *Rx* is the fixed, yet unknown, resistance to be measured. *R*1, *R*2, and *R*3 are resistors of known resistance and the resistance of *R*2 is adjustable. The resistance *R*2 is adjusted until the bridge is "balanced" and no current flows through the galvanometer *Vg*. At this point, the potential difference between the two midpoints (B and D) will be zero. Therefore the ratio of the two resistances in the known leg (*R*2 / *R*1) is equal to the ratio of the two resistances in the unknown leg (*Rx* / *R*3). If the bridge is unbalanced, the direction of the current indicates whether *R*2 is too high or too low.

At the point of balance, ${\begin{aligned}{\frac {R_{2}}{R_{1}}}&={\frac {R_{x}}{R_{3}}}\\[4pt]\Rightarrow R_{x}&={\frac {R_{2}}{R_{1}}}\cdot R_{3}\end{aligned}}$

Detecting zero current with a galvanometer can be done to extremely high precision. Therefore, if *R*1, *R*2, and *R*3 are known to high precision, then *Rx* can be measured to high precision. Very small changes in *Rx* disrupt the balance and are readily detected.

Alternatively, if *R*1, *R*2, and *R*3 are known, but *R*2 is not adjustable, the voltage difference across or current flow through the meter can be used to calculate the value of *Rx*, using Kirchhoff's circuit laws. This setup is frequently used in strain gauge and resistance thermometer measurements, as it is usually faster to read a voltage level off a meter than to adjust a resistance to zero the voltage.

## Derivation

### Quick derivation at balance

At the point of balance, both the voltage and the current between the two midpoints (B and D) are zero. Therefore, *I*1 = *I*2, *I*3 = *I**x*, *V*D = *V*B.

Because of *V*D = *V*B, then *V*DC = *V*BC and *V*AD = *V*AB.

Dividing the last two equations by members and using the above currents equalities, then ${\begin{aligned}{\frac {V_{DC}}{V_{AD}}}&={\frac {V_{BC}}{V_{AB}}}\\[4pt]\Rightarrow {\frac {I_{2}R_{2}}{I_{1}R_{1}}}&={\frac {I_{x}R_{x}}{I_{3}R_{3}}}\\[4pt]\Rightarrow R_{x}&={\frac {R_{2}}{R_{1}}}\cdot R_{3}\end{aligned}}$

### Alternative derivation at balance using voltage divider expressions

ADC and ABC form two voltage dividers, with VG equal to the difference in output voltages. Thus ${\begin{aligned}V_{DC}&=V_{BC}\\I_{2}R_{2}&=I_{x}R_{x}\\V_{AC}{\frac {R_{2}}{R_{1}+R_{2}}}&=V_{AC}{\frac {R_{x}}{R_{3}+R_{x}}}\\{\frac {R_{2}}{R_{1}+R_{2}}}&={\frac {R_{x}}{R_{3}+R_{x}}}\\{\frac {R_{1}+R_{2}}{R_{2}}}&={\frac {R_{3}+R_{x}}{R_{x}}}\\1+{\frac {R_{1}}{R_{2}}}&=1+{\frac {R_{3}}{R_{x}}}\\{\frac {R_{1}}{R_{2}}}&={\frac {R_{3}}{R_{x}}}\\\end{aligned}}$

### Full derivation using Kirchhoff's circuit laws

First, Kirchhoff's current law is used to find the currents in junctions B and D: ${\begin{aligned}I_{3}-I_{x}+I_{G}&=0\\I_{1}-I_{2}-I_{G}&=0\end{aligned}}$

Then, Kirchhoff's voltage law is used for finding the voltage in the loops ABDA and BCDB: ${\begin{aligned}(I_{3}\cdot R_{3})-(I_{G}\cdot R_{G})-(I_{1}\cdot R_{1})&=0\\(I_{x}\cdot R_{x})-(I_{2}\cdot R_{2})+(I_{G}\cdot R_{G})&=0\end{aligned}}$

When the bridge is balanced, then *I**G* = 0, so the second set of equations can be rewritten as: ${\begin{aligned}I_{3}\cdot R_{3}&=I_{1}\cdot R_{1}\quad {\text{(1)}}\\I_{x}\cdot R_{x}&=I_{2}\cdot R_{2}\quad {\text{(2)}}\end{aligned}}$

Then, equation (1) is divided by equation (2) and the resulting equation is rearranged, giving: $R_{x}={{R_{2}\cdot I_{2}\cdot I_{3}\cdot R_{3}} \over {R_{1}\cdot I_{1}\cdot I_{x}}}$

Due to *I*3 = *I**x* and *I*1 = *I*2 being proportional from Kirchhoff's current law, *I*3*I*2 / *I*1*I*x cancels out of the above equation. The desired value of *R**x* is now known to be given as: $R_{x}={{R_{3}\cdot R_{2}} \over {R_{1}}}$

On the other hand, if the resistance of the galvanometer is high enough that *I**G* is negligible, it is possible to compute *R**x* from the three other resistor values and the supply voltage (*V**S*), or the supply voltage from all four resistor values. To do so, one has to work out the voltage from each potential divider and subtract one from the other. The equations for this are: ${\begin{aligned}V_{G}&=\left({R_{2} \over {R_{1}+R_{2}}}-{R_{x} \over {R_{x}+R_{3}}}\right)V_{s}\\[6pt]R_{x}&={{R_{2}\cdot V_{s}-(R_{1}+R_{2})\cdot V_{G}} \over {R_{1}\cdot V_{s}+(R_{1}+R_{2})\cdot V_{G}}}R_{3}\end{aligned}}$ where *V**G* is the voltage of node D relative to node B.

## Significance

The Wheatstone bridge illustrates the concept of a difference measurement, which can be extremely accurate. Variations on the Wheatstone bridge can be used to measure capacitance, inductance, impedance and other quantities, such as the amount of combustible gases in a sample, with an explosimeter. The Kelvin bridge was specially adapted from the Wheatstone bridge for measuring very low resistances. In many cases, the significance of measuring the unknown resistance is related to measuring the impact of some physical phenomenon (such as force, temperature, pressure, etc.) which thereby allows the use of Wheatstone bridge in measuring those elements indirectly.

The concept was extended to alternating current measurements by James Clerk Maxwell in 1865 and further improved as Blumlein bridge by Alan Blumlein in British Patent no. 323,037, 1928.

## Modifications of the basic bridge

The Wheatstone bridge is the fundamental bridge, but there are other modifications that can be made to measure various kinds of resistances when the fundamental Wheatstone bridge is not suitable. Some of the modifications are:

- Carey Foster bridge, for measuring small resistances
- Kelvin bridge, for measuring small four-terminal resistances
- Maxwell bridge, and Wien bridge for measuring reactive components
- Anderson's bridge, for measuring the self-inductance of the circuit, an advanced form of Maxwell's bridge

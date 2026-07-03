---
title: "Admittance"
source: https://en.wikipedia.org/wiki/Admittance
domain: braid-breaker
license: CC-BY-SA-4.0
tags: braid-breaker
fetched: 2026-07-03
---

# Admittance

In electrical engineering, **admittance** is a measure of how easily a circuit or device will allow a current to flow. It is defined as the reciprocal of impedance, analogous to how conductance and resistance are defined. The SI unit of admittance is the siemens (symbol S); the older, synonymous unit is mho, and its symbol is ℧ (an upside-down uppercase omega Ω). Oliver Heaviside coined the term *admittance* in December 1887. Heaviside used Y to represent the magnitude of admittance, but it quickly became the conventional symbol for admittance itself through the publications of Charles Proteus Steinmetz. Heaviside probably chose Y simply because it is next to Z in the alphabet, the conventional symbol for impedance.

Admittance Y, measured in siemens, is defined as the inverse of impedance Z, measured in ohms:

$Y\equiv {\frac {1}{Z}}$

Resistance is a measure of the opposition of a circuit to the flow of a steady current, while impedance takes into account not only the resistance but also dynamic effects (known as reactance). Likewise, admittance is not only a measure of the ease with which a steady current can flow, but also the dynamic effects of the material's susceptance to polarization:

$Y=G+jB\,,$

where

- Y is the admittance (siemens);
- G is the conductance (siemens);
- B is the susceptance (siemens); and
- *j*2 = −1, the imaginary unit.

The dynamic effects of the material's susceptance relate to the universal dielectric response, the power law scaling of a system's admittance with frequency under alternating current conditions.

## Inversion

Parts of this article or section rely on the reader's knowledge of the complex

impedance

representation of

capacitors

and

inductors

and on knowledge of the

frequency domain

representation of signals

.

The impedance, Z, is composed of real and imaginary parts, $Z=R+jX\,,$ where

- R is the resistance (ohms); and
- X is the reactance (ohms).

$Y=Z^{-1}={\frac {1}{R+jX}}=\left({\frac {1}{R^{2}+X^{2}}}\right)\left(R-jX\right)$

Admittance, just like impedance, is a complex number, made up of a real part (the conductance, G), and an imaginary part (the susceptance, B), thus:

$Y=G+jB\,,$

where G (conductance) and B (susceptance) are given by:

${\begin{aligned}G&=\mathrm {Re} (Y)={\frac {R}{R^{2}+X^{2}}}\,,\\B&=\mathrm {Im} (Y)=-{\frac {X}{R^{2}+X^{2}}}\,.\end{aligned}}$

The magnitude and phase of the admittance are given by:

${\begin{aligned}\left|Y\right|&={\sqrt {G^{2}+B^{2}}}={\frac {1}{\sqrt {R^{2}+X^{2}}}}\\\angle Y&=\arctan \left({\frac {B}{G}}\right)=\arctan \left(-{\frac {X}{R}}\right)\,,\end{aligned}}$

where

- G is the conductance, measured in siemens; and
- B is the susceptance, also measured in siemens.

Note that (as shown above) the signs of reactances become reversed in the admittance domain; i.e. capacitive susceptance is positive and inductive susceptance is negative.

## Shunt admittance in electrical power systems modeling

In the context of electrical modeling of transformers and transmission lines, shunt components that provide paths of least resistance in certain models are generally specified in terms of their admittance. Each side of most transformer models contains shunt components which model magnetizing current and core losses. These shunt components can be referenced to the primary or secondary side. For simplified transformer analysis, admittance from shunt elements can be neglected. When shunt components have non-negligible effects on system operation, the shunt admittance must be considered. In the diagram below, all shunt admittances are referred to the primary side. The real and imaginary components of the shunt admittance, conductance and susceptance, are represented by *G*c and B, respectively.

Transmission lines can span hundreds of kilometers, over which the line's capacitance can affect voltage levels. For short length transmission line analysis, which applies to lines shorter than 80 kilometres (50 mi), this capacitance can be ignored and shunt components are not necessary in the model. Lines from 80 to about 250 kilometres (50 to about 155 mi), generally considered to be in the medium-line category, contain a shunt admittance governed by $Y=yl=j\omega Cl\,,$ where

- Y is the total shunt admittance;
- y is the shunt admittance per unit length;
- l is the length of the transmission line; and
- C is the capacitance of the line.

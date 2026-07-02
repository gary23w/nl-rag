---
title: "Kirchhoff's circuit laws"
source: https://en.wikipedia.org/wiki/Kirchhoff's_circuit_laws
domain: electronics
license: CC-BY-SA-4.0
tags: electronics, circuit, resistor, capacitor, transistor, voltage, adc, logic gate
fetched: 2026-07-02
---

# Kirchhoff's circuit laws

**Kirchhoff's circuit laws** are two equalities that deal with the current and potential difference (commonly known as voltage) in the lumped element model of electrical circuits. They were first described in 1845 by German physicist Gustav Kirchhoff. This generalized the work of Georg Ohm and preceded the work of James Clerk Maxwell. Widely used in electrical engineering, they are also called **Kirchhoff's rules** or simply **Kirchhoff's laws**. These laws can be applied in time and frequency domains and form the basis for network analysis.

Both of Kirchhoff's laws can be understood as corollaries of Maxwell's equations in the low-frequency limit. They are accurate for DC circuits, and for AC circuits at frequencies where the wavelengths of electromagnetic radiation are very large compared to the circuits.

## Kirchhoff's current law

This law, also called **Kirchhoff's first law**, or **Kirchhoff's junction rule**, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently:

> *The algebraic sum of currents in a network of conductors meeting at a point is zero.*

Recalling that current is a signed (positive or negative) quantity reflecting direction towards or away from a node, this principle can be succinctly stated as: $\sum _{i=1}^{n}I_{i}=0$ where *n* is the total number of branches with currents flowing towards or away from the node.

Kirchhoff's circuit laws were originally obtained from experimental results. However, the current law can be viewed as an extension of the conservation of charge, since charge is the product of current and the time the current has been flowing. If the net charge in a region is constant, the current law will hold on the boundaries of the region. This means that the current law relies on the fact that the net charge in the wires and components is constant.

### Uses

A matrix version of Kirchhoff's current law is the basis of most circuit simulation software, such as SPICE. The current law is used with Ohm's law to perform nodal analysis.

The current law is applicable to any lumped network irrespective of the nature of the network; whether unilateral or bilateral, active or passive.

## Kirchhoff's voltage law

This law, also called **Kirchhoff's second law**, or **Kirchhoff's loop rule**, states the following:

> *The directed sum of the potential differences (voltages) around any closed loop is zero.*

Similarly to Kirchhoff's current law, the voltage law can be stated as: $\sum _{i=1}^{n}V_{i}=0$

Here, n is the total number of voltages measured.

Derivation of Kirchhoff's voltage law

(A similar derivation can be found in Feynman's lectures.)

Consider some arbitrary circuit. Approximate the circuit with lumped elements, so that time-varying magnetic fields are contained to each component and the field in the region exterior to the circuit is negligible. Based on this assumption, the Maxwell–Faraday equation reveals that $\nabla \times \mathbf {E} =-{\frac {\partial \mathbf {B} }{\partial t}}=\mathbf {0}$ in the exterior region. If each of the components has a finite volume, then the exterior region is simply connected, and thus the electric field is conservative in that region. Therefore, for any loop in the circuit, we find that $\sum _{i}V_{i}=-\sum _{i}\int _{{\mathcal {P}}_{i}}\mathbf {E} \cdot \mathrm {d} \mathbf {l} =\oint \mathbf {E} \cdot \mathrm {d} \mathbf {l} =0$ where ${\textstyle {\mathcal {P}}_{i}}$ are paths around the *exterior* of each of the components, from one terminal to another.

Note that this derivation uses the following definition for the voltage rise from a to b : $V_{a\to b}=-\int _{{\mathcal {P}}_{a\to b}}\mathbf {E} \cdot \mathrm {d} \mathbf {l}$

However, the electric potential (and thus voltage) can be defined in other ways, such as via the Helmholtz decomposition.

### Generalization

In the low-frequency limit, the voltage drop around any loop is zero. This includes imaginary loops arranged arbitrarily in space – not limited to the loops delineated by the circuit elements and conductors. In the low-frequency limit, this is a corollary of Faraday's law of induction (which is one of Maxwell's equations).

This has practical application in situations involving "static electricity".

## Limitations

Kirchhoff's circuit laws are the result of the lumped-element model and both depend on the model being applicable to the circuit in question. When the model is not applicable, the laws do not apply.

The current law is dependent on the assumption that the net charge in any wire, junction or lumped component is constant. Whenever the electric field between parts of the circuit is non-negligible, such as when two wires are capacitively coupled, this may not be the case. This occurs in high-frequency AC circuits, where the lumped element model is no longer applicable. For example, in a transmission line, the charge density in the conductor may be constantly changing.

On the other hand, the voltage law relies on the fact that the actions of time-varying magnetic fields are confined to individual components, such as inductors. In reality, the induced electric field produced by an inductor is not confined, but the leaked fields are often negligible.

### Modelling real circuits with lumped elements

The lumped element approximation for a circuit is accurate at low frequencies. At higher frequencies, leaked fluxes and varying charge densities in conductors become significant. To an extent, it is possible to still model such circuits using parasitic components. If frequencies are too high, it may be more appropriate to simulate the fields directly using finite element modelling or other techniques.

To model circuits so that both laws can still be used, it is important to understand the distinction between *physical* circuit elements and the *ideal* lumped elements. For example, a wire is not an ideal conductor. Unlike an ideal conductor, wires can inductively and capacitively couple to each other (and to themselves), and have a finite propagation delay. Real conductors can be modeled in terms of lumped elements by considering parasitic capacitances distributed between the conductors to model capacitive coupling, or parasitic (mutual) inductances to model inductive coupling. Wires also have some self-inductance.

## Example

Assume an electric network consisting of two voltage sources and three resistors.

According to the first law: $i_{1}-i_{2}-i_{3}=0$ Applying the second law to the closed circuit *s*1, and substituting for voltage using Ohm's law gives: $-R_{2}i_{2}+{\mathcal {E}}_{1}-R_{1}i_{1}=0$ The second law, again combined with Ohm's law, applied to the closed circuit *s*2 gives: $-R_{3}i_{3}-{\mathcal {E}}_{2}-{\mathcal {E}}_{1}+R_{2}i_{2}=0$

This yields a system of linear equations in *i*1, *i*2, *i*3: ${\begin{cases}i_{1}-i_{2}-i_{3}&=0\\-R_{2}i_{2}+{\mathcal {E}}_{1}-R_{1}i_{1}&=0\\-R_{3}i_{3}-{\mathcal {E}}_{2}-{\mathcal {E}}_{1}+R_{2}i_{2}&=0\end{cases}}$ which is equivalent to ${\begin{cases}i_{1}+(-i_{2})+(-i_{3})&=0\\R_{1}i_{1}+R_{2}i_{2}+0i_{3}&={\mathcal {E}}_{1}\\0i_{1}+R_{2}i_{2}-R_{3}i_{3}&={\mathcal {E}}_{1}+{\mathcal {E}}_{2}\end{cases}}$ Assuming ${\begin{aligned}R_{1}&=100\Omega ,&R_{2}&=200\Omega ,&R_{3}&=300\Omega ,\\{\mathcal {E}}_{1}&=3{\text{V}},&{\mathcal {E}}_{2}&=4{\text{V}}\end{aligned}}$ the solution is ${\begin{cases}i_{1}={\frac {1}{1100}}{\text{A}}\\[6pt]i_{2}={\frac {4}{275}}{\text{A}}\\[6pt]i_{3}=-{\frac {3}{220}}{\text{A}}\end{cases}}$

The current *i*3 has a negative sign which means the assumed direction of *i*3 was incorrect and *i*3 is actually flowing in the direction opposite to the red arrow labeled *i*3. The current in *R*3 flows from left to right.

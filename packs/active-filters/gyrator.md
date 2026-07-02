---
title: "Gyrator"
source: https://en.wikipedia.org/wiki/Gyrator
domain: active-filters
license: CC-BY-SA-4.0
tags: active filter, Sallen-Key topology, state variable filter, gyrator circuit
fetched: 2026-07-02
---

# Gyrator

A **gyrator** is a passive, linear, lossless, two-port electrical network element proposed in 1948 by Bernard D. H. Tellegen as a hypothetical fifth linear element after the resistor, capacitor, inductor and ideal transformer. Unlike the four conventional elements, the gyrator is non-reciprocal. Gyrators permit network realizations of two-(or-more)-port devices which cannot be realized with just the four conventional elements. In particular, gyrators make possible network realizations of isolators and circulators. Gyrators do not however change the range of one-port devices that can be realized. Although the gyrator was conceived as a fifth linear element, its adoption makes both the ideal transformer and either the capacitor or inductor redundant. Thus the number of necessary linear elements is in fact reduced to three. Circuits that function as gyrators can be built with transistors and op-amps using feedback.

Tellegen invented a circuit symbol for the gyrator and suggested a number of ways in which a practical gyrator might be built.

An important property of a gyrator is that it inverts the current–voltage characteristic of an electrical component or network. In the case of linear elements, the impedance is also inverted. In other words, a gyrator can make a capacitive circuit behave inductively, a series LC circuit behave like a parallel LC circuit, and so on. It is primarily used in active filter design and miniaturization.

## Behavior

An ideal gyrator is a linear two-port device which couples the current on one port to the voltage on the other and conversely. The instantaneous currents and instantaneous voltages are related by

$v_{2}=Ri_{1},$

$v_{1}=-Ri_{2},$

where R is the *gyration resistance* of the gyrator.

The gyration resistance (or equivalently its reciprocal the *gyration conductance*) has an associated direction indicated by an arrow on the schematic diagram. By convention, the given gyration resistance or conductance relates the voltage on the port at the head of the arrow to the current at its tail. The voltage at the tail of the arrow is related to the current at its head by *minus* the stated resistance. Reversing the arrow is equivalent to negating the gyration resistance, or to reversing the polarity of either port.

Although a gyrator is characterized by its resistance value, it is a lossless component. From the governing equations, the instantaneous power into the gyrator is identically zero:

$P=v_{1}i_{1}+v_{2}i_{2}=(-Ri_{2})i_{1}+(Ri_{1})i_{2}\equiv 0.$

A gyrator is an entirely non-reciprocal device, and hence is represented by antisymmetric impedance and admittance matrices:

$Z={\begin{bmatrix}0&-R\\R&0\end{bmatrix}},\quad Y={\begin{bmatrix}0&G\\-G&0\end{bmatrix}},\quad G={\frac {1}{R}}.$

Customary

ANSI Y32

& IEC standards

Two versions of the symbol used to represent a gyrator in single-line diagrams. A 180° (π

radian) phase shift occurs for signals travelling in the direction of the arrow (or longer arrow), with no phase shift in the reverse direction.

If the gyration resistance is chosen to be equal to the characteristic impedance of the two ports (or to their geometric mean if these are not the same), then the scattering matrix for the gyrator is

$S={\begin{bmatrix}0&-1\\1&0\end{bmatrix}},$

which is likewise antisymmetric. This leads to an alternative definition of a gyrator: a device which transmits a signal unchanged in the forward (arrow) direction, but reverses the polarity of the signal travelling in the backward direction (or equivalently, 180° phase-shifts the backward-travelling signal). The symbol used to represent a gyrator in one-line diagrams (where a waveguide or transmission line is shown as a single line rather than as a pair of conductors), reflects this one-way phase shift.

As with a quarter-wave transformer, if one port of a gyrator is terminated with a linear load, then the other port presents an impedance inversely proportional to the impedance of that load:

$Z_{\text{in}}={\frac {R^{2}}{Z_{\text{load}}}}.$

A generalization of the gyrator is conceivable, in which the forward and backward gyration conductances have different magnitudes, so that the admittance matrix is

$Y={\begin{bmatrix}0&G_{1}\\-G_{2}&0\end{bmatrix}}.$

However, this no longer represents a passive device.

## Name

Tellegen named the element *gyrator* as a blend of *gyroscope* and the common device suffix *-tor* (as in resistor, capacitor, transistor etc.) The -*tor* ending is even more suggestive in Tellegen's native Dutch, where the related element *transformer* is called *transformator*. The gyrator is related to the gyroscope by an analogy in its behaviour.

The analogy with the gyroscope is due to the relationship between the torque and angular velocity of the gyroscope on the two axes of rotation. A torque on one axis will produce a proportional change in angular velocity on the other axis and conversely. A mechanical–electrical analogy of the gyroscope making torque and angular velocity the analogs of voltage and current results in the electrical gyrator.

## Relationship to the ideal transformer

An ideal gyrator is similar to an ideal transformer in being a linear, lossless, passive, memoryless two-port device. However, whereas a transformer couples the voltage on port 1 to the voltage on port 2, and the current on port 1 to the current on port 2, the gyrator cross-couples voltage to current and current to voltage. Cascading two gyrators achieves a voltage-to-voltage coupling identical to that of an ideal transformer.

Cascaded gyrators of gyration resistance $R_{1}$ and $R_{2}$ are equivalent to a transformer of turns ratio $R_{1}:R_{2}$ . Cascading a transformer and a gyrator, or equivalently cascading three gyrators produces a single gyrator of gyration resistance $R_{1}R_{3}/R_{2}$ .

From the point of view of network theory, transformers are redundant when gyrators are available. Anything that can be built from resistors, capacitors, inductors, transformers and gyrators, can also be built using just resistors, gyrators and inductors (or capacitors).

### Magnetic circuit analogy

In the two-gyrator equivalent circuit for a transformer, described above, the gyrators may be identified with the transformer windings, and the loop connecting the gyrators with the transformer magnetic core. The electric current around the loop then corresponds to the rate-of-change of magnetic flux through the core, and the electromotive force (EMF) in the loop due to each gyrator corresponds to the magnetomotive force (MMF) in the core due to each winding.

The gyration resistances are in the same ratio as the winding turn-counts, but collectively of no particular magnitude. So, choosing an arbitrary conversion factor of r ohms per turn, a loop EMF V is related to a core MMF ${\mathcal {F}}$ by

$V=r{\mathcal {F}},$

and the loop current I is related to the core flux-rate ${\dot {\Phi }}$ by

$I={\frac {1}{r}}{\frac {\partial }{\partial t}}\Phi .$

The core of a real, non-ideal, transformer has finite permeance ${\mathcal {P}}$ (non-zero reluctance ${\mathcal {R}}$ ), such that the flux and total MMF satisfy

$\Phi ={\frac {\mathcal {F}}{\mathcal {R}}}={\mathcal {P}}{\mathcal {F}},$

which means that in the gyrator loop

$I={\frac {\mathcal {P}}{r^{2}}}{\frac {\partial }{\partial t}}V$

corresponding to the introduction of a series capacitor

$C={\frac {1}{r^{2}}}{\mathcal {P}}$

in the loop. This is Buntenbach's capacitance–permeance analogy, or the gyrator–capacitor model of magnetic circuits.

## Application

### Simulated inductor

A gyrator can be used to transform a load capacitance into an inductance. At low frequencies and low powers, the behaviour of the gyrator can be reproduced by a small op-amp circuit. This supplies a means of providing an inductive element in a small electronic circuit or integrated circuit. Before the invention of the transistor, coils of wire with large inductance might be used in electronic filters. An inductor can be replaced by a much smaller assembly containing a capacitor, operational amplifiers or transistors, and resistors. This is especially useful in integrated circuit technology.

#### Operation

In the circuit shown, one port of the gyrator is between the input terminal and ground, while the other port is terminated with the capacitor. The circuit works by inverting and multiplying the effect of the capacitor in an RC differentiating circuit, where the voltage across the resistor *R* behaves through time in the same manner as the voltage across an inductor. The op-amp follower buffers this voltage and applies it back to the input through the resistor *RL*. The desired effect is an impedance of the form of an ideal inductor *L* with a series resistance *RL*: $Z=R_{L}+j\omega L.$

From the diagram, the input impedance of the op-amp circuit is $Z_{\text{in}}=(R_{\text{L}}+j\omega R_{L}RC)\parallel \left(R+{\frac {1}{j\omega C}}\right).$

With *RLRC* = *L*, it can be seen that the impedance of the simulated inductor is the desired impedance in parallel with the impedance of the RC circuit. In typical designs, *R* is chosen to be sufficiently large while $\omega RC\approx 1$ such that the first term dominates; thus, the *RC*-circuit's effect on input impedance is negligible:

$Z_{\text{in}}\approx R_{L}+j\omega R_{L}RC.$

This is the same as a resistance *RL* in series with an inductance *L* = *RLRC*. There is a practical limit on the minimum value that *RL* can take, determined by the current output capability of the op-amp.

The impedance cannot increase indefinitely with frequency, and eventually the second term limits the impedance to the value of *R*.

#### Comparison with actual inductors

Simulated elements are electronic circuits that imitate actual elements. Simulated elements cannot replace physical inductors in all the possible applications as they do not possess all the unique properties of physical inductors.

**Magnitudes.** In typical applications, both the inductance and the resistance of the gyrator are much greater than that of a physical inductor. Gyrators can be used to create inductors from the microhenry range up to the megahenry range. Physical inductors are typically limited to tens of henries, and have parasitic series resistances from hundreds of microhms through the low kilohm range. The parasitic resistance of a gyrator depends on the topology, but with the topology shown, series resistances will typically range from tens of ohms through hundreds of kilohms.

**Quality.** Physical capacitors are often much closer to "ideal capacitors" than physical inductors are to "ideal inductors". Because of this, a synthesized inductor realized with a gyrator and a capacitor may, for certain applications, be closer to an "ideal inductor" than any (practical) physical inductor can be. Thus, use of capacitors and gyrators may improve the quality of filter networks that would otherwise be built using inductors. Also, the Q factor of a synthesized inductor can be selected with ease. The Q of an LC filter can be either lower or higher than that of an actual LC filter – for the same frequency, the inductance is much higher, the capacitance much lower, but the resistance also higher. Gyrator inductors typically have higher accuracy than physical inductors, due to the lower cost of precision capacitors than inductors.

**Energy storage.** Simulated inductors do not have the inherent energy storing properties of the real inductors and this limits the possible power applications. The circuit cannot respond like a real inductor to sudden input changes (it does not produce a high-voltage back EMF); its voltage response is limited by the power supply. Since gyrators use active circuits, they only function as a gyrator within the power supply range of the active element. Hence gyrators are usually not very useful for situations requiring simulation of the 'flyback' property of inductors, where a large voltage spike is caused when current is interrupted. A gyrator's transient response is limited by the bandwidth of the active device in the circuit and by the power supply.

**Externalities.** Simulated inductors do not react to external magnetic fields and permeable materials the same way that real inductors do. They also don't create magnetic fields (and induce currents in external conductors) the same way that real inductors do. This limits their use in applications such as sensors, detectors and transducers.

**Grounding.** The fact that one side of the simulated inductor is grounded restricts the possible applications (real inductors are floating). This limitation may preclude its use in some low-pass and notch filters. However the gyrator can be used in a floating configuration with another gyrator so long as the floating "grounds" are tied together. This allows for a floating gyrator, but the inductance simulated across the input terminals of the gyrator pair must be cut in half for each gyrator to ensure that the desired inductance is met (the impedance of inductors in series adds together). This is not typically done as it requires even more components than in a standard configuration and the resulting inductance is a result of two simulated inductors, each with half of the desired inductance.

#### Applications

The primary application for a gyrator is to reduce the size and cost of a system by removing the need for bulky, heavy and expensive inductors. For example, RLC bandpass filter characteristics can be realized with capacitors, resistors and operational amplifiers without using inductors. Thus graphic equalizers can be achieved with capacitors, resistors and operational amplifiers without using inductors because of the invention of the gyrator.

Gyrator circuits are extensively used in telephony devices that connect to a POTS system. This has allowed telephones to be much smaller, as the gyrator circuit carries the DC part of the line loop current, allowing the transformer carrying the AC voice signal to be much smaller due to the elimination of DC current through it. Gyrators are used in most DAAs (data access arrangements). Circuitry in telephone exchanges has also been affected with gyrators being used in line cards. Gyrators are also widely used in hi-fi for graphic equalizers, parametric equalizers, discrete bandstop and bandpass filters such as rumble filters), and FM pilot tone filters.

There are many applications where it is not possible to use a gyrator to replace an inductor:

- High voltage systems utilizing flyback (beyond working voltage of transistors/amplifiers)
- RF systems commonly use real inductors as they are quite small at these frequencies and integrated circuits to build an active gyrator are either expensive or non-existent. However, passive gyrators are possible.
- Power conversion, where a coil is used as energy storage.

## Impedance inversion

In microwave circuits, impedance inversion can be achieved using a quarter-wave impedance transformer instead of a gyrator. The quarter-wave transformer is a passive device and is far simpler to build than a gyrator. Unlike the gyrator, the transformer is a reciprocal component. The transformer is an example of a distributed-element circuit.

## In other energy domains

Analogs of the gyrator exist in other energy domains. The analogy with the mechanical gyroscope has already been pointed out in the name section. Also, when systems involving multiple energy domains are being analysed as a unified system through analogies, such as mechanical-electrical analogies, the transducers between domains are considered either transformers or gyrators depending on which variables they are translating. Electromagnetic transducers translate current into force and velocity into voltage. In the impedance analogy however, force is the analog of voltage and velocity is the analog of current, thus electromagnetic transducers are gyrators in this analogy. On the other hand, piezoelectric transducers are transformers (in the same analogy).

Thus another possible way to make an electrical passive gyrator is to use transducers to translate into the mechanical domain and back again, much as is done with mechanical filters. Such a gyrator can be made with a single mechanical element by using a multiferroic material using its magnetoelectric effect. For instance, a current carrying coil wound around a multiferroic material will cause vibration through the multiferroic's magnetostrictive property. This vibration will induce a voltage between electrodes embedded in the material through the multiferroic's piezoelectric property. The overall effect is to translate a current into a voltage resulting in gyrator action.

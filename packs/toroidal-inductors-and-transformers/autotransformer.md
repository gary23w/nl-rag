---
title: "Autotransformer"
source: https://en.wikipedia.org/wiki/Autotransformer
domain: toroidal-inductors-and-transformers
license: CC-BY-SA-4.0
tags: toroidal inductors and transformers
fetched: 2026-07-03
---

# Autotransformer

In electrical engineering, an **autotransformer** is an electrical transformer with only one winding. The "auto" (Greek for "self") prefix refers to the single coil acting alone. In an autotransformer, portions of the same winding act as both the primary winding and secondary winding sides of the transformer. In contrast, an ordinary transformer has separate primary and secondary windings that are not connected by an electrically conductive path between them.

The autotransformer winding has at least three electrical connections to the winding. Since part of the winding does "double duty", autotransformers have the advantages of often being smaller, lighter, and cheaper than typical dual-winding transformers, but the disadvantage of not providing electrical isolation between primary and secondary circuits. Other advantages of autotransformers include lower leakage reactance, lower losses, lower excitation current, and increased VA rating for a given size and mass.

An example of an application of an autotransformer is one style of traveler's voltage converter, that allows 230-volt devices to be used on 120-volt supply circuits, or the reverse. An autotransformer with multiple taps may be applied to adjust the voltage at the end of a long distribution circuit to correct for excess voltage drop; when automatically controlled, this is one example of a voltage regulator.

## Operation

An autotransformer has a single winding with two end terminals and one or more terminals at intermediate tap points. It is a transformer in which the primary and secondary coils have part of their turns in common. The portion of the winding shared by both the primary and secondary is the common section. The portion of the winding not shared by both the primary and secondary is the series section. The primary voltage is applied across two of the terminals. The secondary voltage is taken from two terminals, one terminal of which is usually in common with a primary voltage terminal.

Since the volts-per-turn is the same in both windings, each develops a voltage in proportion to its number of turns. In an autotransformer, part of the output current flows directly from the input to the output (through the series section), and only part is transferred inductively (through the common section), allowing a smaller, lighter, cheaper core to be used as well as requiring only a single winding. However the voltage and current ratio of autotransformers can be formulated the same as other two-winding transformers:

${\frac {V_{1}}{V_{2}}}={\frac {N_{1}}{N_{2}}}=a$

where $0<V_{2}<V_{1}$ .

The ampere-turns provided by the series section of the winding:

$F_{S}=(N_{1}-N_{2})I_{1}=\left(1-{\frac {1}{a}}\right)N_{1}I_{1}$

The ampere-turns provided by the common section of the winding:

$F_{C}=N_{2}(I_{2}-I_{1})={\frac {N_{1}}{a}}(I_{2}-I_{1})$

For ampere-turn balance, $F_{S}=F_{C}$ :

$\left(1-{\frac {1}{a}}\right)N_{1}I_{1}={\frac {N_{1}}{a}}(I_{2}-I_{1})$

Therefore:

${\frac {I_{1}}{I_{2}}}={\frac {1}{a}}={\frac {N_{2}}{N_{1}}}$

One end of the winding is usually connected in common to both the voltage source and the electrical load. The other end of the source and load are connected to taps along the winding. Different taps on the winding correspond to different voltages, measured from the common end. In a step-down transformer the source is usually connected across the entire winding while the load is connected by a tap across only a portion of the winding. In a step-up transformer, conversely, the load is attached across the full winding while the source is connected to a tap across a portion of the winding. For a step-up transformer, the subscripts in the above equations are reversed where, in this situation, $N_{2}$ and $V_{2}$ are greater than $N_{1}$ and $V_{1}$ , respectively.

As in a two-winding transformer, the ratio of secondary to primary voltages is equal to the ratio of the number of turns of the winding they connect to. For example, connecting the load between the middle of the winding and the common terminal end of the winding of the autotransformer will result in the output load voltage being 50% of the primary voltage. Depending on the application, that portion of the winding used solely in the higher-voltage (lower current) portion may be wound with wire of a smaller gauge, though the entire winding is directly connected.

If one of the center-taps is used for the ground, then the autotransformer can be used as a balun to convert a balanced line (connected to the two end taps) to an unbalanced line (the side with the ground).

An autotransformer does not provide electrical isolation between its windings as an ordinary transformer does; if the neutral side of the input is not at ground voltage, the neutral side of the output will not be either. A failure of the isolation of the windings of an autotransformer can result in full input voltage applied to the output. Also, a break in the part of the winding that is used as both primary and secondary will result in the transformer acting as an inductor in series with the load (which under light load conditions may result in nearly full input voltage being applied to the output). These are important safety considerations when deciding to use an autotransformer in a given application.

Because it requires both fewer windings and a smaller core, an autotransformer for power applications is typically lighter and less costly than a two-winding transformer, up to a voltage ratio of about 3:1; beyond that range, a two-winding transformer is usually more economical.

In three phase power transmission applications, autotransformers have the limitations of not suppressing harmonic currents and as acting as another source of ground fault currents. A large three-phase autotransformer may have a "buried" delta winding, not connected to the outside of the tank, to absorb some harmonic currents.

In practice, losses mean that both standard transformers and autotransformers are not perfectly reversible; one designed for stepping down a voltage will deliver slightly less voltage than required if it is used to step up. The difference is usually slight enough to allow reversal where the actual voltage level is not critical.

Like multiple-winding transformers, autotransformers use time-varying magnetic fields to transfer power. They require alternating currents to operate properly and will not function on direct current. Because the primary and secondary windings are electrically connected, an autotransformer will allow current to flow between windings and therefore does not provide AC or DC isolation.

## Applications

### Power transmission and distribution

Autotransformers are frequently used in power applications to interconnect systems operating at different voltage classes, for example 132 kV to 66 kV for transmission. Another application in industry is to adapt machinery built (for example) for 480 V supplies to operate on a 600 V supply. They are also often used for providing conversions between the two common domestic mains voltage bands in the world (100–130 V and 200–250 V). The links between the UK 400 kV and 275 kV "Super Grid" networks are normally three phase autotransformers with taps at the common neutral end. On long rural power distribution lines, special autotransformers with automatic tap-changing equipment are inserted as voltage regulators, so that customers at the far end of the line receive the same average voltage as those closer to the source. The variable ratio of the autotransformer compensates for the voltage drop along the line.

A special form of auto transformer called a *zig zag* is used to provide grounding on three-phase systems that otherwise have no connection to ground. A zig-zag transformer provides a path for current that is common to all three phases (so-called zero sequence current).

### Audio system

In audio applications, tapped autotransformers are used to adapt speakers to constant-voltage audio distribution systems, and for impedance matching such as between a low-impedance microphone and a high-impedance amplifier input.

### Railways

In railway applications, it is common to power the trains at 25 kV AC. To increase the distance between electricity Grid feeder points, they can be arranged to supply a split-phase 25–0–25 kV feed with the third wire (opposite phase) out of reach of the train's overhead collector pantograph. The 0 V point of the supply is connected to the rail while one 25 kV point is connected to the overhead contact wire. At frequent (about 10 km) intervals, an autotransformer links the contact wire to rail and to the second (antiphase) supply conductor. This system increases usable transmission distance, reduces induced interference into external equipment and reduces cost. A variant is occasionally seen where the supply conductor is at a different voltage to the contact wire with the autotransformer ratio modified to suit.

### Autotransformer starter

Autotransformers can be used as a method of soft starting induction motors. One of the designs of such a starter is the Korndörfer autotransformer starter.

## History

The autotransformer starter was invented in 1908, by Max Korndorfer of Berlin. He filed the application with the U.S. Patent office in May 1908 and was granted the patent US 1,096,922 in May 1914. Max Korndorfer assigned his patent to the General Electric Company.

An induction motor draws very high starting current during its acceleration to full rated speed, typically 6 to 10 times the full load current. Reduced starting current is desirable where the electrical grid is not of sufficient capacity, or where the driven load cannot withstand high starting torque. One basic method to reduce the starting current is with a reduced voltage autotransformer with taps at 50%, 65% and 80% of the applied line voltage; once the motor is started the autotransformer is switched out of circuit.

## Variable autotransformers

By exposing part of the winding coils and making the secondary connection through a sliding brush, a continuously variable turns ratio can be obtained, allowing for very smooth control of output voltage. The output voltage is not limited to the discrete voltages represented by actual number of turns. The voltage can be smoothly varied between turns as the brush has a relatively high resistance (compared with a metal contact) and the actual output voltage is a function of the relative area of brush in contact with adjacent windings. The relatively high resistance of the brush also prevents it from acting as a short circuited turn when it contacts two adjacent turns. Typically the primary connection connects to only a part of the winding allowing the output voltage to be varied smoothly from zero to above the input voltage and thus allowing the device to be used for testing electrical equipment at the limits of its specified voltage range.

The output voltage adjustment can be manual or automatic. The manual type is applicable only for relatively low voltage and is known as a variable AC transformer (often referred to by the trademark name Variac). These are often used in repair shops for testing devices under different voltages or to simulate abnormal line voltages.

The type with automatic voltage adjustment can be used as automatic voltage regulator, to maintain a steady voltage at the customers' service during a wide range of line and load conditions. Another application is a lighting dimmer that doesn't produce the EMI typical of most thyristor dimmers.

### Variac trademark

From 1934 to 2002, **Variac** was a U.S. trademark of General Radio for a variable autotransformer intended to conveniently vary the output voltage for a steady AC input voltage. In 2004, Instrument Service Equipment applied for and obtained the *Variac* trademark for the same type of product. The term *variac* has become a genericised trademark, being used to refer to a variable autotransformer.

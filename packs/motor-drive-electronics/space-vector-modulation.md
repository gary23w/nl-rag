---
title: "Space vector modulation"
source: https://en.wikipedia.org/wiki/Space_vector_modulation
domain: motor-drive-electronics
license: CC-BY-SA-4.0
tags: motor controller, variable-frequency drive, space vector modulation, motor drive
fetched: 2026-07-02
---

# Space vector modulation

**Space vector modulation** (**SVM**) is an algorithm for the control of pulse-width modulation (PWM), invented by Gerhard Pfaff, Alois Weschta, and Albert Wick in 1982. It is used for the creation of alternating current (AC) waveforms; most commonly to drive 3 phase AC powered motors at varying speeds from DC using multiple class-D amplifiers. There are variations of SVM that result in different quality and computational requirements. One active area of development is in the reduction of total harmonic distortion (THD) created by the rapid switching inherent to these algorithms.

## Principle

A three-phase inverter as shown to the right converts a DC supply, via a series of switches, to three output legs which could be connected to a three-phase motor.

The switches must be controlled so that at no time are both switches in the same leg turned on or else the DC supply would be shorted. This requirement may be met by the complementary operation of the switches within a leg. i.e. if A+ is on then A− is off and vice versa. This leads to eight possible switching vectors for the inverter, V0 through V7 with six active switching vectors and two zero vectors.

Vector

A

+

B

+

C

+

A

−

B

−

C

−

V

AB

V

BC

V

CA

V

0

= {000}

OFF

OFF

OFF

ON

ON

ON

0

0

0

zero vector

V

1

= {100}

ON

OFF

OFF

OFF

ON

ON

+V

dc

0

−V

dc

active vector

V

2

= {110}

ON

ON

OFF

OFF

OFF

ON

0

+V

dc

−V

dc

active vector

V

3

= {010}

OFF

ON

OFF

ON

OFF

ON

−V

dc

+V

dc

0

active vector

V

4

= {011}

OFF

ON

ON

ON

OFF

OFF

−V

dc

0

+V

dc

active vector

V

5

= {001}

OFF

OFF

ON

ON

ON

OFF

0

−V

dc

+V

dc

active vector

V

6

= {101}

ON

OFF

ON

OFF

ON

OFF

+V

dc

−V

dc

0

active vector

V

7

= {111}

ON

ON

ON

OFF

OFF

OFF

0

0

0

zero vector

Note that looking down the columns for the active switching vectors V1-6, the output voltages vary as a pulsed sinusoid, with each leg offset by 120 degrees of phase angle.

To implement space vector modulation, a reference signal Vref is sampled with a frequency fs (Ts = 1/fs). The reference signal may be generated from three separate phase references using the αβγ transform. The reference vector is then synthesized using a combination of the two adjacent active switching vectors and one or both of the zero vectors. Various strategies of selecting the order of the vectors and which zero vector(s) to use exist. Strategy selection will affect the harmonic content and the switching losses.

More complicated SVM strategies for the unbalanced operation of four-leg three-phase inverters do exist. In these strategies the switching vectors define a 3D shape (a hexagonal prism in $\alpha \beta \gamma$ coordinates or a dodecahedron in abc coordinates) rather than a 2D hexagon. General SVM techniques are also available for converters with any number of legs and levels.

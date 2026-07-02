---
title: "Gilbert cell"
source: https://en.wikipedia.org/wiki/Gilbert_cell
domain: mixer-rf
license: CC-BY-SA-4.0
tags: frequency mixer, Gilbert cell, image frequency, superheterodyne receiver
fetched: 2026-07-02
---

# Gilbert cell

In electronics, the **Gilbert cell** is a type of frequency mixer. It produces output signals proportional to the product of two input signals. Such circuits are widely used for frequency conversion in radio systems. The advantage of this circuit is the output current is an accurate multiplication of the (differential) base currents of both inputs. As a mixer, its balanced operation cancels out many unwanted mixing products, resulting in a "cleaner" output. Gilbert cells can also be used as variable-gain amplifiers (VGA).

It is a generalized case of an early circuit first used by Howard Jones in 1963, invented independently and greatly augmented by Barrie Gilbert in 1967. It is a specific example of "translinear" design, a current-mode approach to analog circuit design. The specific property of this cell is that the differential output current is a precise algebraic product of its two differential analog current inputs.

## Function

|   |   |   |
|---|---|---|
| Howard Jones, 1963 | Gilbert, 1968 (beta independent) | Gilbert, later (beta dependent) |

There is little difference between the Jones cell and the translinear multiplier in this topology. In both forms, two differential amplifier stages are formed by emitter-coupled transistor pairs (Q1/Q4, Q3/Q5) whose outputs are connected (currents summed) with opposite phases. The emitter junctions of these amplifier stages are fed by the collectors of a third differential pair (Q2/Q6). The output currents of Q2/Q6 become emitter currents for the differential amplifiers. Simplified, the output current of an individual transistor is given by ic = gm vbe. Its transconductance gm is (at T = 300 K) about gm = 40 IC. Combining these equations gives ic = 40 IC vbe,lo. However, IC here is given by vbe,rf gm,rf. Hence ic = 40 vbe,lo vbe,rf gm,rf, which is a multiplication of vbe,lo and vbe,rf. Combining the two different stages output currents yields four-quadrant operation.

The Jones topology can be generalized by "stacking" any number of pairs of differential pairs (whose two differential inputs and two differential outputs are likewise connected out-of-phase and in-phase, respectively) on top of a conventional Jones cell, resulting in a circuit that retains the balanced nature of the Jones cell's operation. Specifically, the differential output current would now be proportional to the product of an *arbitrary* number of differential inputs (or some translinear function thereof). However, the utility of this generalization in practical microelectronics settings is limited due to the large voltage headroom needed to keep all of the transistors in the proper (forward-active) region of operation.

However, in the cells later invented by Gilbert, shown in the figure on the right, there are two additional diode-connected transistors (labeled as V1 and V2). This is a crucial difference because they generate the logarithm of the associated differential (X) input current so that the exponential characteristics of the following transistors result in an ideally perfect multiplication of these input currents with the remaining pair of (Y) currents. This additional diode cell topology is typically used when a low distortion voltage-controlled amplifier (VCA) is required. This topology is rarely used in RF mixer/modulator applications for various reasons, one being that the linearity advantage of the top linearized cascode is minimal due to the near-square wave drive signals to these bases. The drive is less likely to be a fast-edge squarewave at very high frequencies when there may be some advantage in the linearization.

Nowadays, functionally similar circuits can be constructed using CMOS or BiCMOS cells.

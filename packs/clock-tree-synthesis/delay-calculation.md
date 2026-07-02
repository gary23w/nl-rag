---
title: "Delay calculation"
source: https://en.wikipedia.org/wiki/Delay_calculation
domain: clock-tree-synthesis
license: CC-BY-SA-4.0
tags: clock tree synthesis, clock distribution network, clock skew balancing, h-tree topology
fetched: 2026-07-02
---

# Delay calculation

**Delay calculation** is the term used in integrated circuit design for the calculation of the gate delay of a single logic gate and the wires attached to it. By contrast, static timing analysis computes the delays of entire paths, using delay calculation to determine the delay of each gate and wire.

There are many methods used for delay calculation for the gate itself. The choice depends primarily on the speed and accuracy required:

- Circuit simulators such as SPICE may be used. This is the most accurate, but slowest, method.
- Two dimensional tables are commonly used in applications such as logic synthesis, placement and routing. These tables take an output load and input slope and generate a circuit delay and output slope. The values of the tables are usually computed using circuit simulators in a procedure referred to as *characterization* or *standard cell characterization*. A common file format for storing the lookup tables is the *Liberty* format.
- A very simple model called the *K-factor* model is sometimes used. This approximates the delay as a constant plus *k* times the load capacitance.
- A more complex model called Delay Calculation Language, or DCL, calls a user-defined program whenever a delay value is required. This allows arbitrarily complex models to be represented, but raises significant software engineering issues.
- Logical effort provides a simple delay calculation that accounts for gate sizing and is analytically tractable.

Similarly, there are many ways to calculate the delay of a wire. The delay of a wire will normally be different for each destination. In order to increase accuracy (and decrease speed), the most common methods are:

- *Lumped C*. The entire wire capacitance is applied to the gate output, and the delay through the wire itself is ignored.
- Elmore delay is a simple approximation, often used where speed of calculation is important but the delay through the wire itself cannot be ignored. It uses the R and C values of the wire segments in a simple calculation. The delay of each wire segment is the R of that segment times the downstream C. Then all delays are summed from the root. (This assumes the network is tree-structured, true of most nets in chips. In this case, the Elmore delay can be calculated in time O(N) with two tree traversals. If the network is not tree-structured the Elmore delay can still be computed, but involves matrix calculations.)
- *Moment matching* is a more sophisticated analytical method. It can be thought of as either matching multiple moments in the time domain or finding a good rational approximation (a Padé approximation) in the frequency domain. (These are very closely related - see Laplace transform.) It can also be considered a generalization of Elmore delay, which matches the first moment in the time domain (or computes a one-pole approximation in the frequency domain - they are equivalent). The first use of this technique, AWE, used explicit moment matching. Newer methods such as PRIMA and PVL use implicit moment matching, based on Krylov subspaces. These methods are slower than Elmore but more accurate. Compared to circuit simulation they are faster but less accurate.
- Circuit simulators such as SPICE may be used. This is usually the most accurate, but slowest, method.
- DCL, as defined above, can be used for interconnecting as well as gate delay.

Often, it makes sense to combine the calculation of a gate and all the wires connected to its output. This combination is often called the *stage delay*.

The delay of a wire or logic gate may also depend on the behaviour of the nearby components. This is one of the main effects that is analyzed during signal integrity checks.

## Delay calculation in digital design

In the context of semi-custom digital design, pre-characterized digital information is often abstracted in the form of the above-mentioned 2-D look-up table (LUT). The idea behind the semi-custom design method is to use blocks of pre-built and tested components to build something larger, say, a chip.

In this context, the blocks are logic gates such as NAND, OR, AND, etc. Although, in reality, these gates will be composed of transistors, a semi-custom engineer will only be aware of the delay information from the input pin to the output pin, called a timing arc. The 2D table represents the variability of the gate's delay concerning the two independent variables, usually the rate of change of the signal at the input and the load at the output pin. These two variables are called slew and load in design parlance.

A static timing analysis engine will first calculate the delay of the individual cells and string them together to do further analysis.

## Statistical delay calculation

As chip dimensions get smaller, the delays of both gates and wires may need to be treated as statistical estimates instead of deterministic quantities. For gates, this requires extensions to the library formats. For wires, this requires methods that can calculate the means and distributions of wire delays. In both cases, it is critical to capture the dependence on the underlying variables, such as threshold voltage and metal thickness, since these result in correlations among the delays of nearby components. See for an early example.

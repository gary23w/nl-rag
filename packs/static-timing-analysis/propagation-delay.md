---
title: "Propagation delay"
source: https://en.wikipedia.org/wiki/Propagation_delay
domain: static-timing-analysis
license: CC-BY-SA-4.0
tags: static timing analysis, timing closure, clock skew, propagation delay
fetched: 2026-07-02
---

# Propagation delay

**Propagation delay** is the time duration taken for a signal to reach its destination, for example in the electromagnetic field, a wire, gas, fluid or solid body.

## Physics

- An electromagnetic wave travelling through a medium has a propagation delay determined by the speed of light in that particular medium, or ca.(circa/approx) 1 nanosecond per 29.98 centimetres (11.80 in) in a vacuum.
- An electric signal travelling through a wire has a propagation delay of ca. 1 nanosecond per 15 centimetres (5.9 in).

See also radio propagation, velocity factor, signal velocity and mechanical wave.

## Electronics

Logic gates can have a **gate delay** ranging from picoseconds to more than 10 nanoseconds, depending on the technology being used. It is the time between the gate input becoming stable and the gate output becoming stable. Manufacturers often refer to the time from the input changing to 50% of its final input level, to the output reaching 50% of its final output level; this may depend on the direction of the level change, in which case separate fall and rise delays tPHL and tPLH or tf and tr are given.

Reducing gate delays allows digital circuits to process data at a faster rate and improve overall performance. Determining the propagation delay of a combined circuit requires identifying the longest path of propagation delays from input to output, and adding each propagation delay along this path.

The principle of logical effort utilizes propagation delays to compare designs implementing the same logical statement. The difference in propagation delays of logic elements is the major contributor to glitches in asynchronous circuits as a result of race conditions.

- Propagation delay may increase or decrease with operating temperature depending on the device type. As the temperature increases the gate delay decreases for FinFET transistors due to Inverse Temperature Dependence; for metal wires and other conductive materials the propagation delay increases due to rising electrical resistance.
- Marginal increases in supply voltage can increase propagation delay, since the upper switching threshold voltage VIH (often expressed as a percentage of the high-voltage supply rail) naturally increases proportionately.
- Increases in output load capacitance, often from placing increased fan-out loads on a wire, will also increase propagation delay.

All of these factors influence each other through an RC time constant: any increase in load capacitance increases C, heat-induced resistance the R factor, and supply threshold voltage increases will affect whether more than one time constants are required to reach the threshold. If the output of a logic gate is connected to a long trace or used to drive many other gates (high fanout) the propagation delay increases substantially.

## Networking

In computer networks, propagation delay is the amount of time it takes for the head of the signal to travel from the sender to the receiver. It can be computed as the ratio between the link length and the propagation speed over the specific medium.

Propagation delay is equal to *d / s* where *d* is the distance and *s* is the wave propagation speed. In wireless communication, *s*=*c*, i.e. the speed of light. In copper wire, the speed *s* generally ranges from .59c to .77c. This delay is the major obstacle in the development of high-speed computers and is called the interconnect bottleneck in IC systems.

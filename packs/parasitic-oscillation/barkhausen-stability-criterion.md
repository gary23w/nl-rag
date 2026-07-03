---
title: "Barkhausen stability criterion"
source: https://en.wikipedia.org/wiki/Barkhausen_stability_criterion
domain: parasitic-oscillation
license: CC-BY-SA-4.0
tags: parasitic oscillation
fetched: 2026-07-03
---

# Barkhausen stability criterion

In electronics, the **Barkhausen stability criterion** is a mathematical condition to determine when a linear electronic circuit will oscillate. It was put forth in 1921 by German physicist Heinrich Barkhausen (1881–1956). It is widely used in the design of electronic oscillators, and also in the design of general negative feedback circuits such as op amps, to prevent them from oscillating.

## Limitations

Barkhausen's criterion applies to linear circuits with a feedback loop. It cannot be applied directly to active elements with negative resistance like tunnel diode oscillators.

The kernel of the criterion is that a complex pole pair must be placed on the imaginary axis of the complex frequency plane if steady state oscillations should take place. In the real world, it is impossible to balance on the imaginary axis; small errors will cause the poles to be either slightly to the right or left, resulting in infinite growth or decreasing to zero, respectively. Thus, in practice a steady-state oscillator is a non-linear circuit; the poles are manipulated to be slightly to the right, and a nonlinearity is introduced that reduces the loop gain when the output is high.

## Criterion

It states that if *A* is the gain of the amplifying element in the circuit and β(*j*ω) is the transfer function of the feedback path, so β*A* is the loop gain around the feedback loop of the circuit, the circuit will sustain steady-state oscillations only at frequencies for which:

1. The loop gain is equal to unity in absolute magnitude, that is, $|\beta A|=1\,$ and
2. The phase shift around the loop is zero or an integer multiple of 2π: $\angle \beta A=2\pi n,n\in \{0,1,2,\dots \}\,.$

Barkhausen's criterion is a *necessary* condition for oscillation but not a *sufficient* condition: some circuits satisfy the criterion but do not oscillate. Similarly, the Nyquist stability criterion also indicates instability but is silent about oscillation. Apparently there is not a compact formulation of an oscillation criterion that is both necessary and sufficient.

## Erroneous version

Barkhausen's original "formula for self-excitation", intended for determining the oscillation frequencies of the feedback loop, involved an equality sign: |β*A*| = 1. At the time conditionally-stable nonlinear systems were poorly understood; it was widely believed that this gave the boundary between stability (|β*A*| < 1) and instability (|β*A*| ≥ 1), and this erroneous version found its way into the literature. However, *sustained* oscillations only occur at frequencies for which equality holds.

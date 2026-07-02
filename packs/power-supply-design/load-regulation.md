---
title: "Load regulation"
source: https://en.wikipedia.org/wiki/Load_regulation
domain: power-supply-design
license: CC-BY-SA-4.0
tags: power supply, voltage regulator, load regulation, output ripple
fetched: 2026-07-02
---

# Load regulation

**Load regulation** is the capability to maintain a constant voltage (or current) level on the output channel of a power supply despite changes in the supply's load (such as a change in resistance value connected across the supply output).

## Definitions

Load regulation of a constant-voltage source is defined by the equation:

$\%{\text{Load Regulation}}=100\%\,{\frac {V_{min-load}-V_{max-load}}{V_{nom-load}}}$

Where:

- $V_{max-load}$ is the voltage at maximum load. The maximum load is the one that draws the greatest current, i.e. the lowest specified load resistance (never short circuit);
- $V_{min-load}$ is the voltage at minimum load. The minimum load is the one that draws the least current, i.e. the highest specified load resistance (possibly open circuit for some types of linear supplies, usually limited by pass transistor minimum bias levels);
- $V_{nom-load}$ is the voltage at the typical specified load.

For a constant-current supply, the above equation uses currents instead of voltages, and the maximum and minimum load values are when the largest and smallest specified voltage across the load are produced.

For switching power supplies, the primary source of regulation error is switching ripple, rather than control loop precision. In such cases, load regulation is defined without normalizing to voltage at nominal load and has the unit of volts, not a percentage.

${\text{Load Regulation}}(V)=V_{min-load}-V_{max-load}$

## Measurement

A simple way to manually measure load regulation is to connect three parallel load resistors to the power supply where two of the resistors, R2 and R3, are connected through switches while the other resistor, R1 is connected directly. The values of the resistors are selected such that R1 gives the highest load resistance, R1||R2 gives the nominal load resistance and either R1||R2||R3 or R2||R3 gives the lowest load resistance. A voltmeter is then connected in parallel to the resistors and the measured values of voltage for each load state can be used to calculate the load regulation as given in the equation above.

Programmable loads are typically used to automate the measurement of load regulation.

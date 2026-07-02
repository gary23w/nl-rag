---
title: "Power-on reset"
source: https://en.wikipedia.org/wiki/Power-on_reset
domain: power-sequencing
license: CC-BY-SA-4.0
tags: power-on reset, inrush current, hot swapping, power management integrated circuit
fetched: 2026-07-02
---

# Power-on reset

A **power-on reset** (**PoR**, **POR**) generator is a microcontroller or microprocessor peripheral that generates a reset signal when power is applied to the device. It ensures that the device starts operating in a known state.

## PoR generator

In VLSI devices, the **power-on reset** (**PoR**) is an electronic device incorporated into the integrated circuit that detects the power applied to the chip and generates a reset impulse that goes to the entire circuit, placing it into a known state.

A simple PoR uses the charging of a capacitor, in series with a resistor, to measure a time period during which the rest of the circuit is held in a reset state. A Schmitt trigger may be used to deassert the reset signal cleanly, once the rising voltage of the RC network passes the threshold voltage of the Schmitt trigger. The resistor and capacitor values should be determined so that the charging of the RC network takes long enough that the supply voltage will have stabilised by the time the threshold is reached.

One of the issues with using an RC network to generate a PoR pulse is the sensitivity of the R and C values to the power-supply ramp characteristics. When the power supply ramp is rapid, the R and C values can be calculated so that the time to reach the switching threshold of the Schmitt trigger is enough to apply a long enough reset pulse. When the power-supply ramp itself is slow, the RC network tends to get charged up along with the power-supply ramp up. So when the input Schmitt stage is all powered up and ready, the input voltage from the RC network would already have crossed the Schmitt trigger point. This means that there might not be a reset pulse supplied to the core of the VLSI.

## Power-on reset on IBM mainframes

On an IBM mainframe, a **power-on reset** (**POR**) is a sequence of actions that the processor performs either due to a POR request from the operator or as part of turning on power. The operator requests a POR for configuration changes that cannot be recognized by a simple System Reset.

---
title: "Clock gating"
source: https://en.wikipedia.org/wiki/Clock_gating
domain: power-analysis-vlsi
license: CC-BY-SA-4.0
tags: power analysis vlsi, clock gating, power gating, leakage power
fetched: 2026-07-02
---

# Clock gating

In computer architecture, **clock gating** is a popular power management technique used in many synchronous circuits for reducing dynamic power dissipation (a significant source of power dissipation in digital designs), by removing the clock signal when the circuit, or a subpart of it, is idle. Clock gating saves power by pruning part of the clock tree distribution, at the cost of adding more logic to a circuit.

Pruning the clock turns off portions of the circuitry so that the flip-flops in them do not switch state, as switching the state consumes power. When not switched, the switching power consumption is reduced. This technique is particularly effective in systems with significant idle time or predictable periods of inactivity within specific modules.

## Essential details

Digital circuits consume power through multiple mechanisms, typically categorised into dynamic and static components. The equation can describe the average power dissipation in a CMOS circuit:

$P_{\text{avg}}=P_{\text{dynamic}}+P_{\text{short}}+P_{\text{leakage}}+P_{\text{static}}$

- **Pdynamic** results from charging and discharging capacitive loads during logic transitions. It is proportional to the switching activity, capacitance, supply voltage squared, and clock frequency.
- **Pshort** arises during signal transitions, when both PMOS and NMOS transistors momentarily conduct simultaneously, creating a brief short-circuit current path between power and ground.
- **Pleakage** is due to subthreshold and gate leakage currents, which occur even when transistors are off. This component becomes increasingly relevant in deep submicron technologies.
- **Pstatic** includes the power consumed by always-on blocks, such as biasing circuits or reference generators, and is present even in standby conditions.

These components collectively define the total power profile of a digital system, and their optimisation is crucial for low-power design.

These components become increasingly critical in modern integrated circuits, especially with technology scaling, where leakage and short-circuit power can constitute a significant portion of the total power budget.

Clock gating is one of several techniques used to reduce the power consumption of digital circuits. It specifically targets the dynamic power component, Pdynamic, by lowering unnecessary switching activity in clock signals. The following equation can approximate the dynamic power:

$P_{\text{dynamic}}=\alpha \cdot C_{L}\cdot V_{dd}^{2}\cdot f$

Where:

- *α* is the switching activity factor,
- *CL* is the load capacitance,
- *Vdd* is the supply voltage,
- *f* is the clock frequency.

By turning off the clock signal to portions of the circuit when not in use, clock gating reduces *α*, thus decreasing overall dynamic power consumption. This differs from the power-gating technique, which cuts the power supply entirely and simultaneously reduces multiple sources of power dissipation.

## Clock-gating techniques

Clock-gating techniques typically operate by targeting specific clock regions. To apply these techniques, it is often necessary to modify the registers/(flip-flops) in the circuit so that they can be controlled and disconnected from the clock distribution network, effectively isolating blocks of combinational logic.

External circuits can control clock and activation signals through a technique known as Enabled Flip-Flops, or they can be generated internally using traditional clock-gating methods.

When the control signal (CNTRL) is set to 1, the clock-gating circuit turns off the clock by holding it at a fixed logic level, either 0 or 1. One typical implementation uses a CMOS pass-transistor controlled by the inverted control signal.

Clock-gating logic can be added to a design in a variety of ways:

1. It can be coded into the register-transfer level (RTL) code as enable conditions that can be automatically translated into clock-gating logic by synthesis tools (fine-grained clock gating).
2. It can be inserted into the design manually by the RTL designers (typically as module-level clock gating) by instantiating library-specific integrated clock gating (ICG) cells to gate the clocks of specific modules or registers.
3. It can be semi-automatically inserted into the RTL by automated clock-gating tools. These tools either insert ICG cells into the RTL or add enable conditions into the RTL code. These typically also offer sequential clock-gating optimisations.

### Glitch-free clock gating

A common implementation of clock gating uses a level-sensitive latch (or flip-flop) to prevent glitches on the gated clock. The enable signal is captured only when the clock is in its inactive phase, ensuring that the gating control remains stable during the active clock transition. This avoids short unwanted pulses (glitches) that can cause incorrect switching in sequential elements. Many integrated clock-gating (ICG) cells include this latch internally to provide a glitch-free gated clock.

In general, clock gating applied at a coarser granularity leads to reduced resource overhead and greater power savings.

Any RTL modifications to improve clock gating will result in functional changes to the design (since the registers will now hold different values), which need to be verified.

## Other considerations

Sequential clock gating is the process of propagating enable conditions through upstream and downstream sequential elements, allowing additional registers to be clock-gated. This technique extends clock gating beyond individual flip-flops to optimise power savings across larger circuit portions.

Chips designed for battery-powered or ultra-low-power applications—such as mobile phones, wearable devices, and embedded systems—typically simultaneously implement multiple clock gating strategies. Manual clock gating involves software drivers that enable or disable clocks to various idle controllers. In contrast, automatic clock gating uses hardware mechanisms to detect when a clock is unnecessary and dynamically turns it off. These approaches often operate together within the same enable tree. For example, an internal bus or bridge may employ automatic gating, keeping the clock disabled until accessed by the CPU or a DMA engine. In contrast, peripherals on that bus might be permanently gated off if unused in a particular board design.

Clock gating may also be used to reduce area. If many registers have the same enable, clock gating them at a higher point in the clock tree may cost only one integrated clock gate worth of area, but would save a 2:1 multiplexer (the "feedback mux" normally used to implement the enable) worth of area per register that has that enable.

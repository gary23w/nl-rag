---
title: "Automatic generation control"
source: https://en.wikipedia.org/wiki/Automatic_generation_control
domain: brownout-electricity
license: CC-BY-SA-4.0
tags: brownout electricity
fetched: 2026-07-03
---

# Automatic generation control

In an electric power system, **automatic generation control** (**AGC**) is a system for adjusting the power output of multiple generators at different power plants, in response to changes in the load. Since a power grid requires that generation and load closely balance moment by moment, frequent adjustments to the output of generators are necessary. The balance can be judged by measuring the system frequency; if it is increasing, more power is being generated than used, which causes all the machines in the system to accelerate. If the system frequency is decreasing, more load is on the system than the instantaneous generation can provide, which causes all generators to slow down.

## History

Before the use of automatic generation control, one generating unit in a system would be designated as the regulating unit and would be manually adjusted to control the balance between generation and load to maintain system frequency at the desired value. The remaining units would be controlled with speed droop to share the load in proportion to their ratings. With automatic systems, many units in a system can participate in regulation, reducing wear on a single unit's controls and improving overall system efficiency, stability, and economy.

Where the grid has tie interconnections to adjacent control areas, automatic generation control helps maintain the power interchanges over the tie lines at the scheduled levels. With computer-based control systems and multiple inputs, an automatic generation control system can take into account such matters as the most economical units to adjust, the coordination of thermal, hydroelectric, and other generation types, and even constraints related to the stability of the system and capacity of interconnections to other power grids.

## Types

### Turbine-governor control

Turbine generators in a power system have stored kinetic energy due to their large rotating masses. All the kinetic energy stored in a power system in such rotating masses is a part of the grid inertia. When system load increases, grid inertia is initially used to supply the load. This, however, leads to a decrease in the stored kinetic energy of the turbine generators. Since the mechanical power of these turbines correlates with the delivered electrical power, the turbine generators have a decrease in angular velocity, which is directly proportional to a decrease in frequency in synchronous generators.

The purpose of the turbine-governor control (TGC) is to maintain the desired system frequency by adjusting the mechanical power output of the turbine. These controllers have become automated and at steady state, the frequency-power relation for turbine-governor control is,

$\Delta p_{m}=\Delta p_{ref}-1/R\times \Delta f$

where,

$\Delta p_{m}$ is the change in turbine mechanical power output

$\Delta p_{ref}$ is the change in a reference power setting

$R=-\Delta f/\Delta p_{m}=-slope$ is the regulation constant which quantifies the sensitivity of the generator to a change in frequency

$\Delta f$ is the change in frequency.

For steam turbines, steam turbine governing adjusts the mechanical output of the turbine by increasing or decreasing the amount of steam entering the turbine via a throttle valve.

### Load-frequency control

Load-frequency control (LFC) is employed to allow an area to first meet its own load demands, then to assist in returning the steady-state frequency of the system, Δf, to zero. Load-frequency control operates with a response time of a few seconds to keep system frequency stable.

### Economic dispatch

The goal of economic dispatch is to minimize total operating costs in an area by determining how the real power output of each generating unit will meet a given load. Generating units have different costs to produce a unit of electrical energy, and incur different costs for the losses in transmitting energy to the load. An economic dispatch algorithm will run every few minutes to select the combination of generating unit power setpoints that minimizes overall cost, subject to the constraints of transmission limitation or security of the system against failures. Further constraints may be imposed by the water supply of hydroelectric generation, or by the availability of sun and wind power.

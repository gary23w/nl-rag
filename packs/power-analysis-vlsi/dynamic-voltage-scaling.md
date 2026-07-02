---
title: "Dynamic voltage scaling"
source: https://en.wikipedia.org/wiki/Dynamic_voltage_scaling
domain: power-analysis-vlsi
license: CC-BY-SA-4.0
tags: power analysis vlsi, clock gating, power gating, leakage power
fetched: 2026-07-02
---

# Dynamic voltage scaling

In computer architecture, **dynamic voltage scaling** is a power management technique in which the voltage used in a component is increased or decreased, depending upon circumstances. Dynamic voltage scaling to increase voltage is known as **overvolting**; dynamic voltage scaling to decrease voltage is known as **undervolting**. Undervolting is done in order to conserve power, particularly in laptops and other mobile devices, where energy comes from a battery and thus is limited, or in rare cases, to increase reliability. Overvolting is done in order to support higher frequencies for performance.

The term "overvolting" is also used to refer to increasing static operating voltage of computer components to allow operation at higher speed (overclocking).

## Background

MOSFET-based digital circuits operate using voltages at circuit nodes to represent logical state. The voltage at these nodes switches between a high voltage and a low voltage during normal operation—when the inputs to a logic gate transition, the transistors making up that gate may toggle the gate's output.

Toggling a MOSFET's state requires changing its gate voltage from below the transistor's threshold voltage to above it (or from above it to below it). However, changing the gate's voltage requires charging or discharging the capacitance at its node. This capacitance is the sum of capacitances from various sources: primarily transistor gate capacitance, diffusion capacitance, and wires (coupling capacitance).

Higher supply voltages result in faster slew rate (rate of change of voltage per unit of time) when charging and discharging, which allows for quicker transitioning through the MOSFET's threshold voltage. Additionally, the more the gate voltage exceeds the threshold voltage, the lower the resistance of the transistor's conducting channel. This results in a lower RC time constant for quicker charging and discharging of the capacitance of the subsequent logic stage. Quicker transitioning afforded by higher supply voltages allows for operating at higher frequencies.

## Methods

Many modern components allow voltage regulation to be controlled through software (for example, through the BIOS). It is usually possible to control the voltages supplied to the CPU, RAM, PCI, and PCI Express (or AGP) port through a PC's BIOS.

However, some components do not allow software control of supply voltages, and hardware modification is required by overclockers seeking to overvolt the component for extreme overclocks. Video cards and motherboard northbridges are components which frequently require hardware modifications to change supply voltages. These modifications are known as "voltage mods" or "Vmod" in the overclocking community.

## Undervolting

Undervolting is reducing the voltage of a component, usually the processor, reducing temperature and cooling requirements, and possibly allowing a fan to be omitted. Just like overclocking, undervolting is highly subject to the so-called silicon lottery: one CPU can undervolt slightly better than the other and vice versa.

## Power

The *switching power* dissipated by a chip using static CMOS gates is $\alpha \cdot C\cdot V^{2}\cdot f$ , where C is the capacitance being switched per clock cycle, V is the supply voltage, f is the switching frequency, and $\alpha$ is the activity factor. Since V is squared, this part of the power consumption decreases quadratically with voltage. The formula is not exact however, as many modern chips are not implemented using 100% CMOS, but also use special memory circuits, dynamic logic such as domino logic, etc. Moreover, there is also a static leakage current, which has become more and more accentuated as feature sizes have become smaller (below 90 nanometres) and threshold levels lower.

Accordingly, dynamic voltage scaling is widely used as part of strategies to manage switching power consumption in battery powered devices such as cell phones and laptop computers. Low voltage modes are used in conjunction with lowered clock frequencies to minimize power consumption associated with components such as CPUs and DSPs; only when significant computational power is needed will the voltage and frequency be raised.

Some peripherals also support low voltage operational modes. For example, low power MMC and SD cards can run at 1.8 V as well as at 3.3 V, and driver stacks may conserve power by switching to the lower voltage after detecting a card which supports it.

When leakage current is a significant factor in terms of power consumption, chips are often designed so that portions of them can be powered completely off. This is not usually viewed as being dynamic voltage scaling, because it is not transparent to software. When sections of chips can be turned off, as for example on TI OMAP3 processors, drivers and other support software need to support that.

## Program execution speed

The speed at which a digital circuit can switch states - that is, to go from "low" (VSS) to "high" (VDD) or vice versa - is proportional to the voltage differential in that circuit. Reducing the voltage means that circuits switch slower, reducing the maximum frequency at which that circuit can run. This, in turn, reduces the rate at which program instructions that can be issued, which may increase run time for program segments which are sufficiently CPU-bound.

This again highlights why dynamic voltage scaling is generally done in conjunction with dynamic frequency scaling, at least for CPUs. There are complex tradeoffs to consider, which depend on the particular system, the load presented to it, and power management goals. When quick responses are needed (e.g. Mobile Sensors and Context-Aware Computing), clocks and voltages might be raised together. Otherwise, they may both be kept low to maximize battery life.

## Implementations

The 167-processor AsAP 2 chip enables individual processors to make extremely fast (on the order of 1-2ns) and locally controlled changes to their own supply voltages. Processors connect their local power grid to either a higher (VddHi) or lower (VddLow) supply voltage, or can be cut off entirely from either grid to dramatically cut leakage power.

Another approach uses per-core on-chip switching regulators for dynamic voltage and frequency scaling (DVFS).

## Operating system API

Unix system provides a userspace governor, allowing to modify the CPU frequencies (though limited to hardware capabilities).

## System stability

Dynamic frequency scaling is another power conservation technique that works on the same principles as dynamic voltage scaling. Both dynamic voltage scaling and dynamic frequency scaling can be used to prevent computer system overheating, which can result in program or operating system crashes, and possibly hardware damage. Reducing the voltage supplied to the CPU below the manufacturer's recommended minimum setting can result in system instability.

## Temperature

The efficiency of some electrical components, such as voltage regulators, decreases with increasing temperature, so the power used may increase with temperature causing thermal runaway. Increases in voltage or frequency may increase system power demands even faster than the CMOS formula indicates, and vice versa.

## Caveats

The primary caveat of overvolting is increased heat: the power dissipated by a circuit increases with the square of the voltage applied, so even small voltage increases significantly affect power. At higher temperatures, transistor performance is adversely affected, and at some threshold, the performance reduction due to the heat exceeds the potential gains from the higher voltages. Overheating and damage to circuits can occur very quickly when using high voltages.

There are also longer-term concerns: various adverse device-level effects such as hot carrier injection and electromigration occur more rapidly at higher voltages, decreasing the lifespan of overvolted components.

In order to mitigate the increased heat from overvolting, it's recommended to use liquid cooling to achieve higher ceilings and thresholds than you normally would with an aftermarket cooler. Also known as 'all-in-one' (AIO) coolers, they offer a far more effective method of unit cooling by relocating heat outside a computer case via the fans on the radiator whereas air cooling only disperses heat from the affected unit, increasing overall ambient temperatures.

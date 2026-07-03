---
title: "Charge controller"
source: https://en.wikipedia.org/wiki/Charge_controller
domain: charge-controller
license: CC-BY-SA-4.0
tags: charge controller
fetched: 2026-07-03
---

# Charge controller

A **charge controller**, **charge regulator** or **battery regulator** limits the rate at which electric current is added to or drawn from electric batteries to protect against electrical overload, overcharging, and may protect against overvoltage. This prevents conditions that reduce battery performance or lifespan and may pose a safety risk. It may also prevent completely draining ("deep discharging") a battery, or perform controlled discharges, depending on the battery technology, to protect battery life. The terms "charge controller" or "charge regulator" may refer to either a stand-alone device, or to control circuitry integrated within a battery pack, battery-powered device, and/or battery charger.

## Stand-alone charge controllers

Charge controllers are sold to consumers as separate devices, often in conjunction with solar or wind power generators, for uses such as RV, boat, and off-the-grid home battery storage systems. In solar applications, charge controllers may also be called solar regulators or solar charge controllers. Some charge controllers / solar regulators have additional features, such as a low voltage disconnect (LVD), a separate circuit which powers down the load when the batteries become overly discharged (some battery chemistries are such that over-discharge can ruin the battery).

A **series charge controller** or **series regulator** disables further current flow into batteries when they are full. A **shunt charge controller** or **shunt regulator** diverts excess electricity to an auxiliary or "shunt" load, such as an electric water heater, when batteries are full.

Simple charge controllers stop charging a battery when they exceed a set high voltage level, and re-enable charging when battery voltage drops back below that level. Pulse-width modulation (PWM) and maximum power point tracker (MPPT) technologies are more electronically sophisticated, adjusting charging rates depending on the battery's level, to allow charging closer to its maximum capacity.

A charge controller with MPPT capability frees the system designer from closely matching available PV voltage to battery voltage. Considerable efficiency gains can be achieved, particularly when the PV array is located at some distance from the battery. By way of example, a 150 volt PV array connected to an MPPT charge controller can be used to charge a 24 or 48 volt battery. Higher array voltage means lower array current, so the savings in wiring costs can more than pay for the controller.

Charge controllers may also monitor battery temperature to prevent overheating. Some charge controller systems also display data, transmit data to remote displays, and data logging to track electric flow over time.

## Integrated charge controller circuitry

Circuitry that functions as a charge regulator controller may consist of several electrical components, or may be encapsulated in a single microchip, an integrated circuit (IC) usually called a charge controller IC or charge control IC.

Charge controller circuits are used for rechargeable electronic devices such as cell phones, laptop computers, portable audio players, and uninterruptible power supplies, as well as for larger battery systems found in electric vehicles and orbiting space satellites

## Charging protocols

Due to limitations in currents that copper wires could safely handle, charging protocols have been developed to allow the end device to request elevated voltages for increasing the power throughput without increasing heat in the wires. The arriving voltage is then converted down to the battery's optimum charging voltage inside the end device.

### Quick Charge and Pump Express

The two most widely used standards are *Quick Charge* by Qualcomm and *Pump Express* by MediaTek.

The 2014 and 2015 versions of Pump Express, *Pump Express Plus* and *Pump Express Plus 2.0*, differ from by communicating voltage requests to the charger using current modulation signals through the main USB power lanes (*VBUS*) rather than negotiating through the USB 2.0 data lanes.

Pump Express Plus supports elevated voltage levels of 7, 9 and 12 volts, whereas the specification for Quick Charge 2.0 lacks the 7-volt level. A 20-volt level was added in a revision named "class B" of the specification.

The voltage range of the successor Pump Express Plus 2.0 is between 5 volts and 20 volts, with 0.5 volts steps. The Quick Charge 3.0 protocol supports finer-grain voltage levels with 0.2 volts steps and has a lower minimum voltage of approximately 3.3 volts. According to *PocketNow*, Quick Charge 3.0 starts at 3.2 volts with 0.2 volts between each step and goes up to 20 V (3.2 V, 3.4 V, 4.6 V, ..., 19.8 V, 20 V). The site "powerbankexpert.com" claims that the protocol has a minimum voltage of 3.6 volts.

### Oppo VOOC and Huawei SuperCharge

*Oppo VOOC*, also branded as "Dash Charge" for the subsidiary "OnePlus", as well as *SuperCharge* by Huawei, have taken the counter approach by increasing the charging current. Since the voltage that arrives at the end device matches the optimum battery charging voltage, no conversion inside the end device is necessary, which reduces heat there. However, unlike the charging protocols that only elevate voltage, the higher currents would produce more heat in cables' copper wires, making it incompatible with existing cables, and require special high-current cables with thicker copper wires.

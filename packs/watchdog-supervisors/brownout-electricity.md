---
title: "Brownout (electricity)"
source: https://en.wikipedia.org/wiki/Brownout_(electricity)
domain: watchdog-supervisors
license: CC-BY-SA-4.0
tags: watchdog timer, brownout detection, reset circuit, fail-safe design
fetched: 2026-07-02
---

# Brownout (electricity)

A **brownout** is a drop in the magnitude of voltage in an electrical power system.

Unintentional brownouts can be caused by excessive electricity demand, severe weather events, or a malfunction or error affecting electrical grid control or monitoring systems. Intentional brownouts are used for load reduction in an emergency, or to prevent a total grid power outage due to high demand. The term *brownout* comes from the dimming of incandescent lighting when voltage reduces.

In some countries, the term *brownout* refers not to a drop in voltage but to an intentional or unintentional power outage (or blackout).

## Effects

Different types of electrical apparatus will react in different ways to a voltage reduction. Some devices will be severely affected, while others may not be affected at all.

### Resistive loads

The heat output of any resistive device, such as an electric space heater, toaster, oven, and incandescent bulbs is equal to the power consumption, which is directly proportional to the square of the applied voltage if the resistance stays constant. Therefore, a significant reduction of heat output will occur with a relatively small reduction in voltage. An incandescent lamp will dim due to lower heat creation in the filament, as well as lower conversion of heat to light. Generally speaking, no damage will occur but functionality will be impaired.

### Motors

Commutated electric motors, such as universal motors, will run at reduced speed or reduced torque. Depending on the motor design, no harm may occur. However, under load, the motor may draw more current due to the reduced back-EMF developed at the lower armature speed. Unless the motor has ample cooling capacity, it may eventually overheat and burn out.

An induction motor will draw more current to compensate for the decreased voltage, which may lead to overheating and burnout. If a substantial part of a grid's load is electric motors, reducing voltage may not actually reduce load and can result in damage to customers' equipment.

### Power supplies

An unregulated DC supply will produce a lower output voltage. The output voltage ripple will decrease in line with the usually reduced load current. In a cathode-ray tube television, the reduced output voltage will make the screen image smaller, dimmer and fuzzier.

A linear DC regulated supply will maintain the output voltage unless the brownout is severe and the input voltage drops below the drop out voltage for the regulator, at which point the output voltage will fall and high levels of ripple from the rectifier/reservoir capacitor will appear on the output.

A switched-mode power supply will be affected if the brownout voltage is lower than the minimum input voltage of the power supply. As the input voltage falls, the current draw will increase to maintain the same output voltage and current, until such a point that the power supply malfunctions or its under-voltage protection kicks in and disables the output.

### Digital systems

Brownouts can cause unexpected behavior in systems with digital control circuits. Reduced voltages can bring control signals below the threshold at which logic circuits can reliably detect which state is being represented. As the voltage returns to normal levels the logic can latch at an incorrect state; to the extent that even "can't happen" states become possible. The seriousness of this effect and whether steps need to be taken by the designer to prevent it depends on the nature of the equipment being controlled; for instance, a brownout may cause a motor to begin running backwards.

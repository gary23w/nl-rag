---
title: "H-bridge"
source: https://en.wikipedia.org/wiki/H_bridge
domain: motor-drivers-hbridge
license: CC-BY-SA-4.0
tags: h-bridge driver, motor controller, pulse-width modulation drive, freewheeling diode
fetched: 2026-07-02
---

# H-bridge

(Redirected from

H bridge

)

An **H-bridge** is an electronic circuit that switches the polarity of a voltage applied to a load. These circuits are often used in robotics and other applications to allow DC motors to run forwards or backwards. The name is derived from its common schematic diagram representation, with four switching elements configured as the branches of a letter "H" and the load connected as the cross-bar.

Most DC-to-AC converters (power inverters), most AC/AC converters, the DC-to-DC push–pull converter, isolated DC-to-DC converter most motor controllers, and many other kinds of power electronics use H-bridges. In particular, a bipolar stepper motor is almost always driven by a motor controller containing two H-bridges.

## General

H-bridges are available as integrated circuits, or can be built from discrete components.

The term *H-bridge* is derived from the typical graphical representation of such a circuit. An H-bridge is built with four switches (solid-state or mechanical). When the switches S1 and S4 (according to the first figure) are closed (and S2 and S3 are open) a positive voltage is applied across the motor. By opening S1 and S4 switches and closing S2 and S3 switches, this voltage is reversed, allowing reverse operation of the motor.

Using the nomenclature above, the switches S1 and S2 should never be closed at the same time, as this would cause a short circuit on the input voltage source. The same applies to the switches S3 and S4. This condition is known as shoot-through.

## Common usage

An H-bridge is used to supply power to a two terminal device. By proper arrangement of the switches, the polarity of the power to the device can be changed. Two examples are discussed below: DC motor Driver, and transformer for a switching regulator. Note that not every switching configuration is safe; the "short"(see below in "DC motor driver" section) cases are dangerous to the power source and to the switches.

### DC motor driver

Changing the polarity of the power supply to DC motor is used to change the direction of rotation. Apart from changing the rotation direction, the H-bridge can provide additional operation modes, "brake" and "free run until frictional stop". The H-bridge arrangement is generally used to reverse the polarity/direction of the motor, but can also be used to 'brake' the motor, where the motor comes to a sudden stop when the motor's terminals are connected together. By connecting its terminals, the motor's kinetic energy is consumed rapidly in form of electrical current and causes the motor to slow down. Another case allows the motor to coast to a stop, as the motor is effectively disconnected from the circuit. The following table summarizes operation, with S1-S4 corresponding to the diagram above. In the table below, "1" is used to represent "on" state of the switch, "0" to represent the "off" state.

| S1 | S2 | S3 | S4 | **Result** |
|---|---|---|---|---|
| **1** | 0 | 0 | **1** | Motor moves right |
| 0 | **1** | **1** | 0 | Motor moves left |
| 0 | 0 | 0 | 0 | Motor coasts |
| **1** | 0 | 0 | 0 |   |
| 0 | **1** | 0 | 0 |   |
| 0 | 0 | **1** | 0 |   |
| 0 | 0 | 0 | **1** |   |
| **1** | **1** | X | X | Short circuit |
| X | X | **1** | **1** |   |
| **1** | 0 | **1** | 0 | Brakes |
| 0 | **1** | 0 | **1** |   |

### Primary coil driver of switching power converter

Typical primary coil driver is to simply replace the two terminals of the DC motor by the two terminals of the primary coil. The switching current in the primary coil turns electrical energy into magnetic energy and transfers back to ac electrical energy in the secondary coil.

## Construction

### Relays

One way to build an H-bridge is to use an array of relays from a relay board.

A "double pole double throw" (DPDT) relay can generally achieve the same electrical functionality as an H-bridge (considering the usual function of the device). However a semiconductor-based H-bridge would be preferable to the relay where a smaller physical size, high speed switching, or low driving voltage (or low driving power) is needed, or where the wearing out of mechanical parts is undesirable.

Another configuration is to have a DPDT relay to set the direction of current flow and a transistor to enable the current flow. This can extend the relay life, as the relay will be switched while the transistor is off and thereby there is no current flow. It also enables the use of PWM switching to control the current level.

### N and P channel semiconductors

A solid-state H-bridge is typically constructed using opposite polarity devices, such as PNP bipolar junction transistors (BJT) or P-channel MOSFETs connected to the high voltage bus and NPN BJTs or N-channel MOSFETs connected to the low voltage bus.

### N channel-only semiconductors

The most efficient MOSFET designs use N-channel MOSFETs on both the high side and low side because they typically have a third of the ON resistance of P-channel MOSFETs. This requires a more complex design since the gates of the high side MOSFETs must be driven positive with respect to the DC supply rail. Many integrated circuit MOSFET gate drivers include a charge pump within the device to achieve this.

Alternatively, a switched-mode power supply DC–DC converter can be used to provide isolated ('floating') supplies to the gate drive circuitry. A multiple-output flyback converter is well-suited to this application.

Another method for driving MOSFET-bridges is the use of a specialised transformer known as a GDT (gate drive transformer), which gives the isolated outputs for driving the upper FETs gates. The transformer core is usually a ferrite toroid, with 1:1 or 4:9 winding ratio. However, this method can only be used with high frequency signals. The design of the transformer is also very important, as the leakage inductance should be minimized, or cross conduction may occur. The outputs of the transformer are usually clamped by Zener diodes, because high voltage spikes could destroy the MOSFET gates.

### Variants

A common variation of this circuit uses just the two transistors on one side of the load, similar to a class AB amplifier. Such a configuration is called a "half bridge". It acts as an electronic toggle switch, the half bridge is not able to switch polarity of the voltage applied to the load. The half bridge is used in some switched-mode power supplies that use synchronous rectifiers and in switching amplifiers. The half-H-bridge type is commonly abbreviated to "Half-H" to distinguish it from full ("Full-H") H-bridges. Another common variation, adding a third 'leg' to the bridge, creates a three-phase inverter. The three-phase inverter is the core of any AC motor drive.

A further variation is the half-controlled bridge, where the low-side switching device on one side of the bridge, and the high-side switching device on the opposite side of the bridge, are each replaced with diodes. This eliminates the shoot-through failure mode, and is commonly used to drive variable or switched reluctance machines and actuators where bi-directional current flow is not required.

### Commercial availability

There are many commercially available inexpensive single and dual H-bridge packages. The L293x series, being technically mostly obsolete since the late 1970s due to decreased switching losses and higher speeds in more modern semiconductor products, is still found in many hobbyist circuitry. Few packages, like L9110, have built-in flyback diodes for back EMF protection.

## Operation as an inverter

A common use of the H-bridge is an inverter. The arrangement is sometimes known as a single-phase bridge inverter.

The H-bridge with a DC supply will generate a square wave voltage waveform across the load. For a purely inductive load, the current waveform would be a triangle wave, with its peak depending on the inductance, switching frequency, and input voltage.

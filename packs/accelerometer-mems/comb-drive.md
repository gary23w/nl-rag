---
title: "Comb drive"
source: https://en.wikipedia.org/wiki/Comb_drive
domain: accelerometer-mems
license: CC-BY-SA-4.0
tags: accelerometer sensor, piezoelectric accelerometer, proof mass, seismometer
fetched: 2026-07-02
---

# Comb drive

**Comb-drives** are microelectromechanical actuators, often used as linear actuators, which utilize electrostatic forces that act between two electrically conductive combs. Comb drive actuators typically operate at the micro- or nanometer scale and are generally manufactured by bulk micromachining or surface micromachining a silicon wafer substrate.

The attractive electrostatic forces are created when a voltage is applied between the static and moving combs causing them to be drawn together. The force developed by the actuator is proportional to the change in capacitance between the two combs, increasing with driving voltage, the number of comb teeth, and the gap between the teeth. The combs are arranged so that they never touch (because then there would be no voltage difference). Typically the teeth are arranged so that they can slide past one another until each tooth occupies the slot in the opposite comb.

Restoring springs, levers, and crankshafts can be added if the motor's linear operation is to be converted to rotation or other motions.

The force can be derived by first starting with the energy stored in a capacitor and then differentiating in the direction of the force. The energy in a capacitor is given by:

$E={\frac {1}{2}}CV^{2}$

$F={\frac {1}{2}}{\frac {\partial C}{\partial dx_{drive}}}V^{2}$

Using the capacitance for a parallel plate capacitor, the force is:

$F={\frac {-1}{2}}{\frac {nt\epsilon _{o}\epsilon _{r}V^{2}}{d}}$

V = applied electric potential, $\epsilon _{r}$ = relative permittivity of dielectric, $\epsilon _{o}$ = permittivity of free space (8.85 pF/m), n = total number of fingers on both sides of electrodes, t = thickness in the out-of-plane direction of the electrodes, d = gap between electrodes.

## Structure of Comb-drives

• rows of interlocking teeth • half fixed • half part of movable assembly • electrically isolated • electrostatic attraction/repulsion – CMOS drive voltage • many teeth increased force – typically 10μm long and strong

## Scaling Issues

Comb drives cannot scale to large gap distances (equivalently actuation distance), since development of effective forces at large gaps distances would require high voltages—therefore limited by electrical breakdown. More importantly, limitations imposed by gap distance limits the actuation distance.

---
title: "Reluctance motor"
source: https://en.wikipedia.org/wiki/Reluctance_motor
domain: stepper-motors-deep
license: CC-BY-SA-4.0
tags: stepper motor, microstepping drive, switched reluctance motor, holding torque
fetched: 2026-07-02
---

# Reluctance motor

A **reluctance motor** is a type of electric motor that induces non-permanent magnetic poles on the ferromagnetic rotor. The rotor does not have any windings. It generates torque through magnetic reluctance.

Reluctance motor subtypes include synchronous, variable, switched and variable stepping.

Reluctance motors can deliver high power density at low cost, making them attractive for many applications. Disadvantages include high torque ripple (the difference between maximum and minimum torque during one revolution) when operated at low speed, and noise due to torque ripple.

Until the early twenty-first century, their use was limited by the complexity of designing and controlling them. Advances in theory, computer design tools, and low-cost embedded systems for control overcame these obstacles. Microcontrollers use real-time computing control algorithms to tailor drive waveforms according to rotor position and current/voltage feedback. Before the development of large-scale integrated circuits, the control electronics were prohibitively costly.

## Design and operating fundamentals

The stator consists of multiple projecting (salient) electromagnet poles, similar to a wound field brushed DC motor. The rotor consists of soft magnetic material, such as laminated silicon steel, which has multiple projections acting as salient magnetic poles through magnetic reluctance. For switched reluctance motors, the number of rotor poles is typically less than the number of stator poles, which minimizes torque ripple and prevents the poles from all aligning simultaneously—a position that cannot generate torque.

When a rotor pole is equidistant from two adjacent stator poles, the rotor pole is said to be in the "fully unaligned position". This is the position of maximum magnetic reluctance for the rotor pole. In the "aligned position", two (or more) rotor poles are fully aligned with two (or more) stator poles, (which means the rotor poles completely face the stator poles) and is a position of minimum reluctance.

When a stator pole is energized, the rotor torque is in the direction that reduces reluctance. Thus, the nearest rotor pole is pulled from the unaligned position into alignment with the stator field (a position of less reluctance). (This is the same effect used by a solenoid, or when picking up ferromagnetic metal with a magnet.) To sustain rotation, the stator field must rotate in advance of the rotor poles, thus constantly "pulling" the rotor along. Some motor variants run on 3-phase AC power (see the synchronous reluctance variant below). Most modern designs are of the switched reluctance type, because electronic commutation gives significant control advantages for motor starting, speed control and smooth operation (low torque ripple).

The inductance of each phase winding in the motor varies with position, because the reluctance also varies with position. This presents a control systems challenge.

## Types

### Synchronous reluctance

Synchronous reluctance motors (SynRM) have an equal number of stator and rotor poles. The projections on the rotor are arranged to introduce internal flux "barriers", holes that direct the magnetic flux along the so-called direct axis. The number of poles must be even, typically 4 or 6.

The rotor operates at synchronous speeds without current-conducting parts. Rotor losses are minimal compared to those of an induction motor, however it normally has less torque.

Once started at synchronous speed, the motor can operate with sinusoidal voltage. Speed control requires a variable-frequency drive.

High-powered SynRMs typically require rare-earth elements such as neodymium and dysprosium. However, a 2023 study reported the use of a dual-phase magnetic laminate to replace them. Magnetizing such a material creates highly magnetized regions, serving as the rotor poles, while leaving other regions non-magnetic (nonpermeable). In one experiment using high-temperature nitriding to increase strength, a dual-phase rotor output 23 kW at 14,000 RPM with a power density of 1.4 kW and 94% peak efficiency, while a comparable conventional rotor produced 3.7 kW. The use of nonpermeable posts and bridges allows them to be larger and stronger, reducing interfence between the flux lines of the rotor and the stator. One limitation is that magnetization is limited to 1.5 T, compared to conventional motors 2 T.

### Switched reluctance or variable reluctance

The switched reluctance motor (SRM) is a type of reluctance motor. Unlike brushed DC motors, power is delivered to windings in the stator (case) rather than the rotor. This simplifies mechanical design because power does not have to be delivered to the moving rotor, which eliminates the need for a commutator. However it complicates the electrical design, because a switching system must deliver power to the different windings and limit torque ripple. Sources disagree on whether it is a type of stepper motor.

The simplest SRM has the lowest construction cost of any electric motor. Industrial motors may have some cost reduction due to the lack of rotor windings or permanent magnets. Common uses include applications where the rotor must remain stationary for long periods, and in potentially explosive environments such as mining, because no commutation is involved.

The windings in an SRM are electrically isolated from each other, producing higher fault tolerance than induction motors. The optimal drive waveform is not a pure sinusoid, due to the non-linear torque relative to rotor displacement, and the windings' highly position-dependent inductance.

## Applications

- Analog electric meters
- Analog electric clocks
- Some washing machine designs
- Control rod drive mechanisms of nuclear reactors
- Hard disk drive motor
- Electric vehicles
- Power tools such as drill presses, lathes, and bandsaws

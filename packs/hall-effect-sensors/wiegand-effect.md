---
title: "Wiegand effect"
source: https://en.wikipedia.org/wiki/Wiegand_effect
domain: hall-effect-sensors
license: CC-BY-SA-4.0
tags: hall effect sensor, magnetic field sensing, wiegand effect, reed switch
fetched: 2026-07-02
---

# Wiegand effect

The **Wiegand effect** is a nonlinear magnetic effect, named after its discoverer John R. Wiegand, produced in specially annealed and hardened wire called Wiegand wire.

Wiegand wire is low-carbon Vicalloy, a ferromagnetic alloy of cobalt, iron, and vanadium. Initially, the wire is fully annealed. In this state the alloy is "soft" in the magnetic sense; that is, it is attracted to magnets and so magnetic field lines will divert preferentially into the metal, but the metal retains only a very small residual field when the external field is removed.

During manufacture, to give the wire its unique magnetic properties, it is subjected to a series of twisting and untwisting operations to cold-work the outside shell of the wire while retaining a soft core within the wire, and then the wire is aged. The result is that the magnetic coercivity of the outside shell is much larger than that of the inner core. This high coercivity outer shell will retain an external magnetic field even when the field's original source is removed.

The wire now exhibits a very large magnetic hysteresis: If a magnet is brought near the wire, the high coercivity outer shell excludes the magnetic field from the inner soft core until the magnetic threshold is reached, whereupon the entire wire — both the outer shell and inner core — rapidly switches magnetisation polarity. This switchover occurs in a few microseconds, and is called the Wiegand effect.

The value of the Wiegand effect is that the switchover speed is sufficiently fast that a significant voltage can be output from a coil using a Wiegand-wire core. Because the voltage induced by a changing magnetic field is proportional to the rate of change of the field, a Wiegand-wire core can increase the output voltage of a magnetic field sensor by several orders of magnitude as compared to a similar coil with a non-Wiegand core. This higher voltage can easily be detected electronically, and when combined with the high repeatability threshold of the magnetic field switching, making the Wiegand effect useful for positional sensors.

Once the Wiegand wire has flipped magnetization, it will retain that magnetization until flipped in the other direction. Sensors and mechanisms that use the Wiegand effect must take this retention into account.

The Wiegand effect is a macroscopic extension of the Barkhausen effect, as the special treatment of the Wiegand wire causes the wire to act macroscopically as a single large magnetic domain. The numerous small high-coercivity domains in the Wiegand wire outer shell switch in an avalanche, generating the Wiegand effect's rapid magnetic field change.

## Applications

### Wiegand sensors

Wiegand sensors are magnetic sensors that make use of the Wiegand effect to generate a consistent pulse every time magnetic field polarity reverses and therefore do not rely on any external voltage or current. The consistency of the pulses produced by Wiegand sensors can be used to provide energy for low-power and energy-saving applications. Being self-powered, Wiegand sensors have a potential in IoT applications as energy harvesters, proximity sensors, and event counters.

### Wiegand keycards

John R. Wiegand and Milton Velinsky developed an access control card using Wiegand wires.

Besides sensors, the Wiegand effect is used for security keycard door locks. The plastic keycard has a series of short lengths of Wiegand wire embedded in it, which encodes the key by the presence or absence of wires. A second track of wires provides a clock track. The card is read by pulling it through a slot in a reader device, which has a fixed magnetic field and a sensor coil. As each length of wire passes through the magnetic field, its magnetic state flips, which indicates a 1, and this is sensed by the coil. The absence of a wire indicates a 0. The resulting Wiegand protocol digital code is then sent to a host controller to determine whether to electrically unlock the door.

Wiegand cards are more durable and difficult to counterfeit than bar code or magnetic stripe cards. Since the keycode is permanently set into the card at manufacture by the positions of the wires, Wiegand cards can't be erased by magnetic fields or reprogrammed as magnetic stripe cards can.

The Wiegand interface, originally developed for Wiegand-wire cards, is still the de-facto standard convention for transmitting data from any kind of access card to an access control panel.

A capacitive MM code card, like Wiegand cards, embeds a code inside the plastic of the card, and so are more durable and difficult to counterfeit than magnetic stripes or printed barcodes on the surface of the card.

### Rotary encoder

Wiegand wires are used by some rotary magnetic encoders to power the multi-turn circuitry. As the encoder revolves, the Wiegand wire core coil generates a pulse of electricity sufficient to power the encoder and write the turns count to non-volatile memory. This works at any speed of rotation and eliminates the clock/gear mechanism typically associated with multi-turn encoders.

### Wheel speed sensor

Wiegand wires are fitted to the outer diameter of a wheel to measure rotational speeds. An externally mounted reading head detects the Wiegand pulses.

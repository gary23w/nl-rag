---
title: "Dimmer"
source: https://en.wikipedia.org/wiki/Dimmer
domain: dali-lighting
license: CC-BY-SA-4.0
tags: dali lighting protocol, digital addressable lighting interface, lighting control bus, led dimming control
fetched: 2026-07-02
---

# Dimmer

A **dimmer** is a device connected to a light fixture and used to lower the brightness of the light. By changing the voltage waveform applied to the lamp, it is possible to lower the intensity of the light output. Although variable-voltage devices are used for various purposes, the term *dimmer* is generally reserved for those intended to control light output from resistive incandescent, halogen, and (more recently) compact fluorescent lamps (CFLs) and light-emitting diodes (LEDs). More specialized equipment is needed to dim fluorescent, mercury-vapor, solid-state, and other arc lighting.

Dimmers range in size from small units the size of domestic light switches to high-power units used in large theatrical or architectural lighting installations. Small domestic dimmers are generally directly controlled, although remote control systems (such as X10) are available. Modern professional dimmers are generally controlled by a digital control system like DMX or DALI. In newer systems, these protocols are often used in conjunction with Ethernet.

In the professional lighting industry, changes in intensity are called "fades" and can be "fade up" or "fade down". Dimmers with direct manual control had a limit on the speed they could be varied at but this problem has been largely eliminated with modern digital units (although very fast changes in brightness may still be avoided for other reasons like lamp life).

Modern dimmers are built from semiconductors instead of variable resistors, because they have higher efficiency. A variable resistor would dissipate power as heat and acts as a voltage divider. Since semiconductor or solid-state dimmers switch quickly between a low resistance "on" state and a high resistance "off" state, they dissipate very little power compared with the controlled load.

Most recently, software programmable internal dimmers can use signals from the same switch that turns lights on and off to control dimming. No dedicated external dimmer is needed. A simple communications protocol, such as Blink'n'Dim, delivers dimming commands via the power line. They enable computer control via networked switches, but do not require it. Their cost is about the same as the older "dimmability" circuitry that they replace in LED bulbs, fixtures or drivers.

## History

Early dimmers were directly controlled through the manual manipulation of large dimmer panels. This required all power to come through the lighting control location, which could be inconvenient, inefficient and potentially dangerous for large or high-powered systems, such as those used for stage lighting.

In 1896, Granville Woods patented his "safety dimmer", which greatly reduced wasted energy by reducing the amount of energy generated to match desired demand rather than burning off unwanted energy.

In 1959, Joel S. Spira, who later founded the Lutron Electronics Company in 1961, invented a dimmer based on a then-new solid state switching device called a silicon controlled rectifier or SCR. This small device allowed the dimmer to be installed in a standard electrical wall box while saving energy.

In 1966, Eugene Alessio patented a light bulb socket adapter for adjusting the light level on a single light bulb using a TRIAC. To house this device, he decided on a 2-inch (51 mm) round device with one end capable of being screwed into a light bulb socket and the other end able to receive a light bulb.

When solid-state dimmers came into use, analogue remote control systems (such as 0-10 V lighting control systems) became feasible. The wire for the control systems was much smaller (with low current and lower danger) than the heavy power cables of previous lighting systems. Each dimmer had its own control wires, resulting in many wires leaving the lighting control location.

More recent digital control protocols such as DMX512, DALI, or one of the many Ethernet-based protocols like Art-Net, ETCnet, sACN, Pathport, ShowNet or KiNET enable the control of a large number of dimmers (and other stage equipment) through a single cable.

## Types of dimmer

### Rheostat dimmer

Dimmers based on rheostats were inefficient since they would dissipate a significant portion of the power rating of the load as heat. They were large and required plenty of cooling air. Because their dimming effect depended a great deal on the total load applied to each rheostat, the load needed to be matched fairly carefully to the power rating of the rheostat. Finally, as they relied on mechanical control they were slow and it was difficult to change many channels at a time.

#### Salt water dimmer

Early examples of a rheostat dimmer include a salt water dimmer, a kind of liquid rheostat; the liquid between a movable and fixed contact provided a variable resistance. The closer the contacts to each other, the more voltage was available for the light. Salt water dimmers required regular addition of water and maintenance due to corrosion; exposed parts were energized during operation, presenting a shock hazard.

### Coil-rotation transformer

The coil-rotation transformer used a fixed-position electromagnet coil in conjunction with a variable-position coil to vary the voltage in the line by varying the alignment of the two coils. Rotated 90 degrees apart, the secondary coil is affected by two equal but opposite fields from the primary, which effectively cancel each other out and produce no voltage in the secondary.

These coils resembled the standard rotor and stator as used in an electric motor, except that the rotor was held against rotation using brakes and was moved to specific positions using high-torque gearing. Because the rotor did not ever turn a complete revolution, a commutator was not required and long flexible cables could be used on the rotor instead.

### Autotransformer dimmer

Variable autotransformers (trade name "Variac") were then introduced. While they are still nearly as large as rheostat dimmers, which they closely resemble, they are relatively efficient devices. Their voltage output, and so their dimming effect, is largely independent of the load applied so it was far easier to design the lighting that would be attached to each autotransformer channel. Remote control of the dimmers was still impractical, although some dimmers were equipped with motor drives that could slowly and steadily reduce or increase the brightness of the attached lamps. Autotransformers have fallen out of use for lighting but are used for other applications.

However, there are certain lighting scenarios in which autotransformers are still a desirable solution (as of 2021). For instance, the control room of an audio recording studio may require an extremely strict limit for electromagnetic interference. In comparison with solid-state dimmers, the conducted emissions produced by autotransformers are effectively zero.

### Solid-state dimmer

Solid-state, or semiconductor, dimmers were introduced to solve some of these problems. Semiconductor dimmers switch on at an adjustable time (phase angle) after the start of each alternating-current half-cycle, thereby altering the voltage waveform applied to lamps and so changing its RMS effective value. Because they switch instead of absorbing part of the voltage supplied, there is very little wasted power. Dimming can be almost instantaneous and is easily controlled by remote electronics. This development also made it possible to make dimmers small enough to be used in place (within the pattress) of normal domestic light switches.

The switches generate some heat during switching and can also cause radio-frequency interference. Inductors or chokes are used as part of the circuitry to suppress this interference. When the dimmer is at 50% power, the switches are switching their highest voltage (>325 V in Europe) and the sudden surge of power causes the coils on the inductor to move, creating a buzzing sound associated with some types of dimmer; this same effect can be heard in the filaments of the incandescent lamps as "singing". The suppression circuitry might be insufficient to prevent buzzing to be heard on sensitive audio and radio equipment that shares the mains supply with the lighting loads. In this case, special steps must be taken to prevent this interference. European dimmers must comply with relevant EMC legislation requirements; this involves suppressing the emissions described above to limits described in EN55104.

In the electrical schematic shown, a typical light dimmer based on a silicon-controlled rectifier (SCR) dims the light through phase-angle control. This unit is wired in series with the load. Diodes (D2, D3, D4 and D5) form a bridge, which generates pulsed DC. R1 and C1 form a circuit with a time constant. As the voltage increases from zero (at the start of every halfwave) C1 charges up. When C1 is able to make Zener diode D6 conduct and inject current into the SCR, the SCR fires. When the SCR conducts, D1 discharges C1 through the SCR. The SCR shuts off when the current falls to zero and the supply voltage drops at the end of the half cycle, ready for the circuit to start work on the next half cycle. This circuit is called a **leading-edge dimmer** or **forward phase dimming**.

Dimmers based on insulated-gate bipolar transistors (IGBTs) do away with most of the noise present in TRIACs by chopping off the falling side of the sine wave. These circuits are called **trailing-edge dimmers** or **reverse phase dimming**.

An even newer, but still expensive technology is **sine-wave dimming**, which is implemented as a high-power switched-mode power supply followed by a filter.

### mVolt

Multi-Volt or mVolt lamps can operate seamlessly at multiple voltages, typically ranging from 120 Volts to 277 Volts. Multi-Volt lamps produce the same amount of light regardless of supply Voltage. Dimming is accomplished by a separate 0-10 V lighting control dimming signal.

## Control

Non domestic dimmers are usually controlled remotely by means of various protocols. Analogue dimmers usually require a separate wire for each channel of dimming carrying a voltage between 0 and 10 V. Some analogue circuitry then derives a control signal from this and the mains supply for the switches. As more channels are added to the system more wires are needed between the lighting controller and the dimmers.

In the late 1970s, serial analogue protocols were developed. These multiplexed a series of analogue levels onto a single wire, with embedded clocking signal similar to a composite video signal (in the case of Strand Lighting's European D54 standard, handling 384 dimmers) or separate clocking signal (in the case of the US standard AMX192).

Digital protocols, such as DMX512 have proved to be the answer since the late 1980s. In early implementations a digital signal was sent from the controller to a **demultiplexer**, which sat next to the dimmers. This converted the digital signal into a collection of 0 to +10 V or 0 to −10 V signals which could be connected to the individual analogue control circuits.

Modern dimmer designs use microprocessors to convert the digital signal directly into a control signal for the switches. This has many advantages, giving closer control over the dimming, and giving the opportunity for diagnostic feedback to be sent digitally back to the lighting controller.

Some dimmers in residential applications are also equipped with a radio receiver to be used as wireless light switches which can be remotely controlled by a radio transmitter.

## Patching

Patching is the physical ("hard patch") or virtual ("soft patch") assignment to a circuit or channel for the purpose of control.

### Hard patch

Dimmers are usually arranged together in racks, where they can be accessed easily, and then power is run to the instruments being controlled. In architectural installations electricity is run straight from the dimmers to the lights via permanent wiring (this is called a **circuit**). They are hard run and cannot be changed.

However venues such as theatres demand more flexibility. To allow for changes for each show, and occasionally during shows, theatres sometimes install circuits run permanently to sockets around the theatre. Instead of these circuits going directly to the dimmer they are connected to a *patch bay*. A patch bay usually sits next to the dimmers enabling the dimmers to be connected to specific circuits via a patch cable. The patch bay may also enable many circuits to be connected to one dimmer and even series connection for low-voltage lamps. Also in some theatres individual cables are run directly from the light to dimmer. The assigned connections between the circuits (either at the patch bay or in the form of individual cables) and the dimmers is known as the **mains** or **hard patch**. This is most common in older theatres, and on a tour where dimmers will be brought in by the touring company.

### Soft patch

Most modern fixed installations do not have patch bays; instead they have a dimmer-per-circuit, and patch dimmers into channels using a computerized control console's **Soft Patch**.

## Dimming curves

The design of most analogue dimmers meant that the output of the dimmer was not directly proportional to the input. Instead, as the operator brought up a fader, the dimmer would dim slowly at first, then quickly in the middle, then slowly at the top. The shape of the curve resembled that of the third quarter of a sine wave. Different dimmers produced different dimmer curves, and different applications typically demanded different responses.

Television often uses a "square law" curve, providing finer control in top part of the curve, essential to allow accurate trimming of the colour temperature of lighting. Theatrical dimmers tend to use a softer "S" or linear curve. Digital dimmers can be made to have whatever curve the manufacturer desires; they may have a choice between a linear relationship and selection of different curves, so that they can be matched with older analogue dimmers. Sophisticated systems provide user-programmable or nonstandard curves, and a common use of a nonstandard curve is to turn a dimmer into a "non-dim", switching on at a user defined control level.

## Preheat

Switching high-intensity incandescent (filament) lamps to full power from cold can shorten their life dramatically, owing to the large inrush current that occurs. To reduce stress on the lamp filaments, dimmers may have a **preheat** function. This sets a minimum level, usually between 5% and 10%, which appears turned-off, but stops the lamp from cooling down too much. This also speeds up the lamp's reaction to sudden bursts of power that operators of rock'n'roll-style shows appreciate. The opposite of this function is sometimes called **top-set**. This limits the maximum power supplied to a lamp, which can also extend its life.

In less advanced systems, this same effect is achieved by literally pre-heating (warming) the globes before an event or performance. This is usually achieved by slowly bringing the lights up to full (or usually 90-95%) power over a period of between 1/2 to 1 hour. This is as effective as a built-in preheat function.

## Digital

Modern digital desks can emulate preheat and dimmer curves and allow a soft patch to be done in memory. This is often preferred as it means that the dimmer rack can be exchanged for another one without having to transfer complicated settings. Many different curves, or *profiles* can be programmed and used on different channels.

## Rise time

One measure of the quality of a leading edge dimmer is the "rise time". The rise time in this context is the amount of time it takes for the cut part of the waveform to get from zero to the instantaneous output voltage. In the waveform above it is a measure of the slope of the almost vertical edge of the red trace. Typically it is measured in tens to hundreds of microseconds. A longer rise time reduces the noise of the dimmer and the lamp as well as extending the life of the lamp. A longer rise time also reduces the electromagnetic interference produced by the dimmer. Unsurprisingly, a longer rise time is more expensive to implement than a short one, this is because the size of choke has to be increased. Newer dimming methods can help minimize such problems.

---
title: "Capacitor (part 3/3)"
source: https://en.wikipedia.org/wiki/Capacitor
domain: electronics
license: CC-BY-SA-4.0
tags: electronics, circuit, resistor, capacitor, transistor, voltage, adc, logic gate
fetched: 2026-07-02
part: 3/3
---

## Applications

### Energy storage

A capacitor can store electric energy when disconnected from its charging circuit, so it can be used like a temporary battery, or like other types of rechargeable energy storage system. Capacitors are commonly used in electronic devices to maintain power supply while batteries are being changed. (This prevents loss of information in volatile memory.)

A capacitor can facilitate conversion of kinetic energy of charged particles into electric energy and store it.

There are tradeoffs between capacitors and batteries as storage devices. Without external resistors or inductors, capacitors can generally release their stored energy in a very short time compared to batteries. Conversely, batteries can hold a far greater charge per their size. Conventional capacitors provide less than 360 joules per kilogram of specific energy, whereas a conventional alkaline battery has a density of 590 kJ/kg. There is an intermediate solution: supercapacitors, which can accept and deliver charge much faster than batteries, and tolerate many more charge and discharge cycles than rechargeable batteries. They are, however, 10 times larger than conventional batteries for a given charge. On the other hand, it has been shown that the amount of charge stored in the dielectric layer of the thin film capacitor can be equal to, or can even exceed, the amount of charge stored on its plates.

In car audio systems, large capacitors store energy for the amplifier to use on demand. Also, for a flash tube, a capacitor is used to hold the high voltage.

### Digital memory

In the 1930s, John Atanasoff applied the principle of energy storage in capacitors to construct dynamic digital memories for the first binary computers that used electron tubes for logic.

### Pulsed power and weapons

Pulsed power is used in many applications to increase the power intensity (watts) of a volume of energy (joules) by releasing that volume within a very short time. Pulses in the nanosecond range and powers in the gigawatts are achievable. Short pulses often require specially constructed, low-inductance, high-voltage capacitors that are often used in large groups (*capacitor banks*) to supply huge pulses of current for many pulsed power applications. These include electromagnetic forming, Marx generators, pulsed lasers (especially TEA lasers), pulse forming networks, radar, fusion research, and particle accelerators.

Large capacitor banks (reservoir) are used as energy sources for the exploding-bridgewire detonators or slapper detonators in nuclear weapons and other specialty weapons. Experimental work is under way using banks of capacitors as power sources for electromagnetic armour and electromagnetic railguns and coilguns.

### Power conditioning

Reservoir capacitors are used in power supplies where they smooth the output of a full or half wave rectifier. They can also be used in charge pump circuits as the energy storage element in the generation of higher voltages than the input voltage.

Capacitors are connected in parallel with the power circuits of most electronic devices and larger systems (such as factories) to shunt away and conceal current fluctuations from the primary power source to provide a "clean" power supply for signal or control circuits. Audio equipment, for example, uses several capacitors in this way, to shunt away power line hum before it gets into the signal circuitry. The capacitors act as a local reserve for the DC power source, and bypass AC currents from the power supply. This is used in car audio applications, when a stiffening capacitor compensates for the inductance and resistance of the leads to the lead–acid car battery.

#### Power-factor correction

In electric power distribution, capacitors are used for power-factor correction. Such capacitors often come as three capacitors connected as a three phase load. Usually, the values of these capacitors are not given in farads but rather as a reactive power in volt-amperes reactive (var). The purpose is to counteract inductive loading from devices like electric motors and transmission lines to make the load appear to be mostly resistive. Individual motor or lamp loads may have capacitors for power-factor correction, or larger sets of capacitors (usually with automatic switching devices) may be installed at a load center within a building or in a large utility substation.

### Suppression and coupling

#### Signal coupling

Because capacitors pass AC but block DC signals (when charged up to the applied DC voltage), they are often used to separate the AC and DC components of a signal. This method is known as *AC coupling* or "capacitive coupling". Here, a large value of capacitance, whose value need not be accurately controlled, but whose reactance is small at the signal frequency, is employed.

#### Decoupling

A decoupling capacitor is a capacitor used to protect one part of a circuit from the effect of another, for instance to suppress noise or transients. Noise caused by other circuit elements is shunted through the capacitor, reducing the effect they have on the rest of the circuit. It is most commonly used between the power supply and ground. An alternative name is *bypass capacitor* as it is used to bypass the power supply or other high impedance component of a circuit.

Decoupling capacitors need not always be discrete components. Capacitors used in these applications may be built into a printed circuit board, between the various layers. These are often referred to as embedded capacitors. The layers in the board contributing to the capacitive properties also function as power and ground planes, and have a dielectric in between them, enabling them to operate as a parallel plate capacitor.

#### High-pass and low-pass filters

#### Noise suppression, spikes, and snubbers

When an inductive circuit is opened, the current through the inductance collapses quickly, creating a large voltage across the open circuit of the switch or relay. If the inductance is large enough, the energy may generate a spark, causing the contact points to oxidize, deteriorate, or sometimes weld together, or destroying a solid-state switch. A snubber capacitor across the newly opened circuit creates a path for this impulse to bypass the contact points, thereby preserving their life; these were commonly found in contact breaker ignition systems, for instance. Similarly, in smaller scale circuits, the spark may not be enough to damage the switch but may still radiate undesirable radio frequency interference (RFI), which a filter capacitor absorbs. Snubber capacitors are usually employed with a low-value resistor in series, to dissipate energy and minimize RFI. Such resistor-capacitor combinations are available in a single package.

Capacitors are also used in parallel with interrupting units of a high-voltage circuit breaker to equally distribute the voltage between these units. These are called "grading capacitors".

In schematic diagrams, a capacitor used primarily for DC charge storage is often drawn vertically in circuit diagrams with the lower, more negative, plate drawn as an arc. The straight plate indicates the positive terminal of the device, if it is polarized (see electrolytic capacitor).

### Motor starters

In single phase squirrel cage motors, the primary winding within the motor housing is not capable of starting a rotational motion on the rotor, but is capable of sustaining one. To start the motor, a secondary "start" winding has a series non-polarized *starting capacitor* to introduce a lead in the sinusoidal current. When the secondary (start) winding is placed at an angle with respect to the primary (run) winding, a rotating electric field is created. The force of the rotational field is not constant, but is sufficient to start the rotor spinning. When the rotor comes close to operating speed, a centrifugal switch (or current-sensitive relay in series with the main winding) disconnects the capacitor. The start capacitor is typically mounted to the side of the motor housing. These are called capacitor-start motors, that have relatively high starting torque. Typically they can have up-to four times as much starting torque as a split-phase motor and are used on applications such as compressors, pressure washers and any small device requiring high starting torques.

Capacitor-run induction motors have a permanently connected phase-shifting capacitor in series with a second winding. The motor is much like a two-phase induction motor.

Motor-starting capacitors are typically non-polarized electrolytic types, while running capacitors are conventional paper or plastic film dielectric types.

### Signal processing

The energy stored in a capacitor can be used to represent information, either in binary form, as in DRAMs, or in analogue form, as in analog sampled filters and CCDs. Capacitors can be used in analog circuits as components of integrators or more complex filters and in negative feedback loop stabilization. Signal processing circuits also use capacitors to integrate a current signal.

#### Tuned circuits

Capacitors and inductors are applied together in tuned circuits to select information in particular frequency bands. For example, radio receivers rely on variable capacitors to tune the station frequency. Speakers use passive analog crossovers, and analog equalizers use capacitors to select different audio bands.

The resonant frequency *f* of a tuned circuit is a function of the inductance (*L*) and capacitance (*C*) in series, and is given by: f = 1 2 π L C {\displaystyle f={\frac {1}{2\pi {\sqrt {LC}}}}} ({\displaystyle f={\frac {1}{2\pi {\sqrt {LC}}}}}) where L is in henries and C is in farads.

### Sensing

Most capacitors are designed to maintain a fixed physical structure. However, various factors can change the structure of the capacitor, and the resulting change in capacitance can be used to sense those factors.

**Changing the dielectric**

The effects of varying the characteristics of the

dielectric

can be used for sensing purposes. Capacitors with an exposed and porous dielectric can be used to measure humidity in air. Capacitors are used to accurately measure the fuel level in

airplanes

; as the fuel covers more of a pair of plates, the circuit capacitance increases. Squeezing the dielectric can change a capacitor at a few tens of bar pressure sufficiently that it can be used as a pressure sensor.

A selected, but otherwise standard, polymer dielectric capacitor, when immersed in a compatible gas or liquid, can work usefully as a very low cost pressure sensor up to many hundreds of bar.

**Changing the distance between the plates**

Capacitors with a flexible plate can be used to measure strain or pressure. Industrial pressure transmitters used for

process control

use pressure-sensing diaphragms, which form a capacitor plate of an oscillator circuit. Capacitors are used as the

sensor

in

condenser microphones

, where one plate is moved by air pressure, relative to the fixed position of the other plate. Some

accelerometers

use

MEMS

capacitors etched on a chip to measure the magnitude and direction of the acceleration vector. They are used to detect changes in acceleration, in tilt sensors, or to detect free fall, as sensors triggering

airbag

deployment, and in many other applications. Some

fingerprint sensors

use capacitors. Additionally, a user can adjust the pitch of a

theremin

musical instrument by moving their hand since this changes the effective capacitance between the user's hand and the antenna.

**Changing the effective area of the plates**

Capacitive

touch switches

are used on many consumer electronic products.

### Oscillators

A capacitor can possess spring-like qualities in an oscillator circuit. In the image example, a capacitor acts to influence the biasing voltage at the npn transistor's base. The resistance values of the voltage-divider resistors and the capacitance value of the capacitor together control the oscillatory frequency.

### Producing light

A light-emitting capacitor is made from a dielectric that uses phosphorescence to produce light. If one of the conductive plates is made with a transparent material, the light is visible. Light-emitting capacitors are used in the construction of electroluminescent panels, for applications such as backlighting for laptop computers. In this case, the entire panel is a capacitor used for the purpose of generating light.


## Hazards and safety

The hazards posed by a capacitor are usually determined by the amount of energy stored, which can cause electrical burns or heart fibrillation. Factors such as voltage and chassis material are of secondary consideration, which are more related to how easily a shock can be initiated rather than how much damage can occur. Although they usually do not leave a burn, shocks as low as one joule have been reported to cause death under certain conditions, including conductivity of the surfaces, preexisting medical conditions, the humidity of the air, or the pathways it takes through the body (i.e. shocks that travel across the core of the body and, especially, through the heart are more dangerous than those limited to the extremities). Shocks over ten joules generally damage skin, and are considered hazardous. Any capacitor that can store 50 joules or more is considered potentially lethal.

Capacitors may retain a charge long after power is removed from a circuit; this charge can cause dangerous or fatal shocks or damage connected equipment. For example, the flash of a disposable camera has a photoflash capacitor that may contain over 15 joules of energy and be charged to over 300 volts. Service procedures for electronic devices usually include instructions to discharge large or high-voltage capacitors. Larger capacitors may have built-in discharge resistors to dissipate stored energy to a safe level within a few seconds after power is removed. High-voltage capacitors are stored with the terminals shorted, as protection from potentially dangerous voltages due to dielectric absorption or from transient voltages the capacitor may pick up from static charges or passing weather events.

Some old, large oil-filled paper or plastic film capacitors contain polychlorinated biphenyls (PCBs) which can leak into groundwater from landfills. Capacitors containing PCBs were labelled as containing "Askarel" and several other trade names. PCB-filled paper capacitors are found in pre-1975 fluorescent lamp ballasts, and other applications. Such capacitors may be sealed in a metal can with ceramic feed-through connectors.

Capacitors may catastrophically fail when subjected to voltages or currents beyond their rating, or in case of polarized capacitors, applied in a reverse polarity. Failures may create arcing that heats and vaporizes the dielectric fluid, causing a build up of pressurized gas that may result in swelling, rupture, or an explosion. Larger capacitors may have vents or similar mechanism to release of pressure in the event of failure. Capacitors used in RF or sustained high-current applications can overheat, especially in the center of the capacitor rolls. Capacitors used within high-energy capacitor banks can violently explode when a short in one capacitor causes sudden dumping of energy stored in the rest of the bank into the failing unit. High voltage vacuum capacitors can generate soft X-rays even during normal operation. Proper containment, fusing, and preventive maintenance can help to minimize these hazards.

High-voltage capacitors may benefit from a pre-charge to limit in-rush currents at power-up of high voltage direct current (HVDC) circuits. This extends the life of the component and may mitigate high-voltage hazards.

- (Swollen electrolytic capacitors. The vent on the tops allows the release of pressurized gas build-up in the event of failure, preventing it from exploding.) Swollen electrolytic capacitors. The vent on the tops allows the release of pressurized gas build-up in the event of failure, preventing it from exploding.
- (This high-energy capacitor from a defibrillator has a resistor connected between the terminals for safety, to dissipate stored energy.) This high-energy capacitor from a defibrillator has a resistor connected between the terminals for safety, to dissipate stored energy.
- (An exploded electrolytic capacitor, showing fragments of paper and metallic foil) An exploded electrolytic capacitor, showing fragments of paper and metallic foil

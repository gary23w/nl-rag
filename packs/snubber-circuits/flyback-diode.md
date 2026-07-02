---
title: "Flyback diode"
source: https://en.wikipedia.org/wiki/Flyback_diode
domain: snubber-circuits
license: CC-BY-SA-4.0
tags: snubber circuit, RC snubber, flyback diode, transient-voltage-suppression diode
fetched: 2026-07-02
---

# Flyback diode

A **flyback diode** (also called **freewheeling diode**) is any diode connected across an inductor used to eliminate flyback, which is the sudden voltage spike seen across an inductive load when its supply current is suddenly reduced or interrupted. It is used in circuits in which inductive loads are controlled by switches, and in switching power supplies and inverters.

Flyback circuits have been used since 1930 and were refined starting in 1950 for use in television receivers. The word *flyback* comes from the horizontal movement of the electron beam in a cathode ray tube, because the beam flew back to begin the next horizontal line.

This diode is known by many other names, such as snubber diode, commutating diode, freewheeling diode, suppressor diode, clamp diode, or catch diode.

## Operation

Fig. 1 shows an inductor connected to a battery - a constant voltage source. The resistor represents the small static resistance of the inductor's wire windings. When the switch is closed, the voltage from the battery is applied to the inductor, causing current from the battery's positive terminal to flow down through the inductor and resistor. The increase in current causes a back EMF (voltage) across the inductor due to Faraday's law of induction which opposes the change in current. Since the voltage across the inductor is limited to the battery's voltage of 24 volts, the rate of increase of the current is limited to an initial value of ${dI \over dt}={V_{B} \over L},$ so the current through the inductor increases slowly as energy from the battery is stored in the inductor's magnetic field. As the current rises, more voltage is dropped across the resistor and less across the inductor, until the current reaches a steady value of $I=V_{B}/R$ with all the battery voltage across the resistance and none across the inductance.

However, the current drops rapidly when the switch is opened in Fig. 2. The inductor resists the drop in current by developing a very large induced voltage of polarity in the opposite direction of the battery, positive at the lower end of the inductor and negative at the upper end. This voltage pulse, sometimes called the inductive "kick", which can be much larger than the battery voltage, appears across the switch contacts. It causes electrons to jump the air gap between the contacts, causing a momentary electric arc to develop across the contacts as the switch is opened. The arc continues until the energy stored in the inductor's magnetic field is dissipated as heat in the arc. The arc can damage the switch contacts, causing pitting and burning, eventually destroying them. If a transistor is used to switch the current, such as switching power supplies, the high reverse voltage can destroy the transistor.

To prevent the inductive voltage pulse on turnoff, a diode is connected across the inductor, as shown in Fig. 3. The diode doesn't conduct current while the switch is closed because it is reverse-biased by the battery voltage, so it doesn't interfere with the normal operation of the circuit. However, when the switch is opened, the induced voltage across the inductor of opposite polarity forward biases the diode, and it conducts current, limiting the voltage across the inductor and thus preventing the arc from forming at the switch. The inductor and diode momentarily form a loop or circuit powered by the stored energy in the inductor. This circuit supplies a current path to the inductor to replace the current from the battery, so the inductor current does not drop abruptly and does not develop a high voltage. The voltage across the inductor is limited to the forward voltage of the diode, around 0.7 - 1.5V. This "freewheeling" or "flyback" current through the diode and inductor decreases slowly to zero as the magnetic energy in the inductor is dissipated as heat in the series resistance of the windings. This may take a few milliseconds in a small inductor.

(left)

Oscilloscope trace showing inductive voltage spike in solenoid connected to a 24 VDC power supply.

(right)

The same switching transient with a flyback diode (

1N4007

) connected across the solenoid.

Note the different scaling

(50 V / division on the left, 1 V / division on the right).

These images show the voltage spike and its elimination through the use of a flyback diode (1N4007). In this case, the inductor is a solenoid connected to a 24V DC power supply. Each waveform was taken using a digital oscilloscope set to trigger when the voltage across the inductor dipped below zero. **Note the different scaling:** left image 50V/division, right image 1V/division. In Figure 1, the voltage as measured across the switch, bounces/spikes to around -300 V. In Figure 2, a flyback diode was added in antiparallel with the solenoid. Instead of spiking to -300 V, the flyback diode only allows approximately -1.4 V of potential to be built up (-1.4 V is a combination of the forward bias of the 1N4007 diode (1.1 V) and the foot of wiring separating the diode and the solenoid). The waveform in Figure 2 is also smoother than the waveform in Figure 1, perhaps due to arcing at the switch for Figure 1. In both cases, the total time for the solenoid to discharge is a few milliseconds, though the lower voltage drop across the diode will slow relay dropout.

## Design

When used with a DC coil relay, a flyback diode can cause delayed drop-out of the contacts when power is removed, due to the continued circulation of current in the relay coil and diode. When rapid opening of the contacts is important, a resistor or reverse-biased Zener diode can be placed in series with the diode to help dissipate the coil energy faster, at the expense of higher voltage at the switch.

Schottky diodes are preferred in flyback diode applications for switching power converters because they have the lowest forward drop (~0.2 V rather than >0.7 V for low currents) and are able to quickly respond to reverse bias (when the inductor is being re-energized). They, therefore, dissipate less energy while transferring energy from the inductor to a capacitor.

## Induction at the opening of a contact

According to Faraday's law of induction, if the current through an inductance changes, this inductance induces a voltage, so the current will flow as long as there is energy in the magnetic field. If the current can only flow through the air, the voltage is so high that the air conducts. That is why in mechanically switched circuits, the near-instantaneous dissipation which occurs without a flyback diode is often observed as an arc across the opening mechanical contacts. Energy is dissipated in this arc primarily as intense heat, which causes undesirable premature erosion of the contacts. Another way to dissipate energy is through electromagnetic radiation.

Similarly, for non-mechanical solid-state switching (i.e., a transistor), large voltage drops across an unactivated solid-state switch can destroy the component in question (either instantaneously or through accelerated wear and tear).

Some energy is also lost from the system as a whole and from the arc as a broad spectrum of electromagnetic radiation, in the form of radio waves and light. These radio waves can cause undesirable clicks and pops on nearby radio receivers.

To minimise the antenna-like radiation of this electromagnetic energy from wires connected to the inductor, the flyback diode should be connected as physically close to the inductor as practicable. This approach also minimises those parts of the circuit that are subject to an unwanted high-voltage — a good engineering practice.

### Derivation

The voltage at an inductor is, by the law of electromagnetic induction and the definition of inductance:

$V_{L}=-{d\Phi _{B} \over dt}=-L{dI \over dt}$

If there is no flyback diode but only something with great resistance (such as the air between two metal contacts), say, *R*2, we will approximate it as:

$V_{R_{2}}=R_{2}\cdot I$

If we open the switch and ignore *V*CC and *R*1, we get:

$V_{L}=V_{R_{2}}$

or

$-L{dI \over dt}=R_{2}\cdot I$

which is a differential equation with the solution:

$I(t)=I_{0}\cdot e^{-{R_{2} \over L}t}$

We observe that the current will decrease faster if the resistance is high, such as with air.

Now if we open the switch with the diode in place, we only need to consider *L*1, *R*1 and *D*1. For *I* > 0, we can assume:

$V_{D}=\mathrm {constant}$

so:

$V_{L}=V_{R_{1}}+V_{D}$

which is:

$-L{dI \over dt}=R_{1}\cdot I+V_{D}$

whose (first order differential equation) solution is:

$I(t)=(I_{0}+{1 \over R_{1}}V_{D})\cdot e^{-{R_{1} \over L}t}-{1 \over R_{1}}V_{D}$

We can calculate the time it needs to switch off by determining for which t it is *I*(*t*) = 0.

$t={-L \over R_{1}}\cdot ln{\left({V_{D} \over {V_{D}+I_{0}{R_{1}}}}\right)}$

If *V*CC = *I*0*R*1, then

$t={-L \over R_{1}}\cdot ln{\left({1 \over {{\frac {V_{CC}}{V_{D}}}+1}}\right)}={L \over R_{1}}\cdot ln{\left({{\frac {V_{CC}}{V_{D}}}+1}\right)}$

## Applications

Flyback diodes are commonly used when semiconductor devices switch inductive loads off: in relay drivers, H-bridge motor drivers, and so on. A switched-mode power supply also exploits this effect, but the energy is not dissipated to heat and is instead used to pump a packet of additional charge into a capacitor, in order to supply power to a load.

When the inductive load is a relay, the flyback diode can noticeably delay the release of the relay by keeping the coil current flowing longer. A resistor in series with the diode will make the circulating current decay faster at the drawback of an increased reverse voltage. A zener diode in series but with reverse polarity with regard to the flyback diode has the same properties, albeit with a fixed reverse voltage increase. Both the transistor voltages and the resistor or zener diode power ratings should be checked in this case.

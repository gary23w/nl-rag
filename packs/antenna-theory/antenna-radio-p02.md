---
title: "Antenna (radio) (part 2/2)"
source: https://en.wikipedia.org/wiki/Antenna_(radio)
domain: antenna-theory
license: CC-BY-SA-4.0
tags: dipole antenna, radiation pattern, antenna aperture, monopole antenna
fetched: 2026-07-02
part: 2/2
---

## Modeling antennas with line equations

In the first approximation, the current in a thin antenna is distributed

exactly as in a transmission line. —

Schelkunoff

&

Friis

(1952)

The flow of current in wire antennas is identical to the solution of counter-propagating waves in a single conductor transmission line, which can be solved using the telegrapher's equations. Solutions of currents along antenna elements are more conveniently and accurately obtained by numerical methods, so transmission-line techniques have largely been abandoned for precision modelling, but they continue to be a widely used source of useful, simple approximations that describe well the impedance profiles of antennas.

Unlike transmission lines, currents in antennas contribute power to the radiated part electromagnetic field, which can be modeled using radiation resistance.

The end of an antenna element corresponds to an unterminated (open) end of a single-conductor transmission line, resulting in a reflected wave identical to the incident wave, with its voltage *in* phase with the incident wave and its current in the *opposite* phase (thus net zero current, where there is, after all, no further conductor). The combination of the incident and reflected wave, just as in a transmission line, forms a standing wave with a current node at the conductor's end, and a voltage node one-quarter wavelength from the end (if the element is at least that long).

In a *resonant antenna*, the feedpoint of the antenna is at one of those voltage nodes. Due to discrepancies from the simplified version of the transmission line model, the voltage one quarter wavelength from the current node is not exactly zero, but it is near a minimum, and small compared to the much larger voltage at the conductor's end. Hence, a feed point matching the antenna at that spot requires a relatively small voltage but large current (the currents from the two waves add in-phase there), thus a relatively low feedpoint impedance.

Feeding the antenna at other points involves a large voltage, thus a large impedance, and usually one that is primarily reactive (low power factor), which is a terrible impedance match to available transmission lines. Therefore, it is usually desired for an antenna to operate as a resonant element with each conductor having a length of one quarter wavelength (or any other odd multiples of a quarter wavelength).

For instance, a half-wave dipole has two such elements (one connected to each conductor of a balanced transmission line) about one quarter wavelength long. Depending on the conductors' diameters, a small deviation from this length is adopted in order to reach the point where the antenna current and the (small) feedpoint voltage are exactly in phase. Then the antenna presents a purely resistive impedance, and ideally one close to the characteristic impedance of an available transmission line.

Despite these useful properties, resonant antennas have the disadvantage that they achieve resonance (purely resistive feedpoint impedance) only at a fundamental frequency, and perhaps some of its harmonics, and the feedpoint resistance is larger at higher-order resonances. Therefore, resonant antennas can only achieve their good performance within a limited bandwidth, depending on the Q at the resonance.


## Mutual impedance and interaction between antennas

The electric and magnetic fields emanating from a driven antenna element will generally affect the voltages and currents in nearby antennas, antenna elements, or other conductors. This is particularly true when the affected conductor is a resonant element (multiple of half-wavelengths in length) at about the same frequency, as is the case where the conductors are all part of the same active or passive antenna array.

Because the affected conductors are in the near-field, one can *not* just treat two antennas as transmitting and receiving a signal according to the Friis transmission formula for instance, but must calculate the *mutual impedance* matrix which takes into account both voltages and currents (interactions through both the electric and magnetic fields). Thus using the mutual impedances calculated for a specific geometry, one can solve for the radiation pattern of a Yagi–Uda antenna or the currents and voltages for each element of a phased array. Such an analysis can also describe in detail reflection of radio waves by a ground plane or by a corner reflector and their effect on the impedance (and radiation pattern) of an antenna in its vicinity.

Often such near-field interactions are undesired and pernicious. Currents in random metal objects near a transmitting antenna will often be in poor conductors, causing loss of RF power in addition to unpredictably altering the characteristics of the antenna. By careful design, it is possible to reduce the electrical interaction between nearby conductors. For instance, the 90 degree angle in between the two dipoles composing the turnstile antenna ensures no interaction between these, allowing these to be driven independently (but actually with the same signal in quadrature phases in the turnstile antenna design).


## Antenna types

Antennas can be classified by operating principles or by their application. Different authorities placed antennas in narrower or broader categories. Generally these include

- Dipole and monopole antennas
- Array antennas
- Loop antennas
- Parabolic antenna
- Traveling wave antennas
- Log-periodic antenna
- Spiral antenna
- Horn antenna
- Adcock antenna
- Sector antenna
- Helical antenna

These antenna types and others are summarized in greater detail in the overview article, Antenna types, as well as in each of the linked articles in the list above, and in even more detail in articles which those link to.

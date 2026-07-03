---
title: "Braid-breaker"
source: https://en.wikipedia.org/wiki/Braid-breaker
domain: ferrite-bead
license: CC-BY-SA-4.0
tags: ferrite bead
fetched: 2026-07-03
---

# Braid-breaker

A **braid-breaker** is a filter that prevents television interference (TVI). In many cases, TVI is caused by a high field strength of a nearby high frequency (HF) transmitter, the aerial down lead plugged into the back of the TV acts as a longwire antenna or as a simple vertical element. The radio frequency (RF) current flowing through the tuner of the TV tends to generate harmonics which then spoil the viewing.

The braid breaker works by preventing RF signals picked up on the outside flowing into the TV set, while passing RF inside the coax from the antenna.

## Designs

Designs for diminishing unwanted signals are based on two types of filters: a “choke” filter which blocks signals in the electrical *mode* most interference uses, and filters that selectively admit or impede signals depending on the signal frequency.

Further, carefully chosen combinations of filters of either one type or both types multiply each other's effects, so that even if only slightly different, two filters are more effective than a single filter, or either filter alone.

### Ferrite choke

Ferrite ring chokes work by presenting a high impedance to signals traveling along the braid only, but passes through differential-mode ("balanced") currents unchanged. The wanted signal is in differential mode with an equal and opposite current flowing in the braid to that in the cable core. The alternating current in the braid is impeded by the magnetic fields created in the ferrite, effectively placing a large inductance in series with the braid. The currents from the wanted signal, however, produce equal and opposite magnetic flux in the ferrite which cancel out.

The device is called a "choke" because the ferrite in effect "chokes off" the signal path for interference.

### High-pass filter

The other type of filters used are based on frequency: Below their operating frequency limit, inductors (coils) impede signals at higher frequencies more, and admit low frequencies, whereas capacitors do the opposite: capacitors admit high frequencies but impede low frequencies. These can be played-off against each other to impede or admit signals based on frequency.

A simple design for a high-pass filter consists of two 4.7 pF ceramic capacitors and two simple air-core inductor coils (4 turns of 20 AWG copper wire wound using a 6 mm drill bit as a form). The design is a symmetric network: The line is cut and the coils are connected from the braid to the core of the coaxial cable ends, while the capacitors bridge the cut, one capacitor connecting core-to-core and the other reconnecting the cut outer shield braids.

As an extra precaution, a 1.5 MΩ resistor is wired in parallel with the capacitor connecting the shields. The resistor acts as a “slow leak” on the ground wire that prevents buildup of static electricity on the TV aerial, but is too high a resistance to pass a signal carried along the cable, which operates near 72 Ω.

The impedance of the capacitors is very large for shortwave signals, below 50 MHz, but for UHF TV signals above 450 MHz their impedance is very small. In the opposite sense, the impedance of the coils connecting the inner and outer wires at the lower frequencies is very small, while for the wanted UHF signals the coils have a very high impedance. Hence the network does the following:

- At and below HF (below about 50 MHz) the coils short-circuit the core to the braid for both input and output, while the capacitors impede signals passing straight through. Hence isolating the input from the output for HF signals.
- At UHF, the impedance of the coils blocks the short-circuit between the core wire and the braid for both input and output, whereas the capacitors pass through the signals almost unchanged. Hence the UHF signals are connected as normal to the respective terminals on the other side of the network.

### Combination

An even better option is to use both a choke and a high-pass filter, since the filter described above may not be as effective for common-mode currents, which the choke will selectively remove.

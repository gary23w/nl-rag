---
title: "Traveling-wave tube"
source: https://en.wikipedia.org/wiki/Travelling-wave_tube
domain: rf-amplifiers
license: CC-BY-SA-4.0
tags: distributed amplifier, Doherty amplifier, traveling wave tube, load pull
fetched: 2026-07-02
---

# Traveling-wave tube

(Redirected from

Travelling-wave tube

)

A **traveling-wave tube** (**TWT**, pronounced "twit") or **traveling-wave tube amplifier** (**TWTA**, pronounced "tweeta") is a specialized vacuum tube that is used in electronics to amplify radio frequency (RF) signals in the microwave range. It was invented by Andrei Haeff around 1933 as a graduate student at Caltech, and its present form was invented by Rudolf Kompfner in 1942–43. The TWT belongs to a category of "linear beam" tubes, such as the klystron, in which the radio wave is amplified by absorbing power from a beam of electrons as it passes down the tube. Although there are various types of TWT, two major categories are:

- *Helix TWT* - in which the radio waves interact with the electron beam while traveling down a wire helix which surrounds the beam. These have wide bandwidth, but output power is limited to a few hundred watts.
- *Coupled cavity TWT* - in which the radio wave interacts with the beam in a series of cavity resonators through which the beam passes. These function as narrowband power amplifiers.

A major advantage of the TWT over some other microwave tubes is its ability to amplify a wide range of frequencies i.e. a large bandwidth. The bandwidth of the helix TWT can be as high as two octaves, while the cavity versions have bandwidths of 10–20%. Operating frequencies range from 300 MHz to 50 GHz. The power gain of the tube is on the order of 40 to 70 decibels, and output power ranges from a few watts to megawatts.

TWTs are widely used as the power amplifiers and oscillators in radar systems, communication satellite and spacecraft transmitters, and electronic warfare systems.

## Description

### A basic TWT

The TWT is an elongated vacuum tube with an electron gun (a heated cathode that emits electrons) at one end. A voltage applied across the cathode and anode accelerates the electrons towards the far end of the tube, and an external magnetic field around the tube focuses the electrons into a beam. At the other end of the tube the electrons strike the "collector", which returns them to the circuit.

Wrapped around the inside of the tube, just outside the beam path, is a helix of wire, typically oxygen-free copper. The RF signal to be amplified is fed into the helix at a point near the emitter end of the tube. The signal is normally fed into the helix via a waveguide or electromagnetic coil placed at one end, forming a one-way signal path, a directional coupler.

By controlling the accelerating voltage, the speed of the electrons flowing down the tube is set to be similar to the speed of the RF signal running down the helix. The signal in the wire causes a magnetic field to be induced in the center of the helix, where the electrons are flowing. Depending on the phase of the signal, the electrons will either be sped up or slowed down as they pass the windings. This causes the electron beam to "bunch up", known technically as "velocity modulation". The resulting pattern of electron density in the beam is an analog of the original RF signal.

Because the beam is passing the helix as it travels, and that signal varies, it causes induction in the helix, amplifying the original signal. By the time it reaches the other end of the tube, this process has had time to deposit considerable energy back into the helix. A second directional coupler, positioned near the collector, receives an amplified version of the input signal from the far end of the RF circuit. Attenuators placed along the RF circuit prevent the reflected wave from traveling back to the cathode.

Higher powered helix TWTs usually contain beryllium oxide ceramic as both a helix support rod and in some cases, as an electron collector for the TWT because of its special electrical, mechanical, and thermal properties.

### Comparison

There are a number of RF amplifier tubes that operate in a similar fashion to the TWT, known collectively as velocity-modulated tubes. The best known example is the klystron. All of these tubes use the same basic "bunching" of electrons to provide the amplification process, and differ largely in what process causes the velocity modulation to occur.

In the klystron, the electron beam passes through a hole in a resonant cavity which is connected to the source RF signal. The signal at the instant the electrons pass through the hole causes them to be accelerated (or decelerated). The electrons enter a "drift tube" in which faster electrons overtake the slower ones, creating the bunches, after which the electrons pass through another resonant cavity from which the output power is taken. Since the velocity sorting process takes time, the drift tube must often be several feet long.

In comparison, in the TWT the acceleration is caused by the interactions with the helix along the entire length of the tube. This allows the TWT to have a very low noise output, a major advantage of the design. More usefully, this process is much less sensitive to the physical arrangement of the tube, which allows the TWT to operate over a wider variety of frequencies. TWT's are generally at an advantage when low noise and frequency variability are useful.

### Coupled-cavity TWT

Helix TWTs are limited in peak RF power by the current handling (and therefore thickness) of the helix wire. As power level increases, the wire can overheat and cause the helix geometry to warp. Wire thickness can be increased to improve matters, but if the wire is too thick it becomes impossible to obtain the required helix pitch for proper operation. Typically helix TWTs achieve less than 2.5 kW output power.

The **coupled-cavity TWT** overcomes this limit by replacing the helix with a series of coupled cavities arranged axially along the beam. This structure provides a helical waveguide, and hence amplification can occur via velocity modulation. Helical waveguides have very nonlinear dispersion and thus are only narrowband (but wider than klystron). A coupled-cavity TWT can achieve 60 kW output power.

Operation is similar to that of a klystron, except that coupled-cavity TWTs are designed with attenuation between the slow-wave structure instead of a drift tube. The slow-wave structure gives the TWT its wide bandwidth. A free electron laser allows higher frequencies.

## Traveling-wave-tube amplifier

A TWT integrated with a regulated power supply and protection circuits is referred to as a traveling-wave-tube amplifier (abbreviated **TWTA** and often pronounced "TWEET-uh"). It is used to produce high-power radio frequency signals. The bandwidth of a broadband TWTA can be as high as one octave, although tuned (narrowband) versions exist; operating frequencies range from 300 MHz to 50 GHz.

A TWTA consists of a traveling-wave tube coupled with its protection circuits (as in klystron) and regulated power supply electronic power conditioner (EPC), which may be supplied and integrated by a different manufacturer. The main difference between most power supplies and those for vacuum tubes is that efficient vacuum tubes have depressed collectors to recycle kinetic energy of the electrons, so the secondary winding of the power supply needs up to 6 taps of which the helix voltage needs precise regulation. The subsequent addition of a linearizer (as for inductive output tube) can, by complementary compensation, improve the gain compression and other characteristics of the TWTA; this combination is called a linearized TWTA (LTWTA, "EL-tweet-uh").

Broadband TWTAs generally use a helix TWT and achieve less than 2.5 kW output power. TWTAs using a coupled cavity TWT can achieve 15 kW output power, but at the expense of narrower bandwidth.

## Invention, development and early use

The original design and prototype of the TWT was done by Andrei "Andy" Haeff c. 1931 while he was working as a doctoral student at the Kellogg Radiation Laboratory at Caltech. His original patent, "Device for and Method of Controlling High Frequency Currents", was filed in 1933 and granted in 1936.

The invention of the TWT is often attributed to Rudolf Kompfner in 1942–1943. In addition, Nils Lindenblad, working at RCA (Radio Corporation of America) in the USA also filed a patent for a device in May 1940 that was remarkably similar to Kompfner's TWT. Both of these devices were improvements over Haeff's original design as they both used the then newly invented precision electron gun as the source of the electron beam and they both directed the beam down the center of the helix instead of outside of it. These configuration changes resulted in much greater wave amplification than Haeff's design as they relied on the physical principles of velocity modulation and electron bunching. Kompfner developed his TWT in a British Admiralty radar laboratory during World War II. His first sketch of his TWT is dated November 12, 1942, and he built his first TWT in early 1943. The TWT was later refined by Kompfner, John R. Pierce, and Lester M. Winslow at Bell Labs. Note that Kompfner's US patent, granted in 1953, does cite Haeff's previous work.

By the 1950s, after further development at the Electron Tube Laboratory at Hughes Aircraft Company in Culver City, California, TWTs went into production there, and by the 1960s TWTs were also produced by such companies as the English Electric Valve Company, followed by Ferranti in the 1970s.

On July 10, 1962, the first communications satellite, Telstar 1, was launched with a 2 W, 4 GHz RCA-designed TWT transponder used for transmitting RF signals to Earth stations. Syncom 2 was successfully launched into geosynchronous orbit on July 26, 1963, with two 2 W, 1850 MHz Hughes-designed TWT transponders — one active and one spare.

## Uses

TWTAs are commonly used as amplifiers in satellite transponders, where the input signal is very weak and the output needs to be high power. TWTAs used in satellite communications are considered as reliable choices and tend to live beyond their expected lifetime of 15-20 years.

A TWTA whose output drives an antenna is a type of transmitter. TWTA transmitters are used extensively in radar, particularly in airborne fire-control radar systems, and in electronic warfare and self-protection systems. In such applications, a control grid is typically introduced between the TWT's electron gun and slow-wave structure to allow pulsed operation. The circuit that drives the control grid is usually referred to as a grid modulator.

TWTAs have found applications in a number of spacecraft, including all five of the space probes that have achieved the escape velocity to leave the Solar System. For example, dual redundant 12-watt X-band TWTAs are mounted on the body under the dish of the New Horizons spacecraft, which visited Pluto in 2015, then Kuiper belt object 486958 Arrokoth in 2019 to return data at a distance of 43.4 AU from the Sun. Launched in 2021, James Webb Space Telescope makes use of Ka-band TWTs.

## Historical notes

A TWT has sometimes been referred to as a "traveling-wave amplifier tube" (TWAT), although this term was never widely adopted. "TWT" has been pronounced by engineers as "twit", and "TWTA" as "tweeta".

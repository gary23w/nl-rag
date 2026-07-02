---
title: "Flyback transformer"
source: https://en.wikipedia.org/wiki/Flyback_transformer
domain: flyback-converter
license: CC-BY-SA-4.0
tags: flyback converter, flyback transformer, forward converter, isolated converter
fetched: 2026-07-02
---

# Flyback transformer

A **flyback transformer** (**FBT**), also called a **line output transformer** (**LOPT**), is a special type of electrical transformer. It was initially designed to generate high-voltage sawtooth signals at a relatively high frequency. In modern applications, it is used extensively in switched-mode power supplies for both low (3 V) and high voltage (over 10 kV) supplies.

## History

The flyback transformer circuit was invented as a means of controlling the horizontal movement of the electron beam in a cathode-ray tube (CRT). Unlike conventional transformers, a flyback transformer is not fed with a signal of the same waveshape as the intended output current. A convenient side effect of such a transformer is the considerable energy that is available in its magnetic circuit. This can be exploited using extra windings to provide power to operate other parts of the equipment. In particular, very high voltages are easily obtained using relatively few turns of windings which, after rectification, can provide a very high accelerating voltage for a CRT. Many more recent applications of such a transformer dispense with the need to produce high voltages and use the device as a relatively efficient means of producing a wide range of lower voltages using a transformer that is much smaller than a conventional mains transformer.

## Operation and usage

The primary winding of the flyback transformer is driven by a switch from a DC supply (usually a transistor). When the switch is closed, the primary inductance causes the current to build up in a ramp. An integral diode connected in series with the secondary winding prevents the development of a secondary current that would eventually oppose the primary current ramp.

When the switch is opened, the current in the primary falls to zero. The energy stored in the magnetic core is released to the secondary as the magnetic field in the core collapses. The voltage in the output winding rises very quickly (usually in less than a microsecond) until the load conditions limit it. Once the voltage reaches such a level as to allow a secondary current, the charge flow is like a descending ramp.

The cycle can then be repeated. If the secondary current is allowed to drop completely to zero (no energy stored in the core), then it is said that the transformer works in *discontinuous mode*. When the secondary current is always non-zero (some energy is always stored in the core), then this is *continuous mode*. This terminology is used especially in power supply transformers.

The low voltage output winding mirrors the sawtooth of the primary current and, e.g. for television purposes, has fewer turns than the primary, thus providing a higher current. This is a ramped and pulsed waveform that repeats at the horizontal (line) frequency of the display. The flyback (the vertical portion of the sawtooth wave) can be a potential problem for the flyback transformer if the energy has nowhere to go: the faster a magnetic field collapses, the greater the induced voltage, which, if not controlled, can flash over the transformer terminals. The high frequency used permits the use of a much smaller transformer. In television sets, this high frequency is about 15 kilohertz (15.625 kHz for PAL, 15.734 kHz for NTSC), and vibrations from the transformer core caused by magnetostriction can often be heard as a high-pitched whine. In CRT-based computer displays, the frequency can vary over a wide range, from about 30 kHz to 150 kHz.

The transformer can be equipped with extra windings whose sole purpose is to induce a relatively large voltage pulse when the magnetic field collapses as the input switch is turned off. There is considerable energy stored in the magnetic field, and coupling it out via extra windings helps it to collapse quickly, and avoids the voltage flash over that might otherwise occur. The pulse train coming from the flyback transformer windings is converted to direct current by a simple half-wave rectifier. There is no point in using a full wave design as there are no corresponding pulses of opposite polarity. One turn of a winding often produces pulses of several volts. In older television designs, the transformer produced the required high voltage for the CRT accelerating voltage directly with the output rectified by a simple rectifier. In more modern designs, the rectifier is replaced by a voltage multiplier. Color television sets must also use a regulator to control the high voltage. The earliest sets used a shunt vacuum tube regulator, but the introduction of solid-state sets employed a simpler voltage-dependent resistor. The rectified voltage is then used to supply the final anode of the cathode-ray tube.

There are often auxiliary windings that produce lower voltages for driving other parts of the television circuitry. The voltage used to bias the varactor diodes in modern tuners is often derived from the flyback transformer ("Line OutPut Transformer" LOPT). In tube sets, a one or two-turn filament winding is located on the opposite side of the core as the HV secondary, used to drive the HV rectifier tube's heater.

## Practical considerations

In modern displays, the LOPT, voltage multiplier, and rectifier are often integrated into a single package on the main circuit board. There is usually a thickly insulated wire from the LOPT to the anode terminal (covered by a rubber cap) on the side of the picture tube.

One advantage of operating the transformer at the flyback frequency is that it can be much smaller and lighter than a comparable transformer operating at mains (line) frequency. Another advantage is that it provides a failsafe mechanism — should the horizontal deflection circuitry fail, the flyback transformer will cease operating and shut down the rest of the display, preventing the screen burn-in that would otherwise result from a stationary electron beam.

## Construction

The primary is wound first around a ferrite rod, and then the secondary is wound around the primary. This arrangement minimizes the leakage inductance of the primary. Finally, a ferrite frame is wrapped around the primary/secondary assembly, closing the magnetic field lines. Between the rod and the frame is an air gap, which increases the reluctance. The secondary is wound layer by layer with enameled wire, and Mylar film between the layers. In this way, parts of the wire with a higher voltage difference have more dielectric material between them.

## Applications

The flyback transformer operates CRT-display devices such as television sets and CRT computer monitors. The voltage and frequency can each range over a wide scale, depending on the device. For example, a large color TV CRT may require 20 to 50 kV with a horizontal scan rate of 15.734 kHz for NTSC devices and 15.625 kHz for PAL devices. Unlike a power (or "mains") transformer, which uses an alternating current of 50 or 60 hertz, a flyback transformer typically operates with switched currents at much higher frequencies in the range of 15 kHz to 50 kHz.

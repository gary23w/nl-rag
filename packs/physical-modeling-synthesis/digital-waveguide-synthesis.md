---
title: "Digital waveguide synthesis"
source: https://en.wikipedia.org/wiki/Digital_waveguide_synthesis
domain: physical-modeling-synthesis
license: CC-BY-SA-4.0
tags: physical modeling synthesis, karplus strong synthesis, digital waveguide synthesis, string physical model
fetched: 2026-07-02
---

# Digital waveguide synthesis

**Digital waveguide synthesis** is the synthesis of audio using a digital waveguide. Digital waveguides are efficient computational models for physical media through which acoustic waves propagate. For this reason, digital waveguides constitute a major part of most modern physical modeling synthesizers.

A lossless digital waveguide realizes the discrete form of d'Alembert's solution of the one-dimensional wave equation as the superposition of a right-going and a left-going waves,

$y(m,n)=y^{+}(m-n)+y^{-}(m+n),$

where $y^{+}$ is the right-going wave, and $y^{-}$ is the left-going wave. It can be seen from this representation that sampling the function y at a given position m and time n merely involves summing two delayed copies of its traveling waves. These traveling waves will reflect at boundaries such as the suspension points of vibrating strings or the open or closed ends of tubes. Hence the waves travel along closed loops.

Digital waveguide models therefore comprise digital delay lines to represent the geometry of the waveguide which are closed by recursion, digital filters to represent the frequency-dependent losses and mild dispersion in the medium, and often non-linear elements. Losses incurred throughout the medium are generally consolidated so that they can be calculated once at the termination of a delay line, rather than many times throughout.

Waveguides such as acoustic tubes are three-dimensional, but because their lengths are often much greater than their diameters, it is reasonable and computationally efficient to model them as one-dimensional waveguides. Membranes, as used in drums, may be modeled using two-dimensional waveguide meshes, and reverberation in three-dimensional spaces may be modeled using three-dimensional meshes. Vibraphone bars, bells, singing bowls and other sounding solids (also called idiophones) can be modeled by a related method called banded waveguides, where multiple band-limited digital waveguide elements are used to model the strongly dispersive behavior of waves in solids.

The term "digital waveguide synthesis" was coined by Julius O. Smith III, who helped develop it and eventually filed the patent. A digital waveguide model of an ideal vibrating string having a single point of damping implemented as a two-point average and initialized to random initial positions and velocities at every sample can be shown to be equivalent to the Karplus–Strong algorithm which was developed some years earlier. Stanford University owned the patent rights for digital waveguide synthesis and signed an agreement in 1989 with Yamaha to develop the technology. All early patents have expired and new products based on the technology are appearing frequently.

An extension to DWG synthesis of strings made by Smith is commuted synthesis, wherein the excitation to the digital waveguide contains both string excitation and the body response of the instrument. This is possible under the assumption that the string and body are linear time-invariant systems, which is approximately true for typical instruments, allowing the excited body to drive the string, instead of the excited string driving the body as usual. Thus, the string is excited by a "plucked body response". This means it is unnecessary to model the instrument body's resonances explicitly using hundreds of digital filter sections, thereby greatly reducing the number of computations required for a convincing resynthesis.

Prototype waveguide software implementations were done by students of Smith in the Synthesis Toolkit (STK).

The first musical use of the Extended Karplus Strong (EKS) algorithm was in the composition "May All Your Children Be Acrobats" (1981) by David A. Jaffe, followed by his "Silicon Valley Breakdown" (1982). Since the EKS became understood as a special case of digital waveguide synthesis years later, the piece can now be considered the earliest use of digital waveguide synthesis as well.

Related was "A Bicycle Built for Two" by Max Mathews, John Kelly, and Carol Lochbaum at Bell Labs in 1961, which used the Kelly–Lochbaum ladder filter to model the human vocal tract. To distinguish ladder filters from digital waveguide filters, a digital waveguide is defined as a bidirectional delay line at least two samples long over which no scattering occurs.

## Licensees

- Yamaha
  - VL1 (1994) — expensive keyboard (about $10,000 USD)
  - VL1m, VL7 (1994) — tone module and less expensive keyboard, respectively
  - VP1 (prototype) (1994)
  - VL70m (1996) — less expensive tone module
  - EX5 (1999) — workstation keyboard that included a VL module
  - PLG-100VL, PLG-150VL (1999) — plug-in cards for various Yamaha keyboards, tone modules, and the SWG-1000 high-end PC sound card. The MU100R rack-mount tone module included two PLG slots, pre-filled with a PLG-100VL and a PLG-100VH (Vocal Harmonizer).
  - YMF-724, 744, 754, and 764 sound chips for inexpensive DS-XG PC sound cards and motherboards (the VL part only worked on Windows 95, 98, 98SE, and ME, and then only when using `.VxD` drivers, not `.WDM`). No longer made, presumably due to conflict with AC-97 and AC-99 sound card standards (which specify 'wavetables' (sample tables) based on Roland’s XG-competing GS sound system, which Sondius-XG [the means of integrating VL instruments and commands into an XG-compliant MIDI stream along with wavetable XG instruments and commands] cannot integrate with). The MIDI portion of such sound chips, when the VL was enabled, was functionally equivalent to an MU50 Level 1 XG tone module (minus certain digital effects) with greater polyphony (up to 64 simultaneous notes, compared to 32 for Level 1 XG) plus a VL70m (the VL adds an additional note of polyphony, or, rather, a VL solo note backed up by the up-to-64 notes of polyphony of the XG wavetable portion). The 724 only supported stereo out, while the others supported various four and more speaker setups. Yamaha’s own card using these was the WaveForce-128, but a number of licensees made very inexpensive YMF-724 sound cards that retailed for as low as $12 at the peak of the technology’s popularity. The MIDI synth portion (both XG and VL) of the YMF chips was actually just hardware assist to a mostly software synth that resided in the device driver (the XG wavetable samples, for instance, were in system RAM with the driver [and could be replaced or added to easily], not in ROM on the sound card). As such, the MIDI synth, especially with VL in active use, took considerably more CPU power than a truly hardware synth would use, but not as much as a pure software synth. Towards the end of their market period, YMF-724 cards could be had for as little as $12 USD brand new, making them by far the least expensive means of obtaining Sondius-XG CL digital waveguide technology. The DS-XG series also included the YMF-740, but it lacked the Sondius-XG VL waveguide synthesis module, yet was otherwise identical to the YMF-744.
  - S-YXG100plus-VL Soft Synthesizer for PCs with any sound card (again, the VL part only worked on Windows 95, 98, 98SE, and ME: it emulated a .VxD MIDI device driver). Likewise equivalent to an MU50 (minus certain digital effects) plus VL70m. The non-VL version, S-YXG50, would work on any Windows OS, but had no physical modeling, and was just the MU50 XG wavetable emulator. This was basically the synth portion of the YMF chips implemented entirely in software without the hardware assist provided by the YMF chips. Required a somewhat more powerful CPU than the YMF chips did. Could also be used in conjunction with a YMF-equipped sound card or motherboard to provide up to 128 notes of XG wavetable polyphony and up to two VL instruments simultaneously on sufficiently powerful CPUs.
  - S-YXG100plus-PolyVL SoftSynth for then-powerful PCs (e. g. 333+MHz Pentium III), capable of up to eight VL notes at once (all other Yamaha VL implementations except the original VL1 and VL1m were limited to one, and the VL1/1m could do two), in addition to up to 64 notes of XG wavetable from the MU50-emulating portion of the soft synth. Never sold in the US, but was sold in Japan. Presumably a much more powerful system could be done with today’s multi-GHz dual-core CPUs, but the technology appears to have been abandoned. Hypothetically could also be used with a YMF chipset system to combine their capabilities on sufficiently powerful CPUs.
- Korg
  - Prophecy (1995)
  - Z1, MOSS-TRI (1997)
  - EXB-MOSS (2001)
  - OASYS PCI (1999)
  - OASYS (2005) with some modules, for instance the STR-1 plucked strings physical model
  - Kronos (2011) same as OASYS
- Technics
  - WSA1 (1995) PCM + resonator
- Seer Systems
  - Creative WaveSynth (1996) for Creative Labs Sound Blaster AWE64.
  - Reality (1997) - one of the earliest professional software synthesizer products by Dave Smith team
- Cakewalk
  - Dimension Pro (2005) - software synthesizer for OS X and Windows XP.
- Mordartt
  - Pianoteq (since 2005, continued) - Piano emulation software for Windows, macOS, Linux and iOS.
- Applied Acoustic Systems
  - AAS String Studio (as from 2026) - String Oscillator Software for Windows and macOS.

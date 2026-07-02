---
title: "Ferrite bead"
source: https://en.wikipedia.org/wiki/Ferrite_bead
domain: emi-filtering
license: CC-BY-SA-4.0
tags: ferrite bead, common mode choke, line filter, electromagnetic interference
fetched: 2026-07-02
---

# Ferrite bead

A **ferrite bead** – also called a **ferrite block**, **ferrite core**, **ferrite ring**, **EMI filter**, or **ferrite choke** – is a type of choke that suppresses high-frequency electronic noise in electronic circuits.

Ferrite beads employ high-frequency current dissipation in a ferrite ceramic to build high-frequency noise suppression devices.

## Use

Ferrite beads prevent electromagnetic interference (EMI) in two directions: *from* a device or *to* a device. A conductive cable acts as an antenna – if the device produces radio-frequency energy, this can be *transmitted* through the cable, which acts as an unintentional radiator. In this case, the bead is required for regulatory compliance to reduce EMI. Conversely, if there are other sources of EMI, such as household appliances, the bead prevents the cable from acting as an antenna and *receiving* interference from these other devices. This is particularly common on data cables and medical equipment.

Large ferrite beads are commonly seen on external cabling. In addition, various smaller ferrite beads are used internally in circuits—on conductors or around the pins of small circuit-board components, such as transistors, connectors, and integrated circuits.

Beads can block low-level unintended radio frequency energy on wires intended to be DC conductors by acting as a low-pass filter. For example, on unbalanced coax transmission lines (such as video cables), the cable is designed to contain the signal, and beads can be used to block stray common mode current from using the cable as an antenna while not interfering with the signal carried inside the cable. In this use, the bead is a simple form of a balun.

Ferrite beads are one of the simplest and least expensive interference filters to install on preexisting electronic cabling. For a simple ferrite ring, the wire is wrapped around the core through the center, typically five or seven times. Clamp-on cores are also available, which attach without wrapping the wire: this type of ferrite core is usually designed so that the wire passes only once through it. If the fit is not snug enough, the core can be secured with cable ties, or if the center is large enough, the cabling can loop through one or more times. (However, although each loop increases the impedance to high frequencies, it also shifts the frequency of the highest impedance to a lower frequency.) Small ferrite beads can be slipped over component leads to suppress parasitic oscillation.

Surface-mount ferrite beads are available. Like any other surface-mount inductor, these are soldered into a gap in the printed circuit board trace. Inside the bead component, a coil of wire runs between layers of ferrite to form a multi-turn inductor around the high-permeability core.

## Theory of operation

Ferrite beads are used as a passive low-pass filter by dissipating radio frequency (RF) energy as heat by design.

Ideal inductors, on the other hand, have no resistance and hence do not dissipate energy as heat. Ideal inductors only have inductive reactance, which reduces the flow of high-frequency signals by returning some of their energy back towards the signal source (possibly reducing the amount of power drawn) rather than dissipating that energy as heat (as done by the resistance in ferrite beads). While an inductor's reactance may commonly be referred to simply as *impedance*, impedance generally can be any combination of resistance and reactance.

The geometry and electromagnetic properties of coiled wire over the ferrite bead result in an impedance for high-frequency signals, attenuating high-frequency EMI/RFI electronic noise. The energy is either reflected back up the cable or dissipated as low-level heat. Only in extreme cases is the heat noticeable.

A ferrite bead can be added to an inductor to improve, in two ways, its ability to block unwanted high frequency noise. First, the ferrite concentrates the magnetic field, increasing inductance and, therefore, reactance, which filters out the noise. Second, if the ferrite is so designed, it can produce an additional loss in the form of resistance in the ferrite itself. The ferrite creates an inductor with a very low Q factor. This loss heats the ferrite, generally by a negligible amount. While the signal level is large enough to cause interference or undesirable effects in sensitive circuits, the energy blocked is typically relatively small. Depending on the application, the resistive loss characteristic of the ferrite may or may not be desired.

A design that uses a ferrite bead to improve noise filtering must consider specific circuit characteristics and the frequency range to block. Different ferrite materials have different properties concerning frequency, and the manufacturer's literature helps select the most effective material for the frequency range.

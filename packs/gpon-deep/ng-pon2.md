---
title: "NG-PON2"
source: https://en.wikipedia.org/wiki/NG-PON2
domain: gpon-deep
license: CC-BY-SA-4.0
tags: gigabit pon, passive optical network, optical line termination, fiber access
fetched: 2026-07-02
---

# NG-PON2

**NG-PON2** (also known as **TWDM-PON**), *Next-Generation Passive Optical Network 2* is a 2015 telecommunications network standard for a passive optical network (PON). The standard was developed by ITU and details an architecture capable of total network throughput of 40 Gbit/s, corresponding to up to 10 Gbit/s symmetric upstream/downstream speeds available at each subscriber.

A passive optical network is a last mile, fibre-to-the-x telecommunications network that broadcasts data through fibre optic cables. PONs are managed by passive optics such as unpowered splitters and filters, offering high reliability and low cost compared to active networks. The PON data stream is generally converted to a more traditional service such as Ethernet and Wi-Fi at the subscriber's location.

NG-PON2 is compatible with existing PON fibre by replacing optical line terminal (OLT) at the central office, and the optical network unit (ONU) near each end-user.

Unique to this standard is the use of both active filters and tunable lasers in the ONU.

From 2019 until 2021 a series of new Recommendations under the header Higher Speed PON (G.9804 series) was released intended as successors to NG-PON2.

## Technical details

Wavelength allocations include 1524 nm to 1544 nm in the upstream direction and 1596 nm to 1602 nm in the downstream direction.

The architecture calls for time- and wavelength-division multiplexing (**TWDM**) in the upstream and downstream directions. Wavelength-division multiplexing is provided in the downstream direction by combining light from four fixed wavelength OLT lasers with a wavelength mux. The light is then filtered at each ONU with an actively tunable filter that passes only the desired downstream wavelength to its receiver. In the upstream direction, tunable lasers at each ONU are dynamically assigned to a wavelength. Fibres from all ONUs are combined with a passive mux/splitter. Time-division multiplexing is provided in the upstream direction through the use of burst lasers at each ONU.

Each upstream/downstream wavelength is capable of providing up to 10 Gbit/s symmetric bandwidth to each subscriber if the channel is not time-division multiplexed between several ONUs. With wavelength-division multiplexing on four available wavelengths, NG-PON2 can provide up to 40 Gbit/s throughput to the entire optical network.

Deployments for several downstream/upstream subscriber rates are described within the standard including 10/10 Gbit/s at each subscriber, 10/2.5 Gbit/s, and 2.5/2.5 Gbit/s. Additionally, some wavelengths are reserved for potential use in Point-to-Point applications.

NG-PON2 was designed to include backwards-compatibility, or coexistence, with previous architectures to ease deployment into existing optical distribution networks. Wavelengths were specifically chosen to avoid interference with GPON, 10G-PON, RF Video, and OTDR measurements. The standard provides spectral flexibility to occupy reserved wavelengths in deployments devoid of legacy architectures. Additionally, a mux/demux used to combine and separate the NG-PON2 wavelength channels at the OLT can be designed with a coexistence element to isolate legacy wavelengths.

## Standards

The ITU-T G.989 standard is divided into these subsections:

- G.989.1 – General Requirements
- G.989.2 – Physical media dependent (PMD) layer specification
- G.989.3

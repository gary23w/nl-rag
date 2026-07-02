---
title: "Load pull"
source: https://en.wikipedia.org/wiki/Load_pull
domain: rf-amplifiers
license: CC-BY-SA-4.0
tags: distributed amplifier, Doherty amplifier, traveling wave tube, load pull
fetched: 2026-07-02
---

# Load pull

**Load-pull** is the colloquial term applied to the process of systematically varying the impedance presented to a device under test (DUT), most often a transistor, to assess its performance and the associated conditions to deliver that performance in a network. While load-pull itself implies impedance variation at the load port, impedance can also be varied at any of the ports of the DUT, most often at the source.

Load-pull is required when superposition is no longer applicable, which occurs under large-signal operating conditions that make linear approximations unusable. The term load-pull derives from classical oscillator characterization whereupon variation of the load impedance pulls the oscillation center frequency away from nominal. Source-pull is also used for noise characterization, which, although linear, requires multiple impedances to be presented at the source to enable simultaneous solution of an over-determined system that yields the four noise parameters.

Load-pull is the most common method globally for RF and MW power amplifier (PA) design, transistor characterization, semiconductor process development, and ruggedness analysis. A central theme of load-pull is management of nonlinearity versus analysis of nonlinearity, the latter being the domain of advanced mathematics that often yields little physical insight to nonlinear phenomena and suffers from an inability to accurately render actual behavior embedded in a network with significant parasitic and distributed effects. With automated load-pull, it is possible to fully optimize and design a final stage for GSM applications in less than a day, thereby providing a dramatic reduction in design cycle-time while assuring the best possible performance trade-off has been achieved.

While there are in theory no physical limits on the frequency of which load-pull can be performed, most load-pull systems are based on passive distributed networks using either the slab transmission line in its TEM mode or the rectangular waveguide in its TE10 mode. Lumped tuners can be made for HF and VHF frequencies, whereas active load-pull is ideal for on-wafer mm-wave environments, where substantial loss between the tuner and DUT reference-plane limits maximum VSWR.

---
title: "Silicon on insulator"
source: https://en.wikipedia.org/wiki/Silicon-on-insulator
domain: cmos-technology
license: CC-BY-SA-4.0
tags: cmos technology, mosfet transistor, finfet device, threshold voltage
fetched: 2026-07-02
---

# Silicon on insulator

(Redirected from

Silicon-on-insulator

)

In semiconductor manufacturing, **silicon on insulator** (**SOI**) technology is fabrication of silicon semiconductor devices in a layered silicon–insulator–silicon substrate, to reduce parasitic capacitance within the device, thereby improving performance. SOI-based devices differ from conventional silicon-built devices in that the silicon junction is above an electrical insulator, typically silicon dioxide or sapphire (these types of devices are called silicon on sapphire, or SOS). The choice of insulator depends largely on intended application, with sapphire being used for high-performance radio frequency (RF) and radiation-sensitive applications, and silicon dioxide for diminished short-channel effects in other microelectronics devices. The insulating layer and topmost silicon layer also vary widely with application.

## Industry need

SOI technology is one of several manufacturing strategies to allow the continued miniaturization of microelectronic devices, colloquially referred to as "extending Moore's law" (or "more moore", abbreviated "MM"). Reported benefits of SOI relative to conventional silicon (bulk CMOS) processing include:

- Lower parasitic capacitance due to isolation from the bulk silicon, which improves power consumption at matched performance
- Resistance to latchup due to complete isolation of the n- and p-well structures
- Higher performance at equivalent VDD. Can work at low VDDs
- Reduced temperature dependency due to no doping
- Better yield due to high density, better wafer utilization
- Reduced antenna issues
- No body or well taps are needed
- Lower leakage currents due to isolation thus higher power efficiency
- Inherently radiation hardened (resistant to soft errors), reducing the need for redundancy

From a manufacturing perspective, SOI substrates are compatible with most conventional fabrication processes. In general, an SOI-based process may be implemented without special equipment or significant retooling of an existing factory. Among challenges unique to SOI are novel metrology requirements to account for the buried oxide layer and concerns about differential stress in the topmost silicon layer. The threshold voltage of the transistor depends on the history of operation and applied voltage to it, thus making modeling harder. The primary barrier to SOI implementation is the drastic increase in substrate cost, which contributes an estimated 10–15% increase to total manufacturing costs. FD-SOI (fully depleted silicon on insulator) has been seen as a potential low cost alternative to FinFETs.

## SOI transistors

An SOI MOSFET is a metal–oxide–semiconductor field-effect transistor (MOSFET) device in which a semiconductor layer such as silicon or germanium is formed on an insulator layer which may be a buried oxide (BOX) layer formed in a semiconductor substrate. SOI MOSFET devices are adapted for use by the computer industry. The buried oxide layer can be used in SRAM designs. There are two types of SOI devices: PDSOI (partially depleted SOI) and FDSOI (fully depleted SOI) MOSFETs. For a PDSOI P-MOSFET the sandwiched n-type film between the gate oxide (GOX) and buried oxide (BOX) is large, so the depletion region can't cover the whole n region. So to some extent PDSOI behaves like bulk MOSFET. Obviously there are some advantages over the bulk MOSFETs. The film is very thin in FDSOI devices so that the depletion region covers the whole channel region. In FDSOI the front gate (GOX) supports fewer depletion charges than the bulk so an increase in inversion charges occurs resulting in higher switching speeds. The limitation of the depletion charge by the BOX induces a suppression of the depletion capacitance and therefore a substantial reduction of the subthreshold swing allowing FD SOI MOSFETs to work at lower gate bias resulting in lower power operation. The subthreshold swing can reach the minimum theoretical value for MOSFET at 300K, which is 60mV/decade. This ideal value was first demonstrated using numerical simulation. Other drawbacks in bulk MOSFETs, like threshold voltage roll off, etc. are reduced in FDSOI since the source and drain electric fields can't interfere due to the BOX. The main problem in PDSOI is the "floating body effect (FBE)" since the film is not connected to any of the supplies.

## Manufacture of SOI wafers

SiO 2-based SOI wafers can be produced by several methods:

- *SIMOX* - separation by implantation of oxygen – uses an oxygen ion beam implantation process followed by high temperature annealing to create a buried SiO 2 layer.
- Wafer bonding – the insulating layer is formed by directly bonding oxidized silicon with a second substrate. The majority of the second substrate is subsequently removed, the remnants forming the topmost Si layer.
  - One prominent example of a wafer bonding process is the *smart cut* method developed by the French firm Soitec which uses ion implantation followed by controlled exfoliation to determine the thickness of the uppermost silicon layer. Another early method is Bond and Etch-Back SOI (BESOI), which involves bonding an oxidized wafer to a second wafer and then etching back one wafer to form a thin silicon film over the oxide.
  - *NanoCleave* is a technology developed by Silicon Genesis Corporation that separates the silicon via stress at the interface of silicon and silicon-germanium alloy.
  - *ELTRAN* is a technology developed by Canon which is based on porous silicon and water cut.
- Seed methods - wherein the topmost Si layer is grown directly on the insulator. Seed methods require some sort of template for homoepitaxy, which may be achieved by chemical treatment of the insulator, an appropriately oriented crystalline insulator, or vias through the insulator from the underlying substrate.

An exhaustive review of these various manufacturing processes may be found in reference

## Use in the microelectronics industry

IBM began to use SOI in the high-end RS64-IV "Istar" PowerPC-AS microprocessor in 2000. Other examples of microprocessors built on SOI technology include AMD's 130 nm, 90 nm, 65 nm, 45 nm and 32 nm single, dual, quad, six and eight core processors since 2001. Freescale adopted SOI in their PowerPC 7455 CPU in late 2001, currently Freescale is shipping SOI products in 180 nm, 130 nm, 90 nm and 45 nm lines. The 90 nm PowerPC- and Power ISA-based processors used in the Xbox 360, PlayStation 3, and Wii use SOI technology as well. Competitive offerings from Intel however continue to use conventional bulk CMOS technology for each process node, instead focusing on other venues such as HKMG and tri-gate transistors to improve transistor performance. In January 2005, Intel researchers reported on an experimental single-chip silicon rib waveguide Raman laser built using SOI.

As for the traditional foundries, in July 2006 TSMC claimed no customer wanted SOI, but Chartered Semiconductor devoted a whole fab to SOI.

## Use in high-performance radio frequency (RF) applications

In 1990, Peregrine Semiconductor began development of an SOI process technology utilizing a standard 0.5 μm CMOS node and an enhanced sapphire substrate. Its patented silicon on sapphire (SOS) process is widely used in high-performance RF applications. The intrinsic benefits of the insulating sapphire substrate allow for high isolation, high linearity and electro-static discharge (ESD) tolerance. Multiple other companies have also applied SOI technology to successful RF applications in smartphones and cellular radios.

The superior electrical isolation of SOI substrates makes the technology pivotal for a wide range of modern RF components. This enables the development of highly integrated, efficient, and linear circuits that are critical for advanced communication systems. Key applications leveraging these advantages include RF waveguides for 5G networks and satellite communications, high-linearity RF amplifiers and transceivers for automotive and virtual reality applications, and compact, tunable RF filters for next-generation wireless devices. The technology's ability to integrate multiple RF components onto a single chip supports the ongoing trend towards more compact and multifunctional wireless communication systems.

## Use in photonics

SOI wafers are widely used in silicon photonics. The crystalline silicon layer on insulator can be used to fabricate optical waveguides and other optical devices, either passive or active (e.g. through suitable implantations). The buried insulator enables propagation of infrared light in the silicon layer on the basis of total internal reflection. The top surface of the waveguides can be either left uncovered and exposed to air (e.g. for sensing applications), or covered with a cladding, typically made of silica

## Disadvantages

The major disadvantage of SOI technology when compared to conventional semiconductor industry is increased cost of manufacturing. As of 2012 only IBM and AMD used SOI as basis for high-performance processors and the other manufacturers (Intel, TSMC, Global Foundries etc.) used conventional silicon wafers to build their CMOS chips.

## SOI market

As of 2020 the market utilizing the SOI process was projected to grow up by ~15% for the next 5 years according to Market Research Future group.

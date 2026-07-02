---
title: "Foundation Fieldbus"
source: https://en.wikipedia.org/wiki/Foundation_Fieldbus
domain: foundation-fieldbus
license: CC-BY-SA-4.0
tags: foundation fieldbus, fieldbus function block, process automation fieldbus, h1 fieldbus
fetched: 2026-07-02
---

# Foundation Fieldbus

**Foundation Fieldbus** (styled **Foundation Fieldbus**) is an all-digital, serial, two-way communications system that serves as the base-level network in a plant or factory automation environment. It is an open architecture, developed and administered by FieldComm Group.

It is targeted for applications using basic and advanced regulatory control, and for much of the discrete control associated with those functions. Foundation Fieldbus technology is mostly used in process industries, but has recently been implemented in powerplants.

Two related implementations of Foundation Fieldbus have been introduced to meet different needs within the process automation environment. These two implementations use different physical media and communication speeds.

- *Foundation Fieldbus H1* - Operates at 31.25 kbit/s and is generally used to connect to field devices and host systems. It provides communication and power over standard stranded twisted-pair wiring in both conventional and intrinsic safety applications. H1 is currently the most common implementation.
- *HSE* (High-speed Ethernet) - Operates at 100/1000 Mbit/s and generally connects input/output subsystems, host systems, linking devices and gateways. It doesn't currently provide power over the cable, although work is under way to address this using the IEEE802.3af Power over Ethernet (PoE) standard.

Foundation Fieldbus was originally intended as a replacement for the 4-20 mA standard, and today it coexists alongside other technologies such as Modbus, Profibus, and Industrial Ethernet. Foundation Fieldbus today enjoys a growing installed base in many heavy process applications such as refining, petrochemicals, power generation, and even food and beverage, pharmaceuticals, and nuclear applications.

Foundation Fieldbus was developed over a period of many years by the International Society of Automation, or ISA, as SP50. In 1996 the first H1 (31.25 kbit/s) specifications were released. In 1999 the first HSE (High Speed Ethernet) specifications were released. The International Electrotechnical Commission (IEC) standard on field bus, including Foundation Fieldbus, is IEC 61158. Type 1 is Foundation Fieldbus H1, while Type 5 is Foundation Fieldbus HSE.

A typical fieldbus segment consists of the following components:

- H1 card - fieldbus interface card (It is common practice to have redundant H1 cards, but ultimately this is application specific);
- PS - Bulk power (Vdc) to Fieldbus Power Supply;
- FPS - Fieldbus Power Supply and Signal Conditioner (Integrated power supplies and conditioners have become the standard nowadays)
- T - Terminators (Exactly 2 terminators are used per fieldbus segment. One at the FPS and one at the furthest point of a segment at the device coupler);
- LD - Linking Device, alternatively used with HSE networks to terminate 4-8 H1 segments acting as a gateway to an HSE backbone network; and
- Fieldbus devices, (such as transmitters and transducers)

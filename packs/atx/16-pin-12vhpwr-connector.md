---
title: "12VHPWR"
source: https://en.wikipedia.org/wiki/16-pin_12VHPWR_connector
domain: atx
license: CC-BY-SA-4.0
tags: atx
fetched: 2026-07-03
---

# 12VHPWR

(Redirected from

16-pin 12VHPWR connector

)

The **16-pin 12VHPWR connector** is a standard for connecting graphics processing units (GPUs) to computer power supplies for up to 600 W power delivery. It was introduced by Nvidia in 2022 to supersede the previous 6- and 8-pin power connectors for GPUs. The stated aim was to cater to the increasing power requirements of Nvidia GPUs. The connector was formally adopted as part of PCI Express 5.

The connector was replaced by a minor revision called **12V-2x6**, introduced in 2023 with PCIe CEM 5.1 and PCIe ECN 6.0, which changed the GPU- and PSU-side sockets to ensure that the sense pins only make contact if the power pins are seated properly. The cables and their plugs remained unchanged. The change is intended to prevent melting due to partial contact, but melting continued to be reported for GPUs with this new socket. There is a significant change in power negotiation with a new sense pin added.

12VHPWR connectors are marked with an "H+" symbol, whereas 12V-2x6 connectors are marked with an "H++" symbol.

## Overview

The connector first appeared in the Nvidia RTX 40 GPUs. The prior Nvidia RTX 30 series introduced a similar, proprietary connector in the "Founder's Edition" cards, which also uses an arrangement of twelve pins for power, but did not have the sense pins, except for the connector on the founders edition RTX 3090 Ti (though not present on the adapter supplied with those cards.)

The 16-pin 12VHPWR connector, where "12V" signifies the use of 12 volts and "HPWR" stands for "high power", supports higher power delivery to GPUs, up to 600 watts, a significant increase from the 150 watts of the 8-pin connector and the 75 watts of the 6-pin connector. The 16-pin connector comprises twelve power pins arranged in two parallel rows, and four auxiliary sense pins that communicate the maximum allowable power draw. The plug housing should be colored black and made out of glass fibre-filled thermoplastic meeting the UL 94 V-0 classification for flame retardancy. The pins should be made out of copper alloy with tin-plated contact areas. The power cables shall be 16 AWG thick.

Adapters converting multiple 8-pin to a single 16-pin connector are available.

With respect to power supplies, the 12VHPWR connector was first specified in the ATX12V 3.0 specification, where it was specified as required for PSUs over 450 W and optional for lower-wattage PSUs. As of the ATX12V 3.1 specification, "New power supply designs should mount only the 12V-2x6 connector and the 12VHPWR connector should be deprecated."

### Sense behavior

| Sense0 | Sense 1 | 12VHPWR (5.0) | 12VHPWR (ECR) | 12v-2x6 |
|---|---|---|---|---|
| Open | Open | 225/450 | 100/150 | 0/0 |
| Shorted | Undefined, treated as Open/Open | 100/150 |   |   |
| Ground | Open | 375/600 | 150/300 | 150/300 |
| Open | Ground | 225/450 | 225/450 | 225/450 |
| Ground | Ground | 375/600 | 375/600 | 375/600 |

The above table describes the behavior of sense pins on 12VHPWR and 12V-2x6.

- The published version of 12VHPWR in PCIe CEM 5.0 had no requirement for the sense pin; with no sense pins connected, it provides 225 W for startup and 450 W for operation after configuration.
- The Engineering Change Request (ECR) modifies the default level of lower to be at a lower level of 100/150 W, requiring the a new sense pin to be connected to make use of the higher power levels provided by 12VHPWR.
- The 12v-2x6 connector of PCIe CEM 5.1/6.0 is largely similar to the ECR behavior, except that for having no sense pin connected no longer provides *any* power: to get the lowest level, the two sense pins should be shorted together.

### Power excursion

There is an add-on Engineering Change Notice (ECN) to PCIe CEM 5.0 describing a requirement for the computer PSU to handle *power excursion*, short-term peak loads that exceed the stated maximum (sustained) permitted power on the connector. A power supply must be able to handle a 100-microsecond power draw at 3× of maximum sustained power. A similar change has been incorporated into PCIe CEM 5.1 for all add-in card power connectors. The ECN is part of ATX 3.0 and PCIe CEM 5.1 is part of ATX 3.1.

## Reliability and design changes

### Nvidia RTX 4090

Some buyers of the Nvidia RTX 4090, the first GPU to use the new connector, reported that the connectors of their RTX 4090 were melting, which sparked several theories to explain it. After investigation, several sources reported that the main cause was the 12VHPWR connector not being fully seated while being put under load that resulted in overheating of the connector's pins, which in turn caused the melting of the plastic housing.

PCI-SIG, the standards organization responsible for the creation of the 12VHPWR connector, has decided to make changes to the connector's specifications following the failures.

A class-action lawsuit has been filed against Nvidia over melting 12VHPWR cables which the lawsuit states is "a dangerous product that should not have been sold in its current state". The plaintiff who brought the suit claims that Nvidia unjustly enriched itself, violated the product's warranty and engaged in fraud and they are demanding that Nvidia pay damages to affected customers as compensation. However, this lawsuit was voluntarily dismissed with prejudice by the plaintiff on March 10, 2023. No reason is provided as to why the case was dismissed.

Following its own investigation and testing, Nvidia officially offered a statement on the melting connectors. They determined that the melting connectors are caused by user error from not inserting the 12VHPWR connector properly, causing partial contact. They have offered an expedited RMA process for any RTX 4090 affected by the melting connectors. PCI-SIG later said in a statement that Nvidia and their partners were still responsible for testing their products to account for user error.

A revised connector design intended to address these issues was introduced under the new name 12V-2x6.

In February 2024, the U.S. Consumer Product Safety Commission announced a voluntary recall of 12VHPWR adapters made by Cablemod. According to the recall filing, 272 reports were filed with about 25,300 units shipped. The recall covers adapters using both the initial and the revised 12V-2x6 (CEM 5.1) design.

It was also reported that the new connectors have a limited lifespan of around 30–40 mating cycles before contact potentially becoming unreliable.

It has been also noted that the older 6- and 8-pin connectors had substantially larger manufacturer-specified current-carrying capacity in relation to the power limits specified by PCI SIG:

| Connector | 8-pin power | 12VHPWR (H+) / 12V-2x6 (H++) |
|---|---|---|
| Rated current per pin | 4 – 7 A | 9.5 A |
| Rated power | 7 A × 12 V × 3 pin = 252 W | 9.5 A × 12 V × 6 pin = 684 W |
| Specified power | 150 W | 525 W / 600 W |
| Safety factor | 1.68 | 1.30 / 1.14 |

**Notes**

1. Depending on the wire cross-section. HCS-type terminals have lower contact resistances, permitting even higher currents and more mating cycles.
2. For the entire connector with all applicable pins loaded at 12 V. The old 8-pin power connector only uses three pins each for ground and 12 V. For this calculation the nominal voltage is used instead of considering the ATX 2.0/3.0 tolerance band.
3. Specified in the PCI-SIG CEM specification

### Nvidia RTX 5090

The GeForce RTX 50 series use the new 12V-2x6 socket instead of the 12VHPWR. However, the high end RTX 5090 graphics card continued to show melting issues. These flaws are currently only confirmed on the RTX 5090 FE, but the removal of shunt resistors means the new re-design of the Nvidia cards exposes all cards to this flaw. Asus cards and some other brands add additional shunt resistors to detect potential overheating and warn the user, but without the ability to dynamically current balance and prevent overheating.

Analysis of hardware design of the flagship Nvidia GPUs of the last few generations showed a crucial change. The earlier GPU models with 6- or 8-pin power connectors usually had a separate current sensor per each connector. It allowed the GPU to monitor whether the load is distributed evenly among the connectors. The Nvidia RTX 30 series achieved the same by splitting the six 12V pins of the 12VHPWR connector into three groups and also monitor them independently. Starting from the Nvidia RTX 40 series, all the 12V pins of the 12VHPWR connector are internally tied together, so the GPU does not know whether all the pins are making good contact. In this case, it is possible that the GPU may try to sink a lot of current through as little as a single pin, which would lead to excessive heat generation and melted connectors and wires as the result.

### AMD RX 9070 XT

Although the official reference design for the AMD Radeon RX 9070 XT uses traditional 8-pin sockets, a few manufacuters have opted for the new 12V-2x6 socket on their video cards incorporating this chip. In August 2025, an ASRock Taichi OC Radeon RX 9070 XT was reported as having a partly molten "12VHPWR" (actually 12V-2x6) connector on Reddit. The GPU in question did not stop functioning, but discoloration could be seen on one of the power pins. The port on the GPU side was connected via a 3×8-pin connector cable to the PSU.

## Extra safety measures

In response to the reliability concerns with these connectors, vendors have marketed several new features in related products, which attempt to improve safety when using these connectors.

MSI and ASRock market high-power cables with connectors that use brightly-colored plastic around the metal contacts, with the goal of making improper connections more visually obvious. When completely inserted, none of the brightly-colored plastic should be visible. Regardless, there have been a couple of user reports of burnt, neon-yellow, MSI high-power connectors.

The same ASRock cable also has an NTC thermistor built into the GPU-end male connector. Temperature information from that sensor is transmitted to a special separate connector on the PSU end of the cable, which can then be connected to compatible ASRock PSUs. Such PSUs can then apply overheating protection based on the GPU connector's temperature.

Certain ASUS RTX graphics cards include shunt resistors which allow ASUS software to detect amperage imbalances among the high-power pins. The software can then alert the user if a significant imbalance is detected.

Certain ZOTAC graphics cards will illuminate a red indicator LED and refuse to power on if they detect that the 12V-2x6 connector is not fully seated. The cards also use gold-plated pins in their 12V-2x6 connectors, reportedly for better conductivity and more resistance to corrosion. Similarly, certain Galax cards equipped with addressable RGB lighting will turn their lights yellow upon detection of an improper high-power connection.

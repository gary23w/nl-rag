---
title: "Qi (standard)"
source: https://en.wikipedia.org/wiki/Qi_(standard)
domain: wireless-power-transfer
license: CC-BY-SA-4.0
tags: wireless power transfer, resonant inductive coupling, inductive charging, magnetic coupling
fetched: 2026-07-02
---

# Qi (standard)

**Qi** (/tʃiː/ *CHEE*) is an open standard for inductive charging developed by the Wireless Power Consortium. It allows compatible devices, such as smartphones, to receive power when placed on a Qi charger, which can be effective over distances up to 4 cm (1.6 in). Devices that implement the optional Magnetic Power Profile, based on Apple's MagSafe wireless charging technology, using magnets for better device attachment and alignment to a charger may be labelled Qi2.

Qi version 1.0 was released in 2010; by 2017, it had been incorporated into more than 200 models of smartphones, tablets, and other devices. In December 2023, 351 manufacturers were working with the standard, including Apple, Asus, Google, Huawei, LG Electronics, Samsung, Xiaomi, and Sony. The Qi specification version 2.2, released in April 2025, supports charging speeds of up to 25 watts and aims to improve compatibility across devices from various manufacturers. The current version 2.2.1 released in July 2025 includes Qi2 25W branding for the 25 watt charging mode.

## Naming

The name of the Qi standard comes from the Chinese word *qì* (simplified Chinese: 气; traditional Chinese: 氣), meaning "life force" or "vital energy".

## Design

Devices that operate using the Qi standard rely on electromagnetic induction between planar coils. A Qi system consists of two types of devices – the Base Station, which is connected to a power source and provides inductive power, and Mobile Devices, which consume inductive power. The Base Station contains a power transmitter that comprises a transmitting coil that generates an oscillating magnetic field; the Mobile Device contains a power receiver holding a receiving coil. The magnetic field induces an alternating current in the receiving coil by Faraday's law of induction. Close spacing of the two coils ensures the inductive power transfer is efficient.

Base Stations typically have a flat surface – referred to as the Interface Surface – on top of which a user can place one or more Mobile Devices. There are two methods for aligning the transmitting coil (part of the Base Station) and receiving coil (part of the Mobile Device) in order for a power transfer to happen. In the first concept – called guided positioning – a user must place the Mobile Device on a certain location of the Base Station's surface. For this purpose, the Mobile Device provides an alignment aid that is appropriate to its size, shape, and function. The second concept – referred to as free positioning – does not require the user to place the Mobile Device in direct alignment with the transmitting coil. There are several ways to achieve free positioning. In one example a bundle of transmitting coils is used to generate a magnetic field at the location of the receiving coil only. Another example uses mechanical means to move a single transmitting coil underneath the receiving coil. A third option is to use a technique called *Multiple Cooperative Flux Generators*.

The power transmitter includes a power conversion unit and a communications and control unit. Figure 1-1 shows the transmitting coil (array) generating the magnetic field as part of the power conversion unit. The control and communications unit regulates the transferred power to the level that the power receiver requests. A Base Station may contain numerous transmitters, allowing for multiple Mobile Devices to be placed on the same Base Station to charge each of its batteries.

A power receiver comprises a power pick-up unit, and a communications and control unit. A power pick-up unit typically contains a single receiving coil only. The mobile device it charges typically contains a single power receiver. The communications and control unit regulates the transferred power to the level that is appropriate for the device.

### Transmitters

A reference Qi low-power transmitter has a coil of 20 turns (in two layers) in a flat coil, wound on a form with a 19 mm inner diameter and a 40 mm outer diameter, with a below-coil shield of soft iron at least 4 mm larger in diameter which gives an inductance of 24 ± 1 microhenries. This coil is placed in a series resonant circuit which is driven by an H-bridge switching arrangement from the DC source. Power control is automatic and voltage is controllable in steps of 50 millivolts or less.

In the device a proportional-integral-derivative controller is used to modulate the delivered power according to the primary cell voltage.

Other Qi charge transmitters start their connections at 140 kHz, but can adjust to find a frequency to better match the distance between coils. Different Qi reference designs have different coil arrangements, including oval coil and multi-coil systems as well as more complex resonance networks with multiple inductors and capacitors. These designs allow operation at frequencies from 105 to 205 kHz and with maximum resonant circuit voltages as high as 200 volts.

### Receivers

The Qi power receiver hardware reference design starts with a rectangular coil of wire 44 mm × 30 mm outside size, with 14 turns of wire, and with an above-coil magnetic shield. Power output to the portable device is via a full-wave bridge; the power is typically filtered with a capacitor before delivery to the charge controller. Other Qi power receivers use alternate resonance modulators, including switching a resistor or pair of resistors across the receiver resonator capacitor, both before and after the bridge rectifier.

## Features and specifications

The Wireless Power Consortium (WPC) published the Qi low-power specification in August 2009. The Qi specification can be downloaded freely after registration. Under the Qi specification, "low power" inductive transfers deliver power below 5 W using inductive coupling between two planar coils. These coils are typically 5 mm apart but can be up to 40 mm and possibly further apart. The Qi low-power specification has been renamed to the Qi Baseline Power Profile.

Regulation of the output voltage is provided by a digital control loop where the power receiver communicates with the power transmitter and requests more or less power. Communication is unidirectional from the power receiver to the power transmitter via backscatter modulation. In backscatter modulation, the power-receiver coil is loaded, changing the current draw at the power transmitter. These current changes are monitored and demodulated into the information required for the two devices to work together.

In 2011, the WPC began to extend the Qi specification to medium power. As of 2019, the Medium Power standard currently delivers 30 to 65 W. It is expected to eventually support up to 200 W (typically used for portable power tools, robotic vacuum cleaners, drones and e-bikes).

In 2015, the WPC also demonstrated a high-power specification, called "Ki", that will deliver up to 1 kW, allowing the powering of kitchen appliances among other high-power utilities. In 2015, WPC introduced the Qi Extended Power Profile specification which supports charging phones at up to 15 W. Phone companies that support this include LG, Sony, Xiaomi, and Sharp.

In 2024, WPC upgraded Ki to support 2.2 kW wireless power delivery.

WPC introduced Proprietary Power Delivery Extension to allow phone OEMs to deliver higher than Baseline Power Profile's 5 W or the Extended Power Profile's 15 W. Currently, only Samsung has published their compliance test. Other phone companies that use proprietary standards for fast wireless charging include Apple, Huawei and Google.

With Qi version 2.0, WPC introduced Magnetic Power Profile (MPP), an optional part of the specification based on Apple's MagSafe for iPhone. This enables magnetic attachment and alignment with a ring of permanent magnets around the charging coil and is backwards compatible with MagSafe devices. Devices which implement MPP use a new logo and branding, Qi2 in a circle, to distinguish them from Qi devices that do not support MPP (even if they otherwise support Qi v2.0 or later). The "Qi2 in a circle" logo has previously been sporadically used for Qi2 without MPP, this usage is officially disapproved for new products. Previously Qi(1) products are to be labeled as Qi2, as use of the Qi(1) logo has been discontinued.

## Adoption

Nokia first adopted Qi in its Lumia 920, and Samsung Mobile on the Galaxy S3 (supported via a retrofittable official Samsung back cover accessory) in 2012, the Google/LG Nexus 4 followed later that year. Toyota began offering a Qi charging cradle as a factory option on its 2013 Avalon Limited, with Ssangyong the second car manufacturer to offer a Qi option, also in 2013.

As the Qi standard gained popularity, *Qi Hotspots* began to arise in places such as coffee shops, airports, sports arenas, etc. In 2012, The Coffee Bean and Tea Leaf, a US coffee chain, announced plans to install inductive charging stations at selected major metropolitan cities, as did Virgin Atlantic, for United Kingdom's London Heathrow Airport, and New York City's John F. Kennedy International Airport.

In 2015, a survey found that 76% of people surveyed in the United States and China were aware of wireless charging (an increase from 36% the previous year), and 16% of those were using it daily. Furniture retailer IKEA introduced lamps and tables with integrated wireless chargers for sale in 2015, and the Lexus NX gained an optional Qi charging pad in the center console. An estimated 120 million wirelessly charging phones were sold that year, notably the Samsung Galaxy S6, which supported both Qi and the competing Power Matters Alliance standards.

By early 2017, Qi had displaced other competing standards such as Rezence. On September 12, 2017, Apple announced that their new smartphones, the iPhone 8, iPhone 8 Plus, and the iPhone X, would support the Qi standard. Since then, every new iPhone version has supported the Qi wireless charging standard. Apple also announced plans to expand the standard with a new protocol called AirPower, which would have added the ability to charge multiple devices at once; however, this was canceled on March 29, 2019.

By the initial launch of iOS 17 in 2023, Apple launched the iPhone 15 models and iPhone 15 Pro models to support the fast 15 W Qi2-certified wireless charging. With iOS 17.2, Apple added the fast 15W Qi2-certified wireless charging support for the iPhone 13 models, iPhone 13 Pro models, iPhone 14 models and iPhone 14 Pro models.

In July 2024, HMD Global announced the Skyline, which became the first Android device to support the Qi2 MPP standard.

On September 9, 2024, alongside the announcement of the iPhone 16 models and iPhone 16 Pro models, Apple launched a new 25 W MagSafe charger featuring a woven braided cable design, available in 1 m and 2 m length options and maintaining the compatibility with the 15 W Qi2-certified wireless charging standard.

In January 2025, Samsung announced that their latest Galaxy S25 series phones are "Qi2 Ready". This means that while the devices themselves do not have magnets built-in, they are fully compatible with Qi2 when paired with a magnetic case.

In August 2025, the Google Pixel 10 range became the first major Android phones to include built-in magnets for Qi2 MPP. The Google Pixel 10 Pro XL also became the first device to support the new Qi2 25W standard.

## Version history

| Version number | Released | Maximum power | Notes |
|---|---|---|---|
| 1.0 | July 2010 | 5 W | Power transmitter can be a single coil, coil array, or moving coil |
| 1.1 | March 2012 | 5 W | 12 different transmitter specifications, foreign object detection to prevent heating of metal objects near transmitter, added powering transmitter over USB |
| 1.2 | October 2015 | Baseline Power Profile: 5 W Extended Power Profile: 15 W | Increased maximum transmitter power to 15 W, improved thermal tests for transmitters, improved timing specs, improved foreign object detection sensitivity, optional receiver ID (WP-ID). Labeled by Samsung as "Fast Wireless Charging" (initially 10 W, introduced on the Galaxy Note 5 and S6 edge plus, August 2015) requires charging plate to be connected to Qualcomm Quick Charge 2.0-enabled 15 W USB charger (9 V, 1.67 A support). |
| 1.2.3 | February 2017 | Extended Power Profile Class 0: 5–30 W | Added Power Class 0 which allows the consumer to negotiate up to 30 W from the charger |
| 1.3 | January 2021 |   | Completely restructured Specification documents with 15 thematic books describing different aspects of the system Support for authentication of Qi Certified wireless chargers Improved foreign object detection features and testing (including a new low-Q test power receiver) Restrictions on the negotiable power levels Resolution of mistakes, inconsistencies, and ambiguities A substantial number of new compliance tests covering the new features as well as features that were not tested in older version of the specification |
| 2.0 | April 2023 | 15 W | Incorporates Apple's MagSafe standard for alignment and mounting. Rather than requiring the user to manually align the coils through trial and error while looking for an indication of charging, it aligns the device and charging coil automatically, and also provides for mounting small devices, e.g. phones, securely enough for stationary use, or both. Initial standard supports up to 15 W power, but higher power profiles are planned. Also referred to as Qi2, and certified products may display a Qi2 logo. |
| 2.1 | September 2024 |   | Support for Automatic Alignment Profile (AAP) Power Transmitters Support for Magnetic Accessory Covers – MCPE and MCPM Profiles Updated Power Profile and Feature definitions Updated tests to resolve smartphone camera bump mechanical interference with wireless charger Error corrections |
| 2.2 | April 2025 | 25 W | Support for up to 25 watt power transfer Power modes optimizing the power transfer to the capabilities of (USB-C) power adapters Gain measurement and gain linearization to optimize the power control Re-introducing capacitive modulation for power receiver communications Improved magnetic power loss accounting Mated Q-factor check to verify absence of foreign object before starting the power transfer Power loss calibration for foreign object detection above 15 watt power levels |
| 2.2.1 | July 2025 |   | Introduced Qi2 25W branding for 25 watt devices and chargers |
| 2.3 | December 2025 |   | System gain change reporting for a power transmitter. |

### Qi Medium Power standard

- 2019 – 30 W to 65 W
- Future – 200 W

### Ki versions

- 2015 – 1000 W
- 2024 – 2200 W

---
title: "I2C - Wikipedia (part 2/2)"
source: https://en.wikipedia.org/wiki/I%C2%B2C
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
part: 2/2
---

## Derivative technologies

I2C is the basis for the ACCESS.bus, the VESA Display Data Channel (DDC) interface, the System Management Bus (SMBus), Power Management Bus (PMBus) and the Intelligent Platform Management Bus (IPMB, one of the protocols of IPMI). These variants have differences in voltage and clock frequency ranges, and may have interrupt lines.

High-availability systems (AdvancedTCA, MicroTCA) use 2-way redundant I2C for shelf management. Multi-controller I2C capability is a requirement in these systems.

TWI (Two-Wire Interface) or TWSI (Two-Wire Serial Interface) is essentially the same bus implemented on various system-on-chip processors from Atmel and other vendors. Vendors use the name TWI, even though I2C is not a registered trademark as of 2014-11-07. Trademark protection only exists for the respective logo (see upper right corner), and patents on I2C have now lapsed. According to Microchip Technology, TWI and I2C have a few differences. One of them is that TWI does not support START byte.

In some cases, use of the term "two-wire interface" indicates incomplete implementation of the I2C specification. Not supporting arbitration or clock stretching is one common limitation, which is still useful for a single controller communicating with simple targets that never stretch the clock.

MIPI I3C sensor interface standard (I3C) is a development of I2C, under development in 2017.


## Revisions

| Year | Version | Notes | Refs |
|---|---|---|---|
| 1980 | Patent | In 1980, "Philips Nv" filed for a patent in Netherlands. In 1981, "U.S. Phillips Corp" applied for a patent in U.S. then later assigned in 1987 as U.S. Patent 4,689,740. |   |
| 1982 | Original | The 100 kbit/s I2C system was created as a simple internal bus system for building control electronics with various Philips chips. | —N/a |
| 1992 | 1 | Added 400 kbit/s *Fast-mode (Fm)* and a 10-bit addressing mode to increase capacity to 1008 nodes. This was the first standardized version. | —N/a |
| 1998 | 2 | Added 3.4 Mbit/s *High-speed mode (Hs)* with power-saving requirements for electric voltage and current. |   |
| 2000 | 2.1 | Clarified version 2, without significant functional changes. |   |
| 2007 | 3 | Added 1 Mbit/s *Fast-mode plus (Fm+)* (using 20 mA drivers), and a device ID mechanism. |   |
| 2012 | 4 | Added 5 Mbit/s *Ultra Fast-mode (UFm)* for new USDA (data) and USCL (clock) lines using push-pull logic without pull-up resistors, and added an assigned manufacturer ID table. It is only a unidirectional bus. |   |
| 2012 | 5 | Corrected mistakes. |   |
| 2014 | 6 | Corrected two graphs. |   |
| 2021 | 7 | Changed terms "master/slave" to "controller/target" to align with I3C bus specification. Updated Table 5 assigned manufacturer IDs. Added Section 9 overview of I3C bus. This is the current standard. |   |

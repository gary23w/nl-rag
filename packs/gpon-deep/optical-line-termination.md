---
title: "Optical line termination"
source: https://en.wikipedia.org/wiki/Optical_line_termination
domain: gpon-deep
license: CC-BY-SA-4.0
tags: gigabit pon, passive optical network, optical line termination, fiber access
fetched: 2026-07-02
---

# Optical line termination

An **optical line termination** (**OLT**), also called an **optical line terminal**, is a device which serves as the service provider endpoint of a passive optical network. It provides two main functions:

1. to perform conversion between the electrical signals used by the service provider's equipment and the fiber optic signals used by the passive optical network.
2. to coordinate the multiplexing between the conversion devices on the other end of that network (called either optical network terminals or optical network units).

In general, an OLT is akin to a network switch where each port represents one or more client ONT or a node. Each port may be attached to the boards or network/line cards via a SFP module which must be a OLT module for it to have its Tx and Rx wavelengths swapped, but not all OLTs use SFP modules as shown in the image to the left. OLTs are either found at the ISP level inside a cabinet or distribution point, or customer level for connecting ONTs locally, such as a hotel or apartments. Depending on the underlying fiber technology, an OLT can be EPON, GPON, XG-PON or WDM.

An OLT can have several ports, and each port can drive a single PON network with split ratios or splitting factors of around 1:32 or 1:64, meaning that for each port on the OLT, up to 32 or 64 ONUs at customer sites can be connected although this depends on the PON standard the OLT and the PON network supports. XGS-PON networks support split ratios of up to 1:128. An OLT with 272 ports can support up to 34,816 users assuming a split ratio of 1:128 for every port. It can be located in a point of presence which can be a curb-side cabinet or building, or a central office.

## Features

OLTs include the following features:

- A downstream frame processing means for receiving and churning an Asynchronous Transfer Mode cell to generate a downstream frame, and converting a parallel data of the downstream frame into a serial data thereof.
- A wavelength division multiplexing means for performing an electro/optical conversion of the serial data of the downstream frame and performing a wavelength division multiplexing thereof. This is for separating services such as CATV, POTS and Data.
- An upstream frame processing means for extracting data from the wavelength division multiplexing means, searching an overhead field, delineating a slot boundary, and processing a physical layer operations administration and maintenance (PLOAM) cell and a divided slot separately.
- A control signal generation means for performing a media access control (MAC) protocol and generating variables and timing signals used for the downstream frame processing means and the upstream frame processing means.
- A control means for controlling the downstream frame processing means and the upstream frame processing means by using the variables and the timing signals from the control signal generation means.
- Encrypting the traffic so other ONTs don't see each other's traffic by means of GPON Serial Number, PLOAM password or, in case of EPON, LOID ID and password. Some OLTs from vendors such as Nokia or ADTRAN may incorporate other layers of Authentication like CLEI code, Mnemonics, certificates or others via OMCI.

## Vendors

Most vendors integrate an entire fiber optic management system for ISPs to manage OLTs as well as client ONTs and as such are not interoperable.

- ADTRAN
- BT-PON
- FiberHome
- Huawei
- Nokia
- TP-Link
- ZTE
- Zyxel

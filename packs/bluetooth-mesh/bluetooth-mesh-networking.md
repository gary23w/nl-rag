---
title: "Bluetooth mesh networking"
source: https://en.wikipedia.org/wiki/Bluetooth_mesh_networking
domain: bluetooth-mesh
license: CC-BY-SA-4.0
tags: bluetooth mesh, bluetooth low energy, managed flooding, iot mesh network
fetched: 2026-07-02
---

# Bluetooth mesh networking

**Bluetooth Mesh** is a computer mesh networking standard based on Bluetooth Low Energy that allows for many-to-many communication over Bluetooth radio. The Bluetooth Mesh specifications were defined in the Mesh Profile and Mesh Model specifications by the Bluetooth Special Interest Group (Bluetooth SIG). Bluetooth Mesh was conceived in 2014 and adopted on July 13, 2017 (2017-07-13).

## Overview

Bluetooth Mesh is a mesh networking standard that operates on a flood network principle. It is based on the nodes relaying the messages: every relay node that receives a network packet that

- authenticates against a known network key
- is not in message cache
- has a TTL ≥ 2

can be retransmitted with TTL = TTL − 1. Message caching is used to prevent relaying recently seen messages.

Communication is carried in the messages that may be up to 384 bytes long, when using Segmentation and Reassembly (SAR) mechanism, but most of the messages fit in one segment, that is 11 bytes. Each message starts with an opcode, which may be a single byte (for special messages), 2 bytes (for standard messages), or 3 bytes (for vendor-specific messages).

Every message has a source and a destination address, determining which devices process messages. Devices publish messages to destinations which can be single things / groups of things / everything.

Each message has a sequence number that protects the network against replay attacks.

Each message is encrypted and authenticated. Two keys are used to secure messages: (1) network keys – allocated to a single mesh network, (2) application keys – specific for a given application functionality, e.g. turning the light on vs reconfiguring the light.

Messages have a time to live (TTL). Each time a message is received and retransmitted, TTL is decremented which limits the number of "hops", eliminating endless loops.

## Architecture

Bluetooth Mesh has a layered architecture, with multiple layers as below.

| Layer | Functionality |
|---|---|
| Model Layer | It defines a standard way to exchange application specific messages. For example, a Light Lightness Model defines an interoperable way to control lightness. There are mandatory models, called Foundation Models, defining states and messages needed to manage a mesh network. |
| Access Layer | It defines a mechanism to ensure that data is transmitted and received in the right context of a model and its associated application keys. |
| Upper Transport Layer | It defines authenticated encryption of access layer packets using an application (or device specific key). It also defines some control messages to manage Friendship or to notify the behavior of a node using Heartbeat messages. |
| Lower Transport Layer | This layer defines a reliable (through a Block Acknowledgement) Segmented transmission of upper layer packets, when a complete upper layer packet can't be carried in a single network layer packet. It also defines a mechanism to reassemble segments on the receiver. |
| Network Layer | This layer defines how transport packets are addressed over network to one or more nodes. It defines relay functionality for forwarding messages by a relay node to extend the range. It handles the network layer authenticated encryption using network key. |
| Bearer Layer | It defines how the network packets are exchanged between nodes. Mesh Profile Specification defines BLE advert bearer and BLE GATT bearer. Mesh Profile defines Proxy Protocol, through which mesh packets can be exchanged via other bearers like TCP/IP. |

## Types of nodes

Nodes that support the various features can be formed into a particular mesh network topology.

| Feature | Functionality |
|---|---|
| Relay | receive and retransmit mesh messages over the advertising bearer to enable larger networks. |
| Proxy | receive and retransmit mesh messages between GATT and advertising bearers. |
| Low Power | operate within a mesh network at significantly reduced receiver duty cycles only in conjunction with a node supporting the Friend feature. |
| Friend | help a node supporting the Low Power feature to operate by storing messages destined for those nodes. |

## Theoretical limits

The practical limits of Bluetooth Mesh technology are unknown. Some limits that are built into the specification include:

| Limit for a network | Value | Remarks |
|---|---|---|
| Maximum number of nodes | 32 767 | The limit is 32768 addresses and while a node may occupy more than one address, the practical limit is most likely lower. |
| Maximum number of groups | 16 384 Number of virtual groups is 2128. |   |
| Maximum number of scenes | 65 535 |   |
| Maximum number of subnets | 4 096 |   |
| Maximum TTL | 127 |   |

## Mesh models

As of version 1.0 of Bluetooth Mesh specification, the following standard models and model groups have been defined:

### Foundation models

Foundation models have been defined in the core specification. Two of them are mandatory for all mesh nodes.

- Configuration Server (mandatory)
- Configuration Client
- Health Server (mandatory)
- Health Client

### Generic models

- Generic OnOff Server, used to represent devices that do not fit any of the model descriptions defined but support the generic properties of On/Off
- Generic Level Server, keeping the state of an element in a 16-bit signed integer
- Generic Default Transition Time Server, used to represent a default transition time for a variety of devices
- Generic Power OnOff Server & Generic Power OnOff Setup Server, used to represent devices that do not fit any of the model descriptions but support the generic properties of On/Off
- Generic Power Level Server & Generic Power Level Setup Server, including a Generic Power Actual state, a Generic Power Last state, a Generic Power Default state and a Generic Power Range state
- Generic Battery Server, representing a set of four values representing the state of a battery
- Generic Location Server & Generic Location Setup Server, representing location information of an element, either global (Lat/Lon) or local
- Generic User/Admin/Manufacturer/Client Property Server, representing any value to be stored by an element
- Generic OnOff Client & Generic Level Client
- Generic Default Transition Time Client
- Generic Power OnOff Client & Generic Power Level Client
- Generic Battery Client
- Generic Location Client
- Generic Property Client

### Sensors

- Sensor Server & Sensor Setup Server, representing a sensor device. Sensor device may be configured to return a measured value periodically or on request; measurement period (cadence) may be configured to be fixed or to change, so that more important value range is being reported faster.
- Sensor Client

### Time and scenes

- Time Server & Time Setup Server, allowing for time synchronization in mesh network
- Scene Server & Scene Setup Server, allowing for up to 65535 scenes to be configured and recalled when needed.
- Scheduler Server & Scheduler Setup Server
- Time Client, Scene Client & Scheduler Client

### Lighting

- Light Lightness Server & Light Lightness Setup Server, representing a dimmable light source
- Light CTL Server, Light CTL Temperature Server & Light CTL Setup Server, representing a CCT or "tunable white" light source
- Light HSL Server, Light HSL Hue Server, Light HSL Saturation Server & Light HSL Setup Server, representing a light source based on Hue, Saturation, Lightness color representation
- Light xyL Server & Light xyL Setup Server, representing a light source based on modified CIE xyY color space.
- Light LC (Lightness Control) Server & Light LC Setup Server, representing a light control device, able to control Light Lightness model using an occupancy sensor and ambient light sensor. It may be used for light control scenarios like Auto-On, Auto-Off and/or Daylight Harvesting.
- Light Lightness Client, Light CTL Client, Light HSL Client, Light xyL Client & Light LC Client

## Provisioning

Provisioning is a process of installing the device into a network. It is a mandatory step to build a Bluetooth Mesh network.

In the provisioning process, a provisioner securely distributes a network key and a unique address space for a device. The provisioning protocol uses P256 Elliptic Curve Diffie-Hellman Key Exchange to create a temporary key to encrypt network key and other information. This provides security from a passive eavesdropper. It also provides various authentication mechanisms to protect network information, from an active eavesdropper who uses man-in-the-middle attack, during provisioning process.

A key unique to a device known as "Device Key" is derived from elliptic curve shared secret on provisioner and device during the provisioning process. This device key is used by the provisioner to encrypt messages for that specific device.

The security of the provisioning process has been analyzed in a paper presented during the IEEE CNS 2018 conference.

The provisioning can be performed using a Bluetooth GATT connection or advertising using the specific bearer.

## Terminology used in the Bluetooth Mesh Model and Mesh Profile specifications

- Destination: The address to which a message is sent.
- Element: An addressable entity within a device.
- Model: Standardized operation of typical user scenarios.
- Node: A provisioned device.
- Provisioner: A node that can add a device to a mesh network.
- Relay: A node able to retransmit messages.
- Source: The address from which a message is sent.

## Implementations

### Approved ("qualified") by Bluetooth SIG

| Name | Submitter | Qualification date | QDID | Type |
|---|---|---|---|---|
| Bluetooth Stack for Embedded Systems - MESH profile | Silvair, Inc. | July 18, 2017 | 98880 | Profile Subsystem |
| Qualcomm Bluetooth Mesh | Qualcomm Technologies International, Ltd. | July 18, 2017 | 98856 | Profile Subsystem |
| Silvair Mesh Models | Silvair, Inc. | July 26, 2017 | 99282 | Profile Subsystem |
| Wireless Gecko Mesh Profile | Silicon Laboratories | September 21, 2017 | 101318 | Profile Subsystem |
| CYW-MESH 1.0 | Cypress Semiconductor Corporation | October 3, 2017 | 101726 | Component (Tested) |
| Qualcomm Bluetooth Mesh Model | Qualcomm Technologies International, Ltd. | October 20, 2017 | 102243 | Profile Subsystem |
| EtherMind Bluetooth Protocol Stack, 5.0 (Single Mode) + Mesh | Mindtree Limited | January 24, 2018 | 106544 | Component (Tested) |
| Telink SIG Mesh SDK | Telink Semiconductor | February 1, 2018 | 106546 | Profile Subsystem |
| TOSHIBA Bluetooth_stack_mesh-1 | Toshiba Corporation | February 13, 2018 | 104143 | Component (Tested) |
| AMICCOM Mesh Profile | AMICCOM Electronics Corporation | March 14, 2018 | 109370 | Profile Subsystem |
| Amiccom Bluetooth Mesh Model | AMICCOM Electronics Corporation | March 30, 2018 | 110168 | Profile Subsystem |
| Airoha SIG mesh | Airoha Technology Corp. | April 2, 2018 | 110202 | Profile Subsystem |
| Marvell Mesh stack v1.0 | Marvell Technology Group | April 27, 2018 | 110569 | Component (Tested) |
| nRF5 SDK for Mesh | Nordic Semiconductor | May 2, 2018 | 111537 | Profile Subsystem |
| Realtek Bluetooth 5 Mesh Solution | Realsil Microelectronics Inc | July 27, 2018 | 115668 | Profile Subsystem |
| STSW-BNRG-Mesh | STMicroelectronics | August 2, 2018 | 116029 | Profile Subsystem |
| RDA BT Host 5.0 | RDA Microelectronics, Inc. | September 13, 2018 | 115860 | Profile Subsystem |
| JYMC-MESH-1 | Shanghai Frequen Microelectronics Co., Ltd. | October 10, 2018 | 119229 | End Product |
| RW-BLE-MESH | CEVA, Inc. | October 31, 2018 | 119268 | Component (Tested) |
| ARM Ltd Cordio Mesh | ARM Ltd | December 11, 2018 | 116593 | Profile Subsystem |
| Samsung SLSI Bluetooth Mesh | Samsung Electronics Co., Ltd. | December 21, 2018 | 122442 | Profile Subsystem |
| Bluelet Host Stack V12 | Barrot Technology Limited | December 25, 2018 | 123056 | Component (Tested) |
| ESP BLE Mesh v0.6 | Espressif Systems (Shanghai) Pte. Ltd. | January 14, 2019 | 124137 | Profile Subsystem |
| BK3435 BLE Core Spec 5.0 with MESH | Beken Corp | March 12, 2019 | 127926 | End Product |
| Actions Mesh Profile Subsystem | Actions (Zhuhai) Technology Co., Limited | March 21, 2019 | 127646 | Profile Subsystem |
| AliOS Things BLE host and mesh profile v2.1.0 | Alibaba (China) Co., Ltd. | April 19, 2019 | 129750 | Host Subsystem |
| Tonly SIG Mesh Stack | Shenzhen Tonli Science and Technology Development Co., Ltd | May 5, 2019 | 130160 | Profile Subsystem |
| Sino Wealth IBLE SIG Mesh Profile | Sino Wealth Electronic Ltd. | June 18, 2019 | 133403 | Profile Subsystem |
| Qualcomm Bluetooth Mesh and Mesh Model v4.0 | Qualcomm Technologies International, Ltd. | June 19, 2019 | 128410 | Profile Subsystem |
| PAN1020 Mesh Profile subsystem | Shanghai Panchip Microelectronics Co., Ltd | July 1, 2019 | 129291 | Profile Subsystem |
| Apache NimBLE BLE Host including BLE Mesh | JUUL Labs, Inc. | July 15, 2019 | 131934 | Component (Tested) |
| Tmall mesh Stack | Alibaba (China) Co., Ltd. | July 20, 2019 | 128246 | Profile Subsystem |
| ClarinoxBlue | Clarinox Technologies Pty Ltd | August 2, 2019 | 134454 | Host Subsystem |
| BlueX Mesh | BlueX Microelectronics Corp Ltd. | August 20, 2019 | 137436 | Profile Subsystem |
| Zephyr OS Mesh | The Linux Foundation | September 20, 2019 | 139259 | Profile Subsystem |
| WCH Bluetooth Mesh | Nanjing Qinheng Microelectronics Co., Ltd. | June 1, 2020 | 144808 | Profile Subsystem |

### Free and open-source software implementations

Free software and open source software implementations include the following:

- The official (included in Linux kernel by Linus Torvalds in 2001) Linux Bluetooth protocol stack BlueZ, dual free-licensed under the GPL and the LGPL, supports Mesh Profile, from release version 5.47, by providing meshctl tool (deprecated) to configure mesh devices. Release version 5.53 introduced mesh-cfgclient tool for configuring mesh networks. BlueZ was approved as a "qualified" software package by Bluetooth SIG in 2005. BlueZ is not considered to be a qualified Bluetooth Mesh stack as Bluetooth Mesh is not listed in aforementioned qualification record as a supported profile.
- Apache Mynewt NimBLE, free-licensed under the Apache License 2.0, supports Bluetooth Mesh from release version 1.2.0. It was qualified on July 15, 2019 (2019-07-15) with QDID 131934.
- Zephyr OS Mesh, free-licensed under the Apache License 2.0, supports Bluetooth Mesh from release version 1.9.0. Zephyr OS Mesh 1.14.x was qualified on September 20, 2019 (2019-09-20) with QDID 139259.

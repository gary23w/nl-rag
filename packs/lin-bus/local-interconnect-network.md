---
title: "Local Interconnect Network"
source: https://en.wikipedia.org/wiki/Local_Interconnect_Network
domain: lin-bus
license: CC-BY-SA-4.0
tags: lin bus, local interconnect network, lin master node, automotive sub-bus
fetched: 2026-07-02
---

# Local Interconnect Network

**LIN** is a network protocol used for communication between components in modern vehicles. It is a low-cost single-step serial protocol that supports communications up to 19.2 Kbit/s with a maximum bus length of 40 metres (131.23 ft).

## History

The need for a cheap serial network arose as the technologies and the facilities implemented in the car grew, while the CAN bus was too expensive to implement for every component in the car. European car manufacturers started using different serial communication technologies, which led to compatibility problems.

In the late 1990s, the LIN Consortium was founded by five automakers (BMW, Volkswagen Group, Audi, Volvo Cars, Mercedes-Benz), with the technologies supplied (networking and hardware expertise) from Volcano Automotive Group and Motorola. The first fully implemented version of the new LIN specification (LIN version 1.3) was published in November 2002. In September 2003, version 2.0 was introduced to expand capabilities and make provisions for additional diagnostics features. LIN may be used also over the vehicle's battery power line with a special LIN-over-DC-power-line (DC-LIN) transceiver. LIN over DC power line (DC-LIN) was standardized as ISO/AWI 17987-8.

CAN in Automation has been appointed by the ISO Technical Management Board (TMB) as the Registration Authority for the LIN Supplier ID standardized in the ISO 17987 series.

## Network topology

LIN is a broadcast serial network comprising 16 nodes (one primary and up to 15 secondary nodes).

All messages are initiated by the primary node with at most one secondary node replying to a given message identifier. The primary node can also act as a secondary node by replying to its own messages. Because all communications are initiated by the primary node it is not necessary to implement a collision detection.

The primary and secondary nodes are typically microcontrollers, but may be implemented in specialized hardware or ASICs in order to save cost, space, or power.

Current uses combine the low-cost efficiency of LIN and simple sensors to create small networks. These sub-systems can be connected by a back-bone network (i.e. CAN in cars).

## Overview

The LIN bus is an inexpensive serial communications protocol, which effectively supports remote application within a car's network. It is particularly intended for mechatronic nodes in distributed automotive applications, but is equally suited to industrial applications. It is intended to complement the existing CAN network leading to hierarchical networks within cars.

In the late 1990s the Local Interconnect Network (LIN) Consortium was founded by five European automakers, Mentor Graphics (Formerly Volcano Automotive Group) and Freescale (Formerly Motorola, now NXP). The first fully implemented version of the new LIN specification was published in November 2002 as LIN version 1.3. In September 2003 version 2.0 was introduced to expand configuration capabilities and make provisions for significant additional diagnostics features and tool interfaces.

The protocol’s main features are listed below:

- Single master, up to 16 slaves (i.e. no bus arbitration). This is the value recommended by the LIN Consortium to achieve deterministic time response.
  - Slave Node Position Detection (SNPD) allows node address assignment after power-up
- Single-wire communications up to 19.2 kbit/s @ 40 meter bus length. In the LIN specification 2.2, the speed up to 20 kbit/s.
- Guaranteed latency times.
- Variable length of data frame (2, 4 and 8 bytes).
- Configuration flexibility.
- Multicast reception with time synchronization, without crystals or ceramic resonators.
- Data checksum and error detection.
- Detection of defective nodes.
- Low-cost silicon implementation based on standard UART/SCI hardware.
- Enabler for hierarchical networks.
- Operating voltage of 12 V.

Data is transferred across the bus in fixed-form messages of selectable lengths. The master task transmits a header that consists of a break signal followed by synchronization and identifier fields. The slaves respond with a data frame that consists of 2, 4 or 8 data bytes plus 3 bytes of control information.

## LIN message frame

A message contains the following fields:

- Synchronization break
- Synchronization byte
- Identifier byte
- Data bytes
- Checksum byte

### Frame types

1. **Unconditional frame.** These always carry signals and their identifiers are in the range 0 to 59 (0x00 to 0x3b). All subscribers of the unconditional frame shall receive the frame and make it available to the application (assuming no errors were detected).
2. **Event-triggered frame.** The purpose of this is to increase the responsiveness of the LIN cluster without assigning too much of the bus bandwidth to the polling of multiple slave nodes with seldom occurring events. The first data byte of the carried unconditional frame shall be equal to a protected identifier assigned to an event-triggered frame. A slave shall reply with an associated unconditional frame only if its data value has changed. If none of the slave tasks responds to the header the rest of the frame slot is silent and the header is ignored. If more than one slave task responds to the header in the same frame slot a collision will occur, and the master has to resolve the collision by requesting all associated unconditional frames before requesting the event-triggered frame again.
3. **Sporadic frame.** This frame is transmitted by the master as required, so a collision cannot occur. The header of a sporadic frame shall only be sent in its associated frame slot when the master task knows that a signal carried in the frame has been updated. The publisher of the sporadic frame shall always provide the response to the header.
4. **Diagnostic frame.** These always carry diagnostic or configuration data and they always contain eight data bytes. The identifier is either 60 (0x3C), called master request frame, or 61(0x3D), called slave response frame. Before generating the header of a diagnostic frame, the master task asks its diagnostic module if it shall be sent or if the bus shall be silent. The slave tasks publish and subscribe to the response according to their diagnostic module.
5. **User-defined frame.** These can carry any kind of information. Their identifier is 62 (0x3E). The header of a user-defined frame is always transmitted when a frame slot allocated to the frame is processed
6. **Reserved frame.** These shall not be used in a LIN 2.0 cluster. Their identifier is 63 (0x3F).

## LIN hardware

The LIN specification was designed to allow very cheap hardware-nodes being used within a network. It is a low-cost, single-wire network based on ISO 9141. In today’s car networking topologies, microcontrollers with either UART capability or dedicated LIN hardware are used. The microcontroller generates all needed LIN data (protocol ...) (partly) by software and is connected to the LIN network via a LIN transceiver (simply speaking, a level shifter with some add-ons). Working as a LIN node is only part of the possible functionality. The LIN hardware may include this transceiver and works as a pure LIN node without added functionality.

As LIN Slave nodes should be as cheap as possible, they may generate their internal clocks by using RC oscillators instead of crystal oscillators (quartz or a ceramic). To ensure the baud rate-stability within one LIN frame, the SYNC field within the header is used.

## LIN protocol

The LIN-Master uses one or more predefined scheduling tables to start the sending and receiving to the LIN bus. These scheduling tables contain at least the relative timing, where the message sending is initiated. One LIN Frame consists of the two parts: **header** and **response**. The header is always sent by the LIN Master, while the response is sent by either one dedicated LIN-Slave or the LIN master itself.

Transmitted data within the LIN is transmitted serially as eight bit data bytes with one start bit, one stop-bit, and no parity (break field does not have a start or stop bit). Bit rates vary within the range of 1 kbit/s to 20 kbit/s. Data on the bus is divided into recessive (logical HIGH) and dominant (logical LOW). The time normally is considered by the LIN Masters stable clock source, the smallest entity is one bit time (52 μs @ 19.2 kbit/s).

Two bus states – sleep-mode and active – are used within the LIN protocol. While data is on the bus, all LIN-nodes are asked to be in the active state. After a specified timeout, the nodes enter sleep mode and will be released back to active state by a WAKEUP frame. This frame may be sent by any node requesting activity on the bus, either the LIN Master following its internal schedule, or one of the attached LIN Slaves being activated by its internal software application. After all nodes are awakened, the Master continues to schedule the next Identifier.

### Header

The header consists of five parts:

*BREAK:* The BREAK field is used to activate all attached LIN slaves to listen to the following parts of the header. It consists of one start bit and several dominant bits. The length is at least 11-bit times; standard use as of today are 13-bit times, and therefore differs from the basic data format. This is used to ensure that listening LIN nodes with a main-clock differing from the set bus baud rate in specified ranges will detect the BREAK as the frame starting the communication and not as a standard data byte with all values zero (hexadecimal 0x00).

*SYNC:* The SYNC is a standard data format byte with a value of hexadecimal 0x55. LIN slaves running on RC oscillator will use the distance between a fixed amount of rising and falling edges to measure the current bit time on the bus (the master's time normal) and to recalculate the internal baud rate.

*INTER BYTE SPACE:* Inter Byte Space is used to adjust for bus jitter. It is an optional component within the LIN specification. If enabled, then all LIN nodes must be prepared to deal with it.

There is an Inter Byte Space between the BREAK and SYNC field, one between the SYNC and IDENTIFIER, one between the payload and Checksum and one between every Data byte in the payload.

*IDENTIFIER:* The IDENTIFIER defines one action to be fulfilled by one or several of the attached LIN slave nodes. The network designer has to ensure the fault-free functionality in the design phase (one slave is allowed to send data to the bus in one frame time).

If the identifier causes one *physical* LIN slave to send the response, the identifier may be called a Rx-identifier. If the *master's slave task* sends data to the bus, it may be called Tx-identifier.

*RESPONSE SPACE:* Response Space is the time between the IDENTIFIER field and the first Data byte which starts the LIN RESPONSE part of the LIN frame. When a particular LIN frame is transmitted completely, Header + Response, by the LIN MASTER, the LIN MASTER will use the full RESPONSE SPACE TIME to calculate when to send the response after sending the header. If the response part of the LIN frame is coming from a physically different SLAVE NODE, then each node (master & slave) will utilize 50% of the Response Space time in their timeout calculations.

### Response

The response is sent by one of the attached LIN slave **tasks** and is divided into data and checksum.

*DATA:* The responding slave may send zero to eight data bytes to the bus. The amount of data is fixed by the application designer and mirrors data relevant for the application which the LIN slave runs in.

*CHECKSUM:* There are two checksum-models available within LIN - The first is the checksum including the data bytes only (specification up to Version 1.3), the second one includes the identifier in addition (Version 2.0+). The used checksum model is pre-defined by the application designer.

## Slave node position detection (SNPD) or autoaddressing

These methods allow the detection of the position of slave nodes on the LIN bus and allow the assignment of a unique node address (NAD).

- Allows similar or the same devices to be connected on the bus without end of line programming or connector pin programming.

Restrictions:

- All auto-addressing slaves must be in one line
  - Standard slaves can be connected in any way

| SNPD Method | SNPD Method ID | Company |
|---|---|---|
| Extra wire daisy chain | 0x01 | NXP (formerly Philips) |
| Bus shunt method | 0x02 | Elmos Semiconductor |
| Reserved | 0x03 | TBD |
| Reserved | 0x04 | TBD |
| Reserved | 0xFF | TBD |

### Extra wire daisy chain (XWDC)

Each slave node has to provide two extra pins, one input, D1, and one output, D2.

- The first SNPD node input D1 is either set to GND or connected to the output of the master.
  - The output of the first node, D2, is connected to the input, D1 of the second node, and so on resulting in a daisy chain.

Each configuration pin Dx (x=1-2) has additional circuitry to aid in the position detection.

1. Switchable resistive pull-up to Vbat
2. Pull-down to GND
3. Comparator referenced to Vbat/2

#### XWDC auto-addressing procedure

At the start of the procedure no SNPD devices have a NAD assigned

1 First auto-addressing LIN message

1.1 All outputs (D

2

) are set to a high level, all pull-downs are turned off

1.2 The first SNPD node is selected. It is identified by having the input D

1

low (hardwired).

1.3 The selected node takes the address from the LIN configuration message

1.4 The detected node turns on the pull-down at the output D

2

2 Subsequent auto-addressing LIN messages

2.1 The first non addressed SNPD node is selected. It is identified by having the input D

1

low (D

2

of previous node).

2.2 The selected node takes the address from the LIN configuration message

2.3 The detected node turns on the pull-down at the output D

2

2.4 Steps 2.1-2.4 are repeated until all slave nodes are assigned an address

3 All pull-ups and pull-downs are turned off completing the addressing procedure

### Bus shunt method (BSM)

Each slave node has two LIN pins

1. bus_in
2. bus_out

Each slave node needs some additional circuitry compared to the standard LIN circuitry to aid in the position detection.

1. The standard pull-up must be switchable
2. Switchable 2 mA current source from Vbat
3. Shunt resistor
4. Differential amplifier
5. Analog to digital converter

#### BSM auto-addressing procedure

At the start of the procedure, none of the SNPD devices have a NAD assigned. The autoaddressing routine is performed during the sync field. The sync field is broken into three phases:

1 Offset current measurement

1.1 All outputs pull-ups and current sources are switched off

1.2 The bus current is measured,

I

offset

2 Pull-up mode

2.1 Pull-ups are turned on and current sources remain off

2.2 The bus current is measured,

I

PU

2.3 Nodes with ΔI =

I

PU

-

I

offset

< 1

mA are "selected"

3 Current source mode

3.1 Selected nodes switch current source on and others switch pull-ups off

3.2 Bus current is measured,

I

CS

3.3 Node with ΔI =

I

CS

-

I

offset

< 1

mA is detected as the last node

3.4 Current sources are switched off and pull-ups are switched on

3.5 The last node will accept the address contained in the LIN configuration message

This technique is covered by the patents EP 1490772 B1 and US 7091876.

## LIN advantages

- Easy to use
- Components available
- Cheaper than CAN and other communications buses
- Harness reduction
- More reliable vehicles
- Extension easy to implement.
- No protocol license fee required

LIN is not a full replacement of the CAN bus. But the LIN bus is a good alternative wherever low costs are essential and speed/bandwidth is not important. Typically, it is used within sub-systems that are not critical to vehicle performance or safety - some examples are given below.

## Applications

| Application segments | Specific LIN application examples |
|---|---|
| Roof | Sensor, light sensor, light control, sun roof |
| Steering wheel | Cruise control, wiper, turning light, climate control, radio, wheel lock |
| Seat | Seat position motors, occupant sensors, control panel |
| Engine | Sensors, small motors, cooling fan motors |
| Grille | Grille shutter |
| Climate | Small motors, control panel |
| Door | Mirror, central ECU, mirror switch, window lift, seat control switch, door lock |
| Illumination | Vehicle trim enhancement, sill plates illuminated with RGB LED |

## Addressing

Addressing in LIN is achieved with a NAD (Node ADdress) that is part of the PID (protected identifier). NAD values are on 7bits, so in the range 1 to 127 (0x7F) and it is a composition of supplier ID, function ID and variant ID.

You can obtain a supplier ID by contacting CAN in Automation that is the authority responsible for the assignment of such identifiers.

---
title: "CAN FD"
source: https://en.wikipedia.org/wiki/CAN_FD
domain: can-fd-bus
license: CC-BY-SA-4.0
tags: can fd, flexible data-rate, controller area network, bit stuffing frame
fetched: 2026-07-02
---

# CAN FD

**CAN FD** (Controller Area Network Flexible Data-Rate) is a data-communication protocol used for broadcasting sensor data and control information on 2 wire interconnections between different parts of electronic instrumentation and control system. This protocol is used in modern high performance vehicles.

CAN FD is an extension to the original CAN bus protocol that was specified in ISO 11898-1. CAN FD is the second generation of CAN protocol developed by Bosch. The basic idea to overclock part of the frame and to oversize the payload dates back to 1999. Developed in 2011 and released in 2012 by Bosch, CAN FD was developed to meet the need to increase the data transfer rate up to 5 times faster and with larger frame/message sizes for use in modern automotive Electronic Control Units.

As in the classical CAN, CAN FD protocol is designed to reliably transmit and receive sensor data, control commands and to detect data errors between electronic sensor devices, controllers and microcontrollers. Although CAN FD was primarily designed for use in high performance vehicle ECUs, the pervasiveness of classical CAN in the different industries will lead into inclusion of this improved data-communication protocol in a variety of other applications as well, such as in electronic systems used in robotics, defense, industrial automation, underwater vehicles, medical equipment, avionics, down-hole drilling sensors, etc.

## CAN FD versus classical CAN

The primary difference between the classical CAN (Controller Area Network) and CAN FD is the Flexible Data (FD). Using CAN FD, Electronic Control Units (ECUs) are enabled to dynamically switch between different data rates and longer or shorter messages. Faster data speed and more data capacity enhancements results in several system operational advantages compared to classical CAN. Commands issued by the executing ECU software reach the output controller much faster. CAN FD is typically used in high performance ECUs of modern vehicles. A modern vehicle can have more than 70 ECUs that use CAN FD to exchange information over the CAN bus when the engine is running or when the vehicle is moving.

On a CAN bus, a *frame* is the basic unit of messaging. For a classic CAN bus, a frame consists of an 11-bit identifier along with an 8-byte message payload. For CAN FD, a frame is labeled with a 29-bit identifier and carries a 64-byte message payload. Frames with 11-bit identifiers are said to be in FD Base Frame Format (FDBF) and frames with 29-bit identifiers are referred to as FD Extended Frame Format (FEFF). While payload data rates of 5-8 Mbit/s are possible in CAN FD, overall data transfer rates depend on the total length of the bus network and the transceivers used to generate and detect bus signals. Additionally, arbitration data rates are limited to 1 Mbit/s to maintain compatibility with classical CAN devices. The CAN FD protocol specification provides improved error detection in received CAN messages and enhanced flexibility of data transfer speeds to account for differences in sensor polling rates. The CAN bus consists of a shared pair of wires onto which electronic sensors, controller units, and ECUs are connected and is used to exchange information between units operating periodically or on demand. The total number of units connected, the length of the CAN bus wires, and additional electromagnetic factors determine the fastest data transfer rate possible for a given CAN bus. All versions of the CAN protocol are designed with robust collision resolution that depends on signal propagation time, network topology, and the number of units on the bus. To minimize message collision and reduce costly error correction, many CAN bus configurations may limit their data transfer rate well below the bus's theoretical maximum speed.

CAN-FD bus load that was developed by "De Andrade's" equation based on Tindel's equation.

β = τ/ω (β = Busload), (τ = time of slow bits plus faster bits), ω (time in seconds of measurement). τ = Ts + Tf

CAN-FD protocol defines five different error detection mechanisms: Two of them work at the bit level, and the other three at the message level. They are:

```
 - (1) Bit Monitoring, 
 - (2) Bit Stuffing, 
 - (3) Frame Check,
 - (4) Acknowledgement Check and 
 - (5) Cyclic Redundancy Check. There are two options of CRC which should be denoted as for CRC length of 17 (Data Length 0-16 bytes) or CRC length of 21 bits (Data Length 17–64) bytes.
```

Where the transmission time of the (fixed-size) header is given by:

$\textstyle T_{s}=\left({\frac {\left({\text{SOF}}+{\text{ID}}+r1+{\text{IDE}}+{\text{EDL}}+r0+{\frac {\text{BRS}}{2}}+{\frac {\text{CRCdel}}{2}}\right)\cdot 1.2}{t_{x}}}\right)+{\frac {{\text{ACK}}+{\text{DEL}}+{\text{EOF}}+{\text{IFS}}}{t_{x}}}$

The fields are explained in the table below. Here 1.2 is taken to be the factor of the worst case bit stuffing, which means the computation shall be increased by 25%. It is considered BRS and CRCdel divided by 2, because they are exactly in the shift of bit rate transition.

The transmission time of the payload is calculated as:

$\textstyle T_{f}={\frac {\left(\left(D_{f}+{\text{ESI}}+{\text{DLC}}+{\frac {\text{BRS}}{2}}+{\frac {\text{CRCdel}}{2}}\right)\cdot 1.2\right)+{\text{CRC}}+{\text{SB}}}{t_{Y}}}$

Here SB signifies the stuffing bits (5 bits for packets smaller than 6 bytes and 6 bits for packets bigger than 6 bytes). CRC is also size-dependent, set to 17 bits for packets smaller than 6 bytes and to 21 for larger packets. Df represents the CAN-FD payload size which may be 0 to 8, 12, 16, 20, 24, 32, 48, 64 Bytes. t_X is the transmission bandwidth for the message header (up to 1 Mbit/s).

CAN FD also has decreased the number of undetected errors through increases in the performance of the CRC-algorithm. In addition, CAN FD is compatible with existing CAN 2.0 networks, allowing the new protocol to function on the same network as classical CAN. CAN FD bit rate can be up to 8 Mbit/s with the right CAN SIC (Signal Improvement Capability) Transceiver and so up to 8 times faster than classical CAN with 1 Mbit/s data phase.

Due to higher communication speed, CAN FD constraints are tougher in terms of line parasitic capacitance. Therefore, all components on the line have seen their "capacitance" budget reduced compared to regular CAN bus. That is the reason why semiconductor suppliers have released new components approved by car makers. This approval reflects the need for interoperability between all CAN FD systems. Indeed, selected ESD protection components are compatible with all transceivers (CAN or CAN FD) and withstand ISO7637-3.

Despite a higher stand-off voltage≤ (37 V), devices for truck applications must also comply with the low capacitance requirement (3.5 pF).

## Data frame

The data frame used for actual data transmission have two message formats:

- Base frame format: with 11 identifier bits
- Extended frame format: with 29 identifier bits

The frame format is as follows: The bit values are described for CAN-LO signal.

| Field name | Length (bits) | Purpose |
|---|---|---|
| Start-of-frame (SOF) | 1 | Denotes the start of frame transmission |
| Identifier (ID) | 11 | A (unique) identifier which also represents the message priority |
| Stuff bit | 1 | A bit of the opposite polarity to maintain synchronisation; see CAN Bus#Bit stuffing |
| Remote Request Substitution (RRS) | 1 |   |
| Identifier extension bit (IDE) | 1 |   |
| FD Format Indicator (FDF) | 1 | Must be recessive (1) for CAN FD frames and dominant (0) for classic CAN. |
| Reserved bit in FD frames (res) | 1 |   |
| Bit Rate Switch (BRS) | 1 |   |
| Error State Indicator (ESI) | 1 |   |
| Data length code (DLC) | 4 | Number of bytes of data (0–64 bytes) |
| Data field | 0–512 (0-64 bytes) | Data to be transmitted (length in bytes dictated by DLC field) |
| Stuff count | 4 |   |
| CRC | 17-21 | CRC-21 when payload is greater than 16 bytes, else CRC-17 Cyclic redundancy check |
| CRC delimiter | 1 | Must be recessive (1) |
| FSB | 6-7 | Fixed stuffing-bits in CRC Field: for every 4 bits theres 1 stuffing bit (6 stuffing bits for Stuff count and CRC-17, 7 for Stuffcount and CRC-21) |
| ACK slot | 1 | Transmitter sends recessive (1) and any receiver can assert a dominant (0) |
| ACK delimiter | 1 | Must be recessive (1) |
| End-of-frame (EOF) | 7 | Must be recessive (1) |
| Inter-frame spacing (IFS) | 3 | Must be recessive (1) |

1. The values 0-8 indicate 0-8 bytes like classic CAN. The values 9-15 are translated to a value between 12-64 which is the actual length of the data field: 9→12   10→16   11→20   12→24   13→32   14→48   15→64

## CAN & CAN FD TP Headers

CAN + CANFD -TP Header

7 .. 4 (byte 0)

3 .. 0 (byte 0)

15 .. 8 (byte 1)

23..16 (byte 2)

(byte 3)

(byte 4)

(byte 5)

(byte 6)

....

Single Frame (SF)

according to CAN

0

size (1..7)

Data

CAN-FD specific

0

size (0..62)

Data

First Frame (FF)

according to CAN

1

size (8..4095)

Data

CAN-FD specific

0

0

size (4bytes ~4

GB)

Data

Consecutive Frame (CF)

according to CAN

2

index (0..15)

Data

Flow Control Frame (FC)

according to CAN

3

FC flag (0,1,2)

Block size

ST

Unused

The above table explains the transfer protocol defined for CAN + CANFD, based on ISO 15765-2 (ISO-TP), used for sending packets of data longer than what fits in a CAN frame.

- if the first byte is 0x00, then it's a CAN-FD SF, and the second byte specifies the size of the data.
- if the first byte is 0x01-0x07, then it's a normal CAN SF with this byte indicating the size of 1-7 bytes data.
- if the first 2 bytes are 0x1000, then it's a CAN-FD FF, and the following 4 bytes specifies the size of data in high byte first order. This virtually enables to send ~4 GB (approx.) data in CAN FD.
- if the first 2 bytes are 0x1008-0x1FFF, then it's a normal CAN FF with a size of 0x008-0xFFF.

## CAN Transceiver

CAN FD can use Transceiver for classical CAN and CAN FD. Additionally there are new CAN SiC (Signal improvement Capability) Transceiver with 5 to 8 Mbit/s data rate.

## CAN FD in action

In 2017, CAN FD was predicted to be used in most vehicles by 2019–2020.

## CAN FD supporters

Some of the companies behind the new standard include STMicroelectronics, Infineon, NXP, Texas Instruments, Kvaser, Daimler and GM.

CAN FD forms a basic data link layer in some higher Layer protocols like CANopen as CANopen FD and J1939 and supported by different companies with protocol stacks.

## CAN XL

CAN XL is the 3rd version of the CAN data link layer after classical CAN and CAN FD. CAN FD is compatible to CAN XL.

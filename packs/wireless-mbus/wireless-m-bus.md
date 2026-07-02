---
title: "Meter-Bus"
source: https://en.wikipedia.org/wiki/Wireless_M-Bus
domain: wireless-mbus
license: CC-BY-SA-4.0
tags: wireless m-bus, wireless meter-bus, radio meter reading, wm-bus metering
fetched: 2026-07-02
---

# Meter-Bus

(Redirected from

Wireless M-Bus

)

**M-Bus** or **Meter-Bus** is a European standard (EN 13757-2 physical and link layer, EN 13757-3 application layer) for the remote reading of water, gas or electricity meters. M-Bus is also usable for other types of consumption meters, such as heat meters or water meters. The M-Bus interface is made for communication on two wires, making it cost-effective. A radio variant of M-Bus **Wireless M-Bus** is also specified in EN 13757–4.

The M-Bus was developed to fill the need for a system for the networking and remote reading of utility meters, for example to measure the consumption of gas or water in the home. This bus fulfills the special requirements of remotely powered or battery-driven systems, including consumer utility meters. When interrogated, the meters deliver the data they have collected to a common master, such as a hand-held computer, connected at periodic intervals to read all utility meters of a building. An alternative method of collecting data centrally is to transmit meter readings via a modem.

Other applications for the M-Bus such as alarm systems, flexible illumination installations, heating control, etc. are suitable.

## Relation to the OSI model

Since no bus system was available for the requirements of meter reading, the M-Bus was developed by Horst Ziegler of the University of Paderborn in cooperation with Texas Instruments Deutschland GmbH and Techem GmbH. The concept was based on the ISO-OSI Reference Model, in order to realize an open system which could use almost any desired protocol.

Since the M-Bus is not a network, and therefore does not – among other things – need a transport or session layer, the levels four to six of the OSI model are empty. Therefore, only the physical, the data link, the network and the application layer are provided with functions.

| OSI Model |   |   |   |
|---|---|---|---|
|   | Data unit | Layer | Standard |
| Host layers | Data | 7. Application | EN1434-3 |
| 6. Presentation | Empty |   |   |
| 5. Session | Empty |   |   |
| Segment/Datagram | 4. Transport | Empty |   |
| Media layers | Packet | 3. Network | Optional |
| Frame | 2. Data link | IEC 60870 |   |
| Bit | 1. Physical | M-Bus |   |

## Physical wire and connectors

M-Bus connection is called M-Bus or HAN (Home Area Network) consumer connection. M-Bus uses two-wire telephone cable (JYStY 1x*2x*0.8 mm or similar, 73 ohm/km, 120 nF/km) maximum length of 350 meters when using nominal transfer speeds 300 and 9600 baud. Lowering the speed up to 1000 meter cable can be used. There is no standardized connector, but RJ11 and RJ12 Modular connectors are used by meter manufacturers.

The master communication uses voltage signaling, where 1 (idle state, mark) is the bus nominal 36 volts, 0 (space) drops the voltage to 24 volts (V). As bus voltage can vary with length and load, the signal is specified as 1 for bus voltage drop less than 5.5 V, 0 for drop higher than 8.2 V.

Slaves communicate by current consumption, where 1 (idle state, mark) is less than 1.5 milliamperes (mA), 0 (space) raises current to 11–20 mA. The signal is specified as the at least 11 mA current increase.

The slaves are connected via diode bridge and can use either polarity of the wires. To protect the bus against shortcircuited slaves, a 430 ohm is connected in series at each slave (or, two 215 ohm resistors, one for each wire).

A M-bus load unit is 1.5 mA. Most slaves use at most this, some can need two units (3 mA). Masters can provide type-dependent number of load units, and usually visually indicate overload.

## Data link protocol

The data link protocol is described by IEC 870-5, or its updated version, IEC 60870-5.

The data are sent in serial form, at speed between 300 and 9600 bit/s (some variants may operate up to 19200 or 38400 bit/s), using one start bit, one stop bit, and even parity (8e1). The least significant bit is sent first. When sending packets ("telegrams"), there is no pause between stop and subsequent start bit.

Suggested speeds are 300, 2400, 9600, and with newer hardware 38400 bit/s, while 2400 bit/s is most common. Devices with different baudrates can coexist on the same bus. Some devices use Automatic Baud Rate Detection (ABR) or autobauding.

There are four kinds of packets:

| Type | Length | Content | Purpose |
|---|---|---|---|
| Acknowledgement | 1 | `0xE5` |   |
| Short frame | 5 | `0x10`, C-field, A-field, checksum, `0x16` | sending simple commands |
| Long frame | ≥9 | `0x68`, length, length, `0x68`, C-field, A-field, CI-field, [0…252 payload bytes], checksum, `0x16` |   |
| control frame | 9 | `0x68`, `0x03`, `0x03`, `0x68`, C-field, A-field, CI-field, checksum, `0x16` | The control frame is a long frame with no payload. |

C-field is the control/function field. The sequence, from bit 7, is:

- bit 7: 0
- bit 6: 1 for master-to-slave, 0 for slave reply
- bit 5:
  - from master: FCB, frame count bit – indicates request to repeat message when reply was not received
  - from slave: ACD, access demand – 1 when slave wishes to transmit class-1 data, priority data (class-2 data is ordinary non-priority) – the master then should request the class-1 data transfer
- bit 4:
  - from master: FCV, frame count valid – when 0, slave should ignore FCB
  - from slave: DFC, data flow control – when 1, slave can not accept further data
- bit 3,2,1,0: F3,F2,F1,F0, function code – e.g. for short frame, 0 is for initialization of slave, xA is for class-1 (priority) data read, xB is for class-2 (normal) read. For long/control frame, x3 is sending data to slave, x8 is data reply from slave.

A-field is the address field. It is a 8-bit number:

- 0x00 – unset address, assigned at manufacture time, some meters fixed at this
- 0x01..0xFA – slave addresses
- 0xFB, 0xFC – reserved
- 0xFD – "broadcast" for secondary addressing, addressing done on network layer instead of on data link layer
- 0xFE – test broadcast, all slaves reply (collisions will happen, use for testing with a single slave; slave replies with its own address in A-field), also possible to use when there is only one slave on the bus
- 0xFF – broadcast, no reply from slaves

CI-field is the control information field. Defined at application layer.

Length field in control/long frame is sent twice. Both bytes have to be equal. Minimum value is 0x03, as C-field, A-field and CI-field are mandatory parts of the payload.

Slaves respond only to correctly formed packets that match their address. Any fault is indicated by lack of response. Absence of response is defined as no response for 330 bit periods (35 ms for 9600 bit/s, 1.1 s for 300 bit/s) plus 50 ms.

Numerical values are usually sent in BCD format.

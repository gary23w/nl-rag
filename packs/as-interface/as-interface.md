---
title: "AS-Interface"
source: https://en.wikipedia.org/wiki/AS-Interface
domain: as-interface
license: CC-BY-SA-4.0
tags: as-interface protocol, actuator sensor interface, binary sensor bus, lowest-level fieldbus
fetched: 2026-07-02
---

# AS-Interface

**Actuator Sensor Interface** (**AS-Interface** or **ASi**) is an industrial networking solution (Physical Layer, Data access Method and Protocol) used in PLC, DCS and PC-based automation systems. It is designed for connecting simple field I/O devices (e.g. binary ON/OFF devices such as actuators, sensors, rotary encoders, analog inputs and outputs, push buttons, and valve position sensors) in discrete manufacturing and process applications using a single two-conductor cable.

AS-Interface is an 'open' technology supported by a multitude of automation equipment vendors. The AS-Interface has been an international standard according to IEC 62026-2 since 1999.

AS-Interface is a networking alternative to the hard wiring of field devices. It can be used as a partner network for higher level fieldbus networks such as Profibus, DeviceNet, Interbus and Industrial Ethernet, for whom it offers a low-cost remote I/O solution. It is used in automation applications, including conveyor control, packaging machines, process control valves, bottling plants, electrical distribution systems, airport baggage carousels, elevators, bottling lines and food production lines. AS-Interface provides a basis for Functional Safety in machinery safety/emergency stop applications. Safety devices communicating over AS-Interface follow all the normal AS-Interface data rules. The AS-Interface specification is managed by AS-International, a member funded non-profit organization located in Gelnhausen/Germany. Several international subsidiaries exist around the world.

## History

AS-Interface was developed during the late 1980s and early 1990s by a development partnership of 11 companies mostly known for their offering of industrial non-contact sensing devices like inductive sensors, photoelectric sensors, capacitive sensors and ultrasonic sensors. Once development was completed the consortium was resolved and a member organization, *AS-International*, was founded. The first operational system was shown at the 1994 Hanover fair.

In 2018, a new technology step was presented at SPS IPC Drives in Nuremberg. This technology is named ASi-5. ASi-5 was developed by well-known manufacturers of automation technology.

## Use

The AS-Interface (from the Actuator Sensor Interface) has been developed as an alternative to conventional parallel cabling of sensors and actuators and offers the following advantages:

- Flexibility
- Cost saving
- Simplicity
- Reduction of installation errors
- Widely distributed
- Best networking opportunities
- Compatibility

The main application areas of the system are factory automation, process technology and home automation.

## Technology

The AS-Interface is a single-master system, this means a master device exchanges the input and output data with all configured devices. The transmission medium is an unshielded two-wire yellow flat cable. The cable is used for signal transmission and at the same time for power supply (30 V). The communication electronics and participants with low power requirements, like light beams, can be powered directly. Consumers with a higher energy requirement, such as valve terminals, can use a separate, usually black flat cable for power supply (30 V).

The sensors or actuators are often connected via the so-called piercing technology. The insulation of the polarity profiled flat cable is pierced by means of two penetrating mandrels during assembly, this makes an easy and simple connection with reduced assembly efforts. Sensors and actuators that do not have an AS-Interface connection can be connected to the system via modules. For modules with penetration technology, the AS-Interface flat cable must be used.

The topology of the AS-Interface networks is arbitrary. You can build lines, star, ring or tree structures.

### ASi-3 communication and transmission technology

A telegram (message frame) consists of 4-bit user data. The master communicates with the participants with a serial transmission protocol. Each subscriber is assigned an address by an addressing device or via the master. A maximum of 31 (standard devices) or 62 (advanced devices) nodes can be connected. Each node can have up to four inputs and/or four outputs for actuators or sensors. This provides up to 124 (4 x 31 = 124) input and 124 outputs on a standard device network (nodes addressed 1-31) or 248 (4 x 62 = 248) inputs and 248 outputs on an advanced network (nodes addressed 1A - 31A and 1B - 31B ). The serial communication is modulated onto the power supply. Manchester coding is used for the communication. For 31 participants, the cycle is 5 ms. To address 62 participants, two cycles are necessary. The topology of the AS-Interface is arbitrary, but without a repeater or extender, the cable length must not exceed 100 m. Due to a special terminating resistor (a combination of resistive and capacitive load), however, it is possible to increase the maximum cable length up to 300 m. Diagnostic devices or masters with built-in diagnostics simplify network troubleshooting. Failed slaves can be easily replaced, the master automatically redirects them. Safety at Work is the concept of functional safety used in ASi-3 technology. This means that safety-related components such as emergency stop actuations, door interlocks or light grids can be used in the AS-Interface network. This is a different transmission protocol overlaid onto the regular ASi protocol on the same cable and requires a separate safety master such as Siemens ASiMon devices on which your safety devices are configured. AS-Interface can provide safety support up to SIL (Safety Integrity Level) 3 according to IEC 61508 as well as Performance Level e (PL e) according to EN ISO 13849-1.

### ASi-5 communication and transmission technology

16 bits are available for cyclic transmission using ASi-5. A cyclic transmission of up to 32 bytes per participant is possible. An acyclic parameter channel with up to 256 bytes is available for each device as well. ASi-5 is to provide a set of up to 1536 binary inputs and 1536 binary outputs per Ethernet address. 1.2 ms cycle time can be achieved by the system for up to 24 participants. This fast cycle time allows new fields of applications that were previously reserved for expensive network systems. 96 participants can be addressed in an ASi-5 network. These 96 devices then have a cycle time of 5 ms. Communication diagnostics describes the information about message transmission between the connected nodes and the master. The system continuously monitors the transmission quality of the messages from each device connected. This single channel diagnosis is available in the system. Disturbed transmission channels are redirected automatically. Device diagnostics provides information about the connected device. The available diagnostics data are determined by the device manufacturer. Diagnostic data can be transmitted via the acyclic services with a data width of up to 256 bytes. The ASi-5 system is open for the use of parameter interfaces such as e.g. IO-Link. IO-Link devices can be efficiently collected over long distances and could be integrated cyclically up to 32 bytes. 16 safe bits are available for safety-related switching devices, such as emergency stop, light curtains, safety switches and similar are available. It is possible to achieve Safety Integrity Level (SIL)3 Performance Level e according to IEC 13849 for functional safety. ASi-5 uses a novel communication method. The new ASi-5 technology allows the use of ASi-3 components together with components of the new ASi-5 technology on a common cable. If ASi-3 devices are to be used together with ASi-5 components, then in addition to the corresponding devices the use of a new ASi-3 / ASi-5 master is required. Old systems can be easily upgraded by new devices with additional functions. New systems can be installed on a cable using proven ASi-3 components and new ASi-5 devices.

## Standardization

The AS-Interface is described in the international standard IEC 62026-2: 2015. Other local standards are: Europe: EN 62026-2: 2015 Japan: JIS C 82026-2 (2013) China: GB / T 18858.2 (2002) Korea: KS C IEC 62026-2 (2007)

AS-Interface products are certified by the AS-International Association e.V. Tests and certifications ensure that devices from different manufacturers work together. The concepts of functional safety at AS-Interface have been positively assessed by the TÜV (Technical Inspection Association) or the Institute for Occupational Safety of the German Social Accident Insurance and confirmed the fulfillment of the relevant safety standards.

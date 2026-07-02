---
title: "CAN bus (part 2/2)"
source: https://en.wikipedia.org/wiki/CAN_bus
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
part: 2/2
---

## Standardization and protocols

### CAN lower-layer standards

**ISO 11898 series** specifies physical and data link layer (levels 1 and 2 of the ISO/OSI model) of serial communication category called controller area network that supports distributed real-time control and multiplexing for use within road vehicles.

There are several CAN physical layer and other standards:

**ISO 11898-1:2015** specifies the data link layer (DLL) and physical signalling of the controller area network (CAN). This document describes the general architecture of CAN in terms of hierarchical layers according to the ISO reference model for open systems interconnection (OSI) established in ISO/IEC 7498-1 and provides the characteristics for setting up an interchange of digital information between modules implementing the CAN DLL with detailed specification of the logical link control (LLC) sublayer and medium access control (MAC) sublayer.

**ISO 11898-2:2016** specifies the high-speed (transmission rates of up to 1 Mbit/s) medium access unit (MAU), and some medium-dependent interface (MDI) features (according to ISO 8802-3), which comprise the physical layer of the controller area network. ISO 11898-2 uses a two-wire balanced signaling scheme. It is the most used physical layer in vehicle powertrain applications and industrial control networks.

**ISO 11898-3:2006** specifies low-speed, fault-tolerant, medium-dependent interface for setting up an interchange of digital information between electronic control units of road vehicles equipped with the CAN at transmission rates above 40 kbit/s up to 125 kbit/s.

**ISO 11898-4:2004** specifies time-triggered communication in the CAN (TTCAN). It is applicable to setting up a time-triggered interchange of digital information between electronic control units (ECU) of road vehicles equipped with CAN, and specifies the frame synchronization entity that coordinates the operation of both logical link and media access controls in accordance with ISO 11898-1, to provide the time-triggered communication schedule.

**ISO 11898-5:2007** specifies the CAN physical layer for transmission rates up to 1 Mbit/s for use within road vehicles. It describes the medium access unit functions as well as some medium-dependent interface features according to ISO 8802-2. This represents an extension of ISO 11898-2, dealing with new functionality for systems requiring low-power consumption features while there is no active bus communication.

**ISO 11898-6:2013** specifies the CAN physical layer for transmission rates up to 1 Mbit/s for use within road vehicles. It describes the medium access unit functions as well as some medium-dependent interface features according to ISO 8802-2. This represents an extension of ISO 11898-2 and ISO 11898-5, specifying a selective wake-up mechanism using configurable CAN frames.

**ISO 16845-1:2016** provides the methodology and abstract test suite necessary for checking the conformance of any CAN implementation of the CAN specified in ISO 11898-1.

**ISO 16845-2:2018** establishes test cases and test requirements to realize a test plan verifying if the CAN transceiver with implemented selective wake-up functions conform to the specified functionalities. The kind of testing defined in ISO 16845-2:2018 is named as conformance testing.

### CAN-based higher-layer protocols

As the CAN standard does not include common communication features, such as flow control, device addressing, and transportation of data blocks larger than one message, and above all, application data, many implementations of higher layer protocols were created. Several are standardized for a business area, although all can be extended by each manufacturer. For passenger cars, each manufacturer has its own standard.

CAN in Automation (CiA) is the international users' and manufacturers' organization that develops and supports CAN-based higher-layer protocols and their international standardization. Among these specifications are:

#### List of standardized approaches

- ARINC 812 or ARINC 825 (aviation industry)
- CANopen - CiA 301/302-2 and EN 50325-4 (industrial automation)
- IEC 61375-3-3 (use of CANopen in rail vehicles)
- DeviceNet (industrial automation)
- EnergyBus - CiA 454 and IEC 61851-3 (battery–charger communication)
- ISOBUS - ISO 11783 (agriculture)
- ISO-TP - ISO 15765-2 (transport protocol for automotive diagnostics)
- MilCAN (military vehicles)
- NMEA 2000 - IEC 61162-3 (marine industry)
- SAE J1939 (in-vehicle network for buses and trucks)
- SAE J2284 (in-vehicle networks for passenger cars)
- Unified Diagnostic Services (UDS) - ISO 14229 (automotive diagnostics)
- LeisureCAN - open standard for the leisure craft/vehicle industry

#### List of other approaches

- CANaerospace - Stock (for the aviation industry)
- CAN Kingdom - Kvaser (embedded control system)
- CCP/XCP (automotive ECU calibration)
- GMLAN - General Motors (for General Motors)
- RV-C - RVIA (used for recreational vehicles)
- SafetyBUS p - Pilz (used for industrial automation)
- UAVCAN (aerospace and robotics)
- CSP (CubeSat Space Protocol)
- VSCP (Very Simple Control Protocol) a free automation protocol suitable for all sorts of automation tasks

#### CANopen Lift

The CANopen Special Interest Group (SIG) "Lift Control", which was founded in 2001, develops the CANopen application profile CiA 417 for lift control systems. It works on extending the features, improves technical content and ensures that the current legal standards for lift control systems are met. The first version of CiA 417 was published (available for CiA members) in summer 2003, version 2.0 in February 2010, version 2.1.0 in July 2012, version 2.2.0 in December 2015, and version 2.3.1 in February 2020.

Jörg Hellmich (ELFIN GmbH) is the chairman of this SIG and manages a wiki of the CANopen lift community with content about CANopen lift.

### DBC (CAN database files)

CAN DBC files are standardized ASCII files used to define messages sent over a CAN bus. They define the format and purpose of each type of message, including the message IDs, signal names, scaling, offsets, and data types, and provide an interoperable aid to developing CAN bus applications.


## Security

CAN is a low-level protocol and does not support any security features intrinsically. There is also no encryption in standard CAN implementations, which leaves these networks open to man-in-the-middle frame interception. In most implementations, applications are expected to deploy their own security mechanisms; e.g., to authenticate incoming commands or the presence of certain devices on the network. Failure to implement adequate security measures may result in various sorts of attacks if the opponent manages to insert messages on the bus. While passwords exist for some safety-critical functions, such as modifying firmware, programming keys, or controlling antilock brake actuators, these systems are not implemented universally and have a limited number of seed/key pairs.


## Development tools

When developing or troubleshooting the CAN bus, examination of hardware signals can be very important. Logic analyzers and bus analyzers are tools that collect, analyse, decode and store signals so people can view the high-speed waveforms at their leisure. There are also specialist tools as well as CAN bus monitors.

A CAN bus monitor is an analysis tool, often a combination of hardware and software, used during development of hardware that uses the CAN bus.

Typically the CAN bus monitor will listen to the traffic on the CAN bus in order to display it in a user interface. Often the CAN bus monitor offers the possibility to simulate CAN bus activity by sending CAN frames to the bus. The CAN bus monitor can therefore be used to validate expected CAN traffic from a given device or to simulate CAN traffic in order to validate the reaction from a given device connected to the CAN bus.


## Licensing

Bosch holds patents on the technology, though those related to the original protocol have now expired. Manufacturers of CAN-compatible microprocessors pay license fees to Bosch for use of the CAN trademark and any of the newer patents related to CAN FD, and these are normally passed on to the customer in the price of the chip. Manufacturers of products with custom ASICs or FPGAs containing CAN-compatible modules need to pay a fee for the CAN Protocol License if they wish to use the CAN trademark or CAN FD capabilities.

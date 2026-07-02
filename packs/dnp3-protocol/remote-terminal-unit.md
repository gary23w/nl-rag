---
title: "Remote terminal unit"
source: https://en.wikipedia.org/wiki/Remote_terminal_unit
domain: dnp3-protocol
license: CC-BY-SA-4.0
tags: dnp3 protocol, distributed network protocol, scada outstation, utility telemetry
fetched: 2026-07-02
---

# Remote terminal unit

A **remote terminal unit** (**RTU**) is a microprocessor-controlled electronic device that interfaces objects in the physical world to a distributed control system or supervisory control and data acquisition (SCADA) system by transmitting telemetry data to a master system, and by using messages from the master supervisory system to control connected objects. Other terms that may be used for RTU are **remote telemetry unit** and **remote telecontrol unit**.

## Architecture

An RTU monitors the field digital and analog parameters and transmits data to a SCADA Master Station. It runs setup software to connect data input streams to data output streams, define communication protocols, and troubleshoot installation problems in the field.

An RTU may consist of one complex circuit card consisting of various sections needed to do a custom-fitted function, or may consist of many circuit cards including a CPU or processing with communications interface(s), and one or more of the following: (AI) analog input, (DI) digital (status) input, (DO/CO) digital (or control relay) output, or (AO) analog output card(s).

An RTU might even be a small process control unit with a small database for PID, Alarming, Filtering, Trending and other functions complemented with some BASIC (programming language) tasks. Modern RTUs typically support the IEC 61131-3 programming standard for programmable logic controllers. Since RTUs may be routinely deployed in pipeline and grid guarding systems, or in other hard-to-reach or extreme environments (for example in the Biosphere 2 project), they are required to operate under harsh conditions, and implement energy-saving measures (such as switching off IO modules when not in use). For example, it communicates via RS485 or wireless communication links in a multi-drop configuration. In this type of configuration it is a remote unit that collects data and performs simple control tasks. It does not have moving parts and uses extremely low power and is often solar powered.

### Power supply

A form of power supply will be included for operation from the AC mains for various CPU, status wetting voltages and other interface cards. This may consist of AC to DC converters where operated from a station battery system.

RTUs may include a battery and charger circuitry to continue operation in event of AC power failure for critical applications where a station battery is not available.

### Digital (status) inputs

Most RTUs have a section called *input status cards* to read ON/OFF information from the field. They do this by checking if a contact (like a switch) is open or closed at the RTU location. This contact could belong to different devices, like:

- Electrical breakers (open or closed)
- Valves (open or closed)
- Alarms (active or not)
- Machines (in position or not)

Some RTUs can also count events (like how many times a contact opens/closes), but this is optional.

### Analog inputs

An RTU can monitor analog inputs of different types including 0-1 mA, 4–20 mA current loop, 0–10 V., ±2.5 V, ±5.0 V etc. Many RTU inputs buffer larger quantities via transducers to convert and isolate real-world quantities from sensitive RTU input levels. An RTU can also receive analog data via a communication system from a master or intelligent electronic device (IED) sending data values to it.

The RTU or host system translates and scales this raw data into the appropriate units such as the quantity of water left, temperature degrees, or Megawatts, before presenting the data to the user via the human–machine interface.

### Digital (control relay) outputs

RTUs may drive high current capacity relays to a digital output (or "DO") board to switch power on and off to devices in the field. The DO board switches voltage to the coil in the relay, which closes the high current contacts, which completes the power circuit to the device.

RTU outputs may also consist of driving a sensitive logic input on an electronic PLC, or other electronic device using a sensitive 5 V input.

### Analog outputs

While not as commonly used, analog outputs may be included to control devices that require varying quantities, such as graphic recording instruments (strip charts). Summed or processed data quantities may be generated in a master SCADA system and output for display locally or remotely, wherever needed.

### Software and logic control

Modern RTUs are usually capable of executing simple programs autonomously without involving the host computers of the DCS or SCADA system to simplify deployment and to provide redundancy for safety reasons. An RTU in a modern water management system will typically have code to modify its behavior when physical override switches on the RTU are toggled during maintenance-by-maintenance personnel. This is done for safety reasons; a miscommunication between the system operators and the maintenance personnel could cause system operators to mistakenly enable power to a water pump when it is being replaced, for example.

Maintenance personnel should have any equipment they are working on disconnected from power and locked to prevent damage and/or injury.

### Communications

An RTU may be interfaced to multiple master stations and IEDs with different communication protocols (usually serial (RS-232, RS-485, RS-422) or Ethernet). An RTU may support standard protocols (Modbus, IEC 60870-5-101/103/104, DNP3, IEC 60870-6-ICCP, IEC 61850 etc.) to interface any third-party software.

Data transfer may be initiated from either end using various techniques to ensure synchronization with minimal data traffic. The master may poll its subordinate unit (Master to RTU or RTU to IED) for changes of data on a periodic basis. Analog value changes will usually be reported only on changes outside a set limit from the last transmitted value. Digital (status) values observe a similar technique and only transmit groups (bytes) when one included point (bit) changes. Another method used is where a subordinate unit initiates an update of data upon a predetermined change in analog or digital data. Complete data transmission must be performed periodically, with either method, to ensure full synchronization and eliminate stale data. Most communication protocols support both methods, programmable by the installer.

Multiple RTUs or IEDs may share a communications line, in a multi-drop scheme, as units are addressed uniquely and only respond to their own polls and commands.

#### IED communications

IED communications transfer data between the RTU and an IED. This can eliminate the need for many hardware status inputs, analog inputs, and relay outputs in the RTU. Communications are accomplished by copper or fibre optics lines.

#### Master communications

Master communications usually occur between an RTU and a larger control system or a data collection system (incorporated into a larger system). Data may be moved using a copper, fibre optic or radio frequency communication system.

## Applications

- Remote monitoring of functions and instrumentation for:
  - Oil and gas (offshore platforms, onshore oil wells, pumpstations on pipelines)
  - Networks of pump stations (wastewater collection, or for water supply)
  - Environmental monitoring systems (pollution, air quality, emissions monitoring)
  - Mine sites
  - Air traffic equipment such as navigation aids (DVOR, DME, ILS and GP)
- Remote monitoring and control of functions and instrumentation for:
  - Hydro-graphic (water supply, reservoirs, sewage systems)
  - Electrical power transmission networks and associated equipment
  - Natural gas networks and associated equipment
  - Outdoor warning sirens
  - The Biosphere II project

---
title: "Embedded Systems/Common Protocols"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Common_Protocols
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Common Protocols

<

Embedded Systems

This is a list of common protocols used in embedded systems. Eventually, this list will become hyperlinks to sources of information on each. Many of them are byte-stream protocols that can be transmitted by a variety of serial protocols on a variety of hardware.

- I2C
- RS-485 is an extremely common hardware arrangement used by many embedded protocols:
  - CAN on top of RS485
  - DeviceNet on top of CAN. Wikipedia: DeviceNet
  - NMEA 2000 on top of DeviceNet. Wikipedia: NMEA 2000
  - DMX on top of RS485. Wikipedia: DMX512
  - Modbus on top of RS485
  - see Serial Programming/RS-485, Robotics/Computer Control/The Interface/Networks#RS485, Embedded Control Systems Design/Field busses, Embedded Systems/Serial and Parallel IO#RS-485
- MIDI. official MIDI interface schematics (1); beautiful MIDI IN schematic (2).
- BlueTooth
- InfraRed
- ZigBee
- SPI
- RS-232
- USB
- IP Over Serial Connections
- MINES (Microcontroller Interpreter for Networked Embedded Systems) was designed for very small embedded systems (see Gallery of MINES Devices).
- the Tiny Embedded Network
- IEEE Standard for Sensor Transducer Interface
- the three byte Mini SSC protocol (and another Mini SSC protocol example)
- JTAG
- NTSC / PAL television video output: w:TV Typewriter, Generating TV signal by PSoC, Generating TV signal with the PICs, PIC Breakout, ... Parallax Propeller has a video generator ...
- The low-latency Myrinet protocol is used in over 100 of the TOP500 supercomputers, as of June 2005.
- The low-latency InfiniBand protocol is used in over 100 of the TOP500 supercomputers, as of November 2010.
- The various Audio over Ethernet (AoE) protocols are generally designed to be relatively low latency.
- The LIN-Bus (w:Local Interconnect Network), a low-cost vehicle communication network
- Modbus (w:Modbus) protocol works over a variety of hardware interfaces, including
  - Modbus RTU over RS-485
  - Modbus ASCII over 7-bit asynchronous serial lines
  - Modbus TCP over Ethernet
- Firmata is a generic protocol that allows people to completely control the Arduino from software on a host computer. Arduino reference for Firmata; Firmata wiki.
- rosserial "rosserial ... is a general protocol for sending ROS messages over serial links." Code is available for Arduino and a variety of other platforms. (It was designed for ROS, the w: Robot Operating System).
- S.N.A.P - Scaleable Node Address Protocol [1] is media-independent, building on an underlying byte-oriented communication layer.
- Yet Another Scalable Protocol (YASP)
- Labor-Octet-Protocol (LOP) is a simple protocol originally implemented on AVR microcontrollers; it builds on an underlying byte-oriented communication layer and provides support for both message-oriented (all-or-nothing) and stream-oriented communication.
- Inter-Chip Serial Communications (ICSC) is a simple, high-reliability media-independent protocol originally implemented on Arduino.
- Perhaps the simplest-to-parse variable-size packet container format is the netstring format.w:netstring
- JSON (perhaps encapsulated in packets of one of the above formats) seems to be gaining popularity as a way to transmit complex data structures, in a way that is easy for humans to read and debug.[2] w:JSON

---
title: "MIDI 2.0"
source: https://en.wikipedia.org/wiki/MIDI_2.0
domain: midi-2
license: CC-BY-SA-4.0
tags: midi 2.0 protocol, midi 2 bidirectional, midi capability inquiry, general midi protocol
fetched: 2026-07-02
---

# MIDI 2.0

The **MIDI 2.0** standard was unveiled on January 17, 2020, at the Winter NAMM Show in Anaheim, California. Representatives Yamaha, ROLI, Microsoft, Google, and the MIDI Association introduced the update, which enables bidirectional communication while maintaining backward compatibility.

Research on the new MIDI protocol began in 2005. Prototype devices showcasing wired and wireless connections have been shown privately at NAMM. Licensing and product certification policies have been developed, although no projected release date was announced. Proposed physical layer and transport layer included Ethernet-based protocols such as RTP MIDI and Audio Video Bridging/Time-Sensitive Networking, as well as User Datagram Protocol (UDP)-based transport.

AMEI and MMA announced that complete specifications will be published following interoperability testing of prototype implementations from major manufacturers such as Google, Yamaha, Steinberg, Roland, Ableton, Native Instruments, and ROLI, among others. In January 2020, Roland announced the A-88mkII controller keyboard that supports MIDI 2.0. MIDI 2.0 includes MIDI Capability Inquiry specification for property exchange and profiles, and the new Universal MIDI Packet format for high-speed transports which supports both MIDI 1.0 and MIDI 2.0 voice messages.

Some devices operating MIDI 1.0 can "retrofit" some 2.0 features. Since its release in early January 2020 by the MIDI Manufacturers Association, more details have yet to come out about the new update. As of 2021 there were five components to MIDI such as; M2-100-U v1.0 MIDI 2.0 Specification Overview, M2-101-UM v1.1 MIDI-CI Specification, M2-102-U v1.0 Common Rules for MIDI-CI Profiles, M2-103-UM v1.0 Common Rules for MIDI-CI PE and M2-104-UM v1.0 UMP and MIDI 2.0 Protocol Specification. Other specifications regarding MIDI 2.0 include: allowing the use of 32,000 controllers and wide range note enhancements. These enhancements are made better through the property exchange. In June 2023 updated and new MIDI 2.0 specifications were released consisting of M2-100-U MIDI 2.0 Specification Overview, Version 1.1, M2-101-UM MIDI Capability Inquiry (MIDI-CI), Version 1.2, M2-102-U Common Rules for MIDI-CI Profiles, Version 1.1, M2-104-UM Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol, Version 1.1, and M2-116-U MIDI Clip File (SMF2), Version 1.0.

## Property exchange

The property exchange in MIDI 2.0 uses JSON. This provides a human-readable format to exchange data sets. In doing so, this opens up a wide range of capabilities for MIDI 2.0. JSON allows any plugged-in device, whether it be a keyboard, piano, or any other electrical device, to describe what it is doing and what it can do, rather than having the person operating it change their settings every time they operate a new device. For example, a MIDI keyboard that is plugged into an iOS device with specific MIDI settings can now be plugged into a Windows device without manually changing settings. Any musical component used in one device will be recognized and automatically altered in another.

## MIDI Capability Inquiry

MIDI Capability Inquiry (MIDI-CI) specifies Universal SysEx messages to implement device profiles, parameter exchange, and MIDI protocol negotiation. The specifications were released in November 2017 by AMEI and in January 2018 by the MMA.

Parameter exchange defines methods for inquiry of device capabilities, such as supported controllers, patch names, instrument profiles, device configuration and other metadata, and to get or set device configuration settings. Property exchange uses System Exclusive messages that carry JSON format data. Profiles define common sets of MIDI controllers for various instrument types, such as drawbar organs and analog synths, or for particular tasks, improving interoperability between instruments from different manufacturers. Protocol negotiation allows devices to employ the Next Generation protocol or manufacturer-specific protocols.

## Universal MIDI Packet

MIDI 2.0 defines a new Universal MIDI Packet format, which contains messages of varying lengths (32, 64, 96 or 128 bits) depending on the payload type. This new packet format supports a total of 256 MIDI channels, organized in 16 groups of 16 channels; each group can carry either a MIDI 1.0 Protocol stream or a new MIDI 2.0 Protocol stream, and can also include system messages, system exclusive data, and timestamps for precise rendering of several simultaneous notes. To simplify initial adoption, existing products are explicitly allowed to only implement MIDI 1.0 messages. The Universal MIDI Packet is intended for high-speed transport such as USB and Ethernet and is not supported on the existing 5-pin DIN connections. System Real-Time and System Common messages are the same as defined in MIDI 1.0.

## New protocol

As of January 2019, the draft specification of the new protocol supports all core messages that also exist in MIDI 1.0, but extends their precision and resolution; it also defines many new high-precision controller messages. The specification defines default translation rules to convert between MIDI 2.0 Channel Voice and MIDI 1.0 Channel Voice messages that use different data resolution, as well as map 256 MIDI 2.0 streams to 16 MIDI 1.0 streams.

## Data transfer formats

System Exclusive 8 messages use a new 8-bit data format, based on Universal System Exclusive messages. Mixed Data Set messages are intended to transfer large sets of data. System Exclusive 7 messages use the previous 7-bit data format.

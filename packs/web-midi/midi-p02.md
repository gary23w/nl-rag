---
title: "MIDI (part 2/2)"
source: https://en.wikipedia.org/wiki/MIDI
domain: web-midi
license: CC-BY-SA-4.0
tags: web midi api, midi message port, midi input output, musical instrument digital interface
fetched: 2026-07-02
part: 2/2
---

## Alternative hardware transports

In addition to using a 31.25 kbit/s current-loop over a DIN connector, the same data can be transmitted over different hardware transports such as USB, FireWire, and Ethernet.

### USB and FireWire

Members of the USB-IF in 1999 developed a standard for MIDI over USB, the "Universal Serial Bus Device Class Definition for MIDI Devices". MIDI over USB has become increasingly common as other interfaces that had been used for MIDI connections (ISA card, game port, etc.) disappeared from personal computers. Linux, Microsoft Windows, Macintosh OS X, and Apple iOS operating systems include standard class drivers to support devices that use the "Universal Serial Bus Device Class Definition for MIDI Devices".

Apple Computer developed the FireWire interface during the 1990s. It began to appear on digital video (DV) cameras toward the end of the decade, and on G3 Macintosh models in 1999. It was created for use with multimedia applications. Unlike USB, FireWire uses intelligent controllers that can manage their own transmission without attention from the main CPU. As with standard MIDI devices, FireWire devices can communicate with each other with no computer present.

### XLR connectors

The Octave-Plateau Voyetra-8 synthesizer was an early MIDI implementation using XLR3 connectors in place of the 5-pin DIN. It was released in the pre-MIDI years and later retrofitted with a MIDI interface but kept its XLR connector.

#### Serial parallel, and joystick port

As computer-based studio setups became common, MIDI devices that could connect directly to a computer became available. These typically used the 8-pin mini-DIN connector that was used by Apple for serial ports prior to the introduction of the Blue and White G3 models. MIDI interfaces intended for use as the centerpiece of a studio, such as the Mark of the Unicorn MIDI Time Piece, were made possible by a fast transmission mode that could take advantage of these serial ports' ability to operate at 20 times the standard MIDI speed. Mini-DIN ports were built into some late-1990s MIDI instruments so they could connect directly to a computer. Some devices connected via a PCs' DB-25 parallel port, or through the DA-15 game port found on many PC sound cards.

#### mLAN

Yamaha introduced the mLAN protocol in 1999. It was conceived as a local area network for musical instruments using FireWire as the transport and was designed to carry multiple MIDI channels together with multichannel digital audio, data file transfers, and timecode. mLan was used in a number of Yamaha products, notably digital mixing consoles and the Motif synthesizer, and in third-party products such as the PreSonus FIREstation and the Korg Triton Studio. No new mLan products have been released since 2007.

### SCSI Musical Data Interchange

SCSI Musical Data Interchange (SMDI) is a method of using SCSI to transfer information between samplers and computers. SMDI is based loosely on SDS. SMDI uses SCSI instead of SDS to transfer sample data between devices. SDMI was used by some samplers and hard disk recorders in the 1990s (e.g. Kurzweil K2000 and Peavey SP Sample Playback Synthesizer) for fast bidirectional sample transport to hard disk drives and magneto-optical drives.

### Ethernet and Internet Protocol

Computer network implementations of MIDI provide network routing capabilities, and the high-bandwidth channel that earlier alternatives to MIDI, such as ZIPI, were intended to bring. Proprietary implementations have existed since the 1980s, some of which use fiber optic cables for transmission. The Internet Engineering Task Force's RTP-MIDI open specification has gained industry support. Apple has supported this protocol from Mac OS X 10.4 onwards, and a Windows driver based on Apple's implementation exists for Windows XP and newer versions.

### Wireless

Systems for wireless MIDI transmission have been available since the 1980s. Several commercially available transmitters allow wireless transmission of MIDI and OSC signals over Wi-Fi and Bluetooth. iOS devices are able to function as MIDI control surfaces, using Wi-Fi and OSC. An XBee radio can be used to build a wireless MIDI transceiver as a do-it-yourself project. Android devices are able to function as full MIDI control surfaces using several different protocols over Wi-Fi and Bluetooth.


## MIDI 2.0

The MIDI 2.0 standard was unveiled on January 17, 2020, at the Winter NAMM Show in Anaheim, California. Representatives Yamaha, ROLI, Microsoft, Google, and the MIDI Association introduced the update, which enables bidirectional communication while maintaining backward compatibility.

Research on the new MIDI protocol began in 2005. Prototype devices showcasing wired and wireless connections have been shown privately at NAMM. Licensing and product certification policies have been developed, although no projected release date was announced. Proposed physical layer and transport layer included Ethernet-based protocols such as RTP MIDI and Audio Video Bridging/Time-Sensitive Networking, as well as User Datagram Protocol (UDP)-based transport.

AMEI and MMA announced that complete specifications will be published following interoperability testing of prototype implementations from major manufacturers such as Google, Yamaha, Steinberg, Roland, Ableton, Native Instruments, and ROLI, among others. In January 2020, Roland announced the A-88mkII controller keyboard that supports MIDI 2.0. MIDI 2.0 includes MIDI Capability Inquiry specification for property exchange and profiles, and the new Universal MIDI Packet format for high-speed transports which supports both MIDI 1.0 and MIDI 2.0 voice messages.

Some devices operating MIDI 1.0 can "retrofit" some 2.0 features. Since its release in early January 2020 by the MIDI Manufacturers Association, more details have yet to come out about the new update. As of 2021 there were five components to MIDI such as; M2-100-U v1.0 MIDI 2.0 Specification Overview, M2-101-UM v1.1 MIDI-CI Specification, M2-102-U v1.0 Common Rules for MIDI-CI Profiles, M2-103-UM v1.0 Common Rules for MIDI-CI PE and M2-104-UM v1.0 UMP and MIDI 2.0 Protocol Specification. Other specifications regarding MIDI 2.0 include: allowing the use of 32,000 controllers and wide range note enhancements. These enhancements are made better through the property exchange. In June 2023 updated and new MIDI 2.0 specifications were released consisting of M2-100-U MIDI 2.0 Specification Overview, Version 1.1, M2-101-UM MIDI Capability Inquiry (MIDI-CI), Version 1.2, M2-102-U Common Rules for MIDI-CI Profiles, Version 1.1, M2-104-UM Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol, Version 1.1, and M2-116-U MIDI Clip File (SMF2), Version 1.0.

---
title: "RDM (lighting)"
source: https://en.wikipedia.org/wiki/RDM_(lighting)
domain: dmx512-lighting
license: CC-BY-SA-4.0
tags: dmx512 protocol, dmx lighting control, stage lighting control, entertainment lighting bus
fetched: 2026-07-02
---

# RDM (lighting)

**Remote Device Management** (**RDM**) is an addition to the DMX512 control protocol for stage lighting equipment, introduced in 2006. DMX512 was developed in the late 1980s as a standard protocol for lighting consoles to communicate with dimmers, but has since been used for more complex applications, including the control of intelligent lighting fixtures. The addition of RDM addresses many of the shortcomings of DMX512, which is unidirectional with no support for metadata.

RDM revises the DMX512 standard to include bidirectional communication, and introduces additional options for the configuration of fixtures over the DMX512 network. RDM is backwards compatible with existing DMX512 devices, and requires few changes to the physical cabling of DMX512 networks.

The RDM standard was developed by the Entertainment Services and Technology Association, and is maintained as ANSI E1.20.

## Background

DMX512 has been the standard for the control of theatrical lighting devices, including intelligent lighting fixtures, since the mid-1990s. DMX512, based on the RS-485 protocol commonly used in industrial control systems, was the first universal standard for the control of stage lighting equipment.

RDM's predecessor DMX512 is a unidirectional protocol with little capacity for error reporting or automated configuration. A single cable carries one "universe" of DMX512, consisting of 512 "addresses," each of which can be assigned a value from 0 to 255. In the earliest applications of DMX512 networks, a control console would be connected to a rack of dimmers. Within the dimmer rack, a single DMX address would control the voltage level of a single dimmer from 0% to 100%.

In more complex applications involving intelligent lighting fixtures, a DMX address is assigned to each function of a fixture, with some fixtures utilizing blocks of addresses numbering in the dozens. A device's identity within the network is defined by the first address of the block it occupies, akin to a static IP address. In a standard DMX network, each fixture must be manually configured with a starting address, and the same starting address must be separately programmed into the control console.

## Applications

RDM serves multiple main functions: identification, status reporting, and configuration.

Identification allows a control console to automatically detect all devices on the DMX network, distinct from their DMX address. This assists the operator in determining which of their devices have even powered on.

Configuration allows the control console to change the address and other properties of a device. This functionality avoids the time-consuming process of manually setting DMX addresses on each fixture. Intelligent lighting fixtures often have multiple control modes and other settings, which can also be configured over RDM with the proper software support.

Status reporting from lighting fixtures enables the operator to view the status of their devices, including faults such as burnt-out lamps or failed motors.

## Compatibility

RDM is enabled in many new lighting devices, and can be used in the same network as non-RDM-enabled devices, using existing cabling. DMX512 devices that do not support RDM should ignore all RDM commands, but in practice, some devices do malfunction when receiving RDM signals.

DMX networks may include splitters with opto-isolator functionality, which only allow signal transmission in one direction, and filter out RDM signals. DMX splitters that pass through RDM signals are available, but not all splitters include this functionality.

RDM is a technology specific to DMX512 signals over standard twisted-pair wire. Protocols that carry DMX signal over IP networks, such as Streaming ACN and Art-Net, have their own implementations of remote control which are backwards compatible with RDM.

## Technical specifications

### RDM Physical layer

The RDM protocol and the RDM physical layer were designed to be compatible with legacy equipment. All compliant legacy DMX512 receivers should be usable in mixed systems with an RDM controller (console) and RDM responders (receivers). DMX receivers and RDM responders can be used with a legacy DMX console to form a DMX512 only system. From a user’s point of view the system layout is very similar to a DMX system. The controller is placed at one end of the main cable segment. The cable is run receiver to receiver in a daisy-chain fashion. RDM enabled splitters are used the same way DMX splitters would be. The far end (the non console or splitter end) of a cable segment should be terminated.

RDM requires two significant topology changes compared to DMX. However, these changes are generally internal to equipment and therefore not seen by the user.

First, a controller’s (console’s) output is terminated. Second, this termination must provide a bias to keep the line in the ‘marking state’ when no driver is enabled.

The reason for the additional termination is that a network segment will be driven at many points along its length. Hence, either end of the segment, if unterminated, will cause reflections.

A DMX console’s output drivers are always enabled. The RDM protocol is designed so that except during discovery, there should never be data collisions. To ensure this lack of collisions, while making possible implementation on different platforms, there are times when all line drivers are required to be disabled. If nothing more than the termination was done, the line would float to some unknown level. In that case one or more random changes might be read on the line. These random changes greatly decrease system accuracy. So the biasing of the line is required

To assure this, section 2.4.1 (Line Bias Networks) of the standard says; “The command port shall provide a means to bias the termination of the data link to a value of at least 245 mV and verified by using the test circuit described in Appendix F.”

The standard further states that, the biasing mean “shall be polarized such that Data+ of the data link is positive with respect to Data- the data link. The Line Biasing network shall maintain this bias when the data link is loaded with the equivalent of 32 unit loads and common mode voltage is varied over the range of +7 volts to -7 volts DC.”

The standard does not require any particular circuit for providing the basis and termination; however, the simplest method is often a passive pull apart network.

Whatever method is used must be tested with the chosen driver chip to see that the design combination still meets the requirement of E1.20. Tests are given in Appendix F of the standard. These tests are for design verification and are not required as production testing. Experience has shown many EIA485 drivers designed for 5 volt operation will pass the required tests. It is not so clear that all 3.3 volt parts will pass. In either case this performance must be verified. Details of the pull apart network and the tests can be found in **ANSI E1.20 - 2006**.

### Protocol

RDM packets are interspersed with the existing DMX data packets being used to control the lighting. The DMX 512 specification requires that DMX packets begin with the start code. The default Start Code is 0x00(also known as the Null Start Code). By using the start code 0xCC, RDM packets can be safely inserted between DMX data packets without older non-RDM aware devices attempting to read them.

The DMX 512 specification required DMX connectors to be a 5-pin XLR type, with only the first 3 pins being used (pins 4 and 5 were reserved for "future use"). Unfortunately, various manufacturers started using the final two pins for various, proprietary purposes, such as low-voltage power or proprietary talk-back protocols. As a result, the decision was made to have all RDM communication on pins 2 and 3. This raises data collision concerns.

The RDM standard addresses this problem by ensuring that in all cases (except discovery) only one device is authorized to be transmitting at any given time. Only the controller (of which there can be only one) can start an RDM exchange. Responders can speak only if spoken to. The controller will always initiate all RDM communication.

All RDM devices have a unique identifier (UID) that consists of a manufacturer ID and serial number.

RDM communication can be broken down into three types:

- Discovery
- Unicast communication
- Broadcast communication

### Discovery

Discovery is the only situation in which data collisions can occur assuming all connected devices behave correctly. The controller will broadcast a discovery command to all devices and await a response. If there are more than one device connected, the simultaneous responses will likely result in a data collision, and the controller will not receive a correctly formatted response. The controller will then refine its search to a smaller range of UIDs according to a binary search pattern. Once the controller receives a correct response it will attempt to mute the responding device. After a successful mute, the device is no longer allowed to respond to discovery messages, and the controller can continue searching for other devices. Once all devices have been muted (no responses are received to discovery commands), the discovery process is finished and the controller will hold a list of all connected devices.

The controller will need to periodically perform searches for new devices and assert that already discovered devices are still connected.

### Unicast communication

General communication with a specific fixture occurs in a request-response pattern. The controller sends the request to the device, addressing it by the device's UID. When the request has been sent, the controller relinquishes control of the DMX line for a given period of time, so the device can transmit its response. Unicast communication is the only way in which data can be retrieved from a fixture (other than its UID which can be obtained using the discovery mechanism mentioned above). If the device does not respond within a given period of time, the controller can assume communication has failed, and may retry.

### Broadcast communication

To quickly send instructions to multiple fixtures, RDM allows for broadcast communication. This allows the controller to send an instruction to all devices, or all devices from one manufacturer. As more than one device might be receiving the message, responses are not permitted in broadcast communication except during the Discovery process.

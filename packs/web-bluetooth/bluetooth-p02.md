---
title: "Bluetooth (part 2/2)"
source: https://en.wikipedia.org/wiki/Bluetooth
domain: web-bluetooth
license: CC-BY-SA-4.0
tags: web bluetooth api, bluetooth low energy gatt, gatt service characteristic, bluetooth device pairing
fetched: 2026-07-02
part: 2/2
---

## Technical information

### Architecture

#### Software

Seeking to extend the compatibility of Bluetooth devices, the devices that adhere to the standard use an interface called HCI (Host Controller Interface) between the host and the controller.

High-level protocols such as the SDP (Protocol used to find other Bluetooth devices within the communication range, also responsible for detecting the function of devices in range), RFCOMM (Protocol used to emulate serial port connections) and TCS (Telephony control protocol) interact with the baseband controller through the L2CAP (Logical Link Control and Adaptation Protocol). The L2CAP protocol is responsible for the segmentation and reassembly of the packets.

#### Hardware

The hardware that makes up the Bluetooth device is made up of, logically, two parts; which may or may not be physically separate. A radio device, responsible for modulating and transmitting the signal; and a digital controller. The digital controller is likely a CPU, one of whose functions is to run a Link Controller; and interfaces with the host device; but some functions may be delegated to hardware. The Link Controller is responsible for the processing of the baseband and the management of ARQ and physical layer FEC protocols. In addition, it handles the transfer functions (both asynchronous and synchronous), audio coding (e.g. SBC (codec)) and data encryption. The CPU of the device is responsible for attending the instructions related to Bluetooth of the host device, in order to simplify its operation. To do this, the CPU runs software called Link Manager that has the function of communicating with other devices through the LMP protocol.

A Bluetooth device is a short-range wireless device. Bluetooth devices are fabricated on RF CMOS integrated circuit (RF circuit) chips.

### Bluetooth protocol stack

Bluetooth is defined as a layer protocol architecture consisting of core protocols, cable replacement protocols, telephony control protocols, and adopted protocols. Mandatory protocols for all Bluetooth stacks are LMP, L2CAP and SDP. In addition, devices that communicate with Bluetooth almost universally can use these protocols: HCI and RFCOMM.

#### Link Manager

The Link Manager (LM) is the system that manages establishing the connection between devices. It is responsible for the establishment, authentication and configuration of the link. The Link Manager locates other managers and communicates with them via the management protocol of the LMP link. To perform its function as a service provider, the LM uses the services included in the Link Controller (LC). The Link Manager Protocol basically consists of several PDUs (Protocol Data Units) that are sent from one device to another. The following is a list of supported services:

- Transmission and reception of data.
- Name request
- Request of the link addresses.
- Establishment of the connection.
- Authentication.
- Negotiation of link mode and connection establishment.

#### Host Controller Interface

The Host Controller Interface provides a command interface between the controller and the host.

#### Logical Link Control and Adaptation Protocol

The *Logical Link Control and Adaptation Protocol* (L2CAP) is used to multiplex multiple logical connections between two devices using different higher level protocols. Provides segmentation and reassembly of on-air packets.

In *Basic* mode, L2CAP provides packets with a payload configurable up to 64 kB, with 672 bytes as the default MTU, and 48 bytes as the minimum mandatory supported MTU.

In *Retransmission and Flow Control* modes, L2CAP can be configured either for isochronous data or reliable data per channel by performing retransmissions and CRC checks.

Bluetooth Core Specification Addendum 1 adds two additional L2CAP modes to the core specification. These modes effectively deprecate original Retransmission and Flow Control modes:

**Enhanced Retransmission Mode (ERTM)**

This mode is an improved version of the original retransmission mode. This mode provides a reliable L2CAP channel.

**Streaming Mode (SM)**

This is a very simple mode, with no retransmission or flow control. This mode provides an unreliable L2CAP channel.

Reliability in any of these modes is optionally and/or additionally guaranteed by the lower layer Bluetooth BDR/EDR air interface by configuring the number of retransmissions and flush timeout (time after which the radio flushes packets). In-order sequencing is guaranteed by the lower layer.

Only L2CAP channels configured in ERTM or SM may be operated over AMP logical links.

#### Service Discovery Protocol

The *Service Discovery Protocol* (SDP) allows a device to discover services offered by other devices, and their associated parameters. For example, when you use a mobile phone with a Bluetooth headset, the phone uses SDP to determine which Bluetooth profiles the headset can use (Headset Profile, Hands Free Profile (HFP), Advanced Audio Distribution Profile (A2DP) etc.) and the protocol multiplexer settings needed for the phone to connect to the headset using each of them. Each service is identified by a Universally unique identifier (UUID), with official services (Bluetooth profiles) assigned a short form UUID (16 bits rather than the full 128).

#### Radio Frequency Communications

*Radio Frequency Communications* (RFCOMM) is a cable replacement protocol used for generating a virtual serial data stream. RFCOMM provides for binary data transport and emulates EIA-232 (formerly RS-232) control signals over the Bluetooth baseband layer, i.e., it is a serial port emulation.

RFCOMM provides a simple, reliable, data stream to the user, similar to TCP. It is used directly by many telephony related profiles as a carrier for AT commands, as well as being a transport layer for OBEX over Bluetooth.

Many Bluetooth applications use RFCOMM because of its widespread support and publicly available API on most operating systems. Additionally, applications that used a serial port to communicate can be quickly ported to use RFCOMM.

#### Bluetooth Network Encapsulation Protocol

The *Bluetooth Network Encapsulation Protocol* (BNEP) is used for transferring another protocol stack's data via an L2CAP channel. Its main purpose is the transmission of IP packets in the Personal Area Networking Profile. BNEP performs a similar function to SNAP in Wireless LAN.

#### Audio/Video Control Transport Protocol

The *Audio/Video Control Transport Protocol* (AVCTP) is used by the remote control profile to transfer AV/C commands over an L2CAP channel. The music control buttons on a stereo headset use this protocol to control the music player.

#### Audio/Video Distribution Transport Protocol

The *Audio/Video Distribution Transport Protocol* (AVDTP) is used by the advanced audio distribution (A2DP) profile to stream music to stereo headsets over an L2CAP channel intended for video distribution profile in the Bluetooth transmission.

#### Telephony Control Protocol

The *Telephony Control Protocol – Binary* (TCS BIN) is the bit-oriented protocol that defines the call control signaling for the establishment of voice and data calls between Bluetooth devices. Additionally, "TCS BIN defines mobility management procedures for handling groups of Bluetooth TCS devices."

TCS-BIN is only used by the cordless telephony profile, which failed to attract implementers. As such it is only of historical interest.

#### Adopted protocols

Adopted protocols are defined by other standards-making organizations and incorporated into Bluetooth's protocol stack, allowing Bluetooth to code protocols only when necessary. The adopted protocols include:

**Point-to-Point Protocol (PPP)**

Internet standard protocol for transporting

IP datagrams

over a point-to-point link.

**TCP/IP/UDP**

Foundation Protocols for TCP/IP protocol suite

**Object Exchange Protocol (OBEX)**

Session-layer protocol for the exchange of objects, providing a model for object and operation representation

**Wireless Application Environment/Wireless Application Protocol (WAE/WAP)**

WAE specifies an application framework for wireless devices and WAP is an open standard to provide mobile users access to telephony and information services.

### Baseband error correction

Depending on packet type, individual packets may be protected by error correction, either 1/3 rate forward error correction (FEC) or 2/3 rate. In addition, packets with CRC will be retransmitted until acknowledged by automatic repeat request (ARQ).

### Setting up connections

Any Bluetooth device in *discoverable mode* transmits the following information on demand:

- Device name
- Device class
- List of services
- Technical information (for example: device features, manufacturer, Bluetooth specification used, clock offset)

Any device may perform an inquiry to find other devices to connect to, and any device can be configured to respond to such inquiries. However, if the device trying to connect knows the address of the device, it always responds to direct connection requests and transmits the information shown in the list above if requested. Use of a device's services may require pairing or acceptance by its owner, but the connection itself can be initiated by any device and held until it goes out of range. Some devices can be connected to only one device at a time, and connecting to them prevents them from connecting to other devices and appearing in inquiries until they disconnect from the other device.

Every device has a unique 48-bit address. However, these addresses are generally not shown in inquiries. Instead, friendly Bluetooth names are used, which can be set by the user. This name appears when another user scans for devices and in lists of paired devices.

Most cellular phones have the Bluetooth name set to the manufacturer and model of the phone by default. Most cellular phones and laptops show only the Bluetooth names and special programs are required to get additional information about remote devices. This can be confusing as, for example, there could be several cellular phones in range named T610 (see Bluejacking).

### Pairing and bonding

#### Motivation

Many services offered over Bluetooth can expose private data or let a connecting party control the Bluetooth device. Security reasons make it necessary to recognize specific devices, and thus enable control over which devices can connect to a given Bluetooth device. At the same time, it is useful for Bluetooth devices to be able to establish a connection without user intervention (for example, as soon as in range).

To resolve this conflict, Bluetooth uses a process called *bonding*, and a bond is generated through a process called *pairing*. The pairing process is triggered either by a specific request from a user to generate a bond (for example, the user explicitly requests to "Add a Bluetooth device"), or it is triggered automatically when connecting to a service where (for the first time) the identity of a device is required for security purposes. These two cases are referred to as dedicated bonding and general bonding respectively.

Pairing often involves some level of user interaction. This user interaction confirms the identity of the devices. When pairing completes, a bond forms between the two devices, enabling those two devices to connect in the future without repeating the pairing process to confirm device identities. When desired, the user can remove the bonding relationship.

#### Implementation

During pairing, the two devices establish a relationship by creating a shared secret known as a *link key*. If both devices store the same link key, they are said to be *paired* or *bonded*. A device that wants to communicate only with a bonded device can cryptographically authenticate the identity of the other device, ensuring it is the same device it previously paired with. Once a link key is generated, an authenticated ACL link between the devices may be encrypted to protect exchanged data against eavesdropping. Users can delete link keys from either device, which removes the bond between the devices—so it is possible for one device to have a stored link key for a device it is no longer paired with.

Bluetooth services generally require either encryption or authentication and as such require pairing before they let a remote device connect. Some services, such as the Object Push Profile, elect not to explicitly require authentication or encryption so that pairing does not interfere with the user experience associated with the service use-cases.

#### Pairing mechanisms

Pairing mechanisms changed significantly with the introduction of Secure Simple Pairing in Bluetooth v2.1. The following summarizes the pairing mechanisms:

- *Legacy pairing*: This is the only method available in Bluetooth v2.0 and before. Each device must enter a PIN code; pairing is only successful if both devices enter the same PIN code. Any 16-byte UTF-8 string may be used as a PIN code; however, not all devices may be capable of entering all possible PIN codes.
  - *Limited input devices*: The obvious example of this class of device is a Bluetooth Hands-free headset, which generally have few inputs. These devices usually have a *fixed PIN*, for example "0000" or "1234", that are hard-coded into the device.
  - *Numeric input devices*: Mobile phones are classic examples of these devices. They allow a user to enter a numeric value up to 16 digits in length.
  - *Alpha-numeric input devices*: PCs and smartphones are examples of these devices. They allow a user to enter full UTF-8 text as a PIN code. If pairing with a less capable device the user must be aware of the input limitations on the other device; there is no mechanism available for a capable device to determine how it should limit the available input a user may use.
- *Secure Simple Pairing* (SSP): This is required by Bluetooth v2.1, although a Bluetooth v2.1 device may only use legacy pairing to interoperate with a v2.0 or earlier device. Secure Simple Pairing uses a form of public-key cryptography, and some types can help protect against man in the middle, or MITM attacks. SSP has the following authentication mechanisms:
  - *Just works*: As the name implies, this method just works, with no user interaction. However, a device may prompt the user to confirm the pairing process. This method is typically used by headsets with minimal IO capabilities, and is more secure than the fixed PIN mechanism this limited set of devices uses for legacy pairing. This method provides no man-in-the-middle (MITM) protection.
  - *Numeric comparison*: If both devices have a display, and at least one can accept a binary yes/no user input, they may use Numeric Comparison. This method displays a 6-digit numeric code on each device. The user should compare the numbers to ensure they are identical. If the comparison succeeds, the user(s) should confirm pairing on the device(s) that can accept an input. This method provides MITM protection, assuming the user confirms on both devices and actually performs the comparison properly.
  - *Passkey Entry*: This method may be used between a device with a display and a device with numeric keypad entry (such as a keyboard), or two devices with numeric keypad entry. In the first case, the display presents a 6-digit numeric code to the user, who then enters the code on the keypad. In the second case, the user of each device enters the same 6-digit number. Both of these cases provide MITM protection.
  - *Out of band* (OOB): This method uses an external means of communication, such as near-field communication (NFC) to exchange some information used in the pairing process. Pairing is completed using the Bluetooth radio, but requires information from the OOB mechanism. This provides only the level of MITM protection that is present in the OOB mechanism.

SSP is considered simple for the following reasons:

- In most cases, it does not require a user to generate a passkey.
- For use cases not requiring MITM protection, user interaction can be eliminated.
- For *numeric comparison*, MITM protection can be achieved with a simple equality comparison by the user.
- Using OOB with NFC enables pairing when devices simply get close, rather than requiring a lengthy discovery process.

#### Security concerns

Prior to Bluetooth v2.1, encryption is not required and can be turned off at any time. Moreover, the encryption key is only good for approximately 23.5 hours; using a single encryption key longer than this time allows simple XOR attacks to retrieve the encryption key.

- Turning off encryption is required for several normal operations, so it is problematic to detect if encryption is disabled for a valid reason or a security attack.

Bluetooth v2.1 addresses this in the following ways:

- Encryption is required for all non-SDP (Service Discovery Protocol) connections
- A new Encryption Pause and Resume feature is used for all normal operations that require that encryption be disabled. This enables easy identification of normal operation from security attacks.
- The encryption key must be refreshed before it expires.

Link keys may be stored on the device file system, not on the Bluetooth chip itself. Many Bluetooth chip manufacturers let link keys be stored on the device—however, if the device is removable, this means that the link key moves with the device.


## Security

### Overview

Bluetooth implements confidentiality, authentication and key derivation with custom algorithms based on the SAFER+ block cipher. Bluetooth key generation is generally based on a Bluetooth PIN, which must be entered into both devices. This procedure might be modified if one of the devices has a fixed PIN (e.g., for headsets or similar devices with a restricted user interface). During pairing, an initialization key or master key is generated, using the E22 algorithm. The E0 stream cipher is used for encrypting packets, granting confidentiality, and is based on a shared cryptographic secret, namely a previously generated link key or master key. Those keys, used for subsequent encryption of data sent via the air interface, rely on the Bluetooth PIN, which has been entered into one or both devices.

An overview of Bluetooth vulnerabilities exploits was published in 2007 by Andreas Becker.

In September 2008, the National Institute of Standards and Technology (NIST) published a Guide to Bluetooth Security as a reference for organizations. It describes Bluetooth security capabilities and how to secure Bluetooth technologies effectively. While Bluetooth has its benefits, it is susceptible to denial-of-service attacks, eavesdropping, man-in-the-middle attacks, message modification, and resource misappropriation. Users and organizations must evaluate their acceptable level of risk and incorporate security into the lifecycle of Bluetooth devices. To help mitigate risks, included in the NIST document are security checklists with guidelines and recommendations for creating and maintaining secure Bluetooth piconets, headsets, and smart card readers.

Bluetooth v2.1 – finalized in 2007 with consumer devices first appearing in 2009 – makes significant changes to Bluetooth's security, including pairing. See the pairing mechanisms section for more about these changes.

### Bluejacking

Bluejacking is the sending of either a picture or a message from one user to an unsuspecting user through Bluetooth wireless technology. Common applications include short messages, e.g., "You've just been bluejacked!" Bluejacking does not involve the removal or alteration of any data from the device.

Some form of DoS is also possible, even in modern devices, by sending unsolicited pairing requests in rapid succession; this becomes disruptive because most systems display a full screen notification for every connection request, interrupting every other activity, especially on less powerful devices.

### History of security concerns

#### 2001–2004

In 2001, Jakobsson and Wetzel from Bell Laboratories discovered flaws in the Bluetooth pairing protocol and also pointed to vulnerabilities in the encryption scheme. In 2003, Ben and Adam Laurie from A.L. Digital Ltd. discovered that serious flaws in some poor implementations of Bluetooth security may lead to disclosure of personal data. In a subsequent experiment, Martin Herfurt from the trifinite.group was able to do a field-trial at the CeBIT fairgrounds, showing the importance of the problem to the world. A new attack called BlueBug was used for this experiment. In 2004 the first purported virus using Bluetooth to spread itself among mobile phones appeared on the Symbian OS. The virus was first described by Kaspersky Lab and requires users to confirm the installation of unknown software before it can propagate. The virus was written as a proof-of-concept by a group of virus writers known as "29A" and sent to anti-virus groups. Thus, it should be regarded as a potential (but not real) security threat to Bluetooth technology or Symbian OS since the virus has never spread outside of this system. In August 2004, a world-record-setting experiment (see also Bluetooth sniping) showed that the range of Class 2 Bluetooth radios could be extended to 1.78 km (1.11 mi) with directional antennas and signal amplifiers. This poses a potential security threat because it enables attackers to access vulnerable Bluetooth devices from a distance beyond expectation. The attacker must also be able to receive information from the victim to set up a connection. No attack can be made against a Bluetooth device unless the attacker knows its Bluetooth address and which channels to transmit on, although these can be deduced within a few minutes if the device is in use.

#### 2005

In January 2005, a mobile malware worm known as Lasco surfaced. The worm began targeting mobile phones using Symbian OS (Series 60 platform) using Bluetooth enabled devices to replicate itself and spread to other devices. The worm is self-installing and begins once the mobile user approves the transfer of the file (Velasco.sis) from another device. Once installed, the worm begins looking for other Bluetooth enabled devices to infect. Additionally, the worm infects other .SIS files on the device, allowing replication to another device through the use of removable media (Secure Digital, CompactFlash, etc.). The worm can render the mobile device unstable.

In April 2005, University of Cambridge security researchers published results of their actual implementation of passive attacks against the PIN-based pairing between commercial Bluetooth devices. They confirmed that attacks are practicably fast, and the Bluetooth symmetric key establishment method is vulnerable. To rectify this vulnerability, they designed an implementation that showed that stronger, asymmetric key establishment is feasible for certain classes of devices, such as mobile phones.

In June 2005, Yaniv Shaked and Avishai Wool published a paper describing both passive and active methods for obtaining the PIN for a Bluetooth link. The passive attack allows a suitably equipped attacker to eavesdrop on communications and spoof if the attacker was present at the time of initial pairing. The active method makes use of a specially constructed message that must be inserted at a specific point in the protocol, to make the master and slave repeat the pairing process. After that, the first method can be used to crack the PIN. This attack's major weakness is that it requires the user of the devices under attack to re-enter the PIN during the attack when the device prompts them to. Also, this active attack probably requires custom hardware, since most commercially available Bluetooth devices are not capable of the timing necessary.

In August 2005, police in Cambridgeshire, England, issued warnings about thieves using Bluetooth enabled phones to track other devices left in cars. Police are advising users to ensure that any mobile networking connections are de-activated if laptops and other devices are left in this way.

#### 2006

In April 2006, researchers from Secure Network and F-Secure published a report that warns of the large number of devices left in a visible state, and issued statistics on the spread of various Bluetooth services and the ease of spread of an eventual Bluetooth worm.

In October 2006, at the Luxembourgish Hack.lu Security Conference, Kevin Finistere and Thierry Zoller demonstrated and released a remote root shell via Bluetooth on Mac OS X v10.3.9 and v10.4. They also demonstrated the first Bluetooth PIN and Linkkeys cracker, which is based on the research of Wool and Shaked.

#### 2017

In April 2017, security researchers at Armis discovered multiple exploits in the Bluetooth software in various platforms, including Microsoft Windows, Linux, Apple iOS, and Google Android. These vulnerabilities are collectively called "BlueBorne". The exploits allow an attacker to connect to devices or systems without authentication and can give them "virtually full control over the device". Armis contacted Google, Microsoft, Apple, Samsung and Linux developers allowing them to patch their software before the coordinated announcement of the vulnerabilities on 12 September 2017.

#### 2018

In July 2018, Lior Neumann and Eli Biham, researchers at the Technion – Israel Institute of Technology identified a security vulnerability in the latest Bluetooth pairing procedures: Secure Simple Pairing and LE Secure Connections.

Also, in October 2018, Karim Lounis, a network security researcher at Queen's University, identified a security vulnerability, called CDV (Connection Dumping Vulnerability), on various Bluetooth devices that allows an attacker to tear down an existing Bluetooth connection and cause the deauthentication and disconnection of the involved devices. The researcher demonstrated the attack on various devices of different categories and from different manufacturers.

#### 2019

In August 2019, security researchers at the Singapore University of Technology and Design, Helmholtz Center for Information Security, and University of Oxford discovered a vulnerability, called KNOB (Key Negotiation of Bluetooth) in the key negotiation that would "brute force the negotiated encryption keys, decrypt the eavesdropped ciphertext, and inject valid encrypted messages (in real-time)". Google released an Android security patch on 5 August 2019, which removed this vulnerability.

#### 2023

In November 2023, researchers from Eurecom revealed a new class of attacks known as BLUFFS (Bluetooth Low Energy Forward and Future Secrecy Attacks). These 6 new attacks expand on and work in conjunction with the previously known KNOB and BIAS (Bluetooth Impersonation AttackS) attacks. While the previous KNOB and BIAS attacks allowed an attacker to decrypt and spoof Bluetooth packets within a session, BLUFFS extends this capability to all sessions generated by a device (including past, present, and future). All devices running Bluetooth versions 4.2 up to and including 5.4 are affected.


## Health concerns

Bluetooth uses the radio frequency spectrum in the 2.402 GHz to 2.480 GHz range, which is non-ionizing radiation, of similar bandwidth to that used by wireless and mobile phones. No specific harm has been demonstrated, even though wireless transmission has been included by IARC in the possible carcinogen list. Maximum power output from a Bluetooth radio is 100 mW for Class 1, 2.5 mW for Class 2, and 1 mW for Class 3 devices. Even the maximum power output of Class 1 is a lower level than the lowest-powered mobile phones. UMTS and W-CDMA output 250 mW, GSM1800/1900 outputs 1000 mW, and GSM850/900 outputs 2000 mW.


## Award programs

The Bluetooth Innovation World Cup, a marketing initiative of the Bluetooth Special Interest Group (SIG), was an international competition that encouraged the development of innovations for applications leveraging Bluetooth technology in sports, fitness and health care products. The competition aimed to stimulate new markets.

The Bluetooth Innovation World Cup morphed into the Bluetooth Breakthrough Awards in 2013. Bluetooth SIG subsequently launched the Imagine Blue Award in 2016 at Bluetooth World. The Bluetooth Breakthrough Awards program highlights the most innovative products and applications available today, prototypes coming soon, and student-led projects in the making.

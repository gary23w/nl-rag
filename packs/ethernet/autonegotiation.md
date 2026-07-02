---
title: "Autonegotiation"
source: https://en.wikipedia.org/wiki/Autonegotiation
domain: ethernet
license: CC-BY-SA-4.0
tags: ethernet, ethernet frame, csma/cd, medium access control
fetched: 2026-07-02
---

# Autonegotiation

**Autonegotiation** is a signaling mechanism and procedure used by Ethernet over twisted pair by which two connected devices choose common transmission parameters, such as speed, duplex mode, and flow control. In this process, the connected devices first share their capabilities regarding these parameters and then choose the highest-performance transmission mode they both support.

Autonegotiation for twisted pair is defined in clause 28 of IEEE 802.3. and was originally an optional component in the Fast Ethernet standard. It is backwards compatible with the **normal link pulses** (**NLP**) used by 10BASE-T. The protocol was significantly extended in the Gigabit Ethernet standard, and is mandatory for 1000BASE-T gigabit Ethernet over twisted pair.

In the OSI model, autonegotiation resides in the physical layer.

## Standardization and interoperability

In 1995, the Fast Ethernet standard was released. Because this introduced a new speed option for the same wires, it included a means for connected network adapters to negotiate the best possible shared mode of operation. The autonegotiation protocol included in IEEE 802.3 clause 28 was developed from a patented technology by National Semiconductor known as **NWay**. The company gave a letter of assurance for anyone to use their system for a one time license fee. Another company has since bought the rights to that patent.

The first version of the autonegotiation specification, in the 1995 IEEE 802.3u Fast Ethernet standard, was implemented differently by different manufacturers leading to interoperability issues. These problems led many network administrators to manually set the speed and duplex mode of each network interface. However, the use of manual configurations may lead to duplex mismatches. These can be difficult to diagnose because the network is nominally working. Simple network testing utilities such as ping may report a valid connection. However, network performance will be significantly impacted by transmission aborts and subsequent Ethernet frame drops that result from a duplex mismatch. When a duplex mismatch is occurring, the side of the connection that is using half-duplex will report late collisions, while the side using full-duplex will report FCS errors.

The autonegotiation specification was improved in the 1998 release of IEEE 802.3. This was followed by the release of the IEEE 802.3ab Gigabit Ethernet standard in 1999 which specified mandatory autonegotiation for 1000BASE-T. Autonegotiation is also mandatory for 1000BASE-TX and 10GBASE-T implementations. Currently, most network equipment manufacturers recommend using autonegotiation on all access ports and enable it as a factory default setting.

## Function

Autonegotiation can be used by devices that are capable of more than one transmission rate, different duplex modes (half duplex and full duplex), and different transmission standards at the same speed (though in practice only one standard at each speed is widely supported).

During autonegotiation, each device declares its *technology abilities*, that is, its possible modes of operation. The best common mode is chosen, with higher speed preferred over lower, and full duplex preferred over half duplex at the same speed.

Parallel detection is used when a device that is capable of autonegotiation is connected to one that is not. This happens if a device does not support autonegotiation or autonegotiation is disabled on a device. In this condition, the device that is capable of autonegotiation can determine and match speed with the other device. This procedure cannot determine duplex capability, so half duplex is always assumed.

Other than speed and duplex mode, autonegotiation is used to communicate the master-slave parameters for gigabit Ethernet.

## Priority

Upon receipt of the technology abilities of the other device, both devices decide the best possible mode of operation supported by both devices. Among the modes that are supported by both devices, each device chooses the one that is highest priority. The priority among modes is as follows:

1. 40GBASE-T full duplex
2. 25GBASE-T full duplex
3. 10GBASE-T full duplex
4. 5GBASE-T full duplex
5. 2.5GBASE-T full duplex
6. 1000BASE-T full duplex
7. 1000BASE-T half duplex
8. 100BASE-T2 full duplex
9. 100BASE-TX full duplex
10. 100BASE-T2 half duplex
11. 100BASE-T4 half duplex
12. 100BASE-TX half duplex
13. 10BASE-T full duplex
14. 10BASE-T half duplex

## Electrical signals

Autonegotiation is based on pulses similar to those used by 10BASE-T devices to detect the presence of a connection to another device. These *link integrity test* (LIT) pulses are sent by Ethernet devices when they are not sending or receiving any frames. They are unipolar positive-only electrical pulses of a nominal duration of 100 ns, with a maximum pulse width of 200 ns, generated at a 16 ms time interval with a timing variation tolerance of 8 ms. A device detects the failure of a link if neither a frame, nor two of the LIT pulses, is received for 50-150 ms. For this scheme to work, devices must send LIT pulses regardless of receiving any. In the autonegotiation specification, these pulses are called **normal link pulses** (NLP).

NLPs used by autonegotiation are still unipolar, positive-only, and with a nominal duration of 100 ns; but each LIT is replaced by a pulse burst consisting of 17 to 33 pulses sent 125 μs apart. Each pulse burst is called a **fast link pulse** (FLP) burst. The time interval between the start of each FLP burst is the same 16 ms as between NLPs.

The FLP burst consists of 17 NLP at a 125 μs time interval with a tolerance of 14 μs. Between each pair of two consecutive NLPs (i.e. at 62.5 μs after the first NLP of the pulse pair), an additional positive pulse may be present. The presence of this additional pulse indicates a logical 1, its absence a logical 0. As a result, every FLP contains a 16-bit data word. This data word is called a *link code word* (LCW). The bits of the LCW are numbered from 0 to 15, where bit 0 corresponds to the first possible pulse in time and bit 15 to the last.

## The base link code word

Every fast link pulse burst transmits 16 bits of data known as a link code word. The first such word is known as a *base link code word*, and its bits are used as follows:

- 0–4: selector field – indicates which standard is used between IEEE 802.3 and IEEE 802.9
- 5–12: technology ability field – a sequence of bits that encode the possible modes of operations among the 100BASE-T and 10BASE-T modes (see below)
- 13: remote fault – set to one when the device is detecting a link failure
- 14: acknowledgement – the device sets this to one to indicate the correct reception of the base link code word from the other party; this is detected by the reception of at least three identical base code words. Upon receiving these three identical copies, the device sends a link code word with the acknowledge bit set to one from six times to eight times.
- 15: next page – used to indicate the intention of sending other link code words after the base link code word

The technology ability field is composed of eight bits. For IEEE 802.3, these are as follows:

- bit 0: device supports 10BASE-T
- bit 1: device supports 10BASE-T in full duplex
- bit 2: device supports 100BASE-TX
- bit 3: device supports 100BASE-TX in full duplex
- bit 4: device supports 100BASE-T4
- bit 5: device supports pause frame
- bit 6: device supports asymmetric pause for full duplex
- bit 7: reserved

The link code words are also called *pages*. The base link code word is therefore called a base page. The next page bit of the base page is 1 when the device intends to send other pages, which can be used to communicate other abilities. These additional pages are sent only if both devices have sent base pages with a next page bit set to 1. The additional pages are still encoded as link code words (using 17 clock pulses and up to 16-bit pulses).

## Message and unformatted next page

The base page is sufficient for devices to advertise which ones among the 10BASE-T, 100BASE-TX and 100BASE-T4 modes they support. For gigabit Ethernet, two other pages are required. These pages are sent if both devices have sent base pages with a next page bit set to one.

The additional pages are of two kinds: *message pages* and *unformatted pages*. These pages are still 16-bit words encoded as pulses in the same way as the base page. Their first eleven bits are data, while their second-to-last bit indicates whether the page is a message page or an unformatted page. The last bit of each page indicates the presence of an additional page.

The 1000BASE-T supported modes and master-slave data (which is used to decide which of the two devices acts as the master, and which one acts as the slave) are sent using a single message page, followed by a single unformatted page. The message page contains:

- half duplex capability
- whether the device is single port or multiport
- whether master/slave is manually configured or not
- whether the device is manually configured as master or slave

The unformatted page contains a 10-bit word, called a master-slave seed value.

## Duplex mismatch

A duplex mismatch occurs when two connected devices are configured in different duplex modes. This may happen, for example, if one is configured for autonegotiation while the other one has a fixed mode of operation that is full duplex (no autonegotiation). In such conditions, the autonegotiation device correctly detects the speed of operation but is unable to correctly detect the duplex mode. As a result, it sets the correct speed but assumes half-duplex mode.

When a device is operating in full duplex while the other one operates in half duplex, the connection works reliably only at a very low throughput. A full-duplex device may transmit data while it is receiving. However, if the half-duplex device receives data while it is sending, it senses a collision and aborts transmission and then attempts to resend the frame. The full-duplex device will report frame check sequence (FCS) errors on the aborted transmissions. Depending on timing, the half-duplex device may sense a late collision, which it will interpret as a hard error rather than a normal consequence of CSMA/CD and may not attempt to resend the frame. The full-duplex device does not detect any collision and assumes the frame was received without error. This combination of (late) collisions reported at the half-duplex end and FCS errors reported by the full-duplex end are indicators that a duplex mismatch is present.

## Patents

Autonegotiation is covered by the US patents U.S. patent 5,617,418, U.S. patent 5,687,174, E U.S. patent RE39,405 E, E U.S. patent RE39,116 E, US application 971018  (filed 1992-11-02), US application 146729  (filed 1993-11-01), US application 430143  (filed 1995-04-26); European Patent Applications SN 93308568.0 (DE, FR, GB, IT, NL); Korean Patent No. 286791; Taiwanese Patent No. 098359; Japanese Patent No. 3705610; Japanese Patent 4234. Applications SN H5-274147; Korean Patent Applications SN 22995/93; Taiwanese Patent Applications SN 83104531.

## Auto-Negotiation for single-pair Ethernet

Due to its nature, single-pair Ethernet has its own, optional variant of Auto-Negotiation. It uses differential Manchester encoding (DME) pages to negotiate capabilities in a half-duplex manner. Two different signaling speeds are used: 10/5/2.5GBASE-T1, 1000BASE-T1, 100BASE-T1, and 10BASE-T1S support high-speed mode (HSM) at 16.667 Mbit/s and optionally low-speed mode (LSM) at 625 kbit/s, while 10BASE-T1L supports LSM and optionally HSM.

The selection priority for negotiated modes are:

1. 10GBASE-T1
2. 5GBASE-T1
3. 2.5GBASE-T1
4. 1000BASE-T1
5. 100BASE-T1
6. 10BASE-T1S full duplex
7. 10BASE-T1S half duplex
8. 10BASE-T1L

---
title: "GPON"
source: https://en.wikipedia.org/wiki/Gigabit_Passive_Optical_Network
domain: gpon-deep
license: CC-BY-SA-4.0
tags: gigabit pon, passive optical network, optical line termination, fiber access
fetched: 2026-07-02
---

# GPON

(Redirected from

Gigabit Passive Optical Network

)

ITU-T **G.984** is the series of standards that define the architecture and operation of gigabit-per-second–capable passive optical network (**GPON**). It is commonly used to implement the link to the customer (the *last kilometre*, or *last mile*) of fiber-to-the-premises (FTTP) services, using a point-to-multipoint design. GPON supporting a shared bandwidth of downstream data rates of up to 2.4 Gbit/s and normally upstream rates of up to 1.2 Gbit/s.

## Passive optical network

GPON uses passive optical network (PON) is a fiber-optic access architecture in which a single optical fiber from a central location is shared by multiple end users through one or more passive optical splitters in series (cascaded). Unlike traditional point-to-point fiber connections, PON systems distribute optical signals from an optical line terminal (OLT) to many optical network units (ONUs) or optical network terminals (ONTs) without requiring active electronic equipment in the distribution network. The absence of powered components between the central location and subscribers reduces infrastructure costs, simplifies maintenance, and increases reliability.

In a PON architecture, downstream data is broadcast from the optical line terminal (OLT) to all connected optical network units (ONUs), while upstream data is coordinated using time-division multiple access to prevent signal collisions. Passive splitters divide optical signals across multiple fibers, typically serving 16 to 64 subscribers from a single fiber feeder.

## Features

The standard specifies transmission convergence layer, physical layer requirements, management protocols, and service encapsulation for high-speed fiber access networks.

GPON puts requirements on the optical medium and the hardware used to access it, and defines the manner in which Ethernet frames are converted to an optical signal, as well as the parameters of that signal. The bandwidth of the single connection between the optical line termination (OLT) and the optical network terminals (ONTs) is 2.4 Gbit/s down, 1.2 Gbit/s up, or rarely symmetric 2.4 Gbit/s, shared between up to 128 ONTs using a time-division multiple access (TDMA) protocol, which the standard defines.

ITU-T G.984 specifies:

- Use of Non-return-to-zero Line coding
- Use of forward error correction (Reed–Solomon), results in an increased link budget by approximately 3-4 dB.
- Encryption (AES)
- Protocol for line control (OMCI) which includes authentication (GPON serial number and/or PLOAM password).
- For single fiber design, the use of Wavelength-division multiplexing
  - Downstream 1490nm-TX +/- 10nm
  - Upstream 1310nm-RX +/- 10nm
- Timing and clock synchronization
- Power-levelling mechanism
- Dynamic bandwidth allocation

Unlike the EPON standard, which has a much simpler topology, GPON encapsulates Ethernet packets into virtual GPON encapsulation method (GEM) ports, TCONT queues and VLANIDs via OMCI.

The exact kind of fiber cable and connectors to use is undefined but is broadly using OS2 cable with SC/APC connectors.

### Timing and clock traceability requirements

GPON systems require precise timing and clock synchronization to ensure collision-avoidance in upstream transmission in the time-division multiple access (TDMA) from multiple optical network units (ONUs).

The optical line terminal (OLT) provides the primary timing reference for the network, distributing timing information through the downstream signal (every 125µs). Optical network units (ONUs) recover the clock from the received downstream data stream and use it to align their upstream transmissions according to time slots (every 125µs) assigned by the dynamic bandwidth allocation mechanism defined in the transmission convergence layer.

### Attenuation class

Attenuation classes in GPON define the allowable optical loss budget between the OLT and the ONU, ensuring reliable operation over a passive optical distribution network with varying fiber lengths and splitter configurations.

This is similarly to Ethernet 1000BASE-BX10/20/40/80/120/160, which typically specifies a fixed optical reach using separate upstream and downstream wavelengths (often referred to as Base-BX-U and Base-BX-D), GPON attenuation classes define broader link budgets to accommodate passive optical splitters and shared fiber infrastructure, resulting in significantly higher allowable optical loss than typical point-to-point Ethernet fiber links.

| Attenuation class | Attenuation range, dB | Max physical reach, km | Max differential fiber distance, km | Standard |
|---|---|---|---|---|
| Class A | 5-20 | 20 | 20 | G.984.2 |
| Class B | 10-25 | 20 | 20 | G.984.2 |
| Class B+ | 13-28 | 40 | 40 | G.984.7 |
| Class C | 15-30 | 40 | 40 | G.984.7 |
| Class C+ | 17-32 | 60 | 40 | G.984.7 |
| Class D | 20-35 | 60 | 60 | G.984.2 |

### Power-levelling mechanism

The power-levelling mechanism in GPON is used to control the optical transmit power of the ONUs in the upstream direction. In a PON, multiple ONUs share the same optical distribution network and transmit bursts of upstream data toward the central OLT. Because ONUs may be located at different distances from the OLT and have different optical path losses, the received optical power at the OLT can vary significantly. The power-levelling mechanism allows the ONUs transmitter to adjust its launched optical power to compensate for these variations, ensuring that upstream bursts arrive at the OLT within an acceptable dynamic range.

The mechanism operates by defining different ONUs transmit power levels and corresponding detection thresholds at the central OLT During operation, the central OLT measures the received optical power from each ONU and determines whether the power level falls within the desired operating window. If necessary, the OLT sends PLOAM *Change_power_level* message, the ONU adjusts its transmit power to maintain stable reception and prevent receiver overload or insufficient signal levels.

In contrast to ADSL technology, which deteriorates as the distance between the central office and the household rises, with severe signal loss beyond 3km, all customers may enjoy high-speed network access within the 16km range of a fiber central office.

## The standards

The first version of GPON was ratified in 2003. Since then, it has been expanded upon and revised several times. Work on the standard continues. As of July 2018, G.984.5 is currently being revised. The most recent version comprises seven parts:

- G.984.1 : General characteristics, 2008, with amendment 1 (2009) and 2 (2012)
- G.984.2 : Physical Media Dependent (PMD) layer specification, 2003, with amendment 1 (2006) and 2 (2008)
- G.984.3 : Transmission convergence layer specification, 2008, with amendments 1 (2009), 2 (2009), 3 (2012) and erratum 1 (2010)
- G.984.4 : ONT management and control interface (OMCI) specification, 2008, with amendments 1 (2009), 2 (2009), 3 (2010), erratum 1 (2009), corrigendum 1 (2010), and an implementer's guide (2009)
- G.984.5 : Enhancement Band, 2014, Coexistence with future WDM PON technology on the same medium
- G.984.6 : Reach extension (2008), with amendments 1 (2009) and 2 (2012)
- G.984.7 : Long reach (2010)

The GPON OMCI recommendation G.984.4 draws on G.983.2, which defines the BPON management model. However, G.984.4 removed all references to ATM. G.988 is a stand-alone OMCI recommendation and supersedes G.984.4 except for GPON specifics that are not defined in G.988. Future work on the PON management model is expected to appear only in the GPON space.

## Security

Security issues in the G.984 standard series include the possibility of eavesdropping on upstream traffic, replay attacks, PLOAM messages that are not integrity protected and denial of service to other subscribers on the same link.

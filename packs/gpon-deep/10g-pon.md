---
title: "10G-PON"
source: https://en.wikipedia.org/wiki/10G-PON
domain: gpon-deep
license: CC-BY-SA-4.0
tags: gigabit pon, passive optical network, optical line termination, fiber access
fetched: 2026-07-02
---

# 10G-PON

**10G-PON** (also known as **XG-PON** or **G.987**) is a 2010 computer networking standard for data links, capable of delivering shared Internet access rates up to 10 Gbit/s (gigabits per second) over optical fibre. This is the ITU-T's next-generation standard following on from GPON or gigabit-capable PON. Optical fibre is shared by many subscribers in a network known as FTTx in a way that centralises most of the telecommunications equipment, often displacing copper phone lines that connect premises to the phone exchange. Passive optical network (PON) architecture has become a cost-effective way to meet performance demands in access networks, and sometimes also in large optical local networks for *fibre-to-the-desk*.

Passive optical networks are used for the *fibre-to-the-home* or *fibre-to-the-premises* last mile with splitters that connect each central transmitter to many subscribers. The 10 Gbit/s shared capacity is the downstream speed broadcast to all users connected to the same PON, and the 2.5 Gbit/s upstream speed uses multiplexing techniques to prevent data frames from interfering with each other. Each user has a network device that converts between the optical signals and the signals used in building wiring, such as Ethernet and wired analogue plain old telephone service. XGS-PON is a related technology that can deliver upstream and downstream (symmetrical) speeds of up to 10 Gbit/s (gigabits per second), first approved in 2016 as G.9807.1. XGS-PON uses time division multiplexing (TDM) and time division multiple access (TDMA).

## Standards

ITU-T G.987 is the standard for 10G-PON.

Asymmetric 10G-PON is specified as XG-PON1: 10 Gbit/s downstream and 2.5 Gbit/s upstream (nominal line rate of 9.95328 Gbit/s downstream and 2.48832 Gbit/s upstream).

Symmetric 10G-PON is also proposed as XG-PON2 with 10 Gbit/s upstream, but would require more expensive burst-mode lasers on optical network terminals (ONTs) to deliver the upstream transmission speed. Another symmetric 10G-PON standard is XGS-PON (ITU-T G.9807.1, approved 2016-06-22).

Framing is "G-PON like" but uses different wavelengths from G-PON (using a WDM to separate them) so that G-PON subscribers can be upgraded to 10G-PON incrementally while GPON users continue on the original optical line terminal (OLT). The G-PON standard is G.984. This compares to the IEEE 802.3av standard for 10G-EPON based on Ethernet, which has standardised upstream rates of both 1 Gbit/s and 10 Gbit/s. The 10 gigabit PON wavelengths (1577 nm down / 1270 nm up) differ from GPON and EPON (1490 nm down /1310 nm up), allowing it to coexist on the same fibre with either of the gigabit PONs.

### G.987

ITU-T Recommendation G.987 is a family that defines this access network standard (referred to as XG-PON). It comprises four recommendations:

- **G.987**: 10-Gigabit-capable passive optical network (XG-PON) systems: Definitions, Abbreviations, and Acronyms, 2010.
- **G.987.1**: General requirements of 10G-PON systems *(approved 2010-01-13)*. Includes examples of services, user network interfaces (UNIs) and service node interfaces (SNIs), as well as the principal deployment configurations that are requested by network operators.
- **G.987.2**: Physical media dependent (PMD) layer specification *(approved 2010-01-13, updated 2010-10-07)*. Describes a flexible optical fibre access network representing an evolutionary development from G.984.2, asymmetric only in the current version.
- **G.987.3**: Transmission convergence (TC) specifications *(approved 2010-10-07)*.

### G.988

There is also a companion ITU-T standard defining a management and control interface for administering optical network units, referred to by the G.987 recommendations.

- **G.988**: ONU management and control interface (OMCI) specification *(approved 2010-10-07)*.

## ONU equipment

The optical network unit (ONU) supplies network services from the PON to customer premises, connecting customer-premises equipment such as a home gateway or office firewall. An optical network terminal (ONT) is an ONU that functions as a demarcation point servicing a single subscriber; e.g., a dwelling or office. ONU devices supply Ethernet and possibly other services to the users, either directly (by bridging) or through a gateway device such as a residential gateway, firewall, and/or router, POTS, CATV signals to buildings wired for RF video, and some may even be compatible with the emerging G.hn home networking standard.

The ONU receives the downstream data from the Internet or private networks, and also uses time slots allocated by the OLT to send the upstream traffic in burst-mode. TDMA time slots prevent collisions with upstream traffic from other users sharing the same physical PON.

Fibre-to-the-cell site is another emerging application, but has extra synchronisation requirements. A specialised cellular backhaul unit (CBU) can provide PON access for cellular networks.

## OLT and access nodes

The OLT (optical line terminal) connects the PON to aggregated backhaul uplinks, allocates time slots for ONUs and ONTs to transmit upstream data, and transmits shared downstream data in broadcast-mode over the PON to users. Since 10GPON is designed to coexist with GPON devices, migration to a 10GPON capability could be done by upgrading the OLT and then migrating individual ONUs as needed.

Normally the OLT is on a card that slots into an OLT chassis at the central office (CO), which uses special uplink cards for Ethernet backhaul to the telecommunications provider's network and internet. Uplink cards on access equipment will likely use multiple Ethernet interfaces, although it remains to be seen what uplink speeds manufacturers will offer to support 10GPON access. Locating OLTs in outside plant cabinets may be an option for reach extension as a way to minimise the number of central offices covering low population density areas.

ITU and IEEE are planning for convergence of their specifications at the physical layer in 10G that would allow for the shared chips, optics and hardware platforms, thus driving cost reductions for hardware manufacturers.

## Optical distribution network

PON optical distribution networks use single-mode optical fibre in the outside plant, optical splitters and optical distribution frames, duplexed so that both upstream and downstream share the same fibre on separate wavelengths. 10G-PON is no exception with reach similar to previous standards but supporting a higher split ratio of 128 users per PON, or more using reach extenders/amplifiers. Optical splitters creating a point to multipoint topology are also the same technology as those used by other PON systems. This means any PON network should be upgradable by changing the ONT and OLT terminals at each end, with no change to the fibre itself unless different connectors are chosen.

"An Optical Distribution Network (ODN) being installed today will likely need to support four or more generations of PON over its expected 30–40 year life... The fibre should enable maximum flexibility to support any potential new PON technology, be protected with proven, reliable cabling making it easy to install and reliable, and be joined by advanced, low labor and low loss connectivity. The cost of the ODN materials (fibre, cable, and connectivity) at only about 8% comprises a surprisingly small portion of the total network cost."

In an effort to extend the reach with support for 128 subscribers, the standard supports a range of optical budgets from 29 dB to 31 dB. A draft update to the standard is expected to further extend this to 33 dB and 35 dB budget classifications. A PON with a 35 dB optical budget could span 25 km or more and be shared among 128 subscribers. XGS-PON also supports split ratios of up to 1:128.

Some ONTs can receive a broad range of optical spectrum from 1480 nm to 1580 nm, so making the 10G-PON downstream signal visible to G-PON receivers. As a result, ONTs must block the unwanted downstream signals with a wavelength blocking filter (WBF), a small passive optical device.

## Field trials

- In October 2010, Portugal Telecom reported a successful field trial of 10G-PON, transmitting 3D-TV content using XG-PON1 capabilities.
- Verizon also successfully completed a field trial of the pre-standard XG-PON2 (synchronous 10G-PON) capable of delivering a 10 Gbit/s broadband connection both downstream and upstream. In October 2010, at a Verizon customer's business in Taunton, Mass., the XG-PON2 trial used the same optical fibre that provides that business with its existing FiOS network connection and services.
- BT in the UK is providing a trial 10-Gbit/s broadband service to a business customer in Cornwall using XGPON technology, it announced on 23rd Nov 2012.
- Chorus in New Zealand is providing a trial 10-Gbit/s broadband service to customers using XGS-PON technology. It was announced on 18th Nov 2019.
- OpenFiber (wholesale-only FTTH carrier in Italy) has successfully trialled a 10 Gbit service with coexisting GPON on the same fiber, using XGS-PON technology from ZTE, on March 14, 2019 in collaboration with ISP Fibra.city.
  - Announced the commercial availability on its OpenStream product (bitstream access) on March 26, 2021.
- Telecom Italia is starting a trial on three exchanges in Italy using XGS-PON equipment from Nokia, both to its retail customers and to its wholesale clients.
- In mid-2025, Octotel in South Africa started trialing multi-gigabit connections using XGS-PON technology.

## Home Internet service providers

- Italy – TIM; Convergenze
- Netherlands – DELTA, KPN
- Japan – So-net
- Malaysia – Time
- Hong Kong – PCCW-HKT
- Singapore – Singtel, M1
- Switzerland – Swisscom, Salt Fiber, Sunrise, Quickline
- Poland – Inea
- New Zealand – Chorus
- Serbia – Orion Telekom
- Slovakia – Antik Telecom
- Spain – Digi Spain
- Romania – Digi Romania, FiberX
- Sri Lanka – SLT
- United Kingdom – Virgin Media, CityFibre, toob, G.Network, Community Fibre, YouFibre, Fibrus, FullFibre
- Croatia – Telemach
- United States – AT&T, Cox Communications, Frontier Communications, Lumen (also known as CenturyLink and Quantum Fiber), Sonic, Glo Fiber, Summit Broadband, Ziply Fiber, Google Fiber
- Canada – Bell, Rogers, Telus, TBayTel, FibreTel, Beanfield, TelMAX Inc., TelKel, TekSavvy Solutions, Hay Communications
- Bulgaria - Vivacom
- Ireland – SIRO
- France – Bouygues Télécom, SFR, Orange

## Commercial Internet service providers

- Spain – Orange Spain
- Singapore – M1
- France – Sfr, Netalis (France)
- Monaco – Monaco Telecom
- New Zealand – Chorus
- Serbia – Orion Telekom
- Slovakia – Antik Telecom
- Croatia – Telemach
- Philippines – Converge ICT
- United Kingdom – Zzoomm

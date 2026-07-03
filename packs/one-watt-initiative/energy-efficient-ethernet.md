---
title: "Energy-Efficient Ethernet"
source: https://en.wikipedia.org/wiki/Energy-Efficient_Ethernet
domain: one-watt-initiative
license: CC-BY-SA-4.0
tags: one watt initiative
fetched: 2026-07-03
---

# Energy-Efficient Ethernet

In computer networking, **Energy-Efficient Ethernet** (**EEE**) is a set of enhancements to twisted-pair, twinaxial, backplane, and optical fiber Ethernet physical-layer variants that reduce power consumption during periods of low data activity. The intention is to reduce power consumption by at least half, while retaining full compatibility with existing equipment.

The Institute of Electrical and Electronics Engineers (IEEE), through the **IEEE 802.3az** task force, developed the standard. The first study group had its call for interest in November 2006, and the official standards task force was authorized in May 2007. The IEEE ratified the final standard in September 2010. Some companies introduced technology to reduce the power required for Ethernet before the standard was ratified, using the name **Green Ethernet**.

Some energy-efficient switch integrated circuits were developed before the IEEE 802.3az Energy-Efficient Ethernet standard was finalized.

## Potential savings

In 2005, all the network interface controllers in the United States (in computers, switches, and routers) used an estimated 5.3 terawatt-hours of electricity. According to a researcher at the Lawrence Berkeley Laboratory, Energy-Efficient Ethernet can potentially save an estimated US$450 million a year in energy costs in the US. Most of the savings would come from homes (US$200 million) and offices (US$170 million), and the remaining US$80 million from data centers.

## Concepts

The power reduction is accomplished in a few ways. In Fast Ethernet and faster links, constant and significant energy is used by the physical layer as transmitters are active regardless of whether data is being sent. If they could be put into sleep mode when no data is being sent, that energy could be saved. When the controlling software or firmware decides that no data needs to be sent, it can issue a low-power idle (LPI) request to the Ethernet controller physical layer PHY. The PHY will then send LPI symbols for a specified time onto the link, and then disable its transmitter. Refresh signals are sent periodically to maintain link signaling integrity. When there is data to transmit, a normal IDLE signal is sent for a predetermined period of time. The data link is considered to be always operational, as the receive signal circuit remains active even when the transmit path is in sleep mode.

## Green Ethernet

Green Ethernet technology was a superset of the 802.3az standard. In addition to the link load power savings of Energy-Efficient Ethernet, Green Ethernet works in one of two ways. First, it detects link status, allowing each port on the switch to power down into a standby mode when a connected device, such as a computer, is not active. Second, it detects cable length and adjusts the power used for transmission accordingly. Standard switches provide enough power to send a signal up to 100 meters (330 ft). However, this is often unnecessary in the SOHO environment, where 5 to 10 meters (16 to 33 ft) of cabling are typical between rooms. Moreover, small data centers can also benefit from this approach since the majority of cabling is confined to a single room with a few meters of cabling among servers and switches. In addition to the pure power-saving benefits of Green Ethernet, backing off the transmit power on shorter cable runs reduces alien crosstalk and improves the overall performance of the cabling system.

Green Ethernet also encompasses the use of more efficient circuitry in Ethernet chips, and the use of offload engines on Ethernet interface cards intended for network servers. In April 2008, the term was used for switches, and, in July 2008, used with wireless routers that featured user-selectable off periods for Wi-Fi to further reduce energy consumption.

Projected power savings of up to 80 percent were predicted using Green Ethernet switches, translating into a longer product life due to reduced heat.

---
title: "ArpON"
source: https://en.wikipedia.org/wiki/Dynamic_ARP_Inspection
domain: dhcp-snooping
license: CC-BY-SA-4.0
tags: dhcp snooping, rogue dhcp defense, trusted ports, binding table
fetched: 2026-07-02
---

# ArpON

(Redirected from

Dynamic ARP Inspection

)

**ArpON** (**ARP handler inspection**) is a computer software project to improve network security. It has attracted interest among network managers and academic researchers and is frequently cited as a means of protecting against ARP-based attacks.

## Motivation

The Address Resolution Protocol (ARP) has many security issues. These include the Man In The Middle (MITM) attack through the ARP spoofing, ARP cache poisoning, Denial of Service and ARP poison routing attacks.

## Solution

ArpON is a host-based solution that makes the ARP secure and avoids the man-in-the-middle attack through ARP spoofing, ARP cache poisoning or ARP poison routing. This is possible using three kinds of anti-ARP-spoofing techniques:

- SARPI (Static ARP Inspection) for the statically configured networks without DHCP;
- DARPI (Dynamic ARP Inspection) for the dynamically configured networks with DHCP;
- HARPI (Hybrid ARP Inspection) for the statically and dynamically configured networks with DHCP.

The goal of ArpON is therefore to provide a secure and efficient network daemon that provides the SARPI, DARPI and HARPI anti-ARP-spoofing technique, thus making the ARP standardized protocol secure from any foreign intrusion.

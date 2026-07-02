---
title: "Hyperjacking"
source: https://en.wikipedia.org/wiki/Hyperjacking
domain: hyper-v
license: CC-BY-SA-4.0
tags: hyper-v, microsoft hyper-v, hyperjacking, windows virtualization
fetched: 2026-07-02
---

# Hyperjacking

**Hyperjacking** is an attack in which a hacker takes malicious control over the hypervisor that creates the virtual environment within a virtual machine (VM) host. The point of the attack is to target the operating system that is below that of the virtual machines so that the attacker's program can run and the applications on the VMs above it will be completely oblivious to its presence.

## Overview

Hyperjacking involves installing a malicious, fake hypervisor that can manage the entire server system. Regular security measures are ineffective because the operating system will not be aware that the machine has been compromised. In hyperjacking, the hypervisor specifically operates in stealth mode and runs beneath the machine, making it more difficult to detect and more likely to gain access to computer servers where it can affect the operation of the entire institution or company. If the hacker gains access to the hypervisor, everything that is connected to that server can be manipulated. The hypervisor represents a single point of failure when it comes to the security and protection of sensitive information.

For a hyperjacking attack to succeed, an attacker would have to take control of the hypervisor by the following methods:

- Injecting a rogue hypervisor beneath the original hypervisor
- Directly obtaining control of the original hypervisor
- Running a rogue hypervisor on top of an existing hypervisor

## Mitigation techniques

Some basic design features in a virtual environment can help mitigate the risks of hyperjacking:

- Security management of the hypervisor must be kept separate from regular traffic. This is a more network related measure than hypervisor itself related.
- Guest operating systems should never have access to the hypervisor. Management tools should not be installed or used from guest OS.
- Regularly patching the hypervisor.

## Known attacks

As of early 2015, there had not been any report of an actual demonstration of a successful hyperjacking besides "proof of concept" testing. The VENOM vulnerability (CVE-2015-3456) was revealed in May 2015 and had the potential to affect many datacenters. Hyperjackings are rare due to the difficulty of directly accessing hypervisors; however, hyperjacking is considered a real-world threat.

On September 29, 2022, Mandiant and VMware jointly made public their findings that a hacker group has successfully executed malware-based hyperjacking attacks in the wild, affecting multiple target systems in an apparent espionage campaign. In response, Mandiant released a security guide with recommendations for hardening the VMware ESXi hypervisor environment.

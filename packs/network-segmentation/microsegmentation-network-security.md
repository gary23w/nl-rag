---
title: "Microsegmentation (network security)"
source: https://en.wikipedia.org/wiki/Microsegmentation_(network_security)
domain: network-segmentation
license: CC-BY-SA-4.0
tags: network segmentation, network microsegmentation, demilitarized zone network, air gap network, network access control
fetched: 2026-07-02
---

# Microsegmentation (network security)

In network security, **microsegmentation** is a network security architecture that establishes security zone boundaries at the level of individual workloads within data centers and cloud environments, which allows workloads to be isolated and secured independently. Although originally applied to data center networks, microsegmentation is also used in client network environments.

## Types of microsegmentation

### Native OS host-based firewall segmentation

It uses operating system firewalls to regulate network traffic between segments. Rather than relying on routers, network firewalls, or agents, each host firewall performs auditing and enforcement to limit lateral movement between machines.

### Host-agent segmentation

The host-agent segmentation approach relies on endpoint-based agents that are centrally managed and provide visibility into data flows, reducing the difficulty of identifying obscure or encrypted communications. Host-based agent technology is widely recognized as an effective method for microsegmentation, as compromised devices operate as hosts and can be controlled directly. However, this approach requires software to be installed on every host.

### Hypervisor segmentation

Hypervisor segmentation is a microsegmentation implementation in which all traffic passes through the hypervisor. It enables hypervisor-level traffic monitoring, allows existing firewalls to be used, and supports rule migration as instances are created or removed.

### Network segmentation

The network segmentation approach builds on existing infrastructure by using tried-and-true techniques such as access control lists (ACLs) for segmentation.

## Applications

Microsegmentation helps limit attack propagation by restricting internal network attack paths. In Internet of Things (IoT) environments, microsegmentation helps organizations control lateral communication between devices, which is often unmanaged by perimeter-focused security measures.

## Challenges

Microsegmentation is generally compatible with environments running common operating systems such as Linux, Windows, and macOS, but support is limited for mainframes and other legacy systems. During the initial deployment, some applications may not support microsegmentation, and it can result in operational issues. Defining policies that meet the requirements of all internal systems can also be difficult. Policy development may involve internal trade-offs and extended coordination, making the process time-consuming for some organizations. To mitigate deployment complexities and manage policy trade-offs, organizations use automation and self-service applications.

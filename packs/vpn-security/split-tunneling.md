---
title: "Split tunneling"
source: https://en.wikipedia.org/wiki/Split_tunneling
domain: vpn-security
license: CC-BY-SA-4.0
tags: virtual private network, vpn tunneling protocol, ipsec vpn, wireguard protocol, split tunneling
fetched: 2026-07-02
---

# Split tunneling

In computer networking, **split tunneling** allows a user to access distinct security domains at the same time, using the same or different network connections. This connection state is usually facilitated through the simultaneous use of a LAN network interface controller (NIC), radio NIC, Wireless LAN NIC, and virtual private network client software application. Split tunneling is most commonly configured via the use of a remote-access VPN client, which allows the user to simultaneously connect to a nearby wireless network, resources on an off-site corporate network, as well as websites over the internet.

A split tunnel configured to only tunnel traffic destined to a specific set of destinations is called a *split-include* tunnel. When configured to accept all traffic except traffic destined to a specific set of destinations, it is called a *split-exclude* tunnel.

Not every VPN allows split tunneling. Advantages of split tunneling include alleviating bottlenecks, conserving bandwidth (as internet traffic does not have to pass through the VPN server), and enabling a user to not have to continually connect and disconnect when remotely accessing resources.. Disadvantages include potentially bypassing gateway-level security that might be in place within the company infrastructure. Internet service providers often use split tunneling to that implement for DNS hijacking purposes.

### Inverse split tunneling

An "inverse" split tunnel is one that allows all datagrams to enter the tunnel, except those destination IPs explicitly allowed by VPN gateway. The criteria for allowing datagrams to exit the local network interface (outside the tunnel) may vary from vendor to vendor. This keeps control of network gateways to a centralized policy device such as the VPN terminator. This can be augmented by endpoint policy enforcement technologies such as an interface firewall on the endpoint device's network interface driver, group policy object or anti-malware agent. This is related in many ways to network access control (NAC).

### Dynamic split tunneling

A form of split-tunneling that derives the IP addresses to include/exclude at runtime-based on a list of hostname rules/policies.

### IPv6 dual-stack networking

Internal IPv6 content can be hosted and presented to sites via a unique local address range at the VPN level, while external IPv4 & IPv6 content can be accessed via site routers.

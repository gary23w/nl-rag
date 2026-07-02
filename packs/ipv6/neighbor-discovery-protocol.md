---
title: "Neighbor Discovery Protocol"
source: https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol
domain: ipv6
license: CC-BY-SA-4.0
tags: ipv6, ipv6 address, neighbor discovery protocol, ipv6 transition
fetched: 2026-07-02
---

# Neighbor Discovery Protocol

The **Neighbor Discovery Protocol** (**NDP**), or simply **Neighbor Discovery** (**ND**), is a protocol of the Internet protocol suite used with Internet Protocol Version 6 (IPv6). It operates at the internet layer of the Internet model, and is responsible for gathering various information required for network communication, including the configuration of local connections and the domain name servers and gateways.

The protocol defines five ICMPv6 packet types to perform functions for IPv6 similar to the Address Resolution Protocol (ARP) and Internet Control Message Protocol (ICMP) Router Discovery and Router Redirect protocols for IPv4. It provides many improvements over its IPv4 counterparts. For example, it includes Neighbor Unreachability Detection (NUD), thus improving robustness of packet delivery in the presence of failing routers or links, or mobile nodes.

The **Inverse Neighbor Discovery** (**IND**) protocol extension allows nodes to determine and advertise an IPv6 address corresponding to a given link-layer address, similar to Inverse ARP for IPv4.

The Secure Neighbor Discovery Protocol (SEND), a security extension of NDP, uses Cryptographically Generated Addresses (CGA) and the Resource Public Key Infrastructure (RPKI) to provide an alternative mechanism for securing NDP with a cryptographic method that is independent of IPsec. Neighbor Discovery Proxy (ND Proxy) provides a service similar to IPv4 Proxy ARP and allows bridging multiple network segments within a single subnet prefix when bridging cannot be done at the link layer.

## Functions

NDP defines five ICMPv6 packet types for the purpose of router solicitation, router advertisement, neighbor solicitation, neighbor advertisement, and network redirects.

**Router Solicitation (Type 133)**

Hosts inquire with Router Solicitation messages to locate routers on an attached link.

Routers which forward packets not addressed to them generate Router Advertisements immediately upon receipt of this message rather than at their next scheduled time.

**Router Advertisement (Type 134)**

Routers advertise their presence together with various link and Internet parameters either periodically, or in response to a Router Solicitation message.

**Neighbor Solicitation (Type 135)**

Neighbor solicitations are used by nodes to determine the link-layer address of a neighbor, or to verify that a neighbor is still reachable via a cached link-layer address.

**Neighbor Advertisement (Type 136)**

Neighbor advertisements are used by nodes to respond to a Neighbor Solicitation message, or unsolicited to provide new information quickly.

**Redirect (Type 137)**

Routers may inform hosts of a better first-hop router for a destination.

These messages are used to provide the following functionality:

- Router discovery: hosts can locate routers residing on attached links.
- Prefix discovery: hosts can discover address prefixes that are on-link for attached links.
- Parameter discovery: hosts can find link parameters (e.g., MTU).
- Address autoconfiguration: optional stateless configuration of addresses of network interfaces (see IPv6 § Stateless address autoconfiguration (SLAAC) and IPv6 address § Stateless address autoconfiguration).
- Address resolution: mapping between IP addresses and link-layer addresses.
- Next-hop determination: hosts can find next-hop routers for a destination.
- Neighbor unreachability detection (NUD): determine that a neighbor is no longer reachable on the link.
- Duplicate address detection (DAD): nodes can check whether an address is already in use.
- Recursive DNS Server (RDNSS) and DNS Search List (DNSSL) assignment via a router advertisement (RA) options. This is a proposed standard since 2010 and updated in March 2017, but not supported by all clients.
- Packet redirection to provide a better next-hop route for certain destinations.

IANA maintains a list of all current NDP options as they are published.

## Example

Two computers, *A* and *B* are connected to the same local area network with no intervening gateway or router. *A* has a packet to send to IP address *2001:db8::55* which happens to be the address of *B*.

Before sending the packet to *B*, *A* creates a solicited-node multicast address by appending the least-significant 24 bits of *B's* address to the prefix *ff02::1:ff00:0/104*, which is *ff02::1:ff00:55* and creates a solicited-node multicast MAC address by appending the least-significant 24 bits of *B's* solicited-node multicast address to the prefix *33:33:FF:xx:xx:xx*, which is *33:33:FF:00:00:55*. *A* sends a neighbor solicitation message requesting an answer for *2001:db8::55* (destination *ff02::1:ff00:55* IP address and destination *33:33:FF:00:00:55* MAC address), which is accepted by *B* which is listening on its own solicited-node multicast address on the local network. *B* responds with a neighbor advertisement message containing its MAC and IP addresses. *A* receives the response and sends the packet on the link with *B's* MAC address.

Typically, network nodes maintain a lookup cache that associates IP and MAC addresses. In this example, if A had the lookup cached, then it would not need to send the NDP request. Also, when B received the request, it could cache the lookup to A so that if B needs to send a packet to A later, it does not need to use NDP to lookup its MAC address. Finally, when A receives the NDP response, it can cache the lookup for future messages addressed to the same IP address.

## Messages formats

- (Router Solicitation Message) Router Solicitation Message
- (Router Advertisement Message) Router Advertisement Message
- (Neighbor Solicitation Message) Neighbor Solicitation Message
- (Neighbor Advertisement Message) Neighbor Advertisement Message
- (Redirect Message) Redirect Message

---
title: "List of IPv6 transition mechanisms"
source: https://en.wikipedia.org/wiki/IPv6_transition_mechanism
domain: ipv6
license: CC-BY-SA-4.0
tags: ipv6, ipv6 address, neighbor discovery protocol, ipv6 transition
fetched: 2026-07-02
---

# List of IPv6 transition mechanisms

(Redirected from

IPv6 transition mechanism

)

To increase the deployment of IPv6 on the Internet, various transition mechanisms have been proposed to ease this process. Since IPv6 is not directly interoperable with its predecessor protocol IPv4, transition mechanisms are designed to permit hosts on either network type to communicate with any other host.

To meet its technical criteria, IPv6 must have a straightforward transition plan from the current IPv4. The Internet Engineering Task Force (IETF) conducts working groups and discussions through the IETF Internet Drafts and Request for Comments processes to develop these transition technologies toward that goal. Some basic IPv6 transition mechanisms are defined in RFC 4213.

## Stateless IP/ICMP Translation

**Stateless IP/ICMP Translation** (**SIIT**) translates between the packet header formats in IPv6 and IPv4. The SIIT method defines a class of IPv6 addresses called *IPv4-translated* addresses. They have the prefix *::ffff:0:0:0/96* and may be written as *::ffff:0:a.b.c.d*, in which the IPv4 formatted address *a.b.c.d* refers to an *IPv6-enabled* node. The prefix was chosen to yield a zero-valued checksum to avoid changes to the transport protocol header checksum. The algorithm can be used in a solution that allows IPv6 hosts that do not have a permanently assigned IPv4 address to communicate with IPv4-only hosts. Address assignment and routing details are not addressed by the specification. SIIT can be viewed as a special case of stateless network address translation.

The specification is a product of the NGTRANS IETF working group, and was initially drafted in February 2000 by E. Nordmark of Sun Microsystems. It was revised in 2011, and in 2016 its current revision was published.

## Tunnel broker

A tunnel broker provides IPv6 connectivity by encapsulating IPv6 traffic in IPv4 Internet transit links, typically using 6in4. This establishes IPv6 tunnels within the IPv4 Internet. The tunnels may be managed with the Tunnel Setup Protocol (TSP) or AYIYA.

## 6rd

6rd was developed by Rémi Després. It is a mechanism to facilitate rapid deployment of the IPv6 service across IPv4 infrastructures of Internet service providers (ISPs). It uses stateless address mappings between IPv4 and IPv6 addresses, and transmits IPv6 packets across automatic tunnels that follow the same optimized routes between customer nodes as IPv4 packets.

It was used for an early large deployment of an IPv6 service with native addresses during 2007 (RFC 5569). The standard-track specification of the protocol is in RFC 5969.

## Transport Relay Translation

The **Transport Relay Translation** (**TRT**) method acts as an intermediate device between two hosts. The function of the translator is to convert IPV6 into IPV4 addresses and vice versa. TRT accomplishes this translation through IP address mapping and a custom IP address.

The address, for example, if packets are to be transmitted from an IPv6 address (*fec0:0:0:1::/64*) to an IPv4 address (*10.1.1.1*) would read as *fec0:0:0:1::10.1.1.1*. The packets are routed toward the translator firstly through an IPv6/TCP protocol and then from the translator to the IPv4 host through an IPv4/TCP protocol.

TRT employs a similar operation to DNS translation between AAAA and A records known as *DNS ALG*.

## NAT64

NAT64 is a mechanism to allow IPv6 hosts to communicate with IPv4 servers. The NAT64 server is the endpoint for at least one IPv4 address and an IPv6 network segment of 32-bits, e.g., *64:ff9b::/96*. The IPv6 client embeds the IPv4 address with which it wishes to communicate using these bits, and sends its packets to the resulting address. The NAT64 server then creates a NAT-mapping between the IPv6 and the IPv4 address, allowing them to communicate. NAT64 is typically used in conjunction with DNS64.

## DNS64

**DNS64** describes a DNS server that when asked for a domain's AAAA records, but only finds A records, synthesizes the AAAA records from the A records. The first part of the synthesized IPv6 address points to an IPv6/IPv4 translator and the second part embeds the IPv4 address from the A record. The translator in question is usually a NAT64 server. The standard-track specification of DNS64 is in RFC 6147.

There are two noticeable issues with this transition mechanism:

- It only works for cases where DNS is used to find the remote host address; if IPv4 literals are used, the DNS64 server will never be involved.
- Because the DNS64 server needs to return records not specified by the domain owner, DNSSEC validation against the root will fail in cases where the DNS server doing the translation is not the domain owner's server.

```mw
# DNS resolver 2606:4700:4700:64 synthesizes AAAA records for
# ipv6test.google.com to a NAT64 address: 64:ff9b::<original-ipv4>
$ nslookup ipv6test.google.com 2606:4700:4700::64

Non-authoritative answer:
ipv6test.google.com	canonical name = ipv6test.l.google.com.
Name:	ipv6test.l.google.com
Address: 64:ff9b::8efa:c3e4
```

**Implementations**

- Unbound DNS server via the dns64 module
- OpenWrt via unbound opkg packages
- Technitium DNS server via the dns64 DNS app

## ISATAP

ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) is an IPv6 transition mechanism meant to transmit IPv6 packets between dual-stack nodes on top of an IPv4 network.

Unlike 6over4 (an older similar protocol using IPv4 multicast), ISATAP uses IPv4 as a virtual nonbroadcast multiple-access network (NBMA) data link layer, so that it does not require the underlying IPv4 network infrastructure to support multicast.

## 464XLAT

464XLAT allows clients on IPv6-only networks to access IPv4-only Internet services. It extends NAT64 by adding another initial translation step from IPv4 to IPv6, which allows IPv4-only clients or applications to communicate over IPv6-only connections.

The client uses a SIIT translator to convert packets from IPv4 to IPv6. These are then sent to a NAT64 translator which translates them from IPv6 back into IPv4 and on to an IPv4-only server.

The client translator may be implemented on the client itself or on an intermediate device and is known as the CLAT (Customer-side transLATor). RFC 7335 specifies a special IPv4 prefix *192.0.0.0/29* reserved by IANA for use in IPv4 transition scenarios, known as the *IPv4 Service Continuity Prefix*, which was previously reserved for specifically DS-Lite but has since been extended to support any transition mechanism similar in operation. The CLAT implementation may use addresses from this prefix for internal numbering, although packets containing these addresses are never actually sent out over the network.

The NAT64 translator, or PLAT (Provider-side transLATor), must be able to reach both the server and the client (through the CLAT). The PLAT is identical to standalone NAT64, and no changes need to be made from the provider side to support 464XLAT. The use of NAT64 limits connections to a client–server model using UDP, TCP, and ICMP.

If DNS64 is in use on the IPv6-only network, most applications that need to connect to an IPv4-only service will already natively initiate connections using IPv6 to the NAT64 prefix. This means that 464XLAT is only required for applications that do not understand IPv6, have a preference for IPv4, or use hard-coded IPv4 addresses.

**Implementations**

- T-Mobile US became IPv6-only using 464XLAT.
- Orange Polska began IPv6-only (CLAT/NAT64/DNS) service in September 2013, migrating all ADSL, VDSL, and FTTH gateways by January 2015.
- Telstra became IPv6-only for mobile services using 464XLAT in February 2020.
- Android includes a native implementation of CLAT since Jelly Bean 4.3, released in 2013.
- Windows 10 has a native WWAN-only implementation of 464XLAT for desktop and mobile since the 2017 Creators Update.
- Windows 11 (26H1 and older) is limited to the WWAN interface as in windows 10. Extended CLAT support to other network devices was added to Windows Insider Canary builds (>=29599.1000). The implementation follows RFC 7050 (ipv4only.arpa DNS query), RFC 8781 (PREF64, and RFC 8925 (DHCP Option 108) standard..
- macOS starts to have native CLAT support in Ventura, released in 2022.
- iOS has a native CLAT implementation since version 12.0, released in 2018. Additionally, Apple requires all apps submitted to the App Store to work on IPv6-only networks.
- clatd is a CLAT implementation for Linux.
- NetworkManager starting in version 1.58 (unreleased as of 2026-06-17), NetworkManager ships an BPF based CLAT implementation
- OpenWRT linux OS for routers has optional support for clat via the 464xlat package.
- FreeBSD has implemented NAT64 CLAT since Release 12.1.

## Dual-Stack Lite (DS-Lite)

**Dual-Stack Lite** technology does not involve allocating an IPv4 address to customer-premises equipment (CPE) for providing Internet access. The CPE distributes private IPv4 addresses for the LAN clients, according to the networking requirement in the local area network. The CPE encapsulates IPv4 packets within IPv6 packets. The CPE uses its global IPv6 connection to deliver the packet to the ISP's carrier-grade NAT (CGN), which has a global IPv4 address. The original IPv4 packet is recovered, address translation is performed upon the IPv4 packet, and it is routed to the public IPv4 Internet. The carrier-grade NAT router uniquely identifies traffic flows by recording the protocol used (e.g. UDP, SCTP), customer public IPv6 address, the customer node private IPv4 address, customer node port number if applicable (e.g. with UDP or TCP), and the IPv4 address, and port number if applicable, of the upstream node, as a session.

**Lightweight 4over6** extends DS-Lite by moving the NAT functionality from the ISP side to the CPE, eliminating the need to implement carrier-grade NAT. This is accomplished by allocating a port range for a shared IPv4 address to each CPE. Moving the NAT functionality to the CPE allows the ISP to reduce the amount of state tracked for each subscriber, which improves the scalability of the translation infrastructure.

## V4-via-v6 routing

*V4-via-v6* routing is a technique where IPv4 addresses are assigned to end hosts only while intermediate routers are only assigned IPv6 addresses. IPv4 routes are propagated as usual, and no packet translation or encapsulation is employed, but use an IPv6 next hop. V4-via-v6 reduces the amount of management required, since the core network only needs to be assigned IPv6 addresses, but still requires that the core network be able to forward IPv4 packets.

V4-via-v6 is defined for the Border Gateway Protocol (BGP) and the Babel routing protocol. It has been implemented in the Bird Internet routing daemon and in *babeld*.

## MAP

Mapping of Address and Port (MAP) is a Cisco IPv6 transition proposal which combines A+P port address translation with tunneling of the IPv4 packets over an ISP provider's internal IPv6 network. MAP-T and MAP-E entered standards track in July 2015, and Sky Italia has deployed MAP-T in its internet services as early as year 2021.

## Draft proposals

The following mechanisms are still being discussed or have been abandoned by the IETF:

### 4rd

IPv4 Residual Deployment (4rd) is an experimental mechanism to facilitate residual deployment of the IPv4 service across IPv6 networks. Like 6rd, it uses stateless address mappings between IPv6 and IPv4. It supports an extension of IPv4 addressing based on transport-layer ports. This is a stateless variant of the A+P model.

## Deprecated mechanisms

These mechanisms have been deprecated by the IETF:

### NAT-PT

*Network Address Translation/Protocol Translation* (**NAT-PT**) is defined in RFC 2766, but due to numerous problems, it has been obsoleted by RFC 4966 and deprecated to historic status. It is typically used in conjunction with a DNS application-level gateway (DNS-ALG) implementation.

### NAPT-PT

While almost identical to NAT-PT, *Network Address Port Translation + Protocol Translation*, which is also described in RFC 2766, adds translation of the ports as well as the address. This is done primarily to avoid two hosts on one side of the mechanism from using the same exposed port on the other side of the mechanism, which could cause application instability and security flaws. This mechanism has been deprecated by RFC 4966.

## Implementations

- CLATD, a CLAT / SIIT-DC Edge Relay implementation for Linux
- TAYGA, a stateless NAT64 implementation for Linux
- Jool, a SIIT and stateful NAT64 implementation for Linux
- naptd, user-level NAT-PT
- Address Family Transition Router (AFTR), a DS-Lite implementation
- Microsoft Forefront Unified Access Gateway, a discontinued reverse proxy and VPN solution that implements DNS64 and NAT64
- BIND, Berkeley Internet Name Domain DNS server, implements DNS64 since version 9.8
- PF (firewall), the OpenBSD packet filter supports IP version translation since version 5.1, includes NAT64

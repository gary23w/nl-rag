---
title: "Carrier-grade NAT"
source: https://en.wikipedia.org/wiki/Carrier-grade_NAT
domain: carrier-grade-nat
license: CC-BY-SA-4.0
tags: carrier-grade nat, large scale nat, address sharing, ipv4 exhaustion
fetched: 2026-07-02
---

# Carrier-grade NAT

**Carrier-grade NAT** (**CGN** or **CGNAT**) (also known as **large-scale NAT**, **LSN**) is a type of network address translation (NAT) used by Internet service providers (ISPs) in IPv4 network design. With CGN, end sites, in particular residential networks, are configured with private network addresses that are translated to public IPv4 addresses by middlebox network address translator devices embedded in the network operator's network, permitting the sharing of small pools of public addresses among many end users. This essentially repeats the traditional customer-premises NAT function at the ISP level.

Carrier-grade NAT is often used for mitigating IPv4 address exhaustion.

One use scenario of CGN has been labeled as **NAT444**, because some customer connections to Internet services on the public Internet would pass through three different IPv4 addressing domains: the customer's own private network, the carrier's private network and the public Internet.

Another CGN scenario is Dual-Stack Lite, in which the carrier's network uses IPv6 and thus only two IPv4 addressing domains are needed. CGN may also be applied using ISP-level NAT64 translators in combination with 464XLAT, which eliminates IPv4 entirely at the residential network.

CGN techniques were first used in 2000 to accommodate the immediate need for large numbers of IPv4 addresses in General Packet Radio Service (GPRS) deployments of mobile networks. Estimated CGN deployments increased from 1,200 in 2014 to 3,400 in 2016, with 28.85% of the studied deployments appearing to be in mobile operator networks.

## Shared address space

If an ISP deploys a CGN, and uses RFC 1918 address space to number customer gateways, the risk of address collision, and therefore routing failures, arises when the customer network already uses an RFC 1918 address space.

This prompted some ISPs to develop a policy within the American Registry for Internet Numbers (ARIN) to allocate new private address space for CGNs, but ARIN deferred to the IETF before implementing the policy indicating that the matter was not a typical allocation issue but a reservation of addresses for technical purposes (per RFC 2860).

IETF published RFC 6598, detailing a shared address space for use in ISP CGN deployments that can handle the same network prefixes occurring both on inbound and outbound interfaces. ARIN returned address space to the Internet Assigned Numbers Authority (IANA) for this allocation. The allocated address block is 100.64.0.0/10, i.e. IP addresses from 100.64.0.0 to 100.127.255.255.

Devices evaluating whether an IPv4 address is public must be updated to recognize the new address space. Allocating more private IPv4 address space for NAT devices might postpone the need to transition to IPv6.

## Advantages

- Maximises use of limited public IPv4 address space.

## Disadvantages

- Like any form of NAT, it breaks the end-to-end principle.
- It has significant security and reliability problems, by virtue of being stateful.
- It does not solve the IPv4 address exhaustion problem when a public IP address is needed, such as in Web hosting.
- It may create a performance bottleneck that limits scalability.
- It usually prevents the ISP's customers from using port forwarding, because the NAT is usually implemented by mapping ports of the NAT devices in the network to other ports in the external interface. This is done so the router will be able to map the responses to the correct device; in carrier-grade NAT networks, even though the router at the consumer end might be configured for port forwarding, the "master router" of the ISP, which runs the CGN, will block this port forwarding because the actual port would not be the port configured by the consumer. In order to overcome the former disadvantage, the Port Control Protocol (PCP) has been standardized in the RFC 6887; uptake by carriers has been slow.
- In cases of banning traffic based on IP addresses, a system might block the traffic of a spamming user by banning the user's IP address. If that user happens to be behind carrier-grade NAT, other users sharing the same public address with the spammer will be inadvertently blocked. This can create problems for forum and wiki administrators attempting to address disruptive actions of a single malicious user sharing an IP address with legitimate users.
- Streaming media services may see CGN activity as equivalent to VPN or account sharing traffic. Such services often block or ban VPN users for breaching terms of service under an assumption they are accessing content from a cheaper region in an attempt to pay less money for the service, and account sharing traffic being blocked for multiple distinct households or users accessing the content for the price of one login.
- CGN interferes with the operation of several IPv6 transition mechanisms.
- Critics of CGN may argue that the deployment of CGN diverts management and technical resources that would be better applied to promoting and resourcing uptake of IPv6.

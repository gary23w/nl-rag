---
title: "Black hole (networking)"
source: https://en.wikipedia.org/wiki/Black_hole_(networking)
domain: ddos-mitigation-deep
license: CC-BY-SA-4.0
tags: ddos mitigation, volumetric attack scrubbing, anycast absorption, blackhole routing defense, rate limiting protection
fetched: 2026-07-02
---

# Black hole (networking)

In networking, a **black hole** refers to a place in the network where incoming or outgoing traffic is discarded (or "dropped" or sinkholed) without informing the source that the data did not reach its intended recipient.

When examining the topology of the network, the black holes themselves are invisible, and can only be detected by monitoring the lost traffic.

The name is presumed to have originated from the astronomical body called a black hole - an astronomical body so dense that its gravity prevents anything from escaping, even light.

## Addresses

A black hole IP address specifies a host machine that is not running or an address to which no host has been assigned.

Even though TCP/IP provides a means of communicating the delivery failure back to the sender via ICMP, traffic destined for such addresses is often just dropped.

Blackholed addresses are undetectable only to protocols that are both connectionless and unreliable (e.g., UDP). Connection-oriented or reliable protocols (TCP, RUDP) will either fail to connect to a blackholed address or will fail to receive expected acknowledgements.

For IPv6, the black hole prefix is *100::/64*.

For IPv4, no black hole address is explicitly defined, however the reserved IP addresses can help achieve a similar effect. For example, *198.51.100.0/24* is reserved for use in documentation and examples; while the RFC advises that the addresses in this range are not routed, this is not a requirement.

With the invention of cryptocurrencies addresses as locations where monies exist, there is the possibility of blackholing a quantity of crypto.

## Firewalls and "stealth" ports

Most firewalls (and routers for household use) can be configured to silently discard packets addressed to forbidden hosts or ports, resulting in small or large "black holes" in the network.

Personal firewalls that do not respond to ICMP echo requests ("ping") have been designated by some vendors as being in "stealth mode".

Despite this, in most networks the IP addresses of hosts with firewalls configured in this way are easily distinguished from invalid or otherwise unreachable IP addresses: On encountering the latter, a router will generally respond with an ICMP network rsp. host unreachable error. Network address translation (NAT), as used in home and office routers, is generally a more effective way of obscuring the layout of an internal network.

### PMTUD black holes

Some firewalls incorrectly discard all ICMP packets, including the ones needed for Path MTU discovery to work correctly. This causes TCP connections from/to/through hosts with a lower MTU to hang.

## Black hole filtering

A **null route** or **black hole route** is a network route (routing table entry) that goes nowhere. Matching packets are dropped (ignored) rather than forwarded, acting as a kind of very limited firewall. The act of using null routes is often called **blackhole filtering**.

Black hole filtering refers specifically to dropping packets at the routing level, usually using a routing protocol to implement the filtering on several routers at once, often dynamically to respond quickly to distributed denial-of-service attacks (DDoS).

Remote Triggered Black Hole Filtering (RTBH) is a technique that provides the ability to drop undesirable traffic before it enters a protected network. The Internet Exchange (IX) provider usually acquires this technology to help its members or participants to filter such attacks.

Null routes are typically configured with a special route flag; for example, the standard iproute2 command `ip route` allows to set route types `unreachable, blackhole, prohibit` which discard packets. Alternatively, a null route can be implemented by forwarding packets to an illegal IP address such as *0.0.0.0*, or the loopback address.

Null routing has an advantage over classic firewalls since it is available on every potential network router (including all modern operating systems), and adds virtually no performance impact. Due to the nature of high-bandwidth routers, null routing can often sustain higher throughput than conventional firewalls. For this reason, null routes are often used on high-performance core routers to mitigate large-scale denial-of-service attacks before the packets reach a bottleneck, thus avoiding collateral damage from DDoS attacks — although the target of the attack will be inaccessible to anyone. Blackhole filtering can also be abused by malicious attackers on compromised routers to filter out traffic destined to a certain address.

Routing typically only works on the Internet Protocol layer and is very limited in packet classification. It is bound to be stateless due to the nature of IP routers. Typically, classification is limited to the destination IP address prefix, source IP address and incoming network interface.

## DNS Blackhole Server

**Blackhole DNS servers** are Domain Name System (DNS) servers that return a "nonexistent address" answer to reverse DNS lookups for addresses reserved for private use. Their goal is to authoritatively deny the existence of reverse DNS names for such reserved addresses, which reduces the load on other parts of the DNS infrastructure as it allows recursive resolvers to cache the negative answers.

## DNS-based Blackhole List

A **DNS-based Blackhole List** (**DNSBL**) or **Real-time Blackhole List** (**RBL**) is a list of IP addresses published through the Internet Domain Name System (DNS) either as a zone file that can be used by DNS server software, or as a live DNS zone that can be queried in real-time. DNSBLs are most often used to publish the addresses of computers or networks linked to spamming; most mail server software can be configured to reject or flag messages which have been sent from a site listed on one or more such lists. The term "Blackhole List" is sometimes interchanged with the term "blacklist" and "blocklist".

## Black hole e-mail addresses

A black hole e-mail address is an e-mail address which is valid (messages sent to it will not generate errors), but all the received messages are automatically deleted, and never stored or seen by humans. These addresses are often used as return addresses for automated e-mails.

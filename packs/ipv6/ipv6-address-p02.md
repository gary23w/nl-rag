---
title: "IPv6 address (part 2/2)"
source: https://en.wikipedia.org/wiki/IPv6_address
domain: ipv6
license: CC-BY-SA-4.0
tags: ipv6, ipv6 address, neighbor discovery protocol, ipv6 transition
fetched: 2026-07-02
part: 2/2
---

## Historical notes

### Deprecated and obsolete addresses

- The site-local prefix *fec0::/10* specifies that the address is valid only within the site network of an organization. It was part of the original addressing architecture in December 1995, but its use was deprecated in September 2004 because the definition of the term *site* was ambiguous, which led to confusing routing rules. New networks must not support this special type of address. In October 2005, a new specification replaced this address type with unique local addresses.
- The address block *200::/7* was defined as an OSI NSAP-mapped prefix set in August 1996, but was deprecated in December 2004.
- The 96-bit zero-value prefix *::/96*, originally known as *IPv4-compatible addresses*, was mentioned in 1995 but never fully described. This range of addresses was used to represent IPv4 addresses within an IPv6 transition technology. Such an IPv6 address has its first (most significant) 96 bits set to zero, while its last 32 bits are the represented IPv4 address. In February 2006, the IETF deprecated the use of IPv4-compatible addresses. The only remaining use of this address format is to represent an IPv4 address in a table or database with fixed size members that must also be able to store an IPv6 address.
- Address block *3ffe::/16* was allocated for test purposes for the 6bone network in December 1998. Prior to that, the address block *5f00::/8* was used for this purpose. Both address blocks were returned to the address pool in June 2006.
- Due to operational problems with 6to4 the use of address block *2002::/16* is diminishing, since the 6to4 mechanism is deprecated since May 2015. Although IPv4 address block *192.88.99.0/24* is deprecated, *2002::/16* is not.
- In April 2007 the address block *2001:10::/28* was assigned for Overlay Routable Cryptographic Hash Identifiers (ORCHID). It was intended for experimental use. In September 2014 a second version of ORCHID was specified, and with the introduction of block *2001:20::/28* the original block was returned to IANA.

### Miscellaneous

- For reverse DNS lookup, IPv6 addresses were originally registered in the DNS zone *ip6.int*, because it was expected that the top-level domain arpa would be retired. In 2000, the Internet Architecture Board (IAB) reverted this intention and decided in 2001 that arpa should retain its original function. Domains in ip6.int were moved to ip6.arpa and zone ip6.int was officially removed on 6 June 2006.
- In March 2011, the IETF refined the recommendations for allocation of address blocks to end sites. Instead of assigning either a */48*, */64*, or */128* (according to IAB's and IESG's views of 2001), Internet service providers should consider assigning smaller blocks (for example a */56*) to end users. The ARIN, RIPE and APNIC regional registries' policies encourage */56* assignments where appropriate.
- Originally, two proposals existed for translating domain names to IPv6 addresses: one using AAAA records, the other using A6 records. AAAA records, the method that prevailed, are comparable to A records for IPv4, providing a simple mapping from hostname to IPv6 address. The method using A6 records used a hierarchical scheme, in which the mapping of subsequent groups of address bits was specified by additional A6 records, providing the possibility to renumber all hosts in a network by changing a single A6 record. As the perceived benefits of the A6 format were not deemed to outweigh the perceived costs, the method was moved to experimental status in 2002, and finally to historic status in 2012.
- In 2009, many DNS resolvers in home-networking NAT devices and routers were found to handle AAAA records improperly. Some of these simply dropped DNS requests for such records, instead of properly returning the appropriate negative DNS response. Because the request is dropped, the host sending the request has to wait for a timeout causing increased latency when connecting to dual-stack IPv6/IPv4 hosts, as the client software waits for the timeout for the IPv6 connection to fail before trying IPv4. Happy Eyeballs provides a solution to this problem.

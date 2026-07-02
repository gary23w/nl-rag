---
title: "DNS zone"
source: https://en.wikipedia.org/wiki/DNS_zone
domain: aws-route53
license: CC-BY-SA-4.0
tags: aws route53, cloud dns, managed dns, dns resolution
fetched: 2026-07-02
---

# DNS zone

A **DNS zone** is a specific portion of the DNS namespace in the Domain Name System (DNS), which a specific organization or administrator manages. A DNS zone is an administrative space allowing more granular control of the DNS components, such as authoritative nameserver. The DNS is broken up into different zones, distinctly managed areas in the DNS namespace. DNS zones are not necessarily physically separated from one another; however, a DNS zone can contain multiple subdomains, and multiple zones can exist on the same server.

The domain namespace of the Internet is organized into a hierarchical layout of subdomains below the DNS root domain. The individual domains of this tree may serve as delegation points for administrative authority and management. However, it is usually desirable to implement fine-grained delegation boundaries so that multiple sub-levels of a domain may be managed independently. Therefore, the domain name space is partitioned into areas (*zones*) for this purpose. A zone starts at a domain and extends downward in the tree to the leaf nodes or to the top-level of subdomains where other zones start.

A DNS zone is implemented in the configuration system of a domain name server. Historically, it is defined in the zone file, an operating system text file that starts with the special DNS record type *Start of Authority* (SOA) and contains all records for the resources described within the zone. This format was originally used by the Berkeley Internet Name Domain Server (BIND) software package and is defined in RFC 1034 and RFC 1035.

## Domains and zones

Most top-level domain name registry operators offer their namespaces to the public or entities with the mandated geographic or otherwise scoped purpose for registering second-level domains. Similarly, an organization in charge of a lower-level domain may operate its namespace and subdivide its space.

Each registration or allocation of subdomain space obligates the registrant to maintain an administrative and technical infrastructure to manage the responsibility for its zone, including sub-delegation to lower-level domains. Each delegation confers essentially unrestricted technical autonomy over the allocated space. An area of one or more subdomains that have been delegated for management is called a DNS zone. A zone always starts at a domain boundary to include all leaf nodes (hosts) in the domain or ends at the boundary of another independently managed zone.

As each domain is further divided into sub-domains, each becoming a DNS zone with its own set of administrators and DNS servers, the tree grows with the largest number of leaf nodes at the bottom. At this lowest level, in the end-nodes or leaves of the tree, the term *DNS zone* becomes essentially synonymous with the term "domain", both in terms of use and administration. The term *domain* is used in the business functions of the entity assigned to it, and the term *zone* is usually used for the configuration of DNS services.

## Forward DNS zones

DNS zones contain the records for mapping domain names to IP addresses or other information. The resolution of a domain name to its assigned information is also referred to as *forward* resolution, and the DNS zones associated with such processes are often referred to as *forward* zones. The term arose as the opposite of *reverse* zones, which are used for the reverse process: finding the DNS name associated with an IP address. Such reverse zones are maintained in the Internet Address and Routing Parameter Area (domain arpa).

Another common use of the term *forward zone* refers to a specific configuration of DNS name servers, particularly caching name servers, in which resolution of a domain name is forwarded to another name server that is authoritative for the domain in question, rather than being answered from the established cache memory.

## Zones for Internet infrastructure

The top-level domain arpa serves as a delegation zone for various technical infrastructure aspects of DNS and the Internet, and does not implement the registration and delegation system of the country and generic domains. The name *arpa* is a remnant of the ARPANET, one of the predecessor stages of the Internet. Intended as a transitional aid to the DNS, deleting the domain arpa was later found to be impractical. Consequently, the name was officially redefined as an acronym for *Address and Routing Parameter Area*. It contains sub-zones used for reverse resolution of IP addresses to host names (IPv4: in-addr.arpa, IPv6: ip6.arpa), telephone number mapping (ENUM, e164.arpa), and uniform resource identifier resolution (uri.arpa, urn.arpa).

Although the administrative structure of this domain and its sub-domains is different, the technical delegation into zones of responsibility is similar and the DNS tools and servers used are identical to any other zone. Sub-zones are delegated by components of the respective resources. For example, 8.8.2.5.5.2.2.0.0.8.1.e164.arpa., which might represent an E.164 telephone number in the ENUM system, might be sub-delegated at suitable boundaries of the name. An example of an IP addresses in the reverse DNS zone is 166.188.77.208.in-addr.arpa, which represents the address 208.77.188.166 and resolves to the domain name *www.example.com*. In the case of IP addresses, the reverse zones are delegated to the Internet service provider (ISP) to which the IP address block is assigned. When an ISP allocates a range to a customer, it usually also delegates the management of that space to the customer by insertion of name server resource records pointing to the customer's DNS facilities into their zone, or provides other management tools. Allocations of single IP addresses for networks connected through network address translation (NAT) typically do not provide such facilities.

## Example of zone authority in DNS queries

As an example of the DNS resolving process, consider the role of a recursive DNS resolver attempting to look up the address "en.wikipedia.org.". It begins with a list of addresses for the most authoritative name servers it knows about – the root zone name servers (indicated by the full stop or period), which contains name server information for all top-level domains (TLDs) of the Internet.

When querying one of the root name servers, it is possible that the root zone will not directly contain a record for "en.wikipedia.org.", in which case it will provide a referral to the authoritative name servers for the "org." top-level domain (TLD). The resolver is issued a referral to the authoritative name servers for the "org." zone, which it will contact for more specific information. Again when querying one of the "org." name servers, the resolver may be issued with another referral to the "wikipedia.org." zone, whereupon it will again query for "en.wikipedia.org.". Since (as of July 2010) "en.wikipedia.org." is a CNAME to "text.wikimedia.org." (which is in turn a CNAME to "text.esams.wikimedia.org."), and the "wikipedia.org." name servers also happen to contain authoritative data for the "wikimedia.org." zone, the resolution of this particular query occurs entirely within the queried name server, and the resolver will receive the address record it requires with no further referrals.

If the last name server queried did not contain authoritative data for the target of the CNAME, it would have issued the resolver with yet another referral, this time to the zone "text.wikimedia.org.". However, since the resolver had previously determined the authoritative name servers for the zone "org.", it does not need to begin the resolution process from scratch but instead start at zone "org.", thus avoiding another query to the root name servers.

There is no requirement that resolving should involve any referrals at all. Looking up "en.wikipedia.org." on the root name servers always results in referrals, but if an alternative DNS root is used which is set up to contain a record for "en.wikipedia.org.", then the record is returned on the first query.

---
title: "Root name server"
source: https://en.wikipedia.org/wiki/Root_name_server
domain: dnssec
license: CC-BY-SA-4.0
tags: dnssec dns security extensions, dns record signing, dns cache poisoning defense, dns spoofing mitigation, chain of trust validation
fetched: 2026-07-02
---

# Root name server

A **root name server** is a name server for the root zone of the Domain Name System (DNS) of the Internet. It directly answers requests for records in the root zone and answers other requests by returning a list of the authoritative name servers for the appropriate top-level domain (TLD). The root name servers are a critical part of the Internet infrastructure because they are the first step in resolving human-readable host names into IP addresses that are used in communication between Internet hosts.

A combination of limits in the DNS and certain protocols, namely the practical size of unfragmented User Datagram Protocol (UDP) packets, resulted in a decision to limit the number of root servers to thirteen server addresses. However, enabled by the use of anycast addressing, the actual number of root server instances—1954—is much larger, as of December 5, 2025.

## Root domain

The DNS is a hierarchical naming system for computers, services, or any resource participating in the Internet. The top of that hierarchy is the root domain. The root domain does not have a formal name and its label in the DNS hierarchy is an empty string. All fully qualified domain names (FQDNs) on the Internet can be regarded as ending with this empty string for the root domain, and therefore ending in a full stop character (the label delimiter), e.g., "www.example.com.". This is generally implied rather than explicit, as modern DNS software does not actually require that the terminating dot be included when attempting to translate a domain name to an IP address.

The root domain contains all top-level domains of the Internet. As of July 2015, it contained 1058 TLDs, including 730 generic top-level domains (gTLDs) and 301 country code top-level domains (ccTLDs). In addition, the root domain is used for technical name spaces in the management of Internet addressing and other resources, as well as for testing internationalized domain names.

## Resolver operation

When a computer on the Internet needs to resolve a domain name, it uses DNS resolver software to perform the lookup. A resolver breaks the name up into its labels from right to left. The first component (TLD) is queried using a root server to obtain the responsible authoritative server. Queries for each label return more specific name servers until a name server returns the answer of the original query.

In practice, most of this information does not change very often over a period of hours, and therefore it is cached by intermediate name servers or by a name cache built into the user's application. DNS lookups to the root name servers may therefore be relatively infrequent. A survey in 2003 reported that only 2% of all queries to the root servers were legitimate. Incorrect or non-existent caching was responsible for 75% of the queries, 12.5% were for unknown TLDs, and 7% were for lookups using IP addresses as if they were domain names. Some misconfigured desktop computers even tried to update the root server records for the TLDs. A similar list of observed problems and recommended fixes has been published in RFC 4697.

Although any local implementation of DNS can implement its own private root name servers, the term "root name server" is generally used to describe the thirteen well-known root name servers that implement the root name space domain for the Internet's official global implementation of the Domain Name System. Resolvers use a small 3 KB *root.hints* file published by Internic to bootstrap this initial list of root server addresses; in other words, root.hints is necessary in order to break the circular dependency of needing to know the addresses of a root name server to lookup the same address.

## Root server addresses

There are 13 logical root name servers specified, with logical names in the form *letter*.root-servers.net, where *letter* ranges from a to m. The choice of 13 name servers was made because of limitations in the original DNS specification, which specifies a maximum packet size of 512 bytes when using the User Datagram Protocol (UDP). Technically however, fourteen name servers fit into an IPv4 packet.

The addition of IPv6 addresses for the root name servers requires more than 512 bytes, which is facilitated by the EDNS0 extension to the DNS standard.

Although 13 root name servers are specified, this does not mean that there are only 13 physical servers; each operator uses redundant computer equipment so that it can continue providing reliable service even if server hardware or software fails. Additionally, all operate in multiple geographical locations using a routing technique called anycast addressing, providing increased performance and even more fault tolerance. An informational homepage exists for every logical server (except G-Root) under the Root Server Technical Operations Association domain with web address in the form http://*letter*.root-servers.org/, where *letter* ranges from a to m.

Ten servers were originally in the United States; all are now operated using anycast addressing. Three servers were originally located in Stockholm, Sweden (I-Root), Amsterdam, Netherlands (K-Root), and Tokyo, Japan (M-Root) respectively.

Older servers had their own name before the policy of using similar names was established. Since the implementation of anycast addressing, most of the physical root servers are now outside the United States, allowing for high performance worldwide. A local instance is only visible to nearby networks, for example, particular exchange points.

Letter

IPv4

address

IPv6

address

AS-number

Old name

Operator

Operator origin

Location & no. of

sites (global/local)

Software

A

198.41.0.4

2001:503:ba3e::2:30

AS19836,

AS36619, AS36620, AS36622, AS36625, AS36631, AS64820

ns.internic.net

Verisign

United States

Distributed using

anycast

34/22

NSD

and Verisign ATLAS

B

170.247.170.2

2801:1b8:10::b

AS394353

ns1.isi.edu

USC

-

ISI

United States

Distributed using

anycast

6/0

BIND

and

Knot DNS

C

192.33.4.12

2001:500:2::c

AS2149

c.psi.net

Cogent Communications

United States

Distributed using

anycast

13/0

BIND

D

199.7.91.13

2001:500:2d::d

AS10886

terp.umd.edu

University of Maryland

United States

Distributed using

anycast

23/208

NSD

E

192.203.230.10

2001:500:a8::e

AS21556

ns.nasa.gov

NASA Ames Research Center

United States

Distributed using

anycast

130/198

BIND

,

NSD

and Cloudflare

F

192.5.5.241

2001:500:2f::f

AS3557

ns.isc.org

Internet Systems Consortium

United States

Distributed using

anycast

129/225

BIND

and Cloudflare

G

192.112.36.4

2001:500:12::d0d

AS5927

ns.nic.ddn.mil

Defense Information Systems Agency

United States

Distributed using

anycast

6/0

BIND

H

198.97.190.53

2001:500:1::53

AS1508

aos.arl.army.mil

U.S. Army Research Lab

United States

Distributed using

anycast

12/0

NSD

I

192.36.148.17

2001:7fe::53

AS29216

nic.nordu.net

Netnod

Sweden

Distributed using

anycast

90/0

BIND

J

192.58.128.30

2001:503:c27::2:30

AS26415,

AS36626, AS36628, AS36632

—

N/a

Verisign

United States

Distributed using

anycast

62/86

NSD

and Verisign ATLAS

K

193.0.14.129

2001:7fd::1

AS25152

—

N/a

RIPE NCC

Netherlands

Distributed using

anycast

134/12

BIND

,

NSD

and

Knot DNS

L

199.7.83.42

2001:500:9f::42

AS20144

—

N/a

ICANN

United States

Distributed using

anycast

143/0

NSD

and

Knot DNS

M

202.12.27.33

2001:dc3::35

AS7500

—

N/a

WIDE Project

Japan

Distributed using

anycast

8/19

BIND

There are also several alternative namespace systems with an alternative DNS root using their own set of root name servers that exist in parallel to the mainstream name servers. The first, AlterNIC, generated a substantial amount of press.

The function of a root name server may also be implemented locally, or on a provider network. Such servers are synchronized with the official root zone file as published by ICANN, and do not constitute an alternate root.

As the root name servers are an important part of the Internet, they have come under attack several times, although none of the attacks have ever been serious enough to severely affect the performance of the Internet.

## Root server supervision

The DNS Root Server System Advisory Committee is an ICANN committee. ICANN's bylaws say the committee provides advice to ICANN but the committee claims no authority over the servers or server operators.

## Root zone file

The root zone file is a small (about 2 MB) data set at the apex of the Domain Name System, and its publication is the primary purpose of root name servers. It is not to be confused with the *root.hints* file used to bootstrap a resolver.

The contents of the root zone file is a list of names and numeric IP addresses of the root domain authoritative DNS servers for all top-level domains (TLDs) such as com, org, edu, and the country code top-level domains (it also includes that info for root domain, the dot). On 12 December 2004, 773 different authoritative servers for the TLDs were listed. Later the number of TLDs increased greatly. As of July 2020, the root zone consisted of 1511 useful TLDs (excluded are: 55 domains that are not assigned, 8 that are retired, and 11 test domains). Other name servers forward queries for which they do not have any information about authoritative servers to a root name server. The root name server, using its root zone file, answers with a referral to the authoritative servers for the appropriate TLD or with an indication that no such TLD exists.

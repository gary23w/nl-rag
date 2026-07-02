---
title: "IPv6 address (part 1/2)"
source: https://en.wikipedia.org/wiki/IPv6_address
domain: ipv6
license: CC-BY-SA-4.0
tags: ipv6, ipv6 address, neighbor discovery protocol, ipv6 transition
fetched: 2026-07-02
part: 1/2
---

# IPv6 address

An **Internet Protocol version 6 address** (**IPv6 address**) is a numeric label that is used to identify and locate a network interface of a computer or a network node participating in a computer network using IPv6. IP addresses are included in the packet header to indicate the source and the destination of each packet. The IP address of the destination is used to make decisions about routing IP packets to other networks.

IPv6 is the successor to the first addressing infrastructure of the Internet, Internet Protocol version 4 (IPv4). In contrast to IPv4, which defined an IP address as a 32-bit value, IPv6 addresses have a size of 128 bits. Therefore, in comparison, IPv6 has a vastly enlarged address space.


## Addressing methods

IPv6 addresses are classified by the primary addressing and routing methodologies common in networking: unicast addressing, anycast addressing, and multicast addressing.

A unicast address identifies a single network interface. The Internet Protocol delivers packets sent to a unicast address to that specific interface.

An anycast address is assigned to a group of interfaces, usually belonging to different nodes. A packet sent to an anycast address is delivered to just one of the member interfaces, typically the nearest host, according to the routing protocol's definition of distance. Anycast addresses cannot be identified easily, they have the same format as unicast addresses, and differ only by their presence in the network at multiple points. Almost any unicast address can be employed as an anycast address.

A multicast address is also used by multiple hosts that acquire the multicast address destination by participating in the multicast distribution protocol among the network routers. A packet that is sent to a multicast address is delivered to all interfaces that have joined the corresponding multicast group. IPv6 does not implement broadcast addressing. Broadcast's traditional role is subsumed by multicast addressing to the *all-nodes* link-local multicast group *ff02::1*. However, the use of the all-nodes group is not recommended, and most IPv6 protocols use protocol-specific link-local multicast groups to avoid disturbing every interface on a given network.


## Address formats

An IPv6 address consists of 128 bits. For each of the major addressing and routing methodologies, various address formats are recognized by dividing the 128 address bits into bit groups and using established rules for associating the values of these bit groups with special addressing features.

### Unicast and anycast address format

Unicast and anycast addresses are typically composed of two logical parts: a 64-bit network prefix used for routing, and a 64-bit interface identifier used to identify a host's network interface.

| bits | 48 (or more) | 16 (or fewer) | 64 |
|---|---|---|---|
| field | *routing prefix* | *subnet ID* | *interface identifier* |

The *network prefix* (the *routing prefix* combined with the *subnet ID*) is contained in the most significant 64 bits of the address. The size of the routing prefix may vary; a larger prefix size means a smaller subnet ID size. The bits of the *subnet ID* field are available to the network administrator to define subnets within the given network. The 64-bit *interface identifier* is automatically established randomly, obtained from a DHCPv6 server, or assigned manually. (Historically, it was automatically generated from the interface's MAC address using the modified EUI-64 format, but this method is now not recommended for privacy reasons.)

Unique local addresses are addresses analogous to IPv4 private network addresses.

| bits | 7 | 1 | 40 | 16 | 64 |
|---|---|---|---|---|---|
| field | *prefix* | *L* | *random* | *subnet ID* | *interface identifier* |

The *prefix* field contains the binary value 1111110. The *L* bit is one for locally assigned addresses; the address range with *L* set to zero is currently not defined. The *random* field is chosen randomly once, at the inception of the */48* routing prefix.

A link-local address is also based on the interface identifier, but uses a different format for the network prefix.

| bits | 10 | 54 | 64 |
|---|---|---|---|
| field | *prefix* | *zeroes* | *interface identifier* |

The *prefix* field contains the binary value 1111111010. The 54 zeroes that follow make the total network prefix the same for all link-local addresses (*fe80::/64* link-local address prefix), rendering them non-routable.

### Multicast address format

Multicast addresses are formed according to several specific formatting rules, depending on the application.

| bits | 8 | 4 | 4 | 112 |
|---|---|---|---|---|
| field | *prefix* | *flg* | *sc* | *group ID* |

For all multicast addresses, the *prefix* field holds the binary value 11111111.

Currently, three of the four flag bits in the *flg* field are defined; the most-significant flag bit is reserved for future use.

| bit | flag | Meaning when 0 | Meaning when 1 |
|---|---|---|---|
| 8 | *reserved* | *reserved* | *reserved* |
| 9 | R (Rendezvous) | Rendezvous point not embedded | Rendezvous point embedded |
| 10 | P (Prefix) | Without prefix information | Address based on network prefix |
| 11 | T (Transient) | Well-known multicast address | Dynamically assigned multicast address |

The four-bit scope field (*sc*) is used to indicate where the address is valid and unique.

In addition, the scope field is used to identify special multicast addresses, like solicited node.

| bits | 8 | 4 | 4 | 79 | 9 | 24 |
|---|---|---|---|---|---|---|
| field | *prefix* | *flg* | *sc* | *zeroes* | *ones* | *unicast address* |

The *sc(ope)* field holds the binary value 0010 (link-local). Solicited-node multicast addresses are computed as a function of a node's unicast or anycast addresses. A solicited-node multicast address is created by copying the last 24 bits of a unicast or anycast address to the last 24 bits of the multicast address.

Unicast-prefix–based multicast address format

bits

8

4

4

4

4

8

64

32

field

prefix

flg

sc

res

riid

plen

network prefix

group ID

Link-scoped multicast addresses use a comparable format.


## Representation

An IPv6 address is represented as eight groups of four hexadecimal digits, each group representing 16 bits The groups are separated by colons (:). An example of an IPv6 address is:

2001:0db8:85a3:0000:0000:8a2e:0370:7334

The standards provide flexibility in the representation of IPv6 addresses. The full representation of eight four-digit groups may be simplified by several techniques, eliminating parts of the representation. In general, representations are shortened as much as possible. However, this practice complicates several common operations, namely searching for a specific address or an address pattern in text documents or streams, and comparing addresses to determine equivalence. For mitigation of these complications, the Internet Engineering Task Force (IETF) has defined a canonical format for rendering IPv6 addresses in text:

- The hexadecimal digits are always compared in a case-insensitive manner, but IETF recommendations suggest the use of only lower case letters. For example, *2001:db8::1* is preferred over *2001:DB8::1*;
- Leading zeros in each 16-bit field are suppressed, but each group must retain at least one digit. For example, *2001:0db8::0001:0000* is rendered as *2001:db8::1:0*;
- The longest sequence of consecutive all-zero fields is replaced with two colons (*::*). If the address contains multiple runs of all-zero fields of the same size, to prevent ambiguities, it is the leftmost that is compressed. For example, *2001:db8:0:0:1:0:0:1* is rendered as *2001:db8::1:0:0:1* rather than as *2001:db8:0:0:1::1*. *::* is not used to represent just a single all-zero field. For example, *2001:db8:0:0:0:0:2:1* is shortened to *2001:db8::2:1*, but *2001:db8:0000:1:1:1:1:1* is rendered as *2001:db8:0:1:1:1:1:1*.

These methods can lead to very short representations for IPv6 addresses. For example, the localhost (loopback) address, *0:0:0:0:0:0:0:1*, and the IPv6 unspecified address, *0:0:0:0:0:0:0:0*, are reduced to *::1* and *::*, respectively.

During the transition of the Internet from IPv4 to IPv6, it is typical to operate in a mixed addressing environment. For such use cases, a special notation has been introduced, which expresses IPv4-mapped and IPv4-compatible IPv6 addresses by writing the least-significant 32 bits of an address in the familiar IPv4 dot-decimal notation, whereas the 96 most-significant bits are written in IPv6 format. For example, the IPv4-mapped IPv6 address *::ffff:c000:0280* is written as *::ffff:192.0.2.128*, thus expressing clearly the original IPv4 address that was mapped to IPv6.

### Networks

An IPv6 network uses an address block that is a contiguous group of IPv6 addresses of a size that is a power of two. The leading set of bits of the addresses are identical for all hosts in a given network, and are called the network's address or routing *prefix*.

Network address ranges are written in CIDR notation. A network is denoted by the first address in the block (ending in all zeroes), a slash (/), and a decimal value equal to the size in bits of the prefix. For example, the network written as *2001:db8:1234::/48* starts at address *2001:db8:1234:0000:0000:0000:0000:0000* and ends at *2001:db8:1234:ffff:ffff:ffff:ffff:ffff*.

The routing prefix of an interface address may be directly indicated with the address using CIDR notation. For example, the configuration of an interface with address *2001:db8:a::123* connected to subnet *2001:db8:a::/64* is written as *2001:db8:a::123/64*.

### Address block sizes

The size of a block of addresses is specified by writing a slash (/) followed by a number in decimal whose value is the length of the network prefix in bits. For example, an address block with 48 bits in the prefix is indicated by */48*. Such a block contains 2128 − 48 = 280 addresses. The smaller the length of the network prefix, the larger the block: a */21* block is 8 times larger than a */24* block.

### Literal IPv6 addresses in network resource identifiers

Colon (:) characters in IPv6 addresses may conflict with the established syntax of resource identifiers, such as URIs and URLs. The colon is conventionally used to terminate the host path before a port number. To alleviate this conflict, literal IPv6 addresses are enclosed in square brackets in such resource identifiers, for example:

http://[2001:db8:85a3:8d3:1319:8a2e:370:7348]/

When the URL also contains a port number the notation is:

https://[2001:db8:85a3:8d3:1319:8a2e:370:7348]:443/

where the trailing 443 is the example's port number.

### Scoped literal IPv6 addresses (with zone index)

For addresses with other than global scope (as described in § Address scopes), and in particular for link-local addresses, the choice of the network interface for sending a packet may depend on which zone the address belongs to. The same address may be valid in different zones, and in use by a different host in each of those zones. Even if a single address is not in use in different zones, the address prefixes for addresses in those zones may still be identical, which makes the operating system unable to select an outgoing interface based on the information in the routing table (which is prefix-based).

In order to resolve the ambiguity in textual addresses, a *zone index* must be appended to the address. The zone index is separated from the address by a percent sign (%). Although numeric zone indices must be universally supported, the zone index may also be an implementation-dependent string. The link-local address

fe80::1ff:fe23:4567:890a

could be expressed by

fe80::1ff:fe23:4567:890a%eth2

or

fe80::1ff:fe23:4567:890a%3

The former (using an interface name) is customary on most Unix-like operating systems (e.g., BSD, Linux, macOS). The latter (using an interface number) is the only syntax on Microsoft Windows, but as support for this syntax is mandatory per standard, it is also available on other operating systems.

BSD-based operating systems (including macOS) also support an alternative, non-standard syntax, where a numeric zone index is encoded in the second 16-bit word of the address. E.g.:

fe80:3::1ff:fe23:4567:890a

In all operating systems mentioned above, the zone index for link-local addresses actually refers to an interface, not to a zone. As multiple interfaces may belong to the same zone (e.g. when connected to the same network), in practice two addresses with different zone identifiers may actually be equivalent, and refer to the same host on the same link.

When used in uniform resource identifiers (URI), the use of the percent sign causes a syntax conflict, therefore it must be escaped via percent-encoding, e.g.:

http://[fe80::1ff:fe23:4567:890a

%25

eth0]/

### Literal IPv6 addresses in UNC path names

In Microsoft Windows operating systems, IPv4 addresses are valid location identifiers in Uniform Naming Convention (UNC) path names. However, the colon is an illegal character in a UNC path name. Thus, the use of IPv6 addresses is also illegal in UNC names. For this reason, Microsoft implemented a transcription algorithm to represent an IPv6 address in the form of a domain name that can be used in UNC paths. For this purpose, Microsoft registered and reserved the second-level domain *ipv6-literal.net* on the Internet (although they gave up the domain in January 2014). IPv6 addresses are transcribed as a hostname or subdomain name within this namespace, in the following fashion:

2001:db8:85a3:8d3:1319:8a2e:370:7348

is written as

2001-db8-85a3-8d3-1319-8a2e-370-7348.ipv6-literal.net

This notation is automatically resolved locally by Microsoft software, without any queries to DNS name servers.

If the IPv6 address contains a zone index, it is appended to the address portion after an 's' character:

fe80::1ff:fe23:4567:890a%3

is written as

fe80--1ff-fe23-4567-890a

s3

.ipv6-literal.net


## Address scopes

Every IPv6 address, except the unspecified address (*::*), has a *scope*, which specifies in which part of the network it is valid.

### Unicast

For unicast addresses, two scopes are defined: link-local and global.

Link-local addresses and the loopback address have *link-local* scope, which means they can only be used on a single directly attached network. All other addresses (including unique local addresses) have *global* (or *universal*) scope, which means they are potentially globally routable and can be used to connect to addresses with *global* scope anywhere, or to addresses with *link-local* scope on the directly attached network.

Unique local addresses have global scope, but they are not globally administered. As a result, only other hosts in the same administrative domain (e.g., an organization), or within a cooperating administrative domain are able to reach such addresses, if properly routed. As their scope is global, these addresses are valid as a source address when communicating with any other global-scope address, even though it may be impossible to route packets from the destination back to the source.

### Anycast

Anycast addresses are syntactically identical to and indistinguishable from unicast addresses. Their only difference is administrative. Scopes for anycast addresses are therefore the same as for unicast addresses.

### Multicast

For multicast addresses, the four least-significant bits of the second address octet (*ff0s::*) identify the address scope, i.e. the domain in which the multicast packet should be propagated. Predefined and reserved scopes are:

| Value | Scope name | Notes |
|---|---|---|
| 0x0 | *reserved* |   |
| 0x1 | interface-local | Interface-local scope spans only a single interface on a node, and is useful only for loopback transmission of multicast. |
| 0x2 | link-local | Link-local scope spans the same topological region as the corresponding unicast scope. |
| 0x3 | realm-local | Realm-local scope is defined as larger than link-local, automatically determined by network topology and must not be larger than the following scopes. |
| 0x4 | admin-local | Admin-local scope is the smallest scope that must be administratively configured, i.e., not automatically derived from physical connectivity or other, non-multicast-related configuration. |
| 0x5 | site-local | Site-local scope is intended to span a single site belonging to an organisation. |
| 0x8 | organization-local | Organization-local scope is intended to span all sites belonging to a single organization. |
| 0xe | global | Global scope spans all reachable nodes on the Internet – it is unbounded. |
| 0xf | *reserved* |   |

All other scopes are unassigned and available to administrators for defining additional regions.


## Address space

### General allocation

The management of IPv6 address allocation process is delegated to the Internet Assigned Numbers Authority (IANA) by the Internet Architecture Board and the Internet Engineering Steering Group. Its main function is the assignment of large address blocks to the regional Internet registries (RIRs), which have the delegated task of allocation to network service providers and other local registries. The IANA has maintained the official list of allocations of the IPv6 address space since December 1995.

In order to allow efficient route aggregation, thereby reducing the size of the Internet routing tables, only one-eighth of the total address space (*2000::/3*) is currently allocated for use on the Internet. The rest of the IPv6 address space is reserved for future use or for special purposes. The address space is assigned to the RIRs in blocks of */23* up to */12*.

The RIRs assign smaller blocks to local Internet registries that distribute them to users. These are typically in sizes from */19* to */32*. Global unicast assignment records can be found at the various RIRs or other websites.

The addresses are then typically distributed in */48* to */56* sized blocks to the end users. IPv6 addresses are assigned to organizations in much larger blocks as compared to IPv4 address assignments—the recommended allocation is a */48* block which contains 280 addresses, being 248 or about 2.8×1014 times larger than the entire IPv4 address space of 232 addresses and about 7.2×1016 times larger than the */8* blocks of IPv4 addresses, which are the largest allocations of IPv4 addresses. The total pool, however, is sufficient for the foreseeable future, because there are 2128 (exactly 340,282,366,920,938,463,463,374,607,431,768,211,456; or about 3.4×1038, or 340 undecillion) unique IPv6 addresses.

Each RIR can divide each of its multiple */23* blocks into 512 */32* blocks, typically one for each ISP; an ISP can divide its */32* block into 65536 */48* blocks, typically one for each customer; customers can create 65536 */64* networks from their assigned */48* block, each having 264 (exactly 18,446,744,073,709,551,616; or about 1.8×1019) addresses. In contrast, the entire IPv4 address space has only 232 (exactly 4,294,967,296; or about 4.3×109) addresses.

By design, only a small fraction of the address space will be used actively. The large address space ensures that addresses are almost always available, which makes the use of network address translation (NAT) for the purposes of address conservation unnecessary. NAT has been increasingly used for IPv4 networks to help alleviate IPv4 address exhaustion.

### Special allocation

Provider-independent address space is assigned directly to the end user by the RIRs from the special range (*2001:678::/29* for assignees in the RIPE NCC service region) and allows customers to make provider changes without renumbering their networks.

Internet exchange points (IXPs) are assigned special addresses from the ranges *2001:7f8::/32*, *2001:504::/30*, and *2001:7fa::/32* for communication with their connected ISPs.

Root name servers have mostly been assigned addresses from the ranges *2001:500::/30* and *2001:7f8::/29*.

### Reserved anycast addresses

The lowest address within each subnet prefix (the interface identifier set to all zeroes) is reserved as the *subnet-router* anycast address. Applications may use this address when talking to any one of the available routers, as packets sent to this address are delivered to just one router.

The 128 highest addresses within each */64* subnet prefix are reserved to be used as anycast addresses. These addresses usually have the first 57 bits of the interface identifier set to 1, followed by the 7-bit anycast ID. Prefixes for the network can be of any length for routing purposes, but subnets are required to have a length of 64 bits. The address with value 0x7e in the 7 least-significant bits is defined as a mobile IPv6 home agents anycast address. The address with value 0x7f (all bits 1) is reserved and may not be used. No more assignments from this range have been made, so all the remaining values, 0x00 through 0x7d, are reserved as well.


## Special addresses

There are a number of addresses with special meaning in IPv6. The IANA maintains a registry of these special-purpose addresses. They represent less than 2% of the entire address space:

| Address block (CIDR) | First address | Last address | Number of addresses | Usage | Purpose |
|---|---|---|---|---|---|
| ::/128 | :: | :: | 1 | Software | Unspecified address |
| ::1/128 | ::1 | ::1 | 1 | Host | Loopback address—a virtual interface that loops all traffic back to itself, the *localhost* |
| ::ffff:0:0/96 | ::ffff:0.0.0.0 ::ffff:0:0 | ::ffff:255.255.255.255 ::ffff:ffff:ffff | 232 | Software | IPv4-mapped addresses |
| 64:ff9b::/96 | 64:ff9b::0.0.0.0 64:ff9b::0:0 | 64:ff9b::255.255.255.255 64:ff9b::ffff:ffff | 232 | The global Internet | NAT64 IPv4/IPv6 translation |
| 64:ff9b:1::/48 | 64:ff9b:1:: | 64:ff9b:1:ffff:ffff:ffff:ffff:ffff | 280, with 248 for each IPv4 | Private internets | Local-use IPv4/IPv6 translation |
| 100::/64 | 100:: | 100::ffff:ffff:ffff:ffff | 264 | Routing | Discard prefix |
| 2001::/32 | 2001:: | 2001:0:ffff:ffff:ffff:ffff:ffff:ffff | 296 | The global Internet | Teredo tunneling |
| 2001:20::/28 | 2001:20:: | 2001:2f:ffff:ffff:ffff:ffff:ffff:ffff | 2100 | Software | ORCHIDv2 |
| 2001:db8::/32 | 2001:db8:: | 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff | 296 | Documentation | Addresses used in documentation and example source code |
| 2002::/16 | 2002:: | 2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff | 2112 | The global Internet | The 6to4 addressing scheme |
| 3fff::/20 | 3fff:: | 3fff:0fff:ffff:ffff:ffff:ffff:ffff:ffff | 2108 | Documentation | Addresses used in documentation and example source code |
| 5f00::/16 | 5f00:: | 5f00:ffff:ffff:ffff:ffff:ffff:ffff:ffff | 2112 | Routing | IPv6 Segment Routing (SRv6) |
| fc00::/7 | fc00:: | fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | 2121 | Private internets | Unique local address Note L bit equal to 0 is reserved, so currently the first address is fd00::, for 2120 addresses. |
| fe80::/64 from fe80::/10 | fe80:: | fe80::ffff:ffff:ffff:ffff | 264 | Link | Link-local address |
| ff00::/8 | ff00:: | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | 2120 | The global Internet | Multicast address |

In the past *::ffff:0:0.0.0.0/96* (*::ffff:0:0:0/96*) was considered for IPv4/IPv6 translation, but it is no longer reserved.

### Unicast addresses

#### Unspecified address

- *::/128* – The address with all zero bits is called the *unspecified address* (corresponding to *0.0.0.0/32* in IPv4). This address must never be assigned to an interface and is to be used only in software before the application has learned its host's source address appropriate for a pending connection. Routers must not forward packets with the unspecified address.

Applications may listen on one or more specific interfaces for incoming connections, which are shown in listings of active internet connections by a specific IP address (and a port number, separated by a colon). When the unspecified address is shown it means that an application is listening for incoming connections on all available interfaces.

In routing table configuration, the unspecified address may be used to represent the default route address (corresponding to *0.0.0.0/0* in IPv4) for destination addresses (unicast, multicast and others) not specified elsewhere in a routing table.

#### Local addresses

- *::1/128* – The loopback address is a unicast localhost address. This address corresponds to *127.0.0.1/8* in IPv4. If an application in a host sends packets to this address, the IPv6 stack loops these packets back on the same virtual interface.
- *fe80::/10* – Addresses in the link-local prefix are only valid and unique on the local subnet. This address range is comparable to the auto-configuration addresses *169.254.0.0/16* of IPv4. Within this prefix only one */64* subnet is allocated (there are 54 zero bits), yielding an effective format of *fe80::/64*. The least significant 64 bits were previously chosen as the interface hardware address constructed in modified EUI-64 format, but are now pseudo-random values for privacy. A link-local address is required on every IPv6-enabled interface and applications may rely on the existence of a link-local address even when there is no IPv6 routing.

#### Unique local addresses

- *fc00::/7* — Unique local addresses (ULAs) are intended for local communication (comparable to IPv4 private addresses *10.0.0.0/8*, *172.16.0.0/12* and *192.168.0.0/16*). They are routable only within a set of cooperating sites. The block is split into two halves. The lower half of the block (*fc00::/8*) was intended for globally allocated prefixes, but an allocation method has yet to be defined. The upper half (*fd00::/8*) is used for *probabilistically unique* addresses in which the */8* prefix is combined with a 40-bit locally generated pseudorandom number to obtain a */48* private prefix. The procedure for selecting a 40-bit number results in only a negligible chance that two sites that wish to merge or communicate encounter address collisions, but can use the same */48* prefix.

#### Transition from IPv4

- *::ffff:0:0/96* — This prefix is used for IPv6 transition mechanisms and designated as an *IPv4-mapped IPv6 address*. With a few exceptions, this address type allows the transparent use of the transport layer protocols over IPv4 through the IPv6 networking application programming interface. In this dual-stack configuration, server applications only need to open a single listening socket to handle connections from clients using IPv6 or IPv4 protocols. IPv6 clients are handled natively by default, and IPv4 clients appear as IPv6 clients at their IPv4-mapped IPv6 address. Transmission is handled similarly; established sockets may be used to transmit IPv4 or IPv6 datagram, based on the binding to an IPv6 address, or an IPv4-mapped address.
- *::ffff:0:0:0/96* — A prefix used for *IPv4-translated addresses*. These are used by the Stateless IP/ICMP Translation (SIIT) protocol.
- *64:ff9b::/96* — The *well-known prefix*. Addresses with this prefix are used for automatic IPv4/IPv6 translation.
- *64:ff9b:1::/48* — A prefix for locally translated IPv4/IPv6 addresses. Addresses with this prefix can be used for multiple IPv4/IPv6 translation mechanisms like NAT64 and SIIT. Compared to *64:ff9b::/96*, these addresses contain their translated IPv4 address in positions 48-63 and 72–87. This means that for every IPv4 address a */88* IPv6 prefix is assigned to the device. This enables similar use cases as 6to4, where a single public IPv4 address gets translated into a prefix. This way, only one level of NAT is required and the devices do not need to do NAT66 internally if they need additional addresses, e.g. for P2P interfaces or docker containers.
- *2002::/16* — This prefix was used for 6to4 addressing (prefix from the IPv4 network, *192.88.99.0/24*, was also used). The 6to4 addressing scheme is deprecated.

#### Special-purpose addresses

IANA has reserved a so-called *Sub-TLA ID* address block for special assignments of *2001::/23* (split into the range of 64 network prefixes *2001:0000::/29* through *2001:01f8::/29*). The following assignments from this block currently exist:

- *2001::/32* — Used for Teredo tunneling, an IPv6 transition mechanism.
- *2001:1::1/128* — Port Control Protocol Anycast
- *2001:1::2/128* — Traversal Using Relays around NAT Anycast
- *2001:1::3/128* — DNS-SD Service Registration Protocol Anycast
- *2001:2::/48* — Used for benchmarking IPv6. Corresponds with *198.18.0.0/15* used for benchmarking IPv4. Assigned to the Benchmarking Methodology Working Group (BMWG).
- *2001:3::/32* — Automatic Multicast Tunneling, Relay Discovery
- *2001:20::/28* — Overlay Routable Cryptographic Hash Identifiers (ORCHIDv2). These are non-routed IPv6 addresses used for cryptographic hashes.
- *2001:30::/28* — Drone Remote ID Protocol Entity Tags (DETs) Prefix

Furthermore, IANA has reserved the following two IPv6 prefixes for AS112 nameserver operations:

- *2620:4f:8000::/48* — Blackhole servers with the traditional authoritative zones configured
- *2001:4:112::/48* — Blackhole servers for the new blackholing approach involving DNAME records to *empty.as112.arpa*

#### Documentation

- *2001:db8::/32* — This prefix is used in documentation, anywhere an example IPv6 address is given or model networking scenarios are described.
- *3fff::/20* — This documentation prefix was allocated in 2024 to account for modern-day large-scale network modelling, that cannot be covered by a single */32* prefix.

#### Discard

- *100::/64* — This prefix is used for discarding traffic.

#### Deprecated and obsolete

See § Deprecated and obsolete addresses

### Multicast addresses

The multicast addresses *ff0x::*, where *x* is any hexadecimal value, are reserved and managed by the Internet Assigned Numbers Authority (IANA).

| Address | Description | Available scopes |
|---|---|---|
| *ff0x::1* | All nodes address, identify the group of all IPv6 nodes | Available in scope 1 (interface-local) and 2 (link-local): *ff01::1* → All nodes in the interface-local *ff02::1* → All nodes in the link-local |
| *ff0x::2* | All routers | Available in scope 1 (interface-local), 2 (link-local) and 5 (site-local): *ff01::2* → All routers in the interface-local *ff02::2* → All routers in the link-local *ff05::2* → All routers in the site-local |
| *ff02::5* | OSPFIGP | 2 (link-local) |
| *ff02::6* | OSPFIGP designated routers | 2 (link-local) |
| *ff02::9* | RIP routers | 2 (link-local) |
| *ff02::a* | EIGRP routers | 2 (link-local) |
| *ff02::c* | Web Services Dynamic Discovery | 2 (link-local) |
| *ff02::d* | All PIM routers | 2 (link-local) |
| *ff02::1a* | All RPL routers | 2 (link-local) |
| *ff02::16* | All MLDv2-capable routers | 2 (link-local) |
| *ff0x::fb* | mDNSv6 | Available in all scopes |
| *ff0x::101* | All NTP servers | Available in all scopes |
| *ff02::1:1* | Link name | 2 (link-local) |
| *ff02::1:2* | All DHCPv6 servers and relay agents | 2 (link-local) |
| *ff02::1:3* | Link-local multicast name resolution | 2 (link-local) |
| *ff05::1:3* | A relay agent may use this address to reach all DHCPv6 servers in the site. | 5 (site-local) |
| *ff02::1:ff00:0/104* | Solicited-node multicast address (see below) | 2 (link-local) |
| *ff02::2:ff00:0/104* | Node information queries | 2 (link-local) |

#### Solicited-node multicast address

The least significant 24 bits of the solicited-node multicast address group ID are filled with the least significant 24 bits of the interface's unicast or anycast address. These addresses allow link-layer address resolution via Neighbor Discovery Protocol (NDP) on the link without disturbing all nodes on the local network. A host is required to join a solicited-node multicast group for each of its configured unicast or anycast addresses.


## Stateless address autoconfiguration (SLAAC)

On system startup, a node automatically creates a link-local address on each IPv6-enabled interface, even if globally routable addresses are manually configured or obtained through *configuration protocols* (see below). It does so independently and without any prior configuration by **stateless address autoconfiguration** (**SLAAC**), using a component of the Neighbor Discovery Protocol. This address is selected with the prefix *fe80::/64*.

In IPv4, typical *configuration protocols* include DHCP or PPP. Newer IPv6 hosts can be configured to use the Neighbor Discovery Protocol to create a globally routable unicast address: the host sends router solicitation requests and an IPv6 router responds with a prefix assignment. Other ways to automatically assign IPv6 addresses involve a DHCPv6 server, either in stateless mode, where the server gives the required network parameters for the hosts to generate their own global addresses, or in stateful mode, where the server assigns the global addresses and other required parameters.

### Interface identifier

The lower 64 bits of the *fe80::/64* address are populated with a 64-bit interface identifier. It can be derived from these sources:

- As the name "interface identifier" suggests, it can be the network adapter's 48-bit MAC address, which is guaranteed to be unique. A MAC address *00-0C-29-0C-47-D5* is turned into a 64-bit modified EUI-64 by first inserting *FF-FE* in the middle: *00-0C-29-FF-FE-0C-47-D5*, and then inverting the *Universal/Local* bit, becoming *02-0C-29-FF-FE-0C-47-D5* (or *:020c:29ff:fe0c:47d5* in IPv6 address notation).
- However, using the real MAC address of the adapter to derive the interface address is now discouraged in end user devices because it exposes the MAC address to the wider Internet, making it easier to track the user across networks. As a result, it is now common to instead use a *pseudorandom* address. Existing options include the *temporary address*, the *stable privacy address*, and the *cryptographically generated address*. This is related to, but not the same mechanism as, MAC spoofing; the pseudo-random interface identifier does not need to match the MAC address, real or spoofed.

#### Temporary addresses

The globally unique and static MAC addresses used by stateless address autoconfiguration to create interface identifiers offer an opportunity to track user equipment across time and IPv6 network prefix changes. To reduce the prospect of a user identity being permanently tied to an IPv6 address portion, a node may create temporary addresses with interface identifiers based on time-varying random bit strings and relatively short lifetimes (hours to days), after which they are replaced with new addresses.

Temporary addresses may be used as source addresses for originating connections, while external hosts use a public address by querying the Domain Name System (DNS).

Network interfaces configured for IPv6 use temporary addresses by default in OS X Lion and later Apple systems as well as in Windows Vista, Windows 2008 Server and later Microsoft systems.

#### Cryptographically generated addresses

As a means to enhance security for Neighbor Discovery Protocol *cryptographically generated addresses* (CGAs) were introduced in 2005 as part of the Secure Neighbor Discovery (SEND) protocol.

Such an address is generated using two hash functions that take several inputs. The first uses a public key and a random modifier; the latter being incremented repeatedly until a specific amount of zero bits of the resulting hash is acquired. The second hash function takes the network prefix and the previous hash value. The least significant 64 bits of the second hash result is appended to the 64-bit network prefix to form a 128-bit address.

The hash functions can also be used to verify if a specific IPv6 address satisfies the requirement of being a valid CGA. This way, communication can be set up between trusted addresses exclusively.

#### Stable privacy addresses

The use of the modified EUI-64 format has serious implications for security and privacy concerns, because the underlying hardware address (most typically the MAC address which by default includes an organizationally unique identifier (OUI) that identifies the manufacturer of either the whole device or the network adapter) is exposed beyond the local network, permitting the tracking of user activities and correlation of user accounts to other information, and the tailoring of security attacks specific to the device's manufacturer if the OUI refers to the whole device's manufacturer. Modified EUI-64 also reduces the size of the address space for searching for attack targets.

Stable privacy addresses were introduced to remedy these shortcomings. They are stable within a specific network but change when moving to another, to improve privacy. They are chosen deterministically, but randomly, in the entire address space of the network.

Generation of a stable privacy address is based on a hash function that uses several stable parameters. It is implementation specific, but it is recommended to include at least the network prefix, the name of the network interface, a duplicate address counter, and a secret key. The resulting hash value is used to construct the final address: Typically the 64 least significant bits are concatenated to the 64-bit network prefix, to yield a 128-bit address. If the network prefix is smaller than 64 bits, more bits of the hash are used. If the resulting address does not conflict with existing or reserved addresses, it is assigned to the interface. Conflicts are resolved by adjusting the duplicate address counter.

### Neighbor Discovery Protocol operation

#### Solicited-node multicast address

Each interface in SLAAC also has a solicited-node multicast address, formed from the network prefix *ff02::1:ff00:0/104* and the 24 least significant bits of its unicast or anycast address. This multicast address is used in NDP to detect duplicate addresses and to establish the correspondence between IP addresses and link-layer (MAC) addresses.

#### Duplicate address detection

The use of non-hardware-derived addresses presents a possibility of duplicate addresses. The assignment of a unicast IPv6 address to an interface involves an internal test for the uniqueness of that address using *Neighbor Solicitation* and *Neighbor Advertisement* (ICMPv6 type 135 and 136) messages. While in the process of establishing uniqueness an address has a *tentative* state.

The node joins the *solicited-node* multicast address for the tentative address and sends neighbor solicitations, with the tentative address as the target address and the unspecified address (*::/128*) as its source address. The node also joins the all-hosts multicast address *ff02::1*, so it can receive *neighbor advertisements*.

If a node receives a neighbor solicitation with its own tentative address as the target address, then it knows its address is not unique. The same is true if the node receives a neighbor advertisement with the tentative address as the source of the advertisement. Only after having successfully established that an address is unique may it be assigned and used by an interface.

When an anycast address is assigned to an interface (e.g. a subnet-router anycast address), due to the inherent non-uniqueness of this type of address, duplicate address detection is not performed.

#### Router operation

In NDP the router also advertises what /64-sized prefix it has access to on the broader Internet as well as other network parameters. A node that receives this information joins the prefix with its own interface identifier to obtain its unicast address on the broader Internet. For example, if a router has access to *2001:db8:1:2::/64* and the machine has the interface identifier `02-0C-29-FF-FE-0C-47-D5` (continuing the above example), the machine would self-assign the address *2001:db8:1:2:020c:29ff:fe0c:47d5*.

DHCPv6 remains useful for other purposes. For example, it can be used by the ISP's router to hand a /64-sized or shorter prefix to the customer's router, a process called prefix delegation.

#### Address lifetime

Each IPv6 address that is bound to an interface has a defined lifetime. Lifetimes are infinite, unless configured to a shorter period. There are two lifetimes that govern the state of an address: the *preferred lifetime* and the *valid lifetime*. Lifetimes can be configured in routers that provide the values used for autoconfiguration, or specified when manually configuring addresses on interfaces.

When an address is assigned to an interface it gets the status *preferred*, which it holds during its preferred-lifetime. After that lifetime expires the status becomes *deprecated* and no new connections *should* be made using this address. The address becomes *invalid* after its valid-lifetime also expires; the address is removed from the interface and may be assigned somewhere else on the Internet.


## Default address selection

IPv6-enabled network interfaces usually have more than one IPv6 address, for example, a link-local and a global address. They may also have temporary addresses that change after a certain lifetime has expired. IPv6 introduces the concepts of address scope and selection preference, yielding multiple choices for source and destination addresses in communication with another host.

The preference selection algorithm selects the most appropriate address to use in communications with a particular destination, including the use of IPv4-mapped addresses in dual-stack implementations. It uses a configurable preference table that associates each routing prefix with a precedence level. The default table has the following content:

| Prefix | Precedence | Label | Usage |
|---|---|---|---|
| ::1/128 | 50 | 0 | Localhost |
| ::/0 | 40 | 1 | Default unicast |
| ::ffff:0:0/96 | 35 | 4 | IPv4-mapped IPv6 address |
| 2002::/16 | 30 | 2 | 6to4 |
| 2001::/32 | 5 | 5 | Teredo tunneling |
| fc00::/7 | 3 | 13 | Unique local address |
| ::/96 | 1 | 3 | IPv4-compatible addresses (deprecated) |
| fec0::/10 | 1 | 11 | Site-local address (deprecated) |
| 3ffe::/16 | 1 | 12 | 6bone (returned) |

The default configuration places preference on IPv6 usage, and selects destination addresses within the smallest possible scope, so that link-local communication is preferred over globally routed paths when otherwise equally suitable. The prefix policy table is similar to a routing table, with the (inverse) precedence value serving as the role of a link cost; larger values result in higher precedence. Source addresses are preferred to have the same label value as the destination address. Addresses are matched to prefixes based on the longest-matching most-significant bit sequence. Candidate source addresses are obtained from the operating system and candidate destination addresses may be queried via DNS.

To minimize the time to establish a connection when multiple addresses are available for communication, the Happy Eyeballs algorithm was devised. It queries DNS for IPv6 and IPv4 addresses of the target host, sorts candidate addresses using the default address selection table, and tries to establish connections in parallel. The first established connection aborts current and future attempts to connect to other addresses.


## Domain Name System

In the Domain Name System, hostnames are mapped to IPv6 addresses by *AAAA* resource records, so-called *quad-A* records. For reverse lookup the IETF reserved the domain ip6.arpa, where the name space is hierarchically divided by the 1-digit hexadecimal representation of nibble units (4 bits) of the IPv6 address.

As in IPv4, each host is represented in the DNS by two DNS records: an address record and a reverse mapping pointer record. For example, a host computer named *derrick* in zone *example.com* has the unique local address *fdda:5cc1:23:4::1f*. Its quad-A address record is

```
 derrick.example.com.  IN  AAAA  fdda:5cc1:23:4::1f
```

and its IPv6 pointer record is

```
 f.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.0.0.0.3.2.0.0.1.c.c.5.a.d.d.f.ip6.arpa.  IN  PTR   derrick.example.com.
```

This pointer record may be defined in a number of zones, depending on the chain of delegation of authority in the zone d.f.ip6.arpa.

The DNS protocol is independent of its transport layer protocol. Queries and replies may be transmitted over IPv6 or IPv4 transports regardless of the address family of the data requested.

| NAME | Domain name |
|---|---|
| TYPE | AAAA (28) |
| CLASS | Internet (1) |
| TTL | Time to live, in seconds |
| RDLENGTH | Length of RDATA field |
| RDATA | 128-bit IPv6 address in network byte order |

---
title: "Classless Inter-Domain Routing"
source: https://en.wikipedia.org/wiki/Variable-length_subnet_masking
domain: cidr-subnetting
license: CC-BY-SA-4.0
tags: cidr, subnetting, classless inter-domain routing, supernetwork
fetched: 2026-07-02
---

# Classless Inter-Domain Routing

(Redirected from

Variable-length subnet masking

)

**Classless Inter-Domain Routing** (**CIDR** pronounced "cider" or /ˈsɪdər/ *SID-ər*) is a method for allocating IP addresses for IP routing. The Internet Engineering Task Force introduced CIDR in 1993 to replace the previous classful network addressing architecture on the Internet. Its goal was to slow the growth of routing tables on routers across the Internet, and to help slow the rapid exhaustion of IPv4 addresses.

IP addresses are described as consisting of two groups of bits in the address: the most significant bits are the network prefix, which identifies a whole network or subnet, and the least significant set forms the *host identifier*, which specifies a particular interface of a host on that network. This division is used as the basis of traffic routing between IP networks and for address allocation policies.

Whereas classful network design for IPv4 sized the network prefix as one or more eight-bit groups, resulting in the blocks of Class A, B, or C addresses, under CIDR address space, is allocated to Internet service providers (ISPs) and end users on any address-bit boundary. In IPv6, however, the interface identifier has a fixed size of 64 bits by convention, and smaller subnets are never allocated to end users.

CIDR is based on **variable-length subnet masking** (**VLSM**), in which network prefixes have variable length as opposed to the fixed-length prefixing of the previous classful network design. The main benefit of this is that it grants finer control of the sizes of subnets allocated to organizations, hence slowing the exhaustion of IPv4 addresses from the allocation of larger subnets than needed. CIDR gave rise to a new way of writing IP addresses known as CIDR notation, in which an IP address is followed by a suffix indicating the number of bits of the prefix. Some examples of CIDR notation are the addresses *192.0.2.0/24* for IPv4 and *2001:db8::/32* for IPv6. Blocks of addresses having contiguous prefixes may be aggregated as supernets, reducing the number of entries in the global routing table.

## Background

Each IP address consists of a network prefix followed by a host identifier. In the classful network architecture of IPv4, the three most significant bits of the 32-bit IP address defined the size of the network prefix for unicast networking, and determined the network class A, B, or C.

| Class | Most-significant bits | Network prefix length (bits) | Host identifier length (bits) | Address range |
|---|---|---|---|---|
| A | 0 | 8 | 24 | 0.0.0.0–127.255.255.255 |
| B | 10 | 16 | 16 | 128.0.0.0–191.255.255.255 |
| C | 110 | 24 | 8 | 192.0.0.0–223.255.255.255 |
| D(multicast) | 1110 | —N/a | —N/a | 224.0.0.0–239.255.255.255 |
| E(reserved) | 1111 | —N/a | —N/a | 240.0.0.0–255.255.255.255 |

The advantage of this system is that the network prefix can be determined for any IP address without any further information. The disadvantage is that networks were usually too big or too small for most organizations to use, because only three sizes were available. The smallest allocation and routing block contained 28 = 256 addresses, larger than necessary for personal or department networks, but too small for most enterprises. The next larger block contained 216 = 65536 addresses, too large to be used efficiently even by large organizations. But for network users who needed more than 65536 addresses, the only other size (224) provided far too many, more than 16 million. This led to inefficiencies in address use as well as inefficiencies in routing, because it required a large number of allocated class-C networks with individual route announcements, being geographically dispersed with little opportunity for route aggregation.

Within a decade after the invention of the Domain Name System (DNS), the classful network method was found not scalable. This led to the development of subnetting and CIDR. The formerly meaningful class distinctions based on the most-significant address bits were abandoned and the new system was described as "classless", in contrast to the old system, which became known as "classful". Routing protocols were revised to carry not just IP addresses, but also their subnet masks. Implementing CIDR required every host and router on the Internet to be reprogrammed in small ways—no small feat at a time when the Internet was entering a period of rapid growth. In 1993, the Internet Engineering Task Force published a new set of standards, RFC 1518 and RFC 1519, to define this new principle for allocating IP address blocks and routing IPv4 packets. An updated version, RFC 4632, was published in 2006.

After a period of experimentation with various alternatives, Classless Inter-Domain Routing was based on variable-length subnet masking (VLSM), which allows each network to be divided into subnetworks of various power-of-two sizes, so that each subnetwork can be sized appropriately for local needs. Variable-length subnet masks were mentioned as one alternative in RFC 950. Techniques for grouping addresses for common operations were based on the concept of cluster addressing, first proposed by Carl-Herbert Rokitansky.

## CIDR notation

**CIDR notation** is a compact representation of an IP address and its associated subnet mask. The notation was invented by Phil Karn in the 1980s. CIDR notation specifies an IP address, a slash character ⟨/⟩, and a decimal number. The decimal number is the count of consecutive leading *1* bits (from left to right) in the network mask. Each *1* bit denotes a bit of the address range which must remain identical to the given IP address. The IP address in CIDR notation is always represented according to the standards for IPv4 or IPv6.

The address may denote a specific interface address (including a host identifier, such as *10.0.0.1/8*), or it may be the beginning address of an entire network (using a host identifier of 0, as in *10.0.0.0/8* or its equivalent *10/8*). CIDR notation can even be used with no IP address at all, e.g. when referring to a */24* as a generic description of an IPv4 network that has a 24-bit prefix and 8-bit host numbers.

For example:

- *198.51.100.14/24* represents the IPv4 address *198.51.100.14* and its associated network prefix *198.51.100.0*, or equivalently, its subnet mask *255.255.255.0*, which has 24 leading *1* bits.
- the IPv4 block *198.51.100.0/22* represents the 1024 IPv4 addresses from *198.51.100.0* to *198.51.103.255*.
- the IPv6 block *2001:db8::/48* represents the block of IPv6 addresses from *2001:db8:0:0:0:0:0:0* to *2001:db8:0:ffff:ffff:ffff:ffff:ffff*.
- *::1/128* represents the IPv6 loopback address. Its prefix length is 128, which is the number of bits in the address.

In IPv4, CIDR notation came into wide use only after the implementation of the method, which was documented using dotted-decimal subnet mask specification after the slash, for example, *192.24.12.0/255.255.252.0*. Describing the network prefix width as a single number (*192.24.12.0/22*) was easier for network administrators to conceptualize and to calculate. It became gradually incorporated into later standards documents and into network configuration interfaces.

The number of addresses of a network may be calculated as 2address length − prefix length, where "address length" is 128 for IPv6 and 32 for IPv4. For example, in IPv4, the prefix length */29* gives: 232−29 = 23 = 8 addresses.

## Subnet masks

A subnet mask is a bitmask that encodes the prefix length associated with an IPv4 address or network in quad-dotted notation: 32 bits, starting with a number of ones equal to the prefix length, ending with zeros, and encoded in four-part dotted-decimal format: *255.255.255.0*. A subnet mask encodes the same information as a prefix length but predates the advent of CIDR. In CIDR notation, the prefix bits are always contiguous. Subnet masks were allowed by RFC 950 to specify non-contiguous bits until RFC 4632 stated that the mask must consist of only contiguous ones, if any, in the more significant bits and contiguous zeroes, if any, in the less significant bits. Given this constraint, a subnet mask and CIDR notation serve exactly the same function.

## CIDR blocks

CIDR is principally a bitwise, prefix-based standard for the representation of IP addresses and their routing properties. It facilitates routing by allowing blocks of addresses to be grouped into single routing table entries. These groups, commonly called CIDR blocks, share an initial sequence of bits in the binary representation of their IP addresses. IPv4 CIDR blocks are identified using a syntax similar to that of IPv4 addresses: a dotted-decimal address, followed by a slash, then a number from 0 to 32, i.e., *a.b.c.d/n*. The dotted-decimal portion is the IPv4 address. The number following the slash is the prefix length, the number of shared initial bits, counting from the most-significant bit of the address. When emphasizing only the size of a network, the address portion of the notation is usually omitted. Thus, a /20 block is a CIDR block with an unspecified 20-bit prefix.

An IP address is part of a CIDR block and is said to match the CIDR prefix if the initial n bits of the address and the CIDR prefix are the same. An IPv4 address is 32 bits so an n-bit CIDR prefix leaves 32−n bits unmatched, meaning that 232−n IPv4 addresses match a given n-bit CIDR prefix. Shorter CIDR prefixes match more addresses, while longer prefixes match fewer. In the case of overlaid CIDR blocks, an address can match multiple CIDR prefixes of different lengths.

CIDR is also used for IPv6 addresses and the syntax semantic is identical. The prefix length can range from 0 to 128, due to the larger number of bits in the address. However, by convention, a subnet on broadcast MAC layer networks always has 64-bit host identifiers. Larger prefixes (/127) are only used on some point-to-point links between routers, for security and policy reasons.

### Assignment of CIDR blocks

The Internet Assigned Numbers Authority (IANA) issues to regional Internet registries (RIRs) large, short-prefix CIDR blocks. However, a */8* (with over sixteen million addresses) is the largest block IANA will allocate. For example, *62.0.0.0/8* is administered by RIPE NCC, the European RIR. The RIRs, each responsible for a single, large geographic area, such as Europe or North America, subdivide these blocks and allocate subnets to local Internet registries (LIRs). Similar subdividing may be repeated several times at lower levels of delegation. End-user networks receive subnets sized according to their projected short-term need. Networks served by a single ISP are encouraged by IETF recommendations to obtain IP address space directly from their ISP. Networks served by multiple ISPs, on the other hand, may obtain provider-independent address space directly from the appropriate RIR.

For example, in the late 1990s, the IP address *208.130.29.33* (since reassigned) was used by www.freesoft.org. An analysis of this address identified three CIDR prefixes. *208.128.0.0/11*, a large CIDR block containing over 2 million addresses, had been assigned by ARIN (the North American RIR) to MCI. Automation Research Systems (ARS), a Virginia VAR, leased an Internet connection from MCI and was assigned the *208.130.28.0/22* block, capable of addressing just over 1000 devices. ARS used a */24* block for its publicly accessible servers, of which *208.130.29.33* was one. All of these CIDR prefixes would be used at different locations in the network. Outside MCI's network, the *208.128.0.0/11* prefix would be used to direct to MCI traffic bound not only for *208.130.29.33*, but also for any of the roughly two million IP addresses with the same initial 11 bits. Within MCI's network, *208.130.28.0/22* would become visible, directing traffic to the leased line serving ARS. Only within the ARS corporate network would the *208.130.29.0/24* prefix have been used.

### IPv4 CIDR blocks

| Address format | Difference to last address | Mask | Addresses | Relative to class A, B, C | Restrictions on *a*, *b*, *c* and *d* (0..255 unless noted) | Typical use |   |
|---|---|---|---|---|---|---|---|
| Decimal | 2*n* |   |   |   |   |   |   |
| *a.b.c.d/32* |   | *255.255.255.255* | 1 | 20 | 1⁄256 C |   | Host route |
| *a.b.c.d/31* | +*0.0.0.1* | *255.255.255.254* | 2 | 21 | 1⁄128 C | *d* = 0 ... (2*n*) ... 254 | Point-to-point links (RFC 3021) |
| *a.b.c.d/30* | +*0.0.0.3* | *255.255.255.252* | 4 | 22 | 1⁄64 C | *d* = 0 ... (4*n*) ... 252 | Point-to-point links (glue network) |
| *a.b.c.d/29* | +*0.0.0.7* | *255.255.255.248* | 8 | 23 | 1⁄32 C | *d* = 0 ... (8*n*) ... 248 | Smallest multi-host network |
| *a.b.c.d/28* | +*0.0.0.15* | *255.255.255.240* | 16 | 24 | 1⁄16 C | *d* = 0 ... (16*n*) ... 240 | Small LAN |
| *a.b.c.d/27* | +*0.0.0.31* | *255.255.255.224* | 32 | 25 | 1⁄8 C | *d* = 0 ... (32*n*) ... 224 |   |
| *a.b.c.d/26* | +*0.0.0.63* | *255.255.255.192* | 64 | 26 | 1⁄4 C | *d* = 0, 64, 128, 192 |   |
| *a.b.c.d/25* | +*0.0.0.127* | *255.255.255.128* | 128 | 27 | 1⁄2 C | *d* = 0, 128 | Large LAN |
| *a.b.c.0/24* | +*0.0.0.255* | *255.255.255.0* | 256 | 28 | 1 C |   |   |
| *a.b.c.0/23* | +*0.0.1.255* | *255.255.254.0* | 512 | 29 | 2 C | *c* = 0 ... (2*n*) ... 254 |   |
| *a.b.c.0/22* | +*0.0.3.255* | *255.255.252.0* | 1,024 | 210 | 4 C | *c* = 0 ... (4*n*) ... 252 | Small business |
| *a.b.c.0/21* | +*0.0.7.255* | *255.255.248.0* | 2,048 | 211 | 8 C | *c* = 0 ... (8*n*) ... 248 | Small ISP/large business |
| *a.b.c.0/20* | +*0.0.15.255* | *255.255.240.0* | 4,096 | 212 | 16 C | *c* = 0 ... (16*n*) ... 240 |   |
| *a.b.c.0/19* | +*0.0.31.255* | *255.255.224.0* | 8,192 | 213 | 32 C | *c* = 0 ... (32*n*) ... 224 | ISP/large business |
| *a.b.c.0/18* | +*0.0.63.255* | *255.255.192.0* | 16,384 | 214 | 64 C | *c* = 0, 64, 128, 192 |   |
| *a.b.c.0/17* | +*0.0.127.255* | *255.255.128.0* | 32,768 | 215 | 128 C | *c* = 0, 128 |   |
| *a.b.0.0/16* | +*0.0.255.255* | *255.255.0.0* | 65,536 | 216 | 256 C = B |   |   |
| *a.b.0.0/15* | +*0.1.255.255* | *255.254.0.0* | 131,072 | 217 | 2 B | *b* = 0 ... (2*n*) ... 254 |   |
| *a.b.0.0/14* | +*0.3.255.255* | *255.252.0.0* | 262,144 | 218 | 4 B | *b* = 0 ... (4*n*) ... 252 |   |
| *a.b.0.0/13* | +*0.7.255.255* | *255.248.0.0* | 524,288 | 219 | 8 B | *b* = 0 ... (8*n*) ... 248 |   |
| *a.b.0.0/12* | +*0.15.255.255* | *255.240.0.0* | 1,048,576 | 220 | 16 B | *b* = 0 ... (16*n*) ... 240 |   |
| *a.b.0.0/11* | +*0.31.255.255* | *255.224.0.0* | 2,097,152 | 221 | 32 B | *b* = 0 ... (32*n*) ... 224 |   |
| *a.b.0.0/10* | +*0.63.255.255* | *255.192.0.0* | 4,194,304 | 222 | 64 B | *b* = 0, 64, 128, 192 |   |
| *a.b.0.0/9* | +*0.127.255.255* | *255.128.0.0* | 8,388,608 | 223 | 128 B | *b* = 0, 128 |   |
| *a.0.0.0/8* | +*0.255.255.255* | *255.0.0.0* | 16,777,216 | 224 | 256 B = A |   | Largest IANA block allocation |
| *a.0.0.0/7* | +*1.255.255.255* | *254.0.0.0* | 33,554,432 | 225 | 2 A | *a* = 0 ... (2*n*) ... 254 |   |
| *a.0.0.0/6* | +*3.255.255.255* | *252.0.0.0* | 67,108,864 | 226 | 4 A | *a* = 0 ... (4*n*) ... 252 |   |
| *a.0.0.0/5* | +*7.255.255.255* | *248.0.0.0* | 134,217,728 | 227 | 8 A | *a* = 0 ... (8*n*) ... 248 |   |
| *a.0.0.0/4* | +*15.255.255.255* | *240.0.0.0* | 268,435,456 | 228 | 16 A | *a* = 0 ... (16*n*) ... 240 |   |
| *a.0.0.0/3* | +*31.255.255.255* | *224.0.0.0* | 536,870,912 | 229 | 32 A | *a* = 0 ... (32*n*) ... 224 |   |
| *a.0.0.0/2* | +*63.255.255.255* | *192.0.0.0* | 1,073,741,824 | 230 | 64 A | *a* = 0, 64, 128, 192 |   |
| *a.0.0.0/1* | +*127.255.255.255* | *128.0.0.0* | 2,147,483,648 | 231 | 128 A | *a* = 0, 128 |   |
| *0.0.0.0/0* | +*255.255.255.255* | *0.0.0.0* | 4,294,967,296 | 232 | 256 A |   | Entire IPv4 Internet, default route |

In routed subnets larger than */31* or */32*, the number of available host addresses is usually reduced by two, namely the largest address, which is reserved as the broadcast address, and the smallest address, which identifies the network itself and is reserved solely for this purpose.

In such usage, a */31* network, with one binary digit in the host identifier, is unusable, as such a subnet would provide no available host addresses after this reduction. RFC 3021 creates an exception to the "host all ones" and "host all zeros" rules to make */31* networks usable for point-to-point links. */32* addresses (single-host network) must be accessed by explicit routing rules, as there is no address available for a gateway.

### IPv6 CIDR blocks

| Prefix size | Number of equivalent subnets | Interface ID bits |   |   |
|---|---|---|---|---|
| /48 | /56 | /64 |   |   |
| /24 | 16M | 4G | 1T | 104 |
| /25 | 8M | 2G | 512G | 103 |
| /26 | 4M | 1G | 256G | 102 |
| /27 | 2M | 512M | 128G | 101 |
| /28 | 1M | 256M | 64G | 100 |
| /29 | 512K | 128M | 32G | 99 |
| /30 | 256K | 64M | 16G | 98 |
| /31 | 128K | 32M | 8G | 97 |
| /32 | 64K | 16M | 4G | 96 |
| /33 | 32K | 8M | 2G | 95 |
| /34 | 16K | 4M | 1G | 94 |
| /35 | 8K | 2M | 512M | 93 |
| /36 | 4K | 1M | 256M | 92 |
| /37 | 2K | 512K | 128M | 91 |
| /38 | 1K | 256K | 64M | 90 |
| /39 | 512 | 128K | 32M | 89 |
| /40 | 256 | 64K | 16M | 88 |
| /41 | 128 | 32K | 8M | 87 |
| /42 | 64 | 16K | 4M | 86 |
| /43 | 32 | 8K | 2M | 85 |
| /44 | 16 | 4K | 1M | 84 |
| /45 | 8 | 2K | 512K | 83 |
| /46 | 4 | 1K | 256K | 82 |
| /47 | 2 | 512 | 128K | 81 |
| /48 | 1 | 256 | 64K | 80 |
| /49 |   | 128 | 32K | 79 |
| /50 |   | 64 | 16K | 78 |
| /51 |   | 32 | 8K | 77 |
| /52 |   | 16 | 4K | 76 |
| /53 |   | 8 | 2K | 75 |
| /54 |   | 4 | 1K | 74 |
| /55 |   | 2 | 512 | 73 |
| /56 |   | 1 | 256 | 72 |
| /57 |   |   | 128 | 71 |
| /58 |   |   | 64 | 70 |
| /59 |   |   | 32 | 69 |
| /60 |   |   | 16 | 68 |
| /61 |   |   | 8 | 67 |
| /62 |   |   | 4 | 66 |
| /63 |   |   | 2 | 65 |
| /64 |   |   | 1 | 64 |
| **K** = 1,024 |   |   |   |   |
| **M** = 1,048,576 |   |   |   |   |
| **G** = 1,073,741,824 |   |   |   |   |
| **T** = 1,099,511,627,776 |   |   |   |   |

The large address size of IPv6 permitted worldwide route summarization and guaranteed sufficient address pools at each site. The standard subnet size for IPv6 networks is a */64* block, which is required for the operation of stateless address autoconfiguration. At first, the IETF recommended in RFC 3177 as a best practice that all end sites receive */48* address allocations, but criticism and reevaluation of actual needs and practices has led to more flexible allocation recommendations in RFC 6177 suggesting a significantly smaller allocation for some sites, such as a */56* block for residential networks.

This IPv6 subnetting reference lists the sizes for IPv6 subnetworks. Different types of network links may require different subnet sizes. The subnet mask separates the bits of the network identifier prefix from the bits of the interface identifier. Selecting a smaller prefix size results in fewer number of networks covered, but with more addresses within each network.

```
2001:0db8:0123:4567:89ab:cdef:1234:5678
|||| |||| |||| |||| |||| |||| |||| ||||
|||| |||| |||| |||| |||| |||| |||| |||128     Single end-points and loopback
|||| |||| |||| |||| |||| |||| |||| |||127   Point-to-point links (inter-router)
|||| |||| |||| |||| |||| |||| |||| ||124
|||| |||| |||| |||| |||| |||| |||| |120
|||| |||| |||| |||| |||| |||| |||| 116
|||| |||| |||| |||| |||| |||| |||112
|||| |||| |||| |||| |||| |||| ||108
|||| |||| |||| |||| |||| |||| |104
|||| |||| |||| |||| |||| |||| 100
|||| |||| |||| |||| |||| |||96
|||| |||| |||| |||| |||| ||92
|||| |||| |||| |||| |||| |88
|||| |||| |||| |||| |||| 84
|||| |||| |||| |||| |||80
|||| |||| |||| |||| ||76
|||| |||| |||| |||| |72
|||| |||| |||| |||| 68
|||| |||| |||| |||64   Single LAN; default prefix size for SLAAC
|||| |||| |||| ||60   Some (very limited) 6rd deployments (/60 = 16 /64 blocks)
|||| |||| |||| |56   Minimal end-site assignment; e.g. home network (/56 = 256 /64 blocks)
|||| |||| |||| 52   /52 block = 4096 /64 blocks
|||| |||| |||48   Typical assignment for larger sites (/48 = 65536 /64 blocks)
|||| |||| ||44
|||| |||| |40
|||| |||| 36   possible future local Internet registry (LIR) extra-small allocations
|||| |||32   LIR minimum allocations
|||| ||28   LIR medium allocations
|||| |24   LIR large allocations
|||| 20   LIR extra large allocations
|||16
||12   Regional Internet registry (RIR) allocations from IANA
|8
4
```

## Numerical interpretation

Topologically, the set of subnets described by CIDR represents a cover of the corresponding address space. The interval described by the notation $X/n$ numerically corresponds to addresses of the form $[x\cdot 2^{32-n},x\cdot 2^{32-n}+2^{32-n}-1]$ (for IPv4) and $[x\cdot 2^{128n},x\cdot 2^{128n}+2^{128-n}-1]$ (for IPv6), where $X=x\cdot 2^{32-n}$ and $X=x\cdot 2^{128-n}$ has the lower n bits set to 0. For a fixed n , the set of all $X/n$ subnets constitutes a partition, that is, a cover of non-overlapping sets. Increasing n yields finer and finer subpartitions. Thus, two subnets $X/n$ and $Y/m$ are either disjoint or one is a subnet of the other.

## Prefix aggregation

CIDR provides fine-grained routing prefix aggregation. For example, if the first 20 bits of their network prefixes match, sixteen contiguous */24* networks can be aggregated and advertised to a larger network as a single */20* routing table entry. This reduces the number of routes that have to be advertised.

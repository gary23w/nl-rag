---
title: "IEEE 802.1aq (part 2/2)"
source: https://en.wikipedia.org/wiki/IEEE_802.1aq
domain: spanning-tree-protocol
license: CC-BY-SA-4.0
tags: spanning tree protocol, loop prevention, network bridging, broadcast domain
fetched: 2026-07-02
part: 2/2
---

## Implementation notes

802.1aq takes IS-IS topology information augmented with service attachment (I-SID) information, does a series of computations and produces a forwarding table (filtering table) for unicast and multicast entries.

The IS-IS extensions that carry the information required by 802.1aq are given in the **isis-layer2** IETF document listed below.

An implementation of 802.1aq will first modify the IS-IS hellos to include an NLPID (network layer protocol identifier) of 0xC01 in their Protocols-Supported type–length–value (TLV) (type 129) which has been reserved for 802.1aq. The hellos also must include an MSTID (which gives the purpose of each VID), and finally, each ECMT behavior must be assigned to a VID and exchanged in the hellos. The hellos would normally run untagged. Note that NLPID of IP is not required to form an adjacency for 802.1aq, but also will not prevent an adjacency when present.

The links are assigned 802.1aq specific metrics, which travel in their own TLV (Type Length Value), which is more or less identical to the IP link metrics. The calculations will always use the maximum of the two unidirectional link metrics to enforce symmetric route weights.

The node is assigned a MAC address to identify it globally, and this is used to form the IS-IS SYSID. A box mac would normally serve this purpose. The Area-Id is not directly used by 802.1aq but should, of course, be the same for nodes in the same 802.1aq network. Multiple areas/levels are not yet supported.

The node is further assigned an SPSourceID, which is a 20-bit network-wide unique identifier. This can often be the low 20 bits of the SYSID (if unique) or can be dynamically negotiated or manually configured.

The SPSourceID and the ECMT assignments to B-VIDs are then advertised into the IS-IS network in their own 802.1aq TLV.

The 802.1aq computations are restricted to links between nodes that have an 802.1aq link weight and that support the NLPID 0xC01. As previously discussed, the link weights are forced to be symmetric for the purpose of computation by taking the min of two dissimilar values.

When a service is configured in the form of an I-SID assignment to an ECMT behavior, that I-SID is then advertised along with the desired ECMT behavior and an indication of its transmit, receive properties (a new TLV is used for this purpose of course).

When an 802.1aq node receives an IS-IS update, it will compute the unique shortest path to all other IS-IS nodes that support 802.1aq. There will be one unique (symmetric) shortest path per ECMT behavior. The tie breaking used to enforce this uniqueness and ECMT is described below.

The unicast FDB/FIB will be populated based on this first shortest path computation. There will be one entry per ECMT behavior/B-VID produced.

The transit multicast computation (which only applies when transit replication is desired and is not applicable to services that have chosen head-end replication) can be implemented in many ways; care must be taken to keep this efficient, but in general, a series of shortest path computations must be done. The basic requirement is to decide 'am I on the shortest path between two nodes, one of which transmits an I-SID and the other receives that I-SID.'

Rather poor performing pseudocode for this computation looks something like this:

```
for each NODE in network which originates at least one transmit ISID do
    SPF = compute the shortest path trees from NODE for all ECMT B-VIDs.
    for each ECMT behavior do
        for each NEIGHBOR of NODE do
            if NEIGHBOR is on the SPF towards NODE for this ECMT then
                T = NODE's transmit ISIDs unioned with all receive
                    ISIDs below us on SPF
                for each ISID in T do
                    create/modify multicast entry where [
                        MAC-DA   = NODE.SpsourceID:20||ISID:24||LocalBit:1||MulticastBit:1
                        B-VID    = VID associated with this ECMT
                        out port = interface to NEIGHBOR
                        in port  = port towards NODE on the SPF for this ECMT
                    ]
```

The above pseudocode computes many more SPF's than strictly necessary in most cases, and better algorithms are known to decide if a node is on a shortest path between two other nodes. A reference to a paper presented at the IEEE, which gives a much faster algorithm that drastically reduces the number of outer iterations required, is given below.

In general, though, even the exhaustive algorithm above is more than able to handle several hundred-node networks in a few tens of milliseconds on the 1 GHz or greater common CPUs when carefully crafted.

For ISIDs that have chosen head-end replication, the computation is trivial and involves simply finding the other attachment points that receive that ISID and creating a serial unicast table to replicate to them one by one.

### Tie-breaking

802.1aq must produce deterministic symmetric downstream congruent shortest paths. This means that not only must a given node compute the same path forward and reverse, but all the other nodes downstream (and upstream) on that path must also produce the same result. This downstream congruence is a consequence of the hop-by-hop forwarding nature of Ethernet since only the destination address and VID are used to decide the next hop. It is important to keep this in mind when trying to design other ECMT algorithms for 802.1aq, as this is an easy trap to fall into. It begins by taking the unidirectional link metrics that are advertised by ISIS for 802.1aq and ensuring that they are symmetric. This is done by simply taking the MIN of the two values at both ends prior to doing any computations. This alone does not guarantee symmetry, however.

The 802.1aq standard describes a mechanism called a PATHID, which is a network-wide unique identifier for a path. This is a useful logical way to understand how to deterministically break ties but is not how one would implement such a tie-breaker in practice. The PATHID is defined as just the sequence of SYSIDs that make up the path (not including the end points).. sorted. Every path in the network therefore has a unique PATHID independent of where in the network the path is discovered.

802.1aq always picks the lowest PATHID path when a choice presents itself in the shortest path computations. This ensures that every node will make the same decision.

For example, in Figure 7 above, there are four equal-cost paths between node 7 and node 5 as shown by the colors blue, green, pink and brown. The PATHID for these paths are as follows:

- `PATHID[**brown**] = {0,1}`
- `PATHID[**pink**] = {0,3}`
- `PATHID[**green**] = {1,2}`
- `PATHID[**blue**] = {2,3}`

The lowest PATHID is therefore the brown path {0,1}.

This low PATHID algorithm has very desirable properties. The first is that it can be done progressively by simply looking for the lowest SYSID along a path, and secondly, because an efficient implementation that operates stepwise is possible by simply back-tracking two competing paths and looking for the minimum of the two paths' minimum SYSIDs.

The low PATHID algorithm is the basis of all 802.1aq tie breaking. ECMT is also based on the low PATHID algorithm by simply feeding it different SYSID permutations – one per ECMT algorithm. The most obvious permutation to pass is a complete inversion of the SYSID by XOR-ing it with 0xfff... prior to looking for the min of two minimums. This algorithm is referred to as high PATHID because it logically chooses the largest PATHID path when presented with two equal-cost choices.

In the example in figure 7, the path with the highest PATHID is therefore the blue path whose PATHID is {2,3}. Simply inverting all the SYSIDs and running the low PATHID algorithm will yield the same result.

The other 14 defined ECMT algorithms use different permutations of the SYSID by XOR-ing it with different bit masks, which are designed to create a relatively good distribution of bits. It should be clear that different permutations will result in the purple and green paths being lowest in turn.

The 17 individual 64-bit masks used by the ECT algorithm are made up of the same byte value repeated eight times to fill each 64-bit mask. These 17-byte values are as follows:

```mw
ECT-MASK[17] = { 0x00, 0x00, 0xFF, 0x88,
                 0x77, 0x44, 0x33, 0xCC,
                 0xBB, 0x22, 0x11, 0x66,
                 0x55, 0xAA, 0x99, 0xDD,
                 0xEE };
```

ECT-MASK[0] is reserved for a common spanning tree algorithm, while ECT-MASK[1] creates the Low PATHID set of shortest path first trees, ECT-MASK[2] creates the High PATHID set of shortest path trees, and the other indexes create other relatively diverse permutations of shortest path first trees.

In additio,n the ECMT tie-breaking algorithms also permit some degree of human override or tweaking. This is accomplished by including a BridgePriority field together with the SYSID such that the combination, called a BridgeIdentifier, becomes the input to the ECT algorithm. By adjusting the BridgePriority up or down, a path's PATHID can be raised or lowered relative to others, and a substantial degree of tunability is afforded.

The above description gives an easy-to-understand way to view the tie breaking; an actual implementation simply backtracks from the fork point to the join point in two competing equal-cost paths (usually during the Dijkstra shortest path computation) and picks the path traversing the lowest (after masking) BridgePriority|SysId.


## Interoperability

The first public interoperability tests of IEEE 802.1aq were held in Ottawa in October 2010. Two vendors provided SPBM implementations, and a total of 5 physical switches and 32 emulated switches were tested for control/data and OA&M.

Further events were held in Ottawa in January 2011 with 5 vendors and 6 implementations, at 2013's Interop event at Las Vegas where an SPBM network was used as a backbone.


## Competitors

MC-LAG, VXLAN, and QFabric have all been proposed, but the IETF TRILL standard (Transparent Interconnect of Lots of Links) is considered the major competitor of IEEE 802.1aq, and: "the evaluation of relative merits and difference of the two standards proposals is currently a hotly debated topic in the networking industry."


## Deployments

Deployment considerations and interoperability best practices are documented in an IETF document titled "SPB Deployment Considerations"

- 2013 Interop: Networking Leaders Demo Shortest Path Bridging
- 2014 Interop: InteropNet Goes IPv6, Includes Shortest Path Bridging

Extreme Networks, by virtue of its acquisition of the Avaya Networking business and assets, is currently the leading exponent of SPB-based deployments; its enhanced and extended implementation of SPB - including integrated Layer 3 IP Routing and IP Multicast functionality - is marketed under the banner of the "Fabric Connect" technology. Additionally, Extreme Networks is supporting an IETF Internet Draft Draft that defines a means of automatically extended SPBM-based services to end-devices via conventional Ethernet Switches, leveraging an IEEE 802.1AB LLDP-based communications protocol; this capability - marketing "Fabric Attach" technology - allows for the automatic attachment of end-devices, and includes dynamic configuration of VLAN/I-SID (VSN) mappings.

Avaya (acquired by Extreme Networks) has deployed SPB/Fabric Connect solutions for businesses operating across a number of industry verticals:

- **Education**, examples include: Leeds Metropolitan University, Macquaire University, Pearland Independent School District, Ajman University of Science & Technology
- **Transportation**, examples include: Schiphol Telematics, Rheinbahn, Sendai City Transportation Bureau, NSB
- **Banking & Finance**, examples include: Fiducia, Sparebanken Vest
- **Major Events**, examples include: 2013 & 2014 Interop (InteropNet Backbone), 2014 Sochi Winter Olympics, Dubai World Trade Center
- **Healthcare**, examples include: Oslo University Hospital, Concord Hospital, Franciscan Alliance, Sydney Adventist Hospital
- **Manufacturing**, examples include: Fujitsu Technology Solutions
- **Media**, examples include: Schibsted, Medienhaus Lensing, Sanlih Entertainment Television
- **Government**, examples include: City of Redondo Beach, City of Breda, Bezirksamt Neukölln


## Product support

- Alcatel-Lucent 7750-SR,
- Alcatel-Lucent Enterprise OmniSwitch 9900, OmniSwitch 6900, OmniSwitch 6860, OmniSwitch 6865
- Extreme Networks 5000 Series (5720, 5520, 5420 and 5320)
- Extreme Networks VSP 9000 Series
- Extreme Networks VSP 8400 Series
- Extreme Networks VSP 8000 Series (VSP 8284XSQ, VSP 8404C)
- Extreme Networks VSP 7200 Series
- Extreme Networks VSP 4000 Series (VSP 4450GSX-PWR+, VSP 4450GSX-DC, VSP 4450GTX-HT-PWR+, VSP 4850GTS, VSP 4850GTS-PWR+, VSP 4850GTS-DC)
- Extreme Networks ERS 5900 Series
- Extreme Networks ERS 4900 Series
- Extreme Networks ERS 4800 Series
- Enterasys Networks S140 and S180
- Extreme Networks K-Series
- Huawei S9300 (prototype only at the moment)
- Solana
- Spirent
- HP 5900, 5920, 5930, 11900, 12500, 12900
- IP Infusion's ZebOS network platform
- IXIA
- JDSU

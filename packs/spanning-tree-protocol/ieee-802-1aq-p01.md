---
title: "IEEE 802.1aq (part 1/2)"
source: https://en.wikipedia.org/wiki/IEEE_802.1aq
domain: spanning-tree-protocol
license: CC-BY-SA-4.0
tags: spanning tree protocol, loop prevention, network bridging, broadcast domain
fetched: 2026-07-02
part: 1/2
---

# IEEE 802.1aq

**IEEE 802.1aq** is an amendment to the IEEE 802.1Q networking standard which adds support for **Shortest Path Bridging** (**SPB**). This technology is intended to simplify the creation and configuration of Ethernet networks while enabling multipath routing.

SPB is designed to replace the older Spanning Tree Protocols: IEEE 802.1D STP, IEEE 802.1w RSTP, and IEEE 802.1s MSTP. These block any redundant paths that can result in a switching loop, whereas SPB allows all paths to be active with multiple equal-cost paths, provides much larger layer-2 topologies, supports faster convergence times, and improves the efficiency by allowing traffic to load share across all paths of a mesh network. It is designed to preserve the plug-and-play nature that established Ethernet as the de facto protocol at layer 2.

The technology provides VLANs on native Ethernet infrastructures using a link-state protocol to advertise both topology and VLAN membership. Packets are encapsulated at the edge either in MAC-in-MAC per IEEE 802.1ah or tagged per IEEE 802.1Q or IEEE 802.1ad and transported only to other members of VLAN. Unicast, multicast, and broadcast are supported and all routing is on symmetric shortest paths.

The control plane is based on the Intermediate System to Intermediate System (IS-IS) routing protocol, leveraging a small number of extensions defined in RFC 6329.


## History

On 4 March 2006 the working group posted 802.1aq draft 0.1. In March 2012 the IEEE approved the 802.1aq standard.

In May 2013, the first public multivendor interoperability was demonstrated as SPB served as the backbone for Interop 2013 in Las Vegas. In 2013 and 2014 SPB was used to build the InteropNet backbone with only one-tenth the resources of prior years. During Interop 2014 SPB was used as the backbone protocol which can enable software-defined networking (SDN) functionalities.

The 2014 Winter Olympics were the first "fabric-enabled" Games using SPB "IEEE 802.1aq" technology. During the games this fabric network could handle up to 54 Tbit/s of traffic.


## Associated protocols

- IEEE 802.1Q-2014 - Bridges and Bridged Networks - This standard incorporates Shortest Path Bridging (IEEE 802.1aq) with the following: IEEE Std 802.1Q-2011, IEEE Std 802.1Qbe-2011, IEEE Std 802.1Qbc-2011, IEEE Std 802.1Qbb-2011, IEEE Std 802.1Qaz-2011, IEEE Std 802.1Qbf-2011, IEEE Std 802.1Qbg-2012, IEEE Std 802.1Q-2011/Cor 2–2012, and IEEE Std 802.1Qbp-2014, and much functionality previously specified in 802.1D.
- IEEE 802.1ag - Connectivity Fault Management (CFM)
- IEEE 802.1Qbp - Equal Cost Multiple Paths in Shortest Path Bridging
- IEEE P802.1Qcj - Automatic Attachment to Provider Backbone Bridging (PBB) services
- RFC 6329 - IS-IS Extensions Supporting IEEE 802.1aq Shortest Path Bridging

### RFC 6329

The Intermediate System to Intermediate System (IS-IS) protocol, as defined in the IETF proposed standard RFC 6329, is used as the control plane for SPB. SPB requires no state machine or other substantive changes to IS-IS, and simply requires a new Network Layer Protocol Identifier (NLPID) and set of TLVs.

SPB allows for shortest-path forwarding in a mesh-connected Ethernet network utilizing multiple equal-cost paths. This permits SPB to support large Layer 2 topologies, with faster convergence, and improved use of the mesh topology when compared to networks configured with Spanning Tree Protocol. SPB augments IS-IS with a small number of TLVs and sub-TLVs, and supports two Ethernet encapsulating data paths, IEEE 802.1ad provider bridges (PB) and IEEE 802.1ah Provider Backbone Bridges (PBB).

SPB is designed to run in parallel with other network-layer protocols such as IPv4 and IPv6. Standards mandate that the failure of two nodes to establish an SPB adjacency will not have a collateral impact, such as the rejection of an adjacency for other network-layer protocols (e.g., OSPF).

#### Protocol extensions

The IS-IS extensions defined in RFC 6329 that deliver standardized support for 802.1aq SPB are:

- IS-IS Hello (IIH) Protocol Extensions
- Node Information Extensions
- Adjacency Information Extensions
- Service Information Extensions

##### IS-IS Hello (IIH) protocol extensions

802.1aq has been designed to operate in parallel with other network layer protocols such as IPv4 and IPv6; therefore, failure of two nodes to establish an SPB adjacency will not cause network layer protocols to also reject an adjacency. RFC 6328 assigns 802.1aq the Network Layer Protocol ID (NLPID) value 0xC1. This NLPID is used by SPB Bridges to indicate their ability to form adjacencies and operate as part of an 802.1aq domain. 802.1aq frames flow on adjacencies that advertise this NLPID in both directions, and nodes regard an adjacency that has not been advertised in both directions as non-existent (with infinite link metric). 802.1aq augments the normal IIH PDU with three new TLVs, which like all other SPB TLVs, travel within *Multi-Topology TLVs*, therefore allowing multiple logical instances of SPB within a single IS-IS protocol instance.

SPB can use many VIDs, agreeing on which VIDs are used for which purposes. The IIH PDUs carry a digest of all the used VIDs, referred to as the *Multiple Spanning Tree Configuration TLV* which uses a common and compact encoding reused from IEEE 802.1Q.

For the purposes of loop prevention SPB neighbors may also support a mechanism to verify that the contents of their topology databases are synchronized. Exchanging digests of SPB topology information, using the optional *SPB-Digest sub-TLV*, allows nodes to compare information and take specific action where a mismatch in topology is indicated.

Finally, SPB needs to know which shortest path tree (SPT) sets are being used by which VIDs, and this is carried in the *Base VLAN Identifiers TLV*.

##### Node information extensions

All SPB nodal information extensions travel within a new *Multi-Topology (MT) capability TLV*. There can be one or many MT-Capability TLVs present, depending on the amount of information that needs to be carried.

The *SPB Instance sub-TLV* gives the Shortest Path Source ID (SPSourceID) for this node or topology instance. This is used in the formation of multicast destination addresses (DAs) for frames originating from this node or instance.

There are multiple ECT algorithms defined for SPB and additional algorithms may be defined in the future, including but not limited to ECMP- or hash-based behaviors and (*,G) Multicast trees. These algorithms will use this optional TLV to define new algorithm parametric data. For tie-breaking parameters, there are two broad classes of algorithms: one that uses nodal data to break ties and one that uses link data to break ties. The *SPB Instance Opaque Equal cost Tree Algorithm TLV* is used to associate opaque tie-breaking data with a node.

##### Adjacency information extensions

The *SPB Link Metric sub-TLV* occurs within the Multi-Topology Intermediate System Neighbor TLV or within the Extended IS Reachability TLV. *SPB Adjacency Opaque Equal Cost Tree Algorithm TLV* also occurs within the Multi-Topology Intermediate System TLV or the Extended IS Reachability TLV. Where this sub-TLV is not present for an IS-IS adjacency, that adjacency will not carry SPB traffic for the given topology instance.

##### Service information extensions

The *SPBM Service Identifier and Unicast Address TLV* is used to introduce service group membership on the originating node or to advertise an additional B-MAC unicast address present on, or reachable by the node. The *SPBV MAC Address TLV* is the IS-IS sub-TLV used for advertisement of group MAC addresses in SPBV mode.


## Benefits

Shortest Path Bridging-VID (SPBV) and Shortest Path Bridging-MAC (SPBM) are two operating modes of 802.1aq. Both inherit key benefits of link state routing:

- the ability to use all available physical connectivity, because loop avoidance uses a control plane with a global view of network topology
- fast restoration of connectivity after failure, again because of link state routing's global view of network topology
- under failure, the property that only directly affected traffic is impacted during restoration
- rapid restoration of broadcast and multicast connectivity, because IS-IS floods all of the required information in the SPB extensions to IS-IS, thereby allowing unicast and multicast connectivity to be installed in parallel, with no need for a second phase signaling process to run over the converged unicast topology to compute and install multicast trees.

SPBM offers emulation of a transparent Ethernet LAN segment. It implements VLANs with scoped multicast trees, which means no egress discard of broadcast, unknown-unicast and multicast traffic, a feature common to approaches that use a small number of shared trees, hence the network does not simply degrade with size as the percentage of frames discarded goes up.

The carrier-space equivalent of this application is the delivery of Ethernet VPN services to Enterprises over common carrier infrastructure. The required attributes are fundamentally the same; complete transparency for customer Ethernet services (both point-to-point and LAN), and complete isolation between one customer's traffic and that of all other customers.

A further consequence of SPBM's transparency in both data plane and control plane is that it delivers the MEF 6.1 service set. It also provides the carrier with the toolkit to support geo-redundant broadband backhaul; in these applications, many DSLAMs or other access equipment must be backhauled to multiple Broadband Remote Access Server (BRAS) sites, with application-determined binding of sessions to a BRAS. However, DSLAMs must not be allowed to communicate with each other, because carriers then lose the ability to control peer-to-peer connectivity. MEF E-TREE does just this, and further provides an efficient multicast fabric for the distribution of IPTV.

SPBM offers both an ideal multicast replication model, where packets are replicated only at fork points in the shortest path tree that connects members, and also the less state-intensive head-end replication model, where, in essence, serial unicast packets are sent to all other members along the same shortest path first tree. These two models are selected by specifying properties of the service at the edge, which affect the transit node decisions on multicast state installation. This allows for a trade-off to be made between optimum transit replication points (with their larger state costs) vs. reduced core state (but much more traffic) of the head-end replication model. These selections can be different for different members of the same Individual Service ID (I-SID), allowing different trade-offs to be made for different members.

Figure 5 below is a quick way to understand what SPBM is doing on the scale of the entire network. Figure 5 shows how a 7-member E-LAN is created from the edge membership information and the deterministic distributed calculation of per source, per service trees with transit replication. Head-end replication is not shown as it is trivial and simply uses the existing unicast FIBs to forward copies serially to the known other receivers.


## Operations and management

802.1aq builds on all existing Ethernet operations, administration and management (OA&M). Since 802.1aq ensures that its unicast and multicast packets for a given virtual LAN (VLAN) follow the same forward and reverse path and use completely standard 802 encapsulations, all the methods of IEEE 802.1ag and Y.1731 operate unchanged on an 802.1aq network.


## High level

802.1aq is the IEEE-sanctioned link state Ethernet control plane for all IEEE VLANs covered in IEEE 802.1Q. The Shortest Path Bridging virtual local area network identifier (VLAN ID) or Shortest Path Bridging VID (SPBV) provides a capability that is backward compatible with spanning tree technologies. The SPBM provides additional values that use Provider Backbone Bridge (PBB) capabilities. SPB (the generic term for both) combines an Ethernet data path (either IEEE 802.1Q in the case of SPBV, or PBBs per IEEE 802.1ah in the case of SPBM) with an IS-IS link state control protocol running between Shortest Path bridges (Network-to-network interface (NNI) links). The link state protocol is used to discover and advertise the network topology and compute SPTs from all bridges in the SPT Region.

In SPBM, the backbone MAC (B-MAC) addresses of the participating nodes and also the service membership information for interfaces to non-participating devices (User–network interface (UNI) ports) is distributed. Topology data is then input to a calculation engine, which computes symmetric shortest path trees based on minimum cost from each participating node to all other participating nodes. In SPBV, these trees provide a shortest path tree where individual MAC address can be learned and group address membership can be distributed. In SPBM, the shortest path trees are then used to populate forwarding tables for each participating node's individual B-MAC addresses and for group addresses; Group multicast trees are subtrees of the default shortest path tree formed by (source, group) pairing. Depending on the topology, several different equal-cost multi-path trees are possible and SPB supports multiple algorithms per IS-IS instance.

In SPB as with other link-state-based protocols, the computations are done in a distributed fashion. Each node computes the Ethernet-compliant forwarding behavior independently based on a normally synchronized common view of the network and UNI ports. Ethernet filtering Database (or forwarding) tables are populated locally to independently and deterministically implement its portion of the network forwarding behavior.

The two different flavors of data path give rise to two slightly different versions of this protocol. One (SPBM) is intended where complete isolation of many separate instances of client LANs and their associated device MAC addresses is desired, and it therefore uses a full encapsulation (MAC-in-MAC a.k.a. IEEE 802.1ah). The other (SPBV) is intended where such isolation of client device MAC addresses is not necessary, and it reuses only the existing VLAN tag on participating NNI links. Chronologically, SPBV came first, with the project originally being conceived to address scalability and convergence of MSTP.

At the time the specification for PBB was progressing, it became apparent that leveraging both the PBB data plane and a link state control plane would significantly extend Ethernet's capabilities and applications. Provider Link State Bridging (PLSB) was a straw man proposal brought to the IEEE 802.1aq Shortest Path Bridging Working Group, to provide a concrete example of such a system. As IEEE 802.1aq standardization progressed, some of the detailed mechanisms proposed by PLSB were replaced by functional equivalents, but all of the key concepts embodied in PLSB were carried forward into the standard.

### Shortest Path Bridging-VID

A primary feature of Shortest Path Bridging is the ability to use link-state IS-IS to learn network topology. In SPBV the mechanism used to identify the tree is to use a different Shortest Path VLAN ID (SPVID) for each source bridge. The IS-IS topology is used both to allocate unique SPVIDs and to enable shortest path forwarding for individual and group addresses. Originally targeted for small, low-configuration networks, SPB grew into a larger project encompassing the latest provider control plane for SPBV and harmonizing the concepts of Ethernet's data plane.

SPB defines a shortest path *region* which is the boundary of the shortest path topology and the rest of the VLAN topology, which may be any number of legacy bridges. SPB operates by learning the SPB-capable bridges and growing the *region* to include the SPB-capable bridges that have the same Base VID and MSTID configuration digest (Allocation of VIDs for SPB purposes).

SPBV builds shortest-path trees that support loop prevention and optionally support loop mitigation on the SPVID. SPBV still allows learning of Ethernet MAC addresses but it can distribute multicast addresses that can be used to prune the shortest path trees according to the multicast membership either through Multiple MAC Registration Protocol (MMRP) or directly using IS-IS distribution of multicast membership.

SPBV builds shortest-path trees but also interworks with legacy bridges running Rapid Spanning Tree Protocol and Multiple Spanning Tree Protocol (MSTP). SPBV uses techniques from MSTP regions to interwork with non-SPT regions, behaving logically as a large distributed bridge as viewed from outside the region.

SPBV supports shortest path trees, but SPBV also builds a spanning tree, which is computed from the link state database and uses the Base VID. This means that SPBV can use this traditional spanning tree for computation of the common and internal spanning tree (CIST). The CIST is the default tree used to interwork with other legacy bridges. It also serves as a fallback spanning tree if there are configuration problems with SPBV.

SPBV has been designed to manage a moderate number of bridges. SPBV differs from SPBM in that MAC addresses are learned on all bridges that lie on the shortest path, and shared VLAN learning is used since destination MACs may be associated with multiple SPVIDs. SPBV learns all MACs it forwards, even outside the SPBV region.

### Shortest Path Bridging-MAC

Shortest Path Bridging-MAC (SPBM) reuses the PBB data plane, which does not require that the Backbone Core Bridges (BCB) learn encapsulated client addresses. At the edge of the network, the C-MAC (client) addresses are learned. SPBM is very similar to Provider Link State Bridging (PLSB), using the same data and control planes, but the format and contents of the control messages in PLSB are not compatible.

Individual MAC frames of unicast traffic from an Ethernet-attached device that are received at the SPBM edge are encapsulated in a PBB IEEE 802.1ah header and then traverse the IEEE 802.1aq network unchanged until they are stripped of the encapsulation as they egress back to the non-participating attached network at the far side of the participating network.

Ethernet destination addresses (from UNI port attached devices) perform learning over the logical LAN and are forwarded to the appropriate participating B-MAC address to reach the far-end Ethernet destination. In this manner, Ethernet MAC addresses are never looked up in the core of an IEEE 802.1aq network. When comparing SPBM to PBB, the behavior is almost identical to a PBB IEEE 802.1ah network. PBB does not specify how B-MAC addresses are learned, and PBB may use a spanning tree to control the B-VLAN. In SPBM, the main difference is that B-MAC addresses are distributed or computed in the control plane, eliminating the B-MAC learning in PBB. Also, SPBM ensures that the route followed is the shortest path tree.

The forward and reverse paths used for unicast and multicast traffic in an IEEE 802.1aq network are symmetric. This symmetry permits IEEE 802.1ag Continuity Fault Management (CFM) to operate unchanged for SPBV and SPBM and has desirable properties with respect to time distribution protocols such as Precision Time Protocol.

Group address and unknown destination individual frames are optimally transmitted to only members of the same Ethernet service. IEEE 802.1aq supports the creation of thousands of logical Ethernet services in the form of E-LINE, E-LAN or E-TREE constructs, which are formed between non-participating logical ports of the IEEE 802.1aq network. These group address packets are encapsulated with a PBB header, which indicates the source participating address in the SA while the DA indicates the locally significant group address this frame should be forwarded on, and the source bridge where the frame originated. The IEEE 802.1aq multicast forwarding tables are created based on computations such that every bridge that is on the shortest path between a pair of bridges that are members of the same service group will create proper forwarding database (FDB) state to forward or replicate frames it receives to those members of that service group. Since the group address computation produces shortest path trees, there is only ever one copy of a multicast packet on any given link. Since only bridges on the shortest path between participating logical ports create FDB state, the multicast makes efficient use of network resources.

The actual group address forwarding operation operates more or less identically to classical Ethernet; the backbone destination address (B-DA)+ backbone VLAN identifier (B-VID) combination is looked up to find the egress set of next hops. The only difference compared with classical Ethernet is that reverse learning is disabled for participating bridge backbone media access control (B-MAC) addresses and is replaced with an ingress check and discard (when the frame arrives on an incoming interface from an unexpected source). Learning is, however, implemented at the edges of the SPBM multicast tree to learn the B-MAC to MAC address relationship for correct individual frame encapsulation in the reverse direction (as packets arrive over the interface).

Properly implemented, an IEEE 802.1aq network can support up to 1000 participating bridges and provide tens of thousands of layer-2 E-LAN services to Ethernet devices. This can be done by simply configuring the ports facing the Ethernet devices to indicate they are members of a given service. As new members come and go, the IS-IS protocol will advertise the I-SID membership changes and the computations will grow or shrink the trees in the participating node network as necessary to maintain the efficient multicast property for that service.

IEEE 802.1aq has the property that only the point of attachment of a service needs configuration when a new attachment point comes or goes. The trees produced by the computations will automatically be extended or pruned as necessary to maintain connectivity. In some existing implementations, this property is used to automatically (as opposed to through configuration) add or remove attachment points for dual-homed technologies such as rings to maintain optimum packet flow between a nonparticipating ring protocol and the IEEE 802.1aq network by activating a secondary attachment point and deactivating a primary attachment point.

### Failure recovery

Failure recovery is driven by IS-IS with the link failure being advertised and new computations being performed, resulting in new FDB tables. Since no Ethernet addresses are advertised or known by IS-IS, there is no re-learning required by the SPBM core and its learned encapsulations are unaffected by a transit node or link failure.

Link failure detection may be improved using IEEE 802.1ag Continuity Check Protocol (CCP), which tests link status and reports a failure to the IS-IS protocol. This allows much faster failure detection than is possible using the IS-IS hello message loss mechanisms.

Both SPBV and SPBM inherit the rapid convergence of a link-state control plane. A special attribute of SPBM is its ability to rebuild multicast trees in a similar time to unicast convergence, because it substitutes computation for signaling. When an SPBM bridge has performed the computations on a topology database, it knows whether it is on the shortest path between a root and one or more leaves of the SPT and can install state accordingly. Convergence is not gated by incremental discovery of a bridge's place on a multicast tree by the use of separate signaling transactions. However, SPBM on a node does not operate completely independently of its peers and enforces agreement on the current network topology with its peers. This very efficient mechanism uses the exchange of a single digest of link state covering the entire network view, and does not need agreement on each path to each root individually. The result is that the volume of messaging exchanged to converge the network is in proportion to the incremental change in topology and not the number of multicast trees in the network. A simple link event that may change many trees is communicated by signaling the link event only; the consequent tree construction is performed by local computation at each node. The addition of a single service access point to a service instance involves only the announcement of the I-SID, regardless of the number of trees. Similarly, the removal of a bridge, which might involve the rebuilding of hundreds to thousands of trees, is signaled only with a few link-state updates.

In a multi-chassis link aggregation group environment, multiple switch chassis appear as a single switch to the SPB control plane, and multiple links between pairs of chassis appear as an aggregate link. In this context, a single link or node failure is not seen by the control plane and is handled locally, potentially resulting in sub-50 ms recovery times.

### Animations

Three animated GIFs in this section help to show the behavior of 802.1aq.

The first of these gifs, shown in Figure 5, demonstrates the routing in a 66-node network where we have created a 7-member E-LAN using ISID 100. In this example, we show the equal cost tree (ECT) created from each member to reach all of the other members. We cycle through each member to show the full set of trees created for this service. We pause at one point to show the symmetry of routing between two of the nodes and emphasize it with a red line. In each case, the source of the tree is highlighted with a small purple V.

The second of these animated GIFs, shown in Figure 6, demonstrates 8 ECT paths in the same 66-node network as Figure 4. In each subsequent animated frame, the same source is used (in purple) but a different destination is shown (in yellow). For each frame, all of the shortest paths are shown superimposed between the source and destination. When two shortest paths traverse the same hop, the thickness of the lines being drawn is increased. In addition to the 66-node network, a small multi-level data center style network is also shown with sources and destinations both within the servers (at the bottom) and from servers to the router layer at the top. This animation helps to show the diversity of the ECT being produced.

The last of these animated GIFs, shown in Figure 7, demonstrates source-destination ECT paths using all 16 of the standard algorithms currently defined.

- (Figure 5 - Animated E-LAN example in a 66-node 802.1aq network with 7 members) Figure 5 - Animated E-LAN example in a 66-node 802.1aq network with 7 members
- (Figure 6 - Animated ECT example in a 66-node 802.1aq network with 8 ECT) Figure 6 - Animated ECT example in a 66-node 802.1aq network with 8 ECT
- (Figure 7 - Animated ECT example 36-node 802.1aq network with 16 ECT) Figure 7 - Animated ECT example 36-node 802.1aq network with 16 ECT


## Details

### Equal cost multi tree

Sixteen equal cost multi-tree (ECMT) paths are initially defined; however, there are many more possible. ECMT in an IEEE 802.1aq network is more predictable than with internet protocol (IP) or multiprotocol label switching (MPLS) because of symmetry between the forward and reverse paths. The choice as to which ECMT path will be used is therefore an operator-assigned head-end decision, while it is a local or hashing decision with IP/MPLS.

IEEE 802.1aq, when faced with a choice between two equal link cost paths, uses the following logic for its first ECMT tie-breaking algorithm: first, if one path is shorter than the other in terms of hops, the shorter path is chosen; otherwise, the path with the minimum Bridge Identifier (BridgePriority concatenated with IS-IS SysID) is chosen. Other ECMT algorithms are created by simply using known permutations of the BridgePriority and SysIDs. For example, the second defined ECMT algorithm uses the path with the minimum of the inverse of the BridgeIdentifier and can be thought of as taking the path with the maximum node identifier. For SPBM, each permutation is instantiated as a distinct B-VID. The upper limit of multipath permutations is gated by the number of B-VIDs delegated to 802.1aq operation, a maximum of 4094, although the number of useful path permutations would only require a fraction of the available B-VID space. Fourteen additional ECMT algorithms are defined with different bit masks applied to the BridgeIdentifiers. Since the BridgeIdentifier includes a priority field, it is possible to adjust the ECMT behavior by changing BridgePriority.

A service is assigned to a given ECMT B-VID at the edge of the network by configuration. As a result, non-participating packets associated with that service are encapsulated with the VID associated with the desired ECMT end-to-end path. All individual and group address traffic associated with this service will therefore use the proper ECMT B-VID and be carried symmetrically end to end on the proper equal cost multi path. Essentially, the operator decides which services go in which ECMT paths, unlike a hashing solution used in other systems, such as IP/MPLS. Trees can support hashing associated with link aggregation (LAG) groups within a tree branch segment.

This symmetric and end-to-end ECMT behavior gives IEEE 802.1aq a predictable behavior, and offline engineering tools can model data flows. The behavior is also advantageous to networks where one-way delay measurements are important. The one-way delay can be computed as half the round-trip delay. Such computations are used by time distribution protocols such as IEEE 1588.

Shown above are three figures [5,6,7] which show 8 and 16 equal cost tree (ECT) behavior in different network topologies. These are composites of screen captures of an 802.1aq network emulator and show the source in purple, the destination in yellow, and then all the computed and available shortest paths in pink. The thicker the line, the more shortest paths use that link. The animations show three different networks and a variety of source and destination pairs, which continually change to help visualize what is happening.

The equal cost tree (ECT) algorithms can be almost extended through the use of OPAQUE data, which allows extensions beyond the base 16 algorithms more or less infinitely. It is expected that other standards groups or vendors will produce variations on the currently defined algorithms with behaviors suited for different network styles. It is expected that numerous shared tree models will also be defined, as will hop-by-hop hash-based equal-cost multi-path (ECMP) style behaviors, all defined by a VID and an algorithm that every node agrees to run.

### Traffic engineering

802.1aq does not spread traffic on a hop-by-hop basis. Instead, 802.1aq allows assignment of a Service ID (ISID) to a VLAN ID (VID) at the edge of the network. A VID will correspond to exactly one of the possible sets of shortest path nodes in the network and will never stray from that routing. If there are 10 or so shortest paths between different nodes, it is possible to assign different services to different paths and to know that the traffic for a given service will follow exactly the given path. In this manner, traffic can easily be assigned to the desired shortest path. In the event that one of the paths becomes overloaded, it is possible to move some services off that shortest path by reassigning those services' ISID to a different, less loaded, VID at the edges of the network.

The deterministic nature of the routing simplifies offline prediction, computation and experimentation with network loading since actual routes are not dependent on the contents of the packet headers except for the VID.

Figure 4 shows four different equal-cost paths between nodes 7 and 5. An operator can achieve a relatively good balance of traffic across the cut between nodes [0 and 2] and [1 and 3] by assigning the services at nodes 7 and 5 to one of the four desired VIDs. Using more than 4 equal cost tree (ECT) paths in the network will likely allow all 4 of these paths to be used. Balance can also be achieved between nodes 6 and 4 in a similar manner.

In the event that an operator does not wish to manually assign services to shortest paths, it is a simple matter for a switch vendor to allow a simple hash of the ISID to one of the available VIDS to give a degree of non-engineered spreading. For example, the ISID modulo the number of ECT-VIDs could be used to decide on the actual relative VID to use.

In the event that the ECT paths are not sufficiently diverse, the operator has the option of adjusting the inputs to the distributed ECT algorithms to apply attraction or repulsion from a given node by adjusting that node's Bridge Priority. This can be experimented with via offline tools until the desired routes are achieved, at which point the bias can be applied to the real network and then ISIDs can be moved to the resulting routes.

Looking at the animations in Figure 6 shows the diversity available for traffic engineering in a 66-node network. In this animation, there are 8 ECT paths available from each highlighted source to destination and therefore services could be assigned to 8 different pools based on the VID. One such initial assignment in Figure 6 could therefore be (ISID modulo 8) with subsequent fine tuning as required.

### Example

We will work through SPBM behavior on a small example, with emphasis on the shortest-path trees for unicast and multicast.

The network shown in Figure 1 consists of 8 participating nodes numbered 0 through 7. These would be switches or routers running the IEEE 802.1aq protocol. Each of the 8 participating nodes has a number of adjacencies numbered 1..5. These would likely correspond to interface indexes, or possibly port numbers. Since 802.1aq does not support parallel interfaces, each interface corresponds to an adjacency. The port and interface index numbers are, of course, local and are shown because the output of the computations produces an interface index (in the case of unicast) or a set of interface indexes (in the case of multicast), which are part of the forwarding information base (FIB) together with a destination MAC address and backbone VID.

The network has a fully meshed inner core of four nodes (0..3) and then four outer nodes (4,5,6 and 7), each dual-homed onto a pair of inner core nodes.

Normally, when nodes come from the factory, they have a MAC address assigned, which becomes a node identifier, but for the purpose of this example, we will assume that the nodes have MAC addresses of the form 00:00:00:00:N:00 where N is the node id (0..7) from Figure 1. Therefore, node 2 has a MAC address of 00:00:00:00:02:00. Node 2 is connected to node 7 (00:00:00:00:07:00) via node 2's interface/5.

The IS-IS protocol runs on all the links shown since they are between participating nodes. The IS-IS hello protocol has a few additions for 802.1aq, including information about backbone VIDs to be used by the protocol. We will assume that the operator has chosen to use backbone VIDs 101 and 102 for this instance of 802.1aq on this network.

The node will use its MAC addresses as the IS-IS SysId and join a single IS-IS level and exchange link-state packets (LSPs in IS-IS terminology). The LSPs will contain node information and link information such that every node will learn the full topology of the network. Since we have not specified any link weights in this example, the IS-IS protocol will pick a default link metric for all links; therefore, all routing will be minimum hop count.

After topology discovery, the next step is distributed calculation of the unicast routes for both ECMP VIDs and population of the unicast forwarding tables (FIBs).

Consider the route from Node 7 to Node 5: there are a number of equal-cost paths. 802.1aq specifies how to choose two of them: the first is referred to as the Low PATH ID path. This is the path that has the minimum node id on it. In this case, the Low PATH ID path is the 7->0->1->5 path (as shown in red in Figure 2). Therefore, each node on that path will create a forwarding entry toward the MAC address of node five using the first ECMP VID 101. Conversely, 802.1aq specifies a second ECMP tie-breaking algorithm called High PATH ID. This is the path with the maximum node identifier on it and in the example is the 7->2->3->5 path (shown in blue in Figure 2).

Node 7 will therefore have a FIB that, among other thing,s indicates:

- MAC 00:00:00:05:00 / vid 101 the next hop is interface/1.
- MAC 00:00:00:05:00 / vid 102 the next hop is interface/2.

Node 5 will have exactly the inverse in its FIB:

- MAC 00:00:00:07:00 / vid 101 the next hop is interface/1.
- MAC 00:00:00:07:00 / vid 102 the next hop is interface/2.

The intermediate nodes will also produce consistent results, so, for example, node 1 will have the following entries.

- MAC 00:00:00:07:00 / vid 101 the next hop is interface/5.
- MAC 00:00:00:07:00 / vid 102 the next hop is interface/4.
- MAC 00:00:00:05:00 / vid 101 the next hop is interface/2.
- MAC 00:00:00:05:00 / vid 102 the next hop is interface/2.

And Node 2 will have entries as follows:

- MAC 00:00:00:05:00 / vid 101 the next hop is interface/2.
- MAC 00:00:00:05:00 / vid 102 the next hop is interface/3.
- MAC 00:00:00:07:00 / vid 101 the next hop is interface/5.
- MAC 00:00:00:07:00 / vid 102 the next hop is interface/5.

If we had an attached non-participating device at Node 7 talking to a non-participating device at Node 5 (for example, Device A talks to Device C in Figure 3), they would communicate over one of these shortest paths with a MAC-in-MAC encapsulated frame. The MAC header on any of the NNI links would show an outer source address of 00:00:00:70:00, an outer destination address of 00:00:00:50:00 and a BVID of either 101 or 102, depending on which has been chosen for this set of non-participating ports/vids. The header, once inserted at node 7 when received from node A, would not change on any of the links until it egressed back to non-participating Device C at Node 5. All participating devices would do a simple DA+VID lookup to determine the outgoing interface, and would also check that the incoming interface is the proper next hop for the packet's SA+VID. The addresses of the participating nodes 00:00:00:00:00:00 ... 00:00:00:07:00 are never learned but are advertised by IS-IS as the node's SysId.

Unicast forwarding to a non-participating client (e.g., A, B, C, D from Figure 3) address is, of course, only possible when the first hop participating node (e.g., 7) is able to know which last hop participating node (e.g., 5) is attached to the desired non-participating node (e.g., C). Since this information is not advertised by IEEE 802.1aq, it has to be learned. The mechanism for learning is identical to IEEE 802.1ah. In short, the corresponding outer MAC unicast DA, if not known, is replaced by a multicast DA, and when a response is received, the SA of that response now tells us the DA to use to reach the non-participating node that sourced the response. e.g., node 7 learns that C is reached by node 5.

Since we wish to group/scope sets of non-participating ports into services and prevent them from multicasting to each other, IEEE 802.1aq provides a mechanism for per-source, per-service multicast forwarding and defines a special multicast destination address format to provide this. Since the multicast address must uniquely identify the tree, and because there is a tree per source per unique service, the multicast address contains two components: a service component in the low-order 24 bits and a network-wide unique identifier in the upper 22 bits. Since this is a multicast address, the multicast bit is set, and since we are not using the standard OUI space for these manufactured addresses, the Local 'L' bit is set to disambiguate these addresses. In Figure 3 above, this is represented with the DA=[7,O] where the 7 represents packets originating from node 7 and the colored O represents the E-LAN service we are scoped within.

Prior to creating multicast forwarding for a service, nodes with ports that face that service must be told they are members. For example, nodes 7, 4, 5 and 6 are told they are members of the given service, for example, service 200, and further that they should be using BVID 101. This is advertised by ISIS and all nodes then do the SPBM computation to determine if they are participating either as a head end or tail end, or a tandem point between other head and tail ends in the service. Since node 0 is a tandem between nodes 7 and 5, it creates a forwarding entry for packets from node 7 on this service, to node 5. Likewise, since it is a tandem between nodes 7 and 4 it creates forwarding state from node 7 for packets in this service to node 4. This results in a true multicast entry where the DA/VID has outputs on two interfaces, 1 and 2. Node 2, on the other hand, is only on one shortest path in this service and only creates a single forwarding entry from node 7 to node 6 for packets in this service.

Figure 3 only shows a single E-LAN service and only the tree from one of the members; however, very large numbers of E-LAN services with membership from 2 to every node in the network can be supported by advertising the membership, computing the tandem behaviors, manufacturing the known multicast addresses and populating the FIBs. The only real limiting factors are the FIB table sizes and computational power of the individual devices, both of which are growing yearly in leaps and bounds.

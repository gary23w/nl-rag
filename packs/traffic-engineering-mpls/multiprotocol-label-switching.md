---
title: "Multiprotocol Label Switching"
source: https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching
domain: traffic-engineering-mpls
license: CC-BY-SA-4.0
tags: mpls traffic engineering, label distribution, resource reservation, path signaling
fetched: 2026-07-02
---

# Multiprotocol Label Switching

**Multiprotocol Label Switching** (**MPLS**) is a routing technique in telecommunications networks that directs data from one node to the next based on labels rather than network addresses. Whereas network addresses identify endpoints, MPLS labels identify established paths between endpoints. MPLS can encapsulate packets of various network protocols and supports a range of access technologies, including T1/E1, ATM, Frame Relay, and DSL.

MPLS was originally developed to improve packet forwarding by reducing the reliance on complex routing table lookups. With the introduction of hardware-based forwarding engines, forwarding speed is no longer the main reason for deployment, and MPLS today is more often used for traffic engineering, differentiated services quality of service, and BGP/MPLS IP virtual private networks (VPNs).

In an MPLS network, packet-forwarding decisions are made solely on the contents of labels, without the need to examine the packet itself. This allows for the creation of end-to-end connections across any type of transport medium, using any protocol. The primary benefit is to eliminate dependence on a particular OSI data link layer technology, and eliminate the need for multiple layer-2 networks to satisfy different types of traffic. Multiprotocol label switching belongs to the family of packet-switched networks.

MPLS operates at a layer between traditional definitions of OSI Layer 2 (data link layer) and Layer 3 (network layer), and is often referred to as a *layer 2.5* protocol. It was designed to provide a unified data-carrying service for both circuit-based clients and packet-switching clients which provide a datagram service model. It can be used to carry many different kinds of traffic, including IP packets, as well as native Asynchronous Transfer Mode (ATM), Frame Relay, Synchronous Optical Networking (SONET) or Ethernet.

MPLS can exist in both an IPv4 and an IPv6 environment, using appropriate routing protocols. The major goal of MPLS development was the increase of routing speed. This goal is no longer relevant because of the usage of newer switching methods such as ASIC, TCAM and CAM-based switching able to forward plain IPv4 as fast as MPLS labeled packets. Now, therefore, the main benefit of MPLS is to implement limited traffic engineering and layer 3 or layer 2 service provider type VPNs over IPv4 networks.

MPLS is standardized by the IETF in RFC 3031. It is deployed to connect as few as two facilities to very large deployments. In practice, MPLS is mainly used to forward IP protocol data units and Virtual Private LAN Service (VPLS) Ethernet traffic. Major applications of MPLS are telecommunications traffic engineering and MPLS VPN. MPLS works in conjunction with the Internet Protocol (IP) and its routing protocols, usually interior gateway protocols (IGPs) and supports the creation of dynamic, transparent virtual networks with support for traffic engineering, the ability to transport layer VPNs with overlapping address spaces, and for layer-2 pseudowires that are capable of transporting a variety of transport payloads (IPv4, IPv6, ATM, Frame Relay, etc.).

## History

In 1996 a group from Ipsilon Networks proposed a *flow management protocol*. Their *IP Switching* technology, which was defined only to work over ATM, did not achieve market dominance. Cisco Systems introduced a related proposal, not restricted to ATM transmission, called *Tag Switching* with its Tag Distribution Protocol (TDP). It was a Cisco proprietary proposal, and was renamed *Label Switching*. It was handed over to the Internet Engineering Task Force (IETF) for open standardization. The IETF formed the MPLS Working Group in 1997. Work involved proposals from other vendors, and development of a consensus protocol that combined features from several vendors' work.

Some time later it was recognized that the work on threaded indices by Girish Chandranmenon and George Varghese had invented the idea of using labels to represent destination prefixes that was central to tag switching.

One original motivation was to allow the creation of simple high-speed switches since for a significant length of time it was considered impractical to forward IP packets entirely in hardware. Advances in VLSI and in forwarding algorithms have made hardware forwarding of IP packets possible and common. The current advantages of MPLS primarily revolve around the ability to support multiple service models and perform traffic management. MPLS also offers a robust recovery framework that goes beyond the simple protection rings of synchronous optical networking (SONET/SDH).

A number of different technologies were previously deployed with essentially identical goals, such as Frame Relay and ATM. Frame Relay and ATM use *labels* to move frames or cells through a network. The header of the Frame Relay frame and the ATM cell refers to the virtual circuit that the frame or cell resides on. The similarity between Frame Relay, ATM, and MPLS is that at each hop throughout the network, the *label* value in the header is changed. This is different from the forwarding of IP packets.

MPLS technologies have evolved with the strengths and weaknesses of ATM in mind. MPLS is designed to have lower overhead than ATM while providing connection-oriented services for variable-length frames, and has replaced much use of ATM in the market. MPLS dispenses with the cell-switching and signaling-protocol baggage of ATM. MPLS recognizes that small ATM cells are not needed in the core of modern networks, since modern optical networks are fast enough that even full-length 1500-byte packets do not incur significant real-time queuing delays. At the same time, MPLS attempts to preserve the traffic engineering (TE) and out-of-band control that made Frame Relay and ATM attractive for deploying large-scale networks.

### Dates

- 1994: Toshiba presented Cell Switch Router (CSR) ideas to IETF BOF
- 1995: George Varghese and Girish Chandranmenon published paper on threaded indices, a form of label switching, at ACM SIGCOMM annual conference
- 1996: Ipsilon, Cisco and IBM announced label-switching plans
- 1997: Formation of the IETF MPLS working group
- 1999: First MPLS VPN (L3VPN) and TE deployments
- 2000: MPLS Traffic Engineering
- 2001: First MPLS Request for Comments (RFC) published
- 2002: AToM (L2VPN)
- 2004: GMPLS; Large-scale L3VPN
- 2006: Large-scale TE "Harsh"
- 2007: Large-scale L2VPN
- 2009: Label Switching Multicast
- 2011: MPLS transport profile

## Operation

MPLS works by prefixing packets with an MPLS header, containing one or more labels. This is called a label stack.

MPLS packet structure

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

MPLS Label [1]

4

32

MPLS Label [2]

⋮

⋮

⋮

⋮

⋮

MPLS Label [n]

4n

32n

Packet

⋮

⋮

⋮

⋮

Each entry in the label stack contains four fields:

MPLS Label

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Label

TC

S

Time to Live

**Label: 20 bits**

A label with the value of 1 represents the

router alert label

.

**Traffic Class (TC): 3 bits**

Field for QoS (

quality of service

) priority and ECN (

Explicit Congestion Notification

). Prior to 2009 this field was called EXP.

**Bottom of Stack (S): 1 bit**

If this flag is set, it signifies that the current label is the last in the stack.

**Time to Live (TTL): 8 bits**

Time to live.

These MPLS-labeled packets are switched based on the label instead of a lookup in the IP routing table. When MPLS was conceived, label switching was faster than a routing table lookup because switching could take place directly within the switched fabric and avoided CPU and software involvement.

The presence of such a label has to be indicated to the switch. In the case of Ethernet frames this is done through the use of EtherType values 0x8847 and 0x8848, for unicast and multicast connections respectively.

### Equipment

CE

P

/

LSR

PE

/

ELSR

MPLS VPN

network diagram with wikilinks

#### Label switch router

An MPLS router that performs routing based only on the label is called a **label switch router** (**LSR**) or **transit router**. This is a type of router located in the middle of an MPLS network. It is responsible for switching the labels used to route packets.

When an LSR receives a packet, it uses the label included in the packet header as an index to determine the next hop on the label-switched path (LSP) and a corresponding label for the packet from a Label Information Base. The old label is then removed from the header and replaced with the new label before the packet is routed forward.

#### Label edge router

A **label edge router** (LER, also **edge LSR** (which is "technically more correct") or simply *edge router*) is a router that operates at the edge of an MPLS network and acts as the entry and exit points for the network. LERs *push* an MPLS label onto an incoming packet and *pop* it off an outgoing packet. Alternatively, under penultimate hop popping this function may instead be performed by the LSR directly connected to the LER.

When forwarding an IP datagram into the MPLS domain, a LER uses routing information to determine the appropriate label to be affixed, labels the packet accordingly, and then forwards the labeled packet into the MPLS domain. Likewise, upon receiving a labeled packet that is destined to exit the MPLS domain, the LER strips off the label and forwards the resulting IP packet using normal IP forwarding rules.

#### Provider router

In the specific context of an MPLS-based virtual private network (VPN), LERs that function as ingress or egress routers to the VPN are often called provider edge (PE) routers. Devices that function only as transit routers are similarly called provider (P) routers. The job of a P router is significantly easier than that of a PE router.

### Label Distribution Protocol

Labels may be distributed between LERs and LSRs using the Label Distribution Protocol (LDP) or Resource Reservation Protocol (RSVP). LSRs in an MPLS network regularly exchange label and reachability information with each other using standardized procedures in order to build a complete picture of the network so that they can then use that information to forward the packets.

### Label-switched paths

Label-switched paths (LSPs) are established by the network operator for a variety of purposes, such as to create network-based IP virtual private networks or to route traffic along specified paths through the network. In many respects, LSPs are not different from permanent virtual circuits (PVCs) in ATM or Frame Relay networks, except that they are not dependent on a particular layer-2 technology.

### Routing

When an unlabeled packet enters the ingress router and needs to be passed on to an MPLS tunnel, the router first determines the forwarding equivalence class (FEC) for the packet and then inserts one or more labels in the packet's newly created MPLS header. The packet is then passed on to the next hop router for this tunnel.

From an OSI model perspective, the MPLS Header is added between the network layer header and link layer header.

When a labeled packet is received by an MPLS router, the topmost label is examined. Based on the contents of the label a *swap*, *push* or *pop* operation is performed on the packet's label stack. Routers can have prebuilt lookup tables that tell them which kind of operation to do based on the topmost label of the incoming packet so they can process the packet very quickly.

- In a *swap* operation the label is swapped with a new label, and the packet is forwarded along the path associated with the new label.
- In a *push* operation a new label is pushed on top of the existing label, effectively *encapsulating* the packet in another layer of MPLS. This allows hierarchical routing of MPLS packets. Notably, this is used by MPLS VPNs.
- In a *pop* operation the label is removed from the packet, which may reveal an inner label below. This process is called *decapsulation*. If the popped label was the last on the label stack, the packet *leaves* the MPLS tunnel. This can be done by the egress router, or at the penultimate hop.

During these operations, the contents of the packet below the MPLS Label stack are not examined. Indeed, transit routers typically need only to examine the topmost label on the stack. The forwarding of the packet is done based on the contents of the labels, which allows protocol-independent packet forwarding that does not need to look at a protocol-dependent routing table and avoids the expensive IP longest prefix match at each hop.

At the egress router, when the last label has been popped, only the payload remains. This can be an IP packet or any type of packet. The egress router must, therefore, have routing information for the packet's payload since it must forward it without the help of label lookup tables. An MPLS transit router has no such requirement.

Usually, the last label is popped off at the penultimate hop (the hop before the egress router). This is called penultimate hop popping (PHP). This is useful in cases where the egress router has many packets leaving MPLS tunnels and thus spends significant CPU resources on these transitions. By using PHP, transit routers connected directly to this egress router effectively offload it, by popping the last label themselves. In the label distribution protocols, this PHP label pop action is advertised as label value 3 (implicit null) and is never found in a label, since it means that the label is to be popped.

Several MPLS services including end-to-end QoS management, and 6PE, require keeping a label even between the penultimate and the last MPLS router, with a label disposition always done on the last MPLS router, ultimate hop popping (UHP). Some specific label values have been notably reserved for this use. In this scenario the remaining label stack entry conveys information to the last hop (such as its Traffic Class field for QoS information), while also instructing the last hop to pop the label stack using one of the following reserved label values:

- 0: Explicit-null for IPv4
- 2: Explicit-null for IPv6

An MPLS header does not identify the type of data carried inside the MPLS path. To carry two different types of traffic between the same two routers, with different treatment by the core routers for each type, a separate MPLS path for each type of traffic is required.

#### Label-switched path

A label-switched path (LSP) is a path through an MPLS network set up by the NMS or by a signaling protocol such as LDP, RSVP-TE, BGP (or the now deprecated CR-LDP). The path is set up based on criteria in the FEC.

The path begins at an LER, which makes a decision on which label to prefix to a packet based on the appropriate FEC. It then forwards the packet along to the next router in the path, which swaps the packet's outer label for another label, and forwards it to the next router. The last router in the path removes the label from the packet and forwards the packet based on the header of its next layer, for example IPv4. Due to the forwarding of packets through an LSP being opaque to higher network layers, an LSP is also sometimes referred to as an MPLS tunnel.

The router which first prefixes the MPLS header to a packet is an ingress router. The last router in an LSP, which pops the label from the packet, is called an egress router. Routers in between, which need only swap labels, are called transit routers or label switch routers (LSRs).

Note that LSPs are unidirectional; they enable a packet to be label switched through the MPLS network from one endpoint to another. Since bidirectional communication is typically desired, the aforementioned dynamic signaling protocols can automatically set up a separate LSP in the opposite direction.

When link protection is considered, LSPs can be categorized as primary (working), secondary (backup) and tertiary (LSP of last resort).

### Installing and removing paths

There are two standardized protocols for managing MPLS paths: the Label Distribution Protocol (LDP) and RSVP-TE, an extension of the Resource Reservation Protocol (RSVP) for traffic engineering. Furthermore, there exist extensions of the Border Gateway Protocol (BGP) that can be used to manage an MPLS path.

### Multicast addressing

Multicast was, for the most part, an afterthought in MPLS design. It was introduced by point-to-multipoint RSVP-TE. It was driven by service provider requirements to transport broadband video over MPLS.

The hub and spoke multipoint LSP (HSMP LSP) was also introduced by IETF. HSMP LSP is mainly used for multicast, time synchronization, and other purposes.

## Relationship to Internet Protocol

MPLS works in conjunction with the Internet Protocol (IP) and its routing protocols, usually interior gateway protocols (IGPs). MPLS LSPs provide dynamic, transparent virtual networks with support for traffic engineering, the ability to transport layer-3 (IP) VPNs with overlapping address spaces, and support for layer-2 pseudowires using Pseudowire Emulation Edge-to-Edge (PWE3) that are capable of transporting a variety of transport payloads (IPv4, IPv6, ATM, Frame Relay, etc.). MPLS-capable devices are referred to as LSRs. The paths an LSR knows can be defined using explicit hop-by-hop configuration, or are dynamically routed by the Constrained Shortest Path First (CSPF) algorithm, or are configured as a loose route that avoids a particular IP address or that is partly explicit and partly dynamic.

In a pure IP network, the shortest path to a destination is chosen even when the path becomes congested. Meanwhile, in an IP network with MPLS Traffic Engineering CSPF routing, constraints such as the RSVP bandwidth of the traversed links can also be considered, such that the shortest path with available bandwidth will be chosen. MPLS Traffic Engineering relies upon the use of TE extensions to Open Shortest Path First (OSPF) or Intermediate System to Intermediate System (IS-IS) and RSVP. In addition to the constraint of RSVP bandwidth, users can also define their own constraints by specifying link attributes and special requirements for tunnels to route (or not to route) over links with certain attributes.

For end-users the use of MPLS is not visible directly, but can be assumed when doing a traceroute: only nodes that do *full* IP routing are shown as hops in the path, thus not the MPLS nodes used in between, therefore when you see that a packet *hops* between two very distant nodes and hardly any other *hop* is seen in that provider's network (or AS) it is very likely that network uses MPLS.

### MPLS local protection

In the event of a network element failure when recovery mechanisms are employed at the IP layer, restoration may take several seconds which may be unacceptable for real-time applications such as VoIP. In contrast, MPLS local protection meets the requirements of real-time applications with recovery times comparable to those of shortest path bridging networks or SONET rings of less than 50 ms.

## Comparisons

MPLS can make use of existing ATM network or Frame Relay infrastructure, as its labeled flows can be mapped to ATM or Frame Relay virtual-circuit identifiers, and vice versa.

### Frame Relay

Frame Relay aimed to make more efficient use of existing physical resources, which allow for the underprovisioning of data services by telecommunications companies (telcos) to their customers, as clients were unlikely to be utilizing a data service 100 percent of the time. Consequently, oversubscription of capacity by the telcos, while financially advantageous to the provider, can directly affect overall performance.

Telcos often sold Frame Relay to businesses looking for a cheaper alternative to dedicated lines; its use in different geographic areas depended greatly on governmental and telecommunication companies' policies.

Many customers migrated from Frame Relay to MPLS over IP or Ethernet, which in many cases reduced costs and improved manageability and performance of their wide area networks.

### Asynchronous Transfer Mode

While the underlying protocols and technologies are different, both MPLS and ATM provide a connection-oriented service for transporting data across computer networks. In both technologies, connections are signaled between endpoints, the connection state is maintained at each node in the path, and encapsulation techniques are used to carry data across the connection. Excluding differences in the signaling protocols (RSVP/LDP for MPLS and PNNI for ATM) there still remain significant differences in the behavior of the technologies.

The most significant difference is in the transport and encapsulation methods. MPLS is able to work with variable-length packets while ATM uses fixed-length (53 bytes) cells. Packets must be segmented, transported and re-assembled over an ATM network using an adaptation layer, which adds significant complexity and overhead to the data stream. MPLS, on the other hand, simply adds a label to the head of each packet and transmits it on the network.

Differences exist, as well, in the nature of the connections. An MPLS connection (LSP) is unidirectional, allowing data to flow in only one direction between two endpoints. Establishing two-way communications between endpoints requires a pair of LSPs be established. Because two LSPs are used, data flowing in the forward direction may use a different path from data flowing in the reverse direction. ATM point-to-point connections (virtual circuits), on the other hand, are bidirectional, allowing data to flow in both directions over the same path.

Both ATM and MPLS support tunneling of connections inside connections. MPLS uses label stacking to accomplish this while ATM uses *virtual paths*. MPLS can stack multiple labels to form tunnels within tunnels. The ATM virtual path indicator (VPI) and virtual circuit indicator (VCI) are both carried together in the cell header, limiting ATM to a single level of tunneling.

The biggest advantage that MPLS has over ATM is that it was designed from the start to be complementary to IP. Modern routers can support both MPLS and IP natively across a common interface allowing network operators great flexibility in network design and operation. ATM's incompatibilities with IP require complex adaptation, making it comparatively less suitable for today's predominantly IP networks.

## Deployment

MPLS is standardized by the IETF in RFC 3031. It is deployed to connect as few as two facilities to very large deployments. In practice, MPLS is mainly used to forward IP protocol data units (PDUs) and Virtual Private LAN Service (VPLS) Ethernet traffic. Major applications of MPLS are telecommunications traffic engineering and MPLS VPN.

## Evolution

MPLS was originally proposed to allow high-performance traffic forwarding and traffic engineering in IP networks. However, it evolved in Generalized MPLS (GMPLS) to also allow the creation of LSPs in non-native IP networks, such as SONET/SDH networks and wavelength switched optical networks.

## Competing protocols

MPLS can exist in both an IPv4 and an IPv6 environment, using appropriate routing protocols. The major goal of MPLS development was the increase of routing speed. This goal is no longer relevant because of the usage of newer switching methods such as ASIC, TCAM and CAM-based switching able to forward plain IPv4 as fast as MPLS labeled packets. Now, therefore, the main benefit of MPLS is to implement limited traffic engineering and layer 3 or layer 2 service provider type VPNs over IPv4 networks.

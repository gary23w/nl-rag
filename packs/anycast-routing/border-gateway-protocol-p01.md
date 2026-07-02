---
title: "Border Gateway Protocol (part 1/2)"
source: https://en.wikipedia.org/wiki/Border_Gateway_Protocol
domain: anycast-routing
license: CC-BY-SA-4.0
tags: anycast routing, anycast addressing, content delivery, route selection
fetched: 2026-07-02
part: 1/2
---

# Border Gateway Protocol

**Border Gateway Protocol** (**BGP**) is a standardized exterior gateway protocol designed to exchange routing and reachability information among autonomous systems (AS) on the Internet. BGP is classified as a path-vector routing protocol, and it makes routing decisions based on paths, network policies, or rule-sets configured by a network administrator.

BGP used for routing within an autonomous system is called **Interior Border Gateway Protocol** (**iBGP**). In contrast, the Internet application of the protocol is called **Exterior Border Gateway Protocol** (**EBGP**).


## History

In January 1989, at the 12th IETF meeting in Austin, Texas, Yakov Rekhter, Len Bosack, and Kirk Lougheed sat down at a table to design what ultimately became the Border Gateway Protocol (BGP). The initial BGP design was recorded on two napkins, hence often referenced to as the “Two-Napkin Protocol”. The design on the napkins was expanded to three hand-written sheets of paper from which the first interoperable BGP implementation was quickly developed. A photocopy of these three sheets of paper now hangs on the wall of a routing protocol development area at Cisco Systems in Milpitas, California. In the same year, RFC 1105 was published, and the BGP protocol (in various forms) has been in use on the Internet since 1994.

Half a year after the initial publication, the protocol definition was changed in 1990 with the publication of RFC 1136. In October 1991, BGP version 3 was defined in RFC 1267, obsoleting the two earlier versions. In 1994, the current version (BGP4), was published as RFC 1654. Its definition was replaced in March 1995 by RFC 1771. In January 2006, RFC 4271 was published, which currently is the latest definition of BGP4 (although updated by many other RFCs).

RFC 4271 corrected errors, clarified ambiguities and updated the specification with common industry practices. The major enhancement of BGP4 was the support for Classless Inter-Domain Routing (CIDR) and use of route aggregation to decrease the size of routing tables. In its native form, the BGP4 protocol can only work with IPv4 addresses. Since the publication of RFC 2283 in 1998, routing information about a wide range of "address families" (IPv4, IPv6, IPX, etc.) can be carried. The 'Multiprotocol Extensions' have been updated in 2000 with RFC 2858 and finally in 2007 with RFC 4760. With these extensions, the protocol is also referred to as Multiprotocol BGP (MP-BGP).


## Operation

BGP neighbors, called peers, are established by manual configuration among routers to create a TCP session on port 179. A BGP speaker sends 19-byte keep-alive messages every 30 seconds (protocol default value, tunable) to maintain the connection. Among routing protocols, BGP is unique in using TCP as its transport protocol.

When BGP runs between two peers in the same autonomous system (AS), it is referred to as *Internal BGP* (*iBGP* or *Interior Border Gateway Protocol*). When it runs between different autonomous systems, it is called *External BGP* (*eBGP* or *Exterior Border Gateway Protocol*). Routers on the boundary of one AS exchanging information with another AS are called *border* or *edge routers* or simply *eBGP peers* and are typically connected directly, while *iBGP peers* can be interconnected through other intermediate routers. Other deployment topologies are also possible, such as running eBGP peering inside a VPN tunnel, allowing two remote sites to exchange routing information in a secure and isolated manner.

The main difference between iBGP and eBGP peering is in the way routes that were received from one peer are typically propagated by default to other peers:

- New routes learned from an eBGP peer are re-advertised to all iBGP and eBGP peers.
- New routes learned from an iBGP peer are re-advertised to all eBGP peers only.

These route-propagation rules effectively require that all iBGP peers inside an AS are interconnected in a full mesh with iBGP sessions.

How routes are propagated can be controlled in detail via the *route-maps* mechanism. This mechanism consists of a set of rules. Each rule describes, for routes matching some given criteria, what action should be taken. The action could be to drop the route, or it could be to modify some attributes of the route before inserting it in the routing table.

### Extensions negotiation

During the peering handshake, when OPEN messages are exchanged, BGP speakers can negotiate optional capabilities of the session, including multiprotocol extensions and various recovery modes. If the multiprotocol extensions to BGP are negotiated at the time of creation, the BGP speaker can prefix the Network Layer Reachability Information (NLRI) it advertises with an address family prefix. These families include the IPv4 (default), IPv6, IPv4/IPv6 Virtual Private Networks and multicast BGP. Increasingly, BGP is used as a generalized signaling protocol to carry information about routes that may not be part of the global Internet, such as VPNs.

In order to make decisions in its operations with peers, a BGP peer uses a simple finite-state machine (FSM) that consists of six states: Idle; Connect; Active; OpenSent; OpenConfirm; and Established. For each peer-to-peer session, a BGP implementation maintains a state variable that tracks which of these six states the session is in. The BGP defines the messages that each peer should exchange in order to change the session from one state to another.

The first state is the Idle state. In the Idle state, BGP initializes all resources, refuses all inbound BGP connection attempts and initiates a TCP connection to the peer. The second state is Connect. In the Connect state, the router waits for the TCP connection to complete and transitions to the OpenSent state if successful. If unsuccessful, it starts the ConnectRetry timer and transitions to the Active state upon expiration. In the Active state, the router resets the ConnectRetry timer to zero and returns to the Connect state. In the OpenSent state, the router sends an Open message and waits for one in return in order to transition to the OpenConfirm state. Keepalive messages are exchanged and, upon successful receipt, the router is placed into the Established state. In the Established state, the router can send and receive: Keepalive; Update; and Notification messages to and from its peer.

- **Idle State**:
  - Refuse all incoming BGP connections.
  - Start the initialization of event triggers.
  - Initiates a TCP connection with its configured BGP peer.
  - Listens for a TCP connection from its peer.
  - Changes its state to Connect.
  - If an error occurs at any state of the FSM process, the BGP session is terminated immediately and returned to the Idle state. Some of the reasons why a router does not progress from the Idle state are:
    - TCP port 179 is not open.
    - A random TCP port over 1023 is not open.
    - Peer address configured incorrectly on either router.
    - AS number configured incorrectly on either router.
- **Connect State**:
  - Waits for successful TCP negotiation with peer.
  - BGP does not spend much time in this state if the TCP session has been successfully established.
  - Sends Open message to peer and changes state to OpenSent.
  - If an error occurs, BGP moves to the Active state. Some reasons for the error are:
    - TCP port 179 is not open.
    - A random TCP port over 1023 is not open.
    - Peer address configured incorrectly on either router.
    - AS number configured incorrectly on either router.
- **Active State**:
  - If the router was unable to establish a successful TCP session, then it ends up in the Active state.
  - BGP FSM tries to restart another TCP session with the peer and, if successful, then it sends an Open message to the peer.
  - If it is unsuccessful again, the FSM is reset to the Idle state.
  - Repeated failures may result in a router cycling between the Idle and Active states. Some of the reasons for this include:
    - TCP port 179 is not open.
    - A random TCP port over 1023 is not open.
    - BGP configuration error.
    - Network congestion.
    - Flapping network interface.
- **OpenSent State**:
  - BGP FSM listens for an Open message from its peer.
  - Once the message has been received, the router checks the validity of the Open message.
  - If there is an error, it is because one of the fields in the Open message does not match between the peers, e.g., BGP version mismatch, the peering router expects a different My AS, etc. The router then sends a Notification message to the peer indicating why the error occurred.
  - If there is no error, a Keepalive message is sent, various timers are set and the state is changed to OpenConfirm.
- **OpenConfirm State**:
  - The peer is listening for a Keepalive message from its peer.
  - If a Keepalive message is received and no timer has expired before reception of the Keepalive, BGP transitions to the Established state.
  - If a timer expires before a Keepalive message is received, or if an error condition occurs, the router transitions back to the Idle state.
- **Established State**:
  - In this state, the peers send Update messages to exchange information about each route being advertised to the BGP peer.
  - If there is any error in the Update message then a Notification message is sent to the peer, and BGP transitions back to the Idle state.

### Router connectivity and learning routes

In the simplest arrangement, all routers within a single AS and participating in BGP routing must be configured in a full mesh: each router must be configured as a peer to every other router. This causes scaling problems, since the number of required connections grows quadratically with the number of routers involved. To alleviate the problem, BGP implements two options: route reflectors (RFC 4456) and BGP confederations (RFC 5065). The following discussion of basic update processing assumes a full iBGP mesh.

A given BGP router may accept network-layer reachability information (NLRI) updates from multiple neighbors and advertise NLRI to the same, or a different set, of neighbors. The BGP process maintains several routing information bases:

- `RIB`: routers main routing information base table.
- `Loc-RIB`: local routing information base BGP maintains its own master routing table separate from the main routing table of the router.
- `Adj-RIB-In`: For each neighbor, the BGP process maintains a conceptual *adjacent routing information base, incoming*, containing the NLRI received from the neighbor.
- `Adj-RIB-Out`: For each neighbor, the BGP process maintains a conceptual *adjacent routing information base, outgoing*, containing the NLRI sent to the neighbor.

The physical storage and structure of these conceptual tables are decided by the implementer of the BGP code. Their structure is not visible to other BGP routers, although they usually can be interrogated with management commands on the local router. It is quite common, for example, to store the `Adj-RIB-In`, `Adj-RIB-Out` and the `Loc-RIB` together in the same data structure, with additional information attached to the RIB entries. The additional information tells the BGP process such things as whether individual entries belong in the `Adj-RIBs` for specific neighbors, whether the peer-neighbor route selection process made received policies eligible for the `Loc-RIB`, and whether `Loc-RIB` entries are eligible to be submitted to the local router's routing table management process.

BGP submits the routes that it considers best to the main routing table process. Depending on the implementation of that process, the BGP route is not necessarily selected. For example, a directly connected prefix, learned from the router's own hardware, is usually most preferred. As long as that directly connected route's interface is active, the BGP route to the destination will not be put into the routing table. Once the interface goes down and there are no more preferred routes, the Loc-RIB route would be installed in the main routing table.

BGP carries the information with which rules inside BGP-speaking routers can make policy decisions. Some of the information carried that is explicitly intended to be used in policy decisions are:

- Communities
- multi-exit discriminators (MED).
- autonomous systems (AS)

### Route selection process

The BGP standard specifies a number of decision factors, more than the ones that are used by any other common routing process, for selecting NLRI to go into the Loc-RIB. The first decision point for evaluating NLRI is that its next-hop attribute must be reachable (or resolvable). Another way of saying the next-hop must be reachable is that there must be an active route, already in the main routing table of the router, to the prefix in which the next-hop address is reachable.

Next, for each neighbor, the BGP process applies various standard and implementation-dependent criteria to decide which routes conceptually should go into the Adj-RIB-In. The neighbor could send several possible routes to a destination, but the first level of preference is at the neighbor level. Only one route to each destination will be installed in the conceptual Adj-RIB-In. This process will also delete, from the Adj-RIB-In, any routes that are withdrawn by the neighbor.

Whenever a conceptual Adj-RIB-In changes, the main BGP process decides if any of the neighbor's new routes are preferred to routes already in the Loc-RIB. If so, it replaces them. If a given route is withdrawn by a neighbor, and there is no other route to that destination, the route is removed from the Loc-RIB and no longer sent by BGP to the main routing table manager. If the router does not have a route to that destination from any non-BGP source, the withdrawn route will be removed from the main routing table.

As long as there is a tie, the route selection process moves to the next step.

| Step | Scope | Name | Default | Preferred | BGP field | Notes |
|---|---|---|---|---|---|---|
| 1 | Local to router | local Weight | "Off" | Higher |   | Cisco-specific parameter |
| 2 | Internal to AS | Local preference | "Off", all set to 100. | Higher | LOCAL_PREF | If there are several iBGP routes from the neighbor, the one with the highest local preference is selected unless there are several routes with the same local preference. |
| 3 | Accumulated Interior Gateway Protocol (AIGP) | "Off" | Lowest | AIGP | RFC 7311 |   |
| 4 | External to AS | Autonomous system (AS) jumps | "On", skipped if ignored in configuration | Lowest | AS-path | AS jumps is the number of AS numbers that must be traversed to reach the advertised destination. AS1–AS2–AS3 is a shorter path with fewer jumps than AS4–AS5–AS6–AS7. |
| 5 | origin type | "IGP" | Lowest | ORIGIN | 0 = IGP 1 = EGP 2 = Incomplete |   |
| 6 | multi-exit discriminator (MED) | "on", imported from peer AS | Lowest | MULTI_EXIT_DISC | By default only routes with the same peer autonomous system (AS) are compared. Can be set to ignore this. By default, IGP metric is not added. Can be set to add IGP metric. Before the most recent edition of the BGP standard, if an update had no MED value, several implementations created a MED with the highest possible value. The current standard specifies that missing MEDs are treated as the lowest possible value. Since the current rule may cause different behavior than the vendor interpretations, BGP implementations that used the nonstandard default value have a configuration feature that allows the old or standard rule to be selected. |   |
| 7 | Local to router (Loc-RIB) | eBGP over iBGP paths | "on" |   |   | Directly connected, over indirectly |
| 8 | IGP metric to BGP next hop | "on", imported from IGP | Lowest |   | Prefer the route with the lowest interior cost to the next hop, according to the main routing table. If two neighbors advertised the same route, but one neighbor is reachable via a low-bitrate link and the other by a high-bitrate link, and the interior routing protocol calculates lowest cost based on highest bitrate, the route through the high-bitrate link would be preferred and other routes dropped. If a BGP extension is used to support multipath routing, the best path selection may stop here and all paths selected up to this point will be added to the routing table. |   |
| 9 | Path that was received first | "on" | oldest |   | Used to ignore changes on the next steps to minimize route flapping. |   |
| 10 | Neighbor Router ID | "on" | Lowest |   |   |   |
| 11 | Cluster list length | "on" | Lowest |   |   |   |
| 12 | Neighbor IP address | "on" | Lowest |   |   |   |

The local preference, weight, and other criteria can be manipulated by local configuration and software capabilities. Such manipulation, although commonly used, is outside the scope of the standard. For example, the *community* attribute (see below) is not directly used by the BGP selection process. The BGP neighbor process can have a rule to set local preference or another factor based on a manually programmed rule to set the attribute if the community value matches some pattern-matching criterion. If the route was learned from an external peer the per-neighbor BGP process computes a local preference value from local policy rules and then compares the local preference of all routes from the neighbor.

### Communities

BGP communities are attribute tags that can be applied to incoming or outgoing prefixes to achieve some common goal. While it is common to say that BGP allows an administrator to set policies on how prefixes are handled by ISPs, this is generally not possible, strictly speaking. For instance, BGP natively has no concept to allow one AS to tell another AS to restrict advertisement of a prefix to only North American peering customers. Instead, an ISP generally publishes a list of well-known or proprietary communities with a description for each one, which essentially becomes an agreement of how prefixes are to be treated.

| Attribute value | Attribute | Description | Reference |
|---|---|---|---|
| 0x00000000–0x0000FFFF | Reserved |   | RFC 1997 |
| 0x00010000–0xFFFEFFFF | Reserved for private use |   | RFC 1997 |
| 0xFFFF0000 | GRACEFUL_SHUTDOWN | At neighbor AS-peer, set LOCAL_PREF, lower to route away from source. | RFC 8326 |
| 0xFFFF0001 | ACCEPT_OWN | Used to modify how a route originated within one VRF is imported into other VRFs | RFC 7611 |
| 0xFFFF0002 | ROUTE_FILTER_TRANSLATED_v4 |   | RFC draft-l3vpn-legacy-rtc |
| 0xFFFF0003 | ROUTE_FILTER_v4 |   | RFC draft-l3vpn-legacy-rtc |
| 0xFFFF0004 | ROUTE_FILTER_TRANSLATED_v6 |   | RFC draft-l3vpn-legacy-rtc |
| 0xFFFF0005 | ROUTE_FILTER_v6 |   | RFC draft-l3vpn-legacy-rtc |
| 0xFFFF0006 | LLGR_STALE | Stale routes are retained for longer after a session failure | RFC 9494 |
| 0xFFFF0007 | NO_LLGR | LLGR capability should not apply | RFC 9494 |
| 0xFFFF0008 | accept-own-nexthop |   | RFC draft-agrewal-idr-accept-own-nexthop |
| 0xFFFF0009 | Standby PE | Allow for faster recovery of connectivity on different types of failures, with multicast in BGP/MPLS VPNs. | RFC 9026 |
| 0xFFFF029A | BLACKHOLE | To temporarily protect against denial-of-service attack by asking the neighbour AS to discard all traffic to the prefix (blackholing) | RFC 7999 |
| 0xFFFFFF01 | NO_EXPORT | Limit to a BGP confederation boundary | RFC 1997 |
| 0xFFFFFF02 | NO_ADVERTISE | Limit to a BGP peer | RFC 1997 |
| 0xFFFFFF03 | NO_EXPORT_SUBCONFED | Limit to an AS | RFC 1997 |
| 0xFFFFFF04 | NOPEER | "No need" to advertise over a peer link | RFC 3765 |

Examples of common communities include:

- local preference adjustments,
- geographic
- peer type restrictions
- denial-of-service attack identification
- AS prepending options.

An ISP might state that any routes received from customers with following examples:

- To Customers North America (East Coast) 3491:100
- To Customers North America (West Coast) 3491:200

The customer simply adjusts their configuration to include the correct community or communities for each route, and the ISP is responsible for controlling who the prefix is advertised to. The end user has no technical ability to enforce correct actions being taken by the ISP, though problems in this area are generally rare and accidental.

It is a common tactic for end customers to use BGP communities (usually ASN:70,80,90,100) to control the local preference the ISP assigns to advertised routes instead of using MED (the effect is similar). The community attribute is transitive, but communities applied by the customer very rarely propagate outside the next-hop AS. Not all ISPs give out their communities to the public.

#### BGP Extended Community Attribute

The BGP Extended Community Attribute was added in 2006, in order to extend the range of such attributes and to provide a community attribute structuring by means of a type field. The extended format consists of one or two octets for the type field, followed by seven or six octets for the respective community attribute content. The IANA administers the registry for BGP Extended Communities Types.

The Extended Communities Attribute itself is a transitive optional BGP attribute. A bit in the *Type* field within the attribute decides whether the encoded extended community is of a transitive or non-transitive nature. The IANA registry therefore provides different number ranges for the attribute types. Due to the extended attribute range, its usage can be manifold. RFC 4360 exemplarily defines the "Two-Octet AS Specific Extended Community", the "IPv4 Address Specific Extended Community", the "Opaque Extended Community", the "Route Target Community", and the "Route Origin Community". A number of BGP QoS drafts also use this Extended Community Attribute structure for inter-domain QoS signalling.

With the introduction of 32-bit AS numbers, some issues were immediately obvious with the community attribute that only defines a 16-bit ASN field, which prevents the matching between this field and the real ASN value. Since 2014, extended communities are compatible with 32-bit ASNs. To accommodate 32-bit AS numbers in BGP Communities, a Large Community attribute of 12 bytes was defined, divided in three field of 4 bytes each (AS:function:parameter).

### Multi-exit discriminators

MEDs, defined in the main BGP standard, were originally intended to show to another neighbor AS the advertising AS's preference as to which of several links are preferred for inbound traffic. Another application of MEDs is to advertise the value, typically based on delay, of multiple ASs that have a presence at an IXP, that they impose to send traffic to some destination.

Some routers (like Juniper) will use the Metric from OSPF to set MED.

**Examples of MED used with BGP when exported to BGP on Juniper SRX**

```mw
# run show ospf route   
Topology default Route Table:
Prefix             Path  Route      NH       Metric NextHop       Nexthop     
                   Type  Type       Type            Interface     Address/LSP
10.32.37.0/24      Inter Discard    IP       16777215
10.32.37.0/26      Intra Network    IP          101 ge-0/0/1.0    10.32.37.241
10.32.37.64/26     Intra Network    IP          102 ge-0/0/1.0    10.32.37.241
10.32.37.128/26    Intra Network    IP          101 ge-0/0/1.0    10.32.37.241

# show route advertising-protocol bgp 10.32.94.169
  Prefix               Nexthop       MED    Lclpref            AS path
* 10.32.37.0/24           Self                 16777215           I
* 10.32.37.0/26           Self                 101                I
* 10.32.37.64/26          Self                 102                I
* 10.32.37.128/26         Self                 101                I
```


## Packet format

### Message header format

All BGP messages share the following header layout.

BGP version 4 message header format

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

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

4

32

8

64

12

96

16

128

Length

Type

**Marker: 128 bits**

Included for compatibility, MUST be set to all ones.

**Length: 16 bits**

Total length of the message in octets, including the header.

**Type: 8 bits**

Type of BGP message. The following values are defined:

- Open (1)
- Update (2)
- Notification (3)
- KeepAlive (4)
- Route-Refresh (5)

### Open Packet

With an *Open* packet, a BGP session may be initiated.

BGP version 4 'OPEN' message format

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

⋮

⋮

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

16

128

Length

(29+)

Type

(1)

Version

(4)

20

160

My AS

Hold Time

24

192

BGP Identifier

28

224

Parameters Length

30

240

Parameters

34

272

⋮

⋮

**Version: 8 bits**

Version of BGP used.

**My AS: 16 bits**

Senders

autonomous system

number.

**Hold Time: 16 bits**

Timeout timer, used to calculate KeepAlive messages. Default 90 seconds.

**BGP Identifier: 32 bits**

Holds the IP address of the sender.

**Parameters Length: 8 bits**

Total length of the Parameters field in octets. If this (mandatory)

field is zero, there are no parameters in the message.

**Parameters: variable**

Optional parameters. This field is used to convey the capabilities the sender of this packet has to the peer.

A

list

of all capabilities is maintained by

IANA

.

**Example of Open Message**

```
Type: Open Message (1)
Version: 4
My AS: 64496
Hold Time: 90
BGP Identifier: 192.0.2.254
Optional Parameters Length: 16
Optional Parameters:
 Capability: Multiprotocol Extensions Capability (1)
 Capability: Route Refresh Capability (2)
 Capability: Enhanced Route Refresh Capability (70)
```

### Update Packet

Only changes are sent. After the initial exchange, only differences (add/change/remove) are sent.

BGP version 4 'UPDATE' message format

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

⋮

⋮

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

16

128

Length

(23+)

Type

(2)

Withdrawn Routes Length

↴

20

160

↪

Length (cont.)

⋮

⋮

Withdrawn Routes

⋮

⋮

Total Path Attribute Length

⋮

⋮

Path Attributes

⋮

⋮

Network Layer Reachability Information

⋮

⋮

**Withdrawn Routes Length: 16 bits**

Length of the following withdrawn routes. May be zero if no routes are withdrawn.

**Withdrawn Routes: variable**

A list of withdrawn routes, specified as a series of <length, prefix>

tuples

.

**Total Path Attribute Length: 16 bits**

Length of the following path attributes. May be zero if there are no attributes.

**Path Attributes: variable**

List of path attributes, specified as a series of

TLV

structures.

**Network Layer Reachability Information (NLRI): variable**

Reachability information, specified as a series of <length, prefix> tuples. The length of this field can be caclulated as:

Length

- 23 -

Withdrawn Routes Length

-

Total Path Attribute Length

.

**Example of UPDATE Message**

```
Type: UPDATE Message (2)
Withdrawn Routes Length: 0
Total Path Attribute Length: 25
Path attributes
 ORIGIN: IGP
 AS_PATH: 64500
 NEXT_HOP: 192.0.2.254
 MULTI_EXIT_DISC: 0
Network Layer Reachability Information (NLRI)
 192.0.2.0/27
 192.0.2.32/27
 192.0.2.64/27
```

### Notification

If there is an error, it is because one of the fields in the OPEN or UPDATE message does not match between the peers. For example: BGP version mismatch, or the peering router expects a different 'My AS'. The router then sends a Notification message to the peer indicating why the error occurred. An error in the communication usually leads to the teardown of the BGP session. To avoid a cascade of sessions being terminated due to a single error, which can happen in complex scenarios with routers with limited capabilities, extra effort is taken to isolate the problem and keep most sessions going.

BGP version 4 'NOTIFICATION' message format

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

⋮

⋮

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

16

128

Length

(21+)

Type

(3)

Error Code

20

160

Error Subcode

24

192

Data

28

224

⋮

⋮

**Error Code: 8 bits**

A value indicating the type or origin of the error.

**Error Subcode: 8 bits**

A value specifying which error occurred.

| Error Code | Name | subcodes |   |
|---|---|---|---|
| Code | Name |   |   |
| 1 | Message Header Error | 1 | Connection Not Synchronized |
| 2 | Bad Message Length |   |   |
| 3 | Bad Message Type |   |   |
| 2 | OPEN Message Error | 1 | Unsupported Version Number. |
| 2 | Bad Peer AS. |   |   |
| 3 | Bad BGP Identifier. |   |   |
| 4 | Unsupported Authentication Code. |   |   |
| 5 | Authentication Failure. |   |   |
| 6 | Unacceptable Hold Time. |   |   |
| 3 | UPDATE Message Error | 1 | Malformed Attribute List. |
| 2 | Unrecognized Well-known Attribute. |   |   |
| 3 | Missing Well-known Attribute. |   |   |
| 4 | Attribute Flags Error. |   |   |
| 5 | Attribute Length Error. |   |   |
| 6 | Invalid ORIGIN Attribute |   |   |
| 7 | AS Routing Loop. |   |   |
| 8 | Invalid NEXT_HOP Attribute. |   |   |
| 9 | Optional Attribute Error. |   |   |
| 10 | Invalid Network Field. |   |   |
| 11 | Malformed AS_PATH. |   |   |
| 4 | Hold Timer Expired |   |   |
| 5 | Finite State Machine Error |   |   |
| 6 | Cease |   |   |

**Data: variable**

Optional data to help diagnose the problem.

**Example of NOTIFICATION Message**

```
Type: NOTIFICATION Message (3)
Major error Code: OPEN Message Error (2)
Minor error Code (Open Message): Bad Peer AS (2)
Bad Peer AS: 65200
```

### KeepAlive

KeepAlive messages are sent periodically, by both peers of a session, to verify that the remote peer is still alive. They should be sent at intervals of one third the `holdtime`.

BGP version 4 'KEEPALIVE' message format

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

⋮

⋮

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

16

128

Length

(19)

Type

(4)

A keep-alive packet has no data content.

### Route-Refresh

An addition to the initial BGP message types is route-refresh, which allows for soft updating of `Adj-RIB-in`, without resetting the connection.

Before making use of this feature, the capability 'Route Refresh Capability (2)' should be specified in the 'Open' message. Fine-grained routing updates may be acquired when the capability 'Enhanced Route Refresh Capability (70)' is also given.

BGP version 4 'ROUTE-REFRESH' message format

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

⋮

⋮

Marker

(ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff)

16

128

Length

(23+)

Type

(5)

Address Family Identifier

↴

20

160

↪

AFI (cont.)

Message Subtype

SAFI

⋮

⋮

Network Layer Reachability Information

⋮

⋮

⋮

⋮

**Address Family Identifier (AFI): 16 bits**

An identifier for the

address family

(

IPv4

,

IPv6

,

IPX

,

AppleTalk

, etc.) This list is maintained by

IANA

.

**Message Subtype: 8 bits**

This field indicates what kind of route-refresh message this is.

**Subsequent Address Family Identifier: 8 bit**

This field provides additional information about the type of the Network Layer Reachability Information (NLRI) carried in the attribute. Values: 1 (unicast); 2 (multicast); 3 (both).

**Network Layer Reachability Information (NLRI): variable**

Reachability information, specified as a series of <length, prefix> tuples.

**Example of ROUTE-REFRESH Message**

```
Type: ROUTE-REFRESH Message (5)
Address family identifier (AFI): IPv4 (1)
Subtype: Normal route refresh request (0)
Subsequent address family identifier (SAFI): Unicast (1)
```


## Internal scalability

BGP is "the most scalable of all routing protocols."

An autonomous system with internal BGP (iBGP) must have all of its iBGP peers connect to each other in a full mesh (where everyone speaks to everyone directly). This full-mesh configuration requires that each router maintain a session with every other router. In large networks, this number of sessions may degrade the performance of routers, due to either a lack of memory or high CPU process requirements.

### Route reflectors

**Route reflectors** (RRs) reduce the number of connections required in an AS. A single router (or two for redundancy) can be made an RR: other routers in the AS need only be configured as peers to them. An RR offers an alternative to the logical full-mesh requirement of iBGP. The purpose of the RR is concentration. Multiple BGP routers can peer with a central point, the RR – acting as an RR server – rather than peer with every other router in a full mesh. All the other iBGP routers become RR clients.

This approach, similar to OSPF's DR/BDR feature, provides large networks with added iBGP scalability. In a fully meshed iBGP network of 10 routers, 90 individual CLI statements (spread throughout all routers in the topology) are needed just to define the remote-AS of each peer: this quickly becomes a headache to manage. An RR topology can cut these 90 statements down to 18, offering a viable solution for the larger networks administered by ISPs.

An RR is a single point of failure, therefore at least a second RR may be configured in order to provide redundancy. As it is an additional peer for the other 10 routers, it approximately doubles the number of CLI statements, requiring an additional 11 × 2 − 2 = 20 statements in this case. In a BGP multipath environment, the additional RR can also benefit the network by adding local routing throughput if the RRs are acting as traditional routers instead of just a dedicated RR server role.

RRs and confederations both reduce the number of iBGP peers to each router and thus reduce processing overhead. RRs are a pure performance-enhancing technique, while confederations can also be used to implement more fine-grained policy.

#### Rules

RR servers propagate routes inside the AS based on the following rules:

- Routes are always reflected to eBGP peers.
- Routes are never reflected to the originator of the route.
- If a route is received from a non-client peer, reflect to client peers.
- If a route is received from a client peer, reflect to client and non-client peers.

#### Cluster

An RR and its clients form a *cluster*. The *cluster ID* is then attached to every route advertised by the RR to its client or non-client peers. A cluster ID is a cumulative, non-transitive BGP attribute, and every RR must prepend the local cluster ID to the cluster list to avoid routing loops.

### Confederation

Confederations are sets of autonomous systems. In common practice, only one of the confederation AS numbers is seen by the Internet as a whole. Confederations are used in very large networks where a large AS can be configured to encompass smaller, more manageable internal ASs.

The confederated AS is composed of multiple ASs. Each confederated AS alone has iBGP fully meshed and has connections to other ASs inside the confederation. Even though these ASs have eBGP peers to ASs within the confederation, the ASs exchange routing as if they used iBGP. In this way, the confederation preserves next hop, metric, and local preference information. To the outside world, the confederation appears to be a single AS. With this solution, iBGP transit AS problems can be resolved as iBGP requires a full mesh between all BGP routers: a large number of TCP sessions and unnecessary duplication of routing traffic.

Confederations can be used in conjunction with route reflectors. Both confederations and route reflectors can be subject to persistent oscillation unless specific design rules, affecting both BGP and the interior routing protocol, are followed.

These alternatives can introduce problems of their own, including the following:

- route oscillation
- sub-optimal routing
- increase of BGP convergence time

Additionally, route reflectors and BGP confederations were not designed to ease BGP router configuration. Nevertheless, these are common tools for experienced BGP network architects. These tools may be combined, for example, as a hierarchy of route reflectors.


## Stability

The routing tables managed by a BGP implementation are adjusted continually to reflect actual changes in the network, such as links or routers going down and coming back up. In the network as a whole, it is normal for these changes to happen almost continuously, but for any particular router or link, changes are expected to be relatively infrequent. If a router is misconfigured or mismanaged, then it may get into a rapid cycle between down and up states. This pattern of repeated withdrawal and re-announcement, known as route flapping can cause excessive activity in all the other routers that know about the cycling entity, as the same route is continually injected and withdrawn from the routing tables. The BGP design is such that delivery of traffic may not function while routes are being updated. On the Internet, a BGP routing change may cause outages for several minutes.

A feature known as *route flap damping* is built into many BGP implementations, in an attempt to mitigate the effects of route flapping. Without damping, the excessive activity can cause a heavy processing load on routers, which may in turn delay updates on other routes, and so affect overall routing stability. With damping, a route's flapping is exponentially decayed. At the first instance, when a route becomes unavailable and quickly reappears, damping does not take effect, so as to maintain the normal fail-over times of BGP. At the second occurrence, BGP shuns that prefix for a certain length of time; subsequent occurrences are ignored exponentially longer. After the abnormalities have ceased and a suitable length of time has passed for the offending route, prefixes can be reinstated with a clean slate. Damping can also mitigate denial-of-service attacks.

It is also suggested that route flap damping is a feature more desirable if implemented to Exterior Border Gateway Protocol Sessions (eBGP sessions or simply called exterior peers) and not on Interior Border Gateway Protocol Sessions (iBGP sessions or simply called internal peers). With this approach when a route flaps inside an autonomous system, it is not propagated to the external ASs – flapping a route to an eBGP will cause a chain of flapping for the particular route throughout the backbone. This method also successfully avoids the overhead of route flap damping for iBGP sessions.

Subsequent research has shown that flap damping can actually lengthen convergence times in some cases, and can cause interruptions in connectivity even when links are not flapping. Moreover, as backbone links and router processors have become faster, some network architects have suggested that flap damping may not be as important as it used to be, since changes to the routing table can be handled much faster by routers. This has led the RIPE Routing Working Group to write, "With the current implementations of BGP flap damping, the application of flap damping in ISP networks is NOT recommended. ... If flap damping is implemented, the ISP operating that network will cause side-effects to their customers and the Internet users of their customers' content and services ... . These side-effects would quite likely be worse than the impact caused by simply not running flap damping at all."


## Routing table growth

One of the largest problems faced by BGP, and indeed the Internet infrastructure as a whole, is the growth of the Internet routing table. If the global routing table grows to the point where some older, less capable routers cannot cope with the memory requirements or the CPU load of maintaining the table, these routers will cease to be effective gateways between the parts of the Internet they connect. In addition, and perhaps even more importantly, larger routing tables take longer to stabilize after a major connectivity change, leaving network service unreliable, or even unavailable, in the interim.

Until late 2001, the global routing table was growing exponentially, threatening an eventual widespread breakdown of connectivity. In an attempt to prevent this, ISPs cooperated in keeping the global routing table as small as possible by using Classless Inter-Domain Routing (CIDR) and route aggregation. While this slowed the growth of the routing table to a linear process for several years, with the expanded demand for multihoming by end-user networks, the growth was once again superlinear by the middle of 2004.

### 512k day

A Y2K-like overflow triggered in 2014 for those models that were not appropriately updated.

While a full IPv4 BGP table as of August 2014 (512k day) was in excess of 512,000 prefixes, many older routers had a limit of 512k (512,000–524,288) routing table entries. On August 12, 2014, outages resulting from full tables hit eBay, LastPass and Microsoft Azure, among others. A number of Cisco routers commonly in use had TCAM, a form of high-speed content-addressable memory, for storing BGP advertised routes. On impacted routers, the TCAM was by default allocated as 512k IPv4 routes and 256k IPv6 routes. While the reported number of IPv6 advertised routes was only about 20k, the number of advertised IPv4 routes reached the default limit, causing a spillover effect as routers attempted to compensate for the issue by using slow software routing (as opposed to fast hardware routing via TCAM). The main method for dealing with this issue involves operators changing the TCAM allocation to allow more IPv4 entries by reallocating some of the TCAM reserved for IPv6 routes, which requires a reboot on most routers. The 512k problem was predicted by a number of IT professionals.

The actual allocations, which pushed the number of routes above 512k, were the announcement of about 15,000 new routes in short order, starting at 07:48 UTC. Almost all of these routes were to Verizon Autonomous Systems 701 and 705, created as a result of the deaggregation of larger blocks, introducing thousands of new */24* routes, and making the routing table reach 515,000 entries. The new routes appear to have been reaggregated within 5 minutes, but instability across the Internet apparently continued for a number of hours. Even if Verizon had not caused the routing table to exceed 512k entries in the short spike, it would have soon happened through natural growth.

Route summarization is often used to improve aggregation of the BGP global routing table, thereby reducing the necessary table size in routers of an AS. Consider AS1 has been allocated the big address space of *172.16.0.0/16*, this would be counted as one route in the table, but due to customer requirements or traffic engineering purposes, AS1 wants to announce smaller, more specific routes of *172.16.0.0/18*, *172.16.64.0/18*, and *172.16.128.0/18*. The prefix *172.16.192.0/18* does not have any hosts so AS1 does not announce a specific route *172.16.192.0/18*. This all counts as AS1 announcing four routes.

AS2 will see the four routes from AS1 (*172.16.0.0/16*, *172.16.0.0/18*, *172.16.64.0/18*, and *172.16.128.0/18*) and it is up to the routing policy of AS2 to decide whether or not to take a copy of the four routes or, as *172.16.0.0/16* overlaps all the other specific routes, to just store the summary, *172.16.0.0/16*.

If AS2 wants to send data to prefix *172.16.192.0/18*, it will be sent to the routers of AS1 on route *172.16.0.0/16*. At AS1, it will either be dropped or a destination unreachable ICMP message will be sent back, depending on the configuration of AS1's routers.

If AS1 later decides to drop the route *172.16.0.0/16*, leaving *172.16.0.0/18*, *172.16.64.0/18*, and *172.16.128.0/18*, the number of routes AS1 announces drops to three. Depending on the routing policy of AS2, it will store a copy of the three routes, or aggregate *172.16.0.0/18* and *172.16.64.0/18* to *172.16.0.0/17*, thereby reducing the number of routes AS2 stores to two (*172.16.0.0/17* and *172.16.128.0/18*).

If AS2 now wants to send data to prefix *172.16.192.0/18*, it will be dropped or a destination unreachable ICMP message will be sent back at the routers of AS2 (not AS1 as before), because *172.16.192.0/18* is not in the routing table.

### AS number depletion and 32-bit ASNs

In 1995, the first BGP-4 specification coded AS numbers on 16 bits, for 64,510 possible public AS numbers. In 2011, only 15,000 AS numbers were still available, and projections were envisioning a complete depletion of available AS numbers in September 2013.

In 2007 already, the AS coding was extended from 16 to 32 bits, while retaining the 16-bit AS range (0 to 65535) and its reserved AS numbers. This now allows up to 4 billion available AS numbers. An additional private AS range is also defined. To allow the traversal of router groups not able to manage those new ASNs, the new attribute **AS4_PATH** (optional transitive) and the special 16-bit ASN **AS_TRANS** (AS23456) is used. 32-bit ASN assignments started in 2007.

### Load balancing

Another factor contributing to the growth of the routing table is the need for load balancing of multi-homed networks. It is not a trivial task to balance the inbound traffic to a multi-homed network across its multiple inbound paths, due to limitations of the BGP route selection process. For a multi-homed network, if it announces the same network blocks across all of its BGP peers, the result may be that one or several of its inbound links become congested while the other links remain under-utilized, because external networks all picked that set of congested paths as optimal. Like most other routing protocols, BGP does not detect congestion.

To work around this problem, BGP administrators of that multihomed network may divide a large contiguous IP address block into smaller blocks and tweak the route announcement to make different blocks look optimal on different paths, so that external networks will choose a different path to reach different blocks of that multihomed network. Such cases will increase the number of routes as seen on the global BGP table.

One method to address the routing table issue associated with load balancing is to deploy Locator/Identifier Separation Protocol (BGP/LISP) gateways within an Internet exchange point to allow ingress traffic engineering across multiple links. This technique does not increase the number of routes seen on the global BGP table.


## Security

By design, routers running BGP accept advertised routes from other BGP routers by default. This allows for automatic and decentralized routing of traffic across the Internet, but it also leaves the Internet potentially vulnerable to accidental or malicious disruption, known as BGP hijacking. Due to the extent to which BGP is embedded in the core systems of the Internet, and the number of different networks operated by many different organizations that collectively make up the Internet, correcting this vulnerability (such as by introducing the use of cryptographic keys to verify the identity of BGP routers) is a technically and economically challenging problem.

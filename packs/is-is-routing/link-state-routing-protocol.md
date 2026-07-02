---
title: "Link-state routing protocol"
source: https://en.wikipedia.org/wiki/Link-state_routing_protocol
domain: is-is-routing
license: CC-BY-SA-4.0
tags: is-is protocol, link-state routing, interior gateway protocol, network convergence
fetched: 2026-07-02
---

# Link-state routing protocol

**Link-state routing protocols** are one of the two main classes of routing protocols used in packet switching networks for computer communications, the others being distance-vector routing protocols. Examples of link-state routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).

The link-state protocol is performed by every *switching node* in the network (i.e., nodes which are prepared to forward packets; in the Internet, these are called routers). The basic concept of link-state routing is that every node constructs a *map* of the connectivity to the network in the form of a graph, showing which nodes are connected to which other nodes. Each node then independently calculates the next best logical *path* from it to every possible destination in the network. Each collection of best paths will then form each node's routing table.

This contrasts with distance-vector routing protocols, which work by having each node share its routing table with its neighbors. In a link-state protocol, the only information passed between nodes is *connectivity related*. Link-state algorithms are sometimes characterized informally as each router "telling the world about its neighbors."

## Overview

In link-state routing protocols, each router possesses information about the complete network topology. Each router then independently calculates the best next hop from it for every possible destination in the network using local information of the topology. The collection of best next hops forms the routing table.

This contrasts with distance-vector routing protocols, which work by having each node share its routing table with its neighbours. In a link-state protocol, the only information passed between the nodes is the information used to construct the connectivity maps.

## History

What is believed to be the first adaptive routing network of computers, using link-state routing, was designed and implemented during 1976–1977 by a team from Plessey Radar led by Bernard J Harris; the project was for "Wavell" – a system of computer command and control for the British Army. The first link-state routing concept was published in 1979 by John M. McQuillan (then at Bolt, Beranek and Newman) as a mechanism that would calculate routes more quickly when network conditions changed and thus lead to more stable routing.

The technique was later adapted for use in the contemporary link-state routing protocols IS-IS and OSPF. Cisco literature refers to Enhanced Interior Gateway Routing Protocol (EIGRP) as a "hybrid" protocol, despite the fact it distributes routing tables instead of topology maps. However, it does synchronize routing tables at start-up as OSPF does and sends specific updates only when topology changes occur.

In 2004, Radia Perlman proposed using link-state routing for layer 2 frame forwarding with devices called routing bridges, or Rbridges. The Internet Engineering Task Force has standardized the Transparent Interconnection of Lots of Links (TRILL) protocol to accomplish this.

More recently, this hierarchical technique was applied to wireless mesh networks using the Optimized Link State Routing Protocol (OLSR). Where a connection can have varying quality, the quality of a connection can be used to select better connections. This is used in some ad hoc routing protocols that use radio frequency transmission.

## Distributing maps

The first main stage in the link-state algorithm is to give a map of the network to every node. This is done with several subsidiary steps. First, each node needs to determine what other ports it is connected to over fully working links; it does this using *reachability protocol* that it runs periodically and separately with each of its directly connected neighbours.

Each node periodically (and in case of connectivity changes) sends a short message, the link-state advertisement, which:

- Identifies the node that is producing it.
- Identifies all the other nodes (either routers or networks) to which it is directly connected.
- Includes a 'sequence number', which increases every time the source node makes up a new version of the message*.*

This message is sent to all the nodes on a network. As a necessary precursor, each node in the network remembers, for every one of *its* neighbors, the sequence number of the last link-state message which it received from that node. When a link-state advertisement is received at a node, the node looks up the sequence number it has stored for the source of that link-state message; if this message is newer (i.e., has a higher sequence number), it is saved, the sequence number is updated, and a copy is sent in turn to each of that node's neighbors. This procedure rapidly gets a copy of the latest version of each node's link-state advertisement to every node in the network.

The complete set produces the graph for the map of the network. The link-state message giving information about the neighbors is recomputed and then flooded throughout the network whenever there is a change in the connectivity between the node and its neighbors, e.g., when a link fails.

## Calculating the routing table

The second main stage in the link-state algorithm is to produce routing tables by inspecting the maps. Each node independently runs an algorithm over the map to determine the shortest path from itself to every other node in the network; generally, some variant of Dijkstra's algorithm is used. A node maintains two data structures: a Tree data structure tree containing nodes which are "done", and a list of *candidates*. The algorithm starts with both structures empty; it then adds to the first one the node itself. The variant of a greedy algorithm then repetitively does the following:

- All neighbour nodes which are directly connected to the node are just added to the tree (excepting any nodes which are already in either the tree or the *candidate* list). The rest are added to the second (*candidate*) list.
- Each node in the *candidate* list is compared to each of the nodes already in the tree. The candidate node which is closest to any of the nodes already in the tree is itself moved into the tree and attached to the appropriate neighbor node. When a node is moved from the candidate list into the tree, it is removed from the candidate list and is not considered in subsequent iterations of the algorithm.

The two steps are repeated as long as there are any nodes left in the candidate list. (When there are none, all the nodes in the network will have been added to the tree.) This procedure ends with the tree containing all the nodes in the network. For any given destination node, the best path for that destination is the node which is the first step from the root node, down the branch in the shortest-path tree which leads toward the desired destination node.

## Algorithm optimizations

Whenever a change in the connectivity map happens, it is necessary to recompute the shortest-path tree and then recreate the routing table. BBN Technologies discovered how to compute only that part of the tree which could have been affected by a given change in the map.

### Topology reduction

In some cases, it is reasonable to reduce the number of nodes that generate LSA messages. For this reason, a topology reduction strategy can be applied, in which only a subset of the network nodes generate LSA messages. Two widely studied approaches for topology reduction are multipoint relays that are at the base of the Optimized Link State Routing Protocol (OLSR) but have also been proposed for OSPF and connected dominating sets that were again proposed for OSPF.

### Fisheye State Routing

With Fisheye State Routing (FSR), the LSA are sent with different time-to-live values to restrict their diffusion and limit the overhead due to control messages. The same concept is used also in the Hazy Sighted Link State Routing Protocol.

## Failure modes

If all the nodes are not working from exactly the same map, *routing loops* can form. These are situations in which, in the simplest form, two neighboring nodes each think the other is the best path to a given destination. Any packet headed to that destination arriving at either node will loop between the two, hence the name. Routing loops involving more than two nodes are also possible.

This can occur since each node computes its shortest-path tree and its routing table without interacting in any way with any other nodes. If two nodes start with different maps, it is possible to have scenarios in which routing loops are created. In certain circumstances, differential loops may be enabled within a multi-cloud environment. Variable access nodes across the interface protocol may also bypass the simultaneous access node problem.

## Optimized Link State Routing Protocol

The Optimized Link State Routing Protocol (OLSR) is a link-state routing protocol optimized for mobile ad hoc networks (which can also be used on other wireless ad hoc networks). OLSR is proactive and uses hello and topology control messages to disseminate link-state information into the mobile ad hoc network. Using hello messages, each node discovers two-hop neighbor information and elects a set of *multipoint relays* (MPRs). MPRs make OLSR distinct from other link-state routing protocols. Individual nodes use the topology information to compute next-hop paths regarding all nodes in the network using shortest-hop forwarding paths.

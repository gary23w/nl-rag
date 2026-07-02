---
title: "Mesh networking"
source: https://en.wikipedia.org/wiki/Mesh_networking
domain: zigbee-deep
license: CC-BY-SA-4.0
tags: zigbee protocol, zigbee mesh, ieee 802.15.4 network, low-power mesh networking
fetched: 2026-07-02
---

# Mesh networking

Illustration of a

partially connected

mesh network

A

fully connected

mesh network, where each node is connected to every other node in the network

A **mesh network** is a network topology in which the infrastructure nodes (i.e., bridges, switches, and other infrastructure devices) connect directly, dynamically and non-hierarchically to as many other nodes as possible and cooperate with one another to efficiently route data to and from hosts.

This lack of dependency on one node allows for every node to participate in the relay of information. Mesh networks dynamically self-organize and self-configure, which can reduce installation overhead. The ability to self-configure enables dynamic distribution of workloads, particularly in the event that a few nodes should fail. This, in turn, contributes to fault-tolerance and reduced maintenance costs.

Mesh topology may be contrasted with conventional star/tree network topologies in which the bridges/switches are directly linked to only a small subset of other bridges/switches, and the links between these infrastructure neighbours are hierarchical. While star-and-tree topologies are very well established, highly standardized and vendor-neutral, vendors of mesh network devices have not yet all agreed on common standards, and interoperability between devices from different vendors is not yet assured.

## Basic principles

Mesh networks can relay messages using either a *flooding* or a *routing* technique, which makes them different from non-mesh networks. A routed message is propagated along a path by *hopping* from node to node until it reaches its destination. To ensure that all its paths are available, the network must allow for continuous connections and must reconfigure itself around broken paths, using *self-healing* algorithms such as Shortest Path Bridging and TRILL (Transparent Interconnection of Lots of Links). Self-healing allows a routing-based network to operate when a node breaks down or when a connection becomes unreliable. The network is typically quite reliable, as there is often more than one path between a source and a destination in the network. Although mostly used in wireless situations, this concept can also apply to wired networks and to software interaction.

A mesh network whose nodes are all connected to each other is a fully connected network. Fully connected wired networks are more secure and reliable: problems in a cable affect only the two nodes attached to it. In such networks, however, the number of cables, and therefore the cost, goes up rapidly as the number of nodes increases.

## Types

### Wired mesh

Shortest path bridging and TRILL each allow Ethernet switches to be connected in a mesh topology and allow for all paths to be active. IP routing supports multiple paths from source to destination.

### Wireless mesh

A wireless mesh network (WMN) is a network made up of radio nodes organized in a mesh topology. It can also be a form of wireless ad hoc network.

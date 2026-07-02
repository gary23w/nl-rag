---
title: "End-to-end principle"
source: https://en.wikipedia.org/wiki/End-to-end_principle
domain: cypress-e2e
license: CC-BY-SA-4.0
tags: cypress e2e, end-to-end browser testing, cypress test runner, in-browser assertion
fetched: 2026-07-02
---

# End-to-end principle

The **end-to-end** (**E2E**) **principle** is a design principle in computer networking that requires application-specific features (such as reliability and security) to be implemented in the communicating end nodes of the network, instead of in the network itself. Intermediary nodes (such as gateways and routers) that exist to establish the network may still implement these features to improve efficiency but do not guarantee end-to-end functionality.

The essence of what would later be called the end-to-end principle was contained in the work of Donald Davies on packet-switched networks in the 1960s. Louis Pouzin pioneered the use of the end-to-end strategy in the CYCLADES network in the 1970s. The principle was first articulated explicitly in 1981 by Saltzer, Reed, and Clark. The meaning of the end-to-end principle has been continuously reinterpreted ever since its initial articulation. Noteworthy formulations of the end-to-end principle can be found before the seminal 1981 Saltzer, Reed, and Clark paper.

A basic premise of the principle is that the payoffs from adding certain features required by the end application to the communication subsystem quickly diminish. The end hosts have to implement these functions for correctness. Implementing a specific function incurs some resource penalties regardless of whether the function is used or not, and implementing a specific function *in the network* adds these penalties to all clients, whether they need the function or not.

## Concept

The fundamental notion behind the end-to-end principle is that for two processes communicating with each other via some communication means, the *reliability* obtained from that means cannot be expected to be perfectly aligned with the reliability requirements of the processes. In particular, meeting or exceeding very high-reliability requirements of communicating processes separated by networks of nontrivial size is more costly than obtaining the required degree of reliability by positive end-to-end acknowledgments and retransmissions (referred to as PAR or ARQ). Put differently, it is far easier to obtain reliability beyond a certain margin by mechanisms in the *end hosts* of a network rather than in the *intermediary nodes*, especially when the latter are beyond the control of, and not accountable to, the former. Positive end-to-end acknowledgments with infinite retries can obtain arbitrarily high reliability from any network with a higher than zero probability of successfully transmitting data from one end to another.

The end-to-end principle does not extend to functions beyond end-to-end error control and correction, and security. E.g., no straightforward end-to-end arguments can be made for communication parameters such as latency and throughput. In a 2001 paper, Blumenthal and Clark note: "[F]rom the beginning, the end-to-end arguments revolved around requirements that could be implemented correctly at the endpoints; if implementation inside the network is the only way to accomplish the requirement, then an end-to-end argument isn't appropriate in the first place."

The end-to-end principle is closely related, and sometimes seen as a direct precursor, to the principle of net neutrality.

## History

In the 1960s, Paul Baran and Donald Davies, in their pre-ARPANET elaborations of networking, made comments about reliability. Baran introduced the concept of virtual circuits in 1962. His report in 1964 states: "Reliability and raw error rates are secondary. The network must be built with the expectation of heavy damage anyway. Powerful error removal methods exist."

Davies was against the concept of virtual circuits. He captured the essence of the end-to-end principle in his 1967 paper, which stated that users of the network will provide themselves with error control: "It is thought that all users of the network will provide themselves with some kind of error control and that without difficulty this could be made to show up a missing packet. Because of this, loss of packets, if it is sufficiently rare, can be tolerated." Davies built the local-area NPL network with a single packet switch and worked on the simulation of wide-area networks.

The ARPANET was the first large-scale general-purpose packet switching network – implementing several of the concepts previously articulated by Baran and Davies. The design, led by Bob Kahn, was based on reliable virtual circuits. The BBN "IMP Guys" developed the routing algorithm, flow control, software design, and network control.

Building on these ideas, Louis Pouzin, with Hubert Zimmermann and others, developed the CYCLADES network. This was the first wide-area network to implement datagrams and make the hosts responsible for the reliable delivery of data, rather than this being a centralized service of the network itself. Concepts implemented in this network feature in TCP/IP architecture.

## Applications

### ARPANET

The ARPANET demonstrated several important aspects of the end-to-end principle.

**Packet switching pushes some logical functions toward the communication endpoints**

If the basic premise of a distributed network is packet switching, then functions such as reordering and duplicate detection inevitably have to be implemented at the logical endpoints of such a network. Consequently, the ARPANET featured two distinct levels of functionality:

1. a lower level concerned with transporting data packets between neighboring network nodes (called Interface Message Processors or IMPs), and
2. a higher level concerned with various end-to-end aspects of the data transmission.

Dave Clark, one of the authors of the end-to-end principle paper, concludes: "The discovery of packets is not a consequence of the end-to-end argument. It is the success of packets that make the end-to-end argument relevant."

**No arbitrarily reliable data transfer without end-to-end acknowledgment and retransmission mechanisms**

The ARPANET was designed to provide reliable data transport between any two endpoints of the network

–

much like a simple I/O channel between a computer and a nearby peripheral device.

In order to remedy any potential failures of packet transmission normal ARPANET messages were handed from one node to the next node with a positive acknowledgment and retransmission scheme; after a successful handover they were then discarded,

no source-to-destination re-transmission in case of

packet loss

was catered for. However, in spite of significant efforts, perfect reliability as envisaged in the initial ARPANET specification turned out to be impossible to provide

–

a reality that became increasingly obvious once the ARPANET grew well beyond its initial four-node topology.

The ARPANET thus provided a strong case for the inherent limits of network-based hop-by-hop reliability mechanisms in pursuit of true end-to-end reliability.

**Trade-off between reliability, latency, and throughput**

The pursuit of perfect reliability may hurt other relevant parameters of a data transmission

–

most importantly latency and throughput. This is particularly important for applications that value predictable throughput and low latency over reliability

–

the classic example being interactive real-time voice applications. This

use case

was catered for in the ARPANET by providing a raw message service that dispensed with various reliability measures so as to provide faster and lower latency data transmission service to the end hosts.

### TCP/IP

Internet Protocol (IP) is a connectionless datagram service with no delivery guarantees. On the Internet, IP is used for nearly all communications. End-to-end acknowledgment and retransmission is the responsibility of the connection-oriented Transmission Control Protocol (TCP), which sits on top of IP. The functional split between IP and TCP exemplifies the proper application of the end-to-end principle to transport protocol design.

### File transfer

An example of the end-to-end principle is that of an arbitrarily reliable file transfer between two endpoints in a distributed network of a varying, nontrivial size: The only way two endpoints can obtain a completely reliable transfer is by transmitting and acknowledging a checksum for the entire data stream; in such a setting, lesser checksum and acknowledgment (ACK/NACK) protocols are justified only for the purpose of optimizing performance – they are useful to the vast majority of clients, but are not enough to fulfill the reliability requirement of this particular application. A thorough checksum is hence best done at the endpoints, and the network maintains a relatively low level of complexity and reasonable performance for all clients.

## Limitations

The most important limitation of the end-to-end principle is that its basic premise, placing functions in the application endpoints rather than in the intermediary nodes, is not trivial to implement.

An example of the limitations of the end-to-end principle exists in mobile devices with mobile IPv6. Pushing service-specific complexity to the endpoints can cause issues with mobile devices if the device has unreliable access to network channels.

Further problems can be seen with a decrease in network transparency from the addition of network address translation (NAT), which IPv4 relies on to combat address exhaustion. With the introduction of IPv6, users once again have unique identifiers, allowing for true end-to-end connectivity. Unique identifiers may be based on a physical address, or can be generated randomly by the host.

The end-to-end principle advocates pushing coordination-related functionality ever higher, ultimately into the application layer. The premise is that application-level information enables flexible coordination between the application endpoints and yields better performance because the coordination would be exactly what is needed. This leads to the idea of modeling each application via its own application-specific protocol that supports the desired coordination between its endpoints while assuming only a simple lower-layer communication service. Broadly, this idea is known as application semantics (meaning).

Multiagent systems offer approaches based on application semantics that enable convenient implementation of distributed applications without requiring message ordering and delivery guarantees from the underlying communication services. A basic idea in these approaches is to model the coordination between application endpoints via an information protocol and then implement the endpoints (agents) based on the protocol. Information protocols can be enacted over lossy, unordered communication services. A middleware based on information protocols and the associated programming model abstracts away message receptions from the underlying network and enables endpoint programmers to focus on the business logic for sending messages.

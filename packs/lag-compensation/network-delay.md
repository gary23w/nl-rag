---
title: "Network delay"
source: https://en.wikipedia.org/wiki/Network_delay
domain: lag-compensation
license: CC-BY-SA-4.0
tags: lag compensation, network lag, latency compensation, clock synchronization netcode
fetched: 2026-07-02
---

# Network delay

**Network delay** is a design and performance characteristic of a telecommunications network. It specifies the latency for a bit of data to travel across the network from one communication endpoint to another. It is typically measured in multiples or fractions of a second. Delay may differ slightly, depending on the location of the specific pair of communicating endpoints. Engineers usually report both the maximum and average delay, and they divide the delay into several parts:

- Processing delay – time it takes a router to process the packet header
- Queuing delay – time the packet spends in routing queues
- Transmission delay – time it takes to push the packet's bits onto the link
- Propagation delay – time for a signal to propagate through the media

A certain minimum level of delay is experienced by signals due to the time it takes to transmit a packet serially through a link. This delay is extended by more variable levels of delay due to network congestion. IP network delays can range from a few milliseconds to several hundred milliseconds.

For example, the hop count between two communication endpoints (such as server and client), may affect network delay.

---
title: "Round-trip delay"
source: https://en.wikipedia.org/wiki/Round-trip_delay
domain: navigation-timing
license: CC-BY-SA-4.0
tags: navigation timing api, page load milestones, performance navigation entry, dom content loaded timing
fetched: 2026-07-02
---

# Round-trip delay

In telecommunications, **round-trip delay** (**RTD**) or **round-trip time** (**RTT**) is the amount of time it takes for a signal to be sent *plus* the amount of time it takes for acknowledgement of that signal having been received. This time delay includes propagation times for the paths between the two communication endpoints. In the context of computer networks, the signal is typically a data packet. RTT is commonly used interchangeably with **ping time**, which can be determined with the ping command. However, ping time may differ from experienced RTT with other protocols since the payload and priority associated with ICMP messages used by ping may differ from that of other traffic.

End-to-end delay is the length of time it takes for a signal to travel in one direction and is often approximated as half the RTT.

## Protocol design

RTT is a measure of the amount of time taken for an entire message to be sent to a destination and for a reply to be sent back to the sender. The time to send the message to the destination in its entirety is known as the network latency, and thus RTT is twice the latency in the network plus a processing delay at the destination. The other sources of delay in a network that make up the network latency are processing delay in transmission, propagation time, transmission time and queueing time. Propagation time is dependent on distance. Transmission time for a message is proportional to the message size divided by the bandwidth. Thus higher bandwidth networks will have lower transmission time, but the propagation time will remain unchanged, and so RTT does fall with increased bandwidth, but the delay increasingly represents propagation time.

Networks with both high bandwidth and a high RTT (and thus high bandwidth-delay product) can have large amounts of data in transit at any given time. Such *long fat networks* require a special protocol design. One example is the TCP window scale option.

The RTT was originally estimated in TCP by:

$\mathrm {RTT} =\alpha \cdot \mathrm {old\_RTT} +(1-\alpha )\cdot \mathrm {new\_round\_trip\_sample}$

where $\alpha$ is constant weighting factor ( $0\leq \alpha <1$ ). Choosing a value for $\alpha$ close to 1 makes the weighted average immune to changes that last a short time (e.g., a single segment that encounters long delay). Choosing a value for $\alpha$ close to 0 makes the weighted average respond to changes in delay very quickly. This was improved by the Jacobson/Karels algorithm, which takes standard deviation into account as well. Once a new RTT is calculated, it is entered into the equation above to obtain an average RTT for that connection, and the procedure continues for every new calculation.

## Wi-Fi

Accurate round-trip time measurements over Wi-Fi using IEEE 802.11mc are the basis for the Wi-Fi positioning system.

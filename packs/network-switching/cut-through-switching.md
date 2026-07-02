---
title: "Cut-through switching"
source: https://en.wikipedia.org/wiki/Cut-through_switching
domain: network-switching
license: CC-BY-SA-4.0
tags: network switching, packet switching, cut-through switching, collision domain
fetched: 2026-07-02
---

# Cut-through switching

In computer networking, **cut-through switching**, also called **cut-through forwarding** is a method for packet switching systems, wherein the switch starts forwarding a frame (or packet) before the whole frame has been received, normally as soon as the destination address and outgoing interface is determined. Compared to store and forward, this technique reduces latency through the switch and relies on the destination devices for error handling. Pure cut-through switching is only possible when the speed of the outgoing interface is at least equal or higher than the incoming interface speed.

Adaptive switching dynamically selects between cut-through and store and forward behaviors based on current network conditions.

Cut-through switching is closely associated with wormhole switching.

## Use in Ethernet

When cut-through switching is used in Ethernet the switch is not able to verify the integrity of an incoming frame before forwarding it.

The technology was developed by Kalpana, the company that introduced the first Ethernet switch.

The primary advantage of cut-through Ethernet switches, compared to store-and-forward Ethernet switches, is lower latency. Cut-through Ethernet switches can support an end-to-end network delay latency of about ten microseconds. End-to-end application latencies below 3 microseconds require specialized hardware such as InfiniBand.

A cut-through switch will forward corrupted frames, whereas a store and forward switch will drop them. **Fragment free** is a variation on cut-through switching that partially addresses this problem by assuring that collision fragments are not forwarded. Fragment free will hold the frame until the first 64 bytes are read from the source to detect a collision before forwarding. This is only useful if there is a chance of a collision on the source port.

The theory here is that frames that are damaged by collisions are often shorter than the minimum valid Ethernet frame size of 64 bytes. With a fragment-free buffer, the first 64 bytes of each frame update the source MAC and port if necessary, provide the destination MAC, and allow forwarding the frame. If the frame is less than 64 bytes, it is discarded. Frames that are smaller than 64 bytes are called runts; this is why fragment-free switching is sometimes called "runt-less" switching. Because the switch only ever buffers 64 bytes of each frame, fragment-free is a faster mode than store-and-forward, but there still exists a risk of forwarding bad frames.

There are certain scenarios that force a cut-through Ethernet switch to buffer the entire frame, acting like a store-and-forward Ethernet switch for that frame:

- Speed: When the outgoing port is faster than the incoming port, the switch must buffer the entire frame received from the lower-speed port before the switch can start transmitting that frame out the high-speed port, to prevent underrun. (When the outgoing port is slower than the incoming port, the switch can perform cut-through switching and start transmitting that frame before it is entirely received, although it must still buffer most of the frame).
- Congestion: When a cut-through switch decides a frame from one incoming port needs to go out through an outgoing port, but that outgoing port is already busy sending a frame from a second incoming port, the switch must buffer some or all of the frame from the first incoming port.

## Use in Fibre Channel

Cut-through switching is the dominant switching architecture in Fibre Channel due to the low-latency performance required for SCSI traffic. Brocade has implemented cut-through switching in its Fibre Channel ASICs since the 1990s and has been implemented in tens of millions of ports in production SANs worldwide. CRC errors are detected in a cut-through switch and indicated by marking the corrupted frame EOF field as "invalid". The destination devices (host or storage) sees the invalid EOF and discards the frame prior to sending it to the application or LUN. Discarding corrupted frames by the destination device is a 100% reliable method for error handling and is mandated by Fibre Channel standards driven by Technical Committee T11. Discarding corrupted frames at the destination device also minimizes the time to recover bad frames. As soon as the destination device receives the EOF marker as "invalid", recovery of the corrupted frame can begin. With store and forward, the corrupted frame is discarded at the switch forcing a SCSI timeout and a SCSI retry for recovery that can result in delays of tens of seconds.

## Use in ATM

Cut-through switching was one of the important features of IP networks using ATM networks since the edge routers of the ATM network were able to use cell switching through the core of the network with low latency at all points. With higher speed links, this has become less of a problem since packet latency has become much smaller.

## Use in InfiniBand

Cut-through switching is very popular in InfiniBand networks, since these are often deployed in environments where latency is a prime concern, such as supercomputer clusters.

## Use in SMTP

A closely allied concept is offered by the Exim mail transfer agent. When operating as a forwarder the onward connection can be made to the destination while the source connection is still open. This permits data-time rejection (due, for example, to content-scanning) by the target MTA to be notified to the source MTA within the SMTP connection, rather than the traditional bounce message necessitated by the more usual store-and-forward operation.

## Use in Bitcoin

Cut-through switching has been applied to make block-relay lower latency in Bitcoin. Low latency is critical for Bitcoin miners to reduce the rate at which their blocks are orphaned.

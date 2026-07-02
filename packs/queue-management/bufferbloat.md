---
title: "Bufferbloat"
source: https://en.wikipedia.org/wiki/Bufferbloat
domain: queue-management
license: CC-BY-SA-4.0
tags: active queue management, weighted fair queueing, random early detection, congestion avoidance
fetched: 2026-07-02
---

# Bufferbloat

**Bufferbloat** is the undesirable latency that comes from a router or other network equipment buffering too many data packets. Bufferbloat can also cause packet delay variation (also known as jitter), as well as reduce the overall network throughput. When a router or switch is configured to use excessively large buffers, even very high-speed networks can become practically unusable for many interactive applications like voice over IP (VoIP), audio streaming, online gaming, and even ordinary web browsing.

Some communications equipment manufacturers designed unnecessarily large buffers into some of their network products. In such equipment, bufferbloat occurs when a network link becomes congested, causing packets to become queued for long periods in these oversized buffers. In a first-in first-out queuing system, overly large buffers result in longer queues and higher latency, and do not improve network throughput. It can also be induced by specific slow-speed connections hindering the on-time delivery of other packets.

The bufferbloat phenomenon was described as early as 1985. It gained more widespread attention starting in 2009.

According to some sources, the most frequent cause of high latency ("lag") in online video games is local home network bufferbloat. High latency can render modern online gaming impossible.

## Buffering

An established rule of thumb for the network equipment manufacturers was to provide buffers large enough to accommodate at least 250 ms of buffering for a stream of traffic passing through a device. For example, a router's Gigabit Ethernet interface would require a relatively large 32 MB buffer. Such sizing of the buffers can lead to failure of the TCP congestion control algorithm. The buffers then take some time to drain, before congestion control resets and the TCP connection ramps back up to speed and fills the buffers again. Bufferbloat thus causes problems such as high and variable latency, and choking network bottlenecks for all other flows as the buffer becomes full of the packets of one TCP stream and other packets are then dropped.

A bloated buffer has an effect only when this buffer is actually used. In other words, oversized buffers have a damaging effect only when the link they buffer becomes a bottleneck. The size of the buffer serving a bottleneck can be measured using the ping utility provided by most operating systems. First, the other host should be pinged continuously; then, a several-second-long download from it should be started and stopped a few times. By design, the TCP congestion avoidance algorithm will rapidly fill up the bottleneck on the route. If downloading (and uploading, respectively) correlates with a direct and important increase in the round-trip time reported by ping, then it demonstrates that the buffer of the current bottleneck in the download (and upload, respectively) direction is bloated. Since the increase in the round-trip time is caused by the buffer on the bottleneck, the maximum increase gives a rough estimation of its size in milliseconds.

In the previous example, using an advanced traceroute tool instead of the simple pinging (for example, MTR) will not only demonstrate the existence of a bloated buffer on the bottleneck, but will also pinpoint its location in the network. Traceroute achieves this by displaying the route (path) and measuring transit delays of packets across the network. The history of the route is recorded as round-trip times of the packets received from each successive host (remote node) in the route (path).

## Mechanism

Most TCP congestion control algorithms rely on measuring the occurrence of packet drops to determine the available bandwidth between two ends of a connection. The algorithms speed up the data transfer until packets start to drop, then slow down the transmission rate. Ideally, they keep adjusting the transmission rate until it reaches an equilibrium speed of the link. So that the algorithms can select a suitable transfer speed, the feedback about packet drops must occur in a timely manner. With a large buffer that has been filled, the packets will arrive at their destination, but with a higher latency. The packets were not dropped, so TCP does not slow down once the uplink has been saturated, further filling the buffer. Newly arriving packets are dropped only when the buffer is fully saturated. Once this happens, TCP may even decide that the path of the connection has changed, and again go into the more aggressive search for a new operating point.

Packets are queued within a network buffer before being transmitted; in problematic situations, packets are dropped only if the buffer is full. On older routers, buffers were fairly small, so they filled quickly, and therefore packets began to drop shortly after the link became saturated, so the TCP protocol could adjust, and the issue would not become apparent. On newer routers, buffers have become large enough to hold several seconds of buffered data. To TCP, a congested link can appear to be operating normally as the buffer fills. The TCP algorithm is unaware that the link is congested and does not start to take corrective action until the buffer finally overflows and packets are dropped.

All packets passing through a simple buffer implemented as a single queue will experience similar delay, so the latency of any connection that passes through a filled buffer will be affected. Available channel bandwidth can also end up being unused, as some fast destinations may not be promptly reached due to buffers clogged with data awaiting delivery to slow destinations. These effects impair the interactivity of applications using other network protocols, including UDP used in latency-sensitive applications like VoIP and online gaming.

## Impact on applications

Regardless of bandwidth requirements, any type of service that requires consistently low latency or jitter-free transmission can be affected by bufferbloat. Such services include digital voice calls (VOIP), online gaming, video chat, and other interactive applications such as radio streaming, video on demand, and remote login.

When the bufferbloat phenomenon is present and the network is under load, even normal web page loads can take many seconds to complete, or simple DNS queries can fail due to timeouts. Actually any TCP connection can timeout and disconnect, and UDP packets can get discarded. Since the continuation of a TCP download stream depends on acknowledgement (ACK) packets in the upload stream, a bufferbloat problem in the upload can cause failure of other non-related download applications, because the client ACK packets do not timely reach the internet server.

## Detection

The DSLReports Speedtest was an easy-to-use test that included a score for bufferbloat. The DSLReports site went fully offline on March 26, 2025. The ICSI Netalyzr was another on-line tool that could be used for checking networks for the presence of bufferbloat, together with checking for many other common configuration problems. The service was shut down in March 2019. In the absence of DSLReports and Netalyzr, current browser-based bufferbloat tests include the Waveform Bufferbloat Test and Y2KDASH, which samples loaded latency continuously rather than in a single-shot test. The bufferbloat.net web site lists tools and procedures for determining whether a connection has excess buffering that will slow it down.

## Solutions and mitigations

Several technical solutions exist which can be broadly grouped into two categories: solutions that target the network and solutions that target the endpoints. The two types of solutions are often complementary. The problem sometimes arrives with a combination of fast and slow network paths.

Network solutions generally take the form of queue management algorithms. This type of solution has been the focus of the IETF AQM working group. Notable examples include:

- Limiting the IP queue length, see TCP tuning
- AQM algorithms such as CoDel and PIE.
- Hybrid AQM and packet scheduling algorithms such as FQ-CoDel.
- Amendments to the DOCSIS standard to enable smarter buffer control in cable modems.
- Integration of queue management (FQ-CoDel) into the Wi-Fi subsystem of the Linux operating system as Linux is commonly used in wireless access points.

Notable examples of solutions targeting the endpoints are:

- The BBR congestion control algorithm for TCP.
- The Micro Transport Protocol employed by many BitTorrent clients.
- Techniques for using fewer connections, such as HTTP pipelining or HTTP/2 instead of the plain HTTP protocol.

The problem may also be mitigated by reducing the buffer size on the OS and network hardware; however, this is often not configurable, and optimal buffer size is dependent on line rate, which may differ for different destinations.

Utilizing DiffServ (and employing multiple priority-based queues) helps in prioritizing transmission of low-latency traffic (such as VoIP, videoconferencing, gaming), relegating dealing with congestion and bufferbloat onto non-prioritized traffic.

## Optimal buffer size

For the longest delay TCP connections to still get their fair share of the bandwidth, the buffer size should be at least the bandwidth-delay product divided by the square root of the number of simultaneous streams. A typical rule of thumb is 50 ms of line rate data, but some popular consumer grade switches only have 1 ms, which may result in extra bandwidth loss on the longer delay connections in case of local contention with others.

---
title: "CoDel"
source: https://en.wikipedia.org/wiki/CoDel
domain: active-queue-management
license: CC-BY-SA-4.0
tags: active queue management, random early detection, controlled delay, weighted fair queueing
fetched: 2026-07-02
---

# CoDel

**CoDel** (*Controlled Delay*; pronounced "coddle") is an active queue management (AQM) algorithm in network routing, developed by Van Jacobson and Kathleen Nichols and published as RFC8289. It is designed to overcome bufferbloat in networking hardware, such as routers, by setting limits on the delay network packets experience as they pass through buffers in this equipment. CoDel aims to improve on the overall performance of the random early detection (RED) algorithm by addressing some of its fundamental misconceptions, as perceived by Jacobson, and by being easier to manage.

In 2012, an implementation of CoDel was written by Dave Täht and Eric Dumazet for the Linux kernel and dual licensed under the GNU General Public License and the 3-clause BSD license. Dumazet's improvement on CoDel is called FQ-CoDel, standing for "Fair/Flow Queue CoDel"; it was first adopted as the standard AQM and packet scheduling solution in 2014 in the OpenWrt 14.07 release called "Barrier Breaker". From there, CoDel and FQ-CoDel have migrated into various downstream projects such as Tomato, dd-wrt, OPNsense and Ubiquiti's "Smart Queues" feature.

## Theory

CoDel is based on observations of packet behavior in packet-switched networks under the influence of data buffers. Some of these observations are about the fundamental nature of queueing and the causes of bufferbloat, others relate to weaknesses of alternative queue management algorithms. CoDel was developed as an attempt to address the problem of bufferbloat.

### Bufferbloat

The flow of packets slows down while traveling through a network link between a fast and a slow network, especially at the start of a TCP session, when there is a sudden burst of packets and the slower network may not be able to accept the burst quickly enough. Buffers exist to ease this problem by giving the fast network a place to store packets to be read by the slower network at its own pace. In other words, buffers act like shock absorbers to convert bursty arrivals into smooth, steady departures. However, a buffer has limited capacity. The ideal buffer is sized so it can handle a sudden burst of communication and match the speed of that burst to the speed of the slower network. Ideally, the shock-absorbing situation is characterized by a temporary delay for packets in the buffer during the transmission burst, after which the delay rapidly disappears and the network reaches a balance in offering and handling packets.

The TCP congestion control algorithm relies on packet drops to determine the available bandwidth between two communicating devices. It speeds up the data transfer until packets start to drop, and then slows down the transmission rate. Ideally, it keeps speeding up and slowing down as it finds equilibrium at the speed of the link. For this to work, the packet drops must occur in a timely manner so that the algorithm can responsively select a suitable transfer speed. With packets held in an overly-large buffer, the packets will arrive at their destination but with a higher latency but no packets are dropped so TCP does not slow down. Under these conditions, TCP may even decide that the path of the connection has changed and repeat the search for a new equilibrium.

Having a big and constantly full buffer that causes increased transmission delays and reduced interactivity, especially when looking at two or more simultaneous transmissions over the same channel, is called bufferbloat. Available channel bandwidth can also end up being unused, as some fast destinations may not be reached due to buffers being clogged with data awaiting delivery to slow destinations.

### Good and bad queues

CoDel distinguishes between two types of queue: A *good queue* is one that exhibits no bufferbloat. Communication bursts cause no more than a temporary increase in queue delay. The network link utilization is maximized. A *bad queue* exhibits bufferbloat. Communication bursts cause the buffer to fill up and stay filled, resulting in low utilization and a constantly high buffer delay. In order to be effective against bufferbloat, a solution in the form of an active queue management (AQM) algorithm must be able to recognize an occurrence of bufferbloat and react by deploying effective countermeasures.

Van Jacobson asserted in 2006 that existing algorithms have been using incorrect means of recognizing bufferbloat. Algorithms like RED measure the average queue length and consider it a case of bufferbloat if the average grows too large. Jacobson demonstrated in 2006 that this measurement is not a good metric, as the average queue length rises sharply in the case of a communications burst. The queue can then dissipate quickly (good queue) or become a standing queue (bad queue). Other factors in network traffic can also cause false positives or negatives, causing countermeasures to be deployed unnecessarily. Jacobson suggested that average queue length actually contains no information at all about packet demand or network load. He suggested that a better metric might be the minimum queue length during a sliding time window.

## Algorithm

Based on Jacobson's notion from 2006, CoDel was developed to manage queues under control of the minimum delay experienced by packets in the running buffer window. The goal is to keep this minimum delay below 5 milliseconds. If the minimum delay rises to too high a value, packets are dropped from the queue until the delay drops below the maximum level. Nichols and Jacobson cite several advantages to using nothing more than this metric:

- CoDel is parameterless. One of the weaknesses in the RED algorithm (according to Jacobson) is that it is too difficult to configure, especially in an environment with dynamic link rates.
- CoDel treats good queue and bad queue differently. A good queue has low delays by nature, so the management algorithm can ignore it, while a bad queue is subject to management intervention in the form of dropping packets.
- CoDel works off of a parameter that is determined completely locally; It is independent of round-trip delays, link rates, traffic loads and other factors that cannot be controlled or predicted by the local buffer.
- The local minimum delay can only be determined when a packet leaves the buffer, so no extra delay is needed to run the queue to collect statistics to manage the queue.
- CoDel adapts to dynamically changing link rates with no negative impact on utilization.
- The CoDel implementation is relatively simple and therefore can span the spectrum from low-end home routers to high-end routing solutions.

CoDel does nothing to manage the buffer if the minimum delay for the buffer window is below the maximum allowed value. It also does nothing if the buffer is relatively empty (if there are fewer than one MTU's worth of bytes in the buffer). If these conditions do not hold, then CoDel drops packets probabilistically.

The algorithm is independently computed at each network hop. The algorithm operates over an *interval*, initially 100 milliseconds. Per-packet queuing delay is monitored through the hop. As each packet is dequeued for forwarding, the queuing delay (amount of time the packet spent waiting in the queue) is calculated. The lowest queuing delay for the interval is stored. When the last packet of the interval is dequeued, if the lowest queuing delay for the interval is greater than 5 milliseconds, this single packet is dropped and the interval used for the next group of packets is shortened. If the lowest queuing delay for the interval is less than 5 milliseconds, the packet is forwarded and the interval is reset to 100 milliseconds.

When the interval is shortened, it is done so in accordance with the inverse square root of the number of successive intervals in which packets were dropped due to excessive queuing delay. The sequence of intervals is $100$ , ${100 \over {\sqrt {2}}}$ , ${100 \over {\sqrt {3}}}$ , ${100 \over {\sqrt {4}}}$ , ${100 \over {\sqrt {5}}}$ ...

## Simulation results

CoDel has been tested in simulation tests by Nichols and Jacobson, at different MTUs and link rates and other variations of conditions. In general, results indicate:

- In comparison to RED, CoDel keeps the packet delay closer to the target value across the full range of bandwidths (from 3 to 100 Mbit/s). The measured link utilizations are consistently near 100% of link bandwidth.
- At lower MTU, packet delays are lower than at higher MTU. Higher MTU results in good link utilization, lower MTU results in good link utilization at lower bandwidth, degrading to fair utilization at high bandwidth.

Simulation was also performed by Greg White and Joey Padden at CableLabs.

## Implementation

A full implementation of CoDel was realized in May 2012 and made available as open-source software. It was implemented within the Linux kernel (starting with the 3.5 mainline). Dave Täht back-ported CoDel to Linux kernel 3.3 for project CeroWrt, which concerns itself among other things with bufferbloat, where it was exhaustively tested. CoDel began to appear as an option in some proprietary/turnkey bandwidth management platforms in 2013. FreeBSD had CoDel integrated into the 11.x and 10.x code branches in 2016. An implementation is distributed with OpenBSD since version 6.2.

## Derived algorithms

Fair/Flow Queue CoDel (FQ-CoDel; fq_codel in Linux code) adds flow queuing to CoDel so that it differentiates between multiple simultaneous connections and works fairly. It gives the first packet in each stream priority, so that small streams can start and finish quickly for better use of network resources. CoDel co-author Van Jacobson recommends the use of fq_codel over codel where it's available. FQ-CoDel is published as RFC8290. It is written by T. Hoeiland-Joergensen, P. McKenney, D. Täht, J. Gettys, and E. Dumazet, all members of the "bufferbloat project".

Common Applications Kept Enhanced (CAKE; sch_cake in Linux code) is a combined traffic shaper and AQM algorithm presented by the bufferbloat project in 2018. It builds on the experience of using fq_codel with the HTB (Hierarchy Token Bucket) traffic shaper. It improves over the Linux htb+fq_codel implementation by reducing hash collisions between flows, reducing CPU utilization in traffic shaping, and in a few other ways.

In 2022, Dave Täht reviewed the state of fq_codel and sch_cake implementations in the wild. He found that while many systems have switched to either as the default AQM, several implementations have dubious deviations from the standard. For example, Apple's implementation of fq_codel (default in iOS) has a very large number of users but no "codel" component. Täht also notes the general lack of hardware offloading, made more important by the increase in network traffic brought by the COVID-19 pandemic.
